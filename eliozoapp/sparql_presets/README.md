# Preset queries of the Advanced search page

The "Advanced search" page (`/advanced_search`) runs a SPARQL query typed by
the user. The menu above its query field preloads ready-made queries; this
directory defines that menu. Edit the files, no restart needed: they are
read again on every page load.

## Files

Every `*.yaml` file is one top-level menu entry. Files are shown in the
order of their names, hence the number prefixes (`10_examples.yaml`,
`20_problemtypes.yaml`, ...).

```yaml
title: {lv: "Fakultatīvs 7.-8. klasei", en: "Elective course, grades 7-8", lt: "Fakultatyvas 7-8 klasėms"}
items:
  - title: {lv: "Invarianti", en: "Invariants", lt: "Invariantai"}
    label: invariants            # optional: name for canned links
    query: |
      PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
      SELECT ?problemID ...
  - title: "AMO"                 # a submenu: "items" instead of "query"
    items:
      - title: ...
        query: |
          ...
```

* `title` is either one text or a `{lv, en, lt}` mapping; a missing
  language falls back to `lv`, then to any given one.
* An entry has either `query` (a menu item) or `items` (a submenu), which
  may be nested to any depth.
* `label` (optional, but give one to every query) names the query in a
  short link that opens the page and runs it at once:
  `/advanced_search?queryLabel=invariants`. Lowercase letters, digits and
  hyphens; unique across all files (a test checks this). The label takes
  precedence over a `query` parameter in the same URL. In the preset menu
  the items link to these URLs, so "Copy link" on a menu item gives the
  canned link, and a page opened by label shows its link under the form.
* Write the query as a YAML block (`query: |`, then the query indented
  below it); then no characters need escaping.

## What a query must return

* `?problemID` (required): the problem IDs to list, e.g. `"LV.AMO.2011.5.1"`.
* `?section` (optional): problems are grouped under one subtitle per value.
* `?subsection` (optional): a second level of subtitles within a section.

Variable names are case-insensitive; other selected variables are ignored.
Only `SELECT` queries are run, `SERVICE` is refused, at most 100 results
are shown and a query is stopped after 10 seconds.

The `matf*` presets are the `problems.rq` files of `nms-courses/docs`, with
their grouping variable (`?families` or `?family`) renamed to `?section`.
