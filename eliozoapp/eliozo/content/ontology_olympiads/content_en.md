# Olympiads

Every olympiad problem belongs to an **olympiad** (a competition with a country and
a code) and to one of its **events** (a year or a round). See also the
[ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Olympiad` |
| Problem property | `eliozo:olympiad`, value is the ID as **text**, e.g. `"LV.AMO"` |
| Size | 17 olympiads |
| Browse | [Archive > Olympiads](/olympiads) |

## Properties

An olympiad node has `eliozo:OlympiadID` (note the capital O, e.g. `"LV.AMO"`),
`eliozo:olympiadCode` (`"AMO"`), `eliozo:olympiadCountry` (`"LV"`) and, in English,
Latvian and Lithuanian, `eliozo:olympiadName` and `eliozo:olympiadDescription`.

A problem repeats the parts it needs, so most queries do not have to look at the
olympiad node at all:

| Property | Example |
|---|---|
| `eliozo:olympiad` | `"LV.AMO"` |
| `eliozo:olympiadCode` | `"AMO"` |
| `eliozo:country` | `"LV"` |
| `eliozo:event` | `"LV.AMO.2019"` |
| `eliozo:problemYear` | `2019` |
| `eliozo:problemGrade` | `7` |
| `eliozo:olympiadType` | `"RegionalOrOpen"` |

The problem ID itself is built from these parts: `LV.AMO.2019.7.4` is problem 4 for
grade 7 of the Latvian Open Olympiad in 2019.

## The olympiads

| ID | Olympiad |
|---|---|
| `LV.AMO` | Latvian Open Mathematical Olympiad |
| `LV.NOL` | Latvian Municipal Olympiad |
| `LV.SOL` | Latvian Preliminary Olympiad |
| `LV.VOL` | Latvian State Olympiad |
| `LV.TST` | Latvian Team Selection Test |
| `LT.LMMO` | Lithuanian School Mathematical Olympiad |
| `LT.SAV` | Lithuanian School Mathematical Olympiad, Municipal Round |
| `LT.LJMO` | Lithuanian Junior Mathematical Olympiad |
| `LT.LKMMO` | Lithuanian School Team Mathematical Olympiad |
| `LT.LDK` | Mathematical Competition in Honor of the Grand Duchy of Lithuania |
| `LT.VUMIF` | Mathematical Olympiad of Vilnius University MIF |
| `LT.TST` | Lithuanian Team Selection Test |
| `EE.LHT` | Estonian Open Mathematical Competition |
| `EE.PK` | Estonian Mathematical Olympiad, Regional Round |
| `EE.LO` | Estonian Mathematical Olympiad, Final Round |
| `EE.TST` | Estonian Team Selection Test |
| `WW.IMOSHL` | International Mathematical Olympiad (IMO), Shortlist |

## Examples

Grade 5 problems of the Latvian Open Olympiad since 2020, grouped by year:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (STR(?year) AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:olympiad "LV.AMO" ;
         eliozo:problemYear ?year ;
         eliozo:problemGrade 5 .
      FILTER (?year >= 2020)
    }
    ORDER BY DESC(?year) ?problemID

Geometry problems of all national olympiads, with the English name of the
olympiad as subtitle:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:olympiad ?olympiad ;
         eliozo:olympiadType "National" ;
         eliozo:domain "Geom" .
      ?o eliozo:OlympiadID ?olympiad ;
         eliozo:olympiadName ?name .
      FILTER (LANG(?name) = "en")
    }
    ORDER BY ?name ?problemID
