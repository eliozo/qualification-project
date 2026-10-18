# Klausimų tipai

**Klausimo tipas** nurodo, kokio atsakymo prašo uždavinys, taigi ir tai, ką turi
apimti pilnas sprendimas: „rasti visus“ reikalauja sprendinių *ir* įrodymo, kad kitų
nėra; „rasti didžiausią“ reikalauja pavyzdžio *ir* įverčio. Žr. taip pat
[ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Question` |
| Uždavinio savybė | `eliozo:questionType`, reikšmė yra ID kaip **tekstas**, pvz., `"FindAll"` |
| Apimtis | 15 klausimų tipų dviejuose lygiuose |
| Naršyti | [Filtrai](/filter) (pagal klausimo tipą) |

## Klausimų tipai

| ID | Tėvinis | Reikšmė |
|---|---|---|
| `Find` | | rasti arba apskaičiuoti |
| `FindAll` | `Find` | rasti visus objektus su savybe (ir parodyti, kad kitų nėra) |
| `FindValue` | `Find` | apskaičiuoti reikšmę |
| `FindCount` | `Find` | suskaičiuoti |
| `FindOptimal` | | rasti didžiausią/mažiausią: pavyzdys ir įvertis |
| `Prove` | | įrodyti |
| `FindExample` | `Prove` | sukonstruoti pavyzdį |
| `ProveExistence` | `Prove` | įrodyti egzistavimą |
| `ProveUniversal` | `Prove` | įrodyti teiginį visiems atvejams |
| `Decide` | | išsiaiškinti, ar taip, ar ne |
| `DecideExistence` | `Decide` | „ar įmanoma?“ |
| `DecideUniversal` | `Decide` | „ar visada?“ |
| `DecideWinner` | `Decide` | „kas laimi?“ |
| `Algorithm` | | aprašyti algoritmą ar strategiją |
| `ShortAnswer` | | tik atsakymas, be pagrindimo |

Klausimo tipo viršūnė turi `eliozo:questionID`, `eliozo:questionName` (latviškai),
`eliozo:questionDescription`, `eliozo:questionNumber` (`"1.1"`), `eliozo:sorter_L1`,
`eliozo:sorter_L2` ir `skos:broader`. Daugelis uždavinių dar turi senąją reikšmę
`"ProveDisprove"` („įrodyti arba paneigti“), kuri apytiksliai atitinka grupę `Decide`.

## Pavyzdžiai

„Rasti visus“ uždaviniai skaičių teorijoje:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType "FindAll" ;
         eliozo:domain "NT" .
    }
    ORDER BY ?problemID

Kadangi uždavinyje ID saugomas kaip tekstas, su žodynu jis susiejamas per
`eliozo:questionID`, pavyzdžiui, norint visus grupės `Find` uždavinius sugrupuoti pagal
tipą:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT ?problemID (?type AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType ?type .
      ?q eliozo:questionID ?type ;
         skos:broader* eliozo:Find .
    }
    ORDER BY ?type ?problemID

Susiję: klausimo tipas yra uždavinio formuluotės sluoksnyje šalia
[žanrų](/content/ontology_genres) ir [sąvokų](/content/ontology_concepts); jis nurodo
tipinius [metodus](/content/ontology_methods).
