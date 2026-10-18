# Ontology

The Eliozo problem base is stored as an RDF graph. Every problem is a node of the
class `eliozo:Problem`; its properties point to its texts, its solutions, the
olympiad it comes from and to the **classifiers** (metadata) that describe it. This page is
a map of that graph for anyone writing queries on the
[Advanced search](/advanced_search) page.

All names used below belong to two namespaces:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Classifiers

| Classifier | What it describes | Problem property | Values | Browse |
|---|---|---|---|---|
| [Topics](/content/ontology_topics) | the theory the solution uses | `eliozo:topic` | `eliozo:Topic` nodes | [by Topic](/topics), [Topics Table](/topics_table) |
| [Methods](/content/ontology_methods) | the reasoning pattern of the solution | `eliozo:method` | `eliozo:Method` nodes | [by Method](/methods) |
| [Genres](/content/ontology_genres) | what the problem looks like, its "plot" | `eliozo:domain`, `eliozo:subdomain` | text; `eliozo:Domain` nodes | [by Genre](/genres) |
| [Question types](/content/ontology_question_types) | what kind of answer is asked for | `eliozo:questionType` | text | [Filters](/filter) |
| [Concepts](/content/ontology_concepts) | notions used in the statement | `eliozo:concepts` | `eliozo:Concept` nodes | [by Concept](/concepts) |
| [Olympiads](/content/ontology_olympiads) | the competition | `eliozo:olympiad` | text | [Olympiads](/olympiads) |
| [Models](/content/ontology_models) | the mathematical structure the solver builds | *planned* | | |
| [Hint types](/content/ontology_hint_types) | kinds of heuristic hints | *planned* | | |
| [Hints](/content/ontology_hints) | the hints of one problem | *planned* | | |

How the classifiers relate to each other:

![Relations between the classifiers](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

The diagram (labels in Latvian) has two layers. The **problem statement layer**
(left) can be seen without solving the problem: its *genre* (outward similarity,
the plot), the *concepts* in its conditions and its *question type* (the structure of
the answer that is asked for). The **solution layer** (right) describes one specific
solution: its *topic* (theory), its *model* (the mathematical structure built by the
solver; the model is the bridge between the two layers) and its *method* (the
reasoning pattern). Below them, a *hint ladder* supports the solver and suggests
models and methods.

Solid arrows are structural references between the classifier tables, dashed ones
are typical associations ("see also"), dotted ones are suggestions to the solver.
Relations marked with `*` are proposed and not yet filled in.

## The problem node

| Property | Value | Example |
|---|---|---|
| `eliozo:problemID` | text | `"LV.AMO.2019.7.4"` |
| `eliozo:problemText` | Markdown, one per translation, with a language tag | `"Andris apgalvo, ..."@lv` |
| `eliozo:problemTextHtml` | the same text as HTML | |
| `eliozo:olympiad` | olympiad ID | `"LV.AMO"` |
| `eliozo:olympiadCode`, `eliozo:country` | parts of that ID | `"AMO"`, `"LV"` |
| `eliozo:event` | one round of the olympiad | `"LV.AMO.2019"` |
| `eliozo:problemYear`, `eliozo:problemGrade` | integers | `2019`, `7` |
| `eliozo:suggestedGrade` | integer, may repeat | `7` |
| `eliozo:olympiadType` | text | `"National"`, `"RegionalOrOpen"`, `"TeamSelection"`, `"International"`, `"Contest"`, `"Book"` |
| `eliozo:domain` | genre, top level | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | genre | `eliozo:DOM_GridCut` |
| `eliozo:topic` | topic | `eliozo:Divisibility` |
| `eliozo:method` | method | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | concept | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | question type | `"FindAll"` |
| `eliozo:problemSolution` | a solution node | |
| `eliozo:hasVideo` | a video node | |
| `eliozo:answer` | short answer | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | IDs of related or identical problems | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | for problems from books | `"BBK2012"`, `"P1"` |

Not every problem has every property: many problems still have no topic, method or
concepts. Use `OPTIONAL { ... }` for properties that may be missing.

**Solutions** (`eliozo:Solution`) have `eliozo:solutionText` (Markdown, with a
language tag), `eliozo:solutionTextHtml` and `eliozo:solutionNum`. **Videos**
(`eliozo:Video`) have `eliozo:videoTitle`, `eliozo:videoYoutube` and
`eliozo:videoBookmarks`, a list of `eliozo:VideoBookmark` nodes with
`eliozo:videoBookmarkTstamp` (seconds) and `eliozo:videoBookmarkText`.

## Machine-suggested labels

Properties whose names start with an underscore were proposed by a language model
and have not been reviewed. Their values are plain text, not classifier nodes:

| Property | Example values |
|---|---|
| `eliozo:_hasSolutionConcept` | `"DivisibilityRelation"`, `"Invariant"`, `"LatticeGrid"` |
| `eliozo:_hasReasoningMethod` | `"ConstructiveExampleForExistence"`, `"CaseAnalysis"` |
| `eliozo:_hasReasoningMistake` | `"FromSpecialToGeneral"` |
| `eliozo:_readingDifficulty` | `"low"`, `"medium"`, `"high"` |
| `eliozo:_mistakesFit` | `"low"`, `"medium"`, `"high"` |

They cover far more problems than the reviewed classifiers, so they are good for
finding candidates, but check the results.

## Hierarchies

Topics, methods, genres and question types are SKOS hierarchies. Every node has
`skos:broader` (its parent) and the parents list `skos:narrower`. A node also has
an ID (`eliozo:topicID`, ...), a Latvian name (`eliozo:topicName`, ...), a
description and a number such as `"4.1.1.0.0"`, together with integer sort keys
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Problems can be labelled with nodes on any level. To find everything under a node,
follow the hierarchy with a property path: `?t skos:broader* eliozo:Divisibility`
matches `Divisibility` itself and every node below it.

## Writing queries

* A classifier node is written as a name: `?p eliozo:topic eliozo:Divisibility`.
  Text values go in quotes: `?p eliozo:domain "NT"`.
* Texts have language tags. To use only the Latvian text:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Advanced search shows the values of `?problemID`; `?section` and `?subsection`
  group them under subtitles.

Example: number theory problems for grades 5 to 7 about divisibility (the
`Divisibility` topic and everything under it), grouped by topic:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?topicName AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:topic ?topic .
      ?topic skos:broader* eliozo:Divisibility ;
             eliozo:topicName ?topicName .
      FILTER (?grade >= 5 && ?grade <= 7)
    }
    ORDER BY ?topicName ?problemID

The menu "Preset queries" above the query field has more examples.

## Where the data comes from

The classifiers are kept in the Eliozo metadata spreadsheets and exported to Turtle
files (`worksheet-generation-with-llms/scripts/setup/resources`); the problems are
converted from the Markdown files of the problem repositories. Problems are labelled
in their Markdown source, for example `* topic:Divisibility`.

Related standards: the topics are comparable to the
[2020 Mathematics Subject Classification](https://mathscinet.ams.org/mathscinet/msc/msc2020.html)
(MSC2020), and the hierarchies follow the thesaurus standard ISO 25964 (a node that
only groups its children is a *category* and is not assigned to problems).
