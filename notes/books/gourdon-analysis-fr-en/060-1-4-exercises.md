#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1 (INTÉGRALES DE WALLIS). Pour tout \( n \in \mathbb{N} \) , on pose

> EXERCISE 1 (WALLIS INTEGRALS). For any \( n \in \mathbb{N} \) , we define

\[
{I}_{n} = {\int }_{0}^{\pi /2}{\sin }^{n}{xdx}
\]

a) Donner une expression explicite de \( {I}_{n} \) pour tout \( n \in \mathbb{N} \) .

> a) Give an explicit expression for \( {I}_{n} \) for any \( n \in \mathbb{N} \) .

b) En déduire la formule de Wallis

> b) Deduce the Wallis formula

\[
\mathop{\lim }\limits_{{p \rightarrow   + \infty }}\frac{1}{p}{\left\lbrack  \frac{{2p}\left( {{2p} - 2}\right) \cdots 2}{\left( {{2p} - 1}\right) \left( {{2p} - 3}\right) \cdots 1}\right\rbrack  }^{2} = \pi ,
\]

puis montrer que lorsque \( n \rightarrow + \infty ,{I}_{n} \sim \sqrt{\frac{\pi }{2n}} \) .

> then show that as \( n \rightarrow + \infty ,{I}_{n} \sim \sqrt{\frac{\pi }{2n}} \) .

Solution. a) En intégrant par parties, on a

> Solution. a) By integrating by parts, we have

\[
\forall n \geq  2,\;{I}_{n} = {\int }_{0}^{\pi /2}{\sin }^{n - 1}x\sin {xdx} = {\left\lbrack  -{\sin }^{n - 1}x\cos x\right\rbrack  }_{0}^{\pi /2} + \left( {n - 1}\right) {\int }_{0}^{\pi /2}{\sin }^{n - 2}x{\cos }^{2}{xdx}
\]

\[
= \left( {n - 1}\right) \left( {{I}_{n - 2} - {I}_{n}}\right) \;\text{ d’où }\;{I}_{n} = \frac{n - 1}{n}{I}_{n - 2}.
\]

Comme \( {I}_{0} = \pi /2 \) et \( {I}_{1} = {\left\lbrack -\cos x\right\rbrack }_{0}^{\pi /2} = 1 \) , on en déduit

> Since \( {I}_{0} = \pi /2 \) and \( {I}_{1} = {\left\lbrack -\cos x\right\rbrack }_{0}^{\pi /2} = 1 \) , we deduce

\[
\forall p \in  {\mathbb{N}}^{ * },\;{I}_{2p} = \frac{\left( {{2p} - 1}\right) \left( {{2p} - 3}\right) \cdots 1}{{2p}\left( {{2p} - 2}\right) \cdots 2}\frac{\pi }{2}\;\text{ et }\;{I}_{{2p} + 1} = \frac{{2p}\left( {{2p} - 2}\right) \cdots 2}{\left( {{2p} + 1}\right) \left( {{2p} - 1}\right) \cdots 1}.
\]

(*)

> b) En remarquant que

b) By noting that

\[
\forall p \in  {\mathbb{N}}^{ * },\forall x \in  \left\lbrack  {0,\frac{\pi }{2}}\right\rbrack  ,\;0 \leq  {\sin }^{{2p} + 1}x \leq  {\sin }^{2p}x \leq  {\sin }^{{2p} - 1}x,
\]

on tire, par intégration

> we obtain, by integration

\[
\forall p \in  {\mathbb{N}}^{ * },\;{I}_{{2p} + 1} \leq  {I}_{2p} \leq  {I}_{{2p} - 1}\;\text{ donc }\;1 \leq  \frac{{I}_{2p}}{{I}_{{2p} + 1}} \leq  \frac{{I}_{{2p} - 1}}{{I}_{{2p} + 1}} = \frac{{2p} + 1}{2p},
\]

la dernière égalité étant une conséquence de (*). Par conséquent

> the last equality being a consequence of (*). Consequently

\[
\mathop{\lim }\limits_{{p \rightarrow   + \infty }}\frac{{I}_{2p}}{{I}_{{2p} + 1}} = 1
\]

et on en déduit la formule de Wallis avec la formule (*).

> and we deduce the Wallis formula from it with formula (*).

De la formule de Wallis, on déduit

> From the Wallis formula, we deduce

\[
\frac{\left( {{2p} - 1}\right) \left( {{2p} - 3}\right) \cdots 1}{\left( {2p}\right) \left( {{2p} - 2}\right) \cdots 2} \sim  \frac{1}{\sqrt{p\pi }}
\]

donc grâce à (*), on tire

> therefore thanks to (*), we obtain

\[
{I}_{2p} \sim  \frac{1}{2}\sqrt{\frac{\pi }{p}}\;\text{ et }\;{I}_{{2p} + 1} \sim  {I}_{2p} \sim  \frac{1}{2}\sqrt{\frac{\pi }{p}}.
\]

On en déduit l'équivalent demandé.

> We deduce the requested equivalent.

EXERCICE 2. Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction positive et continue sur \( \left\lbrack {a, b}\right\rbrack \) . a) Montrer que

> EXERCISE 2. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a positive and continuous function on \( \left\lbrack {a, b}\right\rbrack \) . a) Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n} = M\;\text{ où }\;M = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}f\left( t\right) .
\]

b) Soit \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue prenant des valeurs strictement positives sur \( \left\lbrack {a, b}\right\rbrack \) . Montrer que

> b) Let \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a continuous function taking strictly positive values on \( \left\lbrack {a, b}\right\rbrack \) . Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}g\left( t\right) dt\right) }^{1/n} = M\;\text{ où }\;M = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}f\left( t\right) .
\]

Solution. a) L’inégalité \( f{\left( t\right) }^{n} \leq {M}^{n} \) pour tout \( t \in \left\lbrack {a, b}\right\rbrack \) entraîne

> Solution. a) The inequality \( f{\left( t\right) }^{n} \leq {M}^{n} \) for all \( t \in \left\lbrack {a, b}\right\rbrack \) implies

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n} \leq  {\left( {\int }_{a}^{b}{M}^{n}\right) }^{1/n} = {\left( b - a\right) }^{1/n}M.
\]

(*)

> Par ailleurs, \( f \) étant continue sur le compact \( \left\lbrack {a, b}\right\rbrack \) , il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( f\left( c\right) = M \) . Pour tout \( \varepsilon > 0 \) , il existe donc un segment \( \left\lbrack {\alpha ,\beta }\right\rbrack \) contenant \( c \) , non réduit à un singleton, tel que

Furthermore, since \( f \) is continuous on the compact set \( \left\lbrack {a, b}\right\rbrack \) , there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( f\left( c\right) = M \) . For all \( \varepsilon > 0 \) , there therefore exists a segment \( \left\lbrack {\alpha ,\beta }\right\rbrack \) containing \( c \) , not reduced to a singleton, such that

\[
\forall t \in  \left\lbrack  {\alpha ,\beta }\right\rbrack  ,\;f\left( t\right)  \geq  M - \varepsilon .
\]

Ceci entraîne

> This implies

\[
{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n} \geq  {\left( {\int }_{\alpha }^{\beta }f{\left( t\right) }^{n}dt\right) }^{1/n} \geq  {\left( {\int }_{\alpha }^{\beta }{\left( M - \varepsilon \right) }^{n}dt\right) }^{1/n} = {\left( \beta  - \alpha \right) }^{1/n}\left( {M - \varepsilon }\right) .
\]

(**)

> Comme \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\mu }^{1/n} = 0 \) pour tout réel \( \mu > 0 \) , on tire de (*) et (**)

Since \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\mu }^{1/n} = 0 \) for all real \( \mu > 0 \) , we obtain from (*) and (**)

\[
\exists N \in  {\mathbb{N}}^{ * },\forall n \geq  N,\;M - {2\varepsilon } \leq  {\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n} \leq  M + \varepsilon .
\]

Ceci étant possible pour tout \( \varepsilon > 0 \) , on en déduit le résultat.

> As this is possible for all \( \varepsilon > 0 \) , we deduce the result.

b) La fonction \( g \) étant continue sur un compact, elle est bornée et atteint ses bornes. On en conclut que les réels

> b) Since the function \( g \) is continuous on a compact set, it is bounded and attains its bounds. We conclude that the real numbers

\[
k = \mathop{\inf }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}g\left( t\right) \;\text{ et }\;K = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}g\left( t\right)
\]

existent et sont strictement positifs. Par ailleurs, le fait que \( {kf}{\left( t\right) }^{n} \leq g\left( t\right) f{\left( t\right) }^{n} \leq {Kf}{\left( t\right) }^{n} \) pour tout \( t \in \left\lbrack {a, b}\right\rbrack \) montre que

> exist and are strictly positive. Furthermore, the fact that \( {kf}{\left( t\right) }^{n} \leq g\left( t\right) f{\left( t\right) }^{n} \leq {Kf}{\left( t\right) }^{n} \) for all \( t \in \left\lbrack {a, b}\right\rbrack \) shows that

\[
{k}^{1/n}{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n} \leq  {\left( {\int }_{a}^{b}f{\left( t\right) }^{n}g\left( t\right) dt\right) }^{1/n} \leq  {K}^{1/n}{\left( {\int }_{a}^{b}f{\left( t\right) }^{n}dt\right) }^{1/n}.
\]

On conclut avec la question précédente et avec les limites \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{k}^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{K}^{1/n} = 1 \) .

> We conclude with the previous question and with the limits \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{k}^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{K}^{1/n} = 1 \) .

EXERCICE 3. Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que \( f\left( a\right) = f\left( b\right) = 0 \) . Soit \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\prime }\left( t\right) }\right| . \)

> EXERCISE 3. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) class function such that \( f\left( a\right) = f\left( b\right) = 0 \) . Let \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\prime }\left( t\right) }\right| . \)

a) Montrer

> a) Show that

\[
\left| {{\int }_{a}^{b}f\left( t\right) {dt}}\right|  \leq  \frac{{\left( b - a\right) }^{2}}{4}M
\]

(*)

> b) Dans quels cas l'inégalité (*) est elle une égalité ?

b) In which cases is the inequality (*) an equality?

> Solution. a) Le problème est symétrique par rapport à \( c = \left( {a + b}\right) /2 \) . On écrit

Solution. a) The problem is symmetric with respect to \( c = \left( {a + b}\right) /2 \) . We write

> et

\[
\forall t \in  \left\lbrack  {a, c}\right\rbrack  ,\;\left| {f\left( t\right) }\right|  = \left| {{\int }_{a}^{t}{f}^{\prime }\left( x\right) {dx}}\right|  \leq  {\int }_{a}^{t}\left| {{f}^{\prime }\left( x\right) }\right| {dx} \leq  M\left( {t - a}\right)
\]

\[
\forall t \in  \left\lbrack  {c, b}\right\rbrack  ,\;\left| {f\left( t\right) }\right|  = \left| {{\int }_{t}^{b}{f}^{\prime }\left( x\right) {dx}}\right|  \leq  {\int }_{t}^{b}\left| {{f}^{\prime }\left( x\right) }\right| {dx} \leq  M\left( {b - t}\right) ,
\]

ce qui entraîne

> which implies

\[
\left| {{\int }_{a}^{b}f\left( t\right) {dt}}\right|  \leq  {\int }_{a}^{b}\left| {f\left( t\right) }\right| {dt} \leq  M\left\lbrack  {{\int }_{a}^{c}\left( {t - a}\right) {dt} + {\int }_{c}^{b}\left( {b - t}\right) {dt}}\right\rbrack   = \frac{{\left( b - a\right) }^{2}}{4}M.
\]

b) Les fonctions en présence étant continues, l'égalité se produira si et seulement si chacune des inégalités précédentes est une égalité. On a donc

> b) Since the functions involved are continuous, equality will occur if and only if each of the preceding inequalities is an equality. We therefore have

\[
\forall t \in  \left\lbrack  {a, c}\right\rbrack  ,\;\left| {f\left( t\right) }\right|  = M\left( {t - a}\right) \;\text{ et }\;\forall t \in  \left\lbrack  {c, b}\right\rbrack  ,\;\left| {f\left( t\right) }\right|  = M\left( {b - t}\right) ,
\]

ce qui entraîne

> which implies

\[
\forall t \in  \left\lbrack  {a, c}\right\rbrack  ,\;f{\left( t\right) }^{2} = {M}^{2}{\left( t - a\right) }^{2}\;\text{ et }\;\forall t \in  \left\lbrack  {c, b}\right\rbrack  ,\;f{\left( t\right) }^{2} = {M}^{2}{\left( b - t\right) }^{2}.
\]

\( \left( {* * }\right) \)

> La fonction \( {f}^{2} \) est de classe \( {\mathcal{C}}^{1} \) , elle est donc dérivable en \( c = \left( {a + b}\right) /2 \) . Les formules (**) donnent successivement \( {\left( {f}^{2}\right) }^{\prime }\left( c\right) = 2{M}^{2}{\left( \frac{b - a}{2}\right) }^{2} \) et \( {\left( {f}^{2}\right) }^{\prime }\left( c\right) = - 2{M}^{2}{\left( \frac{b - a}{2}\right) }^{2} \) , ce qui \( {\text{ n’est possible que si }}^{\prime } \; M = 0 \) . Donc \( f = f\left( a\right) = 0 \) . Réciproquement, la fonction nulle est bien solution.

The function \( {f}^{2} \) is of class \( {\mathcal{C}}^{1} \) , so it is differentiable at \( c = \left( {a + b}\right) /2 \) . The formulas (**) give successively \( {\left( {f}^{2}\right) }^{\prime }\left( c\right) = 2{M}^{2}{\left( \frac{b - a}{2}\right) }^{2} \) and \( {\left( {f}^{2}\right) }^{\prime }\left( c\right) = - 2{M}^{2}{\left( \frac{b - a}{2}\right) }^{2} \) , which \( {\text{ n’est possible que si }}^{\prime } \; M = 0 \) . Thus \( f = f\left( a\right) = 0 \) . Conversely, the zero function is indeed a solution.

> EXERCICE 4. Soient \( E \) un espace euclidien et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une fonction continue. On suppose que

EXERCISE 4. Let \( E \) be a Euclidean space and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) a continuous function. Suppose that

\[
\begin{Vmatrix}{{\int }_{a}^{b}f\left( t\right) {dt}}\end{Vmatrix} = {\int }_{a}^{b}\parallel f\left( t\right) \parallel {dt}
\]

Montrer qu’il existe \( e \in E \) de norme 1 tel que \( f\left( t\right) = \parallel f\left( t\right) \parallel \cdot e \) pour tout \( t \in \left\lbrack {a, b}\right\rbrack \) .

> Show that there exists \( e \in E \) of norm 1 such that \( f\left( t\right) = \parallel f\left( t\right) \parallel \cdot e \) for all \( t \in \left\lbrack {a, b}\right\rbrack \) .

Solution. Si \( {\int }_{a}^{b}f\left( t\right) {dt} = 0 \) , les hypothèses et la continuité de \( f \) entraînent que \( f \) est identique-ment nulle, et le résultat est évident. Sinon, on pose

> Solution. If \( {\int }_{a}^{b}f\left( t\right) {dt} = 0 \) , the hypotheses and the continuity of \( f \) imply that \( f \) is identically zero, and the result is obvious. Otherwise, we set

\[
{e}_{1} = \frac{{\int }_{a}^{b}f\left( t\right) {dt}}{\begin{Vmatrix}{\int }_{a}^{b}f\left( t\right) dt\end{Vmatrix}}\;\text{ de sorte que }{\int }_{a}^{b}f\left( t\right) {dt} = \begin{Vmatrix}{{\int }_{a}^{b}f\left( t\right) {dt}}\end{Vmatrix}{e}_{1}.
\]

Le vecteur \( {e}_{1} \) est de norme 1. On le complète en une base orthonormale \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . On peut écrire \( f = {f}_{1}{e}_{1} + \cdots + {f}_{n}{e}_{n} \) où pour tout \( i,{f}_{i} \) est une fonction continue à valeurs réelles. On a

> The vector \( {e}_{1} \) has norm 1. We complete it into an orthonormal basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . We can write \( f = {f}_{1}{e}_{1} + \cdots + {f}_{n}{e}_{n} \) where for all \( i,{f}_{i} \) is a continuous real-valued function. We have

\[
{\int }_{a}^{b}f\left( t\right) {dt} = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\int }_{a}^{b}{f}_{i}\left( t\right) {dt}}\right) {e}_{i} = \begin{Vmatrix}{{\int }_{a}^{b}f\left( t\right) {dt}}\end{Vmatrix}{e}_{1} = \left( {{\int }_{a}^{b}\parallel f\left( t\right) \parallel {dt}}\right) {e}_{1},
\]

donc en extrayant la composante le long du vecteur \( {e}_{1} \)

> therefore, by extracting the component along the vector \( {e}_{1} \)

\[
{\int }_{a}^{b}{f}_{1}\left( t\right) {dt} = {\int }_{a}^{b}\parallel f\left( t\right) \parallel {dt}
\]

(*)

> Comme \( {f}_{1}\left( t\right) \leq \parallel f\left( t\right) \parallel = {\left( {f}_{1}{\left( t\right) }^{2} + \cdots + {f}_{n}{\left( t\right) }^{2}\right) }^{1/2} \) et que chacune de ces fonctions sont continues, l'égalité (*) entraîne

Since \( {f}_{1}\left( t\right) \leq \parallel f\left( t\right) \parallel = {\left( {f}_{1}{\left( t\right) }^{2} + \cdots + {f}_{n}{\left( t\right) }^{2}\right) }^{1/2} \) and each of these functions is continuous, equality (*) implies

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;{f}_{1}\left( t\right)  = \parallel f\left( t\right) \parallel  = {\left( {f}_{1}{\left( t\right) }^{2} + \cdots  + {f}_{n}{\left( t\right) }^{2}\right) }^{1/2}.
\]

(**)

> Donc \( {f}_{2}\left( t\right) = \ldots = {f}_{n}\left( t\right) = 0 \) pour tout \( t \in \left\lbrack {a, b}\right\rbrack \) , d’où

Thus \( {f}_{2}\left( t\right) = \ldots = {f}_{n}\left( t\right) = 0 \) for all \( t \in \left\lbrack {a, b}\right\rbrack \) , whence

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;f\left( t\right)  = {f}_{1}\left( t\right) {e}_{1} = \parallel f\left( t\right) \parallel {e}_{1},
\]

la dernière égalité étant encore une conséquence de (**).

> the last equality being also a consequence of (**).

EXERCICE 5. Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que \( 0 \leq {f}^{\prime }\left( t\right) \leq 1 \) pour tout \( t \in \left\lbrack {0,1}\right\rbrack \) . Montrer que

> EXERCISE 5. Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) class function such that \( 0 \leq {f}^{\prime }\left( t\right) \leq 1 \) for all \( t \in \left\lbrack {0,1}\right\rbrack \) . Show that

\[
{\int }_{0}^{1}f{\left( x\right) }^{3}{dx} \leq  {\left( {\int }_{0}^{1}f\left( x\right) dx\right) }^{2}.
\]

Solution. On considère les fonctions

> Solution. Consider the functions

\[
\varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  {\int }_{0}^{t}{f}^{3}\left( x\right) {dx}\;\text{ et }\;\psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  {\left( {\int }_{0}^{t}f\left( x\right) dx\right) }^{2}.
\]

Il s’agit de montrer \( \varphi \left( 1\right) \leq \psi \left( 1\right) \) . Les fonctions \( \varphi \) et \( \psi \) sont de classe \( {\mathcal{C}}^{1} \) . Comme \( \varphi \left( 0\right) = \psi \left( 0\right) = 0 \) , ceci sera prouvé si on montre \( {\varphi }^{\prime }\left( x\right) \leq {\psi }^{\prime }\left( x\right) \) pour tout \( x \in \left\lbrack {0,1}\right\rbrack \) , c’est-à-dire si

> We want to show \( \varphi \left( 1\right) \leq \psi \left( 1\right) \) . The functions \( \varphi \) and \( \psi \) are of class \( {\mathcal{C}}^{1} \) . Since \( \varphi \left( 0\right) = \psi \left( 0\right) = 0 \) , this will be proven if we show \( {\varphi }^{\prime }\left( x\right) \leq {\psi }^{\prime }\left( x\right) \) for all \( x \in \left\lbrack {0,1}\right\rbrack \) , that is, if

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;f{\left( x\right) }^{3} \leq  {2f}\left( x\right) {\int }_{0}^{x}f\left( t\right) {dt}.
\]

Comme \( f \geq 0 \) ( \( f\left( 0\right) = 0 \) et \( {f}^{\prime } \) est positive), ceci sera prouvé si on montre

> Since \( f \geq 0 \) ( \( f\left( 0\right) = 0 \) and \( {f}^{\prime } \) is positive), this will be proven if we show

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;f{\left( x\right) }^{2} \leq  2{\int }_{0}^{x}f\left( t\right) {dt}.
\]

Chacune de ces deux fonctions étant dérivable et nulle en 0, ce dernier point sera obtenu si on prouve que la dérivée de la première est inférieure à celle de la seconde sur \( \left\lbrack {0,1}\right\rbrack \) , c'est-à-dire si

> Since each of these two functions is differentiable and zero at 0, this last point will be obtained if we prove that the derivative of the first is less than that of the second on \( \left\lbrack {0,1}\right\rbrack \) , that is, if

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;{2f}\left( x\right) {f}^{\prime }\left( x\right)  \leq  {2f}\left( x\right) .
\]

Ce dernier point est bien réalisé car \( f \) est positive et \( {f}^{\prime } \leq 1 \) par hypothèse. D’où le résultat.

> This last point is indeed satisfied because \( f \) is positive and \( {f}^{\prime } \leq 1 \) by hypothesis. Hence the result.

Remarque. L’égalité se produit lorsque \( f\left( x\right) = x \) ou lorsque \( f \) est la fonction nulle.

> Remark. Equality occurs when \( f\left( x\right) = x \) or when \( f \) is the zero function.

EXERCICE 6. a) Montrer que la suite \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) définie par

> EXERCISE 6. a) Show that the sequence \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) defined by

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{n}{{n}^{2} + {k}^{2}}.
\]

converge et calculer sa limite \( \ell \) .

> converges and calculate its limit \( \ell \) .

b) Donner un équivalent de \( \ell - {u}_{n} \) lorsque \( n \) tend vers l’infini.

> b) Give an equivalent of \( \ell - {u}_{n} \) as \( n \) tends to infinity.

Solution. a) En considérant la fonction \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \frac{1}{1 + {x}^{2}} \) , on remarque que

> Solution. a) By considering the function \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \frac{1}{1 + {x}^{2}} \) , we note that

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}f\left( \frac{k}{n}\right) .
\]

Autrement dit, \( {u}_{n} \) est une somme de Riemann de \( f \) pour une subdivision de pas \( 1/n \) . On en déduit avec le théorème 7 que \( \left( {u}_{n}\right) \) converge et que

> In other words, \( {u}_{n} \) is a Riemann sum of \( f \) for a subdivision with step \( 1/n \) . We deduce from Theorem 7 that \( \left( {u}_{n}\right) \) converges and that

\[
\ell  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{u}_{n} = {\int }_{0}^{1}\frac{dx}{1 + {x}^{2}} = {\left\lbrack  \arctan x\right\rbrack  }_{0}^{1} = \frac{\pi }{4}.
\]

b) C’est classique. On procède comme suit. On considère une primitive \( F \) de \( f \) , de sorte que pour tout \( n \in {\mathbb{N}}^{ * } \) ,

> b) This is standard. We proceed as follows. Consider an antiderivative \( F \) of \( f \) , such that for all \( n \in {\mathbb{N}}^{ * } \) ,

\[
\ell  = F\left( 1\right)  - F\left( 0\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {F\left( \frac{k}{n}\right)  - F\left( \frac{k - 1}{n}\right) }\right) \;\text{ et }\;{u}_{n} = \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}{F}^{\prime }\left( \frac{k}{n}\right) ,
\]

donc

> therefore

\[
\forall n \in  {\mathbb{N}}^{ * },\;\ell  - {u}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\left\lbrack  {F\left( \frac{k}{n}\right)  - F\left( \frac{k - 1}{n}\right)  - \frac{1}{n}{F}^{\prime }\left( \frac{k}{n}\right) }\right\rbrack  .
\]

D’après la formule de Taylor-Lagrange, pour tout \( n \in {\mathbb{N}}^{ * } \) on a

> According to the Taylor-Lagrange formula, for all \( n \in {\mathbb{N}}^{ * } \) we have

\[
\forall k \in  \{ 1\ldots , n\} ,\exists {x}_{k} \in  \left\rbrack  {\frac{k - 1}{n},\frac{k}{n}}\right\lbrack  ,\;F\left( \frac{k - 1}{n}\right)  = F\left( \frac{k}{n}\right)  - \frac{1}{n}{F}^{\prime }\left( \frac{k}{n}\right)  + \frac{1}{2{n}^{2}}{F}^{\prime \prime }\left( {x}_{k}\right) ,
\]

et comme \( {F}^{\prime \prime } = {f}^{\prime } \) ceci entraîne

> and since \( {F}^{\prime \prime } = {f}^{\prime } \) this implies

\[
\ell  - {u}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\left\lbrack  {\frac{-1}{2{n}^{2}}{F}^{\prime \prime }\left( {x}_{k}\right) }\right\rbrack   =  - \frac{1}{2{n}^{2}}\mathop{\sum }\limits_{{k = 1}}^{n}{f}^{\prime }\left( {x}_{k}\right) .
\]

On a encore affaire à une somme de Riemann ; le théorème 7 donne

> We are still dealing with a Riemann sum; Theorem 7 gives

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}{f}^{\prime }\left( {x}_{k}\right)  = {\int }_{0}^{1}{f}^{\prime }\left( t\right) {dt} = f\left( 1\right)  - f\left( 0\right)  =  - \frac{1}{2},
\]

donc \( \ell - {u}_{n} \sim \frac{1}{4n} \) lorsque \( n \) tend vers \( + \infty \) .

> so \( \ell - {u}_{n} \sim \frac{1}{4n} \) as \( n \) tends to \( + \infty \) .

Remarque. On a montré, de manière plus générale, que pour toute fonction \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{1} \)

> Remark. We have shown, more generally, that for any function \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{1} \)

\[
{\int }_{0}^{1}f\left( t\right) {dt} = \mathop{\sum }\limits_{{k = 1}}^{n}f\left( \frac{k}{n}\right)  - \frac{1}{2n}\left( {f\left( 1\right)  - f\left( 0\right) }\right)  + o\left( \frac{1}{n}\right) .
\]

Lorsque la fonction \( f \) possède de bonnes propriétés de régularité, il est possible de pour-suivre ce développement asymptotique (voir le sujet d'étude 3 page 321 sur la formule d'Euler-Maclaurin).

> When the function \( f \) has good regularity properties, it is possible to continue this asymptotic expansion (see study topic 3 on page 321 regarding the Euler-Maclaurin formula).

EXERCICE 7 (INEGALITÉ DE YOUNG). Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction dérivable et strictement croissante telle que \( f\left( 0\right) = 0 \) .

> EXERCISE 7 (YOUNG'S INEQUALITY). Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a differentiable and strictly increasing function such that \( f\left( 0\right) = 0 \) .

a) Pour tout \( x > 0 \) , montrer

> a) For all \( x > 0 \) , show

\[
{\int }_{0}^{x}f\left( t\right) {dt} + {\int }_{0}^{f\left( x\right) }{f}^{-1}\left( t\right) {dt} = {xf}\left( x\right) .
\]

b) En déduire que

> b) Deduce that

\[
\forall a, b > 0,\;{\int }_{0}^{a}f\left( t\right) {dt} + {\int }_{0}^{b}{f}^{-1}\left( t\right) {dt} \geq  {ab},
\]

et que l’égalité se produit si et seulement si \( b = f\left( a\right) \) .

> and that equality occurs if and only if \( b = f\left( a\right) \) .

Solution. a) Cette égalité a une interprétation géométrique simple comme le montre la figure ci contre.

> Solution. a) This equality has a simple geometric interpretation as shown in the figure opposite.

![bo_d7fjkrs91nqc73ereoog_138_504_1419_566_390_0.jpg](images/gourdon_analysis_fr_en_009_bod7fjkrs91nqc73ereoog13850414195663900.jpg)

Figure 1. L’aire \( {xf}\left( x\right) \) du rectangle est la somme des surfaces des régions délimitées par ce rectangle et le graphe de \( f \) .

> Figure 1. The area \( {xf}\left( x\right) \) of the rectangle is the sum of the areas of the regions delimited by this rectangle and the graph of \( f \) .

On considère l'application

> Consider the mapping

\[
g : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{0}^{x}f\left( t\right) {dt} + {\int }_{0}^{f\left( x\right) }{f}^{-1}\left( t\right) {dt} - {xf}\left( x\right) .
\]

Cette application est dérivable, et

> This mapping is differentiable, and

\[
\forall x \geq  0,\;{g}^{\prime }\left( x\right)  = f\left( x\right)  + {f}^{\prime }\left( x\right) {f}^{-1}\left( {f\left( x\right) }\right)  - \left( {f\left( x\right)  + x{f}^{\prime }\left( x\right) }\right)  = 0.
\]

Donc \( g \) est constante, et comme \( g\left( 0\right) = 0 \) on en déduit que \( g \) est nulle, d’où le résultat.

> Thus \( g \) is constant, and since \( g\left( 0\right) = 0 \) we deduce that \( g \) is zero, hence the result.

b) On fixe \( b > 0 \) et on considère l’application

> b) Fix \( b > 0 \) and consider the mapping

\[
\varphi  : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R}\;a \mapsto  {\int }_{0}^{a}f\left( x\right) {dx} + {\int }_{0}^{b}{f}^{-1}\left( x\right) {dx} - {ab}.
\]

Cette application est dérivable, et \( {\varphi }^{\prime }\left( a\right) = f\left( a\right) - b \) pour tout \( a \in \mathbb{R} \) . Comme \( f \) est strictement croissante, on a donc

> This mapping is differentiable, and \( {\varphi }^{\prime }\left( a\right) = f\left( a\right) - b \) for all \( a \in \mathbb{R} \) . Since \( f \) is strictly increasing, we therefore have

\[
\forall a < {f}^{-1}\left( b\right) ,{\varphi }^{\prime }\left( a\right)  < 0\;\text{ et }\;\forall a > {f}^{-1}\left( b\right) ,{\varphi }^{\prime }\left( a\right)  > 0.
\]

Comme \( \varphi \left( {{f}^{-1}\left( b\right) }\right) = 0 \) d’après la question précédente, on déduit de tout ceci que

> As \( \varphi \left( {{f}^{-1}\left( b\right) }\right) = 0 \) from the previous question, we deduce from all this that

\[
\forall a < {f}^{-1}\left( b\right) ,\varphi \left( a\right)  > 0,\;\varphi \left( {{f}^{-1}\left( b\right) }\right)  = 0,\;\forall a > {f}^{-1}\left( b\right) ,\varphi \left( a\right)  > 0.
\]

On a donc démontré l’inégalité désirée, et l’égalité se produit si et seulement si \( a = {f}^{-1}\left( b\right) \) , c’est-à-dire \( b = f\left( a\right) \) , d’où le résultat.

> We have thus proven the desired inequality, and equality holds if and only if \( a = {f}^{-1}\left( b\right) \), that is to say \( b = f\left( a\right) \), hence the result.

EXERCICE 8. Démontrer que la seconde formule de la moyenne (théorème 6 page 128) reste vraie si l’on suppose uniquement \( f \) continue. Autrement dit, montrer que si \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) est une fonction continue, positive et décroissante, et si \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) est continue, alors il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que

> EXERCISE 8. Prove that the second mean value theorem (theorem 6 page 128) remains true if we only assume \( f \) is continuous. In other words, show that if \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is a continuous, positive, and decreasing function, and if \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is continuous, then there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that

\[
{\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} = f\left( a\right) {\int }_{a}^{c}g\left( t\right) {dt}.
\]

(on utilisera une transformation d'Abel à partir d'une expression approchant une somme de Riemann)

> (use an Abel transformation starting from an expression approximating a Riemann sum)

Solution. Nous démarrons comme dans la preuve du théorème 6. On considère l'application \( G : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto {\int }_{a}^{t}g\left( x\right) {dx} \) , continue sur \( \left\lbrack {a, b}\right\rbrack \) , ce qui assure l’existence des réels

> Solution. We start as in the proof of theorem 6. Consider the mapping \( G : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto {\int }_{a}^{t}g\left( x\right) {dx} \), continuous on \( \left\lbrack {a, b}\right\rbrack \), which ensures the existence of the real numbers

\[
m = \mathop{\inf }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}G\left( t\right) \;\text{ et }\;M = \mathop{\sup }\limits_{{t \in  \left\lbrack  {a, b}\right\rbrack  }}G\left( t\right) .
\]

On va montrer \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \) , ce qui prouvera le résultat en appliquant à \( G \) le théorème des valeurs intermédiaires.

> We will show \( {mf}\left( a\right) \leq {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq {Mf}\left( a\right) \), which will prove the result by applying the intermediate value theorem to \( G \).

L'idée est de remplacer l'intégration par parties utilisée dans la preuve du théorème 6 par une transformation d'Abel à partir d'une somme de Riemann. Par comparaison avec la formule

> The idea is to replace the integration by parts used in the proof of theorem 6 with an Abel transformation starting from a Riemann sum. By comparison with the formula

\[
{\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} = G\left( b\right) f\left( b\right)  - G\left( a\right) f\left( a\right)  - {\int }_{a}^{b}{f}^{\prime }\left( t\right) G\left( t\right) ,
\]

(valide uniquement lorsque \( f \) est \( {\mathcal{C}}^{1} \) ) on va écrire, pour une subdivision \( \sigma \) de pas suffisamment petit, avec \( \sigma : a = {a}_{0} < \cdots < {a}_{n} = b \) , une transformation d’Abel de la somme

> (valid only when \( f \) is \( {\mathcal{C}}^{1} \) ) we will write, for a subdivision \( \sigma \) with a sufficiently small mesh, with \( \sigma : a = {a}_{0} < \cdots < {a}_{n} = b \) , an Abel transformation of the sum

\[
I\left( \sigma \right)  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( {a}_{i}\right) \left( {G\left( {a}_{i + 1}\right)  - G\left( {a}_{i}\right) }\right) ,
\]

ce qui donne

> which gives

\[
I\left( \sigma \right)  = G\left( {a}_{n}\right) f\left( {a}_{n - 1}\right)  - G\left( {a}_{0}\right) f\left( {a}_{0}\right)  + \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {f\left( {a}_{i - 1}\right)  - f\left( {a}_{i}\right) }\right) G\left( {a}_{i}\right) .
\]

Comme \( G\left( {a}_{n}\right) f\left( {a}_{n - 1}\right) - G\left( {a}_{0}\right) f\left( {a}_{0}\right) = G\left( b\right) f\left( {a}_{n - 1}\right) \) , cette dernière identité entraîne, compte tenu de la décroissante de la fonction \( f \)

> As \( G\left( {a}_{n}\right) f\left( {a}_{n - 1}\right) - G\left( {a}_{0}\right) f\left( {a}_{0}\right) = G\left( b\right) f\left( {a}_{n - 1}\right) \) , this last identity implies, given the decreasing nature of the function \( f \)

\[
G\left( b\right) f\left( {a}_{n - 1}\right)  + \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {f\left( {a}_{i - 1}\right)  - f\left( {a}_{i}\right) }\right) m \leq  I\left( \sigma \right)  \leq  G\left( b\right) f\left( {a}_{n - 1}\right)  + \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {f\left( {a}_{i - 1}\right)  - f\left( {a}_{i}\right) }\right) M,
\]

c'est-à-dire

> that is to say

\[
G\left( b\right) f\left( {a}_{n - 1}\right)  + m\left( {f\left( {a}_{0}\right)  - f\left( {a}_{n - 1}\right) }\right)  \leq  I\left( \sigma \right)  \leq  G\left( b\right) f\left( {a}_{n - 1}\right)  + M\left( {f\left( {a}_{0}\right)  - f\left( {a}_{n - 1}\right) }\right)
\]

et comme \( f\left( {a}_{n - 1}\right) \geq 0 \) on en déduit

> and since \( f\left( {a}_{n - 1}\right) \geq 0 \) we deduce

\[
{mf}\left( a\right)  \leq  I\left( \sigma \right)  \leq  {Mf}\left( a\right) .
\]

(*)

> Maintenant nous allons approcher \( I\left( \sigma \right) \) par une somme de Riemann de \( {\int }_{a}^{b}{fg} \) . Soit \( \varepsilon > 0 \) . Comme \( g \) est continue sur un segment, elle y uniformément continue d’après le théorème de Heine, donc il existe \( \alpha > 0 \) tel que si \( \left| {x - y}\right| < \alpha \) , alors \( \left| {g\left( x\right) - g\left( y\right) }\right| < \varepsilon \) . Ensuite, le théorème sur les sommes de Riemann nous assure qu’on peut choisir la subdivision \( \left( \sigma \right) \) de pas \( \left| \sigma \right| < \alpha \) telle que \( \left| {S\left( \sigma \right) - {\int }_{a}^{b}{fg}}\right| < \varepsilon \) , où

Now we will approximate \( I\left( \sigma \right) \) by a Riemann sum of \( {\int }_{a}^{b}{fg} \) . Let \( \varepsilon > 0 \) . Since \( g \) is continuous on a segment, it is uniformly continuous there according to the Heine theorem, so there exists \( \alpha > 0 \) such that if \( \left| {x - y}\right| < \alpha \) , then \( \left| {g\left( x\right) - g\left( y\right) }\right| < \varepsilon \) . Next, the theorem on Riemann sums ensures that we can choose the subdivision \( \left( \sigma \right) \) with mesh \( \left| \sigma \right| < \alpha \) such that \( \left| {S\left( \sigma \right) - {\int }_{a}^{b}{fg}}\right| < \varepsilon \) , where

\[
S\left( \sigma \right)  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left( {{a}_{i + 1} - {a}_{i}}\right) f\left( {a}_{i}\right) g\left( {a}_{i}\right) .
\]

On écrit maintenant

> We now write

\[
\left| {I\left( \sigma \right)  - S\left( \sigma \right) }\right|  \leq  \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( {a}_{i}\right) \left| {G\left( {a}_{i + 1}\right)  - G\left( {a}_{i}\right)  - \left( {{a}_{i + 1} - {a}_{i}}\right) g\left( {a}_{i}\right) }\right|  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( {a}_{i}\right) \left| {{\int }_{{a}_{i}}^{{a}_{i + 1}}\left( {g\left( t\right)  - g\left( {a}_{i}\right) }\right) {dt}}\right|
\]

et le pas de la subdivision étant \( \left| \sigma \right| < \alpha \) , on a \( \left| {g\left( t\right) - g\left( {a}_{i}\right) }\right| < \varepsilon \) pour \( t \in \left\lbrack {{a}_{i},{a}_{i + 1}}\right\rbrack \) donc l’inégalité précédente entraîne

> and the mesh of the subdivision being \( \left| \sigma \right| < \alpha \) , we have \( \left| {g\left( t\right) - g\left( {a}_{i}\right) }\right| < \varepsilon \) for \( t \in \left\lbrack {{a}_{i},{a}_{i + 1}}\right\rbrack \) so the previous inequality implies

\[
\left| {I\left( \sigma \right)  - S\left( \sigma \right) }\right|  \leq  \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( {a}_{i}\right) \left( {{a}_{i + 1} - {a}_{i}}\right) \varepsilon  \leq  \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( a\right) \left( {{a}_{i + 1} - {a}_{i}}\right) \varepsilon  = \left( {b - a}\right) f\left( a\right) \varepsilon .
\]

On en déduit

> We deduce

\[
\left| {I\left( \sigma \right)  - {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt}}\right|  \leq  \left| {I\left( \sigma \right)  - S\left( \sigma \right) }\right|  + \left| {S\left( \sigma \right)  - {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt}}\right|  \leq  \left( {b - a}\right) f\left( a\right) \varepsilon  + \varepsilon ,
\]

et finalement, avec (*) on a

> and finally, with (*) we have

\[
{mf}\left( a\right)  - \left( {b - a}\right) f\left( a\right) \varepsilon  - \varepsilon  \leq  {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \leq  {Mf}\left( a\right)  + \left( {b - a}\right) f\left( a\right) \varepsilon  + \varepsilon .
\]

Cette inégalité étant vraie pour tout \( \varepsilon > 0 \) , on en déduit bien \( {mf}\left( a\right) \leq {\int }_{a}^{b}{fg} \leq {Mf}\left( b\right) \) , d’où le résultat.

> Since this inequality is true for all \( \varepsilon > 0 \) , we indeed deduce \( {mf}\left( a\right) \leq {\int }_{a}^{b}{fg} \leq {Mf}\left( b\right) \) , hence the result.

Remarque. - On aurait également pu se ramener au cas du théorème 6 page 128 en construisant une suite de fonctions \( \left( {f}_{n}\right) \) décroissantes positives de classe \( {\mathcal{C}}^{1} \) , qui converge uniformément vers \( f \) .

> Remark. - We could also have reduced it to the case of theorem 6 on page 128 by constructing a sequence of positive decreasing functions \( \left( {f}_{n}\right) \) of class \( {\mathcal{C}}^{1} \) , which converges uniformly to \( f \) .

- On peut démontrer que la seconde formule de la moyenne est encore vraie si on suppose seulement \( f \) et \( g \) Riemann-intégrables.

> - It can be shown that the second mean value theorem is still true if we only assume \( f \) and \( g \) are Riemann-integrable.
