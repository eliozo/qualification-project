"""Gunicorn settings of the ``eliozo-sparql`` service.

Used as ``gunicorn -c sparql_endpoint/gunicorn_conf.py sparql_endpoint.app:application``.
Values come from the same environment as the application (``/etc/eliozo/sparql.env``):

    SPARQL_BIND       listen address (default unix:/run/eliozo-sparql/gunicorn.sock)
    SPARQL_WORKERS    worker processes = queries running at once (default 2)
    SPARQL_QUERY_TIMEOUT  see config.py; the hard limit below is 10 s more

Sync workers handle one request each. A query that is stuck inside the store
(e.g. sorting a huge cross product before the first row) cannot be stopped
from Python, so the hard limit is Gunicorn's worker ``timeout``: the arbiter
kills a worker that has not reported back for that long and starts a new
one. Nginx then answers 502, which it turns into a 503 "query timed out or
service restarting" message (see the Nginx snippet in eliozo-setup).
"""

import os

bind = os.environ.get('SPARQL_BIND', 'unix:/run/eliozo-sparql/gunicorn.sock')
workers = int(os.environ.get('SPARQL_WORKERS', '2'))
worker_class = 'sync'
timeout = int(float(os.environ.get('SPARQL_QUERY_TIMEOUT', '20'))) + 10
graceful_timeout = 10
max_requests = 2000            # recycle workers now and then (memory)
max_requests_jitter = 200
umask = 0o007                  # socket: rw for the service user and group (www-data)
accesslog = None               # Nginx keeps the access log; the app logs each query
errorlog = '-'                 # stderr -> journald
loglevel = 'info'
proc_name = 'eliozo-sparql'
control_socket_disable = True  # Gunicorn >= 25.1 control socket: not needed here
