"""Read-only SPARQL 1.1 Protocol endpoint over the Eliozo Oxigraph store.

A small WSGI application, separate from the Flask site, served by its own
Gunicorn (systemd unit ``eliozo-sparql``) and published by Nginx at
``https://eliozo.dudajevagatve.lv/sparql``. See ``README.md`` in this
directory and ``eliozo-setup/REQUEST022-sparql-endpoint.md``.

Modules:

* ``config``      -- settings (limits, paths) read from environment variables
* ``store``       -- read-only store handle that follows data reloads
* ``protocol``    -- request parsing, query checks, content negotiation
* ``results``     -- SPARQL results serializers (JSON, XML, CSV, TSV)
* ``description`` -- SPARQL Service Description and VoID
* ``app``         -- the WSGI application (``sparql_endpoint.app:application``)
"""
