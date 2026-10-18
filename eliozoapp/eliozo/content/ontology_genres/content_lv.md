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

Rūtiņu figūru sagriešanas uzdevumi, sagrupēti pa klasēm:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?problemID ?grade (CONCAT(STR(?grade), ". klase") AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:subdomain eliozo:DOM_GridCut .
    }
    ORDER BY ?grade ?problemID

Visi ģeometrijas žanri ar to uzdevumiem, divos apakšvirsrakstu līmeņos:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT DISTINCT ?problemID (?parentName AS ?section) (?name AS ?subsection)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:subdomain ?genre .
      ?genre eliozo:domainName ?name ;
             skos:broader ?parent .
      ?parent skos:broader* eliozo:Geom ;
              eliozo:domainName ?parentName .
    }
    ORDER BY ?parentName ?name ?problemID

Saistīts: žanri atsaucas uz saviem tipiskajiem [tematiem](/content/ontology_topics)
un [modeļiem](/content/ontology_models).
