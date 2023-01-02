# SPARQL vaicājumi


## Atlasa prasmes, uzdevuma gadu un sašķirots no zemākā gada uz augstāko

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eozol: <http://www.dudajevagatve.lv/eozol#>
SELECT ?sub WHERE {
?sub eozol:skill "alg.tra.binom.square" ;
     eozol:year ?year
} ORDER BY ASC(?year)
```

## Atlasa prasmes, uzdevuma gadu un tekstu un sašķirots no zemākā gada uz augstāko

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eozol: <http://www.dudajevagatve.lv/eozol#>
SELECT ?sub ?text WHERE {
?sub eozol:skill "alg.tra.binom.square" ;
     eozol:year ?year ;
     eozol:text ?text
} ORDER BY ASC(?year)
```

## Atrod uzdevumus ar "alg.expr" prasmi no visām olimpiādēm

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#> 
SELECT ?problemid ?text WHERE {
?sub eozol:problemid ?problemid .
?sub eozol:skill "alg.expr" .
?sub eozol:text ?text .
} ORDER BY ?obj
```

## Atrod uzdevumus, kas ir apakšprasmes prasmei "alg"

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT ?skillID WHERE {
?alg skos:prefLabel "alg" . ?skillID skos:broader ?alg
}
```

## Atrod uzdevumus, kas ir apakšprasmes prasmei "alg" un sašķiro pēc uzdevumiem alfabēta secībā

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT ?skillID ?desc WHERE {
?alg skos:prefLabel "alg" . ?skillID skos:broader ?alg ; skos:skillDescription ?desc
}
```

## Atrod visas prasmes un apakšprasmes zem algebras

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
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
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT ?problem ?child
WHERE {
    ?parent skos:prefLabel "alg.tra" .
    ?parent skos:narrower+ ?child .
    ?problem eozol:skill ?child .
}
```

## Atrod sakārtotas prasmes, kuras ir zem algebras

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT ?parent_skill_id ?child WHERE {
  ?parent_skill_id skos:prefLabel "alg" .
  ?child skos:broader+ ?parent_skill_id .
  ?child eozol:skillNumber ?child_num .
} ORDER BY ?child_num
```

## Atlasa visas unikālās olimpiādes un valsti

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT DISTINCT ?country ?olympiad
WHERE {
    ?problem eozol:country ?country ; eozol:olympiad ?olympiad .
}
```

## Atlasa visus gadus un klases secīgi pēc konkrētas olimpiādes

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT DISTINCT ?year ?grade
WHERE {
    ?problem eozol:country 'LV' ; eozol:olympiad 'AO' ;
    eozol:year ?year ;
    eozol:grade ?grade .
} ORDER BY ?year ?grade
```

## Atlasa prasmes identifikatoru, prasmes numuru un prasmes aprakstu un sakārto pēc prasmes numura

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription
WHERE { 
?obj eozol:skillIdentifier ?skillIdentifier .
?obj eozol:skillNumber ?skillNumber .
?obj eozol:skillDescription ?skillDescription .
} ORDER BY ?skillNumber
```

## Atlasa prasmes identifikatoru, prasmes numuru, prasmes aprakstu un uzdevuma id un sakārto pēc prasmes numura

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription ?problemid WHERE { 
  ?skill eozol:skillIdentifier ?skillIdentifier .
  ?skill eozol:skillNumber ?skillNumber .
  ?skill eozol:skillDescription ?skillDescription .
  OPTIONAL {?prob eozol:skill ?skill . ?prob eozol:problemid ?problemid . }.
} ORDER BY ?skillNumber
```

## Atlasa specifisku uzdevuma id

Atlasa neobligātos atribūtus - uzdevuma tekstu, gadu, olimpiādi, klasi, valsti, prasmi un prasmes identifikatoru

``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eozol:<http://www.dudajevagatve.lv/eozol#>
SELECT * WHERE {
  ?problem eozol:problemid 'LV.AO.2013.8.1' .
  OPTIONAL {
    ?problem eozol:text ?text ;
             eozol:year ?year ;
             eozol:olympiad ?olympiad ;
             eozol:grade ?grade ;
             eozol:country ?country ;
             eozol:skill ?skill .
    ?skill eozol:skillIdentifier ?skillIdentifier .
  }.
}
```