# Semantinė paieška

Semantinė paieška randa uždavinius, kurie yra **apie tą patį**, ką įvedėte, net jei
jie neturi nė vieno bendro žodžio. Ji visai neieško raidžių ar šablonų: ir jūsų
tekstas, ir kiekvienas uždavinys paverčiami 1536 skaičių vektoriumi (*įterptimi*, kurią
apskaičiuoja OpenAI modelis `text-embedding-3-small`), ir grąžinami uždaviniai, kurių
vektoriai nukreipti artimiausia kryptimi (kosinusinis atstumas; vektoriai saugomi ir
ieškomi PostgreSQL su plėtiniu `pgvector`).

## Kiek teksto įvesti

Visa užklausa tampa vienu vektoriumi, todėl jos ilgis svarbus:

| Užklausa | Ko tikėtis |
|---|---|
| vienas ar du žodžiai, pvz., `trikampis` | silpnai: per mažai prasmės, rezultatai – laisvos asociacijos; geriau naudokite [tikslią paiešką](/content/search_by_keyword) |
| vienas sakinys, aprašantis idėją, pvz., *dalaus iš 9 skaičiaus skaitmenų suma* | gerai: tipiniai uždaviniai šia tema |
| įklijuota visa uždavinio sąlyga | geriausiai: uždaviniai su tokiu pačiu siužetu ar struktūra – panašūs uždaviniai, variantai ir dublikatai iš kitų olimpiadų |

Atsižvelgiama į maždaug **8000 simbolių** (kelis puslapius), ilgesnis tekstas
nukerpamas. Labai ilgas tekstas, kuriame sumaišytos kelios idėjos, suvidurkinamas į
vieną vektorių, ir rezultatas seka vyraujančią idėją – įklijuokite po vieną uždavinį.

## Ką galima ir ko negalima rasti

* **Panašius uždavinius.** Įklijavus uždavinį, randami kiti su ta pačia aplinka
  (šachmatų lenta, turnyras, monetos ant stalo) ar tokio paties tipo klausimu, net jei
  skaičiai ir vardai skiriasi.
* **Sinonimai ir perfrazavimai** sutapatinami: *lygiakraštis trikampis* ir *trikampis,
  kurio visos kraštinės lygios* modeliui yra artimi.
* **Linksniai** nesvarbūs: *trikampis*, *trikampio*, *trikampiui* modeliui reiškia tą
  patį, todėl nereikia ieškoti pagal šaknis.
* **Kitos kalbos.** Modelis daugiakalbis: užklausa angliškai ar lietuviškai randa ir
  latviškai parašytus uždavinius, ir atvirkščiai. Užklausa uždavinių kalba vis dėlto
  paprastai duoda kiek tikslesnius rezultatus.
* **Rašybos klaidos** paprastai netrukdo.
* **Tikslios sąlygos netikrinamos.** Neiginys (*nesidalija*), konkretūs skaičiai,
  „bent“ ir „ne daugiau kaip“ vektoriaus beveik nekeičia. Uždavinys, artimas pagal
  prasmę, bet besiskiriantis tokia detale, vis tiek bus rastas – ir aukštai įvertintas.
* **Metodai randami tik tada, kai jie užrašyti.** Sąlygoje retai pasakyta, kaip
  uždavinys sprendžiamas; norėdami ieškoti pagal sprendimo idėją (*Dirichlė principas*,
  *invariantas*), pasirinkite **Sprendimuose**.

## Formulės

LaTeX formulės skaitomos kaip įprastas tekstas. Jos šiek tiek papildo prasmę –
užklausa su `\sqrt{}` ir `\geq` krypsta link nelygybių su šaknimis, – bet modelis
neskaičiuoja: `x^2-1` ir `(x-1)(x+1)` neatpažįstami kaip lygūs, o viena formulė yra
prasta užklausa. Aprašykite formulę žodžiais arba naudokite
[tikslią paiešką](/content/search_by_keyword) konkrečiam LaTeX fragmentui rasti.

## Kur ieškoma ir kiek rezultatų

Išskleidžiamasis sąrašas šalia paieškos lauko nurodo, su kuo lyginama:

* **Uždaviniuose** – uždavinių sąlygos. Kiekvienas uždavinys saugomas viena kalba –
  latviškai, jei yra latviškas tekstas.
* **Sprendimuose** – sąlygos **ir** visi sprendimai visomis kalbomis. Uždavinio vietą
  sąraše lemia tas jo tekstas, kuris užklausai artimiausias.

**Slenksčio nėra**: paieška visada grąžina **20** artimiausių uždavinių (du
puslapius), pradedant artimiausiu, net jei nė vienas iš jų nėra tikrai tinkamas.
Pirmieji rezultatai patikimiausi; likusius įvertinkite patys.
