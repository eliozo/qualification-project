"""Pārklājuma heiristikas (v1 — leksiska sakritība).

Katram programmas SR meklē sakritību OL_<nr> materiālu failos: SR teksta
saturvārdus salīdzina ar failu sadaļām (Markdown virsraksti). Semantiskā
(embedding) meklēšana ir v2 ideja un šeit netiek lietota.

Manuālas korekcijas: `coverage_overrides.yaml`, atslēga = programmas SR `id`.
"""

from __future__ import annotations

import re
import unicodedata
from functools import lru_cache
from pathlib import Path

try:
    import yaml
except ImportError:  # pārrakstīšanas fails nav obligāts
    yaml = None

# Sliekšņi: saturvārdu daļa, kas atrodama vienā materiāla sadaļā.
SLIEKSNIS_PILNS = 0.70
SLIEKSNIS_DALEJS = 0.45
SLIEKSNIS_PIEMINETS = 0.25

MAX_VIETAS = 3
FRAGMENTA_GARUMS = 240

# Latviešu palīgvārdi + programmas SR biežākie darbības vārdi, kas nešķir SR.
STOPVARDI = {
    "arī", "bet", "gan", "jeb", "kas", "kad", "kur", "kāda", "kādu", "kāds",
    "lai", "lieto", "lietot", "nav", "par", "pēc", "piemēram", "pie", "starp",
    "tai", "tas", "tie", "tml", "to", "tos", "tā", "tās", "un", "uz", "vai",
    "var", "veids", "veidu", "vienā", "citu", "viena", "dažādus", "dažādi",
    "konkrētos", "piemēros", "izmantojot", "situācijas", "kontekstu", "skaitā",
}

MIN_VARDA_GARUMS = 5


def _normalize(teksts: str) -> str:
    teksts = unicodedata.normalize("NFC", teksts.lower())
    return re.sub(r"\s+", " ", teksts)


def _saturvardi(teksts: str) -> set[str]:
    """Saturvārdu celmi (nogriež latviešu galotnes, lai locījumi sakristu)."""
    celmi = set()
    for vards in re.findall(r"[a-zāčēģīķļņōŗšūž]+", _normalize(teksts)):
        if len(vards) < MIN_VARDA_GARUMS or vards in STOPVARDI:
            continue
        celmi.add(vards[: max(MIN_VARDA_GARUMS, len(vards) - 2)])
    return celmi


@lru_cache(maxsize=None)
def _sadalas(celš: Path) -> tuple[tuple[str, str, frozenset], ...]:
    """Sadala materiāla failu sadaļās pēc Markdown virsrakstiem."""
    try:
        saturs = celš.read_text(encoding="utf-8")
    except OSError:
        return ()

    sadalas: list[tuple[str, list[str]]] = [("(faila sākums)", [])]
    for rinda in saturs.splitlines():
        if m := re.match(r"^#{1,6}\s+(.+?)\s*$", rinda):
            sadalas.append((m.group(1), []))
        elif m := re.match(r"^\*\*(.{3,80}?)\*\*\s*$", rinda):
            sadalas.append((m.group(1), []))
        else:
            sadalas[-1][1].append(rinda)

    rezultats = []
    for virsraksts, rindas in sadalas:
        teksts = _normalize(" ".join(rindas))
        if len(teksts) < 40:
            continue
        rezultats.append((virsraksts, teksts, frozenset(_saturvardi(teksts))))
    return tuple(rezultats)


def _fragments(teksts: str, celmi: set[str]) -> str:
    """Izvelk fragmentu ap pirmo sakrītošo saturvārdu."""
    pozicija = 0
    for celms in sorted(celmi, key=len, reverse=True):
        if (p := teksts.find(celms)) >= 0:
            pozicija = p
            break
    sakums = max(0, pozicija - FRAGMENTA_GARUMS // 3)
    gabals = teksts[sakums: sakums + FRAGMENTA_GARUMS].strip()
    return ("…" if sakums else "") + gabals + ("…" if sakums + FRAGMENTA_GARUMS < len(teksts) else "")


def _statuss(dala: float) -> str:
    if dala >= SLIEKSNIS_PILNS:
        return "pilns"
    if dala >= SLIEKSNIS_DALEJS:
        return "dalejs"
    if dala >= SLIEKSNIS_PIEMINETS:
        return "tikai_pieminets"
    return "nav_atrasts"


def ielade_overrides(celš: Path) -> dict:
    if yaml is None or not celš.exists():
        return {}
    dati = yaml.safe_load(celš.read_text(encoding="utf-8")) or {}
    return dati.get("parklajums", dati) if isinstance(dati, dict) else {}


def novertē_sr(sr_teksts: str, faili: list[Path]) -> dict:
    """Aprēķina viena programmas SR pārklājumu materiālu failos."""
    celmi = _saturvardi(sr_teksts)
    if not celmi:
        return {"statuss": "nav_atrasts", "vietas": [], "komentars": "SR tekstā nav saturvārdu."}

    trapijumi = []
    for celš in faili:
        for virsraksts, teksts, sadalas_celmi in _sadalas(celš):
            sakrit = celmi & sadalas_celmi
            if not sakrit:
                continue
            trapijumi.append((len(sakrit) / len(celmi), celš.name, virsraksts, teksts, sakrit))

    if not trapijumi:
        return {
            "statuss": "nav_atrasts",
            "vietas": [],
            "komentars": "Nav ne stundu aprakstos, ne darba lapās, ne vērtēšanas darbos.",
        }

    trapijumi.sort(key=lambda t: t[0], reverse=True)
    labaka_dala = trapijumi[0][0]
    statuss = _statuss(labaka_dala)

    vietas = [
        {"fails": fails, "sadala": virsraksts, "fragments": _fragments(teksts, sakrit)}
        for _, fails, virsraksts, teksts, sakrit in trapijumi[:MAX_VIETAS]
    ]
    if statuss == "nav_atrasts":
        vietas = vietas[:1]

    return {
        "statuss": statuss,
        "vietas": vietas,
        "komentars": (
            f"Leksiska sakritība {labaka_dala:.0%} no SR saturvārdiem "
            f"({len(trapijumi)} sadaļās). Nepieciešama cilvēka caurskate."
        ),
    }


def limena_bridinajumi(standarta_matrica: list[dict], faili: list[Path]) -> list[dict]:
    """Meklē materiālos saturu, kas pēc leksikas tuvāks M.A.* nekā M.O.* SR."""
    bridinajumi = []
    for rinda in standarta_matrica:
        augstakais = rinda.get("augstakais")
        optimalais = rinda.get("optimalais")
        if not augstakais or not optimalais:
            continue
        for a in augstakais if isinstance(augstakais, list) else [augstakais]:
            a_celmi = _saturvardi(a["teksts"])
            o_celmi = _saturvardi(
                optimalais[0]["teksts"] if isinstance(optimalais, list) else optimalais["teksts"]
            )
            tikai_a = a_celmi - o_celmi
            if len(tikai_a) < 4:
                continue
            for celš in faili:
                for virsraksts, teksts, sadalas_celmi in _sadalas(celš):
                    sakrit = tikai_a & sadalas_celmi
                    if len(sakrit) / len(tikai_a) < SLIEKSNIS_PILNS:
                        continue
                    bridinajumi.append(
                        {
                            "vieta": {"fails": celš.name, "sadala": virsraksts},
                            "fragments": _fragments(teksts, sakrit),
                            "atbilst_kodam": a["kods"],
                            "komentars": (
                                "Saturs pēc leksikas atbilst augstākajam apguves līmenim — "
                                "jāpārbauda, vai materiālā tas marķēts kā 'Nav standarta SR'."
                            ),
                        }
                    )
    return bridinajumi
