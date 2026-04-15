#### 3.2. Other applications

*Français : 3.2. Autres applications*

Il existe une multitude de résultats qui peuvent être prouvés grâce à la théorie des invariants de similitude. Par exemple :

> There is a multitude of results that can be proven using the theory of similarity invariants. For example:

- Dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \left( {n = 2\text{ ou }n = 3}\right) \) , deux matrices sont semblables si et seulement si elles ont même polynôme minimal et même polynôme caractéristique (ce résultat est faux dès que \( n \geq  4 \) ).

> - In \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \left( {n = 2\text{ ou }n = 3}\right) \), two matrices are similar if and only if they have the same minimal polynomial and the same characteristic polynomial (this result is false as soon as \( n \geq  4 \)).

- Si \( \mathbb{L} \) est un surcorps commutatif de \( \mathbb{K} \) , si \( A, B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) sont semblables sur \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) , alors \( A \) et \( B \) sont semblables sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . En effet, en vertu de l’unicité, les invariants de similitude dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) sont les invariants de similitude dans \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) (car de plus, le polynôme minimal d’une matrice de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est le même dans \( \mathbb{K}\left\lbrack  X\right\rbrack \) ou dans \( \mathbb{L}\left\lbrack  X\right\rbrack \) ). Ce résultat généralise celui de l’exercice 14 de la page 167.

> - If \( \mathbb{L} \) is a commutative extension field of \( \mathbb{K} \), if \( A, B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) are similar over \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \), then \( A \) and \( B \) are similar over \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). Indeed, by virtue of uniqueness, the similarity invariants in \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) are the similarity invariants in \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) (since, moreover, the minimal polynomial of a matrix of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is the same in \( \mathbb{K}\left\lbrack  X\right\rbrack \) or in \( \mathbb{L}\left\lbrack  X\right\rbrack \)). This result generalizes that of exercise 14 on page 167.

- Si \( f \in  \mathcal{L}\left( E\right) \) et si les seuls endomorphismes commutant avec \( f \) sont des polynômes en \( f \) , alors \( f \) est cyclique. En effet, si tel n’est pas le cas, on a \( \deg \left( {\Pi }_{f}\right)  < n \) donc le nombre \( r \) d’invariants de similitude de \( f \) vérifie \( r \geq  2 \) . Avec les notations du théorème 1, on peut écrire \( E = {F}_{1} \oplus  G \) où \( G = {F}_{2} \oplus  \cdots  \oplus  {F}_{r} \neq  \{ 0\} \) . Si on note \( p \) la projection sur \( G \) parallèlement à \( {F}_{1}, p \) et \( f \) commutent (car \( {F}_{1} \) et \( G \) sont stables par \( f) \) . Si on avait \( p = Q\left( f\right) \) avec \( Q \in  \mathbb{K}\left\lbrack  X\right\rbrack \) , comme \( {p}_{\mid {F}_{1}} = 0 \) on en déduirait \( Q\left( {f}_{\mid {F}_{1}}\right)  = 0 \) , donc \( {\Pi }_{f} = {\Pi }_{{f}_{\mid {F}_{1}}} \) divise \( Q \) , et donc \( p = Q\left( f\right)  = 0 \) , ce qui est absurde. Ceci constitue la réciproque de la question 2/ de l'exercice 6 de la page 191.

> - If \( f \in  \mathcal{L}\left( E\right) \) and if the only endomorphisms commuting with \( f \) are polynomials in \( f \), then \( f \) is cyclic. Indeed, if this is not the case, we have \( \deg \left( {\Pi }_{f}\right)  < n \) so the number \( r \) of similarity invariants of \( f \) satisfies \( r \geq  2 \). With the notation of theorem 1, we can write \( E = {F}_{1} \oplus  G \) where \( G = {F}_{2} \oplus  \cdots  \oplus  {F}_{r} \neq  \{ 0\} \). If we denote by \( p \) the projection onto \( G \) parallel to \( {F}_{1}, p \) and \( f \) commute (because \( {F}_{1} \) and \( G \) are stable by \( f) \). If we had \( p = Q\left( f\right) \) with \( Q \in  \mathbb{K}\left\lbrack  X\right\rbrack \), as \( {p}_{\mid {F}_{1}} = 0 \) we would deduce \( Q\left( {f}_{\mid {F}_{1}}\right)  = 0 \), so \( {\Pi }_{f} = {\Pi }_{{f}_{\mid {F}_{1}}} \) divides \( Q \), and thus \( p = Q\left( f\right)  = 0 \), which is absurd. This constitutes the converse of question 2/ of exercise 6 on page 191.

Annexe C

> Appendix C

##### Continued fractions

*Français : Fractions continues*

Nous proposons ici une introduction aux fractions continues, qui décrivent un moyen simple de générer les meilleurs approximants fractionnaires d'un nombre réel irrationnel. Dans une deuxième partie, nous caractérisons les fractions continues périodiques.

> We offer here an introduction to continued fractions, which describe a simple way to generate the best fractional approximants of an irrational real number. In a second part, we characterize periodic continued fractions.

Problem 1 (FRACTIONS CONTINUES). Étant donnée une suite réelle \( \left( {a}_{n}\right) \) , avec \( {a}_{n} > 0 \) pour \( n > 0 \) , on appelle fraction continue l’expression

> Problem 1 (CONTINUED FRACTIONS). Given a real sequence \( \left( {a}_{n}\right) \), with \( {a}_{n} > 0 \) for \( n > 0 \), a continued fraction is the expression

\[
\left\lbrack  {{a}_{0},{a}_{1},\ldots ,{a}_{n}}\right\rbrack   = {a}_{0} + \frac{1}{{a}_{1} + \frac{1}{{a}_{2} + }}
\]

\[
\begin{array}{l}  \ddots  \; + \frac{1}{{a}_{n - 1} + \frac{1}{{a}_{n}}} \\  \end{array}
\]

De manière équivalente, on définit les fractions continues par \( \left\lbrack {a}_{0}\right\rbrack = {a}_{0},\left\lbrack {{a}_{0},{a}_{1}}\right\rbrack = {a}_{0} + 1/{a}_{1} \) et par la récurrence

> Equivalently, we define continued fractions by \( \left\lbrack {a}_{0}\right\rbrack = {a}_{0},\left\lbrack {{a}_{0},{a}_{1}}\right\rbrack = {a}_{0} + 1/{a}_{1} \) and by the recurrence

\[
\forall n \geq  2,\;\left\lbrack  {{a}_{0},\ldots ,{a}_{n}}\right\rbrack   = \left\lbrack  {{a}_{0},\ldots ,{a}_{n - 2},{a}_{n - 1} + \frac{1}{{a}_{n}}}\right\rbrack  .
\]

(*)

> 1/ (Développement en fraction continue d’un nombre irrationnel). Soit \( \xi \) un nombre réel irrationnel. Partant de \( {\xi }_{0} = \xi \) , on définit les suites \( \left( {a}_{n}\right) \) et \( \left( {\xi }_{n}\right) \) par la relation de récurrence

1/ (Continued fraction expansion of an irrational number). Let \( \xi \) be an irrational real number. Starting from \( {\xi }_{0} = \xi \), we define the sequences \( \left( {a}_{n}\right) \) and \( \left( {\xi }_{n}\right) \) by the recurrence relation

\[
\forall n \in  \mathbb{N},\;{a}_{n} = \left\lbrack  {\xi }_{n}\right\rbrack  ,\;{\xi }_{n + 1} = \frac{1}{{\xi }_{n} - {a}_{n}},
\]

où pour tout \( x \in \mathbb{R},\left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) . La valeur \( {a}_{n} \) s’appelle quotient incomplet d’indice \( n \) , et \( {\xi }_{n} \) le quotient complet d’indice \( n \) .

> where for all \( x \in \mathbb{R},\left\lbrack x\right\rbrack \) denotes the integer part of \( x \). The value \( {a}_{n} \) is called the incomplete quotient of index \( n \), and \( {\xi }_{n} \) the complete quotient of index \( n \).

a) Montrer que les suites \( \left( {a}_{n}\right) \) et \( \left( {\xi }_{n}\right) \) sont bien définies, que \( {a}_{n} > 0 \) et \( {\xi }_{n} > 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) et que de plus

> a) Show that the sequences \( \left( {a}_{n}\right) \) and \( \left( {\xi }_{n}\right) \) are well-defined, that \( {a}_{n} > 0 \) and \( {\xi }_{n} > 0 \) for all \( n \in {\mathbb{N}}^{ * } \) and that furthermore

\[
\forall n \in  {\mathbb{N}}^{ * },\;\xi  = \left\lbrack  {{a}_{0},\ldots ,{a}_{n - 1},{\xi }_{n}}\right\rbrack  .
\]

b) On définit les suites \( \left( {p}_{n}\right) \) et \( \left( {q}_{n}\right) \) par

> b) We define the sequences \( \left( {p}_{n}\right) \) and \( \left( {q}_{n}\right) \) by

\[
{p}_{0} = {a}_{0},\;{p}_{1} = {a}_{1}{a}_{0} + 1,\;{p}_{n} = {a}_{n}{p}_{n - 1} + {p}_{n - 2},
\]

\[
{q}_{0} = 1,\;{q}_{1} = {a}_{1},\;{q}_{n} = {a}_{n}{q}_{n - 1} + {q}_{n - 2}.
\]

Montrer que

> Show that

\[
\forall n \geq  2,\forall x > 0,\;\left\lbrack  {{a}_{0},\ldots ,{a}_{n - 1}, x}\right\rbrack   = \frac{{p}_{n - 1}x + {p}_{n - 2}}{{q}_{n - 1}x + {q}_{n - 2}}.
\]

c) Montrer que les valeurs \( \left\lbrack {{a}_{0},\ldots ,{a}_{n}}\right\rbrack \) (appelées réduites de \( \xi \) ) vérifient

> c) Show that the values \( \left\lbrack {{a}_{0},\ldots ,{a}_{n}}\right\rbrack \) (called convergents of \( \xi \)) satisfy

\[
\forall n \in  \mathbb{N},\;\left\lbrack  {{a}_{0},\ldots ,{a}_{n}}\right\rbrack   = \frac{{p}_{n}}{{q}_{n}}.
\]

d) Montrer que pour tout \( n \in {\mathbb{N}}^{ * } \) , on a la relation \( {p}_{n}{q}_{n - 1} - {p}_{n - 1}{q}_{n} = {\left( -1\right) }^{n - 1} \) .

> d) Show that for all \( n \in {\mathbb{N}}^{ * } \), the relation \( {p}_{n}{q}_{n - 1} - {p}_{n - 1}{q}_{n} = {\left( -1\right) }^{n - 1} \) holds.

e) Montrer que pour tout \( n \in \mathbb{N},{p}_{n}/{q}_{n} \) est une fraction irréductible.

> e) Show that for all \( n \in \mathbb{N},{p}_{n}/{q}_{n} \) is an irreducible fraction.

f) Montrer

> f) Show

\[
\forall n \in  {\mathbb{N}}^{ * },\;\xi  - \frac{{p}_{n}}{{q}_{n}} = \frac{{\left( -1\right) }^{n}}{{q}_{n}\left( {{q}_{n - 1} + {q}_{n}{\xi }_{n + 1}}\right) }.
\]

En déduire que les réduites \( {p}_{n}/{q}_{n} \) sont des approximations fractionnaires de \( \xi \) qui vérifient

> Deduce that the convergents \( {p}_{n}/{q}_{n} \) are fractional approximations of \( \xi \) that satisfy

\[
\left| {\xi  - \frac{{p}_{n}}{{q}_{n}}}\right|  < \frac{1}{{q}_{n}^{2}}
\]

g) Montrer que sur deux réduites consécutives, il en existe une qui vérifie

> g) Show that among two consecutive convergents, there exists one that satisfies

\[
\left| {\xi  - \frac{{p}_{n}}{{q}_{n}}}\right|  < \frac{1}{2{q}_{n}^{2}}
\]

h) Montrer que pour tout \( n \in {\mathbb{N}}^{ * } \) on a

> h) Show that for all \( n \in {\mathbb{N}}^{ * } \) we have

\[
\forall \left( {p, q}\right)  \in  {\mathbb{Z}}^{2},0 < q \leq  {q}_{n},\;\left| {{q\xi } - p}\right|  \geq  \left| {{q}_{n}\xi  - {p}_{n}}\right| .
\]

On dit alors que la réduite \( {p}_{n}/{q}_{n} \) est une meilleure approximation fractionnaire de \( \xi \) .

> We then say that the convergent \( {p}_{n}/{q}_{n} \) is a best fractional approximation of \( \xi \).

2/ (Fractions continues périodiques). On rappelle qu’un nombre \( \xi \in \mathbb{R} \) est quadratique s’il est racine d’un polynôme de degré 2 à coefficients entiers et irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . a) Montrer qu'un nombre quadratique est irrationnel.

> 2/ (Periodic continued fractions). Recall that a number \( \xi \in \mathbb{R} \) is quadratic if it is a root of a degree 2 polynomial with integer coefficients that is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \). a) Show that a quadratic number is irrational.

b) Soit \( \xi \in \mathbb{R} \) un nombre irrationnel et \( \left( {a}_{n}\right) \) et \( \left( {\xi }_{n}\right) \) les suites de quotients incomplets et complets associés au développement en fraction continue de \( \xi \) . Montrer que le dévelop-pement en fractions continues de \( \xi \) est périodique à partir d’un certain rang (c’est-à-dire qu’il existe \( T \in {\mathbb{N}}^{ * } \) et \( r \in \mathbb{N} \) tel que \( {a}_{k + T} = {a}_{k} \) pour tout \( k \geq r \) ) si et seulement s’il existe \( T \in {\mathbb{N}}^{ * } \) et \( r \in \mathbb{N} \) tels que \( {\xi }_{r} = {\xi }_{r + T} \) .

> b) Let \( \xi \in \mathbb{R} \) be an irrational number and \( \left( {a}_{n}\right) \) and \( \left( {\xi }_{n}\right) \) be the sequences of partial and complete quotients associated with the continued fraction expansion of \( \xi \). Show that the continued fraction expansion of \( \xi \) is periodic from a certain point (i.e., there exist \( T \in {\mathbb{N}}^{ * } \) and \( r \in \mathbb{N} \) such that \( {a}_{k + T} = {a}_{k} \) for all \( k \geq r \)) if and only if there exist \( T \in {\mathbb{N}}^{ * } \) and \( r \in \mathbb{N} \) such that \( {\xi }_{r} = {\xi }_{r + T} \).

c) Montrer que si le développement en fraction continue d’un nombre irrationnel \( \xi \in \mathbb{R} \) est périodique à partir d’un certain rang, alors \( \xi \) est quadratique.

> c) Show that if the continued fraction expansion of an irrational number \( \xi \in \mathbb{R} \) is periodic from a certain point, then \( \xi \) is quadratic.

d) Soit \( \xi \in \mathbb{R} \) quadratique et \( Q = \alpha {X}^{2} + {\beta X} + \gamma \in \mathbb{Z}\left\lbrack X\right\rbrack \left( {\alpha \neq 0}\right) \) tel que \( Q\left( \xi \right) = 0 \) .

> d) Let \( \xi \in \mathbb{R} \) be quadratic and \( Q = \alpha {X}^{2} + {\beta X} + \gamma \in \mathbb{Z}\left\lbrack X\right\rbrack \left( {\alpha \neq 0}\right) \) such that \( Q\left( \xi \right) = 0 \).

(i) Montrer que le quotient partiel \( {\xi }_{n} \) d’indice \( n \) est racine du polynôme

> (i) Show that the partial quotient \( {\xi }_{n} \) of index \( n \) is a root of the polynomial

\[
{Q}_{n}\left( X\right)  = {\left( {q}_{n - 1}X + {q}_{n - 2}\right) }^{2}Q\left( \frac{{p}_{n - 1}X + {p}_{n - 2}}{{q}_{n - 1}X + {q}_{n - 2}}\right) ,
\]

(où \( {p}_{n} \) et \( {q}_{n} \) sont les entiers définis en 1/b) associés au développement en fraction continue de \( \xi \) ). Montrer que \( {Q}_{n} \) et \( Q \) ont même discriminant, puis montrer que les polynômes \( {Q}_{n} \) sont en nombre fini.

> (where \( {p}_{n} \) and \( {q}_{n} \) are the integers defined in 1/b) associated with the continued fraction expansion of \( \xi \)). Show that \( {Q}_{n} \) and \( Q \) have the same discriminant, then show that the polynomials \( {Q}_{n} \) are finite in number.

(ii) Montrer que le développement en fraction continue de \( \xi \) est périodique à partir d’un certain rang. b) On procède par récurrence sur \( n \geq 2 \) . Pour \( n = 2 \) le résultat est vrai car

> (ii) Show that the continued fraction expansion of \( \xi \) is periodic from a certain point. b) We proceed by induction on \( n \geq 2 \). For \( n = 2 \) the result is true because

\[
\forall x > 0,\;\left\lbrack  {{a}_{0},{a}_{1}, x}\right\rbrack   = {a}_{0} + \frac{1}{{a}_{1} + 1/x} = {a}_{0} + \frac{x}{{a}_{1}x + 1} = \frac{{a}_{0}{a}_{1}x + {a}_{0} + x}{{a}_{1}x + 1} = \frac{{p}_{1}x + {p}_{0}}{{q}_{1}x + {q}_{0}}.
\]

---

Solution. 1/ a) L’existence des suites \( \left( {a}_{n}\right) \) et \( \left( {\xi }_{n}\right) \) revient à montrer que \( {\xi }_{n} - {a}_{n} \) ne s’annule jamais. Ceci découle du fait que \( {\xi }_{n} \) est un nombre irrationnel, propriété que l’on obtient immé- diatement par récurrence sur \( n \) .

> Solution. 1/ a) The existence of the sequences \( \left( {a}_{n}\right) \) and \( \left( {\xi }_{n}\right) \) amounts to showing that \( {\xi }_{n} - {a}_{n} \) never vanishes. This follows from the fact that \( {\xi }_{n} \) is an irrational number, a property obtained immediately by induction on \( n \).

On a bien \( {a}_{n} > 0 \) et \( {\xi }_{n} > 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) car comme \( {a}_{n - 1} \) est la partie entière du nombre irrationnel \( {\xi }_{n - 1} \) , on a \( 0 < {\xi }_{n - 1} - {a}_{n - 1} < 1 \) donc \( {\xi }_{n} = 1/\left( {{\xi }_{n - 1} - {a}_{n - 1}}\right) > 1 \) et donc \( {a}_{n} = \left\lbrack {\xi }_{n}\right\rbrack \geq 1 \) .

> We have \( {a}_{n} > 0 \) and \( {\xi }_{n} > 0 \) for all \( n \in {\mathbb{N}}^{ * } \) because since \( {a}_{n - 1} \) is the integer part of the irrational number \( {\xi }_{n - 1} \), we have \( 0 < {\xi }_{n - 1} - {a}_{n - 1} < 1 \) thus \( {\xi }_{n} = 1/\left( {{\xi }_{n - 1} - {a}_{n - 1}}\right) > 1 \) and therefore \( {a}_{n} = \left\lbrack {\xi }_{n}\right\rbrack \geq 1 \).

Il reste à démontrer l’égalité \( \xi = \left\lbrack {{a}_{0},\ldots ,{a}_{n - 1},{\xi }_{n}}\right\rbrack \) . Nous procédons par récurrence sur \( n \) . Pour \( n = 1 \) , c’est vrai car

> It remains to prove the equality \( \xi = \left\lbrack {{a}_{0},\ldots ,{a}_{n - 1},{\xi }_{n}}\right\rbrack \). We proceed by induction on \( n \). For \( n = 1 \), it is true because

\[
\left\lbrack  {{a}_{0},{\xi }_{1}}\right\rbrack   = {a}_{0} + \frac{1}{{\xi }_{1}} = {a}_{0} + \left( {{\xi }_{0} - {a}_{0}}\right)  = {\xi }_{0} = \xi .
\]

Supposons maintenant le résultat vrai au rang \( n \) , de sorte que \( \xi = \left\lbrack {{a}_{0},\ldots ,{a}_{n - 1},{\xi }_{n}}\right\rbrack \) . Comme \( {\xi }_{n + 1} = 1/\left( {{\xi }_{n} - {a}_{n}}\right) \) , on a \( {\xi }_{n} = {a}_{n} + 1/{\xi }_{n + 1} \) , et en appliquant (*), on obtient

> Now assume the result is true at rank \( n \), such that \( \xi = \left\lbrack {{a}_{0},\ldots ,{a}_{n - 1},{\xi }_{n}}\right\rbrack \). Since \( {\xi }_{n + 1} = 1/\left( {{\xi }_{n} - {a}_{n}}\right) \), we have \( {\xi }_{n} = {a}_{n} + 1/{\xi }_{n + 1} \), and by applying (*), we obtain

\[
\xi  = \left\lbrack  {{a}_{0},\ldots ,{a}_{n - 1},{a}_{n} + 1/{\xi }_{n + 1}}\right\rbrack   = \left\lbrack  {{a}_{0},\ldots ,{a}_{n - 1},{a}_{n},{\xi }_{n + 1}}\right\rbrack
\]

ce qui est précisément le résultat souhaité au rang \( n + 1 \) .

> which is precisely the desired result at rank \( n + 1 \).

---

Supposons maintenant le résultat vrai au rang \( n \) et montrons le au rang \( n + 1 \) . En appliquant la propriété au rang \( n \) on obtient pour tout \( x > 0 \)

> Now assume the result is true at rank \( n \) and show it at rank \( n + 1 \). By applying the property at rank \( n \) we obtain for all \( x > 0 \)

\[
\left\lbrack  {{a}_{0},\ldots ,{a}_{n - 1},{a}_{n} + \frac{1}{x}}\right\rbrack   = \frac{\left( {{a}_{n} + 1/x}\right) {p}_{n - 1} + {p}_{n - 2}}{\left( {{a}_{n} + 1/x}\right) {q}_{n - 1} + {q}_{n - 2}} = \frac{\left( {{a}_{n}x + 1}\right) {p}_{n - 1} + {p}_{n - 2}x}{\left( {{a}_{n}x + 1}\right) {q}_{n - 1} + {q}_{n - 2}x} = \frac{{p}_{n}x + {p}_{n - 1}}{{q}_{n}x + {q}_{n - 1}}.
\]

Le premier membre de cette expression est égal à \( \left\lbrack {{a}_{0},\ldots ,{a}_{n}, x}\right\rbrack \) , le résultat est donc bien démontré au rang \( n + 1 \) .

> The first term of this expression is equal to \( \left\lbrack {{a}_{0},\ldots ,{a}_{n}, x}\right\rbrack \), the result is therefore indeed proven at rank \( n + 1 \).

c) Le résultat pour \( n = 0 \) et \( n = 1 \) est immédiat compte tenu de la définition de \( {p}_{0},{q}_{0} \) et \( {p}_{1},{q}_{1} \) . Pour \( n \geq 2 \) , il suffit d’appliquer le résultat de la question précédente à \( x = {a}_{n} \) .

> c) The result for \( n = 0 \) and \( n = 1 \) is immediate given the definition of \( {p}_{0},{q}_{0} \) and \( {p}_{1},{q}_{1} \). For \( n \geq 2 \), it suffices to apply the result of the previous question to \( x = {a}_{n} \).

d) Lorsque \( n = 1 \) , le résultat découle de l’égalité \( {p}_{1}{q}_{0} - {p}_{0}{q}_{1} = \left( {{a}_{0}{a}_{1} + 1}\right) - {a}_{0}{a}_{1} = 1 \) et lorsque \( n \geq 2 \) c’est une conséquence de la relation

> d) When \( n = 1 \), the result follows from the equality \( {p}_{1}{q}_{0} - {p}_{0}{q}_{1} = \left( {{a}_{0}{a}_{1} + 1}\right) - {a}_{0}{a}_{1} = 1 \) and when \( n \geq 2 \) it is a consequence of the relation

\[
{p}_{n}{q}_{n - 1} - {p}_{n - 1}{q}_{n} = \left( {{a}_{n}{p}_{n - 1} + {p}_{n - 2}}\right) {q}_{n - 1} - {p}_{n - 1}\left( {{a}_{n}{q}_{n - 1} + {q}_{n - 2}}\right)  =  - \left( {{p}_{n - 1}{q}_{n - 2} - {p}_{n - 2}{q}_{n - 1}}\right) .
\]

e) Les valeurs \( {a}_{n} \) sont entières (ce sont des parties entières), donc \( {p}_{n} \) et \( {q}_{n} \) sont des entiers. Pour \( n = 0,{q}_{0} = 1 \) donc \( {p}_{0}/{q}_{0} \) est bien une fraction irréductible et pour \( n \geq 1 \) , la relation \( {p}_{n}{q}_{n - 1} - {q}_{n}{p}_{n - 1} = {\left( -1\right) }^{n - 1} \) montre que \( {p}_{n} \) et \( {q}_{n} \) sont premiers entre eux (théorème de Bezout), d'où le résultat.

> e) The values \( {a}_{n} \) are integers (they are integer parts), so \( {p}_{n} \) and \( {q}_{n} \) are integers. For \( n = 0,{q}_{0} = 1 \) thus \( {p}_{0}/{q}_{0} \) is indeed an irreducible fraction and for \( n \geq 1 \), the relation \( {p}_{n}{q}_{n - 1} - {q}_{n}{p}_{n - 1} = {\left( -1\right) }^{n - 1} \) shows that \( {p}_{n} \) and \( {q}_{n} \) are coprime (Bézout's theorem), hence the result.

f) Les résultats des questions 1/a) et b) entraînent

> f) The results of questions 1/a) and b) imply

\[
\xi  - \frac{{p}_{n}}{{q}_{n}} = \left\lbrack  {{a}_{0},\ldots ,{a}_{n},{\xi }_{n + 1}}\right\rbrack   - \frac{{p}_{n}}{{q}_{n}} = \frac{{p}_{n}{\xi }_{n + 1} + {p}_{n - 1}}{{q}_{n}{\xi }_{n + 1} + {q}_{n - 1}} - \frac{{p}_{n}}{{q}_{n}}
\]

donc d'après le résultat de la question d)

> therefore according to the result of question d)

\[
\xi  - \frac{{p}_{n}}{{q}_{n}} = \frac{{q}_{n}\left( {{p}_{n}{\xi }_{n + 1} + {p}_{n - 1}}\right)  - {p}_{n}\left( {{q}_{n}{\xi }_{n + 1} + {q}_{n - 1}}\right) }{{q}_{n}\left( {{q}_{n}{\xi }_{n + 1} + {q}_{n - 1}}\right) } = \frac{{q}_{n}{p}_{n - 1} - {p}_{n}{q}_{n - 1}}{{q}_{n}\left( {{q}_{n}{\xi }_{n + 1} + {q}_{n - 1}}\right) } = \frac{{\left( -1\right) }^{n}}{{q}_{n}\left( {{q}_{n}{\xi }_{n + 1} + {q}_{n - 1}}\right) }.
\]

Comme \( {\xi }_{n + 1} > 1 \) (on l’a vu dans la solution de la question 1/a)), ceci entraîne \( \left| {\xi - {p}_{n}/{q}_{n}}\right| < 1/{q}_{n}^{2} \) . g) Soit \( n \in \mathbb{N} \) . Le résultat de la question précédente montre que \( \xi - {p}_{n}/{q}_{n} \) et \( \xi - {p}_{n + 1}/{q}_{n + 1} \) sont de signe contraire, donc

> As \( {\xi }_{n + 1} > 1 \) (as seen in the solution to question 1/a)), this implies \( \left| {\xi - {p}_{n}/{q}_{n}}\right| < 1/{q}_{n}^{2} \) . g) Let \( n \in \mathbb{N} \) . The result of the previous question shows that \( \xi - {p}_{n}/{q}_{n} \) and \( \xi - {p}_{n + 1}/{q}_{n + 1} \) have opposite signs, therefore

\[
\left| {\xi  - \frac{{p}_{n}}{{q}_{n}}}\right|  + \left| {\xi  - \frac{{p}_{n + 1}}{{q}_{n + 1}}}\right|  = \left| {\frac{{p}_{n}}{{q}_{n}} - \frac{{p}_{n + 1}}{{q}_{n + 1}}}\right|  = \frac{1}{{q}_{n}{q}_{n + 1}} < \frac{1}{2{q}_{n}^{2}} + \frac{1}{2{q}_{n + 1}^{2}}
\]

(la dernière inégalité est une conséquence de l’inégalité \( {2xy} = {x}^{2} + {y}^{2} - {\left( x - y\right) }^{2} < {x}^{2} + {y}^{2} \) lorsque \( x \neq y \) , appliquée à \( x = 1/{q}_{n} \) et \( y = 1/{q}_{n + 1} \) )ce qui entraîne le résultat voulu.

> (the last inequality is a consequence of inequality \( {2xy} = {x}^{2} + {y}^{2} - {\left( x - y\right) }^{2} < {x}^{2} + {y}^{2} \) when \( x \neq y \) , applied to \( x = 1/{q}_{n} \) and \( y = 1/{q}_{n + 1} \) ) which leads to the desired result.

h) Raisonnons par l’absurde, en supposant \( \left| {{q\xi } - p}\right| < \left| {{q}_{n}\xi - {p}_{n}}\right| \) avec \( 0 < q \leq {q}_{n} \) et \( n > 0 \) . Comme \( {p}_{n + 1}{q}_{n} - {p}_{n}{q}_{n + 1} = {\left( -1\right) }^{n} \) (d’après 1/d)), il existe deux nombres entiers \( x \) et \( y \) tels que

> h) Let us reason by contradiction, assuming \( \left| {{q\xi } - p}\right| < \left| {{q}_{n}\xi - {p}_{n}}\right| \) with \( 0 < q \leq {q}_{n} \) and \( n > 0 \) . Since \( {p}_{n + 1}{q}_{n} - {p}_{n}{q}_{n + 1} = {\left( -1\right) }^{n} \) (according to 1/d)), there exist two integers \( x \) and \( y \) such that

\[
p = x{p}_{n} + y{p}_{n + 1},\;q = x{q}_{n} + y{q}_{n + 1}.
\]

On a forcément \( x \neq 0 \) (sinon \( q = y{q}_{n + 1} > {q}_{n} \) car \( n > 0 \) , ce qui est contraire aux hypothèses), et \( y \neq 0 \) (sinon \( \left| {{q\xi } - p}\right| = \left| x\right| \cdot \left| {{q}_{n}\xi - {p}_{n}}\right| \geq \left| {{q}_{n}\xi - {p}_{n}}\right| \) , ce qui est contraire aux hypothèses). On doit également avoir \( x \) et \( y \) de signe opposé, sinon on aurait \( \left| q\right| \geq \left| {q}_{n}\right| + \left| {q}_{n + 1}\right| \geq {q}_{n} \) . De plus d’après \( 1/\mathrm{f}) \) , les valeurs \( {q}_{n}\xi - {p}_{n} \) et \( {q}_{n + 1}\xi - {p}_{n + 1} \) ont des signes opposés, donc \( x\left( {{q}_{n}\xi - {p}_{n}}\right) \) et \( y\left( {{q}_{n + 1}\xi - {p}_{n + 1}}\right) \) sont de même signe. Comme

> We must have \( x \neq 0 \) (otherwise \( q = y{q}_{n + 1} > {q}_{n} \) because \( n > 0 \) , which contradicts the hypotheses), and \( y \neq 0 \) (otherwise \( \left| {{q\xi } - p}\right| = \left| x\right| \cdot \left| {{q}_{n}\xi - {p}_{n}}\right| \geq \left| {{q}_{n}\xi - {p}_{n}}\right| \) , which contradicts the hypotheses). We must also have \( x \) and \( y \) of opposite signs, otherwise we would have \( \left| q\right| \geq \left| {q}_{n}\right| + \left| {q}_{n + 1}\right| \geq {q}_{n} \) . Furthermore, according to \( 1/\mathrm{f}) \) , the values \( {q}_{n}\xi - {p}_{n} \) and \( {q}_{n + 1}\xi - {p}_{n + 1} \) have opposite signs, so \( x\left( {{q}_{n}\xi - {p}_{n}}\right) \) and \( y\left( {{q}_{n + 1}\xi - {p}_{n + 1}}\right) \) have the same sign. Since

\[
{q\xi } - p = x\left( {{q}_{n}\xi  - {p}_{n}}\right)  + y\left( {{q}_{n + 1}\xi  - {p}_{n + 1}}\right)
\]

ceci entraîne

> this implies

\[
\left| {{q\xi } - p}\right|  = \left| {x\left( {{q}_{n}\xi  - {p}_{n}}\right) }\right|  + \left| {y\left( {{q}_{n + 1}\xi  - {p}_{n + 1}}\right) }\right|  > \left| {x\left( {{q}_{n}\xi  - {p}_{n}}\right) }\right|  \geq  \left| {{q}_{n}\xi  - {p}_{n}}\right| .
\]

Cette inégalité est une contradiction, ce qui prouve le résultat.

> This inequality is a contradiction, which proves the result.

2/a) Soit \( \xi \in \mathbb{R} \) un nombre quadratique et un polynôme \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) de degré 2, irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) , tel que \( Q\left( \xi \right) = 0 \) . Si \( \xi \in \mathbb{R} \) était rationnel, alors \( Q \) ne serait pas irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) (il serait divisible par \( X - \xi \) ), ce qui est absurde. (De manière équivalente, on montre facilement que les nombres quadratiques sont ceux de la forme \( \frac{A + \sqrt{D}}{B} \) où \( A, B, D \in \mathbb{Z} \) , avec \( B \neq 0 \) et \( D \) un entier naturel qui n'est pas un carré.)

> 2/a) Let \( \xi \in \mathbb{R} \) be a quadratic number and \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) a polynomial of degree 2, irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \), such that \( Q\left( \xi \right) = 0 \). If \( \xi \in \mathbb{R} \) were rational, then \( Q \) would not be irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) (it would be divisible by \( X - \xi \)), which is absurd. (Equivalently, it is easy to show that quadratic numbers are those of the form \( \frac{A + \sqrt{D}}{B} \) where \( A, B, D \in \mathbb{Z} \), with \( B \neq 0 \) and \( D \) a natural number that is not a square.)

b) Compte tenu des formules permettant d'obtenir les quotients incomplets et complets d'un nombre irrationnel, il est immédiat que le quotient incomplet de \( {\xi }_{k} \) d’indice \( n \) est égal à \( {a}_{n + k} \) . Ainsi, si \( {\xi }_{r} = {\xi }_{r + T} \) , l’égalité des quotients incomplets d’indice \( n \) de ces deux nombres entraîne \( {a}_{n + r} = {a}_{n + r + T} \) pour tout \( n \in \mathbb{N} \) , c’est-â-dire \( {a}_{k} = {a}_{k + T} \) pour tout \( k \geq r \) . Réciproquement, si \( {a}_{k} = {a}_{k + T} \) pour tout \( k \geq r \) , alors tous les quotients incomplets de \( {\xi }_{r} \) et \( {\xi }_{r + T} \) sont égaux, donc les réduites de \( {\xi }_{r} \) et \( {\xi }_{r + T} \) sont égales. Comme un nombre irrationnel est égal à la limite de ses réduites (conséquence du résultat de la question 1/f)), ceci entraîne \( {\xi }_{r} = {\xi }_{r + T} \) .

> b) Given the formulas for obtaining the partial and complete quotients of an irrational number, it is immediate that the partial quotient of \( {\xi }_{k} \) with index \( n \) is equal to \( {a}_{n + k} \). Thus, if \( {\xi }_{r} = {\xi }_{r + T} \), the equality of the partial quotients of index \( n \) of these two numbers implies \( {a}_{n + r} = {a}_{n + r + T} \) for all \( n \in \mathbb{N} \), that is to say \( {a}_{k} = {a}_{k + T} \) for all \( k \geq r \). Conversely, if \( {a}_{k} = {a}_{k + T} \) for all \( k \geq r \), then all partial quotients of \( {\xi }_{r} \) and \( {\xi }_{r + T} \) are equal, so the convergents of \( {\xi }_{r} \) and \( {\xi }_{r + T} \) are equal. Since an irrational number is equal to the limit of its convergents (a consequence of the result in question 1/f)), this implies \( {\xi }_{r} = {\xi }_{r + T} \).

c) Soit \( r \in \mathbb{N} \) et \( T \in {\mathbb{N}}^{ * } \) tels que les quotients incomplets \( {\xi }_{r} \) et \( {\xi }_{r + T} \) de \( \xi \) soient égaux. Posons \( s = r + T \) . Les quotients complets et incomplets d’indice \( n \) de \( {\xi }_{r} \) sont ceux de \( \xi \) d’indice \( n + r \) , donc d’après \( 1/\mathrm{a} \) ) on peut écrire \( {\xi }_{r} = \left\lbrack {{a}_{r},\ldots ,{a}_{s - 1},{\xi }_{s}}\right\rbrack \) . Par ailleurs, le résultat de la question 1/b) appliqué au développement en fraction continue de \( {\xi }_{r} \) permet d’écrire

> c) Let \( r \in \mathbb{N} \) and \( T \in {\mathbb{N}}^{ * } \) be such that the partial quotients \( {\xi }_{r} \) and \( {\xi }_{r + T} \) of \( \xi \) are equal. Let \( s = r + T \). The complete and partial quotients of index \( n \) of \( {\xi }_{r} \) are those of \( \xi \) of index \( n + r \), so according to \( 1/\mathrm{a} \)) we can write \( {\xi }_{r} = \left\lbrack {{a}_{r},\ldots ,{a}_{s - 1},{\xi }_{s}}\right\rbrack \). Furthermore, the result of question 1/b) applied to the continued fraction expansion of \( {\xi }_{r} \) allows us to write

\[
{\xi }_{r} = \left\lbrack  {{a}_{r},\ldots ,{a}_{s - 1},{\xi }_{s}}\right\rbrack   = \frac{{k}_{T - 1}{\xi }_{s} + {k}_{T - 2}}{{\ell }_{T - 1}{\xi }_{s} + {\ell }_{T - 2}},\;{k}_{T - 1},{k}_{T - 2},{\ell }_{T - 1},{\ell }_{T - 2} \in  {\mathbb{N}}^{ * }
\]

(où \( {k}_{n}/{\ell }_{n} \) désigne la \( n \) -ième réduite de \( {\xi }_{r} \) ). Comme \( {\xi }_{r} = {\xi }_{s} \) cette égalité entraîne

> (where \( {k}_{n}/{\ell }_{n} \) denotes the \( n \)-th convergent of \( {\xi }_{r} \)). Since \( {\xi }_{r} = {\xi }_{s} \) this equality implies

\[
{\ell }_{T - 1}{\xi }_{r}^{2} + \left( {{\ell }_{T - 2} - {k}_{T - 1}}\right) {\xi }_{r} - {k}_{T - 2} = Q\left( {\xi }_{r}\right)  = 0,\;Q = {\ell }_{T - 1}{X}^{2} + \left( {{\ell }_{T - 2} - {k}_{T - 1}}\right) X - {k}_{T - 2}.
\]

Le polynôme \( Q \) est à coefficients entiers et de degré 2, il est forcément irréductible car \( {\xi }_{r} \) est irrationnel. Ainsi, \( {\xi }_{r} \) est un nombre quadratique.

> The polynomial \( Q \) has integer coefficients and is of degree 2; it is necessarily irreducible because \( {\xi }_{r} \) is irrational. Thus, \( {\xi }_{r} \) is a quadratic number.

Maintenant, la question 1/b) nous assure qu’à partir des réduites \( {p}_{n}/{q}_{n} \) de \( \xi \) , on peut écrire

> Now, question 1/b) ensures that from the convergents \( {p}_{n}/{q}_{n} \) of \( \xi \), we can write

\[
\xi  = \frac{{p}_{r - 1}{\xi }_{r} + {p}_{r - 2}}{{q}_{r - 1}{\xi }_{r} + {q}_{r - 2}}\;\text{ donc }\;{\xi }_{r} = \frac{-{q}_{r - 2}\xi  + {p}_{r - 2}}{{q}_{r - 1}\xi  - {p}_{r - 1}}.
\]

Ceci entraîne que

> This implies that

\[
R = {\left( {q}_{r - 1}X - {p}_{r - 1}\right) }^{2}Q\left( \frac{-{q}_{r - 2}X + {p}_{r - 2}}{{q}_{r - 1}X - {p}_{r - 1}}\right)
\]

annule \( \xi \) . Or \( R \) est un polynôme à coefficients entiers de degré 2 (son coefficient dominant \( {q}_{r - 1}^{2}Q\left( {{q}_{r - 2}/{q}_{r - 1}}\right) \) est non nul car \( Q \) n’a pas de racine rationnelle), et comme \( \xi \) est irrationnel, \( R \) est forcément irréductible. Ainsi, \( \xi \) est bien quadratique.

> vanishes \( \xi \) . Now \( R \) is a polynomial with integer coefficients of degree 2 (its leading coefficient \( {q}_{r - 1}^{2}Q\left( {{q}_{r - 2}/{q}_{r - 1}}\right) \) is non-zero because \( Q \) has no rational root), and since \( \xi \) is irrational, \( R \) is necessarily irreducible. Thus, \( \xi \) is indeed quadratic.

d) (i) Un calcul montre que l'on peut écrire

> d) (i) A calculation shows that we can write

\[
{Q}_{n} = \alpha {\left( {p}_{n - 1}X + {p}_{n - 2}\right) }^{2} + \beta \left( {{p}_{n - 1}X + {p}_{n - 2}}\right) \left( {{q}_{n - 1}X + {q}_{n - 2}}\right)  + \gamma {\left( {q}_{n - 1}X + {q}_{n - 2}\right) }^{2} = {\alpha }_{n}{X}^{2} + {\beta }_{n}X + {\gamma }_{n}
\]

où \( {\alpha }_{n},{\beta }_{n} \) et \( {\gamma }_{n} \) sont trois entiers, avec \( {\alpha }_{n} = {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) \) . Comme \( Q \) n’a pas de racine rationnelle, ceci entraîne \( {\alpha }_{n} \neq 0 \) donc \( {Q}_{n} \) est bien un polynôme de degré 2 à coefficients entiers. Comme \( Q\left( \xi \right) = 0 \) , la formule \( \xi = \frac{{p}_{n - 1}{\xi }_{n} + {p}_{n - 2}}{{q}_{n - 1}{\xi }_{n} + {q}_{n - 2}} \) (voir 1/b)) montre que \( {\xi }_{n} \) est bien racine de \( {Q}_{n} \) .

> where \( {\alpha }_{n},{\beta }_{n} \) and \( {\gamma }_{n} \) are three integers, with \( {\alpha }_{n} = {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) \) . Since \( Q \) has no rational root, this implies \( {\alpha }_{n} \neq 0 \) so \( {Q}_{n} \) is indeed a polynomial of degree 2 with integer coefficients. As \( Q\left( \xi \right) = 0 \) , the formula \( \xi = \frac{{p}_{n - 1}{\xi }_{n} + {p}_{n - 2}}{{q}_{n - 1}{\xi }_{n} + {q}_{n - 2}} \) (see 1/b)) shows that \( {\xi }_{n} \) is indeed a root of \( {Q}_{n} \) .

Montrons que le discriminant \( {\Delta }_{n} \) de \( {Q}_{n} \) est égal au discriminant \( \Delta \) de \( Q \) . Plutôt que de calculer explicitement \( {\alpha }_{n},{\beta }_{n} \) et \( {\gamma }_{n} \) et de développer directement l’expression \( {\beta }_{n}^{2} - 4{\alpha }_{n}{\gamma }_{n} \) (les calculs sont lourds), on va utiliser le fait que le discriminant d'un polynôme de degré 2 est égal au carré de la différence de ses racines, multiplié par le carré de son coefficient dominant. Ainsi, si \( {\xi }^{\prime } \) désigne la deuxième racine de \( Q \) de sorte que \( Q = \alpha \left( {X - \xi }\right) \left( {X - {\xi }^{\prime }}\right) \) , on a \( \Delta = {\alpha }^{2}{\left( \xi - {\xi }^{\prime }\right) }^{2} \) . Les deux racines de \( {Q}_{n} \) étant \( {\xi }_{n} = \frac{-{q}_{n - 2}\xi + {p}_{n - 2}}{{q}_{n - 1}\xi - {p}_{n - 1}} \) et \( {\xi }_{n}^{\prime } = \frac{-{q}_{n - 2}{\xi }^{\prime } + {p}_{n - 2}}{{q}_{n - 1}{\xi }^{\prime } - {p}_{n - 1}} \) , et comme de plus \( {\alpha }_{n} = \; {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) = \alpha \left( {{p}_{n - 1} - {q}_{n - 1}\xi }\right) \left( {{p}_{n - 1} - {q}_{n - 1}{\xi }^{\prime }}\right) \) , on a

> Let us show that the discriminant \( {\Delta }_{n} \) of \( {Q}_{n} \) is equal to the discriminant \( \Delta \) of \( Q \) . Rather than explicitly calculating \( {\alpha }_{n},{\beta }_{n} \) and \( {\gamma }_{n} \) and directly expanding the expression \( {\beta }_{n}^{2} - 4{\alpha }_{n}{\gamma }_{n} \) (the calculations are cumbersome), we will use the fact that the discriminant of a degree 2 polynomial is equal to the square of the difference of its roots, multiplied by the square of its leading coefficient. Thus, if \( {\xi }^{\prime } \) denotes the second root of \( Q \) such that \( Q = \alpha \left( {X - \xi }\right) \left( {X - {\xi }^{\prime }}\right) \) , we have \( \Delta = {\alpha }^{2}{\left( \xi - {\xi }^{\prime }\right) }^{2} \) . The two roots of \( {Q}_{n} \) being \( {\xi }_{n} = \frac{-{q}_{n - 2}\xi + {p}_{n - 2}}{{q}_{n - 1}\xi - {p}_{n - 1}} \) and \( {\xi }_{n}^{\prime } = \frac{-{q}_{n - 2}{\xi }^{\prime } + {p}_{n - 2}}{{q}_{n - 1}{\xi }^{\prime } - {p}_{n - 1}} \) , and since furthermore \( {\alpha }_{n} = \; {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) = \alpha \left( {{p}_{n - 1} - {q}_{n - 1}\xi }\right) \left( {{p}_{n - 1} - {q}_{n - 1}{\xi }^{\prime }}\right) \) , we have

\[
{\Delta }_{n} = {\alpha }_{n}^{2}{\left( {\xi }_{n} - {\xi }_{n}^{\prime }\right) }^{2} = {\alpha }^{2}{\left( {p}_{n - 1} - {q}_{n - 1}\xi \right) }^{2}{\left( {p}_{n - 1} - {q}_{n - 1}{\xi }^{\prime }\right) }^{2}{\left( \frac{-{q}_{n - 2}\xi  + {p}_{n - 2}}{{q}_{n - 1}\xi  - {p}_{n - 1}} - \frac{-{q}_{n - 2}{\xi }^{\prime } + {p}_{n - 2}}{{q}_{n - 1}{\xi }^{\prime } - {p}_{n - 1}}\right) }^{2}
\]

\[
= {\alpha }^{2}\left( {\left( {{q}_{n - 2}\xi  - {p}_{n - 2}}\right) \left( {{q}_{n - 1}{\xi }^{\prime } - {p}_{n - 1}}\right)  - \left( {{q}_{n - 2}{\xi }^{\prime } - {p}_{n - 2}}\right) {\left( {q}_{n - 1}\xi  - {p}_{n - 1})\right) }^{2}}\right.
\]

\[
= {\alpha }^{2}{\left( \left( -{q}_{n - 2}{p}_{n - 1} + {p}_{n - 2}{q}_{n - 1}\right) \xi  - \left( -{q}_{n - 2}{p}_{n - 1} + {p}_{n - 2}{q}_{n - 1}\right) {\xi }^{\prime }\right) }^{2}
\]

\[
= {\alpha }^{2}{\left( {p}_{n - 1}{q}_{n - 2} - {p}_{n - 2}{q}_{n - 1}\right) }^{2}{\left( \xi  - {\xi }^{\prime }\right) }^{2}
\]

et comme \( {p}_{n - 1}{q}_{n - 2} - {p}_{n - 2}{q}_{n - 1} = {\left( -1\right) }^{n - 2} \) (voir 1/d)), ceci entraîne bien \( {\Delta }_{n} = {\alpha }^{2}{\left( \xi - {\xi }^{\prime }\right) }^{2} = \Delta \) .

> and since \( {p}_{n - 1}{q}_{n - 2} - {p}_{n - 2}{q}_{n - 1} = {\left( -1\right) }^{n - 2} \) (see 1/d)), this indeed implies \( {\Delta }_{n} = {\alpha }^{2}{\left( \xi - {\xi }^{\prime }\right) }^{2} = \Delta \) .

Montrons maintenant que les polynômes \( {Q}_{n} \) sont en nombre fini. Il suffit pour cela de montrer que les coefficients \( {\alpha }_{n},{\beta }_{n} \) et \( {\gamma }_{n} \) de \( {Q}_{n} \) sont bornés, ce qui prouvera le résultat compte tenu du fait que ces coefficients sont entiers. Pour le coefficient dominant \( {\alpha }_{n} \) , on part de la relation \( {\alpha }_{n} = {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) \) ce qui entraîne, en appliquant l’inégalité des accroissements finis à la fonction polynôme \( x \mapsto Q\left( x\right) \)

> Let us now show that the polynomials \( {Q}_{n} \) are finite in number. It suffices to show that the coefficients \( {\alpha }_{n},{\beta }_{n} \) and \( {\gamma }_{n} \) of \( {Q}_{n} \) are bounded, which will prove the result given that these coefficients are integers. For the leading coefficient \( {\alpha }_{n} \), we start from the relation \( {\alpha }_{n} = {q}_{n - 1}^{2}Q\left( {{p}_{n - 1}/{q}_{n - 1}}\right) \), which implies, by applying the mean value inequality to the polynomial function \( x \mapsto Q\left( x\right) \)

\[
\left| {\alpha }_{n}\right|  = {q}_{n - 1}^{2}\left| {Q\left( \frac{{p}_{n - 1}}{{q}_{n - 1}}\right)  - Q\left( \xi \right) }\right|  \leq  {q}_{n - 1}^{2}M\left| {\frac{{p}_{n - 1}}{{q}_{n - 1}} - \xi }\right| ,\;M = \mathop{\sup }\limits_{{\left| {x - \xi }\right|  \leq  1}}\left| {{Q}^{\prime }\left( x\right) }\right|
\]

car \( \left| {{p}_{n - 1}/{q}_{n - 1} - \xi }\right| < 1 \) d’après \( 1/\mathrm{f}) \) . D’après \( 1/\mathrm{f}) \) encore une fois, ceci entraîne \( \left| {\alpha }_{n}\right| \leq M \) . Pour le terme constant de \( {Q}_{n} \) , on remarque que \( {\gamma }_{n} = {q}_{n - 2}^{2}Q\left( {{p}_{n - 2}/{q}_{n - 2}}\right) = {\alpha }_{n - 1} \) donc \( \left| {\gamma }_{n - 1}\right| \leq M \) . Il ne reste plus qu’à remarquer que \( {\beta }_{n}^{2} = {\Delta }_{n} + 4{\alpha }_{n}{\gamma }_{n} = \Delta + 4{\alpha }_{n}{\gamma }_{n} \) donc \( {\beta }_{n}^{2} \leq \Delta + 4{M}^{2} \) , donc \( {\beta }_{n} \) est borné également.

> because \( \left| {{p}_{n - 1}/{q}_{n - 1} - \xi }\right| < 1 \) according to \( 1/\mathrm{f}) \). According to \( 1/\mathrm{f}) \) once again, this implies \( \left| {\alpha }_{n}\right| \leq M \). For the constant term of \( {Q}_{n} \), we note that \( {\gamma }_{n} = {q}_{n - 2}^{2}Q\left( {{p}_{n - 2}/{q}_{n - 2}}\right) = {\alpha }_{n - 1} \) therefore \( \left| {\gamma }_{n - 1}\right| \leq M \). It only remains to note that \( {\beta }_{n}^{2} = {\Delta }_{n} + 4{\alpha }_{n}{\gamma }_{n} = \Delta + 4{\alpha }_{n}{\gamma }_{n} \) therefore \( {\beta }_{n}^{2} \leq \Delta + 4{M}^{2} \), so \( {\beta }_{n} \) is also bounded.

(ii) Comme il n’y a qu’un nombre fini de valeurs prises par la suite de polynômes \( \left( {Q}_{n}\right) \) , il y a au moins trois indices distincts \( {n}_{1},{n}_{2},{n}_{3} \) tels que \( {Q}_{{n}_{1}} = {Q}_{{n}_{2}} = {Q}_{{n}_{3}} \) . Or chacun de ces polynômes n’a que deux racines et \( {\xi }_{{n}_{k}} \) est racine de \( {Q}_{{n}_{k}} \) , cela entraîne que parmi \( {\xi }_{{n}_{1}},{\xi }_{{n}_{2}},{\xi }_{{n}_{3}} \) , deux valeurs au moins sont identiques. Ainsi, nous avons montré l’existence de deux indices distincts \( r \) et \( s \) tels que \( {\xi }_{r} = {\xi }_{s} \) , donc le développement en fraction continue de \( \xi \) est bien périodique à partir d'un certain rang d'après 2/b).

> (ii) Since there is only a finite number of values taken by the sequence of polynomials \( \left( {Q}_{n}\right) \), there are at least three distinct indices \( {n}_{1},{n}_{2},{n}_{3} \) such that \( {Q}_{{n}_{1}} = {Q}_{{n}_{2}} = {Q}_{{n}_{3}} \). However, each of these polynomials has only two roots and \( {\xi }_{{n}_{k}} \) is a root of \( {Q}_{{n}_{k}} \), this implies that among \( {\xi }_{{n}_{1}},{\xi }_{{n}_{2}},{\xi }_{{n}_{3}} \), at least two values are identical. Thus, we have shown the existence of two distinct indices \( r \) and \( s \) such that \( {\xi }_{r} = {\xi }_{s} \), so the continued fraction expansion of \( \xi \) is indeed periodic from a certain point according to 2/b).

Remarque. On peut également développer en fraction continue tout nombre rationnel \( \xi = a/b \) , mais la fraction continue est finie et s’arrête dès que \( {\xi }_{n} \) est un entier. On montre alors que l’algorithme permettant d’obtenir la fraction continue de \( \xi \) est l’algorithme d'Euclide.

> Remark. One can also expand any rational number \( \xi = a/b \) into a continued fraction, but the continued fraction is finite and stops as soon as \( {\xi }_{n} \) is an integer. It is then shown that the algorithm used to obtain the continued fraction of \( \xi \) is the Euclidean algorithm.

Le résultat 1/f) entraîne que tout nombre irrationnel \( \xi \) est développable en fraction continue infinie. Réciproquement, on peut montrer que toute fraction continue infinie converge vers un nombre irrationnel. Par ailleurs, l'égalité des limites de deux fractions continues infinies n'est possible que si les quotients incomplets de l'une sont égaux à ceux de l'autre.

> Result 1/f) implies that any irrational number \( \xi \) can be expanded into an infinite continued fraction. Conversely, it can be shown that any infinite continued fraction converges to an irrational number. Furthermore, the equality of the limits of two infinite continued fractions is only possible if the incomplete quotients of one are equal to those of the other.

On peut montrer que si un nombre rationnel \( p/q \) vérifie \( \left| {\xi - p/q}\right| < 1/\left( {2{q}^{2}}\right) \) , alors \( p/q \) est forcément une réduite de \( \xi \) .

> It can be shown that if a rational number \( p/q \) satisfies \( \left| {\xi - p/q}\right| < 1/\left( {2{q}^{2}}\right) \), then \( p/q \) is necessarily a convergent of \( \xi \).

Une application classique des fractions continues est la résolution de l'équation de Pell-Fermat (recherche des solutions entières \( x \) et \( y \) telles que \( {x}^{2} - n{y}^{2} = \pm 1 \) , lorsque \( n \) est un entier qui n'est pas un carré).

> A classic application of continued fractions is solving the Pell-Fermat equation (finding integer solutions \( x \) and \( y \) such that \( {x}^{2} - n{y}^{2} = \pm 1 \), where \( n \) is a non-square integer).
