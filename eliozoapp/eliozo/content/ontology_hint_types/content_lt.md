# Užuominų tipai

**Užuominos tipas** yra euristinio patarimo rūšis, padedanti įstrigusiam sprendėjui:
„išbandyk mažus atvejus“, „ieškok invarianto“, „tarkime priešingai“. Užuominų tipai
atitinka uždavinių sprendimo fazes, kurias aprašė Dž. Polya ir P. Zeitzas. Kiekviena
konkretaus uždavinio [užuomina](/content/ontology_hints) yra kurio nors užuominos
tipo. Žr. taip pat [ontologijos apžvalgą](/ontology).

**Būsena: planuojama.** Užuominų tipų sąrašas sudarytas, tačiau RDF saugykloje jo dar
nėra, todėl užklausose jo dar negalima naudoti.

## Užuominų tipai

| Fazė | Užuominų tipai |
|---|---|
| Suprasti (Understand) | `ClarifyGoal` (išsiaiškink, kas duota ir ko klausiama), `DrawPicture` (nubraižyk brėžinį), `UsingAllData` (panaudok visus duomenis) |
| Tyrinėti (Explore) | `TrialAndError`, `SmallCases`, `LookForPattern`, `ExtremeCases`, `GuessThenProve`, `TryToDisprove`, `DropCondition` |
| Performuluoti (Reformulate) | `Analogy`, `Paraphrase`, `Enumeration` (išvardijimas ir kodavimas), `MakingItEasier`, `MakingItHarder` (apibendrink), `WishfulThinking` |
| Spręsti (Engage) | `AuxiliaryElements`, `CaseAnalysis`, `Continuity`, `DoubleCounting`, `Symmetry`, `WorkingBackwards`, `ParityAndRemainders`, `LookForInvariant`, `ExtremalElement`, `Pigeonhole`, `AssumeContrary`, `ReduceToSmaller`, `SplitIntoSubgoals`, `ExampleAndBound`, `TryColoring`, `TryOrdering` |
| Apžvelgti (Review) | `LookBack` |

Kiekvienas užuominos tipas turi pavadinimą ir aprašymą latviškai ir angliškai, o
daugelis turi nuorodą `Suggests` į [metodus](/content/ontology_methods), prie kurių
jis veda; pavyzdžiui, `LookForInvariant` siūlo `MTH_InvariantMethod`, `DrawPicture`
siūlo `MTH_GeometricInterpretation`, o `ExampleAndBound` yra įprasta
[klausimo](/content/ontology_question_types) `FindOptimal` sprendimo struktūra.

Sąrašas tvarkomas Eliozo metaduomenų skaičiuoklės skirtuke „hintTypes“.
