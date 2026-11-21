# Genres

A **genre** describes what a problem looks like from the outside, before it is
solved: a word problem, a grid to be cut, a tournament, a weighing puzzle, an
equation in integers. Problems of one genre share their "plot" even when they are
solved in different ways. See also the [ontology overview](/ontology).

| | |
|---|---|
| Class | `eliozo:Domain` (the class keeps its older name) |
| Problem properties | `eliozo:domain`: the top level as text, `"Alg"`, `"Comb"`, `"Geom"` or `"NT"`; `eliozo:subdomain`: a genre node, e.g. `eliozo:DOM_GridCut` |
| Size | 80 genres on three levels; IDs below the top level start with `DOM_` |
| Browse | [Order > by Genre](/genres), [Filters](/filter) (by domain) |

## Properties of a genre

| Property | Value | Example |
|---|---|---|
| `eliozo:domainID` | ID, the same as the node name | `"DOM_Triangles"` |
| `eliozo:domainName` | name in Latvian | `"Trijstūri"` |
| `eliozo:domainDescription` | description in Latvian | |
| `eliozo:domainNumber` | position in the tree | `"3.4.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L3` | the same position as integers | `3`, `4`, `0` |
| `skos:broader` / `skos:narrower` | parent / children | `eliozo:Geom` |

The top level:

| ID (`eliozo:domain`) | Genre | Examples below it |
|---|---|---|
| `Alg` | Algebra | `DOM_WordProblems`, `DOM_Equations`, `DOM_Inequalities` |
| `Comb` | Combinatorics | `DOM_CountingObjects`, `DOM_Graphs`, `DOM_GridCut` |
| `Geom` | Geometry | `DOM_Triangles`, `DOM_IntegerLattices` |
| `NT` | Number theory | `DOM_NumeralSystems`, `DOM_NumericConstructions` |

Note the difference: `eliozo:domain` is **text** and holds only the top level,
`eliozo:subdomain` is a **node** of the hierarchy.

## Examples

Grid problems (all genres 3.16.x), grouped by grade: [open the query](/advanced_search?queryLabel=onto-genre-grid-by-grade). The same problems grouped by genre: [open the query](/advanced_search?queryLabel=grid-problems).

All geometry genres with their problems, two levels of subtitles: [open the query](/advanced_search?queryLabel=onto-genre-geometry).

Related: genres refer to their typical [topics](/content/ontology_topics) and
[models](/content/ontology_models).
