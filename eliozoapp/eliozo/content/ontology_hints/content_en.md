# Hints

**Hints** belong to one problem: a short sequence of advice ordered from the most
general to the most specific (a *hint ladder*). A solver who is stuck reads one hint
at a time and gets only as much help as needed. In the [classifier diagram](/ontology)
the hint ladder is the solver's support: its hints suggest
[models](/content/ontology_models) and [methods](/content/ontology_methods).

Every hint is classified by a [hint type](/content/ontology_hint_types), so that, for
instance, all problems whose ladder contains "look for an invariant" can be found
and the phases of a ladder (understand, explore, reformulate, engage, review) can be
compared across problems.

**Status: planned.** Hints are not yet stored with the problems and cannot be used in
queries yet. Until then, the machine-suggested properties
`eliozo:_hasReasoningMethod` and `eliozo:_hasSolutionConcept` (see the
[overview](/ontology)) are the closest substitute for finding problems by the idea of
their solution.
