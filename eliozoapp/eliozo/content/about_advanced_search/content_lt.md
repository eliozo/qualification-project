# Apie išplėstinę paiešką

Puslapyje [Išplėstinė paieška](/advanced_search) uždavinius galima atrinkti SPARQL
užklausomis tiesiai iš Eliozo RDF grafo. Grafo sąvokos (sąlygos ir sprendimai,
klasifikatoriai, hierarchijos ir pavadinimų konvencijos) aprašytos puslapyje
[Įvadas į ontologiją](/ontology); čia surinkta tai, ko reikia užklausoms rašyti.

## Vardų erdvės

Visi toliau vartojami pavadinimai priklauso dviem vardų erdvėms: priešdėlis `eliozo:`
žymi mokyklinių varžybų matematikai būdingus išteklių tipus, savybes ir jų reikšmes;
`skos:` — ryšius klasifikatorių hierarchijose (pavyzdžiui, tema „kvadratinė funkcija“
yra siauresnė už temą „algebra“). Tipinė užklausa prasideda šiais priešdėlių apibrėžimais:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>

## Uždavinio viršūnė

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:problemID` | tekstas | `"LV.AMO.2019.7.4"` |
| `eliozo:problemText` | Markdown, po vieną kiekvienam vertimui, su kalbos žyma | `"Andris apgalvo, ..."@lv` |
| `eliozo:problemTextHtml` | tas pats tekstas HTML formatu | |
| `eliozo:olympiad` | olimpiados ID | `"LV.AMO"` |
| `eliozo:olympiadCode`, `eliozo:country` | šio ID dalys | `"AMO"`, `"LV"` |
| `eliozo:event` | vienas olimpiados turas | `"LV.AMO.2019"` |
| `eliozo:problemYear`, `eliozo:problemGrade` | sveikieji skaičiai | `2019`, `7` |
| `eliozo:suggestedGrade` | sveikasis skaičius, gali kartotis | `7` |
| `eliozo:olympiadType` | tekstas | `"National"`, `"RegionalOrOpen"`, `"TeamSelection"`, `"International"`, `"Contest"`, `"Book"` |
| `eliozo:domain` | sritis (viršutinis žanrų lygis) | `"Alg"`, `"Comb"`, `"Geom"`, `"NT"` |
| `eliozo:subdomain` | žanras | `eliozo:DOM_GridCut` |
| `eliozo:topic` | tema | `eliozo:Divisibility` |
| `eliozo:method` | metodas | `eliozo:MTH_InvariantMethod` |
| `eliozo:concepts` | sąvoka | `eliozo:TRM-divisibility` |
| `eliozo:questionType` | klausimo tipas | `"QTY_FindAll"` |
| `eliozo:problemSolution` | sprendimo viršūnė | |
| `eliozo:hasVideo` | vaizdo įrašo viršūnė | |
| `eliozo:answer` | trumpas atsakymas | `"1"` |
| `eliozo:seeAlso`, `eliozo:sameAs` | giminingų ar tapačių uždavinių ID | `"LV.AMO.2023.6.1"` |
| `eliozo:problemBook`, `eliozo:problemBookSection` | uždaviniams iš knygų | `"BBK2012"`, `"P1"` |

Ne kiekvienas uždavinys turi visas savybes: daugelis uždavinių dar neturi temos, metodo
ar sąvokų.

**Sprendimai** (`eliozo:Solution`) turi `eliozo:solutionText` (Markdown su kalbos žyma),
`eliozo:solutionTextHtml` ir `eliozo:solutionNum`. **Vaizdo įrašai** (`eliozo:Video`)
turi `eliozo:videoTitle`, `eliozo:videoYoutube` ir `eliozo:videoBookmarks` —
`eliozo:VideoBookmark` viršūnių sąrašą su `eliozo:videoBookmarkTstamp` (sekundės) ir
`eliozo:videoBookmarkText`.

## Automatiškai pasiūlytos žymos

Savybės, kurių pavadinimas prasideda pabraukimo ženklu, yra pasiūlytos kalbos modelio ir
nepatikrintos. Jų reikšmės yra paprastas tekstas, o ne klasifikatorių viršūnės:

| Savybė | Reikšmių pavyzdžiai |
|---|---|
| `eliozo:_hasSolutionConcept` | `"DivisibilityRelation"`, `"Invariant"`, `"LatticeGrid"` |
| `eliozo:_hasReasoningMethod` | `"ConstructiveExampleForExistence"`, `"CaseAnalysis"` |
| `eliozo:_hasReasoningMistake` | `"FromSpecialToGeneral"` |
| `eliozo:_readingDifficulty` | `"low"`, `"medium"`, `"high"` |
| `eliozo:_mistakesFit` | `"low"`, `"medium"`, `"high"` |

Jos apima gerokai daugiau uždavinių nei patikrinti klasifikatoriai, todėl tinka
kandidatams ieškoti, tačiau rezultatus reikia patikrinti.

## Užklausų rašymas

* Klasifikatoriaus viršūnė rašoma kaip pavadinimas: `?p eliozo:topic eliozo:Divisibility`.
  Tekstinės reikšmės rašomos kabutėse: `?p eliozo:domain "NT"`.
* Norint rasti viską, kas yra po kuria nors hierarchijos viršūne, naudojamas savybių
  kelias: `?t skos:broader* eliozo:Divisibility` atitinka ir patį `Divisibility`, ir
  kiekvieną po juo esančią viršūnę.
* Savybėms, kurių uždavinys gali neturėti, naudokite `OPTIONAL { ... }`.
* Tekstai turi kalbos žymas. Norint naudoti tik latvišką tekstą:
  `FILTER (LANGMATCHES(LANG(?text), "lv"))`.
* Išplėstinė paieška rodo `?problemID` reikšmes; `?section` ir `?subsection` jas
  sugrupuoja po paantraštėmis.

## Pavyzdžiai

Kiekviena nuoroda atveria išplėstinę paiešką ir iškart įvykdo užklausą; ją ten galima
redaguoti ir paleisti dar kartą. Visos šios užklausos yra ir meniu
„Paruoštos užklausos > Ontologija“ virš užklausos lauko, o kiti pavyzdžiai — to paties
meniu punktuose „Pavyzdžiai“, „Uždavinių tipai“ ir „Teorijos temos“.

* 5–7 klasių uždaviniai apie dalumą (tema `Divisibility` ir viskas po ja), sugrupuoti
  pagal temas: [atverti užklausą](/advanced_search?queryLabel=onto-divisibility-grades-5-7).
* [Temos](/content/ontology_topics):
  [lyginiai](/advanced_search?queryLabel=onto-topic-congruence),
  [uždaviniai su tema, bet be metodo](/advanced_search?queryLabel=onto-topic-without-method).
* [Metodai](/content/ontology_methods):
  [invariantai pagal rūšį](/advanced_search?queryLabel=onto-method-invariants),
  [indukcija 9–12 klasėms](/advanced_search?queryLabel=onto-method-induction).
* [Žanrai](/content/ontology_genres):
  [langelių tinkleliai pagal klases](/advanced_search?queryLabel=onto-genre-grid-by-grade),
  [langelių tinkleliai pagal temą](/advanced_search?queryLabel=grid-problems),
  [geometrijos žanrai](/advanced_search?queryLabel=onto-genre-geometry).
* [Klausimų tipai](/content/ontology_question_types):
  [„rasti visus“ skaičių teorijoje](/advanced_search?queryLabel=onto-qtype-find-all-nt),
  [grupė „rasti“ pagal tipą](/advanced_search?queryLabel=onto-qtype-find-group),
  [pasirenkami atsakymai su „rasti didžiausią“](/advanced_search?queryLabel=onto-qtype-find-optimal-choice).
* [Sąvokos](/content/ontology_concepts):
  [dalumas ir pirminiai skaičiai](/advanced_search?queryLabel=onto-concept-divisibility-primes),
  [uždaviniai pagal sąvoką](/advanced_search?queryLabel=onto-concept-by-term),
  [pasiūlyta sąvoka „Invariant“](/advanced_search?queryLabel=onto-concept-suggested-invariant).
* [Olimpiados](/content/ontology_olympiads):
  [AMO 5 klasė nuo 2020 m.](/advanced_search?queryLabel=onto-olympiad-amo-grade-5),
  [valstybinių olimpiadų geometrija](/advanced_search?queryLabel=onto-olympiad-national-geometry).

## Iš kur gaunami duomenys

Klasifikatoriai saugomi Eliozo metaduomenų skaičiuoklėse ir eksportuojami į Turtle
failus (`worksheet-generation-with-llms/scripts/setup/resources`); uždaviniai
konvertuojami iš uždavinių saugyklų Markdown failų. Uždaviniams žymos priskiriamos jų
Markdown šaltinyje, pavyzdžiui, `* topic:Divisibility`.
