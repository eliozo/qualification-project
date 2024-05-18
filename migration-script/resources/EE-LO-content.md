# <lo-sample/> EE.LO.2010.10.2

Vienādojumam
$$\frac{2}{a^2}+\frac{3}{b^2}+\frac{4}{c^2}=1$$
atrast visus atrisinājumus naturālos skaitļos.

<text lang="ru">
Для уравнения
$$\frac{2}{a^2}+\frac{3}{b^2}+\frac{4}{c^2}=1$$
найти все решения в натуральных числах.
</text>

<!--
questionType=FindAll
genre=integer-equation
-->

<small>

* topic:NumTheoryInequalityMethod
* topic:ExhaustionMethod
* strategy:ExtremeElement
* questionType:FindAll

</small>



## Atrisinājums

Aplūkosim mazāko no $a,b,c$. Ir vairāki gadījumi

(1) Nevar būt, ka minimums ir $1$, jo tad summa pārsniegtu $1$.   
(2) Ja minimālais ir $3$, tad vienādība iestājas tikai tad, ja $a=b=c=3$
(ja kaut viens ir lielāks par $3$, tad summa mazāka par $1$).   
(3) Ja $\mbox{min}(a,b,c)=2$, tad ir divas iespējas:  
(3.1) $a=2$ vai arī  
(3.2) $b = 2$. (Nevar būt $c=2$, jo tad pat viens saskaitāmais $\frac{4}{c^2}=1$.)

**Gadījums (3.1): a=2**

Ievietojam $a=2$, noīsinām un paliek vienādojums:
$$\frac{3}{b^2} + \frac{4}{c^2} = \frac{1}{2}.$$ 

Šķirojam divus apakšgadījumus atkarībā no tā, kurš saskaitāmais lielāks:

(3.1.1) $\frac{3}{b^2}\geq\frac{1}{4}$ jeb $b^2 < 12$. Ievietojot $b=2$, $\frac{3}{b^2}$ ir par lielu; 
tātad $b=3$.   
(3.1.2) $\frac{4}{c^2} > \frac{1}{4}$ jeb $c^2 < 16$. Ievietojot 
$c=2$, $\frac{4}{c^2}$ ir par lielu, tātad $c=3$. 

**Gadījumi (3.1.1) un (3.1.2):** 

(3.1.1) Ievietojot $(a,b)=(2,3)$, iegūstam:
$$\frac{4}{c^2} = 1 - \frac{2}{4} - \frac{3}{9} = \frac{1}{6}$$
jeb $c^2 = 24$, kas nevar būt. 

(3.1.2) Ievietojot $(a,c)=(2,3)$, iegūstam:
$$\frac{3}{b^2} = 1 - \frac{2}{4} - \frac{4}{9} = \frac{1}{18}.$$
jeb $b^2 = 54$, kas nevar būt. 


**Gadījums (3.2) b=2:** 

Ievietojam $b=2$, noīsinām un paliek vienādojums: 
$$\frac{2}{a^2} + \frac{4}{c^2} = \frac{1}{4}.$$

Vismaz viens no saskaitāmajiem ir vismaz puse no summas jeb $1/8$. 
Šķirojam divus apakšgadījumus: 

(3.2.1) $\frac{2}{a^2}\geq\frac{1}{8}$ jeb $a^2 \leq 16$.
 
* Ja $a=2$, tas neder - gadījumus (3.1.x) jau aplūkojām. 
* Ja $a=3$, tad $\frac{4}{c^2} = 1 - \frac{2}{9} - \frac{3}{4} = \frac{1}{36}$. 
Iegūstam, ka $c^2 = 144$, jeb $c=12$. 
* Ja $a=4$, tad $\frac{4}{c^2} = \frac{1}{8}$ jeb $c^2 = 32$, kas nevar būt. 


(3.2.2) $\frac{1}{4} > \frac{4}{c^2}\geq\frac{1}{8}$ jeb $c^2 \leq 32$.

* Ja $c=2,3,4$, tas neder, jo $\frac{4}{c^2}\geq\frac{1}{4}$. 
* Ja $c=5$, tad ievietojam $b=2$, $c=5$:
$\frac{2}{a^2} = 1 - \frac{3}{4} - \frac{4}{25} = \frac{9}{100}$
jeb $a^2 = \frac{200}{9}$, kas nevar būt.

**Atbilde:** Esam ieguvuši divus atrisinājumus:

* $(a,b,c)=(3,3,3)$.   
* $(a,b,c)=(3,2,12)$.  



# <lo-sample/> EE.LO.2011.10.2

Atrast visus naturālu skaitļu četriniekus $(w,x,y,z)$, 
kuriem izpildās vienādība $w^x + w^y = w^z$.

<text lang="ru">
Найти все четвёрки положительных целых чисел $(w, x, y, z)$, 
при которых выполняется равенство $w^x + w^y = w^z$.
</text>

<small>

* questionType:FindAll

</small>

<!--
questionType=FindAll
genre=integer-equation
-->



# <lo-sample/> EE.LO.2012.10.1

Atrast visus tādus naturālu skaitļu pārus $(n,m)$, kuriem 
skaitļu $n$ un $m$ aritmētiskais un ģeometriskais vidējais 
ir dažādi divciparu naturāli skaitļi, kuri iegūstami viens no 
otra, apmainot vietām ciparus.  
*Piezīme.* Par pozitīvu skaitļu $x$, $y$ ģeometrisko vidējo 
sauc skaitli $\sqrt{x y}$.

<small>

* questionType:FindAll

</small>

<text lang="ru">
Найти все такие пары $(n, m)$ положительных целых чисел, при которых
арифметическое и геометрическое среднее чисел $n$ и $m$ являются 
различными двузначными натуральными числами, которые одно из другого
получаются перестановкой цифр.  
*Замечание.* Геометрическим средним положительных чисел $x$, $y$ называется 
число $\sqrt{x y}$.
</text>

<!--
questionType=FindAll
genre=digit-manipulation
concepts=square-root,arithmetic-mean,geometric-mean
-->



# <lo-sample/> EE.LO.2012.10.5

Atrast visus naturālu skaitļu trijniekus $(x,y,z)$, kuriem 
$x \cdot y! + 2y \cdot x! = z!$.  
*Piezīme. Par naturāla skaitļa $n$ faktoriālu $n!$ sauc 
reizinājumu $1 \cdot 2 \cdot \ldots \cdot n$.*

<small>

* questionType:FindAll

</small>

<text lang="ru">
Найти все такие тройки положительных целых чисел (x, y, z), 
при которых $x \cdot y! + 2y \cdot x! = z!$.  
*Замечание. Факториалом $n!$ натурального числа $n$ 
называется произведение $1 \cdot 2 \cdot \ldots \cdot n$.*
</text>

<!--
questionType=FindAll
genre=integer-equation
concepts=factorial
-->



# <lo-sample/> EE.LO.2013.10.1

Vai skaitli $2013$ var izteikt kā divu veselu skaitļu kubu starpību?

<small>

* topic:ModularArithmetic
* topic:DivisibilityRulesForRemainders
* topic:ModularArithmetic
* topic:ModularArithmeticContradiction
* strategy:ModularArithmeticContradiction
* questionType:FindExample

</small>

<text lang="ru">
Можно ли представить число $2013$ как разность кубов двух целых чисел?
</text>

<!--
questionType=ProveDisprove
genre=integer-equation
concepts=power-sums
-->




## Atrisinājums

Ne visi atlikumi ir iespējami, ja pilnu kubu dala ar $m$. Pilnus kubus ir izdevīgi 
aplūkot pēc $7$ moduļa vai pēc $9$ moduļa.

**Apgalvojums:**

* $n^3$, dalot ar $m=7$, dod atlikumus
$0,1,6$ ($6$ vietā var rakstīt arī $-1$, kas atšķiras no $6$ par $7$). 
* $n^3$, dalot ar $m=9$, dod atlikumus
$0,1,8$ ($6$ vietā var rakstīt arī $-1$). 

Apgalvojumu priekš $m=7$ pierāda, kāpinot skaitļus no $0$ līdz $6$ kubā, 
aplūkojot atlikumus. Lielākiem skaitļiem atlikumi atkārtosies.  
Priekš $m=9$ līdzīgi aplūko skaitļus no $0$ līdz $8$
(vai, ja vēlamies, no $-4$ līdz $4$). 

$2013$ dod atlikumu $6$, dalot ar $9$ (un atlikumu $4$, dalot ar $7$).  
Atlikumu $4$, dalot ar $7$, nevar iegūt kā divu kubu starpību.
Aplūkojam "atņemšanas tabulu" $b-a$ atlikumiem (mod 7). 

| mod 7 | $a = 0$ | $a = 1$ | $a = 2$ |
| ----- | ------- | ------- | ------- | 
| b=0   | 0       | 6       | 1       | 
| b=1   | 1       | 0       | 2       | 
| b=6   | 6       | 5       | 0       | 


Atņemot divus pilnus kubus, atlikums dalot ar $7$ var būt
$0,1,2,5,6$, bet tas nevar būt $4$.  
(Līdzīgu spriedumu var arī par atlikumiem, dalot ar $m=9$.)



# <lo-sample/> EE.LO.2014.10.1

Ar $a$ un $n$ apzīmēti naturāli skaitļi. Pierādīt, ka 
$$\left\lfloor \frac{a}{n} \right\rfloor + \left\lfloor \frac{a+1}{n} \right\rfloor + \ldots + \left\lfloor \frac{a+n-1}{n} \right\rfloor = a.$$
*Piezīme.* Katram reālam skaitlim $x$, 
$\lfloor x \rfloor$ apzīmē skaitļa $x$ (apakšējo) veselo daļu, 
t.i. vislielāko veselo skaitli, kas nepārsniedz $x$.

<small>

* questionType:Prove

</small>


<text lang="ru">
Пусть $a$ и $n$ − целые положительные числа. Доказать, что
$$\left\lfloor \frac{a}{n} \right\rfloor + 
left\lfloor \frac{a+1}{n} \right\rfloor + \ldots +
left\lfloor \frac{a+n-1}{n} \right\rfloor = a.$$
*Примечание. Для каждого действительного числа $x$, $\lfloor x \rfloor$ обозначает 
целую часть числа $x$, т.е. наибольшее целое число, не превосходящее $x$.*
</text>


<!--
concepts=floor
-->





# <lo-sample/> EE.LO.2014.10.5

Ar $m$ apzīmēts naturāls skaitlis. Pierādīt, ka, ja Mari uzrakstījusi 
uz tāfeles vismaz $m+3$ skaitļus, tad Jüri vienmēr varēs izvēlēties no 
tiem $4$ tādus, ka kaut kādu divu izvēlēto skaitļu summa un atlikušo 
divu izvēlēto skaitļu summa dos vienādus atlikumus, dalot ar $m$. 


<small>

* questionType:Prove

</small>

<text lang="ru">
Пусть $m$ − положительное целое число. Доказать, что если Маша запишет
на доске по меньшей мере $m + 3$ числа, то у Пети всегда будет 
возможность выбрать из них $4$ таких, что сумма каких-то двух выбранных чисел
и сумма остальных двух выбранных чисел будут давать равные остатки
при делении на $m$.
</text>


<!--
questionType=Prove
genre=game
-->



# <lo-sample/> EE.LO.2015.10.1

Atrast visus naturālos skaitļus $n$, kas lielāki par vienu, 
kuriem 
$\frac{1}{n}$ un $\frac{1}{n + 1}$
izsakāmi kā galīgas decimāldaļas.

<small>

* questionType:FindAll

</small>

<text lang="ru">
Найти все натуральные числа $n$ большие одного, при которых 
$\frac{1}{n}$ и $\frac{1}{n + 1}$
представимы в виде конечных десятичных дробей.
</text>


<!--
concepts=decimal-fractions
-->



# <lo-sample/> EE.LO.2015.10.4

Uz tāfeles virknē viens pēc otra uzrakstīti naturālie skaitļi 
no $1$ līdz $n$, bet zem viņiem tie paši skaitļi, bet pretējā
secībā. Apzīmēsim viena zem otra uzrakstīto skaitļu reizinājumu 
summu ar $S(n)$. Piemēram, 
$S(6) = 1\cdot{}6 + 2\cdot{}5 + 3\cdot{}4 + 4\cdot{}3 + 5\cdot{}2 + 6\cdot{}1 = 56$.)
Pierādīt, ka jebkuram naturālam skaitlim $n$ izpildās vienādības
$$S(n + 1) − S(n) = 1 + 2 + \ldots + n + (n + 1),$$
$$S(n + 1) + S(n) = 1^2 + 2^2 + \ldots + n^2 + (n + 1)^2.$$

<text lang="ru">
На доске в ряд друг за другом записываются натуральные числа от $1$ до $n$,
а под ними те же самые числа, но в обратном порядке. Обозначим сумму
произведений записанных друг над другом чисел через $S(n)$. (Например,
$S(6) = 1\cdot{}6 + 2\cdot{}5 + 3\cdot{}4 + 4\cdot{}3 + 5\cdot{}2 + 6\cdot{}1 = 56$.)
Доказать, что для каждого натурального числа $n$ выполняются равенства
$$S(n + 1) − S(n) = 1 + 2 + \ldots + n + (n + 1),$$
$$S(n + 1) + S(n) = 1^2 + 2^2 + \ldots + n^2 + (n + 1)^2.$$
</text>

<!--
questionType=Prove
genre=sequence-properties
-->




# <lo-sample/> EE.LO.2016.10.1

Atrast visus tos četrciparu skaitļus, kuri ir tieši par $2016$ lielāki 
par skaitli, ko iegūst, pārliekot pirmo ciparu uz beigām.

<text lang="ru">
Найти все такие четырёхзначные числа, которые ровно на $2016$ больше
числа, полученного путём переставления первой цифры в конец.
</text>

<!--
questionType=FindAll
genre=digit-manipulation
-->




# <lo-sample/> EE.LO.2016.10.2

Atrast visus veselu skaitļu pārus $(a,b)$, kuriem izpildās vienādība
$$3(a^2 + b^2) - 7(a + b) = -4.$$

<text lang="ru">
Найти все пары целых чисел $(a, b)$, для которых выполняется равенство
$$3(a^2 + b^2) − 7(a + b) = −4.$$
</text>

<!--
questionType=FindAll
genre=integer-equation
-->



# <lo-sample/> EE.LO.2017.10.1

Juku izvirzījis matemātisku hipotēzi, kas apgalvo, ka jebkuram 
veselam skaitlim $n > 4$ vismaz viens no diviem lielākajiem skaitļiem, 
kuri mazāki par $\frac{n}{2}$, ir savstarpējs pirmskaitlis ar $n$. 
Vai Juku hipotēze ir patiesa?  
*Piezīme. Vesels skaitlis $a$ ir savstarpējs pirmskaitlis ar veselu 
skaitli $b$, ja lielākais kopīgais dalītājs $\mbox{LKD}(a,b)=1$.*

<text lang="ru">
Петя выдвинул математическую гипотезу, согласно которой для каждого 
целого числа $n > 4$ по крайней мере одно из двух наибольших целых
чисел, меньших чем $\frac{n}{2}$, взаимно просто с числом $n$. Верна ли гипотеза
Пети?  
Примечание. Целое число $a$ взаимно просто с целым числом $b$, если
$\mbox{НОД}(a, b) = 1$.
</text>


<!--
questionType=ProveDisprove
concepts=coprimes
-->



# <lo-sample/> EE.LO.2017.10.5

a) Uz tāfeles uzrakstīts trīsciparu skaitļa vispārīgais izskats 
$\overline{ABC}$. 
Anija un Enija pēc kārtas katrā savā gājienā nomaina vienu burtu 
ar ciparu, sāk Anija. Vai Anija varēs tā ierakstīt ciparus, ka neatkarīgi 
no Enijas gājiena iegūtais trīsciparu skaitlis dalīsies ar $11$? 
(Dažādus burtus var aizstāt arī ar to pašu ciparu, bet burtu "A" 
nevar aizstāt ar $0$.)  
b) Anija un Enija vairs negribēja katras spēles sākumā rakstīt 
skaitļa vispārīgo izskatu un nolēma izmainīt noteikumus: 
vispirms Anija uzraksta vienu ciparu, pēc tam Enija raksta tam pa 
labi vai pa kreisi otru ciparu, visbeidzot Anija pieraksta pa 
labi vai pa kreisi jau uzrakstītajiem cipariem trešo 
(ierakstīt starp esošajiem cipariem nav atļauts). 
Vai Anija varēs tā ierakstīt ciparus, ka neatkarīgi no Enijas gājiena
rezultātā būs trīsciparu skaitlis (t.i. pirmais cipars nav $0$), kas
dalās ar $11$? 

<text lang="ru">
а) На доске записан общий вид трёхзначного числа $\overline{ABC}$. 
Аня и Женя по очереди заменяют каждым ходом одну букву цифрой, 
начинает Аня. Сможет ли Аня так записывать цифры, что независимо 
от хода Жени полученное в итоге трёхзначное число делилось бы на $11$? 
(Разные буквы можно заменять одной и той же цифрой, но букву A нельзя
заменять на $0$.)  
б) Аня и Женя утомились в начале каждой игры записывать общий вид
числа и решили изменить правила: сперва Аня записывает одну цифру, 
затем Женя справа или слева от неё вторую, а в конце Аня 
записывает вправо или влево от записанных на доске двух цифр третью 
(между цифрами записывать не разрешается). Сможет ли Аня так
записывать цифры, что независимо от хода Жени в итоге получится
трёхзначное число (т.е. первая цифра не $0$), делящееся на $11$?
</text>

<!--
questionType=Algorithm,ProveDisprove
genre=game
-->




# <lo-sample/> EE.LO.2018.10.1

Atrast visus veselu skaitļu pārus $(a, b)$, kuriem
$$(2a^2 + b)^3 = b^3a.$$

<text lang="ru">
Найти все пары целых чисел (a, b), при которых
$$(2a^2 + b)^3 = b^3a.$$
</text>

<!--
questionType=FindAll
genre=integer-equation
-->



# <lo-sample/> EE.LO.2019.10.1

Atrast visus veselu skaitļu pārus $(x, y)$, kuriem $x − y = \frac{x}{y}$.


<small>

* topic:StandardIdentities
* topic:MutualPrimes

</small>

<text lang="ru">
Найти все пары целых чисел $(x, y)$, при которых $x − y = \frac{x}{y}$.
</text>

<!--
questionType=FindAll
genre=integer-equation
-->


## Atrisinājums

$$xy - y^2 = x\;\Rightarrow\;xy-x=y^2\;\Rightarrow\;x(y-1)=y^2.$$

* Ja $y \geq 0$, tad der $y=2$. Un atrisinājums $(x;y)=(4;2)$.
* Citi $y \geq 0$ neder: 
    - $y=0$ neder (ar nulli nevar dalīt)
    - $y=1$ neder, jo $x-1 \neq x$
    - $y^2$ nedalās ar $y-1$, ja tas lielāks par $1$. 
* Vērtības $y < 0$ arī neder (arī $y^2$ nedalās ar $y-1$, kas
ir divi pēc kārtas sekojoši skaitļi, kuriem nav kopīgu dalītāju).



