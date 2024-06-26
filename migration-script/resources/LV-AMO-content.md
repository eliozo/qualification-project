# <lo-sample/> LV.AMO.2000.7.1

Dots, ka $a,b,c,d$ – naturāli skaitļi un $ab=cd$. Pierādīt, ka skaitli $a^2 + b^2 + c^2 + d^2$ 
var izsacīt kā divu veselu skaitļu kvadrātu summu. Vai to noteikti var izsacīt kā divu naturālu skaitļu kvadrātu summu?

<small>

* topic:StandardIdentities
* questionType:Prove
* concepts:square-Alg

</small>



## Atrisinājums

Izteiksmei var pieskaitīt $2ab$ un atņemt tam vienādo $2cd$, tad atdalīt kvadrātus:

$$a^2 + 2ab + b^2 + c^2 - 2cd + d^2 = (a+b)^2 + (c-d)^2.$$

Tādēļ vienmēr to var izteikt kā divu veselu skaitļu kvadrātu summu.

Ne vienmēr $a^2 + b^2 + c^2 + d^2$ var būt divu naturālu kvadrātu summa. Piemēram,
$1^2+1^2+1^2+1^2 = 4$ nav izsakāms kā $m^2 + n^2$, kur $m, n \in \mathbb{N}$.






# <lo-sample/> LV.AMO.2000.7.2

Atrast mazāko naturālo skaitli, kam visi cipari ir vienādi un kas dalās ar $49$?

<small>

* topic:LittleFermatAndEuler
* topic:IntegerFactorization
* genre:optimization
* questionType:FindOptimal
* concepts:decimal-notation,digit,divisibility

</small>



## Atrisinājums

Aprēķinām atlikumus, dalot $1,11,111,1111,11111,111111$ ar $7$. 
Atlikumi ir $1,4,6,5,2,0$. Tādēļ $111111$ dalās ar $7$ un 
septiņreiz lielāks skaitlis $777777$ dalās ar $49$. 

*Piezīme.* Fakts, ka $111111$ dalās ar $7$ seko no 
tā, ka $10^6 - 1 = 999999$ dalās ar $7$. 
Šī apgalvojuma vispārinājums ir Mazā Fermā teorēma: 
Katram pirmskaitlim $p$ un katram $a$, kas nedalās ar $p$, 
$a^{p-1} - 1$ dalās ar $p$. 



# <lo-sample/> LV.AMO.2000.7.4

Vai naturālos skaitļus

**(A)** no $1$ līdz $12$ ieskaitot,
**(B)** no $1$ līdz $50$ ieskaitot

var tā sadalīt pa pāriem, lai visas pāros ieejošo skaitļu summas būtu dažādas un katra no tām būtu pirmskaitlis?
(Piemēram, skaitļus no 1 līdz 6 varētu sadalīt tā: $1+2=3$, $3+4=7$, $5+6=11$).

<small>

* topic:PrimesDistribution
* topic:NumTheoryPigeonhole
* topic:ExhaustionMethod
* concepts:partition,primes,sum
* questionType:ProveDisprove
* genre:construction

</small>



## Atrisinājums

**(A)** Var sadalīt, piemēram, tā: $(1,4)$, $(2,5)$, $(3,8)$, $(6,7)$, $(9,10)$, $(11,12)$. 

**(B)** Bet $(1,100)$ ir tikai $24$ pirmskaitļi, kas lielāki par $2$.
Tāpēc nav iespējams izveidot $25$ pārus no skaitļiem $[1;50]$ tā, lai iegūtu $25$ dažādus 
pirmskaitļus -- tas būtu pretrunā ar Dirihlē principu.



# <lo-sample/> LV.AMO.2000.8.3

Uz katras no vairākām kartītēm uzrakstīts pa naturālam skaitlim (starp tiem var būt arī vienādi); uz visām kartītēm uzrakstīto skaitļu summa ir $100$. Vai noteikti var atrast tādas kartītes (varbūt vienu pašu), uz kurām uzrakstīto skaitļu summa ir $50$, ja kartīšu skaits ir

**(A)** $50$,
**(B)** $51$?


<small>

* topic:NumTheoryMathInduction
* topic:NumTheoryPigeonhole
* genre:construction
* questionType:ProveDisprove
* strategy:Interpretation
* concepts:sum

</small>




## Atrisinājums

**(A)** Ne vienmēr. Ir šāds pretpiemērs: $49$ kartītes ar "1" un $1$ kartīte ar "51". 

**(B)** Ieviešam sekojošu interpretāciju: Uzzīmējam riņķa līniju, kuru regulāra $100$-stūra
virsotnes sadala $100$ vienādos lokos. Vispirms nokrāsojam vienu no regulārā $100$-stūra virsotnēm sarkanu un 
atbilstoši katras kartītes skaitlim $n_i$ ($i=1,2,\ldots,51$) nokrāsojam sarkanu virsotni, kuru no 
iepriekšējās atdala $n_i$ vienādie loki (virzoties pretēji pulksteņa rādītāju virzienam).
Saliekot visus $51$ lokus, pēdējā sarkanā virsotne būs tā, kuru atzīmēja pašā sākumā 
(jo visu skaitļu $n_i$ summa ir tieši $100$). 

Esam ieguvuši $51$ sarkanu punktu uz riņķa līnijas. 
Visas $100$-stūra virsotnes var sagrupēt pa pāriem (kur vienā pārī ietilpst divas virsotnes, kuras 
ir tieši pretī viena otrai -- kuras atdala tieši $50$ riņķa līnijas loki). 
Pēc Dirihlē principa, vismaz vienā no pāriem abas pretējās virsotnes būs sarkanas, jo pāru 
pavisam ir $50$ (un katrai sarkanajai virsotnei nevar iedot pārī ne-sarkanu). 

Iegūtais pāris ar abām sarkanajām virsotnēm, kas ir tieši pretī viena otrai der kā atrisinājums, 
jo no vienas uz otru var aiziet tieši $50$ soļos, izmantojot skaitļus $n_i$. 




# <lo-sample/> LV.AMO.2000.9.2

Vai skaitli  
**(A)** skaitli $2$,  
**(B)** skaitli $\frac{1}{8}$  
var izsacīt kā četriem dažādiem naturālu skaitļu 
kvadrātiem apgriezto lielumu summu?

<small>

* concepts:sum,square-Alg,inverse-number
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2000.9.4

Apskatām pirmos $n$ naturālos skaitļus. No tiem jāizvēlas divus tā, 
lai to reizinājums būtu vienāds ar visu pārējo skaitļu summu. 
Vai tas ir iespējams, ja  
**(A)** $n=10$,  
**(B)** $n=15$?

<small>

* concepts:sum,product
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2000.10.2

Divu pirmskaitļu starpība ir $100$. Uzrakstot pirmo 
galā otrajam, atkal iegūst pirmskaitli. 
Atrast šos pirmskaitļus un pierādīt, ka citu bez 
Jūsu atrastajiem nav.

<small>

* concepts:primes,digit-manipulation
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2000.11.1

Dots, ka $x^2+y^2+z^2 = t^2$, kur $x,y,z,t$ – naturāli skaitļi. 
Cik no skaitļiem $x,y,z,t$ var būt pāra skaitļi?

<small>

* concepts:even-number
* questionType:FindCount

</small>




# <lo-sample/> LV.AMO.2000.11.4

Funkcijas $f(x)$ argumenti un vērtības ir naturāli skaitļi. 
Katram naturālam $x$ izpildās vienādība

$$f(f(x))+f(x) = 2x.$$

Atrast visas šādas funkcijas $f(x)$ un pierādīt, 
ka citu bez atrastajām nav.

<small>

* concepts:function,argument,value
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2000.12.2

Atrisināt naturālos skaitļos vienādojumu

$$\left( 2a+b \right) \cdot \left( 2b + a \right) = 2^c.$$

<small>

* concepts:equation
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2000.12.5

Naturālu skaitļu virkni sauc par $F$-virkni, 
ja tā ir augoša, bezgalīga un katrs tās loceklis, 
sākot ar trešo, vienāds ar abu iepriekšējo locekļu summu. 
Vai eksistē  
**(A)** galīgs daudzums,  
**(B)** bezgalīgs daudzums  
$F$-virkņu ar īpašību: katrs naturāls skaitlis pieder 
tieši vienai no tām.

<small>

* concepts:sequence
* questionType:ProveDisprove,ProveDisprove

</small>



# <lo-sample/> LV.AMO.2001.7.2

Naturālu skaitli sauc par simetrisku, ja tā pēdējais cipars 
nav $0$ un, uzrakstot tā ciparus apgrieztā secībā, 
skaitlis nemainās. Piemēram, $1221$ ir simetrisks skaitlis, bet $1231$ - nav.  
**(A)** pierādiet: ja simetrisks sešciparu skaitlis dalās ar $13$, tad tas dalās arī ar $7$,  
**(B)** vai taisnība, ka katrs simetrisks sešciparu skaitlis, kas dalās ar $7$, dalās arī ar $13$?

<small>

* topic:DivisibilityRulesOther
* topic:NotationPolynomial
* topic:IntegerCongruence
* concepts:palindrome,decimal-notation
* questionType:Prove,ProveDisprove

</small>




## Atrisinājums

**(A)** $13$ dala $\overline{abcabc}=1001\cdot{}\overline{abc}$ un 
arī $\overline{abccba}$ (tas ir dots). 
Atņemot abus skaitļus, iegūstam $13 \mid 99|a-c|$ un $a=c$.

**Piezīme:** Ievērojam, ka $\overline{abccba}$ var izteikt 
$100001a + 10010b + 1100c = 13\cdot (\ldots ) + 5(a-c)$. 
Tad $a-c$ dalās ar $13$ un $a=c$; aizstāj $c$ un dala ar $7$.

**(B)** $108801$ ir pretpiemērs.





# <lo-sample/> LV.AMO.2001.8.3

Andrim vajadzēja sareizināt divus dažādus pozitīvus trīsciparu skaitļus. 
Izklaidības pēc viņš tos vienkārši uzrakstīja vienu otram galā. 
Iegūtais sešciparu skaitlis izrādījās $3$ reizes lielāks par reizinājumu, 
kuru Andrim vajadzēja iegūt. Kādu sešciparu skaitli Andris uzrakstīja?

<small>

* topic:NotationShift
* topic:StandardIdentities
* topic:NumTheoryInequalityMethod
* questionType:FindAll
* genre:digit-manipulation
* concepts:decimal-notation

</small>




## Atrisinājums

* Apzīmē $a$ un $b$ - abi ir trīsciparu skaitļi
* Ja $1000a+b=3ab$, tad $b/a=3b-1000$. 
* Veseli trīsciparu skaitļi $a,b$ rodas tikai tad, ja $b=334$.



# <lo-sample/> LV.AMO.2001.9.4

Dots, ka $x,y,z$ - naturāli skaitļi un katrs no 
skaitļiem $xy-z$, $xz-y$ un $yz-x$ dalās ar $3$. 
Pierādiet, ka $x^2+y^2+z^2$ dalās ar $3$.

<small>

* concepts:divisibility
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2001.10.3

Kāds ir mazākais pirmskaitlis $p$, kuram nevar atrast tādus 
nenegatīvus veselus skaitļus $x$ un $y$, ka 
${\displaystyle p = \left| 2^x - 3^y \right|}$?

<small>

* concepts:primes
* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2001.11.3

Skaitļu virknes elementi ir naturāli skaitļi. 
Pirmo elementu izvēlas patvaļīgi, bet katrs nākošais 
elements ir vienāds ar iepriekšējā elementa naturālo dalītāju skaitu. 
(Piemēram, ja virknes pirmais elements ir $14$, 
tad virkne ir $14, 4, 3, 2, 2, 2, \ldots$).
Kāds var būt virknes pirmais elements, 
ja neviens tās elements nav naturāla skaitļa kvadrāts?

<small>

* concepts:sequence,divisibility,square-Alg
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2001.12.2

Atrisināt naturālos skaitļos vienādojumu $(2a+b)(2b+a)=2c$.

<small>

* concepts:equation
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2002.7.4

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam 
naturālam skaitlim no $1$ līdz $8$ ieskaitot. 
Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut 
viens jau uzrakstīts skaitlis. 
Kas nevar izdarīt gājienu, zaudē.
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* genre:game
* concepts:divisibility
* questionType:Algorithm
* strategy:Contradiction

</small>



## Atrisinājums

Ja skaitļiem $\{ 2,3,\ldots,7,8\}$ uzvar 1.sp., 
atkārto viņa stratēģiju. Ja uzvar 2.spēlētājs, sāk ar gājienu "$1$".


## Atrisinājums

Sāk ar $2$, tad uz katru $(5; 7)$, $(6; 8)$ un $(4; 3)$ atbild ar otru skaitli no pārīša.



# <lo-sample/> LV.AMO.2002.7.5

Kādu lielāko daudzumu dažādu naturālu skaitļu, kas nepārsniedz $100$, var izvēlēties tā, 
lai nekādu divu izvēlēto skaitļu starpība nebūtu ne $3$, ne $4$, ne $7$?

<small>

* topic:SequencePeriodicity
* topic:NumTheoryPigeonhole
* genre:optimization
* questionType:FindOptimal
* strategy:ExhaustiveSearch,Symmetry

</small>





## Atrisinājums

Ja $>30$, tad no $10$ sk., jāizvēlas $4$. No $\{1,4,8\}$, $\{2,5,9\}$, $\{2,6,10\}$, $\{7\}$ 
jāņem pa $1$ – neiespējami.

Lai izvēlētos $4$ no *ABCABCXABC*, jāņem arī $X$, bet līdzīgi arī *ABCYABCABC* 
un $X$,$Y$ starpība ir $3$.






# <lo-sample/> LV.AMO.2002.8.2

Andrim vajadzēja sareizināt divus dažādus divciparu skaitļus. Izklaidības pēc 
viņš tos vienkārši uzrakstīja vienu otram galā. Iegūtais četrciparu skaitlis izrādījās 
$3$ reizes lielāks par reizinājumu, kuru Andrim vajadzēja iegūt. 
Kādu četrciparu skaitli Andris uzrakstīja?

<small>

* topic:NotationShift
* topic:StandardIdentities
* topic:NumTheoryInequalityMethod
* seeAlso:LV.AMO.2001.8.3
* questionType:FindAll
* genre:digit-manipulation
* concepts:decimal-notation

</small>



## Atrisinājums

Ja $100a+b=3ab$, tad $b/a=3b-100$. Abi cipari $a,b$ ir veseli tad, ja $b=34$.



# <lo-sample/> LV.AMO.2002.8.3

Par Fibonači skaitļiem sauc skaitļus $1; 2; 3; 5; 8; \ldots$ 
(katru nākošo iegūst, saskaitot divus iepriekšējos).
Vai var pastāvēt vienādība $a+b=c+d$,
ja $a$, $b$, $c$, $d$ ir dažādi Fibonači skaitļi?

<small>

* topic:NumTheoryExtremeElement
* concepts:fibonacci-sequence
* questionType:ProveDisprove
* strategy:ExtremeElement

</small>





## Atrisinājums

Ja $d$ ir lielākais no Fibonači skaitļiem, tad $a+b=d$, 
kur $a$,$b$ ir Fibonači skaitļi tieši pirms $d$. Bet tā kā $c>0$ arī 
ir Fibonači skaitlis, tad $a+b<c+d$. 



# <lo-sample/> LV.AMO.2002.9.3

Dots, ka $x, y, z$ naturāli skaitļi un katrs no 
skaitļiem $xy-z$, $xz-y$ un $yz-x$ dalās ar $3$. 
Pierādīt, ka $x^2+y^2+z^2$ dalās ar $3$.

<small>

* seeAlso:LV.AMO.2001.9.4
* concepts:divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2002.10.3

Katrs naturāls skaitlis nokrāsots vienā krāsā. 
Ir zināms: ja divu naturālu skaitļu starpība ir pirmskaitlis, 
tad tie ir nokrāsoti dažādās krāsās. 
Kāds ir mazākais iespējamais krāsu skaits?

<small>

* concepts:primes
* questionType:FindOptimal

</small>



# <lo-sample/> LV.AMO.2002.11.3

Zināms, ka naturāls skaitlis $n$ dalās ar pirmskaitli 
$p$ un $p>\sqrt{n}$. Pierādīt, ka ne $n-1$, $n^3-1$ 
nav divu tādu naturālu skaitļu reizinājums, kuru starpība ir $2$.

<small>

* concepts:primes
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2002.12.4

Skaitļu virkni $a_1, a_2, a_3, \ldots$ veido sekojoši 
$a_1=0$; $a_2=1$; pie $n>2$ skaitli $a_n$ iegūst, 
pierakstot skaitlim $a_{n-1}$ pa labi galā skaitli $a_{n-2}$. 
(Piemēram, $a_3=10$; $a_4=101$, $a_5=10110$ utt.) 
Kādiem $n$ skaitlis $a_n$ dalās ar $11$?

<small>

* concepts:sequence
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2003.7.3

Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam 
skaitlim no $1$ līdz $9$ ieskaitot. Nedrīkst rakstīt skaitļus, ar kuriem dalās 
kaut viens jau uzrakstīts skaitlis. Kas nevar izdarīt gājienu, zaudē. 
Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

<small>

* genre:game
* concepts:divisibility
* questionType:Algorithm
* strategy:Contradiction

</small>



## Atrisinājums

Ja skaitļiem $\{ 2,3,\ldots,8,9\}$ 
uzvar 1.spēlētājs, atkārto viņa stratēģiju. Ja uzvar 2.spēlētājs, 
sāk ar gājienu "1".


## Atrisinājums

Sāk ar $2$, tad katrā grupā $(5;7)$, $(3;8)$ un $(4;6;9)$ uzvar izolēti.






# <lo-sample/> LV.AMO.2003.7.5

Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
Vai tas var būt $0$, ja **(A)** $n=8$, **(B)** $n=9$?

<small>

* topic:InvariantParity
* topic:SeriesMembersSumsClosedFormulas
* topic:ExhaustionMethod
* concepts:absolute-value
* genre:making-moves
* questionType:Algorithm
* strategy:Invariant

</small>

## Ieteikums

Skaitļu komplektā var ar programmēšanas līdzekļiem 
atrast mazāko, ko var iegūt ar šiem gājieniem.



## Atrisinājums

**(A)**
Pie $n=8$ sākotnējais skaitļu komplekts ir $\{ 1,2,3,4,5,6,7,8 \}$. 
Izdarām šādus gājienus: 

* $(4,5) \rightarrow 5^2 - 4^2 = 9$, jaunie skaitļi ir $\{1,2,3,6,7,8,9\}$,
* $(7,9) \rightarrow 9^2 - 7^2 = 32$, jaunie skaitļi ir $\{1,2,3,6,8,32\}$,
* $(2,6) \rightarrow 6^2 - 2^2 = 32$, jaunie skaitļi ir $\{1,3,8,32,32\}$,
* $(1,3) \rightarrow 3^2 - 1^2 = 8$, jaunie skaitļi ir $\{8,8,32,32\}$,
* $(8,8) \rightarrow 8^2 - 8^2 = 0$, jaunie skaitļi ir $\{0,32,32\}$,
* $(32,32) \rightarrow 32^2 - 32^2 = 0$, jaunie skaitļi ir $\{0,0\}$,
* $(0,0) \rightarrow 0^2 - 0^2 = 0$, paliek skaitlis $\{ 0 \}$.


**(B)**
Ja $n=9$, tad visu skaitļu summa ir $1+2+\ldots+9=45$. 
Izdarot gājienu (nodzēšot $a$ un $b$ un uzrakstot $\left| a^2-b^2 \right|$) 
summas paritāte nemainās. Tāpēc pēc katra soļa visu uz tāfeles uzrakstīto 
skaitļu summa būs nepāra skaitlis.





# <lo-sample/> LV.AMO.2003.8.3

Kādā lielākajā daudzumā dažādu naturālu saskaitāmo, 
kas visi lielāki par $1$, var sadalīt skaitli $56$ tā, lai katru divu 
saskaitāmo lielākais kopīgais dalītājs būtu $1$?

<small>

* topic:NumTheoryExtremeElement
* topic:PrimesDistribution
* genre:optimization
* concepts:gcd,coprimes
* questionType:FindOptimal
* strategy:ExtremeElement

</small>



## Atrisinājums

Ar sešu saskaitāmo summu var izteikt $56$ šādi:
$3,5,7,11,13,17$. 

Ar septiņiem vai vairāk saskaitāmajiem nevar, jo 
pat izvēloties visus septiņus mazākos pirmskaitļus, to 
summa ir $2+3+5+7+11+13+17 = 58 > 56$. 



# <lo-sample/> LV.AMO.2003.8.5

Uz katras no divām lapām jāuzraksta pa $n$ veseliem pozitīviem skaitļiem. 
Visiem $2n$ uzrakstītajiem skaitļiem jābūt dažādiem. Pie tam uz lapām uzrakstīto 
skaitļu summām jābūt vienādām savā starpā, un uzrakstīto skaitļu 
kvadrātu summām arī jābūt vienādām savā starpā.  
Vai tas iespējams, ja **(A)** $n=3$, **(B)** $n=4$, **(C)** $n=2003$?

<small>

* topic:SequencePeriodicity
* topic:ExhaustionMethod
* topic:StandardIdentities
* concepts:square
* questionType:ProveDisprove,ProveDisprove,ProveDisprove
* strategy:Symmetry

</small>





## Atrisinājums

**(A)** Aplūkojam divas grupas: $\{ 1,5,6 \}$, $\{ 2,3,7 \}$.
Abās grupās skaitļu summas ir $12$, bet kvadrātu summas ir $62$. 

**(B)** Aplūkojam grupas $(1,4,6,7)$, $(2,3,5,8)$. 

**(C)** Arī šai vērtībai $n = 2003$ to var izdarīt. 
Pamatosim ar indukciju, ka to var izdarīt katram $n = 4m+3$, ja $m \geq 0$ ir 
vesels skaitlis.

*Bāze:* Pie ie $n=3$ var izdarīt kā punktā **(A)**.  
*Induktīvais pieņēmums:* Pieņemsim, ka to var izdarīt kādai vērtībai $n=3+4m$. 
Pamatosim, ka var izdarīt arī lielākai vērtībai:
$n=3+4(m+1)$.
*Induktīvā pāreja:* Sadala pirmos $3+4m$ skaitļus atbilstoši induktīvajam pieņēmumam. 
Ar $k$ apzīmējam lielāko no skaitļiem, kas izmantoti šajā konstrukcijā. 
Pievienosim astoņus jaunus skaitļus, tos sadalot grupās (līdzīgi kā **(B)** punktā):

$$(k+1, k+4, k+6, k+7)\;\;\text{un}\;\;(k+2, k+3, k+5, k+8)$$. 

Visi šie astoņi skaitļi ir savstarpēji dažādi. 

* Vienā grupā summa ir $(k+1) + (k+4) + (k+6) + (k+7) = 4k + 18$. Tāda pati summa ir arī 
  otrajā grupā: $(k+2) + (k+3) + (k+5) + (k+8)$. 
* Vienā grupā kvadrātu summa ir $(k+1)^2 + (k+4)^2 + (k+6)^2 + (k+7)^2 = 4k^2 + 36k + 102$. 
  Arī otrā grupā: $(k+2)^2 + (k+3)^2 + (k+5)^2 + (k+8)^2 = 4k^2 + 36k + 102$. 

Tāpēc pievienojot jaunās abas grupas katru savai pusei, gan skaitļu summas, gan 
to kvadrātu summas joprojām sakritīs.


# <lo-sample/> LV.AMO.2003.9.3

Noskaidrot, kādiem dažādiem pirmskaitļiem 
$p_1, p_2, \ldots, p_n$ pastāv īpašība: 
$p_1p_2p_3\ldots{}p_n$ dalās ar 
$(p_1-1)(p_2-1)\ldots(p_n-1)$.

<small>

* concepts:primes,divisibility
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2003.10.3

Dots, ka $n$ - vesels pozitīvs skaitlis un skaitļi 
$2n+1$ un $3n+1$ ir veselu skaitļu kvadrāti.  
**(A)** atrodiet kaut vienu tādu $n$,  
**(B)** vai $5n+3$ var būt pirmskaitlis?

<small>

* concepts:primes,square-Alg
* questionType:FindExample,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2003.11.3

Vai eksistē tāds naturāls skaitlis $n$, 
ka $6^n-1$ dalās ar $4^n-1$?

<small>

* concepts:divisibility
* questionType:ProveDisprove

</small>



# <lo-sample/> LV.AMO.2003.12.2

Vai eksistē tāds vesels pozitīvs skaitlis $n$, 
ka skaitlim $n^2$ ir tikpat daudz naturālu dalītāju, 
kas dod atlikumu $1$, dalot ar $3$, 
cik naturālu dalītāju, kas dod atlikumu $2$, dalot ar $3$?


<small>

* concepts:divisibility,divisors
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2004.7.3

Kādam mazākajam naturālajam $n$ visas daļas

$$\frac{5}{n+7}, \frac{6}{n+8}, \frac{7}{n+9}, \ldots, \frac{35}{n+37}, \frac{36}{n+38}$$

ir nesaīsināmas?

<small>

* topic:EuclideanAlgorithm
* topic:PrimesDistribution
* concepts:fractions,gcd
* questionType:FindOptimal

</small>





## Atrisinājums

Izmantojam Eiklīda algoritmu.

* Visas daļas izskatās šādi: $\frac{k}{n+(k+2)}$. 
* Vajag, lai $\mbox{LKD}(k,n+(k+2))=1$. 
* $\mbox{LKD}(k,n+(k+2))=\mbox{LKD}(k,n+2)=1$, $k=5,\ldots,36$.

$n+2=37$ ir savstarpējs pirmskaitlis ar visiem $k$, t.i. $n=35$.




# <lo-sample/> LV.AMO.2004.8.3

Dots, ka $A$ un $B$ – naturāli divciparu skaitļi. Skaitli $X$ iegūst, 
pierakstot skaitlim $A$ galā skaitli $B$; skaitli $Y$ iegūst, 
pierakstot skaitlim $B$ galā skaitli $A$. 
Dots, ka $X-Y$ dalās ar $91$. Pierādīt, ka $A=B$.

<small>

* topic:NotationShift
* topic:IntegerFactorization
* concepts:decimal-notation,divisibility
* genre:digit-manipulation
* questionType:Prove

</small>






## Atrisinājums

$(100A+B)-(100B+A) = 99(A-B)$ un $A-B$ dalās ar $91$. Divciparu skaitļiem tas nozīmē $A=B$.





# <lo-sample/> LV.AMO.2004.8.5

Virknē augošā kārtībā izrakstīti naturālie skaitļi no $1$ līdz $2004$ ieskaitot, 
katrs vienu reizi. Izsvītrojam no tās skaitļus, kas atrodas 
$1., 4., 7., 10., \ldots$ vietās. No palikušās virknes atkal
izsvītrojam skaitļus, kas tajā atrodas $1., 4., 7., \ldots$ vietās. 
Ar iegūto virkni rīkojamies tāpat, utt.,
kamēr paliek neizsvītrots viens skaitlis. Kurš tas ir?

<small>

* topic:MultiplesInInterval
* topic:DefiningRecurrentSequences
* topic:NonlinearRecurrences
* concepts:sequence
* genre:making-moves
* questionType:FindAll
* strategy:WorkingBackwards

</small>





## Atrisinājums

Pirms pēdējās izsvītrošanas pēdējais skaitlis bija \#2, pirms tam \#3, \#5, \#8, \#12, utt.
**#GadījumuPārlase** Pēc $n$ svītrošanām pirmais palikušais ir $x_n$. Pamato $x_{n+1} = \left\lceil 3x_n/2 \right\rceil$ pāru un nepāru $x_n$.



# <lo-sample/> LV.AMO.2004.9.5

Kvadrāts sastāv no $n \times n$ rūtiņām. 
Katrā rūtiņā jāieraksta viens no skaitļiem $-1; 0; 1$ tā, lai $n$ rindās
un $n$ kolonnās ierakstīto skaitļu summas visas būtu dažādas.
Vai to var izdarīt, ja **(A)** $n=4$; **(B)** $n=5$?

<small>

* concepts:sum
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2004.10.3

Dots, ka $n$ – naturāls skaitlis.  
**(A)** pierādīt, ka $n^2 + 11 n + 30$ nav naturāls skaitlis,  
**(B)** atrast šī skaitļa pirmo ciparu aiz komata atkarībā no $n$.

<small>

* questionType:Prove,FindAll

</small>


# <lo-sample/> LV.AMO.2004.10.5

Vai, izmantojot tikai $3$ dažādus ciparus, var uzrakstīt 
$16$ trīsciparu skaitļus, kas visi dod dažādus
atlikumus, dalot ar $16$?

<small>

* concepts:remainder,divisibility
* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2004.11.1

Vai eksistē tāds naturāls skaitlis $n$, ka $2004^n-1$ dalās ar $1500^n-1$?

<small>

* concepts:divisibility
* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2004.12.1

Dots, ka $n$ – naturāls skaitlis, $n>1$. Vai izteiksmi

$$\left( x^n + x^{n-1} + \ldots + x + 1 \right)^2 - x^n$$

noteikti var izsacīt kā divu polinomu reizinājumu tā, 
lai neviens no šiem polinomiem nebūtu
konstante un visi abu polinomu 
koeficienti būtu veseli skaitļi?

<small>

* concepts:integer-polynomial
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2004.12.3

Funkcijai $f(n)$ gan argumenti, gan vērtības 
ir naturāli skaitļi, un katriem diviem naturāliem
skaitļiem $x$ un $y$ pastāv vienādība

$$xf(y)+yf(x)=(x+y)f(x^2+y^2).$$

Atrast visas šādas funkcijas $f$ un pierādīt, ka citu bez jūsu atrastajām nav.

<small>

* concepts:function,argument,value
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2004.12.4

Ar $n$ apzīmējam patvaļīgu nepāra naturālu skaitli, 
kas lielāks par $1$. Pierādīt: abi skaitļi $n$ un $n+2$
vienlaicīgi ir pirmskaitļi tad un tikai tad, ja 
$(n-1)!$ nedalās ne ar $n$, ne ar $n+2$.

<small>

* concepts:primes,divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2005.7.4

Triju veselu pozitīvu skaitļu summa ir $407$. 
Ar kādu lielāko daudzumu nuļļu var beigties šo
skaitļu reizinājums?

<small>

* topic:DivisibilityRulesLastDigits
* topic:ModularArithmetic
* genre:optimization
* concepts:decimal-notation
* questionType:FindOptimal
* seeAlso:LT.VILNIUS.2008.12.1

</small>



## Atrisinājums

Ievērojam, ka $407 = 250+125+32$, tad $p = 1000000$. 

Pamatosim, ka vēl vairāk nuļļu dabūt nevar dabūt.

* Divi saskaitāmie nevar beigties ar "5", jo atlikušajam tad jābeidzas ar "7". 
  Tātad vismaz viens saskaitāmais beigsies ar nulli. 
* Vairāk kā sešus $5$-pirmreizinātājus nevar iegūt 
  ($125=5^3$ un $250=5^3\cdot{}2$ ir optimāli).




# <lo-sample/> LV.AMO.2005.8.3

Kā var sadalīt naturālos skaitļus no 1 līdz 9 ieskaitot divās daļās tā, 
lai vienas daļas visu skaitļu summa būtu vienāda ar otras daļas 
visu skaitļu reizinājumu?

<small>

* topic:TreeTraversalBacktracking
* concepts:partition
* genre:construction
* questionType:FindExample
* strategy:CaseAnalysis

</small>


## Atrisinājums

Ja $a,b,c$ ir reizināti, tad var $abc=32$ un $a+b+c=45-32=13$. $(a,b,c)=(1,4,8)$.



# <lo-sample/> LV.AMO.2005.9.1

Atrast mazāko naturālo skaitli, kas dalās ar $225$
un kura decimālajā pierakstā neizmanto nevienu
no cipariem $3; 4; 5; 6; 7; 8; 9$.

<small>

* concepts:divisibility,decimal-notation
* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2005.10.3

Kādiem naturāliem skaitļiem $n$ abi skaitļi 
$2^n-1$ un $2^n+1$ ir pirmskaitļi?

<small>

* concepts:primes
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2005.10.4

Funkcijas $f(t)$ definīcijas apgabals un vērtību 
apgabals ir kopa $\{ 1; 2; \ldots; n\}$, pie tam visas vērtības
ir dažādas. Vai iespējams, ka visi skaitļi $f(x)-x$, 
$x=1; 2; \ldots; n$, ir dažādi, ja  
**(A)** $n=15$, **(B)** $n=16$?

<small>

* concepts:function
* questionType:ProveDisprove,ProveDisprove

</small>



# <lo-sample/> LV.AMO.2005.11.4

Dots, ka $a < b \leq c < d$ ir pozitīvi veseli skaitļi, 
$ad=bc$ un $d - a \leq 1$. Pierādīt, ka $a$ ir vesela skaitļa
kvadrāts.

<small>

* concepts:square-Alg
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2005.12.1

Vai eksistē tāds vesels pozitīvs skaitlis $n$, 
ka skaitlim $n^2$ ir tikpat daudz naturālu dalītāju, 
kas dod atlikumu $1$, dalot ar $3$, 
cik naturālu dalītāju, kas dod atlikumu $2$, dalot ar $3$?

<small>

* seeAlso:LV.AMO.2003.12.2
* concepts:divisibility,remainder
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2005.12.5

Divi spēlētāji spēlē sekojošu spēli, izdarot gājienus 
pēc kārtas. Sākumā doti divi stieņi: viens ar
garumu $n$, otrs ar garumu $n+1$ ($n$ – pozitīvs vesels skaitlis). 
Ar vienu gājienu var vai nu salauzt
vienu stieni divos īsākos, kuru garumi ir pozitīvi 
veseli skaitļi, vai arī izslēgt no turpmākās spēles
gaitas $k$ stieņus, katram no kuriem garums ir $k$ 
($k$ – jebkurš vesels pozitīvs skaitlis). Spēlētājs,
kurš izdara pēdējo gājienu, uzvar.
Kurš spēlētājs uzvar, pareizi spēlējot?

<small>

* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2006.7.1

Vilcienā Rīga-Mehiko vietas numurētas ar naturāliem skaitļiem, sākot ar $1$ 
(numerācija ir vienota visam vilcienam, t.i., ir tikai viena vieta ar numuru $1$, 
viena vieta ar numuru $2$ utt; numuri piešķirti virzienā no lokomotīves uz vilciena "asti"). 
Visos vagonos ir vienāds vietu skaits. Vietas ar numuriem $1996$ un $2015$ ir vienā vagonā,
bet vietas ar numuriem $630$ un $652$ – dažādos vagonos, 
kas pie tam nav blakus viens otram. Cik vietu ir katrā vagonā?

<small>

* topic:SeriesMembersSumsClosedFormulas
* topic:SequenceGaps
* topic:ExhaustionMethod
* concepts:sequence
* questionType:FindAll

</small>





## Atrisinājums

* Vietu skaits $k \leq 22$ (jo $1996$ un $2015$ ir vienā vagonā) 
* Vietu skaits $k \geq 21$ (jo $630$ un $652$ – dažādos vagonos, 
kas pie tam nav blakus viens otram). 
* $1995$ vai $1994$ jādalās ar $k$, jo ar šo vietu beidzas kārtējais vagons.





# <lo-sample/> LV.AMO.2006.8.3

Naturāla skaitļa $x$ ciparu summu apzīmēsim ar $S(x)$. 
Pieņemsim, ka $n$ – tāds naturāls skaitlis, kam vienlaicīgi 
izpildās īpašības $S(n)=10$ un $S(5n)=5$.  
**(A)** atrodiet kaut vienu tādu skaitli,  
**(B)** vai tādu skaitļu ir bezgalīgi daudz?  
**(C)** vai kāds no tādiem skaitļiem ir nepāra?


<small>

* topic:DivisibilityRulesFor2And4
* topic:NotationInsert
* genre:special-numbers,sum-of-digits
* questionType:FindExample,ProveDisprove,ProveDisprove
* strategy:TrialAndError

</small>


## Atrisinājums

Uzminēts piemērs (pāru cipari divreiz samazinās, ja reizina ar $5$).

**(A)** $22222$ der  
**(B)** Var $22222$ vidū iespraust $0$ (arī $64\cdot 10^k$ der).   
**(C)** Ja $n$ nepāra, $5n$ beigtos ar $5$, nav iespējams, jo $n \neq 1$. 



# <lo-sample/> LV.AMO.2006.9.1

Kāda ir lielākā iespējamā ciparu summa septiņciparu 
naturālam skaitlim, kas dalās ar $8$?

<small>

* concepts:sum,divisibility
* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2006.9.5

Apskatām naturālos skaitļus no $1$ līdz $100$ ieskaitot. 
Kādu lielāko daudzumu no tiem var izvēlēties tā, 
lai nekādi divi izvēlētie skaitļi nedalītos viens 
ar otru un katriem diviem izvēlētajiem skaitļiem 
lielākais kopīgais dalītājs būtu lielāks par $1$?

<small>

* concepts:divisibility,gcd
* questionType:FindOptimal

</small>



# <lo-sample/> LV.AMO.2006.10.3

Ir dots, ka, sareizinot visus naturālos skaitļus 
no $1$ līdz $33$ ieskaitot, iegūst

$$86833176188xy8864955181944012zt000000,$$

kur $x, y, z, t$ ir cipari. Noskaidrojiet $x$, 
$y$, $z$ un $t$ vērtības.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2006.11.2

Dots, ka $a<b \leq c < d$ ir pozitīvi veseli 
skaitļi, $ad = bc$ un $\sqrt{d}-\sqrt{a} \leq 1$. 
Pierādīt, ka $a$ ir vesela skaitļa kvadrāts.

<small>

* concepts:square-Alg
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2006.12.1

Vai eksistē tāds vesels pozitīvs skaitlis $n$, 
ka skaitlim $n^2$ ir tikpat daudz naturālu dalītāju, 
kas dod atlikumu $1$, dalot ar $3$, 
cik naturālu dalītāju, kas dod atlikumu $2$, dalot ar $3$?

<small>

* concepts:divisibility,divisors,remainder
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2007.7.1

Kādu lielāko daudzumu dažādu ciparu var izrakstīt pa apli tā, 
lai katri divi blakus uzrakstīti cipari, lasot tos vienalga 
kādā virzienā, veidotu pirmskaitļa pierakstu?


<small>

* topic:HamiltonCircuits
* topic:PrimesDistribution
* genre:optimization
* concepts:primes
* questionType:FindOptimal
* seeAlso:LV.AMO.2008.7.2

</small>



## Atrisinājums

Meklējam ciklu grafā. 
Iespējamie pāri $(1,3)$, $(1,7)$, $(3,7)$, 
$(7,9)$. $4$-cikla nav, jo $9$ tikai viens kaimiņš. $3$-cikls $1-3-7-1$.





# <lo-sample/> LV.AMO.2007.7.3

Uz tāfeles sākumā uzrakstīti $6$ divciparu naturāli skaitļi. 
Andris ar savu gājienu var pieskaitīt dažiem skaitļiem $1$, bet pārējiem skaitļiem $2$. 
(Var arī pieskaitīt visiem skaitļiem $1$ vai visiem skaitļiem $2$.) 
Pēc tam Maija ar savu gājienu var nodzēst jebkuru skaitli, kas dalās ar $7$ 
vai kam ciparu summa dalās ar $7$. Pēc tam gājienu izdara Andris, pēc tam – Maija, utt. 
Pierādīt, ka Maija var panākt, lai skaitļu uz tāfeles vairs nebūtu 
(pieņemsim, ka tiek spēlēts pietiekoši ilgi).


<small>

* topic:SequenceGaps
* topic:InfiniteDescent
* concepts:decimal-notation,divisibility,sum-of-digits
* genre:game
* questionType:Prove

</small>



## Atrisinājums

Ir bezgalīgi daudzi "dzēšami pāri". 
Pārīšiem $(105;106)$, 
$(160;161)$, $(167;168)$, $(175;176)$ utt. Andris nevar tikt pāri.




# <lo-sample/> LV.AMO.2007.8.3

Juliata iedomājās naturālu skaitli, sareizināja visus tā ciparus un iegūto 
rezultātu pareizināja ar iedomāto skaitli. Gala rezultātā Juliata ieguva $1716$. 
Kādu skaitli viņa iedomājās sākumā?

<small>

* topic:CanonicalFactorization
* topic:NumTheoryInequalityMethod
* concepts:decimal-notation
* genre:digit-manipulation
* questionType:FindAll

</small>





## Atrisinājums

Dalījums pirmreizinātājos: $1716=2^2 \cdot 3 \cdot 11 \cdot 13$. 

* Bet skaitļi $11$ un $13$ nav cipari. 
* Visas atbildes ir formā $11 \cdot 13 \cdot k$.




# <lo-sample/> LV.AMO.2007.9.1

Kvadrātveida tabula sastāv no $10 \times 10$ rūtiņām. 
Katrā rūtiņā ierakstīts nenulles cipars. 
No katras rindiņas un katras kolonnas cipariem, 
ņemot tos patvaļīgā secībā, izveidots viens desmitciparu 
naturāls skaitlis. Vai var gadīties, ka tieši $19$ no 
šiem skaitļiem (ne vairāk un ne mazāk) dalās ar $3$?

<small>

* concepts:divisibility
* questionType:ProveDisprove

</small>



# <lo-sample/> LV.AMO.2007.9.3

**(A)** katrs no naturāliem skaitļiem $a$ un $b$ ir izsakāms 
kā divu veselu skaitļu kvadrātu summa. 
Pierādiet, ka arī reizinājums  ir izsakāms šādā veidā.  
**(B)** atrodiet divus tādus polinomus ar veseliem koeficientiem 
$f(x)$ un $g(x)$, ka visiem $x$ pastāv vienādība

$$\left( f(x) \right)^2 + \left( g(x) \right)^2 =$$

$$= \left( x^2+1 \right)\left( x^2 + 4 \right)
\left(x^2 + 2x + 2 \right)\left( x^2 - 2x + 2 \right).$$

<small>

* concepts:sum,square-Alg,equation
* questionType:Prove,FindExample

</small>


# <lo-sample/> LV.AMO.2007.10.1

Desmitciparu naturāls skaitlis dalās ar 
$999\,999$. Vai tas var dalīties arī ar $1\,000\,001$?

<small>

* seeAlso:LV.AMO.2008.10.1
* concepts:divisibility
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2008.8.1

Kādu lielāko daudzumu dažādu ciparu var izrakstīt pa apli tā, 
lai katri divi blakus uzrakstīti cipari, lasot tos vienalga 
kādā virzienā, veidotu pirmskaitļa pierakstu?


<small>

* seeAlso:LV.AMO.2007.7.1
* concepts:primes
* questionType:FindOptimal

</small>





# <lo-sample/> LV.AMO.2008.7.2

Dots, ka $x$ un $y$ – tādi naturāli skaitļi, ka  $x \cdot y = 10^{12}$. 
Vai var būt, ka ne $x$, ne $y$ nesatur savā pierakstā nevienu ciparu $0$?

<small>

* topic:DivisibilityRulesLastDigits
* topic:StandardIdentities
* concepts:decimal-notation
* questionType:ProveDisprove

</small>


## Atrisinājums

Nē. Izmantojam 10^12 dalījumu pirmreizinātājos
$x$ vai $y = 2^{12} = 4096$. (Vai arī sareizināsies $2$ un $5$.)





# <lo-sample/> LV.AMO.2008.8.3

Dots, ka $n>1$ – naturāls skaitlis, kas nav pirmskaitlis. 
Pierādīt, ka var atrast vismaz trīs dažādus naturālus skaitļus $a_1,a_2,\ldots,a_k$, 
kas apmierina sakarību

$$a_1 + a_2 + \ldots + a_k = n \cdot \left( \frac{1}{a_1} + 
\frac{1}{a_2} + \ldots + \frac{1}{a_k} \right).$$

<small>

* topic:DivisorNumberAndSum
* topic:IntegerFactorization
* topic:TelescopicSums
* concepts:primes,series
* questionType:Prove

</small>




## Atrisinājums

* Sadala pa pāriem $a_1a_k = a_2a_{k-1} = \ldots = n$ (un $k \geq 3$).
* Tad $a_1 + \ldots + a_k = a_k + \ldots + a_1$.

$$1+3+9 = 9 \cdot \left( \frac{1}{1} + \frac{1}{3} + \frac{1}{9} \right). $$



# <lo-sample/> LV.AMO.2008.9.1

Kvadrātveida tabula sastāv no $12 \times 12$ rūtiņām. 
Katrā rūtiņā ierakstīts nenulles cipars. No katras 
rindiņas un katras kolonnas cipariem, ņemot tos patvaļīgā secībā, 
izveidots viens divpadsmitciparu naturāls skaitlis. 
Vai var gadīties, ka tieši $23$ no šiem skaitļiem 
(ne vairāk un ne mazāk) dalās ar $3$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2008.9.4

Naturālie skaitļi no $1$ līdz $2008$ ieskaitot 
jāsadala grupās tā, lai izpildītos sakarība: 
ja $a$ dalās ar $b$ un $b$ dalās ar $c$ 
($a$, $b$, $c$ – dažādi naturāli skaitļi), 
tad $a$, $b$ un $c$ visi nepieder vienai un tai pašai grupai. 
Kāds ir mazākais iespējamais grupu skaits?

<small>

* concepts:groups
* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2008.10.1

Desmitciparu naturāls skaitlis dalās ar 9 999 999. 
Vai tas var dalīties arī ar 10 000 001 ?

<small>

* seeAlso:LV.AMO.2007.10.1
* concepts:divisibility
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2008.10.4

Uz $50$ kartiņām uzrakstīti naturāli skaitļi no 
$1$ līdz $50$ ieskaitot (katrs skaitlis uz citas kartiņas). 
Rindā viena aiz otras atrodas $2008$ rūtiņas. 
Kartiņas kaut kā uzliktas uz $50$ rūtiņām (uz katras rūtiņas – 
ne vairāk kā viena kartiņa). Ja kādam $n$, $1 \leq n < 50$, 
kartiņai $n$ tieši pa labi esošā rūtiņa ir brīva, 
tad kartiņu $n+1$ atļauts pārcelt uz šo brīvo rūtiņu; 
to sauc par vienu gājienu. Pierādīt, ka nevar izdarīt 
vairāk par $1250$ gājieniem.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2008.11.2

Funkcija $f(n)$ definēta visiem veseliem $n$ un pieņem 
veselas vērtības. Visiem veseliem $x$ un $y$ pastāv vienādība

$$f(f(x) + y) = x + f(y+2008).$$

Atrast visas tādas funkcijas $f$ un pierādīt, ka citu bez Jūsu atrastajām nav.

<small>

* concepts:function,equation
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2008.11.3

Dots, ka $n$ – naturāls skaitlis. Noskaidrojiet:  
**(A)** vai var gadīties, ka skaitlim $n^2 - 1$ 
ir tieši $10$ dažādi naturāli dalītāji?  
**(B)** vai var gadīties, ka skaitlim $n^2 - 4$ ir tieši 
$10$ dažādi naturāli dalītāji, ja $n$ – pāra skaitlis?

<small>

* concepts:divisors
* questionType:ProveDisprove,ProveDisprove

</small>



# <lo-sample/> LV.AMO.2008.12.2

Kādiem naturāliem $n$ skaitļu kopu  var sadalīt 
divās daļās tā, lai vienlaicīgi izpildītos šādi nosacījumi:  

a. katrs skaitlis nonāktu tieši vienā daļā,  
b. abās daļās būtu vienāds daudzums skaitļu,   
c. katras daļas visu skaitļu vidējais aritmētiskais arī piederētu šai daļai?

<small>

* concepts:arithmetic-mean
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2008.12.4

Vai eksistē tādi trīs naturāli skaitļi, kas visi 
lielāki par $1$ un kam piemīt īpašība:
katra skaitļa kvadrāts, pamazināts par $1$, 
dalās ar katru no abiem pārējiem skaitļiem?

<small>

* concepts:divisibility,square-Alg
* questionType:ProveDisprove

</small>


# LV.AMO.2009.7.2

Trijstūrim $T$ visas malas ir dažāda garuma. Par punktiem $M$ un $N$
zināms tikai tas, ka tie atrodas trijstūra $T$ iekšpusē.  
**(A)** vai var gadīties, ka nogrieznis $MN$ garāks par divām $T$ malām?  
**(B)** vai var gadīties, ka nogrieznis $MN$ garāks par visām $T$ malām? 

<small>

* concepts:triangle
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2009.7.3

Tabula sastāv no $3 \times 3$ rūtiņām. Rūtiņās ierakstīti naturāli skaitļi no $1$
līdz $9$ (katrā rūtiņā cits skaitlis). Skaitļu summas rindās un kolonnās
visas ir dažādas. Kāds lielākais daudzums šo summu var būt pirmskaitļi?

<small>

* topic:ModularParity
* topic:PrimesDistribution
* topic:SeriesMembersSumsClosedFormulas
* topic:ExhaustionMethod
* concepts:primes,sum,table,row,column,natural-numbers
* genre:fill-in-table
* questionType:FindOptimal
* isHard:true

</small>


## Atrisinājums

Nepāri kā pentomino "V". $(5,6,4)$,$(9,8,2)$,$(7,3,1)$. Nevar būt $p_1+p_2+p_3=45$.



# <lo-sample/> LV.AMO.2009.7.4

Trijstūris $ABC$ ir šaurleņķu. Trijstūri $AMB$ un $BNC$ abi ir
vienādmalu un atrodas ārpus $\bigtriangleup ABC$. Pierādīt, ka $AN=CM$.  
![LV.AMO.2016.7.3](geometry-grade07/LV.AMO.2009.7.4.png)

<small>

* concepts:triangle
* questionType:Prove

</small>




# <lo-sample/> LV.AMO.2009.7.5

Vairākiem rūķīšiem ir vienādi naudas daudzumi. Brīdi pa brīdim
kāds no rūķīšiem paņem daļu savas naudas un sadala to pārējiem
vienādās daļās. Pēc kāda laika izrādījās, ka vienam no rūķīšiem ir $8$
dālderi, bet citam – $25$ dālderi. Cik pavisam ir rūķīšu? (Dālderis ir
vienīgā rūķīšiem pieejamā naudas vienība.)

<small>

* topic:InvariantRemainder
* concepts:divisibility
* genre:making-moves
* questionType:FindAll

</small>





## Atrisinājums

Ja rūķu ir $a$, pārdalot $k$ dālderus, 
starpība starp devēja un saņēmēja naudas daudzumiem 
mainās par $(a-1)k+k = ak$. Ja sākumā starpība bija $0$, bet 
beigu starpība ir $17$, tad $a=17$.





# <lo-sample/> LV.AMO.2009.8.4

Profesors Cipariņš ar savu ārzemju kolēģi ieradās Ziemassvētku
eglītes pasākumā, kurā piedalījās universitātes darbinieki, viņu
draugi, ģimenes locekļi, paziņas utt. Norādot uz trim viesiem,
Cipariņš piezīmēja: "Šo cilvēku vecumu reizinājums ir $2450$, bet
summa – divas reizes lielāka nekā Jūsu vecums." Kolēģis atteica:
"Es nezinu un nevaru noskaidrot, cik veci ir šie ļaudis." Tad Cipariņš
piebilda: "Es esmu vecāks par jebkuru citu šai eglītē." Tagad kolēģis
uzreiz pateica minēto $3$ viesu vecumus. Cik gadu tai laikā bija
Cipariņam un cik – viņa kolēģim? (Visus vecumus izsaka veselos
gados.)

<small>

* topic:CanonicalFactorization
* topic:ExhaustionMethod
* genre:word-problem
* isHard:true
* questionType:FindAll

</small>





## Atrisinājums

Kolēģa 1.atbildei atbilst 
$(5,10,49)$ vai $(7,7,50)$. Otrā Profesora Cipariņa piebilde neļauj tos atšķirt.



# <lo-sample/> LV.AMO.2009.9.4

Naturāla skaitļa $n$ pozitīvo dalītāju skaitu apzīmējam ar $d(n)$.
Piemēram, $d(1)=1$; $d(6)=4$ utt. Sauksim skaitli $n$ par 
apaļīgu, ja tas dalās ar $d(n)$.  
**(A)** atrodiet piecus apaļīgus skaitļus,  
**(B)** pierādiet, ka apaļīgu skaitļu ir bezgalīgi daudz.

<small>

* concepts:divisors
* questionType:FindExample,Prove

</small>


# <lo-sample/> LV.AMO.2009.10.2

Dots, ka $p$ un $q$ ir divi viens otram sekojoši nepāra pirmskaitļi
(piemēram, $13$ un $17$). Pierādīt: skaitli $p+q$ var sadalīt triju tādu
naturālu skaitļu reizinājumā, kas visi lielāki par $1$ (starp šiem trim
skaitļiem var būt arī vienādi).

<small>

* concepts:primes
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2009.11.2

Spēlē OP! piedalās $n$ spēlētāji ($n \geq 2$). Spēle notiek vairākas dienas.
Katru dienu viens spēlētājs uzvar, bet pārējie zaudē. Sakaņā ar
noteikumiem $i$-tajā dienā ($i = 1, 2, \ldots$) uzvarētājs saņem
$i(n-1)$ punktus, bet katrs zaudētājs zaudē pa $i$ punktiem. Spēles
sākumā visiem ir pa $0$ punktiem. Pēc kāda mazākā dienu skaita var
gadīties, ka visiem atkal ir pa $0$ punktiem?

<small>

* questionType:FindOptimal

</small>


# <lo-sample/> LV.AMO.2009.11.3

Dots, ka $a$ un $b$ – naturāli skaitļi un skaitļa 
$S = a^2 + ab + b^2$ pēdējais
cipars ir $0$. Kāds ir skaitļa $S$ priekšpēdējais cipars?

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2009.12.3

Dots, ka $n$ - naturāls pāra skaitlis. Apskatām reizinājumu

$$R = n(n + 1)(n + 2)(n + 3).$$

**(A)** vai var būt, ka $R$ ir kāda naturāla skaitļa kvadrāts?  
**(B)** vai var būt, ka $R$ ir kāda naturāla skaitļa kubs?

<small>

* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2009.12.5

Uz galda atrodas $n$ konfektes, $n$ – naturāls skaitlis. Divi spēlētāji
pamīšus ēd pa $x^2$ konfektēm, kur $x$ – naturāls skaitlis ($x$ var mainīties
no gājiena uz gājienu). Tas, kam nav ko ēst, zaudē. Pierādīt: ir
bezgalīgi daudz tādu $n$, ka, pareizi spēlējot, otrais spēlētājs var
uzvarēt.

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2010.7.1

Uz tāfeles uzrakstīti pieci dažādi pirmskaitļi, kas nepārsniedz $100$. Par tiem
zināms, ka

1. pirmais ir $7$;
2. trešais ir par $4$ lielāks nekā piektais;
3. skaitlim, kuru iegūst, ceturto sareizinot ar piekto, visi cipari ir vienādi;
4. pirmais un ceturtais summā dod pieckāršotu otro.

Atrodi visus šos skaitļus!

<small>

* topic:PrimesDistribution
* topic:PrimesDistribution
* topic:CanonicalFactorization
* concepts:primes
* genre:construction
* questionType:FindAll
* strategy:CaseAnalysis

</small>



## Atrisinājums

(a) $p_1=7$, (b) $p_5 \neq 11$, (d) $p_4 \neq 11$, (c) $p_4 p_5 = 3 \cdot 37$, (d) $p_4 \neq 37$. Tātad $(7,2,41,3,37)$.



# <lo-sample/> LV.AMO.2010.7.2

Caur trijstūra $ABC$ virsotni $A$ novilktā taisne $t$ sadala trijstūri divos
vienādos trijstūros.
Vai var gadīties, ka $AB>AC$? 

<small>

* concepts:equal-triangles
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2010.7.3

Ieraksti tabulas ar izmēriem $4 \times 4$ rūtiņas katrā rūtiņā vienu naturālu skaitli
tā, lai vienlaicīgi izpildītos šādas divas īpašības:

1. visi ierakstītie skaitļi ir dažādi;
2. jebkuru četru skaitļu, nekādi divi no kuriem neatrodas ne vienā rindā, 
nedz vienā kolonnā, summa ir $2010$.

Pietiek parādīt vienu veidu, kā to var izdarīt.

<small>

* topic:LinearSystemsApplications
* topic:TreeTraversalBacktracking
* genre:construction
* questionType:FindExample
* genre:magic-construction

</small>





## Atrisinājums

Saskaita 2 tabulas: $((1,2,3,4),\ldots,(1,2,3,4))$ un
$(0,\ldots,0),(4,\ldots,4),(996,\ldots,996),(1000,\ldots,1000)$.





# <lo-sample/> LV.AMO.2010.7.4

Vairākiem bērniem visiem ir vienāds skaits konfekšu. Brīdi pa brīdim kāds
no bērniem paņem daļu savu konfekšu un sadala to pārējiem vienādās
daļās. Pēc kāda laika izrādījās, ka vienam no bērniem ir $4$ konfektes, bet
citam – $23$ konfektes. Cik pavisam ir bērnu? (Konfektes netiek dalītas
daļās, apēstas vai izmestas.)


<small>

* topic:InvariantRemainder
* questionType:FindAll

</small>



## Atrisinājums

Ja bērnu ir $a$, pārdalot $k$ konfektes, starpība mainās par $(a-1)k+k = ak$. 
Ja starpība divu bērnu konfekšu skaitam pēc kāda laika ir $19$, tad $a=19$.



# <lo-sample/> LV.AMO.2010.8.1

Starp skaitļiem

$$6\;\;1\;\;3\;\;4,$$

nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\cdot$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(A)** $25$,
**(B)** $24$.  
Vai to var izdarīt?

<small>

* topic:AlgorithmsOnSyntaxTrees
* questionType:ProveDisprove,ProveDisprove

</small>



## Atrisinājums

**(A)** $(6 + 1) \cdot 3 + 4 = 25$;  
**(B)** $6 : (1 - 3:4)=24$.




# <lo-sample/> LV.AMO.2010.8.2

Andris un Juris katrs izvēlas trīs secīgus naturālus skaitļus tā, ka visi
seši skaitļi ir atšķirīgi. Katru Andra skaitli sareizināja ar katru Jura
skaitli, ieguva deviņus reizinājumus. Pierādi, ka starp iegūtajiem
deviņiem skaitļiem vismaz astoņi būs savā starpā atšķirīgi!

<small>

* topic:NumTheoryExprForConcepts
* topic:ExhaustionMethod
* questionType:Prove

</small>





## Atrisinājums

Ja iedomāti $(a-1,a,a+1)$ un $(b-1,b,b+1)$ tad 2 vienādi reizinājumi var rasties vien tad,  
ja $b \pm 1 = 2a$ vai $a \pm 1 = 2b$.







# <lo-sample/> LV.AMO.2010.9.1

Naturālus skaitļus no $1$ līdz $2N$ jāsadala $N$ pāros tā, 
lai katra pāra skaitļu summa būtu pirmskaitlis, 
pie tam šīm $N$ summām jābūt dažādām. Vai to
iespējams izdarīt, ja  
**(A)** $N = 5$; **(B)** $N = 10$?

<small>

* concepts:primes,sum
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2010.9.3

Naturāla skaitļa $n$ pozitīvo dalītāju skaitu apzīmējam ar $d(n)$. 
Piemēram, $d(1)=1$; $d(6)=4$ utt. 
Sauksim skaitli $n$ par apaļīgu, ja tas dalās ar $d(n)$.  
**(A)** atrodi piecus apaļīgus pāra skaitļus,  
**(B)** pierādi, ka apaļīgu pāra skaitļu ir bezgalīgi daudz.

<small>

* concepts:divisors
* questionType:FindExample,Prove

</small>



# <lo-sample/> LV.AMO.2010.9.4

$2010 \times 2010$ rūtiņas lielā kvadrātā,
sākot ar apakšējo kreiso rūtiņu,
pēc kārtas tiek ierakstīti naturālie
skaitļi kā parādīts zīmējumā
(katrā rūtiņā ierakstīts viens
skaitlis).
Piemēram, skaitlis $19$ ierakstīts
ceturtajā rindā, trešajā kolonnā.  
**(A)** Kurš skaitlis ierakstīts 20. rindā, 10. kolonnā?  
**(B)** Kurā rindā un kurā kolonnā atrodas rūtiņa, 
kurā ierakstīts skaitlis $2010$?

![quadrant](LV.AMO.2010.9.4.png)

<small>

* questionType:FindAll,FindAll

</small>


# <lo-sample/> LV.AMO.2010.10.4

Cik dažādos veidos skaitli $2010$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 


<small>

* topic:SeriesMembersSumsClosedFormulas
* topic:CanonicalFactorization
* topic:ExhaustionMethod
* questionType:FindCount
* concepts:sum,consecutive-numbers

</small>






# <lo-sample/> LV.AMO.2010.11.1

Dotas trīs aritmētiskas progresijas:  
(1) $8, 19, 30, 41, 52, \ldots$  
(2) $8, 21, 34, 47, 60, \ldots$  
(3) $4, 21, 38, 55, 72, \ldots$  
(a) Atrodi mazāko skaitli, kas pieder visām trim 
dotajām virknēm!
(b) Pierādi, ka ir bezgalīgi daudz tādu skaitļu, 
kas pieder visām trim dotajām virknēm!

<small>

* concepts:arithmetic-progression,sequence

</small>



# <lo-sample/> LV.AMO.2010.11.4

Uz tāfeles uzrakstīts skaitlis $2010$. 
Divi spēlētāji spēlē sekojošu spēli. Vienā
gājienā jāizvēlas vienu no pašlaik uz tāfeles 
uzrakstītā skaitļa $N$ dalītājiem
$d > 1$, jāatņem to no $N$, jānodzēš no tāfeles 
$N$ un tā vietā jāraksta iegūtā
starpība $N-d$. Gājienus izdara pēc kārtas. 
Zaudē tas, kurš iegūst $0$. Kurš no
spēlētājiem, pareizi spēlējot, uzvarēs – 
tas, kurš sāk, vai tas, kurš izdara otro gājienu?

<small>

* concepts:divisors
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2010.12.3

Atrodi visus tādus naturālus skaitļus $n$, 
ka skaitļi $n$, $d(n)$ un $d(d(n))$
veido dilstošu aritmētisku progresiju. ($d(x)$ ir 
skaitļa $x$ naturālo dalītāju skaits.)

<small>

* concepts:arithmetic-progression,divisors
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2010.12.5

Uz galda atrodas $n$ cepumi, kur $n$ – naturāls skaitlis. 
Divi spēlētāji pamīšus ēd pa $x^3$ cepumiem, 
kur $x$ – naturāls skaitlis (dažādiem
gājieniem $x$ var būt atšķirīgs). 
Tas, kam nav ko ēst, zaudē. Pierādi: ir bezgalīgi daudz 
tādu $n$, ka, pareizi spēlējot, otrais spēlētājs uzvar!

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.AMO.2011.5.1

Reizināšanas piemērā ciparus aizstāja ar burtiem un ieguva izteiksmi

$$AB \cdot CD = EEE.$$

Atjauno sākotnējo reizināšanas piemēru, ja zināms, ka vienādi burti
apzīmē vienādus ciparus, bet dažādi burti – dažādus ciparus, pie tam
ne $A$, ne $C$ nav $0$. Atrodi visus iespējamos atrisinājumus!

<small>

* topic:IntegerFactorization
* topic:ExhaustionMethod
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2011.5.2

Dotās $3 \times 3$ rūtiņu tabulas katrā rūtiņā
jāieraksta pa vienam naturālam skaitlim tā,
lai katrā rindā, katrā kolonnā un katrā
diagonālē ierakstīto trīs skaitļu summas būtu
vienādas. Ir zināmi trīs rūtiņās ierakstītie
skaitļi (skat. 1. zīm.). Aizpildi pārējās tabulas
rūtiņas!  
![1.zīm](LV.AMO.2011.5.2.png)

<small>

* topic:NumTheoryExprVariables
* topic:AlgebraicTransformations
* questionType:FindAll
* concepts:sum

</small>




# <lo-sample/> LV.AMO.2011.5.3

Parādi, kā kvadrātu var sadalīt vairākos platleņķa trijstūros!

<small>

* topic:ConstructionsTriangulate
* topic:ConstructionsSmallMovements
* topic:CircleInscribedAngles
* questionType:Prove
* concepts:square-Geo,triangle

</small>




# <lo-sample/> LV.AMO.2011.5.4

Vai naturālos skaitļus no $1$ līdz $12$, katru izmantojot tieši vienu reizi,
var uzrakstīt pa apli tādā secībā, ka jebkuru divu blakus esošu skaitļu
starpība ir  
**(a)** $2$ vai $3$;  
**(b)** $3$ vai $4$?

<small>

* topic:TreeTraversalBacktracking
* topic:GraphProblems
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2011.5.5

Kvadrātā ar izmēriem $7 \times 7$ rūtiņas jāizvieto $n$ "stūrīšus"
(2. zīm. attēlotās figūras) tā, lai tajā vairāk nevarētu
ievietot nevienu citu šādu "stūrīti". (Stūrīšu malām jāiet
pa rūtiņu malām. Stūrīši var arī būt pagriezti citādāk.)
Parādi, kā to var izdarīt, ja  
**(A)** $n=9$;  
**(B)** $n=8$.   
![2.zīm.](LV.AMO.2011.5.5.png)

<small>

* topic:CountingUsingSymmetry
* topic:TreeTraversalBacktracking
* questionType:Prove

</small>






# <lo-sample/> LV.AMO.2011.6.1


Vai eksistē tādi naturāli skaitļi $a$ un $b$, kuriem izpildās vienādība

$$a \cdot b \cdot (a+b) = 20102011 ?$$

<small>

* topic:IntegerFactorization
* questionType:ProveDisprove
* concepts:equation

</small>





# <lo-sample/> LV.AMO.2011.6.2


Sešdesmit pensionāri katru dienu *sociālajā tīklā*
sarakstās savā starpā. Katrs kungs sarakstās ar tieši $17$ dāmām, 
bet katra kundze sarakstās ar tieši $13$ kungiem. 
Cik starp šiem pensionāriem ir kungu un cik – kundžu?

<small>

* topic:BipartiteGraphs
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2011.6.3

Kvadrātā ar izmēriem $8 \times 8$ rūtiņas sākotnēji 
visas rūtiņas ir baltas. Kāds mazākais skaits rūtiņu 
šajā kvadrātā jānokrāso zaļas, lai tajā nevarētu atrast 
nevienu pilnībā baltu taisnstūri ar izmēriem $1 \times 3$ 
rūtiņas (novietotu horizontāli vai vertikāli)?

<small>

* topic:ExhaustionMethod
* questionType:FindOptimal

</small>





# <lo-sample/> LV.AMO.2011.6.4


3. zīmējumā dota $3 \times 3$ rūtiņu tabula, 
kurā ierakstīti veseli skaitļi. Vienā gājienā atļauts izvēlēties 
divas dažādas tabulas rūtiņas -- apzīmēsim tajās ierakstītos 
skaitļus attiecīgi ar $a$ un $b$, nodzēst šos divus skaitļus 
un to vietā ierakstīt: a vietā -- skaitli $5a-2b$, bet b  vietā -- skaitli $5b-2a$.
Vai, vairākkārt veicot šādus gājienus, var iegūt tabulu, kāda attēlota 4. zīm.?

![3.zīm.](LV.AMO.2011.6.4A.png)

![4.zīm.](LV.AMO.2011.6.4B.png)


<small>

* topic:InvariantRemainder
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2011.6.5


Betai bija $50$ konfektes, bet Almai un Danai bija vienāds konfekšu skaits. 
Beta pazaudēja vienu konfekti un noskuma. Almai kļuva Betas žēl, un viņa atdeva māsai pusi 
no savām konfektēm. Beta nomierinājās un nolēma, ka viņai tagad konfekšu ir par daudz un atdeva 
pusi no savām Danai. Arī Dana izlēma padalīties ar Almu un atdeva pusi no savām konfektēm Almai. 
Tagad Almai un Betai ir vienāds konfekšu skaits. Cik konfekšu sākumā bija katrai no māsām?

<small>

* topic:AlgebraicTransformations
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2011.7.1

Uz tāfeles augošā secībā uzrakstīti seši dažādi pirmskaitļi, kas
nepārsniedz $100$. Par tiem zināms, ka

1. visu skaitļu pēdējie cipari ir atšķirīgi;
2. sestais skaitlis ir par $14$ lielāks nekā trešais;
3. ceturtā skaitļa pirmais cipars ir vienāds ar otrā skaitļa pēdējo ciparu;
4. piektā un sestā skaitļa pirmie cipari ir vienādi.

Atrodi visus šos skaitļus!

<small>

* topic:PrimesDistribution
* questionType:FindAll
* concepts:primes

</small>





## Atrisinājums

**(a)** $p_1=2$,$p_2=5$.  
**(b)**, **(d)** $(p_3;p_6)=(53,67)$.  
**(c)** $p_4=59$.






# <lo-sample/> LV.AMO.2011.7.3

Atrodi naturālu skaitli, kuru, dalot ar $2010$, atlikumā iegūst $13$, bet,
dalot ar $2011$, atlikumā iegūst $3$.

<small>

* topic:ArithmeticSeriesDivisibility
* topic:ChineseRemainderTheorem
* questionType:FindExample
* concepts:remainder

</small>





# <lo-sample/> LV.AMO.2011.7.4

Kvadrāts sadalīts piecos taisnstūros tā, ka šo taisnstūru malu garumi
centimetros ir visi naturālie skaitļi no $1$ līdz $10$. Parādi vienu
piemēru, kā to var izdarīt! 

<small>

* concepts:square-Geo,rectangle
* questionType:FindExample

</small>




# <lo-sample/> LV.AMO.2011.7.5

Taisne nokrāsota $10$ dažādās krāsās. Pierādi, ka uz tās var atrast
divus vienas krāsas punktus, starp kuriem attālums centimetros ir
vesels skaitlis.


<small>

* concepts:line,point,distance,integer-numbers
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2011.8.1

Starp skaitļiem

$$8\;\;3\;\;5\;\;2,$$

nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\cdot$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(A)** $15$, **(B)** $16$.

<small>

* topic:AlgorithmsOnSyntaxTrees
* questionType:FindExample
* seeAlso:LV.AMO.2010.8.1

</small>


## Atrisinājums

**(A)** $8 - 3 + 5 \ast 2 = 8 - (3 - 5 \ast 2) = 15$;  
**(B)** $8 : (3 - 5:2) = 16$.





# <lo-sample/> LV.AMO.2011.8.4

Leonards izvēlējās patvaļīgu trīsciparu skaitli, pareizināja to ar $2$ un
tam galā pierakstīja sākotnējo skaitli. Vai viņa jauniegūtais skaitlis
noteikti dalās ar **(A)** $17$; **(B)** $23$?

<small>

* topic:NotationShift
* topic:CanonicalFactorization
* questionType:ProveDisprove
* concepts:divisibility

</small>


## Atrisinājums

Ja 3-ciparu skaitlis ir $\overline{abc}$, 
tad jaunais ir $2001\overline{abc}$ dalās ar $23$. Bet $17 \nmid 2001$. 





# <lo-sample/> LV.AMO.2011.8.5

Jānis un Anna spēlē šādu spēli. Uz tāfeles ir uzrakstīts naturāls
skaitlis. Spēlētāji pēc kārtas veic gājienu: no uzrakstītā skaitļa atņem
kādu šī skaitļa ciparu (izņemot $0$), nodzēš uz tāfeles esošo skaitli un
tā vietā uzraksta iegūto starpību. Uzvar tas, kurš pēc sava gājiena
iegūst nulli.  
Sākumā ir uzrakstīts skaitlis $2011$, pirmo gājienu izdara Anna. Kurš
no spēlētājiem, pareizi spēlējot, uzvarēs? Apraksti, kā uzvarētājam
jārīkojas!

<small>

* topic:GameInvariant
* questionType:Algorithm,Prove

</small>



## Ieteikums
 
Pēc katra Annas gājiena skaitlim jādalās ar $10$. 


# <lo-sample/> LV.AMO.2011.9.1

Atrodi visus naturālu skaitļu pārus $(x, y)$ tādus, ka $x\neq y$ un

$$\frac{1}{x^2 + 24} + \frac{1}{y^2 + 24} = \frac{2}{xy + 24}.$$

<small>

* concepts:natural-numbers,pair
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2011.9.3

Dots vienādojums $\# x^2 − \# x + \# = 0$. Divi rūķīši spēlē spēli – pirmais
nosauc trīs dažādus skaitļus, bet otrais tos kaut kādā secībā saliek
„$\#$” vietās. Vai pirmais rūķītis vienmēr var panākt, lai vienādojumam
būtu vismaz viena racionāla sakne?

<small>

* concepts:equation
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2011.9.4

Kāds lielākais skaits pēc kārtas sekojošu naturālu skaitļu var būt ar
īpašību, ka katrs no tiem ir izsakāms kā divu naturālu skaitļu
kvadrātu starpība?

<small>

* concepts:square-Geo,rectangle
* questionType:FindOptimal

</small>




# <lo-sample/> LV.AMO.2011.10.1

Cik dažādos veidos skaitli $2011$ var izteikt kā vismaz divu pēc kārtas
sekojošu naturālu skaitļu summu? Saskaitāmo secība nav svarīga. 

<small>

* seeAlso:LV.AMO.2010.10.4
* concepts:sum,consecutive-numbers
* questionType:FindCount

</small>





# <lo-sample/> LV.AMO.2011.11.1

Dotas trīs aritmētiskas progresijas:  
(1) $1, 15, 29, 43, 57, 71, \ldots$  
(2) $2, 17, 32, 47, 62, 77, \ldots$  
(3) 3, 19, 35, 51, 67, 83, \ldots$  
**(A)** Atrodi mazāko skaitli, kas pieder visām trim dotajām virknēm!  
**(B)** Pierādi, ka ir bezgalīgi daudz tādu skaitļu, kas pieder visām trim
dotajām virknēm!

<small>

* seeAlso:LV.AMO.2010.11.1
* concepts:arithmetic-progression,sequence
* questionType:FindOptimal,Prove

</small>





# <lo-sample/> LV.AMO.2011.11.5

Vai pa riņķa līniju var izvietot $2011$ dažādus naturālus skaitļus tā, ka
jebkuriem diviem blakus esošiem skaitļiem lielākā skaitļa attiecība
pret mazāko ir pirmskaitlis?

<small>

* concepts:circumference,primes
* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2011.12.1

Naturālie skaitļi no $1$ līdz $9$ sadalīti trīs grupās pa trim skaitļiem un
katrā grupā aprēķināta tajā ietilpstošo skaitļu summa. Vai var būt, ka  
**(A)** visas summas ir pirmskaitļi?  
**(B)** visas summas ir atšķirīgi pirmskaitļi?

<small>

* concepts:sum,primes
* questionType:ProveDisprove,ProveDisprove

</small>




# <lo-sample/> LV.AMO.2012.5.1

Divu naturālu skaitļu pierakstā izmantoti tikai cipari $1$, $4$, $6$ un $9$. Vai
var gadīties, ka viens skaitlis ir tieši septiņas reizes lielāks nekā otrs
skaitlis? 

<small>

* topic:ExhaustionMethod
* questionType:ProveDisprove

</small>






# <lo-sample/> LV.AMO.2012.5.2

Parādi, kā kvadrātu var sadalīt vairākos platleņķa trijstūros.
(Trijstūri sauc par platleņķa trijstūri, ja tam ir viens plats leņķis un
divi šauri leņķi.) 

<small>

* topic:ConstructionsTriangulate
* topic:CircleInscribedAngles
* sameAs:LV.AMO.2011.5.3
* questionType:ProveDisprove
* concepts:square-Geo,triangle

</small>





# <lo-sample/> LV.AMO.2012.5.3


Maisā ir baltas, zaļas un sarkanas pogas (citu krāsu pogu maisā nav).
Kādu mazāko skaitu pogu uz labu laimi (tās neredzot) ir jāizņem, lai
noteikti būtu paņemtas vai nu $2$ baltas, vai $3$ zaļas, vai $4$ sarkanas
pogas


<small>

* topic:NumTheoryPigeonholeNewSets
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2012.5.4


$24$-stāvu mājā ir lifts, kuram ir divas pogas. Nospiežot vienu pogu,
tas paceļas (ja iespējams) $17$ stāvus uz augšu, nospiežot otru --
nolaižas $8$ stāvus uz leju (ja iespējams). Noskaidro, no kura stāva ar
šo liftu var nokļūt uz jebkuru citu stāvu šajā mājā.
(Lifts nevar uzbraukt augstāk par 24. stāvu un zemāk par 1. stāvu.) 

<small>

* topic:NumTheoryMathInduction
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2012.5.5

Sadali 1. zīmējumā attēloto figūru trīs vienādās figūrās.
(Figūru un tās spoguļattēlu saucam par vienādām figūrām.) . 
![1.zīm](LV.AMO.2012.5.5.png)

<small>

* topic:SquareGridCutting
* questionType:ProveDisprove

</small>





# <lo-sample/> LV.AMO.2012.7.1

Vai var atrast tādus veselus skaitļus $a$ un $b$, kuriem izpildās vienādība

$$ab(3a + 5b) = 1234567?$$


<small>

* topic:ModularParity
* questionType:ProveDisprove
* concepts:equation

</small>





## Atrisinājums

Nepāru reizinājums nozīmē, ka $a,b$ ir nepāru. Bet tad $3a+5b$ ir pāru, kas ir pretruna. 



# <lo-sample/> LV.AMO.2012.7.2

Doti seši nogriežņi ar garumiem $1\mbox{cm}$, $3\mbox{cm}$, $5\mbox{cm}$, 
$7\mbox{cm}$, $9\mbox{cm}$, $11\mbox{cm}$. 
Cik dažādos veidos no tiem var izvēlēties trīs nogriežņus
tā, ka no tiem var izveidot trijstūri (katra trijstūra mala ir viens
vesels nogrieznis)?

<small>

* concepts:triangle,segment
* questionType:FindCount

</small>



# <lo-sample/> LV.AMO.2012.8.1

Starp skaitļiem

$$4\;\;1\;\;5\;\;7,$$

nemainot to secību, ievieto aritmētisko darbību zīmes ("$+$", "$-$", "$\ast$",
"$:$") un iekavas tā, lai iegūtās izteiksmes vērtība būtu **(A)** $13$, **(B)** $14$. 


<small>

* topic:AlgorithmsOnSyntaxTrees
* questionType:FindExample

</small>





## Atrisinājums

**(A)** $4 \ast 1 \ast 5 - 7 = 13$;  
**(B)** $4:(1-5:7) = 14$ bet arī $(4-1-5)\ast(-7)=14$.






# <lo-sample/> LV.AMO.2012.8.3

Skolas matemātikas olimpiādē piedalījās ne vairāk kā $60$ skolēnu.
Vidējais punktu skaits, ko ieguva zēni, bija $21,6$. Vidējais punktu
skaits, ko ieguva meitenes, bija $15$. Vidējais punktu skaits, ko ieguva
visi skolēni, bija $20$. Cik skolēnu piedalījās olimpiādē?


<small>

* topic:BaricenterCoordinates
* topic:NumTheoryInequalityMethod
* questionType:FindAll

</small>





## Atrisinājums

Pleci $1.6=|21.6-20|$ un $5=|15-20|$ attiecas kā $8$ un $25$. Zēnu ir $25$ un meiteņu $8$.





# <lo-sample/> LV.AMO.2012.8.4

Pa apli uzrakstīti $11$ veseli skaitļi. Jebkuru trīs pēc kārtas ņemtu
skaitļu summa dalās ar $5$. Pierādi, ka visi uzrakstītie skaitļi dalās ar
$5$.


<small>

* topic:PeriodicRemainders
* questionType:Prove
* concepts:sum,divisibility

</small>





## Atrisinājums

Atlikumi $(\operatorname{mod} 5)$ ik pēc $3$ atkārtojas, tātad tie visi vienādi (un vienādi $0$).



# <lo-sample/> LV.AMO.2012.9.1

Atrodi vienu skaitli, kuram ir tieši $12$ veseli pozitīvi dalītāji.

<small>

* topic:ModularArithmetic
* topic:ModularArithmetic
* questionType:FindExample
* concepts:divisors

</small>





# <lo-sample/> LV.AMO.2012.9.2

Trijstūrī $ABC$ $\angle ABC = 90^{\circ}$ , bet punkts $P$ atrodas uz malas $AB$.
Punkti $M$ un $N$ ir attiecīgi nogriežņu $AC$ un $PC$ viduspunkti. Pierādi,
ka $\angle BAC = \angle BMN$. 

<small>

* topic:TriangleCongruence
* questionType:Prove
* concepts:triangle

</small>




# <lo-sample/> LV.AMO.2012.9.3

Kvadrātvienādojuma $x^2 − 507x + a = 0$ saknes ir $p^2$ un $q$, kur $p$ un
$q$ ir pirmskaitļi. Aprēķini $a$ skaitlisko vērtību.

<small>

* topic:ModularArithmetic
* topic:ModularArithmetic
* questionType:FindAll
* concepts:quadratic-equation,primes

</small>





# <lo-sample/> LV.AMO.2012.9.4

Uz tāfeles uzrakstītas deviņas zvaigznītes 
$\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;$. 
Jānis ieraksta kādas zvaigznītes vietā jebkuru ciparu no $1$ līdz $9$. 
Pēc tam Pēteris jebkuru divu citu zvaigznīšu vietā ieraksta 
divus ciparus (tie var arī atkārtoties). Pēc tam vēl divas 
reizes viņi atkārto šo darbību.
Pēteris uzvar, ja iegūtais deviņciparu skaitlis dalās ar $37$. 
Vai Pēteris vienmēr var uzvarēt?

<small>

* topic:ModularArithmetic
* topic:ModularArithmetic
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2012.9.5


Dota trapece, kuras pamatu malu garumi ir $3$ un $13$.
Pierādi, ka to nevar sadalīt piecos vienlielos trijstūros.
(Figūras sauc par vienlielām, ja tām ir vienādi laukumi.)


<small>

* topic:TriangleAreaBaseHeight
* topic:Trapezoids
* questionType:Prove
* concepts:trapezoid,triangle

</small>






# <lo-sample/> LV.AMO.2012.10.1

Pierādi: ja $p$ un $14p^2+1$ ir pirmskaitļi, tad $14p^2-1$ ir naturāla
skaitļa kubs.

<small>

* topic:ModularArithmetic
* topic:ModularArithmetic
* questionType:Prove
* concepts:primes

</small>





## Atrisinājums

* Ja $p$ nedalās ar $3$, tad $p^2$ atlikums, dalot ar $3$, ir $1$. 
* Tad $14p^2$ dod atlikumu $2$, dalot ar $3$, jo skaitli ar atlikumu $2$ 
  reizina ar skaitli ar atlikumu $1$.
* Tad $14p^2+1$ dod atlikumu $0$, dalot ar $3$. Tas nav pirmskaitlis. 

Secinām, ka $p=3$ (citi pirmskaitļi nedalās ar $3$). Tādēļ 
$14p^2 +1 = 127$ un $14p^2 - 1 = 125$, kas tiešām ir pilns kubs $5^3$.




# <lo-sample/> LV.AMO.2012.11.1

Pierādi, ka nav tāda naturāla skaitļa $n$, ka skaitlis 
$n^2 − 3n − 1$ dalās ar $169$.

<small>

* concepts:divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2012.12.1

Skaitļi $A$ un $B$ ir divi dažādi $7$-ciparu skaitļi, 
kuri katrs satur visus ciparus no $1$ līdz $7$. 
Pierādi, ka $A$ nedalās ar $B$.

<small>

* concepts:divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.5.1


Cik reizes diennaktī sakrīt pulksteņa stundu un minūšu
rādītāji? (Plkst. 00:00 un 24:00 ieskaitīt vienu reizi.) *Atbildi pamatot!*

<small>

* questionType:FindCount

</small>



# <lo-sample/> LV.AMO.2013.5.2

$24$-stāvu mājā ir lifts, kuram ir divas pogas. 
Nospiežot vienu pogu,
tas paceļas (ja iespējams) $17$ stāvus uz augšu, nospiežot otru –
nolaižas $8$ stāvus uz leju (ja iespējams). Noskaidro, no kura stāva
ar šo liftu var nokļūt uz jebkuru citu
stāvu šajā mājā. (Lifts nevar uzbraukt
augstāk par 24. stāvu un zemāk par 1.
stāvu.)

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2013.5.3


1. zīmējumā katrā aplītī ierakstīt vienu
ciparu, katrā aplītī – citu, tā, lai katros
trīs aplīšos, kas atrodas uz vienas
taisnes, ierakstīto skaitļu summa būtu
viena un tā pati.  
[1.zīm.](LV.AMO.2013.5.3.png)

<small>

* concepts:sum
* questionType:FindExample

</small>


# <lo-sample/> LV.AMO.2013.5.4

No 2. zīmējumā redzamajām figūrām salikt
taisnstūri ar laukumu $40$ rūtiņas. Figūras nedrīkst
pārklāties un katra veida figūra jāizmanto vismaz
vienu reizi. (Figūras var būt pagrieztas vai
apgrieztas otrādi.) . 
[2.zīm.](LV.AMO.2013.5.4.png)

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.AMO.2013.5.5

Kuba katra skaldne sadalīta četros vienādos kvadrātos. Vai šos
kvadrātus var nokrāsot a) divās; b) trīs krāsās tā, ka kvadrāti, kam
ir kopīga mala, ir nokrāsoti dažādās krāsās? Katrs kvadrāts pilnībā
ir jākrāso vienā krāsā. *Atbildi pamatot!*

<small>

* questionType:ProveDisprove

</small>

# <lo-sample/> LV.AMO.2013.6.1

Uz tāfeles uzrakstīti desmit skaitļi:

$$1\;\;2\;\;3\;\;4\;\;5\;\;6\;\;7\;\;8\;\;9\;\;10.$$

Alfons nodzēš jebkurus divus no tiem (apzīmēsim tos ar $a$ un $b$)
un to vietā uzraksta skaitli, kas vienāds ar  $a+b+2$. Šo operāciju
viņš atkārto, kamēr uz tāfeles paliek viens skaitlis.
Pamato, ka neatkarīgi no secības, kādā Alfons izpilda darbības,
beigās tiek iegūts viens un tas pats skaitlis. Kāds tas ir?

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.6.2

Vai var atrast tādus divus viens otram sekojošus naturālus skaitļus,
viens no kuriem dalās ar $3$ un kuru  
**(A)** ciparu summas atšķiras par 3;   
**(B)** ciparu reizinājumi atšķiras par 3?

<small>

* concepts:divisibility,sum
* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.6.3

Sagriezt 3. zīmējumā attēloto figūru $20$
vienādās mazākās figūrās (figūras var būt
pagrieztas vai apgrieztas otrādi).   
![3.zīm.](LV.AMO.2013.6.3.png)

<small>

* questionType:FindExample

</small>

# <lo-sample/> LV.AMO.2013.6.4

Vai skaitļus no $100$ līdz $200$ var sadalīt divās grupās tā, ka skaitļu
reizinājumi abās grupās ir vienādi?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.6.5

Una un Ivo, gājienus izdarot pēc kārtas, kvadrāta ar izmēriem 5x5
rūtiņas trīs **tukšās** vienas rindas vai kolonnas **blakus** rūtiņās
ieraksta savu vārdu, katru burtu rakstot citā rūtiņā. Uzvar tas
spēlētājs, kurš pēdējais ieraksta savu vārdu. Una izdara pirmo
gājienu. Kurš spēlētājs vienmēr var panākt savu uzvaru?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.7.1

Naturālā divciparu skaitlī neviens no cipariem nav $0$. Pierādīt, ka,
dalot šo skaitli ar tā ciparu reizinājumu, dalījums ir vismaz $\frac{11}{9}$.


<small>

* topic:NumTheoryInequalityLargeIntervals
* topic:NotationPolynomial
* topic:NumTheoryExtremeElement
* questionType:Prove

</small>





## Atrisinājums

$\frac{10a+b}{ab}=\frac{10}{b}+\frac{1}{a}$ ir vismazākā, ja $a=b=9$.





# <lo-sample/> LV.AMO.2013.7.2

Doti seši nogriežņi ar garumiem $1\mbox{cm}$, $3\mbox{cm}$, $5\mbox{cm}$, 
$7\mbox{cm}$, $9\mbox{cm}$, $11\mbox{cm}$. 
Cik dažādos veidos no tiem var izvēlēties trīs nogriežņus
tā, ka no tiem var izveidot trijstūri (katra trijstūra mala ir viens
vesels nogrieznis)?

<small>

* sameAs:LV.AMO.2012.7.2
* concepts:triangle
* questionType:FindCound

</small>




# <lo-sample/> LV.AMO.2013.7.3

Pierādīt, ka skaitlis $1234567891011\ldots{}175176$ (pēc kārtas uzrakstīti
visi naturālie skaitļi no $1$ līdz $176$) nav naturāla skaitļa kvadrāts.
(Skaitļa kvadrāts ir skaitļa reizinājums pašam ar sevi.)


<small>

* topic:DivisibilityRulesLastDigits
* topic:DivisibilityRulesForRemainders
* topic:PrimeFactorizationAndPowers
* topic:SeriesMembersSumsClosedFormulas
* questionType:Prove

</small>



## Atrisinājums

Var izmantot dalāmību ar $3$ šādā spriedumā:

* Minētajam skaitlim ciparu summa kongruenta pēc moduļa $9$ ar
  $1+\ldots+176$. (Decimālciparu pārvietojot, atlikums nemainās).
* Summējam aritmētisku progresiju: 
  $1+\ldots+176=(176\cdot 177)/2$ - dalās ar $3$, bet ne ar $9$.
* Pilns kvadrāts nevar saturēt pirmskaitli $3$ nepāru pakāpē.

Cits atrisinājums izmanto dalāmību ar $2$:

* Pilnu kvadrātu dalījums pirmreizinātājos 
  nevar dalīties ar $8$ un nedalīties ar $16$ – 
  saturēt pirmskaitli $2$ nepāru pakāpē.



# <lo-sample/> LV.AMO.2013.7.4

Vai kvadrātā $5 \times 5$ rūtiņas var iekrāsot **(a)** $6$ rūtiņas; **(b)** $5$ rūtiņas tā,
lai atlikušajā daļā nevarētu ievietot nevienu 4. zīmējumā redzamo
figūru (tā var būt pagriezta vai apgāzta otrādi)?  
![4.zīm](LV.AMO.2013.7.4.png)

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.AMO.2013.7.5

Una un Ivo, gājienus izdarot pēc kārtas, kvadrāta ar izmēriem $6 \times 6$
rūtiņas trīs **tukšās** vienas rindas vai kolonnas **blakus** rūtiņās
ieraksta savu vārdu, katru burtu rakstot citā rūtiņā. Uzvar tas
spēlētājs, kurš pēdējais ieraksta savu vārdu. Una izdara pirmo
gājienu. Kurš spēlētājs vienmēr var panākt savu uzvaru?

<small>

* questionType:FindExample

</small>


# <lo-sample/> LV.AMO.2013.8.1

Atrast visus naturālos skaitļus, kas nepārsniedz $1000000$ un kuri,
nosvītrojot to pirmo ciparu, samazinās $36$ reizes.


<small>

* topic:NumTheoryExpr
* topic:NotationFragments
* questionType:FindAll

</small>



## Atrisinājums

Uzrakstām algebriski, ko nozīmē pirmā cipara nodalīšana no pārējā gabala

$a$ - 1.cipars; $a \cdot 10^k + b = 36b$; $a \cdot 10^k = 35b$. 
Tad $a = 7$, $b=2\cdot 10^{k-1}$. 



# <lo-sample/> LV.AMO.2013.8.2

Dots trijstūris $ABC$ un punkts $P$ tā iekšpusē. Pierādi, ka attālumu
summa no punkta $P$ līdz dotā trijstūra virsotnēm ir lielāka nekā
puse no trijstūra perimetra.

<small>

* concepts:triangle,perimeter
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.8.3

Doti tādi reāli skaitļi $t$ un $a$, ka 
$t^2 - t \cdot sqrt(t) + a = 0$.  
Pierādīt, ka $t \geq 4a$. 

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.8.4

Vai regulāru sešstūri var sadalīt **(A)** deviņos; **(B)** astoņos vienādos
daudzstūros?

<small>

* questionType:ProveDisprove,ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.8.5

Rūķītis ir iedomājies skaitļus $x_1,x_2,x_3,x_4$, 
katrs no tiem ir vai nu $0$, vai $1$. 
Ja rūķītim pajautā: "Kāds ir $i$-tais skaitlis?" ($i = 1, 2, 3\ \mbox{vai}\ 4$ 
pēc izvēles), tad viņš pasaka $x_i$ vērtību. 
Pierādīt, ka ar $3$ jautājumiem pietiek, lai uzzinātu, vai virkne 
$x_1,x_2,x_3,x_4$ ir monotona.  
Skaitļu virkne $x_1,x_2,x_3,x_4$ ir monotona, ja tā ir nedilstoša vai neaugoša 
(t. i., $x_1 \leq x_2 \leq x_3 \leq x_4$ vai
$x_1 \geq x_2 \geq x_3 \geq x_4$).

<small>

* concepts:monotonic-sequence
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.9.1

Dota trapece, kuras pamatu malu garumi ir $3$ un $13$. Pierādīt, ka to
nevar sadalīt piecos vienlielos trijstūros.
(Figūras sauc par vienlielām, ja tām ir vienādi laukumi.)

<small>

* concepts:trapezoid,triangle
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.9.2

Kvadrāta ar izmēriem $4 \times 4$ rūtiņas katra rūtiņu virsotne nokrāsota
vienā no divām krāsām. Pierādīt, ka noteikti var atrast trīs punktus,
kas nokrāsoti vienā krāsā un atrodas vienādsānu taisnleņķa
trijstūra virsotnēs.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.9.3

Doti četri dažādi cipari, neviens no kuriem nav $0$. Visu divciparu
skaitļu, kurus var izveidot no šiem cipariem, summa ir $484$. Atrast
dotos četrus ciparus.

<small>

* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2013.9.4

Dota skaitļu virkne $x_0,x_1,x_2_,x_3,\ldots$, 
kurā $x_0 \geq 0$ un $x_{n+1}=x_n + \frac{2}{x_n}$ visiem 
$n \geq 0$. Pierādīt, ka $x_{100} \geq 20$. 

<small>

* concepts:sequence
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.9.5

Dots izliekts četrstūris. Uzzīmēti četri riņķi, kuru diametri ir
četrstūra malas. Pierādīt, ka šie riņķi pilnībā pārklāj doto četrstūri.

<small>

* concepts:square-Geo,circle
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.10.1

Dots, ka $x_1$ ir vienādojuma $x^2+px+q=0$ sakne, 
bet $x_2$ ir vienādojuma $-x^2+px+q=0$ sakne. Pierādīt, ka vienādojumam 
${\displaystyle \frac{1}{3}x^2+px+q=0 }$ noteikti ir sakne $x_3$, kas 
atrodas starp $x_1$ un $x_2$ (t.i., $x_1 \leq x_3 \leq x_2$ vai 
$x_2 \leq x_3 \leq x_1$).

<small>

* concepts:equation,root
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.10.2

Trijstūrī $ABC$ nogrieznis $CD$ ir bisektrise. Caur punktu $C$ novilkta
riņķa līnija, kas pieskaras malai $AB$ punktā $D$. Tā krusto malas $AC$
un $BC$ attiecīgi punktos $P$ un $Q$. Pierādīt, ka
$AB \parallel PQ$.

<small>

* concepts:circumference
* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.10.3

Par $n$-heksu sauksim plaknes figūru, kas
izveidota no $n$ regulāriem sešstūriem tā, ka
katram sešstūrim ir kopīga mala ar vismaz
vienu citu sešstūri.
Kādam mazākajam $n$ ($n \geq 2$) eksistē tāds
$n$-hekss, ar kuriem nevar pārklāt 5. zīm.
attēloto figūru (tā sastāv no regulāriem
sešstūriem ar caurumu centrā)?  
![5.zīm](LV.AMO.2013.10.3.png)

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.AMO.2013.10.4

No pirmajiem $100$ naturālajiem skaitļiem izvēlēts $51$ skaitlis.
Pierādīt, ka no tiem var izvēlēties divus, no kuriem viens dalās ar
otru.

<small>

* topic:ArithmeticAndGeometricSeries
* topic:NumTheoryPigeonhole
* questionType:Prove
* concepts:divisibility

</small>





## Atrisinājums

Izrakstām ģeometriskas progresijas, kas sākas ar nepāru skaitļiem un $q=2$: 

$$(1,2,4,8,16,32,64),\;(3,6,12,24,48,96),$$

$$(5,10,20,40,80),\ldots,(97),\;(99).$$

* Būs tieši $50$ progresijas (dažās būs tikai pa vienam loceklim), jo līdz $100$ ir tieši $50$ nepāru skaitļi.
* Katrs skaitlis pieder tieši vienai progresijai, jo katram pāru skaitlim atbilst tieši viens nepāru 
skaitlis, kurš rodas, ja atkārtoti dala ar $2$. 
* Izvēloties $k+1$ skaitļus, vismaz divi būs no vienas progresijas (Dirihlē princips).


*Piezīme:*
Ja skaitļu ir tikai $50$, tad līdzīgi secināt nevar.
Var izvēlēties $51,\ldots,100$ - no tiem neviens nedalās ar otru.




# <lo-sample/> LV.AMO.2013.10.5

Vai pa riņķi var uzrakstīt $2013$ naturālus skaitļus tā, lai jebkuru
divu blakus esošu skaitļu attiecība būtu $2$, $3$, $12$ vai $18$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.11.1

Pierādīt, ka nav tāda naturāla skaitļa $n$, ka skaitlis 
$n^2-3n-1$ ar $169$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.11.2

Vai eksistē regulārs daudzstūris, kuram vienas diagonāles garums
ir vienāds ar divu citu diagonāļu garumu summu?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2013.11.3

Doti dažādi nepāra naturāli skaitļi $a_1, a_2, \ldots, a_n$. 
Neviens no tiem nedalās ne ar vienu pirmskaitli, kas lielāks 
kā $5$. Pierādīt, ka

$$\frac{1}{a_1} + \frac{1}{a_2} + \frac{1}{a_3} + \ldots \frac{1}{a_n} < 2.$$

<small>

* concepts:primes,divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.11.4

Kādā valstī ir $2013$ pilsētas, no katras uz katru var aizlidot ar
lidmašīnu. Dažus no šiem reisiem apkalpo aviokompānija $A$,
pārējos – aviokompānija $B$ (ir iespējams, ka no pilsētas $X$ uz
pilsētu $Y$ lido aviokompānijas $A$ lidmašīna, bet no $Y$ uz $X$ --
aviokompānijas $B$ lidmašīna).  
Pierādīt, ka aviokompāniju atbildību par reisiem iespējams
saplānot tā, ka ceļotājs, izlidojot no jebkuras pilsētas $Z$, pa ceļam
apmeklējot vienu vai vairākas pilsētas un pēc tam atgriežoties
pilsētā $Z$, **noteikti** būs lidojis ar abu aviokompāniju lidmašīnām,
neatkarīgi no tā, kādu maršrutu viņš būs izvēlējies un kura ir
sākotnējā pilsēta $Z$.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.11.5

Uz galda virsmas, kurai ir taisnstūra forma, izvietoti vairāki
vienādi kvadrātveida papīra gabaliņi, kuru malas ir paralēlas galda
malām (kvadrātiņi var arī pārklāties). Pierādīt, ka galdā var iedurt
dažas adatas tā, ka katrs papīra gabaliņš būs piesprausts pie galda
tieši ar vienu adatu.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.12.1

Atrisināt reālos skaitļos vienādojumu 
${\displaystyle \log_{10} x  \cdot \log_{10} (4-x)=\frac{1}{4}}$.

<small>

* concepts:equation
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2013.12.2

Trijstūrī $ABC$ punkti $M$, $N$ un $K$ ir attiecīgi malu $AB$, $BC$ un $CA$
viduspunkti. Ir novilktas trīs riņķa līnijas: caur punktiem $K$, $A$, $M$;
caur punktiem $M$, $B$, $N$; caur punktiem $N$, $C$, $K$. Pierādīt, ka visas
novilktās riņķa līnijas krustojas vienā punktā.

<small>

* concepts:circumference
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.12.3

Pierādīt, ka neeksistē tādi naturāli skaitļi $x, y, z$, ka izpildās
vienādība $6^x + 13^y = 29^z$.

<small>

* concepts:equation
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2013.12.4

Kādas valodas alfabētā ir $i$ patskaņi ($i \geq 2$) un 
$j$ līdzskaņi ($j \geq 2$).
Šajā valodā par vārdu sauc jebkuru galīgu burtu (patskaņu un
līdzskaņu) virkni, kas satur vismaz vienu burtu un kurā nekādi divi
patskaņi neparādās pēc kārtas un pēc kārtas uzrakstīti līdzskaņi ir
ne vairāk kā divi (piemēram, ja "A" ir patskanis, bet "B" –
līdzskanis, tad, piemēram, "ABBA" ir vārds, turpretī "BAAB" un
"ABBBA" nav vārdi).  
Ar $S(n)$ apzīmēsim visu to vārdu skaitu, kuri sastāv no $n$ burtiem, $n \geq 1$. 
Pierādīt, ka visiem naturāliem skaitļiem n ir spēkā vienādība

$$S(n+3) = i \cdot j \cdot S(n+1) + i \cdot j^2 \cdot S(n).$$

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2013.12.5

Dota kvadrātisku rūtiņu plakne, katras rūtiņas malas garums ir $1$.
Pierādīt, ka eksistē trijstūris, kura virsotnes atrodas šīs plaknes
rūtiņu virsotnēs un jebkuru divu tā malu garumi atšķiras ne vairāk
kā par ${\displaystyle \frac{1}{2013 \cdot \sqrt{P}}}$, 
kur $P$ ir šī trijstūra perimetrs.

<small>

* questionType:Prove

</small>


# <lo-sample/> LV.AMO.2014.5.1

Pūkainīšu ciemata bērniem Lieldienu zaķis atnesa olas. Katra no tām bija nokrāsota tieši
vienā no krāsām – sarkanā, dzeltenā, zilā. Zināms, ka $20\%$ jeb $40$ olas bija sarkanas,
$\frac{3}{4}$ no atlikušajām bija dzeltenas, bet pārējās -- zilas. Aprēķini:  
**(A)** Cik olas bija zilā krāsā?  
**(B)** Kāda daļa no visām olām bija zilas?  
**(C)** Cik procenti no visām olām bija dzeltenas?

<small>

* topic:AlgebraicEquations
* questionType:FindAll,FindAll,FindAll

</small>





# <lo-sample/> LV.AMO.2014.5.2

Divu naturālu skaitļu pierakstā izmantoti tikai cipari $2$, $3$, $7$ un $8$. Vai var gadīties, ka viens
skaitlis ir tieši trīs reizes lielāks nekā otrs skaitlis?

<small>

* topic:IntegerCongruence
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2014.5.3

Taisnstūra ABCD malu garumi izsakāmi veselos centimetros. Iekrāsotās daļas laukums ir 
$6$ $\mbox{cm}^2$ (skat. 1. zīm.). Nogrieznis $AE$ ir $\frac{1}{3}$
no taisnstūra malas $AD$. Aprēķini taisnstūra
laukumu un perimetru, ja zināms, ka viena taisnstūra mala ir par $5$ $\mbox{cm}$ garāka nekā otra
mala.  
![1.zīm.](LV.AMO.2014.5.3.png)

<small>

* topic:Rectangles
* questionType:FindAll
* concepts:rectangle,area,perimeter

</small>




# <lo-sample/> LV.AMO.2014.5.4

Kvadrāts sastāv no $8 \times 8$ vienādām kvadrātiskām rūtiņām. Tas sagriezts daļās tā, ka
griezumi iet pa rūtiņu robežām.  
Kāds lielākais skaits daļu var būt tādas kā 2. zīm. attēlotā figūra (figūras var būt pagrieztas
jebkurā stāvoklī)?  
![2.zīm.](LV.AMO.2014.5.4.png)

<small>

* topic:SquareGridCutting
* questionType:FindOptimal

</small>




# <lo-sample/> LV.AMO.2014.5.5

Kāds ir **(a)** mazākais, **(b)** lielākais skaitlis, kuru var izteikt gan kā trīs, gan kā divu dažādu
divciparu naturālu skaitļu reizinājumu?

<small>

* topic:NumTheoryInequalityLargeIntervals
* questionType:FindOptimal,FindOptimal
* concepts:product

</small>









# <lo-sample/> LV.AMO.2014.7.2

Vai var atrast tādus veselus skaitļus $a$ un $b$, 
kuriem izpildās vienādība $a \cdot (3a + 5b) \cdot 7b = 7654321$. 


<small>

* topic:ModularParity
* questionType:ProveDisprove

</small>






## Atrisinājums

Nepāru reizinājums nozīmē, ka $a,b$ ir nepāru. 
Bet tad $3a+5b$ ir pāru, kas ir pretruna. 



# <lo-sample/> LV.AMO.2014.7.1

Trijstūrī $ABC$ novilkts augstums $BD$ un mediāna $BE$. Kāds var būt $AC$ garums, ja
$ED = 4\mbox{cm}$ un $DC = 5\mbox{cm}$? 

<small>

* concepts:triangle,height,median
* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2014.7.4

Tabulas $3 \times 3$ rūtiņās katrā rūtiņā jāieraksta pa vienam naturālam skaitlim tā, 
lai katrā rindā,
katrā kolonnā un katrā diagonālē ierakstīto skaitļu summas būtu vienādas. Ir zināmi divās
rūtiņās ierakstītie skaitļi (skat.\ zīm.). Kādam skaitlim jābūt rūtiņā, kas apzīmēta ar
jautājuma zīmi? Atrodiet visas iespējamās vērtības un pamatojiet, ka citu nav!

![](LV.AMO.2014.7.4.png)


<small>

* topic:NumTheoryExprVariables
* questionType:FindAll
* genre:magic-configuration

</small>



## Atrisinājums

Ja $a_{22}=x$, tad summas ir $3x$. Un $a_{13}=2x-13$,
$a_{11}=x-11$, $a_{33}=x+11$, $a_{23}=2$.






# <lo-sample/> LV.AMO.2014.8.1

Skaitli $\frac{1}{13}$
pārveidoja par bezgalīgu decimāldaļu un tajā izsvītroja 2014. ciparu aiz komata.
Kurš skaitlis lielāks – sākotnējais vai iegūtais?


<small>

* topic:PeriodicRemainders
* topic:NumericAlgorithms
* questionType:FindAll
* concepts:decimal-fractions
* genre:digit-manipulation

</small>





## Atrisinājums

$1/13=0.(076923076923)$ (periods $12$ cipari). 
$2014$-tais cipars ir tāds pats kā $10$-tais cipars ir $9$, 
aiz kura seko cipars $2$. Izsvītrojot šo ciparu $9$, tas aizstājas
ar $2$, tāpēc skaitlis kļūst mazāks.






# <lo-sample/> LV.AMO.2014.8.2

Atrast visus naturālos skaitļus, kas nepārsniedz 
$1000000$ un kuri, nosvītrojot to pirmo
ciparu, samazinās $15$ reizes!


<small>

* topic:NumTheoryExpr
* topic:NotationFragments
* questionType:FindAll

</small>





## Atrisinājums

$a$ - 1.cipars; $a \cdot 10^k + b = 15b$; $a \cdot 10^k = 14b$. 
Tad $a = 7$, $b=5\cdot 10^{k-1}$. 





# <lo-sample/> LV.AMO.2014.8.5

Tabulas $3 \times 3$ rūtiņās katrā rūtiņā jāieraksta pa vienam naturālam skaitlim tā, lai katrā rindā,
katrā kolonnā un katrā diagonālē ierakstīto skaitļu summas būtu vienādas. Augšējās rindas
vidējā rūtiņā ierakstīts skaitlis $24$ (skat.\ zīm.). Vai rūtiņā, kas apzīmēta ar jautājuma
zīmi, var būt ierakstīts skaitlis **(a)** $7$,  **(b)** $17$?

![magicsquare](LV.AMO.2014.8.5.png)


<small>

* topic:NumTheoryExprVariables
* topic:TreeTraversalBacktracking
* questionType:ProveDisprove

</small>



## Atrisinājums

Apzīmējam $a_{22}=x$, $a_{31}=b$. 

Tad $a_{13}=2x-b$, $a_{11}=x+b-24$, $a_{33}=x-b+24$, $a_{23}=2b-24$. Pie $b=7$, $a_{23}<0$.




# <lo-sample/> LV.AMO.2014.9.2

Doti četri dažādi cipari, neviens no tiem nav $0$. Visu divciparu skaitļu, 
kurus var izveidot no
šiem cipariem, summa ir $1276$. Atrast dotos četrus ciparus!

<small>

* concepts:sum
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2014.9.4

Tabulas $3 \times 3$ rūtiņās katrā rūtiņā jāieraksta pa vienam 
naturālam skaitlim tā, lai katrā rindā,
katrā kolonnā un katrā diagonālē ierakstīto skaitļu summas 
būtu vienādas, bet visi tabulā
ierakstītie skaitļi ir savā starpā atšķirīgi. Ir zināmi 
divās rūtiņās ierakstītie skaitļi (skat. zīm.). Kāds ir mazākais 
skaitlis, kas var būt ierakstīts tabulas centrālajā rūtiņā?

![magic square](LV.AMO.2014.9.4.png)

<small>

* questionType:FindOptimal

</small>



# <lo-sample/> LV.AMO.2014.10.4

Doti septiņi dažādi naturāli skaitļi; katriem diviem 
no dotajiem skaitļiem aprēķināja to
summu. Kāds lielākais skaits no šīm summām var būt pirmskaitļi?

<small>

* topic:ModularParity
* topic:BipartiteGraphs
* topic:ModularArithmetic
* topic:TreeTraversalBacktracking
* questionType:FindOptimal
* concepts:sum,primes

</small>




## Atrisinājums


Ievērojam, ka vajadzīgs lielākais *skaits*, kas var būt 
pirmskaitļi. Nevis lielākais *dažādu pirmskaitļu* skaits, ko 
var šādi iegūt.

Dažādu naturālu skaitļu summa nevar būt $2$.
Tātad, lai divu skaitļu summa būtu (nepāru) pirmskaitlis, 
viens no tiem ir pāru, otrs ir nepāru. 
Cik no 7 ir pāru un cik nepāru skaitļu?

$$7=0+7=1+6=2+5=3+4=4+3=5+2=6+1=7+0$$

Lielākais teorētiski iespējamais $(n,p)$ pārīšu skaits ir tad, 
ja $4$ no septiņiem skaitļiem ir nepāru un $3$ ir pāru (vai otrādi):
$4\cdot{}3=12$.

Zīmējam grafu:

![](LV.AMO.2014.10.4A.png)

* Nepāru skaitļi veido kopu $A$ ar $4$ elementiem, 
  pāru skaitļi veido kopu $B$ ar $3$ elementiem. 
* Ir tikai $4\cdot{}3$ pāri, kam ir cerība būt pirmskaitļiem. 
  (Saskaitot $p+p$ vai $n+n$ pirmskaitli iegūt nevar.)


**Definīcija:** Ja grafā visas virsotnes var sadalīt divās nepārklājošās 
apakškopās $A$ un $B$ tā, ka jebkura grafa šķautne iet no virsotnes 
kopā $A$ uz virsotni kopā $B$, tad grafu sauc par *divdaļīgu*.  

**Apgalvojums:** Ja divdaļīgā grafā apakškopās $A$ un $B$ ir attiecīgi 
$a$ un $b$ virsotnes, tad tajā ir ne vairāk kā $a\cdot{}b$ šķautnes.

Aplūkojam atlikumus, dalot ar 3.

![](LV.AMO.2014.10.4B.png)

* Izvēloties vismazākos nepāru un pāru skaitļus, tikai $9$ no $12$ 
  teorētiski iespējamajiem ir pirmskaitļi (citas summas dalās ar $9$ - 
  apzīmētas ar raustītu līniju). 
* Ja papildus prasa, lai visi $7$ skaitļi dotu atlikumu $1$ 
  (vai, izņēmuma gadījumā, atlikumu $0$), 
  dalot ar $3$, var panākt, lai visas $12$ summas būtu pirmskaitļi.



# <lo-sample/> LV.AMO.2014.11.2

Skaitļu virknei $(a_i)$ visiem $n>1$ ir spēkā sakarība 
$a_1 + a_2 + \ldots + a_n = n^2 a_n$. Aprēķināt $a_{50}$,
ja zināms, ka $a_1 = 1000$.

<small>

* concepts:sequence
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2014.11.4

Doti $99$ naturāli skaitļi. Zināms, ka nav tāda skaitļa, 
ar ko dalītos visi šie skaitļi, un ka
jebkuru $50$ skaitļu reizinājums dalās ar atlikušo $49$ 
skaitļu reizinājumu. Pierādīt, ka visu $99$
skaitļu reizinājums ir naturāla skaitļa kvadrāts.

<small>

* concepts:product,square-Alg
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2014.12.3

Atrast visus pirmskaitļus $p$, 
kuriem $p^4 − 6$ arī ir pirmskaitlis!

<small>

* concepts:primes
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2015.7.3

**(A)** Atrast tādu naturālu skaitli, kura ciparu summa ir $13$, pēdējie divi
cipari ir $13$ un kurš dalās ar $13$.  
**(B)** Vai var atrast tādu naturālu skaitli, kura ciparu summa ir $11$, pēdējie
divi cipari ir $11$ un kurš dalās ar $11$?


<small>

* topic:DivisibilityRuleFor11
* topic:DivisibilityRulesFor3And9
* questionType:FindExample,ProveDisprove
* concepts:sum

</small>


## Atrisinājums

**(A)** $117$ cip.summa $9$, dalās ar $13$. $11713$ der.  
**(B)** $99k$ pāru/nepāru poz.cip.summa nevar būt $9$.



# <lo-sample/> LV.AMO.2015.7.4

Vienādsānu trijstūrī $ABC$ uz pamata malas $BC$ atzīmēts iekšējs punkts $D$
tā, ka arī trijstūri $ABD$ un $ACD$ ir vienādsānu. Aprēķini trijstūra $ABC$
leņķus! Atrodi visus gadījumus un pamato, ka citu nav!

<small>

* concepts:isosceles-triangle
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2015.8.1

Nosaki, vai izteiksmes $\sqrt{6 + 2\sqrt{5}} + \sqrt{6 - 2\sqrt{5}}$ 
vērtība ir racionāls skaitlis!


<small>

* topic:StandardIdentities
* topic:InfiniteDescent
* questionType:ProveDisprove
* concepts:rational-numbers

</small>



## Atrisinājums

Kāpinot kvadrātā sanāk $20$, bet $\sqrt{20}=2\sqrt{5}$ nav racionāls.





# <lo-sample/> LV.AMO.2015.8.3

Atrast vienu naturālu skaitli, kas lielāks nekā $2015$ un ko nevar izteikt kā
naturāla skaitļa kvadrāta un pirmskaitļa summu.


<small>

* topic:StandardIdentities
* topic:PrimesDistribution
* questionType:FindExample
* concepts:primes,sum,square-Alg

</small>


## Atrisinājums

Ja $N = n^2$ 
liels pilns kvadrāts, tad $n^2 - a^2$ dalās reizinātājos $>2$.


# <lo-sample/> LV.AMO.2015.9.3

Pierādi, ka $x^5 - 5x^3 + 4x$ dalās ar $120$, ja $x$ ir vesels skaitlis!

<small>

* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2015.10.3

Atrast visus naturālos skaitļus, kas ir vienādi ar savu ciparu reizinājumu.
(Par viencipara skaitļa ciparu reizinājumu sauc tā vienīgo ciparu.)

<small>

* strategies:TrialAndError
* topic:InequalityProvingStronger
* questionType:FindAll
* concepts:product

</small>





## Atrisinājums

* Pārbaudot dažādus skaitļus var novērot, ka ciparu reizinājums allaž mazāks par pašu skaitli.
* Pamatojam to 2-ciparu un 3-ciparu skaitļiem $\overline{ab}$ un $\overline{abc}$

$$a\cdot{}b < 10a \leq 10^1\cdot{}a + b = \overline{ab},$$

$$a\cdot{}b\cdot{}c < 10^2\cdot{}a < 100a + 10b + c = \overline{abc}.$$

Skaitļa pirmo decimālciparu reizinot ar $k$ turpmākajiem cipariem, iegūsim 
mazāku rezultātu nekā reizinot ar $10^k$, jo katrs cipars ir mazāks par $10$. 




# <lo-sample/> LV.AMO.2015.11.1

Aplūkojam visus deviņciparu skaitļus, kas nesatur $0$ 
un kam visi cipari ir dažādi. 
Pierādīt, ka starp tiem pāra skaitļu ir tieši divas reizes mazāk
nekā tādu, kas dalās ar $3$, bet nedalās ar $5$.

<small>

* concepts:divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2015.11.3

Naturālam skaitlim $n$ ar $M(n)$ apzīmēsim mazāko naturālo skaitli, kas
beidzas ar $n$ un kura ciparu summa ir $n$. Piemēram, $M(13)=913$.
Pierādīt, ka ir bezgalīgi daudz tādu $n$, ka $M(n)$ dalās ar $n$.

<small>

* concepts:divisibility
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2015.12.5

Atrast visus naturālu skaitļu trijniekus $(a,b,c)$, tādus, ka 
$a \geq b \geq c \geq 2$
un $ab-1$ dalās ar c, $bc-1$ dalās ar $a$, $ac-1$ dalās ar $b$.

<small>

* concepts:divisibility
* questionType:FindAll

</small>










# <lo-sample/> LV.AMO.2016.7.2

Karlsons sev pusdienām nopirka $8$ pīrādziņus un $15$ magoņmaizītes, bet
Brālītis – vienu pīrādziņu un vienu magoņmaizīti. Karlsons par savām
pusdienām samaksāja tieši divus eiro (katra maizīte un pīrādziņš maksā veselu
skaitu centu). Cik samaksāja Brālītis?


<small>

* topic:NumTheoryExpr
* topic:NumTheoryExprForConcepts
* topic:NumTheoryInequalityMethod
* questionType:FindAll

</small>


## Atrisinājums

$200-8p=15m$, t.i. $m$ dalās ar $8$. Un $m$ nevar būt $16$, citādi $p<0$.  





# <lo-sample/> LV.AMO.2016.7.3

Dots, ka $AB\parallel{}CD$ un $AD\parallel{}BC$ (skat. 1.att.).
Nogriežņu $AC$ un $BD$ krustpunkts ir $M$. Uz taisnes
$AB$ izvēlēts tāds punkts $N$, ka $AM=MN$. Pierādīt,
ka $\angle ANC=90^{\circ}$.  
![1.att.](geometry-grade07/LV.AMO.2016.7.3.png)

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.AMO.2016.8.1

Aprēķini dotās izteiksmes vērtību!

$$\frac{2000016 \cdot 1999984}{5^{12} \cdot 2^{13} - 128}$$


<small>

* topic:StandardIdentities
* questionType:FindAll
* concepts:expression

</small>



## Atrisinājums

Rakstām algebrisku pārveidojumu:
$\frac{4(10^6 - 8)(10^6 + 8)}{2(10^{12} -64)} = \frac{4}{2}=2$. 



# <lo-sample/> LV.AMO.2016.8.2

Vai var atrast tādus veselus skaitļus $a$ un $b$, ka $ab(a+43b) = 434343$?


<small>

* topic:ModularParity
* questionType:ProveDisprove

</small>


## Atrisinājums

Reizinājums ir nepāru, t.i. $a,b$ ir nepāru. Bet tad $a+43b$ ir pāru. 



# <lo-sample/> LV.AMO.2016.8.3

Zināms, ka skaitlis dalās ar $2016$ un ka visi tā cipari ir dažādi. Kāds ir lielākais
ciparu skaits, kas var būt šajā skaitlī?


<small>

* topic:DivisibilityRulesLastDigits
* topic:DivisibilityRulesFor3And9
* topic:DivisibilityRulesOther
* topic:ExhaustionMethod
* questionType:FindOptimal
* concepts:divisibility

</small>

## Atrisinājums

Visi $10$ cipari: $32 \mid 45312$. 
Ciparu summa dalās ar $9$. Samaisa $6,7,8,9,0$, lai dalās ar $7$.




# <lo-sample/> LV.AMO.2016.9.2

Vai var atrast tādus veselus skaitļus $x$, $y$ un $z$, ka 
$x^3 − 2016xyz = 10$?

<small>

* seeAlso:LV.AMO.2016.10.2
* questionType:ProveDisprove

</small>




# <lo-sample/> LV.AMO.2016.9.4

Naturālu skaitļu virknes $1; 2; 2; 4; 8; 32; 48; \ldots$ 
katrs loceklis, sākot ar trešo, ir
vienāds ar divu iepriekšējo locekļu nenulles ciparu reizinājumu. 
Kāds ir šīs virknes 2016. loceklis?

<small>

* concepts:sequence,product
* questionType:FindAll

</small>


# <lo-sample/> LV.AMO.2016.10.2

Vai var atrast tādus veselus skaitļus $x$, $y$ un $z$, ka
$x^3 − 2016xyz = 120$?

<small>

* topic:DivisibilityRulesForRemainders
* topic:ModularArithmetic
* topic:ModularArithmeticContradiction 
* questionType:ProveDisprove
* seeAlso:LV.AMO.2016.9.2

</small>


## Atrisinājums

Pretrunas modulis: aplūkojam abu vienādības pušu atlikumus, dalot ar $9$. 
Tā kā $2016$ dalās ar $9$, tad $x^3 \equiv 3 \pmod {9}$. Pārbaudot visus 
kubus $0^3,1^3,\ldots,8^3$, neviens no tiem nedod atlikumu $3$, dalot ar $9$.




# <lo-sample/> LV.AMO.2016.10.3

Aritmētiskās progresijas četri pēc kārtas ņemti locekļi ir veseli
skaitļi $A$, $B$, $C$ un $D$. Pierādīt, ka
$A^2+2B^2+3C^2+4D^2$
var izteikt kā divu
veselu skaitļu kvadrātu summu!

<small>

* topic:SeriesMembersSumsClosedFormulas
* topic:StandardIdentities
* topic:CompletingSquare
* questionType:Prove
* concepts:arithmetic-progression,sum,square-Alg

</small>






# <lo-sample/> LV.AMO.2016.11.2

Vai var atrast tādus naturālus skaitļus $x$, $y$ un $z$, 
ka $x^2 + y^2 + z^2 = \underbrace{1111 \ldots 1}_{2016}$?

<small>

* questionType:ProveDisprove

</small>


# <lo-sample/> LV.AMO.2016.12.2

Pierādīt, ka vienādojumam $10^x + 12^y = 34^z$ nav 
atrisinājuma naturālos skaitļos!

<small>

* concepts:equation
* questionType:Prove

</small>





# <lo-sample/> LV.AMO.2017.7.3


Divus taisnstūra lapas stūrus nolocīja tā, kā parādīts 3.att. Izrādījās, ka lapas
apakšējā mala tika sadalīta trīs vienāda garuma nogriežņos un augšējā mala –
divos vienāda garuma nogriežņos. Pierādīt, ka iekrāsotais trijstūris ir
vienādmalu!  
![LV.AMO.2017.7.3](LV.AMO.2017.7.3.png)

<small>

* concepts:equilateral-triangle
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2017.7.5

Cik ir tādu naturālu divciparu skaitļu, kuriem ciparu reizinājums ir tieši divas
reizes mazāks nekā pats skaitlis?

<small>

* questionType:FindCount
* concepts:product

</small>




# <lo-sample/> LV.AMO.2017.8.5

Vai var atrast tādu desmitciparu skaitli, kas ir vienāds ar visu savu ciparu
reizinājumu?

<small>

* questionType:ProveDisprove
* concepts:product

</small>






# <lo-sample/> LV.AMO.2017.9.5

Atrisināt naturālos skaitļos vienādojumu 
$x^3 + (x+1)^3 = (x+3)^3 + 1$.

<small>

* concepts:equation
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2017.10.5

Pierādīt, ja no trim naturāliem skaitļiem $n$; $n+11$ un $n+22$ divi ir
pirmskaitļi, tad trešais skaitlis dalās ar $6$.

<small>

* topic:DivisibilityProperties
* topic:ArithmeticSeriesAll
* strategy:CaseAnalysis
* questionType:Prove
* concepts:primes

</small>

## Ieteikums 

Gadījumus $n=2,3$ aplūko atsevišķi.



# <lo-sample/> LV.AMO.2017.11.5

Doti naturāli skaitļi $k$ un $n$, $k \leq n$.  
**(A)** Vai noteikti $C_n^k$ dalās ar $n$, ja $k$ un $n$ ir savstarpēji pirmskaitļi?  
**(B)** Vai $k$ un $n$ noteikti ir savstarpēji pirmskaitļi, ja $C_n^k$ dalās ar $n$?  
*Piezīme.* Ar $C_n^k$ apzīmēts kombināciju skaits no $n$ elementiem pa $k$
elementiem.

<small>

* concepts:coprimes
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2017.12.5

**(A)** Doti naturāli skaitļi no $1$ līdz $11$. Izvēlieties deviņus no tiem 
un ierakstiet tos $3 \times 3$ rūtiņu tabulā tā, lai katrā rindā, 
katrā kolonā un abās galvenajās diagonālēs ierakstīto skaitļu 
summa dalās ar $7$.   
**(B)** Vai to pašu ir iespējams izdarīt, ja doti naturāli skaitļi no $1$ līdz $10$?

<small>

* questionType:FindExample,ProveDisprove

</small>






# <lo-sample/> LV.AMO.2018.7.3


Uz trijstūra $ABC$ malas $AB$ izvēlēts patvaļīgs iekšējs punkts $D$. Pierādīt, ka 
$CD > \frac{1}{2}(CA+CB-AB)$.

<small>

* concepts:triangle
* questionType:Prove

</small>






# <lo-sample/> LV.AMO.2018.7.4

Atrast tādu veselu skaitli $n$, lai vienādība

$$(n - 2021)(n - 2018)(n - 2017)(n - 2016) = 2016$$

būtu patiesa!

<small>

* questionType:FindAll

</small>





# <lo-sample/> LV.AMO.2018.8.2

Naturālu skaitļu virknes $1; 8; 8; 64; 192; 432; \ldots$ 
katrs loceklis, sākot ar trešo, ir vienāds ar divu iepriekšējo 
locekļu nenulles ciparu reizinājumu. Kāds ir šīs
virknes 2018. loceklis?

<small>

* questionType:FindAll
* concepts:sequence,product

</small>




# <lo-sample/> LV.AMO.2018.9.4

Atrast lielāko naturālo skaitli, kas dalās ar $7$, kura ciparu summa ir $100$ un
kuram neviens cipars nav $0$.

<small>

* concepts:divisibility,sum
* questionType:FindOptimal

</small>



# <lo-sample/> LV.AMO.2018.10.4

Pierādīt, ja $x$ - naturāls skaitlis, tad
$x^8 - x^2$ dalās ar $252$.

<small>

* topic:DivisibilityRulesFor3And9
* topic:DivisibilityProperties
* topic:ModularArithmetic
* topic:PolynomialDifferenceDivisibility
* questionType:Prove
* concepts:divisibility

</small>


## Atrisinājums

Pārbaudām dalāmību ar 252 reizinātājiem.

**Apgalvojums:** Lai naturāls skaitlis $N$ dalītos ar $252=2^2\cdot{}3^2\cdot{}7^1$
ir nepieciešami un pietiekami, lai $N$ dalītos ar pirmreizinātāju 
augstākajām pakāpēm: $2^2 = 4$, $3^2 = 9$ un $7^1 = 7$. 

* $x^8 - x^2$ dalās ar $4$:
    - Ja $x$ ir pāru skaitlis, tad $x^2$ dalās ar $4$. 
    - Ja $x$ ir nepāru skaitlis, tad $(x^4-x)(x^4+x)$ ir divu pāru skaitļu reizinājums. Tātad arī dalās ar $4$.
* $x^8 - x^2$ dalās ar $9$:  
    - Ja $x$ dalās ar $3$, tad $x^2$ dalās ar $9$.
    - Ja $x = 3k+1$, tad $x^3 - 1 = (3k+1)^3 - 1$ dalās ar $9$ (pārbauda, atverot iekavas)
    - Ja $x = 3k-1$, tad $x^3 + 1 = (3k-1)^3 + 1$ dalās ar $9$ (pārbauda, atverot iekavas)

Pamatosim, ka $x^8 - x^2 = x^2(x^6-1)$ dalās arī ar $7$.

* Ja $x$ dalās ar $7$, tad $x^2$ dalās ar $7$. 
* Ja $x$ nedalās ar $7$, varam izmantot Mazo Fermā teorēmu pie $p=7$. 

**Mazā Fermā teorēma:** Ja $p$ ir pirmskaitlis un $a$ nedalās ar $p$, tad
$a^{p-1}$ dod atlikumu $1$, dalot ar $p$. 

Citiem vārdiem, $a^{p-1}-1$ dalās ar $p$.  
Ievietojot $p-7$, iegūstam, ka 
$a^6 - 1$ dalās ar $7$, ja vien $a$ nedalās ar $7$.

**Empīriska teorēmas pārbaude, ja p=7**

Mazo Fermā teorēmu atcerēties ir derīgi, bet var pamatot citādi.

Pārbaudīsim, ka $x^6$ dod atlikumu $1$, dalot ar $7$ 
visiem $x=1,2,3,4,5,6$. (Lielākām $x$ vērtībām $x$ var aizstāt
ar tā atlikumu, polinoma $x^6$ vērtības atlikums no tā nemainīsies). 

| $x$           | $1$   | $2$   | $3$           | $4$   | $5$           | $6$          |
| ------------- | ----- | ----- | ------------- | ----- | ------------- | ------------ |
| $x^3          | $1$   | $8$   | $27$          | $64$  | $125$         | $216$        | 
| $x^3 \pmod 7$ | $1$   | $1$   | $6$           | $1$   | $6$           | $6$          |
| $x^6 \pmod 7$ | $1$   | $1$   | $36 \equiv 1$ | $1$   | $36 \equiv 1$ | 36 \equiv 1$ |


**Apgalvojums:** Ja $P(x)$ ir polinoms ar veseliem koeficientiem, 
ja $x_1, x_2, m$ ir naturāli skaitļi, pie tam $x_1$ un $x_2$ dod vienādus 
atlikumus, dalot ar $m$ , tad 
arī polinomu vērtības $P(x_1)$ un $P(x_2)$ dod vienādus atlikumus, dalot ar $m$. 

**Definīcija:** Apgalvojumu, ka $x_1$ un $x_2$ dod vienādus atlikumus, dalot ar $m$ pieraksta šādi:
$x_1 \equiv x_2\;(\mbox{mod}\,m)$. To lasa: $x_1$ un $x_2$ ir *kongruenti* pēc moduļa $m$. 

Šajos apzīmējumos katram polinomam $P(x)$ var secināt:

$$ x_1 \equiv x_2\;(\mbox{mod}\,m)\;\;\Rightarrow\;\;P(x_1) \equiv P(x_2)\;(\mbox{mod}\,m)$$





# <lo-sample/> LV.AMO.2018.11.1

Pierādīt, ka visām naturālām $n$ vērtībām izpildās

$$1^3 + 2^3 + 3^3 + \ldots + n^3 = (1 + 2 + 3 + \ldots + n)^2.$$

<small>

* questionType:Prove

</small>




# <lo-sample/> LV.AMO.2018.11.4

Vai eksistē tādi naturāli skaitļi $m$ un $n$, ka $m^2 - n^2 = 2mn$?

<small>

* questionType:ProveDisprove

</small>



# <lo-sample/> LV.AMO.2018.12.4

Naturāls skaitlis $B$ ir iegūts no naturāla skaitļa $A$, samainot vietām tā ciparus.
Zināms, ka $A + B = 10^{45}$. Pierādīt, ka gan $A$, gan $B$ dalās ar $5$.

<small>

* concepts:divisibility
* questionType:Prove

</small>





# <lo-sample/> LV.AMO.2019.7.5

Kādai mazākajai naturālai $n$ vērtībai skaitli $10^n$
iespējams izteikt kā septiņu
naturālu skaitļu reizinājumu tā, lai to visu pēdējie cipari ir dažādi (tas ir,
nevienam no tiem pēdējais cipars nesakrīt ar kāda cita skaitļa pēdējo ciparu)?


<small>

* questionType:FindOptimal
* concepts:product

</small>




# <lo-sample/> LV.AMO.2019.8.5

Kādai mazākajai naturālai $n$ vērtībai skaitli $10^n$
iespējams izteikt kā sešu
naturālu skaitļu reizinājumu tā, ka neviens 
no tiem nav mazāks kā $10$ un to
visu pēdējie cipari ir dažādi (tas ir, 
nevienam no tiem pēdējais cipars nesakrīt
ar kāda cita skaitļa pēdējo ciparu)?

<small>

* questionType:FindOptimal
* concepts:product

</small>





# <lo-sample/> LV.AMO.2019.9.4

Ja naturāla sešciparu skaitļa visus nepāra ciparus aizvietotu ar $7$, iegūtu skaitli,
kas ir par $5998$ lielāks nekā sākotnējais skaitlis. Savukārt, ja sākotnējā skaitlī
ar $7$ aizvietotu visus pāra ciparus, tad iegūtais skaitlis būtu par $500290$ lielāks
nekā sākotnējais. Atrast doto sešciparu skaitli!

<small>

* questionType:FindAll

</small>




# <lo-sample/> LV.AMO.2019.9.5


Vai eksistē tāds kvadrātvienādojums ar veseliem koeficientiem, 
kuram ir sakne

$$\left( \sqrt{2020} − 2\sqrt{2019} + \sqrt{2018} \right)
\left( \sqrt{2020} + \sqrt{2019} \right) \times$$

$$\times \left( \sqrt{2019} + \sqrt{2018} \right)
\left( \sqrt{2020} + \sqrt{2018} \right)?$$

<small>

* concepts:quadratic-equation
* questionType:ProveDisprove

</small>



# <lo-sample/> LV.AMO.2019.10.1

Pierādīt, ka visām naturālām $n$ vērtībām ir spēkā vienādība

$$6 + 24 + 60 + \cdots + n(n + 1)(n + 2) =$$

$$=\frac{n(n+1)(n+2)(n+3)}{4}.$$

<small>

* topic:NumTheoryMathInduction
* questionType:Prove
* concepts:equation

</small>



# <lo-sample/> LV.AMO.2019.10.4

Kādām naturālām $n$ vērtībām izteiksme 
$n^2 + n + 19$ ir kāda naturāla skaitļa kvadrāts?

<small>

* topic:StandardIdentities
* questionType:FindAll
* concepts:square-Alg

</small>



    
# <lo-sample/> LV.AMO.2019.11.1

Atrisināt nevienādību 

$$\frac{(x-20)^{19} \cdot (x + 4)}{\left( \sqrt{x^2 + 4} \right) \left( 9-x^2 \right)} \geq 0.$$

<small>

* concepts:inequality
* questionType:FindAll

</small>



# <lo-sample/> LV.AMO.2019.11.2

Divi spēlētāji pamīšus raksta uz tāfeles skaitļa $216$ 
naturālos dalītājus. Katrā gājienā jāievēro šādi noteikumi:

* nedrīkst atkārtoti rakstīt jau uzrakstītu dalītāju;
* nedrīkst rakstīt dalītāju, kurš ir tieši $2$ vai $3$ reizes lielāks vai mazāks nekā
  kāds jau uzrakstītais dalītājs.

Zaudē tas spēlētājs, kurš nevar izdarīt gājienu. Kurš spēlētājs – pirmais vai
otrais – vienmēr var uzvarēt?

<small>

* topic:FactorizationAndDivisibility
* topic:GameInvariant
* seeAlso:LV.AMO.2019.12.2
* concepts:divisors
* questionType:ProveDisprove

</small>



    
# <lo-sample/> LV.AMO.2019.11.3

Uz trijstūra $ABC$ malām $AB$ un $BC$ izvēlēti attiecīgi tādi punkti $D$ un $E$, ka
$AC \parallel DE$. Nogriežņi $AE$ un $CD$ krustojas punktā $F$. Punkti $B$, $D$, $E$ un $F$
atrodas uz vienas riņķa līnijas. Taisne $BF$ krusto malu $AC$ punktā $H$ un
trijstūrim $ABC$ apvilkto riņķa līniju punktā $G$. Pierādīt, ka $FH = GH$.

<small>

* concepts:triangle,circumscribed-circle
* questionType:Prove

</small>



# <lo-sample/> LV.AMO.2019.11.4

Zināms, ka vairāku naturālu skaitļu summa ir **(A)** $2019$, **(B)** $2020$.   
Kāds ir lielākais iespējamais šo skaitļu reizinājums? 


<small>

* topic:InequalityProvingStronger
* concepts:product
* questionType:FindOptimal,FindOptimal

</small>





# <lo-sample/> LV.AMO.2019.12.2

Divi spēlētāji pamīšus raksta uz tāfeles skaitļa $144$ 
naturālos dalītājus. Katrā gājienā jāievēro šādi noteikumi:

* nedrīkst atkārtoti rakstīt jau uzrakstītu dalītāju;
* nedrīkst rakstīt dalītāju, kurš ir tieši $2$ vai $3$ reizes lielāks vai mazāks nekā
  kāds jau uzrakstītais dalītājs.

Zaudē tas spēlētājs, kurš nevar izdarīt gājienu. Kurš spēlētājs – pirmais vai
otrais – vienmēr var uzvarēt?

<small>

* seeAlso:LV.AMO.2019.11.2
* concepts:divisors
* questionType:ProveDisprove

</small>



## Atrisinājums

* Visi dalītāji veido taisnstūrainu struktūru, kur reizināšana ar $2$
ir virzīšanās pa vienu asi, bet reizināšana ar $3$ - pa otru. 
* Šajā tainstūrī ir simetrijas centrs: $12 = \sqrt{144}$. 
* Pirmais spēlētājs sāk ar $12$, pēc tam uz katru dalītāju $d$ 
atbild ar $144/d$.



    
# <lo-sample/> LV.AMO.2019.12.3

Dots četrstūris $ABCD$, kuram $AB = AD$ un $BC = CD$. Riņķa līnija, kas iet caur
punktiem $A$, $B$ un $C$, krusto nogriežņus $AD$ un $CD$ attiecīgi to iekšējos punktos
$E$ un $F$ un nogriezni $BD$ punktā $G$. Pierādīt, ka $EG = FG$. 

<small>

* concepts:rectangle
* questionType:Prove

</small>





# <lo-sample/> LV.AMO.2019.12.4

Sporta nometnē ir $100$ skolēni. Ar $N$ apzīmējam, cik veidos šos $100$ skolēnus
var sadalīt $50$ pāros (pāru secība un arī skolēnu secība pārī nav svarīga). Ar
kādu lielāko trijnieka pakāpi dalās $N$?


<small>

* topic:RuleOfProduct
* topic:ValuationProperties
* questionType:FindAll

</small>



## Atrisinājums

Aprēķinām $N$, izmantojot reizināšanas likumu. 
Visjaunākajam (visīsākajam u.c.) skolēnam pāri var atrast $99$ veidos.
No atlikušajiem visjaunākajam skolēnam pāri var atrast $97$ veidos.
Pēdējam skolēnam paliek tieši $1$ pāris.
Pilnu variantu skaitu izsaka reizinājums:  

$$N = 99\cdot{}97\cdot{}95\cdot\ldots\cdot{}3\cdot{}1.$$

Grupējam reizinātājus atkarībā no trijnieka pakāpes, ar
kuru tie dalās.

* $(99-3)/6 + 1 = 17$ reizinātāji dalās ar $3$:
  $3 \cdot 9 \cdot 15 \cdot 21 \cdot 27 \cdot \ldots \cdot 99$.
* $(99-9)/18 + 1 = 6$ reizinātāji dalās ar $3^2$: 
  $9 \cdot 27 \cdot 45 \cdot 63 \cdot 81 \cdot 99$
* $(81 - 27)/54 +1 = 2$ reizinātāji dalās ar $3^3$ ($27, 81$). 
* Viens reizinātājs dalās ar $3^4$ ($81$).

Saskaitot šīs pakāpes $17 + 6 + 2 + 1 = 26$. 

*Piezīme.* Līdzīga saskaitīšanas ideja ir arī Ležandra formulā, kas 
atrod lielāko pirmskaitļa pakāpi, ar ko dalās $n!$. 




# <lo-sample/> LV.AMO.2019.12.5

Miljonāru kluba visbagātākajam biedram ir tieši $8$ reizes mazāk naudas nekā
visiem pārējiem biedriem kopā, ceturtajam bagātākajam biedram ir tieši $11$
reizes mazāk naudas nekā visiem pārējiem biedriem kopā, bet
visnabagākajam biedram ir tieši $13$ reizes mazāk naudas nekā visiem pārējiem
biedriem kopā. Cik biedru ir šajā klubā?

<small>

* questionType:FindCount

</small>


    