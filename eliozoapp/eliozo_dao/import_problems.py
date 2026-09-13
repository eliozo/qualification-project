"""Import olympiad problems from external Git problem repositories.

The repositories to publish are listed in ``eliozoapp/problem_repositories.json``
(this replaces the published Google Sheet that used to list the Markdown files).
For every configured repository the importer

  1. resolves a working copy: the configured ``local_checkout`` when it exists,
     otherwise a shallow, sparse clone of ``git_url`` kept under
     ``eliozoapp/data/problem_repos/<name>``;
  2. finds ``<problembase>/<olympiad>/<event>/content_<lang>.md`` in each listed
     olympiad, skipping ``exclude_events`` from the olympiad's ``config.json``
     and from the repository entry. The file in the olympiad's ``default_lang``
     is the master; other languages are translations;
  3. converts each file to ``<event>-content_<lang>.ttl`` in the output directory
     using the converter from the sibling ``worksheet-generation-with-llms``
     checkout, and rejects files that yield no problems;
  4. copies the images of every published event into one flat directory, which
     Flask serves as ``/static/eliozo/images/`` when ``USE_REMOTE_STATIC`` is off.

Usage:
    python -m eliozo_dao.import_problems [--source auto|local|git]
                                         [--images-dir DIR | --no-images]

Afterwards rebuild the store with ``python -m eliozo_dao.load_rdf``.

Environment overrides: ``ELIOZO_PROBLEM_REPOS`` (config file),
``ELIOZO_IMAGES_DIR`` (image destination), ``WORKSHEET_GENERATION_ROOT``
(checkout that provides the Markdown-to-Turtle converter).
"""

from __future__ import annotations

import argparse
import filecmp
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from dataclasses import dataclass, field
from glob import glob

_APP_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

DEFAULT_CONFIG = os.path.join(_APP_ROOT, "problem_repositories.json")
PROBLEM_TTL_DIR = os.path.join(_APP_ROOT, "data", "problem_ttl")
REPO_CACHE_DIR = os.path.join(_APP_ROOT, "data", "problem_repos")
DEFAULT_IMAGES_DIR = os.path.join(_APP_ROOT, "eliozo", "static", "eliozo", "images")
DEFAULT_WORKSHEET_ROOT = os.path.normpath(
    os.path.join(_APP_ROOT, "..", "..", "worksheet-generation-with-llms"))

CONTENT_FILE_RE = re.compile(r"^content_([a-z]{2})\.md$")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".svg")
IMAGE_REF_RE = re.compile(r"!\[[^\]]*\]\(([^()\s/\\]+\.(?:png|jpe?g|gif|svg))\)", re.IGNORECASE)
REPO_NAME_RE = re.compile(r"^[A-Za-z0-9._-]+$")

RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
ELIOZO_PROBLEM = "http://www.dudajevagatve.lv/eliozo#Problem"


@dataclass
class RepoConfig:
    name: str
    git_url: str | None
    branch: str
    local_checkout: str | None
    problembase: str
    olympiads: list[str]
    exclude_events: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ContentFile:
    olympiad: str
    event: str
    lang: str
    is_master: bool
    path: str

    @property
    def ttl_name(self):
        return f"{self.event}-content_{self.lang}.ttl"


@dataclass
class Discovery:
    content_files: list[ContentFile] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def load_config(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    base = os.path.dirname(os.path.abspath(path))
    repos = []
    for entry in data.get("repositories", []):
        name = entry.get("name", "")
        if not REPO_NAME_RE.match(name):
            raise ValueError(f"{path}: repository name {name!r} must match {REPO_NAME_RE.pattern}")
        if not entry.get("olympiads"):
            raise ValueError(f"{path}: repository {name!r} lists no 'olympiads'")
        if not entry.get("git_url") and not entry.get("local_checkout"):
            raise ValueError(f"{path}: repository {name!r} needs 'git_url' and/or 'local_checkout'")
        local = entry.get("local_checkout")
        repos.append(RepoConfig(
            name=name,
            git_url=entry.get("git_url"),
            branch=entry.get("branch", "master"),
            local_checkout=os.path.normpath(os.path.join(base, os.path.expanduser(local))) if local else None,
            problembase=entry.get("problembase", "problembase"),
            olympiads=list(entry["olympiads"]),
            exclude_events=list(entry.get("exclude_events", [])),
        ))
    if not repos:
        raise ValueError(f"{path}: no repositories configured")
    return repos


# --------------------------------------------------------------------------- #
#  Working copies
# --------------------------------------------------------------------------- #

def resolve_checkout(repo, source, cache_dir=REPO_CACHE_DIR):
    """Return the directory holding the repository's files."""
    local = repo.local_checkout
    if source != "git" and local and os.path.isdir(local):
        print(f"[{repo.name}] using local checkout {local} (uncommitted edits included)")
        return local
    if source == "local":
        raise RuntimeError(f"[{repo.name}] local checkout not found: {local}")
    if not repo.git_url:
        raise RuntimeError(f"[{repo.name}] local checkout {local} not found and no git_url to clone")
    return sync_git_checkout(repo, os.path.join(cache_dir, repo.name))


def _git(*args):
    print("  $ git " + " ".join(args))
    subprocess.run(["git", *args], check=True)


def _rmtree(path):
    # Git marks pack files read-only, which makes a plain rmtree fail on Windows.
    def make_writable_and_retry(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=make_writable_and_retry)
    else:
        shutil.rmtree(path, onerror=make_writable_and_retry)


def sync_git_checkout(repo, target):
    """Clone or update a shallow, sparse, blob-less copy of the olympiad dirs.

    A problem repository can be much larger than its olympiad directories
    (kapsitis/math is ~550 MB at HEAD, its problembase ~100 MB), so only the
    configured paths are ever downloaded. Needs git >= 2.27.
    """
    sparse_paths = [f"{repo.problembase}/{o}" for o in repo.olympiads]
    if os.path.isdir(os.path.join(target, ".git")):
        origin = subprocess.run(["git", "-C", target, "remote", "get-url", "origin"],
                                capture_output=True, text=True).stdout.strip()
        if origin != repo.git_url:
            print(f"[{repo.name}] cached clone points at {origin!r}; cloning afresh")
            _rmtree(target)

    if os.path.isdir(os.path.join(target, ".git")):
        print(f"[{repo.name}] updating {target} to {repo.git_url} ({repo.branch})")
        _git("-C", target, "fetch", "--depth", "1", "--filter=blob:none", "origin", repo.branch)
        _git("-C", target, "reset", "--hard", "FETCH_HEAD")
        _git("-C", target, "clean", "-ffdx")
    else:
        if os.path.exists(target):
            _rmtree(target)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        print(f"[{repo.name}] cloning {repo.git_url} ({repo.branch}) into {target}")
        _git("clone", "--depth", "1", "--filter=blob:none", "--sparse",
             "--branch", repo.branch, repo.git_url, target)
    _git("-C", target, "sparse-checkout", "set", *sparse_paths)
    return target


# --------------------------------------------------------------------------- #
#  Discovery
# --------------------------------------------------------------------------- #

def read_olympiad_config(olympiad_dir):
    path = os.path.join(olympiad_dir, "config.json")
    if not os.path.isfile(path):
        raise ValueError(f"{path} is missing; it must define at least 'default_lang'")
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)
    if not cfg.get("default_lang"):
        raise ValueError(f"{path} does not define 'default_lang'")
    return cfg


def _find_images(event_dir):
    found = []
    for dirpath, _dirnames, filenames in os.walk(event_dir):
        found.extend(os.path.join(dirpath, n) for n in filenames
                     if n.lower().endswith(IMAGE_EXTENSIONS))
    return sorted(found)


def _missing_image_refs(content_files, images):
    available = {os.path.basename(p) for p in images}
    warnings = []
    for cf in content_files:
        with open(cf.path, encoding="utf-8") as f:
            refs = IMAGE_REF_RE.findall(f.read())
        for ref in dict.fromkeys(refs):
            if ref not in available:
                warnings.append(f"{cf.olympiad}/{cf.event}/content_{cf.lang}.md references "
                                f"{ref}, which is not in the event directory")
    return warnings


def discover(checkout, repo):
    result = Discovery()
    for olympiad in repo.olympiads:
        olympiad_dir = os.path.join(checkout, repo.problembase, olympiad)
        if not os.path.isdir(olympiad_dir):
            raise ValueError(f"[{repo.name}] olympiad directory not found: {olympiad_dir}")
        cfg = read_olympiad_config(olympiad_dir)
        default_lang = cfg["default_lang"]
        excluded = set(cfg.get("exclude_events", [])) | set(repo.exclude_events)

        for event in sorted(os.listdir(olympiad_dir)):
            event_dir = os.path.join(olympiad_dir, event)
            if event in excluded or not os.path.isdir(event_dir):
                continue
            found = []
            for name in sorted(os.listdir(event_dir)):
                m = CONTENT_FILE_RE.match(name)
                if m:
                    found.append(ContentFile(olympiad, event, m.group(1),
                                             m.group(1) == default_lang,
                                             os.path.join(event_dir, name)))
            if not found:
                continue
            if not any(cf.is_master for cf in found):
                result.warnings.append(
                    f"{olympiad}/{event}: no content_{default_lang}.md, so its translations "
                    "are imported without problem metadata")
            images = _find_images(event_dir)
            result.content_files.extend(found)
            result.images.extend(images)
            result.warnings.extend(_missing_image_refs(found, images))
    return result


# --------------------------------------------------------------------------- #
#  Conversion and images
# --------------------------------------------------------------------------- #

def load_converter(worksheet_root):
    """Import ``markdown_md_to_turtle`` from a worksheet-generation-with-llms checkout."""
    if not os.path.isfile(os.path.join(worksheet_root, "scripts", "markdown_proc", "mdchunk_reader.py")):
        raise RuntimeError(
            f"Markdown-to-Turtle converter not found under {worksheet_root}. Check out "
            "worksheet-generation-with-llms next to qualification-project or set "
            "WORKSHEET_GENERATION_ROOT.")
    if worksheet_root not in sys.path:
        sys.path.insert(0, worksheet_root)
    from scripts.markdown_proc.mdchunk_reader import markdown_md_to_turtle
    return markdown_md_to_turtle


def count_problems(ttl_path):
    from pyoxigraph import NamedNode, RdfFormat, parse

    rdf_type, problem = NamedNode(RDF_TYPE), NamedNode(ELIOZO_PROBLEM)
    return sum(1 for t in parse(path=ttl_path, format=RdfFormat.TURTLE)
               if t.predicate == rdf_type and t.object == problem)


def convert_all(content_files, output_dir, converter):
    """Write one TTL per content file into a freshly emptied output_dir.

    Returns a list of failure messages; a file that fails or yields no
    problems leaves no TTL behind, so load_rdf never sees a partial result.
    """
    os.makedirs(output_dir, exist_ok=True)
    for stale in glob(os.path.join(output_dir, "*.ttl")):
        os.remove(stale)

    failures = []
    written = {}
    for cf in content_files:
        if cf.ttl_name in written:
            failures.append(f"{cf.path}: output {cf.ttl_name} clashes with {written[cf.ttl_name]}")
            continue
        ttl_path = os.path.join(output_dir, cf.ttl_name)
        try:
            converter(cf.path, ttl_path, cf.lang, cf.is_master)
            n = count_problems(ttl_path)
        except Exception as exc:  # the converter can raise anything on bad Markdown
            n, error = 0, f"{type(exc).__name__}: {exc}"
        else:
            error = "no '# <lo-sample/> ...' problem headings found"
        if n == 0:
            if os.path.exists(ttl_path):
                os.remove(ttl_path)
            failures.append(f"{cf.path}: {error}")
            continue
        written[cf.ttl_name] = cf.path
        kind = "" if cf.is_master else "  (translation)"
        print(f"  {cf.ttl_name:36} {n:4} problems{kind}")
    return failures


def copy_images(images, dest_dir):
    """Copy images into one flat directory.

    Returns ``(copied, unchanged, conflicts)``. Files already identical in
    dest_dir are left alone; nothing is ever deleted from dest_dir.
    """
    os.makedirs(dest_dir, exist_ok=True)
    copied = unchanged = 0
    conflicts = []
    source_of = {}
    for src in images:
        name = os.path.basename(src)
        if name in source_of:
            if not filecmp.cmp(src, source_of[name], shallow=False):
                conflicts.append(f"{name}: {src} differs from {source_of[name]}, which was used")
            continue
        source_of[name] = src
        target = os.path.join(dest_dir, name)
        if os.path.isfile(target) and filecmp.cmp(src, target, shallow=False):
            unchanged += 1
            continue
        shutil.copy2(src, target)
        copied += 1
    return copied, unchanged, conflicts


# --------------------------------------------------------------------------- #
#  CLI
# --------------------------------------------------------------------------- #

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config", default=os.environ.get("ELIOZO_PROBLEM_REPOS", DEFAULT_CONFIG),
                        help="Repository list (default: %(default)s)")
    parser.add_argument("--source", choices=["auto", "local", "git"], default="auto",
                        help="auto: local_checkout if present, else clone (default); "
                             "local: only local checkouts; git: always clone/update git_url")
    parser.add_argument("--output", default=PROBLEM_TTL_DIR,
                        help="Directory for the generated TTL files (default: %(default)s)")
    images = parser.add_mutually_exclusive_group()
    images.add_argument("--images-dir", default=os.environ.get("ELIOZO_IMAGES_DIR", DEFAULT_IMAGES_DIR),
                        help="Flat directory to copy problem images into (default: %(default)s)")
    images.add_argument("--no-images", action="store_true", help="Do not copy images")
    args = parser.parse_args(argv)

    try:
        repos = load_config(args.config)
        converter = load_converter(os.environ.get("WORKSHEET_GENERATION_ROOT", DEFAULT_WORKSHEET_ROOT))
        found = Discovery()
        for repo in repos:
            checkout = resolve_checkout(repo, args.source)
            d = discover(checkout, repo)
            print(f"[{repo.name}] {len(d.content_files)} content file(s), {len(d.images)} image(s)")
            found.content_files.extend(d.content_files)
            found.images.extend(d.images)
            found.warnings.extend(d.warnings)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"converting {len(found.content_files)} file(s) into {args.output}")
    failures = convert_all(found.content_files, args.output, converter)

    if not args.no_images:
        copied, unchanged, conflicts = copy_images(found.images, args.images_dir)
        print(f"images: {copied} copied, {unchanged} unchanged -> {args.images_dir}")
        found.warnings.extend(conflicts)

    for w in found.warnings:
        print(f"warning: {w}", file=sys.stderr)
    for f in failures:
        print(f"FAILED: {f}", file=sys.stderr)
    if failures:
        print(f"{len(failures)} file(s) failed; see above", file=sys.stderr)
        return 1
    print("done. Now rebuild the store: python -m eliozo_dao.load_rdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
