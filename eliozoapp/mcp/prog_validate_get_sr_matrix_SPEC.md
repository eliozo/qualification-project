# Specifikācija: MCP serviss `prog-validate`, rīks `get_sr_matrix`

**Mērķauditorija:** Claude Code kodēšanas aģents, kas ģenerē Python failus un HTTP saskarni.
**Versija:** 0.1 (v1 tvērums — viena funkcija `get_sr_matrix` + palīgfunkcija `list_temati`).

---

## 1. Konteksts un datu modelis (trīs slāņi)

Serviss savieno trīs dokumentu slāņus, kas projektā pastāv kā Markdown faili (pandoc konvertācija no Word):

| Slānis | Fails | Vienība | Identifikators |
|---|---|---|---|
| 1. Valsts standarts | `vidusskolas_standarts.md` | SR trīs apguves līmeņos | `M.V.x.y.z.` / `M.O.x.y.z.` / `M.A.x.y.z.` |
| 2. Programmas paraugs | `MATEMATIKA_1_programmas_paraugs_19_maijs.md` | **Temats** (1.–13.) → SR bloki → programmas SR rindas | temata nr.; bloka virsraksts |
| 3. Mācību materiāli | `OL_<nr>__*_metodiskais.md`, `OL_<nr>_dl_*`, `OL_<nr>_fvd_*`, `OL_<nr>_npd*`, `OL_<nr>_kopsavilkums*` | stundu plānojums, stundu apraksti, darba lapas, vērtēšanas darbi | faila prefikss `OL_<nr>` |

**Svarīgi terminoloģiski:** jēdziens **"temats" standartā neeksistē** — standarts ir strukturēts pa lielajām idejām (`## VSK.M.Li.1.` … `## VSK.M.Li.6.`) un sadaļām (`### x.y. <nosaukums>`). Temats ir **programmas parauga** vienība. Saistību starp tematu un standartu definē programmas paraugs: katra temata SR bloka virsrakstā ir citēti standarta kodi, piem.:

```
**Taisnes vienādojums** (M.O.1.2.3., M.O.6.2.4., M.O.6.2.5., M.O.6.2.6.)
```

Tā kā Matemātika I ir optimālā līmeņa kurss, programma citē tikai `M.O.*` kodus; serviss katram citētajam `M.O.` kodam pievieno visu standarta **rindu** (V/O/A tripletu) — sk. 3. sadaļu.

### 1.1. Standarta faila uzbūve (parsēšanai)

- Virsraksti: `## VSK.M.Li.<N>. <lielās idejas teksts>` un `### <x>.<y>. <sadaļas nosaukums>`.
- Katrā sadaļā viena pipe-tabula ar 3 kolonnām: `Vispārīgais apguves līmenis | Optimālais apguves līmenis | Augstākais apguves līmenis`.
- Katra šūna sākas ar kodu (`M.V.6.2.4. <teksts>`). Šūna var būt **tukša** (piem., rindām ar kodiem `M.O.6.2.5.`, `M.O.6.2.6.`, `M.O.6.2.7.`, `M.O.4.5.6.` V un A šūnas ir tukšas) vai saturēt **divus kodus**, atdalītus ar `<br><br>` (piem., `M.A.1.2.4.` un `M.A.1.2.5.` vienā šūnā).
- Kontrolskaitlis: failā kopā ir **212 unikāli kodi**.

### 1.2. Programmas parauga uzbūve (parsēšanai)

- Temata virsraksts: `**<nr>. <NOSAUKUMS LIELAJIEM BURTIEM>** (<stundu skaits> stundas)` — piem., `**12. LĪNIJAS VIENĀDOJUMS, NEVIENĀDĪBAS AR DIVIEM MAINĪGAJIEM** (20 stundas)`. Aiz tā seko rindkopas `**Temata apguves mērķis:**` un `**Jēdzieni:**`.
- Temata SR doti pandoc **grid-tabulā** (`+---+---+`), kur bloku virsraksti ir rindas formā `**<bloka nosaukums>** (<kodu saraksts>)`, un zem katra bloka ir programmas SR rindas ar divām aizpildītām kolonnām: „Sasniedzamais rezultāts" un „Piemēri un skaidrojumi".
- ⚠️ Grid-tabulās teksts ir aplauzts pa vairākām fiziskām rindām — parseris vispirms jāsaliek šūnas kopā (rekomendācija: `pandoc -f markdown -t json` vai rindu apvienošana pēc `+---+` atdalītājiem), tikai tad jāizvelk saturs.

---

## 2. Rīka saskarne (MCP tool)

### 2.1. `get_sr_matrix` — ieejas shēma

```json
{
  "name": "get_sr_matrix",
  "description": "Atgriež programmas parauga temata SR matricu: temata metadatus, programmas SR blokus, citēto standarta kodu pilnās rindas (visi trīs apguves līmeņi) un (pēc izvēles) pārklājumu OL materiālos.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "temats": {
        "description": "Programmas parauga temata identifikators: vesels skaitlis (1..13) vai OL faila prefikss ('OL_12').",
        "oneOf": [
          { "type": "integer", "minimum": 1 },
          { "type": "string", "pattern": "^OL_[0-9]{1,2}$" }
        ]
      },
      "limeni": {
        "description": "Kurus apguves līmeņus iekļaut standarta matricā. Noklusējums — visi trīs.",
        "type": "array",
        "items": { "enum": ["V", "O", "A"] },
        "default": ["V", "O", "A"]
      },
      "ieklaut_parklajumu": {
        "description": "Vai aprēķināt pārklājumu OL_<nr> materiālos (dārgāka operācija; ja false, atgriež tikai standarta+programmas slāņus).",
        "type": "boolean",
        "default": true
      }
    },
    "required": ["temats"]
  }
}
```

### 2.2. `list_temati` — palīgrīks bez parametriem

Atgriež visu programmas paraugā atrasto tematu sarakstu `[{nr, nosaukums, stundas, ol_prefikss, materiali_pieejami: bool}]`. Nepieciešams gan lietotājam, gan kļūdu ziņojumiem (sk. 6. sadaļu).

---

## 3. Atgriežamās vērtības shēma

Atbilde ir viens JSON objekts ar četrām daļām. **Atbilde uz projektā uzdoto jautājumu: jā — `standarta_matrica` satur visu trīs apguves līmeņu kodus un pilnos tekstus** (ar `null` tur, kur standarta tabulā šūna ir tukša). Programma citē tikai `M.O.*`, bet V un A kolonnas ir vajadzīgas divu iemeslu dēļ: (1) caurskatē jāpārbauda, vai materiāla saturs nepārsniedz optimālo līmeni (padziļinājums jāmarķē „Nav standarta SR", un bieži tas faktiski atbilst kādam `M.A.*` kodam); (2) tukšās V šūnas parāda, kuri SR optimālajā līmenī ir „jauni" salīdzinājumā ar vispārīgo.

```jsonc
{
  "temats": {
    "nr": 12,
    "ol_prefikss": "OL_12",
    "nosaukums": "Līnijas vienādojums, nevienādības ar diviem mainīgajiem",
    "stundas": 20,
    "kurss": "Matemātika I",
    "apguves_limenis": "optimālais",
    "merkis": "…",              // no programmas parauga
    "jedzieni": ["taisnes vienādojums", "taisnes virziena koeficients", "…"]
  },

  // 2. slānis: programmas parauga SR bloki ar pārklājumu 3. slānī
  "programmas_sr_bloki": [
    {
      "bloks": "Taisnes vienādojums",
      "citetie_kodi": ["M.O.1.2.3.", "M.O.6.2.4.", "M.O.6.2.5.", "M.O.6.2.6."],
      "programmas_sr": [
        {
          "id": "12.B2.SR5",                          // temats.bloks.kārtas nr — servisa ģenerēts
          "teksts": "Izvēlas taisnes uzdošanas veidu un to lieto, lai noteiktu figūru veidu, pamatotu to īpašības.",
          "piemeri_skaidrojumi": null,
          "parklajums": {
            "statuss": "nav_atrasts",                 // enum: pilns | dalejs | tikai_pieminets | nav_atrasts
            "vietas": [],
            "komentars": "Nav ne plānojuma tabulā, ne stundu aprakstos, ne darba lapās."
          }
        },
        {
          "id": "12.B2.SR6",
          "teksts": "Formulē saistību starp taisni, kas uzdota ar vispārīgo vienādojumu Ax+By+C=0, un vektoru, kura koordinātas ir (A;B), lieto to figūru īpašību noteikšanai.",
          "piemeri_skaidrojumi": "Taisne Ax+By+C=0 ir perpendikulāra vektoram n=(A;B). Vektoru n sauc par taisnes normālvektoru.",
          "parklajums": {
            "statuss": "tikai_pieminets",
            "vietas": [
              { "fails": "OL_12__linija_metodiskais.md", "sadala": "6.–8. stunda",
                "fragments": "Šī pieraksta forma ļau[j] noteikt taisnei perpendikulāra vektora … koordinātas n=(A;B)." }
            ],
            "komentars": "Definīcija ir; lietojums figūru īpašību noteikšanai nav."
          }
        }
      ]
    }
    // … pārējie bloki: "Vienādojums ar diviem nezināmajiem", "Riņķa līnijas vienādojums",
    //   "Nevienādības un to sistēmas ar diviem mainīgajiem"
  ],

  // 1. slānis: citēto kodu pilnās standarta rindas (V/O/A tripleti)
  "standarta_matrica": [
    {
      "rinda_id": "6.2.4",
      "liela_ideja": { "kods": "VSK.M.Li.6.", "nosaukums": "Figūru īpašību, novietojuma, to raksturojošo lielumu izpēte …" },
      "sadala": { "nr": "6.2.", "nosaukums": "Analītiskā ģeometrija" },
      "visparigais": {
        "kods": "M.V.6.2.4.",
        "teksts": "Attēlo koordinātu plaknē taisni, ja tā uzdota analītiski, t. sk. ja tā paralēla ordinātu asij, un vienkāršās situācijās nosaka taisnes virziena koeficientu un uzraksta taisnes vienādojumu pēc tās attēla koordinātu plaknē, lieto taisnes atklāto vienādojumu, vienādojumu ar virziena koeficientu."
      },
      "optimalais": {
        "kods": "M.O.6.2.4.",
        "teksts": "Attēlo koordinātu plaknē taisni, ja tā uzdota analītiski, un uzraksta taisnes vienādojumu pēc tās attēla koordinātu plaknē, t. sk. ja tā paralēla ordinātu asij, lieto taisnes atklāto vienādojumu, vienādojumu ar virziena koeficientu, vienādojumu caur diviem punktiem, vispārīgo vienādojumu, pāriet no viena veida uz citu; izvēlas taisnes uzdošanas veidu un to lieto, lai noteiktu figūru veidu, pamatotu to īpašības."
      },
      "augstakais": {
        "kods": "M.A.6.2.4.",
        "teksts": "Nosaka analītiski uzdotas sakarības, piemēram, x²−y²=1, punktu ģeometrisko vietu un otrādi – veido, pārbauda līniju vienādojumus pēc to attēlojumiem koordinātu plaknē."
      },
      "tips": "satura"          // Li.3–Li.6 = "satura"; Li.1, Li.2 = "caurviju"
    },
    {
      "rinda_id": "6.2.5",
      "liela_ideja": { "kods": "VSK.M.Li.6.", "nosaukums": "…" },
      "sadala": { "nr": "6.2.", "nosaukums": "Analītiskā ģeometrija" },
      "visparigais": null,      // standarta tabulā šūna ir tukša
      "optimalais": {
        "kods": "M.O.6.2.5.",
        "teksts": "Formulē un lieto sakarības starp koeficientiem paralēlu un perpendikulāru taisņu vienādojumos."
      },
      "augstakais": null,
      "tips": "satura"
    },
    {
      "rinda_id": "4.5.6",
      "liela_ideja": { "kods": "VSK.M.Li.4.", "nosaukums": "Sakarības starp lielumiem apraksta algebriskie modeļi un funkcijas …" },
      "sadala": { "nr": "4.5.", "nosaukums": "Vienādojumi, nevienādības, to sistēmas" },
      "visparigais": null,
      "optimalais": {
        "kods": "M.O.4.5.6.",
        "teksts": "Atrisina vienādojumus, nevienādības (pakāpe nepārsniedz otro) un to sistēmas ar diviem mainīgajiem reālo skaitļu kopā, attēlojot atrisinājumu koordinātu plaknē."
      },
      "augstakais": {
        "kods": "M.A.4.5.6.",
        "teksts": "Atrisina dažāda veida vienādojumus, to sistēmas un nevienādības ar parametru."
      },
      "tips": "satura"
    }
    // … pārējās rindas: 1.2.3 (caurviju), 2.1.1 (caurviju), 4.5.1, 6.2.6, 6.2.7
  ],

  // 3. slāņa kopsavilkums + līmeņa pārbaudes brīdinājumi
  "parklajuma_kopsavilkums": {
    "programmas_sr_kopa": 12,
    "pilns": 8, "dalejs": 2, "tikai_pieminets": 1, "nav_atrasts": 1,
    "limena_bridinajumi": [
      {
        "vieta": { "fails": "OL_12__linija_metodiskais.md", "sadala": "Paralēlas un perpendikulāras taisnes" },
        "fragments": "darba lapa \"Attālums no punkta līdz taisnei plaknē\"",
        "atbilst_kodam": "M.A.6.2.3.",
        "komentars": "Saturs atbilst augstākajam apguves līmenim — jāpārbauda, vai materiālā tas marķēts kā 'Nav standarta SR'."
      }
    ]
  }
}
```

**Piezīmes shēmai.**
- Ja `limeni` nesatur `V`/`A`, attiecīgie lauki no `standarta_matrica` ierakstiem tiek izlaisti (ne `null`, bet vispār nav — mazāks konteksta patēriņš MCP klientam).
- Šūna ar diviem kodiem (piem., `M.A.1.2.4.` + `M.A.1.2.5.`) → lauka vērtība ir **masīvs** ar diviem `{kods, teksts}` objektiem. Shēmā: `"augstakais": {objekts} | [{objekts}, …] | null`.
- `tips: "caurviju"` (Li.1 — matemātikas valoda, Li.2 — problēmrisināšana) kodiem pārklājuma statusu v1 versijā **nerēķina** (atgriež `"statuss": "nav_piemerojams"`) — tie caurvij visus tematus un nav pārbaudāmi ar leksisku meklēšanu.
- Pārklājuma noteikšana v1: leksiska (atslēgvārdu/frāžu sakritība starp programmas SR tekstu un OL failiem) + manuāls pārrakstīšanas fails `coverage_overrides.yaml` (atslēga = programmas SR `id`). Semantiskā (embedding) meklēšana — v2, ārpus šī tvēruma.

---

## 4. Darbības piemērs (end-to-end)

**MCP izsaukums** (Claude puse):

```json
{ "method": "tools/call",
  "params": { "name": "get_sr_matrix",
              "arguments": { "temats": "OL_12", "limeni": ["V","O","A"], "ieklaut_parklajumu": true } } }
```

**Sagaidāmā atbilde:** 3. sadaļas JSON ar šādiem kontrolpunktiem tematam 12:
- `temats.stundas == 20`; nosaukums sākas ar „Līnijas vienādojums";
- `programmas_sr_bloki` satur 4 blokus šādā secībā: „Vienādojums ar diviem nezināmajiem", „Taisnes vienādojums", „Riņķa līnijas vienādojums", „Nevienādības un to sistēmas ar diviem mainīgajiem";
- unikālo citēto kodu kopa (8 kodi): `M.O.1.2.3., M.O.2.1.1., M.O.4.5.1., M.O.4.5.6., M.O.6.2.4., M.O.6.2.5., M.O.6.2.6., M.O.6.2.7.`;
- `standarta_matrica` satur 8 rindas; rindām `6.2.5`, `6.2.6`, `6.2.7`, `4.5.6` lauks `visparigais` ir `null` (un `6.2.5`, `6.2.6`, `6.2.7` arī `augstakais` ir `null`);
- rindas `1.2.3` un `2.1.1` ir ar `tips: "caurviju"`.

**HTTP atkļūdošanas izsaukums** (tas pats saturs bez MCP aploksnes):

```
GET /api/v1/sr-matrix/12?limeni=V,O,A&parklajums=true
GET /api/v1/temati
```

---

## 5. Arhitektūra un failu izkārtojums

```
prog-validate/
├── data/                      # avota .md faili (kopijas; ceļš konfigurējams ar env PROG_VALIDATE_DATA)
├── index/
│   ├── standarts.json         # build_index rezultāts: visas 212 kodu rindas
│   ├── programma.json         # temati → bloki → programmas SR → citētie kodi
│   └── temati.json            # temata nr ↔ OL prefikss ↔ pieejamie materiālu faili
├── build_index.py             # vienreizēja/atkārtojama indeksēšana (CLI: python build_index.py --data ./data)
├── server.py                  # FastMCP serveris + REST atkļūdošanas maršruti
├── coverage.py                # pārklājuma heiristikas (leksiskā sakritība)
├── coverage_overrides.yaml    # manuālās korekcijas pa programmas SR id
└── tests/test_sr_matrix.py
```

**Tehnoloģijas:** Python 3.11+, `mcp` pakotne (FastMCP), transports `streamable-http` (galapunkts `/mcp`), REST atkļūdošanai ar to pašu ASGI lietotni. Izvietošanai claude.ai kā *custom connector* nepieciešams publisks HTTPS; lokālai lietošanai Claude Desktop pietiek ar `stdio` transportu (abus atbalstīt ar `--transport` karodziņu).

**Parsēšanas noteikumi (minimums):**
- Standarts: sadaļu virsraksti `^###\s+(\d+)\.(\d+)\.\s+(.+)$`; kodu izvilkšana šūnās `M\.[VOA]\.\d+\.\d+\.\d+\.`; šūnas dalīšana pie `<br><br>`, ja tajā ir >1 kods.
- Programma: temata virsraksts `^\*\*(\d+)\.\s+([^*]+)\*\*\s*\((\d+)\s*stund`; bloka virsraksts grid-šūnā `\*\*(.+?)\*\*\s*\(\s*((?:M\.O\.\d+\.\d+\.\d+\.\s*,?\s*)+)\)`; grid-tabulu šūnas pirms tam jāsaliek kopā (ieteikums: `pandoc -t json`).
- Validācija būvēšanas laikā: katram programmā citētam kodam jāeksistē standartā; pretējā gadījumā `build_index.py` beidzas ar kļūdu sarakstu (tas pats par sevi ir noderīgs konsekvences tests!).

---

## 6. Kļūdu apstrāde

- Nezināms temats → MCP kļūda ar tekstu, kas satur pieejamo tematu sarakstu no `list_temati` (nr + nosaukums), lai klients var pārprasīt.
- Temats bez OL materiāliem (`materiali_pieejami: false`) un `ieklaut_parklajumu: true` → atgriež matricu ar `parklajuma_kopsavilkums: null` un brīdinājumu, nevis kļūdu.
- Indeksa faili trūkst → kļūda ar norādi palaist `build_index.py`.

---

## 7. Akcepttesti (pytest)

1. **T1 Standarta pilnīgums:** pēc `build_index.py` `standarts.json` satur tieši 212 unikālus kodus; katrs kods parādās tieši vienā rindā.
2. **T2 Tukšās šūnas:** rindai `6.2.5` `visparigais is None` un `augstakais is None`; `optimalais.kods == "M.O.6.2.5."`.
3. **T3 Daudzkodu šūna:** rindas `1.2.4` laukā `augstakais` ir saraksts ar kodiem `M.A.1.2.4.` un `M.A.1.2.5.`.
4. **T4 Temats 12:** `get_sr_matrix(12)` kontrolpunkti no 4. sadaļas (bloku skaits un secība, 8 unikālie kodi, stundu skaits 20).
5. **T5 Ekvivalence:** `get_sr_matrix(12)` un `get_sr_matrix("OL_12")` atgriež identisku rezultātu.
6. **T6 Līmeņu filtrs:** ar `limeni=["O"]` atbildes `standarta_matrica` ierakstos nav lauku `visparigais`/`augstakais`.
7. **T7 Kļūda:** `get_sr_matrix(99)` → kļūda, kuras tekstā ir vismaz 10 pieejamo tematu nosaukumi.
8. **T8 Citēto kodu eksistence:** neviens `programma.json` citētais kods nav ārpus `standarts.json` kopas.

---

## 8. Ārpus tvēruma (v2 idejas, nekodēt tagad)

Semantiskais pārklājums ar embeddings; `check_references`, `verify_math`, `lint_document` rīki; pamatskolas standarta (`pamatskolas_standarts.md`) integrācija priekšzināšanu pēctecības pārbaudei; jēdzienu reģistra (`EliozoMetadataSolutionConcept.csv`) sasaiste ar `temats.jedzieni`.
