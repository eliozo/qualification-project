# Temos

**Tema** įvardija teorijos dalį, kurią naudoja sprendimas: dalumas, panašieji
trikampiai, įtraukimo ir atmetimo principas. Temos atsako į klausimą *apie ką
matematiškai yra šis uždavinys?* Žr. taip pat [ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Topic` |
| Uždavinio savybė | `eliozo:topic`, reikšmė yra temos viršūnė, pvz., `eliozo:Divisibility` |
| Apimtis | 637 temos iki penkių lygių |
| Naršyti | [Rikiuoti > pagal temą](/topics), [temų lentelė](/topics_table) |

## Temos savybės

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:topicID` | ID, toks pat kaip viršūnės pavadinimas | `"IntegerCongruence"` |
| `eliozo:topicName` | pavadinimas latviškai | `"Kongruence pēc moduļa"` |
| `eliozo:topicDescription` | aprašymas latviškai | |
| `eliozo:topicNumber` | vieta medyje | `"4.4.0.0.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L5` | ta pati vieta sveikaisiais skaičiais | `4`, `4`, `0`, `0`, `0` |
| `skos:broader` / `skos:narrower` | tėvinė / vaikinės viršūnės | `eliozo:NumTheory` |

Keturios viršutinio lygio temos yra `Algebra` (1), `Combinatorics` (2), `Geometry` (3)
ir `NumTheory` (4). Uždaviniams žymės priskiriamos bet kuriame lygyje — nuo paties
`NumTheory` iki siaurų temų, pavyzdžiui, `ChineseRemainderTheorem`.

Saugykloje yra ir antras, atskiras temų medis, importuotas iš
[problems.ru](https://problems.ru): jo viršūnės taip pat yra `eliozo:Topic`, bet turi
`eliozo:topicTitle` ir `skos:topicUrl` vietoj `eliozo:topicNumber`, ir į jas nenurodo
nė vienas uždavinys. Norėdami palikti tik pagrindinį medį, pridėkite prie šablono
`eliozo:topicNumber ?n`.

## Pavyzdžiai

Uždaviniai apie lyginius (`IntegerCongruence` ir visos temos po ja), sugrupuoti pagal
siauriausią temą:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:topic ?topic .
      ?topic skos:broader* eliozo:IntegerCongruence ;
             eliozo:topicName ?name .
    }
    ORDER BY ?name ?problemID

Uždaviniai, kurie turi temą, bet dar neturi [metodo](/content/ontology_methods),
sugrupuoti pagal viršutinio lygio temą:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?rootName AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:topic ?topic .
      ?topic skos:broader* ?root .
      ?root eliozo:topicName ?rootName .
      FILTER NOT EXISTS { ?root skos:broader ?anyParent }
      FILTER NOT EXISTS { ?p eliozo:method ?anyMethod }
    }
    ORDER BY ?rootName ?problemID

Susiję: tema dažnai turi tipinius [metodus](/content/ontology_methods);
[žanrai](/content/ontology_genres) ir [sąvokos](/content/ontology_concepts) nurodo
tipines temas.
