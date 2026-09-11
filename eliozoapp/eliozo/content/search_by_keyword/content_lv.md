# Precīzā meklēšana

Precīzā meklēšana atrod ievadīto tekstu kā **burtisku apakšvirkni** uzdevuma tekstā.
Netiek atmesta vārdu galotne, teksts netiek sadalīts vārdos un netiek labotas
drukas kļūdas: ievadītajam tekstam ir jāsastopas uzdevumā rakstzīme pēc rakstzīmes.

## Vārdu saknes un galotnes

Tā kā tiek meklēta apakšvirkne, nevis vesels vārds, var meklēt pēc **saknes** un
atrast visas galotnes. Latviešu un lietuviešu valodā tas ir būtiski, jo lietvārdi
katrā locījumā maina galotni:

| Ievadi | Tiks atrasts arī |
|---|---|
| `trijstūr` | trijstūris, trijstūra, trijstūrim, trijstūri, trijstūrī, trijstūriem |
| `kvadrāt` | kvadrāts, kvadrāta, kvadrātu, kvadrātā, kvadrātvienādojums |
| `trikamp` | trikampis, trikampio, trikampiui, trikampį |

Jāņem vērā divas lietas:

* Sakne tiek meklēta **jebkurā vārda vietā**, ne tikai vārda sākumā — `rēķin` atrod
  arī *aprēķini* un *sarēķini*.
* Mainīties drīkst tikai galotne. Ja mainās pati sakne, ar vienu meklējumu nepietiek:
  vārdam *skaitlis* sakne ir `skaitl`, bet vārdiem *skaitļa*, *skaitļi* un *skaitļu*
  tā ir `skaitļ`. Šajā uzdevumu krājumā `skaitl` sastopams 1040 uzdevumos, bet
  `skaitļ` — 1475 uzdevumos, un neviens no tiem neatrod otra formas.

Šādos gadījumos — un vienmēr, kad vajag tieši dažas noteiktas galotnes — noder
[meklēšana ar regulārajām izteiksmēm](/content/search_by_regex): `skait(l|ļ)\w*` uzreiz
aptver visus 1825 šos uzdevumus, bet `trijstūr(is|a|im)` sašaurina meklējumu līdz
trim konkrētām formām.

## Frāzes

Var ievadīt veselu frāzi kopā ar atstarpēm un pieturzīmēm — `taisnleņķa trijstūris`
tiek meklēts kā viena virkne, nevis kā divi neatkarīgi vārdi.

Grūtība ir tā, ka uzdevumu teksti glabājas Markdown formātā ar **rindu pārnesumiem
teikuma vidū**. Frāze, ko pārlūkprogramma parāda vienā rindā, avota tekstā var būt
sadalīta:

<pre><code>Cik dažādos veidos skaitli &#36;2011&#36; var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu?
</code></pre>

Šeit `pēc kārtas sekojošu` vietā, kur tu rakstītu atstarpi, ir rindu pārnesums, tāpēc
precīzā frāze netiek atrasta. Ja frāze, par kuru esi pārliecināts, neko neatrod, meklē
īsāko fragmentu, kas nevar tikt sadalīts, vai arī pārslēdzies uz regulārajām
izteiksmēm un atstarpes vietā raksti `\s+` (jebkura atstarpes rakstzīme):

    kārtas\s+sekojošu

## Lielie un mazie burti

Precīzā meklēšana **neatšķir lielos un mazos burtus**. `Trijstūris`, `trijstūris` un
`TRIJSTŪRIS` atgriež vienus un tos pašus uzdevumus. Toties diakritiskās zīmes ir
svarīgas: `trijsturis` bez garumzīmes neatrod neko.

## Formulu meklēšana

Visas formulas uzdevumu krājumā ir rakstītas LaTeX valodā. Precīzajā meklēšanā LaTeX
jāieraksta tieši tāds, kāds tas ir tekstā — ar **vienu** slīpsvītru un bez
aizsargzīmēm:

| Ievadi | Atrod |
|---|---|
| `\sqrt[3]{` | uzdevumus, kuros ir kubsakne |
| `\frac{1}{2}` | uzdevumus, kuros ir daļa viena otrā |
| `\mathrm{cm}` | uzdevumus, kuros mēra centimetros |

Rakstzīmēm, kas regulārajās izteiksmēs ir īpašas — `(` `)` `[` `]` `{` `}` `.`
`*` `+` `?` `^` `|` `\` — šeit nav nekādas īpašas nozīmes; tās tiek meklētas tāpat kā
jebkuras citas. Tieši tāpēc precīzā meklēšana ir vienkāršākā izvēle, kad zināms
meklējamais teksts burts burtā. Lai meklētu *paraugu*, nevis nemainīgu virkni,
izmanto [meklēšanu ar regulārajām izteiksmēm](/content/search_by_regex).

## Kur tiek meklēts un cik rezultātu

Izkrītošā izvēlne blakus meklēšanas logam nosaka, kur meklēt:

* **Uzdevumos** — tikai uzdevumu formulējumos.
* **Atrisinājumos** — uzdevumu formulējumos **un** visos to atrisinājumos. Uzdevums
  tiek atrasts, ja teksts sastopams vai nu formulējumā, vai kādā no atrisinājumiem,
  tātad šis variants var tikai pievienot rezultātus, nevis tos atņemt.

Tiek atgriezti ne vairāk kā **10** uzdevumi, sakārtoti pēc klases un pēc uzdevuma
identifikatora. Ja rezultātu ir tieši 10, visdrīzāk to ir vairāk — meklējamo tekstu
vajag padarīt garāku un precīzāku.
