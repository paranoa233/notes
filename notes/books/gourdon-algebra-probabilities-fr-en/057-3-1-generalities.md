#### 3.1. Generalities

*Français : 3.1. Généralités*

DéFINITION 1. Soient \( p \) et \( q \in {\mathbb{N}}^{ * } \) . On appelle matrice de type \( \left( {p, q}\right) \) ou matrice à \( p \) lignes et \( q \) colonnes à coefficients dans \( \mathbb{K} \) , toute famille \( {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \) avec pour tout \( \left( {i, j}\right) ,{a}_{i, j} \in \mathbb{K} \) . On note cette matrice de la manière suivante

> DEFINITION 1. Let \( p \) and \( q \in {\mathbb{N}}^{ * } \) . A matrix of type \( \left( {p, q}\right) \) or a matrix with \( p \) rows and \( q \) columns with coefficients in \( \mathbb{K} \) is any family \( {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \) with for all \( \left( {i, j}\right) ,{a}_{i, j} \in \mathbb{K} \) . We denote this matrix as follows

\[
p\text{ lignes }\left\{  {\left( \begin{matrix} \overset{q\text{ colonnes }}{\overbrace{{a}_{1,1}\;{a}_{1,2}\;\cdots \;{a}_{1, q}}} \\  {a}_{2,1}\;{a}_{2,2}\;\cdots \;{a}_{2, q} \\  \vdots \;\vdots \; \ddots  \;\vdots \\  {a}_{p,1}\;{a}_{p,2}\;\cdots \;{a}_{p, q} \end{matrix}\right) \text{ . }}\right.
\]

DÉFINITION 2. L’ensemble des matrices de type \( \left( {p, q}\right) \) à coefficients dans \( \mathbb{K} \) est noté \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) .

> DEFINITION 2. The set of matrices of type \( \left( {p, q}\right) \) with coefficients in \( \mathbb{K} \) is denoted by \( {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) .

— (Cas \( q = 1 \) ). Un élément de \( {\mathcal{M}}_{p,1}\left( \mathbb{K}\right) \) s’appelle une matrice colonne.

> — (Case \( q = 1 \) ). An element of \( {\mathcal{M}}_{p,1}\left( \mathbb{K}\right) \) is called a column matrix.

— (Cas \( p = 1 \) ). Un élément de \( {\mathcal{M}}_{1, q}\left( \mathbb{K}\right) \) s’appelle une matrice ligne.

> — (Case \( p = 1 \) ). An element of \( {\mathcal{M}}_{1, q}\left( \mathbb{K}\right) \) is called a row matrix.

— (Cas \( p = q \) ). Les éléments de \( {\mathcal{M}}_{p, p}\left( \mathbb{K}\right) \) s’appellent des matrices carrées. On note \( {\mathcal{M}}_{p}\left( \mathbb{K}\right) = {\mathcal{M}}_{p, p}\left( \mathbb{K}\right) \) , appelé ensemble des matrices carrées d’ordre (ou de taille) \( p \) .

> — (Case \( p = q \) ). The elements of \( {\mathcal{M}}_{p, p}\left( \mathbb{K}\right) \) are called square matrices. We denote \( {\mathcal{M}}_{p}\left( \mathbb{K}\right) = {\mathcal{M}}_{p, p}\left( \mathbb{K}\right) \) , called the set of square matrices of order (or size) \( p \) .

DÉFINITION 3. Soit \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . On appelle matrice transposée de \( A \) et on note \( {}^{\mathrm{t}}A \) la matrice \( B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq q} \\ {1 \leq j \leq p} \end{matrix}} \in {\mathcal{M}}_{q, p}\left( \mathbb{K}\right) \) avec \( {b}_{i, j} = {a}_{j, i} \) .

> DEFINITION 3. Let \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . The transpose of \( A \) , denoted by \( {}^{\mathrm{t}}A \) , is the matrix \( B = {\left( {b}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq q} \\ {1 \leq j \leq p} \end{matrix}} \in {\mathcal{M}}_{q, p}\left( \mathbb{K}\right) \) with \( {b}_{i, j} = {a}_{j, i} \) .

Remarque 1. - La représentation sous forme de tableau de la matrice \( {}^{\mathrm{t}}A \) est le sy-métrique de celle de \( A \) par rapport à la diagonale constituée des coefficients \( {a}_{i, i} \) .

> Remark 1. - The tabular representation of matrix \( {}^{\mathrm{t}}A \) is the symmetric of that of \( A \) with respect to the diagonal consisting of the coefficients \( {a}_{i, i} \) .

- Pour toute matrice \( A,{}^{\mathrm{t}}\left( {{}^{\mathrm{t}}A}\right)  = A \) .

> - For any matrix \( A,{}^{\mathrm{t}}\left( {{}^{\mathrm{t}}A}\right)  = A \) .

DéFINITION 4 (DéFINITIONS RELATIVES AUX MATRICES CARRÉES). Soit \( n \in {\mathbb{N}}^{ * } \) et une matrice \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq n} \\ {1 \leq j \leq n} \end{matrix}} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> DEFINITION 4 (DEFINITIONS RELATING TO SQUARE MATRICES). Let \( n \in {\mathbb{N}}^{ * } \) and a matrix \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq n} \\ {1 \leq j \leq n} \end{matrix}} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

- Les \( {\left( {a}_{i, i}\right) }_{1 \leq  i \leq  n} \) s’appellent les éléments diagonaux de \( A \) .

> - The \( {\left( {a}_{i, i}\right) }_{1 \leq  i \leq  n} \) are called the diagonal elements of \( A \) .

- La diagonale principale de \( A \) est l’ensemble de ses éléments diagonaux.

> - The main diagonal of \( A \) is the set of its diagonal elements.

Si \( {a}_{i, j} = 0 \) pour \( i > j, A \) est dite triangulaire (ou trigonale) supérieure \( \left( \begin{matrix} \ddots & \ddots \\ 0 & \ddots \end{matrix}\right) \) .

> If \( {a}_{i, j} = 0 \) for \( i > j, A \) , it is said to be upper triangular (or trigonal) \( \left( \begin{matrix} \ddots & \ddots \\ 0 & \ddots \end{matrix}\right) \) .

- Si \( {a}_{i, j} = 0 \) pour \( i < j, A \) est dite triangulaire (ou trigonale) inférieure \( \left( \begin{matrix}  \ddots  & 0 \\   \ddots  &  \ddots   \end{matrix}\right) \) .

> - If \( {a}_{i, j} = 0 \) for \( i < j, A \) , it is said to be lower triangular (or trigonal) \( \left( \begin{matrix}  \ddots  & 0 \\   \ddots  &  \ddots   \end{matrix}\right) \) .

- Si \( {a}_{i, j} = 0 \) pour \( i \neq  j, A \) est dite diagonale.

> - If \( {a}_{i, j} = 0 \) for \( i \neq  j, A \) , it is said to be diagonal.

- S’il existe \( \lambda  \in  \mathbb{K} \) tel que pour tout \( i,{a}_{i, i} = \lambda \) et pour tout \( i \neq  j,{a}_{i, j} = 0 \) , on dit que \( A \) est une matrice scalaire.

> - If there exists \( \lambda  \in  \mathbb{K} \) such that for all \( i,{a}_{i, i} = \lambda \) and for all \( i \neq  j,{a}_{i, j} = 0 \) , \( A \) is said to be a scalar matrix.

- Si pour tout \( \left( {i, j}\right) ,{a}_{i, j} = {a}_{j, i} \) (de manière équivalente si \( {}^{\mathrm{t}}A = A \) ), \( A \) est dite symétrique.

> - If for all \( \left( {i, j}\right) ,{a}_{i, j} = {a}_{j, i} \) (equivalently if \( {}^{\mathrm{t}}A = A \) ), \( A \) is said to be symmetric.

- Si pour tout \( \left( {i, j}\right) ,{a}_{i, j} =  - {a}_{j, i} \) (de manière équivalente si \( {}^{\mathrm{t}}A =  - A \) ), \( A \) est dite antisymétrique. Dans ce cas, si \( \mathbb{K} \) est de caractéristique différente de 2, les éléments diagonaux de \( A \) sont nuls.

> - If for all \( \left( {i, j}\right) ,{a}_{i, j} =  - {a}_{j, i} \) (equivalently if \( {}^{\mathrm{t}}A =  - A \) ), \( A \) is said to be antisymmetric. In this case, if \( \mathbb{K} \) has a characteristic different from 2, the diagonal elements of \( A \) are zero.
