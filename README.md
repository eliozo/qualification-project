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


# Studentu personas datu apstrādei noderīgi standarti

1. **IMS Global Learning Consortium**: This is a non-profit collaborative group that develops and promotes interoperability standards, such as Learning Tools Interoperability (LTI) and Learning Information Services (LIS), to support the integration of diverse learning content, tools, and services.

2. **Open Badges specification**: This is a standard for recognizing and verifying learning based on specific achievements or skills, including through competitions or online academies. It implements privacy-aware features, such as the ability to include detailed data about the achievement while encrypting or anonymizing learner-identifying information.

3. **W3C's Verifiable Claims Working Group**: This group is developing open standards, such as Decentralized Identifiers (DIDs), for expressing and verifying credentials that respect user privacy and control.

4. **GDPR**: The EU General Data Protection Regulation and its privacy principles provide crucial guidance about data protection that all LMS and competition organizers should comply, including data minimization, clear consent requirements, pseudonymization, and access controls.

5. **Student Data Privacy Consortium (SPDC)**: An international community-driven organization that has crafted a suite of tools called the Student Data Privacy Accountability System (SDPAS) to assist in the privacy management and policy compliance process.

6. **Civil Rights, Equity, and Inclusion (CREI) Working Group**: CREI focuses on the development of open standards and best practices to promote civil rights, accessibility, and inclusion in IMS standards and in the wider EdTech community.
