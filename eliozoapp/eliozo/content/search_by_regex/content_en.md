# Regular expression search

Regular expression search matches a **pattern** instead of a fixed string. Use it
when the thing you are looking for varies: a noun with any case ending, a formula
with any numbers in it, or a phrase that may be broken across a line.

Search is **case insensitive** by default, and a pattern matches anywhere inside the
problem text — it does not have to match the whole text.

## The backslash rule

This is the one thing worth learning before anything else. In a regular expression a
backslash starts an escape sequence, so a **LaTeX backslash has to be written twice**:

| You type | Matches in the text | Wrong |
|---|---|---|
| `\\frac` | `\frac` | `\frac` finds nothing |
| `\\sqrt` | `\sqrt` | `\sqrt` finds nothing |
| `\\sin` | `\sin` | `\sin` finds nothing |

The braces, brackets and parentheses of LaTeX are special in a regular expression as
well, so they get a single backslash in front of them: `\{` `\}` `\[` `\]` `\(` `\)`.
Putting the two rules together, the opening of a LaTeX cubic root, `\sqrt[3]{`, is
searched for as

    \\sqrt\[3\]\{

If you do not want to think about escaping at all, use
[exact search](/content/search_by_keyword) instead — there every character means itself.

## Nouns with all their endings

Latvian and Lithuanian nouns change their ending in every case. List the endings in
a group, separated by vertical bars:

    trijstūr(is|a|im|i|ī|iem|os)

    trikamp(is|io|iui|į|yje)

If you do not care which ending it is, match any run of letters instead. `\w` is one
letter or digit, and `*` means "any number of them":

    trijstūr\w*

Note that the base form also appears inside compound and derived words, so
`kvadrāt\w*` will also bring up *kvadrātvienādojums*. Anchor the pattern with `\b`
if you want a word boundary:

    \bkvadrāts\b

## Formulas in the problem base

Formulas are stored as LaTeX inside the Markdown text of the problem, between dollar
signs. This is what the source of a real problem looks like:

<pre><code>Nogriežņa &#36;AB&#36; garums ir &#36;10~\mathrm{cm}&#36;. Uz tā kā uz hipotenūzas konstruēti
divi taisnleņķa trijstūri &#36;ABC&#36; un &#36;ABD&#36;.
</code></pre>

and this is a fragment of a solution:

<pre><code>Tās &#36;n&#36; pēc kārtas ņemtu locekļu summa ir
&#36;\frac{(a+a+n-1) \cdot n}{2}=\frac{(2 a+n-1) \cdot n}{2}&#36;.
</code></pre>

Your pattern is matched against exactly this text — the LaTeX markup, not the
formula as it is drawn on screen. So searching for a fraction means searching for
`\\frac`, and searching for a superscript means searching for `\^`.

## Examples with a mathematical meaning

Several of these formulas are worked out rather than asked about, so they occur only
in the solutions. If a search over the problem statements comes back empty, switch
the drop-down next to the search box to **In solutions** and try again — the
annotations below say which patterns need it.

**The square of a binomial**, such as `(a+b)^2` or `(2x-1)^{2}`. Parentheses with
something inside them, followed by a power of two:

    \([^()]+\)\^\{?2

**A cubic root**, `\sqrt[3]{...}`:

    \\sqrt\[3\]

**The sine of alpha, beta or gamma**, allowing for an optional space between the two
LaTeX commands (*in solutions*):

    \\sin *\\(alpha|beta|gamma)

**A fraction inside a fraction** — the numerator of one fraction opens another one
(*in solutions*):

    \\frac\{[^{}]*\\frac

**A system of equations**, written with a `cases` environment:

    \\begin\{cases\}

**A modular arithmetic problem**, with a congruence and a modulus (*in solutions*):

    \\equiv.*\\pmod

**A phrase that may be broken across a line.** In the Markdown source the sentences
are wrapped, so a space may in fact be a newline. `\s+` matches any run of
whitespace, including a line break:

    taisnleņķa\s+trijstūris

## What is and is not supported

The engine is the regular expression function of SPARQL 1.1. The everyday
constructs all work:

| Construct | Meaning |
|---|---|
| `.` | any single character |
| `*` `+` `?` | zero or more, one or more, optional |
| `{2,3}` | between two and three repetitions |
| `[abc]` `[^abc]` | one of these characters, any character except these |
| `[0-9]` `\d` `\w` `\s` | digit, letter or digit, whitespace |
| `^` <code>&#36;</code> `\b` | start of text, end of text, word boundary |
| `(?i)` | case insensitive — already the default here |

Alternation `(abc|def)` matches either side, as in the noun endings above.

Lookahead `(?=...)`, lookbehind `(?<=...)` and backreferences `\1` are **not**
supported. A pattern that uses them, or a pattern with a syntax error such as an
unclosed bracket, simply returns no results rather than an error message — so if a
complicated pattern gives you nothing, first check that it is well formed.

## Where it searches, and how many results

The drop-down next to the search box chooses what is searched:

* **In problems** — the problem statements only.
* **In solutions** — the problem statements **and** all of their solutions. Many
  formulas appear only in the solutions, so this is where a pattern such as
  `\\frac\{[^{}]*\\frac` really pays off.

At most **10** problems are returned, ordered by grade and then by problem
identifier. If you get exactly 10 results, there are probably more.
