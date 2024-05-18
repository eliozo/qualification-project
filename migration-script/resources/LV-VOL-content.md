# <lo-sample/> LV.VOL.2000.9.1

Dots, ka $n$ - vesels skaitlis. Cik daudzi no skaitļiem $n^2+1$,
$n(n+1)$ un $3n^3-2$ ir pāra skaitļi?

<small>

* questionType:FindCount

</small>



# <lo-sample/> LV.VOL.2000.9.4

Kurus no skaitļiem $1$; $55$; $56$; $7$; $36$ var izsacīt formā
$\frac{1}{a_1} + \frac{2}{a_2} + \ldots + \frac{10}{a_{10}}$, 
kur $a_1, a_2, \ldots, a_{10}$ - naturāli skaitļi, starp
kuriem var būt arī vienādi?

<small>

* questionType:FindCount

</small>


# <lo-sample/> LV.VOL.2000.10.2

Kādu mazāko naturālo skaitli var iegūt kā vērtību, ievietojot
iekavas izteiksmē $15:14:13:12:11:10:9:8:7:6:5:4:3:2$?


<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2000.11.2

Dots, ka $a$ un $b$ - naturāli skaitļi. Ir zināms arī, ka izteiksmes
$a + \frac{b}{a} - \frac{1}{b}$
vērtība ir naturāls skaitlis.  
**(A)** Pierādīt, ka šīs izteiksmes
vērtība ir kāda naturāla skaitļa kvadrāts.  
**(B)** Vai jebkuram
naturālam $n$ var atrast tādus naturālus 
$a$ un $b$, ka $a + \frac{b}{a} - \frac{1}{b} = n^2$?

<small>

* questionType:Prove,ProveDisprove

</small>

# <lo-sample/> LV.VOL.2000.11.4

Doti seši dažādi iracionāli skaitļi. Pierādīt, ka no tiem var
izvēlēties $3$ skaitļus (apzīmēsim tos ar $x$, $y$, $z$) tā, ka visi trīs
skaitļi $x+y$, $x+z$, $y+z$ ir iracionāli.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2000.12.5

Doti $12$ dažādi naturāli skaitļi. Katriem $5$ no tiem mazākais
kopīgais dalāmais ir viens un tas pats skaitlis $M$. Ir zināms,
ka no dotajiem $12$ skaitļiem var izvēlēties $x$ skaitļus tā, ka
katri divi no izvēlētajiem ir savstarpēji pirmskaitļi.  
**(A)** pierādīt, ka $x \leq 4$,  
**(B)** pierādīt: var gadīties, ka $x=4$.

<small>

* questionType:Prove,Prove

</small>


# <lo-sample/> LV.VOL.2001.9.1

Sienāža lēciena garums ir $5$. Viņš sākotnēji atrodas punktā ar
koordinātām $(0;0)$ un var pārvietoties tikai pa punktiem, kam abas
koordinātas ir veseli skaitļi.  
**(A)** Pierādīt, ka sienāzis var nokļūt punktā ar koordinātām $(1;0)$,  
**(B)** Vai sienāzis var nokļūt jebkurā punktā ar veselām koordinātām?

<small>

* topic:PythagoreanTriples
* topic:BezoutIdentity
* questionType:Prove,ProveDisprove

</small>




# <lo-sample/> LV.VOL.2001.9.2

Naturāla skaitļa $A$ ciparus uzrakstīja pretējā secībā un ieguva skaitli $B$.
Izrādījās, ka $B$ dalās ar $A$. Kāds var būt dalījums?

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2001.10.5

Kādiem naturāliem skaitļiem $n$ piemīt sekojoša īpašība: nosvītrojot
skaitļa $2^n$ pirmo ciparu, iegūst divnieka pakāpi ar naturālu kāpinātāju?

<small>

* topic:CountingObjects
* topic:PeriodicRemainders
* topic:DivisibilityRulesFor3And9
* topic:IntegerFactorization
* questionType:FindAll

</small>



## Atrisinājums

Ar eksperimentēšanu atrodam, ka
divnieka pakāpes $32$ un $64$ der. 
Nosvītrotās skaitļa daļas vērtība ($30$ vai $60$) abos gadījumos ir $15$ daudzkārtnis. 
Piemēram:

$$2^6-2^2 = 2^2(2^4-1)=2^2(8+4+2+1).$$ 


Lai $2^n - 2^m = 2^m(2^{n-m}-1)$ būtu nosvītrojamais cipars, šai izteiksmei jādalās ar $5$.
Pakāpes $2^{n-m}$ dalot ar $5$, iegūst šādus atlikumus:

| $n-m$             | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $2^{n-m} \pmod 5$ | 1   | 2   | 4   | 3   | 1   | 2   | 4   | 2   | 1   |
| $2^{n-m} \pmod 3$ | 1   | 2   | 1   | 2   | 1   | 2   | 1   | 2   | 1   |


Tā kā $n-m \neq 0$ un vajag, lai $2^{n-m}-1$ dalās ar $5$, iegūstam, ka $n-m > 0$
dalās ar $4$. Tad $2^{n-m}$ ir $16$, $256$, $4096$, $65536$ utt.   

**Secinājums:** Ja $2^{n-m} - 1$ dalās ar $5$, tad tas
dalās arī ar $3$. To var ieraudzīt tabuliņā, jo arī atlikumi (mod 3) ir periodiski. 
Un tā kā $n-m$ dalās ar $4$, tad tas dalīsies arī ar $2$. 

Izsvītrotais cipars pareizināts ar $10$ pakāpi 
ir $2^m\cdot{}(2^{n-m}-1)$. Šī skaitļa ciparu summai jādalās ar $3$, bet ne ar $9$. 
Vienīgi cipari $3$, $6$ apmierina šo īpašību, tātad 
$2^m\cdot{}(2^{n-m}-1)$ ir vai nu $3 \cdot 10^k$ vai  $6 \cdot 10^k$. 
Bet ja šie skaitļi ir lielāki par $30$ vai $60$, tad
dalot $300$, $600$ (vai $3000$, $6000$ utt.) ar divnieka pakāpēm, 
iegūsim tikai pirmreizinātājus $3$ un $5$.



# <lo-sample/> LV.VOL.2001.11.1

Pierādīt, ka
$\sqrt[3]{5\sqrt{2} + 7} - \sqrt[3]{5\sqrt{2} - 7} = 2$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2001.11.3

Atrisināt naturālos skaitļos vienādojumu $x^2+3^x=y^2$.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2001.12.3

Atrisināt naturālos skaitļos vienādojumu $x^2-y!=2001$. (Piezīme: ar $y!$
saprot visu naturālo skaitļu reizinājumu no $1$ līdz $y$ ieskaitot.)

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2002.9.1

Par naturāliem skaitļiem $x$ un $y$ zināms, ka 
$30<x<40<y<50$ un $xy$ ir kāda vesela 
skaitļa kubs. Kādas ir $x$ un $y$ vērtības?

<small>

* topic:FactorizationAndProperties
* topic:ExhaustionMethod
* questionType:FindAll

</small>



## Atrisinājums

Kādi skaitļi ir pilni kubi

* Reizinājums $xy$ ir pilns kubs, ja ikviena $xy$ 
  pirmreizinātāja pakāpe dalās ar $3$.
* Daudzas $x,y$ vērtības (kas satur tādus pirmreizinātājus $p$, 
  kas nav kvadrātā, kam nevar piereizināt $p^2$), var izslēgt:

$$\left\{ 
\begin{array}{l}
x \neq 31;\;33;\;34;\;35;\;37;\;38;\;39\\
y \neq 41;\;42;\;43;\;44;\;45;\;46;\;47;\;49\\
\end{array} \right.$$


Šķirojam gadījumus:

* Pirmreizinātājus $5$ un $7$ izmantot nav iespējams, jo $y=49$ 
  varētu salikt kopā vienīgi ar $x=35$, bet tad kāpinātājs pie
  $5$ nedalītos ar trīs (jo $x,y \in (25;50)$). 
* Paliek  tikai pirmskaitļi $2$ un $3$ un šādas vērtības:

$$x = 32;\;36\;\;\mbox{un}\;\;y=48.$$

Der vienīgi $x=36$, $y=48$. Tad $xy=2^63^3$ un $\sqrt[3]{xy}=12$.




# <lo-sample/> LV.VOL.2002.10.4

Kādiem naturāliem skaitļiem $n$ skaitlis $n\cdot{}2^{n-1}$ 
ir naturāla skaitļa kvadrāts?

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2002.10.5

Uz tāfeles sākotnēji pa reizei uzrakstīti veselie skaitļi no $0$ līdz
$1024$ ieskaitot. Spēlētāji $A$ un $B$ spēlē sekojošu spēli.
Vispirms $A$ nodzēš $2^9=512$ skaitļus. Pēc tam $B$ nodzēš $2^8=256$
skaitļus. Pēc tam $A$ nodzēš $2^7=128$ skaitļus. Pēc tam $B$ nodzēš
$2^6 =64$ skaitļus utt., kamēr ar pēdējo gājienu $B$ nodzēš $2^0=1$
skaitli. Uz tāfeles paliek divi skaitļi; apzīmēsim tos ar $x$ un $y$.
Spēlētājs $A$ vēlas, lai $\left| x-y \right|$ būtu iespējami liels; 
$B$ vēlas, lai $\left| x-y \right|$ būtu iespējami mazs. 
Cik lielu $\left| x-y \right|$ vērtību $A$ var
sasniegt?

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2002.11.2

Vienā kaudzītē ir $m$ konfektes, otrā - $n$ konfektes. 
Ar vienu gājienu var vai nu apēst vienu konfekti, 
vai apēst pa vienai konfektei no katras kaudzītes, vai arī
pārlikt vienu konfekti no vienas kaudzītes uz otru. 
Kas nevar izdarīt gājienu, zaudē. Andris un Juris 
izdara pa vienam gājienam pēc kārtas; pirmais iet
Andris. Kurš uzvar, pareizi spēlējot?


<small>

* questionType:Algorithm

</small>



# <lo-sample/> LV.VOL.2002.11.5

Kuriem naturāliem skaitļiem $n$, kas lielāki par $3$ 
un nedalās ar $3$, izpildās
īpašība: visi tie naturālie skaitļi, kas mazāki par $n$ 
un kuru lielākais kopīgais dalītājs ar $n$ ir $1$, 
veido aritmētisku progresiju?

<small>

* topic:IntegerFactorization
* topic:ArithmeticAndGeometricSeries
* questionType:FindAll

</small>



## Atrisinājums

* Der visi pirmskaitļi $n>3$, jo skaitļi, kas mazāki par $n$
  un kas ir savstarpēji pirmskaitļi ar $n$ ir šie:
  $1,2,\ldots,n-2,n-1$.
* Der visas pakāpes $2^k > 3$, jo savstarpēji pirmskaitļi 
  ir visi nepāru skaitļi: $1,3,5,\ldots,2^k-3,2^k-1$.

Neder citi skaitļi

Pieņemsim, ka $n = (2k+1)2^m$ ir pāru skaitlis, kas nav $2$ pakāpe un nedalās ar $3$. 
Ja $n$ ir pāru skaitlis, tad $2k+1 > 1$ un tam ir nepāra dalītājs. 
Tāpēc progresijā $1,3,\ldots,n-1$ būs kāds skaitļa $n$ dalītājs.
Līdzīgu iemeslu dēļ neder arī nepāru skaitļi, kas nav pirmskaitļi, bet 
nedalās ar $3$. 




# <lo-sample/> LV.VOL.2002.12.1

Ja $a$ un $b$ - naturāli skaitļi, tad ar $(a,b)$ apzīmējam 
$a$ un $b$ lielāko kopīgo dalītāju. Atrast lielāko iespējamo 
$(4n+3,6n+1)$ vērtību, ja $n$ - naturāls skaitlis.

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2003.9.1

Naturālu skaitli sauc par simetrisku, ja, izlasot tā decimālo
pierakstu no otra gala, iegūst to pašu skaitli. Piemēram,
simetriski ir skaitļi $111$; $424$; $88$; $5225$; $7$. 
Ir zināms, ka visi sešciparu simetriskie naturālie skaitļi 
dalās ar naturālu skaitli $x$. Kādas var būt $x$ vērtības?

<small>

* topic:DivisibilityRuleFor11
* topic:ExtremeElementMethod
* topic:EuclideanAlgorithm
* questionType:FindAll

</small>



## Atrisinājums

Skaitlis $\overline{abccba} = 100001a + 010010b + 001100c$ 
noteikti dalās ar $11$ (dalāmības pazīme, kā arī $100001$, 
$10010$, $1100$ dalās ar $11$). 

Vai $11$ ir lielākais kopīgais dalītājs visiem sešciparu simetriskajiem 
skaitļiem (tātad - lielākā iespējamā $x$ vērtība)? 
Atrodam lielāko kopīgo dalītāju simetriskiem sešciparu skaitļiem  
$100001$ un $101101$:
$$\mbox{LKD}(101101,100001) = \mbox{LKD}(100001,1100).$$ 
* Skaitlis $1100 = 2^2 \cdot 5^2 \cdot 11$, bet
ar $2$ un $5$ nedalās $100001$. 

Tātad $x=11$ ir lielākā $x$ vērtība. Var būt arī vērtība $x=1$. 



# <lo-sample/> LV.VOL.2003.10.2

Dots, ka $a$ un $b$ ir naturāli skaitļi, pie tam $a$ nedalās ar $5$. 
Skaitļu virkni $x_1, x_2, x_3, \ldots$ 
veido sekojoši: $x_1 = 5$, $x_{n+1} = ax_n + b$, ja $n=1;2;3;\ldots$. 
Kādai lielākajai $k$ vērtībai iespējams, ka visi skaitļi
$x_1;x_2;x_3;\ldots;x_k$ ir pirmskaitļi?

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2003.11.2

Naturālu skaitļu virknē $a_1, a_2, \ldots$ pirmo locekli $a_1$ izvēlas
patvaļīgi, un pie $n \geq 1$ pastāv vienādība $a_{n+1} = a_n^3 + 2003$. 
Kāds lielākais daudzums virknes locekļu var būt naturālu skaitļu
kvadrāti?

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2003.12.1

Vai eksistē  
**(A)** tādi naturāli skaitļi $x$, $y$ un $z$, 
kas lielāki par $1$, ka $x! \cdot y! = z!$?  
**(B)** tādi naturāli skaitļi $a, b, c, d, e$, kas lielāki par $1$, ka
$a! \cdot b! \cdot c! \cdot d! = e!$?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2003.12.4

"Tabulā" augšējā rindiņā pēc kārtas izrakstīti naturāli skaitļi no $1$ līdz $5$;
nākošajās rindiņās katrs skaitlis vienāds ar abu virs tā uzrakstīto
skaitļu summu. Kāds skaitlis atrodas apakšējā "virsotnē" tabulā, kas
veidota līdzīgi un kuras augšējā rindiņā izrakstīti 
naturāli skaitļi no $1$ līdz $2003$ ieskaitot?  
![](LV.VOL.2003.12.4.png)

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2004.9.3

Jānītis grib uzrakstīt $n$ dažādus naturālus skaitļus tā, lai nekādu
sešu uzrakstīto skaitļu summa nedalītos ar $6$.
Vai tas ir iespējams, ja  
**(A)** $n=10$,  
**(B)** $n=11$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.VOL.2004.10.3

Uz tāfeles uzrakstīti dažādi pirmskaitļi, to vidējais aritmētiskais
ir $27$.
Kāds vislielākais pirmskaitlis var būt uzrakstīts uz tāfeles?

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2004.11.2

Kādiem pirmskaitļiem $a$ un $b$ skaitlis $a^2 + 3ab + b^2$ ir naturāla
skaitļa kvadrāts?

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2004.12.5

Dots, ka $x_1 = 3$, $y_1 = 4$ un katram naturālam $n$ pastāv sakarība

$$x_{n+1} = 3x_n + 2 y_n,\;\; y_{n+1} = 4x_n + 3y_n.$$

Pierādīt, ka neviens no skaitļiem $y_1, y_2, y_3, \ldots$
nav naturāla skaitļa kubs.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2005.9.2

Dots, ka $B$ – naturāls skaitlis, $A=7\cdot{}B$ un $A$ ciparu summa divas
reizes lielāka par $B$ ciparu summu. Skaitli $C$ iegūst, pierakstot
skaitlim $A$ galā skaitli $B$.  
**(A)** atrast kaut vienu šādu $C$,  
**(B)** pierādīt, ka šādu $C$ ir bezgalīgi daudz,  
**(C)** pierādīt, ka katrs šāds $C$ dalās ar $9$,  
**(D)** vai $C$ noteikti dalās ar $27$?

<small>

* questionType:FindExample,Prove,ProveDisprove

</small>



# <lo-sample/> LV.VOL.2005.9.4

Dots, ka $a$ un $b$ – tādi reāli skaitļi, ka a+b ir vesels skaitlis un
$a^2+b^2=2$. Atrast visus šādus $a$ un $b$ pārus un pierādīt, ka citu bez
Jūsu atrastajiem nav.

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2005.9.5

Katrs naturāls skaitlis no $1$ līdz $2005$ ieskaitot nokrāsots vienā no $n$
krāsām. Ir zināms: ja $a$, $b$ un $c$ ir dažādi skaitļi, $a$ dalās ar $b$ un $b$
dalās ar $c$, tad $a$, $b$ un $c$ nav visi nokrāsoti vienā un tai pašā krāsā.
Atrast mazāko iespējamo $n$ vērtību.

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2005.10.3

Kādām funkcijām $f$ vienlaicīgi piemīt sekojošas īpašības:

a. $f$ definīcijas apgabals ir $\{1; 2; 3; 4; 5; 6; 7; 8; 9; 10\}$,  
b. $f$ vērtības ir naturāli skaitļi, kas nepārsniedz $100$,  
c. $f$ ir augoša funkcija,  
d. visiem $x$ un $y$ no definīcijas apgabala skaitlis 
   $x\cdot{}f(x)+y\cdot{}f(y)$ dalās ar $x+y$?

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2005.11.4

Dots, ka $p$ – pirmskaitlis. Pierādīt, ka apgalvojumi "eksistē tāds
vesels $x$, ka $x^2+x+3$ dalās ar $p$” un "eksistē tāds vesels $y$, ka
$y^2+y+25$ dalās ar $p$" vai nu abi ir pareizi, vai abi – nepareizi.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2005.12.4

Par skaitļu virkni $x_1, x_2, x_3, \ldots$ zināms, ka

* $x_1=1$
* $x_{2n}=1+x_n$ visiem naturāliem $n$
* $x_{2n+1} = \frac{1}{x_{2n}}$ visiem naturāliem $n$.

**(A)** Pierādiet, ka visi virknes locekļi ir dažādi.  
**(B)** Kuri skaitļi ir šīs virknes locekļi?

<small>

* questionType:Prove,FindAll

</small>



# <lo-sample/> LV.VOL.2006.9.1

Atrisināt vienādojumu $x + y = 1025$, ja $x$ un $y$ ir naturāli skaitļi –
skaitļa $640000$ dalītāji.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2006.10.2

Kādiem pirmskaitļiem $p$ un $q$, kas nepārsniedz $100$, 
visi skaitļi $p+6$, $p+10$, $q+4$, $q+10$ un
$p+q+1$ arī ir pirmskaitļi?

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2006.10.5

Kādam mazākajam naturālajam skaitlim $n$ piemīt šāda īpašība:
vienalga kādā veidā nokrāsojot dažus no naturālajiem skaitļiem $1$; $2$;
$3$; $\ldots$; $n$ baltus, bet pārējos – sarkanus, vienādojumam $x + y + z = t$
eksistē atrisinājums, kurā visu četru mainīgo vērtības ir vienā un tai
pašā krāsā (starp šīm vērtībām var būt arī savā starpā vienādas)?

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2006.11.2

Reālu skaitļu virknē $(a_n)$, $n = 1; 2; 3; \ldots$, pirmo locekli $a_1$ izvēlas
patvaļīgi, bet katru nākošo aprēķina pēc formulas $a_{n+1} = a_n(a_n+2)$ ,
$n=1; 2; 3; \ldots$. Kādas vērtības var pieņemt $a_{2006}$?

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2006.11.3

Atrisināt naturālos skaitļos vienādojumu $(x+y)(xy+1) = 2^z$.

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2006.12.1

Pierādīt, ka 
$$\left( 1 + tg 1^{\circ} \right) 
\left( 1 + tg 2^{\circ} \right) 
\left( 1 + tg 3^{\circ} \right) 
\ldots
\left( 1 + tg 44^{\circ} \right) 
\left( 1 + tg 45^{\circ} \right) = 2^{23}.$$

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2006.12.4

Naturāli skaitļi $m$ un $n$ apmierina sekojošu īpašību: $m$ dalās ar
jebkuru no skaitļiem $1; 2; 3; \ldots ; n$, bet nedalās ne ar $n + 1$, ne ar
$n + 2$, ne ar $n + 3$. Kādas ir iespējamās $n$ vērtības?

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2007.9.2

**(A)** Vai var gadīties, ka katram no kvadrātvienādojumiem $x^2 + px + q = 0$,
$x^2 + (p+1)x + (q+1) = 0$ un $x^2 + (p+2)x + (q+2) = 0$ abas saknes ir
veseli skaitļi?  
**(B)** Vai var gadīties, ka bez tam arī vēl katram no kvadrātvienādojumiem
$x^2 + (p-1)x + (q-1)=0$ un $x^2 + (p-2)x + (q-2) = 0$ abas saknes ir veseli
skaitļi? (Saknes var būt arī vienādas.)

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2007.9.5

![squares](LV.VOL.2007.9.5.png)

**(A)** Vai var 1.zīm. parādītās tabulas rūtiņās ierakstīt naturālus skaitļus no $1$
līdz $9$ (katrā rūtiņā – citu skaitli) tā, lai izpildītos īpašība: ja rinda un kolonna
apzīmētas ar vienādiem burtiem, tad tajās ierakstīto skaitļu reizinājumi ir
vienādi?  
**(B)** Vai var 2.zīm. parādītās tabulas rūtiņās ierakstīt naturālus skaitļus no $1$ līdz
$81$ (katrā rūtiņā – citu skaitli) tā, lai izpildītos tāda pati īpašība?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2007.10.1

Vai eksistē tādi naturāli skaitļi $x$ un $y$, ka izteiksmes
$x^2 - y^2 - x + y$ vērtība ir  
**(A)** $10$,  
**(B)** $2007$?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2007.10.3

Ja $n$ - naturāls skaitlis, kas lielāks par $1$, tad ar $x(n)$ apzīmējam lielāko
pirmskaitli, kas nepārsniedz $n$, bet ar $y(n)$ - mazāko pirmskaitli, kas
pārsniedz $n$. Piemēram, $x(6) = 5$; $x(5) = 5$; $y(5) = 7$. Pierādīt, ka
$$\frac{1}{x(2)\cdot{}y(2)}+
\frac{1}{x(3)\cdot{}y(3)}+
\frac{1}{x(4)\cdot{}y(4)}+\ldots+
\frac{1}{x(600)\cdot{}y(600)} = \frac{1}{2} - \frac{1}{601}.$$

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2007.10.5

Uz papīra lapas uzrakstīti n dažādi naturāli skaitļi, kas nepārsniedz $14$. Ir
zināms: katru no naturāliem skaitļiem $1;2;3;\ldots;27$ var izsacīt vai nu kā $x$,
vai kā $2x$, vai kā $x + y$, kur $x$ un $y$ - kaut kādi uzrakstītie skaitļi.
Pierādīt, ka  
**(A)** $n \geq 6$,  
**(B)** $n \geq 7$.

<small>

* questionType:Prove,Prove

</small>



# <lo-sample/> LV.VOL.2007.11.1

Dots, ka $n$ - naturāls skaitlis.  
**(A)** vai skaitļiem $n$ un $n+2007$ ciparu summas var būt vienādas?  
**(B)** vai skaitļiem $n$ un $n+199$ ciparu summas var būt vienādas?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2007.11.5

Reālu skaitļu virknē $a_1, a_2, a_3, \ldots$ dots, ka $a_{11} = 4$, 
$a_{22} = 2 un $a_{33} = 1$.
Bez tam visiem naturāliem $n$ pastāv vienādība
$$\frac{a_{n+3} - a_{n+3}}{a_n - a_{n+1}} = 
\frac{a_{n+3} + a_{n+3}}{a_n + a_{n+1}}.$$
Pierādīt, ka  
**(A)** neviens virknes loceklis nav $0$,  
**(B)** virkne ir periodiska,  
**(C)** $a_1^k + a_2^k + \ldots + a_{100}^k$
ir naturāla skaitļa kvadrāts, ja $k$ - patvaļīgs
naturāls skaitlis.

<small>

* questionType:Prove,Prove,Prove

</small>



# <lo-sample/> LV.VOL.2007.12.5

Naturālo skaitļu kopa sadalīta daļās tā, ka katrs naturāls skaitlis
nonācis tieši vienā daļā un katrā daļā ir bezgalīgi daudz skaitļu. Vai
noteikti starp daļām atradīsies tāda, kas satur jebkura naturāla skaitļa
daudzkārtni?
Atbildēt uz šo jautājumu, ja  
**(A)** daļu ir galīgs daudzums,  
**(B)** daļu ir bezgalīgi daudz.

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2008.9.1

Dots, ka $x$ un $y$ – naturāli skaitļi. 
Pierādīt, ka mazākais naturālais skaitlis, kas
dalās gan ar $x$, gan ar $y$, nav $x+y$.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2008.10.2

Kuriem naturāliem skaitļiem $x$ piemīt īpašība: 
nosvītrojot $x$ trīs pēdējos
ciparus, iegūst $\sqrt[3]{x}$?

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2008.10.3

Ja $x$ un $y$ – naturāli skaitļi (varbūt
vienādi), tad ar $[x,y]$ apzīmējam to
mazāko kopīgo dalāmo. Kādus
naturālus skaitļus $n$ var izteikt formā
$n = [x,y] + [y,z] + [z,x]$?

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2008.11.2

Atrisināt vienādojumu
$$\left| \ldots 
\left|\left|\left| x-1 \right| - 10 \right| - 10^2 \right| - 
\ldots - 10^{2007} \right| = 10^{2008}$$

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2008.11.3

Dots, ka $n$ – naturāls skaitlis un skaitļa 
$n^2$ decimālajā pierakstā viens
cipars ir "2", bet pārējie cipari ir "1". 
Pierādīt, ka $n$ dalās ar $11$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2008.12.3

Atrisināt naturālos skaitļos vienādojumu
$$x^2 + \left( x + 1 \right)^2 = y^2,\;\;\mbox{ja $x \leq 200$}.$$

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2009.9.2

Naturālu skaitli sauc par vienkāršu, 
ja tas ir divu (vienādu vai dažādu)
pirmskaitļu reizinājums. Piemēram, $9=3\cdot{}3$ ir vienkāršs, 
bet $18=2\cdot{}3\cdot{}3$ –
nav. Kāds lielākais daudzums pēc kārtas 
sekojošu naturālu skaitļu var visi būt vienkārši?

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2009.10.2

Apskatām virkni, kas augošā secībā satur visus
naturālos skaitļus, kuri nedalās ar $3$. Virknes
sākums tātad ir
$$1; 2; 4; 5; 7; 8; 10; 11; \ldots$$
Dots, ka $2n$ pēc kārtas ņemtu virknes locekļu summa ir $300$ 
($n$ – kaut kāds naturāls skaitlis). 
Kādas ir iespējamās $n$ vērtības?

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2009.11.1

Apskatām skaitļu virkni 
$F_1=1$; $F_2=2$; $F_{n+2}=F_{n+1}+F_n$ pie $n \geq 1$. 
Kāds lielākais šīs virknes elementu daudzums var veidot 
vienu aritmētisku progresiju? 

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2009.11.2

Atrast skaitļu $3^3-3$; $5^5-5$; $7^7-7$; $\ldots$; 
$2009^{2009}-2009$ lielāko kopīgo dalītāju.

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.VOL.2009.12.2

Katrīna uzrakstīja trīsciparu skaitli $n$, 
kura visi cipari ir dažādi un visi
atšķiras no $0$. Maija uzrakstīja visus 
piecus citus trīsciparu skaitļus,
kas izveidoti no tiem pašiem cipariem, no kā sastāv $n$. 
Maijas uzrakstīto skaitļu summa ir $3434$. 
Kāds var būt skaitlis $n$?


<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2010.9.1

Vai iespējams, ka kvadrātvienādojuma $x^2-ax+b=0$, 
$a$ un $b$ - naturāli skaitļi, saknes ir divu dažādu 
naturālu skaitļu kvadrāti?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2010.9.3

Par *skaistu* sauksim tādu naturālu skaitli, kas 
nedalās ne ar vienu no cipariem savā decimālajā pierakstā 
(neviens skaitlis nedalās ar $0$).
Kāds lielākais daudzums pēc kārtas sekojošu 
naturālu skaitļu visi var būt *skaisti*?

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.VOL.2010.11.4

Par Fibonači skaitļu virkni sauc virkni 
$F_1=1$; $F_2=1$; $F_{i+2}=F_i+F_{i+1}$ pie
$i \geq 1$. Pierādīt, ka katram naturālam 
skaitlim $n$ Fibonači skaitļu virknē ir
tāds virknes loceklis, kas dalās ar $n$.


<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2010.12.2

Dota skaitļu virkne $a_1=1$; $a_2 = 1$; 
$a_i = p\cdot{}a_{i-1} + q\cdot{}a_{i-2}$ pie $i \geq 3$ 
($p$, $q$ – doti naturāli skaitļi). Zināms, ka katram 
naturālam skaitlim $n$ eksistē tāds virknes loceklis $a_k$, 
ka $a_k$ dalās ar $n$.
Pierādīt, ka $p=q=1$.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2010.12.4

Naturāli skaitļi no $1$ līdz $k$ kaut kādā secībā 
ir uzrakstīti pa apli (katrs
tieši vienu reizi). Zināms, ka katram $d$, 
$2 \leq d \leq k-1$, izpildās sekojoša
īpašība: dalot ar $k$ visas iespējamās $d$ 
pēc kārtas sekojošu skaitļu
summas, iegūst visus iespējamos atlikumus.  
Vai ir iespējams, ka **(A)** $k=7$, **(B)** $k=8$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.VOL.2011.9.1

Doti $4023$ kvadrātvienādojumi formā $x^2 + ax + b = 0$. 
Starp visu vienādojumu $a$ vērtībām sastopami visi 
veselie skaitļi no $-2011$ līdz $2011$
(ieskaitot), tāpat arī starp $b$ vērtībām 
sastopami visi veselie skaitļi no $-2011$
līdz $2011$ (ieskaitot). Vai var gadīties, ka visiem 
dotajiem vienādojumiem saknes ir veseli skaitļi?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2011.9.3

Parādīt, ka no visiem trīsciparu skaitļiem, 
kuru pierakstā nav cipara $0$, var
izvēlēties 81 trīsciparu skaitli tā, lai vienlaicīgi 
izpildītos šādas trīs īpašības:

1. visos izvēlētajos skaitļos izsvītrojot pirmo ciparu, 
   katrs divciparu skaitlis, kas nesatur $0$, 
   tiek iegūts tieši vienu reizi;  
2. visos izvēlētajos skaitļos izsvītrojot otro ciparu, 
   katrs divciparu skaitlis, kas nesatur $0$, 
   tiek iegūts tieši vienu reizi;  
3. visos izvēlētajos skaitļos izsvītrojot trešo ciparu, 
   katrs divciparu skaitlis, kas nesatur $0$, 
   tiek iegūts tieši vienu reizi.


<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2011.10.5

Dots polinoms $f(x)$ ar veseliem koeficientiem. Vai iespējams, ka
$f(2011) = 100$, bet $f(11) = 1000$?

<small>

* topic:PolynomialDifferenceDivisibility
* topic:AdvancedIdentities
* questionType:ProveDisprove

</small>

<!--
concepts=integer-polynomial
questionType=ProveDisprove
-->



# <lo-sample/> LV.VOL.2011.11.3

Atrast visus pirmskaitļus $p$, kuriem skaitlis
$p^{p^2 - 5} + 2$
arī ir pirmskaitlis.

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2011.12.3

Pierādīt, ka neeksistē tādi naturāli skaitļi $n$ un $m$,
kuriem ir patiesa
vienādība $\left( 2n \right)^{2n}-1 = m^3$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2012.9.1

**(A)** Vai piecu pēc kārtas ņemtu naturālu 
skaitļu reizinājums var būt
skaitlis $20112012$?  
**(B)** Vai četru pēc kārtas ņemtu naturālu skaitļu
reizinājums var būt skaitlis $20112012$?


<small>

* questionType:ProveDisprove

</small>






# <lo-sample/> LV.VOL.2012.10.3

Naturāla skaitļa $N$ decimālajā pierakstā izmantots tikai cipars $6$.
Pierādīt, ka skaitļa $N^2$ decimālajā pierakstā nav cipara $0$.

<small>

* strategy:TrialAndError 
* topic:SeriesMembersSumsClosedFormulas
* topic:PeriodicDigitGroups
* questionType:Prove

</small>

<!--
concepts=full-square
questionType=Prove
-->



## Atrisinājums

Parādām, kā kāpināt $66\ldots{}66$ kvadrātā

$$6^2=36,\;\;66^2=4356=4455-99,\;\;666^2=443556=444555-999,\ldots$$

Pamatosim, ka 

$$\begin{aligned}
(\underbrace{6\ldots6}_n)^2 & = \overline{\underbrace{4\ldots{}4}_n\underbrace{5\ldots{}5}_n}-\underbrace{9\ldots{}9}_n, \\
\left( 6\cdot(10^n-1)/9 \right)^2 & = 10^n \cdot (4 \cdot (10^n - 1)/9) +(5 \cdot (10^n - 1)/9) - (10^n-1), \\
\frac{4}{9}(10^n-1)^2 & = 10^n \cdot \frac{4}{9}(10^n - 1) +\frac{5}{9}(10^n-1) - (10^n - 1), \\
4(10^n - 1)^2 & = 4\cdot{}10^{2n}-4\cdot{}10^n + 5\cdot{}10^n-5 - 9\cdot{}10^n +9.
\end{aligned}$$

Tātad $\overline{6\ldots6}^2$ pierakstā ir tikai cipari "4","3", "5" un "6":

$$(\underbrace{6\ldots6}_n)^2=\overline{\underbrace{4\ldots{}4}\_{n-1}3\underbrace{5\ldots{}5}\_{n-1}6}$$



# <lo-sample/> LV.VOL.2012.11.1

Pierādīt, ka eksistē bezgalīgi daudz naturālu 
skaitļu $a$, kuriem skaitlis
$n^4 + a$ ir salikts skaitlis visiem naturāliem 
skaitļiem $n > 1$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2012.11.4

Dota naturālu skaitļu virkne $(a_i)$, kur $a_1=5$ 
un katram $n>1$
$a_n = a_1 a_2 \ldots a_{n-1}+4$. 
Pierādīt, ka visiem $n \geq 1$ ir spēkā sakarība
$a_n - \sqrt{a_{n+1}}=2$.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2012.12.1

Divām naturālu skaitļu virknēm $(a_i)$ 
un $(b_i)$ katram $i \geq 1$ ir spēkā
sakarības:
$$a_{b_i} = b_{a_i}\;\;\mbox{un}\;\;a_i-b_i > 2012.$$
Atrast vienu šādu virkņu piemēru.

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.VOL.2012.12.3

Atrisināt naturālos skaitļos vienādojumu
$$n = \left\lfloor \frac{n}{2} \right\rfloor + 
\left\lfloor \frac{n}{3} \right\rfloor + 
\left\lfloor \frac{n}{4} \right\rfloor + 
\ldots + 
\left\lfloor \frac{n}{n+2012} \right\rfloor.$$ 
($\lfloor x \rfloor$ ir veselā daļa no $x$ – lielākais veselais skaitlis, kas nepārsniedz $x$;
piem., $\lfloor 3 \rfloor=3$, 
$\lfloor 4,6 \rfloor =4$, 
$\lfloor 0,2 \rfloor =0$ u.tml.)


<small>

* questionType:FindAll

</small>





# <lo-sample/> LV.VOL.2013.9.1

Atrast tādas ciparu $a$, $b$, $c$, $d$ 
vērtības, lai izpildītos vienādība
$\overline{abcd} + \overline{abc} + \overline{ab} + a = 2013$.

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2013.9.3

Dota virkne $a_1, a_2, a_3,\ldots$, kur 
$a 1 = a 2 = 1$ un visiem $n > 2$ izpildās
$$a_{n+1} = \left\lfloor
\frac{2a_n + a_{n-1}}{3} 
\right\rfloor + 4.$$
Aprēķināt $a_{2013}$.
($\lfloor x \rfloor$ ir veselā daļa no $x$ – 
lielākais veselais skaitlis, kas nepārsniedz $x$;
piemēram, $\lfloor 3 \rfloor =3$, 
$\lfloor 4,6 \rfloor =4$, 
$\lfloor 0,2 \rfloor =0$ u.tml.)

<small>

* questionType:FindExample

</small>




# <lo-sample/> LV.VOL.2013.10.1

Pierādīt, ka vienādojumam $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2}=\frac{1}{2}$ 
nav atrisinājuma naturālos skaitļos.

<small>

* topic:CountingUsingSymmetry
* topic:NumTheoryInequalityLargeIntervals
* questionType:Prove

</small>

<!--
genre=integer-equation
-->



## Atrisinājums

Sākotnējie secinājumi par mainīgajiem

Pieņemam, ka $a \leq b$ (ja tā nav, tad $a$ un $b$ samainām vietām).

* Ja $a \geq 6$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$
* Ja $a \leq 2$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$
* Gadījums $a=3$:

    - Ja $b=6$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$
    - Pie $b=7$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$

* Gadījums $a=4$:

    - Ja $b=4$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} > \frac{1}{2}$
    - Ja $b=5$, tad $\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2} < \frac{1}{2}$

Citas $b$ vērtības var neaplūkot, jo dotajam $a$ ($a=3$ vai $a=4$) izteiksme 
$\frac{1}{a} + \frac{1}{b} + \frac{1}{a^2+b^2}$ arvien samazinās tad, ja $b$ pieaug.



# <lo-sample/> LV.VOL.2013.10.4

Dota Fibonači skaitļu virkne
$F_1 = F_2 = 1$, $F_{i+2} = F_i + F_{i+1}$.  
Pierādīt, ka šajā virknē ir bezgalīgi daudz skaitļu, kas nav naturāla
skaitļa kvadrāti.

<small>

* topic:FibonacciNumbers
* topic:PeriodicRemainders
* topic:ModularArithmetic
* questionType:Prove

</small>


<!--
concepts=fibonacci-sequence,full-square
-->



## Atrisinājums

Atrodam Fibonači virknes atlikumus, dalot ar 3:

| $n$           | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| $F_n$         | 1    | 1    | 2    | 3    | 5    | 8    | 13   | 21   | 34   | 55   |
| $F_n \pmod 3$ | 1    | 1    | 2    | 0    | 2    | 2    | 1    | 0    | 1    | 1    |

Kā redzams tabuliņā $F_1 \equiv F_9 \equiv 1$ un $F_2 \equiv F_{10} \equiv 1$ pēc
$3$ moduļa (tāpēc sākot ar devīto locekli atkal atkārtosies tas pats astoņu 
atlikumu periods: $1,1,2,0,2,2,1,0$). 


* Neviens pilns kvadrāts nevar dot atlikumu $2$, dalot ar $3$, jo $(3k+1)^2$ un 
  $(3k+2)^2$ dod atlikumu $1$. 
* Fibonači virknē atlikums $2$, dalot ar $3$ parādīsies bezgalīgi bieži - 
  $x_3$, $x_5$, $x_6$ (un arī $x_{2+8k}$, $x_{2+8k}$, $x_{2+8k}$ jebkuram $k$).
* Visi šie nebūs naturāla skaitļa kvadrāti. 

Protams, **faktiski** kvadrātu starp Fibonači virknes locekļiem ir vēl krietni mazāk
(no augšminētajiem tikai $1=1^2$ un $144=12^2$). Bet šajā uzdevumā jāpamato, ka
no kādas vietas virknes uzvedība nevar izmainīties tā, ka visi 
pietiekami lielie virknes locekļi ir kvadrāti.


**Apgalvojums:** (1) Dalot ar jebkuru fiksētu skaitli, Fibonači virknes locekļu atlikumi veido periodu.  
(2) Periodiskajai atlikumu virknei nav priekšperioda un tajā bezgalīgi bieži parādās atlikums $0$.  

**Pierādījums:**  
(1) Katru Fibonači virknes locekļa atlikumu nosaka divu iepriekšējo locekļu atlikumi. 
Tiklīdz kā divu pēc kārtas sekojošu atlikumu pārītis sakrīt ar tādu, kas bijis agrāk, Fibonači virknes
atlikumi sāk atkārtoties, izveidojas cikls.  
(2) Atlikumu virknē nevar rasties priekšperiodi, 
jo atlikumus var rēķināt arī pretējā secībā: no $F_{i+2}$ un $F_{i+1}$ atlikumiem 
viennozīmīgi atrodot $F_i$ atlikumu. Tātad atlikumu virkne ir periodiska abos virzienos (nevis tikai 
kļūst periodiska, sākot no kādas vietas). Tā kā $0$-tais Fibonači skaitlis $F_0 = 0$, tad arī atlikums
$0$ parādīsies bezgalīgi bieži (vismaz vienreiz katrā periodā).



# <lo-sample/> LV.VOL.2013.11.1

Pierādīt, ka nav tādas naturālas n vērtības, ka 
$n^2 + 4n + 16$ dalās ar $36$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2013.12.3

Funkcija $f$ apmierina šādas prasības:  
1) $f$ ir definēta visiem veseliem nenegatīviem skaitļiem
un tās vērtības ir veseli skaitļi;  
2) katram $n$ ($n$ – vesels nenegatīvs skaitlis) 
izpildās sakarība
$$f(n) \cdot (f(n+1 )-2) = 4n^2-1.$$
Atrast visas šādas funkcijas $f$ un pierādīt, ka citu nav.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2013.12.4

Ar $d_i$, $i = 1,2,\ldots,k$, 
apzīmēsim visus naturālā skaitļa $n$ naturālos
dalītājus, pie tam $d_1 < d_2 < d_3 < \ldots < d_k$.
Dots, ka 
$d_3^2 d_4^2 \left( d_3^2 + d_4^2 \right) = n^2$. 
Atrast visas iespējamās $n$ vērtības.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2014.9.2

Naturālu skaitļu virknes pirmie trīs locekļi 
ir vienādi ar $1$, bet katrs
nākamais ir vienāds ar trīs iepriekšējo skaitļu summu.
Cik starp virknes
pirmajiem **(A)** $100$, **(B)** $2014$ locekļiem 
ir tādi, kas dalās ar $5$?

<small>

* questionType:FindCount,FindCount

</small>


# <lo-sample/> LV.VOL.2014.10.2

Atrast visas tādas vesela skaitļa $n$ vērtības, kurām gan 
$\frac{n^3+3}{n+3}$, gan $\frac{n^4+4}{n+4}$ ir veseli skaitļi.

<small>

* topic:PolynomialLongDivision
* topic:DivisorNumberAndSum
* questionType:FindAll

</small>


<!--
concepts=integer-polynomial
questionType=FindAll
-->



## Atrisinājums

Polinomus (tāpat kā naturālus skaitļus) var dalīt ar atlikumu. 

**Apgalvojums:**  Ja $A(x)$ un $B(x)$ ir polinomi, $A(x)$ pakāpe ir vismaz tikpat liela kā $B(x)$, 
tad eksistē divi citi polinomi $Q(x), R(x)$, kam $A(x)=Q(x)B(x)+R(x).  
$Q(x)$ sauc par *dalījumu*, bet $R(x)$ - par *atlikumu*.  
$R(x)$ pakāpe ir mazāka nekā $B(x)$ pakāpe.

Var gadīties, ka atlikums $R(x)=0$, ja $A(x)$ izdalās ar $B(x)$ bez atlikuma. 
Var arī gadīties, ka $R(x)$ ir konstante – t.i. $0$-tās pakāpes polinoms.

**Pirmais dalīšanas piemērs:**

$$\begin{aligned}
\frac{n^3+3}{n+3} & = \frac{n^2(n+3) - 3n^2 + 3}{n+3} = \\
                  & = n^2+\frac{-3n^2+3}{n+3} = \\
                  & = n^2+\frac{-3n(n+3)+9n+3}{n+3} = \\
                  & = n^2-3n+\frac{9n+3}{n+3} = \\
                  & = n^2-3n+\frac{9(n+3)-27+3}{n+3} = \\
                  & = n^2-3n+9+\frac{-24}{n+3}.
\end{aligned}$$

Vajag, lai $24$ dalās ar $n+3$.

**Otrais dalīšanas piemērs:**

$$\frac{n^4 + 4}{n+4} = n^3 - 4n^2 + 16n - 64 + \frac{256+4}{n+4}$$

Vajag, lai $260=2\cdot{}2\cdot{}5\cdot{}13$ dalās ar $n+4$ jeb 

$$n+4 \in \{ \ldots, -26, -20, -13, -10, -5, -4, -2, -1 \} \cup$$ 
$$\cup \{1, 2, 4, 5, 10, 13, 20, 26, \ldots \}$$


Atradīsim tos veselos $z$, kuriem dalījums $\frac{24}{x}$ (vai $\frac{260}{x}$) ir vesels?
Dalām pirmreizinātājos.

$$24 = 2^3\cdot{}3^1,\;\;260=2^2\cdot{}5\cdot{}13$$

Cik šādiem skaitļiem ir dalītāju?

**Apgalvojums:** Ja skaitlis $N$ dalās ar $2$ dažādiem pirmskaitļiem
($N=p_1^{a_1}p_2^{a_2}$) tad visi veselie $N$ dalītāji ir formā:  
$d = \pm p_1^{b_1}\cdot{}p_2^{b_2}$, kur $b_1 \leq a_1$ un $b_2 \leq a_2$.  
(Analoģiski arī lielākam pirmskaitļu skaitam.)

Piemēram, $N=24=2^3\cdot{}3^1$ dalītāji ir $d=2^{b_1}3^{b_2}$,
kur $b_1 \in \{ 0,1,2,3 \}$, $b_2 \in \{ 0,1 \}$.


Meklējam divu kopu šķēlumu:

$$n+3 \in \{ -24, -12, -8, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 8, 12, 24 \}$$

un

$$\begin{array}{l}
n+4 \in \{ \ldots, -26, -20, -13, -10, -5, -4, -2, -1 \} \cup \\
\cup \{1, 2, 4, 5, 10, 13, 20, 26, \ldots \} \\
\end{array}$$

No šejienes $(n+4) \in \{ -5, -2, -1, 2, 4, 5, 13 \}$ jeb
$n \in \{ -9, -6, -5, -2, 0, 1, 9 \}$.



# <lo-sample/> LV.VOL.2014.10.3

Ir pieejams neierobežots daudzums $7$ un $13$ centu pastmarku, 
kuras izmanto pasta sūtījumu apmaksāšanai. Diemžēl dažas summas nav 
iespējams apmaksāt tikai ar šīm pastmarkām (piemēram, ja sūtījums 
maksā $6$, $8$ vai $25$ centus). Kāda ir lielākā summa, kuru nav 
iespējams apmaksāt izmantojot tikai šīs pastmarkas?

<small>

* topic:ArithmeticSeriesAll
* topic:NumTheoryInequalityLargeIntervals
* questionType:FindOptimal

</small>

<!--
genre=optimization
concepts=linear-expression
-->



## Atrisinājums

Šķirojam atkarībā no tā, cik $13$ centu pastmarkas lietotas

* $0\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $0$
* $1\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $6$
* $2\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $5$
* $3\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $4$
* $4\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $3$
* $5\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $2$
* $6\cdot{}13 + 7a$ - dalot ar $7$, atlikums ir $1$

**Secinājums:** Lai nomaksātu $8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, \ldots$ centus, vajag
vismaz sešas $13$ centu markas. Mazākā šāda summa ir $6\cdot{}13 = 78$.  
Tātad summu $71$, kas šajā virknē ir
tieši pirms $78$ (un arī dod atlikumu $1$, dalot ar $7$), nevarēs nomaksāt, jo, lietojot mazāk par sešām
$13$-centu markām, nevar iegūt atlikumu $1$, dalot ar $7$. 




# <lo-sample/> LV.VOL.2014.11.2

Noteikt, kāds ir lielākais skaits, cik no pieciem
naturāliem skaitļiem $a$,
$a+14$, $a+22$, $a+32$, $a+46$ var būt pirmskaitļi.

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2014.11.5

Naturālus skaitļus $a$, $b$ un $c$ saista 
sakarība $c^2 = a^2 + b^2$. 
Pierādīt, ka katru no skaitļiem 
$c^2+ab$ un $c^2-ab$ var izteikt kā divu naturālu
skaitļu kvadrātu summu.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2014.12.2

Katram naturālam skaitlim $n$
ir definēta funkcija
$f(n)=\frac{1}{1} + \frac{1}{2} + \ldots + \frac{1}{n}$. 
Pierādīt, ka visiem $n > 1$ ir spēkā sakarība

$$n + f(1) + f(2) + \ldots + f(n-1) = n\cdot{}f(n).$$

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2014.12.5

Vai var atrast tādu naturālu $n$ vērtību, 
kam piemīt īpašība: visu skaitļa
$n$ naturālo dalītāju, izņemot $1$ un $n$, 
kvadrātu summa vienāda ar $n^2$.

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2015.9.1

Atrast visus tādus naturālus skaitļus $n$ un $m$, 
kuriem $\frac{2015}{n^4 - m^4}$ arī ir naturāls skaitlis!

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2015.9.3

Aija izvēlas naturālu skaitli $n \leq 100$ 
un veido skaitļu virkni, kur katru
nākamo virknes locekli iegūst pēc šāda likuma:

* ja $2n \leq 100$, tad virknes nākamais loceklis ir $2n$;
* ja $2n > 100$, tad virknes nākamais loceklis ir $2n-100$.

Ja virknē vēl kādreiz parādās skaitlis $n$, 
tad skaitli $n$ sauksim par
*patīkamu*. Cik pavisam ir patīkamu skaitļu, 
kas nepārsniedz $100$?
Piemēram, skaitlis $40$ ir patīkams, jo 
$\underline{40}; 80; 60; 20; \underline{40}; \ldots$, 
bet $25$ –
nav, jo $25; 50; 100; 100; \ldots$ 
(tālāk virknē nav skaitļu, kas atšķirīgi no $100$).

<small>

* questionType:FindCount

</small>



# <lo-sample/> LV.VOL.2015.10.2

Pierādīt, ka katram naturālam $n$ izteiksme
$3n^5+5n^4-8n$
dalās ar $10$.

<small>

* topic:DivisibilityProperties
* topic:ModularParity
* topic:ModularArithmetic
* questionType:Prove

</small>




## Atrisinājums

* Dalāmību ar $10$ pārbaudām, dalot ar $2$ un $5$
* $3n^5 + 5n^4 - 8n$ vienmēr ir pāru skaitlis (aplūko, ja $n$ ir pāru/nepāru)
* $3n^5 + 5n^4 - 8n$, dalot ar $5$ dod to pašu atlikumu, ko $3n^5 - 3n$

    - Ja $n$ dalās ar $5$, tad $3n(n^4-1)$ dalās ar $n$ (tātad arī ar $5$).
    - Visiem citiem $n$ atlikumiem, dalot ar $5$ (atlikumi $1,2,3,4$) iegūstam: $n^4 - 1$ dalās ar $5$

Jāievieto skaitļi $n=1,2,3,4$ izteiksmē $n^4-1$: vienmēr dalīsies ar $5$.  
Lielākiem skaitļiem ($n=6,7,8,9$) šie atlikumi sāks atkārtoties.




# <lo-sample/> LV.VOL.2015.11.1

Kvadrātvienādojuma
$$(1+\sqrt{5})x^2 - \sqrt[4]{7}\cdot{}(1 + \sqrt{5})^2x + \sqrt[4]{7} = 0$$
saknes ir skaitļi $a$ un $b$.
Pierādīt, ka izteiksmes
$a^4b + ab^4+ 3a^3b^2 + 3a^2b^3 + 16a^4b^3 + 16a^3b^4$
vērtība ir vesels skaitlis!

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2015.11.4

Naturāli skaitļi $a$, $b$ un $c$ ir 
savstarpēji pirmskaitļi un visi ir lielāki
nekā $50$. Zināms, ka $a+b$ dalās ar $c$ un 
$b+c$ dalās ar $a$. Atrast mazāko
iespējamo $b$ vērtību!

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.VOL.2015.12.3

Pierādīt, ka jebkuram naturālam nepāra skaitlim $n$ izteiksme
$2269^n + 2151^n + 1389^n - 1779^n$ dalās ar $2015$.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2016.9.1

Zināms, ka $x$ un $y$ ir tādi naturāli skaitļi, 
ka $xy^2$ ir naturāla skaitļa kubs.
Pierādīt, ka arī $x^2y$ ir naturāla skaitļa kubs!

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2016.9.4

Atrast skaitļa $\frac{2016^{2016}-3}{3}$
mazāko pirmreizinātāju!


<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.VOL.2016.9.5

Naturālu skaitļu virkni $(s_i)$ pēc parauga „2016” veido šādi:

* virknes pirmais loceklis $s_1$ ir $2$;
* virknes otrais loceklis $s_2$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_1$ un tā pierakstā ir cipars $0$;
* virknes trešais loceklis $s_3$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_2$ un tā pierakstā ir cipars $1$;
* virknes ceturtais loceklis $s_4$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_3$ un tā pierakstā ir cipars $6$.

Pēc tam meklētie cipari cikliski atkārtojas: 
2-0-1-6-2-0-$\ldots$. Virknes pirmie locekļi
ir $2; 10; 11; 16; 20; 30; 31; 36; 42; 50$.
Kādi ir četri nākamie skaitļi, kas virknē seko aiz skaitļa $2016$?

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.VOL.2016.10.1

Zināms, ka $x$ un $y$ ir tādi naturāli skaitļi, ka 
$xy^{10}$ ir naturāla skaitļa 33. pakāpe. 
Pierādīt, ka arī $x^{10}y$ ir naturāla skaitļa 33. pakāpe!

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2016.10.4

Pitagora trijstūrī visu malu garumi ir lielāki nekā $5$. 
Vai var gadīties, ka tā
**(a)** trīs malu, **(b)** divu malu garumi ir pirmskaitļi?  
*Piezīme.* Pitagora trijstūris ir taisnleņķa trijstūris, 
kam visi malu garumi ir naturāli skaitļi.

<small>

* questionType:ProveDisprove

</small>


## Ieteikums

Var izmantot paritāti - analizēt gadījumus, kad malu garumi ir pāra (nepāra skaitļi). 

## Ieteikums

Pitagora trijnieka skaitļus ievietot algebriskā identitātē - kvadrātu starpības formulā. 


## Atrisinājums

**(A)**  
Nē, trīs malu garumi nevar būt pirmskaitļi. Taisnleņķa trijstūrī malu garumi $a$, $b$ un $c$ 
apmierina Pitagora teorēmu: $a^2 + b^2 =  c^2$. 
Vismaz viens no skaitļiem $a$, $b$, $c$ ir pāra skaitlis, jo  
divu nepāra skaitļu $a^2$ un $b^2$ summa nevar būt nepāra skaitlis $c^2$.
Tā kā $a,b,c>5$, tad pāra skaitlis noteikti nav pirmskaitlis.

**(B)**
Jā, divu malu garumi var būt pirmskaitļi. Piemēram, der malu garumi $11, 60, 61$, 
jo divi no tiem ir pirmskaitļi un tiem izpildās Pitagora teorēmas nosacījums, tas ir, 
$11^2 + 60^2 = 61^2$ jeb $121 + 3600 = 3721$.

*Piezīme:* Paliek neatbildēts jautājums - kā uzminēt šos skaitļus $(11,60,61)$?
Bezgalīgi daudzus Pitagora trijniekus $(a,b,c)$, kam $b + 1 = c$ (katete par 1 vienību 
īsāka nekā hipotenūza) var iegūt, 
izmantojot algebrisku sakarību: 
$$a^2 = c^2 - b^2 = (c+b)(c-b) = (c + b) \cdot 1 = c+b.$$
Varam atrast dažādus blakusesošu skaitļu pārus $(b,c)$, kuru summa ir nepāra skaitļa kvadrāts $a^2$: 

* $3^2 = 9 = 4 + 5$, tāpēc $(a,b,c) = (3,4,5)$ ir Pitagora trijnieks.
* $5^2 = 25 = 12 + 13$, tāpēc $(a,b,c) = (5,12, 13)$ ir Pitagora trijnieks.
* $7^2 = 49 = 24 + 25$, tāpēc $(7,24,25)$ ir Pitagora trijnieks.
* $9^2 = 81 = 40 + 41$, tāpēc $(9, 40,41)$ ir Pitagora trijnieks. 
* $11^2 = 121 = 60 + 61$, tāpēc $(11,60,61)$ ir Pitagora trijnieks. 

Un trijnieks $(11,60,61)$ ir tāds, kurā atradās divi pirmskaitļi.
Der arī daži citi atrisinājumi, piemēram, $(19, 180, 181)$, 
Sk. [Eiklīda formula Pitagora trijniekiem](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple). 






# <lo-sample/> LV.VOL.2016.11.1

Zināms, ka $x$ un $y$ ir tādi naturāli skaitļi, ka 
$xy^{433}$ ir naturāla skaitļa 2016. pakāpe. 
Pierādīt, ka arī $x^{433}y$ ir naturāla skaitļa 2016. pakāpe!

<small>

* topic:FactorizationAndProperties
* topic:LinearSystemsTransforms
* questionType:Prove

</small>

<!--
concepts=full-powers
-->






## Atrisinājums

**Apgalvojums:** Skaitlis $N$ ir kāda naturāla skaitļa 2016. pakāpe tad un 
tikai tad, ja, sadalot pirmreizinātājos $N=p_1^{a_1}\cdot{}p_2^{a^2}\cdot\ldots\cdot{}p_k^{a_k}$, 
visi kāpinātāji $a_i$ dalās ar $2016$. 
(T.i. vai nu pirmskaitlis $p_i$ vispār nepiedalās $N$ sadalījumā, vai arī piedalās
ar kāpinātāju $a_i = 2016m$.)

**Dalīšana pirmreizinātājos:** Aplūkojam viena konkrēta pirmskaitļa $p$
pakāpi, ar kādu tas ietilpst $x$ un $y$ sadalījumā pirmreizinātājos. 
Pieņemsim, ka šie kāpinātāji ir attiecīgi $a$ un $b$:  
$$x=p^a\cdot\ldots,\;\;y=p^b\cdot\ldots,$$    
$$xy^{433} = p^{a+433b}\ldots,\;\;x^{433}y = p^{433a+b}.$$

**Apgalvojums:** Ja $a+433b$ dalās ar $2016$, tad arī $433a+b$ dalās ar $2016$. 

**Pierādījums:** Apzīmējam $a+433b=2016k$. Reizinām ar $433$:  
$433a+433^2b=2016\cdot{}433k$. 
Pamatosim, ka starpība starp šo un $433a+b$ arī dalās ar $2016$:
$$(433a+433^2b) - (433a+b)=(433^2-1)b = 187488b.$$
Viegli redzēt, ka $187488=2016\cdot{}93$ dalās ar $2016$.







# <lo-sample/> LV.VOL.2016.11.3

Pierādīt, ka katram naturālam skaitlim $n$ ($n>1$) var atrast
tādus naturālus skaitļus $x$ un $y$ ($x \leq y$), ka 
$$\frac{1}{n}=\frac{1}{x(x+1)}+\frac{1}{(x+1)(x+2)}+\cdots{}+\frac{1}{y(y+1)}.$$

<small>

* topic:StandardIdentities
* topic:TelescopicSums
* questionType:Prove

</small>

<!--
concepts=long-sums
-->

## Ieteikums

Pārveidot katru apakšizteiksmi par starpību.


## Atrisinājums

**Apgalvojums:** Ir spēkā identitāte $\frac{1}{n(n+1)} = \frac{1}{n}-\frac{1}{n+1}$.

Piemēri:  
$$\frac{1}{6}=\frac{1}{2\cdot{}3} = \frac{1}{2}-\frac{1}{3},$$
$$\frac{1}{12}=\frac{1}{3\cdot{}4} = \frac{1}{3}-\frac{1}{4},$$
$$\frac{1}{20}=\frac{1}{4\cdot{}5} = \frac{1}{4}-\frac{1}{5}.\;\cdots$$

Katru daļu, kuras saucējā ir divu sekojošu skaitļu reizinājums, 
var izteikt kā starpību.


Izmantojam šo identitāti, lai pārveidotu izteiksmi:

$$\frac{1}{n}=\frac{1}{x(x+1)}+\frac{1}{(x+1)(x+2)}+\cdots{}+\frac{1}{y(y+1)}.$$
$$\frac{1}{n}=\left( \frac{1}{x} - \frac{1}{x+1} \right) + \left( \frac{1}{x+1} - \frac{1}{x+2} \right) +$$
$$+\cdots+\left( \frac{1}{y} - \frac{1}{y+1} \right) = \frac{1}{x} - \frac{1}{y+1}$$

Vai jebkuru daļu $\frac{1}{n}$ var izteikt kā $\frac{1}{x} - \frac{1}{y+1}$?  
Izmantojam vienādības no iepriekšējā slaida. Piemēram, ja $n=5$:   

$$\frac{1}{5} = \frac{1}{4} - \frac{1}{20}.$$






# <lo-sample/> LV.VOL.2016.11.4

Naturālu skaitļu virkni $(s_i)$ pēc parauga "2016" veido šādi:

* virknes pirmais loceklis $s_1$ ir $2$;
* virknes otrais loceklis $s_2$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_1$ un tā pierakstā ir cipars $0$;
* virknes trešais loceklis $s_3$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_2$ un tā pierakstā ir cipars $1$;
* virknes ceturtais loceklis $s_4$ – mazākais naturālais skaitlis, 
  kas lielāks nekā $s_3$ un tā pierakstā ir cipars $6$.

Pēc tam meklētie cipari cikliski atkārtojas: 
2-0-1-6-2-0-$\ldots$. Virknes pirmie locekļi
ir $2; 10; 11; 16; 20; 30; 31; 36; 42; 50$.
Vai šajā virknē ir skaitlis **(A)** 2001, **(B)** 2006?

<small>

* questionType:ProveDisprove

</small>



## Atrisinājums

Pavisam ir četru veidu gājieni: $2 \rightarrow 0$ (skaitlis satur $2$ un meklējam nākamo skaitli, 
kas satur $0$), $0 \rightarrow 1$, $1 \rightarrow 6$ un $6 \rightarrow 2$. 
Ievērojam, ka neviens gājiens neļauj pārlēkt no skaitļa $N$ uz skaitli, kas ir lielāks
nekā $N+10$.

Virknē pēc izdarīta gājiena $1 \rightarrow 6$ būs kāds no skaitļiem $1906$, $1916$, $1926$ vai $1936$.
Aplūkosim, kāda ir tālākā skaitļu virkne katrā no gadījumiem:

* $1906 \xrightarrow{6 \rightarrow 2} 1912 \xrightarrow{2 \rightarrow 0} 1920 \xrightarrow{0 \rightarrow 1} 1921 \xrightarrow{1 \rightarrow 6} 1926 \xrightarrow{6 \rightarrow 2} 1927 \xrightarrow{2 \rightarrow 0} 1930 \xrightarrow{0 \rightarrow 1} 1931 \xrightarrow{1 \rightarrow 6} 1936$. 
* $1916 \xrightarrow{6 \rightarrow 2} 1920 \xrightarrow{2 \rightarrow 0} 1930 \xrightarrow{0 \rightarrow 1} 1931 \xrightarrow{1 \rightarrow 6}$. 

Kā redzams, visos gadījumos virknē pēc gājiena $1 \rightarrow 6$ ir skaitlis $1936$.
Tātad, turpinot virkni, iegūsim

$$1936 \xrightarrow{6 \rightarrow 2} 1942 \xrightarrow{2 \rightarrow 0} 1950 \xrightarrow{0 \rightarrow 1} 1951 \xrightarrow{1 \rightarrow 6} 1956  \xrightarrow{6 \rightarrow 2} 1962 \xrightarrow{2 \rightarrow 0} 1970 \xrightarrow{0 \rightarrow 1} 1971 \xrightarrow{1 \rightarrow 6} 1976,$$  
$$1976 \xrightarrow{6 \rightarrow 2} 1982 \xrightarrow{2 \rightarrow 0} 1990 \xrightarrow{0 \rightarrow 1} 1991 \xrightarrow{1 \rightarrow 6} 1996 \xrightarrow{6 \rightarrow 2} 2000 \xrightarrow{2 \rightarrow 0} 2001 \xrightarrow{0 \rightarrow 1} 2010.$$

Līdz ar to esam pierādījuši, ka skaitlis $2001$ pieder virknei, bet skaitlis $2006$ – nepieder.


# <lo-sample/> LV.VOL.2016.12.1

Zināms, ka $x$, $y$ un $z$ ir tādi naturāli skaitļi, 
ka $x^3y^5z^6$ ir naturāla skaitļa septītā
pakāpe. Pierādīt, ka arī $x^5y^6z^3$ ir naturāla skaitļa 
septītā pakāpe!

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2016.12.3

Pierādīt, ka vismaz viens no $18$ pēc kārtas sekojošiem 
trīsciparu skaitļiem dalās ar savu ciparu summu!

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2016.12.4

Divas funkcijas tiek definētas šādi:
$f(a) = a^2 + 3a + 2$ un
$g(b; c) = b^2 − b + 3c^2 + 3c$. 
Pierādīt, ka jebkurai naturālai $a$ vērtībai
iespējams atrast tādas naturālas $b$ un $c$ vērtības, 
ka $f(a) = g(b; c)$.


<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2017.9.1

Doti $63$ dažādi naturāli skaitļi, kuru summa 
ir $2017$. Atrodiet šos skaitļus un pamatojiet, 
ka citu nav!

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2017.9.3

Naturālā piecciparu skaitlī vienādus ciparus 
aizstāja ar vienādiem burtiem, bet dažādus ciparus – ar
dažādiem burtiem, un ieguva pierakstu $\overline{GANGA}$. 
Zināms, ka $\overline{GANGA}$, dalot ar $7$, dod atlikumu $A$, 
$\overline{GANGA}$, dalot ar $11$, dod atlikumu $N$, 
bet $\overline{GANGA}$, dalot ar $13$, dod atlikumu 
$G$, turklāt $G > A > N$. Kāds varēja būt
sākotnējais skaitlis?

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.VOL.2017.10.2

Dots pirmskaitlis, kas satur vismaz 4 dažādus ciparus. 
Pierādīt, ka tā ciparus var pārkārtot citā secībā tā, lai jauniegūtais skaitlis nebūtu pirmskaitlis!

<small>

* topic:DivisibilityRulesFor2And4
* topic:NotationShift
* topic:ModularArithmetic
* topic:ExhaustionMethod
* questionType:Prove

</small>

<!--
strategy=strengthen-the-hypothesis
concepts=primes
genre=digit-manipulation
-->

## Ieteikums 

Ar izslēgšanu atrod tos 4 ciparus, kuri nedod tūlītēju atrisinājumu.

## Ieteikums

Aplūko atsevišķi skaitli, ko veido pēdējie četri dažādie cipari un pārkārto ciparus tikai tur.

## Ieteikums

Atrast nelielu skaitli, ar kuru ērti pamatot dalāmību pēc ciparu pārkārtošanas.

## Ieteikums 

Samaisām ciparus tā, lai $1,3,7,9$ (katrs pa vienam) nonāktu skaitļa decimālpieraksta pēdējās $4$ pozīcijās. 


## Ieteikums

Šos pēdējos $4$ ciparus maisām tā, lai iegūtu vajadzīgo atlikumu.



## Atrisinājums

Ievērojam, ka jebkurš no cipariem $0,2,4,5,6,8$ skaitļa pierakstā ļauj 
to pārcelt uz beigām un iegūt skaitli, kas nav pirmskaitlis.
Tādēļ vienīgais interesantais gadījums ir tad, ja skaitļa pierakstā 
četri dažādie cipari ir  $1,3,7,9$, bet daži var būt arī atkārtoti. 

Pieļaujot gadījumus, ja skaitļa $n$ pierakstā daži no cipariem $1,3,7,9$ ir 
vairākas reizes, apzīmējam $n_1 = 10000x + 1379$, kur $1379$ ir
četri dažādie cipari, kas novietoti skaitļa beigās, bet 
$10000x$ ir skaitlis, ko veido visi atlikušie cipari, ja tādi ir. 
Skaitli $10000x$ atstāsim nemainīgu, 
bet pārkārtosim ciparus tikai skaitlī $1379$. To var izdarīt $4! = 24$ 
dažādos veidos - tās ir visas četru ciparu permutācijas.

* Ja sākotnējais pirmskaitlis ir $1973$, tad 
  $10000x = 0$, $n_1 = 1379$, $n_2 = 1397$ un visi citi skaitļi augošā secībā līdz 
  $n_{24} = 9731$. 
* Ja sākotnējais pirmskaitlis ir $31379$, tad 
  $10000x = 30000$, $n_1 = 31379$, $n_2 = 31397$ un visi citi augošā secībā 
  līdz $n_{24} = 39731$. (Visos šajos skaitļos mainās vietām tikai pēdējie četri cipari, 
  bet pirmais trijnieks paliek nemainīgs).


Pamatosim, ka neatkarīgi no $10000x$ vērtības ciparus $1379$ var pārkārtot tā, lai 
kāds no skaitļiem $n_i$ dalītos ar $7$. To var viegli redzēt, apskatot dažas no $24$ permutācijām 
in ievērojot, ka var iegūt jebkuru atlikumu, dalot ar $7$: 

[x % 7 for x in [1379, 1397, 1739, 1793, 1937, 1973, 3179, 3197, 3719, 3791, 3917, 3971]]
[0, 4, 3, 1, 5, 6, 1, 5, 2, 4, 4, 2]

* $1379 \equiv 0 \pmod 7$
* $1397 \equiv 4 \pmod 7$
* $1739 \equiv 3 \pmod 7$
* $1793 \equiv 1 \pmod 7$
* $1937 \equiv 5 \pmod 7$
* $1973 \equiv 6 \pmod 7$
* $3971 \equiv 2 \pmod 7$

*Piezīme.* Ievērosim, ka skaitlis $7$, ar ko mēģinām dalīt, ir izraudzīts "dabiski", jo dalāmība ar $2$ vai $5$ mūsu 
gadījumā (ja ir tikai cipari $1,3,7,9$) nav iespējama vispār. Dalāmību ar $3$ neiespaido ciparu 
mainīšana vietām (dalāmības pazīme ar $3$ jeb ciparu summa nav atkarīga no saskaitāmo secības). 
Dalāmība ar $11$ nemainās, ja samaina ciparus nepāru pozīcijās (vai arī pāru pozīcijās) -- 
tātad, arī dalot ar $11$ nevar sagaidīt daudzus atlikumus.



# <lo-sample/> LV.VOL.2017.11.4

Pierādīt, ka no jebkuriem $17$ naturāliem skaitļiem var 
izvēlēties $9$ skaitļus tā, lai to summa dalītos ar $9$.


<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2017.12.4

Naturālu skaitli sauksim par *skaistu*, ja tā visu 
naturālo dalītāju summa (ieskaitot $1$ un pašu skaitli) 
ir nepāra skaitlis. Atrast mazāko naturālo skaitli 
$k$ ar īpašību: starp jebkuriem patvaļīgi izvēlētiem 
$k$ skaistiem skaitļiem var izvēlēties divus 
dažādus skaitļus tā, lai to reizinājums būtu 
naturāla skaitļa kvadrāts!

<small>

* questionType:FindOptimal

</small>






# <lo-sample/> LV.VOL.2018.9.2

Izvēlēti trīs dažādi naturāli skaitļi un aprēķināti 
to reizinājumi pa pāriem, iegūstot trīs reizinājumus.
Pierādīt, ka šos reizinājumus dalot ar $4$, 
vismaz divi dod vienādus atlikumus!

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2018.10.3

Skaitļus $a,b,c$ sauksim par skaistu trijnieku, ja tiem piemīt šādas īpašības: 

* tie ir trīs pēc kārtas esoši naturāli skaitļi;
* katrs no tiem dalās ar savu ciparu summu. 

Piemēram, skaists trijnieks ir $8$, $9$, $10$. 

**(A)** Atrast tādu skaistu trijnieku, kurā mazākais skaitlis ir lielāks nekā $10$.  
**(B)** Pierādīt, ka eksistē bezgalīgi daudz skaistu trijnieku!

<small>

* topic:DivisibilityRulesFor2And4
* topic:DivisibilityRulesFor3And9
* topic:NotationInsert
* questionType:FindExample,Prove

</small>

<!--
concepts=sum-of-digits
-->



## Atrisinājums 

Apskatām vienkāršāku uzdevumu – "labu skaitļu" ķēdītes garumā $2$.  
Var aplūkot tādus skaitļus, kuru vidū var iespraust neierobežotu skaitu nuļļu.

* Pārītī $(20,21)$ pirmais skaitlis dalās ar $2$, bet otrais ar $3$.
* Tas pats pārītim $(200, 201)$, $(2000, 2001)$, utt.

Var izveidot Ķēdītes garumā 3 šādi:  
Skaitļi $110,111,112$ dalās ar attiecīgi ar $2,3,4$.

$$1\underbrace{0\ldots0}_n10,\;\;1\underbrace{0\ldots0}_n11,\;\;1\underbrace{0\ldots0}_n12$$




# <lo-sample/> LV.VOL.2018.11.3

Skaitļus $a, b, c, d, e$ sauksim par *skaistu piecinieku*, 
ja tiem piemīt šādas īpašības:

* tie ir pieci pēc kārtas esoši naturāli skaitļi;
* katrs no tiem dalās ar savu ciparu summu.

Piemēram, skaists piecinieks ir $6, 7, 8, 9, 10$.  
**(A)** Atrast tādu skaistu piecinieku, kurā mazākais skaitlis ir lielāks nekā $10$.  
**(B)** Pierādīt, ka eksistē bezgalīgi daudz skaistu piecinieku!


<small>

* questionType:FindExample,Prove

</small>



# <lo-sample/> LV.VOL.2018.12.3

Atrisināt veselos skaitļos vienādojumu $x^6 + 3x^3 + 1 = y^4$.

<small>

* questionType:FindAll

</small>



# <lo-sample/> LV.VOL.2019.9.3

Vai naturāla skaitļa kvadrāta ciparu summa var būt 
**(A)** $19$, **(B)** $2019$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.VOL.2019.10.1

Pierādīt, ka visus naturālos skaitļus, kas lielāki nekā $100$, 
var izteikt kā pirmskaitļa un salikta skaitļa summu!

<small>

* strategy:TrialAndError
* topic:ModularParity
* questionType:Prove

</small>

<!--
concepts=primes
-->



## Atrisinājums

Mēģinām izteikt, piemēram $101$ dažādos veidos:

$$101 \;=\; 2+99 \;=\; 3+98 \;=\; 4+97 \;=\;$$
$$\;=\; 5+96 \;=\; 7+94 \;=\; \cdots$$

Skaitļu, kas lielāki par $100$ ($101,102,103,\ldots$) ir bezgalīgi daudz; 
arī izteikt var ļoti daudzos veidos. 
Kārtību ievieš, šķirojot gadījumus:

* Ja $n$ ir pāru, tad $n-2$ noteikti nav pirmskaitlis. 
* Ja $n$ ir nepāru, tad $n-3$ noteikti nav pirmskaitlis.





# <lo-sample/> LV.VOL.2019.10.3

Pierādīt, ka nevienai naturālai $n$ vērtībai izteiksmes
$$13^n + 7^n + 2019$$
vērtība nav naturāla skaitļa kvadrāts!

<small>

* topic:PeriodicRemainders
* topic:DivisibilityRulesOther
* questionType:Prove

</small>


<!--
genre=integer-equation
concept=full-square
questionType=Prove
-->




# <lo-sample/> LV.VOL.2019.11.3

Pierādīt, ka nevienai naturālai n vērtībai izteiksmes 
$13^n + 10^n + 7^n + 3^n$ vērtība nav naturāla skaitļa
kvadrāts!

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2019.12.3

Pierādīt, ka nevienai naturālai $n$ vērtībai izteiksmes
$$4^n+5^n+6^n+7^n+8^n+9^n+10^n+11^n+12^n+13^n$$
vērtība nav naturāla skaitļa kvadrāts!

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.VOL.2019.12.5

Atrast  
**(A)** vienu tādu naturālu skaitļu pāri $(a;b)$,  
**(B)**$ trīs tādus naturālu skaitļu pārus $(a; b)$, $a < b$,  
ka lielākais skaitlis, ko nevar izteikt formā $an + bm$, 
kur $m$ un $n$ ir nenegatīvi veseli skaitļi, ir $2019$.

<small>

* questionType:FindExample,FindExample

</small>



# <lo-sample/> LV.VOL.2020.10.4

Aplūkojam skaitļu virkni $7; 737; 73737; 7373737; \ldots$, 
kuras pirmais loceklis ir $7$ un katru nākamo iegūst, iepriekšējam
pierakstot galā $37$. Pierādīt, ka neviens šīs virknes loceklis nedalās ar $17$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.VOL.2020.11.4

Zināms, ka trīsciparu skaitlis $\overline{abc}$ ir pirmskaitlis 
un ka vienādojumam $ax^2 + bx + c = 0$ ir divas reālas saknes. Vai var
gadīties, ka šīs saknes ir **(A)** veseli skaitļi, **(B)** racionāli skaitļi?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.VOL.2021.10.4

Uz tāfeles sākumā uzrakstīts vienādojums 
$2019x^2 + 2020x + 2021 = 0$. 
Divi spēlētāji pēc kārtas izdara
gājienus, pirmais spēlētājs sāk. Vienā gājienā var izvēlēties jebkuru no 
trim koeficientiem vienādojuma kreisajā pusē (pie $x^2$, pie $x$ 
vai brīvo locekli) un no tā atņemt vieninieku. Zaudē tas spēlētājs, pēc kura
gājiena uz tāfeles uzrakstītajam vienādojumam ir kāda vesela sakne. 
Kurš spēlētājs – pirmais vai otrais – uzvarēs, pareizi spēlējot?

<small>

* questionType:Algorithm

</small>



# <lo-sample/> LV.VOL.2021.11.3

Naturālu skaitli sauksim par *elegantu*, ja tā decimālajā pierakstā nav nevienas nulles 
un šis skaitlis dalās ar savu ciparu summu. 
(Eleganti ir visi viencipara skaitļi, kā arī, piemēram, skaitļi $36$ un $322$.) 
Pierādīt, ka ir bezgalīgi daudz elegantu skaitļu!

<small>

* questionType:Prove 

</small>


# <lo-sample/> LV.VOL.2022.10.3

Pierādīt, ka katram naturālam $K>1$ var atrast tādu naturālu skaitli, 
kas dalās ar $13$ un kura ciparu summa ir $K$.

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.VOL.2022.11.3

Sākumā uz papīra lapas uzrakstīts skaitlis $16$. Ja uz lapas ir

* uzrakstīts skaitlis $x$, tad uz tās atļauts uzrakstīt arī skaitli $x^2$;
* uzrakstīti skaitļi $x$ un $y$, tad uz tās atļauts uzrakstīt arī skaitli $|x-y|+1$.

Vai var panākt, lai uz lapas būtu uzrakstīts skaitlis $2022$ 
(neviens uzrakstītais skaitlis netiek nodzēsts)?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.VOL.2023.10.3

Rindā kaut kādā secībā uzrakstīti visi naturālie skaitļi no $1$ līdz $2023$. Vienā gājienā tiek sareizināti
katri divi blakus esošie skaitļi un zem tiem tiek uzrakstīta šī reizinājuma ciparu summa; šādā
veidā tiek iegūta jauna rinda, kurā ir par vienu skaitli mazāk nekā sākotnējā rindā. Pēc pirmā
gājiena tiek iegūta jauna rinda, kurā ir $2022$ skaitļi, pēc otrā gājiena tiek iegūta jauna rinda, kurā
ir $2021$ skaitlis utt., līdz pēc 2022. gājiena tiek iegūta pēdējā jaunā rinda, kurā ir tikai viens
skaitlis. Atrast visas iespējamās šī pēdējā skaitļa vērtības!

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.VOL.2023.11.4

Pierādīt, ka eksistē bezgalīgi daudz tādu naturālu skaitļu četrinieku $(a_1; b_1; a_2; b_2)$,
ka $a_1 \neq a_2$, $b_1 \neq b_2$ un
$$2^{a_1} - \left( b_1 \right)^2 = 2^{a_2} - \left( b_2 \right)^2 > 0.$$

<small>

* questionType:Prove

</small>

## Atrisinājums 

TBD


