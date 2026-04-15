#### 3.4. Exercises

*Français : 3.4. Exercices*

EXERCICE 1. a) Montrer que la suite de fonctions \( \left( {f}_{n}\right) \) définie par

> EXERCISE 1. a) Show that the sequence of functions \( \left( {f}_{n}\right) \) defined by

\[
{f}_{n} : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R},\;{f}_{n}\left( x\right)  = {\left( 1 - \frac{x}{n}\right) }^{n}\text{ si }x \in  \left\lbrack  {0, n}\right\rbrack  ,\;{f}_{n}\left( x\right)  = 0\text{ si }x > n
\]

converge uniformément sur \( {\mathbb{R}}^{ + } \) vers la fonction \( f : x \mapsto {e}^{-x} \) .

> converges uniformly on \( {\mathbb{R}}^{ + } \) to the function \( f : x \mapsto {e}^{-x} \).

b) Montrer que la suite de fonctions \( \left( {f}_{n}\right) \) définie par

> b) Show that the sequence of functions \( \left( {f}_{n}\right) \) defined by

\[
{f}_{n} : \mathbb{C} \rightarrow  \mathbb{C}\;z \mapsto  {\left( 1 + \frac{z}{n}\right) }^{n}
\]

converge uniformément sur tout compact de \( \mathbb{C} \) vers \( f : z \mapsto {e}^{z} \) .

> converges uniformly on every compact subset of \( \mathbb{C} \) to \( f : z \mapsto {e}^{z} \).

Solution. a) Remarquons déjà qu'il y a convergence simple. Pour montrer la convergence uni-forme, nous allons donner deux méthodes.

> Solution. a) Let us first note that there is pointwise convergence. To show uniform convergence, we will provide two methods.

Première méthode. Nous allons utiliser une technique générale, qui consiste à montrer que le maximum sur \( {\mathbb{R}}^{ + } \) de \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| \) tend vers 0 en faisant une étude de fonctions. Fixons un entier \( n > 1 \) et posons \( \varphi : \left\lbrack {0, n}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {e}^{-x} - {f}_{n}\left( x\right) \) . On a, pour tout \( x \in \lbrack 0, n\lbrack \)

> First method. We will use a general technique, which consists of showing that the maximum on \( {\mathbb{R}}^{ + } \) of \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| \) tends to 0 by performing a function study. Let us fix an integer \( n > 1 \) and set \( \varphi : \left\lbrack {0, n}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {e}^{-x} - {f}_{n}\left( x\right) \). We have, for all \( x \in \lbrack 0, n\lbrack \)

\[
{\varphi }^{\prime }\left( x\right)  =  - {e}^{-x} + {\left( 1 - \frac{x}{n}\right) }^{n - 1} = {e}^{-x}\left\lbrack  {\exp \left( {\left( {n - 1}\right) \log \left( {1 - \frac{x}{n}}\right)  + x}\right)  - 1}\right\rbrack  .
\]

Le signe de \( {\varphi }^{\prime }\left( x\right) \) est donc celui de \( \psi \left( x\right) = \left( {n - 1}\right) \log \left( {1 - x/n}\right) + x \) . On a \( {\psi }^{\prime }\left( x\right) = \left( {1 - x}\right) /\left( {n - x}\right) \) , on en déduit que \( \psi \) croît sur \( \left\lbrack {0,1}\right\rbrack \) et décroît sur \( \lbrack 1, n\lbrack \) . Comme \( \psi \left( 0\right) = 0 \) et que \( \psi \left( x\right) \rightarrow - \infty \) lorsque \( x \rightarrow {n}^{ - } \) , on en déduit (faites un tableau de variation) l’existence de \( \alpha \in \rbrack 1, n\lbrack \) tel que

> The sign of \( {\varphi }^{\prime }\left( x\right) \) is therefore that of \( \psi \left( x\right) = \left( {n - 1}\right) \log \left( {1 - x/n}\right) + x \). We have \( {\psi }^{\prime }\left( x\right) = \left( {1 - x}\right) /\left( {n - x}\right) \), from which we deduce that \( \psi \) increases on \( \left\lbrack {0,1}\right\rbrack \) and decreases on \( \lbrack 1, n\lbrack \). Since \( \psi \left( 0\right) = 0 \) and \( \psi \left( x\right) \rightarrow - \infty \) as \( x \rightarrow {n}^{ - } \), we deduce (create a variation table) the existence of \( \alpha \in \rbrack 1, n\lbrack \) such that

\[
\forall x \in  \left\lbrack  {0,\alpha }\right\rbrack  ,\;\psi \left( x\right)  \geq  0,\;\forall x \in  \lbrack \alpha , n\lbrack ,\;\psi \left( x\right)  \leq  0.
\]

Comme \( \psi \) a le signe de \( {\varphi }^{\prime },\varphi \) est croissante sur \( \left\lbrack {0,\alpha }\right\rbrack \) et décroissante sur \( \left\lbrack {\alpha , n}\right\rbrack \) . Comme \( \varphi \left( 0\right) = 0 \) et \( \varphi \left( n\right) = {e}^{-n} \geq 0 \) , on en déduit

> Since \( \psi \) has the sign of \( {\varphi }^{\prime },\varphi \), it is increasing on \( \left\lbrack {0,\alpha }\right\rbrack \) and decreasing on \( \left\lbrack {\alpha , n}\right\rbrack \). Since \( \varphi \left( 0\right) = 0 \) and \( \varphi \left( n\right) = {e}^{-n} \geq 0 \), we deduce

\[
\forall x \in  \left\lbrack  {0, n}\right\rbrack  ,\;0 \leq  \varphi \left( x\right)  \leq  \varphi \left( \alpha \right) \;\text{ avec }\;{\varphi }^{\prime }\left( \alpha \right)  = 0.
\]

Il s’agit donc pour nous de majorer \( \varphi \left( \alpha \right) \) . En exploitant le renseignement \( {\varphi }^{\prime }\left( \alpha \right) = 0 \) , on a

> Our goal is therefore to find an upper bound for \( \varphi \left( \alpha \right) \). By using the information \( {\varphi }^{\prime }\left( \alpha \right) = 0 \), we have

\[
{\left( 1 - \frac{\alpha }{n}\right) }^{n - 1} = {e}^{-\alpha }\;\text{ donc }\;\varphi \left( \alpha \right)  = {e}^{-\alpha } - {\left( 1 - \frac{\alpha }{n}\right) }^{n - 1}\left( {1 - \frac{\alpha }{n}}\right)  = \frac{\alpha }{n}{e}^{-\alpha }.
\]

(*)

> Un rapide étude de \( x \mapsto x{e}^{-x} \) montre que cette fonction atteint son maximum en \( x = 1 \) , donc est majorée par \( 1/e \) sur \( {\mathbb{R}}^{ + } \) , de sorte que (*) entraîne \( \varphi \left( \alpha \right) \leq 1/\left( {ne}\right) \) . Sur \( \lbrack n, + \infty \lbrack \) , on a \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| = \left| {f\left( x\right) }\right| \leq \left| {f\left( n\right) }\right| = \left| {{f}_{n}\left( n\right) - f\left( n\right) }\right| \leq 1/\left( {ne}\right) \) , donc finalement

A quick study of \( x \mapsto x{e}^{-x} \) shows that this function reaches its maximum at \( x = 1 \), and is therefore bounded by \( 1/e \) on \( {\mathbb{R}}^{ + } \), so that (*) implies \( \varphi \left( \alpha \right) \leq 1/\left( {ne}\right) \). On \( \lbrack n, + \infty \lbrack \), we have \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| = \left| {f\left( x\right) }\right| \leq \left| {f\left( n\right) }\right| = \left| {{f}_{n}\left( n\right) - f\left( n\right) }\right| \leq 1/\left( {ne}\right) \), so finally

\[
\forall x \in  {\mathbb{R}}^{ + },\;\left| {{f}_{n}\left( x\right)  - f\left( x\right) }\right|  \leq  \frac{1}{ne},
\]

d'où le résultat.

> hence the result.

- Seconde méthode. Considérons \( \varepsilon  > 0 \) , puis \( M > 0 \) tel que \( {e}^{-M} < \varepsilon \) . Nous commençons par approcher \( \log {f}_{n} \) par \( - x \) sur \( \left\lbrack  {0, M}\right\rbrack \) . D’après la formule de Taylor-Lagrange,

> - Second method. Let us consider \( \varepsilon  > 0 \) , then \( M > 0 \) such that \( {e}^{-M} < \varepsilon \) . We begin by approximating \( \log {f}_{n} \) by \( - x \) on \( \left\lbrack  {0, M}\right\rbrack \) . According to the Taylor-Lagrange formula,

\[
\forall u \in  \left\lbrack  {0,\frac{1}{2}}\right\rbrack  ,\exists \theta  \in  \rbrack 0,1\lbrack ,\;\log \left( {1 - u}\right)  =  - u + \frac{{u}^{2}}{2}\frac{1}{{\left( 1 - \theta u\right) }^{2}},
\]

donc \( \left| {\log \left( {1 - u}\right) + u}\right| \leq 2{u}^{2} \) lorsque \( u \in \left\lbrack {0,1/2}\right\rbrack \) . On en déduit

> therefore \( \left| {\log \left( {1 - u}\right) + u}\right| \leq 2{u}^{2} \) as \( u \in \left\lbrack {0,1/2}\right\rbrack \) . We deduce

\[
\forall n \geq  {2M},\forall x \in  \left\lbrack  {0, M}\right\rbrack  ,\;\left| {n\log \left( {1 - \frac{x}{n}}\right)  + x}\right|  \leq  \frac{2{M}^{2}}{n},
\]

donc \( \left( {\log {f}_{n}}\right) \) converge uniformément vers \( x \mapsto - x \) sur \( \left\lbrack {0, M}\right\rbrack \) . La fonction exponentielle étant 1- lipschitzienne sur \( {\mathbb{R}}^{ - } \) (immédiat par l’inégalité des accroissements finis), on en déduit en prenant l’exponentielle que \( \left( {f}_{n}\right) \) converge uniformément vers \( f \) sur \( \left\lbrack {0, M}\right\rbrack \) . En particulier,

> therefore \( \left( {\log {f}_{n}}\right) \) converges uniformly to \( x \mapsto - x \) on \( \left\lbrack {0, M}\right\rbrack \) . Since the exponential function is 1-Lipschitz on \( {\mathbb{R}}^{ - } \) (immediate by the mean value inequality), we deduce by taking the exponential that \( \left( {f}_{n}\right) \) converges uniformly to \( f \) on \( \left\lbrack {0, M}\right\rbrack \) . In particular,

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\forall x \in  \left\lbrack  {0, M}\right\rbrack  ,\;\left| {{f}_{n}\left( x\right)  - f\left( x\right) }\right|  < \varepsilon .
\]

\( \left( {* * }\right) \)

> Or \( {e}^{-M} < \varepsilon \) , donc \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| \leq {e}^{-x} \leq {e}^{-M} < \varepsilon \) sur \( \lbrack M, + \infty \lbrack \) , donc finalement l’inégalité (**) est vraie sur \( {\mathbb{R}}^{ + } \) tout entier, d’où le résultat.

However \( {e}^{-M} < \varepsilon \) , so \( \left| {{f}_{n}\left( x\right) - f\left( x\right) }\right| \leq {e}^{-x} \leq {e}^{-M} < \varepsilon \) on \( \lbrack M, + \infty \lbrack \) , so finally the inequality (**) is true on the whole of \( {\mathbb{R}}^{ + } \) , hence the result.

> b) Ici, les techniques précédentes ne peuvent plus s'appliquer.

b) Here, the previous techniques can no longer be applied.

> Soit \( C \) un compact de \( \mathbb{C} \) et soit \( M > 0 \) tel que \( \left| z\right| \leq M \) pour tout \( z \in C \) . L’inégalité

Let \( C \) be a compact subset of \( \mathbb{C} \) and let \( M > 0 \) be such that \( \left| z\right| \leq M \) for all \( z \in C \) . The inequality

\[
\forall n \in  {\mathbb{N}}^{ * },\forall k \leq  n,\;{C}_{n}^{k}\frac{1}{{n}^{k}} = \frac{n}{n}\frac{n - 1}{n}\cdots \frac{n - k + 1}{n}\frac{1}{k!} \leq  \frac{1}{k!}
\]

entraîne

> implies

\[
\forall z \in  C,\;\left| {{e}^{z} - {\left( 1 + \frac{z}{n}\right) }^{n}}\right|  = \left| {\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{{z}^{k}}{k!} - \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{C}_{n}^{k}}{{n}^{k}}{z}^{k}}\right|  \leq  \mathop{\sum }\limits_{{k = 0}}^{n}\left| {\frac{1}{k!} - \frac{{C}_{n}^{k}}{{n}^{k}}}\right| {\left| z\right| }^{k} + \mathop{\sum }\limits_{{k > n}}\left| \frac{{z}^{k}}{k!}\right|
\]

\[
\leq  \mathop{\sum }\limits_{{k = 0}}^{n}\left( {\frac{1}{k!} - \frac{{C}_{n}^{k}}{{n}^{k}}}\right) {M}^{k} + \mathop{\sum }\limits_{{k > n}}\frac{{M}^{k}}{k!} = {e}^{M} - {\left( 1 + \frac{M}{n}\right) }^{n}
\]

et comme \( {\left( 1 + M/n\right) }^{n} \rightarrow {e}^{M} \) lorsque \( n \rightarrow + \infty \) , on en déduit le résultat.

> and since \( {\left( 1 + M/n\right) }^{n} \rightarrow {e}^{M} \) as \( n \rightarrow + \infty \) , we deduce the result.

EXERCICE 2. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on définit l’application

> EXERCISE 2. For all \( n \in {\mathbb{N}}^{ * } \) , we define the mapping

\[
{u}_{n} : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R}\;x \mapsto  \frac{x}{{n}^{2} + {x}^{2}}.
\]

a) Montrer que la série de fonctions \( \sum {u}_{n} \) converge simplement sur \( {\mathbb{R}}^{ + } \) vers une fonction continue \( f \) mais que la convergence n’est pas uniforme sur \( {\mathbb{R}}^{ + } \) .

> a) Show that the series of functions \( \sum {u}_{n} \) converges pointwise on \( {\mathbb{R}}^{ + } \) to a continuous function \( f \) but that the convergence is not uniform on \( {\mathbb{R}}^{ + } \) .

b) Montrer que la série de fonctions \( \sum {\left( -1\right) }^{n}{u}_{n} \) converge uniformément sur \( {\mathbb{R}}^{ + } \) tout entier, mais que la convergence n’est pas normale sur \( {\mathbb{R}}^{ + } \) .

> b) Show that the series of functions \( \sum {\left( -1\right) }^{n}{u}_{n} \) converges uniformly on the whole of \( {\mathbb{R}}^{ + } \) , but that the convergence is not normal on \( {\mathbb{R}}^{ + } \) .

Solution. a) La convergence simple est immédiate car pour tout \( x \in {\mathbb{R}}^{ + } \) fixé, \( \sum x/\left( {{n}^{2} + {x}^{2}}\right) \) converge (ceci car \( x/\left( {{n}^{2} + {x}^{2}}\right) \sim x/{n}^{2} \) lorsque \( n \rightarrow + \infty \) ).

> Solution. a) Pointwise convergence is immediate because for any fixed \( x \in {\mathbb{R}}^{ + } \) , \( \sum x/\left( {{n}^{2} + {x}^{2}}\right) \) converges (this is because \( x/\left( {{n}^{2} + {x}^{2}}\right) \sim x/{n}^{2} \) as \( n \rightarrow + \infty \) ).

En revanche, il n’y a pas convergence uniforme sur \( {\mathbb{R}}^{ + } \) . En effet, la minoration

> On the other hand, there is no uniform convergence on \( {\mathbb{R}}^{ + } \) . Indeed, the lower bound

\[
\forall x > 0,\forall p \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{n = p + 1}}^{{2p}}\frac{x}{{x}^{2} + {n}^{2}} \geq  \mathop{\sum }\limits_{{n = p + 1}}^{{2p}}\frac{x}{{x}^{2} + {\left( 2p\right) }^{2}} = \frac{px}{{x}^{2} + 4{p}^{2}}
\]

(*)

> entraîne

implies

\[
\forall p \in  {\mathbb{N}}^{ * },\exists x > 0,\;\mathop{\sum }\limits_{{n = p + 1}}^{{2p}}\frac{x}{{x}^{2} + {n}^{2}} \geq  \frac{1}{5}\;\text{ (prendre }x = p\text{ dans }\left( *\right) ),
\]

autrement dit, la série de fonctions \( \sum {u}_{n} \) ne vérifie pas le critère de Cauchy uniforme sur \( {\mathbb{R}}^{ + } \) . Ceci montre qu'il n'y a pas convergence uniforme sur \( {\mathbb{R}}^{ + } \) .

> in other words, the series of functions \( \sum {u}_{n} \) does not satisfy the uniform Cauchy criterion on \( {\mathbb{R}}^{ + } \) . This shows that there is no uniform convergence on \( {\mathbb{R}}^{ + } \) .

Pour montrer la continuité de la limite simple \( f \) de \( \sum {u}_{n} \) sur \( {\mathbb{R}}^{ + } \) , il aurait été commode que la convergence soit uniforme sur \( {\mathbb{R}}^{ + } \) tout entier, mais ce n’est pas le cas. Pour contourner le problème, on va montrer que \( f \) est continue sur \( \left\lbrack {0, M}\right\rbrack \) pour tout \( M > 0 \) , ce qui entraînera la continuité de \( f \) sur \( {\mathbb{R}}^{ + } \) tout entier. Fixons donc un réel positif quelconque \( M \) . On a

> To show the continuity of the pointwise limit \( f \) of \( \sum {u}_{n} \) on \( {\mathbb{R}}^{ + } \), it would have been convenient if the convergence were uniform on the whole of \( {\mathbb{R}}^{ + } \), but this is not the case. To circumvent the problem, we will show that \( f \) is continuous on \( \left\lbrack {0, M}\right\rbrack \) for all \( M > 0 \), which will imply the continuity of \( f \) on the whole of \( {\mathbb{R}}^{ + } \). Let us therefore fix any positive real number \( M \). We have

\[
\forall n \in  {\mathbb{N}}^{ * },\forall x \in  \left\lbrack  {0, M}\right\rbrack  ,\;\left| {{u}_{n}\left( x\right) }\right|  \leq  \frac{M}{{n}^{2}},
\]

et comme la série \( \sum M/{n}^{2} \) converge, \( \sum {u}_{n} \) converge normalement, donc uniformément, sur \( \left\lbrack {0, M}\right\rbrack \) . Ainsi \( f \) , limite uniforme d’une suite de fonctions continues sur \( \left\lbrack {0, M}\right\rbrack \) , est continue sur \( \left\lbrack {0, M}\right\rbrack \) . D’où le résultat.

> and since the series \( \sum M/{n}^{2} \) converges, \( \sum {u}_{n} \) converges normally, and therefore uniformly, on \( \left\lbrack {0, M}\right\rbrack \). Thus \( f \), the uniform limit of a sequence of continuous functions on \( \left\lbrack {0, M}\right\rbrack \), is continuous on \( \left\lbrack {0, M}\right\rbrack \). Hence the result.

b) Si on fixe \( x \geq 0,\sum {\left( -1\right) }^{n}{u}_{n}\left( x\right) \) est une série numérique alternée dont la valeur absolue du terme général décroît ; la série converge donc (on le savait déjà, car on a montré plus haut qu'elle converge absolument), et de plus les restes sont majorés en valeur absolue par la valeur absolue du premier terme qui les compose (voir le théorème 6 page 214), donc

> b) If we fix \( x \geq 0,\sum {\left( -1\right) }^{n}{u}_{n}\left( x\right) \), it is an alternating numerical series whose general term's absolute value decreases; the series therefore converges (we already knew this, as we showed above that it converges absolutely), and furthermore, the remainders are bounded in absolute value by the absolute value of the first term that composes them (see theorem 6, page 214), therefore

\[
\forall p \in  {\mathbb{N}}^{ * },\;\left| {\mathop{\sum }\limits_{{n = p}}^{{+\infty }}{\left( -1\right) }^{n}\frac{x}{{x}^{2} + {n}^{2}}}\right|  \leq  \frac{x}{{x}^{2} + {p}^{2}} \leq  \frac{\sqrt{{x}^{2} + {p}^{2}}}{{x}^{2} + {p}^{2}} = \frac{1}{\sqrt{{x}^{2} + {p}^{2}}} \leq  \frac{1}{p}.
\]

Cette majoration des restes est indépendante de \( x \geq 0 \) , et elle montre que les restes tendent uniformément vers 0 sur \( {\mathbb{R}}^{ + } \) . La série de fonctions \( \sum {u}_{n} \) converge donc uniformément sur \( {\mathbb{R}}^{ + } \) .

> This bound on the remainders is independent of \( x \geq 0 \), and it shows that the remainders tend uniformly to 0 on \( {\mathbb{R}}^{ + } \). The series of functions \( \sum {u}_{n} \) therefore converges uniformly on \( {\mathbb{R}}^{ + } \).

Il n’y a pas convergence normale sur \( {\mathbb{R}}^{ + } \) tout entier, car pour tout \( n \in {\mathbb{N}}^{ * },\mathop{\sup }\limits_{{x > 0}}{u}_{n}\left( x\right) \geq \; {u}_{n}\left( n\right) = 1/\left( {2n}\right) \) et la série \( \sum 1/\left( {2n}\right) \) diverge.

> There is no normal convergence on the whole of \( {\mathbb{R}}^{ + } \), because for all \( n \in {\mathbb{N}}^{ * },\mathop{\sup }\limits_{{x > 0}}{u}_{n}\left( x\right) \geq \; {u}_{n}\left( n\right) = 1/\left( {2n}\right) \) and the series \( \sum 1/\left( {2n}\right) \) diverges.

Remarque. Retenez la méthode utilisée pour montrer la continuité de la limite simple de la série de fonctions \( \sum {u}_{n} \) : comme il n’y avait pas convergence uniforme sur \( {\mathbb{R}}^{ + } \) tout entier, nous avons montré la convergence uniforme sur \( \left\lbrack {0, M}\right\rbrack \) pour tout \( M > 0 \) . Cette technique est très classique. On procède aussi souvent ainsi pour montrer la dérivabilité d'une suite de fonctions lorsqu'il n'y a pas convergence uniforme sur l'intervalle de départ tout entier.

> Remark. Remember the method used to show the continuity of the pointwise limit of the series of functions \( \sum {u}_{n} \): since there was no uniform convergence on the whole of \( {\mathbb{R}}^{ + } \), we showed uniform convergence on \( \left\lbrack {0, M}\right\rbrack \) for all \( M > 0 \). This technique is very classic. We also often proceed in this way to show the differentiability of a sequence of functions when there is no uniform convergence on the entire starting interval.

EXERCICE 3. Que dire d’une fonction \( f : \mathbb{R} \rightarrow \mathbb{R} \) limite uniforme sur \( \mathbb{R} \) d’une suite de fonctions polynômes \( \left( {P}_{n}\right) \) ?

> EXERCISE 3. What can be said about a function \( f : \mathbb{R} \rightarrow \mathbb{R} \) that is the uniform limit on \( \mathbb{R} \) of a sequence of polynomial functions \( \left( {P}_{n}\right) \)?

Solution. Premier réflexe : \( f \) est continue. Mais il y a bien mieux, et nous allons montrer que \( f \) est une fonction polynôme. Le critère de Cauchy uniforme entraîne

> Solution. First instinct: \( f \) is continuous. But there is much more, and we will show that \( f \) is a polynomial function. The uniform Cauchy criterion implies

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\forall x \in  \mathbb{R},\;\left| {{P}_{n}\left( x\right)  - {P}_{N}\left( x\right) }\right|  \leq  1.
\]

Ainsi, pour tout \( n \geq N,{P}_{N} - {P}_{n} \) est une fonction polynôme bornée sur \( \mathbb{R} \) , donc constante. Autrement dit, pour tout \( n \geq N \) , il existe \( {\alpha }_{n} \in \mathbb{R} \) tel que \( {P}_{n} = {P}_{N} + {\alpha }_{n} \) . La suite \( \left( {{P}_{n}\left( 0\right) }\right) \) converge, donc la suite \( {\left( {\alpha }_{n}\right) }_{n \geq N} = {\left( {P}_{n}\left( 0\right) - {P}_{N}\left( 0\right) \right) }_{n \geq N} \) aussi. Notons \( \alpha \) la limite de \( \left( {\alpha }_{n}\right) \) . On a

> Thus, for all \( n \geq N,{P}_{N} - {P}_{n} \) is a bounded polynomial function on \( \mathbb{R} \), and therefore constant. In other words, for all \( n \geq N \), there exists \( {\alpha }_{n} \in \mathbb{R} \) such that \( {P}_{n} = {P}_{N} + {\alpha }_{n} \). The sequence \( \left( {{P}_{n}\left( 0\right) }\right) \) converges, so the sequence \( {\left( {\alpha }_{n}\right) }_{n \geq N} = {\left( {P}_{n}\left( 0\right) - {P}_{N}\left( 0\right) \right) }_{n \geq N} \) does as well. Let \( \alpha \) be the limit of \( \left( {\alpha }_{n}\right) \). We have

\[
\forall x \in  \mathbb{R},\;f\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{P}_{n}\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{P}_{N}\left( x\right)  + {\alpha }_{n} = {P}_{N}\left( x\right)  + \alpha ,
\]

donc \( f = {P}_{N} + \alpha \) est une fonction polynôme.

> therefore \( f = {P}_{N} + \alpha \) is a polynomial function.

EXERCICE 4. On considère la suite de fonctions \( \left( {f}_{n}\right) \) définie par

> EXERCISE 4. Consider the sequence of functions \( \left( {f}_{n}\right) \) defined by

\[
\forall n \in  \mathbb{N},\;{f}_{n} : \left\lbrack  {0,\frac{\pi }{2}}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  {\cos }^{n}x \cdot  \sin x.
\]

a) Montrer que \( \left( {f}_{n}\right) \) converge uniformément vers la fonction nulle sur \( \left\lbrack {0,\pi /2}\right\rbrack \) .

> a) Show that \( \left( {f}_{n}\right) \) converges uniformly to the zero function on \( \left\lbrack {0,\pi /2}\right\rbrack \).

b) On considère la suite de fonctions \( \left( {g}_{n}\right) \) définie par \( {g}_{n} = \left( {n + 1}\right) {f}_{n} \) . Montrer que sur tout intervalle de la forme \( \left\lbrack {\delta ,\pi /2}\right\rbrack \) avec \( 0 < \delta < \pi /2,\left( {g}_{n}\right) \) converge uniformément vers la fonction nulle, mais que pourtant, la suite \( {\left( {\int }_{0}^{\pi /2}{g}_{n}\left( t\right) dt\right) }_{n} \) ne tend pas vers 0 .

> b) Consider the sequence of functions \( \left( {g}_{n}\right) \) defined by \( {g}_{n} = \left( {n + 1}\right) {f}_{n} \). Show that on any interval of the form \( \left\lbrack {\delta ,\pi /2}\right\rbrack \) with \( 0 < \delta < \pi /2,\left( {g}_{n}\right) \) converges uniformly to the zero function, but that, nevertheless, the sequence \( {\left( {\int }_{0}^{\pi /2}{g}_{n}\left( t\right) dt\right) }_{n} \) does not tend to 0.

Solution. a) On pourrait résoudre l'exercice en essayant de majorer directement le maximum de \( \left| {f}_{n}\right| \) sur \( \left\lbrack {0,\pi /2}\right\rbrack \) en effectuant une étude de fonction, mais nous allons donner une méthode différente qui est plus générale et qui a son intérêt.

> Solution. a) One could solve the exercise by trying to directly bound the maximum of \( \left| {f}_{n}\right| \) on \( \left\lbrack {0,\pi /2}\right\rbrack \) by performing a function study, but we will provide a different method that is more general and of interest.

Analysons la situation. On a \( {\cos }^{n}x \rightarrow 0 \) lorsque \( n \rightarrow + \infty \) uniformément lorsque \( x \) est dans \( \left\lbrack {0,\pi /2}\right\rbrack \) et n’est pas dans un voisinage de 0 . Au voisinage de 0, la fonction sinus est petite. Pour tirer parti de ces deux informations on procède comme suit.

> Let us analyze the situation. We have \( {\cos }^{n}x \rightarrow 0 \) as \( n \rightarrow + \infty \) uniformly when \( x \) is in \( \left\lbrack {0,\pi /2}\right\rbrack \) and is not in a neighborhood of 0. In the neighborhood of 0, the sine function is small. To take advantage of these two pieces of information, we proceed as follows.

Un nombre réel \( \varepsilon > 0 \) étant donné, on considère \( \delta > 0 \) (et \( \delta < \pi /2 \) ) tel que \( \left| {\sin x}\right| < \varepsilon \) sur \( \left\lbrack {0,\delta }\right\rbrack \) (ceci est possible par continuité de la fonction sinus qui est nulle en 0). Sur le reste de l'intervalle, on a

> Given a real number \( \varepsilon > 0 \), we consider \( \delta > 0 \) (and \( \delta < \pi /2 \)) such that \( \left| {\sin x}\right| < \varepsilon \) on \( \left\lbrack {0,\delta }\right\rbrack \) (this is possible by the continuity of the sine function, which is zero at 0). On the rest of the interval, we have

\[
\forall x \in  \left\lbrack  {\delta ,\frac{\pi }{2}}\right\rbrack  ,\forall n \in  \mathbb{N},\;\left| {{f}_{n}\left( x\right) }\right|  \leq  {\left( \cos \delta \right) }^{n},
\]

et comme \( {\left( \cos \delta \right) }^{n} \) tend vers \( 0\left( {\operatorname{car}\left| {\cos \delta }\right| < 1}\right) \) , on en déduit

> and since \( {\left( \cos \delta \right) }^{n} \) tends to \( 0\left( {\operatorname{car}\left| {\cos \delta }\right| < 1}\right) \), we deduce

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\forall x \in  \left\lbrack  {\delta ,\frac{\pi }{2}}\right\rbrack  ,\;\left| {{f}_{n}\left( x\right) }\right|  < \varepsilon .
\]

Comme \( \left| {\sin x}\right| < \varepsilon \) sur \( \left\lbrack {0,\delta }\right\rbrack \) , on a aussi \( \left| {{f}_{n}\left( x\right) }\right| < \varepsilon \) sur \( \left\lbrack {0,\delta }\right\rbrack \) pour tout \( n \) , donc finalement

> As \( \left| {\sin x}\right| < \varepsilon \) on \( \left\lbrack {0,\delta }\right\rbrack \), we also have \( \left| {{f}_{n}\left( x\right) }\right| < \varepsilon \) on \( \left\lbrack {0,\delta }\right\rbrack \) for all \( n \), so finally

\[
\forall n \geq  N,\forall x \in  \left\lbrack  {0,\frac{\pi }{2}}\right\rbrack  ,\;\left| {{f}_{n}\left( x\right) }\right|  < \varepsilon .
\]

b) La convergence uniforme de \( \left( {g}_{n}\right) \) vers0sur \( \left\lbrack {\delta ,\pi /2}\right\rbrack \) est une conséquence de l’inégalité

> b) The uniform convergence of \( \left( {g}_{n}\right) \) to 0 on \( \left\lbrack {\delta ,\pi /2}\right\rbrack \) is a consequence of the inequality

\[
\forall x \in  \left\lbrack  {\delta ,\frac{\pi }{2}}\right\rbrack  ,\forall n \in  \mathbb{N},\;\left| {{g}_{n}\left( x\right) }\right|  \leq  \left( {n + 1}\right) {\cos }^{n}x \leq  \left( {n + 1}\right) {\cos }^{n}\delta
\]

et du fait que \( \left( {n + 1}\right) {\cos }^{n}\delta \rightarrow 0 \) lorsque \( n \rightarrow + \infty \) (ceci car \( \left| {\cos \delta }\right| < 1 \) ).

> and the fact that \( \left( {n + 1}\right) {\cos }^{n}\delta \rightarrow 0 \) as \( n \rightarrow + \infty \) (this is because \( \left| {\cos \delta }\right| < 1 \) ).

Comme \( {\int }_{0}^{\pi /2}{g}_{n}\left( x\right) {dx} = {\left\lbrack -{\cos }^{n + 1}x\right\rbrack }_{0}^{\pi /2} = 1 \) , il est clair que la suite des intégrales de \( {g}_{n} \) ne tend pas vers 0 .

> Since \( {\int }_{0}^{\pi /2}{g}_{n}\left( x\right) {dx} = {\left\lbrack -{\cos }^{n + 1}x\right\rbrack }_{0}^{\pi /2} = 1 \) , it is clear that the sequence of integrals of \( {g}_{n} \) does not tend to 0 .

Remarque. La dernière question de l'exercice est un contre-exemple qui montre que le théorème de convergence dominée (page 151) est faux lorsque la condition de domination n'est pas satisfaite.

> Remark. The last question of the exercise is a counterexample showing that the dominated convergence theorem (page 151) is false when the domination condition is not satisfied.

EXERCICE 5 (THÉORÉMES DE DINI). a) Soit \( \left( {f}_{n}\right) \) une suite croissante de fonctions réelles continues et définies sur un segment \( I = \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) . Si \( \left( {f}_{n}\right) \) converge simplement vers une fonction \( f \) continue sur \( I \) , montrer que la convergence est uniforme.

> EXERCISE 5 (DINI'S THEOREMS). a) Let \( \left( {f}_{n}\right) \) be an increasing sequence of real continuous functions defined on a segment \( I = \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) . If \( \left( {f}_{n}\right) \) converges pointwise to a function \( f \) continuous on \( I \) , show that the convergence is uniform.

b) Soit \( \left( {f}_{n}\right) \) une suite de fonctions croissantes réelles, continues et définies sur un segment

> b) Let \( \left( {f}_{n}\right) \) be a sequence of real increasing functions, continuous and defined on a segment

\( I = \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) . Si \( \left( {f}_{n}\right) \) converge simplement vers une fonction \( f \) continue sur \( I \) , montrer que la convergence est uniforme.

> \( I = \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) . If \( \left( {f}_{n}\right) \) converges pointwise to a function \( f \) continuous on \( I \) , show that the convergence is uniform.

Solution. a) Soit \( \varepsilon > 0 \) . Pour tout \( n \) , considérons l’ensemble

> Solution. a) Let \( \varepsilon > 0 \) . For any \( n \) , consider the set

\[
{F}_{n} = \left\{  {x \in  I \mid  f\left( x\right)  \geq  {f}_{n}\left( x\right)  + \varepsilon }\right\}  .
\]

La suite \( \left( {F}_{n}\right) \) est une suite décroissante de fermés de \( I \) (donc compacts). On a \( { \cap }_{n \geq 0}{F}_{n} = \varnothing \) car pour tout \( x \in I,{f}_{n}\left( x\right) \) converge vers \( f\left( x\right) \) donc il existe \( n \) tel que \( f\left( x\right) < \varepsilon + {f}_{n}\left( x\right) \) , ce qui entraîne \( x \notin {F}_{n} \) . Une suite décroissante de compacts non vide est non vide, donc il existe \( N \) tel que \( {F}_{N} = \varnothing \) , autrement dit \( f < \varepsilon + {f}_{n} \) sur \( I \) pour \( n \geq N \) . Comme la suite \( \left( {f}_{n}\right) \) est croissante, on a également \( {f}_{n} \leq f \) , donc finalement \( {f}_{n} \leq f < \varepsilon + {f}_{n} \) pour \( n \geq N \) d’où le résultat.

> The sequence \( \left( {F}_{n}\right) \) is a decreasing sequence of closed sets of \( I \) (therefore compact). We have \( { \cap }_{n \geq 0}{F}_{n} = \varnothing \) because for any \( x \in I,{f}_{n}\left( x\right) \) converges to \( f\left( x\right) \) so there exists \( n \) such that \( f\left( x\right) < \varepsilon + {f}_{n}\left( x\right) \) , which implies \( x \notin {F}_{n} \) . A decreasing sequence of non-empty compact sets is non-empty, so there exists \( N \) such that \( {F}_{N} = \varnothing \) , in other words \( f < \varepsilon + {f}_{n} \) on \( I \) for \( n \geq N \) . As the sequence \( \left( {f}_{n}\right) \) is increasing, we also have \( {f}_{n} \leq f \) , so finally \( {f}_{n} \leq f < \varepsilon + {f}_{n} \) for \( n \geq N \) hence the result.

b) Tout d'abord, la fonction \( f \) est limite simple de fonctions croissantes, elle est donc croissante. Donnons nous \( \varepsilon > 0 \) . La fonction \( f \) est continue sur le compact \( I \) , donc d’après le théorème de Heine

> b) First of all, the function \( f \) is the pointwise limit of increasing functions, it is therefore increasing. Let us choose \( \varepsilon > 0 \) . The function \( f \) is continuous on the compact \( I \) , so according to the Heine theorem

\[
\exists \eta  > 0,\forall \left( {x,{x}^{\prime }}\right)  \in  {I}^{2},\left| {x - {x}^{\prime }}\right|  < \eta ,\;\left| {f\left( x\right)  - f\left( {x}^{\prime }\right) }\right|  < \varepsilon .
\]

On considère ensuite une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) de \( I \) de pas \( < \eta \) , c’est-à-dire telle que \( {x}_{i + 1} - {x}_{i} < \eta \) pour tout \( i \) . Pour tout \( i \in \{ 0,1,\ldots , p\} \) , la suite \( \left( {{f}_{n}\left( {x}_{i}\right) }\right) \) tend vers \( f\left( {x}_{i}\right) \) , on en déduit (les \( i \) étant en nombre fini)

> Next, we consider a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) of \( I \) with step \( < \eta \), that is to say such that \( {x}_{i + 1} - {x}_{i} < \eta \) for all \( i \). For all \( i \in \{ 0,1,\ldots , p\} \), the sequence \( \left( {{f}_{n}\left( {x}_{i}\right) }\right) \) tends to \( f\left( {x}_{i}\right) \), from which we deduce (the \( i \) being finite in number)

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\forall i \in  \{ 0,\ldots , p\} ,\;\left| {{f}_{n}\left( {x}_{i}\right)  - f\left( {x}_{i}\right) }\right|  < \varepsilon .
\]

Ceci étant, considérons \( x \in I \) . Il existe \( i \in \{ 0,\ldots , p - 1\} \) tel que \( x \in \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) , et les fonctions \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) et \( f \) étant croissantes

> This being so, let us consider \( x \in I \). There exists \( i \in \{ 0,\ldots , p - 1\} \) such that \( x \in \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \), and the functions \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) and \( f \) being increasing

\[
\forall n \in  \mathbb{N},\;{f}_{n}\left( {x}_{i}\right)  \leq  {f}_{n}\left( x\right)  \leq  {f}_{n}\left( {x}_{i + 1}\right) \;\text{ et }\;f\left( {x}_{i}\right)  \leq  f\left( x\right)  \leq  f\left( {x}_{i + 1}\right) ,
\]

donc

> therefore

\[
\forall n \in  \mathbb{N},\;f\left( {x}_{i}\right)  - {f}_{n}\left( {x}_{i + 1}\right)  \leq  f\left( x\right)  - {f}_{n}\left( x\right)  \leq  f\left( {x}_{i + 1}\right)  - {f}_{n}\left( {x}_{i}\right) .
\]

(*)

> Or pour tout \( n \geq N \) ,

However, for all \( n \geq N \),

\[
\left| {f\left( {x}_{i + 1}\right)  - {f}_{n}\left( {x}_{i}\right) }\right|  \leq  \left| {f\left( {x}_{i + 1}\right)  - f\left( {x}_{i}\right) }\right|  + \left| {f\left( {x}_{i}\right)  - {f}_{n}\left( {x}_{i}\right) }\right|  < {2\varepsilon },
\]

de même \( \left| {f\left( {x}_{i}\right) - {f}_{n}\left( {x}_{i + 1}\right) }\right| < {2\varepsilon } \) . On en déduit avec (*) que \( \left| {f\left( x\right) - {f}_{n}\left( x\right) }\right| < {2\varepsilon } \) , et ceci pour tout \( n \geq N \) et pour tout \( x \in I \) , d’où le résultat.

> similarly \( \left| {f\left( {x}_{i}\right) - {f}_{n}\left( {x}_{i + 1}\right) }\right| < {2\varepsilon } \). We deduce from (*) that \( \left| {f\left( x\right) - {f}_{n}\left( x\right) }\right| < {2\varepsilon } \), and this for all \( n \geq N \) and for all \( x \in I \), hence the result.

EXERCICE 6. a) Soit \( \left( {f}_{n}\right) \) une suite de fonctions d’un segment \( I = \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) à valeurs dans un \( \mathbb{R} \) -e.v.n \( E \) . On suppose qu’il existe \( K > 0 \) tel que toutes les fonctions \( {f}_{n} \) soient \( K \) -lipschitziennes. Si \( \left( {f}_{n}\right) \) converge simplement vers une fonction \( f : I \rightarrow E \) , montrer que la convergence est uniforme.

> EXERCISE 6. a) Let \( \left( {f}_{n}\right) \) be a sequence of functions from a segment \( I = \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) with values in an \( \mathbb{R} \)-n.v.s. \( E \). Suppose there exists \( K > 0 \) such that all functions \( {f}_{n} \) are \( K \)-Lipschitz. If \( \left( {f}_{n}\right) \) converges pointwise to a function \( f : I \rightarrow E \), show that the convergence is uniform.

b) Soit \( \left( {f}_{n}\right) \) une suite de fonctions convexes de \( \rbrack a, b\left\lbrack \right. \) dans \( \mathbb{R} \) (où \( \rbrack a, b\lbrack \) est un intervalle de \( \mathbb{R}) \) qui converge simplement vers une fonction \( f : \rbrack a, b\left\lbrack { \rightarrow \mathbb{R}}\right. \) . Montrer que sur tout segment \( \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \) , la suite \( \left( {f}_{n}\right) \) converge uniformément vers \( f \) . La convergence est-elle uniforme sur \( \rbrack a, b\left\lbrack \right. \) tout entier ?

> b) Let \( \left( {f}_{n}\right) \) be a sequence of convex functions from \( \rbrack a, b\left\lbrack \right. \) to \( \mathbb{R} \) (where \( \rbrack a, b\lbrack \) is an interval of \( \mathbb{R}) \)) which converges pointwise to a function \( f : \rbrack a, b\left\lbrack { \rightarrow \mathbb{R}}\right. \). Show that on any segment \( \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \), the sequence \( \left( {f}_{n}\right) \) converges uniformly to \( f \). Is the convergence uniform on the whole of \( \rbrack a, b\left\lbrack \right. \)?

Solution. a) La technique ressemble assez à celles utilisées dans l'exercice précédent. Remarquons tout d’abord que \( f \) , limite simple de fonctions \( K \) -lipschitziennes, est \( K \) -lipschitzienne.

> Solution. a) The technique is quite similar to those used in the previous exercise. Let us first note that \( f \), the pointwise limit of \( K \)-Lipschitz functions, is \( K \)-Lipschitz.

Soit \( \varepsilon > 0 \) et soit \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) une subdivision de \( \left\lbrack {a, b}\right\rbrack \) de pas \( < \varepsilon \) (i.e. \( {x}_{i + 1} - {x}_{i} < \varepsilon \) pour tout \( i \) ). Pour tout \( i \in \{ 0,1,\ldots , p\} \) , la suite \( \left( {{f}_{n}\left( {x}_{i}\right) }\right) \) converge vers \( f\left( {x}_{i}\right) \) donc (les \( i \) sont en nombre finis)

> Let \( \varepsilon > 0 \) and let \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) be a subdivision of \( \left\lbrack {a, b}\right\rbrack \) with step \( < \varepsilon \) (i.e. \( {x}_{i + 1} - {x}_{i} < \varepsilon \) for all \( i \) ). For all \( i \in \{ 0,1,\ldots , p\} \) , the sequence \( \left( {{f}_{n}\left( {x}_{i}\right) }\right) \) converges to \( f\left( {x}_{i}\right) \) therefore (the \( i \) are finite in number)

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\forall i \in  \{ 0,1,\ldots , p\} ,\;\begin{Vmatrix}{{f}_{n}\left( {x}_{i}\right)  - f\left( {x}_{i}\right) }\end{Vmatrix} < \varepsilon .
\]

Si maintenant on considère \( x \in I \) , il existe \( i \) tel que \( x \in \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) donc les fonctions en présence étant toutes \( K \) -lipschitziennes, on a pour tout \( n \geq N \)

> If we now consider \( x \in I \) , there exists \( i \) such that \( x \in \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) therefore, as the functions involved are all \( K \) -Lipschitz, we have for all \( n \geq N \)

\[
\begin{Vmatrix}{{f}_{n}\left( x\right)  - f\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{f}_{n}\left( x\right)  - {f}_{n}\left( {x}_{i}\right) }\end{Vmatrix} + \begin{Vmatrix}{{f}_{n}\left( {x}_{i}\right)  - f\left( {x}_{i}\right) }\end{Vmatrix} + \begin{Vmatrix}{f\left( {x}_{i}\right)  - f\left( x\right) }\end{Vmatrix}
\]

\[
\leq  K\left( {x - {x}_{i}}\right)  + \varepsilon  + K\left( {x - {x}_{i}}\right)  \leq  \left( {{2K} + 1}\right) \varepsilon .
\]

Ceci étant vrai pour tout \( x \in I \) et pour tout \( n \geq N \) , on en déduit le résultat.

> Since this is true for all \( x \in I \) and for all \( n \geq N \) , we deduce the result.

b) L’idée est de se ramener à la question précédente. Soit \( I = \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \) . Fixons \( {\alpha }^{\prime },{\beta }^{\prime } \) tels que \( a < {\alpha }^{\prime } < \alpha < \beta < {\beta }^{\prime } < b \) . Les suites

> b) The idea is to reduce it to the previous question. Let \( I = \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \) . Let us fix \( {\alpha }^{\prime },{\beta }^{\prime } \) such that \( a < {\alpha }^{\prime } < \alpha < \beta < {\beta }^{\prime } < b \) . The sequences

\[
{\left( \frac{{f}_{n}\left( {\alpha }^{\prime }\right)  - {f}_{n}\left( \alpha \right) }{{\alpha }^{\prime } - \alpha }\right) }_{n \in  \mathbb{N}}\;\text{ et }\;{\left( \frac{{f}_{n}\left( \beta \right)  - {f}_{n}\left( {\beta }^{\prime }\right) }{\beta  - {\beta }^{\prime }}\right) }_{n \in  \mathbb{N}}
\]

convergent (conséquence de la convergence simple de \( \left( {f}_{n}\right) \) ), elles sont donc bornées. Désignons par \( K > 0 \) un majorant de la valeur absolue des termes de ces suites. Chaque fonction \( {f}_{n} \) étant convexe, on en déduit pour tout \( n \)

> converge (a consequence of the pointwise convergence of \( \left( {f}_{n}\right) \) ), so they are bounded. Let \( K > 0 \) denote an upper bound of the absolute value of the terms of these sequences. Since each function \( {f}_{n} \) is convex, we deduce for all \( n \)

\[
\forall \left( {x, y}\right)  \in  {\left\lbrack  \alpha ,\beta \right\rbrack  }^{2},\; - K \leq  \frac{{f}_{n}\left( {\alpha }^{\prime }\right)  - {f}_{n}\left( \alpha \right) }{{\alpha }^{\prime } - \alpha } \leq  \frac{{f}_{n}\left( x\right)  - f\left( y\right) }{x - y} \leq  \frac{{f}_{n}\left( \beta \right)  - {f}_{n}\left( {\beta }^{\prime }\right) }{\beta  - {\beta }^{\prime }} \leq  K,
\]

donc \( \left| {{f}_{n}\left( x\right) - {f}_{n}\left( y\right) }\right| \leq K\left| {x - y}\right| \) . Ainsi, toutes les fonctions \( {f}_{n} \) sont \( K \) -lipschitziennes sur \( \left\lbrack {\alpha ,\beta }\right\rbrack \) , et on conclut en utilisant le résultat de la question précédente.

> therefore \( \left| {{f}_{n}\left( x\right) - {f}_{n}\left( y\right) }\right| \leq K\left| {x - y}\right| \) . Thus, all functions \( {f}_{n} \) are \( K \) -Lipschitz on \( \left\lbrack {\alpha ,\beta }\right\rbrack \) , and we conclude by using the result of the previous question.

Il n’y a pas en général convergence uniforme sur \( \rbrack a, b\left\lbrack \right. \) tout entier, comme le montre le contre-exemple classique de la suite de fonctions convexes \( \left( {f}_{n}\right) \) définies par \( {f}_{n} : \rbrack 0,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n} \) qui converge simplement vers 0 sur \( \rbrack 0,1\left\lbrack \right. \) mais pas uniformément.

> There is generally no uniform convergence on the whole of \( \rbrack a, b\left\lbrack \right. \) , as shown by the classic counterexample of the sequence of convex functions \( \left( {f}_{n}\right) \) defined by \( {f}_{n} : \rbrack 0,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n} \) which converges pointwise to 0 on \( \rbrack 0,1\left\lbrack \right. \) but not uniformly.

EXERCICE 7 (PHÉNOMENE DE RUNGE). Soit \( \alpha > 0 \) et \( {f}_{\alpha } \) la fonction

> EXERCISE 7 (RUNGE'S PHENOMENON). Let \( \alpha > 0 \) and \( {f}_{\alpha } \) be the function

\[
{f}_{\alpha } : \left\lbrack  {-1,1}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \frac{1}{{x}^{2} + {\alpha }^{2}}.
\]

Soit \( n \in {\mathbb{N}}^{ * } \) . On considère les \( {2n} \) points équirépartis dans \( \left\lbrack {-1,1}\right\rbrack \) définis par \( {a}_{k} = ({2k} + \) 1) \( /\left( {2n}\right) \) pour \( - n \leq k \leq n - 1 \) . On note \( {P}_{n} \) le polynôme d’interpolation de Lagrange de degré \( < {2n} \) déterminé par les conditions \( {P}_{n}\left( {a}_{k}\right) = {f}_{\alpha }\left( {a}_{k}\right) \) pour \( - n \leq k \leq n - 1 \) . On veut montrer que la suite de fonctions polynômes \( \left( {P}_{n}\right) \) ne converge pas forcément uniformément vers \( {f}_{\alpha } \) sur \( \left\lbrack {-1,1}\right\rbrack \) (c’est le phénomène de Runge).

> Let \( n \in {\mathbb{N}}^{ * } \) . Consider the \( {2n} \) equally spaced points in \( \left\lbrack {-1,1}\right\rbrack \) defined by \( {a}_{k} = ({2k} + \) 1) \( /\left( {2n}\right) \) for \( - n \leq k \leq n - 1 \) . Let \( {P}_{n} \) denote the Lagrange interpolation polynomial of degree \( < {2n} \) determined by the conditions \( {P}_{n}\left( {a}_{k}\right) = {f}_{\alpha }\left( {a}_{k}\right) \) for \( - n \leq k \leq n - 1 \) . We want to show that the sequence of polynomial functions \( \left( {P}_{n}\right) \) does not necessarily converge uniformly to \( {f}_{\alpha } \) on \( \left\lbrack {-1,1}\right\rbrack \) (this is the Runge phenomenon).

a) Montrer la formule

> a) Show the formula

\[
{f}_{\alpha }\left( x\right)  - {P}_{n}\left( x\right)  = \frac{1}{{x}^{2} + {\alpha }^{2}}\frac{{\omega }_{n}\left( x\right) }{{\omega }_{n}\left( {\alpha i}\right) },\;\text{ avec }\;{\omega }_{n}\left( x\right)  = \mathop{\prod }\limits_{{k =  - n}}^{{n - 1}}\left( {x - {a}_{k}}\right) .
\]

b) En déduire le premier terme du développement asymptotique de \( \log \left| {{f}_{\alpha }\left( 1\right) - {P}_{n}\left( 1\right) }\right| \) lorsque \( n \rightarrow \infty \) .

> b) Deduce the first term of the asymptotic expansion of \( \log \left| {{f}_{\alpha }\left( 1\right) - {P}_{n}\left( 1\right) }\right| \) as \( n \rightarrow \infty \) .

c) Montrer que si \( \alpha > 0 \) est suffisamment petit, la suite de fonctions \( \left( {P}_{n}\right) \) ne converge pas uniformément vers \( {f}_{\alpha } \) .

> c) Show that if \( \alpha > 0 \) is sufficiently small, the sequence of functions \( \left( {P}_{n}\right) \) does not converge uniformly to \( {f}_{\alpha } \) .

Solution. a) Il est classique que le polynôme d'interpolation de Lagrange \( {P}_{n} \) existe et s'écrit sous la forme (voir le tome Algèbre)

> Solution. a) It is standard that the Lagrange interpolation polynomial \( {P}_{n} \) exists and can be written in the form (see the Algebra volume)

\[
{P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k =  - n}}^{{n - 1}}\frac{{f}_{\alpha }\left( {a}_{k}\right) {\omega }_{n}\left( x\right) }{\left( {x - {a}_{k}}\right) {\omega }_{n}^{\prime }\left( {a}_{k}\right) }.
\]

(*)

> La clé est maintenant d’utiliser la décomposition en éléments simples de la fraction \( {f}_{\alpha }\left( x\right) /{\omega }_{n}\left( x\right) \) . Cette dernière n’a que des pôles simples, qui sont \( {\alpha i}, - {\alpha i} \) et les \( {\left( {a}_{k}\right) }_{-n \leq k \leq n - 1} \) , on peut donc écrire sa décomposition en éléments simples (voir le tome Algèbre) sous la forme

The key is now to use the partial fraction decomposition of the fraction \( {f}_{\alpha }\left( x\right) /{\omega }_{n}\left( x\right) \) . The latter has only simple poles, which are \( {\alpha i}, - {\alpha i} \) and the \( {\left( {a}_{k}\right) }_{-n \leq k \leq n - 1} \) , so we can write its partial fraction decomposition (see the Algebra volume) in the form

\[
\frac{{f}_{\alpha }\left( x\right) }{{\omega }_{n}\left( x\right) } = \mathop{\sum }\limits_{{k =  - n}}^{{n - 1}}\frac{{f}_{\alpha }\left( {a}_{k}\right) }{\left( {x - {a}_{k}}\right) {\omega }_{n}^{\prime }\left( {a}_{k}\right) } + \frac{1}{{\omega }_{n}\left( {-{i\alpha }}\right) }\frac{i}{{2\alpha }\left( {x + {i\alpha }}\right) } - \frac{1}{{\omega }_{n}\left( {i\alpha }\right) }\frac{i}{{2\alpha }\left( {x - {i\alpha }}\right) }.
\]

(**)

> La relation de symétrie autour de zéro \( {a}_{-j} = - {a}_{j - 1} \) pour \( 1 \leq j \leq n \) donne

The symmetry relation around zero \( {a}_{-j} = - {a}_{j - 1} \) for \( 1 \leq j \leq n \) gives

\[
{\omega }_{n}\left( x\right)  = \mathop{\prod }\limits_{{j = 1}}^{n}\left( {x - {a}_{-j}}\right) \mathop{\prod }\limits_{{j = 1}}^{n}\left( {x - {a}_{j - 1}}\right)  = \mathop{\prod }\limits_{{j = 1}}^{n}\left( {x + {a}_{j - 1}}\right) \left( {x - {a}_{j - 1}}\right)  = \mathop{\prod }\limits_{{j = 0}}^{{n - 1}}\left( {{x}^{2} - {a}_{j}^{2}}\right)
\]

donc la fonction polynôme \( {\omega }_{n}\left( x\right) \) est paire, ce qui fournit \( {\omega }_{n}\left( {-{i\alpha }}\right) = {\omega }_{n}\left( {i\alpha }\right) \) . Avec (*) et (**), on en déduit l’égalité \( {f}_{\alpha }\left( x\right) /{\omega }_{n}\left( x\right) = {P}_{n}\left( x\right) /{\omega }_{n}\left( x\right) + 1/\left( {{x}^{2} + {\alpha }^{2}}\right) /{\omega }_{n}\left( {i\alpha }\right) \) , d’où le résultat.

> therefore the polynomial function \( {\omega }_{n}\left( x\right) \) is even, which provides \( {\omega }_{n}\left( {-{i\alpha }}\right) = {\omega }_{n}\left( {i\alpha }\right) \) . With (*) and (**), we deduce the equality \( {f}_{\alpha }\left( x\right) /{\omega }_{n}\left( x\right) = {P}_{n}\left( x\right) /{\omega }_{n}\left( x\right) + 1/\left( {{x}^{2} + {\alpha }^{2}}\right) /{\omega }_{n}\left( {i\alpha }\right) \) , hence the result.

b) L’expression de \( {\omega }_{n}\left( x\right) \) que nous avions obtenu précédemment donne

> b) The expression for \( {\omega }_{n}\left( x\right) \) that we obtained previously gives

\[
\frac{{\omega }_{n}\left( 1\right) }{{\omega }_{n}\left( {i\alpha }\right) } = \mathop{\prod }\limits_{{j = 0}}^{{n - 1}}\left( \frac{1 - {a}_{j}^{2}}{-{\alpha }^{2} - {a}_{j}^{2}}\right)  = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{j = 0}}^{{n - 1}}\left( \frac{1 - {a}_{j}^{2}}{{\alpha }^{2} + {a}_{j}^{2}}\right)
\]

D'après le résultat obtenu à la question précédente, on a donc

> According to the result obtained in the previous question, we therefore have

\[
\log \left| {{f}_{\alpha }\left( 1\right)  - {P}_{n}\left( 1\right) }\right|  = \log \frac{1}{1 + {\alpha }^{2}} + \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}\log \frac{1 - {a}_{j}^{2}}{{\alpha }^{2} + {a}_{j}^{2}}.
\]

\( \left( {* * * }\right) \)

> Le dernier terme du membre droit est, au facteur 1/n près, une somme de Riemann de la fonction \( {\varphi }_{\alpha }\left( t\right) = \log \frac{1 - {t}^{2}}{{\alpha }^{2} + {t}^{2}} \) pour une subdivision de \( \left\lbrack {0,1}\right\rbrack \) ; nous sommes ici en présence d’une intégrale généralisée et on ne peut donc pas appliquer le théorème 7 page 128. On va procéder comme à l’exercice 5 page 156. Notons d’abord que l’intégrale généralisée \( I\left( \alpha \right) = {\int }_{0}^{1}{\varphi }_{\alpha }\left( t\right) {dt} \) converge (on l’obtient facilement en écrivant \( {\varphi }_{\alpha }\left( t\right) = \log \left( {1 - t}\right) + \log \frac{1 + t}{{\alpha }^{2} + {t}^{2}}) \) . Maintenant, on remarque que \( {\varphi }_{\alpha } \) est décroissante sur \( \rbrack 0,1\rbrack \) (composition de la fonction décroissante \( t \mapsto \left( {1 - {t}^{2}}\right) /\left( {{\alpha }^{2} + {t}^{2}}\right) \) par la fonction log qui est croissante), donc \( {\int }_{{a}_{j}}^{{a}_{j + 1}}{\varphi }_{\alpha }\left( t\right) {dt} \leq \frac{1}{n}{\varphi }_{\alpha }\left( {a}_{j}\right) \leq {\int }_{{a}_{j - 1}}^{{a}_{j}}{\varphi }_{\alpha }\left( t\right) {dt} \) , ce qui, par sommation pour \( 1 \leq j \leq n - 2 \) donne

The last term on the right-hand side is, up to a factor of 1/n, a Riemann sum of the function \( {\varphi }_{\alpha }\left( t\right) = \log \frac{1 - {t}^{2}}{{\alpha }^{2} + {t}^{2}} \) for a subdivision of \( \left\lbrack {0,1}\right\rbrack \); we are dealing here with a generalized integral, and therefore Theorem 7 on page 128 cannot be applied. We will proceed as in exercise 5 on page 156. Let us first note that the generalized integral \( I\left( \alpha \right) = {\int }_{0}^{1}{\varphi }_{\alpha }\left( t\right) {dt} \) converges (this is easily obtained by writing \( {\varphi }_{\alpha }\left( t\right) = \log \left( {1 - t}\right) + \log \frac{1 + t}{{\alpha }^{2} + {t}^{2}}) \)). Now, we observe that \( {\varphi }_{\alpha } \) is decreasing on \( \rbrack 0,1\rbrack \) (composition of the decreasing function \( t \mapsto \left( {1 - {t}^{2}}\right) /\left( {{\alpha }^{2} + {t}^{2}}\right) \) with the log function, which is increasing), so \( {\int }_{{a}_{j}}^{{a}_{j + 1}}{\varphi }_{\alpha }\left( t\right) {dt} \leq \frac{1}{n}{\varphi }_{\alpha }\left( {a}_{j}\right) \leq {\int }_{{a}_{j - 1}}^{{a}_{j}}{\varphi }_{\alpha }\left( t\right) {dt} \), which, by summation for \( 1 \leq j \leq n - 2 \), gives

\[
I\left( \alpha \right)  + o\left( 1\right)  = {\int }_{3/\left( {2n}\right) }^{1 - 1/\left( {2n}\right) }{\varphi }_{\alpha }\left( t\right) {dt} \leq  \frac{1}{n}\mathop{\sum }\limits_{{j = 1}}^{{n - 2}}{\varphi }_{\alpha }\left( {a}_{j}\right)  \leq  {\int }_{1/\left( {2n}\right) }^{1 - 3/\left( {2n}\right) }{\varphi }_{\alpha }\left( t\right) {dt} = I\left( \alpha \right)  + o\left( 1\right) .
\]

Donc \( \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\varphi }_{\alpha }\left( {a}_{j}\right) = {nI}\left( \alpha \right) + o\left( n\right) \) (on a bien \( {\varphi }_{\alpha }\left( {a}_{0}\right) + {\varphi }_{\alpha }\left( {a}_{n - 1}\right) = o\left( n\right) \) ). Avec (***), on en déduit finalement, lorsque \( n \rightarrow \infty \) ,

> Thus \( \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\varphi }_{\alpha }\left( {a}_{j}\right) = {nI}\left( \alpha \right) + o\left( n\right) \) (we indeed have \( {\varphi }_{\alpha }\left( {a}_{0}\right) + {\varphi }_{\alpha }\left( {a}_{n - 1}\right) = o\left( n\right) \)). With (***), we finally deduce, as \( n \rightarrow \infty \),

\[
\log \left| {{f}_{\alpha }\left( 1\right)  - {P}_{n}\left( 1\right) }\right|  = \log \frac{1}{1 + {\alpha }^{2}} + n\left( {I\left( \alpha \right)  + o\left( 1\right) }\right) ,\;\text{ avec }\;I\left( \alpha \right)  = {\int }_{0}^{1}\log \frac{1 - {t}^{2}}{{\alpha }^{2} + {t}^{2}}{dt}.
\]

c) Nous allons montrer que \( I \) est définie et continue en 0 . Lorsque \( \alpha \in \left\lbrack {0,1}\right\rbrack \) et \( 0 < t \leq 1 \) , on a

> c) We will show that \( I \) is defined and continuous at 0. When \( \alpha \in \left\lbrack {0,1}\right\rbrack \) and \( 0 < t \leq 1 \), we have

\[
{\alpha }^{2} + {t}^{2} \leq  2\text{ et }\frac{1}{{\alpha }^{2} + {t}^{2}} \leq  \frac{1}{{t}^{2}}\text{ donc }\left| {\log \left( {{\alpha }^{2} + {t}^{2}}\right) }\right|  \leq  \max \left( {\log 2,\log \frac{1}{{t}^{2}}}\right)  \leq  \log \frac{2}{{t}^{2}}.
\]

Comme la fonction \( t \mapsto \log \left( {2/{t}^{2}}\right) \) est intégrable sur \( \rbrack 0,1\rbrack \) , l’hypothèse de domination est vérifiée donc la fonction \( \alpha \mapsto {\int }_{0}^{1}\log \left( {{\alpha }^{2} + {t}^{2}}\right) {dt} \) est bien définie et continue pour \( \alpha \in \left\lbrack {0,1}\right\rbrack \) . En particulier, \( I \) est définie et continue en \( \alpha = 0 \) , et comme \( I\left( 0\right) = 2\log 2 > 0 \) , on en déduit l’existence de \( {\alpha }_{0} > 0 \) tel que \( I\left( \alpha \right) > 0 \) pour \( 0 \leq \alpha < {\alpha }_{0} \) . D’après le développement asymptotique obtenu à la question précédente, lorsque \( 0 \leq \alpha < {\alpha }_{0} \) , on a donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\log \left| {{f}_{\alpha }\left( 1\right) - {P}_{n}\left( 1\right) }\right| = + \infty \) . Ainsi il n’y a pas convergence simple (et donc pas uniforme) de \( \left( {P}_{n}\right) \) vers \( f \) lorsque \( 0 \leq \alpha < {\alpha }_{0} \) .

> Since the function \( t \mapsto \log \left( {2/{t}^{2}}\right) \) is integrable on \( \rbrack 0,1\rbrack \), the domination hypothesis is satisfied, so the function \( \alpha \mapsto {\int }_{0}^{1}\log \left( {{\alpha }^{2} + {t}^{2}}\right) {dt} \) is well-defined and continuous for \( \alpha \in \left\lbrack {0,1}\right\rbrack \). In particular, \( I \) is defined and continuous at \( \alpha = 0 \), and since \( I\left( 0\right) = 2\log 2 > 0 \), we deduce the existence of \( {\alpha }_{0} > 0 \) such that \( I\left( \alpha \right) > 0 \) for \( 0 \leq \alpha < {\alpha }_{0} \). According to the asymptotic expansion obtained in the previous question, as \( 0 \leq \alpha < {\alpha }_{0} \), we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\log \left| {{f}_{\alpha }\left( 1\right) - {P}_{n}\left( 1\right) }\right| = + \infty \). Thus, there is no pointwise convergence (and therefore no uniform convergence) of \( \left( {P}_{n}\right) \) to \( f \) as \( 0 \leq \alpha < {\alpha }_{0} \).

Remarque. On peut obtenir la forme explicite \( I\left( \alpha \right) = 2\log 2 - \alpha \arctan \left( {1/\alpha }\right) - \log \left( {1 + {\alpha }^{2}}\right) \) . On peut montrer que \( I\left( \alpha \right) > 0 \) pour \( \alpha < {\alpha }_{0} \approx 0,{5255249} \) .

> Remark. One can obtain the explicit form \( I\left( \alpha \right) = 2\log 2 - \alpha \arctan \left( {1/\alpha }\right) - \log \left( {1 + {\alpha }^{2}}\right) \). One can show that \( I\left( \alpha \right) > 0 \) for \( \alpha < {\alpha }_{0} \approx 0,{5255249} \).

- Pour éviter de passer par les sommes de Riemann d'une intégrale généralisée dans b), on aurait pu obtenir le comportement de \( \log \left| {{\omega }_{n}\left( 1\right) }\right| \) par la formule de Stirling. Le comportement de \( \log \left| {{\omega }_{n}\left( {i\alpha }\right) }\right| \) s’obtient directement à partir d’une somme de Riemann d’une fonction définie et continue sur le segment \( \left\lbrack  {0,1}\right\rbrack \) .

> - To avoid using Riemann sums of an improper integral in b), one could have obtained the behavior of \( \log \left| {{\omega }_{n}\left( 1\right) }\right| \) using Stirling's formula. The behavior of \( \log \left| {{\omega }_{n}\left( {i\alpha }\right) }\right| \) is obtained directly from a Riemann sum of a function defined and continuous on the interval \( \left\lbrack  {0,1}\right\rbrack \).

- Ainsi, une suite de polynômes interpolants ne converge pas forcément vers une fonction \( f \) à approcher. Cependant, certaines conditions de majoration des dérivées de \( f \) permettent de garantir qu'un polynôme interpolant est une bonne approximation (voir question b) de l'exercice 7 page 83).

> - Thus, a sequence of interpolating polynomials does not necessarily converge to a function \( f \) to be approximated. However, certain conditions on the bounds of the derivatives of \( f \) allow us to guarantee that an interpolating polynomial is a good approximation (see question b) of exercise 7 on page 83).

EXERCICE 8 (POLYNÔMES D’APPROXIMATION DE BERNSTEIN). On note \( I = \left\lbrack {0,1}\right\rbrack \) et \( \mathcal{C} \) l’e.v des fonctions continues de \( I \) dans \( \mathbb{C} \) . On note, pour toute fonction \( f \in \mathcal{C} \) et \( n \in {\mathbb{N}}^{ * } \)

> EXERCISE 8 (BERNSTEIN APPROXIMATION POLYNOMIALS). Let \( I = \left\lbrack {0,1}\right\rbrack \) and \( \mathcal{C} \) be the vector space of continuous functions from \( I \) to \( \mathbb{C} \). For any function \( f \in \mathcal{C} \) and \( n \in {\mathbb{N}}^{ * } \), we denote

\[
{B}_{n}\left( f\right)  : I \rightarrow  \mathbb{C}\;x \mapsto  \mathop{\sum }\limits_{{k = 0}}^{n}f\left( \frac{k}{n}\right) {b}_{n}^{k}\left( x\right) ,\;\text{ avec }\;{b}_{n}^{k}\left( x\right)  = {C}_{n}^{k}{x}^{k}{\left( 1 - x\right) }^{n - k}.
\]

a) Calculer explicitement l’expression \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right) \) , puis en déduire que pour tout \( \eta > 0 \) et pour tout \( x \in I \) ,

> a) Explicitly calculate the expression \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right) \), then deduce that for all \( \eta > 0 \) and for all \( x \in I \),

\[
\mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  \geq  \eta }}{b}_{n}^{k}\left( x\right)  \leq  \frac{1}{n{\eta }^{2}}.
\]

b) (Théorème de Bernstein) Pour tout \( f \in \mathcal{C} \) , montrer que la suite de fonctions \( {\left( {B}_{n}\left( f\right) \right) }_{n \in \mathbb{N}} \) converge uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) . En déduire le théorème de Weierstrass (théorème 5 page 235).

> b) (Bernstein's Theorem) For any \( f \in \mathcal{C} \), show that the sequence of functions \( {\left( {B}_{n}\left( f\right) \right) }_{n \in \mathbb{N}} \) converges uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \). Deduce the Weierstrass theorem (theorem 5, page 235).

c) Donner une condition nécessaire et suffisante pour que \( f \in \mathcal{C} \) soit limite uniforme sur \( \left\lbrack {0,1}\right\rbrack \) de fonctions polynômes à coefficients entiers.

> c) Give a necessary and sufficient condition for \( f \in \mathcal{C} \) to be the uniform limit on \( \left\lbrack {0,1}\right\rbrack \) of polynomial functions with integer coefficients.

d) Si \( f \) est une fonction lipschitzienne, montrer que \( {\begin{Vmatrix}f - {B}_{n}\left( f\right) \end{Vmatrix}}_{\infty } = O\left( {n}^{-1/2}\right) \) .

> d) If \( f \) is a Lipschitz function, show that \( {\begin{Vmatrix}f - {B}_{n}\left( f\right) \end{Vmatrix}}_{\infty } = O\left( {n}^{-1/2}\right) \).

e) Considérons la fonction \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) définie par \( f\left( x\right) = \left| {x - 1/2}\right| \) . Donner un équivalent de \( {B}_{n}\left( f\right) \left( {1/2}\right) - f\left( {1/2}\right) \) lorsque \( n \rightarrow \infty \) (on pourra utiliser l’égalité \( k{C}_{n}^{k} = \; n{C}_{n - 1}^{k - 1} \) et la formule de Stirling).

> e) Consider the function \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) defined by \( f\left( x\right) = \left| {x - 1/2}\right| \). Give an equivalent for \( {B}_{n}\left( f\right) \left( {1/2}\right) - f\left( {1/2}\right) \) as \( n \rightarrow \infty \) (one may use the equality \( k{C}_{n}^{k} = \; n{C}_{n - 1}^{k - 1} \) and Stirling's formula).

Solution.

> Solution.

a) En notant par abus \( 1, x,{x}^{2} \) les fonctions \( x \mapsto 1, x \mapsto x \) et \( x \mapsto {x}^{2} \) , on a pour tout \( n \in {\mathbb{N}}^{ * } \)

> a) By denoting \( 1, x,{x}^{2} \) as the functions \( x \mapsto 1, x \mapsto x \) and \( x \mapsto {x}^{2} \) for convenience, we have for all \( n \in {\mathbb{N}}^{ * } \)

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( {\frac{{k}^{2}}{{n}^{2}} - {2x}\frac{k}{n} + {x}^{2}}\right) {b}_{n}^{k}\left( x\right)  = {B}_{n}\left( {x}^{2}\right)  - {2x}{B}_{n}\left( x\right)  + {x}^{2}{B}_{n}\left( 1\right) .
\]

(*)

> On se ramène ainsi à exprimer \( {B}_{n}\left( 1\right) ,{B}_{n}\left( x\right) \) et \( {B}_{n}\left( {x}^{2}\right) \) . Pour cela, on part de l’identité bien connue

We thus reduce the problem to expressing \( {B}_{n}\left( 1\right) ,{B}_{n}\left( x\right) \) and \( {B}_{n}\left( {x}^{2}\right) \). To do this, we start from the well-known identity

\[
\forall n \in  {\mathbb{N}}^{ * },\forall \left( {a, b}\right)  \in  {\mathbb{R}}^{2},\;F\left( {a, b}\right)  = {\left( a + \left( 1 - b\right) \right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{a}^{k}{\left( 1 - b\right) }^{n - k}.
\]

On en déduit \( {B}_{n}\left( 1\right) = F\left( {1,1}\right) = 1 \) ,

> We deduce \( {B}_{n}\left( 1\right) = F\left( {1,1}\right) = 1 \),

\[
{B}_{n}\left( x\right)  = \frac{1}{n}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}k{x}^{k}{\left( 1 - x\right) }^{n - k} = \frac{x}{n}\frac{\partial F}{\partial a}\left( {x, x}\right)  = \frac{x}{n}n{\left( x + \left( 1 - x\right) \right) }^{n - 1} = x
\]

et après un petit calcul

> and after a short calculation

\[
{B}_{n}\left( {x}^{2}\right)  = \frac{1}{{n}^{2}}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{k}^{2}{x}^{k}{\left( 1 - x\right) }^{n - k} = \frac{x}{{n}^{2}}\frac{\partial }{\partial a}\left( {a\frac{\partial F}{\partial a}}\right) \left( {x, x}\right)  = {x}^{2} + \frac{x\left( {1 - x}\right) }{n}.
\]

En remplaçant ces expressions dans (*), on obtient

> By replacing these expressions in (*), we obtain

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right)  = \frac{x\left( {1 - x}\right) }{n}.
\]

La seconde partie de la question s'obtient maintenant en écrivant

> The second part of the question is now obtained by writing

\[
\mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  \geq  \eta }}{b}_{n}^{k}\left( x\right)  \leq  \frac{1}{{\eta }^{2}}\mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right)  = \frac{1}{{\eta }^{2}}\frac{x\left( {1 - x}\right) }{n} \leq  \frac{1}{n{\eta }^{2}}.
\]

(**)

> b) Analysons la situation. On peut voir l’expression donnant \( {B}_{n}\left( f\right) \left( x\right) \) comme un barycentre des points \( f\left( {k/n}\right) \) , dont les coefficients les plus significatifs se trouvent dans la région où \( k/n \) est dans un voisinage de \( x \) d’après (**). On a donc \( {B}_{n}\left( f\right) \left( x\right) \simeq f\left( x\right) \) .

b) Let us analyze the situation. We can view the expression giving \( {B}_{n}\left( f\right) \left( x\right) \) as a barycenter of the points \( f\left( {k/n}\right) \), whose most significant coefficients are found in the region where \( k/n \) is in a neighborhood of \( x \) according to (**). We therefore have \( {B}_{n}\left( f\right) \left( x\right) \simeq f\left( x\right) \).

> Précisons. Donnons nous \( \varepsilon > 0 \) . La fonction \( f \) est continue sur le compact \( I \) . Elle est donc bornée de sorte qu’il existe \( M > 0 \) tel que \( \left| {f\left( x\right) }\right| \leq M \) sur \( I \) . Elle est aussi uniformément continue d'après le théorème de Heine donc

Let us be precise. Let \( \varepsilon > 0 \) be given. The function \( f \) is continuous on the compact set \( I \). It is therefore bounded, so there exists \( M > 0 \) such that \( \left| {f\left( x\right) }\right| \leq M \) on \( I \). It is also uniformly continuous according to the Heine-Cantor theorem, so

\[
\exists \eta  > 0,\forall \left( {x,{x}^{\prime }}\right)  \in  {I}^{2},\left| {x - {x}^{\prime }}\right|  < \eta ,\;\left| {f\left( x\right)  - f\left( {x}^{\prime }\right) }\right|  < \varepsilon .
\]

On écrit maintenant

> We now write

\[
\forall x \in  I,\forall n \in  {\mathbb{N}}^{ * },\;\left| {{B}_{n}\left( f\right) \left( x\right)  - f\left( x\right) }\right|  = \left| {{B}_{n}\left( f\right) \left( x\right)  - f\left( x\right) {B}_{n}\left( 1\right) }\right|  \leq  \mathop{\sum }\limits_{{k = 0}}^{n}\left| {f\left( \frac{k}{n}\right)  - f\left( x\right) }\right| {b}_{n}^{k}\left( x\right)
\]

\[
\leq  \varepsilon \left( {\mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  < \eta }}{b}_{n}^{k}\left( x\right) }\right)  + {2M}\left( {\mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  \geq  \eta }}{b}_{n}^{k}\left( x\right) }\right)  \leq  \varepsilon \left( {\mathop{\sum }\limits_{{k = 0}}^{n}{b}_{n}^{k}\left( x\right) }\right)  + \frac{2M}{n{\eta }^{2}} = \varepsilon  + \frac{2M}{n{\eta }^{2}}.
\]

Ainsi, si \( N \in {\mathbb{N}}^{ * } \) est choisi tel que \( {2M}/\left( {N{\eta }^{2}}\right) < \varepsilon \) , on a montré

> Thus, if \( N \in {\mathbb{N}}^{ * } \) is chosen such that \( {2M}/\left( {N{\eta }^{2}}\right) < \varepsilon \), we have shown

\[
\forall n \geq  N,\forall x \in  I,\;\left| {{B}_{n}\left( f\right) \left( x\right)  - f\left( x\right) }\right|  < {2\varepsilon }.
\]

La suite de fonctions \( \left( {{B}_{n}\left( f\right) }\right) \) converge donc uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) .

> The sequence of functions \( \left( {{B}_{n}\left( f\right) }\right) \) therefore converges uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \).

Les \( {B}_{n}\left( f\right) \) sont des fonctions polynômes, on vient donc de montrer que toute fonction continue sur \( \left\lbrack {0,1}\right\rbrack \) est limite uniforme de fonctions polynômes sur \( \left\lbrack {0,1}\right\rbrack \) . On en déduit facilement par changement de variable affine le théorème de Weierstrass (si \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) est continue, on se ramène à \( \left\lbrack {0,1}\right\rbrack \) en considérant \( \left. {g\left( x\right) = f\left\lbrack {a + \left( {b - a}\right) x}\right\rbrack }\right) \) .

> The \( {B}_{n}\left( f\right) \) are polynomial functions, so we have just shown that any continuous function on \( \left\lbrack {0,1}\right\rbrack \) is a uniform limit of polynomial functions on \( \left\lbrack {0,1}\right\rbrack \). We easily deduce the Weierstrass theorem from this by an affine change of variable (if \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) is continuous, we reduce it to \( \left\lbrack {0,1}\right\rbrack \) by considering \( \left. {g\left( x\right) = f\left\lbrack {a + \left( {b - a}\right) x}\right\rbrack }\right) \)).

c) Montrons que \( f \in \mathcal{C} \) est limite uniforme sur \( \left\lbrack {0,1}\right\rbrack \) de fonctions polynômes à coefficients entiers si et seulement si \( f\left( 0\right) \) et \( f\left( 1\right) \) sont des entiers.

> c) Let us show that \( f \in \mathcal{C} \) is the uniform limit on \( \left\lbrack {0,1}\right\rbrack \) of polynomial functions with integer coefficients if and only if \( f\left( 0\right) \) and \( f\left( 1\right) \) are integers.

La condition est nécessaire : en effet, si \( f \) est limite uniforme de fonctions polynômes \( \left( {P}_{n}\right) \) à coefficients entiers, alors \( f\left( 0\right) \) (respectivement \( f\left( 1\right) \) ) est la limite de la suite d’entiers \( \left( {{P}_{n}\left( 0\right) }\right) \) (respectivement \( \left( {{P}_{n}\left( 1\right) }\right) \) ). Une suite d’entiers convergente a pour limite un nombre entier, donc \( f\left( 0\right) \) et \( f\left( 1\right) \) sont des entiers.

> The condition is necessary: indeed, if \( f \) is the uniform limit of polynomial functions \( \left( {P}_{n}\right) \) with integer coefficients, then \( f\left( 0\right) \) (respectively \( f\left( 1\right) \)) is the limit of the sequence of integers \( \left( {{P}_{n}\left( 0\right) }\right) \) (respectively \( \left( {{P}_{n}\left( 1\right) }\right) \)). A convergent sequence of integers has an integer as its limit, therefore \( f\left( 0\right) \) and \( f\left( 1\right) \) are integers.

La condition suffisante s'obtient à partir du résultat de la question précédente. Supposons \( f\left( 0\right) \) et \( f\left( 1\right) \) entiers. On considère la suite de polynômes à coefficients entiers \( \left( {{Z}_{n}\left( f\right) }\right) \) définie par

> The sufficient condition is obtained from the result of the previous question. Suppose \( f\left( 0\right) \) and \( f\left( 1\right) \) are integers. We consider the sequence of polynomials with integer coefficients \( \left( {{Z}_{n}\left( f\right) }\right) \) defined by

\[
{Z}_{n}\left( f\right)  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \mathop{\sum }\limits_{{k = 0}}^{n}\left\lbrack  {f\left( \frac{k}{n}\right) {C}_{n}^{k}}\right\rbrack  {x}^{k}{\left( 1 - x\right) }^{n - k},
\]

où \( \left\lbrack t\right\rbrack \) désigne la partie entière de \( t \) . Pour \( x \in \left\lbrack {0,1}\right\rbrack \) , on a

> where \( \left\lbrack t\right\rbrack \) denotes the integer part of \( t \). For \( x \in \left\lbrack {0,1}\right\rbrack \), we have

\[
{B}_{n}\left( f\right) \left( x\right)  - {Z}_{n}\left( f\right) \left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\left( {f\left( \frac{k}{n}\right)  - \frac{\left\lbrack  f\left( \frac{k}{n}\right) {C}_{n}^{k}\right\rbrack  }{{C}_{n}^{k}}}\right) {b}_{n}^{k}\left( x\right)
\]

(les termes de la somme pour \( k = 0 \) et \( k = n \) sont nuls car \( f\left( 0\right) \) et \( f\left( 1\right) \) sont entiers), et comme \( 0 \leq f\left( {k/n}\right) - \left\lbrack {f\left( {k/n}\right) {C}_{n}^{k}}\right\rbrack /{C}_{n}^{k} < 1/{C}_{n}^{k} \leq 1/n \) pour \( 1 \leq k \leq n - 1 \) on en déduit

> (the terms of the sum for \( k = 0 \) and \( k = n \) are zero because \( f\left( 0\right) \) and \( f\left( 1\right) \) are integers), and since \( 0 \leq f\left( {k/n}\right) - \left\lbrack {f\left( {k/n}\right) {C}_{n}^{k}}\right\rbrack /{C}_{n}^{k} < 1/{C}_{n}^{k} \leq 1/n \) for \( 1 \leq k \leq n - 1 \), we deduce

\[
0 \leq  {B}_{n}\left( f\right) \left( x\right)  - {Z}_{n}\left( f\right) \left( x\right)  \leq  \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\frac{1}{n}{b}_{n}^{k}\left( f\right) \left( x\right)  \leq  \frac{1}{n}\mathop{\sum }\limits_{{k = 0}}^{n}{b}_{n}^{k}\left( f\right) \left( x\right)  = \frac{{B}_{n}\left( 1\right) }{n} = \frac{1}{n},
\]

et ceci pour tout \( x \in \left\lbrack {0,1}\right\rbrack \) . Comme \( \left( {{B}_{n}\left( f\right) }\right) \) converge uniformément vers \( f \) on en déduit que \( \left( {{Z}_{n}\left( f\right) }\right) \) converge uniformément vers \( f \) .

> and this for all \( x \in \left\lbrack {0,1}\right\rbrack \). As \( \left( {{B}_{n}\left( f\right) }\right) \) converges uniformly to \( f \), we deduce that \( \left( {{Z}_{n}\left( f\right) }\right) \) converges uniformly to \( f \).

d) Considérons une fonction \( \lambda \) -lipschitzienne \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) . Soit \( n \in {\mathbb{N}}^{ * } \) et \( \varepsilon = {n}^{-1/2} \) . Pour \( x \in I \) , on a

> d) Consider a \( \lambda \)-Lipschitz function \( f \) on \( \left\lbrack {0,1}\right\rbrack \). Let \( n \in {\mathbb{N}}^{ * } \) and \( \varepsilon = {n}^{-1/2} \). For \( x \in I \), we have

\[
\left| {{B}_{n}\left( f\right) \left( x\right)  - f\left( x\right) }\right|  \leq  \mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  \leq  \varepsilon }}\left| {f\left( \frac{k}{n}\right)  - f\left( x\right) }\right| {b}_{n}^{k}\left( x\right)  + \mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  > \varepsilon }}\left| {f\left( \frac{k}{n}\right)  - f\left( x\right) }\right| {b}_{n}^{k}\left( x\right)
\]

\[
\leq  \mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  \leq  \varepsilon }}{\lambda \varepsilon }{b}_{n}^{k}\left( x\right)  + \mathop{\sum }\limits_{{k,\left| {k/n - x}\right|  > \varepsilon }}\frac{\lambda }{\varepsilon }{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right)
\]

\[
\leq  {\lambda \varepsilon }\mathop{\sum }\limits_{{k = 0}}^{n}{b}_{n}^{k}\left( x\right)  + \frac{\lambda }{\varepsilon }\mathop{\sum }\limits_{{k = 0}}^{n}{\left( \frac{k}{n} - x\right) }^{2}{b}_{n}^{k}\left( x\right)  = {\lambda \varepsilon } + \frac{\lambda }{\varepsilon }\frac{x\left( {1 - x}\right) }{n} \leq  {\lambda \varepsilon } + \frac{\lambda }{n\varepsilon } = \frac{2\lambda }{\sqrt{n}}.
\]

Ceci étant vrai pour tout \( x \in I \) , on en déduit le résultat.

> Since this is true for all \( x \in I \), we deduce the result.

e) Soit \( {u}_{n} = {B}_{n}\left( f\right) \left( {1/2}\right) - f\left( {1/2}\right) = {B}_{n}\left( f\right) \left( {1/2}\right) \) . L’égalité \( {b}_{n}^{k}\left( {1/2}\right) = {C}_{n}^{k}/{2}^{n} \) donne

> e) Let \( {u}_{n} = {B}_{n}\left( f\right) \left( {1/2}\right) - f\left( {1/2}\right) = {B}_{n}\left( f\right) \left( {1/2}\right) \). The equality \( {b}_{n}^{k}\left( {1/2}\right) = {C}_{n}^{k}/{2}^{n} \) gives

\[
{u}_{n} = \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{0 \leq  k < n/2}}\left( {\frac{1}{2} - \frac{k}{n}}\right) {C}_{n}^{k} + \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{n/2 < k \leq  n}}\left( {\frac{k}{n} - \frac{1}{2}}\right) {C}_{n}^{k} = \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{0 \leq  k < n/2}}\left( {1 - \frac{2k}{n}}\right) {C}_{n}^{k}.
\]

où on a utilisé la relation de symétrie \( {C}_{n}^{n - k} = {C}_{n}^{k} \) . Grâce à la relation \( k{C}_{n}^{k} = n{C}_{n - 1}^{k - 1} \) on en déduit

> where we used the symmetry relation \( {C}_{n}^{n - k} = {C}_{n}^{k} \). Thanks to the relation \( k{C}_{n}^{k} = n{C}_{n - 1}^{k - 1} \), we deduce

\[
{2}^{n}{u}_{n} = \mathop{\sum }\limits_{{0 \leq  k < n/2}}{C}_{n}^{k} - 2\mathop{\sum }\limits_{{1 \leq  k < n/2}}{C}_{n - 1}^{k - 1}.
\]

Il reste à utiliser la relation du triangle de Pascal \( {C}_{n}^{k} = {C}_{n - 1}^{k - 1} + {C}_{n - 1}^{k} \) qui entraîne

> It remains to use the Pascal's triangle relation \( {C}_{n}^{k} = {C}_{n - 1}^{k - 1} + {C}_{n - 1}^{k} \) which implies

\[
{2}^{n}{u}_{n} = 1 + \mathop{\sum }\limits_{{1 \leq  k < n/2}}\left( {{C}_{n}^{k} - {C}_{n - 1}^{k - 1}}\right)  - \mathop{\sum }\limits_{{1 \leq  k < n/2}}{C}_{n - 1}^{k - 1} = \mathop{\sum }\limits_{{0 \leq  k < n/2}}{C}_{n - 1}^{k} - \mathop{\sum }\limits_{{1 \leq  k < n/2}}{C}_{n - 1}^{k - 1} = {C}_{n - 1}^{\left\lbrack  \left( n - 1\right) /2\right\rbrack  },
\]

où \( \left\lbrack {\left( {n - 1}\right) /2}\right\rbrack \) désigne la partie entière de \( \left( {n - 1}\right) /2 \) . La formule de Stirling permet facilement d’obtenir l’équivalent \( {C}_{n - 1}^{\left\lbrack \left( n - 1\right) /2\right\rbrack } \sim {2}^{n}/\sqrt{2\pi n} \) . Finalement on a obtenu l’équivalent

> where \( \left\lbrack {\left( {n - 1}\right) /2}\right\rbrack \) denotes the integer part of \( \left( {n - 1}\right) /2 \) . Stirling's formula easily allows obtaining the equivalent \( {C}_{n - 1}^{\left\lbrack \left( n - 1\right) /2\right\rbrack } \sim {2}^{n}/\sqrt{2\pi n} \) . Finally, we have obtained the equivalent

\[
{u}_{n} = {B}_{n}\left( f\right) \left( \frac{1}{2}\right)  - f\left( \frac{1}{2}\right)  \sim  \frac{1}{\sqrt{2\pi n}}.
\]

Ainsi, l'estimation obtenue à la question précédente est la meilleure possible dans l'hypothèse d'une fonction lipschitzienne.

> Thus, the estimate obtained in the previous question is the best possible under the assumption of a Lipschitz function.

Remarque. Le résultat de la question b) de cet exercice est une version constructive du théorème de Weierstrass, mais la convergence est lente, comme le montre le résultat de la question e). Le meilleur approximant polynomial peut s'obtenir par l'algorithme de Remez.

> Remark. The result of question b) of this exercise is a constructive version of the Weierstrass theorem, but the convergence is slow, as shown by the result of question e). The best polynomial approximant can be obtained by the Remez algorithm.

EXERCICE 9 (FONCTION DÉRIVÉE À POINTS DE DISCONTINUITÉS DENSES).

> EXERCISE 9 (DERIVATIVE FUNCTION WITH DENSE DISCONTINUITY POINTS).

a) (Généralisation du théorème 4 page 234 lorsque les fonctions \( {f}_{n} \) sont seulement supposées dérivables). Soit \( \left( {f}_{n}\right) \) une suite de fonctions dérivables de \( I = \left\lbrack {0,1}\right\rbrack \) dans un espace de Banach \( E \) . On suppose que la suite des dérivées \( \left( {f}_{n}^{\prime }\right) \) converge uniformément vers une fonction \( g \) sur \( I \) , et qu’il existe \( {x}_{0} \in I \) tel que la suite \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n \in \mathbb{N}} \) converge. Montrer que \( \left( {f}_{n}\right) \) converge uniformément sur \( I \) vers une fonction dérivable \( f \) qui vérifie \( {f}^{\prime } = g \) .

> a) (Generalization of Theorem 4 on page 234 when the functions \( {f}_{n} \) are only assumed to be differentiable). Let \( \left( {f}_{n}\right) \) be a sequence of differentiable functions from \( I = \left\lbrack {0,1}\right\rbrack \) into a Banach space \( E \) . Suppose that the sequence of derivatives \( \left( {f}_{n}^{\prime }\right) \) converges uniformly to a function \( g \) on \( I \) , and that there exists \( {x}_{0} \in I \) such that the sequence \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n \in \mathbb{N}} \) converges. Show that \( \left( {f}_{n}\right) \) converges uniformly on \( I \) to a differentiable function \( f \) which satisfies \( {f}^{\prime } = g \) .

b) Exhiber une fonction \( f : I = \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) , dérivable sur \( I \) , telle que l’ensemble des points de discontinuité de \( {f}^{\prime } \) soit dense dans \( \left\lbrack {0,1}\right\rbrack \) .

> b) Exhibit a function \( f : I = \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) , differentiable on \( I \) , such that the set of discontinuity points of \( {f}^{\prime } \) is dense in \( \left\lbrack {0,1}\right\rbrack \) .

Solution. a) Ici, on ne peut pas procéder comme dans la preuve du théorème 4 page 234 car une fonction dérivée n'est pas forcément continue (ni Riemann-intégrable).

> Solution. a) Here, we cannot proceed as in the proof of Theorem 4 on page 234 because a derivative function is not necessarily continuous (nor Riemann-integrable).

Nous montrons d’abord que \( \left( {f}_{n}\right) \) vérifie le critère de Cauchy uniforme. Soit \( \varepsilon > 0 \) . D’après les hypothèses,

> We first show that \( \left( {f}_{n}\right) \) satisfies the uniform Cauchy criterion. Let \( \varepsilon > 0 \) . According to the hypotheses,

\[
\exists N \in  \mathbb{N},\forall p, q \geq  N,\;\left( {\begin{Vmatrix}{{f}_{p}\left( {x}_{0}\right)  - {f}_{q}\left( {x}_{0}\right) }\end{Vmatrix} < \varepsilon \text{ et }\forall x \in  I,\;\begin{Vmatrix}{{f}_{p}^{\prime }\left( x\right)  - {f}_{q}^{\prime }\left( x\right) }\end{Vmatrix} < \varepsilon }\right) .
\]

Ainsi, on obtient grâce à l’inégalité des accroissements finis que pour tout \( p, q \geq N \) et pour tout \( x \in I \) ,

> Thus, we obtain thanks to the mean value inequality that for all \( p, q \geq N \) and for all \( x \in I \) ,

\[
\begin{Vmatrix}{{f}_{p}\left( x\right)  - {f}_{q}\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{\left( {{f}_{p} - {f}_{q}}\right) \left( x\right)  - \left( {{f}_{p} - {f}_{q}}\right) \left( {x}_{0}\right) }\end{Vmatrix} + \begin{Vmatrix}{\left( {{f}_{p} - {f}_{q}}\right) \left( {x}_{0}\right) }\end{Vmatrix} < \varepsilon \left| {x - {x}_{0}}\right|  + \varepsilon  \leq  {2\varepsilon }.
\]

Autrement dit, la suite de fonctions \( \left( {f}_{n}\right) \) à valeurs dans un espace de Banach vérifie le critère de Cauchy uniforme, elle converge donc uniformément vers une fonction \( f \) sur \( I \) .

> In other words, the sequence of functions \( \left( {f}_{n}\right) \) with values in a Banach space satisfies the uniform Cauchy criterion, so it converges uniformly to a function \( f \) on \( I \) .

Il nous reste à montrer que \( f \) est dérivable et que \( {f}^{\prime } = g \) . Fixons \( x \in I \) et \( \varepsilon > 0 \) . La suite \( \left( {f}_{n}^{\prime }\right) \) vérifie le critère de Cauchy uniforme donc

> It remains for us to show that \( f \) is differentiable and that \( {f}^{\prime } = g \) . Let us fix \( x \in I \) and \( \varepsilon > 0 \) . The sequence \( \left( {f}_{n}^{\prime }\right) \) satisfies the uniform Cauchy criterion, therefore

\[
\exists N \in  \mathbb{N},\forall p \in  \mathbb{N},\forall t \in  I,\;\begin{Vmatrix}{{f}_{N}^{\prime }\left( t\right)  - {f}_{N + p}^{\prime }\left( t\right) }\end{Vmatrix} \leq  \varepsilon .
\]

(*)

> En appliquant (*) à \( t = x \) et en faisant \( p \rightarrow + \infty \) , on tire \( \begin{Vmatrix}{{f}_{N}^{\prime }\left( x\right) - g\left( x\right) }\end{Vmatrix} \leq \varepsilon \) , et par définition de \( {f}_{N}^{\prime }\left( x\right) \) , on en déduit

By applying (*) to \( t = x \) and letting \( p \rightarrow + \infty \) , we obtain \( \begin{Vmatrix}{{f}_{N}^{\prime }\left( x\right) - g\left( x\right) }\end{Vmatrix} \leq \varepsilon \) , and by the definition of \( {f}_{N}^{\prime }\left( x\right) \) , we deduce

\[
\exists \alpha  > 0,\forall t \in  I,0 < \left| {t - x}\right|  < \alpha ,\;\begin{Vmatrix}{\frac{{f}_{N}\left( t\right)  - {f}_{N}\left( x\right) }{t - x} - g\left( x\right) }\end{Vmatrix} \leq  {2\varepsilon }.
\]

(**)

> Maintenant, l'inégalité des accroissements finis entraîne avec (*)

Now, the mean value inequality implies with (*)

\[
\forall p \in  \mathbb{N},\forall t \in  I,\;\begin{Vmatrix}{\left( {{f}_{N} - {f}_{N + p}}\right) \left( t\right)  - \left( {{f}_{N} - {f}_{N + p}}\right) \left( x\right) }\end{Vmatrix} \leq  \varepsilon \left| {t - x}\right| ,
\]

et on en déduit en fixant \( t \in I \) et en faisant \( p \rightarrow + \infty \) que

> and we deduce from this by fixing \( t \in I \) and letting \( p \rightarrow + \infty \) that

\[
\forall t \in  I,\;\begin{Vmatrix}{\left( {{f}_{N} - f}\right) \left( t\right)  - \left( {{f}_{N} - f}\right) \left( x\right) }\end{Vmatrix} \leq  \varepsilon \left| {t - x}\right| .
\]

(***)

> De (**) et (***), on tire, pour tout \( t \in I \) tel que \( 0 < \left| {t - x}\right| < \alpha \) ,

From (**) and (***), we derive, for any \( t \in I \) such that \( 0 < \left| {t - x}\right| < \alpha \) ,

\[
\begin{Vmatrix}{\frac{f\left( t\right)  - f\left( x\right) }{t - x} - g\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}\frac{\left( {f - {f}_{N}}\right) \left( t\right)  - \left( {f - {f}_{N}}\right) \left( x\right) }{t - x}\end{Vmatrix} + \begin{Vmatrix}{\frac{{f}_{N}\left( t\right)  - {f}_{N}\left( x\right) }{t - x} - g\left( x\right) }\end{Vmatrix} \leq  \varepsilon  + {2\varepsilon } = {3\varepsilon }.
\]

En d’autres termes, nous venons de montrer que la fonction \( f \) est dérivable au point \( x \) et que \( {f}^{\prime }\left( x\right) = g\left( x\right) \) . Ceci étant vrai pour tout \( x \in I \) , on en déduit le résultat.

> In other words, we have just shown that the function \( f \) is differentiable at the point \( x \) and that \( {f}^{\prime }\left( x\right) = g\left( x\right) \) . Since this is true for any \( x \in I \) , we deduce the result.

b) Nous allons construire une telle fonction \( f \) à partir de la fonction

> b) We will construct such a function \( f \) from the function

\[
\varphi  : \left\lbrack  {-1,1}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \left\{  \begin{array}{lll} {x}^{2}\sin \left( {1/x}\right) & \text{ si } & x \neq  0 \\  0 & \text{ si } & x = 0. \end{array}\right.
\]

Cette fonction est dérivable sur \( \left\lbrack {-1,0\left\lbrack \cup \right\rbrack 0,1}\right\rbrack \) et on a \( {\varphi }^{\prime }\left( x\right) = {2x}\sin \left( {1/x}\right) - \cos \left( {1/x}\right) \) sur cet ensemble. Or

> This function is differentiable on \( \left\lbrack {-1,0\left\lbrack \cup \right\rbrack 0,1}\right\rbrack \) and we have \( {\varphi }^{\prime }\left( x\right) = {2x}\sin \left( {1/x}\right) - \cos \left( {1/x}\right) \) on this set. However,

\[
\forall x \in  \left\lbrack  {-1,1}\right\rbrack  ,\; - {x}^{2} \leq  \varphi \left( x\right)  \leq  {x}^{2}\;\text{ donc }\;\forall x \neq  0,\; - \left| x\right|  \leq  \frac{\varphi \left( x\right)  - \varphi \left( 0\right) }{x - 0} \leq  \left| x\right| ,
\]

donc \( \varphi \) est dérivable en 0 et \( {\varphi }^{\prime }\left( 0\right) = 0 \) . Ainsi, \( \varphi \) est une fonction dérivable sur \( \left\lbrack {-1,1}\right\rbrack \) tout entier et \( {\varphi }^{\prime } \) est discontinue en0, continue ailleurs.

> therefore \( \varphi \) is differentiable at 0 and \( {\varphi }^{\prime }\left( 0\right) = 0 \) . Thus, \( \varphi \) is a differentiable function on the entire \( \left\lbrack {-1,1}\right\rbrack \) and \( {\varphi }^{\prime } \) is discontinuous at 0, continuous elsewhere.

L’ensemble \( \mathbb{Q} \cap \left\lbrack {0,1}\right\rbrack \) est dénombrable, il existe donc une bijection \( n \mapsto {r}_{n} \) de \( {\mathbb{N}}^{ * } \) dans \( \mathbb{Q} \cap \left\lbrack {0,1}\right\rbrack \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on définit la fonction

> The set \( \mathbb{Q} \cap \left\lbrack {0,1}\right\rbrack \) is countable, so there exists a bijection \( n \mapsto {r}_{n} \) from \( {\mathbb{N}}^{ * } \) to \( \mathbb{Q} \cap \left\lbrack {0,1}\right\rbrack \) . For any \( n \in {\mathbb{N}}^{ * } \) , we define the function

\[
{f}_{n} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \frac{1}{{n}^{2}}\varphi \left( {x - {r}_{n}}\right) .
\]

L’expression de \( {\varphi }^{\prime } \) montre que \( {\varphi }^{\prime } \) est bornée, donc \( \sum {f}_{n}^{\prime } \) converge normalement sur \( \left\lbrack {0,1}\right\rbrack \) . Il est clair qu’il existe \( {x}_{0} \in \left\lbrack {0,1}\right\rbrack \) tel que \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n} \) converge. D’après le résultat de la question précédente, on en déduit que la série de fonctions \( \sum {f}_{n} \) converge uniformément vers une fonction dérivable \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) qui vérifie \( {f}^{\prime } = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{f}_{n}^{\prime } \) . Nous allons montrer que \( f \) répond à la question.

> The expression for \( {\varphi }^{\prime } \) shows that \( {\varphi }^{\prime } \) is bounded, so \( \sum {f}_{n}^{\prime } \) converges normally on \( \left\lbrack {0,1}\right\rbrack \) . It is clear that there exists \( {x}_{0} \in \left\lbrack {0,1}\right\rbrack \) such that \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n} \) converges. From the result of the previous question, we deduce that the series of functions \( \sum {f}_{n} \) converges uniformly to a differentiable function \( f \) on \( \left\lbrack {0,1}\right\rbrack \) which satisfies \( {f}^{\prime } = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{f}_{n}^{\prime } \) . We will show that \( f \) answers the question.

- Pour tout \( x \in  \left\lbrack  {0,1}\right\rbrack   \smallsetminus  \mathbb{Q},{f}_{n}^{\prime } \) est continue en \( x \) donc \( {f}^{\prime } \) est continue en \( x \) (limite uniforme de fonctions continues en \( x \) ).

> - For any \( x \in  \left\lbrack  {0,1}\right\rbrack   \smallsetminus  \mathbb{Q},{f}_{n}^{\prime } \) is continuous at \( x \) therefore \( {f}^{\prime } \) is continuous at \( x \) (uniform limit of functions continuous at \( x \) ).

- Pour tout \( x \in  \left\lbrack  {0,1}\right\rbrack   \cap  \mathbb{Q} \) , il existe \( N \in  {\mathbb{N}}^{ * } \) tel que \( x = {r}_{N} \) . Pour tout \( n \neq  N \) , on a \( x \neq  {r}_{n} \) donc \( {f}_{n}^{\prime } \) est continue en \( x \) , donc \( \mathop{\sum }\limits_{{n \neq  N}}{f}_{n}^{\prime } \) est continue en \( x \) . Or \( {f}_{N}^{\prime } \) est discontinue en \( x \) , on en déduit que \( {f}^{\prime } = {f}_{N}^{\prime } + \mathop{\sum }\limits_{{n \neq  N}}{f}_{n}^{\prime } \) est discontinue en \( x \) .

> - For any \( x \in  \left\lbrack  {0,1}\right\rbrack   \cap  \mathbb{Q} \) , there exists \( N \in  {\mathbb{N}}^{ * } \) such that \( x = {r}_{N} \) . For any \( n \neq  N \) , we have \( x \neq  {r}_{n} \) so \( {f}_{n}^{\prime } \) is continuous at \( x \) , therefore \( \mathop{\sum }\limits_{{n \neq  N}}{f}_{n}^{\prime } \) is continuous at \( x \) . However \( {f}_{N}^{\prime } \) is discontinuous at \( x \) , we deduce that \( {f}^{\prime } = {f}_{N}^{\prime } + \mathop{\sum }\limits_{{n \neq  N}}{f}_{n}^{\prime } \) is discontinuous at \( x \) .

Finalement, nous avons montré que \( f \) est dérivable sur \( \left\lbrack {0,1}\right\rbrack \) , discontinue en tout point rationnel, continue en tout point irrationnel. D'où le résultat.

> Finally, we have shown that \( f \) is differentiable on \( \left\lbrack {0,1}\right\rbrack \) , discontinuous at every rational point, continuous at every irrational point. Hence the result.

Remarque. On peut montrer que l'ensemble des points de continuité d'une fonction dérivée est dense (voir l'exercice 2 page 419).

> Remark. It can be shown that the set of points of continuity of a derivative function is dense (see exercise 2 page 419).

EXERCICE 10 (THÉORÉME DE HELLY). Soit \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fonctions croissantes d’un intervalle ouvert \( I \) de \( \mathbb{R} \) dans \( \mathbb{R} \) telle que, pour tout \( x \in I \) , la suite \( {\left( {f}_{n}\left( x\right) \right) }_{n \in \mathbb{N}} \) est bornée. Démontrer qu’il existe une sous-suite \( {\left( {f}_{\varphi \left( n\right) }\right) }_{n \in \mathbb{N}} \) et une fonction croissante \( f : I \rightarrow \mathbb{R} \) , telle que cette sous-suite converge simplement vers \( f \) . Solution. L'idée est de procéder par densité, en montrant d'abord le résultat sur les rationnels (dénombrables) de \( I \) , puis d’utiliser la croissance des fonctions \( {f}_{n} \) pour étendre sur \( I \) tout entier.

> EXERCISE 10 (HELLY'S THEOREM). Let \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of increasing functions from an open interval \( I \) of \( \mathbb{R} \) to \( \mathbb{R} \) such that, for all \( x \in I \) , the sequence \( {\left( {f}_{n}\left( x\right) \right) }_{n \in \mathbb{N}} \) is bounded. Prove that there exists a subsequence \( {\left( {f}_{\varphi \left( n\right) }\right) }_{n \in \mathbb{N}} \) and an increasing function \( f : I \rightarrow \mathbb{R} \) , such that this subsequence converges pointwise to \( f \) . Solution. The idea is to proceed by density, by first showing the result on the rationals (countable) of \( I \) , then using the monotonicity of the functions \( {f}_{n} \) to extend it to the whole of \( I \) .

Notons \( {\mathbb{Q}}_{I} = I \cap \mathbb{Q} \) l’ensemble dénombrable des rationnels de \( I \) , et notons \( {x}_{0},{x}_{1},\ldots ,{x}_{n},\ldots \) les éléments de \( {\mathbb{Q}}_{I} \) . On utilise le procédé diagonal, déjà employé dans la solution de l’exercice 2 page 32. De la suite bornée \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n} \) on extrait une sous-suite convergente \( {\left( {f}_{{\varphi }_{0}\left( n\right) }\left( {x}_{0}\right) \right) }_{n} \) . De la suite bornée \( {\left( {f}_{{\varphi }_{0}\left( n\right) }\left( {x}_{1}\right) \right) }_{n} \) , on extrait une sous-suite convergente \( {\left( {f}_{{\varphi }_{0} \circ {\varphi }_{1}\left( n\right) }\left( {x}_{1}\right) \right) }_{n} \) . En procédant par récurrence, on peut ainsi construire, pour tout entier naturel \( p \) , une sous-suite convergente \( {\left( {f}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\left( {x}_{p}\right) \right) }_{n \in \mathbb{N}} \) . La fonction \( \psi : \mathbb{N} \rightarrow \mathbb{N} \) définie par \( \psi \left( n\right) = {\varphi }_{0} \circ \cdots \circ {\varphi }_{n}\left( n\right) \) est strictement croissante, et pour tout entier naturel \( p, \) la suite \( {\left( {f}_{\psi \left( n\right) }\left( {x}_{p}\right) \right) }_{n} \) converge (car \( {\left( {f}_{\psi \left( n\right) }\left( {x}_{p}\right) \right) }_{n \geq p} \) est une sous-suite de \( {\left( {f}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\left( {x}_{p}\right) \right) }_{n \in \mathbb{N}} \) qui converge).

> Let \( {\mathbb{Q}}_{I} = I \cap \mathbb{Q} \) be the countable set of rationals in \( I \), and let \( {x}_{0},{x}_{1},\ldots ,{x}_{n},\ldots \) denote the elements of \( {\mathbb{Q}}_{I} \). We use the diagonal process, already employed in the solution to exercise 2 on page 32. From the bounded sequence \( {\left( {f}_{n}\left( {x}_{0}\right) \right) }_{n} \), we extract a convergent subsequence \( {\left( {f}_{{\varphi }_{0}\left( n\right) }\left( {x}_{0}\right) \right) }_{n} \). From the bounded sequence \( {\left( {f}_{{\varphi }_{0}\left( n\right) }\left( {x}_{1}\right) \right) }_{n} \), we extract a convergent subsequence \( {\left( {f}_{{\varphi }_{0} \circ {\varphi }_{1}\left( n\right) }\left( {x}_{1}\right) \right) }_{n} \). Proceeding by induction, we can thus construct, for every natural number \( p \), a convergent subsequence \( {\left( {f}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\left( {x}_{p}\right) \right) }_{n \in \mathbb{N}} \). The function \( \psi : \mathbb{N} \rightarrow \mathbb{N} \) defined by \( \psi \left( n\right) = {\varphi }_{0} \circ \cdots \circ {\varphi }_{n}\left( n\right) \) is strictly increasing, and for every natural number \( p, \), the sequence \( {\left( {f}_{\psi \left( n\right) }\left( {x}_{p}\right) \right) }_{n} \) converges (since \( {\left( {f}_{\psi \left( n\right) }\left( {x}_{p}\right) \right) }_{n \geq p} \) is a subsequence of \( {\left( {f}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\left( {x}_{p}\right) \right) }_{n \in \mathbb{N}} \) which converges).

Construisons maintenant la fonction \( g \) définie sur \( {\mathbb{Q}}_{I} \) par \( g\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{\psi \left( n\right) }\left( x\right) \) pour tout \( x \in {\mathbb{Q}}_{I} \) . Pour \( x < y \) , on a \( {f}_{\psi \left( n\right) }\left( x\right) \leq {f}_{\psi \left( n\right) }\left( y\right) \) , et en passant à la limite on voit que \( g \) est croissante sur \( {\mathbb{Q}}_{I} \) . On étend \( g \) sur \( I \) tout entier de la manière suivante : pour \( x \in I \smallsetminus {\mathbb{Q}}_{I} \) , on définit

> Let us now construct the function \( g \) defined on \( {\mathbb{Q}}_{I} \) by \( g\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{\psi \left( n\right) }\left( x\right) \) for all \( x \in {\mathbb{Q}}_{I} \). For \( x < y \), we have \( {f}_{\psi \left( n\right) }\left( x\right) \leq {f}_{\psi \left( n\right) }\left( y\right) \), and by passing to the limit we see that \( g \) is increasing on \( {\mathbb{Q}}_{I} \). We extend \( g \) to the whole of \( I \) in the following way: for \( x \in I \smallsetminus {\mathbb{Q}}_{I} \), we define

\[
g\left( x\right)  = \sup {G}_{x},\;\text{ avec }\;{G}_{x} = \left\{  {g\left( y\right)  \mid  y \in  {\mathbb{Q}}_{I}, y < x}\right\}
\]

( \( {G}_{x} \) est non vide car \( I \) est ouvert, et majoré car \( g \) étant croissante, tous les éléments de \( {G}_{x} \) sont inférieurs à \( g\left( z\right) \) pour un \( z > x \) fixé dans \( {\mathbb{Q}}_{I} \) ). Ainsi définie, \( g \) est croissante sur \( I \) , comme on le vérifie facilement en montrant, \( g\left( x\right) \leq g\left( y\right) \) lorsque \( x < y \) , d’abord pour \( x \in I \smallsetminus {\mathbb{Q}}_{I} \) et \( y \in {\mathbb{Q}}_{I} \) , puis pour \( x \in {\mathbb{Q}}_{I} \) et \( y \in I \smallsetminus {\mathbb{Q}}_{I} \) , puis pour \( x \) et \( y \) dans \( I \smallsetminus {\mathbb{Q}}_{I} \) .

> ( \( {G}_{x} \) is non-empty because \( I \) is open, and bounded above because \( g \) being increasing, all elements of \( {G}_{x} \) are less than \( g\left( z\right) \) for a fixed \( z > x \) in \( {\mathbb{Q}}_{I} \) ). Thus defined, \( g \) is increasing on \( I \) , as is easily verified by showing \( g\left( x\right) \leq g\left( y\right) \) when \( x < y \) , first for \( x \in I \smallsetminus {\mathbb{Q}}_{I} \) and \( y \in {\mathbb{Q}}_{I} \) , then for \( x \in {\mathbb{Q}}_{I} \) and \( y \in I \smallsetminus {\mathbb{Q}}_{I} \) , then for \( x \) and \( y \) in \( I \smallsetminus {\mathbb{Q}}_{I} \) .

Montrons que pour \( x \) dans l’ensemble \( C \subset I \) des points de continuité de \( g \) , la suite \( \left( {{f}_{\psi \left( n\right) }\left( x\right) }\right) \) converge vers \( g\left( x\right) \) . Étant donné \( \varepsilon > 0 \) , comme \( g \) est continue en \( x \) , il existe \( a \) et \( b \) dans \( {\mathbb{Q}}_{I} \) tels que \( a < x < b \) et

> Let us show that for \( x \) in the set \( C \subset I \) of continuity points of \( g \) , the sequence \( \left( {{f}_{\psi \left( n\right) }\left( x\right) }\right) \) converges to \( g\left( x\right) \) . Given \( \varepsilon > 0 \) , since \( g \) is continuous at \( x \) , there exist \( a \) and \( b \) in \( {\mathbb{Q}}_{I} \) such that \( a < x < b \) and

\[
\left| {g\left( x\right)  - g\left( a\right) }\right|  < \varepsilon ,\left| {g\left( x\right)  - g\left( b\right) }\right|  < \varepsilon \;\text{ donc }\;g\left( b\right)  - \varepsilon  < g\left( x\right)  < g\left( a\right)  + \varepsilon .
\]

Les suites \( {\left( {f}_{\psi \left( n\right) }\left( a\right) \right) }_{n} \) et \( {\left( {f}_{\psi \left( n\right) }\left( b\right) \right) }_{n} \) convergent vers \( g\left( a\right) \) et \( g\left( b\right) \) respectivement, donc il exis \( N > 0 \) tel que pour tout \( n \geq N,\left| {{f}_{\psi \left( n\right) }\left( a\right) - g\left( a\right) }\right| < \varepsilon \) et \( \left| {{f}_{\psi \left( n\right) }\left( b\right) - g\left( b\right) }\right| < \varepsilon \) , donc

> The sequences \( {\left( {f}_{\psi \left( n\right) }\left( a\right) \right) }_{n} \) and \( {\left( {f}_{\psi \left( n\right) }\left( b\right) \right) }_{n} \) converge to \( g\left( a\right) \) and \( g\left( b\right) \) respectively, so there exists \( N > 0 \) such that for all \( n \geq N,\left| {{f}_{\psi \left( n\right) }\left( a\right) - g\left( a\right) }\right| < \varepsilon \) and \( \left| {{f}_{\psi \left( n\right) }\left( b\right) - g\left( b\right) }\right| < \varepsilon \) , therefore

\[
{f}_{\psi \left( n\right) }\left( b\right)  - {2\varepsilon } < g\left( b\right)  - \varepsilon  < g\left( x\right)  < g\left( a\right)  + \varepsilon  < {f}_{\psi \left( n\right) }\left( a\right)  + {2\varepsilon }
\]

Comme \( {f}_{\psi \left( n\right) } \) est croissante, on en déduit \( {f}_{\psi \left( n\right) }\left( x\right) - {2\varepsilon } < g\left( x\right) < {f}_{\psi \left( n\right) }\left( x\right) + {2\varepsilon } \) . Ceci est vrai pour tout \( n \geq N \) , donc la suite \( \left( {{f}_{\psi \left( n\right) }\left( x\right) }\right) \) converge bien vers \( g\left( x\right) \) , et ceci pour tout \( x \in C \) .

> Since \( {f}_{\psi \left( n\right) } \) is increasing, we deduce \( {f}_{\psi \left( n\right) }\left( x\right) - {2\varepsilon } < g\left( x\right) < {f}_{\psi \left( n\right) }\left( x\right) + {2\varepsilon } \) . This is true for all \( n \geq N \) , so the sequence \( \left( {{f}_{\psi \left( n\right) }\left( x\right) }\right) \) indeed converges to \( g\left( x\right) \) , and this for all \( x \in C \) .

Il reste le cas des points de discontinuité \( D = I \smallsetminus C \) de \( g \) . La fonction \( g \) est croissante donc \( D \) est au plus dénombrable (car une fonction monotone est réglée et l'ensemble des discontinuités d'une fonction réglée est au plus dénombrable, voir le théorème 4 page 99. On peut aussi obtenir ce résultat directement, en associant à chaque discontinuité \( x \) de \( g \) un nombre rationnel différent en le choisissant dans \( \rbrack g\left( {x - }\right) , g\left( {x + }\right) \left\lbrack \right\rbrack \) ). En procédant de la même manière que plus haut, on en déduit qu’il existe une sous-suite \( \left( {f}_{\psi \circ \theta \left( n\right) }\right) \) de \( \left( {f}_{\psi \left( n\right) }\right) \) telle que \( {\left( {f}_{\psi \circ \theta \left( n\right) }\left( x\right) \right) }_{n} \) converge pour tout \( x \in D \) (attention, cette limite n’est pas forcément égale à \( g\left( x\right) \) ).

> The case of the points of discontinuity \( D = I \smallsetminus C \) of \( g \) remains. The function \( g \) is increasing, so \( D \) is at most countable (since a monotonic function is regulated and the set of discontinuities of a regulated function is at most countable; see theorem 4 on page 99. One can also obtain this result directly by associating each discontinuity \( x \) of \( g \) with a distinct rational number chosen from \( \rbrack g\left( {x - }\right) , g\left( {x + }\right) \left\lbrack \right\rbrack \)). By proceeding in the same manner as above, we deduce that there exists a subsequence \( \left( {f}_{\psi \circ \theta \left( n\right) }\right) \) of \( \left( {f}_{\psi \left( n\right) }\right) \) such that \( {\left( {f}_{\psi \circ \theta \left( n\right) }\left( x\right) \right) }_{n} \) converges for all \( x \in D \) (note that this limit is not necessarily equal to \( g\left( x\right) \)).

Ainsi, pour tout \( x \in I \) , la suite \( {\left( {f}_{\psi \circ \theta \left( n\right) }\left( x\right) \right) }_{n} \) converge. La fonction \( f : I \rightarrow \mathbb{R} \) définie par \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{\psi \circ \theta \left( n\right) }\left( x\right) \) est croissante, et ceci clos la démonstration.

> Thus, for all \( x \in I \) , the sequence \( {\left( {f}_{\psi \circ \theta \left( n\right) }\left( x\right) \right) }_{n} \) converges. The function \( f : I \rightarrow \mathbb{R} \) defined by \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{\psi \circ \theta \left( n\right) }\left( x\right) \) is increasing, and this concludes the proof.

EXERCICE 11. Soit \( p \in {\mathbb{N}}^{ * } \) et \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fonctions réelles de classe \( {\mathcal{C}}^{p} \) sur un segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) . On suppose que la suite de fonctions \( {\left( {f}_{n}^{\left( p\right) }\right) }_{n \in \mathbb{N}} \) converge uniformément vers une fonction \( g \) sur \( \left\lbrack {a, b}\right\rbrack \) , et qu’il existe \( p \) points distincts \( {x}_{1},\ldots ,{x}_{p} \) de \( \left\lbrack {a, b}\right\rbrack \) tels que pour tout \( i\left( {1 \leq i \leq p}\right) \) , la suite \( {\left( {f}_{n}\left( {x}_{i}\right) \right) }_{n \in \mathbb{N}} \) converge. Montrer que \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) converge uniformément sur \( \left\lbrack {a, b}\right\rbrack \) vers une fonction \( f \) de classe \( {\mathcal{C}}^{p} \) telle que \( {f}^{\left( p\right) } = g \) .

> EXERCISE 11. Let \( p \in {\mathbb{N}}^{ * } \) and \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of real-valued functions of class \( {\mathcal{C}}^{p} \) on an interval \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) . Suppose that the sequence of functions \( {\left( {f}_{n}^{\left( p\right) }\right) }_{n \in \mathbb{N}} \) converges uniformly to a function \( g \) on \( \left\lbrack {a, b}\right\rbrack \) , and that there exist \( p \) distinct points \( {x}_{1},\ldots ,{x}_{p} \) in \( \left\lbrack {a, b}\right\rbrack \) such that for all \( i\left( {1 \leq i \leq p}\right) \) , the sequence \( {\left( {f}_{n}\left( {x}_{i}\right) \right) }_{n \in \mathbb{N}} \) converges. Show that \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) converges uniformly on \( \left\lbrack {a, b}\right\rbrack \) to a function \( f \) of class \( {\mathcal{C}}^{p} \) such that \( {f}^{\left( p\right) } = g \) .

Solution. C'est une généralisation du théorème de dérivation de la limite d'une suite de fonctions. Notre point de départ est la formule de Taylor avec reste intégral qui donne

> Solution. This is a generalization of the theorem on the differentiation of the limit of a sequence of functions. Our starting point is Taylor's formula with integral remainder, which gives

\[
\forall n \in  \mathbb{N},\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;{f}_{n}\left( x\right)  = {P}_{n}\left( x\right)  + {I}_{n}\left( x\right)
\]

avec

> with

\[
{P}_{n}\left( x\right)  = {f}_{n}\left( a\right)  + \left( {x - a}\right) {f}_{n}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( x - a\right) }^{p - 1}}{\left( {p - 1}\right) !}{f}_{n}^{\left( p - 1\right) }\left( a\right) \;\text{ et }\;{I}_{n}\left( x\right)  = {\int }_{a}^{x}\frac{{\left( x - t\right) }^{p - 1}}{\left( {p - 1}\right) !}{f}_{n}^{\left( p\right) }\left( t\right) {dt}.
\]

Le polynôme \( {P}_{n} \) est de degré \( \leq p - 1 \) , donc il est égal à au polynôme d’interpolation de Lagrange égal à \( {P}_{n}\left( {x}_{i}\right) \) sur les points \( {\left( {x}_{i}\right) }_{1 \leq i \leq p} \) , ce qui s’écrit

> The polynomial \( {P}_{n} \) is of degree \( \leq p - 1 \) , so it is equal to the Lagrange interpolation polynomial equal to \( {P}_{n}\left( {x}_{i}\right) \) at the points \( {\left( {x}_{i}\right) }_{1 \leq i \leq p} \) , which is written as

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;{P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{p}{P}_{n}\left( {x}_{i}\right) {f}_{i}\left( x\right) ,\;\text{ avec }\;{f}_{i}\left( x\right)  = \frac{\mathop{\prod }\limits_{{j \neq  i}}\left( {x - {x}_{j}}\right) }{\mathop{\prod }\limits_{{j \neq  i}}\left( {{x}_{i} - {x}_{j}}\right) }.
\]

Si \( h \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) , notons \( \parallel h{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\left| {h\left( x\right) }\right| \) la norme de la convergence uni-forme. La fonction \( g \) est continue, car c’est la limite uniforme d’une suite de fonctions continues. Considérons la fonction \( I\left( x\right) = {\int }_{a}^{x}\frac{{\left( x - t\right) }^{p - 1}}{\left( {p - 1}\right) !}g\left( t\right) {dt} \) . On a \( {\begin{Vmatrix}I - {I}_{n}\end{Vmatrix}}_{\infty } \leq \frac{{\left( b - a\right) }^{p}}{p!}{\begin{Vmatrix}{f}_{n}^{\left( p\right) } - g\end{Vmatrix}}_{\infty } \) donc \( \left( {I}_{n}\right) \) converge uniformément vers \( I \) . Pour tout \( i \) , on a \( {P}_{n}\left( {x}_{i}\right) = {f}_{n}\left( {x}_{i}\right) - {I}_{n}\left( {x}_{i}\right) \) donc la suite \( {\left( {P}_{n}\left( {x}_{i}\right) \right) }_{n} \) converge. Notons \( {y}_{i} \) sa limite, et notons \( P\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{p}{y}_{i}{f}_{i}\left( x\right) \) le polynôme d’interpolation de Lagrange égal à \( {y}_{i} \) en \( {x}_{i} \) . Posons \( f\left( x\right) = P\left( x\right) + I\left( x\right) \) . La formule

> If \( h \) is continuous on \( \left\lbrack {a, b}\right\rbrack \), let \( \parallel h{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\left| {h\left( x\right) }\right| \) denote the uniform convergence norm. The function \( g \) is continuous, as it is the uniform limit of a sequence of continuous functions. Consider the function \( I\left( x\right) = {\int }_{a}^{x}\frac{{\left( x - t\right) }^{p - 1}}{\left( {p - 1}\right) !}g\left( t\right) {dt} \). We have \( {\begin{Vmatrix}I - {I}_{n}\end{Vmatrix}}_{\infty } \leq \frac{{\left( b - a\right) }^{p}}{p!}{\begin{Vmatrix}{f}_{n}^{\left( p\right) } - g\end{Vmatrix}}_{\infty } \) so \( \left( {I}_{n}\right) \) converges uniformly to \( I \). For all \( i \), we have \( {P}_{n}\left( {x}_{i}\right) = {f}_{n}\left( {x}_{i}\right) - {I}_{n}\left( {x}_{i}\right) \) so the sequence \( {\left( {P}_{n}\left( {x}_{i}\right) \right) }_{n} \) converges. Let \( {y}_{i} \) denote its limit, and let \( P\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{p}{y}_{i}{f}_{i}\left( x\right) \) be the Lagrange interpolation polynomial equal to \( {y}_{i} \) at \( {x}_{i} \). Let \( f\left( x\right) = P\left( x\right) + I\left( x\right) \). The formula

\[
{\begin{Vmatrix}f - {f}_{n}\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}P - {P}_{n}\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}I - {I}_{n}\end{Vmatrix}}_{\infty } \leq  \mathop{\sum }\limits_{{i = 1}}^{p}\left| {{y}_{i} - {P}_{n}\left( {x}_{i}\right) }\right|  \cdot  {\begin{Vmatrix}{f}_{i}\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}I - {I}_{n}\end{Vmatrix}}_{\infty }
\]

montre que \( {\begin{Vmatrix}f - {f}_{n}\end{Vmatrix}}_{\infty } \) converge vers0, donc \( \left( {f}_{n}\right) \) converge uniformément vers \( f \) . Une récurrence facile montre que pour \( 1 \leq k \leq p - 1, f \) est de classe \( {\mathcal{C}}^{k} \) et vérifie

> shows that \( {\begin{Vmatrix}f - {f}_{n}\end{Vmatrix}}_{\infty } \) converges to 0, so \( \left( {f}_{n}\right) \) converges uniformly to \( f \). An easy induction shows that for \( 1 \leq k \leq p - 1, f \) is of class \( {\mathcal{C}}^{k} \) and satisfies

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;{f}^{\left( k\right) }\left( x\right)  = {P}^{\left( k\right) }\left( x\right)  + {\int }_{0}^{x}\frac{{\left( x - t\right) }^{p - k - 1}}{\left( {p - k - 1}\right) !}g\left( t\right) {dt}
\]

En particulier, \( f \) est de classe \( {\mathcal{C}}^{p - 1} \) et vérifie \( {f}^{\left( p - 1\right) }\left( x\right) = {P}^{\left( p - 1\right) }\left( x\right) + {\int }_{0}^{x}g\left( t\right) {dt} \) , donc \( f \) est de classe \( {\mathcal{C}}^{p} \) et \( {f}^{\left( p\right) } = g\left( {\operatorname{car}\deg \left( P\right) \leq p - 1}\right) \) , d’où le résultat.

> In particular, \( f \) is of class \( {\mathcal{C}}^{p - 1} \) and satisfies \( {f}^{\left( p - 1\right) }\left( x\right) = {P}^{\left( p - 1\right) }\left( x\right) + {\int }_{0}^{x}g\left( t\right) {dt} \), so \( f \) is of class \( {\mathcal{C}}^{p} \) and \( {f}^{\left( p\right) } = g\left( {\operatorname{car}\deg \left( P\right) \leq p - 1}\right) \), hence the result.
