#### 3.2. Properties of sequences of functions

*Français : 3.2. Propriétés des suites de fonctions*

Continuité de la fonction limite.

> Continuity of the limit function.

- THÉORÉME 2. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques et \( \left( {f}_{n}\right) \) une suite de fonctions de \( E \) dans \( F \) . Si \( \left( {f}_{n}\right) \) converge uniformément sur \( E \) vers \( f : E \rightarrow  F \) et si toutes les fonctions \( {f}_{n} \) sont continues en \( {x}_{0} \in  E \) , alors \( f \) est continue en \( {x}_{0} \) .

> - THEOREM 2. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces and \( \left( {f}_{n}\right) \) be a sequence of functions from \( E \) to \( F \) . If \( \left( {f}_{n}\right) \) converges uniformly on \( E \) to \( f : E \rightarrow  F \) and if all functions \( {f}_{n} \) are continuous at \( {x}_{0} \in  E \) , then \( f \) is continuous at \( {x}_{0} \) .

Démonstration. La démonstration est très classique, il faut savoir la refaire. Soit \( \varepsilon > 0 \) . La suite de fonctions \( \left( {f}_{n}\right) \) converge uniformément vers \( f \) , donc

> Proof. The proof is very classic; one must know how to reproduce it. Let \( \varepsilon > 0 \) . The sequence of functions \( \left( {f}_{n}\right) \) converges uniformly to \( f \) , therefore

\[
\exists n \in  \mathbb{N},\forall x \in  E,\;\delta \left( {{f}_{n}\left( x\right) , f\left( x\right) }\right)  < \varepsilon .
\]

Or \( {f}_{n} \) est continue en \( {x}_{0} \) , donc

> Now \( {f}_{n} \) is continuous at \( {x}_{0} \), therefore

\[
\exists \alpha  > 0,\forall x \in  E,\mathrm{\;d}\left( {x,{x}_{0}}\right)  < \alpha ,\;\delta \left( {{f}_{n}\left( x\right) ,{f}_{n}\left( {x}_{0}\right) }\right)  < \varepsilon .
\]

On en déduit, pour tout \( x \in X \) vérifiant \( \mathrm{d}\left( {x,{x}_{0}}\right) < \alpha \) ,

> We deduce that, for all \( x \in X \) satisfying \( \mathrm{d}\left( {x,{x}_{0}}\right) < \alpha \),

\[
\delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  \leq  \delta \left( {f\left( x\right) ,{f}_{n}\left( x\right) }\right)  + \delta \left( {{f}_{n}\left( x\right) ,{f}_{n}\left( {x}_{0}\right) }\right)  + \delta \left( {{f}_{n}\left( {x}_{0}\right) , f\left( {x}_{0}\right) }\right)  < \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon },
\]

d'où le résultat.

> whence the result.

Intégration d'une suite de fonctions. Donnons maintenant une généralisation de la proposition 3 page 125. La preuve est immédiate, elle est analogue à celle de ce dernier.

> Integration of a sequence of functions. Let us now provide a generalization of proposition 3 on page 125. The proof is immediate; it is analogous to that of the latter.

\( \rightarrow \) THÉORÉME 3. Soit \( \left( {f}_{n}\right) \) une suite de fonctions continues d’un segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) dans un espace de Banach \( E \) , qui converge uniformément vers \( f \) sur \( \left\lbrack {a, b}\right\rbrack \) . Alors \( f \) est continue et

> \( \rightarrow \) THEOREM 3. Let \( \left( {f}_{n}\right) \) be a sequence of continuous functions from a segment \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) into a Banach space \( E \), which converges uniformly to \( f \) on \( \left\lbrack {a, b}\right\rbrack \). Then \( f \) is continuous and

\[
{\int }_{a}^{b}f\left( t\right) {dt} = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{a}^{b}{f}_{n}\left( t\right) {dt}.
\]

Plus généralement, la fonction \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E\;x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) est limite uniforme de la suite de fonctions \( \left( {F}_{n}\right) \) définie par

> More generally, the function \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E\;x \mapsto {\int }_{a}^{x}f\left( t\right) {dt} \) is the uniform limit of the sequence of functions \( \left( {F}_{n}\right) \) defined by

\[
\forall n \in  \mathbb{N},\;{F}_{n} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  E\;x \mapsto  {\int }_{a}^{x}{f}_{n}\left( t\right) {dt}.
\]

Remarque. L’égalité \( \int f = \mathop{\lim }\limits_{{n \rightarrow \infty }}\int {f}_{n} \) est également vérifiée sous des hypothèses beaucoup moins contraignantes dans le cadre du théorème de convergence dominée (voir le théorème 3 page 151). - Le résultat se généralise si on suppose seulement les \( {f}_{n} \) Riemann-intégrables. Dans ce cas, la limite uniforme \( f \) est également Riemann-intégrable.

> Remark. The equality \( \int f = \mathop{\lim }\limits_{{n \rightarrow \infty }}\int {f}_{n} \) also holds under much less restrictive hypotheses within the framework of the dominated convergence theorem (see theorem 3 on page 151). - The result generalizes if we only assume the \( {f}_{n} \) are Riemann-integrable. In this case, the uniform limit \( f \) is also Riemann-integrable.

En combinant le théorème précédent avec le théorème 1, on en déduit facilement :

> By combining the previous theorem with theorem 1, we easily deduce:

COROLLAIRE 1 (Interversion des signes de sommation). Si \( \sum {g}_{n} \) est une série de fonctions continues d’un segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) dans un espace de Banach \( E \) , qui converge normalement sur \( \left\lbrack {a, b}\right\rbrack \) , alors

> COROLLARY 1 (Interchange of summation signs). If \( \sum {g}_{n} \) is a series of continuous functions from a segment \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) into a Banach space \( E \), which converges normally on \( \left\lbrack {a, b}\right\rbrack \), then

\[
{\int }_{a}^{b}\left( {\mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}\left( t\right) }\right) {dt} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {{\int }_{a}^{b}{g}_{n}\left( t\right) {dt}}\right) .
\]

##### Differentiability and derivative of the limit function.

*Français : Dérivabilité et dérivée de la fonction limite.*

\( \rightarrow \) THÉORÉME 4. Soit \( \left( {f}_{n}\right) \) une suite de fonctions de classe \( {\mathcal{C}}^{1} \) d’un segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) dans un espace de Banach E. On suppose que

> \( \rightarrow \) THEOREM 4. Let \( \left( {f}_{n}\right) \) be a sequence of functions of class \( {\mathcal{C}}^{1} \) from a segment \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) into a Banach space E. Suppose that

(i) il existe \( {x}_{0} \in \left\lbrack {a, b}\right\rbrack \) tel que la suite \( \left( {{f}_{n}\left( {x}_{0}\right) }\right) \) converge ;

> (i) there exists \( {x}_{0} \in \left\lbrack {a, b}\right\rbrack \) such that the sequence \( \left( {{f}_{n}\left( {x}_{0}\right) }\right) \) converges;

(ii) la suite de fonctions \( \left( {f}_{n}^{\prime }\right) \) converge uniformément sur \( \left\lbrack {a, b}\right\rbrack \) vers une fonction \( g \) .

> (ii) the sequence of functions \( \left( {f}_{n}^{\prime }\right) \) converges uniformly on \( \left\lbrack {a, b}\right\rbrack \) to a function \( g \).

Alors \( \left( {f}_{n}\right) \) converge uniformément sur \( \left\lbrack {a, b}\right\rbrack \) vers une fonction \( f \) de classe \( {\mathcal{C}}^{1} \) et vérifiant \( {f}^{\prime } = g. \)

> Then \( \left( {f}_{n}\right) \) converges uniformly on \( \left\lbrack {a, b}\right\rbrack \) to a function \( f \) of class \( {\mathcal{C}}^{1} \) and satisfying \( {f}^{\prime } = g. \)

Démonstration. On applique le théorème 3 à la suite de fonctions \( \left( {f}_{n}^{\prime }\right) \) , et on en conclut que \( \left( {{f}_{n} - {f}_{n}\left( a\right) }\right) \) converge uniformément vers \( h : x \mapsto {\int }_{a}^{x}g\left( t\right) {dt} \) sur \( \left\lbrack {a, b}\right\rbrack \) . En particulier, la suite \( {\left( {f}_{n}\left( {x}_{0}\right) - {f}_{n}\left( a\right) \right) }_{n \in \mathbb{N}} \) converge, donc d’après (i), \( \left( {{f}_{n}\left( a\right) }\right) \) converge, et nous notons \( \ell \) la limite correspondante. On voit facilement que \( \left( {f}_{n}\right) \) converge uniformément vers \( f : x \mapsto h\left( x\right) + \ell \) . Cette fonction \( f \) vérifie bien les propriétés voulues (en particulier, elle est \( {\mathcal{C}}^{1} \) car \( g \) est continue comme limite uniforme de fonctions continues).

> Proof. We apply Theorem 3 to the sequence of functions \( \left( {f}_{n}^{\prime }\right) \), and conclude that \( \left( {{f}_{n} - {f}_{n}\left( a\right) }\right) \) converges uniformly to \( h : x \mapsto {\int }_{a}^{x}g\left( t\right) {dt} \) on \( \left\lbrack {a, b}\right\rbrack \). In particular, the sequence \( {\left( {f}_{n}\left( {x}_{0}\right) - {f}_{n}\left( a\right) \right) }_{n \in \mathbb{N}} \) converges, so according to (i), \( \left( {{f}_{n}\left( a\right) }\right) \) converges, and we denote the corresponding limit by \( \ell \). It is easy to see that \( \left( {f}_{n}\right) \) converges uniformly to \( f : x \mapsto h\left( x\right) + \ell \). This function \( f \) satisfies the desired properties (in particular, it is \( {\mathcal{C}}^{1} \) because \( g \) is continuous as a uniform limit of continuous functions).

Remarque 5. - Il n’est pas difficile d’en déduire que si \( \left( {f}_{n}\right) \) est une suite de fonctions \( {\mathcal{C}}^{1} \) de \( I \) dans \( E \) (où \( I \) est un intervalle quelconque de \( \mathbb{R} \) ) qui vérifie les hypothèses précédentes sur tout segment de \( I \) , alors les mêmes conclusions subsistent (sauf la convergence uniforme de \( \left( {f}_{n}\right) \) sur \( I \) tout entier).

> Remark 5. - It is not difficult to deduce that if \( \left( {f}_{n}\right) \) is a sequence of \( {\mathcal{C}}^{1} \) functions from \( I \) to \( E \) (where \( I \) is any interval of \( \mathbb{R} \)) that satisfies the previous hypotheses on every compact subinterval of \( I \), then the same conclusions hold (except for the uniform convergence of \( \left( {f}_{n}\right) \) on the entirety of \( I \)).

- Pour une série de fonctions \( \sum {g}_{n} \) , les \( {g}_{n} \) étant de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack  {a, b}\right\rbrack \) , ce théorème s’énonce comme suit : s’il existe \( {x}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) tel que \( \sum {g}_{n}\left( {x}_{0}\right) \) converge et si la série de fonctions \( \sum {g}_{n}^{\prime } \) converge normalement sur \( \left\lbrack  {a, b}\right\rbrack \) , alors \( \sum {g}_{n} \) converge normalement sur \( \left\lbrack  {a, b}\right\rbrack \) vers une fonction \( {\mathcal{C}}^{1} \) sur \( \left\lbrack  {a, b}\right\rbrack \) et on a \( {\left( \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}\right) }^{\prime } = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}^{\prime } \) .

> - For a series of functions \( \sum {g}_{n} \), where the \( {g}_{n} \) are of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack  {a, b}\right\rbrack \), this theorem is stated as follows: if there exists \( {x}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) such that \( \sum {g}_{n}\left( {x}_{0}\right) \) converges and if the series of functions \( \sum {g}_{n}^{\prime } \) converges normally on \( \left\lbrack  {a, b}\right\rbrack \), then \( \sum {g}_{n} \) converges normally on \( \left\lbrack  {a, b}\right\rbrack \) to a function \( {\mathcal{C}}^{1} \) on \( \left\lbrack  {a, b}\right\rbrack \) and we have \( {\left( \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}\right) }^{\prime } = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}^{\prime } \).

- Le théorème 4 reste vrai lorsque les fonctions \( \left( {f}_{n}\right) \) sont seulement supposées déri-vables (voir l'exercice 9 page 244).

> - Theorem 4 remains true when the functions \( \left( {f}_{n}\right) \) are only assumed to be differentiable (see exercise 9 on page 244).

En utilisant une récurrence fondée sur le théorème précédent, on en déduit le corollaire suivant qui permet de montrer qu’une fonction limite est de classe \( {\mathcal{C}}^{p} \) .

> Using an induction based on the previous theorem, we deduce the following corollary, which allows us to show that a limit function is of class \( {\mathcal{C}}^{p} \).

COROLLAIRE 2. Soit \( p \in {\mathbb{N}}^{ * } \) et \( \left( {f}_{n}\right) \) une suite de fonctions de classe \( {\mathcal{C}}^{p} \) d’un segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) dans un espace de Banach E. On suppose que pour tout \( k \in \{ 0,1,\ldots , p\} \) , la suite de fonctions \( {\left( {f}_{n}^{\left( k\right) }\right) }_{n} \) converge uniformément vers une fonction \( {g}_{k} \) sur \( \left\lbrack {a, b}\right\rbrack \) . Alors la limite uniforme \( f = {g}_{0}{de}\left( {f}_{n}\right) \) est de classe \( {\mathcal{C}}^{p} \) et vérifie \( {f}^{\left( k\right) } = {g}_{k} \) pour tout \( k \in \{ 0,1,\ldots , p\} \) .

> COROLLARY 2. Let \( p \in {\mathbb{N}}^{ * } \) and \( \left( {f}_{n}\right) \) be a sequence of \( {\mathcal{C}}^{p} \) functions from a segment \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) into a Banach space E. Suppose that for all \( k \in \{ 0,1,\ldots , p\} \), the sequence of functions \( {\left( {f}_{n}^{\left( k\right) }\right) }_{n} \) converges uniformly to a function \( {g}_{k} \) on \( \left\lbrack {a, b}\right\rbrack \). Then the uniform limit \( f = {g}_{0}{de}\left( {f}_{n}\right) \) is of class \( {\mathcal{C}}^{p} \) and satisfies \( {f}^{\left( k\right) } = {g}_{k} \) for all \( k \in \{ 0,1,\ldots , p\} \).

Remarque 6. Le corollaire précédent s'étend aisément aux séries de fonctions : si les \( {g}_{n} \) sont \( {\mathcal{C}}^{p} \) et si \( \sum {g}_{n}^{\left( k\right) } \) converge normalement sur \( \left\lbrack {a, b}\right\rbrack \) pour \( 0 \leq k \leq p \) , alors \( g = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n} \) est de classe \( {\mathcal{C}}^{p} \) et \( {g}^{\left( k\right) } = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}^{\left( k\right) } \) pour \( 0 \leq k \leq p \) .

> Remark 6. The previous corollary extends easily to series of functions: if the \( {g}_{n} \) are \( {\mathcal{C}}^{p} \) and if \( \sum {g}_{n}^{\left( k\right) } \) converges normally on \( \left\lbrack {a, b}\right\rbrack \) for \( 0 \leq k \leq p \), then \( g = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n} \) is of class \( {\mathcal{C}}^{p} \) and \( {g}^{\left( k\right) } = \mathop{\sum }\limits_{{n = 0}}^{\infty }{g}_{n}^{\left( k\right) } \) for \( 0 \leq k \leq p \).

Exemple 3. Considérons une algèbre normée complète \( E \) , un élément \( u \in E \) , et la fonction

> Example 3. Consider a complete normed algebra \( E \), an element \( u \in E \), and the function

\[
{e}_{u} : \mathbb{R} \rightarrow  E\;t \mapsto  \exp \left( {tu}\right)  = \mathop{\sum }\limits_{{n = 0}}^{\infty }\frac{{t}^{n}}{n!}{u}^{n}.
\]

Chaque terme de la série est de classe \( {\mathcal{C}}^{\infty } \) et la série des dérivées \( p \) -ièmes est

> Each term of the series is of class \( {\mathcal{C}}^{\infty } \) and the series of \( p \)-th derivatives is

\[
\mathop{\sum }\limits_{{n \geq  p}}\frac{{t}^{n - p}}{\left( {n - p}\right) !}{u}^{n}
\]

Cette série converge normalement sur tout segment \( S = \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) (car \( \begin{Vmatrix}{{t}^{n - p}{u}^{n}/\left( {n - p}\right) !}\end{Vmatrix} \leq \; \parallel u{\parallel }^{p}{\left( M\parallel u\parallel \right) }^{n - p}/\left( {n - p}\right) \) ! où \( M = \max \{ \left| a\right| ,\left| b\right| \} \) ). On en déduit que \( {e}_{u} \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( S \) et que sa dérivée \( p \) -ième est \( {e}_{u}^{\left( p\right) } = {u}^{p}{e}_{u} \) . Ceci étant vrai pour tout segment \( S \) de \( \mathbb{R} \) , c'est vrai également sur \( \mathbb{R} \) tout entier.

> This series converges normally on any segment \( S = \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) (since \( \begin{Vmatrix}{{t}^{n - p}{u}^{n}/\left( {n - p}\right) !}\end{Vmatrix} \leq \; \parallel u{\parallel }^{p}{\left( M\parallel u\parallel \right) }^{n - p}/\left( {n - p}\right) \) ! where \( M = \max \{ \left| a\right| ,\left| b\right| \} \) ). We deduce that \( {e}_{u} \) is of class \( {\mathcal{C}}^{\infty } \) on \( S \) and that its \( p \)-th derivative is \( {e}_{u}^{\left( p\right) } = {u}^{p}{e}_{u} \) . Since this is true for any segment \( S \) of \( \mathbb{R} \), it is also true on the entirety of \( \mathbb{R} \).
