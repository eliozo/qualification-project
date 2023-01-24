# Kvalifikācijas darbs "Zināšanu grafi matemātikas olimpiāžu uzdevumu meklēšanā"
**Autors: Elizabete Ozoliņa, LU Datorikas fakultātes 3.kursa studente**

# Apraksts 
Šī projekta ietvaros tiek izstrādāta tīmekļa vietne jeb bibliotēka, kurā ir sašķiroti matemātikas olimpiāžu uzdevumi pēc dažādiem kritērijiem.

## Darāmie darbi

NoSQL
Flutter (Dart) vs Android (Java/Kotlin/React Native)

Kas vēl jāizdara:
- Pievienot migrācijas skriptam bildes. (markdown jāizlabo hgroup) 
- Video grāmatzīmes 
- Lietotājs pats var pievienot savu SPARQL
- Test case uz new line LV.AO.2003.10.3 migracijas skripts, slikti strādā ar apakšpunktiem
- publisks flask serveris
- publisks fuseki
- notestēt LV.AO.2000.8.3 http://localhost:5000/grade?year=2000&grade=8&country=LV&olympiad=AO 
- Kā JSON pārveidojas par RDF
- Dažādu filtru pievienošana (aspektorientēts)

Idejas, kā paplašināt ontoloģiju:
- Pēc sarežģītības filtrēt uzdevumus (izsecinām grūtības pakāpi, cik olimpiādes dalībnieki savāca punktus)
- Klasificēt pēc tēmas, eozol:topic (algebra, ģeometrija utt.)
- Katrai prasmei ir anchor tasks, raksturīgākie uzdevumi prasmēm, centrālais uzdevums, sākot mācīt par kādu no prasmēm
- Katrai prasmei un tēmai ir zināma klase, no kuras sāk mācit konkrētu tēmu/prasmi eozol:startingGradeLV
- alg.tra - derētu lasāmāki prasmju nosaukum
