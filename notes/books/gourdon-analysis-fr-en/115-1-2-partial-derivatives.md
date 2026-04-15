#### 1.2. Partial derivatives

*Français : 1.2. Dérivées partielles*

##### Directional derivative.

*Français : Dérivée selon un vecteur.*

DéFINITION 3. Soient \( E \) et \( F \) deux \( \mathbb{R} \) -e.v.n, \( U \) un ouvert de \( E \) , et \( f : U \subset E \rightarrow F \) une application. Soit \( a \in U \) et \( v \in E \) . Si la fonction à variable réelle \( \varphi : t \mapsto f\left( {a + {tv}}\right) \) est dérivable en \( t = 0, f \) est dite dérivable en a selon le vecteur \( v \) . On note alors

> DEFINITION 3. Let \( E \) and \( F \) be two \( \mathbb{R} \) -n.v.s., \( U \) an open subset of \( E \), and \( f : U \subset E \rightarrow F \) a mapping. Let \( a \in U \) and \( v \in E \) . If the real-variable function \( \varphi : t \mapsto f\left( {a + {tv}}\right) \) is differentiable at \( t = 0, f \) , it is said to be differentiable at a along the vector \( v \) . We then denote

\[
{f}_{v}^{\prime }\left( a\right)  = {\varphi }^{\prime }\left( 0\right)  = \mathop{\lim }\limits_{\substack{{t \rightarrow  0} \\  {t \neq  0} }}\frac{f\left( {a + {tv}}\right)  - f\left( a\right) }{t}.
\]

PROPOSITION 4. Si \( f \) est différentiable en un point a, alors \( f \) admet une dérivée selon tout vecteur en a et on a \( {f}_{v}^{\prime }\left( a\right) = d{f}_{a}\left( v\right) \) pour tout \( v \in E \) .

> PROPOSITION 4. If \( f \) is differentiable at a point a, then \( f \) admits a directional derivative along any vector at a and we have \( {f}_{v}^{\prime }\left( a\right) = d{f}_{a}\left( v\right) \) for all \( v \in E \).

Remarque 4. Attention, la dérivabilité selon tout vecteur en a n'entraîne pas forcément la différentiabilité de \( f \) en a. En fait, cela n’entraîne même pas la continuité en \( a \) (voir l'exercice 1 page 329).

> Remark 4. Caution: differentiability along every vector at a does not necessarily imply the differentiability of \( f \) at a. In fact, it does not even imply continuity at \( a \) (see exercise 1 on page 329).

Dérivées partielles. Nous travaillons maintenant sur \( E = {\mathbb{R}}^{n} \) .

> Partial derivatives. We now work on \( E = {\mathbb{R}}^{n} \).

DÉFINITION 4. Soit une application \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) , où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) et \( F \) un e.v.n. Soit \( a \in U \) et \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) la base canonique de \( {\mathbb{R}}^{n} \) . Si pour \( i \in \{ 1,\ldots , n\} , f \) est dérivable en \( a \) selon \( {e}_{i} \) , on dit que \( f \) admet une dérivée partielle en \( a \) d’indice \( i \) et on note

> DEFINITION 4. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) be a mapping, where \( U \) is an open subset of \( {\mathbb{R}}^{n} \) and \( F \) a normed vector space. Let \( a \in U \) and \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be the canonical basis of \( {\mathbb{R}}^{n} \). If for \( i \in \{ 1,\ldots , n\} , f \) is differentiable at \( a \) along \( {e}_{i} \), we say that \( f \) admits a partial derivative at \( a \) with index \( i \) and we denote

\[
{f}_{{e}_{i}}^{\prime }\left( a\right)  = \frac{\partial f}{\partial {x}_{i}}\left( a\right) .
\]

Remarque 5. - La dérivée partielle \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) \) est aussi la dérivée de l’application partielle \( t \mapsto f\left( {{a}_{1},\ldots ,{a}_{i - 1},{a}_{i} + t,{a}_{i + 1},\ldots ,{a}_{n}}\right) \) en \( t = 0. \)

> Remark 5. - The partial derivative \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) \) is also the derivative of the partial mapping \( t \mapsto f\left( {{a}_{1},\ldots ,{a}_{i - 1},{a}_{i} + t,{a}_{i + 1},\ldots ,{a}_{n}}\right) \) at \( t = 0. \)

- à plus forte raison que dans la remarque précédente, il se peut que toutes les dérivées partielles de \( f \) existent en \( a \) sans que \( f \) soit différentiable en \( a \) , ni même continue en \( a \) (voir cependant le théorème qui suit).

> - Even more so than in the previous remark, it is possible for all partial derivatives of \( f \) to exist at \( a \) without \( f \) being differentiable at \( a \), or even continuous at \( a \) (see, however, the following theorem).

- Si \( f : U \subset  {\mathbb{R}}^{n} \rightarrow  \mathbb{R} \) est une application différentiable en \( a \in  U \) , alors \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) \) existe pour tout \( i \) , et on a

> - If \( f : U \subset  {\mathbb{R}}^{n} \rightarrow  \mathbb{R} \) is a differentiable mapping at \( a \in  U \) , then \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) \) exists for all \( i \) , and we have

\[
d{f}_{a} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( a\right) d{x}_{i},\;{\operatorname{grad}}_{a}f = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( a\right) {e}_{i},
\]

où \( \left( {d{x}_{i}}\right) \) est la base duale dans \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) de la base canonique de \( {\mathbb{R}}^{n} \) (conséquence de la proposition 4) — \( {\mathbb{R}}^{n} \) est muni de son produit scalaire standard.

> where \( \left( {d{x}_{i}}\right) \) is the dual basis in \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) of the canonical basis of \( {\mathbb{R}}^{n} \) (consequence of proposition 4) — \( {\mathbb{R}}^{n} \) is equipped with its standard inner product.

\( \rightarrow \) THÉORÉME 1. Soit \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) une application, où \( U \) et un ouvert de \( {\mathbb{R}}^{n} \) et \( F \) un e.v.n. Si toutes les dérivées partielles de \( f \) sur U existent et si elles sont continues en un point a de \( U \) , alors \( f \) est différentiable en a et on a

> \( \rightarrow \) THEOREM 1. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) be a mapping, where \( U \) is an open subset of \( {\mathbb{R}}^{n} \) and \( F \) is a n.v.s. If all partial derivatives of \( f \) on U exist and are continuous at a point a in \( U \) , then \( f \) is differentiable at a and we have

\[
d{f}_{a} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( a\right) d{x}_{i}.
\]

Démonstration. On choisit sur \( {\mathbb{R}}^{n} \) la norme \( \parallel x\parallel = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right| \) . Il s’agit de montrer que l’application \( g : x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto f\left( x\right) - \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \) vérifie \( g\left( x\right) - g\left( a\right) = o\left( {\parallel x - a\parallel }\right) \) au voisinage de \( a. \)

> Proof. We choose the norm \( \parallel x\parallel = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right| \) on \( {\mathbb{R}}^{n} \) . We must show that the mapping \( g : x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto f\left( x\right) - \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \) satisfies \( g\left( x\right) - g\left( a\right) = o\left( {\parallel x - a\parallel }\right) \) in the neighborhood of \( a. \)

Soit \( \varepsilon > 0 \) . Par hypothèse, les dérivées partielles de \( f \) sont continues en \( a \) , donc

> Let \( \varepsilon > 0 \) . By hypothesis, the partial derivatives of \( f \) are continuous at \( a \) , so

\[
\exists \alpha  > 0,\forall x \in  U,\parallel a - x\parallel  < \alpha ,\forall i \in  \{ 1,\ldots , n\} ,\;\begin{Vmatrix}{\frac{\partial g}{\partial {x}_{i}}\left( x\right) }\end{Vmatrix} = \begin{Vmatrix}{\frac{\partial f}{\partial {x}_{i}}\left( x\right)  - \frac{\partial f}{\partial {x}_{i}}\left( a\right) }\end{Vmatrix} < \varepsilon .
\]

Quitte à diminuer \( \alpha > 0 \) , on peut supposer que \( \mathrm{B}\left( {a,\alpha }\right) \subset U \) .

> By potentially shrinking \( \alpha > 0 \) , we may assume that \( \mathrm{B}\left( {a,\alpha }\right) \subset U \) .

Soit \( x \in \mathrm{B}\left( {a,\alpha }\right) \) . On considère les points

> Let \( x \in \mathrm{B}\left( {a,\alpha }\right) \) . We consider the points

\[
{y}_{0} = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \;\text{ et }\;\forall k \in  \{ 1,\ldots , n\} ,\;{y}_{k} = \left( {{x}_{1},\ldots ,{x}_{k},{a}_{k + 1},\ldots ,{a}_{n}}\right) ,
\]

de sorte que \( {y}_{0} = a \) et \( {y}_{n} = x \) . Pour tout \( k \in \{ 1,\ldots , n\} \) , la fonction

> such that \( {y}_{0} = a \) and \( {y}_{n} = x \) . For all \( k \in \{ 1,\ldots , n\} \) , the function

\[
{g}_{k} : \left\lbrack  {{a}_{k},{x}_{k}}\right\rbrack   \rightarrow  F\;t \mapsto  g\left( {{x}_{1},\ldots ,{x}_{k - 1}, t,{a}_{k + 1},\ldots ,{a}_{n}}\right)
\]

\( \left( {\left\lbrack {{a}_{k},{x}_{k}}\right\rbrack \text{ désigne l’intervalle }\left\lbrack {{x}_{k},{a}_{k}}\right\rbrack \text{ si }{x}_{k} < {a}_{k}}\right) \) vérifie

> \( \left( {\left\lbrack {{a}_{k},{x}_{k}}\right\rbrack \text{ désigne l’intervalle }\left\lbrack {{x}_{k},{a}_{k}}\right\rbrack \text{ si }{x}_{k} < {a}_{k}}\right) \) satisfies

\[
{g}_{k}^{\prime }\left( t\right)  = \frac{\partial g}{\partial {x}_{k}}\left( {{x}_{1},\ldots ,{x}_{k - 1}, t,{a}_{k + 1},\ldots ,{a}_{n}}\right) ,
\]

donc \( \begin{Vmatrix}{{g}_{k}^{\prime }\left( t\right) }\end{Vmatrix} < \varepsilon \) sur \( \left\lbrack {{a}_{k},{x}_{k}}\right\rbrack \) . On en déduit, avec le théorème 5 page 75, que \( \begin{Vmatrix}{{g}_{k}\left( {x}_{k}\right) - {g}_{k}\left( {a}_{k}\right) }\end{Vmatrix} \leq \; \varepsilon \left| {{x}_{k} - {a}_{k}}\right| \) . Comme \( {g}_{k}\left( {a}_{k}\right) = g\left( {y}_{k - 1}\right) \) et \( {g}_{k}\left( {x}_{k}\right) = g\left( {y}_{k}\right) \) , ceci entraîne

> thus \( \begin{Vmatrix}{{g}_{k}^{\prime }\left( t\right) }\end{Vmatrix} < \varepsilon \) on \( \left\lbrack {{a}_{k},{x}_{k}}\right\rbrack \) . We deduce from this, with theorem 5 on page 75, that \( \begin{Vmatrix}{{g}_{k}\left( {x}_{k}\right) - {g}_{k}\left( {a}_{k}\right) }\end{Vmatrix} \leq \; \varepsilon \left| {{x}_{k} - {a}_{k}}\right| \) . Since \( {g}_{k}\left( {a}_{k}\right) = g\left( {y}_{k - 1}\right) \) and \( {g}_{k}\left( {x}_{k}\right) = g\left( {y}_{k}\right) \) , this implies

\[
\parallel g\left( x\right)  - g\left( a\right) \parallel  = \begin{Vmatrix}{\mathop{\sum }\limits_{{k = 1}}^{n}\left\lbrack  {g\left( {y}_{k}\right)  - g\left( {y}_{k - 1}\right) }\right\rbrack  }\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\begin{Vmatrix}{g\left( {y}_{k}\right)  - g\left( {y}_{k - 1}\right) }\end{Vmatrix} \leq  \varepsilon \left( {\mathop{\sum }\limits_{{k = 1}}^{n}\left| {{x}_{k} - {a}_{k}}\right| }\right)  = \varepsilon \parallel x - a\parallel .
\]

On a donc bien \( g\left( x\right) - g\left( a\right) = o\left( {\parallel x - a\parallel }\right) \) au voisinage de \( a \) , d’où le résultat.

> We therefore have \( g\left( x\right) - g\left( a\right) = o\left( {\parallel x - a\parallel }\right) \) in the neighborhood of \( a \) , hence the result.

Remarque 6. Attention, la réciproque est fausse. Par exemple, l’application \( f : \mathbb{R} \rightarrow \mathbb{R} \) définie par \( f\left( x\right) = {x}^{2}\sin \left( {1/x}\right) \) si \( x \neq 0, f\left( 0\right) = 0 \) , est différentiable en 0 mais \( {f}^{\prime } \) n’est pas continue en 0.

> Remark 6. Caution, the converse is false. For example, the mapping \( f : \mathbb{R} \rightarrow \mathbb{R} \) defined by \( f\left( x\right) = {x}^{2}\sin \left( {1/x}\right) \) if \( x \neq 0, f\left( 0\right) = 0 \) , is differentiable at 0 but \( {f}^{\prime } \) is not continuous at 0.

Dérivées partielles d'ordre supérieur. Sous réserve d'existence, on peut définir par récurrence sur \( p \) une dérivée partielle d’ordre \( p \) par la relation

> Higher-order partial derivatives. Subject to their existence, one can define by induction on \( p \) a partial derivative of order \( p \) by the relation

\[
\frac{{\partial }^{p}f}{\partial {x}_{{i}_{p}}\cdots \partial {x}_{{i}_{1}}} = \frac{\partial }{\partial {x}_{{i}_{p}}}\left( \frac{{\partial }^{p - 1}f}{\partial {x}_{{i}_{p - 1}}\cdots \partial {x}_{{i}_{1}}}\right) .
\]

Une fonction \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) est dite de classe \( {\mathcal{C}}^{p} \) si toutes ses dérivées partielles jusqu’à l’ordre \( p \) existent et sont continues sur \( U \) . Le théorème 1 assure la cohérence de cette définition avec la définition 1 pour le cas \( {\mathcal{C}}^{1} \) .

> A function \( f : U \subset {\mathbb{R}}^{n} \rightarrow F \) is said to be of class \( {\mathcal{C}}^{p} \) if all its partial derivatives up to order \( p \) exist and are continuous on \( U \) . Theorem 1 ensures the consistency of this definition with definition 1 for the case \( {\mathcal{C}}^{1} \) .

\( \rightarrow \) THÉORÉME 2 (SCHWARZ). Soit une application \( f : U \subset {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) , où \( U \) est un ouvert de \( {\mathbb{R}}^{2} \) , telle que \( f \) admette des dérivées partielles \( {\partial }^{2}f/\partial x\partial y \) et \( {\partial }^{2}f/\partial y\partial x \) sur \( U \) , continues en un point a de U. Alors

> \( \rightarrow \) THEOREM 2 (SCHWARZ). Let a mapping \( f : U \subset {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) , where \( U \) is an open subset of \( {\mathbb{R}}^{2} \) , such that \( f \) admits partial derivatives \( {\partial }^{2}f/\partial x\partial y \) and \( {\partial }^{2}f/\partial y\partial x \) on \( U \) , continuous at a point a in U. Then

\[
\frac{{\partial }^{2}f}{\partial x\partial y}\left( a\right)  = \frac{{\partial }^{2}f}{\partial y\partial x}\left( a\right) .
\]

Démonstration. Soient \( {x}_{0},{y}_{0} \) les coordonnées de \( a \) . Soient \( h > 0 \) et \( k > 0 \) tels que \( \left\lbrack {{x}_{0},{x}_{0} + h}\right\rbrack \times \; \left\lbrack {{y}_{0},{y}_{0} + k}\right\rbrack \subset U \) . On pose

> Proof. Let \( {x}_{0},{y}_{0} \) be the coordinates of \( a \) . Let \( h > 0 \) and \( k > 0 \) be such that \( \left\lbrack {{x}_{0},{x}_{0} + h}\right\rbrack \times \; \left\lbrack {{y}_{0},{y}_{0} + k}\right\rbrack \subset U \) . We set

\[
\delta \left( {h, k}\right)  = f\left( {{x}_{0} + h,{y}_{0} + k}\right)  - f\left( {{x}_{0} + h,{y}_{0}}\right)  - f\left( {{x}_{0},{y}_{0} + k}\right)  + f\left( {{x}_{0},{y}_{0}}\right) .
\]

Si on pose \( \varphi : x \mapsto f\left( {x,{y}_{0} + k}\right) - f\left( {x,{y}_{0}}\right) \) , on a \( \delta \left( {h, k}\right) = \varphi \left( {{x}_{0} + h}\right) - \varphi \left( {x}_{0}\right) \) , et la fonction \( \varphi \) étant dérivable sur \( \left\lbrack {{x}_{0},{x}_{0} + h}\right\rbrack \) , le théorème des accroissements finis assure l’existence de \( {\theta }_{1} \in \rbrack 0,1\left\lbrack \right. \) tel que \( \delta \left( {h, k}\right) = h{\varphi }^{\prime }\left( {{x}_{0} + {\theta }_{1}h}\right) \) , ce qui s’écrit encore

> If we set \( \varphi : x \mapsto f\left( {x,{y}_{0} + k}\right) - f\left( {x,{y}_{0}}\right) \) , we have \( \delta \left( {h, k}\right) = \varphi \left( {{x}_{0} + h}\right) - \varphi \left( {x}_{0}\right) \) , and the function \( \varphi \) being differentiable on \( \left\lbrack {{x}_{0},{x}_{0} + h}\right\rbrack \) , the mean value theorem ensures the existence of \( {\theta }_{1} \in \rbrack 0,1\left\lbrack \right. \) such that \( \delta \left( {h, k}\right) = h{\varphi }^{\prime }\left( {{x}_{0} + {\theta }_{1}h}\right) \) , which can also be written

\[
\delta \left( {h, k}\right)  = h\left\lbrack  {\frac{\partial f}{\partial x}\left( {{x}_{0} + {\theta }_{1}h,{y}_{0} + k}\right)  - \frac{\partial f}{\partial x}\left( {{x}_{0} + {\theta }_{1}h,{y}_{0}}\right) }\right\rbrack  .
\]

Maintenant, l’application \( y \mapsto \frac{\partial f}{\partial x}\left( {{x}_{0} + {\theta }_{1}h, y}\right) \) étant dérivable sur \( \left\lbrack {{y}_{0},{y}_{0} + k}\right\rbrack \) , une nouvelle application du théorème des accroissements finis donne l’existence de \( {\theta }_{2} \in \rbrack 0,1\lbrack \) tel que

> Now, the mapping \( y \mapsto \frac{\partial f}{\partial x}\left( {{x}_{0} + {\theta }_{1}h, y}\right) \) being differentiable on \( \left\lbrack {{y}_{0},{y}_{0} + k}\right\rbrack \) , a new application of the mean value theorem gives the existence of \( {\theta }_{2} \in \rbrack 0,1\lbrack \) such that

\[
\delta \left( {h, k}\right)  = {hk}\frac{{\partial }^{2}f}{\partial y\partial x}\left( {{x}_{0} + {\theta }_{1}h,{y}_{0} + {\theta }_{2}k}\right) .
\]

(*)

> En travaillant à partir de la fonction \( \psi : y \mapsto f\left( {{x}_{0} + h, y}\right) - f\left( {{x}_{0}, y}\right) \) , on montrerait de même l’existence de \( {\theta }_{3},{\theta }_{4} \in \rbrack 0,1\lbrack \) tels que

By working from the function \( \psi : y \mapsto f\left( {{x}_{0} + h, y}\right) - f\left( {{x}_{0}, y}\right) \) , we would similarly show the existence of \( {\theta }_{3},{\theta }_{4} \in \rbrack 0,1\lbrack \) such that

\[
\delta \left( {h, k}\right)  = {hk}\frac{{\partial }^{2}f}{\partial x\partial y}\left( {{x}_{0} + {\theta }_{3}h,{y}_{0} + {\theta }_{4}k}\right) .
\]

(**)

> En égalant (*) et (**) et en faisant tendre \( h \) et \( k \) vers 0, on en déduit en vertu de la continuité des dérivées partielles \( \frac{{\partial }^{2}f}{\partial x\partial y} \) et \( \frac{{\partial }^{2}f}{\partial y\partial x} \) en a, l’égalité de ces dernières au point \( a \) .

By equating (*) and (**) and letting \( h \) and \( k \) tend to 0, we deduce, by virtue of the continuity of the partial derivatives \( \frac{{\partial }^{2}f}{\partial x\partial y} \) and \( \frac{{\partial }^{2}f}{\partial y\partial x} \) at a, the equality of the latter at point \( a \) .

> Remarque 7. Sans la condition de continuité en a des dérivées partielles d'ordre 2, ce résultat est faux (voir l'exercice 1 page 329 pour un contre-exemple).

Remark 7. Without the condition of continuity at a of the second-order partial derivatives, this result is false (see exercise 1 on page 329 for a counterexample).

> COROLLAIRE 1. Si \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{m} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) ) est une application de classe \( {\mathcal{C}}^{p} \) , alors les dérivées partielles jusqu’à l’ordre p ne dépendent pas de l’ordre de dérivation. On peut donc les écrire toutes sous la forme

COROLLARY 1. If \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{m} \) (where \( U \) is an open set of \( {\mathbb{R}}^{n} \) ) is a class \( {\mathcal{C}}^{p} \) mapping, then the partial derivatives up to order p do not depend on the order of differentiation. They can therefore all be written in the form

\[
\frac{{\partial }^{q}f}{\partial {x}_{1}^{{i}_{1}}\partial {x}_{2}^{{i}_{2}}\cdots \partial {x}_{n}^{{i}_{n}}}\;\text{ où }\;{i}_{1} + {i}_{2} + \cdots  + {i}_{n} = q \leq  p.
\]

Matrice jacobienne, jacobien. On se donne une fonction \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{m} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) ), différentiable en un point \( a \) de \( U \) , et on désigne par \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) et \( \left( {{e}_{1}^{\prime },\ldots ,{e}_{m}^{\prime }}\right) \) les bases canoniques de \( {\mathbb{R}}^{n} \) et \( {\mathbb{R}}^{m} \) .

> Jacobian matrix, Jacobian. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{m} \) be a function (where \( U \) is an open set of \( {\mathbb{R}}^{n} \) ), differentiable at a point \( a \) of \( U \) , and let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) and \( \left( {{e}_{1}^{\prime },\ldots ,{e}_{m}^{\prime }}\right) \) denote the canonical bases of \( {\mathbb{R}}^{n} \) and \( {\mathbb{R}}^{m} \) .

On peut écrire \( f \) sous la forme \( f = \mathop{\sum }\limits_{{i = 1}}^{m}{f}_{i}{e}_{i}^{\prime } \) où pour tout \( i,{f}_{i} : U \rightarrow \mathbb{R} \) est une application différentiable en \( a \) , de sorte que

> We can write \( f \) in the form \( f = \mathop{\sum }\limits_{{i = 1}}^{m}{f}_{i}{e}_{i}^{\prime } \) where for all \( i,{f}_{i} : U \rightarrow \mathbb{R} \) is a differentiable mapping at \( a \) , such that

\[
\forall j \in  \{ 1,\ldots , n\} ,\;d{f}_{a}\left( {e}_{j}\right)  = \mathop{\sum }\limits_{{i = 1}}^{m}d{f}_{i, a}\left( {e}_{j}\right) {e}_{i}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{m}\frac{\partial {f}_{i}}{\partial {x}_{j}}\left( a\right) {e}_{i}^{\prime }.
\]

La matrice de \( d{f}_{a} \) dans les bases canoniques de \( {\mathbb{R}}^{n} \) et \( {\mathbb{R}}^{m} \) est

> The matrix of \( d{f}_{a} \) in the canonical bases of \( {\mathbb{R}}^{n} \) and \( {\mathbb{R}}^{m} \) is

\[
{J}_{a} = {\left\lbrack  \frac{\partial {f}_{i}}{\partial {x}_{j}}\left( a\right) \right\rbrack  }_{\begin{matrix} {1 \leq  i \leq  m} \\  {1 \leq  j \leq  n} \end{matrix}} \in  {\mathcal{M}}_{m, n}\left( \mathbb{R}\right) .
\]

On l’appelle matrice jacobienne de \( f \) en a. Lorsque \( m = n,{J}_{a} \) est une matrice carrée et son déterminant est appelé jacobien de \( f \) en \( a \) .

> It is called the Jacobian matrix of \( f \) at a. When \( m = n,{J}_{a} \) is a square matrix, its determinant is called the Jacobian of \( f \) at \( a \) .

Rappelons que la différentielle de la composée de deux fonctions différentiables est la composée des différentielles ; la matrice jacobienne de la composée est donc le produit des matrices jacobiennes. On en déduit en particulier le résultat qui suit :

> Recall that the differential of the composition of two differentiable functions is the composition of the differentials; the Jacobian matrix of the composition is therefore the product of the Jacobian matrices. We deduce in particular the following result:

\( \rightarrow \) Proposition 5. Soient deux applications \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) et \( \varphi : V \subset {\mathbb{R}}^{m} \rightarrow {\mathbb{R}}^{n} \) (où \( U \) et \( V \) sont ouverts) telles que \( \varphi \left( V\right) \subset U \) . On écrit \( \varphi \) sous la forme \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) où \( {\varphi }_{i} : V \rightarrow \mathbb{R} \) pour tout i. Soit a \( \in V \) tel que \( \varphi \) est différentiable en a et \( f \) est différentiable en \( \varphi \left( a\right) \) . Alors l’application \( F = f \circ \varphi : V \rightarrow \mathbb{R} \) est différentiable en a et

> \( \rightarrow \) Proposition 5. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) and \( \varphi : V \subset {\mathbb{R}}^{m} \rightarrow {\mathbb{R}}^{n} \) be two mappings (where \( U \) and \( V \) are open sets) such that \( \varphi \left( V\right) \subset U \) . We write \( \varphi \) in the form \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) where \( {\varphi }_{i} : V \rightarrow \mathbb{R} \) for all i. Let a \( \in V \) such that \( \varphi \) is differentiable at a and \( f \) is differentiable at \( \varphi \left( a\right) \) . Then the mapping \( F = f \circ \varphi : V \rightarrow \mathbb{R} \) is differentiable at a and

\[
\forall j \in  \{ 1,\ldots , m\} ,\;\frac{\partial F}{\partial {u}_{j}}\left( a\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( {\varphi \left( a\right) }\right)  \cdot  \frac{\partial {\varphi }_{i}}{\partial {u}_{j}}\left( a\right) .
\]

Conséquence : En dimension finie, la composée de deux fonctions de classe \( {\mathcal{C}}^{p} \) est de classe \( {\mathcal{C}}^{p} \) . En particulier la somme, le produit (pour des fonctions à valeurs réelles) de fonctions \( {\mathcal{C}}^{p} \) est \( {\mathcal{C}}^{p} \) .

> Consequence: In finite dimension, the composition of two \( {\mathcal{C}}^{p} \) functions is \( {\mathcal{C}}^{p} \). In particular, the sum and product (for real-valued functions) of \( {\mathcal{C}}^{p} \) functions are \( {\mathcal{C}}^{p} \).

Remarque 8. - En particulier, si \( \varphi \) est une fonction d’une seule variable réelle, la formule de la proposition précédente s'écrit

> Remark 8. - In particular, if \( \varphi \) is a function of a single real variable, the formula of the previous proposition is written

\[
{F}^{\prime }\left( a\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( {\varphi \left( a\right) }\right)  \cdot  {\varphi }_{i}^{\prime }\left( a\right) .
\]

- Il est important de bien maîtriser la formule de la proposition précédente. Vous pourrez vous entraîner à montrer que si \( f : {\mathbb{R}}^{2} \rightarrow  \mathbb{R} \) est une fonction de classe \( {\mathcal{C}}^{2} \) et si \( \varphi  : {\mathbb{R}}^{ * } \times  \mathbb{R} \rightarrow  {\mathbb{R}}^{2}\;\left( {r,\theta }\right)  \mapsto  \left( {r\cos \theta , r\sin \theta }\right) \) , l’application \( F = f \circ  \varphi \) (qui est l’expression de \( f \) en coordonnées polaires) est de classe \( {\mathcal{C}}^{2} \) et le laplacien de \( f \) vérifie

> - It is important to master the formula of the previous proposition. You can practice showing that if \( f : {\mathbb{R}}^{2} \rightarrow  \mathbb{R} \) is a \( {\mathcal{C}}^{2} \) function and if \( \varphi  : {\mathbb{R}}^{ * } \times  \mathbb{R} \rightarrow  {\mathbb{R}}^{2}\;\left( {r,\theta }\right)  \mapsto  \left( {r\cos \theta , r\sin \theta }\right) \), the mapping \( F = f \circ  \varphi \) (which is the expression of \( f \) in polar coordinates) is \( {\mathcal{C}}^{2} \) and the Laplacian of \( f \) satisfies

\[
{\Delta f} = \frac{{\partial }^{2}f}{\partial {x}^{2}} + \frac{{\partial }^{2}f}{\partial {y}^{2}} = \frac{{\partial }^{2}F}{\partial {r}^{2}} + \frac{1}{r}\frac{\partial F}{\partial r} + \frac{1}{{r}^{2}}\frac{{\partial }^{2}F}{\partial {\theta }^{2}}.
\]
