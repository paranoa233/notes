#### 1.3. Some classic families of sequences

*Français : 1.3. Quelques familles de suites classiques*

Suites arithmétiques. On appelle ainsi les suites \( \left( {u}_{n}\right) \) à valeurs dans un e.v \( E \) vérifiant une relation de récurrence de la forme \( {u}_{n + 1} = {u}_{n} + a \) où \( a \in E \) . On a alors \( {u}_{n} = {u}_{0} + {na} \) pour tout \( n \in \mathbb{N} \) , et on dit que \( \left( {u}_{n}\right) \) est une suite arithmétique de raison a.

> Arithmetic sequences. These are sequences \( \left( {u}_{n}\right) \) with values in a v.s. \( E \) satisfying a recurrence relation of the form \( {u}_{n + 1} = {u}_{n} + a \) where \( a \in E \) . We then have \( {u}_{n} = {u}_{0} + {na} \) for all \( n \in \mathbb{N} \) , and we say that \( \left( {u}_{n}\right) \) is an arithmetic sequence with common difference a.

Suites géométriques. Ce sont les suites à valeurs réelles (ou complexes) vérifiant une relation de récurrence de la forme \( {u}_{n + 1} = q{u}_{n} \) . On a alors \( {u}_{n} = {q}^{n}{u}_{0} \) pour tout \( n \in \mathbb{N} \) et on dit que \( \left( {u}_{n}\right) \) est une suite géométrique de raison \( q \) . Si \( \left| q\right| > 1 \) , la suite \( \left( {u}_{n}\right) \) diverge; si \( \left| q\right| < 1 \) , elle converge et a pour limite 0 ; si \( q = 1 \) , elle est constante.

> Geometric sequences. These are sequences with real (or complex) values satisfying a recurrence relation of the form \( {u}_{n + 1} = q{u}_{n} \) . We then have \( {u}_{n} = {q}^{n}{u}_{0} \) for all \( n \in \mathbb{N} \) and we say that \( \left( {u}_{n}\right) \) is a geometric sequence with common ratio \( q \) . If \( \left| q\right| > 1 \) , the sequence \( \left( {u}_{n}\right) \) diverges; if \( \left| q\right| < 1 \) , it converges and has a limit of 0; if \( q = 1 \) , it is constant.

Suites arithmético-géométriques. Ce sont les suites à valeurs réelles (ou complexes) vérifiant une relation de récurrence de la forme \( {u}_{n + 1} = q{u}_{n} + a \) . Lorsque \( q = 1 \) on a affaire à une suite arithmétique, et si \( q \neq 1 \) , on a

> Arithmetico-geometric sequences. These are sequences with real (or complex) values satisfying a recurrence relation of the form \( {u}_{n + 1} = q{u}_{n} + a \) . When \( q = 1 \) we are dealing with an arithmetic sequence, and if \( q \neq 1 \) , we have

\[
\forall n \in  \mathbb{N},\;{u}_{n} = {q}^{n}\left( {{u}_{0} - r}\right)  + r\;\text{ avec }\;r = \frac{a}{1 - q}.
\]

Récurrences homographiques. On dit qu’une suite \( \left( {u}_{n}\right) \) (réelle ou complexe) vérifie une récurrence homographique si elle vérifie une relation de récurrence du type

> Homographic recurrences. A sequence \( \left( {u}_{n}\right) \) (real or complex) is said to satisfy a homographic recurrence if it satisfies a recurrence relation of the type

\[
\forall n \in  \mathbb{N},\;{u}_{n + 1} = h\left( {u}_{n}\right) \;\text{ avec }\;h\left( x\right)  = \frac{{ax} + b}{{cx} + d},\;{ad} - {bc} \neq  0.
\]

(*)

> Une telle suite est définie pour tout \( n \) si et seulement si aucune de ses valeurs n’annule le dénominateur de \( h \) . La proposition qui suit permet d’exprimer explicitement \( {u}_{n} \) .

Such a sequence is defined for all \( n \) if and only if none of its values make the denominator of \( h \) zero. The following proposition allows us to explicitly express \( {u}_{n} \) .

> Proposition 2. Soit \( \left( {u}_{n}\right) \) une suite complexe vérifiant (*). On considère l’équation

Proposition 2. Let \( \left( {u}_{n}\right) \) be a complex sequence satisfying (*). Consider the equation

\[
h\left( x\right)  = x\; \Leftrightarrow  \;c{x}^{2} - \left( {a - d}\right) x - b = 0. \tag{E}
\]

- Si (E) admet deux racines distinctes \( \alpha ,\beta \) alors on a

> - If (E) admits two distinct roots \( \alpha ,\beta \) then we have

\[
\forall n \in  \mathbb{N},\;\frac{{u}_{n} - \alpha }{{u}_{n} - \beta } = {k}^{n}\frac{{u}_{0} - \alpha }{{u}_{0} - \beta }\;\text{ où }\;k = \frac{a - {\alpha c}}{a - {\beta c}}.
\]

\( - {Si}\left( E\right) \) admet une racine double \( \alpha \) , alors

> \( - {Si}\left( E\right) \) admits a double root \( \alpha \) , then

\[
\forall n \in  \mathbb{N},\;\frac{1}{{u}_{n} - \alpha } = \frac{1}{{u}_{0} - \alpha } + {kn}\;\text{ où }\;k = \frac{c}{a - {\alpha c}}.
\]

Démonstration. Dans le premier cas, il suffit de remarquer que

> Proof. In the first case, it suffices to note that

\[
\frac{h\left( x\right)  - \alpha }{h\left( x\right)  - \beta } = k\frac{x - \alpha }{x - \beta },
\]

ce que le lecteur vérifiera facilement. Dans le second cas, il suffit de remarquer

> which the reader will easily verify. In the second case, it suffices to note

\[
\frac{1}{h\left( x\right)  - \alpha } = \frac{1}{x - \alpha } + k
\]

Remarque 1. Ces formules permettent de décider s’il existe un entier \( n \) qui annule le dénominateur de \( h \) , en quel cas les termes ultérieurs de la suite ne sont pas définis.

> Remark 1. These formulas allow us to decide if there exists an integer \( n \) that makes the denominator of \( h \) zero, in which case the subsequent terms of the sequence are undefined.

- On peut montrer que si (E) a deux racines distinctes, la valeur \( k \) est aussi égale à \( k = \frac{{c\beta } + d}{{c\alpha } + d} \) ; lorsque \( \left( E\right) \) a une racine double, on a l’égalité \( k = \frac{2c}{a + d} \) .

> - It can be shown that if (E) has two distinct roots, the value \( k \) is also equal to \( k = \frac{{c\beta } + d}{{c\alpha } + d} \) ; when \( \left( E\right) \) has a double root, we have the equality \( k = \frac{2c}{a + d} \) .

Récurrences linéaires à coefficients constants. On dit qu'une suite \( \left( {u}_{n}\right) \) à valeurs complexes vérifie une récurrence linéaire (homogène) d'ordre \( h \) à coefficients constants si

> Linear recurrences with constant coefficients. A complex-valued sequence \( \left( {u}_{n}\right) \) is said to satisfy a linear (homogeneous) recurrence of order \( h \) with constant coefficients if

\[
\forall n \geq  h,\;{u}_{n} = {a}_{1}{u}_{n - 1} + {a}_{2}{u}_{n - 2} + \cdots  + {a}_{h}{u}_{n - h}\;\left( {{a}_{1},\ldots ,{a}_{h} \in  \mathbb{C}}\right) .
\]

(*)

> La proposition qui suit permet de calculer explicitement le terme général d'une telle suite.

The following proposition allows us to explicitly calculate the general term of such a sequence.

> Proposition 3. L'équation

Proposition 3. The equation

\[
{x}^{h} - {a}_{1}{x}^{h - 1} - \cdots  - {a}_{h} = 0 \tag{E}
\]

s’appelle équation caractéristique de la récurrence (*). Si on note \( {r}_{1},\ldots ,{r}_{q} \) ses racines et \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) leur ordre de multiplicité respectifs, alors l’ensemble des suites \( \left( {u}_{n}\right) \) vérifiant (*) est l'ensemble des suites de la forme

> is called the characteristic equation of the recurrence (*). If we denote its roots by \( {r}_{1},\ldots ,{r}_{q} \) and their respective multiplicities by \( {\alpha }_{1},\ldots ,{\alpha }_{q} \), then the set of sequences \( \left( {u}_{n}\right) \) satisfying (*) is the set of sequences of the form

\[
{u}_{n} = {P}_{1}\left( n\right) {r}_{1}^{n} + \cdots  + {P}_{q}\left( n\right) {r}_{q}^{n},
\]

\( \left( {* * }\right) \)

> où pour tout \( i,{P}_{i} \) est un polynôme vérifiant \( \deg \left( {P}_{i}\right) < {\alpha }_{i} \) .

where for all \( i,{P}_{i} \) is a polynomial satisfying \( \deg \left( {P}_{i}\right) < {\alpha }_{i} \) .

> Une preuve de ce résultat fait l'objet du problème 5 page 285. Dans la pratique, si on se donne une suite \( \left( {u}_{n}\right) \) vérifiant (*), les coefficients des polynômes \( {P}_{i} \) correspondant dans (**) sont déterminés à partir des \( h \) premiers termes \( {u}_{0},\ldots ,{u}_{h - 1} \) de la suite.

A proof of this result is the subject of problem 5 on page 285. In practice, if we are given a sequence \( \left( {u}_{n}\right) \) satisfying (*), the coefficients of the corresponding polynomials \( {P}_{i} \) in (**) are determined from the first \( h \) terms \( {u}_{0},\ldots ,{u}_{h - 1} \) of the sequence.

> Remarque 2. On rencontre souvent des récurrences linéaires à coefficients constants d'or-dre 2 :

Remark 2. We often encounter second-order linear recurrences with constant coefficients:

\[
{u}_{0},{u}_{1},\;\forall n \geq  2,\;{u}_{n} = a{u}_{n - 1} + b{u}_{n - 2}.
\]

(***)

> L'équation caractéristique correspondante est

The corresponding characteristic equation is

\[
{x}^{2} - {ax} - b = 0, \tag{E}
\]

et dans ce cas, la proposition précédente s'énonce comme suit.

> and in this case, the previous proposition is stated as follows.

- Si \( \left( E\right) \) possède deux racines distinctes \( {x}_{1},{x}_{2} \) , les suites vérifiant (***) sont celles de la forme

> - If \( \left( E\right) \) has two distinct roots \( {x}_{1},{x}_{2} \) , the sequences satisfying (***) are those of the form

\[
{u}_{n} = \lambda {x}_{1}^{n} + \mu {x}_{2}^{n}.
\]

\( \left( {* * * * }\right) \)

> Les coefficients \( \lambda \) et \( \mu \) sont déterminés à partir des équations \( {u}_{0} = \lambda + \mu \) et \( {u}_{1} = \; \lambda {x}_{1} + \mu {x}_{2} \) .

The coefficients \( \lambda \) and \( \mu \) are determined from the equations \( {u}_{0} = \lambda + \mu \) and \( {u}_{1} = \; \lambda {x}_{1} + \mu {x}_{2} \) .

> - Si \( \left( E\right) \) possède une racine double \( x \) , les suites vérifiant (***) sont celles de la forme

- If \( \left( E\right) \) has a double root \( x \) , the sequences satisfying (***) are those of the form

\[
{u}_{n} = \left( {{\lambda n} + \mu }\right) {x}^{n}.
\]

On détermine \( \lambda \) et \( \mu \) grâce aux équations \( {u}_{0} = \mu \) et \( {u}_{1} = \left( {\lambda + \mu }\right) x \) .

> We determine \( \lambda \) and \( \mu \) using the equations \( {u}_{0} = \mu \) and \( {u}_{1} = \left( {\lambda + \mu }\right) x \) .

Lorsque \( a \) et \( b \) sont réels et que le discriminant \( \Delta = {a}^{2} + {4b} \) de \( \left( E\right) \) est strictement négatif, l'expression (****) fait intervenir des nombres complexes. Dans ce cas, on peut en donner une expression ne faisant intervenir que des nombres réels en écrivant les racines de \( \left( E\right) \) sont la forme \( \rho {e}^{i\theta },\rho {e}^{-{i\theta }} \) , de sorte que (****) se met sous la forme

> When \( a \) and \( b \) are real and the discriminant \( \Delta = {a}^{2} + {4b} \) of \( \left( E\right) \) is strictly negative, the expression (****) involves complex numbers. In this case, we can provide an expression involving only real numbers by writing the roots of \( \left( E\right) \) in the form \( \rho {e}^{i\theta },\rho {e}^{-{i\theta }} \) , so that (****) takes the form

\[
{u}_{n} = {\rho }^{n}\left( {\gamma \cos \left( {n\theta }\right)  + \delta \sin \left( {n\theta }\right) }\right) .
\]
