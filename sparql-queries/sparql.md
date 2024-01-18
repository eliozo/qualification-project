# SPARQL vaicājumi


## Atlasa prasmes, uzdevuma gadu un sašķirots no zemākā gada uz augstāko

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?sub WHERE {
?sub eliozo:skill "alg.tra.binom.square" ;
     eliozo:year ?year
} ORDER BY ASC(?year)
```

## Atlasa prasmes, uzdevuma gadu un tekstu un sašķirots no zemākā gada uz augstāko

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?sub ?text WHERE {
?sub eliozo:skill "alg.tra.binom.square" ;
     eliozo:year ?year ;
     eliozo:text ?text
} ORDER BY ASC(?year)
```

## Atrod uzdevumus ar "alg.expr" prasmi no visām olimpiādēm

``` sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#> 
SELECT ?problemid ?text WHERE {
  ?sub eliozo:problemid ?problemid ;
       eliozo:skill ?skill ;
       eliozo:text ?text .
  ?skill skos:prefLabel "alg.expr" .
} ORDER BY ?problemid
```

## Atrod uzdevumus, kas ir apakšprasmes prasmei "alg"

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?skillID WHERE {
?alg skos:prefLabel "alg" . ?skillID skos:broader ?alg
}
```

## Atrod uzdevumus, kas ir apakšprasmes prasmei "alg" un sašķiro pēc uzdevumiem alfabēta secībā

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?skillID ?desc WHERE {
?alg skos:prefLabel "alg" . ?skillID skos:broader ?alg ; skos:skillDescription ?desc
}
```

## Atrod visas prasmes un apakšprasmes zem algebras

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?parent ?child
WHERE {
    ?parent skos:prefLabel "alg" .
    ?parent skos:narrower+ ?child .
}
```


## Atrod uzdevumus, kas ir apakšprasmes "alg.tra" prasmei

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?problem ?child
WHERE {
    ?parent skos:prefLabel "alg.tra" .
    ?parent skos:narrower+ ?child .
    ?problem eliozo:skill ?child .
}
```

## Atrod sakārtotas prasmes, kuras ir zem algebras

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?parent_skill_id ?child WHERE {
  ?parent_skill_id skos:prefLabel "alg" .
  ?child skos:broader+ ?parent_skill_id .
  ?child eliozo:skillNumber ?child_num .
} ORDER BY ?child_num
```

## Atlasa visas unikālās olimpiādes un valsti

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?country ?olympiad
WHERE {
    ?problem eliozo:country ?country ; eliozo:olympiad ?olympiad .
}
```

## Atlasa visus gadus un klases secīgi pēc konkrētas olimpiādes

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?year ?grade
WHERE {
    ?problem eliozo:country 'LV' ; eliozo:olympiad 'AO' ;
    eliozo:year ?year ;
    eliozo:grade ?grade .
} ORDER BY ?year ?grade
```

## Atlasa prasmes identifikatoru, prasmes numuru un prasmes aprakstu un sakārto pēc prasmes numura

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription
WHERE { 
?obj eliozo:skillIdentifier ?skillIdentifier .
?obj eliozo:skillNumber ?skillNumber .
?obj eliozo:skillDescription ?skillDescription .
} ORDER BY ?skillNumber
```

## Atlasa prasmes identifikatoru, prasmes numuru, prasmes aprakstu un uzdevuma id un sakārto pēc prasmes numura

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription ?problemid WHERE { 
  ?skill eliozo:skillIdentifier ?skillIdentifier .
  ?skill eliozo:skillNumber ?skillNumber .
  ?skill eliozo:skillDescription ?skillDescription .
  OPTIONAL {?prob eliozo:skill ?skill . ?prob eliozo:problemid ?problemid . }.
} ORDER BY ?skillNumber
```

## Atlasa specifisku uzdevuma id

Atlasa neobligātos atribūtus - uzdevuma tekstu, gadu, olimpiādi, klasi, valsti, prasmi un prasmes identifikatoru

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT * WHERE {
  ?problem eliozo:problemid 'LV.AO.2013.8.1' .
  OPTIONAL {
    ?problem eliozo:text ?text ;
             eliozo:year ?year ;
             eliozo:olympiad ?olympiad ;
             eliozo:grade ?grade ;
             eliozo:country ?country ;
             eliozo:skill ?skill .
    ?skill eliozo:skillIdentifier ?skillIdentifier .
  }.
}
```