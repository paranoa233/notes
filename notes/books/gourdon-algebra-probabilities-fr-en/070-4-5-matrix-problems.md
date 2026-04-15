#### 4.5. Matrix problems

*Français : 4.5. Problèmes matriciels*

Applications transposées. Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v de dimension finie, soit \( p = \dim E \) et \( q = \dim F \) . Soit \( u \in \mathcal{L}\left( {E, F}\right) , B \) une base de \( E \) et \( {B}^{\prime } \) une base de \( F \) . Soit \( f \in {F}^{ * } \) , \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{q}}\right) = {\left\lbrack f\right\rbrack }_{{B}^{\prime }}^{\mathbb{K}} \) sa matrice dans la base \( {B}^{\prime } \) . Si \( g = f \circ u \) et \( \left( {{\beta }_{1},\ldots ,{\beta }_{p}}\right) = {\left\lbrack g\right\rbrack }_{B}^{\mathbb{K}} \) , on a

> Transposed maps. Let \( E \) and \( F \) be two finite-dimensional \( \mathbb{K} \) -vector spaces, let \( p = \dim E \) and \( q = \dim F \) . Let \( u \in \mathcal{L}\left( {E, F}\right) , B \) be a basis of \( E \) and \( {B}^{\prime } \) a basis of \( F \) . Let \( f \in {F}^{ * } \) , \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{q}}\right) = {\left\lbrack f\right\rbrack }_{{B}^{\prime }}^{\mathbb{K}} \) be its matrix in the basis \( {B}^{\prime } \) . If \( g = f \circ u \) and \( \left( {{\beta }_{1},\ldots ,{\beta }_{p}}\right) = {\left\lbrack g\right\rbrack }_{B}^{\mathbb{K}} \) , we have

\[
\left( {{\beta }_{1},\ldots ,{\beta }_{p}}\right)  = \left( {{\alpha }_{1},\ldots ,{\alpha }_{q}}\right) {\left\lbrack  u\right\rbrack  }_{B}^{{B}^{\prime }}
\]

donc en transposant ces matrices,

> so by transposing these matrices,

\[
\left( \begin{matrix} {\beta }_{1} \\  \vdots \\  {\beta }_{p} \end{matrix}\right)  = {}^{\mathrm{t}}{\left\lbrack  u\right\rbrack  }_{B}^{{B}^{\prime }}\left( \begin{matrix} {\alpha }_{1} \\  \vdots \\  {\alpha }_{q} \end{matrix}\right) .
\]

De la définition d'une application transposée, on vérifie facilement que ceci équivaut à dire \( {\left\lbrack \begin{matrix} {}^{\mathrm{t}}u \end{matrix}\right\rbrack }_{{B}^{ * }}^{{B}^{\prime * }} = {}^{\mathrm{t}}{\left\lbrack u\right\rbrack }_{B}^{{B}^{\prime }} \) , où \( {B}^{ * } \) et \( {B}^{\prime * } \) sont les bases duales de \( B \) et \( {B}^{\prime } \) . En d’autres termes, la matrice dans les bases duales de \( B \) et \( {B}^{\prime } \) de \( {}^{t}u \) est la transposée de la matrice de \( u \) dans les bases \( B \) et \( {B}^{\prime } \) .

> From the definition of a transposed map, it is easily verified that this is equivalent to saying \( {\left\lbrack \begin{matrix} {}^{\mathrm{t}}u \end{matrix}\right\rbrack }_{{B}^{ * }}^{{B}^{\prime * }} = {}^{\mathrm{t}}{\left\lbrack u\right\rbrack }_{B}^{{B}^{\prime }} \) , where \( {B}^{ * } \) and \( {B}^{\prime * } \) are the dual bases of \( B \) and \( {B}^{\prime } \) . In other words, the matrix of \( {}^{t}u \) in the dual bases of \( B \) and \( {B}^{\prime } \) is the transpose of the matrix of \( u \) in the bases \( B \) and \( {B}^{\prime } \) .

On déduit de ce résultat que \( {\mathrm{{rg}}}^{\mathrm{t}}u = \mathrm{{rg}}u \) , résultat annoncé dans la proposition 6 .

> We deduce from this result that \( {\mathrm{{rg}}}^{\mathrm{t}}u = \mathrm{{rg}}u \) , a result announced in proposition 6 .

Changement de base dans le dual. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \) . Soit \( B = \; \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E,{B}^{ * } = \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) sa base duale. On se pose le problème suivant : quelle est dans la base \( {B}^{ * } \) les coordonnées de la base duale \( {B}^{\prime * } \) d’une nouvelle base \( {B}^{\prime } = \left( {{\varepsilon }_{1},\ldots ,{\varepsilon }_{n}}\right) \) de \( E \) ?

> Change of basis in the dual. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space \( n \) . Let \( B = \; \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E,{B}^{ * } = \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) its dual basis. We pose the following problem: what are the coordinates in the basis \( {B}^{ * } \) of the dual basis \( {B}^{\prime * } \) of a new basis \( {B}^{\prime } = \left( {{\varepsilon }_{1},\ldots ,{\varepsilon }_{n}}\right) \) of \( E \) ?

Soit \( C \) la matrice de passage de la base \( B \) à la base \( {B}^{\prime } \) . Soit \( f \in {E}^{ * },\left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) sa matrice dans la base \( {B}^{ * },\left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) \) sa matrice dans la base \( {B}^{\prime * } \) . Soit \( x \in E, X \) sa matrice (colonne) dans la base \( B, Y \) sa matrice dans la base \( {B}^{\prime } \) . On a \( X = {CY} \) , et

> Let \( C \) be the transition matrix from basis \( B \) to basis \( {B}^{\prime } \) . Let \( f \in {E}^{ * },\left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) be its matrix in basis \( {B}^{ * },\left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) \) its matrix in basis \( {B}^{\prime * } \) . Let \( x \in E, X \) be its (column) matrix in basis \( B, Y \) its matrix in basis \( {B}^{\prime } \) . We have \( X = {CY} \) , and

\[
f\left( x\right)  = \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) X = \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) Y\;\text{ donc }\;\left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) {CY} = \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) Y,
\]

et ceci pour tout \( Y \) donc \( \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) = \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) C \) . En d’autres termes,

> and this for all \( Y \) therefore \( \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) = \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) C \) . In other words,

\[
\left( \begin{matrix} {\beta }_{1} \\  \vdots \\  {\beta }_{n} \end{matrix}\right)  = {}^{\mathrm{t}}C\left( \begin{matrix} {\alpha }_{1} \\  \vdots \\  {\alpha }_{n} \end{matrix}\right) \;\text{ ou encore }\left( \begin{matrix} {\alpha }_{1} \\  \vdots \\  {\alpha }_{n} \end{matrix}\right)  = {\left( {}^{\mathrm{t}}C\right) }^{-1}\left( \begin{matrix} {\beta }_{1} \\  \vdots \\  {\beta }_{n} \end{matrix}\right) .
\]

La matrice de passage de \( {B}^{ * } \) à \( {B}^{\prime * } \) est donc \( {}^{t}{C}^{-1} \) où \( C \) est la matrice de passage de \( B \) à \( {B}^{\prime } \) .

> The transition matrix from \( {B}^{ * } \) to \( {B}^{\prime * } \) is therefore \( {}^{t}{C}^{-1} \) where \( C \) is the transition matrix from \( B \) to \( {B}^{\prime } \) .
