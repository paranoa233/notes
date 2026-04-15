#### 5.1. Trigonometric series

*Français : 5.1. Séries trigonométriques*

##### Trigonometric polynomials.

*Français : Polynômes trigonométriques.*

DéFINITION 1. On appelle polynôme trigonométrique de degré \( \leq N\left( {N \in \mathbb{N}}\right) \) de la variable réelle \( x \) toute fonction de la forme \( x \mapsto \mathop{\sum }\limits_{{n = - N}}^{N}{c}_{n}{e}^{inx}\left( {{c}_{n} \in \mathbb{C}}\right) \) .

> DEFINITION 1. A trigonometric polynomial of degree \( \leq N\left( {N \in \mathbb{N}}\right) \) in the real variable \( x \) is any function of the form \( x \mapsto \mathop{\sum }\limits_{{n = - N}}^{N}{c}_{n}{e}^{inx}\left( {{c}_{n} \in \mathbb{C}}\right) \) .

Compte tenu de la relation \( {e}^{inx} = \cos {nx} + i\sin {nx} \) , il revient au même de dire qu’un po-lynôme trigonométrique est une fonction de la forme \( x \mapsto \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{N}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) où les \( {a}_{n},{b}_{n} \) sont des nombres complexes reliés aux coefficients \( {c}_{n} \) par

> Given the relation \( {e}^{inx} = \cos {nx} + i\sin {nx} \) , it is equivalent to say that a trigonometric polynomial is a function of the form \( x \mapsto \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{N}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) where the \( {a}_{n},{b}_{n} \) are complex numbers related to the coefficients \( {c}_{n} \) by

\[
\forall m \in  \mathbb{N},\;{a}_{m} = {c}_{m} + {c}_{-m}\;\text{ et }\;\forall m \in  {\mathbb{N}}^{ * },\;{b}_{m} = i\left( {{c}_{m} - {c}_{-m}}\right) .
\]

Remarque 1. Un polynôme trigonométrique \( P : x \mapsto \mathop{\sum }\limits_{{-N}}^{N}{c}_{n}{e}^{inx} \) est une fonction continue \( {2\pi } \) -périodique. On a pour tout \( n \) la relation \( {c}_{n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( x\right) {e}^{-{inx}}{dx} \) , qui montre que \( P \) est nul si et seulement si \( {c}_{n} = 0 \) pour tout \( n \) .

> Remark 1. A trigonometric polynomial \( P : x \mapsto \mathop{\sum }\limits_{{-N}}^{N}{c}_{n}{e}^{inx} \) is a continuous \( {2\pi } \) -periodic function. For all \( n \) , we have the relation \( {c}_{n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( x\right) {e}^{-{inx}}{dx} \) , which shows that \( P \) is zero if and only if \( {c}_{n} = 0 \) for all \( n \) .

##### Trigonometric series.

*Français : Séries trigonométriques.*

DÉFINITION 2. On appelle série trigonométrique une série de fonctions de la variable réelle \( x \) de la forme \( {c}_{0} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{c}_{n}{e}^{inx} + {c}_{-n}{e}^{-{inx}}}\right) \) ; on la note \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) .

> DEFINITION 2. A trigonometric series is a series of functions of the real variable \( x \) of the form \( {c}_{0} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{c}_{n}{e}^{inx} + {c}_{-n}{e}^{-{inx}}}\right) \) ; it is denoted by \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) .

Compte tenu de la relation \( {e}^{inx} = \cos {nx} + i\sin {nx} \) , il revient au même de dire qu’une série trigonométrique est une série de fonctions de la forme \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) où les \( {a}_{n},{b}_{n} \) sont des nombres complexes reliés aux coefficients \( {c}_{n} \) par les relations vues précédemment.

> Given the relation \( {e}^{inx} = \cos {nx} + i\sin {nx} \) , it is equivalent to say that a trigonometric series is a series of functions of the form \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) where the \( {a}_{n},{b}_{n} \) are complex numbers related to the coefficients \( {c}_{n} \) by the relations seen previously.

Remarque 2. La série trigonométrique \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converge si et seulement si la suite de fonctions des sommes partielles \( {\left( \mathop{\sum }\limits_{{n = - N}}^{N}{c}_{n}{e}^{inx}\right) }_{N} \) converge, et dans ce cas, la somme de la série est notée \( \mathop{\sum }\limits_{{n = - \infty }}^{{+\infty }}{c}_{n}{e}^{inx} \) (convention de Cauchy). Avec cette convention, la série \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) peut converger sans que \( \mathop{\lim }\limits_{\substack{{p \rightarrow + \infty } \\ {q \rightarrow - \infty } }}\mathop{\sum }\limits_{{n = q}}^{p}{c}_{n}{e}^{inx} \) existe.

> Remark 2. The trigonometric series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converges if and only if the sequence of partial sum functions \( {\left( \mathop{\sum }\limits_{{n = - N}}^{N}{c}_{n}{e}^{inx}\right) }_{N} \) converges, and in this case, the sum of the series is denoted by \( \mathop{\sum }\limits_{{n = - \infty }}^{{+\infty }}{c}_{n}{e}^{inx} \) (Cauchy convention). With this convention, the series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) can converge even if \( \mathop{\lim }\limits_{\substack{{p \rightarrow + \infty } \\ {q \rightarrow - \infty } }}\mathop{\sum }\limits_{{n = q}}^{p}{c}_{n}{e}^{inx} \) does not exist.

Proposition 1. \( {Si}\mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {c}_{n}\right| \) et \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {c}_{-n}\right| \) (resp \( \sum \left| {a}_{n}\right| \) et \( \sum \left| {b}_{n}\right| \) ) convergent, la série trigonométrique

> Proposition 1. \( {Si}\mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {c}_{n}\right| \) and \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {c}_{-n}\right| \) (resp. \( \sum \left| {a}_{n}\right| \) and \( \sum \left| {b}_{n}\right| \)) converge, the trigonometric series

\[
\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{c}_{n}{e}^{inx}\;\left( {\text{ resp. }\;\frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) }\right)
\]

(*)

> converge normalement sur \( \mathbb{R} \) . Sa somme définit une fonction continue et \( {2\pi } \) -périodique sur \( \mathbb{R} \) .

converges normally on \( \mathbb{R} \). Its sum defines a continuous and \( {2\pi } \)-periodic function on \( \mathbb{R} \).

> Proposition 2. Si les suites \( {\left( {c}_{n}\right) }_{n \in \mathbb{N}} \) et \( {\left( {c}_{-n}\right) }_{n \in \mathbb{N}} \) (resp. \( \left( {a}_{n}\right) \) et \( \left( {b}_{n}\right) \) ) sont réelles, décrois-santes et tendent vers 0, alors la série trigonométrique (*) converge simplement sur \( \mathbb{R} \smallsetminus {2\pi }\mathbb{Z} \) , et uniformément sur tout intervalle de la forme \( \left\lbrack {{2k\pi } + \alpha ,2\left( {k + 1}\right) \pi - \alpha }\right\rbrack \) (avec \( 0 < \alpha < \pi \) et \( k \in \mathbb{Z} \) ).

Proposition 2. If the sequences \( {\left( {c}_{n}\right) }_{n \in \mathbb{N}} \) and \( {\left( {c}_{-n}\right) }_{n \in \mathbb{N}} \) (resp. \( \left( {a}_{n}\right) \) and \( \left( {b}_{n}\right) \)) are real, decreasing, and tend to 0, then the trigonometric series (*) converges pointwise on \( \mathbb{R} \smallsetminus {2\pi }\mathbb{Z} \), and uniformly on any interval of the form \( \left\lbrack {{2k\pi } + \alpha ,2\left( {k + 1}\right) \pi - \alpha }\right\rbrack \) (with \( 0 < \alpha < \pi \) and \( k \in \mathbb{Z} \)).

> Démonstration. Il suffit de montrer la convergence uniforme sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha > 0 \) fixé. Pour tout \( n \in \mathbb{N} \) , on note \( {E}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{e}^{ikx} \) . On a

Proof. It suffices to show uniform convergence on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for any fixed \( \alpha > 0 \). For any \( n \in \mathbb{N} \), we denote \( {E}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{e}^{ikx} \). We have

\[
\forall x \in  \left\lbrack  {\alpha ,{2\pi } - \alpha }\right\rbrack  ,\;\left| {{E}_{n}\left( x\right) }\right|  = \left| \frac{1 - {e}^{i\left( {n + 1}\right) x}}{1 - {e}^{ix}}\right|  \leq  \frac{2}{\left| 1 - {e}^{ix}\right| } = \frac{1}{\left| \sin \left( x/2\right) \right| } \leq  \frac{1}{\sin \left( {\alpha /2}\right) }.
\]

(**)

> Maintenant, une transformation d'Abel fournit

Now, an Abel transformation provides

\[
\forall x \in  \left\lbrack  {\alpha ,{2\pi } - \alpha }\right\rbrack  ,\;{S}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{c}_{k}{e}^{ikx} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {{c}_{k} - {c}_{k + 1}}\right) {E}_{k}\left( x\right)  + {c}_{n}{E}_{n}\left( x\right) .
\]

\( \left( {* * * }\right) \)

> D’après (**) et la décroissance de \( \left( {c}_{n}\right) \) , la série \( \sum \left( {{c}_{k} - {c}_{k + 1}}\right) {E}_{k}\left( x\right) \) converge normalement sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) . Par ailleurs, d’après (**) et le fait que \( {c}_{n} \rightarrow 0 \) , la suite de fonctions \( \left( {{c}_{n}{E}_{n}\left( x\right) }\right) \) converge uniformément vers 0 . On en conclut avec (***) que

According to (**) and the decreasing nature of \( \left( {c}_{n}\right) \), the series \( \sum \left( {{c}_{k} - {c}_{k + 1}}\right) {E}_{k}\left( x\right) \) converges normally on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \). Furthermore, according to (**) and the fact that \( {c}_{n} \rightarrow 0 \), the sequence of functions \( \left( {{c}_{n}{E}_{n}\left( x\right) }\right) \) converges uniformly to 0. We conclude with (***) that

\[
\text{ la série de fonctions }\mathop{\sum }\limits_{{n \in  \mathbb{N}}}{c}_{n}{e}^{inx}\text{ converge uniformément sur }\left\lbrack  {\alpha ,{2\pi } - \alpha }\right\rbrack  \text{ . }
\]

\( \left( {* * * * }\right) \)

> Par symétrie, la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{-n}{e}^{-{inx}} \) converge aussi uniformément sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) . On en déduit que \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converge uniformément sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) . Ceci est vrai pour tout \( \alpha \in \rbrack 0,\pi \lbrack \) , on en conclut qu’il y a convergence simple sur \( \rbrack 0,{2\pi }\lbrack \) .

By symmetry, the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{-n}{e}^{-{inx}} \) also converges uniformly on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \). We deduce that \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converges uniformly on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \). This is true for any \( \alpha \in \rbrack 0,\pi \lbrack \), so we conclude that there is pointwise convergence on \( \rbrack 0,{2\pi }\lbrack \).

> En prenant respectivement les parties réelles et imaginaires de la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}{e}^{inx} \) , on en déduit avec (****) que les séries \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}\cos {nx} \) et \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}\sin {nx} \) convergent uniformément sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha > 0 \) dès que \( \left( {c}_{n}\right) \) est une suite réelle décroissante qui tend vers 0 . Ainsi, la série \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) converge uniformément sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha > 0 \) , d'où le résultat.

By taking the real and imaginary parts of the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}{e}^{inx} \) respectively, we deduce with (****) that the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}\cos {nx} \) and \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{c}_{n}\sin {nx} \) converge uniformly on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for any \( \alpha > 0 \) as soon as \( \left( {c}_{n}\right) \) is a decreasing real sequence that tends to 0. Thus, the series \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) converges uniformly on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for any \( \alpha > 0 \), hence the result.

> Remarque 3. On peut montrer que si une série trigonométrique \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converge simplement sur \( \mathbb{R} \) , alors \( {c}_{n} \rightarrow 0 \) lorsque \( \left| n\right| \rightarrow + \infty \) (théorème de Cantor-Lebesgue, voir la question 2/ du problème 29 page 312). Si de plus la limite simple de cette série est nulle en tout point, alors \( {c}_{n} = 0 \) pour tout \( n \) (théorème de Cantor, voir la question \( 3/ \) du même problème).

Remark 3. It can be shown that if a trigonometric series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}{e}^{inx} \) converges pointwise on \( \mathbb{R} \), then \( {c}_{n} \rightarrow 0 \) as \( \left| n\right| \rightarrow + \infty \) (Cantor-Lebesgue theorem, see question 2/ of problem 29 on page 312). If, moreover, the pointwise limit of this series is zero at every point, then \( {c}_{n} = 0 \) for all \( n \) (Cantor's theorem, see question \( 3/ \) of the same problem).
