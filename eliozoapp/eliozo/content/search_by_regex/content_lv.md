# Meklēšana ar regulārajām izteiksmēm

Meklēšana ar regulārajām izteiksmēm atrod nevis nemainīgu virkni, bet **paraugu**.
Tā noder, kad meklējamais var mainīties: lietvārds ar jebkuru galotni, formula ar
jebkuriem skaitļiem vai frāze, kas var būt pārnesta jaunā rindā.

Meklēšana **neatšķir lielos un mazos burtus**, un paraugs tiek meklēts jebkurā
uzdevuma teksta vietā — tam nav jāsakrīt ar visu tekstu.

## Slīpsvītras likums

Šo ir vērts iegaumēt vispirms. Regulārajā izteiksmē slīpsvītra sāk aizsargkombināciju,
tāpēc **LaTeX slīpsvītra jāraksta divreiz**:

| Ievadi | Atbilst tekstā | Nepareizi |
|---|---|---|
| `\\frac` | `\frac` | `\frac` neatrod neko |
| `\\sqrt` | `\sqrt` | `\sqrt` neatrod neko |
| `\\sin` | `\sin` | `\sin` neatrod neko |

Arī LaTeX figūriekavas, kvadrātiekavas un apaļās iekavas regulārajā izteiksmē ir
īpašas rakstzīmes, tāpēc tām priekšā liek vienu slīpsvītru: `\{` `\}` `\[` `\]` `\(`
`\)`. Abus likumus saliekot kopā, LaTeX kubsaknes sākums `\sqrt[3]{` jāmeklē šādi:

    \\sqrt\[3\]\{

Ja negribas domāt par aizsargzīmēm, izmanto
[precīzo meklēšanu](/content/search_by_keyword) — tur katra rakstzīme nozīmē pati sevi.

## Lietvārdi ar visām galotnēm

Latviešu un lietuviešu valodā lietvārdi katrā locījumā maina galotni. Galotnes var
uzskaitīt grupā, atdalot tās ar vertikālām svītrām:

    trijstūr(is|a|im|i|ī|iem|os)

    trikamp(is|io|iui|į|yje)

Ja galotnei nav nozīmes, meklē jebkuru burtu virkni. `\w` ir viens burts vai cipars,
bet `*` nozīmē "jebkurš to skaits":

    trijstūr\w*

Jāievēro, ka pamatforma sastopama arī saliktos un atvasinātos vārdos, tāpēc
`kvadrāt\w*` atradīs arī *kvadrātvienādojumu*. Ja vajag tieši vārda robežu, lieto
`\b`:

    \bkvadrāts\b

Ja mainās pati vārda sakne, abas formas var apvienot vienā paraugā:

    skait(l|ļ)\w*

## Formulas uzdevumu krājumā

Formulas glabājas kā LaTeX uzdevuma Markdown tekstā starp dolāra zīmēm. Tā izskatās
īsta uzdevuma pirmavots:

<pre><code>Nogriežņa &#36;AB&#36; garums ir &#36;10~\mathrm{cm}&#36;. Uz tā kā uz hipotenūzas konstruēti
divi taisnleņķa trijstūri &#36;ABC&#36; un &#36;ABD&#36;.
</code></pre>

un šis ir atrisinājuma fragments:

<pre><code>Tās &#36;n&#36; pēc kārtas ņemtu locekļu summa ir
&#36;\frac{(a+a+n-1) \cdot n}{2}=\frac{(2 a+n-1) \cdot n}{2}&#36;.
</code></pre>

Paraugs tiek salīdzināts tieši ar šo tekstu — ar LaTeX pierakstu, nevis ar formulu
tādu, kāda tā parādās ekrānā. Tātad daļa jāmeklē kā `\\frac`, bet kāpinātājs — kā
`\^`.

## Piemēri ar matemātisku nozīmi

Vairākas no šīm formulām uzdevumos netiek prasītas, bet gan izmantotas risinājuma
gaitā, tāpēc tās sastopamas tikai atrisinājumos. Ja meklēšana uzdevumu formulējumos
neko neatrod, pārslēdz izvēlni blakus meklēšanas logam uz **Atrisinājumos** un mēģini
vēlreiz — zemāk ir norādīts, kuriem paraugiem tas ir vajadzīgs.

**Binoma kvadrāts**, piemēram, `(a+b)^2` vai `(2x-1)^{2}`. Iekavas ar saturu, kam seko
otrā pakāpe:

    \([^()]+\)\^\{?2

**Kubsakne**, `\sqrt[3]{...}`:

    \\sqrt\[3\]

**Alfa, beta vai gamma sinuss**, pieļaujot atstarpi starp abām LaTeX komandām
(*atrisinājumos*):

    \\sin *\\(alpha|beta|gamma)

**Daļa daļā** — vienas daļas skaitītājs sākas ar jaunu daļu (*atrisinājumos*):

    \\frac\{[^{}]*\\frac

**Vienādojumu sistēma**, kas rakstīta ar `cases` vidi:

    \\begin\{cases\}

**Uzdevums par dalīšanu ar atlikumu**, ar kongruenci un moduli (*atrisinājumos*):

    \\equiv.*\\pmod

**Frāze, kas var būt pārnesta jaunā rindā.** Markdown pirmavotā teikumi ir sadalīti
rindās, tāpēc atstarpes vietā var būt rindu pārnesums. `\s+` atbilst jebkurai
atstarpes rakstzīmju virknei, arī rindu pārnesumam:

    taisnleņķa\s+trijstūris

## Kas ir un kas nav atbalstīts

Meklēšanu veic SPARQL 1.1 regulāro izteiksmju funkcija. Visi ikdienā lietotie
elementi darbojas:

| Elements | Nozīme |
|---|---|
| `.` | jebkura viena rakstzīme |
| `*` `+` `?` | nulle vai vairāk, viena vai vairāk, neobligāta |
| `{2,3}` | no divām līdz trim atkārtošanās reizēm |
| `[abc]` `[^abc]` | viena no šīm rakstzīmēm, jebkura rakstzīme, izņemot šīs |
| `[0-9]` `\d` `\w` `\s` | cipars, burts vai cipars, atstarpes rakstzīme |
| `^` <code>&#36;</code> `\b` | teksta sākums, teksta beigas, vārda robeža |
| `(?i)` | neatšķirt lielos un mazos burtus — šeit tas jau ir noklusējums |

Paraugs `(abc|def)` atbilst jebkurai no abām pusēm, tāpat kā galotņu piemēros augstāk.

Priekšskatījums `(?=...)`, atskatīšanās `(?<=...)` un atsauces uz grupām `\1` **nav**
atbalstītas. Paraugs, kas tās izmanto, kā arī paraugs ar sintakses kļūdu, piemēram,
neaizvērtu iekavu, vienkārši neatgriež nevienu rezultātu, nevis kļūdas paziņojumu —
tāpēc, ja sarežģīts paraugs neko neatrod, vispirms pārbaudi, vai tas ir pareizi
uzrakstīts.

## Kur tiek meklēts un cik rezultātu

Izkrītošā izvēlne blakus meklēšanas logam nosaka, kur meklēt:

* **Uzdevumos** — tikai uzdevumu formulējumos.
* **Atrisinājumos** — uzdevumu formulējumos **un** visos to atrisinājumos. Daudzas
  formulas parādās tikai atrisinājumos, tāpēc tieši šeit tāds paraugs kā
  `\\frac\{[^{}]*\\frac` dod rezultātus.

Tiek atgriezti ne vairāk kā **10** uzdevumi, sakārtoti pēc klases un pēc uzdevuma
identifikatora. Ja rezultātu ir tieši 10, visdrīzāk to ir vairāk.
