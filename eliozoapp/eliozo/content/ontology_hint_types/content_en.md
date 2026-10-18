# Hint types

A **hint type** is a kind of heuristic advice that helps a solver who is stuck:
"try small cases", "look for an invariant", "assume the contrary". The hint types
follow the four phases of problem solving described by G. Pólya and P. Zeitz. The
[hints](/content/ontology_hints) of a particular problem are each of some hint type.
See also the [ontology overview](/ontology).

**Status: planned.** The list of hint types exists, but it is not yet in the RDF
store, so it cannot be used in queries yet.

## The hint types

| Phase | Hint types |
|---|---|
| Understand | `ClarifyGoal` (clarify givens and goal), `DrawPicture`, `UsingAllData` (use all the data) |
| Explore | `TrialAndError`, `SmallCases`, `LookForPattern`, `ExtremeCases`, `GuessThenProve`, `TryToDisprove`, `DropCondition` |
| Reformulate | `Analogy`, `Paraphrase`, `Enumeration` (enumeration and encoding), `MakingItEasier`, `MakingItHarder` (generalize), `WishfulThinking` |
| Engage | `AuxiliaryElements`, `CaseAnalysis`, `Continuity`, `DoubleCounting`, `Symmetry`, `WorkingBackwards`, `ParityAndRemainders`, `LookForInvariant`, `ExtremalElement`, `Pigeonhole`, `AssumeContrary`, `ReduceToSmaller`, `SplitIntoSubgoals`, `ExampleAndBound`, `TryColoring`, `TryOrdering` |
| Review | `LookBack` |

Every hint type has a Latvian and an English title and description, and many have a
`Suggests` reference to the [methods](/content/ontology_methods) they lead to; for
example `LookForInvariant` suggests `MTH_InvariantMethod`, `DrawPicture` suggests
`MTH_GeometricInterpretation` and `ExampleAndBound` is the usual structure of a
`FindOptimal` [question](/content/ontology_question_types).

The list is kept in the "hintTypes" tab of the Eliozo metadata spreadsheet.
