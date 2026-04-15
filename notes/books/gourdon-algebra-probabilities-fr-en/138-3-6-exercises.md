#### 3.6. Exercises

*Français : 3.6. Exercices*

EXERCICE 1. Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires à valeurs dans \( {\mathbb{N}}^{ * } \) , indépen-dantes et identiquement distribuées. On note \( {C}_{n} = \operatorname{Card}\left\{ {{X}_{1},\ldots ,{X}_{n}}\right\} \) .

> EXERCISE 1. Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent and identically distributed random variables taking values in \( {\mathbb{N}}^{ * } \). Let \( {C}_{n} = \operatorname{Card}\left\{ {{X}_{1},\ldots ,{X}_{n}}\right\} \).

1/ Montrer que \( E\left( {C}_{n}\right) = o\left( n\right) \) .

> 1/ Show that \( E\left( {C}_{n}\right) = o\left( n\right) \).

2/ On suppose que les \( {X}_{n} \) admettent une espérance. Montrer que \( E\left( {C}_{n}\right) = o\left( \sqrt{n}\right) \) .

> 2/ Assume that the \( {X}_{n} \) have an expected value. Show that \( E\left( {C}_{n}\right) = o\left( \sqrt{n}\right) \).

Solution. 1 / Lorsque \( n \) est grand, les \( {X}_{i} \) ont tendances à rester "petits" car la probabilité que \( {X}_{i} \) soit grand est faible, donc beaucoup d’entre eux sont égaux, et \( {C}_{n} \) est petit. Pour quantifier ceci, on fixe \( a > 0 \) , et on partitionne les \( {X}_{k} \) entre ceux \( \leq a \) et les autres. On obtient

> Solution. 1/ When \( n \) is large, the \( {X}_{i} \) tend to remain "small" because the probability that \( {X}_{i} \) is large is low, so many of them are equal, and \( {C}_{n} \) is small. To quantify this, we fix \( a > 0 \) and partition the \( {X}_{k} \) into those \( \leq a \) and the others. We obtain

\[
{C}_{n} = \operatorname{Card}\left\{  {{X}_{k} \mid  1 \leq  k \leq  n,{X}_{k} \leq  a}\right\}   + \operatorname{Card}\left\{  {{X}_{k} \mid  1 \leq  k \leq  n,{X}_{k} > a}\right\}
\]

\[
\leq  a + \operatorname{Card}\left\{  {k \leq  n \mid  {X}_{k} > a}\right\}   = a + \mathop{\sum }\limits_{{k = 1}}^{n}{\mathbf{1}}_{\left\{  {X}_{k} > a\right\}  },
\]

(où \( {\mathbf{1}}_{A} \) désigne la fonction indicatrice de \( A \) , définie par \( {\mathbf{1}}_{A}\left( x\right) = 1 \) si \( x \in A, = 0 \) sinon) donc

> (where \( {\mathbf{1}}_{A} \) denotes the indicator function of \( A \), defined by \( {\mathbf{1}}_{A}\left( x\right) = 1 \) if \( x \in A, = 0 \) otherwise) therefore

\[
E\left( {C}_{n}\right)  \leq  a + \mathop{\sum }\limits_{{k = 1}}^{n}P\left( {{X}_{k} > a}\right)  = a + {nP}\left( {{X}_{1} > a}\right) .
\]

\( \left( *\right) \)

> En choisissant \( a = \sqrt{n} \) , on en déduit en particulier \( E\left( {C}_{n}\right) \leq \sqrt{n} + {nP}\left( {{X}_{1} > \sqrt{n}}\right) \) , et comme \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{1} > \sqrt{n}}\right) = 0 \) (et \( E\left( {C}_{n}\right) \geq 0 \) ), ceci entraîne bien \( E\left( {C}_{n}\right) = o\left( n\right) \) .

By choosing \( a = \sqrt{n} \), we deduce in particular \( E\left( {C}_{n}\right) \leq \sqrt{n} + {nP}\left( {{X}_{1} > \sqrt{n}}\right) \), and since \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{1} > \sqrt{n}}\right) = 0 \) (and \( E\left( {C}_{n}\right) \geq 0 \)), this indeed implies \( E\left( {C}_{n}\right) = o\left( n\right) \).

> 2 / On va réutiliser (*), en choisissant correctement \( a \) . L’inégalité de Markov entraîne \( P\left( {{X}_{1} > }\right. \; a) \leq E\left( {X}_{1}\right) /a \) , ce qui n’est pas suffisant pour conclure (on en déduit \( E\left( {C}_{n}\right) = O\left( \sqrt{n}\right) \) mais on n’a pas le petit \( o \) ). Une amélioration de cette borne lorsque \( a \) est grand s’obtient en écrivant

2 / We will reuse (*), by choosing \( a \) correctly. Markov's inequality leads to \( P\left( {{X}_{1} > }\right. \; a) \leq E\left( {X}_{1}\right) /a \) , which is not sufficient to conclude (we deduce \( E\left( {C}_{n}\right) = O\left( \sqrt{n}\right) \) but we do not have the small \( o \) ). An improvement of this bound when \( a \) is large is obtained by writing

\[
{aP}\left( {{X}_{1} > a}\right)  = \mathop{\sum }\limits_{{k > a}}{aP}\left( {{X}_{1} = k}\right)  \leq  \mathop{\sum }\limits_{{k > a}}{kP}\left( {{X}_{1} = k}\right)  = o\left( 1\right) ,
\]

car l’existence de l’espérance de \( {X}_{1} \) entraîne la convergence de la série \( \mathop{\sum }\limits_{k}{kP}\left( {{X}_{1} = k}\right) \) . On en déduit \( {aP}\left( {{X}_{1} \geq a}\right) = o\left( 1\right) \) . Donnons maintenant \( \varepsilon > 0 \) . Choisissons \( a = \varepsilon \sqrt{n} \) . Comme \( \varepsilon \sqrt{n} \rightarrow + \infty \) , il existe \( N \in \mathbb{N} \) tel que \( \varepsilon \sqrt{n}P\left( {{X}_{1} > \varepsilon \sqrt{n}}\right) \leq {\varepsilon }^{2} \) , donc

> because the existence of the expectation of \( {X}_{1} \) entails the convergence of the series \( \mathop{\sum }\limits_{k}{kP}\left( {{X}_{1} = k}\right) \) . We deduce \( {aP}\left( {{X}_{1} \geq a}\right) = o\left( 1\right) \) . Let us now give \( \varepsilon > 0 \) . Let us choose \( a = \varepsilon \sqrt{n} \) . Since \( \varepsilon \sqrt{n} \rightarrow + \infty \) , there exists \( N \in \mathbb{N} \) such that \( \varepsilon \sqrt{n}P\left( {{X}_{1} > \varepsilon \sqrt{n}}\right) \leq {\varepsilon }^{2} \) , therefore

\[
\forall n \geq  N,\;E\left( {C}_{n}\right)  \leq  \varepsilon \sqrt{n} + {nP}\left( {{X}_{1} > \varepsilon \sqrt{n}}\right)  \leq  \varepsilon \sqrt{n} + n\frac{{\varepsilon }^{2}}{\varepsilon \sqrt{n}} = {2\varepsilon }\sqrt{n}.
\]

EXERCICE 2. Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, admettant un moment d’ordre 2. On suppose que les \( {X}_{n} \) ont la même espérance \( \mu = E\left( {X}_{1}\right) \) et qu’il existe \( \sigma > 0 \) tel que \( V\left( {X}_{n}\right) \leq {\sigma }^{2} \) pour tout \( n \in {\mathbb{N}}^{ * } \) . On pose \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) .

> EXERCISE 2. Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of real discrete random variables, admitting a second-order moment. We assume that the \( {X}_{n} \) have the same expectation \( \mu = E\left( {X}_{1}\right) \) and that there exists \( \sigma > 0 \) such that \( V\left( {X}_{n}\right) \leq {\sigma }^{2} \) for all \( n \in {\mathbb{N}}^{ * } \) . Let \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) .

1 / On suppose que pour tout \( \left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) tels que \( i + 1 < j \) , les variables aléatoires \( {X}_{i} \) et \( {X}_{j} \) sont indépendantes. Montrer que \( \left( {{S}_{n}/n}\right) \) converge vers \( \mu \) en probabilité, c’est-à-dire

> 1 / We assume that for all \( \left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) such that \( i + 1 < j \) , the random variables \( {X}_{i} \) and \( {X}_{j} \) are independent. Show that \( \left( {{S}_{n}/n}\right) \) converges to \( \mu \) in probability, that is to say

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {\left| {{S}_{n}/n - \mu }\right|  > \varepsilon }\right)  = 0.
\]

2/On suppose que pour tout \( \left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) tels que \( i < j,\operatorname{Cov}\left( {{X}_{i},{X}_{j}}\right) \leq {\sigma }^{2}/\left( {j - i}\right) \) . Montrer que \( \left( {{S}_{n}/n}\right) \) converge vers \( \mu \) en probabilité.

> 2/ We assume that for all \( \left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) such that \( i < j,\operatorname{Cov}\left( {{X}_{i},{X}_{j}}\right) \leq {\sigma }^{2}/\left( {j - i}\right) \) . Show that \( \left( {{S}_{n}/n}\right) \) converges to \( \mu \) in probability.

Solution. 1 / On procède comme dans la démonstration de la loi faible des grands nombres (voir la preuve du théorème 1 page 345). On majore la variance de \( {S}_{n} \) , en écrivant

> Solution. 1 / We proceed as in the proof of the weak law of large numbers (see the proof of theorem 1 on page 345). We bound the variance of \( {S}_{n} \) from above, by writing

\[
V\left( {S}_{n}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}V\left( {X}_{i}\right)  + 2\mathop{\sum }\limits_{{i < j}}\operatorname{Cov}\left( {{X}_{i},{X}_{j}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}V\left( {X}_{i}\right)  + 2\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\operatorname{Cov}\left( {{X}_{i},{X}_{i + 1}}\right)
\]

\[
\leq  n{\sigma }^{2} + 2\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}V{\left( {X}_{i}\right) }^{1/2}V{\left( {X}_{i + 1}\right) }^{1/2} \leq  \left( {{3n} - 2}\right) {\sigma }^{2} \leq  {3n}{\sigma }^{2}.
\]

En appliquant l'inégalité de Bienaymé-Tchébycheff à \( {S}_{n} \) on en déduit, compte tenu du fait que \( E\left( {{S}_{n}/n}\right) = \mu , \)

> By applying the Bienaymé-Chebyshev inequality to \( {S}_{n} \) we deduce, taking into account the fact that \( E\left( {{S}_{n}/n}\right) = \mu , \)

\[
P\left( {\left| {{S}_{n}/n - \mu }\right|  \geq  \varepsilon }\right)  \leq  \frac{V\left( {{S}_{n}/n}\right) }{{\varepsilon }^{2}} = \frac{V\left( {S}_{n}\right) /{n}^{2}}{{\varepsilon }^{2}} \leq  \frac{3{\sigma }^{2}}{n{\varepsilon }^{2}},
\]

d'où le résultat.

> hence the result.

2 / On utilise la même approche. Une borne supérieure sur \( V\left( {S}_{n}\right) \) est fournie par

> 2 / We use the same approach. An upper bound on \( V\left( {S}_{n}\right) \) is provided by

\[
V\left( {S}_{n}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}V\left( {X}_{i}\right)  + 2\mathop{\sum }\limits_{{1 \leq  i < j \leq  n}}\operatorname{Cov}\left( {{X}_{i},{X}_{j}}\right)  \leq  n{\sigma }^{2} + 2\mathop{\sum }\limits_{{1 \leq  i < j \leq  n}}\frac{{\sigma }^{2}}{j - i}
\]

\[
= n{\sigma }^{2} + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\left( {\mathop{\sum }\limits_{\substack{{1 \leq  i < j \leq  n} \\  {j - i = k} }}\frac{{\sigma }^{2}}{j - i}}\right)  = n{\sigma }^{2} + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\left( {n - k}\right) \frac{{\sigma }^{2}}{k} = {\sigma }^{2} + n{\sigma }^{2}{H}_{n - 1},
\]

où intervient le nombre harmonique \( {H}_{n} = 1 + \frac{1}{2} + \cdots + \frac{1}{n} \) . On a \( {H}_{n} \leq 1 + \mathop{\sum }\limits_{{k = 2}}^{n}{\int }_{k - 1}^{k}{dt}/t = \; 1 + {\int }_{1}^{n}{dt}/t = 1 + \log n \) , et le résultat souhaité s’obtient à partir de l’inégalité de Bienaymé Tchébycheff appliquée à \( {S}_{n} \) , en écrivant

> where the harmonic number \( {H}_{n} = 1 + \frac{1}{2} + \cdots + \frac{1}{n} \) appears. We have \( {H}_{n} \leq 1 + \mathop{\sum }\limits_{{k = 2}}^{n}{\int }_{k - 1}^{k}{dt}/t = \; 1 + {\int }_{1}^{n}{dt}/t = 1 + \log n \) , and the desired result is obtained from the Bienaymé-Chebyshev inequality applied to \( {S}_{n} \) , by writing

\[
P\left( {\left| {{S}_{n}/n - \mu }\right|  \geq  \varepsilon }\right)  \leq  \frac{V\left( {S}_{n}\right) /{n}^{2}}{{\varepsilon }^{2}} \leq  {\sigma }^{2}\frac{1/n + {H}_{n}}{n{\varepsilon }^{2}} \leq  \frac{{\sigma }^{2}}{{\varepsilon }^{2}}\frac{2 + \log n}{n}.
\]

EXERCICE 3. Montrer qu'il est impossible de piper deux dés pour que la somme de leurs points suive la loi uniforme sur \( \{ 2,\ldots ,{12}\} \) .

> EXERCISE 3. Show that it is impossible to load two dice so that the sum of their points follows the uniform distribution on \( \{ 2,\ldots ,{12}\} \) .

Solution. Nous allons utiliser les séries génératrices \( {\varphi }_{X} \) et \( {\varphi }_{Y} \) des variables aléatoires \( X \) et \( Y \) des points de chaque dé, qui ici sont des polynômes de degré \( \leq 6 \) . Comme \( P\left( {X = 0}\right) = P\left( {Y = 0}\right) = 0 \) , on peut écrire \( {\varphi }_{X}\left( z\right) = z{\psi }_{X}\left( z\right) \) et \( {\varphi }_{Y}\left( z\right) = z{\psi }_{Y}\left( z\right) \) où \( {\psi }_{X}\left( z\right) \) et \( {\psi }_{Y}\left( z\right) \) sont des polynômes de degré \( \leq 5 \) . Raisonnons par l’absurde et supposons que les deux dés soient pipés de sorte que la somme des points des deux dés suive la loi uniforme sur \( \{ 2,\ldots ,{12}\} \) . On aurait alors

> Solution. We will use the generating functions \( {\varphi }_{X} \) and \( {\varphi }_{Y} \) of the random variables \( X \) and \( Y \) for the points of each die, which here are polynomials of degree \( \leq 6 \) . Since \( P\left( {X = 0}\right) = P\left( {Y = 0}\right) = 0 \) , we can write \( {\varphi }_{X}\left( z\right) = z{\psi }_{X}\left( z\right) \) and \( {\varphi }_{Y}\left( z\right) = z{\psi }_{Y}\left( z\right) \) where \( {\psi }_{X}\left( z\right) \) and \( {\psi }_{Y}\left( z\right) \) are polynomials of degree \( \leq 5 \) . Let us reason by contradiction and assume that the two dice are loaded so that the sum of the points of the two dice follows the uniform distribution on \( \{ 2,\ldots ,{12}\} \) . We would then have

\[
{\varphi }_{X}\left( z\right) {\varphi }_{Y}\left( z\right)  = {\varphi }_{X + Y}\left( z\right)  = \frac{{z}^{2} + {z}^{3} + \cdots  + {z}^{12}}{11}\;\text{ donc }\;{\psi }_{X}\left( z\right) {\psi }_{Y}\left( z\right)  = \frac{1 - {z}^{11}}{{11}\left( {1 - z}\right) }.
\]

(*)

> Comme \( {\psi }_{X} \) et \( {\psi }_{Y} \) ont un degré \( \leq 5 \) , on en déduit deg \( {\psi }_{X} = \deg {\psi }_{Y} = 5 \) . Par ailleurs, le terme de droite de (*) s’annule lorsque \( z = {z}_{k} = \exp \left( {{2ik\pi }/{11}}\right) \) pour \( 1 \leq k \leq {10} \) . Ces dix valeurs distinctes \( {z}_{k} \) forment donc l’ensemble des racines de de \( {\psi }_{X} \) et \( {\psi }_{Y} \) , et aucune n’est réelle. Or \( {\psi }_{X} \) et \( {\psi }_{Y} \) sont des polynômes à coefficients réels de degré impair, donc ils ont chacun au moins une racine réelle, ce qui est absurde.

Since \( {\psi }_{X} \) and \( {\psi }_{Y} \) have degree \( \leq 5 \) , we deduce deg \( {\psi }_{X} = \deg {\psi }_{Y} = 5 \) . Furthermore, the right-hand side of (*) vanishes when \( z = {z}_{k} = \exp \left( {{2ik\pi }/{11}}\right) \) for \( 1 \leq k \leq {10} \) . These ten distinct values \( {z}_{k} \) therefore form the set of roots of \( {\psi }_{X} \) and \( {\psi }_{Y} \) , and none are real. However, \( {\psi }_{X} \) and \( {\psi }_{Y} \) are polynomials with real coefficients of odd degree, so they each have at least one real root, which is absurd.

> EXERCICE 4 (CONVERGENCE DOMINÉE \( {\mathcal{L}}^{2} \) ). Soit \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé. On note \( {\mathcal{L}}^{1}\left( \Omega \right) \) (resp. \( {\mathcal{L}}^{2}\left( \Omega \right) \) ) l’espace vectoriel des variables aléatoires discrètes réelles sur \( \Omega \)

EXERCISE 4 (DOMINATED CONVERGENCE \( {\mathcal{L}}^{2} \) ). Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space. We denote by \( {\mathcal{L}}^{1}\left( \Omega \right) \) (resp. \( {\mathcal{L}}^{2}\left( \Omega \right) \) ) the vector space of real discrete random variables on \( \Omega \)

> qui admettent une espérance (resp. qui admettent un moment d’ordre 2). Soit \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( {\mathcal{L}}^{1}\left( \Omega \right) \) . On suppose que

that admit an expectation (resp. that admit a second-order moment). Let \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of \( {\mathcal{L}}^{1}\left( \Omega \right) \) . We assume that

> (i) \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) converge en probabilité vers une variable aléatoire discrète réelle \( X \) sur \( \Omega \) , c'est-à-dire

(i) \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) converges in probability to a real discrete random variable \( X \) on \( \Omega \) , that is to say

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {\left| {{X}_{n} - X}\right|  \geq  \varepsilon }\right)  = 0.
\]

(ii) Il existe \( Y \in {\mathcal{L}}^{2}\left( \Omega \right) \) , telle que \( \left| X\right| \leq Y \) et \( \forall n \in \mathbb{N},\left| {X}_{n}\right| \leq Y \) . Démontrer que \( X \in {\mathcal{L}}^{1}\left( \Omega \right) \) et que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}E\left( {X}_{n}\right) = E\left( X\right) \) .

> (ii) There exists \( Y \in {\mathcal{L}}^{2}\left( \Omega \right) \) such that \( \left| X\right| \leq Y \) and \( \forall n \in \mathbb{N},\left| {X}_{n}\right| \leq Y \) . Prove that \( X \in {\mathcal{L}}^{1}\left( \Omega \right) \) and that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}E\left( {X}_{n}\right) = E\left( X\right) \) .

Solution. Remarquons déja qu’on a bien \( X \in {\mathcal{L}}^{1}\left( \Omega \right) \) , car l’inégalité \( \left| X\right| \leq Y \) avec \( Y \in {\mathcal{L}}^{2}\left( \Omega \right) \) , entraîne \( \left| X\right| \leq 1 + {Y}^{2} \) , donc \( X \) admet une espérance.

> Solution. Note first that we indeed have \( X \in {\mathcal{L}}^{1}\left( \Omega \right) \) , because the inequality \( \left| X\right| \leq Y \) with \( Y \in {\mathcal{L}}^{2}\left( \Omega \right) \) implies \( \left| X\right| \leq 1 + {Y}^{2} \) , so \( X \) has an expectation.

Montrons maintenant la limite recherchée. Soit \( \varepsilon > 0 \) . Pour tout \( n \in \mathbb{N} \) on note \( {A}_{n} = \; \left\{ {\left| {X - {X}_{n}}\right| \geq \varepsilon }\right\} \) et \( {\mathbf{1}}_{{A}_{n}} \) la fonction indicatrice de \( {A}_{n} \) (définie par \( {\mathbf{1}}_{{A}_{n}}\left( x\right) = 1 \) si \( x \in {A}_{n}, = 0 \) sinon). On a \( {\mathbf{1}}_{{A}_{n}} + {\mathbf{1}}_{{\bar{A}}_{n}} = 1 \) donc

> Let us now show the required limit. Let \( \varepsilon > 0 \) . For any \( n \in \mathbb{N} \) , let \( {A}_{n} = \; \left\{ {\left| {X - {X}_{n}}\right| \geq \varepsilon }\right\} \) and \( {\mathbf{1}}_{{A}_{n}} \) be the indicator function of \( {A}_{n} \) (defined by \( {\mathbf{1}}_{{A}_{n}}\left( x\right) = 1 \) if \( x \in {A}_{n}, = 0 \) , otherwise). We have \( {\mathbf{1}}_{{A}_{n}} + {\mathbf{1}}_{{\bar{A}}_{n}} = 1 \) , therefore

\[
E\left( \left| {{X}_{n} - X}\right| \right)  = E\left( {{\mathbf{1}}_{{A}_{n}}\left| {{X}_{n} - X}\right| }\right)  + E\left( {{\mathbf{1}}_{{\bar{A}}_{n}}\left| {{X}_{n} - X}\right| }\right) .
\]

(*)

> Lorsque \( x \in {\bar{A}}_{n} \) on a \( \left| {{X}_{n} - X}\right| \left( x\right) \leq \varepsilon \) donc \( {\mathbf{1}}_{{\bar{A}}_{n}}\left| {{X}_{n} - X}\right| \leq \varepsilon \) , ce qui entraîne \( E\left( {{\mathbf{1}}_{{\bar{A}}_{n}}\left| {{X}_{n} - X}\right| }\right) \leq \varepsilon \) . Quant au premier terme de la somme de (*), on a

When \( x \in {\bar{A}}_{n} \) , we have \( \left| {{X}_{n} - X}\right| \left( x\right) \leq \varepsilon \) , so \( {\mathbf{1}}_{{\bar{A}}_{n}}\left| {{X}_{n} - X}\right| \leq \varepsilon \) , which implies \( E\left( {{\mathbf{1}}_{{\bar{A}}_{n}}\left| {{X}_{n} - X}\right| }\right) \leq \varepsilon \) . As for the first term of the sum in (*), we have

\[
E\left( {{\mathbf{1}}_{{A}_{n}}\left| {{X}_{n} - X}\right| }\right)  \leq  {2E}\left( {{\mathbf{1}}_{{A}_{n}}Y}\right)  \leq  {2E}{\left( {\mathbf{1}}_{{A}_{n}}\right) }^{1/2}E{\left( {Y}^{2}\right) }^{1/2}.
\]

Comme \( E\left( {\mathbf{1}}_{{A}_{n}}\right) = P\left( {A}_{n}\right) \) l’hypothèse (i) assure l’existence de \( N \in \mathbb{N} \) tel que \( \forall n \geq N, E\left( {\mathbf{1}}_{{A}_{n}}\right) \leq \; {\varepsilon }^{2} \) . Ainsi,(*) entraîne

> Since \( E\left( {\mathbf{1}}_{{A}_{n}}\right) = P\left( {A}_{n}\right) \) , hypothesis (i) ensures the existence of \( N \in \mathbb{N} \) such that \( \forall n \geq N, E\left( {\mathbf{1}}_{{A}_{n}}\right) \leq \; {\varepsilon }^{2} \) . Thus, (*) implies

\[
\forall n \geq  N,\;\left| {E\left( {X}_{n}\right)  - E\left( X\right) }\right|  \leq  E\left( \left| {{X}_{n} - X}\right| \right)  \leq  \varepsilon  + {2\varepsilon E}{\left( {Y}^{2}\right) }^{1/2}.
\]

On en déduit \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}E\left( {X}_{n}\right) = E\left( X\right) \) .

> We deduce from this \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}E\left( {X}_{n}\right) = E\left( X\right) \) .

EXERCICE 5. Soit \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé tel qu’il existe une suite de variables aléatoires discrètes réelles indépendantes \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) , suivant chacune une loi non triviale, c’est-à-dire que pour tout \( n \in {\mathbb{N}}^{ * } \) et pour tout \( x \in \mathbb{R}, P\left( {{X}_{n} = x}\right) < 1 \) .

> EXERCISE 5. Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space such that there exists a sequence of independent real discrete random variables \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) , each following a non-trivial distribution, that is to say that for all \( n \in {\mathbb{N}}^{ * } \) and for all \( x \in \mathbb{R}, P\left( {{X}_{n} = x}\right) < 1 \) .

1/ Si les \( {X}_{n} \) sont identiquement distribuées, montrer que \( \Omega \) est infini non dénombrable. 2/ Montrer que le résultat précédent est faux si on ne suppose pas les \( {X}_{n} \) non identique-ment distribuées (on pourra s'inspirer de l'exercice 7 page 332).

> 1/ If the \( {X}_{n} \) are identically distributed, show that \( \Omega \) is uncountable. 2/ Show that the previous result is false if we do not assume the \( {X}_{n} \) are identically distributed (one may draw inspiration from exercise 7 on page 332).

Solution. 1/ Comme \( {X}_{1} \) est une loi discrète, il existe \( x \in {X}_{1}\left( \Omega \right) \) tel que \( p = P\left( {{X}_{1} = x}\right) > 0 \) . D’après les hypothèses, \( p < 1 \) . Pour tout \( y \in {X}_{1}\left( \Omega \right) , y \neq x, P\left( {{X}_{1} = y}\right) \leq 1 - P\left( {{X}_{1} = x}\right) = 1 - p \) . En notant \( q = \max \{ p,1 - p\} \) , on a donc

> Solution. 1/ Since \( {X}_{1} \) is a discrete distribution, there exists \( x \in {X}_{1}\left( \Omega \right) \) such that \( p = P\left( {{X}_{1} = x}\right) > 0 \) . According to the hypotheses, \( p < 1 \) . For all \( y \in {X}_{1}\left( \Omega \right) , y \neq x, P\left( {{X}_{1} = y}\right) \leq 1 - P\left( {{X}_{1} = x}\right) = 1 - p \) . By denoting \( q = \max \{ p,1 - p\} \) , we therefore have

\[
0 < q < 1\;\text{ et }\;\forall t \in  {X}_{1}\left( \Omega \right) , P\left( {{X}_{1} = t}\right)  \leq  q.
\]

On en déduit, pour tout \( \omega \in \Omega \) , les \( {X}_{n} \) étant indépendantes et identiquement distribuées,

> We deduce from this, for all \( \omega \in \Omega \) , the \( {X}_{n} \) being independent and identically distributed,

\[
\forall n \in  {\mathbb{N}}^{ * },\;P\left( {\{ \omega \} }\right)  \leq  P\left( {{X}_{1} = {X}_{1}\left( \omega \right) ,\ldots ,{X}_{n} = {X}_{n}\left( \omega \right) }\right)  = \mathop{\prod }\limits_{{k = 1}}^{n}P\left( {{X}_{k} = {X}_{k}\left( \omega \right) }\right)  \leq  {q}^{n}.
\]

Comme \( q < 1 \) on en déduit que forcément, \( P\left( {\{ \omega \} }\right) = 0 \) . Si \( \Omega \) était fini ou dénombrable, on aurait \( P\left( \Omega \right) = \mathop{\sum }\limits_{{\omega \in \Omega }}P\left( {\{ \omega \} }\right) = 0 \) , ce qui est absurde. Donc \( \Omega \) est infini non dénombrable.

> Since \( q < 1 \) we deduce that necessarily, \( P\left( {\{ \omega \} }\right) = 0 \) . If \( \Omega \) were finite or countable, we would have \( P\left( \Omega \right) = \mathop{\sum }\limits_{{\omega \in \Omega }}P\left( {\{ \omega \} }\right) = 0 \) , which is absurd. Therefore \( \Omega \) is uncountable.

2/ En procédant comme dans la solution de 1/, on montre facilement que même si les \( {X}_{n} \) ne sont pas identifiquement distribuées, sous l’hypothèse plus générale que \( \forall x \in \mathbb{R},\forall n \in {\mathbb{N}}^{ * } \) , \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}P\left( {{X}_{n} = x}\right) = 0 \) alors \( \Omega \) est forcément infini non dénombrable. Pour trouver un contre-exemple, on doit donc avoir \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}P\left( {{X}_{n} = x}\right) > 0 \) pour au moins une valeur de \( x \) .

> 2/ By proceeding as in the solution to 1/, it is easy to show that even if the \( {X}_{n} \) are not identically distributed, under the more general hypothesis that \( \forall x \in \mathbb{R},\forall n \in {\mathbb{N}}^{ * } \) , \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}P\left( {{X}_{n} = x}\right) = 0 \) then \( \Omega \) is necessarily uncountable. To find a counterexample, we must therefore have \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}P\left( {{X}_{n} = x}\right) > 0 \) for at least one value of \( x \) .

Un tel contre-exemple est fourni en choisissant \( \Omega = {\mathbb{N}}^{ * } \) , muni de la loi zéta

> Such a counterexample is provided by choosing \( \Omega = {\mathbb{N}}^{ * } \) , equipped with the zeta distribution

\[
P\left( {\{ n\} }\right)  = \frac{1}{\zeta \left( 2\right) }\frac{1}{{n}^{2}}
\]

(on pourrait choisir \( P\left( {\{ n\} }\right) = \zeta {\left( s\right) }^{-1}/{n}^{s} \) pour n’importe quel \( s > 1 \) ), puis en choisissant pour tout \( n \) la variable aléatoire \( {X}_{n} \) définie sur \( {\mathbb{N}}^{ * } \) par : \( {X}_{n}\left( k\right) = 1 \) si \( k > 1 \) est divisible par le \( n \) -ième nombre premier \( {p}_{n},{X}_{n}\left( k\right) = 0 \) sinon.

> (one could choose \( P\left( {\{ n\} }\right) = \zeta {\left( s\right) }^{-1}/{n}^{s} \) for any \( s > 1 \) ), then by choosing for every \( n \) the random variable \( {X}_{n} \) defined on \( {\mathbb{N}}^{ * } \) by: \( {X}_{n}\left( k\right) = 1 \) if \( k > 1 \) is divisible by the \( n \) -th prime number \( {p}_{n},{X}_{n}\left( k\right) = 0 \) otherwise.

Montrons que les variables aléatoires \( {X}_{n} \) sont bien indépendantes. On note \( {A}_{q} = q{\mathbb{N}}^{ * } \) pour \( q \in {\mathbb{N}}^{ * } \) . On a \( \left\{ {{X}_{n} = 1}\right\} = {A}_{{p}_{n}} \) et \( \left\{ {{X}_{n} = 0}\right\} = {A}_{{p}_{n}}^{C} \) . Comme on l’a vu dans l’exercice 7 page 332, les \( {\left( {A}_{{p}_{n}}\right) }_{n \in {\mathbb{N}}^{ * }} \) sont indépendants. D’après la proposition 8 page 324, pour toute suite \( \left( {\varepsilon }_{n}\right) \) d’éléments de \( \{ 0,1\} \) , les événéments \( {\left( P\left( {X}_{n} = {\varepsilon }_{n}\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) sont indépendants. On en déduit avec la proposition 2 page 336 que les \( {X}_{n} \) sont indépendants. On a donc construit un espace probabilisé dénombrable et une suite de variables aléatoires indépendantes et non triviales sur cet espace.

> Let us show that the random variables \( {X}_{n} \) are indeed independent. We denote \( {A}_{q} = q{\mathbb{N}}^{ * } \) by \( q \in {\mathbb{N}}^{ * } \) . We have \( \left\{ {{X}_{n} = 1}\right\} = {A}_{{p}_{n}} \) and \( \left\{ {{X}_{n} = 0}\right\} = {A}_{{p}_{n}}^{C} \) . As seen in exercise 7 on page 332, the \( {\left( {A}_{{p}_{n}}\right) }_{n \in {\mathbb{N}}^{ * }} \) are independent. According to proposition 8 on page 324, for any sequence \( \left( {\varepsilon }_{n}\right) \) of elements of \( \{ 0,1\} \) , the events \( {\left( P\left( {X}_{n} = {\varepsilon }_{n}\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) are independent. We deduce from this with proposition 2 on page 336 that the \( {X}_{n} \) are independent. We have thus constructed a countable probability space and a sequence of independent and non-trivial random variables on this space.

EXERCICE 6. Soient \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires à valeurs dans \( \mathbb{N} \) , ave les \( {X}_{n} \) mutuellement indépendantes et identiquement distribuées. On note \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) . On suppose que, presque surement, \( {\left( {S}_{n}/n\right) }_{n \in {\mathbb{N}}^{ * }} \) converge. Montrer que les \( {X}_{n} \) admettent une espérance. (Indication : raisonner par l’absurde en supposant \( E\left( {X}_{1}\right) = + \infty \) , montrer que pour tout \( K \in {\mathbb{N}}^{ * } \) , on a \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} \geq {Kn}}\right) = + \infty \) , puis que presque surement, \( \left. {\lim \sup {X}_{n}/n = + \infty }\right) \) .

> EXERCISE 6. Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of random variables taking values in \( \mathbb{N} \) , with the \( {X}_{n} \) being mutually independent and identically distributed. We denote \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) . Suppose that, almost surely, \( {\left( {S}_{n}/n\right) }_{n \in {\mathbb{N}}^{ * }} \) converges. Show that the \( {X}_{n} \) admit an expectation. (Hint: reason by contradiction by assuming \( E\left( {X}_{1}\right) = + \infty \) , show that for all \( K \in {\mathbb{N}}^{ * } \) , we have \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} \geq {Kn}}\right) = + \infty \) , then that almost surely, \( \left. {\lim \sup {X}_{n}/n = + \infty }\right) \) .

Solution. On suit l’indication en supposant que \( {X}_{1} \) n’admet pas d’espérance, ce qui implique que la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{X}_{1} > n}\right) \) diverge (voir la proposition 7 page 338). Or pour \( K \in {\mathbb{N}}^{ * } \) , on a

> Solution. We follow the hint by assuming that \( {X}_{1} \) does not admit an expectation, which implies that the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{X}_{1} > n}\right) \) diverges (see proposition 7 on page 338). However, for \( K \in {\mathbb{N}}^{ * } \) , we have

\[
\mathop{\sum }\limits_{{j = {Kn}}}^{{K\left( {n + 1}\right)  - 1}}P\left( {{X}_{1} > j}\right)  \leq  \mathop{\sum }\limits_{{j = {Kn}}}^{{K\left( {n + 1}\right)  - 1}}P\left( {{X}_{1} > {Kn}}\right)  = {KP}\left( {{X}_{1} > {Kn}}\right)  = {KP}\left( {{X}_{n} > {Kn}}\right) .
\]

Comme la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{X}_{1} > n}\right) \) diverge, on en déduit que \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} > {Kn}}\right) \) diverge. Les évé- néments \( {\left\{ {X}_{n} > Kn\right\} }_{n \in {\mathbb{N}}^{ * }} \) étant indépendants, l’assertion (ii) du lemme de Borel-Cantelli (voir le théorème 1 page 326) permet de déduire que l’événement \( {A}_{K} = { \cap }_{p \in \mathbb{N}}{ \cup }_{n > p}\left\{ {{X}_{n} > {Kn}}\right\} \) est presque sûr. Sur \( {A}_{K} \) on a \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{X}_{n}/n \geq K \) . On en déduit que sur \( B = { \cap }_{K \in {\mathbb{N}}^{ * }}{A}_{K} \) ,événement presque sûr (intersection dénombrable d’événements presque sûrs) on a \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{X}_{n}/n = \; + \infty \) . La minoration \( {S}_{n}/n \geq {X}_{n}/n \) entraîne donc que presque surement, \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{S}_{n}/n = \; + \infty \) . Ceci est incompatible avec l’hypothèse que \( {\left( {S}_{n}/n\right) }_{n \in {\mathbb{N}}^{ * }} \) converge presque surement. Donc \( {X}_{1} \) admet une espérance, donc tous les \( {X}_{n} \) puisque ces variables aléatoires sont identiquement distribuées.

> Since the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{X}_{1} > n}\right) \) diverges, we deduce that \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} > {Kn}}\right) \) diverges. As the events \( {\left\{ {X}_{n} > Kn\right\} }_{n \in {\mathbb{N}}^{ * }} \) are independent, assertion (ii) of the Borel-Cantelli lemma (see theorem 1 on page 326) allows us to deduce that the event \( {A}_{K} = { \cap }_{p \in \mathbb{N}}{ \cup }_{n > p}\left\{ {{X}_{n} > {Kn}}\right\} \) is almost sure. On \( {A}_{K} \) we have \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{X}_{n}/n \geq K \). We deduce that on \( B = { \cap }_{K \in {\mathbb{N}}^{ * }}{A}_{K} \), an almost sure event (countable intersection of almost sure events), we have \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{X}_{n}/n = \; + \infty \). The lower bound \( {S}_{n}/n \geq {X}_{n}/n \) therefore implies that almost surely, \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}\mathop{\sup }\limits_{{n > p}}{S}_{n}/n = \; + \infty \). This is incompatible with the hypothesis that \( {\left( {S}_{n}/n\right) }_{n \in {\mathbb{N}}^{ * }} \) converges almost surely. Thus \( {X}_{1} \) admits an expectation, and therefore so do all \( {X}_{n} \) since these random variables are identically distributed.

Remarque. Ce résultat peut être vu comme une réciproque de la loi forte des grands nombres.

> Remark. This result can be seen as a converse to the strong law of large numbers.

EXERCICE 7 (INEGALITÉ DE HOEFFDING). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes, indépendantes et centrées,à valeurs dans \( \left\lbrack {-\alpha ,\alpha }\right\rbrack \) avec \( \alpha > 0 \) .

> EXERCISE 7 (HOEFFDING'S INEQUALITY). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent, centered, discrete random variables taking values in \( \left\lbrack {-\alpha ,\alpha }\right\rbrack \) with \( \alpha > 0 \).

1/ a) Soit \( Y \) une variable aléatoire discrète centrée,à valeurs dans \( \left\lbrack {-1,1}\right\rbrack \) . Montrer que pour tout \( t \in \mathbb{R} \) , on a \( E\left( {e}^{tY}\right) \leq \operatorname{ch}\left( t\right) \leq {e}^{{t}^{2}/2} \) .

> 1/ a) Let \( Y \) be a centered discrete random variable taking values in \( \left\lbrack {-1,1}\right\rbrack \). Show that for all \( t \in \mathbb{R} \), we have \( E\left( {e}^{tY}\right) \leq \operatorname{ch}\left( t\right) \leq {e}^{{t}^{2}/2} \).

b) On note \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) . Montrer l’inégalité de Hoeffding :

> b) Let \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) be denoted as such. Show Hoeffding's inequality:

\[
\forall \varepsilon  > 0,\forall n \in  {\mathbb{N}}^{ * },\;P\left( {\left| {S}_{n}\right|  \geq  \varepsilon }\right)  \leq  2\exp \left( {-\frac{{\varepsilon }^{2}}{{2n}{\alpha }^{2}}}\right) .
\]

2/ Montrer que presque surement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) .

> 2/ Show that almost surely, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \).

3/ On suppose ici que les variables aléatoires indépendantes \( {X}_{n} \) suivent une loi de Rade-macher \( P\left( {{X}_{n} = - 1}\right) = 1/2 \) , et \( P\left( {{X}_{n} = 1}\right) = 1/2 \) . Montrer que presque surement, on a \( \mathop{\limsup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq 1 \) (on rappelle que \( \mathop{\limsup }\limits_{n}f\left( n\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\mathop{\sup }\limits_{{p \geq n}}f\left( p\right) \) ).

> 3/ Assume here that the independent random variables \( {X}_{n} \) follow a Rademacher distribution \( P\left( {{X}_{n} = - 1}\right) = 1/2 \) , and \( P\left( {{X}_{n} = 1}\right) = 1/2 \) . Show that almost surely, we have \( \mathop{\limsup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq 1 \) (recall that \( \mathop{\limsup }\limits_{n}f\left( n\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\mathop{\sup }\limits_{{p \geq n}}f\left( p\right) \) ).

Solution. 1/a) La convexité de la fonction exponentielle entraîne

> Solution. 1/a) The convexity of the exponential function implies

\[
\forall y \in  \left\lbrack  {-1,1}\right\rbrack  ,\;{e}^{ty} \leq  \frac{1 - y}{2}{e}^{-t} + \frac{1 + y}{2}{e}^{t}.
\]

On en déduit

> We deduce from this

\[
E\left( {e}^{tY}\right)  \leq  \frac{E\left( {1 - Y}\right) }{2}{e}^{-t} + \frac{E\left( {1 + Y}\right) }{2}{e}^{t} = \operatorname{ch}t = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{2n}}{\left( {2n}\right) !} \leq  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{2n}}{n!{2}^{n}} = {e}^{{t}^{2}/2}.
\]

b) Le résultat précédent appliqué à la variable aléatoire \( {X}_{n}/\alpha \) entraîne \( E\left( {e}^{t{X}_{n}/\alpha }\right) \leq {e}^{{t}^{2}/2} \) pour tout \( t \in \mathbb{R} \) , et l’inégalité est vraie lorsqu’on remplace \( t \) par \( {\alpha t} \) ce qui donne \( E\left( {e}^{t{X}_{n}}\right) \leq {e}^{{t}^{2}{\alpha }^{2}/2} \) . Les \( {X}_{i} \) étant indépendants, les \( {e}^{t{X}_{i}} \) également et ceci entraîne

> b) The previous result applied to the random variable \( {X}_{n}/\alpha \) implies \( E\left( {e}^{t{X}_{n}/\alpha }\right) \leq {e}^{{t}^{2}/2} \) for all \( t \in \mathbb{R} \) , and the inequality holds when replacing \( t \) with \( {\alpha t} \) which gives \( E\left( {e}^{t{X}_{n}}\right) \leq {e}^{{t}^{2}{\alpha }^{2}/2} \) . Since the \( {X}_{i} \) are independent, the \( {e}^{t{X}_{i}} \) are as well, and this implies

\[
E\left( {e}^{t{S}_{n}}\right)  = E\left( {{e}^{t{X}_{1}}\cdots {e}^{t{X}_{n}}}\right)  = E\left( {e}^{t{X}_{1}}\right) \cdots E\left( {e}^{t{X}_{n}}\right)  \leq  {e}^{{t}^{2}n{\alpha }^{2}/2}.
\]

L'inégalité de Markov permet d'en déduire

> Markov's inequality allows us to deduce

\[
P\left( {{S}_{n} > \varepsilon }\right)  = P\left( {{e}^{t{S}_{n}} > {e}^{t\varepsilon }}\right)  \leq  \frac{E\left( {e}^{t{S}_{n}}\right) }{{e}^{t\varepsilon }} \leq  {e}^{{t}^{2}n{\alpha }^{2}/2 - {t\varepsilon }}.
\]

En choisissant \( t = \varepsilon /\left( {n{\alpha }^{2}}\right) \) (valeur qui minimise \( {t}^{2}n{\alpha }^{2}/2 - {t\varepsilon } \) ), on en déduit \( P\left( {{S}_{n} > \varepsilon }\right) \leq \; {e}^{-{\varepsilon }^{2}/\left( {{2n}{\alpha }^{2}}\right) } \) . La même inégalité appliquée à la suite \( \left( {-{X}_{n}}\right) \) entraine \( P\left( {{S}_{n} < - \varepsilon }\right) \leq {e}^{-{\varepsilon }^{2}/\left( {{2n}{\alpha }^{2}}\right) } \) , on en déduit l’inégalité souhaitée pour \( P\left( {\left| {S}_{n}\right| < \varepsilon }\right) \) .

> By choosing \( t = \varepsilon /\left( {n{\alpha }^{2}}\right) \) (the value that minimizes \( {t}^{2}n{\alpha }^{2}/2 - {t\varepsilon } \) ), we deduce \( P\left( {{S}_{n} > \varepsilon }\right) \leq \; {e}^{-{\varepsilon }^{2}/\left( {{2n}{\alpha }^{2}}\right) } \) . The same inequality applied to the sequence \( \left( {-{X}_{n}}\right) \) implies \( P\left( {{S}_{n} < - \varepsilon }\right) \leq {e}^{-{\varepsilon }^{2}/\left( {{2n}{\alpha }^{2}}\right) } \) , from which we deduce the desired inequality for \( P\left( {\left| {S}_{n}\right| < \varepsilon }\right) \) .

2/ En choisissant \( \varepsilon = {n}^{3/4} \) , l’inégalité obtenue à la question précédente s’écrit \( P\left( {\left| {{S}_{n}/n}\right| \geq }\right. \; \left. {n}^{-1/4}\right) \leq \exp \left( {-{n}^{1/2}/\left( {2{\alpha }^{2}}\right) }\right) \) . On en déduit que la série \( \mathop{\sum }\limits_{n}P\left( {\left| {{S}_{n}/n}\right| \geq {n}^{-1/4}}\right) \) converge, donc d’après l’assertion (i) du lemme de Borel-Cantelli (voir le théorème 1 page 326), \( \lim \mathop{\sup }\limits_{n}\left\{ {\left| {{S}_{n}/n}\right| \geq }\right. \; \left. \left. {n}^{-1/4}\right) \right\} \) est négligeable. En passant au complémentaire on a donc montré que presque surement, on a \( \left| {{S}_{n}/n}\right| < {n}^{-1/4} \) sauf eventuellement pour un nombre fini de valeurs de \( n \) . On en déduit que presque surement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) .

> 2/ By choosing \( \varepsilon = {n}^{3/4} \) , the inequality obtained in the previous question is written as \( P\left( {\left| {{S}_{n}/n}\right| \geq }\right. \; \left. {n}^{-1/4}\right) \leq \exp \left( {-{n}^{1/2}/\left( {2{\alpha }^{2}}\right) }\right) \) . We deduce that the series \( \mathop{\sum }\limits_{n}P\left( {\left| {{S}_{n}/n}\right| \geq {n}^{-1/4}}\right) \) converges, so according to assertion (i) of the Borel-Cantelli lemma (see theorem 1 on page 326), \( \lim \mathop{\sup }\limits_{n}\left\{ {\left| {{S}_{n}/n}\right| \geq }\right. \; \left. \left. {n}^{-1/4}\right) \right\} \) is negligible. By passing to the complement, we have therefore shown that almost surely, we have \( \left| {{S}_{n}/n}\right| < {n}^{-1/4} \) except possibly for a finite number of values of \( n \) . We deduce that almost surely, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) .

3 / Soit \( c > 1 \) . On peut appliquer l’inégalité de Hoeffding à \( \left( {X}_{n}\right) \) , avec \( \alpha = 1 \) , ce qui donne

> 3 / Let \( c > 1 \) . We can apply Hoeffding's inequality to \( \left( {X}_{n}\right) \) , with \( \alpha = 1 \) , which gives

\[
P\left( {\left| {S}_{n}\right|  \geq  \sqrt{{2cn}\log n}}\right)  \leq  2\exp \left( {-\frac{{2cn}\log n}{2n}}\right)  = \frac{2}{{n}^{c}}.
\]

Donc la série \( \mathop{\sum }\limits_{n}P\left( {\left| {S}_{n}\right| \geq \sqrt{{2cn}\log n}}\right) \) converge, et avec le lemme de Borel-Cantelli on en déduit l’existence d’un événement \( A\left( c\right) \) presque sûr tel que sur \( A\left( c\right) ,\left| {S}_{n}\right| < \sqrt{{2cn}\log n} \) sauf eventuellement pour un nombre fini d’entiers \( n \) . Sur \( A\left( c\right) \) on a donc lim \( \mathop{\sup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq \; \sqrt{c} \) . En donnant à \( c \) les valeurs \( c = {e}^{1/p} \) avec \( p \in {\mathbb{N}}^{ * } \) , on en déduit que sur l’événement presque sûr \( A = { \cap }_{p \in {\mathbb{N}}^{ * }}A\left( {e}^{1/p}\right) \) (intersection dénombrable d’événements presque sûrs), on a \( \mathop{\limsup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq {e}^{1/\left( {2p}\right) } \) pour tout \( p \in {\mathbb{N}}^{ * } \) , donc que limsup \( \left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq 1 \) sur \( A \) .

> Thus the series \( \mathop{\sum }\limits_{n}P\left( {\left| {S}_{n}\right| \geq \sqrt{{2cn}\log n}}\right) \) converges, and with the Borel-Cantelli lemma we deduce the existence of an almost sure event \( A\left( c\right) \) such that on \( A\left( c\right) ,\left| {S}_{n}\right| < \sqrt{{2cn}\log n} \) except possibly for a finite number of integers \( n \) . On \( A\left( c\right) \) we therefore have lim \( \mathop{\sup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq \; \sqrt{c} \) . By giving \( c \) the values \( c = {e}^{1/p} \) with \( p \in {\mathbb{N}}^{ * } \) , we deduce that on the almost sure event \( A = { \cap }_{p \in {\mathbb{N}}^{ * }}A\left( {e}^{1/p}\right) \) (countable intersection of almost sure events), we have \( \mathop{\limsup }\limits_{n}\left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq {e}^{1/\left( {2p}\right) } \) for all \( p \in {\mathbb{N}}^{ * } \) , and therefore that limsup \( \left| {S}_{n}\right| /\sqrt{{2n}\log n} \leq 1 \) on \( A \) .

Remarque. On déduit facilement du résultat 2/ que pour toute suite de variables aléatoires discrètes \( \left( {X}_{n}\right) \) indépendantes, identiquement distribuées, et uniformément bornées, on a presque surement \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n = E\left( {X}_{1}\right) \) (il suffit d’appliquer 2/ aux variables \( {Y}_{i} = {X}_{i} - E\left( {X}_{1}\right) ) \) . On vient donc de démontrer la loi forte des grands nombres dans le cas des variables aléatoires bornées. Une preuve dans le cas plus général \( {\mathcal{L}}^{4} \) fait l’objet de l'exercice 13 page 363, et dans le cas général, du problème 10 page 389.

> Remark. It is easily deduced from result 2/ that for any sequence of independent, identically distributed, and uniformly bounded discrete random variables \( \left( {X}_{n}\right) \), we have almost surely \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n = E\left( {X}_{1}\right) \) (it suffices to apply 2/ to the variables \( {Y}_{i} = {X}_{i} - E\left( {X}_{1}\right) ) \)). We have thus just proven the strong law of large numbers in the case of bounded random variables. A proof in the more general case \( {\mathcal{L}}^{4} \) is the subject of exercise 13 on page 363, and in the general case, of problem 10 on page 389.

- Lorsque \( \varepsilon \) est beaucoup plus grand que \( 1/\sqrt{n} \) (on parle de grandes dévaitions), l’inégalité de Hoeffding est bien plus fine que l'inégalité (*) du théorème 1 page 345. Une approximation des déviations par rapport à la moyenne est obtenue avec le théorème central limite, qui fait l'objet du problème 9 page 386.

> - When \( \varepsilon \) is much larger than \( 1/\sqrt{n} \) (this is referred to as large deviations), Hoeffding's inequality is much sharper than inequality (*) of theorem 1 on page 345. An approximation of the deviations from the mean is obtained with the central limit theorem, which is the subject of problem 9 on page 386.

EXERCICE 8. On considère une famille \( {\left( {X}_{i, j}\right) }_{\left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}} \) de variables aléatoires discrètes réelles, indépendantes, admettant une même variance \( V\left( {X}_{i, j}\right) = {b}^{2} \) avec \( b > 0 \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) on note \( {M}_{n} \) la matrice aléatoire \( {\left( {X}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> EXERCISE 8. Consider a family \( {\left( {X}_{i, j}\right) }_{\left( {i, j}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}} \) of independent, real-valued discrete random variables, admitting the same variance \( V\left( {X}_{i, j}\right) = {b}^{2} \) with \( b > 0 \). For any \( n \in {\mathbb{N}}^{ * } \), we denote by \( {M}_{n} \) the random matrix \( {\left( {X}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \).

1/a) On suppose que les \( {X}_{i, j} \) sont centrées. Calculer l’espérance et la variance de \( \operatorname{tr}{M}_{n} \) et \( \det {M}_{n} \) .

> 1/a) Assume that the \( {X}_{i, j} \) are centered. Calculate the expectation and variance of \( \operatorname{tr}{M}_{n} \) and \( \det {M}_{n} \).

b) \( \operatorname{Si}\left( {u}_{n}\right) \) est une suite vérifiant \( {b}^{n} = o\left( {u}_{n}\right) \) , montrer \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {\det {M}_{n}}\right| \geq {u}_{n}\sqrt{n!}}\right) = 0 \) . 2/On suppose ici que les \( {X}_{i, j} \) admettent toutes une même espérance \( a \in \mathbb{R} \) .

> b) \( \operatorname{Si}\left( {u}_{n}\right) \) is a sequence satisfying \( {b}^{n} = o\left( {u}_{n}\right) \), show \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {\det {M}_{n}}\right| \geq {u}_{n}\sqrt{n!}}\right) = 0 \). 2/ We assume here that the \( {X}_{i, j} \) all admit the same expectation \( a \in \mathbb{R} \).

a) Calculer l’espérance et la variance de tr \( {M}_{n} \) , et l’espérance de det \( {M}_{n} \) .

> a) Calculate the expectation and variance of tr \( {M}_{n} \), and the expectation of det \( {M}_{n} \).

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {\mathcal{F}}_{n} \) l’ensemble des permutations de \( {\mathcal{S}}_{n} \) sans point fixe, et \( {f}_{n} = \mathop{\sum }\limits_{{\sigma \in {\mathcal{F}}_{n}}}\varepsilon \left( \sigma \right) \) (où \( \varepsilon \left( \sigma \right) \) désigne la signature de la permutation \( \sigma \) ). Montrer que

> b) For any \( n \in {\mathbb{N}}^{ * } \), we denote by \( {\mathcal{F}}_{n} \) the set of permutations of \( {\mathcal{S}}_{n} \) without fixed points, and \( {f}_{n} = \mathop{\sum }\limits_{{\sigma \in {\mathcal{F}}_{n}}}\varepsilon \left( \sigma \right) \) (where \( \varepsilon \left( \sigma \right) \) denotes the signature of the permutation \( \sigma \)). Show that

\[
E\left( {\left( \det {M}_{n}\right) }^{2}\right)  = n!{\left( {a}^{2} + {b}^{2}\right) }^{n}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {f}_{k}{\rho }^{k},\;\rho  = \frac{{a}^{2}}{{a}^{2} + {b}^{2}}.
\]

c) Établir une relation de récurrence vérifiée par \( {f}_{n} \) puis calculer la série génératrice exponentielle \( F\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}_{n}/n \) !. En déduire une expression simplifiée de \( V\left( {\det {M}_{n}}\right) \) .

> c) Establish a recurrence relation satisfied by \( {f}_{n} \) then calculate the exponential generating series \( F\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}_{n}/n \)!. Deduce a simplified expression for \( V\left( {\det {M}_{n}}\right) \).

d) Retrouver la variance de det \( {M}_{n} \) en centrant les \( {X}_{i, j} \) , en complétant \( {M}_{n} \) par une matrice \( {A}_{n} \) de taille \( n + 1 \) bordée par des 1 sur la dernière ligne et des 0 sur sa dernière colonne (le coefficient d'indice \( \left( {n + 1, n + 1}\right) \) étant égal à 1).

> d) Recover the variance of det \( {M}_{n} \) by centering the \( {X}_{i, j} \) , by completing \( {M}_{n} \) with a matrix \( {A}_{n} \) of size \( n + 1 \) bordered by 1s on the last row and 0s on its last column (the coefficient with index \( \left( {n + 1, n + 1}\right) \) being equal to 1).

Solution. 1/a) Pour tr \( {M}_{n} \) le résultat est immédiat car l’indépendance des \( {X}_{i, j} \) entraîne

> Solution. 1/a) For tr \( {M}_{n} \) the result is immediate because the independence of the \( {X}_{i, j} \) implies

\[
E\left( {\operatorname{tr}{M}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}E\left( {X}_{i, i}\right)  = 0\;\text{ et }\;V\left( {\operatorname{tr}{M}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}V\left( {X}_{i, i}\right)  = n{b}^{2}.
\]

Pour le déterminant, l’indépendance des \( {X}_{i, j} \) entraîne

> For the determinant, the independence of the \( {X}_{i, j} \) implies

\[
E\left( {\det {M}_{n}}\right)  = E\left( {\mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) \mathop{\prod }\limits_{{i = 1}}^{n}{X}_{i,\sigma \left( i\right) }}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) E\left( {\mathop{\prod }\limits_{{i = 1}}^{n}{X}_{i,\sigma \left( i\right) }}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {X}_{i,\sigma \left( i\right) }\right)
\]

et comme les \( {X}_{i, j} \) sont centrées on en déduit \( E\left( {\det {M}_{n}}\right) = 0 \) . Pour la variance on écrit

> and since the \( {X}_{i, j} \) are centered we deduce \( E\left( {\det {M}_{n}}\right) = 0 \) . For the variance we write

\[
E\left( {\left( \det {M}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\left( {\sigma ,\mu }\right)  \in  {\mathcal{S}}_{n}^{2}}}\varepsilon \left( \sigma \right) \varepsilon \left( \mu \right) E\left( {\mathop{\prod }\limits_{{i = 1}}^{n}{X}_{i,\sigma \left( i\right) }{X}_{i,\mu \left( i\right) }}\right)  = \mathop{\sum }\limits_{{\left( {\sigma ,\mu }\right)  \in  {\mathcal{S}}_{n}^{2}}}\varepsilon \left( \sigma \right) \varepsilon \left( \mu \right) \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {{X}_{i,\sigma \left( i\right) }{X}_{i,\mu \left( i\right) }}\right) .
\]

(*)

> Si \( \sigma \neq \mu \) , il existe \( i \) tel que \( \sigma \left( i\right) \neq \mu \left( i\right) \) donc \( E\left( {{X}_{i,\sigma \left( i\right) }{X}_{i,\mu \left( i\right) }}\right) = E\left( {X}_{i,\sigma \left( i\right) }\right) E\left( {X}_{i,\mu \left( i\right) }\right) = 0 \) . Dans la somme de (*), on ne doit donc considérer que les cas où \( \sigma = \mu \) , ce qui donne,

If \( \sigma \neq \mu \) , there exists \( i \) such that \( \sigma \left( i\right) \neq \mu \left( i\right) \) so \( E\left( {{X}_{i,\sigma \left( i\right) }{X}_{i,\mu \left( i\right) }}\right) = E\left( {X}_{i,\sigma \left( i\right) }\right) E\left( {X}_{i,\mu \left( i\right) }\right) = 0 \) . In the sum of (*), we must therefore only consider the cases where \( \sigma = \mu \) , which gives,

\[
E\left( {\left( \det {M}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon {\left( \sigma \right) }^{2}\mathop{\prod }\limits_{{i = 1}}^{n}E\left( {X}_{i,\sigma \left( i\right) }^{2}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\mathop{\prod }\limits_{{i = 1}}^{n}{b}^{2} = n!{b}^{2n}.
\]

On conclut avec le théorème de Koënig-Huygens qui donne \( V\left( {\det {M}_{n}}\right) = E\left( {\left( \det {M}_{n}\right) }^{2}\right) = n!{b}^{2n} \) . b) Il suffit d'appliquer l'inégalité de Bienaymé-Tchébycheff qui entraîne

> We conclude with the Koënig-Huygens theorem which gives \( V\left( {\det {M}_{n}}\right) = E\left( {\left( \det {M}_{n}\right) }^{2}\right) = n!{b}^{2n} \) . b) It suffices to apply the Bienaymé-Chebyshev inequality which implies

\[
P\left( {\left| {\det {M}_{n}}\right|  > {u}_{n}\sqrt{n!}}\right)  \leq  \frac{V\left( {M}_{n}\right) }{{u}_{n}^{2}n!} = {\left( \frac{{b}^{n}}{{u}_{n}}\right) }^{2}.
\]

\( \mathbf{2}/\mathbf{a} \) ) En procédant comme dans \( 1/\mathrm{a} \) ) on obtient \( E\left( {\operatorname{tr}{M}_{n}}\right) = {na} \) et \( V\left( {\operatorname{tr}{M}_{n}}\right) = n{b}^{2} \) , et

> \( \mathbf{2}/\mathbf{a} \) ) By proceeding as in \( 1/\mathrm{a} \) ) we obtain \( E\left( {\operatorname{tr}{M}_{n}}\right) = {na} \) and \( V\left( {\operatorname{tr}{M}_{n}}\right) = n{b}^{2} \) , and

\[
E\left( {\det {M}_{n}}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {X}_{i,\sigma \left( i\right) }\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) \mathop{\prod }\limits_{{i = 1}}^{n}a = {a}^{n}\mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) .
\]

On en déduit \( E\left( {\det {M}_{n}}\right) = a \) si \( n = 1, E\left( {\det {M}_{n}}\right) = 0 \) si \( n > 1 \) .

> We deduce \( E\left( {\det {M}_{n}}\right) = a \) if \( n = 1, E\left( {\det {M}_{n}}\right) = 0 \) if \( n > 1 \) .

b) On récrit la formule (*) en posant \( \mu = {\sigma \nu } \) , ce qui donne

> b) We rewrite the formula (*) by setting \( \mu = {\sigma \nu } \) , which gives

\[
E\left( {\left( \det {M}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\left( {\sigma ,\nu }\right)  \in  {\mathcal{S}}_{n}^{2}}}\varepsilon \left( \sigma \right) \varepsilon \left( {\sigma \nu }\right) \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {{X}_{i,\sigma \left( i\right) }{X}_{i,\sigma \left( {\nu \left( i\right) }\right) }}\right) .
\]

On a \( \varepsilon \left( \sigma \right) \varepsilon \left( {\sigma \nu }\right) = \varepsilon {\left( \sigma \right) }^{2}\varepsilon \left( \nu \right) = \varepsilon \left( \nu \right) \) . Par ailleurs,

> We have \( \varepsilon \left( \sigma \right) \varepsilon \left( {\sigma \nu }\right) = \varepsilon {\left( \sigma \right) }^{2}\varepsilon \left( \nu \right) = \varepsilon \left( \nu \right) \) . Furthermore,

\[
E\left( {{X}_{i,\sigma \left( i\right) }{X}_{i,\sigma \left( {\nu \left( i\right) }\right) }}\right)  = \left\{  \begin{array}{ll} E\left( {X}_{i,\sigma \left( i\right) }\right) E\left( {X}_{i,\sigma \left( {\nu \left( i\right) }\right) }\right)  = {a}^{2} & \text{ si }\nu \left( i\right)  \neq  i, \\  E\left( {X}_{i,\sigma \left( i\right) }^{2}\right)  = {a}^{2} + {b}^{2} & \text{ si }\nu \left( i\right)  = i. \end{array}\right.
\]

En notant \( D\left( \nu \right) = \{ i \in \{ 1,\ldots , n\} \mid \nu \left( i\right) \neq i\} \) on a donc

> By noting \( D\left( \nu \right) = \{ i \in \{ 1,\ldots , n\} \mid \nu \left( i\right) \neq i\} \) we therefore have

\[
E\left( {\left( \det {M}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\mathop{\sum }\limits_{{\nu  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \nu \right) {a}^{2\left| {D\left( \nu \right) }\right| }{\left( {a}^{2} + {b}^{2}\right) }^{n - \left| {D\left( \nu \right) }\right| } = n!{\left( {a}^{2} + {b}^{2}\right) }^{n}\mathop{\sum }\limits_{{\nu  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \nu \right) {\rho }^{\left| D\left( \nu \right) \right| }.
\]

Soit \( k \in \{ 0,\ldots , n\} \) . Notons \( {\mathcal{P}}_{k} = \{ I \subset \{ 1,\ldots , n\} ,\left| I\right| = k\} \) . Fixons \( I \in {\mathcal{P}}_{k} \) et \( q \in {\mathcal{S}}_{n} \) telle que \( q\left( {\{ 1,\ldots , k\} }\right) = I \) . Pour tout \( \nu \in {\mathcal{S}}_{n} \) telle que \( D\left( \nu \right) = I \) , la permutation \( {\tau }_{\nu } = {q}^{-1}{\nu q} \) vérifie \( {\tau }_{\nu }\left( i\right) = i \) pour \( k < i \leq n \) , et la restriction \( {\tau }_{\nu }^{\prime } \) de \( {\tau }_{\nu } \) à \( \{ 1,\ldots , k\} \) est dans \( {\mathcal{F}}_{k} \) . On a par ailleurs \( \varepsilon \left( \nu \right) = \varepsilon \left( {\tau }_{\nu }\right) = \varepsilon \left( {\tau }_{\nu }^{\prime }\right) \) . L’application \( \nu \rightarrow {\tau }_{\nu }^{\prime } \) est une bijection de \( \left\{ {\nu \in {\mathcal{S}}_{n} \mid D\left( \nu \right) = I}\right\} \) vers \( {\mathcal{F}}_{k} \) , on a donc \( \mathop{\sum }\limits_{{\nu : D\left( \nu \right) = I}}\varepsilon \left( \nu \right) = \mathop{\sum }\limits_{{\tau \in {\mathcal{F}}_{k}}}\varepsilon \left( \tau \right) = {f}_{k} \) (notons qu’on doit avoir \( {f}_{0} = 1 \) pour que cette égalité reste vraie). On en déduit le résultat demandé en écrivant

> Let \( k \in \{ 0,\ldots , n\} \). Let \( {\mathcal{P}}_{k} = \{ I \subset \{ 1,\ldots , n\} ,\left| I\right| = k\} \). Fix \( I \in {\mathcal{P}}_{k} \) and \( q \in {\mathcal{S}}_{n} \) such that \( q\left( {\{ 1,\ldots , k\} }\right) = I \). For any \( \nu \in {\mathcal{S}}_{n} \) such that \( D\left( \nu \right) = I \), the permutation \( {\tau }_{\nu } = {q}^{-1}{\nu q} \) satisfies \( {\tau }_{\nu }\left( i\right) = i \) for \( k < i \leq n \), and the restriction \( {\tau }_{\nu }^{\prime } \) of \( {\tau }_{\nu } \) to \( \{ 1,\ldots , k\} \) is in \( {\mathcal{F}}_{k} \). Furthermore, we have \( \varepsilon \left( \nu \right) = \varepsilon \left( {\tau }_{\nu }\right) = \varepsilon \left( {\tau }_{\nu }^{\prime }\right) \). The map \( \nu \rightarrow {\tau }_{\nu }^{\prime } \) is a bijection from \( \left\{ {\nu \in {\mathcal{S}}_{n} \mid D\left( \nu \right) = I}\right\} \) to \( {\mathcal{F}}_{k} \), so we have \( \mathop{\sum }\limits_{{\nu : D\left( \nu \right) = I}}\varepsilon \left( \nu \right) = \mathop{\sum }\limits_{{\tau \in {\mathcal{F}}_{k}}}\varepsilon \left( \tau \right) = {f}_{k} \) (note that we must have \( {f}_{0} = 1 \) for this equality to remain true). We deduce the requested result by writing

\[
\mathop{\sum }\limits_{{\nu  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \nu \right) {\rho }^{\left| D\left( \nu \right) \right| } = \mathop{\sum }\limits_{{k = 0}}^{n}\mathop{\sum }\limits_{{I \in  {\mathcal{P}}_{k}}}\mathop{\sum }\limits_{\substack{{\nu  \in  {\mathcal{S}}_{n}} \\  {D\left( \nu \right)  = I} }}\varepsilon \left( \nu \right) {\rho }^{k} = \mathop{\sum }\limits_{{k = 0}}^{n}\mathop{\sum }\limits_{{I \in  {\mathcal{P}}_{k}}}{f}_{k}{\rho }^{k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {f}_{k}{\rho }^{k}.
\]

c) L’égalité précédente appliquée avec \( \rho = 1 \) entraîne

> c) The previous equality applied with \( \rho = 1 \) leads to

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{f}_{k}}{k!}\frac{1}{\left( {n - k}\right) !} = \frac{1}{n!}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {f}_{k} = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right)  = \left\{  \begin{array}{l} 1\text{ si }n = 1 \\  0\text{ si }n > 1. \end{array}\right.
\]

Notons que \( \left| {f}_{k}\right| \leq \left| {\mathcal{F}}_{k}\right| \leq k \) !, donc \( F\left( z\right) \) a un rayon de convergence \( \geq 1 \) . On reconnait dans l’égalité précédente un produit de Cauchy, qui montre que pour tout \( z \) tel que \( \left| z\right| < 1 \) ,

> Note that \( \left| {f}_{k}\right| \leq \left| {\mathcal{F}}_{k}\right| \leq k \) !, so \( F\left( z\right) \) has a radius of convergence \( \geq 1 \). We recognize in the previous equality a Cauchy product, which shows that for any \( z \) such that \( \left| z\right| < 1 \),

\[
F\left( z\right) {e}^{z} = \left( {\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{{f}_{k}}{k!}{z}^{k}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{n!}{z}^{n}}\right)  = {f}_{0} + z = 1 + z.
\]

On en déduit \( F\left( z\right) = {e}^{-z}\left( {1 + z}\right) = 1 + \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\left( {\frac{{\left( -1\right) }^{k}}{k!} + \frac{{\left( -1\right) }^{k - 1}}{\left( {k - 1}\right) !}}\right) {z}^{k} \) et par identification de coefficient on en tire \( {f}_{k} = {\left( -1\right) }^{k}\left( {1 - k}\right) \) . On en déduit, en posant \( \varphi \left( x\right) = {\left( 1 + x\right) }^{n} \) ,

> We deduce \( F\left( z\right) = {e}^{-z}\left( {1 + z}\right) = 1 + \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\left( {\frac{{\left( -1\right) }^{k}}{k!} + \frac{{\left( -1\right) }^{k - 1}}{\left( {k - 1}\right) !}}\right) {z}^{k} \) and by identifying coefficients we obtain \( {f}_{k} = {\left( -1\right) }^{k}\left( {1 - k}\right) \). We deduce, by setting \( \varphi \left( x\right) = {\left( 1 + x\right) }^{n} \),

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {f}_{k}{\rho }^{k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left( {{\left( -\rho \right) }^{k} + {\rho k}{\left( -\rho \right) }^{k - 1}}\right)  = \varphi \left( {-\rho }\right)  + \rho {\varphi }^{\prime }\left( {-\rho }\right)  = {\left( 1 - \rho \right) }^{n - 1}\left( {1 - \rho  + {n\rho }}\right) .
\]

En remplaçant dans l'expression obtenue dans la question précédente, on en déduit, lorsque \( n \geq 2 \) , compte tenu du fait que det \( {M}_{n} \) soit centré et de la valeur de \( \rho \) ,

> By substituting into the expression obtained in the previous question, we deduce, when \( n \geq 2 \), given the fact that det \( {M}_{n} \) is centered and the value of \( \rho \),

\[
V\left( {\det {M}_{n}}\right)  = n!{\left( {a}^{2} + {b}^{2}\right) }^{n}{\left( \frac{{b}^{2}}{{a}^{2} + {b}^{2}}\right) }^{n - 1}\left( {1 + \left( {n - 1}\right) \frac{{a}^{2}}{{a}^{2} + {b}^{2}}}\right)  = n!{b}^{{2n} - 2}\left( {{b}^{2} + n{a}^{2}}\right) .
\]

Il reste à traiter le cas \( n = 1 \) , immédiat car det \( {M}_{1} = {X}_{1,1} \) donc \( V\left( {\det {M}_{1}}\right) = {b}^{2} \) .

> It remains to treat the case \( n = 1 \) , immediate because det \( {M}_{1} = {X}_{1,1} \) therefore \( V\left( {\det {M}_{1}}\right) = {b}^{2} \) .

d) Notons que \( {A}_{n} \) s’écrit par blocs sous la forme \( {A}_{n} = \left( \begin{matrix} {M}_{n} & 0 \\ 1 & 1 \end{matrix}\right) \) et que det \( {A}_{n} = \det {M}_{n} \) . Notons \( {B}_{n} \) la matrice obtenue à partir de \( {A}_{n} \) en retranchant à chacune des \( n \) premières lignes \( a \) fois la dernière. On a det \( {B}_{n} = \det {A}_{n} = \det {M}_{n} \) . Notons \( {X}_{i, j}^{ * } = {X}_{i, j} - a \) les variables aléatoires \( {X}_{i, j} \) centrées. Les coefficients de \( {B}_{n} \) sont \( {B}_{n} = {\left( {Y}_{i, j}\right) }_{1 \leq i, j \leq n + 1} \) , avec \( {Y}_{i, j} = {X}_{i, j}^{ * } \) pour \( 1 \leq i, j \leq n \) , \( {Y}_{i, n + 1} = - a \) pour \( 1 \leq i \leq n \) , et \( {Y}_{n + 1, j} = 1 \) pour \( 1 \leq j \leq n + 1 \) . Les variables aléatoires \( {Y}_{i, j} \) sont indépendantes donc on peut appliquer la formule (*) à \( E\left( {\left( \det {B}_{n}\right) }^{2}\right) \) , ce qui donne

> d) Note that \( {A}_{n} \) can be written in block form as \( {A}_{n} = \left( \begin{matrix} {M}_{n} & 0 \\ 1 & 1 \end{matrix}\right) \) and that det \( {A}_{n} = \det {M}_{n} \) . Let \( {B}_{n} \) be the matrix obtained from \( {A}_{n} \) by subtracting \( a \) times the last row from each of the first \( n \) rows. We have det \( {B}_{n} = \det {A}_{n} = \det {M}_{n} \) . Let \( {X}_{i, j}^{ * } = {X}_{i, j} - a \) be the centered random variables \( {X}_{i, j} \) . The coefficients of \( {B}_{n} \) are \( {B}_{n} = {\left( {Y}_{i, j}\right) }_{1 \leq i, j \leq n + 1} \) , with \( {Y}_{i, j} = {X}_{i, j}^{ * } \) for \( 1 \leq i, j \leq n \) , \( {Y}_{i, n + 1} = - a \) for \( 1 \leq i \leq n \) , and \( {Y}_{n + 1, j} = 1 \) for \( 1 \leq j \leq n + 1 \) . The random variables \( {Y}_{i, j} \) are independent, so we can apply formula (*) to \( E\left( {\left( \det {B}_{n}\right) }^{2}\right) \) , which gives

\[
E\left( {\left( \det {B}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\left( {\sigma ,\mu }\right)  \in  {\left( {\mathcal{S}}_{n + 1}\right) }^{2}}}\varepsilon \left( \sigma \right) \varepsilon \left( \mu \right) {P}_{\sigma ,\mu },\;{P}_{\sigma ,\mu } = \mathop{\prod }\limits_{{i = 1}}^{{n + 1}}E\left( {{Y}_{i,\sigma \left( i\right) }{Y}_{i,\mu \left( i\right) }}\right) .
\]

Si \( \sigma \neq \mu \) , on a au moins deux indices distincts \( i \) et \( j \) tels que \( \sigma \left( i\right) \neq \mu \left( i\right) \) et \( \sigma \left( j\right) \neq \mu \left( j\right) \) . L’un de ces deux indices est \( \leq n \) , par exemple \( i \) . Comme \( \sigma \left( i\right) \neq \mu \left( i\right) \) , l’un de ces deux indices est \( \leq n \) , par exemple \( \sigma \left( i\right) \leq n \) . On a alors \( E\left( {{Y}_{i,\sigma \left( i\right) }{Y}_{i,\mu \left( i\right) }}\right) = E\left( {X}_{i,\sigma \left( i\right) }^{ * }\right) E\left( {Y}_{i,\mu \left( i\right) }\right) = 0 \) . Donc les seuls \( {P}_{\sigma ,\mu } \) non nuls sont ceux pour lesquels \( \sigma = \mu \) . On traite maintenant deux cas. Si \( \sigma \left( {n + 1}\right) = n + 1 \) , alors \( {P}_{\sigma ,\sigma } = \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {\left( {X}_{i,\sigma \left( i\right) }^{ * }\right) }^{2}\right) = {b}^{2n} \) . Si \( \sigma \left( {n + 1}\right) \neq n + 1 \) , alors en notant \( j = {\sigma }^{-1}\left( {n + 1}\right) \) on a

> If \( \sigma \neq \mu \) , we have at least two distinct indices \( i \) and \( j \) such that \( \sigma \left( i\right) \neq \mu \left( i\right) \) and \( \sigma \left( j\right) \neq \mu \left( j\right) \) . One of these two indices is \( \leq n \) , for example \( i \) . Since \( \sigma \left( i\right) \neq \mu \left( i\right) \) , one of these two indices is \( \leq n \) , for example \( \sigma \left( i\right) \leq n \) . We then have \( E\left( {{Y}_{i,\sigma \left( i\right) }{Y}_{i,\mu \left( i\right) }}\right) = E\left( {X}_{i,\sigma \left( i\right) }^{ * }\right) E\left( {Y}_{i,\mu \left( i\right) }\right) = 0 \) . Thus the only non-zero \( {P}_{\sigma ,\mu } \) are those for which \( \sigma = \mu \) . We now treat two cases. If \( \sigma \left( {n + 1}\right) = n + 1 \) , then \( {P}_{\sigma ,\sigma } = \mathop{\prod }\limits_{{i = 1}}^{n}E\left( {\left( {X}_{i,\sigma \left( i\right) }^{ * }\right) }^{2}\right) = {b}^{2n} \) . If \( \sigma \left( {n + 1}\right) \neq n + 1 \) , then by denoting \( j = {\sigma }^{-1}\left( {n + 1}\right) \) we have

\[
{P}_{\sigma ,\sigma } = E\left( {Y}_{j, n + 1}^{2}\right) E\left( {Y}_{n + 1,\sigma \left( {n + 1}\right) }^{2}\right) \mathop{\prod }\limits_{{i \leq  n, i \neq  j}}E\left( {\left( {X}_{i,\sigma \left( i\right) }^{ * }\right) }^{2}\right)  = {a}^{2}{b}^{{2n} - 2}.
\]

On en déduit

> We deduce from this

\[
E\left( {\left( \det {B}_{n}\right) }^{2}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n + 1}}}{P}_{\sigma ,\sigma } = \mathop{\sum }\limits_{\substack{{\sigma  \in  {\mathcal{S}}_{n + 1}} \\  {\sigma \left( {n + 1}\right)  = n + 1} }}{P}_{\sigma ,\sigma } + \mathop{\sum }\limits_{\substack{{\sigma  \in  {\mathcal{S}}_{n + 1}} \\  {\sigma \left( {n + 1}\right)  \neq  n + 1} }}{P}_{\sigma ,\sigma } = n!{b}^{2n} + n\;n!{a}^{2}{b}^{{2n} - 2}.
\]

Comme det \( {M}_{n} = \det {B}_{n} \) , on retrouve ainsi le résultat de la question \( 1/\mathrm{c} \) ).

> Since det \( {M}_{n} = \det {B}_{n} \) , we thus recover the result of question \( 1/\mathrm{c} \) ).

EXERCICE 9 (PROBLEME DU COLLECTIONNEUR). Soit \( r \in {\mathbb{N}}^{ * } \) et \( \left( {X}_{n}\right) \) une suite de variables aléatoires à valeurs dans \( \{ 1,\ldots , r\} \) , indépendantes. qui suivent une loi uniforme sur \( \{ 1,\ldots , r\} \) . Les \( {X}_{n} \) modélisent des vignettes réunies par un collectionneur, qui les achète une par une sans savoir à l’avance laquelle il va avoir. On note \( {t}_{k} \) le nombre d’achats effectués par le collectionneur pour avoir \( k \) vignettes différentes, c’est-à-dire

> EXERCISE 9 (COLLECTOR'S PROBLEM). Let \( r \in {\mathbb{N}}^{ * } \) and \( \left( {X}_{n}\right) \) be a sequence of independent random variables taking values in \( \{ 1,\ldots , r\} \), which follow a uniform distribution on \( \{ 1,\ldots , r\} \). The \( {X}_{n} \) model stickers collected by a collector, who buys them one by one without knowing in advance which one they will get. Let \( {t}_{k} \) be the number of purchases made by the collector to obtain \( k \) different stickers, that is to say

\[
{t}_{0} = 0\;\text{ et }\;\forall k \in  {\mathbb{N}}^{ * }, k \leq  r,\;{t}_{k} = \min \left\{  {n \geq  1 \mid  \operatorname{Card}\left\{  {{X}_{1},\ldots ,{X}_{n}}\right\}   = k}\right\}  .
\]

On s’interesse au temps \( {T}_{r} = {t}_{r} \) nécessaire pour compléter l’ensemble de la collection. 1/ Montrer que l’espérance de \( {T}_{r} \) est égale à

> We are interested in the time \( {T}_{r} = {t}_{r} \) required to complete the entire collection. 1/ Show that the expectation of \( {T}_{r} \) is equal to

\[
E\left( {T}_{r}\right)  = r{H}_{r},\;\text{ où }\;{H}_{r} = \mathop{\sum }\limits_{{k = 1}}^{r}\frac{1}{k}.
\]

(indication : montrer que les \( {\tau }_{k} = {t}_{k} - {t}_{k - 1} \) suivent une loi géométrique). 2/a) Calculer la variance de \( {T}_{r} \) .

> (hint: show that the \( {\tau }_{k} = {t}_{k} - {t}_{k - 1} \) follow a geometric distribution). 2/a) Calculate the variance of \( {T}_{r} \) .

b) Montrer que

> b) Show that

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{r \rightarrow   + \infty }}P\left( {\left| {\frac{{T}_{r}}{r\log r} - 1}\right|  > \varepsilon }\right)  = 0.
\]

\( \mathbf{3/a)} \) Montrer que

> \( \mathbf{3/a)} \) Show that

\[
\forall n \in  \mathbb{N},\;P\left( {{T}_{r} > n}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}{\left( -1\right) }^{k - 1}\left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{n}.
\]

b) Pour tout \( a > 0 \) , montrer que

> b) For all \( a > 0 \) , show that

\[
\mathop{\lim }\limits_{{r \rightarrow   + \infty }}P\left( {\left| \frac{{T}_{r} - r\log r}{r}\right|  < a}\right)  = {e}^{-{e}^{-a}} - {e}^{-{e}^{a}}.
\]

c) En déduire, dans le cas \( r = {100} \) , un encadrement du nombre de vignettes \( {T}_{r} \) à acheter pour avoir 95% de chance de compléter la collection.

> c) Deduce, in the case \( r = {100} \) , a bound for the number of stickers \( {T}_{r} \) to buy to have a 95% chance of completing the collection.

Solution. 1/ Lorsque \( 1 \leq k \leq r \) , la variable aléatoire \( {\tau }_{k} = {t}_{k} - {t}_{k - 1} \) est le nombre d’achats nécéssaires pour passer d’une collection de \( k - 1 \) vignettes différentes à \( k \) vignettes différentes, autrement dit

> Solution. 1/ When \( 1 \leq k \leq r \) , the random variable \( {\tau }_{k} = {t}_{k} - {t}_{k - 1} \) is the number of purchases necessary to go from a collection of \( k - 1 \) different stickers to \( k \) different stickers, in other words

\[
{\tau }_{k} = \min \left\{  {m \geq  1 \mid  {X}_{{t}_{k - 1} + m} \notin  \left\{  {{X}_{1},\ldots ,{X}_{{t}_{k - 1}}}\right\}  }\right\}  .
\]

La variable aléatoire \( {\tau }_{k} \) est le temps d’apparition du premier gain dans un jeu de pile ou face, pour lequel la probabilité de gain est \( \left( {r - k + 1}\right) /r \) (probabilité que \( {X}_{{t}_{k - 1} + m} \) soit l’une des \( r - k + 1 \) vignettes différentes des \( k - 1 \) déjà obtenues). Elle suit donc une loi géométrique de paramètre \( \left( {r - k + 1}\right) /r \) , en particulier on a \( E\left( {\tau }_{k}\right) = r/\left( {r - k + 1}\right) \) . Comme \( {T}_{r} = {\tau }_{1} + \cdots + {\tau }_{r} \) , on en déduit

> The random variable \( {\tau }_{k} \) is the time of the first success in a coin-tossing game, for which the probability of success is \( \left( {r - k + 1}\right) /r \) (probability that \( {X}_{{t}_{k - 1} + m} \) is one of the \( r - k + 1 \) different stickers from the \( k - 1 \) already obtained). It therefore follows a geometric distribution with parameter \( \left( {r - k + 1}\right) /r \) , in particular we have \( E\left( {\tau }_{k}\right) = r/\left( {r - k + 1}\right) \) . As \( {T}_{r} = {\tau }_{1} + \cdots + {\tau }_{r} \) , we deduce

\[
E\left( {T}_{r}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}E\left( {\tau }_{k}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}\frac{r}{r - k + 1} = r{H}_{r}.
\]

2/a) On va d’abord prouver que les \( {\tau }_{k} \) sont indépendants. La valeur de \( {\tau }_{k} \) ne dépend que des des vignettes obtenues après le moment où on a \( k - 1 \) vignettes différentes, et de celles obtenues à ce moment (pour savoir si une vignette est nouvelle). Or les tirages sont indépendants, donc les vignettes obtenues après en avoir eu \( k - 1 \) différentes sont indépendantes des précédentes, et donc de \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) . Par ailleurs, l’ensemble des \( k - 1 \) premières vignettes différentes obtenues est indépendant du temps \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) mis à les obtenir, puisque chaque type de vignette est équiprobable. Ainsi, \( {\tau }_{k} \) est indépendant de \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) . Ceci étant vrai pour tout \( k \) , on en déduit l’indépendances de \( {\tau }_{1},\ldots ,{\tau }_{r} \) .

> 2/a) We will first prove that the \( {\tau }_{k} \) are independent. The value of \( {\tau }_{k} \) depends only on the stickers obtained after the moment when one has \( k - 1 \) different stickers, and on those obtained at that moment (to know if a sticker is new). However, the draws are independent, so the stickers obtained after having had \( k - 1 \) different ones are independent of the previous ones, and therefore of \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) . Furthermore, the set of the first \( k - 1 \) different stickers obtained is independent of the time \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) taken to obtain them, since each type of sticker is equiprobable. Thus, \( {\tau }_{k} \) is independent of \( {\tau }_{1},\ldots ,{\tau }_{k - 1} \) . This being true for all \( k \) , we deduce the independence of \( {\tau }_{1},\ldots ,{\tau }_{r} \) .

L’indépendance des \( {\tau }_{k} \) permet de calculer la variance de \( {T}_{r} = {\tau }_{1} + \cdots + {\tau }_{r} \) comme somme des variances des \( {\tau }_{k} \) . Comme la variance d’une loi géométrique de paramètre \( p \) est \( \left( {1 - p}\right) /{p}^{2} \) , on en déduit

> The independence of the \( {\tau }_{k} \) allows us to calculate the variance of \( {T}_{r} = {\tau }_{1} + \cdots + {\tau }_{r} \) as the sum of the variances of the \( {\tau }_{k} \) . Since the variance of a geometric distribution with parameter \( p \) is \( \left( {1 - p}\right) /{p}^{2} \) , we deduce

\[
V\left( {T}_{r}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}V\left( {\tau }_{r}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}\frac{1 - \left( {r - k + 1}\right) /r}{{\left( r - k + 1\right) }^{2}/{r}^{2}} = \mathop{\sum }\limits_{{k = 1}}^{r}\frac{1 - k/r}{{k}^{2}/{r}^{2}} = r\mathop{\sum }\limits_{{k = 1}}^{r}\frac{r - k}{{k}^{2}} = {r}^{2}\mathop{\sum }\limits_{{k = 1}}^{r}\frac{1}{{k}^{2}} - r{H}_{r}.
\]

b) Notons que l’expression ci-dessus entraîne \( V\left( {T}_{r}\right) \leq {r}^{2}S \) avec \( S = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}1/{k}^{2} \) . L’inégalité de Bienaymé-Tchébycheff entraîne ensuite

> b) Note that the expression above implies \( V\left( {T}_{r}\right) \leq {r}^{2}S \) with \( S = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}1/{k}^{2} \) . Bienaymé-Chebyshev's inequality then implies

\[
P\left( {\left| {{T}_{r} - E\left( {T}_{r}\right) }\right|  \geq  a}\right)  \leq  \frac{V\left( {T}_{r}\right) }{{a}^{2}} \leq  \frac{{r}^{2}S}{{a}^{2}}.
\]

(*)

> Le nombre harmonique \( {H}_{r} \) est proche de \( \log r \) (on a même \( {H}_{r} = \log r + \gamma + o\left( 1\right) \) où \( \gamma \) est la constante d'Euler, ici nous nous contenterons d'une majoration simple), ce qui permet d'appro-cher \( E\left( {T}_{r}\right) \) par \( r\log r \) . Plus précisément on a

The harmonic number \( {H}_{r} \) is close to \( \log r \) (we even have \( {H}_{r} = \log r + \gamma + o\left( 1\right) \) where \( \gamma \) is the Euler constant, here we will settle for a simple upper bound), which allows us to approximate \( E\left( {T}_{r}\right) \) by \( r\log r \) . More precisely, we have

\[
\left| {E\left( {T}_{r}\right)  - r\log r}\right|  = r\left| {{H}_{r} - \log r}\right|  \leq  r\left( {1 + \mathop{\sum }\limits_{{n = 2}}^{r}{\int }_{n - 1}^{n}\left( {\frac{1}{t} - \frac{1}{n}}\right) {dt}}\right)  \leq  r\left( {1 + {\int }_{1}^{r}\frac{dt}{{t}^{2}}}\right)  \leq  {2r}.
\]

On en déduit

> We deduce

\[
\left| {{T}_{r} - r\log r}\right|  \leq  \left| {{T}_{r} - E\left( {T}_{r}\right) }\right|  + \left| {E\left( {T}_{r}\right)  - r\log r}\right|  \leq  \left| {{T}_{r} - E\left( {T}_{r}\right) }\right|  + {2r}.
\]

Donc si \( \left| {{T}_{r} - r\log r}\right| \geq {\varepsilon r}\log r \) , alors \( \left| {{T}_{r} - E\left( {T}_{r}\right) }\right| \geq {\varepsilon r}\log r - {2r} \) . En remplaçant dans (*) on obtient, lorsque \( r \) est assez grand pour que \( \varepsilon \log r - 2 > 0 \) ,

> Therefore, if \( \left| {{T}_{r} - r\log r}\right| \geq {\varepsilon r}\log r \) , then \( \left| {{T}_{r} - E\left( {T}_{r}\right) }\right| \geq {\varepsilon r}\log r - {2r} \) . Substituting into (*) we obtain, when \( r \) is large enough so that \( \varepsilon \log r - 2 > 0 \) ,

\[
P\left( {\left| {\frac{{T}_{r}}{r\log r} - 1}\right|  \geq  \varepsilon }\right)  \leq  P\left( {\left| {{T}_{r} - E\left( {T}_{r}\right) }\right|  \geq  {\varepsilon r}\log r - {2r}}\right)  \leq  \frac{S}{{\left( \varepsilon \log r - 2\right) }^{2}}.
\]

On en déduit le résultat souhaité.

> We deduce the desired result.

3/a) La forme de l'expression suggère l'utilisation de la formule du crible de Poincaré (voir la proposition 2.2 page 321). On a \( \left\{ {{T}_{r} > n}\right\} = { \cup }_{k = 1}^{r}{A}_{k} \) , avec \( {A}_{k} = \left\{ {{X}_{1} \neq k,\ldots ,{X}_{n} \neq k}\right\} \) . La formule du crible entraîne donc

> 3/a) The form of the expression suggests using the Poincaré inclusion-exclusion principle (see proposition 2.2 on page 321). We have \( \left\{ {{T}_{r} > n}\right\} = { \cup }_{k = 1}^{r}{A}_{k} \) , with \( {A}_{k} = \left\{ {{X}_{1} \neq k,\ldots ,{X}_{n} \neq k}\right\} \) . The inclusion-exclusion formula therefore implies

\[
P\left( {{T}_{r} > n}\right)  = P\left( {\mathop{\bigcup }\limits_{{i = 1}}^{r}{A}_{i}}\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , r\} } \\  {J \neq  \varnothing } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right) .
\]

Lorsque \( J \subset \{ 1,\ldots , r\} \) , on a \( { \cap }_{j \in J}{A}_{j} = \left\{ {{X}_{1} \notin J,\ldots ,{X}_{n} \notin J}\right\} \) , et comme les \( {X}_{i} \) sont indépendants on a \( P\left( {{ \cap }_{j \in J}{A}_{j}}\right) = \mathop{\prod }\limits_{{i = 1}}^{n}P\left( {{X}_{i} \notin J}\right) = {\left( 1 - \frac{\left| J\right| }{r}\right) }^{n} \) , d’où

> When \( J \subset \{ 1,\ldots , r\} \) , we have \( { \cap }_{j \in J}{A}_{j} = \left\{ {{X}_{1} \notin J,\ldots ,{X}_{n} \notin J}\right\} \) , and since the \( {X}_{i} \) are independent we have \( P\left( {{ \cap }_{j \in J}{A}_{j}}\right) = \mathop{\prod }\limits_{{i = 1}}^{n}P\left( {{X}_{i} \notin J}\right) = {\left( 1 - \frac{\left| J\right| }{r}\right) }^{n} \) , hence

\[
P\left( {{T}_{r} > n}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}\mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , r\} } \\  {\left| J\right|  = k} }}{\left( -1\right) }^{k - 1}{\left( 1 - \frac{k}{r}\right) }^{n}.
\]

Comme il y a \( \left( \begin{array}{l} r \\ k \end{array}\right) \) parties de \( \{ 1,\ldots , r\} \) à \( k \) éléments, on en déduit le résultat.

> Since there are \( \left( \begin{array}{l} r \\ k \end{array}\right) \) subsets of \( \{ 1,\ldots , r\} \) with \( k \) elements, we deduce the result.

b) Donnons l’idée de l’approche. Lorsqu’on remplace \( n \) par \( r\log r + {ar} \) dans l’expression précé- dente, chaque terme de la somme converge vers

> b) Let us outline the approach. When we replace \( n \) with \( r\log r + {ar} \) in the previous expression, each term of the sum converges to

\[
{\left( -1\right) }^{k - 1}\left( \begin{array}{l} r \\  k \end{array}\right) {e}^{-{nk}/r} \approx  {\left( -1\right) }^{k - 1}\frac{r\left( {r - 1}\right) \cdots \left( {r - k + 1}\right) }{k!}{r}^{-k}{e}^{-{ak}} \approx  {\left( -1\right) }^{k - 1}\frac{{e}^{-{ak}}}{k!},
\]

donc on s’attend à ce que \( P\left( {{T}_{r} > r\log r + {ar}}\right) \) converge vers \( \mathop{\sum }\limits_{{k > 0}}{\left( -1\right) }^{k - 1}{e}^{-{ak}}/k! = 1 - {e}^{-{e}^{-a}} \) . Cette observation nous amène à montrer que

> so we expect \( P\left( {{T}_{r} > r\log r + {ar}}\right) \) to converge to \( \mathop{\sum }\limits_{{k > 0}}{\left( -1\right) }^{k - 1}{e}^{-{ak}}/k! = 1 - {e}^{-{e}^{-a}} \) . This observation leads us to show that

\[
\forall a \in  \mathbb{R},\;\mathop{\lim }\limits_{{r \rightarrow   + \infty }}P\left( {\frac{{T}_{r} - r\log r}{r} > a}\right)  = G\left( a\right) ,\;G\left( a\right)  = 1 - {e}^{-{e}^{-a}}.
\]

\( \left( {* * }\right) \)

> Par commodité on note \( {T}_{r}^{ * } = \left( {{T}_{r} - r\log r}\right) /r \) . Si on montre (**), on aura prouvé le résultat demandé compte tenu de l'égalité

For convenience, we denote \( {T}_{r}^{ * } = \left( {{T}_{r} - r\log r}\right) /r \) . If we show (**), we will have proven the requested result given the equality

\[
P\left( {\left| {T}_{r}^{ * }\right|  < a}\right)  = P\left( {{T}_{r}^{ * } >  - a}\right)  - P\left( {{T}_{r}^{ * } \geq  a}\right)  = P\left( {{T}_{r}^{ * } >  - a}\right)  - P\left( {{T}_{r}^{ * } > a}\right)  - P\left( {{T}_{r}^{ * } = a}\right)
\]

et du fait que \( \mathop{\lim }\limits_{{r \rightarrow + \infty }}P\left( {{T}_{r}^{ * } = a}\right) = 0 \) . On prouve cette dernière assertion. Soit \( \varepsilon > 0 \) ; choisis-sons \( \alpha > 0 \) tel que \( G\left( {a - \alpha }\right) - G\left( a\right) < \varepsilon /2 \) . l’inégalité \( P\left( {{T}_{r}^{ * } = a}\right) \leq P\left( {{T}_{r}^{ * } > a - \alpha }\right) - P\left( {{T}_{r}^{ * } > a}\right) \) et la limite

> and the fact that \( \mathop{\lim }\limits_{{r \rightarrow + \infty }}P\left( {{T}_{r}^{ * } = a}\right) = 0 \) . We prove this last assertion. Let \( \varepsilon > 0 \) ; let us choose \( \alpha > 0 \) such that \( G\left( {a - \alpha }\right) - G\left( a\right) < \varepsilon /2 \) . The inequality \( P\left( {{T}_{r}^{ * } = a}\right) \leq P\left( {{T}_{r}^{ * } > a - \alpha }\right) - P\left( {{T}_{r}^{ * } > a}\right) \) and the limit

\[
\mathop{\lim }\limits_{{r \rightarrow   + \infty }}\left( {P\left( {{T}_{r}^{ * } > a - \alpha }\right)  - P\left( {{T}_{r}^{ * } > a}\right) }\right)  = G\left( {a - \alpha }\right)  - G\left( a\right)  < \varepsilon /2,
\]

entraînent que pour \( r \) assez grand, \( P\left( {{T}_{r}^{ * } = a}\right) < \varepsilon \) , on a donc bien \( \mathop{\lim }\limits_{{r \rightarrow + \infty }}P\left( {{T}_{r}^{ * } = a}\right) = 0 \) .

> imply that for \( r \) large enough, \( P\left( {{T}_{r}^{ * } = a}\right) < \varepsilon \) , so we indeed have \( \mathop{\lim }\limits_{{r \rightarrow + \infty }}P\left( {{T}_{r}^{ * } = a}\right) = 0 \) .

Montrons maintenant (**). Fixons \( a \in \mathbb{R} \) . Soit \( \varepsilon > 0 \) . On a \( {T}_{r}^{ * } > a \) si et seulement si \( {T}_{r} > {n}_{r} \) où \( {n}_{r} = \left\lbrack {r\log r + {ar}}\right\rbrack \) (où \( \left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) ). Supposons \( r \) assez grand pour que \( {n}_{r} \geq 0 \) . Soit \( k \in \mathbb{N}, k \leq r \) . La convexité de la fonction \( t \mapsto {e}^{-t} \) entraîne \( 1 - k/r \leq {e}^{-k/r} \) donc

> Let us now show (**). Let us fix \( a \in \mathbb{R} \) . Let \( \varepsilon > 0 \) . We have \( {T}_{r}^{ * } > a \) if and only if \( {T}_{r} > {n}_{r} \) where \( {n}_{r} = \left\lbrack {r\log r + {ar}}\right\rbrack \) (where \( \left\lbrack x\right\rbrack \) denotes the integer part of \( x \) ). Suppose \( r \) is large enough so that \( {n}_{r} \geq 0 \) . Let \( k \in \mathbb{N}, k \leq r \) . The convexity of the function \( t \mapsto {e}^{-t} \) implies \( 1 - k/r \leq {e}^{-k/r} \) therefore

\[
0 \leq  \left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{{n}_{r}} \leq  \left( \begin{array}{l} r \\  k \end{array}\right) {e}^{-{n}_{r}k/r} \leq  \left( \begin{array}{l} r \\  k \end{array}\right) {e}^{-\left( {r\log r + {ar} - 1}\right) k/r} = \left( \begin{array}{l} r \\  k \end{array}\right) {r}^{-k}{e}^{-{ak}}{e}^{k/r} \leq  \frac{{e}^{-{ak}}}{k!}{e}^{k/r},
\]

où nous avons utilisé l’inégalité \( \left( \begin{array}{l} r \\ k \end{array}\right) = r\left( {r - 1}\right) \cdots \left( {r - k + 1}\right) /k! \leq {r}^{k}/k! \) . Soit \( N \in {\mathbb{N}}^{ * } \) tel que \( \mathop{\sum }\limits_{{k > N}}{e}^{-{ak}}/k! < \varepsilon \) . Lorsque \( r > N \) , l’inégalité précédente entraîne

> where we used the inequality \( \left( \begin{array}{l} r \\ k \end{array}\right) = r\left( {r - 1}\right) \cdots \left( {r - k + 1}\right) /k! \leq {r}^{k}/k! \) . Let \( N \in {\mathbb{N}}^{ * } \) be such that \( \mathop{\sum }\limits_{{k > N}}{e}^{-{ak}}/k! < \varepsilon \) . When \( r > N \) , the previous inequality implies

\[
\left| {\mathop{\sum }\limits_{{k = N + 1}}^{r}{\left( -1\right) }^{k - 1}\left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{{n}_{r}} - \mathop{\sum }\limits_{{k = N + 1}}^{{+\infty }}{\left( -1\right) }^{k - 1}\frac{{e}^{-{ak}}}{k!}}\right|  \leq  \mathop{\sum }\limits_{{k = N + 1}}^{r}\frac{{e}^{-{ak}}}{k!}{e}^{k/r} + \varepsilon  \leq  {\varepsilon e} + \varepsilon .\;\left( {* *  * }\right)
\]

Fixons maintenant \( N \) , et \( k \leq N \) . On a \( {n}_{r}\log \left( {1 - k/r}\right) = \left( {r\log r + {ar} + O\left( 1\right) }\right) \left( {-k/r + O\left( {1/{r}^{2}}\right) }\right) = \; - k\log r - {ak} + O\left( {\log r/r}\right) \) donc

> Let us now fix \( N \) , and \( k \leq N \) . We have \( {n}_{r}\log \left( {1 - k/r}\right) = \left( {r\log r + {ar} + O\left( 1\right) }\right) \left( {-k/r + O\left( {1/{r}^{2}}\right) }\right) = \; - k\log r - {ak} + O\left( {\log r/r}\right) \) therefore

\[
\left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{{n}_{r}} = {e}^{-{ak} + o\left( 1\right) }\left( \begin{array}{l} r \\  k \end{array}\right) {r}^{-k} = \frac{{e}^{{ak} + o\left( 1\right) }}{k!}\frac{r}{r}\frac{r - 1}{r}\cdots \frac{r - k + 1}{r} = \frac{{e}^{{ak} + o\left( 1\right) }}{k!}\mathop{\prod }\limits_{{j = 0}}^{{k - 1}}\left( {1 - \frac{j}{r}}\right) .
\]

Donc lorsque \( r \rightarrow + \infty \) , le terme de gauche converge vers \( {e}^{-{ak}}/k \) !. Ainsi, comme \( N \) est fixé, on a

> Thus, when \( r \rightarrow + \infty \) , the term on the left converges to \( {e}^{-{ak}}/k \) !. So, as \( N \) is fixed, we have

\[
\exists {N}_{1} > N,\forall r > {N}_{1},\;\left| {\mathop{\sum }\limits_{{k = 1}}^{N}{\left( -1\right) }^{k - 1}\left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{{n}_{r}} - \mathop{\sum }\limits_{{k = 1}}^{N}{\left( -1\right) }^{k - 1}\frac{{e}^{-{ak}}}{k!}}\right|  < \varepsilon .
\]

Avec \( \left( {* * * }\right) \) on en déduit

> With \( \left( {* * * }\right) \) we deduce

\[
\forall r > {N}_{1},\;\left| {P\left( {{T}_{r}^{ * } > a}\right)  - G\left( a\right) }\right|  = \left| {\mathop{\sum }\limits_{{k = 1}}^{r}{\left( -1\right) }^{k - 1}\left( \begin{array}{l} r \\  k \end{array}\right) {\left( 1 - \frac{k}{r}\right) }^{{n}_{r}} - \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}{\left( -1\right) }^{k - 1}\frac{{e}^{-{ak}}}{k!}}\right|  < \left( {2 + e}\right) \varepsilon .
\]

On a donc bien démontré l'assertion (**).

> We have therefore indeed proven the assertion (**).

c) On a \( {e}^{-{e}^{-a}} - {e}^{-{e}^{a}} = {0.95} \) pour \( a \simeq {2.97} \) , on en déduit, d’après la question précédente, que \( P\left( {r\log r - {ar} < {T}_{r} < r\log r + {ar}}\right) \simeq {0.95} \) , donc avec \( r = {100} \) ceci fournit l’encadrement \( {163} < {T}_{r} < {758} \) , vérifié environ \( {95}\% \) du temps.

> c) We have \( {e}^{-{e}^{-a}} - {e}^{-{e}^{a}} = {0.95} \) for \( a \simeq {2.97} \) , from which we deduce, according to the previous question, that \( P\left( {r\log r - {ar} < {T}_{r} < r\log r + {ar}}\right) \simeq {0.95} \) , therefore with \( r = {100} \) this provides the bounds \( {163} < {T}_{r} < {758} \) , verified approximately \( {95}\% \) of the time.

Remarque. - On peut montrer que \( P\left( {{T}_{r} \leq n}\right) = {S}_{n, r}r!/{r}^{n} \) , où \( {S}_{n, r} \) est le nombre de Stirling de deuxième espèce (voir le problème 7 page 379).

> Remark. - It can be shown that \( P\left( {{T}_{r} \leq n}\right) = {S}_{n, r}r!/{r}^{n} \) , where \( {S}_{n, r} \) is the Stirling number of the second kind (see problem 7 page 379).

- La majoration obtenue en 2/b) fournit l’encadrement \( - {\varepsilon r}\log r < {T}_{r} - r\log r < {\varepsilon r}\log r \) avec probabilité \( > 1 - S/\left( {\varepsilon \log r - 2}\right) \) . En choisissant \( r = {100} \) et \( \varepsilon  = 1,7 \) on trouve que \( - {323} < {T}_{r} < {1244} \) au moins \( {95}\% \) du temps. La borne inférieure n’apporte rien, et cet encadrement est beaucoup moins bon que celui obtenu à la question 2/b).

> - The upper bound obtained in 2/b) provides the bounds \( - {\varepsilon r}\log r < {T}_{r} - r\log r < {\varepsilon r}\log r \) with probability \( > 1 - S/\left( {\varepsilon \log r - 2}\right) \) . By choosing \( r = {100} \) and \( \varepsilon  = 1,7 \) we find that \( - {323} < {T}_{r} < {1244} \) at least \( {95}\% \) of the time. The lower bound provides nothing, and this interval is much worse than the one obtained in question 2/b).

- La loi définie par \( P\left( {\rbrack  - \infty , x\rbrack }\right)  = {e}^{-{e}^{-x}} \) est appelée loi de Gumbel. Nous avons montré dans la question 3/b) la convergence en loi de \( \left( {{T}_{r} - r\log r}\right) /r \) vers la loi de Gumbel.

> - The distribution defined by \( P\left( {\rbrack  - \infty , x\rbrack }\right)  = {e}^{-{e}^{-x}} \) is called the Gumbel distribution. We showed in question 3/b) the convergence in distribution of \( \left( {{T}_{r} - r\log r}\right) /r \) to the Gumbel distribution.

EXERCICE 10 (RUINE DU JOUEUR). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables de Bernoulli indépendantes et identiquement distribuées, centrées, de paramètre \( p \in \rbrack 0,1\lbrack \) , c’est-à-dire \( P\left( {{X}_{n} = 1}\right) = p \) et \( P\left( {{X}_{n} = - 1}\right) = 1 - p \) . On pose \( {S}_{n} = {S}_{0} + {X}_{1} + \cdots + {X}_{n} \) . On interprète \( {S}_{n} \) comme la fortune d’un joueur qui gagne 1 euro si \( {X}_{n} = 1 \) , et qui perd 1 euro si \( {X}_{n} = - 1 \) . Le joueur part d’une fortune initiale \( {S}_{0} = k > 0 \) , et joue jusqu’à atteindre une fortune de \( N \) ou jusqu’à ce qu’il soit ruiné. On note \( T \) le plus petit entier \( n \) tel que \( {S}_{n} = 0 \) ("le joueur est ruiné") ou \( {S}_{n} = N \) ("le joueur a atteint son objectif"), \( T = + \infty \) si un tel entier n’existe pas. On note \( q = 1 - p \) .

> EXERCISE 10 (GAMBLER'S RUIN). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent and identically distributed centered Bernoulli random variables with parameter \( p \in \rbrack 0,1\lbrack \) , that is \( P\left( {{X}_{n} = 1}\right) = p \) and \( P\left( {{X}_{n} = - 1}\right) = 1 - p \) . Let \( {S}_{n} = {S}_{0} + {X}_{1} + \cdots + {X}_{n} \) . We interpret \( {S}_{n} \) as the fortune of a gambler who wins 1 euro if \( {X}_{n} = 1 \) , and loses 1 euro if \( {X}_{n} = - 1 \) . The gambler starts with an initial fortune \( {S}_{0} = k > 0 \) , and plays until reaching a fortune of \( N \) or until they are ruined. Let \( T \) be the smallest integer \( n \) such that \( {S}_{n} = 0 \) ("the gambler is ruined") or \( {S}_{n} = N \) ("the gambler has reached their goal"), \( T = + \infty \) if no such integer exists. Let \( q = 1 - p \) .

1/ Montrer que presque surement, \( T \) est fini, et que \( T \) admet une espérance.

> 1/ Show that almost surely, \( T \) is finite, and that \( T \) has an expectation.

2/ Montrer que la probabilité \( {p}_{k} = P\left( {\left( {T < + \infty ,{S}_{T} = 0}\right) \mid {S}_{0} = k}\right) \) de ruine du joueur, partant d’une fortune initiale \( k \) , vérifie

> 2/ Show that the probability \( {p}_{k} = P\left( {\left( {T < + \infty ,{S}_{T} = 0}\right) \mid {S}_{0} = k}\right) \) of the gambler's ruin, starting from an initial fortune \( k \) , satisfies

\[
\text{ Si }p = 1/2 : {p}_{k} = 1 - \frac{k}{N},\;\text{ si }p \neq  1/2 : {p}_{k} = \frac{{\left( q/p\right) }^{k} - {\left( q/p\right) }^{N}}{1 - {\left( q/p\right) }^{N}}.
\]

3/ Montrer que l’espérance \( {E}_{k} \) du temps de jeu \( T \) , lorsque le joueur part d’une fortune initiale \( k \) , vérifie

> 3/ Show that the expectation \( {E}_{k} \) of the playing time \( T \), when the player starts with an initial fortune \( k \), satisfies

\[
\text{ Si }p = 1/2 : {E}_{k} = k\left( {N - k}\right) ,\;\text{ si }p \neq  1/2 : {E}_{k} = \frac{1}{q - p}\left( {k - N\frac{1 - {\left( q/p\right) }^{k}}{1 - {\left( q/p\right) }^{N}}}\right) .
\]

et comme les \( {X}_{i} \) suivent tous une même loi et sont indépendants, \( {X}_{2} + \cdots + {X}_{k} \) suit la même loi que \( {X}_{1} + \cdots + {X}_{k - 1} \) , donc : \( P\left( {{A}_{k} \mid {X}_{1} = 1}\right) = P\left( {A}_{k + 1}\right) \) . Un raisonnement du même type fournit \( P\left( {{A}_{k} \mid {X}_{1} = - 1}\right) = P\left( {A}_{k - 1}\right) \) . On en déduit, pour tout \( k \in \mathbb{N} \) tel que \( 0 < k < N \) , l’égalité

> and since the \( {X}_{i} \) all follow the same distribution and are independent, \( {X}_{2} + \cdots + {X}_{k} \) follows the same distribution as \( {X}_{1} + \cdots + {X}_{k - 1} \), therefore: \( P\left( {{A}_{k} \mid {X}_{1} = 1}\right) = P\left( {A}_{k + 1}\right) \). A similar line of reasoning provides \( P\left( {{A}_{k} \mid {X}_{1} = - 1}\right) = P\left( {A}_{k - 1}\right) \). We deduce from this, for any \( k \in \mathbb{N} \) such that \( 0 < k < N \), the equality

\[
{p}_{k} = P\left( {A}_{k}\right)  = P\left( {{A}_{k} \mid  {X}_{1} = 1}\right) P\left( {{X}_{1} = 1}\right)  + P\left( {{A}_{k} \mid  {X}_{1} =  - 1}\right) P\left( {{X}_{1} =  - 1}\right)  = p{p}_{k + 1} + q{p}_{k - 1}.
\]

---

Solution. 1/ On va montrer que \( {S}_{n} \) a une faible probabilité de rester entre 0 et \( N \) lorsque \( n \) devient grand. Soit \( m \in {\mathbb{N}}^{ * } \) . Pour que \( T > {mN} \) il faut que \( 0 < {S}_{jN} < N \) pour tout \( j \leq m \) , en particulier on doit avoir \( \left| {{S}_{\left( {j + 1}\right) N} - {S}_{jN}}\right| < N \) pour tout \( j < m \) . Or l’événement \( {A}_{j} = \; \left\{ {\left| {{S}_{\left( {j + 1}\right) N} - {S}_{jN}}\right| < N}\right\} \) ne contient pas l’événement \( \left\{ {{X}_{{jN} + 1} = 1,\ldots ,{X}_{\left( {j + 1}\right) N} = 1}\right\} \) de probabilité \( {p}^{N} \) , donc \( P\left( {A}_{j}\right) \leq r \) avec \( r = 1 - {p}^{N} < 1 \) . Par ailleurs les événements \( {A}_{1},\ldots ,{A}_{m - 1} \) sont indépendants, car \( {A}_{j} = \left\{ {\left| {{X}_{{jN} + 1} + \cdots + {X}_{\left( {j + 1}\right) N}}\right| < N}\right\} \) et les \( {X}_{i} \) sont indépendants. On en déduit

> Solution. 1/ We will show that \( {S}_{n} \) has a low probability of remaining between 0 and \( N \) when \( n \) becomes large. Let \( m \in {\mathbb{N}}^{ * } \). For \( T > {mN} \) to hold, it is necessary that \( 0 < {S}_{jN} < N \) for all \( j \leq m \), in particular we must have \( \left| {{S}_{\left( {j + 1}\right) N} - {S}_{jN}}\right| < N \) for all \( j < m \). However, the event \( {A}_{j} = \; \left\{ {\left| {{S}_{\left( {j + 1}\right) N} - {S}_{jN}}\right| < N}\right\} \) does not contain the event \( \left\{ {{X}_{{jN} + 1} = 1,\ldots ,{X}_{\left( {j + 1}\right) N} = 1}\right\} \) of probability \( {p}^{N} \), therefore \( P\left( {A}_{j}\right) \leq r \) with \( r = 1 - {p}^{N} < 1 \). Furthermore, the events \( {A}_{1},\ldots ,{A}_{m - 1} \) are independent, because \( {A}_{j} = \left\{ {\left| {{X}_{{jN} + 1} + \cdots + {X}_{\left( {j + 1}\right) N}}\right| < N}\right\} \) and the \( {X}_{i} \) are independent. We deduce

\[
P\left( {T > {mN}}\right)  \leq  P\left( {{A}_{1} \cap  \ldots  \cap  {A}_{m - 1}}\right)  = P\left( {A}_{1}\right) \cdots P\left( {A}_{m - 1}\right)  \leq  {r}^{m - 1}.
\]

Soit \( n \in \mathbb{N}, n > M \) . On a \( n > {aM} \) avec \( a = \left\lbrack {\left( {n - 1}\right) /M}\right\rbrack \) donc \( P\left( {T = n}\right) \leq P\left( {T > {aM}}\right) \leq {r}^{a - 1} \) . Comme \( a \geq n/M - 1 \) , on a donc \( P\left( {T = n}\right) \leq \alpha {\beta }^{n} \) avec \( \alpha = 1/{r}^{2} \) et \( \beta = {r}^{1/M} < 1 \) . On en déduit \( P\left( {T = + \infty }\right) = P\left( {{ \cap }_{n \in \mathbb{N}}\{ T > n\} }\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {T > n}\right) = 0 \) , donc \( T \) est presque surement fini. On en déduit aussi que la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{nP}\left( {T = n}\right) \) est sommable, donc \( T \) admet une espérance.

> Let \( n \in \mathbb{N}, n > M \) . We have \( n > {aM} \) with \( a = \left\lbrack {\left( {n - 1}\right) /M}\right\rbrack \) so \( P\left( {T = n}\right) \leq P\left( {T > {aM}}\right) \leq {r}^{a - 1} \) . Since \( a \geq n/M - 1 \) , we have \( P\left( {T = n}\right) \leq \alpha {\beta }^{n} \) with \( \alpha = 1/{r}^{2} \) and \( \beta = {r}^{1/M} < 1 \) . We deduce \( P\left( {T = + \infty }\right) = P\left( {{ \cap }_{n \in \mathbb{N}}\{ T > n\} }\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {T > n}\right) = 0 \) , so \( T \) is almost surely finite. We also deduce that the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{nP}\left( {T = n}\right) \) is summable, so \( T \) has an expectation.

2 / Notons \( {A}_{k} \) l’événement correspondant à la ruine du joueur, partant d’une fortune initiale \( k \) , c'est-à-dire

> 2 / Let \( {A}_{k} \) be the event corresponding to the player's ruin, starting with an initial fortune \( k \) , that is to say

\[
{A}_{k} = \left\{  {\exists n \mid  k + {X}_{1} + \cdots  + {X}_{n} = 0\text{ et }\forall m < n,0 < k + {X}_{1} + \cdots  + {X}_{m} < N}\right\}
\]

de sorte que \( {p}_{k} = P\left( {A}_{k}\right) \) . Supposons \( 0 < k < N \) . On a

> so that \( {p}_{k} = P\left( {A}_{k}\right) \) . Suppose \( 0 < k < N \) . We have

\[
\left( {{A}_{k} \mid  {X}_{1} = 1}\right)  = \left\{  {\exists n \mid  k + 1 + {X}_{2} + \cdots  + {X}_{n} = 0\text{ et }\forall m < n,0 < k + 1 + {X}_{2} + \cdots  + {X}_{m} < N}\right\}
\]

---

Par ailleurs on a les conditions aux limites \( {p}_{0} = 1 \) et \( {p}_{N} = 0 \) . La relation obtenue est une relation de récurrence linéaire d’ordre 2, dont les solutions sont de la forme \( {p}_{k} = a{r}_{1}^{k} + b{r}_{2}^{k} \) lorsque l’équation caractéristique \( p{r}^{2} - r + q = 0 \) a deux racines distinctes \( r = {r}_{1} \) ou \( r = {r}_{2} \) , de la forme \( {p}_{k} = \left( {a + {kb}}\right) {r}_{1}^{n} \) si cette équation a une racine double \( r = {r}_{1} \) .

> Furthermore, we have the boundary conditions \( {p}_{0} = 1 \) and \( {p}_{N} = 0 \) . The relation obtained is a second-order linear recurrence relation, whose solutions are of the form \( {p}_{k} = a{r}_{1}^{k} + b{r}_{2}^{k} \) when the characteristic equation \( p{r}^{2} - r + q = 0 \) has two distinct roots \( r = {r}_{1} \) or \( r = {r}_{2} \) , and of the form \( {p}_{k} = \left( {a + {kb}}\right) {r}_{1}^{n} \) if this equation has a double root \( r = {r}_{1} \) .

Si \( p = 1/2 \) , l’équation caractéristique a une racine double \( {r}_{1} = 1 \) , donc \( {p}_{k} \) a la forme \( a + {bk} \) . Comme \( {p}_{0} = 1 \) et \( {p}_{N} = 0 \) , on en déduit \( a = 1 \) et \( b = - 1/N \) , donc dans ce cas, \( {p}_{k} = 1 - k/N \) . Si \( p \neq 1/2 \) , les racines de \( p{r}^{2} - r + q \) sont 1 et \( q/p \) , donc \( {p}_{k} \) a la forme \( a + b{\left( q/p\right) }^{k} \) . Les conditions aux limites \( {p}_{0} = 1 \) et \( {p}_{N} = 0 \) fournissent \( a = - {q}^{N}/\left( {{p}^{N} - {q}^{N}}\right) \) et \( b = {p}^{N}/\left( {{p}^{N} - {q}^{N}}\right) \) , et on en déduit la formule souhaitée.

> If \( p = 1/2 \) , the characteristic equation has a double root \( {r}_{1} = 1 \) , so \( {p}_{k} \) has the form \( a + {bk} \) . Since \( {p}_{0} = 1 \) and \( {p}_{N} = 0 \) , we deduce \( a = 1 \) and \( b = - 1/N \) , so in this case, \( {p}_{k} = 1 - k/N \) . If \( p \neq 1/2 \) , the roots of \( p{r}^{2} - r + q \) are 1 and \( q/p \) , so \( {p}_{k} \) has the form \( a + b{\left( q/p\right) }^{k} \) . The boundary conditions \( {p}_{0} = 1 \) and \( {p}_{N} = 0 \) provide \( a = - {q}^{N}/\left( {{p}^{N} - {q}^{N}}\right) \) and \( b = {p}^{N}/\left( {{p}^{N} - {q}^{N}}\right) \) , and we deduce the desired formula.

3 / Comme pour la question 2 /, on va déterminer une relation de récurrence sur \( {E}_{k} \) . Notons \( {T}_{k} \) la variable aléatoire \( T \) lorsque la fortune initiale du joueur est égale à \( k \) , de sorte que \( {E}_{k} = E\left( {T}_{k}\right) \) . La proposition 8 page 339 sur les espérances conditionnelles donne

> 3 / As with question 2 /, we will determine a recurrence relation for \( {E}_{k} \) . Let \( {T}_{k} \) be the random variable \( T \) when the player's initial fortune is equal to \( k \) , such that \( {E}_{k} = E\left( {T}_{k}\right) \) . Proposition 8 on page 339 regarding conditional expectations gives

\[
{E}_{k} = E\left( {T}_{k}\right)  = E\left( {{T}_{k} \mid  {X}_{1} = 1}\right) P\left( {{X}_{1} = 1}\right)  + E\left( {{T}_{k} \mid  {X}_{1} =  - 1}\right) P\left( {{X}_{1} =  - 1}\right) .
\]

(*)

> Supposons \( 0 < k < N \) . On a

Assume \( 0 < k < N \) . We have

\[
\left\{  {{T}_{k} = n \mid  {X}_{1} = 1}\right\}   = \left\{  {\inf \left\{  {j \mid  k + 1 + {X}_{2} + \cdots  + {X}_{j} \in  \{ 0, N\} }\right\}   = n}\right\}
\]

et comme \( {X}_{2} + \cdots + {X}_{j} \) suit la même loi que \( {X}_{1} + \cdots + {X}_{j - 1} \) , on en déduit

> and since \( {X}_{2} + \cdots + {X}_{j} \) follows the same distribution as \( {X}_{1} + \cdots + {X}_{j - 1} \) , we deduce

\[
P\left( {{T}_{k} = n \mid  {X}_{1} = 1}\right)  = P\left( {\inf \left\{  {j \mid  k + 1 + {X}_{1} + \cdots  + {X}_{j} \in  \{ 0, N\} }\right\}   = n - 1}\right)  = P\left( {{T}_{k + 1} = n - 1}\right) .
\]

On a donc

> We therefore have

\[
E\left( {{T}_{k} \mid  {X}_{1} = 1}\right)  = \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}{nP}\left( {{T}_{k} = n \mid  {X}_{1} = 1}\right)  = \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}{nP}\left( {{T}_{k + 1} = n - 1}\right)  = 1 + E\left( {T}_{k + 1}\right) .
\]

Un raisonnement similaire donne \( E\left( {{T}_{k} \mid {X}_{1} = - 1}\right) = 1 + E\left( {T}_{k - 1}\right) \) . Avec (*), on en déduit

> Similar reasoning gives \( E\left( {{T}_{k} \mid {X}_{1} = - 1}\right) = 1 + E\left( {T}_{k - 1}\right) \) . With (*), we deduce

\[
\forall k \in  \mathbb{N},0 < k < N,\;{E}_{k} = p\left( {1 + {E}_{k + 1}}\right)  + q\left( {1 + {E}_{k - 1}}\right) .
\]

\( \left( {* * }\right) \)

> Les conditions aux limites sont \( {E}_{0} = {E}_{N} = 0 \) . Pour abaisser l’ordre de la récurrence, on écrit l’égalité (**) sous la forme \( 1 + p\left( {{E}_{k + 1} - {E}_{k}}\right) + q\left( {{E}_{k - 1} - {E}_{k}}\right) = 0 \) , on a donc \( 1 + p{\Delta }_{k} - q{\Delta }_{k - 1} = 0 \) où \( {\Delta }_{k} = {E}_{k + 1} - {E}_{k} \) .

The boundary conditions are \( {E}_{0} = {E}_{N} = 0 \) . To lower the order of the recurrence, we write equality (**) in the form \( 1 + p\left( {{E}_{k + 1} - {E}_{k}}\right) + q\left( {{E}_{k - 1} - {E}_{k}}\right) = 0 \) , so we have \( 1 + p{\Delta }_{k} - q{\Delta }_{k - 1} = 0 \) where \( {\Delta }_{k} = {E}_{k + 1} - {E}_{k} \) .

> Lorsque \( p = 1/2 \) , la récurrence s’écrit \( 1 + \left( {{\Delta }_{k} - {\Delta }_{k - 1}}\right) /2 = 0 \) , donc \( {\Delta }_{k} - {\Delta }_{k - 1} = - 2 \) , ce qui entraîne \( {\Delta }_{k} = {\Delta }_{0} - {2k} \) . On en déduit

When \( p = 1/2 \) , the recurrence is written as \( 1 + \left( {{\Delta }_{k} - {\Delta }_{k - 1}}\right) /2 = 0 \) , so \( {\Delta }_{k} - {\Delta }_{k - 1} = - 2 \) , which leads to \( {\Delta }_{k} = {\Delta }_{0} - {2k} \) . We deduce

\[
{E}_{k} = {E}_{0} + \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\Delta }_{j} = k{\Delta }_{0} - k\left( {k - 1}\right) .
\]

Comme \( {E}_{N} = 0 \) , on trouve \( {\Delta }_{0} = N - 1 \) . Finalement on a \( {E}_{k} = k\left( {N - k}\right) \) pour \( 0 \leq k \leq N \) .

> Since \( {E}_{N} = 0 \) , we find \( {\Delta }_{0} = N - 1 \) . Finally, we have \( {E}_{k} = k\left( {N - k}\right) \) for \( 0 \leq k \leq N \) .

Lorsque \( p \neq 1/2 \) , on linéarise en recherchant \( \alpha \) tel que \( p\left( {{\Delta }_{k} - \alpha }\right) - q\left( {{\Delta }_{k - 1} - \alpha }\right) = 0 \) . Ceci est vrai pour \( \left( {-p + q}\right) \alpha = 1 \) , c’est-à-dire \( \alpha = 1/\left( {q - p}\right) \) . Donc pour \( 0 < k < N \) , on a \( {\Delta }_{k} - \alpha = \left( {q/p}\right) \left( {{\Delta }_{k - 1} - \alpha }\right) \) . Donc \( {\Delta }_{k} - \alpha = \left( {{\Delta }_{0} - \alpha }\right) {\left( q/p\right) }^{k} \) . On en déduit

> When \( p \neq 1/2 \) , we linearize by seeking \( \alpha \) such that \( p\left( {{\Delta }_{k} - \alpha }\right) - q\left( {{\Delta }_{k - 1} - \alpha }\right) = 0 \) . This is true for \( \left( {-p + q}\right) \alpha = 1 \) , that is to say \( \alpha = 1/\left( {q - p}\right) \) . So for \( 0 < k < N \) , we have \( {\Delta }_{k} - \alpha = \left( {q/p}\right) \left( {{\Delta }_{k - 1} - \alpha }\right) \) . Thus \( {\Delta }_{k} - \alpha = \left( {{\Delta }_{0} - \alpha }\right) {\left( q/p\right) }^{k} \) . We deduce

\[
{E}_{k} = {E}_{0} + \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\Delta }_{j} = \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}\left( {\alpha  + \left( {{\Delta }_{0} - \alpha }\right) {\left( \frac{q}{p}\right) }^{j}}\right)  = {k\alpha } + \left( {{\Delta }_{0} - \alpha }\right) \frac{1 - {\left( q/p\right) }^{k}}{1 - q/p}.
\]

Comme \( {E}_{N} = 0 \) , on en déduit \( {\Delta }_{0} - \alpha = - {N\alpha }\left( {1 - q/p}\right) /\left( {1 - {\left( q/p\right) }^{N}}\right) \) . On a donc

> Since \( {E}_{N} = 0 \) , we deduce \( {\Delta }_{0} - \alpha = - {N\alpha }\left( {1 - q/p}\right) /\left( {1 - {\left( q/p\right) }^{N}}\right) \) . We therefore have

\[
\forall k \in  \mathbb{N},0 \leq  k \leq  N,\;{E}_{k} = {k\alpha } - {N\alpha }\frac{1 - {\left( q/p\right) }^{k}}{1 - {\left( q/p\right) }^{N}} = \frac{1}{q - p}\left( {k - N\frac{1 - {\left( q/p\right) }^{k}}{1 - {\left( q/p\right) }^{N}}}\right) .
\]

Remarque. Cet exercice modélise un joueur au casino avec une fortune initiale \( k \) , le casino ayant une fortune \( N \) . La fortune du casino est bien plus grande que celle du joueur, donc même si \( p = 1/2 \) , le joueur est ruiné avec la probabilité \( 1 - k/N \) , proche de 1 . En jouant

> Remark. This exercise models a gambler at a casino with an initial fortune \( k \) , the casino having a fortune \( N \) . The casino's fortune is much larger than the player's, so even if \( p = 1/2 \) , the player is ruined with probability \( 1 - k/N \) , close to 1 . By playing

à la roulette, on a en fait \( p = {18}/{37} < 1/2 \) (lorsque la bille atterrit sur le " 0 ", la banque empoche toutes les mises), donc la probabilité de ruine du joueur, donnée par la deuxième formule de 2/, est encore plus importante.

> at roulette, we actually have \( p = {18}/{37} < 1/2 \) (when the ball lands on "0", the bank takes all bets), so the player's probability of ruin, given by the second formula in 2/, is even higher.

EXERCICE 11. 1/ Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires indépendantes à valeurs dans \( \mathbb{Z} \) , suivant toutes une loi de Rademacher :

> EXERCISE 11. 1/ Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent random variables taking values in \( \mathbb{Z} \), all following a Rademacher distribution:

\[
P\left( {{X}_{n} =  - 1}\right)  = \frac{1}{2},\;P\left( {{X}_{n} = 1}\right)  = \frac{1}{2}.
\]

On note \( {S}_{n} \) la variable définie par \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) . Donner un équivalent, lorsque \( n \rightarrow + \infty \) , de \( P\left( {{S}_{2n} = 0}\right) \) .

> Let \( {S}_{n} \) be the variable defined by \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \). Provide an equivalent, as \( n \rightarrow + \infty \), of \( P\left( {{S}_{2n} = 0}\right) \).

2/ (Généralisation) Soit \( K \in {\mathbb{N}}^{ * } \) . Donner un équivalent de \( P\left( {{S}_{2n} = 0}\right) \) lorsque les variables aléatoires \( {X}_{n} \) sont indépendantes,à valeurs dans \( \{ {2k} + 1 - {2K},0 \leq k < {2K}\} = \{ 1 - \; {2K},3 - {2K},\cdots ,{2K} - 1\} \) et équidistribuées, c’est-à-dire

> 2/ (Generalization) Let \( K \in {\mathbb{N}}^{ * } \). Provide an equivalent of \( P\left( {{S}_{2n} = 0}\right) \) when the random variables \( {X}_{n} \) are independent, taking values in \( \{ {2k} + 1 - {2K},0 \leq k < {2K}\} = \{ 1 - \; {2K},3 - {2K},\cdots ,{2K} - 1\} \) and identically distributed, that is

\[
\forall k \in  0,\ldots ,{2K} - 1,\;P\left( {{X}_{n} = {2k} + 1 - {2K}}\right)  = \frac{1}{2K}.
\]

Solution. 1/ On a \( {S}_{2n} = 0 \) si et seulement si il y a exactement \( n \) valeurs parmi les \( {\left( {X}_{k}\right) }_{1 \leq k \leq {2n}} \) qui sont égales à 1 (et les \( n \) autres forcément égales à-1), donc \( P\left( {{S}_{2n} = 0}\right) = {2}^{-{2n}}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \) . On obtient un équivalent de cette expression en utilisant la formule de Stirling \( m! \sim \sqrt{2\pi m}{\left( m/e\right) }^{m} \) , ce qui donne

> Solution. 1/ We have \( {S}_{2n} = 0 \) if and only if there are exactly \( n \) values among the \( {\left( {X}_{k}\right) }_{1 \leq k \leq {2n}} \) that are equal to 1 (and the \( n \) others necessarily equal to -1), so \( P\left( {{S}_{2n} = 0}\right) = {2}^{-{2n}}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \). We obtain an equivalent of this expression using Stirling's formula \( m! \sim \sqrt{2\pi m}{\left( m/e\right) }^{m} \), which gives

\[
P\left( {{S}_{2n} = 0}\right)  \sim  \frac{1}{{2}^{2n}}\sqrt{2\pi 2n}{\left( \frac{2n}{e}\right) }^{2n} \cdot  {\left( \frac{1}{\sqrt{2\pi n}}{\left( \frac{e}{n}\right) }^{n}\right) }^{2} = \frac{1}{\sqrt{\pi n}}.
\]

2/ Lorsque \( K > 1 \) , l’expression explicite de \( P\left( {{S}_{2n} = 0}\right) \) est une somme multiple et n’est pas adaptée au calcul d'un équivalent. On s'en sort en utilisant les fonctions caractéristiques (voir la définition 13 page 348). Puisque les \( {X}_{k} \) sont indépendantes et de même loi, la fonction caracté- ristique \( {\varphi }_{{S}_{2n}} \) de \( {S}_{2n} \) s’exprime sous la forme

> 2/ When \( K > 1 \), the explicit expression of \( P\left( {{S}_{2n} = 0}\right) \) is a multiple sum and is not suitable for calculating an equivalent. We get around this by using characteristic functions (see definition 13 on page 348). Since the \( {X}_{k} \) are independent and identically distributed, the characteristic function \( {\varphi }_{{S}_{2n}} \) of \( {S}_{2n} \) is expressed in the form

\[
{\varphi }_{{S}_{2n}}\left( \theta \right)  = {\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n},\;\text{ avec }\;{\varphi }_{{X}_{1}}\left( \theta \right)  = \frac{1}{2K}\mathop{\sum }\limits_{{k = 0}}^{{{2K} - 1}}{e}^{\left( {\left( {{2k} + 1}\right)  - {2K}}\right) {i\theta }},
\]

(*)

> et la formule (*) de la remarque 18 page 348 fournit l'identité

and formula (*) from remark 18 on page 348 provides the identity

\[
P\left( {{S}_{2n} = 0}\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\varphi }_{{S}_{2n}}\left( \theta \right) {d\theta } = \frac{1}{\pi }{\int }_{0}^{\pi }{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } = \frac{2}{\pi }{\int }_{0}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta }.
\]

\( \left( {* * }\right) \)

> où on a utilisé la parité de la fonction \( {2\pi } \) -périodique \( {\varphi }_{{X}_{1}} \) et l’identité \( {\varphi }_{{X}_{1}}\left( {\pi - \theta }\right) = {\varphi }_{{X}_{1}}\left( \theta \right) \) . Pour calculer un équivalent à partir de cette dernière expression, on va utiliser la méthode de Laplace (voir le tome Analyse), que nous redémontrons ici dans notre contexte. L'approche consiste à remarquer que \( {\varphi }_{{X}_{1}}\left( \theta \right) \) admet son module maximum lorsque \( \theta = 0 \) , dictant ainsi la valeur de l’intégrale. Au voisinage de \( \theta = 0\left( {\theta \neq 0}\right) \) on a

where we used the parity of the \( {2\pi } \)-periodic function \( {\varphi }_{{X}_{1}} \) and the identity \( {\varphi }_{{X}_{1}}\left( {\pi - \theta }\right) = {\varphi }_{{X}_{1}}\left( \theta \right) \). To calculate an equivalent from this last expression, we will use Laplace's method (see the Analysis volume), which we re-prove here in our context. The approach consists of noting that \( {\varphi }_{{X}_{1}}\left( \theta \right) \) reaches its maximum modulus when \( \theta = 0 \), thus dictating the value of the integral. In the neighborhood of \( \theta = 0\left( {\theta \neq 0}\right) \) we have

\[
{\varphi }_{{X}_{1}}\left( \theta \right)  = \frac{{e}^{\left( {1 - {2K}}\right) {i\theta }}}{2K}\frac{{e}^{4Ki\theta } - 1}{{e}^{2i\theta } - 1} = \frac{\sin \left( {2K\theta }\right) }{{2K}\sin \left( \theta \right) } = \frac{{2K\theta } - {\left( 2K\theta \right) }^{3}/6 + o\left( {\theta }^{3}\right) }{{2K}\left( {\theta  - {\theta }^{3}/6 + o\left( {\theta }^{3}\right) }\right) } = 1 - \alpha {\theta }^{2} + o\left( {\theta }^{2}\right) ,\left( {* *  * }\right)
\]

où \( \alpha = \left( {4{K}^{2} - 1}\right) /6 \) , on a donc \( {\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n} \approx {e}^{-{2\alpha n}{\theta }^{2}} \) et donc la dernière intégrale de (**) est approximée par \( {\int }_{0}^{\pi /2}{e}^{-{2\alpha n}{\theta }^{2}}{d\theta } \sim {\left( 2\alpha n\right) }^{-1/2}{\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} \) (par le changement de variable \( \left. {t = {\left( 2\alpha n\right) }^{1/2}\theta }\right) \) .

> where \( \alpha = \left( {4{K}^{2} - 1}\right) /6 \) , we therefore have \( {\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n} \approx {e}^{-{2\alpha n}{\theta }^{2}} \) and thus the last integral of (**) is approximated by \( {\int }_{0}^{\pi /2}{e}^{-{2\alpha n}{\theta }^{2}}{d\theta } \sim {\left( 2\alpha n\right) }^{-1/2}{\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} \) (by the change of variable \( \left. {t = {\left( 2\alpha n\right) }^{1/2}\theta }\right) \) .

Procédons maintenant rigoureusement. Soit \( \varepsilon > 0 \) . L’estimation (***) entraîne \( {\varphi }_{{X}_{1}}\left( \theta \right) = \; \left. {{e}^{-\alpha {\theta }^{2}\left( {1 + o\left( 1\right) }\right) }\text{ donc il existe }a \in }\right\rbrack 0,\pi /2\lbrack \) tel que

> Let us now proceed rigorously. Let \( \varepsilon > 0 \) . The estimate (***) implies \( {\varphi }_{{X}_{1}}\left( \theta \right) = \; \left. {{e}^{-\alpha {\theta }^{2}\left( {1 + o\left( 1\right) }\right) }\text{ donc il existe }a \in }\right\rbrack 0,\pi /2\lbrack \) such that

\[
\forall \theta  \in  \left\lbrack  {0, a}\right\rbrack  ,\;\exp \left( {-\alpha \left( {1 + \varepsilon }\right) {\theta }^{2}}\right)  \leq  {\varphi }_{{X}_{1}}\left( \theta \right)  \leq  \exp \left( {-\alpha \left( {1 - \varepsilon }\right) {\theta }^{2}}\right)
\]

donc

> therefore

\[
{\int }_{0}^{a}{e}^{-{2n\alpha }\left( {1 + \varepsilon }\right) {\theta }^{2}}{d\theta } \leq  {\int }_{0}^{a}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \leq  {\int }_{0}^{a}{e}^{-{2n\alpha }\left( {1 - \varepsilon }\right) {\theta }^{2}}{d\theta }.
\]

Un équivalent des deux intégrales qui encadrent celle du milieu est obtenu avec le résultat suivant :

> An equivalent for the two integrals bounding the middle one is obtained with the following result:

\[
\forall \beta  > 0,\;{\int }_{0}^{a}{e}^{-{n\beta }{\theta }^{2}}{d\theta } = {\left( n\beta \right) }^{-1/2}{\int }_{0}^{a{\left( n\beta \right) }^{1/2}}{e}^{-{t}^{2}}{dt} \sim  \frac{I}{{\left( n\beta \right) }^{1/2}},\;I = {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt}.
\]

En appliquant ce résultat avec \( \beta = {2\alpha }\left( {1 + \varepsilon }\right) \) puis \( \beta = {2\alpha }\left( {1 - \varepsilon }\right) \) , on en déduit l’existence de \( N \in {\mathbb{N}}^{ * } \) tel que pour tout \( n \geq N \)

> By applying this result with \( \beta = {2\alpha }\left( {1 + \varepsilon }\right) \) then \( \beta = {2\alpha }\left( {1 - \varepsilon }\right) \) , we deduce the existence of \( N \in {\mathbb{N}}^{ * } \) such that for all \( n \geq N \)

\[
\frac{I}{{\left( 2n\alpha \left( 1 + \varepsilon \right) \right) }^{1/2}}\left( {1 - \varepsilon }\right)  \leq  {\int }_{0}^{a}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \leq  \frac{I}{{\left( 2n\alpha \left( 1 - \varepsilon \right) \right) }^{1/2}}\left( {1 + \varepsilon }\right) .
\]

On majore ensuite \( \left| {{\varphi }_{{X}_{1}}\left( \theta \right) }\right| \) sur \( \left\lbrack {a,\pi /2}\right\rbrack \) à partir de son expression sous forme de somme dans (*) dont les termes d’indice \( K - 1 \) et \( K \) valent respectivement \( {e}^{-{i\theta }} \) et \( {e}^{i\theta } \) , et les autres ont leur module majorés par 1. Ceci permet d'écrire

> We then bound \( \left| {{\varphi }_{{X}_{1}}\left( \theta \right) }\right| \) on \( \left\lbrack {a,\pi /2}\right\rbrack \) using its sum expression in (*) whose terms with indices \( K - 1 \) and \( K \) are equal to \( {e}^{-{i\theta }} \) and \( {e}^{i\theta } \) respectively, and the others have their modulus bounded by 1. This allows us to write

\[
\forall \theta  \in  \left\lbrack  {a,\pi /2}\right\rbrack  ,\;\left| {{\varphi }_{{X}_{1}}\left( \theta \right) }\right|  \leq  \frac{{2K} - 2 + 2\cos \theta }{2K} \leq  q,\;\text{ avec }\;q = \frac{{2K} + 2\left( {\cos a - 1}\right) }{2K} < 1.
\]

Donc \( \left| {{\int }_{a}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta }}\right| \leq \left( {\pi /2}\right) {q}^{2n} \) , et pour tout \( n \geq N \)

> Thus \( \left| {{\int }_{a}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta }}\right| \leq \left( {\pi /2}\right) {q}^{2n} \) , and for all \( n \geq N \)

\[
\frac{I}{{\left( 2n\alpha \right) }^{1/2}}\frac{1 - \varepsilon }{{\left( 1 + \varepsilon \right) }^{1/2}} - \frac{\pi }{2}{q}^{2n} \leq  {\int }_{0}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \leq  \frac{I}{{\left( 2n\alpha \right) }^{1/2}}\frac{1 + \varepsilon }{{\left( 1 - \varepsilon \right) }^{1/2}} + \frac{\pi }{2}{q}^{2n}.
\]

Comme \( 0 < q < 1 \) , on a \( {q}^{2n} = o\left( {n}^{-1/2}\right) \) donc ceci entraîne l’existence de \( {N}_{1} \geq N \) tel que

> Since \( 0 < q < 1 \) , we have \( {q}^{2n} = o\left( {n}^{-1/2}\right) \) so this implies the existence of \( {N}_{1} \geq N \) such that

\[
\forall n \geq  {N}_{1},\;\frac{I}{{\left( 2n\alpha \right) }^{1/2}}\frac{{\left( 1 - \varepsilon \right) }^{2}}{{\left( 1 + \varepsilon \right) }^{1/2}} \leq  {\int }_{0}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \leq  \frac{I}{{\left( 2n\alpha \right) }^{1/2}}\frac{{\left( 1 + \varepsilon \right) }^{2}}{{\left( 1 - \varepsilon \right) }^{1/2}}.
\]

L’existence de \( {N}_{1} \) étant assurée pour tout \( \varepsilon > 0 \) , les deux fonctions de \( \varepsilon \) en présence étant continues en \( \varepsilon = 0 \) , on en déduit que \( {\int }_{0}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \sim I/{\left( 2n\alpha \right) }^{1/2} \) . Compte tenu de la valeur de \( \alpha = \left( {4{K}^{2} - 1}\right) /6 \) et avec (**) on en déduit

> The existence of \( {N}_{1} \) being ensured for all \( \varepsilon > 0 \) , the two functions of \( \varepsilon \) present being continuous at \( \varepsilon = 0 \) , we deduce that \( {\int }_{0}^{\pi /2}{\varphi }_{{X}_{1}}{\left( \theta \right) }^{2n}{d\theta } \sim I/{\left( 2n\alpha \right) }^{1/2} \) . Given the value of \( \alpha = \left( {4{K}^{2} - 1}\right) /6 \) and with (**) we deduce

\[
P\left( {{S}_{2n} = 0}\right)  \sim  \frac{2}{\pi }\frac{I}{{\left( \left( 4{K}^{2} - 1\right) n/3\right) }^{1/2}}.
\]

La valeur de \( I \) est classique (voir le tome Analyse), ici on peut la retrouver à partir de l’équivalent obtenu dans la question précédente, qui correspond au cas \( K = 1 \) , ce qui fournit \( {2I}/\pi = 1/\sqrt{\pi } \) , donc \( I = \sqrt{\pi }/2 \) . En conclusion on a donc

> The value of \( I \) is standard (see the Analysis volume), here it can be recovered from the equivalent obtained in the previous question, which corresponds to the case \( K = 1 \) , which provides \( {2I}/\pi = 1/\sqrt{\pi } \) , so \( I = \sqrt{\pi }/2 \) . In conclusion, we therefore have

\[
P\left( {{S}_{2n} = 0}\right)  \sim  \frac{1}{{\left( \left( 4{K}^{2} - 1\right) \pi n/3\right) }^{1/2}}.
\]

EXERCICE 12 (LOI FAIBLE DES GRANDS NOMBRES, CAS \( {\mathcal{L}}^{1} \) ). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, indépendantes, identiquement distribuées, et ad-mettant une espérance (on ne suppose pas que les \( {X}_{n} \) admettent une variance).

> EXERCISE 12 (WEAK LAW OF LARGE NUMBERS, CASE \( {\mathcal{L}}^{1} \) ). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent, identically distributed real discrete random variables admitting an expectation (we do not assume that the \( {X}_{n} \) admit a variance).

1 / Montrer que \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) converge en probabilité vers \( m = E\left( {X}_{1}\right) \) , c’est-à-dire

> 1 / Show that \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) converges in probability to \( m = E\left( {X}_{1}\right) \) , that is to say

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {\left| {\left( {{X}_{1} + \cdots  + {X}_{n}}\right) /n - m}\right|  > \varepsilon }\right)  = 0.
\]

(indication : considérer la variable aléatoire tronquée \( {Y}_{n} = {X}_{n} \times {\mathbf{1}}_{\left| {X}_{n}\right| \leq M} \) (où \( {\mathbf{1}}_{A} \) est la fonction indicatrice de \( A \) définie par \( {\mathbf{1}}_{A}\left( \omega \right) = 1 \) si \( \omega \in A, = 0 \) sinon), avec \( M \) bien choisi). 2/ Montrer que même si les \( {X}_{n} \) admettent tous une espérance,égale à \( m \) , ce résultat est faux si on ne suppose pas les \( {X}_{n} \) identiquement distribuées.

> (hint: consider the truncated random variable \( {Y}_{n} = {X}_{n} \times {\mathbf{1}}_{\left| {X}_{n}\right| \leq M} \) (where \( {\mathbf{1}}_{A} \) is the indicator function of \( A \) defined by \( {\mathbf{1}}_{A}\left( \omega \right) = 1 \) if \( \omega \in A, = 0 \) otherwise), with \( M \) well chosen). 2/ Show that even if the \( {X}_{n} \) all admit an expectation equal to \( m \) , this result is false if we do not assume the \( {X}_{n} \) are identically distributed.

Solution. 1/ Quitte à considérer la suite \( \left( {{X}_{n} - m}\right) \) , on peut supposer \( m = 0 \) . Par commodité, pour toute suite \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) de variables aléatoires réelles, on note \( {\left( {\bar{A}}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) la suite de variables aléatoires des moyennes, définie par \( {\bar{A}}_{n} = \left( {{A}_{1} + \cdots + {A}_{n}}\right) /n \) .

> Solution. 1/ Without loss of generality, considering the sequence \( \left( {{X}_{n} - m}\right) \) , we can assume \( m = 0 \) . For convenience, for any sequence \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) of real random variables, we denote by \( {\left( {\bar{A}}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) the sequence of random variables of the means, defined by \( {\bar{A}}_{n} = \left( {{A}_{1} + \cdots + {A}_{n}}\right) /n \) .

Soit \( \varepsilon > 0 \) . On suit l’indication en considèrant la variable aléatoire tronquée \( {Y}_{n} = {X}_{n}{\mathbf{1}}_{\left| {X}_{n}\right| < M} \) , où la valeur de \( M > 0 \) sera choisie plus tard. On note \( {Z}_{n} = {X}_{n} - {Y}_{n} = {X}_{n}{\mathbf{1}}_{\left| {X}_{n}\right| > M} \) . On a

> Let \( \varepsilon > 0 \) . We follow the hint by considering the truncated random variable \( {Y}_{n} = {X}_{n}{\mathbf{1}}_{\left| {X}_{n}\right| < M} \) , where the value of \( M > 0 \) will be chosen later. We denote \( {Z}_{n} = {X}_{n} - {Y}_{n} = {X}_{n}{\mathbf{1}}_{\left| {X}_{n}\right| > M} \) . We have

\[
{\bar{X}}_{n} = {\bar{X}}_{n} - E\left( {\bar{X}}_{n}\right)  = \left( {{\bar{Y}}_{n} - E\left( {\bar{Y}}_{n}\right) }\right)  + \left( {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right) .
\]

Donc si \( \left| {\bar{X}}_{n}\right| \geq {2\varepsilon } \) alors \( \left| {{\bar{Y}}_{n} - E\left( {\bar{Y}}_{n}\right) }\right| \geq \varepsilon \) ou \( \left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right| \geq \varepsilon \) , ce qui entraîne

> Therefore if \( \left| {\bar{X}}_{n}\right| \geq {2\varepsilon } \) then \( \left| {{\bar{Y}}_{n} - E\left( {\bar{Y}}_{n}\right) }\right| \geq \varepsilon \) or \( \left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right| \geq \varepsilon \) , which implies

\[
P\left( {\left| {\bar{X}}_{n}\right|  \geq  {2\varepsilon }}\right)  \leq  P\left( {\left| {{\bar{Y}}_{n} - E\left( {\bar{Y}}_{n}\right) }\right|  \geq  \varepsilon }\right)  + P\left( {\left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right|  \geq  \varepsilon }\right) .
\]

Comme \( {Y}_{k} \) est bornée,à valeur dans \( \left\lbrack {-M, M}\right\rbrack \) , elle admet un moment d’ordre 2 et sa variance vérifie \( V\left( {Y}_{k}\right) \leq E\left( {Y}_{k}^{2}\right) \leq {M}^{2} \) . En appliquant l’inégalité de Bienaymé-Tchébycheff on a donc

> Since \( {Y}_{k} \) is bounded, with values in \( \left\lbrack {-M, M}\right\rbrack \) , it admits a second-order moment and its variance satisfies \( V\left( {Y}_{k}\right) \leq E\left( {Y}_{k}^{2}\right) \leq {M}^{2} \) . By applying Bienaymé-Chebyshev's inequality we therefore have

\[
P\left( {\left| {{\bar{Y}}_{n} - E\left( {\bar{Y}}_{n}\right) }\right|  \geq  \varepsilon }\right)  \leq  \frac{V\left( {\bar{Y}}_{n}\right) }{{\varepsilon }^{2}} = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{V\left( {Y}_{k}\right) }{{n}^{2}{\varepsilon }^{2}} \leq  \frac{{M}^{2}}{n{\varepsilon }^{2}}.
\]

Par ailleurs, l'inégalité de Markov fournit

> Furthermore, Markov's inequality provides

\[
P\left( {\left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right|  \geq  \varepsilon }\right)  \leq  \frac{E\left( \left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right| \right) }{\varepsilon } \leq  \frac{{2E}\left( \left| {\bar{Z}}_{n}\right| \right) }{\varepsilon } \leq  \frac{2}{\varepsilon }\mathop{\sum }\limits_{{k = 1}}^{n}\frac{E\left( \left| {Z}_{k}\right| \right) }{n} = \frac{{2E}\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right|  \geq  M}}\right) }{\varepsilon }.
\]

On a \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) = \mathop{\sum }\limits_{{x \in {X}_{1}\left( \Omega \right) ,\left| x\right| \geq M}}\left| x\right| P\left( {{X}_{1} = x}\right) \) donc \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) \) tend vers 0 lorsque \( M \rightarrow + \infty \) . Choisissons \( M \) de sorte que \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) \leq {\varepsilon }^{2} \) . On a alors \( P\left( {\left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right| \geq }\right. \; \varepsilon ) \leq {2\varepsilon } \) . On a donc finalement montré

> We have \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) = \mathop{\sum }\limits_{{x \in {X}_{1}\left( \Omega \right) ,\left| x\right| \geq M}}\left| x\right| P\left( {{X}_{1} = x}\right) \) so \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) \) tends to 0 as \( M \rightarrow + \infty \) . Let us choose \( M \) such that \( E\left( {\left| {X}_{1}\right| {\mathbf{1}}_{\left| {X}_{1}\right| \geq M}}\right) \leq {\varepsilon }^{2} \) . We then have \( P\left( {\left| {{\bar{Z}}_{n} - E\left( {\bar{Z}}_{n}\right) }\right| \geq }\right. \; \varepsilon ) \leq {2\varepsilon } \) . We have therefore finally shown

\[
P\left( {\left| {\bar{X}}_{n}\right|  \geq  {2\varepsilon }}\right)  \leq  \frac{{M}^{2}}{n{\varepsilon }^{2}} + {2\varepsilon },
\]

donc lorsque \( n \geq {M}^{2}/{\varepsilon }^{3} \) , on a \( P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) .

> so when \( n \geq {M}^{2}/{\varepsilon }^{3} \) , we have \( P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) .

Fixons nous maintenant \( \delta > 0 \) . Soit \( \varepsilon > 0,\varepsilon \leq \delta /2 \) . D’après ce que nous venons de montrer, il existe \( N \in {\mathbb{N}}^{ * } \) tel que pour tout \( n \geq N \) , on a \( P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) . On en déduit que pour \( n \geq N, P\left( {\left| {\bar{X}}_{n}\right| \geq \delta }\right) \leq P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) . On a donc bien \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {\bar{X}}_{n}\right| \geq \delta }\right) = 0 \) .

> Let us now fix \( \delta > 0 \) . Let \( \varepsilon > 0,\varepsilon \leq \delta /2 \) . According to what we have just shown, there exists \( N \in {\mathbb{N}}^{ * } \) such that for all \( n \geq N \) , we have \( P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) . We deduce from this that for \( n \geq N, P\left( {\left| {\bar{X}}_{n}\right| \geq \delta }\right) \leq P\left( {\left| {\bar{X}}_{n}\right| \geq {2\varepsilon }}\right) \leq {3\varepsilon } \) . We therefore indeed have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {\bar{X}}_{n}\right| \geq \delta }\right) = 0 \) .

2 / Considérons une suite de variables aléatoires \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) indépendantes vérifiant \( P\left( {{X}_{n} = - 1}\right) = \; 1 - 1/{n}^{2} \) et \( P\left( {{X}_{n} = {n}^{2} - 1}\right) = 1/{n}^{2} \) . Pour tout \( n \) on a \( E\left( {X}_{n}\right) = 0 \) et

> 2 / Consider a sequence of independent random variables \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) satisfying \( P\left( {{X}_{n} = - 1}\right) = \; 1 - 1/{n}^{2} \) and \( P\left( {{X}_{n} = {n}^{2} - 1}\right) = 1/{n}^{2} \) . For all \( n \) we have \( E\left( {X}_{n}\right) = 0 \) and

\[
P\left( {{X}_{1} = 0,{X}_{2} =  - 1,\ldots ,{X}_{n} =  - 1}\right)  = \mathop{\prod }\limits_{{k = 2}}^{n}\left( {1 - \frac{1}{{k}^{2}}}\right)  = {e}^{-\left( {{u}_{2} + \cdots  + {u}_{n}}\right) },\;{u}_{k} = \log \left( \frac{1}{1 - 1/{k}^{2}}\right) .
\]

La série à termes positifs \( \sum {u}_{k} \) converge car \( {u}_{k} \sim 1/{k}^{2} \) . En notant \( S \) sa somme on a donc

> The series with positive terms \( \sum {u}_{k} \) converges because \( {u}_{k} \sim 1/{k}^{2} \) . By denoting \( S \) its sum we therefore have

\[
\forall n \in  {\mathbb{N}}^{ * },\;P\left( {{X}_{1} + \cdots  + {X}_{n} = 1 - n}\right)  \geq  P\left( {{X}_{1} = 0,{X}_{2} =  - 1,\ldots ,{X}_{n} =  - 1}\right)  \geq  {e}^{-S}.
\]

Donc \( P\left( {\left| {\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n)}\right| \geq 1/2}\right) \geq P\left( {{X}_{1} + \cdots + {X}_{n} = 1 - n}\right) \geq {e}^{-S} \) ne tend pas vers 0 . Le résultat \( 1/ \) est donc faux avec \( \varepsilon = 1/2 \) .

> Therefore \( P\left( {\left| {\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n)}\right| \geq 1/2}\right) \geq P\left( {{X}_{1} + \cdots + {X}_{n} = 1 - n}\right) \geq {e}^{-S} \) does not tend to 0 . The result \( 1/ \) is therefore false with \( \varepsilon = 1/2 \) .

Remarque. Même si les \( {X}_{n} \) ne sont pas identiquement distribuées, le résultat 1/ reste vrai si on suppose que les \( {X}_{n} \) ont la même espérance, et sont equi-sommables, c’est-à-dire si \( \forall \varepsilon > 0,\exists M > 0,\forall n \in {\mathbb{N}}^{ * }, E\left( {\left| {X}_{n} \mid {\mathbf{1}}_{\left| {X}_{n}\right| \geq M}) \leq \varepsilon .\right| }^{2}\right) \)

> Remark. Even if the \( {X}_{n} \) are not identically distributed, the result 1/ remains true if we assume that the \( {X}_{n} \) have the same expectation and are equi-integrable, that is to say if \( \forall \varepsilon > 0,\exists M > 0,\forall n \in {\mathbb{N}}^{ * }, E\left( {\left| {X}_{n} \mid {\mathbf{1}}_{\left| {X}_{n}\right| \geq M}) \leq \varepsilon .\right| }^{2}\right) \)

EXERCICE 13 (LOI FORTE DES GRANDS NOMBRES, CAS \( {\mathcal{L}}^{4} \) ). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, indépendantes. On suppose que les \( {X}_{n} \) admettent toutes un moment d’ordre 4 et sont centrées, et qu’il existe \( K > 0 \) tel que \( E\left( {X}_{n}^{4}\right) \leq K \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> EXERCISE 13 (STRONG LAW OF LARGE NUMBERS, CASE \( {\mathcal{L}}^{4} \) ). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent real discrete random variables. We assume that the \( {X}_{n} \) all admit a moment of order 4 and are centered, and that there exists \( K > 0 \) such that \( E\left( {X}_{n}^{4}\right) \leq K \) for all \( n \in {\mathbb{N}}^{ * } \) .

1 / Montrer que chaque \( {X}_{k} \) admet des moments d’ordre 1,2 et 3 . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) , montrer que

> 1/ Show that each \( {X}_{k} \) admits moments of order 1, 2, and 3. For all \( n \in {\mathbb{N}}^{ * } \) , we denote \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) , show that

\[
E\left( {S}_{n}^{4}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}E\left( {X}_{i}^{4}\right)  + 3\mathop{\sum }\limits_{{1 \leq  i, j \leq  n, i \neq  j}}E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) ,
\]

---

puis montrer que \( E\left( {S}_{n}^{4}\right) \leq 3{n}^{2}K \) .

> then show that \( E\left( {S}_{n}^{4}\right) \leq 3{n}^{2}K \) .

2/ En déduire que pour tout \( \varepsilon > 0,\mathop{\sum }\limits_{n}P\left( {\left| {{S}_{n}/n}\right| > \varepsilon }\right) \) converge, puis que presque sur-

> 2/ Deduce that for all \( \varepsilon > 0,\mathop{\sum }\limits_{n}P\left( {\left| {{S}_{n}/n}\right| > \varepsilon }\right) \) converges, then that almost sure-

ement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) .

> ly, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) .

---

Solution. 1/ Comme vu dans la remarque 8 page 339, l’inégalité \( {\left| {X}_{k}\right| }^{m} \leq 1 + {\left| {X}_{k}\right| }^{4} \) pour \( 1 \leq m \leq 3 \) montre que \( {X}_{k} \) admet bien un moment d’ordre 1,2 et 3 . Montrons maintenant l'identité demandée. On a

> Solution. 1/ As seen in remark 8 on page 339, the inequality \( {\left| {X}_{k}\right| }^{m} \leq 1 + {\left| {X}_{k}\right| }^{4} \) for \( 1 \leq m \leq 3 \) shows that \( {X}_{k} \) indeed admits a moment of order 1, 2, and 3. Let us now show the requested identity. We have

\[
E\left( {S}_{n}^{4}\right)  = \mathop{\sum }\limits_{{1 \leq  {i}_{1},{i}_{2},{i}_{3},{i}_{4} \leq  n}}E\left( {{X}_{{i}_{1}}{X}_{{i}_{2}}{X}_{{i}_{3}}{X}_{{i}_{4}}}\right) .
\]

(*)

> S’il existe \( k \in \{ 1,2,3,4\} \) tel que \( {i}_{k} \) n’apparait qu’une fois parmi \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \) , alors \( {X}_{{i}_{k}} \) est indé- pendant de \( \mathop{\prod }\limits_{{j \neq k}}{X}_{{i}_{j}} \) , donc \( E\left( {{X}_{{i}_{1}}{X}_{{i}_{2}}{X}_{{i}_{3}}{X}_{{i}_{4}}}\right) = E\left( {X}_{{i}_{k}}\right) E\left( {\mathop{\prod }\limits_{{j \neq k}}{X}_{{i}_{j}}}\right) = 0 \) . On peut donc retirer dans la somme (*) tous les termes dont un (au moins) des indices \( {i}_{k} \) n’apparait qu’une fois parmi \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \) . Il ne reste donc que les termes pour lesquels chaque indice \( {i}_{k} \) apparait au moins deux fois parmi \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \) . Ces indices sont soit de la forme \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, i, i, i}\right) \) avec \( 1 \leq i \leq n \) , soit de la forme \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, i, j, j}\right) \) avec \( i \neq j \) , soit \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, j, i, j}\right) \) avec \( i \neq j \) , soit \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, j, j, i}\right) \) avec \( i \neq j \) . En résumé on a donc

If there exists \( k \in \{ 1,2,3,4\} \) such that \( {i}_{k} \) appears only once among \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \), then \( {X}_{{i}_{k}} \) is independent of \( \mathop{\prod }\limits_{{j \neq k}}{X}_{{i}_{j}} \), thus \( E\left( {{X}_{{i}_{1}}{X}_{{i}_{2}}{X}_{{i}_{3}}{X}_{{i}_{4}}}\right) = E\left( {X}_{{i}_{k}}\right) E\left( {\mathop{\prod }\limits_{{j \neq k}}{X}_{{i}_{j}}}\right) = 0 \). We can therefore remove from the sum (*) all terms for which one (at least) of the indices \( {i}_{k} \) appears only once among \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \). Only the terms for which each index \( {i}_{k} \) appears at least twice among \( {i}_{1},{i}_{2},{i}_{3},{i}_{4} \) remain. These indices are either of the form \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, i, i, i}\right) \) with \( 1 \leq i \leq n \), or of the form \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, i, j, j}\right) \) with \( i \neq j \), or \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, j, i, j}\right) \) with \( i \neq j \), or \( \left( {{i}_{1},{i}_{2},{i}_{3},{i}_{4}}\right) = \left( {i, j, j, i}\right) \) with \( i \neq j \). In summary, we therefore have

\[
E\left( {S}_{n}^{4}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}E\left( {X}_{i}^{4}\right)  + 3\mathop{\sum }\limits_{{1 \leq  i, j \leq  n, i \neq  j}}E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) .
\]

\( \left( {* * }\right) \)

> Lorsque \( i \neq j \) , l’indépendance de \( {X}_{i} \) et \( {X}_{j} \) entraîne \( E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) = E\left( {X}_{i}^{2}\right) E\left( {X}_{j}^{2}\right) \) . Comme \( E{\left( {X}_{i}^{2}\right) }^{2} \leq \; E\left( {X}_{i}^{4}\right) \left( {\operatorname{car}E\left( {X}_{i}^{4}\right) - E{\left( {X}_{i}^{2}\right) }^{2} = V\left( {X}_{i}^{2}\right) \geq 0}\right) \) , on en déduit \( E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) \leq E{\left( {X}_{i}^{4}\right) }^{1/2}E{\left( {X}_{j}^{4}\right) }^{1/2} \leq K \) . Finalement (**) donne \( E\left( {S}_{n}^{4}\right) \leq {nK} + {3n}\left( {n - 1}\right) K \leq 3{n}^{2}K \) .

When \( i \neq j \), the independence of \( {X}_{i} \) and \( {X}_{j} \) implies \( E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) = E\left( {X}_{i}^{2}\right) E\left( {X}_{j}^{2}\right) \). Since \( E{\left( {X}_{i}^{2}\right) }^{2} \leq \; E\left( {X}_{i}^{4}\right) \left( {\operatorname{car}E\left( {X}_{i}^{4}\right) - E{\left( {X}_{i}^{2}\right) }^{2} = V\left( {X}_{i}^{2}\right) \geq 0}\right) \), we deduce \( E\left( {{X}_{i}^{2}{X}_{j}^{2}}\right) \leq E{\left( {X}_{i}^{4}\right) }^{1/2}E{\left( {X}_{j}^{4}\right) }^{1/2} \leq K \). Finally, (**) gives \( E\left( {S}_{n}^{4}\right) \leq {nK} + {3n}\left( {n - 1}\right) K \leq 3{n}^{2}K \).

> 2 / L'inégalité de Markov et le résultat de la question précédente permet d'écrire, pour tout \( \varepsilon > 0 \)

2 / Markov's inequality and the result of the previous question allow us to write, for any \( \varepsilon > 0 \)

\[
P\left( {\left| \frac{{S}_{n}}{n}\right|  > \varepsilon }\right)  = P\left( {{\left( \frac{{S}_{n}}{n}\right) }^{4} > {\varepsilon }^{4}}\right)  \leq  \frac{E\left( {\left( {S}_{n}/n\right) }^{4}\right) }{{\varepsilon }^{4}} \leq  \frac{3K}{{n}^{2}{\varepsilon }^{4}},
\]

donc la série \( \sum P\left( {\left| {{S}_{n}/n}\right| > \varepsilon }\right) \) converge. Le lemme de Borel Cantelli nous assure donc l’existence d’un événement presque sûr \( A\left( \varepsilon \right) \) sur lequel il n’y a qu’un nombre fini de \( n \) tel que \( \left| {{S}_{n}/n}\right| > \varepsilon \) . L’événement \( A = { \cap }_{p \in {\mathbb{N}}^{ * }}A\left( {1/p}\right) \) , intersection dénombrable d’événements presque sûrs, est presque sûr, et sur \( A \) on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) (pour tout \( \varepsilon > 0 \) , choisissons \( p \in {\mathbb{N}}^{ * } \) tel que \( 1/p < \varepsilon \) ; l’inclusion \( {A}_{p} \subset A \) entraîne qu’il n’y a qu’un nombre fini de \( n \) tel que \( \left| {{S}_{n}/n}\right| > 1/p \) , donc il existe \( N \in {\mathbb{N}}^{ * } \) tel que pour \( n \geq N,\left| {{S}_{n}/n}\right| \leq 1/p < \varepsilon ) \) .

> so the series \( \sum P\left( {\left| {{S}_{n}/n}\right| > \varepsilon }\right) \) converges. The Borel-Cantelli lemma therefore ensures the existence of an almost sure event \( A\left( \varepsilon \right) \) on which there are only a finite number of \( n \) such that \( \left| {{S}_{n}/n}\right| > \varepsilon \) . The event \( A = { \cap }_{p \in {\mathbb{N}}^{ * }}A\left( {1/p}\right) \) , a countable intersection of almost sure events, is almost sure, and on \( A \) we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{n}/n = 0 \) (for any \( \varepsilon > 0 \) , let us choose \( p \in {\mathbb{N}}^{ * } \) such that \( 1/p < \varepsilon \) ; the inclusion \( {A}_{p} \subset A \) implies that there are only a finite number of \( n \) such that \( \left| {{S}_{n}/n}\right| > 1/p \) , so there exists \( N \in {\mathbb{N}}^{ * } \) such that for \( n \geq N,\left| {{S}_{n}/n}\right| \leq 1/p < \varepsilon ) \) .

Remarque. Ce résultat est plus fort que celui obtenu à la question 2/ de l'exercice 7 page 352 dans le cas des variables aléatoires bornées (toute variable aléatoire bornée admet un moment d'ordre 4).

> Remark. This result is stronger than the one obtained in question 2/ of exercise 7 on page 352 in the case of bounded random variables (any bounded random variable admits a 4th order moment).
