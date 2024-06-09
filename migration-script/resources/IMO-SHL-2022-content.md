# <lo-sample/> IMO_SHL.2022.A1

Let $(a_n)_{n\geq 1}$ be a sequence of positive real numbers with the property that

$$(a_{n+1})^2 + a_na_{n+2} \leq a_n + a_{n+2}$$

for all positive integers $n$. Show that $a_{2022}\leq 1$.

<small>

* domain:Alg
* source:Nigeria
* questionType:Prove
* concepts:sequence,real-numbers,integer-numbers

</small>

## Solution

We begin by observing that 
$\left(a_{n+1}\right)^{2}-1 \leqslant a_{n}+a_{n+2}-a_{n} a_{n+2}-1$, which is equivalent to

$$\left(a_{n+1}\right)^{2}-1 \leqslant\left(1-a_{n}\right)\left(a_{n+2}-1\right)$$

Suppose now that there exists a positive integer $n$ such that $a_{n+1}>1$ and $a_{n+2}>1$. 
Since $\left(a_{n+1}\right)^{2}-1 \leqslant\left(1-a_{n}\right)\left(a_{n+2}-1\right)$, 
we deduce that $0<1-a_{n}<1<1+a_{n+2}$, thus 
$\left(a_{n+1}\right)^{2}-1<\left(a_{n+2}+1\right)\left(a_{n+2}-1\right)=\left(a_{n+2}\right)^{2}-1$.

On the other hand, 
$\left(a_{n+2}\right)^{2}-1 \leqslant\left(1-a_{n+3}\right)\left(a_{n+1}-1\right)<\left(1+a_{n+1}\right)\left(a_{n+1}-1\right)=\left(a_{n+1}\right)^{2}-1$, 
a contradiction. We have shown that we cannot have two consecutive terms, 
except maybe $a_{1}$ and $a_{2}$, strictly greater than $1$.

Finally, suppose $a_{2022}>1$. This implies that $a_{2021} \leqslant 1$ and $a_{2023} \leqslant 1$. 
Therefore $0< \left(a_{2022}\right)^{2}-1 \leqslant\left(1-a_{2021}\right)\left(a_{2023}-1\right) \leqslant 0$, 
a contradiction. We conclude that $a_{2022} \leqslant 1$.






# <lo-sample/> IMO_SHL.2022.A2

Let $k \ge 2$ be an integer. Find the smallest integer $n \ge k+1$ with the property that there 
exists a set of $n$ distinct real numbers such that each of its elements can be written as a 
sum of $k$ other distinct elements of the set.

<small>

* domain:Alg
* source:Slovakia
* questionType:FindOptimal
* concepts:integer-numbers

</small>


## Solution

*Answer:* $n=k+4$.

First we show that $n \geqslant k+4$. Suppose that there exists such a set 
with $n$ numbers and denote them by $a_{1}<a_{2}<\cdots<a_{n}$.

Note that in order to express $a_{1}$ as a sum of $k$ distinct elements of the set, 
we must have $a_{1} \geqslant a_{2}+\cdots+a_{k+1}$ and, similarly for $a_{n}$, 
we must have $a_{n-k}+\cdots+a_{n-1} \geqslant a_{n}$. We also know that $n \geqslant k+1$.

If $n=k+1$ then we have $a_{1} \geqslant a_{2}+\cdots+a_{k+1}>a_{1}+\cdots+a_{k} \geqslant a_{k+1}$, 
which gives a contradiction.

If $n=k+2$ then we have $a_{1} \geqslant a_{2}+\cdots+a_{k+1} \geqslant a_{k+2}$, 
that again gives a contradiction.

If $n=k+3$ then we have 
$a_{1} \geqslant a_{2}+\cdots+a_{k+1}$ and $a_{3}+\cdots+a_{k+2} \geqslant a_{k+3}$. 
Adding the two inequalities we get $a_{1}+a_{k+2} \geqslant a_{2}+a_{k+3}$, again a contradiction.

It remains to give an example of a set with $k+4$ elements satisfying the 
condition of the problem. We start with the case when $k=2 l$ and $l \geqslant 1$. 
In that case, denote by $A_{i}=\{-i, i\}$ and take the set $A_{1} \cup \cdots \cup A_{l+2}$, 
which has exactly $k+4=2 l+4$ elements. We are left to show that this set satisfies the required condition.

Note that if a number $i$ can be expressed in the desired way, 
then so can $-i$ by negating the expression. 
Therefore, we consider only $1 \leqslant i \leqslant l+2$.

If $i<l+2$, we sum the numbers from some $l-1$ sets 
$A_{j}$ with $j \neq 1, i+1$, and the numbers $i+1$ and -1 .

For $i=l+2$, we sum the numbers from some $l-1$ sets $A_{j}$ with $j \neq 1, l+1$, 
and the numbers $l+1$ and 1 .

It remains to a give a construction for odd $k=2 l+1$ with $l \geqslant 1$ 
(since $k \geqslant 2$ ). To that end, we modify the construction for $k=2 l$ 
by adding 0 to the previous set.

This is a valid set as 0 can be added to each constructed expression, 
and 0 can be expressed as follows: take the numbers $1,2,-3$ and all the numbers 
from the remaining $l-1$ sets $A_{4}, A_{5}, \cdots, A_{l+2}$.




# <lo-sample/> IMO_SHL.2022.A3

Let $\mathbb{R}^+$ denote the set of positive real numbers. Find all functions 
$f: \mathbb{R}^+ \to \mathbb{R}^+$ such that for each $x \in \mathbb{R}^+$, there is exactly one 
$y \in \mathbb{R}^+$ satisfying $$xf(y)+yf(x) \leq 2$$

<small>

* domain:Alg
* source:Netherlands
* questionType:FindAll
* concepts:real-numbers,function

</small>


## Solution

*Answer:* The function $f(x)=1/x$ is the only solution.

First we prove that the function $f(x)=1/x$ satisfies the condition of the problem statement. 
The AM-GM inequality gives

$$\frac{x}{y}+\frac{y}{x} \geqslant 2$$

for every $x, y>0$, with equality if and only if $x=y$. 
This means that, for every $x>0$, there exists a unique $y>0$ such that

$$\frac{x}{y}+\frac{y}{x} \leqslant 2$$

namely $y=x$.

Let now $f: \mathbb{R}_{>0} \rightarrow \mathbb{R}_{>0}$ be a function that satisfies 
the condition of the problem statement. We say that a pair of positive real numbers $(x, y)$ 
is good if $x f(y)+y f(x) \leqslant 2$. Observe that if $(x, y)$ is good, then so is $(y, x)$.

*Lemma 1.0.* If $(x, y)$ is good, then $x=y$.

*Proof.* Assume that there exist positive real numbers $x \neq y$ such that $(x, y)$ is good. 
The uniqueness assumption says that $y$ is the unique positive real number such that $(x, y)$ 
is good. In particular, $(x, x)$ is not a good pair. This means that

$$x f(x)+x f(x)>2$$

and thus $x f(x)>1$. Similarly, $(y, x)$ is a good pair, so $(y, y)$ is not a good pair, 
which implies $y f(y)>1$. We apply the AM-GM inequality to obtain

$$x f(y)+y f(x) \geqslant 2 \sqrt{x f(y) \cdot y f(x)}=2 \sqrt{x f(x) \cdot y f(y)}>2$$

This is a contradiction, since $(x, y)$ is a good pair.

By assumption, for any $x>0$, there always exists a good pair containing $x$, 
however Lemma 1 implies that the only good pair that can contain $x$ is $(x, x)$, so

$$x f(x) \leqslant 1 \quad \Longleftrightarrow \quad f(x) \leqslant \frac{1}{x}$$

for every $x>0$.

In particular, with $x=1/f(t)$ for $t>0$, we obtain

$$\frac{1}{f(t)} \cdot f\left(\frac{1}{f(t)}\right) \leqslant 1$$

Hence

$$t \cdot f\left(\frac{1}{f(t)}\right) \leqslant t f(t) \leqslant 1$$

We claim that $(t, 1 / f(t))$ is a good pair for every $t>0$. Indeed,

$$t \cdot f\left(\frac{1}{f(t)}\right)+\frac{1}{f(t)} f(t)=t \cdot f\left(\frac{1}{f(t)}\right)+1 \leqslant 2$$

Lemma 1 implies that $t=1 / f(t) \Longleftrightarrow f(t)=1 / t$ for every $t>0$.

Solution 1.1. We give an alternative way to prove that 
$f(x)=1/x$ assuming $f(x) \leqslant 1 / x$ for every $x>0$.

Indeed, if $f(x)<1/x$ then for every $a>0$ with $f(x)<1/a<1/x$ 
(and there are at least two of them), we have

$$a f(x)+x f(a)<1+\frac{x}{a}<2$$

Hence $(x, a)$ is a good pair for every such $a$, a contradiction. We conclude that $f(x)=1/x$.

Solution 1.2. We can also conclude from Lemma 1 and $f(x) \leqslant 1 / x$ as follows.

*Lemma 2.* The function $f$ is decreasing.

*Proof.* Let $y>x>0$. Lemma 1 says that $(x, y)$ is not a good pair, but $(y, y)$ is. Hence

$$x f(y)+y f(x)>2 \geqslant 2 y f(y)>y f(y)+x f(y)$$

where we used $y>x$ (and $f(y)>0$ ) in the last inequality. This implies that $f(x)>f(y)$, showing that $f$ is decreasing.

We now prove that $f(x)=1 / x$ for all $x$. Fix a value of $x$ and note that for $y>x$ 
we must have $x f(x)+y f(x)>x f(y)+y f(x)>2$ (using that $f$ is decreasing for the first step), 
hence $f(x)>\frac{2}{x+y}$. The last inequality is true for every $y>x>0$. 
If we fix $x$ and look for the supremum of the expression $\frac{2}{x+y}$ over all $y>x$, we get

$$f(x) \geqslant \frac{2}{x+x}=\frac{1}{x}$$

Since we already know that $f(x) \leqslant 1/x$, we conclude that $f(x)=1/x$.



## Solution

*Answer:* The function $f(x)=1/x$ is the only solution.

As in the first solution, we note that $f(x)=1 / x$ is a solution, 
and we set out to prove that it is the only one. We write $g(x)$ for the unique 
positive real number such that $(x, g(x))$ is a good pair. 
In this solution, we prove Lemma 2 without assuming Lemma 1.

*Lemma 2.* The function $f$ is decreasing.

*Proof.* Consider $x<y$. It holds that $y f(g(y))+g(y) f(y) \leqslant 2$. 
Moreover, because $y$ is the only positive real number such that $(g(y), y)$ 
is a good pair and $x \neq y$, we have $x f(g(y))+g(y) f(x)>$ 2. 
Combining these two inequalities yields

$$x f(g(y))+g(y) f(x)>2 \geqslant y f(g(y))+g(y) f(y)$$

or $f(g(y))(x-y)>g(y)(f(y)-f(x))$. Because $g(y)$ and $f(g(y))$ are both positive while 
$x-y$ is negative, it follows that $f(y)<f(x)$, showing that $f$ is decreasing.

We now prove Lemma 1 using Lemma 2. Suppose that $x \neq y$ but $x f(y)+y f(x) \leqslant 2$. 
As in the first solution, we get $x f(x)+x f(x)>2$ and $y f(y)+y f(y)>2$, which implies $x f(x)+y f(y)>2$. Now

$$x \cdot f(x)+y \cdot f(y)>2 \geqslant x \cdot f(y)+y \cdot f(x)$$

implies $(x-y)(f(x)-f(y))>0$, which contradicts the fact that $f$ is decreasing. 
So $y=x$ is the unique $y$ such that $(x, y)$ is a good pair, 
and in particular we have $f(x) \leqslant 1 / x$.

We can now conclude the proof as in Solution 1.



## Solution

As in the other solutions we verify that the function $f(x)=1/x$ is a solution. 
We first want to prove the following lemma:

*Lemma 3.* For all $x \in \mathbb{R}_{>0}$ we actually have $x f(g(x))+g(x) f(x)=2$ 
(that is: the inequality is actually an equality).

*Proof.* We proceed by contradiction: Assume there exists some number $x>0$ 
such that for $y=g(x)$ we have $x f(y)+y f(x)<2$. 
Then for any $0<\epsilon<\frac{2-x f(y)-y f(x)}{2 f(x)}$ we have, by uniqueness 
of $y$, that $x f(y+\epsilon)+(y+\epsilon) f(x)>2$. Therefore

$$\begin{align*}
f(y+\epsilon) & >\frac{2-(y+\epsilon) f(x)}{x}=\frac{2-y f(x)-\epsilon f(x)}{x} \\
& >\frac{2-y f(x)-\frac{2-x f(y)-y f(x)}{2}}{x} \\
& =\frac{2-x f(y)-y f(x)}{2 x}+f(y)>f(y) \tag{1}
\end{align*}$$

Furthermore, for every such $\epsilon$ we have 
$g(y+\epsilon) f(y+\epsilon)+(y+\epsilon) f(g(y+\epsilon)) \leqslant 2$ and 
$g(y+\epsilon) f(y)+y f(g(y+\epsilon))>2$ (since $y \neq y+\epsilon=g(g(y+\epsilon)))$. 
This gives us the two inequalities

$$f(g(y+\epsilon)) \leqslant \frac{2-g(y+\epsilon) f(y+\epsilon)}{y+\epsilon} \quad 
\text { and } \quad f(g(y+\epsilon))>\frac{2-g(y+\epsilon) f(y)}{y}$$

Combining these two inequalities and rearranging the terms leads to the inequality

$$2 \epsilon<g(y+\epsilon)[(y+\epsilon) f(y)-y f(y+\epsilon)]$$

Moreover combining with the inequality (1) we obtain

$$2 \epsilon<g(y+\epsilon)\left[(y+\epsilon) f(y)-y\left(\frac{2-x f(y)-y f(x)}{2 x}+f(y)\right)\right] = 
g(y+\epsilon)\left[\epsilon f(y)-y \frac{2-x f(y)-y f(x)}{2 x}\right]$$

We now reach the desired contradiction, since for $\epsilon$ sufficiently small we have 
that the left hand side is positive while the right hand side is negative.

With this lemma it then follows that for all $x, y \in \mathbb{R}_{>0}$ we have

$$x f(y)+y f(x) \geqslant 2$$

since for $y=g(x)$ we have equality and by uniqueness for $y \neq g(x)$ the inequality is strict.

In particular for every $x \in \mathbb{R}_{>0}$ and for $y=x$ we have $2 x f(x) \geqslant 2$, 
or equivalently $f(x) \geqslant 1 / x$ for all $x \in \mathbb{R}_{>0}$. 
With this inequality we obtain for all $x \in \mathbb{R}_{>0}$

$$2 \geqslant x f(g(x))+g(x) f(x) \geqslant \frac{x}{g(x)}+\frac{g(x)}{x} \geqslant 2$$

where the first inequality comes from the problem statement. Consequently each of these 
inequalities must actually be an equality, and in particular we obtain 
$f(x)=1/x$ for all $x \in \mathbb{R}_{>0}$.

## Solution

Again, let us prove that $f(x)=1 / x$ is the only solution. 
Let again $g(x)$ be the unique positive real number such that $(x, g(x))$ is a good pair.

*Lemma 4.* The function $f$ is strictly convex.

Proof. Consider the function $q_{s}(x)=f(x)+s x$ for some real number $s$. 
If $f$ is not strictly convex, then there exist $u<v$ and $t \in(0,1)$ such that

$$f(t u+(1-t) v) \geqslant t f(u)+(1-t) f(v)$$

Hence

$$\begin{aligned}
q_{s}(t u+(1-t) v) & \geqslant t f(u)+(1-t) f(v)+s(t u+(1-t) v) \\
& =t q_{s}(u)+(1-t) q_{s}(v)
\end{aligned}$$

Let $w=t u+(1-t) v$ and consider the case $s=f(g(w)) / g(w)$. For that particular choice of $s$, 
the function $q_{s}(x)$ has a unique minimum at $x=w$. However, since 
$q_{s}(w) \geqslant t q_{s}(u)+(1-t) q_{s}(v)$, it must hold 
$q_{s}(u) \leqslant q_{s}(w)$ or $q_{s}(v) \leqslant q_{s}(w)$, a contradiction.

*Lemma 5.* The function $f$ is continuous.

*Proof.* Since $f$ is strictly convex and defined on an open interval, it is also continuous.

As in Solution 1, we can prove that $f(x) \leqslant 1 / x$. If $f(x)<1 / x$, 
then we consider the function $h(y)=x f(y)+y f(x)$ which is continuous. 
Since $h(x)<2$, there exist at least two distinct $z \neq x$ such that 
$h(z)<2$ giving that $(x, z)$ is good pair for both values of $z$, 
a contradiction. We conclude that $f(x)=1/x$ as desired.

*Comment.* Lemma 5 implies Lemma 3, using an argument similar as in the end of Solution 4.





# <lo-sample/> IMO_SHL.2022.A4

Let $n \geqslant 3$ be an integer, and let $x_1,x_2,\ldots,x_n$ be real numbers in the interval 
$[0,1]$. Let $s=x_1+x_2+\ldots+x_n$, and assume that $s \geqslant 3$. 
Prove that there exist integers $i$ and $j$ with $1 \leqslant i<j \leqslant n$ such that

$$2^{j-i}x_ix_j>2^{s-3}.$$

<small>

* domain:Alg
* source:Trinidad and Tobago
* questionType:Prove
* concepts:real-numbers,integer-numbers

</small>


## Solution.

Let $1 \leqslant a<b \leqslant n$ be such that $2^{b-a} x_{a} x_{b}$ is maximal. 
This choice of $a$ and $b$ implies that $x_{a+t} \leqslant 2^{t} x_{a}$ for all 
$1-a \leqslant t \leqslant b-a-1$, and similarly $x_{b-t} \leqslant 2^{t} x_{b}$ 
for all $b-n \leqslant t \leqslant b-a+1$. 
Now, suppose that $x_{a} \in\left(\frac{1}{2^{u+1}}, \frac{1}{2^{u}}\right]$ and 
$x_{b} \in\left(\frac{1}{2^{v+1}}, \frac{1}{2^{v}}\right]$, 
and write $x_{a}=2^{-\alpha}, x_{b}=2^{-\beta}$. Then

$$\sum_{i=1}^{a+u-1} x_{i} \leqslant 2^{u} x_{a}\left(\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2^{a+u-1}}\right) 
< 2^{u} x_{a} \leqslant 1$$

and similarly,

$$\sum_{i=b-v+1}^{n} x_{i} \leqslant 2^{v} x_{b}\left(\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2^{n-b+v}}\right)
< 2^{v} x_{b} \leqslant 1$$

In other words, the sum of the $x_{i}$ 's for $i$ outside of the interval $[a+u, b-v]$ 
is strictly less than 2. Since the total sum is at least $3$, and each term is at most $1$, 
it follows that this interval must have at least two integers. 
i.e., $a+u<b-v$. Thus, by bounding the sum of the $x_{i}$ for $i \in[1, a+u] \cup[b-v, n]$ 
like above, and trivially bounding each $x_{i} \in(a+u, b-v)$ by 1 , we obtain

$$s<2^{u+1} x_{a}+2^{v+1} x_{b}+((b-v)-(a+u)-1)=b-a+\left(2^{u+1-\alpha}+2^{v+1-\beta}-(u+v+1)\right)$$

Now recall $\alpha \in(u, u+1]$ and $\beta \in(v, v+1]$, so applying Bernoulli's inequality yields $\left.2^{u+1-\alpha}+2^{v+1-\beta}-u-v-1 \leqslant(1+(u+1-\alpha))\right)+(1+(v+1-\beta))-u-v-1=3-\alpha-\beta$.

It follows that $s-3<b-a-\alpha-\beta$, and so

$$2^{s-3}<2^{b-a-\alpha-\beta}=2^{b-a} x_{a} x_{b}$$

*Comment 1.* It is not hard to see that the inequality is tight. 
Suppose that $n = 2k+1$, and we set $x_{k+1}=1, x_{k}=x_{k+2}=\frac{1}{2}+\frac{1}{2^{k}}$, 
and $x_{k+1-t}=x_{k+1+t}=\frac{1}{2^{t}}$. Then $s=3$ (so the right hand side is 1), and

$$\max _{i<j} 2^{j-i} x_{i} x_{j}=2^{2}\left(\frac{1}{2}+\frac{1}{2^{k}}\right)^{2}$$

which can be made arbitrarily close to 1 . Note that $s$ can be made larger by putting in more $1$s in the middle (and this accommodates even $n$ as well).

*Comment 2.* An alternative formulation of the problem is to show that there exists 
a positive constant $c$ (or find the best such $c$ ) such that

$$\max _{i<j} 2^{j-i} x_{i} x_{j}>c 2^{s}$$

The above shows that $c=1 / 8$ is the best possible. A somewhat simpler ending to the proof can be given for $c=1 / 32$.

End of solution for $c=1/32$.

As in the original solution, we arrive at

$$s<2^{u+1} x_{a}+2^{v+1} x_{b}+((b-v)-(a+u)-1)=b-a+\left(2^{u+1-\alpha}+2^{v+1-\beta}-(u+v+1)\right)$$

Now $2^{b-a} x_{a} x_{b} \geqslant 2^{b-a} 2^{-u-1} 2^{-v-1}$, so it is enough to show $s-5<b-a-u-v-2$, 
or $s<b-a-$ $u-v+3$. The fact that $u+1-\alpha<1$ and $v+1-\beta<1$ implies 
$2^{u+1-\alpha}+2^{v+1-\beta}<4$, and so $s<b-a+(2+2-u-v-1)=b-a-u-v-3$.




# <lo-sample/> IMO_SHL.2022.A5

Find all positive integers $n \geqslant 2$ for which there exist $n$ real numbers 
$a_1<\cdots<a_n$ and a real number $r>0$ such that the $\tfrac{1}{2}n(n-1)$ differences 
$a_j-a_i$ for $1 \leqslant i<j \leqslant n$ are equal, in some order, to the numbers 
$r^1,r^2,\ldots,r^{\frac{1}{2}n(n-1)}$.

<small>

* domain:Alg
* source:Czech Republic
* questionType:FindAll
* concepts:integer-numbers,real-numbers

</small>

## Solution

*Answer:* $n \in\{2,3,4\}$.

We first show a solution for each $n \in\{2,3,4\}$. We will later show the impossibility of 
finding such a solution for $n \geqslant 5$.

For $n=2$, take for example $\left(a_{1}, a_{2}\right)=(1,3)$ and $r=2$.

For $n=3$, take the root $r>1$ of $x^{2}-x-1=0$ (the golden ratio) and set 
$\left(a_{1}, a_{2}, a_{3}\right)=$ $\left(0, r, r+r^{2}\right)$. Then

$$\left(a_{2}-a_{1}, a_{3}-a_{2}, a_{3}-a_{1}\right)=\left(r, r^{2}, r+r^{2}=r^{3}\right)$$

For $n=4$, take the root $r \in(1,2)$ of $x^{3}-x-1=0$ (such a root exists because $1^{3}-1-1<0$ 
and $\left.2^{3}-2-1>0\right)$ and set 
$\left(a_{1}, a_{2}, a_{3}, a_{4}\right)=\left(0, r, r+r^{2}, r+r^{2}+r^{3}\right)$. Then

$$\left(a_{2}-a_{1}, a_{3}-a_{2}, a_{4}-a_{3}, a_{3}-a_{1}, a_{4}-a_{2}, a_{4}-a_{1}\right) = 
\left(r, r^{2}, r^{3}, r^{4}, r^{5}, r^{6}\right)$$

For $n \geqslant 5$, we will proceed by contradiction. Suppose there exist numbers 
$a_{1}<\cdots<a_{n}$ and $r>1$ satisfying the conditions of the problem. We start with a lemma:

*Lemma.* We have $r^{n-1}>2$.

Proof. There are only $n-1$ differences $a_{j}-a_{i}$ with $j=i+1$, 
so there exists an exponent $e \leqslant n$ and a difference $a_{j}-a_{i}$ 
with $j \geqslant i+2$ such that $a_{j}-a_{i}=r^{e}$. This implies

$$r^{n} \geqslant r^{e}=a_{j}-a_{i}=\left(a_{j}-a_{j-1}\right)+\left(a_{j-1}-a_{i}\right)>r+r=2r$$

thus $r^{n-1}>2$ as desired.

To illustrate the general approach, we first briefly sketch the idea behind the argument 
in the special case $n=5$. In this case, we clearly have $a_{5}-a_{1}=r^{10}$. 
Note that there are 3 ways to rewrite $a_{5}-a_{1}$ as a sum of two differences, namely

$$\left(a_{5}-a_{4}\right)+\left(a_{4}-a_{1}\right),\left(a_{5}-a_{3}\right)+\left(a_{3}-a_{1}\right),
\left(a_{5}-a_{2}\right)+\left(a_{2}-a_{1}\right)$$

Using the lemma above and convexity of the function $f(n)=r^{n}$, 
we argue that those three ways must be $r^{10}=r^{9}+r^{1}=r^{8}+r^{4}=r^{7}+r^{6}$. 
That is, the "large" exponents keep dropping by 1 , while the "small" exponents 
keep increasing by $n-2, n-3, \ldots, 2$. Comparing any two such equations, 
we then get a contradiction unless $n \leqslant 4$.

Now we go back to the full proof for any $n \geqslant 5$. 
Denote $b=\frac{1}{2} n(n-1)$. Clearly, we have $a_{n}-a_{1}=r^{b}$. Consider the $n-2$ equations of the form:

$$a_{n}-a_{1}=\left(a_{n}-a_{i}\right)+\left(a_{i}-a_{1}\right) \text { for } i \in\{2, \ldots, n-1\}$$

In each equation, one of the two terms on the right-hand side must be at least 
$\frac{1}{2}\left(a_{n}-a_{1}\right)$. But from the lemma we have 
$r^{b-(n-1)}=r^{b} / r^{n-1}<\frac{1}{2}\left(a_{n}-a_{1}\right)$, 
so there are at most $n-2$ sufficiently large elements in 
$\left\{r^{k} \mid 1 \leqslant k<b\right\}$, namely $r^{b-1}, \ldots, r^{b-(n-2)}$ 
(note that $r^{b}$ is already used for $a_{n}-a_{1}$ ). 
Thus, the "large" terms must be, in some order, precisely equal to elements in

$$L=\left\{r^{b-1}, \ldots, r^{b-(n-2)}\right\}$$

Next we claim that the "small" terms in the $n-2$ equations must be equal to the elements in

$$S=\left\{\left.r^{b-(n-2)-\frac{1}{2} i(i+1)} \right\rvert\, 1 \leqslant i \leqslant n-2\right\}$$

in the corresponding order (the largest "large" term with the smallest 
"small" term, etc.). Indeed, suppose that

$$r^{b}=a_{n}-a_{1}=r^{b-i}+r^{\alpha_{i}} \text { for } i \in\{1, \ldots, n-2\}$$

where $1 \leqslant \alpha_{1}<\cdots<\alpha_{n-2} \leqslant b-(n-1)$. 
Since $r>1$ and $f(r)=r^{n}$ is convex, we have

$$r^{b-1}-r^{b-2}>r^{b-2}-r^{b-3}>\ldots>r^{b-(n-3)}-r^{b-(n-2)}$$

implying

$$r^{\alpha_{2}}-r^{\alpha_{1}}>r^{\alpha_{3}}-r^{\alpha_{2}}>\ldots>r^{\alpha_{n-2}}-r^{\alpha_{n-3}}$$

Convexity of $f(r)=r^{n}$ further implies

$$\alpha_{2}-\alpha_{1}>\alpha_{3}-\alpha_{2}>\ldots>\alpha_{n-2}-\alpha_{n-3}$$

Note that $\alpha_{n-2}-\alpha_{n-3} \geqslant 2$ : Otherwise we would have $\alpha_{n-2}-\alpha_{n-3}=1$ and thus

$$r^{\alpha_{n-3}} \cdot(r-1)=r^{\alpha_{n-2}}-r^{\alpha_{n-3}}=r^{b-(n-3)}-r^{b-(n-2)}=r^{b-(n-2)} \cdot(r-1)$$

implying that $\alpha_{n-3}=b-(n-2)$, a contradiction. Therefore, we have

$$\begin{aligned}
\alpha_{n-2}-\alpha_{1} & =\left(\alpha_{n-2}-\alpha_{n-3}\right)+\cdots+\left(\alpha_{2}-\alpha_{1}\right) \\
& \geqslant 2+3+\cdots+(n-2) \\
& =\frac{1}{2}(n-2)(n-1)-1=\frac{1}{2} n(n-3)
\end{aligned}$$

On the other hand, from $\alpha_{n-2} \leqslant b-(n-1)$ and $\alpha_{1} \geqslant 1$ we get

$$\alpha_{n-2}-\alpha_{1} \leqslant b-n=\frac{1}{2} n(n-1)-n=\frac{1}{2} n(n-3)$$

implying that equalities must occur everywhere and the claim about the small terms follows.

Now, assuming $n-2 \geqslant 2$, we have the two different equations:

$$r^{b}=r^{b-(n-2)}+r^{b-(n-2)-1} \text { and } r^{b}=r^{b-(n-3)}+r^{b-(n-2)-3}$$

which can be rewritten as

$$\begin{equation*}
r^{n-1}=r+1 \quad \text { and } \quad r^{n+1}=r^{4}+1 \tag{1}
\end{equation*}$$

Simple algebra now gives

$$r^{4}+1=r^{n+1}=r^{n-1} \cdot r^{2}=r^{3}+r^{2} \Longrightarrow(r-1)\left(r^{3}-r-1\right)=0$$

Since $r \neq 1$, using Equation (1) we conclude $r^{3}=r+1=r^{n-1}$, 
thus $n=4$, which gives a contradiction.




# <lo-sample/> IMO_SHL.2022.A6

Let $\mathbb R$ be the set of real numbers. We denote by 
$\mathcal F$ the set of all functions $f\colon\mathbb R\to\mathbb R$ such that

$$f(x + f(y)) = f(x) + f(y)$$

for every $x,y\in\mathbb R$ Find all rational numbers $q$ such that 
for every function $f\in\mathcal F$, there exists some $z\in\mathbb R$ satisfying $f(z)=qz$.

<small>

* domain:Alg
* source:Indonesia
* questionType:FindAll
* concepts:real-numbers,function,rational-numbers

</small>

## Solution

*Answer:* The desired set of rational numbers is 
$\left\{\frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0\right\}$.

Let $Z$ be the set of all rational numbers $q$ such that for every function 
$f \in \mathcal{F}$, there exists some $z \in \mathbb{R}$ satisfying $f(z)=q z$. Let further

$$S=\left\{\frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0\right\}$$

We prove that $Z=S$ by showing the two inclusions: $S \subseteq Z$ and $Z \subseteq S$.

We first prove that $S \subseteq Z$. Let $f \in \mathcal{F}$ and let $P(x, y)$ be the relation 
$f(x+f(y))=f(x)+$ $f(y)$. First note that $P(0,0)$ gives $f(f(0))=2 f(0)$. 
Then, $P(0, f(0))$ gives $f(2 f(0))=3 f(0)$. We claim that

$$f(k f(0))=(k+1) f(0)$$

for every integer $k \geqslant 1$. The claim can be proved by induction. 
The cases $k=1$ and $k=2$ have already been established. 
Assume that $f(k f(0))=(k+1) f(0)$ and consider $P(0, k f(0))$ which gives

$$f((k+1) f(0))=f(0)+f(k f(0))=(k+2) f(0)$$

This proves the claim. We conclude that $\frac{k+1}{k} \in Z$ for every integer 
$k \geqslant 1$. Note that $P(-f(0), 0)$ gives $f(-f(0))=0$. We now claim that

$$f(-k f(0))=(-k+1) f(0)$$

for every integer $k \geqslant 1$. The proof by induction is similar to the one above. 
We conclude that $\frac{-k+1}{-k} \in Z$ for every integer $k \geqslant 1$. 
This shows that $S \subseteq Z$.

We now prove that $Z \subseteq S$. Let $p$ be a rational number outside the set $S$. 
We want to prove that $p$ does not belong to $Z$. To that end, we construct a function 
$f \in \mathcal{F}$ such that $f(z) \neq p z$ for every $z \in \mathbb{R}$. 
The strategy is to first construct a function

$$g:[0,1) \rightarrow \mathbb{Z}$$

and then define $f$ as $f(x)=g(\{x\})+\lfloor x\rfloor$. This function $f$ belongs to $\mathcal{F}$. Indeed,

$$\begin{aligned}
f(x+f(y)) & =g(\{x+f(y)\})+\lfloor x+f(y)\rfloor \\
& =g(\{x+g(\{y\})+\lfloor y\rfloor\})+\lfloor x+g(\{y\})+\lfloor y\rfloor\rfloor \\
& =g(\{x\})+\lfloor x\rfloor+g(\{y\})+\lfloor y\rfloor \\
& =f(x)+f(y)
\end{aligned}$$

where we used that $g$ only takes integer values.

*Lemma 1.* For every $\alpha \in[0,1)$, there exists $m \in \mathbb{Z}$ such that

$$m+n \neq p(\alpha+n)$$

for every $n \in \mathbb{Z}$.

*Proof.* Note that if $p=1$ the claim is trivial. If $p \neq 1$, then the claim is 
equivalent to the existence of an integer $m$ such that

$$\frac{m-p \alpha}{p-1}$$

is never an integer. Assume the contrary. That would mean that both

$$\frac{m-p \alpha}{p-1} \text { and } \frac{(m+1)-p \alpha}{p-1}$$

are integers, and so is their difference. The latter is equal to

$$\frac{1}{p-1}$$

Since we assumed $p \notin S, 1 /(p-1)$ is never an integer. This is a contradiction.

Define $g:[0,1) \rightarrow \mathbb{Z}$ by $g(\alpha)=m$ for any integer $m$ 
that satisfies the conclusion of Lemma 1. Note that $f(z) \neq p z$ if and and only if

$$g(\{z\})+\lfloor z\rfloor \neq p(\{z\}+\lfloor z\rfloor)$$

The latter is guaranteed by the construction of the function $g$. We conclude that 
$p \notin Z$ as desired. This shows that $Z \subset S$.





# <lo-sample/> IMO_SHL.2022.A7

For a positive integer $n$ we denote by $s(n)$ the sum of the digits of $n$. 
Let $P(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$ be a polynomial, where $n \geqslant 2$ 
and $a_i$ is a positive integer for all $0 \leqslant i \leqslant n-1$. 
Could it be the case that, for all positive integers $k$, $s(k)$ 
and $s(P(k))$ have the same parity?


<small>

* domain:Alg
* source:Belarus
* questionType:ProveDisprove
* concepts:integer-numbers

</small>

## Solution

*Answer:* No. For any such polynomial there exists a positive integer $k$ such 
that $s(k)$ and $s(P(k))$ have different parities.

With the notation above, we begin by choosing a positive integer $t$ such that

$$10^{t}>\max \left\{\frac{100^{n-1} a_{n-1}}{\left(10^{\frac{1}{n-1}}-9^{\frac{1}{n-1}}\right)^{n-1}}, 
\frac{a_{n-1}}{9} 10^{n-1}, \frac{a_{n-1}}{9}\left(10 a_{n-1}\right)^{n-1}, \ldots, 
\frac{a_{n-1}}{9}\left(10 a_{0}\right)^{n-1}\right\}$$

As a direct consequence of $10^{t}$ being bigger than the first quantity listed in the above set, we get that the interval

$$I=\left[\left(\frac{9}{a_{n-1}} 10^{t}\right)^{\frac{1}{n-1}},\left(\frac{1}{a_{n-1}} 
10^{t+1}\right)^{\frac{1}{n-1}}\right)$$

contains at least $100$ consecutive positive integers.

Let $X$ be a positive integer in $I$ such that $X$ is congruent to 
$1 \bmod 100$. Since $X \in I$ we have

$$9 \cdot 10^{t} \leqslant a_{n-1} X^{n-1}<10^{t+1}$$

thus the first digit (from the left) of $a_{n-1} X^{n-1}$ must be $9$.

Next, we observe that 
$a_{n-1}\left(10 a_{i}\right)^{n-1}<9 \cdot 10^{t} \leqslant a_{n-1} X^{n-1}$, 
thus $10 a_{i}<X$ for all $i$, which immediately implies that $a_{0}<a_{1} X<\cdots<a_{n} X^{n}$, 
and the number of digits of this strictly increasing sequence forms a 
strictly increasing sequence too. In other words, if $i<j$, the number 
of digits of $a_{i} X^{i}$ is less than the number of digits of $a_{j} X^{j}$.

Let $\alpha$ be the number of digits of $a_{n-1} X^{n-1}$, thus 
$10^{\alpha-1} \leqslant a_{n-1} X^{n-1}<10^{\alpha}$. We are now going to look at 
$P\left(10^{\alpha} X\right)$ and $P\left(10^{\alpha-1} X\right)$ 
and prove that the sum of their digits has different parities. 
This will finish the proof since 
$s\left(10^{\alpha} X\right)=s\left(10^{\alpha-1} X\right)=s(X)$.

We have $P\left(10^{\alpha} X\right)=10^{\alpha n} X^{n}+a_{n-1} 10^{\alpha(n-1)} X^{n-1}+\cdots+a_{0}$, 
and since $10^{\alpha(i+1)}>10^{\alpha i} a_{n-1} X^{n-1}>$ $10^{\alpha i} a_{i} X^{i}$, 
the terms $a_{i} 10^{\alpha i} X^{i}$ do not interact when added; 
in particular, there is no carryover caused by addition. 
Thus we have $s\left(P\left(10^{\alpha} X\right)\right)=s\left(X^{n}\right)+s\left(a_{n-1} X^{n-1}\right)+\cdots+s\left(a_{0}\right)$.

We now look at $P\left(10^{\alpha-1} X\right)=10^{(\alpha-1) n} X^{n}+a_{n-1} 10^{(\alpha-1)(n-1)} X^{n-1}+\cdots+a_{0}$. 
Firstly, if $i<n-1$, then $a_{n-1} X^{n-1}$ has more digits than 
$a_{i} X^{i}$ and $a_{n-1} X^{n-1} \geqslant 10 a_{i} X^{i}$. It now follows that 
$10^{(\alpha-1)(i+1)+1}>10^{(\alpha-1) i} a_{n-1} X^{n-1} \geqslant 10^{(\alpha-1) i+1} a_{i} X^{i}$, 
thus all terms $10^{(\alpha-1) i} a_{i} X^{i}$ for $0 \leqslant i \leqslant n-1$ 
come in 'blocks', exactly as in the previous case.

Finally, $10^{(\alpha-1) n+1}>10^{(\alpha-1)(n-1)} a_{n-1} X^{n-1} \geqslant 10^{(\alpha-1) n}$, 
thus $10^{(\alpha-1)(n-1)} a_{n-1} X^{n-1}$ has exactly $(\alpha-1) n+1$ digits, 
and its first digit is 9 , as established above. On the other hand, 
$10^{(\alpha-1) n} X^{n}$ has exactly $(\alpha-1) n$ zeros, 
followed by 01 (as $X$ is $1 \bmod 100$). Therefore, when we add the terms, 
the 9 and 1 turn into 0 , the 0 turns into 1 , and nothing else is affected.

Putting everything together, we obtain

$$
s\left(P\left(10^{\alpha-1} X\right)\right)=s\left(X^{n}\right)+s\left(a_{n-1} X^{n-1}\right)+\cdots+s\left(a_{0}\right)-9=s\left(P\left(10^{\alpha} X\right)\right)-9
$$

thus $s\left(P\left(10^{\alpha} X\right)\right)$ and $s\left(P\left(10^{\alpha-1} X\right)\right)$ 
have different parities, as claimed.




# <lo-sample/> IMO_SHL.2022.A8

For a positive integer $n$, an $n$-sequence is a sequence $(a_0,\ldots,a_n)$ 
of non-negative integers satisfying the following condition: if $i$ and $j$ 
are non-negative integers with $i+j \leqslant n$, then $a_i+a_j \leqslant n$ and $a_{a_i+a_j}=a_{i+j}$.

Let $f(n)$ be the number of $n$-sequences. Prove that there exist positive real numbers 
$c_1$, $c_2$, and $\lambda$ such that \[c_1\lambda^n<f(n)<c_2\lambda^n\]for all positive integers $n$.

<small>

* domain:Alg
* source:Canada
* questionType:Prove
* concepts:integer-numbers,sequence,real-numbers

</small>


## Solution

*Answer:* Such constants exist with $\lambda=3^{1 / 6}$; we will discuss 
appropriate values of $c_{1}$ and $c_{2}$ in the solution below.

In order to solve this, we will give a complete classification of $n$-sequences.

Let $k=\lfloor n / 2\rfloor$. We will say that an $n$-sequence is large if 
$a_{i}>k$ for some $i$, and small if no such $i$ exists. 
For now we will assume that $\left(a_{i}\right)$ is not the identity sequence 
(in other words, that $a_{i} \neq i$ for some $i$ ).

*Lemma 1.* If $a_{r}=a_{s}$ and $r, s<n$, then $a_{r+1}=a_{s+1}$.

*Proof.* We have $a_{r+1}=a_{a_{r}+a_{1}}=a_{a_{s}+a_{1}}=a_{s+1}$.

*Lemma 2.* If $i \leqslant k$, then $a_{i} \leqslant k$.

*Proof.* We have $i+i \leqslant n$, so $a_{i}+a_{i} \leqslant n$ whence $a_{i} \leqslant k$.

*Lemma 3.* There exist $r, s$ such that $a_{r}=a_{s}$ and $r \neq s$.

*Proof.* If $a_{0} \neq 0$ then $a_{2 a_{0}}=a_{0}$. 
Otherwise, $a_{a_{i}}=a_{i}$ for all $i$, so take $i$ such that 
$a_{i} \neq i$ (which we can do by our earlier assumption).

*Lemma 4.* Let $r$ be the smallest index such that $a_{s}=a_{r}$ for some $s>r$, 
and let $d$ be the minimum positive integer such that $a_{r+d}=a_{r}$. Then

1. The subsequence $\left(a_{r}, a_{r+1}, \ldots, a_{n}\right)$ 
   is periodic with minimal period $d$. That is, for $u<v$, we have $a_{u}=a_{v}$ 
   if and only if $u, v \geqslant r$ and $d \mid v-u$.
2. $a_{i}=i$ for $i<r$ and $a_{i} \geqslant r$ for $i \geqslant r$.

In this case we say $\left(a_{i}\right)$ has period $d$ and offset $r$.

*Proof.* We prove each in turn:

1. The "if" implication is clear from Lemma 1. For the reverse direction, 
   suppose $a_{u}=a_{v}$. Then there are integers $r \leqslant u_{0}, v_{0}<r+d$ 
   such that $d \mid u-u_{0}, v-v_{0}$, so $a_{u_{0}}=a_{u}=a_{v}=$ $a_{v_{0}}$. 
   If $u_{0}<v_{0}$ then $a_{r+d+u_{0}-v_{0}}=a_{r+d}=a_{r}$, 
   contradicting the minimality of $d$. There is a similar contradiction when 
   $u_{0}>v_{0}$. Thus $u_{0}=v_{0}$, so $d \mid u-v$.
2. If $r=0$ there is nothing to prove. Otherwise $a_{0}=a_{2 a_{0}}$ so $2 a_{0}=0$. 
   Then we have $a_{a_{i}}=a_{i}$ for all $i$, so $a_{i}=i$ for $i<r$.

*Lemma 5.* Either

1. $d \mid a_{i}-i$ for all $i$, or
2. $r=0$ and $d \mid a_{i}-i-d / 2$ for all $i$.

*Proof.* Note that Lemma 4 tells us that if $a_{u}=a_{v}$ then $d \mid u-v$. 
Since $a_{a_{i}+a_{0}}=a_{i}$ for all $i$, we have $d \mid a_{i}-i+a_{0}$. 
For $i=0$, this means that $d \mid 2 a_{0}$. If $d \mid a_{0}$ then that 
means that $d \mid a_{i}-i$ for all $i$. Otherwise, if $d \nmid a_{0}$, 
then $d \mid a_{0}-d / 2$ and thus $d \mid a_{i}-i-d / 2$ for all $i$. 
In addition, part 2 of Lemma 4 says that we must have $r=0$ in this case.

*Lemma 6.* If $d$ is even and $d \mid a_{0}-d / 2$, then $\left(a_{i}\right)$ is small. 
(Note that we must have $r=0$ in this case.)

*Proof.* Note that if $d \leqslant k+1$, then by Lemma 
$2,\left(a_{0}, \ldots, a_{d-1}\right)$ is a period for the sequence consisting 
of elements at most $k$, so $\left(a_{i}\right)$ must be small. 
Now suppose $d>k+1$. We show that $a_{i} \leqslant k$ for all $i$ by induction. 
Note that Lemma 2 already establishes this for $i \leqslant k$. 
We must have $d \mid a_{d / 2}$ and $a_{d / 2} \leqslant k<d$ so $a_{d / 2}=0$. 
Thus, for $i>k$, if 
$a_{j} \leqslant k$ for $j<i$, then $a_{i-d / 2} \leqslant k$, so $a_{i}=a_{(i-d / 2)+d / 2}=a_{a_{i-d / 2}} \leqslant k$.

*Lemma 7.* If $\left(a_{i}\right)$ is small, then $r+d \leqslant k+1$.

*Proof.* Since $\left(a_{i}\right)$ is small, there exists $u, v \leqslant k+1$ 
such that $u<v$ and $a_{u}=a_{v}$. Thus $u \leqslant r$ and $d \mid v-u$, so $r+d \leqslant v \leqslant k+1$.

*Lemma 8.* If $\left(a_{i}\right)$ is large, then $r+d>k+1$ and $a_{i}=i$ 
for all $0 \leqslant i<r+d$.

*Proof.* Since $\left(a_{i}\right)$ is large and has period $d$ and offset $r$, 
the period $\left(a_{r}, \ldots, a_{r+d-1}\right)$ must have an element that 
is larger than $k$, so by Lemma 2 we must have $r+d-1>k$.

We already have $a_{i}=i$ for $i<r$. Now we show that $a_{i}=i$ for 
$r \leqslant i \leqslant k$. By Lemma 6 we have $d \mid a_{i}-i$ but 
$r \leqslant i \leqslant k$. Since $k-r+1>d$, this means that $a_{i}=i$ for $i \leqslant k$.

Finally, one can show inductively that $a_{i}=i$ for $k<i<r+d$. 
Indeed, if $a_{j}=j$ for all $j<i$, then $a_{i} \geqslant i$ 
(otherwise $a_{i}=a_{j}$ for some $j<i$, but then $r \leqslant j$ and $i<r+d$ 
means that $d \nmid j-i$.) However, $a_{i}+(n-i)=a_{i}+a_{n-i} \leqslant n$, so $a_{i}=i$.

Thus large sequences are determined by $r$ and $d$. It is not hard to 
check that all sequences of the form $a_{i}=i$ for $i<r+d$ and with period 
$d$ and offset $r$ are $n$-sequences. There are $(n-k-1)(n+k+2) / 2$ 
possible choices of $(r, d)$ where $0 \leqslant r<n, d \geqslant 1$, and $k+1<r+d \leqslant n$.

For small sequences, for a given period $d$ and offset $r$, we need to choose 
the period $\left(a_{r}, \ldots, a_{r+d-1}\right)$ satisfying 
$r \leqslant a j \leqslant k$ and $d \mid a_{j}-j$ for $r \leqslant j<r+d$. 
There are $g(k+1-r, d)$ such choices, where we define $g(x, d)$ to be 
$(p+1)^{q} p^{d-q}$ with $p=\lfloor x / d\rfloor$ and $q=x-d p$.

Furthermore, if $d$ is even then there are $g(k+1, d)$ choices for the period 
$\left(a_{0}, \ldots, a_{d-1}\right)$ satisfying $d \mid a_{j}-j-d / 2$ for $j<d$. 
Again it is not hard to check that, once these choices are made, then the resulting sequence is an $n$-sequence.

Thus the total number of $n$-sequences is

$$\begin{equation*}
f(n)=1+\frac{(n-k-1)(n+k+2)}{2}+\sum_{d^{\prime}=1}^{\lfloor(k+1) / 2\rfloor} 
g\left(k+1,2 d^{\prime}\right)+\sum_{r=0}^{k} \sum_{d=1}^{k+1-r} g(k+1-r, d) \tag{1}
\end{equation*}$$

Now, to show that $f(n)>c_{1} \lambda^{n}$ for some $c_{1}$, we note that

$$f(n)>g\left(k+1,\left\lfloor\frac{k+1}{3}\right\rfloor\right) \geqslant 3^{\lfloor(k+1) / 3\rfloor}>3^{n / 6}-1$$

To show that $f(n)<c_{2} \lambda^{n}$ for some $c_{2}$, it actually suffices 
to show that there is a positive real number $c_{3}$ such that for all positive integers $x$,

$$\sum_{d=1}^{x} g(x, d) \leqslant c_{3} 3^{x / 3}$$

In fact, the following lemma suffices, as it bounds the left hand side of the above 
inequality by a pair of geometric series with initial term $3^{x / 3}$ :

*Lemma.* For positive $d, x$, we have:

$$g(x, d) \leqslant \begin{cases}3^{x / 3}\left(\frac{64}{81}\right)^{x / 3-d}, & 
\text { if } d \leqslant x / 3 \\ 3^{x / 3}\left(\frac{8}{9}\right)^{d-x / 3}, & 
\text { if } d \geqslant x / 3\end{cases}$$

Proof. There are a few key observations needed, all of which are immediate from the definition:

- $(x, d)$ is the maximum product of a sequence of $d$ integers that sums to $x$.
- For any positive integer $k$, we have $g(k x, k d)=g(x, d)^{k}$.
- If $2 d \leqslant x \leqslant 3 d$, then $g(x, d)=2^{3 d-x} 3^{x-2 d}$. Likewise, if $3 d \leqslant x \leqslant 4 d$ then $g(x, d)=$ $3^{4 d-x} 4^{x-3 d}$.

With these observations, if $d \leqslant x / 3$, then

$$3^{4(x-3 d)} g(3 x, 3 d) \leqslant g(3 x+12(x-3 d), 3 d+4(x-3 d))=g(15 x-36 d, 4 x-9 d)$$

To calculate $g(15 x-36 d, 4 x-9 d)$, note that

$$\begin{aligned}
& 3(4 x-9 d)=12 x-27 d \leqslant 15 x-36 d \\
& 4(4 x-9 d)=16 x-36 d \geqslant 15 x-36 d
\end{aligned}$$

so

$$g(15 x-36 d, 4 x-9 d)=3^{4(4 x-9 d)-(15 x-36 d)} 4^{(15 x-36 d)-3(4 x-9 d)}=3^{x} 4^{3(x-3 d)}$$

Thus

$$g(x, d)^{3}=g(3 x, 3 d)=\frac{3^{4(x-3 d)} g(3 x, 3 d)}{3^{4(x-3 d)}} \leqslant 
\frac{3^{x} 4^{3(x-3 d)}}{3^{4(x-3 d)}}=3^{x}\left(\frac{64}{81}\right)^{x-3 d}$$

which completes the proof of the first claim. Likewise, if $d \geqslant x / 3$,

$$3^{2(3 d-x)} g(3 x, 3 d) 3 \leqslant g(3 x+6(3 d-x), 3 d+2(3 d-x))=g(18 d-3 x, 9 d-2 x)$$

Again we have

$$2(9 d-2 x) \leqslant 18-3 x \leqslant 18-3 x+3(3 d-x)=3(9 d-2 x)$$

so

$$g(18 d-3 x, 9 d-2 x)=2^{3(9 d-2 x)-(18 d-3 x)} 3^{(18 d-3 x)-2(9 d-2 x)}=2^{3(3 d-x)} 3^{x}$$

Thus

$$g(x, d)^{3}=g(3 x, 3 d)=\frac{2^{3(3 d-x)} g(3 x, 3 d)}{3^{2(3 d-x)}} \leqslant 
\frac{2^{3(3 d-x) 3^{x}}}{3^{2(3 d-x)}}=3^{x}\left(\frac{8}{9}\right)^{3 d-x}$$

from which the second claim follows.

Common remarks. The best possible value of $c_{1}$ is constrained by $n=1$: 
in this case, $f(1)=2$, which means that $c_{1}>2 \cdot 3^{-1 / 6} \approx 1.66537$.

With a careful analysis one can show that the best possible value of $c_{2}$ is 
$\frac{236567}{4930} 3^{1 / 3} \approx$ 69.20662$.






# <lo-sample/> IMO_SHL.2022.C1

A $\pm 1$-sequence is a sequence of $2022$ numbers $a_1, \ldots, a_{2022},$ 
each equal to either $+1$ or $-1$. Determine the largest $C$ so that, 
for any $\pm 1$-sequence, there exists an integer $k$ and indices 
$1 \le t_1 < \ldots < t_k \le 2022$ so that $t_{i+1} - t_i \le 2$ for all $i$, 
and $$\left| \sum_{i = 1}^{k} a_{t_i} \right| \ge C.$$


<small>

* domain:Comb
* source:Czech Republic
* questionType:FindOptimal


</small>


## Solution

*Answer:* The answer is $C=506$.

First, we prove that this can always be achieved. Without loss of generality, 
suppose at least $\frac{2022}{2}=1011$ terms of the $\pm 1$-sequence are $+1$. 
Define a subsequence as follows: starting at $t=0$, if $a_{t}=+1$ we always include 
$a_{t}$ in the subsequence. Otherwise, we skip $a_{t}$ if we can 
(i.e. if we included $a_{t-1}$ in the subsequence), otherwise we include it out 
of necessity, and go to the next $t$. Clearly, this subsequence will include all $+1$s. 
Also, for each $-1$ included in the sequence, a $-1$ must have been skipped, 
so at most $\left\lfloor\frac{1011}{2}\right\rfloor=505$ can be included. 
Hence the sum is at least $1011-505=506$, as desired.

Next, we prove that, for the $\pm 1$-sequence

$$(\{-1\},\{+1,+1\},\{-1,-1\},\{+1,+1\}, \ldots,\{+1,+1\},\{-1,-1\},\{+1\})$$

each admissible subsequence $a_{t_{i}}$ has $-506 \leqslant \sum_{i} a_{t_{i}} \leqslant 506$. 
We say that the terms inside each curly bracket is a block. In total, 
there are $1012$ blocks - $506$ of them hold $+1$s, and $506 of them hold $-1$s. 
(The two blocks at each end hold $1$ number each, each other block holds $2$.)

Suppose an admissible subsequence includes terms from $k$ blocks holding 
$+1$s. Then, in each $-1$-pair in between the $+1$-pairs, the subsequence 
must also include at least one $-1$. There can be at most two $+1$s 
included from each $+1$-block, and at least one $-1$ must be included 
from each $-1$-block, so the sum is at most $2k-(k-1)=k+1$.

For $k<506$, this is at most $506$. If $k=506$, one of the $+1$-blocks must be 
the one at the end, meaning it can only include one $+1$, so that the maximum 
in this case is only $k$, not $k+1$, so in this case the sum is also at most $506$.

Hence we have shown that for any admissible subsequence, $\sum_{i} a_{t_{i}} \leqslant 506$. Analogously we can show that $-506 \leqslant \sum_{i} a_{t_{i}}$, meaning that $C \leqslant 506$ as desired.

*Comment.* A possible reformulation of the problem is the following:  
2022 buckets of water are arranged in a row, each coloured either red or blue. 
Sally the salmon plays a game in the following way: first, she chooses any 
bucket she likes to start in. Then, any number of times she may jump either 
to the next bucket in the row, or across it to land in the bucket after that. 
(She may not jump across more than one bucket.) At any point, she may finish 
the game. At that time, her score is the absolute value of the difference 
between the number of red and blue buckets she visited during the game. 
Determine the largest $C$ so that no matter how the buckets are coloured,
Sally can achieve a score of at least $C$.


# <lo-sample/> IMO_SHL.2022.C2

The Bank of Oslo issues two types of coin: aluminum (denoted A) and bronze (denoted B). 
Marianne has $n$ aluminum coins and $n$ bronze coins arranged in a row 
in some arbitrary initial order. A chain is any subsequence of consecutive 
coins of the same type. Given a fixed positive integer $k \leq 2n$, 
Gilberty repeatedly performs the following operation: 
he identifies the longest chain containing 
the $k^{th}$ coin from the left and moves all coins in that chain to the left end of the row. 
For example, if $n=4$ and $k=4$, the process starting from the ordering 
$AABBBABA$ would be $AABBBABA \to BBBAAABA \to AAABBBBA \to BBBBAAAA \to \ldots$.

Find all pairs $(n,k)$ with $1 \leq k \leq 2n$ such that for every initial ordering, 
at some moment during the process, the leftmost $n$ coins will all be of the same type.


<small>

* domain:Comb
* source:France
* questionType:FindAll
* concepts:integer-numbers

</small>


## Solution

Define a block to be a maximal subsequence of consecutive coins made out of 
the same metal, and let $M^{b}$ denote a block of $b$ coins of metal $M$. 
The property that there is at most one aluminium coin adjacent to a copper coin 
is clearly equivalent to the configuration having two blocks, one consisting of 
all $A$-s and one consisting of all $C$-s.

First, notice that if $k<n$, the sequence $A^{n-1} C^{n-1} AC$ remains 
fixed under the operation, and will therefore always have $4$ blocks. 
Next, if $k>\frac{3 n+1}{2}$, let $a=k-n-1, b=2 n-k+1$. 
Then $k>2 a+b, k>2 b+a$, so the configuration $A^{a} C^{b} A^{b} C^{a}$ 
will always have four blocks:

$$A^{a} C^{b} A^{b} C^{a} \rightarrow C^{a} A^{a} C^{b} A^{b} \rightarrow A^{b} C^{a} A^{a} C^{b} 
\rightarrow C^{b} A^{b} C^{a} A^{a} \rightarrow A^{a} C^{b} A^{b} C^{a} \rightarrow \ldots$$

Therefore a pair $(n, k)$ can have the desired property only if 
$n \leqslant k \leqslant \frac{3n+1}{2}$. We claim that all such pairs in 
fact do have the desired property. Clearly, the number of blocks in 
a configuration cannot increase, so whenever the operation is applied, 
it either decreases or remains constant. We show that unless there are 
only two blocks, after a finite amount of steps the number of blocks will decrease.

Consider an arbitrary configuration with $c \geqslant 3$ blocks. 
We note that as $k \geqslant n$, the leftmost block cannot be moved, 
because in this case all $n$ coins of one type are in the leftmost block, 
meaning there are only two blocks. If a block which is not the leftmost 
or rightmost block is moved, its neighbor blocks will be merged, 
causing the number of blocks to decrease.

Hence the only case in which the number of blocks does not decrease 
in the next step is if the rightmost block is moved. If $c$ is odd, 
the leftmost and the rightmost blocks are made of the same metal, 
so this would merge two blocks. Hence $c \geqslant 4$ must be even. 
Suppose there is a configuration of $c$ blocks with the $i$-th block having 
size $a_{i}$ so that the operation always moves the rightmost block:

$$A^{a_{1}} \ldots A^{a_{c-1}} C^{a_{c}} \rightarrow C^{a_{c}} A^{a_{1}} \ldots 
A^{a_{c-1}} \rightarrow A^{a_{c-1}} C^{a_{c}} A^{a_{1}} \ldots C^{a_{c-2}} \rightarrow \ldots$$

Because the rightmost block is always moved, $k \geqslant 2 n+1-a_{i}$ 
for all $i$. Because $\sum a_{i}=2 n$, summing this over all $i$ we get 
$ck \geqslant 2cn+c - \sum a_{i} = 2cn + c - 2n$, so 
$k \geqslant 2n+1 - \frac{2n}{c} \geqslant \frac{3 n}{2}+1$. 
But this contradicts $k \leqslant \frac{3n+1}{2}$. Hence at some point the 
operation will not move the rightmost block, meaning that the number 
of blocks will decrease, as desired.




# <lo-sample/> IMO_SHL.2022.C3

In each square of a garden shaped like a $2022 \times 2022$ board, 
there is initially a tree of height $0$. A gardener and a 
lumberjack alternate turns playing the following game, 
with the gardener taking the first turn:

* The gardener chooses a square in the garden. Each tree on that square and all the 
  surrounding squares (of which there are at most eight) then becomes one unit taller.
* The lumberjack then chooses four different squares on the board. Each tree of 
  positive height on those squares then becomes one unit shorter.

We say that a tree is majestic if its height is at least $10^6$. Determine the largest $K$ such 
that the gardener can ensure there are eventually $K$ majestic trees on the board, 
no matter how the lumberjack plays.


<small>

* domain:Comb
* source:Colombia
* questionType:FindOptimal
* concepts:game,square-Alg

</small>

## Solution

*Answer:* $K=5 \cdot \frac{2022^{2}}{9}=2271380$. 
In general, for a $3 N \times 3 N$ board, $K=5 N^{2}$.

We solve the problem for a general $3N \times 3N$ board. First, we prove 
that the lumberjack has a strategy to ensure there are never more than 
$5 N^{2}$ majestic trees. Giving the squares of the board coordinates 
in the natural manner, colour each square where at least one of its 
coordinates are divisible by 3 , shown below for a $9 \times 9$ board:

![](IMO_SHL.2022.C3A.png)

Then, as each $3 \times 3$ square on the board contains exactly $5$ 
coloured squares, each move of the gardener will cause at most 
$4$ trees on non-coloured squares to grow. 
The lumberjack may therefore cut those trees, ensuring no tree on a non-coloured 
square has positive height after his turn. Hence there cannot ever be more majestic 
trees than coloured squares, which is $5 N^{2}$.

Next, we prove the gardener may ensure there are $5 N^{2}$ majestic trees. 
In fact, we prove this statement in a modified game which is more difficult 
for the gardener: on the lumberjack's turn in the modified game, he may decrement 
the height of all trees on the board except those the gardener did not just grow, 
in addition to four of the trees the gardener just grew. Clearly, a sequence 
of moves for the gardener which ensures that there are $K$ majestic trees 
in the modified game also ensures this in the original game.

Let $M=\binom{9}{5}$; we say that a map is one of the $M$ possible ways 
to mark 5 squares on a $3 \times 3$ board. In the modified game, after the 
gardener chooses a $3 \times 3$ subboard on the board, the lumberjack chooses 
a map in this subboard, and the total result of the two moves is that each 
tree marked on the map increases its height by $1$, each tree in the subboard 
which is not in the map remains unchanged, and each tree outside the subboard 
decreases its height by $1$. Also note that if the gardener chooses a 
$3 \times 3$ subboard $M l$ times, the lumberjack will have to choose some 
map at least $l$ times, so there will be at least $5$ trees which each have 
height $\geqslant l$.

The strategy for the gardener will be to divide the board into $N^{2}$ 
disjoint $3 \times 3$ subboards, number them $0, \ldots, N^{2}-1$ in 
some order. Then, for $b=N^{2}-1, \ldots, 0$ in order, he plays 
$10^{6} M(M+1)^{b}$ times on subboard number $b$. Hence, on subboard 
number $b$, the moves on that subboard will first ensure $5$ of its trees 
grows by at least $10^{6}(M+1)^{b}$, and then each move after that 
will decrease their heights by $1$. (As the trees on subboard $b$ 
had height $0$ before the gardener started playing there, no move made 
on subboards $\geqslant b$ decreased their heights.) 
As the gardener makes $10^{6} M(M+1)^{b-1}+\ldots=10^{6}\left((M+1)^{b}-1\right)$ 
moves after he finishes playing on subboard $b$, this means that on 
subboard $b$, there will be 5 trees of height at least 
$10^{6}(M+1)^{b}-10^{6}\left((M+1)^{b}-1\right)=10^{6}$, 
hence each of the subboard has $5$ majestic trees, which was what we wanted.



# <lo-sample/> IMO_SHL.2022.C4

Let $n > 3$ be a positive integer. Suppose that $n$ children are arranged 
in a circle, and $n$ coins are distributed between them (some children 
may have no coins). At every step, a child with at 
least $2$ coins may give $1$ coin to each of their immediate neighbors 
on the right and left. Determine all initial distributions of the coins 
from which it is possible that, after a finite number of steps, 
each child has exactly one coin.


<small>

* domain:Comb
* source:Israel
* questionType:FindAll
* concepts:integer-numbers

</small>





## Solution

*Answer:* All distributions where $\sum_{i=1}^{n} i c_{i}=\frac{n(n+1)}{2}(\bmod n)$, 
where $c_{i}$ denotes the number of coins the $i$-th child starts with.

Number the children $1, \ldots, n$, and denote the number of coins the $i$-th 
child has by $c_{i}$. A step of this process consists of reducing some $c_{i}$ by $2$, 
and increasing $c_{i-1}, c_{i+1}$ by $1$. (Indices are considered 
$(\bmod n)$.) Because $(i-1)-2 i+(i+1)=0$, the quantity 
$\sum_{i=1}^{n} i c_{i}(\bmod n)$ will be invariant under this process. 
Hence a necessary condition for the children to end up with an uniform 
distribution of coins is that

$$\sum_{i=1}^{n} i c_{i}=\frac{n(n+1)}{2} \quad(\bmod n)$$

We will show that this condition is also sufficient. Consider an arbitrary 
initial distribution of coins. First, whenever child $i$ has more than one 
coin and $i \neq n$, have child $i$ pass coins to its neighbors. 
(Child $i$ does nothing.) Then, after some amount of such steps, 
it must eventually become impossible to do any more steps because no child 
except perhaps child $i$ has more than 1 coin. (To see this, consider e.g. 
the quantity $\sum_{i=1}^{n-1} i^{2} c_{i}$, which (as $(i-1)^{2}+(i+1)^{2}>2 i^{2}$) 
increases at each step.)

Hence we can reach a state of the form $\left(z_{1}, \ldots, z_{n-1}, M\right)$, 
where $z_{i}=0$ or 1 . Call such states semi-uniform states of irregularity $M$.

*Lemma.* If there is a string of children having coins 
$a, \overbrace{1, \ldots, 1}^{k \text { ones }}, b, \overbrace{1, \ldots, 1}^{k \text { ones }}, c$, 
with $b \geqslant 2$, after some sequence of steps we may reach the state 
$a+1, \overbrace{1, \ldots, 1}^{k \text { ones }}, b-2, \overbrace{1, \ldots, 1}^{k \text { ones }}, c+1$. 
We call performing this sequence of steps long-passing coins.

*Proof.* This is simply repeated application of the operation. 
We prove the lemma by induction on $k$. For $k=0$, this is just the operation 
of the problem. If $k=1$, have the child with $b$ coins pass coins, 
then both of their neighbors pass coins, then the child with $b$ coins 
pass coins again. For $k \geqslant 2$, first, have the child with $b$ 
coins pass coins, then have both their neigbors send coins, giving the state

$$a, \overbrace{1, \ldots, 1}^{k-2}, 2,0, b, 0,2, \overbrace{1, \ldots, 1}^{k-2 \text { ones }}, c.$$

Now set aside the children with $a, b$ and $c$ coins, and have each child with 2 coins give them to their neighbors until there are no such children remaining. This results in the state

$$a+1,0, \overbrace{1, \ldots, 1}^{k-2}, b, \overbrace{1, \ldots, 1}^{\text {ones }}, 0, c+1.$$

By the induction hypothesis, we can have the child with $b$ coins may pass a 
coin to each of the children with 0 coins, proving the lemma.

Claim. We can reach a semi-uniform state of irregularity $M \leqslant 2$.

Proof. If $M>3$, because there are only $n$ coins in total, there must be at 
least two children with 0 coins. Consider the arc of the circle spanned by 
the two such children closest to the child with $M$ coins. It has the form

$$0, \overbrace{1, \ldots, 1}^{a \text { ones }}, M, \overbrace{1, \ldots, 1}^{b \text { ones }}, 0$$

If $a=b$, applying the previous lemma we can have the child with $M$ coins 
long-pass a coin to each of the children with 0 coins, which yields a 
semi-uniform state with lower $M$. Otherwise, WLOG $a>b$, so we can have the 
child with $M$ coins long-pass a coin to each of the children at distance $b$ 
from it, reaching a state of the form $(\alpha:=a-b-1, \beta:=b)$

$$0, \overbrace{1, \ldots, 1}^{\alpha \text { ones }}, 2, 
\overbrace{1, \ldots, 1}^{\beta \text { ones }}, M-2, \overbrace{1, \ldots, 1}^{c \text { ones }}$$

The children in the rightmost string of ones need make no further moves, 
so consider only the leftmost string. If $\alpha<\beta$, have the child 
with $2$ coins long-pass coins to the child with $0$ coins to its left 
and some child with $1$ coin to its right, reaching a new state of the 
form $\overbrace{}^{\alpha \text { ones }} \beta$ ones

$$0, \overbrace{1, \ldots, 1}^{\alpha \text { ones }}, 2, \overbrace{1, \ldots, 1}^{\beta \text { ones }}, M-2$$ 

with a smaller $\beta$. As $\beta$ cannot decrease indefinitely, eventually 
$\alpha \geqslant \beta$. If $\alpha=\beta$, have the child with $2$ coins 
long-pass to the child with $M$ coins and the child with 0 coins, 
reaching a semi-uniform state of irregularity $M-1$ as desired. Otherwise, 
$\alpha<\beta$, so have the child with 2 coins long-pass to the child with 
$M$ coins and a child with 1 coin, reaching a state of the form

$$0, \overbrace{1, \ldots, 1}^{x \text { ones }}, 2, \overbrace{1, \ldots, 1}^{y \text { ones }}, 
0, \overbrace{1, \ldots, 1}^{z \text { ones }}, M-1$$

Now, consider only the substring between the two children with $0$ coins, 
which has the form 

$$0, \overbrace{1, \ldots, 1}^{x \text { ones }}, 2, \overbrace{1, \ldots, 1,0}^{y \text { ones }}, 0.$$ 

Repeatedly have the child in this substring with $2$ coins long-pass to the 
closest child with 0 coins and some other child. If the other child has $1$ coin, 
we have a new strictly shorter substring of the form 
$0, \overbrace{1, \ldots, 1}^{x \text { ones }}, 2, \overbrace{1, \ldots, 1}^{y \text { ones }}, 0$. 
Hence eventually it must happen that the other child also has $0$ coins, 
at which point we reach a semi-uniform state of irregularity $M-1$, proving the claim.

We have now shown that we can reach a semi-regular state of irregularity 
$M \leqslant 2$, If $M=1$, each child must have one coin, as desired. 
Otherwise, we must have $M=2$, so there is one child with 0 coins, 
one child with $2$ coins, and the remaining children all have $1$ coin. 
Recall that the state we started with satisfied the invariant

$$\sum_{i=1}^{n} i c_{i}=\frac{n(n+1)}{2} \quad(\bmod n)$$

Because each step preserves this invariant, this must also be true of the 
current state. Number the children so that the child with $M$ coins is child 
number $n$, and suppose the child with 0 coins is child $k$. Then 

$$\frac{n(n+1)}{2}=\sum_{i=1}^{n} i c_{i}=\left(\sum_{i=1}^{n} 1 \cdot c_{i}\right)-k=\frac{n(n+1)}{2}-k(\bmod n),$$ 

so $k=0 \pmod {n}$. But this is impossible, as no child except the child 
with $M$ coins has an index divisible by $n$. Hence we cannot end up in a 
semi-regular state of irregularity $2$, so we are done.

## Solution

Encode the sequence $c_{i}$ as a polynomial $p(x)=\sum_{i} a_{i} x_{i}$. 
The cyclic nature of the problem makes it natural to work modulo $x^{n}-1$. 
Child $i$ performing a step is equivalent to adding $x^{i}(x-1)^{2}$ 
to the polynomial, and we want to reach the polynomial 
$q(x)=1+x+\ldots+$ $x^{n-1}$. Since we only add multiples of $(x-1)^{2}$, 
this is only possible if $p(x)=q(x)$ modulo the ideal generated by $x^{n}-1$ 
and $(x-1)^{2}$, i.e.

$$\left(x^{n}-1,(x-1)^{2}\right)=(x-1)\left(\frac{x^{n}-1}{x-1}, x-1\right)=(x-1) \cdot(n,(x-1))$$

This is equivalent to $p(1)=q(1)$ (which simply translates to the condition 
that there are $n$ coins) and $p^{\prime}(1)=q^{\prime}(1)(\bmod n)$, 
which translates to the invariant described in solution $1$.



# <lo-sample/> IMO_SHL.2022.C5

Let $m,n \geqslant 2$ be integers, let $X$ be a set with $n$ elements, and let 
$X_1,X_2,\ldots,X_m$ be pairwise distinct non-empty, not necessary disjoint subset of $X$. 
A function $f \colon X \to \{1,2,\ldots,n+1\}$ is called nice if there exists an index $k$ such that 

$$\sum_{x \in X_k} f(x)>\sum_{x \in X_i} f(x) \quad \text{for all } i \ne k.$$

Prove that the number of nice functions is at least $n^n$.


<small>

* domain:Comb
* source:Germany
* questionType:Prove
* concepts:integer-numbers,subset,function

</small>


## Solution

For a subset $Y \subseteq X$, we write $f(Y)$ for $\sum_{y \in Y} f(y)$. 
Note that a function $f: X \rightarrow$ $\{1, \ldots, n+1\}$ is nice, 
if and only if $f\left(X_{i}\right)$ is maximized by a unique index $i \in\{1, \ldots, m\}$.

We will first investigate the set $\mathcal{F}$ of functions 
$f: X \rightarrow\{1, \ldots, n\}$; note that $|\mathcal{F}|=n^{n}$. 
For every function $f \in \mathcal{F}$, define a corresponding function 
$f^{+}: X \rightarrow\{1,2, \ldots, n+1\}$ in the following way: 
Pick some set $X_{l}$ that maximizes the value $f\left(X_{l}\right)$.

- For all $x \in X_{l}$, define $f^{+}(x)=f(x)+1$.
- For all $x \in X \backslash X_{l}$, define $f^{+}(x)=f(x)$.

*Claim.* The resulting function $f^{+}$is nice.

*Proof.* Note that $f^{+}\left(X_{i}\right)=f\left(X_{i}\right)+\left|X_{i} \cap X_{l}\right|$ 
holds for all $X_{i}$. We show that $f^{+}\left(X_{i}\right)$ is maximized 
at the unique index $i=l$. Hence consider some arbitrary index $j \neq l$. 
Then $X_{l} \subset X_{j}$ is impossible, as this would imply 
$f\left(X_{j}\right)>f\left(X_{l}\right)$ and thereby contradict the choice 
of set $X_{l}$; this in particular yields 
$\left|X_{l}\right|>\left|X_{j} \cap X_{l}\right|$.

$$f^{+}\left(X_{l}\right)=f\left(X_{l}\right)+\left|X_{l}\right| \geqslant f\left(X_{j}\right)+\left|X_{l}\right|>f\left(X_{j}\right)+\left|X_{j} \cap X_{l}\right|=f^{+}\left(X_{j}\right)$$

The first inequality follows since $X_{l}$ was chosen to maximize the value 
$f\left(X_{l}\right)$. The second (strict) inequality follows from 
$\left|X_{l}\right|>\left|X_{j} \cap X_{l}\right|$ as observed above. 
This completes the proof of the claim. $\square$

Next observe that function $f$ can be uniquely reconstructed from 
$f^{+}$: the claim yields that $f^{+}$ has a unique maximizer $X_{l}$, 
and by decreasing the value of $f^{+}$on $X_{l}$ by $1$, 
we get we can fully determine the values of $f$. 
As each of the $n^{n}$ functions $f \in \mathcal{F}$ yields 
a (unique) corresponding nice function 
$f^{+}: X \rightarrow\{1,2, \ldots, n+1\}$, the proof is complete.







# <lo-sample/> IMO_SHL.2022.C6

Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially 
containing a single pebble. One can perform moves of the following form: choose two piles, 
take an equal number of pebbles from each pile and form a new pile out of these pebbles. 
Find (in terms of $n$) the smallest number of nonempty piles that one can obtain by 
performing a finite sequence of moves of this form.


<small>

* domain:Comb
* source:Croatia
* questionType:FindOptimal
* concepts:integer-numbers,sequence

</small>


## Solution

*Answer:* $1$ if $n$ is a power of two, and $2$ otherwise.

The solution we describe is simple, but not the most effective one.

We can combine two piles of $2^{k-1}$ pebbles to make one pile of 
$2^{k}$ pebbles. In particular, given $2^{k}$ piles of one pebble, 
we may combine them as follows:

$$\begin{array}{lll}
2^{k} \text { piles of } 1 \text { pebble } & \rightarrow 2^{k-1} \text { piles of } 2 \text { pebbles } \\
2^{k-1} \text { piles of } 2 \text { pebbles } & \rightarrow 2^{k-2} \text { piles of } 4 \text { pebbles } \\
2^{k-2} \text { piles of } 4 \text { pebbles } & \rightarrow 2^{k-3} \text { piles of } 8 \text { pebbles } \\
& \vdots & \\
2 \text { piles of } 2^{k-1} \text { pebbles } & \rightarrow 1 \text { pile of } 2^{k} \text { pebbles }
\end{array}$$

This proves the desired result in the case when $n$ is a power of $2$.

If $n$ is not a power of $2$, choose $N$ such that $2^{N}<n<2^{N+1}$. 
Let $m=n-2^{N}$. Then $0<m<2^{N}$. Make a pile of $2^{N}$ pebbles 
and call it the large pile. (Alternatively, one can be more efficient 
and make a pile of $2^{M}$ pebbles where $m \leqslant 2^{M}$.) 
Since $n$ is not a power of two, there is at least one other pile 
with pebbles. All other piles have a single pebble (initial condition).

Choose one single pebble pile and remove the pebble and one pebble 
from the large pile and form a pile of $2$ pebbles. If $m<2^{N}-1$, 
remove another pebble from the large pile and one pebble from the 
$2$-pile and form a new pile of $2$ pebbles. Repeat until the 
large pile contains exactly $m$ pebbles.

At this point we have one pile of $m$ pebbles, one pile of $2$ 
pebbles, and the rest are single pebble piles. There must be 
$n-m-2=2^{N}-2$ single piles. Combine two and two into piles 
of two pebbles. Then there are $2^{N-1}$ piles of two pebbles, 
which we can make into one pile of $2^{N}$ pebbles. 
We are left with exactly two piles of pebbles.

Lastly we will prove that it is not possible to form a single 
pile with all pebbles when $n$ is not a power of two. 
A move consists of choosing two piles of say $a$ and $b$ 
pebbles, then removing $c \leqslant \min (a, b)$ pebbles 
from both piles, and forming a new pile with $2 c$ pebbles.
If we include piles of zero pebbles, then this move changes 
the number of pebbles in three piles as follows (and leaves 
all other piles unchanged):

$$\begin{array}{lll}
a & \rightarrow a-c \\
b & \rightarrow b-c \\
0 & \rightarrow 2 c
\end{array}$$

Assume that after the move the number of pebbles in each pile 
is divisible by an odd integer $m$. In particular, $m|2 c, m| a-c$ 
and $m \mid b-c$. Since $m$ is odd, it follows that $m \mid c$, 
and then that $m \mid a$ and $m \mid b$. Hence also before the move 
the number of pebbles in each pile is divisible by the integer $m$.

If $n$ is not a power of 2 , then $n$ is divisible by an odd integer 
$m>1$. In order to make a single pile of $n$ pebbles, we would have 
to start with a distribution in which the number of pebbles in each 
pile is divisible by the integer $m$. This is impossible when we 
start with all piles containing a single pebble.

Remarks on starting configurations From any starting configuration 
that is not a single pile, if there are at least two piles with at 
least two pebbles, we can remove one pebble from two such piles, 
and form a new pile with $2$ pebbles. We can repeat this until we 
have one pile of $2$ pebbles and the rest are single pebble piles, 
and then proceed as in the solution. Hence, if $n$ is a power of two, 
we can make a single pile from any starting configuration.

If $n$ is of the form $n=2^{k} m$ where $m>1$ is odd, then we can 
make a single pile from any starting configuration in which the 
number of pebbles in each pile is divisible by the integer $m$, 
otherwise two piles is the best we can do. Half of this is 
proven already. For the other half, assume we start with a 
configuration in which the number of pebbles in each pile is 
divisible by the integer $m$. Replace each pile of $t m$ pebbles 
with a pile of $t$ boulders. We now have a total of $2^{k}$ 
boulders, hence we can make them into one pile of $2^{k}$ boulders. 
Replacing the boulders with pebbles again, we are done.


## Solution

We show an alternative strategy if $n$ is not a power of $2$. 
Write $n$ in binary form: $n=2^{i_{1}}+2^{i_{2}}+\cdots+2^{i_{k}}$, 
where $i_{1}>i_{2}>\cdots>i_{k}$. Now we make piles of sizes 
$2^{i_{1}}, 2^{i_{2}}, \ldots, 2^{i_{k}}$. We call the pile with 
$2^{i_{1}}$ the large pile, all the others are the small piles.

The strategy is the following: take the two smallest small pile. 
If they have the same size of $2^{a}$, we make a pile of size 
$2^{a+1}$. If they have different sizes, we double the smaller 
pile using the large pile (we allow the large pile to have a 
negative number of pebbles: later we prove that it is not possible). 
We call all the new piles small. When we have only one small pile, 
we terminate the process: we have at most $2$ piles.

After each move we have one less number of piles, and all the 
piles have cardinality power of 2. The number of pebbles is 
decreasing, and at the end of the process, it has a size of 
$n-2^{i_{2}+1} \geqslant n-2^{i_{1}}>0$, thus we can manage 
to have two piles.



## Solution 

Throughout the solution, we will consider the moves in reverse order.
Namely, imagine we have some piles of pebbles, and we are allowed 
to perform moves as follows: take a pile with an even number 
of pebbles, split it into two equal halves and add the pebbles 
from each half to a different pile, possibly forming new piles 
(we may assume for convenience that there are infinitely many 
empty piles at any given moment). Given a configuration of piles 
$\mathcal{C}$, we will use $|\mathcal{C}|$ to denote the number 
of non-empty piles in $\mathcal{C}$. Given two configurations 
$\mathcal{C}_{1}, \mathcal{C}_{2}$, we will say that 
$\mathcal{C}_{2}$ is reachable from $\mathcal{C}_{1}$ if 
$\mathcal{C}_{2}$ can be obtained by performing a finite sequence 
of moves starting from $\mathcal{C}_{1}$. 
Call a configuration of piles $\mathcal{C}$

- simple if each (non-empty) pile in $\mathcal{C}$ consists of 
  a single pebble;
- good if at least one (non-empty) pile in $\mathcal{C}$ has an 
  even number of pebbles and the numbers of pebbles on the piles 
  in $\mathcal{C}$ have no non-trivial odd common divisor 
  ($\mathcal{C}$ has the odd divisor property);
- solvable if there exists a simple configuration which is reachable 
  from $\mathcal{C}$.

The problem asks to find the smallest number of non-empty piles in a 
solvable configuration consisting of $n$ pebbles. We begin the process 
of answering this question by making the following observation:

*Lemma 1.* Let $\mathcal{C}$ be a configuration of piles. 
Let $\mathcal{C}^{\prime}$ be a configuration obtained by applying a 
single move to $\mathcal{C}$. Then

(i) if $\mathcal{C}^{\prime}$ has the odd divisor property, then so does $\mathcal{C}$;  
(ii) the converse to (i) holds if $\left|\mathcal{C}^{\prime}\right| \geqslant|\mathcal{C}|$.  

*Proof.* Suppose that the move consists of splitting a pile of size $2a$ 
and adding $a$ pebbles to each of two piles of sizes $b$ and $c$. Here, 
$a$ is a positive integer and $b, c$ are non-negative integers. 
Thus, $\mathcal{C}^{\prime}$ can be obtained from $\mathcal{C}$ by replacing 
the piles of sizes $2a, b, c$ by two piles of sizes $a+b$ and $a+c$. 
Note that the extra assumption 
$\left|\mathcal{C}^{\prime}\right| \geqslant|\mathcal{C}|$ of part (ii) 
holds if and only if at least one of $b, c$ is zero.

(i) Suppose $\mathcal{C}$ doesn't have the odd divisor property, 
i.e. there exists an odd integer $d>1$ such that the size of each pile 
in $\mathcal{C}$ is divisible by $d$. In particular, $2 a, b, c$ are 
multiples of $d$, so since $d$ is odd, it follows that $a, b, c$ are all 
divisible by $d$. Thus, $a+b$ and $a+c$ are also divisible by $d$, 
so $d$ divides the size of each pile in $\mathcal{C}^{\prime}$. 
In conclusion, $\mathcal{C}^{\prime}$ doesn't have the odd divisor property.

(ii) If $\mathcal{C}^{\prime}$ doesn't have the odd divisor property 
and at least one of $b, c$ is zero, then there exists an odd integer $d>1$ 
such that the size of each pile in $\mathcal{C}^{\prime}$ is divisible 
by $d$. In particular, $d$ divides $a+b$ and $a+c$, so since at least 
one of these numbers is equal to $a$, it follows that $d$ divides $a$. 
But then $d$ must divide all three of $a, b$ and $c$, and hence it 
certainly divides $2 a, b$ and $c$. Thus, $\mathcal{C}$ doesn't 
have the odd divisor property, as desired.

*Lemma 2.* If $\mathcal{C}_{2}$ is reachable from $\mathcal{C}_{1}$ 
and $\mathcal{C}_{2}$ has the odd divisor property, then so does 
$\mathcal{C}_{1}$. In particular, any solvable configuration has 
the odd divisor property.

*Proof.* The first statement follows by inductively applying part (i) of Lemma 1. The second statement follows from the first because every simple configuration has the odd divisor property.

The main claim is the following:

*Lemma 3.* Let $\mathcal{C}$ be a good configuration. Then there exists a 
configuration $\mathcal{C}^{\prime}$ with the following properties:

- $\mathcal{C}^{\prime}$ is reachable from $\mathcal{C}$ and 
  $\left|\mathcal{C}^{\prime}\right|>|\mathcal{C}|$;
- $\mathcal{C}^{\prime}$ is either simple or good.

*Proof.* Call a configuration terminal if it is a counterexample to the 
claim. The following claim is at the heart of the proof:

*Claim.* Let $a_{1}, \ldots, a_{k}$ be the numbers of pebbles on the 
non-empty piles of a terminal configuration $\mathcal{C}$. 
Then there exists a unique $i \in[k]$ such that $a_{i}$ is even. 
Moreover, for all $t \geqslant 1$ we have 
$a_{j} \equiv \frac{a_{i}}{2}\left(\bmod 2^{t}\right)$ for all $j \neq i$.

*Proof of Claim.* Since the configuration is good, there must exist 
$i \in[k]$ such that $a_{i}$ is even. Moreover, by assumption, if we split 
the pile with $a_{i}$ pebbles into two equal halves, the resulting 
configuration will not be good. By part (ii) of Lemma 2,the only way this 
can happen is that $\frac{a_{i}}{2}$ and $a_{j}$ for all $j \neq i$ are odd. 
To prove the second assertion, we proceed by induction on $t$, 
ith the case $t=1$ already being established. If $t \geqslant 2$, 
then split the pile with $a_{i}$ pebbles into two equal halves and move 
one half to the pile with $a_{j}$ pebbles. Since $\frac{a_{i}}{2}$ 
and $a_{j}$ are both odd, $a_{j}+\frac{a_{i}}{2}$ is even, 
so by part (ii) of Lemma 2, the resulting configuration 
$\mathcal{C}^{\prime}$ is good. Thus, $\mathcal{C}^{\prime}$ is terminal, 
so by the induction hypothesis, we have 
$\frac{a_{i}}{2} \equiv \frac{1}{2}\left(a_{j}+\frac{a_{i}}{2}\right)\left(\bmod 2^{t-1}\right)$, 
whence $a_{j} \equiv \frac{a_{i}}{2} \pmod {2^{t}}$), as desired.

Suppose for contradiction that there exists a configuration as in the Claim. 
It follows that there exists $i \in[k]$ and an odd integer $x$ such 
that $a_{i}=2 x$ and $a_{j}=x$ for all $j \neq i$. Thus, $x$ is an 
odd common divisor of $a_{1}, \ldots, a_{k}$, so by the odd divisor 
property, we must have $x=1$. But then we can obtain a simple 
configuration by splitting the only pile with two pebbles into 
two piles each consisting of a single pebble, which is a contradiction.

With the aid of Lemmas 2 and 3, it is not hard to characterise 
all solvable configurations: Lemma 4. A configuration of piles 
$\mathcal{C}$ is solvable if and only if it is simple or good.

*Proof.* ($\Longrightarrow$) Suppose $\mathcal{C}$ is not simple. 
Then since we have to be able to perform at least one move, 
there must be at least one non-empty pile in $\mathcal{C}$ with 
an even number of pebbles. Moreover, by Lemma 2, $\mathcal{C}$ 
has the odd divisor property, so it must be good.

$(\Longleftarrow)$ This follows by repeatedly applying Lemma 3 until 
we reach a simple configuration. Note that the process must stop 
eventually since the number of non-empty piles is bounded from above.

Finally, the answer to the problem is implied by the following 
corollary of Lemma 4: Lemma 5. Let $n$ be a positive integer. Then

(i) a configuration consisting of a single pile of $n$ pebbles 
is solvable if and only if $n$ is a power of two;

(ii) if $n \geqslant 2$, then the configuration consisting of 
piles of sizes 2 and $n-2$ is good.

*Proof.* (i) By Lemma 4, this configuration is solvable if and only 
if either $n=1$ or $n$ is even and has no non-trivial odd divisor, 
so the conclusion follows.

(ii) Since 2 is even and has no non-trivial odd divisor, this configuration 
is certainly good, so the conclusion follows by Lemma 4.

Common remarks. Instead of choosing pebbles from two piles, one 
could allow choosing an equal number of pebbles from each of $k$ piles, 
where $k \geqslant 2$ is a fixed (prime) integer. However, this seems 
to yield a much harder problem - if $k=3$, numerical evidence suggests 
the same answer as in the case $k=2$ (with powers of two replaced by 
powers of three), but the case $k=5$ is already unclear.




# <lo-sample/> IMO_SHL.2022.C7

Lucy starts by writing $s$ integer-valued $2022$-tuples on a blackboard. 
After doing that, she can take any two (not necessarily distinct) tuples 
$\mathbf{v}=(v_1,\ldots,v_{2022})$ and $\mathbf{w}=(w_1,\ldots,w_{2022})$ 
that she has already written, and apply one of the following operations 
to obtain a new tuple:

$$\begin{aligned}
\mathbf{v}+\mathbf{w} &= (v_1+w_1,\ldots,v_{2022}+w_{2022}) \\ 
\mathbf{v} \lor \mathbf{w} &= (\max(v_1,w_1),\ldots,\max(v_{2022},w_{2022}))
\end{aligned}$$

and then write this tuple on the blackboard.

It turns out that, in this way, Lucy can write any integer-valued 
$2022$-tuple on the blackboard after finitely many steps. 
What is the smallest possible number $s$ of tuples that she initially wrote?


<small>

* domain:Comb
* source:Czech Republic
* questionType:FindOptimal
* concepts:integer-numbers

</small>

## Solution

*Answer:* The smallest possible number is $s=3$.

We solve the problem for $n$-tuples for any $n \geqslant 3$: 
we will show that the answer is $s=3$, regardless of the value of $n$.

First, let us briefly introduce some notation. For an $n$-tuple 
$\mathbf{v}$, we will write $\mathbf{v}_{i}$ for its $i$-th coordinate 
(where $1 \leqslant i \leqslant n$ ). For a positive integer $n$ and a 
tuple $\mathbf{v}$ we will denote by $n \cdot \mathbf{v}$ the tuple 
obtained by applying addition on $\mathbf{v}$ with itself $n$ times. 
Furthermore, we denote by $\mathbf{e}(i)$ the tuple which has $i$-th 
coordinate equal to one and all the other coordinates equal to zero. 
We say that a tuple is positive if all its coordinates are positive, 
and negative if all its coordinates are negative.

We will show that three tuples suffice, and then that two tuples do not suffice.

Three tuples suffice. Write $\mathbf{c}$ for the constant-valued 
tuple $\mathbf{c}=(-1, \ldots,-1)$.

We note that it is enough for Lucy to be able to make the tuples 
$\mathbf{e}(1), \ldots, \mathbf{e}(n), \mathbf{c}$; from those any 
other tuple $\mathbf{v}$ can be made as follows. First we choose 
some positive integer $k$ such that $k+\mathbf{v}_{i}>0$ 
for all $i$. Then, by adding a positive number of copies of 
$\mathbf{c}, \mathbf{e}(1), \ldots, \mathbf{e}(n)$, she can make

$$k \mathbf{c}+\left(k+\mathbf{v}_{1}\right) \cdot \mathbf{e}(1)+\cdots+\left(k+\mathbf{v}_{n}\right) \cdot \mathbf{e}(n)$$

which we claim is equal to $\mathbf{v}$. Indeed, this can be checked 
by comparing coordinates: the $i$-th coordinate of the right-hand side 
is $-k+\left(k+\mathbf{v}_{i}\right)=\mathbf{v}_{i}$ as needed.

Lucy can take her three starting tuples to be $\mathbf{a}, \mathbf{b}$ 
and $\mathbf{c}$, such that $\mathbf{a}_{i}=-i^{2}, \mathbf{b}_{i}=i$ 
and $\mathbf{c}=-1$ (as above).

For any $1 \leqslant j \leqslant n$, write $\mathbf{d}(j)$ for the tuple 
$2 \cdot \mathbf{a}+4 j \cdot \mathbf{b}+\left(2 j^{2}-1\right) \cdot \mathbf{c}$, 
which Lucy can make by adding together $\mathbf{a}, \mathbf{b}$ and 
$\mathbf{c}$ repeatedly. This has $i$ th term

$$\begin{aligned}
\mathbf{d}(j)_{i} & =2 \mathbf{a}_{i}+4 j \mathbf{b}_{i}+\left(2 j^{2}-1\right) \mathbf{c}_{i} \\
& =-2 i^{2}+4 i j-\left(2 j^{2}-1\right) \\
& =1-2(i-j)^{2}
\end{aligned}$$

This is $1$ if $j=i$, and at most -1 otherwise. Hence Lucy can 
produce the tuple $\mathbf{1}=(1, \ldots, 1)$ as $\mathbf{d}(1) \vee \cdots \vee \mathbf{d}(n)$.

She can then produce the constant tuple $\mathbf{0}=(0, \ldots, 0)$ 
as $\mathbf{1}+\mathbf{c}$, and for any $1 \leqslant j \leqslant n$ 
she can then produce the tuple $\mathbf{e}(j)$ as $\mathbf{d}(j) \vee \mathbf{0}$. 
Since she can now produce $\mathbf{e}(1), \ldots, \mathbf{e}(n)$ 
and already had $\mathbf{c}$, she can (as we argued earlier) produce any integer-valued tuple.

**Two tuples do not suffice.** We start with an observation: 
Let $a$ be a non-negative real number and suppose that two tuples 
$\mathbf{v}$ and $\mathbf{w}$ satisfy 
$\mathbf{v}_{j} \geqslant a \mathbf{v}_{k}$ and $\mathbf{w}_{j} \geqslant a \mathbf{w}_{k}$ 
for some $1 \leqslant j, k \leqslant n$. Then we claim that the 
same inequality holds for $\mathbf{v}+\mathbf{w}$ and 
$\mathbf{v} \vee \mathbf{w}$ : Indeed, the property for the sum is 
verified by an easy computation:

$$(\mathbf{v}+\mathbf{w})_{j}=\mathbf{v}_{j}+\mathbf{w}_{j} \geqslant a \mathbf{v}_{k}+a \mathbf{w}_{k}=a(\mathbf{v}+\mathbf{w})_{k}$$

For the second operation, we denote by $\mathbf{m}$ the tuple 
$\mathbf{v} \vee \mathbf{w}$. Then 
$\mathbf{m}_{j} \geqslant \mathbf{v}_{j} \geqslant a \mathbf{v}_{k}$ and 
$\mathbf{m}_{j} \geqslant \mathbf{w}_{j} \geqslant a \mathbf{w}_{k}$. 
Since $\mathbf{m}_{k}=\mathbf{v}_{k}$ or $\mathbf{m}_{k}=\mathbf{w}_{k}$, 
the observation follows.

As a consequence of this observation we have that if all starting 
tuples satisfy such an inequality, then all generated tuples 
will also satisfy it, and so we would not be able to obtain every 
integer-valued tuple.

Let us now prove that Lucy needs at least three starting tuples. 
For contradiction, let us suppose that Lucy started with only two 
tuples $\mathbf{v}$ and $\mathbf{w}$. We are going to distinguish 
two cases. In the first case, suppose we can find a coordinate $i$ 
such that $\mathbf{v}_{i}, \mathbf{w}_{i} \geqslant 0$. 
Both operations preserve the sign, thus we can not generate any 
tuple that has negative $i$-th coordinate. Similarly for 
$\mathbf{v}_{i}, \mathbf{w}_{i} \leqslant 0$.

Suppose the opposite, i.e., for every $i$ we have either 
$\mathbf{v}_{i}>0>\mathbf{w}_{i}$, or $\mathbf{v}_{i}<0<\mathbf{w}_{i}$. 
Since we assumed that our tuples have at least three coordinates, 
by pigeonhole principle there exist two coordinates $j \neq k$ 
such that $\mathbf{v}_{j}$ has the same sign as $\mathbf{v}_{k}$ 
and $\mathbf{w}_{j}$ has the same sign as $\mathbf{w}_{k}$ 
(because there are only two possible combinations of signs).

Without loss of generality assume that 
$\mathbf{v}_{j}, \mathbf{v}_{k}>0$ and $\mathbf{w}_{j}, \mathbf{w}_{k}<0$. 
Let us denote the positive real number $\mathbf{v}_{j} / \mathbf{v}_{k}$ 
by $a$. If $\mathbf{w}_{j} / \mathbf{w}_{k} \leqslant a$, then both 
inequalities $\mathbf{v}_{j} \geqslant a \mathbf{v}_{k}$ and 
$\mathbf{w}_{j} \geqslant a \mathbf{w}_{k}$ are satisfied. 
On the other hand, if $\mathbf{w}_{j} / \mathbf{w}_{k} \leqslant a$, 
then both $\mathbf{v}_{k} \geqslant(1 / a) \mathbf{v}_{j}$ 
and $\mathbf{w}_{k} \geqslant(1 / a) \mathbf{w}_{j}$ are satisfied. 
In either case, we have found the desired inequality satisfied 
by both starting tuples, a contradiction with the observation above.

## Common remarks.

1. For $n \in\{1,2\}$, two starting $n$-tuples are necessary 
   and sufficient.
2. The operations,$+ \vee$ used in this problem are studied 
   in the area of tropical geometry. However, as far as we know, 
   familiarity with tropical geometry does not help when solving the problem.







# <lo-sample/> IMO_SHL.2022.C8

Let $n$ be a positive integer. A Nordic square is an $n \times n$ board containing 
all the integers from $1$ to $n^2$ so that each cell contains exactly one number. 
Two different cells are considered adjacent if they share a common side. 
Every cell that is adjacent only to cells containing larger numbers is called a valley. 
An uphill path is a sequence of one or more cells such that:

(i) the first cell in the sequence is a valley,  
(ii) each subsequent cell in the sequence is adjacent to the previous cell, and  
(iii) the numbers written in the cells in the sequence are in increasing order.

Find, as a function of $n$, the smallest possible total number of uphill paths in a Nordic square.

<small>

* domain:Comb
* Author:Nikola Petrović
* source:Serbia
* questionType:FindOptimal
* concepts:integer-numbers,sequence,function

</small>


## Solution

Answer: $2 n^{2}-2 n+1$.

## Solution.

We will call any field that is only adjacent to fields with larger numbers a well. 
Other fields will be called non-wells. Let us make a second $n \times n$ board $B$ 
where in each field we will write the number of good sequences which end on 
the corresponding field in the original board $A$. We will thus look for the 
minimal possible value of the sum of all entries in $B$.

We note that any well has just one good path ending in it, consisting of 
just the well, and that any other field has the number of good paths ending 
in it equal to the sum of this quantity for all the adjacent fields with 
smaller values, since a good path can only come into the field from a field 
of lower value. Therefore, if we fill in the fields in $B$ in increasing 
order with respect to their values in $A$, it follows that each field not 
adjacent to any already filled field will receive a 1, while each field 
adjacent to already filled fields will receive the sum of the numbers 
already written on these adjacent fields.

We note that there is at least one well in $A$, that corresponding 
with the field with the entry 1 in $A$. Hence, the sum of values of fields 
in $B$ corresponding to wells in $A$ is at least 1 . We will now try to 
minimize the sum of the non-well entries, i.e. of the entries in $B$ 
corresponding to the non-wells in $A$. We note that we can ascribe 
to each pair of adjacent fields the value of the lower assigned number 
and that the sum of non-well entries will then equal to the sum of the 
ascribed numbers. Since the lower number is still at least 1, the sum 
of non-well entries will at least equal the number of pairs of adjacent 
fields, which is $2 n(n-1)$. Hence, the total minimum sum of entries in 
$B$ is at least $2 n(n-1)+1=2 n^{2}-2 n+1$. The necessary conditions 
for the minimum to be achieved is for there to be only one well and for 
no two entries in $B$ larger than 1 to be adjacent to each other.

We will now prove that the lower limit of $2 n^{2}-2 n+1$ entries can 
be achieved. This amounts to finding a way of marking a certain set of squares, 
those that have a value of 1 in $B$, such that no two unmarked squares 
are adjacent and that the marked squares form a connected tree with respect to adjacency.

For $n=1$ and $n=2$ the markings are respectively the lone field 
and the L-trimino. Now, for $n>2$, let $s=2$ for $n \equiv 0,2 \bmod 3$ 
and $s=1$ for $n \equiv 1 \bmod 3$. We will take indices $k$ and 
$l$ to be arbitrary non-negative integers. For $n \geqslant 3$ we will 
construct a path of marked squares in the first two columns consisting 
of all squares of the form $(1, i)$ where $i$ is not of the form 
$6 k+s$ and $(2, j)$ where $j$ is of the form $6 k+s-1,6 k+s$ or 
$6+s+1$. Obviously, this path is connected. Now, let us consider 
the fields $(2,6 k+s)$ and $(1,6 k+s+3)$. For each considered field 
$(i, j)$ we will mark all squares of the form $(l, j)$ for $l>i$ 
and $(i+2 k, j \pm 1)$. One can easily see that no set of marked 
fields will produce a cycle, that the only fields of the unmarked 
form $(1,6 k+s),(2+2 l+1,6 k+s \pm 1)$ and $(2+2 l, 6 k+s+3 \pm 1)$ 
and that no two are adjacent, since
the consecutive considered fields are in columns of opposite parity. 
Examples of markings are given for $n=3,4,5,6,7$, and the corresponding 
constructions for $A$ and $B$ are given for $n=5$.

![](IMO_SHL.2022.C8A.png)

## Common remarks.

- The construction can be achieved in different ways. For example, it can also be done 
  recursively; we can complete any construction for $n$ to a construction for $n+1$.
- It is a natural idea to change the direction of the path: that way it can start anywhere, 
  but only can end in a well, which exactly means that we cannot extend the path. 
  This is just a reformulation of the problem, but can give some intuitions.





# <lo-sample/> IMO_SHL.2022.C9

Let $\mathbb Z_{\ge 0}$ be the set of non-negative integers, and let 
$f:\mathbb Z_{\ge 0}\times \mathbb Z_{\ge 0} \to \mathbb Z_{\ge 0}$ be a 
bijection such that whenever $f(x_1,y_1) > f(x_2, y_2)$, we have 

$$f(x_1+1, y_1) > f(x_2 + 1, y_2)\;\;\text{and}\;\;f(x_1, y_1+1) > f(x_2, y_2+1).$$

Let $N$ be the number of pairs of integers $(x,y)$ with $0\le x,y<100$, 
such that $f(x,y)$ is odd. Find the smallest and largest possible values of $N$.


<small>

* domain:Comb
* questionType:FindOptimal
* source:U.S.A.
* concepts:integer-numbers,pair

</small>

## Solution 

*Answer:* The optimal bounds are $2500 \leqslant N \leqslant 7500$.

We defer the constructions to the end of the solution. Instead, we begin 
by characterizing all such functions $f$, prove a formula and key property 
for such functions, and then solve the problem, providing constructions.

Characterization Suppose $f$ satisfies the given relation. 
The condition can be written more strongly as

$$\begin{aligned}
f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right) & \Longleftrightarrow f\left(x_{1}+1, y_{1}\right)>f\left(x_{2}+1, y_{2}\right) \\
& \Longleftrightarrow f\left(x_{1}, y_{1}+1\right)>f\left(x_{2}, y_{2}+1\right)
\end{aligned}$$

In particular, this means for any $(k, l) \in \mathbb{Z}^{2}, f(x+k, y+l)-f(x, y)$ 
has the same sign for all $x$ and $y$.

Call a non-zero vector $(k, l) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0}$ 
a needle if $f(x+k, y)-f(x, y+l)>0$ for all $x$ and $y$. It is not hard to see 
that needles and non-needles are both closed under addition, and thus under 
scalar division (whenever the quotient lives in $\mathbb{Z}^{2}$ ).

In addition, call a positive rational number $\frac{k}{l}$ a grade if the vector 
$(k, l)$ is a needle. (Since needles are closed under scalar multiples and 
quotients, this is well-defined.)

*Claim.* Grades are closed upwards.

*Proof.* Consider positive rationals 
$k_{1} / l_{1}<k_{2} / l_{2}$ with $k_{1} / l_{1}$ a grade. Then:

- $\left(k_{1}, l_{1}\right)$ is a needle
- so $\left(k_{1} l_{2}, l_{1} l_{2}\right)$ is a needle,
- so $\left(k_{2} l_{1}, l_{1} l_{2}\right)$ is a needle 
  (as $k_{2} l_{1}-k_{1} l_{2}>0$ and $(1,0)$ is a needle).

Thus $\left(k_{2}, l_{2}\right)$ is a needle, as wanted.


*Claim.* A grade exists.

*Proof.* If no positive integer $n$ is a grade, then $f(1,0)>f(0, n)$ 
for all $n$ which is impossible.

Similarly, there is an $n$ such that $f(0,1)<f(n, 0)$, thus 
$1/n$ is not a grade for some large $n$. That means that small positive 
rational values are not grades, then there is a switch, and after 
that all values are grades. Call the place of that switch 
$\alpha$. Here $\alpha$ is the infimum of the grades.

*Claim (Key property).* If $x_{1}+y_{1} \alpha>x_{2}+y_{2} \alpha$ 
then $f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right)$.

*Proof.* If both $x_{1} \geqslant x_{2}$ and $y_{1} \geqslant y_{2}$ this is clear.

Suppose $x_{1} \geqslant x_{2}$ and $y_{1}<y_{2}$. Then $\frac{x_{1}-x_{2}}{y_{2}-y_{1}}>\alpha$ is a grade. This gives $f\left(x_{1}, y_{1}\right)>f\left(x_{2}, y_{2}\right)$. Suppose $x_{1}<x_{2}$ and $y_{1} \geqslant y_{2}$. Then $\frac{x_{2}-x_{1}}{u_{1}-u_{2}}<\alpha$ is not a grade. This gives $f\left(x_{2}, y_{2}\right)<f\left(x_{1}, y_{1}\right)$.

From those observations we get the following claim.

*Claim.* The function $f$ orders pairs $(x, y)$ based on the value of 
$x+y \alpha$. If $\alpha$ is rational, tiebreaking is done by larger 
$x$-coordinate or $y$-coordinate (depending on whether $\alpha$ is a grade).

We can imagine this the following way: take a line with slope $-\frac{1}{\alpha}$ 
under the first quadrant of the plane. And we start to move this line 
upward (but it stays parallel to the original line). First it hits 
$(0,0)$, so $f(0,0)=0$. And each time the line hits a point $p, f(p)$ 
is the number of points hit before. If $\alpha \in \mathbb{Q}$, 
it is possible that the line hits multiple points. Then those 
points are ordered the same way as their $x$ or $y$ coordinates, 
depending on whether $\alpha$ is a grade.

We understood the behaviour of $f$, now we need to focus on the 
region of 

$$A = \left\{(x, y) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \mid 
x<100, y<100\right\}.$$ 

First, we can assume that $\alpha$ is irrational. If we change it a little 
bit in the right direction, the behaviour and values of the $f$ function does not change in $A$.

*Claim.*

$$f(x, y)+f(x+1, y+1)=f(x+1, y)+f(x, y+1)+1$$

*Proof.*

$$\begin{gathered}
f(x+1, y+1)-f(x, y+1)= \\
\#\left\{(a, b) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \mid x+(y+1) \alpha \leqslant a+b \alpha<(x+1)+(y+1) \alpha\right\}= \\
\#\left\{(a, b) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{>0} \mid x+(y+1) \alpha \leqslant a+b \alpha<(x+1)+(y+1) \alpha\right\}+ \\
\#\left\{(a, 0) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \mid(x+1)+y \alpha \leqslant a<(x+1)+(y+1) \alpha\right\}= \\
\#\left\{(a, b) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \mid x+y \alpha \leqslant a+b \alpha<(x+1)+y \alpha\right\}+1=f(x+1, y)-f(x, y)
\end{gathered}$$

From this claim we immediately get that $2500 \leqslant N \leqslant 7500$; 
now we show that those bounds are indeed sharp.

Remember that if $\alpha$ is irrational then

$$f(a, b)=\#\left\{(x, y) \in \mathbb{Z}_{\geqslant 0} \times \mathbb{Z}_{\geqslant 0} \mid x+y \alpha<a+b \alpha\right\}$$

**Construction for 7500.** Select $\alpha \approx 199.999$.

*Claim.*

1. $f(n, 0)=n$ for $0 \leqslant n \leqslant 100$.
2. $f(0, k) \equiv k \quad \bmod 2$ for $0 \leqslant k \leqslant 100$.

*Proof.*

1. $f(n, 0)=\#\{(x, y) \mid x+y \alpha<n\}=\#\{(x, y) \mid x+199 y<n\}=n$.
2. $$\begin{aligned}
   & f(0, k)=\#\{(x, y) \mid x+y \alpha<k \alpha\}=\sum_{l=0}^{k-1} \#\{(x, l) \mid x+l \alpha<k \alpha\} \\
   & \quad=\sum_{l=0}^{k-1} \#\{x \mid x<(k-l) \alpha\}=\sum_{l=0}^{k-1} 200(k-l)-1=200 A-k
   \end{aligned}$$
   for some integer $A$.

From this claim, using the equality $f(x, y)+f(x+1, y+1)=f(x+1, y)+f(x, y+1)+1$, 
we can prove that mod 2 the region $A$ looks like the following: 
in the rows $(-, 2y)$ the remainders modulo 2 alternate, 
while the rows $(-, 2y+1)$ contain only odd numbers.

![](IMO_SHL.2022.C9A.png)

The numbers mod $2$ in the construction for $7500$.

Construction for 2500 Select $\alpha \approx 200.001$.

## Claim.

1. $f(n, 0)=n$ for $0 \leqslant n \leqslant 100$.
2. $f(0, k) \equiv 0 \quad \bmod 2$ for $0 \leqslant k \leqslant 100$.

Proof.

1. As above.
2. Similarly to the above:

$$\begin{aligned}
f(0, k) & =\#\{(x, y) \mid x+y \alpha<k \alpha\}=\sum_{l=0}^{k-1} \#\{(x, l) \mid x+l \alpha<k \alpha\} \\
& =\sum_{l=0}^{k-1} \#\{x \mid x<(k-l) \alpha\}=\sum_{l=0}^{k-1} 200(k-l)=200 A\end{aligned}$$

for some integer $A$.

Similarly to the above, we can prove that $\bmod 2$ the region $A$ looks like the following: 
in the rows $(-, 2y)$ the remainder modulo $2$ alternate, while the rows 
$(-, 2y+1)$ contain only even numbers.

![](IMO_SHL.2022.C9B.png)

The numbers mod 2 in the construction for 7500.

## Common remarks

- In the proposer's solution, an exact formula is proved 
  in the case where $\alpha$ is irrational. Let $\mu=\frac{1}{\alpha}$ and $\nu=\alpha$. Then

  $$f(a, b)=a b+(\lceil 1 \mu\rceil+\cdots+\lceil\mu\rceil)+(\lceil 1 \nu\rceil+\cdots+\lceil\nu\rceil)$$

  They even suggested that this could be the source of a fun olympiad problem: it is not easy to see that $f$ is a bijection.

- (On the choice of statement, by the proposer). As seen in the solution, such functions 
  have various properties, and it was not clear what statement to choose.

  I decided to go with the present statement since I believe it requires a good 
  understanding of the setup and the functions involved. The key property is 
  used in order to establish the bounds, and the formula is used to develop 
  constructions and easily verify they work.

  While choosing a different statement (e.g. just prove the key property) may make 
  the problem less bulky, I believe that doing so runs the risk of introducing 
  unintended solutions which don't "see the full picture." In fact, the present 
  statement probably runs admits such solutions as well, likely through proving 
  the key property via simply examining valid locations for $n+1$ given the 
  locations of $0, \ldots, n$, and using induction.

  Unfortunately, I'm not sure how else to improve the statement.

  One person I've shown this problem to suggests removing one half of the problem, 
  by only asking for the smallest or only the largest possible value of $N$. 
  Their rationale is that the two parts are mostly the same. 
  I sympathize with them, but am reluctant to break the symmetry.

- (PSC) The real difficulty of this problem is that one should understand 
  the whole picture, and in particular how the function $f$ works, and how 
  that quadrant can behave. In this solution we characterised all such 
  functions $f$, before even talking about parity, while the problem only 
  asks the number of odd numbers.





# <lo-sample/> IMO_SHL.2022.G1

Let $ABCDE$ be a convex pentagon such that $BC=DE$. Assume that there is a point $T$ inside 
$ABCDE$ with $TB=TD,TC=TE$ and $\angle ABT = \angle TEA$. 
Let line $AB$ intersect lines $CD$ and $CT$ at points $P$ and $Q$, respectively. 
Assume that the points $P,B,A,Q$ occur on their line in that order. 
Let line $AE$ intersect $CD$ and $DT$ at points $R$ and $S$, respectively. 
Assume that the points $R,E,A,S$ occur on their line in that order. 
Prove that the points $P,S,Q,R$ lie on a circle.


<small>

* domain:Geom
* source:Slovakia
* questionType:Prove
* concepts:point,line,angle

</small>


## Solution

By the conditions we have $B C=D E, C T=E T$ and $T B=T D$, 
so the triangles $T B C$ and $T D E$ are congruent, in particular 
$\angle B T C=\angle D T E$.

In triangles $T B Q$ and $T E S$ we have $\angle T B Q=\angle S E T$ 
and $\angle Q T B=180^{\circ}-\angle B T C=180^{\circ}-$ $\angle D T E=\angle E T S$, 
so these triangles are similar to each other. It follows that $\angle T S E=\angle B Q T$ and

$$\frac{T D}{T Q}=\frac{T B}{T Q}=\frac{T E}{T S}=\frac{T C}{T S}$$

By rearranging this relation we get $T D \cdot T S=T C \cdot T Q$, so 
$C, D, Q$ and $S$ are concyclic. (Alternatively, we can get 
$\angle C Q D=\angle C S D$ from the similar triangles $T C S$ and $T D Q$.) 
Hence, $\angle D C Q=\angle D S Q$.

Finally, from the angles of triangle $C Q P$ we get

$$\angle R P Q=\angle R C Q-\angle P Q C=\angle D S Q-\angle D S R=\angle R S Q$$

which proves that $P, Q, R$ and $S$ are concyclic.

![](IMO_SHL.2022.G1A.png)

## Solution

As in the previous solution, we note that triangles $TBC$ and $TDE$ 
are congruent. Denote the intersection point of $DT$ and $BA$ by $V$, 
and the intersection point of $CT$ and $EA$ by $W$. 
From triangles $BCQ$ and $DES$ we then have

$$\begin{aligned}
\angle VSW & = \angle DSE = 180^{\circ} - \angle SED - \angle EDS = 180^{\circ}-\angle AET - \angle TED - \angle EDT \\
& =180^{\circ}-\angle TBA-\angle TCB-\angle CBT = 180^{\circ}-\angle QCB-\angle CBQ = \angle BQC = \angle VQW
\end{aligned}$$

meaning that $VSQW$ is cyclic, and in particular $\angle WVQ=\angle WSQ$. Since

$$\angle VTB = 180^{\circ}-\angle BTC-\angle CTD = 180^{\circ}-\angle CTD - \angle DTE=\angle ETW$$

and $\angle T B V=\angle W E T$ by assumption, we have that the triangles 
$VTB$ and $WTE$ are similar, hence

$$\frac{VT}{WT} = \frac{BT}{ET} = \frac{DT}{CT}$$

Thus $CD \| VW$, and angle chasing yields

$$\angle R P Q=\angle W V Q=\angle W S Q=\angle R S Q$$

concluding the proof.


# <lo-sample/> IMO_SHL.2022.G2

In the acute-angled triangle $ABC$, the point $F$ is the foot of the altitude 
from $A$, and $P$ is a point on the segment $AF$. The lines through $P$ parallel 
to $AC$ and $AB$ meet $BC$ at $D$ and $E$, respectively. 
Points $X \ne A$ and $Y \ne A$ lie on the circles $ABD$ and $ACE$, 
respectively, such that $DA = DX$ and $EA = EY$.

Prove that $B, C, X,$ and $Y$ are concyclic.

<small>

* domain:Geom
* source:Netherlands
* questionType:Prove
* concepts:angle,triangle,point,altitude,segment,circle

</small>


## Solution

Let $A^{\prime}$ be the intersection of lines $B X$ and $C Y$. 
By power of a point, it suffices to prove that 
$A^{\prime} B \cdot A^{\prime} X=A^{\prime} C \cdot A^{\prime} Y$, 
or, equivalently, that $A^{\prime}$ lies on the radical axis of the circles $A B D X$ and $ACEY$.

From $D A=D X$ it follows that in circle $A B D X$, point $D$ bisects 
of one of the $\operatorname{arcs} A X$. Therefore, depending on the order 
of points, the line $B C$ is either the internal or external bisector of 
$\angle ABX$. In both cases, line $B X$ is the reflection of 
$BA$ in line $BDC$. Analogously, line $C Y$ is the reflection of 
$CA$ in line $BC$; we can see that $A^{\prime}$ is the reflection of 
$A$ in line $B C$, so $A,F$ and $A^{\prime}$ are collinear.

By $PD \| AC$ and $PE \| AB$ we have 
$\frac{FD}{FC} = \frac{FP}{FA} = \frac{FE}{FB}$, 
hence $FD \cdot FB = FE \cdot FC$. 
So, point $F$ has equal powers with respect to circles $ABDX$ and $ACEY$.

Point $A$, being a common point of the two circles, is another point 
with equal powers, so the radical axis of circles $ABDX$ and $ACEY$ 
is the altitude $A F$ that passes through $A^{\prime}$.

![](IMO_SHL.2022.G2A.png)

## Solution

We present another way to prove that line $APA^{\prime}$ is the 
radical axis of the circles $A B D$ and $A C E$. It suffices to show 
that the second intersection point of $ABD$ and $ACE$ lies on $AP$.

Define $N$ to be the second intersection of circle $PDE$ and $AP$. 
From $\angle DNA = \angle DNP =  \angle DEP = \angle DBA$ it follows that $N$ lies on circle $ABD$; analogously, we can show that $N$ lies on circle $A C E$.



# <lo-sample/> IMO_SHL.2022.G3

Let $ABCD$ be a cyclic quadrilateral. Assume that the points 
$Q, A, B, P$ are collinear in this order, in such a way that the 
line $AC$ is tangent to the circle $ADQ$, and the line $BD$ is 
tangent to the circle $BCP$. Let $M$ and $N$ be the midpoints 
of segments $BC$ and $AD$, respectively. Prove that the following three 
lines are concurrent: line $CD$, the tangent of circle $ANQ$ at point $A$, 
and the tangent to circle $BMP$ at point $B$.


<small>

* domain:Geom
* source:Slovakia
* questionType:Prove
* concepts:tangent,circle,segments,point

</small>


## Solution

We first prove that triangles $A D Q$ and $C D B$ are similar. Since $A B C D$ is 
cyclic, we have $\angle D A Q=\angle D C B$. By the tangency of 
$A C$ to the circle $A Q D$ we also have $\angle C B D=\angle C A D=\angle A Q D$. 
The claimed similarity is proven.

Let $R$ be the midpoint of $C D$. Points $N$ and $R$ correspond in the proven 
similarity, and so $\angle Q N A=\angle B R C$.

![](IMO_SHL.2022.G3A.png)

Let $K$ be the second common point of line $C D$ with circle $A B R$ (i.e., 
if $C D$ intersects circle $A B R$, then $K \neq R$ is the other intersection; 
otherwise, if $C D$ is tangent to $C D$, then $K=R$ ). In both cases, 
we have $\angle B A K=\angle B R C=\angle Q N A$; that indicates that 
$AK$ is tangent to circle $A N Q$. It can be showed analogously 
that $BK$ is tangent to circle $BMP$.

Comment. Note that $M$ and $N$ can be any points on lines $BC$ and 
$AD$ such that $BM:MC = DN:NA$, as we then simply choose $R$ to be 
such that $DR:RC$ is that same ratio, and the rest of the proof remains unchanged.

## Solution

We present a second solution, without using the condition that $ABCD$ 
is cyclic. Again, $M$ and $N$ can be any points on lines $BC$ and 
$AD$ such that $BM:MC=DN:NA$.

Let $AB$ and $CD$ meet at $T$ (if $AB \| CD$ then $T$ is their 
common ideal point). Let $CD$ meet the tangent to the circle $ANQ$ 
at $A$, and the tangent to the circle $BMP$ at $B$ at points 
$K_{1}$ and $K_{2}$, respectively.

![](IMO_SHL.2022.G3B.png)

Let $I$ and $J$ be the ideal points of $AD$ and $BC$, respectively. 
Notice that the pencils $\left(AD, AC, AT, AK_{1}\right)$ and 
$(QA, QD, QI, QN)$ of lines are congruent, because 
$\angle K_{1} AD=\angle AQN$, $\angle CAD=\angle AQD$ and $\angle IAT = \angle IQT$. 
Hence,

$$\left(D, C ; T, K_{1}\right) = \left(A D, A C ; A T, A K_{1}\right) = 
(QA, QD ; QI, QN)=(A,D ; I,N)=\frac{DN}{NA}$$

It can be obtained analogously that

$$\left(D,C ; T,K_{2}\right)=\left(BD,BC ; BT,BK_{2}\right)=(PC,PB ; PJ,PM)=(C,B ; I,N) = \frac{BM}{MC}$$

From $BM:MC = DN:DA$ we get $\left(D,C ; T,K_{1}\right) = \left(D,C ; T,K_{2}\right)$ 
and hence $K_{1}=K_{2}$.





# <lo-sample/> IMO_SHL.2022.G4

Let $ABC$ be an acute-angled triangle with $AC > AB$, let $O$ be its circumcentre, 
and let $D$ be a point on the segment $BC$. The line through $D$ perpendicular 
to $BC$ intersects the lines $AO, AC,$ and $AB$ at $W, X,$ and $Y,$ respectively. 
The circumcircles of triangles $AXY$ and $ABC$ intersect again at $Z \ne A$.

Prove that if $W \ne D$ and $OW = OD,$ then $DZ$ is tangent to the circle $AXY.$


<small>

* domain:Geom
* source:United Kingdom
* questionType:Prove
* concepts:line,triangle,segment,point,circle

</small>


## Solution

Let $AO$ intersect $BC$ at $E$. As $EDW$ is a right-angled triangle 
and $O$ is on $WE$, the condition $OW = OD$ means $O$ is the 
circumcentre of this triangle. So $OD = OE$ which establishes that 
$D,E$ are reflections in the perpendicular bisector of $BC$.

Now observe:

$$180^{\circ} - \angle DXZ = \angle ZXY = \angle ZAY = \angle ZCD$$

which shows $CDXZ$ is cyclic.

![](IMO_SHL.2022.G4A.png)

We next show that $A Z \| B C$. To do this, introduce point $Z^{\prime}$ on circle 
$ABC$ such that $AZ^{\prime} \| BC$. By the previous result, it suffices 
to prove that $CDXZ^{\prime}$ is cyclic. Notice that triangles $BAE$ and 
$CZ^{\prime} D$ are reflections in the perpendicular bisector of $BC$. 
Using this and that $A,O,E$ are collinear:

$$\angle DZ^{\prime}C = \angle BAE = \angle BAO = 90^{\circ} - \frac{1}{2} \angle AOB = 
90^{\circ}-\angle C = \angle DXC$$

so $DXZ^{\prime}C$ is cyclic, giving $Z \equiv Z^{\prime}$ as desired.

Using $AZ \| BC$ and $CDXZ$ cyclic we get:

$$\angle AZD = \angle CDZ = \angle CXZ = \angle AYZ$$

which by the converse of alternate segment theorem shows $DZ$ is tangent to circle $AXY$.


## Solution

Notice that point $Z$ is the Miquel-point of lines $AC, BC, BA$ 
and $DY$; then $B,D,Z,Y$ and $C,D,X,Y$ are concyclic. Moreover, 
$Z$ is the centre of the spiral similarity that maps $BC$ to $YX$.

By $BC \perp YX$, the angle of that similarity is $90^{\circ}$; 
hence the circles $ABCZ$ and $AXYZ$ are perpendicular, therefore the 
radius $OZ$ in circle $ABCZ$ is tangent to circle $AXYZ$.

![](IMO_SHL.2022.G4B.png)

By $OW = OD$, the triangle $OWD$ is isosceles, and

$$\angle ZOA = 2 \angle ZBA = 2 \angle ZBY = 2 \angle ZDY = \angle ODW + \angle DWO$$

so $D$ lies on line $ZO$ that is tangent to circle $AXY$.



# <lo-sample/> IMO_SHL.2022.G5

Let $ABC$ be a triangle and $\ell_1,\ell_2$ be two parallel lines. 
Let $\ell_i$ intersects line $BC,CA,AB$ at $X_i,Y_i,Z_i$, respectively. 
Let $\Delta_i$ be the triangle formed by the line passed through $X_i$ and 
perpendicular to $BC$, the line passed through $Y_i$ and perpendicular to $CA$, 
and the line passed through $Z_i$ and perpendicular to $AB$. 
Prove that the circumcircles of $\Delta_1$ and $\Delta_2$ are tangent.


<small>

* domain:Geom
* source:Vietnam
* questionType:Prove
* concepts:triangle,line

</small>


## Solution

Throughout the solutions, $\sphericalangle(p, q)$ will denote the 
directed angle between lines $p$ and $q$, taken modulo $180^{\circ}$.

Let the vertices of $\Delta_{i}$ be $D_{i}, E_{i}, F_{i}$, 
such that lines $E_{i} F_{i}, F_{i} D_{i}$ and $D_{i} E_{i}$ are the perpendiculars through $X, Y$ and $Z$, respectively, and denote the 
circumcircle of $\Delta_{i}$ by $\omega_{i}$.

In triangles $D_{1} Y_{1} Z_{1}$ and $D_{2} Y_{2} Z_{2}$ we have 
$Y_{1} Z_{1} \| Y_{2} Z_{2}$ because they are parts of $\ell_{1}$ 
and $\ell_{2}$. Moreover, $D_{1} Y_{1} \| D_{2} Y_{2}$ are 
perpendicular to $A C$ and $D_{1} Z_{1} \| D_{2} Z_{2}$ are 
perpendicular to $A B$, so the two triangles are homothetic 
and their homothetic centre is $Y_{1} Y_{2} \cap Z_{1} Z_{2}=A$. 
Hence, line $D_{1} D_{2}$ passes through $A$. Analogously, 
line $E_{1} E_{2}$ passes through $B$ and $F_{1} F_{2}$ passes through $C$.

![](IMO_SHL.2022.G5A.png)

The corresponding sides of $\Delta_{1}$ and $\Delta_{2}$ are parallel, 
because they are perpendicular to the respective sides of triangle $ABC$. 
Hence, $\Delta_{1}$ and $\Delta_{2}$ are either homothetic, or they can be
translated to each other. Using that $B, X_{2}, Z_{2}$ and $E_{2}$ are concyclic,
$C, X_{2}, Y_{2}$ and $F_{2}$ are concyclic, $Z_{2}E_{2} \perp AB$ and 
$Y_{2}, F_{2} \perp A C$ we can calculate

$$\begin{align*}
\sphericalangle\left(E_{1} E_{2}, F_{1} F_{2}\right) & =\sphericalangle\left(E_{1} E_{2}, X_{1} X_{2}\right)+\sphericalangle\left(X_{1} X_{2}, F_{1} F_{2}\right)=\sphericalangle\left(B E_{2}, B X_{2}\right)+\sphericalangle\left(C X_{2}, C F_{2}\right) \\
& =\sphericalangle\left(Z_{2} E_{2}, Z_{2} X_{2}\right)+\sphericalangle\left(Y_{2} X_{2}, Y_{2} F_{2}\right)=\sphericalangle\left(Z_{2} E_{2}, \ell_{2}\right)+\sphericalangle\left(\ell_{2}, Y_{2} F_{2}\right) \\
& =\sphericalangle\left(Z_{2} E_{2}, Y_{2} F_{2}\right)=\sphericalangle(A B, A C) \not \equiv 0, \tag{1}
\end{align*}$$

and conclude that lines $E_{1} E_{2}$ and $F_{1} F_{2}$ are not parallel. 
Hence, $\Delta_{1}$ and $\Delta_{2}$ are homothetic; the lines 
$D_{1}D_{2}, E_{1}E_{2}$, and $F_{1}F_{2}$ are concurrent at the 
homothetic centre of the two triangles. Denote this homothetic centre by $H$.

For $i=1,2$, using (1), and that $A, Y_{i}, Z_{i}$ and $D_{i}$ are concyclic,

$$\begin{aligned}
\sphericalangle\left(H E_{i}, H F_{i}\right) & =\sphericalangle\left(E_{1} E_{2}, F_{1} F_{2}\right)=\sphericalangle(A B, A C) \\
& =\sphericalangle\left(A Z_{i}, A Y_{i}\right)=\sphericalangle\left(D_{i} Z_{i}, D_{i} Y_{i}\right)=\sphericalangle\left(D_{i} E_{i}, D_{i} F_{i}\right)
\end{aligned}$$

so $H$ lies on circle $\omega_{i}$.

The same homothety that maps $\Delta_{1}$ to $\Delta_{2}$, sends $\omega_{1}$ 
to $\omega_{2}$ as well. Point $H$, that is the centre of the homothety, 
is a common point of the two circles, That finishes proving that $\omega_{1}$ 
and $\omega_{2}$ are tangent to each other.

## Solution

As in the first solution, let the vertices of $\Delta_{i}$ be $D_{i}, E_{i}, F_{i}$, 
such that $E_{i} F_{i}, F_{i} D_{i}$ and $D_{i} E_{i}$ are the perpendiculars 
through $X_{i}, Y_{i}$ and $Z_{i}$, respectively. In the same way we conclude 
that $\left(A, D_{1}, D_{2}\right),\left(B, E_{1}, E_{2}\right)$ and 
$\left(C, F_{1}, F_{2}\right)$ are collinear.

The corresponding sides of triangles $ABC$ and $D_{i}E_{i}F_{i}$ 
are perpendicular to each other. Hence, there is a spiral similarity 
with rotation $\pm 90^{\circ}$ that maps $A B C$ to $D_{i} E_{i} F_{i}$; 
let $M_{i}$ be the centre of that similarity. 
Hence, $\sphericalangle\left(M_{i} A, M_{i} D_{i}\right) = \sphericalangle\left(M_{i} B, M_{i} E_{i}\right) = \sphericalangle\left(M_{i} C, M_{i} F_{i}\right)=90^{\circ}$.
The circle with diameter $A D_{i}$ passes through $M_{i}, Y_{i}, Z_{i}$, 
so $M_{i}, A, Y_{i}, Z_{i}, D_{i}$ are concyclic; analogously 
$\left(M_{i}, B, X_{i}, Z_{i}, E_{i}\right)$ and 
$\left(M_{i}, C, X_{i}, Y_{i}, F_{i}\right)$ are concyclic.

By applying Desargues' theorem to triangles $A B C$ and $D_{i}E_{i}F_{i}$ 
we conclude that the lines $AD_{i}$, $BE_{i}$ and $BF_{i}$ are concurrent; 
let their intersection be $H$. Since $\left(A, D_{1} . D_{2}\right)$,
$\left(B, E_{1} . E_{2}\right)$ and $\left(C, F_{1} . F_{2}\right)$ are collinear, 
we obtain the same point $H$ for $i=1$ and $i=2$.

![](IMO_SHL.2022.G5B.png)

By $\sphericalangle(C B, C H)=\sphericalangle\left(C X_{i}, C F_{i}\right)=\sphericalangle\left(Y_{i} X_{i}, Y_{i} F_{i}\right)=\sphericalangle\left(Y_{i} Z_{i}, Y_{i} D_{i}\right)=\sphericalangle\left(A Z_{i}, A D_{i}\right)=$ $\sphericalangle(A B, A H)$, point $H$ lies on circle $ABC$.

Analogously, from $\sphericalangle\left(F_{i} D_{i}, F_{i} H\right)=\sphericalangle\left(F_{i} Y_{i}, F_{i} C\right)=\sphericalangle\left(X_{i} Y_{i}, X_{i} C\right)=\sphericalangle\left(X_{i} Z_{i}, X_{i} B\right)=$ $\sphericalangle\left(E_{i} Z_{i}, E_{i} B\right)=\sphericalangle\left(E_{i} D_{i}, E_{i} H\right)$, 
we can see that point $H$ lies on circle $D_{i} E_{i} F_{i}$ as well. 
Therefore, circles $A B C$ and $D_{i} E_{i} F_{i}$ intersect at point $H$.

The spiral similarity moves the circle $A B C$ to circle $D_{i} E_{i} F_{i}$, 
so the two circles are perpendicular. Hence, both circles $D_{1} E_{1} F_{1}$ 
and $D_{2} E_{2} F_{2}$ are tangent to the radius of circle $A B C$ at $H$.

**Comment 1.** As the last picture suggests, the circles $A B C$ and 
$D_{i} E_{i} F_{i}$ pass through $M_{i}$. In fact, point $M_{i}$, 
being the second intersection of circles $D_{i} E_{i} F_{i}$ and 
$D_{i} Y_{i} Z_{i}$, the Miquel point of the lines $A Y_{i}, A Z_{i}, C X_{i}$ 
and $X_{i} Y_{i}$, so it is concyclic with $A, B, C$. 
Similarly, $M_{i}$ the Miquel point of lines 
$D_{i} E_{i}$, $E_{i} F_{i}, F_{i} Y_{i}$ and $X_{i} Y_{i}$, 
so it is concyclic with $D_{i}, E_{i}, D_{i}$.

**Comment 2.** Instead of two lines $\ell_{1}$ and $\ell_{2}$, it is 
possible to reformulate the problem with a single, varying line $\ell$:

Let $A B C$ be a triangle, and let $\ell$ be a varying line whose 
direction is fixed. Let $\ell$ intersect lines $B C$, $C A$, and 
$AB$ at $X,Y$, and $Z$, respectively. Suppose that the line through $X$, 
perpendicular to $BC$, the line through $Y$, perpendicular to $CA$, 
and the line through $Z$, perpendicular to $AB$, 
determine a non-degenerate triangle $\Delta$.

Show that as $\ell$ varies, the circumcircles of the obtained 
triangles $\Delta$ pass through a fixed point, and these circles are tangent to each other.

A reasonable approach is finding the position of line $\ell$ 
when the triangle $DEF$ degenerates to a single point. That happens when 
the line $XYZ$ is the Simson line respect to point $D=E=F$ on the 
circumcircle $ABC$. Based on this observation a possible variant 
of the solution is as follows.

Let $H$ be the second intersection of circles $A B C$ and line $AD$. 
Like in the solutions above, we can find that the line $AD$ is fixed, 
so $H$ is independent of the position of line $\ell$.

![](IMO_SHL.2022.G5C.png)

From $\sphericalangle(H F, H D)=\sphericalangle(H C, H A)=\sphericalangle(B C, B A)=\sphericalangle(B X, B Z)=\sphericalangle(E X, E Z)=\sphericalangle(E F, E D)$ we can see that circle $\Delta$ passes through $H$. 
Hence, all circles $D E F$ passes through a fixed point.

The corresponding sides of triangles $A B C$ and $D E F$ are perpendicular, 
so their circumcircle are perpendicular; that proves that circle $DEF$ 
is tangent to the radius of circle $ABC$ at $H$.




# <lo-sample/> IMO_SHL.2022.G6

Let $ABC$ be an acute triangle with altitude $\overline{AH}$, and let $P$ be 
a variable point such that the angle bisectors $k$ and $\ell$ of $\angle PBC$ 
and $\angle PCB$, respectively, meet on $\overline{AH}$. Let $k$ meet 
$\overline{AC}$ at $E$, $\ell$ meet $\overline{AB}$ at $F$, and 
$\overline{EF}$ meet $\overline{AH}$ at $Q$. Prove that as $P$ varies, 
line $PQ$ passes through a fixed point.


<small>

* domain:Geom
* source:Iran
* questionType:Prove
* concepts:triangle,altitude,point,angle

</small>


## Solution

Let the reflections of the line $BC$ with respect to the lines 
$AB$ and $AC$ intersect at point $K$. We will prove that $P,Q$ and 
$K$ are collinear, so $K$ is the common point of the varying line $PQ$.

Let lines $B E$ and $C F$ intersect at $I$. For every point $O$ 
and $d>0$, denote by $(O, d)$ the circle centred at $O$ with radius $d$, 
and define $\omega_{I}=(I, IH)$ and $\omega_{A}=(A, AH)$. 
Let $\omega_{K}$ and $\omega_{P}$ be the incircle of triangle 
$KBC$ and the $P$-excircle of triangle $PBC$, respectively.

Since $IH \perp BC$ and $AH \perp BC$, the circles $\omega_{A}$ 
and $\omega_{I}$ are tangent to each other at $H$. So, $H$ is 
the external homothetic centre of $\omega_{A}$ and $\omega_{I}$. 
From the complete quadrangle $BCEF$ we have $(A, I ; Q, H)=-1$, 
therefore $Q$ is the internal homothetic centre of 
$\omega_{A}$ and $\omega_{I}$. Since $B A$ and $C A$ are the 
external bisectors of angles $\angle K B C$ and $\angle KCB$, 
circle $\omega_{A}$ is the $K$-excircle in triangle $BKC$. 
Hence, $K$ is the external homothetic centre of $\omega_{A}$ 
and $\omega_{K}$. Also it is clear that $P$ is the external homothetic 
centre of $\omega_{I}$ and $\omega_{P}$. Let point $T$ be the 
tangency point of $\omega_{P}$ and $B C$, and let $T^{\prime}$ 
be the tangency point of $\omega_{K}$ and $B C$. Since $\omega_{I}$ 
is the incircle and $\omega_{P}$ is the $P$-excircle of $PBC$, $TC=BH$ 
and since $\omega_{K}$ is the incircle and $\omega_{A}$ is the 
$K$-excircle of $KBC$, $T^{\prime}C = BH$. Therefore $TC = T^{\prime}C$ 
and $T \equiv T^{\prime}$. It yields that $\omega_{K}$ and 
$\omega_{P}$ are tangent to each other at $T$.

![](IMO_SHL.2022.G6A.png)

Let point $S$ be the internal homothetic centre of $\omega_{A}$ 
and $\omega_{P}$, and let $S^{\prime}$ be the internal homothetic 
centre of $\omega_{I}$ and $\omega_{K}$. It's obvious that $S$ 
and $S^{\prime}$ lie on $B C$. We claim that $S \equiv S^{\prime}$. 
To prove our claim, let $r_{A}, r_{I}, r_{P}$, and $r_{K}$ be the 
radii of $\omega_{A}, \omega_{I}, \omega_{P}$ and $\omega_{k}$, respectively.

It is well known that if the sides of a triangle are $a, b, c$, 
its semiperimeter is $s=(a+b+c) / 2$, and the radii of the incircle 
and the $a$-excircle are $r$ and $r_{a}$, respectively, then 
$r \cdot r_{a}=(s-b)(s-c)$. Applying this fact to triangle $PBC$ 
we get $r_{I} \cdot r_{P}=B H \cdot C H$. The same fact in triangle $K C B$
yields $r_{K} \cdot r_{A}=C T \cdot B T$. Since $BH=CT$ and 
$BT=CH$, from these two we get

$$\frac{H S}{S T}=\frac{r_{A}}{r_{P}}=\frac{r_{I}}{r_{K}}=\frac{H S^{\prime}}{S^{\prime} T}$$

so $S=S^{\prime}$ indeed.

Finally, by applying the generalised Monge's theorem to the circles 
$\omega_{A}$, $\omega_{I}$, and $\omega_{K}$ (with two pairs of internal 
and one pair of external common tangents), we can see that points 
$Q$, $S$, and $K$ are collinear. Similarly one can show that $Q,S$ 
and $P$ are collinear, and the result follows.

Solution 2. Again, let $B E$ and $C F$ meet at $I$, that is the 
incentre in triangle $B C P$; then $P I$ is the third angle bisector. 
From the tangent segments of the incircle we have $BP - CP = \mathrm{BH}-\mathrm{CH}$; 
hence, the possible points $P$ lie on a branch of a hyperbola $\mathcal{H}$ 
with foci $B,C$, and $H$ is a vertex of $\mathcal{H}$. Since $PI$ bisects 
the angle between the radii $BP$ and $CP$ of the hyperbola, 
line $PI$ is tangent to $\mathcal{H}$.

![](IMO_SHL.2022.G6B.png)

Let $K$ be the second intersection of $P Q$ and $\mathcal{H}$, 
we will show that $A K$ is tangent to $\mathcal{H}$ at $K$; 
this property determines $K$.

Let $G=K I \cap A P$ and $M=P I \cap A K$. From the complete quadrangle 
$B C E F$ we can see that $(H, Q ; I, A)$ is harmonic, so in the complete 
quadrangle $A P I K$, point $H$ lies on line $G M$.

Consider triangle $AIM$. Its side $A I$ is tangent to $\mathcal{H}$ at $H$, 
the side $I M$ is tangent to $\mathcal{H}$ at $P$, and $K$ is a common point 
of the third side $A M$ and the hyperbola such that the lines $A P$, $I K$ 
and $M H$ are concurrent at the generalised Gergonne-point $G$. 
It follows that the third side, $A M$ is also tangent to $\mathcal{H}$ at $K$.

(Alternatively, in the last step we can apply the converse of Brianchon's 
theorem to the degenerate hexagon $A H I P M K$. By the theorem there 
is a conic section $\mathcal{H}^{\prime}$ such that lines $A I, I M$ and 
$M A$ are tangent to $\mathcal{H}^{\prime}$ at $H, P$ and $K$, respectively. 
But the three points $H, K$ and $P$, together with the tangents at $H$ and 
$P$ uniquely determine $\mathcal{H}^{\prime}$, so indeed 
$\mathcal{H}^{\prime}=\mathcal{H}$.)




# <lo-sample/> IMO_SHL.2022.G7

Two triangles $ABC$, $A’B’C’$ have the same orthocenter $H$ and the same 
circumcircle with center $O$. Letting $PQR$ be the triangle formed by 
$AA’, BB’, CC’$, prove that the circumcenter of $PQR$ lies on $OH$.


<small>

* domain:Geom
* source:Denmark
* questionType:Prove
* concepts:triangle

</small>


## Solution

In what follows, $\sphericalangle(p, q)$ will denote the directed angle 
between lines $p$ and $q$, taken modulo $180^{\circ}$. 
Denote by $O$ the centre of $\omega$. In any triangle, the homothety 
with ratio $-\frac{1}{2}$ centred at the centroid of the triangle 
takes the vertices to the midpoints of the opposite sides and it 
takes the orthocentre to the circumcentre. Therefore the triangles 
$ABC$ and $A^{\prime}B^{\prime}C^{\prime}$ share the same centroid 
$G$ and the midpoints of their sides lie on a circle $\rho$ with 
centre on $O H$. We will prove that $\omega, \Omega$, and 
$\rho$ are coaxial, so in particular it follows that their 
centres are collinear on $OH$.

Let $D=B B^{\prime} \cap C C^{\prime}$, 
$E=C C^{\prime} \cap A A^{\prime}$, 
$F=A A^{\prime} \cap B B^{\prime}$, 
$S=B C^{\prime} \cap B^{\prime} C$, and 
$T=B C \cap B^{\prime} C^{\prime}$. 
Since $D, S$, and $T$ are the intersections of opposite sides and of the 
diagonals in the quadrilateral $B B^{\prime} C C^{\prime}$ inscribed in 
$\omega$, by Brocard's theorem triangle $DST$ is self-polar with 
respect to $\omega$, i.e. each vertex is the pole of the opposite side. 
We apply this in two ways.

![](IMO_SHL.2022.G7A.png)

First, from $D$ being the pole of $S T$ it follows that the inverse 
$D^{*}$ of $D$ with respect to $\omega$ is the projection of $D$ onto $ST$. 
In particular, $D^{*}$ lies on the circle with diameter $SD$. 
If $N$ denotes the midpoint of $S D$ and $R$ the radius of $\omega$, 
then the power of $O$ with respect to this circle is 
$ON^{2} - ND^{2}=O D \cdot OD^{*}=R^{2}$. By rearranging, we see that 
$N D^{2}$ is the power of $N$ with respect to $\omega$.

Second, from $T$ being the pole of $SD$ it follows that $OT$ is 
perpendicular to $S D$. Let $M$ and $M^{\prime}$ denote the midpoints 
of $B C$ and $B^{\prime} C^{\prime}$. Then since $OM \perp BC$ and 
$OM^{\prime} \perp B^{\prime}C^{\prime}$ it follows that $OMM^{\prime}T$ 
is cyclic and

$$\sphericalangle(S D, B C)=\sphericalangle(O T, O M)=\sphericalangle\left(B^{\prime} C^{\prime}, M M^{\prime}\right)$$

From $B B^{\prime} C C^{\prime}$ being cyclic we also have 
$\sphericalangle\left(B C, B B^{\prime}\right)=\sphericalangle\left(C C^{\prime}, B^{\prime} C^{\prime}\right)$, 
hence we obtain

$$\begin{aligned}
\sphericalangle\left(S D, B B^{\prime}\right) & =\sphericalangle(S D, B C)+\sphericalangle\left(B C, B B^{\prime}\right) \\
& =\sphericalangle\left(B^{\prime} C^{\prime}, M M^{\prime}\right)+\sphericalangle\left(C C^{\prime}, B^{\prime} C^{\prime}\right)=\sphericalangle\left(C C^{\prime}, M M^{\prime}\right) .
\end{aligned}$$

Now from the homothety mentioned in the beginning, we know that $M M^{\prime}$ 
is parallel to $A A^{\prime}$, hence the above implies that 
$\sphericalangle\left(S D, B B^{\prime}\right)=\sphericalangle\left(C C^{\prime}, A A^{\prime}\right)$, 
which shows that $\Omega$ is tangent to $S D$ at $D$. In particular, 
$N D^{2}$ is also the power of $N$ with respect to $\Omega$.

Additionally, from $B B^{\prime} C C^{\prime}$ being cyclic it follows 
that triangles $D B C$ and $D C^{\prime} B^{\prime}$ are inversely similar, 
so $\sphericalangle\left(B B^{\prime}, D M^{\prime}\right)=\sphericalangle\left(D M, C C^{\prime}\right)$. 
This yields

$$\begin{aligned}
\sphericalangle\left(S D, D M^{\prime}\right) & =\sphericalangle\left(S D, B B^{\prime}\right)+\sphericalangle\left(B B^{\prime}, D M^{\prime}\right) \\
& =\sphericalangle\left(C C^{\prime}, M M^{\prime}\right)+\sphericalangle\left(D M, C C^{\prime}\right)=\sphericalangle\left(D M, M M^{\prime}\right)
\end{aligned}$$

which shows that the circle $D M M^{\prime}$ is also tangent to $S D$. 
Since $N, M$, and $M^{\prime}$ are collinear on the Newton-Gauss line 
of the complete quadrilateral determined by the lines 
$B B^{\prime}, C C^{\prime}, B C^{\prime}$, and $B^{\prime} C$, 
it follows that $N D^{2}=N M \cdot N M^{\prime}$. Hence $N$ has 
the same power with respect to $\omega$, $\Omega$, and $\rho$.

By the same arguments there exist points on the tangents to $\Omega$ 
at $E$ and $F$ which have the same power with respect to $\omega, \Omega$, 
and $\rho$. The tangents to a given circle at three distinct points 
cannot be concurrent, hence we obtain at least two distinct points 
with the same power with respect to $\omega, \Omega$, and $\rho$. 
Hence the three circles are coaxial, as desired.

**Comment 1.** Instead of invoking the Newton-Gauss line, one can also 
use a nice symmetry argument: If from the beginning we swapped the 
labels of $B^{\prime}$ and $C^{\prime}$, then in the proof above 
the labels of $D$ and $S$ would be swapped while the labels of $M$
and $M^{\prime}$ do not change. The consequence is that the circle 
$S M M^{\prime}$ is also tangent to $S D$. Since $N$ is the midpoint 
of $S D$ it then has the same power with respect to circles 
$DMM^{\prime}$ and $SMM^{\prime}$, so it lies on their radical axis $MM^{\prime}$.

**Comment 2.** There exists another triple of points on the common 
radical axis of $\omega, \Omega$, and $\rho$ which can be used to solve 
the problem. We outline one such solution.

![](IMO_SHL.2022.G7B.png)

Let $L$ and $L^{\prime}$ denote the feet of the altitudes from $A$ and 
$A^{\prime}$ in triangle $A B C$ and $A^{\prime} B^{\prime} C^{\prime}$, 
respectively. Since $\rho$ is the nine-point circle of the two triangles 
it contains both $L$ and $L^{\prime}$. Furthermore, $H A \cdot H L$ 
and $H A^{\prime} \cdot H L^{\prime}$ both equal twice the power of $H$ 
with respect to $\rho$, so $A, A^{\prime}, L, L^{\prime}$ 
are concyclic as well.

Now let $\ell=A A^{\prime}$ and denote $P=L L^{\prime} \cap \ell, K=B C \cap \ell$, 
and $K^{\prime}=B^{\prime} C^{\prime} \cap \ell$. As $M M^{\prime} \| \ell$ 
(shown in the previous solution) and $L L^{\prime} M M^{\prime}$ is cyclic

$$
\sphericalangle(B C, \ell)=\sphericalangle\left(B C, M M^{\prime}\right)=\sphericalangle\left(L L^{\prime}, B^{\prime} C^{\prime}\right)
$$

so $K, K^{\prime}, L$, and $L^{\prime}$ are also concyclic. 
From the cyclic quadrilaterals $A A^{\prime} L L^{\prime}$ and 
$K K^{\prime} L L^{\prime}$ we get 
$P A \cdot P A^{\prime}=P L \cdot P L^{\prime}=P K \cdot P K^{\prime}$. 
This implies that $P$ is the centre of the (unique) involution $\sigma$ 
on $\ell$ that swaps $A, A^{\prime}$ and $K, K^{\prime}$. On the other hand, 
by Desargues' involution theorem applied to the line $\ell$, 
the quadrilateral $B B^{\prime} C C^{\prime}$, and its circumcircle $\omega$, 
the involution $\sigma$ also swaps $E$ and $F$. Hence

$$PA \cdot PA^{\prime} = PL \cdot PL^{\prime} = PE \cdot PF$$

However, this means that $P$ has the same power with respect to 
$\omega, \Omega$, and $\rho$, and by the same arguments there exist 
points on $B B^{\prime}$ and $C C^{\prime}$ with this property.



# <lo-sample/> IMO_SHL.2022.G8

Let $AA'BCC'B'$ be a convex cyclic hexagon such that $AC$ is tangent 
to the incircle of the triangle $A'B'C'$, and $A'C'$ is tangent to the 
incircle of the triangle $ABC$. Let the lines $AB$ and $A'B'$ meet at 
$X$ and let the lines $BC$ and $B'C'$ meet at $Y$.

Prove that if $XBYB'$ is a convex quadrilateral, then it has an incircle.


<small>

* domain:Geom
* source:Australia
* questionType:Prove
* concepts:hexagon,tangent,triangle,line,inscribed-circle

</small>


## Solution

Denote by $\omega$ and $\omega^{\prime}$ the incircles of $\triangle ABC$ 
and $\triangle A^{\prime} B^{\prime} C^{\prime}$ and let $I$ and 
$I^{\prime}$ be the centres of these circles. Let $N$ and $N^{\prime}$ 
be the second intersections of $B I$ and $B^{\prime} I^{\prime}$ 
with $\Omega$, the circumcircle of $A^{\prime} B C C^{\prime} B^{\prime} A$, 
and let $O$ be the centre of $\Omega$. Note that 
$O N \perp A C, O N^{\prime} \perp A^{\prime} C^{\prime}$ and 
$O N=O N^{\prime}$ so $N N^{\prime}$ is parallel to the angle bisector 
$I I^{\prime}$ of $A C$ and $A^{\prime} C^{\prime}$. Thus 
$I I^{\prime} \| N N^{\prime}$ which is antiparallel to $B B^{\prime}$ 
with respect to $B I$ and $B^{\prime} I^{\prime}$. 
Therefore $B, I, I^{\prime}, B^{\prime}$ are concyclic.

![](IMO_SHL.2022.G8A.png)

Further define $P$ as the intersection of $A C$ and $A^{\prime} C^{\prime}$ 
and $M$ as the antipode of $N^{\prime}$ in $\Omega$. Consider the circle 
$\Gamma_{1}$ with centre $N$ and radius $N A=N C$ and the circle 
$\Gamma_{2}$ with centre $M$ and radius $M A^{\prime}=M C^{\prime}$. 
Their radical axis passes through $P$ and is perpendicular to 
$M N \perp N N^{\prime} \| I P$, so $I$ lies on their radical axis. 
Therefore, since $I$ lies on $\Gamma_{1}$, it must also lie on $\Gamma_{2}$. 
Thus, if we define $Z$ as the second intersection of $M I$ with $\Omega$, 
we have that $I$ is the incentre of triangle $Z A^{\prime} C^{\prime}$. 
(Note that the point $Z$ can also be constructed directly via Poncelet's porism.)

Consider the incircle $\omega_{c}$ with centre $I_{c}$ of triangle $C^{\prime} B^{\prime} Z$. Note that $\angle Z I C^{\prime}=90^{\circ}+$ $\frac{1}{2} \angle Z A^{\prime} C^{\prime}=90^{\circ}+\frac{1}{2} \angle Z B^{\prime} C^{\prime}=\angle Z I_{c} C^{\prime}$, 
so $Z, I, I_{c}, C^{\prime}$ are concyclic. 
Similarly $B^{\prime}, I^{\prime}, I_{c}, C^{\prime}$ are concyclic.

The external centre of dilation from $\omega$ to $\omega_{c}$ is the 
intersection of $I I_{c}$ and $C^{\prime} Z(D$ in the picture), 
that is the radical centre of circles $\Omega, C^{\prime} I_{c} I Z$ and 
$I I^{\prime} I_{c}$. Similarly, the external centre of dilation from 
$\omega^{\prime}$ to $\omega_{c}$ is the intersection of $I^{\prime} I_{c}$ 
and $B^{\prime} C^{\prime}$ ( $D^{\prime}$ in the picture), that is the 
radical centre of circles $\Omega, B^{\prime} I^{\prime} I_{c} C^{\prime}$ 
and $I I^{\prime} I_{c}$. Therefore the Monge line of $\omega, \omega^{\prime}$ 
and $\omega_{c}$ is line $D D^{\prime}$, and the radical axis of 
$\Omega$ and circle $I I^{\prime} I_{c}$ coincide. Hence the external 
centre $T$ of dilation from $\omega$ to $\omega^{\prime}$ is also on 
the radical axis of $\Omega$ and circle $I I^{\prime} I_{c}$.

![](IMO_SHL.2022.G8B.png)

Now since $B, I, I^{\prime}, B^{\prime}$ are concyclic, the intersection 
$T^{\prime}$ of $B B^{\prime}$ and $I I^{\prime}$ is on the radical axis 
of $\Omega$ and circle $I I^{\prime} I_{c}$. Thus $T^{\prime}=T$ and 
$T$ lies on line $B B^{\prime}$. Finally, construct a circle $\Omega_{0}$ 
tangent to $A^{\prime} B^{\prime}, B^{\prime} C^{\prime}, A B$ on the 
same side of these lines as $\omega^{\prime}$. The centre of dilation 
from $\omega^{\prime}$ to $\Omega_{0}$ is $B^{\prime}$, so by Monge's 
theorem the external centre of dilation from $\Omega_{0}$ to $\omega$ 
must be on the line $T B B^{\prime}$. However, it is on line $A B$, 
so it must be $B$ and $B C$ must be tangent to $\Omega_{0}$ as desired.

![](IMO_SHL.2022.G8C.png)






# <lo-sample/> IMO_SHL.2022.N1

A number is called Norwegian if it has three distinct positive divisors 
whose sum is equal to $2022$. Determine the smallest Norwegian number.  
(*Note:* The total number of positive divisors of a Norwegian number 
is allowed to be larger than $3$.)


<small>

* domain:NT
* source:Cyprus
* questionType:FindOptimal
* concepts:divisors,sum

</small>


## Solution

*Answer:* $1344$

Observe that $1344$ is a Norwegian number as $6$, $672$ and $1344$ are three distinct 
divisors of $1344$ and $6+672+1344=2022$. It remains to show that this 
is the smallest such number.

Assume for contradiction that $N<1344$ is Norwegian and let 
$N/a$, $N/b$ and $N/c$ be the three distinct divisors of $N$, with $a<b<c$. Then

$$2022=N\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)<1344\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)$$

and so

$$\left(\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\right)>\frac{2022}{1344}=\frac{337}{224}=\frac{3}{2}+\frac{1}{224}$$

If $a>1$ then

$$\frac{1}{a}+\frac{1}{b}+\frac{1}{c} \leqslant \frac{1}{2}+\frac{1}{3}+\frac{1}{4}=\frac{13}{12}<\frac{3}{2}$$

so it must be the case that $a=1$. Similarly, it must hold that $b<4$ since otherwise

$$1+\frac{1}{b}+\frac{1}{c} \leqslant 1+\frac{1}{4}+\frac{1}{5}<\frac{3}{2}$$

This leaves two cases to check, $b=2$ and $b=3$.

**Case** $b=3$. Then

$$\frac{1}{c}>\frac{3}{2}+\frac{1}{224}-1-\frac{1}{3}>\frac{1}{6}$$

so $c=4$ or $c=5$. If $c=4$ then

$$2022=N\left(1+\frac{1}{3}+\frac{1}{4}\right)=\frac{19}{12} N$$

but this is impossible as $19 \nmid 2022$. If $c=5$ then

$$2022=N\left(1+\frac{1}{3}+\frac{1}{5}\right)=\frac{23}{15} N$$

which again is impossible, as $23 \nmid 2022$.

**Case** $b=2$. Note that $c<224$ since

$$\frac{1}{c}>\frac{3}{2}+\frac{1}{224}-1-\frac{1}{2}=\frac{1}{224}$$

It holds that

$$2022=N\left(1+\frac{1}{2}+\frac{1}{c}\right)=\frac{3 c+2}{2 c} N \Rightarrow(3 c+2) N=4044 c$$

Since $(c, 3 c-2)=(c, 2) \in\{1,2\}$, then $3 c+2 \mid 8088=2^{3} \cdot 3 \cdot 337$ 
which implies that $3 c+2 \mid 2^{3} \cdot 337$. But since 
$3c+2 \geqslant 3 \cdot 3+2>8=2^{3}$ and $3c+2 \neq 337$, then it must hold that 
$3c+2 \geqslant 2 \cdot 337$, contradicting $c<224$.


# <lo-sample/> IMO_SHL.2022.N2

Find all positive integers $n>2$ such that

$$n! \mid \prod_{ p<q\le n, p,q \, \text{primes}} (p+q)$$


<small>

* domain:NT
* source:Nigeria
* questionType:FindAll
* concepts:integer-numbers

</small>


## Solution

*Answer:* This only holds for $n=7$.

Assume that $n$ satisfies $n!\mid \prod_{p<q \leqslant n}(p+q)$ and 
let $2=p_{1}<p_{2}<\cdots<p_{m} \leqslant n$ be the primes in 
$\{1,2, \ldots, n\}$. Each such prime divides $n$ !. In particular, 
$p_{m} \mid p_{i}+p_{j}$ for some $p_{i}<p_{j} \leqslant n$. But

$$0<\frac{p_{i}+p_{j}}{p_{m}}<\frac{p_{m}+p_{m}}{p_{m}}=2$$

so $p_{m}=p_{i}+p_{j}$ which implies $m \geqslant 3, p_{i}=2$ and $p_{m}=2+p_{j}=2+p_{m-1}$.

Similarly, $p_{m-1} \mid p_{k}+p_{l}$ for some $p_{k}<p_{l} \leqslant n$. But

$$0<\frac{p_{l}+p_{k}}{p_{m-1}} \leqslant \frac{p_{m}+p_{m-1}}{p_{m-1}}=\frac{2 p_{m-1}+2}{p_{m-1}}<3$$

so either $p_{m-1}=p_{l}+p_{k}$ or $2 p_{m-1}=p_{l}+p_{k}$. 
As above, the former case gives $p_{m-1}=2+p_{m-2}$. 
If $2 p_{m-1}=p_{l}+p_{k}$, then $p_{m-1}<p_{k}$, so $k=m$ and

$$2 p_{m-1}=p_{l}+p_{m-1}+2 \Rightarrow p_{m-1}=p_{l}+2=p_{m-2}+2$$

Either way, $p_{m-2}>2$ and 3 divides one of $p_{m-2}, p_{m-1}=p_{m-2}+2$ and 
$p_{m}=p_{m-2}+4$. This implies $sp_{m-2}=3$ and thus $p_{m}=7$, giving $7 \leqslant n<11$.

Finally, a quick computation shows that $7! \mid \prod_{p<q \leqslant 7}(p+q)$ 
but $8!\nmid \prod_{p<q \leqslant 7}(p+q)$, so neither does $9!$ and $10!$.



# <lo-sample/> IMO_SHL.2022.N3

Let $a > 1$ be a positive integer and $d > 1$ be a positive integer 
coprime to $a$. Let $x_1=1$, and for $k\geq 1$, define

$$x_{k+1} = \begin{cases} 
x_k + d &\text{if } a \text{ does not divide } x_k \\ 
x_k/a & \text{if } a \text{ divides } x_k 
\end{cases}$$

Find, in terms of $a$ and $d$, the greatest positive integer $n$ 
for which there exists an index $k$ such that $x_k$ is divisible by $a^n$.


<small>

* domain:NT
* source:Croatia
* questionType:FindOptimal
* concepts:integer-numbers,coprimes,divisibility

</small>


## Solution

*Answer:* $n$ is the exponent with $d<a^{n}<a d$.

By trivial induction, $x_{k}$ is coprime to $d$.

By induction and the fact that there can be at most $a-1$ consecutive 
increasing terms in the sequence, it also holds that $x_{k}<d a$ if 
$x_{k}=x_{k-1}+d$ and that $x_{k}<d$ if $x_{k}=\frac{x_{k-1}}{a}$ or $k=1$. 
This gives the upper bound on the exponent.

This implies that the sequence is (eventually) periodic, 
and that both increasing and decreasing steps happen infinitely many times. 
Let $a^{-k}$ be the multiplicative inverse of $a^{k}$ modulo $d$. 
The sequence contains elements congruent to $1, a^{-1}, a^{-2}, \ldots$ modulo $d$.

Let $x_{k_{0}}$ the first element such that $x_{k_{0}} \equiv a^{-n}(\bmod d)$. 
We have either $k_{0}=1$ or $x_{k_{0}}=$ $x_{k_{0}-1} / a$; 
in both cases $x_{k_{0}}<d<a^{n}<d a$ and therefore

$$x_{k_{0}} \in\left\{a^{n}-d, a^{n}-2 d, \ldots, a^{n}-(a-1) d\right\}$$

In this set no element is divisible by $a$, so therefore the sequence 
will visit the value $a^{n}$ in the next $a-1$ steps.

## Solution

Like in the first solution, $x_{k}$ is relatively prime to $d$ and $x_{k}<a d$ for all $k$.

Let

$$S=\left\{x \in \mathbb{Z}_{>0}: 0<x<a d, \operatorname{gcd}(x, d)=1\right\} \quad \text { and } \quad f: S \rightarrow S, f(x)= \begin{cases}x+d & \text { if } a \nmid x \\ x / a & \text { if } a \mid x\end{cases}$$

So, we have $x_{1}=1$ and $x_{k+1}=f\left(x_{k}\right)$.

Notice that the recurrence formula is invertible. Suppose that $f(x)=y$ for some 
$x, y \in S$. If $y>d$ then $y-d \in S$ but $a \cdot y \notin S$; otherwise, 
if $y<d$ then $a \cdot y \in S$ but $y-d \notin S$. So, the function $f$ 
is a permutation on $S$, and its inverse is

$$f^{-1}(y)=\left\{\begin{array}{ll}
y-d & \text { if } y>d, \\
a \cdot y & \text { if } y<d
\end{array} \quad \text { for all } y \in S\right.$$

It follows that the sequence is periodic, and therefore attains the initial 
value 1 infinitely many times. Let $k_{1}>1$ be an index such that $x_{k_{1}}=1$. Then

$$x_{k_{1}}=1, \quad x_{k_{1}-1}=f^{-1}(1)=a, x_{k_{1}-2}=f^{-1}(a)=a^{2}, \ldots, \quad x_{k_{1}-n}=a^{n}$$

## Solution 

Like in the first solution, $x_{k}$ is relatively prime to $d$ and $x_{k}<a d$ for all $k$.

We wish to prove that there are $n$ consecutive decreasing indices. Let 
$m_{0}=0$ and $m_{k}$ be the $k$-th smallest decreasing index (an index 
$k$ is decreasing if $x_{k}=x_{k-1} / a$ ) and define a sequence 
$\left(y_{k}\right)_{k}=\left(x_{m_{k}}\right)_{k}$, i.e. the 
subsequence consisting only of elements with decreasing indices. 
For each $k \geqslant 1$ we can write

$$y_{k+1}=\frac{y_{k}+z_{k} d}{a}$$

for some $z_{k} \in\{0,1, \ldots, a-1\}$, where $z_{k}=0$ 
if and only if $y_{k}$ and $y_{k+1}$ are consecutive elements in the original sequence. Then

$$y_{k}=\frac{1+\left(z_{0}+z_{1} a+\cdots+z_{k-1} a^{k-1}\right) d}{a^{k}}$$

because $y_{k}$ is bounded the sequence is (eventually) periodic. 
Consider some $y_{u}=y_{u+v}$ where $v \geqslant 1$. We can write

$$y_{u}=\frac{1+\left(z_{0}+z_{1} a+\cdots+z_{u-1} a^{u-1}\right) d}{a^{u}}$$

and

$$y_{u+v}=\frac{1+\left(z_{0}+z_{1} a+\cdots+z_{u+v-1} a^{u+v-1}\right) d}{a^{u+v}}$$

and so

$$\frac{1+\left(z_{0}+z_{1} a+\cdots+z_{u+v-1} a^{u+v-1}\right) d}{a^{u+v}}=\frac{1+\left(z_{0}+z_{1} a+\cdots+z_{u-1} a^{u-1}\right) d}{a^{u}}$$

Rearranging gives

$$\frac{a^{v}-1}{d}=z_{0}+z_{1} a+\cdots+z_{v-1} a^{v-1}+\left(z_{v}-z_{0}\right) a^{v}+\cdots+\left(z_{u+v-1}-z_{u-1}\right) a^{u+v-1}$$

Since $d>a^{n} / a=a^{n-1}$ the LHS is strictly less than $a^{v-n}$. 
This implies that on the RHS, the coefficients of $a^{v-n}, a^{v-n+1}, \ldots$ 
must all be zero, i.e. $z_{v-n}=z_{v-n+1}=\cdots=z_{v-1}=0$.
This implies that there are $n$ consecutive decreasing indices in the original sequence.



# <lo-sample/> IMO_SHL.2022.N4

Find all triples $(a,b,p)$ of positive integers with 
$p$ prime and \[ a^p=b!+p. \]


<small>

* domain:NT
* questionType:FindAll
* source:Belgium
* concepts:integer-numbers

</small>


## Solution

*Answer:* $(2,2,2)$ and $(3,4,3)$.

Clearly, $a>1$. We consider three cases.

**Case 1:** We have $a<p$. Then we either have $a \leqslant b$ which implies 
$a \mid a^{p}-b!=p$ leading to a contradiction, or $a>b$ which is also impossible 
since in this case we have $b!\leqslant a!<a^{p}-p$, where the last 
inequality is true for any $p>a>1$.

**Case 2:** We have $a>p$. In this case $b!=a^{p}-p>p^{p}-p \geqslant p!$ so $b>p$ 
which means that $a^{p}=b!+p$ is divisible by $p$. Hence, $a$ is divisible by $p$ 
and $b!=a^{p}-p$ is not divisible by $p^{2}$. This means that $b<2 p$. If $a<p^{2}$ 
then $a / p<p$ divides both $a^{p}$ and $b!$ and hence it also divides 
$p=a^{p}-b!$ which is impossible. On the other hand, 
the case $a \geqslant p^{2}$ is also impossible since then 
$a^{p} \geqslant\left(p^{2}\right)^{p}>(2 p-1)!+p \geqslant b!+p$.

**Comment.** The inequality $p^{2 p}>(2 p-1)!+p$ can be shown e.g. by using

$$(2p-1)!=[1 \cdot(2 p-1)] \cdot[2 \cdot(2 p-2)] \cdots \cdots[(p-1)(p+1)] \cdot p < 
\left(\left(\frac{2 p}{2}\right)^{2}\right)^{p-1} \cdot p=p^{2 p-1}$$

where the inequality comes from applying AM-GM to each of the terms in square brackets.

**Case 3:** We have $a=p$. In this case $b!=p^{p}-p$. One can check that 
the values $p=2,3$ lead to the claimed solutions and $p=5$ does not lead to a solution. 
So we now assume that $p \geqslant 7$. 
We have $b!=p^{p}-p>p!$ and so $b \geqslant p+1$ which implies that

$$\nu_{2}((p+1)!) \leqslant \nu_{2}(b!) = \nu_{2}\left(p^{p-1}-1\right) \stackrel{LTE}{=} 
2\nu_{2}(p-1) + \nu_{2}(p+1)-1 = \nu_{2}\left(\frac{p-1}{2} \cdot(p-1) \cdot(p+1)\right),$$

where in the middle we used lifting-the-exponent lemma. On the RHS we have three 
factors of $(p+1)!$. But, due to $p+1 \geqslant 8$, there are at least $4$ even 
numbers among $1,2, \ldots, p+1$, so this case is not possible.


## Solution

The cases $a \neq p$ are covered as in solution 1 , as are $p=2,3$. 
For $p \geqslant 5$ we have $b!=p\left(p^{p-1}-1\right)$. By Zsigmondy's Theorem 
there exists some prime $q$ that divides $p^{p-1}-1$ but does not divide 
$p^{k}-1$ for $k<p-1$. It follows that $\operatorname{ord}_{q}(p)=p-1$, and hence 
$q \equiv 1$ $\bmod (p-1)$. Note that $p \neq q$. But then we must have 
$q \geqslant 2 p-1$, giving

$$b!\geqslant(2 p-1)!=[1 \cdot(2 p-1)] \cdot[2 \cdot(2 p-2)] \cdots \cdots[(p-1) \cdot(p+1)] 
\cdot p>(2 p-1)^{p-1} p>p^{p}>p^{p}-p,$$ 

a contradiction.


## Solution

The cases $a \neq p$ are covered as in solution 1, 
as are $p=2,3$. Also $b>p$, as $p^{p}>p!+p$ for $p>2$. 
The cases $p=5,7,11$ are also checked manually, so assume $p \geqslant 13$.
Let $q \mid p+1$ be an odd prime. By LTE

$$\nu_{q}\left(p^{p}-p\right) = \nu_{q}\left(\left(p^{2}\right)^{\frac{p-1}{2}}-1\right) = 
\nu_{q}\left(p^{2}-1\right) + \nu_{q}\left(\frac{p-1}{2}\right) = \nu_{q}(p+1)$$

But $b \geqslant p+1$, so then $\nu_{q}(b!) > \nu_{q}(p+1)$, since $q<p+1$, a contradiction. 
This means that $p+1$ has no odd prime divisor, i.e. $p+1=2^{k}$ for some $k$.
Now let $q \mid p-1$ be an odd prime. By LTE

$$\nu_{q}\left(p^{p}-p\right)=2 \nu_{q}(p-1)$$

Let $d = \nu_{q}(p-1)$. Then $p \geqslant 1+q^{d}$, so

$$\nu_{q}(b!) \geqslant \nu_{q}(p!) \geqslant \nu_{q}\left(q^{d}!\right)>q^{d-1} \geqslant 2d$$

provided $d \geqslant 2$ and $q>3$, or $d \geqslant 3$.

If $q=3, d=2$ and $p \geqslant 13$ then 
$\nu_{q}(b!) \geqslant \nu_{q}(p!) \geqslant \nu_{q}(13!)=5 > 2d$. 
Either way, $d \leqslant 1$. If $p>2 q+1$ (so $p>3 q$, as $q \mid p-1$ ) then

$$\nu_{q}(b!) \geqslant \nu_{q}((3q)!)=3$$

so we must have $q \geqslant \frac{p}{2}$, in other words, $p-1 = 2q$. 
This implies that $p=2^{k}-1$ and $q=2^{k-1}-1$ are both prime, 
but it is not possible to have two consecutive Mersenne primes.



## Solution

Let $a=p, b>p$ and $p \geqslant 5$ (the remaining cases are dealt with as in solution $3$). 
Modulo $(p+1)^{2}$ it holds that

$p^{p}-p=(p+1-1)^{p}-p \equiv\binom{p}{1}(p+1)(-1)^{p-1}+(-1)^{p}-p=p(p+1)-1-p=p^{2}-1 \not \equiv 0 \bmod \left((p+1)^{2}\right)$.

Since $p \geqslant 5$, the numbers 2 and $\frac{p+1}{2}$ are distinct and less than or equal to $p$. Therefore, $p+1 \mid p!$, and so $(p+1)^{2} \mid(p+1)!$.

But $b \geqslant p+1$, so $b!\equiv 0 \not \equiv p^{p}-p \bmod (p+1)^{2}$, a contradiction.




# <lo-sample/> IMO_SHL.2022.N5

For each $1\leq i\leq 9$ and $T\in\mathbb N$, define $d_i(T)$ 
to be the total number of times the digit $i$ appears when 
all the multiples of $1829$ between $1$ and $T$ inclusive 
are written out in base $10$.

Show that there are infinitely many $T\in\mathbb N$ such that there are 
precisely two distinct values among $d_1(T)$, $d_2(T)$, $\dots$, $d_9(T)$.


<small>

* domain:NT
* questionType:Prove
* source:United Kingdom
* concepts:digit

</small>

## Solution

Let $n:=1829$. First, we choose some $k$ such that $n \mid 10^{k}-1$. 
For instance, any multiple of $\varphi(n)$ would work since $n$ is coprime to $10$. 
We will show that either $T=10^{k}-1$ or $T=10^{k}-2$ has the desired 
property, which completes the proof since $k$ can be taken to be arbitrary large.

For this it suffices to show that 
$\#\left\{d_{i}\left(10^{k}-1\right): 1 \leqslant i \leqslant 9\right\} \leqslant 2$. 
Indeed, if

$$\#\left\{d_{i}\left(10^{k}-1\right): 1 \leqslant i \leqslant 9\right\}=1$$

then, since $10^{k}-1$ which consists of all nines is a multiple of $n$, we have

$$d_{i}\left(10^{k}-2\right)=d_{i}\left(10^{k}-1\right) \text { for } i \in\{1, \ldots, 8\}, \text { and } d_{9}\left(10^{k}-2\right)<d_{9}\left(10^{k}-1\right)$$

This means that $\#\left\{d_{i}\left(10^{k}-2\right): 1 \leqslant i \leqslant 9\right\}=2$.

To prove that $\#\left\{d_{i}\left(10^{k}-1\right)\right\} \leqslant 2$ we 
need an observation. Let 
$\overline{a_{k-1} a_{k-2} \ldots a_{0}} \in\left\{1, \ldots, 10^{k}-1\right\}$ 
be the decimal expansion of an arbitrary number, possibly with leading zeroes. 
Then $\overline{a_{k-1} a_{k-2} \ldots a_{0}}$ is divisible by $n$ if and only if 
$\overline{a_{k-2} \ldots a_{0} a_{k-1}}$ is divisible by $n$. 
Indeed, this follows from the fact that

$$10 \cdot \overline{a_{k-1} a_{k-2} \ldots a_{0}}-\overline{a_{k-2} \ldots a_{0} a_{k-1}}=\left(10^{k}-1\right) \cdot a_{k-1}$$

is divisible by $n$.

This observation shows that the set of multiples of $n$ between 1 and $10^{k}-1$ 
is invariant under simultaneous cyclic permutation of digits when numbers are 
written with leading zeroes. Hence, for each $i \in\{1, \ldots, 9\}$ the number 
$d_{i}\left(10^{k}-1\right)$ is $k$ times larger than the number of $k$ digit 
numbers which start from the digit $i$ and are divisible by $n$. Since the 
latter number is either $\left\lfloor 10^{k-1} / n\right\rfloor$ or 
$1+\left\lfloor 10^{k-1} / n\right\rfloor$, we conclude that 
$\#\left\{d_{i}\left(10^{k}-1\right)\right\} \leqslant 2$.

**Comment.** More careful analysis shows that 
$\#\left\{d_{i}\left(10^{k}-1\right): 1 \leqslant i \leqslant 9\right\}=1$ 
if and only if $n \equiv 1$ $(\bmod 10)$, which is not the case for $n=1829$.



# <lo-sample/> IMO_SHL.2022.N6

Let $Q$ be a set of prime numbers, not necessarily finite. 
For a positive integer $n$ consider its prime factorization: 
define $p(n)$ to be the sum of all the exponents and 
$q(n)$ to be the sum of the exponents corresponding 
only to primes in $Q$. A positive integer $n$ is called 
special if $p(n)+p(n+1)$ and $q(n)+q(n+1)$ are both even integers. 
Prove that there is a constant $c>0$ independent of the set 
$Q$ such that for any positive integer $N>100$, 
the number of special integers in $[1,N]$ is at least $cN$.

(For example, if $Q=\{3,7\}$, then $p(42)=3$, $q(42)=2$, $p(63)=3$, 
$q(63)=3$, $p(2022)=3$, $q(2022)=1$.)


<small>

* domain:NT
* questionType:Prove
* source:Costa Rica
* concepts:integer-numbers,primes

</small>

## Solution

Let us call two positive integers $m, n$ friends if $p(m)+p(n)$ and 
$q(m)+q(n)$ are both even integers. We start by noting that the pairs 
$(p(k), q(k))$ modulo 2 can take at most 4 different values; thus, 
among any five different positive integers there are two which are friends.

In addition, both functions $p$ and $q$ satisfy $f(a b)=f(a)+f(b)$ for any 
$a, b$. Therefore, if $m$ and $n$ are divisible by $d$, then both $p$ and 
$q$ satisfy the equality $f(m)+f(n) = f(m/d) + f(n/d) + 2f(d)$. 
This implies that $m, n$ are friends if and only if $m/d, n/d$ are friends.

Let us call a set of integers $\left\{n_{1}, n_{2}, \ldots, n_{5}\right\}$ 
an interesting set if for any indexes $i, j$, the difference 
$d_{i j}=\left|n_{i}-n_{j}\right|$ divides both $n_{i}$ and $n_{j}$. 
We claim that if elements of an interesting set are all positive, 
then we can obtain a special integer. Indeed, if we were able to construct 
such a set, then there would be a pair of integers $\left\{n_{i}, n_{j}\right\}$ 
which are friends, according to the first observation. 
Additionally, the second observation yields that the quotients 
$n_{i} / d_{i j}, n_{j} / d_{i j}$ form a pair of friends, which happen 
to be consecutive integers, thus giving a special integer as desired.

In order to construct a family of interesting sets, we can start by observing 
that the set $\{0,6,8,9,12\}$ is an interesting set. Using that 
$72=2^{3} \cdot 3^{2}$ is the least common multiple of all pairwise differences 
in this set, we obtain a family of interesting sets by considering

$$\{72 k, 72 k+6,72 k+8,72 k+9,72 k+12\}$$

for any $k \geqslant 1$. If we consider the quotients (of these numbers 
by the appropriate differences), then we obtain that the set

$$S_{k}=\{6 k, 8 k, 9 k, 12 k, 12 k+1,18 k+2,24 k+2,24 k+3,36 k+3,72 k+8\}$$

has at least one special integer. In particular, the interval $[1,100 k]$ 
contains the sets $S_{1}, S_{2}, \ldots, S_{k}$, each of which has a special 
number. Any special number can be contained in at most ten sets $S_{k}$, 
from where we conclude that the number of special integers in $[1,100 k]$ 
is at least $k/10$.

Finally, let $N=100 k+r$, with $k \geqslant 1$ and $0 \leqslant r<100$, 
so that we have $N<100(k+1) \leqslant 200k$. Then the number of special 
integers in $[1, N]$ is at least $k/10 > N/2000$, as we wanted to prove.

**Comment 1.** The statement is also true for $N \geqslant 15$ as at least 
one of the numbers $7,14,15$ is special.

**Comment 2.** Another approach would be to note that if 
$p(2 n), p(2 n+1), p(2 n+2)$ all have the same parity then one of the numbers 
$n, 2n, 2n+1$ is special. Indeed, if $q(n)+q(n+1)$ is even then $n$ is 
special since $p(n)+p(n+1) \equiv p(2n) + p(2n+2) \equiv 0 \pmod {2}$. 
Otherwise, if $q(n)+q(n+1)$ is odd, so is $q(2n) + q(2n+2)$ which implies 
that exactly one of the numbers $2n, 2n+1$ is special.

Unfortunately, it seems hard to show that the set of such $n$ has positive 
density: see a recent paper 
[https://arxiv.org/abs/1509.01545](https://arxiv.org/abs/1509.01545) 
for the proof that all eight patterns of the parities of 
$p(n), p(n+1), p(n+2)$ appear for a positive proportion of positive integers.



# <lo-sample/> IMO_SHL.2022.N7

Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. 
Prove that there is at most one way (up to rotation and reflection) 
to place the elements of $S$ around the circle such that the product 
of any two neighbors is of the form $x^2+x+k$ for some positive integer $x$.


<small>

* domain:NT
* questionType:Prove
* source:U.S.A.
* concepts:integer-numbers,primes

</small>

## Solution

Let us allow the value $x=0$ as well; we prove the same statement under this 
more general constraint. Obviously that implies the statement with the original conditions.

Call a pair $\{p, q\}$ of primes with $p \neq q$ special if $p q=x^{2}+x+k$ 
for some nonnegative integer $x$. The following claim is the key mechanism of the problem:

*Claim.*  
(a) For every prime $r$, there are at most two primes less than $r$ forming a special pair with $r$.  
(b) If such $p$ and $q$ exist, then $\{p, q\}$ is itself special.  

We present two proofs of the claim.

*Proof 1.* We are interested in integers $1 \leqslant x<r$ satsfying

$$\begin{equation*}
x^{2}+x+k \equiv 0 \quad(\bmod r) \tag{1}
\end{equation*}$$

Since there are at most two residues modulo $r$ that can satisfy that quadratic 
congruence, there are at most two possible values of $x$. That proves (a).

Now suppose there are primes $p, q$ with $p<q<r$ and nonnegative integers $x, y$ such that

$$\begin{aligned}
& x^{2}+x+k=p r \\
& y^{2}+y+k=q r
\end{aligned}$$

From $p<q<r$ we can see that $0 \leqslant x<y \leqslant r-1$. 
The numbers $x, y$ are the two solutions of (1); by Vieta's formulas, 
we should have $x+y \equiv-1(\bmod r)$, so $x+y=r-1$.

Letting $K=4 k-1, X=2 x+1$, and $Y=2 y+1$, we obtain

$$\begin{gathered}
4 p r=X^{2}+K \\
4 q r=Y^{2}+K
\end{gathered}$$

with $X+Y=2 r$. Multiplying the two above equations,

$$\begin{aligned}
16 p q r^{2} & =\left(X^{2}+K\right)\left(Y^{2}+K\right) \\
& =(X Y-K)^{2}+K(X+Y)^{2} \\
& =(X Y-K)^{2}+4 K r^{2} \\
4 p q & =\left(\frac{X Y-K}{2 r}\right)^{2}+K
\end{aligned}$$

In particular, the number $Z=\frac{X Y-K}{2 r}$ should be an integer, 
and so $4 p q=Z^{2}+K$. By parity, $Z$ is odd, and thus

$$p q=z^{2}+z+k \quad \text { where } z=\frac{Z-1}{2}$$

so $\{p, q\}$ is special.

*Proof 2.* As before, we suppose that

$$\begin{aligned}
& x^{2}+x+k=p r \\
& y^{2}+y+k=q r
\end{aligned}$$

Subtracting, we have

$$(x+y+1)(x-y)=r(p-q)$$

As before, we have $x+y=r-1$, so $x-y=p-q$, and

$$\begin{aligned}
& x=\frac{1}{2}(r+p-q-1) \\
& y=\frac{1}{2}(r+q-p-1)
\end{aligned}$$

Then,

$$\begin{aligned}
k=p r-x^{2}-x & =\frac{1}{4}\left(4 p r-(r+p-q-1)^{2}-2(r+p-q-1)\right) \\
& =\frac{1}{4}\left(4 p r-(r+p-q)^{2}+1\right) \\
& =\frac{1}{4}\left(2 p q+2 p r+2 q r-p^{2}-q^{2}-r^{2}+1\right)
\end{aligned}$$

which is symmetric in $p, q, r$, so

$$pq = z^{2}+z+k \quad \text { where } z=\frac{1}{2}(p+q-r-1)$$

and $\{p, q\}$ is special.

Now we settle the problem by induction on $|S|$, with $|S| \leqslant 3$ clear.

Suppose we have proven it for $|S|=n$ and consider $|S|=n+1$. Let $r$ be the largest prime in $S$; the claim tells us that in any valid cycle of primes:

- the neighbors of $r$ are uniquely determined, and
- removing $r$ from the cycle results in a smaller valid cycle.

It follows that there is at most one valid cycle, completing the inductive step.

*Comment.* The statement is not as inapplicable as it might seem. For example, for $k=41$, the following 385 primes form a valid cycle of primes:

53, 4357, 104173, 65921, 36383, 99527, 193789, 2089123, 1010357, 2465263, 319169, 15559, 3449, 2647, 1951, 152297, 542189, 119773, 91151, 66431, 222137, 1336799, 469069, 45613, 1047941, 656291, 355867, 146669, 874879, 2213327, 305119, 3336209, 1623467, 520963, 794201, 1124833, 28697, 15683, 42557, 6571, 39607, 1238833, 835421, 2653681, 5494387, 9357539, 511223, 1515317, 8868173, 114079681, 59334071, 22324807, 3051889, 5120939, 7722467, 266239, 693809 , 3931783, 1322317, 100469, 13913, 74419, 23977, 1361, 62983, 935021, 512657, 1394849, 216259, 45827, 31393, 100787, 1193989, 600979, 209543, 357661, 545141, 19681, 10691, 28867, 165089, 2118023, 6271891, 12626693, 21182429, 1100467, 413089, 772867, 1244423, 1827757, 55889, 1558873, 5110711, 1024427, 601759, 290869, 91757, 951109, 452033, 136471, 190031, 4423, 9239, 15809, 24133, 115811, 275911, 34211, 877, 6653, 88001, 46261, 317741, 121523, 232439, 379009, 17827, 2699, 15937, 497729, 335539, 205223, 106781, 1394413, 4140947, 8346383, 43984757, 14010721, 21133961, 729451, 4997297, 1908223, 278051, 529747, 40213, 768107, 456821, 1325351, 225961, 1501921, 562763, 75527, 5519, 9337, 14153, 499, 1399, 2753, 14401, 94583, 245107, 35171, 397093, 195907, 2505623, 34680911, 18542791, 7415917, 144797293, 455529251, 86675291, 252704911, 43385123, 109207907, 204884269, 330414209, 14926789, 1300289, 486769, 2723989, 907757, 1458871, 65063, 4561, 124427, 81343, 252887, 2980139, 1496779, 3779057, 519193, 47381, 135283, 268267, 446333, 669481, 22541, 54167, 99439, 158357, 6823, 32497, 1390709, 998029, 670343, 5180017, 13936673, 2123491, 4391941, 407651, 209953, 77249, 867653, 427117, 141079, 9539, 227, 1439, 18679, 9749, 25453, 3697, 42139, 122327, 712303, 244261, 20873, 52051, 589997, 4310569, 1711069, 291563, 3731527, 11045429, 129098443, 64620427, 162661963, 22233269, 37295047, 1936969, 5033449, 725537, 1353973, 6964457, 2176871, 97231, 7001, 11351, 55673, 16747, 169003, 1218571, 479957, 2779783, 949609, 4975787, 1577959, 2365007, 3310753, 79349, 23189, 107209, 688907, 252583, 30677, 523, 941, 25981, 205103, 85087, 1011233, 509659, 178259, 950479, 6262847, 2333693, 305497, 3199319, 9148267, 1527563, 466801, 17033, 9967, 323003, 4724099, 14278309, 2576557, 1075021, 6462593, 2266021, 63922471, 209814503, 42117791, 131659867, 270892249, 24845153, 12104557, 3896003, 219491, 135913, 406397, 72269, 191689, 2197697, 1091273, 2727311, 368227, 1911661, 601883, 892657, 28559, 4783, 60497, 31259, 80909, 457697, 153733, 11587, 1481, 26161, 15193, 7187, 2143, 21517, 10079, 207643, 1604381, 657661, 126227, 372313, 2176331, 748337, 64969, 844867, 2507291, 29317943, 14677801, 36952793, 69332267, 111816223, 5052241, 8479717, 441263, 3020431, 1152751, 13179611, 38280013, 6536771, 16319657, 91442699, 30501409, 49082027, 72061511, 2199433, 167597, 317963, 23869, 2927, 3833, 17327, 110879, 285517, 40543, 4861, 21683, 50527, 565319, 277829, 687917, 3846023, 25542677, 174261149, 66370753, 9565711, 1280791, 91393, 6011, 7283, 31859, 8677, 10193, 43987, 11831, 13591, 127843, 358229, 58067, 15473, 65839, 17477, 74099, 19603, 82847, 21851, 61.








# <lo-sample/> IMO_SHL.2022.N8

Prove that $5^n-3^n$ is not divisible by $2^n+65$ for any positive integer $n$.


<small>

* domain:NT
* questionType:Prove
* source:Belgium
* concepts:divisibility,integer-numbers

</small>



## Solution

Let $n$ be a positive integer, and let $m=2^{n}+65$. For the sake of 
contradiction, suppose that $m \mid 5^{n}-3^{n}$, so $5^{n} \equiv 3^{n} \pmod {m}$.

Notice that if $n$ is even, then $3 \mid m$, but $3 \nmid 5^{n}-3^{n}$, contradiction. 
So, from now on we assume that $n$ is odd, $n=2 k+1$. Obviously $n=1$ is not possible, 
so $n \geqslant 3$. Notice that $m$ is coprime to $2$, $3$ and $5$.

Let $m_{1}$ be the smallest positive multiple of $m$ that can be written in the
form of either $\left|5a^{2} - 3b^{2}\right|$ or $\left|a^{2}-15 b^{2}\right|$ 
with some integers $a$ and $b$.

Note that $5^{n}-3^{n}=5\left(5^{k}\right)^{2}-3\left(3^{k}\right)^{2}$ is a 
multiple of $m$, so the set of such multiples is non-empty, and therefore $m_{1}$ is well-defined.

**Part 1.** First we show that $m_{1} \leqslant 5 m$. Consider the numbers

$$5^{k+1} x+3^{k+1} y, \quad 0 \leqslant x, y \leqslant \sqrt{m}$$

There are $\lfloor\sqrt{m}\rfloor+1>\sqrt{m}$ choices for $x$ and $y$, 
so there are more than $m$ possible pairs $(x, y)$. Hence, two of these 
sums are congruent modulo $m$ : 
$5^{k+1} x_{1}+3^{k+1} y_{1} \equiv 5^{k+1} x_{2}+3^{k+1} y_{2}(\bmod m)$.

Now choose $a=x_{1}-x_{2}$ and $b=y_{1}-y_{2}$; at least one of 
$a, b$ is nonzero, and

$$5^{k+1} a+3^{k+1} b \equiv 0 \quad(\bmod m), \quad|a|,|b| \leqslant \sqrt{m}$$

From

$$0 \equiv\left(5^{k+1} a\right)^{2}-\left(3^{k+1} b\right)^{2}=5^{n+1} a^{2}-3^{n+1} b^{2} \equiv 5 \cdot 3^{n} a^{2}-3^{n+1} b^{2}=3^{n}\left(5 a^{2}-3 b^{2}\right) \pmod {m}$$

we can see that $\left|5 a^{2}-3 b^{2}\right|$ is a multiple of $m$. 
Since at least one of $a$ and $b$ is nonzero, $5 a^{2} \neq 3 b^{2}$. 
Hence, by the choice of $a, b$, we have 
$0<\left|5 a^{2}-3 b^{2}\right| \leqslant \max \left(5 a^{2}, 3 b^{2}\right) \leqslant 5 m$.
That shows that $m_{1} \leqslant 5 m$.

**Part 2.** Next, we show that $m_{1}$ cannot be divisible by $2$, $3$ and $5$. 
Since $m_{1}$ equals either $\left|5 a^{2}-3 b^{2}\right|$ or 
$\left|a^{2}-15 b^{2}\right|$ with some integers $a, b$, we have six cases to check. 
In all six cases, we will get a contradiction by presenting another 
multiple of $m$, smaller than $m_{1}$.

- If $5 \mid m_{1}$ and $m_{1}=\left|5 a^{2}-3 b^{2}\right|$, then $5 \mid b$ and 
  $\left|a^{2}-15\left(\frac{b}{5}\right)^{2}\right|=\frac{m_{1}}{5}<m_{1}$.
- If $5 \mid m_{1}$ and $m_{1}=\left|a^{2}-15 b^{2}\right|$, then $5 \mid a$ and 
  $\left|5\left(\frac{a}{5}\right)^{2}-3 b^{2}\right|=\frac{m_{1}}{5}<m_{1}$.
- If $3 \mid m_{1}$ and $m_{1}=\left|5 a^{2}-3 b^{2}\right|$, then $3 \mid a$ and 
  $\left|b^{2}-15\left(\frac{a}{3}\right)^{2}\right|=\frac{m_{1}}{3}<m_{1}$.
- If $3 \mid m_{1}$ and $m_{1}=\left|a^{2}-15 b^{2}\right|$, then $3 \mid a$ and 
  $\left|5 b^{2}-3\left(\frac{a}{3}\right)^{2}\right|=\frac{m_{1}}{3}<m_{1}$.
- If $2 \mid m_{1}$ and $m_{1}=\left|5 a^{2}-3 b^{2}\right|$, then 
  $\left|\left(\frac{5 a-3 b}{2}\right)^{2}-15\left(\frac{a-b}{2}\right)^{2}\right|=\frac{m_{1}}{2}<m_{1}$.
- If $2 \mid m_{1}$ and $m_{1}=\left|a^{2}-15 b^{2}\right|$, then 
  $\left|5\left(\frac{a-3 b}{2}\right)^{2}-3\left(\frac{a-5 b}{2}\right)^{2}\right|=\frac{m_{1}}{2}<m_{1}$.

(The last two expressions can be obtained from 
$(\sqrt{5} a+\sqrt{3} b)(\sqrt{5}-\sqrt{3})=(5 a-3 b)+\sqrt{15}(b-a)$ and $(a+\sqrt{15} b)(\sqrt{5}-\sqrt{3})=\sqrt{5}(a-3 b)+\sqrt{3}(5 b-a)$.)

In all six cases, we found that either $\frac{m_{1}}{2}, \frac{m_{1}}{3}$ or 
$\frac{m_{1}}{5}$ is of the form $\left|5 x^{2}-3 y^{2}\right|$ or 
$\left|x^{2}-15 y^{2}\right|$. Since $m$ is coprime to $2$, $3$ and $5$, 
the presented number is a multiple of $m$, but this contradicts the minimality of $m_{1}$.


**Part 3.** The last remaining case is $m_{1}=m$, so either 
$m=\left|5 a^{2}-3 b^{2}\right|$ or $m=\left|a^{2}-15 b^{2}\right|$. 
We will get a contradiction by considering the two sides modulo $3$, $4$ and $5$.

- $2^{n}+65=5 a^{2}-3 b^{2}$ is not possible, because 
  $2^{n}+65 \equiv 1(\bmod 3)$, but $5 a^{2}-3 b^{2} \not \equiv 1$ $(\bmod 3)$.
- $2^{n}+65=3 b^{2}-5 a^{2}$ is not possible, because 
  $2^{n}+65 \equiv 1(\bmod 4)$, but $3 b^{2}-5 a^{2} \not \equiv 1$ $(\bmod 4)$.
- $2^{n}+65=a^{2}-15 b^{2}$ is not possible, because 
  $2^{n}+65 \equiv \pm 2(\bmod 5)$, but $a^{2}-15 b^{2} \not \equiv \pm 2$ $(\bmod 5)$.
- $2^{n}+65=15 b^{2}-a^{2}$ is not possible, because
  $2^{n}+65 \equiv 1(\bmod 4)$, but $15 b^{2}-a^{2} \not \equiv 1$ $(\bmod 4)$.

We found a contradiction in all cases, that completes the solution.

**Comment 1.** Part I is a standard application of Thue's lemma:

*Lemma (Thue).* Suppose that $m>1$ and $c$ are integers, and $X, Y$ are 
positive integers such that $X \leqslant m<X Y$. Then there exist some 
integers $x, y$ with $|x|<X$ and $0<y<Y$, such that $x \equiv c y(\bmod m)$.

It is a well-known corollary that if $c, d$ are coprime to $m$, the congruence 
$c x^{2} \equiv d y^{2}(\bmod m)$ has a solution such that $x, y$ are coprime 
to $m$, and $X, Y$ are positive integers such that $X Y>m$, then 
$c x^{2} \equiv d y^{2}(\bmod m)$ has a solution such that at least one of 
$x, y$ is nonzero, $|x|<X$ and $|y|<Y$.

In the solution we applied this corollary with $c=5, d=3, X=Y=\lfloor\sqrt{m}\rfloor+1$.

**Comment 2.** In fact, we proved that a positive integer $m$ with 
$m \equiv 13$ or $37(\bmod 60)$ cannot divide any nonzero integer of the 
form $5 a^{2}-3 b^{2}$ or $a^{2}-15 b^{2}$ with coprime integers $a, b$. 
In other words, if $m \equiv 13$ or $37(\bmod 60)$, then 15 is not a 
quadratic residue modulo $m$. Using the tools of quadratic reciprocity, 
the solution can be significantly shortened.

Suppose that $a$ and $b$ are coprime. For every prime divisor $p>5$ of 
$5 a^{2}-3 b^{2}$ or $a^{2}-15 b^{2}$, we have

$$\begin{equation*}
1=\left(\frac{15}{p}\right)=\left(\frac{3}{p}\right)\left(\frac{5}{p}\right)=(-1)^{\frac{p-1}{2}}\left(\frac{p}{3}\right)\left(\frac{p}{5}\right) \tag{1}
\end{equation*}$$

where $\left(\frac{a}{p}\right)$ stands for the Legendre symbol. 
Considering the remainders of $p$ when divided by $4$, $3$ and $5$, $(1)$ leads to

$$p \equiv \pm 1, \pm 7, \pm 11 \text { or } \pm 17 \bmod 60$$

These remainders form a subgroup of the reduced remainders modulo $60$. 
Since $13$ and $37$ are not elements in this subgroup, the number $m=2^{n}+65$ 
cannot be a product of such primes.

Instead of handling the prime divisors of $m$ separately, we can use 
Jacobi symbols for further simplification, as shown in the next solution.


## Solution 

Suppose again that $5^{n} \equiv 3^{n} \pmod {m=2^{n}+65}$. 
Like in the first solution, we conclude that $n$ must be odd, and 
$n \geqslant 3$, so $8 \mid 2^{n}$.

Using Jacobi symbols, 

$$-1=\left(\frac{2^{n}+65}{5}\right)=\left(\frac{5}{2^{n}+65}\right)=\left(\frac{5^{n}}{2^{n}+65}\right)=\left(\frac{3^{n}}{2^{n}+65}\right)=\left(\frac{3}{2^{n}+65}\right)=\left(\frac{2^{n}+65}{3}\right)=1,$$

contradiction.


