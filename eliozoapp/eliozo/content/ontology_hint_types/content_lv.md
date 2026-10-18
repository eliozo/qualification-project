# Norāžu tipi

**Norādes tips** ir heiristiska padoma veids, kas palīdz risinātājam, kurš iestrēdzis:
"izmēģini mazos gadījumus", "meklē invariantu", "pieņem pretējo". Norāžu tipi seko
uzdevumu risināšanas fāzēm, ko aprakstījuši Dž. Poja un P. Zeics. Katra konkrēta
uzdevuma [norāde](/content/ontology_hints) ir kāda norādes tipa. Skatīt arī
[ontoloģijas pārskatu](/ontology).

**Statuss: plānots.** Norāžu tipu saraksts ir izveidots, taču RDF krātuvē tā vēl nav,
tāpēc vaicājumos to vēl nevar izmantot.

## Norāžu tipi

| Fāze | Norāžu tipi |
|---|---|
| Saprast (Understand) | `ClarifyGoal` (noskaidro doto un prasīto), `DrawPicture` (uzzīmē attēlu), `UsingAllData` (izmanto visu doto) |
| Izpētīt (Explore) | `TrialAndError`, `SmallCases`, `LookForPattern`, `ExtremeCases`, `GuessThenProve`, `TryToDisprove`, `DropCondition` |
| Pārformulēt (Reformulate) | `Analogy`, `Paraphrase`, `Enumeration` (uzskaitīšana un kodēšana), `MakingItEasier`, `MakingItHarder` (vispārini), `WishfulThinking` |
| Risināt (Engage) | `AuxiliaryElements`, `CaseAnalysis`, `Continuity`, `DoubleCounting`, `Symmetry`, `WorkingBackwards`, `ParityAndRemainders`, `LookForInvariant`, `ExtremalElement`, `Pigeonhole`, `AssumeContrary`, `ReduceToSmaller`, `SplitIntoSubgoals`, `ExampleAndBound`, `TryColoring`, `TryOrdering` |
| Atskatīties (Review) | `LookBack` |

Katram norādes tipam ir nosaukums un apraksts latviski un angliski, un daudziem ir
atsauce `Suggests` uz [metodēm](/content/ontology_methods), pie kurām tas ved;
piemēram, `LookForInvariant` iesaka `MTH_InvariantMethod`, `DrawPicture` iesaka
`MTH_GeometricInterpretation`, bet `ExampleAndBound` ir parastā atrisinājuma
struktūra [jautājumam](/content/ontology_question_types) `FindOptimal`.

Saraksts tiek uzturēts Eliozo metadatu izklājlapas cilnē "hintTypes".
