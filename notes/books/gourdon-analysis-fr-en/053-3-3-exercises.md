#### 3.3. Exercises

*Français : 3.3. Exercices*

EXERCICE 1. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une fonction convexe et majorée sur \( \mathbb{R} \) . Montrer que \( f \) est constante. Le résultat reste t-il valable si on suppose seulement \( f \) définie, convexe et majorée sur \( {\mathbb{R}}^{ + } \) ?

> EXERCISE 1. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a convex and bounded-above function on \( \mathbb{R} \). Show that \( f \) is constant. Does the result remain valid if we only assume \( f \) is defined, convex, and bounded-above on \( {\mathbb{R}}^{ + } \)?

Solution. Supposons \( f \) non constante, de sorte qu’il existe \( x, y \in \mathbb{R}, x < y \) , avec \( f\left( x\right) \neq f\left( y\right) \) .

> Solution. Suppose \( f \) is not constant, such that there exists \( x, y \in \mathbb{R}, x < y \), with \( f\left( x\right) \neq f\left( y\right) \).

- Si \( f\left( x\right)  < f\left( y\right) \) , la convexité de \( f \) entraîne

> - If \( f\left( x\right)  < f\left( y\right) \), the convexity of \( f \) implies

\[
\forall z > y,\;\frac{f\left( z\right)  - f\left( y\right) }{z - y} \geq  \frac{f\left( y\right)  - f\left( x\right) }{y - x} = a\;\text{ ou encore }\;f\left( z\right)  \geq  f\left( y\right)  + a\left( {z - y}\right) .
\]

Comme \( f\left( y\right) > f\left( x\right) \) , on a \( a > 0 \) et donc \( \mathop{\lim }\limits_{{z \rightarrow + \infty }}f\left( z\right) = + \infty \) ce qui est contraire aux hypothèses.

> Since \( f\left( y\right) > f\left( x\right) \), we have \( a > 0 \) and therefore \( \mathop{\lim }\limits_{{z \rightarrow + \infty }}f\left( z\right) = + \infty \), which contradicts the hypotheses.

- Si \( f\left( x\right)  > f\left( y\right) \) , on montrerait de même que \( \mathop{\lim }\limits_{{z \rightarrow   - \infty }}f\left( z\right)  =  + \infty \) , d’où l’absurdité. L’application \( f \) est donc constante.

> - If \( f\left( x\right)  > f\left( y\right) \), we would show similarly that \( \mathop{\lim }\limits_{{z \rightarrow   - \infty }}f\left( z\right)  =  + \infty \), hence the absurdity. The mapping \( f \) is therefore constant.

Le résultat est faux lorsque les hypothèses ne sont vraies que sur \( {\mathbb{R}}^{ + } \) , comme le montre l’exemple de la fonction \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto \frac{1}{1 + x} \) .

> The result is false when the hypotheses are only true on \( {\mathbb{R}}^{ + } \), as shown by the example of the function \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto \frac{1}{1 + x} \).

EXERCICE 2. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction convexe.

> EXERCISE 2. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a convex function.

a) Montrer que \( \ell = \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{f\left( x\right) }{x} \) existe.

> a) Show that \( \ell = \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{f\left( x\right) }{x} \) exists.

b) On suppose que \( \ell \in \mathbb{R} \) . Montrer que \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) - \ell x \) existe.

> b) Suppose that \( \ell \in \mathbb{R} \). Show that \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) - \ell x \) exists.

Solution. a) Comme \( f \) est convexe, la fonction \( {\mathbb{R}}^{+ * } \rightarrow \mathbb{R}\;x \mapsto \frac{f\left( x\right) - f\left( 0\right) }{x - 0} \) est croissante. Donc \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{f\left( x\right) - f\left( 0\right) }{x} \) existe, et cette limite n’est autre que \( \ell \) . On a d’ailleurs \( \ell \in \mathbb{R} \cup \{ + \infty \} \) (on peut avoir \( \ell = + \infty \) comme le montre l’exemple de la fonction \( x \mapsto {x}^{2} \) ).

> Solution. a) Since \( f \) is convex, the function \( {\mathbb{R}}^{+ * } \rightarrow \mathbb{R}\;x \mapsto \frac{f\left( x\right) - f\left( 0\right) }{x - 0} \) is increasing. Thus \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{f\left( x\right) - f\left( 0\right) }{x} \) exists, and this limit is none other than \( \ell \). Moreover, we have \( \ell \in \mathbb{R} \cup \{ + \infty \} \) (it is possible to have \( \ell = + \infty \) as shown by the example of the function \( x \mapsto {x}^{2} \)).

b) L’application \( g : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) - \ell x \) est convexe (somme de deux fonctions convexes), et elle vérifie \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) }{x} = 0 \) .

> b) The mapping \( g : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) - \ell x \) is convex (sum of two convex functions), and it satisfies \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) }{x} = 0 \).

Montrons que \( g \) est décroissante. Soient \( a, b \in {\mathbb{R}}^{ + }, a < b \) . Comme \( g \) est convexe, la fonction \( x \mapsto \frac{g\left( x\right) - g\left( a\right) }{x - a} \) est croissante. Or \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) - g\left( a\right) }{x - a} = \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) }{x} = 0 \) . Donc pour tout \( x \neq a \) , \( \frac{g\left( x\right) - g\left( a\right) }{x - a} \leq 0 \) . En appliquant ceci à \( x = b \) , on en déduit \( g\left( b\right) \leq g\left( a\right) \) .

> Let us show that \( g \) is decreasing. Let \( a, b \in {\mathbb{R}}^{ + }, a < b \). Since \( g \) is convex, the function \( x \mapsto \frac{g\left( x\right) - g\left( a\right) }{x - a} \) is increasing. However, \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) - g\left( a\right) }{x - a} = \mathop{\lim }\limits_{{x \rightarrow + \infty }}\frac{g\left( x\right) }{x} = 0 \). Thus for all \( x \neq a \), \( \frac{g\left( x\right) - g\left( a\right) }{x - a} \leq 0 \). By applying this to \( x = b \), we deduce \( g\left( b\right) \leq g\left( a\right) \).

Une fonction décroissante sur \( {\mathbb{R}}^{ + } \) admet toujours une limite en \( + \infty \) , donc \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = \; \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) - \ell x \) existe. Cette limite appartient à \( \mathbb{R} \cup \{ - \infty \} \) (elle peut valoir \( - \infty \) comme le montre l’exemple de la fonction \( x \mapsto - \log \left( {1 + x}\right) ) \) .

> A decreasing function on \( {\mathbb{R}}^{ + } \) always admits a limit at \( + \infty \), so \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = \; \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) - \ell x \) exists. This limit belongs to \( \mathbb{R} \cup \{ - \infty \} \) (it can be equal to \( - \infty \) as shown by the example of the function \( x \mapsto - \log \left( {1 + x}\right) ) \).

EXERCICE 3 (CRITERE PRATIQUE DE CONVEXITÉ D'UNE FONCTION). Soient \( I \) un in-tervalle \( \mathrm{{de}}\mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application. Montrer que \( f \) est convexe si et seulement si pour tout segment \( \left\lbrack {a, b}\right\rbrack \) inclus dans \( I \) et pour tout \( \mu \in \mathbb{R} \) , l’application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \; \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) est bornée sur \( \left\lbrack {a, b}\right\rbrack \) et atteint sa borne supérieure en \( a \) ou en \( b \) .

> EXERCISE 3 (PRACTICAL CRITERION FOR THE CONVEXITY OF A FUNCTION). Let \( I \) be an interval \( \mathrm{{de}}\mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a mapping. Show that \( f \) is convex if and only if for every segment \( \left\lbrack {a, b}\right\rbrack \) included in \( I \) and for every \( \mu \in \mathbb{R} \), the mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \; \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) is bounded on \( \left\lbrack {a, b}\right\rbrack \) and attains its supremum at \( a \) or at \( b \).

Solution. Condition nécessaire. Soit \( \left\lbrack {a, b}\right\rbrack \) un segment inclus dans \( I \) et \( \mu \in \mathbb{R} \) . L’application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) est convexe sur \( \left\lbrack {a, b}\right\rbrack \) car c’est la somme de deux fonctions convexes. L’un des réels \( \varphi \left( a\right) ,\varphi \left( b\right) \) est donc la borne supérieure de \( \varphi \) car si \( M = \sup \{ \varphi \left( a\right) ,\varphi \left( b\right) \} \) ,

> Solution. Necessary condition. Let \( \left\lbrack {a, b}\right\rbrack \) be a segment included in \( I \) and \( \mu \in \mathbb{R} \). The mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) is convex on \( \left\lbrack {a, b}\right\rbrack \) because it is the sum of two convex functions. One of the real numbers \( \varphi \left( a\right) ,\varphi \left( b\right) \) is therefore the supremum of \( \varphi \) because if \( M = \sup \{ \varphi \left( a\right) ,\varphi \left( b\right) \} \),

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;\varphi \left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right)  \leq   + {\lambda \varphi }\left( a\right)  + \left( {1 - \lambda }\right) \varphi \left( b\right)  \leq  {\lambda M} + \left( {1 - \lambda }\right) M = M.
\]

Condition suffisante. Soit \( \left\lbrack {a, b}\right\rbrack \) un sous-intervalle fermé de \( I \) . On choisit \( \mu \) de sorte que \( \varphi \left( a\right) = \; \varphi \left( b\right) \) , c’est-à-dire que l’on considère l’application

> Sufficient condition. Let \( \left\lbrack {a, b}\right\rbrack \) be a closed sub-interval of \( I \). We choose \( \mu \) such that \( \varphi \left( a\right) = \; \varphi \left( b\right) \), that is to say, we consider the mapping

\[
\varphi  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  f\left( x\right)  - \frac{f\left( b\right)  - f\left( a\right) }{b - a}x.
\]

Ainsi on a bien \( \varphi \left( a\right) = \varphi \left( b\right) \) . Par hypothèse on a

> Thus we have \( \varphi \left( a\right) = \varphi \left( b\right) \). By hypothesis we have

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;\varphi \left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right)  \leq  \varphi \left( a\right)  = \varphi \left( b\right)
\]

et en remplaçant \( \varphi \) par son expression en fonction de \( f \) , on vérifie facilement que ceci s’écrit aussi

> and by replacing \( \varphi \) with its expression as a function of \( f \), we easily verify that this can also be written as

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right)  \leq  {\lambda f}\left( a\right)  + \left( {1 - \lambda }\right) f\left( b\right) .
\]

Ceci étant vrai pour tout \( \left\lbrack {a, b}\right\rbrack \subset I \) , on en déduit que \( f \) est convexe.

> Since this is true for all \( \left\lbrack {a, b}\right\rbrack \subset I \), we deduce that \( f \) is convex.

Remarque. Ce critère rend parfois des services pour démontrer la convexité d'une fonction (voir les deux exercices qui suivent).

> Remark. This criterion is sometimes useful for proving the convexity of a function (see the two following exercises).

EXERCICE 4. Soit \( I \) un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application continue. Montrer que \( f \) est convexe si et seulement si

> EXERCISE 4. Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a continuous mapping. Show that \( f \) is convex if and only if

\[
\forall x \in  I,\forall h > 0\text{ vérifiant }\left( {x - h, x + h}\right)  \in  {I}^{2},\;{2hf}\left( x\right)  \leq  {\int }_{x - h}^{x + h}f\left( t\right) {dt}.
\]

Solution. Condition nécessaire. Soit \( x \in I \) et \( h > 0 \) tel que \( \left( {x - h, x + h}\right) \in {I}^{2} \) . On a

> Solution. Necessary condition. Let \( x \in I \) and \( h > 0 \) be such that \( \left( {x - h, x + h}\right) \in {I}^{2} \). We have

\[
\forall t \in  \left\lbrack  {0, h}\right\rbrack  ,\;f\left( x\right)  = f\left( \frac{\left( {x - t}\right)  + \left( {x + t}\right) }{2}\right)  \leq  \frac{1}{2}\left( {f\left( {x - t}\right)  + f\left( {x + t}\right) }\right) ,
\]

et en intégrant cette inégalité pour \( t \in \left\lbrack {0, h}\right\rbrack \) on obtient

> and by integrating this inequality for \( t \in \left\lbrack {0, h}\right\rbrack \) we obtain

\[
{\int }_{x}^{x + h}f\left( x\right) {dt} \leq  \frac{1}{2}\left\lbrack  {{\int }_{x - h}^{x}f\left( t\right) {dt} + {\int }_{x}^{x + h}f\left( t\right) {dt}}\right\rbrack
\]

d'où le résultat.

> whence the result.

Condition suffisante. Utilisons le critère de l'exercice 3. Si \( f \) n'était pas convexe, il existerait un sous-intervalle fermé \( \left\lbrack {a, b}\right\rbrack \) de \( I \) et \( \mu \in \mathbb{R} \) tels que l’application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) n’admet pas son maximum en \( a \) ou en \( b \) . L’application \( \varphi \) étant continue, il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( \varphi \left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\varphi \left( x\right) \) , et par construction, on a \( \varphi \left( c\right) > \varphi \left( a\right) \) et \( \varphi \left( c\right) > \varphi \left( b\right) \) . Soit \( h = \inf \{ b - c, c - a\} \) . La continuité de \( \varphi \) entraîne

> Sufficient condition. Let us use the criterion from exercise 3. If \( f \) were not convex, there would exist a closed sub-interval \( \left\lbrack {a, b}\right\rbrack \) of \( I \) and \( \mu \in \mathbb{R} \) such that the mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + {\mu x} \) does not attain its maximum at \( a \) or at \( b \). Since the mapping \( \varphi \) is continuous, there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( \varphi \left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\varphi \left( x\right) \), and by construction, we have \( \varphi \left( c\right) > \varphi \left( a\right) \) and \( \varphi \left( c\right) > \varphi \left( b\right) \). Let \( h = \inf \{ b - c, c - a\} \). The continuity of \( \varphi \) implies

\[
{\int }_{c - h}^{c + h}\varphi \left( t\right) {dt} < {\int }_{c - h}^{c + h}\varphi \left( c\right) {dt} = {2h\varphi }\left( c\right) ,
\]

et en remplaçant \( \varphi \) par son expression en fonction de \( f \) , on obtient

> and by replacing \( \varphi \) with its expression as a function of \( f \), we obtain

\[
{\int }_{c - h}^{c + h}f\left( t\right) {dt} < {2hf}\left( c\right) .
\]

Ceci est contraire aux hypothèses. La fonction \( f \) est donc convexe.

> This contradicts the hypotheses. The function \( f \) is therefore convex.

EXERCICE 5. Soit \( I \) un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application continue. a) Montrer que \( f \) est convexe si et seulement si

> EXERCISE 5. Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a continuous mapping. a) Show that \( f \) is convex if and only if

\[
\forall x \in  \overset{ \circ  }{I},\forall \varepsilon  > 0,\exists h \in  \rbrack 0,\varepsilon \lbrack ,\;f\left( x\right)  \leq  \frac{1}{2}\left\lbrack  {f\left( {x + h}\right)  + f\left( {x - h}\right) }\right\rbrack  .
\]

(on pourra utiliser le résultat de l'exercice 3).

> (one may use the result of exercise 3).

b) Montrer que \( f \) est convexe si

> b) Show that \( f \) is convex if

\[
\forall x \in  \overset{ \circ  }{I},\;\mathop{\lim }\limits_{\substack{{\ell  \rightarrow  0} \\  {\ell  > 0} }}\mathop{\sup }\limits_{{\left| h\right|  \leq  \ell }}\frac{f\left( {x + h}\right)  + f\left( {x - h}\right)  - {2f}\left( x\right) }{{h}^{2}} \geq  0
\]

c) Montrer que \( f \) est affine si

> c) Show that \( f \) is affine if

\[
\forall x \in  \overset{ \circ  }{I},\;\mathop{\lim }\limits_{\substack{{h \rightarrow  0} \\  {h > 0} }}\frac{f\left( {x + h}\right)  + f\left( {x - h}\right)  - {2f}\left( x\right) }{{h}^{2}} = 0,
\]

Solution. a) La condition nécessaire est évidente. Pour montrer la condition suffisante, nous allons utiliser le critère donné dans l'exercice 3.

> Solution. a) The necessary condition is obvious. To show the sufficient condition, we will use the criterion given in exercise 3.

Soit \( \left\lbrack {a, b}\right\rbrack \subset I \) et \( \mu \in \mathbb{R} \) . On vérifie immédiatement que l’application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \; f\left( x\right) + {\mu x} \) vérifie les mêmes hypothèses que \( f \) . Il s’agit de montrer que \( \varphi \) atteint son maximum sur \( \left\lbrack {a, b}\right\rbrack \) en \( a \) ou en \( b \) . Comme \( \varphi \) est continue sur le compact \( \left\lbrack {a, b}\right\rbrack ,\varphi \) est bornée et atteint ses bornes. Si on désigne par \( M \) son maximum, l’ensemble \( \Gamma = {\varphi }^{-1}\left( {\{ M\} }\right) \) est donc non vide. Soit \( c = \inf \Gamma \) . La continuité de \( \varphi \) entraîne que \( \Gamma \) est fermé, donc \( c \in \Gamma \) , donc \( \varphi \left( c\right) = M \) . Si \( a < c < b \) , alors par hypothèse

> Let \( \left\lbrack {a, b}\right\rbrack \subset I \) and \( \mu \in \mathbb{R} \). We immediately verify that the mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \; f\left( x\right) + {\mu x} \) satisfies the same hypotheses as \( f \). It is a matter of showing that \( \varphi \) attains its maximum on \( \left\lbrack {a, b}\right\rbrack \) at \( a \) or at \( b \). Since \( \varphi \) is continuous on the compact \( \left\lbrack {a, b}\right\rbrack ,\varphi \), it is bounded and attains its bounds. If we denote its maximum by \( M \), the set \( \Gamma = {\varphi }^{-1}\left( {\{ M\} }\right) \) is therefore non-empty. Let \( c = \inf \Gamma \). The continuity of \( \varphi \) implies that \( \Gamma \) is closed, therefore \( c \in \Gamma \), therefore \( \varphi \left( c\right) = M \). If \( a < c < b \), then by hypothesis

\[
\exists h > 0,\;\left( {a < c - h < c < c + h < b\text{ et }\varphi \left( c\right)  \leq  \frac{1}{2}\left\lbrack  {\varphi \left( {c - h}\right)  + \varphi \left( {c + h}\right) }\right\rbrack  }\right) .
\]

Comme \( \varphi \left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\varphi \left( x\right) \) , cette dernière inégalité entraîne \( \varphi \left( {c - h}\right) = \varphi \left( {c + h}\right) = \varphi \left( c\right) = M \) , ce qui est contradictoire avec la définition de \( c \) . Donc \( c = a \) ou \( c = b \) et le résultat est prouvé.

> As \( \varphi \left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\varphi \left( x\right) \) , this last inequality leads to \( \varphi \left( {c - h}\right) = \varphi \left( {c + h}\right) = \varphi \left( c\right) = M \) , which contradicts the definition of \( c \) . Therefore \( c = a \) or \( c = b \) and the result is proven.

b) Pour tout \( \alpha > 0 \) , on définit l’application \( {f}_{\alpha } : I \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + \alpha {x}^{2} \) . On a

> b) For all \( \alpha > 0 \) , we define the mapping \( {f}_{\alpha } : I \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) + \alpha {x}^{2} \) . We have

\[
\forall x \in  I,\forall h > 0,\;\frac{{f}_{\alpha }\left( {x + h}\right)  + {f}_{\alpha }\left( {x - h}\right)  - 2{f}_{\alpha }\left( x\right) }{{h}^{2}} = \frac{f\left( {x + h}\right)  + f\left( {x - h}\right)  - {2f}\left( x\right) }{{h}^{2}} + {2\alpha },
\]

et donc en vertu des hypothèses vérifiées par \( f \) ,

> and therefore, by virtue of the hypotheses satisfied by \( f \) ,

\[
\forall \varepsilon  > 0,\forall x \in  \overset{ \circ  }{I},\exists h \in  \rbrack 0,\varepsilon \left\lbrack  {,\;\frac{{f}_{\alpha }\left( {x + h}\right)  + {f}_{\alpha }\left( {x - h}\right)  - 2{f}_{\alpha }\left( x\right) }{{h}^{2}} \geq  \alpha  > 0,}\right.
\]

ce qui entraîne

> which leads to

\[
\forall \varepsilon  > 0,\forall x \in  \overset{ \circ  }{I},\exists h \in  \rbrack 0,\varepsilon \lbrack ,\;{f}_{\alpha }\left( x\right)  \leq  \frac{1}{2}\left\lbrack  {{f}_{\alpha }\left( {x + h}\right)  + {f}_{\alpha }\left( {x - h}\right) }\right\rbrack  ,
\]

ce qui prouve la convexité de \( {f}_{\alpha } \) d’après le résultat de la question précédente.

> which proves the convexity of \( {f}_{\alpha } \) according to the result of the previous question.

Ainsi l’application \( f \) , limite simple de fonctions convexes (les applications \( {f}_{\alpha } \) lorsque \( \alpha \rightarrow 0 + \) ) est convexe.

> Thus the mapping \( f \) , a simple limit of convex functions (the mappings \( {f}_{\alpha } \) when \( \alpha \rightarrow 0 + \) ) is convex.

c) L'application \( f \) vérifie les hypothèses de la question précédente donc est convexe. Ceci est vrai également pour \( - f \) donc \( f \) est concave. Une fonction convexe et concave est forcément affine, d'où le résultat.

> c) The mapping \( f \) satisfies the hypotheses of the previous question and is therefore convex. This is also true for \( - f \) , so \( f \) is concave. A convex and concave function is necessarily affine, hence the result.

Remarque. Un corollaire du résultat de la question a) est le suivant.

> Remark. A corollary of the result of question a) is as follows.

Si \( f \) est continue sur I et vérifie \( f\left( \frac{x + y}{2}\right) \leq \frac{1}{2}\left\lbrack {f\left( x\right) + f\left( y\right) }\right\rbrack \) pour tout \( \left( {x, y}\right) \in {I}^{2} \) , alors \( f \) est convexe.

> If \( f \) is continuous on I and satisfies \( f\left( \frac{x + y}{2}\right) \leq \frac{1}{2}\left\lbrack {f\left( x\right) + f\left( y\right) }\right\rbrack \) for all \( \left( {x, y}\right) \in {I}^{2} \) , then \( f \) is convex.

Ceci peut être démontré directement, en procédant comme suit :

> This can be proven directly by proceeding as follows:

- On se donne \( x \) et \( y \in  I \) .

> - Let \( x \) and \( y \in  I \) be given.

- On montre par récurrence sur \( n \) que pour tout entier \( k \) compris entre 0 et \( {2}^{n} \) , on a \( f\left( \frac{{kx} + \left( {{2}^{n} - k}\right) y}{{2}^{n}}\right)  \leq  \frac{{kf}\left( x\right)  + \left( {{2}^{n} - k}\right) f\left( y\right) }{{2}^{n}}. \)

> - We show by induction on \( n \) that for any integer \( k \) between 0 and \( {2}^{n} \) , we have \( f\left( \frac{{kx} + \left( {{2}^{n} - k}\right) y}{{2}^{n}}\right)  \leq  \frac{{kf}\left( x\right)  + \left( {{2}^{n} - k}\right) f\left( y\right) }{{2}^{n}}. \)

- En utilisant la continuité de \( f \) et la densité des nombres de la forme \( k/{2}^{n}\left( {k \in  \mathbb{Z}}\right. \) , \( n \in  \mathbb{N} \) ), on provue que \( f\left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right)  \leq  {\lambda f}\left( x\right)  + \left( {1 - \lambda }\right) f\left( y\right) \) pour tout \( \lambda  \in  \left\lbrack  {0,1}\right\rbrack \) .

> - Using the continuity of \( f \) and the density of numbers of the form \( k/{2}^{n}\left( {k \in  \mathbb{Z}}\right. \) , \( n \in  \mathbb{N} \) ), we prove that \( f\left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right)  \leq  {\lambda f}\left( x\right)  + \left( {1 - \lambda }\right) f\left( y\right) \) for all \( \lambda  \in  \left\lbrack  {0,1}\right\rbrack \) .

EXERCICE 6 (FONCTIONS LOGARITHMIQUEMENT CONVEXES). On dit qu'une fonction \( f \) à valeurs dans ] \( 0, + \infty \lbrack \) est logarithmiquement convexe si la fonction log \( f \) est convexe.

> EXERCISE 6 (LOGARITHMICALLY CONVEX FUNCTIONS). A function \( f \) with values in ] \( 0, + \infty \lbrack \) is said to be logarithmically convex if the function log \( f \) is convex.

Soit \( I \) un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow {\mathbb{R}}^{+ * } \) une application.

> Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow {\mathbb{R}}^{+ * } \) a mapping.

a) Montrer que si \( f \) est logarithmiquement convexe, alors \( f \) est convexe.

> a) Show that if \( f \) is logarithmically convex, then \( f \) is convex.

b) Montrer que \( f \) est logarithmiquement convexe si et seulement si l’application \( I \rightarrow \; {\mathbb{R}}^{+ * }\;x \mapsto f\left( x\right) {c}^{x} \) est convexe pour tout \( c > 0 \) .

> b) Show that \( f \) is logarithmically convex if and only if the mapping \( I \rightarrow \; {\mathbb{R}}^{+ * }\;x \mapsto f\left( x\right) {c}^{x} \) is convex for all \( c > 0 \) .

c) Montrer que si \( f \) et \( g : I \rightarrow {\mathbb{R}}^{+ * } \) sont logarithmiquement convexes, alors \( f + g \) aussi.

> c) Show that if \( f \) and \( g : I \rightarrow {\mathbb{R}}^{+ * } \) are logarithmically convex, then \( f + g \) is as well.

Solution. a) Soient \( a, b \in I \) et \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . On a

> Solution. a) Let \( a, b \in I \) and \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . We have

\[
\log \left\lbrack  {f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right) }\right\rbrack   \leq  \lambda \log f\left( a\right)  + \left( {1 - \lambda }\right) \log f\left( b\right)  \leq  \log \left\lbrack  {\left( {1 - \lambda }\right) f\left( a\right)  + {\lambda f}\left( b\right) }\right\rbrack
\]

(la première inégalité résulte des hypothèses et la seconde résulte de la concavité de l'application logarithme). En ne considérant maintenant les membres extrêmes de ces inégalités, on en déduit, en vertu du caractère croissant de la fonction logarithme \( f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right) \leq {\lambda f}\left( a\right) + \left( {1 - \lambda }\right) f\left( b\right) \) , d'où le résultat.

> (the first inequality follows from the hypotheses and the second follows from the concavity of the logarithm mapping). By considering only the extreme members of these inequalities, we deduce, by virtue of the increasing nature of the logarithm function \( f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right) \leq {\lambda f}\left( a\right) + \left( {1 - \lambda }\right) f\left( b\right) \) , hence the result.

b) Condition nécessaire. Pour tout \( c > 0 \) , l’application \( x \mapsto \log f\left( x\right) + x\log c \) est convexe (somme de deux fonctions convexes), autrement dit \( x \mapsto \log \left( {f\left( x\right) {c}^{x}}\right) \) est convexe. D’après la question précédente, ceci entraîne la convexité de \( x \mapsto f\left( x\right) {c}^{x} \) .

> b) Necessary condition. For all \( c > 0 \) , the mapping \( x \mapsto \log f\left( x\right) + x\log c \) is convex (sum of two convex functions), in other words \( x \mapsto \log \left( {f\left( x\right) {c}^{x}}\right) \) is convex. According to the previous question, this implies the convexity of \( x \mapsto f\left( x\right) {c}^{x} \) .

Condition suffisante. Soient \( \left( {a, b}\right) \in {I}^{2} \) et \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . D’après les hypothèses, on a

> Sufficient condition. Let \( \left( {a, b}\right) \in {I}^{2} \) and \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . According to the hypotheses, we have

\[
\forall c > 0,\;f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right) {c}^{{\lambda a} + \left( {1 - \lambda }\right) b} \leq  {\lambda f}\left( a\right) {c}^{a} + \left( {1 - \lambda }\right) f\left( b\right) {c}^{b}.
\]

Ceci s'écrit aussi

> This can also be written

\[
\forall c > 0,\;f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right)  \leq  {\lambda f}\left( a\right) {c}^{\left( {1 - \lambda }\right) \left( {a - b}\right) } + \left( {1 - \lambda }\right) f\left( b\right) {c}^{\lambda \left( {b - a}\right) } = {\lambda f}\left( a\right) {\alpha }^{\left( 1 - \lambda \right) } + \left( {1 - \lambda }\right) f\left( b\right) {\alpha }^{-\lambda },
\]

(*)

> où on a posé \( \alpha = {c}^{a - b} \) . L’idée est maintenant de minimiser le terme de droite de cette dernière équation pour avoir la majoration la plus fine possible du membre de gauche. Les paramètres \( a, b,\lambda \) étant fixés, une étude de la fonction \( \alpha \mapsto {\lambda f}\left( a\right) {\alpha }^{\left( 1 - \lambda \right) } + \left( {1 - \lambda }\right) f\left( b\right) {\alpha }^{-\lambda } \) montre qu’elle atteint son minimum sur \( {\mathbb{R}}^{+ * } \) en \( \alpha = f\left( b\right) /f\left( a\right) \) , valeur en laquelle elle vaut précisément \( f{\left( a\right) }^{\lambda }f{\left( b\right) }^{1 - \lambda } \) . En remplaçant dans (*) avec cette valeur de \( \alpha \) , on en déduit

where we have set \( \alpha = {c}^{a - b} \) . The idea is now to minimize the right-hand term of this last equation to obtain the finest possible upper bound for the left-hand side. With the parameters \( a, b,\lambda \) fixed, a study of the function \( \alpha \mapsto {\lambda f}\left( a\right) {\alpha }^{\left( 1 - \lambda \right) } + \left( {1 - \lambda }\right) f\left( b\right) {\alpha }^{-\lambda } \) shows that it reaches its minimum on \( {\mathbb{R}}^{+ * } \) at \( \alpha = f\left( b\right) /f\left( a\right) \) , a value at which it is precisely \( f{\left( a\right) }^{\lambda }f{\left( b\right) }^{1 - \lambda } \) . By substituting into (*) with this value of \( \alpha \) , we deduce

\[
f\left( {{\lambda a} + \left( {1 - \lambda }\right) b}\right)  \leq  f{\left( a\right) }^{\lambda }f{\left( b\right) }^{1 - \lambda }.
\]

En prenant le logarithme, on en déduit alors la convexité de log \( f \) .

> By taking the logarithm, we then deduce the convexity of log \( f \) .

c) Il suffit d'utiliser le résultat de la question précédente (sans laquelle le résultat serait difficile à prouver), en montrant que pour tout \( c > 0 \) , l’application \( x \mapsto \left( {f\left( x\right) + g\left( x\right) }\right) {c}^{x} \) est convexe. Ceci est immédiat car toujours d’après le résultat de la question précédente, les fonctions \( x \mapsto f\left( x\right) {c}^{x} \) et \( x \mapsto g\left( x\right) {c}^{x} \) sont convexes pour tout \( c > 0 \) .

> c) It suffices to use the result of the previous question (without which the result would be difficult to prove), by showing that for all \( c > 0 \) , the mapping \( x \mapsto \left( {f\left( x\right) + g\left( x\right) }\right) {c}^{x} \) is convex. This is immediate because, still according to the result of the previous question, the functions \( x \mapsto f\left( x\right) {c}^{x} \) and \( x \mapsto g\left( x\right) {c}^{x} \) are convex for all \( c > 0 \) .
