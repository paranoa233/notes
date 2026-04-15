#### 1.2. Cauchy problem, Cauchy-Lipschitz theorem

*Français : 1.2. Problème de Cauchy, théorème de Cauchy-Lipschitz*

Problème de Cauchy. On se donne une équation différentielle

> Cauchy problem. We are given a differential equation

\[
{y}^{\left( n\right) } = F\left( {t, y,{y}^{\prime },\ldots ,{y}^{\left( n - 1\right) }}\right)
\]

\( \left( *\right) \)

> et \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \in \Omega \) . On appelle problème de Cauchy de (*) en \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \) la recherche d’une fonction \( \varphi : I \rightarrow E \) (où \( I \) est un intervalle de \( \mathbb{R} \) ) solution de (*) et vérifiant \( {t}_{0} \in I,\varphi \left( {t}_{0}\right) = {x}_{0},\ldots ,{\varphi }^{\left( n - 1\right) }\left( {t}_{0}\right) = {x}_{n - 1} \) .

and \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \in \Omega \) . We call the Cauchy problem for (*) at \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \) the search for a function \( \varphi : I \rightarrow E \) (where \( I \) is an interval of \( \mathbb{R} \) ) that is a solution to (*) and satisfies \( {t}_{0} \in I,\varphi \left( {t}_{0}\right) = {x}_{0},\ldots ,{\varphi }^{\left( n - 1\right) }\left( {t}_{0}\right) = {x}_{n - 1} \) .

> On dit qu’il y a unicité au problème de Cauchy (*) en \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \) s’il existe au moins une solution à ce problème de Cauchy et si pour toutes solutions \( \varphi : I \rightarrow E \) et \( \psi : J \rightarrow E \) à ce problème, les fonctions \( \varphi \) et \( \psi \) coïncident sur \( I \cap J \) .

We say that there is uniqueness for the Cauchy problem (*) at \( \left( {{t}_{0},{x}_{0},\ldots ,{x}_{n - 1}}\right) \) if there exists at least one solution to this Cauchy problem and if for any solutions \( \varphi : I \rightarrow E \) and \( \psi : J \rightarrow E \) to this problem, the functions \( \varphi \) and \( \psi \) coincide on \( I \cap J \) .

> Lorsque la fonction \( F \) vérifient certaines hypothèses, on peut assurer l’unicité au problème de Cauchy. Rappelons que l'on peut se limiter à l'étude des équations différen-tielles du premier ordre.

When the function \( F \) satisfies certain hypotheses, we can guarantee uniqueness for the Cauchy problem. Recall that we can limit ourselves to the study of first-order differential equations.

> Existence et unicité locale d'une solution : théorème de Cauchy-Lipschitz. Rappel. On dit qu’une application \( F \) d’un ouvert \( \Omega \) de \( \mathbb{R} \times {\mathbb{R}}^{n} \) est localement lipschitzienne en la seconde variable si pour tout \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , il existe un voisinage \( V \) de \( \left( {{t}_{0},{x}_{0}}\right) \) et \( k > 0 \) tels que

Local existence and uniqueness of a solution: Cauchy-Lipschitz theorem. Reminder. We say that a mapping \( F \) from an open set \( \Omega \) of \( \mathbb{R} \times {\mathbb{R}}^{n} \) is locally Lipschitz in the second variable if for all \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , there exists a neighborhood \( V \) of \( \left( {{t}_{0},{x}_{0}}\right) \) and \( k > 0 \) such that

\[
\forall t \in  \mathbb{R},\forall x,{x}^{\prime } \in  {\mathbb{R}}^{n},\left( {t, x}\right)  \in  V,\left( {t,{x}^{\prime }}\right)  \in  V,\;\begin{Vmatrix}{F\left( {t, x}\right)  - F\left( {t,{x}^{\prime }}\right) }\end{Vmatrix} \leq  k\begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix}.
\]

\( \rightarrow \) THÉORÉME 1 (CAUCHY-LIPSCHITZ). Soit \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( \Omega \) est un ouvert de \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) une fonction continue et localement lipschitzienne en la seconde variable. Alors pour tout \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , il existe un intervalle \( I \) voisinage de \( {t}_{0} \) dans \( \mathbb{R} \) et une application \( \varphi : I \rightarrow {\mathbb{R}}^{n} \) solution de \( {y}^{\prime } = F\left( {t, y}\right) \) telle que \( \varphi \left( {t}_{0}\right) = {x}_{0} \) . De plus, il y a unicité pour le problème de Cauchy de cette équation différentielle en \( \left( {{t}_{0},{x}_{0}}\right) \) .

> \( \rightarrow \) THEOREM 1 (CAUCHY-LIPSCHITZ). Let \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( \Omega \) is an open subset of \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) be a continuous function that is locally Lipschitz in the second variable. Then for any \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , there exists an interval \( I \) , a neighborhood of \( {t}_{0} \) in \( \mathbb{R} \) , and a mapping \( \varphi : I \rightarrow {\mathbb{R}}^{n} \) that is a solution to \( {y}^{\prime } = F\left( {t, y}\right) \) such that \( \varphi \left( {t}_{0}\right) = {x}_{0} \) . Furthermore, there is uniqueness for the Cauchy problem of this differential equation at \( \left( {{t}_{0},{x}_{0}}\right) \) .

Démonstration. Existence. Nous aurons besoin de la notion de cylindre de sécurité. Un point \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) est fixé. Pour tout \( r > 0 \) , on pose \( {\mathrm{B}}_{r} = \left\{ {x \in {\mathbb{R}}^{n} \mid \begin{Vmatrix}{x - {x}_{0}}\end{Vmatrix} \leq r}\right\} \) et pour tout \( \alpha > 0,{I}_{\alpha } = \rbrack {t}_{0} - \alpha ,{t}_{0} + \alpha \left\lbrack \right. \) . Soit \( V \) un voisinage compact de \( \left( {{t}_{0},{x}_{0}}\right) \) dans \( \Omega \) sur lequel \( F \) est \( k \) -lipschitzienne en la seconde variable (la compacité de \( V \) est une commodité pour que \( F \) soit bornée sur \( V \) , mais même en dimension infinie, comme \( F \) est continue en \( \left( {{t}_{0},{x}_{0}}\right) \) , on peut choisir \( V \) telle que \( F \) soit bornée sur \( V \) ). Notons \( M \) un majorant de \( F \) sur \( V \) . On peut choisir \( r > 0 \) et \( \alpha > 0 \) , désormais fixés, tels que \( {I}_{\alpha } \times {B}_{r} \subset V \) et \( {\alpha M} < r \) (on dit que \( {I}_{\alpha } \times {B}_{r} \) est un cylindre de sécurité pour \( F \) en \( \left( {{t}_{0},{x}_{0}}\right) \) ).

> Proof. Existence. We will need the concept of a safety cylinder. A point \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) is fixed. For any \( r > 0 \) , we set \( {\mathrm{B}}_{r} = \left\{ {x \in {\mathbb{R}}^{n} \mid \begin{Vmatrix}{x - {x}_{0}}\end{Vmatrix} \leq r}\right\} \) and for any \( \alpha > 0,{I}_{\alpha } = \rbrack {t}_{0} - \alpha ,{t}_{0} + \alpha \left\lbrack \right. \) . Let \( V \) be a compact neighborhood of \( \left( {{t}_{0},{x}_{0}}\right) \) in \( \Omega \) on which \( F \) is \( k \) -Lipschitz in the second variable (the compactness of \( V \) is a convenience so that \( F \) is bounded on \( V \) , but even in infinite dimension, since \( F \) is continuous at \( \left( {{t}_{0},{x}_{0}}\right) \) , we can choose \( V \) such that \( F \) is bounded on \( V \) ). Let \( M \) denote an upper bound of \( F \) on \( V \) . We can choose \( r > 0 \) and \( \alpha > 0 \) , now fixed, such that \( {I}_{\alpha } \times {B}_{r} \subset V \) and \( {\alpha M} < r \) (we say that \( {I}_{\alpha } \times {B}_{r} \) is a safety cylinder for \( F \) at \( \left( {{t}_{0},{x}_{0}}\right) \) ).

La fonction \( F \) est continue, toute solution est donc de classe \( {\mathcal{C}}^{1} \) . Ainsi, une application \( \varphi : {I}_{\alpha } \rightarrow {\mathbb{R}}^{n} \) est solution si et seulement si pour tout \( t \in I,\left( {t,\varphi \left( t\right) }\right) \in \Omega \) et \( \varphi \left( t\right) = {x}_{0} + \; {\int }_{{t}_{0}}^{t}F\left( {u,\varphi \left( u\right) }\right) {du}. \)

> The function \( F \) is continuous, so any solution is of class \( {\mathcal{C}}^{1} \) . Thus, a mapping \( \varphi : {I}_{\alpha } \rightarrow {\mathbb{R}}^{n} \) is a solution if and only if for all \( t \in I,\left( {t,\varphi \left( t\right) }\right) \in \Omega \) and \( \varphi \left( t\right) = {x}_{0} + \; {\int }_{{t}_{0}}^{t}F\left( {u,\varphi \left( u\right) }\right) {du}. \)

Notons \( \Gamma \) l’ensemble des fonctions continues \( \psi : {I}_{\alpha } \rightarrow {\mathbb{R}}^{n} \) telles que \( \psi \left( {I}_{\alpha }\right) \subset {B}_{r} \) . Pour tout \( \psi \in \Gamma \) , l’application

> Let \( \Gamma \) denote the set of continuous functions \( \psi : {I}_{\alpha } \rightarrow {\mathbb{R}}^{n} \) such that \( \psi \left( {I}_{\alpha }\right) \subset {B}_{r} \) . For any \( \psi \in \Gamma \) , the mapping

\[
\widetilde{\psi } : {I}_{\alpha } \rightarrow  {\mathbb{R}}^{n}\;t \mapsto  {x}_{0} + {\int }_{{t}_{0}}^{t}F\left( {u,\psi \left( u\right) }\right) {du}
\]

(*)

> vérifie

satisfies

\[
\forall t \in  {I}_{\alpha },\;\begin{Vmatrix}{\widetilde{\psi }\left( t\right)  - {x}_{0}}\end{Vmatrix} \leq  \left| {{\int }_{{t}_{0}}^{t}\parallel F\left( {u,\psi \left( u\right) }\right) \parallel {du}}\right|  \leq  {\alpha M} < r,
\]

donc \( \widetilde{\psi } \in \Gamma \) . On est donc autorisé (et c’est là l’utilité du cylindre de sécurité) à définir la suite de fonctions \( \left( {\psi }_{n}\right) \) par

> so \( \widetilde{\psi } \in \Gamma \) . We are therefore authorized (and this is the utility of the safety cylinder) to define the sequence of functions \( \left( {\psi }_{n}\right) \) by

\[
{\psi }_{0} : {I}_{\alpha } \rightarrow  {\mathbb{R}}^{n}\;t \mapsto  {x}_{0}\;\text{ et }\;\forall n \in  \mathbb{N},\;{\psi }_{n + 1} = {\widetilde{\psi }}_{n}.
\]

Montrons que pour tout \( t \in {I}_{\alpha } \) et pour tout \( n \in \mathbb{N},\begin{Vmatrix}{{\psi }_{n + 1}\left( t\right) - {\psi }_{n}\left( t\right) }\end{Vmatrix} \leq r{k}^{n}{\left| t - {t}_{0}\right| }^{n}/n \) !. Pour \( n = 0 \) , c’est immédiat d’après (*). Pour passer du rang \( n - 1 \) au rang \( n \) , il suffit d’écrire, pour tout \( t \in {I}_{\alpha } \) ,

> Let us show that for all \( t \in {I}_{\alpha } \) and for all \( n \in \mathbb{N},\begin{Vmatrix}{{\psi }_{n + 1}\left( t\right) - {\psi }_{n}\left( t\right) }\end{Vmatrix} \leq r{k}^{n}{\left| t - {t}_{0}\right| }^{n}/n \) !. For \( n = 0 \) , it is immediate from (*). To move from rank \( n - 1 \) to rank \( n \) , it suffices to write, for all \( t \in {I}_{\alpha } \) ,

\[
\begin{Vmatrix}{{\psi }_{n + 1}\left( t\right)  - {\psi }_{n}\left( t\right) }\end{Vmatrix} \leq  \left| {{\int }_{{t}_{0}}^{t}\begin{Vmatrix}{F\left( {u,{\psi }_{n}\left( u\right) }\right)  - F\left( {u,{\psi }_{n - 1}\left( u\right) }\right) }\end{Vmatrix}{du}}\right|  \leq  \left| {{\int }_{{t}_{0}}^{t}k\begin{Vmatrix}{{\psi }_{n}\left( u\right)  - {\psi }_{n - 1}\left( u\right) }\end{Vmatrix}{du}}\right|
\]

\[
\leq  r\frac{{k}^{n}}{\left( {n - 1}\right) !}\left| {{\int }_{{t}_{0}}^{t}{\left| t - {t}_{0}\right| }^{n - 1}{dt}}\right|  = r\frac{{k}^{n}}{n!}{\left| t - {t}_{0}\right| }^{n}.
\]

La série de fonctions \( \sum \left( {{\psi }_{n + 1} - {\psi }_{n}}\right) \) converge donc normalement sur \( {I}_{\alpha } \) , par conséquent la suite de fonctions \( \left( {\psi }_{n}\right) \) converge uniformément sur \( {I}_{\alpha } \) . Notons \( \psi \) la fonction limite. On a \( \psi \in \Gamma \) et

> The series of functions \( \sum \left( {{\psi }_{n + 1} - {\psi }_{n}}\right) \) therefore converges normally on \( {I}_{\alpha } \) , consequently the sequence of functions \( \left( {\psi }_{n}\right) \) converges uniformly on \( {I}_{\alpha } \) . Let \( \psi \) denote the limit function. We have \( \psi \in \Gamma \) and

\[
\forall n \in  \mathbb{N},\forall t \in  {I}_{\alpha },\;{\psi }_{n + 1}\left( t\right)  = {x}_{0} + {\int }_{{t}_{0}}^{t}F\left( {u,{\psi }_{n}\left( u\right) }\right) {du},
\]

et en faisant tendre \( n \) vers \( + \infty \) on en déduit \( \psi \left( t\right) = {x}_{0} + {\int }_{{t}_{0}}^{t}F\left( {u,\psi \left( u\right) }\right) {du} \) , c’est-à-dire que \( \psi \) est solution au problème de Cauchy en \( \left( {{t}_{0},{x}_{0}}\right) \) sur l’intervalle \( {I}_{\alpha } \) .

> and by letting \( n \) tend to \( + \infty \) we deduce \( \psi \left( t\right) = {x}_{0} + {\int }_{{t}_{0}}^{t}F\left( {u,\psi \left( u\right) }\right) {du} \) , that is to say that \( \psi \) is a solution to the Cauchy problem at \( \left( {{t}_{0},{x}_{0}}\right) \) on the interval \( {I}_{\alpha } \) .

Unicité. Soient \( \varphi : I \rightarrow {\mathbb{R}}^{n} \) et \( \psi : J \rightarrow {\mathbb{R}}^{n} \) deux solutions au problème de Cauchy en \( \left( {{t}_{0},{x}_{0}}\right) \) . En notant, pour tout \( t \in I \cap J,{M}_{t} = \mathop{\sup }\limits_{{u \in \left( {{t}_{0}, t}\right) }}\parallel \psi \left( u\right) - \varphi \left( u\right) \parallel \) , une récurrence sur \( n \) donne

> Uniqueness. Let \( \varphi : I \rightarrow {\mathbb{R}}^{n} \) and \( \psi : J \rightarrow {\mathbb{R}}^{n} \) be two solutions to the Cauchy problem at \( \left( {{t}_{0},{x}_{0}}\right) \) . By noting, for all \( t \in I \cap J,{M}_{t} = \mathop{\sup }\limits_{{u \in \left( {{t}_{0}, t}\right) }}\parallel \psi \left( u\right) - \varphi \left( u\right) \parallel \) , a recurrence on \( n \) gives

\[
\forall t \in  I \cap  J,\forall n \in  \mathbb{N},\;\parallel \varphi \left( t\right)  - \psi \left( t\right) \parallel  \leq  \left| {{\int }_{{t}_{0}}^{t}\parallel F\left( {u,\varphi \left( u\right) }\right)  - F\left( {u,\psi \left( u\right) }\right) \parallel {du}}\right|  \leq  \frac{{\left| t - {t}_{0}\right| }^{n}}{n!}{k}^{n}{M}_{t}.
\]

Ceci étant vrai pour tout \( n \in \mathbb{N} \) , on en déduit \( \varphi \left( t\right) = \psi \left( t\right) \) pour tout \( t \in I \cap J \) .

> Since this is true for all \( n \in \mathbb{N} \) , we deduce \( \varphi \left( t\right) = \psi \left( t\right) \) for all \( t \in I \cap J \) .

Remarque 2. - L’existence au problème de Cauchy reste vraie si \( F \) est seulement supposée continue (théorème de Péano), mais il n'y a plus forcément l'unicité (voir l'exercice 1).

> Remark 2. - Existence for the Cauchy problem remains true if \( F \) is only assumed to be continuous (Peano's theorem), but uniqueness is no longer guaranteed (see exercise 1).

- L'unicité au problème de Cauchy est riche de conséquences (voir les exercices de cette partie).

> - Uniqueness for the Cauchy problem is rich in consequences (see the exercises in this section).

- Si \( F \) est de classe \( {\mathcal{C}}^{1}, F \) est localement lipschitzienne en la seconde variable. C’est souvent ce que l'on rencontre dans la pratique, et le théorème de Cauchy-Lipschitz est alors applicable.

> - If \( F \) is of class \( {\mathcal{C}}^{1}, F \) it is locally Lipschitz in the second variable. This is often what is encountered in practice, and the Cauchy-Lipschitz theorem is then applicable.

- Pour les équations différentielles d'ordre \( n \) (en les ramenant à celles d'ordre 1 par la technique décrite plus haut), le théorème de Cauchy s’exprime ainsi : si \( {y}^{\left( n\right) } = \; F\left( {t, y,{y}^{\prime },\ldots ,{y}^{\left( n - 1\right) }}\right) \) est une équation différentielle d’ordre \( n \) et si \( F \) est continue et localement lipschitzienne par rapport à la seconde variable \( Y = \left( {{y}_{0},\ldots ,{y}_{n - 1}}\right) \) , alors il y a unicité au problème de Cauchy.

> - For differential equations of order \( n \) (by reducing them to first-order equations using the technique described above), the Cauchy theorem is expressed as follows: if \( {y}^{\left( n\right) } = \; F\left( {t, y,{y}^{\prime },\ldots ,{y}^{\left( n - 1\right) }}\right) \) is a differential equation of order \( n \) and if \( F \) is continuous and locally Lipschitz with respect to the second variable \( Y = \left( {{y}_{0},\ldots ,{y}_{n - 1}}\right) \), then there is uniqueness for the Cauchy problem.

Terminons par le corollaire suivant portant sur les solutions maximales.

> Let us conclude with the following corollary regarding maximal solutions.

COROLLAIRE 1. Soit \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( \Omega \) est un ouvert de \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) une fonction continue et localement lipschitzienne en la seconde variable. Alors pour tout \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , il existe une unique solution maximale \( \varphi \) de l’équation différentielle \( {y}^{\prime } = F\left( {t, y}\right) \) prenant la valeur \( {x}_{0} \) en \( {t}_{0} \) ; cette solution maximale est définie sur un intervalle ouvert de \( \mathbb{R} \) .

> COROLLARY 1. Let \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( \Omega \) is an open subset of \( \mathbb{R} \times {\mathbb{R}}^{n} \)) be a function continuous and locally Lipschitz in the second variable. Then for any \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \), there exists a unique maximal solution \( \varphi \) to the differential equation \( {y}^{\prime } = F\left( {t, y}\right) \) taking the value \( {x}_{0} \) at \( {t}_{0} \); this maximal solution is defined on an open interval of \( \mathbb{R} \).
