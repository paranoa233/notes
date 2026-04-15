#### 2.2. Series with positive terms

*Français : 2.2. Séries à termes positifs*

Toute suite réelle croissante et majorée converge, et comme conséquence immédiate, on a le résultat suivant.

> Every increasing and bounded real sequence converges, and as an immediate consequence, we have the following result.

THÉORÉME 2. Une série \( \sum {u}_{n} \) à termes réels positifs converge si et seulement si la suite \( \left( {S}_{n}\right) \) des sommes partielles est majorée.

> THEOREM 2. A series \( \sum {u}_{n} \) with positive real terms converges if and only if the sequence \( \left( {S}_{n}\right) \) of partial sums is bounded.

On en déduit facilement :

> From this, we easily deduce:

THÉORÉME 3. On considère deux séries réelles \( \sum {u}_{n} \) et \( \sum {v}_{n} \) telles que

> THEOREM 3. Consider two real series \( \sum {u}_{n} \) and \( \sum {v}_{n} \) such that

\[
\forall n \in  \mathbb{N},\;0 \leq  {u}_{n} \leq  {v}_{n}.
\]

Alors si \( \sum {v}_{n} \) converge, \( \sum {u}_{n} \) converge ; si \( \sum {u}_{n} \) diverge, \( \sum {v}_{n} \) diverge.

> Then if \( \sum {v}_{n} \) converges, \( \sum {u}_{n} \) converges; if \( \sum {u}_{n} \) diverges, \( \sum {v}_{n} \) diverges.

\( \rightarrow \) THÉORÈME 4. Soient \( \sum {u}_{n} \) et \( \sum {v}_{n} \) deux séries à termes positifs.

> \( \rightarrow \) THEOREM 4. Let \( \sum {u}_{n} \) and \( \sum {v}_{n} \) be two series with positive terms.

(i) Si \( {v}_{n} = O\left( {u}_{n}\right) \) lorsque \( n \rightarrow + \infty \) et si \( \sum {u}_{n} \) converge, alors \( \sum {v}_{n} \) converge;

> (i) If \( {v}_{n} = O\left( {u}_{n}\right) \) as \( n \rightarrow + \infty \) and if \( \sum {u}_{n} \) converges, then \( \sum {v}_{n} \) converges;

(ii) si \( {u}_{n} \sim {v}_{n} \) lorsque \( n \rightarrow + \infty \) , alors les séries \( \sum {u}_{n} \) et \( \sum {v}_{n} \) sont de même nature.

> (ii) if \( {u}_{n} \sim {v}_{n} \) as \( n \rightarrow + \infty \), then the series \( \sum {u}_{n} \) and \( \sum {v}_{n} \) are of the same nature.

Remarque 2. Attention, l'assertion (ii) de ce dernier théorème n'est vraie que pour des séries à termes positifs (voir l'exercice 7 page 223 pour un contre-exemple avec des séries à termes non positifs).

> Remark 2. Caution: assertion (ii) of this last theorem is only true for series with positive terms (see exercise 7 on page 223 for a counterexample with series having non-positive terms).

\( \rightarrow \) Proposition 2 (Séries DE RIEMANN). Soit \( \alpha \) un nombre réel. La série de Riemann

> \( \rightarrow \) Proposition 2 (RIEMANN series). Let \( \alpha \) be a real number. The Riemann series

\[
\mathop{\sum }\limits_{{n \geq  1}}\frac{1}{{n}^{\alpha }}
\]

converge si et seulement si \( \alpha > 1 \) .

> converges if and only if \( \alpha > 1 \) .

Équivalents des sommes partielles et des restes. Le résultat qui suit est crucial dans beaucoup d'exercices. Il complète le théorème 4.

> Equivalents of partial sums and remainders. The following result is crucial in many exercises. It complements theorem 4.

\( \rightarrow \) THÉORÉME 5. Soient \( \sum {u}_{n} \) et \( \sum {v}_{n} \) deux séries à termes positifs, telles que \( {u}_{n} \sim {v}_{n} \) lorsque \( n \rightarrow + \infty \) . Alors

> \( \rightarrow \) THEOREM 5. Let \( \sum {u}_{n} \) and \( \sum {v}_{n} \) be two series with positive terms, such that \( {u}_{n} \sim {v}_{n} \) as \( n \rightarrow + \infty \) . Then

(i) si \( \sum {u}_{n} \) converge, \( \sum {v}_{n} \) converge et les restes vérifient

> (i) if \( \sum {u}_{n} \) converges, \( \sum {v}_{n} \) converges and the remainders satisfy

\[
\mathop{\sum }\limits_{{k = n}}^{{+\infty }}{u}_{k} \sim  \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{v}_{k},\;n \rightarrow   + \infty ;
\]

(ii) si \( \sum {u}_{n} \) diverge, \( \sum {v}_{n} \) diverge et les sommes partielles vérifient

> (ii) if \( \sum {u}_{n} \) diverges, \( \sum {v}_{n} \) diverges and the partial sums satisfy

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \sim  \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k},\;n \rightarrow   + \infty .
\]

Démonstration. On sait déjà que les séries \( \sum {u}_{n} \) et \( \sum {v}_{n} \) ont même nature (c’est l’assertion (ii) du théorème 4).

> Proof. We already know that the series \( \sum {u}_{n} \) and \( \sum {v}_{n} \) have the same nature (this is assertion (ii) of theorem 4).

(i). Soit \( \varepsilon > 0 \) . L’équivalence \( {u}_{n} \sim {v}_{n} \) entraîne

> (i). Let \( \varepsilon > 0 \) . The equivalence \( {u}_{n} \sim {v}_{n} \) implies

\[
\exists N \in  \mathbb{N},\forall k \geq  N,\;\left( {1 - \varepsilon }\right) {u}_{k} \leq  {v}_{k} \leq  \left( {1 + \varepsilon }\right) {u}_{k},
\]

donc

> therefore

\[
\forall n \geq  N,\;\left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{u}_{k} \leq  \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{v}_{k} \leq  \left( {1 + \varepsilon }\right) \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{u}_{k},
\]

d'où (i).

> whence (i).

(ii). Soit \( \varepsilon > 0 \) . Comme précédemment, on commence par écrire

> (ii). Let \( \varepsilon > 0 \) . As before, we begin by writing

\[
\exists N \in  \mathbb{N},\forall k \geq  N,\;\left( {1 - \varepsilon }\right) {u}_{k} \leq  {v}_{k} \leq  \left( {1 + \varepsilon }\right) {u}_{k}.
\]

On en déduit

> We deduce from this

\[
\forall n \geq  N,\;\mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{v}_{k} + \left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = N}}^{n}{u}_{k} \leq  \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \leq  \mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{v}_{k} + \left( {1 + \varepsilon }\right) \mathop{\sum }\limits_{{k = N}}^{n}{u}_{k}.
\]

Comme \( \sum {u}_{n} \) diverge, chacun des termes extrêmes de ces inégalités sont respectivement équiva-lents à \( \left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) et \( \left( {1 + \varepsilon }\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) On en déduit

> Since \( \sum {u}_{n} \) diverges, each of the extreme terms of these inequalities are respectively equivalent to \( \left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) and \( \left( {1 + \varepsilon }\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) We deduce from this

\[
\exists {N}^{\prime } \geq  N,\forall n \geq  {N}^{\prime },\;\left( {1 - {2\varepsilon }}\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \leq  \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \leq  \left( {1 + {2\varepsilon }}\right) \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k},
\]

d'où le résultat.

> whence the result.

Application. Ce dernier résultat permet de donner des développements asymptotiques de certaines suites ou séries. Pour illustrer ce propos, nous allons donner un développement asymptotique à l’ordre 3 des nombres harmoniques \( {H}_{n} \) définis par

> Application. This last result allows us to provide asymptotic expansions for certain sequences or series. To illustrate this, we will provide an asymptotic expansion to the 3rd order of the harmonic numbers \( {H}_{n} \) defined by

\[
\forall n \in  {\mathbb{N}}^{ * },\;{H}_{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots  + \frac{1}{n}.
\]

a) On commence par remarquer que lorsque \( n \rightarrow + \infty \) ,

> a) We begin by noting that when \( n \rightarrow + \infty \) ,

\[
\frac{1}{n} \sim  \log \left( {1 + \frac{1}{n}}\right)
\]

Comme \( \sum 1/n \) diverge et que les deux séries en présence sont à termes positifs, on peut appliquer la partie (ii) du théorème 5 qui entraîne

> Since \( \sum 1/n \) diverges and both series involved have positive terms, we can apply part (ii) of theorem 5, which implies

\[
{H}_{n} \sim  \mathop{\sum }\limits_{{k = 1}}^{n}\log \left( {1 + \frac{1}{k}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\log \left( \frac{k + 1}{k}\right)  = \log \left( {\mathop{\prod }\limits_{{k = 1}}^{n}\frac{k + 1}{k}}\right)  = \log \left( {n + 1}\right) ,
\]

autrement dit \( {H}_{n} \sim \log n \) .

> in other words \( {H}_{n} \sim \log n \) .

b) Nous avons obtenu le premier terme de notre développement asymptotique. Pour ob-tenir le suivant, on considère la suite \( {U}_{n} = {H}_{n} - \log n \) , et on écrit

> b) We have obtained the first term of our asymptotic expansion. To obtain the next one, we consider the sequence \( {U}_{n} = {H}_{n} - \log n \) , and we write

\[
{U}_{n} - {U}_{n - 1} = \frac{1}{n} - \log n + \log \left( {n - 1}\right)  = \frac{1}{n} + \log \left( {1 - \frac{1}{n}}\right)  \sim   - \frac{1}{2{n}^{2}}
\]

(*)

> donc la série \( \sum \left( {{U}_{n} - {U}_{n - 1}}\right) \) converge. Comme

therefore the series \( \sum \left( {{U}_{n} - {U}_{n - 1}}\right) \) converges. Since

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{k = 2}}^{n}\left( {{U}_{k} - {U}_{k - 1}}\right)  = {U}_{n} - {U}_{1},
\]

la suite \( \left( {U}_{n}\right) \) converge. Notons \( \gamma \) sa limite, de sorte que

> the sequence \( \left( {U}_{n}\right) \) converges. Let \( \gamma \) be its limit, such that

\[
{H}_{n} = \log n + {U}_{n} = \log n + \gamma  + o\left( 1\right) .
\]

c) Poursuivons. En appliquant la partie (i) du théorème 5, on en déduit un équivalent des restes de \( \sum \left( {{U}_{n} - {U}_{n - 1}}\right) \) , ce qui s’écrit

> c) Let us continue. By applying part (i) of theorem 5, we deduce an equivalent for the remainders of \( \sum \left( {{U}_{n} - {U}_{n - 1}}\right) \), which is written

\[
\gamma  - {U}_{n} = \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\left( {{U}_{k} - {U}_{k - 1}}\right)  \sim   - \frac{1}{2}\mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{1}{{k}^{2}}.
\]

Pour obtenir un équivalent de ce dernier terme, on écrit

> To obtain an equivalent for this last term, we write

\[
\forall k \geq  2,\;{\int }_{k}^{k + 1}\frac{dt}{{t}^{2}} \leq  \frac{1}{{k}^{2}} \leq  {\int }_{k - 1}^{k}\frac{dt}{{t}^{2}}\;\text{ donc }
\]

\[
\forall n \geq  1,\;\frac{1}{n + 1} = {\int }_{n + 1}^{+\infty }\frac{dt}{{t}^{2}} \leq  \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{1}{{k}^{2}} \leq  {\int }_{n}^{+\infty }\frac{dt}{{t}^{2}} = \frac{1}{n},\;\text{ d’où }\;\mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{1}{{k}^{2}} \sim  \frac{1}{n}.
\]

Finalement, on a démontré

> Finally, we have proven

\[
{U}_{n} - \gamma  \sim  \frac{1}{2}\mathop{\sum }\limits_{{k = n}}^{{+\infty }}\frac{1}{{k}^{2}} \sim  \frac{1}{2n},\;\text{ donc }\;{H}_{n} = \log n + {U}_{n} = \log n + \gamma  + \frac{1}{2n} + o\left( \frac{1}{2n}\right) .
\]

Remarque 3. - Il est important de retenir ce résultat. Le nombre réel \( \gamma \) est une constante classique appelée constante d'Euler. On a \( \gamma = {0.577215664}\ldots \)

> Remark 3. - It is important to remember this result. The real number \( \gamma \) is a classic constant called the Euler constant. We have \( \gamma = {0.577215664}\ldots \)

- On aurait pu poursuivre ce développement asymptotique en itérant la méthode. Un développement asymptotique de \( {H}_{n} \) à un ordre quelconque fait l’objet du sujet d'étude 3 page 321, par la formule d'Euler-Maclaurin.

> - We could have continued this asymptotic expansion by iterating the method. An asymptotic expansion of \( {H}_{n} \) to any order is the subject of study 3 on page 321, using the Euler-Maclaurin formula.

- Cette méthode est assez générale. On peut l'utiliser par exemple sur la série \( \sum \log \left( n\right) \) pour obtenir un développement asymptotique de \( n \) ! à plusieurs termes (voir le commentaire de l'exercice 3 page 219 sur la formule de Stirling).

> - This method is quite general. It can be used, for example, on the series \( \sum \log \left( n\right) \) to obtain a multi-term asymptotic expansion of \( n \)! (see the commentary for exercise 3 on page 219 regarding Stirling's formula).

##### Series-integral comparison.

*Français : Comparaison série-intégrale.*

Proposition 3. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction positive, continue par morceaux et décroissante sur \( {\mathbb{R}}^{ + } \) . Alors la suite \( \left( {U}_{n}\right) \) définie par

> Proposition 3. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a positive, piecewise continuous, and decreasing function on \( {\mathbb{R}}^{ + } \). Then the sequence \( \left( {U}_{n}\right) \) defined by

\[
\forall n \in  \mathbb{N},\;{U}_{n} = f\left( 0\right)  + f\left( 1\right)  + \cdots  + f\left( n\right)  - {\int }_{0}^{n}f\left( t\right) {dt}
\]

est convergente. En particulier, la série \( \sum f\left( n\right) \) et l’intégrale \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) ont même nature.

> is convergent. In particular, the series \( \sum f\left( n\right) \) and the integral \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) have the same nature.

Démonstration. La décroissance de \( f \) entraîne

> Proof. The decreasing nature of \( f \) implies

\[
\forall k \in  \mathbb{N},\;f\left( {k + 1}\right)  \leq  {\int }_{k}^{k + 1}f\left( t\right) {dt} \leq  f\left( k\right) .
\]

On en déduit

> We deduce

\[
\forall n \in  \mathbb{N},\;{U}_{n} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {f\left( k\right)  - {\int }_{k}^{k + 1}f\left( t\right) {dt}}\right)  + f\left( n\right)  \geq  f\left( n\right)  \geq  0
\]

et

\[
\forall n \in  \mathbb{N},\;{U}_{n + 1} - {U}_{n} = f\left( {n + 1}\right)  - {\int }_{n}^{n + 1}f\left( t\right) {dt} \leq  0.
\]

La suite \( \left( {U}_{n}\right) \) est décroissante et minorée, elle converge donc.

> The sequence \( \left( {U}_{n}\right) \) is decreasing and bounded below, therefore it converges.

Remarque 4. Ce résultat reste vrai si \( f \) est seulement supposée décroissante à partir d’une certaine abscisse \( X \) (reprenez la preuve précédente).

> Remark 4. This result remains true if \( f \) is only assumed to be decreasing from a certain abscissa \( X \) (review the previous proof).

- Si \( f \) est \( {\mathcal{C}}^{1} \) à valeurs complexes et \( {f}^{\prime } \) est intégrable sur \( {\mathbb{R}}^{ + } \) , on peut également montrer que la série \( \sum f\left( n\right) \) et l’intégrale \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) ont même nature (voir l’exercice 12 page 227).

> - If \( f \) is \( {\mathcal{C}}^{1} \) with complex values and \( {f}^{\prime } \) is integrable on \( {\mathbb{R}}^{ + } \), one can also show that the series \( \sum f\left( n\right) \) and the integral \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) have the same nature (see exercise 12 on page 227).

Exemple 2. - On retrouve avec ce résultat celui de la proposition 2 sur les séries de Riemann.

> Example 2. - With this result, we recover that of proposition 2 regarding Riemann series.

- Si on applique ce résultat à la fonction \( f : x \mapsto  1/\left( {1 + x}\right) \) , on montre que la suite \( \left( {U}_{n}\right) \) définie par

> - If we apply this result to the function \( f : x \mapsto  1/\left( {1 + x}\right) \), we show that the sequence \( \left( {U}_{n}\right) \) defined by

\[
{U}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - {\int }_{0}^{n - 1}f\left( t\right) {dt} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \log n
\]

converge. En notant \( \gamma \) la limite de \( \left( {U}_{n}\right) \) (c’est la constante d’Euler), on retrouve ainsi le fait que

> converges. By denoting \( \gamma \) as the limit of \( \left( {U}_{n}\right) \) (this is the Euler constant), we thus recover the fact that

\[
{H}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} = \log n + \gamma  + o\left( 1\right) .
\]

Séries de Bertrand. On appelle ainsi les séries de la forme

> Bertrand series. This is the name given to series of the form

\[
\mathop{\sum }\limits_{{n \geq  2}}\frac{1}{{n}^{\alpha }{\log }^{\beta }n},\;\left( {\alpha ,\beta }\right)  \in  {\mathbb{R}}^{2}.
\]

(*)

> On a vu (voir la proposition 6 page 149 sur les intégrales de Bertrand) que

We have seen (see proposition 6 page 149 on Bertrand integrals) that

\[
\left( {{\int }_{2}^{+\infty }\frac{dt}{{t}^{\alpha }{\log }^{\beta }t}\;\text{ converge }}\right)  \Leftrightarrow  \;\left( {\left( {\alpha  > 1}\right) \;\text{ ou }\;\left( {\alpha  = 1\text{ et }\beta  > 1}\right) }\right) .
\]

Si \( \alpha \leq 0 \) , il est clair que la série de Bertrand (*) diverge pour tout \( \beta \in \mathbb{R} \) (on peut dire par exemple que le terme général est supérieur à \( 1/n \) à partir d’un certain rang). Si \( \alpha > 0 \) , la fonction \( f\left( t\right) = {t}^{-\alpha }{\log }^{-\beta }t \) étant décroissante au voisinage de \( + \infty \) , on en déduit (voir la remarque précédente) que

> If \( \alpha \leq 0 \), it is clear that the Bertrand series (*) diverges for all \( \beta \in \mathbb{R} \) (we can say for example that the general term is greater than \( 1/n \) from a certain rank). If \( \alpha > 0 \), the function \( f\left( t\right) = {t}^{-\alpha }{\log }^{-\beta }t \) being decreasing in the neighborhood of \( + \infty \), we deduce (see the previous remark) that

\[
\left( {\mathop{\sum }\limits_{{n \geq  2}}\frac{1}{{n}^{\alpha }{\log }^{\beta }n}\text{ converge }}\right)  \Leftrightarrow  \;\left( {\left( {\alpha  > 1}\right) \text{ ou }\left( {\alpha  = 1\text{ et }\beta  > 1}\right) }\right) .
\]
