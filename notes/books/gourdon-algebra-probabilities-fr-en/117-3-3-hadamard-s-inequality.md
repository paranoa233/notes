#### 3.3. Hadamard's inequality

*Français : 3.3. Inégalité d'Hadamard*

Nous nous proposons de montrer le théorème suivant.

> We propose to prove the following theorem.

\( \rightarrow \) THÉORÉME 7. Les vecteurs colonnes \( {X}_{1},\ldots ,{X}_{n} \) d’une matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) vérifient

> \( \rightarrow \) THEOREM 7. The column vectors \( {X}_{1},\ldots ,{X}_{n} \) of a matrix \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) satisfy

\[
\left| {\det M}\right|  \leq  \begin{Vmatrix}{X}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{X}_{n}\end{Vmatrix},
\]

(*)

> où pour tout \( i,\begin{Vmatrix}{X}_{i}\end{Vmatrix} = \sqrt{{X}_{i}^{ * }{X}_{i}} \) désigne la norme hermitienne standard.

where for all \( i,\begin{Vmatrix}{X}_{i}\end{Vmatrix} = \sqrt{{X}_{i}^{ * }{X}_{i}} \) denotes the standard Hermitian norm.

> Si pour tout \( i,{X}_{i} \neq 0, l \) ’inégalité \( \left( *\right) \) est une égalité si et seulement si la famille \( \left( {X}_{i}\right) \) est orthogonale.

If for all \( i,{X}_{i} \neq 0, l \) the inequality \( \left( *\right) \) is an equality if and only if the family \( \left( {X}_{i}\right) \) is orthogonal.

> Démonstration. Si det \( M = 0 \) , l’inégalité est évidemment vérifiée. Sinon, \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) forme une base de \( {\mathbb{C}}^{n} \) . En utilisant le procédé d’orthonormalisation de Schmidt (voir la partie 2.2 de ce chapitre), on construit une base orthogonale \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) de \( {\mathbb{C}}^{n} \) telle que

Proof. If det \( M = 0 \), the inequality is obviously satisfied. Otherwise, \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) forms a basis of \( {\mathbb{C}}^{n} \). Using the Schmidt orthonormalization process (see part 2.2 of this chapter), we construct an orthogonal basis \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) of \( {\mathbb{C}}^{n} \) such that

\[
\forall k,{Y}_{k} = {X}_{k} + {\lambda }_{1, k}{Y}_{1} + \cdots  + {\lambda }_{k - 1, k}{Y}_{k - 1},\;{\lambda }_{i, k} \in  \mathbb{C}.
\]

On ne change pas un déterminant en retranchant à une colonne une combinaison linéaire des autres, ce qui prouve \( \det M = \det N \) , où \( N = \left( {{Y}_{1}\left| \cdots \right| {Y}_{n}}\right) \) est la matrice dont les vecteurs colonnes sont les \( {Y}_{i} \) . Posons \( D = {N}^{ * }N = {\left( {d}_{i, j}\right) }_{1 \leq i, j \leq n} \) . On voit facilement que \( {d}_{i, j} = {Y}_{i}^{ * }{Y}_{j} \) . Les \( {Y}_{i} \) étant orthogonaux deux à deux, on a \( {d}_{i, j} = 0 \) dès que \( i \neq j \) . Par ailleurs, \( {d}_{i, i} = {Y}_{i}^{ * }{Y}_{i} = {\begin{Vmatrix}{Y}_{i}\end{Vmatrix}}^{2} \) , d'où

> A determinant is not changed by subtracting a linear combination of the other columns from one column, which proves \( \det M = \det N \), where \( N = \left( {{Y}_{1}\left| \cdots \right| {Y}_{n}}\right) \) is the matrix whose column vectors are the \( {Y}_{i} \). Let \( D = {N}^{ * }N = {\left( {d}_{i, j}\right) }_{1 \leq i, j \leq n} \). We easily see that \( {d}_{i, j} = {Y}_{i}^{ * }{Y}_{j} \). Since the \( {Y}_{i} \) are pairwise orthogonal, we have \( {d}_{i, j} = 0 \) as soon as \( i \neq j \). Furthermore, \( {d}_{i, i} = {Y}_{i}^{ * }{Y}_{i} = {\begin{Vmatrix}{Y}_{i}\end{Vmatrix}}^{2} \), hence

\[
{N}^{ * }N = \left( \begin{matrix} {\begin{Vmatrix}{Y}_{1}\end{Vmatrix}}^{2} & & 0 \\   &  \ddots  & \\  0 & & {\begin{Vmatrix}{Y}_{n}\end{Vmatrix}}^{2} \end{matrix}\right) ,
\]

et donc

> and therefore

\[
\det \left( {{N}^{ * }N}\right)  = \det \left( {N}^{ * }\right) \det \left( N\right)  = {\left| \det \left( N\right) \right| }^{2} = \mathop{\prod }\limits_{{i = 1}}^{n}{\begin{Vmatrix}{Y}_{i}\end{Vmatrix}}^{2},
\]

ce qui entraîne \( \left| {\det N}\right| = \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{Y}_{i}\end{Vmatrix} \) . Or pour tout \( k,{X}_{k} = {Y}_{k} - {\lambda }_{1, k}{Y}_{1} - \cdots - {\lambda }_{k - 1, k}{Y}_{k - 1} \) , donc

> which implies \( \left| {\det N}\right| = \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{Y}_{i}\end{Vmatrix} \) . Now for all \( k,{X}_{k} = {Y}_{k} - {\lambda }_{1, k}{Y}_{1} - \cdots - {\lambda }_{k - 1, k}{Y}_{k - 1} \) , therefore

\[
{\begin{Vmatrix}{X}_{k}\end{Vmatrix}}^{2} = {\begin{Vmatrix}{Y}_{k}\end{Vmatrix}}^{2} + {\left| {\lambda }_{1, k}\right| }^{2}{\begin{Vmatrix}{Y}_{1}\end{Vmatrix}}^{2} + \cdots  + {\left| {\lambda }_{k - 1, k}\right| }^{2}{\begin{Vmatrix}{Y}_{k - 1}\end{Vmatrix}}^{2}.
\]

(*)

> Cette égalité entraîne \( \begin{Vmatrix}{Y}_{k}\end{Vmatrix} \leq \begin{Vmatrix}{X}_{k}\end{Vmatrix} \) , donc

This equality implies \( \begin{Vmatrix}{Y}_{k}\end{Vmatrix} \leq \begin{Vmatrix}{X}_{k}\end{Vmatrix} \) , therefore

\[
\left| {\det M}\right|  = \left| {\det N}\right|  = \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{Y}_{i}\end{Vmatrix} \leq  \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{X}_{i}\end{Vmatrix}.
\]

\( \left( {* * }\right) \)

> Cas d’égalité. Si les \( {X}_{i} \) sont orthogonaux entre eux deux à deux, on a \( {X}_{i} = {Y}_{i} \) pour tout \( i \) , et d’après ce que l’on a vu plus haut, \( \left| {\det M}\right| = \left| {\det N}\right| = \begin{Vmatrix}{Y}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{Y}_{n}\end{Vmatrix} = \begin{Vmatrix}{X}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{X}_{n}\end{Vmatrix} \) .

Equality case. If the \( {X}_{i} \) are pairwise orthogonal, we have \( {X}_{i} = {Y}_{i} \) for all \( i \) , and according to what we saw above, \( \left| {\det M}\right| = \left| {\det N}\right| = \begin{Vmatrix}{Y}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{Y}_{n}\end{Vmatrix} = \begin{Vmatrix}{X}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{X}_{n}\end{Vmatrix} \) .

> Réciproquement, supposons qu’il y ait égalité et que pour tout \( i,{X}_{i} \neq 0 \) . Alors det \( M \neq 0 \) . Il faut alors que \( \left( {* * }\right) \) soit une égalité, c’est à dire \( \begin{Vmatrix}{Y}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{Y}_{n}\end{Vmatrix} = \begin{Vmatrix}{X}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{X}_{n}\end{Vmatrix} \neq 0 \) . Or, pour tout \( i,\begin{Vmatrix}{Y}_{i}\end{Vmatrix} \leq \begin{Vmatrix}{X}_{i}\end{Vmatrix} \) , on doit donc avoir \( \begin{Vmatrix}{X}_{i}\end{Vmatrix} = \begin{Vmatrix}{Y}_{i}\end{Vmatrix} \) pour tout \( i \) . Ceci entraîne avec \( \left( *\right) \) que tous les \( {\lambda }_{j, k} \) sont nuls, donc que \( {Y}_{k} = {X}_{k} \) pour tout \( k \) . Les \( {X}_{i} \) sont donc deux à deux orthogonaux.

Conversely, suppose there is equality and that for all \( i,{X}_{i} \neq 0 \) . Then det \( M \neq 0 \) . It must then be that \( \left( {* * }\right) \) is an equality, that is to say \( \begin{Vmatrix}{Y}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{Y}_{n}\end{Vmatrix} = \begin{Vmatrix}{X}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{X}_{n}\end{Vmatrix} \neq 0 \) . Now, for all \( i,\begin{Vmatrix}{Y}_{i}\end{Vmatrix} \leq \begin{Vmatrix}{X}_{i}\end{Vmatrix} \) , we must therefore have \( \begin{Vmatrix}{X}_{i}\end{Vmatrix} = \begin{Vmatrix}{Y}_{i}\end{Vmatrix} \) for all \( i \) . This implies with \( \left( *\right) \) that all \( {\lambda }_{j, k} \) are zero, therefore that \( {Y}_{k} = {X}_{k} \) for all \( k \) . The \( {X}_{i} \) are therefore pairwise orthogonal.

> Remarque 8. Le théorème reste vrai dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \subset {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

Remark 8. The theorem remains true in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \subset {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .
