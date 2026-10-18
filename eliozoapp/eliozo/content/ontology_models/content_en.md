# Models

A **model** is the mathematical structure that the solver builds to solve the
problem: a linear relation between quantities, "distance = speed × time", a graph
of acquaintances, a table of remainders. In the [classifier diagram](/ontology) the
model is the bridge between the problem statement and the solution: a problem of a
given [genre](/content/ontology_genres) is translated into a model, and the model is
then handled with a [method](/content/ontology_methods) and the theory of a
[topic](/content/ontology_topics).

**Status: planned.** The list of models exists, but models are not yet in the RDF
store and problems are not yet labelled with them, so they cannot be used in
queries yet.

## The list of models

About 135 models, with IDs that start with `MDL_`, for example:

| ID | Model |
|---|---|
| `MDL_LinearRelationBetweenQuantities` | linear relation between quantities |
| `MDL_DistanceTimeSpeed` | distance equals speed times time |
| `MDL_ProportionsAndRatios` | proportions and ratios |
| `MDL_PercentagesAsRatios` | percentages as ratios and changes |
| `MDL_ParityInvariant` | parity invariant |
| `MDL_PairingStrategyInGames` | pairing strategy in games |

Every model has a Latvian and an English title, a Latvian description, a domain
(`Alg`, `Comb`, `Geom`, `NT`), a concept group, a grade level and references:

* `MethodRef`: the [method](/content/ontology_methods) usually applied to the model,
  e.g. `MTH_AlgebraicModel`;
* `TopicRefs`: related [topics](/content/ontology_topics);
* `ConceptRefs`: the [concepts](/content/ontology_concepts) the model is built from.

The list is kept in the "models" tab of the Eliozo metadata spreadsheet.
