#### 1.2. Orthogonality

*Français : 1.2. Orthogonalité*

\( E \) désigne toujours un \( \mathbb{K} \) -e.v (ou un \( \mathbb{C} \) -e.v lorsque l’on parle de forme hermitienne). On se fixe une forme quadratique (resp. hermitienne) \( \Phi \) sur \( E \) , de forme polaire \( \varphi \) .

> \( E \) always denotes a \( \mathbb{K} \) -v.s. (or a \( \mathbb{C} \) -v.s. when discussing Hermitian forms). We fix a quadratic (resp. Hermitian) form \( \Phi \) on \( E \) , with polar form \( \varphi \) .

DÉFINITION 9. On appelle cône isotrope de \( \Phi \) l’ensemble \( {C}_{\Phi } = \{ x \in E \mid \Phi \left( x\right) = 0\} \) . On dit que \( \Phi \) est définie si \( {C}_{\Phi } = \{ 0\} \) . Un vecteur \( x \in E \) est dit isotrope (pour \( \Phi \) ) si \( \Phi \left( x\right) = 0 \) , i.e. \( x \in {C}_{\Phi } \) .

> DEFINITION 9. The isotropic cone of \( \Phi \) is the set \( {C}_{\Phi } = \{ x \in E \mid \Phi \left( x\right) = 0\} \) . We say that \( \Phi \) is definite if \( {C}_{\Phi } = \{ 0\} \) . A vector \( x \in E \) is said to be isotropic (for \( \Phi \) ) if \( \Phi \left( x\right) = 0 \) , i.e. \( x \in {C}_{\Phi } \) .

DéFINITION 10. Deux vecteurs \( x \) et \( y \) de \( E \) sont dit orthogonaux selon \( \Phi \) (ou selon \( \varphi \) ) si \( \varphi \left( {x, y}\right) = 0 \) (ce qui équivaut à \( \varphi \left( {y, x}\right) = 0 \) ).

> DEFINITION 10. Two vectors \( x \) and \( y \) of \( E \) are said to be orthogonal with respect to \( \Phi \) (or with respect to \( \varphi \) ) if \( \varphi \left( {x, y}\right) = 0 \) (which is equivalent to \( \varphi \left( {y, x}\right) = 0 \) ).

Soit \( A \subset E \) . On appelle orthogonal de \( A \) selon \( \Phi \) (ou \( \varphi \) ) l’ensemble

> Let \( A \subset E \) . The orthogonal of \( A \) with respect to \( \Phi \) (or \( \varphi \) ) is the set

\[
{A}^{ \bot  } = \{ y \in  E \mid  \forall x \in  A,\varphi \left( {x, y}\right)  = 0\} .
\]

Deux sous-ensembles \( A \) et \( B \) de \( E \) sont dit orthogonaux selon \( \Phi \) (ou selon \( \varphi \) ) si pour tout \( x \in A \) et pour tout \( y \in B,\varphi \left( {x, y}\right) = 0 \) . On note alors \( A \bot B \) .

> Two subsets \( A \) and \( B \) of \( E \) are said to be orthogonal with respect to \( \Phi \) (or with respect to \( \varphi \) ) if for all \( x \in A \) and for all \( y \in B,\varphi \left( {x, y}\right) = 0 \) . We then denote it \( A \bot B \) .

Remarque 4. - Si \( A \subset E,{A}^{ \bot } \) est un s.e.v de \( E \) et on a \( {A}^{ \bot } = {\left( \operatorname{Vect}A\right) }^{ \bot } \) .

> Remark 4. - If \( A \subset E,{A}^{ \bot } \) is a subspace of \( E \) and we have \( {A}^{ \bot } = {\left( \operatorname{Vect}A\right) }^{ \bot } \) .

- Si \( B \) désigne le sous-ensemble de \( {E}^{ * } \) (dual de \( E \) ) défini par \( B = \{ \varphi \left( {x, \cdot  }\right)  \mid  x \in  A\} \) , \( {A}^{ \bot  } \) est l’orthogonal (au sens dual) de \( B \) , i. e. \( {A}^{ \bot  } = {B}^{ \circ  } \) (voir la partie 4.3 page 134).

> - If \( B \) denotes the subset of \( {E}^{ * } \) (dual of \( E \) ) defined by \( B = \{ \varphi \left( {x, \cdot  }\right)  \mid  x \in  A\} \) , \( {A}^{ \bot  } \) is the orthogonal (in the dual sense) of \( B \) , i.e. \( {A}^{ \bot  } = {B}^{ \circ  } \) (see part 4.3 page 134).

PROPOSITION 3. On parle d’orthogonalité au sens de \( \Phi \) .

> PROPOSITION 3. We speak of orthogonality in the sense of \( \Phi \) .

\[
\text{ (i) }\operatorname{Si}F \subset  E,\;F \subset  {F}^{ \bot   \bot  }\;\text{ (ii) }\operatorname{Si}A \subset  B \subset  E,\;{B}^{ \bot  } \subset  {A}^{ \bot  }\text{ . }
\]

Définition 11. On appelle noyau de \( \Phi \) le s.e.v de \( E \) noté Ker \( \Phi \) défini par

> Definition 11. The kernel of \( \Phi \) is the subspace of \( E \) denoted Ker \( \Phi \) defined by

\[
\operatorname{Ker}\Phi  = {E}^{ \bot  } = \{ x \in  E \mid  \forall y \in  E,\varphi \left( {x, y}\right)  = 0\} .
\]

La forme \( \Phi \) est dite non dégénérée si Ker \( \Phi = \{ 0\} \) , dégénérée si Ker \( \Phi \neq \{ 0\} \) .

> The form \( \Phi \) is said to be non-degenerate if Ker \( \Phi = \{ 0\} \) , degenerate if Ker \( \Phi \neq \{ 0\} \) .

Proposition 4. On a Ker \( \Phi \subset {C}_{\Phi } \) . En particulier, si \( \Phi \) est définie, alors \( \Phi \) est non dégénérée.

> Proposition 4. We have Ker \( \Phi \subset {C}_{\Phi } \) . In particular, if \( \Phi \) is definite, then \( \Phi \) is non-degenerate.

Remarque 5. La réciproque est fausse. Par exemple, si \( \Phi \left( u\right) = \Phi \left( {x, y}\right) = {x}^{2} - {y}^{2},\Phi \) est non dégénérée mais n’est pas définie puisque pour tout \( x,\Phi \left( {x, x}\right) = \Phi \left( {x, - x}\right) = 0 \) .

> Remark 5. The converse is false. For example, if \( \Phi \left( u\right) = \Phi \left( {x, y}\right) = {x}^{2} - {y}^{2},\Phi \) is non-degenerate but not definite since for all \( x,\Phi \left( {x, x}\right) = \Phi \left( {x, - x}\right) = 0 \) .

Notation. Pour unifier les notations, pour toute matrice \( M \) à coefficients dans \( \mathbb{K} \) , on note \( {M}^{ * } \) la transposée de \( M \) . Lorsque le corps de base est \( \mathbb{C} \) et que l’on parle de forme hermitienne, la notation \( {M}^{ * } \) désigne la transconjuguée de \( M \) (i.e. \( {M}^{ * } = \left. {{}^{\mathrm{t}}\bar{M}}\right) \) . Ainsi en dimension finie, si \( A \) désigne la matrice de \( \varphi \) dans une base \( B \) de \( E \) , on a \( {A}^{ * } = A \) et pour tout \( x, y,\varphi \left( {x, y}\right) = {X}^{ * }{AY} \) . Cette notation est avantageuse puisqu’elle permet de traiter en même temps le cas des formes quadratiques et des formes hermitiennes.

> Notation. To unify notation, for any matrix \( M \) with coefficients in \( \mathbb{K} \) , we denote \( {M}^{ * } \) as the transpose of \( M \) . When the base field is \( \mathbb{C} \) and we are dealing with a Hermitian form, the notation \( {M}^{ * } \) denotes the conjugate transpose of \( M \) (i.e. \( {M}^{ * } = \left. {{}^{\mathrm{t}}\bar{M}}\right) \) . Thus in finite dimension, if \( A \) denotes the matrix of \( \varphi \) in a basis \( B \) of \( E \) , we have \( {A}^{ * } = A \) and for all \( x, y,\varphi \left( {x, y}\right) = {X}^{ * }{AY} \) . This notation is advantageous as it allows treating the case of quadratic forms and Hermitian forms simultaneously.

Proposition 5. Supposons E de dimension finie. Soit B une base de E. En identifiant les vecteurs de \( E \) et leur représentation en vecteurs colonne dans la base \( B \) , on a \( \operatorname{Ker}\Phi = \) Ker \( A \) , où \( A \) désigne la matrice de \( \Phi \) dans la base \( B \) .

> Proposition 5. Suppose E is finite-dimensional. Let B be a basis of E. By identifying vectors of \( E \) and their representation as column vectors in basis \( B \), we have \( \operatorname{Ker}\Phi = \) Ker \( A \), where \( A \) denotes the matrix of \( \Phi \) in basis \( B \).

Démonstration. On a \( x \in \operatorname{Ker}\Phi \Leftrightarrow \forall y \in E,\varphi \left( {x, y}\right) = 0 \Leftrightarrow \forall Y,{X}^{ * }{AY} = 0 \Leftrightarrow {X}^{ * }A = 0 \; \Leftrightarrow {\left( {X}^{ * }A\right) }^{ * } = {A}^{ * }X = {AX} = 0 \Leftrightarrow X \in \operatorname{Ker}A \) .

> Proof. We have \( x \in \operatorname{Ker}\Phi \Leftrightarrow \forall y \in E,\varphi \left( {x, y}\right) = 0 \Leftrightarrow \forall Y,{X}^{ * }{AY} = 0 \Leftrightarrow {X}^{ * }A = 0 \; \Leftrightarrow {\left( {X}^{ * }A\right) }^{ * } = {A}^{ * }X = {AX} = 0 \Leftrightarrow X \in \operatorname{Ker}A \).

Bases \( \Phi \) -orthogonales.

> \( \Phi \)-orthogonal bases.

DÉFINITION 12. Une base \( B \) de \( E \) est dite \( \Phi \) -orthogonale si pour tout couple d’éléments distincts \( \left( {e,{e}^{\prime }}\right) \) de \( B \) , on a \( \varphi \left( {e,{e}^{\prime }}\right) = 0 \) .

> DEFINITION 12. A basis \( B \) of \( E \) is said to be \( \Phi \)-orthogonal if for any pair of distinct elements \( \left( {e,{e}^{\prime }}\right) \) of \( B \), we have \( \varphi \left( {e,{e}^{\prime }}\right) = 0 \).

Remarque 6. En dimension finie, si \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base \( \Phi \) -orthogonale, alors

> Remark 6. In finite dimension, if \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is a \( \Phi \)-orthogonal basis, then

\[
\forall \left( {x}_{i}\right)  \in  {\mathbb{K}}^{n},\;\Phi \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2}\Phi \left( {e}_{i}\right) .
\]

Autrement dit, la matrice de \( \Phi \) dans la base \( B \) est diagonale.

> In other words, the matrix of \( \Phi \) in basis \( B \) is diagonal.

THÉORÉME 1. Si E est de dimension finie, il existe une base \( \Phi \) -orthogonale de E.

> THEOREM 1. If E is finite-dimensional, there exists a \( \Phi \)-orthogonal basis of E.

Démonstration. On procède par récurrence sur la dimension \( n \) de \( E \) . Pour \( n = 1 \) , il n’y a rien à montrer. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Si \( \Phi \) est identiquement nulle, alors toute base de \( E \) est \( \Phi \) -orthogonale. Sinon, il existe \( v \in E \) tel que \( \Phi \left( v\right) \neq 0 \) . Dans ce cas, l’application \( f = \varphi \left( {v, \cdot }\right) \) définie par \( f\left( x\right) = \varphi \left( {v, x}\right) \) est une forme linéaire non nulle sur \( E \) . Son noyau \( H \) est un hyperplan de \( E \) , et comme \( v \notin H \) , on a \( E = H \oplus \operatorname{Vect}\left( v\right) \) . Comme dim \( H = n - 1 \) , d’après l’hypothèse de récurrence, il existe une base \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) de \( H \) orthogonale pour \( {\Phi }_{\mid H} \) . On voit alors facilement que \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, v}\right) \) est une base \( \Phi \) -orthogonale.

> Proof. We proceed by induction on the dimension \( n \) of \( E \). For \( n = 1 \), there is nothing to show. Assume the result is true at rank \( n - 1 \) and show it at rank \( n \). If \( \Phi \) is identically zero, then any basis of \( E \) is \( \Phi \)-orthogonal. Otherwise, there exists \( v \in E \) such that \( \Phi \left( v\right) \neq 0 \). In this case, the map \( f = \varphi \left( {v, \cdot }\right) \) defined by \( f\left( x\right) = \varphi \left( {v, x}\right) \) is a non-zero linear form on \( E \). Its kernel \( H \) is a hyperplane of \( E \), and since \( v \notin H \), we have \( E = H \oplus \operatorname{Vect}\left( v\right) \). Since dim \( H = n - 1 \), by the induction hypothesis, there exists a basis \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) of \( H \) orthogonal for \( {\Phi }_{\mid H} \). It is then easy to see that \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, v}\right) \) is a \( \Phi \)-orthogonal basis.

COROLLAIRE 1. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telle que \( {A}^{ * } = A \) . Il existe une matrice inversible \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) telle que \( {P}^{ * }{AP} \) soit une matrice diagonale.

> COROLLARY 1. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be such that \( {A}^{ * } = A \). There exists an invertible matrix \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) such that \( {P}^{ * }{AP} \) is a diagonal matrix.

Démonstration. L’application \( \Phi \) définie sur \( {\mathbb{K}}^{n} \) par \( \Phi \left( X\right) = {X}^{ * }{AX} \) est une forme quadratique (resp. hermitienne) dont la forme polaire est \( \varphi : \left( {X, Y}\right) \mapsto {X}^{ * }{AY} \) . D’après le théorème précédent, il existe une base \( B \) de \( {\mathbb{K}}^{n} \) qui est \( \Phi \) -orthogonale. La matrice \( M \) de \( \Phi \) dans \( B \) est diagonale, et si \( P \) désigne la matrice de passage de la base canonique de \( {\mathbb{K}}^{n} \) à \( B \) , on a \( M = {P}^{ * }{AP} \) , d’où le résultat.

> Proof. The map \( \Phi \) defined on \( {\mathbb{K}}^{n} \) by \( \Phi \left( X\right) = {X}^{ * }{AX} \) is a quadratic (resp. Hermitian) form whose polar form is \( \varphi : \left( {X, Y}\right) \mapsto {X}^{ * }{AY} \). According to the previous theorem, there exists a basis \( B \) of \( {\mathbb{K}}^{n} \) that is \( \Phi \)-orthogonal. The matrix \( M \) of \( \Phi \) in \( B \) is diagonal, and if \( P \) denotes the transition matrix from the canonical basis of \( {\mathbb{K}}^{n} \) to \( B \), we have \( M = {P}^{ * }{AP} \), hence the result.

Remarque 7. Lorsque \( \mathbb{K} = \mathbb{R} \) (où \( \mathbb{K} = \mathbb{C} \) dans le cas hermitien), un résultat plus fort fait l’objet du corollaire 1 page 256, qui affirme que l’on peut choisir pour \( P \) une matrice orthogonale (ou unitaire dans le cas hermitien). L'intérêt du résultat précédent est qu'il est valable pour n’importe quel corps \( \mathbb{K} \) .

> Remark 7. When \( \mathbb{K} = \mathbb{R} \) (or \( \mathbb{K} = \mathbb{C} \) in the Hermitian case), a stronger result is the subject of corollary 1 on page 256, which states that one can choose an orthogonal (or unitary in the Hermitian case) matrix for \( P \). The interest of the previous result is that it is valid for any field \( \mathbb{K} \).

Si \( \Phi \) est une forme quadratique, le théorème 1 assure en dimension finie l’existence d’une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \Phi \) -orthogonale. En posant \( {\lambda }_{i} = \Phi \left( {e}_{i}\right) \) , on a

> If \( \Phi \) is a quadratic form, theorem 1 ensures the existence of an \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \Phi \)-orthogonal basis in finite dimension. By setting \( {\lambda }_{i} = \Phi \left( {e}_{i}\right) \), we have

\[
\forall x \in  E,\;\Phi \left( x\right)  = \Phi \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{e}_{i}^{ * }\left( x\right) {e}_{i}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\left( {e}_{i}^{ * }\left( x\right) \right) }^{2}.
\]

En d'autres termes, on a écrit \( \Phi \) comme combinaison linéaire de carrés de formes linéaires indépendantes. Dans la pratique, ces formes linéaires peuvent être calculées grâce à la méthode qui suit.

> In other words, we have written \( \Phi \) as a linear combination of squares of independent linear forms. In practice, these linear forms can be calculated using the following method.

Méthode de Gauss. Donnons nous une forme quadratique

> Gauss's method. Let us consider a quadratic form

\[
\Phi \left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i}{x}_{i}^{2} + \mathop{\sum }\limits_{{1 \leq  i < j \leq  n}}{a}_{i, j}{x}_{i}{x}_{j}.
\]

En procédant par récurrence, nous allons écrire \( \Phi \) comme combinaison linéaire de carrés de formes linéaires indépendantes. Il y a deux cas.

> Proceeding by induction, we will write \( \Phi \) as a linear combination of squares of independent linear forms. There are two cases.

Premier cas. Il existe au moins un indice \( i \) tel que \( {a}_{i, i} \neq 0 \) , par exemple \( a = {a}_{1,1} \neq 0 \) . On peut écrire \( \Phi \) sous la forme

> First case. There exists at least one index \( i \) such that \( {a}_{i, i} \neq 0 \), for example \( a = {a}_{1,1} \neq 0 \). We can write \( \Phi \) in the form

\[
\Phi \left( {{x}_{1},\ldots ,{x}_{n}}\right)  = a{x}_{1}^{2} + {x}_{1}B\left( {{x}_{2},\ldots ,{x}_{n}}\right)  + C\left( {{x}_{2},\ldots ,{x}_{n}}\right) ,
\]

où \( B \) est une forme linéaire en \( \left( {{x}_{2},\ldots ,{x}_{n}}\right) \) et \( C \) une forme quadratique en \( \left( {{x}_{2},\ldots ,{x}_{n}}\right) \) . On réécrit \( \Phi \) comme

> where \( B \) is a linear form in \( \left( {{x}_{2},\ldots ,{x}_{n}}\right) \) and \( C \) is a quadratic form in \( \left( {{x}_{2},\ldots ,{x}_{n}}\right) \). We rewrite \( \Phi \) as

\[
\Phi \left( {{x}_{1},\ldots ,{x}_{n}}\right)  = a{\left( {x}_{1} + \frac{B\left( {{x}_{2},\ldots ,{x}_{n}}\right) }{2a}\right) }^{2} + \left\lbrack  {C\left( {{x}_{2},\ldots ,{x}_{n}}\right)  - \frac{B{\left( {x}_{2},\ldots ,{x}_{n}\right) }^{2}}{4a}}\right\rbrack  .
\]

En d'autres termes, on a écrit \( \Phi \) comme la somme d’une constante multipliée par le carré d’une forme linéaire (ici \( a{\left\lbrack {x}_{1} + B/\left( 2a\right) \right\rbrack }^{2} \) ) et d’une forme quadratique en \( {x}_{2},\ldots ,{x}_{n} \) (ici, \( C - {B}^{2}/\left( {4a}\right) ) \) . On itère alors la méthode de Gauss en partant cette fois de \( C - {B}^{2}/\left( {4a}\right) \) , et on obtient finalement la réduction souhaitée.

> In other words, we have written \( \Phi \) as the sum of a constant multiplied by the square of a linear form (here \( a{\left\lbrack {x}_{1} + B/\left( 2a\right) \right\rbrack }^{2} \)) and a quadratic form in \( {x}_{2},\ldots ,{x}_{n} \) (here, \( C - {B}^{2}/\left( {4a}\right) ) \)). We then iterate Gauss's method starting this time from \( C - {B}^{2}/\left( {4a}\right) \), and we finally obtain the desired reduction.

Second cas. Pour tous les indices \( i,{a}_{i, i} = 0 \) . Si \( \Phi \) est nulle, c’est terminé, sinon il existe au moins un \( {a}_{i, j} \) non nul (avec \( i < j \) ), par exemple \( a = {a}_{1,2} \neq 0 \) . On peut écrire \( \Phi \) sous la forme

> Second case. For all indices \( i,{a}_{i, i} = 0 \). If \( \Phi \) is zero, it is finished; otherwise, there exists at least one non-zero \( {a}_{i, j} \) (with \( i < j \)), for example \( a = {a}_{1,2} \neq 0 \). We can write \( \Phi \) in the form

\[
\Phi \left( {{x}_{1},\ldots ,{x}_{n}}\right)  = a{x}_{1}{x}_{2} + {x}_{1}B\left( {{x}_{3},\ldots ,{x}_{n}}\right)  + {x}_{2}C\left( {{x}_{3},\ldots ,{x}_{n}}\right)  + D\left( {{x}_{3},\ldots ,{x}_{n}}\right) ,
\]

où \( B \) et \( C \) sont des formes linéaires et \( D \) une forme quadratique en \( \left( {{x}_{3},\ldots ,{x}_{n}}\right) \) . On réécrit \( \Phi \) comme

> where \( B \) and \( C \) are linear forms and \( D \) is a quadratic form in \( \left( {{x}_{3},\ldots ,{x}_{n}}\right) \). We rewrite \( \Phi \) as

\[
\Phi \left( {{x}_{1},\ldots ,{x}_{n}}\right)  = a\left( {{x}_{1} + \frac{C}{a}}\right) \left( {{x}_{2} + \frac{B}{a}}\right)  + \left( {D - \frac{BC}{a}}\right)
\]

\[
= \frac{a}{4}\left\lbrack  {{\left( {x}_{1} + {x}_{2} + \frac{B + C}{a}\right) }^{2} - {\left( {x}_{1} - {x}_{2} + \frac{C - B}{a}\right) }^{2}}\right\rbrack   + \left\lbrack  {D - \frac{BC}{a}}\right\rbrack  .
\]

Les deux premiers termes du dernier membre de cette égalité sont les carrés de formes linéaires, et on itère la méthode de Gauss en partant cette fois de \( D - {BC}/a \) , forme quadratique en \( \left( {{x}_{3},\ldots ,{x}_{n}}\right) \) .

> The first two terms of the last member of this equality are the squares of linear forms, and we iterate Gauss's method starting this time from \( D - {BC}/a \), a quadratic form in \( \left( {{x}_{3},\ldots ,{x}_{n}}\right) \).

Remarque 8. - Il existe bien sûr d'autres moyens d'écrire une forme quadratique comme combinaison linéaire de carrés de formes linéaires. L'avantage de la méthode de Gauss est qu'elle assure l'indépendance des formes linéaires obtenues (résultat non démontré ici, mais facile à obtenir).

> Remark 8. - There are of course other ways to write a quadratic form as a linear combination of squares of linear forms. The advantage of Gauss's method is that it ensures the independence of the linear forms obtained (a result not proven here, but easy to obtain).

- Le cas des formes hermitiennes se traite de manière analogue, en remplaçant les carrés par les carrés des modules. Par exemple la forme hermitienne

> - The case of Hermitian forms is treated analogously, by replacing squares with the squares of moduli. For example, the Hermitian form

\[
\Phi \left( {x, y}\right)  = x\bar{y} + \bar{x}y\;\text{ se réduit en }\;\Phi \left( {x, y}\right)  = \frac{1}{2}\left( {{\left| x + y\right| }^{2} - {\left| x - y\right| }^{2}}\right) .
\]

La forme hermitienne

> The Hermitian form

\( \Phi \left( {x, y, z}\right) = x\bar{x} + y\bar{y} - {2i}\bar{x}y + {2ix}\bar{y} + {2y}\bar{z} + 2\bar{y}z\; \) se réduit en

> \( \Phi \left( {x, y, z}\right) = x\bar{x} + y\bar{y} - {2i}\bar{x}y + {2ix}\bar{y} + {2y}\bar{z} + 2\bar{y}z\; \) reduces to

\[
\Phi \left( {x, y, z}\right)  = \left( {x - {2iy}}\right) \left( {\bar{x} + {2i}\bar{y}}\right)  - {3y}\bar{y} + 2\bar{y}z + {2y}\bar{z} = {\left| x - 2iy\right| }^{2} - 3{\left| y - \frac{2z}{3}\right| }^{2} + \frac{4}{3}{\left| z\right| }^{2}.
\]

Propriétés des orthogonaux selon \( \Phi \) . La lettre \( \Phi \) désigne toujours une forme quadra-tique (resp. hermitienne) sur \( E \) et lorsque l’on parlera d’orthogonal, ce sera par rapport à \( \Phi \) .

> Properties of orthogonals according to \( \Phi \) . The letter \( \Phi \) always denotes a quadratic (resp. Hermitian) form on \( E \) and when we speak of an orthogonal, it will be with respect to \( \Phi \) .

Proposition 6. Supposons \( E \) de dimension finie. Tout s.e.v \( F \) de \( E \) vérifie

> Proposition 6. Suppose \( E \) is finite-dimensional. Any subspace \( F \) of \( E \) satisfies

(i) \( \dim F + \dim {F}^{ \bot } = \dim E + \dim \left( {F \cap \operatorname{Ker}\Phi }\right) \) .

> (ii) \( {F}^{ \bot \bot } = F + \operatorname{Ker}\Phi \) .

(ii) \( {F}^{ \bot \bot } = F + \operatorname{Ker}\Phi \) .

> Démonstration. (i). On considère l’application \( \psi : F \rightarrow {E}^{ * }\;x \mapsto \varphi \left( {x, \cdot }\right) \) . Cette application est linéaire, donc \( \dim \left( {\operatorname{Ker}\psi }\right) + \dim \left( {\operatorname{Im}\psi }\right) = \dim F \) . Or \( \operatorname{Ker}\psi = F \cap \operatorname{Ker}\Phi \) et \( {\left( \operatorname{Im}\psi \right) }^{ \circ } = {F}^{ \bot } \) (voir la remarque 4). Comme d’après le théorème 3 page 134, on a dim(Im \( \psi {)}^{ \circ } = \dim E - \dim \left( {\operatorname{Im}\psi }\right) \) , on en déduit

Proof. (i). Consider the map \( \psi : F \rightarrow {E}^{ * }\;x \mapsto \varphi \left( {x, \cdot }\right) \) . This map is linear, so \( \dim \left( {\operatorname{Ker}\psi }\right) + \dim \left( {\operatorname{Im}\psi }\right) = \dim F \) . However, \( \operatorname{Ker}\psi = F \cap \operatorname{Ker}\Phi \) and \( {\left( \operatorname{Im}\psi \right) }^{ \circ } = {F}^{ \bot } \) (see remark 4). Since according to theorem 3 on page 134, we have dim(Im \( \psi {)}^{ \circ } = \dim E - \dim \left( {\operatorname{Im}\psi }\right) \) , we deduce

\[
\dim {F}^{ \bot  } = \dim E - \left( {\dim F - \dim \left( {\operatorname{Ker}\psi }\right) }\right)  = \dim E - \dim F + \dim \left( {F \cap  \operatorname{Ker}\Phi }\right) ,
\]

d'où (i).

> whence (i).

(ii). On a \( F \subset {F}^{ \bot \bot } \) et \( \operatorname{Ker}\Phi \subset {F}^{ \bot \bot } \) , donc \( F + \operatorname{Ker}\Phi \subset {F}^{ \bot \bot } \) . Pour prouver l’égalité, nous allons prouver l’égalité des dimensions. En appliquant (i) à \( {F}^{ \bot } \) , on a

> (ii). We have \( F \subset {F}^{ \bot \bot } \) and \( \operatorname{Ker}\Phi \subset {F}^{ \bot \bot } \) , so \( F + \operatorname{Ker}\Phi \subset {F}^{ \bot \bot } \) . To prove the equality, we will prove the equality of the dimensions. By applying (i) to \( {F}^{ \bot } \) , we have

\[
\dim {F}^{ \bot  } + \dim {F}^{ \bot   \bot  } = \dim E + \dim \operatorname{Ker}\left( {{F}^{ \bot  } \cap  \operatorname{Ker}\Phi }\right)  = \dim E + \dim \left( {\operatorname{Ker}\Phi }\right)
\]

(comme \( \operatorname{Ker}\Phi \subset {F}^{ \bot },{F}^{ \bot } \cap \operatorname{Ker}\Phi = \operatorname{Ker}\Phi \) ). En retranchant (i) à cette égalité, on obtient

> (as \( \operatorname{Ker}\Phi \subset {F}^{ \bot },{F}^{ \bot } \cap \operatorname{Ker}\Phi = \operatorname{Ker}\Phi \) ). By subtracting (i) from this equality, we obtain

\[
\dim {F}^{ \bot   \bot  } - \dim F = \dim \left( {\operatorname{Ker}\Phi }\right)  - \dim \left( {F \cap  \operatorname{Ker}\Phi }\right)
\]

donc dim \( {F}^{ \bot \bot } = \dim \left( {F + \operatorname{Ker}\Phi }\right) \) et le résultat.

> thus dim \( {F}^{ \bot \bot } = \dim \left( {F + \operatorname{Ker}\Phi }\right) \) and the result.

Proposition 7. Soit \( F \) un s.e.v de dimension finie de \( E \) (mais \( E \) de dimension quel-conque). Alors

> Proposition 7. Let \( F \) be a finite-dimensional subspace of \( E \) (but \( E \) of arbitrary dimension). Then

(i) Si la restriction \( {\Phi }_{\mid F} \) de \( \Phi \dot{a}F \) est définie, on a \( F \oplus {F}^{ \bot } = E \) .

> (i) If the restriction \( {\Phi }_{\mid F} \) of \( \Phi \dot{a}F \) is definite, we have \( F \oplus {F}^{ \bot } = E \) .

(ii) Si \( \Phi \) est définie, on a \( F = {F}^{ \bot \bot } \) .

> (ii) If \( \Phi \) is definite, we have \( F = {F}^{ \bot \bot } \) .

Démonstration. (i). Si \( x \in F \cap {F}^{ \bot } \) , alors \( \varphi \left( {x, x}\right) = 0 \) et comme la restriction de \( \Phi \) à \( F \) est définie par hypothèse, on a forcément \( x = 0 \) . Autrement dit, \( F \cap {F}^{ \bot } = \{ 0\} \;\left( *\right) \) .

> Proof. (i). If \( x \in F \cap {F}^{ \bot } \) , then \( \varphi \left( {x, x}\right) = 0 \) and since the restriction of \( \Phi \) to \( F \) is definite by hypothesis, we necessarily have \( x = 0 \) . In other words, \( F \cap {F}^{ \bot } = \{ 0\} \;\left( *\right) \) .

D’après le théorème 1, il existe une base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) de \( F \) , orthogonale pour la restriction de \( \Phi \) à \( F \) . Soit \( x \in E \) . On cherche à écrire \( x = y + z \) avec \( y \in F \) et \( z \in {F}^{ \bot } \) . Écrivons \( y = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{e}_{i} \) . Alors \( z = x - y \in {F}^{ \bot } \) si et seulement si pour tout \( j \in \{ 1,\ldots , p\} ,\varphi \left( {{e}_{j}, z}\right) = 0 \) , i.e. si pour tout \( j \) , \( \varphi \left( {{e}_{j}, x}\right) - {\lambda }_{j}\varphi \left( {{e}_{j},{e}_{j}}\right) = 0 \) . En choisissant \( {\lambda }_{i} = \frac{\varphi \left( {{e}_{i}, x}\right) }{\varphi \left( {{e}_{i},{e}_{i}}\right) } \) , on voit donc que \( x = y + z \) , avec \( y \in F \) et \( z \in {F}^{ \bot } \) . Donc \( F + {F}^{ \bot } = E \) d’où (i) avec \( \left( *\right) \) .

> According to theorem 1, there exists a basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) of \( F \) that is orthogonal for the restriction of \( \Phi \) to \( F \) . Let \( x \in E \) . We seek to write \( x = y + z \) with \( y \in F \) and \( z \in {F}^{ \bot } \) . Let us write \( y = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{e}_{i} \) . Then \( z = x - y \in {F}^{ \bot } \) if and only if for all \( j \in \{ 1,\ldots , p\} ,\varphi \left( {{e}_{j}, z}\right) = 0 \) , i.e., if for all \( j \) , \( \varphi \left( {{e}_{j}, x}\right) - {\lambda }_{j}\varphi \left( {{e}_{j},{e}_{j}}\right) = 0 \) . By choosing \( {\lambda }_{i} = \frac{\varphi \left( {{e}_{i}, x}\right) }{\varphi \left( {{e}_{i},{e}_{i}}\right) } \) , we therefore see that \( x = y + z \) , with \( y \in F \) and \( z \in {F}^{ \bot } \) . Thus \( F + {F}^{ \bot } = E \) whence (i) with \( \left( *\right) \) .

(ii). On sait (voir proposition 3) que \( F \subset {F}^{ \bot \bot } \) . Montrons l’inclusion réciproque. Soit \( x \in \; {F}^{ \bot \bot } \) . D’après (i), il existe \( y \in F \) et \( z \in {F}^{ \bot } \) tels que \( x = y + z \) . Or \( \varphi \left( {x, z}\right) = 0 = \varphi \left( {y, z}\right) + \varphi \left( {z, z}\right) = \; \varphi \left( {z, z}\right) \) , donc \( z \in {C}_{\Phi } \) et \( \Phi \) étant définie, \( z = 0 \) . Donc \( x = y \in F \) , d’où \( {F}^{ \bot \bot } \subset F \) .

> (ii). We know (see proposition 3) that \( F \subset {F}^{ \bot \bot } \) . Let us show the reverse inclusion. Let \( x \in \; {F}^{ \bot \bot } \) . According to (i), there exist \( y \in F \) and \( z \in {F}^{ \bot } \) such that \( x = y + z \) . However, \( \varphi \left( {x, z}\right) = 0 = \varphi \left( {y, z}\right) + \varphi \left( {z, z}\right) = \; \varphi \left( {z, z}\right) \) , so \( z \in {C}_{\Phi } \) and \( \Phi \) being defined, \( z = 0 \) . Thus \( x = y \in F \) , whence \( {F}^{ \bot \bot } \subset F \) .

Loi d'inertie de Sylvester. Dans toute la suite, \( \Phi \) représente soit une forme quadratique sur un \( \mathbb{R} \) -e.v \( E \) , soit une forme hermitienne sur un \( \mathbb{C} \) -e.v \( E \) .

> Sylvester's law of inertia. Throughout the following, \( \Phi \) represents either a quadratic form on an \( \mathbb{R} \) -v.s. \( E \) , or a Hermitian form on a \( \mathbb{C} \) -v.s. \( E \) .

Supposons \( E \) de dimension finie \( n \) . D’après le théorème 1, il existe une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) qui est \( \Phi \) -orthogonale. Ceci entraîne que pour tout \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) ,

> Suppose \( E \) is of finite dimension \( n \) . According to theorem 1, there exists a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) which is \( \Phi \) -orthogonal. This implies that for all \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) ,

\[
\Phi \left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{2}\Phi \left( {e}_{i}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\left| {e}_{i}^{ * }\left( x\right) \right| }^{2},\;\text{ où }\;{\lambda }_{i} = \Phi \left( {e}_{i}\right)  \in  \mathbb{R}.
\]

Chaque \( {\lambda }_{i} \) est soit positif, soit négatif, soit nul. Supposons par exemple

> Each \( {\lambda }_{i} \) is either positive, negative, or zero. Suppose for example

\[
{\lambda }_{1},\ldots ,{\lambda }_{p} > 0,\;{\lambda }_{p + 1},\ldots ,{\lambda }_{p + q} < 0\;\text{ et }\;{\lambda }_{p + q + 1} = \cdots  = {\lambda }_{n} = 0.
\]

Pour \( i,1 \leq i \leq p \) , on peut écrire \( {\lambda }_{i} = {\omega }_{i}^{2} \) et pour \( i, p + 1 \leq i \leq p + q \) , on peut écrire \( {\lambda }_{i} = - {\omega }_{i}^{2} \) , où les \( {\omega }_{i} \) sont réels non nuls. En posant \( {f}_{i} = {\omega }_{i}{e}_{i}^{ * } \) , on a

> For \( i,1 \leq i \leq p \) , we can write \( {\lambda }_{i} = {\omega }_{i}^{2} \) and for \( i, p + 1 \leq i \leq p + q \) , we can write \( {\lambda }_{i} = - {\omega }_{i}^{2} \) , where the \( {\omega }_{i} \) are non-zero real numbers. By setting \( {f}_{i} = {\omega }_{i}{e}_{i}^{ * } \) , we have

\[
\Phi \left( x\right)  = {\left| {f}_{1}\left( x\right) \right| }^{2} + \cdots  + {\left| {f}_{p}\left( x\right) \right| }^{2} - {\left| {f}_{p + 1}\left( x\right) \right| }^{2} - \cdots  - {\left| {f}_{p + q}\left( x\right) \right| }^{2},
\]

(*)

> et \( {f}_{1},\ldots ,{f}_{p + q} \) sont des formes linéaires linéairement indépendantes.

and \( {f}_{1},\ldots ,{f}_{p + q} \) are linearly independent linear forms.

> - THÉORÉME 2 (SYLVESTER). Quelle que soit la décomposition de \( \Phi \) du type (*)

- THEOREM 2 (SYLVESTER). Regardless of the decomposition of \( \Phi \) of type (*)

\[
\Phi \left( x\right)  = {\left| {g}_{1}\left( x\right) \right| }^{2} + \cdots  + {\left| {g}_{{p}^{\prime }}\left( x\right) \right| }^{2} - {\left| {g}_{{p}^{\prime } + 1}\left( x\right) \right| }^{2} - \cdots  - {\left| {g}_{{p}^{\prime } + {q}^{\prime }}\left( x\right) \right| }^{2},
\]

\( \left( {* * }\right) \)

> où \( {g}_{1},\ldots ,{g}_{{p}^{\prime } + {q}^{\prime }} \) sont des formes linéaires linéairement indépendantes, on a \( {p}^{\prime } = p \) et \( {q}^{\prime } = q \) . Le couple \( \left( {p, q}\right) \) s’appelle la signature de \( \Phi \) , et le rang de \( \Phi \) est égal à \( p + q \) .

where \( {g}_{1},\ldots ,{g}_{{p}^{\prime } + {q}^{\prime }} \) are linearly independent linear forms, we have \( {p}^{\prime } = p \) and \( {q}^{\prime } = q \) . The pair \( \left( {p, q}\right) \) is called the signature of \( \Phi \) , and the rank of \( \Phi \) is equal to \( p + q \) .

> Démonstration. Supposons \( {p}^{\prime } \neq p \) , par exemple \( {p}^{\prime } > p \) . Complétons \( {g}_{1},\ldots ,{g}_{{p}^{\prime } + {q}^{\prime }} \) en une base \( {g}_{1},\ldots ,{g}_{n} \) de \( {E}^{ * } \) . Les formes linéaires \( {f}_{1},\ldots ,{f}_{p},{g}_{{p}^{\prime } + 1},\ldots ,{g}_{n} \) sont au nombre de \( p + n - {p}^{\prime } < n \) , et donc

Proof. Suppose \( {p}^{\prime } \neq p \) , for example \( {p}^{\prime } > p \) . Let us complete \( {g}_{1},\ldots ,{g}_{{p}^{\prime } + {q}^{\prime }} \) into a basis \( {g}_{1},\ldots ,{g}_{n} \) of \( {E}^{ * } \) . The linear forms \( {f}_{1},\ldots ,{f}_{p},{g}_{{p}^{\prime } + 1},\ldots ,{g}_{n} \) are \( p + n - {p}^{\prime } < n \) in number, and therefore

\[
\exists x \neq  0,\;{f}_{1}\left( x\right)  = \cdots  = {f}_{p}\left( x\right)  = {g}_{{p}^{\prime } + 1}\left( x\right)  = \cdots  = {g}_{n}\left( x\right)  = 0.
\]

Ceci entraîne \( \Phi \left( x\right) \leq 0 \) d’après l’expression \( \left( *\right) \) de \( \Phi \) . Au moins l’un des \( {g}_{i}\left( x\right) \) pour \( 1 \leq i \leq {p}^{\prime } \) est non nul, car sinon on aurait \( {g}_{1}\left( x\right) = \cdots = {g}_{{p}^{\prime }}\left( x\right) = {g}_{{p}^{\prime } + 1}\left( x\right) = \cdots = {g}_{n}\left( x\right) = 0 \) et donc \( x = 0 \) car \( {\left( {g}_{i}\right) }_{1 \leq i \leq n} \) est une base de \( {E}^{ * } \) . Donc \( \Phi \left( x\right) > 0 \) d’après l’expression \( \left( {* * }\right) \) de \( \Phi \) , ce qui est contradictoire. Ainsi \( p = {p}^{\prime } \) . On montrerait de même que \( q = {q}^{\prime } \) .

> This implies \( \Phi \left( x\right) \leq 0 \) according to the expression \( \left( *\right) \) of \( \Phi \) . At least one of the \( {g}_{i}\left( x\right) \) for \( 1 \leq i \leq {p}^{\prime } \) is non-zero, because otherwise we would have \( {g}_{1}\left( x\right) = \cdots = {g}_{{p}^{\prime }}\left( x\right) = {g}_{{p}^{\prime } + 1}\left( x\right) = \cdots = {g}_{n}\left( x\right) = 0 \) and therefore \( x = 0 \) since \( {\left( {g}_{i}\right) }_{1 \leq i \leq n} \) is a basis of \( {E}^{ * } \) . Thus \( \Phi \left( x\right) > 0 \) according to the expression \( \left( {* * }\right) \) of \( \Phi \) , which is contradictory. Thus \( p = {p}^{\prime } \) . We would show similarly that \( q = {q}^{\prime } \) .

Quant au rang de \( \Phi \) , il suffit de remarquer que la matrice de \( \Phi \) dans la base \( \Phi \) -orthogonale \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est \( \left( \begin{matrix} {I}_{p} & 0 & 0 \\ 0 & - {I}_{q} & 0 \\ 0 & 0 & 0 \end{matrix}\right) \) , donc de rang \( p + q \) .

> As for the rank of \( \Phi \) , it suffices to note that the matrix of \( \Phi \) in the \( \Phi \) -orthogonal basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is \( \left( \begin{matrix} {I}_{p} & 0 & 0 \\ 0 & - {I}_{q} & 0 \\ 0 & 0 & 0 \end{matrix}\right) \) , and therefore of rank \( p + q \) .

Remarque 9. Si on trouve trois s.e.v \( {F}^{ + },{F}^{ - },{F}^{0} \) de \( E \) qui sont \( \Phi \) -orthogonaux deux à deux, tels que \( {F}^{ + } \oplus {F}^{ - } \oplus {F}^{0} = E,\Phi \left( x\right) > 0 \) sur \( {F}^{ + } \smallsetminus \{ 0\} ,\Phi \left( x\right) < 0 \) sur \( {F}^{ - } \smallsetminus \{ 0\} \) et \( \Phi \left( x\right) = 0 \) sur \( {F}^{0} \) , alors la signature de \( \Phi \) est \( \left( {\dim {F}^{ + },\dim {F}^{ - }}\right) \) . En effet, si \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) (resp. \( \left( {{e}_{p + 1},\ldots ,{e}_{p + q}}\right) ,\left( {{e}_{p + q + 1},\ldots ,{e}_{n}}\right) \) ) est une base orthogonale pour la restriction de \( \Phi \) à \( {F}^{ + } \) (resp. à \( {F}^{ - } \) ,à \( {F}^{0} \) ), alors \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base de \( E \) , et on peut écrire

> Remark 9. If we find three subspaces \( {F}^{ + },{F}^{ - },{F}^{0} \) of \( E \) that are pairwise \( \Phi \) -orthogonal, such that \( {F}^{ + } \oplus {F}^{ - } \oplus {F}^{0} = E,\Phi \left( x\right) > 0 \) on \( {F}^{ + } \smallsetminus \{ 0\} ,\Phi \left( x\right) < 0 \) on \( {F}^{ - } \smallsetminus \{ 0\} \) and \( \Phi \left( x\right) = 0 \) on \( {F}^{0} \) , then the signature of \( \Phi \) is \( \left( {\dim {F}^{ + },\dim {F}^{ - }}\right) \) . Indeed, if \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) (resp. \( \left( {{e}_{p + 1},\ldots ,{e}_{p + q}}\right) ,\left( {{e}_{p + q + 1},\ldots ,{e}_{n}}\right) \) ) is an orthogonal basis for the restriction of \( \Phi \) to \( {F}^{ + } \) (resp. to \( {F}^{ - } \) , to \( {F}^{0} \) ), then \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is a basis of \( E \) , and we can write

\[
\Phi \left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{p}\Phi \left( {e}_{i}\right) {\left| {e}_{i}^{ * }\left( x\right) \right| }^{2} + \mathop{\sum }\limits_{{i = p + 1}}^{{p + q}}\Phi \left( {e}_{i}\right) {\left| {e}_{i}^{ * }\left( x\right) \right| }^{2}
\]

avec \( \Phi \left( {e}_{i}\right) > 0 \) pour \( 1 \leq i \leq p \) et \( \Phi \left( {e}_{i}\right) < 0 \) pour \( p + 1 \leq i \leq p + q \) .

> with \( \Phi \left( {e}_{i}\right) > 0 \) for \( 1 \leq i \leq p \) and \( \Phi \left( {e}_{i}\right) < 0 \) for \( p + 1 \leq i \leq p + q \) .
