# <lo-sample/> LV.NOL.2015.12.5

Vai eksistē tādi naturāli skaitļi $a,\ b$ un $c$, ka skaitļa $a^{2}+b^{2}+c^{2}$

**(A)** pēdējie divi cipari ir $15$;  
**(B)** pēdējie četri cipari ir $2015$?

<small>

* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>

## Atrisinājums

**(A)** Jā, eksistē, piemēram, $a=9,\ b=5,\ c=3$. Tad 
$a^{2}+b^{2}+c^{2}=81+25+9=115$.

**(B)** Pierādīsim, ka šādi skaitļi neeksistē. Apskatām vienādojumu

$$\begin{equation*}
a^{2}+b^{2}+c^{2}=\overline{\ldots 2015} \tag{*}
\end{equation*}$$

Skaitlis dalās ar $8$, ja tā pēdējo trīs ciparu veidotais skaitlis dalās ar 
$8$.

Skaitli $\overline{\ldots 2015}$ dalot ar $8$, iegūst atlikumu 
$7(\overline{\ldots 2015}=\underset{\vdots 8}{\overline{\ldots 2000}}+15=\underset{\vdots 8}{\overline{\ldots 2000}}+\underset{\vdots 8}{8}+7)$.

Jebkuru naturālu skaitli var pierakstīt formā $8m+k$, kur 
$k=0,\ 1,\ \ldots,\ 7$.

Apskatām skaitļa kvadrātu 
$(8m+k)^{2}=64m^{2}+16mk+k^{2}=8 \cdot\left(8m^{2}+2mk\right)+k^{2}$. Skaitli 
$(8m+k)^{2}$ dalot ar $8$, iegūsim tādu pašu atlikumu, kā $k^{2}$, dalot ar 
$8$.

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $k^{2}$ | $0$ | $1$ | $4$ | $9$ | $16$ | $25$ | $36$ | $49$ |
| Atlikums, dalot ar $8$ | $0$ | $1$ | $4$ | $1$ | $0$ | $1$ | $4$ | $1$ |

Tātad skaitļa kvadrātu, dalot ar $8$, atlikumā var iegūt $0,\ 1,\ 4$.

Skaitli $7$ (vienādojuma $\left({ }^{*}\right)$ labās puses atlikums) nevar 
iegūt, izmantojot tikai minētos atlikumus.

Tātad vienādojumam (*) nav atrisinājuma jeb neeksistē tādi naturāli skaitļi 
$a$, $b$ un $c$, ka skaitļa $a^{2}+b^{2}+c^{2}$ pēdējie četri cipari ir $2015$.

*Piezīme.* Uzdevumu var risināt, izmantojot kongruenci pēc moduļa $8$.