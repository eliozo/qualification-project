# Concepts

A **concept** is a mathematical notion that occurs in the problem statement: prime
number, sum, triangle, divisibility. Concepts help to find problems by their
vocabulary and to see which terms a student must know to read the problem. See also
the [ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Concept` |
| Problem property | `eliozo:concepts`, value is a concept node, e.g. `eliozo:TRM-divisibility` |
| Size | 134 concepts, no hierarchy; node names start with `TRM-` |
| Browse | [Order > by Concept](/concepts) |

## Properties of a concept

| Property | Value | Example |
|---|---|---|
| `eliozo:conceptID` | ID, tagged `@en` | `"absolute-value"@en` |
| `eliozo:termEN` | English term | `"absolute value"@en` |
| `eliozo:termLV` | Latvian term | `"absolūtā vērtība"@lv` |
| `eliozo:descLV` | Latvian explanation (only some concepts) | |

Because `eliozo:conceptID` has a language tag, compare it with `"primes"@en` or with
`STR(?id) = "primes"`.

A larger list of concepts (about 270, CamelCase names such as `PositiveIntegers`,
grouped and linked to [topics](/content/ontology_topics)) is being prepared and is not
yet in the store. The machine-suggested property `eliozo:_hasSolutionConcept` (plain
text, see the [overview](/ontology)) already uses mostly names from that list.

## Examples

Problems that use both divisibility and prime numbers:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:concepts eliozo:TRM-divisibility, eliozo:TRM-primes .
    }
    ORDER BY ?problemID

Problems grouped by their concepts, with the English term as subtitle:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (?term AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:concepts ?concept .
      ?concept eliozo:termEN ?term .
    }
    ORDER BY ?term ?problemID

Problems whose machine-suggested concepts include "Invariant":

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:_hasSolutionConcept "Invariant" .
    }
    ORDER BY ?problemID

Related: [models](/content/ontology_models) refer to the concepts they are built
from.
