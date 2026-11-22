# Par paplašināto meklēšanu

Lapā [Paplašinātā meklēšana](/advanced_search) uzdevumus var atlasīt ar
SPARQL vaicājumiem tieši no Eliozo RDF grafa. Grafa jēdzieni (formulējumi un
atrisinājumi, klasifikatori, hierarhijas un vārdu konvencijas) aprakstīti lapā
[Ievads ontoloģijā](/ontology); šeit apkopots, kas vajadzīgs vaicājumu rakstīšanai.

## Vārdtelpas

Visi turpmāk lietotie nosaukumi pieder divām vārdtelpām: prefikss `eliozo:` apzīmē
skolas sacensību matemātikai raksturīgus resursu tipus, īpašības un to vērtības;
`skos:` — attiecības klasifikatoru hierarhijās (piemēram, temats "kvadrātfunkcija"
ir šaurāks nekā temats "algebra"). Ar šīm prefiksu definīcijām sākas tipisks vaicājums:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Uzdevuma virsotne

| Īpašība | Vērtība | Piemērs |
|---|---|---|
| `eliozo:problemID` | teksts | `"LV.AMO.2019.7.4"` |
| `eliozo:problemText` | Markdown, viens katram tulkojumam, ar valodas birku | `"Andris apgalvo, ..."@lv` |
| `eliozo:problemTextHtml` | tas pats teksts HTML formā | |
| `eliozo:olympiad` | olimpiādes ID | `"LV.AMO"` |
| `eliozo:olympiadCode`, `eliozo:country` | šī ID daļas | `"AMO"`, `"LV"` |
| `eliozo:event` | viena olimpiādes kārta | `"LV.AMO.2019"` |
| `eliozo:problemYear`, `eliozo:problemGrade` | veseli skaitļi | `2019`, `7` |
| `eliozo:suggestedGrade` | vesels skaitlis, var atkārtoties | `7` |
| `eliozo:olympiadType` | teksts | `"National"`, `"RegionalOrOpen"`, `"TeamSelection"`, `"International"`, `"Contest"`, `"Book"` |
| `eliozo:domain` | nozare (žanra augšējais līmenis) | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | žanrs | `eliozo:DOM_GridCut` |
| `eliozo:topic` | temats | `eliozo:Divisibility` |
| `eliozo:method` | metode | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | jēdziens | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | jautājuma tips | `"QTY_FindAll"` |
| `eliozo:problemSolution` | atrisinājuma virsotne | |
| `eliozo:hasVideo` | video virsotne | |
| `eliozo:answer` | īsā atbilde | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | radniecīgu vai identisku uzdevumu ID | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | grāmatu uzdevumiem | `"BBK2012"`, `"P1"` |

Ne katram uzdevumam ir visas īpašības: daudziem uzdevumiem vēl nav temata, metodes
vai jēdzienu.

**Atrisinājumiem** (`eliozo:Solution`) ir `eliozo:solutionText` (Markdown ar valodas
birku), `eliozo:solutionTextHtml` un `eliozo:solutionNum`. **Video**
(`eliozo:Video`) ir `eliozo:videoTitle`, `eliozo:videoYoutube` un
`eliozo:videoBookmarks` — `eliozo:VideoBookmark` virsotņu saraksts ar
`eliozo:videoBookmarkTstamp` (sekundes) un `eliozo:videoBookmarkText`.

## Automātiski ieteiktās birkas

Īpašības, kuru nosaukums sākas ar pasvītru, ir ieteicis valodas modelis, un tās nav
pārbaudītas. To vērtības ir vienkāršs teksts, nevis klasifikatoru virsotnes:

| Īpašība | Vērtību piemēri |
|---|---|
| `eliozo:_hasSolutionConcept` | `"DivisibilityRelation"`, `"Invariant"`, `"LatticeGrid"` |
| `eliozo:_hasReasoningMethod` | `"ConstructiveExampleForExistence"`, `"CaseAnalysis"` |
| `eliozo:_hasReasoningMistake` | `"FromSpecialToGeneral"` |
| `eliozo:_readingDifficulty` | `"low"`, `"medium"`, `"high"` |
| `eliozo:_mistakesFit` | `"low"`, `"medium"`, `"high"` |

Tās aptver daudz vairāk uzdevumu nekā pārbaudītie klasifikatori, tāpēc der kandidātu
meklēšanai, taču rezultāti jāpārbauda.

## Vaicājumu rakstīšana

* Klasifikatora virsotni raksta kā nosaukumu: `?p eliozo:topic eliozo:Divisibility`.
  Teksta vērtības raksta pēdiņās: `?p eliozo:domain "NT"`.
* Lai atrastu visu, kas atrodas zem kādas hierarhijas virsotnes, izmanto īpašību
  ceļu: `?t skos:broader* eliozo:Divisibility` atbilst gan pašam `Divisibility`, gan
  katrai virsotnei zem tā.
* Īpašībām, kuru uzdevumam var nebūt, lieto `OPTIONAL { ... }`.
* Tekstiem ir valodas birkas. Lai lietotu tikai latvisko tekstu:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Paplašinātā meklēšana parāda `?problemID` vērtības; `?section` un `?subsection`
  tās sagrupē zem apakšvirsrakstiem.

## Piemēri

Katra saite atver paplašināto meklēšanu un uzreiz izpilda vaicājumu; to var tur
rediģēt un palaist vēlreiz. Visi šie vaicājumi ir arī izvēlnē
"Sagatavotie vaicājumi > Ontoloģija" virs vaicājuma lauka, bet citi piemēri — tās
pašas izvēlnes punktos "Piemēri", "Uzdevumu tipi" un "Teorijas temati".

* 5.–7. klases uzdevumi par dalāmību (temats `Divisibility` un viss zem tā),
  sagrupēti pa tematiem: [atvērt vaicājumu](/advanced_search?queryLabel=onto-divisibility-grades-5-7).
* [Temati](/content/ontology_topics):
  [kongruences](/advanced_search?queryLabel=onto-topic-congruence),
  [uzdevumi ar tematu, bet bez metodes](/advanced_search?queryLabel=onto-topic-without-method).
* [Metodes](/content/ontology_methods):
  [invarianti pēc veida](/advanced_search?queryLabel=onto-method-invariants),
  [indukcija 9.–12. klasei](/advanced_search?queryLabel=onto-method-induction).
* [Žanri](/content/ontology_genres):
  [rūtiņu režģi pēc klasēm](/advanced_search?queryLabel=onto-genre-grid-by-grade),
  [rūtiņu režģi pēc tēmas](/advanced_search?queryLabel=grid-problems),
  [ģeometrijas žanri](/advanced_search?queryLabel=onto-genre-geometry).
* [Jautājumu tipi](/content/ontology_question_types):
  ["atrast visus" skaitļu teorijā](/advanced_search?queryLabel=onto-qtype-find-all-nt),
  [grupa "atrast" pēc tipa](/advanced_search?queryLabel=onto-qtype-find-group),
  [izvēles atbildes ar "atrast lielāko"](/advanced_search?queryLabel=onto-qtype-find-optimal-choice).
* [Jēdzieni](/content/ontology_concepts):
  [dalāmība un pirmskaitļi](/advanced_search?queryLabel=onto-concept-divisibility-primes),
  [uzdevumi pēc jēdziena](/advanced_search?queryLabel=onto-concept-by-term),
  [ieteiktais jēdziens "Invariant"](/advanced_search?queryLabel=onto-concept-suggested-invariant).
* [Olimpiādes](/content/ontology_olympiads):
  [AMO 5. klase kopš 2020. gada](/advanced_search?queryLabel=onto-olympiad-amo-grade-5),
  [valsts olimpiāžu ģeometrija](/advanced_search?queryLabel=onto-olympiad-national-geometry).

## No kurienes nāk dati

Klasifikatori tiek uzturēti Eliozo metadatu izklājlapās un eksportēti Turtle failos
(`worksheet-generation-with-llms/scripts/setup/resources`); uzdevumi tiek konvertēti
no uzdevumu repozitoriju Markdown failiem. Uzdevumiem birkas piešķir to Markdown
avotā, piemēram, `* topic:Divisibility`.
