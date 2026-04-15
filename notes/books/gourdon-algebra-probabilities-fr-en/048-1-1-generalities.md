#### 1.1. Generalities

*Français : 1.1. Généralités*

DÉFINITION 1. On appelle K-espace vectoriel (ou e.v sur K) un ensemble \( E \) muni d’une loi interne (notée +) et d’une loi externe (notée ·) admettant \( \mathbb{K} \) comme ensemble d’opérateurs et vérifiant :

> DEFINITION 1. A K-vector space (or v.s. over K) is a set \( E \) equipped with an internal law (denoted +) and an external law (denoted ·) admitting \( \mathbb{K} \) as a set of operators and satisfying:

(i) \( \left( {E, + }\right) \) est un groupe abélien.

> (i) \( \left( {E, + }\right) \) is an abelian group.

(ii) Pour tout \( \left( {x, y}\right) \in {E}^{2} \) et \( \left( {\lambda ,\mu }\right) \in {\mathbb{K}}^{2} \) ,

> (ii) For all \( \left( {x, y}\right) \in {E}^{2} \) and \( \left( {\lambda ,\mu }\right) \in {\mathbb{K}}^{2} \) ,

\[
\text{ a) }\lambda  \cdot  \left( {x + y}\right)  = \lambda  \cdot  x + \lambda  \cdot  y\text{ , }
\]

b) \( \left( {\lambda + \mu }\right) \cdot x = \lambda \cdot x + \mu \cdot x \) ,

\[
\text{ c) }\lambda  \cdot  \left( {\mu  \cdot  x}\right)  = \left( {\lambda \mu }\right)  \cdot  x\text{ , }
\]

d) \( 1 \cdot x = x \) .

> Remarque 1. - Cette définition entraîne : \( \left( {\lambda \cdot x = 0}\right) \Leftrightarrow \left( {\lambda = 0\text{ ou }x = 0}\right) \) .

Remark 1. - This definition implies: \( \left( {\lambda \cdot x = 0}\right) \Leftrightarrow \left( {\lambda = 0\text{ ou }x = 0}\right) \) .

> - On dit que \( E \) est une \( \mathbb{K} \) -algèbre s’il existe de plus une loi interne, notée \( \circ \) , vérifiant

- We say that \( E \) is a \( \mathbb{K} \) -algebra if there exists in addition an internal law, denoted \( \circ \) , satisfying

> (i) \( \left( {E,+, \circ }\right) \) est un anneau,

(i) \( \left( {E,+, \circ }\right) \) is a ring,

> (ii) \( \forall \left( {x, y}\right) \in {E}^{2},\forall \lambda \in \mathbb{K},\lambda \cdot \left( {x \circ y}\right) = \left( {\lambda \cdot x}\right) \circ y = x \circ \left( {\lambda \cdot y}\right) \) .

(ii) \( \forall \left( {x, y}\right) \in {E}^{2},\forall \lambda \in \mathbb{K},\lambda \cdot \left( {x \circ y}\right) = \left( {\lambda \cdot x}\right) \circ y = x \circ \left( {\lambda \cdot y}\right) \) .

> Exemple 1. Les ensembles suivant sont des \( \mathbb{K} \) -espaces vectoriels : \( \mathbb{K},{\mathbb{K}}^{n} \) (muni des lois \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) + \left( {{y}_{1},\ldots ,{y}_{n}}\right) = \left( {{x}_{1} + {y}_{1},\ldots ,{x}_{n} + {y}_{n}}\right) \) et \( \lambda \cdot \left( {{x}_{1},\ldots ,{x}_{n}}\right) = \left( {\lambda {x}_{1},\ldots ,\lambda {x}_{n}}\right) ), \) toute extension de corps \( \mathbb{L} \) de \( \mathbb{K} \) , l’ensemble des fonctions d’un ensemble \( \Omega \) dans \( \mathbb{K},\mathbb{K}\left\lbrack X\right\rbrack \) , \( \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack . \)

Example 1. The following sets are \( \mathbb{K} \) -vector spaces: \( \mathbb{K},{\mathbb{K}}^{n} \) (equipped with the laws \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) + \left( {{y}_{1},\ldots ,{y}_{n}}\right) = \left( {{x}_{1} + {y}_{1},\ldots ,{x}_{n} + {y}_{n}}\right) \) and \( \lambda \cdot \left( {{x}_{1},\ldots ,{x}_{n}}\right) = \left( {\lambda {x}_{1},\ldots ,\lambda {x}_{n}}\right) ), \) any field extension \( \mathbb{L} \) of \( \mathbb{K} \) , the set of functions from a set \( \Omega \) to \( \mathbb{K},\mathbb{K}\left\lbrack X\right\rbrack \) , \( \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack . \)

> DéFINITION 2. Les éléments d’un \( \mathbb{K} \) -e.v s’appellent des vecteurs, ceux de \( \mathbb{K} \) des scalaires.

DEFINITION 2. The elements of a \( \mathbb{K} \) -v.s. are called vectors, those of \( \mathbb{K} \) are called scalars.

> DéFINITION 3. Soit \( \left( {E,+, \cdot }\right) \) un \( \mathbb{K} \) -e.v et \( F \subset E \) . On dit que \( F \) est un sous-espace vectoriel de \( E \) si \( \left( {F,+, \cdot }\right) \) est un \( \mathbb{K} \) -e.v.

DEFINITION 3. Let \( \left( {E,+, \cdot }\right) \) be a \( \mathbb{K} \) -v.s. and \( F \subset E \) . We say that \( F \) is a vector subspace of \( E \) if \( \left( {F,+, \cdot }\right) \) is a \( \mathbb{K} \) -v.s.

> Exemple 2. Les ensembles \( \{ 0\} \) et \( E \) sont des s.e.v de \( E;{\mathbb{K}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \leq n\} \) est un s.e.v de \( \mathbb{K}\left\lbrack X\right\rbrack ;\mathcal{C}\left( {\mathbb{R},\mathbb{R}}\right) \) (ensemble des fonctions continues de \( \mathbb{R} \) dans \( \mathbb{R} \) ) est un s.e.v du \( \mathbb{R} \) -e.v des fonctions de \( \mathbb{R} \) dans \( \mathbb{R} \) ; si \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , l’idéal \( \left( P\right) \) est un s.e.v de \( \mathbb{K}\left\lbrack X\right\rbrack \) .

Example 2. The sets \( \{ 0\} \) and \( E \) are subspaces of \( E;{\mathbb{K}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \leq n\} \) is a subspace of \( \mathbb{K}\left\lbrack X\right\rbrack ;\mathcal{C}\left( {\mathbb{R},\mathbb{R}}\right) \) (set of continuous functions from \( \mathbb{R} \) to \( \mathbb{R} \)) is a subspace of the \( \mathbb{R} \)-vector space of functions from \( \mathbb{R} \) to \( \mathbb{R} \); if \( P \in \mathbb{K}\left\lbrack X\right\rbrack \), the ideal \( \left( P\right) \) is a subspace of \( \mathbb{K}\left\lbrack X\right\rbrack \).

> Proposition 1. Soit \( \left( {E,+, \cdot }\right) \) un \( \mathbb{K} \) -e.v et \( F \subset E \) . Alors \( \left( {F,+, \cdot }\right) \) est un s.e.v de \( E \) si et seulement si

Proposition 1. Let \( \left( {E,+, \cdot }\right) \) be a \( \mathbb{K} \)-vector space and \( F \subset E \). Then \( \left( {F,+, \cdot }\right) \) is a subspace of \( E \) if and only if

\[
\text{ (i) }F \neq  \varnothing \;\left( {ii}\right) \;\forall \left( {x, y}\right)  \in  {F}^{2},\forall \left( {\lambda ,\mu }\right)  \in  {\mathbb{K}}^{2},{\lambda x} + {\mu y} \in  F\text{ . }
\]

Remarque 2. On montre rarement directement qu'un ensemble est un e.v, mais souvent que c'est un s.e.v d'un e.v connu (à l'aide de la proposition précédente).

> Remark 2. One rarely shows directly that a set is a vector space, but often that it is a subspace of a known vector space (using the previous proposition).

Proposition 2. Soit \( E \) un \( \mathbb{K} \) -e.v et \( {\left( {E}_{i}\right) }_{i \in I} \) une famille de s.e.v de \( E \) . Alors \( { \cap }_{i \in I}{E}_{i} \) est un s.e.v de \( E \) .

> Proposition 2. Let \( E \) be a \( \mathbb{K} \)-vector space and \( {\left( {E}_{i}\right) }_{i \in I} \) a family of subspaces of \( E \). Then \( { \cap }_{i \in I}{E}_{i} \) is a subspace of \( E \).

Remarque 3. Attention, ce théorème est faux pour la réunion (voir l'exercice 1).

> Remark 3. Warning, this theorem is false for the union (see exercise 1).

Somme de sous-espaces vectoriels.

> Sum of vector subspaces.

DéFINITION 4. Soit \( E \) un \( \mathbb{K} \) -e.v, \( {\left( {E}_{i}\right) }_{i \in I} \) une famille de s.e.v de \( E \) . On note \( \mathop{\sum }\limits_{{i \in I}}{E}_{i} = \) \{ \( \mathop{\sum }\limits_{{i \in I}}{x}_{i} \mid \) les \( {x}_{i} \in {E}_{i} \) étant tous nuls sauf un nombre fini\}. L’ensemble \( \mathop{\sum }\limits_{{i \in I}}{E}_{i} \) est un s.e.v de \( E \) appelé somme des s.e.v \( {\left( {E}_{i}\right) }_{i \in I} \) .

> DEFINITION 4. Let \( E \) be a \( \mathbb{K} \)-vector space, \( {\left( {E}_{i}\right) }_{i \in I} \) a family of subspaces of \( E \). We denote \( \mathop{\sum }\limits_{{i \in I}}{E}_{i} = \) \{ \( \mathop{\sum }\limits_{{i \in I}}{x}_{i} \mid \) the \( {x}_{i} \in {E}_{i} \) being all zero except for a finite number\}. The set \( \mathop{\sum }\limits_{{i \in I}}{E}_{i} \) is a subspace of \( E \) called the sum of the subspaces \( {\left( {E}_{i}\right) }_{i \in I} \).

DéFINITION 5. Soient \( {E}_{1},\ldots ,{E}_{n}n \) sous-espaces vectoriels d’un \( \mathbb{K} \) -e.v \( E \) . On dit que \( E \) est somme directe de \( {E}_{1},\ldots ,{E}_{n} \) si tout vecteur \( x \in E \) s’écrit de manière unique sous la forme \( x = {x}_{1} + \cdots + {x}_{n} \) où \( \forall i,{x}_{i} \in {E}_{i} \) . On note alors \( E = {E}_{1} \oplus \cdots \oplus {E}_{n} = { \oplus }_{i = 1}^{n}{E}_{i} \) .

> DEFINITION 5. Let \( {E}_{1},\ldots ,{E}_{n}n \) be subspaces of a \( \mathbb{K} \)-vector space \( E \). We say that \( E \) is the direct sum of \( {E}_{1},\ldots ,{E}_{n} \) if every vector \( x \in E \) can be written uniquely in the form \( x = {x}_{1} + \cdots + {x}_{n} \) where \( \forall i,{x}_{i} \in {E}_{i} \). We then denote it \( E = {E}_{1} \oplus \cdots \oplus {E}_{n} = { \oplus }_{i = 1}^{n}{E}_{i} \).

Remarque 4. Si \( E = {E}_{1} \oplus \cdots \oplus {E}_{n} \) , on a bien sûr \( E = \mathop{\sum }\limits_{{i = 1}}^{n}{E}_{i} = {E}_{1} + \cdots + {E}_{n} \) .

> Remark 4. If \( E = {E}_{1} \oplus \cdots \oplus {E}_{n} \), we naturally have \( E = \mathop{\sum }\limits_{{i = 1}}^{n}{E}_{i} = {E}_{1} + \cdots + {E}_{n} \).

Proposition 3. Soient \( {E}_{1} \) et \( {E}_{2} \) deux s.e.v d’un \( \mathbb{K} \) -e.v E. Alors \( E = {E}_{1} \oplus {E}_{2} \) si et seulement si \( E = {E}_{1} + {E}_{2} \) et \( {E}_{1} \cap {E}_{2} = \{ 0\} \) .

> Proposition 3. Let \( {E}_{1} \) and \( {E}_{2} \) be two subspaces of a \( \mathbb{K} \)-vector space E. Then \( E = {E}_{1} \oplus {E}_{2} \) if and only if \( E = {E}_{1} + {E}_{2} \) and \( {E}_{1} \cap {E}_{2} = \{ 0\} \).

Remarque 5. - Cette proposition est fausse s'il y a plus de deux s.e.v.

> Remark 5. - This proposition is false if there are more than two subspaces.

- On dit que \( n \) s.e.v \( {E}_{1},\ldots ,{E}_{n} \) sont en somme directe si \( \mathop{\sum }\limits_{{i = 1}}^{n}{E}_{i} = { \oplus  }_{i = 1}^{n}{E}_{i} \) . On a le résultat pratique suivant : Les \( {\left( {E}_{i}\right) }_{1 \leq  i \leq  n} \) sont en somme directe si et seulement si l’égalité \( {x}_{1} + \cdots  + {x}_{n} = 0 \) avec \( \forall i,{x}_{i} \in  {E}_{i} \) , entraîne \( \forall i,{x}_{i} = 0 \) .

> - We say that \( n \) subspaces \( {E}_{1},\ldots ,{E}_{n} \) are in direct sum if \( \mathop{\sum }\limits_{{i = 1}}^{n}{E}_{i} = { \oplus  }_{i = 1}^{n}{E}_{i} \) . We have the following practical result: The \( {\left( {E}_{i}\right) }_{1 \leq  i \leq  n} \) are in direct sum if and only if the equality \( {x}_{1} + \cdots  + {x}_{n} = 0 \) with \( \forall i,{x}_{i} \in  {E}_{i} \) implies \( \forall i,{x}_{i} = 0 \) .

Familles génératrices, familles libres.

> Generating families, linearly independent families.

DÉFINITION 6. Soit \( {\left( {x}_{i}\right) }_{i \in I} \) une famille de vecteurs d’un \( \mathbb{K} \) -e.v \( E \) . On appelle combinaison linéaire des \( {\left( {x}_{i}\right) }_{i \in I} \) toute somme \( \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} \) où pour tout \( i,{\lambda }_{i} \in \mathbb{K} \) et où les \( {\lambda }_{i} \) sont tous nuls sauf un nombre fini.

> DEFINITION 6. Let \( {\left( {x}_{i}\right) }_{i \in I} \) be a family of vectors of a \( \mathbb{K} \) -v.s. \( E \) . A linear combination of \( {\left( {x}_{i}\right) }_{i \in I} \) is any sum \( \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} \) where for all \( i,{\lambda }_{i} \in \mathbb{K} \) and where the \( {\lambda }_{i} \) are all zero except for a finite number.

- L’ensemble \( F \) des combinaisons linéaires des \( {\left( {x}_{i}\right) }_{i \in  I} \) est un s.e.v de \( E \) noté Vect \( {\left( {x}_{i}\right) }_{i \in  I} \) . C’est le plus petit s.e.v de \( E \) contenant tous les \( {x}_{i} \) .

> - The set \( F \) of linear combinations of \( {\left( {x}_{i}\right) }_{i \in  I} \) is a subspace of \( E \) denoted Vect \( {\left( {x}_{i}\right) }_{i \in  I} \) . It is the smallest subspace of \( E \) containing all the \( {x}_{i} \) .

DéFINITION 7. Soit \( E \) un \( \mathbb{K} \) -e.v et \( A \subset E \) . On note Vect \( A = \operatorname{Vect}{\left( a\right) }_{a \in A} \) . On dit que \( A \) est une partie génératrice de \( E \) (ou \( {\left( a\right) }_{a \in A} \) une famille génératrice de \( E \) ) si Vect \( A = E \) .

> DEFINITION 7. Let \( E \) be a \( \mathbb{K} \) -v.s. and \( A \subset E \) . We denote Vect \( A = \operatorname{Vect}{\left( a\right) }_{a \in A} \) . We say that \( A \) is a generating set of \( E \) (or \( {\left( a\right) }_{a \in A} \) a generating family of \( E \) ) if Vect \( A = E \) .

DéFINITION 8. Soit \( {\left( {x}_{i}\right) }_{i \in I} \) une famille d’un \( \mathbb{K} \) -e.v \( E \) . Alors (i) et (ii) sont équivalents :

> DEFINITION 8. Let \( {\left( {x}_{i}\right) }_{i \in I} \) be a family of a \( \mathbb{K} \) -v.s. \( E \) . Then (i) and (ii) are equivalent:

(i) Toute combinaison linéaire vérifiant \( \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} = 0 \) vérifie \( \forall i,{\lambda }_{i} = 0 \) .

> (i) Any linear combination satisfying \( \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} = 0 \) satisfies \( \forall i,{\lambda }_{i} = 0 \) .

(ii) Aucun vecteur de la famille n'est combinaison linéaire des autres.

> (ii) No vector in the family is a linear combination of the others.

Une famille de vecteurs vérifiant (i) ou (ii) est dite libre (on dit aussi que les vecteurs \( {\left( {x}_{i}\right) }_{i \in I} \) sont linéairement indépendants). Dans le cas contraire, la famille est dite liée.

> A family of vectors satisfying (i) or (ii) is called linearly independent (we also say that the vectors \( {\left( {x}_{i}\right) }_{i \in I} \) are linearly independent). Otherwise, the family is called linearly dependent.

Citons enfin le théorème qui est à la base de la théorie sur la dimension des espaces vectoriels.

> Finally, let us cite the theorem that forms the basis of the theory of the dimension of vector spaces.

THÉORÉME 1. Dans un e.v E engendré par un nombre fini n de vecteurs (c'est-à-dire \( \exists \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {E}^{n}, E = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) ), toute famille libre a au plus \( n \) éléments.

> THEOREM 1. In a v.s. E generated by a finite number n of vectors (i.e., \( \exists \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {E}^{n}, E = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) ), any linearly independent family has at most \( n \) elements.
