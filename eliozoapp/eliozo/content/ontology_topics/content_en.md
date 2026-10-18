# Topics

A **topic** names the piece of theory that a solution uses: divisibility, similar
triangles, the inclusion-exclusion principle. Topics answer the question *what is
this problem about mathematically?* See also the [ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Topic` |
| Problem property | `eliozo:topic`, value is a topic node, e.g. `eliozo:Divisibility` |
| Size | 637 topics on up to five levels |
| Browse | [Order > by Topic](/topics), [Topics Table](/topics_table) |

## Properties of a topic

| Property | Value | Example |
|---|---|---|
| `eliozo:topicID` | ID, the same as the node name | `"IntegerCongruence"` |
| `eliozo:topicName` | name in Latvian | `"Kongruence pēc moduļa"` |
| `eliozo:topicDescription` | description in Latvian | |
| `eliozo:topicNumber` | position in the tree | `"4.4.0.0.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L5` | the same position as integers | `4`, `4`, `0`, `0`, `0` |
| `skos:broader` / `skos:narrower` | parent / children | `eliozo:NumTheory` |

The four top-level topics are `Algebra` (1), `Combinatorics` (2), `Geometry` (3) and
`NumTheory` (4). Problems are labelled on any level, from `NumTheory` itself down to
narrow topics such as `ChineseRemainderTheorem`.

The store also holds a second, separate topic tree imported from
[problems.ru](https://problems.ru): its nodes are `eliozo:Topic` as well, but have
`eliozo:topicTitle` and `skos:topicUrl` instead of `eliozo:topicNumber`, and no problems
point to them. Add `eliozo:topicNumber ?n` to a pattern to keep only the main tree.

## Examples

Problems on congruences (`IntegerCongruence` and all topics under it), grouped by
the narrowest topic:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:topic ?topic .
      ?topic skos:broader* eliozo:IntegerCongruence ;
             eliozo:topicName ?name .
    }
    ORDER BY ?name ?problemID

Problems that have a topic but no [method](/content/ontology_methods) yet, grouped by
top-level topic:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?rootName AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:topic ?topic .
      ?topic skos:broader* ?root .
      ?root eliozo:topicName ?rootName .
      FILTER NOT EXISTS { ?root skos:broader ?anyParent }
      FILTER NOT EXISTS { ?p eliozo:method ?anyMethod }
    }
    ORDER BY ?rootName ?problemID

Related: a topic often comes with typical [methods](/content/ontology_methods);
[genres](/content/ontology_genres) and [concepts](/content/ontology_concepts) refer
to typical topics.
