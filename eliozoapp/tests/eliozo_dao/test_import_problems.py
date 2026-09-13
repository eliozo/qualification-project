"""Tests for eliozo_dao.import_problems (repository config, discovery, images).

Everything except the last test runs on a synthetic problem repository in
tmp_path; the conversion test needs the sibling worksheet-generation-with-llms
checkout and is skipped without it.
"""

import json
import os

import pytest

from eliozo_dao import import_problems as ip

PROBLEM_MD = """# <lo-sample/> LV.VOL.2025.9.1

Problem text.

![1. att.](LV.VOL.2025.9.1A.png)

![](LV.VOL.2025.9.1B.png)

## Atrisinājums

Solution text.
"""


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def problem_repo(tmp_path):
    vol = tmp_path / "math" / "problembase" / "LV.VOL"
    _write(vol / "config.json", json.dumps({"default_lang": "lv", "exclude_events": ["lv-vol-2000"]}))
    _write(vol / "lv-vol-2025" / "content_lv.md", PROBLEM_MD)
    _write(vol / "lv-vol-2025" / "content_en.md", "# <lo-sample/> LV.VOL.2025.9.1\n\nEnglish.\n")
    _write(vol / "lv-vol-2025" / "content_lv2.md", "not a content file")
    _write(vol / "lv-vol-2025" / "VOL_75_uzd_atr.md", "not a content file")
    (vol / "lv-vol-2025" / "LV.VOL.2025.9.1A.png").write_bytes(b"A")
    _write(vol / "lv-vol-2000" / "content_lv.md", "excluded by the olympiad config")
    (vol / "lv-vol-2000" / "LV.VOL.2000.9.1.png").write_bytes(b"old")
    _write(vol / "lv-vol-2001" / "content_lv.md", "excluded by the repository entry")
    (vol / "no-content-yet").mkdir()
    return tmp_path / "math"


def _repo(checkout, **overrides):
    values = dict(name="test", git_url=None, branch="master", local_checkout=str(checkout),
                  problembase="problembase", olympiads=["LV.VOL"], exclude_events=["lv-vol-2001"])
    values.update(overrides)
    return ip.RepoConfig(**values)


def test_load_config_resolves_local_checkout_against_config_dir(tmp_path):
    cfg = tmp_path / "app" / "repos.json"
    _write(cfg, json.dumps({"repositories": [
        {"name": "math", "git_url": "https://example.org/math.git",
         "local_checkout": "../math", "olympiads": ["LV.VOL"]}]}))

    [repo] = ip.load_config(str(cfg))

    assert repo.local_checkout == os.path.normpath(str(tmp_path / "math"))
    assert (repo.branch, repo.problembase, repo.exclude_events) == ("master", "problembase", [])


@pytest.mark.parametrize("entry", [
    {"name": "math", "git_url": "https://example.org/math.git"},
    {"name": "math", "olympiads": ["LV.VOL"]},
    {"name": "../escape", "git_url": "https://example.org/math.git", "olympiads": ["LV.VOL"]},
])
def test_load_config_rejects_incomplete_entries(tmp_path, entry):
    cfg = tmp_path / "repos.json"
    _write(cfg, json.dumps({"repositories": [entry]}))
    with pytest.raises(ValueError):
        ip.load_config(str(cfg))


def test_shipped_config_is_valid():
    repos = ip.load_config(ip.DEFAULT_CONFIG)
    assert all(r.git_url for r in repos)


def test_discover_finds_master_and_translation_and_honours_exclusions(problem_repo):
    found = ip.discover(str(problem_repo), _repo(problem_repo))

    assert [(c.event, c.lang, c.is_master) for c in found.content_files] == [
        ("lv-vol-2025", "en", False),
        ("lv-vol-2025", "lv", True),
    ]
    assert [c.ttl_name for c in found.content_files] == [
        "lv-vol-2025-content_en.ttl", "lv-vol-2025-content_lv.ttl"]
    assert [os.path.basename(p) for p in found.images] == ["LV.VOL.2025.9.1A.png"]


def test_discover_warns_about_image_references_without_a_file(problem_repo):
    found = ip.discover(str(problem_repo), _repo(problem_repo))
    assert len(found.warnings) == 1
    assert "LV.VOL.2025.9.1B.png" in found.warnings[0]


def test_discover_rejects_unknown_olympiad(problem_repo):
    with pytest.raises(ValueError, match="LV.XYZ"):
        ip.discover(str(problem_repo), _repo(problem_repo, olympiads=["LV.XYZ"]))


def test_resolve_checkout_uses_existing_local_checkout(problem_repo):
    assert ip.resolve_checkout(_repo(problem_repo), "auto") == str(problem_repo)


def test_resolve_checkout_local_mode_requires_the_checkout(tmp_path):
    with pytest.raises(RuntimeError, match="not found"):
        ip.resolve_checkout(_repo(tmp_path / "absent"), "local")


def test_copy_images_skips_identical_files_and_reports_conflicts(tmp_path):
    a1, a2, b = tmp_path / "e1" / "A.png", tmp_path / "e2" / "A.png", tmp_path / "e1" / "B.png"
    for path, data in [(a1, b"one"), (a2, b"two"), (b, b"bee")]:
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(data)
    dest = tmp_path / "images"

    copied, unchanged, conflicts = ip.copy_images([str(a1), str(a2), str(b)], str(dest))
    assert (copied, unchanged, len(conflicts)) == (2, 0, 1)
    assert (dest / "A.png").read_bytes() == b"one"

    copied, unchanged, _ = ip.copy_images([str(a1), str(b)], str(dest))
    assert (copied, unchanged) == (0, 2)


@pytest.mark.skipif(
    not os.path.isdir(os.path.join(ip.DEFAULT_WORKSHEET_ROOT, "scripts", "markdown_proc")),
    reason="worksheet-generation-with-llms checkout not found")
def test_convert_all_writes_ttl_and_rejects_files_without_problems(problem_repo, tmp_path):
    converter = ip.load_converter(ip.DEFAULT_WORKSHEET_ROOT)
    event_dir = problem_repo / "problembase" / "LV.VOL" / "lv-vol-2025"
    not_found = tmp_path / "404" / "content_lv.md"
    _write(not_found, "404: Not Found")
    files = [
        ip.ContentFile("LV.VOL", "lv-vol-2025", "lv", True, str(event_dir / "content_lv.md")),
        ip.ContentFile("LV.VOL", "lv-vol-2026", "lv", True, str(not_found)),
    ]
    out = tmp_path / "ttl"
    out.mkdir()
    (out / "stale-content_lv.ttl").write_text("stale", encoding="utf-8")

    failures = ip.convert_all(files, str(out), converter)

    assert sorted(os.listdir(out)) == ["lv-vol-2025-content_lv.ttl"]
    assert ip.count_problems(str(out / "lv-vol-2025-content_lv.ttl")) == 1
    assert len(failures) == 1 and "404" in failures[0]
