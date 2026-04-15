#### 3.4. Gram matrices

*Français : 3.4. Matrices de Gram*

DéFINITION 2. Soit \( E \) un espace préhilbertien (réel ou complexe) et \( {x}_{1},\cdots {x}_{n}n \) vecteurs de \( E \) . On appelle matrice de Gram de \( {x}_{1},\ldots ,{x}_{n} \) la matrice \( {\left\lbrack \left( {x}_{i} \cdot {x}_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) et déterminant de Gram le déterminant de cette matrice, noté \( G\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) .

> DEFINITION 2. Let \( E \) be a pre-Hilbert space (real or complex) and \( {x}_{1},\cdots {x}_{n}n \) vectors of \( E \) . The Gram matrix of \( {x}_{1},\ldots ,{x}_{n} \) is the matrix \( {\left\lbrack \left( {x}_{i} \cdot {x}_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) and the Gram determinant is the determinant of this matrix, denoted \( G\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) .

Proposition 3. Toute matrice de Gram est hermitienne positive. Réciproquement, toute matrice hermitienne positive est une matrice de Gram.

> Proposition 3. Every Gram matrix is positive Hermitian. Conversely, every positive Hermitian matrix is a Gram matrix.

De plus, la matrice de Gram de \( n \) vecteurs \( {x}_{1},\ldots ,{x}_{n} \) est définie si et seulement si la famille \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) est libre.

> Furthermore, the Gram matrix of \( n \) vectors \( {x}_{1},\ldots ,{x}_{n} \) is defined if and only if the family \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) is linearly independent.

Démonstration. Soient \( {x}_{1},\ldots ,{x}_{n} \) des vecteurs d’un espace préhilbertien \( E \) et \( M \) leur matrice de Gram. Soit \( F = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) et \( m = \dim F \) . Fixons nous une base orthonormée \( \mathcal{B} \) de \( F \) , et pour tout \( i \) notons \( {X}_{i} \) le vecteur colonne des coordonnées de \( {x}_{i} \) dans \( \mathcal{B} \) . On a \( {x}_{i} \cdot {x}_{j} = {X}_{i}^{ * }{X}_{j} \) , de sorte que \( M = {N}^{ * }N \) où \( N \) désigne la matrice \( m \times n \) dont les colonnes sont les \( {X}_{i} \) . Ceci montre que la matrice carrée \( M \) de taille \( n \) est hermitienne \( \left( {{M}^{ * } = {N}^{ * }{N}^{* * } = {N}^{ * }N = M}\right) \) et positive (car pour tout vecteur colonne \( X,{X}^{ * }{MX} = \left( {{X}^{ * }{N}^{ * }}\right) \left( {NX}\right) = {\left( NX\right) }^{ * }\left( {NX}\right) = \parallel {NX}{\parallel }^{2},\parallel \cdot \parallel \) désignant la norme euclidienne (resp. hermitienne) standard).

> Proof. Let \( {x}_{1},\ldots ,{x}_{n} \) be vectors in a pre-Hilbert space \( E \) and \( M \) be their Gram matrix. Let \( F = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) and \( m = \dim F \) . Fix an orthonormal basis \( \mathcal{B} \) of \( F \) , and for every \( i \) denote by \( {X}_{i} \) the column vector of the coordinates of \( {x}_{i} \) in \( \mathcal{B} \) . We have \( {x}_{i} \cdot {x}_{j} = {X}_{i}^{ * }{X}_{j} \) , so that \( M = {N}^{ * }N \) where \( N \) denotes the matrix \( m \times n \) whose columns are the \( {X}_{i} \) . This shows that the square matrix \( M \) of size \( n \) is Hermitian \( \left( {{M}^{ * } = {N}^{ * }{N}^{* * } = {N}^{ * }N = M}\right) \) and positive (because for any column vector \( X,{X}^{ * }{MX} = \left( {{X}^{ * }{N}^{ * }}\right) \left( {NX}\right) = {\left( NX\right) }^{ * }\left( {NX}\right) = \parallel {NX}{\parallel }^{2},\parallel \cdot \parallel \) denoting the standard Euclidean (resp. Hermitian) norm).

Réciproquement, si \( M = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) est une matrice hermitienne positive, d’après l’exer-cice 1 page 257, il existe une matrice \( n \times n \) hermitienne \( H \) telle que \( M = {H}^{2} = {H}^{ * }H \) . Si on désigne les vecteurs colonne de \( H \) par \( {X}_{1},\ldots ,{X}_{n} \) , on voit facilement que la relation \( M = {H}^{ * }H \) entraîne \( {a}_{i, j} = {X}_{i}^{ * }{X}_{j} = {X}_{i} \cdot {X}_{j} \) . La matrice \( M \) est bien une matrice de Gram.

> Conversely, if \( M = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) is a positive Hermitian matrix, according to exercise 1 on page 257, there exists a Hermitian matrix \( n \times n \) \( H \) such that \( M = {H}^{2} = {H}^{ * }H \) . If we denote the column vectors of \( H \) by \( {X}_{1},\ldots ,{X}_{n} \) , we easily see that the relation \( M = {H}^{ * }H \) implies \( {a}_{i, j} = {X}_{i}^{ * }{X}_{j} = {X}_{i} \cdot {X}_{j} \) . The matrix \( M \) is indeed a Gram matrix.

Cas défini. Une matrice de Gram \( M \) est définie si et seulement si \( \left( {{X}^{ * }{MX} = 0 \Rightarrow X = 0}\right) \) . En réutilisant les notations précédentes, on a \( {X}^{ * }{MX} = \parallel {NX}{\parallel }^{2} \) . Donc \( M \) est définie si et seulement si ( \( \parallel {NX}{\parallel }^{2} = 0 \Rightarrow X = 0 \) ). Ceci équivaut à dire que Ker \( N = \{ 0\} \) , ou encore que les vecteurs \( {x}_{i} \) forment une famille libre.

> Definite case. A Gram matrix \( M \) is definite if and only if \( \left( {{X}^{ * }{MX} = 0 \Rightarrow X = 0}\right) \) . Reusing the previous notations, we have \( {X}^{ * }{MX} = \parallel {NX}{\parallel }^{2} \) . Thus \( M \) is definite if and only if ( \( \parallel {NX}{\parallel }^{2} = 0 \Rightarrow X = 0 \) ). This is equivalent to saying that Ker \( N = \{ 0\} \) , or that the vectors \( {x}_{i} \) form a linearly independent family.

Les déterminants de Gram permettent de calculer la distance d'un point à un s.e.v, avec le théorème suivant.

> Gram determinants allow for the calculation of the distance from a point to a subspace, with the following theorem.

\( \rightarrow \) THÉORÉME 8. Soit E un espace préhilbertien, \( V \) un sous-espace de \( E \) muni d’une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) (pas forcément orthonormale). Soit \( x \in E \) . Alors la distance \( d \) de \( x \) à \( V \; \left( {d = \mathop{\inf }\limits_{{y \in V}}\parallel x - y\parallel }\right) \) vérifie

> \( \rightarrow \) THEOREM 8. Let E be a pre-Hilbert space, \( V \) a subspace of \( E \) equipped with a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) (not necessarily orthonormal). Let \( x \in E \) . Then the distance \( d \) from \( x \) to \( V \; \left( {d = \mathop{\inf }\limits_{{y \in V}}\parallel x - y\parallel }\right) \) satisfies

\[
{d}^{2} = \frac{G\left( {{e}_{1},\ldots ,{e}_{n}, x}\right) }{G\left( {{e}_{1},\ldots ,{e}_{n}}\right) }.
\]

Démonstration. D’après la proposition 2 de la partie 2.2 (page 254), on a \( d = \parallel z\parallel \) où \( z = x - y \) , \( y \) étant la projection orthogonale de \( x \) sur \( V \) . On a alors

> Proof. According to proposition 2 of part 2.2 (page 254), we have \( d = \parallel z\parallel \) where \( z = x - y \) , \( y \) being the orthogonal projection of \( x \) onto \( V \) . We then have

\[
\forall i,\;{e}_{i} \cdot  y = {e}_{i} \cdot  x\;\text{ et }\;\parallel x{\parallel }^{2} = \parallel y{\parallel }^{2} + \parallel z{\parallel }^{2},
\]

ce qui entraîne

> which implies

\[
M = \left( \begin{matrix} {e}_{1} \cdot  {e}_{1} & \cdots & {e}_{1} \cdot  {e}_{n} & {e}_{1} \cdot  x \\  \vdots & & \vdots & \vdots \\  {e}_{n} \cdot  {e}_{1} & \cdots & {e}_{n} \cdot  {e}_{n} & {e}_{n} \cdot  x \\  x \cdot  {e}_{1} & \cdots & x \cdot  {e}_{n} & x \cdot  x \end{matrix}\right)  = \left( \begin{matrix} {e}_{1} \cdot  {e}_{1} & \cdots & {e}_{1} \cdot  {e}_{n} & {e}_{1} \cdot  y \\  \vdots & & \vdots & \vdots \\  {e}_{n} \cdot  {e}_{1} & \cdots & {e}_{n} \cdot  {e}_{n} & {e}_{n} \cdot  y \\  y \cdot  {e}_{1} & \cdots & y \cdot  {e}_{n} & \parallel y{\parallel }^{2} + \parallel z{\parallel }^{2} \end{matrix}\right) .
\]

La linéarité de det \( M \) par rapport à sa dernière colonne entraîne det \( M = \det P + \det Q \) , où

> The linearity of det \( M \) with respect to its last column implies det \( M = \det P + \det Q \) , where

\[
P = \left( \begin{matrix} {e}_{1} \cdot  {e}_{1} & \cdots & {e}_{1} \cdot  {e}_{n} & {e}_{1} \cdot  y \\  \vdots & & \vdots & \vdots \\  {e}_{n} \cdot  {e}_{1} & \cdots & {e}_{n} \cdot  {e}_{n} & {e}_{n} \cdot  y \\  y \cdot  {e}_{1} & \cdots & y \cdot  {e}_{n} & \parallel y{\parallel }^{2} \end{matrix}\right) \;\text{ et }\;Q = \left( \begin{matrix} {e}_{1} \cdot  {e}_{1} & \cdots & {e}_{1} \cdot  {e}_{n} & 0 \\  \vdots & & \vdots & \vdots \\  {e}_{n} \cdot  {e}_{1} & \cdots & {e}_{n} \cdot  {e}_{n} & 0 \\  y \cdot  {e}_{1} & \cdots & y \cdot  {e}_{n} & \parallel z{\parallel }^{2} \end{matrix}\right) .
\]

Or \( \det P = G\left( {{e}_{1},\ldots ,{e}_{n}, y}\right) = 0 \) car \( y \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) et \( \det Q = \parallel z{\parallel }^{2}G\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) . Finale-ment

> However, \( \det P = G\left( {{e}_{1},\ldots ,{e}_{n}, y}\right) = 0 \) because \( y \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) and \( \det Q = \parallel z{\parallel }^{2}G\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) . Finally

\[
G\left( {{e}_{1},\ldots ,{e}_{n}, x}\right)  = \det M = \det Q = \parallel z{\parallel }^{2}G\left( {{e}_{1},\ldots ,{e}_{n}}\right)  = {d}^{2}G\left( {{e}_{1},\ldots ,{e}_{n}}\right) .
\]
