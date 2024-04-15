# <lo-sample/> LV.NOL.2000.7.4 

Naturālu skaitli sauc par interesantu, ja tā ciparu summa dalās ar $5$. 

**(a)** atrast kaut vienu tādu interesantu $x$, ka arī $x+9$ ir interesants,   
**(b)** cik pavisam ir tādu interesantu $x$, kādi minēti **(a)** punktā?  
**(c)** pierādīt: starp jebkuriem $9$ pēc kārtas ņemtiem naturāliem skaitļiem ir 
vismaz viens interesants.


<small>

* [nota.divrule.3_9.rem](#)
* [seq.gaps](#)
* [seq.arithm.mod](#)

</small>

<!--
genre=special-numbers
questionType=Find.Any,Find.Count,Prove.ForAll
-->



## Atlikumi, dalot ar 9 

**(a)** un **(b)**
$x$ un $x+9$ ciparu summas mēdz atšķirties par
$9$ daudzkārtni, tie var atšķirties par $0$ vai $45$, utt. 

* Par $0$ atšķiras, piemēram, $5$ un $14$ ciparu summas. 
* Par $45$ atšķiras, piemēram, $1999999$ un $2000008$ ciparu summas. 



## Gadījumu pārlase

**(c)** Skaitļu ciparu summas veido virknes, kas deviņus soļus aug pa $1$ (vienu 
ciparam pieaugot no $0$ līdz $9$), 
pēc tam vienu soli par kaut kādu daudzumu sadilst (vienu cipars no $9$ pēkšņi 
pārvēršas par $0$). Virknīte garumā $9$ (neatkarīgi no tā, kurā brīdī 
vienu cipars pārlec uz $0$), saturēs augošu gabalu garumā $5$.



# <lo-sample/> LV.NOL.2000.7.5 

Uz tāfeles uzrakstīti skaitļi $\frac{3}{2}$; $\frac{4}{5}$; $\frac{5}{3}$. 
Ar vienu gājienu atļauts izvēlēties divus no uzrakstītajiem skaitļiem 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt 
uz tāfeles skaitļus $\frac{b^2}{a}$ un $\frac{a^2}{b}$. Vai, izdarot vairākus 
šādus gājienus pēc kārtas, var panākt, lai uz tāfeles vienlaicīgi 
atrastos skaitļi $\frac{4}{3}$; $\frac{4}{5}$; $\frac{5}{2}$? 

<small>

* [misc.invar.expr](#)

</small>

<!--
genre=making-moves
questionType=ProveDisprove.Exists
seeAlso=LV.NOL.2019.8.4
-->



## Invariants
 
Trīs skaitļu reizinājums nemainās. Tomēr šajā piemērā reizinājumiem 
sākumā un beigās jāatšķiras. Pretruna.

$$\frac{3}{2}\cdot\frac{4}{5}\cdot\frac{5}{3} = \frac{2}{1}$$
$$\frac{4}{3}\cdot\frac{4}{5}\cdot\frac{5}{2} = \frac{8}{3}$$



# <lo-sample/> LV.NOL.2000.8.5 

Tabula sastāv no $n \times n$ rūtiņām. Katrā rūtiņā jāieraksta
$0$, $1$ vai $2$ tā, lai, aprēķinot rindiņās un kolonnās 
ierakstīto skaitļu summas, iegūtu visus naturālos skaitļus no $1$ līdz $2n$, 
katru vienu reizi. Vai to var izdarīt, ja  
**(a)** $n = 5$, **(b)** $n=6$? 

<small>

* [misc.invar.expr](#)
* [alg.series.sum](#)
* [misc.try](#)

</small>

<!--
genre=magic-configuration
questionType=ProveDisprove.Exists
-->



## Neiespējamība

$n=5$ nevar, jo $1+2+\ldots+10=55$ ir nepāru skaitlis, bet 
tam jābūt pāru (summas pa rindiņām un kolonnām sakrīt).



## Piemēra konstruēšana

$n=6$ var ($1,2,3,10,11,12$ pa vertikāli).

<table>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>2</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td><td>2</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td></tr>
</table>



# <lo-sample/> LV.NOL.2000.9.2 

Kvadrāts sastāv no $3 \times 3$ rūtiņām. Tajās ieraksta veselus skaitļus no $1$ līdz $9$ (katrā rūtiņā -
citu skaitli). Pēc tam katrām divām rūtiņām, kurām ir kopīga mala, aprēķina tajās ierakstīto
skaitļu summu (pavisam būs $12$ summas). Kādu mazāko skaitu dažādu vērtību var iegūt?

<small>

* [misc.extr](#)

</small>

<!--
genre=fill-in-table
questionType=Find.Min
-->



## Piemēra konstrukcija

Mazāk kā $4$ vērtības nevar, jo skaitli vidū saskaita ar $4$ dažādiem skaitļiem. 
Četras var: $((3,8,1),(4,5,6),(9,2,7))$. 

<table>
<tr><td>3</td><td>8</td><td>1</td></tr>
<tr><td>4</td><td>5</td><td>6</td></tr>
<tr><td>9</td><td>2</td><td>7</td></tr>
</table>



# <lo-sample/> LV.NOL.2000.9.4 

Uz $5$ kartītēm uzrakstīts pa naturālam skaitlim (starp tiem var būt arī vienādi). Uz katrām
trim kartītēm uzrakstīto skaitļu summa dalās ar to skaitļu summu, kas uzrakstīti uz abām
pārējām kartītēm.

1. atrodiet kaut vienu piemēru, kur šis nosacījums izpildās,
2. vai tas var izpildīties, ja uz visām kartītēm uzrakstīti dažādi skaitļi?

<small>

* [alg.expr](#)

</small>

<!--
questionType=Find.Any,ProveDisprove.Exists
-->



## Gadījumu šķirošana

* Ja visi $5$ skaitļi vienādi ar $a$, tad nevar gadīties, ka $3a$ dalās ar $2a$. 
* Ja četri skaitļi vienādi un viens atšķiras, var izvēlēties komplektu $(1,1,1,1,2)$. 






# <lo-sample/> LV.NOL.2000.10.1 

Dots, ka $A$ un $B$ ir trīsciparu naturāli skaitļi, 
pie tam $A$ simtu cipars sakrīt ar $A$ vienu
ciparu. Zināms arī, ka $A-B=297$ un $B$ ciparu summa ir $23$. Atrast $A$ un $B$.


<!--
concepts=sum-of-digits
questionType=Find.All
-->



# <lo-sample/> LV.NOL.2000.10.2 

Kvadrāts sastāv no $3 \times 3$ rūtiņām. 
Katrā rūtiņā jāieraksta pa naturālam skaitlim, kas
nepārsniedz n (visiem skaitļiem jābūt dažādiem) tā, lai 
no katriem diviem skaitļiem, kas
ierakstīti rūtiņās ar kopīgu malu, viens dalītos ar otru.  
Vai to var izdarīt, ja (a) $n=15$, (b) $n=13$?

<!--
genre=fill-in-table
questionType=ProveDisprove.Exists
-->





# <lo-sample/> LV.NOL.2000.10.5 

No pirmajiem $20$ naturālajiem skaitļiem izvēlēti 
$10$ skaitļi tā, ka to summa ir $105$, bet
nekādu divu izvēlēto skaitļu summa nav $21$. 
Aprēķināt visu izvēlēto skaitļu kvadrātu
summu.

<!--
questionType=Find.All
-->



## ABC

**#MasuCentrs** No katra pāra $(n,21-n)$ ņemts tieši viens. 



# <lo-sample/> LV.NOL.2000.11.1 

Ar $\lfloor a \rfloor$ apzīmējam lielāko veselo skaitli, kas nepārsniedz $a$. 
Piemēram, $\lfloor 4.8 \rfloor=4$; $\lfloor 5 \rfloor=5$.
Atrisināt pozitīvos skaitļos vienādojumu
$$ x \left\lfloor x \left\lfloor x \right\rfloor \right\rfloor = 41. $$


<!--
seeAlso=LV.NOL.2001.11.1
questionType=Find.All
-->



## ABC

**#Nevienādība** **#GadījumuPārlase** $x \in [3;4)$. Tad $x \lfloor 3x \rfloor = 41$. Trīs gadījumi: $x \cdot 9 = 41$, $x \cdot 10 = 41$, $x \cdot 11 = 41$. Vienīgi $x = 41/11$ der.



# <lo-sample/> LV.NOL.2000.11.4 

Naturāls skaitlis $n$, kas nedalās ar $4$, vienāds ar savu četru mazāko naturālo dalītāju
kvadrātu summu.

1. pierādīt, ka $n$ noteikti ir pāra skaitlis,
2. atrast vienu tādu skaitli $n$,
3. pierādīt, ka citu tādu $n$ nav.

<!--
questionType=Prove.ForAll,Find.Any,Prove.NotExists
-->



## ABC

**#Paritāte** **#Polinomi** Četru nepāru summa nav nepāru. $N = 1^2 + 2^2 + p^2 + (2p)^2 = 5(p^2+1)$, t.i. mazākais nepāru $p\,\mid\,N$ ir $5$, un $5(5^2+1) = 130$. 



# <lo-sample/> LV.NOL.2000.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir 1, bet katrs nākošais vienāds ar abu
iepriekšējo summu. Vai ar $5$ dalās šīs virknes
(a) $21$-ais, (b) $2000$-ais loceklis?

<!--
seeAlso=LV.NOL.2001.12.1
seeAlso=LV.NOL.2003.12.1
seeAlso=LV.NOL.2004.12.1
questionType=Find.Only
-->



## ABC

**#Kongruences** **#PeriodiskaVirkne**  Pirmie $20$ atlikumi: $1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0$, tālāk periods. $F_{21}$ dos atlikumu $1$, bet $F_{2000}$ dalīsies ar $5$. 







# <lo-sample/> LV.NOL.2001.7.1 

Divos pēc kārtas sekojošos gados katrā ir $365$ dienas. 
Pirmajā no tiem sestdienu ir vairāk nekā trešdienu. 
Kuru nedēļas dienu otrajā gadā ir visvairāk? 

<small>

* [mod.congr](#)
* [seq.arithm.numestimate](#)

</small>

<!--
questionType=Find.All
-->



## 365:7 - dalīšana ar atlikumu
 
$365$ dienu gads sākas un beidzas ar to pašu dienu. 
1.gads sākas/beidzas ar sestdienu (visu citu dienu ir vienāds skaits). 
Bet nākamais sākas un beidzas ar svētdienu.



# <lo-sample/> LV.NOL.2001.7.4 

Virknē uzrakstīti cipari no $1$ līdz $9$ (skat. zīmējumu):
$$1\;\;2\;\;3\;\;4\;\;5\;\;6\;\;7\;\;8\;\;9$$
Kādu lielāko daudzumu semikolu var ievietot starp blakus esošiem 
cipariem, lai tie sadalītu ciparu virkni tādu naturālu skaitļu pierakstos, 
no kuriem katriem diviem lielākais kopīgais dalītājs ir $1$? 
(Piemēram, $123;45678;9$ neder, jo $123$ un $9$ abi dalās ar $3$.)

<small>

* [misc.extr.pigeon](#)
* [comb.full](#)

</small>

<!--
concepts=coprimes
questionType=Find.Max
-->



## ABC
 
**#DirihlēPrincips** **#LKD** Ja ir $6$ semikoli, aiz 2 pāru cipariem beigtos skaitlis. Ar pieciem: $1;23;4;5;67;89$.




# <lo-sample/> LV.NOL.2001.8.3 

Uzrakstiet kaut vienu desmitciparu skaitli, kam visi 
cipari ir dažādi un kam piemīt īpašība: izsvītrojot jebkurus $n$ ciparus
($n$ – jebkurš naturāls skaitlis, kas nepārsniedz $6$), 
atlikušie cipari (tai pašā secībā) veido saliktu skaitli. 
Pamatojiet savu risinājumu. 

<small>

* [nota.divrule.2_5_10.divides](#)
* [comb.full](#)

</small>


<!--
concepts=primes,composite-numbers
genre=digit-manipulation
questionType=Find.Max
-->



## Dalāmība ar 2 un 5

* Ja skaitļa beigās pāru cipari un $5$, tad tie visi jāizsvītro. 
* Pārkārtojot $(1,3,7,9)$ dažādā secībā, meklējam saliktu skaitli. 
* $1379$ dalās ar $7$. Tātad $1379502468$ der. 



# <lo-sample/> LV.NOL.2001.9.1 

Dots, $n$ – naturāls skaitlis. 
Pierādiet, ka vismaz viens no skaitļiem  $n^3 - n$
un $n^3 + n$
dalās ar $10$.

<!--
questionType=Prove.Exists
-->



## ABC

**#GadījumuPārlase** **#Kongruences** $0^3+0$, $1^3-1$, $2^3+2$, $3^3+3$, 
$4^3-4$, $5^5-5$, $6^6 - 6$, $7^3 + 7$, $8^3 + 8$, $9^9-9$.  




# <lo-sample/> LV.NOL.2001.9.5 

Plakne sadalīta kvadrātiņos kā rūtiņu lapa; 
rūtiņas malas garums ir $1$.
Uzzīmēta slēgta lauzta līnija, kuras visi posmi iet pa 
rūtiņu malām, un katra
posma garums ir nepāra skaitlis. 
Vai šai līnijai var būt tieši  
(a) $2000$, (b) $2001$, (c) $2002$ posmi?


<!--
questionType=ProveDisprove.Exists
-->



## ABC

**#Invariants** Ar $2000$ var (saliek kopā 2 "trepes"). $2001$ nevar, 
jo mijas horizontāli un vertikāli posmi. $2002$ nevar, 
jo $1001$ nepāra (horizontālo) pārvietojumu summa nevar būt $0$.   



# <lo-sample/> LV.NOL.2001.10.1 

Dots, ka $A$ un $B$ ir trīsciparu naturāli skaitļi, 
pie tam $A$ simtu cipars sakrīt
ar $B$ vienu ciparu, bet $B$ simtu cipars sakrīt ar 
$A$ vienu ciparu. Zināms arī, ka
$A - B = 297$ un $B$ ciparu summa ir $23$. Atrast $A$ un $B$.


<!--
concepts=sum-of-digits
questionType=ProveDisprove.Exists
-->



# <lo-sample/> LV.NOL.2001.10.4 

Izsacīt izteiksmes 
$$\sqrt{1 + \frac{1}{1^2} + \frac{1}{2^2}}
+ \sqrt{1 + \frac{1}{2^2} + \frac{1}{3^2}} +$$
$$+ \sqrt{1 + \frac{1}{3^2} + \frac{1}{4^2}}
+ \cdots + \sqrt{1 + \frac{1}{9^2} + \frac{1}{10^2}}$$
vērtību kā galīgu decimāldaļskaitli. 

<!--
concepts=square-root,decimal-fractions
questionType=Find.Only
-->




# <lo-sample/> LV.NOL.2001.11.3 

Kādiem naturāliem $k$ skaitlis $k^k + 1$ ir pirmskaitlis, kas mazāks par
$10^{19}$. 


<!--
questionType=Find.All
concepts=primes
seeAlso=LV.NOL.2002.11.1
-->



## ABC

**#Nevienādība** **#AlgebriskaIdentitāte** Ja $k >1$ ir nepāra dalītājs, tad dalās reizinātājos kā $a^{2n+1}+b^{2n+1}$. Arī $8^8+1 = (2^8)^3 + 1^3$ dalās reizinātājos, bet $16^{16}+1>10^{19}$. Tāpēc $k=1,2,4$.




# <lo-sample/> LV.NOL.2001.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir 1, bet katrs nākošais
vienāds ar abu iepriekšējo summu. Vai ar 5 dalās šīs virknes

1. $21$-ais,
2. $2000$-ais loceklis? 


<!--
questionType=Find.Only
concepts=fibonacci-sequence
-->








# <lo-sample/> LV.NOL.2002.7.3 


Uz tāfeles uzrakstīti naturālie skaitļi no $3$ līdz $10$ ieskaitot, 
katrs vienu reizi. 
Ar vienu gājienu atļauts diviem uz tāfeles esošiem 
skaitļiem vienlaicīgi pieskaitīt pa vieniniekam. 
Kāds lielākais dažādu pirmskaitļu daudzums var vienlaikus atrasties uz tāfeles?


<small>

* [div.prop.primes.small](#)
* [misc.invar.parity](#)

</small>

<!--
genre=optimization
questionType=Find.Max
-->



## ABC
 
**#Invariants** **#Konstrukcija** $8$ nepāru pirmskaitļu summa var būt $52+2k$; visi var būt pirmskaitļi. 




# <lo-sample/> LV.NOL.2002.8.3 

Burtnīcā ir $100$ lapas; tās lappuses sanumurētas dabīgā kārtībā ar numuriem 
no $1$ līdz $200$. Vai izrauto lappušu numuru summa var būt $1000$, ja tiek izrautas  
**(a)** $31$ lapa;   
**(b)** $30$ lapas?   
*Piezīme.* Lapas var neraut pēc kārtas.

<small>

* [misc.invar.parity](#)
* [misc.invar.congr](#)
* [alg.ineq.monotonicity](#)
* [seq.arithm.summation](#)


</small>

<!--
concepts=arithmetic-progression
questionType=ProveDisprove.Exists
-->



## Paritāte
 
**(a)** summa būtu nepāru. 
**(b)** trīsdesmit $4k_i-1$ summa nedalītos ar $4$.

Var pamatot arī ar nevienādību:  
Jau $1+\ldots+60 > 1000$, tādēļ pat vismazāko lapu numuru summa ir par lielu.



# <lo-sample/> LV.NOL.2002.9.1 

Jānis uzrakstīja $n$ pēc kārtas sekojošus naturālus skaitļus.
Neviens no tiem nedalās ar diviem vai vairāk dažādiem 
pirmskaitļiem. Kāda ir
lielākā iespējamā $n$ vērtība?

<!--
concepts=primes
questionType=Find.Max
-->



## ABC

**#Dalāmība** Tādi ir $1,2,3,4,5$. Vairāk kā $n=5$ nevar būt, jo katram sestajam ($6$ dalītājiem) ir divi pirmskaitļu dalītāji.



# <lo-sample/> LV.NOL.2002.9.4 

Ar $p(n)$ apzīmēsim naturāla skaitļa n ciparu reizinājumu. 
Piemēram,
$p(26)=12$; $p(8)=8$; $p(102)=0$.
Aprēķināt summu $p(1)+p(2)+p(3)+\ldots +p(2001)+p(2002)$.



## ABC

**#AlgebrisksPārveidojums** Trīsciparu skaitļiem $p(n)$ summa būs $(1+2+\ldots+9)^3$ (pārbauda, atverot iekavas). Visiem prasītajiem: $45+45^2+2\cdot 45^3 = 184320$. 




# <lo-sample/> LV.NOL.2002.10.3 

Naturālu skaitļu $m$ un $n$ lielākais kopīgais dalītājs 
ir $d$, bet mazākais
kopīgais dalāmais ir $D$. Pierādiet: 
$2m+n=2D+d$ tad un tikai tad, ja $m$ dalās ar $n$.



## ABC

**#MKD** **#LKD**  **#AlgebriskaNevienādība** Ja $m$ dalās ar $n$, tad $D=m$, $d=n$ un $2m+n=2D+d$. 
Reizinājums $Dd=mn$ ir fiksēts; $2D+d = 2D+mn/D$ monotoni aug, ja $D \geq \sqrt{mn/2}$.




# <lo-sample/> LV.NOL.2002.10.5 

Dotas $2002$ konfekšu kastes. Katrā kastē ir 
vismaz viena konfekte, un
nekādās divās kastēs konfekšu daudzumi nav vienādi. 
Nevienā kastē nav vairāk par $2002$ konfektēm. 
Ar vienu gājienu atļauts no dažām
kastēm apēst vienādu skaitu konfekšu 
(drīkst arī ēst konfektes tikai no
vienas kastes).  
Kāds ir mazākais gājienu skaits, ar kuru var apēst visas konfektes?




## ABC

**#Binārais pieraksts** Katru no $2002$ skaitļiem var pierakstīt ar $11$ binārā pieraksta cipariem. 
$2002_{10}=11111010010_{2}$. Katrā gājienā noēd bināro ciparu, kur tas ir.
Ja ēd $10$ dienas, tad var noēst tikai $2^{10}$ dažādus skaitļus.



# <lo-sample/> LV.NOL.2002.11.2 

Andris izvēlējās 5 dažādus naturālus skaitļus un katriem diviem
izvēlētajiem skaitļiem aprēķināja to summu. Kādu mazāko daudzumu
dažādu rezultātu Andris varēja iegūt?

<!--
seeAlso=LV.NOL.2003.11.1  
seeAlso=LV.NOL.2004.11.1  
questionType=Find.Min
-->



# <lo-sample/> LV.NOL.2002.12.1 

Dots, ka $\sin x$ - racionāls skaitlis. Vai $\sin 2x$ var būt  
(a) racionāls, (b) iracionāls, (c) nedefinēts?

<!--
concepts=irrational-numbers,rational-numbers
questionType=ProveDisprove.Exists
-->



## ABC

**#PitagoraTrijnieki** **#IracionalitātesPierādījumi** Racionāls: $\sin x = 4/5$; $\sin 2x = 2 \sin x \cos x = 2 \cdot \frac{4}{5} \cdot \frac{3}{4} = \frac{24}{25}$. Iracionāls: $\sin (\pi / 3) = \frac{\sqrt{3}}{2}$. Sinuss definēts visiem $x \in \mathbb{R}$.






# <lo-sample/> LV.NOL.2003.7.4/LV.NOL.2005.7.1 


Kādu mazāko daudzumu no skaitļiem   
$1;2;3;\ldots;12;13$ var izsvītrot, lai 
katru divu atlikušo summa būtu salikts skaitlis? 

<small>

* [comb.graph.bipartite](#)
* [mod.fix.parity](#)

</small>

<!--
questionType=Find.Min
concepts=primes,composite-numbers
-->



## ABC
 
**#DirihlēPrincips** **#Paritāte** **#Pirmskaitļi** Var svītrot $6$ pāru skaitļus. Mazāk nevar, jo jāizjauc $6$ pāri $(1;12)$ utt.




# <lo-sample/> LV.NOL.2003.8.3 

Kādu mazāko daudzumu no naturāliem skaitļiem $1;2;3;\ldots;12$ var izsvītrot, 
lai atlikušos varētu sadalīt divās grupās ar īpašību: 
vienas grupas visu skaitļu reizinājums vienāds ar otras grupas visu skaitļu reizinājumu. 

<small>

* [div.fta](#)

</small>


<!--
questionType=Find.Min
-->



## ABC
 
**#EiklīdaLemma** Jāsvītro $7, 11$ un viens $3$ daudzkārtnis. $1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 8 \cdot 9 \cdot 10$.




# <lo-sample/> LV.NOL.2003.9.1 

Jānis uzrakstīja $n$ pēc kārtas sekojošus naturālus skaitļus. 
Neviens no tiem nedalās ar trim vai vairāk dažādiem 
pirmskaitļiem. Kāda ir lielākā iespējamā $n$ vērtība?

<!--
concepts=primes
questionType=Find.Max
-->



## ABC

**#Dalāmība** Tādi ir $1,2,\ldots,29$. Vairāk kā $n=29$ nevar būt, jo katram trīsdesmitajam ($30$ dalītājiem) ir trīs pirmskaitļu dalītāji.





# <lo-sample/> LV.NOL.2003.9.5 

Uz galda atrodas $n$ konfektes. Andris un Pēteris pēc kārtas 
izdara gājienus; pirmais iet Andris. 
Ar vienu gājienu tiek paņemtas dažas
konfektes; pie tam jāņem vismaz $1$ konfekte, 
bet nedrīkst ņemt vairāk
par pusi uz galda esošo konfekšu. 
Tas zēns, pēc kura gājiena uz galda
paliek 1 konfekte, zaudē.
Kas uzvar, pareizi spēlējot, ja  
(a) $n = 47$,  
(b) $n = 2003$?

<!--
questionType=Algorithm,Prove.ForAll
-->



# <lo-sample/> LV.NOL.2003.10.1 

Dots, ka $x$ un $y$ – naturāli skaitļi. Vai var gadīties, ka

1. $(2x+3y)(3x+2y)$ dalās ar $5$, bet nedalās ar $25$?
2. $(2x+3y)(3x+2y)$ dalās ar $2003$, bet nedalās ar $2003^2$?

<!--
questionType=ProveDisprove.Exists
-->



# <lo-sample/> LV.NOL.2003.11.4 

Ir zināms, ka skaitlis $38$ ir mazākais naturālais skaitlis, kura kvadrāts
beidzas ar $3$ četriniekiem: $38^2 = 1444$.

1. vai šādu naturālu skaitļu ir bezgalīgi daudz?
2. atrodiet otro mazāko naturālo skaitli ar šādu īpašību.

<!--
questionType=ProveDisprove.Other,Find.Min
-->



## ABC

**#AlgebriskaIdentitāte** (a) Jā; visi $1000n + 38$ der. Atverot iekavas, $(500-38)^2$ arī beidzas ar $444$. 
Mazāku nav: ja $x \in [39;49]$, $x^2$ nebeidzas ar $44$. Tātad $(n*100 \pm 38)^2$, 
kur $n \in \{ 1,2,3,4,5 \}$ - pārlasa visiem simtu ciparus. 




# <lo-sample/> LV.NOL.2003.12.1 

Skaitļu virknē pirmais un otrais loceklis abi ir $1$, bet katrs nākošais
vienāds ar abu iepriekšējo summu. Vai ar $5$ dalās šīs virknes  
(a) $20$-ais,  
(b) $2003$-ais loceklis?

<!--
seeAlso=LV.NOL.2000.12.1
questionType=Find.Only
-->




## ABC

**#Kongruences** **#PeriodiskaVirkne**  Pirmie $20$ atlikumi: $1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0$, tālāk periods. $F_{20}$ dalīsies ar $5$, bet $F_{2003}$ dos atlikumu $2$, dalot ar $5$. 



# <lo-sample/> LV.NOL.2003.12.5 

Vai eksistē tādas $12$ ģeometriskas progresijas, kas sastāv no reāliem
skaitļiem, ka katrs naturāls skaitlis no $1$ līdz $100$ ieskaitot pieder vismaz
vienai no šīm progresijām?

<!--
concepts=geometric-progression,real-numbers
questionType=ProveDisprove.Exists
-->






# <lo-sample/> LV.NOL.2004.7.1 

Kādu mazāko daudzumu no skaitļiem $1; 2; 3; \ldots; 14; 15$ var izsvītrot, 
lai katru divu atlikušo summa būtu salikts skaitlis?

<small>

* [comb.graph.bipartite](#)
* [div.prop.primes.small](#)
* [misc.invar.parity](#)

</small>

<!--
concepts=composite-numbers
questionType=Find.Min
-->



## ABC
 
**#DirihlēPrincips** **#Paritāte** **#Pirmskaitļi** Var svītrot $7$ pāru skaitļus. Mazāk nevar, jo jāizjauc $7$ pāri $(1,12)$ utt. 


# <lo-sample/> LV.NOL.2004.8.1 

Kādu mazāko daudzumu no naturāliem skaitļiem $1;2;3;\ldots;14;15$ var izsvītrot, 
lai atlikušos varētu sadalīt divās grupās ar īpašību: 
vienas grupas visu skaitļu reizinājums vienāds ar otras grupas visu skaitļu reizinājumu?

<small>

* [div.fta](#)

</small>

<!--
questionType=Find.Min
seeAlso=LV.NOL.2003.8.3
-->




## ABC
 
**#EiklīdaLemma** Jāsvītro $11,13$ un pa vienam $2$ un $5$ daudzkārtnim ($10$). $3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 \cdot 12 = 1 \cdot 2 \cdot 8 \cdot 9 \cdot 14 \cdot 15$




# <lo-sample/> LV.NOL.2004.8.2 

Ir zināms, ka skaitļa $2^{200}$ decimālajā pierakstā ir $61$ cipars. 
Cik daudziem no skaitļiem $2^1; 2^2; 2^3; \ldots; 2^{199}; 2^{200}$ 
decimālais pieraksts sākas ar ciparu $1$?

<small>

* [nota.est.numdigits](#)
* [seq.geom.estimate](#)

</small>

<!--
questionType=Find.Count
seeAlso=[Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law)
seeAlso=[Ideal Voting](https://meduza.io/feature/2017/01/13/itogi-vyborov-v-gosdumu-okazalis-slishkom-idealnymi)
seeAlso=LV.NOL.2005.8.1
-->




## Grupēšana pēc ciparu skaita

* Visas divnieku pakāpes var grupēt pēc ciparu skaita
* Katrā grupā (izņemot viencipara sk.) tieši viena pakāpe sākas ar "1". 



# <lo-sample/> LV.NOL.2004.9.2 

Dots, ka $x$ – naturāls skaitlis. 
Kāds lielākais daudzums no skaitļiem
$$x;\; x + 2;\; x + 4;\; x + 6;\; x + 8$$
var vienlaicīgi būt pirmskaitļi?



# <lo-sample/> LV.NOL.2004.9.4 

Uz tāfeles uzrakstīti $2004$ skaitļi; viens no tiem ir $1$. 
Ar vienu gājienu atļauts
nodzēst vienu skaitli un tā vietā uzrakstīt skaitli 
$a + b - c$, kur $a$, $b$ un $c$ – kaut
kādi trīs no nenodzēstajiem skaitļiem. Vai, atkārtojot 
šādus gājienus vairākas
reizes, var panākt, lai uz tāfeles vienlaicīgi 
būtu uzrakstīti $2004$ skaitļi, kas
visi vienādi ar $1$?




# <lo-sample/> LV.NOL.2004.10.2 

Naturālu skaitli sauc par palindromu, ja tā decimālais
pieraksts ir simetrisks.
Piemēram, palindromi ir $11$; $505$; $4774$ utt.
Visi palindromi, sākot ar $11$, izrakstīti 
virknē augošā secībā. Kāda var būt
blakus uzrakstītu palindromu starpība, ja zināms, 
ka tā ir pirmskaitlis?

<!--
concepts=palindrome
-->




# <lo-sample/> LV.NOL.2004.11.2 

Atrast mazāko tādu naturālu skaitli $n$, $n > 1$, 
ka katram veselam $x$ skaitlis $x^n  - x$
dalās ar $10$.




# <lo-sample/> LV.NOL.2004.12.1 

Skaitļu virknē $1; 1; 2; 3; 5; \ldots$ katrs loceklis, sākot ar trešo, vienāds ar abu
iepriekšējo locekļu summu. Noskaidrot, vai ar $6$ dalās

1. virknes $24$-ais loceklis,
2. virknes $2004$-ais loceklis.

<!--
seeAlso=LV.NOL.2000.12.1
-->






# <LO-REFFF/> LV.NOL.2005.7.1 


Kādu mazāko daudzumu no skaitļiem   
$1;2;3;\ldots;12;13$ var izsvītrot, lai 
katru divu atlikušo summa būtu salikts skaitlis? 



<!--
mainEntry=LV.NOL.2003.7.4
-->







# <lo-sample/> LV.NOL.2005.7.4 

Naturālu skaitli $n$ sauc par īpašu, ja tas ir vienāds ar četru savu dažādu 
dalītāju summu.  
(a) atrodiet kaut vienu īpašu skaitli,  
(b) pierādiet, ka īpašu skaitļu ir bezgalīgi daudz,  
(c) pierādiet, ka visi īpaši skaitļi ir pāru skaitļi. 

<small>

* [div.fta.divisors.frac](#)
* [misc.extr.param](#)
* [mod.fix.parity](#)

</small>

<!--
seeAlso=[Semiperfect number](https://en.wikipedia.org/wiki/Semiperfect_number)
-->




## Dalītāju izteikšana
 
**(a,b)** $n=n/2+n/3+n/7+n/42$; tātad $42k$ ir īpaši. 

**Nav nepāru īpašu skaitļu:**

* Pat "ekstrēmākie" dalītāji ir par mazu:
$$\frac{n}{3}+\frac{n}{5}+\frac{n}{7}+\frac{n}{9} < n.$$
* Nepāru skaitļiem visi dalītāji ir nepāru; 
četru nepāru summa nevar būt pāru.




# <lo-sample/> LV.NOL.2005.8.1 

Ir zināms, ka skaitļa $2^{100}$ decimālajā pierakstā ir $31$ cipars. 
Cik daudziem no skaitļiem $2^1; 2^2; 2^3; \ldots; 2^{99}; 2^{100}$ 
decimālais pieraksts sākas ar ciparu $1$?


<small>

* [nota.est.numdigits](#)
* [seq.geom.estimate](#)

</small>

<!--
seeAlso=LV.NOL.2004.8.2
-->



## ABC
 
**#Nevienādība** Katram ciparu skaitam, izņemot 1-cipara sk., ir tieši viens $2^n$, kas sākas ar ciparu $1$.



# <lo-sample/> LV.NOL.2005.8.3 

Andris iedomājās patvaļīgu naturālu skaitli $n$. Juris ar vienu gājienu 
var pateikt Andrim piecus dažādus naturālus skaitļus
$x_1,x_2,x_3,x_4,x_5$, un Andris pateiks Jurim **vienu**
no skaitļiem $nx_1$, $nx_2$, $nx_3$, $nx_4$, $nx_5$ (bet nepaskaidros, 
**kura** reizinājuma vērtību viņš saka). 
Ar kādu mazāko jautājumu skaitu Juris var noteikti noskaidrot $n$? 

<small>

* [div.common.lcm](#)
* [div.prop.primes.inf](#)
* [div.fta](#)

</small>

<!--
genre=games
questionType=Find.Min
-->




## Ar 1 gājienu nepietiek
 
Pirmajā gājienā Andris var atbildēt ar tādu $x$, 
kas dalās ar vairākiem $x_i$. 



## Ar 2 gājieniem pietiek

Otrajā gājienā Juris nosauc 5 pirmskaitļus $p_i > x_1$ (kur $x_1$ - 
Andra pirmais nosauktais skaitlis). 
Atkarībā no tā, ar kuru pirmskaitli dalās Andra atbilde $x_2$, 
var noteikt $n$.



# <lo-sample/> LV.NOL.2005.9.2 

Kāda var būt četru tādu divciparu pirmskaitļu summa, 
kas sastādīti no cipariem $1$;
$2$; $3$; $4$; $5$; $6$; $7$; $9$, 
izmantojot katru no tiem tieši vienu reizi?



# <lo-sample/> LV.NOL.2005.9.4 

Vai eksistē tādi $6$ skaitļi, ka, aprēķinot visas 
iespējamās to summas pa diviem,
iegūst visus naturālos skaitļus no $1$ līdz 
$15$ ieskaitot?



# <lo-sample/> LV.NOL.2005.9.5 

Ciparu virkni veido sekojoši: tās pirmie cipari 
ir $1; 2; 3; 4$, bet katrs nākošais
vienāds ar četru iepriekšējo summas pēdējo ciparu. 
(Tātad virkne ir $1; 2; 3; 4; 0; 9; 6; 9; \ldots$)

1. Vai virknē kādreiz pēc kārtas parādīsies 
cipari $2; 0; 0; 5$ tieši šādā secībā?
2. Vai virknē kādreiz pēc kārtas citur nekā 
sākumā parādīsies cipari $1; 2; 3; 4$?




# <lo-sample/> LV.NOL.2005.10.1 

Sākumā uz tāfeles uzrakstīti naturāli skaitļi no 
$1$ līdz $10$, katrs vienu reizi. Ar vienu
gājienu atļauts izvēlēties jebkuru uz tāfeles 
uzrakstītu skaitļu grupu, nodzēst to un
vietā uzrakstīt atlikumu, kādu dod nodzēsto 
skaitļu summa, dalot ar $3$. Pēc
vairākiem šādiem gājieniem uz tāfeles palika 
divi skaitļi; viens no tiem bija $8$.
Kāds varēja būt otrs skaitlis?




# <lo-sample/> LV.NOL.2005.10.5 

Uz papīra lapas uzrakstīti vairāki dažādi naturāli 
skaitļi; neviens no tiem
nepārsniedz $100$. Zināms, ka:

1. $1$ un $100$ ir uzrakstīti uz lapas,
2. ja $n$ uzrakstīts uz lapas un $n \neq 1$, 
tad var atrast vai nu tādu uz lapas uzrakstītu
skaitli $x$, ka $n=2x$, vai divus tādus uz lapas
uzrakstītus skaitļus $x$ un $y$, ka $n=x+y$.

Kāds mazākais daudzums skaitļu var būt uzrakstīti 
uz lapas?




# <lo-sample/> LV.NOL.2005.11.1 

Aprēķināt $\sqrt{2005 \cdot 2003 \cdot 1999 \cdot 1997 + 36}$. 



# <lo-sample/> LV.NOL.2005.11.3 

Naturālu skaitli $n$ sauksim par līdzsvarotu, ja tā visus naturālos dalītājus 
(ieskaitot $1$ un pašu $n$) var sadalīt trīs daļās ar vienādām summām.

1. atrast kaut vienu līdzsvarotu skaitli,
2. pierādīt, ka līdzsvarotu skaitļu ir bezgalīgi daudz.




# <lo-sample/> LV.NOL.2005.12.5 

Trijstūra malu garumi izsakās ar pirmskaitļiem. Vai tā laukums var būt naturāls
skaitlis? (Malas mēra metros, laukumu – kvadrātmetros.)









# <lo-sample/> LV.NOL.2006.7.4/LV.NOL.2007.7.4


Kuri naturālie skaitļi ir vienādi ar trīs savu dažādu pozitīvu dalītāju summu?


<small>

* [div.fta.divisors.frac](#)
* [alg.ineq.monotonicity](#)

</small>



## Pāreja uz daļām
 
* $n = (n/2) + (n/3) + (n/6)$ jeb $1 = 1/2+1/3+1/6$. (Tātad der visi, kas
dalās ar $6$.)
* Citādi skaitli $1$ sadalīt dažādu daļu summā nevar - var pamatot ar nevienādībām.



# <lo-sample/> LV.NOL.2006.8.1 


Ir zināms, ka visiem $x$ pastāv vienādība  
$$x^4 + 64 = (x^2 - 4x + 8)\cdot A,$$
kur $A$ ir izteiksme, kas izveidota no $x$ un naturāliem skaitļiem ar 
saskaitīšanas, atņemšanas un reizināšanas operāciju palīdzību. 
Atrast $A$. 


<small>

* [alg.tra.binom.complsquare](#)

</small>



## ABC
 
**#AlgebriskaIdentitāte** Kreisajai pusei var pieskaitīt un atņemt $16x^2$, tad atdalīt pilno kvadrātu.



# <lo-sample/> LV.NOL.2006.8.3 

Vai var izrakstīt rindā visus naturālos skaitļus no $1$ līdz $2006$ ieskaitot 
katru vienu reizi tā, lai katru $3$ pēc kārtas uzrakstīto skaitļu summa dalītos ar $4$. 


<small>

* [mod.period](#)
* [mod.congr.classes](#)

</small>



## ABC
 
**#Invariants** **#PeriodiskaVirkne** Atlikumi, dalot ar $4$ šādā virknē atkārtosies ar periodu $3$, t.i.\ viens no atlikumiem neparādīsies vispār.



# <lo-sample/> LV.NOL.2006.9.4 

Kuri naturālie skaitļi $x$ 
apmierina vienlaicīgi visas sekojošās prasības:
\begin{itemize}
1. $x \leq 2006$,
2. $x$ dalās ar $5$,
3. $x+1$ dalās ar $7$,
4. $x+2$ dalās ar $9$,
5. $x+3$ dalās ar $11$?
\end{itemize}



# <lo-sample/> LV.NOL.2006.9.5 

Gunārs un Dzintars pamīšus raksta uz 
tāfeles pa vienam naturālam skaitlim,
kas nepārsniedz $1000$. Sāk 
Dzintars, uzrakstot skaitli $1$. 
Neviens jau uzrakstīts
skaitlis netiek nodzēsts; nevienu skaitli 
nedrīkst rakstīt otrreiz.
Ja kaut kāds skaitlis $x$ jau ir uz tāfeles, 
tad ar kārtējo gājienu drīkst uzrakstīt
vai nu $x+1$, vai $2x$ (ja izvēlētais 
rakstāmais skaitlis nepārsniedz $1000$). 
Tas, kurš uzraksta $1000$, uzvar. 
Kurš no zēniem uzvar, pareizi spēlējot?



# <lo-sample/> LV.NOL.2006.10.1 

Atrodiet lielāko $12$-ciparu skaitli 
ar īpašību: katri divi blakus uzrakstīti cipari
veido pirmskaitli, un visi šie $11$ pirmskaitļi ir dažādi.




# <lo-sample/> LV.NOL.2006.11.1 

Doti $6$ viens otram sekojoši naturāli skaitļi. 
Pierādīt: eksistē pirmskaitlis, ar kuru
dalās tieši viens no šiem skaitļiem.




# <lo-sample/> LV.NOL.2006.11.5 

Andrim, Dzintaram un Gunāram ir liels daudzums zīmīšu. Uz katras zīmītes ir
uzrakstīts viens no skaitļiem $2$; $3$; $4$; $5$; $6$; $7$; $8$. 
Maija uzlīmēja katram no viņiem uz
pieres pa vienai zīmītei. Katrs zēns redz zīmītes uz abu draugu pierēm, bet neredz
zīmīti uz savas pieres. Maija, visiem dzirdot, paziņoja: "Ne visi skaitļi uz jūsu
pierēm ir dažādi. Visu triju skaitļu reizinājums ir vesela skaitļa kvadrāts."
Vai zēni nesarunājoties var noskaidrot, kādi skaitļi ir uz viņu pierēm?



# <lo-sample/> LV.NOL.2006.12.3 

Kuriem pirmskaitļiem p piemīt īpašība: skaitlim  $p^2 + 11$
ir mazāk nekā $11$
naturālu dalītāju?



# <lo-sample/> LV.NOL.2006.12.5 

Pa apli izvietotas $n$ spuldzes; sākotnēji tās visas ir izslēgtas. Viena spuldze
apzīmēta ar $S$. Atrodam visus skaitļa $n$ pozitīvos dalītājus, ieskaitot $1$ un $n$.
Katram šādam dalītājam $d$ veicam sekojošu operāciju: mainām katras $d$-tās
spuldzes stāvokli (sākot ar spuldzi $S$), pavisam izdarot $n$ maiņas.
Kurām $n$ vērtībām, beidzot šīs darbības, visas spuldzes būs ieslēgtas?

<!--
seeAlso=LV.NOL.2007.12.2
-->










# <lo-sample/> LV.NOL.2007.7.1 


Kurus naturālos skaitļus $n$ var izsacīt formā ${\displaystyle n=\frac{x}{y}}$, 
kur $x = a^5$, $y = b^3$, $a$ un $b$ – naturāli skaitļi? 


<small>

* [div.common.gcd.bezout](#)
* [div.fta](#)
* [alg.tra.pow.nest](#)

</small>

<!--
seeAlso=LV.NOL.2008.7.1
seeAlso=LV.NOL.2009.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** Katru pirmskaitļa pakāpi $p^k$ skaitļa $n$ sadalījumā var izteikt $p^{5c}/p^{3d}$ kaut kādiem naturāliem $c,d$.
**#AlgebriskaIdentitāte** $n = n^{10}/n^{9} = (n^2)^5/(n^3)^3$. 



# <lo-sample/> LV.NOL.2007.8.4 


Atrast mazāko naturālo skaitli, kas dalās ar katru no kaut kādiem $12$ pēc kārtas
ņemtiem naturāliem skaitļiem.


<small>

* [seq.arithm.numestimate](#)
* [div.common.lcm](#)

</small>



## Abi novērtējumi

Apzīmējam ar $M$ mazāko skaitli, kas dalās ar $12$ pēc kārtas sekojošiem $\mathbb{N}$ 
elementiem.

* Skaitlis, kas dalās ar $k$, $k+1$, $\ldots$, $k+11$, dalās arī ar $1,2,\ldots,12$. Šo skaitļu mazākais kopīgais dalāmais ir $8\cdot 9\cdot 5\cdot 7\cdot 11 = 27720$, tātad $M \geq 27720$. 
* Tieši $M =  8\cdot 9\cdot 5\cdot 7\cdot 11 = 27720$ dalās ar $12$ pēc kārtas ņemtiem skaitļiem (no $1$ līdz $12$). Tātad $M \leq 27720$.




# <lo-sample/> LV.NOL.2007.9.5 

Kvadrāts sastāv no $10 \times 10$ 
rūtiņām. Katrā rūtiņā ierakstīts 
naturāls skaitlis, kas
nepārsniedz $10$. Ja divām rūtiņām ir kopēja 
mala vai kopējs stūris, tad tajās
ierakstīto skaitļu lielākais kopīgais dalītājs ir $1$.

1. pierādīt, ka kāds skaitlis ierakstīts 
vismaz $15$ rūtiņās,
2. pierādīt, ka kāds skaitlis ierakstīts 
vismaz $17$ rūtiņās.




# <lo-sample/> LV.NOL.2007.10.3 

Sauksim naturālu skaitli $n > 1$ par labu, 
ja visus tā pozitīvos dalītājus var
sadalīt divās daļās, kuru summas ir vienādas.

1. atrodiet kaut vienu labu skaitli, kas lielāks 
par $10$,
2. vai eksistē labi skaitļi, kas lielāki 
par $20072007$?




# <lo-sample/> LV.NOL.2007.11.1 

Atrisināt naturālos skaitļos vienādojumu $x^2 + 3x = 2^y$. 



# <lo-sample/> LV.NOL.2007.12.3 

Kādiem naturāliem skaitļiem $n$ vienlaicīgi piemīt sekojošas īpašības:

1. $n-1$ un $n+1$ ir pirmskaitļi,
2. skaitļa n visu naturālo dalītāju summa (ieskaitot $1$ un $n$) ir $2n$?










# <lo-sample/> LV.NOL.2008.7.1 

Kurus naturālos skaitļus $n$ var izsacīt formā $n=\frac{x}{y}$, kur $x = a^3$, 
$y = b^4$, $a$ un $b$ – naturāli skaitļi? 


<small>

* [div.common.gcd.bezout](#)
* [div.fta](#)
* [alg.tra.pow.nest](#)

</small>

<!--
seeAlso=LV.NOL.2007.7.1
seeAlso=LV.NOL.2009.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** Katru pirmskaitļa pakāpi $p^k$ skaitļa $n$ sadalījumā var izteikt $p^{3c}/p^{4d}$ kaut kādiem naturāliem $c,d$.
**#AlgebriskaIdentitāte** $n = n^{9}/n^{8} = (n^3)^3/(n^2)^4$.  



# <lo-sample/> LV.NOL.2008.7.3 


Sporta klubā sapulcējušies cīkstoņi un vingrotājas. 
Cīkstoņu vidējais svars ir $84$ kg; vingrotāju vidējais svars ir $54$ kg; 
visu sportistu vidējais svars ir $71$ kg. 
Pierādīt, ka cīkstoņu skaits dalās ar $17$. 

<small>

* [alg.series.mean](#)
* [alg.ineq.equations](#)
* [div.fta.divisors](#)

</small>



## ABC
 
**#MasuCentrs** **#LKD** Lai $71$ būtu līdzsvara punkts starp $84k$ un $54m$, attiecībai $k/m$ jābūt $17/13$ un $\operatorname{LKD}(13,17)=1$.



# <lo-sample/> LV.NOL.2008.8.1 


Sešciparu naturālu skaitli sauc par laimīgu, ja kaut kādu $3$ ciparu summa vienāda 
ar pārējo $3$ ciparu summu. Divi viens otram sekojoši skaitļi ir laimīgi. 
Pierādīt, ka viens no tiem dalās ar $10$.


<small>

* [seq.gaps](#)
* [misc.invar.parity](#)

</small>



## ABC
 
**#Decimālpieraksts** **#Paritāte** Palielinot skaitli par $1$ bez pārnesuma, tā ciparu summas paritāte mainās par $1$.  



# <lo-sample/> LV.NOL.2008.9.1 

Atrodiet vismaz $5$ dažādus pirmskaitļus, ar kuriem dalās skaitlis $3^{32} - 2^{32}$. 



# <lo-sample/> LV.NOL.2008.10.1 

Atrodiet mazāko naturālo skaitli, ko var izsacīt gan kā $15$, gan kā $16$, gan kā 
$17$ pēc kārtas ņemtu naturālu skaitļu summu. 



## ABC

**#AritmētiskaProgresija** **#MKD** Mazākais skaitlis, kas dalās ar $15$, $8$ un $17$ ir $2040$.



# <lo-sample/> LV.NOL.2008.11.4 

Apzīmējam $f(n) = 1^n + 2^n + 3^n + 4^n$, $n=1;2;3;\ldots$. Ar kādu lielāko 
daudzumu nuļļu var beigties skaitlis $f(n)$?



# <lo-sample/> LV.NOL.2008.12.2 

Kādiem naturāliem skaitļiem $n$ vienlaicīgi piemīt sekojošas īpašības:

1. $n-1$ un $n+1$ ir pirmskaitļi, 
2. skaitļa $n$ visu naturālo dalītāju summa (ieskaitot $1$ un $n$) ir $2n$?







# <lo-sample/> LV.NOL.2009.7.1 


Kurus naturālos skaitļus $n$ var izsacīt formā ${\displaystyle n=\frac{x}{y}}$, 
kur $x = a^3$, $y = b^5$, $a$ un $b$ – naturāli skaitļi? 


<small>

* [div.common.gcd.bezout](#)
* [div.fta](#)
* [alg.tra.pow.nest](#)

</small>

<!--
seeAlso=LV.NOL.2007.7.1
seeAlso=LV.NOL.2008.7.1
-->



## ABC
 
**#DalījumsPirmreizinātājos** **#LineārasKongruences** 
Jebkuru pirmskaitļa pakāpi $p^v$ var izteikt kā $(p^k)^3/(p^m)^5$. 
**#AlgebriskaIdentitāte** $n = n^{21}/n^{20} = (n^7)^3/(n^4)^5$. 



# <lo-sample/> LV.NOL.2009.7.3 

Naturālam skaitlim $a$ ir tieši $4$ dalītāji, bet naturālam skaitlim $b$ –
tieši $6$ dalītāji. Pierādiet, ka reizinājumam $ab$ ir **vismaz** $9$ dalītāji. 
Vai var gadīties, ka šim reizinājumam ir **tieši** $9$ dalītāji?  
*Piezīme.* Apskatām tikai tādus dalītājus, kas paši ir naturāli skaitļi. 
Pie skaitļa dalītājiem pieskaita gan viņu pašu, gan vieninieku.)


<small>

* [div.fta.divisors.num](#)
* [comb.full](#)

</small>



## Dalītāju skaita noteikšana

* Tieši četri dalītāji var būt tādam $a$, kas ir vai nu 
$p^3$ vai $pq$. ($p,q$ - pirmskaitļi)
* Līdzīgi $b$ ir $r^5$ vai $r^2s$. ($r,s$ - pirmskaitļi)
* Ja $p=r$, var dabūt $ab = p^3p^5 = p^8$.



## Gadījumu pārlase

Mazāk kā $9$ dalītāji var rasties $3$ veidos:

* $p^a$, kur $a+1 < 9$,
* $p^aq^b$, kur $(a+1)(b+1) < 9$,
* $p^aq^br^c$, kur $(a+q)(b+1)(c+1) < 9$. 

Neviens no šiem gadījumiem neatbilst mūsu nosacījumam.



# <lo-sample/> LV.NOL.2009.8.1 


Tabulā (sk. zīmējumu) Katrīnai jāizvēlas $4$ rūtiņas tā, ka katrā rindā un 
katrā kolonnā tika izvēlēta tieši viena rūtiņa. Pierādiet: neatkarīgi no tā, kuras 
$4$ rūtiņas saskaņā ar šiem noteikumiem Katrīna izvēlēsies, tajās ierakstīto skaitļu summa būs $64$. 

![tabula](LV.NOL.2009.8.1.png)

<small>

* [alg.linear.comb](#)
* [mod.congr.classes](#)

</small>



## ABC
 
**#DalīšanaArAtlikumu** **#SummasPārkārtošana** Sadala divu tabuliņu summā: vienā $1\ldots 7$, otrā $8k$. Vienmēr $(1+3+5+7) + (0+8+16+24) = 64$.





# <lo-sample/> LV.NOL.2009.8.3 

Atrodiet skaitļa $113^{113} - 19^{19}$ pēdējo ciparu. 

<small>

* [mod.exp](#)
* [mod.congr.classes](#)

</small>




## ABC
 
**#PeriodiskaVirkne** **#PēdējieCipari** $113$ pakāpes mainās ar periodu $(1,3,9,7)$, bet $19$ pakāpes ar periodu $(1,9)$. 



# <lo-sample/> LV.NOL.2009.9.2 

Kuri četrciparu naturāli skaitļi vienādi ar savu divu pēdējo ciparu 
veidotā naturālā skaitļa kvadrātu?



# <lo-sample/> LV.NOL.2009.10.1 

Atrodiet mazāko naturālo skaitli, kuru var izsacīt gan kā 
$11$, gan $12$, gan kā $13$ pēc kārtas ņemtu naturālu skaitļu summu. 



# <lo-sample/> LV.NOL.2009.10.3 

Dots, ka $a$ un $b$ ir naturāli skaitļi, $a^2$ dalās ar $b$ un 
$b^2$ dalās ar $a$. Pierādīt, ka $(a+b)^3$ dalās ar $a \cdot b$. 
Vai noteikti $(a + b)^2$ dalās ar $a \cdot b$? 




# <lo-sample/> LV.NOL.2009.11.2 

Atrisināt veselos skaitļos vienādojumu ${\displaystyle \frac{x^2}{2} + \frac{5}{y} = 7}$. 



# <lo-sample/> LV.NOL.2009.12.2 

Dots, ka $p$ ir pirmskaitlis un $n = \left( p^2 - 1 \right) \left( p^2 - 4 \right) + 9$. 
Kāda ir mazākā iespējamā $n$ ciparu summa? Kuriem $p$ tā tiek sasniegta?



# <lo-sample/> LV.NOL.2010.11.1 

Dots, ka $p$ un $q$ ir naturāli skaitļi un kvadrātvienādojuma 
$x^2 + px + q = 0$ saknes ir $x_1$ un $x_2$. Pierādīt, ka 

1. $x_1^2 + x_2^2$, 
2. $x_1^8 + x_2^8$, 
3. $x_1^5 + x_2^5$

ir vesels skaitlis. 









# <lo-sample/> LV.NOL.2010.7.3 


Cik ir tādu naturālu skaitļu $x$ robežās no $1$ līdz $2010$ ieskaitot, ka
$(x+1)(x+2)(x+3)$ dalās ar $343$? 

<small>

* [seq.arithm.numestimate](#)
* [div.fta.divisors.test](#)

</small>



## ABC
 
**#Dalāmība** **#DalījumsPirmreizinātājos** Katrs septītais skaitlis dalās ar $7$, tādēļ $x+1$, $x+2$ vai $x+3$ dalās ar $7^3 = 343$.



# <lo-sample/> LV.NOL.2010.8.1 


Kuru no skaitļiem 
$$102^2 \cdot 103^2 \cdot \ldots \cdot 199^2\;\;\mbox{un}\;\;(102^2 - 1)(103^2 - 1)\ldots(199^2-1)$$
sadalot pirmskaitļu reizinājumā, iegūst vairāk **dažādu** pirmskaitļu? Par cik vairāk?  
*Piezīme.* $24 = 2 \cdot 2 \cdot 2 \cdot 3$ satur divus dažādus pirmskaitļus; $2$ un $3$.

<small>

* [alg.tra.factor.sqdiff](#)
* [div.prop.primes.small](#)
* [alg.series.prod](#)

</small>



## ABC
 
**#AlgebriskaIdentitāte** **#Pirmskaitļi** Dala reizinātājos $102^2 - 1=(102-1)(102+1)$ utt., īsina. Labajā pusē par pirmreizinātāju $101$ vairāk.  



# <lo-sample/> LV.NOL.2010.8.3 


Četrciparu skaitlim pārlika ciparus citā kārtībā. 
Pierādīt: sākotnējā un iegūtā skaitļa starpība dalās ar $9$. 

<small>

* [nota.divrule.3_9.rem](#)
* [nota.combine](#)

</small>



## ABC
 
**#DalāmībaAr3Un9** **#DalīšanaArAtlikumu** $n$ atlikums dalot ar $9$ (arī pārkārtotā $n$ atlikums) vienādi ar $n$ ciparu summas atl.


# <lo-sample/> LV.NOL.2010.9.1 

Atrodiet kaut vienu kvadrātvienādojumu ar veseliem koeficientiem, 
kam viena no saknēm ir 

1. $\sqrt{2} + 1$
2. $\sqrt{7 + 4\sqrt{3}}$

*Piezīme.* Katrā uzdevuma daļā runā par **citu** kvadrātvienādojumu.



# <lo-sample/> LV.NOL.2010.9.5 

Atrisināt naturālos skaitļos vienādojumu sistēmu 
${\displaystyle \left\{ 
\begin{array}{rcl}
x^2 + y & = & z^2\\
y^2 + x & = & t^2
\end{array}
\right.}$





# <lo-sample/> LV.NOL.2010.10.2

Dots, ka $a$ un $b$ ir naturāli skaitļi, $a^2$
dalās ar $b$ un $b^2$ dalās ar $a$. 
Pierādīt, ka $(a-b)^3$
dalās ar $a\cdot{}b$. Vai noteikti
$(a-b)^2$ dalās ar $a\cdot{}b$?

<small>

* [alg.tra.binom.newton](#)
* [div.prop.add](#)
* [div.prop.prod](#)

</small>



## Algebrisks pārveidojums

$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

Katrs no $4$ saskaitāmajiem dalās ar $ab$:

* $\frac{a^3}{ab} = \frac{a^2}{b}$ (zināms, ka dalās)
* $\frac{3a^2b}{ab} = 3a$ un $\frac{3ab^2}{ab}=3b$ (abus var saīsināt)
* $\frac{b^3}{ab} = \frac{b^2}{a}$ (zināms, ka dalās)



## Pretpiemērs (der ļoti daudz kas)

* Ja $a=9$, $b=3$, tad $(a-b)^2 = 36$ nedalās ar $ab=27$.
* Ja $a=18$, $b=12$, tad $(a-b)^2 = 36$ nedalās ar $ab=216$.




# <lo-sample/> LV.NOL.2010.10.4

Atrisināt naturālos skaitļos vienādojumu $x^3 = y! + 2$.

<small>

* [misc.try](#)
* [mod.fix.parity](#) 
* [alg.tra.pow.prod](#)
* [div.valu.prop.prod](#)
* [div.valu.prop.min](#)
* [mod.eq.contradict](#)

</small>




## Faktoriālu un pilno kubu tabulas

<table>
<tr><th>$x$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
<tr><th>$x^3$</th><td>1</td><td>8</td><td>27</td><td>64</td><td>125</td><td>216</td><td>343</td><td>512</td><td>729</td><td>1000</td></tr>
</table>

<table>
<tr><th>$y$</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
<tr><th>$y!$</th><td>1</td><td>2</td><td>6</td><td>24</td><td>120</td><td>720</td><td>5040</td><td>40320</td><td>362880</td><td>3628800</td></tr>
<tr><th>$y!+2$</th><td>3</td><td>4</td><td>8</td><td>26</td><td>122</td><td>722</td><td>5042</td><td>40322</td><td>362882</td><td>3628802</td></tr>
</table>

* Redzam, ka $2^3 = 3!+2$ (ja $x=2, y=3$). 
* Vai ir citas saknes, kur $y>3$? 
* Aplūkojam $x$ paritāti. Vienīgā iespēja: $x$ ir pāru skaitlis: $x=2k$.
    - Tad $(2k)^3 = y!+2$ jeb $8k^3 = y! + 2$.
    - Kreisā puse dalās ar $8$, bet labā (pie $y>3$) dod atlikumu $2$, dalot ar $8$.




# <lo-sample/> LV.NOL.2010.11.2 

Atrisināt veselos skaitļos vienādojumu 
${\displaystyle \frac{x^2}{2} + \frac{5}{y} = 7}$. 



# <lo-sample/> LV.NOL.2010.12.1 

Dots, ka  $n$ – naturāls skaitlis, kas nedalās ar $5$. 
Kāda ir mazākā iespējamā ciparu summa skaitlim 
${\displaystyle \left( n^2 - 1 \right)\left( n^2 - 4 \right) + 7}$? 
Pie kādām $n$ vērtībām tā tiek sasniegta?






# <lo-sample/> LV.NOL.2011.7.1 

Atrodiet skaitļa $1^2 + 2^2 + \ldots + 99^2$ pēdējo ciparu. 

<small>

* [misc.symm.periodicity](#)
* [mod.congr.classes](#)

</small>



## ABC
 
**#Simetrija** **#PēdējieCipari** $10$ grupas: $\left( 1^2 + 2^2 + \ldots + 8^2 + 9^2 \right)$ katra ar pēdējo ciparu $(1+4+9+6)\cdot 2 + 5 = 5$.




# <lo-sample/> LV.NOL.2011.7.2 


Cik ir tādu naturālu skaitļu $n$ no $1$ līdz $2011$ ieskaitot, 
ka skaitlis $(n+1)(n+2)(n+3)$ dalās ar $125$. 


<small>

* [seq.arithm.numestimate](#)
* [div.fta.divisors.test](#)

</small>



## ABC
 
**#Dalāmība** **#DalījumsPirmreizinātājos** Katrs piektais skaitlis dalās ar $5$, t.i. $n+1$, $n+2$ vai $n+3$ jādalās ar $5^3 = 125$. 



# <lo-sample/> LV.NOL.2011.8.1 

Piecciparu skaitlis $B$ ir iegūts no mazāka piecciparu skaitļa $A$, 
samainot vietām tā ciparus. Pierādīt, ka $B-A$ dalās ar $9$.


<small>

* [nota.combine](#)
* [nota.divrule.3_9.rem](#)

</small>



## ABC

**#DalāmībaAr3Un9** **#DalāmībaAr3Un9** **#DalīšanaArAtlikumu** $A$ atlikums dalot ar $9$ (arī $B$ atlikums) vienādi ar $A$ ciparu summas atl.



# <lo-sample/> LV.NOL.2011.9.4 

Pierādīt, ka nav tādu naturālu skaitļu $a$, $x$, $y$ un $z$, ka 
$7^a = 7^x + 7^y + 7^z$. 



# <lo-sample/> LV.NOL.2011.10.3 

Ar $\lfloor a \rfloor$ apzīmējam lielāko veselo skaitli, kas nepārsniedz $a$. 
Atrisināt pozitīvos skaitļos vienādojumu 
${\displaystyle x \cdot \left\lfloor x \cdot \lfloor x \rfloor \right\rfloor = 41}$. 




# <lo-sample/> LV.NOL.2011.11.4 

Zināms, ka $a$ un $b$ ir naturāli skaitļi, pie tam $a^b + 1$ dalās ar $21$. 
Kāda ir mazākā iespējamā summas $a+b$ vērtība? 



# <lo-sample/> LV.NOL.2011.12.3 

Naturālu skaitli sauksim par *fantastisku*, ja tas ir vienāds ar sava kvadrāta ciparu 
reizinājumu. Piemēram, $1$ ir fantastisks (jo $1^2 = 1$ un $1 = 1$), bet 
$4$ – nē (jo $4^2 = 16$, bet $1 \cdot 6 = 6 \neq 4$). 
Pierādīt, ka visi nepāra skaitļi, kas lielāki par $1$, nav fantastiski. 








# <lo-sample/> LV.NOL.2012.7.1 

Ar naturālu skaitli var veikt divu veidu operācijas:

1. reizināt ar $7$
2. nodzēst skaitļa lielāko (vienu no lielākajiem, ja tādi ir vairāki) ciparu. 

Vai ar šādām operācijām no skaitļa $9$ var iegūt skaitli $27$, 
atkārtojot tās vairākas reizes jebkādā secībā?

<small>

* [comb.graph.bfs](#)

</small>



## Koka apstaigāšana, lai meklētu
 
$9 \rightarrow 63 \rightarrow 441 \rightarrow 41 \rightarrow 287 \rightarrow 27$. 



# <lo-sample/> LV.NOL.2012.7.4 

Pierādīt, ka $1004041$ nav pirmskaitlis. 


<small>

* [nota.divrule.101](#)

</small>



## Dalāmības pazīme ar 101
 
Ar $101$ dalās skaitļi, kam apaļajās un kvadrātiekavās liktās summas atšķiras par $101k$: $[01](00)[40](41)$.



# <lo-sample/> LV.NOL.2012.8.1 

Skaitli $3999991$ uzrakstīt kā divu veselu skaitļu reizinājumu tā, 
lai katrs no reizinātājiem ir lielāks nekā $1$. 

<small>

* [alg.tra.factor.sqdiff](#)

</small>



## Kvadrātu starpības formula
 
$3999991 = 4000000 - 9 = 2000^2 - 3^2$. 



# <lo-sample/> LV.NOL.2012.8.3 

Vai naturāla skaitļa ciparu reizinājums var būt skaitlis $\overline{aabbcc}$? 
(Pieraksts $\overline{kmn}$ nozīmē, ka skaitlī ir $k$ simti, $m$ desmiti un 
$n$ vieni.)

<small>

* [nota.divrule.11](#)
* [div.prop.euclidlemma](#)

</small>




## Dalāmība ar 11
 
* $\overline{aabbcc}$ dalās ar $11$ jo ciparu summas pāru un nepāru pozīcijās sakrīt. 
* Neviens cipars nav $11$. Tāpēc arī šādu ciparu reizinājums nevar dalīties ar $11$.



# <lo-sample/> LV.NOL.2012.9.4 

Dota skaitļu virkne $1,1,2,5,9,6,\ldots$. Tā tiek veidota pēc likuma: 
virknes pirmie divi locekļi ir $1$, bet katrs nākamais ir vienāds ar divu 
iepriekšējo locekļu kvadrātu summas pēdējo ciparu. 

1. Noteikt, vai šīs virknes $2012$. loceklis ir pāra vai nepāra skaitlis. 
2. Aprēķināt virknes $2012$. locekli. 




# <lo-sample/> LV.NOL.2012.9.5 

Dots naturāls skaitlis $n \geq 3$. Aplūkojam visus naturālos skaitļus no $1$ līdz $n-1$
ieskaitot, kas ir savstarpēji pirmskaitļi ar skaitli $n$. 
Pierādīt, ka šo skaitļu summa dalās ar $n$. 






# <lo-sample/> LV.NOL.2012.10.3

Doti seši pēc kārtas sekojoši naturāli skaitļi. Pierādīt, ka var atrast tādu
pirmskaitli $p$, ka **tieši viens** no dotajiem skaitļiem dalās ar $p$.

<small>

* [seq.arithm.mod.gaps](#)

</small>

<!--
strategy=contradiction
-->



# <lo-sample/> LV.NOL.2012.10.4

Ir aprēķinātas skaitļu $2^{2012}$ un $5^{2012}$ vērtības 
un iegūtie skaitļi uzrakstīti viens aiz otra. 
Cik cipari uzrakstīti?




# <lo-sample/> LV.NOL.2013.10.4

Ansītis aprēķināja skaitļu $2^{2013}$ un $5^{2013}$ vērtības 
un iegūtos skaitļus uzrakstīja
vienu aiz otra. Cik cipari uzrakstīti?

<small>

* [misc.try](#)
* [nota.est.numdigits.prod](#)

</small>


<!--
sameAs=LV.NOL.2012.10.4
-->










# <lo-sample/> LV.NOL.2012.11.1 

Vai eksistē tāds naturāls skaitlis $m$, kura ciparu reizinājums ir vienāds
ar simetrisku 8-ciparu skaitli?  
(Par *simetrisku* sauc skaitli, kas vienādi lasāms no abiem galiem.)

<!--
concepts=palindrome
-->



# <lo-sample/> LV.NOL.2012.11.4 

Atrast augošu aritmētisku progresiju, kuras visi elementi ir 
naturāli skaitļi un kurai piemīt īpašība: neviens tās elements **nav**
naturāla skaitļa $k$-tā pakāpe jebkuram naturālam $k \geq 2$. 



# <lo-sample/> LV.NOL.2012.12.4 

Kādiem pirmskaitļiem $p$ skaitlim $p^2 + 23$ ir tieši četri naturāli dalītāji?










# <lo-sample/> LV.NOL.2013.7.1 

Naturālie skaitļi no $1$ līdz $18$ sadalīti pa pāriem tā, ka katrā pārī 
esošo skaitļu summa ir naturāla skaitļa kvadrāts. 
Ar ko pārī apvienots skaitlis $1$?  
*Piezīme.* Par skaitļa kvadrātu sauc skaitļa reizinājumu pašam ar sevi.


<small>

* [alg.ineq.equations](#)
* [comb.graph.bipartite](#)

</small>




## ABC
 
**#GadījumuPārlase** **#Grafi** (18,7), (17,8), (16,9) $\rightarrow$ (2,14) $\rightarrow$ (11,5) $\rightarrow$ (4,12) $\rightarrow$ (13,3) $\rightarrow$ (1,15).



# <lo-sample/> LV.NOL.2013.7.2 

Cik starp pirmajiem $2013$ naturālajiem skaitļiem ir tādu skaitļu $x$, ka skaitlis
$x(x+1)(x+2)$ dalās ar $111$?


<small>

* [nota.divrule.composite](#)
* [seq.arithm.numestimate](#)

</small>



## ABC
 
**#Dalāmība** **#DalīšanaPirmreizinātājos** $x(x+1)(x+2)$ Vienmēr dalās ar $3$, bet tam jādalās arī ar $37$. Tādu $x$ ir trīsreiz vairāk kā $\left\lfloor 2013/37 \right\rfloor$. 



# <lo-sample/> LV.NOL.2013.7.4 

Vai pa riņķi var uzrakstīt $13$ naturālus skaitļus tā, lai jebkuru blakus
esošu skaitļu starpība būtu $6$, $10$, $14$ vai $18$? 

<small>

* [misc.invar.congr](#)

</small>



## ABC
 
**#Invariants** Skaitļu atlikums, dalot ar $4$, palielinās par $2$ katrā solī. Pēc $13$ soļiem arī mainās par $2$, bet jāpaliek tam pašam.



# <lo-sample/> LV.NOL.2013.8.1 

Skaitli $8999999$ uzraksti kā divu veselu skaitļu reizinājumu tā, lai katrs
no reizinātājiem ir lielāks nekā $1$. 

<small>

* [alg.tra.factor.sqdiff](#)

</small>



## ABC
 
**#AlgebriskaIdentitāte** Pārveido $3000^2 - 1^2$ pēc kvadrātu starpības formulas.



# <lo-sample/> LV.NOL.2013.8.3 


Cik ir tādu četrciparu skaitļu, kuru pierakstā ir vismaz viens pāra cipars?

<small>

* [comb.count.mult](#)
* [comb.count.complement](#)

</small>



## ABC
 
**#PretējaisNotikums** **#ReizināšanasLikums** $4$-ciparu skaitļu bez pāru cipariem ir $5^4 = 625$; citu būs $9000 - 625$.



# <lo-sample/> LV.NOL.2013.8.4 


Kvadrātā $3 \times 3$ rūtiņas ieraksti deviņus dažādus naturālus skaitļus tā, 
lai katrā rindiņā ierakstīto skaitļu reizinājums un 
katrā kolonnā ierakstīto skaitļu reizinājums būtu viens un tas pats.


<small>

* [comb.full.backtrack](#)
* [alg.tra.pow.nest](#)

</small>



## ABC
 
**#MaģiskaisKvadrāts** **#PakāpjuĪpašības** Izveido $3 \times 3$ parasto maģisko kvadrātu. Pēc tam ceļ attiecīgajās pakāpēs. 



# <lo-sample/> LV.NOL.2013.9.1 

Vai eksistē tāds naturāls skaitlis, kura kvadrāta pēdējie $9$ cipari ir 
$987654321$? 



# <lo-sample/> LV.NOL.2013.10.4 

Ansītis aprēķināja skaitļu $2^{2013}$ un $5^{2013}$ vērtības
un iegūtos skaitļus uzrakstīja vienu aiz otra. 
Cik cipari uzrakstīti?




# <lo-sample/> LV.NOL.2013.11.1 

Atrisināt veselos skaitļos vienādojumu $(x-y)(x+y)=x$. 



# <lo-sample/> LV.NOL.2013.11.4 

Polinoms $P(x)$ ar veseliem koeficientiem četrām veselām $x$ vērtībām 
pieņem vērtību $2000$. Pierādīt, ka nav tādas veselas 
$x$ vērtības, pie kuras dotais polinoms pieņem vērtību $2013$. 




# <lo-sample/> LV.NOL.2013.12.3 

Dots, ka $n>1$ ir tāds naturāls skaitlis, kas, dalot ar $7$, dod 
atlikumu $1$. Pierādīt, ka skaitļa $n^2 + 3n + 3$ visi pirmreizinātāji 
ir mazāki nekā $n^2$. 












# <lo-sample/> LV.NOL.2014.7.3 


Cik starp pirmajiem $2014$ naturālajiem skaitļiem ir tādu skaitļu $x$, ka 
skaitlis $x(x+1)(x+2)$ dalās ar $87$? 

<small>

* [nota.divrule.composite](#)
* [seq.arithm.numestimate](#)

</small>



## ABC
 
**#Dalāmība** **#DalīšanaPirmreizinātājos** $x(x+1)(x+2)$ Vienmēr dalās ar $3$, jādalās ar $29$. Tādu $x$ ir trīsreiz vairāk kā $\left\lfloor 2014/29 \right\rfloor$. 



# <lo-sample/> LV.NOL.2014.8.3 

Cik ir tādu piecciparu skaitļu, kuru pierakstā ir vismaz viens nepāra cipars?

<small>

* [comb.count.mult](#)
* [comb.count.complement](#)

</small>



## ABC
 
**#PretējaisNotikums** **#ReizināšanasLikums** $5$-ciparu skaitļu bez nepāru cipariem ir $4 \cdot 5^4 = 2500$; citu būs $90000 - 2500$.



# <lo-sample/> LV.NOL.2014.9.3 

Atrisināt naturālos skaitļos vienādojumu $3abc + 3a + 3b = 7bc + 7$. 




# <lo-sample/> LV.NOL.2014.10.2

Pierādīt, ka, izvēloties $52$ no aritmētiskās progresijas 
$1, 4, 7, 10, \ldots$ locekļiem, kas nepārsniedz
$300$, vienmēr starp šiem skaitļiem var atrast divus skaitļus, kuru summa ir $302$.

<small>

* [seq.arithm.expr](#)
* [seq.arithm.numestimate](#)
* [seq.arithm.pairsum](#)
* [misc.extr.pigeon](#)

</small>



## Progresijā ir 100 locekļu zem 300

$$1, 4, 7, \ldots, 148, 151, 154, \ldots, 298$$

* Diviem locekļiem - $1$, $151$ - nav pāra, ar ko summa ir $302$.
* Vēl ir 49 pārīši - $(4,298)$, $(7,295)$, $\ldots$, $(148,154)$.
* Izvēloties $52$ skaitļus, vismaz $50$ no tiem būs $\neq 1$, $\neq 151$. 
* Dirihlē princips - divi būs no viena pārīša.







# <lo-sample/> LV.NOL.2014.11.1 

Polinoms $P(x)$, kura visi koeficienti ir veseli skaitļi, piecām 
veselām $x$ vērtībām 
pieņem vērtību $2000$. Pierādīt, ka nav tādas veselas 
$x$ vērtības, pie kuras dotais polinoms pieņem vērtību $2014$. 



# <lo-sample/> LV.NOL.2014.11.3 

Kādiem maturāliem skaitļiem $n$ piemīt šāda īpašība: visu skaitļa $n$ 
naturālo dalītāju, izņemot $1$ un $n$, kvadrātu summa 
vienāda ar pašu skaitli $n$? 



# <lo-sample/> LV.NOL.2014.12.3 

Uz tāfeles uzrakstīti visi trīsciparu skaitļi, kas dalās ar $31$: 
$$124, 155, 186, 217, \ldots, 961, 992.$$
Vai no šiem skaitļiem var izvēlēties **(a)** deviņus, **(b)** desmit tā, 
ka gan simtu, gan desmitu, gan vienu pozīcijā vismaz pa vienai reizei 
atrodams katrs no cipariem $1$ līdz $9$? 



# <lo-sample/> LV.NOL.2014.12.5 

Vai var atrast tādus $2014$ dažādus naturālus skaitļus 
$a_1, a_2,\ldots,a_{2014}$, ka 
$$\frac{1}{a_1} + \frac{1}{a_2} + \ldots + \frac{1}{a_{2014}} = 1?$$










# <lo-sample/> LV.NOL.2015.7.2 

Sensenos laikos saimnieciskajam Gotfrīdam bija $99$ aitas un $21$ kamielis, 
citu mājlopu Gotfrīdam nebija. Bagdādē par $4$ kamieļiem pretī varēja saņemt $8$ 
aitas, bet Damaskā par $5$ aitām pretī varēja saņemt $3$ kamieļus. 
Vai, atkārtoti mainot dzīvniekus tikai šajās divās pilsētās, Gotfrīds varēja iegūt 
tieši $2015$ mājlopus?

<small>

* [misc.invar.congr](#)
* [misc.invar.parity](#)

</small>



## Salīdzina paritāti
 
Katras maiņas iznākumā dzīvnieku kopskaits mainās par pāru skaitli. $99+21$ ir pāru, bet $2015$ – nepāru.



# <lo-sample/> LV.NOL.2015.7.3 

Tabulā, kuras izmēri ir $3 \times 3$ rūtiņas, katrā rūtiņā ierakstīts viens naturāls skaitlis, 
kas nepārsniedz $10$, visi ierakstītie skaitļi ir dažādi. 
Katrām divām rūtiņām ar kopīgu malu aprēķina tajos ierakstīto skaitļu summu. 
Vai iespējams, ka visas iegūtās summas ir pirmskaitļi?

<small>

* [comb.constr.color](#)
* [mod.fix.parity](#)
* [div.prop.primes.small](#)
* [comb.full](#)

</small>



## ABC
 
**#GadījumuPārlase** **#Krāsošana** Pāru/nepāru skaitļi kā šaha galdiņš. Vidū liek $1$, pārlasa $2,4,6,10$ izvietojumu variantus ($8$ neizmanto).



# <lo-sample/> LV.NOL.2015.8.1 

Pierādi, ka 

1. $49^5 + 7^9$ dalās ar $2$; 
2. $49^5 - 7^9$ dalās ar $6$.


<small>

* [mod.congr.classes](#)

</small>



## ABC
 
**#DalīšanaArAtlikumu** Divu nepāru skaitļu summas/starpības ir pāru skaitļi. Pie tam $49^n$ un $7^n$ dod atlikumu $1$, dalot ar $3$. 



# <lo-sample/> LV.NOL.2015.8.2 

Autoservisā "Šrotiņš" ir $39$ mašīnas. Naskais Maigonis katra mēneša 20. 
datumā vai nu pārdod $7$ restaurētas mašīnas un to vietā nopērk 
$16$ vecas mašīnas, vai arī $19$ mašīnas nodod metāllūžņos 
un to vietā nopērk $4$ vecas mašīnas. 
Nekādas citas darbības, kas maina mašīnu skaitu, netiek veiktas. 
Vai iespējams, ka "Šrotiņā" kāda mēneša 21. datumā būs tieši $2015$ mašīnas?

<small>

* [misc.invar.congr](#)

</small>



## Salīdzina atlikumus (mod 3)
 
Mašīnu skaits mainās par $-7+16=9$ vai par $-19+4 = -15$, t.i. par $3k$. Bet $39+3k \neq 2015$.




# <lo-sample/> LV.NOL.2015.9.2 

Regulāra astoņstūra virsotnēs pēc kārtas uzrakstīti skaitļi 
$7, 15, 3, 17, 1, 9, 5, 11$. Ar skaitļiem atļauts veikt šādas darbības:

1. pieskaitīt kādam skaitlim divus skaitļus, kas atrodas blakus virsotnēs; 
2. atņemt no skaitļa divkāršotu pretējā virsotnē uzrakstīto skaitli, ja 
starpība ir pozitīva.

Vai, atkārtoti izpildot šīs darbības, var panākt, ka vienā no virsotnēm 
būs ierakstīts skaitlis $2014$? 



# <lo-sample/> LV.NOL.2015.9.4 

Uz tāfeles uzrakstīti naturāli skaitļi no $1$ līdz $13$. Dārta 
grib nodzēst vienu no tiem, bet pārējos ierakstīt $3 \times 4$ 
rūtiņu tabulā (katru skaitli vienā rūtiņā) tā, lai visās rindās un 
kolonnās skaitļu vidējais aritmētiskais būtu vienāds.

1. Pierādīt, ka ir tieši viens skaitlis, kuru nodzēšot, viņa 
to varēs izdarīt!
2. Atrast vienu skaitļu izvietojuma piemēru!






# <lo-sample/> LV.NOL.2015.10.2

Ar naturālu skaitli atļauts veikt šādas darbības:

* pieskaitīt $6$;
* dalīt ar $4$, ja skaitlis dalās ar $4$;
* mainīt vietām skaitļa ciparus (skaitļa sākumā nedrīkst atrasties nulle).

Vai, atkārtoti izpildot šīs darbības, no skaitļa $30$ var iegūt skaitli $2015$?

<small>

* [nota.divrule.3_9.divides](#)
* [misc.invar](#)

</small>



## Invariants ir dalāmība ar $3$

Ja sākotnējais skaitlis $x$ dalījās ar $3$, tad pēc katras darbības arī rezultāts dalīsies ar $3$:

* $x+6$ dalās ar $3$, ja $x$ dalās ar $3$
* $x/4$ dalās ar $3$, ja $x$ dalās ar $3$ (un arī ar $4$, lai varētu izdalīt).
* $x'$ (pārkārtotiem cipariem) arī dalās ar $3$, jo ciparu summa nemainās.

$30$ dalās ar $3$, bet $2015$ nedalās. Tātad pārveidot par $2015$ nevar. 






# <lo-sample/> LV.NOL.2015.10.3

Vairāku pēc kārtas sekojošu naturālu skaitļu summa ir $177$. 
Kādas vērtības var pieņemt
mazākais no šiem saskaitāmajiem?

<small>

* [seq.arithm.summation](#)
* [div.fta.proc](#)
* [comb.full](#)

</small>



## Aritmētiskas progresijas locekļu summa

$$S=a_1 + a_2 + \ldots + a_n = \frac{a_1 + a_n}{2}\cdot{}n$$

> Aritmētiskās progresijas summu iegūst, reizinot "vidējo elementu": 
> $a_v = \frac{a_1+a_n}{2}$ ar progresijas locekļu skaitu: $S = a_v\cdot{}n$.  
> Ja $n$ ir nepāru skaitlis, tad vidējais elements $a_v$ tiešām progresijā ir.  
> Ja $n$ ir nepāru skaitlis, tad "vidējais elements" ir abu vidējo locekļu 
> aritmētiskais vidējais. 

Abos gadījumos $2\cdot{}177 = (a_1+a_n)\cdot{}n$ jeb
$$2 \cdot 3 \cdot 59 = (a_1+a_n)\cdot{}n$$



## Gadījumu pārlase

Skaitlim $2 \cdot 3 \cdot 59$ ir tikai galīgs skaits dalītāju $n$:

* Ja $n=2$, tad $177 = 88\frac{1}{2}\cdot{}2 = 88+89$,
* Ja $n=3$, tad $177 = 59\cdot{}3 = 58+59+60$,
* Ja $n=6$, tad $177 = 29\frac{1}{2}\cdot{}6=$
$=27+28+29+30+31+32$. 

Vēl lielāki $2 \cdot 3 \cdot 59$ dalītāji ($n=59$ u.c.) novestu pie ļoti garām aritmētiskām 
progresijām, kurās būtu arī negatīvi locekļi.
Tās neder, jo $177$ bija vairāku pēc kārtas sekojošu **naturālu** skaitļu summa.





# <lo-sample/> LV.NOL.2015.10.4

Vai eksistē tāds vesels skaitlis $x$, ka visi skaitļi

1. $x$, $x+23$, $x+45$, $x+121$
2. $x$, $x+23$, $x+46$, $x+121$

ir veselu skaitļu pakāpes ar naturālu kāpinātāju, 
kas lielāks nekā 1 (kāpinātāji var būt dažādi)?

<small>

* [misc.try](#)
* [div.fta.pow.other](#)
* [mod.fix.parity](#)

</small>

<!--
strategy=contradiction
-->




## Ievieto nelielas vērtības

* $x$ arī ir vesela skaitļa pakāpe
* Pārbaudām $x=1,4,8,9,16,25,32,36,49,\ldots$
* Jau $x=4$ der (pirmajā piemērā)



## Kas notiek otrajā piemērā?

* Vai $x$ un $x+46$ var *vienlaikus* būt naturālu skaitļu pakāpes?
* Ja $x$ ir pāru, tad **gan** $x$, **gan** $x+46$ dalās ar $4$.
* Ja $x$ ir nepāru, tad **gan** $x+23$, **gan** $x+121$ dalās ar $4$.







# <lo-sample/> LV.NOL.2015.11.3 

Kāds ir mazākais naturālais skaitlis $n$, kuru iespējams 
izteikt kā trīs dažādu naturālu skaitļu $a$, $b$ un $c$ summu tā, 
ka visi skaitļi $a+b$, $a+c$, $b+c$ ir naturālu skaitļu kvadrāti? 



# <lo-sample/> LV.NOL.2015.12.2 

Ar naturālu skaitli atļauts izdarīt šādas darbības:
\begin{itemize}
1. pieskaitīt skaitlim tā ciparu summu;
2. atņemt no skaitļa tā ciparu summu.
\end{itemize}
Vai, atkārtoti izpildot šīs darbības, no skaitļa $139$ 
var iegūt skaitli **(a)** $63$; **(b)** $193$?



# <lo-sample/> LV.NOL.2015.12.5 

Vai eksistē tādi naturāli skaitļi $a$, $b$ un $c$, ka skaitļa $a^2 + b^2 + c^2$

1. pēdējie divi cipari ir $15$; 
2. pēdējie četri cipari ir $2015$? 












# <lo-sample/> LV.NOL.2016.7.2 

Dots naturāls skaitlis, kas dalās ar $99$ un kura pēdējais cipars nav $0$. 
Pierādi, ka uzrakstot šī skaitļa ciparus pretējā secībā, arī iegūst skaitli, kas
dalās ar $99$. 

<small>

* [nota.divrule.3_9.divides](#)
* [nota.divrule.11](#)
* [nota.divrule.composite](#)

</small>



## ABC
 
**#DalāmībaAr11** **#DalāmībaAr3Un9** Dalāmībai ar $9$ ciparu summa nemainās; 
ar $11$ – pāru/nepāru pozīcijās ciparu summas atšķiras par $11k$.



# <lo-sample/> LV.NOL.2016.7.5 


(a) Vai var atrast dažādus veselus skaitļus 
$a$, $b$, $c$ un $d$ tādus, ka izpildās vienādības
$a+b = cd$ un $ab = c+d$?  
(b) Vai šādus skaitļus var atrast, ja papildus zināms, ka $a > 2016$?


<small>

* [misc.symm.rename](#)
* [misc.extr.param](#)

</small>



## Ekstrēmais elements - 1

* $a,b,c,d$ uzdevuma formulā ir simetriski.
* Izvēlamies vienu nelielu vērtību - piemēram $c=1$. Tad $a+b=d$, $ab=d+1$ 
(divu skaitļu summa par $1$ mazāka nekā reizinājums).
* Var izvēlēties $a=2$, $b=3$, $c=1$ un $d=5$.
 
 

## Ekstrēmais elements - 2

* $a,b,c,d$ uzdevuma formulā ir simetriski.
* Izvēlamies $c=0$. Tad $a+b=0$, $ab=d$.
* Var izvēlēties $c=0$, $a = 2017$, $b = -2017$, $d = -2017^2$.



# <lo-sample/> LV.NOL.2016.8.2 

Karlīna uzrakstīja divus skaitļus, kuru pierakstā nav izmantots cipars $0$. 
Katru ciparu viņa aizstāja ar burtu: dažādus ciparus – ar dažādiem burtiem, 
vienādus – ar vienādiem. Viens no uzrakstītajiem 
skaitļiem *DUBĻUNNN* dalās ar $104$. Pierādi, ka otrais skaitlis *BURBUĻVANNA* nedalās ar $56$. 


<small>

* [nota.divrule.2_5_10.divides](#)

</small>



## ABC
 
**#DalāmībaAr4Un8** **#LKD** *NNN* Dalās ar $8$ t.t.t. ja $N=0$ vai $N=8$. 
*NNA* dalās ar $8$ tikai tad, ja $A=0$ vai $A=8$. T.i. $A=N$ – pretruna.



# <lo-sample/> LV.NOL.2016.9.2 

Pierādīt, ka 

1. no pieciem naturāliem skaitļiem vienmēr var izvēlēties vairākus
(vismaz divus), kuru summa dalās ar $4$;
2. var atrast četrus tādus naturālus skaitļus, ka no tiem nevar izvēlēties
vairākus (vismaz divus), kuru summa dalās $4$. 




# <lo-sample/> LV.NOL.2016.9.5 

Doti $2016$ skaitļi: $1^2$; $2^2$; $3^2$; $\ldots$; $2015^2$; $2016^2$. 
Vai starp šiem skaitļiem var salikt ``$+$'' un ``$-$'' zīmes tā, lai iegūtās izteiksmes
vērtība būtu $0$?






# <lo-sample/> LV.NOL.2016.10.1

Pierādīt, ka katram naturālam $n$ ir patiesa vienādība
$$1\cdot{}4 + 2\cdot{}7 + 3\cdot{}10 + \cdots + n\cdot{}(3n + 1) = n(n+1)^2.$$

<small>

* [seq.gaps](#)
* [misc.ind](#)

</small>




## Definējam virkni 

$$a_n = 1\cdot{}4 + 2\cdot{}7 + 3\cdot{}10 + \cdots + n\cdot{}(3n + 1)$$

* Katrs nākamais šīs virknes loceklis ir par $n\cdot{}(3n+1)$ lielāks kā iepriekšējais

Tikpat liela ir starpība starp $n(n+1)^2$ un izteiksmi, kur $n$ aizstāj ar $n-1$: $(n-1)n^2$:

$$n(n+1)^2 - (n-1)n^2 = n(n^2 + 2n + 1) - n^3 + n^2 =$$
$$= n^3+2n^2+n - n^3+n^2 = 3n^2 + n = n(3n+1).$$



## Matemātiskā indukcija

* Ja $n=1$, tad $a_1 = 1\cdot{}4 = 4$ un arī $n(n+1)^2 = 4$. 
* Arī vēlāk gan virkne $a_n$, gan formula $n(n+1)^2$ pieaug vienādiem soļiem. 






# <lo-sample/> LV.NOL.2016.10.2

Pierādīt, ka no jebkuriem trim naturālu skaitļu kvadrātiem var izvēlēties divus tā, 
ka to summa vai starpība dalās ar $5$.

<small>

* [mod.congr.pow](#)
* [mod.congr.pow](#)
* [misc.extr.pigeon](#)

</small>



## Pilnu kvadrātu atlikumi, dalot ar 5

$$(1^2,2^2,3^2,4^2,5^2)=(1,4,9,16,25).$$

* Atlikumi, dalot ar $5$, ir sekojoši: $(1,4,4,1,0)$. Pēc tam tie atkārtojas.
* Starp tiem ir tikai $3$ dažādi atlikumi: $0,1,4$. 
* Izvēloties trīs kvadrātus:
    - Vai nu divi no tiem sakritīs,
    - No katra būs pa vienam - tad $1+4$ dalās ar $5$.




# <lo-sample/> LV.NOL.2016.11.2 

Pierādīt, ka starp jebkuriem pieciem naturālu skaitļu kvadrātiem var atrast divus tādus, 
ka to summa vai starpība dalās ar $13$. 



# <lo-sample/> LV.NOL.2016.12.2 

Atrast visu skaitļu, kas pierakstāmi formā $a^4 - b^4$, kur $a > b > 5$ un 
$a$ un $b$ ir pirmskaitļi, lielāko kopīgo dalītāju!







# <lo-sample/> LV.NOL.2017.7.2 

Piecciparu skaitļa, kas dalās ar $13$, pirmais cipars ir vienāds ar ceturto, bet otrais – ar piekto. Kāds ir šī
skaitļa trešais cipars? Atrodi visas iespējamās vērtības un pamato, ka citu nav!



# <lo-sample/> LV.NOL.2017.8.2 

Ja no piecciparu skaitļa, kam pirmais cipars vienāds ar ceturto, bet otrais – ar piekto, atņem vieninieku tad
iegūtais skaitlis dalās ar $11$. Kāds var būt sākotnējā piecciparu skaitļa trešais cipars? Atrodi visus
iespējamos variantus un pamato, ka citu nav!




# <lo-sample/> LV.NOL.2017.9.4 

Naturālu skaitli sauksim par *pārdabisku*, ja, tā ciparus uzrakstot pretējā secībā, iegūst skaitli, kas ir lielāks
nekā sākotnējais skaitlis, un iegūtais skaitlis dalās ar sākotnējo skaitli. Mazākais *pārdabiskais* skaitlis ir
$1089$, jo $9801 : 1089 = 9$. Atrast vēl divus citus *pārdabiskus* skaitļus!



# <lo-sample/> LV.NOL.2017.9.5 

1. Pierādīt, ka starp $1010$ dažādiem naturāliem skaitļiem, no kuriem neviens nepārsniedz $2017$, vienmēr
iespējams izvēlēties trīs skaitļus tā, ka divu izvēlēto skaitļu summa ir vienāda ar trešo skaitli!
2. Vai šāda īpašība ir spēkā arī $1009$ dažādiem naturāliem skaitļiem, kas nepārsniedz $2017$?







# <lo-sample/> LV.NOL.2017.10.5

Desmitciparu skaitlī vienādus ciparus aizvietojot ar vienādiem burtiem, 
bet dažādus – ar dažādiem, ieguva
vārdu $MATEMĀTIKA$ (īsais "A" un garais "Ā" aizstāj atšķirīgus ciparus). 
Papildus zināms, ka skaitlis $\overline{MA}$
dalās ar $2$, $\overline{MAT}$ - ar 3, $\overline{MATE}$ - ar 4, 
$\overline{MATEM}$ - ar 5, $\overline{MATEMĀ}$ - ar 6, $\overline{MATEMĀT}$ - ar 7,
$\overline{MATEMĀTI}$ - ar 8, $\overline{MATEMĀTIK}$ - ar 9, 
$\overline{MATEMĀTIKA}$ - ar 10. Noteikt, kāds bija sākotnējais
desmitciparu skaitlis!

<small>

* [nota.divrule.2_5_10.divides](#)
* [nota.divrule.2_5pow.divides](#)
* [nota.divrule.3_9.divides](#)
* [nota.divrule.composite](#)
* [comb.full](#)

</small>



## Gadījumu pārlase

* $\overline{MATEMĀTIKA}$ dalās ar $10$ ($A=0$)
* $\overline{MATEM}$ dalās ar $5$ ($M=5$)
* $\overline{MAT}=\overline{50T}$ dalās ar $3$ ($T = 1,4,7$)
* Dalāmība ar $2,4,6,8$ ($E$, $Ā$, $I$ ir pāru cipari $\neq 0$)
* Dalāmība ar $4$ ($TI$ un $TE$ dalās ar $4$, t.i $T \neq 4$)
* Dalāmība ar $6$ ($\overline{MATEMĀ}$ ciparu summa ir $5+0+(1|7)+(2|6)+5+(4|8)$
t.i. $\overline{EMĀ}=258$ vai $\overline{EMĀ}=654$.
* Dalāmība ar $7$: $50(1|7)(2|6)5(4|8)(1|7)$
($\overline{MATEMĀT}$ ir $5012581$ vai $5076547$)
* Dalāmība ar $8$: $50125816$, $50765472$
* $5076547290$ der (bet $5012581680$ neder, jo cipari $K$ un $Ā$ nedrīkst sakrist).








# <lo-sample/> LV.NOL.2017.11.3 

Atrisināt naturālos skaitļos vienādojumu sistēmu:
$$\left\{ \begin{array}{rcl}
x + z & = & 2007, \\
31xz & = & y^2.
\end{array} \right.$$



# <lo-sample/> LV.NOL.2017.12.3 

Naturālu skaitli sauksim par *pārdabisku*, ja, tā ciparus uzrakstot 
pretējā secībā, iegūst skaitli, kas ir lielāks
nekā sākotnējais skaitlis, un iegūtais skaitlis dalās ar sākotnējo skaitli. 
Mazākais pārdabiskais skaitlis ir
$1089$, jo $9801:1089 = 9$. 

1. Atrast vēl divus citus pārdabiskus skaitļus! 
2. Pierādīt, ka pārdabisku skaitļu ir bezgalīgi daudz!









# <lo-sample/> LV.NOL.2018.7.1 

Četrstāvu mājai ir vairāk nekā $200$ logu. Zināms, ka pirmajā stāvā 
ir nepāra skaits logu, bet katrā no nākamiem stāviem to ir tieši 
par diviem mazāk nekā stāvu zemāk. Kāds mazākais logu skaits var būt 
šīs mājas ceturtajā stāvā?



# <lo-sample/> LV.NOL.2018.7.4 

Dots, ka piecciparu skaitlis $\overline{acbba}$ dalās ar $11$ un $a>b>c$. 
Pierādīt, ka var atrast trīs citus piecciparu skaitļus,
kas dalās ar $11$, ir lielāki nekā $\overline{acbba}$ un veidoti, 
samainot vietām sākotnējā skaitļa ciparus!



# <lo-sample/> LV.NOL.2018.8.4 

No cipariem $1, 2, 3, 4, 5, 6, 7, 8, 9$, katru izmantojot vienu reizi, 
izveidoti trīs trīsciparu skaitļi. Ar kādu lielāko
nuļļu skaitu var beigties šo trīs skaitļu summa?





# <lo-sample/> LV.NOL.2018.9.4 

Vai var atrast tādus veselus skaitļus $x$𝑥 un $y$, ka 
$20x^3 − 17y^2 + 1 = 2018$?





# <lo-sample/> LV.NOL.2018.10.4

No cipariem $1, 2, 3, 4, 5, 6, 7, 8, 9$, katru izmantojot 
divas reizes, izveidoti trīs sešciparu skaitļi. Ar kādu lielāko
nuļļu skaitu var beigties trīs izveidoto skaitļu summa?

<small>

* [nota.divrule.3_9.divides](#)
* [nota.est.numdigits.sum](#)
* [comb.constr.alpha](#)

</small>

<!--
strategy=contradiction
-->




## No pretējā

* Katrs sešciparu skaitlis ir mazāks par 1 miljonu. 
* 3 šādu skaitļu summa ir zem 10 miljoniem (7-cipari). 
* Vai var beigties ar 6 nullēm?
* Ciparu summas dēļ jādalās ar $9$, bet $9000000$ ir par daudz.



## Vai var beigties ar 5 nullēm? 

Konstruējam, ikreiz liekot mazākos iespējamos ciparus.

![Saskaitīšana stabiņā](LV.NOL.2018.10.4.png)




# <lo-sample/> LV.NOL.2018.11.4 

No cipariem $1, 2, 3, 4, 5, 6, 7, 8, 9$, katru izmantojot divas reizes, 
izveidoja vienu septiņciparu, vienu sešciparu un
vienu piecciparu skaitli. Ar kādu lielāko nuļļu skaitu 
var beigties trīs izveidoto skaitļu summa?



# <lo-sample/> LV.NOL.2018.12.4 

Doti naturāli skaitļi $a$ un $b$. Pierādīt

1. ja $20a + 18b$ dalās ar $7$, tad $201a + 8b$ dalās ar $7$;
2. ja $201a + 8b$ dalās ar $7$, tad $20a + 18b$ dalās ar $7$.



# <lo-sample/> LV.NOL.2018.12.5 

Vienādojuma ar veseliem koeficientiem $x^4 + bx^2 + c = 0$ 
vienas saknes vērtība ir $\sqrt{20} - \sqrt{18}$. Atrast
vienādojuma koeficientus un pārējās trīs saknes!







# <lo-sample/> LV.NOL.2019.7.4 

Vai var atrast tādus veselus skaitļus $a$ un $b$, ka $ab(a+5b) = 150015$?

<!--
questionType=ProveDisprove.Exists
genre=integer-equation
-->



# <lo-sample/> LV.NOL.2019.7.5

Uz tāfeles uzrakstītas deviņas zvaigznītes 
$$\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast\;\ast.$$
Mārtiņš ieraksta kādas zvaigznītes vietā jebkuru ciparu
no $1$ līdz $9$. Pēc tam Rihards jebkuru divu citu zvaigznīšu vietā ieraksta 
divus nenulles ciparus (tie var arī
atkārtoties). Pēc tam vēl divas reizes viņi atkārto šo darbību. 
Rihards uzvar, ja iegūtais deviņciparu skaitlis dalās
ar $31$. Vai Rihards vienmēr var uzvarēt?

<!--
questionType=Algorithm,ProveDisprove.ForAll
genre=game
concepts=divisibility
-->



# <lo-sample/> LV.NOL.2019.8.4

Uz tāfeles uzrakstīti skaitļi $\frac{3}{2}, \frac{4}{5}, \frac{5}{3}$. 
Ar vienu gājienu atļauts izvēlēties divus no uzrakstītajiem skaitļiem (apzīmēsim
tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt uz tāfeles skaitļus
$\frac{b^2}{a}$ un $\frac{a^2}{b}$. 
Vai, izdarot vairākus šādus gājienus,
var panākt, lai uz tāfeles vienlaicīgi būtu uzrakstīti skaitļi 
$\frac{4}{3}, \frac{4}{5}, \frac{5}{2}$. 

<!--
seeAlso=LV.NOL.2000.7.5
genre=making-moves
questionType=ProveDisprove.Exists
-->



# <lo-sample/> LV.NOL.2019.8.5

Izmantojot divus atšķirīgus nenulles ciparus $x$ un $y$ 
ir izveidoti divi trīsciparu skaitļi
$\overline{xyx}$ un $\overline{yxy}$. 
Zināms, ka $\overline{xyx}$
dalās ar $3$, bet $\overline{yxy}$ dalās ar $4$. 
Kāds var būt izveidotais trīsciparu skaitlis $\overline{yxy}$?

<!--
questionType=Find.All
concepts=divisibility
-->



# <lo-sample/> LV.NOL.2019.9.5

Kāds mazākais ciparu skaits jāpieraksta ciparu virknes $3456$ beigās, 
lai iegūtu skaitli, kas dalās ar $2019$?

<!--
questionType=Find.Min
concepts=divisibility
genre=digit-manipulation
-->



# <lo-sample/> LV.NOL.2019.10.5

Atrast visus pirmskaitļu pārus $(m,n)$, kuriem 
$20m + 18n = 2018$.

<small>

* [nota.divrule.2_5_10.divides](#)
* [div.fta.proc](#)

</small>

<!--
concepts=primes
questionType=Find.All
genre=integer-equation
-->


## Risinājums

* Īsinām $20m+18n=2018\;\Rightarrow\;10m+9n=1009$. 
* Lai $1009 - 9n$ dalītos ar $10$, $n$ pēdējais cipars ir "1":  
$m=(1009-9n)/10$ ir vesels, ja $n=1,11,21,31,41,51,61,71,81,91,101,111$
* Atbilstošie pāri: $(100,1)$, $(91,11)$, $(82,21)$, <red>$(73,31)$</red>, $(64,41)$, 
$(55,51)$, $(46,61)$, <red>$(37,71)$</red>, $(28,81)$, $(19,91)$, $(10,101)$, $(1,111)$. 

No tiem der tikai divi: $(73,31)$, $(37,71)$






# <lo-sample/> LV.NOL.2019.11.5

Atrast visus pirmskaitļu pārus $(m,n)$, kuriem $20m + 19n = 2019$.

<!--
questionType=Find.All
concepts=linear-expression,primes
genre=integer-equation
-->


# <lo-sample/> LV.NOL.2019.12.5

Pierādīt, ka vienādojumam
$(a - b)^2 = a+b$ ir bezgalīgi daudz atrisinājumu naturālos skaitļos!

<!--
questionType=Prove.Other
genre=integer-equation
-->











































