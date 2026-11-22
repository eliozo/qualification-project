# About Advanced Search

On the [Advanced Search](/advanced_search) page, problems can be selected with SPARQL
queries directly from the Eliozo RDF graph. The concepts of the graph (statements and
solutions, classifiers, hierarchies and naming conventions) are described on the page
[Introduction to the Ontology](/ontology); this page collects what is needed for
writing queries.

## Namespaces

All names used below belong to two namespaces: the prefix `eliozo:` denotes the
resource types, properties and values specific to school competition mathematics;
`skos:` denotes the relations in classifier hierarchies (for example, the topic
"quadratic function" is narrower than the topic "algebra"). A typical query starts
with these prefix definitions:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

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
| `eliozo:domain` | domain (top level of the genres) | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | genre | `eliozo:DOM_GridCut` |
| `eliozo:topic` | topic | `eliozo:Divisibility` |
| `eliozo:method` | method | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | concept | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | question type | `"QTY_FindAll"` |
| `eliozo:problemSolution` | a solution node | |
| `eliozo:hasVideo` | a video node | |
| `eliozo:answer` | short answer | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | IDs of related or identical problems | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | for problems from books | `"BBK2012"`, `"P1"` |

Not every problem has every property: many problems still have no topic, method or
concepts.

**Solutions** (`eliozo:Solution`) have `eliozo:solutionText` (Markdown, with a
language tag), `eliozo:solutionTextHtml` and `eliozo:solutionNum`. **Videos**
(`eliozo:Video`) have `eliozo:videoTitle`, `eliozo:videoYoutube` and
`eliozo:videoBookmarks`, a list of `eliozo:VideoBookmark` nodes with
`eliozo:videoBookmarkTstamp` (seconds) and `eliozo:videoBookmarkText`.

## Machine-suggested labels

Properties whose names start with an underscore were proposed by a language model and
have not been reviewed. Their values are plain text, not classifier nodes:

| Property | Example values |
|---|---|
| `eliozo:_hasSolutionConcept` | `"DivisibilityRelation"`, `"Invariant"`, `"LatticeGrid"` |
| `eliozo:_hasReasoningMethod` | `"ConstructiveExampleForExistence"`, `"CaseAnalysis"` |
| `eliozo:_hasReasoningMistake` | `"FromSpecialToGeneral"` |
| `eliozo:_readingDifficulty` | `"low"`, `"medium"`, `"high"` |
| `eliozo:_mistakesFit` | `"low"`, `"medium"`, `"high"` |

They cover far more problems than the reviewed classifiers, so they are good for
finding candidates, but check the results.

## Writing queries

* A classifier node is written as a name: `?p eliozo:topic eliozo:Divisibility`.
  Text values go in quotes: `?p eliozo:domain "NT"`.
* To find everything under a node of a hierarchy, use a property path:
  `?t skos:broader* eliozo:Divisibility` matches `Divisibility` itself and every node
  below it.
* Use `OPTIONAL { ... }` for properties a problem may lack.
* Texts have language tags. To use only the Latvian text:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Advanced search shows the values of `?problemID`; `?section` and `?subsection`
  group them under subtitles.

## Examples

Each link opens the advanced search and runs the query at once; you can edit it there
and run it again. All these queries are also in the menu "Preset queries > Ontology"
above the query field; more examples are in the items "Examples", "Problem types" and
"Theory topics" of the same menu.

* Problems on divisibility for grades 5–7 (the topic `Divisibility` and everything
  under it), grouped by topic: [open the query](/advanced_search?queryLabel=onto-divisibility-grades-5-7).
* [Topics](/content/ontology_topics):
  [congruences](/advanced_search?queryLabel=onto-topic-congruence),
  [problems with a topic but no method](/advanced_search?queryLabel=onto-topic-without-method).
* [Methods](/content/ontology_methods):
  [invariants by kind](/advanced_search?queryLabel=onto-method-invariants),
  [induction for grades 9–12](/advanced_search?queryLabel=onto-method-induction).
* [Genres](/content/ontology_genres):
  [grids by grade](/advanced_search?queryLabel=onto-genre-grid-by-grade),
  [grids by topic](/advanced_search?queryLabel=grid-problems),
  [geometry genres](/advanced_search?queryLabel=onto-genre-geometry).
* [Question types](/content/ontology_question_types):
  ["find all" in number theory](/advanced_search?queryLabel=onto-qtype-find-all-nt),
  [the "find" group by type](/advanced_search?queryLabel=onto-qtype-find-group),
  [multiple choice with "find the largest"](/advanced_search?queryLabel=onto-qtype-find-optimal-choice).
* [Concepts](/content/ontology_concepts):
  [divisibility and primes](/advanced_search?queryLabel=onto-concept-divisibility-primes),
  [problems by concept](/advanced_search?queryLabel=onto-concept-by-term),
  [the suggested concept "Invariant"](/advanced_search?queryLabel=onto-concept-suggested-invariant).
* [Olympiads](/content/ontology_olympiads):
  [AMO grade 5 since 2020](/advanced_search?queryLabel=onto-olympiad-amo-grade-5),
  [geometry in national olympiads](/advanced_search?queryLabel=onto-olympiad-national-geometry).

## Where the data comes from

The classifiers are kept in the Eliozo metadata spreadsheets and exported to Turtle
files (`worksheet-generation-with-llms/scripts/setup/resources`); the problems are
converted from the Markdown files of the problem repositories. Problems are labelled
in their Markdown source, for example `* topic:Divisibility`.
