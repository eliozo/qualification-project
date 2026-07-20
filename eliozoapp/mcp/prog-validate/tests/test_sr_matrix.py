"""Akcepttesti pēc SPEC 7. sadaļas (T1–T8)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SAKNE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SAKNE))

import build_index  # noqa: E402
import server  # noqa: E402

LIMENU_LAUKI = ("visparigais", "optimalais", "augstakais")


@pytest.fixture(scope="session", autouse=True)
def indekss(tmp_path_factory):
    """Pārbūvē indeksu tīrā mapē, lai testi netiktu ietekmēti no vecas kopijas."""
    out = tmp_path_factory.mktemp("index")
    build_index.build(SAKNE / "data", out, kluss=True)
    server.INDEX_DIR = out
    server._indekss = None
    yield out


@pytest.fixture(scope="session")
def standarts(indekss):
    return json.loads((indekss / "standarts.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def programma(indekss):
    return json.loads((indekss / "programma.json").read_text(encoding="utf-8"))


def _kodi(vertiba) -> list[str]:
    if vertiba is None:
        return []
    if isinstance(vertiba, list):
        return [e["kods"] for e in vertiba]
    return [vertiba["kods"]]


def _rinda(standarts: dict, rinda_id: str) -> dict:
    return next(r for r in standarts["rindas"] if r["rinda_id"] == rinda_id)


# --- T1 -------------------------------------------------------------------

def test_t1_standarta_pilnigums(standarts):
    """212 unikāli kodi; katrs kods parādās tieši vienā rindā."""
    kodu_rindas: dict[str, set[str]] = {}
    for rinda in standarts["rindas"]:
        for lauks in LIMENU_LAUKI:
            for kods in _kodi(rinda[lauks]):
                kodu_rindas.setdefault(kods, set()).add(rinda["rinda_id"])

    assert len(kodu_rindas) == 212
    daudzas = {k: v for k, v in kodu_rindas.items() if len(v) > 1}
    assert not daudzas, f"Kodi vairākās rindās: {daudzas}"


# --- T2 -------------------------------------------------------------------

def test_t2_tuksas_sunas(standarts):
    rinda = _rinda(standarts, "6.2.5")
    assert rinda["visparigais"] is None
    assert rinda["augstakais"] is None
    assert rinda["optimalais"]["kods"] == "M.O.6.2.5."


# --- T3 -------------------------------------------------------------------

def test_t3_daudzkodu_suna(standarts):
    augstakais = _rinda(standarts, "1.2.4")["augstakais"]
    assert isinstance(augstakais, list)
    assert [e["kods"] for e in augstakais] == ["M.A.1.2.4.", "M.A.1.2.5."]
    assert all(e["teksts"] for e in augstakais)


# --- T4 -------------------------------------------------------------------

SAGAIDAMIE_BLOKI = [
    "Vienādojums ar diviem nezināmajiem",
    "Taisnes vienādojums",
    "Riņķa līnijas vienādojums",
    "Nevienādības un to sistēmas ar diviem mainīgajiem",
]

SAGAIDAMIE_KODI = {
    "M.O.1.2.3.", "M.O.2.1.1.", "M.O.4.5.1.", "M.O.4.5.6.",
    "M.O.6.2.4.", "M.O.6.2.5.", "M.O.6.2.6.", "M.O.6.2.7.",
}


@pytest.fixture(scope="session")
def t12(indekss):
    return server.get_sr_matrix_impl(12, ieklaut_parklajumu=False)


def test_t4_temata_metadati(t12):
    assert t12["temats"]["nr"] == 12
    assert t12["temats"]["stundas"] == 20
    assert t12["temats"]["nosaukums"].startswith("Līnijas vienādojums")
    assert t12["temats"]["ol_prefikss"] == "OL_12"


def test_t4_bloku_skaits_un_seciba(t12):
    assert [b["bloks"] for b in t12["programmas_sr_bloki"]] == SAGAIDAMIE_BLOKI


def test_t4_unikalie_citetie_kodi(t12):
    kodi = {k for b in t12["programmas_sr_bloki"] for k in b["citetie_kodi"]}
    assert kodi == SAGAIDAMIE_KODI


def test_t4_standarta_matrica(t12):
    matrica = t12["standarta_matrica"]
    assert len(matrica) == 8

    pec_id = {r["rinda_id"]: r for r in matrica}
    for rinda_id in ("6.2.5", "6.2.6", "6.2.7", "4.5.6"):
        assert pec_id[rinda_id]["visparigais"] is None, rinda_id
    for rinda_id in ("6.2.5", "6.2.6", "6.2.7"):
        assert pec_id[rinda_id]["augstakais"] is None, rinda_id

    assert pec_id["1.2.3"]["tips"] == "caurviju"
    assert pec_id["2.1.1"]["tips"] == "caurviju"
    assert pec_id["6.2.4"]["tips"] == "satura"


# --- T5 -------------------------------------------------------------------

def test_t5_ekvivalence(indekss):
    ar_skaitli = server.get_sr_matrix_impl(12, ieklaut_parklajumu=True)
    ar_prefiksu = server.get_sr_matrix_impl("OL_12", ieklaut_parklajumu=True)
    assert ar_skaitli == ar_prefiksu


# --- T6 -------------------------------------------------------------------

def test_t6_limenu_filtrs(indekss):
    atbilde = server.get_sr_matrix_impl(12, limeni=["O"], ieklaut_parklajumu=False)
    for rinda in atbilde["standarta_matrica"]:
        assert "visparigais" not in rinda
        assert "augstakais" not in rinda
        assert rinda["optimalais"]["kods"].startswith("M.O.")


# --- T7 -------------------------------------------------------------------

def test_t7_nezinams_temats(indekss):
    with pytest.raises(server.ProgValidateError) as exc:
        server.get_sr_matrix_impl(99)

    zinojums = str(exc.value)
    nosaukumi = [t["nosaukums"] for t in server.list_temati_impl()]
    atrastie = [n for n in nosaukumi if n in zinojums]
    assert len(atrastie) >= 10, f"Kļūdas tekstā tikai {len(atrastie)} tematu nosaukumi"


# --- T8 -------------------------------------------------------------------

def test_t8_citeto_kodu_eksistence(standarts, programma):
    standarta_kodi = {
        kods
        for rinda in standarts["rindas"]
        for lauks in LIMENU_LAUKI
        for kods in _kodi(rinda[lauks])
    }
    citetie = {
        kods
        for temats in programma["temati"]
        for bloks in temats["programmas_sr_bloki"]
        for kods in bloks["citetie_kodi"]
    }
    assert citetie, "Programmā nav atrasts neviens citēts kods"
    assert citetie <= standarta_kodi, f"Ārpus standarta: {sorted(citetie - standarta_kodi)}"


# --- Papildu: pārklājuma slānis un list_temati ----------------------------

def test_list_temati_shema(indekss):
    temati = server.list_temati_impl()
    assert len(temati) >= 13
    assert {"nr", "nosaukums", "stundas", "ol_prefikss", "materiali_pieejami"} == set(temati[0])


def test_parklajums_tematam_ar_materialiem(indekss):
    atbilde = server.get_sr_matrix_impl(12, ieklaut_parklajumu=True)
    kopsavilkums = atbilde["parklajuma_kopsavilkums"]
    assert kopsavilkums is not None

    sr_skaits = sum(len(b["programmas_sr"]) for b in atbilde["programmas_sr_bloki"])
    assert kopsavilkums["programmas_sr_kopa"] == sr_skaits

    statusi = {"pilns", "dalejs", "tikai_pieminets", "nav_atrasts", "nav_piemerojams"}
    for bloks in atbilde["programmas_sr_bloki"]:
        for sr in bloks["programmas_sr"]:
            assert sr["parklajums"]["statuss"] in statusi


def test_temats_bez_materialiem_atgriez_bridinajumu(indekss):
    bez = next(t for t in server.list_temati_impl() if not t["materiali_pieejami"])
    atbilde = server.get_sr_matrix_impl(bez["nr"], ieklaut_parklajumu=True)
    assert atbilde["parklajuma_kopsavilkums"] is None
    assert atbilde["bridinajumi"]


def test_truksts_indeksa_faili_dod_noraditu_kludu(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "INDEX_DIR", tmp_path / "nav")
    monkeypatch.setattr(server, "_indekss", None)
    with pytest.raises(server.ProgValidateError, match="build_index.py"):
        server.list_temati_impl()
    server._indekss = None
