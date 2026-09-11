# Exact search

Exact search looks for the text you type **as a literal substring** of the problem.
There is no stemming, no tokenizing into words and no spell-checking: the text you
type must occur character by character somewhere in the problem.

## Word stems and endings

Because the match is a substring and not a whole word, you can search for a **stem**
and find every ending. This matters in Latvian and Lithuanian, where nouns change
their ending in every case:

| You type | Also found |
|---|---|
| `trijstūr` | trijstūris, trijstūra, trijstūrim, trijstūri, trijstūrī, trijstūriem |
| `kvadrāt` | kvadrāts, kvadrāta, kvadrātu, kvadrātā, kvadrātvienādojums |
| `trikamp` | trikampis, trikampio, trikampiui, trikampį |

Two things to keep in mind:

* The stem is matched **anywhere in a word**, not only at its beginning — `rēķin`
  also finds *aprēķini* and *sarēķini*.
* Only the ending may vary. Where the stem itself changes, one search is not enough:
  *skaitlis* has the stem `skaitl`, but *skaitļa*, *skaitļi* and *skaitļu* have
  `skaitļ`. In this problem base `skaitl` occurs in 1040 problems and `skaitļ` in
  1475 — neither of them finds the other's forms.

For cases like that, and whenever you need exactly one of several endings, use
[regular expression search](/content/search_by_regex): `skait(l|ļ)\w*` covers all 1825 of
those problems at once, and `trijstūr(is|a|im)` narrows a search down to three
specific forms.

## Phrases

You can type a whole phrase, including spaces and punctuation — `taisnleņķa trijstūris`
is matched as a single string, not as two independent words.

The catch is that problem texts are stored as Markdown with **line breaks inside the
sentences**. A phrase that your browser shows on one line may be split in the source:

<pre><code>Cik dažādos veidos skaitli &#36;2011&#36; var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu?
</code></pre>

Here `pēc kārtas sekojošu` contains a newline where you would type a space, so the
exact phrase does not match. If a phrase you are sure about returns nothing, search
for the shortest fragment that cannot be split, or switch to regular expression
search and write `\s+` (any whitespace) in place of the space:

    kārtas\s+sekojošu

## Letter case

Exact search is **case insensitive**. `Trijstūris`, `trijstūris` and `TRIJSTŪRIS`
all return the same problems. Diacritics are *not* ignored, though: `trijsturis`
without the macron finds nothing.

## Searching for formulas

All formulas in the problem base are written in LaTeX. In exact search you type the
LaTeX exactly as it appears in the text, with a **single** backslash and no escaping:

| You type | Finds |
|---|---|
| `\sqrt[3]{` | problems containing a cubic root |
| `\frac{1}{2}` | problems containing the fraction one half |
| `\mathrm{cm}` | problems measured in centimetres |

Characters that are special in a regular expression — `(` `)` `[` `]` `{` `}` `.`
`*` `+` `?` `^` `|` `\` — have no special meaning here; they are matched as
themselves. That makes exact search
the simpler choice whenever you know the literal text you are after. To search for a
*pattern* rather than a fixed string, use
[regular expression search](/content/search_by_regex).

## Where it searches, and how many results

The drop-down next to the search box chooses what is searched:

* **In problems** — the problem statements only.
* **In solutions** — the problem statements **and** all of their solutions. A problem
  is returned when the text occurs in the statement or in any one of its solutions,
  so this can only ever add results, never remove them.

At most **10** problems are returned, ordered by grade and then by problem
identifier. If you get exactly 10 results, there are probably more — make the search
text longer and more specific.
