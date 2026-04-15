#### 3.4. Change of basis

*Français : 3.4. Changement de base*

Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * }, B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) et \( {B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n}^{\prime }}\right) \) deux bases de \( E \) . Pour tout \( j,1 \leq j \leq n \) , on peut écrire \( {e}_{j}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i, j}{e}_{i} \) avec les \( {p}_{i, j} \in \mathbb{K} \) . La matrice \( P = {\left( {p}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq n} \\ {1 \leq j \leq n} \end{matrix}} \) (dont les colonnes sont les coordonnées des vecteurs de \( {B}^{\prime } \) dans la base \( B \) ) s’appelle matrice de passage de \( B \) à \( {B}^{\prime } \) . La matrice \( P \) est inversible. Si \( x \in E \) , si \( X \) (resp. \( {X}^{\prime } \) ) désigne le vecteur colonne dont les éléments sont les coordonnées de \( x \) dans la base \( B \) (resp. dans la base \( {B}^{\prime } \) ), alors on a \( X = P{X}^{\prime } \) .

> Let \( E \) be a \( \mathbb{K} \) -v.s. of finite dimension \( n \in {\mathbb{N}}^{ * }, B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) and \( {B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n}^{\prime }}\right) \) two bases of \( E \) . For any \( j,1 \leq j \leq n \) , we can write \( {e}_{j}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i, j}{e}_{i} \) with the \( {p}_{i, j} \in \mathbb{K} \) . The matrix \( P = {\left( {p}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq n} \\ {1 \leq j \leq n} \end{matrix}} \) (whose columns are the coordinates of the vectors of \( {B}^{\prime } \) in the basis \( B \) ) is called the transition matrix from \( B \) to \( {B}^{\prime } \) . The matrix \( P \) is invertible. If \( x \in E \) , if \( X \) (resp. \( {X}^{\prime } \) ) denotes the column vector whose elements are the coordinates of \( x \) in the basis \( B \) (resp. in the basis \( {B}^{\prime } \) ), then we have \( X = P{X}^{\prime } \) .

Remarque 4. Attention à l’erreur courante qui consisterait à écrire \( {X}^{\prime } = {PX} \) .

> Remark 4. Beware of the common error that would consist of writing \( {X}^{\prime } = {PX} \) .

PROPOSITION 3. Soient E et \( F \) deux \( \mathbb{K} \) -e.v de dimensions finies respectivement égales à p et q. Soient \( {B}_{0} \) et \( {B}_{0}^{\prime } \) deux bases de \( E, P \) la matrice de passage de \( {B}_{0} \) à \( {B}_{0}^{\prime },{B}_{1} \) et \( {B}_{1}^{\prime } \) deux bases de \( F, Q \) la matrice de passage de \( {B}_{1} \) à \( {B}_{1}^{\prime } \) . Soit \( f \in \mathcal{L}\left( {E, F}\right) \) . Si \( A = {\left\lbrack f\right\rbrack }_{{B}_{0}}^{{B}_{1}} \) , \( {A}^{\prime } = {\left\lbrack f\right\rbrack }_{{B}_{0}^{\prime }}^{{B}_{1}^{\prime }} \) , on a \( {A}^{\prime } = {Q}^{-1}{AP} \) .

> PROPOSITION 3. Let E and \( F \) be two finite-dimensional \( \mathbb{K} \) -vector spaces of dimensions p and q, respectively. Let \( {B}_{0} \) and \( {B}_{0}^{\prime } \) be two bases of \( E, P \) the transition matrix from \( {B}_{0} \) to \( {B}_{0}^{\prime },{B}_{1} \) and \( {B}_{1}^{\prime } \) two bases of \( F, Q \) the transition matrix from \( {B}_{1} \) to \( {B}_{1}^{\prime } \) . Let \( f \in \mathcal{L}\left( {E, F}\right) \) . If \( A = {\left\lbrack f\right\rbrack }_{{B}_{0}}^{{B}_{1}} \) , \( {A}^{\prime } = {\left\lbrack f\right\rbrack }_{{B}_{0}^{\prime }}^{{B}_{1}^{\prime }} \) , then \( {A}^{\prime } = {Q}^{-1}{AP} \) .

DÉFINITION 6. Soient \( A, B \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . On dit que \( A \) et \( B \) sont équivalentes s’il existe \( P \in \mathcal{G}{\ell }_{q}\left( \mathbb{K}\right) \) et \( Q \in \mathcal{G}{\ell }_{p}\left( \mathbb{K}\right) \) telles que \( B = {QAP} \) . La relation "est équivalente à" est une relation d'équivalence.

> DEFINITION 6. Let \( A, B \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . We say that \( A \) and \( B \) are equivalent if there exist \( P \in \mathcal{G}{\ell }_{q}\left( \mathbb{K}\right) \) and \( Q \in \mathcal{G}{\ell }_{p}\left( \mathbb{K}\right) \) such that \( B = {QAP} \) . The relation "is equivalent to" is an equivalence relation.

Remarque 5. On a vu un peu plus haut que les matrices d'une même application \( f \in \; \mathcal{L}\left( {E, F}\right) \) dans des bases différentes sont équivalentes.

> Remark 5. We saw earlier that the matrices of the same map \( f \in \; \mathcal{L}\left( {E, F}\right) \) in different bases are equivalent.

PROPOSITION 4. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) , \( B \) et \( {B}^{\prime } \) deux bases de \( E \) , \( P \) la matrice de passage de \( B \) à \( {B}^{\prime } \) . Soit \( f \in \mathcal{L}\left( E\right) \) . Si \( A = {\left\lbrack f\right\rbrack }_{B} \) et \( {A}^{\prime } = {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) , alors \( {A}^{\prime } = {P}^{-1}{AP}. \)

> PROPOSITION 4. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space of dimension \( n \in {\mathbb{N}}^{ * } \) , \( B \) and \( {B}^{\prime } \) two bases of \( E \) , \( P \) the transition matrix from \( B \) to \( {B}^{\prime } \) . Let \( f \in \mathcal{L}\left( E\right) \) . If \( A = {\left\lbrack f\right\rbrack }_{B} \) and \( {A}^{\prime } = {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) , then \( {A}^{\prime } = {P}^{-1}{AP}. \)

DéFINITION 7. Deux matrices \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) sont dites semblables s’il existe \( P \in \; \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) tel que \( B = {P}^{-1}{AP} \) . La relation de similitude est une relation d’équivalence.

> DEFINITION 7. Two matrices \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) are said to be similar if there exists \( P \in \; \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) such that \( B = {P}^{-1}{AP} \) . The similarity relation is an equivalence relation.
