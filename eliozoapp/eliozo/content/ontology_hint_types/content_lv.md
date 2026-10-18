# Ieteikumu tipi

**Ieteikuma tips** ir heiristisks padoms, lai palīdzētu sākt risināt:
"izmēģini mazos gadījumus", "meklē invariantu", "pieņem pretējo". Daži 
ieteikumu tipi atbilst
uzdevumu risināšanas fāzēm, ko aprakstījuši Dž. Poja un P. Zeics
(*Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*)
Konkrētam uzdevumam [norāde](/content/ontology_hints) ir īss vēstījums (līdz 140 drukas 
simboliem), kas satur 1-2 ieteikumu tipus kā heštagus. Sk. arī
[ontoloģijas pārskatu](/ontology).

**Statuss: plānots.** Ieteikumu tipu saraksts ir izveidots, taču RDF krātuvē 
tos neatspoguļojam, tāpēc arī SPARQL vaicājumos tos pagaidām neizmantojam.

## Ieteikumu tipi

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
