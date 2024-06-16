# 1.Daļa: SKAITĻU DALĀMĪBA

## Dalītāji un dalāmība

Viens no galvenajiem skaitļu teorijas jēdzieniem ir skaitļu dalāmība.

**Definīcija:**
Saka, ka vesels skaitlis $m$ dalās ar veselu skaitli $n$, jeb $n$ ir $m$ dalītājs, 
ja eksistē tāds vesels skaitlis $k$, kuram $m = n \cdot k$. 
To pieraksta šādi $m \mathrel{\vdots} n$ jeb $n \mid m$.

**Dalāmības īpašības:**	

**D1.** Ja $a \mid b$ un $a \mid c$, tad $a \mid b+c$ un $a \mid b-c$;  
**D2.** Ja $a \mid b$, tad $a \mid b \cdot k$;  
**D3.** Ja $a \mid b_1$, $a\mid b_2$, $\ldots$, $a \mid b_n$, 
tad $a \mid \left(b_1k_1 + b_2k_2 + \cdots + b_nk_n \right)$;  
**D4.** Ja $a \mid b$ un $b \mid c$, tad $a \mid c$;  
**D5.** Ja $a \mid x$ un $b \mid y$, tad $ab \mid xy$;  
**D6.** Ja $a,b \in \mathbb{N}$, $a \mid b$ un $b \mid a$, tad $a =b$.


## Dalīšana ar atlikumu

**Definīcija:**
Izdalīt veselu skaitli $m$ ar naturālu skaitli $n$ ar atlikumu 
nozīmē uzrakstīt skaitli formā $m=nq+r$, turklāt $q$ un $r$ 
ir veseli skaitļi, un $0 \leq r \leq n-1$.

Praktiski dalīšanu ar atlikumu izpilda kā parastu dalīšanu, 
tikai šo procesu pabeidz, tiklīdz atlikums kļūst mazāks par dalītāju.

Mēs parasti neuzdodam sev jautājumu, vai vienmēr var izdalīt ar atlikumu 
un vai atlikums nosakāms viennozīmīgi. 

**Teorēma:** 
Jebkuram veselam skaitlim $m$ un jebkuram naturālam skaitlim $n$ 
eksistē tieši viens veselu skaitļu pāris $(q,r)$, kuram izpildās nosacījumi:
$$m = q \cdot n + r,\;\;0 \leq r < n.$$


**Pierādījums.** 

* **Eksistence (Izdalīt ar atlikumu vienmēr var).**  
  Ar $q$ apzīmēsim lielāko veselo skaitli, 
  kurš nepārsniedz $\frac{m}{n}$; tad  $q \leq \frac{m}{n} < q+1$ un $qn \leq m < qn+n$. 
  Ar $r$ apzīmēsim skaitli $m-qn$; tātad $m = q \cdot n + r$. 
  No nevienādībām $qn \leq m < qn+n$ seko, ka $0 \leq r < n$.

* **Unitāte (Izdalīt ar atlikumu var tikai vienā veidā).**  
  Pieņemsim, ka to pašu skaitli $m$ var izteikt divos dažādos veidos: 
  $$\left\{ \begin{array}{ll}
  m = q_1 \cdot n + r_1, & 0 \leq r_1 < n\\
  m = q_1 \cdot n + r_1, & 0 \leq r_1 < n.\\
  \end{array} \}$$
	
  Atņemot no pirmās vienādības otro, iegūstam:

  $$0 = (q_1 - q_2) \cdot n + (r_1 - r_2)\;\;\text{jeb}\;\; (q_2 - q_1) \cdot n = (r_1 - r_2).$$

  Tātad $r_1 - r_2$ dalās ar $n$. Tā kā $|r_1 - r_2 | < n$, tad 
  $r_1 - r_2 = 0$ un tādēļ arī $r_1 = r_2$ un $q_1 = q_2$.  
  Unitāte pierādīta.



## LKD un MKD 

Pievērsiet īpašu  uzmanību LKD un MKD definīcijām. Tās atšķiras no  
no skolas programmas. Šajās definīcijās neizmanto attiecības  
"lielāks" un "mazāks", tikai dalāmības attiecību. 
Šīs definīcijas var izmantot, lai ieviestu LKD un MKD jēdzienus arī 
situācijās, kad objekti nav salīdzināmi. 
(Piemēram, var tādā pašā veidā definēt arī LKD vai MKD diviem polinomiem kaut 
arī polinomi nav salīdzināmi tāpat kā skaitļi.)

**Definīcija:** Veselu skaitli $d$ sauc par veselu skaitļu $a$ un $b$ 
*lielāko kopīgo dalītāju* un apzīmē $d = \operatorname{gcd}(a, b)$, 
ja izpildās sekojošas īpašības:
	
1. $d \mid a$ un $d \mid b$;
2. ja $t$ ir tāds vesels skaitlis, ka $t \mid a$ un $t \mid b$, tad $t \mid d$.


**Definīcija:** 
Veselu skaitli $m$ sauc par veselu skaitļu $a$ un $b$ mazāko kopīgo dalāmo 
un apzīmē $\operatorname{lcm}(a, b)$, ja tam izpildās sekojošas īpašības:

1. $a \mid m$ un $b \mid m$;
2. ja $s$ ir tāds vesels skaitlis, ka $a \mid s$ un $b \mid s$, tad $m \mid s$.

Izmantojot definīcijas, var pierādīt, ka skaitļu LKD un MKD ir noteikti viennozīmīgi, 
ja neņem vērā skaitļu zīmi. Taču LKD un MKD eksistence, ievērojot doto definīciju, 
ir pietiekami sarežģīts apgalvojums. Eksistences pierādījums ir saistīts ar 
Eiklīda algoritmu – metodi, kas aprēķina skaitļu 
(un ne tikai skaitļu, bet, piemēram, arī polinomu) lielāko kopīgo dalītāju.

**LKD īpašības:**

1. $\operatorname{gcd}(a,b) = \operatorname{gcd}(b,a)$,
2. $\operatorname{gcd}(a,b) = \operatorname{gcd}(a, b+ka)$,
3. $\operatorname{gcd}(a,b,c) = \operatorname{gcd}(\operatorname{gcd}(a,b),c)$,
4. $\operatorname{gcd}(ta,tb) = t \cdot \operatorname{gcd}(a,b)$,
5. $\operatorname{gcd}(a,b) \cdot \operatorname{lcm}(a,b) = a \cdot b$.
6. Ja $\operatorname{gcd}(x,y) = 1$, $x \mid a$ un $y \mid b$, tad  $xy \mid a$,
7. Ja $\operatorname{gcd}(a,x) = 1$ un $x \mid ab$, tad $x \mid b$.



## Eiklīda algoritms

Doti naturāli skaitļi $a_0$ un $a_1$; pieņemsim, ka $a_0 > a_1$. 
Izdalīsim skaitli $a_0$ ar $a_1$ ar atlikumu: 
$a_0 = a_1q_1 + a_2$, $0 \leq a_2 < a_1$.  
Pēc tam izdalīsim  $a_1$ ar $a_2$ ar atlikumu, atlikumu apzīmēsim ar $a_3$. 
Šo procesu turpināsim, kamēr atlikumā iegūsim $0$. 
Process beigsies, jo virkne $(a_n)$ ir stingri dilstoša nenegatīvu skaitļu virkne. 
Rezultātā  iegūsim šādu sistēmu:  

$$\left\{ \begin{array}{ll}
a_0 = a_1q_1 + a_2, & a_2 < a_1,\\
a_1 = a_2q_2 + a_3, & a_3 < a_2,\\
\ldots & \\
a_{k-2} = a_{k-1}q_{k-1} + a_k, & a_k < a_{k-1},\\
a_{k-1} = a_kq_k. & \\
\end{array} \right\}$$
	
**Teorēma:** Pēdējais nenulles atlikums, ko iegūst, 
realizējot Eiklīda algoritmu ar skaitļiem $a_0$ un $a_1$, 
ir skaitļu $a_0$ un $a_1$ LKD. 
Turklāt, eksistē tādi veseli skaitļi $t$ un $s$, ka $a_k = ta_0 + sa_1$.


## Pirmskaitļi

**Definīcija:**  
Naturālu skaitli $n>1$ sauc par pirmskaitli, ja tam nav citu dalītāju, 
izņemot $1$ un $n$.

**Pirmskaitļu īpašības:**

1.  Naturāls skaitlis $n>1$ nav pirmskaitlis tad un tikai tad, 
    kad eksistē tāds skaitļa $n$ dalītājs $m>1$, kurš nepārsniedz $\sqrt{n}$.
2. *Eiklīda lemma.* Ja $p$ ir pirmskaitlis, un $p \mid ab$, tad $p \mid a$ vai $p \mid b$.
3. Eksistē bezgalīgi daudz pirmskaitļu.
4. *Bertrāna postulāts.* Jebkuram naturālam skaitlim $n \geq 2$ 
   eksistē pirmskaitlis $p$, kurš atrodas intervālā $n < p < 2n$.
5. *Dirihlē teorēma.* Ja $(a,b)=1$, tad eksistē bezgalīgi daudz 
   tādu naturālu skaitļu $n$, ka $an+b$ ir pirmskaitlis.


## Dalāmības pazīmes

Šīs tēmas uzdevumos izmantojamas dalāmības pazīmes ar 
$3$, $9$ un $11$. Tās ir šādas:

* Skaitlis dalās ar $3$, ja tā ciparu summa dalās ar $3$.
* Skaitlis dalās ar $9$, ja tā ciparu summa dalās ar $9$. 
* Skaitlis dalās ar $11$, ja tā ciparu summa, kas atrodas pāra pozīcijās,    
  mīnus ciparu summa, kas atrodas nepāra pozīcijās, dalās ar $11$.


Uzdevumi, kas izmanto dalāmības pazīmes ar $2$, $4$, $8$, $5$, $25$ 
tiks aplūkoti citās tēmās, jo dalāmības pazīmes ar šiem skaitļiem 
izmanto tikai skaitļu pēdējos ciparus. 
Aplūkot skaitļa pēdējos ciparus, nozīmē aplūkot skaitli pēc moduļa $10^n$.




# <lo-sample/> BBK2012.P1.1

Vai eksistē 3 viens otram sekojoši skaitļi, kuru reizinājums ir 
$19941995199620$? 

## Atrisinājums

Nē, neeksistē. Trīs sekojošu naturālu skaitļu reizinājums dalās ar $3$, 
bet dotais skaitlis ar $3$ nedalās, jo tā ciparu summa nedalās ar $3$.


# <lo-sample/> BBK2012.P1.2

Vai $6$ pēc kārtas ņemtu naturālu skaitļu reizinājums var būt $1111140960$? 

## Atrisinājums

Nē, nevar. Sešu pēc kārtas ņemtu naturālu skaitļu reizinājums dalās ar $9$, 
bet dotais skaitlis ar $9$ nedalās.


# <lo-sample/> BBK2012.P1.3

Andris saskaitīja sešus viens otram sekojošus naturālus skaitļus un ieguva rezultātu, 
kurā katrs cipars no $2$ līdz $9$ sastopams vienu reizi, bet cipars $1$ – divas reizes. 
Pierādīt, ka Andris kļūdījās.

## Atrisinājums

Viegli pārbaudīt, ka sešu viens otram sekojošu naturālu skaitļu summa dalās ar $3$, 
bet skaitlis, kurā katrs cipars no $2$ līdz $9$ sastopams vienu reizi, 
bet cipars $1$ – divas reizes ar $3$ nedalās, jo tā ciparu summa $46$ ar $3$ nedalās. 


# <lo-sample/> BBK2012.P1.4

Pierādīt, ka skaitlis $\underbrace{111\ldots{}1}_{\mbox{27 vieninieki}}$
dalās ar $27$. 

## Atrisinājums

Ievērosim, ka izpildās vienādība

$$\underbrace{111\ldots{}1}_{\mbox{27 vieninieki}} = 111 \cdot \underbrace{1001001\ldots{}001}_{\mbox{9 vieninieki}}.$$

No dalāmības pazīmēm ar $3$ un $9$ seko, ka pirmais reizinātājs dalās ar $3$, 
bet otrais ar $9$; tātad viss reizinājums dalās ar $27$.

# <lo-sample/> BBK2012.P1.5


Pierādīt, ka skaitlis $\underbrace{111\ldots{}1}_{\mbox{81 vieninieki}}$ dalās ar $81$. 

## Atrisinājums

Ievērosim, ka

`$$\underbrace{111\ldots{}1}_{\mbox{81 vieninieki}} = 
\underbrace{111\ldots{}1}_{\mbox{9 vieninieki}} \cdot \underbrace{100\ldots{}0100\ldots{}01}_{\mbox{9 vieninieki}}.$$`

Katrs no reizinātājiem dalās ar $9$, jo ciparu summa dalās ar $9$. Tātad reizinājums dalās ar $81$.



# <lo-sample/> BBK2012.P1.6

Visi piecciparu skaitļi no $11111$ līdz $99999$ patvaļīgā secībā 
uzrakstīti viens aiz otra. Pierādiet, ka uzrakstītais skaitlis nav divnieka naturāla pakāpe.

## Atrisinājums

Uzrakstītā skaitļa ciparu summa dalās ar $9$. 
Tātad šis skaitlis dalās ar $9$, un tas nevar būt divnieka pakāpe.


# <lo-sample/> BBK2012.P1.7

Aplūkosim visus deviņciparu skaitļus, kuru decimālajā pierakstā katrs cipars 
no $1$ līdz $9$ uzrakstīti tieši vienu reizi. Nosakiet, kāds ir šo skaitļu 
lielākais kopīgais dalītājs.

## Atrisinājums

Katra šāda skaitļa ciparu summa ir $45$. 
Tātad visi šie skaitļi dalās ar $9$. Tā kā $123456798 - 123456789=9$, 
tad visu doto skaitļu kopīgais dalītājs nevar būt lielāks par $9$.  
Atbilde: doto skaitļu LKD ir $9$.




# <lo-sample/> BBK2012.P1.8

No skaitļa 1985 atņēma tā ciparu summu, no rezultāta – tā ciparu summu, utt.

**(A)** Pierādiet, ka noteikti kādreiz iegūsim viencipara skaitli.
**(B)** Kāds tas būs?

## Atrisinājums

Atņemot no skaitļa tā ciparu summu iegūstam skaitli, 
kas dalās ar $9$. Ja skaitlis nav viencipara, tad tā ciparu summa 
ir mazāka par pašu skaitli; tātad iegūt nulli var iegūt tikai 
no viencipara skaitļa, un rezultātā šajā virknē būs viencipara 
skaitlis, kas dalās ar $9$ – tātad tas būs skaitlis $9$.



# <lo-sample/> BBK2012.P1.9

Reizināšanas pierakstā viens cipars aizstāts ar zvaigznīti.

$$1\ast{}74633 \times 2840332 = 3904414098156.$$ 

Kas tas par ciparu?

## Atrisinājums

Izmantojot dalāmības pazīmes ar $3$ un $9$, noskaidrojam, ka skaitļu 
reizinājums dalās ar $9$, bet otrais reizinātājs nedalās ar $3$. 
Tātad pirmais reizinātājs dalās ar $9$. Tā kā pirmā reizinātāja 
ierakstīto ciparu summa ir $24$, lai tas dalītos ar $9$, zvaigznītes 
vietā ir jāieraksta cipars $3$.


# <lo-sample/> BBK2012.P1.10

Jānis sareizināja visus naturālos skaitļus no $1$ līdz $13$ (ieskaitot) 
un atrada rezultāta otro pakāpi. Iznāca

$$387757880 \ast{} 3632640000,$$

kur viens cipars aizstāts ar zvaigznīti.
Atrodiet, kāds cipars aizstāts ar zvaigznīti.

## Atrisinājums

Jāņa iegūtais reizinājums dalās ar $9$; 
tātad arī tā ciparu summa dalās ar $9$.
Šī ciparu  summa ir $77+\ast$. Lai šī summa dalītos ar $9$, 
ciparam $\ast$ ir jābūt vienādam ar $4$.



# <lo-sample/> BBK2012.P1.11

No skaitļa $1230123012301230$ jāizsvītro vairāki cipari tā, 
lai iegūtais skaitlis dalītos ar $9$ un būtu maksimāli liels. Kuri cipari jāizsvītro? 

## Atrisinājums

Tā kā uzrakstītā skaitļa ciparu summa ir $15$, tad, lai atlikušais skaitlis 
dalītos ar $9$ ir jāizsvītro cipari, kuru summa ir $6$. Protams, lai iegūtu 
lielāko skaitli ir jāizsvītro pēc iespējas mazāk cipari; tātad jāizsvītro 
divi trijnieki.

Tā kā vecākās šķiras ir nozīmīgākas, tad jānosvītro abi pēdējie trijnieki.


# <lo-sample/> BBK2012.P1.12

No nenulles cipariem, katru izmantojot tieši 1 reizi, jāizveido triju trīsciparu 
skaitļu decimālie pieraksti. Vai var gadīties tā, ka

**(A)**  neviens no tiem nedalās ar $3$,  
**(B)**  tie visi dalās ar $3$,  
**(C)**  divi no tiem dalās ar $3$, bet trešais – nē?

## Atrisinājums

**(A)**  Jā, var; piemēram, $125, 368, 479$.

**(B)**  Jā, var; piemēram, $123, 456, 789$.

**(C)**  Nē, nevar. Visu trīs skaitļu ciparu summu summa ir $45$. 
Ja izpildās uzdevuma nosacījumi, tad pirmo divu skaitļu ciparu 
summas dalās ar $3$, bet trešā skaitļa ciparu summa nedalās ar $3$. 
Tas nozīmē, ka visu trīs skaitļu ciparu summu summa nedalās ar $3$, 
bet $45$ ar $3$ dalās.



# <lo-sample/> BBK2012.P1.13

Dots patvaļīgs $1973$-ciparu skaitlis, kurš dalās ar $9$. Šī skaitļa ciparu 
summu apzīmēsim ar $a$; skaitļa $a$ ciparu summu apzīmēsim ar $b$; skaitļa $b$ 
ciparu summu apzīmēsim ar $c$. Ar ko ir vienāds skaitlis $c$?

## Atrisinājums

Ievērosim, ka $a \leq 9 \cdot 1973 = 17757$; 
tātad $b<45$ un $c \leq 12$. 
Tā kā sākotnējais skaitlis dalās ar $9$, tad arī $9 \mid a$, $9 \mid b$, $9 \mid c$. 
Tātad $c = 9$.



# <lo-sample/> BBK2012.P1.14

Atrast vislielāko pozitīvo skaitli, ar kuru dalās katrs skaitlis, 
kas satur visus ciparus (katru tieši vienu reizi).

## Atrisinājums

Meklējamais skaitlis ir $9$. Tiešām, ar 9 dalās visi skaitļi, 
kas satur katru ciparu tieši vienu reizi, jo tā ciparu summa $45$ dalās ar $9$.
Ja $k$ ir skaitlis, ar kuru dalās visi “dažādciparu” skaitļi, 
tad ar $k$ dalās skaitļi $9876543210$ un $9876543201$, 
tātad ar $k$ dalās arī šo skaitļu starpība – skaitlis $9$. Tātad $k \leq 9$.



# <lo-sample/> BBK2012.P1.15

Pierādiet, ka, ja pietiekamā un nepieciešamā dalāmības 
pazīme ar skaitli $n$ nav atkarīga no skaitļa ciparu secības, 
tad $n$ ir vai nu trīs, vai deviņi.

## Atrisinājums

Pieņemsim, ka aplūkota dalāmības pazīme ar skaitli $k$. 
Izvēlēsimies $n$-ciparu skaitli $m$ intervālā 
$[1230\ldots{}0; 1239\ldots{}9]$, kurš dalās ar $k$. 
Tātad $m=\overline{123a_4\ldots{}a_n}$, un $k\mid{}m$. 
Ja dalāmības pazīme nav atkarīga no ciparu secības, 
tad arī skaitļi $\overline{3a_4\ldots{}a_n21}$ un 
$\overline{3a_4\ldots{}a_n12}$ dalās ar $k$. 
Šo skaitļu starpība ir $9$. Tātad $k\mid{}9$, un $k=3$ 
vai $k=9$.



# <lo-sample/> BBK2012.P1.16

Apzīmēsim skaitļa $a$ ciparu summu ar $S(a)$. 
Pierādiet, ka no vienādības $S(a) = S(2a)$ seko, 
ka $a$ dalās ar $9$.

## Atrisinājums

No vienādības $S(a)=S(2a)$ seko, ka $a \equiv 2a \pmod 9$. 
Tātad $a \equiv 0 \pmod 9$, jeb $9\mid{}a$.



# <lo-sample/> BBK2012.P1.17

Skaitli $A$ pareizinot ar $3$, tā ciparu summa nemainās.
Pierādīt, ka $A$ dalās ar $9$.

## Atrisinājums

Apzīmēsim $3A=B$. 
Tā kā $B$ dalās ar $3$, tad arī $B$ ciparu summa $S(B)$ 
dalās ar $3$. Tā kā skaitļu $A$ un $B$ ciparu summas ir vienādas, 
tad arī skaitļa $A$ ciparu summa dalās ar $3$; tātad $A$ dalās ar $3$. 
Tas nozīmē, ka $B$ dalās ar $9$; tātad $B$ ciparu summa $S(B)$ 
dalās ar $9$ un arī skaitļa $A$ ciparu summa dalās ar $9$. 
Tātad $A$ dalās ar $9$.



# <lo-sample/> BBK2012.P1.18

Dots, ka $n$ – kaut kāds naturāls skaitlis. Skaitlim $2^n$ 
atrodam ciparu summu. Iegūtajai summai atkal atrodam ciparu summu, 
utt. Pieņemsim, ka kādreiz iegūsim desmitciparu skaitli. 
Pierādīt, ka tam ir vismaz divi vienādi cipari.

## Atrisinājums

Ja iegūtajam skaitlim visi cipari būtu dažādi, tad to summa būtu 
$0+1+2+\cdots{}+9=45$; t.i., šis skaitlis dalītos ar $9$. 
Bet tad arī skaitlim $2^n$ jādalās ar $9$, taču $2^n$ ar $9$ nedalās.



# <lo-sample/> BBK2012.P1.19

Vai astoņciparu skaitlis, kura decimālais pieraksts ir simetrisks, 
var būt pirmskaitlis?

## Atrisinājums

Simetrisks astoņciparu skaitlis dalās ar 11 pēc dalāmības pazīmes, 
un tas nevar būt pirmskaitlis.



# <lo-sample/> BBK2012.P1.20

Vai četrciparu skaitlis, kura pirmais cipars vienāds ar pēdējo, 
bet otrais ar trešo var būt pirmskaitlis?

## Atrisinājums

Nē, nevar būt, jo šāds skaitlis dalās ar 11. Tiešām

$$\overline{abba} = 1000a + 100b + 10b + a = 1001a + 110b = 11 \cdot (91a + 10b).$$



# <lo-sample/> BBK2012.P1.21

Ar vienādiem burtiem apzīmēti vienādi cipari, ar dažādiem burtiem – dažādi. 
Pierādīt, ka vienādība

$$\text{JĀ}\,\times\,\text{NĒ} \,=\, \text{FFGG}$$

nav pareiza.

## Atrisinājums

Skaitlis  $FFGG$  dalās ar $11$ (dalījums ir $F0G$), 
bet neviens no kreisās puses reizinātājiem ar $11$ nedalās; tā ir pretruna.


# <lo-sample/> BBK2012.P1.22

Pierādiet apgalvojumu: ja skaitlis dalās ar $99$, tad tā ciparu summa 
ir ne mazāka kā $18$.

## Atrisinājums

Apzīmēsim ar $S_1$ dotā skaitļa ciparu summu, kas atrodas nepāra pozīcijās, 
un ar $S_2$ dotā skaitļa ciparu summu, kas atrodas pāra pozīcijās. 
Tā kā dotais skaitlis dalās ar $9$, tad $9 \mid (S_1 + S_2)$; savukārt no tā, 
ka skaitlis dalās ar $11$, seko, ka $11 \mid (S_1 - S_2)$. 
Ja izpildās vienādība $S_1 + S_2 = 9$, tad $S_1 - S_2$ nevar dalīties ar $11$. 
Tātad $S_1 + S_2 \geq 2 \cdot 9 = 18$.


# <lo-sample/> BBK2012.P1.23

Autobusa biļetei ir sešciparu numurs no $000000$ līdz $999999$. 
Kādu biļešu ir vairāk: 
tādu, kuru numuru pirmo trīs ciparu summa ir vienāda ar pēdējo 
trīs ciparu summu, vai tādu, kuru numurs dalās ar $11$?

## Atrisinājums

Vairāk ir tādu biļešu, kuru numuri dalās ar $11$. 
Tiešām, katrai biļetei $\overline{a_1a_2a_3a_4a_5a_6}$, 
kurai izpildās vienādība $a_1 + a_2 + a_3 = a_4 + a_5 + a_6$, 
piekārtosim biļeti $\overline{a_1a_4a_2a_5a_3a_6}$, kuras numurs 
(no dalāmības pazīmes ar $11$) dalās ar $11$. 
Tā kā ne visas biļetes, kuru numuri dalās ar $11$, 
tiek iegūtas šādā veidā (piemēram, biļete $605000$ tā nav iegūta), 
tad vajadzīgais apgalvojums ir pierādīts.


# <lo-sample/> BBK2012.P1.24

Pierādiet, ka skaitlis $\overline{a_1a_2\cdots{}a_{3m}}$ dalās ar $7$
($11$ vai $13$) tad un tikai tad, kad 
skaitlis 

$$\overline{a_1a_2a_3} - \overline{a_4a_5a_6} + \cdots + 
(-1)^{m-1}\overline{a_{3m-2}a_{3m-1}a_{3m}}$$

dalās ar $7$ ($11$ vai $13$).

## Atrisinājums

Tā kā $1000^k \equiv (-1)^k \pmod {1001}$, tad 
$$\overline{a_1a_2a_3\cdots{}a_{3m-2}a_{3m-1}a_{3m}} \equiv \overline{a_1a_2a_3} \cdot 10^{3m-3} + \cdots + \overline{a_{3m-2}a_{3m-1}a_{3m}} \equiv$$
$$\equiv \overline{a_1a_2a_3} \cdot (-1)^{m-1} + \overline{a_4a_5a_6} \cdot (-1)^{m-2} + \cdots + \overline{a_{3m-2}a_{3m-1}a_{3m}} \equiv$$
$$\equiv (-1)^{m-1}\left( \overline{a_1a_2a_3} - \overline{a_4a_5a_6}  + \cdots + (-1)^{m-1}\overline{a_{3m-2}a_{3m-1}a_{3m}}  \right) \pmod {1001}.$$


# <lo-sample/> BBK2012.P1.25

Kuri no sekojošiem skaitļiem ir pirmskaitļi?
Pamatojiet savu atbildi:

**(A)** $1395$;
**(B)** $131313$;
**(C)** $1993$;
**(D)** $1991$.

## Atrisinājums

**(A)**  Nē, jo skaitlis dalās ar $5$.
**(B)**  Nē, jo skaitlis dalās ar $13$.
**(C)**  Jā, $1993$ ir pirmskaitlis.
**(D)**	Nē, jo skaitlis dalās ar $11$.


# <lo-sample/> BBK2012.P1.26

Pierādīt, ka sešciparu skaitlis dalās ar $13$ tādā un 
tikai tādā gadījumā, ja ar $13$ dalās tā pirmo trīs 
ciparu un pēdējo trīs ciparu veidoto skaitļu starpība 
(mazinātājs varētu sākties ar vienu vai vairākām nullēm).

## Atrisinājums

Apgalvojums seko no vienādības
$$\overline{abcdef} = 1000 \cdot \overline{abc} + \overline{def} =$$
$$= 1001 \cdot \overline{abc} + (\overline{def} - \overline{abc}) = 13 \cdot 77 \overline{abc} + (\overline{def} - \overline{abc}).$$
No šejienes redzams, ka $\overline{abcdef}$ dalās ar $13$ tad un tikai tad, kad $(\overline{def} - \overline{abc})$ dalās ar $13$.










# Dalāmības īpašības

Dalāmības īpašības sk. [Jēdziens: dalītājs](Concept-p1.1-divisor.md), 
šeit papildus izmantojam sekojošus apgalvojumus:

* Ja $p$ ir pirmskaitlis un $p \mid ab$, tad $p \mid a$ vai $p \mid b$.
* Ja $a_1 \mid m$, $a_2 \mid m$, $\ldots$, $a_n \mid m$, tad
  $\operatorname{lcm}(a_1,a_2,\ldots,a_n)\,\mid\,m$. 
* Ja $a$ un $b$ ir savstarpēji pirmskaitļi un $a \mid bc$, tad $a \mid c$.

Pirmās un trešās īpašības pierādījumi nebūt nav vienkārši.
To pamatā ir teorēma par Eiklīda algoritmu un šīs īpašība tiks pierādītas otrajā nodaļā. 
Otrā īpašība seko no MKD definīcijas. Taču, rēķinot uzdevumus par skaitļu dalāmību, 
mums pašreiz nav vajadzības zināt aritmētikas pamatteorēmas pierādījumu, 
un tāpēc pagaidām izmantosim šīs īpašības uzdevumu risināšanā, atceroties, 
ka to pierādījumi tiks aplūkoti vēlāk, kad tiks pierādīta aritmētikas pamatteorēma.
Risinot uzdevumus, jāizmanto arī skaitļa sadalījums pirmreizinātājos 
un jāmāk uzrakstīt visi skaitļa dalītāji. Arī šajā gadījumā mēs faktiski 
lietojam aritmētikas pamatteorēmu, kas pagaidām nav pierādīta.

## Jautājumi paškontrolei

Pamatojiet norādītās atbildes.

1. Dots, ka naturāls skaitlis dalās ar $3$ un $4$. Vai šis 
   skaitlis noteikti dalās ar $12$?  
   Atbilde: jā.
2. Dots, ka naturāls skaitlis dalās ar $6$ un $4$. Vai šis skaitlis 
   noteikti dalās ar 24?  
   Atbilde: nē. 
3. Kur ir būtiskā atšķirība starp pirmo un otro jautājumu?  
   Atbilde: $3$ un $4$ ir savstarpēji pirmskaitļi, bet $6$ un $4$ – nē. 
4. Skaitlis $A$ nedalās ar $3$. Vai skaitlis $2A$ var dalīties ar $3$?
   Atbilde: nē.
5. Dots, ka $A$ ir pāra skaitlis. Vai skaitlis $3A$ 
   noteikti dalās ar $6$?  
   Atbilde: jā.
6. Skaitlis $5A$ dalās ar $3$. Vai skaitlis $A$ noteikti 
   dalās ar $3$?  
   Atbilde: jā.
7. Skaitlis $15A$ dalās ar $6$. Vai skaitlis $A$ 
   noteikti dalās ar $6$?  
   Atbilde: nē.





# Dalāmības īpašības: Ievaduzdevumi

# <lo-sample/> BBK2012.P1.E2.1

Dots, ka $5 \mid a$ un $5 \mid b$. Pierādiet, ka 
$5 \mid (a^2 + 7b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$5 \mid a$, tātad $5 \mid a^2$ (īpašība **D2**); 
$5 \mid b$, tātad $5 \mid 7b$ (īpašība **D2**). 
No īpašības **D1** seko, ka $5 \mid (a^2 + 7b)$.



# <lo-sample/> BBK2012.P1.E2.2

Dots, ka $7 \mid a$. Pierādiet, ka $7 \mid (a^2 + 3a + 7b - 21)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$7 \mid a$, tātad $7 \mid a^2$ un $7 \mid 3a$ (īpašība **D2**); 
$7 \mid 7b$ un $7 \mid 21$. No īpašības **D3** seko, ka 
$7 \mid (a^2 + 3a ­+ 7b - 21)$.




# <lo-sample/> BBK2012.P1.E2.3
 
Dots, ka $n \mid a$ un $n \mid (5a + b)$. Pierādiet, ka $n \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$b = (5a + b) - 5a$. Tā kā $n \mid (5a + b)$ un $n \mid 5a$ 
(jo $n \mid a$), tad $n$ ir šo skaitļu starpības dalītājs, t.i., $n \mid b$.



# <lo-sample/> BBK2012.P1.E2.4

Dots, ka $n \mid (a - b)$. Pierādiet, ka $n \mid (a^2 + a - b^2 - b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Izteiksmi $a­^­­­­­­2 + a - b2 - b$ var sadalīt reizinātājos 
$(a - b)(a + b + 1)$. Tā kā $n \mid (a - b)$, 
tad no īpašības **D2** seko, ka $n \mid (a^­­­­­­­2 + a - b^2 - b)$.



# <lo-sample/> BBK2012.P1.E2.5

Dots, ka $n \mid 3a$ un $n \mid (12a + 5b)$. Pierādiet, ka $n \mid 10b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No īpašības **D3** seko, ka $n \mid 5b = (12a +5b) - 4 \cdot 3a$. 
Tātad $n$ dala arī $10b$ (īpašība **D2**).


# <lo-sample/> BBK2012.P1.E2.6

Dots, ka $5 \mid (a - b)$ un $7 \mid (a + b)$. Pierādiet, ka $35 \mid (a^2 - b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No īpašības **D5** seko, ka $5 \cdot 7 = 35 \mid (a-b)(a+b) = a^2 - b^2$.



# <lo-sample/> BBK2012.P1.E2.7

Doti tādi naturāli skaitļi $a, b, c$, ka $a \mid b$, 
$b \mid c$, $c \mid a$. Pierādiet, ka 
$a = b = c$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No tā, ka $b \mid c$ un $c \mid a$ seko, ka $b \mid a$ (īpašība **D4**). 
Tā kā $a \mid b$ un $b \mid a$, tad $a = b$ (īpašība **D6**). 
Līdzīgi pierāda, ka $b = c$.



# <lo-sample/> BBK2012.P1.E2.8

Dots, ka $3 \mid (a - 1)$ un $5 \mid (a+2)$. Pierādiet, 
ka $15 \mid (a^2 + a - 2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Apgalvojums seko no vienādības $a^2 + a - 2 = (a -1)(a + 2)$ un īpašības **D5**.


# <lo-sample/> BBK2012.P1.E2.9

Kuri no skaitļiem $101, 111, 141, 143, 155, 161, 163$ ir pirmskaitļi?

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Visi no dotajiem skaitļiem ir mazāki par $13^2 = 169$. 
Tātad, lai noskaidrotu, vai dotie skaitļi ir pirmskaitļi, 
mums jāpārbauda to dalāmība ar pirmskaitļiem, kuri ir mazāki par 13. 
Tie ir $2$, $3$, $5$, $7$ un $11$. 
Pārbaudot redzam, ka pirmskaitļi ir skaitļi $101$, $141$, $163$.



# <lo-sample/> BBK2012.P1.E2.10

Atrodiet visus pirmskaitļus intervālā $[100, 120]$.

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Tā kā $\sqrt{120} < 11$, tad pietiek pārbaudīt dalāmību ar 
pirmskaitļiem, kas ir mazāki par $11$. Tie ir 2, 3, 5 un 7. 
Vienīgais pāra pirmskaitlis ir $2 \not\in [100, 120]$; tāpēc
pāra skaitļi nav jāaplūko. 
Izrakstīsim visus nepāra skaitļus no $[100;120]$ un pasvītrosim 
tos, kas dalās ar $2$, $3$, $5$ vai $7$: 

$$101, 103, \underline{105}, 107, 109, \underline{111}, 113, \underline{115}, \underline{117}, \underline{119}.$$

Nepasvītrotie skaitļi $101$, $103$, $107$, $109$, $113$ ir pirmskaitļi.


# <lo-sample/> BBK2012.P1.E2.11

Atrodiet visus pirmskaitļus intervālā $[180, 200]$s.

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Dotajā intervālā pirmskaitļi ir skaitļi  $181$, $191$, $193$, $197$ un $199$.
Citi neder, jo $3 \mid 183$, $5 \mid 185$, $11 \mid 187$, 
$3 \mid 189$, $5 \mid 195$ (vai arī ir pāra skaitļi).  

# <lo-sample/> BBK2012.P1.E2.12

Ar kādām naturālām $n$ vērtībām skaitlis $n^2 - 1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Zināms, ka $n^2 - 1 = (n - 1)(n + 1)$. 
Tātad, ja $n - 1 > 1$, tad $n^2-1$ nav pirmskaitlis, jo $n-1$ 
ir tā dalītājs, pie kam $n -1 \neq 1$ un $n-1 \neq n^2 -1$. 
Atliek pārbaudīt $n$ vērtības $n=1$ un $n=2$. 
Ja $n =1$, tad $n^2 - 1 = 0$ nav pirmskaitlis. 
Ja $n = 2$, tad $n^2 - 1 = 3$ ir pirmskaitlis.


# <lo-sample/> BBK2012.P1.E2.13

Dots, ka $5 \mid 12a$. Pierādiet, ka $5 \mid a$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No pirmskaitļu 2.īpašības seko, ka $5 \mid 12$ vai $5 \mid a$. 
Tā kā $\operatorname{gcd}(5, 12) = 1$, tad $5 \mid a$.


# <lo-sample/> BBK2012.P1.E2.14

Dots, ka $7 \mid a$ un $7 \mid (2a + 3b)$. Pierādiet, ka $7 \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No īpašības **D3** seko, ka $7 \mid (2a + 3b) - 2a = 3b$. 
No pirmskaitļu 2 īpašības seko, ka $7 \mid b$.



# <lo-sample/> BBK2012.P1.E2.15

Dots, ka $5 \mid 7b$ un $7 \mid 5a$. Pierādiet, ka $35 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No pirmskaitļu 2.īpašības seko, ka $5 \mid b$ un $7 \mid a$. 
Tātad $35 \mid ab$ (īpašība **D5**).



# <lo-sample/> BBK2012.P1.E2.16

Dots, ka $n \mid (5a + 3b)$ un $n \mid (3a + 2b)$. 
Pierādiet, ka $n \mid a$ un $n \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Pareizinot $5a + 3b$ ar $2$ un $3a + 2b$ ar $3$ un atņemot 
otro izteiksmi no pirmās, iegūsim: $2 (5a + 3b) - 3 (3a + 2b) = a$. 
Tā kā $n \mid (5a + 3b)$ un $n \mid (3a + 2b)$, tad $n \mid a$ 
(īpašība **D3**). Izmantojot vienādību $b = 5 (3a + 2b) - 3 (5a + 3b)$,
pierāda, ka $n \mid b$.



# <lo-sample/> BBK2012.P1.E2.17

Dots, ka $n \mid (3a + 7b)$ un $n \mid (2a + 5b)$. 
Pierādiet, ka $n \mid a$ un $n \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Seko no tā, ka $a = 5 (3a + 7b) - 7 (2a + 5b)$ un 
$b = 3 (2a + 5b) - 2 (3a + 7b)$.




# <lo-sample/> BBK2012.P1.E2.18

Dots, ka $5 \mid (3a + 4b)$ un $5 \mid (2a + 3b)$. 
Pierādiet, ka $25 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$5 \mid a$, jo $a = 3 (3a + 4b) - 4 (2a + 3b)$.   
$5 \mid b$, jo $b = 3 (2a + 3b) - 2 (3a + 4b)$.  
No īpašības **D5** seko, ka $25 \mid ab$.



# <lo-sample/> BBK2012.P1.E2.19

Pierādiet, ka visiem naturāliem $n$ skaitlis 
$n^2 + n + 6$ dalās ar $2$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Viens no skaitļiem $n$ vai $n + 1$ ir pāra skaitlis, 
tāpēc $n^2+ n = n(n + 1)$ dalās ar $2$. Tātad $2 \mid (n^2+ n + 6)$.



# <lo-sample/> BBK2012.P1.E2.20

Dots, ka $n \mid (a - b)$. Pierādiet, ka $n \mid (a^3 + a^2 - b^3 - b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Seko no tā, ka $a^3 + a^2 - b^3 - b^2 = (a^3 - b^3) + (a^2 - b^2)$,   
$(a^3 - b^3) + (a^2 - b^2) = (a - b)(a^2 + ab + b2) + (a - b)(a + b)$.  
Abi saskaitāmie dalās ar $a-b$, tātad arī ar $n$. 


# <lo-sample/> BBK2012.P1.E2.21

Dots, ka $n \mid (a + 2b)$. Pierādiet, ka $n \mid (a^3 + 2a + 8b^3 + 4b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Seko no tā, ka $a^3 + 2a + 8b^3 + 4b = (a^3 + 8b^3) + 2(a + 2b)$,  
$(a^3 + 8b^3) + 2(a + 2b) = (a + 2b)(a^2 - 2ab + 4b^2) + 2(a + 2b)$.  
Abi saskaitāmie dalās ar $a+2b$, tātad arī ar $n$. 



# <lo-sample/> BBK2012.P1.E2.22

Dots, ka daļa $a/b$ ir saīsināma. Vai daļa $(a - b)/(a + b)$ ir saīsināma? 
Un otrādi, ja zināms, ka daļa $(a - b)/(a + b)$ ir saīsināma, 
vai daļa $a/b$ noteikti ir saīsināma?

<small>

* skill:DivisibilityProperties
* questionType:ProveDisprove

</small>

## Atrisinājums

Jā, ir saīsināma. Ja $n \mid a$ un $n \mid b$, tad $n \mid (a - b)$ un 
$n \mid (a + b)$. Apgrieztais apgalvojums neizpildās, jo, 
ņemot, piemēram, $a = 5$ un $b = 3$ redzam, ka daļa $5/3$ 
nav saīsināma, bet daļa $(5 - 3)/(5 + 3)$ ir saīsināma.





# <lo-sample/> BBK2012.P1.E2.23

Dots, ka $11 \mid (3x + 7y)$ un $11 \mid (2x + 5y)$. Pierādiet, ka 
$121 \mid (x^2 + y^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$11 \mid x$, jo $x = 5 (3x + 7y) - 7 (2x + 5y)$ un   
$11 \mid y$, jo $y = 3 (2x + 5y) - 2 (3x + 7y)$.   
Tātad $11^2 \mid x^2$, $11^2  \mid y^2$, un $121 \mid x^2 + 3y^2$.



# <lo-sample/> BBK2012.P1.E2.24

Doti tādi naturāli skaitļi $a,b$, ka $a \mid (a + b)$ un $b \mid (a + b)$.
Pierādiet, ka $a = b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No $a \mid (a + b)$ seko, ka $a \mid b$. Līdzīgi iegūstam, ka $b \mid a$. 
No īpašības **D6** seko, ka $a = b$.




# <lo-sample/> BBK2012.P1.E2.25

Dots, ka $2 \mid (a - 1)$ un $3 \mid (a + 1)$. 
Pierādiet, ka $6 \mid (a^2 + 5)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No dalāmības īpašībām seko, ka $6 \mid (a - 1)(a + 1) = a^2 - 1$. 
Tātad $6 \mid (a^2 + 5)$, jo $a^2 + 5 = (a^2 - 1) + 6$.




# <lo-sample/> BBK2012.P1.E2.26

Dots, ka $6 \mid (a - b)$ un $6 \mid (a + b)$. 
Pierādiet, ka $3 \mid (a^2 + 8b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No tā, ka $6 \mid (a - b)$ seko, ka $6 \mid (a^2 - b^2) = (a - b)(a + b)$. 
No īpašības **D1** seko, ka $6 \mid (a^2 - b^2 + 6b^2) = a^2 + 5b^2$. 
Tā kā $3 \mid 6$, tad arī $3 \mid (a^2 + 5b^2)$.



# <lo-sample/> BBK2012.P1.E2.27

Ar kādām naturālām $n$ vērtībām skaitlis $n^3-1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Zināms, ka $n^3 - 1 = (n - 1)(n^2 + n + 1)$. Tātad, ja $n-1 > 1$, 
tad $n^3-1$ nav pirmskaitlis, jo $n-1$ ir tā dalītājs, pie kam 
$n-1 >1$ un $n-1 < n^3-1$. Atliek pārbaudīt $n$ vērtības $n = 1$ un $n = 2$.
Ja $n=1$, tad $n^3-1 = 0$ nav pirmskaitlis. Ja $n = 2$, 
tad $n^3 - 1 = 7$ ir pirmskaitlis.





# <lo-sample/> BBK2012.P1.E2.28

Ar kādām naturālām $n$ vērtībām skaitlis $n^2+5n+6$ ir pirmskaitlis? 

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Skaitlis $n^2 + 5n + 6 = (n + 2)(n + 3)$ nav pirmskaitlis 
nevienai n vērtībai, jo tas sadalās reizinātājos, kuri ir lielāki par $1$.






# <lo-sample/> BBK2012.P1.E2.29

Ar kādām naturālām $a$ un $b$ vērtībām skaitlis 
$ab + a + b + 1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Izteiksmi $ab + a + b + 1$ sadalām reizinātājos $(a+1)(b+1)$. 
Tātad šis skaitlis nav pirmskaitlis nekādām $a$ un $b$ vērtībām, 
jo abi reizinātāji ir lielāki par $1$.



# <lo-sample/> BBK2012.P1.E2.30

Dots, ka $4 \mid x$ un $3 \mid y$. Pierādiet, ka $12 \mid (xy + 8y + 9x)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$12 \mid xy$, jo $4 \mid x$ un $3 \mid y$ (īpašība **D5**); 
$12 \mid 8y$, jo $4 \mid 8$ un $3 \mid y$; $12 \mid 9x$, 
jo $3 \mid 9$ un $4 \mid x$.  Tātad $12$ dala arī šo skaitļu summu 
$xy + 8y + 9x$.




# <lo-sample/> BBK2012.P1.E2.31

Dots, ka $11 \mid (4a + b)$ un $11 \mid (a+4b)$. Pierādiet, 
ka $11 \mid a$ un $11 \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No uzdevuma nosacījumiem seko, ka skaitlis $4(a + 4b) - (4a +b) = 15b$ 
dalās ar $11$. No pirmskaitļu 2. īpašības izriet, ka $11 \mid b$. 
Līdzīgi pierāda, ka $11 \mid a$.



# <lo-sample/> BBK2012.P1.E2.32

Dots, ka $7 \mid (3a + b)$ un $7 \mid (a + 3b)$. Pierādiet, ka $49 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

$7 \mid (3(a + 3b) - (3a + b)) = 8b$. 
Tātad, $7 \mid b$. Līdzīgi pierāda, ka $7 \mid a$. 
No īpašības **D5** seko, ka $49 \mid ab$.




# <lo-sample/> BBK2012.P1.E2.33

Dots, ka $7 \mid (2a + 3b)$. Pierādiet, ka $7 \mid (a + 5b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No dotā seko, ka $7 \mid 4(2a +3b) = 8a + 12b$. 
Tātad arī skaitlis 
$a + 5b = 8a + 12b - 7(a + b)$ dalās ar $7$.




# <lo-sample/> BBK2012.P1.E2.34

Dots, ka $13 \mid (a + 4b)$. Pierādiet, ka $13 \mid (10a + b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No dotā seko, ka $13 \mid 10(a +4b) = 10a + 40b$. Tātad arī skaitlis 
$10a + b = (10a + 40b) - 39b$ dalās ar $13$.





# <lo-sample/> BBK2012.P1.E2.35

Dots, ka $11 \mid (3a + 7b)$. Pierādiet, ka $11 \mid (4a + 2b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

No dotā seko, ka $11 \mid 5(3a +7b) = 15a + 35b$. 
Tātad arī skaitlis 
$4a + 2b = 15a + 35b - 11(a + 3b)$ dalās ar $11$.




# <lo-sample/> BBK2012.P1.E2.36

Pierādiet, ka skaitlis $4a + 5b$ dalās ar $17$ tad un tikai tad, 
kad skaitlis $7a - 3b$ dalās ar $17$.

<small>

* skill:DivisibilityProperties
* questionType:Prove

</small>

## Atrisinājums

Ja $17 \mid (4a +5b)$, tad arī skaitlis $6(4a +5b) = 24a + 30b$ dalās ar $17$. Tas nozīmē, ka skaitlis $7a - 4b = 24a + 30b - 17(a + 2b)$ dalās ar $17$.
Līdzīgi pierāda apgriezto apgalvojumu.





# <lo-sample/> BBK2012.P1.E2.37

Ar kādām naturālām $n$ un $m$ vērtībām skaitlis 
$(n-m)(n^2+m-1)$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:FindAll

</small>

## Atrisinājums

Nav tādu $n$ un $m$ vērtību. Vērtības $n<m$ dod negatīvu rezultātu un neder.
Ja $n-m=0$, tad $0$ nav pirmskaitlis. 
Ja $n-m \geq 2$, tad izteiksme $(n-m)(n^2+m-1)$ dalās ar $n-m$, pie tam 
$n-m \neq 1$ un $n-m \neq (n-m)(n^2+m-1)$. 

Visbeidzot, ja $n-m=1$, tad $n^2 + m - 1$, tad 
$n^2 + (n-1) - 1 = n^2 + n - 2 = n(n+1) - 2$. Tas vienmēr ir pāra skaitlis, 
jo vismaz viens no $n$ vai $n+1$ ir pāra. Vienīgais pāra pirmskaitlis ir $2$, 
bet $n(n+1) - 2 \neq 2$ nekādam $n$, jo izteiksme $n(n+1)-2$ ir augoša un 
pieņem vērtības $0, 4, 10, 18, \ldots$ pie $n=1,2,3,4,\ldots$. 
Šīs vērtības "pārlec pāri" vērtībai $2$.





# <lo-sample/> BBK2012.P1.E2.38

Atrodiet vismaz vienu naturālu skaitli $n$, 
lai intervālā $[n, n + 10]$ nebūtu neviena pirmskaitļa.


<small>

* skill:DivisibilityProperties
* questionType:FindExample

</small>

## Atrisinājums

Uzdevuma nosacījumus apmierina, piemēram, skaitlis 
$n = 12! +2 = 479001602$. 
Tiešām, ja $1 < k < 13$ , tad $12! + k$ ir salikts skaitlis, 
jo $k$ ir šā skaitļa dalītājs.

Ir arī daudz mazāki atrisinājumi, piemēram $n=114$. 
Intervālā $[114;126]$ nav neviena pirmskaitļa.








# <lo-sample/> BBK2012.P1.27

Ar kādu ciparu beidzas reizinājums

$$11 \cdot 12 \cdot 13 \cdot 14 \cdot 15 \cdot 16 \cdot 17 \cdot 18 \cdot 19 \cdot 20 \cdot 21 \cdot 22 \cdot 23 ?$$

## Atrisinājums

Šis reizinājums dalās ar $10$; tātad tā pēdējais cipars ir $0$.


# <lo-sample/> BBK2012.P1.28

Četrus veselus pozitīvus skaitļus katru dalīja ar 5 ar atlikumu. 
Iegūto atlikumu summa ir $3$. Pierādīt, ka šo četru skaitļu 
reizinājums dalās ar $5$.

## Atrisinājums

Atlikumi ir veseli nenegatīvi skaitļi. Ja četru atlikumu summa ir $3$, 
tad vismaz viens no tiem ir $0$; atbilstošais skaitlis un līdz ar to 
visu skaitļu reizinājums dalās ar $5$.



# <lo-sample/> BBK2012.P1.29

Dalot $1 \cdot 2$  ar $3$, $2 \cdot 3$ ar $4$,
$3 \cdot 4$  ar $5$, atlikumā iegūst $2$. 
Vai vienmēr, dalot divu viens otram sekojošu naturālu 
skaitļu reizinājumu ar nākošo naturālo skaitli, atlikuma iegūst $2$?

## Atrisinājums

Jā, tā notiek vienmēr, jo $(n-2) \cdot (n-1) = n^2 - 3n + 2 = (n-3) \cdot n + 2$. 



# <lo-sample/> BBK2012.P1.30

Pierādīt, ka $2^{1995} + 2^{1996} + 2^{1997} + 2^{1998}$ dalās ar $15$.

## Atrisinājums

No vienādības

$$2^{1995} + 2^{1996} + 2^{1997} + 2^{1998} = 2^{1995} \cdot (1+2+4+8) =  2^{1995} \cdot 15$$

seko, ka dotais skaitlis dalās ar $15$.


# <lo-sample/> BBK2012.P1.31

Dots, ka $a$ un $b$ ir naturāli skaitļi un $a+b = 210$. 
Pierādīt, ka $ab$ nedalās ar $210$. 

## Atrisinājums

Pieņemsim pretējo, ka $a \cdot b$ dalās ar $210$.
Ievērosim, ka $210 = 2 \cdot 3 \cdot 5 \cdot 7$. 
Ar $p$  apzīmēsim jebkuru no pirmskaitļiem $2, 3, 5, 7$. 
Tad $a \cdot b$ dalās ar $p$. 
Tātad vismaz viens no skaitļiem $a$, $b$ dalās ar $p$. 
Tā kā $a + b = 210$ dalās ar $p$, 
tad arī otrs skaitlis dalās ar $p$.
Tātad gan $a$, gan $b$ dalās ar $2 \cdot 3 \cdot 5 \cdot 7 = 210$, 
bet tādā gadījumā $a \geq 210$, $b \geq 210$ un $a + b > 210$. 
Iegūta pretruna.


# <lo-sample/> BBK2012.P1.32

Uz skaitļu ass attēloti vairāki veseli skaitļi, kas ņemti pēc kārtas (skat. 1. zīm.):

![](BBK2012.P1.32.png){ width=300px }

Divi no tiem skaitļiem, kas attēloti ar melniem aplīšiem, dalās ar 3, bet divi – ar 5 (nav zināms, kuri). Norādiet zīmējumā skaitli, kurš dalās ar 15. Pamatojiet savu atbildi.

## Atrisinājums

Skat. zīm.

![](BBK2012.P1.32A.png){ width=300px }

Ja divi skaitļi dalās ar $5$, tad arī to starpība dalās ar $5$. 
No atzīmētajiem skaitļiem tikai skaitļu $C$ un $B$ 
starpība dalās ar $5$ . Nākošais skaitlis aiz $C$, kas dalās ar 
$5$ ir $E$. Tā kā abi atlikušie skaitļi $A$ un $D$ dalās ar $3$, un $E -D = 3$, 
tad arī $E$ dalās ar 3.
Tā kā skaitlis $E$ dalās ar $3$ un $5$, tad dalās arī ar $15$.



# <lo-sample/> BBK2012.P1.33

Doti $6$ stieņi, katrs $50$ cm garš. Vai tos var sagriezt 
gabalos tā, lai rastos $12$ gabali ar garumu $12$ cm katrs, 
$30$ gabali ar garumu $3$ cm katrs un $11$ gabali ar garumu $6$ cm katrs?

## Atrisinājums

Nē. Visu daļu garumi dalās ar $3$, bet $50$ ar $3$ nedalās.


# <lo-sample/> BBK2012.P1.34

**(A)** Vai piecu pēc kārtas ņemtu skaitļu summa var būt $24$?  
**(B)** Vai tā var būt $1984$?  
**(C)** Vai tā var būt $1985$?

## Atrisinājums

Aplūkosim piecu pēc kārtas ņemtu skaitļu summu:

$$S = (n-2) + (n-1) + n + (n+1) + (n+2) = 5n.$$

Tātad šī summa dalās ar $5$ un nevar pieņemt vērtības 
$24$ un $1984$, bet var pieņemt vērtību $1985$.


# <lo-sample/> BBK2012.P1.35

Naturālus skaitļus no $1$ līdz $25$ ieskaitot jāsadala 
vairākās grupās ( katram skaitlim jānonāk tieši vienā grupā) tā, 
lai katrā grupā mazākais skaitlis būtu $8$ reizes mazāks 
par visu citu šīs grupas skaitļu summu.
Vai to var izdarīt?

## Atrisinājums

Saskaņā ar uzdevuma nosacījumiem katrā grupā skaitļu summai jādalās ar $9$; 
tātad visu skaitļu summai arī jādalās ar $9$, 
bet $1 + 2 + 3 + \cdots + 25 = \frac{25 \cdot 26}{2} = 325$ 
nedalās ar $9$. Tas nozīmē, ka to izdarīt nevar.


# <lo-sample/> BBK2012.P1.36

Trīs no aritmētiskās progresijas locekļiem ir $41$, $113$, $193$. 
Atrast lielāko iespējamo diferences vērtību, ja zināms, ka tā ir vesels skaitlis.

<small>

* topic:GcdAndLcm
* questionType:FindOptimal

</small>

## Atrisinājums

Aritmētiskās progresijas locekļu starpības ir tās diferences $d$ daudzkārtņi. 
Tātad $113 - 41 = 72$ un $193 - 113 = 80$ dalās ar $d$. 
Tātad arī $80 - 72$ dalās ar $d$. Tas nozīmē, ka $d \leq 8$. 
Vērtība $d=8$ ir iespējama; aritmētiskā progresija $a_k = 8k+1$ ar diferenci $8$ 
satur visus norādītos skaitļus.








# <lo-sample/> BBK2012.P1.37 

Pierādīt, ka $10a+b$ dalās ar $7$ tad un tikai tad, ja $a-2b$ dalās ar $7$ ($a$ un $b$ ir naturāli skaitļi).

## Atrisinājums

Ja $10a+b$ dalās ar $7$, tad arī $(10a+b) - 7(a+b) = 3(a-2b)$ dalās ar $7$; 
līdz ar to $a-2 b$ dalās ar $7$.

Ja $a-2b$ dalās ar $7$, tad $3(a-2b)+7(a+b) = 10a+b$ dalās ar $7$.


# <lo-sample/> BBK2012.P1.38

Dots, ka $a$ un $b$ --  naturāli skaitļi un gan $3a+4b$, gan $2a+3b$ dalās ar $7$. 
Pierādīt, ka gan $a$, gan $b$ dalās ar $7$.

## Atrisinājums

No tā, ka $3a+4b$ un $2a+3b$ dalās ar $7$, seko, ka
$a+b = (3a+4b)-(2a+3b)$ dalās ar $7$. Līdzīgi iegūstam, ka
$b = (2a+3b) - 2\cdot(a+b)$ dalās ar $7$.

No vienādības $2a = (2a+3b)-3b$ seko, ka $2a$ dalās ar $7$; tātad arī $a$ dalās ar $7$.




# <lo-sample/> BBK2012.P1.39  

Dots, ka $a$ - naturāls skaitlis, $p$ - pirmskaitlis, pie tam $3 a+1$ un $a-8$ dalās ar $p$. Aprēķināt $p$.


## Atrisinājums

No dotā seko, ka arī skaitlis $(3 a+1)-3(a-8)=25$ dalās ar pirmskaitli $p$. Tātad $p=5$.

Jāpamato arī, ka eksistē šāds naturāls skaitlis $a$, kuram $3 a+1$ un $a-8$ dalās ar $5$. 
Var, piemēram, izvēlēties skaitli $a=13$.



# <lo-sample/> BBK2012.P1.40

Naturāli skaitli $a$ un $b$ ir tādi, ka $34a = 43b$.
Vai $a+b$ var būt pirmskaitlis?


## Atrisinājums

No dotā seko, ka $34(a+b) = 34a+34b = 43b+34b = 77b$. Tas nozīmē, ka skaitlis $34(a+b)$ dalās ar $77$.

Tā kā skaitļiem $34$ un $77$ nav kopīgu dalītāju (lielāku par $1$), tad ar $77$ 
dalās skaitlis $a+b$; tātad tas nav pirmskaitlis (tam, piemēram, ir dalītājs $7$, 
kas atšķirīgs no $1$ un paša skaitļa).



# <lo-sample/> BBK2012.P1.41 

Dots, ka $a, b, c$ - dažādi naturāli skaiţ̦li. Kāds lielākais daudzums no skaiţ̦iem 
$a+b, \quad a+c, \quad b+c$ var būt pirmskaitļi?

## Atrisinājums

Ja $a=1, b=2, c=3$, tad veidojas divi pirmskaitļi $a+b=3$ un $b+c=5$. 

Vairāk par diviem pirmskaitļiem nevar būt, jo starp trim skaitļiem $a,b,c$ ir vismaz divi,
kuru paritātes ir vienādas. Šo skaitļu summa dalās ar $2$, un tā nevar būt pirmskaitlis.



# <lo-sample/> BBK2012.P1.42 

Noskaidrojiet  
**(A)** vai visu naturālo skaitļu reizinājums no $1$ līdz $76$ ieskaitot dalās ar $77$;  
**(B)** vai visu naturālo skaitļu reizinājums no $1$ lîdz $100$ ieskaitot dalās ar $101$?

## Atrisinājums

**(A)** Jā, jo šis reizinājums satur gan skaitli $7$, gan $11$.

**(B)** Nē, jo $101$ ir pirmskaitlis; visi reizinātāji ir mazāki par $101$ un nevar 
dalīties ar $101$. Tātad arī reizinājums nedalās ar $101$.



# <lo-sample/> BBK2012.P1.43 

**(A)** Pierādīt, ka katru $499$ pēc kārtas n̦emtu naturālu skaitļu reizinājums dalās ar $1996$.  
**(B)** Vai katru $498$ pēc kārtas n̦emtu naturālu skaitlu reizinājums dalās ar $1996$?


## Atrisinājums

**(A)** Ievērosim, ka $1996 = 499 \cdot 4$. No $499$ pēc kārtas ņemtiem naturāliem 
skaitļiem viens dalās ar $499$; starp jebkuriem $4$ pēc kārtas n̦emtiem naturāliem 
skaitl̦iem viens dalās ar $4$. Tāpēc reizinājums dalās ar $1996$.

**(B)** Tā kā $499$ ir pirmskaitlis, tad $1 \cdot 2 \cdot 3 \cdots \cdots 498$ nedalās ar 
$499$, un, tātad, nedalās arī ar $1996$.




# <lo-sample/> BBK2012.P1.44 

**(A)** atrast kaut vienu $n$ ar īpašību: jebkuru pēc kārtas n̦emtu $n$ naturālu skaiţlu summa dalās ar $1996$,  
**(B)** atrast vismazāko $n$, kam piemīt (A) punktā minētā īpašība.


## Atrisinājums

**(A)** $S=(a+1)+(a+2)+\cdots+(a+n)=n a+\frac{n(n+1)}{2}$. Redzam, ka skaitlim 
$n=1996 \cdot 2 = 3992$ prasītā īpašība izpildās.

**(B)** Pierādīsim, ka tā ir mazākā vērtība, kurai izpildās prasītā īpašība. 
Tiešām, n̦emot $a=1$ un $a=2$, iegūstam, ka 
$\left(2 n+\frac{n(n+1)}{2}\right)-\left(n+\frac{n(n+1)}{2}\right)=n$ 
dalās ar $1996$. Bet skaitlis $n=1996$ neder, jo, ņemot $a=1$, iegūstam summu, kura nedalās ar $1996$.





# <lo-sample/> BBK2012.P1.45

Kāds lielākais pirmskaitlu daudzums var būt sastopams starp $12$ pēc kārtas n̦emtiem naturāliem skaitļiem?

## Atrisinājums

No $2$ līdz $13$ sastopami $6$ pirmskaitļi: $2, 3, 5, 7, 11, 13$.

Pierādīsim, ka vairāk par $6$ pirmskaitļiem būt nevar. No $1$ līdz $12$ ir $5$ pirmskaitļi. 
Ja mazākais, no grupas skaitļiem ir lielāks par $2$, tad katrs pāra skaitlis šajā grupā 
ir salikts skaitlis. Pāra skaitļi katrā grupā ir $6$; tātad grupā nevar būt vairāk par $6$ 
pirmskaitļiem.


# <lo-sample/> BBK2012.P1.46

Zināms, ka dalot skaitlus $2077$ un $100$ ar $a$, iegūti vienādi atlikumi. 
Kādas var būt skaitļa $a$ vērtības?

## Atrisinājums

No dotā seko, ka $a \mid(2077-100)=1977$. Skaitļa $1977$ sadalījums 
pirmreizinātājos ir šāds: $1977=3 \cdot 659$. Tātad $a \in\{1,3,659,1977\}$.


# <lo-sample/> BBK2012.P1.47

Dalot skaitli $1987$ ar $a$, atlikumā ieguva skaitli $9$. Kādas var būt skaitla $a$ vērtības?


## Atrisinājums

No uzdevuma nosacījumiem seko, ka $1987=ak+9$, $a>9$. Tātad $a \mid(1987-9)=2 \cdot 23 \cdot 43$. 
Skaitlis $a$ var būt jebkurš skaitļa $1978$ dalītājs, kurš lielāks par $9$.

*Atbilde:* $a \in\{23,43,46,86,988,1978\}$.


# <lo-sample/> BBK2012.P1.48

Skaitli $1991$ dalot ar $a$, atlikumā iegūst $9$. Kāds var būt $a$?



## Atrisinājums

Tā kā $1991 = ka+9$, tad $ka = 1982 = 2 \cdot 991$, kur abi reizinātāji ir pirmskaitļi. 
Tātad $a \in\{1,2,991,1982\}$. Tā kā $a>9$, tad der tikai skaitļi $991$ un $1982$.


# <lo-sample/> BBK2012.P1.49

Vai dažādu pirmskaitļu apgriezto lielumu summa var būt vesels skaitlis?


## Atrisinājums

Nē, nevar būt. Pien̦emsim pretējo, ka 
$\frac{1}{p_{1}}+\frac{1}{p_{2}}+\cdots+\frac{1}{p_{n}}=m$, $m \in N$. 
Pareizinot vienādību ar skaitli $p_{1} p_{2} \ldots p_{n-1}$, iegūsim vienādību

$$\begin{aligned}
& p_{2} p_{3} \ldots p_{n-1}+p_{1} p_{3} \ldots p_{n-1}+\cdots+\frac{p_{1} p_{2} \ldots p_{n-1}}{p_{n}}= \\
& p_{1} p_{2} \ldots p_{n-1} m
\end{aligned}$$

Redzam, ka skaitlim $p_{1} p_{2} \ldots p_{n-1}$ jādalās ar $p_{n}$, taču tas nav iespējams.

Iegūtā pretruna pierāda, ka pien̦ēmums bija nepareizs.


# <lo-sample/> BBK2012.P1.50 

Naturāls skaitlis $A$, dalot ar $1981$, dod atlikumā $35$, bet, dalot ar $1982$, 
dod atlikumā $13$. Kādu atlikumu dod $A$, dalot ar $14$?


## Atrisinājums

Tā kā skaiţ̦i $1981$ un $35$ dalās ar $7$, tad no pirmā nosacījuma 
$A=1981 \cdot q+35$ seko, ka $7 \mid A$. Otrais nosacījums $A=1982 \cdot q+13$ 
norāda, ka $A$ ir nepāra skaitlis. Tātad, dalot skaitli $A$ ar $14$, atlikumā iegūsim $7$.


# <lo-sample/> BBK2012.P1.51

Doti $12$ pēc kārtas n̦emti naturāli skaitl̦i. Pierādiet, ka vismaz viens 
no tiem ir mazāks par savu dalītāju summu. (Tiek ņemti skaița naturālie 
dalītāji, kas mazāki par pašu skaitli).


## Atrisinājums

No $12$ pēc kārtas ņemtiem skaitliem var izvēlēties tādu skaitli $n$, kurš dalās ar $12$. 
Tādā gadījumā $\frac{n}{2}, \frac{n}{3}, \frac{n}{4}$ ir skaiț̣a $n$ dalītāji, kuru summa 
$\frac{n}{2}+\frac{n}{3}+\frac{n}{4}=\frac{13}{12} n$ ir lielāka par $n$.




# <lo-sample/> BBK2012.P1.52

Vai iespējams norādīt tādu galīgu skaitu ģeometrisko progresiju, 
kuru locekļi ir naturāli skaitļi, ka jebkurš naturāls skaitlis 
piederētu vismaz vienai progresijai?


<small>

* topic:GeometricSeriesGaps
* questionType:ProveDisprove

</small>


## Atrisinājums

Nē, tādas ǵeometriskas progresijas neeksistē. Aplūkosim galīgu skaitu geometrisko progresiju

$$\left\{a_{1} q_{1}^{k}\right\},\,\left\{a_{2} q_{2}^{k}\right\},\,\ldots,\,\left\{a_{n} q_{n}^{k}\right\},\quad{}k \in \mathbb{N}$$

un n̦emsim visus skaitļu $a_{1}, a_{2}, \ldots, a_{n}, q_{1}, q_{2}, \ldots, q_{n}$ pirmreizinātājus. 
Izvēlēsimies tādu pirmskaitli $p$, kurš nepieder norādītajai kopai. Skaidrs, ka šis skaitlis 
nevar piederēt nevienai no dotajām ǵeometriskajām progresijām.




# <lo-sample/> BBK2012.P1.53

**(A)** Atrast mazāko naturālo skaitli, kuru

* dalot ar $2$, iegūst atlikumā $1$;
* dalot ar $3$, iegūst atlikumā $2$;
* dalot ar $4$, iegūst atlikumā $3$;
* dalot ar $5$, iegūst atlikumā $4$;
* dalot ar $6$, iegūst atlikumā $5$.

**(B)** Atrast mazāko naturālo skaitli, kuru dalot ar $n, n+1, \ldots, n+m$, 
iegūst atlikumā atbilstoši $r, r+1, \ldots, r+m$.

## Atrisinājums

**(A)** Ja $a$ ir meklētais skaitlis, tad $a+1$ dalās ar 2, 3, 4, 5, 6. Tātad $a+1=[2,3,4,5,6]=60$ un $a=59$.

**(B)** Līdzīgi pierāda, ka $x=[r, r+1, \ldots, r+m]+r-n$.






# <lo-sample/> BBK2012.P1.54

Noteikt, kāds varēja būt mazākais kokosriekstu skaits, ko savāca pieci jūrnieki 
uz neapdzīvotas salas, ja viṇi dalīja kokosriekstus šādi: pirmais no viņiem, 
kamēr pārējie gulēja, iedeva vienu riekstu pērtiķim un paņēma sev $\frac{1}{5}$ 
no atlikušajiem riekstiem; tālāk tieši tāpat pēc kārtas rīkojās visi pārējie jūrnieki. 
Pēc tam visi kopā vēl vienu reizi dalīja riekstus: Vienu iedeva pērtiķim, 
bet pārējos sadalīja savā starpā piecās vienādās daļās.

## Atrisinājums

Pievienosim sākotnējai riekstu kaudzei $4$ viltus riekstus. Tad šo kaudzi pirmais jūrnieks 
var sadalīt $5$ vienādās daļās. Šo procesu var atkārtot $6$ reizes. Tātad 
$\left(\frac{4}{5}\right)^{6} \cdot a$ ir vesels skaitlis. Mazākā iespējamā $a$ vērtība ir 
$5^{6}$. Tas nozīmē, ka mazākais iespējamais kokosriekstu skaits sākumā bija $5^{6}-4$.



# <lo-sample/> BBK2012.P1.55

Dots, ka $a, b, c$ - naturāli skaitļi. Cik daudzi no skaitliem $a+b$, $a+c$, $b+c$ 
var vienlaikus dalîties ar $3$?

## Atrisinājums

Jebkurš skaitlu daudzums no $0$ līdz $3$. Piemēri:

$$(1,4,7),\,(1,3,6),\,(1,2,5),\,(3,6,9).$$




# <lo-sample/> BBK2012.P1.56

Atrast kaut vienu veselu skaitli $n$, kas apmierina divas šādas īpašības:

a. $n$ nedalās ne ar vienu no skaițiem $2,3,4,5,6,7,8,9,10$,
b. $n-1$ dalās ar katru no skaitļiem $2,3,4,5,6,7,8,9,10$.

## Atrisinājums

Ja skaitlis $n-1$ dalās ar katru no skaitliem $2,3,4,5,6,7,8,9,10$, tad skaitlis $n$ nedalās 
ne ar vienu no šiem skaiţliem. Skaitli $n-1$ var izvēlēties kā norādīto skaiţu mazāko 
kopīgo dalāmo (protams, var ņemt arī doto skaitlu reizinājumu).

$$\operatorname{MKD}(2,3,4,5,6,7,8,9,10)=2^{3} \cdot 3^{2} \cdot 5 \cdot 7=2520.$$

Tātad der skaitlis $n=2521$.




# <lo-sample/> BBK2012.P1.57

Kāds ir lielākais daudzums pēc kārtas n̦emtu naturālu trīsciparu skaitlu, 
no kuriem nevienu nevar izsacìt kā divu (dažādu vai vienādu) divciparu skaitļu reizinājumu?


## Atrisinājums

Starp $10$ pēc kārtas ņemtiem trīsciparu skaițiem viens dalās ar $10$; tātad šis skaitlis 
$\overline{ab0} = \overline{ab} \cdot 10$ ir divu divciparu skaitlu reizinājums.

No otras puses var uzrādīt $9$ pēc kārtas ṇemtus skaitlus $101, 102,\ldots, 109$, 
kas nav divu divciparu skaiţ̦u reizinājumi (tiešām, vienam no šiem reizinātājiem būtu 
jābūt ne lielākam par $\sqrt{109}$; vienīgais šāds divciparu skaitlis ir $10$, 
bet dotie skaitlii ar $10$ nedalās).

Tātad lielākais meklējamo skaitlu skaits ir $9$.



# <lo-sample/> BBK2012.P1.58

Vai iespējama vienādība $a,bc=\overline{ab}: c$ ?

*Piezīme:* $a,bc$ ir decimāldala ar ciparu $a$ pirms komata un cipariem $b$ un $c$ aiz komata; 
$\overline{ab}$ ir divciparu skaitlis.

## Atrisinājums

Doto vienādību var pārrakstīt šādi: $a+0.1b+0.01c = (10a+b):c$. Pareizinot vienādību ar 
$100c$, iegūstam $100ac + 10bc + c^{2} = 1000a + 100b$; tātad $c$ dalās ar $10$, 
bet tas nav iespējams, jo $c$ ir cipars, kas nav $0$.




# <lo-sample/> BBK2012.P1.59

Ar $\overline{xyz}$ apzīmēsim trīsciparu skaitli ar cipariem $x,y,z$. 
Pierādīt, ka, ja $\overline{abc}$ dalās ar $37$, tad arī 
$\overline{bca}+\overline{cab}$ dalās ar $37$.


## Atrisinājums

Ievērosim, ka

$$\begin{aligned}
& \overline{a b c}+\overline{b c a}+\overline{c a b}= \\
& (100 a+10 b+c)+(100 b+10 b+a)+(100 c+a+b)= \\
& 111 \cdot(a+b+c)=3 \cdot 37 \cdot(a+b+c)
\end{aligned}$$

Tātad $\overline{bca} + \overline{cab} = 3 \cdot 37 \cdot(a+b+c)-\overline{abc}$
dalās ar $37$.




# <lo-sample/> BBK2012.P1.60

Atrast visus divciparu skaitlus, kuru summa ar skaitli, kas pierakstitts ar tiem pašiem cipariem 
otrādā kārtībā, ir naturāla skaiţ̦a kvadrāts.


## Atrisinājums

Apzīmēsim meklējamo skaitli ar $\overline{ab}$. Tad

$$\overline{ab} + \overline{ba} = (10a+b) + (10b+a) = 11(a+b) = n^{2}.$$

Tas nozīmè, ka $n$ dalās ar $11$; tāpēc $11(a+b)$ dalās ar $121$. Tas nozīmē, 
ka $a+b$ dalās ar $11$. Tā kā $a$ un $b$ ir cipari, tad $a+b=11$. Visi šādi skaitli der, 
jo rezultātā iegūstam skaitli $121=11^{2}$.

*Atbilde:* $29, 38, 47, 56, 65, 74, 83, 92$.




# <lo-sample/> BBK2012.P1.61

Atrast visus naturālos divciparu skaitlus, kam piemīt īpašība: šī skaiț̣a un skaiţ̦a, 
kuru iegūst mainot tā ciparus vietām, starpība ir kāda naturāla skaiţ̦a kvadrāts.


## Atrisinājums

Dots, ka $\overline{ab} - \overline{ba} = n^{2}$. 
Tātad $n^{2}=\overline{ab}-\overline{ba} = 9 \cdot(a-b)$. 
Tas nozīmē, ka $n$ dalās ar $3$ un $a-b=k^{2}$.

Iegūstam šādus skaiţ̦us: (neskaitot skaitļus, kuru pierakstā ir $0$):

$$\begin{aligned}
& 12,23,34,45,56,67,78,89,98,87,76.65,54,43,32,21 \\
& 15,26,37,48,59,95,84,73,62,51. \\
\end{aligned}$$






# <lo-sample/> BBK2012.P1.62

Atrisināt pirmskaiţ̦os vienādojumu

$$x^{3}-y^{3}=z.$$



## Atrisinājums

No vienādības $(x-y) \cdot\left(x^{2}+x y+y^{2}\right)=z$
seko, ka $x-y=1$, jo $z$ ir pirmskaitlis. Tā kā $x$ un $y$ arī ir pirmskaitļi 
un ir tikai viens pāra pirmskaitlis $2$, tad $x=3$ un $y=2$. Atliek pārbaudīt, ka 
$3^{3}-2^{3}=19$ arī ir pirmskaitlis.






# <lo-sample/> BBK2012.P1.63

Doti četri naturāli skaiţ̧i $a, b, c, d$, kuri ir savstarpēji pirmskaitļi ar skaitli 
$m = ad - bc$. Pierādiet, ka visām veselām $x$ un $y$ vērtībām, kurām $ax + by$ 
dalās ar $m$, skaitlis $cx + dy$ arī dalās ar $m$.


## Atrisinājums

Uzrakstīsim sekojošu identitāti

$$d(ax+by) - b(cx+dy) = x(ad-bc) = xm.$$

Tātad, ja $m \mid (ax+by)$, tad $m \mid b(cx+dy)$. Nemot vērā, ka $(m,b)=1$, 
iegūsim, ka $m \mid(cx+dy)$.





# <lo-sample/> BBK2012.P1.64

Doti tādi veseli skaiţ̦i $u$ un $v$, ka $u^{2}+u v+v^{2}$ dalās ar 9. 
Pierādiet, ka abi skaitlii $u$ un $v$ dalās ar $3$.


## Atrisinājums

Dots, ka skaitlis $u^{2}+uv+v^{2} = (u-v)^{2} + 3uv$ dalās ar $9$. No šejienes seko, ka

$$3 \mid (u-v)^{2},\quad 3 \mid (u-v)\quad \text{un} \quad 9 \mid (u-v)^{2}.$$

Tādā gadījumā $9 \mid 3uv$ un $3 \mid uv$. Redzam, ka vismaz viens no skaitļiem 
$u$ un $v$ dalās ar 3, bet n̦emot vērā, ka $u$ un $v$ starpība dalās ar $3$, 
iegūstam, ka abi skaitļi $u$ un $v$ dalās ar $3$.




# <lo-sample/> BBK2012.P1.65

Pierādiet, ka naturāls skaitlis $n$ ir pirmskaitlis tad un tikai tad, kad eksistē viens vienīgs 
skaitļu pāris $(x, y)$, kuram izpildās vienādība $\frac{1}{x}-\frac{1}{y}=\frac{1}{n}$.


## Atrisinājums

Pien̦emsim, ka $\frac{1}{x}-\frac{1}{y}=\frac{1}{n}$. Tad $x<n$ un $n \neq 1$. Apzīmēsim 
$x=n-i$ ($0<i<n$). Ievietojot dotajā vienādībā, iegūsim vienādību

$$\frac{1}{n-i}-\frac{1}{n}=\frac{1}{y},\quad \text{jeb}\quad y=\frac{n(n-i)}{i}.$$

Skaidrs, ka vienmēr eksistē viens atrisinājums $i=1, x=n-1, y=n(n-1)$. tam atbilst identitāte

$$\frac{1}{n-1}-\frac{1}{n(n-1)}=\frac{1}{n}.$$

Ja $n$ ir pirmskaitlis, tad $(n, i)=1$, un no tā, ka $i \mid n(n-i)$ seko, ka 
$i \mid(n-i)$ un $i \mid n$ , jeb $i=1$. Tātad šajā gadījumā citu atrisinājumu nav.

Ja $n$ nav pirmskaitlis, tad $n=n_{1}n_{2}$, un mēs varam uzrakstīt vēl citu atrisinājumu 
$i=n_{1}, x=n-n_{1}, y=\left(n-n_{1}\right) n_{2}$.





# <lo-sample/> BBK2012.P1.66

Atņemot no divciparu skaița $\overline{ab}$ divciparu skaitli $\overline{ba}$, ieguva naturāla 
skaiţ̦a kubu. Atrast visus tādus skaiţlus, kuriem izpildās šāda īpašība.



## Atrisinājums

Tā kā $\overline{ab} - \overline{ba} = (10a+b) - (10b+a) = 9(a-b)$ dalās ar $9$, 
tad iegūtais kvadrāts varēja būt $9$, $36$ vai $81$. No šejienes seko, ka $a-b=1, a-b=4$ vai $a-b=9$.

*Atbilde:* $21, 32, 43, 54, 65, 76, 87, 98, 51, 62, 73, 84, 95$.





# <lo-sample/> BBK2012.P1.67

Pirmo $n$ naturālo skaitlu summa ir trīsciparu skaitlis, kuram visi cipari ir vienādi. Atrast skaitli $n$.


## Atrisinājums

Uzdevuma nosacījumu pierakstīsim šādi:

$$1+2+\cdots+n=\overline{k k k} ; \quad \frac{n(n+1)}{2}=k \cdot 3 \cdot 37, \quad 0<k \leq 9$$

Viens no skaitļiem $n$ vai $n+1$ dalās ar 37, bet tā kā $\frac{73 \cdot 74}{2}>999$, 
tad $n=37$ vai $n+1=37$. Ja $n=37$, tad $n+1=38$, un šo skaiţ̦u reizinājums nedalās ar $3$. 
Atliek vērtība $n=36$. Šajā gadījumā iegūstam prasīto vienādību

$$1+2+\cdots+36=666.$$






# <lo-sample/> BBK2012.P1.68

Zināms, ka divu dotu racionālu skaitlu summa un reizinājums ir veseli skaitli. 
Pierādīt, ka dotie skaitļi paši ir veseli.
Vai apgalvojums paliek spēkā, ja nav zināms, ka dotie skaitļi ir racionāli?


## Atrisinājums

Apzīmēsim dotos skaitlus ar $x$ un $y$. Tad

$$\left\{ \begin{array}{l}
x + y = n\\
xy = m
\end{array} 
\quad \Rightarrow \quad
x + \frac{m}{x} = n
\quad \Rightarrow \quad
x^2 + m = nx.$$

Pien̦emsim, ka $x=\frac{p}{q}$ nesaīsināma daļa un $q>1$. 
Pēc pārveidojumiem iegūstam vienādību $p^{2} = q(np-qm)$.

Šī vienādība nav iespējama, jo vienādības labās puses izteiksme dalās ar $q$, bet 
kreisās puses izteiksme nedalās ($p$ un $q$ nav kopīgu dalītāju). 
Tātad $x$ (un līdz ar to arī $y$) ir veseli skaitļi.

Iracionāliem skaitliem apgalvojums nav spēkā. Piemēram, skaitļiem

$$x=2+\sqrt{2}, \quad y=2-\sqrt{2}$$

gan summa, gan reizinājums ir veseli skaitļi.




# <lo-sample/> BBK2012.P1.69

Naturālu skaitli sauc par interesantu, ja tā ciparu summa dalās ar $5$.

**(A)** Atrast kaut vienu tādu interesantu $x$, ka ari $x+9$ ir interesants,  
**(B)** Cik pavisam ir tādu interesantu $x$, kādi minēti (A) punktā?  
**(C)** Pierādīt: starp jebkuriem 9 pēc kārtas n̦emtiem naturāliem skaitliem ir vismaz viens interesants.


## Atrisinājums

**(A)** Tāds, piemēram, ir skaitlis $5$.

**(B)** Tādu skaitļu ir bezgalīgi daudz. Piemēram, tādi ir skaiţ̦i $55 \ldots 505$.

**(C)** Sauksim par bloku desmit pēc kārtas ņemtus skaitlus 
$\overline{n0}, \overline{n1}, \ldots, \overline{n9}$.  
No $9$ pēc kārtas ņemtiem naturāliem skaitliem vismaz $5$ pieder vienam blokam; 
šo skaitlu ciparu summas ir pēc kārtas n̦emti naturāli skaitļi, 
tāpēc viena no tām dalās ar $5$.





# <lo-sample/> BBK2012.P1.70

Atrodiet divciparu skaitli, kurš ir vienāds ar otrā cipara kvadrāta un pirmā cipara summu.



## Atrisinājums

Apzīmēsim meklējamo skaitli ar $\overline{ab}$. Tad $10a+b = a+b^{2}$, jeb $9a=b^{2}-b$. 
Tāpēc $b(b-1)$ dalās ar $9$. Tas ir iespējams tikai, ja cipars $b$ ir $9$.

*Atbilde:* meklējamais skaitlis ir $89$.




# <lo-sample/> BBK2012.P1.71

Atrodiet trīsciparu skaitli, kuru kāpinot jebkurā naturālā pakāpē, iegūstam skaitli, 
kura pēdējie trīs cipari veido sākotnējo skaitli.


## Atrisinājums

Apzīmēsim meklējamo skaitli ar $N$. Tad $1000 \mid \left(N^{2}-N\right)$ un
$8 \cdot 125 \mid (N-1) \cdot N$.

Tā kā $N$ un $N-1$ ir savstarpēji pirmskaiţ̦i, un neviens no tiem nevar dalīties ar 
$8 \cdot 125$, tad pastāv divas iespējas:

a. $8 \mid N$ un $125 \mid(N-1)$, jeb $N=376$;
b. $125 \mid N$ un $8 \mid(N-1)$, jeb $N=625$.

Tā kā jebkuram naturālam $k \quad N^{k}-N=N\left(N^{k-1}-1\right)$ dalās ar $N(N-1)$, 
tad abas iegūtās $N$ vērtības apmierina uzdevuma nosacījumus.





# <lo-sample/>BBK2012.P1.72

Atrodiet visas tādas naturālu skaitļu virknes $(a_n)$, 
kurām izpildās sekojošas īpašības:

a. visiem naturāliem $n$, $a_n \leq n\sqrt{n}$,  
b. visiem naturāliem $m$ un $n$ starpība $a_m - a_n$ dalās ar $m-n$.

<!--
questionType=FindAll
concepts=square-root
-->


## Atrisinājums

No dotā seko, ka $a_{1}=1, a_{2}=1$ vai $2$. Aplūkosim abus gadījumus:

a. $a_{1}=1, a_{2}=1$; tad $(n-1) \mid \left(a_{n}-1\right)$ un 
   $(n-2) \mid\left(a_{n}-1\right)$. Tas nozīmē, ka $a_{n}=1$ vai $a_{n}>(n-1)(n-2)$. 
   No nevienādības $a_{n} \leq n \sqrt{n}$ seko, ka eksistē kāda vieta $n_0$ šajā virknē, 
   ka visiem $n \geq n_{0}$ ir spēkā $a_{n}=1$. 
   Pierādīsim, ka $a_{k}=1$ visiem naturāliem $k$. N̦emsim $n \geq n_{0}$.
   Tad $a_{k}-1=a_{k}-a_{n}$ un tātad $(a_k - 1) \vdots (k-n)$.

   Tā kā $n$ ir patvaļīgi liels skaitlis, tad $a_{k}-1=0$, tātad $a_{k}=1$.

b. Otrajā gadījumā analoǵiski pierāda, ka $a_{n}=n$ visiem naturāliem $n$.




# <lo-sample/> BBK2012.P1.73

Dots naturāls skaitlis $m$. Noteikt cik daudz ir tādu veselu nenegatīvu skaitlu $k$, 
kuriem $m+k^{2}$ ir pilns kvadrāts.


## Atrisinājums

Dotajai $m$ vērtībai mums ir jānosaka, cik atrisinājumu ir vienādojumam $m+y^{2}=x^{2}$ 
veselos nenegatīvos skaitlos $x,y$. Vienādojumu pārveidojam formā

$$m=(x+y)(x-y)$$

Skaitļu $x+y$ un $x-y$ paritāte ir vienāda.
Tātad, ja $m=4k+2$, tad vienādojumam nav atrisinājumu.

Ja $m$ ir nepāra skaitlis, tad katram skaitļa $m$ sadalījumam reizinātājos 
$m=d_{1}d_{2}$, $d_{1} \leq d_{2}$ atbilst atrisinājums $x, y$, ko iegūst, risinot sistēmu

$$\left\{\begin{array}{l}
x-y = d_{1} \\
x+y = d_{2}
\end{array}\right.$$

Apzīmējot ar $d(m)$ skaiţ̣a $m$ naturālo dalītāju skaitu, iegūsim, ka atrisinājumu skaits ir 
$\frac{d(m)}{2}$, ja $m$ nav pilns kvadrāts, un atrisinājumu skaits ir $\frac{d(m)+1}{2}$, 
ja $m$ ir pilns kvadrāts.

Ja $m$ dalās ar $4$, tad $x+y$ un $x-y$ jābūt pāra skaitļiem. Katram vienādojuma atrisinājumam 
atbilst skaiț̣a $m$ sadalījums reizinātājos $m=2 q_{1} \cdot 2 q_{2}$, jeb 
$\frac{m}{4}=q_{1}q_{2}$. Tātad, atrisinājumu skaits ir $\frac{d\left(\frac{m}{4}\right)}{2}$, 
ja $m$ nav pilns kvadrāts, un atrisinājumu skaits ir $\frac{d\left(\frac{m}{4}\right)+1}{2}$, 
ja $m$ ir pilns kvadrāts.




# <lo-sample/> BBK2012.P1.74

Pierādiet, ka pirmos $n$ naturālos skaitlus nevar sadalīt divās grupās tā, lai visu vienas 
grupas skaitlu reizinājums būtu vienāds ar visu otrās grupas skaitḷu reizinājumu.


## Atrisinājums

No Bertrāna postulāta seko, ka skaitļu grupā no $1$ līdz $n$ eksistē pirmskaitlis $p$, 
kurš lielāks par $\frac{n}{2}$. Visi šā pirmskaiṭ̦a daudzkārtņi ir lielāki par $n$. 
Tas nozīmē, ka, sadalot pirmos $n$ naturālos skaitļus divās grupās, vienas grupas skaitļu 
reizinājums dalīsies ar $p$, bet otrs nē. Tātad šie reizinājumi nevar būt vienādi.





# <lo-sample/> BBK2012.P1.75

Atrodiet visus tādus naturālus skaitlus $m$, kuriem izpildās vienādība

$$1! \cdot 3! \cdot 5! \cdot \cdots \cdot (2m-1)! = \left(\frac{m(m+1)}{2}\right)!$$


## Atrisinājums

Nemsim pirmskaitli $p$, kuram izpildās nevienādības $(2 m-1)<p<2(2 m-1)$. Ja izpildītos 
nevienādība $2(2 m-1) \leq \frac{m(m+1)}{2}$, tad $p$ būtu vienādības labās puses
dalītājs, bet nebūtu vienādības kreisās puses dalītājs, un dotā vienādība neizpildītos. 
Tātad $2(2m-1) > \frac{m(m+1)}{2}$, jeb $m \leq 6$. 
Pārbaudot šīs $m$ vērtības, redzam, ka vienādība izpildīsies, ja $m \in\{1,2,3,4\}$.






# <lo-sample/> BBK2012.P1.76

Skolotājs uzrakstīja uz tāfeles naturālu skaitli. Pirmais skolnieks pateica, 
ka šis skaitlis dalās ar $2$, otrais -- ka šis skaitlis dalās ar $3$, utt., 
trīsdesmitais -- ka šis skaitlis dalās ar $31$. 
Izrādījās, ka $28$ skolnieki ir pateikuši taisnību, bet divi, ka atbildēja viens pēc otra, 
ir kļūdījušies. Kuri no skolniekiem kḷūdījās?


## Atrisinājums

Skaitļiem, ar kuriem dalāmību pārbaudīja skolnieki, kuri kļūdījās, izpildās šādas īpašības:

a. Katrs no šiem skaitliem ir pirmskaitļa pakāpe. Tiešām, ja tas tā nebūtu, tad šo skaitli 
   $x$ varētu uzrakstīt formā $x=l m, \quad(l, m)=1, \quad l>1, m>1$. Taču skolotājas 
   nosauktais skaitlis $A$ dalās ar $l$ un $m$, jo $l<x-1, \quad m<x-1$ , bet dalāmību 
   ar šiem skaițiem pārbaudīja skolnieki, kas nekļūdījās. Tātad $A$ dalās ar 
   $lm=x$, un skolnieks, kas pārbaudīja dalāmību ar $x$, nav kļūdījies.

b. Katrs no šiem skaitliem ir lielāks par $15$. Tiešām, ja $x \leq 15$, tad 
   $2x \leq 30$, un tā kā $2x \mid A$, tad arī $x \mid A$.

Viens no nosauktajiem skaitliem ir pāra skaitlis. Tātad tas ir divnieka pakāpe. 
No nosacījuma $15 < 2^{n} \leq 31$ seko, ka $2^{n}=16$. Der tikai skaitļu pāris $16,17$.

*Atbilde:* Kļūdījās piecpadsmitais un sešpadsmitais skolēni.





# <lo-sample/> BBK2012.P1.77

Atrodiet visus reālu skaitļu trijniekus $(a, b, c)$, kuriem visi skaitļi 
$\frac{a}{b}+\frac{b}{c}$, $\frac{b}{c}+\frac{c}{a}, \frac{c}{a}+\frac{a}{b}$ ir veseli.


## Atrisinājums

*Atbilde:* $\left( \pm t, \pm t, \pm t \right)$, $t \in R$, $t \neq 0$.

$$2 \cdot \frac{a}{b} = \left( \frac{a}{b}+\frac{b}{c} \right) + \left( \frac{c}{a}+\frac{a}{b} \right) - \left(\frac{b}{c}+\frac{c}{a}\right)$$

ir vesels skaitlis. Līdzīgi pierāda, ka $2 \cdot \frac{b}{c}$ un $2 \cdot \frac{c}{a}$ ir veseli skaitļi.

Ja $2 \cdot \frac{a}{b}$ ir pāra skaitlis (t.i. $\frac{a}{b}$ -- vesels skaitlis), 
tad no vienādības $\frac{b}{c}=\left(\frac{a}{b}+\frac{b}{c}\right)-\frac{a}{b}$ seko, 
ka $\frac{b}{c}$ ir vesels skaitlis; līdz̄̄gi arī $\frac{c}{a}$ ir vesels skaitlis. 
Tā kā $\frac{a}{b} \cdot \frac{b}{c} \cdot \frac{c}{a}=1$, tad 
$\left| \frac{a}{b} \right| = \left| \frac{b}{c} \right| = \left| \frac{c}{a} \right| = 1$, 
un iegūstam atbildē norādīto atrisinājumu. Ja $2 \cdot \frac{a}{b}$ ir nepāra skaitlis, 
tad arī $2 \cdot \frac{b}{c}$ un $2 \cdot \frac{c}{a}$ ir nepāra skaiţ̦i. Taču 
$2 \cdot \frac{a}{b} \cdot 2 \cdot \frac{b}{c} \cdot 2 \cdot \frac{c}{a}=8$, 
bet nepāra skaitļu reizinājums nevar būt pāra skaitlis.




# <lo-sample/> BBK2012.P1.78

Pien̦msim, ka $p$ un $q$ ir divi viens otram sekojoši nepāra pirmskaitļi.
Pierādīt, ka $p+q$ ir vismaz trīs naturālu skaitļu reizinājums, katrs no kuriem ir lielāks par $1$.


## Atrisinājums

Tā kā $q-p=2k$, tad $p+q=2 \cdot(p+k)$. Ievērosim, ka

$$p< p+k < p+2k = q.$$

Skaitlis $p+k$ nav pirmskaitlis, jo atrodas starp diviem viens otram sekojošiem 
pirmskaitļiem; tātad to var sadalīt divu naturālu skaitļu reizinājumā.





## Skaiţ̦a n! Dalītāji

Pirmo $n$ naturālo skaitlu reizinājumu apzīmē ar $n!$. Skaidrs, ka visi naturālie skaitļi 
(tai skaitā arī pirmskaitļi), kas nepārsniedz $n$ ir skaitļa $n!$ dalītāji. 
Šis vienkāršais apgalvojums tiks izmantots sekojošo uzdevumu risināšanai.

Vispirms aplūkosim, kā šo ideju bija izmantojis Eiklīds, lai pierādītu, ka pirmskaitļu 
skaits ir bezgalīgs. Pien̦emsim pretējo, ka pirmskaitļu skaits ir galīgs. 
Tādā gadījumā aplūkosim visus pirmskaitļus $p_{1}<p_{2}<\cdots<p_{n}$. Ņemsim skaitli 
$N=p_{1} p_{2} \cdots p_{n}+1$. Skaitlis $N$ dalās ar kādu pirmskaitli $p$. Skaidrs, ka 
$p \neq p_{i}$, jo pretējā gadījumā iegūstam, ka $p \mid\left(p_{1} p_{2} \cdots p_{n}+1\right)$, tātad

$$p \mid\left(\left(p_{1} p_{2} \cdots p_{n}+1\right)-\left(p_{1} p_{2} \cdots p_{n}\right)\right)=1,$$

kas nav iespējams. Šī pretruna pierāda, ka pirmskaitļu skaits ir bezgalīgs.

Šis rezultāts ir pirmais jautājumā par to, cik daudz ir pirmskaitļu - precīzāk: 
cik bieži naturālo skaiţ̦u virknē ir sastopami pirmskaitļi? 
Šis jautājums faktiski ir pamatā veselam skaitļu teorijas virzienam, ko sauc par 
pirmskaitļu sadalījuma teoriju. Lai novērtētu pirmskaitļu daudzumu, tiek aplūkota 
funkcija $\Pi(x)$, kuru definē šādi: $\Pi(x)$ ir pirmskaitļu skaits, kuri nepārsniedz $x$. 
Apgalvojumu, ka pirmskaitļu skaits ir bezgalīgs var pierakstīt šādi:

$$\lim _{x \rightarrow \infty} \prod_{0}(x)=\infty .$$

Taču, kā zināms, funkcijas, kuras bezgalībā tiecas un bezgalību, var augt ātrāk vai lēnāk. 
Precīzs funkcijas $\Pi(x)$ augšanas ātruma novērtējums redzams teorēmā par 
pirmskaitļu sadalījumu. Šo hipotēzi 16 gadu vecumā izteica Gauss, un 1896. gadā 
neatkarīgi pierādīja Adamārs un Valle-Pusens.



**Teorēma (par pirmskaitļu izvietojumu):** Ir spēkā sekojoša robeža:

$$\lim _{x \rightarrow \infty}\left(\prod(x) \cdot \frac{\ln x}{x}\right)=1.$$

Teorēma būtībā nozīmē, ka starp pirmajiem $n$ naturālajiem skaițiem ir apmēram 
$\frac{n}{\ln n}$ pirmskaitļu.

Tomēr uzdevumi par pirmskaitļu sadalījumu ir ļoti sarežğîti, un daudzi no tiem 
arī pašreiz nav atrisināti. Neatrisināti, piemēram, ir šādi uzdevumi.

- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $n^{2}+1$ ?
- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $2^{n}+1$ ? (Fermā pirmskaitlii).
- Vai eksistē bezgalīgi daudz pirmskaitļu, kas uzrakstāmi formā $2^{n}-1$ ? (Mersena pirmskaitļi).
- Vai eksistē bezgalīgi daudz tādu pirmskaitļu $p$, kuriem skaitlis $p+2$ arī ir pirmskaitlis? (Dvīņu problēma).

Tagad paskatīsimies, kā Eiklīda ideja tiek izmantota uzdevumu risināšanā.





# <lo-sample/> BBK2012.P1.79

Vai $(n-1)!$ dalās ar $n$, ja  
**(A)** $n=16$,  
**(B)** $n=41$,  
**(C)** $n=1991$,  
**(D)** $n=1993$?


## Atrisinājums

**(A)** Jā, jo $16=2 \cdot 8$ un $15!$ satur abus šos reizinātājus.  
**(B)** Nē, jo 41 ir pirmskaitlis, bet $40!$ nesatur pirmreizinātājus, lielākus par $40$.  
**(C)** Jā, jo $1991=11 \cdot 181$.  
**(D)** Nē, jo 1993 ir pirmskaitlis.




# <lo-sample/> BBK2012.P1.80

Pierādīt, ka var atrast $1000$ pēc kārtas ņemtus naturālus skaitļus starp 
kuriem nav neviena pirmskaitļa.


## Atrisinājums

Aplūkosim šādus $1000$ pēc kārtas ņemtus naturālus skaitļus:

$$1001!+2, 1001!+3, 1001!+4, \ldots, 1001!+1001$$

Starp šiem skaitļiem nav pirmskaitļu, jo skaitlis $1001!+k$ dalās ar $k$, ja $k \in [2;1001]$.




# <lo-sample/> BBK2012.P1.81

Pierādiet, ka mazākais naturālais skaitlis $N>1$, kurš ir savstarpējais pirmskaitlis ar 
skaițiem $1,2, \ldots, n$, ir pirmskaitlis.

## Atrisinājums

Pien̦emsim, ka skaitlim $N$ eksistē dalītājs $d$, kurš ir atšķirīgs no $1$ un $N$. tad skaitlis 
$d$ ir savstarpējs pirmskaitlis ar skaitļiem $1,2, \ldots, n$ un ir mazāks par $N$. 
Tas ir pretrunā ar skaitļa $N$ izvēli. Tātad $N$ ir pirmskaitlis.





# <lo-sample/> BBK2012.P1.82

Pierādiet, ka eksistē bezgalīgi daudz tādu pirmskaitlu $q$, kuriem eksistē tāds naturāls skaitlis $n<q$, 
ka skaitlis $(n-1)!+1$ dalās ar $q$.


## Atrisinājums

Ņemsim jebkuru saliktu skaitli $n$ un jebkuru skaitļa $(n-1)!+1$ pirmreizinātāju $q$. 
Skaidrs, ka $q>n-1$ un $q \neq n$, jo $n$ nav pirmskaitlis.

No šejienes $q>n$. Tā kā $n$ ir jebkurš skaitlis, tad šādu skaitļu $q$ eksistē bezgalīgi daudz.




# <lo-sample/> BBK2012.P1.83

Kādiem naturāliem $n$ skaitlis $(n-1)!$ nedalās ar $n$?


## Atrisinājums

Ja $n$ ir pirmskaitlis, tad $(n-1)!$ acīmredzami nedalās ar $n$.

Ja skaitli $n$ var uzrakstīt formā $n=ab$, $1<a<b$, tad 
$(n-1)!=1 \cdot \ldots \cdot a \cdot \ldots \cdot b \cdot \ldots \cdot(n-1)$ dalās ar $n=ab$.

Jebkuru saliktu skaitli, kurš nav pirmskaiț̣a kvadrāts, šādā veidā var uzrakstīt (pamatojiet to!).

Atliek aplūkot gadījumu, kad $n=p^{2}. Ja $n=2^{2}$, tad $(n-1) !=6$ nedalās ar $4$. 
Ja $n=p^{2}$, $p>2$, tad $(n-1)!=1 \cdot \ldots \cdot p \cdot \ldots \cdot 2 p \cdot \ldots \cdot(n-1)$ 
dalās ar $p^{2}$, jo reizinātājs $2p$ tiešām parādās skaiț̣a $(n-1)!$ sadalījumā reizinātājos. 
Tas seko no nevienādības $n-1 = p^{2}-1 > 2p$.

*Atbilde:* $n$ ir pirmskaitlis vai $n=4$.





# <lo-sample/> BBK2012.P1.84

Dots nepāra skaitlis $n>1$. Pierādiet, ka $n$ un $n+2$ ir pirmskaitļi tad un tikai tad, 
kad $(n-1)!$ nedalās ne ar $n$, ne ar $n+2$.


## Atrisinājums

Atzīmēsim, ka skaiț̣a $(n-1)!$ visi pirmreizinātāji ir mazāki par $n$. 
Ja skaitlis $(n-1)!$ dalās ar $n$ vai $n+2$, tad šis skaitlis ir salikts skaitlis. 
Apgrieztā apgalvojuma pierādījums analoǵisks iepriekšējā uzdevuma pierādījumam.




# <lo-sample/> BBK2012.P1.85

Ar $n?$ apzīmēsim visu pirmskaitḷu reizinājumu, kuri nepārsniedz $n$. 
Pierādiet, ka visiem $n \geq 4$ izpildās nevienādība $(n-1)? > n$.


## Atrisinājums

Pien̦emsim, ka $(n-1)? = p_{1}p_{2} \cdots p_{n} \leq n$, un tātad $p_{1} p_{2} \cdots p_{n}-1<n$. 
Aplūkosim skaitļa $p_{1} p_{2} \cdots p_{n}-1$ pirmreizinātāju $p$. 
Tas nesakrīt ne ar vienu no skaitļiem $p_{i}$, jo $p_{1} p_{2} \cdots p_{n}-1$ nedalās ar $p_{i}$.

Taču skaitlis $p$ ir mazāks par $n$, un tam būtu jāsakrīt ar kādu no $p_{i}$.
Iegūta pretruna, kas pierāda, ka prasītā nevienādība vienmēr izpildās.




# <lo-sample/> BBK2012.P1.86

Ar $p_{n}$ apzīmēsim $n$-to pēc kārtas pirmskaitli. Pierādiet, ka visiem naturāliem 
$n$ izpildās nevienādība $p_{n}<2^{2^{n}}$.

## Atrisinājums

Apgalvojumu pierādīsim ar indukciju.

Ja $n=1$, tad $p_{1}=2<2^{2^{1}}$.

Pien̦emsim, ka apgalvojums izpildās, ja $n \leq s$, un pierādīsim, ka tas izpildās, ja $n=s+1$. 
Aplūkosim skaitļa $a=p_{1} p_{2} \cdots p_{s}+1$ pirmreizinātāju $p$. 
Skaidrs, ka $p \neq p_{i}$. Tātad $p \quad p_{s+1}$. No šejienes

$$\begin{aligned}
& p_{s+1} \leq p \leq a \leq 2^{2^{1}} \cdot 2^{2^{2}} \cdot \ldots \cdot 2^{2^{s}}+1= \\
& 2^{2^{1}+2^{2}+\cdots+2^{s}}+1=2^{2^{s+1}-2}+1<2^{2^{s+1}}
\end{aligned}$$

Apgalvojums pierādīts.





# <lo-sample/> BBK2012.P1.87

Pierādiet, ka eksistē bezgalīgi daudz tādu pirmskaitļu $p$, ar kuriem vienādojumam 
$x^{2}+x+1 = py$ eksistē atrisinājums veselos skaitļos.


## Atrisinājums

Pien̦emsim, ka pirmskaitļu, kam izpildās dotā īpašība ir galīgs skaits, un apzīmēsim tos ar 
$p_{1}, p_{2}, \ldots, p_{n}$. Ņemsim $x=p_{1} p_{2} \cdots p_{n}$ un skaitļa

$$x^{2}+x+1=\left(p_{1} p_{2} \cdots p_{n}\right)^{2}+p_{1} p_{2} \cdots p_{n}+1$$

pirmreizinātāju $p$. Skaidrs, ka $p \neq p_{i}$, jo pretējā gadījumā

$$p_{i} \mid\left(x^{2}+x+1\right)-x^{2}-x=1$$

Turklāt izpildās vienādība $x^{2}+x+1=p y$, kas norāda, ka arī pirmskaitlim $p$ izpildās prasītā īpašība.

Tātad šādu pirmskaitļu skaits nav ierobežots.





# <lo-sample/> BBK2012.P1.88

Ar $q_{n}$ apzīmēsim mazāko pirmskaitli, kurš nav $n$ dalītājs. 
Pierādiet, ka $\lim _{n \rightarrow \infty} \frac{q_{n}}{n}=0$.

## Atrisinājums

Pierādījumā aplūko skaiţ̦u $p_{1} p_{2} \cdots p_{n}-1$ un $p_{1} p_{2} \cdots p_{n}+1$ visus pirmreizinātājus.




# <lo-sample/> BBK2012.P1.89

Pierādīt, bezgalīgi daudziem pirmskaitļiem $p$ var 
atrast tādus naturālus skaitļus $x$ un $y$, ka 
$2x^2 + 2x + 1 = py$. 

<!--
sameAs=LV.OTHER.TST.1979.9.1
-->


## Atrisinājums

Jāpierāda, ka polinoma $2x^{2}+2x+1$ vērtības, kur $x=1,2,3, \ldots, n, \ldots$, 
dalās ar bezgalīgi daudziem pirmskaitļiem.

Pien̦emsim pretêjo, ka šīs vērtības dalās tikai ar galīgu daudzumu pirmskaitļu 
$P_{1}$, $P_{2}, P_{3}, \ldots, P_{\mathrm{n}}$. Aplūkosim vērtību 
$x_{0}=P_{1} P_{2} P_{3} \cdots P_{n}$. Tad $2 x_{0}^{2}+2 x_{0}+1$ nedalās ne ar 
$P_{1}$, ne ar $P_{2}$, ne ar $P_{3}, \ldots$ ne ar $P_{\mathrm{n}}$ -- visos gadijumos 
rodas atlikums $1$. Bet $2x_{0}^{2}+2x_{0}+1$ ar vismaz vienu pirmskaitli 
(varbūt pats ar sevi) noteikti dalās. Tātad $2 x_{0}^{2}+2 x_{0}+1$ dalās ar kādu 
citu pirmskaitli, ne ar $P_{1}, P_{2}, P_{3}, \ldots, P_{\mathrm{n}}$. Iegūta pretruna.








## Lielākais kopīgais dalītājs un mazākais kopīgais dalāmais


# <lo-sample/> BBK2012.P1.E4.1

Izdalīt ar atlikumu:  
**(A)** $1996$ ar $11$,  
**(B)** $200$ ar $10$,  
**(C)** $15$ ar $1$,  
**(D)** $0$ ar $5$,  
**(E)** $-17$ ar $3$,  
**(F)** $3 ar $12$,  
**(G)** $-3$ ar $12$,  
**(H)** $-18$ ar $3$,  
**(I)** $-111$ ar $7$. 

## Atrisinājums

**(A)** $1996=11 \times 181+5$; 181 ir nepilnais dalījums, 5 ir atlikums.
**(B)** $200=10 \times 20+0$;
**(C)** $15=1 \times 15+0$;
**(D)** $0=5 \times 0+0$;
**(E)** $-17=3 \times(-6)+1$;
**(F)** $3=12 \times 0+3$;
**(G)** $-3=12 \times(-1)+9$;
**(H)** $-18=3 \times(-6)+0$;
**(I)** $-111=7 \times(-16)+1$.




# <lo-sample/> BBK2012.P1.E4.2

Ar Eiklīda algoritmu aprēķināt:  
**(A)** $(33,18)$,  
**(B)** $(1260,406)$,  
**(C)** $(56,39)$,  
**(D)** $(312,138)$.

## Atrisinājums

**(A)**

$$\begin{aligned}
33 & = 18 \times 1+15\\
18 & = 15 \times 1+3 \\
15 & = 3 \times 5 \\
\end{aligned}

Tātad, $\gcd(33,18)=3$. Eiklīda algoritmu (kas no lielākā skaitļa arvien 
patur atlikumu, kas rodas, dalot ar mazāko skaitli) var pierakstīt arī tā:

$$\gcd(33,18) = \gcd(18,15) = \gcd(15,3) = 3.$$

**(B)**

$$\gcd(1260, 406) = \gcd(406, 42) = \gcd(42, 28) = \gcd(28,14) = 14.$$ 


**(C)**

$$\gcd(56, 39) = \gcd(39, 17) = \gcd(17, 5) = \gcd(5,2) = \gcd(2,1) = 1.$$ 


**(D)**

$$\gcd(312, 138) = \gcd(128, 36) = \gcd(36,30) = \gcd(30, 6) = 6.$$




# <lo-sample/> BBK2012.P1.E4.3

Izmantojot formulu $[a,b] = ab/(a,b)$, aprēķināt $[a,b]$:  
**(A)** $[30,18]$,  
**(B)** $[55,25]$,  
**(C)** $[143,91]$,  
**(D)** $[200,150]$.


## Atrisinājums

**(A)** $(30,18)=6$, $[30,18]=\frac{30 \cdot 18}{6}=90$.  
**(B)** $(55,25)=5$, $[55,25]=\frac{55 \cdot 25}{5}=275$.  
**(C)** $(143,91)=13,[143,91]=\frac{143 \cdot 91}{13}=1001$.  
**(D)** $(200,150)=50,[200,150]=\frac{200 \cdot 150}{50}=600$.




# <lo-sample/> BBK2012.P1.E4.4

Saīsināt daļas:  
**(A)** $39/24$,  
**(B)** $60/16$,  
**(C)** $612/522$,  
**(D)** $3053/4343$.


## Atrisinājums

*Atbilde:* **(A)** $13/8$; **(B)** $15/4$; **(C)** $34/29$; **(D)** $71/101$.



# <lo-sample/> BBK2012.P1.E4.5

Ar Eiklīda algoritmu aprēķināt $d=(a,b)$, un izteikt skaitli $d$ formā $ua + vb$.  
**(A)** $(15,9)$,  
**(B)** $(187,68)$,  
**(C)** $(200,325)$,  
**(D)** $(200,40)$.


## Atrisinājums

**(A)**

$$\begin{aligned}
15 & = 9 \times 1+6 \\ 
9 & = 6 \times 1+3 \\
6 & = 3 \times 2 \\
(15,9) & = 3.\\
\end{aligned}$$

Pārrakstām šādā formā:

$$\begin{aligned}
a_{1} & = a_{2} \times 1+a_{3} \\
a_{2} & = a_{3} \times 1+a_{4} \\
a_{3} & = a_{4} \times 2 \\
\end{aligned}$$

$\left(a_{1}, a_{2}\right) = a_{4} = a_{2}-a_{3} = a_{2}-\left(a_{1}-a_{2}\right) = -a_{1}+2 a_{2}$.
Tātad $(15,9)=3=(-1) \times 15+2 \times 9$;

**(B)** $(187,68)=17=(-1) \times 187+3 \times 68$;  
**(C)** $(200,325)=25=5 \times 200-3 \times 325$;  
**(D)** $(200,40)=40=0 \times 200+1 \times 40$.






# <lo-sample/> BBK2012.P1.E4.6

Dots, ka $a-b$ dalās ar $5$, un $a+b$ dalās ar $5$. Pierādiet, ka abi skaitļi 
$a$ un $b$ dalās ar $5$.


## Atrisinājums

$2a = (a-b)+(a+b)$ dalās ar $5$. Tā kā $(2,5)=1$, tad $a$ dalās ar $5$. 
Līdzīgi pierāda, ka $b$ dalās ar $5$.




# <lo-sample/> BBK2012.P1.E4.7

Dalot skaitli $a$ ar $13$, iegūstam nepilno dalījumu $17$. 
Noteikt skaiț̣a $a$ lielāko iespējamo vērtību.


## Atrisinājums

$a=13 \times 17+\mathrm{r}$, $0 \leq r<13$. Tātad lielākā iespējamā $a$ 
vērtība ir $a = 13 \times 17 + 12=233$.




# <lo-sample/> BBK2012.P1.E4.8

Dalot skaitli $x$ ar $7$, iegūstam nepilno dalījumu $11$. 
Kādas vērtības var pien̦emt skaitlis $x$?


## Atrisinājums

$x=7 \times 11+\mathrm{r}$, $0 \leq r<7$. Tātad $x$ var pien̦emt vērtības $77, 78, 79, 80, 81, 82, 83$.




# <lo-sample/> BBK2012.P1.E4.9

Skaitli $a$ dalot ar $12$, atlikumā iegūstam $7$. Kādu atlikumu iegūsim, skaitli 
$a$ dalot ar $6$?


## Atrisinājums

$a = 12q+7 = 6(2q+1) + 1$. Skaitli $a$ dalot ar $6$, atlikumā iegūsim $1$.




# <lo-sample/> BBK2012.P1.E4.10

Skaitli $a$ dalot ar $18$, atlikumā iegūstam $12$. Kādu atlikumu iegūsim, 
skaitli $a$ dalot ar $3$?


## Atrisinājums

$a = 18q+12 = 3(6q+4)+0$. Skaitli $a$ dalot ar $3$, atlikumā iegūsim $0$.



# <lo-sample/> BBK2012.P1.E4.11

Dots, ka $(a,b)=6$. Kādas vērtības var pien̦emt sekojošie skaitļi?  
**(A)** $(a, b+5a)$,  
**(B)** $(8a+3b, 5a+2b)$,  
**(C)** $(4a, 4b)$,  
**(D)** $(a, 2b)$,  
**(E)** $(5a, 2b)$,  
**(F)** $(4a+6b, 6a+8b)$.



## Atrisinājums

**(A)** $(a, b+5 a)=(a, b+5 a-5 a)=(a, b)=6$;

**(B)** Izmantojot LKD 2.īpašību, pārveidojam izteiksmes tā, 
lai samazinātos koeficients pie $b$, lîdz tas kļūs vienāds ar $0$.

$(8a+3b, 5a+2b) = (8a+3b-(5a+2b), 5a+2b) = (3a+b, 5a+2b) =$  
$(3a+b$, 5a+2b -2(3a+b)) = (3a+b,-a) = (3a+b-3a,-a) = (b,-a) = (b,-a) = (b, a) = 6$.

Rēķinot LKD, nen̦em vērā skaitļa zīmi.

**(C)** $(4a, 4b) = 4(a,b)=24$ (īpašība LKD2.).

**(D)** Apzīmēsim $(a, 2 b)=x$.  
Skaidrs, ka $(a, b) \mid(a, 2b)$ un $(a, 2b) \mid (2a, 2b) = 2(a,b)$; 
t.i. $6 \mid x$ un $x \mid 12$. Tātad $x=6$ vai $x=12$. Parādīsim, ka ir iespējamas abas atbildes:

* ja $a=6$, $b=18, tad $(a, b)=6$ un $(a, 2 b)=6$;
* ja $a=12$, $b=6$, tad $(a, b)=6$ un $(a, 2 b)=12$.

**(E)** Apzīmēsim $(5a, 2b)=x$; pastāv šādas sakarības:  
$(a, b) \mid(5a, 2b)$ un $(5a, 2b) \mid (10a, 10b) = 10(a,b)$, 
jeb $6 \mid x$ un $x \mid 60$. Tātad $x$ var pienemt vērtības $6,12,30,60$. 
(Ar piemēriem jāparāda, ka tādas vērtības tiešām realizējas).

**(F)** $(4 a+6 b, 6 a+8 b)=(4 a+6 b,(6 a+8 b)-(4 a+6 b))=(4 a+6 b, 2 a+2 b)=$  
$(4a+6b-2(2a+2b), 2a+2b) = (2b, 2a+2b) = (2b, 2a) = 2(b, a)=12$.



# <lo-sample/> BBK2012.P1.E4.12

Dots, ka $(x, y)=10$. Kādas vērtības var pien̦mt sekojošie skaitļi?  
**(A)** $(x, y+3x)$,  
**(B)** $(3x+7y, 2x+5y)$,   
**(C)** $(x, 2y)$,  
**(D)** $(3x, 3y)$,  
**(E)** $(3x, 2y)$,  
**(F)** $(2x+2y, 3x+4y)$,  
**(G)** $(4x+6y, 6x+10y)$,  
**(H)** $(30x+14y, 21x+10y)$.



## Atrisinājums

Atbildes: **(A)** 10 ; **(B)** 10 ; **(C)** $10 ; 20$; **(D)** 30; **(E)** $10;20;30;60$; **(F)** $10;20$; 
**(G)** $20$; **(H)** $10;20;30;60$.




# <lo-sample/> BBK2012.P1.E4.13

Dots, ka $10 \mid (4a+3b)$ un $10 \mid (3a+5b)$. Pierādiet, ka $10 \mid a$ 
un $10 \mid b$.

## Atrisinājums

$11a = 5(4a+3b) - 3(3a+5b)$ dalās ar $10$ (īpašība D3).
Tā kā $(10,11)=1$, tad $10 \mid a$ (īpašība L5). 
$3(4a+3b) - 4(3a+5b) = -11b$ dalās ar $10$. Tātad arī $b$ dalās ar $10$.




# <lo-sample/> BBK2012.P1.E4.14

Pierādiet, ka trīs pēc kārtas n̦emtu naturālu skaițlu reizinājums dalās ar $6$.


## Atrisinājums

Pierāda, ka šis reizinājums dalās ar $2$ un ar $3$.






# <lo-sample/> BBK2012.P1.E4.15

Dots, ka $6 \mid(3a-8b)$ un $6 \mid (2a-3b)$. Pierādiet, ka $36 \mid \left(a^{2} + ab + b^{2}\right)$.


## Atrisinājums

$2(3a-8b)-3(2a-3b)=-7b$ dalās ar $6$. Tātad $b$ dalās ar $6$. 
Līdzīgi pierāda, ka $a$ dalās ar $6$. No īpašības D5 seko, ka skaitli $a^{2}$, $ab$ un $b^{2}$ 
dalās ar $36$. Tātad $\left( a^{2}+ab+b^{2} \right)$ dalās ar $36$.




# <lo-sample/> BBK2012.P1.E4.16

Pierādiet, ka skaitļi $\left(n^{3}-1\right)/(n-1)$ un $(n+1)^{2}$ ir savstarpēji pirmskaitļi. 


## Atrisinājums

$\left(\left(n^{3}-1\right) /(n-1),(n+1)^{2}\right)=\left(n^{2}+n+1, n^{2}+2 n+1\right)=$  
$\left(n^{2}+n+1,\left(n^{2}+2 n+1\right)-\left(n^{2}+n+1\right)\right)=\left(n^{2}+n+1, n\right)=$  
$\left(n^{2}+n+1-(n+1) n, n\right)=(1, n)=1$.




# <lo-sample/> BBK2012.P1.E4.17

Dots, ka $2a+3b$ dalās ar $5$ un $2a+9b$ dalās ar $5$. Pierādiet, ka abi skaitļi $a$ un $b$ dalās ar $5$.


## Atrisinājums

$6b = (2a+9b)-(2a+3b)$ dalās ar $5$. Tā kā $(6,5)=1$, tad arī $b$ dalās ar $5$; 
$2a=(2a+3b)-3b$ dalās ar $5$, un arī $a$ dalās ar $5$.




# <lo-sample/> BBK2012.P1.E4.18

Cik daudz ir trīsciparu skaitļu, kas dalās ar $13$?


## Atrisinājums

Trīsciparu skaiţ̦i atrodas intervālā $[100; 999]$. Intervālā $[1; 999]$ atrodas 
$[999 / 13] = 76$ skaitļi, kas dalās ar $13$. Intervālā $[1; 99]$ atrodas $[99 / 13] = 7$ skaitļi, 
kas dalās ar $13$. Tātad trīsciparu skaitḷu, kas dalās ar $13$, pavisam ir $76-7=69$.





# <lo-sample/> BBK2012.P1.E4.19

Cik daudz ir četrciparu skaițlu, kas dalās ar $7$?


## Atrisinājums

Četrciparu skaiţu, kas dalās ar $7$, pavisam ir $\lfloor 9999 / 7 \rfloor -  \lfloor 999 / 7 \rfloor = 1286$.





# <lo-sample/> BBK2012.P1.E4.20

Pierādiet, ka skaitļi $n^{3} + 2n$ un $n^{2}+1$ ir savstarpēji pirmskaitļi visām $n$ vērtībām.


## Atrisinājums

$\left(n^{3}+2 n, n^{2}+1\right) = \left( n^{3}+2n-n \left(n^{2}+1 \right), n^{2}+1 \right) = \left(n, n^{2}+1\right)=$  
$\left(n, n^{2}+1-n \cdot n\right)=(n, 1)=1$.




# <lo-sample/> BBK2012.P1.E4.21

Dalāmais ir vienāds ar $371$, bet nepilnais dalījums ir $14$. 
Nosakiet iespējamās dalītāja vērtības un atbilstošos atlikumus.


## Atrisinājums

$371 = x \times 14+r$, $0 \leq r<x$.
$14 x<371$, tātad $x \leq[371 / 14]=26$.
$371=14 x+r<14 x+x=15 x$, tātad $x>371 / 15>24$.

*Atbilde:* Dalījums $x=25$, atlikums $r=21$; dalījums $x=26$, atlikums $r=7$.





# <lo-sample/> BBK2012.P1.E4.22

Dalot skaitli $100$ ar $b$, atlikumā ieguvām $6$. Kādas vērtības var pien̦emt skaitlis $b$?


## Atrisinājums

$100 = bq+6$, $b>6$. $bq=94=2 \times 47$. $b$ ir skaitlạa 94 dalītājs, kas lielāks par $6$. 
Tātad $b=47$ vai $b=94$.




# <lo-sample/> BBK2012.P1.E4.23

Dots, ka $(a,c)=1$ un $(b,c)=1$. Pierādiet, ka $(ab, c)=1$.


## Atrisinājums

Pien̦msim pretējo, ka $(ab,c)=d \neq 1$. Ar $p$ apzīmēsim kādu no skaitļa $d$ pirmreizinātājiem, 
t.i. $p \mid c$ un $p \mid a b$. No pirmskaitḷu 2.īpašības seko, ka $p \mid a$ vai $p \mid b$. 
Pirmajā gadījumā $p \mid a$ un $p \mid c$, bet tas ir pretrunā ar vienādību $(a, c)=1$. 
Otrajā gadījumā $p \mid b$ un $p \mid c$, bet tas ar pretrunā ar vienādību $(b, c)=1$. 
Iegūtā pretruna parāda, ka pien̦ēmums ir aplams. Tas nozīmē, ka $(ab, c)=1$
vai $7$. Tā kā $n$ ir nepāra skaitlis, tad šis atlikums var būt tikai $7$.





# <lo-sample/> BBK2012.P1.E4.24

Dots, ka $(a,b)=1$. Kādas vērtības var pieņemt skaitlis 
$\left(a+b, a^{2}+b^{2}\right)$?


## Atrisinājums

Pien̦emsim, ka $p$ ir kopīgs skaitlu $a+b$ un $a^{2}+b^{2}$ nepāra pirmreizinātājs. 
Tad $p \mid(a+b)^{2}-\left(a^{2}+b^{2}\right)=2ab$ un $p \mid a$ vai $p \mid b$. 
Bet tā kā $p \mid(a+b)$, tad $p \mid a$ un $p \mid b$, bet tas ir pretrunā ar uzdevuma 
nosacījumiem, ka $(a, b)=1$. Abi skaitlii $a$ un $b$ nedrīkst vienlaicīgi 
būt pāra skaitļi. Atliek divas iespējas:

1. viens no skaitliem ir pāra skaitlis, bet otrs nepāra skaitlis un $\left(a+b, a^{2}+b^{2}\right)=1$;
2. abi skaitlii ir nepāra skaitļi. Tādā gadījumā gan $a+b$, gan $a^{2}+b^{2}$
   dalās ar $2$ un viegli pārbaudīt, ka $a^{2}+b^{2}$ ar 4 nedalās. Tas nozīmē, ka 
   $\left(a+b, a^{2}+b^{2}\right)=2$.




# <lo-sample/> BBK2012.P1.E4.25

Pierādiet, ka četru pēc kārtas n̦emtu naturālu skaitļu reizinājums dalās ar $24$.


## Atrisinājums

Pierāda, ka četru pēc kārtas n̦emtu naturālu skaitlu reizinājums dalās ar $3$ un ar $8$.




# <lo-sample/> BBK2012.P1.E4.26

Dots, ka $5\,\mid\,(4a+7b)$ un $5\,\mid\,(3a+8b)$. Pierādiet, ka $250\,\mid\,ab(a+b)$.

## Atrisinājums

$5 \mid 3(4a+7b) - 4(3a+8b) = -11b$, tātad $5 \mid b$; līdzīgi pierāda, ka $5 \mid a$. 
No tā seko, ka $5 \mid (a+b)$. Ja viens no skaițiem $a,b$ ir pāra skaitlis, tad $2 \mid ab$. 
Ja abi ir nepāra skaitļi, tad $2 \mid (a+b)$. Visos gadījumos $2 \mid ab(a+b)$. 
Tātad $2 \times 5 \times 5 \times 5=250 \mid ab(a+b)$.













# <lo-sample/> BBK2012.P1.90

Dots, ka $a$ un $b$ ir divi naturāli skaitļi. Vai var būt, ka to lielākais kopējais dalītājs 
ir $32$, bet to mazākais kopīgais dalāmais ir $1200$?

## Atrisinājums

Nē, nevar būt. Divu skaitlu mazākais kopīgais dalāmais dalās ar katru no dotajiem skaitļiem, 
tātad dalās arī ar to lielāko kopīgo dalāmo; bet $1200$ nedalās ar $32$.




# <lo-sample/> BBK2012.P1.91

Pierādīt, ka skaiţu $19951995$ un $19952003$ lielākais kopīgais dalītājs ir $1$.

## Atrisinājums

Apzīmēsim ar $d$ doto skaitlu lielāko kopīgo dalītāju. Tad doto skaitļu starpība $8$ 
dalās ar $d$; tas nozīmē, ka $d$ ir $1$, $2$, $4$ vai $8$. Tā kā $19951995$ ir nepāra skaitlis, 
tad $d$ arī jābūt nepāra skaitlim. Tas nozīmē, ka $d=1$.





# <lo-sample/> BBK2012.P1.92

Dots naturāls skaitlis $n$. Pierādīt, ka abi skaiț̣i $2n+5$ un $3n+8$ vienlaicīgi nedalās
ne ar kādu naturālu skaitli, kas lielāks par $1$.


## Atrisinājums

Pien̦emsim, ka $2n+5$ un $3 n+8$ dalās ar kādu naturālu skaitli $m$. Tad ar $m$ dalās 
arī skaitlis $3 \cdot(2n+5) - 2 \cdot(3n+8)=1$. Tātad $m=1$.



# <lo-sample/> BBK2012.P1.93

Dots, ka $n$ - naturāls skaitlis. Pierādīt, ka $3n+2$ 
un $7n+5$ ir savstarpēji pirmskaitļi.

<!--
sameAs=LV.OTHER.TST.1976.9.3
-->

## Atrisinājums

Ja $x$ ir doto skaitlu kopīgais dalītājs, tad $x$ dala arī skaitli 
$3(7n+5) - 7(3n+2)=1$. Tātad tas var būt tikai $1$.



# <lo-sample/> BBK2012.P1.94

Aritmētiskā progresija, kuras locekļi ir veseli skaitļi satur skaitļus 
$13$, $37$ un $79$. 
Kāda var būt lielākā šīs progresijas diferences vērtība?

<small>

* topic:GcdAndLcm

</small>

<!--
seeAlso=BBK2012.P1.36
questionType=FindOptimal
-->

## Atrisinājums

Ar $d$ apzīmēsim dotās progresijas diferenci. Tad

$$d \mid(113-41)=72 \text { un } d \mid(193-113)=80.$$

Lielākā iespējamā $d$ vērtība ir $(72,80)=8$. Šāda $d$ vērtība der, jo visi dotie skaitļi 
pieder aritmētiskai progresijai $a_{n} = 8m+1$, kuras diference ir $8$.




# <lo-sample/> BBK2012.P1.95

Atrodiet kaut vienu tādu naturālu skaitli $n$, ka $n$ dalās ar $6,(n+1)$ dalās ar $5$, 
$(n+2)$ dalās ar $4$, $(n+3)$ dalās ar $3$, $(n+4)$ dalās ar $2$.

## Atrisinājums

Tāds skaitlis, piemēram, ir $54$.

Tiešām, $54$ dalās ar $6$; $54+1=55$ dalās ar $5$; $54+2=56$ dalās ar $4$; $54+3=57$ dalās ar $3$; 
$54+4=58$ dalās ar $2$.

Tādu skaitļu ir bezgalīgi daudz. Piemēram, visi skaiţ̦i, kas uzrakstāmi formā $60k+54$





# <lo-sample/> BBK2012.P1.96

Dots, ka $n$ dalās ar $6$, $n$ - naturāls skaitlis. Pierādīt, ka $n$ var sadalīt 
triju dažādu veselu pozitīvu saskaitāmo summā tā, lai katriem diviem no tiem lielākais kopīgais dalītājs būtu $1$.

## Atrisinājums

Ja $n=6k$, ņemam saskaitāmos $2k-1, 2k, \quad 2k+1$.

Blakus esošiem naturāliem skaitļiem LKD vienmēr ir $1$. Atliek pārbaudīt, ka arī skaiţlu 
$2k-1$ un $2k+1$ LKD ir $1$. Tiešām, ja skaiţli $2k-1$ un $2k+1$ abi dalās ar $x$, 
tad arī to starpība (skaitlis $2$) dalās ar $x$. Tātad $x=1$ vai $x=2$. Tā kā $2k+1$ 
nedalās ar $2$, tad skaitļu $2k-1$ un $2k+1$ LKD ir 1 .




# <lo-sample/> BBK2012.P1.97

Pierādīt, ka katru naturālu skaitli, kas lielāks par $17$, 
var izsacīt kā triju tādu
naturālu skaitļu summu, no kuriem katriem diviem 
lielākais kopīgais dalītājs ir $1$.

<!--
sameAs=LV.OTHER.TST.1985.9.3
-->

## Atrisinājums

Pāra skaitlus izsaka šādi:

$$\begin{aligned}
& 6k = 2 + 3 + (6k-5) \\
& 6k+2 = 3 + 4 + (6k-5) \\
& 6k+4 = 2 + 3 + (6k-1)
\end{aligned}$$

Nepāra skaitlus izsaka šādi:

$$\begin{aligned}
& 12k+1 = (6k-7) + (6k-1) + 9 \\
& 12k+3 = (6k-1) + (6k+1) + 3 \\
& 12k+5 = (6k-5) + (6k+1) + 9, \\
& 12k+7 = (6k+5) + (6k-1) + 3, \\
& 12k+9 = (6k-1) + (6k+1) + 9, \\
& 12k+11 = (6k+1) + (6k+7) + 3
\end{aligned}$$

Viegli pārbaudīt, ka jebkuru divu skaitļu, kuri ierakstīti summās, 
lielākais kopīgais dalītājs ir $1$.





# <lo-sample/> BBK2012.P1.98

Doti naturāli skaitļi $x$ un $y$; $u$ ir to lielākais kopigais dalītājs,
$v$ ir to mazākais kopīgais dalāmais. Atrisināt vienādojumu sistēmu.

$$\left\{\begin{array}{l}
x \cdot y \cdot u \cdot v = 3600 \\
u + v = 32 \\
\end{array}\right.$$


## Atrisinājums

Jebkuriem naturāliem skaitliem $x$ un $y$ izpildās īpašība

$$x \cdot y=\operatorname{LKD}(x, y) \cdot \operatorname{MKD}(x, y)$$

Izmantojot šo īpašību, no dotā iegūstam

$$\left\{\begin{array}{l}
(uv)^2 = 3600 \\
u+v = 32 \\
\end{array}\right.
\;\Rightarrow\;
\left\{\begin{array}{l}
uv = 60 \\
u+v = 32 \\
\end{array}\right.$$

Iegūstam $(u;v) = (2;30)$. Otrs pāris $(u;v) = (30;2)$ neder, 
jo $\operatorname{LKD}(x, y)=u \leq \operatorname{MKD}(x, y)=v$.

Tātad abi skaiţ̦i $x$ un $y$ ir skaitļa $30$ dalîtāji, un tie abi ir pāra skaitļi. 
Tātad $x$ var pieņemt vērtības 2, 6, 10,30. Tām atbilst četri atrisinājumu pāri.

*Atbilde:* $\{(2,30),(6,10),(10,6),(30,2)\}$.




# <lo-sample/> BBK2012.P1.99

Virknē uzrakstīti cipari no $1$ līdz $9$:
$$1\;\;2\;\;3\;\;4\;\;5\;\;6\;\;7\;\;8\;\;9$$
Kādu lielāko daudzumu semikolu var ievietot starp 
blakus esošiem cipariem, lai tie sadalītu ciparu virkni 
tādu naturālo skaitļu pierakstos, no kuriem 
katriem diviem lielākais kopīgais dalītājs ir $1$?
(Piemēram, pieraksts $123;45678;9$ neder, 
jo $123$ un $9$ abi dalās ar $3$.)

<!--
questionType=FindOptimal
seeAlso=LV.NO.2001.7.4
-->

## Atrisinājums

Var ielikt $5$ semikolus, piemēram:

$$1 ; 23 ; 4 ; 5 ; 67 ; 89.$$

Vairāk par $5$ semikoliem ielikt nevar, jo tādā gadījumā veidotos vismaz 
$7$ skaitli; no tiem vismaz divi būtu pāra skaiţ̦li, jo nepāra skaitl̦i 
var būt tikai $5$ (ir tikai 5 nepāra cipari, ar kuriem jābeidzas nepāra 
skaitļiem). Šie pāra skaiţ̦i nav savstarpēji pirmskaiţ̦i, jo abi dalās ar $2$.





# <lo-sample/> BBK2012.P1.100

Sešciparu skaitļa $N$ pirmais cipars ir $7$, piektais - $2$, 
bet pēdējais - nepāra skaitlis. Zināms, ka dalot $N$ ar skaiţ̧iem $3$, $4$, $7$, $9$, $11$ un $13$, 
rezultātā iegūstam vienādus atlikumus. Atrodiet skaitli $N$.

## Atrisinājums

Ar $r$ apzīmēsim atlikumu, ko iegūstam, dalot skaitli $N$ ar $3,4,7,9,11,13$. 
Protams, $0 \leq r<3$, un tā kā $N$ ir nepāra skaitlis, tad $r=1$. 
Tātad $N-1$ dalās ar visiem skaitliem $3$, $4$, $7$, $9$, $11$, $13$ un arī ar to mazāko 
kopīgo dalāmo 36036. Iegūstam vienādību

$$\overline{7 \ast \ast \ast 2 \ast} = x \cdot 36036+1.$$

No nevienādībām $700000<x \cdot 36036+1<800000$ seko， ka $20 \leq x \leq 22$. Pārbaudot šīs 
vērtības redzam, ka der tikai skaitlis $x=20$, un meklētais skaitlis $N$ ir $720721$.




# <lo-sample/> BBK2012.P1.101

Doti naturāli skaiți $a_{1}<a_{2}<\cdots<a_{n}$. Pierādiet, ka 
$\left[ a_{1}, a_{2}, \ldots, a_{n} \right] \geq n a_{1}$.

## Atrisinājums

Apzīmēsim ar $A$ skaiț̣u $a_{1}, a_{2}, \ldots, a_{n}$ mazāko kopīgo dalāmo. 
Tādā gadījumā izpildās nevienādības

$$\frac{A}{a_{1}}>\frac{A}{a_{2}}>\ldots>\frac{A}{a_{n}} \geq 1$$

No šejienes seko, ka $\frac{A}{a_{1}} \geq n$, jo visi uzrakstītie skaitļi ir naturāli. 
Tātad $A \geq n a_{1}$; prasītais pierādīts.




# <lo-sample/> BBK2012.P1.102

Doti naturāli skaiţ̦i $a$ un $b$. Pierādiet, ka no skaitļiem $a, 2a, 3a, \ldots, ba$ tieši 
$(a,b)$ dalās ar $b$.

## Atrisinājums

Apzīmēsim $(a, b)=d$. Tad $a=rd$, $b=s d$, $(r, s)=1$. Skaitļus 
$a, 2a, \ldots, ba$ dalot ar $b$, iegūstam skaitļus $\frac{r}{s}, \frac{2r}{s}, \ldots, \frac{(ds)r}{s}$. 
Skaitlis $\frac{kr}{s}$ ir vesels tad un tikai tad, ja $k$ dalās ar $s$. 
Starp pirmajiem $s$ skaiţliem šādu skaitļu ir tieši $d$. Apgalvojums pierādīts.





# <lo-sample/> BBK2012.P1.103

Doti veseli skaiţ̦i $a$ un $b$. Pierādiet, ka skaitļu $a+b$ un $a^{2}+b^{2}$ LKD ir vienāds ar $1$ vai $2$.

## Atrisinājums

Izmantojot vienādību $2 a b=(a+b)^{2}-\left(a^{2}+b^{2}\right)$ pierāda, ka skaitļiem 
$a+b$ un $a^{2}+b^{2}$ nav kopīgu dalītāju, kas ir lielāki par $2$.




# <lo-sample/> BBK2012.P1.104

Skaitļu virkne $(a_i)$ tiek definēta šādi: 
$$a_1=19,\;a_2=90,\;a_{n+2}=a_n+a_{n+1},\;\mbox{ja}\;n=1,2,3,\ldots.$$
Atrast skaitļu $a_{1989}$ un $a_{1990}$ lielāko kopīgo dalītāju.


<small>

* topic:LinearRecurrencesConstant
* topic:InvariantAlgebraic
* topic:NumTheoryMathInduction

</small>

<!--
questionType=FindAll
-->

## Atrisinājums

Atzīmēsim lielākā kopīgā dalītāja pamatīpašību:

$$(a, b)=(a, b+ka),$$

kur $k$ - patvaļīgs vesels skaitlis. Tātad

$$\begin{aligned}
& \left(a_{1989}, a_{1990}\right) = \left(a_{1999}, a_{1990}-a_{1989}\right) = \left(a_{1989}, a_{1988}\right) = \left(a_{1989}-a_{1988}, a_{1988}\right)= \\
& \left(a_{1987}, a_{1988}\right)=\cdots=\left(a_{1}, a_{2}\right)=(19,90)=1.
\end{aligned}$$





# <lo-sample/> BBK2012.P1.105 

Kādu lielāko vērtību var pieņemt skaitļu $a_{1}, a_{2}, \ldots, a_{10}$ LKD, 
ja to summa ir $1001$?


## Atrisinājums

Apzīmēsim $\left(a_{1}, a_{2}, \ldots, a_{10}\right)$ ar $d$. Tad

a. $d \mid \left(a_{1}+a_{2}+\cdots+a_{10}\right) = 1001$,
b. $d \mid \min \left\{a_{i}\right\}$, t.i. $d \leq \frac{1001}{10}$, $d \leq 100$.

Skaitļa $1001$ lielākais dalitājs, kas nepārsniedz $100$ ir $91$. 
Piemērs, kad šāda vērtība realizējas, ir sekojošs:

$$a_{1}=a_{2}=\cdots=a_{9}=91, \quad a_{10}=182.$$




# <lo-sample/> BBK2012.P1.106 

Skaitļi $a_{1}, a_{2}, a_{3}, \ldots, a_{10}$ ir veseli pozitīvi skaitļi un  
$$a_{1}+a_{2}+a_{3}+\cdots+a_{10}=1001$$

Kādas vērtības var būt skaitļu $a_{1}, a_{2}, a_{3}, \ldots, a_{10}$ 
lielākajam kopīgajam dalītājam?


## Atrisinājums

Tā kā $a_{1}+a_{2}+\cdots+a_{10}=1001$, tad 1001 dalās ar visu skaitļu 
$a_{1}, a_{2}, \ldots, a_{10}$ kopīgo dalītāju. Tā kā $1001=7 \cdot 11 \cdot 13$, 
tad apskatāmo skaitļu lielākais kopīgais dalītājs nevar pienemt citas vērtỉbas kā 
$1,7,11,13,77,91,143,1001$. Vērtības $143$ un $1001$ neder, jo tad katrs skaitlis būtu 
ne mazāks par 143 un to summa būtu lielāka par $1001$. 
Atlikušajām $6$ vērtībām var norādīt atbilstošos piemērus:

* $1,1,1,1,1,1,1,1,1,992$; $d=1$;
* $7,7,7,7,7,7,7,7,7,938$; $d=7$
* $11,11,11,11,11,11,11,11,11,902$; $d=11$;
* $13,13,13,13,13,13,13,13,13,884$; $d=13$;
* $77,77,77,77,77,77,77,77,77,308$; $d=77$;
* $91,91,91,91,91,91,91,91,91,182$; $d=91$.





# <lo-sample/> BBK2012.P1.107 

Skaitlis $2401$ ir izteikts kā $25$ naturālu skaitļu summa. 
Kāda ir mazākā iespējamā šo skaitļu MKD vērtība?

## Atrisinājums

*Atbilde:* $98$.

Atzīmēsim, ka vismaz viens no dotajiem saskaitāmajiem ir lielāks par $96$. 
Pretējā gadījumā summa nepārsniegtu $25 \cdot 96=2400$.

Pierādīsim, ka MKD nav $97$. Ja tā būtu, tad visi saskaitāmie būtu vienādi ar 
$97$ vai $1$, jo $97$ ir pirmskaitlis. Ja starp tiem ir vieninieks,
tad summa nepārsniedz $1+24 \cdot 97<2401$. Ja tie visi ir vienādi ar $97$, 
tad summa ir $25 \cdot 97=2425 \neq 2401$.

Skaiţu komplektu, kuru MKD ir $98$ izvēlamies šādi: $24$ reizes skaitlis $98$ un viens skaitlis $49$.




# <lo-sample/> BBK2012.P1.108 

Kādu lielāko daudzumu naturālu skaitļu, kas nepārsniedz $360$, var izvēlēties tā, 
lai neviens no tiem nebūtu pirmskaitlis, bet katru divu izraudzīto skaitļu 
lielākais kopīgais dalītājs būtu $1$?

## Atrisinājums

Skaitlis $1$ ir savstarpējs pirmskaitlis ar visiem naturāliem skaitļiem. 
Aplūkosim naturālus skaitļus no $2$ līdz $360$. Ja tāds $n$ nav pirmskaitlis, 
tad tam jādalās ar kādu pirmskaitli, kas nepārsniedz 
$\sqrt{n} \leq \sqrt{360}<\sqrt{361}=19$.

Par $19$ mazāki ir tikai $7$ pirmskaitli: $2, 3, 5, 7, 11, 13, 17$. Tātad, ja izvēlēsimies 
(neskaitot $1$) vairāk nekā $7$ šādus skaitlus, tad vismaz diviem no tiem būs kopīgs 
pirmreizinātājs. Tātad vairāk par $8$ skaițiem izvēlēties nevar.

Piemērs ar $8$ skaitļiem ir šāds:

$1,2^{2}, 3^{2}, 5^{2}, 7^{2}, 11^{2}, 13^{2}, 17^{2}$.




# <lo-sample/> BBK2012.P1.109 

Pierādīt, ka no katriem  
**(A)** trim,  
**(B)** pieciem,  
**(C)** septiņiem  
pēc kārtas n̦emtiem naturāliem skaiţ̦iem var izvēlēties vienu tā, 
ka tas ir savstarpējs pirmskaitlis ar katru no pārējiem.

## Atrisinājums

**(A)** no skaițiem $n, n+1, n+2$ var izvēlēties skaitli $n+1$;  
**(B)** katri divi no pieciem pēc kārtas ņemtiem skaitļiem atšķiras par $1$, $2$, $3$ vai $4$.
No šiem skaiţ̧iem izvēlēsimies tādu, kurš nedalās ne ar $2$, ne ar $3$. 
Tas būs savstarpējs pirmskaitlis ar visiem pārējiem skaitļiem.  
**(C)** katri divi no septiņiem pēc kārtas n̦emtiem skaitļiem atšķiras par $1$, $2$, 
$3$, $4$, $5$ vai $6$. Starp tiem ir vismaz 3 nepāra skaitļi 
$n, n+2, n+4$. No šiem skaitļiem tikai viens var dalīties ar 3 un viens var 
dalīties ar $5$. Atlikušais skaitlis apmierina uzdevuma nosacījumus.




# <lo-sample/> BBK2012.P1.110 

Doti naturāli skaiţ̧i $a$ un $b$. Zināms, ka $\frac{a+1}{b}+\frac{b+1}{a}$ ir vesels skaitlis.
Pierādīt, ka $(a, b) \leq \sqrt{a+b}$.


## Atrisinājums

Apzīmēsim $(a, b)=d$. No vienādības

$$\frac{a+1}{b}+\frac{b+1}{a}=\frac{a^{2}+b^{2}+a+b}{ab}$$

seko, ka $a^{2}+b^{2}+a+b$ dalās ar $a b$, un tātad arī ar $d^{2}$. 
Arī $a^{2}+b^{2}$ dalās ar $d^{2}$. Tātad $a+b$ dalās ar $d^{2}$; 
tas nozīmē, ka $a+b \geq d^{2}$. Izvelkot kvadrātsakni, iegūstam prasīto.




# <lo-sample/> BBK2012.P1.111 

Doti naturāli skaiţ̦i $a, b, a^{\prime}, b^{\prime}$. 
Apzīmēsim $(a, b)$ ar $d$ un $a^{\prime}, b^{\prime}$ ar $d^{\prime}$. 
Pierādīt, ka $\left(a a^{\prime}, a b^{\prime}, b a^{\prime}, b b^{\prime}\right)=d d^{\prime}$.


## Atrisinājums

Izmantojot LKD īpašības, iegūstam

$$\begin{aligned}
& \left(a a^{\prime}, a b^{\prime}, b a^{\prime}, b b^{\prime}\right)=\left(\left(a a^{\prime}, a b^{\prime}\right),\left(b a^{\prime}, b b^{\prime}\right)\right)= \\
& \left(a\left(a^{\prime}, b^{\prime}\right), b\left(a^{\prime}, b^{\prime}\right)\right)=\left(a d^{\prime}, b d^{\prime}\right)=(a, b) d^{\prime}=d d^{\prime}
\end{aligned}$$




# <lo-sample/> BBK2012.P1.112 

Vai skaitlis $x$ noteikti ir racionāls, ja zināms, ka racionāli ir sekojoši skaitļi   
**(A)** $x^{55}$ un $x^{89}$,  
**(B)** $x^{91}$ un $x^{42}$?

## Atrisinājums

**(A)** No dotā seko, ka racionāls ir skaitlis $x^{98}: x^{55}=x^{34}$. Līdzīgi iegūstam, ka 
racionāli ir skaitļi $x^{55}:x^{34}=x^{21}$, x^{34}:x^{21}=x^{13}$, $x^{21}:x^{13}=x^{8}$, 
$x^{13}:x^{8}=x^{5}$, $x^{8}:x^{5}=x^{3}$, $x^{5}:x^{3}=x^{2}$, $x^{3}:x^{2}=x$ ir racionāli.

**(B)** Nē. Ja, piemēram, $x=\sqrt[7]{2}$, tad $x$ nav racionāls skaitlis, 
bet $x^{91}=2^{13}$ un $x^{42}=2^{6}$ ir racionāli skaiţ̦i.




# <lo-sample/> BBK2012.P1.113 

Doti naturāli skaiţ̦i $a, b, c$, kuriem $(a, b, c)=1$, un izpildās vienādība

$$\frac{1}{a}+\frac{1}{b}=\frac{1}{c}$$

Pierādiet, ka $a+b$ ir naturāla skaiţ̦a kvadrāts.

## Atrisinājums

Pārveidosim doto vienādību formā $a+b=\frac{a b}{c}$. Apzīmēsim $(a, b)=d$; tad $a=a_{1}d$, $b=b_{1}d$, 
$\left(a_{1}, b_{1}\right)=1$. Iegūstam

$$\left(a_{1}+b_{1}\right) d=\frac{a_{1} b_{1} d^{2}}{c}, \text{ jeb }\left(a_{1}+b_{1}\right)=\frac{a_{1} b_{1} d}{c}.$$

No šejienes var secināt, ka $\frac{a_{1}+b_{1}}{d}=\frac{a_{1} b_{1}}{c}$ 
ir vesels skaitlis, jo $(d, c)=(a, b, c)=1$.

Arī skaitlis $c=\frac{a_{1} b_{1} d}{a_{1}+b_{1}}$ ir vesels skaitlis, un tā kā 
$\left(a_{1}, a_{1}+b_{1}\right)=\left(b_{1}, a_{1}+b_{1}\right)=1$, tad 
$\frac{d}{a_{1}+b_{1}}$ ir vesels skaitlis. Tātad, $d$ dalās ar $a_{1}+b_{1}, a_{1}+b_{1}$ 
dalās ar $d$, un $a_{1}+b_{1}=d$. Rezultātā iegūstam, ka $a+b=d\left(a_{1}+b_{1}\right)=d^{2}$.




# <lo-sample/> BBK2012.P1.114

Naturāliem skaiţ̧iem $x, y, z$ izpildās vienādība $\frac{1}{x}-\frac{1}{y}=\frac{1}{z}$. 
Skaitļu $x, y, z$ lielākais kopīgais dalītājs ir $h$. Pierādīt, ka skaitļi $h x y z$ un $h(y-z)$ ir kvadrāti.

## Atrisinājums

Apzīmēsim $x=ah$, $y=bh$, $z=ch$, $(a, b, c)=1$. 
Doto vienādību pārveidojam formā $c(b-a)=ab$. Tad $hxyz = h^{4} c^{2}(b-a)$ 
un $h(y-x)=h^{2}(b-a)$. Mums ir jāpierāda, ka $b-a$ ir kvadrāts.

Apzīmēsim $f=(b, c)$, $b=fk$, $c=fl$, $(k, l)=1$. No vienādības $c(b-a)=a b$ seko, 
ka $f^{2}kl = af(k+l)$. Tā kā $k,l$ un $k+l$ ir savstarpēji pirmskaitļi, 
tad $(k+l) \mid f$; $f=n(k+l)$. No šejienes

$$b=n(k+l) k, \quad c=n(k+l)l,\;\; a=\frac{f^{2}kl}{f(k+l)}=nkl.$$

Redzam, ka $n$ ir skaitlu $a, b$ un $c$ dalītājs; tātad $n=1$ un $b-a=k^{2}$. Prasītais pierādīts.




# <lo-sample/> BBK2012.P1.115

Atrodiet visus tādus dažādu naturālu skaitļu trijniekus, 
kuriem skaitļi $ab$, $ac$ un $bc$ veido aritmētisko progresiju.

<!--
questionType=FindAll
-->

## Atrisinājums


Nosacījumu, ka trīs skaiţ̦i $ab$, $bc$, $ac$ veido aritmētisko progresiju, pierakstīsim šādi:

$$ab + bc = 2ac, \text { jeb } a=\frac{bc}{2c-b}.$$

Apzīmēsim $(b, c)=d$; tad $b=b_{1}d$, $c=c_{1}d$, $\left(b_{1}, c_{1}\right)=1$. No šejienes 
$a=\frac{b_{1} c_{1} d}{2 b_{1}-c_{1}}$; tātad $b_{1} c_{1} d$ dalās ar $2 b_{1}-c_{1}$.

Tā kā $\left(b_{1}, 2 b_{1}-c_{1}\right) = \left(b_{1}, c_{1}\right) = 1$ un 
$\left(c_{1}, 2b_{1} - c_{1} \right) = \left(2b_{1}, c_{1}\right) \in\{1,2\}$, 
tad pastāv divas iespējas:

(a) $\left(b_{1}, 2 b_{1}-c_{1}\right)=1,\left(c_{1}, 2 b_{1}-c_{1}\right)=1$; tad $d=\left(2 b_{1}-c_{1}\right) k$.

Iegūts sekojošs atrisinājums:

$$\begin{aligned}
& b=\left(2 b_{1}-c_{1}\right) k, c=c_{1}\left(2 b_{1}-c_{1}\right) k, a=b_{1} c_{1} k \\
& b_{1}, c_{1}, k \in N, \quad\left(b_{1}, c_{1}\right)=1, \quad 2 b_{1}-c_{1}>0.
\end{aligned}$$

Līdzīgi aplūko otru iespēju.





# <lo-sample/> BBK2012.P1.116 

Dots naturāls skaitlis $n$. Aplūkosim tādu naturālu skaiţ̦u pārus 
$(u, v)$, kuriem $[u, v]=n$. Pierādiet, ka šādu pāru skaits ir 
vienāds ar skaiț̣a $n^{2}$ pozitīvo dalītāju skaitu.


## Atrisinājums

Lai pierādītu prasīto apgalvojumu, katram naturālu skaitlu pārim $(u ; v)$, kuram $[u, v]=1$, 
viennozīmīgi piekārtosim skaitla $n^{2}$ naturālu dalītāju.

Attēlojumu definēsim šādi:

$$f(u, v)=\frac{u \cdot n}{v}=d.$$

Var pārbaudīt, ka $d$ ir $n^{2}$ dalītājs. Apgriezto attēlojumu definē ar formulām:

$$u=\frac{d n}{[d, n]},\;\; v=\frac{n^{2}}{[d, n]} .$$

No šejienes seko prasītais.





# <lo-sample/> BBK2012.P1.117

Aplūkojam visus naturālos skaitļus no $1$ līdz  
$2\,000\,000$ ieskaitot. Izvēlēsimies
no tiem kaut kādus  $1\,000\,001$ skaitļus.
Pierādīt, ka starp izvēlētajiem skaitļiem 
noteikti atradīsies divi tādi, kas ir savstarpēji
pirmskaitļi.
Vai to noteikti var apgalvot, ja tiek izvēlēti 
$1\,000\,000$ skaitļi?

<!--
sameAs=LV.OTHER.TST.1981.9.2
-->

## Atrisinājums

Vispirms pierādīsim, ka divi viens otram sekojoši naturāli skaitli ir savstarpēji pirmskaitļi. 
Tiešām $(n,(n+1))=(n,(n+1)-n)=(n, 1)=1$.

Sadalīsim visus dotos skaitļus pāros:

$$(1,2),(3,4), \ldots,(1999999,2000000).$$

Tādu pāru ir $1000000$. Mums ir jāizvēlas $1000001$ skaitlis; tātad vismaz divi skaiţ̦i būs no 
viena pāra - tie būs savstarpēji pirmskaitļi.

$1000000$ skaitļus izvēlēties var: jāņem visi pāra skaitļi; jebkuri divi no tiem nav 
savstarpēji pirmskaitli, jo tie abi dalās ar $2$.






# <lo-sample/> BBK2012.P1.118 

Uz tāfeles uzrakstìti 1999 naturāli skaiţ̦i (starp tiem var būt arī vienādi). 
Ar vienu gājienu aţ̦auts nodzēst divus skaitlus un to vietā uzrakstīt 
nodzēsto skaitlu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo.

Pierādīt, ka izdarot šādus gājienus pietiekami ilgi, uz tāfeles uzrakstītie 
skaitļi kādreiz pārstās mainīties.


## Atrisinājums

Apzīmēsim $\operatorname{LKD}(x, y)=(x, y)=u$, bet $\operatorname{MKD}(x, y)=[x, y]=v$. 
No vienādības $u \cdot v=x \cdot y$ seko, ka kopējais skaitļu reizinājums $R$ nemainās. 
Atzīmēsim, ka no šejienes seko, ka kopējā skaitļu summa nevar palielināties bezgalīgi ilgi. 
Tiešām, ja skaitļu summa palielinātos bezgalīgi ilgi, tad tā kļūtu lielāka par $1999R$. 
Tādā gadījumā kāds no skaitļiem būtu lielāks par $R$, un arī viss reizinājums būtu palielinājies.

Atliek pierādīt tikai tādu faktu:

Ja $x<y$, $u<x<y<v$, kur $u, x, y, v$ -- reāli skaitli, $xy=uv$, tad $u+v>x+y$.

Šis fakts nozīmē, ka, aizvietojot skaiţus $x, y$ ar to lielāko kopīgo dalītāju un 
mazāko kopīgo dalāmo visu skaitlu summa palielinās (izṇemot gadījumu, kad $x=u$ un $y=v$). 
Pierādījums:

$$u+v=\sqrt{(u-v)^{2}+4uv} > \sqrt{(x-y)^{2} + 4xy}=x+y.$$

Tas nozīmē, ka ar laiku iestāsies stabilizācija; no jebkuriem diviem skaitļiem 
viens būs otra dalītājs un izpildīsies vienādības $u=(x, y)$ un $v=[x, y]$; 
tātad vai nu $x$ būs skaitļa $y$ dalītājs, vai otrādi.





# <lo-sample/> BBK2012.P1.119

Doti naturāli skaitļi $a$, $b$ un $m$; $\mbox{LKD}(a,b)=1$. 
Pierādiet, ka aritmētiskajā progresijā $ak+b$, ($k=0,1,2,\ldots$) 
ir bezgalīgi daudz locekļu, kas ir savstarpēji pirmskaitļi ar skaitli $m$.

<small>

* topic:ArithmeticSeriesAll

</small>

<!--
questionType=Prove
-->


## Atrisinājums

Apzīmēsim ar $A$ visu tādu skaitļa $m$ pirmreizinātāju reizinājumu, kuri ir arī skaitļa $a$ dalītāji.  
Apzīmēsim ar $B$ visu tādu skaitļa $m$ pirmreizinātāju reizinājumu, kuri ir arī skaitļa $b$ dalītāji.  
Apzīmēsim ar $C$ visu tādu skaitḷa $m$ pirmreizinātāju reizinājumu, kuri nav ne $a$ ne $b$ dalītāji.

Tad $(A, B)=(A, C)=(C, B)=1$.

Pierādīsim, ka $(aAC+b, m)=1$. Pieņemsim pretējo, ka eksistē pirmskaitlis $p$, kurš dala 
$aAC+b$ un $m$. Ja $p \mid m$, tad $p$ dala $A,B$ vai $C$.

Ja $A$ dalās ar $p$, tad no tā, ka $aAC+b$ dalās ar $p$, seko, ka arī $b$ dalās ar $p$. 
No tā, ka $b$ un $m$ dalās ar $p$, seko, ka $B$ dalās ar $p$. Iegūta pretruna ar to, ka $(A, B)=1$. 
Līdzīgi nonākam pie pretrunas arī gadījumos, kad $B$ vai $C$ dalās ar $p$.

Tātad $(a A C+b, m)=1$; bet tad arī

$$(a(A C+t m)+b, m)=(a A C+b, m)=1.$$

Ņemot aritmētiskajā progresijā $ak+b$ un $k = AC + tm$, mēs iegūsim bezgalīgi 
daudz locekļus, kuri ir savstarpēji pirmskaitļi ar $m$.





# <lo-sample/> BBK2012.P1.120

Doti $12$ dažādi naturāli skaiţ̦li. Katriem $5$ no tiem mazākais kopīgais 
dalāmais ir viens un tas pats skaitlis $M$. Ir zināms, ka no dotajiem 
$12$ skaitliem var izvēlēties $x$ skaiţ̧us tā, ka katri divi no izvēlētajiem 
skaiţ̦liem ir savstarpēji pirmskaitļi.  
**(A)** Pierādīt, ka $x \leq 4$.  
**(B)** Pierādīt, ka var gadīties, ka $x=4$.


## Atrisinājums

**(A)** Pien̦emsim pretējo, ka ir izdevies izvēlēties piecus skaitļus, kas ir 
pa pāriem savstarpēji pirmskaiţ̦i; apzīmēsim tos ar $a_{1}, a_{2}, a_{3}, a_{4}, a_{5}$. 
Šo skaitlu MKD ir $a_{1} a_{2} a_{3} a_{4} a_{5}$, tāpēc jebkuru piecu doto 
skaitļu MKD ir $a_{1} a_{2} a_{3} a_{4} a_{5}$.

Apzīmēsim ar $y$ jebkuru no dotajiem $12$ skaitļiem, kas nav ne $a_{1}$, ne 
$a_{2}$, ne $a_{3}$, ne $a_{4}$, ne $a_{5}$. Apskatīsim $5$ skaitļus 
$y, a_{2}, a_{3}, a_{4}, a_{5}$. To MKD noteikti satur reizinājumu 
$a_{2} a_{3} a_{4} a_{5}$ un vēl tos pirmreizinātājus, kas jāpievieno 
lai šis MKD dalîtos ar $y$. No otras puses šis MKD ir 
$a_{1} \cdot\left(a_{2} a_{3} a_{4} a_{5}\right)$. Tāpēc $a_{1}$ noteikti ieiet
kā reizinātājs skaitlī $y$, tātad $y$ dalās ar $a_{1}$. Līdzīgi pierāda, ka 
$y$ dalās ar $a_{2}, a_{3}, a_{4}, a_{5}$. Tā kā $a_{1}, a_{2}, a_{3}, a_{4}, a_{5}$ 
ir pa pāriem savstarpēji pirmskaitļi, tad $y$ dalās ar $a_{1} a_{2} a_{3} a_{4} a_{5}$.

No otras puses 
$\operatorname{MKD}\left(y, a_{2}, a_{3}, a_{4}, a_{5}\right)=a_{1} a_{2} a_{3} a_{4} a_{5}$, 
tāpēc $a_{1} a_{2} a_{3} a_{4} a_{5}$ dalās ar $y$. Tas nozīmē, ka 
$y=a_{1} a_{2} a_{3} a_{4} a_{5}$. Iznāk, ka katrs mūsu kopas skaitlis, kas nav 
s$a_{1}, a_{2}, a_{3}, a_{4}, a_{5}$ ir vienāds ar $a_{1} a_{2} a_{3} a_{4} a_{5}$. 
Tā ir pretruna ar uzdevuma nosacījumu, ka visi dotie skaitļi ir dažādi.

**(B)** Pieņemsim, ka $p_{1}, p_{2}, \ldots, p_{8}$ ir dažādi pirmskaitļi.

Aplūkosim skaitlus $p_{1}, p_{2}, p_{3}, p_{4} p_{5} p_{6} p_{7} p_{8}$ kā arī visus 
šo $8$ pirmskaitļu reizinājumus pa septiṇiem skaitļiem. Kopā mums ir $12$ skaitļi. 
Pirmie 4 no tiem ir pa pāriem savstarpēji pirmskaitļi. Ievērosim, ka visi šie 
skaitļi ir skaitļa $P=p_{1} p_{2} p_{3} \cdots p_{8}$ dalîtāji. Pierādīsim, 
ka jebkuru $5$ no $12$ izvêlētajiem skaitliem MKD ir vienāds ar $P$. Ja starp 
izvēlētajiem $5$ skaiţ̦iem ir vismaz divi "reizinājumi pa 7", tad ar to jau pietiek, 
lai MKD būtu $P$ (šie divi reizinājumi satur visus $8$ pirmskaitļus). 
Ja "reizinājums pa $7$" starp tiem ir tikai viens, tad pārējie skaitļi ir 
$p_{1}, p_{2}, p_{3}, p_{4} p_{5} p_{6} p_{7} p_{8}$, un atkal MKD 
ir vienāds ar $P$. Apgalvojums pierādīts.





# <lo-sample/> BBK2012.P1.121

Dota virkne $x_1=19,\;x_2=95,\;x_{n+2}=\mbox{LKD}(x_{n+1},x_n)+x_n$, 
ja $n \geq 1$. Atrast skaitļu $x_{1995}$ un $x_{1996}$ 
lielāko kopīgo dalītāju.


<small>

* topic:NonlinearRecurrences
* topic:InvariantAlgebraic
* topic:NumTheoryMathInduction

</small>

<!--
questionType=FindAll
-->


## Atrisinājums

Ar indukciju pierādīsim, ka $\operatorname{LKD}\left(x_{k-1}, x_{k}\right)=19$.
Ja $k=3, \operatorname{tad} \operatorname{LKD}\left(x_{k-1}, x_{k}\right)=\operatorname{LKD}(95,114)=19$.

Pien̦emsim, ka apgalvojums izpildās, ja $k=n$; pierādīsim, ka apgalvojums izpildās, ja $k=n+1$.
Tātad $x_{n-1}=19a$, $x_{n}=19b$, $(a, b)=1$. No šejienes seko
$$\left(x_{n}, x_{n+1}\right)=(19 b, 19(b+1))=19.$$
Apgalvojums pierādīts.












## Skaitļa n daudzkārtņu skaits intervālā

**Teorēma (par daudzkārtņu skaitu intervālā):** Starp pirmajiem $m$ naturālajiem skaitļiem 
ir tieši $\left\lfloor \frac{m}{n}\right\rfloor$ skaitla $n$ daudzkārtņu.

*Pierādījums.* Skaiț̣a $n$ daudzkārtņi, kas nepārsniedz $m$ ir uzrakstāmi formā 
$1 \cdot n, 2 \cdot n, \ldots, k \cdot n$, turklāt $kn \leq m$ un $(k+1)n > m$. Šādu daudzkārtṇu skaits ir $k$.

Pārveidojot nevienādības, iegūstam $k \leq \frac{m}{n}<k+1$. Tātad $k=\left\lfloor \frac{m}{n} \right\rfloor$.








# <lo-sample/> BBK2012.P1.122

Cik daudz ir tādu naturālu skaitļu $n \leq 1983$, kuriem $3n+5$ dalās ar $7$?

<small>

* topic:ArithmeticSeriesDivisibility
* topic:MultiplesInInterval
* topic:SequencePeriodicity

</small>

<!--
questionType=FindCount
seeAlso=LV.VO.1983.8.1
-->

## Atrisinājums

Tā kā $(3x+5)+7 = 3(x+4)$, tad skaitlis $3x+5$ dalās ar $7$ tad un tikai tad, kad ar $7$ dalās 
skaitlis $x+4$. Mums ir jānoskaidro cik intervālā $[1,1983]$ ir skaitlu $x$, kuriem $x+4$ 
dalās ar 7. Tas nozīmē, ka mums ir jānoskaidro cik intervālā [5, 1987] ir skaiţ̧u $y$, kuri dalās ar $7$.

Tādu skaiţ̦u ir $\left\lfloor \frac{1987}{7} \right\rfloor - \left\lfloor \frac{4}{7}\right \right\rfloor = 283$.



# <lo-sample/> BBK2012.P1.123

Cik daudz ir tādu naturālu skaitļu $n \leq 1000$, kuri nedalās ne ar $5$, ne ar $7$?


<small>

* topic:GcdAndLcm
* topic:ArithmeticSeriesDivisibility
* topic:SequencePeriodicity
* topic:MultiplesInInterval

</small>

<!--
questionType=FindCount
-->

## Atrisinājums

No izslēgšanas ieslēgšanas formulas seko, ka tādu skaitļu pavisam ir 
$1000 - \left\lfloor \frac{1000}{5} \right\rfloor - \left\lfloor \frac{1000}{7} \right\rfloor + \left\lfloor \frac{1000}{35} \right\rfloor = 676$.



# <lo-sample/> BBK2012.P1.124

Atrast  
**(A)** visu to naturālo skaitļu summu, kas nepārsniedz $1000$ un dalās ar $5$;  
**(B)** visu to naturālo skaitļu summu, kas nepārsniedz $1000$ un dalās 
vai nu ar $3$, vai ar $5$.

<!--
questionType=FindAll
-->

<small>

* topic:InclusionExclusionPrinciple
* topic:SequencePeriodicity

</small>


## Atrisinājums

**(A)** Šādi skaitli veido aritmētisku progresiju ar 200 locekliem, kurā pirmais loceklis 
ir $5$ un pēdējais $-1000$. Tāpēc $S_{1}=\frac{5+1000}{2} \cdot 200=100500$.

**(B)** Skaitļi, kas dalās ar $3$, veido aritmētisku progresiju, kuras summa ir 
$S_{2}=166833$. Skaiți, kas dalās ar $15$, veido aritmētisku progresiju, kuras summa ir 
$S_{3}=33165$. Meklējamā summa ir $S_{1}+S_{2}-S_{3}=234168$.



# <lo-sample/> BBK2012.P1.125

Cik daudz tādu piecciparu skaitļu, kuru pēdējais cipars ir $6$, 
un kuri dalās ar $3$?

<small>

* topic:ChineseRemainderTheorem
* topic:SequencePeriodicity

</small>

<!--
questionType=FindCount
-->


## Atrisinājums

Skaitlis $\overline{abcd}$ dalās ar 3 tad un tikai tad, kad $\overline{abcd}$ 
dalās ar 3. Tādu skaitļu pavisam ir

$$\left\lfloor \frac{9999}{3} \right\rfloor - \left\lfloor \frac{999}{3} \right\rfloor = 3000.$$



# <lo-sample/> BBK2012.P1.126

No naturāliem skaitļiem, kas nepārsniedz $1993$, izvēlieties $1328$ 
skaitļus tā, lai starp jebkuriem trim izvēlētajiem būtu vismaz divi,
kuru lielākais kopīgais dalītājs pārsniedz vieninieku.
Pietiek uzrādīt vienu šādu $1328$ skaitļu komplektu.

<small>

* topic:SequencePeriodicity

</small>

<!--
concepts=mutual-primes,gcd
questionType=FindExample
-->

## Atrisinājums

Izvēlēsimies skaitļus, kas dalās ar $2$ vai $3$. Šādu skaitļu ir

$$\left\lfloor \frac{1993}{2} \right\rfloor + \left\lfloor \frac{1993}{3}\right\rfloor - \left\lfloor \frac{1993}{6} \right\rfloor = 1328.$$

Starp jebkuriem trim no tiem būs vai nu divi, kas dalās ar $2$, vai divi, kas dalās ar $3$.



# <lo-sample/> BBK2012.P1.127

Pierādīt, ka jebkuriem naturāliem skaitļiem $n$ un $k$ izpildās vienādība 
$$\left\lfloor \frac{n}{k} \right\rfloor +
\left\lfloor \frac{n+1}{k} \right\rfloor + \ldots + 
\left\lfloor \frac{n+k-1}{k} \right\rfloor = n.$$

<!--
questionType=Prove
-->


## Atrisinājums

Ja $0 \leq j \leq k$, tad $\left[\frac{n+j}{k}\right]$ norāda tādu skaitlu skaitu, 
kas nepārsniedz $n$ un, dalot ar $k$, dod atlikumā $k-j$, ja $j \neq 0$, vai $0$, 
ja $j=0$. No šejienes seko prasītā vienādība, jo katrs skaitlis no $1$ lîdz $n$, 
daloties ar $k$, dod atlikumu no $0$ līdz $k-1$ un summā

$$\left[\frac{n}{k}\right]+\left[\frac{n+1}{k}\right]+\cdots+\left[\frac{n+k-1}{k}\right]$$

tiek ieskaitīts tieši vienu reizi.



# <lo-sample/> BBK2012.P1.128

Ar $\lfloor x \rfloor$ apzīmē lielāko veselo skaitli, kas nepārsniedz $x$. 
Pierādīt: ja $p$ un $q$ – naturāli skaitļi, kuru lielākais kopīgais dalītājs ir $1$, tad
$$\left\lfloor \frac{p}{q} \right\rfloor +
\left\lfloor \frac{2p}{q} \right\rfloor + 
\left\lfloor \frac{3p}{q} \right\rfloor + \ldots + 
\left\lfloor \frac{(q-1)p}{q} \right\rfloor =$$
$$=\left\lfloor \frac{q}{p} \right\rfloor +
\left\lfloor \frac{2q}{p} \right\rfloor + 
\left\lfloor \frac{3q}{p} \right\rfloor + \ldots + 
\left\lfloor \frac{(p-1)q}{p} \right\rfloor.$$

<!--
questionType=Prove
-->

## Atrisinājums

Pierādījumā izmanto faktu, ka skaiţ̦i $p, 2p, \ldots, (q-1)p$ 
dod visus nenulles atlikumus pēc moduḷa $q$.





# <lo-sample/> BBK2012.P1.129
	
Dots naturāls skaitlis $n$. Aprēķināt summu
$$\left\lfloor \frac{n+1}{2} \right\rfloor +
\left\lfloor \frac{n+2}{2^2} \right\rfloor + \ldots + 
\left\lfloor \frac{n+2^k}{2^{k+1}} \right\rfloor + \ldots.$$

<!--
questionType=FindAll
-->

## Atrisinājums

Apzīmēsim doto summu ar $S_{n}$. Tad

$$S_{n+1}-S_{n}=\sum_{k=0}^{\infty}\left(\left[\frac{n+2^{k}+1}{2^{k+1}}\right]-\left[\frac{n+2^{k}}{2^{k+1}}\right]\right)$$

Aprakstīsim šīs starpības

$$\left[\frac{n+2^{k}+1}{2^{k+1}}\right]-\left[\frac{n+2^{k}}{2^{k+1}}\right]=\left\{\begin{array}{c}
0, \text { ja } 2^{k+1} \text { nedala }\left(n+2^{k}+1\right) \\
1, \text { ja } 2^{k+1} \text { dala }\left(n+2^{k}+1\right) .
\end{array}\right.$$

Pien̦emsim, ka $n+1=2^{m} \cdot A$, un $A$ nedalās ar $2$. 
Skaidrs, ka $n+2^{k}+1=2^{m} \cdot A+2^{k}$ dalās ar $2^{k+1}$ tad un tikai tad, 
kad $m=k$. Tātad aplūkotā starpība nav 0 tikai vienai skaiț̣a $k$ vērtībai. 
Rezultātā iegūstam vienādību $S_{n+1}-S_{n}=1$, kas izpildās visiem $n$. 
Tā kā $S_{1}=1$, tad $S_{n}=n$.




# <lo-sample/> BBK2012.P1.130

Pierādīt, ka vienādība
$$\sum_{k=1}^n \left\lfloor \frac{n}{k} \right\rfloor = 
2 + \sum_{k=1}^{n-1} \left\lfloor \frac{n-1}{k} \right\rfloor,\;
n \in \mathbb{N}, n\geq 2$$
izpildās tad un tikai tad, kad $n$ ir pirmskaitlis.

<!--
questionType=Prove
-->



## Atrisinājums

Ievērosim, ka  
$$\sum_{k=1}^{n}\left[\frac{n}{k}\right]=\left[\frac{n}{1}\right]+\sum_{k=2}^{n-1}\left[\frac{n}{k}\right]+\left[\frac{n}{n}\right]=n+1+\sum_{k=2}^{n-1}\left[\frac{n}{k}\right]$$  
bet  
$$\sum_{k=1}^{n-1}\left[\frac{n-1}{k}\right]=\left[\frac{n-1}{1}\right]+\sum_{k=2}^{n-1}\left[\frac{n-1}{k}\right]=n-1+\sum_{k=2}^{n-1}\left[\frac{n-1}{k}\right]$$   
un pierādāmā vienādība ir ekvivalenta ar sekojošu vienādību:

$$\sum_{k=2}^{n-1}\left(\left[\frac{n}{k}\right]-\left[\frac{n-1}{k}\right]\right)=0$$

Tā kā  
$$\left(\left[\frac{n}{k}\right]-\left[\frac{n-1}{k}\right]\right)=\left\{\begin{array}{c}
0, \text { ja } k \text { nedala } n \\
1, \text { ja } k \text { dala } n,
\end{array}\right.$$  
tad dotā vienādība izpildās tad un tikai tad, kad $n$ nedalās 
ne ar vienu no skaitliem $2,3, \ldots, n-1$; t.i., kad $n$ ir pirmskaitlis.



# <lo-sample/> BBK2012.P1.131

Atrodiet visus tādus naturālus skaitļus $k$, kuriem virkne $k+1,k+2,\ldots,k+100$
satur maksimālo iespējamo pirmskaitļu skaitu.

<!--
questionType=FindAll
-->

## Atrisinājums

Eksistē tikai viens šāds skaitlis $k=1$.

Šajā gadījumā virkne $k+1, k+2, \ldots, k+100$ satur $26$ pirmskaitļus.
Ja $k \in\{2,3,4\}$, tad virknē ir $25$ pirmskaitļi. 
Ja $k \in\{5,6\}$, tad virknē $24$ pirmskaitļi. Tālāk aplūkosim $k \geq 7$. Tādā gadījumā jebkurš no skaițliem, 
kurš dalās ar $2$, $3$, $5$ vai $7$, ir salikts skaitlis. Pakāpeniski pierādām sekojošu apgalvojumus:

a. Tieši $50$ skaitļi virknē dalās ar $2$.
b. Virknē ir ne mazāk kā $16$ skaitli, kas dalās ar $3$, bet nedalās ar $2$.
c. Virknē ir ne mazāk kā $6$ skaitli, kas dalās ar $5$, bet nedalās ar $2$ vai $3$.
d. Virknē ir ne mazāk kā $3$ skaiți, kas dalās ar $7$, bet nedalās ar $2$, $3$ vai $5$.

Tātad virknē ir ne vairāk kā $100-50-16-6-3=25$ pirmskaitļi.




# <lo-sample/> BBK2012.P1.132

Ar $d(i)$ apzīmēsim skaitļa $i$ naturālo dalītāju skaitu. 
Pierādiet, ka jebkuram naturālam skaitlim $n$ izpildās vienādība 
$$d(1)+d(2)+\ldots+d(n)= \left\lfloor \frac{n}{1} \right\rfloor + 
\left\lfloor \frac{n}{2} \right\rfloor + \ldots + 
\left\lfloor \frac{n}{n} \right\rfloor.$$


<!--
questionType=Prove
-->

## Atrisinājums

Aplūkosim funkciju, kas definēta visiem naturāliem skaitlu pāriem $(i, j)$ :

$$
f(i, j)=\left\{\begin{array}{l}
0, \text { ja } i \text { nedala } j \\
1, \text { ja } i \text { dala } j
\end{array}\right.
$$

Aprēķināsim summu $\sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)$ divos dažādos veidos:

$$\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)=\sum_{i=1}^{n}\left[\frac{n}{i}\right] \\
& \sum_{i=1}^{n} \sum_{j=1}^{n} f(i, j)=\sum_{j=1}^{n} \sum_{i=1}^{n} f(i, j)=\sum_{j=1}^{n} d(j)
\end{aligned}$$

No šejienes seko pierādāmā vienādība.






