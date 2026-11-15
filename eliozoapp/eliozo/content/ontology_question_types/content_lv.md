# Jautājumu tipi

**Jautājuma tips** pasaka, kāda veida atbildi prasa uzdevums, un līdz ar to — kādām
daļām jābūt pilnā atrisinājumā: "atrast visus" prasa atrisinājumus *un* pierādījumu, ka
citu nav; "atrast lielāko" prasa piemēru *un* novērtējumu. Jautājuma tipu nosaka pēc
šīm **nepieciešamajām daļām**, nevis pēc formulējuma vārdiem vai precīzas kvantoru
secības. Skatīt arī [ontoloģijas pārskatu](/ontology).

**Atbildes formāts** ir atsevišķa ass: tas pasaka, kādā veidā atbilde jāiesniedz un kas
tiek vērtēts (pilns atrisinājums, tikai skaitlis, izvēle no variantiem).

| | |
|---|---|
| Klase | `eliozo:Question` |
| Uzdevuma īpašība | `eliozo:questionType`, vērtība ir ID kā **teksts**, piem., `"QTY_FindAll"` |
| Otrais tips (reti) | `eliozo:questionTypeSecondary`, tāda paša veida vērtība |
| Atbildes formāts | `eliozo:responseFormat`, vērtība ir ID kā **teksts**, piem., `"RSP_AnswerNumeric"` |
| Apjoms | 14 jautājumu tipi (4 grupas, 10 apakštipi) un 10 atbildes formāti (2 grupas, 8 apakštipi) |
| Vārdnīca | `questionTypes2.csv` |
| Pārlūkot | [Filtri](/filter) (pēc jautājuma tipa) |

## Jautājumu tipi

Katram tipam ir formāls nosaukums, viens kanoniskais jautājums un saraksts ar citiem
tipiskiem formulējumiem (vārdnīcas slejas `QuestionLv` un `OtherQuestionsLv`).

| ID | Vecākais | Nosaukums | Kanoniskais jautājums | Nepieciešamās daļas |
|---|---|---|---|---|
| `QTY_Find` | | Atrast | Atrodi … | atkarīgs no apakštipa |
| `QTY_FindAll` | `QTY_Find` | Atrast visus atrisinājumus | Atrodi visus … | visas atbildes; pārbaude, ka katra der; pierādījums, ka citu nav |
| `QTY_FindValue` | `QTY_Find` | Atrast vērtību vai skaitu | Aprēķini … | vērtība vai skaits; aprēķins vai saskaitīšana ar pamatojumu |
| `QTY_FindOptimal` | `QTY_Find` | Atrast lielāko vai mazāko | Atrodi lielāko (mazāko) … | optimālā vērtība; piemērs, kas to sasniedz; novērtējums, ka labāk nevar |
| `QTY_Construct` | | Konstruēt | Parādi … | atkarīgs no apakštipa |
| `QTY_ConstructExample` | `QTY_Construct` | Konstruēt piemēru | Uzrādi piemēru … | piemērs; pārbaude, ka tas der |
| `QTY_ConstructProcedure` | `QTY_Construct` | Konstruēt procedūru | Parādi, kā … | procedūra pa soļiem; pierādījums, ka tā strādā katrā gadījumā |
| `QTY_Prove` | | Pierādīt | Pierādi, ka … | atkarīgs no apakštipa |
| `QTY_ProveExistence` | `QTY_Prove` | Pierādīt eksistenci | Pierādi, ka eksistē … | konstrukcija ar pārbaudi vai nekonstruktīvs spriedums |
| `QTY_ProveUniversal` | `QTY_Prove` | Pierādīt vispārīgu apgalvojumu | Pierādi, ka visiem … | vispārīgs spriedums, kas aptver visus gadījumus |
| `QTY_Decide` | | Noskaidrot | Vai …? | atkarīgs no apakštipa |
| `QTY_DecideExistence` | `QTY_Decide` | Noskaidrot eksistenci | Vai var …? | jā vai nē; ja jā — piemērs; ja nē — neiespējamības pierādījums |
| `QTY_DecideUniversal` | `QTY_Decide` | Noskaidrot vispārīgu apgalvojumu | Vai vienmēr …? | jā vai nē; ja jā — vispārīgs pierādījums; ja nē — pretpiemērs |
| `QTY_DecideWinner` | `QTY_Decide` | Noskaidrot uzvarētāju | Kurš uzvar, pareizi spēlējot? | uzvarētājs; stratēģija; pierādījums, ka tā atbild uz katru pretinieka gājienu |

Jautājuma tipa virsotnei ir `eliozo:questionID`, `eliozo:questionName` (latviski),
`eliozo:questionDescription`, `eliozo:questionNumber` (`"1.1"`), `eliozo:sorter_L1`,
`eliozo:sorter_L2` un `skos:broader`. Vārdnīcas jaunās slejas (kanoniskais jautājums,
citi formulējumi, nepieciešamās daļas) īpašībām vēl jāpiesaista.

## Kā izvēlēties tipu

Formulējuma vārdi tipu nenosaka viennozīmīgi: ar "Atrodi …" var sākties četri dažādi
tipi. Tipu izvēlas ar šādiem jautājumiem.

1. **Vai apgalvojuma patiesums ir dots?** Ja ir dots un jāuzraksta pierādījums, grupa ir
   `QTY_Prove`; ja tas jānoskaidro, grupa ir `QTY_Decide`.
2. **Vai jautājumu izšķirtu viens konkrēts piemērs?** Ja jā, tips ir eksistences tips
   (`QTY_ProveExistence`, `QTY_DecideExistence`); ja nē, vispārīgais tips
   (`QTY_ProveUniversal`, `QTY_DecideUniversal`). Šis tests aizstāj kvantoru
   skaitīšanu. Piemēram, "pierādi, ka katram $n$ eksistē …" ir vispārīgs apgalvojums,
   jo piemērs vienam $n$ to neizšķir; neiespējamības apgalvojumi ("pierādi, ka nevar …")
   arī ir vispārīgi. Ja pirmais kvantors ir pa ļoti mazu kopu, ko var pārlasīt pa
   gadījumiem, tipu nosaka nākamā prasība.
3. **Vai nezināmais ir definēts ar nosacījumu?** Ja nezināmo nosaka vienādojums vai
   īpašība, tips ir `QTY_FindAll` (jāpierāda, ka citu atbilžu nav). Ja formulējums pats
   nosaka vienu objektu (noteikta konfigurācija, dota izteiksme, objektu skaits), tips ir
   `QTY_FindValue`. Šaubu gadījumā izvēlas `QTY_FindAll`. Ģeometrijas uzdevumu, kas
   izskatās pēc `QTY_FindValue`, bet pieļauj divas konfigurācijas ar dažādām atbildēm,
   anotē kā `QTY_FindAll`.
4. **Vai objekts obligāti jāuzrāda?** Ja atbilde ir pats piemērs vai procedūra, grupa ir
   `QTY_Construct` un nekonstruktīvi spriedumi neder. Ja jāpierāda tikai tas, ka objekts
   eksistē, tips ir `QTY_ProveExistence` un der arī Dirihlē princips, pierādījums no
   pretējā vai stratēģijas zagšana.

Virstipus (`QTY_Find`, `QTY_Construct`, `QTY_Prove`, `QTY_Decide`) anotē tikai tad, ja
neviens apakštips neder.

## Kam tipu piešķir

- Tipu piešķir **jautājumam**. Lielākajai daļai uzdevumu ir viens jautājums, un tips
  attiecas uz visu uzdevumu.
- Ja uzdevumam ir apakšpunkti (A), (B), katram apakšpunktam ir savs tips.
- Tips nav atkarīgs no atrisinājuma: tas ir vienāds visiem derīgiem atrisinājumiem, un to
  var piešķirt, pirms atrisinājums ir zināms.
- Grupā `QTY_Decide` no atbildes (jā vai nē) ir atkarīgs tikai tas, kuras daļas
  atrisinājumā vajadzīgas; pats tips no atbildes nav atkarīgs.
- Lemmām un starprezultātiem atrisinājuma iekšienē jautājuma tipu nepiešķir.

## Kombinēti tipi

Parasti jautājumam ir **viens** tips. Izņēmuma gadījumos, kad vienā jautājumā ir divu
tipu nepieciešamās daļas, pievieno otro tipu (`eliozo:questionTypeSecondary`). Vairāk par
diviem tipiem nelieto. Galvenais tips ir tas, kas nosaka atrisinājuma kopējo uzbūvi.

| Formulējums | Galvenais tips | Otrais tips | Paskaidrojums |
|---|---|---|---|
| "Ar kādu mazāko svēršanu skaitu var atrast viltoto monētu?" | `QTY_FindOptimal` | `QTY_ConstructProcedure` | Piemērs, kas sasniedz optimumu, ir procedūra; novērtējums parāda, ka ar mazāk soļiem nepietiek. |
| "Kurām $n$ vērtībām uzvar pirmais spēlētājs?" | `QTY_FindAll` | `QTY_DecideWinner` | Katrai $n$ vērtībai jānoskaidro uzvarētājs un jāuzrāda viņa stratēģija. |
| "Pierādi, ka summa nepārsniedz 5, un parādi, ka vienādība ir iespējama." | `QTY_ProveUniversal` | `QTY_ConstructExample` | Novērtējums ir vispārīgs spriedums; vienādības gadījumu parāda ar piemēru. |

Kombinēts tips **nav** vajadzīgs šādos gadījumos.

- Uzdevumam ir atsevišķi apakšpunkti (A), (B): katram piešķir savu tipu.
- "Kuriem $n$ kvadrātu var sagriezt $n$ kvadrātos?" ir parasts `QTY_FindAll`: pārbaude,
  ka katra atbilde der, ir konstrukcija, un pierādījums, ka citu nav, ir neiespējamības
  spriedums. Abas daļas jau ietilpst tipā `QTY_FindAll`.
- Uzdevums ar jautājumu "Cik …?" ir `QTY_FindValue`, arī tad, ja risinājumā vispirms
  atrod visus objektus un pēc tam tos saskaita.

## Spēles

Spēļu uzdevumos tips ir atkarīgs no tā, kas ir dots un kas jāuzrāda.

| Formulējums | Tips | Kas jāuzrāda |
|---|---|---|
| "Kurš uzvar, pareizi spēlējot?" | `QTY_DecideWinner` | uzvarētājs, viņa stratēģija un pierādījums, ka tā strādā |
| "Parādi, kā pirmais spēlētājs var uzvarēt." | `QTY_ConstructProcedure` | stratēģija un pierādījums, ka tā strādā |
| "Pierādi, ka pirmais spēlētājs var uzvarēt." | `QTY_ProveExistence` | pietiek ar pierādījumu, ka stratēģija eksistē (der arī stratēģijas zagšana) |
| "Kurām $n$ vērtībām uzvar pirmais spēlētājs?" | `QTY_FindAll` + `QTY_DecideWinner` | uzvarētājs un stratēģija katrai $n$ vērtībai |

`QTY_DecideWinner` ir atsevišķs tips, jo tā daļas nevar izteikt ar citiem tipiem. Tipā
`QTY_DecideExistence` atbildi "jā" pamato ar piemēru, bet atbildi "nē" — ar vispārīgu
neiespējamības pierādījumu. Tipā `QTY_DecideWinner` **abas** atbildes pamato ar
konstrukciju: tā spēlētāja stratēģiju, kurš uzvar. Vispārīgais spriedums ir stratēģijas
pārbaudē: tai jāparedz atbilde uz **katru** pretinieka gājienu.

Tipiskās kļūdas šajā tipā:

- stratēģijas vietā aprakstīta viena izspēlēta partija;
- stratēģija paredz atbildes tikai uz pretinieka "saprātīgajiem" gājieniem;
- nosaukts uzvarētājs, bet nav pamatots, ka stratēģijā paredzētais gājiens vienmēr ir
  iespējams.

## Atbildes formāti

Atbildes formāts nav jautājuma tips: to pašu jautājumu var uzdot dažādos formātos.
Uzdevums konkursā Ķengurs var būt `QTY_FindValue` ar formātu `RSP_AnswerChoice`; tas
pats uzdevums olimpiādē būtu `QTY_FindValue` ar formātu `RSP_SolutionFull`. Tāpēc arī
testu uzdevumiem piešķir jautājuma tipu: tas pasaka, kas būtu jāpamato, ja uzdevumu
uzdotu ar pilnu atrisinājumu.

Formātu parasti nosaka sacensības un kārta, tāpēc to var mantot no uzdevuma avota un
norādīt atsevišķi tikai tad, ja tas atšķiras. Ja formāts nav norādīts, pieņem
`RSP_SolutionFull`.

| ID | Vecākais | Nosaukums | Kanoniskā norāde | Kas jāiesniedz |
|---|---|---|---|---|
| `RSP_Solution` | | Atrisinājums ar pamatojumu | Pamato savu atbildi. | atkarīgs no apakštipa |
| `RSP_SolutionFull` | `RSP_Solution` | Pilns rakstisks atrisinājums | Uzraksti pilnu atrisinājumu. | atbilde un visas jautājuma tipa prasītās daļas |
| `RSP_SolutionBrief` | `RSP_Solution` | Atbilde ar īsu pamatojumu | Ieraksti atbildi un īsi to pamato. | atbilde un viens vai daži teikumi ar galveno ideju |
| `RSP_SolutionOral` | `RSP_Solution` | Mutiska prezentācija | Izstāsti atrisinājumu un atbildi uz jautājumiem. | izklāsts pie tāfeles un atbildes uz oponenta jautājumiem |
| `RSP_Answer` | | Tikai atbilde | Ieraksti tikai atbildi. | atkarīgs no apakštipa |
| `RSP_AnswerNumeric` | `RSP_Answer` | Skaitliska atbilde | Ieraksti atbildi kā skaitli. | viens skaitlis noteiktā pierakstā |
| `RSP_AnswerOpen` | `RSP_Answer` | Īsa brīva atbilde | Ieraksti atbildi. | izteiksme, kopa, vārds vai piemērs |
| `RSP_AnswerChoice` | `RSP_Answer` | Viena izvēle no vairākām | Izvēlies pareizo atbildi. | viens no piedāvātajiem variantiem |
| `RSP_AnswerMultiSelect` | `RSP_Answer` | Vairākas izvēles | Atzīmē visus pareizos apgalvojumus. | visi pareizie varianti |
| `RSP_AnswerYesNo` | `RSP_Answer` | Jā vai nē | Atbildi ar jā vai nē. | viena no divām atbildēm |

Formāts `RSP_SolutionBrief` ir starpposms starp testu un pilnu atrisinājumu: īss
paskaidrojums attur no minēšanas, un to var vērtēt automātiski. Formāts
`RSP_SolutionOral` atbilst matemātiskajām cīņām un mutiskajām olimpiādēm.

## Vecās vērtības

| Vecā vērtība | Jaunā vērtība |
|---|---|
| `Find`, `FindAll`, `FindOptimal` | `QTY_Find`, `QTY_FindAll`, `QTY_FindOptimal` |
| `FindValue`, `FindCount` | `QTY_FindValue` |
| `FindExample` | `QTY_ConstructExample` |
| `Algorithm` | `QTY_ConstructProcedure` |
| `Prove`, `ProveExistence`, `ProveUniversal` | `QTY_Prove`, `QTY_ProveExistence`, `QTY_ProveUniversal` |
| `Decide`, `DecideExistence`, `DecideUniversal`, `DecideWinner` | `QTY_Decide`, `QTY_DecideExistence`, `QTY_DecideUniversal`, `QTY_DecideWinner` |
| `ProveDisprove` | `QTY_Decide` (aptuveni; ieteicams precizēt līdz apakštipam) |
| `ShortAnswer` | atbildes formāts `RSP_Answer` vai tā apakštips; jautājuma tips jāpiešķir no jauna |

## Piemēri

"Atrast visus" uzdevumi skaitļu teorijā:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType "QTY_FindAll" ;
         eliozo:domain "NT" .
    }
    ORDER BY ?problemID

Tā kā uzdevumā ID glabājas kā teksts, ar vārdnīcu to savieno caur
`eliozo:questionID`, piemēram, lai visus grupas `QTY_Find` uzdevumus sagrupētu pēc tipa:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    SELECT ?problemID (?type AS ?section)
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType ?type .
      ?q eliozo:questionID ?type ;
         skos:broader* eliozo:QTY_Find .
    }
    ORDER BY ?type ?problemID

Testu uzdevumi ar izvēles atbildēm, kurus var pārveidot par "atrast lielāko vai mazāko"
uzdevumiem ar pilnu atrisinājumu:

    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID
    WHERE {
      ?p eliozo:problemID ?problemID ;
         eliozo:questionType "QTY_FindOptimal" ;
         eliozo:responseFormat "RSP_AnswerChoice" .
    }
    ORDER BY ?problemID

Saistīts: jautājuma tips ir uzdevuma formulējuma slānī blakus
[žanriem](/content/ontology_genres) un [jēdzieniem](/content/ontology_concepts); tas
norāda uz tipiskām [metodēm](/content/ontology_methods). Tipam `QTY_FindOptimal` atbilst
stratēģijas birka `ExampleAndBound`, tipam `QTY_DecideWinner` — metode
`MTH_ProcedureGameStrategy`.
