#### 2.2. Orthogonality

*Français : 2.2. Orthogonalité*

L'orthogonalité définie pour une forme quadratique ou hermitienne s'applique en par-ticulier pour un produit scalaire. Ainsi, deux vecteurs \( x \) et \( y \) sont dit orthogonaux si et seulement si \( x \cdot y = 0 \) (ou encore si et seulement si \( y \cdot x = 0 \) ).

> Orthogonality defined for a quadratic or Hermitian form applies in particular to an inner product. Thus, two vectors \( x \) and \( y \) are said to be orthogonal if and only if \( x \cdot y = 0 \) (or equivalently if and only if \( y \cdot x = 0 \)).

Une famille de vecteurs non nuls \( {\left( {e}_{i}\right) }_{i \in I} \) est dite orthogonale si elle vérifie \( {e}_{i} \cdot {e}_{j} = 0 \) dès que \( i \neq j \) (et c’est alors une famille libre). Si de plus on a \( \begin{Vmatrix}{e}_{i}\end{Vmatrix} = 1 \) pour tout \( i \in I \) , la famille est dite orthonormale (ou orthonormée).

> A family of non-zero vectors \( {\left( {e}_{i}\right) }_{i \in I} \) is said to be orthogonal if it satisfies \( {e}_{i} \cdot {e}_{j} = 0 \) whenever \( i \neq j \) (and it is then a linearly independent family). If, in addition, we have \( \begin{Vmatrix}{e}_{i}\end{Vmatrix} = 1 \) for all \( i \in I \), the family is said to be orthonormal.

On peut ainsi parler de base orthogonale ou orthonormale. Si \( E \) est un espace euclidien (resp. hermitien) et si \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base orthonormée de \( E \) , alors

> We can thus speak of an orthogonal or orthonormal basis. If \( E \) is a Euclidean (resp. Hermitian) space and if \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is an orthonormal basis of \( E \), then

\[
\forall x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \in  E,\;\forall y = \mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}{e}_{i} \in  E,\;x \cdot  y = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{y}_{i}\;\text{ (resp. }x \cdot  y = \mathop{\sum }\limits_{{i = 1}}^{n}\overline{{x}_{i}}{y}_{i}\text{ ). }
\]

Les coordonnées \( \left( {x}_{i}\right) \) de \( x \) dans la base orthonormale \( \left( {e}_{i}\right) \) de \( E \) vérifient \( {x}_{i} = {e}_{i} \cdot x \) .

> The coordinates \( \left( {x}_{i}\right) \) of \( x \) in the orthonormal basis \( \left( {e}_{i}\right) \) of \( E \) satisfy \( {x}_{i} = {e}_{i} \cdot x \).

Proposition 1. Si \( {\left( {e}_{i}\right) }_{i \in I} \) est une famille finie orthogonale de vecteurs de \( E \) , on a l’égalité \( {\begin{Vmatrix}\mathop{\sum }\limits_{{i \in I}}{e}_{i}\end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{i \in I}}{\begin{Vmatrix}{e}_{i}\end{Vmatrix}}^{2}. \)

> Proposition 1. If \( {\left( {e}_{i}\right) }_{i \in I} \) is a finite orthogonal family of vectors of \( E \), we have the equality \( {\begin{Vmatrix}\mathop{\sum }\limits_{{i \in I}}{e}_{i}\end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{i \in I}}{\begin{Vmatrix}{e}_{i}\end{Vmatrix}}^{2}. \)

Remarque 2. Dans un espace préhilbertien réel, si \( \parallel x + y{\parallel }^{2} = \parallel x{\parallel }^{2} + \parallel y{\parallel }^{2} \) , alors \( x \) et \( y \) sont orthogonaux. Ceci est faux dans un espace préhilbertien complexe (par exemple, si \( x \neq 0,\parallel x + {ix}{\parallel }^{2} = {\left| 1 + i\right| }^{2}\parallel x{\parallel }^{2} = 2\parallel x{\parallel }^{2} = \parallel x{\parallel }^{2} + \parallel {ix}{\parallel }^{2} \) et pourtant \( x \) et \( {ix} \) ne sont pas orthogonaux).

> Remark 2. In a real pre-Hilbert space, if \( \parallel x + y{\parallel }^{2} = \parallel x{\parallel }^{2} + \parallel y{\parallel }^{2} \), then \( x \) and \( y \) are orthogonal. This is false in a complex pre-Hilbert space (for example, if \( x \neq 0,\parallel x + {ix}{\parallel }^{2} = {\left| 1 + i\right| }^{2}\parallel x{\parallel }^{2} = 2\parallel x{\parallel }^{2} = \parallel x{\parallel }^{2} + \parallel {ix}{\parallel }^{2} \) and yet \( x \) and \( {ix} \) are not orthogonal).

THÉORÉME 1 (DE LA MÉDIANE). Pour tout couple \( \left( {x, y}\right) \in {E}^{2} \) , on a

> THEOREM 1 (APOLLONIUS' THEOREM). For any pair \( \left( {x, y}\right) \in {E}^{2} \), we have

\[
\parallel x + y{\parallel }^{2} + \parallel x - y{\parallel }^{2} = 2\left( {\parallel x{\parallel }^{2} + \parallel y{\parallel }^{2}}\right) .
\]

Remarque 3. - On peut montrer réciproquement que si une norme vérifie cette relation, c'est une norme euclidienne (resp. hermitienne) — voir l'exercice 9 page 263.

> Remark 3. - Conversely, it can be shown that if a norm satisfies this relation, it is a Euclidean (resp. Hermitian) norm — see exercise 9 on page 263.

- Le théorème de la médiane est encore appelé identité du parallélogramme.

> - The median theorem is also called the parallelogram identity.

Procédé d'orthogonalisation de Schmidt. Nous allons construire, en partant d'une famille libre finie \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de vecteurs de \( E \) , une base orthogonale \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) de \( \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) telle que pour tout \( k,{u}_{k} \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \) . On procède par récurrence.

> Gram-Schmidt orthogonalization process. Starting from a finite linearly independent family \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of vectors of \( E \), we will construct an orthogonal basis \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) of \( \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) such that for all \( k,{u}_{k} \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \). We proceed by induction.

- On prend \( {u}_{1} = {e}_{1} \) .

> - We take \( {u}_{1} = {e}_{1} \).

- On cherche \( {u}_{2} \) sous la forme \( {e}_{2} + {\lambda }_{1,2}{u}_{1} \) . On veut que \( {u}_{1} \cdot  {u}_{2} = 0 \) , ce qui sera réalisé si et seulement si

> - We look for \( {u}_{2} \) in the form \( {e}_{2} + {\lambda }_{1,2}{u}_{1} \). We want \( {u}_{1} \cdot  {u}_{2} = 0 \), which will be achieved if and only if

\[
{\lambda }_{1,2} =  - \frac{{u}_{1} \cdot  {e}_{2}}{{\begin{Vmatrix}{u}_{1}\end{Vmatrix}}^{2}}.
\]

- Les vecteurs \( {u}_{1},\ldots ,{u}_{k - 1} \) étant construits, on cherche \( {u}_{k} \) sous la forme \( {e}_{k} + {\lambda }_{1, k}{u}_{1} + \; \cdots  + {\lambda }_{k - 1, k}{u}_{k - 1} \) . On veut que \( {u}_{i} \cdot  {u}_{k} = 0 \) pour \( 1 \leq  i \leq  k - 1 \) , ce qui sera réalisé si et seulement si on prend

> - With the vectors \( {u}_{1},\ldots ,{u}_{k - 1} \) constructed, we look for \( {u}_{k} \) in the form \( {e}_{k} + {\lambda }_{1, k}{u}_{1} + \; \cdots  + {\lambda }_{k - 1, k}{u}_{k - 1} \) . We want \( {u}_{i} \cdot  {u}_{k} = 0 \) for \( 1 \leq  i \leq  k - 1 \) , which will be achieved if and only if we take

\[
{\lambda }_{i, k} =  - \frac{{u}_{i} \cdot  {e}_{k}}{{\begin{Vmatrix}{u}_{i}\end{Vmatrix}}^{2}}.
\]

En normant les vecteurs \( {u}_{i} \) , on obtient même une base orthonormée.

> By normalizing the vectors \( {u}_{i} \) , we even obtain an orthonormal basis.

Remarque 4. La matrice de passage de la famille \( \left( {e}_{i}\right) \) à la famille \( \left( {u}_{j}\right) \) est de la forme

> Remark 4. The transition matrix from the family \( \left( {e}_{i}\right) \) to the family \( \left( {u}_{j}\right) \) is of the form

\[
P = \left( \begin{matrix} 1 &  \times  & \cdots &  \times  \\  0 & 1 &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & 1 \end{matrix}\right) .
\]

THÉORÉME 2. Soit E un espace préhilbertien (réel ou complexe) et F un s.e.v de E. Alors (i) \( F \subset {F}^{ \bot \bot } \)

> THEOREM 2. Let E be a pre-Hilbert space (real or complex) and F a subspace of E. Then (i) \( F \subset {F}^{ \bot \bot } \)

(ii) Si \( F \) est de dimension finie, on a \( E = F \oplus {F}^{ \bot } \) et \( F = {F}^{ \bot \bot } \) .

> (ii) If \( F \) is finite-dimensional, we have \( E = F \oplus {F}^{ \bot } \) and \( F = {F}^{ \bot \bot } \) .

Démonstration. L'assertion (i) résulte de la proposition 3 de la section 1 et la (ii) est une application de la proposition 7 page 245.

> Proof. Assertion (i) follows from proposition 3 of section 1 and (ii) is an application of proposition 7 on page 245.

Remarque 5. L'assertion (ii) reste vraie en dimension infinie si \( F \) est complet mais est fausse dans le cas général (voir l'exercice 11 page 265).

> Remark 5. Assertion (ii) remains true in infinite dimension if \( F \) is complete but is false in the general case (see exercise 11 on page 265).

Projection et symétrie orthogonale.

> Orthogonal projection and symmetry.

DéFINITION 1. Soit \( E \) un espace préhilbertien et \( F \) un s.e.v de \( E \) de dimension finie. Le théorème précédent dit que \( F \oplus {F}^{ \bot } = E \) .

> DEFINITION 1. Let \( E \) be a pre-Hilbert space and \( F \) a finite-dimensional subspace of \( E \) . The previous theorem states that \( F \oplus {F}^{ \bot } = E \) .

- On appelle projection orthogonale sur \( F \) la projection sur \( F \) parallèlement à \( {F}^{ \bot  } \) .

> - We call orthogonal projection onto \( F \) the projection onto \( F \) parallel to \( {F}^{ \bot  } \) .

- On appelle symétrie orthogonale par rapport à \( F \) la symétrie par rapport à \( F \) parallèlement à \( {F}^{ \bot  } \) .

> - We call orthogonal symmetry with respect to \( F \) the symmetry with respect to \( F \) parallel to \( {F}^{ \bot  } \) .

Remarque 6. Si \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base orthonormale de \( F \) , alors la projection orthogo-nale de \( x \) sur \( F \) est égale à \( y = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \) avec \( {\lambda }_{i} = {e}_{i} \cdot x \) .

> Remark 6. If \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is an orthonormal basis of \( F \) , then the orthogonal projection of \( x \) onto \( F \) is equal to \( y = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \) with \( {\lambda }_{i} = {e}_{i} \cdot x \) .

PROPOSITION 2. Soit E un espace préhilbertien et F un s.e.v de E de dimension finie. Soit \( x \in E \) et p la projection orthogonale sur F. Alors la distance de \( x \) à \( F \) vérifie \( d\left( {x, F}\right) = \parallel x - p\left( x\right) \parallel . \)

> PROPOSITION 2. Let E be a pre-Hilbert space and F a finite-dimensional subspace of E. Let \( x \in E \) and p be the orthogonal projection onto F. Then the distance from \( x \) to \( F \) satisfies \( d\left( {x, F}\right) = \parallel x - p\left( x\right) \parallel . \)

Démonstration. Soit \( y \in F \) . On a \( x - y = \left( {x - p\left( x\right) }\right) + \left( {p\left( x\right) - y}\right) \) . Or \( x - p\left( x\right) \in {F}^{ \bot } \) et \( p\left( x\right) - y \in F \) , donc \( \parallel x - y{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} + \parallel p\left( x\right) - y{\parallel }^{2} \) , donc \( \mathop{\inf }\limits_{{y \in F}}\parallel x - y{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} \) , d’où le résultat.

> Proof. Let \( y \in F \) . We have \( x - y = \left( {x - p\left( x\right) }\right) + \left( {p\left( x\right) - y}\right) \) . Now \( x - p\left( x\right) \in {F}^{ \bot } \) and \( p\left( x\right) - y \in F \) , so \( \parallel x - y{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} + \parallel p\left( x\right) - y{\parallel }^{2} \) , so \( \mathop{\inf }\limits_{{y \in F}}\parallel x - y{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} \) , hence the result.

Remarque 7. Comme \( x - p\left( x\right) \) est orthogonal à \( p\left( x\right) \) , la relation \( x = \left( {x - p\left( x\right) }\right) + p\left( x\right) \) entraîne \( \parallel x{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} + \parallel p\left( x\right) {\parallel }^{2} \) , donc \( d{\left( x, F\right) }^{2} = \parallel x{\parallel }^{2} - \parallel p\left( x\right) {\parallel }^{2} \) . Si \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base orthonormale de \( F \) , on a donc \( d{\left( x, F\right) }^{2} = \parallel x{\parallel }^{2} - \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {\lambda }_{i}\right| }^{2} \) , où \( {\lambda }_{i} = {e}_{i} \cdot x \) .

> Remark 7. Since \( x - p\left( x\right) \) is orthogonal to \( p\left( x\right) \), the relation \( x = \left( {x - p\left( x\right) }\right) + p\left( x\right) \) implies \( \parallel x{\parallel }^{2} = \parallel x - p\left( x\right) {\parallel }^{2} + \parallel p\left( x\right) {\parallel }^{2} \), therefore \( d{\left( x, F\right) }^{2} = \parallel x{\parallel }^{2} - \parallel p\left( x\right) {\parallel }^{2} \). If \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is an orthonormal basis of \( F \), we then have \( d{\left( x, F\right) }^{2} = \parallel x{\parallel }^{2} - \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {\lambda }_{i}\right| }^{2} \), where \( {\lambda }_{i} = {e}_{i} \cdot x \).
