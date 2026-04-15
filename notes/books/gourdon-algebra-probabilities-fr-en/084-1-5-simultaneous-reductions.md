#### 1.5. Simultaneous reductions

*Français : 1.5. Réductions simultanées*

Proposition 7. Soient \( f, g \in \mathcal{L}\left( E\right) \) tels que \( f \circ g = g \circ f \) . Alors

> Proposition 7. Let \( f, g \in \mathcal{L}\left( E\right) \) be such that \( f \circ g = g \circ f \). Then

(i) Tout sous-espace propre de \( f \) est stable par \( g \) (en particulier Ker \( f \) ).

> (i) Every eigenspace of \( f \) is stable by \( g \) (in particular Ker \( f \)).

(ii) Im \( f \) est stable par \( g \) .

> (ii) Im \( f \) is stable by \( g \).

Démonstration. (i) Soit \( {E}_{\lambda } \) un sous-espace propre de \( f \) . Pour tout \( x \in {E}_{\lambda }, f\left\lbrack {g\left( x\right) }\right\rbrack = g\left\lbrack {f\left( x\right) }\right\rbrack = \; g\left( {\lambda x}\right) = {\lambda g}\left( x\right) \) donc \( g\left( x\right) \in {E}_{\lambda }. \)

> Proof. (i) Let \( {E}_{\lambda } \) be an eigenspace of \( f \). For all \( x \in {E}_{\lambda }, f\left\lbrack {g\left( x\right) }\right\rbrack = g\left\lbrack {f\left( x\right) }\right\rbrack = \; g\left( {\lambda x}\right) = {\lambda g}\left( x\right) \) therefore \( g\left( x\right) \in {E}_{\lambda }. \)

(ii) Soit \( y \in \operatorname{Im}f \) , et \( x \in E \) tel que \( y = f\left( x\right) \) . On a \( g\left( y\right) = g\left\lbrack {f\left( x\right) }\right\rbrack = f\left\lbrack {g\left( x\right) }\right\rbrack \in \operatorname{Im}f \) .

> (ii) Let \( y \in \operatorname{Im}f \), and \( x \in E \) such that \( y = f\left( x\right) \). We have \( g\left( y\right) = g\left\lbrack {f\left( x\right) }\right\rbrack = f\left\lbrack {g\left( x\right) }\right\rbrack \in \operatorname{Im}f \).

\( \rightarrow \) THÉORÉME 4 (DIAGONALISATION SIMULTANÉE). Si \( f \) et \( g \in \mathcal{L}\left( E\right) \) sont diagonalisables et commutent, il existe une base commune de diagonalisation de \( f \) et \( g \) (on dit alors que \( f \) et \( g \) sont codiagonalisables).

> \( \rightarrow \) THEOREM 4 (SIMULTANEOUS DIAGONALIZATION). If \( f \) and \( g \in \mathcal{L}\left( E\right) \) are diagonalizable and commute, there exists a common basis of diagonalization for \( f \) and \( g \) (we then say that \( f \) and \( g \) are codiagonalizable).

Démonstration. Soient \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) les valeurs propres de \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) les sous-espaces propres correspondants. Pour tout \( i,{E}_{{\lambda }_{i}} \) est stable par \( g \) . La restriction de \( g \) à \( {E}_{{\lambda }_{i}},{g}_{\mid {E}_{{\lambda }_{i}}} \) , induit un endomorphisme de \( {E}_{{\lambda }_{i}} \) , diagonalisable d’après la proposition 6. Il existe donc une base \( {B}_{i} \) de \( {E}_{{\lambda }_{i}} \) de vecteurs propres de \( g \) (et bien sûr de \( f \) car \( {f}_{\mid {E}_{{\lambda }_{i}}} = {\lambda }_{i}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) ). Or \( E = { \oplus }_{i = 1}^{r}{E}_{{\lambda }_{i}} \) , donc \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) est une base de diagonalisation commune de \( f \) et \( g \) .

> Proof. Let \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) be the eigenvalues of \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) the corresponding eigenspaces. For any \( i,{E}_{{\lambda }_{i}} \) is stable by \( g \) . The restriction of \( g \) to \( {E}_{{\lambda }_{i}},{g}_{\mid {E}_{{\lambda }_{i}}} \) induces an endomorphism of \( {E}_{{\lambda }_{i}} \) , diagonalizable according to proposition 6. There exists therefore a basis \( {B}_{i} \) of \( {E}_{{\lambda }_{i}} \) of eigenvectors of \( g \) (and of course of \( f \) because \( {f}_{\mid {E}_{{\lambda }_{i}}} = {\lambda }_{i}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) ). Now \( E = { \oplus }_{i = 1}^{r}{E}_{{\lambda }_{i}} \) , so \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) is a common diagonalization basis for \( f \) and \( g \) .

Remarque 10. La réciproque est vraie : si \( f \) et \( g \) se diagonalisent dans une même base, alors \( f \) et \( g \) commutent (il suffit de remarquer que \( f \) et \( g \) commutent sur cette base).

> Remark 10. The converse is true: if \( f \) and \( g \) are diagonalizable in the same basis, then \( f \) and \( g \) commute (it suffices to note that \( f \) and \( g \) commute on this basis).

\( \rightarrow \) THÉORÉME 5 (TRIGONALISATION SIMULTANÉE). Si \( f \) et \( g \in \mathcal{L}\left( E\right) \) sont trigonalisables et commutent, alors il existe une base de trigonalisation commune de \( f \) et \( g \) (on dit alors que \( f \) et \( g \) sont cotrigonalisables).

> \( \rightarrow \) THEOREM 5 (SIMULTANEOUS TRIGONALIZATION). If \( f \) and \( g \in \mathcal{L}\left( E\right) \) are trigonalizable and commute, then there exists a common trigonalization basis for \( f \) and \( g \) (we then say that \( f \) and \( g \) are cotrigonalizable).

Démonstration. Préliminaire. Remarquons déjà que \( f \) et \( g \) ont un vecteur propre commun. En effet, \( f \) admet une valeur propre \( \lambda \in \mathbb{K} \) (puisque \( f \) est trigonalisable). Le sous-espace propre \( {E}_{\lambda } \) est stable par \( g \) , et \( {g}_{\mid {E}_{\lambda }} \) est trigonalisable (voir la remarque 9), donc admet un vecteur propre \( x \in {E}_{\lambda } \) . Finalement, \( x \) est un vecteur propre commun à \( f \) et \( g \) .

> Proof. Preliminary. Let us first note that \( f \) and \( g \) have a common eigenvector. Indeed, \( f \) admits an eigenvalue \( \lambda \in \mathbb{K} \) (since \( f \) is trigonalizable). The eigenspace \( {E}_{\lambda } \) is stable by \( g \) , and \( {g}_{\mid {E}_{\lambda }} \) is trigonalizable (see remark 9), so it admits an eigenvector \( x \in {E}_{\lambda } \) . Finally, \( x \) is a common eigenvector for \( f \) and \( g \) .

On procède maintenant par récurrence sur \( n \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) . Pour le montrer au rang \( n \) , nous donnons deux méthodes.

> We now proceed by induction on \( n \) . For \( n = 1 \) , it is obvious. Assume the result is true at rank \( n - 1 \) . To show it at rank \( n \) , we provide two methods.

Première méthode. Comme \( f \circ g = g \circ f \) , on a \( {}^{\mathrm{t}}g \circ {}^{\mathrm{t}}f = {}^{\mathrm{t}}f \circ {}^{\mathrm{t}}g \) , donc d’après le préliminaire appliqué à \( {}^{\mathrm{t}}f \) et \( {}^{\mathrm{t}}g \) , il existe un vecteur propre \( x \in {E}^{ * } \) commun à \( {}^{\mathrm{t}}f \) et à \( {}^{\mathrm{t}}g \) . Ainsi, \( \mathbb{K}x \) est stable par \( {}^{\mathrm{t}}f \) et \( {}^{\mathrm{t}}g \) , donc l’orthogonal \( H \) de \( \mathbb{K}x \) dans \( E \) , est un hyperplan de \( E \) stable par \( f \) et \( g \) . D’après l’hypothèse de récurrence, \( {f}_{\mid H} \) et \( {g}_{\mid H} \) sont trigonalisables dans une même base \( {B}^{\prime } \) de \( H \) . Soit \( e \in E \) tel que \( B = \left( {{B}^{\prime }, e}\right) \) forme une base de \( E \) . Alors

> First method. Since \( f \circ g = g \circ f \) , we have \( {}^{\mathrm{t}}g \circ {}^{\mathrm{t}}f = {}^{\mathrm{t}}f \circ {}^{\mathrm{t}}g \) , so according to the preliminary applied to \( {}^{\mathrm{t}}f \) and \( {}^{\mathrm{t}}g \) , there exists a common eigenvector \( x \in {E}^{ * } \) for \( {}^{\mathrm{t}}f \) and \( {}^{\mathrm{t}}g \) . Thus, \( \mathbb{K}x \) is stable under \( {}^{\mathrm{t}}f \) and \( {}^{\mathrm{t}}g \) , so the orthogonal \( H \) of \( \mathbb{K}x \) in \( E \) , is a hyperplane of \( E \) stable under \( f \) and \( g \) . By the induction hypothesis, \( {f}_{\mid H} \) and \( {g}_{\mid H} \) are trigonalizable in the same basis \( {B}^{\prime } \) of \( H \) . Let \( e \in E \) be such that \( B = \left( {{B}^{\prime }, e}\right) \) forms a basis of \( E \) . Then

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix}  & & & \\   & {\left\lbrack  {f}_{\mid H}\right\rbrack  }_{{B}^{\prime }} & & \underset{ \times  }{\vdots } \\  0 & \cdots & 0 &  \times   \end{matrix}\right)
\]

et comme la matrice de \( {f}_{\mid H} \) dans \( {B}^{\prime } \) est triangulaire supérieure, on en déduit que \( {\left\lbrack f\right\rbrack }_{B} \) est triangulaire supérieure. De même, \( {\left\lbrack g\right\rbrack }_{B} \) est triangulaire supérieure, d’où le résultat au rang \( n \) . Seconde méthode. Le préliminaire assure l’existence d’un vecteur propre \( x \) commun à \( f \) et à \( g \) . Complétons \( x \) en une base \( B = \left( {x,{e}_{2},\ldots ,{e}_{n}}\right) \) de \( E \) . On a

> and since the matrix of \( {f}_{\mid H} \) in \( {B}^{\prime } \) is upper triangular, we deduce that \( {\left\lbrack f\right\rbrack }_{B} \) is upper triangular. Similarly, \( {\left\lbrack g\right\rbrack }_{B} \) is upper triangular, hence the result at rank \( n \) . Second method. The preliminary ensures the existence of a common eigenvector \( x \) for \( f \) and \( g \) . Let us complete \( x \) into a basis \( B = \left( {x,{e}_{2},\ldots ,{e}_{n}}\right) \) of \( E \) . We have

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} \alpha &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & M & \\  0 & & &  \end{matrix}\right) \;\text{ et }\;{\left\lbrack  g\right\rbrack  }_{B} = \left( \begin{matrix} \frac{\beta }{0} &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & N & \\  0 & & &  \end{matrix}\right) .
\]

Comme \( {P}_{f} = \left( {\alpha - X}\right) {P}_{M},{P}_{M} \) est comme \( {P}_{f} \) scindé sur \( \mathbb{K} \) , donc \( M \) est trigonalisable. De même, \( N \) est trigonalisable. Or \( {fg} = {gf} \) , donc \( {\left\lbrack f\right\rbrack }_{B}{\left\lbrack g\right\rbrack }_{B} = {\left\lbrack g\right\rbrack }_{B}{\left\lbrack f\right\rbrack }_{B} \) , ce qui s’écrit

> Since \( {P}_{f} = \left( {\alpha - X}\right) {P}_{M},{P}_{M} \) is like \( {P}_{f} \) split over \( \mathbb{K} \) , therefore \( M \) is trigonalizable. Similarly, \( N \) is trigonalizable. Now \( {fg} = {gf} \) , so \( {\left\lbrack f\right\rbrack }_{B}{\left\lbrack g\right\rbrack }_{B} = {\left\lbrack g\right\rbrack }_{B}{\left\lbrack f\right\rbrack }_{B} \) , which is written

\[
\left( \begin{matrix}  \times  &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & {MN} & \\  0 & & &  \end{matrix}\right)  = \left( \begin{matrix}  \times  &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & {NM} & \\  0 & & &  \end{matrix}\right)
\]

et donc \( {MN} = {NM} \) . Soit \( {B}_{1} = \left( {{e}_{2},\ldots ,{e}_{n}}\right) \) et \( H = \operatorname{Vect}{B}_{1} \) , hyperplan de \( E \) . On note \( p \) la projection sur \( H \) parallèlement à \( \mathbb{K}x \) . Soit \( {f}_{1} = p \circ {f}_{\mid H} \) et \( {g}_{1} = p \circ {g}_{\mid H} \in \mathcal{L}\left( H\right) \) . Comme \( {\left\lbrack {f}_{1}\right\rbrack }_{{B}_{1}} = M \) et \( {\left\lbrack {g}_{1}\right\rbrack }_{{B}_{1}} = N,{f}_{1} \) et \( {g}_{1} \) commutent donc d’après l’hypothèse de récurrence, il existe une base \( {B}_{1} \) de \( H \) qui trigonalise à la fois \( {f}_{1} \) et \( {g}_{1} \) . Dans la base \( {B}^{\prime } = \left( {x,{B}_{1}}\right) \) on a

> and thus \( {MN} = {NM} \) . Let \( {B}_{1} = \left( {{e}_{2},\ldots ,{e}_{n}}\right) \) and \( H = \operatorname{Vect}{B}_{1} \) , a hyperplane of \( E \) . We denote by \( p \) the projection onto \( H \) parallel to \( \mathbb{K}x \) . Let \( {f}_{1} = p \circ {f}_{\mid H} \) and \( {g}_{1} = p \circ {g}_{\mid H} \in \mathcal{L}\left( H\right) \) . Since \( {\left\lbrack {f}_{1}\right\rbrack }_{{B}_{1}} = M \) and \( {\left\lbrack {g}_{1}\right\rbrack }_{{B}_{1}} = N,{f}_{1} \) and \( {g}_{1} \) commute, then by the induction hypothesis, there exists a basis \( {B}_{1} \) of \( H \) that trigonalizes both \( {f}_{1} \) and \( {g}_{1} \) . In the basis \( {B}^{\prime } = \left( {x,{B}_{1}}\right) \) we have

\[
{\left\lbrack  f\right\rbrack  }_{{B}^{\prime }} = \left( \begin{matrix}  \times  &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & {\left\lbrack  {f}_{1}\right\rbrack  }_{{B}_{1}} & \\  0 & & &  \end{matrix}\right)
\]

ce qui montre que \( {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) est triangulaire supérieure. De même \( {\left\lbrack g\right\rbrack }_{{B}^{\prime }} \) est triangulaire supérieure, d'où le résultat.

> which shows that \( {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) is upper triangular. Similarly, \( {\left\lbrack g\right\rbrack }_{{B}^{\prime }} \) is upper triangular, hence the result.

Remarque 11. - La formulation matricielle de ces deux théorèmes est la suivante : Soient \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) diagonalisables (resp. trigonalisables) telles que \( {AB} = {BA} \) . Alors il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) telle que \( {P}^{-1}{AP} \) et \( {P}^{-1}{BP} \) soient diagonales (resp. triangulaires supérieures).

> Remark 11. - The matrix formulation of these two theorems is as follows: Let \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be diagonalizable (resp. trigonalizable) such that \( {AB} = {BA} \) . Then there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) such that \( {P}^{-1}{AP} \) and \( {P}^{-1}{BP} \) are diagonal (resp. upper triangular).

— La première méthode des démonstrations des théorèmes 3 et 5 montre l'intérêt de l’utilisation des applications transposées \( {}^{\mathrm{t}}f \in \mathcal{L}\left( {E}^{ * }\right) \) dans les raisonnements par récurrence (voir la partie 4 page 132 du chapitre III). Ce procédé est à retenir !

> — The first method of the proofs of theorems 3 and 5 shows the value of using transposed maps \( {}^{\mathrm{t}}f \in \mathcal{L}\left( {E}^{ * }\right) \) in inductive reasoning (see part 4 page 132 of chapter III). This process is worth remembering!
