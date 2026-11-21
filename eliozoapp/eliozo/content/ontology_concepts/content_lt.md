# Sąvokos

**Sąvoka** yra matematinė sąvoka, kuri pasitaiko uždavinio formuluotėje: pirminis
skaičius, suma, trikampis, dalumas. Sąvokos padeda rasti uždavinius pagal jų žodyną ir
matyti, ką mokinys turi žinoti, kad perskaitytų uždavinį. Žr. taip pat
[ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Concept` |
| Uždavinio savybė | `eliozo:concepts`, reikšmė yra sąvokos viršūnė, pvz., `eliozo:TRM-divisibility` |
| Apimtis | 134 sąvokos be hierarchijos; viršūnių pavadinimai prasideda `TRM-` |
| Naršyti | [Rikiuoti > pagal sąvoką](/concepts) |

## Sąvokos savybės

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:conceptID` | ID su žyme `@en` | `"absolute-value"@en` |
| `eliozo:termEN` | terminas angliškai | `"absolute value"@en` |
| `eliozo:termLV` | terminas latviškai | `"absolūtā vērtība"@lv` |
| `eliozo:descLV` | paaiškinimas latviškai (tik kai kurioms sąvokoms) | |

Kadangi `eliozo:conceptID` turi kalbos žymę, lyginkite jį su `"primes"@en` arba su
`STR(?id) = "primes"`.

Rengiamas platesnis sąvokų sąrašas (apie 270 sąvokų su CamelCase pavadinimais,
pavyzdžiui, `PositiveIntegers`, sugrupuotų ir susietų su
[temomis](/content/ontology_topics)); saugykloje jo dar nėra. Automatiškai pasiūlyta
savybė `eliozo:_hasSolutionConcept` (paprastas tekstas, žr. [apžvalgą](/ontology))
jau naudoja daugiausia šio sąrašo pavadinimus.

## Pavyzdžiai

Uždaviniai, kuriuose naudojamas ir dalumas, ir pirminiai skaičiai: [atverti užklausą](/advanced_search?queryLabel=onto-concept-divisibility-primes).

Uždaviniai, sugrupuoti pagal sąvokas, su angliškuoju terminu kaip paantrašte: [atverti užklausą](/advanced_search?queryLabel=onto-concept-by-term).

Uždaviniai, kurių automatiškai pasiūlytose sąvokose yra „Invariant“: [atverti užklausą](/advanced_search?queryLabel=onto-concept-suggested-invariant).

Susiję: [modeliai](/content/ontology_models) nurodo sąvokas, iš kurių jie sudaryti.
