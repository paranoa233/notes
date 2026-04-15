#### 4.2. Gronwall's Lemma and applications

*Français : 4.2. Lemme de Gronwall et applications*

On a parfois affaire à des inégalités portant sur une fonction et sa dérivée. Ce type de problème peut être résolu grâce au résultat qui suit.

> We are sometimes faced with inequalities involving a function and its derivative. This type of problem can be solved using the following result.

\( \rightarrow \) THÉORÉME 1 (LEMME DE GRONWALL). Soient \( \varphi ,\psi \) et \( y \) trois fonctions continues sur un segment \( \left\lbrack {a, b}\right\rbrack \) ,à valeurs positives et vérifiant l’inégalité

> \( \rightarrow \) THEOREM 1 (GRONWALL'S LEMMA). Let \( \varphi ,\psi \) and \( y \) be three continuous functions on a segment \( \left\lbrack {a, b}\right\rbrack \), taking positive values and satisfying the inequality

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;y\left( t\right)  \leq  \varphi \left( t\right)  + {\int }_{a}^{t}\psi \left( s\right) y\left( s\right) {ds}.
\]

(*)

> Alors

Then

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;y\left( t\right)  \leq  \varphi \left( t\right)  + {\int }_{a}^{t}\varphi \left( s\right) \psi \left( s\right) \exp \left( {{\int }_{s}^{t}\psi \left( u\right) {du}}\right) {ds}.
\]

Démonstration. Posons \( F\left( t\right) = {\int }_{a}^{t}\psi \left( s\right) y\left( s\right) {ds} \) . En multipliant les deux membres de (*) par \( \psi \left( t\right) \) , on obtient \( {F}^{\prime }\left( t\right) - \psi \left( t\right) F\left( t\right) \leq \varphi \left( t\right) \psi \left( t\right) \) , ce qui s’écrit aussi

> Proof. Let \( F\left( t\right) = {\int }_{a}^{t}\psi \left( s\right) y\left( s\right) {ds} \) . Multiplying both sides of (*) by \( \psi \left( t\right) \) , we obtain \( {F}^{\prime }\left( t\right) - \psi \left( t\right) F\left( t\right) \leq \varphi \left( t\right) \psi \left( t\right) \) , which can also be written as

\[
{G}^{\prime }\left( t\right)  \leq  \varphi \left( t\right) \psi \left( t\right) \exp \left( {-{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) \;\text{ avec }\;G\left( t\right)  = F\left( t\right) \exp \left( {-{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) .
\]

Comme \( G\left( a\right) = F\left( a\right) = 0 \) , on en déduit, par intégration

> Since \( G\left( a\right) = F\left( a\right) = 0 \) , we deduce, by integration

\[
G\left( t\right)  \leq  {\int }_{a}^{t}\varphi \left( s\right) \psi \left( s\right) \exp \left( {-{\int }_{a}^{s}\psi \left( u\right) {du}}\right) {ds}.
\]

Or, d’après \( \left( *\right) , y\left( t\right) \leq \varphi \left( t\right) + G\left( t\right) \exp \left( {{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) \) , d’où le résultat en utilisant l’inégalité ci dessus.

> However, according to \( \left( *\right) , y\left( t\right) \leq \varphi \left( t\right) + G\left( t\right) \exp \left( {{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) \) , hence the result using the inequality above.

Ce théorème n'est pas au programme des classes de mathématiques spéciales. Il n'est pas nécessaire de connaître le résultat, mais il faut en revanche savoir le retrouver fa-cilement, et se souvenir que le lemme de Gronwall exprime qu'à partir d'une inégalité intégrale portant sur \( y \) , on peut en déduire une inégalité sur \( y \) .

> This theorem is not in the curriculum for special mathematics classes. It is not necessary to know the result, but one must be able to derive it easily and remember that Gronwall's lemma expresses that from an integral inequality involving \( y \) , one can deduce an inequality on \( y \) .

On utilise parfois le lemme de Gronwall dans le cas particulier suivant.

> Gronwall's lemma is sometimes used in the following special case.

COROLLAIRE 1. Soient \( \psi \) et \( y : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{ + } \) deux fonctions continues et vérifiant

> COROLLARY 1. Let \( \psi \) and \( y : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{ + } \) be two continuous functions satisfying

\[
\exists c \geq  0,\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;y\left( t\right)  \leq  c + {\int }_{a}^{t}\psi \left( s\right) y\left( s\right) {ds}.
\]

Alors

> Then

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;y\left( t\right)  \leq  c\exp \left( {{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) .
\]

Démonstration. Il s'agit du lemme de Gronwall dans le cas particulier où \( \varphi \) est la fonction constante égale à \( c \) , on a donc pour tout \( t \in \left\lbrack {a, b}\right\rbrack \)

> Proof. This is Gronwall's lemma in the special case where \( \varphi \) is the constant function equal to \( c \) , so for all \( t \in \left\lbrack {a, b}\right\rbrack \) we have

\[
y\left( t\right)  \leq  c + {\int }_{a}^{t}{c\psi }\left( s\right) \exp \left( {{\int }_{s}^{t}\psi \left( u\right) {du}}\right) {ds} = c - c{\left\lbrack  \exp \left( {\int }_{s}^{t}\psi \left( u\right) du\right) \right\rbrack  }_{s = a}^{s = t} = c\exp \left( {{\int }_{a}^{t}\psi \left( s\right) {ds}}\right) .
\]

Entraînez vous à démontrer ce corollaire directement, sans utiliser le lemme de Gron-wall général.

> Practice proving this corollary directly, without using the general Gronwall's lemma.

Citons enfin une application intéressante du lemme de Gronwall, utile dans les majo-rations d'erreurs sur les solutions d'équations différentielles.

> Finally, let us cite an interesting application of Gronwall's lemma, useful for error bounds on solutions to differential equations.

COROLLAIRE 2. Soit \( y : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{n} \) une fonction de classe \( {\mathcal{C}}^{1} \) vérifiant

> COROLLARY 2. Let \( y : \left\lbrack {a, b}\right\rbrack \rightarrow {\mathbb{R}}^{n} \) be a function of class \( {\mathcal{C}}^{1} \) satisfying

\[
\exists \alpha  > 0,\exists \beta  \geq  0,\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;\begin{Vmatrix}{{y}^{\prime }\left( t\right) }\end{Vmatrix} \leq  \beta  + \alpha \parallel y\left( t\right) \parallel .
\]

Alors

> Then

\[
\forall t \in  \left\lbrack  {a, b}\right\rbrack  ,\;\parallel y\left( t\right) \parallel  \leq  \parallel y\left( a\right) \parallel {e}^{\alpha \left( {t - a}\right) } + \frac{\beta }{\alpha }\left( {{e}^{\alpha \left( {t - a}\right) } - 1}\right) .
\]

Démonstration. Il suffit d’écrire, pour tout \( t \in \left\lbrack {a, b}\right\rbrack \) ,

> Proof. It suffices to write, for all \( t \in \left\lbrack {a, b}\right\rbrack \) ,

\[
\parallel y\left( t\right) \parallel  \leq  \parallel y\left( a\right) \parallel  + \parallel y\left( t\right)  - y\left( a\right) \parallel  \leq  \parallel y\left( a\right) \parallel  + {\int }_{a}^{t}\begin{Vmatrix}{{y}^{\prime }\left( t\right) }\end{Vmatrix}{dt} \leq  \parallel y\left( a\right) \parallel  + \beta \left( {t - a}\right)  + \alpha {\int }_{a}^{t}\parallel y\left( s\right) \parallel {ds},
\]

puis on applique le lemme de Gronwall et on conclut en intégrant par parties.

> then apply Gronwall's lemma and conclude by integrating by parts.

Exercices.

> Exercises.

EXERCICE 1. Soit \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) , strictement positive et croissante. Montrer que toutes les solutions de l’équation différentielle \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) sont bornées sur \( {\mathbb{R}}^{ + } \) .

> EXERCISE 1. Let \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{1} \) , strictly positive and increasing. Show that all solutions to the differential equation \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) are bounded on \( {\mathbb{R}}^{ + } \) .

Solution. On va chercher à utiliser le lemme de Gronwall. Soit \( y \) une solution de \( \left( L\right) \) sur \( {\mathbb{R}}^{ + } \) . On a \( 2{y}^{\prime }{y}^{\prime \prime } + {2q}\left( t\right) y{y}^{\prime } = 0 \) , donc par intégration

> Solution. We will seek to use Gronwall's lemma. Let \( y \) be a solution of \( \left( L\right) \) on \( {\mathbb{R}}^{ + } \) . We have \( 2{y}^{\prime }{y}^{\prime \prime } + {2q}\left( t\right) y{y}^{\prime } = 0 \) , so by integration

\[
\forall t \in  {\mathbb{R}}^{ + },\;{y}^{\prime }{\left( t\right) }^{2} - {y}^{\prime }{\left( 0\right) }^{2} + 2{\int }_{0}^{t}q\left( s\right) y\left( s\right) {y}^{\prime }\left( s\right) {ds} = 0,
\]

et en intégrant par parties, on obtient

> and integrating by parts, we obtain

\[
\forall t \in  {\mathbb{R}}^{ + },\;{y}^{\prime }{\left( t\right) }^{2} + q\left( t\right) y{\left( t\right) }^{2} = K + {\int }_{0}^{t}{q}^{\prime }\left( s\right) y{\left( s\right) }^{2}{ds},\;K = {y}^{\prime }{\left( 0\right) }^{2} + q\left( 0\right) y{\left( 0\right) }^{2}.
\]

On a donc

> We therefore have

\[
\forall t \in  {\mathbb{R}}^{ + },\;q\left( t\right) y{\left( t\right) }^{2} \leq  K + {\int }_{0}^{t}\frac{{q}^{\prime }\left( s\right) }{q\left( s\right) }q\left( s\right) {y}^{2}\left( s\right) {ds}.
\]

En appliquant le premier corollaire du lemme de Gronwall à la fonction \( q{y}^{2} \) , on en déduit

> Applying the first corollary of Gronwall's lemma to the function \( q{y}^{2} \) , we deduce

\[
\forall t \in  {\mathbb{R}}^{ + },\;q\left( t\right) y{\left( t\right) }^{2} \leq  K\exp \left( {{\int }_{0}^{t}\frac{{q}^{\prime }\left( s\right) }{q\left( s\right) }{ds}}\right)  = K\frac{q\left( t\right) }{q\left( 0\right) },
\]

donc \( y{\left( t\right) }^{2} \leq K/q\left( 0\right) \) pour tout \( t \in {\mathbb{R}}^{ + } \) , d’où le résultat.

> thus \( y{\left( t\right) }^{2} \leq K/q\left( 0\right) \) for all \( t \in {\mathbb{R}}^{ + } \) , whence the result.

EXERCICE 2. Soit \( F : \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;\left( {t, x}\right) \mapsto F\left( {t, x}\right) \) une fonction de classe \( {\mathcal{C}}^{1} \) et globalement lipschitzienne en \( x \) , i.e

> EXERCISE 2. Let \( F : \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;\left( {t, x}\right) \mapsto F\left( {t, x}\right) \) be a function of class \( {\mathcal{C}}^{1} \) and globally Lipschitz in \( x \) , i.e.

\[
\exists C > 0,\forall t \in  \mathbb{R},\forall x, y \in  {\mathbb{R}}^{n},\;\parallel F\left( {t, x}\right)  - F\left( {t, y}\right) \parallel  \leq  C\parallel x - y\parallel .
\]

On pose \( G = F + f \) , où \( f : \mathbb{R} \times {\mathbb{R}}^{n} \) est une fonction de classe \( {\mathcal{C}}^{1} \) qui vérifie \( \parallel f\left( {t, x}\right) \parallel \leq \varepsilon \) pour tout \( \left( {t, x}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \) , où \( \varepsilon > 0 \) est fixé.

> Let \( G = F + f \) , where \( f : \mathbb{R} \times {\mathbb{R}}^{n} \) is a function of class \( {\mathcal{C}}^{1} \) satisfying \( \parallel f\left( {t, x}\right) \parallel \leq \varepsilon \) for all \( \left( {t, x}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \) , where \( \varepsilon > 0 \) is fixed.

On suppose que les deux problèmes différentiels

> Assume that the two differential problems

\[
\left\{  {\begin{array}{l} {x}^{\prime } = F\left( {t, x}\right) \\  x\left( 0\right)  = {x}_{0} \end{array}\;\text{ et }\;\left\{  \begin{array}{l} {y}^{\prime } = G\left( {t, y}\right) \\  y\left( 0\right)  = {y}_{0} \end{array}\right. }\right.
\]

admettent respectivement une solution \( x \) et \( y \) , définies sur un même intervalle \( \left\lbrack {0, T}\right\rbrack \) de \( \mathbb{R} \) . Montrer

> admit respectively a solution \( x \) and \( y \) , defined on the same interval \( \left\lbrack {0, T}\right\rbrack \) of \( \mathbb{R} \) . Show

\[
\forall t \in  \left\lbrack  {0, T}\right\rbrack  ,\;\parallel x\left( t\right)  - y\left( t\right) \parallel  \leq  \begin{Vmatrix}{{x}_{0} - {y}_{0}}\end{Vmatrix}{e}^{Ct} + \frac{\varepsilon }{C}\left( {{e}^{Ct} - 1}\right) .
\]

Solution. Posons \( u = x - y \) . Pour tout \( t \in \left\lbrack {0, T}\right\rbrack \) , on a

> Solution. Let \( u = x - y \) . For all \( t \in \left\lbrack {0, T}\right\rbrack \) , we have

\[
\begin{Vmatrix}{{u}^{\prime }\left( t\right) }\end{Vmatrix} = \begin{Vmatrix}{{x}^{\prime }\left( t\right)  - {y}^{\prime }\left( t\right) }\end{Vmatrix} = \parallel F\left( {t, x\left( t\right) }\right)  - G\left( {t, y\left( t\right) }\right) \parallel  = \parallel F\left( {t, x\left( t\right) }\right)  - F\left( {t, y\left( t\right) }\right)  - f\left( {t, y\left( t\right) }\right) \parallel
\]

\[
\leq  \parallel F\left( {t, x\left( t\right) }\right)  - F\left( {t, y\left( t\right) }\right) \parallel  + \parallel f\left( {t, y\left( t\right) }\right) \parallel  \leq  C\parallel u\left( t\right) \parallel  + \varepsilon ,
\]

et il suffit ensuite d'appliquer le second corollaire du lemme de Gronwall.

> and it then suffices to apply the second corollary of Gronwall's lemma.

Remarque. Ce résultat entraîne qu'une petite variation de la vitesse initiale d'un point matériel et une petite variation du champ de forces auquel est soumis ce point entraîne une petite variation de sa trajectoire.

> Remark. This result implies that a small variation in the initial velocity of a material point and a small variation in the force field to which this point is subjected leads to a small variation in its trajectory.
