# prog-validate — HTTPS izvietošana (atsevišķs ASGI process + Nginx)

Mērķis: `https://eliozo.dudajevagatve.lv/mcp/` apkalpo īsto MCP `streamable-http`
protokolu (claude.ai *custom connector*), **neaiztiekot** esošo Flask/Gunicorn
izvietojumu.

## Kāpēc atsevišķs process

Flask lietotne ir **WSGI** (sinhrona, `wsgi:handler` zem Gunicorn). MCP
`streamable-http` galapunkts ir **ASGI** (Starlette + Server-Sent Events) — to
nevar apkalpot no sinhrona WSGI procesa. Tāpēc MCP serviss darbojas kā patstāvīgs
uvicorn process uz `127.0.0.1:8001`, un Nginx to reverse-proxy pārsūta `/mcp/`.

```
claude.ai ──HTTPS──> Nginx ──/eliozo──> Gunicorn (WSGI)  Flask     [nemainīts]
                          └──/mcp────> uvicorn  (ASGI)  asgi:app  [jauns process]
```

## Soļi

1. **Atkarības** tajā pašā virtualenv, ko lieto Flask:
   ```bash
   <venv>/bin/pip install -r requirements.txt uvicorn
   ```
   (`requirements.txt` dod `mcp`, `PyYAML`, `pytest`; `uvicorn` ir ASGI serveris.)

2. **Uzbūvē indeksu** (mape `index/` ir `.gitignore`d — to ģenerē uz vietas):
   ```bash
   cd <deploy>/mcp/prog-validate && <venv>/bin/python build_index.py
   ```
   Tas pats ir konsekvences tests (kļūda, ja programmā citēts kods nav standartā).

3. **systemd serviss** — `deploy/prog-validate.service` (izlabo ceļus tajā):
   ```bash
   sudo cp deploy/prog-validate.service /etc/systemd/system/
   sudo systemctl daemon-reload && sudo systemctl enable --now prog-validate
   sudo systemctl status prog-validate
   ```

4. **Nginx** — iekopē `deploy/nginx-mcp.conf` location blokus esošajā
   `server { server_name eliozo.dudajevagatve.lv; … }` blokā (tajā pašā, kas jau
   proxy `/eliozo`), tad:
   ```bash
   sudo nginx -t && sudo systemctl reload nginx
   ```

## Pārbaude pēc izvietošanas

```bash
# REST (lokāli uz servera):
curl -s http://127.0.0.1:8001/api/v1/temati | head -c 200

# MCP handshake caur publisko HTTPS:
curl -s -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"t","version":"1"}}}'
# Sagaidāms: event: message … "serverInfo":{"name":"prog-validate", …}
```

claude.ai pusē: **Settings → Connectors → Add custom connector**, URL
`https://eliozo.dudajevagatve.lv/mcp`. Rīki `get_sr_matrix` un `list_temati`
parādās pēc pievienošanas.

## Atjaunināšana

Pēc jauna deploy (dati/kods mainīti): `sudo systemctl restart prog-validate`
(unit `ExecStartPre` pārbūvē indeksu). Flask serviss jārestartē atsevišķi, kā
līdz šim — tie ir neatkarīgi.
