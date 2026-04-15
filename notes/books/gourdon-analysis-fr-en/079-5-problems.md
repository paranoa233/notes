### 5. Problems

*Français : 5. Problèmes*

Problem 1. Soient \( \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) non réduit à un singleton et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) une application de classe \( {\mathcal{C}}^{1} \) telle que \( f\left( a\right) = 0 \) . Montrer les deux inégalités suivantes et caractériser l'égalité.

> Problem 1. Let \( \left\lbrack {a, b}\right\rbrack \) be a segment of \( \mathbb{R} \) not reduced to a singleton and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) be a function of class \( {\mathcal{C}}^{1} \) such that \( f\left( a\right) = 0 \) . Show the following two inequalities and characterize the equality.

\[
\text{ a) }\;{\int }_{a}^{b}{\left| f\left( x\right) \right| }^{2}{dx}\; \leq  \frac{{\left( b - a\right) }^{2}}{2}{\int }_{a}^{b}{\left| {f}^{\prime }\left( x\right) \right| }^{2}{dx}
\]

\[
\text{ b) }\;{\int }_{a}^{b}\left| {{f}^{\prime }\left( x\right) f\left( x\right) }\right| {dx} \leq  \left( \frac{b - a}{2}\right) {\int }_{a}^{b}{\left| {f}^{\prime }\left( x\right) \right| }^{2}{dx}\text{ . }
\]

Solution. a) L'inégalité de Schwarz entraîne

> Solution. a) The Schwarz inequality implies

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;{\left| f\left( x\right) \right| }^{2} = {\left| {\int }_{a}^{x}{f}^{\prime }\left( t\right) dt\right| }^{2} \leq  \left( {{\int }_{a}^{x}{\left| {f}^{\prime }\left( t\right) \right| }^{2}{dt}}\right)  \cdot  \left( {{\int }_{a}^{x}{1dt}}\right)  \leq  \left( {x - a}\right) {\int }_{a}^{b}{\left| {f}^{\prime }\left( t\right) \right| }^{2}{dt}\;\left( *\right)
\]

(*)

> d'où l'inégalité désirée en intégrant (*) sur \( \left\lbrack {a, b}\right\rbrack \) .

from which the desired inequality follows by integrating (*) over \( \left\lbrack {a, b}\right\rbrack \) .

> Les fonctions en présence étant continues, l'égalité se produira si et seulement si chacune des inégalités précédentes est une égalité. En particulier, s'il y a égalité, la dernière inégalité de (*) doit être une égalité, ce qui entraîne

Since the functions involved are continuous, equality will occur if and only if each of the preceding inequalities is an equality. In particular, if there is equality, the last inequality of (*) must be an equality, which implies

\[
\forall x \in  \rbrack a, b\rbrack ,\;{\int }_{a}^{x}\left| {{f}^{\prime }\left( t\right) }\right| {dt} = {\int }_{a}^{b}\left| {{f}^{\prime }\left( t\right) }\right| {dt}.
\]

Comme \( \left. {\left| {f}^{\prime }\right| \text{ est continue, ceci entraîne que }{f}^{\prime }\text{ est nulle sur }}\right\rbrack a, b\rbrack \) donc sur \( \left\lbrack {a, b}\right\rbrack \) par continuité. La fonction \( f \) est donc constante, et comme \( f\left( a\right) = 0, f \) est nulle. Réciproquement, si \( f \) est nulle, il y a bien égalité.

> Since \( \left. {\left| {f}^{\prime }\right| \text{ est continue, ceci entraîne que }{f}^{\prime }\text{ est nulle sur }}\right\rbrack a, b\rbrack \) therefore on \( \left\lbrack {a, b}\right\rbrack \) by continuity. The function \( f \) is thus constant, and since \( f\left( a\right) = 0, f \) is zero. Conversely, if \( f \) is zero, there is indeed equality.

b) On pose

> b) Let us set

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;u\left( x\right)  = {\int }_{a}^{x}\left| {{f}^{\prime }\left( t\right) }\right| {dt}.
\]

La fonction \( u \) vérifie

> The function \( u \) satisfies

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;\left| {f\left( x\right) }\right|  = \left| {{\int }_{a}^{x}{f}^{\prime }\left( t\right) {dt}}\right|  \leq  {\int }_{a}^{x}\left| {{f}^{\prime }\left( t\right) }\right| {dt} = u\left( x\right) .
\]

En particulier,

> In particular,

\[
{\int }_{a}^{b}\left| {{f}^{\prime }\left( x\right) f\left( x\right) }\right| {dx} \leq  {\int }_{a}^{b}\left| {{f}^{\prime }\left( x\right) }\right| u\left( x\right) {dx} = {\int }_{a}^{b}{u}^{\prime }\left( x\right) u\left( x\right) {dx} = {\left\lbrack  \frac{{u}^{2}\left( x\right) }{2}\right\rbrack  }_{a}^{b} = \frac{1}{2}{\left( {\int }_{a}^{b}\left| {f}^{\prime }\left( x\right) \right| dt\right) }^{2}.
\]

En appliquant l'inégalité de Schwarz, on a

> By applying the Schwarz inequality, we have

\[
{\left( {\int }_{a}^{b}\left| {f}^{\prime }\left( x\right) \right| dx\right) }^{2} \leq  \left( {{\int }_{a}^{b}{1dx}}\right)  \cdot  \left( {{\int }_{a}^{b}{\left| {f}^{\prime }\left( x\right) \right| }^{2}{dt}}\right)  = \left( {b - a}\right) {\int }_{a}^{b}{\left| {f}^{\prime }\left( x\right) \right| }^{2}{dt},
\]

\( \left( {* * }\right) \)

> d'où l'inégalité désirée.

from which the desired inequality follows.

> S’il y a égalité, alors l’inégalité de Schwarz (**) est une égalité, donc les fonctions \( t \mapsto {f}^{\prime }\left( t\right) \) et \( t \mapsto 1 \) sont liées, autrement dit \( {f}^{\prime } \) est constante et \( f \) est affine. Réciproquement, si \( f \) est affine, chacune des inégalités précédente est une égalité. Finalement, l'inégalité b) est une égalité si et seulement si \( f \) est affine (et toujours \( f\left( a\right) = 0 \) ).

If there is equality, then the Schwarz inequality (**) is an equality, so the functions \( t \mapsto {f}^{\prime }\left( t\right) \) and \( t \mapsto 1 \) are proportional, in other words \( {f}^{\prime } \) is constant and \( f \) is affine. Conversely, if \( f \) is affine, each of the preceding inequalities is an equality. Finally, inequality b) is an equality if and only if \( f \) is affine (and still \( f\left( a\right) = 0 \) ).

> Problème 2. On considère l'application

Problem 2. Consider the mapping

\[
F : \left\lbrack  {0,1\left\lbrack  { \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{x}^{{x}^{2}}\frac{dt}{\log t}.}\right. }\right.
\]

Montrer l’existence de \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) \) et calculer cette limite. En déduire la valeur de l'intégrale

> Show the existence of \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) \) and calculate this limit. Deduce the value of the integral

\[
I = {\int }_{0}^{1}\frac{t - 1}{\log t}{dt}
\]

Solution. On ne sait pas exprimer une primitive de \( t \mapsto 1/\log t \) avec des fonctions usuelles (en fait, on ne peut pas !). Cependant, lorsque \( t \) est voisin de \( 1,1/\log t \) est proche de \( 1/\left( {t\log t}\right) \) dont on connaît une primitive. C’est cette idée que nous mettons en forme. Pour tout \( x \in \rbrack 0,1\lbrack \) , on a

> Solution. We do not know how to express an antiderivative of \( t \mapsto 1/\log t \) using standard functions (in fact, we cannot!). However, when \( t \) is close to \( 1,1/\log t \), it is close to \( 1/\left( {t\log t}\right) \), for which we know an antiderivative. We formalize this idea. For all \( x \in \rbrack 0,1\lbrack \), we have

\[
\forall t \in  \left\lbrack  {{x}^{2}, x}\right\rbrack  ,\;\frac{{x}^{2}}{t\log t} \leq  \frac{1}{\log t} \leq  \frac{x}{t\log t},
\]

donc par intégration

> therefore, by integration

\[
{x}^{2}{\int }_{x}^{{x}^{2}}\frac{dt}{t\log t} \leq  F\left( x\right)  \leq  x{\int }_{x}^{{x}^{2}}\frac{dt}{t\log t}.
\]

Sachant que

> Knowing that

\[
{\int }_{x}^{{x}^{2}}\frac{dt}{t\log t} = {\left\lbrack  \log \left( \log t\right) \right\rbrack  }_{x}^{{x}^{2}} = \log 2
\]

on a donc \( {x}^{2}\log 2 \leq F\left( x\right) \leq x\log 2 \) pour tout \( x \in \rbrack 0,1\left\lbrack \right. \) . On en déduit \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) = \log 2 \) et \( F\left( 0\right) = 0 \) .

> we therefore have \( {x}^{2}\log 2 \leq F\left( x\right) \leq x\log 2 \) for all \( x \in \rbrack 0,1\left\lbrack \right. \). We deduce \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) = \log 2 \) and \( F\left( 0\right) = 0 \).

Donnons maintenant la valeur de \( I \) . La fonction \( F \) est dérivable sur \( \rbrack 0,1\lbrack \) et on a

> Let us now give the value of \( I \). The function \( F \) is differentiable on \( \rbrack 0,1\lbrack \) and we have

\[
\forall x \in  \rbrack 0,1\left\lbrack  {,\;{F}^{\prime }\left( x\right)  = \frac{2x}{\log \left( {x}^{2}\right) } - \frac{1}{\log x} = \frac{x - 1}{\log x}.}\right.
\]

Donc

> Therefore

\[
I = {\int }_{0}^{1}\frac{t - 1}{\log t}{dt} = {\int }_{0}^{1}{F}^{\prime }\left( t\right) {dt} = \mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}F\left( x\right)  - F\left( 0\right)  = \log 2.
\]

Problems 3 (INTÉGRALE DE DIRICHLET). Calculer l'intégrale

> Problem 3 (DIRICHLET INTEGRAL). Calculate the integral

\[
I = {\int }_{0}^{\pi /2}\log \left( {\sin x}\right) {dx}.
\]

Solution. La convergence de l’intégrale est immédiate (en 0, \( \log \left( {\sin x}\right) = \log \left( {x + o\left( x\right) }\right) = \; \log x + \log \left( {1 + o\left( 1\right) }\right) \sim \log x \) ). On ne sait pas exprimer de primitive de l’intégrande de \( I \) avec des fonctions usuelles (c'est d'ailleurs là que réside tout l'intérêt de l'exercice).

> Solution. The convergence of the integral is immediate (at 0, \( \log \left( {\sin x}\right) = \log \left( {x + o\left( x\right) }\right) = \; \log x + \log \left( {1 + o\left( 1\right) }\right) \sim \log x \)). We do not know how to express an antiderivative of the integrand of \( I \) using standard functions (this is, in fact, where the whole interest of the exercise lies).

Pour calculer \( I \) , on utilise la formule \( \sin x = 2\sin \left( {x/2}\right) \cos \left( {x/2}\right) \) qui entraîne

> To calculate \( I \), we use the formula \( \sin x = 2\sin \left( {x/2}\right) \cos \left( {x/2}\right) \) which implies

\[
I = {\int }_{0}^{\pi /2}\log {2dx} + {\int }_{0}^{\pi /2}\log \left( {\sin \frac{x}{2}}\right) {dx} + {\int }_{0}^{\pi /2}\log \left( {\cos \frac{x}{2}}\right) {dx}
\]

\[
= \frac{\pi \log 2}{2} + 2{\int }_{0}^{\pi /4}\log \left( {\sin x}\right) {dx} + 2{\int }_{0}^{\pi /4}\log \left( {\cos x}\right) {dx}.
\]

(*)

> Le changement de variable \( u = \pi /2 - x \) montre que

The change of variable \( u = \pi /2 - x \) shows that

\[
{\int }_{0}^{\pi /4}\log \left( {\cos x}\right) {dx} = {\int }_{\pi /4}^{\pi /2}\log \left( {\sin x}\right) {dx}.
\]

L’assertion (*) s’écrit donc \( I = \frac{\pi \log 2}{2} + {2I} \) , donc finalement \( I = - \frac{\pi \log 2}{2} \) .

> Assertion (*) is therefore written as \( I = \frac{\pi \log 2}{2} + {2I} \), so finally \( I = - \frac{\pi \log 2}{2} \).

Remarque. On peut aussi calculer \( I \) en l’écrivant sous la forme \( I = \frac{1}{2}{\int }_{0}^{\pi /2}\log \left( {1 - {\cos }^{2}x}\right) {dx} \) et en développant le logarithme en série au voisinage de 1.

> Remark. One can also calculate \( I \) by writing it in the form \( I = \frac{1}{2}{\int }_{0}^{\pi /2}\log \left( {1 - {\cos }^{2}x}\right) {dx} \) and expanding the logarithm in a series near 1.

Problem 4. Pour tout \( a \in \rbrack - 1, + \infty \lbrack \) , calculer

> Problem 4. For all \( a \in \rbrack - 1, + \infty \lbrack \), calculate

\[
F\left( a\right)  = {\int }_{0}^{\pi /2}\frac{\log \left( {1 + a\cos x}\right) }{\cos x}{dx}.
\]

---

Solution. L'intégrande n'admet pas de primitive exprimable avec les fonctions usuelles. L'idée est de dériver \( F \) par rapport à \( a \) et de remarquer qu’ainsi, on se ramène à une intégrale que l’on sait calculer.

> Solution. The integrand does not admit an antiderivative expressible with standard functions. The idea is to differentiate \( F \) with respect to \( a \) and notice that, in doing so, we reduce it to an integral that we know how to calculate.

Lorsque \( a \in \rbrack - 1, + \infty \lbrack \) , l’intégrande est continue sur \( \lbrack 0,\pi /2\lbrack \) et elle est prolongeable par continuité en \( \pi /2 \) car au voisinage de ce point

> When \( a \in \rbrack - 1, + \infty \lbrack \) , the integrand is continuous on \( \lbrack 0,\pi /2\lbrack \) and can be extended by continuity at \( \pi /2 \) because in the neighborhood of this point

\[
\frac{\log \left( {1 + a\cos x}\right) }{\cos x} = \frac{a\cos x + o\left( {\cos x}\right) }{\cos x} = a + o\left( 1\right) .
\]

Ainsi prolongée, la fonction \( f : \left( {a, x}\right) \mapsto \log \left( {1 + a\cos x}\right) /\cos x \) admet une dérivée partielle par rapport à \( a \) qui est continue sur \( \rbrack - 1, + \infty \left\lbrack {\times \left\lbrack {0,\pi /2}\right\rbrack }\right. \) et qui vaut \( {\left( 1 + a\cos x\right) }^{-1} \) . Le théorème de dérivation sous le signe intégral permet donc d’affirmer que \( F \) est dérivable et que

> Thus extended, the function \( f : \left( {a, x}\right) \mapsto \log \left( {1 + a\cos x}\right) /\cos x \) admits a partial derivative with respect to \( a \) which is continuous on \( \rbrack - 1, + \infty \left\lbrack {\times \left\lbrack {0,\pi /2}\right\rbrack }\right. \) and which equals \( {\left( 1 + a\cos x\right) }^{-1} \) . The theorem of differentiation under the integral sign therefore allows us to state that \( F \) is differentiable and that

\[
\forall a >  - 1,\;{F}^{\prime }\left( a\right)  = {\int }_{0}^{\pi /2}\frac{dx}{1 + a\cos x}.
\]

On calcule cette dernière intégrale en effectuant le changement de variable \( u = \tan \left( {t/2}\right) \) , ce qui donne

> We calculate this last integral by performing the change of variable \( u = \tan \left( {t/2}\right) \) , which gives

\[
\forall a >  - 1,\;{F}^{\prime }\left( a\right)  = 2{\int }_{0}^{1}\frac{du}{\left( {1 + a}\right)  + \left( {1 - a}\right) {u}^{2}}.
\]

On traite ensuite deux cas selon la position de \( a \) par rapport à 1 .

> We then consider two cases depending on the position of \( a \) relative to 1.

- Si \( a \in  \rbrack  - 1,1\left\lbrack  {\text{ , on peut écrire }a = \cos {2\theta }\text{ avec }\theta  \in  }\right\rbrack  0,\pi /2\lbrack \) . On a alors

> - If \( a \in  \rbrack  - 1,1\left\lbrack  {\text{ , on peut écrire }a = \cos {2\theta }\text{ avec }\theta  \in  }\right\rbrack  0,\pi /2\lbrack \). We then have

\[
{F}^{\prime }\left( a\right)  = {\int }_{0}^{1}\frac{du}{{\cos }^{2}\theta  + {u}^{2}{\sin }^{2}\theta } = \frac{1}{{\cos }^{2}\theta }{\int }_{0}^{1}\frac{du}{1 + {u}^{2}{\tan }^{2}\theta } = \frac{2}{\sin {2\theta }}{\int }_{0}^{\tan \theta }\frac{dv}{1 + {v}^{2}} = \frac{2\theta }{\sin {2\theta }},
\]

---

et finalement

> and finally

\[
\forall a \in  \rbrack  - 1,1\left\lbrack  {,\;{F}^{\prime }\left( a\right)  = \frac{\arccos a}{\sqrt{1 - {a}^{2}}}.}\right.
\]

(*)

> - Si \( a > 1 \) , on écrit \( a = \operatorname{ch}{2\theta } \) avec \( \theta  > 0 \) , de sorte que

- If \( a > 1 \), we write \( a = \operatorname{ch}{2\theta } \) with \( \theta  > 0 \), so that

\[
{F}^{\prime }\left( a\right)  = {\int }_{0}^{1}\frac{du}{{\operatorname{ch}}^{2}\theta  - {u}^{2}{\operatorname{sh}}^{2}\theta } = \frac{1}{{\operatorname{ch}}^{2}\theta }{\int }_{0}^{1}\frac{du}{1 - {u}^{2}{\operatorname{th}}^{2}\theta } = \frac{2}{\operatorname{sh}{2\theta }}{\int }_{0}^{\operatorname{th}\theta }\frac{dv}{1 + {v}^{2}} = \frac{2\theta }{\operatorname{sh}{2\theta }}.
\]

Donc

> Therefore

\[
\forall a > 1,\;{F}^{\prime }\left( a\right)  = \frac{\operatorname{argch}a}{\sqrt{{a}^{2} - 1}}.
\]

(**)

> Ceci étant, on tire grâce à (*) que pour \( a \in \rbrack - 1,1\lbrack \) ,

Given this, we deduce from (*) that for \( a \in \rbrack - 1,1\lbrack \),

\[
F\left( a\right)  = F\left( 0\right)  + {\int }_{0}^{a}{F}^{\prime }\left( x\right) {dx} = {\int }_{0}^{a}\frac{\arccos x}{\sqrt{1 - {x}^{2}}}{dx} = {\left\lbrack  -\frac{{\left( \arccos x\right) }^{2}}{2}\right\rbrack  }_{0}^{a} = \frac{{\pi }^{2}}{8} - \frac{{\left( \arccos a\right) }^{2}}{2}.
\]

La fonction \( F \) étant continue en \( a = 1 \) , cette expression permet de montrer que

> Since the function \( F \) is continuous at \( a = 1 \), this expression allows us to show that

\[
F\left( 1\right)  = \mathop{\lim }\limits_{{a \rightarrow  {1}^{ - }}}F\left( a\right)  = \frac{{\pi }^{2}}{8}.
\]

On a maintenant avec (**)

> We now have with (**)

\[
\forall a > 1,\;F\left( a\right)  = F\left( 1\right)  + {\int }_{1}^{a}\frac{\operatorname{argch}x}{\sqrt{{x}^{2} - 1}}{dx} = \frac{{\pi }^{2}}{8} + \frac{{\left( \operatorname{argch}a\right) }^{2}}{2}.
\]

Remarque. On peut également résoudre cet exercice en utilisant une inversion de som-mations dans les intégrales doubles. On écrit

> Remark. This exercise can also be solved by using an inversion of summations in double integrals. We write

\[
\frac{\log \left( {1 + a\cos x}\right) }{\cos x}{dx} = {\int }_{0}^{a}\frac{dt}{1 + t\cos x}\text{ donc }F\left( a\right)  = {\int }_{0}^{\pi /2}\left( {{\int }_{0}^{a}\frac{dt}{1 + t\cos x}}\right) {dx},
\]

puis on applique le théorème de Fubini qui nous autorise à inverser les sommations :

> then we apply Fubini's theorem, which allows us to invert the summations:

\[
F\left( a\right)  = {\int }_{0}^{a}\left( {{\int }_{0}^{\pi /2}\frac{dx}{1 + t\cos x}}\right) {dt}
\]

et on poursuit comme plus haut.

> and we proceed as above.

Ceci est un fait général : on peut prouver l'interversion de sommation dans les intégrales doubles grâce au théorème de dérivation sous le signe intégral. Considérons en effet une fonction continue \( f : \left\lbrack {a, b}\right\rbrack \times \left\lbrack {c, d}\right\rbrack \rightarrow \mathbb{R} \) . On définit l’application

> This is a general fact: one can prove the inversion of summation in double integrals using the theorem of differentiation under the integral sign. Indeed, consider a continuous function \( f : \left\lbrack {a, b}\right\rbrack \times \left\lbrack {c, d}\right\rbrack \rightarrow \mathbb{R} \). We define the mapping

\[
F : \left\lbrack  {c, d}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{a}^{b}\left( {{\int }_{c}^{x}f\left( {t, u}\right) {dt}}\right) {du}.
\]

En appliquant le théorème de dérivation sous le signe intégral, on voit que \( F \) est dérivable et que

> By applying the theorem of differentiation under the integral sign, we see that \( F \) is differentiable and that

\[
\forall x \in  \left\lbrack  {c, d}\right\rbrack  ,\;{F}^{\prime }\left( x\right)  = {\int }_{a}^{b}f\left( {x, u}\right) {du}.
\]

On en déduit

> We deduce from this

\[
{\int }_{a}^{b}\left( {{\int }_{c}^{d}f\left( {t, u}\right) {dt}}\right) {du} = F\left( d\right)  = F\left( c\right)  + {\int }_{c}^{d}{F}^{\prime }\left( x\right) {dx} = {\int }_{c}^{d}\left( {{\int }_{a}^{b}f\left( {x, u}\right) {du}}\right) {dx}.
\]

Problème 5. Soit \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une fonction de classe \( {\mathcal{C}}^{2} \) , nulle en 0 . On pose

> Problem 5. Let \( f : \left\lbrack {0, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a function of class \( {\mathcal{C}}^{2} \), equal to 0 at 0. We define

\[
{I}_{0} = {\int }_{0}^{+\infty }f{\left( x\right) }^{2}{dx},\;{I}_{1} = {\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx},\;\text{ et }\;{I}_{2} = {\int }_{0}^{+\infty }{f}^{\prime \prime }{\left( x\right) }^{2}{dx}.
\]

Montrer que si \( {f}^{2} \) et \( {\left( {f}^{\prime \prime }\right) }^{2} \) sont intégrables sur \( {\mathbb{R}}^{ + } \) , alors \( {\left( {f}^{\prime }\right) }^{2} \) également et \( {I}_{1}^{2} \leq {I}_{0}{I}_{2} \) .

> Show that if \( {f}^{2} \) and \( {\left( {f}^{\prime \prime }\right) }^{2} \) are integrable on \( {\mathbb{R}}^{ + } \), then \( {\left( {f}^{\prime }\right) }^{2} \) is also integrable and \( {I}_{1}^{2} \leq {I}_{0}{I}_{2} \).

Solution. Nous allons utiliser l'inégalité de Schwarz. Commençons par montrer la convergence de l’intégrale \( {I}_{1} \) . On intègre par parties, en écrivant, pour tout \( X > 0 \) ,

> Solution. We will use the Schwarz inequality. Let us begin by showing the convergence of the integral \( {I}_{1} \). We integrate by parts, writing, for all \( X > 0 \),

\[
{\int }_{0}^{X}{f}^{\prime }{\left( x\right) }^{2}{dx} = {\left\lbrack  f\left( x\right) {f}^{\prime }\left( x\right) \right\rbrack  }_{0}^{X} - {\int }_{0}^{X}f\left( x\right) {f}^{\prime \prime }\left( x\right) {dx} = f\left( X\right) {f}^{\prime }\left( X\right)  - {\int }_{0}^{X}f\left( x\right) {f}^{\prime \prime }\left( x\right) {dx}.
\]

(*)

> L’inégalité de Schwarz nous assure que la fonction \( f{f}^{\prime \prime } \) est intégrable sur \( {\mathbb{R}}^{ + } \) et que de plus

The Schwarz inequality ensures that the function \( f{f}^{\prime \prime } \) is integrable on \( {\mathbb{R}}^{ + } \) and that, moreover,

\[
{\int }_{0}^{+\infty }\left| {f\left( x\right) {f}^{\prime \prime }\left( x\right) }\right| {dx} \leq  {\left( {\int }_{0}^{+\infty }f{\left( x\right) }^{2}dx\right) }^{1/2} \cdot  {\left( {\int }_{0}^{+\infty }{f}^{\prime \prime }{\left( x\right) }^{2}dx\right) }^{1/2} = {I}_{0}^{1/2}{I}_{2}^{1/2}.
\]

\( \left( {* * }\right) \)

> L’égalité (*) entraîne donc le fait que \( {\int }_{0}^{X}{f}^{\prime }{\left( x\right) }^{2}{dx} - f\left( X\right) {f}^{\prime }\left( X\right) \) converge lorsque \( X \rightarrow + \infty \) . Si l’intégrale \( {\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx} \) diverge, alors \( f\left( X\right) {f}^{\prime }\left( X\right) \rightarrow + \infty \) lorsque \( X \rightarrow + \infty \) , donc \( {f}^{2}\left( X\right) = \; 2{\int }_{0}^{X}f\left( x\right) {f}^{\prime }\left( x\right) {dx} \) tend vers \( + \infty \) , ce qui est impossible car \( {f}^{2} \) est intégrable sur \( {\mathbb{R}}^{ + } \) par hypothèse. L’intégrale \( {\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx} \) converge donc, et alors (*) montre que \( f\left( X\right) {f}^{\prime }\left( X\right) \) converge lorsque \( X \rightarrow + \infty \) . Notons \( \ell = \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) {f}^{\prime }\left( x\right) \) . Si \( \ell \neq 0 \) , on a d’après le théorème 3 page 163 (dernière assertion de (i)),

Equality (*) therefore implies that \( {\int }_{0}^{X}{f}^{\prime }{\left( x\right) }^{2}{dx} - f\left( X\right) {f}^{\prime }\left( X\right) \) converges as \( X \rightarrow + \infty \). If the integral \( {\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx} \) diverges, then \( f\left( X\right) {f}^{\prime }\left( X\right) \rightarrow + \infty \) as \( X \rightarrow + \infty \), so \( {f}^{2}\left( X\right) = \; 2{\int }_{0}^{X}f\left( x\right) {f}^{\prime }\left( x\right) {dx} \) tends to \( + \infty \), which is impossible because \( {f}^{2} \) is integrable on \( {\mathbb{R}}^{ + } \) by hypothesis. The integral \( {\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx} \) therefore converges, and then (*) shows that \( f\left( X\right) {f}^{\prime }\left( X\right) \) converges as \( X \rightarrow + \infty \). Let \( \ell = \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) {f}^{\prime }\left( x\right) \). If \( \ell \neq 0 \), we have according to Theorem 3 on page 163 (last assertion of (i)),

\[
{f}^{2}\left( X\right)  = 2{\int }_{0}^{X}f\left( x\right) {f}^{\prime }\left( x\right) {dx} \sim  2\ell X\;\left( {X \rightarrow   + \infty }\right) ,
\]

ce qui est impossible car \( {f}^{2} \) est intégrable sur \( {\mathbb{R}}^{ + } \) .

> which is impossible because \( {f}^{2} \) is integrable on \( {\mathbb{R}}^{ + } \).

Finalement, on a \( f\left( X\right) {f}^{\prime }\left( X\right) \rightarrow 0 \) lorsque \( X \rightarrow + \infty \) . En faisant \( X \rightarrow + \infty \) dans (*), on obtient

> Finally, we have \( f\left( X\right) {f}^{\prime }\left( X\right) \rightarrow 0 \) as \( X \rightarrow + \infty \). By letting \( X \rightarrow + \infty \) in (*), we obtain

\[
{\int }_{0}^{+\infty }{f}^{\prime }{\left( x\right) }^{2}{dx} =  - {\int }_{0}^{+\infty }f\left( x\right) {f}^{\prime \prime }\left( x\right) {dx},
\]

d'où le résultat avec (**).

> whence the result with (**).

Problem 6. Soit une fonction \( f : \mathbb{R} \rightarrow \mathbb{R} \) continue et intégrable sur \( \mathbb{R} \) . On pose

> Problem 6. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a continuous and integrable function on \( \mathbb{R} \). We define

\[
I\left( a\right)  = {\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt}.
\]

a) Montrer que \( \mathop{\lim }\limits_{{a \rightarrow 0}}I\left( a\right) = 0 \) .

> a) Show that \( \mathop{\lim }\limits_{{a \rightarrow 0}}I\left( a\right) = 0 \).

b) Montrer l’existence et donner la valeur de \( \mathop{\lim }\limits_{{a \rightarrow + \infty }}I\left( a\right) \) .

> b) Show the existence and give the value of \( \mathop{\lim }\limits_{{a \rightarrow + \infty }}I\left( a\right) \).

Solution. a) On ne peut pas ici appliquer le théorème de convergence dominée car il est impossible d’obtenir une majoration du type \( \left| {f\left( {t + a}\right) - f\left( t\right) }\right| \leq \varphi \left( t\right) \) indépendamment de \( a \) . Pour contourner le problème, on se donne \( \varepsilon > 0 \) et on considère \( A > 0 \) tel que

> Solution. a) We cannot apply the dominated convergence theorem here because it is impossible to obtain a bound of the type \( \left| {f\left( {t + a}\right) - f\left( t\right) }\right| \leq \varphi \left( t\right) \) independently of \( a \). To circumvent the problem, we choose \( \varepsilon > 0 \) and consider \( A > 0 \) such that

\[
{\int }_{\left| t\right|  \geq  A}\left| {f\left( t\right) }\right| {dt} = {\int }_{-\infty }^{-A}\left| {f\left( t\right) }\right| {dt} + {\int }_{A}^{+\infty }\left| {f\left( t\right) }\right| {dt} < \varepsilon .
\]

On pose \( B = A + 1 \) . Pour tout nombre réel \( a \) tel que \( \left| a\right| < 1 \) , on a

> We define \( B = A + 1 \). For any real number \( a \) such that \( \left| a\right| < 1 \), we have

\[
{\int }_{\left| t\right|  \geq  B}\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt} \leq  {\int }_{\left| t\right|  \geq  B}\left| {f\left( {t + a}\right) }\right| {dt} + {\int }_{\left| t\right|  \geq  B}\left| {f\left( t\right) }\right| {dt}
\]

\[
= {\int }_{-\infty }^{-B + a}\left| {f\left( t\right) }\right| {dt} + {\int }_{B + a}^{+\infty }\left| {f\left( t\right) }\right| {dt} + {\int }_{\left| t\right|  \geq  B}\left| {f\left( t\right) }\right| {dt} \leq  \varepsilon  + \varepsilon  = {2\varepsilon }
\]

car \( - B + a < - A \) et \( B + a > A \) . Ceci entraîne

> because \( - B + a < - A \) and \( B + a > A \). This implies

\[
I\left( a\right)  = {\int }_{\left| t\right|  \leq  B}\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt} + {\int }_{\left| t\right|  \geq  B}\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt} \leq  {\int }_{-B}^{B}\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt} + {2\varepsilon }.
\]

(*)

> Lorsque \( a \rightarrow 0 \) , l’intégrale \( {\int }_{-B}^{B}\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} \) tend vers 0 car le domaine d’intégration est un segment de \( \mathbb{R} \) et la fonction \( \left| {f\left( {t + a}\right) - f\left( t\right) }\right| \) est continue par rapport à \( a \) et nulle lorsque \( a = 0 \) . Ainsi

When \( a \rightarrow 0 \) , the integral \( {\int }_{-B}^{B}\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} \) tends to 0 because the domain of integration is a segment of \( \mathbb{R} \) and the function \( \left| {f\left( {t + a}\right) - f\left( t\right) }\right| \) is continuous with respect to \( a \) and zero when \( a = 0 \) . Thus

\[
\exists \alpha  > 0,\left( {\alpha  < 1}\right) ,\forall a \in  \left\lbrack  {-\alpha ,\alpha }\right\rbrack  ,\;{\int }_{-B}^{B}\left| {f\left( {t + a}\right)  - f\left( t\right) }\right| {dt} < \varepsilon .
\]

Avec l’inégalité (*) ceci entraîne \( \forall a \in \left\lbrack {-\alpha ,\alpha }\right\rbrack ,\;{\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} \leq {3\varepsilon } \) , d’où le résultat.

> With inequality (*) this leads to \( \forall a \in \left\lbrack {-\alpha ,\alpha }\right\rbrack ,\;{\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} \leq {3\varepsilon } \) , hence the result.

b) Lorsque \( f \) est une fonction à support compact (i. e. nulle en dehors d’un compact) on voit facilement que la limite recherchée existe et vaut \( 2{\int }_{-\infty }^{+\infty }\left| {f\left( t\right) }\right| {dt} \) . C’est ce que nous allons prouver dans le cas général.

> b) When \( f \) is a function with compact support (i. e. zero outside a compact set) it is easy to see that the sought limit exists and equals \( 2{\int }_{-\infty }^{+\infty }\left| {f\left( t\right) }\right| {dt} \) . This is what we will prove in the general case.

On commence par symétriser le problème. Le changement de variable \( u = t + a/2 \) montre que \( {\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} = {\int }_{-\infty }^{+\infty }\left| {f\left( {u + \frac{a}{2}}\right) - f\left( {u - \frac{a}{2}}\right) }\right| {du} \) Ainsi, on est ramené à prouver l'existence et donner la valeur de

> We begin by symmetrizing the problem. The change of variable \( u = t + a/2 \) shows that \( {\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right) - f\left( t\right) }\right| {dt} = {\int }_{-\infty }^{+\infty }\left| {f\left( {u + \frac{a}{2}}\right) - f\left( {u - \frac{a}{2}}\right) }\right| {du} \) Thus, we are reduced to proving the existence and giving the value of

\[
\mathop{\lim }\limits_{{a \rightarrow   + \infty }}{\int }_{-\infty }^{+\infty }\left| {f\left( {t + a}\right)  - f\left( {t - a}\right) }\right| {dt}
\]

\( \left( {* * }\right) \)

> On note \( {f}_{a} \) la fonction \( t \mapsto f\left( {t + a}\right) \) . On va montrer que la contribution de l’intégrale précédente pour \( t \geq 0 \) converge vers \( {\int }_{\mathbb{R}}\left| f\right| \) . On écrit, pour \( a > 0 \) ,

Let \( {f}_{a} \) be the function \( t \mapsto f\left( {t + a}\right) \) . We will show that the contribution of the previous integral for \( t \geq 0 \) converges to \( {\int }_{\mathbb{R}}\left| f\right| \) . We write, for \( a > 0 \) ,

\[
{\int }_{{\mathbb{R}}^{ + }}\left| {{f}_{a} - {f}_{-a}}\right|  - {\int }_{\mathbb{R}}\left| f\right|  = {\int }_{{\mathbb{R}}^{ + }}\left| {{f}_{a} - {f}_{-a}}\right|  - {\int }_{\mathbb{R}}\left| {f}_{-a}\right|  = {\int }_{{\mathbb{R}}^{ + }}\left( {\left| {{f}_{a} - {f}_{-a}}\right|  - \left| {f}_{-a}\right| }\right)  + {\int }_{{\mathbb{R}}^{ - }}\left| {f}_{-a}\right| .
\]

Avec l’inégalité \( \left| {\left| {{f}_{a} - {f}_{-a}}\right| - \left| {f}_{-a}\right| }\right| \leq \left| {f}_{a}\right| \) on en déduit

> With inequality \( \left| {\left| {{f}_{a} - {f}_{-a}}\right| - \left| {f}_{-a}\right| }\right| \leq \left| {f}_{a}\right| \) we deduce

\[
\left| {{\int }_{{\mathbb{R}}^{ + }}\left| {{f}_{a} - {f}_{-a}}\right|  - {\int }_{\mathbb{R}}\left| f\right| }\right|  \leq  {\int }_{{\mathbb{R}}^{ + }}\left| {f}_{a}\right|  + {\int }_{{\mathbb{R}}^{ - }}\left| {f}_{-a}\right|  = {\int }_{\left| t\right|  \geq  a}\left| {f\left( t\right) }\right| {dt}.
\]

Comme \( f \) est intégrable sur \( \mathbb{R} \) , ceci entraîne que \( {\int }_{{\mathbb{R}}^{ + }}\left| {{f}_{a} - {f}_{-a}}\right| \) converge vers \( {\int }_{\mathbb{R}}\left| f\right| \) . On montrerait de même que \( {\int }_{{\mathbb{R}}^{ - }}\left| {{f}_{a} - {f}_{-a}}\right| \) converge vers \( {\int }_{\mathbb{R}}\left| f\right| \) , et par sommation on a finalement démontré que (**) converge vers \( 2{\int }_{\mathbb{R}}\left| f\right| \) lorsque \( a \rightarrow + \infty \) .

> Since \( f \) is integrable on \( \mathbb{R} \) , this implies that \( {\int }_{{\mathbb{R}}^{ + }}\left| {{f}_{a} - {f}_{-a}}\right| \) converges to \( {\int }_{\mathbb{R}}\left| f\right| \) . We would show similarly that \( {\int }_{{\mathbb{R}}^{ - }}\left| {{f}_{a} - {f}_{-a}}\right| \) converges to \( {\int }_{\mathbb{R}}\left| f\right| \) , and by summation we have finally demonstrated that (**) converges to \( 2{\int }_{\mathbb{R}}\left| f\right| \) when \( a \rightarrow + \infty \) .

Problem 7. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) , intégrable sur \( {\mathbb{R}}^{ + } \) , telle que \( {\left( {f}^{\prime }\right) }^{2} \) est intégrable sur \( {\mathbb{R}}^{ + } \) . Montrer que \( f \) est bornée sur \( {\mathbb{R}}^{ + } \) .

> Problem 7. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{1} \) , integrable on \( {\mathbb{R}}^{ + } \) , such that \( {\left( {f}^{\prime }\right) }^{2} \) is integrable on \( {\mathbb{R}}^{ + } \) . Show that \( f \) is bounded on \( {\mathbb{R}}^{ + } \) .

Solution. Nous allons montrer que \( f \) tend vers 0 en \( + \infty \) , ce qui montrera le résultat. D’après le théorème 4 page 152, comme \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converge, il suffit de montrer que \( f \) est uniformément continue sur \( {\mathbb{R}}^{ + } \) .

> Solution. We will show that \( f \) tends to 0 as \( + \infty \) , which will prove the result. According to theorem 4 on page 152, since \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converges, it suffices to show that \( f \) is uniformly continuous on \( {\mathbb{R}}^{ + } \) .

Soient deux nombres réels \( x \) et \( y \) tels que \( 0 \leq x < y \) . L’inégalité de Schwarz entraîne

> Let two real numbers \( x \) and \( y \) be such that \( 0 \leq x < y \) . The Schwarz inequality implies

\[
\left| {f\left( y\right)  - f\left( x\right) }\right|  = \left| {{\int }_{x}^{y}{f}^{\prime }\left( t\right) {dt}}\right|  \leq  {\left( {\int }_{x}^{y}{\left( {f}^{\prime }\left( t\right) \right) }^{2}dt\right) }^{1/2} \cdot  {\left( {\int }_{x}^{y}1dt\right) }^{1/2} \leq  \left( {{\int }_{{\mathbb{R}}^{ + }}{\left( {f}^{\prime }\right) }^{2}}\right) \sqrt{y - x}.
\]

Ceci entraîne que \( f \) est uniformément continue sur \( {\mathbb{R}}^{ + } \) , d’où le résultat.

> This implies that \( f \) is uniformly continuous on \( {\mathbb{R}}^{ + } \) , hence the result.

Problem 8. Soit \( f : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une fonction continue et croissante. On suppose que la fonction

> Problem 8. Let \( f : \left\lbrack {1, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a continuous and increasing function. Suppose that the function

\[
F : \left\lbrack  {1, + \infty \left\lbrack  { \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{1}^{x}\frac{f\left( t\right) }{t}{dt}}\right. }\right.
\]

vérifie \( F\left( x\right) \sim x \) lorsque \( x \rightarrow + \infty \) . Montrer que \( f\left( x\right) \sim x \) lorsque \( x \rightarrow + \infty \) .

> satisfies \( F\left( x\right) \sim x \) as \( x \rightarrow + \infty \) . Show that \( f\left( x\right) \sim x \) as \( x \rightarrow + \infty \) .

Solution. Soit \( \delta \in \rbrack 0,1\lbrack \) . D’après les hypothèses,

> Solution. Let \( \delta \in \rbrack 0,1\lbrack \) . According to the hypotheses,

\[
\exists {x}_{0} > 1,\forall x \geq  {x}_{0},\;\left( {1 - \delta }\right) x \leq  {\int }_{1}^{x}\frac{f\left( t\right) }{t}{dt} \leq  \left( {1 + \delta }\right) x.
\]

Ceci entraîne pour tout \( \varepsilon \in \rbrack 0,1\lbrack \)

> This implies for all \( \varepsilon \in \rbrack 0,1\lbrack \)

\[
\forall x \geq  {x}_{1},\;{\int }_{x}^{x + {\varepsilon x}}\frac{f\left( t\right) }{t}{dt} \leq  \left( {1 + \delta }\right) \left( {1 + \varepsilon }\right) x - \left( {1 - \delta }\right) x = \left( {\varepsilon  + {2\delta } + {\delta \varepsilon }}\right) x,
\]

et comme \( f \) est croissante

> and since \( f \) is increasing

\[
\forall x \geq  {x}_{1},\;{\varepsilon x}\frac{f\left( x\right) }{x\left( {1 + \varepsilon }\right) } \leq  {\int }_{x}^{x + {\varepsilon x}}\frac{f\left( t\right) }{t}{dt} \leq  \left( {\varepsilon  + {2\delta } + {\delta \varepsilon }}\right) x\;\text{ donc }\;f\left( x\right)  \leq  \frac{\varepsilon  + {2\delta } + {\delta \varepsilon }}{\varepsilon }\left( {1 + \varepsilon }\right) x.
\]

En choisissant \( \varepsilon = \sqrt{\delta } \) , on en déduit

> By choosing \( \varepsilon = \sqrt{\delta } \) , we deduce

\[
\forall x \geq  {x}_{1},\;f\left( x\right)  \leq  \left( {1 + 2\sqrt{\delta } + \delta }\right) \left( {1 + \sqrt{\delta }}\right) x = {\left( 1 + \sqrt{\delta }\right) }^{3}x.
\]

En d'autres termes, nous venons de montrer

> In other words, we have just shown

\[
\forall \alpha  > 0,\exists {x}_{1} > 1,\forall x \geq  {x}_{1},\;f\left( x\right)  \leq  x\left( {1 + \alpha }\right) .
\]

On montrerait de même

> Similarly, one would show

\[
\forall \alpha  > 0,\exists {x}_{2} > 1,\forall x \geq  {x}_{2},\;f\left( x\right)  \geq  x\left( {1 - \alpha }\right) .
\]

On en déduit \( f\left( x\right) \sim x \) lorsque \( x \rightarrow + \infty \) .

> We deduce \( f\left( x\right) \sim x \) as \( x \rightarrow + \infty \) .

Problem 9. On désigne par \( E \) l’ensemble des fonctions continues sur \( \left\lbrack {0,1}\right\rbrack \) à valeurs dans \( {\mathbb{R}}^{+ * } \) . Pour tout \( f \in E \) , on note

> Problem 9. Let \( E \) denote the set of continuous functions on \( \left\lbrack {0,1}\right\rbrack \) with values in \( {\mathbb{R}}^{+ * } \) . For any \( f \in E \) , we denote

\[
I\left( f\right)  = \left( {{\int }_{0}^{1}f\left( t\right) {dt}}\right)  \cdot  \left( {{\int }_{0}^{1}\frac{dt}{f\left( t\right) }}\right)
\]

et on note \( \Gamma = I\left( E\right) = \{ I\left( f\right) , f \in E\} \) .

> and we denote \( \Gamma = I\left( E\right) = \{ I\left( f\right) , f \in E\} \) .

a) Déterminer \( m = \inf \Gamma \) . Pour quelles fonctions de \( E \) a-t-on \( I\left( f\right) = m \) ?

> a) Determine \( m = \inf \Gamma \) . For which functions in \( E \) do we have \( I\left( f\right) = m \) ?

b) Déterminer sup \( \Gamma \) .

> b) Determine sup \( \Gamma \) .

Solution. a) Soit \( f \in E \) . D’après l’inégalité de Schwarz

> Solution. a) Let \( f \in E \). According to the Schwarz inequality

\[
1 = {\left( {\int }_{0}^{1}\sqrt{f\left( t\right) }\frac{1}{\sqrt{f\left( t\right) }}dt\right) }^{2} \leq  \left( {{\int }_{0}^{1}f\left( t\right) {dt}}\right)  \cdot  \left( {{\int }_{0}^{1}\frac{dt}{f\left( t\right) }}\right)  = I\left( f\right) ,
\]

(*)

> ce qui montre que \( I\left( f\right) \geq 1 \) . L’image de la fonction constante égale à1par \( I \) est égal à1, on a donc \( m = 1 \) . Les fonctions \( f \) de \( E \) étant continues, l’inégalité de Schwarz (*) se produira si et seulement si \( \sqrt{f} \) et \( 1/\sqrt{f} \) sont proportionnelles, c’est-à-dire si et seulement si

which shows that \( I\left( f\right) \geq 1 \). The image of the constant function equal to 1 by \( I \) is equal to 1, so we have \( m = 1 \). Since the functions \( f \) of \( E \) are continuous, the Schwarz inequality (*) will hold if and only if \( \sqrt{f} \) and \( 1/\sqrt{f} \) are proportional, that is to say if and only if

\[
\exists \lambda  > 0,\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;\sqrt{f\left( x\right) } = \frac{\lambda }{\sqrt{f\left( x\right) }}\;\text{ ou encore }\;f\left( x\right)  = \lambda .
\]

Les fonctions \( f \) telles que \( I\left( f\right) = 1 \) sont donc les fonctions constantes de \( E \) .

> The functions \( f \) such that \( I\left( f\right) = 1 \) are therefore the constant functions of \( E \).

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , il est possible de construire une fonction \( {f}_{n} \) de \( E \) telle que

> b) For any \( n \in {\mathbb{N}}^{ * } \), it is possible to construct a function \( {f}_{n} \) of \( E \) such that

\[
\forall x \in  \left\lbrack  {0,\frac{1}{3}}\right\rbrack  ,\;f\left( x\right)  = 1\;\text{ et }\;\forall x \in  \left\lbrack  {\frac{2}{3},1}\right\rbrack  ,\;f\left( x\right)  = n
\]

(on peut prendre par exemple une fonction définie comme telle sur \( \left\lbrack {0,1/3}\right\rbrack \cup \left\lbrack {2/3,1}\right\rbrack \) et affine sur \( \left\lbrack {1/3,2/3}\right\rbrack ) \) . On a alors

> (one can take for example a function defined as such on \( \left\lbrack {0,1/3}\right\rbrack \cup \left\lbrack {2/3,1}\right\rbrack \) and affine on \( \left\lbrack {1/3,2/3}\right\rbrack ) \). We then have

\[
\forall n \in  {\mathbb{N}}^{ * },\;I\left( {f}_{n}\right)  \geq  \frac{n}{3} \cdot  \frac{1}{3} = \frac{n}{9},
\]

donc sup \( \Gamma = + \infty \) .

> therefore sup \( \Gamma = + \infty \).

Remarque. On peut également traiter la question a) en écrivant

> Remark. One can also treat question a) by writing

\[
{2I}\left( f\right)  = {\iint }_{{\left\lbrack  0,1\right\rbrack  }^{2}}\left( {\frac{f\left( x\right) }{f\left( y\right) } + \frac{f\left( y\right) }{f\left( x\right) }}\right) {dxdy}
\]

(on obtient cette expression en appliquant le théorème de Fubini) puis en remarquant que \( f\left( x\right) /f\left( y\right) + f\left( y\right) /f\left( x\right) \geq 2 \) (en posant \( \alpha = f\left( x\right) /f\left( y\right) \) , on a \( \alpha + 1/\alpha = 2 + {\left( \alpha - 1\right) }^{2}/\alpha \geq 2 \) ).

> (this expression is obtained by applying Fubini's theorem) then by noting that \( f\left( x\right) /f\left( y\right) + f\left( y\right) /f\left( x\right) \geq 2 \) (by setting \( \alpha = f\left( x\right) /f\left( y\right) \), we have \( \alpha + 1/\alpha = 2 + {\left( \alpha - 1\right) }^{2}/\alpha \geq 2 \)).

Problem 10. Pour tout \( \rho \in \mathbb{R} \smallsetminus \{ - 1,1\} \) , on pose

> Problem 10. For any \( \rho \in \mathbb{R} \smallsetminus \{ - 1,1\} \), we define

\[
I\left( \rho \right)  = {\int }_{0}^{\pi }\log \left( {1 - {2\rho }\cos \theta  + {\rho }^{2}}\right) {d\theta }.
\]

a) Comparer \( I\left( \rho \right) \) et \( I\left( {\rho }^{2}\right) \) . En déduire la valeur de \( I\left( \rho \right) \) .

> a) Compare \( I\left( \rho \right) \) and \( I\left( {\rho }^{2}\right) \). Deduce the value of \( I\left( \rho \right) \).

b) Retrouver la valeur de \( I\left( \rho \right) \) en utilisant les sommes de Riemann.

> b) Find the value of \( I\left( \rho \right) \) again using Riemann sums.

Solution. L’égalité \( 1 - {2\rho }\cos \theta + {\rho }^{2} = {\left( 1 - \rho \cos \theta \right) }^{2} + {\rho }^{2}{\sin }^{2}\theta = {\left| 1 - \rho {e}^{i\theta }\right| }^{2} \) montre que \( I\left( \rho \right) \) existe pour tout \( \rho \notin \{ - 1,1\} \) .

> Solution. The equality \( 1 - {2\rho }\cos \theta + {\rho }^{2} = {\left( 1 - \rho \cos \theta \right) }^{2} + {\rho }^{2}{\sin }^{2}\theta = {\left| 1 - \rho {e}^{i\theta }\right| }^{2} \) shows that \( I\left( \rho \right) \) exists for any \( \rho \notin \{ - 1,1\} \).

a) Le changement de variable \( \psi = \pi - \theta \) montre que la fonction \( \rho \mapsto I\left( \rho \right) \) est paire. Donc si \( \rho \notin \{ - 1,1\} \)

> a) The change of variable \( \psi = \pi - \theta \) shows that the function \( \rho \mapsto I\left( \rho \right) \) is even. So if \( \rho \notin \{ - 1,1\} \)

\[
{2I}\left( \rho \right)  = I\left( \rho \right)  + I\left( {-\rho }\right)  = {\int }_{0}^{\pi }\log \left( {{\left| 1 - \rho {e}^{i\theta }\right| }^{2}{\left| 1 + \rho {e}^{i\theta }\right| }^{2}}\right) {d\theta }.
\]

Comme \( \left( {1 - \rho {e}^{i\theta }}\right) \left( {1 + \rho {e}^{i\theta }}\right) = 1 - {\rho }^{2}{e}^{2i\theta } \) ceci entraîne

> Since \( \left( {1 - \rho {e}^{i\theta }}\right) \left( {1 + \rho {e}^{i\theta }}\right) = 1 - {\rho }^{2}{e}^{2i\theta } \) this implies

\[
{2I}\left( \rho \right)  = {\int }_{0}^{\pi }\log \left( {\left| 1 - {\rho }^{2}{e}^{2i\theta }\right| }^{2}\right) {d\theta } = \frac{1}{2}{\int }_{0}^{2\pi }\log \left( {\left| 1 - {\rho }^{2}{e}^{i\theta }\right| }^{2}\right) {d\theta }.
\]

Le changement de variable \( \varphi = \theta - \pi \) donne

> The change of variable \( \varphi = \theta - \pi \) gives

\[
{\int }_{\pi }^{2\pi }\log \left( {\left| 1 - {\rho }^{2}{e}^{i\theta }\right| }^{2}\right) {d\theta } = {\int }_{0}^{\pi }\log \left( \left| {1 + {\rho }^{2}{e}^{i\varphi }}\right| \right) {d\varphi } = I\left( {-{\rho }^{2}}\right)  = I\left( {\rho }^{2}\right) ,
\]

on a donc montré \( {2I}\left( \rho \right) = \frac{1}{2}\left( {I\left( {\rho }^{2}\right) + I\left( {\rho }^{2}\right) }\right) = I\left( {\rho }^{2}\right) \) . On en conclut facilement

> we have therefore shown \( {2I}\left( \rho \right) = \frac{1}{2}\left( {I\left( {\rho }^{2}\right) + I\left( {\rho }^{2}\right) }\right) = I\left( {\rho }^{2}\right) \). We easily conclude

\[
\forall n \in  {\mathbb{N}}^{ * },\;I\left( \rho \right)  = \frac{1}{{2}^{n}}I\left( {\rho }^{{2}^{n}}\right) .
\]

(*)

> - Si \( \left| \rho \right|  < 1 \) , la continuité de \( I \) en 0 entraîne \( I\left( \rho \right)  = 0 \) (il suffit de faire \( n \rightarrow   + \infty \) dans (*)).

- If \( \left| \rho \right|  < 1 \), the continuity of \( I \) at 0 implies \( I\left( \rho \right)  = 0 \) (it suffices to set \( n \rightarrow   + \infty \) in (*)).

> - Si \( \left| \rho \right|  > 1 \) , c’est un peu plus délicat. On commence par montrer \( I\left( \rho \right)  \sim  {2\pi }\log \rho \) lorsque \( \rho  \rightarrow   + \infty \) . On a

- If \( \left| \rho \right|  > 1 \), it is a bit more delicate. We start by showing \( I\left( \rho \right)  \sim  {2\pi }\log \rho \) when \( \rho  \rightarrow   + \infty \). We have

\[
\forall \theta  \in  \left\lbrack  {0,\pi }\right\rbrack  ,\;{\rho }^{2}\left( {1 - \frac{2}{\rho } + \frac{1}{{\rho }^{2}}}\right)  \leq  1 - {2\rho }\cos \theta  + {\rho }^{2} \leq  {\rho }^{2}\left( {1 + \frac{2}{\rho } + \frac{1}{{\rho }^{2}}}\right)
\]

donc par intégration

> thus by integration

\[
{2\pi }\log \rho  + \pi \log \left( {1 - \frac{2}{\rho } + \frac{1}{{\rho }^{2}}}\right)  \leq  I\left( \rho \right)  \leq  {2\pi }\log \rho  + \pi \log \left( {1 + \frac{2}{\rho } + \frac{1}{{\rho }^{2}}}\right) ,
\]

ce qui entraîne bien \( I\left( \rho \right) \sim {2\pi }\log \rho \) lorsque \( \rho \rightarrow + \infty \) . En particulier, si on fixe \( \rho > 1 \) , on a, lorsque l’entier \( n \) tend vers \( + \infty \)

> which indeed implies \( I\left( \rho \right) \sim {2\pi }\log \rho \) when \( \rho \rightarrow + \infty \). In particular, if we fix \( \rho > 1 \), we have, as the integer \( n \) tends to \( + \infty \)

\[
I\left( {\rho }^{{2}^{n}}\right)  \sim  {2}^{n + 1}\pi \log \rho
\]

et on en déduit en faisant tendre \( n \) vers l’infini dans (*) que \( I\left( \rho \right) = {2\pi }\log \rho \) . Si \( \rho < - 1 \) , on a \( I\left( \rho \right) = I\left( {-\rho }\right) \) . Finalement, on a montré

> and we deduce from this by letting \( n \) tend to infinity in (*) that \( I\left( \rho \right) = {2\pi }\log \rho \). If \( \rho < - 1 \), we have \( I\left( \rho \right) = I\left( {-\rho }\right) \). Finally, we have shown

\[
\forall \rho  \in  \mathbb{R},\left| \rho \right|  > 1,\;I\left( \rho \right)  = {2\pi }\log \left| \rho \right| .
\]

b) Soit \( \rho \in \mathbb{R} \smallsetminus \{ - 1,1\} \) . En appliquant le théorème sur les sommes de Riemann, on a

> b) Let \( \rho \in \mathbb{R} \smallsetminus \{ - 1,1\} \). By applying the theorem on Riemann sums, we have

\[
I\left( \rho \right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{u}_{n}\;\text{ avec }\;{u}_{n} = \frac{\pi }{n}\log \left\lbrack  {\mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 - {2\rho }\cos \left( \frac{k\pi }{n}\right)  + {\rho }^{2}}\right) }\right\rbrack  .
\]

Or

\[
\forall k \in  \mathbb{Z},\;{\rho }^{2} - {2\rho }\cos \left( \frac{k\pi }{n}\right)  + 1 = \left( {\rho  - {\omega }_{k}}\right) \left( {\rho  - {\omega }_{-k}}\right) ,\;\left( {{\omega }_{k} = {e}^{{ik\pi }/n}}\right) ,
\]

et comme \( \mathop{\prod }\limits_{{k = - n}}^{{n - 1}}\left( {X - {\omega }_{k}}\right) = {X}^{2n} - 1 \) (les \( {2n} \) nombres complexes \( {\omega }_{k} \) pour \( - n \leq k < n \) sont des racines distinctes du polynôme \( {X}^{2n} - 1 \) ), on en déduit

> and since \( \mathop{\prod }\limits_{{k = - n}}^{{n - 1}}\left( {X - {\omega }_{k}}\right) = {X}^{2n} - 1 \) (the \( {2n} \) complex numbers \( {\omega }_{k} \) for \( - n \leq k < n \) are distinct roots of the polynomial \( {X}^{2n} - 1 \)), we deduce

\[
\mathop{\prod }\limits_{{k = 1}}^{n}\left( {\rho  - {\omega }_{k}}\right) \left( {\rho  - {\omega }_{-k}}\right)  = \left( {\mathop{\prod }\limits_{{k =  - n}}^{{n - 1}}\left( {\rho  - {\omega }_{k}}\right) }\right) \frac{\rho  - {\omega }_{n}}{\rho  - {\omega }_{0}} = \left( {{\rho }^{2n} - 1}\right) \frac{\rho  + 1}{\rho  - 1}
\]

et donc

> and therefore

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \frac{\pi }{n}\log \left( \frac{\left( {{\rho }^{2n} - 1}\right) \left( {\rho  + 1}\right) }{\rho  - 1}\right) .
\]

(**)

> - Si \( \left| \rho \right|  < 1 \) , on a facilement lim \( {}_{n \rightarrow   + \infty }{u}_{n} = 0 \) d’après (**), donc \( I\left( \rho \right)  = 0 \) .

- If \( \left| \rho \right|  < 1 \), we easily have lim \( {}_{n \rightarrow   + \infty }{u}_{n} = 0 \) according to (**), so \( I\left( \rho \right)  = 0 \).

> - Si \( \left| \rho \right|  > 1 \) , on transforme (**) en

- If \( \left| \rho \right|  > 1 \), we transform (**) into

\[
{u}_{n} = {2\pi }\log \left| \rho \right|  + \frac{\pi }{n}\log \left( {\frac{\rho  + 1}{\rho  - 1}\left( {1 - \frac{1}{{\rho }^{2n}}}\right) }\right) ,
\]

ce qui entraîne \( I\left( \rho \right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} = {2\pi }\log \left| \rho \right| \) .

> which implies \( I\left( \rho \right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} = {2\pi }\log \left| \rho \right| \).

Remarque. On peut montrer que les intégrales \( I\left( 1\right) \) et \( I\left( {-1}\right) \) existent et qu’elles sont nulles.

> Remark. One can show that the integrals \( I\left( 1\right) \) and \( I\left( {-1}\right) \) exist and are equal to zero.

Problem 11. a) Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue par morceaux. Montrer que

> Problem 11. a) Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a piecewise continuous function. Show that

\[
\mathop{\lim }\limits_{\substack{{q \rightarrow  1} \\  {q < 1} }}I\left( q\right)  = {\int }_{0}^{1}f\left( t\right) {dt}\;\text{ où }\;\forall q \in  \rbrack 0,1\lbrack ,\;I\left( q\right)  = \left( {1 - q}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{q}^{n}f\left( {q}^{n}\right) .
\]

b) En utilisant le résultat de la question précédente, calculer

> b) Using the result of the previous question, calculate

\[
{\int }_{0}^{1}\frac{t - 1}{\log t}{dt}
\]

Solution. a) Pour tout \( q \in \rbrack 0,1\lbrack , I\left( q\right) \) est bien définie car \( f \) est bornée et on peut écrire

> Solution. a) For all \( q \in \rbrack 0,1\lbrack , I\left( q\right) \) is well-defined because \( f \) is bounded and we can write

\[
I\left( q\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {{q}^{n} - {q}^{n + 1}}\right) f\left( {q}^{n}\right) .
\]

Cette expression peut s'apparenter à une somme de Riemann infinie pour la subdivision infinie \( 1, q,{q}^{2},\ldots ,{q}^{n},\ldots \) Le théorème 7 page 128 sur les sommes de Riemann ne s’applique que pour des subdivisions finies, nous allons donc nous y ramener. Soit \( \varepsilon > 0 \) On sait qu’il existe \( \alpha > 0 \) tel que pour toute subdivision \( \sigma : 0 = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = 1 \) de \( \left\lbrack {0,1}\right\rbrack \) vérifiant \( \left| \sigma \right| < \alpha \) , on ait

> This expression can be likened to an infinite Riemann sum for the infinite subdivision \( 1, q,{q}^{2},\ldots ,{q}^{n},\ldots \). Theorem 7 on page 128 regarding Riemann sums only applies to finite subdivisions, so we will reduce it to that case. Let \( \varepsilon > 0 \). We know there exists \( \alpha > 0 \) such that for any subdivision \( \sigma : 0 = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = 1 \) of \( \left\lbrack {0,1}\right\rbrack \) satisfying \( \left| \sigma \right| < \alpha \), we have

\[
\left| {\mathop{\sum }\limits_{{i = 1}}^{n}\left( {{x}_{i} - {x}_{i - 1}}\right) f\left( {x}_{i}\right)  - {\int }_{0}^{1}f\left( t\right) {dt}}\right|  < \varepsilon .
\]

Soit \( q \) tel que \( 1 - \alpha < q < 1 \) et \( N \in {\mathbb{N}}^{ * } \) tel que \( {q}^{N} < \alpha \) . Pour tout \( n \geq N \) , la subdivision

> Let \( q \) be such that \( 1 - \alpha < q < 1 \) and \( N \in {\mathbb{N}}^{ * } \) such that \( {q}^{N} < \alpha \) . For any \( n \geq N \) , the subdivision

\[
{\sigma }_{n} : 0 < {q}^{n} < {q}^{n - 1} < \cdots  < q < 1
\]

vérifie \( \left| {\sigma }_{n}\right| < \alpha \) (on a \( {q}^{i} - {q}^{i + 1} = {q}^{i}\left( {1 - q}\right) \leq 1 - q < \alpha \) pour tout \( i \) et \( {q}^{n} - 0 \leq {q}^{N} < \alpha \) ), donc

> satisfies \( \left| {\sigma }_{n}\right| < \alpha \) (we have \( {q}^{i} - {q}^{i + 1} = {q}^{i}\left( {1 - q}\right) \leq 1 - q < \alpha \) for all \( i \) and \( {q}^{n} - 0 \leq {q}^{N} < \alpha \) ), therefore

\[
\left| {\left( {1 - q}\right) f\left( 1\right)  + \left( {q - {q}^{2}}\right) f\left( q\right)  + \cdots  + \left( {{q}^{n - 1} - {q}^{n}}\right) f\left( {q}^{n - 1}\right)  + \left( {{q}^{n} - 0}\right) f\left( {q}^{n}\right)  - {\int }_{0}^{1}f\left( t\right) {dt}}\right|  < \varepsilon .
\]

Ceci est vrai pour tout \( n \geq N \) . En faisant tendre \( n \) vers \( + \infty \) , on en déduit

> This is true for all \( n \geq N \) . By letting \( n \) tend to \( + \infty \) , we deduce

\[
\left| {\mathop{\sum }\limits_{{i = 0}}^{{+\infty }}\left( {{q}^{i} - {q}^{i + 1}}\right) f\left( {q}^{i}\right)  - {\int }_{0}^{1}f\left( t\right) {dt}}\right|  \leq  \varepsilon .
\]

Ainsi, pour tout \( q \) vérifiant \( 1 - \alpha < q < 1 \) , on a \( \left| {I\left( q\right) - {\int }_{0}^{1}f\left( t\right) {dt}}\right| \leq \varepsilon \) . D’où le résultat. b) Ici, la valeur correspondante de \( I\left( q\right) \) pour la fonction intégrée est

> Thus, for all \( q \) satisfying \( 1 - \alpha < q < 1 \) , we have \( \left| {I\left( q\right) - {\int }_{0}^{1}f\left( t\right) {dt}}\right| \leq \varepsilon \) . Hence the result. b) Here, the corresponding value of \( I\left( q\right) \) for the integrated function is

\[
\forall q \in  \rbrack 0,1\lbrack ,\;I\left( q\right)  = \left( {1 - q}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{q}^{n}\frac{{q}^{n} - 1}{n\log q} = \frac{q - 1}{\log q}\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{q}^{n}}{n} - \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{q}^{2n}}{n}}\right) ,
\]

et le développement en série entière du logarithme fournit

> and the power series expansion of the logarithm provides

\[
\forall q \in  \rbrack 0,1\lbrack ,\;I\left( q\right)  = \frac{q - 1}{\log q}\left( {-\log \left( {1 - q}\right)  + \log \left( {1 - {q}^{2}}\right) }\right)  = \frac{q - 1}{\log q}\log \left( {1 + q}\right) .
\]

Comme \( \log q \sim q - 1 \) lorsque \( q \rightarrow 1 \) , cette formule entraîne \( \mathop{\lim }\limits_{{q \rightarrow {1}^{ - }}}I\left( q\right) = \log 2 \) , et finalement on a \( {\int }_{0}^{1}\left( {t - 1}\right) /\log {tdt} = \log 2 \) d’après la question précédente.

> Since \( \log q \sim q - 1 \) as \( q \rightarrow 1 \) , this formula leads to \( \mathop{\lim }\limits_{{q \rightarrow {1}^{ - }}}I\left( q\right) = \log 2 \) , and finally we have \( {\int }_{0}^{1}\left( {t - 1}\right) /\log {tdt} = \log 2 \) according to the previous question.

Remarque. La valeur de cette dernière intégrale est calculée avec une méthode différente dans le problème 2 page 177.

> Remark. The value of this last integral is calculated using a different method in problem 2 on page 177.

Problem 12 (PREUVE DU THÉORÉME DE D’ALEMBERT). 1/ Soit \( f : \mathbb{R} \rightarrow {\mathbb{C}}^{ * } \) une fonction de classe \( {\mathcal{C}}^{1} \) à valeurs complexes, \( {2\pi } \) -périodique et ne s’annulant pas. On définit

> Problem 12 (PROOF OF D’ALEMBERT’S THEOREM). 1/ Let \( f : \mathbb{R} \rightarrow {\mathbb{C}}^{ * } \) be a \( {\mathcal{C}}^{1} \) class function with complex values, \( {2\pi } \) -periodic and non-vanishing. We define

\[
I\left( f\right)  = \frac{1}{2i\pi }{\int }_{0}^{2\pi }\frac{{f}^{\prime }\left( \theta \right) }{f\left( \theta \right) }{d\theta }.
\]

En s’appuyant sur la fonction \( \varphi \left( t\right) = \exp \left( {{\int }_{0}^{t}\frac{{f}^{\prime }\left( \theta \right) }{f\left( \theta \right) }{d\theta }}\right) \) , montrer que \( I\left( f\right) \in \mathbb{Z} \) .

> By relying on the function \( \varphi \left( t\right) = \exp \left( {{\int }_{0}^{t}\frac{{f}^{\prime }\left( \theta \right) }{f\left( \theta \right) }{d\theta }}\right) \) , show that \( I\left( f\right) \in \mathbb{Z} \) .

2/ Soit \( P \) un polynôme complexe non constant. Pour tout \( r > 0 \) . On pose \( {f}_{P, r}\left( t\right) = P\left( {r{e}^{it}}\right) \) . a) (Théorème de d’Alembert). Pour \( P \) fixé, en étudiant la fonction \( r \mapsto I\left( {f}_{P, r}\right) \) pour \( r > 0 \) , prouver que \( P \) a au moins une racine complexe.

> 2/ Let \( P \) be a non-constant complex polynomial. For all \( r > 0 \) . Let \( {f}_{P, r}\left( t\right) = P\left( {r{e}^{it}}\right) \) . a) (D’Alembert’s Theorem). For a fixed \( P \) , by studying the function \( r \mapsto I\left( {f}_{P, r}\right) \) for \( r > 0 \) , prove that \( P \) has at least one complex root.

b) Calculer la valeur de \( I\left( {f}_{P, r}\right) \) en fonction de \( r \) et des zéros de \( P \) .

> b) Calculate the value of \( I\left( {f}_{P, r}\right) \) in terms of \( r \) and the zeros of \( P \) .

Solution. 1/ La fonction \( \varphi \) est de classe \( {\mathcal{C}}^{1} \) et elle vérifie \( {\varphi }^{\prime }\left( t\right) = \frac{{f}^{\prime }\left( t\right) }{f\left( t\right) }\varphi \left( t\right) \) , elle est donc solution de l’équation différentielle \( {y}^{\prime } - \frac{{f}^{\prime }}{f}y = 0 \) . Comme \( f \) est solution de cette équation différentielle et que l’espace de ses solutions est de dimension 1, il existe \( \lambda \in \mathbb{C} \) tel que \( \varphi = {\lambda f} \) . Comme \( f \) est \( {2\pi } \) - périodique c’est aussi le cas de \( \varphi \) , en particulier \( \varphi \left( {2\pi }\right) = \varphi \left( 0\right) \) ce qui entraîne \( {\int }_{0}^{2\pi }\frac{{f}^{\prime }\left( \theta \right) }{f\left( \theta \right) }{d\theta } \in {2i\pi }\mathbb{Z} \) donc \( I\left( f\right) \in \mathbb{Z} \) .

> Solution. 1/ The function \( \varphi \) is of class \( {\mathcal{C}}^{1} \) and satisfies \( {\varphi }^{\prime }\left( t\right) = \frac{{f}^{\prime }\left( t\right) }{f\left( t\right) }\varphi \left( t\right) \) , it is therefore a solution to the differential equation \( {y}^{\prime } - \frac{{f}^{\prime }}{f}y = 0 \) . Since \( f \) is a solution to this differential equation and the space of its solutions is of dimension 1, there exists \( \lambda \in \mathbb{C} \) such that \( \varphi = {\lambda f} \) . Since \( f \) is \( {2\pi } \) -periodic, the same applies to \( \varphi \) , in particular \( \varphi \left( {2\pi }\right) = \varphi \left( 0\right) \) which implies \( {\int }_{0}^{2\pi }\frac{{f}^{\prime }\left( \theta \right) }{f\left( \theta \right) }{d\theta } \in {2i\pi }\mathbb{Z} \) therefore \( I\left( f\right) \in \mathbb{Z} \) .

2/a) Raisonnons par l’absurde et supposons que \( P \) ne s’annule pas sur \( \mathbb{C} \) . Alors la fonction

> 2/a) Let us reason by contradiction and assume that \( P \) does not vanish on \( \mathbb{C} \) . Then the function

\[
g : {\mathbb{R}}^{ + } \rightarrow  \mathbb{C},\;r \mapsto  I\left( {f}_{P, r}\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }\frac{{P}^{\prime }\left( {r{e}^{i\theta }}\right) r{e}^{i\theta }}{P\left( {r{e}^{i\theta }}\right) }{d\theta }
\]

(*)

> est définie sur \( {\mathbb{R}}^{ + } \) tout entier. En vertu de la continuité de la fonction intégrée par rapport à \( r \) , le théorème de continuité sous le signe intégral montre que \( g \) est continue. Hors elle est à valeur dans \( \mathbb{Z} \) d’après le résultat de la question précédente, elle est donc constante. Comme \( g\left( 0\right) = 0 \) , on en déduit que \( g \) est identiquement nulle. Regardons maintenant ce qui se passe lorsque \( r \rightarrow + \infty \) . Soit \( n \) le degré de \( P \) et \( a \) son coefficient dominant. Lorsque \( \left| z\right| \rightarrow + \infty \) , on a \( P\left( z\right) \sim a{z}^{n} \) et \( {P}^{\prime }\left( z\right) \sim {na}{z}^{n - 1} \) , donc \( z{P}^{\prime }\left( z\right) /P\left( z\right) \) converge vers \( n \) . Ainsi, lorsque \( r \rightarrow + \infty \) , l’intégrande de (*) converge vers \( n \) . De plus cette intégrale est bornée indépendamment de \( r \) (car \( z{P}^{\prime }\left( z\right) /P\left( z\right) \) a une limite finie lorsque \( \left| z\right| \rightarrow + \infty \) , donc est bornée sur \( \mathbb{C} \) ), donc d’après le théorème de convergence dominée on a

is defined on the whole of \( {\mathbb{R}}^{ + } \) . By virtue of the continuity of the integrand with respect to \( r \) , the theorem of continuity under the integral sign shows that \( g \) is continuous. However, it takes values in \( \mathbb{Z} \) according to the result of the previous question, so it is constant. Since \( g\left( 0\right) = 0 \) , we deduce that \( g \) is identically zero. Let us now look at what happens when \( r \rightarrow + \infty \) . Let \( n \) be the degree of \( P \) and \( a \) its leading coefficient. When \( \left| z\right| \rightarrow + \infty \) , we have \( P\left( z\right) \sim a{z}^{n} \) and \( {P}^{\prime }\left( z\right) \sim {na}{z}^{n - 1} \) , so \( z{P}^{\prime }\left( z\right) /P\left( z\right) \) converges to \( n \) . Thus, when \( r \rightarrow + \infty \) , the integrand of (*) converges to \( n \) . Moreover, this integral is bounded independently of \( r \) (since \( z{P}^{\prime }\left( z\right) /P\left( z\right) \) has a finite limit when \( \left| z\right| \rightarrow + \infty \) , and is therefore bounded on \( \mathbb{C} \) ), so according to the dominated convergence theorem we have

\[
\mathop{\lim }\limits_{{r \rightarrow   + \infty }}g\left( r\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }\left( {\mathop{\lim }\limits_{{r \rightarrow   + \infty }}\frac{{P}^{\prime }\left( {r{e}^{i\theta }}\right) r{e}^{i\theta }}{P\left( {r{e}^{i\theta }}\right) }}\right) {d\theta } = n,
\]

ce qui est contradictoire avec le fait que \( g \) est identiquement nulle. Ainsi, le polynôme complexe \( P \) doit nécéssairement s’annuler sur \( \mathbb{C} \) .

> which contradicts the fact that \( g \) is identically zero. Thus, the complex polynomial \( P \) must necessarily vanish on \( \mathbb{C} \) .

b) Notons \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) les zéros de \( P \) ,éventuellement avec leur multiplicité, de sorte que \( P\left( z\right) = \; a\left( {z - {\alpha }_{1}}\right) \cdots \left( {z - {\alpha }_{n}}\right) \) . On a

> b) Let \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) denote the zeros of \( P \) , possibly with their multiplicity, such that \( P\left( z\right) = \; a\left( {z - {\alpha }_{1}}\right) \cdots \left( {z - {\alpha }_{n}}\right) \) . We have

\[
\frac{z{P}^{\prime }\left( z\right) }{P\left( z\right) } = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{z}{z - {\alpha }_{k}} = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{z{P}_{k}^{\prime }\left( z\right) }{{P}_{k}\left( z\right) },\;\text{ où }\;{P}_{k}\left( z\right)  = z - {\alpha }_{k}.
\]

\( \left( {* * }\right) \)

> Si aucune racine de \( P \) ne se trouve sur le cercle \( \left| z\right| = r \) , la valeur \( I\left( {f}_{P, r}\right) \) est bien définie et l’identité (**) montre que \( I\left( {f}_{P, r}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}I\left( {f}_{{P}_{k}, r}\right) \) . De la même manière que ce que l’on a vu pour \( P \) précédemment, pour tout \( k \) , la valeur \( r \mapsto I\left( {f}_{{P}_{k}, r}\right) \) est une fonction continue de \( r \) sur les intervalles où elle est définie, donc sur l’intervalle \( \left\lbrack {0,\left| {\alpha }_{k}\right| \left\lbrack \right. }\right. \) et sur l’intervalle \( \left. \right\rbrack \left| {\alpha }_{k}\right| , + \infty \lbrack \) . De plus elle est à valeur dans \( \mathbb{Z} \) , donc constante sur chacun de ces intervalles. En particulier, si \( r < \left| {\alpha }_{k}\right| \) on a \( I\left( {f}_{{P}_{k}, r}\right) = I\left( {f}_{{P}_{k},0}\right) = 0 \) , et si \( r > \left| {\alpha }_{k}\right| \) , alors de la même manière que précédemment on a \( I\left( {f}_{{P}_{k}, r}\right) = \mathop{\lim }\limits_{{t \rightarrow + \infty }}I\left( {f}_{{P}_{k}, t}\right) = \deg \left( {P}_{k}\right) = 1 \) . En conclusion, la valeur \( I\left( {f}_{P, r}\right) \) est définie lorsque qu’aucune des racines de \( P \) n’est sur le cercle \( \left| z\right| = r \) , et égale au nombre de racines de \( P \) (comptées avec leur ordre du multiplicité) dans le disque \( \left| z\right| < r \) .

If no root of \( P \) lies on the circle \( \left| z\right| = r \), the value \( I\left( {f}_{P, r}\right) \) is well-defined and the identity (**) shows that \( I\left( {f}_{P, r}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}I\left( {f}_{{P}_{k}, r}\right) \). In the same way as seen previously for \( P \), for any \( k \), the value \( r \mapsto I\left( {f}_{{P}_{k}, r}\right) \) is a continuous function of \( r \) on the intervals where it is defined, thus on the interval \( \left\lbrack {0,\left| {\alpha }_{k}\right| \left\lbrack \right. }\right. \) and on the interval \( \left. \right\rbrack \left| {\alpha }_{k}\right| , + \infty \lbrack \). Furthermore, it takes values in \( \mathbb{Z} \), and is therefore constant on each of these intervals. In particular, if \( r < \left| {\alpha }_{k}\right| \) we have \( I\left( {f}_{{P}_{k}, r}\right) = I\left( {f}_{{P}_{k},0}\right) = 0 \), and if \( r > \left| {\alpha }_{k}\right| \), then in the same way as before we have \( I\left( {f}_{{P}_{k}, r}\right) = \mathop{\lim }\limits_{{t \rightarrow + \infty }}I\left( {f}_{{P}_{k}, t}\right) = \deg \left( {P}_{k}\right) = 1 \). In conclusion, the value \( I\left( {f}_{P, r}\right) \) is defined when none of the roots of \( P \) are on the circle \( \left| z\right| = r \), and is equal to the number of roots of \( P \) (counted with their multiplicity) in the disk \( \left| z\right| < r \).

> Remarque. - La valeur \( I\left( f\right) \) est appelée indice de la courbe \( f \) sur \( \left\lbrack {0,{2\pi }}\right\rbrack \) . On peut montrer (c’est une conséquence du théorème du relèvement) qu’on peut écrire \( f\left( \theta \right) = \rho \left( \theta \right) {e}^{{i\varphi }\left( \theta \right) } \) , où \( \rho : \mathbb{R} \rightarrow {\mathbb{R}}^{+ * } \) et \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) sont de classe \( {\mathcal{C}}^{1} \) . On a \( \rho = \left| f\right| \) et \( \varphi \) représente l’argument de \( f \) obtenu par continuité. Comme \( f \) est \( {2\pi } \) -périodique, \( \varphi \left( 0\right) \equiv \varphi \left( {2\pi }\right) \left( {\;\operatorname{mod}\;{2\pi }}\right) \) donc \( \varphi \left( {2\pi }\right) - \varphi \left( 0\right) = {2k\pi } \) avec \( k \in \mathbb{Z} \) . On peut montrer facilement que \( k = I\left( f\right) \) ; ainsi \( I\left( f\right) \) représente le nombre de tours autour de 0, effectués dans le sens trigonométrique, que fait la courbe fermée \( f \) restreinte à \( \left\lbrack {0,{2\pi }}\right\rbrack \) .

Remark. - The value \( I\left( f\right) \) is called the index of the curve \( f \) with respect to \( \left\lbrack {0,{2\pi }}\right\rbrack \). It can be shown (as a consequence of the lifting theorem) that one can write \( f\left( \theta \right) = \rho \left( \theta \right) {e}^{{i\varphi }\left( \theta \right) } \), where \( \rho : \mathbb{R} \rightarrow {\mathbb{R}}^{+ * } \) and \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) are of class \( {\mathcal{C}}^{1} \). We have \( \rho = \left| f\right| \) and \( \varphi \) represents the argument of \( f \) obtained by continuity. Since \( f \) is \( {2\pi } \)-periodic, \( \varphi \left( 0\right) \equiv \varphi \left( {2\pi }\right) \left( {\;\operatorname{mod}\;{2\pi }}\right) \) thus \( \varphi \left( {2\pi }\right) - \varphi \left( 0\right) = {2k\pi } \) with \( k \in \mathbb{Z} \). It can be easily shown that \( k = I\left( f\right) \); thus \( I\left( f\right) \) represents the number of turns around 0, made in the counterclockwise direction, by the closed curve \( f \) restricted to \( \left\lbrack {0,{2\pi }}\right\rbrack \).

> - Le calcul de l’intégrale correspondant à \( I\left( {f}_{{P}_{k}, r}\right) \) peut aussi se faire directement,à partir d'une primitive de l'intégrande ou en la développant en série. La méthode que nous avons présentée est plus élégante dans le cadre du problème.

- The calculation of the integral corresponding to \( I\left( {f}_{{P}_{k}, r}\right) \) can also be done directly, using an antiderivative of the integrand or by expanding it into a series. The method we presented is more elegant in the context of the problem.

> - Deux autres preuves du théorème de d'Alembert (encore appelé théorème fondamental de l'algèbre) sont proposées dans le tome Algèbre.

- Two other proofs of d'Alembert's theorem (also called the fundamental theorem of algebra) are proposed in the Algebra volume.

> Problems 13. Déterminer les fonctions continues \( f : \mathbb{R} \rightarrow \mathbb{R} \) telles que, pour tout \( x \in \mathbb{R} \) , l’intégrale \( {\int }_{0}^{1}\frac{f\left( {x + t}\right) - f\left( x\right) }{{t}^{2}}{dt} \) converge.

Problems 13. Determine the continuous functions \( f : \mathbb{R} \rightarrow \mathbb{R} \) such that, for all \( x \in \mathbb{R} \), the integral \( {\int }_{0}^{1}\frac{f\left( {x + t}\right) - f\left( x\right) }{{t}^{2}}{dt} \) converges.

> Solution. Si \( f \) est dérivable sur \( \mathbb{R} \) , on a nécessairement \( {f}^{\prime }\left( x\right) = 0 \) pour tout \( x \in \mathbb{R} \) . En effet, s’il existe \( x \in \mathbb{R} \) tel que \( {f}^{\prime }\left( x\right) \neq 0 \) , l’équivalent \( \left( {f\left( {x + t}\right) - f\left( x\right) }\right) /{t}^{2}{ \sim }_{t \rightarrow 0}{f}^{\prime }\left( x\right) /t \) montre que cette fonction ne serait pas intégrable sur \( \left\lbrack {0,1}\right\rbrack \) , ce qui est contraire aux hypothèses. Ainsi, si \( f \) est dérivable, sa dérivée s’annule sur \( \mathbb{R} \) donc \( f \) est nécéssairement une fonction constante.

Solution. If \( f \) is differentiable on \( \mathbb{R} \), we necessarily have \( {f}^{\prime }\left( x\right) = 0 \) for all \( x \in \mathbb{R} \). Indeed, if there exists \( x \in \mathbb{R} \) such that \( {f}^{\prime }\left( x\right) \neq 0 \), the equivalent \( \left( {f\left( {x + t}\right) - f\left( x\right) }\right) /{t}^{2}{ \sim }_{t \rightarrow 0}{f}^{\prime }\left( x\right) /t \) shows that this function would not be integrable on \( \left\lbrack {0,1}\right\rbrack \), which contradicts the hypotheses. Thus, if \( f \) is differentiable, its derivative vanishes on \( \mathbb{R} \), so \( f \) is necessarily a constant function.

> Montrons que ce résultat reste vrai si \( f \) est seulement supposée continue. Pour cela raisonnons par l’absurde et supposons \( f \) non constante. L’idée est de déterminer un \( x \) tel que au voisinage de \( t = {0}^{ + } \) , on puisse écrire \( \left| {f\left( {x + t}\right) - f\left( x\right) }\right| \geq {\alpha t} \) avec \( \alpha > 0 \) . Comme \( f \) est non constante, il existe \( a, b \in \mathbb{R}, a < b \) , tels que \( f\left( a\right) \neq f\left( b\right) \) . Quitte à considérer la fonction \( f - f\left( a\right) \) , on peut supposer \( f\left( a\right) = 0 \) . Quitte à considérer \( - f \) , on peut supposer \( f\left( b\right) > 0 \) . Quitte à considérer \( t \mapsto f\left( {a + \left( {b - a}\right) t}\right) \) on peut supposer que \( a = 0 \) et \( b = 1 \) . En résumé, on peut supposer que \( 0 = f\left( 0\right) < f\left( 1\right) \) . Considérons la fonction \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto f\left( 1\right) /3 + {tf}\left( 1\right) /3 \) , et notons \( A = \{ t \in \left\lbrack {0,1}\right\rbrack \mid f\left( t\right) \leq \varphi \left( t\right) \} \) . L’ensemble \( A \) est non vide puisque \( 0 = f\left( 0\right) < \varphi \left( 0\right) = f\left( 1\right) /3 \) , donc \( 0 \in A \) . Par ailleurs \( 1 \notin A \) car \( f\left( 1\right) > \varphi \left( 1\right) = {2f}\left( 1\right) /3 \) . On peut donc définir \( c = \sup A \) , et on a \( c < 1 \) par continuité de \( f \) et \( \varphi \) . Comme \( A \) est fermé on a \( c \in A \) donc \( f\left( c\right) \leq \varphi \left( c\right) \) . Si on avait \( f\left( c\right) < \varphi \left( c\right) \) , alors par continuité de \( f \) et \( \varphi \) on pourrait trouver \( d \in \rbrack c,1\rbrack \) tel que \( f\left( d\right) < \varphi \left( d\right) \) , ce qui est en contradiction avec la définition de \( c \) . Donc \( f\left( c\right) = \varphi \left( c\right) \) . De plus, par définition de \( c \) on a \( f\left( t\right) > \varphi \left( t\right) \) pour tout \( t \in \rbrack c,1\rbrack \) . On en déduit que

Let us show that this result remains true if \( f \) is only assumed to be continuous. To do this, let us reason by contradiction and assume \( f \) is non-constant. The idea is to determine a \( x \) such that in the neighborhood of \( t = {0}^{ + } \), we can write \( \left| {f\left( {x + t}\right) - f\left( x\right) }\right| \geq {\alpha t} \) with \( \alpha > 0 \). Since \( f \) is non-constant, there exist \( a, b \in \mathbb{R}, a < b \) such that \( f\left( a\right) \neq f\left( b\right) \). By considering the function \( f - f\left( a\right) \), we can assume \( f\left( a\right) = 0 \). By considering \( - f \), we can assume \( f\left( b\right) > 0 \). By considering \( t \mapsto f\left( {a + \left( {b - a}\right) t}\right) \), we can assume that \( a = 0 \) and \( b = 1 \). In summary, we can assume that \( 0 = f\left( 0\right) < f\left( 1\right) \). Consider the function \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto f\left( 1\right) /3 + {tf}\left( 1\right) /3 \), and let \( A = \{ t \in \left\lbrack {0,1}\right\rbrack \mid f\left( t\right) \leq \varphi \left( t\right) \} \). The set \( A \) is non-empty since \( 0 = f\left( 0\right) < \varphi \left( 0\right) = f\left( 1\right) /3 \), so \( 0 \in A \). Furthermore, \( 1 \notin A \) because \( f\left( 1\right) > \varphi \left( 1\right) = {2f}\left( 1\right) /3 \). We can therefore define \( c = \sup A \), and we have \( c < 1 \) by continuity of \( f \) and \( \varphi \). Since \( A \) is closed, we have \( c \in A \), so \( f\left( c\right) \leq \varphi \left( c\right) \). If we had \( f\left( c\right) < \varphi \left( c\right) \), then by continuity of \( f \) and \( \varphi \), we could find \( d \in \rbrack c,1\rbrack \) such that \( f\left( d\right) < \varphi \left( d\right) \), which contradicts the definition of \( c \). Therefore, \( f\left( c\right) = \varphi \left( c\right) \). Moreover, by definition of \( c \), we have \( f\left( t\right) > \varphi \left( t\right) \) for all \( t \in \rbrack c,1\rbrack \). We deduce that

\[
\forall t \in  \rbrack c,1\rbrack ,\;f\left( t\right)  - f\left( c\right)  > \varphi \left( t\right)  - \varphi \left( c\right)  = \left( {t - c}\right) f\left( 1\right) /3.
\]

Ainsi on a \( \left\lbrack {f\left( {c + t}\right) - f\left( c\right) }\right\rbrack /{t}^{2} > \alpha /t \) pour \( t \in \rbrack 0,1 - c\rbrack \) avec \( \alpha = f\left( 1\right) /3 > 0 \) , donc l’intégrale \( {\int }_{0}^{1}\left\lbrack {f\left( {c + t}\right) - f\left( c\right) }\right\rbrack /{t}^{2}{dt} \) diverge. Ceci est contraire aux hypothèses, on en déduit que \( f \) est une fonction constante.

> Thus we have \( \left\lbrack {f\left( {c + t}\right) - f\left( c\right) }\right\rbrack /{t}^{2} > \alpha /t \) for \( t \in \rbrack 0,1 - c\rbrack \) with \( \alpha = f\left( 1\right) /3 > 0 \) , so the integral \( {\int }_{0}^{1}\left\lbrack {f\left( {c + t}\right) - f\left( c\right) }\right\rbrack /{t}^{2}{dt} \) diverges. This contradicts the hypotheses, we deduce that \( f \) is a constant function.

Réciproquement, il est évident que toute fonction constante \( f \) vérifie les propriétés de l'énoncé.

> Conversely, it is obvious that any constant function \( f \) satisfies the properties stated.

Problem 14. Soit \( f \) une application définie sur \( \left\lbrack {0,1}\right\rbrack \) ,à valeurs strictement positives, et continue. Calculer

> Problem 14. Let \( f \) be a mapping defined on \( \left\lbrack {0,1}\right\rbrack \) , with strictly positive values, and continuous. Calculate

\[
\mathop{\lim }\limits_{\substack{{\alpha  \rightarrow  0} \\  {\alpha  > 0} }}{\left( {\int }_{0}^{1}{f}^{\alpha }\left( t\right) dt\right) }^{1/\alpha }.
\]

Solution. On note

> Solution. Let us denote

\[
F : \left\lbrack  {0, + \infty \left\lbrack  { \rightarrow  \mathbb{R}\;\alpha  \mapsto  {\int }_{0}^{1}{f}^{\alpha }\left( t\right) {dt}.}\right. }\right.
\]

La fonction \( \varphi : {\mathbb{R}}^{ + } \times \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;\left( {\alpha , t}\right) \mapsto {f}^{\alpha }\left( t\right) \) est continue, dérivable par rapport à \( \alpha \) et

> The function \( \varphi : {\mathbb{R}}^{ + } \times \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;\left( {\alpha , t}\right) \mapsto {f}^{\alpha }\left( t\right) \) is continuous, differentiable with respect to \( \alpha \) and

\[
\forall \left( {\alpha , t}\right)  \in  {\mathbb{R}}^{ + } \times  \left\lbrack  {0,1}\right\rbrack  ,\;\frac{\partial \varphi }{\partial \alpha }\left( {\alpha , t}\right)  = \log f\left( t\right)  \cdot  {f}^{\alpha }\left( t\right)
\]

est continue sur \( {\mathbb{R}}^{ + } \times \left\lbrack {0,1}\right\rbrack \) . Donc \( F \) est dérivable sur \( {\mathbb{R}}^{ + } \) et

> is continuous on \( {\mathbb{R}}^{ + } \times \left\lbrack {0,1}\right\rbrack \) . Thus \( F \) is differentiable on \( {\mathbb{R}}^{ + } \) and

\[
\forall \alpha  \geq  0,\;{F}^{\prime }\left( \alpha \right)  = {\int }_{0}^{1}\log f\left( t\right)  \cdot  {f}^{\alpha }\left( t\right) {dt},\;\text{ en particulier }{F}^{\prime }\left( 0\right)  = {\int }_{0}^{1}\log f\left( t\right) {dt}.
\]

Or \( F\left( 0\right) = 1 \) , donc lorsque \( \alpha \rightarrow {0}^{ + } \) ,

> However \( F\left( 0\right) = 1 \) , so when \( \alpha \rightarrow {0}^{ + } \) ,

\[
F{\left( \alpha \right) }^{1/\alpha } = \exp \left( \frac{\log F\left( \alpha \right) }{\alpha }\right)  = \exp \left( \frac{\log \left( {1 + \alpha {F}^{\prime }\left( 0\right)  + o\left( \alpha \right) }\right) }{\alpha }\right)  = \exp \left( {{F}^{\prime }\left( 0\right)  + o\left( 1\right) }\right) .
\]

Finalement, la limite recherchée vaut

> Finally, the sought limit is equal to

\[
\exp \left( {{F}^{\prime }\left( 0\right) }\right)  = \exp \left( {{\int }_{0}^{1}\log f\left( t\right) {dt}}\right) .
\]

Remarque. On a déjà calculé la limite de la même fonction lorsque le paramètre \( \alpha \) tend vers \( + \infty \) (voir l’exercice 2 page 130).

> Remark. We have already calculated the limit of the same function when the parameter \( \alpha \) tends to \( + \infty \) (see exercise 2 page 130).

Problem 15 (IRRATIONALITÉ DE \( {\pi }^{2} \) ). a) Soit \( g : \mathbb{R} \rightarrow \mathbb{R} \) une fonction polynôme à coefficients entiers. On considère la fonction polynôme

> Problem 15 (IRRATIONALITY OF \( {\pi }^{2} \) ). a) Let \( g : \mathbb{R} \rightarrow \mathbb{R} \) be a polynomial function with integer coefficients. Consider the polynomial function

\[
h : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \frac{{x}^{n}g\left( x\right) }{n!}.
\]

Pour tout \( k \in \mathbb{N} \) , montrer que \( {h}^{\left( k\right) }\left( 0\right) \) est entier.

> For all \( k \in \mathbb{N} \) , show that \( {h}^{\left( k\right) }\left( 0\right) \) is an integer.

b) On suppose que \( {\pi }^{2} \) est rationnel, de sorte qu’il existe \( a, b \in {\mathbb{N}}^{ * } \) tel que \( {\pi }^{2} = a/b \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) on pose

> b) Suppose that \( {\pi }^{2} \) is rational, such that there exists \( a, b \in {\mathbb{N}}^{ * } \) where \( {\pi }^{2} = a/b \) . For all \( n \in {\mathbb{N}}^{ * } \) we define

\[
{I}_{n} = \pi {a}^{n}{\int }_{0}^{1}{f}_{n}\left( x\right) \sin \left( {\pi x}\right) {dx},\;\text{ où }\;{f}_{n}\left( x\right)  = \frac{{x}^{n}{\left( 1 - x\right) }^{n}}{n!}.
\]

Montrer que \( {I}_{n} \) est un entier. Conclure.

> Show that \( {I}_{n} \) is an integer. Conclude.

Solution. a) Écrivons \( g\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{p}{a}_{k}{x}^{k} \) . On a

> Solution. a) Let us write \( g\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{p}{a}_{k}{x}^{k} \) . We have

\[
h\left( x\right)  = \frac{1}{n!}\mathop{\sum }\limits_{{k = 0}}^{p}{a}_{k}{x}^{k + n},\;\left( {{a}_{k} \in  \mathbb{Z}}\right) .
\]

Donc

> Therefore

\[
\text{ - si }0 \leq  k \leq  n - 1,\;{h}^{\left( k\right) }\left( 0\right)  = 0 \in  \mathbb{Z}
\]

\[
{h}^{\left( k\right) }\left( 0\right)  = \frac{k!}{n!}{a}_{k - n} = k\left( {k - 1}\right) \cdots \left( {n + 1}\right) {a}_{k - n} \in  \mathbb{Z}
\]

b) En intégrant deux fois par parties, on trouve

> b) By integrating by parts twice, we find

\[
{\int }_{0}^{1}{f}_{n}\left( x\right) \sin \left( {\pi x}\right) {dx} = \frac{{f}_{n}\left( 1\right)  - {f}_{n}\left( 0\right) }{\pi } - \frac{1}{{\pi }^{2}}{\int }_{0}^{1}{f}_{n}^{\prime \prime }\left( x\right) \sin \left( {\pi x}\right) {dx},
\]

puis en itérant, on trouve

> then by iterating, we find

\[
{\int }_{0}^{1}{f}_{n}\left( x\right) \sin \left( {\pi x}\right) {dx} = \frac{{f}_{n}\left( 1\right)  - {f}_{n}\left( 0\right) }{\pi } - \frac{{f}_{n}^{\prime \prime }\left( 1\right)  - {f}_{n}^{\prime \prime }\left( 0\right) }{{\pi }^{3}} + \cdots
\]

\[
\cdots  + {\left( -1\right) }^{n}\frac{{f}_{n}^{\left( 2n\right) }\left( 1\right)  - {f}_{n}^{\left( 2n\right) }\left( 0\right) }{{\pi }^{{2n} + 1}} + {\left( -1\right) }^{n + 1}{\int }_{0}^{1}{f}_{n}^{\left( 2n + 2\right) }\left( x\right) \sin \left( {\pi x}\right) {dx}.
\]

Cette dernière intégrale est nulle car \( {f}_{n} \) est une fonction polynôme de degré \( {2n} \) , donc finalement

> This last integral is zero because \( {f}_{n} \) is a polynomial function of degree \( {2n} \) , so finally

\[
{I}_{n} = {a}^{n}\left( {{f}_{n}\left( 1\right)  - {f}_{n}\left( 0\right)  - \frac{{f}_{n}^{\prime \prime }\left( 1\right)  - {f}_{n}^{\prime \prime }\left( 0\right) }{{\pi }^{2}} + \cdots  + {\left( -1\right) }^{n}\frac{{f}_{n}^{\left( 2n\right) }\left( 1\right)  - {f}_{n}^{\left( 2n\right) }\left( 0\right) }{{\pi }^{2n}}}\right) .
\]

D’après le résultat de la question a), on a \( {f}_{n}^{\left( 2k\right) }\left( 0\right) \in \mathbb{Z} \) pour tout entier \( k \) , et comme \( {f}_{n}\left( {1 - x}\right) = \; {f}_{n}\left( x\right) \) on a aussi \( {f}_{n}^{\left( 2k\right) }\left( 1\right) \in \mathbb{Z} \) . Ceci entraîne, pour tout entier \( k,0 \leq k \leq n \)

> According to the result of question a), we have \( {f}_{n}^{\left( 2k\right) }\left( 0\right) \in \mathbb{Z} \) for every integer \( k \) , and since \( {f}_{n}\left( {1 - x}\right) = \; {f}_{n}\left( x\right) \) we also have \( {f}_{n}^{\left( 2k\right) }\left( 1\right) \in \mathbb{Z} \) . This implies, for every integer \( k,0 \leq k \leq n \)

\[
{a}^{n}\frac{{f}_{n}^{\left( 2k\right) }\left( 1\right)  - {f}_{n}^{\left( 2k\right) }\left( 0\right) }{{\pi }^{2k}} = {a}^{n}\frac{{b}^{k}}{{a}^{k}}\left( {{f}_{n}^{\left( 2k\right) }\left( 1\right)  - {f}_{n}^{\left( 2k\right) }\left( 0\right) }\right)  = {a}^{n - k}{b}^{k}\left( {{f}_{n}^{\left( 2k\right) }\left( 1\right)  - {f}_{n}^{\left( 2k\right) }\left( 0\right) }\right)  \in  \mathbb{Z}.
\]

Ainsi, \( {I}_{n} \in \mathbb{Z} \) . Or \( 0 < {I}_{n} < \pi {a}^{n}/n \) ! et comme \( {a}^{n}/n \) ! tend vers 0 lorsque \( n \rightarrow + \infty \) (c’est classique, on sait même que la série entière \( \sum {z}^{n}/n \) ! a un rayon de convergence infini), il existe un entier \( n \) pour lequel \( \pi {a}^{n}/n! < 1 \) . Ceci entraîne \( 0 < {I}_{n} < 1 \) , ce qui est impossible puisqu’on a montré que \( {I}_{n} \) était entier.

> Thus, \( {I}_{n} \in \mathbb{Z} \) . However \( 0 < {I}_{n} < \pi {a}^{n}/n \) ! and since \( {a}^{n}/n \) ! tends to 0 as \( n \rightarrow + \infty \) (this is standard, we even know that the power series \( \sum {z}^{n}/n \) ! has an infinite radius of convergence), there exists an integer \( n \) for which \( \pi {a}^{n}/n! < 1 \) . This implies \( 0 < {I}_{n} < 1 \) , which is impossible since we showed that \( {I}_{n} \) was an integer.

Le nombre réel \( {\pi }^{2} \) est donc irrationnel (ce qui entraîne que \( \pi \) est irrationnel).

> The real number \( {\pi }^{2} \) is therefore irrational (which implies that \( \pi \) is irrational).

Remarque. On peut montrer que \( \pi \) est transcendant (voir une preuve dans le tome Algèbre), mais c'est beaucoup plus difficile.

> Remark. One can show that \( \pi \) is transcendental (see a proof in the Algebra volume), but it is much more difficult.

Problem 16 (MOYENNE ARITHMÉTICO-GÉOMÉTRIQUE). Soient \( a, b \in \mathbb{R}, a, b > 0 \) .

> Problem 16 (ARITHMETIC-GEOMETRIC MEAN). Let \( a, b \in \mathbb{R}, a, b > 0 \) .

1 / On considère les deux suites \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) définies par

> 1 / Consider the two sequences \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) defined by

\[
{u}_{0} = a,{v}_{0} = b\;\text{ et }\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = \frac{{u}_{n} + {v}_{n}}{2},\;{v}_{n + 1} = \sqrt{{u}_{n}{v}_{n}}.
\]

Montrer que les suites \( \left( {u}_{n}\right) \) et \( \left( {b}_{n}\right) \) convergent vers la même limite.

> Show that the sequences \( \left( {u}_{n}\right) \) and \( \left( {b}_{n}\right) \) converge to the same limit.

2/a) On note \( M\left( {a, b}\right) \) la limite commune des ces deux suites (on l’appelle la moyenne arithmético-géométrique de a et b). Montrer que

> 2/a) Let \( M\left( {a, b}\right) \) be the common limit of these two sequences (it is called the arithmetic-geometric mean of a and b). Show that

\[
\frac{\pi }{2}\frac{1}{M\left( {a, b}\right) } = T\left( {a, b}\right) ,\;\text{ où }\;T\left( {a, b}\right)  = {\int }_{0}^{\pi /2}\frac{d\theta }{\sqrt{{a}^{2}{\cos }^{2}\theta  + {b}^{2}{\sin }^{2}\theta }}
\]

(*)

> (on pourra montrer que \( T\left( {a, b}\right) = T\left( {\left( {a + b}\right) /2,\sqrt{ab}}\right) \) en effectuant le changement de variable \( t = b\tan \theta \) puis le changement de variable \( u = \frac{1}{2}\left( {t - {ab}/t}\right) ) \) . b) (Constante de Gauss.) Montrer que

(one may show that \( T\left( {a, b}\right) = T\left( {\left( {a + b}\right) /2,\sqrt{ab}}\right) \) by performing the change of variable \( t = b\tan \theta \) then the change of variable \( u = \frac{1}{2}\left( {t - {ab}/t}\right) ) \) . b) (Gauss's constant.) Show that

\[
\frac{1}{M\left( {\sqrt{2},1}\right) } = \frac{2}{\pi }{\int }_{0}^{1}\frac{dt}{\sqrt{1 - {t}^{4}}}.
\]

Solution. 1/ Il est commode de supposer que \( a \geq b \) , on se ramène facilement à ce cas car les valeurs de \( {u}_{1} \) et \( {v}_{1} \) ne changent pas si on intervertit \( a \) et \( b \) . Une récurrence immédiate montre que toutes les valeurs des termes des suites \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) sont strictement positives. On remarque ensuite que \( {v}_{n} \leq {u}_{n} \) : pour \( n = 0 \) c’est vrai car \( a \geq b \) , et lorsque \( n \in {\mathbb{N}}^{ * } \) ceci découle de

> Solution. 1/ It is convenient to assume that \( a \geq b \) , we easily reduce to this case because the values of \( {u}_{1} \) and \( {v}_{1} \) do not change if we swap \( a \) and \( b \) . An immediate induction shows that all values of the terms of the sequences \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) are strictly positive. We then note that \( {v}_{n} \leq {u}_{n} \) : for \( n = 0 \) it is true because \( a \geq b \) , and when \( n \in {\mathbb{N}}^{ * } \) this follows from

\[
{u}_{n} - {v}_{n} = \frac{1}{2}\left( {{u}_{n - 1} - 2\sqrt{{u}_{n - 1}{v}_{n - 1}} + {v}_{n - 1}}\right)  = \frac{1}{2}{\left( \sqrt{{u}_{n - 1}} - \sqrt{{v}_{n - 1}}\right) }^{2} \geq  0.
\]

La suite \( \left( {u}_{n}\right) \) décroît, la suite \( \left( {v}_{n}\right) \) croît, car

> The sequence \( \left( {u}_{n}\right) \) decreases, the sequence \( \left( {v}_{n}\right) \) increases, because

\[
\forall n \in  \mathbb{N},\;{u}_{n + 1} - {u}_{n} = \frac{1}{2}\left( {{v}_{n} - {u}_{n}}\right)  \leq  0\;\text{ et }\;\frac{{v}_{n + 1}}{{v}_{n}} = \sqrt{\frac{{u}_{n}}{{v}_{n}}} \geq  1.
\]

Finalement, nous avons montré

> Finally, we have shown

\[
\forall n \in  \mathbb{N},\;{v}_{0} \leq  {v}_{1} \leq  \cdots  \leq  {v}_{n} \leq  {u}_{n} \leq  \cdots  \leq  {u}_{1} \leq  {u}_{0}.
\]

La suite décroissante \( \left( {u}_{n}\right) \) est minorée par l’un quelconque des termes de \( \left( {v}_{n}\right) \) , elle est donc convergente. De même, \( \left( {v}_{n}\right) \) est croissante et majorée par l’un quelconque des termes de \( \left( {u}_{n}\right) \) , donc convergente. Enfin, on montre facilement par récurrence que

> The decreasing sequence \( \left( {u}_{n}\right) \) is bounded below by any of the terms of \( \left( {v}_{n}\right) \), so it is convergent. Similarly, \( \left( {v}_{n}\right) \) is increasing and bounded above by any of the terms of \( \left( {u}_{n}\right) \), and therefore convergent. Finally, we easily show by induction that

\[
\forall n \in  \mathbb{N},\;0 \leq  {u}_{n} - {v}_{n} \leq  \left( {a - b}\right) /{2}^{n}.
\]

\( \left( {* * }\right) \)

> En effet, ceci est vrai pour \( n = 0 \) , et si on suppose la propriété vraie pour \( n \) on a

Indeed, this is true for \( n = 0 \), and if we assume the property is true for \( n \), we have

\[
{u}_{n + 1} - {v}_{n + 1} = \frac{1}{2}{\left( \sqrt{{u}_{n}} - \sqrt{{v}_{n}}\right) }^{2} = \frac{1}{2}\frac{{u}_{n} - {v}_{n}}{\sqrt{{u}_{n}} + \sqrt{{v}_{n}}}\left( {\sqrt{{u}_{n}} - \sqrt{{v}_{n}}}\right)  \leq  \frac{{u}_{n} - {v}_{n}}{2}.
\]

L’encadrement (**) prouve que les limites de \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) sont égales. Nous aurions pu montrer l’égalité des limites en procédant par continuité : en notant \( U \) et \( V \) les limites respectives de \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) , on a par continuité \( U = \left( {U + V}\right) /2 \) et \( V = \sqrt{UV} \) , donc \( U = V \) . Néanmoins (**) est plus intéréssant car il indique une convergence rapide \( \operatorname{de}\left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) vers leur limite commune. Notons que nous avons prouvé que \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) sont des suites adjacentes.

> The inequality (**) proves that the limits of \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) are equal. We could have shown the equality of the limits by proceeding via continuity: by denoting \( U \) and \( V \) as the respective limits of \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \), we have by continuity \( U = \left( {U + V}\right) /2 \) and \( V = \sqrt{UV} \), thus \( U = V \). Nevertheless, (**) is more interesting because it indicates rapid convergence of \( \operatorname{de}\left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) toward their common limit. Note that we have proven that \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) are adjacent sequences.

2/a) Comme indiqué, on effectue d’abord le changement de variable \( t = b\tan \theta \) . On obtient

> 2/a) As indicated, we first perform the change of variable \( t = b\tan \theta \). We obtain

\[
T\left( {a, b}\right)  = {\int }_{0}^{+\infty }\frac{dt}{\sqrt{\left( {{t}^{2} + {a}^{2}}\right) \left( {{t}^{2} + {b}^{2}}\right) }}.
\]

\( \left( {* * * }\right) \)

> On effectue maintenant le changement de variable \( u = \left( {t - {ab}/t}\right) /2 \) . Les calculs ne sont pas si faciles à obtenir. En notant \( c = \left( {a + b}\right) /2 \) et \( d = \sqrt{ab} \) , on écrit

We now perform the change of variable \( u = \left( {t - {ab}/t}\right) /2 \). The calculations are not so easy to obtain. By denoting \( c = \left( {a + b}\right) /2 \) and \( d = \sqrt{ab} \), we write

\[
{u}^{2} + {c}^{2} = \frac{{\left( {t}^{2} - ab\right) }^{2}}{4{t}^{2}} + \frac{{\left( a + b\right) }^{2}}{4} = \frac{{t}^{4} + \left( {{a}^{2} + {b}^{2}}\right) {t}^{2} + {a}^{2}{b}^{2}}{4{t}^{2}} = \frac{\left( {{t}^{2} + {a}^{2}}\right) \left( {{t}^{2} + {b}^{2}}\right) }{4{t}^{2}}
\]

\[
{u}^{2} + {d}^{2} = \frac{{\left( {t}^{2} - ab\right) }^{2}}{4{t}^{2}} + {\left( \sqrt{ab}\right) }^{2} = \frac{{t}^{4} + {2ab}{t}^{2} + {a}^{2}{b}^{2}}{4{t}^{2}} = \frac{{\left( {t}^{2} + ab\right) }^{2}}{4{t}^{2}}.
\]

Comme \( {du} = \left( {{t}^{2} + {ab}}\right) /\left( {2{t}^{2}}\right) {dt} \) , on en déduit

> Since \( {du} = \left( {{t}^{2} + {ab}}\right) /\left( {2{t}^{2}}\right) {dt} \), we deduce

\[
T\left( {c, d}\right)  = \frac{1}{2}{\int }_{-\infty }^{+\infty }\frac{du}{\sqrt{\left( {{u}^{2} + {c}^{2}}\right) \left( {{u}^{2} + {d}^{2}}\right) }} = \frac{1}{2}{\int }_{0}^{+\infty }\frac{4{t}^{2}}{\sqrt{\left( {{t}^{2} + {a}^{2}}\right) \left( {{t}^{2} + {b}^{2}}\right) }}\frac{1}{{t}^{2} + {ab}}\frac{{t}^{2} + {ab}}{2{t}^{2}}{dt},
\]

la première égalité provenant de la parité de la fonction intégrée. Dans la dernière intégrale, après simplification, on reconnait l’intégrande de l’intégrale (***), on en déduit \( T\left( {c, d}\right) = T\left( {a, b}\right) \) .

> the first equality coming from the parity of the integrated function. In the last integral, after simplification, we recognize the integrand of the integral (***), from which we deduce \( T\left( {c, d}\right) = T\left( {a, b}\right) \).

Prouvons maintenant l’identité (*). L’égalité \( T\left( {a, b}\right) = T\left( {\frac{a + b}{2},\sqrt{ab}}\right) \) , entraîne \( T\left( {{u}_{n},{v}_{n}}\right) = \; T\left( {{u}_{n + 1},{v}_{n + 1}}\right) \) pour tout \( n \in \mathbb{N} \) , donc \( T\left( {a, b}\right) = T\left( {{u}_{0},{v}_{0}}\right) = T\left( {{u}_{n},{v}_{n}}\right) \) pour tout \( n \in \mathbb{N} \) . La fonction \( T\left( {a, b}\right) \) est l’intégrale d’une fonction continue en \( \left( {a, b}\right) \) , intégrée sur le segment \( \left\lbrack {0,\pi /2}\right\rbrack \) , elle est donc continue en \( \left( {a, b}\right) \) . On peut maintenant passer à la limite dans l’égalité \( T\left( {a, b}\right) = \; T\left( {{u}_{n},{v}_{n}}\right) \) , ce qui donne \( T\left( {a, b}\right) = T\left( {M\left( {a, b}\right) , M\left( {a, b}\right) }\right) \) . On en déduit le résultat car

> Let us now prove the identity (*). The equality \( T\left( {a, b}\right) = T\left( {\frac{a + b}{2},\sqrt{ab}}\right) \) implies \( T\left( {{u}_{n},{v}_{n}}\right) = \; T\left( {{u}_{n + 1},{v}_{n + 1}}\right) \) for all \( n \in \mathbb{N} \), therefore \( T\left( {a, b}\right) = T\left( {{u}_{0},{v}_{0}}\right) = T\left( {{u}_{n},{v}_{n}}\right) \) for all \( n \in \mathbb{N} \). The function \( T\left( {a, b}\right) \) is the integral of a function continuous in \( \left( {a, b}\right) \), integrated over the segment \( \left\lbrack {0,\pi /2}\right\rbrack \), so it is continuous in \( \left( {a, b}\right) \). We can now take the limit in the equality \( T\left( {a, b}\right) = \; T\left( {{u}_{n},{v}_{n}}\right) \), which gives \( T\left( {a, b}\right) = T\left( {M\left( {a, b}\right) , M\left( {a, b}\right) }\right) \). We deduce the result because

\[
T\left( {M\left( {a, b}\right) , M\left( {a, b}\right) }\right)  = {\int }_{0}^{\pi /2}\frac{d\theta }{M\left( {a, b}\right) } = \frac{\pi }{2}\frac{1}{M\left( {a, b}\right) }.
\]

b) En effectuant le changement de variable \( t = \cos \theta \) , on obtient

> b) By performing the change of variable \( t = \cos \theta \) , we obtain

\[
{\int }_{0}^{1}\frac{dt}{\sqrt{1 - {t}^{4}}} = {\int }_{0}^{\pi /2}\frac{1}{\sqrt{1 + {\cos }^{2}\theta }}\frac{\sin {\theta d\theta }}{\sqrt{1 - {\cos }^{2}\theta }} = {\int }_{0}^{\pi /2}\frac{d\theta }{\sqrt{1 + {\cos }^{2}\theta }} = {\int }_{0}^{\pi /2}\frac{d\theta }{\sqrt{2{\cos }^{2}\theta  + {\sin }^{2}\theta }}.
\]

La dernière intégrale est \( T\left( {\sqrt{2},1}\right) \) , on en déduit le résultat grâce à l’identité (*).

> The last integral is \( T\left( {\sqrt{2},1}\right) \) , from which we deduce the result using identity (*).

Remarque. L'identité (*) a été prouvée par Gauss. L'intégrale de (*) se ramène à l'intégrale elliptique de première espèce \( K\left( k\right) = {\int }_{0}^{\pi /2}{\left( 1 - {k}^{2}{\sin }^{2}\theta \right) }^{-1/2}{d\theta } = T\left( {1,\sqrt{1 - {k}^{2}}}\right) \) .

> Remark. Identity (*) was proven by Gauss. The integral in (*) reduces to the elliptic integral of the first kind \( K\left( k\right) = {\int }_{0}^{\pi /2}{\left( 1 - {k}^{2}{\sin }^{2}\theta \right) }^{-1/2}{d\theta } = T\left( {1,\sqrt{1 - {k}^{2}}}\right) \) .

- La valeur \( G = 1/M\left( {\sqrt{2},1}\right) \) est appelée constante de Gauss. L’intégrale \( {\int }_{0}^{1}{dt}/\sqrt{1 - {t}^{4}} \) correspond à la longueur d'un arc de lemniscate qui est la courbe définie par l'équation \( {\left( {x}^{2} + {y}^{2}\right) }^{2} = {x}^{2} - {y}^{2} \) . Les suites \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) convergent très rapidement (la convergence est quadratique, dans le cas de \( a = \sqrt{2} \) et \( b = 1 \) on a \( \left| {M\left( {a, b}\right)  - {u}_{n}}\right|  \leq  {\left( \sqrt{2} - 1\right) }^{{2}^{n}} \) ), et Gauss calcula les premières valeurs de \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) pour obtenir 11 décimales de \( G \) .

> - The value \( G = 1/M\left( {\sqrt{2},1}\right) \) is called Gauss's constant. The integral \( {\int }_{0}^{1}{dt}/\sqrt{1 - {t}^{4}} \) corresponds to the arc length of a lemniscate, which is the curve defined by the equation \( {\left( {x}^{2} + {y}^{2}\right) }^{2} = {x}^{2} - {y}^{2} \) . The sequences \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) converge very rapidly (convergence is quadratic; in the case of \( a = \sqrt{2} \) and \( b = 1 \) we have \( \left| {M\left( {a, b}\right)  - {u}_{n}}\right|  \leq  {\left( \sqrt{2} - 1\right) }^{{2}^{n}} \) ), and Gauss calculated the first values of \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) to obtain 11 decimal places of \( G \) .

- Ces résultats obtenus par Gauss ont introduit la théorie des intégrales et des fonctions elliptiques, qui joue un rôle important en théorie des nombres.

> - These results obtained by Gauss introduced the theory of elliptic integrals and functions, which plays an important role in number theory.

Problems 17. On considère, pour \( \beta > 0 \) l’intégrale

> Problems 17. Consider, for \( \beta > 0 \) the integral

\[
{I}_{\beta }\left( x\right)  = {\int }_{0}^{+\infty }\frac{\cos \left( {xt}\right) }{1 + {t}^{2}}{e}^{-{\beta t}}{dt},\;x \in  \mathbb{R}.
\]

a) Montrer que la fonction \( x \mapsto {I}_{\beta }\left( x\right) \) est deux fois dérivable sur \( \mathbb{R} \) et qu’elle vérifie

> a) Show that the function \( x \mapsto {I}_{\beta }\left( x\right) \) is twice differentiable on \( \mathbb{R} \) and that it satisfies

\[
{I}_{\beta }\left( x\right)  - {I}_{\beta }^{\prime \prime }\left( x\right)  = \frac{\beta }{{\beta }^{2} + {x}^{2}}.
\]

b) Démontrer l'identité

> b) Prove the identity

\[
{I}_{\beta }\left( x\right)  = \frac{{e}^{x}{F}_{\beta }\left( x\right)  + {e}^{-x}{F}_{\beta }\left( {-x}\right) }{2},\;\text{ avec }\;{F}_{\beta }\left( x\right)  = {\int }_{x}^{+\infty }\frac{\beta {e}^{-t}}{{\beta }^{2} + {t}^{2}}{dt}.
\]

c) En déduire les valeurs

> c) Deduce the values

\[
C\left( x\right)  = {\int }_{0}^{+\infty }\frac{\cos \left( {xt}\right) }{1 + {t}^{2}}{dt} = \frac{\pi }{2}{e}^{-\left| x\right| },\;S\left( x\right)  = {\int }_{0}^{+\infty }\frac{t\sin \left( {xt}\right) }{1 + {t}^{2}}{dt} = \left\{  \begin{array}{ll} \frac{\pi }{2}{e}^{-x} & \left( {x > 0}\right) \\  0 & \left( {x = 0}\right) \\   - \frac{\pi }{2}{e}^{x} & \left( {x < 0}\right)  \end{array}\right.
\]

On montre de même que \( {I}_{\beta }^{\prime } \) est dérivable et que

> We show similarly that \( {I}_{\beta }^{\prime } \) is differentiable and that

\[
{I}_{\beta }^{\prime \prime }\left( x\right)  =  - {\int }_{0}^{+\infty }\frac{{t}^{2}\cos \left( {xt}\right) }{1 + {t}^{2}}{e}^{-{\beta t}}{dt}.
\]

---

Solution. a) \( {I}_{\beta }\left( x\right) \) est bien définie car son intégrande est majorée en valeur absolue par \( {e}^{-{\beta t}} \) , intégrable sur \( {\mathbb{R}}^{ + } \) . Notons \( f\left( {x, t}\right) \) l’intégrande de \( {I}_{\beta }\left( x\right) \) . Sa dérivée partielle par rapport à \( x \) est \( \partial f/\partial x = - t\sin \left( {xt}\right) /\left( {1 + {t}^{2}}\right) {e}^{-{\beta t}} \) , donc \( \left| {\partial f/\partial x}\right| \) est majorée sur \( {\mathbb{R}}^{ + } \) par la fonction intégrable \( t \mapsto {e}^{-{\beta t}} \) , donc \( {I}_{\beta } \) est bien dérivable et

> Solution. a) \( {I}_{\beta }\left( x\right) \) is well-defined because its integrand is bounded in absolute value by \( {e}^{-{\beta t}} \) , which is integrable on \( {\mathbb{R}}^{ + } \) . Let \( f\left( {x, t}\right) \) be the integrand of \( {I}_{\beta }\left( x\right) \) . Its partial derivative with respect to \( x \) is \( \partial f/\partial x = - t\sin \left( {xt}\right) /\left( {1 + {t}^{2}}\right) {e}^{-{\beta t}} \) , so \( \left| {\partial f/\partial x}\right| \) is bounded on \( {\mathbb{R}}^{ + } \) by the integrable function \( t \mapsto {e}^{-{\beta t}} \) , therefore \( {I}_{\beta } \) is indeed differentiable and

\[
{I}_{\beta }^{\prime }\left( x\right)  =  - {\int }_{0}^{+\infty }\frac{t\sin \left( {xt}\right) }{1 + {t}^{2}}{e}^{-{\beta t}}{dt}.
\]

---

La relation souhaitée s'obtient maintenant facilement :

> The desired relation is now easily obtained:

\[
{I}_{\beta }\left( x\right)  - {I}_{\beta }^{\prime \prime }\left( x\right)  = {\int }_{0}^{+\infty }\frac{\left( {1 + {t}^{2}}\right) \cos \left( {xt}\right) }{1 + {t}^{2}}{e}^{-{\beta t}}{dt} = {\int }_{0}^{+\infty }\Re \left( {e}^{\left( {{ix} - \beta }\right) t}\right) {dt} = \Re \left( \frac{1}{\beta  - {ix}}\right)  = \frac{\beta }{{\beta }^{2} + {x}^{2}}.
\]

b) Notons \( {J}_{\beta }\left( x\right) = \frac{1}{2}\left( {{e}^{x}{F}_{\beta }\left( x\right) + {e}^{-x}{F}_{\beta }\left( {-x}\right) }\right) \) . Nous allons montrer que \( {J}_{\beta } \) vérifie la même équation différentielle que \( {I}_{\beta } \) . Partant de l’égalité

> b) Let \( {J}_{\beta }\left( x\right) = \frac{1}{2}\left( {{e}^{x}{F}_{\beta }\left( x\right) + {e}^{-x}{F}_{\beta }\left( {-x}\right) }\right) \) . We will show that \( {J}_{\beta } \) satisfies the same differential equation as \( {I}_{\beta } \) . Starting from the equality

\[
{e}^{x}{F}_{\beta }^{\prime }\left( x\right)  =  - \frac{\beta }{{\beta }^{2} + {x}^{2}}
\]

(qui entraîne en particulier que \( {e}^{x}{F}_{\beta }^{\prime }\left( x\right) \) est paire) on obtient par dérivations successives

> (which implies in particular that \( {e}^{x}{F}_{\beta }^{\prime }\left( x\right) \) is even) we obtain by successive differentiations

\[
2{J}_{\beta }^{\prime }\left( x\right)  = {e}^{x}{F}_{\beta }\left( x\right)  - {e}^{-x}{F}_{\beta }\left( {-x}\right)  + {e}^{x}{F}_{\beta }^{\prime }\left( x\right)  - {e}^{-x}{F}_{\beta }^{\prime }\left( {-x}\right)  = {e}^{x}{F}_{\beta }\left( x\right)  - {e}^{-x}{F}_{\beta }\left( {-x}\right) ,
\]

\[
2{J}_{\beta }^{\prime \prime }\left( x\right)  = {e}^{x}{F}_{\beta }\left( x\right)  + {e}^{-x}{F}_{\beta }\left( {-x}\right)  + {e}^{x}{F}_{\beta }^{\prime }\left( x\right)  + {e}^{-x}{F}_{\beta }^{\prime }\left( {-x}\right)  = 2{J}_{\beta }\left( x\right)  - \frac{2\beta }{{\beta }^{2} + {x}^{2}}.
\]

En divisant par 2 cette dernière égalité, on voit que \( {J}_{\beta } \) est une solution particulière de l’équation différentielle linéaire vérifiée par \( {I}_{\beta } \) . La différence \( {K}_{\beta } = {I}_{\beta } - {J}_{\beta } \) vérifie l’équation linéaire d’ordre deux \( {K}_{\beta }^{\prime \prime } - {K}_{\beta } = 0 \) , donc \( {K}_{\beta }\left( x\right) = \lambda {e}^{x} + \mu {e}^{-x} \) avec \( \lambda ,\mu \in \mathbb{R} \) . Ainsi, on a

> By dividing this last equality by 2, we see that \( {J}_{\beta } \) is a particular solution to the linear differential equation satisfied by \( {I}_{\beta } \). The difference \( {K}_{\beta } = {I}_{\beta } - {J}_{\beta } \) satisfies the second-order linear equation \( {K}_{\beta }^{\prime \prime } - {K}_{\beta } = 0 \), therefore \( {K}_{\beta }\left( x\right) = \lambda {e}^{x} + \mu {e}^{-x} \) with \( \lambda ,\mu \in \mathbb{R} \). Thus, we have

\[
{I}_{\beta }\left( x\right)  = {J}_{\beta }\left( x\right)  + {K}_{\beta }\left( x\right)  = {J}_{\beta }\left( x\right)  + \lambda {e}^{x} + \mu {e}^{-x}.
\]

Or les fonctions \( {I}_{\beta }\left( x\right) \) et \( {J}_{\beta }\left( x\right) \) sont bornées sur \( \mathbb{R} \) (on a \( \left| {{I}_{\beta }\left( x\right) }\right| \leq {\int }_{0}^{+\infty }{e}^{-{\beta t}}{dt} \) et \( \left| {{e}^{x}{F}_{\beta }\left( x\right) }\right| \leq \; \left. {{\int }_{-\infty }^{+\infty }\beta /\left( {{\beta }^{2} + {t}^{2}}\right) {dt}}\right) \) , on a donc forcément \( \lambda = \mu = 0 \) d’où le résultat.

> However, the functions \( {I}_{\beta }\left( x\right) \) and \( {J}_{\beta }\left( x\right) \) are bounded on \( \mathbb{R} \) (we have \( \left| {{I}_{\beta }\left( x\right) }\right| \leq {\int }_{0}^{+\infty }{e}^{-{\beta t}}{dt} \) and \( \left| {{e}^{x}{F}_{\beta }\left( x\right) }\right| \leq \; \left. {{\int }_{-\infty }^{+\infty }\beta /\left( {{\beta }^{2} + {t}^{2}}\right) {dt}}\right) \), so we necessarily have \( \lambda = \mu = 0 \)), hence the result.

c) Il est immédiat que \( {I}_{\beta } \) est également définie pour \( \beta = 0 \) . Fixons \( x \in \mathbb{R} \) . La fonction

> c) It is immediate that \( {I}_{\beta } \) is also defined for \( \beta = 0 \). Let us fix \( x \in \mathbb{R} \). The function

\[
f : \left\lbrack  {0, + \infty \left\lbrack  {\times \left\lbrack  {0, + \infty \left\lbrack  { \rightarrow  \mathbb{R}}\right. }\right. }\right. }\right. \left( {\beta , t}\right)  \mapsto  \frac{\cos \left( {xt}\right) }{1 + {t}^{2}}{e}^{-{\beta t}}
\]

est continue et \( \left| {f\left( {\beta , \cdot }\right) }\right| \) est majorée par la fonction intégrable \( t \mapsto 1/\left( {1 + {t}^{2}}\right) \) . L’hypothèse de domination est donc bien vérifiée, ce qui montre que la fonction \( \beta \mapsto {I}_{\beta }\left( x\right) \) est continue sur \( {\mathbb{R}}^{ + } \) . En particulier

> is continuous and \( \left| {f\left( {\beta , \cdot }\right) }\right| \) is bounded by the integrable function \( t \mapsto 1/\left( {1 + {t}^{2}}\right) \). The domination hypothesis is therefore well verified, which shows that the function \( \beta \mapsto {I}_{\beta }\left( x\right) \) is continuous on \( {\mathbb{R}}^{ + } \). In particular

\[
C\left( x\right)  = {I}_{0}\left( x\right)  = \mathop{\lim }\limits_{\substack{{\beta  \rightarrow  0} \\  {\beta  > 0} }}{I}_{\beta }\left( x\right) .
\]

Utilisons maintenant l’expression de \( {I}_{\beta } \) obtenue à la question précédente, en faisant tendre \( \beta \) vers 0 en considérant la suite \( {\left( 1/n\right) }_{n > 0} \) . Lorsque \( n \in {\mathbb{N}}^{ * } \) un changement de variable donne

> Let us now use the expression for \( {I}_{\beta } \) obtained in the previous question, by letting \( \beta \) tend to 0 while considering the sequence \( {\left( 1/n\right) }_{n > 0} \). When \( n \in {\mathbb{N}}^{ * } \) a change of variable gives

\[
{F}_{1/n}\left( x\right)  = {\int }_{nx}^{+\infty }\frac{{e}^{-t/n}}{1 + {t}^{2}}{dt} = {\int }_{-\infty }^{+\infty }{f}_{n}\left( t\right) {dt},\;{f}_{n}\left( t\right)  = \left\{  \begin{array}{ll} {e}^{-t/n}/\left( {1 + {t}^{2}}\right) & \text{ si }t \geq  {nx}, \\  0 & \text{ si }t < {nx}. \end{array}\right.
\]

On a la majoration \( \left| {{f}_{n}\left( t\right) }\right| \leq {e}^{-x}/\left( {1 + {t}^{2}}\right) \) par une fonction intégrable sur \( \mathbb{R} \) . Lorsque \( x > 0 \) , la suite de fonction \( \left( {f}_{n}\right) \) converge simplement vers la fonction nulle, et lorsque \( x < 0,\left( {f}_{n}\right) \) converge simplement vers \( t \mapsto 1/\left( {1 + {t}^{2}}\right) \) sur \( \mathbb{R} \) . Ainsi, le théorème de convergence dominée donne

> We have the bound \( \left| {{f}_{n}\left( t\right) }\right| \leq {e}^{-x}/\left( {1 + {t}^{2}}\right) \) by an integrable function on \( \mathbb{R} \). When \( x > 0 \), the sequence of functions \( \left( {f}_{n}\right) \) converges pointwise to the zero function, and when \( x < 0,\left( {f}_{n}\right) \) it converges pointwise to \( t \mapsto 1/\left( {1 + {t}^{2}}\right) \) on \( \mathbb{R} \). Thus, the dominated convergence theorem gives

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{F}_{1/n}\left( x\right)  = 0\;\left( {x > 0}\right) ,\;\mathop{\lim }\limits_{{n \rightarrow  \infty }}{F}_{1/n}\left( x\right)  = {\int }_{-\infty }^{+\infty }\frac{dt}{1 + {t}^{2}} = \pi \;\left( {x < 0}\right) .
\]

A partir de la relation établie dans la question précédente, on en déduit lorsque \( x > 0 \)

> From the relation established in the previous question, we deduce when \( x > 0 \)

\[
C\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{I}_{1/n}\left( x\right)  = \frac{1}{2}\left( {{e}^{x}\mathop{\lim }\limits_{{n \rightarrow  \infty }}{F}_{1/n}\left( x\right)  + {e}^{-x}\mathop{\lim }\limits_{{n \rightarrow  \infty }}{F}_{1/n}\left( {-x}\right) }\right)  = \frac{\pi }{2}{e}^{-x}.
\]

Par parité on obtient \( C\left( x\right) = \frac{\pi }{2}{e}^{-\left| x\right| } \) pour \( x < 0 \) . La valeur de \( C\left( 0\right) = \pi /2 \) est immédiate.

> By parity we obtain \( C\left( x\right) = \frac{\pi }{2}{e}^{-\left| x\right| } \) for \( x < 0 \). The value of \( C\left( 0\right) = \pi /2 \) is immediate.

Pour calculer \( S\left( x\right) \) , le principe est maintenant de dériver l’expression précédente, mais c’est délicat car l’intégrande dérivée n’est pas intégrable sur \( {\mathbb{R}}^{ + } \) . Supposons \( x > 0 \) et commençons par montrer que l'intégrale impropre \( S\left( x\right) \) converge. En effet, une intégration par parties donne

> To calculate \( S\left( x\right) \), the principle is now to differentiate the previous expression, but this is delicate because the derived integrand is not integrable on \( {\mathbb{R}}^{ + } \). Assume \( x > 0 \) and let us begin by showing that the improper integral \( S\left( x\right) \) converges. Indeed, integration by parts gives

\[
{S}_{T}\left( x\right)  = {\int }_{0}^{T}\frac{t\sin \left( {xt}\right) }{1 + {t}^{2}}{dt} = {\left\lbrack  -\frac{\cos \left( {xt}\right) }{x}\frac{t}{1 + {t}^{2}}\right\rbrack  }_{0}^{T} + {\int }_{0}^{T}\frac{\cos \left( {xt}\right) }{x}\frac{1 - {t}^{2}}{{\left( 1 + {t}^{2}\right) }^{2}}{dt}.
\]

Le premier terme de la dernière somme converge lorsque \( T \rightarrow + \infty \) , et le dernier également puisque son intégrande est intégrable sur \( {\mathbb{R}}^{ + } \) . L’intégrale \( S\left( x\right) \) converge donc pour tout \( x > 0 \) . Considérons maintenant la suite de fonction \( \left( {C}_{n}\right) \) définie par \( {C}_{n}\left( x\right) = {\int }_{0}^{n}\cos \left( {xt}\right) /\left( {1 + {t}^{2}}\right) {dt} \) (qui converge simplement vers \( C\left( x\right) \) ). Pour tout \( n \in \mathbb{N},{C}_{n} \) est dérivable, et \( {C}_{n}^{\prime }\left( x\right) = {S}_{n}\left( x\right) \) . En intégrant par parties, on a

> The first term of the last sum converges as \( T \rightarrow + \infty \), and the last one as well since its integrand is integrable on \( {\mathbb{R}}^{ + } \). The integral \( S\left( x\right) \) therefore converges for all \( x > 0 \). Now consider the sequence of functions \( \left( {C}_{n}\right) \) defined by \( {C}_{n}\left( x\right) = {\int }_{0}^{n}\cos \left( {xt}\right) /\left( {1 + {t}^{2}}\right) {dt} \) (which converges pointwise to \( C\left( x\right) \)). For all \( n \in \mathbb{N},{C}_{n} \), it is differentiable, and \( {C}_{n}^{\prime }\left( x\right) = {S}_{n}\left( x\right) \). Integrating by parts, we have

\[
{S}_{n}\left( x\right)  - S\left( x\right)  = {\int }_{n}^{+\infty }\frac{t\sin \left( {xt}\right) }{1 + {t}^{2}}{dt} = \frac{\cos \left( {xn}\right) }{x}\frac{n}{1 + {n}^{2}} + {\int }_{n}^{+\infty }\frac{\cos \left( {xt}\right) }{x}\frac{1 - {t}^{2}}{{\left( 1 + {t}^{2}\right) }^{2}}{dt},
\]

donc on a la majoration, pour \( a > 0 \) fixé

> thus we have the upper bound, for fixed \( a > 0 \)

\[
\forall x \geq  a,\;\left| {{C}_{n}^{\prime }\left( x\right)  - S\left( x\right) }\right|  = \left| {{S}_{n}\left( x\right)  - S\left( x\right) }\right|  \leq  \frac{1}{an} + {\int }_{n}^{+\infty }\frac{1}{a}\frac{1}{1 + {t}^{2}}{dt}.
\]

Le terme à droite de la dernière inégalité tend vers 0 lorsque \( n \rightarrow + \infty \) , on en déduit que la suite de fonctions \( \left( {C}_{n}^{\prime }\right) \) converge uniformément vers \( S \) sur \( \lbrack a, + \infty \lbrack \) . Donc \( C \) est bien dérivable sur \( \lbrack a, + \infty \lbrack \) et \( {C}^{\prime }\left( x\right) = S\left( x\right) \) pour \( x \geq a \) . Ceci étant vrai pour tout \( a > 0 \) , on en déduit que \( C \) est dérivable sur \( \rbrack 0, + \infty \left\lbrack \right. \) et que \( {C}^{\prime } = S \) sur cet intervalle. A partir de la forme close \( C\left( x\right) = \frac{\pi }{2}{e}^{-x} \) on en déduit \( S\left( x\right) = {C}^{\prime }\left( x\right) = - \frac{\pi }{2}{e}^{-x} \) . Le résultat pour \( x < 0 \) s’en déduit car \( S \) est une fonction impaire, et pour \( x = 0 \) car l’intégrande de \( S \) est nulle dans ce cas.

> The term on the right of the last inequality tends to 0 as \( n \rightarrow + \infty \), from which we deduce that the sequence of functions \( \left( {C}_{n}^{\prime }\right) \) converges uniformly to \( S \) on \( \lbrack a, + \infty \lbrack \). Thus \( C \) is indeed differentiable on \( \lbrack a, + \infty \lbrack \) and \( {C}^{\prime }\left( x\right) = S\left( x\right) \) for \( x \geq a \). Since this is true for all \( a > 0 \), we deduce that \( C \) is differentiable on \( \rbrack 0, + \infty \left\lbrack \right. \) and that \( {C}^{\prime } = S \) on this interval. From the closed form \( C\left( x\right) = \frac{\pi }{2}{e}^{-x} \), we deduce \( S\left( x\right) = {C}^{\prime }\left( x\right) = - \frac{\pi }{2}{e}^{-x} \). The result for \( x < 0 \) follows because \( S \) is an odd function, and for \( x = 0 \) because the integrand of \( S \) is zero in this case.

Probleme 18 (THÉORÉME DES RÉSIDUS, VERSION FAIBLE). On considère une fraction rationnelle \( R \) à coefficients complexes, intégrable sur \( \mathbb{R} \) . On note \( {\mathcal{P}}^{ + } = \{ z \in \mathbb{C} \mid \Im \left( z\right) > 0\} \) et \( {a}_{1},\ldots ,{a}_{n} \) la liste des pôles de \( R\left( {{a}_{i} \neq {a}_{j}\text{ pour }i \neq j}\right) \) . Pour tout \( k \) , on note \( {\operatorname{Res}}_{R}\left( {a}_{k}\right) \) le coefficient de \( 1/\left( {X - {a}_{k}}\right) \) dans l’écriture de \( R \) en éléments simples. a) Montrer

> Problem 18 (RESIDUE THEOREM, WEAK VERSION). Consider a rational fraction \( R \) with complex coefficients, integrable on \( \mathbb{R} \). Let \( {\mathcal{P}}^{ + } = \{ z \in \mathbb{C} \mid \Im \left( z\right) > 0\} \) and \( {a}_{1},\ldots ,{a}_{n} \) be the list of poles of \( R\left( {{a}_{i} \neq {a}_{j}\text{ pour }i \neq j}\right) \). For all \( k \), let \( {\operatorname{Res}}_{R}\left( {a}_{k}\right) \) be the coefficient of \( 1/\left( {X - {a}_{k}}\right) \) in the partial fraction decomposition of \( R \). a) Show

\[
\mathop{\sum }\limits_{{k = 1}}^{n}{\operatorname{Res}}_{R}\left( {a}_{k}\right)  = 0.
\]

b) Montrer

> b) Show

\[
I = {\int }_{-\infty }^{+\infty }R\left( t\right) {dt} = {2i\pi }\mathop{\sum }\limits_{{{a}_{k} \in  {\mathcal{P}}^{ + }}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) .
\]

Solution. a) On peut écrire \( R = P/Q \) avec \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) . Comme \( R \) est intégrable sur \( \mathbb{R} \) , on a \( \deg \left( Q\right) \geq \deg \left( P\right) + 2 \) . Pour tout \( k,1 \leq k \leq n \) , notons \( {\alpha }_{k} \) l’ordre de multiplicité du pôle \( {a}_{k} \) . On peut écrire

> Solution. a) We can write \( R = P/Q \) with \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) . Since \( R \) is integrable on \( \mathbb{R} \) , we have \( \deg \left( Q\right) \geq \deg \left( P\right) + 2 \) . For any \( k,1 \leq k \leq n \) , let \( {\alpha }_{k} \) denote the multiplicity of the pole \( {a}_{k} \) . We can write

\[
R\left( X\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {\mathop{\sum }\limits_{{\ell  = 1}}^{{\alpha }_{k}}\frac{{A}_{k,\ell }}{{\left( X - {a}_{k}\right) }^{\ell }}}\right) \;{A}_{k,\ell } \in  \mathbb{C}\;\text{ et }\;{A}_{k,1} = {\operatorname{Res}}_{R}\left( {a}_{k}\right) .
\]

Comme \( R = P/Q \) avec \( \deg \left( Q\right) \geq \deg \left( P\right) + 2 \) , on a

> Since \( R = P/Q \) with \( \deg \left( Q\right) \geq \deg \left( P\right) + 2 \) , we have

\[
0 = \mathop{\lim }\limits_{{t \rightarrow   + \infty }}{tR}\left( t\right)  = \mathop{\lim }\limits_{{t \rightarrow   + \infty }}\mathop{\sum }\limits_{{k = 1}}^{n}\left( {\mathop{\sum }\limits_{{\ell  = 1}}^{{\alpha }_{k}}\frac{{A}_{k,\ell }t}{{\left( t - {a}_{k}\right) }^{\ell }}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}{A}_{k,1} = \mathop{\sum }\limits_{{k = 1}}^{n}{\operatorname{Res}}_{R}\left( {a}_{k}\right) .
\]

b) La fonction \( R \) est intégrable sur \( \mathbb{R} \) donc aucun de ses pôles \( {a}_{k} \) n’est réel. De plus, pour tout \( k \) , on a

> b) The function \( R \) is integrable on \( \mathbb{R} \) , so none of its poles \( {a}_{k} \) are real. Furthermore, for any \( k \) , we have

\[
\forall \ell  \geq  2,\;{\int }_{-\infty }^{+\infty }\frac{dt}{{\left( t - {a}_{k}\right) }^{\ell }} = {\left\lbrack  \frac{1}{\left( {1 - \ell }\right) {\left( t - {a}_{k}\right) }^{\ell  - 1}}\right\rbrack  }_{-\infty }^{+\infty } = 0,
\]

donc

> therefore

\[
I = {\int }_{-\infty }^{+\infty }\left( {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{A}_{k,1}}{t - {a}_{k}}}\right) {dt}.
\]

(*)

> On ne peut pas à ce stade intervertir les signes de sommation. On va s'en sortir en montrant que \( {\int }_{-T}^{T}{dt}/\left( {t - {a}_{k}}\right) \) converge lorsque \( T \rightarrow \infty \) . Pour tout \( k \) ,écrivons \( {a}_{k} = {x}_{k} + i{y}_{k} \) avec \( {x}_{k},{y}_{k} \in \mathbb{R} \) (et \( {y}_{k} \neq 0 \) puisque \( {a}_{k} \notin \mathbb{R} \) ). La primitive suivante

At this stage, we cannot interchange the summation signs. We will overcome this by showing that \( {\int }_{-T}^{T}{dt}/\left( {t - {a}_{k}}\right) \) converges as \( T \rightarrow \infty \) . For any \( k \) , let us write \( {a}_{k} = {x}_{k} + i{y}_{k} \) with \( {x}_{k},{y}_{k} \in \mathbb{R} \) (and \( {y}_{k} \neq 0 \) since \( {a}_{k} \notin \mathbb{R} \) ). The following primitive

\[
\int \frac{dt}{t - {a}_{k}} = \int \frac{\left( {t - {x}_{k}}\right)  + i{y}_{k}}{{\left( t - {x}_{k}\right) }^{2} + {y}_{k}^{2}}{dt} = \frac{1}{2}\log \left( {{\left( t - {x}_{k}\right) }^{2} + {y}_{k}^{2}}\right)  + i\arctan \left( \frac{t - {x}_{k}}{{y}_{k}}\right)  + K,
\]

permet d'affirmer

> allows us to state

\[
{\int }_{-T}^{T}\frac{dt}{t - {a}_{k}} = \frac{1}{2}\log \left( \frac{{\left( T - {x}_{k}\right) }^{2} + {y}_{k}^{2}}{{\left( T + {x}_{k}\right) }^{2} + {y}_{k}^{2}}\right)  + i\left\lbrack  {\arctan \frac{T - {x}_{k}}{{y}_{k}} + \arctan \frac{T + {x}_{k}}{{y}_{k}}}\right\rbrack
\]

d'ou on déduit

> from which we deduce

\[
\mathop{\lim }\limits_{{T \rightarrow   + \infty }}{\int }_{-T}^{T}\frac{dt}{t - {a}_{k}} = \left\{  \begin{array}{ll} {i\pi } & \text{ si }{y}_{k} > 0, \\   - {i\pi } & \text{ si }{y}_{k} < 0. \end{array}\right.
\]

Donc d'après (*) on a

> Thus, according to (*), we have

\[
I = \mathop{\sum }\limits_{{k = 1}}^{n}{A}_{k,1}\left( {\mathop{\lim }\limits_{{T \rightarrow   + \infty }}{\int }_{-T}^{T}\frac{dt}{t - {a}_{k}}}\right)  = {i\pi }\left( {\mathop{\sum }\limits_{{{y}_{k} > 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right)  - \mathop{\sum }\limits_{{{y}_{k} < 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) }\right) .
\]

D’après la question a), on a \( \mathop{\sum }\limits_{{{y}_{k} < 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) = - \mathop{\sum }\limits_{{{y}_{k} > 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) \) , donc finalement

> According to question a), we have \( \mathop{\sum }\limits_{{{y}_{k} < 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) = - \mathop{\sum }\limits_{{{y}_{k} > 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) \) , so finally

\[
I = {2i\pi }\mathop{\sum }\limits_{{{y}_{k} > 0}}{\operatorname{Res}}_{R}\left( {a}_{k}\right)  = {2i\pi }\mathop{\sum }\limits_{{{a}_{k} \in  {\mathcal{P}}^{ + }}}{\operatorname{Res}}_{R}\left( {a}_{k}\right) .
\]

Remarque. Ce résultat est en fait une conséquence du théorème des résidus. Ce dernier s'applique dans le cadre beaucoup plus général de la théorie des fonctions analytiques.

> Remark. This result is actually a consequence of the residue theorem. The latter applies in the much more general framework of the theory of analytic functions.

Probleme 19. a) En utilisant le résultat du problème précédent, calculer, pour tout \( \left( {n, m}\right) \in {\mathbb{N}}^{2}, n < m \) , l’intégrale

> Problem 19. a) Using the result of the previous problem, calculate, for any \( \left( {n, m}\right) \in {\mathbb{N}}^{2}, n < m \) , the integral

\[
I = {\int }_{-\infty }^{+\infty }\frac{{x}^{2n}}{1 + {x}^{2m}}{dx}.
\]

b) En déduire, pour tout \( \alpha > 1 \) , la valeur de

> b) Deduce, for any \( \alpha > 1 \) , the value of

\[
J\left( \alpha \right)  = {\int }_{0}^{+\infty }\frac{dt}{1 + {t}^{\alpha }}.
\]

Solution. a) L'intégrande est bien intégrable sur \( \mathbb{R} \) car son dénominateur ne s'annule par sur \( \mathbb{R} \) et à l’infini, elle est équivalente à \( {x}^{2\left( {n - m}\right) } \) et \( n - m \leq - 1 \) . En vue d’appliquer le résultat du problème précédent, recherchons les résidus de l'intégrande. Son dénominateur s'écrit

> Solution. a) The integrand is indeed integrable on \( \mathbb{R} \) because its denominator does not vanish on \( \mathbb{R} \) and at infinity, it is equivalent to \( {x}^{2\left( {n - m}\right) } \) and \( n - m \leq - 1 \) . In order to apply the result of the previous problem, let us find the residues of the integrand. Its denominator is written

\[
{X}^{2m} + 1 = \mathop{\prod }\limits_{{k = 0}}^{{{2m} - 1}}\left( {X - {\xi }_{k}}\right) ,\;{\xi }_{k} = \exp \left( \frac{\left( {{2k} + 1}\right) {i\pi }}{2m}\right)  = {\alpha }^{{2k} + 1}\;\text{ avec }\;\alpha  = \exp \left( \frac{i\pi }{2m}\right)
\]

donc tous les pôles sont simples, et on a la décomposition en éléments simples

> therefore all poles are simple, and we have the partial fraction decomposition

\[
R\left( X\right)  = \frac{{X}^{2n}}{{X}^{2m} + 1} = \mathop{\sum }\limits_{{k = 0}}^{{{2m} - 1}}\frac{{A}_{k}}{X - {\xi }_{k}}\;\text{ avec }\;{A}_{k} = \frac{{\xi }_{k}^{2n}}{{2m}{\xi }_{k}^{{2m} - 1}} =  - \frac{{\xi }_{k}^{{2n} + 1}}{2m} =  - \frac{{\alpha }^{\left( {{2n} + 1}\right) \left( {{2k} + 1}\right) }}{2m},
\]

autrement dit, on a \( {2m} \) résidus \( {A}_{k} \) associés aux pôles \( {\xi }_{k} \) qui sont les valeurs

> in other words, we have \( {2m} \) residues \( {A}_{k} \) associated with the poles \( {\xi }_{k} \) which are the values

\[
{A}_{k} =  - \frac{{\beta }^{{2k} + 1}}{2m},\;\beta  = {\alpha }^{{2n} + 1} = \exp \left( \frac{\left( {{2n} + 1}\right) {i\pi }}{2m}\right) .
\]

Comme les résidus de \( R \) dont les parties imaginaires sont strictement positives sont les \( {A}_{k} \) pour \( 0 \leq k \leq m - 1 \) , le résultat du problème précédent entraîne

> Since the residues of \( R \) whose imaginary parts are strictly positive are the \( {A}_{k} \) for \( 0 \leq k \leq m - 1 \) , the result of the previous problem implies

\[
I = {2i\pi }\mathop{\sum }\limits_{{k = 0}}^{{m - 1}}{A}_{k} =  - \frac{2i\pi }{2m}\mathop{\sum }\limits_{{k = 0}}^{{m - 1}}{\beta }^{{2k} + 1} =  - \frac{i\pi \beta }{m}\frac{1 - {\beta }^{2m}}{1 - {\beta }^{2}} = \frac{i\pi }{m}\frac{2}{\beta  - 1/\beta } = \frac{\pi }{m\sin \left( {\frac{{2n} + 1}{2m}\pi }\right) }.
\]

b) Nous allons exploiter l’idée suivante : si \( \alpha \) est de la forme \( {2m}/\left( {{2n} + 1}\right) \) , le changement de variable \( u = {t}^{1/\left( {{2n} + 1}\right) } \) nous ramène à une intégrale du type de a).

> b) We will exploit the following idea: if \( \alpha \) is of the form \( {2m}/\left( {{2n} + 1}\right) \), the change of variable \( u = {t}^{1/\left( {{2n} + 1}\right) } \) brings us back to an integral of the type in a).

La fonction \( {f}_{\alpha } : t \mapsto 1/\left( {1 + {t}^{\alpha }}\right) \) est intégrable sur \( {\mathbb{R}}^{ + } \) pour tout \( \alpha > 1 \) . Si \( a > 1 \) , l’application \( \alpha \mapsto J\left( \alpha \right) \) est continue sur \( \lbrack a, + \infty \lbrack \) (on a \( {f}_{\alpha } \leq {f}_{a} \) pour \( \alpha \geq a \) donc l’hypothèse de domination est vérifiée). Ceci étant vrai pour tout \( a > 1, J \) est continue sur \( \rbrack 1, + \infty \lbrack \) .

> The function \( {f}_{\alpha } : t \mapsto 1/\left( {1 + {t}^{\alpha }}\right) \) is integrable on \( {\mathbb{R}}^{ + } \) for all \( \alpha > 1 \). If \( a > 1 \), the mapping \( \alpha \mapsto J\left( \alpha \right) \) is continuous on \( \lbrack a, + \infty \lbrack \) (we have \( {f}_{\alpha } \leq {f}_{a} \) for \( \alpha \geq a \), so the domination hypothesis is satisfied). Since this is true for all \( a > 1, J \), it is continuous on \( \rbrack 1, + \infty \lbrack \).

Fixons maintenant \( \alpha > 1 \) . Comme \( \mathbb{Q} \) est dense dans \( \mathbb{R} \) , on peut trouver deux suites d’entiers \( \left( {p}_{n}\right) \) et \( \left( {q}_{n}\right) \) tendant chacune vers l’infini, telles que \( \left( {{p}_{n}/{q}_{n}}\right) \) converge vers \( \alpha \) . Comme \( {q}_{n} \rightarrow + \infty \) , la suite \( \left( {2{p}_{n}/\left( {2{q}_{n} + 1}\right) }\right) \) converge aussi vers \( \alpha \) . Le fait que \( \alpha > 1 \) assure l’existence d’un rang à partir duquel \( {p}_{n} > {q}_{n} \) .

> Let us now fix \( \alpha > 1 \). Since \( \mathbb{Q} \) is dense in \( \mathbb{R} \), we can find two sequences of integers \( \left( {p}_{n}\right) \) and \( \left( {q}_{n}\right) \) both tending to infinity, such that \( \left( {{p}_{n}/{q}_{n}}\right) \) converges to \( \alpha \). Since \( {q}_{n} \rightarrow + \infty \), the sequence \( \left( {2{p}_{n}/\left( {2{q}_{n} + 1}\right) }\right) \) also converges to \( \alpha \). The fact that \( \alpha > 1 \) ensures the existence of a rank from which \( {p}_{n} > {q}_{n} \).

Lorsque \( p > q \) sont deux entiers naturels, le changement de variable \( u = {t}^{1/\left( {{2q} + 1}\right) } \) donne

> When \( p > q \) are two natural integers, the change of variable \( u = {t}^{1/\left( {{2q} + 1}\right) } \) gives

\[
J\left( \frac{2p}{{2q} + 1}\right)  = \left( {{2q} + 1}\right) {\int }_{0}^{+\infty }\frac{{u}^{2q}{du}}{1 + {u}^{2p}} = \frac{{2q} + 1}{2}{\int }_{-\infty }^{+\infty }\frac{{u}^{2q}{du}}{1 + {u}^{2p}} = \pi {\left( \frac{2p}{{2q} + 1}\sin \left( \frac{\pi }{\frac{2p}{{2q} + 1}}\right) \right) }^{-1}.
\]

Ainsi, la fonction \( J \) étant continue en \( \alpha \) , on a

> Thus, the function \( J \) being continuous at \( \alpha \), we have

\[
J\left( \alpha \right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}J\left( \frac{2{p}_{n}}{2{q}_{n} + 1}\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\pi {\left( \frac{2{p}_{n}}{2{q}_{n} + 1}\sin \left( \frac{\pi }{\frac{2{p}_{n}}{2{q}_{n} + 1}}\right) \right) }^{-1} = \frac{\pi }{\alpha \sin \left( {\pi /\alpha }\right) }.
\]

PROBLEME 20 (UNE PREUVE DU THÉORÉME DE CONVERGENCE DOMINÉE). On note \( {\mathcal{C}}_{m}\left( {I, F}\right) \) l’e.v. des fonctions continues par morceaux sur \( I \) à valeurs dans \( F \) .

> PROBLEM 20 (A PROOF OF THE DOMINATED CONVERGENCE THEOREM). Let \( {\mathcal{C}}_{m}\left( {I, F}\right) \) be the vector space of piecewise continuous functions on \( I \) with values in \( F \).

1 / Soit \( S = \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) et \( f \in {\mathcal{C}}_{m}\left( {S,\mathbb{R}}\right) \) . Soit \( \varepsilon > 0 \) . Montrer qu’il existe deux fonctions continues \( {f}_{ - } \) et \( {f}_{ + } \) dans de \( S \) dans \( \mathbb{R} \) telles que

> 1 / Let \( S = \left\lbrack {a, b}\right\rbrack \) be a segment of \( \mathbb{R} \) and \( f \in {\mathcal{C}}_{m}\left( {S,\mathbb{R}}\right) \). Let \( \varepsilon > 0 \). Show that there exist two continuous functions \( {f}_{ - } \) and \( {f}_{ + } \) in \( S \) from \( \mathbb{R} \) such that

\[
{f}_{ - } \leq  f \leq  {f}_{ + }\;\text{ et }\;\left( {{\int }_{S}{f}_{ + }}\right)  - \varepsilon  < {\int }_{S}f < \left( {{\int }_{S}{f}_{ - }}\right)  + \varepsilon .
\]

2 / Soit \( I \) un intervalle de \( \mathbb{R} \) et \( E \) un e.v.n complet. Soit \( \left( {u}_{n}\right) \) une suite d’éléments de \( {\mathcal{C}}_{m}\left( {I, E}\right) \) , telle que \( {u}_{n} \) est intégrable sur \( I \) pour tout \( n \) , et telle que la série de fonc-tions \( \sum {u}_{n} \) converge simplement vers une fonction \( f \in {\mathcal{C}}_{m}\left( {I, E}\right) \) sur \( I \) . On suppose que \( \mathop{\sum }\limits_{n}{\int }_{I}\begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converge.

> 2 / Let \( I \) be an interval of \( \mathbb{R} \) and \( E \) a complete normed vector space. Let \( \left( {u}_{n}\right) \) be a sequence of elements of \( {\mathcal{C}}_{m}\left( {I, E}\right) \), such that \( {u}_{n} \) is integrable on \( I \) for all \( n \), and such that the series of functions \( \sum {u}_{n} \) converges pointwise to a function \( f \in {\mathcal{C}}_{m}\left( {I, E}\right) \) on \( I \). Suppose that \( \mathop{\sum }\limits_{n}{\int }_{I}\begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converges.

a) Soit \( S = \left\lbrack {a, b}\right\rbrack \) un segment inclus dans \( I \) . Montrer que \( {\int }_{S}\parallel f\parallel \leq \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{S}\begin{Vmatrix}{u}_{n}\end{Vmatrix} \) (commencer par le cas où \( f \) et les \( {u}_{n} \) sont continues, en appliquant à \( \parallel f\parallel \) et \( \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) un argument similaire à celui utilisé pour la preuve du premier théorème de Dini, puis adapter le rai-sonnement).

> a) Let \( S = \left\lbrack {a, b}\right\rbrack \) be a segment included in \( I \). Show that \( {\int }_{S}\parallel f\parallel \leq \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{S}\begin{Vmatrix}{u}_{n}\end{Vmatrix} \) (start with the case where \( f \) and the \( {u}_{n} \) are continuous, by applying to \( \parallel f\parallel \) and \( \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) an argument similar to that used for the proof of the first Dini theorem, then adapt the reasoning).

b) Montrer que \( f \) est intégrable sur \( I \) et que

> b) Show that \( f \) is integrable on \( I \) and that

\[
{\int }_{I}\parallel f\parallel  \leq  \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{I}\begin{Vmatrix}{u}_{n}\end{Vmatrix}\;\text{ et }\;{\int }_{I}f = \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{I}{u}_{n}.
\]

3/ Soit \( \left( {f}_{n}\right) \) une suite d’éléments de \( {\mathcal{C}}_{m}\left( {I,{\mathbb{R}}^{ + }}\right) \) convergeant simplement vers la fonction nulle sur \( I \) , et telle qu’il existe une fonction \( \varphi \in {\mathcal{C}}_{m}\left( {I,{\mathbb{R}}^{ + }}\right) \) , intégrable sur \( I \) , vérifiant \( {f}_{n} \leq \varphi \) pour tout \( n \) .

> 3/ Let \( \left( {f}_{n}\right) \) be a sequence of elements of \( {\mathcal{C}}_{m}\left( {I,{\mathbb{R}}^{ + }}\right) \) converging pointwise to the zero function on \( I \), and such that there exists a function \( \varphi \in {\mathcal{C}}_{m}\left( {I,{\mathbb{R}}^{ + }}\right) \), integrable on \( I \), satisfying \( {f}_{n} \leq \varphi \) for all \( n \).

a) Soit \( n \in \mathbb{N} \) . Pour \( p \geq n \) , on pose \( {f}_{n, p} = \max \left( {{f}_{n},{f}_{n + 1},\ldots ,{f}_{p}}\right) \) . Montrer qu’il existe \( {p}_{n} \geq n \) tel que \( {p}_{n} \geq {p}_{n - 1} \) et \( \left| {{\int }_{I}{f}_{n, p} - {\int }_{I}{f}_{n,{p}_{n}}}\right| < {2}^{-n} \) pour tout \( p \geq {p}_{n} \) .

> a) Let \( n \in \mathbb{N} \). For \( p \geq n \), we define \( {f}_{n, p} = \max \left( {{f}_{n},{f}_{n + 1},\ldots ,{f}_{p}}\right) \). Show that there exists \( {p}_{n} \geq n \) such that \( {p}_{n} \geq {p}_{n - 1} \) and \( \left| {{\int }_{I}{f}_{n, p} - {\int }_{I}{f}_{n,{p}_{n}}}\right| < {2}^{-n} \) for all \( p \geq {p}_{n} \).

b) On pose \( {g}_{n} = {f}_{n,{p}_{n}} \) . Montrer que \( \left| {{g}_{n + 1} - {g}_{n}}\right| \leq 2\left( {{f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}}}\right) + {g}_{n} - {g}_{n + 1} \) .

> b) Let \( {g}_{n} = {f}_{n,{p}_{n}} \) . Show that \( \left| {{g}_{n + 1} - {g}_{n}}\right| \leq 2\left( {{f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}}}\right) + {g}_{n} - {g}_{n + 1} \) .

c) En déduire que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}{f}_{n} = 0 \) .

> c) Deduce that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}{f}_{n} = 0 \) .

4/ Démontrer le théorème de convergence dominée (page 151).

> 4/ Prove the dominated convergence theorem (page 151).

Solution. 1/ Si \( f \) est continue c’est évident. Sinon, notons \( {x}_{1} < {x}_{2} < \cdots < {x}_{n} \) les points de discontinuité de \( f \) . Soient deux réels \( m \) et \( M \) tels que \( m < \mathop{\inf }\limits_{{x \in S}}f\left( x\right) \) et \( M > \mathop{\sup }\limits_{{x \in S}}f\left( x\right) \) .

> Solution. 1/ If \( f \) is continuous, it is obvious. Otherwise, let \( {x}_{1} < {x}_{2} < \cdots < {x}_{n} \) be the points of discontinuity of \( f \) . Let two real numbers \( m \) and \( M \) be such that \( m < \mathop{\inf }\limits_{{x \in S}}f\left( x\right) \) and \( M > \mathop{\sup }\limits_{{x \in S}}f\left( x\right) \) .

Soit \( \alpha > 0 \) avec \( \alpha < \frac{1}{2}\min \left( {{x}_{i + 1} - {x}_{i}}\right) \) . Considérons la fonction continue \( {\varphi }_{ - } \) définie sur \( S \) par

> Let \( \alpha > 0 \) with \( \alpha < \frac{1}{2}\min \left( {{x}_{i + 1} - {x}_{i}}\right) \) . Consider the continuous function \( {\varphi }_{ - } \) defined on \( S \) by

\[
{\varphi }_{ - }\left( x\right)  = m + \left( {M - m}\right) \frac{\left| x - {x}_{i}\right| }{\alpha },\;\text{ si }\;x \in  {J}_{i} = \left\lbrack  {{x}_{i} - \alpha ,{x}_{i} + \alpha }\right\rbrack   \cap  S,\;{\varphi }_{ - }\left( x\right)  = M\;\text{ ailleurs. }
\]

L’application \( {f}_{ - } = \min \left( {f,{\varphi }_{ - }}\right) \) vérifie \( {f}_{ - } \leq f \) par construction et est continue, car

> The mapping \( {f}_{ - } = \min \left( {f,{\varphi }_{ - }}\right) \) satisfies \( {f}_{ - } \leq f \) by construction and is continuous, because

- si \( x \) n’est pas l’un des \( {x}_{i}, f \) est continue en \( x \) donc \( {f}_{ - } = \frac{1}{2}\left( {f + {\varphi }_{ - } - \left| {f - {\varphi }_{ - }}\right| }\right) \) l’est aussi ;

> - if \( x \) is not one of the \( {x}_{i}, f \) , it is continuous at \( x \) , so \( {f}_{ - } = \frac{1}{2}\left( {f + {\varphi }_{ - } - \left| {f - {\varphi }_{ - }}\right| }\right) \) is as well;

- pour tout \( i,{f}_{ - }\left( {x}_{i}\right)  = m \) donc \( {f}_{ - } = {\varphi }_{ - } \) sur un voisinage de \( {x}_{i} \) , donc \( {f}_{ - } \) est continue en \( {x}_{i} \) .

> - for all \( i,{f}_{ - }\left( {x}_{i}\right)  = m \) , so \( {f}_{ - } = {\varphi }_{ - } \) on a neighborhood of \( {x}_{i} \) , so \( {f}_{ - } \) is continuous at \( {x}_{i} \) .

Lorsque \( x \) n’est pas dans l’un des \( {J}_{i} \) , on a \( {f}_{ - }\left( x\right) = f\left( x\right) \) car \( f\left( x\right) < M = {\varphi }_{ - }\left( x\right) \) . On a donc

> When \( x \) is not in one of the \( {J}_{i} \) , we have \( {f}_{ - }\left( x\right) = f\left( x\right) \) because \( f\left( x\right) < M = {\varphi }_{ - }\left( x\right) \) . We therefore have

\[
{\int }_{S}\left( {f - {f}_{ - }}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\int }_{{J}_{i}}\left( {f - {f}_{ - }}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}{\int }_{{J}_{i}}\left( {M - m}\right)  \leq  {2\alpha n}\left( {M - m}\right)
\]

En choisissant \( \alpha \leq \varepsilon /\left( {2\left( {M - m}\right) n}\right) \) , on a donc \( {\int }_{S}\left( {f - {f}_{ - }}\right) < \varepsilon \) . On construit de manière analogue \( {f}_{ + } = \max \left( {{\varphi }_{ + }, f}\right) \) avec \( {\varphi }_{ + } = M - \left( {M - m}\right) \left| {x - {x}_{i}}\right| /\alpha \) sur \( {J}_{i} \) et \( {\varphi }_{ + } = m \) ailleurs.

> By choosing \( \alpha \leq \varepsilon /\left( {2\left( {M - m}\right) n}\right) \) , we therefore have \( {\int }_{S}\left( {f - {f}_{ - }}\right) < \varepsilon \) . We construct \( {f}_{ + } = \max \left( {{\varphi }_{ + }, f}\right) \) analogously with \( {\varphi }_{ + } = M - \left( {M - m}\right) \left| {x - {x}_{i}}\right| /\alpha \) on \( {J}_{i} \) and \( {\varphi }_{ + } = m \) elsewhere.

2/ a) Comme indiqué, nous allons commencer par le cas où \( f \) et les \( {u}_{n} \) sont continues. Soit \( \varepsilon > 0 \) . Pour tout \( n \) , considérons l’ensemble

> 2/ a) As indicated, we will start with the case where \( f \) and the \( {u}_{n} \) are continuous. Let \( \varepsilon > 0 \) . For all \( n \) , consider the set

\[
{F}_{n} = \left\{  {x \in  S : \parallel f\left( x\right) \parallel  \geq  \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{n}\begin{Vmatrix}{{u}_{k}\left( x\right) }\end{Vmatrix}}\right\}
\]

La suite \( \left( {F}_{n}\right) \) est une suite décroissante de fermés de \( S \) (donc compacts). On a \( { \cap }_{n > 0}{F}_{n} = \varnothing \) car pour tout \( x \in S \) , il existe \( n \) tel que \( \begin{Vmatrix}{f\left( x\right) - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\left( x\right) }\end{Vmatrix} < \varepsilon \) , ce qui entraîne \( x \notin {F}_{n} \) . Une suite décroissante de compacts non vide est non vide, donc il existe forcément \( n \) tel que \( {F}_{n} = \varnothing \) , autrement dit \( \parallel f\parallel < \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) sur \( S \) . Ceci entraîne

> The sequence \( \left( {F}_{n}\right) \) is a decreasing sequence of closed sets of \( S \) (therefore compact). We have \( { \cap }_{n > 0}{F}_{n} = \varnothing \) because for any \( x \in S \) , there exists \( n \) such that \( \begin{Vmatrix}{f\left( x\right) - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\left( x\right) }\end{Vmatrix} < \varepsilon \) , which implies \( x \notin {F}_{n} \) . A decreasing sequence of non-empty compact sets is non-empty, so there necessarily exists \( n \) such that \( {F}_{n} = \varnothing \) , in other words \( \parallel f\parallel < \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) on \( S \) . This implies

\[
{\int }_{S}\parallel f\parallel  \leq  \left( {b - a}\right) \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{n}{\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq  \left( {b - a}\right) \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix}.
\]

Cette dernière majoration est vraie pour tout \( \varepsilon > 0 \) donc on a bien le résultat attendu.

> This last upper bound is true for all \( \varepsilon > 0 \) so we indeed have the expected result.

Traitons maintenant le cas général. Soit \( \varepsilon > 0 \) . D’après 1/, il existe une fonction continue \( g \) sur \( S \) et une suite \( \left( {v}_{n}\right) \) de fonctions continues sur \( S \) telles que

> Let us now treat the general case. Let \( \varepsilon > 0 \) . According to 1/, there exists a continuous function \( g \) on \( S \) and a sequence \( \left( {v}_{n}\right) \) of continuous functions on \( S \) such that

\[
g \leq  \parallel f\parallel \;\text{ avec }{\int }_{S}\parallel f\parallel  < \varepsilon  + {\int }_{S}g,\;\text{ et }\;\forall n \in  \mathbb{N},\;\begin{Vmatrix}{u}_{n}\end{Vmatrix} \leq  {v}_{n}\;\text{ avec }{\int }_{S}{v}_{n} \leq  \frac{\varepsilon }{{2}^{n}} + {\int }_{S}\begin{Vmatrix}{u}_{n}\end{Vmatrix}.
\]

On note \( {G}_{n} = \left\{ {x \in S : g\left( x\right) \geq \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k}\left( x\right) }\right\} \) , de sorte que \( \left( {G}_{n}\right) \) est une suite décroissante de compacts. Leur intersection est vide (car \( \begin{Vmatrix}{f\left( x\right) - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\left( x\right) }\end{Vmatrix} < \varepsilon \) entraîne \( g\left( x\right) < \varepsilon + \; \left. {\mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k}\left( x\right) }\right) \) , donc il existe \( n \) avec \( {G}_{n} = \varnothing \) . Ceci entraîne \( g < \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \) sur \( S \) , donc

> We denote \( {G}_{n} = \left\{ {x \in S : g\left( x\right) \geq \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k}\left( x\right) }\right\} \) , so that \( \left( {G}_{n}\right) \) is a decreasing sequence of compact sets. Their intersection is empty (because \( \begin{Vmatrix}{f\left( x\right) - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\left( x\right) }\end{Vmatrix} < \varepsilon \) implies \( g\left( x\right) < \varepsilon + \; \left. {\mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k}\left( x\right) }\right) \) , so there exists \( n \) with \( {G}_{n} = \varnothing \) . This implies \( g < \varepsilon + \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \) on \( S \) , so

\[
{\int }_{S}\parallel f\parallel  \leq  \varepsilon  + {\int }_{S}g \leq  \left( {1 + b - a}\right) \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{n}{\int }_{S}{v}_{k} \leq  \left( {3 + b - a}\right) \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{n}{\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq  \left( {3 + b - a}\right) \varepsilon  + \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix}.
\]

On conclut comme précédemment.

> We conclude as before.

b) Comme \( {\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq {\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) , le résultat précédent entraîne la majoration

> b) Since \( {\int }_{S}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq {\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) , the previous result implies the upper bound

\[
{\int }_{S}\parallel f\parallel  \leq  \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix},
\]

et ceci pour tout segment \( S \) de \( I \) . Par définition, \( f \) est donc intégrable sur \( I \) et on a \( {\int }_{I}\parallel f\parallel \leq \; \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) . En appliquant ce même résultat à \( f - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) on obtient

> and this for any segment \( S \) of \( I \) . By definition, \( f \) is therefore integrable on \( I \) and we have \( {\int }_{I}\parallel f\parallel \leq \; \mathop{\sum }\limits_{{k = 0}}^{\infty }{\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix} \) . By applying this same result to \( f - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) we obtain

\[
{\int }_{I}\begin{Vmatrix}{f - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = n + 1}}^{\infty }{\int }_{I}\begin{Vmatrix}{u}_{k}\end{Vmatrix}
\]

donc \( {\left( {\int }_{I}\begin{Vmatrix}f - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\end{Vmatrix}\right) }_{n \in \mathbb{N}} \) tend vers 0 lorsque \( n \rightarrow \infty \) . Comme \( \begin{Vmatrix}{{\int }_{I}f - \mathop{\sum }\limits_{{k = 0}}^{n}{\int }_{I}{u}_{k}}\end{Vmatrix} \leq {\int }_{I}\parallel f - \; \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\parallel \) , on en déduit lim \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}f = \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{I}{u}_{n} \) .

> therefore \( {\left( {\int }_{I}\begin{Vmatrix}f - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\end{Vmatrix}\right) }_{n \in \mathbb{N}} \) tends to 0 as \( n \rightarrow \infty \) . Since \( \begin{Vmatrix}{{\int }_{I}f - \mathop{\sum }\limits_{{k = 0}}^{n}{\int }_{I}{u}_{k}}\end{Vmatrix} \leq {\int }_{I}\parallel f - \; \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}\parallel \) , we deduce lim \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}f = \mathop{\sum }\limits_{{n = 0}}^{\infty }{\int }_{I}{u}_{n} \) .

3/ a) Fixons \( n \) . Remarquons que les \( {f}_{n, p} \) sont dans \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) (le maximum de deux fonctions \( a \) et \( b \) de \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) s’écrit \( \frac{1}{2}\left( {a + b + \left| {a - b}\right| }\right) \) donc est dans \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) ) et intégrables car \( {f}_{n, p} \leq \varphi \) . La suite \( {\left( {f}_{n, p}\right) }_{p} \) est croissante, donc la suite \( {\left( {I}_{n, p}\right) }_{p} \) définie par \( {I}_{n, p} = {\int }_{I}{f}_{n, p} \) est croissante. Comme elle est majorée par \( {\int }_{I}\varphi \) , elle converge, donc c’est une suite de Cauchy, donc il existe \( {p}_{n} \) tel que \( \left| {{I}_{n, p} - {I}_{n, q}}\right| < {2}^{-n} \) pour \( p, q \geq {p}_{n} \) . On peut choisir \( {p}_{n} \) aussi grand que voulu, d’où le résultat.

> 3/ a) Let us fix \( n \) . Note that the \( {f}_{n, p} \) are in \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) (the maximum of two \( a \) and \( b \) functions of \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) is written \( \frac{1}{2}\left( {a + b + \left| {a - b}\right| }\right) \) and is therefore in \( {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) ) and are integrable because \( {f}_{n, p} \leq \varphi \) . The sequence \( {\left( {f}_{n, p}\right) }_{p} \) is increasing, so the sequence \( {\left( {I}_{n, p}\right) }_{p} \) defined by \( {I}_{n, p} = {\int }_{I}{f}_{n, p} \) is increasing. As it is bounded above by \( {\int }_{I}\varphi \) , it converges, so it is a Cauchy sequence, therefore there exists \( {p}_{n} \) such that \( \left| {{I}_{n, p} - {I}_{n, q}}\right| < {2}^{-n} \) for \( p, q \geq {p}_{n} \) . We can choose \( {p}_{n} \) as large as desired, hence the result.

b) Si \( {g}_{n + 1} - {g}_{n} < 0 \) , c’est immédiat car \( {f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}} \geq 0 \) . Sinon il suffit de remarquer que \( {g}_{n + 1} - {g}_{n} = {f}_{n + 1,{p}_{n + 1}} - {f}_{n,{p}_{n}} \leq {f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}}. \)

> b) If \( {g}_{n + 1} - {g}_{n} < 0 \) , it is immediate because \( {f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}} \geq 0 \) . Otherwise, it suffices to note that \( {g}_{n + 1} - {g}_{n} = {f}_{n + 1,{p}_{n + 1}} - {f}_{n,{p}_{n}} \leq {f}_{n,{p}_{n + 1}} - {f}_{n,{p}_{n}}. \)

c) Posons \( {u}_{n} = {g}_{n} - {g}_{n + 1} \) . L’inégalité précédente entraîne

> c) Let \( {u}_{n} = {g}_{n} - {g}_{n + 1} \) . The previous inequality implies

\[
{\int }_{I}\left| {u}_{n}\right|  \leq  2\left| {{I}_{n,{p}_{n + 1}} - {I}_{n,{p}_{n}}}\right|  + {\int }_{I}{g}_{n} - {\int }_{I}{g}_{n + 1} \leq  {2}^{1 - n} + {\int }_{I}{g}_{n} - {\int }_{I}{g}_{n + 1},
\]

par sommation on obtient

> by summation we obtain

\[
\forall p \in  \mathbb{N},\;\mathop{\sum }\limits_{{n = 0}}^{p}{\int }_{I}\left| {u}_{n}\right|  \leq  \mathop{\sum }\limits_{{n = 0}}^{p}{2}^{1 - n} + {\int }_{I}{g}_{0} - {\int }_{I}{g}_{p + 1} \leq  4 + {\int }_{I}{g}_{0}.
\]

Par ailleurs, la suite de fonctions \( \left( {g}_{n}\right) \) converge simplement vers 0, donc on a \( \mathop{\sum }\limits_{{k > n}}{u}_{k} = {g}_{n} \) . Finalement nous avons montré que la série de fonctions \( \mathop{\sum }\limits_{{k \geq n}}{u}_{k} \) vérifie les hypothèses de la partie \( 2/ \) du problème, donc

> Furthermore, the sequence of functions \( \left( {g}_{n}\right) \) converges pointwise to 0, so we have \( \mathop{\sum }\limits_{{k > n}}{u}_{k} = {g}_{n} \) . Finally, we have shown that the series of functions \( \mathop{\sum }\limits_{{k \geq n}}{u}_{k} \) satisfies the hypotheses of part \( 2/ \) of the problem, therefore

\[
0 \leq  {\int }_{I}{f}_{n} \leq  {\int }_{I}{g}_{n} = {\int }_{I}\left( {\mathop{\sum }\limits_{{k \geq  n}}{u}_{k}}\right)  = \mathop{\sum }\limits_{{k \geq  n}}{\int }_{I}{u}_{k}.
\]

Le dernier terme est le reste d’une série absolument convergente, d’où \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}{f}_{n} = 0 \) .

> The last term is the remainder of an absolutely convergent series, hence \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\int }_{I}{f}_{n} = 0 \) .

4/ Reprenons les notations du théorème de convergence dominée, page 151. On a \( \parallel f\parallel \leq \varphi \) donc \( f \) est bien intégrable. Ensuite, il suffit d’appliquer le résultat de la question précédente à la suite \( \left( \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix}\right) \) , majorée par la fonction intégrable \( {2\varphi } \) , et qui converge simplement vers la fonction nulle. Donc \( \left( {{\int }_{I}\begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix}}\right) \) tend vers 0, et comme \( \begin{Vmatrix}{{\int }_{I}{f}_{n} - {\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} \) , ceci termine la preuve du théorème de convergence dominée.

> 4/ Let us return to the notation of the dominated convergence theorem, page 151. We have \( \parallel f\parallel \leq \varphi \) so \( f \) is indeed integrable. Next, it suffices to apply the result of the previous question to the sequence \( \left( \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix}\right) \) , bounded by the integrable function \( {2\varphi } \) , and which converges pointwise to the zero function. Thus \( \left( {{\int }_{I}\begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix}}\right) \) tends to 0, and since \( \begin{Vmatrix}{{\int }_{I}{f}_{n} - {\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} \) , this completes the proof of the dominated convergence theorem.

PROBLEME 21 (DEUXIÉME PREUVE DU THÉORÉME DE CONVERGENCE DOMINÉE). Quelques définitions et remarques.

> PROBLEM 21 (SECOND PROOF OF THE DOMINATED CONVERGENCE THEOREM). Some definitions and remarks.

- Une partie bornée \( E \) de \( \mathbb{R} \) est dite élémentaire si \( E \) est réunion finie d’intervalles bornés, i. e. si \( {\chi }_{E} \) (fonction caractéristique de \( E \) ) est une fonction en escalier. On peut alors définir la mesure de \( E \) par \( m\left( E\right)  = {\int }_{\mathbb{R}}{\chi }_{E}\left( t\right) {dt} \) . De même, si \( f \) est continue par morceaux sur \( \left\lbrack  {a, b}\right\rbrack   \supset  E \) , on définit \( {\int }_{E}f = {\int }_{a}^{b}f\left( t\right) {\chi }_{E}\left( t\right) {dt} \) .

> - A bounded subset \( E \) of \( \mathbb{R} \) is called elementary if \( E \) is a finite union of bounded intervals, i.e., if \( {\chi }_{E} \) (characteristic function of \( E \) ) is a step function. We can then define the measure of \( E \) by \( m\left( E\right)  = {\int }_{\mathbb{R}}{\chi }_{E}\left( t\right) {dt} \) . Similarly, if \( f \) is piecewise continuous on \( \left\lbrack  {a, b}\right\rbrack   \supset  E \) , we define \( {\int }_{E}f = {\int }_{a}^{b}f\left( t\right) {\chi }_{E}\left( t\right) {dt} \) .

- Si \( E \) et \( F \) sont deux parties élémentaires disjointes et \( f \) une fonction réelle continue par morceaux, on a facilement \( {\int }_{E \cup  F}f = {\int }_{E}f + {\int }_{F}f \) ; si \( \left| {f\left( x\right) }\right|  \leq  K \) pour tout \( x \in  E \) , alors \( \left| {{\int }_{E}f}\right|  \leq  {Km}\left( E\right) \) .

> - If \( E \) and \( F \) are two disjoint elementary subsets and \( f \) is a piecewise continuous real function, we easily have \( {\int }_{E \cup  F}f = {\int }_{E}f + {\int }_{F}f \) ; if \( \left| {f\left( x\right) }\right|  \leq  K \) for all \( x \in  E \) , then \( \left| {{\int }_{E}f}\right|  \leq  {Km}\left( E\right) \) .

- Il est également clair que si \( E \) est élémentaire, alors pour tout \( \varepsilon  > 0 \) , il existe un ensemble \( H \) , borné, fermé et élémentaire, tel que \( H \subset  E \) et \( m\left( H\right)  > m\left( E\right)  - \varepsilon \) .

> - It is also clear that if \( E \) is elementary, then for all \( \varepsilon  > 0 \) , there exists a bounded, closed, and elementary set \( H \) such that \( H \subset  E \) and \( m\left( H\right)  > m\left( E\right)  - \varepsilon \) .

a) Soit \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite décroissante de sous-ensembles bornés de \( \mathbb{R} \) telle que \( { \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n} = \; \varnothing \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note

> a) Let \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a decreasing sequence of bounded subsets of \( \mathbb{R} \) such that \( { \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n} = \; \varnothing \) . For all \( n \in {\mathbb{N}}^{ * } \) , we denote

\[
{\alpha }_{n} = \sup {\Gamma }_{n}\text{ où }{\Gamma }_{n} = \{ m\left( E\right) , E\text{ élémentaire et }E \subset  {A}_{n}\} .
\]

Montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} = 0 \) .

> Show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} = 0 \) .

b) Soit \( \left( {f}_{n}\right) \) une suite de fonctions de \( \left\lbrack {a, b}\right\rbrack \) dans un e.v.n complet \( A \) , continue par morceaux, convergeant simplement vers une fonction \( f : \left\lbrack {a, b}\right\rbrack \rightarrow A \) continue par morceaux, et uniformément bornée, c'est-à-dire

> b) Let \( \left( {f}_{n}\right) \) be a sequence of functions from \( \left\lbrack {a, b}\right\rbrack \) to a complete n.v.s. \( A \) , piecewise continuous, converging pointwise to a piecewise continuous function \( f : \left\lbrack {a, b}\right\rbrack \rightarrow A \) , and uniformly bounded, that is to say

\[
\exists K > 0,\forall n \in  {\mathbb{N}}^{ * },\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;\begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq  K.
\]

Montrer que

> Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}{f}_{n}\left( t\right) {dt} = {\int }_{a}^{b}f\left( t\right) {dt}
\]

c) En déduire une preuve du théorème de convergence dominée (page 151).

> c) Deduce a proof of the dominated convergence theorem (page 151).

Solution. a) Toute partie élémentaire incluse dans \( {A}_{n + 1} \) est incluse dans \( {A}_{n} \) , donc \( {\Gamma }_{n + 1} \subset {\Gamma }_{n} \) , donc \( {\alpha }_{n + 1} \leq {\alpha }_{n} \) . Autrement dit, la suite \( \left( {\alpha }_{n}\right) \) est décroissante. Comme elle est minorée par 0, elle converge. On note \( \ell \) sa limite.

> Solution. a) Any elementary set included in \( {A}_{n + 1} \) is included in \( {A}_{n} \), therefore \( {\Gamma }_{n + 1} \subset {\Gamma }_{n} \), thus \( {\alpha }_{n + 1} \leq {\alpha }_{n} \). In other words, the sequence \( \left( {\alpha }_{n}\right) \) is decreasing. Since it is bounded below by 0, it converges. We denote its limit by \( \ell \).

Il s’agit de montrer \( \ell = 0 \) . Pour cela, on raisonne par l’absurde en supposant \( \ell > 0 \) . On fixe un nombre réel \( \delta \) tel que \( 0 < \delta < \ell \) . Pour tout \( n \) , il existe une partie \( {E}_{n} \subset {A}_{n} \) élémentaire et fermée, telle que \( m\left( {E}_{n}\right) > {\alpha }_{n} - \delta /{2}^{n} \) . Pour tout \( n \) , l’ensemble

> We must show \( \ell = 0 \). To do this, we reason by contradiction by assuming \( \ell > 0 \). We fix a real number \( \delta \) such that \( 0 < \delta < \ell \). For every \( n \), there exists an elementary and closed set \( {E}_{n} \subset {A}_{n} \) such that \( m\left( {E}_{n}\right) > {\alpha }_{n} - \delta /{2}^{n} \). For every \( n \), the set

\[
{H}_{n} = \mathop{\bigcap }\limits_{{i = 1}}^{n}{E}_{n}
\]

est élémentaire et fermé, et la suite \( \left( {H}_{n}\right) \) est une suite décroissante de fermés. Si on montre que \( {H}_{n} \) est non vide pour tout \( n \) , alors \( { \cap }_{n \in {\mathbb{N}}^{ * }}{H}_{n} \) sera non vide (suite décroissante de compacts non vides), ce qui sera en contradiction avec le fait que

> is elementary and closed, and the sequence \( \left( {H}_{n}\right) \) is a decreasing sequence of closed sets. If we show that \( {H}_{n} \) is non-empty for all \( n \), then \( { \cap }_{n \in {\mathbb{N}}^{ * }}{H}_{n} \) will be non-empty (decreasing sequence of non-empty compact sets), which will contradict the fact that

\[
\mathop{\bigcap }\limits_{{n \in  {\mathbb{N}}^{ * }}}{H}_{n} \subset  \mathop{\bigcap }\limits_{{n \in  {\mathbb{N}}^{ * }}}{A}_{n} = \varnothing
\]

et on en conclura le résultat.

> and we will conclude the result from this.

Soit \( n \in {\mathbb{N}}^{ * } \) . Fixons une partie élémentaire \( E \subset {A}_{n} \) telle que \( m\left( E\right) > \delta \) . On a

> Let \( n \in {\mathbb{N}}^{ * } \). Let us fix an elementary set \( E \subset {A}_{n} \) such that \( m\left( E\right) > \delta \). We have

\[
E \smallsetminus  {H}_{n} = \mathop{\bigcup }\limits_{{i = 1}}^{n}\left( {E \smallsetminus  {E}_{i}}\right) \;\text{ donc }\;m\left( {E \smallsetminus  {H}_{n}}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}m\left( {E \smallsetminus  {E}_{i}}\right) .
\]

(*)

> Or pour tout \( i,1 \leq i \leq n \) ,

However, for every \( i,1 \leq i \leq n \),

\[
m\left( {E \smallsetminus  {E}_{i}}\right)  + m\left( {E}_{i}\right)  = m\left( {E \cup  {E}_{i}}\right)  \leq  {\alpha }_{i}\;\text{ donc }\;m\left( {E \smallsetminus  {E}_{i}}\right)  \leq  {\alpha }_{i} - m\left( {E}_{i}\right)  \leq  \frac{\delta }{{2}^{i}},
\]

ce qui d'après (*) entraîne

> which, according to (*), implies

\[
m\left( {E \smallsetminus  {H}_{n}}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\delta }{{2}^{i}} < \delta .
\]

Ceci entraîne \( {H}_{n} \neq \varnothing \) car \( m\left( E\right) > \delta \) par construction. D’où le résultat.

> This implies \( {H}_{n} \neq \varnothing \) because \( m\left( E\right) > \delta \) by construction. Hence the result.

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , posons \( {g}_{n} = \begin{Vmatrix}{f - {f}_{n}}\end{Vmatrix} \) . On aura prouvé le résultat si on montre

> b) For every \( n \in {\mathbb{N}}^{ * } \), let us set \( {g}_{n} = \begin{Vmatrix}{f - {f}_{n}}\end{Vmatrix} \). We will have proven the result if we show

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}{g}_{n}\left( t\right) {dt} = 0.
\]

\( \left( {* * }\right) \)

> La suite de fonctions \( \left( {g}_{n}\right) \) converge simplement vers 0, et on a \( 0 \leq {g}_{n} \leq {2K} \) sur \( \left\lbrack {a, b}\right\rbrack \) .

The sequence of functions \( \left( {g}_{n}\right) \) converges pointwise to 0, and we have \( 0 \leq {g}_{n} \leq {2K} \) on \( \left\lbrack {a, b}\right\rbrack \).

> Ceci étant, considérons \( \varepsilon > 0 \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on pose

This being said, let us consider \( \varepsilon > 0 \). For every \( n \in {\mathbb{N}}^{ * } \), we set

\[
{A}_{n} = \left\{  {x \in  \left\lbrack  {a, b}\right\rbrack  \mid \exists i \geq  n,{g}_{i}\left( x\right)  \geq  \varepsilon }\right\}  .
\]

La suite \( \left( {A}_{n}\right) \) est décroissante et on a \( { \cap }_{n \in \mathbb{N}}{A}_{n} = \varnothing \) . D’après le résultat de la question a), on peut donc trouver \( N \in {\mathbb{N}}^{ * } \) tel que tout \( n \geq N \) et pour toute partie élémentaire \( E \subset {A}_{n}, m\left( E\right) < \varepsilon \) . Soit \( n \geq N \) , et soit \( s \) une fonction en escalier telle que \( s \leq {g}_{n} \) .

> The sequence \( \left( {A}_{n}\right) \) is decreasing and we have \( { \cap }_{n \in \mathbb{N}}{A}_{n} = \varnothing \). According to the result of question a), we can therefore find \( N \in {\mathbb{N}}^{ * } \) such that for any \( n \geq N \) and for any elementary set \( E \subset {A}_{n}, m\left( E\right) < \varepsilon \). Let \( n \geq N \), and let \( s \) be a step function such that \( s \leq {g}_{n} \).

On pose \( E = \{ x \in \left\lbrack {a, b}\right\rbrack \mid s\left( x\right) \geq \varepsilon \} \) et \( F = \left\lbrack {a, b}\right\rbrack \smallsetminus E \) . Les ensembles \( E \) et \( F \) sont élémentaires (car \( s \) est en escalier). Comme \( E \subset {A}_{n} \) , on a \( m\left( E\right) < \varepsilon \) donc

> Let \( E = \{ x \in \left\lbrack {a, b}\right\rbrack \mid s\left( x\right) \geq \varepsilon \} \) and \( F = \left\lbrack {a, b}\right\rbrack \smallsetminus E \) be given. The sets \( E \) and \( F \) are elementary (since \( s \) is a step function). As \( E \subset {A}_{n} \) , we have \( m\left( E\right) < \varepsilon \) therefore

\[
{\int }_{a}^{b}s\left( t\right) {dt} = {\int }_{E}s + {\int }_{F}s \leq  {\int }_{E}{2K} + {\int }_{F}\varepsilon  \leq  {2Km}\left( E\right)  + \left( {b - a}\right) \varepsilon  \leq  {M\varepsilon },\;M = {2K} + \left( {b - a}\right) .
\]

Ceci étant vrai pour toute fonction en escalier \( s \) inférieure à la fonction continue par morceaux \( {g}_{n} \) , on en déduit \( {\int }_{a}^{b}{g}_{n}\left( t\right) {dt} \leq {M\varepsilon } \) . Ceci étant vrai pour tout \( n \geq N \) , on en déduit (**).

> Since this is true for any step function \( s \) less than the piecewise continuous function \( {g}_{n} \) , we deduce \( {\int }_{a}^{b}{g}_{n}\left( t\right) {dt} \leq {M\varepsilon } \) . Since this is true for any \( n \geq N \) , we deduce (**).

c) On reprend les notations du théorème de convergence dominée page 151. Soit \( \varepsilon > 0 \) , et soit un segment \( J = \left\lbrack {a, b}\right\rbrack \) inclus dans \( I \) tel que \( {\int }_{I \smallsetminus J}\varphi = {\int }_{I}\varphi - {\int }_{J}\varphi < \varepsilon \) . D’après le résultat de la question précédente appliqué au segment \( J \) (que l’on peut bien appliquer car \( \varphi \) est bornée sur cet intervalle) il existe \( N \in {\mathbb{N}}^{ * } \) tel que \( \begin{Vmatrix}{{\int }_{J}{f}_{n} - {\int }_{J}f}\end{Vmatrix} < \varepsilon \) pour tout \( n \geq N \) . Ainsi, pour tout \( n \geq N \) on a

> c) We use the notation from the dominated convergence theorem on page 151. Let \( \varepsilon > 0 \) , and let a segment \( J = \left\lbrack {a, b}\right\rbrack \) be included in \( I \) such that \( {\int }_{I \smallsetminus J}\varphi = {\int }_{I}\varphi - {\int }_{J}\varphi < \varepsilon \) . According to the result of the previous question applied to the segment \( J \) (which can indeed be applied because \( \varphi \) is bounded on this interval) there exists \( N \in {\mathbb{N}}^{ * } \) such that \( \begin{Vmatrix}{{\int }_{J}{f}_{n} - {\int }_{J}f}\end{Vmatrix} < \varepsilon \) for all \( n \geq N \) . Thus, for all \( n \geq N \) we have

\[
\begin{Vmatrix}{{\int }_{I}{f}_{n} - {\int }_{I}f}\end{Vmatrix} \leq  \begin{Vmatrix}{{\int }_{I}{f}_{n} - {\int }_{J}{f}_{n}}\end{Vmatrix} + \begin{Vmatrix}{{\int }_{J}{f}_{n} - {\int }_{J}f}\end{Vmatrix} + \begin{Vmatrix}{{\int }_{J}f - {\int }_{I}f}\end{Vmatrix} \leq  {\int }_{I \smallsetminus  J}\varphi  + \varepsilon  + {\int }_{I \smallsetminus  J}\varphi  \leq  {3\varepsilon },
\]

d'où le résultat.

> whence the result.

Remarque. On adapte facilement cette démonstration dans les cas où les \( {f}_{n} \) et \( f \) sont seulement supposées Riemann-intégrables.

> Remark. This proof is easily adapted to cases where \( {f}_{n} \) and \( f \) are only assumed to be Riemann-integrable.
