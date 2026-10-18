# Question types

The **question type** tells what kind of answer the problem asks for, and so what a
complete solution must contain: "find all" needs the solutions *and* a proof that
there are no others; "find the largest" needs an example *and* a bound. See also the
[ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Question` |
| Problem property | `eliozo:questionType`, value is the ID as **text**, e.g. `"FindAll"` |
| Size | 15 question types on two levels |
| Browse | [Filters](/filter) (by question type) |

## The question types

| ID | Parent | Meaning |
|---|---|---|
| `Find` | | find or compute |
| `FindAll` | `Find` | find all objects with the property (and show there are no others) |
| `FindValue` | `Find` | compute a value |
| `FindCount` | `Find` | count |
| `FindOptimal` | | find the largest/smallest: an example and a bound |
| `Prove` | | prove |
| `FindExample` | `Prove` | construct an example |
| `ProveExistence` | `Prove` | prove that something exists |
| `ProveUniversal` | `Prove` | prove a statement for all cases |
| `Decide` | | find out whether it is so or not |
| `DecideExistence` | `Decide` | "is it possible?" |
| `DecideUniversal` | `Decide` | "is it always so?" |
| `DecideWinner` | `Decide` | "who wins?" |
| `Algorithm` | | describe an algorithm or a strategy |
| `ShortAnswer` | | the answer only, without justification |

A question type node has `eliozo:questionID`, `eliozo:questionName` (Latvian),
`eliozo:questionDescription`, `eliozo:questionNumber` (`"1.1"`), `eliozo:sorter_L1`,
`eliozo:sorter_L2` and `skos:broader`. Many problems still carry the older value
`"ProveDisprove"` ("prove or disprove"), which roughly corresponds to the `Decide` group.

## Examples

"Find all" problems in number theory:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType "FindAll" ;
         eliozo:domain "NT" .
    }
    ORDER BY ?problemID

Because the problem holds the ID as text, join it with the vocabulary through
`eliozo:questionID`, e.g. to group all problems of the `Find` group by type:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT ?problemID (?type AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType ?type .
      ?q eliozo:questionID ?type ;
         skos:broader* eliozo:Find .
    }
    ORDER BY ?type ?problemID

Related: the question type is in the problem statement layer, next to
[genres](/content/ontology_genres) and [concepts](/content/ontology_concepts); it
points to typical [methods](/content/ontology_methods).
