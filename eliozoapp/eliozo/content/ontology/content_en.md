# Introduction to the Ontology

The Eliozo problem base is an RDF graph. Every problem is a resource of the type
`eliozo:Problem`; its properties point to the problem text (in several languages),
its solutions, its source (a book or an olympiad, the year, the grade, the number on
the problem sheet) and to the metadata describing the problem, whose values usually
come from controlled classifier vocabularies. This page describes the concepts of the
graph; how to use them in SPARQL queries is explained on the page
[About Advanced Search](/content/about_advanced_search).

## Statements and solutions

The graph has two main resources — *problem statements* (RDF type `eliozo:Problem`)
and *problem solutions* (RDF type `eliozo:Solution`). The metadata accordingly forms
two layers:

* The **statement layer** holds classifiers that can be determined before solving the
  problem: the *question type* (the structure of the answer asked for), the *domain*,
  the *genre* (outward similarity or plot) and the *concepts* used in the conditions.
* The **solution layer** describes a specific solution: its *topics* (the theory used),
  its *model* (the "load-bearing" mathematical structure that connects the conditions
  with the solution; it is the bridge between the two layers), its *methods* (the
  tactics and reasoning patterns used) and the *concepts* used in the solution.

The following object types are also named "first-class" objects (non-anonymous RDF
resources with unique URLs):

* `eliozo:Claim` — a *claim* stated in the solution of a problem (additional claims or
  lemmas are usually needed for harder problems, for example in IMO solutions). Claims
  may have proofs of their own, with the same RDF type `eliozo:Solution`.
* `eliozo:Hint` — a *hint* attached either to a statement (of the original problem or
  of a claim within it) or to a solution. Recommended length: up to 160 characters.
  For some problems the hints are ordered from the most general to the most specific —
  that is a *hint ladder*.
* `eliozo:KeyIdea` — a *key idea*: a complete summary of a solution or of a part of it,
  after which only technical details remain for the solver. Unlike a hint, a key idea
  does not nudge towards anything, but it may be somewhat longer. Recommended length:
  up to 500 characters.

All these objects "belong" to a specific problem and do not exist on their own. Even
if an idea fits several problems, it is formulated independently in each of them.

## Classifiers

Property values are usually not invented anew for each problem but taken from a
*controlled vocabulary*. We informally call these vocabularies classifiers, because
their values often form hierarchies and are assigned by classification procedures.
Every classifier has its own page in this section of the menu.

| Classifier | What it describes | Problem property | Values | Browse |
|---|---|---|---|---|
| [Topics](/content/ontology_topics) | the theory used in solutions | `eliozo:topic` | `eliozo:Topic` nodes | [by Topic](/topics), [Topics Table](/topics_table) |
| [Methods](/content/ontology_methods) | the reasoning pattern of a solution | `eliozo:method` | `eliozo:Method` nodes | [by Method](/methods) |
| [Genres and domains](/content/ontology_genres) | one of the 4 domains; the (outward) setting of the problem | `eliozo:domain`, `eliozo:subdomain` | text; `eliozo:Domain` nodes | [by Genre](/genres) |
| [Question types](/content/ontology_question_types) | the question type and the expected structure of the solution | `eliozo:questionType` | text | [Filters](/filter) |
| [Concepts](/content/ontology_concepts) | concepts in the statement or in solutions | `eliozo:concepts` | `eliozo:Concept` nodes | [by Concept](/concepts) |
| [Olympiads](/content/ontology_olympiads) | the olympiad or another source | `eliozo:olympiad` | text | [Olympiads](/olympiads) |
| [Models](/content/ontology_models) | the "load-bearing" mathematical structure of a solution | *planned* | | |
| [Hint types](/content/ontology_hint_types) | the solving phase or the heuristic of a hint | *planned* | | |
| [Hints](/content/ontology_hints) | the hints of a specific problem | *planned* | | |

How the classifiers relate to each other:

![Relations between the classifiers](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

The diagram (labels in Latvian) shows the statement layer on the left (genre,
concepts, question type) and the solution layer on the right (topic, model, method).
Below them, the hint ladder supports the solver and suggests models and methods.
Solid lines are structural references between the classifier tables, dashed ones are
typical associations ("see also"), dotted ones are suggestions to the solver.
Relations marked with `*` are proposed and not yet filled in.

## Hierarchies (SKOS)

Topics, methods, genres and question types are SKOS hierarchies. Every node has
`skos:broader` (its parent) and the parents list `skos:narrower`. A node also has an
ID (`eliozo:topicID`, ...), a Latvian name (`eliozo:topicName`, ...), a description
and a number such as `"4.1.1.0.0"`, together with integer sort keys
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Problems can be labelled with nodes on any level. However, hierarchies may contain
nodes that only group their children (subcategories) and are not used for labelling
problems. For example, no problem has the topic `eliozo:TPC_Algebra` ("the solution
uses some algebra"), but a problem can have the topic `eliozo:TPC_Identities` ("the
solution uses algebraic identities"). Non-assignable concepts are marked with
`ex:assignable false`; all other concepts of a taxonomy are assignable by default.

The site does not yet use `skos:Collection` to build collections of concepts
independent of the hierarchy.

## Naming conventions

Resources, their types, properties and values have user-friendly names and unique
identifiers that rarely change, so queries stay relatively stable. This does not rule
out technical identifiers (GUIDs) at the infrastructure level, which are not meant for
user interfaces.

* **Problem identifiers:**
  - `LV.AMO.2026.5.1` — the Latvian Open Mathematics Olympiad 2026, grade 5,
    problem 1.
  - If there are several olympiads of the same type in a year, an extra letter tells
    them apart: `LV.AMO.2022A` took place in April 2022, `LV.AMO.2022B` in November
    2022. Similarly, `EE.LHT.2024S` is the Estonian open (*lahtine*) olympiad in autumn
    (*sügis*) and `EE.LHT.2024T` the one in winter (*talv*).
  - Codes of international olympiads start with `WW`: `WW.IMOSHL.2022.A1` is algebra
    problem 1 of the IMO shortlist, `WW.BW.2026.20` is problem 20 of Baltic Way 2026.
  - `BBK2012.P1.2` is a problem from the source BBK2012 (the book "Olimpiāžu un
    konkursu uzdevumu krājums skaitļu teorijā" by A.Bērziņš, A.Bērziņa and D.Kūma),
    part 1 ("Divisibility of numbers"), problem 2, while `BBK2012.P1.E2` is example 2
    of the same part. (Examples in books often have their own numbering and are
    usually presented together with their solutions.)
* **RDF type** names are in camel case and start with a capital letter:
  `eliozo:Problem`, `eliozo:KeyIdea`.
* **RDF property** names are in camel case and start with a lowercase letter:
  `eliozo:problemSolution`.
* **Classifier values** often get a prefix that tells the classifier:
  - `eliozo:TPC_Algebra` — the topic algebra;
  - `eliozo:MTH_MathematicalInduction` — the method of mathematical induction;
  - `eliozo:DOM_Algebra` — one of the 4 domains;
  - `eliozo:GEN_Weighings` — a genre: problems about weighings;
  - `QTY_FindAll` — a question type: find all and prove there are no others;
  - `RSP_SolutionFull` — a response format: a full solution with all justifications
    is required.

## Compatibility with other ontologies

Some problem properties (for example, the source and origin, the use of a concept,
formula or picture in the text, the copyright status) are objectively verifiable facts
that are not specific to olympiad mathematics. Currently they also use the `eliozo:`
namespace, but well-established vocabularies could be used instead:

* the content units of problems could be described with *Dublin Core* (for example,
  `dcterms:subject` instead of `eliozo:topic`);
* publicly known information about authors — with *FOAF*;
* the topics overlap considerably with the
  [2020 Mathematics Subject Classification (MSC2020)](https://mathscinet.ams.org/mathscinet/msc/msc2020.html);
* concepts could possibly be described following the thesaurus standard ISO 25964.
