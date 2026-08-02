# prog-validate — MCP serviss

Rīki `list_programs`, `list_temati` un `get_sr_matrix`
(SPEC v0.1, sk. `prompts/prog_validate_get_sr_matrix_SPEC.md`).

Serviss savieno trīs dokumentu slāņus: valsts standartus, mācību programmas un
OL mācību materiālus. **Mape ir pašpietiekama** — visi avota dati ir `data/`, un
kods neatsaucas ne uz vienu failu ārpus šīs mapes. To var pārvietot uz atsevišķu
repozitoriju bez izmaiņām.

## Uzstādīšana

```bash
pip install -r requirements.txt
python build_index.py            # ģenerē index/*.json no data/
python build_index.py --strikti  # nezināms citētais kods = būves kļūda
```

`build_index.py` vienlaikus ir konsekvences tests: tas pārbauda, ka neviens
pamatskolas standarta kods nav pazudis parsējot, un ka katrs programmā citētais
standarta kods eksistē. Nezināmi citētie kodi nonāk programmas laukā
`nezinamie_kodi` (redzams `list_programs` atbildē) un tiek izdrukāti kā
brīdinājumi — ar `--strikti` būve tādā gadījumā krīt.

### `index/standarts.json` uzbūve

Indekss aptver **abus** standartus. Rinda = viens sasniedzamais rezultāts visās
tā kolonnās; kolonnu ass atšķiras pa izglītības pakāpēm:

| `izglitibas_pakape` | Avots | Šūnu lauki | `klasu_grupas` |
|---|---|---|---|
| `vidusskola` | `data/vidusskolas_standarts.md` | `visparigais` / `optimalais` / `augstakais` (apguves līmeņi, kodi `M.V/O/A.…`) | `["10-12"]` |
| `pamatskola` | `data/pamatskolas_standarts.md` | `klases_1_3` / `klases_4_6` / `klases_7_9` (klašu grupas, kodi `M.3/6/9.…`) | tikai tās, kurās rindā ir SR |

Pamatskolā apguves līmeņu nav — 1.–9. klasē visi apgūst to pašu. To vietā
standarts pie tā paša temata atgriežas trīs reizes ar pieaugošu detalizāciju
("spirāles" uzbūve), un tieši tāpēc **rinda tiek glabāta nesadalīta**: blakus
esošās šūnas ir viena temata pakāpieni, un tukša šūna nozīmē, ka attiecīgajā
klašu grupā šī temata vēl/vairs nav. Rindas id ir `PSK.<sadaļa>.<kārtas nr>`
(piem., `PSK.1.1.3`), jo kodu numerācija starp kolonnām nesakrīt.

Papildus rindām fails satur plakanu `kodu_indekss` (kods → `klasu_grupa`,
`beidzot_klasi`/`limenis`, `rinda_id`, `lauks`, `liela_ideja`, `sadala`, `tips`)
un `klasu_grupas` katalogu. Tas ir tiešais atbalsts `new_tools.md` rīkiem, kuriem
no `TopicId` uzreiz jāzina `GradeBand` (`classify_content_level`,
`search_taxonomy`, `check_prerequisites`); caur `rinda_id` no jebkura koda var
atgriezties pie rindas un atrast pārējos spirāles pakāpienus.

## Mācību programmas

Visi programmu faili dzīvo mapē `data/curricula/` un tiek atrasti **pēc faila
nosaukuma**:

```
program_<program_id>[_<loma>].<md|json|csv>

<program_id> ::= <valsts>.<izdevejs>.<kurss-vai-macibu-gads>[.<grupa>]
<loma>       ::= papildu tabula pie tās pašas programmas (piem. concepts)
```

| Fails | Programma |
|---|---|
| `program_lv.skola2030.mat1.md` | Matemātika I (optimālais līmenis, 10.–12. kl.) |
| `program_lv.skola2030.mat2.md` | Matemātika II (augstākais līmenis, 10.–12. kl.) |
| `program_lv.skola2030.mat1-9.md` | Matemātika 1.–9. klasei |
| `program_lv.avg.2025-26.7a.json` | Āgenskalna Valsts ģimnāzijas 7.a stundu plāns |
| `program_lv.avg.2025-26.7a_concepts.csv` | tā paša plāna jēdzienu tabula |

Divi programmu **tipi**: `paraugs` (Skola2030 paraugi — temati ar SR blokiem un
citētiem standarta kodiem) un `stundu_plans` (reāli skolas plāni — temati ar
kalendāru, pārbaudes darbiem un ievesto jēdzienu sarakstu, bez SR blokiem).
Paralēlās klases (7.a/8.a/9.a) ir **atsevišķas programmas**, jo tās mācīja
dažādi skolotāji pēc savas tematu secības; vienā skolas gadā tās sasaista lauks
`kopa` (`lv.avg.2025-26`), ko var lietot arī kā filtru.

Jaunu stundu plānu pievieno, vienkārši iekopējot failu ar pareizu nosaukumu —
konfigurācija nav vajadzīga. `data/curricula/programmas.yaml` glabā tikai to, ko
no paša faila nolasīt nevar: Markdown paraugiem — metadatus un **parsētāja
profilu** (`avotina_html` pandoc `<table>` tabulām, `avotina_grid` grid tabulām,
`avotina_grid_1_9` — grid tabulas ar `A7.1.`/`G9.5.` tematu marķieriem), JSON
plāniem — iestādi un kopu. Parsētāju pievieno `programmas.py` vārdnīcā
`PARSETAJI`.

`index/programmas.json` satur visas programmas normalizētā formā: metadati,
temati (`temats_id` = `<program_id>#T<nr>`), SR bloki un citētie kodi.

## Palaišana

```bash
python server.py                                     # stdio (Claude Desktop / Claude Code)
python server.py --transport streamable-http --port 8000
```

HTTP režīmā papildus MCP galapunktam `/mcp` ir REST atkļūdošanas maršruti:

```
GET /api/v1/programmas?tips=paraugs&klase=7
GET /api/v1/temati?programma=lv.skola2030.mat2&klasu_grupa=10-12
GET /api/v1/sr-matrix/12?limeni=V,O,A&parklajums=true&programma=lv.skola2030.mat1
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
| `data/` | avota faili: standarti, OL materiāli, `curricula/` programmas |
| `data/curricula/programmas.yaml` | programmu reģistrs (nosaukumu shēma, metadati, parsētāju profili) |
| `build_index.py` | parsē avotus → `index/standarts.json`, `index/programmas.json` |
| `programmas.py` | programmu atrašana, parsētāji, normalizēšana |
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
- Standartu parsēšana pieņem pipe-tabulas; programmām lieto gan pandoc HTML
  (`<table>`), gan grid (`+---+---+`) tabulas — abas `data/` failos sastopamas.
- Matemātikā I ir **22 temati** (ne 13, kā minēts SPEC 2.1. sadaļā); OL materiāli
  šobrīd pieejami 12 no tiem un tikai šai programmai, tāpēc `get_sr_matrix`
  pārklājumu rēķina tikai tur.
- Avotu dokumentu nepilnības, ko parsētājs neizlabo: 1.–9. klases paraugā divi
  temati numurēti `3.6.` (tāpēc `temats_id` veido kārtas numurs, ne marķieris),
  plānojuma tabulā minētajiem `A7.5.` un `G7.2.` nav detalizētas sadaļas, un
  temats `6.5.` atsaucas uz kodu `M.6.4.3.3.`, kāda standartā nav (sk.
  `nezinamie_kodi`).
- Stundu plānu temati nesatur standarta SR blokus — `get_sr_matrix` tiem atgriež
  metadatus, kalendāru un ievestos jēdzienus ar attiecīgu brīdinājumu.
