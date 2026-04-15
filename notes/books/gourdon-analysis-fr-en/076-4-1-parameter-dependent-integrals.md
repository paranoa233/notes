#### 4.1. Parameter-dependent integrals

*Français : 4.1. Intégrales dépendant d'un paramètre*

Dans cette sous-partie, \( I \) désigne un intervalle quelconque de \( \mathbb{R} \) , d’extrémités \( a \) et \( b \) (avec \( - \infty \leq a < b \leq + \infty \) ), et \( E \) désigne un e.v.n complet.

> In this subsection, \( I \) denotes an arbitrary interval of \( \mathbb{R} \) , with endpoints \( a \) and \( b \) (with \( - \infty \leq a < b \leq + \infty \) ), and \( E \) denotes a complete n.v.s.

— THÉORÉME 1 (CONTINUITÉ SOUS LE SIGNE INTÉGRAL). Soit A un espace métrique et une application

> — THEOREM 1 (CONTINUITY UNDER THE INTEGRAL SIGN). Let A be a metric space and a mapping

\[
f : A \times  I \rightarrow  E\;\left( {x, t}\right)  \mapsto  f\left( {x, t}\right)
\]

vérifiant les propriétés suivantes

> satisfying the following properties

(i) pour tout \( x \in A \) , l’application \( f\left( {x, \cdot }\right) : t \mapsto f\left( {x, t}\right) \) est continue par morceaux sur I,

> (i) for all \( x \in A \) , the mapping \( f\left( {x, \cdot }\right) : t \mapsto f\left( {x, t}\right) \) is piecewise continuous on I,

(ii) pour tout \( t \in I \) , \( {l}^{\prime } \) application \( f\left( {\cdot , t}\right) : x \mapsto f\left( {x, t}\right) \) est continue sur \( A \)

> (ii) for all \( t \in I \) , \( {l}^{\prime } \) mapping \( f\left( {\cdot , t}\right) : x \mapsto f\left( {x, t}\right) \) is continuous on \( A \)

(iii) il existe une fonction positive \( \varphi \) , continue par morceaux et intégrable sur \( I \) , telle que \( \parallel f\left( {x, t}\right) \parallel \leq \varphi \left( t\right) \) pour tout \( x \in A \) (Hypothèse de domination).

> (iii) there exists a positive function \( \varphi \) , piecewise continuous and integrable on \( I \) , such that \( \parallel f\left( {x, t}\right) \parallel \leq \varphi \left( t\right) \) for all \( x \in A \) (Domination hypothesis).

Alors l'application

> Then the mapping

\[
\Phi  : A \rightarrow  E\;x \mapsto  {\int }_{a}^{b}f\left( {x, t}\right) {dt}
\]

est bien définie, et elle est continue sur A.

> is well-defined, and it is continuous on A.

Démonstration. L’hypothèse de domination montre que \( f\left( {x, \cdot }\right) \) est intégrable pour tout \( x \in A \) , donc \( \Phi \) est bien définie. Pour prouver qu’elle est continue en tout point \( x \in A \) , il suffit de montrer que pour toute suite \( \left( {x}_{n}\right) \) dans \( A \) convergeant vers \( x \) , on a bien \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\Phi \left( {x}_{n}\right) = \Phi \left( x\right) \) . Soit \( \left( {x}_{n}\right) \) une telle suite. La suite de fonctions \( \left( {f}_{n}\right) \) définie par \( {f}_{n} : I \rightarrow E\;t \mapsto f\left( {{x}_{n}, t}\right) \) converge simplement vers \( t \mapsto f\left( {x, t}\right) \) d’après l’hypothèse (ii). L’hypothèse (iii) nous permet d’appliquer le théorème de convergence dominée, qui donne \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{a}^{b}{f}_{n}\left( t\right) {dt} = {\int }_{a}^{b}f\left( {x, t}\right) {dt} \) , c’est-à-dire \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\Phi \left( {x}_{n}\right) = \Phi \left( x\right) . \)

> Proof. The domination hypothesis shows that \( f\left( {x, \cdot }\right) \) is integrable for all \( x \in A \) , so \( \Phi \) is well-defined. To prove that it is continuous at any point \( x \in A \) , it suffices to show that for any sequence \( \left( {x}_{n}\right) \) in \( A \) converging to \( x \) , we have \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\Phi \left( {x}_{n}\right) = \Phi \left( x\right) \) . Let \( \left( {x}_{n}\right) \) be such a sequence. The sequence of functions \( \left( {f}_{n}\right) \) defined by \( {f}_{n} : I \rightarrow E\;t \mapsto f\left( {{x}_{n}, t}\right) \) converges pointwise to \( t \mapsto f\left( {x, t}\right) \) according to hypothesis (ii). Hypothesis (iii) allows us to apply the dominated convergence theorem, which gives \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{a}^{b}{f}_{n}\left( t\right) {dt} = {\int }_{a}^{b}f\left( {x, t}\right) {dt} \) , that is to say \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\Phi \left( {x}_{n}\right) = \Phi \left( x\right) . \)

\( \rightarrow \) THÉORÉME 2 (DÉRIVATION SOUS LE SIGNE INTÉGRAL). Soit A un intervalle de \( \mathbb{R} \) et \( f : A \times I \rightarrow E\;\left( {x, t}\right) \mapsto f\left( {x, t}\right) \) une application vérifiant les propriétés suivantes

> \( \rightarrow \) THEOREM 2 (DIFFERENTIATION UNDER THE INTEGRAL SIGN). Let A be an interval of \( \mathbb{R} \) and \( f : A \times I \rightarrow E\;\left( {x, t}\right) \mapsto f\left( {x, t}\right) \) a mapping satisfying the following properties

(i) pour tout \( x \in A \) , l’application \( f\left( {x, \cdot }\right) : t \mapsto f\left( {x, t}\right) \) est continue par morceaux et intégrable sur I,

> (i) for all \( x \in A \) , the mapping \( f\left( {x, \cdot }\right) : t \mapsto f\left( {x, t}\right) \) is piecewise continuous and integrable on I,

(ii) \( f \) admet une dérivée partielle \( \frac{\partial f}{\partial x} \) vérifiant les hypothèses du théorème précédent. Alors l'application

> (ii) \( f \) admits a partial derivative \( \frac{\partial f}{\partial x} \) satisfying the hypotheses of the previous theorem. Then the mapping

\[
\Phi  : A \rightarrow  E\;x \mapsto  {\int }_{a}^{b}f\left( {x, t}\right) {dt}
\]

est de classe \( {\mathcal{C}}^{1} \) sur \( A \) et on a

> is of class \( {\mathcal{C}}^{1} \) on \( A \) and we have

\[
\forall x \in  A,\;{\Phi }^{\prime }\left( x\right)  = {\int }_{a}^{b}\frac{\partial f}{\partial x}\left( {x, t}\right) {dt}.
\]

Démonstration. Soit \( x \in A \) et \( \left( {x}_{n}\right) \) une suite dans \( A \smallsetminus \{ x\} \) convergeant vers \( x \) . La suite de fonctions \( \left( {g}_{n}\right) \) définie par \( {g}_{n} : I \rightarrow E\;t \mapsto \left( {f\left( {{x}_{n}, t}\right) - f\left( {x, t}\right) }\right) /\left( {{x}_{n} - x}\right) \) converge simplement vers \( \frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) sur \( I \) . La fonction \( {g}_{n} \) est bien continue par morceaux et intégrable sur \( I \) . De plus, comme \( \begin{Vmatrix}{\frac{\partial f}{\partial x}\left( {y, t}\right) }\end{Vmatrix} \leq \varphi \left( t\right) \) pour tout \( y \in I \) , l’inégalité des accroissements finis entraîne que \( \begin{Vmatrix}{{g}_{n}\left( t\right) }\end{Vmatrix} \leq \varphi \left( t\right) \) . Ainsi, on peut appliquer le théorème de convergence dominée qui nous assure la convergence de \( {\int }_{I}{g}_{n} \) vers \( {\int }_{I}\frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) . Comme \( {\int }_{I}{g}_{n} = \left( {\Phi \left( {x}_{n}\right) - \Phi \left( x\right) }\right) /\left( {{x}_{n} - x}\right) \) , nous venons de démontrer que \( \Phi \) est dérivable en \( x \) et que \( {\Phi }^{\prime }\left( x\right) = {\int }_{I}\frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) . La dernière intégrande vérifiant les hypothèses du théorème de continuité sous le signe intégral, on en déduit que \( {\Phi }^{\prime } \) est continue.

> Proof. Let \( x \in A \) and \( \left( {x}_{n}\right) \) be a sequence in \( A \smallsetminus \{ x\} \) converging to \( x \) . The sequence of functions \( \left( {g}_{n}\right) \) defined by \( {g}_{n} : I \rightarrow E\;t \mapsto \left( {f\left( {{x}_{n}, t}\right) - f\left( {x, t}\right) }\right) /\left( {{x}_{n} - x}\right) \) converges pointwise to \( \frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) on \( I \) . The function \( {g}_{n} \) is indeed piecewise continuous and integrable on \( I \) . Furthermore, since \( \begin{Vmatrix}{\frac{\partial f}{\partial x}\left( {y, t}\right) }\end{Vmatrix} \leq \varphi \left( t\right) \) for all \( y \in I \) , the mean value inequality implies that \( \begin{Vmatrix}{{g}_{n}\left( t\right) }\end{Vmatrix} \leq \varphi \left( t\right) \) . Thus, we can apply the dominated convergence theorem, which ensures the convergence of \( {\int }_{I}{g}_{n} \) to \( {\int }_{I}\frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) . As \( {\int }_{I}{g}_{n} = \left( {\Phi \left( {x}_{n}\right) - \Phi \left( x\right) }\right) /\left( {{x}_{n} - x}\right) \) , we have just shown that \( \Phi \) is differentiable at \( x \) and that \( {\Phi }^{\prime }\left( x\right) = {\int }_{I}\frac{\partial f}{\partial x}\left( {x, \cdot }\right) \) . Since the last integrand satisfies the hypotheses of the theorem of continuity under the integral sign, we deduce that \( {\Phi }^{\prime } \) is continuous.

Remarque 1. - Les résultats des deux théorèmes précédents restent vrais lorsque l’hypothèse de domination est vérifiée uniquement sur un voisinage de tout point de \( A \) (la continuité, la dérivabilité, sont des propriétés locales). C’est en particulier le cas si \( A \subset {\mathbb{R}}^{n} \) et si l’hypothèse de domination est vraie sur tout compact \( K \) de \( A \) .

> Remark 1. - The results of the two previous theorems remain true when the domination hypothesis is satisfied only on a neighborhood of every point of \( A \) (continuity and differentiability are local properties). This is in particular the case if \( A \subset {\mathbb{R}}^{n} \) and if the domination hypothesis is true on every compact \( K \) of \( A \) .

- Lorsque les intégrales définissant \( \Phi \) sont semi-convergentes, les théorèmes précédents ne s’appliquent plus. On passe en général par une suite de fonctions \( {f}_{n}\left( x\right)  = {\int }_{{K}_{n}}f\left( {x, \cdot  }\right) \) où les \( {K}_{n} \) sont des segments de \( I \) qui tendent vers \( I \) , puis on prouve des résultats de convergence uniforme pour \( \left( {f}_{n}\right) \) (voir un exemple dans la solution 2/b) de l’exercice 4 page 168).

> - When the integrals defining \( \Phi \) are semi-convergent, the previous theorems no longer apply. We generally use a sequence of functions \( {f}_{n}\left( x\right)  = {\int }_{{K}_{n}}f\left( {x, \cdot  }\right) \) where the \( {K}_{n} \) are segments of \( I \) that tend toward \( I \) , then we prove uniform convergence results for \( \left( {f}_{n}\right) \) (see an example in the solution 2/b) of exercise 4 on page 168).

Dans le cas où \( I \) est un segment de \( \mathbb{R} \) (et \( A \) un intervalle de \( \mathbb{R} \) ), et \( f \) continue, l'hypothèse de domination n'est plus nécessaire, comme l'exprime le corollaire suivant.

> In the case where \( I \) is a segment of \( \mathbb{R} \) (and \( A \) an interval of \( \mathbb{R} \)), and \( f \) is continuous, the domination hypothesis is no longer necessary, as expressed by the following corollary.

\( \rightarrow \) COROLLAIRE 1. Soit A un intervalle de \( \mathbb{R} \) et \( \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) . Soit une application \( f : A \times \left\lbrack {a, b}\right\rbrack \rightarrow E\;\left( {x, t}\right) \mapsto f\left( {x, t}\right) \) continue sur \( A \times \left\lbrack {a, b}\right\rbrack \) . Alors l’application

> \( \rightarrow \) COROLLARY 1. Let A be an interval of \( \mathbb{R} \) and \( \left\lbrack {a, b}\right\rbrack \) a segment of \( \mathbb{R} \) . Let \( f : A \times \left\lbrack {a, b}\right\rbrack \rightarrow E\;\left( {x, t}\right) \mapsto f\left( {x, t}\right) \) be a mapping continuous on \( A \times \left\lbrack {a, b}\right\rbrack \) . Then the mapping

\[
\Phi  : A \rightarrow  E\;x \mapsto  {\int }_{a}^{b}f\left( {x, t}\right) {dt}
\]

est continue sur A. Si de plus, \( f \) est dérivable par rapport \( \dot{a}x \) et si \( \frac{\partial f}{\partial x} \) est continue sur \( A \times \left\lbrack {a, b}\right\rbrack \) , alors \( \Phi \) est de classe \( {\mathcal{C}}^{1} \) sur \( A \) et on a \( {\Phi }^{\prime }\left( x\right) = {\int }_{a}^{b}\frac{\partial f}{\partial x}\left( {x, t}\right) {dt} \) .

> is continuous on A. If, in addition, \( f \) is differentiable with respect to \( \dot{a}x \) and if \( \frac{\partial f}{\partial x} \) is continuous on \( A \times \left\lbrack {a, b}\right\rbrack \) , then \( \Phi \) is of class \( {\mathcal{C}}^{1} \) on \( A \) and we have \( {\Phi }^{\prime }\left( x\right) = {\int }_{a}^{b}\frac{\partial f}{\partial x}\left( {x, t}\right) {dt} \) .

Démonstration. Soit \( K \) un compact de \( A \) . On peut appliquer le théorème 1 sur \( K \times \left\lbrack {a, b}\right\rbrack \) (l’hypothèse de domination est vérifiée car \( f \) , continue sur le compact \( K \times \left\lbrack {a, b}\right\rbrack \) , y est bornée) qui prouve que \( \Phi \) est continue sur \( K \) . Donc \( \Phi \) est continue sur tout compact de \( A \) , donc sur \( A \) tout entier. On montre de la même manière les résultats relatifs à la dérivation de \( \Phi \) .

> Proof. Let \( K \) be a compact subset of \( A \) . We can apply Theorem 1 on \( K \times \left\lbrack {a, b}\right\rbrack \) (the domination hypothesis is satisfied because \( f \) , continuous on the compact set \( K \times \left\lbrack {a, b}\right\rbrack \) , is bounded there), which proves that \( \Phi \) is continuous on \( K \) . Thus \( \Phi \) is continuous on every compact subset of \( A \) , and therefore on all of \( A \) . The results relating to the differentiation of \( \Phi \) are shown in the same way.

Remarque 2. On peut également obtenir ce corollaire sans passer par le théorème de convergence dominée,à partir de l’uniforme continuité de \( f \) (et \( \frac{\partial f}{\partial x} \) ) sur \( K \times \left\lbrack {a, b}\right\rbrack \) .

> Remark 2. This corollary can also be obtained without using the dominated convergence theorem, starting from the uniform continuity of \( f \) (and \( \frac{\partial f}{\partial x} \) ) on \( K \times \left\lbrack {a, b}\right\rbrack \) .

La fonction gamma. La fonction gamma est une fonction classique définie par

> The gamma function. The gamma function is a classical function defined by

\[
\Gamma  : \rbrack 0, + \infty \left\lbrack  { \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{0}^{+\infty }{e}^{-t}{t}^{x - 1}{dt}.}\right.
\]

Cette fonction vérifie les propriétés suivantes (démontrées dans le sujet d'étude 1 page 315, plus largement consacré à l'étude de cette fonction)

> This function satisfies the following properties (proven in study topic 1 on page 315, which is more broadly devoted to the study of this function)

- La fonction \( \Gamma \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \rbrack 0, + \infty \lbrack \) et pour tout \( n \in  {\mathbb{N}}^{ * } \) on a

> - The function \( \Gamma \) is of class \( {\mathcal{C}}^{\infty } \) on \( \rbrack 0, + \infty \lbrack \) and for all \( n \in  {\mathbb{N}}^{ * } \) we have

\[
\forall x > 0,\;{\Gamma }^{\left( n\right) }\left( x\right)  = {\int }_{0}^{+\infty }{\left( \log t\right) }^{n}{e}^{-t}{t}^{x - 1}{dt}.
\]

- On a la relation fonctionnelle \( \Gamma \left( {x + 1}\right)  = {x\Gamma }\left( x\right) \) pour tout \( x > 0 \) .

> - We have the functional relation \( \Gamma \left( {x + 1}\right)  = {x\Gamma }\left( x\right) \) for all \( x > 0 \) .

- En particulier, \( \Gamma \left( 1\right)  = 1 \) et \( \Gamma \left( {n + 1}\right)  = n \) ! pour tout entier \( n \in  \mathbb{N} \) .

> - In particular, \( \Gamma \left( 1\right)  = 1 \) and \( \Gamma \left( {n + 1}\right)  = n \) ! for all integers \( n \in  \mathbb{N} \) .

- On a \( \Gamma \left( {1/2}\right)  = \sqrt{\pi } \) (le changement de variable \( t = {u}^{2} \) donne \( \Gamma \left( {1/2}\right)  = {2I} \) avec \( I = {\int }_{0}^{+\infty }{e}^{-{u}^{2}}{du} \) et le calcul de \( I \) est classique - voir l’exercice 2 page 167).

> - We have \( \Gamma \left( {1/2}\right)  = \sqrt{\pi } \) (the change of variable \( t = {u}^{2} \) gives \( \Gamma \left( {1/2}\right)  = {2I} \) with \( I = {\int }_{0}^{+\infty }{e}^{-{u}^{2}}{du} \) and the calculation of \( I \) is classical - see exercise 2 on page 167).
