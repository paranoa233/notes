#### 3.2. Matrices and linear maps

*Français : 3.2. Matrices et applications linéaires*

Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v de dimension finie, \( \dim E = q \in {\mathbb{N}}^{ * },\dim F = p \in {\mathbb{N}}^{ * } \) . Soit \( B = \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) une base de \( E,{B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{p}^{\prime }}\right) \) une base de \( F \) . Soit \( f \in \mathcal{L}\left( {E, F}\right) \) . Pour tout \( j,1 \leq j \leq q \) , on peut écrire \( f\left( {e}_{j}\right) = \mathop{\sum }\limits_{{i = 1}}^{\widehat{p}}{a}_{i, j}{e}_{i}^{\prime } \) où les \( {a}_{i, j} \in \mathbb{K} \) . La matrice \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \) est appelée matrice de \( f \) dans les bases \( B \) et \( {B}^{\prime } \) et notée \( {\left\lbrack f\right\rbrack }_{B}^{{B}^{\prime }} \) . Il revient au même de dire que les vecteurs colonnes de la matrice \( {\left\lbrack f\right\rbrack }_{B}^{{B}^{\prime }} \) sont les coordonnées dans la base \( {B}^{\prime } \) des images par \( f \) des vecteurs composant la base \( B \) .

> Let \( E \) and \( F \) be two finite-dimensional \( \mathbb{K} \) -vector spaces, \( \dim E = q \in {\mathbb{N}}^{ * },\dim F = p \in {\mathbb{N}}^{ * } \) . Let \( B = \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) be a basis of \( E,{B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{p}^{\prime }}\right) \) and \( F \) a basis of \( F \) . Let \( f \in \mathcal{L}\left( {E, F}\right) \) . For any \( j,1 \leq j \leq q \) , we can write \( f\left( {e}_{j}\right) = \mathop{\sum }\limits_{{i = 1}}^{\widehat{p}}{a}_{i, j}{e}_{i}^{\prime } \) where the \( {a}_{i, j} \in \mathbb{K} \) . The matrix \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \) is called the matrix of \( f \) in the bases \( B \) and \( {B}^{\prime } \) and is denoted by \( {\left\lbrack f\right\rbrack }_{B}^{{B}^{\prime }} \) . It is equivalent to say that the column vectors of the matrix \( {\left\lbrack f\right\rbrack }_{B}^{{B}^{\prime }} \) are the coordinates in the basis \( {B}^{\prime } \) of the images under \( f \) of the vectors composing the basis \( B \) .

On munit \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) des opérations suivantes :

> We equip \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) with the following operations:

- Si \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) et \( B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) , on définit \( A + B = {\left( {a}_{i, j} + {b}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) .

> - If \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) and \( B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) , we define \( A + B = {\left( {a}_{i, j} + {b}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) .

- Si \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) et \( \lambda  \in  \mathbb{K} \) , on définit \( {\lambda A} = {\left( \lambda {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) .

> - If \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) and \( \lambda  \in  \mathbb{K} \) , we define \( {\lambda A} = {\left( \lambda {a}_{i, j}\right) }_{\begin{matrix} {1 \leq  i \leq  p} \\  {1 \leq  j \leq  q} \end{matrix}} \) .

Muni de ces opérations, \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) est un \( \mathbb{K} \) -e.v. Si pour tout \( \left( {i, j}\right) ,1 \leq i \leq p,1 \leq j \leq q \) , \( {E}_{i, j} \) désigne la matrice dont tous les éléments sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1, les \( {E}_{i, j}\left( {1 \leq i \leq p,1 \leq j \leq q}\right) \) forment une base de \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) appelée base canonique de \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . Ceci entraîne en particulier le résultat suivant.

> Equipped with these operations, \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) is a \( \mathbb{K} \) -v.s. If for all \( \left( {i, j}\right) ,1 \leq i \leq p,1 \leq j \leq q \) , \( {E}_{i, j} \) denotes the matrix whose elements are all zero except for the one with index \( \left( {i, j}\right) \) which equals 1, the \( {E}_{i, j}\left( {1 \leq i \leq p,1 \leq j \leq q}\right) \) form a basis of \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) called the canonical basis of \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . This leads in particular to the following result.

PROPOSITION 1. Le \( \mathbb{K} \) -e.v \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) est de dimension finie pq.

> PROPOSITION 1. The \( \mathbb{K} \) -v.s. \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) is of finite dimension pq.

Fixons deux bases \( B \) de \( E \) et \( {B}^{\prime } \) de \( F \) . L’application

> Let us fix two bases \( B \) of \( E \) and \( {B}^{\prime } \) of \( F \) . The mapping

\[
\Phi  : \mathcal{L}\left( {E, F}\right)  \rightarrow  {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \;f \mapsto  {\left\lbrack  f\right\rbrack  }_{B}^{{B}^{\prime }}
\]

est un isomorphisme de \( \mathbb{K} \) -e.v. En particulier, \( \dim \left( {\mathcal{L}\left( {E, F}\right) }\right) = \dim \left( {{\mathcal{M}}_{p, q}\left( \mathbb{K}\right) }\right) = {pq} = \; \left( {\dim E}\right) \cdot \left( {\dim F}\right) \) .

> is an isomorphism of \( \mathbb{K} \) -v.s. In particular, \( \dim \left( {\mathcal{L}\left( {E, F}\right) }\right) = \dim \left( {{\mathcal{M}}_{p, q}\left( \mathbb{K}\right) }\right) = {pq} = \; \left( {\dim E}\right) \cdot \left( {\dim F}\right) \) .

Multiplication de matrices.

> Matrix multiplication.

DéFINITION 5. Soient \( p, q, r \in {\mathbb{N}}^{ * } \) et \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) , B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq q} \\ {1 \leq j \leq r} \end{matrix}} \in \; {\mathcal{M}}_{q, r}\left( \mathbb{K}\right) \) . On définit la matrice \( C = {\left( {c}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq r} \end{matrix}} \in {\overline{\mathcal{M}}}_{p, r}\left( \mathbb{K}\right) \) par \( {c}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{q}{a}_{i, k}{b}_{k, j} \) . La matrice \( C \) est appelée produit des matrices \( A \) et \( B \) et on note \( C = {AB} \) .

> DEFINITION 5. Let \( p, q, r \in {\mathbb{N}}^{ * } \) and \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) , B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq q} \\ {1 \leq j \leq r} \end{matrix}} \in \; {\mathcal{M}}_{q, r}\left( \mathbb{K}\right) \) . We define the matrix \( C = {\left( {c}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq r} \end{matrix}} \in {\overline{\mathcal{M}}}_{p, r}\left( \mathbb{K}\right) \) by \( {c}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{q}{a}_{i, k}{b}_{k, j} \) . The matrix \( C \) is called the product of matrices \( A \) and \( B \) and is denoted by \( C = {AB} \) .

Remarque 2. - Attention, le produit de \( A \) par \( B \) ne peut être réalisé que si le nombre de lignes de \( B \) est égal au nombre de colonnes de \( A \) .

> Remark 2. - Note that the product of \( A \) by \( B \) can only be performed if the number of rows of \( B \) is equal to the number of columns of \( A \) .

— Le produit de matrices est associatif (mais pas commutatif) et distributif par rapport à l'addition.

> — Matrix multiplication is associative (but not commutative) and distributive with respect to addition.

- Soit \( f \in  \mathcal{L}\left( {E, F}\right) , B \) une base de \( E,{B}^{\prime } \) une base de \( F \) . Soit \( x \in  E \) et \( y = f\left( x\right) \) . On note \( X \) la matrice colonne dont les éléments sont les coordonnées de \( x \) dans la base \( B, Y \) la matrice colonne dont les éléments sont les coordonnées de \( y = f\left( x\right) \) dans la base \( {B}^{\prime } \) . On a alors \( Y = {\left\lbrack  f\right\rbrack  }_{B}^{{B}^{\prime }}X \) , au sens du produit de matrices défini plus haut.

> - Let \( f \in  \mathcal{L}\left( {E, F}\right) , B \) be a basis of \( E,{B}^{\prime } \) a basis of \( F \) . Let \( x \in  E \) and \( y = f\left( x\right) \) . We denote by \( X \) the column matrix whose elements are the coordinates of \( x \) in the basis \( B, Y \) the column matrix whose elements are the coordinates of \( y = f\left( x\right) \) in the basis \( {B}^{\prime } \) . We then have \( Y = {\left\lbrack  f\right\rbrack  }_{B}^{{B}^{\prime }}X \) , in the sense of the matrix product defined above.

Proposition 2. Soient \( E, F \) et \( G \) des \( \mathbb{K} \) -e.v de dimensions finies. Soit \( B \) une base de \( E,{B}^{\prime } \) une base de \( F \) et \( {B}^{\prime \prime } \) une base de \( G \) . Si \( f \in \mathcal{L}\left( {F, G}\right) \) et \( g \in \mathcal{L}\left( {E, F}\right) \) , on a \( {\left\lbrack fg\right\rbrack }_{B}^{{B}^{\prime \prime }} = {\left\lbrack f\right\rbrack }_{{B}^{\prime }}^{{B}^{\prime \prime }}{\left\lbrack g\right\rbrack }_{B}^{{B}^{\prime }}. \)

> Proposition 2. Let \( E, F \) and \( G \) be finite-dimensional \( \mathbb{K} \) -vector spaces. Let \( B \) be a basis of \( E,{B}^{\prime } \) a basis of \( F \) and \( {B}^{\prime \prime } \) a basis of \( G \) . If \( f \in \mathcal{L}\left( {F, G}\right) \) and \( g \in \mathcal{L}\left( {E, F}\right) \) , we have \( {\left\lbrack fg\right\rbrack }_{B}^{{B}^{\prime \prime }} = {\left\lbrack f\right\rbrack }_{{B}^{\prime }}^{{B}^{\prime \prime }}{\left\lbrack g\right\rbrack }_{B}^{{B}^{\prime }}. \)

Remarque 3. (Produit par blocs). Si \( M \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) et \( {M}^{\prime } \in {\mathcal{M}}_{q, r}\left( \mathbb{K}\right) \) ,

> Remark 3. (Block multiplication). If \( M \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) and \( {M}^{\prime } \in {\mathcal{M}}_{q, r}\left( \mathbb{K}\right) \) ,

\[
M = \left( \begin{matrix} \overset{r}{A} & \overset{q - r}{B} \\  C & D \end{matrix}\right) ,\;{M}^{\prime } = \left. \left( \begin{matrix} {A}^{\prime } & {B}^{\prime } \\  {C}^{\prime } & {D}^{\prime } \end{matrix}\right) \right\}  {}_{q - r\text{ lignes }}^{r\text{ lignes }}
\]

alors

> then

\[
M{M}^{\prime } = \left( \begin{array}{ll} A{A}^{\prime } + B{C}^{\prime } & A{B}^{\prime } + B{D}^{\prime } \\  C{A}^{\prime } + D{C}^{\prime } & C{B}^{\prime } + D{D}^{\prime } \end{array}\right) .
\]

Tout se passe comme si on multipliait deux matrices \( 2 \times 2 \) , en prenant garde à l’ordre dans les produits (il n'y a pas commutativité).

> Everything proceeds as if we were multiplying two \( 2 \times 2 \) matrices, taking care of the order in the products (there is no commutativity).
