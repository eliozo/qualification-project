r"""Tests for keyword (exact) and regex search in ``eliozo_dao.search_repository``.

The tests run against a small curated TTL fixture loaded into an in-memory
pyoxigraph store rather than against the full olympiad RDF dump. Rationale:
the dump is rebuilt from ``migration-script/resources`` whenever new olympiads
are added, so any assertion on it ("this regex finds 6 problems") would rot on
the next content import. The fixture below is written in the same shape as the
real data -- Latvian problem statements with LaTeX formulas, ``@lv`` language
tags, problems with zero, one or two solutions, problems in several languages,
books without grade or country -- so it still exercises the query text for real.

The LaTeX in the fixture is copied in style from actual problems: nested
``\frac``, ``\sqrt[3]{...}``, ``\sin \alpha``, squared binomials. Several of
those patterns deliberately occur *only inside solutions*, which is what
separates the two values of the "search-target" select box in
``main_content.html``.

Note on regex escaping: the pattern reaching these functions is the regex
verbatim, so a literal LaTeX backslash is written ``\\`` (two characters) in
the pattern -- hence the ``r"\\frac"`` spellings below.
"""

import pytest

import eliozo_dao.problem_listing as problem_listing
from eliozo_dao.problem_listing import UNTAGGED, chooseTranslation
from eliozo_dao.search_repository import (
    SEARCH_MODE_EXACT,
    SEARCH_MODE_REGEX,
    SEARCH_TARGET_PROBLEMS,
    SEARCH_TARGET_SOLUTIONS,
    escape_sparql_literal,
    replace_non_ascii_with_unicode_escape,
    searchProblems,
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

# --- Ranking: every problem below contains the word "Kārtošanas" -----------
# Listed out of order on purpose; the expected order is in RANKED_IDS.
eliozo:BBK2012.P1.3 a eliozo:Problem ;
    eliozo:problemID "BBK2012.P1.3" ;
    eliozo:problemText "Kārtošanas pārbaude: grāmata bez klases."@lv ;
    eliozo:problemTextHtml "<p>BBK2012.P1.3</p>"@lv .

eliozo:LT.LMMO.2019.9.1 a eliozo:Problem ;
    eliozo:problemID "LT.LMMO.2019.9.1" ;
    eliozo:problemGrade 9 ; eliozo:problemYear 2019 ; eliozo:country "LT" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>LT.LMMO.2019.9.1</p>"@lv .

eliozo:LV.NOL.2021.9.1 a eliozo:Problem ;
    eliozo:problemID "LV.NOL.2021.9.1" ;
    eliozo:problemGrade 9 ; eliozo:problemYear 2021 ; eliozo:country "LV" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>LV.NOL.2021.9.1</p>"@lv .

eliozo:LV.AMO.2021.9.10 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2021.9.10" ;
    eliozo:problemGrade 9 ; eliozo:problemYear 2021 ; eliozo:country "LV" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>LV.AMO.2021.9.10</p>"@lv .

eliozo:WW.IMOSHL.2022.A1 a eliozo:Problem ;
    eliozo:problemID "WW.IMOSHL.2022.A1" ;
    eliozo:problemText "Kārtošanas pārbaude: saraksts bez klases."@lv ;
    eliozo:problemTextHtml "<p>WW.IMOSHL.2022.A1</p>"@lv .

eliozo:LV.AMO.2021.9.2 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2021.9.2" ;
    eliozo:problemGrade 9 ; eliozo:problemYear 2021 ; eliozo:country "LV" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>LV.AMO.2021.9.2</p>"@lv .

eliozo:LV.AMO.2020.9.7 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2020.9.7" ;
    eliozo:problemGrade 9 ; eliozo:country "LV" ;
    eliozo:problemText "Kārtošanas pārbaude: gads nav zināms."@lv ;
    eliozo:problemTextHtml "<p>LV.AMO.2020.9.7</p>"@lv .

eliozo:EE.PK.2021.9.1 a eliozo:Problem ;
    eliozo:problemID "EE.PK.2021.9.1" ;
    eliozo:problemGrade 9 ; eliozo:problemYear 2021 ; eliozo:country "EE" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>EE.PK.2021.9.1</p>"@lv .

eliozo:LV.AMO.2019.8.1 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2019.8.1" ;
    eliozo:problemGrade 8 ; eliozo:problemYear 2019 ; eliozo:country "LV" ;
    eliozo:problemText "Kārtošanas pārbaude."@lv ;
    eliozo:problemTextHtml "<p>LV.AMO.2019.8.1</p>"@lv .

# --- Translations: every problem below contains \binom{7}{3} ---------------
# 6.1: lv, en, lt           6.2: lt, ru            6.3: ru, ee
# 6.4: ee, en, lv           6.5: two lv texts
# The HTML says which translation was picked.
eliozo:LV.MLT.2020.6.1 a eliozo:Problem ;
    eliozo:problemID "LV.MLT.2020.6.1" ;
    eliozo:problemGrade 6 ; eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:problemText "Izvēļu skaits ir $\\binom{7}{3}$."@lv ,
                       "The number of choices is $\\binom{7}{3}$."@en ,
                       "Pasirinkimų skaičius yra $\\binom{7}{3}$."@lt ;
    eliozo:problemTextHtml "<p>6.1 lv</p>"@lv , "<p>6.1 en</p>"@en , "<p>6.1 lt</p>"@lt ;
    eliozo:problemSolution eliozo:SOLN.LV.MLT.2020.6.1.SUB1 .

eliozo:SOLN.LV.MLT.2020.6.1.SUB1 a eliozo:Solution ;
    eliozo:solutionNum 1 ;
    eliozo:solutionText "Atbilde: $\\binom{7}{3} = 35$."@lv ;
    eliozo:solutionTextHtml "<p>35</p>"@lv .

eliozo:LV.MLT.2020.6.2 a eliozo:Problem ;
    eliozo:problemID "LV.MLT.2020.6.2" ;
    eliozo:problemGrade 6 ; eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:problemText "Pasirinkimų skaičius yra $\\binom{7}{3}$."@lt ,
                       "Число выборов равно $\\binom{7}{3}$."@ru ;
    eliozo:problemTextHtml "<p>6.2 lt</p>"@lt , "<p>6.2 ru</p>"@ru .

eliozo:LV.MLT.2020.6.3 a eliozo:Problem ;
    eliozo:problemID "LV.MLT.2020.6.3" ;
    eliozo:problemGrade 6 ; eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:problemText "Число выборов равно $\\binom{7}{3}$."@ru ,
                       "Valikute arv on $\\binom{7}{3}$."@ee ;
    eliozo:problemTextHtml "<p>6.3 ru</p>"@ru , "<p>6.3 ee</p>"@ee .

eliozo:LV.MLT.2020.6.4 a eliozo:Problem ;
    eliozo:problemID "LV.MLT.2020.6.4" ;
    eliozo:problemGrade 6 ; eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:problemText "Valikute arv on $\\binom{7}{3}$."@ee ,
                       "The number of choices is $\\binom{7}{3}$."@en ,
                       "Izvēļu skaits ir $\\binom{7}{3}$."@lv ;
    eliozo:problemTextHtml "<p>6.4 ee</p>"@ee , "<p>6.4 en</p>"@en , "<p>6.4 lv</p>"@lv .

eliozo:LV.MLT.2020.6.5 a eliozo:Problem ;
    eliozo:problemID "LV.MLT.2020.6.5" ;
    eliozo:problemGrade 6 ; eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:problemText "Izvēļu skaits ir $\\binom{7}{3}$."@lv ,
                       "Izvēļu skaits ir $\\binom{7}{3}$ (otrs teksts)."@lv ;
    eliozo:problemTextHtml "<p>6.5 lv B</p>"@lv , "<p>6.5 lv A</p>"@lv .

# --- An untranslated problem: the lv text is an empty placeholder ----------
eliozo:WW.TST.2022.B1 a eliozo:Problem ;
    eliozo:problemID "WW.TST.2022.B1" ;
    eliozo:problemText ""@lv , "Blank translation check."@en ;
    eliozo:problemTextHtml ""@lv , "<p>B1 en</p>"@en .
'''

# Twelve extra problems sharing one token, so that paging can be observed.
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
FILLER_IDS = ["LV.TST.2021.%d.%d" % (i, i) for i in range(1, FILLER_COUNT + 1)]

# The "Kārtošanas" problems under the default SEARCH_RESULT_ORDER.
RANKED_IDS = [
    "LV.AMO.2019.8.1",     # grade 8 before grade 9
    "EE.PK.2021.9.1",      # grade 9, year 2021: country EE before LV ...
    "LV.AMO.2021.9.2",     # ... even though olympiad PK > AMO
    "LV.AMO.2021.9.10",    # 9.2 before 9.10: numbers compare as numbers
    "LV.NOL.2021.9.1",     # olympiad AMO before NOL
    "LT.LMMO.2019.9.1",    # year 2019 after 2021, although LT < LV
    "LV.AMO.2020.9.7",     # no year: after every grade-9 problem with a year
    "WW.IMOSHL.2022.A1",   # no grade: last; olympiad IMOSHL ...
    "BBK2012.P1.3",        # ... before P1
]

MULTILINGUAL_IDS = ["LV.MLT.2020.6.1", "LV.MLT.2020.6.2", "LV.MLT.2020.6.3",
                    "LV.MLT.2020.6.4", "LV.MLT.2020.6.5"]


@pytest.fixture
def search_store(monkeypatch):
    """In-memory oxigraph store preloaded with ``SEARCH_FIXTURE_TTL``."""
    from pyoxigraph import RdfFormat, Store

    import eliozo_dao

    store = Store()
    store.load(input=SEARCH_FIXTURE_TTL, format=RdfFormat.TURTLE)
    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    yield store


def search(pattern, mode=SEARCH_MODE_EXACT, target=SEARCH_TARGET_PROBLEMS,
           caseSensitive=False, uiLang="lv", offset=0, pageSize=100):
    return searchProblems(pattern, mode, target, uiLang=uiLang, offset=offset,
                          pageSize=pageSize, isCaseSensitive=caseSensitive)


def exact(pattern, **kwargs):
    """Problem IDs found by exact search, in ranked order."""
    return [p["problemid"] for p in search(pattern, SEARCH_MODE_EXACT, **kwargs)["problems"]]


def regex(pattern, **kwargs):
    """Problem IDs found by regex search, in ranked order."""
    return [p["problemid"] for p in search(pattern, SEARCH_MODE_REGEX, **kwargs)["problems"]]


def shown(pattern, uiLang):
    """{problemid: textHtml} as displayed for the ``\\binom`` problems."""
    return {p["problemid"]: p["textHtml"]
            for p in search(pattern, uiLang=uiLang)["problems"]}


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
    assert exact("taisnleņķa trijstūra") == ["LV.TST.2020.5.1"]


def test_keyword_is_case_insensitive_by_default(search_store):
    assert exact("LEŅĶIEM") == ["LV.TST.2020.8.3"]


def test_keyword_case_sensitive_flag_is_honoured(search_store):
    assert exact("Leņķiem", caseSensitive=True) == ["LV.TST.2020.8.3"]
    assert exact("leņķiem", caseSensitive=True) == []


def test_keyword_matches_latex_macro_verbatim(search_store):
    """Exact search takes the pattern literally, so a LaTeX macro is typed as
    it appears in the markdown -- with a single backslash."""
    assert exact("\\sqrt[3]{27}") == ["LV.TST.2020.9.4"]


def test_keyword_is_not_a_regex(search_store):
    """"$(a+b)^2" contains regex metacharacters; exact search must match them
    as plain text and not blow up."""
    assert exact("$(a+b)^2 \\geq 4ab$") == ["LV.TST.2020.7.2"]


def test_keyword_with_double_quotes(search_store):
    assert exact('par "labu"') == ["LV.TST.2020.X.8"]


def test_keyword_without_grade_is_still_returned(search_store):
    """The problem matched here has no eliozo:problemGrade -- the OPTIONAL in
    the query must keep it in the result set."""
    assert "LV.TST.2020.X.8" in exact("divciparu")


def test_keyword_no_match_returns_empty(search_store):
    result = search("kvadratvienadojums")
    assert result["problems"] == []
    assert result["total"] == 0


def test_keyword_results_are_ordered_by_grade(search_store):
    assert exact("Aprēķini") == ["LV.TST.2020.5.1", "LV.TST.2020.9.4",
                                 "LV.TST.2020.10.5", "LV.TST.2020.12.7"]


# --------------------------------------------------------------------------
# Regex search -- patterns with a mathematical meaning
# --------------------------------------------------------------------------

def test_regex_square_of_a_binomial(search_store):
    """(something)^2 -- the LaTeX for a squared binomial."""
    assert regex(r"\([^()]+\)\^\{?2") == ["LV.TST.2020.7.2"]


def test_regex_cubic_root(search_store):
    assert regex(r"\\sqrt\[3\]\{") == ["LV.TST.2020.9.4"]


def test_regex_sine_of_a_greek_angle(search_store):
    """Sine of alpha, beta or gamma; in the problem texts only beta/gamma
    occur (the alpha one hides in a solution -- see the search-target tests)."""
    assert regex(r"\\sin *\\(alpha|beta|gamma)") == ["LV.TST.2020.8.3"]


def test_regex_fraction_inside_a_fraction(search_store):
    """\\frac{ ... \\frac -- a fraction whose numerator opens another one."""
    assert regex(r"\\frac\{[^{}]*\\frac") == ["LV.TST.2020.12.7"]


def test_regex_needs_a_doubled_backslash_for_a_latex_macro(search_store):
    """In regex mode the pattern is a regex, so "\\frac" (single backslash)
    means form-feed + "rac" and must not match anything."""
    assert regex("\\frac") == []
    assert regex(r"\\frac") == ["LV.TST.2020.11.6", "LV.TST.2020.12.7"]


def test_regex_is_case_insensitive_by_default(search_store):
    assert regex("LEŅĶIEM") == ["LV.TST.2020.8.3"]


def test_regex_case_sensitive_flag_is_honoured(search_store):
    assert regex("Leņķiem", caseSensitive=True) == ["LV.TST.2020.8.3"]
    assert regex("leņķiem", caseSensitive=True) == []


def test_regex_character_classes_survive_case_insensitivity(search_store):
    r"""Case insensitivity must not be implemented by lowercasing the pattern:
    that would turn \S (non-space) into \s (space) and invert the match."""
    assert regex(r"\\sqrt\[3\]\{\S+\}") == ["LV.TST.2020.9.4"]


def test_regex_anchors_and_alternation(search_store):
    assert regex(r"^(Pierādi|Atrisini)") == [
        "LV.TST.2020.7.2", "LV.TST.2020.8.3", "LV.TST.2020.11.6"]


# --------------------------------------------------------------------------
# Search target: problems only (3A) vs problems + their solutions (3B)
# --------------------------------------------------------------------------

def test_keyword_target_solutions_finds_solution_only_text(search_store):
    """"sin \\alpha" occurs only inside a solution of LV.TST.2020.10.5."""
    keyword = "\\sin \\alpha"
    assert exact(keyword, target=SEARCH_TARGET_PROBLEMS) == []
    assert exact(keyword, target=SEARCH_TARGET_SOLUTIONS) == ["LV.TST.2020.10.5"]


def test_regex_target_solutions_finds_nested_fraction_in_solutions(search_store):
    """A fraction inside a fraction: one problem has it in its own text, a
    second one only in its solution."""
    pattern = r"\\frac\{[^{}]*\\frac"
    assert regex(pattern, target=SEARCH_TARGET_PROBLEMS) == ["LV.TST.2020.12.7"]
    assert regex(pattern, target=SEARCH_TARGET_SOLUTIONS) == [
        "LV.TST.2020.11.6", "LV.TST.2020.12.7"]


def test_regex_target_solutions_widens_the_greek_angle_search(search_store):
    assert regex(r"\\sin *\\(alpha|beta|gamma)", target=SEARCH_TARGET_SOLUTIONS) == [
        "LV.TST.2020.8.3", "LV.TST.2020.10.5"]


def test_target_solutions_still_matches_the_problem_text(search_store):
    """"In solutions" means "problem text OR any solution text", not
    "solutions only" -- a hit in the problem statement still counts."""
    assert exact("taisnleņķa trijstūra", target=SEARCH_TARGET_SOLUTIONS) == [
        "LV.TST.2020.5.1"]


def test_target_solutions_does_not_lose_problems_without_solutions(search_store):
    """LV.TST.2020.9.4 has no solutions at all; the solution branch of the
    UNION must not turn the query into a join on eliozo:problemSolution."""
    assert regex(r"\\sqrt\[3\]\{", target=SEARCH_TARGET_SOLUTIONS) == ["LV.TST.2020.9.4"]


def test_default_target_is_problems_only(search_store):
    keyword = "\\sin \\alpha"
    assert searchProblems(keyword, SEARCH_MODE_EXACT) == searchProblems(
        keyword, SEARCH_MODE_EXACT, SEARCH_TARGET_PROBLEMS)


# --------------------------------------------------------------------------
# Deduplication: every problem at most once
# --------------------------------------------------------------------------

def test_problem_with_two_matching_solutions_is_listed_once(search_store):
    """LV.TST.2020.12.7 matches in its text and in both of its solutions."""
    assert exact("\\frac", target=SEARCH_TARGET_SOLUTIONS).count("LV.TST.2020.12.7") == 1


@pytest.mark.parametrize("target", [SEARCH_TARGET_PROBLEMS, SEARCH_TARGET_SOLUTIONS])
@pytest.mark.parametrize("mode", [SEARCH_MODE_EXACT, SEARCH_MODE_REGEX])
def test_problem_matching_in_several_translations_is_listed_once(search_store, mode, target):
    """Every \\binom problem matches in two or three translations (6.1 also in
    its solution, 6.5 in two texts of the same language)."""
    pattern = "\\binom{7}{3}" if mode == SEARCH_MODE_EXACT else r"\\binom\{7\}\{3\}"
    result = search(pattern, mode=mode, target=target)
    assert [p["problemid"] for p in result["problems"]] == MULTILINGUAL_IDS
    assert result["total"] == len(MULTILINGUAL_IDS)


def test_total_counts_problems_not_translations(search_store):
    assert search("\\binom", pageSize=2)["total"] == len(MULTILINGUAL_IDS)


# --------------------------------------------------------------------------
# Which translation is shown
# --------------------------------------------------------------------------

def test_ui_language_translation_is_preferred(search_store):
    assert shown("\\binom", "lv")["LV.MLT.2020.6.1"] == "<p>6.1 lv</p>"
    assert shown("\\binom", "lt")["LV.MLT.2020.6.1"] == "<p>6.1 lt</p>"
    assert shown("\\binom", "en")["LV.MLT.2020.6.1"] == "<p>6.1 en</p>"


def test_english_is_the_fallback_before_alphabetical_order(search_store):
    """6.4 has ee, en and lv: with UI language lt, en wins although ee sorts first."""
    assert shown("\\binom", "lt")["LV.MLT.2020.6.4"] == "<p>6.4 en</p>"


def test_alphabetically_first_language_without_ui_language_or_english(search_store):
    texts = shown("\\binom", "lv")
    assert texts["LV.MLT.2020.6.2"] == "<p>6.2 lt</p>"   # lt < ru
    assert texts["LV.MLT.2020.6.3"] == "<p>6.3 ee</p>"   # ee < ru


def test_ui_language_outside_the_allowed_three_is_ignored(search_store):
    """6.2 has ru, but ru is not a UI language, so rule 1 does not apply."""
    assert shown("\\binom", "ru")["LV.MLT.2020.6.2"] == "<p>6.2 lt</p>"
    assert shown("\\binom", None)["LV.MLT.2020.6.1"] == "<p>6.1 en</p>"


def test_chosen_language_is_reported(search_store):
    langs = {p["problemid"]: p["lang"] for p in search("\\binom", uiLang="lt")["problems"]}
    assert langs == {"LV.MLT.2020.6.1": "lt", "LV.MLT.2020.6.2": "lt",
                     "LV.MLT.2020.6.3": "ee", "LV.MLT.2020.6.4": "en",
                     "LV.MLT.2020.6.5": "lv"}


def test_two_texts_in_one_language_give_a_stable_choice(search_store):
    assert shown("\\binom", "lv")["LV.MLT.2020.6.5"] == "<p>6.5 lv A</p>"


def test_empty_translation_counts_as_missing(search_store):
    """WW.TST.2022.B1 has an empty lv placeholder, like the IMO shortlist in the
    real data: with UI language lv the English text must be shown, not nothing."""
    page = search("Blank translation check", uiLang="lv")["problems"]
    assert [(p["problemid"], p["lang"], p["textHtml"]) for p in page] == [
        ("WW.TST.2022.B1", "en", "<p>B1 en</p>")]


def test_choose_translation_rules():
    assert chooseTranslation({}, "lv") is None
    assert chooseTranslation({"lv": "a", "en": "b"}, "lv") == "lv"
    assert chooseTranslation({"lv": "a", "en": "b"}, "lt") == "en"
    assert chooseTranslation({"ua": "a", "pl": "b", "lt": "c"}, "en") == "lt"
    assert chooseTranslation({UNTAGGED: "untagged", "ru": "b"}, "lv") == "ru"
    assert chooseTranslation({UNTAGGED: "untagged"}, "lv") == UNTAGGED


def test_requested_translation_wins_when_it_exists():
    """The problem pages pass the "lang" URL parameter as ``requested``."""
    assert chooseTranslation({"lv": "a", "en": "b"}, "lv", requested="en") == "en"
    assert chooseTranslation({"lv": "a"}, "lv", requested="en") == "lv"


# --------------------------------------------------------------------------
# Notes telling where the match is
# --------------------------------------------------------------------------

def notes(pattern, uiLang="lv", **kwargs):
    """{problemid: (shown language, matchLang, solutionMatchLang)}"""
    return {p["problemid"]: (p["lang"], p["matchLang"], p["solutionMatchLang"])
            for p in search(pattern, uiLang=uiLang, **kwargs)["problems"]}


def test_no_note_when_the_shown_text_contains_the_match(search_store):
    """LV.MLT.2020.6.1 also matches in a solution, but the match is already visible."""
    found = notes("\\binom{7}{3}", target=SEARCH_TARGET_SOLUTIONS)
    assert sorted(found) == MULTILINGUAL_IDS
    assert {(m, s) for _, m, s in found.values()} == {(None, None)}


def test_note_names_the_translation_that_contains_the_match(search_store):
    assert notes("number of choices") == {
        "LV.MLT.2020.6.1": ("lv", "en", None),
        "LV.MLT.2020.6.4": ("lv", "en", None),
    }
    assert notes("number of choices", uiLang="en") == {
        "LV.MLT.2020.6.1": ("en", None, None),
        "LV.MLT.2020.6.4": ("en", None, None),
    }


def test_note_picks_the_translation_by_precedence(search_store):
    """6.1 is shown in lv and matches in en and lt: en wins by the fallback rule."""
    pattern = r"choices|Pasirinkimų"
    assert notes(pattern, mode=SEARCH_MODE_REGEX)["LV.MLT.2020.6.1"] == ("lv", "en", None)
    assert notes(pattern, mode=SEARCH_MODE_REGEX, uiLang="lt")["LV.MLT.2020.6.1"] == (
        "lt", None, None)


def test_note_points_to_a_matching_solution(search_store):
    assert notes("= 35", target=SEARCH_TARGET_SOLUTIONS) == {
        "LV.MLT.2020.6.1": ("lv", None, "lv")}
    assert notes("\\sin \\alpha", target=SEARCH_TARGET_SOLUTIONS) == {
        "LV.TST.2020.10.5": ("lv", None, "lv")}


def test_solution_note_only_when_solutions_are_searched(search_store):
    """6.1 matches "choices" in its en statement and "= 35" in its lv solution."""
    pattern = r"choices|= 35"
    assert notes(pattern, mode=SEARCH_MODE_REGEX)["LV.MLT.2020.6.1"] == ("lv", "en", None)
    assert notes(pattern, mode=SEARCH_MODE_REGEX, target=SEARCH_TARGET_SOLUTIONS)[
        "LV.MLT.2020.6.1"] == ("lv", "en", "lv")


# --------------------------------------------------------------------------
# Ranking
# --------------------------------------------------------------------------

def test_default_ranking(search_store):
    """grade asc, year desc, country asc, olympiad asc, problem ID; missing values last."""
    assert exact("Kārtošanas") == RANKED_IDS


def test_ranking_is_configured_in_one_place(search_store, monkeypatch):
    monkeypatch.setattr(problem_listing, "SEARCH_RESULT_ORDER",
                        [("year", "asc"), ("problemid", "asc")])
    assert exact("Kārtošanas") == [
        "LT.LMMO.2019.9.1", "LV.AMO.2019.8.1",                      # 2019
        "EE.PK.2021.9.1", "LV.AMO.2021.9.2", "LV.AMO.2021.9.10",
        "LV.NOL.2021.9.1",                                           # 2021
        "BBK2012.P1.3", "LV.AMO.2020.9.7", "WW.IMOSHL.2022.A1",      # no year
    ]


def test_missing_values_stay_last_in_descending_order(search_store, monkeypatch):
    monkeypatch.setattr(problem_listing, "SEARCH_RESULT_ORDER",
                        [("grade", "desc"), ("problemid", "asc")])
    found = exact("Kārtošanas")
    assert found[-2:] == ["BBK2012.P1.3", "WW.IMOSHL.2022.A1"]
    assert found[0] in ("EE.PK.2021.9.1", "LT.LMMO.2019.9.1")   # a grade-9 problem


def test_bad_ranking_configuration_is_rejected(search_store, monkeypatch):
    monkeypatch.setattr(problem_listing, "SEARCH_RESULT_ORDER", [("difficulty", "asc")])
    with pytest.raises(ValueError):
        exact("Kārtošanas")


# --------------------------------------------------------------------------
# Paging
# --------------------------------------------------------------------------

def test_first_page_holds_page_size_problems(search_store):
    result = search("Aizpildijuma uzdevums", pageSize=10)
    assert result["total"] == FILLER_COUNT
    assert [p["problemid"] for p in result["problems"]] == FILLER_IDS[:10]


def test_pages_cover_every_problem_exactly_once(search_store):
    pages = [search("Aizpildijuma uzdevums", offset=offset, pageSize=5)
             for offset in (0, 5, 10)]
    ids = [p["problemid"] for page in pages for p in page["problems"]]
    assert ids == FILLER_IDS
    assert [len(page["problems"]) for page in pages] == [5, 5, 2]


def test_regex_search_is_paged_too(search_store):
    result = search("Aizpildijuma", mode=SEARCH_MODE_REGEX, offset=10, pageSize=10)
    assert [p["problemid"] for p in result["problems"]] == FILLER_IDS[10:]
    assert result["total"] == FILLER_COUNT


def test_default_page_size(search_store):
    result = searchProblems("Aizpildijuma uzdevums", SEARCH_MODE_EXACT)
    assert result["pageSize"] == problem_listing.PAGE_SIZE == 10
    assert len(result["problems"]) == 10


def test_offset_past_the_end_gives_an_empty_page(search_store):
    result = search("Aizpildijuma uzdevums", offset=50)
    assert result["problems"] == []
    assert result["total"] == FILLER_COUNT


def test_negative_offset_is_treated_as_zero(search_store):
    result = search("Aizpildijuma uzdevums", offset=-10, pageSize=3)
    assert result["offset"] == 0
    assert [p["problemid"] for p in result["problems"]] == FILLER_IDS[:3]
