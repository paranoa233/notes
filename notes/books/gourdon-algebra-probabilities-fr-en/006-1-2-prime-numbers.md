#### 1.2. Prime numbers

*Français : 1.2. Nombres premiers*

DéFINITION 6. On dit qu'un entier naturel \( p \geq 2 \) est un nombre premier si ses seuls diviseurs sont \( p, - p,1 \) et -1 .

> DEFINITION 6. A natural integer \( p \geq 2 \) is said to be a prime number if its only divisors are \( p, - p,1 \) and -1 .

— THÉORÉME 3 (THÉORÉME FONDAMENTAL DE L'ARITHMÉTIQUE). Tout entier naturel \( n \geq 2 \) s’écrit de manière unique à l’ordre prés sous la forme

> — THEOREM 3 (FUNDAMENTAL THEOREM OF ARITHMETIC). Every natural integer \( n \geq 2 \) can be written uniquely, up to order, in the form

\[
n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}},
\]

(*)

> où les \( {p}_{i} \) sont des nombres premiers distincts et les \( {\alpha }_{i} \) des entiers naturels non nuls. La relation \( \left( *\right) \) s’appelle la décomposition de \( n \) en facteurs premiers.

where the \( {p}_{i} \) are distinct prime numbers and the \( {\alpha }_{i} \) are non-zero natural integers. The relation \( \left( *\right) \) is called the prime factorization of \( n \) .

> Remarque 4. - Tout entier \( n,\left| n\right| \geq 2 \) , est divisible par un nombre premier.

Remark 4. - Every integer \( n,\left| n\right| \geq 2 \) is divisible by a prime number.

> - Si \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) et \( m = {p}_{1}^{{\beta }_{1}}\cdots {p}_{k}^{{\beta }_{k}} \) , où les \( {p}_{i} \) sont des nombres premiers distincts et les \( {\alpha }_{i},{\beta }_{i} \) des entiers naturels, alors pgcd \( \left( {n, m}\right)  = {p}_{1}^{{\gamma }_{1}}\cdots {p}_{k}^{{\gamma }_{k}} \) et ppcm \( \left( {n, m}\right)  = \; {p}_{1}^{{\delta }_{1}}\cdots {p}_{k}^{{\delta }_{k}} \) où \( {\gamma }_{i} = \inf \left( {{\alpha }_{i},{\beta }_{i}}\right) \) et \( {\delta }_{i} = \sup \left( {{\alpha }_{i},{\beta }_{i}}\right) \) .

- If \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) and \( m = {p}_{1}^{{\beta }_{1}}\cdots {p}_{k}^{{\beta }_{k}} \) , where \( {p}_{i} \) are distinct prime numbers and \( {\alpha }_{i},{\beta }_{i} \) are natural numbers, then gcd \( \left( {n, m}\right)  = {p}_{1}^{{\gamma }_{1}}\cdots {p}_{k}^{{\gamma }_{k}} \) and lcm \( \left( {n, m}\right)  = \; {p}_{1}^{{\delta }_{1}}\cdots {p}_{k}^{{\delta }_{k}} \) where \( {\gamma }_{i} = \inf \left( {{\alpha }_{i},{\beta }_{i}}\right) \) and \( {\delta }_{i} = \sup \left( {{\alpha }_{i},{\beta }_{i}}\right) \) .

> PROPOSITION 6. Si un nombre premier \( p \) ne divise pas un entier a, alors \( p \) et a sont premiers entre eux.

PROPOSITION 6. If a prime number \( p \) does not divide an integer a, then \( p \) and a are coprime.

> PROPOSITION 7. Si un nombre premier divise un produit d'entiers \( {a}_{1}\cdots {a}_{n} \) , il divise au moins l’un des facteurs \( {a}_{i} \) de ce produit.

PROPOSITION 7. If a prime number divides a product of integers \( {a}_{1}\cdots {a}_{n} \) , it divides at least one of the factors \( {a}_{i} \) of this product.

> PROPOSITION 8. L'ensemble des nombres premiers est infini.

PROPOSITION 8. The set of prime numbers is infinite.

> Démonstration. Raisonnons par l'absurde et supposons qu'il y ait un nombre fini de nombres premiers. Soit \( N \) le plus grand d’entre eux. Posons \( M = N! + 1 \) et désignons par \( p \) un nombre premier divisant \( M \) . Comme \( p \leq N \) , on a \( p \mid \left( {N!}\right) \) , donc \( p \mid \left( {M - N!}\right) = 1 \) , ce qui est absurde. I

Proof. Let us reason by contradiction and assume that there is a finite number of prime numbers. Let \( N \) be the largest of them. Let \( M = N! + 1 \) and let \( p \) be a prime number dividing \( M \) . Since \( p \leq N \) , we have \( p \mid \left( {N!}\right) \) , therefore \( p \mid \left( {M - N!}\right) = 1 \) , which is absurd. I

> Proposition 9. Soit \( p \) un nombre premier et \( k \) un entier, \( 1 \leq k \leq p - 1 \) . Alors \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) .

Proposition 9. Let \( p \) be a prime number and \( k \) an integer, \( 1 \leq k \leq p - 1 \) . Then \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) .

> Proposition 10. Soit \( n \geq 2 \) un entier. L’anneau \( \mathbb{Z}/n\mathbb{Z} \) est un corps si et seulement si n est premier.

Proposition 10. Let \( n \geq 2 \) be an integer. The ring \( \mathbb{Z}/n\mathbb{Z} \) is a field if and only if n is prime.

> \( \rightarrow \) THÉORÉME 4 (FERMAT). Soit \( p \geq 2 \) un nombre premier. Alors

\( \rightarrow \) THEOREM 4 (FERMAT). Let \( p \geq 2 \) be a prime number. Then

\[
\forall a \in  \mathbb{Z},\;{a}^{p} \equiv  a\;\left( {\;\operatorname{mod}\;p}\right)
\]

et

\[
\forall a \in  \mathbb{Z}, p \nmid  a,\;{a}^{p - 1} \equiv  1\;\left( {\;\operatorname{mod}\;p}\right) .
\]

THÉOREME 5 (WILSON). Un entier \( p \geq 2 \) est un nombre premier si et seulement si

> THEOREM 5 (WILSON). An integer \( p \geq 2 \) is a prime number if and only if

\[
\left( {p - 1}\right) ! \equiv   - 1\;\left( {\;\operatorname{mod}\;p}\right) .
\]

Démonstration. Condition nécessaire. Si \( p = 2 \) ou \( p = 3 \) , c’est évident. Pour traiter le cas \( p > 3 \) , on commence par rechercher les éléments \( x \) du groupe multiplicatif \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) égaux à leur inverse. Ils vérifient \( {x}^{2} = \overline{1} \) , c’est-à-dire \( \left( {x - \overline{1}}\right) \left( {x + \overline{1}}\right) = \overline{0} \) . Les seuls éléments de \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) égaux à leurs inverses sont donc \( x = \overline{1} \) et \( x = \overline{-1} \) . On range les autres \( \overline{2},\overline{3},\ldots ,\overline{p - 2} \) en \( \frac{p - 3}{2} \) paires d’éléments \( \left\{ {{x}_{i},{y}_{i}}\right\} \) telles que \( {x}_{i}{y}_{i} = \overline{1} \) . Si \( k = \frac{p - 3}{2} \) , on peut écrire

> Proof. Necessary condition. If \( p = 2 \) or \( p = 3 \), it is obvious. To handle the case \( p > 3 \), we begin by searching for elements \( x \) of the multiplicative group \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) equal to their inverse. They satisfy \( {x}^{2} = \overline{1} \), that is to say \( \left( {x - \overline{1}}\right) \left( {x + \overline{1}}\right) = \overline{0} \). The only elements of \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) equal to their inverses are therefore \( x = \overline{1} \) and \( x = \overline{-1} \). We arrange the other \( \overline{2},\overline{3},\ldots ,\overline{p - 2} \) into \( \frac{p - 3}{2} \) pairs of elements \( \left\{ {{x}_{i},{y}_{i}}\right\} \) such that \( {x}_{i}{y}_{i} = \overline{1} \). If \( k = \frac{p - 3}{2} \), we can write

\[
\overline{2} \cdot  \overline{3}\cdots \overline{p - 2} = \mathop{\prod }\limits_{{i = 1}}^{k}\left( {{x}_{i}{y}_{i}}\right)  = \overline{1}\;\text{ donc }\;\left( {p - 1}\right) ! \equiv   - 1\;\left( {\;\operatorname{mod}\;p}\right) .
\]

Condition suffisante. Supposons \( p \) non premier, et notons \( a \) un diviseur de \( p \) vérifiant \( 1 < a < p \) . On a \( a \mid \left\lbrack {\left( {p - 1}\right) ! + 1}\right\rbrack \) par hypothèse, et a \( \mid \left( {p - 1}\right) ! \) puisque \( 1 < a < p \) , donc \( a \mid 1 \) ce qui est absurde.

> Sufficient condition. Suppose \( p \) is not prime, and let \( a \) be a divisor of \( p \) satisfying \( 1 < a < p \). We have \( a \mid \left\lbrack {\left( {p - 1}\right) ! + 1}\right\rbrack \) by hypothesis, and a \( \mid \left( {p - 1}\right) ! \) since \( 1 < a < p \), therefore \( a \mid 1 \) which is absurd.
