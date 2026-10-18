# Modeļi

**Modelis** ir matemātiskā struktūra, ko risinātājs uzbūvē, lai uzdevumu atrisinātu:
lineāra sakarība starp lielumiem, "ceļš = ātrums × laiks", pazīšanās grafs, atlikumu
tabula. [Klasifikatoru grafā](/ontology) modelis ir tilts starp uzdevuma formulējumu
un atrisinājumu: noteikta [žanra](/content/ontology_genres) uzdevumu pārtulko
modelī, un modeli tālāk apstrādā ar [metodi](/content/ontology_methods) un
[temata](/content/ontology_topics) teoriju.

**Statuss: plānots.** Modeļu saraksts ir izveidots, taču modeļu vēl nav RDF krātuvē
un uzdevumiem tie vēl nav piešķirti, tāpēc vaicājumos tos vēl nevar izmantot.

## Modeļu saraksts

Ap 135 modeļu, kuru ID sākas ar `MDL_`, piemēram:

| ID | Modelis |
|---|---|
| `MDL_LinearRelationBetweenQuantities` | lineāra sakarība starp lielumiem |
| `MDL_DistanceTimeSpeed` | ceļš = ātrums × laiks |
| `MDL_ProportionsAndRatios` | proporcijas un attiecības |
| `MDL_PercentagesAsRatios` | procenti kā attiecības un izmaiņas |
| `MDL_ParityInvariant` | paritātes invariants |
| `MDL_PairingStrategyInGames` | pārošanas stratēģija spēlēs |

Katram modelim ir nosaukums latviski un angliski, apraksts latviski, nozare (`Alg`,
`Comb`, `Geom`, `NT`), jēdzienu grupa, klašu līmenis un atsauces:

* `MethodRef`: [metode](/content/ontology_methods), ko modelim parasti lieto,
  piem., `MTH_AlgebraicModel`;
* `TopicRefs`: saistītie [temati](/content/ontology_topics);
* `ConceptRefs`: [jēdzieni](/content/ontology_concepts), no kuriem modelis veidots.

Saraksts tiek uzturēts Eliozo metadatu izklājlapas cilnē "models".
