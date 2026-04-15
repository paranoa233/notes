#### 3.6. Rank of a matrix

*Français : 3.6. Rang d'une matrice*

DéFINITION 8. Soit \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . On appelle rang de \( A \) le rang de ses vecteurs colonnes dans \( {\mathbb{K}}^{p} \) , et on le note rg \( A \) . Si \( A \) est la matrice d’une application linéaire \( f \) , on a rg \( A = \; \operatorname{rg}f \) .

> DEFINITION 8. Let \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . The rank of \( A \) is defined as the rank of its column vectors in \( {\mathbb{K}}^{p} \) , and is denoted by rg \( A \) . If \( A \) is the matrix of a linear map \( f \) , we have rg \( A = \; \operatorname{rg}f \) .

Remarque 7. - Si \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) , alors \( \operatorname{rg}A \leq \inf \{ p, q\} \) .

> Remark 7. - If \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) , then \( \operatorname{rg}A \leq \inf \{ p, q\} \) .

- Si \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , alors \( A \) est inversible si et seulement si rg \( A = n \) .

> - If \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , then \( A \) is invertible if and only if rg \( A = n \) .

THÉORÉME 1. Soit \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . Si \( r = \operatorname{rg}A \geq 1 \) , \( A \) est équivalente à la matrice

> THEOREM 1. Let \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . If \( r = \operatorname{rg}A \geq 1 \) , \( A \) is equivalent to the matrix

\[
{J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right) .
\]

COROLLAIRE 1. Deux matrices \( A \) et \( B \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) sont équivalentes si et seulement si \( \operatorname{rg}A = \operatorname{rg}B \) .

> COROLLARY 1. Two matrices \( A \) and \( B \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) are equivalent if and only if \( \operatorname{rg}A = \operatorname{rg}B \) .

DéFINITION 9. Soit \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) , et soient deux sous-ensembles non vides \( I \subset \{ 1,\ldots , p\} \) et \( J \subset \{ 1,\ldots , q\} \) . La matrice \( B = {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) s’appelle matrice extraite de \( A, A \) s’appelle une matrice bordante de \( B \) .

> DEFINITION 9. Let \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) , and let two non-empty subsets be \( I \subset \{ 1,\ldots , p\} \) and \( J \subset \{ 1,\ldots , q\} \) . The matrix \( B = {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) is called a submatrix of \( A, A \) and is called a bordering matrix of \( B \) .

THÉORÉME 2. Soit \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . Le rang de \( A \) est le plus grand des ordres des matrices carrées inversibles extraites de A.

> THEOREM 2. Let \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . The rank of \( A \) is the largest order of the invertible square matrices extracted from A.

COROLLAIRE 2. Le rang de toute matrice est égal au rang de sa transposée.

> COROLLARY 2. The rank of any matrix is equal to the rank of its transpose.

Remarque 8. En d'autres termes, le corollaire précédent dit que le rang des vecteurs colonnes d'une matrice est égal au rang de ses vecteurs ligne.

> Remark 8. In other words, the previous corollary states that the rank of the column vectors of a matrix is equal to the rank of its row vectors.

- Dans la pratique, pour trouver le rang d'une matrice, on utilise le résultat suivant : on ne change pas le rang d'une matrice en multipliant une colonne par un scalaire non nul, ou en ajoutant a une colonne une combinaison linéaire des autres colonnes (même chose sur les lignes). Par exemple, en opérant sur les lignes,

> - In practice, to find the rank of a matrix, we use the following result: the rank of a matrix does not change when multiplying a column by a non-zero scalar, or by adding a linear combination of other columns to a column (the same applies to rows). For example, by performing operations on the rows,

\[
\operatorname{rg}\left( \begin{matrix} 2 & 1 & 3 &  - 3 \\   - 1 & 2 & 1 & 4 \\  1 & 1 & 2 &  - 1 \end{matrix}\right)  = \operatorname{rg}\left( \begin{matrix} 2 & 1 & 3 &  - 3 \\  0 & 3 & 3 & 3 \\  1 & 1 & 2 &  - 1 \end{matrix}\right)
\]

\[
= \operatorname{rg}\left( \begin{matrix} 2 & 1 & 3 &  - 3 \\  0 & 1 & 1 & 1 \\  2 & 2 & 4 &  - 2 \end{matrix}\right)  = \operatorname{rg}\left( \begin{matrix} 2 & 1 & 3 &  - 3 \\  0 & 1 & 1 & 1 \\  0 & 1 & 1 & 1 \end{matrix}\right)  = 2.
\]
