# Olimpiāžu matemātikas ontoloģija

## Uzdevumu krātuves mērķi

Esošie [olimpiāžu uzdevumu arhīvi](/references) 
parasti apkopo uzdevumus un to atrisinājumus; reizēm 
pievienojot tiem meklēšanas iespējas.  
[ArtOfProblemSolving.Contests](https://artofproblemsolving.com/community/c13_contests)
izmanto heštagus, bet [problems.ru](https://problems.ru/) katram uzdevumam 
parāda tematus, klases un sarežģītības novērtējumu.

* **Atbilstība programmu paraugiem:** Latvijas pamatizglītībā un vidusskolas 
  kursos Matemātika I un Matemātika II izmantojamas 
  [Skola2030 un 2026.g. programmas](https://mape.gov.lv/page/programms). 
  Piedāvājot uzdevumus mūsdienu skolēniem, nevar paļauties 
  uz senākiem izglītības standartiem vai tām klasēm, kas norādītas 
  [NMS uzdevumu arhīvā](https://www.nms.lu.lv/arhivs-un-materali/uzdevumu-arhivs/).
  Piesaiste standartam un programmai prasa pārbaudāmību, bet 
  esošajos olimpiāžu arhīvos informācijas par skolas zināšanām nav.
* **Citu metadatu priekšapstrāde:** Uzdevumu efektīvai meklēšanai 
  un ranžēšanai nepieciešama klasifikācija. Uzdevumus vislabāk 
  šķirot lielās grupās un proaktīvi (pirms zināms, ko lietotāji meklēs), 
  jo konsekventu indeksāciju grūti panākt dažiem atsevišķam uzdevumam pēc pieprasījuma.
* **Pakāpeniska palīdzība:** Olimpiāžu uzdevumu mācīšanas pieredzi 
  var apkopot kā *norāžu kāpnes*, kas ved pie *pamatidejām*. 
  MI rīki viegli saģenerētu norādes, bet tās jāpārskata un jānotestē, 
  jo nevietā sniegtas norādes un slikti strukturēta palīdzība 
  neko neuzlabo. Mācīšanas gaitā rodas arī *pedagoģiskie novērojumi*
  par biežiem pārpratumiem un izplatītām kļūdām.
* **Uzdevumu empīriskā grūtība:** Katras olimpiādes rezultātu tabula 
  dod faktuālo pamatojumu (*grounding*), lai varētu spriest par uzdevumu 
  grūtības pakāpi. Empīriska grūtība, ja to var iegūt, ir daudz precīzāka
  par jebkādu "spekulatīvi" iegūtu grūtības skaitli (piemēram, atrisinājuma 
  garums, izmantoto pamatideju skaits, priekšzināšanu apjoms, utt.).
  Olimpiādēs izveidojas arī *vērtēšanas kritēriji*, kas palīdz saprast, 
  kādi daļējie vērtējumi bija izplatīti.
* **Uzdevumu saistība:** Uzdevumu varianti, līdzīga pamatideja citā ietērpā 
  un līdzīgi fragmenti atrisinājumos ļauj atrast radniecīgu uzdevumu virknes, 
  kas pamazām noskaidrojas, strādājot ar uzdevumu korpusu. 
* **Iztīrīts teksts vairākās valodās:** Ja arhīvu uzdevumus pārskata pēc olimpiādēm,
  uzdevumu un atrisinājumu tekstos var novērst nepilnības. 





## Datu apraksts

Eliozo uzdevumu krātuve ir RDF grafs. Katrs uzdevums ir resurss
ar tipu `eliozo:Problem`; īpašības norāda uz uzdevuma tekstu 
latviski un angliski, atrisinājumiem, avotu un izcelsmi 
(grāmatu, olimpiādi, gadu, klasi, numuru uzdevumu lapā), 
un arī uzdevumu aprakstošiem metadatiem, kas parasti 
pieņem vērtības no kontrolētām klasifikatoru vārdnīcām. 
Te skaidrojam RDF datu struktūru, lai lapā
[Paplašinātā meklēšana](/advanced_search) rakstītu SPARQL 
vaicājumus.

Visi turpmāk lietotie nosaukumi pieder divām vārdtelpām: 
prefikss `eliozo:` norāda uz skolas sacensību matemātikai 
raksturīgiem resursu tipiem, īpašībām un to iespējamajām 
vērtībām; `skos:` norāda uz attiecībām klasifikatoru 
vērtību hierarhijās (piemēram, temats "kvadrātfunkcija" 
ir šaurāks nekā temats "algebra"). Prefiksu definīcijas, 
ar ko sākas tipisks SPARQL vaicājums:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Klasifikatori

Dažas RDF īpašības uzdevumiem (piemēram, avots un izcelsme, jēdziena, 
formulas vai attēla lietojums tekstā, autortiesību statuss) 
ir objektīvi pārbaudāmi fakti, kas nav specifiski olimpiāžu matemātikai. 
Tiem ceram izmantot vispārpieņemtas mini ontoloģijas 
(uzdevumu satura vienības varētu aprakstīt ar *Dublin Core*, 
un publiski zināmo informāciju par autoriem -- ar *FOAF*).

Satura veidošanā svarīgākas ir  
olimpiādēm specifiskas metadatu īpašības un to 
vērtības. Parasti īpašību vērtības nevis izdomā katram 
uzdevumam no jauna, bet ņem no *kontrolētas vārdnīcas* 
(*controlled vocabulary*). Īpašībām atbilstošās 
vērtību vārdnīcas neformāli sauksim arī par klasifikatoriem, 
jo vārdnīcās iekļautās vērtības bieži veido hierarhijas 
un var runāt par klasificēšanas procedūrām, lai piešķirtu 
īpašībai vērtības.


| Klasifikators | Kas tajā aprakstīts | RDF īpašība | Vērtību vārdnīca | Pārlūkot |
|---|---|---|---|---|
| [Temati](/content/ontology_topics) | teorija atrisinājumos | `eliozo:topic` | [tematu tabula](/topics_table) | [pēc temata](/topics) |
| [Metodes](/content/ontology_methods) | atrisinājuma spriedumu šablons | `eliozo:method` | [metožu tabula](/methods_table) | [pēc metodes](/methods) |
| [Nozares](/content/ontology_domains) | kura no 4 nozarēm | `eliozo:domain` | [nozaru tabula](/domains_table) | sk. [Filtri](/filter) |
| [Žanri](/content/ontology_genres) | uzdevuma (virspusējs) konteksts | `eliozo:domain`, `eliozo:genre` | [žanru tabula](/genres_table) | [pēc žanra](/genres) |
| [Jautājumu tipi](/content/ontology_question_types) | jautājuma tips (un atrisinājuma sagaidāmā struktūra) | `eliozo:questionType` | [jautājumu tipu tabula](/question_types_table) | sk. [Filtri](/filter) |
| [Jēdzieni](/content/ontology_concepts) | jēdzieni uzdevuma formulējumā vai atrisinājumos | `eliozo:concepts` | [jēdzienu tabula](/concepts_table) | [pēc jēdziena](/concepts) |
| [Olimpiādes](/content/ontology_olympiads) | olimpiāde vai cits avots | `eliozo:olympiad` | [olimpiāžu tabula](/olympiads_table) | [Olimpiādes](/olympiads) |
| [Modeļi](/content/ontology_models) | "nesošā" matemātiskā struktūra atrisinājumā | *plānots* | | |
| [Ieteikumu tipi](/content/ontology_hint_types) | risināšanas fāze vai ieteikuma heiristika | *plānots* | | |
| [Ieteikumi](/content/ontology_hints) | ieteikumi konkrētajam uzdevumam | *plānots* | | |

Kā klasifikatori saistīti savā starpā:

![Klasifikatoru attiecību grafs](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

Grafā ir divi galvenie resursi -- *uzdevumu formulējumi*
(RDF tips `eliozo:Problem`), *uzdevumu atrisinājumi* (RDF tips `eliozo:Solution`).
* *Formulējumu slānī* piešķir klasifikatorus, ko var noteikt
  pirms uzdevuma risināšanas (*jautājuma tips* - ar prasītās atbildes struktūru, 
  *nozare*, *žanrs* - piederība pēc ārējās līdzības vai sižeta, 
  nosacījumos izmantotie *jēdzieni*).
* *Atrisinājumu slānī* īpašības piešķir konkrētajam atrisinājumam 
  (*tematus* - izmantoto teoriju, *modeli* - "nesošo" matemātisko struktūru, 
  kas parāda saistību starp nosacījumu un atrisinājumu, 
  *metodes* - risinājumā izmantotās taktikas un spriedumu šablonus. 

Atsevišķi nosaukti objekti (neanonīmi RDF resursi ar unikālām URL adresēm) 
ir arī šādiem objektu tipiem:

* `eliozo:Claim` - apgalvojums (dažos gadījumos - cita veida
  apakšuzdevums), kas ierakstīts uzdevuma atrisinājumā (parasti vajadzīgs
  sarežģītākiem uzdevumiem, piemēram, lemmas IMO atrisinājumos). 
  Apgalvojumiem, kas ir iekļauti lielākā atrisinājumā, mēdz būt 
  arī pierādījumi ar jau zināmo RDF tipu `eliozo:Solution`.
* `eliozo:Hint` - norāde, ko vai nu pievieno apgalvojumam (ieskaitot 
  sākotnējā uzdevuma formulējumu), 
* `eliozo:KeyIdea` - 



Solution → proves → Claim	1	0..*
Solution → usesClaim → Claim	0..*	0..*
Solution → usesIdea → KeyIdea	0..*	0..*
Hint → targetsClaim → Claim	1	0..*
Hint → revealsIdea → KeyIdea	0..*	0..*

* 

resursi 
(spriedumu šablonu). Zem tiem *ieteikumu kāpnes* (hint ladder) atbalsta risinātāju un
iesaka modeļus un metodes.

Nepārtrauktās līnijas ir strukturālās saites starp klasifikatoru tabulām,
svītrotās — citas saites ("skatīt arī").
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
[2020 Mathematics Subject Classification (MSC2020)](https://mathscinet.ams.org/mathscinet/msc/msc2020.html), bet hierarhijas veidotas pēc tēzauru standarta ISO 25964 (virsotne, kas
tikai grupē bērnus, ir *kategorija*, un to uzdevumiem nepiešķir).
