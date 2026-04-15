### 5. Problems

*Français : 5. Problèmes*

Problem 1. Résoudre sur \( {\mathbb{R}}^{+ * } \) l’équation différentielle \( \left( E\right) : {y}^{\prime }\log t + {2t}{y}^{2} - y/t = 0 \) . Étant donné \( {y}_{0} \in \mathbb{R} \) ,étudier l’existence de solutions \( y \) de \( \left( E\right) \) définies sur \( {\mathbb{R}}^{+ * } \) telles que \( y\left( 1\right) = {y}_{0}. \)

> Problem 1. Solve the differential equation \( \left( E\right) : {y}^{\prime }\log t + {2t}{y}^{2} - y/t = 0 \) on \( {\mathbb{R}}^{+ * } \) . Given \( {y}_{0} \in \mathbb{R} \) , study the existence of solutions \( y \) to \( \left( E\right) \) defined on \( {\mathbb{R}}^{+ * } \) such that \( y\left( 1\right) = {y}_{0}. \)

Solution. L’équation différentielle \( \left( E\right) \) est résolue sur chacun des intervalles \( \rbrack 0,1\left\lbrack \text{ ou }\right\rbrack 1, + \infty \lbrack \) . Nous nous plaçons donc sur l'un de ces intervalles.

> Solution. The differential equation \( \left( E\right) \) is solved on each of the intervals \( \rbrack 0,1\left\lbrack \text{ ou }\right\rbrack 1, + \infty \lbrack \) . We therefore restrict ourselves to one of these intervals.

La forme de \( \left( E\right) \) nous invite à poser \( y = z\log t \) . En remplaçant dans \( \left( E\right) \) , on obtient fa-cilement \( \left( {E}^{\prime }\right) : {z}^{\prime } + {2t}{z}^{2} = 0 \) . Il s’agit d’une équation de Ricatti. Le théorème de Cauchy-Lipschitz nous dit qu’en dehors de la solution nulle, aucune solution \( z \) de \( \left( {E}^{\prime }\right) \) ne s’annule. Ainsi, si \( z \) n’est pas la solution nulle, \( \left( {E}^{\prime }\right) \) peut s’écrire \( {z}^{\prime }/{z}^{2} = - {2t} \) , donc par intégration, on a \( 1/z = - {t}^{2} + c \) , où \( c \) est une constante réelle. Autrement dit, les solutions de \( \left( {E}^{\prime }\right) \) sont celles de la forme \( z\left( t\right) = {\left( {t}^{2} - c\right) }^{-1} \) ou la fonction nulle.

> The form of \( \left( E\right) \) invites us to set \( y = z\log t \) . By substituting into \( \left( E\right) \) , we easily obtain \( \left( {E}^{\prime }\right) : {z}^{\prime } + {2t}{z}^{2} = 0 \) . This is a Riccati equation. The Cauchy-Lipschitz theorem tells us that, apart from the zero solution, no solution \( z \) of \( \left( {E}^{\prime }\right) \) vanishes. Thus, if \( z \) is not the zero solution, \( \left( {E}^{\prime }\right) \) can be written as \( {z}^{\prime }/{z}^{2} = - {2t} \) , so by integration, we have \( 1/z = - {t}^{2} + c \) , where \( c \) is a real constant. In other words, the solutions of \( \left( {E}^{\prime }\right) \) are those of the form \( z\left( t\right) = {\left( {t}^{2} - c\right) }^{-1} \) or the zero function.

Ainsi, si \( y \) est une solution de \( \left( E\right) \) sur \( {\mathbb{R}}^{+ * } \) , en notant \( {I}_{1} = \rbrack 0,1\left\lbrack {\text{ et }{I}_{2} = }\right\rbrack 1, + \infty \lbrack \) , on a pour tout \( k \in \{ 1,2\} \)

> Thus, if \( y \) is a solution of \( \left( E\right) \) on \( {\mathbb{R}}^{+ * } \) , by denoting \( {I}_{1} = \rbrack 0,1\left\lbrack {\text{ et }{I}_{2} = }\right\rbrack 1, + \infty \lbrack \) , we have for all \( k \in \{ 1,2\} \)

\[
\exists {c}_{k} \in  \mathbb{R},\forall t \in  {I}_{k},\;y\left( t\right)  = \frac{\log t}{{t}^{2} - {c}_{k}},
\]

(*)

> ou bien \( y \) est identiquement nulle sur \( {I}_{k} \) .

or \( y \) is identically zero on \( {I}_{k} \) .

> Si \( y \) est du type (*) sur \( {I}_{k} \) , on doit nécessairement avoir \( {c}_{1} \geq 1 \) ou \( {c}_{1} \leq 0 \) (pour \( k = 1 \) ), et \( {c}_{2} \leq 1 \) (pour \( k = 2 \) ).

If \( y \) is of type (*) on \( {I}_{k} \) , we must necessarily have \( {c}_{1} \geq 1 \) or \( {c}_{1} \leq 0 \) (for \( k = 1 \) ), and \( {c}_{2} \leq 1 \) (for \( k = 2 \) ).

> (i) De plus, si \( {c}_{1} \neq 1 \) (resp. \( {c}_{2} \neq 1 \) ), on a \( y\left( 1\right) = 0 \) et la dérivée à gauche (resp. à droite) de \( y \) en 1 est \( {y}_{\mathrm{g}}^{\prime }\left( 1\right) = {\left( 1 - {c}_{1}\right) }^{-1} \) (resp. \( {y}_{\mathrm{d}}^{\prime }\left( 1\right) = {\left( 1 - {c}_{2}\right) }^{-1} \) ).

(i) Furthermore, if \( {c}_{1} \neq 1 \) (resp. \( {c}_{2} \neq 1 \) ), we have \( y\left( 1\right) = 0 \) and the left (resp. right) derivative of \( y \) at 1 is \( {y}_{\mathrm{g}}^{\prime }\left( 1\right) = {\left( 1 - {c}_{1}\right) }^{-1} \) (resp. \( {y}_{\mathrm{d}}^{\prime }\left( 1\right) = {\left( 1 - {c}_{2}\right) }^{-1} \) ).

> (ii) Si \( {c}_{1} = 1 \) (resp. \( {c}_{2} = 1 \) ), on a facilement \( y\left( 1\right) = 1/2 \) .

(ii) If \( {c}_{1} = 1 \) (resp. \( {c}_{2} = 1 \) ), we easily have \( y\left( 1\right) = 1/2 \) .

> Traitons maintenant plusieurs cas selon la forme de \( y \) sur \( {I}_{1} \) .

Let us now treat several cases according to the form of \( y \) on \( {I}_{1} \) .

> - Si \( y \) est identiquement nulle sur \( {I}_{1} \) , alors nécessairement \( y \) est identiquement nulle sur \( {I}_{2} \) (d’après (i) et (ii)), donc \( y \) est identiquement nulle sur \( {\mathbb{R}}^{+ * } \) .

- If \( y \) is identically zero on \( {I}_{1} \) , then necessarily \( y \) is identically zero on \( {I}_{2} \) (according to (i) and (ii)), so \( y \) is identically zero on \( {\mathbb{R}}^{+ * } \) .

> - Si \( y \) est du type (*) avec \( {c}_{1} \neq  1 \) , alors nécessairement (d’après (i) et (ii)), \( y \) est du type (*) sur \( {I}_{2} \) avec \( {c}_{2} \neq  1 \) et l’égalité des dérivées à gauche et à droite de \( f \) en 1 donne \( {c}_{1} = {c}_{2} \) , et vues les conditions imposées à \( {c}_{1} \) et \( {c}_{2} \) , on a nécessairement \( {c}_{1} = {c}_{2} \leq  0 \) .

- If \( y \) is of type (*) with \( {c}_{1} \neq  1 \) , then necessarily (according to (i) and (ii)), \( y \) is of type (*) on \( {I}_{2} \) with \( {c}_{2} \neq  1 \) and the equality of the left and right derivatives of \( f \) at 1 gives \( {c}_{1} = {c}_{2} \) , and given the conditions imposed on \( {c}_{1} \) and \( {c}_{2} \) , we necessarily have \( {c}_{1} = {c}_{2} \leq  0 \) .

> - Si \( y \) est du type (*) avec \( {c}_{1} = 1 \) , alors \( y \) est nécessairement du type (*) sur \( {I}_{2} \) avec \( {c}_{2} = 1 \) . Dans ce cas, on a \( y\left( t\right)  = \log t/\left( {{t}^{2} - 1}\right) \) pour tout \( t \neq  1, y\left( 1\right)  = 1/2 \) , et on vérifie facilement que \( y \) est dérivable en 1 .

- If \( y \) is of type (*) with \( {c}_{1} = 1 \) , then \( y \) is necessarily of type (*) on \( {I}_{2} \) with \( {c}_{2} = 1 \) . In this case, we have \( y\left( t\right)  = \log t/\left( {{t}^{2} - 1}\right) \) for all \( t \neq  1, y\left( 1\right)  = 1/2 \) , and it is easily verified that \( y \) is differentiable at 1 .

> Finalement, les solutions sur \( {\mathbb{R}}^{+ * } \) de \( \left( E\right) \) sont

Finally, the solutions on \( {\mathbb{R}}^{+ * } \) of \( \left( E\right) \) are

> - la fonction nulle ;

- the zero function;

> - les fonctions de la forme \( t \mapsto  \log t/\left( {{t}^{2} - c}\right) , c \leq  0 \) ;

- functions of the form \( t \mapsto  \log t/\left( {{t}^{2} - c}\right) , c \leq  0 \) ;

> - la fonction \( t \mapsto  \log t/\left( {{t}^{2} - 1}\right) \) si \( t \neq  1,1 \mapsto  1/2 \) .

- the function \( t \mapsto  \log t/\left( {{t}^{2} - 1}\right) \) if \( t \neq  1,1 \mapsto  1/2 \) .

> Si \( {y}_{0} \in \mathbb{R} \) est donné, on en déduit qu’il n’y a de solution \( y \) sur \( {\mathbb{R}}^{+ * } \) vérifiant \( y\left( 1\right) = {y}_{0} \) si et seulement si \( {y}_{0} \in \{ 0,1/2\} \) . Si \( {y}_{0} = 0 \) , il y a une infinité de solutions ; si \( {y}_{0} = 1/2 \) , il n’y a qu’une seule solution.

If \( {y}_{0} \in \mathbb{R} \) is given, we deduce that there is a solution \( y \) on \( {\mathbb{R}}^{+ * } \) satisfying \( y\left( 1\right) = {y}_{0} \) if and only if \( {y}_{0} \in \{ 0,1/2\} \) . If \( {y}_{0} = 0 \) , there are infinitely many solutions; if \( {y}_{0} = 1/2 \) , there is only one solution.

> Problem 2. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une fonction continue. On suppose que l’équation différentielle \( \left( E\right) : {y}^{\prime } = f\left( y\right) \) admet une solution \( \varphi \) définie sur \( \mathbb{R} \) et bornée sur \( \mathbb{R} \) . Montrer qu’il existe \( {t}_{0} \in \mathbb{R} \) tel que \( f\left( {t}_{0}\right) = 0 \) .

Problem 2. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a continuous function. Suppose that the differential equation \( \left( E\right) : {y}^{\prime } = f\left( y\right) \) admits a solution \( \varphi \) defined on \( \mathbb{R} \) and bounded on \( \mathbb{R} \) . Show that there exists \( {t}_{0} \in \mathbb{R} \) such that \( f\left( {t}_{0}\right) = 0 \) .

> Solution. Raisonnons par l’absurde, en supposant \( f\left( t\right) \neq 0 \) pour tout \( t \in \mathbb{R} \) . Comme \( f \) est continue, \( f \) garde alors un signe constant sur \( \mathbb{R} \) , par exemple \( f\left( t\right) > 0 \) pour tout \( t \in \mathbb{R} \) .

Solution. Let us reason by contradiction, assuming \( f\left( t\right) \neq 0 \) for all \( t \in \mathbb{R} \) . Since \( f \) is continuous, \( f \) then maintains a constant sign on \( \mathbb{R} \) , for example \( f\left( t\right) > 0 \) for all \( t \in \mathbb{R} \) .

> Ainsi, pour tout \( t \in \mathbb{R},{\varphi }^{\prime }\left( t\right) = f\left( {\varphi \left( t\right) }\right) > 0 \) . Donc \( \varphi \) est strictement croissante. De plus \( \varphi \) est bornée, elle converge donc en \( + \infty \) . Soit \( \ell \) sa limite. En faisant tendre \( t \) vers \( + \infty \) dans \( {\varphi }^{\prime }\left( t\right) = f\left( {\varphi \left( t\right) }\right) \) , on en déduit, par continuité de \( f \) , que \( {\varphi }^{\prime } \) converge vers \( {\ell }^{\prime } = f\left( \ell \right) > 0 \) en \( + \infty \) . La fonction \( {\varphi }^{\prime } \) est continue et vérifie \( {\varphi }^{\prime }\left( t\right) \sim {\ell }^{\prime } \) , donc par intégration des équivalents, on en déduit que lorsque \( t \rightarrow + \infty ,\varphi \left( t\right) - \varphi \left( 0\right) \sim {\ell }^{\prime }t \) . Ceci est impossible car \( {\ell }^{\prime } \neq 0 \) et \( \varphi \) est bornée sur \( \mathbb{R} \) . D'où le résultat.

Thus, for all \( t \in \mathbb{R},{\varphi }^{\prime }\left( t\right) = f\left( {\varphi \left( t\right) }\right) > 0 \). Therefore \( \varphi \) is strictly increasing. Furthermore, \( \varphi \) is bounded, so it converges at \( + \infty \). Let \( \ell \) be its limit. By letting \( t \) tend to \( + \infty \) in \( {\varphi }^{\prime }\left( t\right) = f\left( {\varphi \left( t\right) }\right) \), we deduce, by continuity of \( f \), that \( {\varphi }^{\prime } \) converges to \( {\ell }^{\prime } = f\left( \ell \right) > 0 \) at \( + \infty \). The function \( {\varphi }^{\prime } \) is continuous and satisfies \( {\varphi }^{\prime }\left( t\right) \sim {\ell }^{\prime } \), so by integration of equivalents, we deduce that when \( t \rightarrow + \infty ,\varphi \left( t\right) - \varphi \left( 0\right) \sim {\ell }^{\prime }t \). This is impossible because \( {\ell }^{\prime } \neq 0 \) and \( \varphi \) is bounded on \( \mathbb{R} \). Hence the result.

> Problem 3 (Métheo 3 (Métheode d'Euler-Cauchy pour l'INTÉGRATION NUMÉRIQUE D'UNE ÉQUATION DIFFÉRENTIELLE). Soient \( T > 0, I = \left\lbrack {0, T}\right\rbrack \) , et \( f : I \times {\mathbb{R}}^{m} \rightarrow {\mathbb{R}}^{m} \) une fonction de classe \( {\mathcal{C}}^{1} \) . On suppose

Problem 3 (Euler-Cauchy method for the NUMERICAL INTEGRATION OF A DIFFERENTIAL EQUATION). Let \( T > 0, I = \left\lbrack {0, T}\right\rbrack \), and \( f : I \times {\mathbb{R}}^{m} \rightarrow {\mathbb{R}}^{m} \) be a function of class \( {\mathcal{C}}^{1} \). We assume

\[
\exists L > 0,\forall t \in  I,\forall x, y \in  {\mathbb{R}}^{m},\;\parallel f\left( {t, x}\right)  - f\left( {t, y}\right) \parallel  \leq  L\parallel x - y\parallel .
\]

Soit \( y : I \rightarrow {\mathbb{R}}^{m} \) une solution de l’équation différentielle \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \) . On se propose d’approcher numériquement \( y \) par la méthode dite d’Euler-Cauchy. Soit \( N \in {\mathbb{N}}^{ * } \) , \( h = T/N \) et pour tout \( n \in \{ 0,1,\ldots , N\} ,{t}_{n} = {nh} \) . On définit \( {y}_{0},{y}_{1},\ldots ,{y}_{N} \) par récurrence par

> Let \( y : I \rightarrow {\mathbb{R}}^{m} \) be a solution to the differential equation \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \). We propose to numerically approximate \( y \) using the so-called Euler-Cauchy method. Let \( N \in {\mathbb{N}}^{ * } \), \( h = T/N \) and for all \( n \in \{ 0,1,\ldots , N\} ,{t}_{n} = {nh} \). We define \( {y}_{0},{y}_{1},\ldots ,{y}_{N} \) by recurrence as

\[
{y}_{0} = y\left( 0\right) \;\text{ et }\;{y}_{n + 1} = {y}_{n} + {hf}\left( {{t}_{n},{y}_{n}}\right) .
\]

Pour tout \( n \in \{ 0,1,\ldots , N\} \) , on pose \( {e}_{n} = y\left( {t}_{n}\right) - {y}_{n} \) . On se propose de majorer \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} \) .

> For all \( n \in \{ 0,1,\ldots , N\} \), we set \( {e}_{n} = y\left( {t}_{n}\right) - {y}_{n} \). We propose to find an upper bound for \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} \).

Comme \( f \) est de classe \( {\mathcal{C}}^{1}, y \) est de classe \( {\mathcal{C}}^{2} \) , et on pose \( M = \sup \left\{ {\begin{Vmatrix}{{y}^{\prime \prime }\left( t\right) }\end{Vmatrix}, t \in I}\right\} \) . a) On pose \( {\varepsilon }_{n} = \left\lbrack {y\left( {t}_{n + 1}\right) - y\left( {t}_{n}\right) }\right\rbrack - {hf}\left( {{t}_{n}, y\left( {t}_{n}\right) }\right) \) . Montrer que pour tout \( n \in \{ 0,1,\ldots , N\} \) , \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq M{h}^{2}/2. \)

> Since \( f \) is of class \( {\mathcal{C}}^{1}, y \) is of class \( {\mathcal{C}}^{2} \), and we set \( M = \sup \left\{ {\begin{Vmatrix}{{y}^{\prime \prime }\left( t\right) }\end{Vmatrix}, t \in I}\right\} \). a) We set \( {\varepsilon }_{n} = \left\lbrack {y\left( {t}_{n + 1}\right) - y\left( {t}_{n}\right) }\right\rbrack - {hf}\left( {{t}_{n}, y\left( {t}_{n}\right) }\right) \). Show that for all \( n \in \{ 0,1,\ldots , N\} \), \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq M{h}^{2}/2. \)

b) En déduire

> b) Deduce

\[
\forall n \in  \{ 0,1,\ldots , N\} ,\;\begin{Vmatrix}{e}_{n}\end{Vmatrix} \leq  \frac{Mh}{2L}{e}^{L{t}_{n}}.
\]

Solution. a) On peut aussi écrire

> Solution. a) We can also write

\[
{\varepsilon }_{n} = \left\lbrack  {y\left( {t}_{n + 1}\right)  - y\left( {t}_{n}\right) }\right\rbrack   - h{y}^{\prime }\left( {t}_{n}\right)  = {\int }_{{t}_{n}}^{{t}_{n + 1}}\left\lbrack  {{y}^{\prime }\left( t\right)  - {y}^{\prime }\left( {t}_{n}\right) }\right\rbrack  {dt},
\]

et comme \( \begin{Vmatrix}{{y}^{\prime }\left( t\right) - {y}^{\prime }\left( {t}_{n}\right) }\end{Vmatrix} \leq M\left( {t - {t}_{n}}\right) \) , on en déduit \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq {\int }_{{t}_{n}}^{{t}_{n + 1}}M\left( {t - {t}_{n}}\right) {dt} = M{h}^{2}/2 \) .

> and since \( \begin{Vmatrix}{{y}^{\prime }\left( t\right) - {y}^{\prime }\left( {t}_{n}\right) }\end{Vmatrix} \leq M\left( {t - {t}_{n}}\right) \) , we deduce \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq {\int }_{{t}_{n}}^{{t}_{n + 1}}M\left( {t - {t}_{n}}\right) {dt} = M{h}^{2}/2 \) .

b) On commence par écrire

> b) We begin by writing

\[
{e}_{n + 1} - {e}_{n} = y\left( {t}_{n + 1}\right)  - y\left( {t}_{n}\right)  - \left( {{y}_{n + 1} - {y}_{n}}\right)  = {\varepsilon }_{n} + h\left\lbrack  {f\left( {{t}_{n}, y\left( {t}_{n}\right) }\right)  - f\left( {{t}_{n},{y}_{n}}\right) }\right\rbrack  ,
\]

donc

> therefore

\[
\begin{Vmatrix}{{e}_{n + 1} - {e}_{n}}\end{Vmatrix} \leq  \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} + {hL}\begin{Vmatrix}{e}_{n}\end{Vmatrix}\;\text{ d’où }\;\begin{Vmatrix}{e}_{n + 1}\end{Vmatrix} \leq  \left( {1 + {hL}}\right) \begin{Vmatrix}{e}_{n}\end{Vmatrix} + \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix}.
\]

Maintenant, avec les inégalités \( 1 + {hL} \leq {e}^{hL} \) et \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq M{h}^{2}/2 \) , on en déduit \( \begin{Vmatrix}{e}_{n + 1}\end{Vmatrix} \leq {e}^{hL}\begin{Vmatrix}{e}_{n}\end{Vmatrix} + \; M{h}^{2}/2 \) , et une récurrence sur \( n \) donne

> Now, with the inequalities \( 1 + {hL} \leq {e}^{hL} \) and \( \begin{Vmatrix}{\varepsilon }_{n}\end{Vmatrix} \leq M{h}^{2}/2 \) , we deduce \( \begin{Vmatrix}{e}_{n + 1}\end{Vmatrix} \leq {e}^{hL}\begin{Vmatrix}{e}_{n}\end{Vmatrix} + \; M{h}^{2}/2 \) , and an induction on \( n \) gives

\[
\begin{Vmatrix}{e}_{n}\end{Vmatrix} \leq  {e}^{nhL}\begin{Vmatrix}{e}_{0}\end{Vmatrix} + \left( {1 + {e}^{hL} + \cdots  + {e}^{\left( {n - 1}\right) {hL}}}\right) M\frac{{h}^{2}}{2}.
\]

Comme \( {e}_{0} = 0 \) , ceci s’écrit aussi

> Since \( {e}_{0} = 0 \) , this can also be written

\[
\begin{Vmatrix}{e}_{n}\end{Vmatrix} \leq  \left( {1 + {e}^{hL} + \cdots  + {e}^{\left( {n - 1}\right) {hL}}}\right) M\frac{{h}^{2}}{2} = \frac{{e}^{nhL} - 1}{{e}^{hL} - 1}M\frac{{h}^{2}}{2} \leq  \frac{{e}^{nhL}}{hL}M\frac{{h}^{2}}{2} = {e}^{L{t}_{n}}\frac{Mh}{2L},
\]

et c'est terminé.

> and that is the end.

Problem 4. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une fonction continue, impaire, strictement positive sur \( {\mathbb{R}}^{+ * } \) . On considère l’équation différentielle \( \left( E\right) : {x}^{\prime \prime } + f\left( x\right) = 0 \) (équation d’un point matériel soumis à un champ de forces contraire à sa position).

> Problem 4. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a continuous, odd, strictly positive function on \( {\mathbb{R}}^{+ * } \) . Consider the differential equation \( \left( E\right) : {x}^{\prime \prime } + f\left( x\right) = 0 \) (equation of a material point subject to a force field opposing its position).

a) Montrer que les solutions maximales de \( \left( E\right) \) sont définies sur \( \mathbb{R} \) .

> a) Show that the maximal solutions of \( \left( E\right) \) are defined on \( \mathbb{R} \) .

b) Soit \( x \) une solution de \( \left( E\right) \) vérifiant les conditions initiales \( x\left( 0\right) = {x}_{0} > 0,{x}^{\prime }\left( 0\right) = 0 \) . Montrer que \( x \) est une fonction périodique et exprimer sa période.

> b) Let \( x \) be a solution of \( \left( E\right) \) satisfying the initial conditions \( x\left( 0\right) = {x}_{0} > 0,{x}^{\prime }\left( 0\right) = 0 \) . Show that \( x \) is a periodic function and express its period.

Solution. a) Soit \( x \) une solution maximale de \( \left( E\right) \) , et soit \( \rbrack a, b\left\lbrack \text{ son intervalle de définition. On a }\right\rbrack \; {x}^{\prime }{x}^{\prime \prime } + {x}^{\prime }f\left( x\right) = 0 \) , donc par intégration, on obtient l’existence d’une constante \( K \in \mathbb{R} \) telle que

> Solution. a) Let \( x \) be a maximal solution of \( \left( E\right) \) , and let \( \rbrack a, b\left\lbrack \text{ son intervalle de définition. On a }\right\rbrack \; {x}^{\prime }{x}^{\prime \prime } + {x}^{\prime }f\left( x\right) = 0 \) , so by integration, we obtain the existence of a constant \( K \in \mathbb{R} \) such that

\[
\forall t \in  \rbrack a, b\left\lbrack  {,\;\frac{{x}^{\prime }{\left( t\right) }^{2}}{2} + F\left( {x\left( t\right) }\right)  = K,\;\text{ où }\;F\left( u\right)  = {\int }_{0}^{u}f\left( t\right) {dt}.}\right.
\]

(*)

> (l'interprétation physique de ce résultat est la conservation de l'énergie cinétique ajoutée à l'énergie potentielle). La fonction \( F \) , primitive d’une fonction impaire, est paire. Par ailleurs, \( {F}^{\prime }\left( t\right) = f\left( t\right) \geq 0 \) sur \( {\mathbb{R}}^{ + } \) , et comme \( F\left( 0\right) = 0, F \) est positive sur \( {\mathbb{R}}^{ + } \) , donc sur \( \mathbb{R} \) .

(the physical interpretation of this result is the conservation of kinetic energy added to potential energy). The function \( F \) , an antiderivative of an odd function, is even. Furthermore, \( {F}^{\prime }\left( t\right) = f\left( t\right) \geq 0 \) on \( {\mathbb{R}}^{ + } \) , and since \( F\left( 0\right) = 0, F \) is positive on \( {\mathbb{R}}^{ + } \) , therefore on \( \mathbb{R} \) .

> Donc \( {x}^{\prime }{\left( t\right) }^{2}/2 = K - F\left( {x\left( t\right) }\right) \leq K \) est majorée, donc \( {x}^{\prime } \) est bornée. Si \( b < + \infty \) , on en déduit, d’après l’inégalité des accroissements finis, que \( x \) est bornée au voisinage de \( b \) . Le vecteur \( V = \left( \begin{matrix} x \\ {x}^{\prime } \end{matrix}\right) \) est donc borné au voisinage de \( b \) . Par ailleurs, \( V \) est solution de l’équation différentielle du premier ordre \( {X}^{\prime } + g\left( X\right) = 0 \) , où \( g\left( \begin{matrix} x \\ y \end{matrix}\right) = \left( \begin{matrix} - y \\ f\left( x\right) \end{matrix}\right) \) , le principe de majoration a priori (voir le théorème 1 page 400 ou l’exercice 1 page 401) entraîne que \( V \) n’est pas borné au voisinage de \( b \) , ce qui est absurde. On a donc \( b = + \infty \) . On montrerait de même que \( a = - \infty \) .

Thus \( {x}^{\prime }{\left( t\right) }^{2}/2 = K - F\left( {x\left( t\right) }\right) \leq K \) is bounded above, so \( {x}^{\prime } \) is bounded. If \( b < + \infty \) , we deduce from the mean value inequality that \( x \) is bounded in the neighborhood of \( b \) . The vector \( V = \left( \begin{matrix} x \\ {x}^{\prime } \end{matrix}\right) \) is therefore bounded in the neighborhood of \( b \) . Furthermore, \( V \) is a solution to the first-order differential equation \( {X}^{\prime } + g\left( X\right) = 0 \) , where \( g\left( \begin{matrix} x \\ y \end{matrix}\right) = \left( \begin{matrix} - y \\ f\left( x\right) \end{matrix}\right) \) , the principle of a priori bounds (see theorem 1 on page 400 or exercise 1 on page 401) implies that \( V \) is not bounded in the neighborhood of \( b \) , which is absurd. We therefore have \( b = + \infty \) . We would show similarly that \( a = - \infty \) .

> b) En faisant \( t = 0 \) dans (*) on obtient \( K = F\left( {x}_{0}\right) \) , donc

b) By setting \( t = 0 \) in (*) we obtain \( K = F\left( {x}_{0}\right) \) , therefore

\[
\forall t \in  \mathbb{R},\;\frac{{x}^{\prime }{\left( t\right) }^{2}}{2} = F\left( {x}_{0}\right)  - F\left( {x\left( t\right) }\right) .
\]

\( \left( {* * }\right) \)

> On a \( {x}^{\prime \prime }\left( 0\right) = - f\left( {x}_{0}\right) < 0 \) , et comme \( {x}^{\prime }\left( 0\right) = 0 \) , il existe \( \varepsilon > 0 \) tel que \( {x}^{\prime }\left( t\right) < 0 \) sur \( \rbrack 0,\varepsilon \lbrack \) . Ainsi, l’ensemble \( \Gamma = \left\{ {t > 0\mid \forall u \in \rbrack 0, t\lbrack ,{x}^{\prime }\left( u\right) < 0}\right\} \) est non vide. Notons \( {t}_{0} = \sup \Gamma \) . On a \( {x}^{\prime }\left( t\right) < 0 \) pour tout \( t \in \rbrack 0,{t}_{0}\left\lbrack \right. \) , et d’après (**), on a \( F\left( {x\left( t\right) }\right) < F\left( {x}_{0}\right) \) pour tout \( t \in \rbrack 0,{t}_{0}\lbrack \) . Comme \( F \) est croissante sur \( {\mathbb{R}}^{ + } \) et paire, on en déduit \( \left| {x\left( t\right) }\right| < {x}_{0} \) pour tout \( t \in \rbrack 0,{t}_{0}\lbrack \) .

We have \( {x}^{\prime \prime }\left( 0\right) = - f\left( {x}_{0}\right) < 0 \) , and since \( {x}^{\prime }\left( 0\right) = 0 \) , there exists \( \varepsilon > 0 \) such that \( {x}^{\prime }\left( t\right) < 0 \) on \( \rbrack 0,\varepsilon \lbrack \) . Thus, the set \( \Gamma = \left\{ {t > 0\mid \forall u \in \rbrack 0, t\lbrack ,{x}^{\prime }\left( u\right) < 0}\right\} \) is non-empty. Let \( {t}_{0} = \sup \Gamma \) . We have \( {x}^{\prime }\left( t\right) < 0 \) for all \( t \in \rbrack 0,{t}_{0}\left\lbrack \right. \) , and according to (**), we have \( F\left( {x\left( t\right) }\right) < F\left( {x}_{0}\right) \) for all \( t \in \rbrack 0,{t}_{0}\lbrack \) . Since \( F \) is increasing on \( {\mathbb{R}}^{ + } \) and even, we deduce \( \left| {x\left( t\right) }\right| < {x}_{0} \) for all \( t \in \rbrack 0,{t}_{0}\lbrack \) .

> Maintenant, l'équation (**) entraîne

Now, equation (**) implies

\[
\forall t \in  \rbrack 0,{t}_{0}\left\lbrack  {,\;\frac{{x}^{\prime }\left( t\right) }{\sqrt{2\left( {F\left( {x}_{0}\right)  - F\left( {x\left( t\right) }\right) }\right) }} =  - 1\;\text{ donc }\;t = {\int }_{x\left( t\right) }^{{x}_{0}}\frac{du}{\sqrt{2\left( {F\left( {x}_{0}\right)  - F\left( u\right) }\right) }}}\right.
\]

\( \left( {* * * }\right) \)

> (l’intégrale est bien convergente car au voisinage de \( {x}_{0}^{ - }, F\left( {x}_{0}\right) - F\left( u\right) \sim \left( {{x}_{0} - u}\right) f\left( {x}_{0}\right) \) donc \( \sqrt{F\left( {x}_{0}\right) - F\left( u\right) } \sim \sqrt{f\left( {x}_{0}\right) }\sqrt{{x}_{0} - u} \) ). Par ailleurs, l’intégrale

(the integral is indeed convergent because in the neighborhood of \( {x}_{0}^{ - }, F\left( {x}_{0}\right) - F\left( u\right) \sim \left( {{x}_{0} - u}\right) f\left( {x}_{0}\right) \) , therefore \( \sqrt{F\left( {x}_{0}\right) - F\left( u\right) } \sim \sqrt{f\left( {x}_{0}\right) }\sqrt{{x}_{0} - u} \) ). Furthermore, the integral

\[
{T}_{0} = {\int }_{-{x}_{0}}^{{x}_{0}}\frac{du}{\sqrt{2\left( {F\left( {x}_{0}\right)  - F\left( u\right) }\right) }}
\]

converge (la fonction \( F \) est paire), et comme son intégrande est positive et que \( \left| {x\left( t\right) }\right| < {x}_{0} \) pour tout \( t \in \rbrack 0,{t}_{0}\left\lbrack {,\left( {* * * }\right) \text{ entraîne }t < {T}_{0}\text{ pour tout }t \in }\right\rbrack 0,{t}_{0}\left\lbrack {\text{ , donc }{t}_{0} \leq {T}_{0}}\right. \) . Ainsi, \( {t}_{0} \) est fini. Par continuité de \( {x}^{\prime } \) on a \( {x}^{\prime }\left( {t}_{0}\right) = 0 \) , donc \( F\left( {x\left( {t}_{0}\right) }\right) = F\left( {x}_{0}\right) \) d’après (**), et comme \( F \) est paire, strictement croissante sur \( {\mathbb{R}}^{ + } \) , ceci entraîne \( \left| {x\left( {t}_{0}\right) }\right| = {x}_{0} \) . De plus, \( x \) est strictement décroissante sur \( \rbrack 0,{t}_{0}\left\lbrack \right. \) , donc \( x\left( {t}_{0}\right) < {x}_{0} \) , donc la seule possibilité est \( x\left( {t}_{0}\right) = - {x}_{0} \) . En faisant maintenant tendre \( t \) vers \( {t}_{0} \) par valeurs inférieures dans (***), on en déduit \( {t}_{0} = {T}_{0} \) .

> converges (the function \( F \) is even), and since its integrand is positive and \( \left| {x\left( t\right) }\right| < {x}_{0} \) for all \( t \in \rbrack 0,{t}_{0}\left\lbrack {,\left( {* * * }\right) \text{ entraîne }t < {T}_{0}\text{ pour tout }t \in }\right\rbrack 0,{t}_{0}\left\lbrack {\text{ , donc }{t}_{0} \leq {T}_{0}}\right. \). Thus, \( {t}_{0} \) is finite. By continuity of \( {x}^{\prime } \) we have \( {x}^{\prime }\left( {t}_{0}\right) = 0 \), so \( F\left( {x\left( {t}_{0}\right) }\right) = F\left( {x}_{0}\right) \) according to (**), and since \( F \) is even, strictly increasing on \( {\mathbb{R}}^{ + } \), this implies \( \left| {x\left( {t}_{0}\right) }\right| = {x}_{0} \). Furthermore, \( x \) is strictly decreasing on \( \rbrack 0,{t}_{0}\left\lbrack \right. \), so \( x\left( {t}_{0}\right) < {x}_{0} \), therefore the only possibility is \( x\left( {t}_{0}\right) = - {x}_{0} \). Now, by letting \( t \) tend to \( {t}_{0} \) from below in (***), we deduce \( {t}_{0} = {T}_{0} \).

Considérons maintenant la fonction \( y : t \mapsto - x\left( {t + {T}_{0}}\right) \) . On a \( y\left( 0\right) = - x\left( {t}_{0}\right) = {x}_{0},{y}^{\prime }\left( 0\right) = \; - {x}^{\prime }\left( {t}_{0}\right) = 0 \) , et comme \( f \) est impaire, \( y \) est solution de \( \left( E\right) \) . D’après le théorème de Cauchy-Lipschitz, il y a unicité au problème de Cauchy, et comme \( x \) et \( y \) ont les mêmes conditions initiales en 0, on a \( x = y \) sur \( \mathbb{R} \) . En d’autres termes, \( x\left( t\right) = - x\left( {t + {T}_{0}}\right) \) pour tout \( t \in \mathbb{R} \) . On en déduit \( x\left( t\right) = - x\left( {t + {T}_{0}}\right) = x\left( {t + 2{T}_{0}}\right) \) . Donc \( x \) est \( 2{T}_{0} \) -périodique. La fonction \( x \) n’admet pas de période plus petite, car nous avons montré \( x\left( t\right) < x\left( 0\right) \) sur \( \rbrack 0,{T}_{0}\rbrack \) et sur \( \rbrack {T}_{0},2{T}_{0}\lbrack , x\left( t\right) \mid = \; \left| {x\left( {t - {T}_{0}}\right) }\right| < x\left( 0\right) \) , donc finalement, \( x\left( t\right) \neq x\left( 0\right) \) sur \( \rbrack 0,2{T}_{0}\lbrack \) .

> Let us now consider the function \( y : t \mapsto - x\left( {t + {T}_{0}}\right) \). We have \( y\left( 0\right) = - x\left( {t}_{0}\right) = {x}_{0},{y}^{\prime }\left( 0\right) = \; - {x}^{\prime }\left( {t}_{0}\right) = 0 \), and since \( f \) is odd, \( y \) is a solution to \( \left( E\right) \). According to the Cauchy-Lipschitz theorem, there is uniqueness for the Cauchy problem, and since \( x \) and \( y \) have the same initial conditions at 0, we have \( x = y \) on \( \mathbb{R} \). In other words, \( x\left( t\right) = - x\left( {t + {T}_{0}}\right) \) for all \( t \in \mathbb{R} \). We deduce \( x\left( t\right) = - x\left( {t + {T}_{0}}\right) = x\left( {t + 2{T}_{0}}\right) \). Thus \( x \) is \( 2{T}_{0} \)-periodic. The function \( x \) does not admit a smaller period, because we have shown \( x\left( t\right) < x\left( 0\right) \) on \( \rbrack 0,{T}_{0}\rbrack \) and on \( \rbrack {T}_{0},2{T}_{0}\lbrack , x\left( t\right) \mid = \; \left| {x\left( {t - {T}_{0}}\right) }\right| < x\left( 0\right) \), so finally, \( x\left( t\right) \neq x\left( 0\right) \) on \( \rbrack 0,2{T}_{0}\lbrack \).

Remarque. On traite de la même manière l’équation du pendule \( L{\theta }^{\prime \prime } + g\sin \theta = 0 \) . Partant d’une vitesse nulle en \( \theta = {\theta }_{0} \) , le pendule a sa période égale à \( 2\sqrt{L/g}{\int }_{-{\theta }_{0}}^{{\theta }_{0}}\frac{d\theta }{\sqrt{2\left( {\cos \theta - \cos {\theta }_{0}}\right) }} \) .

> Remark. The pendulum equation is treated in the same way \( L{\theta }^{\prime \prime } + g\sin \theta = 0 \). Starting from zero velocity at \( \theta = {\theta }_{0} \), the pendulum has a period equal to \( 2\sqrt{L/g}{\int }_{-{\theta }_{0}}^{{\theta }_{0}}\frac{d\theta }{\sqrt{2\left( {\cos \theta - \cos {\theta }_{0}}\right) }} \).

Problem 5. Déterminer les solutions à valeurs réelles définies sur \( \mathbb{R} \) , deux fois dérivables, de l’équation différentielle \( \left( E\right) : y{y}^{\prime }{y}^{\prime \prime } = 0 \) .

> Problem 5. Determine the twice-differentiable real-valued solutions defined on \( \mathbb{R} \) for the differential equation \( \left( E\right) : y{y}^{\prime }{y}^{\prime \prime } = 0 \).

Solution. Soit \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) une fonction deux fois dérivable vérifiant \( \varphi {\varphi }^{\prime }{\varphi }^{\prime \prime } = 0 \) . On va montrer (on s’en doutait) que \( {\varphi }^{\prime \prime } = 0 \) , c’est-à-dire que \( \varphi \) est une fonction affine.

> Solution. Let \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) be a twice-differentiable function satisfying \( \varphi {\varphi }^{\prime }{\varphi }^{\prime \prime } = 0 \). We will show (as suspected) that \( {\varphi }^{\prime \prime } = 0 \), meaning that \( \varphi \) is an affine function.

Pour cela, raisonnons par l’absurde et supposons l’existence de \( {t}_{0} \in \mathbb{R} \) tel que \( {\varphi }^{\prime \prime }\left( {t}_{0}\right) \neq 0 \) . Quitte à considérer la fonction \( t \mapsto \varphi \left( {t + {t}_{0}}\right) \) , on peut même supposer \( {t}_{0} = 0 \) , de sorte que \( {\varphi }^{\prime \prime }\left( 0\right) \neq 0 \) .

> To do this, let us reason by contradiction and assume the existence of \( {t}_{0} \in \mathbb{R} \) such that \( {\varphi }^{\prime \prime }\left( {t}_{0}\right) \neq 0 \). By considering the function \( t \mapsto \varphi \left( {t + {t}_{0}}\right) \), we can even assume \( {t}_{0} = 0 \), such that \( {\varphi }^{\prime \prime }\left( 0\right) \neq 0 \).

Dans un premier temps, nous montrons l’existence d’un \( \alpha > 0 \) vérifiant \( {\varphi }^{\prime }\left( t\right) \neq 0 \) pour tout \( t \) tel que \( 0 < \left| t\right| < \alpha \) . Si \( {\varphi }^{\prime }\left( 0\right) \neq 0 \) , c’est évident par continuité de \( {\varphi }^{\prime } \) . Sinon, \( {\varphi }^{\prime }\left( 0\right) = 0 \) , et il suffit d’écrire \( {\varphi }^{\prime }\left( t\right) = {\varphi }^{\prime }\left( 0\right) + t{\varphi }^{\prime \prime }\left( 0\right) + o\left( t\right) = t\left\lbrack {{\varphi }^{\prime \prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) pour conclure.

> First, we show the existence of an \( \alpha > 0 \) satisfying \( {\varphi }^{\prime }\left( t\right) \neq 0 \) for all \( t \) such that \( 0 < \left| t\right| < \alpha \). If \( {\varphi }^{\prime }\left( 0\right) \neq 0 \), it is obvious by the continuity of \( {\varphi }^{\prime } \). Otherwise, \( {\varphi }^{\prime }\left( 0\right) = 0 \), and it suffices to write \( {\varphi }^{\prime }\left( t\right) = {\varphi }^{\prime }\left( 0\right) + t{\varphi }^{\prime \prime }\left( 0\right) + o\left( t\right) = t\left\lbrack {{\varphi }^{\prime \prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) to conclude.

Ensuite, nous montrons l’existence de \( \beta > 0 \) vérifiant \( \varphi \left( t\right) \neq 0 \) pour tout \( t \) tel que \( 0 < \left| t\right| < \beta \) . Si \( \varphi \left( 0\right) \neq 0 \) , c’est immédiat par continuité de \( \varphi \) . Sinon, \( \varphi \left( 0\right) = 0 \) . Si \( {\varphi }^{\prime }\left( 0\right) \neq 0 \) , il suffit d’écrire \( \varphi \left( t\right) = t\left\lbrack {{\varphi }^{\prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) , et si \( {\varphi }^{\prime }\left( 0\right) = 0 \) , on écrit \( \varphi \left( t\right) = \frac{{t}^{2}}{2}\left\lbrack {{\varphi }^{\prime \prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) pour conclure.

> Next, we show the existence of \( \beta > 0 \) satisfying \( \varphi \left( t\right) \neq 0 \) for all \( t \) such that \( 0 < \left| t\right| < \beta \) . If \( \varphi \left( 0\right) \neq 0 \) , it is immediate by the continuity of \( \varphi \) . Otherwise, \( \varphi \left( 0\right) = 0 \) . If \( {\varphi }^{\prime }\left( 0\right) \neq 0 \) , it suffices to write \( \varphi \left( t\right) = t\left\lbrack {{\varphi }^{\prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) , and if \( {\varphi }^{\prime }\left( 0\right) = 0 \) , we write \( \varphi \left( t\right) = \frac{{t}^{2}}{2}\left\lbrack {{\varphi }^{\prime \prime }\left( 0\right) + o\left( 1\right) }\right\rbrack \) to conclude.

En posant maintenant \( \gamma = \inf \{ \alpha ,\beta \} \) , on a donc \( \varphi \left( t\right) {\varphi }^{\prime }\left( t\right) \neq 0 \) pour tout \( t \) tel que \( 0 < \left| t\right| < \gamma \) . Comme \( \varphi \) est solution de \( \left( E\right) \) , on en déduit \( {\varphi }^{\prime \prime }\left( t\right) = 0 \) pour tout \( t \) vérifiant \( 0 < \left| t\right| < \gamma \) .

> By setting \( \gamma = \inf \{ \alpha ,\beta \} \) now, we therefore have \( \varphi \left( t\right) {\varphi }^{\prime }\left( t\right) \neq 0 \) for all \( t \) such that \( 0 < \left| t\right| < \gamma \) . Since \( \varphi \) is a solution to \( \left( E\right) \) , we deduce \( {\varphi }^{\prime \prime }\left( t\right) = 0 \) for all \( t \) satisfying \( 0 < \left| t\right| < \gamma \) .

Pour montrer \( {\varphi }^{\prime \prime }\left( 0\right) = 0 \) , on pourrait maintenant conclure avec le théorème de Darboux. On peut s’en tirer autrement, en procédant comme suit. Comme \( {\varphi }^{\prime \prime } = 0 \) sur \( \rbrack 0,\gamma \lbrack ,{\varphi }^{\prime } \) est constante sur ] \( 0,\gamma \lbrack \) . De même, \( {\varphi }^{\prime } \) est constante sur \( \rbrack - \gamma ,0\lbrack \) . Par continuité de \( {\varphi }^{\prime } \) en \( 0,{\varphi }^{\prime } \) est donc constante sur \( \rbrack - \gamma ,\gamma \left\lbrack \right. \) , donc \( {\varphi }^{\prime \prime }\left( 0\right) = 0 \) . Ceci est contradictoire, d’où le résultat.

> To show \( {\varphi }^{\prime \prime }\left( 0\right) = 0 \) , we could now conclude using Darboux's theorem. We can manage otherwise by proceeding as follows. Since \( {\varphi }^{\prime \prime } = 0 \) on \( \rbrack 0,\gamma \lbrack ,{\varphi }^{\prime } \) is constant on ] \( 0,\gamma \lbrack \) . Similarly, \( {\varphi }^{\prime } \) is constant on \( \rbrack - \gamma ,0\lbrack \) . By the continuity of \( {\varphi }^{\prime } \) at \( 0,{\varphi }^{\prime } \) , it is therefore constant on \( \rbrack - \gamma ,\gamma \left\lbrack \right. \) , hence \( {\varphi }^{\prime \prime }\left( 0\right) = 0 \) . This is a contradiction, hence the result.

Problem 6. Soit \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que \( f\left( 0\right) = 0 \) . On suppose que pour tout \( x \in {\mathbb{R}}^{n} \) , la matrice jacobienne de \( f \) en \( x \) , notée \( {f}^{\prime }\left( x\right) \) , est symétrique définie négative.

> Problem 6. Let \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a function of class \( {\mathcal{C}}^{1} \) such that \( f\left( 0\right) = 0 \) . Suppose that for all \( x \in {\mathbb{R}}^{n} \) , the Jacobian matrix of \( f \) at \( x \) , denoted by \( {f}^{\prime }\left( x\right) \) , is symmetric negative definite.

Montrer que si \( Y : \mathbb{R} \rightarrow {\mathbb{R}}^{n} \) est une solution de l’équation différentielle \( {Y}^{\prime } = f\left( Y\right) \) , alors \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}Y\left( t\right) = 0 \) .

> Show that if \( Y : \mathbb{R} \rightarrow {\mathbb{R}}^{n} \) is a solution to the differential equation \( {Y}^{\prime } = f\left( Y\right) \) , then \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}Y\left( t\right) = 0 \) .

Solution. Soit \( X \in {\mathbb{R}}^{n}, X \neq 0 \) . En posant \( V : t \mapsto {}^{t}{Xf}\left( {tX}\right) \) , on a \( {V}^{\prime }\left( t\right) = {}^{t}X{f}^{\prime }\left( {tX}\right) X < 0 \) pour tout \( t \in \mathbb{R} \) (car \( {f}^{\prime }\left( {tX}\right) \) est définie négative). Ainsi \( V \) est strictement décroissante. Comme \( V\left( 0\right) = 0 \) , on en déduit \( V\left( 1\right) = {}^{t}{Xf}\left( X\right) < 0 \) . En résumé, nous avons montré

> Solution. Let \( X \in {\mathbb{R}}^{n}, X \neq 0 \) . By setting \( V : t \mapsto {}^{t}{Xf}\left( {tX}\right) \) , we have \( {V}^{\prime }\left( t\right) = {}^{t}X{f}^{\prime }\left( {tX}\right) X < 0 \) for all \( t \in \mathbb{R} \) (since \( {f}^{\prime }\left( {tX}\right) \) is negative definite). Thus \( V \) is strictly decreasing. As \( V\left( 0\right) = 0 \) , we deduce \( V\left( 1\right) = {}^{t}{Xf}\left( X\right) < 0 \) . In summary, we have shown

\[
\forall X \in  {\mathbb{R}}^{n}, X \neq  0,\;{}^{t}{Xf}\left( X\right)  < 0.
\]

(*)

> Ceci étant, posons \( \alpha : t \mapsto {}^{t}Y\left( t\right) Y\left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \) . On a

Given this, let us set \( \alpha : t \mapsto {}^{t}Y\left( t\right) Y\left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \) . We have

\[
\forall u \in  \mathbb{R},\;{\alpha }^{\prime }\left( u\right)  = {}^{t}{Y}^{\prime }\left( u\right) Y\left( u\right)  + {}^{t}Y\left( u\right) {Y}^{\prime }\left( u\right)  = {2}^{t}Y\left( u\right) {Y}^{\prime }\left( u\right)  = {2}^{t}Y\left( u\right) f\left( {Y\left( u\right) }\right) ,
\]

\( \left( {* * }\right) \)

> donc d’après (*), \( {\alpha }^{\prime }\left( u\right) \leq 0 \) pour tout \( u \in \mathbb{R} \) . Ainsi, la fonction \( \alpha \) est décroissante. Comme elle est positive, elle admet donc une limite \( \ell \in {\mathbb{R}}^{ + } \) en \( + \infty \) . Il s’agit de montrer \( \ell = 0 \) .

therefore, according to (*), \( {\alpha }^{\prime }\left( u\right) \leq 0 \) for all \( u \in \mathbb{R} \) . Thus, the function \( \alpha \) is decreasing. Since it is positive, it therefore admits a limit \( \ell \in {\mathbb{R}}^{ + } \) at \( + \infty \) . It remains to show \( \ell = 0 \) .

> Supposons \( \ell > 0 \) . Sur \( {\mathbb{R}}^{ + } \) , on a \( \ell \leq \alpha \left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \leq \alpha \left( 0\right) \) , autrement dit, pour \( t \geq 0, Y\left( t\right) \) prend ses valeurs dans le compact \( K = \left\{ {X \in {\mathbb{R}}^{n} \mid \ell \leq \parallel X{\parallel }^{2} \leq \alpha \left( 0\right) }\right\} \) . D’après \( \left( *\right) \) et comme \( \ell > 0 \) , on a \( {}^{t}{Xf}\left( X\right) < 0 \) pour tout \( X \in K \) , et la compacité de \( K \) entraîne \( \gamma = \sup \left\{ {{}^{t}{Xf}\left( X\right) , X \in }\right. \; K\} < 0 \) . Ainsi, d’après (**), on a \( {\alpha }^{\prime }\left( t\right) \leq {2\gamma } < 0 \) pour tout \( t \geq 0 \) , donc \( \alpha \left( t\right) - \alpha \left( 0\right) \leq - {2\gamma t} \) , ce qui entraîne lim \( {}_{t \rightarrow + \infty }\alpha \left( t\right) = - \infty \) . Ceci est impossible puisque \( \alpha \) est positive. Donc \( \ell = 0 \) , d’où le résultat.

Suppose \( \ell > 0 \) . On \( {\mathbb{R}}^{ + } \) , we have \( \ell \leq \alpha \left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \leq \alpha \left( 0\right) \) , in other words, for \( t \geq 0, Y\left( t\right) \) takes its values in the compact set \( K = \left\{ {X \in {\mathbb{R}}^{n} \mid \ell \leq \parallel X{\parallel }^{2} \leq \alpha \left( 0\right) }\right\} \) . According to \( \left( *\right) \) and since \( \ell > 0 \) , we have \( {}^{t}{Xf}\left( X\right) < 0 \) for all \( X \in K \) , and the compactness of \( K \) implies \( \gamma = \sup \left\{ {{}^{t}{Xf}\left( X\right) , X \in }\right. \; K\} < 0 \) . Thus, according to (**), we have \( {\alpha }^{\prime }\left( t\right) \leq {2\gamma } < 0 \) for all \( t \geq 0 \) , therefore \( \alpha \left( t\right) - \alpha \left( 0\right) \leq - {2\gamma t} \) , which implies lim \( {}_{t \rightarrow + \infty }\alpha \left( t\right) = - \infty \) . This is impossible since \( \alpha \) is positive. Therefore \( \ell = 0 \) , hence the result.

> PROBLÉME 7 (RÉSOLUTION D'ÉQUATIONS MATRICIELLES GRÁCE AUX ÉQUATIONS DIF-FÉRENTIELLES). 1/ Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice dont les valeurs propres \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) vérifient \( \Re \left( {\lambda }_{i}\right) < 0 \) pour tout \( i \) . Si \( \parallel .\parallel \) désigne une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , montrer qu’il existe \( \alpha > 0 \) et \( K > 0 \) tel que \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq K{e}^{-{\alpha t}} \) pour tout \( t \geq 0 \) .

PROBLEM 7 (SOLVING MATRIX EQUATIONS USING DIFFERENTIAL EQUATIONS). 1/ Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a matrix whose eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) satisfy \( \Re \left( {\lambda }_{i}\right) < 0 \) for all \( i \) . If \( \parallel .\parallel \) denotes an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , show that there exist \( \alpha > 0 \) and \( K > 0 \) such that \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq K{e}^{-{\alpha t}} \) for all \( t \geq 0 \) .

> 2 / a) Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Exprimer la solution \( Y : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) de l’équation différentielle \( \left( E\right) : {Y}^{\prime } = {AY} + {YB} \) , telle que \( Y\left( 0\right) = C \) , où \( C \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice donnée.

2 / a) Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Express the solution \( Y : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) of the differential equation \( \left( E\right) : {Y}^{\prime } = {AY} + {YB} \) , such that \( Y\left( 0\right) = C \) , where \( C \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is a given matrix.

> b) On suppose que pour toute valeur propre \( \lambda \) de \( A \) ou de \( B,\Re \left( \lambda \right) < 0 \) . Montrer que pour toute matrice \( C \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , il existe une unique matrice \( X \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que \( {AX} + {XB} = C \) , puis exprimer \( X \) en fonction de \( A, B \) et \( C \) .

b) Assume that for every eigenvalue \( \lambda \) of \( A \) or \( B,\Re \left( \lambda \right) < 0 \) . Show that for any matrix \( C \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , there exists a unique matrix \( X \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that \( {AX} + {XB} = C \) , then express \( X \) in terms of \( A, B \) and \( C \) .

> 3 / Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Montrer que l’équation matricielle \( {}^{t}{AS} + {SA} = - C \) admet une solution \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) symétrique positive pour toute matrice symétrique positive \( C \) si et seulement si pour toute valeur propre \( \lambda \) de \( A \) , on a \( \Re \left( \lambda \right) < 0 \) . (Indication. Pour la condition nécessaire, on pourra étudier les variations de la fonction \( u \mapsto {}^{t}\left( {{e}^{uA}\bar{X}}\right) S\left( {{e}^{uA}X}\right) \) , où \( X \in {\mathbb{C}}^{n} \) ).

3 / Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Show that the matrix equation \( {}^{t}{AS} + {SA} = - C \) admits a symmetric positive solution \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) for any symmetric positive matrix \( C \) if and only if for every eigenvalue \( \lambda \) of \( A \) , we have \( \Re \left( \lambda \right) < 0 \) . (Hint: For the necessary condition, one may study the variations of the function \( u \mapsto {}^{t}\left( {{e}^{uA}\bar{X}}\right) S\left( {{e}^{uA}X}\right) \) , where \( X \in {\mathbb{C}}^{n} \) ).

> Solution. 1/ On sait que l’on peut écrire \( A = D + N \) , où \( D \) est une matrice diagonalisable dont les valeurs propres sont \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) et \( N \) une matrice nilpotente vérifiant \( {DN} = {ND} \) (voir le tome Algèbre sur la décomposition de Dunford).

Solution. 1/ We know that we can write \( A = D + N \) , where \( D \) is a diagonalizable matrix whose eigenvalues are \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) and \( N \) is a nilpotent matrix satisfying \( {DN} = {ND} \) (see the Algebra volume on the Dunford decomposition).

> Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( D = {P}^{-1}{D}_{1}P \) où \( {D}_{1} \) est la matrice diagonale dont les coefficients diagonaux sont \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) . Pour tout \( t \in \mathbb{R},{e}^{t{D}_{1}} \) est la matrice diagonale dont les coefficients diagonaux sont les \( {e}^{t{\lambda }_{i}} \) . En désignant par \( \parallel .{\parallel }_{\infty } \) la norme \( {\begin{Vmatrix}\left( {a}_{i, j}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{{i, j}}\left| {a}_{i, j}\right| \) sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , on a \( {\begin{Vmatrix}{e}^{t{D}_{1}}\end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {e}^{t{\lambda }_{i}}\right| = {e}^{-{ct}} \) , où \( c = - \mathop{\sup }\limits_{i}\Re \left( {\lambda }_{i}\right) > 0 \) . Comme toutes les normes sont équivalentes en dimension finie, on en déduit l’existence de \( {K}_{1} > 0 \) tel que \( \begin{Vmatrix}{e}^{t{D}_{1}}\end{Vmatrix} \leq {K}_{1}{e}^{-{ct}} \) pour tout \( t \in \mathbb{R} \) . Comme \( {e}^{tD} = {P}^{-1}{e}^{t{D}_{1}}P \) pour tout \( t \in \mathbb{R} \) , on en déduit

Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) be such that \( D = {P}^{-1}{D}_{1}P \) where \( {D}_{1} \) is the diagonal matrix whose diagonal coefficients are \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) . For any \( t \in \mathbb{R},{e}^{t{D}_{1}} \) is the diagonal matrix whose diagonal coefficients are the \( {e}^{t{\lambda }_{i}} \) . By denoting by \( \parallel .{\parallel }_{\infty } \) the \( {\begin{Vmatrix}\left( {a}_{i, j}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{{i, j}}\left| {a}_{i, j}\right| \) norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , we have \( {\begin{Vmatrix}{e}^{t{D}_{1}}\end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {e}^{t{\lambda }_{i}}\right| = {e}^{-{ct}} \) , where \( c = - \mathop{\sup }\limits_{i}\Re \left( {\lambda }_{i}\right) > 0 \) . Since all norms are equivalent in finite dimension, we deduce the existence of \( {K}_{1} > 0 \) such that \( \begin{Vmatrix}{e}^{t{D}_{1}}\end{Vmatrix} \leq {K}_{1}{e}^{-{ct}} \) for all \( t \in \mathbb{R} \) . Since \( {e}^{tD} = {P}^{-1}{e}^{t{D}_{1}}P \) for all \( t \in \mathbb{R} \) , we deduce

\[
\forall t \in  \mathbb{R},\;\begin{Vmatrix}{e}^{tD}\end{Vmatrix} \leq  {K}_{2}{e}^{-{ct}}\text{ avec }{K}_{2} = \begin{Vmatrix}{P}^{-1}\end{Vmatrix} \cdot  {K}_{1} \cdot  \parallel P\parallel .
\]

Maintenant, comme \( N \) est nilpotente, on a

> Now, since \( N \) is nilpotent, we have

\[
\forall t \in  \mathbb{R},\;{e}^{tN} = {I}_{n} + {tN} + \cdots  + \frac{{t}^{n - 1}}{\left( {n - 1}\right) !}{N}^{n - 1},
\]

et on en déduit que \( \begin{Vmatrix}{e}^{tN}\end{Vmatrix} = o\left( {t}^{n}\right) \) lorsque \( t \rightarrow + \infty \) . Maintenant, \( D \) et \( N \) commutent, donc \( {e}^{tA} = {e}^{{tD} + {tN}} = {e}^{tD}{e}^{tN} \) pour tout \( t \in {\mathbb{R}}^{ + } \) , donc \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq \begin{Vmatrix}{e}^{tD}\end{Vmatrix} \cdot \begin{Vmatrix}{e}^{tN}\end{Vmatrix} = o\left( {{e}^{-{ct}}{t}^{n}}\right) \) lorsque \( t \rightarrow + \infty \) . Comme \( {t}^{n} = o\left( {e}^{{ct}/2}\right) \) , on a \( {e}^{-{ct}}{t}^{n} = o\left( {e}^{-{ct}/2}\right) \) lorsque \( t \rightarrow + \infty \) , donc finalement \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} = o\left( {e}^{-{\alpha t}}\right) \) lorsque \( t \rightarrow + \infty \) avec \( \alpha = c/2 > 0 \) . D’où le résultat.

> and we deduce that \( \begin{Vmatrix}{e}^{tN}\end{Vmatrix} = o\left( {t}^{n}\right) \) as \( t \rightarrow + \infty \) . Now, \( D \) and \( N \) commute, so \( {e}^{tA} = {e}^{{tD} + {tN}} = {e}^{tD}{e}^{tN} \) for all \( t \in {\mathbb{R}}^{ + } \) , thus \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq \begin{Vmatrix}{e}^{tD}\end{Vmatrix} \cdot \begin{Vmatrix}{e}^{tN}\end{Vmatrix} = o\left( {{e}^{-{ct}}{t}^{n}}\right) \) as \( t \rightarrow + \infty \) . Since \( {t}^{n} = o\left( {e}^{{ct}/2}\right) \) , we have \( {e}^{-{ct}}{t}^{n} = o\left( {e}^{-{ct}/2}\right) \) as \( t \rightarrow + \infty \) , so finally \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} = o\left( {e}^{-{\alpha t}}\right) \) as \( t \rightarrow + \infty \) with \( \alpha = c/2 > 0 \) . Hence the result.

2 / a) L'équation différentielle correspondante est linéaire à coefficients constant, donc on sait déjà qu’une telle solution \( X \) existe et est unique. Or on vérifie facilement que \( Y : t \mapsto {e}^{tA}C{e}^{tB} \) convient, c’est donc la solution de \( \left( E\right) \) vérifiant \( Y\left( 0\right) = C \) .

> 2 / a) The corresponding differential equation is linear with constant coefficients, so we already know that such a solution \( X \) exists and is unique. However, it is easy to verify that \( Y : t \mapsto {e}^{tA}C{e}^{tB} \) works, so it is the solution to \( \left( E\right) \) satisfying \( Y\left( 0\right) = C \) .

b) Existence. En désignant par \( Y \) la fonction de \( \mathbb{R} \) dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) trouvée précédemment, on a \( {Y}^{\prime } = {AY} + {YB} \) donc par intégration entre 0 et \( t \) , on obtient

> b) Existence. By denoting by \( Y \) the function from \( \mathbb{R} \) to \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) found previously, we have \( {Y}^{\prime } = {AY} + {YB} \) so by integrating between 0 and \( t \) , we obtain

\[
Y\left( t\right)  - C = A\left( {{\int }_{0}^{t}Y\left( s\right) {ds}}\right)  + \left( {{\int }_{0}^{t}Y\left( s\right) {ds}}\right) B.
\]

\( \left( *\right) \) .

> Par ailleurs, les hypothèses sur les valeurs propres des matrices \( A \) et \( B \) permettent d’affirmer, grâce au résultat de la question \( 1/ \) , l’existence de \( \alpha > 0 \) et \( M > 0 \) telles que \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq M{e}^{-{\alpha t}} \) et \( \begin{Vmatrix}{e}^{tB}\end{Vmatrix} \leq M{e}^{-{\alpha t}} \) pour tout \( t > 0 \) . La forme de \( Y\left( t\right) \) entraîne donc

Furthermore, the hypotheses on the eigenvalues of matrices \( A \) and \( B \) allow us to affirm, thanks to the result of question \( 1/ \) , the existence of \( \alpha > 0 \) and \( M > 0 \) such that \( \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \leq M{e}^{-{\alpha t}} \) and \( \begin{Vmatrix}{e}^{tB}\end{Vmatrix} \leq M{e}^{-{\alpha t}} \) for all \( t > 0 \) . The form of \( Y\left( t\right) \) therefore implies

\[
\forall t \geq  0,\;\parallel Y\left( t\right) \parallel  \leq  \begin{Vmatrix}{e}^{tA}\end{Vmatrix} \cdot  \parallel C\parallel  \cdot  \begin{Vmatrix}{e}^{tB}\end{Vmatrix} \leq  K{e}^{-{2\alpha t}}\text{ avec }K = {M}^{2}\parallel C\parallel .
\]

On en déduit que l’intégrale \( {\int }_{0}^{+\infty }Y\left( s\right) {ds} \) converge absolument donc converge, et que \( Y\left( t\right) \) tend vers 0 lorsque \( t \rightarrow + \infty \) . En faisant \( t \rightarrow + \infty \) dans (*), on en déduit

> We deduce that the integral \( {\int }_{0}^{+\infty }Y\left( s\right) {ds} \) converges absolutely and therefore converges, and that \( Y\left( t\right) \) tends to 0 as \( t \rightarrow + \infty \) . By letting \( t \rightarrow + \infty \) in (*), we deduce

\[
C = {AX} + {XB}\;\text{ avec }\;X =  - {\int }_{0}^{+\infty }Y\left( s\right) {ds} =  - {\int }_{0}^{+\infty }{e}^{tA}C{e}^{tB}{dt}.
\]

Unicité. Pour montrer que \( X \) ainsi défini est unique, il suffit de montrer que l’application \( \Phi : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;X \mapsto {AX} + {XB} \) est injective. Nous venons de montrer dans la partie existence que \( \Phi \) est surjective. Comme \( \Phi \) est un endomorphisme en dimension finie, ceci entraîne l’injectivité de \( \Phi \) , d’où le résultat.

> Uniqueness. To show that \( X \) thus defined is unique, it suffices to show that the map \( \Phi : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;X \mapsto {AX} + {XB} \) is injective. We have just shown in the existence part that \( \Phi \) is surjective. Since \( \Phi \) is an endomorphism in finite dimension, this implies the injectivity of \( \Phi \) , hence the result.

3/ Condition nécessaire. Par hypothèse, il existe une matrice symétrique positive \( S \) telle que \( {}^{t}{AS} + {SA} = - {I}_{n} \) . Soit \( X \in {\mathbb{C}}^{n} \) un vecteur non nul, et considérons l’application

> 3/ Necessary condition. By hypothesis, there exists a positive symmetric matrix \( S \) such that \( {}^{t}{AS} + {SA} = - {I}_{n} \) . Let \( X \in {\mathbb{C}}^{n} \) be a non-zero vector, and consider the mapping

\[
{V}_{X} : \mathbb{R} \rightarrow  {\mathbb{C}}^{n}\;u \mapsto  {}^{t}\left( {{e}^{uA}\bar{X}}\right) S\left( {{e}^{uA}X}\right) .
\]

On a

> We have

\[
\forall u \in  \mathbb{R},\;{V}_{X}^{\prime }\left( u\right)  = {}^{t}\left( {A{e}^{uA}\bar{X}}\right) S\left( {{e}^{uA}X}\right)  + {}^{t}\left( {{e}^{uA}\bar{X}}\right) S\left( {A{e}^{uA}X}\right)
\]

\[
= {}^{t}{\bar{X}}^{t}{e}^{uA}\left( {{}^{t}{AS} + {SA}}\right) {e}^{uA}X =  - {}^{t}\left( {{e}^{uA}\bar{X}}\right) \left( {{e}^{uA}X}\right)  < 0
\]

(le terme \( {}^{t}\left( {{e}^{uA}\bar{X}}\right) \left( {{e}^{uA}X}\right) \) est le carré de la norme hermitienne de \( {e}^{uA}X \) qui est non nul, car \( X \neq 0 \) et \( {e}^{uA} \) est inversible - toute exponentielle de matrice est inversible, l’inverse de \( {e}^{M} \) étant \( \left. {e}^{-M}\right) \) .

> (the term \( {}^{t}\left( {{e}^{uA}\bar{X}}\right) \left( {{e}^{uA}X}\right) \) is the square of the Hermitian norm of \( {e}^{uA}X \) which is non-zero, because \( X \neq 0 \) and \( {e}^{uA} \) is invertible - any matrix exponential is invertible, the inverse of \( {e}^{M} \) being \( \left. {e}^{-M}\right) \) .

Ceci étant, soit \( \lambda \) une valeur propre de \( A \) et \( X \in {\mathbb{C}}^{n} \) un vecteur propre non nul associé. Pour tout \( n \in \mathbb{N},{A}^{n}X = {\lambda }^{n}X \) donc \( {e}^{uA}X = {e}^{\lambda u}X \) , et en passant au conjugué, \( {e}^{uA}\bar{X} = {e}^{\overline{\lambda }u}\bar{X} \) , donc

> Given this, let \( \lambda \) be an eigenvalue of \( A \) and \( X \in {\mathbb{C}}^{n} \) a non-zero associated eigenvector. For all \( n \in \mathbb{N},{A}^{n}X = {\lambda }^{n}X \) therefore \( {e}^{uA}X = {e}^{\lambda u}X \) , and by taking the conjugate, \( {e}^{uA}\bar{X} = {e}^{\overline{\lambda }u}\bar{X} \) , therefore

\[
\forall u \in  \mathbb{R},\;{V}_{X}\left( u\right)  = {}^{t}\left( {{e}^{\overline{\lambda }u}\bar{X}}\right) S\left( {{e}^{\lambda u}X}\right)  = {e}^{\left( {\lambda  + \overline{\lambda }}\right) u}{}^{t}\bar{X}{SX}.
\]

On en déduit \( {V}_{X}^{\prime }\left( 0\right) = \left( {\lambda + \overline{\lambda }}\right) {V}_{X}\left( 0\right) = 2\Re \left( \lambda \right) {V}_{X}\left( 0\right) \) . Or on a vu plus haut que \( {V}_{X}^{\prime }\left( 0\right) < 0 \) et comme \( S \) est positive, on a \( {V}_{X}\left( 0\right) = {}^{t}\bar{X}{SX} \geq 0 \) . Donc nécessairement \( \Re \left( \lambda \right) < 0 \) , et ceci pour toute valeur propre \( \lambda \) de \( A \) .

> We deduce \( {V}_{X}^{\prime }\left( 0\right) = \left( {\lambda + \overline{\lambda }}\right) {V}_{X}\left( 0\right) = 2\Re \left( \lambda \right) {V}_{X}\left( 0\right) \) . However, we saw above that \( {V}_{X}^{\prime }\left( 0\right) < 0 \) and since \( S \) is positive, we have \( {V}_{X}\left( 0\right) = {}^{t}\bar{X}{SX} \geq 0 \) . Thus necessarily \( \Re \left( \lambda \right) < 0 \) , and this for any eigenvalue \( \lambda \) of \( A \) .

Condition suffisante. Supposons que \( \Re \left( \lambda \right) < 0 \) pour toute valeur propre \( \lambda \) de \( A \) . Comme \( {}^{t}A \) a les mêmes valeurs propres \( A \) , la résultat de la question 1/b) s’applique et montre que la matrice \( S = {\int }_{0}^{+\infty }{e}^{{u}^{t}A}C{e}^{uA}{du} \) vérifie \( {}^{t}{AS} + {SA} = - C \) . Pour tout \( u \) , la matrice \( S\left( u\right) = {e}^{{u}^{t}A}C{e}^{uA} \) est congrue à la matrice \( C \) , donc symétrique positive. Comme \( S \) est l’intégrale de \( S\left( u\right) \) sur \( {\mathbb{R}}^{ + } \) , on en déduit que \( S \) est symétrique. Par ailleurs, pour tout \( X \in {\mathbb{R}}^{n} \) , on a

> Sufficient condition. Suppose that \( \Re \left( \lambda \right) < 0 \) for any eigenvalue \( \lambda \) of \( A \) . Since \( {}^{t}A \) has the same eigenvalues as \( A \) , the result from question 1/b) applies and shows that the matrix \( S = {\int }_{0}^{+\infty }{e}^{{u}^{t}A}C{e}^{uA}{du} \) satisfies \( {}^{t}{AS} + {SA} = - C \) . For all \( u \) , the matrix \( S\left( u\right) = {e}^{{u}^{t}A}C{e}^{uA} \) is congruent to the matrix \( C \) , and therefore positive symmetric. Since \( S \) is the integral of \( S\left( u\right) \) over \( {\mathbb{R}}^{ + } \) , we deduce that \( S \) is symmetric. Furthermore, for all \( X \in {\mathbb{R}}^{n} \) , we have

\[
{}^{t}{XSX} = {\int }_{0}^{+\infty }{}^{t}{XS}\left( u\right) {Xdu} \geq  0
\]

car \( {}^{t}{XS}\left( u\right) X \geq 0 \) pour tout \( u \) . Finalement, \( S \) est symétrique positive et vérifie \( {}^{t}{AS} + {SA} = - C \) , d'où le résultat.

> because \( {}^{t}{XS}\left( u\right) X \geq 0 \) for all \( u \) . Finally, \( S \) is positive symmetric and satisfies \( {}^{t}{AS} + {SA} = - C \) , hence the result.

Problem 8. Soit \( A : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une application continue telle que pour tout \( t \in \mathbb{R} \) , la matrice symétrique \( B\left( t\right) = {}^{t}A\left( t\right) + A\left( t\right) \) est négative. On considère le système différentiel \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y\left( {Y \in {\mathbb{R}}^{n}}\right) . \)

> Problem 8. Let \( A : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a continuous mapping such that for all \( t \in \mathbb{R} \) , the symmetric matrix \( B\left( t\right) = {}^{t}A\left( t\right) + A\left( t\right) \) is negative. Consider the differential system \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y\left( {Y \in {\mathbb{R}}^{n}}\right) . \)

a) Si \( {Y}_{1} \) et \( {Y}_{2} \) sont deux solutions de \( \left( L\right) \) sur \( \mathbb{R} \) , montrer que \( {}^{t}{Y}_{1}\left( t\right) {Y}_{2}\left( t\right) \) converge lorsque \( t \rightarrow + \infty \) .

> a) If \( {Y}_{1} \) and \( {Y}_{2} \) are two solutions of \( \left( L\right) \) on \( \mathbb{R} \) , show that \( {}^{t}{Y}_{1}\left( t\right) {Y}_{2}\left( t\right) \) converges as \( t \rightarrow + \infty \) .

b) Montrer que \( \left( L\right) \) admet une solution non identiquement nulle \( Y \) qui tend vers 0 en \( + \infty \) si et seulement si

> b) Show that \( \left( L\right) \) admits a non-identically zero solution \( Y \) that tends to 0 at \( + \infty \) if and only if

\[
\mathop{\lim }\limits_{{t \rightarrow   + \infty }}{\int }_{0}^{t}\operatorname{tr}\left( {A\left( s\right) }\right) {ds} =  - \infty .
\]

(Indication. On pourra utiliser le résultat de l'exercice 7 page 388).

> (Hint: You may use the result of exercise 7 on page 388).

Solution. a) Commençons par remarquer que si \( Y \) est une solution de \( \left( L\right) \) , alors la fonction \( V : t \mapsto \parallel Y\left( t\right) {\parallel }^{2} = {}^{t}Y\left( t\right) Y\left( t\right) \) vérifie

> Solution. a) Let us begin by noting that if \( Y \) is a solution of \( \left( L\right) \) , then the function \( V : t \mapsto \parallel Y\left( t\right) {\parallel }^{2} = {}^{t}Y\left( t\right) Y\left( t\right) \) satisfies

\[
\forall t \in  \mathbb{R},\;{V}^{\prime }\left( t\right)  = {}^{t}{Y}^{\prime }\left( t\right) Y\left( t\right)  + {}^{t}Y\left( t\right) {Y}^{\prime }\left( t\right)  = {}^{t}Y\left( t\right) B\left( t\right) Y\left( t\right)  \leq  0,
\]

donc \( V \) est décroissante, et comme elle est positive, \( V\left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \) converge nécessairement lorsque \( t \rightarrow + \infty \) .

> therefore \( V \) is decreasing, and since it is positive, \( V\left( t\right) = \parallel Y\left( t\right) {\parallel }^{2} \) necessarily converges as \( t \rightarrow + \infty \) .

Maintenant, si \( {Y}_{1} \) et \( {Y}_{2} \) sont deux solutions de \( \left( L\right) \) , on a \( {}^{t}{Y}_{1}{Y}_{2} = \frac{1}{2}\left( {{\begin{Vmatrix}{Y}_{1} + {Y}_{2}\end{Vmatrix}}^{2} - {\begin{Vmatrix}{Y}_{1}\end{Vmatrix}}^{2} - {\begin{Vmatrix}{Y}_{2}\end{Vmatrix}}^{2}}\right) \) , donc d’après ce que l’on vient de voir, \( {}^{t}{Y}_{1}{Y}_{2} \) converge en \( + \infty \) .

> Now, if \( {Y}_{1} \) and \( {Y}_{2} \) are two solutions of \( \left( L\right) \) , we have \( {}^{t}{Y}_{1}{Y}_{2} = \frac{1}{2}\left( {{\begin{Vmatrix}{Y}_{1} + {Y}_{2}\end{Vmatrix}}^{2} - {\begin{Vmatrix}{Y}_{1}\end{Vmatrix}}^{2} - {\begin{Vmatrix}{Y}_{2}\end{Vmatrix}}^{2}}\right) \) , so according to what we have just seen, \( {}^{t}{Y}_{1}{Y}_{2} \) converges at \( + \infty \) .

b) On sait que l’ensemble \( \mathcal{S} \) des solutions de \( \left( L\right) \) est un espace vectoriel de dimension \( n \) . Soit \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) une base de \( \mathcal{S} \) . Pour tout \( t \in \mathbb{R} \) , on note \( R\left( t\right) \) la matrice de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) dont les vecteurs colonnes sont les \( {Y}_{i}\left( t\right) \) , et on note \( M\left( t\right) = {}^{t}R\left( t\right) R\left( t\right) \) . Le coefficient d’indice \( \left( {i, j}\right) \) de \( M\left( t\right) \) est \( {}^{t}{Y}_{i}\left( t\right) {Y}_{j}\left( t\right) \) , donc d’après la question précédente, \( M\left( t\right) \) converge lorsque \( t \rightarrow + \infty \) . Notons \( M = \mathop{\lim }\limits_{{t \rightarrow + \infty }}M\left( t\right) . \)

> b) We know that the set \( \mathcal{S} \) of solutions of \( \left( L\right) \) is a vector space of dimension \( n \) . Let \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) be a basis of \( \mathcal{S} \) . For all \( t \in \mathbb{R} \) , we denote by \( R\left( t\right) \) the matrix of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) whose column vectors are the \( {Y}_{i}\left( t\right) \) , and we denote \( M\left( t\right) = {}^{t}R\left( t\right) R\left( t\right) \) . The coefficient with index \( \left( {i, j}\right) \) of \( M\left( t\right) \) is \( {}^{t}{Y}_{i}\left( t\right) {Y}_{j}\left( t\right) \) , so according to the previous question, \( M\left( t\right) \) converges as \( t \rightarrow + \infty \) . Let us denote \( M = \mathop{\lim }\limits_{{t \rightarrow + \infty }}M\left( t\right) . \)

Comme \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) est une base de solutions de \( \mathcal{S} \) , toute solution de \( \left( L\right) \) peut s’écrire sous la forme \( t \mapsto R\left( t\right) {X}_{0} \) , où \( {X}_{0} \in {\mathbb{R}}^{n} \) est un vecteur fixé. Comme \( {\begin{Vmatrix}R\left( t\right) {X}_{0}\end{Vmatrix}}^{2} = {}^{t}\left( {R\left( t\right) {X}_{0}}\right) \left( {R\left( t\right) {X}_{0}}\right) = \; {}^{t}{X}_{0}M\left( t\right) {X}_{0} \) , on voit donc que l’existence d’une solution non nulle de \( \left( L\right) \) qui tend vers 0 en \( + \infty \) équivaut à l’existence d’un vecteur \( {X}_{0} \neq 0 \) tel que \( {}^{t}{X}_{0}M\left( t\right) {X}_{0} \) tend vers 0 en \( + \infty \) . Comme \( M\left( t\right) \) converge vers \( M \) , ceci équivaut aussi à l’existence de \( {X}_{0} \neq 0 \) tel que \( {}^{t}{X}_{0}M{X}_{0} = 0 \) . Comme \( M \) est positive (limite de matrices positives), ceci équivaut à det \( M = 0 \) , et comme l’application déterminant est continue, ceci équivaut aussi à \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\det M\left( t\right) = 0 \) . Comme \( M\left( t\right) = {}^{t}R\left( t\right) R\left( t\right) \) , ceci s’écrit aussi \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\det R\left( t\right) = 0 \) . On conclut facilement puisque d’après la question b) de l'exercice 7 page 388,

> Since \( \left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \) is a basis of solutions for \( \mathcal{S} \), any solution of \( \left( L\right) \) can be written in the form \( t \mapsto R\left( t\right) {X}_{0} \), where \( {X}_{0} \in {\mathbb{R}}^{n} \) is a fixed vector. Since \( {\begin{Vmatrix}R\left( t\right) {X}_{0}\end{Vmatrix}}^{2} = {}^{t}\left( {R\left( t\right) {X}_{0}}\right) \left( {R\left( t\right) {X}_{0}}\right) = \; {}^{t}{X}_{0}M\left( t\right) {X}_{0} \), we see that the existence of a non-zero solution of \( \left( L\right) \) that tends to 0 at \( + \infty \) is equivalent to the existence of a vector \( {X}_{0} \neq 0 \) such that \( {}^{t}{X}_{0}M\left( t\right) {X}_{0} \) tends to 0 at \( + \infty \). Since \( M\left( t\right) \) converges to \( M \), this is also equivalent to the existence of \( {X}_{0} \neq 0 \) such that \( {}^{t}{X}_{0}M{X}_{0} = 0 \). Since \( M \) is positive (limit of positive matrices), this is equivalent to det \( M = 0 \), and since the determinant map is continuous, this is also equivalent to \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\det M\left( t\right) = 0 \). Since \( M\left( t\right) = {}^{t}R\left( t\right) R\left( t\right) \), this can also be written as \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\det R\left( t\right) = 0 \). We conclude easily since, according to question b) of exercise 7 on page 388,

\[
\forall t \in  \mathbb{R},\;\det R\left( t\right)  = \operatorname{wronskien}\left( {{Y}_{1},\ldots ,{Y}_{n}}\right) \left( t\right)  = \det R\left( 0\right)  \cdot  \exp \left\lbrack  {{\int }_{0}^{t}\operatorname{tr}A\left( u\right) {du}}\right\rbrack  .
\]

Problem 9. Soit \( y : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une solution de l’équation différentielle \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = \) 0, où \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) est une fonction continue telle que \( {\int }_{0}^{+\infty }t\left| {q\left( t\right) }\right| {dt} \) converge.

> Problem 9. Let \( y : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a solution of the differential equation \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = \) 0, where \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) is a continuous function such that \( {\int }_{0}^{+\infty }t\left| {q\left( t\right) }\right| {dt} \) converges.

Montrer que \( {y}^{\prime } \) converge en \( + \infty \) .

> Show that \( {y}^{\prime } \) converges at \( + \infty \).

Solution. La formule de Taylor avec reste intégral donne l'existence de deux constantes réelles \( a \) et \( b \) telles que

> Solution. Taylor's formula with integral remainder gives the existence of two real constants \( a \) and \( b \) such that

\[
\forall t \geq  1,\;y\left( t\right)  = {at} + b + {\int }_{1}^{t}\left( {t - s}\right) {y}^{\prime \prime }\left( s\right) {ds} = {at} + b - {\int }_{1}^{t}\left( {t - s}\right) q\left( s\right) y\left( s\right) {ds}.
\]

Ceci entraîne

> This implies

\[
\forall t \geq  1,\;\left| \frac{y\left( t\right) }{t}\right|  \leq  \left| a\right|  + \frac{\left| b\right| }{t} + {\int }_{1}^{t}s\left| {q\left( s\right) }\right| \left| \frac{y\left( s\right) }{s}\right| {ds},
\]

donc d'après le lemme de Gronwall (voir le théorème 1 page 397),

> therefore, according to Gronwall's lemma (see theorem 1 on page 397),

\[
\forall t \geq  1,\;\left| \frac{y\left( t\right) }{t}\right|  \leq  \left| a\right|  + \frac{\left| b\right| }{t} + {\int }_{1}^{t}\left( {\left| a\right| s + \left| b\right| }\right) \left| {q\left( s\right) }\right| \exp \left( {{\int }_{s}^{t}u\left| {q\left( u\right) }\right| {du}}\right) {ds}.
\]

Comme \( {\int }_{0}^{+\infty }t\left| {q\left( t\right) }\right| {dt} \) converge, on en déduit facilement que \( \left| {y\left( t\right) /t}\right| \) est bornée sur \( \lbrack 1, + \infty \lbrack \) .

> Since \( {\int }_{0}^{+\infty }t\left| {q\left( t\right) }\right| {dt} \) converges, we easily deduce that \( \left| {y\left( t\right) /t}\right| \) is bounded on \( \lbrack 1, + \infty \lbrack \).

En d’autres termes, \( y\left( t\right) = O\left( t\right) \) au voisinage de \( + \infty \) . Comme

> In other words, \( y\left( t\right) = O\left( t\right) \) in the neighborhood of \( + \infty \). Since

\[
\forall t \in  {\mathbb{R}}^{ + },\;{y}^{\prime }\left( t\right)  = {y}^{\prime }\left( 0\right)  + {\int }_{0}^{t}{y}^{\prime \prime }\left( s\right) {ds} = {y}^{\prime }\left( 0\right)  - {\int }_{0}^{t}q\left( s\right) y\left( s\right) {ds},
\]

on en déduit que \( {y}^{\prime }\left( t\right) \) converge lorsque \( t \rightarrow + \infty \) .

> we deduce that \( {y}^{\prime }\left( t\right) \) converges when \( t \rightarrow + \infty \).

Problem 10. On s’intéresse aux solutions sur \( {\mathbb{R}}^{+ * } \) ,à valeurs réelles, de l’équation différentielle

> Problem 10. We are interested in the real-valued solutions on \( {\mathbb{R}}^{+ * } \) of the differential equation

\[
{t}^{2}{y}^{\prime \prime } + \left( {a + 1}\right) t{y}^{\prime } + \left( {{t}^{2} + \frac{1}{4}}\right) y = 0, \tag{L}
\]

où \( a \geq 1 \) .

> where \( a \geq 1 \).

a) Montrer que sur \( {\mathbb{R}}^{+ * },\left( L\right) \) admet au moins une solution de la forme \( t \mapsto {t}^{\alpha }\varphi \left( t\right) \) où \( \alpha \in \mathbb{R} \) et où \( \varphi \) est la somme d’une série entière de rayon infini avec \( \varphi \left( 0\right) \neq 0 \) .

> a) Show that on \( {\mathbb{R}}^{+ * },\left( L\right) \) there exists at least one solution of the form \( t \mapsto {t}^{\alpha }\varphi \left( t\right) \) where \( \alpha \in \mathbb{R} \) and where \( \varphi \) is the sum of a power series with infinite radius of convergence with \( \varphi \left( 0\right) \neq 0 \) .

b) Donner le comportement asymptotique en \( {0}^{ + } \) de la solution générale sur \( {\mathbb{R}}^{+ * } \) de \( \left( L\right) \) . (Indication. Distinguer deux cas, selon que \( {a}^{2} - 1 \) soit le carré d’un entier ou non.)

> b) Give the asymptotic behavior as \( {0}^{ + } \) of the general solution on \( {\mathbb{R}}^{+ * } \) of \( \left( L\right) \) . (Hint: Distinguish between two cases, depending on whether \( {a}^{2} - 1 \) is the square of an integer or not.)

c) (Application.) Montrer que l’équation différentielle \( \left( E\right) : {t}^{4}{y}^{\prime \prime } - \frac{2}{3}{t}^{3}{y}^{\prime } + \left( {1 + \frac{{t}^{2}}{4}}\right) y = 0 \) admet une unique solution \( f \) sur \( {\mathbb{R}}^{+ * } \) qui vérifie \( f\left( t\right) \sim {t}^{1/6} \) lorsque \( t \rightarrow + \infty \) , et donner un développement asymptotique à trois termes de \( f \) en \( + \infty \) .

> c) (Application.) Show that the differential equation \( \left( E\right) : {t}^{4}{y}^{\prime \prime } - \frac{2}{3}{t}^{3}{y}^{\prime } + \left( {1 + \frac{{t}^{2}}{4}}\right) y = 0 \) admits a unique solution \( f \) on \( {\mathbb{R}}^{+ * } \) satisfying \( f\left( t\right) \sim {t}^{1/6} \) as \( t \rightarrow + \infty \) , and provide a three-term asymptotic expansion of \( f \) as \( + \infty \) .

Solution. a) Nous recherchons une solution \( f \) de \( \left( L\right) \) la forme \( {t}^{\alpha }\varphi \left( t\right) \) , où \( \varphi \left( t\right) \) est la somme d’une série entière \( \sum {u}_{n}{t}^{n} \) dont le rayon de convergence est infini. Supposons qu’une telle solution \( f \) existe ; on aura

> Solution. a) We seek a solution \( f \) of \( \left( L\right) \) of the form \( {t}^{\alpha }\varphi \left( t\right) \) , where \( \varphi \left( t\right) \) is the sum of a power series \( \sum {u}_{n}{t}^{n} \) whose radius of convergence is infinite. Suppose such a solution \( f \) exists; we then have

\[
\forall t > 0,\;f\left( t\right)  = {t}^{\alpha }\varphi \left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n}{t}^{n + \alpha }.
\]

(*)

> La fonction \( f \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( {\mathbb{R}}^{+ * } \) , et compte tenu de l’expression de la dérivée d’une fonction définie par une série entière, on a, pour tout \( t > 0 \) ,

The function \( f \) is of class \( {\mathcal{C}}^{\infty } \) on \( {\mathbb{R}}^{+ * } \) , and given the expression for the derivative of a function defined by a power series, we have, for all \( t > 0 \) ,

\[
{f}^{\prime }\left( t\right)  = \alpha {t}^{\alpha  - 1}\varphi \left( t\right)  + {t}^{\alpha }{\varphi }^{\prime }\left( t\right)  = \alpha {t}^{\alpha  - 1}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n}{t}^{n} + {t}^{\alpha }\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n{u}_{n}{t}^{n - 1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\alpha  + n}\right) {u}_{n}{t}^{n + \alpha  - 1}.
\]

En d'autres termes, on peut dériver terme à terme l'expression (*). De même, on montrerait \( {f}^{\prime \prime }\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\alpha + n}\right) \left( {\alpha + n - 1}\right) {t}^{n + \alpha - 2} \) . Maintenant, \( f \) vérifie l’équation différentielle \( \left( L\right) \) , donc

> In other words, we can differentiate the expression (*) term by term. Similarly, we could show \( {f}^{\prime \prime }\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\alpha + n}\right) \left( {\alpha + n - 1}\right) {t}^{n + \alpha - 2} \) . Now, \( f \) satisfies the differential equation \( \left( L\right) \) , so

\[
\forall t > 0,\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\alpha  + n}\right) \left( {\alpha  + n - 1}\right) {u}_{n}{t}^{n + \alpha } + \left( {a + 1}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\alpha  + n}\right) {u}_{n}{t}^{n + \alpha } + \left( {{t}^{2} + \frac{1}{4}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n}{t}^{n + \alpha }}\right)  = 0.
\]

Après division par \( {t}^{\alpha } \) , nous sommes en présence d’une série entière en \( t \) dont la somme est nulle pour tout \( t > 0 \) . On en déduit que ses coefficients sont nuls (voir la conséquence du corollaire 1 page 249), ce qui s'écrit

> After dividing by \( {t}^{\alpha } \) , we are left with a power series in \( t \) whose sum is zero for all \( t > 0 \) . We deduce that its coefficients are zero (see the consequence of corollary 1 on page 249), which is written as

\[
\left\lbrack  {\alpha \left( {\alpha  - 1}\right)  + \left( {a + 1}\right) \alpha  + \frac{1}{4}}\right\rbrack  {u}_{0} = 0
\]

\[
\left\lbrack  {\left( {\alpha  + 1}\right) \alpha  + \left( {a + 1}\right) \left( {\alpha  + 1}\right)  + \frac{1}{4}}\right\rbrack  {u}_{1} = 0
\]

\[
\left\lbrack  {\left( {\alpha  + 2}\right) \left( {\alpha  + 1}\right)  + \left( {a + 1}\right) \left( {\alpha  + 2}\right)  + \frac{1}{4}}\right\rbrack  {u}_{2} + {u}_{0} = 0
\]

... ... .

\[
\left\lbrack  {\left( {\alpha  + n}\right) \left( {\alpha  + n - 1}\right)  + \left( {a + 1}\right) \left( {\alpha  + n}\right)  + \frac{1}{4}}\right\rbrack  {u}_{n} + {u}_{n - 2} = 0.
\]

Autrement dit, si \( P \) est le polynôme \( P = X\left( {X - 1}\right) + \left( {a + 1}\right) X + 1/4 = {X}^{2} + {aX} + 1/4 \) , on a

> In other words, if \( P \) is the polynomial \( P = X\left( {X - 1}\right) + \left( {a + 1}\right) X + 1/4 = {X}^{2} + {aX} + 1/4 \) , we have

\[
P\left( \alpha \right) {u}_{0} = 0,\;P\left( {\alpha  + 1}\right) {u}_{1} = 0\;\text{ et }\;\forall n \geq  2,\;P\left( {\alpha  + n}\right) {u}_{n} + {u}_{n - 2} = 0.
\]

\( \left( {* * }\right) \)

> Les racines de \( P \) sont \( {\alpha }_{1} = - \frac{a}{2} + \frac{1}{2}\sqrt{{a}^{2} - 1} \) et \( {\alpha }_{2} = - \frac{a}{2} - \frac{1}{2}\sqrt{{a}^{2} - 1} \) .

The roots of \( P \) are \( {\alpha }_{1} = - \frac{a}{2} + \frac{1}{2}\sqrt{{a}^{2} - 1} \) and \( {\alpha }_{2} = - \frac{a}{2} - \frac{1}{2}\sqrt{{a}^{2} - 1} \) .

> Maintenant, choisissons \( \alpha = {\alpha }_{1} \) , de sorte que \( P\left( \alpha \right) = 0 \) et \( P\left( {\alpha + n}\right) \neq 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Partant de \( {u}_{0} = 1 \) , l’unique suite \( \left( {u}_{n}\right) \) vérifiant (**) est donnée par

Now, let us choose \( \alpha = {\alpha }_{1} \) , such that \( P\left( \alpha \right) = 0 \) and \( P\left( {\alpha + n}\right) \neq 0 \) for all \( n \in {\mathbb{N}}^{ * } \) . Starting from \( {u}_{0} = 1 \) , the unique sequence \( \left( {u}_{n}\right) \) satisfying (**) is given by

\[
\forall n \in  \mathbb{N},\;{u}_{2n} = \frac{1}{\mathop{\prod }\limits_{{k = 1}}^{n}P\left( {\alpha  + {2k}}\right) }\;\text{ et }\;{u}_{{2n} + 1} = 0.
\]

La série entière \( \sum {u}_{n}{t}^{n} = \sum {u}_{2n}{t}^{2n} \) a un rayon de convergence infini car \( {u}_{2n}/{u}_{{2n} - 2} = 1/P(\alpha + \) 2n) donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{2n}/{u}_{{2n} - 2} = 0 \) (voir la règle de D’Alembert, page 248). De plus, elle vérifie par construction la relation de récurrence (**), donc si \( \varphi \) désigne sa somme, \( t \mapsto {t}^{\alpha }\varphi \left( t\right) \) vérifie l’équation différentielle \( \left( L\right) \) et \( \varphi \left( 0\right) = {u}_{0} = 1 \neq 0 \) .

> The power series \( \sum {u}_{n}{t}^{n} = \sum {u}_{2n}{t}^{2n} \) has an infinite radius of convergence because \( {u}_{2n}/{u}_{{2n} - 2} = 1/P(\alpha + \) 2n) thus \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{2n}/{u}_{{2n} - 2} = 0 \) (see D’Alembert’s ratio test, page 248). Furthermore, it satisfies the recurrence relation (**) by construction, so if \( \varphi \) denotes its sum, \( t \mapsto {t}^{\alpha }\varphi \left( t\right) \) satisfies the differential equation \( \left( L\right) \) and \( \varphi \left( 0\right) = {u}_{0} = 1 \neq 0 \) .

b) Si \( {a}^{2} - 1 \) n’est pas le carré d’un entier, alors les deux racines \( {\alpha }_{1} \) et \( {\alpha }_{2} \) du polynôme \( P \) exhibé plus haut ne différent pas d’un entier (car \( {\alpha }_{1} - {\alpha }_{2} = \sqrt{{a}^{2} - 1} \) ), et l’opération effectuée plus haut en remplaçant \( \alpha \) par \( {\alpha }_{1} \) peut être reprise telle quelle en remplaçant \( \alpha \) par \( {\alpha }_{2} \) (car \( P\left( {\alpha }_{2}\right) = 0 \) et \( P\left( {{\alpha }_{2} + n}\right) \neq 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) ). Ainsi, nous avons prouvé l’existence de deux séries entières dont les sommes \( \varphi \) et \( \psi \) sont non nulles en 0 et telles que \( t \mapsto {t}^{{\alpha }_{1}}\varphi \left( t\right) \) et \( t \mapsto {t}^{{\alpha }_{2}}\psi \left( t\right) \) sont solutions de \( \left( L\right) \) . Ces deux solutions sont linéairement indépendantes, car si \( \lambda {t}^{{\alpha }_{1}}\varphi \left( t\right) + \mu {t}^{{\alpha }_{2}}\psi \left( t\right) = 0 \) pour tout \( t > 0 \) , alors \( \lambda {t}^{{\alpha }_{1} - {\alpha }_{2}}\varphi \left( t\right) + {\mu \psi }\left( t\right) = 0 \) , et en faisant tendre \( t \) vers \( {0}^{ + } \) , on obtient \( {\mu \psi }\left( 0\right) = \mu = 0 \) (car \( {\alpha }_{2} < {\alpha }_{1} \) ), puis on conclut facilement \( \lambda = 0 \) . On sait par ailleurs que l’ensemble des solutions de \( \left( L\right) \) sur \( {\mathbb{R}}^{+ * } \) forme un e.v de dimension 2, et on en conclut que la solution générale de \( \left( L\right) \) est \( t \mapsto \lambda {t}^{{\alpha }_{1}}\varphi \left( t\right) + \mu {t}^{{\alpha }_{2}}\psi \left( t\right) \) . Nous connaissons \( {\alpha }_{1},{\alpha }_{2} \) , et nous savons donner des relations de récurrence permettant de calculer les coefficients de \( \varphi \) et \( \psi \) . Ceci nous permet d’obtenir un développement asymptotique de la solution générale de \( \left( L\right) \) .

> b) If \( {a}^{2} - 1 \) is not the square of an integer, then the two roots \( {\alpha }_{1} \) and \( {\alpha }_{2} \) of the polynomial \( P \) exhibited above do not differ by an integer (since \( {\alpha }_{1} - {\alpha }_{2} = \sqrt{{a}^{2} - 1} \) ), and the operation performed above by replacing \( \alpha \) with \( {\alpha }_{1} \) can be repeated as is by replacing \( \alpha \) with \( {\alpha }_{2} \) (since \( P\left( {\alpha }_{2}\right) = 0 \) and \( P\left( {{\alpha }_{2} + n}\right) \neq 0 \) for all \( n \in {\mathbb{N}}^{ * } \) ). Thus, we have proven the existence of two power series whose sums \( \varphi \) and \( \psi \) are non-zero at 0 and such that \( t \mapsto {t}^{{\alpha }_{1}}\varphi \left( t\right) \) and \( t \mapsto {t}^{{\alpha }_{2}}\psi \left( t\right) \) are solutions of \( \left( L\right) \) . These two solutions are linearly independent, because if \( \lambda {t}^{{\alpha }_{1}}\varphi \left( t\right) + \mu {t}^{{\alpha }_{2}}\psi \left( t\right) = 0 \) for all \( t > 0 \) , then \( \lambda {t}^{{\alpha }_{1} - {\alpha }_{2}}\varphi \left( t\right) + {\mu \psi }\left( t\right) = 0 \) , and by letting \( t \) tend to \( {0}^{ + } \) , we obtain \( {\mu \psi }\left( 0\right) = \mu = 0 \) (since \( {\alpha }_{2} < {\alpha }_{1} \) ), and then we easily conclude \( \lambda = 0 \) . We also know that the set of solutions of \( \left( L\right) \) on \( {\mathbb{R}}^{+ * } \) forms a vector space of dimension 2, and we conclude that the general solution of \( \left( L\right) \) is \( t \mapsto \lambda {t}^{{\alpha }_{1}}\varphi \left( t\right) + \mu {t}^{{\alpha }_{2}}\psi \left( t\right) \) . We know \( {\alpha }_{1},{\alpha }_{2} \) , and we know how to provide recurrence relations to calculate the coefficients of \( \varphi \) and \( \psi \) . This allows us to obtain an asymptotic expansion of the general solution of \( \left( L\right) \) .

Traitons maintenant le cas où \( {a}^{2} - 1 = {m}^{2} \) , avec \( m \in \mathbb{N} \) . Soit \( \Phi : t \mapsto {t}^{\alpha }\varphi \left( t\right) \) la solution de \( \left( L\right) \) trouvée à la question précédente. Munis de cette solution de \( \left( L\right) \) , nous allons déterminer la solution générale de \( \left( L\right) \) grâce à la méthode d’abaissement de l’ordre décrite à la page 380 : on cherche la solution générale \( f \) de \( \left( L\right) \) sous la forme \( f\left( t\right) = g\left( t\right) \Phi \left( t\right) \) , où \( g \) est une fonction de classe \( {\mathcal{C}}^{2} \) encore inconnue (la fonction \( \Phi \) est \( > 0 \) sur \( {\mathbb{R}}^{+ * } \) donc ne s’y annule pas, car par construction, tous les coefficients de \( \varphi \) sont strictement positifs on nuls). En remplaçant dans \( \left( L\right) \) , on obtient

> Let us now treat the case where \( {a}^{2} - 1 = {m}^{2} \) , with \( m \in \mathbb{N} \) . Let \( \Phi : t \mapsto {t}^{\alpha }\varphi \left( t\right) \) be the solution to \( \left( L\right) \) found in the previous question. Equipped with this solution to \( \left( L\right) \) , we will determine the general solution to \( \left( L\right) \) using the order reduction method described on page 380: we seek the general solution \( f \) of \( \left( L\right) \) in the form \( f\left( t\right) = g\left( t\right) \Phi \left( t\right) \) , where \( g \) is a function of class \( {\mathcal{C}}^{2} \) that is still unknown (the function \( \Phi \) is \( > 0 \) on \( {\mathbb{R}}^{+ * } \) and therefore does not vanish there, because by construction, all coefficients of \( \varphi \) are strictly positive or zero). Substituting into \( \left( L\right) \) , we obtain

\[
0 = {t}^{2}\left( {{g}^{\prime \prime }\Phi  + 2{g}^{\prime }{\Phi }^{\prime } + g{\Phi }^{\prime \prime }}\right)  + \left( {a + 1}\right) t\left( {{g}^{\prime }\Phi  + g{\Phi }^{\prime }}\right)  + \left( {{t}^{2} + \frac{1}{4}}\right) \left( {g\Phi }\right)
\]

\[
= g\left\lbrack  {{t}^{2}{\Phi }^{\prime \prime } + \left( {a + 1}\right) t{\Phi }^{\prime } + \left( {{t}^{2} + \frac{1}{4}}\right) \Phi }\right\rbrack   + t\left\lbrack  {t{g}^{\prime \prime }\Phi  + {g}^{\prime }\left( {{2t}{\Phi }^{\prime } + \left( {a + 1}\right) \Phi }\right) }\right\rbrack
\]

et comme \( \Phi \) est solution de \( \left( L\right) \) , on voit que \( f = {g\Phi } \) sera solution de \( \left( L\right) \) si et seulement si \( {g}^{\prime } \) est solution de l’équation différentielle \( \left( {L}^{\prime }\right) : t{y}^{\prime }\Phi + y\left( {{2t}{\Phi }^{\prime } + \left( {a + 1}\right) \Phi }\right) = 0 \) . Les solutions de \( \left( {L}^{\prime }\right) \) sont les fonctions de la forme \( t \mapsto \lambda \exp \left( {-F\left( t\right) }\right) \) , où \( \lambda \) est une constante réelle et \( F \) une primitive de \( 2{\Phi }^{\prime }/\Phi + \left( {a + 1}\right) /t \) sur \( {\mathbb{R}}^{+ * } \) . On peut prendre pour \( F \) la fonction définie par \( F\left( t\right) = 2\log \Phi + \left( {a + 1}\right) \log t \) , donc finalement, la solution générale de \( \left( {L}^{\prime }\right) \) est

> and since \( \Phi \) is a solution to \( \left( L\right) \) , we see that \( f = {g\Phi } \) will be a solution to \( \left( L\right) \) if and only if \( {g}^{\prime } \) is a solution to the differential equation \( \left( {L}^{\prime }\right) : t{y}^{\prime }\Phi + y\left( {{2t}{\Phi }^{\prime } + \left( {a + 1}\right) \Phi }\right) = 0 \) . The solutions to \( \left( {L}^{\prime }\right) \) are functions of the form \( t \mapsto \lambda \exp \left( {-F\left( t\right) }\right) \) , where \( \lambda \) is a real constant and \( F \) is an antiderivative of \( 2{\Phi }^{\prime }/\Phi + \left( {a + 1}\right) /t \) on \( {\mathbb{R}}^{+ * } \) . We can take for \( F \) the function defined by \( F\left( t\right) = 2\log \Phi + \left( {a + 1}\right) \log t \) , so finally, the general solution to \( \left( {L}^{\prime }\right) \) is

\[
t \mapsto  \lambda \frac{1}{\Phi {\left( t\right) }^{2}}{t}^{-\left( {a + 1}\right) } = \lambda \frac{{t}^{-2{\alpha }_{1} - a - 1}}{\varphi {\left( t\right) }^{2}} = \lambda \frac{{t}^{-m - 1}}{\varphi {\left( t\right) }^{2}},\;\lambda  \in  \mathbb{R}.
\]

\( \left( {* * * }\right) \)

> La fonction \( t \mapsto 1/\varphi {\left( t\right) }^{2} \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( {\mathbb{R}}^{ + } \) . On considère son développement limité en 0 jusqu’à un ordre \( p \geq m \) :

The function \( t \mapsto 1/\varphi {\left( t\right) }^{2} \) is of class \( {\mathcal{C}}^{\infty } \) on \( {\mathbb{R}}^{ + } \) . We consider its Taylor expansion at 0 up to an order \( p \geq m \) :

\[
\frac{1}{\varphi {\left( t\right) }^{2}} = {a}_{0} + {a}_{1}t + {a}_{2}{t}^{2} + \cdots  + {a}_{p}{t}^{p} + o\left( {t}^{p}\right)
\]

(on connaît les coefficients de \( \varphi \) , on peut donc calculer les coefficients du développement limité de \( 1/{\varphi }^{2} \) ), de sorte qu’un développement asymptotique de (***) en \( {0}^{ + } \) à la constante multiplicative \( \lambda \) près est

> (we know the coefficients of \( \varphi \) , so we can calculate the coefficients of the Taylor expansion of \( 1/{\varphi }^{2} \) ), such that an asymptotic expansion of (***) at \( {0}^{ + } \) up to a multiplicative constant \( \lambda \) is

\[
\frac{{a}_{0}}{{t}^{m + 1}} + \frac{{a}_{1}}{{t}^{m}} + \cdots  + \frac{{a}_{m - 1}}{{t}^{2}} + \frac{{a}_{m}}{t} + {a}_{m + 1} + \cdots  + {a}_{p}{t}^{p - m - 1} + o\left( {t}^{p - m - 1}\right) .
\]

Comme \( {g}^{\prime } \) est solution de \( \left( {L}^{\prime }\right) \) , on en déduit par intégration qu’un développement asymptotique de \( g \) est,à une constante multiplicative près,

> Since \( {g}^{\prime } \) is a solution to \( \left( {L}^{\prime }\right) \) , we deduce by integration that an asymptotic expansion of \( g \) is, up to a multiplicative constant,

\[
c - \frac{{a}_{0}}{m}\frac{1}{{t}^{m}} - \cdots  - \frac{{a}_{m - 1}}{t} + {a}_{m}\log t + {a}_{m + 1}t + \cdots  + \frac{{a}_{p}}{p - m}{t}^{p - m} + o\left( {t}^{p - m}\right) ,
\]

où \( c \) est une constante réelle. Maintenant, il ne reste plus qu’à écrire que la solution générale de \( \left( L\right) \) est le produit de \( g \) par \( \Phi \) , pour obtenir un développement asymptotique de la solution générale de \( \left( L\right) \) . (Le point remarquable ici est la présence d'un logarithme dans le développement asymptotique).

> where \( c \) is a real constant. Now, it only remains to write that the general solution to \( \left( L\right) \) is the product of \( g \) by \( \Phi \) , to obtain an asymptotic expansion of the general solution to \( \left( L\right) \) . (The remarkable point here is the presence of a logarithm in the asymptotic expansion).

c) Pour étudier le comportement asymptotique en \( + \infty \) , on va effectuer le changement de variable \( u = 1/t \) pour se ramener en 0 . Posons donc \( z\left( t\right) = y\left( {1/t}\right) \) , de sorte que \( y\left( t\right) = z\left( {1/t}\right) \) . Comme

> c) To study the asymptotic behavior at \( + \infty \), we will perform the change of variable \( u = 1/t \) to reduce it to 0. Let us therefore set \( z\left( t\right) = y\left( {1/t}\right) \), such that \( y\left( t\right) = z\left( {1/t}\right) \). Since

\[
{y}^{\prime }\left( t\right)  =  - \frac{1}{{t}^{2}}{z}^{\prime }\left( \frac{1}{t}\right) \;\text{ et }\;{y}^{\prime \prime }\left( t\right)  = \frac{1}{{t}^{4}}{z}^{\prime \prime }\left( \frac{1}{t}\right)  + \frac{2}{{t}^{3}}{z}^{\prime }\left( \frac{1}{t}\right) ,
\]

on voit que \( y \) est solution de \( \left( E\right) \) sur \( {\mathbb{R}}^{+ * } \) si et seulement si

> we see that \( y \) is a solution of \( \left( E\right) \) on \( {\mathbb{R}}^{+ * } \) if and only if

\[
\forall t > 0,\;0 = {z}^{\prime \prime }\left( \frac{1}{t}\right)  + \frac{8}{3}t{z}^{\prime }\left( \frac{1}{t}\right)  + \left( {1 + \frac{{t}^{2}}{4}}\right) z\left( \frac{1}{t}\right) .
\]

En posant \( u = 1/t \) , ceci est équivalent à dire que \( z \) est solution de l’équation différentielle \( \left( {E}^{\prime }\right) : {u}^{2}{z}^{\prime \prime } + \frac{8}{3}u{z}^{\prime } + \left( {{u}^{2} + \frac{1}{4}}\right) z = 0 \) . On s’est ramené à une équation différentielle du type précédent avec \( a = 5/3 \) , et il s’agit de montrer qu’il existe une unique solution \( g \) de \( \left( {E}^{\prime }\right) \) sur \( {\mathbb{R}}^{+ * } \) telle que \( g\left( u\right) \sim {u}^{-1/6} \) au voisinage de 0 .

> By setting \( u = 1/t \), this is equivalent to saying that \( z \) is a solution of the differential equation \( \left( {E}^{\prime }\right) : {u}^{2}{z}^{\prime \prime } + \frac{8}{3}u{z}^{\prime } + \left( {{u}^{2} + \frac{1}{4}}\right) z = 0 \). We have reduced it to a differential equation of the previous type with \( a = 5/3 \), and it is a matter of showing that there exists a unique solution \( g \) of \( \left( {E}^{\prime }\right) \) on \( {\mathbb{R}}^{+ * } \) such that \( g\left( u\right) \sim {u}^{-1/6} \) in the neighborhood of 0.

En reprenant les notations précédentes, le polynôme \( P \) est ici \( P = X\left( {X - 1}\right) + \frac{8}{3}X + \frac{1}{4} = \; {X}^{2} + \frac{5}{3} + \frac{1}{4} \) , dont les racines sont \( {\alpha }_{1} = - \frac{3}{2} \) et \( {\alpha }_{2} = - \frac{1}{6} \) . Ces deux racines ne diffèrent pas d’un entier, nous sommes donc dans les conditions du premier cas traité à la question précédente. Nous avions montré qu’une base de solutions de \( \left( {E}^{\prime }\right) \) est constitué des fonctions \( u \mapsto {u}^{{\alpha }_{1}}\varphi \left( u\right) \) et \( u \mapsto {u}^{{\alpha }_{2}}\psi \left( u\right) \) , où \( \varphi \) et \( \psi \) sont les sommes de deux séries entières de rayon de convergence infini, non nulles en 0, dont les coefficients sont déterminés grâce à la relation de récurrence (**). Vues les valeurs \( {\alpha }_{1} = - 3/2 \) et \( {\alpha }_{2} = - 1/6 \) , on voit qu’il existe une unique solution \( g \) de \( \left( {E}^{\prime }\right) \) équivalente à \( {u}^{-1/6} \) en \( {0}^{ + } \) , qui est la fonction \( u \mapsto {u}^{-1/6}\psi \left( t\right) \) , où \( \psi \left( u\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n}{u}^{n} \) avec

> Using the previous notation, the polynomial \( P \) is here \( P = X\left( {X - 1}\right) + \frac{8}{3}X + \frac{1}{4} = \; {X}^{2} + \frac{5}{3} + \frac{1}{4} \), whose roots are \( {\alpha }_{1} = - \frac{3}{2} \) and \( {\alpha }_{2} = - \frac{1}{6} \). These two roots do not differ by an integer, so we are in the conditions of the first case treated in the previous question. We showed that a basis of solutions for \( \left( {E}^{\prime }\right) \) consists of the functions \( u \mapsto {u}^{{\alpha }_{1}}\varphi \left( u\right) \) and \( u \mapsto {u}^{{\alpha }_{2}}\psi \left( u\right) \), where \( \varphi \) and \( \psi \) are the sums of two power series with an infinite radius of convergence, non-zero at 0, whose coefficients are determined by the recurrence relation (**). Given the values \( {\alpha }_{1} = - 3/2 \) and \( {\alpha }_{2} = - 1/6 \), we see that there exists a unique solution \( g \) of \( \left( {E}^{\prime }\right) \) equivalent to \( {u}^{-1/6} \) at \( {0}^{ + } \), which is the function \( u \mapsto {u}^{-1/6}\psi \left( t\right) \), where \( \psi \left( u\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n}{u}^{n} \) with

\[
{u}_{0} = 1,\;\forall n \in  {\mathbb{N}}^{ * },\;{u}_{2n} = \frac{1}{\mathop{\prod }\limits_{{k = 1}}^{n}P\left( {{\alpha }_{2} + k}\right) }\;\text{ et }\;{u}_{{2n} - 1} = 0.
\]

De menus calculs nous donnent \( {u}_{0} = 1,{u}_{2} = - 3/{20} \) et \( {u}_{4} = 9/{1280} \) , donc \( g\left( u\right) = {u}^{-1/6}(1 - \; \frac{3}{20}{u}^{2} + \frac{9}{1280}{u}^{4} + O\left( {u}^{6}\right) ) \) . Comme \( f\left( t\right) = g\left( {1/t}\right) \) , on en conclut finalement que lorsque \( t \rightarrow + \infty \) ,

> Minor calculations give us \( {u}_{0} = 1,{u}_{2} = - 3/{20} \) and \( {u}_{4} = 9/{1280} \), so \( g\left( u\right) = {u}^{-1/6}(1 - \; \frac{3}{20}{u}^{2} + \frac{9}{1280}{u}^{4} + O\left( {u}^{6}\right) ) \). Since \( f\left( t\right) = g\left( {1/t}\right) \), we finally conclude that when \( t \rightarrow + \infty \),

\[
f\left( t\right)  = {t}^{1/6} - \frac{3}{20}{t}^{-{11}/6} + \frac{9}{1280}{t}^{-{23}/6} + O\left( {t}^{-{35}/6}\right) .
\]

Remarque. L’équation \( P\left( \alpha \right) = 0 \) de l’exercice s’appelle équation indicielle de l’équation différentielle \( \left( L\right) \) .

> Remark. The equation \( P\left( \alpha \right) = 0 \) from the exercise is called the indicial equation of the differential equation \( \left( L\right) \) .

Cet exercice est un cas particulier du théorème de Fuchs portant sur les points singu-liers réguliers d'une équation différentielle linéaire. Dans le cas des équations différentielles du type

> This exercise is a special case of Fuchs' theorem concerning the regular singular points of a linear differential equation. In the case of differential equations of the type

\[
{t}^{n}{p}_{n}\left( t\right) {y}^{\left( n\right) } + {t}^{n - 1}{p}_{n - 1}\left( t\right) {y}^{\left( n - 1\right) } + \cdots  + t{p}_{1}\left( t\right) {y}^{\prime } + {p}_{0}\left( t\right) y = 0, \tag{E}
\]

(0 est singulier pour \( \left( E\right) \) car le terme dominant s’annule en 0 ) où les \( {p}_{i}\left( t\right) \) sont des polynômes en \( t \) et \( {p}_{n}\left( 0\right) \neq 0 \) , ce dernier s’exprime comme suit : si l’équation indicielle de (E), définie par

> (0 is singular for \( \left( E\right) \) because the leading term vanishes at 0) where the \( {p}_{i}\left( t\right) \) are polynomials in \( t \) and \( {p}_{n}\left( 0\right) \neq 0 \) , the latter is expressed as follows: if the indicial equation of (E), defined by

\[
\alpha \left( {\alpha  - 1}\right) \cdots \left( {\alpha  - n + 1}\right) {p}_{n}\left( 0\right)  + \cdots  + \alpha \left( {\alpha  - 1}\right) {p}_{2}\left( 0\right)  + \alpha {p}_{1}\left( 0\right)  + {p}_{0}\left( 0\right)  = 0,
\]

est telle que deux de ses racines \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) ne diffèrent jamais d’un entier, alors une base des solutions de \( \left( E\right) \) est constituée de fonctions de la forme \( t \mapsto {t}^{{\alpha }_{i}}{\varphi }_{i}\left( t\right) \) , où \( {\varphi }_{i} \) est la somme d'une série entière dont le rayon de convergence est non nul, et dont les coefficients peuvent être déterminés par une relation de récurrence obtenue en remplaçant formellement cette solution dans \( \left( E\right) \) . Lorsque certains des \( {\alpha }_{i} \) diffèrent d’un entier, c’est plus délicat, et on voit apparaître des comportements en \( \log t \) en voisinage de \( {0}^{ + } \) .

> is such that two of its roots \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) never differ by an integer, then a basis of solutions for \( \left( E\right) \) consists of functions of the form \( t \mapsto {t}^{{\alpha }_{i}}{\varphi }_{i}\left( t\right) \) , where \( {\varphi }_{i} \) is the sum of a power series with a non-zero radius of convergence, and whose coefficients can be determined by a recurrence relation obtained by formally substituting this solution into \( \left( E\right) \) . When some of the \( {\alpha }_{i} \) differ by an integer, it is more delicate, and behaviors in \( \log t \) appear in the neighborhood of \( {0}^{ + } \) .

Les équations différentielles linéaires à coefficients polynomiaux sont appelées équa-tions holonomes. Parmi ce type d'équations, on peut trouver des solutions avec d'autres types de singularités, qui font apparaître des comportements en \( {\left( \log t\right) }^{k}{t}^{\alpha }{e}^{c{t}^{\beta }} \) au voisinage de l'origine.

> Linear differential equations with polynomial coefficients are called holonomic equations. Among this type of equation, one can find solutions with other types of singularities, which give rise to behaviors in \( {\left( \log t\right) }^{k}{t}^{\alpha }{e}^{c{t}^{\beta }} \) in the neighborhood of the origin.

ANNEXE A

> APPENDIX A

##### Baire's Theorem and applications

*Français : Théorème de Baire et applications*

Cette annexe présente, sous forme d'une série d'exercices, le théorème de Baire, suivi de plusieurs applications, notamment le théorème de Banach-Steinhaus. Ces notions ne sont pas au programme des classes de mathématiques spéciales, mais elles constituent une fort jolie théorie tout à fait accessible. Certains résultats sont surprenants, comme par exemple

> This appendix presents, in the form of a series of exercises, Baire's theorem, followed by several applications, notably the Banach-Steinhaus theorem. These concepts are not in the curriculum for special mathematics classes, but they constitute a very beautiful and quite accessible theory. Some results are surprising, such as, for example,

— l'ensemble des points de continuité d'une fonction dérivée est dense (exemple his-torique dû à Baire lui-même, voir l'exercice 2 page 419) ;

> — the set of points of continuity of a derivative function is dense (a historical example due to Baire himself, see exercise 2 on page 419);

- l'ensemble des fonctions continues nulle part dérivables est dense dans l'ensemble des fonctions continues. Cette "plaie lamentable" dont se détournait Hermite est plus étendue que l'on ne pourrait le penser (voir l'exercice 4 page 421) ;

> - the set of continuous nowhere differentiable functions is dense in the set of continuous functions. This "lamentable plague" from which Hermite turned away is more widespread than one might think (see exercise 4 on page 421);

- un endomorphisme bijectif et continu sur un espace de Banach a son inverse continu (théorème de Banach, voir l'exercice 6 page 423).

> - a bijective and continuous endomorphism on a Banach space has a continuous inverse (Banach's theorem, see exercise 6 on page 423).

##### Baire's theorem

*Français : Le théorème de Baire*

EXERCICE 0 (THÉORÉME DE BAIRE).

> EXERCISE 0 (BAIRE'S THEOREM).

DÉFINITION 1. On dit qu'un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est un espace de Baire si toute intersection dénombrable d’ouverts denses dans \( E \) est dense dans \( E \) , autrement dit si

> DEFINITION 1. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is said to be a Baire space if every countable intersection of dense open sets in \( E \) is dense in \( E \) , in other words if

(i) pour toute suite d’ouverts \( {\left( {O}_{n}\right) }_{n \in \mathbb{N}} \) telle que \( \forall n \in \mathbb{N},\overline{{O}_{n}} = E,\;\overline{{ \cap }_{n \in \mathbb{N}}{O}_{n}} = E \) .

> (i) for any sequence of open sets \( {\left( {O}_{n}\right) }_{n \in \mathbb{N}} \) such that \( \forall n \in \mathbb{N},\overline{{O}_{n}} = E,\;\overline{{ \cap }_{n \in \mathbb{N}}{O}_{n}} = E \) .

1 / a) Montrer que cette définition est équivalente à la suivante :

> 1 / a) Show that this definition is equivalent to the following:

(ii) Toute réunion dénombrable de fermés d'intérieurs vides de \( E \) est d'intérieur vide dans \( E \) .

> (ii) Any countable union of closed sets with empty interiors in \( E \) has an empty interior in \( E \) .

DéFINITION 2. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace de Baire et \( A \) une partie de \( E \) .

> DEFINITION 2. Let \( \left( {E,\mathrm{\;d}}\right) \) be a Baire space and \( A \) a subset of \( E \) .

- On dit que \( A \) est un résiduel si elle contient une intersection dénombrable d’ouverts denses dans \( E \) .

> - We say that \( A \) is a residual set if it contains a countable intersection of dense open sets in \( E \) .

- On dit que \( A \) est maigre si elle est contenue dans une réunion dénombrable de fermés de \( E \) d’intérieurs vides.

> - We say that \( A \) is meager if it is contained in a countable union of closed sets of \( E \) with empty interiors.

b) Montrer qu’une partie \( A \) d’un espace de Baire \( E \) est maigre si et seulement si \( E \smallsetminus A \) est un résiduel.

> b) Show that a subset \( A \) of a Baire space \( E \) is meager if and only if \( E \smallsetminus A \) is a residual set.

2/ (Théorème de Baire.) Montrer que tout espace métrique complet est un espace de Baire.

> 2/ (Baire's Theorem.) Show that every complete metric space is a Baire space.

3/ (Un lemme utile dans les applications.) Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace de Baire et \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fermés de \( E \) telle que \( { \cup }_{n \in \mathbb{N}}{F}_{n} = E \) . Montrer que l’ouvert \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) est dense dans E.

> 3/ (A useful lemma for applications.) Let \( \left( {E,\mathrm{\;d}}\right) \) be a Baire space and \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) a sequence of closed sets of \( E \) such that \( { \cup }_{n \in \mathbb{N}}{F}_{n} = E \) . Show that the open set \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) is dense in E.

Solution. 1/ a) (i) \( \Rightarrow \) (ii). Soit \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fermés d’intérieurs vides. Pour tout \( n \) , l’ouvert \( {O}_{n} = E \smallsetminus {F}_{n} \) est dense dans \( E \) car \( \overline{E \smallsetminus {F}_{n}} = E \smallsetminus {F}_{n} = E \) . Ainsi, d’après (i),

> Solution. 1/ a) (i) \( \Rightarrow \) (ii). Let \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of closed sets with empty interiors. For all \( n \) , the open set \( {O}_{n} = E \smallsetminus {F}_{n} \) is dense in \( E \) because \( \overline{E \smallsetminus {F}_{n}} = E \smallsetminus {F}_{n} = E \) . Thus, according to (i),

\[
\mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}{O}_{n} = \mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}\left( {E \smallsetminus  {F}_{n}}\right)  = E \smallsetminus  \left\lbrack  {\mathop{\bigcup }\limits_{{n \in  \mathbb{N}}}{F}_{n}}\right\rbrack
\]

est dense dans \( E \) , c’est-à-dire : \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) est d’intérieur vide.

> is dense in \( E \) , that is to say: \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) has an empty interior.

L’implication (ii) \( \Rightarrow \) (i) se traite de la même manière en considérant les fermés \( {F}_{n} = \; E \smallsetminus {O}_{n} \) .

> The implication (ii) \( \Rightarrow \) (i) is handled in the same way by considering the closed sets \( {F}_{n} = \; E \smallsetminus {O}_{n} \) .

b) Soit \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fermés d’intérieurs vides. Pour tout \( n \in \mathbb{N} \) , posons \( {O}_{n} = E \smallsetminus {F}_{n} \) , ouvert dense dans \( E \) . On a

> b) Let \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of closed sets with empty interiors. For all \( n \in \mathbb{N} \) , let \( {O}_{n} = E \smallsetminus {F}_{n} \) , an open dense set in \( E \) . We have

\[
\left( {A \subset  \left\lbrack  {\mathop{\bigcup }\limits_{{n \in  \mathbb{N}}}{F}_{n}}\right\rbrack  }\right)  \Leftrightarrow  \left( {E \smallsetminus  A}\right)  \supset  E \smallsetminus  \left\lbrack  {\mathop{\bigcup }\limits_{{n \in  \mathbb{N}}}{F}_{n}}\right\rbrack   = \mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}\left( {E \smallsetminus  {F}_{n}}\right)  = \mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}{O}_{n},
\]

et on en déduit facilement que \( A \) est maigre si et seulement si \( E \smallsetminus A \) est un résiduel. (Au passage, remarquons par définition d'un espace de Baire, qu'un ensemble maigre est d'intérieur vide et qu'un résiduel est dense dans \( E \) .)

> and we easily deduce that \( A \) is meager if and only if \( E \smallsetminus A \) is a residual set. (Incidentally, note by the definition of a Baire space that a meager set has an empty interior and a residual set is dense in \( E \) .)

2/ Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique complet et \( {\left( {O}_{n}\right) }_{n \in \mathbb{N}} \) une suite d’ouverts denses dans \( E \) . Pour montrer que \( { \cap }_{n \in \mathbb{N}}{O}_{n} \) est dense dans \( E \) , il faut montrer

> 2/ Let \( \left( {E,\mathrm{\;d}}\right) \) be a complete metric space and \( {\left( {O}_{n}\right) }_{n \in \mathbb{N}} \) a sequence of dense open sets in \( E \) . To show that \( { \cap }_{n \in \mathbb{N}}{O}_{n} \) is dense in \( E \) , we must show

\[
\forall V\text{ ouvert non vide de }E,\;V \cap  \left\lbrack  {\mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}{O}_{n}}\right\rbrack   \neq  \varnothing .
\]

Donnons nous donc un ouvert non vide \( V \) de \( E \) . Par récurrence, on va construire une suite \( \left( {B}_{n}\right) \) de boules fermées de \( E \) telles que

> Let us therefore take a non-empty open set \( V \) of \( E \) . By induction, we will construct a sequence \( \left( {B}_{n}\right) \) of closed balls of \( E \) such that

(I) \( \forall n \in \mathbb{N},{B}_{n} \) est une boule fermée de rayon non nul et inférieur à \( 1/{2}^{n} \) .

> (I) \( \forall n \in \mathbb{N},{B}_{n} \) is a closed ball with a non-zero radius less than \( 1/{2}^{n} \) .

(II) \( {B}_{0} \subset {O}_{0} \cap V \) et \( \forall n \in \mathbb{N},{B}_{n + 1} \subset {O}_{n + 1} \cap {B}_{n} \) .

> (II) \( {B}_{0} \subset {O}_{0} \cap V \) and \( \forall n \in \mathbb{N},{B}_{n + 1} \subset {O}_{n + 1} \cap {B}_{n} \) .

L’ouvert \( {O}_{0} \) est dense dans \( E \) donc \( {O}_{0} \cap V \neq \varnothing \) . Or \( {O}_{0} \cap V \) est ouvert, il existe donc une boule ouverte \( \mathrm{B}\left( {{x}_{0}, r}\right) \subset {O}_{0} \cap V \) . Si \( {B}_{0} \) est la boule fermée de centre \( {x}_{0} \) et de rayon \( \inf \{ r/2,1\} \) , on a donc \( {B}_{0} \subset {O}_{0} \cap V \) .

> The open set \( {O}_{0} \) is dense in \( E \) so \( {O}_{0} \cap V \neq \varnothing \) . However, \( {O}_{0} \cap V \) is open, so there exists an open ball \( \mathrm{B}\left( {{x}_{0}, r}\right) \subset {O}_{0} \cap V \) . If \( {B}_{0} \) is the closed ball with center \( {x}_{0} \) and radius \( \inf \{ r/2,1\} \) , then we have \( {B}_{0} \subset {O}_{0} \cap V \) .

Supposons les boules \( {B}_{0},\ldots ,{B}_{n} \) construites et vérifiant (I) et (II). L’ouvert \( {O}_{n + 1} \) est dense dans \( E \) , donc \( {O}_{n + 1} \cap {B}_{n} \) est un ouvert non vide. Il existe donc une boule ouverte \( \mathrm{B}\left( {x, r}\right) \) incluse dans \( {O}_{n + 1} \cap {B}_{n} \) . Si \( {B}_{n + 1} \) désigne le boule fermée de centre \( x \) et de rayon \( \inf \left\{ {r/2,1/{2}^{n + 1}}\right\} \) on a donc \( {B}_{n + 1} \subset {O}_{n + 1} \cap {B}_{n} \) . Ainsi, \( {B}_{n + 1} \) vérifie (I) et (II).

> Suppose the balls \( {B}_{0},\ldots ,{B}_{n} \) are constructed and satisfy (I) and (II). The open set \( {O}_{n + 1} \) is dense in \( E \) , so \( {O}_{n + 1} \cap {B}_{n} \) is a non-empty open set. There therefore exists an open ball \( \mathrm{B}\left( {x, r}\right) \) included in \( {O}_{n + 1} \cap {B}_{n} \) . If \( {B}_{n + 1} \) denotes the closed ball with center \( x \) and radius \( \inf \left\{ {r/2,1/{2}^{n + 1}}\right\} \) , we then have \( {B}_{n + 1} \subset {O}_{n + 1} \cap {B}_{n} \) . Thus, \( {B}_{n + 1} \) satisfies (I) and (II).

Par construction, \( {\left( {B}_{n}\right) }_{n \in \mathbb{N}} \) est une suite décroissante de fermés non vides de \( E \) dont le diamètre tend vers 0 . De plus \( E \) est complet, il existe donc \( x \in E \) tel que \( { \cap }_{n \in \mathbb{N}}{B}_{n} = \{ x\} \) (voir la proposition 9 de la page 20). Or \( {B}_{0} \subset V \) , donc \( x \in V \) . D’après (II), on a aussi \( {B}_{n} \subset {O}_{n} \) pour tout \( n \) , donc \( x \in {O}_{n} \) pour tout \( n \) . Ainsi, \( x \in { \cap }_{n \in \mathbb{N}}{O}_{n} \) . Finalement, nous avons prouvé que \( V \) et \( { \cap }_{n \in \mathbb{N}}{O}_{n} \) ont au moins un point commun, d’où le théorème.

> By construction, \( {\left( {B}_{n}\right) }_{n \in \mathbb{N}} \) is a decreasing sequence of non-empty closed sets of \( E \) whose diameter tends to 0 . Moreover, \( E \) is complete, so there exists \( x \in E \) such that \( { \cap }_{n \in \mathbb{N}}{B}_{n} = \{ x\} \) (see proposition 9 on page 20). However, \( {B}_{0} \subset V \) , so \( x \in V \) . According to (II), we also have \( {B}_{n} \subset {O}_{n} \) for all \( n \) , so \( x \in {O}_{n} \) for all \( n \) . Thus, \( x \in { \cap }_{n \in \mathbb{N}}{O}_{n} \) . Finally, we have proven that \( V \) and \( { \cap }_{n \in \mathbb{N}}{O}_{n} \) have at least one point in common, hence the theorem.

3/ Soit \( G \) le fermé \( E \smallsetminus \left( {{ \cup }_{n}{F}_{n}}\right) \) . Il s’agit de montrer que \( G \) est d’intérieur vide.

> 3/ Let \( G \) be the closed set \( E \smallsetminus \left( {{ \cup }_{n}{F}_{n}}\right) \) . It is a matter of showing that \( G \) has an empty interior.

Pour tout \( n \in \mathbb{N} \) , le fermé \( G \cap {F}_{n} \) est d’intérieur vide car \( \overset{\text{ ⏜ }}{G \cap {F}_{n}} \subset G \cap {F}_{n} = \varnothing \) , donc \( \left( {E,\mathrm{\;d}}\right) \) étant un espace de Baire,

> For all \( n \in \mathbb{N} \) , the closed set \( G \cap {F}_{n} \) has an empty interior because \( \overset{\text{ ⏜ }}{G \cap {F}_{n}} \subset G \cap {F}_{n} = \varnothing \) , so \( \left( {E,\mathrm{\;d}}\right) \) being a Baire space,

\[
\mathop{\bigcup }\limits_{{n \in  \mathbb{N}}}\left( {G \cap  {F}_{n}}\right)  = G \cap  \left\lbrack  {\mathop{\bigcup }\limits_{{n \in  \mathbb{N}}}{F}_{n}}\right\rbrack   = G \cap  E = G
\]

est d'intérieur vide.

> has an empty interior.

Remarque. On peut également définir un espace de Baire pour un espace topologique général, avec les mêmes définitions. On peut montrer qu'un espace topologique compact est un espace de Baire.

> Remark. One can also define a Baire space for a general topological space, with the same definitions. One can show that a compact topological space is a Baire space.

##### Applications

Les exercices qui suivent sont indépendants les uns des autres, mais il est nécessaire d'avoir fait l'exercice 0 pour les traiter.

> The following exercises are independent of one another, but it is necessary to have completed exercise 0 to address them.

EXERCICE 1 (UN E.V.N Å BASE DÉNOMBRABLE N'EST PAS COMPLET). Prouver, en utilisant le théorème de Baire, qu’un espace vectoriel normé \( E \) admettant une base dénombrable n’est pas complet.

> EXERCISE 1 (A NORMED VECTOR SPACE WITH A COUNTABLE BASIS IS NOT COMPLETE). Prove, using the Baire category theorem, that a normed vector space \( E \) admitting a countable basis is not complete.

Solution. Soit \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) une base de \( E \) . Pour tout entier naturel \( n \) , on pose \( {F}_{n} = \operatorname{Vect}\left( {{e}_{0},\ldots ,{e}_{n}}\right) \) . Le s.e.v \( {F}_{n} \) est un fermé (car s.e.v de dimension finie), d’intérieur vide car si une boule ouverte \( \mathrm{B}\left( {x, r}\right) \) est incluse dans \( {F}_{n} \) (avec \( r > 0 \) ), alors \( x \in {F}_{n} \) donc \( \mathrm{B}\left( {0, r}\right) = \mathrm{B}\left( {x, r}\right) - \{ x\} \) est inclus dans \( {F}_{n} \) , et \( {F}_{n} \) étant invariant par homothétie, \( E \subset {F}_{n} \) ce qui est absurde.

> Solution. Let \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) be a basis of \( E \) . For every natural number \( n \) , let \( {F}_{n} = \operatorname{Vect}\left( {{e}_{0},\ldots ,{e}_{n}}\right) \) . The subspace \( {F}_{n} \) is closed (as a finite-dimensional subspace) and has an empty interior, because if an open ball \( \mathrm{B}\left( {x, r}\right) \) were included in \( {F}_{n} \) (with \( r > 0 \) ), then \( x \in {F}_{n} \) , so \( \mathrm{B}\left( {0, r}\right) = \mathrm{B}\left( {x, r}\right) - \{ x\} \) would be included in \( {F}_{n} \) , and since \( {F}_{n} \) is invariant under homothety, \( E \subset {F}_{n} \) , which is absurd.

Supposons maintenant \( E \) complet. D’après le théorème de Baire, \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) est d’intérieur vide dans \( E \) , ce qui est absurde car \( { \cup }_{n \in \mathbb{N}}{F}_{n} = E \) . D’où le résultat.

> Now suppose \( E \) is complete. According to the Baire category theorem, \( { \cup }_{n \in \mathbb{N}}{F}_{n} \) has an empty interior in \( E \) , which is absurd because \( { \cup }_{n \in \mathbb{N}}{F}_{n} = E \) . Hence the result.

Remarque. Ce même résultat est prouvé sans utiliser le théorème de Baire à l'exercice 8 de la page 56.

> Remark. This same result is proven without using the Baire category theorem in exercise 8 on page 56.

EXERCICE 2 (UNE FONCTION DÉRIVÉE EST CONTINUE SUR UN ENSEMBLE DENSE).

> EXERCISE 2 (A DERIVATIVE FUNCTION IS CONTINUOUS ON A DENSE SET).

1/ Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques. On suppose que \( \left( {E,\mathrm{\;d}}\right) \) est complet. On considère une suite \( \left( {f}_{n}\right) \) d’applications continues de \( E \) dans \( F \) , convergeant simplement vers une application \( f \) de \( E \) dans \( F \) .

> 1/ Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces. Assume \( \left( {E,\mathrm{\;d}}\right) \) is complete. Consider a sequence \( \left( {f}_{n}\right) \) of continuous mappings from \( E \) to \( F \) , converging pointwise to a mapping \( f \) from \( E \) to \( F \) .

a) Pour tout \( \varepsilon > 0 \) , pour tout \( n \in \mathbb{N} \) , on pose

> a) For every \( \varepsilon > 0 \) , for every \( n \in \mathbb{N} \) , let

\[
{F}_{n,\varepsilon } = \left\{  {x \in  E\mid \forall p \geq  n,\delta \left( {{f}_{n}\left( x\right) ,{f}_{p}\left( x\right) }\right)  \leq  \varepsilon }\right\}  .
\]

Montrer que \( {\Omega }_{\varepsilon } = { \cup }_{n \in \mathbb{N}}{F}_{n,\varepsilon } \) est un ouvert dense dans \( E \) et que

> Show that \( {\Omega }_{\varepsilon } = { \cup }_{n \in \mathbb{N}}{F}_{n,\varepsilon } \) is an open dense set in \( E \) and that

\[
\forall {x}_{0} \in  {\Omega }_{\varepsilon },\exists V\text{ voisinage de }{x}_{0},\forall x \in  V,\;\delta \left( {f\left( {x}_{0}\right) , f\left( x\right) }\right)  \leq  {3\varepsilon }.
\]

b) En déduire que l’ensemble des points de continuité de \( f \) est un résiduel.

> b) Deduce that the set of points of continuity of \( f \) is a residual set.

2/ (Application.) Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application dérivable sur \( \mathbb{R} \) . Que dire de l’ensemble des points de continuité de la fonction dérivée \( {f}^{\prime } \) ?

> 2/ (Application.) Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a differentiable mapping on \( \mathbb{R} \) . What can be said about the set of points of continuity of the derivative function \( {f}^{\prime } \) ?

Solution. 1/ a) Fixons \( \varepsilon > 0 \) et \( n \in \mathbb{N} \) . Pour \( p \geq n \) , l’ensemble \( {G}_{p} = \left\{ {x \in E \mid \delta \left( {{f}_{n}\left( x\right) ,{f}_{p}\left( x\right) }\right) \leq }\right. \; \varepsilon \} \) est fermé (car \( {f}_{n} \) et \( {f}_{p} \) sont continues) donc \( {F}_{n,\varepsilon } = { \cap }_{p \geq n}{G}_{p} \) est fermé.

> Solution. 1/ a) Let us fix \( \varepsilon > 0 \) and \( n \in \mathbb{N} \) . For \( p \geq n \) , the set \( {G}_{p} = \left\{ {x \in E \mid \delta \left( {{f}_{n}\left( x\right) ,{f}_{p}\left( x\right) }\right) \leq }\right. \; \varepsilon \} \) is closed (because \( {f}_{n} \) and \( {f}_{p} \) are continuous), therefore \( {F}_{n,\varepsilon } = { \cap }_{p \geq n}{G}_{p} \) is closed.

Par hypothèse, la suite \( \left( {f}_{n}\right) \) converge simplement, donc \( { \cup }_{n \in \mathbb{N}}{F}_{n,\varepsilon } = E \) , ce qui entraîne (voir la partie 3/ de l'exercice 0 ) que

> By hypothesis, the sequence \( \left( {f}_{n}\right) \) converges pointwise, so \( { \cup }_{n \in \mathbb{N}}{F}_{n,\varepsilon } = E \) , which implies (see part 3/ of exercise 0 ) that

\[
{\Omega }_{\varepsilon } = { \cup  }_{n \in  \mathbb{N}}{\overset{ \circ  }{F}}_{n,\varepsilon }
\]

est un ouvert dense dans l’espace complet \( E \) .

> is a dense open set in the complete space \( E \) .

Ceci étant, soit \( {x}_{0} \in {\Omega }_{\varepsilon } \) et soit \( n \in \mathbb{N} \) tel que \( {x}_{0} \in {F}_{n,\varepsilon } \) . Comme \( {f}_{n} \) est continue, il existe un voisinage \( V \) de \( {x}_{0} \) inclus dans \( {\overset{ \circ }{F}}_{n,\varepsilon } \) tel que

> Given this, let \( {x}_{0} \in {\Omega }_{\varepsilon } \) and let \( n \in \mathbb{N} \) be such that \( {x}_{0} \in {F}_{n,\varepsilon } \) . Since \( {f}_{n} \) is continuous, there exists a neighborhood \( V \) of \( {x}_{0} \) included in \( {\overset{ \circ }{F}}_{n,\varepsilon } \) such that

\[
\forall x \in  V,\;\delta \left( {{f}_{n}\left( {x}_{0}\right) ,{f}_{n}\left( x\right) }\right)  \leq  \varepsilon .
\]

Or \( V \) est inclus dans \( {F}_{n,\varepsilon } \) donc

> However, \( V \) is included in \( {F}_{n,\varepsilon } \) so

\[
\forall x \in  V,\forall p \geq  n,\;\delta \left( {{f}_{n}\left( x\right) ,{f}_{p}\left( x\right) }\right)  \leq  \varepsilon ,
\]

donc en faisant tendre \( n \) vers l’infini (pour \( x \) et \( n \) fixés) on obtient \( \delta \left( {{f}_{n}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \) pour tout \( x \in V \) . Finalement,

> therefore, by letting \( n \) tend to infinity (for fixed \( x \) and \( n \) ) we obtain \( \delta \left( {{f}_{n}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \) for all \( x \in V \) . Finally,

\[
\forall x \in  V,\;\delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  \leq  \delta \left( {f\left( x\right) ,{f}_{n}\left( x\right) }\right)  + \delta \left( {{f}_{n}\left( x\right) , f\left( x\right) }\right)  + \delta \left( {{f}_{n}\left( {x}_{0}\right) , f\left( {x}_{0}\right) }\right)  \leq  \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon }.
\]

b) Posons \( R = { \cap }_{n \in {\mathbb{N}}^{ * }}{\Omega }_{1/n} \) et montrons que \( f \) est continue en tout point de \( R \) . Soit \( {x}_{0} \in R \) et \( \varepsilon > 0 \) . Fixons \( n \in {\mathbb{N}}^{ * } \) tel que \( 1/n \leq \varepsilon /3 \) . Comme \( {x}_{0} \in {\Omega }_{1/n} \) , d’après le résultat de la question précédente, il existe un voisinage \( V \) de \( {x}_{0} \) tel que

> b) Let \( R = { \cap }_{n \in {\mathbb{N}}^{ * }}{\Omega }_{1/n} \) and let us show that \( f \) is continuous at every point of \( R \) . Let \( {x}_{0} \in R \) and \( \varepsilon > 0 \) . Fix \( n \in {\mathbb{N}}^{ * } \) such that \( 1/n \leq \varepsilon /3 \) . Since \( {x}_{0} \in {\Omega }_{1/n} \) , according to the result of the previous question, there exists a neighborhood \( V \) of \( {x}_{0} \) such that

\[
\forall x \in  V,\;\delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  \leq  \frac{3}{n} \leq  \varepsilon .
\]

Ceci suffit à prouver que \( f \) est continue en \( {x}_{0} \) .

> This suffices to prove that \( f \) is continuous at \( {x}_{0} \) .

L’ensemble des points de continuité de \( f \) contient donc \( R \) . C’est donc un résiduel, en parti-culier dense dans \( E \) d’après le théorème de Baire.

> The set of points of continuity of \( f \) therefore contains \( R \) . It is thus a residual set, in particular dense in \( E \) according to the Baire category theorem.

2/ Pour tout \( n \in {\mathbb{N}}^{ * } \) , on considère la fonction

> 2/ For all \( n \in {\mathbb{N}}^{ * } \) , we consider the function

\[
{f}_{n} : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \frac{f\left( {x + \frac{1}{n}}\right)  - f\left( x\right) }{\frac{1}{n}}.
\]

La suite \( \left( {f}_{n}\right) \) est une suite de fonctions continues qui converge simplement vers \( {f}^{\prime } \) sur \( \mathbb{R} \) . On en déduit d’après 1/b) que l’ensemble des points de continuité de \( {f}^{\prime } \) est un résiduel, en particulier dense dans \( \mathbb{R} \) puisque \( \mathbb{R} \) est complet.

> The sequence \( \left( {f}_{n}\right) \) is a sequence of continuous functions that converges pointwise to \( {f}^{\prime } \) on \( \mathbb{R} \) . We deduce from 1/b) that the set of points of continuity of \( {f}^{\prime } \) is a residual set, in particular dense in \( \mathbb{R} \) since \( \mathbb{R} \) is complete.

Remarque. On sait qu'il existe des fonctions dérivées discontinues sur un ensemble dense (voir l'exercice 9 page 244).

> Remark. We know that there exist derivative functions that are discontinuous on a dense set (see exercise 9 page 244).

EXERCICE 3. a) On considère une application \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) continue et on suppose que pour tout \( x > 0 \) , la suite \( {\left( f\left( nx\right) \right) }_{n \in \mathbb{N}} \) converge vers 0 . En utilisant le théorème de Baire, montrer que \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) = 0 \) .

> EXERCISE 3. a) Consider a continuous mapping \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) and assume that for all \( x > 0 \) , the sequence \( {\left( f\left( nx\right) \right) }_{n \in \mathbb{N}} \) converges to 0 . Using the Baire category theorem, show that \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) = 0 \) .

b) Soit \( \Omega \subset \rbrack 0, + \infty \lbrack \) un ouvert non borné. Montrer

> b) Let \( \Omega \subset \rbrack 0, + \infty \lbrack \) be an unbounded open set. Show

\[
\exists {x}_{0} > 0,\forall N \in  \mathbb{N},\exists n \geq  N,\;n{x}_{0} \in  \Omega .
\]

Retrouver grâce à ce dernier résultat le résultat du a).

> Recover the result of a) using this last result.

Solution. a) Soit \( \varepsilon > 0 \) . On introduit, pour tout \( n \in {\mathbb{N}}^{ * } \) , l’ensemble

> Solution. a) Let \( \varepsilon > 0 \) . We introduce, for all \( n \in {\mathbb{N}}^{ * } \) , the set

\[
{F}_{n} = \{ x \geq  0 \mid  \forall p \in  \mathbb{N}, p \geq  n,\left| {f\left( {px}\right) }\right|  \leq  \varepsilon \} .
\]

Comme \( f \) est continue, \( {F}_{n} \) est un fermé de \( {\mathbb{R}}^{ + } \) , donc de \( \mathbb{R} \) . L’hypothèse vérifiée par \( f \) entraîne \( \rbrack 0, + \infty \left\lbrack { \subset { \cup }_{n \in {\mathbb{N}}^{ * }}{F}_{n}}\right. \) , donc d’après le théorème de Baire, il existe \( {n}_{0} \in {\mathbb{N}}^{ * } \) tel que \( {F}_{{n}_{0}} \neq \varnothing \) . Soient \( \alpha ,\beta > 0 \) tels que \( \rbrack \alpha ,\beta \left\lbrack { \subset {F}_{{n}_{0}}}\right. \) , de sorte que

> Since \( f \) is continuous, \( {F}_{n} \) is a closed subset of \( {\mathbb{R}}^{ + } \), and thus of \( \mathbb{R} \). The hypothesis satisfied by \( f \) implies \( \rbrack 0, + \infty \left\lbrack { \subset { \cup }_{n \in {\mathbb{N}}^{ * }}{F}_{n}}\right. \), so by the Baire category theorem, there exists \( {n}_{0} \in {\mathbb{N}}^{ * } \) such that \( {F}_{{n}_{0}} \neq \varnothing \). Let \( \alpha ,\beta > 0 \) be such that \( \rbrack \alpha ,\beta \left\lbrack { \subset {F}_{{n}_{0}}}\right. \), so that

\[
\forall x \in  \rbrack \alpha ,\beta \lbrack ,\forall p \geq  {n}_{0},\;\left| {f\left( {px}\right) }\right|  \leq  \varepsilon .
\]

(*)

> L’équivalence \( \left( {\left( {p + 1}\right) \alpha < {p\beta }}\right) \Leftrightarrow \left( {p > \frac{\alpha }{\beta - \alpha }}\right) \) montre que

The equivalence \( \left( {\left( {p + 1}\right) \alpha < {p\beta }}\right) \Leftrightarrow \left( {p > \frac{\alpha }{\beta - \alpha }}\right) \) shows that

\[
\forall N \in  \mathbb{N}, N > \frac{\alpha }{\beta  - \alpha },\;\mathop{\bigcup }\limits_{{p \geq  N}}\rbrack {p\alpha },{p\beta }\left\lbrack   = \right\rbrack  {N\alpha }, + \infty \lbrack .
\]

Ceci est en particulier vrai pour un entier \( N \) fixé supérieur à \( {n}_{0} \) et à \( \alpha /\left( {\beta - \alpha }\right) \) . Donc d’après (*), on a \( \left| {f\left( x\right) }\right| \leq \varepsilon \) pour tout \( x \geq {N\alpha } \) , d’où le résultat.

> This is in particular true for a fixed integer \( N \) greater than \( {n}_{0} \) and \( \alpha /\left( {\beta - \alpha }\right) \). Thus, according to (*), we have \( \left| {f\left( x\right) }\right| \leq \varepsilon \) for all \( x \geq {N\alpha } \), hence the result.

b) Fixons \( n \in {\mathbb{N}}^{ * } \) et posons \( {\Omega }_{n} = \{ x > 0 \mid \exists p \geq n,{px} \in \Omega \} \) . L’ensemble \( {\Omega }_{n} \) est ouvert. Il est même dense dans \( {\mathbb{R}}^{ + } \) . En effet, considérons un intervalle ouvert \( \rbrack \alpha ,\beta \left\lbrack \right. \) inclus dans \( {\mathbb{R}}^{ + } \) . En procédant comme dans la question précédente, on montre que

> b) Let us fix \( n \in {\mathbb{N}}^{ * } \) and set \( {\Omega }_{n} = \{ x > 0 \mid \exists p \geq n,{px} \in \Omega \} \). The set \( {\Omega }_{n} \) is open. It is even dense in \( {\mathbb{R}}^{ + } \). Indeed, consider an open interval \( \rbrack \alpha ,\beta \left\lbrack \right. \) included in \( {\mathbb{R}}^{ + } \). By proceeding as in the previous question, we show that

\[
\exists N \geq  n,\;\mathop{\bigcup }\limits_{{p \geq  N}}\rbrack {p\alpha },{p\beta }\left\lbrack   = \right\rbrack  {N\alpha }, + \infty \lbrack .
\]

Comme \( \Omega \) n’est pas borné, on en déduit \( \left( {{ \cup }_{p \geq N}\left\rbrack {{p\alpha },{p\beta }}\right\lbrack }\right) \cap \Omega \neq \varnothing \) , donc \( \rbrack \alpha ,\beta \lbrack \cap {\Omega }_{n} \neq \varnothing \) .

> Since \( \Omega \) is not bounded, we deduce \( \left( {{ \cup }_{p \geq N}\left\rbrack {{p\alpha },{p\beta }}\right\lbrack }\right) \cap \Omega \neq \varnothing \), and therefore \( \rbrack \alpha ,\beta \lbrack \cap {\Omega }_{n} \neq \varnothing \).

Ainsi \( {\Omega }_{n} \) est un ouvert dense dans \( {\mathbb{R}}^{ + } \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Comme \( {\mathbb{R}}^{ + } \) est complet, on en déduit d’après le théorème de Baire que \( { \cap }_{n \in {\mathbb{N}}^{ * }}{\Omega }_{n} \) est dense dans \( {\mathbb{R}}^{ + } \) . Ce dernier contient donc au moins un élément \( {x}_{0} > 0 \) , et il est clair qu’un tel réel \( {x}_{0} \) répond à la question.

> Thus \( {\Omega }_{n} \) is an open dense set in \( {\mathbb{R}}^{ + } \) for all \( n \in {\mathbb{N}}^{ * } \). Since \( {\mathbb{R}}^{ + } \) is complete, we deduce from the Baire category theorem that \( { \cap }_{n \in {\mathbb{N}}^{ * }}{\Omega }_{n} \) is dense in \( {\mathbb{R}}^{ + } \). The latter therefore contains at least one element \( {x}_{0} > 0 \), and it is clear that such a real number \( {x}_{0} \) answers the question.

Résolvons maintenant la question a) à partir de ce dernier résultat. Raisonnons par l'absurde. Si a) est faux,

> Let us now solve question a) based on this last result. Let us reason by contradiction. If a) is false,

\[
\exists \varepsilon  > 0,\forall A > 0,\exists x > A,\;\left| {f\left( x\right) }\right|  > \varepsilon .
\]

Autrement dit, l’ouvert \( \Omega = \{ x > 0,\left| {f\left( x\right) }\right| > \varepsilon \} \) est non borné. Donc

> In other words, the open set \( \Omega = \{ x > 0,\left| {f\left( x\right) }\right| > \varepsilon \} \) is unbounded. Therefore

\[
\exists {x}_{0} > 0,\forall N \in  \mathbb{N},\exists n \geq  N,\;n{x}_{0} \in  \Omega ,
\]

ce qui s’exprime en disant que la suite \( {\left( f\left( n{x}_{0}\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) ne tend pas vers 0 . Ceci est absurde, d’où le résultat.

> which is expressed by saying that the sequence \( {\left( f\left( n{x}_{0}\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) does not tend to 0. This is absurd, hence the result.

EXERCICE 4 (LES FONCTIONS CONTINUES NULLE PART DÉRIVABLES SONT DENSES).

> EXERCISE 4 (NOWHERE DIFFERENTIABLE CONTINUOUS FUNCTIONS ARE DENSE).

On note \( \mathcal{C} \) le \( \mathbb{R} \) -e.v des fonctions continues de \( I = \left\lbrack {0,1}\right\rbrack \) dans \( \mathbb{R} \) , muni de la norme de la convergence uniforme \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in I}}\left| {f\left( t\right) }\right| \) . L’e.v \( \mathcal{C} \) est un espace de Banach (car fermé de \( \mathcal{B}\left( {I,\mathbb{R}}\right) \) , ensemble des fonctions bornées de \( I \) dans \( \mathbb{R} \) , complet d’après l’exercice 1 page 21).

> Let \( \mathcal{C} \) be the \( \mathbb{R} \) -v.s. of continuous functions from \( I = \left\lbrack {0,1}\right\rbrack \) to \( \mathbb{R} \) , equipped with the uniform convergence norm \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in I}}\left| {f\left( t\right) }\right| \) . The v.s. \( \mathcal{C} \) is a Banach space (as it is a closed subset of \( \mathcal{B}\left( {I,\mathbb{R}}\right) \) , the set of bounded functions from \( I \) to \( \mathbb{R} \) , which is complete according to exercise 1 on page 21).

Pour \( \varepsilon > 0 \) et \( n \in \mathbb{N} \) , on considère l’ensemble

> For \( \varepsilon > 0 \) and \( n \in \mathbb{N} \) , we consider the set

\[
{U}_{\varepsilon , n} = \left\{  {f \in  \mathcal{C}\mid \forall x \in  I,\exists y \in  I,0 < \left| {y - x}\right|  < \varepsilon ,\;\left| \frac{f\left( y\right)  - f\left( x\right) }{y - x}\right|  > n}\right\}  .
\]

a) Montrer que \( {U}_{\varepsilon , n} \) est un ouvert de \( \mathcal{C} \) .

> a) Show that \( {U}_{\varepsilon , n} \) is an open subset of \( \mathcal{C} \) .

b) Montrer que \( {U}_{\varepsilon , n} \) est dense dans \( \mathcal{C} \) (indication : pour \( f \in \mathcal{C} \) , pour \( \delta > 0 \) , on considérera la fonction \( x \mapsto f\left( x\right) + \delta \sin \left( {Nx}\right) \) avec \( N \) bien choisi).

> b) Show that \( {U}_{\varepsilon , n} \) is dense in \( \mathcal{C} \) (hint: for \( f \in \mathcal{C} \) , for \( \delta > 0 \) , consider the function \( x \mapsto f\left( x\right) + \delta \sin \left( {Nx}\right) \) with a well-chosen \( N \) ).

c) En déduire que l’ensemble des fonctions de \( \mathcal{C} \) nulle part dérivables est un résiduel dans \( \mathcal{C} \) .

> c) Deduce that the set of functions in \( \mathcal{C} \) that are nowhere differentiable is a residual set in \( \mathcal{C} \) .

Solution. a) Nous allons montrer que le complémentaire \( {F}_{\varepsilon , n} \) de \( {U}_{\varepsilon , n} \) dans \( \mathcal{C} \) est fermé. Pour cela, on commence par remarquer que

> Solution. a) We will show that the complement \( {F}_{\varepsilon , n} \) of \( {U}_{\varepsilon , n} \) in \( \mathcal{C} \) is closed. To do this, we first note that

\[
{F}_{\varepsilon , n} = \left\{  {f \in  \mathcal{C}\mid \exists x \in  I,\forall y \in  I,\left| {y - x}\right|  < \varepsilon \;\left| {f\left( y\right)  - f\left( x\right) }\right|  \leq  n\left| {y - x}\right| }\right\}  .
\]

On considère ensuite une suite \( {\left( {f}_{p}\right) }_{p \in \mathbb{N}} \) de \( {F}_{\varepsilon , n} \) qui converge vers \( f \in \mathcal{C} \) . Il s’agit de montrer que \( f \in {F}_{\varepsilon , n} \) .

> Next, we consider a sequence \( {\left( {f}_{p}\right) }_{p \in \mathbb{N}} \) in \( {F}_{\varepsilon , n} \) that converges to \( f \in \mathcal{C} \) . We must show that \( f \in {F}_{\varepsilon , n} \) .

Pour tout \( p \in \mathbb{N} \) , on a \( {f}_{p} \in {F}_{\varepsilon , n} \) donc

> For all \( p \in \mathbb{N} \) , we have \( {f}_{p} \in {F}_{\varepsilon , n} \) therefore

\[
\exists {x}_{p} \in  I,\forall y \in  I,\left| {y - {x}_{p}}\right|  < \varepsilon ,\;\left| {{f}_{p}\left( y\right)  - {f}_{p}\left( {x}_{p}\right) }\right|  \leq  n\left| {y - {x}_{p}}\right| .
\]

La suite \( \left( {x}_{p}\right) \) prend ses valeurs dans le compact \( I \) , on peut donc en extraire une sous-suite convergente \( \left( {x}_{\varphi \left( p\right) }\right) \) , dont nous notons \( x \) la limite. Soit \( y \in I \) tel que \( 0 < \left| {y - x}\right| < \varepsilon \) . Il existe \( P \in \mathbb{N} \) tel que \( 0 < \left| {y - {x}_{\varphi \left( p\right) }}\right| < \varepsilon \) pour tout \( p \geq P \) . Ainsi,

> The sequence \( \left( {x}_{p}\right) \) takes its values in the compact set \( I \) , so we can extract a convergent subsequence \( \left( {x}_{\varphi \left( p\right) }\right) \) , whose limit we denote by \( x \) . Let \( y \in I \) be such that \( 0 < \left| {y - x}\right| < \varepsilon \) . There exists \( P \in \mathbb{N} \) such that \( 0 < \left| {y - {x}_{\varphi \left( p\right) }}\right| < \varepsilon \) for all \( p \geq P \) . Thus,

\[
\forall p \geq  P,\;\left| {{f}_{\varphi \left( p\right) }\left( y\right)  - {f}_{\varphi \left( p\right) }\left( {x}_{\varphi \left( p\right) }\right) }\right|  \leq  n\left| {y - {x}_{\varphi \left( p\right) }}\right| .
\]

\( \left( *\right) \)

> Le caractère continu de \( f \) conjugué au fait que \( \left( {f}_{p}\right) \) tende vers \( f \) au sens de \( \parallel .{\parallel }_{\infty } \) montre que \( \left( {{f}_{\varphi \left( p\right) }\left( {x}_{\varphi \left( p\right) }\right) }\right) \) tend vers \( f\left( x\right) \) . En faisant tendre \( p \) vers l’infini dans (*), on en déduit que \( \left| {f\left( y\right) - f\left( x\right) }\right| \leq n\left| {y - x}\right| \) . Ceci étant vrai pour tout \( y \in I \) tel que \( \left| {y - x}\right| < \varepsilon \) , on en déduit que \( f \in {F}_{\varepsilon , n} \) et le résultat.

The continuous nature of \( f \) combined with the fact that \( \left( {f}_{p}\right) \) tends to \( f \) in the sense of \( \parallel .{\parallel }_{\infty } \) shows that \( \left( {{f}_{\varphi \left( p\right) }\left( {x}_{\varphi \left( p\right) }\right) }\right) \) tends to \( f\left( x\right) \) . By letting \( p \) tend to infinity in (*), we deduce that \( \left| {f\left( y\right) - f\left( x\right) }\right| \leq n\left| {y - x}\right| \) . Since this is true for any \( y \in I \) such that \( \left| {y - x}\right| < \varepsilon \) , we deduce \( f \in {F}_{\varepsilon , n} \) and the result.

> b) Soit \( f \in \mathcal{C} \) et \( \delta > 0 \) . Il s’agit de trouver \( g \in {U}_{\varepsilon , n} \) tel que \( \parallel f - g{\parallel }_{\infty } \leq \delta \) . On va chercher \( g \) sous la forme \( f\left( x\right) + \delta \sin \left( {Nx}\right) \) .

b) Let \( f \in \mathcal{C} \) and \( \delta > 0 \) . We must find \( g \in {U}_{\varepsilon , n} \) such that \( \parallel f - g{\parallel }_{\infty } \leq \delta \) . We will look for \( g \) in the form \( f\left( x\right) + \delta \sin \left( {Nx}\right) \) .

> L’uniforme continuité de \( f \) sur le compact \( I \) est assurée par le théorème de Heine, de sorte que

The uniform continuity of \( f \) on the compact set \( I \) is guaranteed by the Heine-Cantor theorem, so that

\[
\exists \alpha  \in  \rbrack 0,\varepsilon \lbrack ,\forall \left( {x, y}\right)  \in  {I}^{2},\left| {x - y}\right|  < \alpha ,\;\left| {f\left( x\right)  - f\left( y\right) }\right|  < \frac{\delta }{4}.
\]

On choisit maintenant \( N > {2\pi } \) tel que \( \frac{4\pi }{N} < \alpha \) et \( \frac{\delta N}{8\pi } > n \) . Posons \( g\left( x\right) = f\left( x\right) + \delta \sin \left( {Nx}\right) \) . Soit \( x \in I \) . Il est clair que

> We now choose \( N > {2\pi } \) such that \( \frac{4\pi }{N} < \alpha \) and \( \frac{\delta N}{8\pi } > n \) . Let \( g\left( x\right) = f\left( x\right) + \delta \sin \left( {Nx}\right) \) . Let \( x \in I \) . It is clear that

\[
\exists y \in  I,\;{2\pi } \leq  \left| {{Nx} - {Ny}}\right|  \leq  {4\pi }\;\text{ et }\left| {\sin \left( {Nx}\right)  - \sin \left( {Ny}\right) }\right|  \geq  1.
\]

On a en particulier

> In particular, we have

\[
\frac{2\pi }{N} \leq  \left| {x - y}\right|  \leq  \frac{4\pi }{N}\;\text{ donc }\;\left| {x - y}\right|  < \alpha \;\text{ donc }\;\left| \frac{f\left( y\right)  - f\left( x\right) }{y - x}\right|  < \frac{\delta }{4} \cdot  \frac{N}{2\pi } = \frac{\delta N}{8\pi }.
\]

De plus,

> Furthermore,

\[
\left| \frac{\delta \sin \left( {Ny}\right)  - \delta \sin \left( {Nx}\right) }{y - x}\right|  \geq  \frac{\delta }{\left| y - x\right| } \geq  \frac{\delta N}{4\pi },
\]

donc

> therefore

\[
\left| \frac{g\left( y\right)  - g\left( x\right) }{y - x}\right|  > \frac{\delta N}{4\pi } - \frac{\delta N}{8\pi } = \frac{\delta N}{8\pi } > n,\;\text{ avec }\;0 < \left| {y - x}\right|  < \alpha  < \varepsilon .
\]

Donc \( g \in {U}_{\varepsilon , n} \) , et comme \( \parallel f - g{\parallel }_{\infty } = \delta \) , on en déduit le résultat.

> Thus \( g \in {U}_{\varepsilon , n} \) , and since \( \parallel f - g{\parallel }_{\infty } = \delta \) , we deduce the result.

c) Posons \( R = { \cap }_{n \in {\mathbb{N}}^{ * }}{U}_{1/n, n} \) . Soit \( f \in R \) . Pour tout \( n, f \in {U}_{1/n, n} \) donc si on se donne \( x \in I \) ,

> c) Let \( R = { \cap }_{n \in {\mathbb{N}}^{ * }}{U}_{1/n, n} \) . Let \( f \in R \) . For all \( n, f \in {U}_{1/n, n} \) , so if we are given \( x \in I \) ,

\[
\forall n \in  {\mathbb{N}}^{ * },\exists {x}_{n} \in  I,0 < \left| {x - {x}_{n}}\right|  < \frac{1}{n}\;\text{ et }\;\left| \frac{f\left( x\right)  - f\left( {x}_{n}\right) }{x - {x}_{n}}\right|  > n.
\]

Donc \( \left( {x}_{n}\right) \) tend vers \( x \) et \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| \frac{f\left( x\right) - f\left( {x}_{n}\right) }{x - {x}_{n}}\right| = + \infty \) , ce qui montre que \( f \) n’est pas dérivable en \( x \) . Ceci étant vrai pour tout \( x \in I, f \) est nulle part dérivable.

> Thus \( \left( {x}_{n}\right) \) tends to \( x \) and \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| \frac{f\left( x\right) - f\left( {x}_{n}\right) }{x - {x}_{n}}\right| = + \infty \) , which shows that \( f \) is not differentiable at \( x \) . Since this is true for any \( x \in I, f \) , it is nowhere differentiable.

Ainsi, tout élément de \( R \) est nulle part dérivable. Comme \( R \) est une intersection dénombrable d’ouverts denses dans le complet \( \mathcal{C} \) , l’ensemble des éléments de \( \mathcal{C} \) nulle part dérivables est un résiduel, en particulier dense dans \( \mathcal{C} \) d’après le théorème de Baire.

> Thus, every element of \( R \) is nowhere differentiable. As \( R \) is a countable intersection of dense open sets in the complete space \( \mathcal{C} \) , the set of nowhere differentiable elements of \( \mathcal{C} \) is a residual set, and in particular dense in \( \mathcal{C} \) according to the Baire category theorem.

Remarque. Une construction explicite d'une application continue nulle part dérivable fait l'objet de l'exercice 9 page 86.

> Remark. An explicit construction of a continuous nowhere differentiable function is the subject of exercise 9 on page 86.

EXERCICE 5. Soit \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{\infty } \) vérifiant

> EXERCISE 5. Let \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) be a mapping of class \( {\mathcal{C}}^{\infty } \) satisfying

\[
\forall x \in  \mathbb{R},\exists n \in  \mathbb{N},\;{\varphi }^{\left( n\right) }\left( x\right)  = 0.
\]

On veut montrer que \( \varphi \) est une fonction polynôme sur \( \mathbb{R} \) .

> We want to show that \( \varphi \) is a polynomial function on \( \mathbb{R} \) .

On pose \( {F}_{n} = \left\{ {x \in \mathbb{R} \mid {\varphi }^{\left( n\right) }\left( x\right) = 0}\right\} \) pour tout \( n \in \mathbb{N} \) puis \( \Omega = { \cup }_{n \in \mathbb{N}}{\overset{ \circ }{F}}_{n} \) et \( F = \mathbb{R} \smallsetminus \Omega \) .

> Let \( {F}_{n} = \left\{ {x \in \mathbb{R} \mid {\varphi }^{\left( n\right) }\left( x\right) = 0}\right\} \) for all \( n \in \mathbb{N} \) then \( \Omega = { \cup }_{n \in \mathbb{N}}{\overset{ \circ }{F}}_{n} \) and \( F = \mathbb{R} \smallsetminus \Omega \) .

a) Soit \( {\left( {x}_{p}\right) }_{p \in \mathbb{N}} \) une suite de points distincts de \( \mathbb{R} \) tendant vers \( x \in \mathbb{R} \) telle qu’il existe

> a) Let \( {\left( {x}_{p}\right) }_{p \in \mathbb{N}} \) be a sequence of distinct points of \( \mathbb{R} \) tending to \( x \in \mathbb{R} \) such that there exists

\( {n}_{0} \in \mathbb{N} \) vérifiant \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = 0 \) pour tout \( p \) . Montrer que \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) pour tout \( n \geq {n}_{0} \) .

> \( {n}_{0} \in \mathbb{N} \) satisfying \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = 0 \) for all \( p \) . Show that \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) for all \( n \geq {n}_{0} \) .

b) Montrer que sur toute composante connexe de \( \Omega ,\varphi \) est polynomiale.

> b) Show that on every connected component of \( \Omega ,\varphi \) is polynomial.

c) Montrer que \( F \) n’a aucun point isolé.

> c) Show that \( F \) has no isolated points.

d) En supposant \( F \neq \varnothing \) , obtenir une absurdité. Conclure.

> d) Assuming \( F \neq \varnothing \) , obtain an absurdity. Conclude.

Solution. a) Quitte à prendre une sous-suite de \( \left( {x}_{p}\right) \) , on peut supposer cette suite strictement monotone, par exemple strictement croissante. Pour tout \( p \) , on a \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p + 1}\right) \) donc d’après le théorème de Rolle, il existe \( {y}_{p} \in \rbrack {x}_{p},{x}_{p + 1}\left\lbrack \right. \) tel que \( {\varphi }^{\left( {n}_{0} + 1\right) }\left( {y}_{p}\right) \) . Ainsi construite, la suite \( \left( {y}_{p}\right) \) est une suite de points distincts tendant vers \( x \) et annulant \( {\varphi }^{\left( {n}_{0} + 1\right) } \) . En itérant le procédé, on peut ainsi construire pour tout \( n \geq {n}_{0} \) une suite de points distincts de \( \mathbb{R} \) tendant vers \( x \) et annulant \( {\varphi }^{\left( n\right) } \) . Par continuité de \( {\varphi }^{\left( n\right) } \) , on en déduit \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) pour tout \( n \geq {n}_{0} \) .

> Solution. a) By taking a subsequence of \( \left( {x}_{p}\right) \) if necessary, we can assume this sequence is strictly monotonic, for example strictly increasing. For all \( p \) , we have \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p + 1}\right) \) so by Rolle's theorem, there exists \( {y}_{p} \in \rbrack {x}_{p},{x}_{p + 1}\left\lbrack \right. \) such that \( {\varphi }^{\left( {n}_{0} + 1\right) }\left( {y}_{p}\right) \) . Constructed this way, the sequence \( \left( {y}_{p}\right) \) is a sequence of distinct points tending to \( x \) and vanishing at \( {\varphi }^{\left( {n}_{0} + 1\right) } \) . By iterating the process, we can thus construct for all \( n \geq {n}_{0} \) a sequence of distinct points of \( \mathbb{R} \) tending to \( x \) and vanishing at \( {\varphi }^{\left( n\right) } \) . By continuity of \( {\varphi }^{\left( n\right) } \) , we deduce \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) for all \( n \geq {n}_{0} \) .

b) Soit \( \rbrack a, b\left\lbrack {\text{ une composante connexe de l’ouvert }\Omega \text{ et soit }\left\lbrack {c, d}\right\rbrack \text{ un segment inclus dans }}\right\rbrack a, b\lbrack \) . Soit \( {x}_{0} \in \rbrack c, d\lbrack \) . Il existe \( n \in \mathbb{N} \) tel que \( {x}_{0} \in {F}_{n} \) donc il existe \( \alpha > 0 \) tel que \( {\varphi }^{\left( n\right) } \) s’annule sur \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \left\lbrack \right. \) . On peut donc trouver un polynôme \( P \) tel que \( \varphi = P \) sur \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \) . Ainsi, l'ensemble

> b) Let \( \rbrack a, b\left\lbrack {\text{ une composante connexe de l’ouvert }\Omega \text{ et soit }\left\lbrack {c, d}\right\rbrack \text{ un segment inclus dans }}\right\rbrack a, b\lbrack \) . Let \( {x}_{0} \in \rbrack c, d\lbrack \) . There exists \( n \in \mathbb{N} \) such that \( {x}_{0} \in {F}_{n} \) therefore there exists \( \alpha > 0 \) such that \( {\varphi }^{\left( n\right) } \) vanishes on \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \left\lbrack \right. \) . We can thus find a polynomial \( P \) such that \( \varphi = P \) on \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \) . Thus, the set

\[
\Gamma  = \left\{  {t \in  \rbrack {x}_{0}, d\rbrack \mid \forall x \in  \left\lbrack  {{x}_{0}, t}\right\rbrack  ,\varphi \left( x\right)  = P\left( x\right) }\right\}
\]

est non vide, donc \( \beta = \sup \Gamma \) existe bien.

> is non-empty, so \( \beta = \sup \Gamma \) does indeed exist.

Supposons \( \beta < d \) . Comme \( \beta \in \rbrack c, d\left\lbrack { \subset \Omega \text{ , il existe un voisinage }V = }\right\rbrack \beta - \eta ,\beta + \eta \lbrack \) de \( \beta \) et un polynôme \( Q \) tels que \( \varphi = Q \) sur \( V \) (même raisonnement que précédemment). Donc \( P = Q \) sur l’ouvert \( V \cap \rbrack {x}_{0},\beta \left\lbrack { \neq \varnothing \text{ , donc }P\text{ et }Q}\right. \) sont identiques, donc \( \beta + \eta \in \Gamma \) . Ceci est absurde, donc \( \beta = d \) , c’est-à-dire \( \varphi = P \) sur \( \left\lbrack {{x}_{0}, d}\right\rbrack \) . On montrerait de même que \( \varphi = P \) sur \( \left\lbrack {c,{x}_{0}}\right\rbrack \) . Ainsi, \( \varphi = P \) sur tout segment de la composante connexe \( \rbrack a, b\left\lbrack {\text{ , donc }\varphi = P\text{ sur }}\right\rbrack a, b\lbrack \) tout entier.

> Suppose \( \beta < d \) . As \( \beta \in \rbrack c, d\left\lbrack { \subset \Omega \text{ , il existe un voisinage }V = }\right\rbrack \beta - \eta ,\beta + \eta \lbrack \) of \( \beta \) and a polynomial \( Q \) such that \( \varphi = Q \) on \( V \) (same reasoning as before). Thus \( P = Q \) on the open set \( V \cap \rbrack {x}_{0},\beta \left\lbrack { \neq \varnothing \text{ , donc }P\text{ et }Q}\right. \) are identical, so \( \beta + \eta \in \Gamma \) . This is absurd, so \( \beta = d \) , that is to say \( \varphi = P \) on \( \left\lbrack {{x}_{0}, d}\right\rbrack \) . We would show in the same way that \( \varphi = P \) on \( \left\lbrack {c,{x}_{0}}\right\rbrack \) . Thus, \( \varphi = P \) on any segment of the connected component \( \rbrack a, b\left\lbrack {\text{ , donc }\varphi = P\text{ sur }}\right\rbrack a, b\lbrack \) entirely.

c) Raisonnons par l’absurde et supposons que \( F \) admette un point isolé \( {x}_{0} \) , de sorte qu’il existe \( \varepsilon > 0 \) tel que \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack {\cap F = \left\{ {x}_{0}\right\} }\right. \) . On a \( \rbrack {x}_{0} - \varepsilon ,{x}_{0}\left\lbrack { \subset \Omega }\right. \) et d’après la question b), il existe un polynôme \( P \) tel que \( \varphi = P \) sur \( \rbrack {x}_{0} - \varepsilon ,{x}_{0}\lbrack \) . De même, il existe un polynôme \( Q \) tel que \( \varphi = Q \) sur \( \rbrack {x}_{0},{x}_{0} + \varepsilon \lbrack \) . Par continuité des dérivées successives de \( \varphi \) et de \( P, Q \) , on a \( \forall n \in \mathbb{N} \) , \( {P}^{\left( n\right) }\left( {x}_{0}\right) = {\varphi }^{\left( n\right) }\left( {x}_{0}\right) = {Q}^{\left( n\right) }\left( {x}_{0}\right) \) . La formule de Taylor pour les polynômes en \( x = {x}_{0} \) montre alors que \( P \) et \( Q \) sont identiques, donc \( \varphi = P \) sur \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack \right. \) . Si \( n = \deg \left( P\right) \) , on a donc \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack { \subset {\overset{ \circ }{F}}_{n + 1} \subset \Omega }\right. \) . Ceci est absurde car \( {x}_{0} \notin \Omega \) , d’où le résultat.

> c) Let us reason by contradiction and assume that \( F \) admits an isolated point \( {x}_{0} \), such that there exists \( \varepsilon > 0 \) where \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack {\cap F = \left\{ {x}_{0}\right\} }\right. \). We have \( \rbrack {x}_{0} - \varepsilon ,{x}_{0}\left\lbrack { \subset \Omega }\right. \) and, according to question b), there exists a polynomial \( P \) such that \( \varphi = P \) on \( \rbrack {x}_{0} - \varepsilon ,{x}_{0}\lbrack \). Similarly, there exists a polynomial \( Q \) such that \( \varphi = Q \) on \( \rbrack {x}_{0},{x}_{0} + \varepsilon \lbrack \). By continuity of the successive derivatives of \( \varphi \) and \( P, Q \), we have \( \forall n \in \mathbb{N} \), \( {P}^{\left( n\right) }\left( {x}_{0}\right) = {\varphi }^{\left( n\right) }\left( {x}_{0}\right) = {Q}^{\left( n\right) }\left( {x}_{0}\right) \). Taylor's formula for polynomials at \( x = {x}_{0} \) then shows that \( P \) and \( Q \) are identical, so \( \varphi = P \) on \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack \right. \). If \( n = \deg \left( P\right) \), we then have \( \rbrack {x}_{0} - \varepsilon ,{x}_{0} + \varepsilon \left\lbrack { \subset {\overset{ \circ }{F}}_{n + 1} \subset \Omega }\right. \). This is absurd because \( {x}_{0} \notin \Omega \), hence the result.

d) Supposons le fermé \( F \) non vide. Par hypothèse, \( { \cup }_{n \in \mathbb{N}}{F}_{n} = \mathbb{R} \) , donc \( F = { \cup }_{n \in \mathbb{N}}\left( {F \cap {F}_{n}}\right) \) . Pour tout \( n, F \cap {F}_{n} \) est fermé dans \( F \) et \( F \) est complet (car fermé de \( \mathbb{R} \) ). D’après le théorème de Baire, il existe donc \( {n}_{0} \in \mathbb{N} \) tel que l’intérieur de \( F \cap {F}_{{n}_{0}} \) (pour la topologie induite par \( F \) ) soit non vide, c'est-à-dire

> d) Suppose the closed set \( F \) is non-empty. By hypothesis, \( { \cup }_{n \in \mathbb{N}}{F}_{n} = \mathbb{R} \), so \( F = { \cup }_{n \in \mathbb{N}}\left( {F \cap {F}_{n}}\right) \). For all \( n, F \cap {F}_{n} \) is closed in \( F \) and \( F \) is complete (as a closed subset of \( \mathbb{R} \)). According to the Baire category theorem, there therefore exists \( {n}_{0} \in \mathbb{N} \) such that the interior of \( F \cap {F}_{{n}_{0}} \) (for the topology induced by \( F \)) is non-empty, that is to say

\[
\exists {n}_{0} \in  \mathbb{N},\exists a, b \in  \mathbb{R},\;\rbrack a, b\left\lbrack  {\cap F \neq  \varnothing \;\text{ et }\;}\right\rbrack  a, b\lbrack  \cap  F \subset  {F}_{{n}_{0}}.
\]

(*)

> Soit \( x \in \rbrack a, b\left\lbrack \cap \right. F \) . D’après c), on peut trouver une suite de points distincts \( {\left( {x}_{p}\right) }_{p \in \mathbb{N}} \) de \( \rbrack a, b\lbrack \cap F \) tendant vers \( x \) . D’après (*), on a \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = 0 \) pour tout \( p \) , donc d’après a), \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) pour tout \( n \geq {n}_{0} \) .

Let \( x \in \rbrack a, b\left\lbrack \cap \right. F \). According to c), we can find a sequence of distinct points \( {\left( {x}_{p}\right) }_{p \in \mathbb{N}} \) of \( \rbrack a, b\lbrack \cap F \) tending towards \( x \). According to (*), we have \( {\varphi }^{\left( {n}_{0}\right) }\left( {x}_{p}\right) = 0 \) for all \( p \), so according to a), \( {\varphi }^{\left( n\right) }\left( x\right) = 0 \) for all \( n \geq {n}_{0} \).

> Si maintenant \( x \in \rbrack a, b\left\lbrack {\cap \Omega \text{ , alors comme }}\right\rbrack a, b\lbrack \cap F \neq \varnothing \) , la composante connexe \( {\Omega }_{x} \) de \( \Omega \) contenant \( x \) possède au moins une extrémité \( {x}_{0} \) dans \( \rbrack a, b\lbrack \) . D’après b), il existe un polynôme \( P \) tel que \( \varphi = P \) sur \( {\Omega }_{x} \) . Or \( {x}_{0} \in F \) donc pour tout \( n \geq {n}_{0},{\varphi }^{\left( n\right) }\left( {x}_{0}\right) = {P}^{\left( n\right) }\left( {x}_{0}\right) = 0 \) , ce qui montre que \( \deg \left( P\right) < {n}_{0} \) . Donc \( {\varphi }^{\left( {n}_{0}\right) }\left( x\right) = {P}^{\left( {n}_{0}\right) }\left( x\right) = 0 \) .

If now \( x \in \rbrack a, b\left\lbrack {\cap \Omega \text{ , alors comme }}\right\rbrack a, b\lbrack \cap F \neq \varnothing \), the connected component \( {\Omega }_{x} \) of \( \Omega \) containing \( x \) has at least one endpoint \( {x}_{0} \) in \( \rbrack a, b\lbrack \). According to b), there exists a polynomial \( P \) such that \( \varphi = P \) on \( {\Omega }_{x} \). However \( {x}_{0} \in F \) so for all \( n \geq {n}_{0},{\varphi }^{\left( n\right) }\left( {x}_{0}\right) = {P}^{\left( n\right) }\left( {x}_{0}\right) = 0 \), which shows that \( \deg \left( P\right) < {n}_{0} \). Thus \( {\varphi }^{\left( {n}_{0}\right) }\left( x\right) = {P}^{\left( {n}_{0}\right) }\left( x\right) = 0 \).

> En résumé, on a prouvé \( {\varphi }^{\left( {n}_{0}\right) }\left( x\right) = 0 \) pour tout \( x \in \rbrack a, b\left\lbrack \right. \) . Donc ] \( a, b\lbrack \subset {F}_{{n}_{0}} \) , ce qui est absurde car \( \rbrack a, b\left\lbrack {\cap F \neq \varnothing }\right. \) . Donc \( F = \varnothing \) , donc \( \Omega = \mathbb{R} \) , et d’après b), \( \varphi \) est polynomiale sur \( \mathbb{R} \) tout entier.

In summary, we have proven \( {\varphi }^{\left( {n}_{0}\right) }\left( x\right) = 0 \) for all \( x \in \rbrack a, b\left\lbrack \right. \). Thus ] \( a, b\lbrack \subset {F}_{{n}_{0}} \), which is absurd because \( \rbrack a, b\left\lbrack {\cap F \neq \varnothing }\right. \). Therefore \( F = \varnothing \), so \( \Omega = \mathbb{R} \), and according to b), \( \varphi \) is polynomial on the whole of \( \mathbb{R} \).

> EXERCICE 6 (THÉORÉME DE L'APPLICATION OUVERTE ; THÉORÉME DE BANACH). Soient \( E \) et \( F \) deux espaces de Banach.

EXERCISE 6 (OPEN MAPPING THEOREM; BANACH THEOREM). Let \( E \) and \( F \) be two Banach spaces.

> 1 / Théorème de l’application ouverte. Soit \( T : E \rightarrow F \) une application linéaire continue et surjective. Pour tout \( r > 0 \) , on note \( \mathrm{B}\left( r\right) = \{ x \in E \mid \parallel x\parallel < r\} \) .

1 / Open mapping theorem. Let \( T : E \rightarrow F \) be a continuous and surjective linear map. For all \( r > 0 \), we denote \( \mathrm{B}\left( r\right) = \{ x \in E \mid \parallel x\parallel < r\} \).

> a) En utilisant le théorème de Baire, montrer que pour tout \( r > 0,\overline{T\left\lbrack {\mathrm{\;B}\left( r\right) }\right\rbrack } \) est un voisinage de 0 dans \( F \) .

a) Using the Baire category theorem, show that for all \( r > 0,\overline{T\left\lbrack {\mathrm{\;B}\left( r\right) }\right\rbrack } \) is a neighborhood of 0 in \( F \).

> b) Soit \( r > 0 \) . Pour tout \( n \in \mathbb{N} \) , on pose \( {V}_{n} = \mathrm{B}\left( {r/{2}^{n}}\right) \) . Montrer que \( \overline{T\left( {V}_{1}\right) } \subset T\left( {V}_{0}\right) \) (indication : si \( {y}_{1} \in \overline{T\left( {V}_{1}\right) } \) , construire deux suites \( \left( {y}_{n}\right) \) de \( F \) et \( \left( {x}_{n}\right) \) de \( E \) telles que \( {y}_{n} \in T\left( {V}_{n}\right) ,{x}_{n} \in {V}_{n} \) et \( {y}_{n} - {y}_{n + 1} = T\left( {x}_{n}\right) \) puis considérer \( \left. {\sum {x}_{n}}\right) \)

b) Let \( r > 0 \). For all \( n \in \mathbb{N} \), we set \( {V}_{n} = \mathrm{B}\left( {r/{2}^{n}}\right) \). Show that \( \overline{T\left( {V}_{1}\right) } \subset T\left( {V}_{0}\right) \) (hint: if \( {y}_{1} \in \overline{T\left( {V}_{1}\right) } \), construct two sequences \( \left( {y}_{n}\right) \) of \( F \) and \( \left( {x}_{n}\right) \) of \( E \) such that \( {y}_{n} \in T\left( {V}_{n}\right) ,{x}_{n} \in {V}_{n} \) and \( {y}_{n} - {y}_{n + 1} = T\left( {x}_{n}\right) \) then consider \( \left. {\sum {x}_{n}}\right) \)

> c) En déduire que \( T \) est une application ouverte (i. e. pour tout ouvert \( \Omega \) de \( E, T\left( \Omega \right) \) est un ouvert de \( F \) ).

c) Deduce that \( T \) is an open map (i. e. for every open set \( \Omega \) of \( E, T\left( \Omega \right) \) is an open set of \( F \)).

> 2 / Théorème de Banach. Si \( T : E \rightarrow F \) est une application linéaire continue et bijective, montrer que \( {T}^{-1} \) est continue.

2 / Banach's Theorem. If \( T : E \rightarrow F \) is a continuous and bijective linear map, show that \( {T}^{-1} \) is continuous.

> Solution. 1/ a) Pour tout \( n \in {\mathbb{N}}^{ * },{F}_{n} = \overline{T\left\lbrack {\mathrm{\;B}\left( {nr}\right) }\right\rbrack } \) est un fermé de \( F \) . Comme \( T \) est surjective, \( { \cup }_{n \in \mathbb{N}}{F}_{n} = F \) , donc d’après le théorème de Baire, il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( {F}_{n} \neq \varnothing \) , i. e. il existe une boule ouverte \( \mathrm{B}\left( {x,\rho }\right) \) de centre \( x \) de rayon \( \rho > 0 \) incluse dans \( {F}_{n} \) .

Solution. 1/ a) For all \( n \in {\mathbb{N}}^{ * },{F}_{n} = \overline{T\left\lbrack {\mathrm{\;B}\left( {nr}\right) }\right\rbrack } \) is a closed subset of \( F \) . Since \( T \) is surjective, \( { \cup }_{n \in \mathbb{N}}{F}_{n} = F \) , therefore by Baire's theorem, there exists \( n \in {\mathbb{N}}^{ * } \) such that \( {F}_{n} \neq \varnothing \) , i.e., there exists an open ball \( \mathrm{B}\left( {x,\rho }\right) \) with center \( x \) and radius \( \rho > 0 \) included in \( {F}_{n} \) .

> On a alors \( \mathrm{B}\left( {0,\rho }\right) \subset {F}_{2n} \) . En effet, donnons nous \( y \in \mathrm{B}\left( {x,\rho }\right) \subset {F}_{n} \) . Il existe deux suites \( \left( {x}_{p}\right) \) et \( \left( {y}_{p}\right) \) de \( \mathrm{B}\left( {nr}\right) \) telles que

We then have \( \mathrm{B}\left( {0,\rho }\right) \subset {F}_{2n} \) . Indeed, let us take \( y \in \mathrm{B}\left( {x,\rho }\right) \subset {F}_{n} \) . There exist two sequences \( \left( {x}_{p}\right) \) and \( \left( {y}_{p}\right) \) of \( \mathrm{B}\left( {nr}\right) \) such that

\[
x = \mathop{\lim }\limits_{{p \rightarrow   + \infty }}T\left( {x}_{p}\right) \;\text{ et }\;y = \mathop{\lim }\limits_{{p \rightarrow   + \infty }}T\left( {y}_{p}\right) .
\]

Donc \( y - x = \mathop{\lim }\limits_{{p \rightarrow \infty }}T\left( {{y}_{p} - {x}_{p}}\right) \) , et comme pour tout \( p,{y}_{p} - {x}_{p} \in \mathrm{B}\left( {2nr}\right) \) , on en déduit \( y - x \in {F}_{2n} \) . Ceci est vrai pour tout \( y \in \mathrm{B}\left( {x,\rho }\right) \) donc \( \mathrm{B}\left( {0,\rho }\right) \subset {F}_{2n} \) .

> Thus \( y - x = \mathop{\lim }\limits_{{p \rightarrow \infty }}T\left( {{y}_{p} - {x}_{p}}\right) \) , and as for all \( p,{y}_{p} - {x}_{p} \in \mathrm{B}\left( {2nr}\right) \) , we deduce \( y - x \in {F}_{2n} \) . This is true for all \( y \in \mathrm{B}\left( {x,\rho }\right) \) so \( \mathrm{B}\left( {0,\rho }\right) \subset {F}_{2n} \) .

Finalement, on a

> Finally, we have

\[
\mathrm{B}\left( {0,\frac{\rho }{2n}}\right)  = \frac{1}{2n}\mathrm{\;B}\left( {0,\rho }\right)  \subset  \frac{1}{2n}{F}_{2n} = \overline{T\left\lbrack  {\mathrm{\;B}\left( r\right) }\right\rbrack  },
\]

d'où le résultat.

> whence the result.

b) Soit \( {y}_{1} \in \overline{T\left( {V}_{1}\right) } \) . Comme \( \overline{T\left( {V}_{2}\right) } \) est un voisinage de 0 d’après la question précédente, on a

> b) Let \( {y}_{1} \in \overline{T\left( {V}_{1}\right) } \) . Since \( \overline{T\left( {V}_{2}\right) } \) is a neighborhood of 0 according to the previous question, we have

\[
\overline{T\left( {V}_{1}\right) } \subset  T\left( {V}_{1}\right)  + \overline{T\left( {V}_{2}\right) }\;\text{ donc }\;\exists {x}_{1} \in  {V}_{1},\exists {y}_{2} \in  \overline{T\left( {V}_{2}\right) },\;{y}_{1} - {y}_{2} = T\left( {x}_{1}\right) .
\]

En itérant le procédé, on construit ainsi deux suites \( \left( {y}_{n}\right) \) de \( F \) et \( \left( {x}_{n}\right) \) de \( E \) telles que

> By iterating the process, we thus construct two sequences \( \left( {y}_{n}\right) \) of \( F \) and \( \left( {x}_{n}\right) \) of \( E \) such that

\[
\forall n \in  \mathbb{N},\;{y}_{n} \in  \overline{T\left( {V}_{n}\right) },\;{x}_{n} \in  {V}_{n}\;\text{ et }\;{y}_{n} - {y}_{n + 1} = T\left( {x}_{n}\right) .
\]

Pour tout \( n,{x}_{n} \in {V}_{n} \) donc \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} < r/{2}^{n} \) , donc \( \sum \begin{Vmatrix}{x}_{n}\end{Vmatrix} \) converge, donc \( E \) étant complet, \( \sum {x}_{n} \) converge. On note \( x = \mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n} \) . En écrivant

> For all \( n,{x}_{n} \in {V}_{n} \) so \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} < r/{2}^{n} \) , therefore \( \sum \begin{Vmatrix}{x}_{n}\end{Vmatrix} \) converges, so \( E \) being complete, \( \sum {x}_{n} \) converges. We denote \( x = \mathop{\sum }\limits_{{n = 1}}^{\infty }{x}_{n} \) . By writing

\[
\forall N \in  {\mathbb{N}}^{ * },\;T\left( {\mathop{\sum }\limits_{{n = 1}}^{N}{x}_{n}}\right)  = \mathop{\sum }\limits_{{n = 1}}^{N}T\left( {x}_{n}\right)  = \mathop{\sum }\limits_{{n = 1}}^{N}\left( {{y}_{n} - {y}_{n + 1}}\right)  = {y}_{1} - {y}_{N + 1}
\]

et en faisant tendre \( N \) vers \( + \infty \) , on obtient \( T\left( x\right) = {y}_{1} \) (ceci parce que \( T \) est continue et que \( {y}_{N} \rightarrow 0 \) lorsque \( N \rightarrow + \infty \) , ce dernier fait étant aussi une conséquence de la continuité de \( T \) ). Comme pour tout \( n,\begin{Vmatrix}{x}_{n}\end{Vmatrix} < r/{2}^{n} \) , on a \( \parallel x\parallel < r \) . Finalement, \( {y}_{1} \in T\left( {V}_{0}\right) \) .

> and letting \( N \) tend to \( + \infty \) , we obtain \( T\left( x\right) = {y}_{1} \) (this is because \( T \) is continuous and \( {y}_{N} \rightarrow 0 \) when \( N \rightarrow + \infty \) , the latter fact also being a consequence of the continuity of \( T \) ). As for all \( n,\begin{Vmatrix}{x}_{n}\end{Vmatrix} < r/{2}^{n} \) , we have \( \parallel x\parallel < r \) . Finally, \( {y}_{1} \in T\left( {V}_{0}\right) \) .

c) En combinant les résultats des deux questions précédentes, on s’aperçoit que \( T\left\lbrack {\mathrm{\;B}\left( r\right) }\right\rbrack \) est un voisinage de 0 pour tout \( r > 0 \) . Donc si \( U \) est un voisinage de \( 0, T\left( U\right) \) est un voisinage de 0.

> c) By combining the results of the two previous questions, we see that \( T\left\lbrack {\mathrm{\;B}\left( r\right) }\right\rbrack \) is a neighborhood of 0 for all \( r > 0 \) . Thus, if \( U \) is a neighborhood of \( 0, T\left( U\right) \) , it is a neighborhood of 0.

Considérons maintenant un ouvert \( \Omega \) de \( E \) et \( x \in \Omega \) . L’ensemble \( \Omega - x \) est un voisinage de 0, donc \( T\left( {\Omega - x}\right) \) est un voisinage de 0, donc \( T\left( \Omega \right) = T\left( {\Omega - x}\right) + T\left( x\right) \) est un voisinage de \( T\left( x\right) \) , et ceci pour tout \( x \in \Omega \) , donc \( T\left( \Omega \right) \) est ouvert.

> Now consider an open set \( \Omega \) of \( E \) and \( x \in \Omega \) . The set \( \Omega - x \) is a neighborhood of 0, so \( T\left( {\Omega - x}\right) \) is a neighborhood of 0, so \( T\left( \Omega \right) = T\left( {\Omega - x}\right) + T\left( x\right) \) is a neighborhood of \( T\left( x\right) \) , and this for all \( x \in \Omega \) , therefore \( T\left( \Omega \right) \) is open.

2/ Soit \( U = {T}^{-1} \) . D’après le théorème de l’application ouverte, pour tout ouvert \( \Omega \) de \( E \) , \( {U}^{-1}\left( \Omega \right) = T\left( \Omega \right) \) est un ouvert de \( E \) . L’image réciproque par \( U \) de tout ouvert est un ouvert, on en conclut que \( U = {T}^{-1} \) est continue.

> 2/ Let \( U = {T}^{-1} \) . According to the open mapping theorem, for any open set \( \Omega \) of \( E \) , \( {U}^{-1}\left( \Omega \right) = T\left( \Omega \right) \) is an open set of \( E \) . The preimage of any open set by \( U \) is an open set, we conclude that \( U = {T}^{-1} \) is continuous.

EXERCICE 7 (THÉORÉME DE BANACH-STEINHAUS ET CONSÉQUENCES).

> EXERCISE 7 (BANACH-STEINHAUS THEOREM AND CONSEQUENCES).

Soit \( E \) un espace de Banach, \( F \) un e.v.n. On note \( {\mathcal{L}}_{c}\left( {E, F}\right) \) l’e.v des applications linéaires continues de \( E \) dans \( F \) , muni de la norme \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \) .

> Let \( E \) be a Banach space, \( F \) a n.v.s. We denote by \( {\mathcal{L}}_{c}\left( {E, F}\right) \) the v.s. of continuous linear maps from \( E \) to \( F \) , equipped with the norm \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \) .

1/ Théorème de Banach-Steinhaus. Soit \( H \subset {\mathcal{L}}_{c}\left( {E, F}\right) \) . Montrer que ou bien \( {\left( \parallel f\parallel \right) }_{f \in H} \) est borné, ou bien il existe \( x \in E \) tel que \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel = + \infty \) .

> 1/ Banach-Steinhaus Theorem. Let \( H \subset {\mathcal{L}}_{c}\left( {E, F}\right) \) . Show that either \( {\left( \parallel f\parallel \right) }_{f \in H} \) is bounded, or there exists \( x \in E \) such that \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel = + \infty \) .

2/ (Une première conséquence.) Soit \( \left( {f}_{n}\right) \) une suite d’applications linéaires continues de \( E \) dans \( F \) , qui converge simplement vers une fonction \( f : E \rightarrow F \) . Montrer que \( f \) est une application linéaire et continue.

> 2/ (A first consequence.) Let \( \left( {f}_{n}\right) \) be a sequence of continuous linear maps from \( E \) to \( F \) that converges pointwise to a function \( f : E \rightarrow F \) . Show that \( f \) is a continuous linear map.

3 / (Une autre conséquence.) Soit \( {E}_{1} \) un espace de Banach, \( {E}_{2} \) un e.v.n. Soit \( B : {E}_{1} \times {E}_{2} \rightarrow \; F \) une application bilinéaire dont les applications partielles sont continues, c’est-à-dire

> 3/ (Another consequence.) Let \( {E}_{1} \) be a Banach space, \( {E}_{2} \) a n.v.s. Let \( B : {E}_{1} \times {E}_{2} \rightarrow \; F \) be a bilinear map whose partial maps are continuous, i.e.

- pour tout \( x \in  {E}_{1} \) , l’application \( B\left( {x, \cdot  }\right)  : {E}_{2} \rightarrow  F\;y \mapsto  B\left( {x, y}\right) \) est continue;

> - for all \( x \in  {E}_{1} \) , the map \( B\left( {x, \cdot  }\right)  : {E}_{2} \rightarrow  F\;y \mapsto  B\left( {x, y}\right) \) is continuous;

- pour tout \( y \in  {E}_{2} \) , l’application \( B\left( {\cdot , y}\right)  : {E}_{1} \rightarrow  F\;x \mapsto  B\left( {x, y}\right) \) est continue. Montrer que \( B \) est continue sur \( {E}_{1} \times  {E}_{2} \) .

> - for all \( y \in  {E}_{2} \) , the map \( B\left( {\cdot , y}\right)  : {E}_{1} \rightarrow  F\;x \mapsto  B\left( {x, y}\right) \) is continuous. Show that \( B \) is continuous on \( {E}_{1} \times  {E}_{2} \) .

Solution.1/ Pour tout \( k \in \mathbb{N} \) , on pose

> Solution.1/ For all \( k \in \mathbb{N} \) , we set

\[
{\Omega }_{k} = \{ x \in  E \mid  \mathop{\sup }\limits_{{f \in  H}}\parallel f\left( x\right) \parallel  > k\} .
\]

L’ensemble \( {\Omega }_{k} \) est ouvert. En effet, si \( {x}_{0} \in {\Omega }_{k} \) , il existe \( f \in H \) tel que \( \begin{Vmatrix}{f\left( {x}_{0}\right) }\end{Vmatrix} > k \) . Comme \( f \) est continue, il existe \( \rho > 0 \) tel que \( \parallel f\left( x\right) \parallel > k \) pour \( \begin{Vmatrix}{x - {x}_{0}}\end{Vmatrix} < \rho \) . Donc la boule \( B\left( {{x}_{0},\rho }\right) \) est contenue dans \( {\Omega }_{k} \) .

> The set \( {\Omega }_{k} \) is open. Indeed, if \( {x}_{0} \in {\Omega }_{k} \) , there exists \( f \in H \) such that \( \begin{Vmatrix}{f\left( {x}_{0}\right) }\end{Vmatrix} > k \) . Since \( f \) is continuous, there exists \( \rho > 0 \) such that \( \parallel f\left( x\right) \parallel > k \) for \( \begin{Vmatrix}{x - {x}_{0}}\end{Vmatrix} < \rho \) . Thus, the ball \( B\left( {{x}_{0},\rho }\right) \) is contained in \( {\Omega }_{k} \) .

Si chaque \( {\Omega }_{k} \) est dense dans \( E \) , alors \( E \) étant complet, le théorème de Baire assure que \( { \cap }_{k \in \mathbb{N}}{\Omega }_{k} \) est dense dans \( E \) , en particulier non vide. Si on choisit \( x \in { \cap }_{k \in \mathbb{N}}{\Omega }_{k} \) , on a alors \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel = + \infty . \)

> If each \( {\Omega }_{k} \) is dense in \( E \) , then since \( E \) is complete, the Baire category theorem ensures that \( { \cap }_{k \in \mathbb{N}}{\Omega }_{k} \) is dense in \( E \) , and in particular non-empty. If we choose \( x \in { \cap }_{k \in \mathbb{N}}{\Omega }_{k} \) , we then have \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel = + \infty . \)

Sinon, il existe un entier \( k \) tel que \( {\Omega }_{k} \) ne soit pas dense dans \( E \) . En d’autres termes,

> Otherwise, there exists an integer \( k \) such that \( {\Omega }_{k} \) is not dense in \( E \) . In other words,

\[
\exists {x}_{0} \in  E,\exists \rho  > 0,\;\mathrm{B}\left( {{x}_{0},\rho }\right)  \cap  {\Omega }_{k} = \varnothing ,
\]

de sorte que pour tout \( x \in \mathrm{B}\left( {{x}_{0},\rho }\right) ,\mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel \leq k \) . On en déduit

> so that for all \( x \in \mathrm{B}\left( {{x}_{0},\rho }\right) ,\mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel \leq k \) . We deduce from this

\[
\forall x \in  \mathrm{B}\left( {0,\rho }\right) ,\forall f \in  H,\;\parallel f\left( x\right) \parallel  = \begin{Vmatrix}{f\left( {x + {x}_{0}}\right)  - f\left( {x}_{0}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{f\left( {x + {x}_{0}}\right) }\end{Vmatrix} + \begin{Vmatrix}{f\left( {x}_{0}\right) }\end{Vmatrix} \leq  {2k}.
\]

Par continuité de chaque \( f \in H \) , cette inégalité reste vraie sur la boule fermée \( {\mathrm{B}}_{\mathrm{f}}\left( {0,\rho }\right) \) . Ainsi,

> By continuity of each \( f \in H \) , this inequality remains true on the closed ball \( {\mathrm{B}}_{\mathrm{f}}\left( {0,\rho }\right) \) . Thus,

\[
\forall f \in  H,\forall x \in  E,\parallel x\parallel  = 1,\;\parallel f\left( x\right) \parallel  = \frac{1}{\rho }\parallel f\left( {\rho x}\right) \parallel  \leq  \frac{2k}{\rho }\;\text{ donc }\;\forall f \in  H,\;\parallel f\parallel  \leq  \frac{2k}{\rho },
\]

d'où le résultat.

> whence the result.

2 / La fonction \( f \) , limite simple de fonctions linéaires, est clairement linéaire.

> 2/ The function \( f \) , as a pointwise limit of linear functions, is clearly linear.

Il reste à montrer la continuité de \( f \) . Appliquons le théorème de Banach-Steinhaus avec \( H = \; \left\{ {{f}_{n}, n \in \mathbb{N}}\right\} \) . La suite \( \left( {f}_{n}\right) \) converge simplement, donc pour tout \( x \in E,\mathop{\sup }\limits_{{n \in \mathbb{N}}}\begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} < + \infty \) . D’après la question précédente, ceci entraîne l’existence de \( M > 0 \) tel que \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) pour tout \( n \in \mathbb{N} \) . Si \( \parallel x\parallel = 1 \) , on a donc \( \begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq M \) pour tout \( n \) , donc \( \parallel f\left( x\right) \parallel \leq M \) . Ceci est vrai pour tout vecteur normé \( x \) , donc \( f \) est continue.

> It remains to show the continuity of \( f \) . Let us apply the Banach-Steinhaus theorem with \( H = \; \left\{ {{f}_{n}, n \in \mathbb{N}}\right\} \) . The sequence \( \left( {f}_{n}\right) \) converges pointwise, so for all \( x \in E,\mathop{\sup }\limits_{{n \in \mathbb{N}}}\begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} < + \infty \) . According to the previous question, this implies the existence of \( M > 0 \) such that \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) for all \( n \in \mathbb{N} \) . If \( \parallel x\parallel = 1 \) , we therefore have \( \begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq M \) for all \( n \) , hence \( \parallel f\left( x\right) \parallel \leq M \) . This is true for any normalized vector \( x \) , so \( f \) is continuous.

3/ Considérons l'ensemble

> 3/ Let us consider the set

\[
H = \{ B\left( {\cdot , y}\right) ,\parallel y\parallel  = 1\}  \subset  {\mathcal{L}}_{c}\left( {{E}_{1}, F}\right) .
\]

D’après les hypothèses, pour tout \( x \in {E}_{1} \) , l’application \( y \mapsto B\left( {x, y}\right) \) est continue. Ceci entraîne \( \mathop{\sup }\limits_{{\parallel y\parallel = 1}}\parallel B\left( {x, y}\right) \parallel < + \infty \) , autrement dit on a \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel < + \infty \) pour tout \( x \in {E}_{1} \) . L’e.v.n \( {E}_{1} \) est complet, donc d’après le théorème de Banach-Steinhaus,

> According to the hypotheses, for all \( x \in {E}_{1} \) , the mapping \( y \mapsto B\left( {x, y}\right) \) is continuous. This implies \( \mathop{\sup }\limits_{{\parallel y\parallel = 1}}\parallel B\left( {x, y}\right) \parallel < + \infty \) , in other words we have \( \mathop{\sup }\limits_{{f \in H}}\parallel f\left( x\right) \parallel < + \infty \) for all \( x \in {E}_{1} \) . The n.v.s. \( {E}_{1} \) is complete, so according to the Banach-Steinhaus theorem,

\[
\exists M > 0,\forall y \in  {E}_{2},\parallel y\parallel  = 1,\;\parallel B\left( {\cdot , y}\right) \parallel  \leq  M.
\]

Autrement dit, pour tout \( \left( {x, y}\right) \in {E}_{1} \times {E}_{2} \) vérifiant \( \parallel x\parallel = \parallel y\parallel = 1 \) , on a \( \parallel B\left( {x, y}\right) \parallel \leq M \) . Donc \( B \) est continue sur \( {E}_{1} \times {E}_{2} \) (c’est classique à partir de cette dernière inégalité !)

> In other words, for all \( \left( {x, y}\right) \in {E}_{1} \times {E}_{2} \) satisfying \( \parallel x\parallel = \parallel y\parallel = 1 \) , we have \( \parallel B\left( {x, y}\right) \parallel \leq M \) . Thus \( B \) is continuous on \( {E}_{1} \times {E}_{2} \) (this is standard from this last inequality!)

EXERCICE 8 (EXISTENCE DE FONCTIONS CONTINUES DIFFÉRENTES DE LEUR SÉRIE DE FOURIER). On note \( {\mathcal{C}}_{2\pi } \) l’ensemble des fonctions de \( \mathbb{R} \) dans \( \mathbb{C} \) qui sont \( {2\pi } \) -périodiques et continues. Pour tout \( f \in {\mathcal{C}}_{2\pi } \) , on note

> EXERCISE 8 (EXISTENCE OF CONTINUOUS FUNCTIONS DIFFERENT FROM THEIR FOURIER SERIES). Let \( {\mathcal{C}}_{2\pi } \) denote the set of functions from \( \mathbb{R} \) to \( \mathbb{C} \) that are \( {2\pi } \) -periodic and continuous. For all \( f \in {\mathcal{C}}_{2\pi } \) , we denote

\[
\forall p \in  \mathbb{Z},\;{c}_{p}\left( f\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( t\right) {e}^{-{ipt}}{dt}
\]

(coefficients de Fourier de \( f \) ). Pour tout \( n \in {\mathbb{N}}^{ * } \) , on considère l’application

> (Fourier coefficients of \( f \) ). For all \( n \in {\mathbb{N}}^{ * } \) , we consider the mapping

\[
{\ell }_{n} : {\mathcal{C}}_{2\pi } \rightarrow  \mathbb{C}\;f \mapsto  \mathop{\sum }\limits_{{p =  - n}}^{n}{c}_{p}\left( f\right) .
\]

On muni \( {\mathcal{C}}_{2\pi } \) de la norme \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{-\pi \leq t < \pi }}\left| {f\left( t\right) }\right| \) .

> We equip \( {\mathcal{C}}_{2\pi } \) with the norm \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{-\pi \leq t < \pi }}\left| {f\left( t\right) }\right| \) .

a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , montrer que \( {\ell }_{n} \) est une forme linéaire continue et calculer sa norme \( \begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = \mathop{\sup }\limits_{{\parallel f{\parallel }_{\infty } = 1}}\left| {{\ell }_{n}\left( f\right) }\right| . \)

> a) For all \( n \in {\mathbb{N}}^{ * } \) , show that \( {\ell }_{n} \) is a continuous linear form and calculate its norm \( \begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = \mathop{\sup }\limits_{{\parallel f{\parallel }_{\infty } = 1}}\left| {{\ell }_{n}\left( f\right) }\right| . \)

b) Montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = + \infty \) . Conclure avec le théorème de Banach-Steinhaus.

> b) Show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = + \infty \) . Conclude using the Banach-Steinhaus theorem.

Solution. a) L’application \( {\ell }_{n} \) est clairement une forme linéaire. La relation classique

> Solution. a) The mapping \( {\ell }_{n} \) is clearly a linear form. The classical relation

\[
\mathop{\sum }\limits_{{p =  - n}}^{n}{e}^{ipt} = \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }\;\text{ entraîne }\;\forall f \in  {\mathcal{C}}_{2\pi },\;{\ell }_{n}\left( f\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }f\left( t\right) {dt},
\]

donc si \( \parallel f{\parallel }_{\infty } = 1 \) , on a

> therefore if \( \parallel f{\parallel }_{\infty } = 1 \) , we have

\[
\left| {{\ell }_{n}\left( f\right) }\right|  \leq  \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left| \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }\right| {dt}.
\]

(*)

> Pour tout \( \varepsilon > 0 \) , on définit la fonction de \( {\mathcal{C}}_{2\pi } \)

For any \( \varepsilon > 0 \) , we define the function \( {\mathcal{C}}_{2\pi } \)

\[
{f}_{\varepsilon } : \mathbb{R} \rightarrow  \mathbb{C}\;t \mapsto  \frac{{D}_{n}\left( t\right) }{\left| {{D}_{n}\left( t\right) }\right|  + \varepsilon },\;\text{ où }\;{D}_{n}\left( t\right)  = \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }.
\]

On a \( {\begin{Vmatrix}{f}_{\varepsilon }\end{Vmatrix}}_{\infty } \leq 1 \) et on montre facilement que

> We have \( {\begin{Vmatrix}{f}_{\varepsilon }\end{Vmatrix}}_{\infty } \leq 1 \) and it is easy to show that

\[
\mathop{\lim }\limits_{\substack{{\varepsilon  \rightarrow  0} \\  {\varepsilon  > 0} }}\left| {{\ell }_{n}\left( {f}_{\varepsilon }\right) }\right|  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left| \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }\right| {dt}.
\]

Avec (*), on en déduit

> With (*), we deduce

\[
\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left| \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{\sin \left( {t/2}\right) }\right| {dt}.
\]

b) L’inégalité \( \left| {\sin \left( {t/2}\right) }\right| \leq \left| {t/2}\right| \) pour tout nombre réel \( t \) entraîne

> b) The inequality \( \left| {\sin \left( {t/2}\right) }\right| \leq \left| {t/2}\right| \) for any real number \( t \) implies

\[
\forall n \in  {\mathbb{N}}^{ * },\;\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} \geq  \frac{1}{\pi }{\int }_{0}^{\pi }\left| \frac{\sin \left\lbrack  {\left( {{2n} + 1}\right) t/2}\right\rbrack  }{t/2}\right| {dt} = \frac{2}{\pi }{\int }_{0}^{\left( {{2n} + 1}\right) \pi /2}\left| \frac{\sin u}{u}\right| {du}.
\]

Comme l’intégrale \( {\int }_{0}^{+\infty }\left| {\sin u/u}\right| {du} \) diverge (car \( {\int }_{\left( {n - 1}\right) \pi }^{n\pi }\left| {\sin u/u}\right| {du} \geq \frac{1}{n\pi }{\int }_{\left( {n - 1}\right) \pi }^{n\pi }\left| {\sin u}\right| {du} = \; \left. \frac{2}{n\pi }\right) \) , on en déduit \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = + \infty \) .

> Since the integral \( {\int }_{0}^{+\infty }\left| {\sin u/u}\right| {du} \) diverges (because \( {\int }_{\left( {n - 1}\right) \pi }^{n\pi }\left| {\sin u/u}\right| {du} \geq \frac{1}{n\pi }{\int }_{\left( {n - 1}\right) \pi }^{n\pi }\left| {\sin u}\right| {du} = \; \left. \frac{2}{n\pi }\right) \) , we deduce \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{\ell }_{n}\end{Vmatrix} = + \infty \) .

Maintenant, \( {\mathcal{C}}_{2\pi } \) est complet (car fermé de \( \mathcal{B}\left( {\mathbb{R},\mathbb{C}}\right) \) , e.v des fonctions bornées de \( \mathbb{R} \) dans \( \mathbb{C} \) qui est complet - voir l'exercice 1 page 21), et on peut donc appliquer le théorème de Banach-Steinhaus qui entraîne l’existence de \( f \in {\mathcal{C}}_{2\pi } \) tel que \( \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {{\ell }_{n}\left( f\right) }\right| = + \infty \) . Autrement dit, la série de Fourier de \( f \) en 0 diverge. La fonction \( f \) est donc différente de sa série de Fourier. En conclusion, il existe des fonctions continues différentes de leur série de Fourier.

> Now, \( {\mathcal{C}}_{2\pi } \) is complete (as a closed subset of \( \mathcal{B}\left( {\mathbb{R},\mathbb{C}}\right) \) , the vector space of bounded functions from \( \mathbb{R} \) to \( \mathbb{C} \) which is complete - see exercise 1 on page 21), and we can therefore apply the Banach-Steinhaus theorem which implies the existence of \( f \in {\mathcal{C}}_{2\pi } \) such that \( \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {{\ell }_{n}\left( f\right) }\right| = + \infty \) . In other words, the Fourier series of \( f \) at 0 diverges. The function \( f \) is therefore different from its Fourier series. In conclusion, there exist continuous functions that are different from their Fourier series.

Remarque. Un exemple explicite d'une fonction continue \( {2\pi } \) -périodique dont la série de Fourier diverge en 0 fait l'objet de l'exercice 4 page 275.

> Remark. An explicit example of a continuous \( {2\pi } \) -periodic function whose Fourier series diverges at 0 is the subject of exercise 4 on page 275.

##### Other applications

*Français : Autres applications*

Le lecteur amusé par les applications précédentes du théorème de Baire pourra s'exer-cer sur les suivantes :

> The reader amused by the previous applications of the Baire theorem may practice on the following:

- il n'existe pas de partition dénombrable de \( \left\lbrack  {0,1}\right\rbrack \) en fermés ;

> - there is no countable partition of \( \left\lbrack  {0,1}\right\rbrack \) into closed sets;

- il n’existe pas d’application \( f : \mathbb{R} \rightarrow  \mathbb{R} \) continue en tout point de \( \mathbb{Q} \) et discontinue en tout point de \( \mathbb{R} \smallsetminus  \mathbb{Q} \) (par contre, il existe des fonctions continues en tout point de \( \mathbb{R} \smallsetminus  \mathbb{Q} \) et discontinues en tout point de \( \mathbb{Q} \) , voir le problème 11 page 114) ;

> - there is no mapping \( f : \mathbb{R} \rightarrow  \mathbb{R} \) continuous at every point of \( \mathbb{Q} \) and discontinuous at every point of \( \mathbb{R} \smallsetminus  \mathbb{Q} \) (however, there exist functions continuous at every point of \( \mathbb{R} \smallsetminus  \mathbb{Q} \) and discontinuous at every point of \( \mathbb{Q} \) , see problem 11 on page 114);

- si \( {E}_{1} \) et \( {E}_{2} \) sont deux espaces métriques complets et si une fonction \( f \) définie sur \( {E}_{1} \times  {E}_{2} \) a toutes ses applications partielles continues, alors \( f \) est continue sur un ensemble dense.

> - if \( {E}_{1} \) and \( {E}_{2} \) are two complete metric spaces and if a function \( f \) defined on \( {E}_{1} \times  {E}_{2} \) has all its partial mappings continuous, then \( f \) is continuous on a dense set.

##### Remark on the Banach-Steinhaus theorem

*Français : Remarque sur le théorème de Banach-Steinhaus*

Il existe une version plus forte de ce théorème, valable sur des espaces vectoriels appelés espaces de Fréchet. Ce ne sont pas des espaces normés, mais des espaces métriques dont la distance n'est pas issue d'une norme.

> There is a stronger version of this theorem, valid for vector spaces called Fréchet spaces. These are not normed spaces, but metric spaces whose distance is not derived from a norm.

ANNEXE B

> APPENDIX B

##### Hilbert spaces

*Français : Espaces de Hilbert*

Cette annexe présente, sous forme d'un problème, les résultats généraux relatifs aux espaces de Hilbert. Ce problème est suivi de deux exercices indépendants :

> This appendix presents, in the form of a problem, the general results relating to Hilbert spaces. This problem is followed by two independent exercises:

- le premier porte sur la topologie faible dans un espace de Hilbert,

> - the first concerns weak topology in a Hilbert space,

- le second sur les opérateurs compacts et leur théorie spectrale dans les espaces de Hilbert.

> - the second concerns compact operators and their spectral theory in Hilbert spaces.

Cet appendice suppose connue la théorie des espaces préhilbertiens.

> This appendix assumes knowledge of the theory of pre-Hilbert spaces.
