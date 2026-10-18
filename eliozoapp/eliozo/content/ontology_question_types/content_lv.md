# Jautājumu tipi

**Jautājuma tips** pasaka, kāda veida atbildi prasa uzdevums, un līdz ar to — kas
jāietver pilnā atrisinājumā: "atrast visus" prasa atrisinājumus *un* pierādījumu, ka
citu nav; "atrast lielāko" prasa piemēru *un* novērtējumu. Skatīt arī
[ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Question` |
| Uzdevuma īpašība | `eliozo:questionType`, vērtība ir ID kā **teksts**, piem., `"FindAll"` |
| Apjoms | 15 jautājumu tipi divos līmeņos |
| Pārlūkot | [Filtri](/filter) (pēc jautājuma tipa) |

## Jautājumu tipi

| ID | Vecākais | Nozīme |
|---|---|---|
| `Find` | | atrast vai aprēķināt |
| `FindAll` | `Find` | atrast visus objektus ar īpašību (un parādīt, ka citu nav) |
| `FindValue` | `Find` | aprēķināt vērtību |
| `FindCount` | `Find` | saskaitīt |
| `FindOptimal` | | atrast lielāko/mazāko: piemērs un novērtējums |
| `Prove` | | pierādīt |
| `FindExample` | `Prove` | konstruēt piemēru |
| `ProveExistence` | `Prove` | pierādīt eksistenci |
| `ProveUniversal` | `Prove` | pierādīt apgalvojumu visiem gadījumiem |
| `Decide` | | noskaidrot: ir vai nav |
| `DecideExistence` | `Decide` | "vai eksistē?" |
| `DecideUniversal` | `Decide` | "vai vienmēr?" |
| `DecideWinner` | `Decide` | "kurš uzvar?" |
| `Algorithm` | | aprakstīt algoritmu vai stratēģiju |
| `ShortAnswer` | | tikai atbilde, bez pamatojuma |

Jautājuma tipa virsotnei ir `eliozo:questionID`, `eliozo:questionName` (latviski),
`eliozo:questionDescription`, `eliozo:questionNumber` (`"1.1"`), `eliozo:sorter_L1`,
`eliozo:sorter_L2` un `skos:broader`. Daudziem uzdevumiem vēl ir vecā vērtība
`"ProveDisprove"` ("pierādīt vai apgāzt"), kas aptuveni atbilst grupai `Decide`.

## Piemēri

"Atrast visus" uzdevumi skaitļu teorijā:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType "FindAll" ;
         eliozo:domain "NT" .
    }
    ORDER BY ?problemID

Tā kā uzdevumā ID glabājas kā teksts, ar vārdnīcu to savieno caur
`eliozo:questionID`, piemēram, lai visus grupas `Find` uzdevumus sagrupētu pēc tipa:

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

Saistīts: jautājuma tips ir uzdevuma formulējuma slānī blakus
[žanriem](/content/ontology_genres) un [jēdzieniem](/content/ontology_concepts); tas
norāda uz tipiskām [metodēm](/content/ontology_methods).
