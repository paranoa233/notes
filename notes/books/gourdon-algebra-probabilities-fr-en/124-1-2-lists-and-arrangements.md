#### 1.2. Lists and arrangements

*Français : 1.2. Listes et arrangements*

Proposition 6. Soient \( n \) ensembles finis \( {E}_{1},\ldots ,{E}_{n} \) . Le produit cartésien \( {E}_{1} \times \ldots \times {E}_{n} \) est un ensemble fini et vérifie \( \left| {{E}_{1} \times \ldots \times {E}_{n}}\right| = \left| {E}_{1}\right| \times \ldots \times \left| {E}_{n}\right| \) . En particulier, pour un ensemble fini \( E \) on a \( \left| {E}^{n}\right| = {\left| E\right| }^{n} \) .

> Proposition 6. Let \( n \) be finite sets \( {E}_{1},\ldots ,{E}_{n} \) . The Cartesian product \( {E}_{1} \times \ldots \times {E}_{n} \) is a finite set and satisfies \( \left| {{E}_{1} \times \ldots \times {E}_{n}}\right| = \left| {E}_{1}\right| \times \ldots \times \left| {E}_{n}\right| \) . In particular, for a finite set \( E \) we have \( \left| {E}^{n}\right| = {\left| E\right| }^{n} \) .

DéFINITION 2. Soit \( E \) un ensemble et \( p \in {\mathbb{N}}^{ * } \) . On appelle \( p \) -liste (ou \( p \) -uplet) de \( E \) tout élément \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) de \( {E}^{p} \) .

> DEFINITION 2. Let \( E \) be a set and \( p \in {\mathbb{N}}^{ * } \) . A \( p \) -list (or \( p \) -tuple) of \( E \) is any element \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) of \( {E}^{p} \) .

Remarque 5. - La proposition précédente indique que lorsque \( E \) est un ensemble fini, il y a \( {\left| E\right| }^{p} \) p-listes de \( E \) .

> Remark 5. - The previous proposition indicates that when \( E \) is a finite set, there are \( {\left| E\right| }^{p} \) p-lists of \( E \) .

- Dans une liste, l'ordre des éléments importe (ce n'est pas un ensemble), et un même élément peut figurer plusieurs fois dans la liste. Ainsi les listes modélisent les tirages successifs avec remise. Par exemple, dans un jeu de 52 cartes, le nombre de façons de tirer 10 cartes avec remise est \( {52}^{10} \) .

> - In a list, the order of elements matters (it is not a set), and the same element can appear multiple times in the list. Thus, lists model successive draws with replacement. For example, in a 52-card deck, the number of ways to draw 10 cards with replacement is \( {52}^{10} \) .

PROPOSITION 7. Soit \( E \) un ensemble. On pose \( n = \left| E\right| \) . Soit \( p \in {\mathbb{N}}^{ * }, p \leq n \) . On appelle \( p \) -arrangement de E toute p-liste de E d’éléments distincts. Le nombre de p-arrangements de \( E \) est \( {A}_{n}^{p} = n\left( {n - 1}\right) \cdots \left( {n - p + 1}\right) = n!/\left( {n - p}\right) \) !. En particulier si \( p = n \) le nombre de \( n \) -arrangements de \( E \) est \( n \) !.

> PROPOSITION 7. Let \( E \) be a set. Let \( n = \left| E\right| \) . Let \( p \in {\mathbb{N}}^{ * }, p \leq n \) . A \( p \) -arrangement of E is any p-list of E with distinct elements. The number of p-arrangements of \( E \) is \( {A}_{n}^{p} = n\left( {n - 1}\right) \cdots \left( {n - p + 1}\right) = n!/\left( {n - p}\right) \) !. In particular, if \( p = n \) the number of \( n \) -arrangements of \( E \) is \( n \) !.

Remarque 6. - Construire un \( p \) -arrangement de \( E \) , c’est donc choisir un premier élément de \( E \) ( \( n \) possibilités), puis un deuxième élément distinct du premier ( \( n - 1 \) possibilités), etc, jusqu’à un \( p \) -ième élément distinct des \( p - 1 \) précédents ( \( n - p + 1 \) possibilités). Le nombre total est donc bien \( n\left( {n - 1}\right) \cdots \left( {n - p + 1}\right) \) .

> Remark 6. - Constructing a \( p \) -arrangement of \( E \) means choosing a first element from \( E \) ( \( n \) possibilities), then a second element distinct from the first ( \( n - 1 \) possibilities), and so on, up to a \( p \) -th element distinct from the \( p - 1 \) previous ones ( \( n - p + 1 \) possibilities). The total number is therefore indeed \( n\left( {n - 1}\right) \cdots \left( {n - p + 1}\right) \) .

- Dans les arrangements, l'ordre des éléments importe mais ceux ci sont distincts. Ainsi les arrangements modélisent les tirages successifs sans remise. Par exemple, dans un jeu de 52 cartes, le nombre de façons de tirer 10 cartes sans remise est \( {A}_{52}^{10} = {52} \times  {51} \times  \ldots  \times  {43}. \)

> - In arrangements, the order of elements matters but they are distinct. Thus, arrangements model successive draws without replacement. For example, in a 52-card deck, the number of ways to draw 10 cards without replacement is \( {A}_{52}^{10} = {52} \times  {51} \times  \ldots  \times  {43}. \)

Proposition 8 (NOMBRE D'APPLICATIONS ENTRE DEUX ENSEMBLES). Soient \( E \) et \( F \) deux ensembles finis.

> Proposition 8 (NUMBER OF MAPPINGS BETWEEN TWO SETS). Let \( E \) and \( F \) be two finite sets.

(i) L’ensemble des applications de \( E \) vers \( F \) , noté \( {F}^{E} \) , est fini, et on a \( \left| {F}^{E}\right| = {\left| F\right| }^{\left| E\right| } \) .

> (i) The set of mappings from \( E \) to \( F \) , denoted by \( {F}^{E} \) , is finite, and we have \( \left| {F}^{E}\right| = {\left| F\right| }^{\left| E\right| } \) .

(ii) En notant \( p = \left| E\right| \) et \( n = \left| F\right| \) , et lorsque \( p \leq n, l \) ’ensemble des applications injectives de \( E \) dans \( F \) est fini et de cardinal \( {A}_{n}^{p} = n!/\left( {n - p}\right) ! \) .

> (ii) By denoting \( p = \left| E\right| \) and \( n = \left| F\right| \) , and when \( p \leq n, l \) the set of injective mappings from \( E \) to \( F \) is finite and of cardinality \( {A}_{n}^{p} = n!/\left( {n - p}\right) ! \) .

(iii) En notant \( n = \left| E\right| \) , l’ensemble des bijections de \( E \) vers \( E \) , appelées permutations de \( E \) et noté \( {\mathcal{S}}_{E} \) , est fini et de cardinal \( n \) !.

> (iii) By denoting \( n = \left| E\right| \) , the set of bijections from \( E \) to \( E \) , called permutations of \( E \) and denoted \( {\mathcal{S}}_{E} \) , is finite and of cardinality \( n \) !.

Démonstration. Montrons d’abord (i) et (ii). Soit \( p = \left| E\right| \) et notons \( {x}_{1},\ldots ,{x}_{p} \) les élements de \( E \) . A tout \( p \) -uplet \( Y = \left( {{y}_{1},\ldots ,{y}_{p}}\right) \) de \( F \) on associe la fonction \( {\varphi }_{Y} : E \rightarrow F \) définie par \( {\varphi }_{Y}\left( {x}_{k}\right) = {y}_{k} \) , pour \( 1 \leq k \leq p \) . L’application \( Y \mapsto {\varphi }_{Y} \) est une bijection de \( {F}^{p} \) vers \( {F}^{E} \) , donc \( \left| {F}^{E}\right| = \left| {F}^{p}\right| = {\left| F\right| }^{p} = {\left| F\right| }^{\left| E\right| } \) d’après la proposition 6. On en déduit (i)

> Proof. Let us first show (i) and (ii). Let \( p = \left| E\right| \) and let \( {x}_{1},\ldots ,{x}_{p} \) denote the elements of \( E \) . To any \( p \) -tuple \( Y = \left( {{y}_{1},\ldots ,{y}_{p}}\right) \) of \( F \) we associate the function \( {\varphi }_{Y} : E \rightarrow F \) defined by \( {\varphi }_{Y}\left( {x}_{k}\right) = {y}_{k} \) , for \( 1 \leq k \leq p \) . The mapping \( Y \mapsto {\varphi }_{Y} \) is a bijection from \( {F}^{p} \) to \( {F}^{E} \) , so \( \left| {F}^{E}\right| = \left| {F}^{p}\right| = {\left| F\right| }^{p} = {\left| F\right| }^{\left| E\right| } \) according to proposition 6. We deduce (i) from this.

Restreinte aux \( p \) -arrangements,’application \( Y \mapsto {\varphi }_{Y} \) est une bijection de l’ensemble des \( p \) -arrangements de \( F \) vers l’ensemble des applications injectives de \( {F}^{E} \) . On en déduit (ii).

> Restricted to \( p \) -arrangements, the mapping \( Y \mapsto {\varphi }_{Y} \) is a bijection from the set of \( p \) -arrangements of \( F \) to the set of injective mappings of \( {F}^{E} \) . We deduce (ii) from this.

Pour (iii) on observe que \( E \) étant ensemble fini, les bijections de \( E \) sur \( E \) sont les injections de \( E \) sur \( E \) , et on conclut avec (ii).

> For (iii) we observe that since \( E \) is a finite set, the bijections from \( E \) to \( E \) are the injections from \( E \) to \( E \) , and we conclude with (ii).

Remarque 7. - Muni de la loi de composition, l’ensemble \( {\mathcal{S}}_{E} \) des permutations de \( E \) est un groupe, appelé groupe symétrique de \( E \) . Lorsque \( E = \{ 1,\ldots , n\} \) , on retrouve le groupe symétrique d’indice \( n \) (voir la définition 11 page 22), noté \( {\mathcal{S}}_{n} \) . On le retrouve parfois lorsqu'on souhaite compter le nombre de permutations de \( \{ 1,\ldots , n\} \) ayant certaines propriétés (voir par exemple l’exercice 8 page 312).

> Remark 7. - Equipped with the composition law, the set \( {\mathcal{S}}_{E} \) of permutations of \( E \) is a group, called the symmetric group of \( E \) . When \( E = \{ 1,\ldots , n\} \) , we recover the symmetric group of index \( n \) (see definition 11 page 22), denoted \( {\mathcal{S}}_{n} \) . It is sometimes encountered when one wishes to count the number of permutations of \( \{ 1,\ldots , n\} \) having certain properties (see for example exercise 8 page 312).

- Compter le nombre de surjections est plus difficile ; on le retrouve dans le cadre de l'étude des nombres de Stirling de seconde espèce (voir le problème 7 page 379).

> - Counting the number of surjections is more difficult; it is encountered in the context of the study of Stirling numbers of the second kind (see problem 7 page 379).

PROPOSITION 9. Soit \( E \) est un ensemble fini. Alors l’ensemble \( \mathcal{P}\left( E\right) \) des parties de \( E \) est fini et \( \left| {\mathcal{P}\left( E\right) }\right| = {2}^{\left| E\right| } \) .

> PROPOSITION 9. Let \( E \) be a finite set. Then the set \( \mathcal{P}\left( E\right) \) of subsets of \( E \) is finite and \( \left| {\mathcal{P}\left( E\right) }\right| = {2}^{\left| E\right| } \) .

Démonstration. À chaque partie \( F \) de \( E \) on associe la fonction \( {\mathbf{1}}_{F} : E \rightarrow \{ 0,1\} \) indicatrice de \( F \) , définie par \( {\mathbf{1}}_{F}\left( x\right) = 1 \) si \( x \in F \) , \( = 0 \) sinon. L’application \( F \mapsto {\mathbf{1}}_{F} \) est une bijection de \( \mathcal{P}\left( E\right) \) sur \( \{ 0,1{\} }^{\left| E\right| } \) , donc on a \( \left| {\mathcal{P}\left( E\right) }\right| = {2}^{\left| E\right| } \) .

> Proof. To each subset \( F \) of \( E \) we associate the indicator function \( {\mathbf{1}}_{F} : E \rightarrow \{ 0,1\} \) of \( F \), defined by \( {\mathbf{1}}_{F}\left( x\right) = 1 \) if \( x \in F \), \( = 0 \) otherwise. The mapping \( F \mapsto {\mathbf{1}}_{F} \) is a bijection from \( \mathcal{P}\left( E\right) \) to \( \{ 0,1{\} }^{\left| E\right| } \), therefore we have \( \left| {\mathcal{P}\left( E\right) }\right| = {2}^{\left| E\right| } \).
