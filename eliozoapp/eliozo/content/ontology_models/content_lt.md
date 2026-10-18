# Modeliai

**Modelis** yra matematinė struktūra, kurią sprendėjas sukuria, kad išspręstų
uždavinį: tiesinis ryšys tarp dydžių, „kelias = greitis × laikas“, pažinčių grafas,
liekanų lentelė. [Klasifikatorių grafe](/ontology) modelis yra tiltas tarp uždavinio
formuluotės ir sprendimo: tam tikro [žanro](/content/ontology_genres) uždavinys
išverčiamas į modelį, o modelis toliau nagrinėjamas [metodu](/content/ontology_methods)
ir [temos](/content/ontology_topics) teorija.

**Būsena: planuojama.** Modelių sąrašas sudarytas, tačiau modelių dar nėra RDF
saugykloje ir uždaviniams jie dar nepriskirti, todėl užklausose jų dar negalima
naudoti.

## Modelių sąrašas

Apie 135 modelius, kurių ID prasideda `MDL_`, pavyzdžiui:

| ID | Modelis |
|---|---|
| `MDL_LinearRelationBetweenQuantities` | tiesinis ryšys tarp dydžių |
| `MDL_DistanceTimeSpeed` | kelias = greitis × laikas |
| `MDL_ProportionsAndRatios` | proporcijos ir santykiai |
| `MDL_PercentagesAsRatios` | procentai kaip santykiai ir pokyčiai |
| `MDL_ParityInvariant` | lyginumo invariantas |
| `MDL_PairingStrategyInGames` | porų strategija žaidimuose |

Kiekvienas modelis turi pavadinimą latviškai ir angliškai, aprašymą latviškai, sritį
(`Alg`, `Comb`, `Geom`, `NT`), sąvokų grupę, klasių lygį ir nuorodas:

* `MethodRef`: [metodas](/content/ontology_methods), kuris modeliui paprastai
  taikomas, pvz., `MTH_AlgebraicModel`;
* `TopicRefs`: susijusios [temos](/content/ontology_topics);
* `ConceptRefs`: [sąvokos](/content/ontology_concepts), iš kurių modelis sudarytas.

Sąrašas tvarkomas Eliozo metaduomenų skaičiuoklės skirtuke „models“.
