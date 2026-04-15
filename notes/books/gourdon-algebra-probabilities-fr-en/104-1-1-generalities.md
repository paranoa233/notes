#### 1.1. Generalities

*Français : 1.1. Généralités*

On définit d'abord les formes bilinéaires.

> We first define bilinear forms.

Définition 1 (Forme bilinéaire). Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v et une application

> Definition 1 (Bilinear form). Let \( E \) and \( F \) be two \( \mathbb{K} \) -vector spaces and a mapping

\[
\varphi  : E \times  F \rightarrow  \mathbb{K}\;\left( {x, y}\right)  \mapsto  \varphi \left( {x, y}\right) .
\]

On dit que \( \varphi \) est une forme bilinéaire si pour tout \( x \in E \) , l’application \( \varphi \left( {x, \cdot }\right) : y \mapsto \varphi \left( {x, y}\right) \) est linéaire et si pour tout \( y \in F \) , l’application \( \varphi \left( {\cdot , y}\right) : x \mapsto \varphi \left( {x, y}\right) \) est linéaire.

> We say that \( \varphi \) is a bilinear form if for all \( x \in E \) , the mapping \( \varphi \left( {x, \cdot }\right) : y \mapsto \varphi \left( {x, y}\right) \) is linear and if for all \( y \in F \) , the mapping \( \varphi \left( {\cdot , y}\right) : x \mapsto \varphi \left( {x, y}\right) \) is linear.

Les formes sesquilinéaires sont définies lorsque le corps de base est \( \mathbb{C} \) .

> Sesquilinear forms are defined when the base field is \( \mathbb{C} \) .

DéFINITION 2 (Forme sesquilinéaire). Soient \( E \) et \( F \) deux \( \mathbb{C} \) -e.v et une application

> DEFINITION 2 (Sesquilinear form). Let \( E \) and \( F \) be two \( \mathbb{C} \) -vector spaces and a mapping

\[
\varphi  : E \times  F \rightarrow  \mathbb{C}\;\left( {x, y}\right)  \mapsto  \varphi \left( {x, y}\right) .
\]

On dit que \( \varphi \) est une forme sesquilinéaire si pour tout \( x \in E \) , l’application \( \varphi \left( {x, \cdot }\right) \) est linéaire et si pour tout \( y \in F \) , l’application \( \varphi \left( {\cdot , y}\right) \) est antilinéaire (i.e. pour tout \( {x}_{1},{x}_{2} \in \; E,\varphi \left( {{x}_{1} + {x}_{2}, y}\right) = \varphi \left( {{x}_{1}, y}\right) + \varphi \left( {{x}_{2}, y}\right) \) et pour tout \( \lambda \in \mathbb{C} \) , pour tout \( x \in E,\varphi \left( {{\lambda x}, y}\right) = \; \left. {\overline{\lambda }\varphi \left( {x, y}\right) }\right) \) .

> We say that \( \varphi \) is a sesquilinear form if for all \( x \in E \) , the mapping \( \varphi \left( {x, \cdot }\right) \) is linear and if for all \( y \in F \) , the mapping \( \varphi \left( {\cdot , y}\right) \) is antilinear (i.e. for all \( {x}_{1},{x}_{2} \in \; E,\varphi \left( {{x}_{1} + {x}_{2}, y}\right) = \varphi \left( {{x}_{1}, y}\right) + \varphi \left( {{x}_{2}, y}\right) \) and for all \( \lambda \in \mathbb{C} \) , for all \( x \in E,\varphi \left( {{\lambda x}, y}\right) = \; \left. {\overline{\lambda }\varphi \left( {x, y}\right) }\right) \) .

Remarque 1. - Dans toute la suite, les espaces \( E \) et \( F \) seront les mêmes.

> Remark 1. - Throughout the following, the spaces \( E \) and \( F \) will be the same.

- Toute forme sesquilinéaire sur \( E \times  F \) est une forme bilinéaire lorsque les e.v \( E \) et \( F \) sont considérés comme des \( \mathbb{R} \) -e.v.

> - Any sesquilinear form on \( E \times  F \) is a bilinear form when the vector spaces \( E \) and \( F \) are considered as \( \mathbb{R} \) -vector spaces.

Exemple 1. Si \( E \) désigne le \( \mathbb{C} \) -e.v des fonctions continues de \( \left\lbrack {0,1}\right\rbrack \) dans \( \mathbb{C} \) , l’application

> Example 1. If \( E \) denotes the \( \mathbb{C} \) -vector space of continuous functions from \( \left\lbrack {0,1}\right\rbrack \) to \( \mathbb{C} \) , the mapping

\[
\varphi  : {E}^{2} \rightarrow  \mathbb{C}\;\left( {f, g}\right)  \mapsto  {\int }_{0}^{1}\overline{f\left( t\right) }g\left( t\right) {dt}
\]

définit une forme sesquilinéaire sur \( {E}^{2} \) .

> defines a sesquilinear form on \( {E}^{2} \) .

Dans toute la suite de cette section, \( E \) désigne un \( \mathbb{K} \) -e.v

> Throughout the remainder of this section, \( E \) denotes a \( \mathbb{K} \) -vector space

Écriture en dimension finie. Supposons \( E \) de dimension finie \( n \) et fixons une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . Alors pour tout \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) et \( y = \mathop{\sum }\limits_{{j = 1}}^{n}{y}_{j}{e}_{j} \) dans \( E \) , la bilinéarité de \( \varphi \) entraîne

> Representation in finite dimension. Suppose \( E \) is of finite dimension \( n \) and fix a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . Then for any \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) and \( y = \mathop{\sum }\limits_{{j = 1}}^{n}{y}_{j}{e}_{j} \) in \( E \) , the bilinearity of \( \varphi \) implies

\[
\varphi \left( {x, y}\right)  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}{x}_{i}{y}_{j}\varphi \left( {{e}_{i},{e}_{j}}\right)  = {}^{\mathrm{t}}{XMY}
\]

où \( M \) est la matrice de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) définie par \( M = {\left( \varphi \left( {e}_{i},{e}_{j}\right) \right) }_{1 \leq i, j \leq n} \) et où \( X \) et \( Y \) sont les vecteurs colonne \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) , Y = \left( \begin{matrix} {y}_{1} \\ \vdots \\ {y}_{n} \end{matrix}\right) \) . La matrice \( M \) est appelée matrice de \( \varphi \) dans la base \( B \) .

> where \( M \) is the matrix of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) defined by \( M = {\left( \varphi \left( {e}_{i},{e}_{j}\right) \right) }_{1 \leq i, j \leq n} \) and where \( X \) and \( Y \) are the column vectors \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) , Y = \left( \begin{matrix} {y}_{1} \\ \vdots \\ {y}_{n} \end{matrix}\right) \) . The matrix \( M \) is called the matrix of \( \varphi \) in the basis \( B \) .

Avec les mêmes notations, si \( E \) est un \( \mathbb{C} \) -e.v et \( \varphi \) une forme sesquilinéaire sur \( E \) , on a

> With the same notation, if \( E \) is a \( \mathbb{C} \) -vector space and \( \varphi \) is a sesquilinear form on \( E \) , we have

\[
\varphi \left( {x, y}\right)  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}\overline{{x}_{i}}{y}_{j}\varphi \left( {{e}_{i},{e}_{j}}\right)  = {}^{\mathrm{t}}\bar{X}{MY},
\]

où \( \bar{X} \) désigne le vecteur conjugué de \( X \) (i.e les composantes de \( \bar{X} \) sont les conjuguées de celles de \( X \) ). On dit que \( M \) est la matrice de \( \varphi \) dans la base \( B \) .

> where \( \bar{X} \) denotes the conjugate vector of \( X \) (i.e., the components of \( \bar{X} \) are the conjugates of those of \( X \) ). We say that \( M \) is the matrix of \( \varphi \) in the basis \( B \) .

L’application qui à \( \varphi \) associe sa matrice dans une base fixée de \( E \) est un isomorphisme. En particulier, l’ensemble des formes bilinéaires (ou sesquilinéaires) sur \( E \) est un \( \mathbb{K} \) -espace vectoriel de dimension \( {n}^{2} \) (où \( n = \dim E \) ).

> The mapping that associates to \( \varphi \) its matrix in a fixed basis of \( E \) is an isomorphism. In particular, the set of bilinear (or sesquilinear) forms on \( E \) is a \( \mathbb{K} \) -vector space of dimension \( {n}^{2} \) (where \( n = \dim E \) ).

Lorsque \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{K} = \mathbb{C} \) , l’écriture précédente entraîne qu’en dimension finie, les formes quadratiques et sesquilinéaires (pour \( \mathbb{K} = \mathbb{C} \) ) sont des fonctions continues.

> When \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{K} = \mathbb{C} \) , the previous expression implies that in finite dimension, quadratic and sesquilinear forms (for \( \mathbb{K} = \mathbb{C} \) ) are continuous functions.

Changement de base. On suppose toujours que \( E \) est de dimension finie. Soient \( B \) et \( {B}^{\prime } \) deux bases de \( E, P \) la matrice de passage de \( B \) à \( {B}^{\prime } \) . Si \( \varphi \) est une forme bilinéaire (resp. sesquilinéaire) sur \( E \) , et si \( M \) désigne sa matrice dans la base \( B,{M}^{\prime } \) dans la base \( {B}^{\prime } \) , alors

> Change of basis. We still assume that \( E \) is of finite dimension. Let \( B \) and \( {B}^{\prime } \) be two bases of \( E, P \) the transition matrix from \( B \) to \( {B}^{\prime } \) . If \( \varphi \) is a bilinear (resp. sesquilinear) form on \( E \) , and if \( M \) denotes its matrix in the basis \( B,{M}^{\prime } \) in the basis \( {B}^{\prime } \) , then

\[
{M}^{\prime } = {}^{\mathrm{t}}{PMP}\;\text{ (resp. }{M}^{\prime } = {}^{\mathrm{t}}\bar{P}{MP}\text{ ). }
\]

On dit que les matrices \( M \) et \( {M}^{\prime } \) sont congrues. Les matrices \( M \) et \( {M}^{\prime } \) sont alors équi-valentes, donc de même rang. Ce rang s’appelle le rang de \( \varphi \) . Le rang de \( \varphi \) est aussi la dimension du s.e.v des formes linéaires \( \{ \varphi \left( {x, \cdot }\right) \mid x \in E\} \) dans le dual de \( E \) .

> The matrices \( M \) and \( {M}^{\prime } \) are said to be congruent. The matrices \( M \) and \( {M}^{\prime } \) are then equivalent, and therefore have the same rank. This rank is called the rank of \( \varphi \). The rank of \( \varphi \) is also the dimension of the subspace of linear forms \( \{ \varphi \left( {x, \cdot }\right) \mid x \in E\} \) in the dual of \( E \).

##### Symmetries in bilinear and sesquilinear forms.

*Français : Symétries dans les formes bilinéaires et sesquilinéaires.*

DéFINITION 3. Soit \( \varphi \) une forme bilinéaire sur \( E \) . On dit que

> DEFINITION 3. Let \( \varphi \) be a bilinear form on \( E \). We say that

- \( \varphi \) est symétrique si pour tout \( \left( {x, y}\right)  \in  {E}^{2},\varphi \left( {x, y}\right)  = \varphi \left( {y, x}\right) \) ,

> - \( \varphi \) is symmetric if for all \( \left( {x, y}\right)  \in  {E}^{2},\varphi \left( {x, y}\right)  = \varphi \left( {y, x}\right) \),

- \( \varphi \) est antisymétrique si pour tout \( \left( {x, y}\right)  \in  {E}^{2},\varphi \left( {x, y}\right)  =  - \varphi \left( {y, x}\right) \) .

> - \( \varphi \) is antisymmetric if for all \( \left( {x, y}\right)  \in  {E}^{2},\varphi \left( {x, y}\right)  =  - \varphi \left( {y, x}\right) \).

Remarque 2. - Si K est de caractéristique 2, l'antisymétrie équivaut à la symétrie.

> Remark 2. - If K is of characteristic 2, antisymmetry is equivalent to symmetry.

- Si \( E \) est de dimension finie et si \( B \) est une base de \( E \) , une forme bilinéaire \( \varphi \) sur \( E \) est symétrique (resp. antisymétrique) si et seulement si sa matrice dans la base \( B \) est symétrique (resp. antisymétrique).

> - If \( E \) is of finite dimension and if \( B \) is a basis of \( E \), a bilinear form \( \varphi \) on \( E \) is symmetric (resp. antisymmetric) if and only if its matrix in the basis \( B \) is symmetric (resp. antisymmetric).

- Si la caractéristique de \( \mathbb{K} \) est différente de 2, une forme bilinéaire \( \varphi \) est antisymé- trique si et seulement si \( \varphi \left( {x, x}\right)  = 0 \) pour tout \( x \in  E \) (cas particulier du théorème 1 page 141 dans le cas bilinéaire).

> - If the characteristic of \( \mathbb{K} \) is different from 2, a bilinear form \( \varphi \) is antisymmetric if and only if \( \varphi \left( {x, x}\right)  = 0 \) for all \( x \in  E \) (special case of theorem 1 on page 141 in the bilinear case).

- Si la caractéristique de \( \mathbb{K} \) est différente de 2, si on désigne par \( {\mathcal{S}}_{n} \) (resp. \( {\mathcal{A}}_{n} \) ) le s.e.v des matrices symétriques (resp. antisymétriques) de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on a \( {\mathcal{S}}_{n} \oplus  {\mathcal{A}}_{n} = \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . En effet,

> - If the characteristic of \( \mathbb{K} \) is different from 2, if we denote by \( {\mathcal{S}}_{n} \) (resp. \( {\mathcal{A}}_{n} \)) the subspace of symmetric (resp. antisymmetric) matrices of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), we have \( {\mathcal{S}}_{n} \oplus  {\mathcal{A}}_{n} = \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). Indeed,

\[
{\mathcal{S}}_{n} \cap  {\mathcal{A}}_{n} = \{ 0\} \;\operatorname{car}\text{ si }\;A = {}^{\mathrm{t}}A =  - {}^{\mathrm{t}}A,\;\text{ alors }\;{}^{\mathrm{t}}A = 0\text{ donc }A = 0\text{ . }
\]

\[
{\mathcal{S}}_{n} + {\mathcal{A}}_{n} = {\mathcal{M}}_{n}\left( \mathbb{K}\right) \;\text{ car }\;\forall A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\;A = \underset{ \in  {\mathcal{S}}_{n}}{\underbrace{\frac{1}{2}\left( {A + {}^{\mathrm{t}}A}\right) }} + \underset{ \in  {\mathcal{A}}_{n}}{\underbrace{\frac{1}{2}\left( {A - {}^{\mathrm{t}}A}\right) }}.
\]

De plus, \( \dim {\mathcal{S}}_{n} = n\left( {n + 1}\right) /2 \) et \( \dim {\mathcal{A}}_{n} = n\left( {n - 1}\right) /2 \) (si \( {E}_{i, j} \) désigne la matrice dont tous les coefficients sont nuls sauf celui d'indice \( \left( {i, j}\right) \) qui vaut 1, la famille \( \left( {{\left( {E}_{i, i}\right) }_{1 \leq i \leq n},{\left( {E}_{i, j} + {E}_{j, i}\right) }_{1 \leq i < j \leq n}}\right) \) est une base de \( {\mathcal{S}}_{n} \) , la famille \( {\left( {E}_{i, j} - {E}_{j, i}\right) }_{1 \leq i < j \leq n} \) est une base de \( {\mathcal{A}}_{n} \) ).

> Furthermore, \( \dim {\mathcal{S}}_{n} = n\left( {n + 1}\right) /2 \) and \( \dim {\mathcal{A}}_{n} = n\left( {n - 1}\right) /2 \) (if \( {E}_{i, j} \) denotes the matrix whose coefficients are all zero except for the one with index \( \left( {i, j}\right) \) which is 1, the family \( \left( {{\left( {E}_{i, i}\right) }_{1 \leq i \leq n},{\left( {E}_{i, j} + {E}_{j, i}\right) }_{1 \leq i < j \leq n}}\right) \) is a basis of \( {\mathcal{S}}_{n} \), the family \( {\left( {E}_{i, j} - {E}_{j, i}\right) }_{1 \leq i < j \leq n} \) is a basis of \( {\mathcal{A}}_{n} \)).

— En conséquence, si la caractéristique de \( \mathbb{K} \) est différente de 2, l’ensemble \( \mathcal{S} \) (resp. \( \mathcal{A} \) ) des formes bilinéaires symétriques (resp. antisymétriques) sur \( E \) (avec dim \( E = n \) ) est un \( \mathbb{K} \) -e.v de dimension \( n\left( {n + 1}\right) /2 \) (resp. \( n\left( {n - 1}\right) /2 \) ). De plus, si \( \mathcal{B} \) désigne le \( \mathbb{K} \) -e.v des formes bilinéaires sur \( E \) , on a \( \mathcal{S} \oplus \mathcal{A} = \mathcal{B} \) .

> — Consequently, if the characteristic of \( \mathbb{K} \) is not 2, the set \( \mathcal{S} \) (resp. \( \mathcal{A} \) ) of symmetric (resp. antisymmetric) bilinear forms on \( E \) (with dim \( E = n \) ) is a \( \mathbb{K} \) -v.s. of dimension \( n\left( {n + 1}\right) /2 \) (resp. \( n\left( {n - 1}\right) /2 \) ). Furthermore, if \( \mathcal{B} \) denotes the \( \mathbb{K} \) -v.s. of bilinear forms on \( E \) , we have \( \mathcal{S} \oplus \mathcal{A} = \mathcal{B} \) .

DÉFINITION 4. Soit \( \varphi \) une forme sesquilinéaire sur un \( \mathbb{C} \) -e.v \( E \) . On dit que \( \varphi \) est à symétrie hermitienne si pour tout \( \left( {x, y}\right) \in {E}^{2},\varphi \left( {x, y}\right) = \overline{\varphi \left( {y, x}\right) } \) .

> DEFINITION 4. Let \( \varphi \) be a sesquilinear form on a \( \mathbb{C} \) -v.s. \( E \) . We say that \( \varphi \) is Hermitian symmetric if for all \( \left( {x, y}\right) \in {E}^{2},\varphi \left( {x, y}\right) = \overline{\varphi \left( {y, x}\right) } \) .

Remarque 3. - Si \( \varphi \) est à symétrie hermitienne, alors pour tout \( x \in E,\varphi \left( {x, x}\right) \in \mathbb{R} \) (ceci car \( \varphi \left( {x, x}\right) = \overline{\varphi \left( {x, x}\right) } \) ).

> Remark 3. - If \( \varphi \) is Hermitian symmetric, then for all \( x \in E,\varphi \left( {x, x}\right) \in \mathbb{R} \) (this is because \( \varphi \left( {x, x}\right) = \overline{\varphi \left( {x, x}\right) } \) ).

- Si \( E \) est de dimension finie sur \( \mathbb{C} \) et si \( B \) est une base de \( E \) , alors une forme sesquilinéaire \( \varphi \) sur \( E \) est à symétrie hermitienne si et seulement si sa matrice \( M \) dans la base \( B \) vérifie \( {}^{\mathrm{t}}\bar{M} = M \) . On dit alors que \( M \) est une matrice hermitienne. Toute matrice hermitienne \( M \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) peut s’écrire de manière unique sous la forme \( M = S + {iA} \) , où \( S, A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) avec \( S \) symétrique et \( A \) antisymétrique. L’ensemble des matrices hermitiennes de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) forme un \( \mathbb{R} \) -e.v de dimension \( {n}^{2} \) (mais attention, ce n'est pas un C-e.v).

> - If \( E \) is finite-dimensional over \( \mathbb{C} \) and if \( B \) is a basis of \( E \) , then a sesquilinear form \( \varphi \) on \( E \) is Hermitian symmetric if and only if its matrix \( M \) in the basis \( B \) satisfies \( {}^{\mathrm{t}}\bar{M} = M \) . We then say that \( M \) is a Hermitian matrix. Any Hermitian matrix \( M \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) can be uniquely written in the form \( M = S + {iA} \) , where \( S, A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) with \( S \) symmetric and \( A \) antisymmetric. The set of Hermitian matrices of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) forms a \( \mathbb{R} \) -v.s. of dimension \( {n}^{2} \) (but note, it is not a C-v.s.).

Formes quadratiques. On suppose ici que la caractéristique de \( \mathbb{K} \) est différente de 2.

> Quadratic forms. We assume here that the characteristic of \( \mathbb{K} \) is not 2.

DÉFINITION 5. On appelle forme quadratique sur \( E \) toute application \( q \) de la forme

> DEFINITION 5. A quadratic form on \( E \) is any map \( q \) of the form

\[
q : E \rightarrow  \mathbb{K}\;x \mapsto  \varphi \left( {x, x}\right)
\]

où \( \varphi \) est une forme bilinéaire symétrique sur \( E \) .

> where \( \varphi \) is a symmetric bilinear form on \( E \) .

PROPOSITION 1. Soit q une forme quadratique sur E. Il existe une unique forme bilinéaire symétrique \( \varphi \) telle que pour tout \( x \in E, q\left( x\right) = \varphi \left( {x, x}\right) \) . La forme bilinéaire \( \varphi \) s’appelle la forme polaire de \( q \) et on a

> PROPOSITION 1. Let q be a quadratic form on E. There exists a unique symmetric bilinear form \( \varphi \) such that for all \( x \in E, q\left( x\right) = \varphi \left( {x, x}\right) \) . The bilinear form \( \varphi \) is called the polar form of \( q \) and we have

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\varphi \left( {x, y}\right)  = \frac{1}{2}\left\lbrack  {q\left( {x + y}\right)  - q\left( x\right)  - q\left( y\right) }\right\rbrack   = \frac{1}{4}\left\lbrack  {q\left( {x + y}\right)  - q\left( {x - y}\right) }\right\rbrack  .
\]

Exemple 2. - Si \( \varphi \left( {x, y}\right) = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{x}_{i}{y}_{j} \) , la forme quadratique associée à \( \varphi \) est

> Example 2. - If \( \varphi \left( {x, y}\right) = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{x}_{i}{y}_{j} \) , the quadratic form associated with \( \varphi \) is

\[
q\left( x\right)  = \mathop{\sum }\limits_{i}{a}_{i, i}{x}_{i}^{2} + \mathop{\sum }\limits_{{i < j}}\left( {{a}_{i, j} + {a}_{j, i}}\right) {x}_{i}{x}_{j}.
\]

- Réciproquement, si \( q\left( x\right)  = \mathop{\sum }\limits_{i}{a}_{i, i}{x}_{i}^{2} + \mathop{\sum }\limits_{{i < j}}{a}_{i, j}{x}_{i}{x}_{j} \) , alors \( q \) est une forme quadra-tique et sa forme polaire est

> - Conversely, if \( q\left( x\right)  = \mathop{\sum }\limits_{i}{a}_{i, i}{x}_{i}^{2} + \mathop{\sum }\limits_{{i < j}}{a}_{i, j}{x}_{i}{x}_{j} \) , then \( q \) is a quadratic form and its polar form is

\[
\varphi \left( {x, y}\right)  = \mathop{\sum }\limits_{i}{a}_{i, i}{x}_{i}{y}_{i} + \frac{1}{2}\mathop{\sum }\limits_{{i < j}}{a}_{i, j}\left( {{x}_{i}{y}_{j} + {x}_{j}{y}_{i}}\right) .
\]

DÉFINITION 6. Soit \( q \) une forme quadratique sur \( E \) , où \( E \) est de dimension finie, et \( B \) une base de \( E \) . On appelle matrice de \( q \) dans la base \( B \) la matrice de la forme polaire \( \varphi \) de \( q \) dans la base \( B \) , et rang de \( q \) le rang de cette matrice. Le rang de \( q \) est aussi le rang de sa forme polaire.

> DEFINITION 6. Let \( q \) be a quadratic form on \( E \) , where \( E \) is finite-dimensional, and \( B \) be a basis of \( E \) . The matrix of \( q \) in the basis \( B \) is defined as the matrix of the polar form \( \varphi \) of \( q \) in the basis \( B \) , and the rank of \( q \) as the rank of this matrix. The rank of \( q \) is also the rank of its polar form.

Exemple 3. On se place dans \( {\mathbb{R}}^{3} \) et on y définit la forme quadratique \( q \) par

> Example 3. We work in \( {\mathbb{R}}^{3} \) and define the quadratic form \( q \) by

\[
u = \left( {x, y, z}\right)  \mapsto  q\left( u\right)  = 3{x}^{2} + {y}^{2} + {2xy} - {3xz}.
\]

Alors la matrice de \( q \) dans la base canonique de \( {\mathbb{R}}^{3} \) est

> Then the matrix of \( q \) in the canonical basis of \( {\mathbb{R}}^{3} \) is

\[
A = \left( \begin{matrix} 3 & 1 &  - \frac{3}{2} \\  1 & 1 & 0 \\   - \frac{3}{2} & 0 & 0 \end{matrix}\right)
\]

Formes hermitiennes.

> Hermitian forms.

DÉFINITION 7. On appelle forme hermitienne sur un \( \mathbb{C} \) -e.v \( E \) toute application de la forme

> DEFINITION 7. A Hermitian form on a \( \mathbb{C} \) -v.s. \( E \) is any mapping of the form

\[
\Phi  : E \rightarrow  \mathbb{R}\;x \mapsto  \varphi \left( {x, x}\right)
\]

où \( \varphi \) est une forme sesquilinéaire à symétrie hermitienne.

> where \( \varphi \) is a sesquilinear form with Hermitian symmetry.

Proposition 2. Soit \( \Phi \) une forme hermitienne. Il existe une unique forme sesquilinéaire à symétrie hermitienne \( \varphi \) telle que pour tout \( x \in E,\Phi \left( x\right) = \varphi \left( {x, x}\right) \) . La forme \( \varphi \) s’appelle la forme polaire \( {de},\theta \) , et on a

> Proposition 2. Let \( \Phi \) be a Hermitian form. There exists a unique sesquilinear form with Hermitian symmetry \( \varphi \) such that for all \( x \in E,\Phi \left( x\right) = \varphi \left( {x, x}\right) \) . The form \( \varphi \) is called the polar form \( {de},\theta \) , and we have

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\varphi \left( {x, y}\right)  = \frac{1}{4}\left\lbrack  {\Phi \left( {x + y}\right)  - \Phi \left( {x - y}\right)  + {i\Phi }\left( {x - {iy}}\right)  - {i\Phi }\left( {x + {iy}}\right) }\right\rbrack  .
\]

DéFINITION 8. Soit \( \Phi \) une forme hermitienne sur un \( \mathbb{C} \) -e.v \( E \) de dimension finie et \( B \) une base de \( E \) . On appelle matrice de \( \Phi \) dans la base \( B \) la matrice de sa forme polaire \( \varphi \) dans \( B \) , et rang de \( \Phi \) le rang de cette matrice. Le rang de \( \Phi \) est aussi le rang de sa forme polaire.

> DEFINITION 8. Let \( \Phi \) be a Hermitian form on a finite-dimensional \( \mathbb{C} \) -v.s. \( E \) and \( B \) be a basis of \( E \) . The matrix of \( \Phi \) in the basis \( B \) is defined as the matrix of its polar form \( \varphi \) in \( B \) , and the rank of \( \Phi \) as the rank of this matrix. The rank of \( \Phi \) is also the rank of its polar form.

Exemple 4. Sur \( {\mathbb{C}}^{2} \) , si \( \Phi : u = \left( {x, y}\right) \mapsto \bar{x}x - 2\bar{y}y + \frac{3}{2}\bar{y}x + \frac{3}{2}y\bar{x} \) , alors \( \Phi \) est une forme hermitienne de forme polaire

> Example 4. On \( {\mathbb{C}}^{2} \) , if \( \Phi : u = \left( {x, y}\right) \mapsto \bar{x}x - 2\bar{y}y + \frac{3}{2}\bar{y}x + \frac{3}{2}y\bar{x} \) , then \( \Phi \) is a Hermitian form with polar form

\[
\varphi \left( {{u}_{1},{u}_{2}}\right)  = \overline{{x}_{1}}{x}_{2} - 2\overline{{y}_{1}}{y}_{2} + \frac{3}{2}\overline{{y}_{1}}{x}_{2} + \frac{3}{2}\overline{{x}_{1}}{y}_{2},
\]

et la matrice de \( \Phi \) dans la base canonique de \( {\mathbb{R}}^{2} \) est \( \left( \begin{matrix} 1 & \frac{3}{2} \\ \frac{3}{2} & - 2 \end{matrix}\right) \) , son rang est 2 .

> and the matrix of \( \Phi \) in the canonical basis of \( {\mathbb{R}}^{2} \) is \( \left( \begin{matrix} 1 & \frac{3}{2} \\ \frac{3}{2} & - 2 \end{matrix}\right) \) , its rank is 2 .
