#!/usr/bin/env python3
"""Indeksē `prog-validate` servisa avota dokumentus divos JSON failos.

    python build_index.py [--data ./data] [--out ./index] [--strikti]

Rezultāts:
    index/standarts.json   – visas standarta rindas (vidusskolai V/O/A tripleti,
                             pamatskolai 1.–3./4.–6./7.–9. klases tripleti) +
                             plakans `kodu_indekss` (kods → klašu grupa, rinda, …)
    index/programmas.json  – visas reģistrētās mācību programmas: metadati,
                             temati, SR bloki, citētie kodi, OL materiāli

Programmu atrašanu un parsēšanu sk. `programmas.py` un `data/curricula/programmas.yaml`.
Būvēšanas laikā tiek pārbaudīts, ka katrs programmā citētais kods eksistē
standartā; nezināmie nonāk programmas laukā `nezinamie_kodi` (ar `--strikti` —
būve beidzas ar kļūdu).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import programmas as prog

HERE = Path(__file__).resolve().parent
DEFAULT_DATA = HERE / "data"
DEFAULT_OUT = HERE / "index"

STANDARTS_FAILS = "vidusskolas_standarts.md"
PAMATSKOLAS_FAILS = "pamatskolas_standarts.md"

LIMENU_BURTI = ("V", "O", "A")
LIMENU_LAUKI = {"V": "visparigais", "O": "optimalais", "A": "augstakais"}

# Vidusskolas standarta kolonnas ir apguves līmeņi (V/O/A), pamatskolas standarta
# kolonnas – klašu grupas ("Beidzot 3./6./9. klasi"), jo 1.–9. klasē visi skolēni
# apgūst vienu un to pašu saturu. Rindā blakus esošās šūnas ir viena un tā paša
# temata "spirāles" pakāpieni, tāpēc tās glabājam vienā ierakstā.
PSK_KLASES = ("3", "6", "9")
PSK_LAUKI = {"3": "klases_1_3", "6": "klases_4_6", "9": "klases_7_9"}
PSK_KLASU_GRUPAS = {"3": "1-3", "6": "4-6", "9": "7-9"}
VSK_KLASU_GRUPA = "10-12"

KLASU_GRUPAS = [
    {"kods": "1-3", "nosaukums": "1.–3. klase", "beidzot_klasi": 3,
     "izglitibas_pakape": "pamatskola", "lauks": "klases_1_3"},
    {"kods": "4-6", "nosaukums": "4.–6. klase", "beidzot_klasi": 6,
     "izglitibas_pakape": "pamatskola", "lauks": "klases_4_6"},
    {"kods": "7-9", "nosaukums": "7.–9. klase", "beidzot_klasi": 9,
     "izglitibas_pakape": "pamatskola", "lauks": "klases_7_9"},
    {"kods": "10-12", "nosaukums": "10.–12. klase", "beidzot_klasi": 12,
     "izglitibas_pakape": "vidusskola", "lauks": None},
]

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

# Pamatskolas standarts: "## M.Li.4. …" un kodi "M.3.4.1.1." / "M.6…" / "M.9…"
RE_PSK_LIELA_IDEJA = re.compile(r"^##\s+(M\.Li\.(\d+)\.)\s+(.+?)\s*$")
RE_PSK_KODS = re.compile(r"M\.([369])\.(\d+)\.(\d+)\.(\d+)\.")
RE_PSK_KODU_PRIEKSPUSE = re.compile(r"^\s*((?:M\.[369]\.\d+\.\d+\.\d+\.\s*/?\s*)+)")


def _parse_sunu(sunas_teksts: str, atlase: str, re_prieksa=RE_KODU_PRIEKSPUSE, re_kods=RE_KODS):
    """Atgriež None | {kods, teksts} | [{kods, teksts}, …] konkrētai kolonnai.

    `atlase` ir kolonnas pazīme koda otrajā pozīcijā: vidusskolā līmeņa burts
    (V/O/A), pamatskolā klašu grupas beigu klase (3/6/9).
    """
    if not sunas_teksts.strip():
        return None

    ieraksti = []
    for dala in sunas_teksts.split("<br><br>"):
        dala = dala.strip()
        if not dala:
            continue
        m = re_prieksa.match(dala)
        if not m:
            continue
        kodi = re_kods.findall(m.group(1))
        kods = next(
            (f"M.{b}.{x}.{y}.{z}." for b, x, y, z in kodi if b == atlase), None
        )
        if kods is None:
            # Šūna pieder citai kolonnai (piem., V teksts atkārtots O kolonnā).
            continue
        ieraksti.append({"kods": kods, "teksts": dala[m.end():].strip()})

    if not ieraksti:
        return None
    return ieraksti[0] if len(ieraksti) == 1 else ieraksti


def _ieraksti(vertiba) -> list[dict]:
    if vertiba is None:
        return []
    return list(vertiba) if isinstance(vertiba, list) else [vertiba]


def _pirmais_kods(vertiba):
    if vertiba is None:
        return None
    if isinstance(vertiba, list):
        return vertiba[0]["kods"]
    return vertiba["kods"]


def _visi_kodi(vertiba):
    return [e["kods"] for e in _ieraksti(vertiba)]


def sunu_lauki(rinda: dict) -> list[str]:
    """Rindas šūnu lauku nosaukumi atbilstoši izglītības pakāpei."""
    if rinda.get("izglitibas_pakape") == "pamatskola":
        return [PSK_LAUKI[k] for k in PSK_KLASES]
    return [LIMENU_LAUKI[b] for b in LIMENU_BURTI]


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

        ieraksts = {
            "rinda_id": None,
            "izglitibas_pakape": "vidusskola",
            "klasu_grupas": [VSK_KLASU_GRUPA],
            "liela_ideja": liela_ideja,
            "sadala": sadala,
        }
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


def parse_pamatskolas_standartu(celš: Path) -> list[dict]:
    """Pamatskolas standarts: kolonnas ir klašu grupas, nevis apguves līmeņi.

    Katra tabulas rinda dod vienu ierakstu ar līdz trim šūnām (`klases_1_3`,
    `klases_4_6`, `klases_7_9`) — tieši tā tiek saglabāta standarta "spirāle":
    blakus esošās šūnas ir viens un tas pats temats dažādā detalizācijas pakāpē.
    Tukša šūna nozīmē, ka attiecīgajā klašu grupā šī temata vēl/vairs nav.
    """
    liela_ideja = None
    sadala = None
    rindas: list[dict] = []
    kartas_nr: dict[str, int] = {}

    for rinda in celš.read_text(encoding="utf-8").splitlines():
        if m := RE_PSK_LIELA_IDEJA.match(rinda):
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
        if not RE_PSK_KODS.search(rinda):  # virsraksta / atdalītāja rinda
            continue
        if liela_ideja is None or sadala is None:
            continue

        ieraksts = {
            "rinda_id": None,
            "izglitibas_pakape": "pamatskola",
            "klasu_grupas": [],
            "liela_ideja": liela_ideja,
            "sadala": sadala,
        }
        for klase, suna in zip(PSK_KLASES, sunas):
            vertiba = _parse_sunu(suna, klase, RE_PSK_KODU_PRIEKSPUSE, RE_PSK_KODS)
            ieraksts[PSK_LAUKI[klase]] = vertiba
            if vertiba is not None:
                ieraksts["klasu_grupas"].append(PSK_KLASU_GRUPAS[klase])

        if not ieraksts["klasu_grupas"]:
            continue

        # Kodu numerācija rindā nesakrīt starp kolonnām (piem., M.3.1.1.2. blakus
        # M.6.1.1.3.), tāpēc rindas id veido sadaļas nr + kārtas nr sadaļā.
        nr = kartas_nr[sadala["nr"]] = kartas_nr.get(sadala["nr"], 0) + 1
        ieraksts["rinda_id"] = f"PSK.{sadala['nr'].rstrip('.')}.{nr}"
        ieraksts["tips"] = "caurviju" if liela_ideja["nr"] in CAURVIJU_IDEJAS else "satura"
        rindas.append(ieraksts)

    return rindas


def _validē_pamatskolas_kodus(celš: Path, rindas: list[dict]) -> None:
    """Neviens avota kods nedrīkst pazust parsējot, un tam jāatbilst sadaļai."""
    avota_kodi = {f"M.{b}.{x}.{y}.{z}." for b, x, y, z in RE_PSK_KODS.findall(
        celš.read_text(encoding="utf-8")
    )}
    parsētie = {
        kods
        for rinda in rindas
        for lauks in sunu_lauki(rinda)
        for kods in _visi_kodi(rinda[lauks])
    }
    if trukst := sorted(avota_kodi - parsētie):
        raise SystemExit(f"{celš.name}: neparsēti kodi: {trukst}")

    neatbilst = [
        (rinda["rinda_id"], kods)
        for rinda in rindas
        for lauks in sunu_lauki(rinda)
        for kods in _visi_kodi(rinda[lauks])
        if not kods.startswith(f"M.{kods.split('.')[1]}.{rinda['sadala']['nr']}")
    ]
    if neatbilst:
        raise SystemExit(f"{celš.name}: kodi neatbilst sadaļai: {neatbilst[:10]}")


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
# Kodu indekss (kods → klašu grupa, līmenis, rinda) turpmākajiem rīkiem
# --------------------------------------------------------------------------


def _kodu_indekss(rindas: list[dict]) -> dict[str, dict]:
    """Plakans kods → metadatu indekss.

    Vajadzīgs `new_tools.md` rīkiem (`search_taxonomy`, `classify_content_level`,
    `check_prerequisites`), kuriem no `TopicId` uzreiz jāzina `GradeBand`, un no
    kuriem caur `rinda_id` var atrast pārējos tā paša temata spirāles pakāpienus.
    """
    indekss: dict[str, dict] = {}
    for rinda in rindas:
        pamatskola = rinda["izglitibas_pakape"] == "pamatskola"
        if pamatskola:
            kolonnas = [
                (PSK_LAUKI[k], {"klasu_grupa": PSK_KLASU_GRUPAS[k], "beidzot_klasi": int(k)})
                for k in PSK_KLASES
            ]
        else:
            kolonnas = [
                (LIMENU_LAUKI[b], {"klasu_grupa": VSK_KLASU_GRUPA, "limenis": LIMENU_LAUKI[b]})
                for b in LIMENU_BURTI
            ]

        for lauks, meta in kolonnas:
            for poz, ieraksts in enumerate(_ieraksti(rinda[lauks])):
                indekss[ieraksts["kods"]] = {
                    "izglitibas_pakape": rinda["izglitibas_pakape"],
                    **meta,
                    "rinda_id": rinda["rinda_id"],
                    "lauks": lauks,
                    "poz": poz,
                    "liela_ideja": rinda["liela_ideja"]["kods"],
                    "sadala": rinda["sadala"]["nr"],
                    "tips": rinda["tips"],
                }
    return indekss


# --------------------------------------------------------------------------
# Būvēšana
# --------------------------------------------------------------------------


def build(data_dir: Path, out_dir: Path, *, kluss: bool = False, strikti: bool = False) -> dict:
    vsk_rindas = parse_standarts(data_dir / STANDARTS_FAILS)
    psk_rindas = parse_pamatskolas_standartu(data_dir / PAMATSKOLAS_FAILS)
    _validē_pamatskolas_kodus(data_dir / PAMATSKOLAS_FAILS, psk_rindas)
    standarta_rindas = vsk_rindas + psk_rindas
    visas_programmas = prog.build_programmas(data_dir)
    materiali = atrod_materialus(data_dir)

    # --- validācija: kodu unikalitāte standartā -------------------------
    kods_uz_rindu: dict[str, str] = {}
    dublikati = []
    for rinda in standarta_rindas:
        for lauks in sunu_lauki(rinda):
            for kods in _visi_kodi(rinda[lauks]):
                if kods in kods_uz_rindu and kods_uz_rindu[kods] != rinda["rinda_id"]:
                    dublikati.append(kods)
                kods_uz_rindu[kods] = rinda["rinda_id"]
    if dublikati:
        raise SystemExit(f"Kodi atkārtojas vairākās rindās: {sorted(set(dublikati))}")

    # --- validācija: programmās citētie kodi eksistē standartā ------------
    # Programmas nāk no dažādiem autoriem, un atsevišķas atsauces mēdz būt
    # kļūdainas. Nezināmu kodu neizmetam klusi: to fiksē programmas laukā
    # `nezinamie_kodi` (redzams `list_programs` atbildē). Ar --strikti būve krīt.
    trukstosie = []
    for programma in visas_programmas:
        nezinamie = []
        for temats in programma["temati"]:
            for bloks in temats["programmas_sr_bloki"]:
                for kods in bloks["citetie_kodi"]:
                    if kods not in kods_uz_rindu:
                        nezinamie.append(kods)
                        trukstosie.append((programma["program_id"], temats["marker"], bloks["bloks"], kods))
        programma["nezinamie_kodi"] = sorted(set(nezinamie))

    if trukstosie and not kluss:
        for pid, marker, bloks, kods in trukstosie:
            print(f"BRĪDINĀJUMS: {pid} temats {marker}, bloks '{bloks}': "
                  f"kods {kods} nav standartā", file=sys.stderr)
    if trukstosie and strikti:
        raise SystemExit(f"{len(trukstosie)} citētie kodi nav atrodami standartā.")

    # --- OL materiāli tematiem --------------------------------------------
    for programma in visas_programmas:
        for temats in programma["temati"]:
            faili = materiali.get(temats["ol_prefikss"] or "", [])
            temats["materiali_pieejami"] = bool(faili)
            temats["faili"] = faili

    kodu_indekss = _kodu_indekss(standarta_rindas)

    out_dir.mkdir(parents=True, exist_ok=True)
    _raksta(
        out_dir / "standarts.json",
        {
            "kodu_skaits": len(kods_uz_rindu),
            "kodu_skaits_pec_pakapes": {
                "vidusskola": sum(1 for m in kodu_indekss.values()
                                  if m["izglitibas_pakape"] == "vidusskola"),
                "pamatskola": sum(1 for m in kodu_indekss.values()
                                  if m["izglitibas_pakape"] == "pamatskola"),
            },
            "klasu_grupas": KLASU_GRUPAS,
            "rindas": standarta_rindas,
            "kodu_indekss": kodu_indekss,
        },
    )
    _raksta(
        out_dir / "programmas.json",
        {
            "programmu_skaits": len(visas_programmas),
            "kopas": prog.ielade_registru(data_dir)["kopas"],
            "programmas": visas_programmas,
        },
    )

    if not kluss:
        print(f"standarts.json  : {len(standarta_rindas)} rindas "
              f"({len(vsk_rindas)} vsk + {len(psk_rindas)} psk), "
              f"{len(kods_uz_rindu)} unikāli kodi")
        print(f"programmas.json : {len(visas_programmas)} programmas")
        for p in visas_programmas:
            ar_mat = sum(1 for t in p["temati"] if t["materiali_pieejami"])
            brid = f", {len(p['nezinamie_kodi'])} nezināmi kodi" if p["nezinamie_kodi"] else ""
            print(f"   {p['program_id']:22} {p['tips']:13} {len(p['temati']):3} temati"
                  f", {ar_mat} ar OL materiāliem{brid}")

    return {"standarts": standarta_rindas, "programmas": visas_programmas}


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
    ap.add_argument("--strikti", action="store_true",
                    help="beigt ar kļūdu, ja programmā citēts kods nav standartā")
    args = ap.parse_args()
    build(args.data, args.out, strikti=args.strikti)


if __name__ == "__main__":
    main()
