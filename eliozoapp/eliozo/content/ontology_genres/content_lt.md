# Žanrai

**Žanras** aprašo, kaip uždavinys atrodo iš išorės, dar prieš jį sprendžiant:
tekstinis uždavinys, langelių figūros karpymas, turnyras, svėrimas, lygtis sveikaisiais
skaičiais. To paties žanro uždaviniai turi bendrą „siužetą“, net jei sprendžiami
skirtingai. Žr. taip pat [ontologijos apžvalgą](/ontology).

| | |
|---|---|
| Klasė | `eliozo:Domain` (klasė išlaikė senąjį pavadinimą) |
| Uždavinio savybės | `eliozo:domain`: viršutinis lygis kaip tekstas, `"Alg"`, `"Comb"`, `"Geom"` arba `"NT"`; `eliozo:subdomain`: žanro viršūnė, pvz., `eliozo:DOM_GridCut` |
| Apimtis | 80 žanrų trijuose lygiuose; ID žemiau viršutinio lygio prasideda `DOM_` |
| Naršyti | [Rikiuoti > pagal žanrą](/genres), [Filtrai](/filter) (pagal sritį) |

## Žanro savybės

| Savybė | Reikšmė | Pavyzdys |
|---|---|---|
| `eliozo:domainID` | ID, toks pat kaip viršūnės pavadinimas | `"DOM_Triangles"` |
| `eliozo:domainName` | pavadinimas latviškai | `"Trijstūri"` |
| `eliozo:domainDescription` | aprašymas latviškai | |
| `eliozo:domainNumber` | vieta medyje | `"3.4.0"` |
| `eliozo:sorter_L1` ... `eliozo:sorter_L3` | ta pati vieta sveikaisiais skaičiais | `3`, `4`, `0` |
| `skos:broader` / `skos:narrower` | tėvinė / vaikinės viršūnės | `eliozo:Geom` |

Viršutinis lygis:

| ID (`eliozo:domain`) | Žanras | Pavyzdžiai po juo |
|---|---|---|
| `Alg` | algebra | `DOM_WordProblems`, `DOM_Equations`, `DOM_Inequalities` |
| `Comb` | kombinatorika | `DOM_CountingObjects`, `DOM_Graphs`, `DOM_GridCut` |
| `Geom` | geometrija | `DOM_Triangles`, `DOM_IntegerLattices` |
| `NT` | skaičių teorija | `DOM_NumeralSystems`, `DOM_NumericConstructions` |

Atkreipkite dėmesį į skirtumą: `eliozo:domain` yra **tekstas** ir turi tik viršutinį
lygį, o `eliozo:subdomain` yra hierarchijos **viršūnė**.

## Pavyzdžiai

Langelių figūrų karpymo uždaviniai, sugrupuoti pagal klases:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?problemID ?grade (CONCAT(STR(?grade), " klasė") AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:problemGrade ?grade ;
         eliozo:subdomain eliozo:DOM_GridCut .
    }
    ORDER BY ?grade ?problemID

Visi geometrijos žanrai su jų uždaviniais, dviem paantraščių lygiais:

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

Susiję: žanrai nurodo savo tipines [temas](/content/ontology_topics) ir
[modelius](/content/ontology_models).
