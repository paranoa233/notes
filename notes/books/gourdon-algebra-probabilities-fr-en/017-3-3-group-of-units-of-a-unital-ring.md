#### 3.3. Group of units of a unital ring

*Français : 3.3. Groupe des inversibles d'un anneau unitaire*

On rappelle que les élément d’un anneau unitaire \( \left( {A,+, \cdot }\right) \) inversibles pour la loi ⋅ sont appelés les inversibles de l’anneau \( A \) .

> Recall that the elements of a unital ring \( \left( {A,+, \cdot }\right) \) that are invertible under the operation ⋅ are called the units of the ring \( A \).

DÉFINITION 10. L'ensemble des inversibles d'un anneau unitaire \( A \) , muni de la loi multiplicative, est un groupe appelé groupe des inversibles de \( A \) .

> DEFINITION 10. The set of units of a unital ring \( A \), equipped with the multiplicative operation, is a group called the group of units of \( A \).

Proposition 4. Soit un entier \( n \geq 2 \) et \( k \) un entier. L’élément \( k \) (classe de \( k \) dans \( \mathbb{Z}/n\mathbb{Z} \) ) est inversible dans \( \mathbb{Z}/n\mathbb{Z} \) si et seulement si \( k \land n = 1 \) .

> Proposition 4. Let \( n \geq 2 \) be an integer and \( k \) an integer. The element \( k \) (the class of \( k \) in \( \mathbb{Z}/n\mathbb{Z} \)) is invertible in \( \mathbb{Z}/n\mathbb{Z} \) if and only if \( k \land n = 1 \).

\( \rightarrow \) THÉORÉME 1 (DES CHINOIS). Soient \( m \) et \( n \) deux entiers naturels non nuls premiers entre eux. Les anneaux \( \left( {\mathbb{Z}/m\mathbb{Z}}\right) \times \left( {\mathbb{Z}/n\mathbb{Z}}\right) \) et \( \mathbb{Z}/{mn}\mathbb{Z} \) sont isomorphes.

> \( \rightarrow \) THEOREM 1 (CHINESE REMAINDER THEOREM). Let \( m \) and \( n \) be two non-zero natural numbers that are coprime. The rings \( \left( {\mathbb{Z}/m\mathbb{Z}}\right) \times \left( {\mathbb{Z}/n\mathbb{Z}}\right) \) and \( \mathbb{Z}/{mn}\mathbb{Z} \) are isomorphic.

Démonstration. On considère l'application

> Proof. Consider the map

\[
f : \mathbb{Z} \rightarrow  \mathbb{Z}/m\mathbb{Z} \times  \mathbb{Z}/n\mathbb{Z}\;x \mapsto  \left( {\dot{x},\bar{x}}\right) .
\]

C’est un morphisme d’anneaux, de noyau Ker \( f = \{ x \in \mathbb{Z}\left| \;\right| m \mid x \) et \( n \mid x\} \) . Comme \( m \land n = 1 \) , on a aussi Ker \( f = \{ x \in \mathbb{Z}\left| {\;{mn}}\right| x\} = {mn}\mathbb{Z} \) . Donc \( f\left( \mathbb{Z}\right) \) et \( \mathbb{Z}/{mn}\mathbb{Z} \) sont isomorphes. En particulier, \( \operatorname{Card}\left( {f\left( \mathbb{Z}\right) }\right) = \operatorname{Card}\left( {\mathbb{Z}/{mn}\mathbb{Z}}\right) = {mn} \) et donc \( f\left( \mathbb{Z}\right) = \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z} \) . Finalement, on vient de montrer que \( \mathbb{Z}/{mn}\mathbb{Z} \) et \( \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z} \) sont isomorphes.

> It is a ring homomorphism with kernel Ker \( f = \{ x \in \mathbb{Z}\left| \;\right| m \mid x \) and \( n \mid x\} \). Since \( m \land n = 1 \), we also have Ker \( f = \{ x \in \mathbb{Z}\left| {\;{mn}}\right| x\} = {mn}\mathbb{Z} \). Thus \( f\left( \mathbb{Z}\right) \) and \( \mathbb{Z}/{mn}\mathbb{Z} \) are isomorphic. In particular, \( \operatorname{Card}\left( {f\left( \mathbb{Z}\right) }\right) = \operatorname{Card}\left( {\mathbb{Z}/{mn}\mathbb{Z}}\right) = {mn} \) and therefore \( f\left( \mathbb{Z}\right) = \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z} \). Finally, we have just shown that \( \mathbb{Z}/{mn}\mathbb{Z} \) and \( \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z} \) are isomorphic.

Remarque 3. - En procédant par récurrence sur \( p \) , on montre que si \( {n}_{1},\ldots ,{n}_{p} \) sont premiers entre eux deux à deux, alors \( \mathbb{Z}/{n}_{1}\cdots {n}_{p}\mathbb{Z} \) et \( \mathbb{Z}/{n}_{1}\mathbb{Z} \times \cdots \times \mathbb{Z}/{n}_{p}\mathbb{Z} \) sont isomorphes.

> Remark 3. - By proceeding by induction on \( p \), we show that if \( {n}_{1},\ldots ,{n}_{p} \) are pairwise coprime, then \( \mathbb{Z}/{n}_{1}\cdots {n}_{p}\mathbb{Z} \) and \( \mathbb{Z}/{n}_{1}\mathbb{Z} \times \cdots \times \mathbb{Z}/{n}_{p}\mathbb{Z} \) are isomorphic.

- La surjectivité de l’application \( f \) prouve que si \( m \land  n = 1 \) , alors

> - The surjectivity of the map \( f \) proves that if \( m \land  n = 1 \), then

\[
\left( {\forall a, b \in  \mathbb{Z},\exists x \in  \mathbb{Z}}\right) ,\;x \equiv  a\;\left( {\;\operatorname{mod}\;m}\right) \;\text{ et }\;x \equiv  b\;\left( {\;\operatorname{mod}\;n}\right) .
\]

Dans la pratique, la méthode de recherche d’un tel élément \( x \) peut se faire comme suit.

> In practice, the method for finding such an element \( x \) can be done as follows.

- On cherche \( u \) et \( v \) tels que \( {um} + {vn} = 1 \) grâce à l’algorithme d’Euclide (voir l'exercice 2 page 12)

> - We seek \( u \) and \( v \) such that \( {um} + {vn} = 1 \) using the Euclidean algorithm (see exercise 2 on page 12)

- Il suffit alors de prendre \( x = a + {um}\left( {b - a}\right) \) (par exemple).

> - It then suffices to take \( x = a + {um}\left( {b - a}\right) \) (for example).

##### Euler's totient function.

*Français : Indicateur d'Euler.*

DéFINITION 11. Soit un entier \( n > 1 \) . Notons \( {G}_{n} \) le groupe des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) . On appelle indicateur d’Euler de \( n \) l’entier \( \varphi \left( n\right) = \operatorname{Card}\left( {G}_{n}\right) \) . D’après la proposition 4, \( \varphi \left( n\right) \) est aussi le nombre d’entiers \( k \in \{ 1,2,\cdots , n\} \) tels que \( k \land n = 1 \) .

> DEFINITION 11. Let \( n > 1 \) be an integer. Let \( {G}_{n} \) denote the group of units of \( \mathbb{Z}/n\mathbb{Z} \) . The Euler totient function of \( n \) is the integer \( \varphi \left( n\right) = \operatorname{Card}\left( {G}_{n}\right) \) . According to proposition 4, \( \varphi \left( n\right) \) is also the number of integers \( k \in \{ 1,2,\cdots , n\} \) such that \( k \land n = 1 \) .

Remarque 4. En vertu de la proposition 5 page 22, le nombre de générateurs d'un groupe cyclique d’ordre \( n \) (typiquement \( \mathbb{Z}/n\mathbb{Z} \) ) est \( \varphi \left( n\right) \) .

> Remark 4. By virtue of proposition 5 on page 22, the number of generators of a cyclic group of order \( n \) (typically \( \mathbb{Z}/n\mathbb{Z} \) ) is \( \varphi \left( n\right) \) .

THÉORÉME 2 (EULER). Soit un entier \( n > 1 \) . Si k est un entier premier avec n, on a \( {k}^{\varphi \left( n\right) } \equiv 1\left( {\;\operatorname{mod}\;n}\right) . \)

> THEOREM 2 (EULER). Let \( n > 1 \) be an integer. If k is an integer coprime to n, then \( {k}^{\varphi \left( n\right) } \equiv 1\left( {\;\operatorname{mod}\;n}\right) . \)

Démonstration. Si \( k \land n = 1 \) , alors \( \dot{k} \) est élément du groupe \( {G}_{n} \) des inversibles de \( \mathbb{Z}/n\mathbb{Z} \) d’après la proposition 4. Comme l’ordre de \( {G}_{n} \) vaut \( \varphi \left( n\right) \) , on en déduit \( {\dot{k}}^{\varphi \left( n\right) } = \dot{1} \) dans \( \mathbb{Z}/n\mathbb{Z} \) , d’où le résultat.

> Proof. If \( k \land n = 1 \) , then \( \dot{k} \) is an element of the group \( {G}_{n} \) of units of \( \mathbb{Z}/n\mathbb{Z} \) according to proposition 4. Since the order of \( {G}_{n} \) is \( \varphi \left( n\right) \) , we deduce \( {\dot{k}}^{\varphi \left( n\right) } = \dot{1} \) in \( \mathbb{Z}/n\mathbb{Z} \) , hence the result.

Ce dernier résultat généralise le théorème de Fermat. Le calcul de \( \varphi \left( n\right) \) fait l’objet de la proposition suivante.

> This last result generalizes Fermat's theorem. The calculation of \( \varphi \left( n\right) \) is the subject of the following proposition.

Proposition 5. Soit \( n \geq 2 \) un entier, \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) sa décomposition en facteurs premiers. Alors

> Proposition 5. Let \( n \geq 2 \) be an integer, \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) its prime factorization. Then

\[
\varphi \left( n\right)  = {p}_{1}^{{\alpha }_{1} - 1}\cdots {p}_{k}^{{\alpha }_{k} - 1}\left( {{p}_{1} - 1}\right) \cdots \left( {{p}_{k} - 1}\right)  = n\left( {1 - \frac{1}{{p}_{1}}}\right) \cdots \left( {1 - \frac{1}{{p}_{k}}}\right) .
\]

Démonstration. Soit \( p \) un nombre premier et \( \alpha \in {\mathbb{N}}^{ * } \) . Alors \( k \) n’est pas premier avec \( {p}^{\alpha } \) si et seulement si \( p \mid k \) . L’ensemble des nombres de \( \left\{ {1,2,\ldots ,{p}^{\alpha }}\right\} \) non premiers avec \( p \) est donc \( \left\{ {p,{2p},{3p},\ldots ,\left( {p}^{\alpha - 1}\right) p}\right\} \) . Ce dernier étant de cardinal \( {p}^{\alpha - 1} \) , on en tire \( \varphi \left( {p}^{\alpha }\right) = {p}^{\alpha } - {p}^{\alpha - 1}\;\left( *\right) \) .

> Proof. Let \( p \) be a prime number and \( \alpha \in {\mathbb{N}}^{ * } \) . Then \( k \) is not coprime to \( {p}^{\alpha } \) if and only if \( p \mid k \) . The set of numbers in \( \left\{ {1,2,\ldots ,{p}^{\alpha }}\right\} \) not coprime to \( p \) is therefore \( \left\{ {p,{2p},{3p},\ldots ,\left( {p}^{\alpha - 1}\right) p}\right\} \) . The latter having cardinality \( {p}^{\alpha - 1} \) , we derive \( \varphi \left( {p}^{\alpha }\right) = {p}^{\alpha } - {p}^{\alpha - 1}\;\left( *\right) \) .

- Si \( m \) et \( n \) sont premiers entre eux, d’après le théorème des Chinois, \( \mathbb{Z}/m\mathbb{Z} \times  \mathbb{Z}/n\mathbb{Z} \) est isomorphe à \( \mathbb{Z}/{mn}\mathbb{Z} \) . En restreignant l’isomorphisme à \( {G}_{m} \times  {G}_{n} \) , on voit que \( {G}_{m} \times  {G}_{n} \) est isomorphe à \( {G}_{mn} \) . Donc \( \varphi \left( {mn}\right)  = \varphi \left( m\right) \varphi \left( n\right) \;\left( {* * }\right) \) .

> - If \( m \) and \( n \) are coprime, by the Chinese Remainder Theorem, \( \mathbb{Z}/m\mathbb{Z} \times  \mathbb{Z}/n\mathbb{Z} \) is isomorphic to \( \mathbb{Z}/{mn}\mathbb{Z} \) . By restricting the isomorphism to \( {G}_{m} \times  {G}_{n} \) , we see that \( {G}_{m} \times  {G}_{n} \) is isomorphic to \( {G}_{mn} \) . Thus \( \varphi \left( {mn}\right)  = \varphi \left( m\right) \varphi \left( n\right) \;\left( {* * }\right) \) .

- Si maintenant \( n \geq  2 \) est un entier dont la décomposition en facteurs premiers est \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) , on a d’après (**) \( \varphi \left( n\right)  = \varphi \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \varphi \left( {p}_{k}^{{\alpha }_{k}}\right) \) , d’où le résultat d’après (*).

> - If \( n \geq  2 \) is now an integer whose prime factorization is \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) , we have by (**) \( \varphi \left( n\right)  = \varphi \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \varphi \left( {p}_{k}^{{\alpha }_{k}}\right) \) , hence the result by (*).

Remarque 5. En particulier si \( p \) est un nombre premier, \( \varphi \left( p\right) = p - 1 \) et on retrouve le théorème de Fermat avec le théorème 2.

> Remark 5. In particular, if \( p \) is a prime number, \( \varphi \left( p\right) = p - 1 \) and we recover Fermat's Little Theorem with Theorem 2.

Proposition 6. Pour tout entier \( n \geq 2 \) , on a \( n = \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) \) .

> Proposition 6. For any integer \( n \geq 2 \) , we have \( n = \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) \) .

Démonstration. Considérons les fractions

> Proof. Consider the fractions

\[
\frac{1}{n},\frac{2}{n},\cdots ,\frac{n - 1}{n},\frac{n}{n}.
\]

Nous cherchons à les mettre sous forme irréductible \( \frac{a}{d} \) ou \( d \) doit nécessairement diviser \( n \) . Pour chaque \( d \) divisant \( n \) , il y a \( \varphi \left( d\right) \) numérateurs \( a \) possibles (puisque le nombre d’entiers \( a \) tels que \( a \land d = 1 \) est \( \varphi \left( d\right) ) \) . Comme il y a en tout \( n \) fractions, on en déduit le résultat.

> We seek to put them in irreducible form \( \frac{a}{d} \) where \( d \) must necessarily divide \( n \) . For each \( d \) dividing \( n \) , there are \( \varphi \left( d\right) \) possible numerators \( a \) (since the number of integers \( a \) such that \( a \land d = 1 \) is \( \varphi \left( d\right) ) \) . As there are \( n \) fractions in total, we deduce the result.
