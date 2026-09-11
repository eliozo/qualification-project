# Tiksli paieška

Tiksli paieška ieško įvesto teksto kaip **pažodinio poteksčio** uždavinio tekste.
Galūnės neatmetamos, tekstas neskaidomas į žodžius ir rašybos klaidos netaisomos:
įvestas tekstas uždavinyje turi pasitaikyti ženklas po ženklo.

## Žodžių šaknys ir galūnės

Kadangi ieškoma potekstės, o ne viso žodžio, galima ieškoti pagal **šaknį** ir rasti
visas galūnes. Lietuvių ir latvių kalbose tai svarbu, nes daiktavardžiai kiekvienu
linksniu keičia galūnę:

| Įvedi | Bus rasta ir |
|---|---|
| `trikamp` | trikampis, trikampio, trikampiui, trikampį, trikampyje |
| `kvadrat` | kvadratas, kvadrato, kvadratą, kvadratinis |
| `trijstūr` | trijstūris, trijstūra, trijstūrim, trijstūri (latviškuose uždaviniuose) |

Verta turėti omenyje du dalykus:

* Šaknies ieškoma **bet kurioje žodžio vietoje**, ne tik jo pradžioje.
* Keistis gali tik galūnė. Jei keičiasi pati šaknis, vienos paieškos nepakanka:
  latviško žodžio *skaitlis* šaknis yra `skaitl`, o formų *skaitļa*, *skaitļi* ir
  *skaitļu* — `skaitļ`. Šiame uždavinyne `skaitl` pasitaiko 1040 uždavinių, o
  `skaitļ` — 1475 uždaviniuose, ir nė viena iš jų neranda kitos formų.

Tokiais atvejais — ir visada, kai reikia būtent kelių konkrečių galūnių — praverčia
[paieška reguliariosiomis išraiškomis](/content/search_by_regex): `skait(l|ļ)\w*` iš karto
apima visus 1825 tokius uždavinius, o `trikamp(is|io|iui)` susiaurina paiešką iki
trijų konkrečių formų.

## Frazės

Galima įvesti visą frazę kartu su tarpais ir skyrybos ženklais — `taisnleņķa
trijstūris` ieškoma kaip vienos eilutės, o ne kaip dviejų nepriklausomų žodžių.

Sunkumas tas, kad uždavinių tekstai saugomi Markdown formatu su **eilučių lūžiais
sakinio viduryje**. Frazė, kurią naršyklė parodo vienoje eilutėje, šaltinio tekste
gali būti perskirta:

<pre><code>Cik dažādos veidos skaitli &#36;2011&#36; var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu?
</code></pre>

Čia `pēc kārtas sekojošu` toje vietoje, kur rašytum tarpą, yra eilutės lūžis, todėl
tiksli frazė nerandama. Jei frazė, kuria esi tikras, nieko neranda, ieškok trumpiausio
fragmento, kuris negali būti perskirtas, arba persijunk į reguliariąsias išraiškas ir
vietoj tarpo rašyk `\s+` (bet koks tarpo ženklas):

    kārtas\s+sekojošu

## Didžiosios ir mažosios raidės

Tiksli paieška **neskiria didžiųjų ir mažųjų raidžių**. `Trikampis`, `trikampis` ir
`TRIKAMPIS` grąžina tuos pačius uždavinius. O diakritiniai ženklai yra svarbūs:
`trijsturis` be ilgumos ženklo neranda nieko.

## Formulių paieška

Visos uždavinyno formulės parašytos LaTeX kalba. Tikslioje paieškoje LaTeX rašomas
lygiai toks, koks jis yra tekste — su **viena** pasvirąja brūkšnele ir be jokių
kaitos ženklų:

| Įvedi | Randa |
|---|---|
| `\sqrt[3]{` | uždavinius su kubine šaknimi |
| `\frac{1}{2}` | uždavinius su trupmena viena antroji |
| `\mathrm{cm}` | uždavinius, kuriuose matuojama centimetrais |

Ženklai, kurie reguliariosiose išraiškose yra ypatingi — `(` `)` `[` `]` `{` `}` `.`
`*` `+` `?` `^` `|` `\` — čia neturi jokios ypatingos reikšmės; jų ieškoma taip pat
kaip ir bet kurių kitų. Būtent todėl tiksli paieška yra paprastesnis pasirinkimas,
kai ieškomas tekstas žinomas raidė raidėn. Norint ieškoti *šablono*, o ne pastovios
eilutės, naudok [paiešką reguliariosiomis išraiškomis](/content/search_by_regex).

## Kur ieškoma ir kiek rezultatų

Išskleidžiamasis sąrašas šalia paieškos lauko nurodo, kur ieškoti:

* **Uždaviniuose** — tik uždavinių formuluotėse.
* **Sprendimuose** — uždavinių formuluotėse **ir** visuose jų sprendimuose. Uždavinys
  randamas, jei tekstas pasitaiko arba formuluotėje, arba bet kuriame iš sprendimų,
  todėl šis variantas gali tik pridėti rezultatų, bet ne jų atimti.

Grąžinama ne daugiau kaip **10** uždavinių, surikiuotų pagal klasę ir uždavinio
identifikatorių. Jei rezultatų yra lygiai 10, greičiausiai jų yra daugiau — ieškomą
tekstą reikia pailginti ir patikslinti.
