#!/usr/bin/env python3
"""Indeksē `prog-validate` servisa avota dokumentus trijos JSON failos.

    python build_index.py [--data ./data] [--out ./index]

Rezultāts:
    index/standarts.json  – visas standarta rindas (V/O/A tripleti)
    index/programma.json  – temati → SR bloki → programmas SR → citētie kodi
    index/temati.json     – temata nr ↔ OL prefikss ↔ pieejamie materiālu faili

Būvēšanas laikā tiek validēts, ka katrs programmā citētais kods eksistē
standartā; pretējā gadījumā skripts beidzas ar kļūdu sarakstu.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_DATA = HERE / "data"
DEFAULT_OUT = HERE / "index"

STANDARTS_FAILS = "vidusskolas_standarts.md"
PROGRAMMA_FAILS = "MATEMATIKA_1_programmas_paraugs_19_maijs.md"

LIMENU_BURTI = ("V", "O", "A")
LIMENU_LAUKI = {"V": "visparigais", "O": "optimalais", "A": "augstakais"}

# Li.1 (matemātikas valoda) un Li.2 (problēmrisināšana) caurvij visus tematus.
CAURVIJU_IDEJAS = {1, 2}


# --------------------------------------------------------------------------
# 1. slānis: valsts standarts
# --------------------------------------------------------------------------

RE_LIELA_IDEJA = re.compile(r"^##\s+(VSK\.M\.Li\.(\d+)\.)\s+(.+?)\s*$")
RE_SADALA = re.compile(r"^###\s+(\d+)\.(\d+)\.\s+(.+?)\s*$")
RE_KODS = re.compile(r"M\.([VOA])\.(\d+)\.(\d+)\.(\d+)\.")
# Šūnas sākumā var būt viens kods vai vairāki, atdalīti ar "/" (M.V.5.3.3./M.O.5.3.3.)
RE_KODU_PRIEKSPUSE = re.compile(r"^\s*((?:M\.[VOA]\.\d+\.\d+\.\d+\.\s*/?\s*)+)")


def _parse_sunu(sunas_teksts: str, burts: str):
    """Atgriež None | {kods, teksts} | [{kods, teksts}, …] konkrētam līmenim."""
    if not sunas_teksts.strip():
        return None

    ieraksti = []
    for dala in sunas_teksts.split("<br><br>"):
        dala = dala.strip()
        if not dala:
            continue
        m = RE_KODU_PRIEKSPUSE.match(dala)
        if not m:
            continue
        kodi = RE_KODS.findall(m.group(1))
        kods = next(
            (f"M.{b}.{x}.{y}.{z}." for b, x, y, z in kodi if b == burts), None
        )
        if kods is None:
            # Šūna pieder citam līmenim (piem., V teksts atkārtots O kolonnā).
            continue
        ieraksti.append({"kods": kods, "teksts": dala[m.end():].strip()})

    if not ieraksti:
        return None
    return ieraksti[0] if len(ieraksti) == 1 else ieraksti


def _pirmais_kods(vertiba):
    if vertiba is None:
        return None
    if isinstance(vertiba, list):
        return vertiba[0]["kods"]
    return vertiba["kods"]


def _visi_kodi(vertiba):
    if vertiba is None:
        return []
    if isinstance(vertiba, list):
        return [e["kods"] for e in vertiba]
    return [vertiba["kods"]]


def parse_standarts(celš: Path) -> list[dict]:
    liela_ideja = None
    sadala = None
    rindas: list[dict] = []

    for rinda in celš.read_text(encoding="utf-8").splitlines():
        if m := RE_LIELA_IDEJA.match(rinda):
            liela_ideja = {"kods": m.group(1), "nr": int(m.group(2)), "nosaukums": m.group(3)}
            continue
        if m := RE_SADALA.match(rinda):
            sadala = {"nr": f"{m.group(1)}.{m.group(2)}.", "nosaukums": m.group(3)}
            continue

        if not rinda.startswith("|"):
            continue
        sunas = [s.strip() for s in rinda.strip().strip("|").split("|")]
        if len(sunas) != 3:
            continue
        if not RE_KODS.search(rinda):  # virsraksta / atdalītāja rinda
            continue
        if liela_ideja is None or sadala is None:
            continue

        ieraksts = {"rinda_id": None, "liela_ideja": liela_ideja, "sadala": sadala}
        for burts, suna in zip(LIMENU_BURTI, sunas):
            ieraksts[LIMENU_LAUKI[burts]] = _parse_sunu(suna, burts)

        kods = (
            _pirmais_kods(ieraksts["optimalais"])
            or _pirmais_kods(ieraksts["visparigais"])
            or _pirmais_kods(ieraksts["augstakais"])
        )
        if kods is None:
            continue
        _, x, y, z = RE_KODS.match(kods).groups()
        ieraksts["rinda_id"] = f"{x}.{y}.{z}"
        ieraksts["tips"] = "caurviju" if liela_ideja["nr"] in CAURVIJU_IDEJAS else "satura"
        rindas.append(ieraksts)

    return rindas


# --------------------------------------------------------------------------
# 2. slānis: programmas paraugs (pandoc HTML tabulas)
# --------------------------------------------------------------------------

RE_TEMATS = re.compile(
    r"^\*\*(\d+)\.[ ]+(.+?)\*\*\s*\((\d+)\s*stund", re.MULTILINE | re.DOTALL
)
RE_MERKIS = re.compile(r"\*\*Temata apguves mērķis:\*\*\s*(.+?)\n\s*\n", re.DOTALL)
RE_JEDZIENI = re.compile(r"\*\*Jēdzieni:\*\*\s*(.+?)\n\s*\n", re.DOTALL)
RE_BLOKA_VIRSRAKSTS = re.compile(r"^(.*?)\s*\(\s*((?:M\.O\.\d+\.\d+\.\d+\.[\s,]*)+)\)\s*$")


class _TabulasParseris(HTMLParser):
    """Izvelk tabulas rindas kā [(colspan, teksts), …] sarakstus."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rindas: list[list[tuple[int, str]]] = []
        self._rinda: list[tuple[int, str]] | None = None
        self._bufers: list[str] | None = None
        self._colspan = 1

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self._rinda = []
        elif tag in ("td", "th") and self._rinda is not None:
            self._bufers = []
            self._colspan = int(dict(attrs).get("colspan", 1))
        elif tag in ("p", "br") and self._bufers is not None:
            self._bufers.append(" ")

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self._bufers is not None:
            teksts = re.sub(r"\s+", " ", "".join(self._bufers)).strip()
            self._rinda.append((self._colspan, teksts))
            self._bufers = None
        elif tag == "tr" and self._rinda is not None:
            self.rindas.append(self._rinda)
            self._rinda = None
        elif tag in ("p",) and self._bufers is not None:
            self._bufers.append(" ")

    def handle_data(self, data):
        if self._bufers is not None:
            self._bufers.append(data)


def _nosaukuma_forma(lielie_burti: str) -> str:
    """`LĪNIJAS VIENĀDOJUMS, …` → `Līnijas vienādojums, …`."""
    teksts = re.sub(r"\s+", " ", lielie_burti).strip().lower()
    return teksts[:1].upper() + teksts[1:]


def parse_programma(celš: Path) -> list[dict]:
    saturs = celš.read_text(encoding="utf-8")
    atrastie = list(RE_TEMATS.finditer(saturs))
    temati = []

    for i, m in enumerate(atrastie):
        sakums = m.start()
        beigas = atrastie[i + 1].start() if i + 1 < len(atrastie) else len(saturs)
        gabals = saturs[sakums:beigas]

        nr = int(m.group(1))
        temats = {
            "nr": nr,
            "ol_prefikss": f"OL_{nr}",
            "nosaukums": _nosaukuma_forma(m.group(2)),
            "stundas": int(m.group(3)),
            "kurss": "Matemātika I",
            "apguves_limenis": "optimālais",
            "merkis": None,
            "jedzieni": [],
            "programmas_sr_bloki": [],
        }

        if mm := RE_MERKIS.search(gabals):
            temats["merkis"] = re.sub(r"\s+", " ", mm.group(1)).strip()
        if mm := RE_JEDZIENI.search(gabals):
            jedzieni = re.sub(r"\s+", " ", mm.group(1)).strip()
            temats["jedzieni"] = [j.strip() for j in jedzieni.split(",") if j.strip()]

        tabula = re.search(r"<table.*?</table>", gabals, re.DOTALL)
        if tabula:
            temats["programmas_sr_bloki"] = _parse_blokus(nr, tabula.group(0))
        temati.append(temats)

    return temati


def _parse_blokus(temata_nr: int, tabulas_html: str) -> list[dict]:
    p = _TabulasParseris()
    p.feed(tabulas_html)

    bloki: list[dict] = []
    for rinda in p.rindas:
        if len(rinda) == 1 and rinda[0][0] >= 3:
            teksts = rinda[0][1]
            if m := RE_BLOKA_VIRSRAKSTS.match(teksts):
                kodi = re.findall(r"M\.O\.\d+\.\d+\.\d+\.", m.group(2))
                bloki.append(
                    {
                        "bloks": m.group(1).strip(),
                        "citetie_kodi": list(dict.fromkeys(kodi)),
                        "programmas_sr": [],
                    }
                )
            continue

        if len(rinda) != 3 or not bloki:
            continue
        sr_teksts = rinda[0][1]
        piemeri = rinda[2][1]
        if not sr_teksts or sr_teksts == "Sasniedzamais rezultāts":
            continue

        bloks = bloki[-1]
        bloks["programmas_sr"].append(
            {
                "id": f"{temata_nr}.B{len(bloki)}.SR{len(bloks['programmas_sr']) + 1}",
                "teksts": sr_teksts,
                "piemeri_skaidrojumi": piemeri or None,
            }
        )

    return bloki


# --------------------------------------------------------------------------
# 3. slānis: OL materiālu faili
# --------------------------------------------------------------------------


def atrod_materialus(data_dir: Path) -> dict[str, list[str]]:
    """OL prefikss → materiālu failu ceļi (relatīvi pret data/)."""
    pec_prefiksa: dict[str, list[str]] = {}
    for celš in sorted(data_dir.rglob("*.md")):
        m = re.match(r"^(OL_\d{1,2})(?=[_.])", celš.name)
        if not m:
            continue
        rel = celš.relative_to(data_dir).as_posix()
        pec_prefiksa.setdefault(m.group(1), []).append(rel)
    return pec_prefiksa


# --------------------------------------------------------------------------
# Būvēšana
# --------------------------------------------------------------------------


def build(data_dir: Path, out_dir: Path, *, kluss: bool = False) -> dict:
    standarta_rindas = parse_standarts(data_dir / STANDARTS_FAILS)
    temati = parse_programma(data_dir / PROGRAMMA_FAILS)
    materiali = atrod_materialus(data_dir)

    # --- validācija: kodu unikalitāte standartā -------------------------
    kods_uz_rindu: dict[str, str] = {}
    dublikati = []
    for rinda in standarta_rindas:
        for lauks in LIMENU_LAUKI.values():
            for kods in _visi_kodi(rinda[lauks]):
                if kods in kods_uz_rindu and kods_uz_rindu[kods] != rinda["rinda_id"]:
                    dublikati.append(kods)
                kods_uz_rindu[kods] = rinda["rinda_id"]
    if dublikati:
        raise SystemExit(f"Kodi atkārtojas vairākās rindās: {sorted(set(dublikati))}")

    # --- validācija: programmā citētie kodi eksistē standartā ------------
    trukstosie = []
    for temats in temati:
        for bloks in temats["programmas_sr_bloki"]:
            for kods in bloks["citetie_kodi"]:
                if kods not in kods_uz_rindu:
                    trukstosie.append((temats["nr"], bloks["bloks"], kods))
    if trukstosie:
        for nr, bloks, kods in trukstosie:
            print(f"KĻŪDA: temats {nr}, bloks '{bloks}': kods {kods} nav standartā", file=sys.stderr)
        raise SystemExit(f"{len(trukstosie)} citētie kodi nav atrodami standartā.")

    # --- temati.json ------------------------------------------------------
    temati_kopsavilkums = [
        {
            "nr": t["nr"],
            "nosaukums": t["nosaukums"],
            "stundas": t["stundas"],
            "ol_prefikss": t["ol_prefikss"],
            "materiali_pieejami": bool(materiali.get(t["ol_prefikss"])),
            "faili": materiali.get(t["ol_prefikss"], []),
        }
        for t in temati
    ]

    out_dir.mkdir(parents=True, exist_ok=True)
    _raksta(out_dir / "standarts.json", {"kodu_skaits": len(kods_uz_rindu), "rindas": standarta_rindas})
    _raksta(out_dir / "programma.json", {"temati": temati})
    _raksta(out_dir / "temati.json", {"temati": temati_kopsavilkums})

    if not kluss:
        print(f"standarts.json : {len(standarta_rindas)} rindas, {len(kods_uz_rindu)} unikāli kodi")
        print(f"programma.json : {len(temati)} temati")
        ar_mat = sum(1 for t in temati_kopsavilkums if t["materiali_pieejami"])
        print(f"temati.json    : {ar_mat}/{len(temati_kopsavilkums)} tematiem ir OL materiāli")

    return {"standarts": standarta_rindas, "temati": temati, "temati_kopsavilkums": temati_kopsavilkums}


def _raksta(celš: Path, dati: dict) -> None:
    celš.write_text(json.dumps(dati, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    for straume in (sys.stdout, sys.stderr):
        try:  # Windows konsole pēc noklusējuma nav UTF-8
            straume.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Būvē prog-validate indeksu.")
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    build(args.data, args.out)


if __name__ == "__main__":
    main()
