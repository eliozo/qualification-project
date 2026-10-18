# Ontologija

Eliozo uždavinių bazė saugoma kaip RDF grafas. Kiekvienas uždavinys yra klasės
`eliozo:Problem` viršūnė; jos savybės nurodo uždavinio tekstus, sprendimus,
olimpiadą ir **klasifikatorius** (metaduomenis), kurie uždavinį aprašo. Šis puslapis
yra to grafo žemėlapis tiems, kurie rašo užklausas puslapyje
[Išplėstinė paieška](/advanced_search).

Visi toliau naudojami pavadinimai priklauso dviem vardų sritims:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Klasifikatoriai

| Klasifikatorius | Ką jis aprašo | Uždavinio savybė | Reikšmės | Naršyti |
|---|---|---|---|---|
| [Temos](/content/ontology_topics) | teoriją, kurią naudoja sprendimas | `eliozo:topic` | `eliozo:Topic` viršūnės | [pagal temą](/topics), [temų lentelė](/topics_table) |
| [Metodai](/content/ontology_methods) | sprendimo samprotavimo šabloną | `eliozo:method` | `eliozo:Method` viršūnės | [pagal metodą](/methods) |
| [Žanrai](/content/ontology_genres) | kaip uždavinys atrodo, jo „siužetą“ | `eliozo:domain`, `eliozo:subdomain` | tekstas; `eliozo:Domain` viršūnės | [pagal žanrą](/genres) |
| [Klausimų tipai](/content/ontology_question_types) | kokio atsakymo prašoma | `eliozo:questionType` | tekstas | [Filtrai](/filter) |
| [Sąvokos](/content/ontology_concepts) | sąvokas uždavinio formuluotėje | `eliozo:concepts` | `eliozo:Concept` viršūnės | [pagal sąvoką](/concepts) |
| [Olimpiados](/content/ontology_olympiads) | varžybas | `eliozo:olympiad` | tekstas | [Olimpiados](/olympiads) |
| [Modeliai](/content/ontology_models) | matematinę struktūrą, kurią sukuria sprendėjas | *planuojama* | | |
| [Užuominų tipai](/content/ontology_hint_types) | euristinių užuominų rūšis | *planuojama* | | |
| [Užuominos](/content/ontology_hints) | vieno uždavinio užuominas | *planuojama* | | |

Kaip klasifikatoriai susiję tarpusavyje:

![Klasifikatorių ryšių grafas](/content/ontology/klasifikatoru_attiecibu_grafs.svg)

Grafe (užrašai latviškai) yra du sluoksniai. **Uždavinio formuluotės sluoksnis**
(kairėje) matomas dar nesprendžiant uždavinio: jo *žanras* (išorinis panašumas,
siužetas), *sąvokos* sąlygose ir *klausimo tipas* (prašomo atsakymo struktūra).
**Sprendimo sluoksnis** (dešinėje) aprašo vieną konkretų sprendimą: jo *temą*
(teoriją), *modelį* (matematinę struktūrą, kurią sukuria sprendėjas; modelis yra
tiltas tarp abiejų sluoksnių) ir *metodą* (samprotavimo šabloną). Po jais
*užuominų kopėčios* (hint ladder) padeda sprendėjui ir siūlo modelius bei metodus.

Ištisinės rodyklės yra struktūrinės nuorodos tarp klasifikatorių lentelių,
brūkšninės — tipiniai ryšiai („žr. taip pat“), taškinės — užuominos sprendėjui.
Ryšiai, pažymėti `*`, yra siūlomi ir dar neužpildyti.

## Uždavinio viršūnė

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:problemID` | tekstas | `"LV.AMO.2019.7.4"` |
| `eliozo:problemText` | Markdown, po vieną kiekvienam vertimui, su kalbos žyme | `"Andris apgalvo, ..."@lv` |
| `eliozo:problemTextHtml` | tas pats tekstas HTML formatu | |
| `eliozo:olympiad` | olimpiados ID | `"LV.AMO"` |
| `eliozo:olympiadCode`, `eliozo:country` | šio ID dalys | `"AMO"`, `"LV"` |
| `eliozo:event` | vienas olimpiados turas | `"LV.AMO.2019"` |
| `eliozo:problemYear`, `eliozo:problemGrade` | sveikieji skaičiai | `2019`, `7` |
| `eliozo:suggestedGrade` | sveikasis skaičius, gali kartotis | `7` |
| `eliozo:olympiadType` | tekstas | `"National"`, `"RegionalOrOpen"`, `"TeamSelection"`, `"International"`, `"Contest"`, `"Book"` |
| `eliozo:domain` | žanras, viršutinis lygis | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | žanras | `eliozo:DOM_GridCut` |
| `eliozo:topic` | tema | `eliozo:Divisibility` |
| `eliozo:method` | metodas | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | sąvoka | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | klausimo tipas | `"FindAll"` |
| `eliozo:problemSolution` | sprendimo viršūnė | |
| `eliozo:hasVideo` | vaizdo įrašo viršūnė | |
| `eliozo:answer` | trumpas atsakymas | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | susijusių ar tapačių uždavinių ID | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | uždaviniams iš knygų | `"BBK2012"`, `"P1"` |

Ne kiekvienas uždavinys turi visas savybes: daugelis uždavinių dar neturi temos,
metodo ar sąvokų. Savybėms, kurių gali nebūti, naudokite `OPTIONAL { ... }`.

**Sprendimai** (`eliozo:Solution`) turi `eliozo:solutionText` (Markdown su kalbos
žyme), `eliozo:solutionTextHtml` ir `eliozo:solutionNum`. **Vaizdo įrašai**
(`eliozo:Video`) turi `eliozo:videoTitle`, `eliozo:videoYoutube` ir
`eliozo:videoBookmarks` — `eliozo:VideoBookmark` viršūnių sąrašą su
`eliozo:videoBookmarkTstamp` (sekundės) ir `eliozo:videoBookmarkText`.

## Automatiškai pasiūlytos žymės

Savybes, kurių pavadinimas prasideda pabraukimo ženklu, pasiūlė kalbos modelis, ir jos
nėra patikrintos. Jų reikšmės yra paprastas tekstas, o ne klasifikatorių viršūnės:

| Savybė | Reikšmių pavyzdžiai |
|---|---|
| `eliozo:_hasSolutionConcept` | `"DivisibilityRelation"`, `"Invariant"`, `"LatticeGrid"` |
| `eliozo:_hasReasoningMethod` | `"ConstructiveExampleForExistence"`, `"CaseAnalysis"` |
| `eliozo:_hasReasoningMistake` | `"FromSpecialToGeneral"` |
| `eliozo:_readingDifficulty` | `"low"`, `"medium"`, `"high"` |
| `eliozo:_mistakesFit` | `"low"`, `"medium"`, `"high"` |

Jos apima daug daugiau uždavinių nei patikrinti klasifikatoriai, todėl tinka
kandidatams ieškoti, tačiau rezultatus reikia patikrinti.

## Hierarchijos

Temos, metodai, žanrai ir klausimų tipai yra SKOS hierarchijos. Kiekviena viršūnė
turi `skos:broader` (tėvinę viršūnę), o tėvinės viršūnės — `skos:narrower`.
Viršūnė taip pat turi ID (`eliozo:topicID`, ...), pavadinimą latviškai
(`eliozo:topicName`, ...), aprašymą ir numerį, pavyzdžiui, `"4.1.1.0.0"`, kartu su
sveikųjų skaičių rikiavimo raktais `eliozo:sorter_L1`, `eliozo:sorter_L2`, ...

Uždaviniams gali būti priskirtos bet kurio lygio viršūnės. Norėdami rasti viską, kas
yra po tam tikra viršūne, sekite hierarchiją savybių keliu:
`?t skos:broader* eliozo:Divisibility` atitinka ir patį `Divisibility`, ir kiekvieną
viršūnę po juo.

## Užklausų rašymas

* Klasifikatoriaus viršūnė rašoma kaip pavadinimas: `?p eliozo:topic eliozo:Divisibility`.
  Teksto reikšmės rašomos kabutėse: `?p eliozo:domain "NT"`.
* Tekstai turi kalbos žymes. Norint naudoti tik latvišką tekstą:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Išplėstinė paieška rodo `?problemID` reikšmes; `?section` ir `?subsection` jas
  sugrupuoja po paantraštėmis.

Pavyzdys: 5–7 klasių uždaviniai apie dalumą (tema `Divisibility` ir viskas po ja),
sugrupuoti pagal temas:

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

Daugiau pavyzdžių yra meniu „Paruoštos užklausos“ virš užklausos lauko.

## Iš kur gaunami duomenys

Klasifikatoriai tvarkomi Eliozo metaduomenų skaičiuoklėse ir eksportuojami į Turtle
failus (`worksheet-generation-with-llms/scripts/setup/resources`); uždaviniai
konvertuojami iš uždavinių saugyklų Markdown failų. Žymės uždaviniams priskiriamos jų
Markdown šaltinyje, pavyzdžiui, `* topic:Divisibility`.

Susiję standartai: temos palyginamos su
[2020 Mathematics Subject Classification](https://mathscinet.ams.org/mathscinet/msc/msc2020.html)
(MSC2020), o hierarchijos sudarytos pagal tezaurų standartą ISO 25964 (viršūnė, kuri
tik grupuoja vaikines viršūnes, yra *kategorija* ir uždaviniams nepriskiriama).
