#!/usr/bin/env python3
"""ASGI ieejas punkts `prog-validate` MCP servisam (HTTPS izvietošanai).

Šis modulis atklāj module-level objektu `app` — Starlette (ASGI) lietotni, ko
var palaist ar uvicorn vai gunicorn (ar uvicorn worker):

    uvicorn asgi:app --host 127.0.0.1 --port 8001
    gunicorn -k uvicorn.workers.UvicornWorker --bind 127.0.0.1:8001 asgi:app

Lietotne apkalpo:
    /mcp            – MCP `streamable-http` protokols (claude.ai custom connector)
    /api/v1/temati            – REST atkļūdošana
    /api/v1/sr-matrix/{temats} – REST atkļūdošana

Nginx reverse-proxy pārsūta `https://<host>/mcp/` → šo procesu (sk. deploy/).

Ceļus var pārdefinēt ar env `PROG_VALIDATE_DATA` / `PROG_VALIDATE_INDEX`
(noklusējums: šīs mapes ./data un ./index).
"""

from __future__ import annotations

import server

# REST atkļūdošanas maršrutus reģistrē PIRMS ASGI lietotnes būvēšanas.
server._pievieno_rest_marsrutus()

# Starlette (ASGI) lietotne ar MCP streamable-http galapunktu /mcp + REST maršrutiem.
app = server.mcp.streamable_http_app()
