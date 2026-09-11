# Paieška reguliariosiomis išraiškomis

Paieška reguliariosiomis išraiškomis ieško ne pastovios eilutės, o **šablono**. Ji
praverčia, kai ieškomas dalykas gali kisti: daiktavardis su bet kuria galūne, formulė
su bet kokiais skaičiais arba frazė, kuri gali būti perkelta į kitą eilutę.

Paieška **neskiria didžiųjų ir mažųjų raidžių**, o šablono ieškoma bet kurioje
uždavinio teksto vietoje — jam nebūtina atitikti viso teksto.

## Pasvirosios brūkšnelės taisyklė

Šią taisyklę verta įsidėmėti pirmiausia. Reguliariojoje išraiškoje pasviroji brūkšnelė
pradeda kaitos ženklą, todėl **LaTeX brūkšnelė rašoma dukart**:

| Įvedi | Atitinka tekste | Neteisingai |
|---|---|---|
| `\\frac` | `\frac` | `\frac` neranda nieko |
| `\\sqrt` | `\sqrt` | `\sqrt` neranda nieko |
| `\\sin` | `\sin` | `\sin` neranda nieko |

LaTeX riestiniai, laužtiniai ir paprastieji skliaustai reguliariojoje išraiškoje taip
pat yra ypatingi ženklai, todėl prieš juos rašoma viena brūkšnelė: `\{` `\}` `\[` `\]`
`\(` `\)`. Sudėjus abi taisykles, LaTeX kubinės šaknies pradžios `\sqrt[3]{` ieškoma
taip:

    \\sqrt\[3\]\{

Jei nesinori galvoti apie kaitos ženklus, naudok
[tikslią paiešką](/content/search_by_keyword) — ten kiekvienas ženklas reiškia pats save.

## Daiktavardžiai su visomis galūnėmis

Lietuvių ir latvių kalbose daiktavardžiai kiekvienu linksniu keičia galūnę. Galūnes
galima išvardyti grupėje, atskiriant jas stačiais brūkšniais:

    trikamp(is|io|iui|į|yje)

    trijstūr(is|a|im|i|ī|iem|os)

Jei galūnė nesvarbi, ieškok bet kokios raidžių sekos. `\w` yra viena raidė arba
skaitmuo, o `*` reiškia „bet kiek jų“:

    trikamp\w*

Atkreipk dėmesį, kad pagrindinė forma pasitaiko ir sudurtiniuose bei vediniuose,
todėl `kvadrat\w*` ras ir *kvadratinę lygtį*. Jei reikia būtent žodžio ribos, naudok
`\b`:

    \bkvadratas\b

Jei keičiasi pati žodžio šaknis, abi formas galima sujungti į vieną šabloną:

    skait(l|ļ)\w*

## Formulės uždavinyne

Formulės saugomos kaip LaTeX uždavinio Markdown tekste tarp dolerio ženklų. Štai kaip
atrodo tikro uždavinio pirminis tekstas:

<pre><code>Nogriežņa &#36;AB&#36; garums ir &#36;10~\mathrm{cm}&#36;. Uz tā kā uz hipotenūzas konstruēti
divi taisnleņķa trijstūri &#36;ABC&#36; un &#36;ABD&#36;.
</code></pre>

o štai sprendimo fragmentas:

<pre><code>Tās &#36;n&#36; pēc kārtas ņemtu locekļu summa ir
&#36;\frac{(a+a+n-1) \cdot n}{2}=\frac{(2 a+n-1) \cdot n}{2}&#36;.
</code></pre>

Šablonas lyginamas būtent su šiuo tekstu — su LaTeX užrašu, o ne su formule tokia,
kokia ji matoma ekrane. Taigi trupmenos ieškoma kaip `\\frac`, o laipsnio rodiklio —
kaip `\^`.

## Matematinės prasmės pavyzdžiai

Kelios iš šių formulių uždaviniuose ne klausiamos, o naudojamos sprendžiant, todėl
pasitaiko tik sprendimuose. Jei paieška uždavinių formuluotėse nieko neranda,
perjunk sąrašą šalia paieškos lauko į **Sprendimuose** ir pabandyk dar kartą — žemiau
nurodyta, kuriems šablonams to reikia.

**Dvinario kvadratas**, pavyzdžiui, `(a+b)^2` arba `(2x-1)^{2}`. Skliaustai su turiniu,
po kurių eina antrasis laipsnis:

    \([^()]+\)\^\{?2

**Kubinė šaknis**, `\sqrt[3]{...}`:

    \\sqrt\[3\]

**Alfa, beta arba gama sinusas**, leidžiant tarpą tarp abiejų LaTeX komandų
(*sprendimuose*):

    \\sin *\\(alpha|beta|gamma)

**Trupmena trupmenoje** — vienos trupmenos skaitiklyje prasideda nauja trupmena
(*sprendimuose*):

    \\frac\{[^{}]*\\frac

**Lygčių sistema**, užrašyta `cases` aplinka:

    \\begin\{cases\}

**Uždavinys apie dalybą su liekana**, su lyginiu ir moduliu (*sprendimuose*):

    \\equiv.*\\pmod

**Frazė, kuri gali būti perkelta į kitą eilutę.** Markdown pirminiame tekste sakiniai
laužomi į eilutes, todėl vietoj tarpo gali būti eilutės lūžis. `\s+` atitinka bet
kokią tarpo ženklų seką, taip pat ir eilutės lūžį:

    taisnleņķa\s+trijstūris

## Kas palaikoma ir kas ne

Paiešką atlieka SPARQL 1.1 reguliariųjų išraiškų funkcija. Visi kasdien naudojami
elementai veikia:

| Elementas | Reikšmė |
|---|---|
| `.` | bet koks vienas ženklas |
| `*` `+` `?` | nulis ar daugiau, vienas ar daugiau, neprivalomas |
| `{2,3}` | nuo dviejų iki trijų pasikartojimų |
| `[abc]` `[^abc]` | vienas iš šių ženklų, bet koks ženklas, išskyrus šiuos |
| `[0-9]` `\d` `\w` `\s` | skaitmuo, raidė arba skaitmuo, tarpo ženklas |
| `^` <code>&#36;</code> `\b` | teksto pradžia, teksto pabaiga, žodžio riba |
| `(?i)` | neskirti didžiųjų ir mažųjų raidžių — čia tai jau numatyta |

Šablonas `(abc|def)` atitinka bet kurią iš abiejų pusių, kaip ir galūnių pavyzdžiuose
aukščiau.

Žvilgsnis pirmyn `(?=...)`, žvilgsnis atgal `(?<=...)` ir nuorodos į grupes `\1`
**nepalaikomi**. Šablonas, kuris juos naudoja, taip pat šablonas su sintaksės klaida,
pavyzdžiui, neuždarytu skliaustu, tiesiog negrąžina nė vieno rezultato, o ne klaidos
pranešimą — todėl, jei sudėtingas šablonas nieko neranda, pirmiausia patikrink, ar jis
parašytas taisyklingai.

## Kur ieškoma ir kiek rezultatų

Išskleidžiamasis sąrašas šalia paieškos lauko nurodo, kur ieškoti:

* **Uždaviniuose** — tik uždavinių formuluotėse.
* **Sprendimuose** — uždavinių formuluotėse **ir** visuose jų sprendimuose. Daugelis
  formulių pasirodo tik sprendimuose, todėl būtent čia toks šablonas kaip
  `\\frac\{[^{}]*\\frac` duoda rezultatų.

Grąžinama ne daugiau kaip **10** uždavinių, surikiuotų pagal klasę ir uždavinio
identifikatorių. Jei rezultatų yra lygiai 10, greičiausiai jų yra daugiau.
