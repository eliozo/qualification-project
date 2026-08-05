# "Math Level" MCP serviss — API specifikācija (v0.1)

MCP serviss, kas matemātikas satura vienībai (uzdevums, darba lapa, pierādījums, teorijas fragments) nosaka piemēroto klašu grupu, klasi vai — konkrētas mācību programmas kontekstā — mēnesi/mācību nedēļu, kā arī risina pretējo uzdevumu (kas dotā brīdī jau ir mācīts un kas ir "svaigs").

## 1. Dizaina principi

1. **Seši rīki, visi tikai lasoši.** Katram rīkam MCP anotācijas `readOnlyHint: true`, `idempotentHint: true` — droši LLM aģentiem (nav blakusefektu) un viegli testējami cilvēkiem (MCP Inspector, curl).
2. **LLM tikai vienā vietā.** Vienīgais rīks, kas izmanto valodas modeli, ir `extract_content_concepts` (caur MCP *sampling* — t.i., izsaucēja BYOK modeli; ja klients sampling neatbalsta, servera fallback modelis). Visi pārējie rīki ir deterministiskas tabulu operācijas — rezultāti reproducējami un regresiju testi triviāli.
3. **Divkārša ievade visur, kur klasificē.** Katrs klasifikācijas rīks pieņem *vai nu* `concept_labels` (ja izsaucējs jau pats veicis pirmsklasifikāciju ar savu LLM), *vai* `content` (neapstrādāts teksts — tad serveris iekšēji izsauc ekstrakciju). Ja padoti abi, `concept_labels` ņem virsroku (deterministiskais ceļš vienmēr lētāks un paredzamāks).
4. **Izskaidrojamība.** Katra klasifikācijas atbilde satur "kāpēc": kuri jēdzieni "pavelk" līmeni uz augšu (`limiting_concepts`) vai kuru trūkst (`missing`). LLM aģents to var tieši citēt lietotājam.
5. **Maigas kļūdas.** Nepazīstami identifikatori nerada izņēmumu — tie tiek atgriezti laukā `unknown_labels`, un klasifikācija notiek ar atlikušajiem. Tas atbilst LLM izsaucēju realitātei (reizēm halucinēti labels).
6. **Versijas.** Katra atbilde satur `taxonomy_version` (jēdzienu kataloga un standartu revīzija) un, ja piedalās programma, `program_revision`.

## 2. Identifikatori un koplietotie tipi

| Tips | Formāts | Avots |
|---|---|---|
| `ConceptLabel` | PascalCase, piem. `EvenOddParity`, `GCD` | `EliozoMetadataSolutionConcept.csv` kolonna `Label` |
| `TopicId` | Standarta SR kods (`M.9.1.1.1.`, `VSK.M.Li.2...`) vai programmas temata kods (`MAT1.T05`) | standartu .md faili, programmu paraugi |
| `ProgramId` | piem. `lv.g7.2025-26.planimetrija` | reģistrētie kalendārie plāni (kā `grade7_topics.csv`) |
| `GradeBand` | `"1-3" \| "4-6" \| "7-9" \| "10-12"` | pamatskolas/vidusskolas standarts |
| `VskLevel` | `"visparigais" \| "optimalais" \| "augstakais"` | vidusskolas standarts |
| `Domain` | `"NT" \| "Alg" \| "Geom" \| "Comb" \| ...` | jēdzienu kataloga kolonna `Domain` |

**`TimePoint`** — laika moments programmas ietvaros; tieši viens no laukiem:

```json
{ "date": "2026-02-10" }        // kalendāra datums
{ "school_week": 24 }            // mācību gada nedēļa (1..~36)
{ "month": 2 }                   // kalendāra mēnesis programmas gada ietvaros
```

## 3. Rīki (tools)

### 3.1. `list_programs`

Uzskaita servisā reģistrētās mācību programmas (kalendāros plānus). Sākumpunkts smalkajai (nedēļas/mēneša) klasifikācijai un atklājamībai — LLM aģents vispirms uzzina, kādi `program_id` vispār eksistē.

> **Ieviests** (`prog-validate/server.py`), ar atkāpēm no šeit plānotā:
> lauku nosaukumi ir latviski (kā pārējos rīkos), reģistrā līdzās kalendārajiem
> plāniem (`tips: "stundu_plans"`) ir arī programmu paraugi (`tips: "paraugs"`),
> kuriem nav ne `grade`, ne `span`, bet ir `klasu_grupas` un `apguves_limenis`.
> Paralēlās klases ir atsevišķas programmas, sasaistītas ar lauku `kopa`, un
> atbilde blakus `programmas` satur arī `kopas` sarakstu. Filtri: `tips`,
> `klase`, `klasu_grupa`, `macibu_gads`. Sk. `prog-validate/README.md`.

```ts
list_programs(input: {
  grade?: number,          // filtrs, piem. 7
  school_year?: string     // piem. "2025/2026"
}) => {
  programs: [{
    program_id: string,
    title: string,           // "7. klase, planimetrija, 2025/26"
    grade: number,
    school_year: string,
    span: { from: "2025-09-01", to: "2026-05-29" },
    source: string,          // faila/plāna izcelsme
    program_revision: string
  }],
  taxonomy_version: string
}
```

### 3.2. `search_taxonomy`

Brīva teksta (vai neprecīzu nosaukumu) pārvēršana kanoniskos identifikatoros. Determinisks (pilnteksta + fuzzy meklēšana pār `TitleLv`, `TitleEn`, `DescriptionLv`, standartu SR tekstiem), **nelieto LLM**. Kalpo arī kā batch-lookup: ja padots `ids`, atgriež tieši šos ierakstus ar pilnu aprakstu.

```ts
search_taxonomy(input: {
  query?: string,                  // "atlikumi pēc moduļa"
  ids?: string[],                  // precīza izgūšana pēc Label (alternatīva query)
  facet?: Facet | Facet[] | "any", // Facet = "concept" | "topic" | "model" | "method" | "genre" | "questionType"
  mode?: "lexical" | "semantic" | "hybrid",   // noklusēti "hybrid"
  domain?: Domain,                 // nākotnē caur šo varēs pārslēgt nozari
  max_earliest_grade?: number,        // tikai jēdzieni, ko sāk mācīt ≤ šai klasei (katram jēdzienam zināma noklusētā minimālā klase; ar šo atmetam "lielo klašu" rindas, ja vaicājumam tās nevajag)
  include_hierarchy?: boolean,     // L1..L5 vecāku ķēde
  include_examples?: number,       // 0..5 enkura uzdevumi katrai rindai
  limit?: number
}) => {
  matches: [{
    id: string, facet: Facet,
    title_lv, title_en?, description_lv?,
    parents?: [{ id, title_lv }],
    annotation_policy?: string,    // piem. "anotē apakštipu, ne virsmezglu" (questionTypes)
    curricular_status?, first_grade?, vsk_level?,
    anchor_examples?: [{ problem_id, statement_excerpt }],
    score: number,
    score_components?: { lexical?: number, semantic?: number }
  }],
  taxonomy_version, embedding_model_version?
}
```

*Kāpēc atsevišķs rīks:* gan cilvēkiem (kataloga pārlūkošana), gan LLM aģentiem, kas paši veikuši pirmsklasifikāciju "aptuveniem" nosaukumiem un pirms `classify_*` izsaukumiem grib tos kanonizēt.

### 3.3. `extract_content_concepts`

Satura vienība → taksonomijas jēdzieni un temati (prasība 5). **Vienīgais rīks ar LLM** — izmanto MCP sampling (izsaucēja modeli), rezultātu vienmēr validē pret taksonomiju: labels, kas katalogā neeksistē, tiek izmesti, nevis atgriezti.

```ts
extract_content_annotations(input: {
  statement: string,
  solution?: string,
  content_kind?: "problem" | "solution" | "theorem" | "explanation" | "worksheet" ,
  facets?: Facet[],                 // noklusēti visas piemērojamās
  allow_inferred_solution?: boolean, // atļaut "solve-then-classify" models/methods prognozei
  min_confidence?: number
}) => {
  annotations: {                    // confidence is a number in [0;1]
    concepts:  [{ label, confidence, basis, evidence }],
    topics:    [{ label, confidence, basis, evidence }],
    models:    [{ label, confidence, basis, evidence }],  // tukšs + piezīme, ja nav atrisinājuma
    methods:   [{ label, confidence, basis, evidence }],
    genre:     { label, confidence } | null,
    question_type: { label, confidence, rule_based: boolean } | null
  },
  needs_review: boolean,
  review_reasons: string[],          // "models bez atrisinājuma", "divi kandidāti ar tuvu score" ...
  nearest_classified_problems: [{ problem_id, similarity, shared_labels: string[] }],
  taxonomy_version, pipeline_version
}

```

*Piezīme izsaucējiem:* ja pirmsklasifikācija jau veikta pašu spēkiem, šo rīku var izlaist un `concept_labels` padot tieši 3.4.–3.6. rīkiem.

### 3.4. `classify_content_level`

Galvenais klasifikators (prasības 2 un 3). Bez `program_id` atgriež rupjo klasifikāciju (klašu grupa, minimālā klase, vidusskolas līmenis); ar `program_id` — arī agrāko kalendāro momentu, kad saturs kļūst skolēniem saprotams.

```ts
classify_content_level(input: {
  concept_labels?: ConceptLabel[],   // vismaz viens no concept_labels / content
  content?: string,                  // ja dots bez labels — iekšēji izsauc 3.3.
  program_id?: ProgramId             // ieslēdz smalko (nedēļas/mēneša) klasifikāciju
}) => {
  school_stage: "pamatskola" | "vidusskola",
  grade_band: GradeBand,             // "7-9" u.tml.
  min_grade: number,                 // agrākā klase, kurā VISI jēdzieni jau mācīti
  vsk_level?: VskLevel,              // tikai vidusskolas saturam
  limiting_concepts: [{              // izskaidrojamība: kas nosaka min_grade/līmeni
    label: ConceptLabel,
    title_lv: string,
    first_grade?: number,
    vsk_level?: VskLevel
  }],
  program_placement?: {              // tikai ja dots program_id
    earliest: { date: string, school_week: number, month: number },
    blocking_topics: [{ topic_id: TopicId, title: string, taught_at: TimePoint }]
  },
  unknown_labels: string[],
  taxonomy_version: string
}
```

*Semantika:* `min_grade = max(first_grade)` pār visiem jēdzieniem; `program_placement.earliest` = pēdējā (vēlākā) bloķējošā temata beigu datums plānā. Tā ir **apakšējā robeža saprotamībai** — API atbild "no kura brīža saturs ir saprotams", nevis "cik grūts tas ir" (grūtības kalibrēšana ir apzināti ārpus tvēruma, sk. §6).

### 3.5. `check_prerequisites`

Validators (prasības 3 lietojums): vai satura vienība ir izmantojama dotajā programmā dotajā brīdī. Tipiski — pārbaudes darba vai darba lapas validēšana: rezultāts derīgs, ja `ready = true` (neviena `missing` jēdziena).

```ts
check_prerequisites(input: {
  program_id: ProgramId,
  at: TimePoint,                        // plānotais izmantošanas brīdis
  concept_labels?: ConceptLabel[],
  content?: string,
  recent_window_weeks?: number          // "svaiguma" logs, noklusēti 4
}) => {
  ready: boolean,
  missing: [{                           // jēdzieni, kas VĒL NAV mācīti līdz `at`
    label: ConceptLabel,
    title_lv: string,
    first_taught: TimePoint | null      // null = šajā programmā vispār neparādās
  }],
  covered: ConceptLabel[],              // jau mācītie no pieprasītajiem
  fresh: [{                             // no covered — nesen aktualizētie
    label: ConceptLabel,
    last_seen: TimePoint,
    via: "taught" | "tested" | "homework"
  }],
  unknown_labels: string[],
  taxonomy_version: string,
  program_revision: string
}
```

### 3.6. `get_program_coverage`

Pretējais virziens (prasība 4): dots brīdis programmā → kas jau ir mācīts un kas ir aktuāls. Paredzēts olimpiādes vai pārbaudes darba **komplektēšanai** — atlasīt uzdevumus, kuru jēdzieni ir `covered`, ideālā gadījumā `recent`.

```ts
get_program_coverage(input: {
  program_id: ProgramId,
  at: TimePoint,                        // piem. { "month": 2 } — "februārī"
  recent_window_weeks?: number,         // noklusēti 4
  include_upcoming_weeks?: number       // noklusēti 0; >0 atgriež arī tuvāko plānu
}) => {
  current_topic: { topic_id: TopicId, title: string } | null,
  covered_topics: [{ topic_id, title, taught: { from: TimePoint, to: TimePoint } }],
  covered_concepts: ConceptLabel[],     // pilns apgūto jēdzienu saraksts uz `at`
  recent: {                             // "svaigais" saturs loga ietvaros
    taught: ConceptLabel[],
    tested: ConceptLabel[],
    homework: ConceptLabel[]
  },
  upcoming?: [{ topic_id, title, planned: TimePoint }],
  taxonomy_version: string,
  program_revision: string
}
```

## 4. MCP resursi un prompti

Statiskie avoti tiek publicēti kā **MCP resources** (tikai lasāmi), lai cilvēki un aģenti var pārlūkot izejmateriālus, nekonstruējot rīku izsaukumus:

| Resource URI | Saturs |
|---|---|
| `taxonomy://concepts` | pilns jēdzienu katalogs (JSON, ģenerēts no CSV) |
| `standards://pamatskola`, `standards://vidusskola` | standartu dokumenti |
| `programs://{program_id}/calendar` | konkrētās programmas kalendārais plāns |

Viens **MCP prompt** `classify-content-unit`: gatava prompta sagatave izsaucēja LLM pirmsklasifikācijai — satur aktuālo labels sarakstu ar īsiem aprakstiem un instrukciju atgriezt tikai kanoniskos identifikatorus. Tas standartizē BYOK ceļu, lai dažādi aģenti pirmsklasificē vienādi.

## 5. Tipiskās izsaukumu ķēdes

| Lietojums (prasība) | Izsaukumu secība |
|---|---|
| Uzdevums → jēdzienu saraksts (5) | `extract_content_concepts` |
| Uzdevums → klašu grupa/līmenis (2) | `classify_content_level(content)` *vai* pirmsklasifikācija ārpusē → `classify_content_level(concept_labels)` |
| Uzdevums → "8. klases novembris" (3) | `list_programs` → `classify_content_level(labels, program_id)` |
| Pārbaudes darba validēšana (3) | `extract_content_concepts` (par katru uzdevumu) → `check_prerequisites(program_id, at)`; darbs derīgs, ja visiem `ready = true` |
| Olimpiāde 7. klasei februārī (4) | `get_program_coverage(program_id, {month: 2})` → uzdevumu atlase, kuru jēdzieni ⊆ `covered_concepts`, priekšroku dodot `recent` |
| Nosaukuma kanonizācija | `search_taxonomy(query)` |

## 6. Apzināti ārpus tvēruma (v0.1)

Grūtības pakāpes vērtēšana (viens un tas pats jēdzienu kopums var dot gan rutīnas, gan olimpiādes līmeņa uzdevumu) — nākotnē paplašināms ar `difficulty` lauku ekstrakcijas atbildē. Rakstīšanas operācijas (jaunu programmu/jēdzienu reģistrācija) — v0.1 tās notiek datu slānī, nevis caur MCP, lai visi rīki paliek read-only. Vidusskolas jēdzienu pārklājums: pašreizējais katalogs ietver `Grade` līdz 9. klasei; `vsk_level` klasifikācijai katalogs jāpapildina ar vidusskolas jēdzieniem un to līmeņu piesaisti VSK SR kodiem — tas ir datu, nevis API jautājums (API forma jau to paredz).

