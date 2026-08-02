"""Mācību programmu reģistrs: failu atrašana, parsēšana, normalizēšana.

Servisā līdzās pastāv divu veidu programmas:

* `paraugs`       – Skola2030 programmu paraugi Markdown formātā (Matemātika I,
                    Matemātika II, Matemātika 1.–9. klasei). Temats satur SR
                    blokus ar citētiem standarta kodiem.
* `stundu_plans`  – reāli skolas stundu plāni (JSON + CSV, eksports no e-klases
                    žurnāla). Temats satur kalendāru un ievesto jēdzienu sarakstu,
                    bet ne standarta SR blokus.

Abi tipi tiek nolasīti vienā un tajā pašā formā (sk. `_temats()` atslēgas), lai
`list_temati` un `list_programs` strādā ar jebkuru programmu vienādi.

Failu nosaukumu shēmu un reģistru sk. `data/curricula/programmas.yaml`.
"""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

try:
    import yaml
except ImportError:  # reģistrs nav obligāts — bez tā strādā noklusējumi
    yaml = None

PROGRAMMU_MAPE = "curricula"
REGISTRA_FAILS = "programmas.yaml"

# program_<program_id>[_<loma>].<ext>
RE_FAILS = re.compile(r"^program_([a-z0-9.\-]+?)(?:_([a-z0-9\-]+))?\.(md|json|csv)$", re.I)

KLASU_GRUPAS = ((1, 3, "1-3"), (4, 6, "4-6"), (7, 9, "7-9"), (10, 12, "10-12"))

# Standarta kods jebkurā no sastopamajām rakstībām: "M.O.4.5.1.", "M.A.1.1.1"
# (bez beigu punkta), "M9.3.2.1." (bez punkta aiz M). Normalizē uz "M.O.4.5.1.".
RE_KODS_BRIVS = re.compile(r"M\.?([VOA369])\.(\d+)\.(\d+)\.(\d+)\.?")


class ProgrammuKluda(ValueError):
    """Programmas faila/reģistra kļūda, kas parādāma lietotājam."""


def klasu_grupa(klase: int | None) -> str | None:
    if klase is None:
        return None
    for no, lidz, kods in KLASU_GRUPAS:
        if no <= klase <= lidz:
            return kods
    return None


def normalize_kodus(teksts: str) -> list[str]:
    """Visi standarta kodi tekstā kanoniskā formā, saglabājot secību."""
    kodi = [f"M.{a}.{x}.{y}.{z}." for a, x, y, z in RE_KODS_BRIVS.findall(teksts)]
    return list(dict.fromkeys(kodi))


def _tirs(teksts: str) -> str:
    """Pandoc artefakti nost: treknraksts, rindu pārnesumi, dubultatstarpes.

    `\\` rindas beigās ir pandoc rindas pārtraukums; `\\(`, `\\.` u. tml. ir
    aizsargātas pieturzīmes. LaTeX komandas (`\\mathbb`) netiek aiztiktas.
    """
    teksts = teksts.replace("**", "")
    teksts = re.sub(r"\\(?=\s|$)", " ", teksts)
    teksts = re.sub(r"\\([^A-Za-z0-9])", r"\1", teksts)
    return re.sub(r"\s+", " ", teksts).strip()


# --------------------------------------------------------------------------
# Reģistrs un failu atrašana
# --------------------------------------------------------------------------


def ielade_registru(data_dir: Path) -> dict:
    celš = data_dir / PROGRAMMU_MAPE / REGISTRA_FAILS
    if yaml is None or not celš.exists():
        return {"programmas": {}, "kopas": {}}
    dati = yaml.safe_load(celš.read_text(encoding="utf-8")) or {}
    return {"programmas": dati.get("programmas") or {}, "kopas": dati.get("kopas") or {}}


def atrod_failus(data_dir: Path) -> dict[str, dict[str, list[str]]]:
    """program_id → {loma → faili} (ceļi relatīvi pret data/).

    Loma `pamats` ir programmas galvenais fails (.md vai .json), pārējās —
    papildu tabulas, piem. `concepts` (program_<id>_concepts.csv).
    """
    atrastie: dict[str, dict[str, list[str]]] = {}
    mape = data_dir / PROGRAMMU_MAPE
    if not mape.is_dir():
        return atrastie

    for celš in sorted(mape.iterdir()):
        m = RE_FAILS.match(celš.name)
        if not m:
            continue
        program_id, loma, _ = m.groups()
        rel = celš.relative_to(data_dir).as_posix()
        atrastie.setdefault(program_id, {}).setdefault(loma or "pamats", []).append(rel)
    return atrastie


# --------------------------------------------------------------------------
# Kopīgā temata forma
# --------------------------------------------------------------------------


def _temats(program_id: str, nr: int, marker: str, nosaukums: str, **papildus) -> dict:
    temats = {
        "temats_id": f"{program_id}#T{nr:02d}",
        "program_id": program_id,
        "nr": nr,
        "marker": marker,
        "nosaukums": nosaukums,
        "klase": None,
        "klasu_grupa": None,
        "stundas": None,
        "stundu_diapazons": None,
        "macibu_dienas": None,
        "ol_prefikss": None,
        "merkis": None,
        "jedzieni": [],
        "programmas_sr_bloki": [],
    }
    temats.update(papildus)
    return temats


def _stundas(teksts: str) -> tuple[int | None, list[int] | None]:
    """`"15--17 stundas"` → (15, [15, 17]); `"16 stundas"` → (16, None)."""
    skaitli = [int(x) for x in re.findall(r"\d+", teksts)]
    if not skaitli:
        return None, None
    if len(skaitli) == 1:
        return skaitli[0], None
    return min(skaitli), [min(skaitli), max(skaitli)]


# --------------------------------------------------------------------------
# Parsētājs `avotina_html`: Matemātika I (pandoc <table> tabulas)
# --------------------------------------------------------------------------

RE_TEMATS = re.compile(r"^\*\*(\d+)\.[ ]+(.+?)\*\*\s*\((\d+)\s*stund", re.MULTILINE | re.DOTALL)
RE_MERKIS = re.compile(r"\*\*Temata apguves mērķis:\*\*\s*(.+?)\n\s*\n", re.DOTALL)
RE_JEDZIENI = re.compile(r"\*\*Jēdzieni:\*\*\s*(.+?)\n\s*\n", re.DOTALL)
RE_BLOKA_VIRSRAKSTS = re.compile(r"^(.*?)\s*\(\s*([^()]*?M\.?[VOA369][^()]*?)\)\s*$")


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


def _nosaukuma_forma(nosaukums: str) -> str:
    """`LĪNIJAS VIENĀDOJUMS, …` → `Līnijas vienādojums, …`.

    Jauktā reģistrā rakstītus nosaukumus (`Talesa teorēma …`) neaiztiek, lai
    nesabojātu īpašvārdus.
    """
    teksts = re.sub(r"\s+", " ", nosaukums).strip()
    if teksts != teksts.upper():
        return teksts
    teksts = teksts.lower()
    return re.sub(r"(^|(?<=[.:!?] ))(\w)", lambda m: m.group(0).upper(), teksts)


def _bloka_virsraksts(teksts: str) -> tuple[str, list[str]] | None:
    """`"Taisnes vienādojums (M.O.6.2.4.)"` → `("Taisnes vienādojums", [kods])`."""
    teksts = _tirs(teksts)
    if m := RE_BLOKA_VIRSRAKSTS.match(teksts):
        kodi = normalize_kodus(m.group(2))
        if kodi:
            return m.group(1).strip(), kodi
    kodi = normalize_kodus(teksts)
    if kodi:  # kodi ir, bet ne iekavās formā, ko gaidījām
        return RE_KODS_BRIVS.split(teksts)[0].strip(" (,;"), kodi
    return None


def parse_avotina_html(program_id: str, saturs: str, meta: dict) -> list[dict]:
    atrastie = list(RE_TEMATS.finditer(saturs))
    temati = []

    for i, m in enumerate(atrastie):
        beigas = atrastie[i + 1].start() if i + 1 < len(atrastie) else len(saturs)
        gabals = saturs[m.start():beigas]
        nr = int(m.group(1))

        temats = _temats(
            program_id, nr, f"{nr}.", _nosaukuma_forma(m.group(2)),
            stundas=int(m.group(3)),
            klasu_grupa=(meta.get("klasu_grupas") or [None])[0],
            ol_prefikss=f"OL_{nr}" if meta.get("ol_materiali") else None,
        )
        _merkis_un_jedzieni(temats, gabals)

        if tabula := re.search(r"<table.*?</table>", gabals, re.DOTALL):
            temats["programmas_sr_bloki"] = _html_blokus(temats["temats_id"], tabula.group(0))
        temati.append(temats)

    return temati


def _merkis_un_jedzieni(temats: dict, gabals: str) -> None:
    if m := RE_MERKIS.search(gabals):
        temats["merkis"] = _tirs(m.group(1))
    if m := RE_JEDZIENI.search(gabals):
        temats["jedzieni"] = [j.strip() for j in _tirs(m.group(1)).split(",") if j.strip()]


def _html_blokus(temats_id: str, tabulas_html: str) -> list[dict]:
    p = _TabulasParseris()
    p.feed(tabulas_html)

    bloki: list[dict] = []
    for rinda in p.rindas:
        if len(rinda) == 1 and rinda[0][0] >= 3:
            if virsraksts := _bloka_virsraksts(rinda[0][1]):
                nosaukums, kodi = virsraksts
                bloki.append({"bloks": nosaukums, "citetie_kodi": kodi, "programmas_sr": []})
            continue

        if len(rinda) != 3 or not bloki:
            continue
        sr_teksts = rinda[0][1]
        if not sr_teksts or sr_teksts == "Sasniedzamais rezultāts":
            continue
        _pievieno_sr(bloki, temats_id, sr_teksts, rinda[2][1])

    return bloki


def _pievieno_sr(bloki: list[dict], temats_id: str, sr_teksts: str, piemeri: str,
                 caurviju: str | None = None) -> None:
    bloks = bloki[-1]
    ieraksts = {
        # Pilns id, jo tematu numuri dažādās programmās atkārtojas; šo atslēgu
        # lieto arī `coverage_overrides.yaml`.
        "id": f"{temats_id}.B{len(bloki)}.SR{len(bloks['programmas_sr']) + 1}",
        "teksts": sr_teksts,
        "piemeri_skaidrojumi": piemeri or None,
    }
    if caurviju:
        ieraksts["caurviju_prasmes"] = caurviju.split()
    bloks["programmas_sr"].append(ieraksts)


# --------------------------------------------------------------------------
# Parsētāji `avotina_grid*`: pandoc grid tabulas (+---+---+)
# --------------------------------------------------------------------------

RE_GRID_SEP = re.compile(r"^\+[-=+:]+\+\s*$")
# 1.–9. klases paraugā tematu marķē klase un kārtas nr, algebrai/ģeometrijai
# 7.–9. klasē vēl priekšā A vai G: "1.2.", "A7.1.", "G9.5.".
RE_TEMATS_1_9 = re.compile(
    r"^\*\*([AG]?)(\d+)\.(\d+)\.\s+([^*]+?)\*\*\s*\(([^)]*?stund[^)]*)\)",
    re.MULTILINE | re.DOTALL,
)


def _grid_tabulas(teksts: str) -> list[list[list[str]]]:
    """Grid tabulas kā rindu saraksti; rinda = šūnu tekstu saraksts."""
    rindas = teksts.splitlines()
    tabulas: list[list[list[str]]] = []
    i = 0
    while i < len(rindas):
        if not RE_GRID_SEP.match(rindas[i]):
            i += 1
            continue
        sakums = i
        while i < len(rindas) and rindas[i][:1] in ("+", "|"):
            i += 1
        tabulas.append(_grid_rindas(rindas[sakums:i]))
    return [t for t in tabulas if t]


def _grid_rindas(rindas: list[str]) -> list[list[str]]:
    izvade: list[list[str]] = []
    bufers: list[str] = []
    for r in rindas:
        if RE_GRID_SEP.match(r):
            if bufers:
                izvade.append(_grid_suna(bufers))
                bufers = []
            continue
        bufers.append(r)
    if bufers:
        izvade.append(_grid_suna(bufers))
    return izvade


def _grid_suna(rindas: list[str]) -> list[str]:
    sunas: list[list[str]] | None = None
    for rinda in rindas:
        teksts = rinda.strip().strip("|")
        gabali = teksts.split("|")
        if sunas is None:
            sunas = [[g] for g in gabali]
        elif len(gabali) == len(sunas):
            for suna, gabals in zip(sunas, gabali):
                suna.append(gabals)
        else:
            # Rindas iekšienē mainījies kolonnu skaits (apvienota šūna) —
            # turpinājumu pieliek pirmajai šūnai, lai teksts nepazūd.
            sunas[0].append(teksts)
    return [_tirs(" ".join(s)) for s in (sunas or [])]


def _grid_kolonnas(tabula: list[list[str]]) -> tuple[int, int | None, int | None]:
    """(SR kolonna, piemēru kolonna, caurviju kolonna) pēc virsraksta rindas."""
    for rinda in tabula[:2]:
        virsraksti = [_tirs(c).lower() for c in rinda]
        if any(v.startswith("sasniedzamais rezultāts") for v in virsraksti):
            sr = next(i for i, v in enumerate(virsraksti) if v.startswith("sasniedzamais"))
            piem = next((i for i, v in enumerate(virsraksti) if v.startswith("piemēri")), None)
            citas = [i for i in range(len(virsraksti)) if i not in (sr, piem)]
            return sr, piem, (citas[0] if citas else None)
    return 0, (2 if tabula and len(tabula[0]) > 2 else 1), None


def _grid_blokus(temats_id: str, tabulas: list[list[list[str]]]) -> list[dict]:
    bloki: list[dict] = []
    for tabula in tabulas:
        sr_kol, piem_kol, caurviju_kol = _grid_kolonnas(tabula)
        for rinda in tabula:
            if len(rinda) == 1:  # pilna platuma rinda = bloka virsraksts
                if virsraksts := _bloka_virsraksts(rinda[0]):
                    nosaukums, kodi = virsraksts
                    bloki.append({"bloks": nosaukums, "citetie_kodi": kodi, "programmas_sr": []})
                elif teksts := _tirs(rinda[0]):
                    bloki.append({"bloks": teksts, "citetie_kodi": [], "programmas_sr": []})
                continue

            if sr_kol >= len(rinda):
                continue
            sr_teksts = _tirs(rinda[sr_kol])
            if not sr_teksts or sr_teksts.lower().startswith("sasniedzamais rezultāts"):
                continue
            if not bloki:  # SR bez bloka virsraksta — savācam bez koda
                bloki.append({"bloks": None, "citetie_kodi": [], "programmas_sr": []})
            _pievieno_sr(
                bloki, temats_id, sr_teksts,
                _tirs(rinda[piem_kol]) if piem_kol is not None and piem_kol < len(rinda) else "",
                _tirs(rinda[caurviju_kol]) if caurviju_kol is not None and caurviju_kol < len(rinda) else None,
            )
    return bloki


def parse_avotina_grid(program_id: str, saturs: str, meta: dict) -> list[dict]:
    atrastie = list(RE_TEMATS.finditer(saturs))
    temati = []

    for i, m in enumerate(atrastie):
        beigas = atrastie[i + 1].start() if i + 1 < len(atrastie) else len(saturs)
        gabals = saturs[m.start():beigas]
        nr = int(m.group(1))

        temats = _temats(
            program_id, nr, f"{nr}.", _nosaukuma_forma(m.group(2)),
            stundas=int(m.group(3)),
            klasu_grupa=(meta.get("klasu_grupas") or [None])[0],
        )
        _merkis_un_jedzieni(temats, gabals)
        temats["programmas_sr_bloki"] = _grid_blokus(temats["temats_id"], _grid_tabulas(gabals))
        temati.append(temats)

    return temati


def parse_avotina_grid_1_9(program_id: str, saturs: str, meta: dict) -> list[dict]:
    atrastie = list(RE_TEMATS_1_9.finditer(saturs))
    temati = []

    for i, m in enumerate(atrastie):
        beigas = atrastie[i + 1].start() if i + 1 < len(atrastie) else len(saturs)
        gabals = saturs[m.start():beigas]

        joma, klase, kartas_nr, nosaukums, stundas = m.groups()
        # Dokumentā ir dublēti marķieri (divi temati "3.6."), tāpēc temata id
        # veido kārtas numurs programmā, bet marķieris paliek kā dokumentā.
        nr = i + 1
        marker = f"{joma}{klase}.{kartas_nr}."
        stundu_skaits, diapazons = _stundas(stundas)

        temats = _temats(
            program_id, nr, marker, _nosaukuma_forma(nosaukums),
            stundas=stundu_skaits,
            stundu_diapazons=diapazons,
            klase=int(klase),
            klasu_grupa=klasu_grupa(int(klase)),
            joma={"A": "algebra", "G": "geometrija"}.get(joma),
        )
        _merkis_un_jedzieni(temats, gabals)
        temats["programmas_sr_bloki"] = _grid_blokus(temats["temats_id"], _grid_tabulas(gabals))
        temati.append(temats)

    return temati


PARSETAJI = {
    "avotina_html": parse_avotina_html,
    "avotina_grid": parse_avotina_grid,
    "avotina_grid_1_9": parse_avotina_grid_1_9,
}


# --------------------------------------------------------------------------
# Stundu plāni (JSON no e-klases žurnāla eksporta)
# --------------------------------------------------------------------------


def parse_stundu_planu(program_id: str, dati: dict, meta: dict) -> list[dict]:
    klase = dati.get("grade")
    temati = []
    for i, t in enumerate(dati.get("topics") or [], start=1):
        jedzieni = t.get("introduces_concepts") or []
        temats = _temats(
            program_id, t.get("order", i), t.get("marker") or f"{i}.", _tirs(t.get("title", "")),
            klase=klase,
            klasu_grupa=klasu_grupa(klase),
            macibu_dienas=t.get("lesson_days"),
            jedzieni=[j["label"] for j in jedzieni],
        )
        temats["temats_id"] = t.get("topic_id") or temats["temats_id"]
        temats["ievies_jedzienus"] = jedzieni
        temats["macits"] = t.get("taught")
        temats["parbaudes_darbi"] = t.get("test_events") or []
        temats["majasdarbi"] = bool(t.get("has_homework"))
        temati.append(temats)
    return temati


# --------------------------------------------------------------------------
# Programmu būvēšana
# --------------------------------------------------------------------------

STANDARTU_FAILI = {
    "vidusskola": "vidusskolas_standarts.md",
    "pamatskola": "pamatskolas_standarts.md",
}


def build_programmas(data_dir: Path) -> list[dict]:
    """Visas atrastās programmas normalizētā formā, sakārtotas pēc program_id."""
    registrs = ielade_registru(data_dir)
    faili = atrod_failus(data_dir)
    programmas = []

    for program_id in sorted(faili):
        lomas = faili[program_id]
        pamats = lomas.get("pamats")
        if not pamats:
            continue
        if len(pamats) > 1:
            raise ProgrammuKluda(
                f"{program_id}: vairāki pamata faili ({', '.join(pamats)}); "
                "papildu tabulām lieto program_<id>_<loma>.<ext>"
            )
        programmas.append(_programma(data_dir, program_id, pamats[0], lomas, registrs))

    return programmas


def _programma(data_dir: Path, program_id: str, rel: str, lomas: dict, registrs: dict) -> dict:
    meta = dict(registrs["programmas"].get(program_id) or {})
    celš = data_dir / rel
    ir_json = celš.suffix.lower() == ".json"

    if ir_json:
        dati = json.loads(celš.read_text(encoding="utf-8"))
        temati = parse_stundu_planu(program_id, dati, meta)
        klases = [dati["grade"]] if dati.get("grade") else meta.get("klases") or []
        pamatdati = {
            "nosaukums": meta.get("nosaukums") or dati.get("title") or program_id,
            "tips": meta.get("tips", "stundu_plans"),
            "skolotajs": dati.get("teacher"),
            "macibu_gads": dati.get("school_year") or meta.get("macibu_gads"),
            "revizija": dati.get("program_revision"),
            "kalendars": {
                "no": (dati.get("span") or {}).get("from"),
                "lidz": (dati.get("span") or {}).get("to"),
                "macibu_dienas": dati.get("total_lesson_days"),
                "pirma_nedela": dati.get("week1_monday"),
            },
            "izcelsme": dati.get("source"),
        }
    else:
        parseris = meta.get("parseris")
        if parseris not in PARSETAJI:
            raise ProgrammuKluda(
                f"{program_id}: reģistrā nav zināma parsētāja (`parseris`) — "
                f"pieejamie: {', '.join(sorted(PARSETAJI))}. Sk. {PROGRAMMU_MAPE}/{REGISTRA_FAILS}."
            )
        temati = PARSETAJI[parseris](program_id, celš.read_text(encoding="utf-8"), meta)
        klases = meta.get("klases") or []
        pamatdati = {
            "nosaukums": meta.get("nosaukums") or program_id,
            "tips": meta.get("tips", "paraugs"),
            "skolotajs": None,
            "macibu_gads": meta.get("macibu_gads"),
            "revizija": meta.get("revizija"),
            "kalendars": None,
            "izcelsme": meta.get("avota_fails"),
        }

    klasu_grupas = meta.get("klasu_grupas") or sorted(
        {t["klasu_grupa"] for t in temati if t["klasu_grupa"]}
    )
    standarts = meta.get("standarts") or ("pamatskola" if klasu_grupas[:1] != ["10-12"] else "vidusskola")

    return {
        "program_id": program_id,
        **pamatdati,
        "kopa": meta.get("kopa"),
        "izglitibas_pakape": standarts,
        "standarta_fails": STANDARTU_FAILI.get(standarts),
        "apguves_limenis": meta.get("apguves_limenis"),
        "klasu_grupas": klasu_grupas,
        "klases": klases,
        "autors": meta.get("autors"),
        "izdevejs": meta.get("izdevejs"),
        "iestade": meta.get("iestade"),
        "avots": rel,
        "faili": sorted(f for celi in lomas.values() for f in celi),
        "temati": temati,
    }
