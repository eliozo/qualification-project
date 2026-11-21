# Olimpiāžu matemātikas ontoloģija

## Uzdevumu krātuves mērķi

Latvijā no 1951.gada notiek [valsts olimpiādes](https://www.nms.lu.lv/olimpiades/valsts-olimpiade/) (ieskaitot skolas/sagatavošanās un rajona/novada posmus), 
bet no 1974.gada notiek [Atklātās olimpiādes](https://www.nms.lu.lv/olimpiades/atklata-olimpiade/). Uzdevumi un atrisinājumi pieejami 
[NMS arhīvā](https://www.nms.lu.lv/arhivs-un-materali/uzdevumu-arhivs/olimpiazu-uzdevumu-arhivs/). 

Arhīvs piedāvā uzdevumus sakārtotus atbilstoši olimpiādes tipam, 
norises gadam un klasei, bet reizēm šie dati jāizmanto arī citos griezumos. 

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
  šķirot lielās grupās pirms zināms, ko lietotāji meklēs.  
  Konsekventu indeksāciju grūti panākt dažiem uzdevumiem pēc pieprasījuma.
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


Eliozo primārā auditorija ir skolēni, 
skolotāji un citi, kuri viņus gatavo olimpiādēm, jaunu olimpiāžu komplektu 
sastādītāji. 
Vietnē Eliozo cenšamies nodrošināt datu redzamību MI rīkiem, lai 
vietnē apkopoto informāciju  varētu izmantot arī jaunos veidos, 
kurus Web saskarne neparedz. 

* Lētos metadatus, kurus var piešķirt un pārbaudīt MI aģenti  
  (klasifikatorus pēc temata, jēdzieniem, jautājuma 
  tipa) cenšamies izveidot pēc iespējas visiem uzdevumiem šajā vietnē - 
  tie ir vairāki tūkstoši uzdevumu. 
* Dārgos metadatus, kuri prasa uzdevuma testēšanu skolēnu auditorijā 
  vai tā piedāvāšanu olimpiādē (*ground truth*) veidojam mazākam skaitam 
  pedagoģiski interesantu uzdevumu - ceram to izdarīt dažiem simtiem uzdevumu, 
  lai nosegtu olimpiāžu dalībniekiem parasti mācāmos tematus.


### Citas olimpiāžu uzdevumu krātuves

* [ArtOfProblemSolving.Contests](https://artofproblemsolving.com/community/c13_contests)
  Uzdevumu publicēšanas un risināšanas forums, kur uzdevumus 
  var marķēt ar heštagiem. Ap 80 tūkstoši olimpiāžu uzdevumu. 
* [MIT CSAIL projekts MatNet](https://mathnet.mit.edu/) - ap 30 tūkstoši 
  uzdevumu no dažādu līmeņu starptautiskām sacensībām; sašķiroti 
  pa apakšnozarēm un tēmām. Projekta nodoms ir veicināt AI rīku 
  spējas risināt dažāda stila olimpiāžu uzdevumus. 
* [Omni-MATH](https://omni-math.github.io/) - ap 5 tūkstoši uzdevumu 
  modeļu apmācībai. 
* [OlymMATH](https://arxiv.org/html/2503.21380v3) - uzdevumi ķīniešu un 
  angļu valodās, labi anotēti un atrisināti ar Lean4. Var izmantot 
  AI rīku testēšanai. 
* [Olimpiāžu uzdevumu arhīvi](/references) Latvijas kaimiņvalstīs.
* [problems.ru](https://problems.ru/) satur olimpiāžu matemātiku no bijušās PSRS 
  avotiem. Katram uzdevumam parāda teorijas tematus, klases un sarežģītības novērtējumu.


## Datu modelis

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


Grafā ir divi galvenie resursi -- *uzdevumu formulējumi*
(RDF tips `eliozo:Problem`) un *uzdevumu atrisinājumi* (RDF tips `eliozo:Solution`).
* *Formulējumu slānī* piešķir klasifikatorus, ko var noteikt
  pirms uzdevuma risināšanas (*jautājuma tips* - ar prasītās atbildes struktūru, 
  *nozare*, *žanrs* - piederība pēc ārējās līdzības vai sižeta, 
  nosacījumos izmantotie *jēdzieni*).
* *Atrisinājumu slānī* īpašības piešķir konkrētajam atrisinājumam 
  (*tematus* - izmantoto teoriju, *modeli* - "nesošo" matemātisko struktūru, 
  kas parāda saistību starp nosacījumu un atrisinājumu, 
  *metodes* - risinājumā izmantotās taktikas un spriedumu šablonus, 
  atrisinājumos izmantotos *jēdzienus*).

Atsevišķi nosaukti "first-class" objekti (neanonīmi RDF resursi ar unikālām URL adresēm) 
ir arī šādi objektu tipi:

* `eliozo:Claim` jeb *Apgalvojums*, kas ierakstīts uzdevuma 
  atrisinājumā (parasti papildu apgalvojumi vai lemmas vajadzīgi
  sarežģītākiem uzdevumiem, piemēram, IMO atrisinājumos).
  Apgalvojumiem, kas ir iekļauti lielākā atrisinājumā, mēdz būt 
  arī pierādījumi ar jau zināmo RDF tipu `eliozo:Solution`.
* `eliozo:Hint` - norāde, ko vai nu pievieno apgalvojumam (ieskaitot 
  sākotnējā uzdevuma formulējumu) vai atrisinājumam (gan sākotnējā 
  uzdevuma, gan arī tajā iekļauta apgalvojuma atrisinājumam).
  Ieteicamais garums līdz 160 simboli. 
* `eliozo:KeyIdea` - atrisinājuma vai kādas tā daļas pilnvērtīgs 
  kopsavilkums, no kura risinātājam atliek izpildīt tehniskas 
  detaļas. Atšķirībā no norādes, pamatideja ne uz ko nemudina, bet 
  var būt pierakstīta drusku garāk. Ieteicamais garums līdz 500 simboli.



### Vārdu konvencijas

RDF datos resursiem, resursu tipiem, īpašībām un to vērtībām 
ir lietotājam draudzīgi nosaukumi un unikāli identifikatori, 
kuri reti mainās un ļauj rakstīt salīdzinoši stabilus 
SPARQL vaicājumus. 
Tas neizslēdz infrastruktūras līmenī izmantot arī "tehniskus identifikatorus"
(GUID), kas nav domāti lietotāju saskarnēm. 

* Uzdevumiem ir šādi identifikatori: 

  - "LV.AMO.2026.5.1" - Latvijas atklātās matemātikas olimpiāde 
    2026.gadā, 5.klases 1.uzdevums. 
  - Ja kādā gadā ir vairākas vienāda tipa olimpiādes, tās 
    var atšķirt ar papildu burtiem. Piemēram, "LV.AMO.2022A" apzīmē 
    olimpiādi, kas notika 2022.g. aprīlī, bet "LV.AMO.2022B" apzīmē 
    olimpiādi, kas notika 2022.g. novembrī. 
    Līdzīgi "EE.LHT.2024S" apzīmē Igaunijas atklāto (lahtine) olimpiādi 
    rudenī (sügis) un "EE.LHT.2024T" apzīmē Igaunijas atklāto olimpiādi 
    ziemā (talv). 
  - Starptautiskām olimpiādēm uzdevumu kodi sākas ar "WW". Piemēram, 
    "WW.IMOSHL.2022.A1" ir IMO īsā saraksta (shortlist) algebras uzdevums 
    nr.1, bet "WW.BW.2026.20" ir Baltic Way 2026.g. olimpiādes uzdevums nr.20.
  - "BBK2012.P1.2" ir uzdevums no avota BBK2012 (A.Bērziņa, A.Bērziņas un 
    D.Kūmas grāmata "Olimpiāžu un konkursu uzdevumu krājums skaitļu teorijā"), 
    šīs grāmatas 1.daļas ("Skaitļu dalāmība"), uzdevums nr.2. 
    Savukārt "BBK2012.P1.E2" ir 2.piemērs no tās pašas grāmatas. 
    (Piemēri ir tādi uzdevumi, kam grāmatās var būt atsevišķa numerācija un 
    kas parasti tiek izklāstīti kopā ar atrisinājumiem.)

* RDF tipu nosaukumi ir kamieļrakstā un sākas ar lielo burtu. 
  Piemēram, `eliozo:Problem`, `eliozo:KeyIdea`. 

* RDF īpašību nosaukumi ir kamieļrakstā un sākas ar mazo burtu. 
  Piemēram, `eliozo:hasSolution`.

* RDF īpašību vērtībām (nosauktiem resursiem) bieži pievienojam 
  prefiksus, lai tos varētu atšķirt arī paliekot vienā vārdtelpā.

  - `eliozo:TPC_Algebra`: temats algebra (*topic*). 
  - `eliozo:MTH_MathematicalInduction`: matemātiskās indukcijas metode (*method*).
  - `eliozo:DOM_Algebra`: viena no 4 nozarēm (*domain*).
  - `eliozo:GEN_Weighings`: žanrs - uzdevumi par svēršanu (*genre*). 
  - `eliozo:QTY_FindAll`: jautājuma tips - atrast visus un pamatot, ka citu bez atrastajiem nav (*question-type*). 
  - `eliozo:RSP_SolutionFull`: atbildes formāts - pilns risinājums (uzdevumā paredzēts rakstīt pilnu atrisinājumu ar visiem pamatojumiem). 
    



### Savietojamība ar SKOS

Temati, metodes, žanri un jautājumu tipi ir SKOS hierarhijas. Katrai virsotnei ir
`skos:broader` (vecākā virsotne), vecākajām — `skos:narrower`. Virsotnei ir arī ID
(`eliozo:topicID`, ...), latvisks nosaukums (`eliozo:topicName`, ...), apraksts un
numurs, piemēram, `"4.1.1.0.0"`, kopā ar veselu skaitļu kārtošanas atslēgām
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Uzdevumiem var piešķirt jebkura līmeņa virsotnes. Lai atrastu visu, kas atrodas zem
kādas virsotnes, sekojiet hierarhijai ar īpašību ceļu: `?t skos:broader* eliozo:Divisibility`
atbilst gan pašam `Divisibility`, gan katrai virsotnei zem tā.

Hierarhijās mēdz būt virsotnes, kas tikai grupē bērnus (apakškategorijas), 
bet tās neizmanto uzdevumu marķēšanai. Piemēram, nevienam uzdevumam `eliozo:Topic` 
nav `eliozo:problemTopic` vērtība `eliozo:TPC_Algebra` (uzdevuma atrisinājumā 
izmantojamas kaut kādas algebras tēmas). Toties var piešķirt vērtību
`eliozo:TPC_Identities` (uzdevuma atrisinājumā izmantotas algebriskas identitātes). 

Nepiešķiramas vērtības (*non-assignable concepts*) marķē 
ar `ex:assignable false`. Visi citi jēdzieni taksonomijā ir piešķirami 
(*assignable concept*) - noklusētā vērtība.

Pagaidām vietnē neizmantojam `skos:Collection`, lai veidotu no hierarhijas neatkarīgas 
jēdzienu kolekcijas.


### Savietojamība ar citām ontoloģijām

Dažas RDF īpašības uzdevumiem (piemēram, avots un izcelsme, jēdziena, 
formulas vai attēla lietojums tekstā, autortiesību statuss) 
ir objektīvi pārbaudāmi fakti, kas nav specifiski olimpiāžu matemātikai. 
Pašreiz arī šādām īpašībām ir `eliozo:` vārdtelpas prefikss, 
bet varētu izmantot arī dažas vispārpieņemtas vārdtelpas. 

* Uzdevumu satura vienības varētu aprakstīt ar *Dublin Core*, 
* Publiski zināmo informāciju par autoriem varētu aprakstīt ar *FOAF*, 
* `eliozo:Topic` ievērojami pārklājas ar matemātisko zināšanu klasifikatoru 
  [2020 Mathematics Subject Classification (MSC2020)](https://mathscinet.ams.org/mathscinet/msc/msc2020.html). 
* Jēdzieni, iespējams būtu apzīmējami ar tēzauru standartu ISO 25964. 
  
Piemēram, varētu lietot Dublin Core īpašību  
`dcterms:subject` tā vietā lai rakstītu `eliozo:topic` (kas apzīmē 
resursa tēmu), bet pagaidām tā nedarām.



## Klasifikatori

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




Solution → proves → Claim	1	0..*
Solution → usesClaim → Claim	0..*	0..*
Solution → usesIdea → KeyIdea	0..*	0..*
Hint → targetsClaim → Claim	1	0..*
Hint → revealsIdea → KeyIdea	0..*	0..*



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



## Vaicājumu rakstīšana

* Klasifikatora virsotni raksta kā nosaukumu: `?p eliozo:topic eliozo:Divisibility`.
  Teksta vērtības raksta pēdiņās: `?p eliozo:domain "NT"`.
* Tekstiem ir valodas birkas. Lai lietotu tikai latvisko tekstu:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Paplašinātā meklēšana parāda `?problemID` vērtības; `?section` un `?subsection`
  tās sagrupē zem apakšvirsrakstiem.

## Piemēri

Katra saite atver [paplašināto meklēšanu](/advanced_search) un uzreiz izpilda
vaicājumu; to var tur rediģēt un palaist vēlreiz. Visi šie vaicājumi ir arī izvēlnē
"Sagatavotie vaicājumi > Ontoloģija" virs vaicājuma lauka, bet citi piemēri —
tās pašas izvēlnes punktos "Piemēri", "Uzdevumu tipi" un "Teorijas temati".

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

