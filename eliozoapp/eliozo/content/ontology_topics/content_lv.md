# Temati

**Temats** nosauc teorijas daļu, ko izmanto atrisinājums: dalāmība, līdzīgi
trijstūri, ieslēgšanas-izslēgšanas princips. Temati atbild uz jautājumu *par ko
matemātiski ir šis uzdevums?* Skatīt arī [ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Topic` |
| Uzdevuma īpašība | `eliozo:topic`, vērtība ir temata virsotne, piem., `eliozo:Divisibility` |
| Apjoms | 637 temati līdz pieciem līmeņiem |
| Pārlūkot | [Kārtot > pēc tēmas](/topics), [tēmu tabula](/topics_table) |

## Temata īpašības

| Īpašība | Vērtība | Piemērs |
|---|---|---|
| `eliozo:topicID` | ID, tāds pats kā virsotnes nosaukums | `"IntegerCongruence"` |
| `eliozo:topicName` | nosaukums latviski | `"Kongruence pēc moduļa"` |
| `eliozo:topicDescription` | apraksts latviski | |
| `eliozo:topicNumber` | vieta kokā | `"4.4.0.0.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L5` | tā pati vieta veselos skaitļos | `4`, `4`, `0`, `0`, `0` |
| `skos:broader` / `skos:narrower` | vecākā / bērnu virsotnes | `eliozo:NumTheory` |

Četri augšējā līmeņa temati ir `Algebra` (1), `Combinatorics` (2), `Geometry` (3) un
`NumTheory` (4). Uzdevumiem birkas piešķir jebkurā līmenī — no paša `NumTheory` līdz
šauriem tematiem, piemēram, `ChineseRemainderTheorem`.

Krātuvē ir arī otrs, atsevišķs tematu koks, kas importēts no
[problems.ru](https://problems.ru): arī tā virsotnes ir `eliozo:Topic`, taču tām ir
`eliozo:topicTitle` un `skos:topicUrl`, nevis `eliozo:topicNumber`, un uz tām
neattiecas neviens uzdevums. Lai paturētu tikai galveno koku, pievienojiet šablonam
`eliozo:topicNumber ?n`.

## Piemēri

Uzdevumi par kongruencēm (`IntegerCongruence` un visi temati zem tā), sagrupēti pēc
šaurākā temata: [atvērt vaicājumu](/advanced_search?queryLabel=onto-topic-congruence).

Uzdevumi, kuriem ir temats, bet vēl nav [metodes](/content/ontology_methods),
sagrupēti pēc augšējā līmeņa temata: [atvērt vaicājumu](/advanced_search?queryLabel=onto-topic-without-method).

Saistīts: tematam bieži ir tipiskas [metodes](/content/ontology_methods);
[žanri](/content/ontology_genres) un [jēdzieni](/content/ontology_concepts) atsaucas
uz tipiskiem tematiem.
