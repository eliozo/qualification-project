#!/usr/bin/env python3
"""`prog-validate` MCP serviss: rīki `list_programs`, `list_temati`, `get_sr_matrix`.

    python server.py                        # stdio (Claude Desktop / Claude Code)
    python server.py --transport streamable-http --port 8000

Datu ceļš konfigurējams ar env `PROG_VALIDATE_DATA` (noklusējums: ./data);
indeksa ceļš ar `PROG_VALIDATE_INDEX` (noklusējums: ./index).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Literal

from mcp.server.fastmcp import FastMCP

import coverage as cov

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("PROG_VALIDATE_DATA", HERE / "data"))
INDEX_DIR = Path(os.environ.get("PROG_VALIDATE_INDEX", HERE / "index"))
OVERRIDES = HERE / "coverage_overrides.yaml"

LIMENU_LAUKI = {"V": "visparigais", "O": "optimalais", "A": "augstakais"}
VISI_LIMENI = ["V", "O", "A"]

# Vidusskolas rindā kolonnas ir apguves līmeņi, pamatskolas rindā – klašu grupas
# (1.–9. klasē līmeņu nav; tā vietā standarts tai pašā tematā atgriežas trīs
# reizes ar pieaugošu detalizāciju).
KLASU_GRUPU_LAUKI = {"1-3": "klases_1_3", "4-6": "klases_4_6", "7-9": "klases_7_9"}
SUNU_LAUKI = tuple(LIMENU_LAUKI.values()) + tuple(KLASU_GRUPU_LAUKI.values())


class ProgValidateError(ValueError):
    """Lietotājam adresēta kļūda (nonāk MCP kļūdas tekstā)."""


# --------------------------------------------------------------------------
# Indeksa ielāde
# --------------------------------------------------------------------------

_indekss: dict[str, Any] | None = None


def indekss() -> dict[str, Any]:
    global _indekss
    if _indekss is not None:
        return _indekss

    trukst = [f for f in ("standarts.json", "programmas.json")
              if not (INDEX_DIR / f).exists()]
    if trukst:
        raise ProgValidateError(
            f"Trūkst indeksa faili ({', '.join(trukst)}) mapē {INDEX_DIR}. "
            "Palaid: python build_index.py --data ./data"
        )

    def ielasa(vards: str) -> dict:
        return json.loads((INDEX_DIR / vards).read_text(encoding="utf-8"))

    standarts = ielasa("standarts.json")
    programmas = ielasa("programmas.json")
    _indekss = {
        "standarts": standarts,
        "rindas_pec_koda": {
            kods: rinda
            for rinda in standarts["rindas"]
            for lauks in SUNU_LAUKI
            for kods in _kodi(rinda.get(lauks))
        },
        # kods → {klasu_grupa, limenis, rinda_id, …}; sk. build_index._kodu_indekss.
        "kodu_indekss": standarts.get("kodu_indekss", {}),
        "klasu_grupas": standarts.get("klasu_grupas", []),
        "programmas": programmas["programmas"],
        "programmas_pec_id": {p["program_id"]: p for p in programmas["programmas"]},
        "kopas": programmas.get("kopas", {}),
        "overrides": cov.ielade_overrides(OVERRIDES),
    }
    return _indekss


def _kodi(vertiba) -> list[str]:
    if vertiba is None:
        return []
    if isinstance(vertiba, list):
        return [e["kods"] for e in vertiba]
    return [vertiba["kods"]]


# --------------------------------------------------------------------------
# Rīku loģika
# --------------------------------------------------------------------------


# Programma, ko lieto `get_sr_matrix`, ja izsaucējs nav norādījis citu.
NOKLUSETA_PROGRAMMA = "lv.skola2030.mat1"

LISTES_LAUKI = (
    "temats_id", "program_id", "nr", "marker", "nosaukums", "klase", "klasu_grupa",
    "stundas", "stundu_diapazons", "macibu_dienas", "ol_prefikss", "materiali_pieejami",
)

PROGRAMMU_LAUKI = (
    "program_id", "nosaukums", "tips", "kopa", "izglitibas_pakape", "klasu_grupas",
    "klases", "apguves_limenis", "standarta_fails", "autors", "izdevejs", "iestade",
    "skolotajs", "macibu_gads", "revizija", "kalendars", "avots", "faili",
    "izcelsme", "nezinamie_kodi",
)


def _programmas(programma: str | list[str] | None) -> list[dict]:
    """Izvēlas programmas pēc id, kopas id vai "visas".

    Bez norādes — visi programmu paraugi (`tips == "paraugs"`), t. i. Skola2030
    paraugi; reālie skolu stundu plāni jāpieprasa tieši, jo tie ir viena skolas
    gada momentuzņēmumi, nevis vispārīgs saturs.
    """
    visas = indekss()["programmas"]
    if programma is None:
        return [p for p in visas if p["tips"] == "paraugs"]

    prasitas = [programma] if isinstance(programma, str) else list(programma)
    izvele: list[dict] = []
    for prasita in prasitas:
        prasita = prasita.strip()
        if prasita.lower() in ("visas", "*", "all"):
            return visas
        atbilst = [p for p in visas
                   if prasita in (p["program_id"], p.get("kopa"))]
        if not atbilst:
            _nezinama_programma(prasita)
        izvele.extend(p for p in atbilst if p not in izvele)
    return izvele


def _nezinama_programma(prasita: str) -> None:
    ix = indekss()
    saraksts = "\n".join(
        f"  {p['program_id']:24} {p['tips']:13} {p['nosaukums']}"
        for p in ix["programmas"]
    )
    kopas = ", ".join(sorted(ix["kopas"])) or "nav"
    raise ProgValidateError(
        f"Nezināma programma: {prasita!r}. Pieejamās programmas:\n{saraksts}\n"
        f"Kopas: {kopas}. Visas uzreiz: 'visas'."
    )


def list_temati_impl(
    programma: str | list[str] | None = None,
    klase: int | None = None,
    klasu_grupa: str | None = None,
) -> list[dict]:
    temati = []
    for p in _programmas(programma):
        for t in p["temati"]:
            if klase is not None and t["klase"] != klase:
                continue
            if klasu_grupa is not None and t["klasu_grupa"] != klasu_grupa:
                continue
            temati.append({k: t.get(k) for k in LISTES_LAUKI})
    return temati


def list_programs_impl(
    tips: str | None = None,
    klase: int | None = None,
    klasu_grupa: str | None = None,
    macibu_gads: str | None = None,
) -> dict:
    ix = indekss()
    programmas = []
    for p in ix["programmas"]:
        if tips is not None and p["tips"] != tips:
            continue
        if klase is not None and klase not in (p["klases"] or []):
            continue
        if klasu_grupa is not None and klasu_grupa not in p["klasu_grupas"]:
            continue
        if macibu_gads is not None and p["macibu_gads"] != macibu_gads:
            continue

        kopsavilkums = {k: p.get(k) for k in PROGRAMMU_LAUKI}
        kopsavilkums["tematu_skaits"] = len(p["temati"])
        kopsavilkums["stundas_kopa"] = sum(t["stundas"] or 0 for t in p["temati"]) or None
        kopsavilkums["temati_ar_materialiem"] = sum(
            1 for t in p["temati"] if t.get("materiali_pieejami")
        )
        kopsavilkums["sr_bloki"] = sum(len(t["programmas_sr_bloki"]) for t in p["temati"])
        kopsavilkums["citetie_kodi"] = len({
            k for t in p["temati"] for b in t["programmas_sr_bloki"] for k in b["citetie_kodi"]
        })
        programmas.append(kopsavilkums)

    izmantotas_kopas = {p["kopa"] for p in programmas if p["kopa"]}
    return {
        "programmas": programmas,
        "kopas": [
            {"kopa": k, **v, "programmas": sorted(
                p["program_id"] for p in programmas if p["kopa"] == k
            )}
            for k, v in ix["kopas"].items() if k in izmantotas_kopas
        ],
        "noklusetais_atlases_kriterijs": "bez filtriem — visas reģistrētās programmas",
    }


def _atrod_tematu(temats: int | str, programma: str | list[str] | None = None) -> tuple[dict, dict]:
    """`(programma, temats)` pēc temata id, OL prefiksa, marķiera vai kārtas nr."""
    kandidati = _programmas(programma if programma is not None else NOKLUSETA_PROGRAMMA)

    if isinstance(temats, str):
        atslega = temats.strip()
        if "#" in atslega:  # pilns temata id — programma izriet no tā
            kandidati = _programmas(atslega.split("#", 1)[0])
        for p in kandidati:
            for t in p["temati"]:
                if atslega in (t["temats_id"], t["marker"], t["marker"].rstrip(".")):
                    return p, t
                if t["ol_prefikss"] and atslega.upper() == t["ol_prefikss"]:
                    return p, t
        if not atslega.isdigit():
            _neatrasts(temats, kandidati)
        temats = int(atslega)

    for p in kandidati:
        for t in p["temati"]:
            if t["nr"] == temats:
                return p, t
    _neatrasts(temats, kandidati)


def _neatrasts(temats, kandidati: list[dict]) -> None:
    rindas = []
    for p in kandidati:
        rindas.append(f"  [{p['program_id']}] {p['nosaukums']}")
        rindas += [
            f"    {t['marker']:8} {t['nosaukums']}"
            + (f" ({t['stundas']} h)" if t["stundas"] else "")
            for t in p["temati"]
        ]
    raise ProgValidateError(
        f"Nezināms temats: {temats!r}. Pieejamie temati:\n" + "\n".join(rindas)
    )


def _standarta_matrica(kodi: list[str], limeni: list[str]) -> list[dict]:
    ix = indekss()
    izlaist = {LIMENU_LAUKI[b] for b in VISI_LIMENI if b not in limeni}
    matrica: list[dict] = []
    redzetie: set[str] = set()

    for kods in kodi:
        rinda = ix["rindas_pec_koda"].get(kods)
        if rinda is None or rinda["rinda_id"] in redzetie:
            continue
        redzetie.add(rinda["rinda_id"])
        matrica.append({k: v for k, v in rinda.items() if k not in izlaist})
    return matrica


def _materialu_faili(temats: dict) -> list[Path]:
    return [DATA_DIR / rel for rel in temats.get("faili", [])]


def get_sr_matrix_impl(
    temats: int | str,
    limeni: list[str] | None = None,
    ieklaut_parklajumu: bool = True,
    programma: str | None = None,
) -> dict:
    ix = indekss()
    prog, pilns = _atrod_tematu(temats, programma)
    limeni = [l.upper() for l in (limeni or VISI_LIMENI)]
    if nederigi := [l for l in limeni if l not in VISI_LIMENI]:
        raise ProgValidateError(f"Nederīgi apguves līmeņi: {nederigi}. Atļautie: V, O, A.")

    bridinajumi: list[str] = []
    if prog["tips"] == "stundu_plans":
        bridinajumi.append(
            f"{prog['program_id']} ir stundu plāns — tam nav standarta SR bloku; "
            "atgriezti temata metadati, kalendārs un ievestie jēdzieni."
        )

    rekina_parklajumu = ieklaut_parklajumu and pilns.get("materiali_pieejami", False)
    if ieklaut_parklajumu and not rekina_parklajumu:
        bridinajumi.append(
            f"Tematam {pilns['marker']} ({pilns['ol_prefikss'] or 'bez OL prefiksa'}) "
            "nav OL materiālu — pārklājums nav aprēķināts."
        )

    faili = _materialu_faili(pilns) if rekina_parklajumu else []
    visi_kodi: list[str] = []
    bloki: list[dict] = []
    skaititajs = {"pilns": 0, "dalejs": 0, "tikai_pieminets": 0, "nav_atrasts": 0, "nav_piemerojams": 0}

    for bloks in pilns["programmas_sr_bloki"]:
        visi_kodi.extend(bloks["citetie_kodi"])
        # Bloks, kura visi citētie kodi ir caurviju (Li.1, Li.2), v1 netiek vērtēts.
        tikai_caurviju = bool(bloks["citetie_kodi"]) and all(
            (ix["rindas_pec_koda"].get(k) or {}).get("tips") == "caurviju"
            for k in bloks["citetie_kodi"]
        )

        sr_saraksts = []
        for sr in bloks["programmas_sr"]:
            ieraksts = dict(sr)
            if rekina_parklajumu:
                if parraksts := ix["overrides"].get(sr["id"]):
                    parklajums = {
                        "statuss": parraksts.get("statuss", "nav_atrasts"),
                        "vietas": parraksts.get("vietas", []),
                        "komentars": parraksts.get("komentars", "Manuāla korekcija."),
                    }
                elif tikai_caurviju:
                    parklajums = {
                        "statuss": "nav_piemerojams",
                        "vietas": [],
                        "komentars": "Caurviju SR (Li.1/Li.2) — leksiski nav pārbaudāms.",
                    }
                else:
                    parklajums = cov.novertē_sr(sr["teksts"], faili)
                ieraksts["parklajums"] = parklajums
                skaititajs[parklajums["statuss"]] = skaititajs.get(parklajums["statuss"], 0) + 1
            sr_saraksts.append(ieraksts)

        bloki.append(
            {
                "bloks": bloks["bloks"],
                "citetie_kodi": bloks["citetie_kodi"],
                "programmas_sr": sr_saraksts,
            }
        )

    unikalie_kodi = list(dict.fromkeys(visi_kodi))
    matrica = _standarta_matrica(unikalie_kodi, limeni)

    atbilde = {
        "programma": {
            "program_id": prog["program_id"],
            "nosaukums": prog["nosaukums"],
            "tips": prog["tips"],
            "apguves_limenis": prog["apguves_limenis"],
            "izglitibas_pakape": prog["izglitibas_pakape"],
        },
        "temats": {
            "temats_id": pilns["temats_id"],
            "nr": pilns["nr"],
            "marker": pilns["marker"],
            "ol_prefikss": pilns["ol_prefikss"],
            "nosaukums": pilns["nosaukums"],
            "klase": pilns["klase"],
            "klasu_grupa": pilns["klasu_grupa"],
            "stundas": pilns["stundas"],
            "stundu_diapazons": pilns["stundu_diapazons"],
            "macibu_dienas": pilns["macibu_dienas"],
            "merkis": pilns["merkis"],
            "jedzieni": pilns["jedzieni"],
            **({"macits": pilns["macits"], "parbaudes_darbi": pilns["parbaudes_darbi"]}
               if "macits" in pilns else {}),
        },
        "programmas_sr_bloki": bloki,
        "standarta_matrica": matrica,
        "parklajuma_kopsavilkums": None,
    }

    if rekina_parklajumu:
        atbilde["parklajuma_kopsavilkums"] = {
            "programmas_sr_kopa": sum(skaititajs.values()),
            **skaititajs,
            "limena_bridinajumi": cov.limena_bridinajumi(matrica, faili) if "A" in limeni else [],
        }
    if bridinajumi:
        atbilde["bridinajumi"] = bridinajumi

    return atbilde


# --------------------------------------------------------------------------
# Transporta drošība (DNS-rebinding aizsardzība)
# --------------------------------------------------------------------------
# MCP SDK pēc noklusējuma atļauj tikai localhost Host/Origin galvenes un noraida
# pārējās ar 421 ("Invalid Host header") / 403 ("Invalid Origin"). Aiz TLS
# reverse-proxy (Nginx) backends redz PUBLISKO resursdatoru
# (Host: eliozo.dudajevagatve.lv), tāpēc bez šī allow-list neviens publiskais
# pieprasījums netiek apkalpots — tieši tas izraisīja claude.ai savienojuma kļūdu.
#
# Aizsardzība paliek IESLĒGTA — atļaujam tikai konkrētās vērtības (drošāk nekā to
# pilnībā izslēgt; ļaunprātīgs Host joprojām tiek noraidīts). Serviss ir tikai
# lasāms un bez autentifikācijas. Vērtības pārrakstāmas ar env mainīgajiem
# PROG_VALIDATE_ALLOWED_HOSTS / PROG_VALIDATE_ALLOWED_ORIGINS (komatatdalīti).

def _saraksts_no_env(nosaukums: str, noklusejums: list[str]) -> list[str]:
    raw = os.environ.get(nosaukums)
    if raw is None:
        return noklusejums
    return [x.strip() for x in raw.split(",") if x.strip()]


_ATLAUTIE_HOSTI = _saraksts_no_env(
    "PROG_VALIDATE_ALLOWED_HOSTS",
    ["eliozo.dudajevagatve.lv", "eliozo.dudajevagatve.lv:*",
     "127.0.0.1:*", "localhost:*", "[::1]:*"],
)
_ATLAUTIE_ORIGINS = _saraksts_no_env(
    "PROG_VALIDATE_ALLOWED_ORIGINS",
    ["https://eliozo.dudajevagatve.lv", "https://claude.ai",
     "http://127.0.0.1:*", "http://localhost:*", "http://[::1]:*"],
)


# --------------------------------------------------------------------------
# MCP
# --------------------------------------------------------------------------

try:
    from mcp.server.transport_security import TransportSecuritySettings

    mcp = FastMCP(
        "prog-validate",
        transport_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=True,
            allowed_hosts=_ATLAUTIE_HOSTI,
            allowed_origins=_ATLAUTIE_ORIGINS,
        ),
    )
except ImportError:
    # Vecāks MCP SDK bez TransportSecuritySettings — tādās versijās nav arī
    # noklusējuma DNS-rebinding aizsardzības, tāpēc publiskie pieprasījumi strādā
    # bez papildu konfigurācijas.
    mcp = FastMCP("prog-validate")


@mcp.tool(
    description=(
        "Uzskaita servisā reģistrētās mācību programmas: Skola2030 programmu paraugus "
        "(tips 'paraugs') un reālus skolu stundu plānus ar kalendāru (tips 'stundu_plans'). "
        "Paralēlās klases ir atsevišķas programmas, jo tās mācīja dažādi skolotāji; "
        "vienam skolas gadam tās sasaista lauks 'kopa'. Iegūtos 'program_id' lieto "
        "'list_temati' un 'get_sr_matrix' izsaukumos."
    )
)
def list_programs(
    tips: Literal["paraugs", "stundu_plans"] | None = None,
    klase: int | None = None,
    klasu_grupa: Literal["1-3", "4-6", "7-9", "10-12"] | None = None,
    macibu_gads: str | None = None,
) -> dict:
    """
    Args:
        tips: Atlasa tikai programmu paraugus vai tikai stundu plānus.
        klase: Atlasa programmas, kas aptver šo klasi (piem. 7).
        klasu_grupa: Atlasa programmas, kas aptver šo klašu grupu.
        macibu_gads: Piem. '2025/2026' (tikai stundu plāniem).
    """
    return list_programs_impl(tips, klase, klasu_grupa, macibu_gads)


@mcp.tool(
    description=(
        "Atgriež mācību programmu tematu sarakstu (temata id, marķieris, nosaukums, klase, "
        "klašu grupa, stundas, vai pieejami OL mācību materiāli). Bez 'programma' norādes "
        "uzskaita visus programmu paraugus; stundu plānus pieprasa ar to program_id, kopas "
        "id vai 'visas'. Programmu sarakstu sk. 'list_programs'."
    )
)
def list_temati(
    programma: str | list[str] | None = None,
    klase: int | None = None,
    klasu_grupa: Literal["1-3", "4-6", "7-9", "10-12"] | None = None,
) -> list[dict]:
    """
    Args:
        programma: program_id ('lv.skola2030.mat2'), kopas id ('lv.avg.2025-26'),
            šādu vērtību saraksts vai 'visas'. Noklusējums — visi programmu paraugi.
        klase: Atlasa tikai šīs klases tematus (piem. 7).
        klasu_grupa: Atlasa tikai šīs klašu grupas tematus.
    """
    return list_temati_impl(programma, klase, klasu_grupa)


@mcp.tool(
    description=(
        "Atgriež programmas temata SR matricu: temata metadatus, programmas SR blokus, "
        "citēto standarta kodu pilnās rindas (vidusskolai visi trīs apguves līmeņi, "
        "pamatskolai visas trīs klašu grupas) un (pēc izvēles) pārklājumu OL materiālos."
    )
)
def get_sr_matrix(
    temats: int | str,
    limeni: list[Literal["V", "O", "A"]] | None = None,
    ieklaut_parklajumu: bool = True,
    programma: str | None = None,
) -> dict:
    """
    Args:
        temats: Temata identifikators: pilns id ('lv.skola2030.mat2#T03'), marķieris
            programmā ('A7.1.'), OL faila prefikss ('OL_12') vai kārtas numurs.
        limeni: Kurus apguves līmeņus iekļaut standarta matricā (attiecas uz vidusskolas
            rindām). Noklusējums — visi trīs.
        ieklaut_parklajumu: Vai aprēķināt pārklājumu OL_<nr> materiālos (dārgāka operācija).
        programma: Kurā programmā meklēt tematu. Noklusējums — 'lv.skola2030.mat1'.
    """
    return get_sr_matrix_impl(temats, limeni, ieklaut_parklajumu, programma)


def _pievieno_rest_marsrutus() -> None:
    """REST atkļūdošanas maršruti tai pašai ASGI lietotnei (tikai HTTP režīmā)."""
    from starlette.requests import Request
    from starlette.responses import JSONResponse

    def _json(dati, status: int = 200) -> JSONResponse:
        return JSONResponse(dati, status_code=status)

    def _int(vards: str, params) -> int | None:
        vertiba = params.get(vards)
        return int(vertiba) if vertiba and vertiba.isdigit() else None

    @mcp.custom_route("/api/v1/programmas", methods=["GET"])
    async def _programmu_saraksts(request: Request) -> JSONResponse:
        q = request.query_params
        try:
            return _json(list_programs_impl(
                q.get("tips"), _int("klase", q), q.get("klasu_grupa"), q.get("macibu_gads")
            ))
        except ProgValidateError as e:
            return _json({"error": str(e)}, 500)

    @mcp.custom_route("/api/v1/temati", methods=["GET"])
    async def _temati(request: Request) -> JSONResponse:
        q = request.query_params
        try:
            return _json(list_temati_impl(
                q.get("programma"), _int("klase", q), q.get("klasu_grupa")
            ))
        except ProgValidateError as e:
            return _json({"error": str(e)}, 404)

    @mcp.custom_route("/api/v1/sr-matrix/{temats}", methods=["GET"])
    async def _sr_matrix(request: Request) -> JSONResponse:
        temats = request.path_params["temats"]
        q = request.query_params
        limeni = [l for l in q.get("limeni", "V,O,A").split(",") if l]
        parklajums = q.get("parklajums", "true").lower() != "false"
        try:
            return _json(get_sr_matrix_impl(temats, limeni, parklajums, q.get("programma")))
        except ProgValidateError as e:
            return _json({"error": str(e)}, 404)


def main() -> None:
    for straume in (sys.stdout, sys.stderr):
        try:
            straume.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="prog-validate MCP serviss")
    ap.add_argument("--transport", choices=["stdio", "streamable-http"], default="stdio")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.settings.host = args.host
        mcp.settings.port = args.port
        _pievieno_rest_marsrutus()
        mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
