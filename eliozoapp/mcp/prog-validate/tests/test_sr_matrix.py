"""Akcepttesti pēc SPEC 7. sadaļas (T1–T8)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SAKNE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SAKNE))

import build_index  # noqa: E402
import programmas as programmas_modulis  # noqa: E402
import server  # noqa: E402

LIMENU_LAUKI = ("visparigais", "optimalais", "augstakais")
KLASU_GRUPU_LAUKI = ("klases_1_3", "klases_4_6", "klases_7_9")


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
def programmas(indekss):
    return json.loads((indekss / "programmas.json").read_text(encoding="utf-8"))


def _programma(programmas: dict, program_id: str) -> dict:
    return next(p for p in programmas["programmas"] if p["program_id"] == program_id)


def _kodi(vertiba) -> list[str]:
    if vertiba is None:
        return []
    if isinstance(vertiba, list):
        return [e["kods"] for e in vertiba]
    return [vertiba["kods"]]


def _rinda(standarts: dict, rinda_id: str) -> dict:
    return next(r for r in standarts["rindas"] if r["rinda_id"] == rinda_id)


def _rindas(standarts: dict, pakape: str) -> list[dict]:
    return [r for r in standarts["rindas"] if r["izglitibas_pakape"] == pakape]


def _kodu_rindas(rindas: list[dict], lauki: tuple[str, ...]) -> dict[str, set[str]]:
    kodu_rindas: dict[str, set[str]] = {}
    for rinda in rindas:
        for lauks in lauki:
            for kods in _kodi(rinda[lauks]):
                kodu_rindas.setdefault(kods, set()).add(rinda["rinda_id"])
    return kodu_rindas


# --- T1 -------------------------------------------------------------------

def test_t1_standarta_pilnigums(standarts):
    """Vidusskolā 212 unikāli kodi; katrs kods parādās tieši vienā rindā."""
    kodu_rindas = _kodu_rindas(_rindas(standarts, "vidusskola"), LIMENU_LAUKI)

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
    nosaukumi = [t["nosaukums"] for t in server.list_temati_impl(server.NOKLUSETA_PROGRAMMA)]
    atrastie = [n for n in nosaukumi if n in zinojums]
    assert len(atrastie) >= 10, f"Kļūdas tekstā tikai {len(atrastie)} tematu nosaukumi"


# --- T8 -------------------------------------------------------------------

def test_t8_citeto_kodu_eksistence(standarts, programmas):
    """Katrs citētais kods ir standartā; izņēmumi fiksēti `nezinamie_kodi`."""
    standarta_kodi = set(standarts["kodu_indekss"])
    for p in programmas["programmas"]:
        citetie = {
            kods
            for temats in p["temati"]
            for bloks in temats["programmas_sr_bloki"]
            for kods in bloks["citetie_kodi"]
        }
        arpus = citetie - standarta_kodi
        assert arpus == set(p["nezinamie_kodi"]), p["program_id"]

    # Vidusskolas paraugi citē tikai sava līmeņa kodus, un tie visi ir standartā.
    mat1 = _programma(programmas, "lv.skola2030.mat1")
    mat2 = _programma(programmas, "lv.skola2030.mat2")
    assert mat1["nezinamie_kodi"] == [] and mat2["nezinamie_kodi"] == []
    assert all(
        k.startswith("M.O.")
        for t in mat1["temati"] for b in t["programmas_sr_bloki"] for k in b["citetie_kodi"]
    )
    assert all(
        k.startswith("M.A.")
        for t in mat2["temati"] for b in t["programmas_sr_bloki"] for k in b["citetie_kodi"]
    )


# --- Papildu: pārklājuma slānis un list_temati ----------------------------

def test_list_temati_shema(indekss):
    temati = server.list_temati_impl()
    assert len(temati) >= 13
    assert set(server.LISTES_LAUKI) == set(temati[0])
    # Bez norādes — visi programmu paraugi, stundu plāni netiek iekļauti.
    assert {t["program_id"] for t in temati} == {
        "lv.skola2030.mat1", "lv.skola2030.mat1-9", "lv.skola2030.mat2"
    }


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


# --- Pamatskolas standarts (M.3./M.6./M.9. kodi) --------------------------

def test_pamatskolas_kodi_ir_indeksa(standarts):
    """Katrs pamatskolas kods parādās tieši vienā rindā un vienā klašu grupā."""
    kodu_rindas = _kodu_rindas(_rindas(standarts, "pamatskola"), KLASU_GRUPU_LAUKI)

    assert len(kodu_rindas) == 219
    daudzas = {k: v for k, v in kodu_rindas.items() if len(v) > 1}
    assert not daudzas, f"Kodi vairākās rindās: {daudzas}"
    assert kodu_rindas.keys() == set(
        k for k, m in standarts["kodu_indekss"].items()
        if m["izglitibas_pakape"] == "pamatskola"
    )


def test_pamatskolai_nav_apguves_limenu(standarts):
    """1.–9. klasē visi apgūst to pašu — V/O/A lauku pamatskolas rindās nav."""
    for rinda in _rindas(standarts, "pamatskola"):
        assert not set(rinda) & set(LIMENU_LAUKI)
        assert "limenis" not in rinda


def test_spirale_saglabata_rinda(standarts):
    """Blakus šūnas rindā ir viens temats trijās klašu grupās."""
    rinda = _rinda(standarts, "PSK.1.1.1")
    assert rinda["klasu_grupas"] == ["1-3", "4-6", "7-9"]
    assert rinda["klases_1_3"]["kods"] == "M.3.1.1.1."
    assert [e["kods"] for e in rinda["klases_4_6"]] == ["M.6.1.1.1.", "M.6.1.1.2."]
    assert rinda["klases_7_9"]["kods"] == "M.9.1.1.1."

    # Tukša šūna: šī temata 1.–3. klasē vēl nav.
    bez_saknes = _rinda(standarts, "PSK.1.1.3")
    assert bez_saknes["klases_1_3"] is None
    assert bez_saknes["klasu_grupas"] == ["4-6", "7-9"]


def test_klasu_grupas_atskir_pakapes(standarts):
    grupas = {g["kods"]: g for g in standarts["klasu_grupas"]}
    assert set(grupas) == {"1-3", "4-6", "7-9", "10-12"}

    ki = standarts["kodu_indekss"]
    assert ki["M.3.6.4.1."]["klasu_grupa"] == "1-3"
    assert ki["M.6.6.4.1."]["klasu_grupa"] == "4-6"
    assert ki["M.9.6.4.1."]["klasu_grupa"] == "7-9"
    assert ki["M.O.6.2.4."]["klasu_grupa"] == "10-12"
    assert ki["M.O.6.2.4."]["limenis"] == "optimalais"
    # Visi vidusskolas standarta temati ir 10.–12. klase.
    for rinda in _rindas(standarts, "vidusskola"):
        assert rinda["klasu_grupas"] == ["10-12"]


def test_pamatskolas_kods_atrodams_serverī(indekss):
    rinda = server.indekss()["rindas_pec_koda"]["M.9.4.3.4."]
    assert rinda["rinda_id"] == "PSK.4.3.1"
    assert rinda["izglitibas_pakape"] == "pamatskola"
    assert server.indekss()["kodu_indekss"]["M.9.4.3.4."]["beidzot_klasi"] == 9


def test_caurviju_tips_ari_pamatskola(standarts):
    ki = standarts["kodu_indekss"]
    assert ki["M.3.1.1.1."]["tips"] == "caurviju"   # Li.1 – matemātikas valoda
    assert ki["M.6.2.2.1."]["tips"] == "caurviju"   # Li.2 – problēmrisināšana
    assert ki["M.9.3.1.1."]["tips"] == "satura"


# --- Programmu reģistrs un list_programs ----------------------------------

VISAS_PROGRAMMAS = {
    "lv.skola2030.mat1", "lv.skola2030.mat2", "lv.skola2030.mat1-9",
    "lv.avg.2025-26.7a", "lv.avg.2025-26.8a", "lv.avg.2025-26.9a",
}


def test_registrs_atrod_visas_programmas(programmas):
    assert {p["program_id"] for p in programmas["programmas"]} == VISAS_PROGRAMMAS


def test_failu_nosaukumu_shema(indekss):
    """program_<program_id>[_<loma>].<ext> — id izriet no faila nosaukuma."""
    faili = programmas_modulis.atrod_failus(SAKNE / "data")
    assert set(faili) == VISAS_PROGRAMMAS
    avg = faili["lv.avg.2025-26.7a"]
    assert avg["pamats"] == ["curricula/program_lv.avg.2025-26.7a.json"]
    assert avg["concepts"] == ["curricula/program_lv.avg.2025-26.7a_concepts.csv"]
    assert faili["lv.skola2030.mat2"]["pamats"] == ["curricula/program_lv.skola2030.mat2.md"]


def test_list_programs_metadati(indekss):
    atbilde = server.list_programs_impl()
    pec_id = {p["program_id"]: p for p in atbilde["programmas"]}
    assert set(pec_id) == VISAS_PROGRAMMAS

    mat2 = pec_id["lv.skola2030.mat2"]
    assert (mat2["tips"], mat2["apguves_limenis"], mat2["klasu_grupas"]) == (
        "paraugs", "augstakais", ["10-12"])
    assert mat2["tematu_skaits"] == 15 and mat2["citetie_kodi"] > 0

    mat19 = pec_id["lv.skola2030.mat1-9"]
    assert mat19["izglitibas_pakape"] == "pamatskola"
    assert mat19["apguves_limenis"] is None      # pamatizglītībā līmeņu nav
    assert mat19["klasu_grupas"] == ["1-3", "4-6", "7-9"]

    plans = pec_id["lv.avg.2025-26.7a"]
    assert plans["tips"] == "stundu_plans"
    assert plans["kopa"] == "lv.avg.2025-26"
    assert plans["skolotajs"] and plans["macibu_gads"] == "2025/2026"
    assert plans["kalendars"]["no"] == "2025-09-01"
    assert "curricula/program_lv.avg.2025-26.7a_concepts.csv" in plans["faili"]


def test_list_programs_paralelas_klases_ir_atseviskas_bet_kopa(indekss):
    atbilde = server.list_programs_impl(tips="stundu_plans")
    assert len(atbilde["programmas"]) == 3
    kopa = next(k for k in atbilde["kopas"] if k["kopa"] == "lv.avg.2025-26")
    assert kopa["programmas"] == ["lv.avg.2025-26.7a", "lv.avg.2025-26.8a", "lv.avg.2025-26.9a"]
    assert kopa["iestade"]


def test_list_programs_filtri(indekss):
    def ids(**kw):
        return {p["program_id"] for p in server.list_programs_impl(**kw)["programmas"]}

    assert ids(tips="paraugs") == {
        "lv.skola2030.mat1", "lv.skola2030.mat2", "lv.skola2030.mat1-9"}
    assert ids(klase=7) == {"lv.skola2030.mat1-9", "lv.avg.2025-26.7a"}
    assert ids(klasu_grupa="10-12") == {"lv.skola2030.mat1", "lv.skola2030.mat2"}
    assert ids(macibu_gads="2025/2026") == {
        "lv.avg.2025-26.7a", "lv.avg.2025-26.8a", "lv.avg.2025-26.9a"}
    assert ids(tips="stundu_plans", klase=9) == {"lv.avg.2025-26.9a"}


# --- Programmu atkarīgs list_temati / get_sr_matrix ------------------------

def test_list_temati_pec_programmas(indekss):
    mat2 = server.list_temati_impl("lv.skola2030.mat2")
    assert len(mat2) == 15
    assert all(t["program_id"] == "lv.skola2030.mat2" for t in mat2)
    assert mat2[0]["temats_id"] == "lv.skola2030.mat2#T01"

    # Kopas id izvērš visās tās programmās.
    kopa = server.list_temati_impl("lv.avg.2025-26")
    assert {t["program_id"] for t in kopa} == {
        "lv.avg.2025-26.7a", "lv.avg.2025-26.8a", "lv.avg.2025-26.9a"}

    assert len(server.list_temati_impl("visas")) == len(kopa) + len(server.list_temati_impl())


def test_list_temati_filtre_pec_klases(indekss):
    septitas = server.list_temati_impl("visas", klase=7)
    assert {t["program_id"] for t in septitas} == {
        "lv.skola2030.mat1-9", "lv.avg.2025-26.7a"}
    assert all(t["klasu_grupa"] == "7-9" for t in septitas)

    saakums = server.list_temati_impl("lv.skola2030.mat1-9", klasu_grupa="1-3")
    assert saakums and all(t["klase"] in (1, 2, 3) for t in saakums)


def test_list_temati_nezinama_programma_dod_sarakstu(indekss):
    with pytest.raises(server.ProgValidateError) as exc:
        server.list_temati_impl("nav.tadas")
    assert "lv.skola2030.mat1" in str(exc.value) and "lv.avg.2025-26.7a" in str(exc.value)


def test_get_sr_matrix_citaa_programmaa(indekss):
    """Marķieris `A7.1.` eksistē tikai 1.–9. klases paraugā."""
    atbilde = server.get_sr_matrix_impl(
        "A7.1.", ieklaut_parklajumu=False, programma="lv.skola2030.mat1-9")
    assert atbilde["programma"]["program_id"] == "lv.skola2030.mat1-9"
    assert atbilde["temats"]["klase"] == 7 and atbilde["temats"]["klasu_grupa"] == "7-9"
    # Pamatskolas rindas nāk ar klašu grupu šūnām, ne apguves līmeņiem.
    rinda = atbilde["standarta_matrica"][0]
    assert rinda["izglitibas_pakape"] == "pamatskola"
    assert "klases_7_9" in rinda and "optimalais" not in rinda


def test_get_sr_matrix_pilns_temata_id_nosaka_programmu(indekss):
    atbilde = server.get_sr_matrix_impl("lv.skola2030.mat2#T03", ieklaut_parklajumu=False)
    assert atbilde["programma"]["apguves_limenis"] == "augstakais"
    assert atbilde["temats"]["nosaukums"] == "Funkcija"
    kodi = {k for b in atbilde["programmas_sr_bloki"] for k in b["citetie_kodi"]}
    assert kodi and all(k.startswith("M.A.") for k in kodi)


def test_get_sr_matrix_stundu_planam_dod_bridinajumu(indekss):
    atbilde = server.get_sr_matrix_impl(1, ieklaut_parklajumu=False,
                                        programma="lv.avg.2025-26.7a")
    assert atbilde["programmas_sr_bloki"] == []
    assert atbilde["temats"]["jedzieni"]           # ievestie taksonomijas jēdzieni
    assert atbilde["temats"]["macits"]["from"]["date"] == "2025-09-01"
    assert any("stundu plāns" in b for b in atbilde["bridinajumi"])


def test_sr_id_ir_programmas_meroga(programmas):
    """SR id satur programmu, jo tematu numuri programmās atkārtojas."""
    visi = [
        sr["id"]
        for p in programmas["programmas"]
        for t in p["temati"]
        for b in t["programmas_sr_bloki"]
        for sr in b["programmas_sr"]
    ]
    assert len(visi) == len(set(visi)), "SR id nav unikāli"
    assert all(v.startswith(("lv.skola2030.", "lv.avg.")) for v in visi)


def test_truksts_indeksa_faili_dod_noraditu_kludu(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "INDEX_DIR", tmp_path / "nav")
    monkeypatch.setattr(server, "_indekss", None)
    with pytest.raises(server.ProgValidateError, match="build_index.py"):
        server.list_temati_impl()
    server._indekss = None
