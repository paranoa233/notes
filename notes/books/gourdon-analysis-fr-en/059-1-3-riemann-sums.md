#### 1.3. Riemann sums

*Français : 1.3. Sommes de Riemann*

##### Riemann sums.

*Français : Sommes de Riemann.*

Notation. Soient \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application bornée, \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) une subdivision de \( \left\lbrack {a, b}\right\rbrack \) et \( \xi = {\left( {\xi }_{i}\right) }_{1 \leq i \leq n} \) une famille de \( n \) réels telle que \( {\xi }_{i} \in \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) pour tout \( i \in \{ 1,\ldots , n\} \) . Le couple \( \left( {\sigma ,\xi }\right) \) s’appelle une subdivision pointée.

> Notation. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a bounded mapping, \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) a subdivision of \( \left\lbrack {a, b}\right\rbrack \), and \( \xi = {\left( {\xi }_{i}\right) }_{1 \leq i \leq n} \) a family of \( n \) real numbers such that \( {\xi }_{i} \in \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) for all \( i \in \{ 1,\ldots , n\} \). The pair \( \left( {\sigma ,\xi }\right) \) is called a tagged subdivision.

On appelle somme de Riemann de la fonction \( f \) pour la subdivision pointée \( \left( {\sigma ,\xi }\right) \) la grandeur notée \( S\left( {f,\sigma ,\xi }\right) \) définie par

> The Riemann sum of the function \( f \) for the tagged subdivision \( \left( {\sigma ,\xi }\right) \) is the quantity denoted by \( S\left( {f,\sigma ,\xi }\right) \) defined by

\[
S\left( {f,\sigma ,\xi }\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{x}_{i} - {x}_{i - 1}}\right) f\left( {\xi }_{i}\right) .
\]

On rappelle que le pas de \( \sigma \) est le réel \( \mathop{\sup }\limits_{{1 \leq i \leq n}}\left( {{x}_{i} - {x}_{i - 1}}\right) \) , noté \( \left| \sigma \right| \) .

> Recall that the mesh of \( \sigma \) is the real number \( \mathop{\sup }\limits_{{1 \leq i \leq n}}\left( {{x}_{i} - {x}_{i - 1}}\right) \), denoted by \( \left| \sigma \right| \).

\( \rightarrow \) THÉORÉME 7. Soit une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) continue par morceaux. Pour tout \( \varepsilon > 0 \) , il existe \( \alpha > 0 \) tel que pour toute subdivision pointée \( \left( {\sigma ,\xi }\right) \) de \( \left\lbrack {a, b}\right\rbrack \) vérifiant \( \left| \sigma \right| < \alpha \) , on ait

> \( \rightarrow \) THEOREM 7. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a piecewise continuous mapping. For any \( \varepsilon > 0 \), there exists \( \alpha > 0 \) such that for any tagged subdivision \( \left( {\sigma ,\xi }\right) \) of \( \left\lbrack {a, b}\right\rbrack \) satisfying \( \left| \sigma \right| < \alpha \), we have

\[
\begin{Vmatrix}{{\int }_{a}^{b}f\left( x\right) {dx} - S\left( {f,\sigma ,\xi }\right) }\end{Vmatrix} \leq  \varepsilon .
\]

Démonstration. Nous allons prouver le résultat en trois étapes.

> Proof. We will prove the result in three steps.

Étape 1. Supposons que \( f \) soit de la forme \( f = {\chi }_{\left\lbrack c, d\right\rbrack } \cdot e \) , où \( {\chi }_{\left\lbrack c, d\right\rbrack } \) est la fonction caractéristique d’un segment \( \left\lbrack {c, d}\right\rbrack \) inclus dans \( \left\lbrack {a, b}\right\rbrack \) et \( e \in E \) . Soit \( \left( {\sigma ,\xi }\right) \) une subdivision pointée de \( \left\lbrack {a, b}\right\rbrack \) . Écrivons

> Step 1. Suppose \( f \) is of the form \( f = {\chi }_{\left\lbrack c, d\right\rbrack } \cdot e \), where \( {\chi }_{\left\lbrack c, d\right\rbrack } \) is the characteristic function of a segment \( \left\lbrack {c, d}\right\rbrack \) included in \( \left\lbrack {a, b}\right\rbrack \) and \( e \in E \). Let \( \left( {\sigma ,\xi }\right) \) be a tagged subdivision of \( \left\lbrack {a, b}\right\rbrack \). Let us write

\[
\sigma  : a = {x}_{0} < {x}_{1} < \cdots  < {x}_{n} = b,\;\xi  = {\left( {\xi }_{i}\right) }_{1 \leq  i \leq  n}.
\]

On remarque que

> We note that

\[
S\left( {f,\sigma ,\xi }\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\int }_{{x}_{i - 1}}^{{x}_{i}}f\left( {\xi }_{i}\right) {dx}\;\text{ donc }\;\begin{Vmatrix}{S\left( {f,\sigma ,\xi }\right)  - {\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{i = 1}}^{n}\begin{Vmatrix}{{\int }_{{x}_{i - 1}}^{{x}_{i}}\left( {f\left( {\xi }_{i}\right)  - f\left( x\right) }\right) {dx}}\end{Vmatrix}.
\]

Parmi les intervalles \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \left( {1 \leq i \leq n}\right) \) , il y en a au plus deux sur lesquels \( f \) ne soit pas constante. On en conclut facilement

> Among the intervals \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \left( {1 \leq i \leq n}\right) \), there are at most two on which \( f \) is not constant. We easily conclude

\[
\begin{Vmatrix}{S\left( {f,\sigma ,\xi }\right)  - {\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix} \leq  2\left| \sigma \right|  \cdot  \parallel e\parallel ,
\]

d'où le résultat.

> whence the result.

Étape 2. Supposons que \( f \) soit une fonction en escalier. On peut écrire \( f \) comme une somme finie de fonctions du type de celles traitées dans l'étape 1, et le résultat s'obtient ensuite facilement par linéarité de l’intégrale et de l’application \( f \mapsto S\left( {f,\sigma ,\xi }\right) \) .

> Step 2. Suppose \( f \) is a step function. We can write \( f \) as a finite sum of functions of the type treated in step 1, and the result is then easily obtained by the linearity of the integral and the mapping \( f \mapsto S\left( {f,\sigma ,\xi }\right) \).

Étape 3. Traitons maintenant le cas général. Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une fonction continue par morceaux. Soient \( \varepsilon > 0 \) et une fonction en escalier \( \varphi \) telle que \( \parallel f - \varphi \parallel \leq \varepsilon \) sur \( \left\lbrack {a, b}\right\rbrack \) . L’étape précédente nous assure l’existence d’un réel \( \alpha > 0 \) tel que pour toute subdivision pointée \( \left( {\sigma ,\xi }\right) \) vérifiant \( \left| \sigma \right| < \alpha \) , on ait

> Step 3. Let us now treat the general case. Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a piecewise continuous function. Let \( \varepsilon > 0 \) and a step function \( \varphi \) be such that \( \parallel f - \varphi \parallel \leq \varepsilon \) on \( \left\lbrack {a, b}\right\rbrack \) . The previous step ensures the existence of a real number \( \alpha > 0 \) such that for any tagged subdivision \( \left( {\sigma ,\xi }\right) \) satisfying \( \left| \sigma \right| < \alpha \) , we have

\[
\begin{Vmatrix}{S\left( {\varphi ,\sigma ,\xi }\right)  - {\int }_{a}^{b}\varphi \left( x\right) {dx}}\end{Vmatrix} < \varepsilon ,
\]

Ainsi, pour une telle subdivision pointée \( \left( {\sigma ,\xi }\right) \) , on a

> Thus, for such a tagged subdivision \( \left( {\sigma ,\xi }\right) \) , we have

\[
\begin{Vmatrix}{S\left( {f,\sigma ,\xi }\right)  - {\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix}
\]

\[
\leq  \parallel S\left( {f,\sigma ,\xi }\right)  - S\left( {\varphi ,\sigma ,\xi }\right) \parallel  + \begin{Vmatrix}{S\left( {\varphi ,\sigma ,\xi }\right)  - {\int }_{a}^{b}\varphi \left( x\right) {dx}}\end{Vmatrix} + \begin{Vmatrix}{{\int }_{a}^{b}\varphi \left( x\right) {dx} - {\int }_{a}^{b}f\left( x\right) {dx}}\end{Vmatrix}
\]

\[
\leq  S\left( {\parallel f - \varphi \parallel ,\sigma ,\xi }\right)  + \varepsilon  + {\int }_{a}^{b}\parallel \varphi \left( x\right)  - f\left( x\right) \parallel {dx}
\]

\[
\leq  \left( {b - a}\right) \varepsilon  + \varepsilon  + \left( {b - a}\right) \varepsilon  = \left( {1 + 2\left( {b - a}\right) }\right) \varepsilon .
\]

d'où le théorème.

> whence the theorem.

Conséquence : Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application continue par morceaux. Alors

> Consequence: Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a piecewise continuous mapping. Then

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{b - a}{n}\mathop{\sum }\limits_{{i = 1}}^{n}f\left( {a + i\frac{b - a}{n}}\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{b - a}{n}\mathop{\sum }\limits_{{i = 0}}^{{n - 1}}f\left( {a + i\frac{b - a}{n}}\right)  = {\int }_{a}^{b}f\left( x\right) {dx}.
\]

Exemple 1. En appliquant ce dernier résultat à \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto 1/\left( {1 + t}\right) \) , on obtient

> Example 1. By applying this last result to \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto 1/\left( {1 + t}\right) \) , we obtain

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}f\left( \frac{i}{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{n + i} = {\int }_{0}^{1}\frac{dt}{1 + t} = {\left\lbrack  \log \left( 1 + t\right) \right\rbrack  }_{0}^{1} = \log 2.
\]

Remarque 7. - Le théorème 7 est également vrai sur les fonctions Riemann-intégrables. Réciproquement, si \( E \) est un e.v.n de dimension finie, on peut même montrer qu'une fonction est Riemann-intégrable si et seulement si ses sommes de Riemann "convergent" lorsque le pas des subdivisions tend vers 0 .

> Remark 7. - Theorem 7 is also true for Riemann-integrable functions. Conversely, if \( E \) is a finite-dimensional n.v.s., one can even show that a function is Riemann-integrable if and only if its Riemann sums "converge" as the mesh of the subdivisions tends to 0.

- Sous certaines hypothèses de régularité sur \( f \) , il est possible de donner un développement asymptotique de \( \frac{b - a}{n}\mathop{\sum }\limits_{i}f\left( {a + i\frac{b - a}{n}}\right)  - {\int }_{a}^{b}f\left( x\right) {dx} \) . Ceci est un problème classique qu’il est bon de savoir résoudre (voir l'exercice 6 et le sujet d'étude 3 page 321).

> - Under certain regularity assumptions on \( f \) , it is possible to provide an asymptotic expansion of \( \frac{b - a}{n}\mathop{\sum }\limits_{i}f\left( {a + i\frac{b - a}{n}}\right)  - {\int }_{a}^{b}f\left( x\right) {dx} \) . This is a classic problem that is good to know how to solve (see exercise 6 and study topic 3 on page 321).

- Attention, le résultat de ce théorème n'est pas vrai pour les fonctions intégrables ou les intégrales généralisées, sauf sous certaines hypothèses (voir l'exercice 5 page 156 qui est classique).

> - Warning: the result of this theorem is not true for integrable functions or improper integrals, except under certain assumptions (see exercise 5 on page 156, which is a classic).
