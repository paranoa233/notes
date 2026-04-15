#### 2.3. Symmetric group

*Français : 2.3. Groupe symétrique*

DÉFINITION 11. Pour tout entier naturel \( n \) non nul, on note \( {\mathcal{S}}_{n} \) le groupe des permutations de \( \{ 1,\ldots , n\} \) (muni de la loi de composition). Le groupe \( {\mathcal{S}}_{n} \) est appelé groupe symétrique d’indice \( n \) . Si \( s \in {\mathcal{S}}_{n} \) , on note \( s = \left( \begin{matrix} 1 & 2 & \cdots & n \\ s\left( 1\right) & s\left( 2\right) & \cdots & s\left( n\right) \end{matrix}\right) \) .

> DEFINITION 11. For any non-zero natural number \( n \), we denote by \( {\mathcal{S}}_{n} \) the group of permutations of \( \{ 1,\ldots , n\} \) (equipped with the composition law). The group \( {\mathcal{S}}_{n} \) is called the symmetric group of index \( n \). If \( s \in {\mathcal{S}}_{n} \), we denote it by \( s = \left( \begin{matrix} 1 & 2 & \cdots & n \\ s\left( 1\right) & s\left( 2\right) & \cdots & s\left( n\right) \end{matrix}\right) \).

Remarque 7. On a \( \operatorname{Card}\left( {\mathcal{S}}_{n}\right) = n! \) .

> Remark 7. We have \( \operatorname{Card}\left( {\mathcal{S}}_{n}\right) = n! \).

DÉFINITION 12. Lorsque \( i \neq j \) , on appelle transposition sur \( i, j \) la permutation notée \( {\tau }_{i, j} \) permutant les éléments \( i \) et \( j \) :

> DEFINITION 12. When \( i \neq j \), a transposition on \( i, j \) is the permutation denoted by \( {\tau }_{i, j} \) that swaps the elements \( i \) and \( j \):

\[
{\tau }_{i, j} = \left( \begin{array}{lllllllllll} 1 & \cdots & i - 1 & \mathbf{i} & i + 1 & \cdots & j - 1 & \mathbf{j} & j + 1 & \cdots & n \\  1 & \cdots & i - 1 & \mathbf{j} & i + 1 & \cdots & j - 1 & \mathbf{i} & j + 1 & \cdots & n \end{array}\right) .
\]

THÉORÉME 5. Tout élément de \( {\mathcal{S}}_{n} \) se décompose en produit de transpositions.

> THEOREM 5. Every element of \( {\mathcal{S}}_{n} \) can be decomposed into a product of transpositions.

DéFINITION 13. Si \( s \in {\mathcal{S}}_{n} \) et \( a \in \{ 1,\ldots , n\} \) , on appelle orbite de \( a \) suivant \( s \) l’ensemble \( {\mathcal{O}}_{s}\left( a\right) = \left\{ {{s}^{k}\left( a\right) , k \in \mathbb{Z}}\right\} . \)

> DEFINITION 13. If \( s \in {\mathcal{S}}_{n} \) and \( a \in \{ 1,\ldots , n\} \), the orbit of \( a \) under \( s \) is the set \( {\mathcal{O}}_{s}\left( a\right) = \left\{ {{s}^{k}\left( a\right) , k \in \mathbb{Z}}\right\} . \)

DéFINITION 14. Soit \( \gamma \in {\mathcal{S}}_{n} \) . On dit que \( \gamma \) est un cycle si parmi les \( {\mathcal{O}}_{\gamma }\left( a\right) ,1 \leq a \leq n \) , il n’existe qu’une seule orbite non réduite à un élément. Autrement dit s’il existe \( p \geq 2 \) et \( a \in \{ 1,\ldots , n\} \) tels que

> DEFINITION 14. Let \( \gamma \in {\mathcal{S}}_{n} \). We say that \( \gamma \) is a cycle if among the \( {\mathcal{O}}_{\gamma }\left( a\right) ,1 \leq a \leq n \), there is only one orbit not reduced to a single element. In other words, if there exist \( p \geq 2 \) and \( a \in \{ 1,\ldots , n\} \) such that

\[
{\mathcal{O}}_{\gamma }\left( a\right)  = \left\{  {a,\gamma \left( a\right) ,\ldots ,{\gamma }^{p - 1}\left( a\right) }\right\}  \;\text{ et }\;\forall x \notin  {\mathcal{O}}_{\gamma }\left( a\right) ,\gamma \left( x\right)  = x.
\]

L’orbite \( {\mathcal{O}}_{\gamma }\left( a\right) \) est appelé support du cycle, son cardinal la longueur du cycle, et on note \( \gamma = \left( {a,\gamma \left( a\right) ,\ldots ,{\gamma }^{p - 1}\left( a\right) }\right) . \)

> The orbit \( {\mathcal{O}}_{\gamma }\left( a\right) \) is called the support of the cycle, its cardinality the length of the cycle, and we denote it by \( \gamma = \left( {a,\gamma \left( a\right) ,\ldots ,{\gamma }^{p - 1}\left( a\right) }\right) . \)

Exemple 5. - Une transposition est un cycle de longueur 2.

> Example 5. - A transposition is a cycle of length 2.

- Dans \( {\mathcal{S}}_{5}, s = \left( {1,3,5}\right)  = \left( \begin{array}{lllll} 1 & 2 & 3 & 4 & 5 \\  3 & 2 & 5 & 4 & 1 \end{array}\right) \) est un cycle de support \( \{ 1,3,5\} \) et de longueur 3.

> - In \( {\mathcal{S}}_{5}, s = \left( {1,3,5}\right)  = \left( \begin{array}{lllll} 1 & 2 & 3 & 4 & 5 \\  3 & 2 & 5 & 4 & 1 \end{array}\right) \) is a cycle with support \( \{ 1,3,5\} \) and length 3.

- L’élément \( s = \left( \begin{array}{llll} 1 & 2 & 3 & 4 \\  2 & 1 & 4 & 3 \end{array}\right) \) de \( {\mathcal{S}}_{4} \) n’est pas un cycle (deux orbites, \( \{ 1,2\} \) et \( \{ 3,4\} \) ).

> - The element \( s = \left( \begin{array}{llll} 1 & 2 & 3 & 4 \\  2 & 1 & 4 & 3 \end{array}\right) \) of \( {\mathcal{S}}_{4} \) is not a cycle (two orbits, \( \{ 1,2\} \) and \( \{ 3,4\} \) ).

Remarque 8. - Des cycles à supports disjoints commutent.

> Remark 8. - Cycles with disjoint supports commute.

- L’ordre d’un cycle dans le groupe \( {\mathcal{S}}_{n} \) est sa longueur.

> - The order of a cycle in the group \( {\mathcal{S}}_{n} \) is its length.

\( \rightarrow \) THÉORÉME 6. Toute permutation \( s \neq \) Id se décompose de manière unique à l’ordre prés en un produit de cycles dont les supports sont deux à deux disjoints.

> \( \rightarrow \) THEOREM 6. Any permutation \( s \neq \) Id decomposes uniquely, up to order, into a product of cycles with pairwise disjoint supports.

Exemple 6. \( \; - \left( \begin{array}{llll} 1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3 \end{array}\right) = \left( {1,2}\right) \cdot \left( {3,4}\right) = \left( {3,4}\right) \cdot \left( {1,2}\right) \) .

> Example 6. \( \; - \left( \begin{array}{llll} 1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3 \end{array}\right) = \left( {1,2}\right) \cdot \left( {3,4}\right) = \left( {3,4}\right) \cdot \left( {1,2}\right) \) .

\( - \left( \begin{array}{lllllll} 1 & 2 & 3 & 4 & 5 & 6 & 7 \\ 2 & 6 & 5 & 1 & 3 & 4 & 7 \end{array}\right) = \left( {1,2,6,4}\right) \cdot \left( {3,5}\right) \cdot \left( 7\right) = \left( {3,5}\right) \cdot \left( {1,2,6,4}\right) \cdot \left( 7\right) = \left( {3,5}\right) \cdot \left( 7\right) \cdot \left( {1,2,6,4}\right) . \)

> Signature d'une permutation.

Signature of a permutation.

> DÉFINITION 15. Soit \( s \in {\mathcal{S}}_{n} \) . On appelle signature de \( s \) le produit

DEFINITION 15. Let \( s \in {\mathcal{S}}_{n} \) . The signature of \( s \) is defined as the product

\[
\varepsilon \left( s\right)  = \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\frac{s\left( j\right)  - s\left( i\right) }{j - i}.
\]

On a \( \varepsilon \left( s\right) \in \{ - 1,1\} \) . Si \( \varepsilon \left( s\right) = 1 \) (resp. \( \varepsilon \left( s\right) = - 1), s \) est dite paire (resp. impaire).

> We have \( \varepsilon \left( s\right) \in \{ - 1,1\} \) . If \( \varepsilon \left( s\right) = 1 \) (resp. \( \varepsilon \left( s\right) = - 1), s \) is said to be even (resp. odd).

Proposition 6. Si s et t sont deux éléments de \( {\mathcal{S}}_{n} \) alors \( \varepsilon \left( {st}\right) = \varepsilon \left( s\right) \varepsilon \left( t\right) \) .

> Proposition 6. If s and t are two elements of \( {\mathcal{S}}_{n} \) then \( \varepsilon \left( {st}\right) = \varepsilon \left( s\right) \varepsilon \left( t\right) \) .

Remarque 9. - Une transposition est de signature -1 .

> Remark 9. - A transposition has signature -1 .

- La proposition précédente exprime le fait que \( \varepsilon  : {\mathcal{S}}_{n} \rightarrow  \{  - 1,1\} \) est un morphisme de groupe. L’ensemble \( {\mathcal{A}}_{n} = {\varepsilon }^{-1}\left( {\{ 1\} }\right)  = \operatorname{Ker}\varepsilon \) est un sous-groupe distingué de \( {\mathcal{S}}_{n} \) , d’indice 2 : on a \( \operatorname{Card}\left( {\mathcal{A}}_{n}\right)  = n!/2 \) et \( {\mathcal{A}}_{n} \) s’appelle le groupe alterné d’indice \( n \) .

> - The previous proposition expresses the fact that \( \varepsilon  : {\mathcal{S}}_{n} \rightarrow  \{  - 1,1\} \) is a group homomorphism. The set \( {\mathcal{A}}_{n} = {\varepsilon }^{-1}\left( {\{ 1\} }\right)  = \operatorname{Ker}\varepsilon \) is a normal subgroup of \( {\mathcal{S}}_{n} \) , of index 2: we have \( \operatorname{Card}\left( {\mathcal{A}}_{n}\right)  = n!/2 \) and \( {\mathcal{A}}_{n} \) is called the alternating group of degree \( n \) .

PROPOSITION 7. La signature d’un cycle de longueur \( p \) est \( {\left( -1\right) }^{p - 1} \) .

> PROPOSITION 7. The signature of a cycle of length \( p \) is \( {\left( -1\right) }^{p - 1} \) .

Démonstration. Soit \( s = \left( {{a}_{1},{a}_{2},\cdots ,{a}_{p}}\right) \) un cycle de longueur \( p \) . Le cycle \( s \) peut se décomposer sous la forme \( s = \left( {{a}_{1},{a}_{p}}\right) \cdot \left( {{a}_{1},{a}_{p - 1}}\right) \cdots \left( {{a}_{1},{a}_{3}}\right) \cdot \left( {{a}_{1},{a}_{2}}\right) \) , c’est le produit de \( p - 1 \) transpositions. Une transposition étant de signature -1, on en déduit le résultat.

> Proof. Let \( s = \left( {{a}_{1},{a}_{2},\cdots ,{a}_{p}}\right) \) be a cycle of length \( p \) . The cycle \( s \) can be decomposed as \( s = \left( {{a}_{1},{a}_{p}}\right) \cdot \left( {{a}_{1},{a}_{p - 1}}\right) \cdots \left( {{a}_{1},{a}_{3}}\right) \cdot \left( {{a}_{1},{a}_{2}}\right) \) , which is the product of \( p - 1 \) transpositions. Since a transposition has signature -1, we deduce the result.
