r"""Tests for keyword (exact) and regex search in ``eliozo_dao.search_repository``.

The tests run against a small curated TTL fixture loaded into an in-memory
pyoxigraph store rather than against the full olympiad RDF dump. Rationale:
the dump is rebuilt from ``migration-script/resources`` whenever new olympiads
are added, so any assertion on it ("this regex finds 6 problems") would rot on
the next content import. The fixture below is written in the same shape as the
real data -- Latvian problem statements with LaTeX formulas, ``@lv`` language
tags, problems with zero, one or two solutions -- so it still exercises the
query text for real.

The LaTeX in the fixture is copied in style from actual problems: nested
``\frac``, ``\sqrt[3]{...}``, ``\sin \alpha``, squared binomials. Several of
those patterns deliberately occur *only inside solutions*, which is what
separates the two values of the "search-target" select box in
``main_content.html``.

Note on regex escaping: the pattern reaching these functions is the regex
verbatim, so a literal LaTeX backslash is written ``\\`` (two characters) in
the pattern -- hence the ``r"\\frac"`` spellings below.
"""

import json

import pytest

from eliozo_dao.search_repository import (
    SEARCH_TARGET_PROBLEMS,
    SEARCH_TARGET_SOLUTIONS,
    escape_sparql_literal,
    getProblemsByKeywordSPARQL,
    getProblemsByRegexSPARQL,
    replace_non_ascii_with_unicode_escape,
)


# In TTL a backslash is written doubled, exactly as in the real content files,
# so this is a raw Python string and "\\frac" below is the LaTeX macro \frac.
SEARCH_FIXTURE_TTL = r'''
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .

# --- 5th grade: plain Latvian text, one solution, no interesting LaTeX ------
eliozo:LV.TST.2020.5.1 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.5.1" ;
    eliozo:problemGrade 5 ;
    eliozo:problemText """Nogriežņa $AB$ garums ir $10~\\mathrm{cm}$. Aprēķini
taisnleņķa trijstūra $ABC$ laukumu!"""@lv ;
    eliozo:problemTextHtml """<p>Nogriežņa $AB$ garums ir $10~\\mathrm{cm}$.</p>"""@lv ;
    eliozo:problemSolution eliozo:SOLN.LV.TST.2020.5.1.SUB1 .

eliozo:SOLN.LV.TST.2020.5.1.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText """## Atrisinājums

Laukums ir $\\frac{AB \\cdot h}{2} = 25~\\mathrm{cm}^2$."""@lv ;
    eliozo:solutionTextHtml """<p>Laukums ir $\\frac{AB \\cdot h}{2}$.</p>"""@lv .

# --- 7th grade: square of a binomial in the problem text -------------------
eliozo:LV.TST.2020.7.2 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.7.2" ;
    eliozo:problemGrade 7 ;
    eliozo:problemText """Pierādi, ka $(a+b)^2 \\geq 4ab$ visiem reāliem
skaitļiem $a$ un $b$."""@lv ;
    eliozo:problemTextHtml """<p>Pierādi, ka $(a+b)^2 \\geq 4ab$.</p>"""@lv ;
    eliozo:problemSolution eliozo:SOLN.LV.TST.2020.7.2.SUB1 .

eliozo:SOLN.LV.TST.2020.7.2.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText """Pārveidojam starpību: $(a+b)^2 - 4ab = (a-b)^2 \\geq 0$."""@lv ;
    eliozo:solutionTextHtml """<p>$(a+b)^2 - 4ab = (a-b)^2$.</p>"""@lv .

# --- 8th grade: sines of beta and gamma, and a capitalised word ------------
eliozo:LV.TST.2020.8.3 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.8.3" ;
    eliozo:problemGrade 8 ;
    eliozo:problemText """Pierādi, ka $\\sin \\beta + \\sin \\gamma \\leq 2$
jebkuriem Leņķiem $\\beta$ un $\\gamma$."""@lv ;
    eliozo:problemTextHtml """<p>Pierādi, ka $\\sin \\beta + \\sin \\gamma \\leq 2$.</p>"""@lv .

# --- 9th grade: cubic roots in the problem text, no solution --------------
eliozo:LV.TST.2020.9.4 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.9.4" ;
    eliozo:problemGrade 9 ;
    eliozo:problemText """Aprēķini $\\sqrt[3]{27} + \\sqrt[3]{64}$ vērtību!"""@lv ;
    eliozo:problemTextHtml """<p>Aprēķini $\\sqrt[3]{27} + \\sqrt[3]{64}$.</p>"""@lv .

# --- 10th grade: sine of alpha appears ONLY in the solution ---------------
eliozo:LV.TST.2020.10.5 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.10.5" ;
    eliozo:problemGrade 10 ;
    eliozo:problemText """Vienādsānu trijstūrī leņķis pie virsotnes ir
$\\alpha$, bet sānu mala ir $b$. Aprēķini trijstūra laukumu!"""@lv ;
    eliozo:problemTextHtml """<p>Vienādsānu trijstūrī leņķis ir $\\alpha$.</p>"""@lv ;
    eliozo:problemSolution eliozo:SOLN.LV.TST.2020.10.5.SUB1 .

eliozo:SOLN.LV.TST.2020.10.5.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText """Laukums ir $S = \\frac{1}{2} b^2 \\sin \\alpha$,
jo augstums pret sānu malu ir $b \\sin \\alpha$."""@lv ;
    eliozo:solutionTextHtml """<p>$S = \\frac{1}{2} b^2 \\sin \\alpha$.</p>"""@lv .

# --- 11th grade: fraction in the problem, nested fraction in the solution --
eliozo:LV.TST.2020.11.6 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.11.6" ;
    eliozo:problemGrade 11 ;
    eliozo:problemText """Atrisini vienādojumu $\\frac{x+1}{2} = 3$!"""@lv ;
    eliozo:problemTextHtml """<p>Atrisini vienādojumu $\\frac{x+1}{2} = 3$!</p>"""@lv ;
    eliozo:problemSolution eliozo:SOLN.LV.TST.2020.11.6.SUB1 .

eliozo:SOLN.LV.TST.2020.11.6.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText """Pārrakstām vienādojumu formā
$\\frac{\\frac{x+1}{2}}{3} = 1$ un iegūstam $x = 5$."""@lv ;
    eliozo:solutionTextHtml """<p>$\\frac{\\frac{x+1}{2}}{3} = 1$.</p>"""@lv .

# --- 12th grade: nested fraction in the problem text, TWO solutions --------
eliozo:LV.TST.2020.12.7 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.12.7" ;
    eliozo:problemGrade 12 ;
    eliozo:problemText """Aprēķini $\\frac{\\frac{1}{2}+\\frac{1}{3}}{\\frac{1}{4}}$!"""@lv ;
    eliozo:problemTextHtml """<p>Aprēķini $\\frac{\\frac{1}{2}+\\frac{1}{3}}{\\frac{1}{4}}$!</p>"""@lv ;
    eliozo:problemSolution eliozo:SOLN.LV.TST.2020.12.7.SUB1,
        eliozo:SOLN.LV.TST.2020.12.7.SUB2 .

eliozo:SOLN.LV.TST.2020.12.7.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText """Saskaitām daļas: $\\frac{\\frac{5}{6}}{\\frac{1}{4}}
= \\frac{10}{3}$."""@lv ;
    eliozo:solutionTextHtml """<p>$\\frac{10}{3}$.</p>"""@lv .

eliozo:SOLN.LV.TST.2020.12.7.SUB2 a eliozo:Solution ;
    eliozo:solutionNum 2 ;
    eliozo:solutionText """Otrs veids: reizinām skaitītāju un saucēju ar $12$,
iegūstot $\\frac{\\frac{12}{2}+\\frac{12}{3}}{3}$."""@lv ;
    eliozo:solutionTextHtml """<p>$\\frac{10}{3}$.</p>"""@lv .

# --- No eliozo:problemGrade at all: the query's OPTIONAL must not drop it --
eliozo:LV.TST.2020.X.8 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.X.8" ;
    eliozo:problemText """Skaitli sauksim par "labu", ja tas dalās ar $7$.
Cik ir divciparu labo skaitļu?"""@lv ;
    eliozo:problemTextHtml """<p>Skaitli sauksim par "labu", ja tas dalās ar $7$.</p>"""@lv .
'''

# Twelve extra problems sharing one token, so that LIMIT 10 can be observed.
FILLER_COUNT = 12
SEARCH_FIXTURE_TTL += "".join(
    """
eliozo:LV.TST.2021.{grade}.{n} a eliozo:Problem ;
    eliozo:problemID "LV.TST.2021.{grade}.{n}" ;
    eliozo:problemGrade {grade} ;
    eliozo:problemText "Aizpildijuma uzdevums numur {n}."@lv ;
    eliozo:problemTextHtml "<p>Aizpildijuma uzdevums numur {n}.</p>"@lv .
""".format(n=i, grade=i)
    for i in range(1, FILLER_COUNT + 1)
)


@pytest.fixture
def search_store(monkeypatch):
    """In-memory oxigraph store preloaded with ``SEARCH_FIXTURE_TTL``."""
    from pyoxigraph import RdfFormat, Store

    import eliozo_dao

    store = Store()
    store.load(input=SEARCH_FIXTURE_TTL, format=RdfFormat.TURTLE)
    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    yield store


def ids(rawJson):
    """Problem IDs of a SPARQL JSON result, in the order the query returned."""
    return [row["problemid"]["value"]
            for row in json.loads(rawJson)["results"]["bindings"]]


# --------------------------------------------------------------------------
# Escaping helpers
# --------------------------------------------------------------------------

def test_replace_non_ascii_maps_latvian_diacritics():
    assert replace_non_ascii_with_unicode_escape("trijstūra") == "trijst\\u016Bra"


def test_escape_sparql_literal_doubles_backslashes():
    """A LaTeX macro must survive the SPARQL string parser: "\\s" is not a
    legal SPARQL escape, so the backslash has to be doubled."""
    assert escape_sparql_literal("\\sqrt") == "\\\\sqrt"


def test_escape_sparql_literal_escapes_quotes_and_newlines():
    assert escape_sparql_literal('par "labu"') == 'par \\"labu\\"'
    assert escape_sparql_literal("a\nb") == "a\\nb"


def test_escape_sparql_literal_keeps_diacritic_escapes_intact():
    """Diacritics are escaped last: their own backslash must not be doubled,
    otherwise \\u016B would reach SPARQL as a literal backslash-u sequence."""
    assert escape_sparql_literal("trijstūra") == "trijst\\u016Bra"


# --------------------------------------------------------------------------
# Keyword (exact) search
# --------------------------------------------------------------------------

def test_keyword_finds_latvian_phrase(search_store):
    assert ids(getProblemsByKeywordSPARQL("taisnleņķa trijstūra", False)) == [
        "LV.TST.2020.5.1"]


def test_keyword_is_case_insensitive_by_default(search_store):
    assert ids(getProblemsByKeywordSPARQL("LEŅĶIEM", False)) == ["LV.TST.2020.8.3"]


def test_keyword_case_sensitive_flag_is_honoured(search_store):
    assert ids(getProblemsByKeywordSPARQL("Leņķiem", True)) == ["LV.TST.2020.8.3"]
    assert ids(getProblemsByKeywordSPARQL("leņķiem", True)) == []


def test_keyword_matches_latex_macro_verbatim(search_store):
    """Exact search takes the pattern literally, so a LaTeX macro is typed as
    it appears in the markdown -- with a single backslash."""
    assert ids(getProblemsByKeywordSPARQL("\\sqrt[3]{27}", False)) == [
        "LV.TST.2020.9.4"]


def test_keyword_is_not_a_regex(search_store):
    """"$(a+b)^2" contains regex metacharacters; exact search must match them
    as plain text and not blow up."""
    assert ids(getProblemsByKeywordSPARQL("$(a+b)^2 \\geq 4ab$", False)) == [
        "LV.TST.2020.7.2"]


def test_keyword_with_double_quotes(search_store):
    assert ids(getProblemsByKeywordSPARQL('par "labu"', False)) == [
        "LV.TST.2020.X.8"]


def test_keyword_without_grade_is_still_returned(search_store):
    """The problem matched here has no eliozo:problemGrade -- the OPTIONAL in
    the query must keep it in the result set."""
    assert "LV.TST.2020.X.8" in ids(getProblemsByKeywordSPARQL("divciparu", False))


def test_keyword_no_match_returns_empty(search_store):
    assert ids(getProblemsByKeywordSPARQL("kvadratvienadojums", False)) == []


def test_keyword_results_are_ordered_by_grade(search_store):
    found = ids(getProblemsByKeywordSPARQL("Aprēķini", False))
    assert found == ["LV.TST.2020.5.1", "LV.TST.2020.9.4",
                     "LV.TST.2020.10.5", "LV.TST.2020.12.7"]


def test_keyword_result_is_capped_at_ten(search_store):
    found = ids(getProblemsByKeywordSPARQL("Aizpildijuma uzdevums", False))
    assert len(found) == 10, f"{FILLER_COUNT} problems match, query LIMIT is 10"
    assert found[0] == "LV.TST.2021.1.1", "ordered by grade, so grade 1 first"


# --------------------------------------------------------------------------
# Regex search -- patterns with a mathematical meaning
# --------------------------------------------------------------------------

def test_regex_square_of_a_binomial(search_store):
    """(something)^2 -- the LaTeX for a squared binomial."""
    assert ids(getProblemsByRegexSPARQL(r"\([^()]+\)\^\{?2", False)) == [
        "LV.TST.2020.7.2"]


def test_regex_cubic_root(search_store):
    assert ids(getProblemsByRegexSPARQL(r"\\sqrt\[3\]\{", False)) == [
        "LV.TST.2020.9.4"]


def test_regex_sine_of_a_greek_angle(search_store):
    """Sine of alpha, beta or gamma; in the problem texts only beta/gamma
    occur (the alpha one hides in a solution -- see the search-target tests)."""
    pattern = r"\\sin *\\(alpha|beta|gamma)"
    assert ids(getProblemsByRegexSPARQL(pattern, False)) == ["LV.TST.2020.8.3"]


def test_regex_fraction_inside_a_fraction(search_store):
    """\\frac{ ... \\frac -- a fraction whose numerator opens another one."""
    pattern = r"\\frac\{[^{}]*\\frac"
    assert ids(getProblemsByRegexSPARQL(pattern, False)) == ["LV.TST.2020.12.7"]


def test_regex_needs_a_doubled_backslash_for_a_latex_macro(search_store):
    """In regex mode the pattern is a regex, so "\\frac" (single backslash)
    means form-feed + "rac" and must not match anything."""
    assert ids(getProblemsByRegexSPARQL("\\frac", False)) == []
    assert ids(getProblemsByRegexSPARQL(r"\\frac", False)) == [
        "LV.TST.2020.11.6", "LV.TST.2020.12.7"]


def test_regex_is_case_insensitive_by_default(search_store):
    assert ids(getProblemsByRegexSPARQL("LEŅĶIEM", False)) == ["LV.TST.2020.8.3"]


def test_regex_case_sensitive_flag_is_honoured(search_store):
    assert ids(getProblemsByRegexSPARQL("Leņķiem", True)) == ["LV.TST.2020.8.3"]
    assert ids(getProblemsByRegexSPARQL("leņķiem", True)) == []


def test_regex_character_classes_survive_case_insensitivity(search_store):
    r"""Case insensitivity must not be implemented by lowercasing the pattern:
    that would turn \S (non-space) into \s (space) and invert the match."""
    assert ids(getProblemsByRegexSPARQL(r"\\sqrt\[3\]\{\S+\}", False)) == [
        "LV.TST.2020.9.4"]


def test_regex_anchors_and_alternation(search_store):
    assert ids(getProblemsByRegexSPARQL(r"^(Pierādi|Atrisini)", False)) == [
        "LV.TST.2020.7.2", "LV.TST.2020.8.3", "LV.TST.2020.11.6"]


def test_regex_result_is_capped_at_ten(search_store):
    assert len(ids(getProblemsByRegexSPARQL(r"Aizpildijuma", False))) == 10


# --------------------------------------------------------------------------
# Search target: problems only (3A) vs problems + their solutions (3B)
# --------------------------------------------------------------------------

def test_keyword_target_solutions_finds_solution_only_text(search_store):
    """"sin \\alpha" occurs only inside a solution of LV.TST.2020.10.5."""
    keyword = "\\sin \\alpha"
    assert ids(getProblemsByKeywordSPARQL(
        keyword, False, SEARCH_TARGET_PROBLEMS)) == []
    assert ids(getProblemsByKeywordSPARQL(
        keyword, False, SEARCH_TARGET_SOLUTIONS)) == ["LV.TST.2020.10.5"]


def test_regex_target_solutions_finds_nested_fraction_in_solutions(search_store):
    """A fraction inside a fraction: one problem has it in its own text, a
    second one only in its solution."""
    pattern = r"\\frac\{[^{}]*\\frac"
    assert ids(getProblemsByRegexSPARQL(
        pattern, False, SEARCH_TARGET_PROBLEMS)) == ["LV.TST.2020.12.7"]
    assert ids(getProblemsByRegexSPARQL(
        pattern, False, SEARCH_TARGET_SOLUTIONS)) == ["LV.TST.2020.11.6",
                                                      "LV.TST.2020.12.7"]


def test_regex_target_solutions_widens_the_greek_angle_search(search_store):
    pattern = r"\\sin *\\(alpha|beta|gamma)"
    assert ids(getProblemsByRegexSPARQL(
        pattern, False, SEARCH_TARGET_SOLUTIONS)) == ["LV.TST.2020.8.3",
                                                      "LV.TST.2020.10.5"]


def test_target_solutions_still_matches_the_problem_text(search_store):
    """"In solutions" means "problem text OR any solution text", not
    "solutions only" -- a hit in the problem statement still counts."""
    assert ids(getProblemsByKeywordSPARQL(
        "taisnleņķa trijstūra", False, SEARCH_TARGET_SOLUTIONS)) == [
        "LV.TST.2020.5.1"]


def test_target_solutions_returns_each_problem_once(search_store):
    """LV.TST.2020.12.7 has two solutions, both matching -- the problem must
    still appear as a single row."""
    found = ids(getProblemsByKeywordSPARQL(
        "\\frac", False, SEARCH_TARGET_SOLUTIONS))
    assert found.count("LV.TST.2020.12.7") == 1


def test_target_solutions_does_not_lose_problems_without_solutions(search_store):
    """LV.TST.2020.9.4 has no solutions at all; the EXISTS branch must not
    turn the query into an inner join on eliozo:problemSolution."""
    assert ids(getProblemsByRegexSPARQL(
        r"\\sqrt\[3\]\{", False, SEARCH_TARGET_SOLUTIONS)) == ["LV.TST.2020.9.4"]


def test_default_target_is_problems_only(search_store):
    keyword = "\\sin \\alpha"
    assert ids(getProblemsByKeywordSPARQL(keyword, False)) == ids(
        getProblemsByKeywordSPARQL(keyword, False, SEARCH_TARGET_PROBLEMS))
