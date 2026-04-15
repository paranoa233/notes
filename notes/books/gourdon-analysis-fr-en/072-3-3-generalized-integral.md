#### 3.3. Generalized integral

*Français : 3.3. Intégrale généralisée*

DéFINITION 4. Soient \( \lbrack a, b\lbrack \) un intervalle de \( \mathbb{R}\left( {\text{ avec } - \infty < a < b \leq + \infty }\right) \) et \( f : \lbrack a, b\lbrack \rightarrow E \) une fonction continue par morceaux. Si \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{a}^{x}f\left( t\right) {dt} \) existe et est finie, on dit que l’intégrale généralisée (ou impropre) \( {\int }_{a}^{b}f\left( t\right) {dt} \) converge (ou qu’elle est convergente) et on pose \( {\int }_{a}^{b}f\left( t\right) {dt} = \ell \) . Dans le cas contraire, on dit que l’intégrale \( {\int }_{a}^{b}f\left( t\right) {dt} \) diverge (ou qu'elle est divergente).

> DEFINITION 4. Let \( \lbrack a, b\lbrack \) be an interval of \( \mathbb{R}\left( {\text{ avec } - \infty < a < b \leq + \infty }\right) \) and \( f : \lbrack a, b\lbrack \rightarrow E \) be a piecewise continuous function. If \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{a}^{x}f\left( t\right) {dt} \) exists and is finite, we say that the generalized (or improper) integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) converges (or is convergent) and we set \( {\int }_{a}^{b}f\left( t\right) {dt} = \ell \) . Otherwise, we say that the integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) diverges (or is divergent).

Remarque 2. - Si \( f \) est intégrable sur \( \lbrack a, b\lbrack \) , l’intégrale généralisée \( {\int }_{a}^{b}f\left( t\right) {dt} \) converge (on dit aussi que l'intégrale \( {\int }_{a}^{b}f\left( t\right) {dt} \) est absolument convergente), et la valeur de l'intégrale donnée par la définition précédente est identique à celle de la définition 3 page 147. La réciproque est fausse ; les intégrales généralisées qui convergent mais ne convergent pas absolument sont appelées intégrales semi-convergentes.

> Remark 2. - If \( f \) is integrable on \( \lbrack a, b\lbrack \), the generalized integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) converges (it is also said that the integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) is absolutely convergent), and the value of the integral given by the previous definition is identical to that of definition 3 on page 147. The converse is false; generalized integrals that converge but do not converge absolutely are called semi-convergent integrals.

- Si \( f \) est positive, \( f \) est intégrable si et seulement si l’intégrale \( {\int }_{a}^{b}f\left( t\right) {dt} \) converge.

> - If \( f \) is positive, \( f \) is integrable if and only if the integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) converges.

- Lorsque \( f \) est continue par morceaux sur \( \rbrack a, b\rbrack \left( {-\infty  \leq  a < b <  + \infty }\right) \) , on définirait de même \( {\int }_{a}^{b}f\left( t\right) {dt} = \mathop{\lim }\limits_{{x > a}}{\int }_{x}^{b}f\left( t\right) {dt} \) lorsque cette limite existe.

> - When \( f \) is piecewise continuous on \( \rbrack a, b\rbrack \left( {-\infty  \leq  a < b <  + \infty }\right) \), \( {\int }_{a}^{b}f\left( t\right) {dt} = \mathop{\lim }\limits_{{x > a}}{\int }_{x}^{b}f\left( t\right) {dt} \) is defined similarly when this limit exists.

- Pour tout \( c \in  \left\lbrack  {a, b\lbrack }\right. \) , les intégrales \( {\int }_{c}^{b}f\left( t\right) {dt} \) et \( {\int }_{a}^{b}f\left( t\right) {dt} \) sont de même nature.

> - For all \( c \in  \left\lbrack  {a, b\lbrack }\right. \), the integrals \( {\int }_{c}^{b}f\left( t\right) {dt} \) and \( {\int }_{a}^{b}f\left( t\right) {dt} \) are of the same nature.

- Les propriétés élémentaires vérifiées par les fonctions intégrables restent vraies pour les intégrales généralisées (linéarité, positivité, relation de Chasles, ...).

> - The elementary properties satisfied by integrable functions remain true for generalized integrals (linearity, positivity, Chasles' relation, ...).

DéFINITION 5. Soient] \( a, b\left\lbrack {\text{ un intervalle de }\mathbb{R}\left( {\text{ avec } - \infty \leq a < b \leq + \infty }\right) \text{ et }f : }\right\rbrack a, b\lbrack \rightarrow E \) une fonction continue par morceaux sur ] \( a, b \) [. Si

> DEFINITION 5. Let \( a, b\left\lbrack {\text{ un intervalle de }\mathbb{R}\left( {\text{ avec } - \infty \leq a < b \leq + \infty }\right) \text{ et }f : }\right\rbrack a, b\lbrack \rightarrow E \) be a piecewise continuous function on ] \( a, b \) [. If

\[
\ell  = \mathop{\lim }\limits_{{\left( {x, y}\right)  \rightarrow  \left( {a, b}\right) }}{\int }_{x}^{y}f\left( t\right) {dt}
\]

existe, on dit que l’intégrale \( {\int }_{a}^{b}f\left( t\right) {dt} \) converge et on note \( {\int }_{a}^{b}f\left( t\right) {dt} = \ell \) . Dans le cas contraire, on dit que \( {\int }_{a}^{b}f\left( t\right) {dt} \) diverge.

> exists, we say that the integral \( {\int }_{a}^{b}f\left( t\right) {dt} \) converges and we denote it by \( {\int }_{a}^{b}f\left( t\right) {dt} = \ell \) . Otherwise, we say that \( {\int }_{a}^{b}f\left( t\right) {dt} \) diverges.

Remarque 3. - Cette définition est cohérente avec la précédente : si \( f \) est continue par morceaux sur \( \lbrack a, b\lbrack \) (on ferme en \( a \) ) et si \( {\int }_{a}^{b}f\left( t\right) {dt} \) converge au sens de la première définition, alors cette même intégrale converge au sens de la seconde définition.

> Remark 3. - This definition is consistent with the previous one: if \( f \) is piecewise continuous on \( \lbrack a, b\lbrack \) (closed at \( a \) ) and if \( {\int }_{a}^{b}f\left( t\right) {dt} \) converges in the sense of the first definition, then this same integral converges in the sense of the second definition.

- Pour tout \( c \in  \rbrack a, b\lbrack \) on a l’équivalence

> - For all \( c \in  \rbrack a, b\lbrack \) we have the equivalence

\[
\left( {{\int }_{a}^{b}f\left( t\right) {dt}\text{ converge }}\right)  \Leftrightarrow  \left( {{\int }_{a}^{c}f\left( t\right) {dt}\text{ converge et }{\int }_{c}^{b}f\left( t\right) {dt}\text{ converge }}\right) .
\]

Cette équivalence nous permet de nous limiter à l'étude de la convergence des intégrales généralisées du type de celles introduites dans la définition 4.

> This equivalence allows us to limit ourselves to studying the convergence of generalized integrals of the type introduced in definition 4.

- En particulier, si \( f : \mathbb{R} \rightarrow  E \) est continue par morceaux, l’intégrale \( {\int }_{-\infty }^{+\infty }f\left( t\right) {dt} \) converge si et seulement si chacune des deux intégrales \( {\int }_{-\infty }^{0}f\left( t\right) {dt} \) et \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converge. Ceci n’est pas équivalent à dire que la limite \( \mathop{\lim }\limits_{{x \rightarrow   + \infty }}{\int }_{-x}^{x}f\left( t\right) {dt} \) existe (la condition est nécessaire mais pas suffisante comme le montre le contre-exemple de la fonction \( f\left( t\right)  = t \) ).

> - In particular, if \( f : \mathbb{R} \rightarrow  E \) is piecewise continuous, the integral \( {\int }_{-\infty }^{+\infty }f\left( t\right) {dt} \) converges if and only if each of the two integrals \( {\int }_{-\infty }^{0}f\left( t\right) {dt} \) and \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) converges. This is not equivalent to saying that the limit \( \mathop{\lim }\limits_{{x \rightarrow   + \infty }}{\int }_{-x}^{x}f\left( t\right) {dt} \) exists (the condition is necessary but not sufficient, as shown by the counterexample of the function \( f\left( t\right)  = t \) ).

Citons enfin le théorème qui suit, qui rend parfois quelques services.

> Finally, let us cite the following theorem, which is sometimes useful.

THÉORÉME 4. Soit a \( \in \mathbb{R} \) et \( f : \left\lbrack {a, + \infty \left\lbrack { \rightarrow E}\right. }\right. \) une fonction uniformément continue sur \( \left\lbrack {a, + \infty \left\lbrack \right. \text{ . Si l’intégrale }{\int }_{a}^{+\infty }f\left( t\right) {dt}}\right. \) converge, alors \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

> THEOREM 4. Let a \( \in \mathbb{R} \) and \( f : \left\lbrack {a, + \infty \left\lbrack { \rightarrow E}\right. }\right. \) be a uniformly continuous function on \( \left\lbrack {a, + \infty \left\lbrack \right. \text{ . Si l’intégrale }{\int }_{a}^{+\infty }f\left( t\right) {dt}}\right. \) converges, then \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

Démonstration. Soit \( \varepsilon > 0 \) . L’uniforme continuité de \( f \) entraîne

> Proof. Let \( \varepsilon > 0 \) . The uniform continuity of \( f \) implies

\[
\exists \eta  > 0,\forall x, y \geq  a,\left| {x - y}\right|  < \eta ,\;\parallel f\left( x\right)  - f\left( y\right) \parallel  < \varepsilon ,
\]

et la convergence de l’intégrale \( {\int }_{a}^{+\infty }f\left( t\right) {dt} \) entraîne

> and the convergence of the integral \( {\int }_{a}^{+\infty }f\left( t\right) {dt} \) implies

\[
\exists A > a,\forall x, y \geq  A,\;\begin{Vmatrix}{{\int }_{x}^{y}f\left( t\right) {dt}}\end{Vmatrix} \leq  {\varepsilon \eta }.
\]

Considérons maintenant \( x > A \) . On a

> Now consider \( x > A \) . We have

\[
\eta \parallel f\left( x\right) \parallel  = \begin{Vmatrix}{{\int }_{x}^{x + \eta }f\left( x\right) {dt}}\end{Vmatrix} \leq  \begin{Vmatrix}{{\int }_{x}^{x + \eta }\left( {f\left( x\right)  - f\left( t\right) }\right) {dt}}\end{Vmatrix} + \begin{Vmatrix}{{\int }_{x}^{x + \eta }f\left( t\right) {dt}}\end{Vmatrix}
\]

\[
\leq  {\int }_{x}^{x + \eta }{\varepsilon dt} + {\varepsilon \eta } = {2\varepsilon \eta }
\]

donc \( \parallel f\left( x\right) \parallel \leq {2\varepsilon } \) . Ceci étant vrai pour tout \( x > A \) , on en déduit le résultat.

> therefore \( \parallel f\left( x\right) \parallel \leq {2\varepsilon } \) . Since this is true for all \( x > A \) , we deduce the result.

Remarque 4. Le théorème est faux si \( f \) est seulement supposée continue (pour un contre-exemple, voir le troisième alinéa de la remarque 6 - on peut également construire un contre-exemple d'une fonction continue positive non bornée dont l'intégrale sur \( \mathbb{R} \) converge, en considérant une fonction nulle sauf en certains endroits où elle possède des "pics" de plus en plus grands et de plus en plus étroits lorsque \( x \rightarrow + \infty \) ).

> Remark 4. The theorem is false if \( f \) is only assumed to be continuous (for a counterexample, see the third paragraph of remark 6 - one can also construct a counterexample of a positive continuous unbounded function whose integral over \( \mathbb{R} \) converges, by considering a function that is zero except in certain places where it has "peaks" that become increasingly large and narrow as \( x \rightarrow + \infty \) ).
