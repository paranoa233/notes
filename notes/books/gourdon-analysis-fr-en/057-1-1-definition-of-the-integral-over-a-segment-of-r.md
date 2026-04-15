#### 1.1. Definition of the integral over a segment of \( \mathbb{R} \)

*Français : 1.1. Définition de l'intégrale sur un segment de \( \mathbb{R} \)*

##### Integral of step functions.

*Français : Intégrale des fonctions en escalier.*

DéFINITION 1. On appelle subdivision de \( \left\lbrack {a, b}\right\rbrack \) toute partie finie de \( \left\lbrack {a, b}\right\rbrack \) contenant \( a \) et \( b \) . Si \( \sigma \) est une subdivision de \( \left\lbrack {a, b}\right\rbrack \) , on peut écrire \( \sigma = \left\{ {{x}_{0},{x}_{1},\ldots ,{x}_{n}}\right\} \) avec \( a = {x}_{0} < {x}_{1} < \; \ldots < {x}_{n} = b \) . C’est en général la notation employée pour désigner une subdivision.

> DEFINITION 1. A subdivision of \( \left\lbrack {a, b}\right\rbrack \) is any finite subset of \( \left\lbrack {a, b}\right\rbrack \) containing \( a \) and \( b \). If \( \sigma \) is a subdivision of \( \left\lbrack {a, b}\right\rbrack \), we can write \( \sigma = \left\{ {{x}_{0},{x}_{1},\ldots ,{x}_{n}}\right\} \) with \( a = {x}_{0} < {x}_{1} < \; \ldots < {x}_{n} = b \). This is generally the notation used to designate a subdivision.

On appelle pas (ou module) de la subdivision \( \sigma \) et on note \( \left| \sigma \right| \) le réel \( \mathop{\sup }\limits_{{1 \leq i \leq n}}\left( {{x}_{i} - {x}_{i - 1}}\right) \) .

> The step (or mesh) of the subdivision \( \sigma \) is called and denoted by \( \left| \sigma \right| \) the real number \( \mathop{\sup }\limits_{{1 \leq i \leq n}}\left( {{x}_{i} - {x}_{i - 1}}\right) \).

DÉFINITION 2. Une application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) est dite en escalier s’il existe une subdivision de \( \left\lbrack {a, b}\right\rbrack \)

> DEFINITION 2. A mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) is said to be a step function if there exists a subdivision of \( \left\lbrack {a, b}\right\rbrack \)

\[
\sigma  : a = {x}_{0} < {x}_{1} < \ldots  < {x}_{n} = b
\]

telle que pour tout \( i \in \{ 1,\ldots , n\} ,\varphi \) soit constante sur \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) . Une telle subdivision \( \sigma \) est dite alors bien adaptée à \( \varphi \) .

> such that for all \( i \in \{ 1,\ldots , n\} ,\varphi \), it is constant on \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \). Such a subdivision \( \sigma \) is then said to be well-adapted to \( \varphi \).

DéFINITION 3 (Intégrale d’une fonction en escalier). Soit \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une fonction en escalier. Soit \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) une subdivision de \( \left\lbrack {a, b}\right\rbrack \) bien adaptée à \( \varphi \) , de sorte que pour tout \( i \in \{ 1,\ldots , n\} \) , il existe \( {c}_{i} \in E \) telle que \( \varphi \left( x\right) = {c}_{i} \) sur \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) . La valeur

> DEFINITION 3 (Integral of a step function). Let \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a step function. Let \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) be a subdivision of \( \left\lbrack {a, b}\right\rbrack \) well-adapted to \( \varphi \), such that for all \( i \in \{ 1,\ldots , n\} \), there exists \( {c}_{i} \in E \) such that \( \varphi \left( x\right) = {c}_{i} \) on \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \). The value

\[
I\left( {\sigma ,\varphi }\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{x}_{i} - {x}_{i - 1}}\right) {c}_{i}
\]

est indépendante de la subdivision \( \sigma \) adaptée à \( \varphi \) . On la note alors \( I\left( \varphi \right) \) ou encore \( {\int }_{\left\lbrack a, b\right\rbrack }\varphi \) ou \( {\int }_{a}^{b}\varphi \left( x\right) {dx} \) , et on l’appelle intégrale de \( \varphi \) .

> is independent of the subdivision \( \sigma \) adapted to \( \varphi \). It is then denoted by \( I\left( \varphi \right) \) or \( {\int }_{\left\lbrack a, b\right\rbrack }\varphi \) or \( {\int }_{a}^{b}\varphi \left( x\right) {dx} \), and is called the integral of \( \varphi \).

Remarque 1. - Toute fonction en escalier sur \( \left\lbrack {a, b}\right\rbrack \) à valeurs dans \( \mathbb{K} \) est combinaison linéaire de fonctions caractéristiques de segments contenus dans \( \left\lbrack {a, b}\right\rbrack \) .

> Remark 1. - Any step function on \( \left\lbrack {a, b}\right\rbrack \) with values in \( \mathbb{K} \) is a linear combination of characteristic functions of segments contained in \( \left\lbrack {a, b}\right\rbrack \).

- L’ensemble \( \mathcal{E}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) des fonctions en escalier sur \( \left\lbrack  {a, b}\right\rbrack \) est un \( \mathbb{K} \) -e.v, et l’application \( \mathcal{E} \rightarrow  E\;\varphi  \mapsto  I\left( \varphi \right) \) est linéaire.

> - The set \( \mathcal{E}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) of step functions on \( \left\lbrack  {a, b}\right\rbrack \) is a \( \mathbb{K} \)-v.s., and the mapping \( \mathcal{E} \rightarrow  E\;\varphi  \mapsto  I\left( \varphi \right) \) is linear.

- Pour toute fonction en escalier \( \varphi ,\parallel \varphi \parallel \) est une fonction en escalier et \( \parallel I\left( \varphi \right) \parallel  \leq \; I\left( {\parallel \varphi \parallel }\right) \) .

> - For any step function \( \varphi ,\parallel \varphi \parallel \) is a step function and \( \parallel I\left( \varphi \right) \parallel  \leq \; I\left( {\parallel \varphi \parallel }\right) \).

- Si \( \varphi \) et \( \psi \) sont en escalier,à valeurs réelles, et si \( \varphi  \leq  \psi \) , alors \( I\left( \varphi \right)  \leq  I\left( \psi \right) \) .

> - If \( \varphi \) and \( \psi \) are step functions, with real values, and if \( \varphi  \leq  \psi \), then \( I\left( \varphi \right)  \leq  I\left( \psi \right) \).

##### Integral of a piecewise continuous function.

*Français : Intégrale d'une fonction continue par morceaux.*

Bien qu'on puisse définir l'intégrale de classes de fonctions beaucoup plus générales, nous nous limiterons à l'intégrale des fonctions continues par morceaux sur un segment \( \left\lbrack {a, b}\right\rbrack \subset \mathbb{R} \) dont la définition se trouve page 98 .

> Although one can define the integral of much more general classes of functions, we will limit ourselves to the integral of piecewise continuous functions on a segment \( \left\lbrack {a, b}\right\rbrack \subset \mathbb{R} \), the definition of which can be found on page 98.

\( \rightarrow \) Définition 4 (INTÉGRALE D'UNE FONCTION CONTINUE PAR MORCEAUX). Soit une fonction \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) continue par morceaux. Alors tout \( n \in {\mathbb{N}}^{ * } \) , il existe une fonction en escalier \( {\varphi }_{n} : \left\lbrack {a, b}\right\rbrack \rightarrow E \) telle que \( \begin{Vmatrix}{f - {\varphi }_{n}}\end{Vmatrix} < 1/n \) sur \( \left\lbrack {a, b}\right\rbrack \) . La suite \( \left( {u}_{n}\right) \) définie par \( {u}_{n} = {\int }_{a}^{b}{\varphi }_{n}\left( t\right) {dt} \) est alors une suite de Cauchy dans \( E \) , donc convergente. Sa limite ne dépend pas du choix des fonctions en escaliers \( {\varphi }_{n} \) , on la note \( {\int }_{a}^{b}f\left( t\right) {dt} \) (ou encore \( {\int }_{\left\lbrack a, b\right\rbrack }f \) ) et on l’appelle intégrale de \( f \) .

> \( \rightarrow \) Definition 4 (INTEGRAL OF A PIECEWISE CONTINUOUS FUNCTION). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a piecewise continuous function. Then for any \( n \in {\mathbb{N}}^{ * } \) , there exists a step function \( {\varphi }_{n} : \left\lbrack {a, b}\right\rbrack \rightarrow E \) such that \( \begin{Vmatrix}{f - {\varphi }_{n}}\end{Vmatrix} < 1/n \) on \( \left\lbrack {a, b}\right\rbrack \) . The sequence \( \left( {u}_{n}\right) \) defined by \( {u}_{n} = {\int }_{a}^{b}{\varphi }_{n}\left( t\right) {dt} \) is then a Cauchy sequence in \( E \) , and therefore convergent. Its limit does not depend on the choice of step functions \( {\varphi }_{n} \) , we denote it \( {\int }_{a}^{b}f\left( t\right) {dt} \) (or also \( {\int }_{\left\lbrack a, b\right\rbrack }f \) ) and call it the integral of \( f \) .

Démonstration. Comme \( f \) est continue par morceaux, c’est une fonction réglée, donc pour tout \( n \in {\mathbb{N}}^{ * } \) il existe bien une fonction en escalier \( {\varphi }_{n} \) vérifiant \( \begin{Vmatrix}{f - {\varphi }_{n}}\end{Vmatrix} < 1/n \) sur \( \left\lbrack {a, b}\right\rbrack \) (voir la proposition 5 page 99). La suite \( \left( {u}_{n}\right) \) vérifie bien le critère de Cauchy car d’après la remarque 1, et comme \( \begin{Vmatrix}{{\varphi }_{p} - {\varphi }_{q}}\end{Vmatrix} \leq \begin{Vmatrix}{{\varphi }_{p} - f}\end{Vmatrix} + \begin{Vmatrix}{f - {\varphi }_{q}}\end{Vmatrix} \leq 1/p + 1/q \) , on a

> Proof. Since \( f \) is piecewise continuous, it is a regulated function, so for any \( n \in {\mathbb{N}}^{ * } \) there indeed exists a step function \( {\varphi }_{n} \) satisfying \( \begin{Vmatrix}{f - {\varphi }_{n}}\end{Vmatrix} < 1/n \) on \( \left\lbrack {a, b}\right\rbrack \) (see proposition 5 page 99). The sequence \( \left( {u}_{n}\right) \) indeed satisfies the Cauchy criterion because according to remark 1, and since \( \begin{Vmatrix}{{\varphi }_{p} - {\varphi }_{q}}\end{Vmatrix} \leq \begin{Vmatrix}{{\varphi }_{p} - f}\end{Vmatrix} + \begin{Vmatrix}{f - {\varphi }_{q}}\end{Vmatrix} \leq 1/p + 1/q \) , we have

\[
\forall p, q \in  \mathbb{N}, p, q \geq  n\;\begin{Vmatrix}{{u}_{p} - {u}_{q}}\end{Vmatrix} = \begin{Vmatrix}{I\left( {{\varphi }_{p} - {\varphi }_{q}}\right) }\end{Vmatrix} \leq  I\left( \begin{Vmatrix}{{\varphi }_{p} - {\varphi }_{q}}\end{Vmatrix}\right)  \leq  I\left( {2/n}\right)  = 2\left( {b - a}\right) /n.
\]

Comme \( E \) est complet par hypothèse (c’est un espace de Banach), la suite \( \left( {u}_{n}\right) \) converge. On note \( \ell \) sa limite.

> Since \( E \) is complete by hypothesis (it is a Banach space), the sequence \( \left( {u}_{n}\right) \) converges. We denote its limit by \( \ell \) .

Unicité de la limite. Soit \( \left( {\psi }_{n}\right) \) une autre suite de fonctions en escalier vérifiant \( \begin{Vmatrix}{f - {\psi }_{n}}\end{Vmatrix} < 1/n \) sur \( \left\lbrack {a, b}\right\rbrack \) . On note \( {\ell }^{\prime } \) la limite de \( {v}_{n} = I\left( {\psi }_{n}\right) \) . L’inégalité

> Uniqueness of the limit. Let \( \left( {\psi }_{n}\right) \) be another sequence of step functions satisfying \( \begin{Vmatrix}{f - {\psi }_{n}}\end{Vmatrix} < 1/n \) on \( \left\lbrack {a, b}\right\rbrack \) . We denote the limit of \( {v}_{n} = I\left( {\psi }_{n}\right) \) by \( {\ell }^{\prime } \) . The inequality

\[
\begin{Vmatrix}{{\psi }_{n} - {\varphi }_{n}}\end{Vmatrix} \leq  \begin{Vmatrix}{{\psi }_{n} - f}\end{Vmatrix} + \begin{Vmatrix}{f - {\varphi }_{n}}\end{Vmatrix} \leq  2/n
\]

entraîne

> implies

\[
\forall n,\;\begin{Vmatrix}{{v}_{n} - {u}_{n}}\end{Vmatrix} = \begin{Vmatrix}{I\left( {{\psi }_{n} - {\varphi }_{n}}\right) }\end{Vmatrix} \leq  I\left( \begin{Vmatrix}{{\psi }_{n} - {\varphi }_{n}}\end{Vmatrix}\right)  \leq  I\left( {2/n}\right)  = 2\left( {b - a}\right) /n
\]

donc \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{{u}_{n} - {v}_{n}}\end{Vmatrix} = 0 \) . Donc \( {\ell }^{\prime } = \ell \) .

> so \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{{u}_{n} - {v}_{n}}\end{Vmatrix} = 0 \) . Thus \( {\ell }^{\prime } = \ell \) .

Remarque 2. - Lorsque \( f \) est à valeurs réelles, on peut définir

> Remark 2. - When \( f \) is real-valued, we can define

\[
{I}^{ - }\left( f\right)  = \mathop{\sup }\limits_{\substack{{\varphi  \in  \mathcal{E}} \\  {\varphi  \leq  f} }}I\left( \varphi \right) \;\text{ et }\;{I}^{ + }\left( f\right)  = \mathop{\inf }\limits_{\substack{{\psi  \in  \mathcal{E}} \\  {\psi  \geq  f} }}I\left( \psi \right) ,
\]

où \( \mathcal{E} \) désigne l’ensemble des fonctions en escalier de \( \left\lbrack {a, b}\right\rbrack \) dans \( \mathbb{R} \) . Lorsque \( f \) est continue par morceaux, on a \( {I}^{ - }\left( f\right) = {I}^{ + }\left( f\right) \) , et cette valeur commune est un moyen équivalent de définir l’intégrale de \( f \) . La définition 4 permet de ne pas se limiter au cadre où \( E = \mathbb{R} \) et donne une définition intrinsèque de l’intégrale sur tout e.v.n complet, en particulier sur \( \mathbb{C} \) et sur tout e.v de dimension finie (voir la remarque 3).

> where \( \mathcal{E} \) denotes the set of step functions from \( \left\lbrack {a, b}\right\rbrack \) to \( \mathbb{R} \). When \( f \) is piecewise continuous, we have \( {I}^{ - }\left( f\right) = {I}^{ + }\left( f\right) \), and this common value is an equivalent way to define the integral of \( f \). Definition 4 allows us not to be limited to the case where \( E = \mathbb{R} \) and provides an intrinsic definition of the integral on any complete normed vector space, in particular on \( \mathbb{C} \) and on any finite-dimensional vector space (see Remark 3).

- Lorsque \( f \) et \( g \) sont deux fonctions continues par morceaux qui diffèrent seulement en un nombre fini de points, leurs intégrales sont identiques.

> - When \( f \) and \( g \) are two piecewise continuous functions that differ only at a finite number of points, their integrals are identical.

- L'intégrale d'une fonction en escalier donnée par la définition 4 est cohérente avec celle donnée dans la définition 3.

> - The integral of a step function given by Definition 4 is consistent with that given in Definition 3.

- Lorsque \( a > b \) , on définit \( {\int }_{a}^{b}f\left( x\right) {dx} =  - {\int }_{b}^{a}f\left( x\right) {dx} \) .

> - When \( a > b \), we define \( {\int }_{a}^{b}f\left( x\right) {dx} =  - {\int }_{b}^{a}f\left( x\right) {dx} \).

- La définition précédente s'étend facilement pour définir l'intégrale d'une fonction réglée. On peut de manière plus générale définir les fonctions Riemann-intégrables, qui sont les fonctions \( f \) telles que pour tout \( \varepsilon  > 0 \) , on peut trouver \( \varphi \) et \( \mu \) en escalier telles que \( \parallel f - \varphi \parallel  < \mu \) et \( I\left( \mu \right)  < \varepsilon \) . En faisant tendre \( \varepsilon \) vers 0, les valeurs \( I\left( \varphi \right) \) convergent vers une valeur unique appelée intégrale de Riemann de \( f \) . Toute fonction continue par morceaux, toute fonction réglée, est Riemann-intégrable.

> - The previous definition extends easily to define the integral of a regulated function. More generally, one can define Riemann-integrable functions, which are functions \( f \) such that for any \( \varepsilon  > 0 \), one can find step functions \( \varphi \) and \( \mu \) such that \( \parallel f - \varphi \parallel  < \mu \) and \( I\left( \mu \right)  < \varepsilon \). By letting \( \varepsilon \) tend to 0, the values \( I\left( \varphi \right) \) converge to a unique value called the Riemann integral of \( f \). Any piecewise continuous function, any regulated function, is Riemann-integrable.

Proposition 1. Soient \( E \) un \( \mathbb{K} \) -e.v.n de dimension finie (toujours avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ), \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application. On peut écrire \( f = \; \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{i}{e}_{i} \) où pour tout \( i \) , l’application \( {f}_{i} \) prend ses valeurs dans \( \mathbb{K} \) . L’application \( f \) est continue par morceaux si et seulement si chacune des applications \( {f}_{i} \) est continue par morceaux et on a alors

> Proposition 1. Let \( E \) be a finite-dimensional \( \mathbb{K} \)-normed vector space (always with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \)), \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) a basis of \( E \), and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) a mapping. We can write \( f = \; \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{i}{e}_{i} \) where for all \( i \), the mapping \( {f}_{i} \) takes its values in \( \mathbb{K} \). The mapping \( f \) is piecewise continuous if and only if each of the mappings \( {f}_{i} \) is piecewise continuous, and we then have

\[
{\int }_{a}^{b}f\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\int }_{a}^{b}{f}_{i}\left( x\right) {dx}}\right) {e}_{i}.
\]

Remarque 3. - En particulier, \( \mathbb{C} \) est un \( \mathbb{R} \) -e.v dont \( \left( {1, i}\right) \) est une base. L’application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) s’écrit sous la forme \( f = {f}_{1} + i{f}_{2} \) (où \( {f}_{1},{f}_{2} \) sont à valeurs réelles) et on a \( {\int }_{a}^{b}f\left( x\right) {dx} = {\int }_{a}^{b}{f}_{1}\left( x\right) {dx} + i\left( {{\int }_{a}^{b}{f}_{2}\left( x\right) {dx}}\right) \) .

> Remark 3. - In particular, \( \mathbb{C} \) is a \( \mathbb{R} \)-vector space of which \( \left( {1, i}\right) \) is a basis. The mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) is written in the form \( f = {f}_{1} + i{f}_{2} \) (where \( {f}_{1},{f}_{2} \) are real-valued) and we have \( {\int }_{a}^{b}f\left( x\right) {dx} = {\int }_{a}^{b}{f}_{1}\left( x\right) {dx} + i\left( {{\int }_{a}^{b}{f}_{2}\left( x\right) {dx}}\right) \).

- On peut définir l’intégrale d’une fonction \( f \) à valeurs dans un \( \mathbb{R} \) -e.v de dimension finie \( E \) à partir de l’intégrale des fonctions à valeurs réelles, en procédant comme suit : on considère une base \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) , on écrit \( f = \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{i}{e}_{i} \) où les \( {f}_{i} \) sont à valeurs réelles, et on pose \( {\int }_{a}^{b}f\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\int }_{a}^{b}{f}_{i}\left( x\right) {dx}}\right) {e}_{i} \) . Il faut ensuite vérifier que cette définition ne dépend pas de la base \( \mathcal{B} \) choisie. L’avantage de la définition que nous avons adoptée (voir définition 4) est qu'elle est intrinsèque (i. e elle ne privilégie pas de base).

> - One can define the integral of a function \( f \) with values in a finite-dimensional \( \mathbb{R} \) -vector space \( E \) starting from the integral of real-valued functions, by proceeding as follows: consider a basis \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) , write \( f = \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{i}{e}_{i} \) where the \( {f}_{i} \) are real-valued, and set \( {\int }_{a}^{b}f\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\int }_{a}^{b}{f}_{i}\left( x\right) {dx}}\right) {e}_{i} \) . It must then be verified that this definition does not depend on the chosen basis \( \mathcal{B} \) . The advantage of the definition we have adopted (see definition 4) is that it is intrinsic (i.e., it does not favor any basis).
