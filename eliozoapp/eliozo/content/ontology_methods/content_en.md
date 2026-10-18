# Methods

A **method** is the reasoning pattern of a solution: mathematical induction, the
pigeonhole principle, an invariant, proof by contradiction. Where a
[topic](/content/ontology_topics) says *what theory* is used, the method says *how the
argument is built*. See also the [ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Method` |
| Problem property | `eliozo:method`, value is a method node, e.g. `eliozo:MTH_InvariantMethod` |
| Size | 53 methods on two levels; IDs start with `MTH_` |
| Browse | [Order > by Method](/methods) |

## Properties of a method

| Property | Value | Example |
|---|---|---|
| `eliozo:methodID` | ID, the same as the node name | `"MTH_PigeonholePrincipleBasic"` |
| `eliozo:methodName` | name in Latvian | `"Dirihlē princips"` |
| `eliozo:methodDescription` | description in Latvian | |
| `eliozo:methodNumber` | position in the tree | `"2.1"` |
| `eliozo:sorter_L1`, `eliozo:sorter_L2` | the same position as integers | `2`, `1` |
| `skos:broader` / `skos:narrower` | parent / children | `eliozo:MTH_MeanValuePrinciple` |

The nine method groups:

| No. | ID | Name |
|---|---|---|
| 1 | `MTH_MathematicalInduction` | mathematical induction |
| 2 | `MTH_MeanValuePrinciple` | mean value principle (pigeonhole) |
| 3 | `MTH_ExtremePrinciple` | extremal element |
| 4 | `MTH_InvariantMethod` | invariants |
| 5 | `MTH_ContradictionMethod` | proof by contradiction |
| 6 | `MTH_InterpretationMethod` | interpretations (geometric, physical, coding, ...) |
| 7 | `MTH_Transformations` | transformations of expressions |
| 8 | `MTH_Augmentation` | augmenting a structure (auxiliary elements) |
| 9 | `MTH_Algorithms` | algorithmic methods |

Some problems are labelled with method names that are not (or no longer) in the
vocabulary. The machine-suggested property `eliozo:_hasReasoningMethod` (plain text,
see the [overview](/ontology)) uses its own, finer names.

## Examples

Invariant problems, grouped by the kind of invariant:

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

Induction problems for grades 9 to 12, grouped by grade:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID ?grade (CONCAT("Grade ", STR(?grade)) AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:method ?method .
      ?method skos:broader* eliozo:MTH_MathematicalInduction .
      FILTER (?grade >= 9)
    }
    ORDER BY ?grade ?problemID

Related: [hint types](/content/ontology_hint_types) suggest methods; a
[model](/content/ontology_models) refers to the method usually applied to it.
