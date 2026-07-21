#!/usr/bin/env python3
"""`prog-validate` MCP serviss: rīki `get_sr_matrix` un `list_temati`.

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

    trukst = [f for f in ("standarts.json", "programma.json", "temati.json")
              if not (INDEX_DIR / f).exists()]
    if trukst:
        raise ProgValidateError(
            f"Trūkst indeksa faili ({', '.join(trukst)}) mapē {INDEX_DIR}. "
            "Palaid: python build_index.py --data ./data"
        )

    def ielasa(vards: str) -> dict:
        return json.loads((INDEX_DIR / vards).read_text(encoding="utf-8"))

    standarts = ielasa("standarts.json")
    _indekss = {
        "standarts": standarts,
        "rindas_pec_koda": {
            kods: rinda
            for rinda in standarts["rindas"]
            for lauks in LIMENU_LAUKI.values()
            for kods in _kodi(rinda.get(lauks))
        },
        "programma": ielasa("programma.json"),
        "temati": ielasa("temati.json")["temati"],
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


def list_temati_impl() -> list[dict]:
    return [
        {k: t[k] for k in ("nr", "nosaukums", "stundas", "ol_prefikss", "materiali_pieejami")}
        for t in indekss()["temati"]
    ]


def _atrod_tematu(temats: int | str) -> dict:
    ix = indekss()
    if isinstance(temats, str):
        temats = temats.strip()
        if temats.upper().startswith("OL_"):
            atslega = temats.upper()
            atrasts = next((t for t in ix["temati"] if t["ol_prefikss"] == atslega), None)
            if atrasts:
                return atrasts
            _neatrasts(temats)
        elif temats.isdigit():
            temats = int(temats)
        else:
            _neatrasts(temats)

    atrasts = next((t for t in ix["temati"] if t["nr"] == temats), None)
    if atrasts is None:
        _neatrasts(temats)
    return atrasts


def _neatrasts(temats) -> None:
    saraksts = "\n".join(
        f"  {t['nr']}. {t['nosaukums']} ({t['stundas']} h)" for t in indekss()["temati"]
    )
    raise ProgValidateError(
        f"Nezināms temats: {temats!r}. Pieejamie programmas parauga temati:\n{saraksts}"
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
) -> dict:
    ix = indekss()
    kopsavilkums = _atrod_tematu(temats)
    limeni = [l.upper() for l in (limeni or VISI_LIMENI)]
    if nederigi := [l for l in limeni if l not in VISI_LIMENI]:
        raise ProgValidateError(f"Nederīgi apguves līmeņi: {nederigi}. Atļautie: V, O, A.")

    pilns = next(t for t in ix["programma"]["temati"] if t["nr"] == kopsavilkums["nr"])
    bridinajumi: list[str] = []

    rekina_parklajumu = ieklaut_parklajumu and kopsavilkums["materiali_pieejami"]
    if ieklaut_parklajumu and not rekina_parklajumu:
        bridinajumi.append(
            f"Tematam {kopsavilkums['nr']} ({kopsavilkums['ol_prefikss']}) nav OL materiālu — "
            "pārklājums nav aprēķināts."
        )

    faili = _materialu_faili(kopsavilkums) if rekina_parklajumu else []
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
        "temats": {
            "nr": kopsavilkums["nr"],
            "ol_prefikss": kopsavilkums["ol_prefikss"],
            "nosaukums": kopsavilkums["nosaukums"],
            "stundas": kopsavilkums["stundas"],
            "kurss": pilns["kurss"],
            "apguves_limenis": pilns["apguves_limenis"],
            "merkis": pilns["merkis"],
            "jedzieni": pilns["jedzieni"],
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
        "Atgriež visu programmas paraugā atrasto tematu sarakstu "
        "(nr, nosaukums, stundas, OL prefikss, vai pieejami mācību materiāli)."
    )
)
def list_temati() -> list[dict]:
    return list_temati_impl()


@mcp.tool(
    description=(
        "Atgriež programmas parauga temata SR matricu: temata metadatus, programmas SR "
        "blokus, citēto standarta kodu pilnās rindas (visi trīs apguves līmeņi) un "
        "(pēc izvēles) pārklājumu OL materiālos."
    )
)
def get_sr_matrix(
    temats: int | str,
    limeni: list[Literal["V", "O", "A"]] | None = None,
    ieklaut_parklajumu: bool = True,
) -> dict:
    """
    Args:
        temats: Programmas parauga temata identifikators: vesels skaitlis vai
            OL faila prefikss ('OL_12').
        limeni: Kurus apguves līmeņus iekļaut standarta matricā. Noklusējums — visi trīs.
        ieklaut_parklajumu: Vai aprēķināt pārklājumu OL_<nr> materiālos (dārgāka operācija).
    """
    return get_sr_matrix_impl(temats, limeni, ieklaut_parklajumu)


def _pievieno_rest_marsrutus() -> None:
    """REST atkļūdošanas maršruti tai pašai ASGI lietotnei (tikai HTTP režīmā)."""
    from starlette.requests import Request
    from starlette.responses import JSONResponse

    def _json(dati, status: int = 200) -> JSONResponse:
        return JSONResponse(dati, status_code=status)

    @mcp.custom_route("/api/v1/temati", methods=["GET"])
    async def _temati(request: Request) -> JSONResponse:
        try:
            return _json(list_temati_impl())
        except ProgValidateError as e:
            return _json({"error": str(e)}, 500)

    @mcp.custom_route("/api/v1/sr-matrix/{temats}", methods=["GET"])
    async def _sr_matrix(request: Request) -> JSONResponse:
        temats = request.path_params["temats"]
        limeni = [l for l in request.query_params.get("limeni", "V,O,A").split(",") if l]
        parklajums = request.query_params.get("parklajums", "true").lower() != "false"
        try:
            return _json(get_sr_matrix_impl(temats, limeni, parklajums))
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
