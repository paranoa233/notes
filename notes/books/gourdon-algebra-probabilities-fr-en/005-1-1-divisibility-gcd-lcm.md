#### 1.1. Divisibility - gcd, lcm

*Français : 1.1. Divisibilité - pgcd, ppcm*

DéFINITION 1. Soient \( a \) et \( b \) deux entiers relatifs. On dit que a divise \( b \) (ou que \( b \) est un multiple de \( a \) ), et on note \( a \mid b \) , s’il existe un entier \( n \) tel que \( b = {an} \) . Si \( a \) ne divise pas \( b \) , on note \( a \nmid b \) .

> DEFINITION 1. Let \( a \) and \( b \) be two relative integers. We say that a divides \( b \) (or that \( b \) is a multiple of \( a \) ), and we denote it \( a \mid b \) , if there exists an integer \( n \) such that \( b = {an} \) . If \( a \) does not divide \( b \) , we denote it \( a \nmid b \) .

Proposition 1 (DIVISION EUCLIDIENNE). Soient \( a \in \mathbb{Z}, b \in {\mathbb{N}}^{ * } \) . Il existe un unique couple \( \left( {q, r}\right) \in \mathbb{Z} \times \mathbb{N} \) tel que

> Proposition 1 (EUCLIDEAN DIVISION). Let \( a \in \mathbb{Z}, b \in {\mathbb{N}}^{ * } \) . There exists a unique pair \( \left( {q, r}\right) \in \mathbb{Z} \times \mathbb{N} \) such that

\[
a = {bq} + r,\;\text{ avec }\;0 \leq  r \leq  b - 1.
\]

\( q \) s’appelle le quotient, \( r \) le reste, de la division euclidienne de a par \( b \) .

> \( q \) is called the quotient, \( r \) the remainder, of the Euclidean division of a by \( b \) .

Classes de congruence modulo \( n \) .

> Congruence classes modulo \( n \) .

DéFINITION 2. Soit \( n \) un entier naturel non nul. On note \( n\mathbb{Z} = \{ {nk}, k \in \mathbb{Z}\} \) . Si \( x \) et \( y \) sont deux entiers, on note \( x \equiv y\left( {\;\operatorname{mod}\;n}\right) \) si \( x - y \in n\mathbb{Z} \) . et on dit alors que \( x \) et \( y \) sont congrus modulo \( n \) .

> DEFINITION 2. Let \( n \) be a non-zero natural integer. We denote \( n\mathbb{Z} = \{ {nk}, k \in \mathbb{Z}\} \) . If \( x \) and \( y \) are two integers, we denote \( x \equiv y\left( {\;\operatorname{mod}\;n}\right) \) if \( x - y \in n\mathbb{Z} \) . and we then say that \( x \) and \( y \) are congruent modulo \( n \) .

DéFINITION 3. Soit \( n \) un entier naturel non nul. L’anneau quotient de \( \mathbb{Z} \) par \( n\mathbb{Z} \) est noté \( \mathbb{Z}/n\mathbb{Z} \) . On note généralement \( \bar{x} \) (ou \( \dot{x} \) ) la classe d’un entier \( x \) dans \( \mathbb{Z}/n\mathbb{Z} \) . Ainsi, \( \mathbb{Z}/n\mathbb{Z} = \{ \overline{0},\overline{1},\ldots ,\overline{n - 1}\} . \)

> DEFINITION 3. Let \( n \) be a non-zero natural integer. The quotient ring of \( \mathbb{Z} \) by \( n\mathbb{Z} \) is denoted \( \mathbb{Z}/n\mathbb{Z} \) . We generally denote \( \bar{x} \) (or \( \dot{x} \) ) the class of an integer \( x \) in \( \mathbb{Z}/n\mathbb{Z} \) . Thus, \( \mathbb{Z}/n\mathbb{Z} = \{ \overline{0},\overline{1},\ldots ,\overline{n - 1}\} . \)

##### GCD.

*Français : PGCD.*

DéFINITION 4. - Soient \( {a}_{1},\ldots ,{a}_{n} \) des entiers. Il existe un unique entier naturel \( d \) tel que \( {a}_{1}\mathbb{Z} + \cdots + {a}_{n}\mathbb{Z} = d\mathbb{Z} \) . Ainsi défini, \( d \) s’appelle le pgcd de \( {a}_{1},\ldots ,{a}_{n} \) et on note \( d = \operatorname{pgcd}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . L’entier \( d \) est aussi le plus grand entier naturel divisant tous les \( {a}_{i}\left( {1 \leq i \leq n}\right) \) .

> DEFINITION 4. - Let \( {a}_{1},\ldots ,{a}_{n} \) be integers. There exists a unique natural integer \( d \) such that \( {a}_{1}\mathbb{Z} + \cdots + {a}_{n}\mathbb{Z} = d\mathbb{Z} \) . Thus defined, \( d \) is called the gcd of \( {a}_{1},\ldots ,{a}_{n} \) and is denoted by \( d = \operatorname{pgcd}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . The integer \( d \) is also the largest natural integer dividing all \( {a}_{i}\left( {1 \leq i \leq n}\right) \) .

- Lorsque pgcd \( \left( {{a}_{1},\ldots ,{a}_{n}}\right)  = 1 \) , on dit que les entiers \( {a}_{1},\ldots ,{a}_{n} \) sont premiers entre eux dans leur ensemble. Lorsque pgcd \( \left( {{a}_{i},{a}_{j}}\right)  = 1 \) dès que \( i \neq  j \) , les entiers \( {a}_{i} \) sont dits premiers entre eux deux à deux.

> - When gcd \( \left( {{a}_{1},\ldots ,{a}_{n}}\right)  = 1 \) , the integers \( {a}_{1},\ldots ,{a}_{n} \) are said to be coprime as a set. When gcd \( \left( {{a}_{i},{a}_{j}}\right)  = 1 \) whenever \( i \neq  j \) , the integers \( {a}_{i} \) are said to be pairwise coprime.

Remarque 1. - Des entiers premiers entre eux deux à deux sont premiers entre eux dans leur ensemble.

> Remark 1. - Pairwise coprime integers are coprime as a set.

- Il résulte de la définition du pgcd que les diviseurs communs à une famille d'entiers sont les diviseurs du pgcd.

> - It follows from the definition of the gcd that the common divisors of a family of integers are the divisors of the gcd.

- Lorsque \( {a}_{1},\ldots ,{a}_{n} \) sont des entiers, on a

> - When \( {a}_{1},\ldots ,{a}_{n} \) are integers, we have

\[
\forall a \in  \mathbb{Z},\;\operatorname{pgcd}\left( {a{a}_{1},\ldots , a{a}_{n}}\right)  = \left| a\right| \operatorname{pgcd}\left( {{a}_{1},\ldots ,{a}_{n}}\right) .
\]

- Le pgcd de deux entiers \( a \) et \( b \) se note aussi \( a \land  b \) .

> - The gcd of two integers \( a \) and \( b \) is also denoted by \( a \land  b \) .

\( \rightarrow \) THÉORÉME 1 (BEZOUT). Des entiers \( {a}_{1},\ldots ,{a}_{n} \) sont premiers entre eux dans leur ensemble si et seulement s’il existe des entiers \( {u}_{1},\ldots ,{u}_{n} \) tels que \( {u}_{1}{a}_{1} + \cdots + {u}_{n}{a}_{n} = 1 \) .

> \( \rightarrow \) THEOREM 1 (BEZOUT). Integers \( {a}_{1},\ldots ,{a}_{n} \) are coprime as a whole if and only if there exist integers \( {u}_{1},\ldots ,{u}_{n} \) such that \( {u}_{1}{a}_{1} + \cdots + {u}_{n}{a}_{n} = 1 \) .

Remarque 2. Lorsque deux entiers \( a \) et \( b \) sont premiers entre eux, le théorème de Bezout assure l’existence d’un couple \( \left( {u, v}\right) \in {\mathbb{Z}}^{2} \) tel que \( {au} + {bv} = 1 \) . Il existe un moyen pratique de calculer un tel couple ( \( u, v \) ), appelé algorithme d’Euclide (voir l’exercice 2).

> Remark 2. When two integers \( a \) and \( b \) are coprime, Bezout's theorem ensures the existence of a pair \( \left( {u, v}\right) \in {\mathbb{Z}}^{2} \) such that \( {au} + {bv} = 1 \) . There is a practical way to calculate such a pair ( \( u, v \) ), called the Euclidean algorithm (see exercise 2).

- THÉORÉME 2 (GAUSS). Soient a, b et c trois entiers. Si a divise le produit bc et si a et b sont premiers entre eux, alors a divise c.

> - THEOREM 2 (GAUSS). Let a, b, and c be three integers. If a divides the product bc and if a and b are coprime, then a divides c.

Proposition 2. Si un entier a est premier avec des entiers \( {b}_{1},\ldots ,{b}_{n} \) , alors a est premier avec le produit \( {b}_{1}\ldots {b}_{n} \) .

> Proposition 2. If an integer a is coprime to integers \( {b}_{1},\ldots ,{b}_{n} \) , then a is coprime to the product \( {b}_{1}\ldots {b}_{n} \) .

Proposition 3. Soient \( {a}_{1},\ldots ,{a}_{n}n \) entiers premiers entre eux deux à deux et b un entier. Le produit \( {a}_{1}\cdots {a}_{n} \) divise \( b \) si et seulement si pour tout \( i,{a}_{i} \) divise \( b \) .

> Proposition 3. Let \( {a}_{1},\ldots ,{a}_{n}n \) be pairwise coprime integers and b an integer. The product \( {a}_{1}\cdots {a}_{n} \) divides \( b \) if and only if for all \( i,{a}_{i} \) divides \( b \) .

PPCM.

> DéFINITION 5. Soient \( {a}_{1},\ldots ,{a}_{n} \) des entiers. Il existe un unique entier naturel \( d \) tel que \( {a}_{1}\mathbb{Z} \cap \cdots \cap {a}_{n}\mathbb{Z} = d\mathbb{Z} \) . Ainsi défini, \( d \) s’appelle le \( {ppcm} \) de \( {a}_{1},\ldots ,{a}_{n} \) et on note \( d = \) ppcm \( \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . L’entier \( d \) est aussi le plus petit entier naturel non nul multiple de tous les \( {a}_{i}\left( {1 \leq i \leq n}\right) \) .

DEFINITION 5. Let \( {a}_{1},\ldots ,{a}_{n} \) be integers. There exists a unique natural integer \( d \) such that \( {a}_{1}\mathbb{Z} \cap \cdots \cap {a}_{n}\mathbb{Z} = d\mathbb{Z} \) . Thus defined, \( d \) is called the \( {ppcm} \) of \( {a}_{1},\ldots ,{a}_{n} \) and is denoted \( d = \) lcm \( \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . The integer \( d \) is also the smallest non-zero natural integer that is a multiple of all \( {a}_{i}\left( {1 \leq i \leq n}\right) \) .

> Remarque 3. - Il résulte de cette définition que les multiples communs à une famille d'entiers sont les multiples de leur ppcm.

Remark 3. - It follows from this definition that the common multiples of a family of integers are the multiples of their lcm.

> - On a facilement

- We easily have

\[
\forall a \in  \mathbb{Z},\;\operatorname{ppcm}\left( {a{a}_{1},\ldots , a{a}_{n}}\right)  = \left| a\right| \operatorname{ppcm}\left( {{a}_{1},\ldots ,{a}_{n}}\right) .
\]

- Le ppcm de deux entiers \( a \) et \( b \) se note aussi \( a \vee  b \) .

> - The lcm of two integers \( a \) and \( b \) is also denoted \( a \vee  b \) .

Proposition 4. Soient \( {a}_{1},\ldots ,{a}_{n} \) des entiers premiers entre eux deux à deux. Alors

> Proposition 4. Let \( {a}_{1},\ldots ,{a}_{n} \) be pairwise coprime integers. Then

\[
\operatorname{ppcm}\left( {{a}_{1},\ldots ,{a}_{n}}\right)  = \left| {{a}_{1}\cdots {a}_{n}}\right| .
\]

Proposition 5. Pour deux entiers a et b, on a pgcd \( \left( {a, b}\right) \times \operatorname{ppcm}\left( {a, b}\right) = \left| {ab}\right| \) .

> Proposition 5. For two integers a and b, we have gcd \( \left( {a, b}\right) \times \operatorname{ppcm}\left( {a, b}\right) = \left| {ab}\right| \) .
