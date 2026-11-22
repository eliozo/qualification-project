# Įvadas į ontologiją

Eliozo uždavinių bazė yra RDF grafas. Kiekvienas uždavinys yra `eliozo:Problem` tipo
išteklius; jo savybės nurodo uždavinio tekstą (keliomis kalbomis), sprendimus, šaltinį
(knygą ar olimpiadą, metus, klasę, numerį uždavinių lape) ir uždavinį aprašančius
metaduomenis, kurių reikšmės paprastai imamos iš kontroliuojamų klasifikatorių žodynų.
Šiame puslapyje aprašomos grafo sąvokos; kaip jas naudoti SPARQL užklausose, paaiškinta
puslapyje [Apie išplėstinę paiešką](/content/about_advanced_search).

## Sąlygos ir sprendimai

Grafe yra du pagrindiniai ištekliai — *uždavinių sąlygos* (RDF tipas `eliozo:Problem`)
ir *uždavinių sprendimai* (RDF tipas `eliozo:Solution`). Atitinkamai metaduomenys
sudaro du sluoksnius:

* **Sąlygų sluoksnyje** yra klasifikatoriai, kuriuos galima nustatyti prieš sprendžiant
  uždavinį: *klausimo tipas* (prašomo atsakymo struktūra), *sritis*, *žanras*
  (priklausymas pagal išorinį panašumą ar siužetą) ir sąlygoje vartojamos *sąvokos*.
* **Sprendimų sluoksnis** aprašo konkretų sprendimą: *temos* (panaudota teorija),
  *modelis* („laikančioji“ matematinė struktūra, siejanti sąlygą su sprendimu; tai tiltas
  tarp abiejų sluoksnių), *metodai* (sprendime panaudotos taktikos ir samprotavimų
  šablonai) ir sprendimuose vartojamos *sąvokos*.

Atskirai įvardyti „first-class“ objektai (neanoniminiai RDF ištekliai su unikaliais URL)
yra ir šie objektų tipai:

* `eliozo:Claim` — uždavinio sprendime suformuluotas *teiginys* (papildomų teiginių ar
  lemų paprastai reikia sudėtingesniems uždaviniams, pavyzdžiui, IMO sprendimuose).
  Teiginiai gali turėti savo įrodymus su tuo pačiu RDF tipu `eliozo:Solution`.
* `eliozo:Hint` — *užuomina*, pridedama arba prie sąlygos (pradinio uždavinio ar jame
  esančio teiginio), arba prie sprendimo. Rekomenduojamas ilgis — iki 160 simbolių. Kai
  kuriems uždaviniams užuominos išdėstytos nuo bendriausios iki konkrečiausios — tai
  *užuominų laiptai* (*hint ladder*).
* `eliozo:KeyIdea` — *pagrindinė idėja*: išsami sprendimo ar jo dalies santrauka, po
  kurios sprendėjui lieka atlikti tik technines detales. Skirtingai nuo užuominos,
  pagrindinė idėja nieko neragina, bet gali būti šiek tiek ilgesnė. Rekomenduojamas
  ilgis — iki 500 simbolių.

Visi šie objektai „priklauso“ konkrečiam uždaviniui ir savarankiškai neegzistuoja. Net
jei kokia nors idėja tinka keliems uždaviniams, kiekviename iš jų ji formuluojama
nepriklausomai.

## Klasifikatoriai

Savybių reikšmės paprastai ne sugalvojamos kiekvienam uždaviniui iš naujo, o imamos iš
*kontroliuojamo žodyno* (*controlled vocabulary*). Šiuos žodynus neformaliai vadiname
klasifikatoriais, nes jų reikšmės dažnai sudaro hierarchijas ir priskiriamos
klasifikavimo procedūromis. Kiekvienas klasifikatorius turi savo puslapį šiame meniu
skyriuje.

| Klasifikatorius | Ką aprašo | Uždavinio savybė | Reikšmės | Naršyti |
|---|---|---|---|---|
| [Temos](/content/ontology_topics) | sprendimuose naudojama teorija | `eliozo:topic` | `eliozo:Topic` viršūnės | [pagal temą](/topics), [temų lentelė](/topics_table) |
| [Metodai](/content/ontology_methods) | sprendimo samprotavimų šablonas | `eliozo:method` | `eliozo:Method` viršūnės | [pagal metodą](/methods) |
| [Žanrai ir sritys](/content/ontology_genres) | viena iš 4 sričių; (išorinis) uždavinio kontekstas | `eliozo:domain`, `eliozo:subdomain` | tekstas; `eliozo:Domain` viršūnės | [pagal žanrą](/genres) |
| [Klausimų tipai](/content/ontology_question_types) | klausimo tipas ir laukiama sprendimo struktūra | `eliozo:questionType` | tekstas | [Filtrai](/filter) |
| [Sąvokos](/content/ontology_concepts) | sąvokos uždavinio sąlygoje ar sprendimuose | `eliozo:concepts` | `eliozo:Concept` viršūnės | [pagal sąvoką](/concepts) |
| [Olimpiados](/content/ontology_olympiads) | olimpiada ar kitas šaltinis | `eliozo:olympiad` | tekstas | [Olimpiados](/olympiads) |
| [Modeliai](/content/ontology_models) | „laikančioji“ matematinė sprendimo struktūra | *planuojama* | | |
| [Užuominų tipai](/content/ontology_hint_types) | sprendimo fazė ar užuominos euristika | *planuojama* | | |
| [Užuominos](/content/ontology_hints) | konkretaus uždavinio užuominos | *planuojama* | | |

Kaip klasifikatoriai susiję tarpusavyje:

![Klasifikatorių ryšių grafas](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

Diagramoje (užrašai latviškai) kairėje yra sąlygų sluoksnis (žanras, sąvokos, klausimo
tipas), dešinėje — sprendimų sluoksnis (tema, modelis, metodas). Po jais užuominų
laiptai padeda sprendėjui ir siūlo modelius bei metodus. Ištisinės linijos — struktūrinės
nuorodos tarp klasifikatorių lentelių, brūkšninės — tipinės asociacijos („žr. taip pat“),
taškinės — pasiūlymai sprendėjui. Žvaigždute `*` pažymėti ryšiai yra pasiūlyti ir dar
neužpildyti.

## Hierarchijos (SKOS)

Temos, metodai, žanrai ir klausimų tipai yra SKOS hierarchijos. Kiekviena viršūnė turi
`skos:broader` (tėvinę viršūnę), o tėvinės — `skos:narrower`. Viršūnė taip pat turi ID
(`eliozo:topicID`, ...), latvišką pavadinimą (`eliozo:topicName`, ...), aprašymą ir
numerį, pavyzdžiui, `"4.1.1.0.0"`, kartu su sveikųjų skaičių rikiavimo raktais
`eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Uždaviniams galima priskirti bet kurio lygio viršūnes. Tačiau hierarchijose būna
viršūnių, kurios tik grupuoja vaikus (subkategorijos) ir nenaudojamos uždaviniams žymėti.
Pavyzdžiui, nė vienas uždavinys neturi temos `eliozo:TPC_Algebra` („sprendime naudojamos
kažkokios algebros temos“), bet galima priskirti temą `eliozo:TPC_Identities` („sprendime
naudojami algebriniai tapatumai“). Nepriskiriamos sąvokos žymimos `ex:assignable false`;
visos kitos taksonomijos sąvokos pagal nutylėjimą yra priskiriamos.

Svetainėje kol kas nenaudojame `skos:Collection` nuo hierarchijos nepriklausomoms sąvokų
kolekcijoms sudaryti.

## Pavadinimų konvencijos

Ištekliai, jų tipai, savybės ir reikšmės turi naudotojui patogius pavadinimus ir
unikalius identifikatorius, kurie retai keičiasi, todėl užklausos išlieka gana stabilios.
Tai neatmeta techninių identifikatorių (GUID) infrastruktūros lygmeniu, kurie nėra skirti
naudotojo sąsajoms.

* **Uždavinių identifikatoriai:**
  - `LV.AMO.2026.5.1` — Latvijos atvirosios matematikos olimpiados 2026 m. 5 klasės
    1 uždavinys.
  - Jei per metus vyksta kelios to paties tipo olimpiados, jos atskiriamos papildoma
    raide: `LV.AMO.2022A` vyko 2022 m. balandį, `LV.AMO.2022B` — 2022 m. lapkritį.
    Panašiai `EE.LHT.2024S` yra Estijos atviroji (*lahtine*) olimpiada rudenį
    (*sügis*), o `EE.LHT.2024T` — žiemą (*talv*).
  - Tarptautinių olimpiadų kodai prasideda `WW`: `WW.IMOSHL.2022.A1` — IMO trumpojo
    sąrašo (*shortlist*) 1-asis algebros uždavinys, `WW.BW.2026.20` — Baltic Way 2026 m.
    olimpiados 20-asis uždavinys.
  - `BBK2012.P1.2` — uždavinys iš šaltinio BBK2012 (A. Bērziņio, A. Bērziņos ir
    D. Kūmos knyga „Olimpiāžu un konkursu uzdevumu krājums skaitļu teorijā“), jos
    1 dalies („Skaičių dalumas“) 2 uždavinys, o `BBK2012.P1.E2` — tos pačios dalies
    2 pavyzdys. (Pavyzdžiai knygose dažnai numeruojami atskirai ir paprastai pateikiami
    kartu su sprendimais.)
* **RDF tipų** pavadinimai rašomi kupranugario stiliumi ir prasideda didžiąja raide:
  `eliozo:Problem`, `eliozo:KeyIdea`.
* **RDF savybių** pavadinimai rašomi kupranugario stiliumi ir prasideda mažąja raide:
  `eliozo:problemSolution`.
* **Klasifikatorių reikšmėms** dažnai pridedamas priešdėlis, nurodantis klasifikatorių:
  - `eliozo:TPC_Algebra` — tema (*topic*) algebra;
  - `eliozo:MTH_MathematicalInduction` — matematinės indukcijos metodas (*method*);
  - `eliozo:DOM_Algebra` — viena iš 4 sričių (*domain*);
  - `eliozo:GEN_Weighings` — žanras (*genre*): uždaviniai apie svėrimus;
  - `QTY_FindAll` — klausimo tipas (*question type*): rasti visus ir įrodyti, kad kitų
    nėra;
  - `RSP_SolutionFull` — atsakymo formatas: reikia parašyti pilną sprendimą su visais
    pagrindimais.

## Suderinamumas su kitomis ontologijomis

Kai kurios uždavinių savybės (pavyzdžiui, šaltinis ir kilmė, sąvokos, formulės ar
paveikslo naudojimas tekste, autorių teisių statusas) yra objektyviai patikrinami faktai,
nebūdingi vien olimpiadų matematikai. Šiuo metu jos taip pat turi `eliozo:` vardų erdvės
priešdėlį, bet būtų galima naudoti visuotinai priimtas vardų erdves:

* uždavinių turinio vienetus būtų galima aprašyti *Dublin Core* (pavyzdžiui,
  `dcterms:subject` vietoj `eliozo:topic`);
* viešai žinomą informaciją apie autorius — *FOAF*;
* temos gerokai persidengia su matematikos žinių klasifikatoriumi
  [2020 Mathematics Subject Classification (MSC2020)](https://mathscinet.ams.org/mathscinet/msc/msc2020.html);
* sąvokas galbūt būtų galima aprašyti pagal tezaurų standartą ISO 25964.
