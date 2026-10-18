# Ontoloģija

Eliozo uzdevumu bāze glabājas kā RDF grafs. Katrs uzdevums ir klases
`eliozo:Problem` virsotne; tās īpašības norāda uz uzdevuma tekstiem, atrisinājumiem,
olimpiādi un **klasifikatoriem** (metadatiem), kas uzdevumu apraksta. Šī lapa ir šī
grafa karte tiem, kas raksta vaicājumus lapā
[Paplašinātā meklēšana](/advanced_search).

Visi turpmāk lietotie nosaukumi pieder divām vārdtelpām:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Klasifikatori

| Klasifikators | Ko tas apraksta | Uzdevuma īpašība | Vērtības | Pārlūkot |
|---|---|---|---|---|
| [Temati](/content/ontology_topics) | teoriju, ko izmanto atrisinājums | `eliozo:topic` | `eliozo:Topic` virsotnes | [pēc tēmas](/topics), [tēmu tabula](/topics_table) |
| [Metodes](/content/ontology_methods) | atrisinājuma spriedumu šablonu | `eliozo:method` | `eliozo:Method` virsotnes | [pēc metodes](/methods) |
| [Žanri](/content/ontology_genres) | kā uzdevums izskatās, tā "sižetu" | `eliozo:domain`, `eliozo:subdomain` | teksts; `eliozo:Domain` virsotnes | [pēc žanra](/genres) |
| [Jautājumu tipi](/content/ontology_question_types) | kāda veida atbilde prasīta | `eliozo:questionType` | teksts | [Filtri](/filter) |
| [Jēdzieni](/content/ontology_concepts) | jēdzienus uzdevuma formulējumā | `eliozo:concepts` | `eliozo:Concept` virsotnes | [pēc jēdziena](/concepts) |
| [Olimpiādes](/content/ontology_olympiads) | sacensības | `eliozo:olympiad` | teksts | [Olimpiādes](/olympiads) |
| [Modeļi](/content/ontology_models) | matemātisko struktūru, ko uzbūvē risinātājs | *plānots* | | |
| [Norāžu tipi](/content/ontology_hint_types) | heiristisko norāžu veidus | *plānots* | | |
| [Norādes](/content/ontology_hints) | viena uzdevuma norādes | *plānots* | | |

Kā klasifikatori saistīti savā starpā:

![Klasifikatoru attiecību grafs](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

Grafā ir divi slāņi. **Uzdevuma formulējuma slānis** (pa kreisi) ir redzams, uzdevumu
vēl nerisinot: tā *žanrs* (ārējā līdzība, sižets), *jēdzieni* nosacījumos un
*jautājuma tips* (prasītās atbildes struktūra). **Atrisinājuma slānis** (pa labi)
apraksta vienu konkrētu atrisinājumu: tā *tematu* (teoriju), *modeli* (matemātisko
struktūru, ko uzbūvē risinātājs; modelis ir tilts starp abiem slāņiem) un *metodi*
(spriedumu šablonu). Zem tiem *norāžu kāpnes* (hint ladder) atbalsta risinātāju un
iesaka modeļus un metodes.

Nepārtrauktās bultas ir strukturālas atsauces starp klasifikatoru tabulām,
svītrotās — tipiskas saistības ("skatīt arī"), punktētās — norādes risinātājam.
Ar `*` atzīmētās saites ir ierosinātas un vēl nav aizpildītas.

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
| `eliozo:domain` | žanrs, augšējais līmenis | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | žanrs | `eliozo:DOM_GridCut` |
| `eliozo:topic` | temats | `eliozo:Divisibility` |
| `eliozo:method` | metode | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | jēdziens | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | jautājuma tips | `"FindAll"` |
| `eliozo:problemSolution` | atrisinājuma virsotne | |
| `eliozo:hasVideo` | video virsotne | |
| `eliozo:answer` | īsā atbilde | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | radniecīgu vai identisku uzdevumu ID | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | grāmatu uzdevumiem | `"BBK2012"`, `"P1"` |

Ne katram uzdevumam ir visas īpašības: daudziem uzdevumiem vēl nav temata, metodes vai
jēdzienu. Īpašībām, kuru var nebūt, lietojiet `OPTIONAL { ... }`.

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

## Hierarhijas

Temati, metodes, žanri un jautājumu tipi ir SKOS hierarhijas. Katrai virsotnei ir
`skos:broader` (vecākā virsotne), vecākajām — `skos:narrower`. Virsotnei ir arī ID
(`eliozo:topicID`, ...), latvisks nosaukums (`eliozo:topicName`, ...), apraksts un
numurs, piemēram, `"4.1.1.0.0"`, kopā ar veselu skaitļu kārtošanas atslēgām
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Uzdevumiem var piešķirt jebkura līmeņa virsotnes. Lai atrastu visu, kas atrodas zem
kādas virsotnes, sekojiet hierarhijai ar īpašību ceļu: `?t skos:broader* eliozo:Divisibility`
atbilst gan pašam `Divisibility`, gan katrai virsotnei zem tā.

## Vaicājumu rakstīšana

* Klasifikatora virsotni raksta kā nosaukumu: `?p eliozo:topic eliozo:Divisibility`.
  Teksta vērtības raksta pēdiņās: `?p eliozo:domain "NT"`.
* Tekstiem ir valodas birkas. Lai lietotu tikai latvisko tekstu:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Paplašinātā meklēšana parāda `?problemID` vērtības; `?section` un `?subsection`
  tās sagrupē zem apakšvirsrakstiem.

Piemērs: 5.–7. klases uzdevumi par dalāmību (temats `Divisibility` un viss zem tā),
sagrupēti pa tematiem:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?topicName AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:topic ?topic .
      ?topic skos:broader* eliozo:Divisibility ;
             eliozo:topicName ?topicName .
      FILTER (?grade >= 5 && ?grade <= 7)
    }
    ORDER BY ?topicName ?problemID

Vairāk piemēru ir izvēlnē "Sagatavotie vaicājumi" virs vaicājuma lauka.

## No kurienes nāk dati

Klasifikatori tiek uzturēti Eliozo metadatu izklājlapās un eksportēti Turtle failos
(`worksheet-generation-with-llms/scripts/setup/resources`); uzdevumi tiek konvertēti
no uzdevumu repozitoriju Markdown failiem. Uzdevumiem birkas piešķir to Markdown
avotā, piemēram, `* topic:Divisibility`.

Saistītie standarti: temati ir salīdzināmi ar
[2020 Mathematics Subject Classification](https://mathscinet.ams.org/mathscinet/msc/msc2020.html)
(MSC2020), bet hierarhijas veidotas pēc tēzauru standarta ISO 25964 (virsotne, kas
tikai grupē bērnus, ir *kategorija*, un to uzdevumiem nepiešķir).
