# Metodes

**Metode** ir atrisinājuma spriedumu šablons: matemātiskā indukcija, Dirihlē
princips, invariants, pierādījums no pretējā. Ja [temats](/content/ontology_topics)
pasaka, *kādu teoriju* izmanto, tad metode pasaka, *kā veidots spriedums*. Skatīt arī
[ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Method` |
| Uzdevuma īpašība | `eliozo:method`, vērtība ir metodes virsotne, piem., `eliozo:MTH_InvariantMethod` |
| Apjoms | 53 metodes divos līmeņos; ID sākas ar `MTH_` |
| Pārlūkot | [Kārtot > pēc metodes](/methods) |

## Metodes īpašības

| Īpašība | Vērtība | Piemērs |
|---|---|---|
| `eliozo:methodID` | ID, tāds pats kā virsotnes nosaukums | `"MTH_PigeonholePrincipleBasic"` |
| `eliozo:methodName` | nosaukums latviski | `"Dirihlē princips"` |
| `eliozo:methodDescription` | apraksts latviski | |
| `eliozo:methodNumber` | vieta kokā | `"2.1"` |
| `eliozo:sorter_L1`, `eliozo:sorter_L2` | tā pati vieta veselos skaitļos | `2`, `1` |
| `skos:broader` / `skos:narrower` | vecākā / bērnu virsotnes | `eliozo:MTH_MeanValuePrinciple` |

Deviņas metožu grupas:

| Nr. | ID | Nosaukums |
|---|---|---|
| 1 | `MTH_MathematicalInduction` | matemātiskā indukcija |
| 2 | `MTH_MeanValuePrinciple` | vidējās vērtības metode (Dirihlē princips) |
| 3 | `MTH_ExtremePrinciple` | ekstremālā elementa metode |
| 4 | `MTH_InvariantMethod` | invariantu metode |
| 5 | `MTH_ContradictionMethod` | pierādījums no pretējā |
| 6 | `MTH_InterpretationMethod` | interpretāciju metode (ģeometriskā, fizikālā, kodēšana, ...) |
| 7 | `MTH_Transformations` | izteiksmju pārveidojumi |
| 8 | `MTH_Augmentation` | struktūru papildināšana (palīgelementi) |
| 9 | `MTH_Algorithms` | algoritmiskās metodes |

Dažiem uzdevumiem ir metožu nosaukumi, kuru vārdnīcā nav (vai vairs nav).
Automātiski ieteiktā īpašība `eliozo:_hasReasoningMethod` (vienkāršs teksts, sk.
[pārskatu](/ontology)) lieto savus, sīkākus nosaukumus.

## Piemēri

Invariantu uzdevumi, sagrupēti pēc invarianta veida: [atvērt vaicājumu](/advanced_search?queryLabel=onto-method-invariants).

Indukcijas uzdevumi 9.–12. klasei, sagrupēti pa klasēm: [atvērt vaicājumu](/advanced_search?queryLabel=onto-method-induction).

Saistīts: [norāžu tipi](/content/ontology_hint_types) iesaka metodes;
[modelis](/content/ontology_models) atsaucas uz metodi, ko tam parasti lieto.
