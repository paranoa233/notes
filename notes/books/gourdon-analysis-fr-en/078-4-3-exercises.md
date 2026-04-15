#### 4.3. Exercises

*Français : 4.3. Exercices*

\( \rightarrow \) EXERCICE 1. On considère une application \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) strictement croissante telle que \( f\left( 0\right) = 0 \) et \( f\left( 1\right) = 1 \) . Montrer que

> \( \rightarrow \) EXERCISE 1. Consider a strictly increasing mapping \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) such that \( f\left( 0\right) = 0 \) and \( f\left( 1\right) = 1 \) . Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{0}^{1}f{\left( t\right) }^{n}{dt} = 0.
\]

---

Solution. C'est classique. On procède comme suit.

> Solution. This is a classic. We proceed as follows.

Comme \( f \) est strictement croissante sur \( \left\lbrack {0,1}\right\rbrack \) , on a \( 0 = f\left( 0\right) \leq f\left( x\right) < f\left( 1\right) = 1 \) pour \( 0 \leq x < 1 \) . Ainsi, la suite de fonctions \( \left( {f}^{n}\right) \) converge simplement vers la fonction \( \varphi \) définie par \( \varphi \left( t\right) = 0 \) pour \( t \in \left\lbrack {0,1\lbrack }\right. \) et \( \varphi \left( 1\right) = 1 \) . Par ailleurs, on a la majoration \( 0 \leq {f}^{n} \leq 1 \) indépendante de \( n \) . On peut donc appliquer le théorème de convergence dominée, qui assure la converge de \( {\int }_{0}^{1}f{\left( t\right) }^{n}{dt} \) vers \( {\int }_{0}^{1}\varphi \left( t\right) {dt} = 0. \)

> Since \( f \) is strictly increasing on \( \left\lbrack {0,1}\right\rbrack \) , we have \( 0 = f\left( 0\right) \leq f\left( x\right) < f\left( 1\right) = 1 \) for \( 0 \leq x < 1 \) . Thus, the sequence of functions \( \left( {f}^{n}\right) \) converges pointwise to the function \( \varphi \) defined by \( \varphi \left( t\right) = 0 \) for \( t \in \left\lbrack {0,1\lbrack }\right. \) and \( \varphi \left( 1\right) = 1 \) . Furthermore, we have the bound \( 0 \leq {f}^{n} \leq 1 \) independent of \( n \) . We can therefore apply the dominated convergence theorem, which ensures the convergence of \( {\int }_{0}^{1}f{\left( t\right) }^{n}{dt} \) to \( {\int }_{0}^{1}\varphi \left( t\right) {dt} = 0. \)

---

EXERCICE 2 (INTÉGRALE DE GAUSS : \( {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} \) ). Le but de l’exercice est de donner deux méthodes pour calculer l'intégrale de Gauss

> EXERCISE 2 (GAUSSIAN INTEGRAL: \( {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} \) ). The goal of the exercise is to provide two methods for calculating the Gaussian integral

\[
I = {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt}
\]

1/ (Première méthode.) Exprimer l'application

> 1/ (First method.) Express the mapping

\[
g : \left\lbrack  {0, + \infty \left\lbrack  { \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{0}^{1}\frac{{e}^{-\left( {{t}^{2} + 1}\right) {x}^{2}}}{{t}^{2} + 1}{dt}}\right. }\right.
\]

en fonction de \( x \mapsto {\int }_{0}^{x}{e}^{-{t}^{2}}{dt} \) . En déduire \( I \) .

> in terms of \( x \mapsto {\int }_{0}^{x}{e}^{-{t}^{2}}{dt} \) . Deduce \( I \) .

2/ (Seconde méthode.) Soit \( n \in {\mathbb{N}}^{ * } \) . Pour tout \( t \in \left\lbrack {0,\sqrt{n}}\right\rbrack \) , montrer

> 2/ (Second method.) Let \( n \in {\mathbb{N}}^{ * } \) . For all \( t \in \left\lbrack {0,\sqrt{n}}\right\rbrack \) , show

\[
{\left( 1 - \frac{{t}^{2}}{n}\right) }^{n} \leq  {e}^{-{t}^{2}} \leq  {\left( 1 + \frac{{t}^{2}}{n}\right) }^{-n}.
\]

En déduire \( I \) en utilisant les intégrales de Wallis.

> Deduce \( I \) using Wallis integrals.

Solution. 1/ La fonction

> Solution. 1/ The function

\[
\left\lbrack  {0, + \infty \left\lbrack  {\times \left\lbrack  {0,1}\right\rbrack  \;\left( {x, t}\right)  \mapsto  \frac{{e}^{-\left( {{t}^{2} + 1}\right) {x}^{2}}}{{t}^{2} + 1}}\right\rbrack  }\right.
\]

admet une dérivée partielle par rapport à \( x \) continue. On en déduit (théorème de dérivabilité sous le signe intégral, et plus précisément le corollaire 1 page 162) que \( g \) est dérivable et que

> admits a continuous partial derivative with respect to \( x \) . We deduce (theorem of differentiability under the integral sign, and more precisely corollary 1 page 162) that \( g \) is differentiable and that

\[
\forall x \geq  0,\;{g}^{\prime }\left( x\right)  =  - {2x}{\int }_{0}^{1}{e}^{-\left( {{t}^{2} + 1}\right) {x}^{2}}{dt} =  - {2x}{e}^{-{x}^{2}}{\int }_{0}^{1}{e}^{-{\left( tx\right) }^{2}}{dt},
\]

ce qui, après le changement de variable \( u = {tx} \) donne

> which, after the change of variable \( u = {tx} \) gives

\[
{g}^{\prime }\left( x\right)  =  - 2{e}^{-{x}^{2}}{\int }_{0}^{x}{e}^{-{u}^{2}}{du} =  - 2{f}^{\prime }\left( x\right) f\left( x\right) \;\text{ avec }\;f : x \mapsto  {\int }_{0}^{x}{e}^{-{u}^{2}}{du}.
\]

En intégrant, on en déduit

> By integrating, we deduce

\[
\forall x \geq  0,\;g\left( x\right)  - g\left( 0\right)  =  - \left( {{f}^{2}\left( x\right)  - {f}^{2}\left( 0\right) }\right) \;\text{ donc }\;g\left( x\right)  = \frac{\pi }{4} - {f}^{2}\left( x\right) .
\]

(*)

> Les inégalités

The inequalities

\[
0 \leq  g\left( x\right)  \leq  {e}^{-{x}^{2}}{\int }_{0}^{1}\frac{dt}{1 + {t}^{2}}\;\text{ entraînent }\;\mathop{\lim }\limits_{{x \rightarrow   + \infty }}g\left( x\right)  = 0,
\]

et la fonction \( f \) étant positive, on en déduit avec (*) que

> and the function \( f \) being positive, we deduce with (*) that

\[
\mathop{\lim }\limits_{{x \rightarrow   + \infty }}f\left( x\right)  = \sqrt{\frac{\pi }{4}}\;\text{ ce qui s’écrit }\;I = {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} = \frac{\sqrt{\pi }}{2}.
\]

2/ La fonction logarithme est concave, elle se trouve donc en dessous de sa tangente en 1, ce qui s’écrit log \( \left( {1 + x}\right) \leq x \) pour \( x > - 1 \) . En particulier pour tout \( n \in {\mathbb{N}}^{ * } \) on a

> 2/ The logarithm function is concave, it therefore lies below its tangent at 1, which is written log \( \left( {1 + x}\right) \leq x \) for \( x > - 1 \) . In particular for all \( n \in {\mathbb{N}}^{ * } \) we have

\[
\forall t \in  \left\lbrack  {0,\sqrt{n}\left\lbrack  \right. ,\;\log \left( {1 - \frac{{t}^{2}}{n}}\right)  \leq   - \frac{{t}^{2}}{n}\;\text{ et }\;\log \left( {1 + \frac{{t}^{2}}{n}}\right)  \leq  \frac{{t}^{2}}{n}.}\right.
\]

En multipliant respectivement par \( n \) et \( - n \) puis en prenant l’exponentielle, on en déduit

> By multiplying respectively by \( n \) and \( - n \) then taking the exponential, we deduce

\[
\forall t \in  \left\lbrack  {0,\sqrt{n}\left\lbrack  {,\;{\left( 1 - \frac{{t}^{2}}{n}\right) }^{n} \leq  {e}^{-{t}^{2}} \leq  {\left( 1 + \frac{{t}^{2}}{n}\right) }^{-n}.}\right. }\right.
\]

On a donc

> We therefore have

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\int }_{0}^{\sqrt{n}}{\left( 1 - \frac{{t}^{2}}{n}\right) }^{n}{dt} \leq  {\int }_{0}^{\sqrt{n}}{e}^{-{t}^{2}}{dt} \leq  {\int }_{0}^{+\infty }{\left( 1 + \frac{{t}^{2}}{n}\right) }^{-n}{dt}.
\]

En effectuant le changement de variable \( t = \sqrt{n}\cos u \) dans le membre de gauche et \( t = \sqrt{n}\operatorname{cotan}u \) dans le membre de droite, cette dernière assertion s'écrit aussi

> By performing the change of variable \( t = \sqrt{n}\cos u \) in the left member and \( t = \sqrt{n}\operatorname{cotan}u \) in the right member, this last assertion is also written

\[
\forall n \in  {\mathbb{N}}^{ * },\;\sqrt{n}{\int }_{0}^{\pi /2}{\sin }^{{2n} + 1}{udu} \leq  {\int }_{0}^{\sqrt{n}}{e}^{-{t}^{2}}{dt} \leq  \sqrt{n}{\int }_{0}^{\pi /2}{\sin }^{{2n} - 2}{udu}.
\]

(**)

> Les intégrales de Wallis vérifient l'équivalent (voir l'exercice 1 page 130)

Wallis integrals satisfy the equivalent (see exercise 1 page 130)

\[
{\int }_{0}^{\pi /2}{\sin }^{n}{udu} \sim  \sqrt{\frac{\pi }{2n}}\text{ lorsque }n \rightarrow   + \infty .
\]

Ceci montre que les deux termes extrêmes de (**) tendent vers \( \sqrt{\pi }/2 \) lorsque \( n \rightarrow + \infty \) , et on en déduit en faisant tendre \( n \) vers l’infini dans (**) que

> This shows that the two extreme terms of (**) tend to \( \sqrt{\pi }/2 \) when \( n \rightarrow + \infty \) , and we deduce by letting \( n \) tend to infinity in (**) that

\[
I = {\int }_{0}^{+\infty }{e}^{-{t}^{2}}{dt} = \mathop{\lim }\limits_{{x \rightarrow   + \infty }}{\int }_{0}^{\sqrt{x}}{e}^{-{t}^{2}}{dt} = \frac{\sqrt{\pi }}{2}.
\]

Remarque. Il existe d'autres moyens de calculer cette intégrale (voir l'exemple 2 page 355 par exemple).

> Remark. There are other ways to calculate this integral (see example 2 page 355 for instance).

EXERCICE 3. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{\infty } \) nulle en 0 . Montrer que l'application

> EXERCISE 3. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{\infty } \) vanishing at 0 . Show that the mapping

\[
g : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \left\{  \begin{array}{ll} f\left( x\right) /x & \text{ si }x \neq  0 \\  {f}^{\prime }\left( 0\right) & \text{ si }x = 0 \end{array}\right.
\]

est de classe \( {\mathcal{C}}^{\infty } \) .

> is of class \( {\mathcal{C}}^{\infty } \) .

Solution. Comme \( f\left( 0\right) = 0 \) , on a \( f\left( x\right) = {\int }_{0}^{x}{f}^{\prime }\left( t\right) {dt} \) pour tout \( x \in \mathbb{R} \) . Pour \( x \) fixé, le changement de variable \( t = {\lambda x} \) fournit

> Solution. Since \( f\left( 0\right) = 0 \) , we have \( f\left( x\right) = {\int }_{0}^{x}{f}^{\prime }\left( t\right) {dt} \) for all \( x \in \mathbb{R} \) . For a fixed \( x \) , the change of variable \( t = {\lambda x} \) provides

\[
f\left( x\right)  = x{\int }_{0}^{1}{f}^{\prime }\left( {\lambda x}\right) {d\lambda }\;\text{ donc }\;g\left( x\right)  = {\int }_{0}^{1}{f}^{\prime }\left( {\lambda x}\right) {d\lambda }.
\]

La fonction \( {f}^{\prime } \) étant de classe \( {\mathcal{C}}^{\infty } \) , on en déduit en appliquant par récurrence le théorème de dérivation sous le signe intégral, que \( g \) est de classe \( {\mathcal{C}}^{\infty } \) .

> Since the function \( {f}^{\prime } \) is of class \( {\mathcal{C}}^{\infty } \) , we deduce by applying the theorem of differentiation under the integral sign by induction that \( g \) is of class \( {\mathcal{C}}^{\infty } \) .

Remarque. Ce résultat est un cas particulier du lemme d’Hadamard lorsque \( n = 1 \) (voir l'exercice 4 page 331).

> Remark. This result is a special case of Hadamard's lemma when \( n = 1 \) (see exercise 4 on page 331).

EXERCICE 4. 1 / Calculer, pour tout \( x \geq 0 \) , la valeur de l’intégrale

> EXERCISE 4. 1 / Calculate, for all \( x \geq 0 \) , the value of the integral

\[
I\left( x\right)  = {\int }_{0}^{+\infty }\frac{\sin \left( {xt}\right) }{t}{e}^{-t}{dt}.
\]

\( 2/ \) a) Soit \( \alpha > 0 \) . Calculer, pour tout \( x \geq 0 \) , la valeur de

> \( 2/ \) a) Let \( \alpha > 0 \) . Calculate, for all \( x \geq 0 \) , the value of

\[
I\left( x\right)  = {\int }_{0}^{+\infty }{e}^{-t}{e}^{ixt}{t}^{\alpha  - 1}{dt}
\]

(on exprimera \( I \) en fonction de \( \Gamma \left( x\right) = {\int }_{0}^{+\infty }{t}^{x - 1}{e}^{-t}{dt} \) ).

> (express \( I \) in terms of \( \Gamma \left( x\right) = {\int }_{0}^{+\infty }{t}^{x - 1}{e}^{-t}{dt} \) ).

b) En déduire, pour tout \( \alpha \in \rbrack 0,1\left\lbrack \text{ , la valeur de }\right. \)

> b) Deduce, for all \( \alpha \in \rbrack 0,1\left\lbrack \text{ , la valeur de }\right. \)

\[
J\left( \alpha \right)  = {\int }_{0}^{+\infty }{t}^{\alpha  - 1}{e}^{it}{dt}
\]

3/ Pour tout \( x \geq 0 \) , calculer

> 3/ For all \( x \geq 0 \) , calculate

\[
I\left( x\right)  = {\int }_{-\infty }^{+\infty }{e}^{-{t}^{2}}{e}^{2i\pi tx}{dt}
\]

Solution. L'idée est de trouver une équation différentielle vérifiée par chacune de ces intégrales puis de la résoudre pour exprimer explicitement l'intégrale correspondante.

> Solution. The idea is to find a differential equation satisfied by each of these integrals and then solve it to explicitly express the corresponding integral.

1 / L’intégrande est bien intégrable sur ] \( 0, + \infty \) [ (elle est égale à \( x + o\left( 1\right) \) lorsque \( t \rightarrow 0 \) ). La dérivée de l’intégrande par rapport à \( x \) est \( {e}^{-t}\cos {xt} \) , dont la valeur absolue est majorée indépendamment de \( x \) par \( {e}^{-t} \) , intégrable sur \( \rbrack 0, + \infty \lbrack \) . En vertu du théorème de dérivation sous le signe intégral, on en déduit que \( I \) est dérivable et que

> 1 / The integrand is indeed integrable on ] \( 0, + \infty \) [ (it is equal to \( x + o\left( 1\right) \) when \( t \rightarrow 0 \) ). The derivative of the integrand with respect to \( x \) is \( {e}^{-t}\cos {xt} \) , whose absolute value is bounded independently of \( x \) by \( {e}^{-t} \) , which is integrable on \( \rbrack 0, + \infty \lbrack \) . By virtue of the theorem of differentiation under the integral sign, we deduce that \( I \) is differentiable and that

\[
\forall x \in  {\mathbb{R}}^{ + },\;{I}^{\prime }\left( x\right)  = {\int }_{0}^{+\infty }{e}^{-t}\cos {xtdt} = \Re \left( {{\int }_{0}^{+\infty }{e}^{-t + {ixt}}{dt}}\right)  = \Re \left( \frac{1}{1 - {ix}}\right)  = \frac{1}{1 + {x}^{2}}.
\]

On en déduit

> We deduce

\[
\forall x \in  {\mathbb{R}}^{ + },\;I\left( x\right)  = I\left( 0\right)  + {\int }_{0}^{x}\frac{dt}{1 + {t}^{2}} = \arctan x.
\]

2/ a) En procédant comme dans la solution de la question précédente, on montre que \( I \) est dérivable et que

> 2/ a) By proceeding as in the solution to the previous question, we show that \( I \) is differentiable and that

\[
\forall x \in  {\mathbb{R}}^{ + },\;{I}^{\prime }\left( x\right)  = i{\int }_{0}^{+\infty }{e}^{-t}{e}^{ixt}{t}^{\alpha }{dt}.
\]

Par ailleurs, une intégration par parties donne

> Furthermore, integration by parts gives

\[
\forall x \geq  0,\;I\left( x\right)  = {\left\lbrack  {e}^{\left( {-1 + {ix}}\right) t} \cdot  \frac{{t}^{\alpha }}{\alpha }\right\rbrack  }_{0}^{+\infty } - \left( \frac{-1 + {ix}}{\alpha }\right) {\int }_{0}^{+\infty }{e}^{-t}{e}^{ixt}{t}^{\alpha }{dt} =  - \frac{i + x}{\alpha }{I}^{\prime }\left( x\right) .
\]

Cette équation différentielle vérifée par \( I \) s’intègre, compte tenu du fait que

> This differential equation satisfied by \( I \) can be integrated, taking into account the fact that

\[
\int \frac{dx}{i + x} = \int \frac{x - i}{{x}^{2} + 1}{dx} = \frac{1}{2}\log \left( {{x}^{2} + 1}\right)  - i\arctan x + k,\;k \in  \mathbb{C},
\]

et on tire

> and we obtain

\[
\exists C \in  \mathbb{C},\;I\left( x\right)  = C\exp \left\lbrack  {-\alpha \left( {\frac{1}{2}\log \left( {{x}^{2} + 1}\right)  - i\arctan x}\right) }\right\rbrack   = C{\left( {x}^{2} + 1\right) }^{-\alpha /2}{e}^{{i\alpha }\arctan x}.
\]

Or \( I\left( 0\right) = C = \Gamma \left( \alpha \right) \) , donc finalement

> Or \( I\left( 0\right) = C = \Gamma \left( \alpha \right) \) , so finally

\[
\forall x \in  {\mathbb{R}}^{ + },\;I\left( x\right)  = \Gamma \left( \alpha \right) {\left( {x}^{2} + 1\right) }^{-\alpha /2}{e}^{{i\alpha }\arctan x}.
\]

b) Le changement de variable \( u = {xt} \) dans l’intégrale définissant \( I\left( x\right) \) donne

> b) The change of variable \( u = {xt} \) in the integral defining \( I\left( x\right) \) gives

\[
\forall x > 0,\;I\left( x\right)  = \frac{1}{{x}^{\alpha }}{\int }_{0}^{+\infty }{e}^{-u/x}{e}^{iu}{u}^{\alpha  - 1}{du}.
\]

Lorsque \( x \rightarrow + \infty \) , on a \( {e}^{-u/x} \rightarrow 1 \) et on s’attend à ce que la dernière intégrale tende vers \( J\left( x\right) \) . C'est ce dernier point que nous montrons maintenant. On ne peut pas ici utiliser directement le théorème de continuité sous le signe intégral sur tout le domaine d'intégration. Définissons la fonction

> When \( x \rightarrow + \infty \) , we have \( {e}^{-u/x} \rightarrow 1 \) and we expect the last integral to tend to \( J\left( x\right) \) . It is this last point that we now demonstrate. We cannot directly use the theorem of continuity under the integral sign over the entire domain of integration here. Let us define the function

\[
\widetilde{I} : {\mathbb{R}}^{ + } \rightarrow  \mathbb{C}\;y \mapsto  {\int }_{0}^{+\infty }{e}^{-{uy}}{e}^{iu}{u}^{\alpha  - 1}{du}.
\]

Pour \( y > 0 \) , l’existence de \( \widetilde{I}\left( y\right) \) est immédiate. Pour \( y = 0 \) , son existence est une conséquence de la règle d’Abel (voir le théorème 5 page 152). Pour montrer la continuité de \( \widetilde{I} \) en 0, on va montrer que \( \widetilde{I} \) est limite uniforme de fonctions continues. On considère la suite de fonctions \( \left( {\widetilde{I}}_{n}\right) \) définie par

> For \( y > 0 \) , the existence of \( \widetilde{I}\left( y\right) \) is immediate. For \( y = 0 \) , its existence is a consequence of Abel's rule (see theorem 5 on page 152). To show the continuity of \( \widetilde{I} \) at 0, we will show that \( \widetilde{I} \) is the uniform limit of continuous functions. We consider the sequence of functions \( \left( {\widetilde{I}}_{n}\right) \) defined by

\[
\forall n \in  {\mathbb{N}}^{ * },\forall y \geq  0,\;{\widetilde{I}}_{n}\left( y\right)  = {\int }_{1/n}^{n}{e}^{-{uy}}{e}^{iu}{u}^{\alpha  - 1}{du}.
\]

La seconde formule de la moyenne donne

> The second mean value theorem gives

\[
\forall n \in  {\mathbb{N}}^{ * },\forall y \geq  0,\forall X > n,\exists a, b \geq  n,
\]

\[
{\int }_{n}^{X}{e}^{-{uy}}{e}^{iu}{u}^{\alpha  - 1}{du} = {e}^{-{ny}}\left( {{\int }_{n}^{a}\cos u{u}^{\alpha  - 1}{du} + i{\int }_{n}^{b}\sin u{u}^{\alpha  - 1}{du}}\right)
\]

donc pour tout \( n \in {\mathbb{N}}^{ * } \) et pour tout \( y \geq 0 \) ,

> so for all \( n \in {\mathbb{N}}^{ * } \) and for all \( y \geq 0 \) ,

\[
\left| {{\widetilde{I}}_{n}\left( y\right)  - \widetilde{I}\left( y\right) }\right|  \leq  {\int }_{0}^{1/n}{u}^{\alpha  - 1}{du} + \mathop{\sup }\limits_{{t \geq  n}}\left| {{\int }_{n}^{t}\cos u{u}^{\alpha  - 1}{du}}\right|  + \mathop{\sup }\limits_{{t \geq  n}}\left| {{\int }_{n}^{t}\sin u{u}^{\alpha  - 1}{du}}\right| ,
\]

et on en déduit que \( \left( {\widetilde{I}}_{n}\right) \) converge uniformément vers \( \widetilde{I} \) sur \( {\mathbb{R}}^{ + } \) . Le théorème de continuité sous le signe intégral assure la continuité de \( {\widetilde{I}}_{n} \) en 0 pour tout \( n \in {\mathbb{N}}^{ * } \) , donc \( \widetilde{I} \) , limite uniforme de fonctions continues sur \( {\mathbb{R}}^{ + } \) , est continue sur \( {\mathbb{R}}^{ + } \) . En particulier, \( \widetilde{I} \) est continue en \( {0}^{ + } \) ce qui s'écrit aussi

> and we deduce that \( \left( {\widetilde{I}}_{n}\right) \) converges uniformly to \( \widetilde{I} \) on \( {\mathbb{R}}^{ + } \) . The theorem of continuity under the integral sign ensures the continuity of \( {\widetilde{I}}_{n} \) at 0 for all \( n \in {\mathbb{N}}^{ * } \) , so \( \widetilde{I} \) , the uniform limit of continuous functions on \( {\mathbb{R}}^{ + } \) , is continuous on \( {\mathbb{R}}^{ + } \) . In particular, \( \widetilde{I} \) is continuous at \( {0}^{ + } \) which is also written as

\[
\mathop{\lim }\limits_{{x \rightarrow   + \infty }}{x}^{\alpha }I\left( x\right)  = J\left( \alpha \right)
\]

et d'après le résultat de la question précédente on en déduit

> and according to the result of the previous question we deduce

\[
J\left( \alpha \right)  = \Gamma \left( \alpha \right) {e}^{{i\alpha \pi }/2}.
\]

3/ En procédant comme dans la solution de la question1/, on montre que \( I \) est dérivable et que

> 3/ By proceeding as in the solution to question 1/, we show that \( I \) is differentiable and that

\[
\forall x \in  {\mathbb{R}}^{ + },\;{I}^{\prime }\left( x\right)  = {2i\pi }{\int }_{-\infty }^{+\infty }t{e}^{-{t}^{2}}{e}^{2i\pi tx}{dt}.
\]

Par ailleurs, une intégration par parties donne

> Furthermore, integration by parts gives

\[
\forall x \geq  0,\;I\left( x\right)  = {\left\lbrack  \frac{1}{2i\pi x}{e}^{-{t}^{2}}{e}^{2i\pi xt}\right\rbrack  }_{-\infty }^{+\infty } + \frac{1}{2i\pi x}{\int }_{-\infty }^{+\infty }{2t}{e}^{-{t}^{2}}{e}^{2i\pi xt}{dt} = \frac{1}{i\pi x}\frac{1}{2i\pi }{I}^{\prime }\left( x\right) .
\]

En résolvant cette équation différentielle vérifiée par \( I \) , on trouve

> By solving this differential equation satisfied by \( I \) , we find

\[
\forall x \geq  0,\;I\left( x\right)  = I\left( 0\right) {e}^{-{\pi }^{2}{x}^{2}}.
\]

La constante \( I\left( 0\right) \) est calculable : elle vaut \( \sqrt{\pi } \) (voir l’exercice 2).

> The constant \( I\left( 0\right) \) is computable: it is equal to \( \sqrt{\pi } \) (see exercise 2).

EXERCICE 5. Pour tout \( t > 0 \) , on pose

> EXERCISE 5. For all \( t > 0 \) , we define

\[
I\left( t\right)  = {\int }_{1}^{+\infty }\frac{{e}^{-{tx}}}{\sqrt[3]{{x}^{3} + 1}}{dx}.
\]

Donner un équivalent de \( I\left( t\right) \) lorsque \( t \) tend vers \( {0}^{ + } \) .

> Give an equivalent of \( I\left( t\right) \) when \( t \) tends to \( {0}^{ + } \) .

Solution. La convergence de l’intégrale donnant \( I\left( t\right) \) pour tout \( t > 0 \) est immédiate. Pour trouver son équivalent lorsque \( t \rightarrow {0}^{ + } \) il est commode de commencer par effectuer le changement de variable \( u = {tx} \) (ceci pour localiser la zone qui contribue au terme dominant de l’intégrale), ce qui donne

> Solution. The convergence of the integral giving \( I\left( t\right) \) for all \( t > 0 \) is immediate. To find its equivalent when \( t \rightarrow {0}^{ + } \) it is convenient to start by performing the change of variable \( u = {tx} \) (this is to locate the zone that contributes to the dominant term of the integral), which gives

\[
\forall t > 0,\;I\left( t\right)  = {\int }_{t}^{+\infty }\frac{{e}^{-u}}{\sqrt[3]{{u}^{3} + {t}^{3}}}{du}.
\]

Lorsque \( t \rightarrow {0}^{ + } \) , la contribution prépondérante de l’intégrale se produit lorsque \( u \) est proche de \( t \) . Dans cette zone, l’intégrande se comporte comme \( {\left( {u}^{3} + {t}^{3}\right) }^{-1/3} \) . Lorsque \( u \) est proche de 0 mais grand par rapport à \( t \) , la contribution de ce terme reste significative, et il est alors bien approché par \( 1/u \) . On s’attend par conséquent à ce que \( I\left( t\right) \) soit équivalent à \( {\int }_{t}^{1}{du}/u = - \log t \) . C'est ce que nous allons montrer rigoureusement dans les lignes qui suivent.

> When \( t \rightarrow {0}^{ + } \), the dominant contribution to the integral occurs when \( u \) is close to \( t \). In this region, the integrand behaves like \( {\left( {u}^{3} + {t}^{3}\right) }^{-1/3} \). When \( u \) is close to 0 but large compared to \( t \), the contribution of this term remains significant, and it is then well approximated by \( 1/u \). We therefore expect \( I\left( t\right) \) to be equivalent to \( {\int }_{t}^{1}{du}/u = - \log t \). This is what we will show rigorously in the following lines.

Pour tout \( t > 0 \) , on écrit

> For any \( t > 0 \), we write

\[
I\left( t\right)  - {\int }_{t}^{1}\frac{du}{u} = \underset{{I}_{1}\left( t\right) }{\underbrace{{\int }_{t}^{1}\left( {\frac{1}{{\left( {u}^{3} + {t}^{3}\right) }^{1/3}} - \frac{1}{u}}\right) {du}}} + \underset{{I}_{2}\left( t\right) }{\underbrace{{\int }_{t}^{1}\frac{{e}^{-u} - 1}{{\left( {u}^{3} + {t}^{3}\right) }^{1/3}}{du}}} + \underset{{I}_{3}\left( t\right) }{\underbrace{{\int }_{1}^{+\infty }\frac{{e}^{-u}}{{\left( {u}^{3} + {t}^{3}\right) }^{1/3}}{du}}}.
\]

(*)

> Nous allons prouver que les intégrales \( {I}_{1}\left( t\right) ,{I}_{2}\left( t\right) \) et \( {I}_{3}\left( t\right) \) du second membre de cette égalité sont bornées lorsque \( t \rightarrow {0}^{ + } \) . Pour les deux dernières c’est facile car il suffit d’écrire (compte tenu de la classique inégalité \( 1 - {e}^{-u} \leq u \) )

We will prove that the integrals \( {I}_{1}\left( t\right) ,{I}_{2}\left( t\right) \) and \( {I}_{3}\left( t\right) \) on the right-hand side of this equality are bounded as \( t \rightarrow {0}^{ + } \). For the last two, it is easy because it suffices to write (given the classic inequality \( 1 - {e}^{-u} \leq u \))

\[
\left| {{I}_{2}\left( t\right) }\right|  \leq  {\int }_{t}^{1}\frac{u}{{\left( {u}^{3} + {t}^{3}\right) }^{1/3}}{du} \leq  {\int }_{t}^{1}{du} \leq  1\;\text{ et }\;\left| {{I}_{3}\left( t\right) }\right|  \leq  {\int }_{1}^{+\infty }{e}^{-u}{du} = 1.
\]

Pour l’intégrale \( {I}_{1}\left( t\right) \) on écrit

> For the integral \( {I}_{1}\left( t\right) \) we write

\[
\forall t > 0,\;\left| {{I}_{1}\left( t\right) }\right|  = {\int }_{t}^{1}\frac{1}{u}\left( {1 - {\left( 1 + \frac{t}{u}\right) }^{-1/3}}\right) {du},
\]

et compte tenu du fait que \( 1 - {\left( 1 + x\right) }^{-1/3} \leq x/3 \) pour tout \( x \geq 0 \) (inégalité que l’on obtient par exemple en utilisant la convexité de la fonction \( x \mapsto {\left( 1 + x\right) }^{-1/3} \) ), on a

> and given the fact that \( 1 - {\left( 1 + x\right) }^{-1/3} \leq x/3 \) for all \( x \geq 0 \) (an inequality obtained for example by using the convexity of the function \( x \mapsto {\left( 1 + x\right) }^{-1/3} \) ), we have

\[
\forall t > 0,\;\left| {{I}_{1}\left( t\right) }\right|  \leq  {\int }_{t}^{1}\frac{1}{u}\frac{t}{3u}{du} = \frac{t}{3}{\int }_{t}^{1}\frac{du}{{u}^{2}} = \frac{1}{3}.
\]

Ainsi nous avons montré \( {I}_{1}\left( t\right) + {I}_{2}\left( t\right) + {I}_{3}\left( t\right) = O\left( 1\right) \) lorsque \( t \rightarrow {0}^{ + } \) , donc grâce à \( \left( *\right) \) on en déduit

> Thus we have shown \( {I}_{1}\left( t\right) + {I}_{2}\left( t\right) + {I}_{3}\left( t\right) = O\left( 1\right) \) as \( t \rightarrow {0}^{ + } \) , so thanks to \( \left( *\right) \) we deduce

\[
I\left( t\right)  + \log t = O\left( 1\right) \text{ donc }I\left( t\right)  =  - \log t + O\left( 1\right)  \sim   - \log t\text{ lorsque }t \rightarrow  {0}^{ + }.
\]

EXERCICE 6. 1/ Donner un équivalent, lorsque \( t \rightarrow + \infty \) de

> EXERCISE 6. 1/ Find an equivalent, as \( t \rightarrow + \infty \) of

\[
\text{ a) }I\left( t\right)  = {\int }_{0}^{+\infty }{x}^{-{\alpha x}}{t}^{x}{dx}\;\left( {\alpha  > 0}\right) \;\mathbf{b})\;I\left( t\right)  = {\int }_{0}^{\pi }\left( {\sin x}\right) {x}^{t}{dx}
\]

(on pourra utiliser le théorème 4 page 164 sur la méthode de Laplace).

> (one may use theorem 4 on page 164 regarding Laplace's method).

2 / Donner un équivalent, lorsque \( t \rightarrow {0}^{ + } \) , de

> 2 / Find an equivalent, as \( t \rightarrow {0}^{ + } \) , of

\[
I\left( t\right)  = {\int }_{0}^{+\infty }\exp \left( {\frac{{x}^{\alpha }}{\alpha } - {tx}}\right) {dx}\;\left( {0 < \alpha  < 1}\right) .
\]

---

Solution. 1/ a) On ne peut pas appliquer tel que le théorème 4 car dans l’expression \( {t}^{x} = {e}^{\left( {\log t}\right) x} \) , la fonction dans l’exponentielle est croissante en \( x \) . On procède comme il est indiqué dans le commentaire du corollaire 2.

> Solution. 1/ a) We cannot apply theorem 4 as is because in the expression \( {t}^{x} = {e}^{\left( {\log t}\right) x} \) , the function in the exponential is increasing in \( x \) . We proceed as indicated in the commentary of corollary 2.

On écrit \( {x}^{-{\alpha x}}{t}^{x} = \exp \left( {f\left( x\right) }\right) \) où \( f\left( x\right) = \log t \cdot x - {\alpha x}\log x \) . Comme \( f\left( x\right) \rightarrow - \infty \) lorsque \( x \rightarrow + \infty \) , l’intégrale \( I\left( t\right) \) converge. Cherchons l’abscisse \( x \) du maximum de \( f \) . On a

> We write \( {x}^{-{\alpha x}}{t}^{x} = \exp \left( {f\left( x\right) }\right) \) where \( f\left( x\right) = \log t \cdot x - {\alpha x}\log x \) . As \( f\left( x\right) \rightarrow - \infty \) as \( x \rightarrow + \infty \) , the integral \( I\left( t\right) \) converges. Let us find the abscissa \( x \) of the maximum of \( f \) . We have

\[
{f}^{\prime }\left( x\right)  = \log t - \alpha \left( {1 + \log x}\right)
\]

donc le maximum de \( f \) est atteint au point \( x = {t}^{1/\alpha }/e \) . Pour le ramener à une abscisse fixe, on effectue le changement de variable \( x = u{t}^{1/\alpha }/e \) . On obtient

> so the maximum of \( f \) is reached at the point \( x = {t}^{1/\alpha }/e \) . To bring it back to a fixed abscissa, we perform the change of variable \( x = u{t}^{1/\alpha }/e \) . We obtain

\[
I\left( t\right)  = s{\int }_{0}^{+\infty }{e}^{{sh}\left( u\right) }{du}\;\text{ où }\;s = \frac{{t}^{1/\alpha }}{e}\;\text{ et }\;h\left( u\right)  = {\alpha u}\left( {1 - \log u}\right) .
\]

La fonction \( h \) admet un unique maximum en \( u = 1 \) , et on a \( h\left( 1\right) = \alpha ,{h}^{\prime \prime }\left( 1\right) = - \alpha \) . On peut donc appliquer le corollaire 2 à cette dernière intégrale, ce qui donne

> The function \( h \) admits a unique maximum at \( u = 1 \) , and we have \( h\left( 1\right) = \alpha ,{h}^{\prime \prime }\left( 1\right) = - \alpha \) . We can therefore apply corollary 2 to this latter integral, which gives

\[
{\int }_{0}^{+\infty }{e}^{{sh}\left( u\right) }{du} \sim  \Gamma \left( \frac{1}{2}\right) {e}^{\alpha s}\sqrt{\frac{2}{\alpha s}}.
\]

Donc, compte tenu de l’expression de \( s \) en fonction de \( t \) et du fait que \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) , on trouve

> Therefore, given the expression of \( s \) as a function of \( t \) and the fact that \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) , we find

\[
I\left( t\right)  \sim  \sqrt{\frac{2\pi }{e\alpha }}{t}^{1/\left( {2\alpha }\right) }\exp \left( \frac{\alpha {t}^{1/\alpha }}{e}\right) .
\]

---

b) Pour se ramener aux hypothèses usuelles d'application de la méthode de Laplace, on commence par effectuer le changement de variable \( u = \pi - x \) , ce qui donne

> b) To reduce to the usual hypotheses for applying Laplace's method, we begin by performing the change of variable \( u = \pi - x \) , which gives

\[
I\left( t\right)  = {\int }_{0}^{\pi }\left( {\sin u}\right) {\left( \pi  - u\right) }^{t}{du} = {\int }_{0}^{\pi }g\left( u\right) {e}^{{th}\left( u\right) }{du}
\]

avec \( g\left( u\right) = \sin u \sim u \) et \( h\left( u\right) = \log \left( {\pi - u}\right) = \log \pi - \frac{u}{\pi } + o\left( u\right) \left( {u \rightarrow {0}^{ + }}\right) \) . On peut donc appliquer le théorème 4 qui donne

> with \( g\left( u\right) = \sin u \sim u \) and \( h\left( u\right) = \log \left( {\pi - u}\right) = \log \pi - \frac{u}{\pi } + o\left( u\right) \left( {u \rightarrow {0}^{ + }}\right) \) . We can therefore apply theorem 4 which gives

\[
I\left( t\right)  \sim  \Gamma \left( 2\right) {\pi }^{t}{\left( \frac{t}{\pi }\right) }^{-2} = \frac{{\pi }^{t + 2}}{{t}^{2}}.
\]

2/ On ne peut pas appliquer telle quelle la méthode de Laplace car l'intégrale est étudiée lorsque le paramètre \( t \) tend vers \( {0}^{ + } \) . Pour se ramener à un paramètre qui tend vers \( + \infty \) , on effectue le changement de variable \( u = {tx} \) , qui donne

> 2/ We cannot apply Laplace's method as is because the integral is studied as the parameter \( t \) tends to \( {0}^{ + } \) . To reduce to a parameter that tends to \( + \infty \) , we perform the change of variable \( u = {tx} \) , which gives

\[
I\left( t\right)  = \frac{1}{t}{\int }_{0}^{+\infty }\exp \left( {\frac{{u}^{\alpha }}{\alpha {t}^{\alpha }} - u}\right) {du}.
\]

La fonction \( f\left( u\right) = \frac{{u}^{\alpha }}{\alpha {t}^{\alpha }} - u \) prend son maximum pour \( u = {t}^{\alpha /\left( {\alpha - 1}\right) } \) , ce qui nous amène à effectuer le changement de variable \( u = v{t}^{\alpha /\left( {\alpha - 1}\right) } \) . On trouve

> The function \( f\left( u\right) = \frac{{u}^{\alpha }}{\alpha {t}^{\alpha }} - u \) reaches its maximum at \( u = {t}^{\alpha /\left( {\alpha - 1}\right) } \) , which leads us to perform the change of variable \( u = v{t}^{\alpha /\left( {\alpha - 1}\right) } \) . We find

\[
I\left( t\right)  = \frac{s}{t}{\int }_{0}^{+\infty }{e}^{{sh}\left( v\right) }{dv},\;\text{ où }\;s = {t}^{\alpha /\left( {\alpha  - 1}\right) }\;\text{ et }\;h\left( v\right)  = \frac{{v}^{\alpha }}{\alpha } - v.
\]

La fonction \( h \) admet un maximum unique qu’elle atteint en \( v = 1 \) . De plus,

> The function \( h \) has a unique maximum reached at \( v = 1 \) . Furthermore,

\[
h\left( 1\right)  = \frac{1 - \alpha }{\alpha }\;\text{ et }\;{h}^{\prime \prime }\left( 1\right)  = \alpha  - 1.
\]

En appliquant le corollaire 2, on obtient donc

> By applying corollary 2, we therefore obtain

\[
{\int }_{0}^{+\infty }{e}^{{sh}\left( v\right) }{dv} \sim  \Gamma \left( \frac{1}{2}\right) {e}^{\left( {1 - \alpha }\right) s/\alpha }\sqrt{\frac{2}{\left( {1 - \alpha }\right) s}}\;\left( {s \rightarrow   + \infty }\right) .
\]

Or \( s = {t}^{-\alpha /\left( {1 - \alpha }\right) } \) et \( 0 < \alpha < 1 \) . Lorsque \( t \rightarrow {0}^{ + } \) , on a donc \( s \rightarrow + \infty \) , et finalement

> However, \( s = {t}^{-\alpha /\left( {1 - \alpha }\right) } \) and \( 0 < \alpha < 1 \) . When \( t \rightarrow {0}^{ + } \) , we therefore have \( s \rightarrow + \infty \) , and finally

\[
I\left( t\right)  \sim  \sqrt{\frac{2\pi }{1 - \alpha }}{t}^{\frac{\alpha  - 2}{2\left( {1 - \alpha }\right) }}\exp \left( {\frac{1 - \alpha }{\alpha }{t}^{-\frac{\alpha }{1 - \alpha }}}\right) ,\;\left( {t \rightarrow  {0}^{ + }}\right) .
\]

EXERCICE 7. Soient \( a \in \mathbb{R} \) et \( g : \left\lbrack {a, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) une application de classe \( {\mathcal{C}}^{1} \) . On suppose que \( g \) ne s’annule pas au voisinage de l’infini et que lorsque \( x \rightarrow + \infty \) , on a

> EXERCISE 7. Let \( a \in \mathbb{R} \) and \( g : \left\lbrack {a, + \infty \left\lbrack { \rightarrow \mathbb{R}}\right. }\right. \) be a \( {\mathcal{C}}^{1} \) class mapping. Suppose that \( g \) does not vanish in the neighborhood of infinity and that when \( x \rightarrow + \infty \) , we have

\[
\frac{{g}^{\prime }\left( x\right) }{g\left( x\right) } \sim  \frac{\mu }{x},\;\mu  \neq  0,\mu  \neq   - 1.
\]

Montrer que

> Show that

\[
\operatorname{si}\mu  >  - 1,\;{\int }_{a}^{+\infty }g\left( t\right) {dt}\;\text{ diverge }\;\text{ et }\;{\int }_{a}^{x}g\left( t\right) {dt} \sim  \frac{{xg}\left( x\right) }{\mu  + 1}\;\left( {x \rightarrow   + \infty }\right)
\]

\[
1,\;{\int }_{a}^{+\infty }g\left( t\right) {dt}\text{ converge }\;\text{ et }\;{\int }_{x}^{+\infty }g\left( t\right) {dt} \sim   - \frac{{xg}\left( x\right) }{\mu  + 1}\;\left( {x \rightarrow   + \infty }\right) .
\]

Solution. On traite d'abord le cas \( \mu > - 1 \) . Le théorème 3 (page 163) sur les équivalents de primitives entraîne

> Solution. We first treat the case \( \mu > - 1 \) . Theorem 3 (page 163) on equivalents of primitives implies

\[
{\int }_{a}^{x}\frac{{g}^{\prime }\left( t\right) }{g\left( t\right) }{dt} \sim  \mu {\int }_{a}^{x}\frac{dt}{t}\;\text{ autrement dit }\;\log g\left( x\right)  \sim  \mu \log x.
\]

En particulier,

> In particular,

\[
\forall \varepsilon  > 0,\exists X > a,\forall x \geq  X,\;\log g\left( x\right)  \geq  \left( {\mu  - \varepsilon }\right) \log x\;\text{ ou encore }\;g\left( x\right)  \geq  {x}^{\mu  - \varepsilon }.
\]

En choisissant \( \varepsilon > 0 \) suffisamment petit pour que \( \mu - \varepsilon > - 1 \) , on en déduit que \( {\int }_{a}^{+\infty }g\left( t\right) {dt} \) diverge. Par ailleurs, en intégrant par parties, on a

> By choosing \( \varepsilon > 0 \) small enough so that \( \mu - \varepsilon > - 1 \) , we deduce that \( {\int }_{a}^{+\infty }g\left( t\right) {dt} \) diverges. Furthermore, by integrating by parts, we have

\[
{\int }_{a}^{x}g\left( t\right) {dt} = {\left\lbrack  tg\left( t\right) \right\rbrack  }_{a}^{x} - {\int }_{a}^{x}t{g}^{\prime }\left( t\right) {dt}\;\text{ donc }\;{\int }_{a}^{x}\left( {g\left( t\right)  + t{g}^{\prime }\left( t\right) }\right) {dt} = {xg}\left( x\right)  - {ag}\left( a\right) .
\]

Or

\[
g\left( t\right)  + t{g}^{\prime }\left( t\right)  = g\left( t\right) \left( {1 + t\frac{{g}^{\prime }\left( t\right) }{g\left( t\right) }}\right)  \sim  g\left( t\right) \left( {1 + \mu }\right) ,
\]

donc en vertu du théorème 3 , on a

> therefore, by virtue of theorem 3, we have

\[
{xg}\left( x\right)  - {ag}\left( a\right)  = {\int }_{a}^{x}\left( {g\left( t\right)  + t{g}^{\prime }\left( t\right) }\right) {dt} \sim  \left( {\mu  + 1}\right) {\int }_{a}^{x}g\left( t\right) {dt}.
\]

On en déduit le résultat.

> We deduce the result.

Le cas \( \mu < - 1 \) se traite de la même manière.

> The case \( \mu < - 1 \) is treated in the same way.

EXERCICE 8. On considère le logarithme intégral, qui est l'application définie par

> EXERCISE 8. Consider the logarithmic integral, which is the mapping defined by

\[
\forall x \geq  2,\;\operatorname{Li}\left( x\right)  = {\int }_{2}^{x}\frac{dt}{\log t}.
\]

Pour tout \( n \in {\mathbb{N}}^{ * } \) , donner un développement asymptotique de Li \( \left( x\right) \) à \( n \) termes lorsque \( x \rightarrow + \infty \) .

> For any \( n \in {\mathbb{N}}^{ * } \) , provide an asymptotic expansion of Li \( \left( x\right) \) to \( n \) terms as \( x \rightarrow + \infty \) .

Solution. En intégrant une fois par parties, on a

> Solution. By integrating once by parts, we have

\[
\forall x \geq  2,\;{\int }_{2}^{x}\frac{dt}{\log t} = {\left\lbrack  \frac{t}{\log t}\right\rbrack  }_{2}^{x} + {\int }_{2}^{x}\frac{dt}{{\log }^{2}t}.
\]

En itérant le procédé, on tombe au bout de \( n - 1 \) étapes sur la relation

> By iterating the process, we arrive after \( n - 1 \) steps at the relation

\[
\operatorname{Li}\left( x\right)  = {\left\lbrack  \frac{t}{\log t}\right\rbrack  }_{2}^{x} + 1!{\left\lbrack  \frac{t}{{\log }^{2}t}\right\rbrack  }_{2}^{x} + 2!{\left\lbrack  \frac{t}{{\log }^{3}t}\right\rbrack  }_{2}^{x} + \cdots  + \left( {n - 1}\right) !{\left\lbrack  \frac{t}{{\log }^{n}t}\right\rbrack  }_{2}^{x} + n!{\int }_{2}^{x}\frac{dt}{{\log }^{n + 1}t}.
\]

(*)

> Nous cherchons à obtenir un équivalent de la dernière primitive. Le logarithme est une fonction qui varie très peu (en poussant, on peut dire que log \( x \) est presque une constante vers l’infini), et on s’attend à ce que \( {\int }_{2}^{x}{\log }^{-\left( {n + 1}\right) }{tdt} \sim x/{\log }^{n + 1}x \) . Pour prouver ceci, on écrit

We seek to obtain an equivalent for the last primitive. The logarithm is a function that varies very little (at the limit, one could say that log \( x \) is almost a constant towards infinity), and we expect that \( {\int }_{2}^{x}{\log }^{-\left( {n + 1}\right) }{tdt} \sim x/{\log }^{n + 1}x \) . To prove this, we write

\[
\frac{d}{dt}\left( \frac{t}{{\log }^{n + 1}t}\right)  = \frac{1}{{\log }^{n + 1}t} - \frac{\left( n + 1\right) }{{\log }^{n + 2}t} \sim  \frac{1}{{\log }^{n + 1}t},\;\left( {t \rightarrow   + \infty }\right) .
\]

Le théorème 3 nous autorise à intégrer cet équivalent. En d’autres termes, lorsque \( x \rightarrow + \infty \) on a

> Theorem 3 allows us to integrate this equivalent. In other words, when \( x \rightarrow + \infty \) we have

\[
{\left\lbrack  \frac{x}{{\log }^{n + 1}x}\right\rbrack  }_{2}^{x} = {\int }_{2}^{x}\frac{d}{dt}\left( \frac{t}{{\log }^{n + 1}t}\right) {dt} \sim  {\int }_{2}^{x}\frac{dt}{{\log }^{n + 1}t}\;\text{ donc }\;{\int }_{2}^{x}\frac{dt}{{\log }^{n + 1}t} \sim  \frac{x}{{\log }^{n + 1}x}.
\]

Avec (*), on en déduit finalement

> With (*), we finally deduce

\[
\operatorname{Li}\left( x\right)  = \frac{x}{\log x} + \frac{1!x}{{\log }^{2}x} + \frac{2!x}{{\log }^{3}x} + \cdots  + \frac{n!x}{{\log }^{n + 1}x} + o\left( \frac{x}{{\log }^{n + 1}x}\right) .
\]

Remarque. Tous les termes de ce développement asymptotique tendent vers \( + \infty \) lorsque \( x \rightarrow + \infty \) .

> Remark. All terms of this asymptotic expansion tend towards \( + \infty \) when \( x \rightarrow + \infty \) .

EXERCICE 9. Donner un équivalent, lorsque \( t \rightarrow + \infty \) , de

> EXERCISE 9. Provide an equivalent, when \( t \rightarrow + \infty \) , of

\[
I\left( t\right)  = {\int }_{0}^{1}\cos x{e}^{{it}\operatorname{ch}x}{dx}.
\]

Solution. Commençons par analyser intuitivement la situation. Lorsque \( t \) est grand, \( x \mapsto {e}^{{it}\operatorname{ch}x} \) tourne très vite autour de l'origine dans \( \mathbb{C} \) , ce qui a pour effet de rendre l'intégrale petite. Mais lorsque \( x \) est proche de 0, l’application \( x \mapsto \operatorname{ch}x \) varie peu (sa dérivée est nulle en 0 ), et cette rotation est très ralentie (on dit que la phase \( t\operatorname{ch}x \) est stationnaire). La partie de l’intégrale correspondant à ce voisinage apporte donc une contribution prépondérante. Pour cette raison, on va travailler au voisinage de 0.

> Solution. Let us begin by intuitively analyzing the situation. When \( t \) is large, \( x \mapsto {e}^{{it}\operatorname{ch}x} \) rotates very quickly around the origin in \( \mathbb{C} \) , which has the effect of making the integral small. But when \( x \) is close to 0, the mapping \( x \mapsto \operatorname{ch}x \) varies little (its derivative is zero at 0), and this rotation is greatly slowed down (we say that the phase \( t\operatorname{ch}x \) is stationary). The part of the integral corresponding to this neighborhood therefore provides a predominant contribution. For this reason, we will work in the neighborhood of 0.

Le développement limité

> The Taylor expansion

\[
\operatorname{ch}x = 1 + \frac{{x}^{2}}{2} + o\left( {x}^{2}\right) \;x \rightarrow  {0}^{ + }
\]

nous invite à écrire \( \operatorname{ch}x = 1 + 2{\operatorname{sh}}^{2}\left( {x/2}\right) \) et d’effectuer le changement de variable \( u = \operatorname{sh}\left( {x/2}\right) \) dans l'intégrale. On trouve

> invites us to write \( \operatorname{ch}x = 1 + 2{\operatorname{sh}}^{2}\left( {x/2}\right) \) and to perform the change of variable \( u = \operatorname{sh}\left( {x/2}\right) \) in the integral. We find

\[
I\left( t\right)  = 2{e}^{it}J\left( t\right) ,\;\text{ où }\;J\left( t\right)  = {\int }_{0}^{\alpha }g\left( u\right) {e}^{{2it}{u}^{2}}{du}\;\text{ avec }\;\alpha  = \operatorname{sh}\frac{1}{2},\;g\left( u\right)  = \frac{\cos \left( {2\operatorname{argsh}u}\right) }{\sqrt{1 + {u}^{2}}}.
\]

La fonction \( g \) est de classe \( {\mathcal{C}}^{\infty } \) et \( g\left( 0\right) = 1 \) . Nous allons montrer, comme on s’y attend suite à la discussion que nous avons eu plus haut, que

> The function \( g \) is of class \( {\mathcal{C}}^{\infty } \) and \( g\left( 0\right) = 1 \) . We will show, as expected following the discussion we had above, that

\[
J\left( t\right)  \sim  {\int }_{0}^{\alpha }{e}^{{2it}{u}^{2}}{du}\;\text{ lorsque }\;t \rightarrow   + \infty .
\]

Le changement de variable \( v = {2t}{u}^{2} \) fournit

> The change of variable \( v = {2t}{u}^{2} \) provides

\[
{\int }_{0}^{\alpha }{e}^{{2it}{u}^{2}}{du} = \frac{1}{2\sqrt{2t}}{\int }_{0}^{{2t}{\alpha }^{2}}\frac{{e}^{iv}}{\sqrt{v}}{dv} \sim  \frac{K}{2\sqrt{2t}}\;\text{ avec }\;K = {\int }_{0}^{+\infty }\frac{{e}^{iv}}{\sqrt{v}}{dv}.
\]

(*).

> Par ailleurs, on a

Furthermore, we have

\[
J\left( t\right)  - {\int }_{0}^{\alpha }{e}^{{2it}{u}^{2}}{du} = {\int }_{0}^{\alpha }{g}_{1}\left( u\right) {e}^{{2it}{u}^{2}}{du}\;\text{ avec }\;{g}_{1}\left( u\right)  = g\left( u\right)  - 1.
\]

\( \left( {* * }\right) \)

> La fonction \( {g}_{1} \) est de classe \( {\mathcal{C}}^{\infty } \) et elle est nulle en 0, on peut en déduire facilement que \( u \mapsto \; {g}_{1}\left( u\right) /u \) se prolonge en une fonction de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,\alpha }\right\rbrack \) (cette dernière est même de classe \( {\mathcal{C}}^{\infty } \) , voir l’exercice 3 page 168). On peut donc écrire

The function \( {g}_{1} \) is of class \( {\mathcal{C}}^{\infty } \) and is zero at 0; we can easily deduce that \( u \mapsto \; {g}_{1}\left( u\right) /u \) extends to a function of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,\alpha }\right\rbrack \) (the latter is even of class \( {\mathcal{C}}^{\infty } \) , see exercise 3 on page 168). We can therefore write

\[
{\int }_{0}^{\alpha }{g}_{1}\left( u\right) {e}^{{2it}{u}^{2}}{du} = \frac{1}{4it}{\int }_{0}^{\alpha }\left( \frac{{g}_{1}\left( u\right) }{u}\right) \frac{d}{du}\left( {e}^{{2it}{u}^{2}}\right) {du}
\]

\[
= \frac{1}{4it}{\left\lbrack  \frac{{g}_{1}\left( u\right) }{u}{e}^{{2it}{u}^{2}}\right\rbrack  }_{0}^{\alpha } - \frac{1}{4it}{\int }_{0}^{\alpha }\frac{d}{du}\left\lbrack  \frac{{g}_{1}\left( u\right) }{u}\right\rbrack  {e}^{{2it}{u}^{2}}{du},
\]

ce qui montre, avec (**)

> which shows, with (**)

\[
J\left( t\right)  - {\int }_{0}^{\alpha }{e}^{{2it}{u}^{2}}{du} = O\left( \frac{1}{t}\right) ,\;\left( {t \rightarrow   + \infty }\right) .
\]

Avec (*) on en déduit

> With (*) we deduce

\[
I\left( t\right)  = 2{e}^{it}J\left( t\right)  \sim  \frac{K{e}^{it}}{\sqrt{2t}}\;\text{ avec }\;K = {\int }_{0}^{+\infty }\frac{{e}^{iv}}{\sqrt{v}}{dv}.
\]

Remarque. On a \( K = \Gamma \left( {1/2}\right) {e}^{{i\pi }/4} = \sqrt{\pi }{e}^{{i\pi }/4} \) (voir la question 2/b) de l’exercice 4).

> Remark. We have \( K = \Gamma \left( {1/2}\right) {e}^{{i\pi }/4} = \sqrt{\pi }{e}^{{i\pi }/4} \) (see question 2/b) of exercise 4).

- Il existe une technique générale appelée la méthode de la phase stationnaire qui permet de donner un équivalent des intégrales de la forme \( {\int }_{a}^{b}g\left( x\right) {e}^{{ith}\left( x\right) }{dx} \) lorsque \( t \rightarrow   + \infty \) .

> - There exists a general technique called the stationary phase method which allows one to provide an equivalent for integrals of the form \( {\int }_{a}^{b}g\left( x\right) {e}^{{ith}\left( x\right) }{dx} \) when \( t \rightarrow   + \infty \) .

EXERCICE 10. Soit \( a > 0 \) . Donner un équivalent, lorsque \( n \rightarrow + \infty \) , de

> EXERCISE 10. Let \( a > 0 \) . Give an equivalent, as \( n \rightarrow + \infty \) , of

\[
{I}_{n} = {\int }_{0}^{+\infty }\frac{dx}{\left( {1 + {x}^{a}}\right) \left( {2 + {x}^{a}}\right) \cdots \left( {n + {x}^{a}}\right) }.
\]

Solution. Pour \( n \) fixé, l’intégrande de \( {I}_{n} \) est équivalente à \( {x}^{-{na}} \) lorsque \( x \rightarrow + \infty \) , ce qui montre que \( {I}_{n} \) existe dès que \( n > 1/a \) .

> Solution. For fixed \( n \) , the integrand of \( {I}_{n} \) is equivalent to \( {x}^{-{na}} \) as \( x \rightarrow + \infty \) , which shows that \( {I}_{n} \) exists as soon as \( n > 1/a \) .

En effectuant le changement de variable \( t = {x}^{a} \) , on voit que

> By performing the change of variable \( t = {x}^{a} \) , we see that

\[
{I}_{n} = \frac{1}{a}{\int }_{0}^{+\infty }\frac{{t}^{\alpha }{dt}}{\left( {1 + t}\right) \left( {2 + t}\right) \cdots \left( {n + t}\right) } = \frac{1}{a}{J}_{n}\;\text{ où }\;\alpha  = \frac{1}{a} - 1.
\]

On s’est ainsi ramené à rechercher un équivalent de \( {J}_{n} \) lorsque \( n \rightarrow + \infty \) . On sent intuitivement que c’est la partie correspondant aux valeurs de \( x \) proches de 0 qui va donner une contribution prépondérante à l'intégrale. Ceci nous amène à rechercher un équivalent de

> We have thus reduced the problem to finding an equivalent of \( {J}_{n} \) as \( n \rightarrow + \infty \) . We intuitively feel that it is the part corresponding to values of \( x \) close to 0 that will provide a predominant contribution to the integral. This leads us to look for an equivalent of

\[
{K}_{n} = {\int }_{0}^{1}\frac{{t}^{\alpha }{dt}}{\left( {1 + t}\right) \left( {2 + t}\right) \cdots \left( {n + t}\right) }.
\]

Cette dernière intégrale a des bornes d'intégrations finies, ce qui nous simplifiera la tache dans la suite du calcul. Nous prouverons ultérieurement que l’on a bien \( {K}_{n} \sim {J}_{n} \) .

> This last integral has finite limits of integration, which will simplify the task in the rest of the calculation. We will prove later that we indeed have \( {K}_{n} \sim {J}_{n} \) .

Poursuivons. On écrit

> Let us continue. We write

\[
{K}_{n} = \frac{{L}_{n}}{n!},\;{L}_{n} = {\int }_{0}^{1}\frac{{t}^{\alpha }{dt}}{\left( {1 + t}\right) \left( {1 + t/2}\right) \cdots \left( {1 + t/n}\right) },
\]

nous ramenant ainsi à trouver un équivalent de \( {L}_{n} \) . Commençons par donner l’idée. On va écrire

> thus reducing us to finding an equivalent of \( {L}_{n} \) . Let us start by giving the idea. We will write

\[
\mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + \frac{t}{k}}\right)  = \exp \left\lbrack  {\mathop{\sum }\limits_{{k = 1}}^{n}\log \left( {1 + \frac{t}{k}}\right) }\right\rbrack   \simeq  \exp \left\lbrack  {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{t}{k}}\right\rbrack   \simeq  \exp \left( {t\log n}\right) .
\]

Il s'agit de rendre rigoureuse cette affirmation. On part de l'inégalité classique

> It is a matter of making this statement rigorous. We start from the classical inequality

\[
\forall u \geq  0,\;\left| {\log \left( {1 + u}\right)  - u}\right|  \leq  \frac{{u}^{2}}{2}
\]

(conséquence de l’inégalité de Taylor-Lagrange appliquée à \( t \mapsto \log \left( {1 + t}\right) \) sur \( \left\lbrack {0, u}\right\rbrack \) à l’ordre 2). Donc pour tout \( n \in {\mathbb{N}}^{ * } \) et pour tout \( t \in \left\lbrack {0,1}\right\rbrack \) ,

> (a consequence of the Taylor-Lagrange inequality applied to \( t \mapsto \log \left( {1 + t}\right) \) on \( \left\lbrack {0, u}\right\rbrack \) at order 2). Therefore, for all \( n \in {\mathbb{N}}^{ * } \) and for all \( t \in \left\lbrack {0,1}\right\rbrack \) ,

\[
\left| {\mathop{\sum }\limits_{{k = 1}}^{n}\log \left( {1 + \frac{t}{k}}\right)  - t\left( {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{k}}\right) }\right|  \leq  \frac{{t}^{2}}{2}\left( {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{{k}^{2}}}\right)  \leq  K{t}^{2}\;\text{ avec }\;K = \frac{1}{2}\mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{1}{{k}^{2}}.
\]

(*)

> Il est classique que \( \mathop{\sum }\limits_{{k = 1}}^{n}1/k = \log n + {u}_{n} \) où \( \left( {u}_{n}\right) \) est une suite qui tend vers la constante d’Euler \( \gamma \) . La suite \( \left( {u}_{n}\right) \) est en particulier bornée, et si on désigne par \( M \) un majorant de \( \left| {u}_{n}\right| \) , l'assertion (*) entraîne

It is standard that \( \mathop{\sum }\limits_{{k = 1}}^{n}1/k = \log n + {u}_{n} \) where \( \left( {u}_{n}\right) \) is a sequence that tends to the Euler constant \( \gamma \) . The sequence \( \left( {u}_{n}\right) \) is in particular bounded, and if we denote by \( M \) an upper bound of \( \left| {u}_{n}\right| \) , the assertion (*) implies

\[
\forall n \in  {\mathbb{N}}^{ * },\forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\;\left| {\mathop{\sum }\limits_{{k = 1}}^{n}\log \left( {1 + \frac{t}{k}}\right)  - t\log n}\right|  \leq  t\left| {u}_{n}\right|  + K{t}^{2} \leq  \left( {M + K}\right) t = {Lt},
\]

inégalité que l'on peut aussi écrire sous la forme

> an inequality that can also be written in the form

\[
\forall n \in  {\mathbb{N}}^{ * },\forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\;t\left( {\log n - L}\right)  \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\log \left( {1 + \frac{t}{k}}\right)  \leq  t\left( {\log n + L}\right) .
\]

En prenant l'exponentielle, ceci s'écrit

> Taking the exponential, this is written

\[
\forall n \in  {\mathbb{N}}^{ * },\forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\;{e}^{t\left( {\log n - L}\right) } \leq  \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + \frac{t}{k}}\right)  \leq  {e}^{t\left( {\log n + L}\right) }
\]

donc finalement

> so finally

\[
\forall n \in  {\mathbb{N}}^{ * },{\int }_{0}^{1}{t}^{\alpha }{e}^{-t\left( {\log n + L}\right) }{dt} \leq  {L}_{n} \leq  {\int }_{0}^{1}{t}^{\alpha }{e}^{-t\left( {\log n - L}\right) }{dt}.
\]

(**)

> Or, de manière générale on a

However, in general we have

\[
{\int }_{0}^{1}{t}^{\alpha }{e}^{-{\lambda t}}{dt} = \frac{1}{{\lambda }^{\alpha  + 1}}{\int }_{0}^{\lambda }{t}^{\alpha }{e}^{-t}{dt} \sim  \frac{\Gamma \left( {\alpha  + 1}\right) }{{\lambda }^{\alpha  + 1}},\;\lambda  \rightarrow   + \infty .
\]

Ainsi, les termes extrêmes des inégalités (**) sont tout deux équivalents à

> Thus, the extreme terms of the inequalities (**) are both equivalent to

\[
\frac{\Gamma \left( {\alpha  + 1}\right) }{{\left( \log n\right) }^{\alpha  + 1}}
\]

\( \left( {* * * }\right) \)

> (car \( \log n - L \sim \log n \) et \( \log n + L \sim \log n \) lorsque \( n \rightarrow + \infty \) ). On en déduit d’après (**) que (***) est un équivalent de \( {L}_{n} \) , donc finalement

(because \( \log n - L \sim \log n \) and \( \log n + L \sim \log n \) as \( n \rightarrow + \infty \) ). We deduce from (**) that (***) is an equivalent of \( {L}_{n} \) , so finally

\[
{K}_{n} = \frac{1}{n!}{L}_{n} \sim  \frac{1}{n!}\frac{\Gamma \left( {\alpha  + 1}\right) }{{\left( \log n\right) }^{\alpha  + 1}},\;n \rightarrow   + \infty .
\]

(***

> Pour achever notre calcul, il reste à montrer que \( {J}_{n} \sim {K}_{n} \) . Pour cela, on écrit d’abord

To complete our calculation, it remains to show that \( {J}_{n} \sim {K}_{n} \) . For this, we first write

\[
{J}_{n} - {K}_{n} = {\int }_{1}^{+\infty }\frac{{f}_{N}\left( t\right) {dt}}{\left( {N + t}\right) \cdots \left( {n + t}\right) },\;{f}_{N}\left( t\right)  = \frac{{t}^{\alpha }}{\left( {1 + t}\right) \left( {2 + t}\right) \cdots \left( {N - 1 + t}\right) }
\]

Fixons un entier \( N > \alpha + 2 \) , de sorte que \( {f}_{N} \) est intégrable sur \( \lbrack 1, + \infty \lbrack \) . Pour \( n > N \) on a

> Let us fix an integer \( N > \alpha + 2 \) , such that \( {f}_{N} \) is integrable on \( \lbrack 1, + \infty \lbrack \) . For \( n > N \) we have

\[
0 \leq  {J}_{n} - {K}_{n} \leq  {\int }_{1}^{+\infty }\frac{{f}_{N}\left( t\right) {dt}}{\left( {N + 1}\right) \cdots \left( {n + 1}\right) } = \frac{\left( {N!}\right) {\int }_{1}^{+\infty }{f}_{N}\left( t\right) {dt}}{\left( {n + 1}\right) !} = O\left( \frac{1}{\left( {n + 1}\right) !}\right) .
\]

Avec (****), on en déduit que \( {J}_{n} \sim {K}_{n} \) . Finalement, compte tenu du fait que \( \alpha = 1/a - 1 \) , on a montré

> With (****), we deduce that \( {J}_{n} \sim {K}_{n} \) . Finally, given the fact that \( \alpha = 1/a - 1 \) , we have shown

\[
{I}_{n} = \frac{1}{a}{J}_{n} \sim  \frac{1}{a}\frac{1}{n!}\frac{1}{{\left( \log n\right) }^{1/a}}\Gamma \left( \frac{1}{a}\right) .
\]

Remarque. On peut utiliser la formule de Stirling pour exprimer l'équivalent obtenu sous une forme ne faisant pas intervenir de factorielle.

> Remark. One can use Stirling's formula to express the obtained equivalent in a form that does not involve factorials.
