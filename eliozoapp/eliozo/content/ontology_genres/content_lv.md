# Žanri

**Žanrs** apraksta, kā uzdevums izskatās no ārpuses, pirms to atrisina: teksta
uzdevums, rūtiņu figūras sagriešana, turnīrs, svēršana, vienādojums veselos
skaitļos. Viena žanra uzdevumiem ir kopīgs "sižets", pat ja tos risina dažādi.
Skatīt arī [ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Domain` (klasei saglabāts vecais nosaukums) |
| Uzdevuma īpašības | `eliozo:domain`: augšējais līmenis kā teksts, `"Alg"`, `"Comb"`, `"Geom"` vai `"NT"`; `eliozo:subdomain`: žanra virsotne, piem., `eliozo:DOM_GridCut` |
| Apjoms | 80 žanri trīs līmeņos; ID zem augšējā līmeņa sākas ar `DOM_` |
| Pārlūkot | [Kārtot > pēc žanra](/genres), [Filtri](/filter) (pēc nozares) |

## Žanra īpašības

| Īpašība | Vērtība | Piemērs |
|---|---|---|
| `eliozo:domainID` | ID, tāds pats kā virsotnes nosaukums | `"DOM_Triangles"` |
| `eliozo:domainName` | nosaukums latviski | `"Trijstūri"` |
| `eliozo:domainDescription` | apraksts latviski | |
| `eliozo:domainNumber` | vieta kokā | `"3.4.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L3` | tā pati vieta veselos skaitļos | `3`, `4`, `0` |
| `skos:broader` / `skos:narrower` | vecākā / bērnu virsotnes | `eliozo:Geom` |

Augšējais līmenis:

| ID (`eliozo:domain`) | Žanrs | Piemēri zem tā |
|---|---|---|
| `Alg` | algebra | `DOM_WordProblems`, `DOM_Equations`, `DOM_Inequalities` |
| `Comb` | kombinatorika | `DOM_CountingObjects`, `DOM_Graphs`, `DOM_GridCut` |
| `Geom` | ģeometrija | `DOM_Triangles`, `DOM_IntegerLattices` |
| `NT` | skaitļu teorija | `DOM_NumeralSystems`, `DOM_NumericConstructions` |

Ievērojiet atšķirību: `eliozo:domain` ir **teksts** un satur tikai augšējo līmeni,
bet `eliozo:subdomain` ir hierarhijas **virsotne**.

## Piemēri

Uzdevumi par rūtiņu režģiem (visi žanri 3.16.x), sagrupēti pa klasēm: [atvērt vaicājumu](/advanced_search?queryLabel=onto-genre-grid-by-grade). Tie paši uzdevumi, sagrupēti pa žanriem: [atvērt vaicājumu](/advanced_search?queryLabel=grid-problems).

Visi ģeometrijas žanri ar to uzdevumiem, divos apakšvirsrakstu līmeņos: [atvērt vaicājumu](/advanced_search?queryLabel=onto-genre-geometry).

Saistīts: žanri atsaucas uz saviem tipiskajiem [tematiem](/content/ontology_topics)
un [modeļiem](/content/ontology_models).
