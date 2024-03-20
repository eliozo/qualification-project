# Dalāmības īpašības: Uzdevumu piemēri

# <lo-sample/> BBK2012.P1.E2.1

Dots, ka $5 \mid a$ un $5 \mid b$. Pierādiet, ka 
$5 \mid (a^2 + 7b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

$5 \mid a$, tātad $5 \mid a^2$ (īpašība **D2**); 
$5 \mid b$, tātad $5 \mid 7b$ (īpašība **D2**). 
No īpašības **D1** seko, ka $5 \mid (a^2 + 7b)$.



# <lo-sample/> BBK2012.P1.E2.2

Dots, ka $7 \mid a$. Pierādiet, ka $7 \mid (a^2 + 3a + 7b - 21)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

$7 \mid a$, tātad $7 \mid a^2$ un $7 \mid 3a$ (īpašība **D2**); 
$7 \mid 7b$ un $7 \mid 21$. No īpašības **D3** seko, ka 
$7 \mid (a^2 + 3a ­+ 7b - 21)$.




# <lo-sample/> BBK2012.P1.E2.3
 
Dots, ka $n \mid a$ un $n \mid (5a + b)$. Pierādiet, ka $n \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

$b = (5a + b) - 5a$. Tā kā $n \mid (5a + b)$ un $n \mid 5a$ 
(jo $n \mid a$), tad $n$ ir šo skaitļu starpības dalītājs, t.i., $n \mid b$.



# <lo-sample/> BBK2012.P1.E2.4

Dots, ka $n \mid (a - b)$. Pierādiet, ka $n \mid (a^2 + a - b^2 - b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

Izteiksmi $a­^­­­­­­2 + a - b2 - b$ var sadalīt reizinātājos 
$(a - b)(a + b + 1)$. Tā kā $n \mid (a - b)$, 
tad no īpašības **D2** seko, ka $n \mid (a^­­­­­­­2 + a - b^2 - b)$.



# <lo-sample/> BBK2012.P1.E2.5

Dots, ka $n \mid 3a$ un $n \mid (12a + 5b)$. Pierādiet, ka $n \mid 10b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No īpašības **D3** seko, ka $n \mid 5b = (12a +5b) - 4 \cdot 3a$. 
Tātad $n$ dala arī $10b$ (īpašība **D2**).


# <lo-sample/> BBK2012.P1.E2.6

Dots, ka $5 \mid (a - b)$ un $7 \mid (a + b)$. Pierādiet, ka $35 \mid (a^2 - b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No īpašības **D5** seko, ka $5 \cdot 7 = 35 \mid (a-b)(a+b) = a^2 - b^2$.



# <lo-sample/> BBK2012.P1.E2.7

Doti tādi naturāli skaitļi $a, b, c$, ka $a \mid b$, 
$b \mid c$, $c \mid a$. Pierādiet, ka 
$a = b = c$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

Apgalvojums seko no vienādības $a^2 + a - 2 = (a -1)(a + 2)$ un īpašības **D5**.


# <lo-sample/> BBK2012.P1.E2.9

Kuri no skaitļiem $101, 111, 141, 143, 155, 161, 163$ ir pirmskaitļi?

<small>

* skill:DivisibilityProperties
* questionType:Find.All

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
* questionType:Find.All

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
* questionType:Find.All

</small>

## Atrisinājums

Dotajā intervālā pirmskaitļi ir skaitļi  $181$, $191$, $193$, $197$ un $199$.
Citi neder, jo $3 \mid 183$, $5 \mid 185$, $11 \mid 187$, 
$3 \mid 189$, $5 \mid 195$ (vai arī ir pāra skaitļi).  

# <lo-sample/> BBK2012.P1.E2.12

Ar kādām naturālām $n$ vērtībām skaitlis $n^2 - 1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:Find.All

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

No pirmskaitļu 2.īpašības seko, ka $5 \mid 12$ vai $5 \mid a$. 
Tā kā $\operatorname{gcd}(5, 12) = 1$, tad $5 \mid a$.


# <lo-sample/> BBK2012.P1.E2.14

Dots, ka $7 \mid a$ un $7 \mid (2a + 3b)$. Pierādiet, ka $7 \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No īpašības **D3** seko, ka $7 \mid (2a + 3b) - 2a = 3b$. 
No pirmskaitļu 2 īpašības seko, ka $7 \mid b$.



# <lo-sample/> BBK2012.P1.E2.15

Dots, ka $5 \mid 7b$ un $7 \mid 5a$. Pierādiet, ka $35 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No pirmskaitļu 2.īpašības seko, ka $5 \mid b$ un $7 \mid a$. 
Tātad $35 \mid ab$ (īpašība **D5**).



# <lo-sample/> BBK2012.P1.E2.16

Dots, ka $n \mid (5a + 3b)$ un $n \mid (3a + 2b)$. 
Pierādiet, ka $n \mid a$ un $n \mid b$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

Seko no tā, ka $a = 5 (3a + 7b) - 7 (2a + 5b)$ un 
$b = 3 (2a + 5b) - 2 (3a + 7b)$.




# <lo-sample/> BBK2012.P1.E2.18

Dots, ka $5 \mid (3a + 4b)$ un $5 \mid (2a + 3b)$. 
Pierādiet, ka $25 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

Viens no skaitļiem $n$ vai $n + 1$ ir pāra skaitlis, 
tāpēc $n^2+ n = n(n + 1)$ dalās ar $2$. Tātad $2 \mid (n^2+ n + 6)$.



# <lo-sample/> BBK2012.P1.E2.20

Dots, ka $n \mid (a - b)$. Pierādiet, ka $n \mid (a^3 + a^2 - b^3 - b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

Seko no tā, ka $a^3 + a^2 - b^3 - b^2 = (a^3 - b^3) + (a^2 - b^2)$,   
$(a^3 - b^3) + (a^2 - b^2) = (a - b)(a^2 + ab + b2) + (a - b)(a + b)$.  
Abi saskaitāmie dalās ar $a-b$, tātad arī ar $n$. 


# <lo-sample/> BBK2012.P1.E2.21

Dots, ka $n \mid (a + 2b)$. Pierādiet, ka $n \mid (a^3 + 2a + 8b^3 + 4b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:ProveDisprove.ForAll

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
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

No $a \mid (a + b)$ seko, ka $a \mid b$. Līdzīgi iegūstam, ka $b \mid a$. 
No īpašības **D6** seko, ka $a = b$.




# <lo-sample/> BBK2012.P1.E2.25

Dots, ka $2 \mid (a - 1)$ un $3 \mid (a + 1)$. 
Pierādiet, ka $6 \mid (a^2 + 5)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No dalāmības īpašībām seko, ka $6 \mid (a - 1)(a + 1) = a^2 - 1$. 
Tātad $6 \mid (a^2 + 5)$, jo $a^2 + 5 = (a^2 - 1) + 6$.




# <lo-sample/> BBK2012.P1.E2.26

Dots, ka $6 \mid (a - b)$ un $6 \mid (a + b)$. 
Pierādiet, ka $3 \mid (a^2 + 8b^2)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No tā, ka $6 \mid (a - b)$ seko, ka $6 \mid (a^2 - b^2) = (a - b)(a + b)$. 
No īpašības **D1** seko, ka $6 \mid (a^2 - b^2 + 6b^2) = a^2 + 5b^2$. 
Tā kā $3 \mid 6$, tad arī $3 \mid (a^2 + 5b^2)$.



# <lo-sample/> BBK2012.P1.E2.27

Ar kādām naturālām $n$ vērtībām skaitlis $n^3-1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:Find.All

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
* questionType:Find.All

</small>

## Atrisinājums

Skaitlis $n^2 + 5n + 6 = (n + 2)(n + 3)$ nav pirmskaitlis 
nevienai n vērtībai, jo tas sadalās reizinātājos, kuri ir lielāki par $1$.






# <lo-sample/> BBK2012.P1.E2.29

Ar kādām naturālām $a$ un $b$ vērtībām skaitlis 
$ab + a + b + 1$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:Find.All

</small>

## Atrisinājums

Izteiksmi $ab + a + b + 1$ sadalām reizinātājos $(a+1)(b+1)$. 
Tātad šis skaitlis nav pirmskaitlis nekādām $a$ un $b$ vērtībām, 
jo abi reizinātāji ir lielāki par $1$.



# <lo-sample/> BBK2012.P1.E2.30

Dots, ka $4 \mid x$ un $3 \mid y$. Pierādiet, ka $12 \mid (xy + 8y + 9x)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

No uzdevuma nosacījumiem seko, ka skaitlis $4(a + 4b) - (4a +b) = 15b$ 
dalās ar $11$. No pirmskaitļu 2. īpašības izriet, ka $11 \mid b$. 
Līdzīgi pierāda, ka $11 \mid a$.



# <lo-sample/> BBK2012.P1.E2.32

Dots, ka $7 \mid (3a + b)$ un $7 \mid (a + 3b)$. Pierādiet, ka $49 \mid ab$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

$7 \mid (3(a + 3b) - (3a + b)) = 8b$. 
Tātad, $7 \mid b$. Līdzīgi pierāda, ka $7 \mid a$. 
No īpašības **D5** seko, ka $49 \mid ab$.




# <lo-sample/> BBK2012.P1.E2.33

Dots, ka $7 \mid (2a + 3b)$. Pierādiet, ka $7 \mid (a + 5b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No dotā seko, ka $7 \mid 4(2a +3b) = 8a + 12b$. 
Tātad arī skaitlis 
$a + 5b = 8a + 12b - 7(a + b)$ dalās ar $7$.




# <lo-sample/> BBK2012.P1.E2.34

Dots, ka $13 \mid (a + 4b)$. Pierādiet, ka $13 \mid (10a + b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

</small>

## Atrisinājums

No dotā seko, ka $13 \mid 10(a +4b) = 10a + 40b$. Tātad arī skaitlis 
$10a + b = (10a + 40b) - 39b$ dalās ar $13$.





# <lo-sample/> BBK2012.P1.E2.35

Dots, ka $11 \mid (3a + 7b)$. Pierādiet, ka $11 \mid (4a + 2b)$.

<small>

* skill:DivisibilityProperties
* questionType:Prove.ForAll

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
* questionType:Prove.ForAll

</small>

## Atrisinājums

Ja $17 \mid (4a +5b)$, tad arī skaitlis $6(4a +5b) = 24a + 30b$ dalās ar $17$. Tas nozīmē, ka skaitlis $7a - 4b = 24a + 30b - 17(a + 2b)$ dalās ar $17$.
Līdzīgi pierāda apgriezto apgalvojumu.





# <lo-sample/> BBK2012.P1.E2.37

Ar kādām naturālām $n$ un $m$ vērtībām skaitlis 
$(n-m)(n^2+m-1)$ ir pirmskaitlis?

<small>

* skill:DivisibilityProperties
* questionType:Find.All

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
* questionType:Find.Any

</small>

## Atrisinājums

Uzdevuma nosacījumus apmierina, piemēram, skaitlis 
$n = 12! +2 = 479001602$. 
Tiešām, ja $1 < k < 13$ , tad $12! + k$ ir salikts skaitlis, 
jo $k$ ir šā skaitļa dalītājs.

Ir arī daudz mazāki atrisinājumi, piemēram $n=114$. 
Intervālā $[114;126]$ nav neviena pirmskaitļa.




