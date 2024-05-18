# <lo-sample/> LT.VUMIF.2016.9.3

Atrodiet visas naturālas $n$ vērtības, kurām skaitlis
$\frac{n^3 + 3}{n^2 + 7}$
ir naturāls.

<text lang="lt">
Raskite visas natūraliąsias $n$ reikšmes, su kuriomis skaičius
$\frac{n^3 + 3}{n^2 + 7}$
yra natūralusis.
</text>

<small>

* topic:PolynomialLongDivision
* topic:NumTheoryInequalityMethod
* topic:ExhaustionMethod
* strategy:CaseAnalysis

</small>




## Atrisinājums

*#PolynomialDivision*  
Ja skaitītājā polinoma pakāpe (kubs) ir vismaz tāda
pati kā saucējā (kvadrāts), tad tos var dalīt, iegūstot
atlikumu:

$$\frac{n^3 + 3}{n^2 + 7} = \frac{n(n^2 + 7) - 7n + 3}{n^2 + 7} = 
n + \frac{-7n+3}{n^2 + 7}.$$

* Skaitītājs un saucējs ir pozitīvi naturāliem $n$, t.i. dalījums
būs naturāls t.t.t. ja daļa $\frac{-7n+3}{n^2+7}$ ir vesela. 
* Ja $n \geq 7$, tad daļa nav vesela, jo
$$|n^2 + 7| \geq |7n + 7| > |-7n+3|$$


*#CaseAnalysis*  
$\frac{-7n+3}{n^2+7}$ ievietojam 
visas vērtības $n=1,2,3,4,5,6$. (Lielākas ievietojot, 
nav cerību iegūt naturālu skaitli, 
jo tām saucēja modulis pārsniedz skaitītāja
moduli.)

* Ja $n=2$, tad $\frac{-7n+3}{n^2 + 7} = \frac{-11}{11} = -1$. 
* Ja $n=5$, tad $\frac{-7n+3}{n^2 + 7} = \frac{-32}{32} = -1$. 
* Vērtībām $n=1,3,4,6$ sanāk daļskaitļi.




# <lo-sample/> LT.VUMIF.2016.10.3

Atrodiet mazāko naturālo skaitli $n$, kuram skaitļi 
$\sqrt[5]{5n}$, $\sqrt[6]{6n}$, $\sqrt[7]{7n}$
ir naturāli. 

<text lang="lt">
Raskite mažiausią natūralųjį skaičių $n$, kuriam skaičiai
$\sqrt[5]{5n}$, $\sqrt[6]{6n}$, $\sqrt[7]{7n}$
yra natūralieji.
</text>


<small>

* topic:CanonicalFactorization
* topic:PrimeFactorizationAndPowers
* topic:GcdAndLcmProperties
* topic:ArithmeticSeriesGaps
* topic:ChineseRemainderTheorem

</small>




## Atrisinājums

*#PrimeFactorization*  
Apzīmējam $n = 2^a3^b5^c7^d$ ir $n$ sadalījums pirmreizinātājos. 
Citus pirmreizinātājus neieviešam
(aizdomas, ka tie nebūs vajadzīgi - citi kāpinātāji būs $0$). 

* $\sqrt[5]{5n} \in \mathbb{N}$ nozīmē, ka $a, b, c-1, d$ dalās ar $5$
* $\sqrt[6]{6n} \in \mathbb{N}$ nozīmē, ka $a-1, b-1, c, d$ dalās ar $6$
* $\sqrt[7]{7n} \in \mathbb{N}$ nozīmē, ka $a,b,c,d-1$ dalās ar $7$


*#CongrienceSystems*  
Risinām kongruenču sistēmas skaitļiem $a,b,c,d$.

* (Veseli nenegatīvi kāpinātāji) 
$a$ un $b$ dalās ar $5$ un $7$, dod atlikumu $5$, dalot ar $6$. 
Mazākais tāds skaitlis ir $a=b=35$.
* $c$ dalās ar $6$ un $7$, dod atlikumu $4$, dalot ar $5$. 
Mazākais tāds skaitlis ir $c=84$.
* $d$ dalās ar $5$ un $6$, dod atlikumu $6$, dalot ar $7$. 
Mazākais tāds skaitlis ir $90$. 

$$n = 2^{35}\cdot{}3^{35}\cdot{}5^{84}\cdot{}7^{90}.$$




# <lo-sample/> LT.VUMIF.2016.11_12.1

Agne savā traukā ielēja $p$ litrus ūdens, 
bet Bens savā traukā ielēja $q$ litrus ūdens. 
Pārmaiņus veikdami gājienus, viņi spēlē sekojošu spēli. 
Gājiena laikā spēlētājs no sava trauka otra spēlētāja
traukā ielej tik daudz ūdens, 
cik ūdens jau ir otrā spēlētāja traukā.
Spēli sāk Agne. Pēc simts gājieniem Agnes traukā
bija $q$ litri ūdens, bet Bena traukā - $p$ litri ūdens. 
Atrodiet $\frac{p}{q}$.

<text lang="lt">
Agnė į savo turimą indą įpylė $p$ litrų vandens, 
o Benas į savąjį indą įpylė $q$ litrų vandens.
Pakaitomis atlikdami ėjimus, jie žaidžia tokį žaidimą. 
Ėjimo metu žaidėjas iš savo indo į
kito žaidėjo indą turi įpilti tiek vandens, 
kiek jo tuo metu yra kito žaidėjo inde. Žaidimą
pradėjo Agnė. Po šimto ėjimų Agnės inde buvo $q$ 
litrų vandens, o Beno – $p$ litrų vandens.
Raskite $\frac{p}{q}$.
</text>




# <lo-sample/> LT.VUMIF.2016.11_12.3

Noskaidrojiet, vai eksistē tāds naturāls skaitlis $n$, ka 
skaitlis $n \cdot 2^{2016} - 7$ ir
naturāla skaitļa kvadrāts.

<text lang="lt">
Nustatykite, ar egzistuoja toks natūralusis skaičius $n$, 
kad skaičius $n \cdot 2^{2016} - 7$ yra
natūraliojo skaičiaus kvadratas.
</text>




# <lo-sample/> LT.VUMIF.2017.9.2

Vai izmantojot tieši pa vienai reizei visus desmit ciparus 
$0,1,2,\ldots,9$ var uzrakstīt divus naturālus skaitļus, ka 
viens skaitlis būtu otra kvadrāts?  
*Piezīme.* Pirmais skaitļa cipars nevar būt nulle.

<text lang="lt">
Ar panaudojus po lygiai vieną kartą visus dešimt skaitmenų
$0,1,2,\ldots,9$ galima užrašyti du natūraliuosius skaičius, 
kad vienas skaičius būtų kito kvadratas?  
*Pastaba.* Pirmasis skaičiaus skaitmuo negali būti nulis. 
</text>

<small>

* topic:DigitsInOperationResult
* topic:ExhaustionMethod

</small>




## Atrisinājums

**Apgalvojums:** Ja naturāla skaitļa $n$ decimālpierakstā ir $k$
cipari, tad tā kvadrāta $n^2$ decimālpierakstā 
ir $2k$ vai $2k-1$ cipari. 

*Pierādījums.* Mazākā $n$ vērtība ar $k$ cipariem ir 
$10^{k-1}$ (vieninieks ar $k-1$ nullēm). 
Šī skaitļa kvadrāts ir $10^{2k-2}$, t.i. $2k-1$ cipari.  
Savukārt lielākā $n$ vērtība ir $10^k-1$ (visi $k$ deviņnieki). 
Tad šī skaitļa kvadrāts ir 
$$(10^k-1)^2 = 10^{2k} - 2\cdot{}10^k + 1=\overline{\underbrace{9\ldots9}_k8\underbrace{0\ldots0}_k1},$$


*#CaseAnalysis*
Desmit ciparus var sadalīt divās daļās kā $1+9=2+8=3+7=4+6=5+5$. 

* Kāpinot kvadrātā $3$-ciparu skaitli, var iegūt $5$-ciparu vai $6$-ciparu rezultātu. 
* Kāpinot kvadrātā $4$-ciparu skaitli, var iegūt $7$-ciparu vai $8$-ciparu rezultātu. 

Neviena no summām $3+5$, $3+6$, $4+7$, $4+8$ nav precīzi $10$. Tātad šādi sadalīt nevar, 
jo nebūs vajadzīgais ciparu kopskaits.


**Radniecīgs uzdevums:** Ja atmetam ciparu $0$, uzdevums jārisina citādi: šoreiz var kāpināt kvadrātā $3$-ciparu 
skaitli $n$ un iegūt $6$-ciparu rezultātu $m=n^2$. 

* $n+n^2$ dod tādu pašu atlikumu, dalot ar $9$, kā $n$ un $n^2$ kopīgā ciparu summa: $1+2+\ldots+9=45$, jeb $n+n^2$ dalās ar $9$. 
* Ir tikai divas iespējas: 
    - $n$ dalās ar $9$ vai arī 
    - $n$ dod atlikumu $8$, dalot ar $9$. (Var izmēģināt visus atlikumus, ko dod $n$, dalot ar $9$.)

Der, piemēram, šādi skaitļi: 

$$567^2=321489;\;\;854^2=729316.$$





# <lo-sample/> LT.VUMIF.2017.10.1

Atrodiet visus veselu skaitļu pārus $(a,b)$, 
kuriem eksistē tādi veseli skaitļi $x$ un
$y$, ka
$$8x^4 + 8y^4 = a^4 + 6a^2b^2 + b^4.$$


<text lang="lt">
Raskite visas sveikųjų skaičių poras $(a,b)$, 
kurioms egzistuoja tokie sveikieji skaičiai $x$ ir
$y$, kad
$$8x^4 + 8y^4 = a^4 + 6a^2b^2 + b^4.$$
</text>



# <lo-sample/> LT.VUMIF.2017.10.2

Atrodiet visus veselo skaitļu $m$ un $n$ pārus
$(m,n)$, kas apmierina vienādību 
$$m^2 + 2m - 9 = n^2 + n.$$

<text lang="lt">
Raskite visas sveikųjų skaičių $m$ ir $n$ poras 
$(m, n)$, tenkinančias lygybę
$$m^2 + 2m - 9 = n^2 + n.$$
</text>

<small>

* topic:CompletingSquare
* topic:FullPowerGaps
* topic:NumTheoryInequalityLargeIntervals
* topic:ExhaustionMethod

</small>


## Atrisinājums

*#CompleteTheSquare*  
Pārrakstām doto vienādību:  
$m^2 +2m +1 -10 = n^2 + n.$  
$(m+1)^2 = n^2 + n + 10.$

Jāatrod tie $n$, kuriem 
$n^2 + n + 10$ ir pilns kvadrāts, tad
$$m = \sqrt{n^2+n+10} - 1.$$

Atrodam atstarpes starp blakus kvadrātiem:

* Aiz $n^2$ nākamais pilnais kvadrāts ir 
$(n+1)^2 = n^2 + 2n + 1$, bet iepriekšējais
pilnais kvadrāts ir $n^2 - 2n + 1$. 
* Ja $n>0$, tad pie $n \geq 10$:
$$n^2 + n + 10 < n^2 + 2n + 1.$$
* Ja $n=0$, tad $n^2 + n + 10 = 10$ nav pilns kvadrāts.
* Ja $n<0$, tad $f(n) = n^2 + n + 10$ 
pieņem vērtības $10,12,16,22,30,40,52,66,82,100,\ldots$
pie $n \in \{ -1,-2,\ldots,-10 \}$. 
* Parabola $n^2 + n + 10$ ir simetriska, tāpēc
vērtība pie pozitīva $n_1$ ir tāda pati kā pie negatīva 
$-1-n_1$. 


*#CaseAnalysis*    
Pilnā pārlase pozitīvo n atrašanai:

* Ievietojam $n$ vērtības $1,2,\ldots,10$. 
* $n^2 + n+10$ attiecīgās vērtības ir 
$12,16,22,30,40,52,66,82,100,120$
* Kopā ar negatīvajām vērtībām, iegūstam, ka 
$n$ vērtības var būt $-10,-3,2,9$. 
* Atrisinājumi:
$$(m,n) \in \{ (9; -10), (3; -3), (3; 2), (9; 9) \}.$$







# <lo-sample/> LT.VUMIF.2017.11_12.2

Atrodiet vienādojuma
$$x^2y^2 + 208 + 4(\mbox{LKD}(x,y) + \mbox{MKD}(x,y))^2$$
visus naturālos atrisinājumus $(x,y)$. 
Šeit $\mbox{LKD}(x,y)$ un $\mbox{MKD}(x,y)$ attiecīgi apzīmē skaitļu 
$x$ un $y$ lielāko kopīgo dalītāju un mazāko kopīgo dalāmo. 

<text lang="lt">
Raskite lygties
$$x^2y^2 + 208 + 4(\mbox{DBD}(x,y) + \mbox{MBK}(x,y))^2$$
visus natūraliuosius sprendinius $(x,y)$. 
Čia $\mbox{DBD}(x,y)$ ir $\mbox{MBK}(x,y)$ atitinkamai žymi
skaičių $x$ ir $y$ didžiausią bendrą daliklį ir 
mažiausią bendrą kartotinį.
</text>



# <lo-sample/> LT.VUMIF.2017.11_12.4

Uz tāfeles uzrakstīts skaitlis $636363$. 
Divi spēlētāji $A$ un $B$ pārmaiņus veic gājienus, 
pirmo gājienu izdara $A$. 
Gājiena laikā ir jānodzēš uz tāfeles esošais skaitlis un 
jāuzraksta tā starpība ar jebkuru viņa naturālu dalītāju. 
Spēlētājs, kurš uzraksta $0$, zaudē. Noskaidrojiet, kuram 
spēlētājam ir uzvaras stratēģija, un parādiet to.

<text lang="lt">
Lentoje užrašytas skaičius $636363$. 
Du žaidėjai $A$ ir $B$ pakaitomis atlieka ėjimus, pirmąjį
ėjimą atlieka $A$. Ėjimo metu reikia nutrinti 
lentoje esantį skaičių ir užrašyti jo ir bet kurio
jo natūraliojo daliklio skirtumą. Žaidėjas, užrašęs 
skaičių $0$, pralaimi. Nustatykite, kuris
žaidėjas turi pergalės strategiją, ir nurodykite ją.
</text>


<small>

* topic:GameInvariant
* strategy:BeginAtTheEnd

</small>



## Atrisinājums

> **Definīcija:** Par "aukstām" pozīcijām sauksim tās, no kurām sākot, 
> uzvar otrais spēlētājs $B$. (Visas citas ir "karstas" 
> pozīcijas.)

* "1" ir auksta pozīcija
* "2" (tikai pāreja $2 \rightarrow 1$) ir karsta.
* "3" (tikai pāreja $3 \rightarrow 2$) ir auksta. utt.


![Dalītāju atņemšana](LT.VUMIF.2017.11_12.4.svg)

**A:** "6" (pārejas uz "3", "4" vai "5") ir karsta, jo **eksistē** pāreja uz aukstu.  
**B:** "7" (pārejas tikai uz karstu "6") ir auksta, jo **katra**/**vienīgā** pāreja uz karstu.  
**C:** "9" (pārejas uz "6" un "8") ir auksta, jo **katra** pāreja uz karstu.


Otrais spēlētājs var pēc katra gājienu pāra saglabāt sekojošu invariantu.

**Apgalvojums:** Ja sākumā uz tāfeles uzrakstīts 
nepāru skaitlis, tad otrais spēlētājs var pēc katra sava 
gājiena panākt, lai tur joprojām būtu nepāru skaitlis. 

*Nav pabeigts.*




# <lo-sample/> LT.VUMIF.2018.9.4

Naturālam skaitlim $M = 3N$ 
ir tikpat ciparu, cik naturālam skaitlim $N > 10$. 
Lai iegūtu skaitli $M$, vajag palielināt
ikvienu skaitļa $N$ ciparu: vienam no cipariem 
pieskaitīt $2$, bet pie atlikušajiem cipariem 
pieskaitīt pa nepāru naturālam skaitlim (ne obligāti 
visiem to pašu). 
Atrodiet visas iespējamās skaitļa $N$ pēdējā 
cipara vērtības.

<text lang="lt">
Natūralusis skaičius $M = 3N$ 
turi tiek pat skaitmenų, kaip ir
natūralusis skaičius $N > 10$. 
Norint gauti skaičių $M$, reikia padidinti 
kiekvieną iš skaičiaus $N$ skaitmenų: prie vieno skaitmens
pridėti $2$, o prie likusių skaitmenų 
pridėti po nelyginį natūralųjį
skaičių (nebūtinai po tą patį). 
Raskite visas galimas skaičiaus $N$
paskutinio skaitmens reikšmes.
</text>



# <lo-sample/> LT.VUMIF.2018.10.4

Skaitļa $n>1$ visu pozitīvo dalītāju 
(ieskaitot $1$ un $n$) reizinājums vienāds ar $n^3$.
Norādiet visas iespējamās skaitļa $n$ vērtības, 
uzrakstot, kāds var būt skaitļa $n$ sadalījums pirmreizinātājos. 

<text lang="lt">
Skaičiaus $n>1$ visų teigiamų daliklių 
(įskaitant $1$ ir $n$) sandauga lygi $n^3$.
Nurodykite visas galimas skaičiaus $n$ reikšmes, 
užrašydami, koks gali būti skaičiaus $n$ 
skaidinys pirminiais daugikliais.
</text>

<small>

* topic:DivisorNumberAndSum
* topic:FactorizationAndDivisibility

</small>



## Atrisinājums

**Apgalvojums:** Ja skaitlis $n$ nav pilns kvadrāts, tad 
tā dalītājus var sadalīt pa pāriem $(d_1,d_2)$, kur
katrā pārī reizinājums $d_1d_2=n$. (Ja $n$ ir pilns kvadrāts, 
tad dalītājam $\sqrt{n}$ nav pāra.)

Ja skaitļa dalītāju reizinājums ir $n^3$, tad tam ir 
tieši $6$ pozitīvi dalītāji. 

Iespējami divi dalījumi pirmreizinātājos: 

* $n=p^5$
* $n=p^2q^1$. 


**Apgalvojums:** Skaitlim ar sadalījumu pirmreizinātājos
$$n=p_1^{a_1}p_2^{a_2}\cdots{}p_k^{a_k}$$
dalītāju skaits ir 
$$(a_1+1)(a_2+1)\cdots{}(a_k+1).$$

Skaitli $6$ var izteikt vai nu kā $(5+1)$ vai 
arī kā $(2+1)(1+1)$. Daži piemēri:

* Skaitlim $n=32=2^5$ ir 6 dalītāji: $1,2,4,8,16,32$. 
To reizinājums ir $32^3$. 
* Skaitlim $n=12=2^23^1$ ir 6 dalītāji: $1,2,3,4,6,12$. 
To reizinājums ir $12^3$.



# <lo-sample/> LT.VUMIF.2018.11_12.4

Naturālie skaitļi $p$, $x$, $y$ apmierina vienādojumus:
$$p + 1 = 2x^2,\;\;p^2 + 1 = 2y^2.$$
Noskaidrojiet visas iespējamās skaitļa $p$ vērtības, ja 
zināms, ka šis skaitlis ir pirmskaitlis. 

<text lang="lt">
Natūralieji skaičiai $p$, $x$, $y$ tenkina lygtis:
$p + 1 = 2x^2,\;\;p^2 + 1 = 2y^2.$$
Nustatykite visas galimas skaičiaus $p$ reikšmes, 
jei žinoma, kad šis skaičius pirminis.
</text>



# <lo-sample/> LT.VUMIF.2019.9.1

Atrodiet visus veselu skaitļu trijniekus $(x,y,z)$, 
kas apmierina vienādojumu sistēmu
$$
\left\{ \begin{array}{l}
x^3 + y^3 = z^3 + 1,\\
y^2 - x^2 = x+y,\\
2x^3 - 6x = z^3 - 4x^2.
\end{array} \right.$$

<text lang="lt">
Raskite visus sveikųjų skaičių trejetus $(x,y,z)$, 
tenkinančius lygčių sistemą
$$
\left\{ \begin{array}{l}
x^3 + y^3 = z^3 + 1,\\
y^2 - x^2 = x+y,\\
2x^3 - 6x = z^3 - 4x^2.
\end{array} \right.$$
</text>



# <lo-sample/> LT.VUMIF.2019.9.2

Algis un Balis spēlē sekojošu spēli, 
pārmaiņus izdarīdami gājienus. Sākumā 
ir divas monētu kaudzītes: vienā kaudzītē
ir $m$ monētas, bet otrā $n$ monētas.
Gājiena laikā jāveic jebkura viena no trim 
sekojošām darbībām:
1) izmest vienu monētu no jebkuras kaudzītes;
2) izmest pa vienai monētai no abām kaudzītēm; 
3) pārcelt vienu monētu no jebkuras kaudzītes uz otru kaudzīti. 
Sāk Algis. Spēlētājs, kurš nevar veikt gājienu, zaudē. 
Noskaidrojiet visus naturālu skaitļu pārus $(m,n)$, 
kuriem Balim ir uzvaras stratēģija, t.i. kurām viņš var
nodrošināt uzvaru, lai kā spēlētu Algis. 

<text lang="lt">
Algis ir Balys žaidžia tokį žaidimą, 
pakaitomis atlikdami ėjimus. Pradžioje
yra dvi monetų krūvelės: vienoje krūvelėje 
yra $m$ monetų, o kitoje yra $n$
monetų. Ėjimo metu reikia atlikti bet 
kurį vieną iš šių trijų veiksmų: 
1) išmesti vieną monetą iš bet kurios krūvelės; 
2) išmesti po vieną monetą iš abiejų krūvelių; 
3) perkelti vieną monetą iš bet kurios krūvelės į kitą. 
Pradeda Algis. Žaidėjas, negalintis atlikti ėjimo, 
pralaimi. Nustatykite visas natūraliųjų skaičių $(m,n)$ 
poras, kurioms Balys turi pergalės strategiją, t. y.
kurioms jis gali užsitikrinti pergalę, 
kad ir kaip žaistų Algis.
</text>


<small>

* topic:GameInvariant
* topic:ModularParity
* topic:StrongAndReverseInduction

</small>

<!--
strategy=begin-at-the-end
-->




## Atrisinājums

**Definīcija:** 
Galīgā divu spēlētāju spēlē par aukstu pozīciju sauksim tādu, kurā pirmajam spēlētājam neeksistē uzvaroša stratēģija: 
jebkurš viņa gājiens noved karstā pozīcijā (no kuras pretinieks var atkal atgriezties aukstā pozīcijā utt. 
līdz otrā spēlētāja uzvarai. 


| **(0,0)** | (1,0)     | **(2,0)** | (3,0)     | **(4,0)** | 
| --------- | --------- | --------- | --------- | --------- |
| (0,1)     | (1,1)     | (2,1)     | (3,1)     | (4,1)     | 
| **(0,2)** | (1,2)     | **(2,2)** | (3,2)     | **(4,2)** | 
| (0,3)     | (1,3)     | (2,3)     | (3,3)     | (4,3)     | 
| **(0,4)** | (1,4)     | **(2,4)** | (3,4)     | **(4,4)** | 



* **(0,0)** ir auksta pozīcija; ja tā ir pēc Baļa gājiena, viņš tūlīt uzvar. 
* Pozīcijas, no kurām **eksistē** gājiens 
  uz **(0,0)** ir karstas. Tajās
  uzvar tas, kam pirmais gājiens: (0,1), (1,0), (1,1).
* No (0,2) un (2,0) **katrs** gājiens ir uz
  karstu pozīciju; tādēļ tās ir aukstas. 


Ievērojam, ka aukstām pozīcijām izpildās īpašība: abi 
skaitļi ir pāru. 

**Apgalvojums par invariantu:** Ja $(m,n)$ abi ir pāru skaitļi, tad
Balis pēc katra sava gājiena var nodrošināt, ka šī īpašība saglabājas:
abi skaitļi atkal ir pāru skaitļi. 

Algis noteikti rada vienu vai divus nepāru skaitļus pēc sava gājiena.

* Ja pēc viņa gājiena ir viens nepāru skaitlis, 
  tad Balis no tā atņem $1$. 
* Ja abi ir nepāru, tad Balis atņem no abiem.


**Apgalvojums:** Balis uzvar visiem $(m,n)$, kas ir pāru skaitļi. 

No pretējā: Ja eksistē tādi divi pāru skaitļi $(m,n)$, kuriem Balis neuzvar, 
atrodam to pāri, kam $m+n$ ir vismazākais. Abos gadījumos 
Balis var atbildēt uz Alģa gājienu, iegūstot
jaunus divus pāru skaitļus $(m_2,n_2)$, kam $m_2+n_2 < m+n$.   
(Ņemam vērā, ka Balis nekad nepārliek no vienas kaudzītes otrā.)

Skaitļiem $(m_2,n_2)$ Balis uzvar pēc induktīvā pieņēmuma. Pretruna.





# <lo-sample/> LT.VUMIF.2019.9.4

Jurgis uzrakstīja trīs naturālus skaitļus, 
no kuriem katrs beidzas ar to pašu ciparu, ar kuru 
beidzas pārējo divu skaitļu summa, un sareizināja tos. 
Jurgis uzrakstīja tikai reizinājuma pēdējos trīs 
ciparus. Kādu ciparu trijnieku viņš varēja iegūt? 
Atrodiet visas iespējas. 

<text lang="lt">
Jurgis užrašė tris natūraliuosius skaičius, 
iš kurių kiekvienas baigiasi tuo
pačiu skaitmeniu kaip kitų dviejų skaičių 
suma, ir sudaugino juos. Jurgis
užrašė tik sandaugos paskutinius tris 
skaitmenis. Kokį skaitmenų trejetą jis
galėjo gauti? Raskite visas galimybes.
</text>

<small>

* topic:ModularArithmeticOther
* topic:CongruenceEquations
* topic:CountingUsingSymmetry
* topic:ExhaustionMethod
* topic:DivisibilityRulesLastDigits

</small>



## Atrisinājums

**Definīcija:** Ar $a \equiv b\;(\mbox{mod}\,10)$ apzīmējam to, ka
$a$ un $b$ dod vienādus atlikumus, dalot ar $10$ (jeb beidzas
ar to pašu ciparu). 

$$\left\{ \begin{array}{ll}
a + b \equiv c & (\mbox{mod}\,10) \\
b + c \equiv a & (\mbox{mod}\,10) \\
c + a \equiv b & (\mbox{mod}\,10)
\end{array} \right.$$

* Saskaitot visas trīs kongruences, iegūsim
$$\begin{array}{ll}
2a+2b+2c \equiv a+b+c & (\mbox{mod}\,10)\;\mbox{jeb}\\
a+b+c \equiv 0\ & (\mbox{mod}\,10).
\end{array}$$


Tātad trīs Jurģa iedomāto skaitļu summa beidzas 
ar ciparu $0$. Atņemot kongruences 
$a+b+c \equiv 0\;(\mbox{mod}\,10)$ un 
$a + b \equiv c\;(\mbox{mod}\,10)$ iegūstam
$c \equiv -c\;(\mbox{mod}\,10)$.

Tātad $c$ (un simetrijas dēļ arī $b$ un $a$) 
beidzas ar $0$ vai ar $5$. 
Pārlasot gadījumus $(0;0;0)$,  $(5;0;0)$, 
$(5;5;0)$, $(5;5;5)$, der tikai 
$(0;0;0)$ un $(5;5;0)$. 



Apskatām pēdējos trīs ciparus.

* Ja $a,b,c$ visi beidzas ar $0$, tad pēdējie trīs
cipari ir $000$, jo reizinājums dalās ar $1000$. 
* Ja $a$, $b$ beidzas ar $5$, bet $c$ beidzas ar $0$, 
tad reizinājums dalās ar $5\cdot{}5\cdot{}10 = 250$. 
* Dalāmības pazīme ar $250$ ir tāda, ka pēdējie trīs
cipari dalās ar $250$ ($000$, $250$, $500$, $750$). 
* Var dabūt jebkuru 3 ciparu kombināciju, kas dalās ar $250$

| $(a,b,c)$    | $abc$ beidzamie cipari | 
| ------------ | ---------------------- |
| $(5,5,10)$   | $250$                  |
| $(5,5,20)$   | $500$                  |
| $(5,15,10)$  | $750$                  |
| $(5,5,40)$   | $1000$                 |



# <lo-sample/> LT.VUMIF.2019.10.4

Naturālu skaitli sauksim par *septiņīgu*, 
ja tam ir tieši $70$ ciparu: $10$ vieninieku, 
$10$ divnieku, $\ldots$, $10$ septiņnkieku. 
Pierādīt, ka, ja viens septiņīgs skaitlis dalās
ar citu septiņīgu skaitli, tad tie ir vienādi. 

<text lang="lt">
Natūralųjį skaičių vadinsime *septintiniu*, 
jei jis turi lygiai $70$ skaitmenų: $10$
vienetų, $10$ dvejetų, $\ldots$, $10$ septynetų. 
Įrodykite, kad jei vienas septintinis
skaičius dalijasi iš kito, tai jie lygūs.
</text>

<small>

* topic:DivisibilityRulesForRemainders
* topic:Invariant
* topic:ModularArithmetic

</small>



## Atrisinājums

**Apgalvojums:** Skaitlis $n$ un tā ciparu summa $S(n)$ 
dod vienādus atlikumus, dalot ar $9$ (vispārināta
dalāmības pazīme).  
**Secinājums:** Mainot vietām ciparus, skaitļa
atlikums, dalot ar $9$, nemainās.

Septiņīgam skaitlim ciparu summa: 
$$10\cdot(1+2+\ldots+7) = 10\cdot{}28=280.$$

$280$ dod atlikumu $1$, dalot ar $9$. Tātad arī 
katrs septiņīgs skaitlis dos atlikumu $1$, dalot ar $9$. 


Septiņīgu skaitļu daudzkārtņiem izpildās šādi apgalvojumi:

* Divu septiņīgu skaitļu attiecība nevar pārsniegt $7$. 
* Reizinot skaitli $9k+1$ (atlikums $1$, dalot ar $9$)
ar jebkuru skaitli $2,\ldots,7$, sanāks attiecīgi 
atlikumi $2,\ldots,7$. 
* Tātad šie reizinājumi nebūs septiņīgi. 

*Secinājums.* Vienīgais septiņīga skaitļa daudzkārtnis, kas 
var būt septiņīgs ir viņš pats.



# <lo-sample/> LT.VUMIF.2019.11_12.4

Naturālu skaitli sauksim par *piecīgu*, ja
tam ir tieši $500$ ciparu: pa $100$ divnieku, 
trijnieku, četrinieku, piecinieku un sešinieku. 
Pie piecīga skaitļa $M$ labajā pusē pierakstot 
divus ciparus $81$, iegūts skaitlis 
$N = \overline{M81}$. Pierādiet, ka  
a) $M$ nedalās ne ar vienu piecīgu skaitli, izņemot sevi pašu;  
b) $N$ nedalās ne ar vienu piecīgu skaitli. 

<text lang="lt">
Natūralųjį skaičių vadinsime *penktiniu*, 
jei jis turi lygiai $500$ skaitmenų: po
$100$ dvejetų, trejetų, ketvertų, penketų ir šešetų. 
Prie penktinio skaičiaus $M$
iš dešinės prirašius du skaitmenis $81$, 
gautas skaičius $N = \overline{M81}$. Įrodykite,
kad a) $M$ nesidalija iš jokio penktinio skaičiaus, 
išskyrus save patį; 
b) $N$ nesidalija iš jokio penktinio skaičiaus.
</text>

<small>

* topic:DivisibilityRulesForRemainders
* topic:ModularArithmetic
* topic:ChineseRemainderTheorem
* topic:NumTheoryInequalityLargeIntervals
* topic:ExhaustionMethod

</small>



## Atrisinājums

* Piecīgam skaitlim ciparu summa: 
$$100\cdot(2+3+4+5+6) = 100\cdot{}20=2000.$$
* Piecīgs skaitlis $P$, dalot ar $5$, dod atlikumu $2$. 
* Skaitļi $2P,3P,4P$ dos attiecīgi atlikumus
$4,6,1$ ($5P$ būs jau vairāk kā $500$ ciparu.)

*Secinājums.* Ja $M$ dalās ar piecīgu skaitli $P$, tad 
$M/P = 1$ (jo dalījumus $2,3,4$ iegūt nevar - pretruna ar atlikumiem, 
kādus var dot $P$ daudzkārtņi). 



Vai piecīga skaitļa daudzkārtnim beigās var būt cipari "81"?

* Ja $N=\overline{M81}$, tad arī $N$ ciparu summa $2009$ dod atlikumu 
$2$, dalot ar $9$. 
* Lai $N$ dalītos ar piecīgu skaitli $P$, tad $N=k\cdot{}P$, kur
$k$ dod atlikumu $1$, dalot ar $9$.
* Lai $k\cdot{}P=N$ varētu beigties ar ciparu $1$, vajag, lai $P$ 
beidzas ar ciparu $3$ (cipars $5$ neder) un $k$ beidzas ar ciparu 
$7$ jeb dod atlikumu $7$, dalot ar $10$

Rakstām kongruenču sistēmu. 
Ja $N=\overline{M81}$ un $N=kP$, kur $M,P$ abi ir piecīgi skaitļi, 
tad:

$$\left\{ \begin{array}{ll}
k \equiv 1 & (\mbox{mod}\,9)\\
k \equiv 7 & (\mbox{mod}\,10)
\end{array} \right.$$

Vajadzīgos atlikumus, dalot ar $9$ un $10$ dod šī progresija:
$37, 127, 217, 307,\ldots$. Reizinātājs $k=307$ ir par lielu: 
reizinot pat mazāko piecīgo skaitli $P=\overline{222\ldots}$
rezultāts sāksies ar cipariem "68" (t.i. vairs nebūs piecīgs).


*#ExhaustiveSearch*  
Ja $k=37, 127, 217$, tad reizinot tos ar jebkādiem 
piecīga skaitļa $P$ pēdējiem cipariem (kur pats pēdējais 
cipars ir "3"), neiegūstam beigās ciparus "81":

| $k$             | $37$         | $127$      | $217$      |
| --------------- | ------------ | ---------- | ---------- |
| $P=\ldots{}23$  | $\ldots{}51$ | $\ldots21$ | $\ldots91$ |
| $P=\ldots{}33$  | $\ldots{}21$ | $\ldots91$ | $\ldots61$ |
| $P=\ldots{}43$  | $\ldots{}91$ | $\ldots61$ | $\ldots31$ |
| $P=\ldots{}53$  | $\ldots{}61$ | $\ldots31$ | $\ldots01$ |
| $P=\ldots{}63$  | $\ldots{}31$ | $\ldots01$ | $\ldots71$ |




