# Semantic search

Semantic search finds problems that are **about the same thing** as the text you type,
even if they share no words with it. It does not look for letters or patterns at all:
both your text and every problem are turned into a vector of 1536 numbers (an
*embedding*, computed by the OpenAI model `text-embedding-3-small`), and the problems
whose vectors point in the closest direction are returned (cosine distance, stored and
searched in PostgreSQL with the `pgvector` extension).

## How much text to type

The whole query becomes a single vector, so its length matters:

| Query | What to expect |
|---|---|
| one or two words, e.g. `trijstūris` | weak: too little meaning, results are loose associations — use [exact search](/content/search_by_keyword) instead |
| one sentence describing the idea, e.g. *the sum of the digits of a number divisible by 9* | good: typical problems on that idea |
| a whole problem statement, pasted | best: problems with the same plot or structure — similar problems, variants and duplicates from other olympiads |

Up to about **8000 characters** (several pages) are taken into account; anything longer
is cut off. Very long texts that mix several ideas are averaged into one vector, so the
result follows the dominant idea — paste one problem at a time.

## What it can and cannot find

* **Similar problems.** Pasting a problem finds others with the same setting (a
  chessboard, a tournament, coins on a table) or the same kind of question, even when
  the numbers and names differ.
* **Synonyms and paraphrases** are matched: *equilateral triangle* and *a triangle with
  all sides equal* end up close to each other.
* **Inflected forms** do not matter: *trijstūris*, *trijstūrim*, *trijstūru* mean the
  same to the model, so there is no need to search by stems.
* **Other languages.** The model is multilingual: a query in English or Lithuanian also
  finds problems written in Latvian, and vice versa. A query in the language of the
  problems still tends to give slightly closer matches.
* **Typos** usually do no harm.
* **Exact conditions are not checked.** Negation (*not divisible*), specific numbers,
  "at least" versus "at most" barely change the vector. A problem that is close in
  meaning but differs in such a detail will still be found — and ranked high.
* **Methods are only found if they are written down.** The statement rarely says how a
  problem is solved; to search by an idea of the solution (*pigeonhole principle*,
  *invariant*), choose **In solutions**.

## Formulas

LaTeX formulas are read as ordinary text. They add to the meaning a little — a query
with `\sqrt{}` and `\geq` leans towards inequalities with roots — but the model does not
do mathematics: `x^2-1` and `(x-1)(x+1)` are not recognised as equal, and a formula
alone is a poor query. Describe the formula in words, or use
[exact search](/content/search_by_keyword) to look for a specific piece of LaTeX.

## Where it searches, and how many results

The drop-down next to the search box chooses what is compared:

* **In problems** — the problem statements. Each problem is stored in one language,
  Latvian whenever a Latvian text exists.
* **In solutions** — the statements **and** every solution, in every language. A
  problem ranks by whichever of its texts is closest to the query.

There is **no threshold**: the search always returns the **20** closest problems (two
pages), ordered from the closest, even if none of them is really relevant. The first
results are the most reliable; judge the rest yourself.
