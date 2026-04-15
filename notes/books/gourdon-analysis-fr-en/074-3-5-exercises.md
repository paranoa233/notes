#### 3.5. Exercises

*Français : 3.5. Exercices*

EXERCICE 1. Étudier la nature des intégrales suivantes :

> EXERCISE 1. Study the nature of the following integrals:

\[
\text{ a) }{\int }_{0}^{1}\frac{\operatorname{ch}t - \cos t}{{t}^{5/2}}{dt}\;\text{ b) }\;{\int }_{2/\pi }^{+\infty }\log \left( {\cos \frac{1}{t}}\right) {dt}\;\text{ c) }\;{\int }_{0}^{+\infty }\frac{\sqrt{t}\sin \left( {1/{t}^{2}}\right) }{\log \left( {1 + t}\right) }{dt}
\]

\[
\text{ d) }{\int }_{0}^{+\infty }\frac{\sin t}{{t}^{\alpha }}{dt},\;\alpha  \in  \mathbb{R}\;\text{ e) }{\int }_{0}^{+\infty }\frac{\log \left( {1 + {t}^{\alpha }}\right) }{{t}^{\beta }}{dt},\;\left( {\alpha ,\beta }\right)  \in  {\mathbb{R}}^{2}\text{ . }
\]

Solution. a) La fonction \( f : t \mapsto \left( {\operatorname{ch}t - \cos t}\right) {t}^{-5/2} \) est continue sur \( \rbrack 0,1\rbrack \) . Le problème se situe donc en 0 . Au voisinage de 0, on a

> Solution. a) The function \( f : t \mapsto \left( {\operatorname{ch}t - \cos t}\right) {t}^{-5/2} \) is continuous on \( \rbrack 0,1\rbrack \) . The problem therefore lies at 0. In the neighborhood of 0, we have

\[
\operatorname{ch}t - \cos t = \left( {1 + \frac{{t}^{2}}{2} + o\left( {t}^{2}\right) }\right)  - \left( {1 - \frac{{t}^{2}}{2} + o\left( {t}^{2}\right) }\right)  = {t}^{2} + o\left( {t}^{2}\right)  \sim  {t}^{2},
\]

donc \( f\left( t\right) \sim {t}^{-1/2} \) lorsque \( t \rightarrow {0}^{ + } \) . On en déduit (grâce à la proposition 5) que l’intégrale \( {\int }_{0}^{1}f\left( t\right) {dt} \) est absolument convergente.

> so \( f\left( t\right) \sim {t}^{-1/2} \) when \( t \rightarrow {0}^{ + } \) . We deduce (thanks to proposition 5) that the integral \( {\int }_{0}^{1}f\left( t\right) {dt} \) is absolutely convergent.

b) Ici, la fonction \( f : t \mapsto \log \left( {\cos \left( {1/t}\right) }\right) \) est continue sur \( \rbrack 2/\pi , + \infty \lbrack \) . Étudions le comportement de cette fonction aux deux bornes de cet intervalle. Lorsque \( t \rightarrow {0}^{ + } \) ,

> b) Here, the function \( f : t \mapsto \log \left( {\cos \left( {1/t}\right) }\right) \) is continuous on \( \rbrack 2/\pi , + \infty \lbrack \) . Let us study the behavior of this function at the two bounds of this interval. When \( t \rightarrow {0}^{ + } \) ,

\[
f\left( {\frac{2}{\pi } + t}\right)  = \log \left( {\cos \left( {\frac{\pi }{2} \cdot  \frac{1}{1 + {t\pi }/2}}\right) }\right)  = \log \left( {\cos \left( {\frac{\pi }{2} - t\frac{{\pi }^{2}}{4} + o\left( t\right) }\right) }\right)
\]

\[
= \log \left( {\sin \left( {\frac{t{\pi }^{2}}{4} + o\left( t\right) }\right) }\right)  = \log \left( {\frac{t{\pi }^{2}}{4} + o\left( t\right) }\right)  = \log t + \log \left( {\frac{{\pi }^{2}}{4} + o\left( 1\right) }\right)  \sim  \log t,
\]

donc \( {\int }_{2/\pi }^{1}f\left( t\right) {dt} \) converge absolument. Lorsque \( t \rightarrow + \infty \) ,

> so \( {\int }_{2/\pi }^{1}f\left( t\right) {dt} \) converges absolutely. When \( t \rightarrow + \infty \) ,

\[
f\left( t\right)  = \log \left( {1 - \frac{1}{2{t}^{2}} + o\left( \frac{1}{{t}^{2}}\right) }\right)  =  - \frac{1}{2{t}^{2}} + o\left( \frac{1}{{t}^{2}}\right)  \sim   - \frac{1}{2{t}^{2}},
\]

ce qui montre que l’intégrale \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converge absolument.

> which shows that the integral \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converges absolutely.

L'intégrale proposée est donc absolument convergente.

> The proposed integral is therefore absolutely convergent.

c) La fonction \( f : t \mapsto \frac{\sqrt{t}\sin \left( {1/{t}^{2}}\right) }{\log \left( {1 + t}\right) } \) est continue sur \( \rbrack 0, + \infty \left\lbrack \right. \) . En \( {0}^{ + } \) , on a

> c) The function \( f : t \mapsto \frac{\sqrt{t}\sin \left( {1/{t}^{2}}\right) }{\log \left( {1 + t}\right) } \) is continuous on \( \rbrack 0, + \infty \left\lbrack \right. \) . At \( {0}^{ + } \) , we have

\[
\left| {f\left( t\right) }\right|  \leq  \frac{\sqrt{t}}{\log \left( {1 + t}\right) } \sim  \frac{1}{\sqrt{t}}\;\text{ donc }\;f\left( t\right)  = O\left( \frac{1}{\sqrt{t}}\right) ,
\]

ce qui montre que \( {\int }_{0}^{1}f\left( t\right) {dt} \) est absolument convergente. En \( + \infty \) , on a

> which shows that \( {\int }_{0}^{1}f\left( t\right) {dt} \) is absolutely convergent. At \( + \infty \) , we have

\[
f\left( t\right)  \sim  \frac{\sqrt{t}}{\log t}\frac{1}{{t}^{2}} = \frac{1}{{t}^{3/2}\log t} = O\left( \frac{1}{{t}^{3/2}}\right) ,
\]

donc \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) est absolument convergente. On en déduit que l’intégrale proposée est absolu-ment convergente.

> therefore \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) is absolutely convergent. We deduce that the proposed integral is absolutely convergent.

d) La fonction \( {f}_{\alpha } : t \mapsto {t}^{-\alpha }\sin t \) est continue sur \( \rbrack 0, + \infty \left\lbrack \right. \) . On sait que l’intégrale \( {\int }_{1}^{+\infty }{f}_{\alpha }\left( t\right) {dt} \) converge si et seulement si \( \alpha > 0 \) (voir la remarque 6). Par ailleurs, lorsque \( t \rightarrow {0}^{ + } \) on a \( {f}_{\alpha }\left( t\right) \sim 1/{t}^{\alpha - 1} \) , donc \( {\int }_{0}^{1}{f}_{\alpha }\left( t\right) {dt} \) converge si et seulement si \( \alpha < 2 \) . Finalement, l’intégrale proposée converge si et seulement si \( 0 < \alpha < 2 \) (elle est semi-convergente pour \( 0 < \alpha \leq 1 \) et absolument convergente pour \( 1 < \alpha < 2 \) ).

> d) The function \( {f}_{\alpha } : t \mapsto {t}^{-\alpha }\sin t \) is continuous on \( \rbrack 0, + \infty \left\lbrack \right. \) . We know that the integral \( {\int }_{1}^{+\infty }{f}_{\alpha }\left( t\right) {dt} \) converges if and only if \( \alpha > 0 \) (see remark 6). Furthermore, when \( t \rightarrow {0}^{ + } \) we have \( {f}_{\alpha }\left( t\right) \sim 1/{t}^{\alpha - 1} \) , so \( {\int }_{0}^{1}{f}_{\alpha }\left( t\right) {dt} \) converges if and only if \( \alpha < 2 \) . Finally, the proposed integral converges if and only if \( 0 < \alpha < 2 \) (it is semi-convergent for \( 0 < \alpha \leq 1 \) and absolutely convergent for \( 1 < \alpha < 2 \) ).

e) L’application \( {f}_{\alpha ,\beta } : \;x \mapsto {t}^{-\beta }\log \left( {1 + {t}^{\alpha }}\right) \) est continue sur \( \rbrack 0, + \infty \left\lbrack \right. \) . En \( {0}^{ + } \) , trois cas se produisent :

> e) The mapping \( {f}_{\alpha ,\beta } : \;x \mapsto {t}^{-\beta }\log \left( {1 + {t}^{\alpha }}\right) \) is continuous on \( \rbrack 0, + \infty \left\lbrack \right. \) . At \( {0}^{ + } \) , three cases occur:

- Si \( \alpha  > 0 \) , on a \( {f}_{\alpha ,\beta }\left( t\right)  \sim  {t}^{\alpha  - \beta } \) donc \( {\int }_{0}^{1}{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( \beta  - \alpha  < 1 \) .

> - If \( \alpha  > 0 \) , we have \( {f}_{\alpha ,\beta }\left( t\right)  \sim  {t}^{\alpha  - \beta } \) so \( {\int }_{0}^{1}{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( \beta  - \alpha  < 1 \) .

- Si \( \alpha  = 0 \) , on a \( {f}_{\alpha ,\beta }\left( t\right)  = \left( {\log 2}\right) {t}^{-\beta } \) donc l’intégrale converge si et seulement si \( \beta  < 1 \) .

> - If \( \alpha  = 0 \) , we have \( {f}_{\alpha ,\beta }\left( t\right)  = \left( {\log 2}\right) {t}^{-\beta } \) so the integral converges if and only if \( \beta  < 1 \) .

- Si \( \alpha  < 0 \) , on a \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \alpha \left( {\log t}\right) {t}^{-\beta } \) donc \( {\int }_{0}^{1}{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( \beta  < 1 \) (voir les intégrales de Bertrand, proposition 6).

> - If \( \alpha  < 0 \) , we have \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \alpha \left( {\log t}\right) {t}^{-\beta } \) so \( {\int }_{0}^{1}{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( \beta  < 1 \) (see Bertrand integrals, proposition 6).

En \( + \infty \) , on traite également trois cas :

> At \( + \infty \) , we also treat three cases:

- Si \( \alpha  > 0 \) , alors \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \alpha \left( {\log t}\right) {t}^{-\beta } \) donc \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( \beta  > 1 \) .

> - If \( \alpha  > 0 \) , then \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \alpha \left( {\log t}\right) {t}^{-\beta } \) so \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( \beta  > 1 \) .

- Si \( \alpha  = 0 \) , alors \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \left( {\log 2}\right) {t}^{-\beta } \) donc \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( \beta  > 1 \) .

> - If \( \alpha  = 0 \) , then \( {f}_{\alpha ,\beta }\left( t\right)  \sim  \left( {\log 2}\right) {t}^{-\beta } \) therefore \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( \beta  > 1 \) .

- Si \( \alpha  < 0 \) , alors \( {f}_{\alpha ,\beta }\left( t\right)  \sim  {t}^{\alpha  - \beta } \) donc \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( \beta  - \alpha  > 1 \) . De tout ceci, on déduit que \( {\int }_{0}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converge si et seulement si \( 1 + \alpha  < \beta  < 1 \) ou \( 1 < \beta  < \alpha  + 1 \) .

> - If \( \alpha  < 0 \) , then \( {f}_{\alpha ,\beta }\left( t\right)  \sim  {t}^{\alpha  - \beta } \) therefore \( {\int }_{1}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( \beta  - \alpha  > 1 \) . From all this, we deduce that \( {\int }_{0}^{+\infty }{f}_{\alpha ,\beta }\left( t\right) {dt} \) converges if and only if \( 1 + \alpha  < \beta  < 1 \) or \( 1 < \beta  < \alpha  + 1 \) .

EXERCICE 2. Soit \( f : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une fonction continue telle que l’intégrale \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converge. Montrer que pour tout nombre réel \( a > 0 \) , l’intégrale

> EXERCISE 2. Let \( f : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a continuous function such that the integral \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converges. Show that for any real number \( a > 0 \) , the integral

\[
{\int }_{1}^{+\infty }\frac{f\left( t\right) }{{t}^{a}}{dt}
\]

converge.

> converges.

Solution. Il s'agit en fait d'un cas particulier de la règle d'Abel (théorème 5). Nous allons ce-pendant prouver le résultat directement sans faire appel à cette dernière (la preuve est d'ailleurs tout-à-fait représentative de celle de la règle d’Abel dans le cas où \( f \) est continue et \( g \) est \( {\mathcal{C}}^{1} \) ).

> Solution. This is actually a special case of Abel's rule (theorem 5). We will, however, prove the result directly without invoking the latter (the proof is, moreover, quite representative of that of Abel's rule in the case where \( f \) is continuous and \( g \) is \( {\mathcal{C}}^{1} \) ).

On considère l’application \( F : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}\;x \mapsto {\int }_{1}^{x}f\left( t\right) {dt}}\right. }\right. \) . Par hypothèse, cette application converge lorsque \( x \rightarrow + \infty \) , elle est donc bornée. En intégrant par parties, on a pour tout \( a > 0 \)

> Consider the mapping \( F : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}\;x \mapsto {\int }_{1}^{x}f\left( t\right) {dt}}\right. }\right. \) . By hypothesis, this mapping converges as \( x \rightarrow + \infty \) , so it is bounded. By integrating by parts, we have for all \( a > 0 \)

\[
\forall X > 1,\;{\int }_{1}^{X}\frac{f\left( t\right) }{{t}^{a}}{dt} = {\left\lbrack  \frac{F\left( t\right) }{{t}^{a}}\right\rbrack  }_{1}^{X} + a{\int }_{1}^{X}\frac{F\left( t\right) }{{t}^{1 + a}}{dt}.
\]

La dernière intégrale converge absolument lorsque \( X \rightarrow + \infty \) car \( F \) est bornée et \( a > 0 \) . Quant au terme entre crochets, il converge également lorsque \( X \rightarrow + \infty \) toujours parce que \( F \) est bornée et \( a > 0 \) . On en déduit le résultat.

> The last integral converges absolutely as \( X \rightarrow + \infty \) because \( F \) is bounded and \( a > 0 \) . As for the term in brackets, it also converges as \( X \rightarrow + \infty \) again because \( F \) is bounded and \( a > 0 \) . We deduce the result from this.

EXERCICE 3. Donner la nature des deux intégrales suivantes :

> EXERCISE 3. Determine the nature of the following two integrals:

\[
\text{ a) }{\int }_{0}^{+\infty }\frac{dx}{1 + {x}^{4}{\sin }^{2}x}\;\mathbf{b})\;{\int }_{1}^{+\infty }{\left| \sin x\right| }^{x}{dx}\text{ . }
\]

Solution. a) La nature de cette intégrale ne peut pas être décidée en utilisant "les méthodes usuelles" de comparaison avec des fonctions dont la nature de l'intégrale est connue. On s'en sort autrement en utilisant une comparaison série-intégrale. Pour tout \( n \in \mathbb{N} \) , on pose

> Solution. a) The nature of this integral cannot be decided using "usual methods" of comparison with functions whose integral nature is known. We get around this by using a series-integral comparison. For all \( n \in \mathbb{N} \) , we set

\[
{u}_{n} = {\int }_{n\pi }^{\left( {n + 1}\right) \pi }f\left( x\right) {dx}\;\text{ où }\;f\left( x\right)  = \frac{1}{1 + {x}^{4}{\sin }^{2}x}.
\]

La fonction \( f \) étant positive, la série \( \sum {u}_{n} \) et l’intégrale \( {\int }_{0}^{+\infty }f\left( x\right) {dx} \) ont même nature (en effet, l’égalité \( {\int }_{0}^{n\pi }f\left( t\right) {dt} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{u}_{k} \) montre que si l’une est bornée l’autre l’est également). Nous sommes donc ramené à donner la nature de la série \( \sum {u}_{n} \) . Nous allons prouver qu’elle converge. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on a

> Since the function \( f \) is positive, the series \( \sum {u}_{n} \) and the integral \( {\int }_{0}^{+\infty }f\left( x\right) {dx} \) have the same nature (indeed, the equality \( {\int }_{0}^{n\pi }f\left( t\right) {dt} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{u}_{k} \) shows that if one is bounded, the other is as well). We are therefore reduced to determining the nature of the series \( \sum {u}_{n} \) . We will prove that it converges. For all \( n \in {\mathbb{N}}^{ * } \) , we have

\[
{u}_{n} \leq  {\int }_{n\pi }^{\left( {n + 1}\right) \pi }\frac{dt}{1 + {n}^{4}{\pi }^{4}{\sin }^{2}t} = {\int }_{0}^{\pi }\frac{dt}{1 + {n}^{4}{\pi }^{4}{\sin }^{2}t} = 2{\int }_{0}^{\pi /2}\frac{dt}{1 + {n}^{4}{\pi }^{4}{\sin }^{2}t} = 2{I}_{n}.
\]

La minoration classique \( \sin t \geq {2t}/\pi \) sur \( \left\lbrack {0,\pi /2}\right\rbrack \) (que l’on peut obtenir, par exemple, en utilisant la concavité de la fonction sinus sur cet intervalle) entraîne

> The classic lower bound \( \sin t \geq {2t}/\pi \) on \( \left\lbrack {0,\pi /2}\right\rbrack \) (which can be obtained, for example, by using the concavity of the sine function on this interval) leads to

\[
\forall n \in  {\mathbb{N}}^{ * },\;{I}_{n} \leq  {\int }_{0}^{\pi /2}\frac{dt}{1 + {n}^{4}{\pi }^{4}4{t}^{2}/{\pi }^{2}} = {\int }_{0}^{\pi /2}\frac{dt}{1 + 4{n}^{4}{\pi }^{2}{t}^{2}},
\]

ce qui en effectuant le changement de variable \( u = 4{n}^{2}{\pi t} \) entraîne

> which, by performing the change of variable \( u = 4{n}^{2}{\pi t} \), leads to

\[
\forall n \in  {\mathbb{N}}^{ * },\;{I}_{n} \leq  \frac{1}{4{n}^{2}\pi }{\int }_{0}^{2{n}^{2}{\pi }^{2}}\frac{du}{1 + {u}^{2}} \leq  \frac{1}{4{n}^{2}\pi }{\int }_{0}^{+\infty }\frac{du}{1 + {u}^{2}},
\]

autrement dit, \( {u}_{n} \leq 2{I}_{n} = O\left( {1/{n}^{2}}\right) \) . Ceci suffit pour conclure que la série \( \sum {u}_{n} \) converge.

> in other words, \( {u}_{n} \leq 2{I}_{n} = O\left( {1/{n}^{2}}\right) \). This is sufficient to conclude that the series \( \sum {u}_{n} \) converges.

b) Ici, comme précédemment, on ne peut pas s'en tirer en utilisant les méthodes usuelles de critère de convergence d'une intégrale. On procède également par comparaison série-intégrale. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on pose

> b) Here, as before, we cannot get by using the usual methods for the convergence criterion of an integral. We also proceed by series-integral comparison. For any \( n \in {\mathbb{N}}^{ * } \), we set

\[
{u}_{n} = {\int }_{\left( {n - 1}\right) \pi }^{n\pi }{\left| \sin x\right| }^{x}{dx}.
\]

La fonction intégrée étant positive, nous avons montré précédemment que l'intégrale et la série \( \sum {u}_{n} \) avaient même nature. Nous allons montrer cette fois que \( \sum {u}_{n} \) diverge. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on a

> Since the integrand is positive, we have shown previously that the integral and the series \( \sum {u}_{n} \) have the same nature. We will show this time that \( \sum {u}_{n} \) diverges. For any \( n \in {\mathbb{N}}^{ * } \), we have

\[
{u}_{n} \geq  {\int }_{\left( {n - 1}\right) \pi }^{n\pi }{\left| \sin x\right| }^{4n}{dx} = {\int }_{0}^{\pi }{\sin }^{4n}{xdx} = 2{\int }_{0}^{\pi /2}{\sin }^{4n}{xdx} = 2{I}_{n}.
\]

L’intégrale \( {I}_{n} \) est une intégrale classique : c’est une intégrale de Wallis, dont on sait (voir l’exercice 1, page 130) qu’elle est équivalente à \( \sqrt{\pi /\left( {8n}\right) } \) . Donc \( \sum {I}_{n} \) diverge, et comme \( {u}_{n} \geq 2{I}_{n} \) , \( \sum {u}_{n} \) diverge. L’intégrale proposée diverge donc.

> The integral \( {I}_{n} \) is a classic integral: it is a Wallis integral, which we know (see exercise 1, page 130) is equivalent to \( \sqrt{\pi /\left( {8n}\right) } \). Thus \( \sum {I}_{n} \) diverges, and since \( {u}_{n} \geq 2{I}_{n} \), \( \sum {u}_{n} \) diverges. The proposed integral therefore diverges.

EXERCICE 4. Soit \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une fonction continue par morceaux, positive et décroissante, et intégrable sur \( {\mathbb{R}}^{ + } \) . Montrer que \( f\left( x\right) = o\left( {1/x}\right) \) lorsque \( x \rightarrow + \infty \) .

> EXERCISE 4. Let \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a piecewise continuous, positive, and decreasing function, integrable on \( {\mathbb{R}}^{ + } \). Show that \( f\left( x\right) = o\left( {1/x}\right) \) as \( x \rightarrow + \infty \).

Solution. Soit \( \varepsilon > 0 \) . Comme \( f \) est intégrable, le critère de Cauchy s’applique, donc

> Solution. Let \( \varepsilon > 0 \). Since \( f \) is integrable, the Cauchy criterion applies, so

\[
\exists X > 0,\forall x > X,\;{\int }_{x}^{2x}f\left( t\right) {dt} < \varepsilon ,
\]

et on en déduit, la fonction \( f \) étant décroissante,

> and we deduce, since the function \( f \) is decreasing,

\[
\forall x > X,\;{xf}\left( {2x}\right)  = {\int }_{x}^{2x}f\left( {2x}\right) {dt} \leq  {\int }_{x}^{2x}f\left( t\right) {dt} < \varepsilon .
\]

Donc \( 0 \leq \left( {2x}\right) f\left( {2x}\right) \leq {2\varepsilon } \) pour tout \( x > X \) . Ceci entraîne \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}{xf}\left( x\right) = 0 \) d’où le résultat.

> Thus \( 0 \leq \left( {2x}\right) f\left( {2x}\right) \leq {2\varepsilon } \) for all \( x > X \). This leads to \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}{xf}\left( x\right) = 0 \), hence the result.

Remarque. Ce résultat est une version continue de celui de l'exercice 2 page 219.

> Remark. This result is a continuous version of the one in exercise 2 on page 219.

EXERCICE 5. a) Soit \( f : \rbrack 0,1\lbrack \rightarrow \mathbb{R} \) une fonction croissante telle que l’intégrale \( {\int }_{0}^{1}f\left( t\right) {dt} \) converge. Montrer que

> EXERCISE 5. a) Let \( f : \rbrack 0,1\lbrack \rightarrow \mathbb{R} \) be an increasing function such that the integral \( {\int }_{0}^{1}f\left( t\right) {dt} \) converges. Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}f\left( \frac{k}{n}\right)  = {\int }_{0}^{1}f\left( t\right) {dt}
\]

b) (Application.) Montrer que pour tout nombre réel \( \alpha > 0 \) , on a

> b) (Application.) Show that for any real number \( \alpha > 0 \), we have

\[
\mathop{\sum }\limits_{{k = 1}}^{n}{k}^{\alpha  - 1} \sim  \frac{{n}^{\alpha }}{\alpha }\text{ lorsque }n \rightarrow   + \infty .
\]

Solution. a) C’est ultra-classique. Il suffit d’écrire, la fonction \( f \) étant croissante, que

> Solution. a) This is ultra-classic. It suffices to write, since the function \( f \) is increasing, that

\[
\forall k \in  \{ 1,\ldots , n - 1\} ,\;{\int }_{\left( {k - 1}\right) /n}^{k/n}f\left( t\right) {dt} \leq  \frac{1}{n}f\left( \frac{k}{n}\right)  \leq  {\int }_{k/n}^{\left( {k + 1}\right) /n}f\left( t\right) {dt},
\]

puis de sommer cette relation pour \( k \) allant de 1 à \( n \) , ce qui donne

> then to sum this relation for \( k \) going from 1 to \( n \), which gives

\[
{\int }_{0}^{1 - 1/n}f\left( t\right) {dt} \leq  \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}f\left( \frac{k}{n}\right)  \leq  {\int }_{1/n}^{1}f\left( t\right) {dt},
\]

d’où le résultat en faisant tendre \( n \) vers l’infini puisque chacun des termes extrêmes de ces inégalités tend vers \( {\int }_{0}^{1}f\left( t\right) {dt} \) .

> hence the result by letting \( n \) tend to infinity, since each of the extreme terms of these inequalities tends to \( {\int }_{0}^{1}f\left( t\right) {dt} \).

b) En appliquant le résultat précédent à la fonction \( f : x \mapsto {x}^{\alpha - 1} \) , on obtient

> b) By applying the previous result to the function \( f : x \mapsto {x}^{\alpha - 1} \), we obtain

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{\left( \frac{k}{n}\right) }^{\alpha  - 1} = {\int }_{0}^{1}{t}^{\alpha  - 1}{dt} = \frac{1}{\alpha }\;\text{ donc }\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{{n}^{\alpha }}\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{k}^{\alpha  - 1} = \frac{1}{\alpha },
\]

et on en déduit facilement le résultat.

> and we easily deduce the result from this.

EXERCICE 6. Soient \( \varphi : \mathbb{R} \rightarrow \mathbb{C} \) une fonction continue par morceaux sur \( \mathbb{R}, T \) -périodique, et \( f : I \rightarrow \mathbb{C} \) une fonction continue par morceaux et intégrable sur un intervalle \( I \) de \( \mathbb{R} \) . On note \( a \) et \( b \) les extrémités de l’intervalle \( I \) , avec \( - \infty \leq a < b \leq + \infty \) . a) Montrer

> EXERCISE 6. Let \( \varphi : \mathbb{R} \rightarrow \mathbb{C} \) be a piecewise continuous \( \mathbb{R}, T \)-periodic function, and \( f : I \rightarrow \mathbb{C} \) be a piecewise continuous and integrable function on an interval \( I \) of \( \mathbb{R} \). Let \( a \) and \( b \) denote the endpoints of the interval \( I \), with \( - \infty \leq a < b \leq + \infty \). a) Show

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}f\left( t\right) \varphi \left( {nt}\right) {dt} = \frac{1}{T}\left( {{\int }_{0}^{T}\varphi \left( t\right) {dt}}\right)  \cdot  \left( {{\int }_{a}^{b}f\left( t\right) {dt}}\right) .
\]

(*)

> b) (Lemme de Riemann-Lebesgue) Montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\int }_{a}^{b}f\left( t\right) {e}^{int}{dt} = 0 \) . c) Si \( I \) est un segment de \( \mathbb{R} \) et \( f \) de classe \( {\mathcal{C}}^{1} \) sur \( I \) , montrer \( {\int }_{a}^{b}f\left( t\right) {e}^{int}{dt} = O\left( {1/n}\right) \) .

b) (Riemann-Lebesgue Lemma) Show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\int }_{a}^{b}f\left( t\right) {e}^{int}{dt} = 0 \). c) If \( I \) is a segment of \( \mathbb{R} \) and \( f \) is of class \( {\mathcal{C}}^{1} \) on \( I \), show \( {\int }_{a}^{b}f\left( t\right) {e}^{int}{dt} = O\left( {1/n}\right) \).

> d) On suppose \( I = \mathbb{R} \) . En utilisant le changement de variable \( u = t - \pi /n \) , obtenir directement (sans utiliser le résultat de la question a)) le lemme de Riemann-Lebesgue (question b)).

d) Assume \( I = \mathbb{R} \). Using the change of variable \( u = t - \pi /n \), obtain the Riemann-Lebesgue lemma (question b)) directly (without using the result from question a)).

> Solution. a) Posons \( K = \frac{1}{T}{\int }_{0}^{T}\varphi \left( t\right) {dt} \) . Il s’agit de montrer que

Solution. a) Let \( K = \frac{1}{T}{\int }_{0}^{T}\varphi \left( t\right) {dt} \). We must show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}f\left( t\right)  \cdot  \left( {\varphi \left( {nt}\right)  - K}\right) {dt} = 0\;\text{ ou encore }\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}f\left( t\right) \psi \left( {nt}\right) {dt} = 0
\]

\( \left( {* * }\right) \)

> avec \( \psi = \varphi - K \) . Notons que la fonction \( \psi \) vérifie \( {\int }_{0}^{T}\psi \left( t\right) {dt} = 0 \) . Pour prouver (**), nous allons procéder en trois étapes : d’abord lorsque \( f \) est la fonction caractéristique d’un segment inclus dans \( I \) , puis lorsque \( f \) est en escalier sur un segment de \( I \) , puis lorsque \( f \) est continue par morceaux et intégrable sur \( I \) .

with \( \psi = \varphi - K \) . Note that the function \( \psi \) satisfies \( {\int }_{0}^{T}\psi \left( t\right) {dt} = 0 \) . To prove (**), we will proceed in three steps: first when \( f \) is the characteristic function of a segment included in \( I \) , then when \( f \) is a step function on a segment of \( I \) , and finally when \( f \) is piecewise continuous and integrable on \( I \) .

> (i) Si \( f \) est la fonction caractéristique d’un segment \( J = \left\lbrack {\alpha ,\beta }\right\rbrack \) inclus dans \( I \) , on a

(i) If \( f \) is the characteristic function of a segment \( J = \left\lbrack {\alpha ,\beta }\right\rbrack \) included in \( I \) , we have

\[
{I}_{n} = {\int }_{a}^{b}f\left( t\right) \psi \left( {nt}\right) {dt} = {\int }_{\alpha }^{\beta }\psi \left( {nt}\right) {dt} = \frac{1}{n}{\int }_{n\alpha }^{n\beta }\psi \left( t\right) {dt}.
\]

Soit \( p \) l’entier naturel tel que \( {n\alpha } + {pT} \leq {n\beta } < {n\alpha } + \left( {p + 1}\right) T \) ( \( p \) est la partie entière de \( n\left( {\beta - \alpha }\right) /T) \) . On peut écrire

> Let \( p \) be the natural integer such that \( {n\alpha } + {pT} \leq {n\beta } < {n\alpha } + \left( {p + 1}\right) T \) ( \( p \) is the integer part of \( n\left( {\beta - \alpha }\right) /T) \) . We can write

\[
{I}_{n} = \frac{1}{n}\left( {{\int }_{n\alpha }^{{n\alpha } + {pT}}\psi \left( t\right) {dt} + {\int }_{{n\alpha } + {pT}}^{n\beta }\psi \left( t\right) {dt}}\right)
\]

\[
= \frac{1}{n}\left( {p{\int }_{0}^{T}\psi \left( t\right) {dt} + {\int }_{{n\alpha } + {pT}}^{n\beta }\psi \left( t\right) {dt}}\right)  = \frac{1}{n}{\int }_{{n\alpha } + {pT}}^{n\beta }\psi \left( t\right) {dt},
\]

et comme \( 0 \leq {n\beta } - \left( {{n\alpha } + {pT}}\right) < T \) ceci entraîne

> and since \( 0 \leq {n\beta } - \left( {{n\alpha } + {pT}}\right) < T \) this implies

\[
\left| {I}_{n}\right|  \leq  \frac{1}{n}{\int }_{0}^{T}\left| {\psi \left( t\right) }\right| {dt}
\]

On en déduit que (**) est bien vérifié pour \( f \) .

> We deduce that (**) is indeed satisfied for \( f \) .

(ii) Si \( f \) est une fonction en escalier sur un segment inclus dans \( I, f \) est combinaison linéaire de fonctions caractéristiques de segments inclus dans \( I \) , on en déduit par linéarité que (**) reste vrai pour \( f \) .

> (ii) If \( f \) is a step function on a segment included in \( I, f \) , it is a linear combination of characteristic functions of segments included in \( I \) , we deduce by linearity that (**) remains true for \( f \) .

(iii) Traitons maintenant le cas où \( f \) est continue par morceaux et intégrable sur \( I \) . Soit \( \varepsilon > 0 \) . Comme \( f \) est intégrable, il existe un segment \( J = \left\lbrack {c, d}\right\rbrack \) inclus dans \( I \) tel que \( {\int }_{a}^{c}\left| {f\left( t\right) }\right| {dt} + {\int }_{d}^{b}\left| {f\left( t\right) }\right| {dt} < \varepsilon \) . Ensuite, la restriction de \( f \) à \( J \) étant continue par morceaux, elle est réglée donc il existe une fonction en escalier \( g \) telle que \( \left| {f - g}\right| < \varepsilon /\left( {d - c}\right) \) sur \( J \) . L’étape précédente nous assure l’existence de \( N \in \mathbb{N} \) tel que pour tout \( n \geq N \) , \( \left| {{\int }_{c}^{d}g\left( t\right) \psi \left( {nt}\right) {dt}}\right| < \varepsilon \) . Ainsi, en notant \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {0, T}\right\rbrack }}\left| {\psi \left( t\right) }\right| = \mathop{\sup }\limits_{{t \in \mathbb{R}}}\left| {\psi \left( t\right) }\right| \) , on a, pour \( n \geq N \)

> (iii) Let us now treat the case where \( f \) is piecewise continuous and integrable on \( I \) . Let \( \varepsilon > 0 \) . Since \( f \) is integrable, there exists a segment \( J = \left\lbrack {c, d}\right\rbrack \) included in \( I \) such that \( {\int }_{a}^{c}\left| {f\left( t\right) }\right| {dt} + {\int }_{d}^{b}\left| {f\left( t\right) }\right| {dt} < \varepsilon \) . Next, the restriction of \( f \) to \( J \) being piecewise continuous, it is regulated, so there exists a step function \( g \) such that \( \left| {f - g}\right| < \varepsilon /\left( {d - c}\right) \) on \( J \) . The previous step ensures the existence of \( N \in \mathbb{N} \) such that for all \( n \geq N \) , \( \left| {{\int }_{c}^{d}g\left( t\right) \psi \left( {nt}\right) {dt}}\right| < \varepsilon \) . Thus, by denoting \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {0, T}\right\rbrack }}\left| {\psi \left( t\right) }\right| = \mathop{\sup }\limits_{{t \in \mathbb{R}}}\left| {\psi \left( t\right) }\right| \) , we have, for \( n \geq N \)

\[
\left| {{\int }_{c}^{d}f\left( t\right) \psi \left( {nt}\right) {dt}}\right|  \leq  {\int }_{c}^{d}\left| {f\left( t\right)  - g\left( t\right) }\right|  \cdot  \left| {\psi \left( {nt}\right) }\right| {dt} + \left| {{\int }_{c}^{d}g\left( t\right) \psi \left( {nt}\right) {dt}}\right|  \leq  {M\varepsilon } + \varepsilon .
\]

Ceci entraîne que lorsque \( n \geq N \) ,

> This implies that when \( n \geq N \) ,

\[
\left| {{\int }_{a}^{b}f\left( t\right) \psi \left( {nt}\right) {dt}}\right|  \leq  M{\int }_{a}^{c}\left| {f\left( t\right) }\right| {dt} + \left| {{\int }_{c}^{d}f\left( t\right) \psi \left( {nt}\right) {dt}}\right|  + M{\int }_{d}^{b}\left| {f\left( t\right) }\right| {dt} \leq  {2M\varepsilon } + \varepsilon .
\]

Ceci termine la solution de la question a).

> This completes the solution to question a).

b) C’est une conséquence directe du résultat de la question précédente, car \( t \mapsto {e}^{it} \) est \( {2\pi } \) - périodique et \( {\int }_{0}^{2\pi }{e}^{it}{dt} = 0 \) .

> b) This is a direct consequence of the result from the previous question, because \( t \mapsto {e}^{it} \) is \( {2\pi } \) -periodic and \( {\int }_{0}^{2\pi }{e}^{it}{dt} = 0 \) .

c) Lorsque \( f \) est de classe \( {\mathcal{C}}^{1} \) sur le segment \( I = \left\lbrack {a, b}\right\rbrack \) , on procède en intégrant par parties :

> c) When \( f \) is of class \( {\mathcal{C}}^{1} \) on the segment \( I = \left\lbrack {a, b}\right\rbrack \) , we proceed by integrating by parts:

\[
{I}_{n} = {\int }_{a}^{b}f\left( t\right) {e}^{int}{dt} = {\left\lbrack  f\left( t\right) \frac{{e}^{int}}{in}\right\rbrack  }_{a}^{b} - \frac{1}{in}{\int }_{a}^{b}{f}^{\prime }\left( t\right) {e}^{int}{dt}
\]

(***)

> donc

therefore

\[
\left| {I}_{n}\right|  \leq  \frac{1}{n}\left( {\left| {f\left( b\right) }\right|  + \left| {f\left( a\right) }\right|  + {\int }_{a}^{b}\left| {{f}^{\prime }\left( t\right) }\right| {dt}}\right) ,
\]

d’où \( {I}_{n} = O\left( {1/n}\right) \) .

> whence \( {I}_{n} = O\left( {1/n}\right) \) .

d) Lorsque \( n \in {\mathbb{N}}^{ * } \) , le changement de variable \( u = t - \pi /n \) donne

> d) When \( n \in {\mathbb{N}}^{ * } \) , the change of variable \( u = t - \pi /n \) gives

\[
{I}_{n} = {\int }_{-\infty }^{+\infty }f\left( t\right) {e}^{int}{dt} = {\int }_{-\infty }^{+\infty }f\left( {u + \pi /n}\right) {e}^{{inu} + {i\pi }}{du} =  - {\int }_{-\infty }^{+\infty }f\left( {t + \pi /n}\right) {e}^{int}{dt},
\]

d'où on déduit

> from which we deduce

\[
2{I}_{n} = {\int }_{-\infty }^{+\infty }\left( {f\left( t\right)  - f\left( {t + \pi /n}\right) }\right) {e}^{int}{dt}.
\]

\( \left( {* * * * }\right) \)

> L’intégrande de cette intégrale converge simplement vers 0 lorsque \( n \rightarrow \infty \) , mais son module n’est pas majoré par une fonction intégrable \( \varphi \) indépendamment de \( n \) . La convergence de (****) vers 0 s’obtient en écrivant \( \left| {I}_{n}\right| \leq \frac{1}{2}{\int }_{-\infty }^{+\infty }\left| {f\left( t\right) - f\left( {t + \pi /n}\right) }\right| {dt} \) et en procédant comme dans la solution de la question a) du problème 6 page 180.

The integrand of this integral converges pointwise to 0 as \( n \rightarrow \infty \) , but its modulus is not bounded by an integrable function \( \varphi \) independently of \( n \) . The convergence of (****) to 0 is obtained by writing \( \left| {I}_{n}\right| \leq \frac{1}{2}{\int }_{-\infty }^{+\infty }\left| {f\left( t\right) - f\left( {t + \pi /n}\right) }\right| {dt} \) and proceeding as in the solution to question a) of problem 6 on page 180.

> Remarque. - Lorsque \( I \) est un segment et si \( f \) est suffisamment régulière, on peut obtenir un développement asymptotique de \( {I}_{n} \) en itérant l’intégration par parties dans (***).

Remark. - When \( I \) is a segment and if \( f \) is sufficiently regular, one can obtain an asymptotic expansion of \( {I}_{n} \) by iterating integration by parts in (***).

> - Le résultat de la question c) se généralise aisément lorsqu’on remplace \( {e}^{int} \) par une fonction continue \( T \) -périodique \( \varphi \) telle que \( {\int }_{0}^{T}\varphi \left( t\right) {dt} = 0 \) .

- The result of question c) is easily generalized when replacing \( {e}^{int} \) with a continuous \( T \) -periodic function \( \varphi \) such that \( {\int }_{0}^{T}\varphi \left( t\right) {dt} = 0 \) .

> EXERCICE 7. a) Soit \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une fonction continue par morceaux et décroissante, telle que l’intégrale \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converge et est non nulle. Pour tout \( t > 0 \) , prouver la convergence de

EXERCISE 7. a) Let \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a piecewise continuous and decreasing function, such that the integral \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converges and is non-zero. For all \( t > 0 \) , prove the convergence of

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}f\left( {nt}\right)
\]

et donner un équivalent de cette dernière expression lorsque \( t \rightarrow {0}^{ + } \) .

> and give an equivalent of this last expression when \( t \rightarrow {0}^{ + } \) .

b) (Application.) Donner un équivalent, lorsque \( x \rightarrow {1}^{ - } \) , de la série entière

> b) (Application.) Give an equivalent, when \( x \rightarrow {1}^{ - } \) , of the power series

\[
x \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{{n}^{2}}
\]

Solution. a) La fonction \( f \) décroît et son intégrale converge, on en déduit que \( f \) tend vers 0 à l’infini. En utilisant encore la décroissance de \( f \) , on en déduit que \( f \) est positive.

> Solution. a) The function \( f \) is decreasing and its integral converges, from which we deduce that \( f \) tends to 0 at infinity. Using the decreasing nature of \( f \) again, we deduce that \( f \) is positive.

Ensuite, on procède comme dans l'exercice 5. La fonction \( f \) étant décroissante, on a

> Next, we proceed as in exercise 5. Since the function \( f \) is decreasing, we have

\[
\forall t > 0,\forall n \in  {\mathbb{N}}^{ * },\;{\int }_{nt}^{\left( {n + 1}\right) t}f\left( x\right) {dx} \leq  {tf}\left( {nt}\right)  \leq  {\int }_{\left( {n - 1}\right) t}^{nt}f\left( x\right) {dx}.
\]

(*)

> La dernière inégalité entraîne par sommation

The last inequality implies by summation

\[
\forall t > 0,\forall N \in  {\mathbb{N}}^{ * },\;t\mathop{\sum }\limits_{{n = 1}}^{N}f\left( {nt}\right)  \leq  {\int }_{0}^{Nt}f\left( x\right) {dx} \leq  {\int }_{0}^{+\infty }f\left( x\right) {dx},
\]

autrement dit, les sommes partielles de la série étudiée sont majorées (lorsque \( t > 0 \) est fixé). Les termes de la série étant positifs, on en déduit qu’elle converge, et ceci pour tout \( t > 0 \) . Maintenant, par sommation de (*) sur \( n \in {\mathbb{N}}^{ * } \) , on obtient

> in other words, the partial sums of the series studied are bounded (when \( t > 0 \) is fixed). Since the terms of the series are positive, we deduce that it converges, and this for all \( t > 0 \) . Now, by summing (*) over \( n \in {\mathbb{N}}^{ * } \) , we obtain

\[
\forall t > 0,\;{\int }_{t}^{+\infty }f\left( x\right) {dx} \leq  t\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}f\left( {nt}\right)  \leq  {\int }_{0}^{+\infty }f\left( x\right) {dx},
\]

et on en déduit que

> and we deduce that

\[
\mathop{\lim }\limits_{{t \rightarrow  {0}^{ + }}}t\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}f\left( {nt}\right)  = {\int }_{0}^{+\infty }f\left( x\right) {dx}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}f\left( {nt}\right)  \sim  \frac{1}{t}{\int }_{0}^{+\infty }f\left( x\right) {dx}
\]

(cette dernière assertion a bien un sens car l'intégrale est non nulle par hypothèse).

> (this last assertion is well-defined because the integral is non-zero by hypothesis).

b) En posant \( x = {e}^{-{t}^{2}} \) , on a

> b) By setting \( x = {e}^{-{t}^{2}} \) , we have

\[
\forall x \in  \rbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{{n}^{2}} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{e}^{-{\left( nt\right) }^{2}} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}f\left( {nt}\right)
\]

avec \( f : u \mapsto {e}^{-{u}^{2}} \) . En posant \( c = {\int }_{0}^{+\infty }{e}^{-{u}^{2}}{du} \) , on en déduit grâce au résultat de la question précédente que

> with \( f : u \mapsto {e}^{-{u}^{2}} \) . By setting \( c = {\int }_{0}^{+\infty }{e}^{-{u}^{2}}{du} \) , we deduce from the result of the previous question that

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{{n}^{2}} \sim  \frac{c}{t} = \frac{c}{\sqrt{-\log x}} \sim  \frac{c}{\sqrt{1 - x}}.
\]

Remarque. On peut montrer que \( c = \sqrt{\pi }/2 \) (voir l’exercice 2 page 167). EXERCICE 8. Soit \( f : \lbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) une fonction continue telle que l’intégrale

> Remark. It can be shown that \( c = \sqrt{\pi }/2 \) (see exercise 2 on page 167). EXERCISE 8. Let \( f : \lbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) be a continuous function such that the integral

\[
{\int }_{1}^{+\infty }\frac{f\left( t\right) }{t}{dt}
\]

converge.

> converges.

a) Soient deux nombres réels strictement positifs \( a \) et \( b \) . Montrer que l’intégrale

> a) Let \( a \) and \( b \) be two strictly positive real numbers. Show that the integral

\[
{\int }_{0}^{+\infty }\frac{f\left( {at}\right)  - f\left( {bt}\right) }{t}{dt}
\]

converge et calculer sa valeur.

> converges and calculate its value.

b) (Application.) Si \( a, b > 0 \) , calculer l’intégrale

> b) (Application.) If \( a, b > 0 \) , calculate the integral

\[
{\int }_{0}^{+\infty }\frac{{e}^{-{at}} - {e}^{-{bt}}}{t}{dt}
\]

Solution. a) Nous allons en même temps prouver la convergence de l'intégrale et donner sa valeur. Posons

> Solution. a) We will simultaneously prove the convergence of the integral and provide its value. Let

\[
g : \rbrack 0, + \infty \left\lbrack  { \rightarrow  \mathbb{R}\;t \mapsto  \frac{f\left( {at}\right)  - f\left( {bt}\right) }{t}.}\right.
\]

Le changement de variable \( x = {\alpha t} \) montre que pour tout \( \alpha > 0,{\int }_{1}^{+\infty }\left( {f\left( {\alpha t}\right) /t}\right) {dt} \) est de même nature que \( {\int }_{\alpha }^{+\infty }\left( {f\left( t\right) /t}\right) {dt} \) , c’est-à-dire convergente. L’intégrale \( {\int }_{1}^{+\infty }g\left( t\right) {dt} \) converge donc. En définitive, il s'agit pour nous de prouver l'existence et donner la valeur de

> The change of variable \( x = {\alpha t} \) shows that for any \( \alpha > 0,{\int }_{1}^{+\infty }\left( {f\left( {\alpha t}\right) /t}\right) {dt} \) it is of the same nature as \( {\int }_{\alpha }^{+\infty }\left( {f\left( t\right) /t}\right) {dt} \) , that is to say convergent. The integral \( {\int }_{1}^{+\infty }g\left( t\right) {dt} \) therefore converges. Ultimately, we need to prove the existence and provide the value of

\[
\mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x > 0} }}{\int }_{x}^{+\infty }g\left( t\right) {dt}
\]

En effectuant les changements de variable \( u = {at} \) et \( v = {bt} \) , on trouve respectivement

> By performing the changes of variable \( u = {at} \) and \( v = {bt} \) , we find respectively

\[
\forall x > 0,\;{\int }_{x}^{+\infty }\frac{f\left( {at}\right) }{t}{dt} = {\int }_{ax}^{+\infty }\frac{f\left( u\right) }{u}{du}\;\text{ et }\;{\int }_{x}^{+\infty }\frac{f\left( {bt}\right) }{t}{dt} = {\int }_{bx}^{+\infty }\frac{f\left( v\right) }{v}{dv},
\]

d'où on tire

> from which we derive

\[
\forall x > 0,\;{\int }_{x}^{+\infty }g\left( t\right) {dt} = {\int }_{ax}^{+\infty }\frac{f\left( t\right) }{t}{dt} - {\int }_{bx}^{+\infty }\frac{f\left( t\right) }{t}{dt} = {\int }_{ax}^{bx}\frac{f\left( t\right) }{t}{dt}.
\]

La fonction \( f \) étant continue, on a d’après la première formule de la moyenne

> Since the function \( f \) is continuous, we have according to the first mean value theorem

\[
\left. {\forall x > 0,\exists {c}_{x} \in  }\right\rbrack  {ax},{bx}\left\lbrack  {,\;{\int }_{x}^{+\infty }g\left( t\right) {dt} = {\int }_{ax}^{bx}\frac{f\left( t\right) }{t}{dt} = f\left( {c}_{x}\right) {\int }_{ax}^{bx}\frac{dt}{t} = f\left( {c}_{x}\right) \log \frac{b}{a}.}\right.
\]

Comme \( f \) est continue en 0 et que \( {c}_{x} \) tend vers 0 avec \( x \) , on en déduit que

> As \( f \) is continuous at 0 and \( {c}_{x} \) tends to 0 as \( x \) does, we deduce that

\[
\mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x > 0} }}{\int }_{x}^{+\infty }g\left( t\right) {dt} = f\left( 0\right) \log \frac{b}{a}.
\]

Autrement dit, l’intégrale proposée converge et sa valeur est \( f\left( 0\right) \log \left( {b/a}\right) \) .

> In other words, the proposed integral converges and its value is \( f\left( 0\right) \log \left( {b/a}\right) \) .

b) Il suffit d’appliquer le résultat de la question précédente à la fonction \( f : x \mapsto {e}^{-x} \) qui vérifie bien les hypothèses requises. En 0, cette fonction prend la valeur 1, donc l'intégrale converge et

> b) It suffices to apply the result of the previous question to the function \( f : x \mapsto {e}^{-x} \) which satisfies the required hypotheses. At 0, this function takes the value 1, so the integral converges and

\[
{\int }_{0}^{+\infty }\frac{{e}^{-{at}} - {e}^{-{bt}}}{t}{dt} = \log \frac{b}{a}.
\]

EXERCICE 9. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction continue par morceaux, positive, telle que \( {f}^{2} \) est intégrable sur \( {\mathbb{R}}^{ + } \) . Montrer que lorsque \( x \rightarrow + \infty \) ,

> EXERCISE 9. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a piecewise continuous, positive function such that \( {f}^{2} \) is integrable on \( {\mathbb{R}}^{ + } \) . Show that as \( x \rightarrow + \infty \) ,

\[
{\int }_{0}^{x}f\left( t\right) {dt} = o\left( \sqrt{x}\right) .
\]

Solution. On pense bien sûr à utiliser l'inégalité de Schwarz. En l'utilisant sur le domaine \( \left\lbrack {0, x}\right\rbrack \) on montre seulement que \( {\int }_{0}^{x}f\left( t\right) {dt} = O\left( \sqrt{x}\right) \) , mais on n’a pas le petit o. On procède autrement.

> Solution. One naturally thinks of using the Schwarz inequality. By using it on the domain \( \left\lbrack {0, x}\right\rbrack \) we only show that \( {\int }_{0}^{x}f\left( t\right) {dt} = O\left( \sqrt{x}\right) \) , but we do not get the little o. We proceed differently.

Soit \( \varepsilon > 0 \) et soit \( {x}_{0} > 0 \) tel que \( {\int }_{{x}_{0}}^{+\infty }{f}^{2}\left( t\right) {dt} < {\varepsilon }^{2} \) . Pour tout \( x > {x}_{0} \) , l’inégalité de Schwarz entraîne

> Let \( \varepsilon > 0 \) and let \( {x}_{0} > 0 \) be such that \( {\int }_{{x}_{0}}^{+\infty }{f}^{2}\left( t\right) {dt} < {\varepsilon }^{2} \) . For any \( x > {x}_{0} \) , the Schwarz inequality implies

\[
{\int }_{{x}_{0}}^{x}f\left( t\right) {dt} = {\int }_{{x}_{0}}^{x}1 \cdot  f\left( t\right) {dt} \leq  {\left( {\int }_{{x}_{0}}^{x}dt\right) }^{1/2} \cdot  {\left( {\int }_{{x}_{0}}^{x}{f}^{2}\left( t\right) dt\right) }^{1/2} \leq  \left( \sqrt{x - {x}_{0}}\right) \varepsilon ,
\]

donc si on choisit \( {x}_{1} > {x}_{0} \) tel que \( {\int }_{0}^{{x}_{0}}f\left( t\right) {dt} \leq \varepsilon \sqrt{{x}_{1}} \) , on a

> so if we choose \( {x}_{1} > {x}_{0} \) such that \( {\int }_{0}^{{x}_{0}}f\left( t\right) {dt} \leq \varepsilon \sqrt{{x}_{1}} \) , we have

\[
\forall x > {x}_{1},\;{\int }_{0}^{x}f\left( t\right) {dt} \leq  {\int }_{0}^{{x}_{0}}f\left( t\right) {dt} + \varepsilon \sqrt{x - {x}_{0}} \leq  \varepsilon \left( {\sqrt{{x}_{1}} + \sqrt{x}}\right)  \leq  {2\varepsilon }\sqrt{x}.
\]

Par ailleurs \( f \) est positive donc \( {\int }_{0}^{x}f \) également. On en déduit le résultat.

> Furthermore, \( f \) is positive, so \( {\int }_{0}^{x}f \) is as well. We deduce the result.
