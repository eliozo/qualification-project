# sparqljs.min.js

Browser build of [SPARQL.js](https://github.com/RubenVerborgh/SPARQL.js)
3.7.3 with its dependency rdf-data-factory 1.1.3 (both MIT licensed). The
Advanced search page (`templates/advanced_search_content.html`) uses its
parser to point at syntax errors before a query is sent to the server. It
defines the global `SparqlJs` (`new SparqlJs.Parser().parse(query)`).

Rebuild (in an empty directory, Node.js 18 or newer):

    npm install --ignore-scripts sparqljs@3.7.3 esbuild@0.25.9
    echo 'module.exports = require("sparqljs");' > entry.js
    npx esbuild entry.js --bundle --minify --platform=browser --format=iife \
        --global-name=SparqlJs --legal-comments=none --outfile=sparqljs.min.js
