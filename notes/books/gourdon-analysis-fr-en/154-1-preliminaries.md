### 1. Preliminaries

*Français : 1. Préliminaires*

Problems 1 (Propriétés de la fonction \( \zeta \left( s\right) \) ). 1/ (La fonction \( \zeta \left( s\right) \) ) On considère la fonction Zêta de Riemann, définie pour la variable complexe \( s \) par la série

> Problem 1 (Properties of the function \( \zeta \left( s\right) \)). 1/ (The function \( \zeta \left( s\right) \)) Consider the Riemann Zeta function, defined for the complex variable \( s \) by the series

\[
\zeta \left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}},\;s \in  D = \{ s \in  \mathbb{C} \mid  \Re \left( s\right)  > 1\}
\]

a) Montrer que cette série est bien définie pour \( s \in D \) et que \( \zeta \left( s\right) \) est continue sur \( D \) . Montrer de plus que pour \( s = \sigma + {it} \in D\left( {\sigma , t \in \mathbb{R}}\right) \) , on a \( \left| {\zeta \left( s\right) }\right| \leq \sigma /\left( {\sigma - 1}\right) \) . b) Pour tout \( N \in {\mathbb{N}}^{ * } \) , montrer que

> a) Show that this series is well-defined for \( s \in D \) and that \( \zeta \left( s\right) \) is continuous on \( D \). Furthermore, show that for \( s = \sigma + {it} \in D\left( {\sigma , t \in \mathbb{R}}\right) \), we have \( \left| {\zeta \left( s\right) }\right| \leq \sigma /\left( {\sigma - 1}\right) \). b) For all \( N \in {\mathbb{N}}^{ * } \), show that

\[
\forall s \in  D,\;\zeta \left( s\right)  - \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{s}} = s{\int }_{N}^{+\infty }\frac{1/2-\{ x\} }{{x}^{s + 1}}{dx} + \frac{{N}^{1 - s}}{s - 1} - \frac{{N}^{-s}}{2},
\]

(*)

> où \( \{ x\} = x - \left\lbrack x\right\rbrack \) désigne la partie fractionnaire de \( x \) .

where \( \{ x\} = x - \left\lbrack x\right\rbrack \) denotes the fractional part of \( x \).

> c) Montrer que \( \zeta \left( s\right) \) est prolongeable en une fonction continue sur \( \bar{D} \smallsetminus \{ 1\} \) , où \( \bar{D} = \{ s \in \; \mathbb{C} \mid \Re \left( s\right) \geq 1\} \) , et qu’il existe une fonction \( \eta \left( s\right) \) continue sur \( \bar{D} \) tout entier tel que

c) Show that \( \zeta \left( s\right) \) can be extended to a continuous function on \( \bar{D} \smallsetminus \{ 1\} \), where \( \bar{D} = \{ s \in \; \mathbb{C} \mid \Re \left( s\right) \geq 1\} \), and that there exists a function \( \eta \left( s\right) \) continuous on the entire \( \bar{D} \) such that

\[
\forall s \in  \bar{D} \smallsetminus  \{ 1\} ,\;\zeta \left( s\right)  = \eta \left( s\right)  + \frac{1}{s - 1}.
\]

d) Pour une fonction \( s \mapsto f\left( s\right) \) de la variable complexe \( s = \sigma + {i\tau }\left( {\sigma ,\tau \in \mathbb{R}}\right) \) , on désigne par \( {f}^{\prime }\left( s\right) \) la dérivée en \( x = \sigma \) de la fonction \( x \mapsto f\left( {x + {i\tau }}\right) \) (nous n’aurons pas besoin du cadre, généralement utilisé, de la dérivée par rapport à la variable complexe \( s \) de \( f\left( s\right) \) ). Montrer que \( {\zeta }^{\prime }\left( s\right) \) existe et est continue sur \( \bar{D} \smallsetminus \{ 1\} \) et que la fonction \( {\eta }^{\prime }\left( s\right) \) est même définie et continue sur \( \bar{D} \) tout entier.

> d) For a function \( s \mapsto f\left( s\right) \) of the complex variable \( s = \sigma + {i\tau }\left( {\sigma ,\tau \in \mathbb{R}}\right) \), we denote by \( {f}^{\prime }\left( s\right) \) the derivative at \( x = \sigma \) of the function \( x \mapsto f\left( {x + {i\tau }}\right) \) (we will not need the framework, generally used, of the derivative with respect to the complex variable \( s \) of \( f\left( s\right) \)). Show that \( {\zeta }^{\prime }\left( s\right) \) exists and is continuous on \( \bar{D} \smallsetminus \{ 1\} \) and that the function \( {\eta }^{\prime }\left( s\right) \) is even defined and continuous on the entire \( \bar{D} \).

2/ a) En désignant par \( {p}_{k} \) le \( k \) -ième nombre premier, montrer l’identité d’Euler

> 2/ a) Denoting by \( {p}_{k} \) the \( k \)-th prime number, show Euler's identity

\[
\forall s \in  D,\;\zeta \left( s\right)  = \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}\left( \frac{1}{1 - {p}_{k}^{-s}}\right) \;\left( \right. \text{ on rappelle que }\mathop{\prod }\limits_{{k = 1}}^{\infty } = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\mathop{\prod }\limits_{{k = 1}}^{n}).
\]

b) En déduire que pour tout \( s \in D \) , on a \( \zeta \left( s\right) \neq 0 \) .

> b) Deduce that for all \( s \in D \), we have \( \zeta \left( s\right) \neq 0 \).

c) On considère la série définie pour \( s \in D \) par

> c) Consider the series defined for \( s \in D \) by

\[
Z\left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\Lambda \left( n\right) }{{n}^{s}},\;\Lambda \left( n\right)  = \left\{  \begin{array}{ll} \log p & \text{ si }\exists k \in  {\mathbb{N}}^{ * } : n = {p}^{k}\text{ avec }p\text{ premier } \\  0 & \text{ sinon. } \end{array}\right.
\]

( \( \Lambda \left( n\right) \) s’appelle la fonction de Mangoldt). Montrer l’identité \( \zeta \left( s\right) Z\left( s\right) = - {\zeta }^{\prime }\left( s\right) \) pour tout \( s \in D \) .

> (\( \Lambda \left( n\right) \) is called the Mangoldt function). Show the identity \( \zeta \left( s\right) Z\left( s\right) = - {\zeta }^{\prime }\left( s\right) \) for all \( s \in D \).

3 / a) Montrer l’existence de \( {M}_{0} > 0 \) et de \( {M}_{1} > 0 \) tels que

> 3 / a) Show the existence of \( {M}_{0} > 0 \) and \( {M}_{1} > 0 \) such that

\[
\forall \sigma  \in  \left\lbrack  {1,2}\right\rbrack  ,\forall t \in  \mathbb{R},\left| t\right|  \geq  2,\;\left| {\zeta \left( {\sigma  + {it}}\right) }\right|  \leq  {M}_{0}\log \left| t\right| ,\;\left| {{\zeta }^{\prime }\left( {\sigma  + {it}}\right) }\right|  \leq  {M}_{1}{\log }^{2}\left| t\right|
\]

b) Montrer que si \( p > 1 \) ,

> b) Show that if \( p > 1 \),

\[
\forall s \in  D,\;s = \sigma  + {i\tau },\;\log \left| {1 - {p}^{-s}}\right|  =  - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\cos \left( {{n\tau }\log p}\right) }{n{p}^{n\sigma }}.
\]

\( \left( {* * }\right) \)

> Après avoir montré \( 3 + 4\cos \theta + \cos {2\theta } \geq 0 \) pour \( \theta \in \mathbb{R} \) , démontrer ensuite l’inégalité

After showing \( 3 + 4\cos \theta + \cos {2\theta } \geq 0 \) for \( \theta \in \mathbb{R} \), then prove the inequality

\[
\forall \sigma  > 1,\forall \tau  \in  \mathbb{R},\;{\left| \zeta \left( \sigma \right) \right| }^{3}{\left| \zeta \left( \sigma  + i\tau \right) \right| }^{4}\left| {\zeta \left( {\sigma  + {2i\tau }}\right) }\right|  \geq  1.
\]

c) En déduire que \( \zeta \left( s\right) \) ne s’annule pas sur \( \bar{D} \smallsetminus \{ 1\} \) . Montrer ensuite l’existence de \( {m}_{0} > 0 \) tel que

> c) Deduce that \( \zeta \left( s\right) \) does not vanish on \( \bar{D} \smallsetminus \{ 1\} \). Then show the existence of \( {m}_{0} > 0 \) such that

\[
\forall \sigma  \in  \left\lbrack  {1,2}\right\rbrack  ,\forall t \in  \mathbb{R},\left| t\right|  \geq  2,\;\left| {\zeta \left( {\sigma  + {it}}\right) }\right|  \geq  \frac{{m}_{0}}{{\log }^{7}\left| t\right| }
\]

(considérer séparément les cas \( \sigma \geq {\sigma }_{t} = 1 + \varepsilon /{\log }^{9}\left| t\right| \) et \( 1 \leq \sigma < {\sigma }_{t} \) . Pour ce dernier, utiliser 3/b) et l’inégalité \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \geq \left| {\zeta \left( {{\sigma }_{t} + {it}}\right) }\right| - {\int }_{\sigma }^{{\sigma }_{t}}\left| {{\zeta }^{\prime }\left( {x + {it}}\right) }\right| {dx} \) ).

> (consider the cases \( \sigma \geq {\sigma }_{t} = 1 + \varepsilon /{\log }^{9}\left| t\right| \) and \( 1 \leq \sigma < {\sigma }_{t} \) separately. For the latter, use 3/b) and the inequality \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \geq \left| {\zeta \left( {{\sigma }_{t} + {it}}\right) }\right| - {\int }_{\sigma }^{{\sigma }_{t}}\left| {{\zeta }^{\prime }\left( {x + {it}}\right) }\right| {dx} \)).

d) Montrer que la fonction \( F\left( s\right) = \zeta \left( s\right) - Z\left( s\right) \) est prolongeable en une fonction continue sur \( \bar{D} \) tout entier, et qu’il existe \( {M}_{F} > 0 \) et \( A > 0 \) tels que

> d) Show that the function \( F\left( s\right) = \zeta \left( s\right) - Z\left( s\right) \) can be extended to a continuous function on the entire \( \bar{D} \), and that there exist \( {M}_{F} > 0 \) and \( A > 0 \) such that

\[
\forall \sigma , t : 1 \leq  \sigma  \leq  2,\left| t\right|  \geq  A,\;\left| {F\left( {\sigma  + {it}}\right) }\right|  \leq  {M}_{F}{\log }^{9}\left| t\right| .
\]

c) L'identité précédente utilisée avec \( N = 1 \) donne

> c) The previous identity used with \( N = 1 \) gives

\[
\forall s \in  D,\;\eta \left( s\right)  = \zeta \left( s\right)  - \frac{1}{s - 1} = \frac{1}{2} + s{\int }_{1}^{+\infty }\frac{1/2-\{ x\} }{{x}^{s + 1}}{dx}.
\]

(***)

---

Solution. 1/ a) Pour \( \sigma > 1 \) , notons \( {D}_{\sigma } = \{ z \in \mathbb{C} \mid \Re \left( z\right) \geq \sigma \} \) . Pour \( s \in {D}_{\sigma } \) avec \( \sigma > 1 \) , on a \( \left| {1/{n}^{s}}\right| \leq 1/{n}^{\sigma } \) , donc la série converge normalement sur \( {D}_{\sigma } \) . Ainsi, \( \zeta \left( s\right) \) est bien définie et continue sur \( {D}_{\sigma } \) , et ceci est vrai pour tout \( \sigma > 1 \) donc \( \zeta \left( s\right) \) est bien définie et continue sur \( D \) . L’inégalité \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq \sigma /\left( {\sigma - 1}\right) \) s’obtient en écrivant

> Solution. 1/ a) For \( \sigma > 1 \), let us denote \( {D}_{\sigma } = \{ z \in \mathbb{C} \mid \Re \left( z\right) \geq \sigma \} \). For \( s \in {D}_{\sigma } \) with \( \sigma > 1 \), we have \( \left| {1/{n}^{s}}\right| \leq 1/{n}^{\sigma } \), so the series converges normally on \( {D}_{\sigma } \). Thus, \( \zeta \left( s\right) \) is well-defined and continuous on \( {D}_{\sigma } \), and this is true for all \( \sigma > 1 \) so \( \zeta \left( s\right) \) is well-defined and continuous on \( D \). The inequality \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq \sigma /\left( {\sigma - 1}\right) \) is obtained by writing

\[
\left| {\zeta \left( {\sigma  + {it}}\right) }\right|  \leq  1 + \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\frac{1}{{n}^{\sigma }} \leq  1 + \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}{\int }_{n - 1}^{n}\frac{dt}{{t}^{\sigma }} = 1 + {\int }_{1}^{+\infty }\frac{dt}{{t}^{\sigma }} = 1 + \frac{1}{\sigma  - 1} = \frac{\sigma }{\sigma  - 1}.
\]

b) Une intégration par parties donne l’égalité, pour \( n \in {\mathbb{N}}^{ * } \) et \( s \in D \)

> b) Integration by parts gives the equality, for \( n \in {\mathbb{N}}^{ * } \) and \( s \in D \)

\[
s{\int }_{n}^{n + 1}\frac{1/2 - x + n}{{x}^{s + 1}}{dx} = {\left\lbrack  -\frac{1/2 - x + n}{{x}^{s}}\right\rbrack  }_{n}^{n + 1} - {\int }_{n}^{n + 1}\frac{dx}{{x}^{s}} = \frac{1}{2{\left( n + 1\right) }^{s}} + \frac{1}{2{n}^{s}} - {\int }_{n}^{n + 1}\frac{dx}{{x}^{s}}.
\]

Par sommation pour \( n \) allant de \( N \) à \( + \infty \) on obtient

> By summation for \( n \) ranging from \( N \) to \( + \infty \) we obtain

\[
s{\int }_{N}^{+\infty }\frac{1/2-\{ x\} }{{x}^{s + 1}}{dx} = \mathop{\sum }\limits_{{n = N}}^{{+\infty }}\left( {\frac{1}{2{n}^{s}} + \frac{1}{2{\left( n + 1\right) }^{s}}}\right)  - {\int }_{N}^{+\infty }\frac{dx}{{x}^{s}} = \zeta \left( s\right)  - \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{s}} + \frac{1}{2{N}^{s}} - \frac{{N}^{1 - s}}{s - 1}.
\]

---

L’intégrande de la dernière intégrale est continue par rapport à \( s \) sur \( \bar{D} \) et elle est majorée en valeur absolue sur \( \bar{D} \) par \( x \mapsto 1/\left( {2{x}^{2}}\right) \) , intégrable sur \( \lbrack 1, + \infty \lbrack \) . Donc l’intégrale est une fonction continue de \( s \) sur \( \bar{D} \) et \( \eta \left( s\right) \) est bien prolongeable en une fonction continue sur \( \bar{D} \) , d’où le résultat.

> The integrand of the last integral is continuous with respect to \( s \) on \( \bar{D} \) and is bounded in absolute value on \( \bar{D} \) by \( x \mapsto 1/\left( {2{x}^{2}}\right) \), which is integrable on \( \lbrack 1, + \infty \lbrack \). Therefore, the integral is a continuous function of \( s \) on \( \bar{D} \) and \( \eta \left( s\right) \) can indeed be extended to a continuous function on \( \bar{D} \), hence the result.

d) Il suffit de montrer que \( {\eta }^{\prime }\left( s\right) \) existe et est continue sur \( \bar{D} \) . Soit \( s = \sigma + {it} \in \bar{D} \) . Dans l’intégrale de l’expression (***) de \( \eta \left( s\right) \) , l’intégrande \( \left( {1/2-\{ x\} }\right) /{x}^{\sigma + 1 + {it}} \) est continûment dérivable par rapport à \( \sigma \) , sa dérivée est \( - \left( {1/2-\{ x\} }\right) \log x/\left( {x}^{\sigma + 1 + {it}}\right) \) qui est majorée en valeur absolue par \( \log x/{x}^{2} \) lorsque \( s = \sigma + {it} \in \bar{D} \) . Cette dernière fonction est intégrable sur \( \lbrack 1, + \infty \lbrack \) , l’hypothèse de domination est donc vérifiée. On en déduit que \( {\eta }^{\prime }\left( s\right) \) existe et est continue sur \( \bar{D} \) .

> d) It suffices to show that \( {\eta }^{\prime }\left( s\right) \) exists and is continuous on \( \bar{D} \). Let \( s = \sigma + {it} \in \bar{D} \). In the integral of expression (***) from \( \eta \left( s\right) \), the integrand \( \left( {1/2-\{ x\} }\right) /{x}^{\sigma + 1 + {it}} \) is continuously differentiable with respect to \( \sigma \), its derivative is \( - \left( {1/2-\{ x\} }\right) \log x/\left( {x}^{\sigma + 1 + {it}}\right) \), which is bounded in absolute value by \( \log x/{x}^{2} \) when \( s = \sigma + {it} \in \bar{D} \). This latter function is integrable on \( \lbrack 1, + \infty \lbrack \), so the domination hypothesis is satisfied. We deduce that \( {\eta }^{\prime }\left( s\right) \) exists and is continuous on \( \bar{D} \).

2 / a) On remarque déjà que pour tout \( k \) et pour tout \( s \in D,{\left( 1 - {p}_{k}^{-s}\right) }^{-1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{p}_{k}^{-{ns}} \) .

> 2 / a) We first note that for all \( k \) and for all \( s \in D,{\left( 1 - {p}_{k}^{-s}\right) }^{-1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{p}_{k}^{-{ns}} \).

Fixons \( m, M \in {\mathbb{N}}^{ * } \) . Pour tout \( s = \sigma + {it} \in D \) , l’unicité de la décomposition d’un entier en facteurs premiers implique

> Let us fix \( m, M \in {\mathbb{N}}^{ * } \). For all \( s = \sigma + {it} \in D \), the uniqueness of the prime factorization of an integer implies

\[
\mathop{\prod }\limits_{{k = 1}}^{m}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{M}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right)  = \mathop{\sum }\limits_{{0 \leq  {i}_{1},\ldots ,{i}_{m} \leq  M}}\frac{1}{{\left( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}}\right) }^{s}} = \mathop{\sum }\limits_{{n \in  {\mathcal{F}}_{m, M}}}\frac{1}{{n}^{s}},
\]

où \( {\mathcal{F}}_{m, M} \) désigne l’ensemble des entiers \( n \in {\mathbb{N}}^{ * } \) de la forme \( n = {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}} \) avec \( 0 \leq {i}_{k} \leq M \) . Maintenant, donnons nous \( N \in {\mathbb{N}}^{ * } \) . Soit \( {p}_{{m}_{0}} \) le plus grand nombre premier \( {p}_{i} \) et \( {M}_{0} \) la plus grande des puissances \( {i}_{k} \) apparaissant dans toutes les décompositions en facteurs premiers des \( N \) premiers entiers \( 1,\ldots , N \) . Considérons \( m \geq {m}_{0} \) et \( M \geq {M}_{0} \) . Tous les entiers compris entre 1 et \( N \) sont dans \( {\mathcal{F}}_{m, M} \) donc

> where \( {\mathcal{F}}_{m, M} \) denotes the set of integers \( n \in {\mathbb{N}}^{ * } \) of the form \( n = {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}} \) with \( 0 \leq {i}_{k} \leq M \). Now, let us choose \( N \in {\mathbb{N}}^{ * } \). Let \( {p}_{{m}_{0}} \) be the largest prime number \( {p}_{i} \) and \( {M}_{0} \) be the largest of the powers \( {i}_{k} \) appearing in all prime factorizations of the first \( N \) integers \( 1,\ldots , N \). Consider \( m \geq {m}_{0} \) and \( M \geq {M}_{0} \). All integers between 1 and \( N \) are in \( {\mathcal{F}}_{m, M} \) therefore

\[
\left| {\zeta \left( s\right)  - \mathop{\prod }\limits_{{k = 1}}^{m}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{M}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right) }\right|  = \left| {\mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }, n \notin  {\mathcal{F}}_{m, M}}}\frac{1}{{n}^{s}}}\right|  \leq  \mathop{\sum }\limits_{{n > N}}\frac{1}{{n}^{\sigma }}.
\]

Cette expression est valable pour tout \( M \geq {M}_{0} \) . En faisant tendre \( M \) vers \( + \infty \) , on en déduit

> This expression is valid for all \( M \geq {M}_{0} \). By letting \( M \) tend towards \( + \infty \), we deduce

\[
\left| {\zeta \left( s\right)  - \mathop{\prod }\limits_{{k = 1}}^{m}\frac{1}{1 - {p}_{k}^{-s}}}\right|  = \left| {\zeta \left( s\right)  - \mathop{\prod }\limits_{{k = 1}}^{m}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{{+\infty }}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right) }\right|  \leq  \mathop{\sum }\limits_{{n > N}}\frac{1}{{n}^{\sigma }}.
\]

Comme on peut choisir \( N \) pour rendre \( \mathop{\sum }\limits_{{n > N}}1/{n}^{\sigma } \) arbitrairement petit pour \( \sigma \geq {\sigma }_{0} > 1 \) et que l’inégalité précédente vaut pour tout \( m \geq {m}_{0} \) , on en déduit que le produit infini de l’identité d’Euler converge uniformément vers \( \zeta \left( s\right) \) sur \( {D}_{{\sigma }_{0}} \) dès que \( {\sigma }_{0} > 1 \) . Ceci étant vrai pour tout \( {\sigma }_{0} > 1 \) on en déduit que l’identité d’Euler vaut sur \( D \) tout entier.

> As we can choose \( N \) to make \( \mathop{\sum }\limits_{{n > N}}1/{n}^{\sigma } \) arbitrarily small for \( \sigma \geq {\sigma }_{0} > 1 \) and the previous inequality holds for all \( m \geq {m}_{0} \) , we deduce that the infinite product of Euler's identity converges uniformly to \( \zeta \left( s\right) \) on \( {D}_{{\sigma }_{0}} \) as soon as \( {\sigma }_{0} > 1 \) . Since this is true for all \( {\sigma }_{0} > 1 \) , we deduce that Euler's identity holds on the entire \( D \) .

b) Fixons \( s = \sigma + {it} \in D \) . Remarquons d’abord que \( 1 - {p}_{k}^{-s} \) est non nul pour tout \( k \) et que

> b) Let us fix \( s = \sigma + {it} \in D \) . First, note that \( 1 - {p}_{k}^{-s} \) is non-zero for all \( k \) and that

\[
1 - {p}_{k}^{-\sigma } \leq  \left| {1 - {p}_{k}^{-s}}\right|  \leq  1 + {p}_{k}^{-\sigma }\;\text{ donc }\;\log \left( {1 - {p}_{k}^{-\sigma }}\right)  \leq  \log \left| {1 - {p}_{k}^{-s}}\right|  \leq  \log \left( {1 + {p}_{k}^{-\sigma }}\right) .
\]

On en déduit, lorsque \( k \rightarrow \infty \) , l’estimation \( \log \left| {1 - {p}_{k}^{-s}}\right| = O\left( {p}_{k}^{-\sigma }\right) = O\left( {k}^{-\sigma }\right) \) , donc la série \( \sum \log \left| {1 - {p}_{k}^{-s}}\right| \) converge. Si on note \( \ell \) sa limite, ceci signifie que \( \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}1/\left| {1 - {p}_{k}^{-s}}\right| = \exp \left( {-\ell }\right) \) est non nul. On en déduit que \( \zeta \left( s\right) \neq 0 \) d’après l’identité d’Euler.

> We deduce, when \( k \rightarrow \infty \) , the estimate \( \log \left| {1 - {p}_{k}^{-s}}\right| = O\left( {p}_{k}^{-\sigma }\right) = O\left( {k}^{-\sigma }\right) \) , therefore the series \( \sum \log \left| {1 - {p}_{k}^{-s}}\right| \) converges. If we denote its limit by \( \ell \) , this means that \( \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}1/\left| {1 - {p}_{k}^{-s}}\right| = \exp \left( {-\ell }\right) \) is non-zero. We deduce that \( \zeta \left( s\right) \neq 0 \) according to Euler's identity.

c) Pour \( \sigma > 1 \) fixé et \( s \in {D}_{\sigma } \) , la majoration \( \left| {\Lambda \left( n\right) /{n}^{s}}\right| \leq \log n/{n}^{\sigma } \) montre que la série \( \sum \Lambda \left( n\right) /{n}^{s} \) converge normalement sur ce domaine. On peut même écrire

> c) For fixed \( \sigma > 1 \) and \( s \in {D}_{\sigma } \) , the bound \( \left| {\Lambda \left( n\right) /{n}^{s}}\right| \leq \log n/{n}^{\sigma } \) shows that the series \( \sum \Lambda \left( n\right) /{n}^{s} \) converges normally on this domain. We can even write

\[
Z\left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\Lambda \left( n\right) }{{n}^{s}} = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\mathop{\sum }\limits_{{j = 1}}^{{+\infty }}\frac{\log {p}_{k}}{{\left( {p}_{k}^{j}\right) }^{s}} = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{p}_{k}^{-s}\log {p}_{k}}{1 - {p}_{k}^{-s}},
\]

et cette dernière série converge normalement vers \( Z\left( s\right) \) sur \( {D}_{\sigma } \) .

> and this last series converges normally to \( Z\left( s\right) \) on \( {D}_{\sigma } \) .

On considère maintenant pour tout \( n \in {\mathbb{N}}^{ * } \) , le produit fini

> We now consider for all \( n \in {\mathbb{N}}^{ * } \) , the finite product

\[
{P}_{n}\left( s\right)  = \mathop{\prod }\limits_{{k = 1}}^{n}\frac{1}{1 - {p}_{k}^{-s}}
\]

dont la dérivée vérifie

> whose derivative satisfies

\[
{P}_{n}^{\prime }\left( s\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}\left( {\mathop{\prod }\limits_{\substack{{1 \leq  k \leq  n} \\  {k \neq  j} }}\frac{1}{1 - {p}_{k}^{-s}}}\right) \frac{\left( -{p}_{j}^{-s}\log {p}_{j}\right) }{{\left( 1 - {p}_{j}^{-s}\right) }^{2}} =  - {P}_{n}\left( s\right) \mathop{\sum }\limits_{{j = 1}}^{n}\frac{{p}_{j}^{-s}\log {p}_{j}}{1 - {p}_{j}^{-s}}.
\]

Nous avons vu plus haut que pour \( \sigma > 1 \) fixé, la série \( \mathop{\sum }\limits_{j}{p}_{j}^{-s}\log {p}_{j}/\left( {1 - {p}_{j}^{-s}}\right) \) converge normale-ment sur \( {D}_{\sigma } \) . Comme de plus \( {P}_{n}\left( s\right) \) converge uniformément vers \( \zeta \left( s\right) \) sur \( {D}_{\sigma } \) (voir \( 2/a)) \) et que \( \left| {\zeta \left( s\right) }\right| \leq \sigma /\left( {1 - \sigma }\right) \) est bornée sur ce domaine, on en déduit que \( {P}_{n}^{\prime }\left( s\right) \) converge uniformément sur \( {D}_{\sigma } \) , donc forcément vers \( {\zeta }^{\prime }\left( s\right) \) . En faisant tendre \( n \) vers l’infini dans la dernière identité on obtient

> We have seen above that for fixed \( \sigma > 1 \) , the series \( \mathop{\sum }\limits_{j}{p}_{j}^{-s}\log {p}_{j}/\left( {1 - {p}_{j}^{-s}}\right) \) converges normally on \( {D}_{\sigma } \) . Since, moreover, \( {P}_{n}\left( s\right) \) converges uniformly to \( \zeta \left( s\right) \) on \( {D}_{\sigma } \) (see \( 2/a)) \) ) and \( \left| {\zeta \left( s\right) }\right| \leq \sigma /\left( {1 - \sigma }\right) \) is bounded on this domain, we deduce that \( {P}_{n}^{\prime }\left( s\right) \) converges uniformly on \( {D}_{\sigma } \) , and therefore necessarily to \( {\zeta }^{\prime }\left( s\right) \) . By letting \( n \) tend to infinity in the last identity, we obtain

\[
{\zeta }^{\prime }\left( s\right)  =  - \zeta \left( s\right) \mathop{\sum }\limits_{{j = 1}}^{{+\infty }}\frac{{p}_{j}^{-s}\log {p}_{j}}{1 - {p}_{j}^{-s}} =  - \zeta \left( s\right) Z\left( s\right) .
\]

3/a) Commençons par montrer l’estimation sur \( \zeta \left( {\sigma + {it}}\right) \) , pour \( 1 \leq \sigma \leq 2 \) et \( \left| t\right| \geq 2 \) . L’identité (*) entraîne

> 3/a) Let us begin by showing the estimate on \( \zeta \left( {\sigma + {it}}\right) \) , for \( 1 \leq \sigma \leq 2 \) and \( \left| t\right| \geq 2 \) . Identity (*) implies

\[
\left| {\zeta \left( s\right) }\right|  \leq  \mathop{\sum }\limits_{{n = 1}}^{N}\left| \frac{1}{{n}^{s}}\right|  + \left| s\right| {\int }_{N}^{+\infty }\left| \frac{1}{2{x}^{s + 1}}\right| {dx} + \left| \frac{{N}^{1 - s}}{s - 1}\right|  + \left| \frac{{N}^{-s}}{2}\right|
\]

\[
\leq  \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n} + \left| s\right| {\int }_{N}^{+\infty }\frac{1}{2{x}^{2}}{dx} + \left| \frac{1}{s - 1}\right|  + \frac{1}{2} \leq  \left( {1 + \log N}\right)  + \frac{\left| s\right| }{2N} + 1.
\]

En choisissant \( N = \left\lbrack \left| t\right| \right\rbrack + 1 \) , on en déduit \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq 2 + \log \left( {\left| t\right| + 1}\right) + 2\left| t\right| /{2N} \leq 4 + \log \left| t\right| \) . Ainsi, on a montré \( \zeta \left( {\sigma + {it}}\right) = O\left( {\log \left| t\right| }\right) \) uniformément pour \( 1 \leq \sigma \leq 2 \) et \( \left| t\right| \geq 2 \) , d’où la première estimation.

> By choosing \( N = \left\lbrack \left| t\right| \right\rbrack + 1 \), we deduce \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq 2 + \log \left( {\left| t\right| + 1}\right) + 2\left| t\right| /{2N} \leq 4 + \log \left| t\right| \). Thus, we have shown \( \zeta \left( {\sigma + {it}}\right) = O\left( {\log \left| t\right| }\right) \) uniformly for \( 1 \leq \sigma \leq 2 \) and \( \left| t\right| \geq 2 \), which gives the first estimate.

On s’y prend de manière similaire pour l’estimation de \( {\zeta }^{\prime }\left( s\right) \) . On commence par dériver l'identité (*) (nous avions montré que nous pouvions bien dériver sous le signe intégral en \( 1/d \) )), ce qui donne, pour tout \( N \in {\mathbb{N}}^{ * } \)

> We proceed similarly for the estimation of \( {\zeta }^{\prime }\left( s\right) \). We begin by differentiating the identity (*) (we had shown that we could indeed differentiate under the integral sign in \( 1/d \)), which gives, for all \( N \in {\mathbb{N}}^{ * } \)

\[
{\zeta }^{\prime }\left( s\right)  =  - \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\log n}{{n}^{s}} + {\int }_{N}^{+\infty }\frac{1/2-\{ x\} }{{x}^{s + 1}}\left( {1 - s\log x}\right) {dx} - \frac{{N}^{1 - s}\log N}{s - 1} - \frac{{N}^{1 - s}}{{\left( s - 1\right) }^{2}} + \frac{{N}^{-s}\log N}{2}.
\]

Lorsque \( s = \sigma + {it} \) avec \( 1 \leq \sigma \leq 2 \) et \( \left| t\right| \geq 2 \) , l’expression précédente donne la majoration

> When \( s = \sigma + {it} \) with \( 1 \leq \sigma \leq 2 \) and \( \left| t\right| \geq 2 \), the previous expression gives the upper bound

\[
\left| {{\zeta }^{\prime }\left( s\right) }\right|  \leq  \mathop{\sum }\limits_{{n = 2}}^{N}\frac{\log n}{n} + {\int }_{N}^{+\infty }\frac{1 + \left| s\right| \log x}{2{x}^{2}}{dx} + \frac{\log N}{2} + \frac{1}{4} + \frac{\log N}{2N}
\]

\[
\leq  {\int }_{1}^{N}\frac{\log x}{x}{dx} + \frac{1}{2N} + \frac{\left| s\right| }{2}{\int }_{N}^{+\infty }\frac{\log x}{{x}^{2}}{dx} + \log N + \frac{1}{4}.
\]

Or \( {\int }_{1}^{N}\log x/{xdx} = \frac{1}{2}{\log }^{2}N \) et \( {\int }_{N}^{+\infty }\log x/{x}^{2}{dx} = \left( {1 + \log N}\right) /N \) , donc finalement

> However, \( {\int }_{1}^{N}\log x/{xdx} = \frac{1}{2}{\log }^{2}N \) and \( {\int }_{N}^{+\infty }\log x/{x}^{2}{dx} = \left( {1 + \log N}\right) /N \), so finally

\[
\left| {{\zeta }^{\prime }\left( s\right) }\right|  \leq  \frac{{\log }^{2}N}{2} + \frac{1}{2N} + \frac{\left| s\right| }{2}\frac{1 + \log N}{N} + \log N + \frac{1}{2}.
\]

En choisissant \( N = \left\lbrack \left| t\right| \right\rbrack + 1 \) , on voit que ceci entraîne \( \left| {{\zeta }^{\prime }\left( s\right) }\right| = O\left( {{\log }^{2}\left| t\right| }\right) \) uniformément pour \( 1 \leq \sigma \leq 2 \) .

> By choosing \( N = \left\lbrack \left| t\right| \right\rbrack + 1 \), we see that this implies \( \left| {{\zeta }^{\prime }\left( s\right) }\right| = O\left( {{\log }^{2}\left| t\right| }\right) \) uniformly for \( 1 \leq \sigma \leq 2 \).

b) La première identité est tout simplement une conséquence de la définition du logarithme complexe, mais cette notion n'est pas aux programmes des classes préparatoires. On s'en tire autrement. Fixons \( \theta \in \mathbb{R} \) et considérons la série entière \( {f}_{\theta }\left( x\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\cos \left( {n\theta }\right) {x}^{n}/n \) , dont le rayon de convergence est \( R = 1 \) . Sa dérivée se calcule explicitement

> b) The first identity is simply a consequence of the definition of the complex logarithm, but this notion is not in the preparatory classes curriculum. We get around it differently. Let us fix \( \theta \in \mathbb{R} \) and consider the power series \( {f}_{\theta }\left( x\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\cos \left( {n\theta }\right) {x}^{n}/n \), whose radius of convergence is \( R = 1 \). Its derivative is calculated explicitly

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;{f}_{\theta }^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\cos \left( {n\theta }\right) {x}^{n - 1} = \Re \left( \frac{{e}^{i\theta }}{1 - x{e}^{i\theta }}\right)  = \frac{\cos \theta  - x}{1 - {2x}\cos \theta  + {x}^{2}}.}\right.
\]

Ainsi, comme \( {f}_{\theta }\left( 0\right) = 0 \) , on a

> Thus, since \( {f}_{\theta }\left( 0\right) = 0 \), we have

\[
{f}_{\theta }\left( x\right)  = {\int }_{0}^{x}{f}_{\theta }^{\prime }\left( t\right) {dt} = {\int }_{0}^{x}\frac{\cos \theta  - t}{1 - {2t}\cos \theta  + {t}^{2}}{dt} =  - \frac{1}{2}\log \left( {1 - {2x}\cos \theta  + {x}^{2}}\right)  =  - \log \left| {1 - x{e}^{i\theta }}\right| .
\]

On en déduit l’identité (**) en choisissant \( x = {p}^{-\sigma } \) et \( \theta = \tau \log p \) .

> We deduce the identity (**) by choosing \( x = {p}^{-\sigma } \) and \( \theta = \tau \log p \).

Comme \( 3 + 4\cos \theta + \cos {2\theta } = 2{\left( 1 + \cos \theta \right) }^{2} \) , la première expression est toujours positive pour \( \theta \in \mathbb{R} \) . Ceci entraîne, lorsque \( p \) est un nombre premier et \( \sigma > 1 \) , que l’expression

> Since \( 3 + 4\cos \theta + \cos {2\theta } = 2{\left( 1 + \cos \theta \right) }^{2} \), the first expression is always positive for \( \theta \in \mathbb{R} \). This implies, when \( p \) is a prime number and \( \sigma > 1 \), that the expression

\[
3\log \left| {1 - {p}^{-\sigma }}\right|  + 4\log \left| {1 - {p}^{-\sigma  - {i\tau }}}\right|  + \log \left| {1 - {p}^{-\sigma  - {2i\tau }}}\right|  =  - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{3 + 4\cos \left( {{n\tau }\log p}\right)  + \cos \left( {{2n\tau }\log p}\right) }{n{p}^{n\sigma }}
\]

est toujours négative, donc \( {\left| 1 - {p}^{-\sigma }\right| }^{3} \cdot {\left| 1 - {p}^{-\sigma - {i\tau }}\right| }^{4} \cdot \left| {1 - {p}^{-\sigma - {2i\tau }}}\right| \leq 1 \) . Compte tenu de l’identité d’Euler (question 2/a)) appliquée à \( \zeta \left( \sigma \right) ,\zeta \left( {\sigma + {i\tau }}\right) \) et \( \zeta \left( {\sigma + {2i\tau }}\right) \) , ceci entraîne bien le résultat attendu.

> is always negative, so \( {\left| 1 - {p}^{-\sigma }\right| }^{3} \cdot {\left| 1 - {p}^{-\sigma - {i\tau }}\right| }^{4} \cdot \left| {1 - {p}^{-\sigma - {2i\tau }}}\right| \leq 1 \) . Given Euler's identity (question 2/a)) applied to \( \zeta \left( \sigma \right) ,\zeta \left( {\sigma + {i\tau }}\right) \) and \( \zeta \left( {\sigma + {2i\tau }}\right) \) , this indeed leads to the expected result.

c) On a déjà démontré que \( \zeta \left( s\right) \) ne s’annule pas sur \( D \) , donc il s’agit ici de montrer que \( \zeta \left( s\right) \) ne s’annule pas pour \( \Re \left( s\right) = 1 \) . Raisonnons par l’absurde et supposons \( \zeta \left( {1 + {i\tau }}\right) = 0 \) , avec \( \tau \neq 0 \) . La dérivabilité en \( \sigma = 1 \) de l’application \( \lbrack 1, + \infty \lbrack \rightarrow \mathbb{C},\sigma \mapsto \zeta \left( {\sigma + {i\tau }}\right) \) ,établi en \( 1/\mathrm{d}) \) , entraîne \( \zeta \left( {\sigma + {i\tau }}\right) = O\left( {\sigma - 1}\right) \) lorsque \( \sigma \rightarrow {1}^{ + } \) . Par ailleurs, \( \zeta \left( \sigma \right) = O\left( {1/\left( {\sigma - 1}\right) }\right) \) lorsque \( \sigma \rightarrow {1}^{ + } \) . Comme de plus \( \zeta \left( {\sigma + {2i\tau }}\right) = O\left( 1\right) \) , tout ceci entraîne

> c) We have already shown that \( \zeta \left( s\right) \) does not vanish on \( D \) , so here we must show that \( \zeta \left( s\right) \) does not vanish for \( \Re \left( s\right) = 1 \) . Let us reason by contradiction and assume \( \zeta \left( {1 + {i\tau }}\right) = 0 \) , with \( \tau \neq 0 \) . The differentiability at \( \sigma = 1 \) of the mapping \( \lbrack 1, + \infty \lbrack \rightarrow \mathbb{C},\sigma \mapsto \zeta \left( {\sigma + {i\tau }}\right) \) , established in \( 1/\mathrm{d}) \) , implies \( \zeta \left( {\sigma + {i\tau }}\right) = O\left( {\sigma - 1}\right) \) as \( \sigma \rightarrow {1}^{ + } \) . Furthermore, \( \zeta \left( \sigma \right) = O\left( {1/\left( {\sigma - 1}\right) }\right) \) as \( \sigma \rightarrow {1}^{ + } \) . Since, in addition, \( \zeta \left( {\sigma + {2i\tau }}\right) = O\left( 1\right) \) , all this leads to

\[
{\left| \zeta \left( \sigma \right) \right| }^{3}{\left| \zeta \left( \sigma  + i\tau \right) \right| }^{4}\left| {\zeta \left( {\sigma  + {2i\tau }}\right) }\right|  = O\left( {\left( \sigma  - 1\right) }^{-3}\right)  \times  O\left( {\left( \sigma  - 1\right) }^{4}\right)  \times  O\left( 1\right)  = O\left( {\sigma  - 1}\right) ,\;\sigma  \rightarrow  {1}^{ - }
\]

donc cette expression peut être rendue arbitrairement proche de 0, ce qui est incompatible avec l’inégalité établie à la question précédente. Donc \( \zeta \left( {1 + {i\tau }}\right) \) ne s’annule jamais.

> so this expression can be made arbitrarily close to 0, which is incompatible with the inequality established in the previous question. Therefore, \( \zeta \left( {1 + {i\tau }}\right) \) never vanishes.

Donnons maintenant une minoration de \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \) . Soit \( \varepsilon > 0 \) . L’inégalité établie à la question précédente entraîne, lorsque \( {\sigma }_{t} = 1 + \varepsilon /{\log }^{9}\left| t\right| \leq \sigma \leq 2 \) et \( \left| t\right| \geq 2 \)

> Let us now provide a lower bound for \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| \) . Let \( \varepsilon > 0 \) . The inequality established in the previous question implies, when \( {\sigma }_{t} = 1 + \varepsilon /{\log }^{9}\left| t\right| \leq \sigma \leq 2 \) and \( \left| t\right| \geq 2 \)

\[
\left| \frac{1}{\zeta \left( {\sigma  + {it}}\right) }\right|  \leq  {\left| \zeta \left( \sigma \right) \right| }^{3/4}{\left| \zeta \left( \sigma  + 2it\right) \right| }^{1/4} \leq  \frac{{\sigma }^{3/4}{\left( {M}_{0}\log \left| 2t\right| \right) }^{1/4}}{{\left( \sigma  - 1\right) }^{3/4}} \leq  \frac{2{M}_{0}^{1/4}{\log }^{1/4}\left| t\right| }{{\left( \varepsilon {\log }^{-9}\left| t\right| \right) }^{3/4}} = \frac{{\log }^{7}\left| t\right| }{A{\varepsilon }^{3/4}},
\]

avec \( A = 1/\left( {2{M}_{0}^{1/4}}\right) \) . Lorsque \( 1 \leq \sigma < {\sigma }_{t} \) et \( \left| t\right| \geq 2 \) , on écrit

> with \( A = 1/\left( {2{M}_{0}^{1/4}}\right) \) . When \( 1 \leq \sigma < {\sigma }_{t} \) and \( \left| t\right| \geq 2 \) , we write

\[
\left| {\zeta \left( {\sigma  + {it}}\right) }\right|  \geq  \left| {\zeta \left( {{\sigma }_{t} + {it}}\right) }\right|  - {\int }_{\sigma }^{{\sigma }_{t}}\left| {{\zeta }^{\prime }\left( {x + {it}}\right) }\right| {dx} \geq  \frac{A{\varepsilon }^{3/4}}{{\log }^{7}\left| t\right| } - \left( {{\sigma }_{t} - \sigma }\right) {M}_{1}{\log }^{2}\left| t\right|  = \frac{{\varepsilon }^{3/4}\left( {A - {\varepsilon }^{1/4}{M}_{1}}\right) }{{\log }^{7}\left| t\right| }.
\]

En choisissant \( \varepsilon > 0 \) suffisamment petit, on peut supposer que \( {m}_{0} = {\varepsilon }^{3/4}\left( {A - {\varepsilon }^{1/4}{M}_{1}}\right) \) est strictement positif. Ainsi choisi, \( {m}_{0} \) vérifie \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| > {m}_{0}/{\log }^{7}\left| t\right| \) pour \( 1 \leq \sigma \leq 2 \) et \( \left| t\right| \geq 2 \) . d) Il est immédiat que \( F \) , comme \( \zeta \) et \( {\zeta }^{\prime } \) , est prolongeable en une fonction continue sur \( \bar{D} \smallsetminus \{ 1\} \) . Lorsque \( s \in \bar{D} \smallsetminus \{ 1\} \) on a, vu que \( Z\left( s\right) = - {\zeta }^{\prime }\left( s\right) /\zeta \left( s\right) \) ,

> By choosing \( \varepsilon > 0 \) sufficiently small, we can assume that \( {m}_{0} = {\varepsilon }^{3/4}\left( {A - {\varepsilon }^{1/4}{M}_{1}}\right) \) is strictly positive. Thus chosen, \( {m}_{0} \) satisfies \( \left| {\zeta \left( {\sigma + {it}}\right) }\right| > {m}_{0}/{\log }^{7}\left| t\right| \) for \( 1 \leq \sigma \leq 2 \) and \( \left| t\right| \geq 2 \) . d) It is immediate that \( F \) , like \( \zeta \) and \( {\zeta }^{\prime } \) , can be extended to a continuous function on \( \bar{D} \smallsetminus \{ 1\} \) . When \( s \in \bar{D} \smallsetminus \{ 1\} \) we have, given that \( Z\left( s\right) = - {\zeta }^{\prime }\left( s\right) /\zeta \left( s\right) \) ,

\[
F\left( s\right)  = \eta \left( s\right)  + \frac{1}{s - 1} + \frac{{\eta }^{\prime }\left( s\right)  - \frac{1}{{\left( s - 1\right) }^{2}}}{\eta \left( s\right)  + \frac{1}{s - 1}} = \eta \left( s\right)  + \frac{\eta \left( s\right)  + \left( {s - 1}\right) {\eta }^{\prime }\left( s\right) }{1 + \left( {s - 1}\right) \eta \left( s\right) },
\]

et le dernier terme converge lorsque \( s \rightarrow 1 \) (vers \( {2\eta }\left( 1\right) \) ) donc \( F \) est bien prolongeable en une fonction continue sur \( \bar{D} \) tout entier.

> and the last term converges as \( s \rightarrow 1 \) (to \( {2\eta }\left( 1\right) \) ) so \( F \) is indeed extendable to a continuous function on the entire \( \bar{D} \) .

La majoration de \( \left| {F\left( s\right) }\right| \) est immédiate à partir des majorations démontrées précédemment pour \( \left| {\zeta \left( s\right) }\right| \) et \( \left| {{\zeta }^{\prime }\left( s\right) }\right| \) et de la minoration obtenue pour \( \left| {\zeta \left( s\right) }\right| \) .

> The upper bound of \( \left| {F\left( s\right) }\right| \) is immediate from the bounds demonstrated previously for \( \left| {\zeta \left( s\right) }\right| \) and \( \left| {{\zeta }^{\prime }\left( s\right) }\right| \) and the lower bound obtained for \( \left| {\zeta \left( s\right) }\right| \) .

Remarque. L’expression (***) permet de définir \( \zeta \left( s\right) \) pour \( \Re \left( s\right) > 0 \) (sauf en \( s = 1 \) ). Dans le cadre des fonctions analytiques (ce qui est le cas pour \( \zeta \left( s\right) \) ), ce prolongement est unique. On peut même poursuivre le procédé (l'identité (***) est issue de la formule d'Euler-Maclaurin au premier ordre, que l'on peut utiliser à un ordre supérieur) pour prolonger la fonction \( \zeta \left( s\right) \) sur \( \mathbb{C} \smallsetminus \{ 1\} \) tout entier.

> Remark. The expression (***) allows defining \( \zeta \left( s\right) \) for \( \Re \left( s\right) > 0 \) (except at \( s = 1 \) ). In the context of analytic functions (which is the case for \( \zeta \left( s\right) \) ), this extension is unique. One can even continue the process (the identity (***) comes from the Euler-Maclaurin formula at the first order, which can be used at a higher order) to extend the function \( \zeta \left( s\right) \) to the entire \( \mathbb{C} \smallsetminus \{ 1\} \) .

Problem 2 (FORMULE DE PERRON). a) En utilisant le résultat de la question c) du problème 17 page 190, montrer

> Problem 2 (PERRON'S FORMULA). a) Using the result of question c) of problem 17 on page 190, show

\[
\forall x > 0,\forall \sigma  > 0,\;{P}_{\sigma }\left( x\right)  = \frac{1}{2\pi }\mathop{\lim }\limits_{{T \rightarrow   + \infty }}{\int }_{-T}^{T}\frac{{x}^{\sigma  + {it}}}{\sigma  + {it}}{dt} = \left\{  \begin{array}{ll} 1 & \left( {x > 1}\right) \\  1/2 & \left( {x = 1}\right) \\  0 & \left( {0 < x < 1}\right)  \end{array}\right.
\]

b) Montrer que

> b) Show that

\[
\forall x > 0,\forall \sigma  > 0,\;{Q}_{\sigma }\left( x\right)  = \frac{1}{2\pi }{\int }_{-\infty }^{+\infty }\frac{{x}^{1 + \sigma  + {it}}}{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt} = \left\{  \begin{array}{ll} \left( {x - 1}\right) & \left( {x > 1}\right) \\  0 & \left( {0 < x \leq  1}\right)  \end{array}\right.
\]

c) Soit \( {\left( {a}_{n}\right) }_{n \geq 1} \) une suite de nombres complexes vérifiant, pour tout \( \varepsilon > 0,{a}_{n} = O\left( {n}^{\varepsilon }\right) \) . On considère la fonction \( G\left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{a}_{n}/{n}^{s} \) de la variable complexe \( s \) (série de Dirichlet). Montrer que \( G \) est définie et continue sur \( D = \{ z \in \mathbb{C} \mid \Re \left( z\right) > 1\} \) et que

> c) Let \( {\left( {a}_{n}\right) }_{n \geq 1} \) be a sequence of complex numbers satisfying, for all \( \varepsilon > 0,{a}_{n} = O\left( {n}^{\varepsilon }\right) \) . Consider the function \( G\left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{a}_{n}/{n}^{s} \) of the complex variable \( s \) (Dirichlet series). Show that \( G \) is defined and continuous on \( D = \{ z \in \mathbb{C} \mid \Re \left( z\right) > 1\} \) and that

\[
\forall \sigma  > 1,\;{\int }_{0}^{x}\varphi \left( y\right) {dy} = \frac{1}{2\pi }{\int }_{-\infty }^{+\infty }\frac{{x}^{1 + \sigma  + {it}}G\left( {\sigma  + {it}}\right) }{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt},\;\text{ où }\;\varphi \left( y\right)  = \mathop{\sum }\limits_{{1 \leq  n \leq  y}}{a}_{n}.
\]

---

Solution. a) En coupant l’intégrale en deux pour se ramener sur l’intervalle \( \left\lbrack {0, T}\right\rbrack \) , on trouve

> Solution. a) By splitting the integral in two to reduce it to the interval \( \left\lbrack {0, T}\right\rbrack \) , we find

\[
{\int }_{-T}^{T}\frac{{x}^{\sigma  + {it}}}{\sigma  + {it}}{dt} = {\int }_{0}^{T}\left( {\frac{{x}^{\sigma  + {it}}}{\sigma  + {it}} + \frac{{x}^{\sigma  - {it}}}{\sigma  - {it}}}\right) {dt} = {x}^{\sigma }{\int }_{0}^{T}\frac{{2\sigma }\cos \left( {t\log x}\right)  + {2t}\sin \left( {t\log x}\right) }{{\sigma }^{2} + {t}^{2}}{dt}
\]

\[
= 2{x}^{\sigma }\left( {{\int }_{0}^{\sigma T}\frac{\cos \left( {{\sigma u}\log x}\right) }{1 + {u}^{2}}{du} + {\int }_{0}^{\sigma T}\frac{u\sin \left( {{\sigma u}\log x}\right) }{1 + {u}^{2}}{du}}\right)
\]

où on a effectué le changement de variable \( t = {\sigma u} \) . Lorsque \( T \rightarrow + \infty \) , les deux dernières intégrales convergent respectivement vers les intégrales \( C\left( {\sigma \log x}\right) \) et \( S\left( {\sigma \log x}\right) \) de la question c) du problème 17 page 190. On en déduit que \( {P}_{\sigma }\left( x\right) \) existe bien et que

> where we performed the change of variable \( t = {\sigma u} \) . As \( T \rightarrow + \infty \) , the last two integrals converge respectively to the integrals \( C\left( {\sigma \log x}\right) \) and \( S\left( {\sigma \log x}\right) \) from question c) of problem 17 on page 190. We deduce that \( {P}_{\sigma }\left( x\right) \) indeed exists and that

\[
{P}_{\sigma }\left( x\right)  = \frac{{x}^{\sigma }}{\pi }\left( {C\left( {\sigma \log x}\right)  + S\left( {\sigma \log x}\right) }\right) .
\]

Les valeurs de \( C\left( v\right) \) et \( S\left( v\right) \) sont connues avec la question c) du problème 17 page 190. Elles entraînent \( C\left( v\right) + S\left( v\right) = \pi {e}^{-v} \) si \( v > 0, C\left( 0\right) + S\left( 0\right) = \pi /2 \) et \( C\left( v\right) + S\left( v\right) = 0 \) si \( v < 0 \) . On en déduit que si \( x > 1 \) alors \( \sigma \log x > 0 \) donc \( {P}_{\sigma }\left( x\right) = \frac{{x}^{\sigma }}{\pi }\left( {\pi {e}^{-\sigma \log x}}\right) = 1 \) , si \( x = 1 \) , \( {P}_{\sigma }\left( x\right) = \frac{1}{\pi }\left( {\pi /2}\right) = 1/2 \) , et si \( 0 < x < 1 \) alors \( {P}_{\sigma }\left( x\right) = 0. \)

> The values of \( C\left( v\right) \) and \( S\left( v\right) \) are known from question c) of problem 17 on page 190. They lead to \( C\left( v\right) + S\left( v\right) = \pi {e}^{-v} \) if \( v > 0, C\left( 0\right) + S\left( 0\right) = \pi /2 \) and \( C\left( v\right) + S\left( v\right) = 0 \) if \( v < 0 \) . We deduce that if \( x > 1 \) then \( \sigma \log x > 0 \) so \( {P}_{\sigma }\left( x\right) = \frac{{x}^{\sigma }}{\pi }\left( {\pi {e}^{-\sigma \log x}}\right) = 1 \) , if \( x = 1 \) , \( {P}_{\sigma }\left( x\right) = \frac{1}{\pi }\left( {\pi /2}\right) = 1/2 \) , and if \( 0 < x < 1 \) then \( {P}_{\sigma }\left( x\right) = 0. \)

b) L’idée est de montrer que \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) \) . L’hypothèse de domination n’étant pas vérifiée pour l’intégrande dérivée, on procède autrement. On considère pour tout \( n \in {\mathbb{N}}^{ * } \)

> b) The idea is to show that \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) \) . Since the domination hypothesis is not satisfied for the derived integrand, we proceed differently. We consider for all \( n \in {\mathbb{N}}^{ * } \)

\[
{f}_{n}\left( x\right)  = \frac{1}{2\pi }{\int }_{-n}^{n}\frac{{x}^{1 + \sigma  + {it}}}{\left( {1 + \sigma  + {it}}\right) \left( {\sigma  + {it}}\right) }{dt}.
\]

L’intégrande est continûment dérivable par rapport à \( x \) donc \( {f}_{n}\left( x\right) \) est dérivable et

> The integrand is continuously differentiable with respect to \( x \) so \( {f}_{n}\left( x\right) \) is differentiable and

\[
{f}_{n}^{\prime }\left( x\right)  = \frac{1}{2\pi }{\int }_{-n}^{n}\frac{{x}^{\sigma  + {it}}}{\sigma  + {it}}{dt}.
\]

On intègre par parties en supposant \( x > 0 \) et \( x \neq 1 \) ce qui donne

> We integrate by parts assuming \( x > 0 \) and \( x \neq 1 \) which gives

\[
{f}_{n}^{\prime }\left( x\right)  = \frac{{x}^{\sigma }}{{2i\pi }\log x}\left( {\frac{{x}^{in}}{\sigma  + {in}} - \frac{{x}^{-{in}}}{\sigma  - {in}} + {\int }_{-n}^{n}\frac{i{x}^{it}}{{\left( \sigma  + it\right) }^{2}}{dt}}\right) .
\]

Comme \( {P}_{\sigma }\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n}^{\prime }\left( x\right) \) on en déduit \( {P}_{\sigma }\left( x\right) = \frac{{x}^{\sigma }}{{2i\pi }\log x}{\int }_{-\infty }^{+\infty }\frac{i{x}^{it}}{{\left( \sigma + it\right) }^{2}}{dt} \) , et donc

> Since \( {P}_{\sigma }\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n}^{\prime }\left( x\right) \) we deduce \( {P}_{\sigma }\left( x\right) = \frac{{x}^{\sigma }}{{2i\pi }\log x}{\int }_{-\infty }^{+\infty }\frac{i{x}^{it}}{{\left( \sigma + it\right) }^{2}}{dt} \) , and therefore

\[
\left| {{f}_{n}^{\prime }\left( x\right)  - {P}_{\sigma }\left( x\right) }\right|  \leq  \left| \frac{{x}^{\sigma }}{{2\pi }\log x}\right| \left( {\frac{2}{n} + {\int }_{-\infty }^{-n}\frac{1}{{t}^{2}}{dt} + {\int }_{n}^{+\infty }\frac{1}{{t}^{2}}{dt}}\right)  = \frac{2{x}^{\sigma }}{{\pi n}\left| {\log x}\right| }.
\]

Cette inégalité entraîne la convergence uniforme de \( \left( {f}_{n}^{\prime }\right) \) vers \( {P}_{\sigma } \) sur tout segment de la forme \( \left\lbrack {a, b}\right\rbrack \) avec \( 0 < a < b < 1 \) ou \( 1 < a < b \) . On en déduit que \( {Q}_{\sigma } \) , limite simple de \( \left( {f}_{n}\right) \) , est dérivable sur tout segment de cette forme, donc sur \( \rbrack 0,1\left\lbrack \cup \right\rbrack 1, + \infty \lbrack \) et que \( {Q}_{\sigma }^{\prime } = {P}_{\sigma } \) sur cet intervalle.

> This inequality implies the uniform convergence of \( \left( {f}_{n}^{\prime }\right) \) to \( {P}_{\sigma } \) on any segment of the form \( \left\lbrack {a, b}\right\rbrack \) with \( 0 < a < b < 1 \) or \( 1 < a < b \) . We deduce that \( {Q}_{\sigma } \) , the pointwise limit of \( \left( {f}_{n}\right) \) , is differentiable on any segment of this form, therefore on \( \rbrack 0,1\left\lbrack \cup \right\rbrack 1, + \infty \lbrack \) and that \( {Q}_{\sigma }^{\prime } = {P}_{\sigma } \) on this interval.

---

Maintenant on a \( {Q}_{\sigma }\left( x\right) = O\left( {x}^{1 + \sigma }\right) \) donc \( \mathop{\lim }\limits_{{x \rightarrow 0, x > 0}}{Q}_{\sigma }\left( x\right) = 0 \) et comme \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) = 0 \) pour \( 0 < x < 1 \) , on en déduit \( {Q}_{\sigma }\left( x\right) = 0 \) pour \( 0 < x < 1 \) . Comme \( {Q}_{\sigma } \) est continue sur \( {\mathbb{R}}^{ + } \) (son intégrande est continue et majorée en valeur absolue par une fonction intégrable lorsque \( x \) est dans tout segment inclus dans \( \rbrack 0, + \infty \left\lbrack \right\rbrack \) ), on a aussi \( {Q}_{\sigma }\left( 1\right) = 0 \) . Comme de plus \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) = 1 \) pour \( x > 1 \) , le théorème des accroissements finis entraîne \( {Q}_{\sigma }\left( x\right) = x - 1 \) pour \( x > 1 \) .

> Now we have \( {Q}_{\sigma }\left( x\right) = O\left( {x}^{1 + \sigma }\right) \) so \( \mathop{\lim }\limits_{{x \rightarrow 0, x > 0}}{Q}_{\sigma }\left( x\right) = 0 \) and since \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) = 0 \) for \( 0 < x < 1 \) , we deduce \( {Q}_{\sigma }\left( x\right) = 0 \) for \( 0 < x < 1 \) . As \( {Q}_{\sigma } \) is continuous on \( {\mathbb{R}}^{ + } \) (its integrand is continuous and bounded in absolute value by an integrable function when \( x \) is in any segment included in \( \rbrack 0, + \infty \left\lbrack \right\rbrack \) ), we also have \( {Q}_{\sigma }\left( 1\right) = 0 \) . Since furthermore \( {Q}_{\sigma }^{\prime }\left( x\right) = {P}_{\sigma }\left( x\right) = 1 \) for \( x > 1 \) , the mean value theorem implies \( {Q}_{\sigma }\left( x\right) = x - 1 \) for \( x > 1 \) .

c) Soit \( \delta > 0 \) . Par hypothèse, il existe \( M > 0 \) tel que \( \left| {a}_{n}\right| \leq M{n}^{\delta /2} \) pour tout \( n \in {\mathbb{N}}^{ * } \) , donc pour tout \( s \in {D}_{1 + \delta } = \left\{ {z \in \mathbb{C} \mid \Re \left( z\right) \geq 1 + \delta }\right\} \) on a \( \left| {{a}_{n}/{n}^{s}}\right| \leq M/{n}^{1 + \delta /2} \) . Ainsi, la série de fonctions \( \sum {a}_{n}/{n}^{s} \) converge normalement sur \( {D}_{1 + \delta } \) , elle est donc continue (et bornée) sur ce domaine Ceci étant vrai pour tout \( \delta > 0 \) on en déduit que \( G\left( s\right) \) est bien définie et continue sur \( D \) .

> c) Let \( \delta > 0 \) . By hypothesis, there exists \( M > 0 \) such that \( \left| {a}_{n}\right| \leq M{n}^{\delta /2} \) for all \( n \in {\mathbb{N}}^{ * } \) , so for all \( s \in {D}_{1 + \delta } = \left\{ {z \in \mathbb{C} \mid \Re \left( z\right) \geq 1 + \delta }\right\} \) we have \( \left| {{a}_{n}/{n}^{s}}\right| \leq M/{n}^{1 + \delta /2} \) . Thus, the series of functions \( \sum {a}_{n}/{n}^{s} \) converges normally on \( {D}_{1 + \delta } \) , it is therefore continuous (and bounded) on this domain. This being true for all \( \delta > 0 \) we deduce that \( G\left( s\right) \) is well-defined and continuous on \( D \) .

Montrons la formule de Perron. Soit \( \sigma > 1 \) . Comme \( \sum {a}_{n}/{n}^{s} \) converge normalement sur \( {D}_{\sigma } \) , en particulier sur \( \Re \left( s\right) = \sigma \) , on peut inverser les signes de sommation ce qui donne

> Let us show Perron's formula. Let \( \sigma > 1 \) . Since \( \sum {a}_{n}/{n}^{s} \) converges normally on \( {D}_{\sigma } \) , in particular on \( \Re \left( s\right) = \sigma \) , we can invert the summation signs which gives

\[
\frac{1}{2\pi }{\int }_{-\infty }^{+\infty }\frac{{x}^{1 + \sigma  + {it}}G\left( {\sigma  + {it}}\right) }{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt} = \frac{1}{2\pi }\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\int }_{-\infty }^{+\infty }\frac{{x}^{1 + \sigma  + {it}}{a}_{n}/{n}^{\sigma  + {it}}}{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{a}_{n}{Q}_{\sigma }\left( \frac{x}{n}\right) .
\]

Compte tenu de la valeur de \( {Q}_{\sigma }\left( x\right) \) obtenue à la question précédente, ceci entraîne

> Given the value of \( {Q}_{\sigma }\left( x\right) \) obtained in the previous question, this implies

\[
\frac{1}{2\pi }{\int }_{-\infty }^{+\infty }\frac{{x}^{1 + \sigma  + {it}}G\left( {\sigma  + {it}}\right) }{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt} = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}\left( {x - n}\right) {a}_{n}.
\]

(*)

> Par ailleurs, pour \( 0 \leq y \leq x \) on peut écrire \( \varphi \left( y\right) = \mathop{\sum }\limits_{{1 \leq n \leq x}}{a}_{n}{\chi }_{n}\left( y\right) \) où \( {\chi }_{n}\left( y\right) = 0 \) si \( y < n \) , \( {\chi }_{n}\left( y\right) = 1 \) pour \( y \geq n \) . Ceci montre que

Furthermore, for \( 0 \leq y \leq x \) we can write \( \varphi \left( y\right) = \mathop{\sum }\limits_{{1 \leq n \leq x}}{a}_{n}{\chi }_{n}\left( y\right) \) where \( {\chi }_{n}\left( y\right) = 0 \) if \( y < n \) , \( {\chi }_{n}\left( y\right) = 1 \) for \( y \geq n \) . This shows that

\[
{\int }_{0}^{x}\varphi \left( y\right) {dy} = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}{\int }_{0}^{x}{a}_{n}{\chi }_{n}\left( y\right) {dy} = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}{\int }_{n}^{x}{a}_{n}{dy} = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}\left( {x - n}\right) {a}_{n}.
\]

Grâce à l'égalité (*) on en déduit la formule de Perron.

> Thanks to equality (*) we deduce Perron's formula.
