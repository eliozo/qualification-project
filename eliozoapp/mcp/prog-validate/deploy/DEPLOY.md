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

## Uz `eliozo.dudajevagatve.lv` to nedara ar rokām

Šis fails apraksta soļus **principā** (un derēs uz jauna hosta). Uz esošā servera
tie ir iesaiņoti divos skriptos, kurus lieto to vietā:

| Kad | Ko palaist |
|---|---|
| Pirmreizēji / pēc venv pārbūves / ja kaut kas salūzis | `sudo python3 eliozo-setup/scripts/setup-mcp-prog-validate.py` (idempotents; `--check`, `--dry-run`) |
| Kārtējā koda vai `data/` izmaiņa | Jenkins pipeline **`deploy_mcp`** (vai `deploy_eliozo` ar `DEPLOY_MCP=true`) |

Pirmais skripts nolasa dzīvos ceļus no `eliozo-gunicorn.service` unit faila, tāpēc
tas vienmēr trāpa tajā kokā, ko Gunicorn reāli apkalpo. Sk. `eliozo-setup/
ADMIN-GUIDE.md` sadaļu "MCP Service (`prog-validate`)".

## Soļi

1. **Atkarības** tajā pašā virtualenv, ko lieto Flask:
   ```bash
   <venv>/bin/pip install -r requirements.txt
   ```
   (`mcp`, `PyYAML`, `uvicorn`, `pytest`.)

2. **Uzbūvē indeksu** (mape `index/` ir `.gitignore`d — to ģenerē uz vietas):
   ```bash
   cd <app_dir>/mcp/prog-validate && <venv>/bin/python build_index.py
   ```
   Tas pats ir konsekvences tests (kļūda, ja programmā citēts kods nav standartā).
   Būve aizņem <1 s, tāpēc to atkārto katrā servisa startā (`ExecStartPre`).

3. **systemd serviss** — `deploy/prog-validate.service` (izlabo ceļus tajā):
   ```bash
   sudo cp deploy/prog-validate.service /etc/systemd/system/
   sudo systemctl daemon-reload && sudo systemctl enable --now prog-validate
   sudo systemctl status prog-validate
   ```
   `User=` jābūt tam lietotājam, kam **pieder** izvietojuma koks (šeit `eliozo`),
   jo `ExecStartPre` raksta `index/`. `www-data` nepietiek.

4. **Nginx** — iekopē `deploy/nginx-mcp.conf` location blokus esošajā
   `server { server_name eliozo.dudajevagatve.lv; … }` blokā (tajā pašā, kas jau
   proxy Flask lietotni uz `/`), tad:
   ```bash
   sudo nginx -t && sudo systemctl reload nginx
   ```

### Konkrētās vērtības uz šī hosta (pārbaudīts 2026-08-03)

| Elements | Vērtība |
|---|---|
| `<app_dir>` | `/home/eliozo/workspace/qualification-project/eliozoapp` |
| `<venv>` | `/home/eliozo/workspace/qualification-project/venv-eliozo` |
| Servisa lietotājs | `eliozo:www-data` |
| Upstream | `127.0.0.1:8001` (tikai loopback) |
| Nginx sait | `/etc/nginx/sites-available/eliozo`, marķieris `# --- prog-validate MCP (REQUEST013) ---` |

## Pārbaude pēc izvietošanas

```bash
# REST (lokāli uz servera):
curl -s http://127.0.0.1:8001/api/v1/programmas | head -c 200
curl -s "http://127.0.0.1:8001/api/v1/temati?programma=visas" | head -c 200

# MCP handshake caur publisko HTTPS:
curl -s -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"t","version":"1"}}}'
# Sagaidāms: event: message … "serverInfo":{"name":"prog-validate", …}
```

claude.ai pusē: **Settings → Connectors → Add custom connector**, URL
`https://eliozo.dudajevagatve.lv/mcp`. Rīki `list_programs`, `list_temati` un
`get_sr_matrix` parādās pēc pievienošanas.

## Atjaunināšana

Pēc jauna deploy (dati/kods mainīti): `sudo systemctl restart prog-validate`
(unit `ExecStartPre` pārbūvē indeksu). Flask serviss jārestartē atsevišķi, kā
līdz šim — tie ir neatkarīgi.

Automatizēti to dara Jenkins pipeline **`deploy_mcp`**
(`worksheet-generation-with-llms/Jenkins/deploy_mcp.groovy`), kas izsauc root
palīgu `/usr/local/bin/deploy-mcp`. Svarīgi, ko tas dara papildus rsync'am:

- `--exclude 'index/'`, lai `--delete` nenoņemtu uz servera ģenerēto indeksu
  (pretējā gadījumā starp rsync un restartu ir logs, kurā serviss ir bez indeksa);
- `--chown=eliozo:www-data` + `chown -R`, jo rsync kā root citādi atstāj failus
  `jenkins` īpašumā un `build_index.py` (kas strādā kā `eliozo`) nevar rakstīt
  `index/`;
- `pip install -r prog-validate/requirements.txt` — MCP atkarības **nav**
  `eliozoapp/requirements.txt`;
- `systemctl restart prog-validate` + handshake dūmu tests.

`deploy_eliozo` pipeline rsync'o visu `eliozoapp/` (arī `mcp/`), tāpēc tas
**nevar** MCP servisu atstāt mierā — pēc tā izpildes dzīvais serviss citādi
turpina strādāt ar veco kodu. Tāpēc tam ir `DEPLOY_MCP` parametrs (pēc
noklusējuma `true`), kas izsauc to pašu palīgu.
