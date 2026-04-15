#### 3.2. Regulated functions

*Français : 3.2. Fonctions réglées*

Dans cette partie, \( E \) désigne un \( \mathbb{R} \) -espace de Banach, et \( \left\lbrack {a, b}\right\rbrack \) désigne un segment de \( \mathbb{R} \) non réduit à un singleton.

> In this part, \( E \) denotes a Banach \( \mathbb{R} \) -space, and \( \left\lbrack {a, b}\right\rbrack \) denotes a segment of \( \mathbb{R} \) not reduced to a singleton.

DÉFINITION 2. Une application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) est dite en escalier s’il existe une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que pour tout \( i,\varphi \) soit constante sur \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) .

> DEFINITION 2. A mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) is called a step function if there exists a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that for all \( i,\varphi \) it is constant on \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) .

DÉFINITION 3. Une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) est dite réglée si elle est limite uniforme sur \( \left\lbrack {a, b}\right\rbrack \) de fonctions en escalier. En d’autres termes, \( f \) est réglée si pour tout \( \varepsilon > 0 \) , il existe une fonction \( \varphi \) est escalier telle que \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) .

> DEFINITION 3. A mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) is called regulated if it is a uniform limit on \( \left\lbrack {a, b}\right\rbrack \) of step functions. In other words, \( f \) is regulated if for all \( \varepsilon > 0 \) , there exists a step function \( \varphi \) such that \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) for all \( x \in \left\lbrack {a, b}\right\rbrack \) .

Proposition 4. Une fonction réglée sur \( \left\lbrack {a, b}\right\rbrack \) est bornée.

> Proposition 4. A regulated function on \( \left\lbrack {a, b}\right\rbrack \) is bounded.

Démonstration. Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une fonction réglée. Il existe une fonction en escalier \( \varphi \) telle que \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < 1 \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) . Comme \( \varphi \) est en escalier, \( \varphi \) est bornée. Soit \( M \) un majorant de \( \parallel \varphi \parallel \) sur \( \left\lbrack {a, b}\right\rbrack \) . Pour tout \( x \in \left\lbrack {a, b}\right\rbrack ,\parallel f\left( x\right) \parallel < 1 + \parallel \varphi \left( x\right) \parallel \leq 1 + M \) , ce qui prouve le résultat.

> Proof. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a regulated function. There exists a step function \( \varphi \) such that \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < 1 \) for all \( x \in \left\lbrack {a, b}\right\rbrack \) . Since \( \varphi \) is a step function, \( \varphi \) is bounded. Let \( M \) be an upper bound of \( \parallel \varphi \parallel \) on \( \left\lbrack {a, b}\right\rbrack \) . For all \( x \in \left\lbrack {a, b}\right\rbrack ,\parallel f\left( x\right) \parallel < 1 + \parallel \varphi \left( x\right) \parallel \leq 1 + M \) , which proves the result.

DÉFINITION 4. Une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) est dite continue par morceaux s’il existe une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que la restriction de \( f \) à chaque intervalle ouvert \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) soit prolongeable en une fonction continue sur l’intervalle fermé \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) .

> DEFINITION 4. A mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) is said to be piecewise continuous if there exists a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that the restriction of \( f \) to each open interval \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) can be extended to a continuous function on the closed interval \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) .

Remarque 3. - La condition "prolongeable en une fonction continue sur \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) " est importante ; elle équivaut à dire que la limite à droite (resp. à gauche) de \( f\left( x\right) \) lorsque \( x \) tend vers \( {x}_{i - 1} \) (resp. vers \( {x}_{i} \) ) existe.

> Remark 3. - The condition "can be extended to a continuous function on \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) " is important; it is equivalent to saying that the right-hand (resp. left-hand) limit of \( f\left( x\right) \) as \( x \) approaches \( {x}_{i - 1} \) (resp. \( {x}_{i} \) ) exists.

- L’ensemble \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) des fonctions à valeurs dans \( E \) et continues par morceaux sur \( \left\lbrack  {a, b}\right\rbrack \) est un espace vectoriel. Si \( E \) est une algèbre, \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) est une algèbre.

> - The set \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) of functions with values in \( E \) and piecewise continuous on \( \left\lbrack  {a, b}\right\rbrack \) is a vector space. If \( E \) is an algebra, \( {\mathcal{C}}_{m}\left( {\left\lbrack  {a, b}\right\rbrack  , E}\right) \) is an algebra.

Proposition 5. Toute fonction continue par morceaux sur \( \left\lbrack {a, b}\right\rbrack \) est réglée.

> Proposition 5. Every piecewise continuous function on \( \left\lbrack {a, b}\right\rbrack \) is regulated.

Démonstration. On montre d’abord le résultat pour une fonction continue \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) . Comme \( \left\lbrack {a, b}\right\rbrack \) est compact, \( f \) est uniformément continue sur \( \left\lbrack {a, b}\right\rbrack \) d’après le théorème de Heine. Ainsi, si on se donne \( \varepsilon > 0 \) ,

> Proof. We first show the result for a continuous function \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) . Since \( \left\lbrack {a, b}\right\rbrack \) is compact, \( f \) is uniformly continuous on \( \left\lbrack {a, b}\right\rbrack \) according to the Heine-Cantor theorem. Thus, if we are given \( \varepsilon > 0 \) ,

\[
\exists \alpha  > 0,\forall x, y \in  \left\lbrack  {a, b}\right\rbrack  ,\left| {x - y}\right|  < \alpha ,\;\parallel f\left( x\right)  - f\left( y\right) \parallel  < \varepsilon .
\]

(*)

> Considérons une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que \( {x}_{i} - {x}_{i - 1} < \alpha \) pour tout \( i \in \{ 1,\ldots , n\} \) et construisons une application \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) de la manière suivante :

Consider a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that \( {x}_{i} - {x}_{i - 1} < \alpha \) for all \( i \in \{ 1,\ldots , n\} \) and construct a mapping \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow E \) as follows:

\[
\forall i,\;\varphi \left( {x}_{i}\right)  = f\left( {x}_{i}\right) \;\text{ et }\;\forall i,\forall x \in  \rbrack {x}_{i - 1},{x}_{i}\lbrack ,\;\varphi \left( x\right)  = f\left( \frac{{x}_{i - 1} + {x}_{i}}{2}\right) .
\]

Cette fonction est en escalier et elle vérifie \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) d’après (*). La fonction \( f \) est donc réglée.

> This function is a step function and it satisfies \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) for all \( x \in \left\lbrack {a, b}\right\rbrack \) according to (*). The function \( f \) is therefore regulated.

Considérons maintenant le cas d'une fonction continue par morceaux pour une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) . Soit \( \varepsilon > 0 \) . La restriction \( {f}_{i} \) de \( f \) sur \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) se prolonge en une fonction continue \( {f}_{i} \) sur \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) , donc on peut trouver une fonction en escalier \( {\varphi }_{i} \) vérifiant \( \begin{Vmatrix}{{f}_{i} - {\varphi }_{i}}\end{Vmatrix} < \varepsilon \) sur \( \rbrack {x}_{i - 1},{x}_{i}\left\lbrack {\text{ . La fonction }\varphi \text{ construite sur }\left\lbrack {a, b}\right\rbrack \text{ par }\varphi \left( x\right) = {\varphi }_{i}\left( x\right) \text{ pour }x \in }\right\rbrack {x}_{i - 1},{x}_{i}\lbrack \) et \( \varphi \left( {x}_{i}\right) = f\left( {x}_{i}\right) \) est en escalier et par construction, \( \parallel f - \varphi \parallel < \varepsilon \) sur \( \left\lbrack {a, b}\right\rbrack \) tout entier. Ainsi \( f \) est une fonction réglée.

> Now consider the case of a piecewise continuous function for a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \). Let \( \varepsilon > 0 \). The restriction \( {f}_{i} \) of \( f \) to \( \rbrack {x}_{i - 1},{x}_{i}\lbrack \) extends to a continuous function \( {f}_{i} \) on \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \), so we can find a step function \( {\varphi }_{i} \) satisfying \( \begin{Vmatrix}{{f}_{i} - {\varphi }_{i}}\end{Vmatrix} < \varepsilon \) on \( \rbrack {x}_{i - 1},{x}_{i}\left\lbrack {\text{ . La fonction }\varphi \text{ construite sur }\left\lbrack {a, b}\right\rbrack \text{ par }\varphi \left( x\right) = {\varphi }_{i}\left( x\right) \text{ pour }x \in }\right\rbrack {x}_{i - 1},{x}_{i}\lbrack \) and \( \varphi \left( {x}_{i}\right) = f\left( {x}_{i}\right) \) is a step function and by construction, \( \parallel f - \varphi \parallel < \varepsilon \) on the whole of \( \left\lbrack {a, b}\right\rbrack \). Thus \( f \) is a regulated function.

DéFINITION 5. Soient \( I \) un intervalle de \( \mathbb{R} \) et une application \( f : I \rightarrow E \) . On dit que \( f \) présente une discontinuité de première espèce en un point \( {x}_{0} \in I \) si \( f \) n’est pas continue en \( {x}_{0} \) et si \( f\left( {{x}_{0} - }\right) \) (limite à gauche de \( f \) en \( {x}_{0} \) ) et \( f\left( {{x}_{0} + }\right) \) (limite à droite de \( f \) en \( {x}_{0} \) ) existent. La définition s’étend aux bornes de \( I \) lorsque \( I \) y est fermé en ne considérant que l’existence de \( f\left( {{x}_{0} + }\right) \) ou \( f\left( {{x}_{0} - }\right) \) selon le cas.

> DEFINITION 5. Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow E \) a mapping. We say that \( f \) has a discontinuity of the first kind at a point \( {x}_{0} \in I \) if \( f \) is not continuous at \( {x}_{0} \) and if \( f\left( {{x}_{0} - }\right) \) (left limit of \( f \) at \( {x}_{0} \)) and \( f\left( {{x}_{0} + }\right) \) (right limit of \( f \) at \( {x}_{0} \)) exist. The definition extends to the endpoints of \( I \) when \( I \) is closed there by considering only the existence of \( f\left( {{x}_{0} + }\right) \) or \( f\left( {{x}_{0} - }\right) \) as appropriate.

Remarque 4. Il est équivalent de dire que \( f\left( {{x}_{0} + }\right) \) et \( f\left( {{x}_{0} - }\right) \) existent et que les valeurs \( f\left( {{x}_{0} - }\right) , f\left( {{x}_{0} + }\right) , f\left( {x}_{0}\right) \) ne sont pas toutes identiques.

> Remark 4. It is equivalent to say that \( f\left( {{x}_{0} + }\right) \) and \( f\left( {{x}_{0} - }\right) \) exist and that the values \( f\left( {{x}_{0} - }\right) , f\left( {{x}_{0} + }\right) , f\left( {x}_{0}\right) \) are not all identical.

THÉORENE 4. Une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) est réglée si et seulement si tout point de discontinuité de \( f \) est de première espèce. L’ensemble des points de discontinuité de \( f \) est alors au plus dénombrable.

> THEOREM 4. A mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) is regulated if and only if every point of discontinuity of \( f \) is of the first kind. The set of points of discontinuity of \( f \) is then at most countable.

Démonstration. Condition nécessaire. Soit \( {x}_{0} < b \) un point de discontinuité de \( f \) . Soit \( \varepsilon > 0 \) et soit \( \varphi \) une fonction en escalier telle que \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) pour tout \( x \in \left\lbrack {a, b}\right\rbrack \) . Il existe \( \alpha > 0 \) tel que \( \varphi \) soit constante sur \( \rbrack {x}_{0},{x}_{0} + \alpha \lbrack \) , ce qui entraîne

> Proof. Necessary condition. Let \( {x}_{0} < b \) be a point of discontinuity of \( f \). Let \( \varepsilon > 0 \) and let \( \varphi \) be a step function such that \( \parallel f\left( x\right) - \varphi \left( x\right) \parallel < \varepsilon \) for all \( x \in \left\lbrack {a, b}\right\rbrack \). There exists \( \alpha > 0 \) such that \( \varphi \) is constant on \( \rbrack {x}_{0},{x}_{0} + \alpha \lbrack \), which implies

\[
\forall x, y \in  \rbrack {x}_{0},{x}_{0} + \alpha \lbrack ,\;\parallel f\left( x\right)  - f\left( y\right) \parallel  \leq  \parallel f\left( x\right)  - \varphi \left( x\right) \parallel  + \parallel \varphi \left( x\right)  - \varphi \left( y\right) \parallel  + \parallel \varphi \left( y\right)  - f\left( y\right) \parallel  < {2\varepsilon }.
\]

L’espace vectoriel \( E \) étant complet, on en déduit d’après le critère de Cauchy pour les fonctions que \( f\left( {{x}_{0} + }\right) = \mathop{\lim }\limits_{\substack{{x \rightarrow {x}_{0}} \\ {x > {x}_{0}} }}f\left( x\right) \) existe. On montrerait de même que \( f\left( {{x}_{0} - }\right) \) existe pour \( {x}_{0} > a \) .

> Since the vector space \( E \) is complete, we deduce from the Cauchy criterion for functions that \( f\left( {{x}_{0} + }\right) = \mathop{\lim }\limits_{\substack{{x \rightarrow {x}_{0}} \\ {x > {x}_{0}} }}f\left( x\right) \) exists. We would show similarly that \( f\left( {{x}_{0} - }\right) \) exists for \( {x}_{0} > a \).

Condition suffisante. Soit \( \varepsilon > 0 \) . Pour \( x \in \rbrack a, b\left\lbrack \right. \) on pose \( \omega \left( {f, x}\right) = \max (\parallel f\left( {x - }\right) - f\left( x\right) \parallel ,\parallel f\left( x\right) - \; f\left( {x + }\right) \parallel ) \) . D’après le résultat de la question a) de l’exercice 7 page 36, l’ensemble \( {A}_{\varepsilon } = \{ x \in \; \rbrack a, b\left\lbrack {,\omega \left( {f, x}\right) \geq \varepsilon }\right\rbrack \) est fini. Il existe donc une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que \( \omega \left( {f, x}\right) < \varepsilon \) sur chaque \( \rbrack {x}_{i},{x}_{i + 1}\lbrack \) , et d’après le résultat de la question d) du même exercice, on peut donc trouver pour tout \( i \) un \( {\alpha }_{i} > 0 \) tel que

> Sufficient condition. Let \( \varepsilon > 0 \). For \( x \in \rbrack a, b\left\lbrack \right. \) we set \( \omega \left( {f, x}\right) = \max (\parallel f\left( {x - }\right) - f\left( x\right) \parallel ,\parallel f\left( x\right) - \; f\left( {x + }\right) \parallel ) \). According to the result of question a) of exercise 7 on page 36, the set \( {A}_{\varepsilon } = \{ x \in \; \rbrack a, b\left\lbrack {,\omega \left( {f, x}\right) \geq \varepsilon }\right\rbrack \) is finite. There therefore exists a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that \( \omega \left( {f, x}\right) < \varepsilon \) on each \( \rbrack {x}_{i},{x}_{i + 1}\lbrack \), and according to the result of question d) of the same exercise, we can therefore find for all \( i \) a \( {\alpha }_{i} > 0 \) such that

\[
\forall x, y \in  \rbrack {x}_{i},{x}_{i + 1}\lbrack ,\left| {x - y}\right|  < {\alpha }_{i},\;\parallel f\left( x\right)  - f\left( y\right) \parallel  < {2\varepsilon }.
\]

(*)

> Pour tout \( i \) , considérons une subdivision \( {x}_{i} = {y}_{i,0} < {y}_{i,1} < \cdots < {y}_{i,{n}_{i}} = {x}_{i + 1} \) de \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) telle que \( {y}_{i, j + 1} - {y}_{i, j} < {\alpha }_{i} \) pour tout \( j \) . On construit la fonction en escalier \( {\varphi }_{i} \) sur \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) en posant

For all \( i \), consider a subdivision \( {x}_{i} = {y}_{i,0} < {y}_{i,1} < \cdots < {y}_{i,{n}_{i}} = {x}_{i + 1} \) of \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) such that \( {y}_{i, j + 1} - {y}_{i, j} < {\alpha }_{i} \) for all \( j \). We construct the step function \( {\varphi }_{i} \) on \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) by setting

\[
\forall j,\;{\varphi }_{i}\left( {y}_{i, j}\right)  = f\left( {y}_{i, j}\right) ,\;\forall j,\forall x \in  \rbrack {y}_{i, j},{y}_{i, j + 1}\left\lbrack  {,\;{\varphi }_{i}\left( x\right)  = f\left( \frac{{y}_{i, j} + {y}_{i, j + 1}}{2}\right) .}\right.
\]

D’après (*), on a \( \begin{Vmatrix}{f - {\varphi }_{i}}\end{Vmatrix} < {2\varepsilon } \) sur \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) . La fonction \( \varphi \) construite sur \( \left\lbrack {a, b}\right\rbrack \) par \( \varphi \left( x\right) = {\varphi }_{i}\left( x\right) \) pour \( x \in \rbrack {x}_{i - 1},{x}_{i}\left\lbrack \right. \) et \( \varphi \left( {x}_{i}\right) = f\left( {x}_{i}\right) \) est en escalier et vérifie \( \parallel f - \varphi \parallel < {2\varepsilon } \) sur \( \left\lbrack {a, b}\right\rbrack \) tout entier. Ainsi \( f \) est une fonction réglée.

> According to (*), we have \( \begin{Vmatrix}{f - {\varphi }_{i}}\end{Vmatrix} < {2\varepsilon } \) on \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \). The function \( \varphi \) constructed on \( \left\lbrack {a, b}\right\rbrack \) by \( \varphi \left( x\right) = {\varphi }_{i}\left( x\right) \) for \( x \in \rbrack {x}_{i - 1},{x}_{i}\left\lbrack \right. \) and \( \varphi \left( {x}_{i}\right) = f\left( {x}_{i}\right) \) is a step function and satisfies \( \parallel f - \varphi \parallel < {2\varepsilon } \) on the entirety of \( \left\lbrack {a, b}\right\rbrack \). Thus, \( f \) is a regulated function.

Ensemble des points de discontinuité de \( f \) . L’ensemble des points de discontinuité de \( f \) est au plus dénombrable d'après le résultat de la question b) de l'exercice 7 page 36. Conséquence : Une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) monotone est réglée. En effet, supposons par exemple \( f \) croissante. Si \( \left. {\left. {{x}_{0} \in }\right\rbrack a, b}\right\rbrack \) , alors \( f\left( x\right) \leq f\left( {x}_{0}\right) \) pour tout \( x < {x}_{0} \) , et comme \( f \) est croissante, \( f\left( {{x}_{0} - }\right) = \mathop{\lim }\limits_{\substack{{x \rightarrow {x}_{0}} \\ {x < {x}_{0}} }}f\left( x\right) \) existe. De même, \( f\left( {{x}_{0} + }\right) \) existe pour tout \( {x}_{0} \in \lbrack a, b\lbrack \) . Ainsi, tout point de discontinuité de \( f \) est forcément de première espèce, donc \( f \) est réglée.

> Set of discontinuity points of \( f \). The set of discontinuity points of \( f \) is at most countable according to the result of question b) of exercise 7 on page 36. Consequence: A monotonic mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is regulated. Indeed, suppose for example \( f \) is increasing. If \( \left. {\left. {{x}_{0} \in }\right\rbrack a, b}\right\rbrack \), then \( f\left( x\right) \leq f\left( {x}_{0}\right) \) for all \( x < {x}_{0} \), and since \( f \) is increasing, \( f\left( {{x}_{0} - }\right) = \mathop{\lim }\limits_{\substack{{x \rightarrow {x}_{0}} \\ {x < {x}_{0}} }}f\left( x\right) \) exists. Similarly, \( f\left( {{x}_{0} + }\right) \) exists for all \( {x}_{0} \in \lbrack a, b\lbrack \). Thus, every discontinuity point of \( f \) is necessarily of the first kind, so \( f \) is regulated.
