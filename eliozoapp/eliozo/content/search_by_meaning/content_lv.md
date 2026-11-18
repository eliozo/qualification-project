# Semantiskā meklēšana

Semantiskā meklēšana atrod uzdevumus, kas ir **par to pašu**, par ko ievadītais teksts,
pat ja tiem nav neviena kopīga vārda. Tā nemeklē ne burtus, ne šablonus: gan ievadītais
teksts, gan katrs uzdevums tiek pārvērsts 1536 skaitļu vektorā (*iegultnē*, ko aprēķina
OpenAI modelis `text-embedding-3-small`), un tiek atgriezti uzdevumi, kuru vektori
vērsti vistuvākajā virzienā (kosinusa attālums; vektori glabājas un tiek meklēti
PostgreSQL ar paplašinājumu `pgvector`).

## Cik garu tekstu ievadīt

Viss vaicājums kļūst par vienu vektoru, tāpēc tā garums ir svarīgs:

| Vaicājums | Ko sagaidīt |
|---|---|
| viens vai divi vārdi, piem., `trijstūris` | vāji: par maz nozīmes, rezultāti ir brīvas asociācijas — labāk lietot [precīzo meklēšanu](/content/search_by_keyword) |
| viens teikums, kas apraksta ideju, piem., *ar 9 dalāma skaitļa ciparu summa* | labi: tipiski uzdevumi par šo ideju |
| ielīmēts viss uzdevuma formulējums | vislabāk: uzdevumi ar tādu pašu sižetu vai uzbūvi — līdzīgi uzdevumi, varianti un dublikāti no citām olimpiādēm |

Tiek ņemtas vērā līdz aptuveni **8000 rakstzīmēm** (vairākas lappuses), garāks teksts tiek
nogriezts. Ļoti garš teksts, kurā sajauktas vairākas idejas, tiek savidējots vienā
vektorā, un rezultāts seko dominējošajai idejai — ielīmējiet pa vienam uzdevumam.

## Ko var un ko nevar atrast

* **Līdzīgus uzdevumus.** Ielīmējot uzdevumu, atrodas citi ar tādu pašu vidi (šaha
  galdiņš, turnīrs, monētas uz galda) vai tāda paša veida jautājumu, arī ja skaitļi un
  vārdi atšķiras.
* **Sinonīmi un pārfrāzējumi** tiek sapāroti: *vienādmalu trijstūris* un *trijstūris,
  kuram visas malas vienādas* modelim ir tuvi.
* **Locījumiem** nav nozīmes: *trijstūris*, *trijstūrim*, *trijstūru* modelim nozīmē
  to pašu, tāpēc nav jāmeklē pēc saknēm.
* **Citas valodas.** Modelis ir daudzvalodu: vaicājums angliski vai lietuviski atrod
  arī latviski rakstītus uzdevumus, un otrādi. Vaicājums uzdevumu valodā tomēr parasti
  dod nedaudz precīzākus rezultātus.
* **Drukas kļūdas** parasti netraucē.
* **Precīzi nosacījumi netiek pārbaudīti.** Noliegums (*nedalās*), konkrēti skaitļi,
  "vismaz" pret "ne vairāk kā" vektoru gandrīz nemaina. Uzdevums, kas pēc nozīmes ir
  tuvs, bet atšķiras šādā detaļā, tik un tā tiks atrasts — un augstu novērtēts.
* **Metodes atrodas tikai tad, ja tās ir uzrakstītas.** Formulējumā reti teikts, kā
  uzdevumu risina; lai meklētu pēc risinājuma idejas (*Dirihlē princips*, *invariants*),
  izvēlieties **Atrisinājumos**.

## Formulas

LaTeX formulas tiek lasītas kā parasts teksts. Tās nedaudz papildina nozīmi —
vaicājums ar `\sqrt{}` un `\geq` sliecas uz nevienādībām ar saknēm —, bet modelis
nerēķina: `x^2-1` un `(x-1)(x+1)` netiek atpazīti kā vienādi, un formula viena pati
ir slikts vaicājums. Aprakstiet formulu vārdiem vai lietojiet
[precīzo meklēšanu](/content/search_by_keyword), lai atrastu konkrētu LaTeX fragmentu.

## Kur meklē un cik rezultātu

Izkrītošais saraksts blakus meklēšanas laukam nosaka, ar ko salīdzina:

* **Uzdevumos** — uzdevumu formulējumi. Katrs uzdevums glabājas vienā valodā —
  latviski, ja latviskais teksts ir.
* **Atrisinājumos** — formulējumi **un** visi risinājumi visās valodās. Uzdevuma vietu
  sarakstā nosaka tas tā teksts, kas vaicājumam ir vistuvākais.

**Sliekšņa nav**: meklēšana vienmēr atgriež **20** tuvākos uzdevumus (divas lappuses),
sākot ar tuvāko, pat ja neviens no tiem nav īsti atbilstošs. Pirmie rezultāti ir
visdrošākie; pārējos izvērtējiet paši.
