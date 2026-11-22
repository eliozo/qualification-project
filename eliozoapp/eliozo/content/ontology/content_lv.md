# Ievads ontoloģijā

Eliozo uzdevumu krātuve ir RDF grafs. Katrs uzdevums ir resurss ar tipu
`eliozo:Problem`; tā īpašības norāda uz uzdevuma tekstu (vairākās valodās),
atrisinājumiem, avotu (grāmatu vai olimpiādi, gadu, klasi, numuru uzdevumu lapā)
un uzdevumu aprakstošiem metadatiem, kas parasti pieņem vērtības no kontrolētām
klasifikatoru vārdnīcām. Šajā lapā aprakstīti grafa jēdzieni; kā tos izmantot
SPARQL vaicājumos, skaidro lapa [Par paplašināto meklēšanu](/content/about_advanced_search).

## Formulējumi un atrisinājumi

Grafā ir divi galvenie resursi — *uzdevumu formulējumi* (RDF tips `eliozo:Problem`)
un *uzdevumu atrisinājumi* (RDF tips `eliozo:Solution`). Atbilstoši metadati
veido divus slāņus:

* **Formulējumu slānī** ir klasifikatori, ko var noteikt pirms uzdevuma risināšanas:
  *jautājuma tips* (prasītās atbildes struktūra), *nozare*, *žanrs* (piederība pēc
  ārējās līdzības vai sižeta) un nosacījumos izmantotie *jēdzieni*.
* **Atrisinājumu slānī** īpašības apraksta konkrēto atrisinājumu: *temati*
  (izmantotā teorija), *modelis* ("nesošā" matemātiskā struktūra, kas parāda
  saistību starp nosacījumu un atrisinājumu; tas ir tilts starp abiem slāņiem),
  *metodes* (risinājumā izmantotās taktikas un spriedumu šabloni) un atrisinājumos
  izmantotie *jēdzieni*.

Atsevišķi nosaukti "first-class" objekti (neanonīmi RDF resursi ar unikālām URL
adresēm) ir arī šādi objektu tipi:

* `eliozo:Claim` jeb *apgalvojums*, kas ierakstīts uzdevuma atrisinājumā (parasti
  papildu apgalvojumi vai lemmas vajadzīgi sarežģītākiem uzdevumiem, piemēram, IMO
  atrisinājumos). Apgalvojumiem mēdz būt arī savi pierādījumi ar to pašu RDF tipu
  `eliozo:Solution`.
* `eliozo:Hint` jeb *norāde*, ko pievieno vai nu formulējumam (sākotnējā uzdevuma
  vai tajā iekļauta apgalvojuma), vai atrisinājumam. Ieteicamais garums — līdz 160
  simboliem. Dažiem uzdevumiem norādes ir sakārtotas sarakstā no vispārīgākās līdz
  konkrētākajai — tās ir *norāžu kāpnes* (*hint ladder*).
* `eliozo:KeyIdea` jeb *pamatideja* — atrisinājuma vai kādas tā daļas pilnvērtīgs
  kopsavilkums, pēc kura risinātājam atliek izpildīt tehniskas detaļas. Atšķirībā
  no norādes pamatideja ne uz ko nemudina, bet var būt drusku garāka. Ieteicamais
  garums — līdz 500 simboliem.

Visi šie objekti "pieder" konkrētam uzdevumam un patstāvīgi neeksistē. Pat ja kāda
ideja der vairākiem uzdevumiem, katrā no tiem to formulē neatkarīgi.

## Klasifikatori

Parasti īpašību vērtības nevis izdomā katram uzdevumam no jauna, bet ņem no
*kontrolētas vārdnīcas* (*controlled vocabulary*). Šīs vārdnīcas neformāli sauksim
par klasifikatoriem, jo to vērtības bieži veido hierarhijas un vērtības piešķir ar
klasificēšanas procedūrām. Katram klasifikatoram ir sava lapa šīs izvēlnes sadaļā.

| Klasifikators | Kas tajā aprakstīts | Uzdevuma īpašība | Vērtības | Pārlūkot |
|---|---|---|---|---|
| [Temati](/content/ontology_topics) | teorija atrisinājumos | `eliozo:topic` | `eliozo:Topic` virsotnes | [pēc temata](/topics), [tematu tabula](/topics_table) |
| [Metodes](/content/ontology_methods) | atrisinājuma spriedumu šablons | `eliozo:method` | `eliozo:Method` virsotnes | [pēc metodes](/methods) |
| [Žanri un nozares](/content/ontology_genres) | viena no 4 nozarēm; uzdevuma (virspusējs) konteksts | `eliozo:domain`, `eliozo:subdomain` | teksts; `eliozo:Domain` virsotnes | [pēc žanra](/genres) |
| [Jautājumu tipi](/content/ontology_question_types) | jautājuma tips un atrisinājuma sagaidāmā struktūra | `eliozo:questionType` | teksts | [Filtri](/filter) |
| [Jēdzieni](/content/ontology_concepts) | jēdzieni uzdevuma formulējumā vai atrisinājumos | `eliozo:concepts` | `eliozo:Concept` virsotnes | [pēc jēdziena](/concepts) |
| [Olimpiādes](/content/ontology_olympiads) | olimpiāde vai cits avots | `eliozo:olympiad` | teksts | [Olimpiādes](/olympiads) |
| [Modeļi](/content/ontology_models) | "nesošā" matemātiskā struktūra atrisinājumā | *plānots* | | |
| [Ieteikumu tipi](/content/ontology_hint_types) | risināšanas fāze vai norādes heiristika | *plānots* | | |
| [Norādes](/content/ontology_hints) | norādes konkrētajam uzdevumam | *plānots* | | |

Kā klasifikatori saistīti savā starpā:

![Klasifikatoru attiecību grafs](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

Kreisajā pusē ir formulējumu slānis (žanrs, jēdzieni, jautājuma tips), labajā —
atrisinājumu slānis (temats, modelis, metode). Zem tiem norāžu kāpnes atbalsta
risinātāju un iesaka modeļus un metodes. Nepārtrauktās līnijas ir strukturālās
saites starp klasifikatoru tabulām, svītrotās — tipiskas asociācijas ("skatīt
arī"), punktētās — ieteikumi risinātājam. Ar `*` atzīmētās saites ir ierosinātas
un vēl nav aizpildītas.

## Hierarhijas (SKOS)

Temati, metodes, žanri un jautājumu tipi ir SKOS hierarhijas. Katrai virsotnei ir
`skos:broader` (vecākā virsotne), vecākajām — `skos:narrower`. Virsotnei ir arī ID
(`eliozo:topicID`, ...), latvisks nosaukums (`eliozo:topicName`, ...), apraksts un
numurs, piemēram, `"4.1.1.0.0"`, kopā ar veselu skaitļu kārtošanas atslēgām
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Uzdevumiem var piešķirt jebkura līmeņa virsotnes. Taču hierarhijās mēdz būt
virsotnes, kas tikai grupē bērnus (apakškategorijas) un netiek izmantotas uzdevumu
marķēšanai. Piemēram, nevienam uzdevumam nav temata `eliozo:TPC_Algebra` ("atrisinājumā
izmantotas kaut kādas algebras tēmas"), toties var piešķirt tematu
`eliozo:TPC_Identities` ("atrisinājumā izmantotas algebriskas identitātes").
Nepiešķiramos jēdzienus (*non-assignable concepts*) marķē ar `ex:assignable false`;
visi citi taksonomijas jēdzieni pēc noklusējuma ir piešķirami (*assignable*).

Pagaidām vietnē neizmantojam `skos:Collection`, lai veidotu no hierarhijas
neatkarīgas jēdzienu kolekcijas.

## Vārdu konvencijas

Resursiem, to tipiem, īpašībām un vērtībām ir lietotājam draudzīgi nosaukumi un
unikāli identifikatori, kuri reti mainās un ļauj rakstīt salīdzinoši stabilus
vaicājumus. Tas neizslēdz infrastruktūras līmenī izmantot arī tehniskus
identifikatorus (GUID), kas nav domāti lietotāju saskarnēm.

* **Uzdevumu identifikatori:**
  - `LV.AMO.2026.5.1` — Latvijas atklātās matemātikas olimpiādes 2026.gada 5.klases
    1.uzdevums.
  - Ja kādā gadā ir vairākas vienāda tipa olimpiādes, tās atšķir ar papildu burtu:
    `LV.AMO.2022A` notika 2022.g. aprīlī, `LV.AMO.2022B` — 2022.g. novembrī.
    Līdzīgi `EE.LHT.2024S` ir Igaunijas atklātā (*lahtine*) olimpiāde rudenī
    (*sügis*), bet `EE.LHT.2024T` — ziemā (*talv*).
  - Starptautisko olimpiāžu kodi sākas ar `WW`: `WW.IMOSHL.2022.A1` ir IMO īsā
    saraksta (*shortlist*) 1.algebras uzdevums, `WW.BW.2026.20` — Baltic Way
    2026.g. olimpiādes 20.uzdevums.
  - `BBK2012.P1.2` ir uzdevums no avota BBK2012 (A.Bērziņa, A.Bērziņas un D.Kūmas
    grāmata "Olimpiāžu un konkursu uzdevumu krājums skaitļu teorijā"), tās 1.daļas
    ("Skaitļu dalāmība") 2.uzdevums, bet `BBK2012.P1.E2` — tās pašas daļas
    2.piemērs. (Piemēriem grāmatās mēdz būt atsevišķa numerācija, un tos parasti
    izklāsta kopā ar atrisinājumiem.)
* **RDF tipu** nosaukumi ir kamieļrakstā un sākas ar lielo burtu: `eliozo:Problem`,
  `eliozo:KeyIdea`.
* **RDF īpašību** nosaukumi ir kamieļrakstā un sākas ar mazo burtu:
  `eliozo:problemSolution`.
* **Klasifikatoru vērtībām** bieži pievieno prefiksu, kas norāda klasifikatoru:
  - `eliozo:TPC_Algebra` — temats (*topic*) algebra;
  - `eliozo:MTH_MathematicalInduction` — matemātiskās indukcijas metode (*method*);
  - `eliozo:DOM_Algebra` — viena no 4 nozarēm (*domain*);
  - `eliozo:GEN_Weighings` — žanrs (*genre*): uzdevumi par svēršanu;
  - `QTY_FindAll` — jautājuma tips (*question type*): atrast visus un pamatot, ka
    citu bez atrastajiem nav;
  - `RSP_SolutionFull` — atbildes formāts: jāraksta pilns atrisinājums ar visiem
    pamatojumiem.

## Savietojamība ar citām ontoloģijām

Dažas uzdevumu īpašības (piemēram, avots un izcelsme, jēdziena, formulas vai attēla
lietojums tekstā, autortiesību statuss) ir objektīvi pārbaudāmi fakti, kas nav
specifiski olimpiāžu matemātikai. Pašreiz arī tām ir `eliozo:` vārdtelpas prefikss,
bet varētu izmantot vispārpieņemtas vārdtelpas:

* uzdevumu satura vienības varētu aprakstīt ar *Dublin Core* (piemēram,
  `dcterms:subject` īpašības `eliozo:topic` vietā);
* publiski zināmo informāciju par autoriem — ar *FOAF*;
* temati ievērojami pārklājas ar matemātisko zināšanu klasifikatoru
  [2020 Mathematics Subject Classification (MSC2020)](https://mathscinet.ams.org/mathscinet/msc/msc2020.html);
* jēdzienus, iespējams, varētu aprakstīt atbilstoši tēzauru standartam ISO 25964.
