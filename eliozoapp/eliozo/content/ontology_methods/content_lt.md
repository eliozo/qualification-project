# Metodai

**Metodas** yra sprendimo samprotavimo šablonas: matematinė indukcija, Dirichlė
principas, invariantas, įrodymas prieštaros būdu. Jei [tema](/content/ontology_topics)
sako, *kokia teorija* naudojama, tai metodas sako, *kaip sudarytas samprotavimas*.
Žr. taip pat [ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Method` |
| Uždavinio savybė | `eliozo:method`, reikšmė yra metodo viršūnė, pvz., `eliozo:MTH_InvariantMethod` |
| Apimtis | 53 metodai dviejuose lygiuose; ID prasideda `MTH_` |
| Naršyti | [Rikiuoti > pagal metodą](/methods) |

## Metodo savybės

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:methodID` | ID, toks pat kaip viršūnės pavadinimas | `"MTH_PigeonholePrincipleBasic"` |
| `eliozo:methodName` | pavadinimas latviškai | `"Dirihlē princips"` |
| `eliozo:methodDescription` | aprašymas latviškai | |
| `eliozo:methodNumber` | vieta medyje | `"2.1"` |
| `eliozo:sorter_L1`, `eliozo:sorter_L2` | ta pati vieta sveikaisiais skaičiais | `2`, `1` |
| `skos:broader` / `skos:narrower` | tėvinė / vaikinės viršūnės | `eliozo:MTH_MeanValuePrinciple` |

Devynios metodų grupės:

| Nr. | ID | Pavadinimas |
|---|---|---|
| 1 | `MTH_MathematicalInduction` | matematinė indukcija |
| 2 | `MTH_MeanValuePrinciple` | vidutinės reikšmės metodas (Dirichlė principas) |
| 3 | `MTH_ExtremePrinciple` | kraštutinio elemento metodas |
| 4 | `MTH_InvariantMethod` | invariantų metodas |
| 5 | `MTH_ContradictionMethod` | įrodymas prieštaros būdu |
| 6 | `MTH_InterpretationMethod` | interpretacijų metodas (geometrinė, fizikinė, kodavimas, ...) |
| 7 | `MTH_Transformations` | reiškinių pertvarkiai |
| 8 | `MTH_Augmentation` | struktūrų papildymas (pagalbiniai elementai) |
| 9 | `MTH_Algorithms` | algoritminiai metodai |

Kai kurie uždaviniai turi metodų pavadinimus, kurių žodyne nėra (arba nebėra).
Automatiškai pasiūlyta savybė `eliozo:_hasReasoningMethod` (paprastas tekstas, žr.
[apžvalgą](/ontology)) naudoja savo, smulkesnius pavadinimus.

## Pavyzdžiai

Invariantų uždaviniai, sugrupuoti pagal invarianto rūšį:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:method ?method .
      ?method skos:broader* eliozo:MTH_InvariantMethod ;
              eliozo:methodName ?name .
    }
    ORDER BY ?name ?problemID

Indukcijos uždaviniai 9–12 klasėms, sugrupuoti pagal klases:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID ?grade (CONCAT(STR(?grade), " klasė") AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:method ?method .
      ?method skos:broader* eliozo:MTH_MathematicalInduction .
      FILTER (?grade >= 9)
    }
    ORDER BY ?grade ?problemID

Susiję: [užuominų tipai](/content/ontology_hint_types) siūlo metodus;
[modelis](/content/ontology_models) nurodo metodą, kuris jam paprastai taikomas.
