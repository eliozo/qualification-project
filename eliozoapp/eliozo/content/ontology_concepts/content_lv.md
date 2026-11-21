# Jēdzieni

**Jēdziens** ir matemātisks jēdziens, kas parādās uzdevuma formulējumā: pirmskaitlis,
summa, trijstūris, dalāmība. Jēdzieni palīdz atrast uzdevumus pēc to vārdu krājuma
un redzēt, kas skolēnam jāzina, lai uzdevumu izlasītu. Skatīt arī
[ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Concept` |
| Uzdevuma īpašība | `eliozo:concepts`, vērtība ir jēdziena virsotne, piem., `eliozo:TRM-divisibility` |
| Apjoms | 134 jēdzieni bez hierarhijas; virsotņu nosaukumi sākas ar `TRM-` |
| Pārlūkot | [Kārtot > pēc jēdziena](/concepts) |

## Jēdziena īpašības

| Īpašība | Vērtība | Piemērs |
|---|---|---|
| `eliozo:conceptID` | ID ar birku `@en` | `"absolute-value"@en` |
| `eliozo:termEN` | termins angliski | `"absolute value"@en` |
| `eliozo:termLV` | termins latviski | `"absolūtā vērtība"@lv` |
| `eliozo:descLV` | skaidrojums latviski (tikai dažiem jēdzieniem) | |

Tā kā `eliozo:conceptID` ir valodas birka, salīdziniet to ar `"primes"@en` vai ar
`STR(?id) = "primes"`.

Tiek gatavots plašāks jēdzienu saraksts (ap 270 jēdzienu ar CamelCase nosaukumiem,
piemēram, `PositiveIntegers`, sagrupēti un saistīti ar
[tematiem](/content/ontology_topics)); krātuvē tā vēl nav. Automātiski ieteiktā
īpašība `eliozo:_hasSolutionConcept` (vienkāršs teksts, sk. [pārskatu](/ontology))
jau lieto galvenokārt šī saraksta nosaukumus.

## Piemēri

Uzdevumi, kuros izmantota gan dalāmība, gan pirmskaitļi: [atvērt vaicājumu](/advanced_search?queryLabel=onto-concept-divisibility-primes).

Uzdevumi, sagrupēti pēc jēdzieniem, ar latvisko terminu kā apakšvirsrakstu: [atvērt vaicājumu](/advanced_search?queryLabel=onto-concept-by-term).

Uzdevumi, kuru automātiski ieteiktajos jēdzienos ir "Invariant": [atvērt vaicājumu](/advanced_search?queryLabel=onto-concept-suggested-invariant).

Saistīts: [modeļi](/content/ontology_models) atsaucas uz jēdzieniem, no kuriem tie
veidoti.
