# MCP servisi — pārbaude un pieslēgšana

Šajā mapē ir MCP (Model Context Protocol) servisi. Šobrīd viens:

| Serviss | Galapunkts | Mape |
|---|---|---|
| `prog-validate` | `https://eliozo.dudajevagatve.lv/mcp` | [`prog-validate/`](prog-validate/) |

Izvietošanas apraksts: [`prog-validate/deploy/DEPLOY.md`](prog-validate/deploy/DEPLOY.md).

---

## 1. Autentifikācijas pārbaude (authless)

Serviss ir **bez autentifikācijas** (authless). claude.ai *custom connector*
pievienošana bez OAuth strādā tikai tad, ja izpildās visi trīs nosacījumi:

1. neautentificēts `POST /mcp` atbild ar **200** (nevis 401/403);
2. atbildēs **nav** `WWW-Authenticate` galvenes;
3. OAuth metadatu ceļi (`/.well-known/oauth-*`) atbild ar **404**.

### 1.1. Neautentificēts MCP handshake → 200

```bash
curl -sS -D - -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1.0"}}}'
```

Sagaidāms: `HTTP/1.1 200 OK`, `Content-Type: text/event-stream`, galvene
`mcp-session-id: <hex>` un `"serverInfo":{"name":"prog-validate", …}`.

### 1.2. Pilna sesija bez akreditācijas datiem

```bash
SID=$(curl -sS -D - -o /dev/null -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1.0"}}}' \
  | grep -i '^mcp-session-id' | tr -d '\r' | awk '{print $2}')

curl -sS -o /dev/null -w "initialized: %{http_code}\n" -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SID" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'          # sagaidāms 202

curl -sS -X POST https://eliozo.dudajevagatve.lv/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'                   # sagaidāms 200 + rīku saraksts
```

### 1.3. `WWW-Authenticate` galvenes nav

```bash
curl -sSI https://eliozo.dudajevagatve.lv/mcp | grep -i www-authenticate || echo "OK: nav WWW-Authenticate"
```

### 1.4. OAuth metadati netiek pasniegti → 404

```bash
for p in /.well-known/oauth-protected-resource \
         /.well-known/oauth-authorization-server \
         /.well-known/oauth-protected-resource/mcp \
         /.well-known/oauth-authorization-server/mcp \
         /.well-known/openid-configuration \
         /register; do
  printf '%s  %s\n' "$(curl -sS -o /dev/null -w '%{http_code}' https://eliozo.dudajevagatve.lv$p)" "$p"
done
```

Visiem jābūt `404`. Ja kāds atbild ar `200`, klients uzskatīs servisu par
OAuth-aizsargātu un pieprasīs pieteikšanos.

### 1.5. Kas **nav** autentifikācijas problēma

Šīs atbildes ir MCP `streamable-http` protokola normāla uzvedība, nevis auth:

| Pieprasījums | Atbilde | Nozīme |
|---|---|---|
| `GET /mcp` bez `mcp-session-id` | `400` `Bad Request: Missing session ID` | protokols prasa vispirms `initialize` ar POST |
| `GET /mcp` ar derīgu `mcp-session-id` | `200`, atvērta SSE straume | pareizi |
| `HEAD /mcp` | `405 Method Not Allowed` | HEAD netiek atbalstīts |
| `GET /mcp/` (ar slīpsvītru) | `307` → `/mcp` | klienti seko pāradresācijai |

Kritiskā atšķirība: **401 nekad neparādās** un `WWW-Authenticate` nekad netiek
sūtīts. Tikai tas nosaka, vai klients sāks OAuth plūsmu.

### 1.6. Pārbaudes rezultāts (2026-08-01)

| Pārbaude | Rezultāts |
|---|---|
| `POST /mcp` `initialize` bez auth | **200** ✅ (`prog-validate` v1.28.1) |
| `notifications/initialized` | **202** ✅ |
| `tools/list` bez auth | **200** ✅ (`list_temati`, `get_sr_matrix`) |
| `GET /mcp` ar sesijas ID | **200**, SSE straume ✅ |
| `WWW-Authenticate` galvene | nav nevienā ceļā ✅ |
| `/.well-known/oauth-*`, `/register` | visi **404** ✅ |

Secinājums: `prog-validate` ir pilnībā authless un derīgs pievienošanai
claude.ai kā *custom connector* bez OAuth.

> **Drošības piezīme.** Authless nozīmē, ka rīkus var izsaukt jebkurš, kas zina
> URL. Tas ir pieņemami, jo serviss ir tikai lasošs un atgriež publiskus mācību
> satura dokumentus. Ja kādreiz tiek pievienots rīks ar blakusefektiem vai
> nepubliskiem datiem, šis lēmums jāpārskata.

---

## 2. Pieslēgšana Claude tīmekļa lietotnē (Claude Pro)

Attālinātie MCP servisi claude.ai pieslēdzas kā **custom connector**. Nepieciešams
Pro (vai Max / Team / Enterprise) abonements.

1. Atver [claude.ai](https://claude.ai) → **Settings** → **Connectors**.
2. Spied **Add custom connector** (lapas apakšā, sadaļā *Custom connectors*).
3. **Name:** `prog-validate`
   **Remote MCP server URL:** `https://eliozo.dudajevagatve.lv/mcp`
   – URL **bez** slīpsvītras beigās (ar slīpsvītru seko 307 pāradresācija, ko ne
   visi klienti apstrādā).
   – OAuth Client ID / Secret laukus **atstāj tukšus** — serviss ir authless.
4. Spied **Add**. Sarakstā jāparādās `prog-validate` ar statusu *Connected*.
   Ja Claude pieprasa pieteikšanos vai rāda auth kļūdu, atkārto 1. sadaļas
   pārbaudes — kaut kas galapunktā sūta 401 vai OAuth metadatus.
5. Jaunā sarunā spied rīku/spraudņa ikonu ievades laukā un pārliecinies, ka
   `prog-validate` ir ieslēgts un rāda abus rīkus.

### 2.1. Dūmu tests sarunā

Uzdod Claude šos jautājumus — katrs izsauc citu rīku:

```
Izmanto prog-validate rīku list_temati un parādi visus tematus tabulā.
```
Sagaidāms: 22 temati; 12 no tiem ar pieejamiem OL materiāliem.

```
Izmanto prog-validate un parādi 12. temata SR matricu tikai optimālajam līmenim.
```
Sagaidāms: `get_sr_matrix` izsaukums ar `temats=12`, `limeni=["O"]`; atbildē
temata metadati, programmas SR bloki, standarta kodu rindas un pārklājums.

Claude pirms katra izsaukuma prasa apstiprinājumu; var atzīmēt *Allow always*.

### 2.2. Ja savienojums neizdodas

| Simptoms | Pārbaude |
|---|---|
| *Could not connect* | `sudo systemctl status prog-validate` uz servera; `curl -s http://127.0.0.1:8001/api/v1/temati \| head -c 200` |
| Prasa pieteikšanos / OAuth | 1.3. un 1.4. pārbaude — kaut kas sūta 401 vai OAuth metadatus |
| Savienots, bet rīku nav | `tools/list` (1.2.) — vai serveris tos vispār deklarē |
| Ilgi karājas un atmet | Nginx buferizācija: `proxy_buffering off` un `proxy_read_timeout 3600s` `/mcp` blokā (sk. `deploy/nginx-mcp.conf`) |

Servera žurnāli: `sudo journalctl -u prog-validate -f` un
`sudo tail -f /var/log/nginx/error.log`.

---

## 3. Pieslēgšana Claude Code / Claude Desktop

**Attālināti (HTTP), tas pats galapunkts:**

```bash
claude mcp add --transport http prog-validate https://eliozo.dudajevagatve.lv/mcp
claude mcp list        # jāparāda "Connected"
```

**Lokāli (stdio), izstrādei bez izvietošanas** — sk.
[`prog-validate/README.md`](prog-validate/README.md) 45. rindu (`mcpServers`
konfigurācija ar `python server.py`).
