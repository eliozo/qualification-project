# Olimpiados

Kiekvienas olimpiados uždavinys priklauso **olimpiadai** (varžyboms su šalimi ir
kodu) ir vienam jos **turui** (metams arba etapui). Žr. taip pat
[ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Olympiad` |
| Uždavinio savybė | `eliozo:olympiad`, reikšmė yra ID kaip **tekstas**, pvz., `"LV.AMO"` |
| Apimtis | 17 olimpiadų |
| Naršyti | [Archyvas > Olimpiados](/olympiads) |

## Savybės

Olimpiados viršūnė turi `eliozo:OlympiadID` (atkreipkite dėmesį į didžiąją O, pvz.,
`"LV.AMO"`), `eliozo:olympiadCode` (`"AMO"`), `eliozo:olympiadCountry` (`"LV"`) ir
anglų, latvių bei lietuvių kalbomis `eliozo:olympiadName` ir
`eliozo:olympiadDescription`.

Uždavinys pats pakartoja reikalingas dalis, todėl daugumai užklausų olimpiados
viršūnės visai nereikia:

| Savybė | Pavyzdys |
|---|---|
| `eliozo:olympiad` | `"LV.AMO"` |
| `eliozo:olympiadCode` | `"AMO"` |
| `eliozo:country` | `"LV"` |
| `eliozo:event` | `"LV.AMO.2019"` |
| `eliozo:problemYear` | `2019` |
| `eliozo:problemGrade` | `7` |
| `eliozo:olympiadType` | `"RegionalOrOpen"` |

Iš šių dalių sudarytas ir pats uždavinio ID: `LV.AMO.2019.7.4` yra 2019 metų Latvijos
atvirosios matematikos olimpiados 7 klasės 4 uždavinys.

## Olimpiados

| ID | Olimpiada |
|---|---|
| `LV.AMO` | Latvijos atviroji matematikos olimpiada |
| `LV.NOL` | Latvijos savivaldybių olimpiada |
| `LV.SOL` | Latvijos pasiruošimo olimpiada |
| `LV.VOL` | Latvijos valstybinė olimpiada |
| `LV.TST` | Latvijos atrankos varžybos |
| `LT.LMMO` | Lietuvos mokinių matematikos olimpiada |
| `LT.SAV` | Lietuvos mokinių matematikos olimpiados savivaldybių etapas |
| `LT.LJMO` | Lietuvos jaunesniųjų klasių matematikos olimpiada |
| `LT.LKMMO` | Lietuvos komandinė mokinių matematikos olimpiada |
| `LT.LDK` | Matematinės varžybos Lietuvos Didžiosios Kunigaikštystės garbei |
| `LT.VUMIF` | Vilniaus Universiteto MIF matematikos olimpiada |
| `LT.TST` | Lietuvos atrankos į IMO ir MEMO olimpiadas |
| `EE.LHT` | Estijos atviros matematikos varžybos |
| `EE.PK` | Estijos matematikos olimpiados rajoniniai turai |
| `EE.LO` | Estijos matematikos olimpiados finalinis turas |
| `EE.TST` | Estijos atrankos varžybos |
| `WW.IMOSHL` | Tarptautinė matematikos olimpiada (IMO), trumpasis sąrašas |

## Pavyzdžiai

Latvijos atvirosios olimpiados 5 klasės uždaviniai nuo 2020 metų, sugrupuoti pagal
metus:

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

Visų nacionalinių olimpiadų geometrijos uždaviniai su lietuvišku olimpiados
pavadinimu kaip paantrašte:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:olympiad ?olympiad ;
         eliozo:olympiadType "National" ;
         eliozo:domain "Geom" .
      ?o eliozo:OlympiadID ?olympiad ;
         eliozo:olympiadName ?name .
      FILTER (LANG(?name) = "lt")
    }
    ORDER BY ?name ?problemID
