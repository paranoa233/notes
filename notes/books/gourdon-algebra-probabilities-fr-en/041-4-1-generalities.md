#### 4.1. Generalities

*Français : 4.1. Généralités*

Soit \( A \) un anneau commutatif unitaire. L’anneau \( A\left\lbrack X\right\rbrack \) est aussi commutatif unitaire. On peut donc définir l’anneau des polynômes à une indéterminée à coefficients dans \( A\left\lbrack X\right\rbrack \) . C’est \( A\left\lbrack X\right\rbrack \left\lbrack Y\right\rbrack \) , noté aussi \( A\left\lbrack {X, Y}\right\rbrack \) , appelé anneau des polynômes à coefficients dans \( A \) à deux indéterminées. Les éléments de \( A\left\lbrack {X, Y}\right\rbrack \) sont ceux de la forme

> Let \( A \) be a commutative unital ring. The ring \( A\left\lbrack X\right\rbrack \) is also commutative and unital. We can therefore define the ring of polynomials in one indeterminate with coefficients in \( A\left\lbrack X\right\rbrack \). This is \( A\left\lbrack X\right\rbrack \left\lbrack Y\right\rbrack \), also denoted \( A\left\lbrack {X, Y}\right\rbrack \), called the ring of polynomials in two indeterminates with coefficients in \( A \). The elements of \( A\left\lbrack {X, Y}\right\rbrack \) are those of the form

\[
P = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{X}^{i}{Y}^{j},\;{a}_{i, j} \in  A
\]

où la somme sur \( \left( {i, j}\right) \) est finie. Par récurrence, on définit même

> where the sum over \( \left( {i, j}\right) \) is finite. By induction, we even define

\[
A\left\lbrack  {{X}_{1},\ldots ,{X}_{n}}\right\rbrack   = A\left\lbrack  {{X}_{1},\ldots ,{X}_{n - 1}}\right\rbrack  \left\lbrack  {X}_{n}\right\rbrack  ,
\]

anneau des polynômes à coefficients dans \( A \) à \( n \) indéterminées.

> ring of polynomials with coefficients in \( A \) in \( n \) indeterminates.

- Si \( A = \mathbb{K} \) est un corps commutatif, \( \mathbb{K}\left\lbrack  {{X}_{1},\cdots ,{X}_{n}}\right\rbrack \) est une \( \mathbb{K} \) -algèbre, dont \( \left\{  {{X}_{1}^{{i}_{1}}\cdots {X}_{n}^{{i}_{n}} \mid  \left( {{i}_{1},\ldots ,{i}_{n}}\right)  \in  {\mathbb{N}}^{n}}\right\} \) est une base.

> - If \( A = \mathbb{K} \) is a commutative field, \( \mathbb{K}\left\lbrack  {{X}_{1},\cdots ,{X}_{n}}\right\rbrack \) is a \( \mathbb{K} \)-algebra, of which \( \left\{  {{X}_{1}^{{i}_{1}}\cdots {X}_{n}^{{i}_{n}} \mid  \left( {{i}_{1},\ldots ,{i}_{n}}\right)  \in  {\mathbb{N}}^{n}}\right\} \) is a basis.

- Si \( A \) est intègre, \( A\left\lbrack  {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) est un anneau intègre.

> - If \( A \) is an integral domain, \( A\left\lbrack  {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) is an integral domain.

Si \( n \geq 2 \) , et \( \mathbb{K} \) est un corps, \( \mathbb{K}\left\lbrack {{X}_{1},\cdots ,{X}_{n}}\right\rbrack \) n’est pas un anneau principal (en revanche c'est un anneau factoriel, ce qui lui confère des propriétés arithmétiques ; cette notion n'est pas au programme de mathématiques spéciales).

> If \( n \geq 2 \), and \( \mathbb{K} \) is a field, \( \mathbb{K}\left\lbrack {{X}_{1},\cdots ,{X}_{n}}\right\rbrack \) is not a principal ideal ring (however, it is a unique factorization domain, which gives it arithmetic properties; this notion is not in the special mathematics curriculum).

DÉFINITION 1 (DEGRÉ PARTIEL). Soit \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) et \( i,1 \leq i \leq n \) . On peut écrire \( P = \mathop{\sum }\limits_{j}{P}_{j}{X}_{i}^{j} \) avec pour tout \( j,{P}_{j} \in A\left\lbrack {{X}_{1},\ldots ,{X}_{i - 1},{X}_{i + 1},\ldots ,{X}_{n}}\right\rbrack \) . On appelle degré partiel de \( P \) selon \( {X}_{i} \) le degré de \( P \) considéré comme polynôme en \( {X}_{i} \) et on le note \( {\deg }_{{X}_{i}}\left( P\right) \) (avec les notations précédentes, \( {\deg }_{{X}_{i}}\left( P\right) = \sup \left\{ {j \mid {P}_{j} \neq 0}\right\} \) ).

> DEFINITION 1 (PARTIAL DEGREE). Let \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) and \( i,1 \leq i \leq n \). We can write \( P = \mathop{\sum }\limits_{j}{P}_{j}{X}_{i}^{j} \) with for all \( j,{P}_{j} \in A\left\lbrack {{X}_{1},\ldots ,{X}_{i - 1},{X}_{i + 1},\ldots ,{X}_{n}}\right\rbrack \). We call the partial degree of \( P \) with respect to \( {X}_{i} \) the degree of \( P \) considered as a polynomial in \( {X}_{i} \) and denote it by \( {\deg }_{{X}_{i}}\left( P\right) \) (with the previous notations, \( {\deg }_{{X}_{i}}\left( P\right) = \sup \left\{ {j \mid {P}_{j} \neq 0}\right\} \)).

DÉFINITION 2 (DEGRÉ TOTAL). Le degré total d’un monôme \( a{X}_{1}^{{i}_{1}}\cdots {X}_{n}^{{i}_{n}}, a \neq 0 \) , est \( {i}_{1} + \cdots + {i}_{n} \) . Si \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) , le degré total de \( P \) , noté deg \( \left( P\right) \) , est le plus grand degré total des monômes qui forment \( P \) .

> DEFINITION 2 (TOTAL DEGREE). The total degree of a monomial \( a{X}_{1}^{{i}_{1}}\cdots {X}_{n}^{{i}_{n}}, a \neq 0 \) is \( {i}_{1} + \cdots + {i}_{n} \). If \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \), the total degree of \( P \), denoted deg \( \left( P\right) \), is the largest total degree of the monomials that form \( P \).

De même que dans \( \mathbb{K}\left\lbrack X\right\rbrack \) , on peut définir dans \( \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) des fonctions polynôme de \( n \) variables. On a en particulier le résultat suivant.

> Just as in \( \mathbb{K}\left\lbrack X\right\rbrack \), we can define in \( \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) polynomial functions of \( n \) variables. In particular, we have the following result.

Proposition 1. Soit \( \mathbb{K} \) un corps commutatif infini et un polynôme \( P \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . \( {SiP}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) pour tout \( n \) -uplet \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) de \( {\mathbb{K}}^{n} \) , on a \( P = 0 \) .

> Proposition 1. Let \( \mathbb{K} \) be an infinite commutative field and \( P \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) a polynomial. \( {SiP}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) for every \( n \) -tuple \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) of \( {\mathbb{K}}^{n} \) , we have \( P = 0 \) .

Remarque 1. - Comme pour les polynômes à une indéterminée, ce résultat est faux si \( \mathbb{K} \) est un corps fini. Par exemple dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \left( {p\text{ premier }}\right) \) , le polynôme \( P = \left( {X}_{1}\right) \left( {{X}_{1} - \overline{1}}\right) \cdots \left( {{X}_{1} - \left( \overline{p - 1}\right) }\right) {X}_{2}\cdots {X}_{n} \) est non nul et pourtant, pour tout \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{Z}/p\mathbb{Z}, P\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0. \)

> Remark 1. - As with polynomials in one indeterminate, this result is false if \( \mathbb{K} \) is a finite field. For example in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \left( {p\text{ premier }}\right) \) , the polynomial \( P = \left( {X}_{1}\right) \left( {{X}_{1} - \overline{1}}\right) \cdots \left( {{X}_{1} - \left( \overline{p - 1}\right) }\right) {X}_{2}\cdots {X}_{n} \) is non-zero and yet, for every \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{Z}/p\mathbb{Z}, P\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0. \)

- Attention, même si K est un corps infini, on peut avoir \( P\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = 0 \) pour une infinité de \( n \) -uplets \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) sans que \( P = 0 \) (prendre par exemple \( P\left( {X, Y}\right)  = \; X - Y \) sur \( \mathbb{R}\left\lbrack  {X, Y}\right\rbrack  ) \) .

> - Warning, even if K is an infinite field, we may have \( P\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = 0 \) for infinitely many \( n \)-tuples \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) without \( P = 0 \) (take for example \( P\left( {X, Y}\right)  = \; X - Y \) over \( \mathbb{R}\left\lbrack  {X, Y}\right\rbrack  ) \)).
