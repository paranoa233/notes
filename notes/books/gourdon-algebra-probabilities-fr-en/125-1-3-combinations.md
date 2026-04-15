#### 1.3. Combinations

*Français : 1.3. Combinaisons*

DÉFINITION 3. Soit \( E \) un ensemble fini, soit \( n = \left| E\right| \) . Soit \( p \in \mathbb{N} \) . On appelle \( p \) -combinaison de \( E \) tout partie de \( E \) de cardinal \( p \) . Le nombre de \( p \) -combinaisons de \( E \) ne dépend que de \( n \) et \( p \) . On le note \( \left( \begin{array}{l} n \\ p \end{array}\right) \) ou encore \( {C}_{n}^{p} \) .

> DEFINITION 3. Let \( E \) be a finite set, let \( n = \left| E\right| \). Let \( p \in \mathbb{N} \). A \( p \)-combination of \( E \) is any subset of \( E \) with cardinality \( p \). The number of \( p \)-combinations of \( E \) depends only on \( n \) and \( p \). It is denoted by \( \left( \begin{array}{l} n \\ p \end{array}\right) \) or also \( {C}_{n}^{p} \).

Proposition 10. Si \( 0 \leq p \leq n \) , on a \( \left( \begin{array}{l} n \\ p \end{array}\right) = \frac{n!}{p!\left( {n - p}\right) !} \) . Lorsque \( p > n \) on a \( \left( \begin{array}{l} n \\ p \end{array}\right) = 0 \) .

> Proposition 10. If \( 0 \leq p \leq n \), we have \( \left( \begin{array}{l} n \\ p \end{array}\right) = \frac{n!}{p!\left( {n - p}\right) !} \). When \( p > n \) we have \( \left( \begin{array}{l} n \\ p \end{array}\right) = 0 \).

Remarque 8. - La notation \( {C}_{n}^{p} \) est de moins en moins utilisée car peu commode.

> Remark 8. - The notation \( {C}_{n}^{p} \) is used less and less because it is inconvenient.

- Dans les combinaisons, les éléments sont distincts et leur ordre n'importe pas. Ainsi les combinaisons modélisent les tirages simultanés. Par exemple, dans un jeu de 52 cartes, le nombre de façons de tirer 10 cartes simultanément est (10).

> - In combinations, the elements are distinct and their order does not matter. Thus, combinations model simultaneous draws. For example, in a 52-card deck, the number of ways to draw 10 cards simultaneously is (10).

- Il est remarquable que \( \frac{n!}{p!\left( {n - p}\right) !} \) soit un entier. Cette propriété est utilisée dans le sujet d’étude 1 page 47 à partir de l’entier \( \left( \begin{matrix} {2n} \\  n \end{matrix}\right) \) pour prouver qu’il existe toujours au moins un nombre premier \( p \) vérifiant \( n < p < {2n} - 2 \) , dès que \( n \geq  4 \) .

> - It is remarkable that \( \frac{n!}{p!\left( {n - p}\right) !} \) is an integer. This property is used in study topic 1 on page 47 starting from the integer \( \left( \begin{matrix} {2n} \\  n \end{matrix}\right) \) to prove that there always exists at least one prime number \( p \) satisfying \( n < p < {2n} - 2 \), as soon as \( n \geq  4 \).

- Pour \( 1 \leq  p \leq  n \) , on appelle \( p \) -liste strictement croissante de \( \{ 1,\ldots , n\} \) toute famille d’entiers \( \left( {{i}_{1},\ldots ,{i}_{p}}\right) \) telle que \( 1 \leq  {i}_{1} < \ldots  < {i}_{p} \leq  n \) . Il y a \( \left( \begin{array}{l} n \\  p \end{array}\right) p \) -listes de cette forme. En effet, à chaque \( p \) -combinaison de \( \{ 1,\ldots , n\} \) on peut associer une et une seule \( p \) -liste strictement croissante en rangeant ses éléments par ordre croissant. De manière équivalente, le nombre de fonctions strictement croissantes de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) est \( \left( \begin{array}{l} n \\  p \end{array}\right) \) .

> - For \( 1 \leq  p \leq  n \), a strictly increasing \( p \)-list of \( \{ 1,\ldots , n\} \) is any family of integers \( \left( {{i}_{1},\ldots ,{i}_{p}}\right) \) such that \( 1 \leq  {i}_{1} < \ldots  < {i}_{p} \leq  n \). There are \( \left( \begin{array}{l} n \\  p \end{array}\right) p \) lists of this form. Indeed, to each \( p \)-combination of \( \{ 1,\ldots , n\} \) one can associate one and only one strictly increasing \( p \)-list by arranging its elements in increasing order. Equivalently, the number of strictly increasing functions from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \) is \( \left( \begin{array}{l} n \\  p \end{array}\right) \).

— On appelle p-combinaison avec répétition les p-listes dans lesquelles on autorise les répétitions mais dans lesquelles l'ordre ne compte pas. Les \( p \) -combinaisons avec répétition modélisent les tirages avec remise, dans lesquels l'ordre ne compte pas. Les \( p \) -combinaisons avec répétition d’un ensemble \( E \) de cardinal \( n \) sont au nombre de \( \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \) . Ce résultat est classique et fait l’objet de l’exercice 4 page 306 (trois preuves sont proposées).

> — A p-combination with repetition is defined as a p-list in which repetitions are allowed but order does not matter. \( p \) -combinations with repetition model draws with replacement where order does not matter. The number of \( p \) -combinations with repetition of a set \( E \) with cardinality \( n \) is \( \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \) . This result is classic and is the subject of exercise 4 on page 306 (three proofs are proposed).

Proposition 11. Soient \( n \) et \( p \) deux entiers naturels. Alors

> Proposition 11. Let \( n \) and \( p \) be two natural integers. Then

\[
{si0} \leq  p \leq  n,\;\left( \begin{array}{l} n \\  p \end{array}\right)  = \left( \begin{matrix} n \\  n - p \end{matrix}\right) ,
\]

(formule de symétrie)

> (symmetry formula)

\[
{sip}, n \geq  1,\;\left( \begin{array}{l} n \\  p \end{array}\right)  = \left( \begin{array}{l} n - 1 \\  p - 1 \end{array}\right)  + \left( \begin{matrix} n - 1 \\  p \end{matrix}\right) ,
\]

\[
\operatorname{si}p, n \geq  1,\;\left( \begin{array}{l} n \\  p \end{array}\right)  = \frac{n}{p}\left( \begin{array}{l} n - 1 \\  p - 1 \end{array}\right)  = \frac{n - p + 1}{p}\left( \begin{matrix} n \\  p - 1 \end{matrix}\right) ,
\]

\[
{sip}, n \geq  0,\;\left( \begin{array}{l} n + 1 \\  p + 1 \end{array}\right)  = \mathop{\sum }\limits_{{q = p}}^{n}\left( \begin{array}{l} q \\  p \end{array}\right) .
\]

Démonstration. Remarquons que lorsque \( p > n \) , il est facile d’obtenir les trois dernières propriétés (les termes sont nuls). On peut donc se placer dans le cas où \( p \leq n \) .

> Proof. Note that when \( p > n \) , it is easy to obtain the last three properties (the terms are zero). We can therefore assume the case where \( p \leq n \) .

Les trois premières propriétés sont faciles à montrer avec une approche combinatoire, ou à partir de la proprosition 10.

> The first three properties are easy to show using a combinatorial approach, or from proposition 10.

Pour montrer la dernière propriété on part de l’identité \( \left( \begin{array}{l} q \\ p \end{array}\right) = \left( \begin{array}{l} q + 1 \\ p + 1 \end{array}\right) - \left( \begin{matrix} q \\ p + 1 \end{matrix}\right) \) (consé- quence de la formule de Pascal) que l’on somme sur \( q \) . On peut aussi en obtenir une preuve combinatoire en procédant comme suit. Pour tout \( k,1 \leq k \leq n - p + 1 \) , on note \( {A}_{k} \) l’ensemble des parties \( P \) de \( \{ 1,\ldots , n + 1\} \) à \( p + 1 \) éléments tel que le plus petit entier dans \( P \) est \( k \) . Il y a autant d’éléments dans \( {A}_{k} \) que dans l’ensemble des parties de \( \{ k + 1,\ldots , n + 1\} \) à \( p \) éléments, donc \( \left| {A}_{k}\right| = \left( \begin{matrix} n - k + 1 \\ p \end{matrix}\right) \) . Comme toute partie de \( \{ 1,\ldots , n + 1\} \) à \( p + 1 \) éléments est dans l’un et l’un seulement des \( {A}_{k} \) avec \( 1 \leq k \leq n - p + 1 \) , on en déduit

> To show the last property, we start from the identity \( \left( \begin{array}{l} q \\ p \end{array}\right) = \left( \begin{array}{l} q + 1 \\ p + 1 \end{array}\right) - \left( \begin{matrix} q \\ p + 1 \end{matrix}\right) \) (a consequence of Pascal's formula) which we sum over \( q \) . We can also obtain a combinatorial proof by proceeding as follows. For any \( k,1 \leq k \leq n - p + 1 \) , we denote by \( {A}_{k} \) the set of subsets \( P \) of \( \{ 1,\ldots , n + 1\} \) with \( p + 1 \) elements such that the smallest integer in \( P \) is \( k \) . There are as many elements in \( {A}_{k} \) as in the set of subsets of \( \{ k + 1,\ldots , n + 1\} \) with \( p \) elements, thus \( \left| {A}_{k}\right| = \left( \begin{matrix} n - k + 1 \\ p \end{matrix}\right) \) . Since every subset of \( \{ 1,\ldots , n + 1\} \) with \( p + 1 \) elements is in one and only one of the \( {A}_{k} \) with \( 1 \leq k \leq n - p + 1 \) , we deduce

\[
\left( \begin{array}{l} n + 1 \\  p + 1 \end{array}\right)  = \mathop{\sum }\limits_{{k = 1}}^{{n - p + 1}}\left| {A}_{k}\right|  = \left( \begin{array}{l} n \\  p \end{array}\right)  + \left( \begin{matrix} n - 1 \\  p \end{matrix}\right)  + \cdots  + \left( \begin{array}{l} p \\  p \end{array}\right) .
\]

Proposition 12. Soit \( n \in \mathbb{N} \) . Alors

> Proposition 12. Let \( n \in \mathbb{N} \) . Then

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right)  = {2}^{n}
\]

PROPOSITION 13 (FORMULE DU BINÔME). Soient a et b deux éléments d'une algèbre, qui commutent (ab=ba). Alors on a

> PROPOSITION 13 (BINOMIAL THEOREM). Let a and b be two elements of an algebra that commute (ab=ba). Then we have

\[
{\left( a + b\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {a}^{k}{b}^{n - k}
\]

Remarque 9. - Cette formule justifie le nom de coefficients binomiaux pour les \( \left( \begin{array}{l} n \\ k \end{array}\right) \) .

> Remark 9. - This formula justifies the name binomial coefficients for \( \left( \begin{array}{l} n \\ k \end{array}\right) \) .

- Cette formule peut être utilisée lorsque \( a \) et \( b \) sont des nombres réels ou complexes, des polynômes, et aussi lorsque \( a \) et \( b \) sont des matrices qui commutent.

> - This formula can be used when \( a \) and \( b \) are real or complex numbers, polynomials, and also when \( a \) and \( b \) are matrices that commute.

La formule de Vandermonde énoncée ci-dessous n'est pas au programme des classes préparatoires mais elle est classique et il faut savoir la redémontrer.

> Vandermonde's identity stated below is not in the preparatory classes curriculum, but it is classic and one must know how to re-prove it.

Proposition 14 (FORMULE DE VANDERMONDE). Soient \( m, n \) et \( p \) des entiers naturels. Alors on a

> Proposition 14 (VANDERMONDE'S IDENTITY). Let \( m, n \) and \( p \) be natural integers. Then we have

\[
\mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{matrix} m \\  p - k \end{matrix}\right)  = \left( \begin{matrix} n + m \\  p \end{matrix}\right)
\]

Démonstration. Une preuve algébrique est immédiate en utilisant la formule du binôme, à partir de l’identité \( {\left( 1 + X\right) }^{n}{\left( 1 + X\right) }^{m} = {\left( 1 + X\right) }^{m + n} \) . Si \( p > m + n \) les deux termes de l’expression sont nuls donc l’identité est vraie. Supposons maintenant \( p \leq n + m \) . Par commodité, on développe \( {\left( 1 + X\right) }^{n} \) par la formule du binôme en poursuivant jusqu’au degré \( n + m \) (on peut le faire car lorsque \( k > n \) , on a \( \left( \begin{array}{l} n \\ k \end{array}\right) = 0 \) ), on fait la même chose pour \( {\left( 1 + X\right) }^{m} \) . On obtient

> Proof. An algebraic proof is immediate using the binomial theorem, starting from the identity \( {\left( 1 + X\right) }^{n}{\left( 1 + X\right) }^{m} = {\left( 1 + X\right) }^{m + n} \). If \( p > m + n \) both terms of the expression are zero, so the identity is true. Now assume \( p \leq n + m \). For convenience, we expand \( {\left( 1 + X\right) }^{n} \) using the binomial theorem, continuing up to degree \( n + m \) (this is possible because when \( k > n \), we have \( \left( \begin{array}{l} n \\ k \end{array}\right) = 0 \)), and we do the same for \( {\left( 1 + X\right) }^{m} \). We obtain

\[
\left( {\mathop{\sum }\limits_{{i = 0}}^{{n + m}}\left( \begin{array}{l} n \\  i \end{array}\right) {X}^{i}}\right) \left( {\mathop{\sum }\limits_{{j = 0}}^{{n + m}}\left( \begin{matrix} m \\  j \end{matrix}\right) {X}^{j}}\right)  = \mathop{\sum }\limits_{{p = 0}}^{{n + m}}\left( \begin{matrix} n + m \\  p \end{matrix}\right) {X}^{p}.
\]

Avec ce tour de passe-passe, on en déduit immédiatement par produit de polynômes, que le coefficient de \( {X}^{p} \) dans le terme de gauche est égal à

> With this sleight of hand, we immediately deduce by polynomial multiplication that the coefficient of \( {X}^{p} \) in the left-hand term is equal to

\[
\mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{matrix} m \\  p - k \end{matrix}\right)
\]

et celui de droite est égal à \( \left( \begin{matrix} n + m \\ p \end{matrix}\right) \) , d’où le résultat.

> and the one on the right is equal to \( \left( \begin{matrix} n + m \\ p \end{matrix}\right) \), hence the result.

Remarque 10. - La formule de Vandermonde est vérifiée même si \( p > n \) ou \( p > m \) (rappelons que \( \left( \begin{array}{l} n \\ k \end{array}\right) = 0 \) si \( k > n \) ).

> Remark 10. - Vandermonde's identity holds even if \( p > n \) or \( p > m \) (recall that \( \left( \begin{array}{l} n \\ k \end{array}\right) = 0 \) if \( k > n \)).

- On peut aussi en donner une preuve combinatoire, en comptant de deux manières différentes le nombre de parties à \( p \) éléments d’un ensemble \( E \cup  F \) , ou \( E \) et \( F \) sont disjoints de cardinal respectifs \( m \) et \( n \) .

> - One can also provide a combinatorial proof by counting in two different ways the number of subsets with \( p \) elements of a set \( E \cup  F \), where \( E \) and \( F \) are disjoint with respective cardinalities \( m \) and \( n \).

- Dans le cas particulier où \( m = p \) , on en déduit (en utilisant la formule de symétrie)

> - In the special case where \( m = p \), we deduce (using the symmetry formula)

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{array}{l} m \\  k \end{array}\right)  = \left( \begin{matrix} n + m \\  m \end{matrix}\right)
\]

En particulier si \( n = m \) on obtient

> In particular, if \( n = m \) we obtain

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( \begin{array}{l} n \\  k \end{array}\right) }^{2} = \left( \begin{matrix} {2n} \\  n \end{matrix}\right)
\]

Coefficient multinomial.

> Multinomial coefficient.

Proposition 15. Soit \( E \) un ensemble fini non vide et soit \( n = \left| E\right| \) . Soit \( p \in {\mathbb{N}}^{ * } \) et \( {i}_{1},\ldots ,{i}_{p} \) des entiers naturels tels que \( {i}_{1} + \cdots + {i}_{p} = n \) . Alors le nombre de partitions ordonnées \( \left( {{A}_{1},\ldots ,{A}_{p}}\right) \) de \( E \) , telles que pour tout \( k,\left| {A}_{k}\right| = {i}_{k} \) est égal à

> Proposition 15. Let \( E \) be a non-empty finite set and let \( n = \left| E\right| \). Let \( p \in {\mathbb{N}}^{ * } \) and \( {i}_{1},\ldots ,{i}_{p} \) be natural integers such that \( {i}_{1} + \cdots + {i}_{p} = n \). Then the number of ordered partitions \( \left( {{A}_{1},\ldots ,{A}_{p}}\right) \) of \( E \), such that for all \( k,\left| {A}_{k}\right| = {i}_{k} \) is equal to

\[
\left( \begin{matrix} n \\  {i}_{1},\ldots ,{i}_{p} \end{matrix}\right)  = \frac{n!}{{i}_{1}!\cdots {i}_{p}!}.
\]

Proposition 16 (FORMULE DU MULTINOME). Soient \( {a}_{1},\ldots ,{a}_{p} \) des éléments d’une al-gèbre qui commutent deux à deux. Alors pour tout \( n \in {\mathbb{N}}^{ * } \) on a

> Proposition 16 (MULTINOMIAL THEOREM). Let \( {a}_{1},\ldots ,{a}_{p} \) be elements of an algebra that commute pairwise. Then for all \( n \in {\mathbb{N}}^{ * } \) we have

\[
{\left( {a}_{1} + \cdots  + {a}_{p}\right) }^{n} = \mathop{\sum }\limits_{\substack{{{i}_{1},\ldots ,{i}_{p} \in  \mathbb{N}} \\  {{i}_{1} + \cdots  + {i}_{p} = n} }}\left( \begin{matrix} n \\  {i}_{1},\ldots ,{i}_{p} \end{matrix}\right) {a}_{1}^{{i}_{1}}\cdots {a}_{p}^{{i}_{p}}.
\]
