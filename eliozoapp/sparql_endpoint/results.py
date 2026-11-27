"""Serializers for SELECT and ASK results, and for graphs.

pyoxigraph can serialize a whole result set, but the endpoint returns at
most ``max_rows`` rows and must know whether there were more before it sends
the headers. So the rows are collected first and written by the functions
below, which follow the W3C formats:

* JSON  https://www.w3.org/TR/sparql11-results-json/
* XML   https://www.w3.org/TR/rdf-sparql-XMLres/
* CSV and TSV  https://www.w3.org/TR/sparql11-results-csv-tsv/

Triple terms (RDF 1.2 / RDF-star) are written as the JSON ``triple`` type and
the XML ``<triple>`` element, as Oxigraph and Jena do.
"""

import csv
import io
import json
from xml.sax.saxutils import escape, quoteattr

from pyoxigraph import BlankNode, Literal, NamedNode, Triple, serialize

XSD_STRING = 'http://www.w3.org/2001/XMLSchema#string'
RDF_LANG_STRING = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'
RDF_DIR_LANG_STRING = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#dirLangString'

# Prefixes for Turtle / RDF/XML output, to make it readable.
PREFIXES = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    'eliozo': 'http://www.dudajevagatve.lv/eliozo#',
}


def _direction(literal):
    d = getattr(literal, 'direction', None)
    if d is None:
        return None
    return str(getattr(d, 'value', d)).lower().rsplit('.', 1)[-1]


def _plain_datatype(literal):
    """The datatype IRI to write, or None for simple and language-tagged literals."""
    dt = literal.datatype.value
    return None if dt in (XSD_STRING, RDF_LANG_STRING, RDF_DIR_LANG_STRING) else dt


# --- JSON -------------------------------------------------------------------

def json_term(term):
    if isinstance(term, NamedNode):
        return {'type': 'uri', 'value': term.value}
    if isinstance(term, BlankNode):
        return {'type': 'bnode', 'value': term.value}
    if isinstance(term, Literal):
        out = {'type': 'literal', 'value': term.value}
        if term.language:
            out['xml:lang'] = term.language
            if _direction(term):
                out['its:dir'] = _direction(term)
        elif _plain_datatype(term):
            out['datatype'] = _plain_datatype(term)
        return out
    if isinstance(term, Triple):
        return {'type': 'triple', 'value': {
            'subject': json_term(term.subject),
            'predicate': json_term(term.predicate),
            'object': json_term(term.object)}}
    raise TypeError(f'unexpected term {term!r}')


def select_json(variables, rows):
    bindings = [{v: json_term(t) for v, t in zip(variables, row) if t is not None}
                for row in rows]
    return json.dumps({'head': {'vars': variables}, 'results': {'bindings': bindings}},
                      ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def ask_json(value):
    return json.dumps({'head': {}, 'boolean': bool(value)}, separators=(',', ':')).encode('utf-8')


# --- XML --------------------------------------------------------------------

_XML_HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n'
             '<sparql xmlns="http://www.w3.org/2005/sparql-results#">\n')


def _xml_term(term):
    if isinstance(term, NamedNode):
        return f'<uri>{escape(term.value)}</uri>'
    if isinstance(term, BlankNode):
        return f'<bnode>{escape(term.value)}</bnode>'
    if isinstance(term, Literal):
        if term.language:
            return f'<literal xml:lang={quoteattr(term.language)}>{escape(term.value)}</literal>'
        dt = _plain_datatype(term)
        if dt:
            return f'<literal datatype={quoteattr(dt)}>{escape(term.value)}</literal>'
        return f'<literal>{escape(term.value)}</literal>'
    if isinstance(term, Triple):
        return ('<triple>'
                f'<subject>{_xml_term(term.subject)}</subject>'
                f'<predicate>{_xml_term(term.predicate)}</predicate>'
                f'<object>{_xml_term(term.object)}</object>'
                '</triple>')
    raise TypeError(f'unexpected term {term!r}')


def select_xml(variables, rows):
    out = [_XML_HEAD, '<head>']
    out += [f'<variable name={quoteattr(v)}/>' for v in variables]
    out.append('</head>\n<results>\n')
    for row in rows:
        out.append('<result>')
        for v, t in zip(variables, row):
            if t is not None:
                out.append(f'<binding name={quoteattr(v)}>{_xml_term(t)}</binding>')
        out.append('</result>\n')
    out.append('</results>\n</sparql>\n')
    return ''.join(out).encode('utf-8')


def ask_xml(value):
    return (_XML_HEAD + '<head/>\n<boolean>' + ('true' if value else 'false')
            + '</boolean>\n</sparql>\n').encode('utf-8')


# --- CSV and TSV ------------------------------------------------------------

def _csv_value(term):
    if term is None:
        return ''
    if isinstance(term, BlankNode):
        return '_:' + term.value
    if isinstance(term, (NamedNode, Literal)):
        return term.value
    return nt_term(term)


def select_csv(variables, rows):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator='\r\n')
    writer.writerow(variables)
    for row in rows:
        writer.writerow([_csv_value(t) for t in row])
    return buf.getvalue().encode('utf-8')


_NT_ESCAPES = str.maketrans({'\\': '\\\\', '"': '\\"', '\n': '\\n', '\r': '\\r', '\t': '\\t'})


def nt_term(term):
    """A term in N-Triples syntax, with tabs and newlines escaped (for TSV)."""
    if isinstance(term, NamedNode):
        return f'<{term.value}>'
    if isinstance(term, BlankNode):
        return '_:' + term.value
    if isinstance(term, Literal):
        text = '"' + term.value.translate(_NT_ESCAPES) + '"'
        if term.language:
            d = _direction(term)
            return text + '@' + term.language + ('--' + d if d else '')
        dt = _plain_datatype(term)
        return text + (f'^^<{dt}>' if dt else '')
    if isinstance(term, Triple):
        return (f'<<( {nt_term(term.subject)} {nt_term(term.predicate)} '
                f'{nt_term(term.object)} )>>')
    raise TypeError(f'unexpected term {term!r}')


def select_tsv(variables, rows):
    lines = ['\t'.join('?' + v for v in variables)]
    lines += ['\t'.join('' if t is None else nt_term(t) for t in row) for row in rows]
    return ('\n'.join(lines) + '\n').encode('utf-8')


def ask_text(value):
    """ASK as CSV/TSV (not defined by the W3C note; same shape as Jena)."""
    return ('_askResult\n' + ('true' if value else 'false') + '\n').encode('utf-8')


SELECT_WRITERS = {'json': select_json, 'xml': select_xml, 'csv': select_csv, 'tsv': select_tsv}
ASK_WRITERS = {'json': ask_json, 'xml': ask_xml, 'csv': ask_text, 'tsv': ask_text}


def graph_bytes(triples, rdf_format, prefixes=None):
    """Serialize a list of pyoxigraph Triples in the given ``RdfFormat``."""
    return serialize(triples, format=rdf_format, prefixes=prefixes or PREFIXES)
