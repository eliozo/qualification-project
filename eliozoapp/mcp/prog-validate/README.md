# prog-validate — MCP serviss

Rīki `get_sr_matrix` un `list_temati` (SPEC v0.1, sk. `prompts/prog_validate_get_sr_matrix_SPEC.md`).

Serviss savieno trīs dokumentu slāņus: valsts standartu, programmas paraugu un
OL mācību materiālus. **Mape ir pašpietiekama** — visi avota dati ir `data/`, un
kods neatsaucas ne uz vienu failu ārpus šīs mapes. To var pārvietot uz atsevišķu
repozitoriju bez izmaiņām.

## Uzstādīšana

```bash
pip install -r requirements.txt
python build_index.py            # ģenerē index/*.json no data/
```

`build_index.py` vienlaikus ir konsekvences tests: ja kāds programmā citēts
`M.O.*` kods neeksistē standartā, būvēšana beidzas ar kļūdu sarakstu.

## Palaišana

```bash
python server.py                                     # stdio (Claude Desktop / Claude Code)
python server.py --transport streamable-http --port 8000
```

HTTP režīmā papildus MCP galapunktam `/mcp` ir REST atkļūdošanas maršruti:

```
GET /api/v1/temati
GET /api/v1/sr-matrix/12?limeni=V,O,A&parklajums=true
```

### HTTPS izvietošana (ASGI process aiz Nginx)

Produkcijā MCP galapunktu apkalpo `asgi.py` (module-level `app`, Starlette/ASGI)
zem uvicorn — atsevišķs process no Flask/Gunicorn, ko Nginx proxy pārsūta `/mcp/`:

```bash
python -m uvicorn asgi:app --host 127.0.0.1 --port 8001
```

Pilna instrukcija (systemd unit + Nginx snippets): **`deploy/DEPLOY.md`**.

### Claude Desktop / Claude Code konfigurācija (stdio)

```json
{
  "mcpServers": {
    "prog-validate": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "<šīs mapes absolūtais ceļš>"
    }
  }
}
```

Ceļus var pārdefinēt ar `PROG_VALIDATE_DATA` un `PROG_VALIDATE_INDEX`.

## Testi

```bash
python -m pytest tests/ -q
```

Testi paši pārbūvē indeksu pagaidu mapē, tāpēc tie nav atkarīgi no `index/` stāvokļa.
Sedz SPEC 7. sadaļas T1–T8 plus pārklājuma slāņa un kļūdu apstrādes pārbaudes.

## Faili

| Fails | Nozīme |
|---|---|
| `data/` | avota `.md` faili (standarts, programmas paraugs, OL materiāli) |
| `build_index.py` | parsē avotus → `index/standarts.json`, `programma.json`, `temati.json` |
| `server.py` | FastMCP serveris (`stdio` / `streamable-http`) + REST maršruti |
| `coverage.py` | pārklājuma heiristikas (leksiskā sakritība) |
| `coverage_overrides.yaml` | manuālas korekcijas pa programmas SR `id` |
| `tests/test_sr_matrix.py` | akcepttesti |

## Zināmie ierobežojumi (v1)

- **Pārklājums ir leksisks, nevis semantisks.** `coverage.py` salīdzina SR teksta
  saturvārdu celmus ar materiālu sadaļām. Tas šķiro pareizajā virzienā (temata
  paša SR → `pilns`, sveši SR → `tikai_pieminets`/`nav_atrasts`), bet ir trokšņains:
  sveši SR reti nokrīt līdz `nav_atrasts`, jo sakrīt vispārīgā matemātikas leksika.
  **Rezultāti ir caurskates sākumpunkts, nevis spriedums** — apstrīdamos gadījumus
  fiksē `coverage_overrides.yaml`. Semantiskā (embedding) meklēšana ir v2 tvērumā.
- `limena_bridinajumi` izmanto to pašu leksisko heiristiku un praksē ir konservatīvi
  (tematam 12 — 0 brīdinājumu).
- Standarta parsēšana pieņem pipe-tabulas, programmas parauga — pandoc HTML tabulas
  (`<table>`), kā tās faktiski ir `data/` failos. SPEC minētās grid-tabulas
  (`+---+---+`) šajos avotos nesastopamas.
- Programmas paraugā ir **22 temati** (ne 13, kā minēts SPEC 2.1. sadaļā); OL
  materiāli šobrīd pieejami 12 no tiem.
