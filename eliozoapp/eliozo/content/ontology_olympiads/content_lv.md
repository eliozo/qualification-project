# Olimpiādes

Katrs olimpiādes uzdevums pieder **olimpiādei** (sacensībām ar valsti un kodu) un
vienai no tās **kārtām** (gadam vai posmam). Skatīt arī
[ontoloģijas pārskatu](/ontology).

| | |
|---|---|
| Klase | `eliozo:Olympiad` |
| Uzdevuma īpašība | `eliozo:olympiad`, vērtība ir ID kā **teksts**, piem., `"LV.AMO"` |
| Apjoms | 17 olimpiādes |
| Pārlūkot | [Arhīvs > Olimpiādes](/olympiads) |

## Īpašības

Olimpiādes virsotnei ir `eliozo:OlympiadID` (ievērojiet lielo O, piem., `"LV.AMO"`),
`eliozo:olympiadCode` (`"AMO"`), `eliozo:olympiadCountry` (`"LV"`) un angļu, latviešu
un lietuviešu valodā `eliozo:olympiadName` un `eliozo:olympiadDescription`.

Uzdevums atkārto vajadzīgās daļas pats, tāpēc lielākajai daļai vaicājumu olimpiādes
virsotne nemaz nav jāaplūko:

| Īpašība | Piemērs |
|---|---|
| `eliozo:olympiad` | `"LV.AMO"` |
| `eliozo:olympiadCode` | `"AMO"` |
| `eliozo:country` | `"LV"` |
| `eliozo:event` | `"LV.AMO.2019"` |
| `eliozo:problemYear` | `2019` |
| `eliozo:problemGrade` | `7` |
| `eliozo:olympiadType` | `"RegionalOrOpen"` |

No šīm daļām veidots arī pats uzdevuma ID: `LV.AMO.2019.7.4` ir 2019. gada Atklātās
matemātikas olimpiādes 7. klases 4. uzdevums.

## Olimpiādes

| ID | Olimpiāde |
|---|---|
| `LV.AMO` | Latvijas Atklātā matemātikas olimpiāde |
| `LV.NOL` | Novada olimpiāde |
| `LV.SOL` | Latvijas sagatavošanās olimpiāde |
| `LV.VOL` | Latvijas valsts olimpiāde |
| `LV.TST` | Latvijas papildsacensības par vietu izlasē |
| `LT.LMMO` | Lietuvas skolēnu matemātikas olimpiāde |
| `LT.SAV` | Lietuvas skolēnu matemātikas olimpiādes pašvaldību kārta |
| `LT.LJMO` | Lietuvas jaunāko klašu matemātikas olimpiāde |
| `LT.LKMMO` | Lietuvas skolēnu komandu matemātikas olimpiāde |
| `LT.LDK` | Matemātikas sacensības Lietuvas Lielkņazistes godam |
| `LT.VUMIF` | Viļņas Universitātes MIF matemātikas olimpiāde |
| `LT.TST` | Lietuvas atlases sacensības |
| `EE.LHT` | Igaunijas atklātās matemātikas sacensības |
| `EE.PK` | Igaunijas matemātikas olimpiādes reģionu kārta |
| `EE.LO` | Igaunijas olimpiādes noslēguma kārta |
| `EE.TST` | Igaunijas atlases sacensības |
| `WW.IMOSHL` | Starptautiskā matemātikas olimpiāde (IMO), īsais saraksts |

## Piemēri

Atklātās olimpiādes 5. klases uzdevumi kopš 2020. gada, sagrupēti pa gadiem:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (STR(?year) AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:olympiad "LV.AMO" ;
         eliozo:problemYear ?year ;
         eliozo:problemGrade 5 .
      FILTER (?year >= 2020)
    }
    ORDER BY DESC(?year) ?problemID

Visu valsts olimpiāžu ģeometrijas uzdevumi ar olimpiādes latvisko nosaukumu kā
apakšvirsrakstu:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID (?name AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:olympiad ?olympiad ;
         eliozo:olympiadType "National" ;
         eliozo:domain "Geom" .
      ?o eliozo:OlympiadID ?olympiad ;
         eliozo:olympiadName ?name .
      FILTER (LANG(?name) = "lv")
    }
    ORDER BY ?name ?problemID
