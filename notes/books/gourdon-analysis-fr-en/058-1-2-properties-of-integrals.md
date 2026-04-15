#### 1.2. Properties of integrals

*Français : 1.2. Propriétés des intégrales*

Nous commençons par donner pêle-mêle les propriétés les plus élémentaires.

> We begin by listing the most elementary properties in no particular order.

- Relation de Chasles. Soit \( f : \left\lbrack  {a, b}\right\rbrack   \rightarrow  E \) continue par morceaux et \( c \in  \rbrack a, b\lbrack \) . On a \( {\int }_{a}^{b}f\left( x\right) {dx} = {\int }_{a}^{c}f\left( x\right) {dx} + {\int }_{c}^{b}f\left( x\right) {dx}. \)

> - Chasles' relation. Let \( f : \left\lbrack  {a, b}\right\rbrack   \rightarrow  E \) be piecewise continuous and \( c \in  \rbrack a, b\lbrack \) . We have \( {\int }_{a}^{b}f\left( x\right) {dx} = {\int }_{a}^{c}f\left( x\right) {dx} + {\int }_{c}^{b}f\left( x\right) {dx}. \)

- Linéarité de l’intégrale. L’ensemble \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) des fonctions continues par morceaux sur \( \left\lbrack  {a, b}\right\rbrack \) est un \( \mathbb{K} \) -e.v et l’application \( {\mathcal{C}}_{m}\left( \left\lbrack  {a, b}\right\rbrack  \right)  \rightarrow  E\;\varphi  \mapsto  {\int }_{a}^{b}\varphi \left( x\right) {dx} \) est linéaire.

> - Linearity of the integral. The set \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) of piecewise continuous functions on \( \left\lbrack  {a, b}\right\rbrack \) is a \( \mathbb{K} \) -vector space and the mapping \( {\mathcal{C}}_{m}\left( \left\lbrack  {a, b}\right\rbrack  \right)  \rightarrow  E\;\varphi  \mapsto  {\int }_{a}^{b}\varphi \left( x\right) {dx} \) is linear.

- Positivité de l’intégrale. Si \( f, g : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) sont continues par morceaux et si \( f \geq  g \) sur \( \left\lbrack  {a, b}\right\rbrack \) , alors \( {\int }_{a}^{b}f\left( x\right) {dx} \geq  {\int }_{a}^{b}g\left( x\right) {dx} \) (le cas de l’inégalité stricte est plus délicat ; voir la proposition 4).

> - Positivity of the integral. If \( f, g : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) are piecewise continuous and if \( f \geq  g \) on \( \left\lbrack  {a, b}\right\rbrack \) , then \( {\int }_{a}^{b}f\left( x\right) {dx} \geq  {\int }_{a}^{b}g\left( x\right) {dx} \) (the case of strict inequality is more delicate; see proposition 4).

- Si \( \parallel .\parallel \) est une norme sur \( E \) , alors \( \begin{Vmatrix}{{\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix} \leq  {\int }_{a}^{b}\parallel f\left( x\right) \parallel {dx} \) .

> - If \( \parallel .\parallel \) is a norm on \( E \) , then \( \begin{Vmatrix}{{\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix} \leq  {\int }_{a}^{b}\parallel f\left( x\right) \parallel {dx} \) .

Proposition 3. Soit \( \left( {f}_{n}\right) \) une suite de fonctions continues par morceaux de \( \left\lbrack {a, b}\right\rbrack \) dans E qui converge uniformément sur \( \left\lbrack {a, b}\right\rbrack \) vers une fonction continue par morceaux \( f \) . Alors

> Proposition 3. Let \( \left( {f}_{n}\right) \) be a sequence of piecewise continuous functions from \( \left\lbrack {a, b}\right\rbrack \) to E that converges uniformly on \( \left\lbrack {a, b}\right\rbrack \) to a piecewise continuous function \( f \) . Then

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}{f}_{n}\left( x\right) {dx} = {\int }_{a}^{b}f\left( x\right) {dx}.
\]

(*)

> Remarque 4. Le théorème de convergence dominée (voir théorème 3 page 151) offre un cadre beaucoup plus commode pour obtenir la convergence d'intégrales d'une suite de fonctions, et c'est ce dernier que l'on utilise le plus souvent.

Remark 4. The dominated convergence theorem (see theorem 3 on page 151) offers a much more convenient framework for obtaining the convergence of integrals of a sequence of functions, and it is the latter that is most often used.

> Proposition 4. Soient \( f \) et \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) deux fonctions continues. Si \( f \geq g \) sur \( \left\lbrack {a, b}\right\rbrack \) et s’il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( f\left( c\right) > g\left( c\right) \) , alors \( {\int }_{a}^{b}f\left( x\right) {dx} > {\int }_{a}^{b}g\left( x\right) {dx} \) .

Proposition 4. Let \( f \) and \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be two continuous functions. If \( f \geq g \) on \( \left\lbrack {a, b}\right\rbrack \) and if there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( f\left( c\right) > g\left( c\right) \), then \( {\int }_{a}^{b}f\left( x\right) {dx} > {\int }_{a}^{b}g\left( x\right) {dx} \).

> Démonstration. On pose \( \gamma = f\left( c\right) - g\left( c\right) > 0 \) . La continuité de \( f - g \) en \( c \) entraîne l’existence d’un segment non réduit à un singleton \( \left\lbrack {\alpha ,\beta }\right\rbrack \) contenant \( c \) tel que \( f\left( t\right) \geq g\left( t\right) + \gamma /2 \) pour tout \( t \in \left\lbrack {\alpha ,\beta }\right\rbrack \) . Ainsi,

Proof. Let \( \gamma = f\left( c\right) - g\left( c\right) > 0 \). The continuity of \( f - g \) at \( c \) implies the existence of a non-degenerate interval \( \left\lbrack {\alpha ,\beta }\right\rbrack \) containing \( c \) such that \( f\left( t\right) \geq g\left( t\right) + \gamma /2 \) for all \( t \in \left\lbrack {\alpha ,\beta }\right\rbrack \). Thus,

\[
{\int }_{\alpha }^{\beta }f\left( x\right) {dx} \geq  {\int }_{\alpha }^{\beta }\left( {g\left( x\right)  + \frac{\gamma }{2}}\right) {dx} = {\int }_{\alpha }^{\beta }g\left( x\right) {dx} + \frac{\left( {\beta  - \alpha }\right) \gamma }{2} > {\int }_{\alpha }^{\beta }g\left( t\right) {dt}.
\]

Comme \( f \geq g \) sur \( \left\lbrack {a, b}\right\rbrack \) , on a par ailleurs

> Since \( f \geq g \) on \( \left\lbrack {a, b}\right\rbrack \), we also have

\[
{\int }_{a}^{\alpha }f\left( x\right) {dx} \geq  {\int }_{a}^{\alpha }g\left( x\right) {dx}\;\text{ et }\;{\int }_{\beta }^{b}f\left( x\right) {dx} \geq  {\int }_{\beta }^{b}g\left( x\right) {dx}.
\]

On en déduit facilement le résultat avec la relation de Chasles.

> The result follows easily from the Chasles relation.

##### Norms and integrals.

*Français : Normes et intégrales.*

THÉORÉME 1 (INÉGALITÉ DE SCHWARZ). Soient \( f, g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) deux applications continues par morceaux. Alors

> THEOREM 1 (SCHWARZ INEQUALITY). Let \( f, g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) be two piecewise continuous mappings. Then

\[
{\left| {\int }_{a}^{b}\overline{f\left( x\right) }g\left( x\right) dx\right| }^{2} \leq  \left( {{\int }_{a}^{b}{\left| f\left( x\right) \right| }^{2}{dx}}\right)  \cdot  \left( {{\int }_{a}^{b}{\left| g\left( x\right) \right| }^{2}{dx}}\right) .
\]

Si f et g sont continues et f non identiquement nulle, cette inégalité est une égalité si et seulement s’il existe \( \alpha \in \mathbb{C} \) tel que \( g\left( x\right) = {\alpha f}\left( x\right) \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) .

> If f and g are continuous and f is not identically zero, this inequality is an equality if and only if there exists \( \alpha \in \mathbb{C} \) such that \( g\left( x\right) = {\alpha f}\left( x\right) \) for all \( x \in \left\lbrack {a, b}\right\rbrack \).

Démonstration. Désignons par \( {\mathcal{C}}_{m}\left( \left\lbrack {a, b}\right\rbrack \right) \) l’algèbre des fonctions continues par morceaux de \( \left\lbrack {a, b}\right\rbrack \) dans \( \mathbb{C} \) , et considérons la forme hermitienne positive \( \Phi : {\mathcal{C}}_{m}\left( \left\lbrack {a, b}\right\rbrack \right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{a}^{b}\overline{f\left( x\right) }f\left( x\right) {dx} \) , dont la forme polaire est

> Proof. Let \( {\mathcal{C}}_{m}\left( \left\lbrack {a, b}\right\rbrack \right) \) denote the algebra of piecewise continuous functions from \( \left\lbrack {a, b}\right\rbrack \) to \( \mathbb{C} \), and consider the positive Hermitian form \( \Phi : {\mathcal{C}}_{m}\left( \left\lbrack {a, b}\right\rbrack \right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{a}^{b}\overline{f\left( x\right) }f\left( x\right) {dx} \), whose polar form is

\[
\varphi  : {\mathcal{C}}_{m}{\left( \left\lbrack  a, b\right\rbrack  \right) }^{2} \rightarrow  \mathbb{C}\;\left( {f, g}\right)  \mapsto  {\int }_{a}^{b}\overline{f\left( x\right) }g\left( x\right) {dx}
\]

(voir le tome Algèbre). L'inégalité de Schwarz appliquée à \( \varphi \) donne

> (see the Algebra volume). Applying the Schwarz inequality to \( \varphi \) gives

\[
\forall f, g \in  {\mathcal{C}}_{m}\left( \left\lbrack  {a, b}\right\rbrack  \right) ,\;{\left| \varphi \left( f, g\right) \right| }^{2} \leq  \Phi \left( f\right) \Phi \left( g\right) ,
\]

d'où la première assertion du théorème. La restriction de \( \Phi \) à l'e.v des fonctions continues sur \( \left\lbrack {a, b}\right\rbrack \) est définie, et on sait alors que l’inégalité de Schwarz est une égalité si et seulement si \( f \) et \( g \) forment une famille liée, d’où la seconde assertion du théorème.

> whence the first assertion of the theorem. The restriction of \( \Phi \) to the vector space of continuous functions on \( \left\lbrack {a, b}\right\rbrack \) is defined, and it is known that the Schwarz inequality is an equality if and only if \( f \) and \( g \) are linearly dependent, whence the second assertion of the theorem.

Conséquence : Sur l’e.v \( \mathcal{C}\left( {\left\lbrack {a, b}\right\rbrack ,\mathbb{K}}\right) \) des fonctions continues sur \( \left\lbrack {a, b}\right\rbrack \) , les applications

> Consequence: On the vector space \( \mathcal{C}\left( {\left\lbrack {a, b}\right\rbrack ,\mathbb{K}}\right) \) of continuous functions on \( \left\lbrack {a, b}\right\rbrack \), the mappings

\[
{N}_{1}\left( f\right)  = {\int }_{a}^{b}\left| {f\left( t\right) }\right| {dt},\;{N}_{2}\left( f\right)  = \sqrt{{\int }_{a}^{b}{\left| f\left( t\right) \right| }^{2}{dt}},\;{N}_{\infty }\left( f\right)  = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}\left| {f\left( t\right) }\right|
\]

sont des normes. L'inégalité de Schwarz entraîne que \( {N}_{2} \) vérifie bien l'inégalité triangu-laire ; la nullité de \( {N}_{1}\left( f\right) \) ou \( {N}_{2}\left( f\right) \) entraîne bien celle de \( f \) d’après la proposition 4.

> are norms. The Schwarz inequality implies that \( {N}_{2} \) indeed satisfies the triangle inequality; the vanishing of \( {N}_{1}\left( f\right) \) or \( {N}_{2}\left( f\right) \) indeed implies that of \( f \) according to Proposition 4.

(i) La norme \( {N}_{1} \) s’appelle norme de la convergence en moyenne.

> (i) The norm \( {N}_{1} \) is called the mean convergence norm.

(ii) La norme \( {N}_{2} \) s’appelle norme de la convergence en moyenne quadratique.

> (ii) The norm \( {N}_{2} \) is called the mean square convergence norm.

(iii) La norme \( {N}_{\infty } \) (encore notée \( \parallel \cdot {\parallel }_{\infty } \) ) s’appelle norme de la convergence uniforme.

> (iii) The norm \( {N}_{\infty } \) (also denoted \( \parallel \cdot {\parallel }_{\infty } \) ) is called the uniform convergence norm.

Ces normes vérifient les inégalités

> These norms satisfy the inequalities

\[
{N}_{1}\left( f\right)  \leq  \sqrt{b - a}{N}_{2}\left( f\right)  \leq  \left( {b - a}\right) \parallel f{\parallel }_{\infty }.
\]

Étude de la fonction \( x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) .

> Study of the function \( x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) .

\( \rightarrow \) THÉORÉME 2. Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une fonction continue par morceaux sur \( \left\lbrack {a, b}\right\rbrack \) . Alors l’application \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E\;x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) est \( {\mathcal{C}}^{1} \) par morceaux et continue sur \( \left\lbrack {a, b}\right\rbrack \) . De plus, \( F \) est dérivable à gauche et à droite en tout point \( x \) de \( I \) , et on a \( {F}_{g}^{\prime }\left( x\right) = \mathop{\lim }\limits_{\substack{{t \rightarrow x} \\ {t < x} }}f\left( t\right) \) et \( {F}_{d}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{t \rightarrow x}}f\left( t\right) \) . En particulier, si \( f \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) alors \( F \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {a, b}\right\rbrack \) et \( {F}^{\prime }\left( x\right) = f\left( x\right) \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) .

> \( \rightarrow \) THEOREM 2. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a piecewise continuous function on \( \left\lbrack {a, b}\right\rbrack \) . Then the mapping \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E\;x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) is piecewise \( {\mathcal{C}}^{1} \) and continuous on \( \left\lbrack {a, b}\right\rbrack \) . Furthermore, \( F \) is differentiable from the left and from the right at every point \( x \) of \( I \) , and we have \( {F}_{g}^{\prime }\left( x\right) = \mathop{\lim }\limits_{\substack{{t \rightarrow x} \\ {t < x} }}f\left( t\right) \) and \( {F}_{d}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{t \rightarrow x}}f\left( t\right) \) . In particular, if \( f \) is continuous on \( \left\lbrack {a, b}\right\rbrack \) then \( F \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {a, b}\right\rbrack \) and \( {F}^{\prime }\left( x\right) = f\left( x\right) \) for all \( x \in \left\lbrack {a, b}\right\rbrack \) .

COROLLAIRE 1. Toute application continue \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) admet au moins une primitive \( F \) , et pour toute primitive \( F \) de \( f \) , on a \( {\int }_{a}^{b}f\left( x\right) {dx} = {\left\lbrack F\right\rbrack }_{a}^{b} = F\left( b\right) - F\left( a\right) \) .

> COROLLARY 1. Every continuous mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) admits at least one primitive \( F \) , and for any primitive \( F \) of \( f \) , we have \( {\int }_{a}^{b}f\left( x\right) {dx} = {\left\lbrack F\right\rbrack }_{a}^{b} = F\left( b\right) - F\left( a\right) \) .

C'est ce dernier résultat qui amène à rechercher des primitives d'une fonction pour calculer son intégrale. Ce problème sera étudié plus particulièrement dans la partie 2 de ce chapitre. En l’appliquant à \( f = u{v}^{\prime } + {u}^{\prime }v \) dont la primitive est \( F = {uv} \) , on obtient le résultat qui suit.

> It is this last result that leads to searching for primitives of a function to calculate its integral. This problem will be studied more specifically in part 2 of this chapter. By applying it to \( f = u{v}^{\prime } + {u}^{\prime }v \) whose primitive is \( F = {uv} \) , we obtain the following result.

\( \rightarrow \) THÉORÉME 3 (INTÉGRATION PAR PARTIES). Soient \( u, v : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) deux fonctions de classe \( {\mathcal{C}}^{1} \) . Alors

> \( \rightarrow \) THEOREM 3 (INTEGRATION BY PARTS). Let \( u, v : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) be two functions of class \( {\mathcal{C}}^{1} \) . Then

\[
{\int }_{a}^{b}u\left( x\right) {v}^{\prime }\left( x\right) {dx} = {\left\lbrack  u \cdot  v\right\rbrack  }_{a}^{b} - {\int }_{a}^{b}{u}^{\prime }\left( x\right) v\left( x\right) {dx}.
\]

Citons enfin un dernier résultat, particulièrement utilisé lors de calculs de primitives.

> Finally, let us cite one last result, particularly used when calculating primitives.

\( \rightarrow \) THÉORÉME 4 (CHANGEMENT DE VARIABLE). Soit \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{1} \) et \( f : I \subset \mathbb{R} \rightarrow E \) une application continue par morceaux telle que \( \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \subset I \) (où I est un intervalle de \( \mathbb{R} \) ). Alors

> \( \rightarrow \) THEOREM 4 (CHANGE OF VARIABLE). Let \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) map and \( f : I \subset \mathbb{R} \rightarrow E \) be a piecewise continuous map such that \( \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \subset I \) (where I is an interval of \( \mathbb{R} \) ). Then

\[
{\int }_{a}^{b}f\left( {\varphi \left( t\right) }\right) {\varphi }^{\prime }\left( t\right) {dt} = {\int }_{\varphi \left( a\right) }^{\varphi \left( b\right) }f\left( u\right) {du}.
\]

Conséquence : En conjuguant le théorème du changement de variable avec la relation de Chasles, on obtient les résultats qui suivent.

> Consequence: By combining the change of variable theorem with the Chasles relation, we obtain the following results.

- Soit \( f \) une application \( f : \left\lbrack  {-a, a}\right\rbrack   \rightarrow  E \) une continue par morceaux. Si \( f \) est paire, alors \( {\int }_{-a}^{a}f\left( x\right) {dx} = 2{\int }_{0}^{a}f\left( x\right) {dx} \) . Si \( f \) est impaire, alors \( {\int }_{-a}^{a}f\left( x\right) {dx} = 0 \) .

> - Let \( f \) be a \( f : \left\lbrack  {-a, a}\right\rbrack   \rightarrow  E \) piecewise continuous map. If \( f \) is even, then \( {\int }_{-a}^{a}f\left( x\right) {dx} = 2{\int }_{0}^{a}f\left( x\right) {dx} \) . If \( f \) is odd, then \( {\int }_{-a}^{a}f\left( x\right) {dx} = 0 \) .

- Soit \( f : \mathbb{R} \rightarrow  E \) une application continue par morceaux et \( T \) -périodique. Alors

> - Let \( f : \mathbb{R} \rightarrow  E \) be a piecewise continuous and \( T \) -periodic map. Then

\[
\forall a \in  \mathbb{R},\;{\int }_{a}^{a + T}f\left( t\right) {dt} = {\int }_{0}^{T}f\left( t\right) {dt}.
\]

##### First and second mean value theorems.

*Français : Première et seconde formule de la moyenne.*

THÉORÉME 5 (PREMIERE FORMULE DE LA MOYENNE). Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue et \( g : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{ + } \) une fonction continue par morceaux et positive. Alors

> THEOREM 5 (FIRST MEAN VALUE THEOREM). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a continuous function and \( g : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{ + } \) be a piecewise continuous and positive function. Then

\[
\exists c \in  \left\lbrack  {a, b}\right\rbrack  ,\;{\int }_{a}^{b}f\left( x\right) g\left( x\right) {dx} = f\left( c\right) {\int }_{a}^{b}g\left( x\right) {dx}.
\]

Démonstration. Posons \( m = \mathop{\inf }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) et \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) . On a

> Proof. Let \( m = \mathop{\inf }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) and \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) . We have

\[
m{\int }_{a}^{b}g\left( x\right) {dx} \leq  {\int }_{a}^{b}f\left( x\right) g\left( x\right) {dx} \leq  M{\int }_{a}^{b}g\left( x\right) {dx}.
\]

Si \( {\int }_{a}^{b}g = 0 \) , l’inégalité précédente montre que \( {\int }_{a}^{b}{fg} = 0 \) et le résultat est évident. Sinon, on a \( m \leq \left( {{\int }_{a}^{b}{fg}}\right) /\left( {{\int }_{a}^{b}g}\right) \leq M \) et on conclut en appliquant le théorème des valeurs intermédiaires à la fonction continue \( f \) .

> If \( {\int }_{a}^{b}g = 0 \) , the previous inequality shows that \( {\int }_{a}^{b}{fg} = 0 \) and the result is obvious. Otherwise, we have \( m \leq \left( {{\int }_{a}^{b}{fg}}\right) /\left( {{\int }_{a}^{b}g}\right) \leq M \) and we conclude by applying the intermediate value theorem to the continuous function \( f \) .

Remarque 5. Attention, la fonction \( g \) doit être positive.

> Remark 5. Note that the function \( g \) must be positive.

THÉORÉME 6 (SECONDE FORMULE DE LA MOYENNE). Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction positive décroissante de classe \( {\mathcal{C}}^{1} \) et \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue. Alors il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que

> THEOREM 6 (SECOND MEAN VALUE THEOREM). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a positive decreasing function of class \( {\mathcal{C}}^{1} \) and \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a continuous function. Then there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that

\[
{\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} = f\left( a\right) {\int }_{a}^{c}g\left( t\right) {dt}.
\]

Démonstration. L’application \( G : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto {\int }_{a}^{t}g\left( x\right) {dx} \) est de classe \( {\mathcal{C}}^{1} \) donc continue sur \( \left\lbrack {a, b}\right\rbrack \) . Ceci assure l’existence des réels

> Proof. The map \( G : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto {\int }_{a}^{t}g\left( x\right) {dx} \) is of class \( {\mathcal{C}}^{1} \) and therefore continuous on \( \left\lbrack {a, b}\right\rbrack \) . This ensures the existence of the real numbers

\[
m = \mathop{\inf }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}G\left( t\right) \;\text{ et }\;M = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}G\left( t\right) .
\]

Montrons \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \) , ce qui prouvera le résultat en appliquant à \( G \) le théorème des valeurs intermédiaires. En intégrant par parties, on a

> Let us show \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \), which will prove the result by applying the intermediate value theorem to \( G \). Integrating by parts, we have

\[
{\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} = {\left\lbrack  G\left( t\right) f\left( t\right) \right\rbrack  }_{a}^{b} - {\int }_{a}^{b}G\left( t\right) {f}^{\prime }\left( t\right) {dt} = G\left( b\right) f\left( b\right)  - {\int }_{a}^{b}G\left( t\right) {f}^{\prime }\left( t\right) {dt}.
\]

Or \( {mf}\left( b\right) \leq G\left( b\right) f\left( b\right) \leq {Mf}\left( b\right) \) et

> However, \( {mf}\left( b\right) \leq G\left( b\right) f\left( b\right) \leq {Mf}\left( b\right) \) and

\[
m\left( {f\left( a\right)  - f\left( b\right) }\right)  =  - m{\int }_{a}^{b}{f}^{\prime }\left( t\right) {dt} \leq   - {\int }_{a}^{b}G\left( t\right) {f}^{\prime }\left( t\right) {dt} \leq   - M{\int }_{a}^{b}{f}^{\prime }\left( t\right) {dt} = M\left( {f\left( a\right)  - f\left( b\right) }\right) ,
\]

donc finalement \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \) . Ceci prouve le résultat en vertu de la conti-nuité de \( G \) .

> thus finally \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \). This proves the result by virtue of the continuity of \( G \).

Remarque 6. - Cette formule n'est pas au programme des classes préparatoires mais elle peut rendre de précieux services (par exemple pour démontrer la convergence de certaines intégrales semi-convergentes comme \( {\int }_{1}^{+\infty }\sin \left( t\right) /{tdt} \) ; voir également la règle d'Abel formulée dans le théorème 5). Il faut savoir refaire sa démonstration qui est simple.

> Remark 6. - This formula is not in the preparatory classes curriculum, but it can be very useful (for example, to prove the convergence of certain semi-convergent integrals such as \( {\int }_{1}^{+\infty }\sin \left( t\right) /{tdt} \); see also the Abel test formulated in Theorem 5). One must know how to reproduce its proof, which is simple.

- Ce résultat reste vrai si on suppose uniquement \( f \) continue (voir l’exercice 8 page 135), et même si \( f \) et \( g \) sont uniquement supposées Riemann-intégrables.

> - This result remains true if we only assume \( f \) is continuous (see exercise 8 on page 135), and even if \( f \) and \( g \) are only assumed to be Riemann-integrable.
