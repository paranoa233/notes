#### 2.6. Exercises

*Français : 2.6. Exercices*

EXERCICE 1. Soit \( \left( {u}_{n}\right) \) la suite définie par

> EXERCISE 1. Let \( \left( {u}_{n}\right) \) be the sequence defined by

\[
{u}_{0} = 1,\;\forall n \in  \mathbb{N},\;\frac{{u}_{n + 1}}{{u}_{n}} = \frac{n + a}{n + b},
\]

où \( a \) et \( b \) sont deux nombres réels positifs fixés. Donner la nature de la série \( \sum {u}_{n} \) en fonction de \( a \) et \( b \) et calculer sa somme lorsqu’elle converge.

> where \( a \) and \( b \) are two fixed positive real numbers. Determine the nature of the series \( \sum {u}_{n} \) as a function of \( a \) and \( b \) and calculate its sum when it converges.

Solution. Pour la convergence de la série, il suffit de remarquer que lorsque \( n \rightarrow + \infty \) ,

> Solution. For the convergence of the series, it suffices to note that when \( n \rightarrow + \infty \),

\[
\frac{{u}_{n + 1}}{{u}_{n}} = \frac{1}{1 + \left( {b - a}\right) /\left( {n + a}\right) } = \frac{1}{1 + \left( {b - a}\right) /n + O\left( {1/{n}^{2}}\right) },
\]

donc d’après la règle de Raab-Duhamel, il existe \( \lambda > 0 \) tel que \( {u}_{n} \sim \lambda /{n}^{b - a} \) . Ainsi, \( \sum {u}_{n} \) converge si et seulement si \( b - a > 1 \) .

> therefore, according to Raabe-Duhamel's rule, there exists \( \lambda > 0 \) such that \( {u}_{n} \sim \lambda /{n}^{b - a} \). Thus, \( \sum {u}_{n} \) converges if and only if \( b - a > 1 \).

Sommons la série lorsque \( b - a > 1 \) . La relation \( \left( {n + b}\right) {u}_{n + 1} = \left( {n + a}\right) {u}_{n} \) entraîne

> Let us sum the series when \( b - a > 1 \). The relation \( \left( {n + b}\right) {u}_{n + 1} = \left( {n + a}\right) {u}_{n} \) implies

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\left( {k + b}\right) {u}_{k + 1} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( {k + a}\right) {u}_{k}\;\text{ donc }\;\mathop{\sum }\limits_{{k = 1}}^{{n + 1}}\left( {k + b - 1}\right) {u}_{k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( {k + a}\right) {u}_{k},
\]

ce qui s’écrit

> which is written as

\[
\left( {b - a - 1}\right) \left( {\mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}}\right)  + \left( {n + b}\right) {u}_{n + 1} = \left( {b - 1}\right) {u}_{0}.
\]

(*)

> Lorsque \( n \rightarrow + \infty ,{u}_{n} \sim \lambda /{n}^{b - a} \) avec \( b - a > 1 \) , donc \( \left( {n + b}\right) {u}_{n + 1} \rightarrow 0 \) , et en faisant \( n \rightarrow + \infty \) dans (*), on obtient finalement

When \( n \rightarrow + \infty ,{u}_{n} \sim \lambda /{n}^{b - a} \) with \( b - a > 1 \) , thus \( \left( {n + b}\right) {u}_{n + 1} \rightarrow 0 \) , and by setting \( n \rightarrow + \infty \) in (*), we finally obtain

\[
\left( {b - a - 1}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} = \left( {b - 1}\right) {u}_{0} = \left( {b - 1}\right) \;\text{ donc }\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} = \frac{b - 1}{b - a - 1}.
\]

EXERCICE 2. Soit \( \left( {u}_{n}\right) \) une suite à termes positifs et décroissante. Si la série \( \sum {u}_{n} \) converge, montrer que \( {u}_{n} = o\left( {1/n}\right) \) lorsque \( n \rightarrow + \infty \) .

> EXERCISE 2. Let \( \left( {u}_{n}\right) \) be a decreasing sequence of positive terms. If the series \( \sum {u}_{n} \) converges, show that \( {u}_{n} = o\left( {1/n}\right) \) as \( n \rightarrow + \infty \) .

Solution. Soit \( \varepsilon > 0 \) . La série \( \sum {u}_{n} \) converge donc il existe \( N \in \mathbb{N} \) tel que \( \mathop{\sum }\limits_{{n = N + 1}}^{\infty }{u}_{n} < \varepsilon \) . On en déduit, la suite \( \left( {u}_{n}\right) \) étant décroissante, que

> Solution. Let \( \varepsilon > 0 \) . The series \( \sum {u}_{n} \) converges, so there exists \( N \in \mathbb{N} \) such that \( \mathop{\sum }\limits_{{n = N + 1}}^{\infty }{u}_{n} < \varepsilon \) . We deduce, since the sequence \( \left( {u}_{n}\right) \) is decreasing, that

\[
\forall p > N,\;\left( {p - N}\right) {u}_{p} \leq  {u}_{N + 1} + {u}_{N + 2} + \cdots  + {u}_{p} \leq  \mathop{\sum }\limits_{{n = N + 1}}^{\infty }{u}_{n} < \varepsilon ,
\]

donc pour tout \( p > {2N},\left( {p/2}\right) {u}_{p} \leq \left( {p - N}\right) {u}_{p} < \varepsilon \) . Finalement, nous avons \( 0 \leq p{u}_{p} \leq {2\varepsilon } \) pour tout \( p > {2N} \) . Ainsi, \( \left( {n{u}_{n}}\right) \) tend vers0, d’où le résultat.

> thus for all \( p > {2N},\left( {p/2}\right) {u}_{p} \leq \left( {p - N}\right) {u}_{p} < \varepsilon \) . Finally, we have \( 0 \leq p{u}_{p} \leq {2\varepsilon } \) for all \( p > {2N} \) . Thus, \( \left( {n{u}_{n}}\right) \) tends to 0, hence the result.

Remarque. Ce résultat est la version discrète de celui de l'exercice 4 page 156.

> Remark. This result is the discrete version of the one in exercise 4 on page 156.

EXERCICE 3 (FORMULE DE STIRLING). On considère la suite \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) définie par

> EXERCISE 3 (STIRLING'S FORMULA). Consider the sequence \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) defined by

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \frac{{n}^{n}{e}^{-n}\sqrt{n}}{n!}.
\]

Donner la nature de la série de terme général \( {v}_{n} = \log \left( {{u}_{n + 1}/{u}_{n}}\right) \) . En déduire l’existence d’un entier \( k > 0 \) tel que

> Determine the nature of the series with general term \( {v}_{n} = \log \left( {{u}_{n + 1}/{u}_{n}}\right) \) . Deduce the existence of an integer \( k > 0 \) such that

\[
n! \sim  k\sqrt{n}{n}^{n}{e}^{-n}\;n \rightarrow   + \infty .
\]

(*)

> Calculer la constante \( k \) en utilisant la formule de Wallis (voir l’exercice 1 page 130).

Calculate the constant \( k \) using Wallis's formula (see exercise 1 on page 130).

> Solution. Estimons \( {v}_{n} \) lorsque \( n \rightarrow + \infty \) :

Solution. Let us estimate \( {v}_{n} \) as \( n \rightarrow + \infty \) :

\[
{v}_{n} = \log \left\lbrack  {{\left( \frac{n + 1}{n}\right) }^{n + 1/2}{e}^{-1}}\right\rbrack   =  - 1 + \left( {n + \frac{1}{2}}\right) \log \left( {1 + \frac{1}{n}}\right)
\]

\[
=  - 1 + \left( {n + \frac{1}{2}}\right) \left( {\frac{1}{n} - \frac{1}{2{n}^{2}} + O\left( \frac{1}{{n}^{3}}\right) }\right)  = O\left( \frac{1}{{n}^{2}}\right) .
\]

Cette expression montre que \( \sum {v}_{n} \) converge. Comme on a \( {v}_{1} + \cdots + {v}_{n} = \log {u}_{n + 1} - \log {u}_{1} \) pour tout \( n \) , la suite \( \left( {\log {u}_{n}}\right) \) converge. En notant \( \lambda \) sa limite, on voit que \( \left( {u}_{n}\right) \) converge vers \( k = {e}^{\lambda } > 0 \) , d’où l’équivalent (*).

> This expression shows that \( \sum {v}_{n} \) converges. Since we have \( {v}_{1} + \cdots + {v}_{n} = \log {u}_{n + 1} - \log {u}_{1} \) for all \( n \) , the sequence \( \left( {\log {u}_{n}}\right) \) converges. Denoting its limit by \( \lambda \) , we see that \( \left( {u}_{n}\right) \) converges to \( k = {e}^{\lambda } > 0 \) , hence the equivalent (*).

Il nous reste à calculer la constante \( k \) . Comme indiqué dans l’énoncé, nous allons utiliser la formule de Wallis qui est

> It remains for us to calculate the constant \( k \) . As indicated in the problem statement, we will use Wallis's formula, which is

\[
\mathop{\lim }\limits_{{p \rightarrow   + \infty }}\frac{1}{p}{\left\lbrack  \frac{{2p}\left( {{2p} - 2}\right) \cdots 2}{\left( {{2p} - 1}\right) \left( {{2p} - 3}\right) \cdots 1}\right\rbrack  }^{2} = \pi .
\]

Par ailleurs, en utilisant l’équivalent (*) on a lorsque \( p \rightarrow + \infty \)

> Furthermore, using the equivalent (*) we have as \( p \rightarrow + \infty \)

\[
\frac{1}{p}{\left\lbrack  \frac{{2p}\left( {{2p} - 2}\right) \cdots 2}{\left( {{2p} - 1}\right) \left( {{2p} - 3}\right) \cdots 1}\right\rbrack  }^{2} = \frac{1}{p}{\left\lbrack  \frac{{2}^{2p}{\left( p!\right) }^{2}}{\left( {2p}\right) !}\right\rbrack  }^{2} \sim  \frac{{2}^{4p}}{p}\frac{{k}^{4}{p}^{{4p} + 2}{e}^{-{4p}}}{{k}^{2}{\left( 2p\right) }^{{4p} + 1}{e}^{-{4p}}} = \frac{{k}^{2}}{2},
\]

donc \( \pi = {k}^{2}/2 \) d’après la formule de Wallis, d’où \( k = \sqrt{2\pi } \) . Finalement, le résultat obtenu est

> thus \( \pi = {k}^{2}/2 \) according to Wallis's formula, hence \( k = \sqrt{2\pi } \) . Finally, the result obtained is

\[
n! \sim  \sqrt{2\pi n}{n}^{n}{e}^{-n}\;n \rightarrow   + \infty .
\]

Remarque. Il faut connaître ce résultat et savoir le prouver. A partir de la série \( \sum {v}_{n} \) , en procédant comme on l'a fait page 211 pour donner un développement asymptotique des nombres harmoniques, il est possible de calculer un développement asymptotique de \( n \) !.

> Remark. One must know this result and how to prove it. Starting from the series \( \sum {v}_{n} \) , by proceeding as done on page 211 to provide an asymptotic expansion of harmonic numbers, it is possible to calculate an asymptotic expansion of \( n \) !.

Une version continue de la formule de Stirling est traitée dans l'exemple 2 page 166.

> A continuous version of Stirling's formula is covered in example 2 on page 166.

EXERCICE 4. a) Montrer l'égalité

> EXERCISE 4. a) Show the equality

\[
\mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\left( {\zeta \left( k\right)  - 1}\right)  = 1,\;\text{ où }\;\zeta \left( k\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{k}}.
\]

b) Montrer l'égalité

> b) Show the equality

\[
\mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\frac{\zeta \left( k\right)  - 1}{k} = 1 - \gamma ,\;\text{ où }\;\gamma  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \log n.
\]

Solution. a) Il s'agit d'un exercice d'interversion de sommation. Pour tout \( k \geq 2 \) , la série à termes positifs \( \mathop{\sum }\limits_{{n \geq 2}}1/{n}^{k} \) est convergente, et sa somme \( \zeta \left( k\right) - 1 \) vérifie

> Solution. a) This is an exercise in interchanging summation. For any \( k \geq 2 \), the series with positive terms \( \mathop{\sum }\limits_{{n \geq 2}}1/{n}^{k} \) is convergent, and its sum \( \zeta \left( k\right) - 1 \) satisfies

\[
\zeta \left( k\right)  - 1 = \frac{1}{{2}^{k}} + \mathop{\sum }\limits_{{n = 3}}^{{+\infty }}\frac{1}{{n}^{k}} \leq  \frac{1}{{2}^{k}} + {\int }_{2}^{+\infty }\frac{dt}{{t}^{k}} = \frac{1}{{2}^{k}} + \frac{1}{\left( {k + 1}\right) {2}^{k}} \leq  \frac{1}{{2}^{k - 1}}.
\]

La série à termes positifs \( \mathop{\sum }\limits_{{k \geq 2}}\left( {\zeta \left( k\right) - 1}\right) \) est donc convergente. Les séries en présence étant convergentes et à termes positifs, elles sont absolument convergentes donc on peut donc appliquer le théorème d'interversion de sommation (voir le théorème 10 page 217) qui entraîne

> The series with positive terms \( \mathop{\sum }\limits_{{k \geq 2}}\left( {\zeta \left( k\right) - 1}\right) \) is therefore convergent. Since the series involved are convergent and have positive terms, they are absolutely convergent, so we can apply the theorem on the interchange of summation (see theorem 10 on page 217), which leads to

\[
\mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\left( {\zeta \left( k\right)  - 1}\right)  = \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\frac{1}{{n}^{k}}}\right)  = \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\frac{1}{{n}^{k}}}\right)  = \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\frac{1}{n\left( {n - 1}\right) } = \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\left( {\frac{1}{n - 1} - \frac{1}{n}}\right)
\]

d'où le résultat.

> hence the result.

b) Remarquons que si \( {U}_{n} = \left( {\mathop{\sum }\limits_{{k = 1}}^{n}1/k}\right) - \log n \) , on a

> b) Note that if \( {U}_{n} = \left( {\mathop{\sum }\limits_{{k = 1}}^{n}1/k}\right) - \log n \), we have

\[
\forall n \geq  2,\;{\delta }_{n} = {U}_{n} - {U}_{n - 1} = \frac{1}{n} - \log n + \log \left( {n - 1}\right)  = \frac{1}{n} + \log \left( {1 - \frac{1}{n}}\right)  =  - \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\frac{1}{k{n}^{k}}
\]

où le dernier terme est obtenu grâce au développement de \( \log \left( {1 - 1/n}\right) \) en série entière. Ceci assure la convergence de la série \( \mathop{\sum }\limits_{{k \geq 2}}1/\left( {k{n}^{k}}\right) \) . Par ailleurs, l’égalité

> where the last term is obtained through the power series expansion of \( \log \left( {1 - 1/n}\right) \). This ensures the convergence of the series \( \mathop{\sum }\limits_{{k \geq 2}}1/\left( {k{n}^{k}}\right) \). Furthermore, the equality

\[
\forall N > 2,\;\mathop{\sum }\limits_{{n = 2}}^{N}{\delta }_{n} = \mathop{\sum }\limits_{{n = 2}}^{N}\left( {{U}_{n} - {U}_{n - 1}}\right)  = {U}_{N} - {U}_{1} = {U}_{N} - 1,
\]

associée à la convergence de \( \left( {U}_{n}\right) \) vers la constante d’Euler \( \gamma \) (c’est classique, voir par exemple la page 211 sur les sommes harmoniques), prouve que la série à termes négatifs \( \mathop{\sum }\limits_{{n \geq 2}}{\delta }_{n} \) converge, et sa somme est \( \gamma - 1 \) . On peut appliquer le théorème d’interversion des limites (les séries sont toutes à termes négatifs et convergentes, donc absolument convergentes) qui entraîne

> associated with the convergence of \( \left( {U}_{n}\right) \) to the Euler constant \( \gamma \) (this is standard, see for example page 211 on harmonic sums), proves that the series with negative terms \( \mathop{\sum }\limits_{{n \geq 2}}{\delta }_{n} \) converges, and its sum is \( \gamma - 1 \). We can apply the theorem on the interchange of limits (the series all have negative terms and are convergent, hence absolutely convergent), which leads to

\[
1 - \gamma  =  - \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}{\delta }_{n} = \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\frac{1}{k{n}^{k}}}\right)  = \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\frac{1}{k{n}^{k}}}\right)  = \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}\frac{\zeta \left( k\right)  - 1}{k}
\]

d'où le résultat.

> hence the result.

EXERCICE 5. Soit \( f : {\mathbb{R}}^{ + } \rightarrow {\mathbb{R}}^{+ * } \) une fonction de classe \( {\mathcal{C}}^{1} \) vérifiant

> EXERCISE 5. Let \( f : {\mathbb{R}}^{ + } \rightarrow {\mathbb{R}}^{+ * } \) be a \( {\mathcal{C}}^{1} \) class function satisfying

\[
\mathop{\lim }\limits_{{x \rightarrow   + \infty }}\frac{{f}^{\prime }\left( x\right) }{f\left( x\right) } =  - \infty .
\]

Montrer que la série \( \sum f\left( n\right) \) converge et donner un équivalent, lorsque \( n \rightarrow + \infty \) , de \( {R}_{n} = \mathop{\sum }\limits_{{k = n}}^{{+\infty }}f\left( k\right) . \)

> Show that the series \( \sum f\left( n\right) \) converges and provide an equivalent, as \( n \rightarrow + \infty \), for \( {R}_{n} = \mathop{\sum }\limits_{{k = n}}^{{+\infty }}f\left( k\right) . \)

Solution. Soit \( A > 0 \) . Il existe \( N > 0 \) tel que pour tout \( x \geq N,{f}^{\prime }\left( x\right) /f\left( x\right) \leq - A \) . Ainsi, si on se donne un entier \( n \geq N \) , on peut écrire

> Solution. Let \( A > 0 \). There exists \( N > 0 \) such that for all \( x \geq N,{f}^{\prime }\left( x\right) /f\left( x\right) \leq - A \). Thus, if we choose an integer \( n \geq N \), we can write

\[
\forall p \geq  n,\;\log \frac{f\left( {n + p}\right) }{f\left( n\right) } = {\int }_{n}^{n + p}\frac{{f}^{\prime }\left( x\right) }{f\left( x\right) }{dx} \leq  {\int }_{n}^{n + p} - {Adx} =  - {pA},
\]

de sorte que \( f\left( {n + p}\right) \leq f\left( n\right) {e}^{-{pA}} \) pour tout \( p \in {\mathbb{N}}^{ * } \) . La fonction \( f \) étant positive, ceci assure la convergence de la série \( \sum f\left( n\right) \) . De plus, notre majoration entraîne

> so that \( f\left( {n + p}\right) \leq f\left( n\right) {e}^{-{pA}} \) for all \( p \in {\mathbb{N}}^{ * } \). Since the function \( f \) is positive, this ensures the convergence of the series \( \sum f\left( n\right) \). Furthermore, our bound implies

\[
\forall n \geq  N,\;0 \leq  {R}_{n + 1} = \mathop{\sum }\limits_{{p = 1}}^{{+\infty }}f\left( {n + p}\right)  \leq  f\left( n\right) \mathop{\sum }\limits_{{p = 1}}^{{+\infty }}{e}^{-{pA}} = \frac{{e}^{-A}}{1 - {e}^{-A}}f\left( n\right) .
\]

Comme on peut prendre \( A \) aussi grand que l’on veut, nous avons en fait montré que

> Since we can take \( A \) as large as we want, we have in fact shown that

\[
\forall \varepsilon  > 0,\exists N > 0,\forall n \geq  N,\;0 \leq  {R}_{n + 1} \leq  {\varepsilon f}\left( n\right) .
\]

Autrement dit, \( {R}_{n + 1} = o\left( {f\left( n\right) }\right) \) , donc \( {R}_{n} = f\left( n\right) + {R}_{n + 1} \sim f\left( n\right) \) lorsque \( n \rightarrow + \infty \) .

> In other words, \( {R}_{n + 1} = o\left( {f\left( n\right) }\right) \), so \( {R}_{n} = f\left( n\right) + {R}_{n + 1} \sim f\left( n\right) \) as \( n \rightarrow + \infty \).

Remarque. Un exemple d’application de ce résultat est la convergence de \( \sum {e}^{-{n}^{2}} \) et le fait que \( \mathop{\sum }\limits_{{p = n}}^{{+\infty }}{e}^{-{p}^{2}} \sim {e}^{-{n}^{2}} \) .

> Remark. An example of an application of this result is the convergence of \( \sum {e}^{-{n}^{2}} \) and the fact that \( \mathop{\sum }\limits_{{p = n}}^{{+\infty }}{e}^{-{p}^{2}} \sim {e}^{-{n}^{2}} \) .

EXERCICE 6. Soit \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) une série à termes \( > 0 \) .

> EXERCISE 6. Let \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) be a series with \( > 0 \) terms.

1 / a) Si \( \sum {u}_{n} \) diverge, discuter en fonction du paramètre \( \alpha > 0 \) la nature de la série

> 1 / a) If \( \sum {u}_{n} \) diverges, discuss the nature of the series according to the parameter \( \alpha > 0 \)

\[
\sum \frac{{u}_{n}}{{S}_{n}^{\alpha }},\;\text{ où }\;{S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k}.
\]

b) On suppose \( {u}_{n} = o\left( {S}_{n}\right) \) lorsque \( n \rightarrow + \infty \) . Exprimer en fonction de \( {S}_{n} \) un équivalent des sommes partielles (resp. des restes) de la série \( \sum {u}_{n}/{S}_{n}^{\alpha } \) lorsqu’elle diverge (resp. lorsqu'elle converge).

> b) Assume \( {u}_{n} = o\left( {S}_{n}\right) \) as \( n \rightarrow + \infty \) . Express an equivalent of the partial sums (resp. remainders) of the series \( \sum {u}_{n}/{S}_{n}^{\alpha } \) in terms of \( {S}_{n} \) when it diverges (resp. when it converges).

2/ a) Si \( \sum {u}_{n} \) converge, discuter en fonction du paramètre \( \alpha > 0 \) la nature de la série

> 2/ a) If \( \sum {u}_{n} \) converges, discuss the nature of the series according to the parameter \( \alpha > 0 \)

\[
\sum \frac{{u}_{n}}{{R}_{n}^{\alpha }},\;\text{ où }\;{R}_{n} = \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{u}_{k}.
\]

b) On suppose \( {u}_{n} = o\left( {R}_{n}\right) \) lorsque \( n \rightarrow + \infty \) . Exprimer en fonction de \( {R}_{n} \) un équivalent des sommes partielles (resp. des restes) de la série \( \sum {u}_{n}/{R}_{n}^{\alpha } \) lorsqu’elle diverge (resp. lorsqu'elle converge).

> b) Assume \( {u}_{n} = o\left( {R}_{n}\right) \) as \( n \rightarrow + \infty \) . Express an equivalent of the partial sums (resp. remainders) of the series \( \sum {u}_{n}/{R}_{n}^{\alpha } \) in terms of \( {R}_{n} \) when it diverges (resp. when it converges).

Solution. 1/ a) Ceci dépend de la position de \( \alpha \) par rapport à 1, comme on le voit dans le cas où \( {u}_{n} = 1 \) pour tout \( n \) (dans ce cas, on a affaire aux séries de Riemann).

> Solution. 1/ a) This depends on the position of \( \alpha \) relative to 1, as seen in the case where \( {u}_{n} = 1 \) for all \( n \) (in this case, we are dealing with Riemann series).

- Si \( \alpha  > 1 \) , on écrit

> - If \( \alpha  > 1 \) , we write

\[
\forall n \in  {\mathbb{N}}^{ * },\;\frac{{u}_{n}}{{S}_{n}^{\alpha }} = \frac{{S}_{n} - {S}_{n - 1}}{{S}_{n}^{\alpha }} \leq  {\int }_{{S}_{n - 1}}^{{S}_{n}}\frac{dt}{{t}^{\alpha }}\;\text{ donc }\;\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{u}_{k}}{{S}_{k}^{\alpha }} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}{\int }_{{S}_{k - 1}}^{{S}_{k}}\frac{dt}{{t}^{\alpha }} = {\int }_{{S}_{0}}^{{S}_{n}}\frac{dt}{{t}^{\alpha }},
\]

et comme \( \alpha > 1 \) , on en conclut que les sommes partielles de la série à termes positifs \( \sum {u}_{n}/{S}_{n}^{\alpha } \) sont majorées. Si \( \alpha > 1 \) , la série \( \sum {u}_{n}/{S}_{n}^{\alpha } \) est donc convergente.

> and since \( \alpha > 1 \) , we conclude that the partial sums of the series with positive terms \( \sum {u}_{n}/{S}_{n}^{\alpha } \) are bounded. If \( \alpha > 1 \) , the series \( \sum {u}_{n}/{S}_{n}^{\alpha } \) is therefore convergent.

— Si \( \alpha \leq 1 \) , nous allons montrer que la série diverge. Par hypothèse, \( \sum {u}_{n} \) diverge, donc il existe \( N \in \mathbb{N} \) tel que \( {S}_{n} \geq 1 \) pour tout \( n \geq N \) . On écrit ensuite

> — If \( \alpha \leq 1 \) , we will show that the series diverges. By hypothesis, \( \sum {u}_{n} \) diverges, so there exists \( N \in \mathbb{N} \) such that \( {S}_{n} \geq 1 \) for all \( n \geq N \) . We then write

\[
\forall p \geq  N,\forall q > p,\;\mathop{\sum }\limits_{{n = p + 1}}^{q}\frac{{u}_{n}}{{S}_{n}^{\alpha }} \geq  \mathop{\sum }\limits_{{n = p + 1}}^{q}\frac{{u}_{n}}{{S}_{n}} \geq  \frac{{u}_{p + 1} + \cdots  + {u}_{q}}{{S}_{q}} = \frac{{S}_{q} - {S}_{p}}{{S}_{q}} = 1 - \frac{{S}_{p}}{{S}_{q}}.
\]

(*)

> Pour tout \( p \geq N \) , il existe \( q > p \) tel que \( {S}_{q} \geq 2{S}_{p} \) . On en déduit avec (*) que

For all \( p \geq N \) , there exists \( q > p \) such that \( {S}_{q} \geq 2{S}_{p} \) . We deduce from (*) that

\[
\forall p \geq  N,\exists q > p,\;\mathop{\sum }\limits_{{n = p + 1}}^{q}\frac{{u}_{n}}{{S}_{n}^{\alpha }} \geq  \frac{1}{2}.
\]

Le critère de Cauchy n’est donc pas vérifié pour la série \( \sum {u}_{n}/{S}_{n}^{\alpha } \) , elle diverge donc. En résumé, la série \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converge si et seulement si \( \alpha > 1 \) .

> The Cauchy criterion is therefore not satisfied for the series \( \sum {u}_{n}/{S}_{n}^{\alpha } \) , so it diverges. In summary, the series \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converges if and only if \( \alpha > 1 \) .

b) On va utiliser une comparaison série-intégrale. On écrit

> b) We will use a series-integral comparison. We write

\[
\forall n \in  {\mathbb{N}}^{ * },\;\frac{{u}_{n}}{{S}_{n}^{\alpha }} = \frac{{S}_{n} - {S}_{n - 1}}{{S}_{n}^{\alpha }} \leq  {\int }_{{S}_{n - 1}}^{{S}_{n}}\frac{dt}{{t}^{\alpha }} \leq  \frac{{S}_{n} - {S}_{n - 1}}{{S}_{n - 1}^{\alpha }} = \frac{{u}_{n}}{{S}_{n - 1}^{\alpha }},
\]

et comme \( {u}_{n} = o\left( {S}_{n}\right) \) , on a \( {S}_{n - 1} = {S}_{n} - {u}_{n} \sim {S}_{n} \) lorsque \( n \rightarrow + \infty \) , de sorte que notre encadrement entraîne

> and since \( {u}_{n} = o\left( {S}_{n}\right) \) , we have \( {S}_{n - 1} = {S}_{n} - {u}_{n} \sim {S}_{n} \) as \( n \rightarrow + \infty \) , so our inequality implies

\[
\frac{{u}_{n}}{{S}_{n}^{\alpha }} \sim  {\int }_{{S}_{n - 1}}^{{S}_{n}}\frac{dt}{{t}^{\alpha }}.
\]

\( \left( {* * }\right) \)

> (Noter au passage que dans le cas ou \( {u}_{n} = o\left( {S}_{n}\right) \) , cet équivalent est un autre moyen de parvenir au fait que \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converge si et seulement si \( \alpha > 1 \) .) Supposons \( \alpha \leq 1 \) . D’après (**) et le théorème 5 page 210, on a

(Note in passing that in the case where \( {u}_{n} = o\left( {S}_{n}\right) \) , this equivalent is another way to arrive at the fact that \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converges if and only if \( \alpha > 1 \) .) Suppose \( \alpha \leq 1 \) . According to (**) and Theorem 5 on page 210, we have

\[
\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{u}_{k}}{{S}_{k}^{\alpha }} \sim  \mathop{\sum }\limits_{{k = 1}}^{n}{\int }_{{S}_{k - 1}}^{{S}_{k}}\frac{dt}{{t}^{\alpha }} = {\int }_{{S}_{0}}^{{S}_{n}}\frac{dt}{{t}^{\alpha }}.
\]

On en déduit

> We deduce

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{u}_{k}}{{S}_{k}^{\alpha }} \sim  \left\{  {\begin{array}{lll} {S}_{n}^{1 - \alpha }/\left( {1 - \alpha }\right) & \text{ si } & 0 < \alpha  < 1 \\  \log {S}_{n} & \text{ si } & \alpha  = 1 \end{array}.}\right.
\]

Si maintenant \( \alpha > 1 \) , la série \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converge et d’après (**) et le théorème 5, on a

> If now \( \alpha > 1 \) , the series \( \sum {u}_{n}/{S}_{n}^{\alpha } \) converges and according to (**) and theorem 5, we have

\[
\mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{{u}_{n}}{{S}_{n}^{\alpha }} \sim  \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{\int }_{{S}_{k - 1}}^{{S}_{k}}\frac{dt}{{t}^{\alpha }} = {\int }_{{S}_{n}}^{+\infty }\frac{dt}{{t}^{\alpha }} = \frac{1}{\left( {\alpha  - 1}\right) {S}_{n}^{\alpha  - 1}}.
\]

2/ a) Comme précédemment, tout dépend de la position de \( \alpha \) par rapport à 1.

> 2/ a) As before, everything depends on the position of \( \alpha \) relative to 1.

- Si \( \alpha  < 1 \) , on écrit pour tout \( n \)

> - If \( \alpha  < 1 \) , we write for all \( n \)

\[
\frac{{u}_{n}}{{R}_{n}^{\alpha }} = \frac{{R}_{n} - {R}_{n + 1}}{{R}_{n}^{\alpha }} \leq  {\int }_{{R}_{n + 1}}^{{R}_{n}}\frac{dt}{{t}^{\alpha }}\;\text{ donc }\;\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{u}_{k}}{{R}_{k}^{\alpha }} \leq  {\int }_{{R}_{n + 1}}^{{R}_{0}}\frac{dt}{{t}^{\alpha }} \leq  {\int }_{0}^{{R}_{0}}\frac{dt}{{t}^{\alpha }}
\]

(le dernière intégrale converge bien car \( \alpha < 1 \) ). On en déduit que les sommes partielles de la série étudiée sont majorées, la série converge donc.

> (the last integral converges well because \( \alpha < 1 \) ). We deduce that the partial sums of the series under study are bounded, so the series converges.

- Si \( \alpha  \geq  1 \) , on commence par fixer un entier \( N \in  \mathbb{N} \) tel que \( {R}_{n} \leq  1 \) pour tout \( n \geq  N \) , puis on écrit

> - If \( \alpha  \geq  1 \) , we start by fixing an integer \( N \in  \mathbb{N} \) such that \( {R}_{n} \leq  1 \) for all \( n \geq  N \) , then we write

\[
\forall p, q \geq  N,\left( {q > p}\right) ,\;\mathop{\sum }\limits_{{k = p}}^{{q - 1}}\frac{{u}_{k}}{{R}_{k}^{\alpha }} \geq  \mathop{\sum }\limits_{{k = p}}^{{q - 1}}\frac{{u}_{k}}{{R}_{k}} \geq  \frac{{u}_{p} + \cdots  + {u}_{q - 1}}{{R}_{p}} = \frac{{R}_{p} - {R}_{q}}{{R}_{p}} = 1 - \frac{{R}_{q}}{{R}_{q}}.
\]

L’entier \( p \geq N \) étant fixé, il existe \( q > p \) tel que \( {R}_{q} < {R}_{p}/2 \) , et la dernière expression montre alors que notre série ne satisfait pas le critère de Cauchy. Elle diverge donc si \( \alpha \geq 1 \) . Finalement, nous avons montré que \( \sum {u}_{n}/{R}_{n}^{\alpha } \) converge si et seulement si \( \alpha < 1 \) .

> With the integer \( p \geq N \) fixed, there exists \( q > p \) such that \( {R}_{q} < {R}_{p}/2 \) , and the last expression then shows that our series does not satisfy the Cauchy criterion. It therefore diverges if \( \alpha \geq 1 \) . Finally, we have shown that \( \sum {u}_{n}/{R}_{n}^{\alpha } \) converges if and only if \( \alpha < 1 \) .

b) En procédant comme dans la solution de la question 1/ b), on montre que sous l'hypothèse \( {u}_{n} = o\left( {R}_{n}\right) , \)

> b) By proceeding as in the solution to question 1/ b), we show that under the hypothesis \( {u}_{n} = o\left( {R}_{n}\right) , \)

\[
\frac{{u}_{n}}{{R}_{n}^{\alpha }} \sim  {\int }_{{R}_{n}}^{{R}_{n + 1}}\frac{dt}{{t}^{\alpha }}.
\]

En poursuivant le raisonnement comme nous l'avions fait plus haut, on en déduit

> By continuing the reasoning as we did above, we deduce

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{u}_{k}}{{R}_{k}^{\alpha }} \sim  \left\{  {\begin{array}{ll} \log \left( {1/{R}_{n}}\right) & \text{ si }\alpha  = 1, \\  {\left( \left( \alpha  - 1\right) {R}_{n}^{\alpha  - 1}\right) }^{-1} & \text{ si }\alpha  > 1, \end{array}\;\text{ et pour }\alpha  < 1\;\mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{{u}_{n}}{{R}_{n}^{\alpha }} \sim  \frac{{R}_{n}^{1 - \alpha }}{1 - \alpha }.}\right.
\]

EXERCICE 7. a) Discuter en fonction du paramètre \( \alpha > 0 \) la nature de la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{u}_{n} \) où

> EXERCISE 7. a) Discuss the nature of the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{u}_{n} \) as a function of the parameter \( \alpha > 0 \) , where

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \frac{{\left( -1\right) }^{n - 1}}{{n}^{\alpha } + {\left( -1\right) }^{n}}.
\]

b) Discuter en fonction des réels \( \theta ,\varphi \) la nature de la série \( \mathop{\sum }\limits_{{n \geq 2}}{u}_{n} \) où

> b) Discuss the nature of the series \( \mathop{\sum }\limits_{{n \geq 2}}{u}_{n} \) as a function of the real numbers \( \theta ,\varphi \) , where

\[
\forall n \geq  2,\;{u}_{n} = \frac{{e}^{ni\theta }}{\sqrt{n} + {e}^{ni\varphi }}.
\]

c) Plus généralement, discuter en fonction des paramètres \( \theta ,\varphi \in \mathbb{R} \) et \( \alpha > 0 \) la nature de la série \( \mathop{\sum }\limits_{{n \geq 2}}{u}_{n} \) où

> c) More generally, discuss the nature of the series \( \mathop{\sum }\limits_{{n \geq 2}}{u}_{n} \) as a function of the parameters \( \theta ,\varphi \in \mathbb{R} \) and \( \alpha > 0 \) , where

\[
\forall n \geq  2,\;{u}_{n} = \frac{{e}^{ni\theta }}{{n}^{\alpha } + {e}^{ni\varphi }}.
\]

Solution. a) On a affaire à une série alternée. Attention à ne pas commettre l'erreur d'appliquer directement le théorème 6 page 214, sous prétexte que la suite \( \left( {{n}^{\alpha } + {\left( -1\right) }^{n}}\right) \) est "pratiquement" décroissante.

> Solution. a) We are dealing with an alternating series. Be careful not to make the mistake of applying Theorem 6 on page 214 directly, under the pretext that the sequence \( \left( {{n}^{\alpha } + {\left( -1\right) }^{n}}\right) \) is "practically" decreasing.

Une bonne manière de procéder est de calculer un développement asymptotique de \( \left( {u}_{n}\right) \) :

> A good way to proceed is to calculate an asymptotic expansion of \( \left( {u}_{n}\right) \) :

\[
{u}_{n} = \frac{{\left( -1\right) }^{n - 1}}{{n}^{\alpha }}\frac{1}{1 + {\left( -1\right) }^{n}{n}^{-\alpha }} = \frac{{\left( -1\right) }^{n - 1}}{{n}^{\alpha }} + \frac{1}{{n}^{2\alpha }} + o\left( \frac{1}{{n}^{2\alpha }}\right)  = {v}_{n} + {w}_{n},
\]

\[
{v}_{n} = \frac{{\left( -1\right) }^{n - 1}}{{n}^{\alpha }},\;{w}_{n} \sim  \frac{1}{{n}^{2\alpha }}.
\]

La série \( \sum {v}_{n} \) converge d’après le théorème 6 page 214, et comme \( {u}_{n} = {v}_{n} + {w}_{n} \) , on en déduit que \( \sum {u}_{n} \) et \( \sum {w}_{n} \) ont même nature. Comme \( {w}_{n} \sim {n}^{-{2\alpha }} \) (et que \( {w}_{n} \in \mathbb{R} \) ), on voit finalement que \( \sum {u}_{n} \) converge si et seulement si \( \alpha > 1/2 \) .

> The series \( \sum {v}_{n} \) converges according to Theorem 6 on page 214, and since \( {u}_{n} = {v}_{n} + {w}_{n} \) , we deduce that \( \sum {u}_{n} \) and \( \sum {w}_{n} \) have the same nature. Since \( {w}_{n} \sim {n}^{-{2\alpha }} \) (and since \( {w}_{n} \in \mathbb{R} \) ), we finally see that \( \sum {u}_{n} \) converges if and only if \( \alpha > 1/2 \) .

b) Comme précédemment, le plus sûr est de calculer un développement asymptotique de \( \left( {u}_{n}\right) \) :

> b) As before, the safest way is to calculate an asymptotic expansion of \( \left( {u}_{n}\right) \) :

\[
{u}_{n} = \frac{{e}^{ni\theta }}{\sqrt{n}}\left( \frac{1}{1 + {e}^{ni\varphi }/\sqrt{n}}\right)  = {v}_{n} + {w}_{n} + O\left( \frac{1}{{n}^{3/2}}\right) ,\;{v}_{n} = \frac{{e}^{ni\theta }}{\sqrt{n}},\;{w}_{n} =  - \frac{{e}^{{ni}\left( {\theta  + \varphi }\right) }}{n}.
\]

Ceci montre que la série \( \sum {u}_{n} - \left( {{v}_{n} + {w}_{n}}\right) \) converge, donc \( \sum {u}_{n} \) est de même nature que \( \sum \left( {{v}_{n} + }\right. \; {w}_{n} \) ). A ce stade, on traite plusieurs cas.

> This shows that the series \( \sum {u}_{n} - \left( {{v}_{n} + {w}_{n}}\right) \) converges, so \( \sum {u}_{n} \) is of the same nature as \( \sum \left( {{v}_{n} + }\right. \; {w}_{n} \) ). At this stage, we treat several cases.

(i) Si \( \theta \notin {2\pi }\mathbb{Z} \) et \( \theta + \varphi \notin {2\pi }\mathbb{Z} \) , alors chacune des séries \( \sum {v}_{n} \) et \( \sum {w}_{n} \) converge (c’est la plus classique conséquence de la règle d’Abel, voir l’exemple 3 page 215), donc \( \sum \left( {{v}_{n} + {w}_{n}}\right) \) converge, donc \( \sum {u}_{n} \) converge.

> (i) If \( \theta \notin {2\pi }\mathbb{Z} \) and \( \theta + \varphi \notin {2\pi }\mathbb{Z} \) , then each of the series \( \sum {v}_{n} \) and \( \sum {w}_{n} \) converges (this is the most classic consequence of Abel's test, see example 3 on page 215), therefore \( \sum \left( {{v}_{n} + {w}_{n}}\right) \) converges, so \( \sum {u}_{n} \) converges.

(ii) Si \( \theta \in {2\pi }\mathbb{Z} \) et \( \theta + \varphi \in {2\pi }\mathbb{Z} \) , on a \( {v}_{n} + {w}_{n} \sim 1/\sqrt{n} \) , et comme \( {v}_{n} + {w}_{n} \in \mathbb{R},\sum \left( {{v}_{n} + {w}_{n}}\right) \) diverge, donc \( \sum {u}_{n} \) diverge.

> (ii) If \( \theta \in {2\pi }\mathbb{Z} \) and \( \theta + \varphi \in {2\pi }\mathbb{Z} \) , we have \( {v}_{n} + {w}_{n} \sim 1/\sqrt{n} \) , and since \( {v}_{n} + {w}_{n} \in \mathbb{R},\sum \left( {{v}_{n} + {w}_{n}}\right) \) diverges, therefore \( \sum {u}_{n} \) diverges.

(iii) Si l’un et l’un seulement des réels \( \theta ,\theta + \varphi \) est un multiple de \( {2\pi } \) , alors parmi les séries \( \sum {v}_{n} \) et \( \sum {w}_{n} \) , l’une est divergente et l’autre convergente (ce dernier point est toujours justifié par la règle d’Abel). On en déduit que \( \sum \left( {{v}_{n} + {w}_{n}}\right) \) diverge, donc \( \sum {u}_{n} \) diverge.

> (iii) If one and only one of the real numbers \( \theta ,\theta + \varphi \) is a multiple of \( {2\pi } \) , then among the series \( \sum {v}_{n} \) and \( \sum {w}_{n} \) , one is divergent and the other is convergent (this last point is always justified by Abel's test). We deduce that \( \sum \left( {{v}_{n} + {w}_{n}}\right) \) diverges, so \( \sum {u}_{n} \) diverges.

Finalement, nous avons montré que \( \sum {u}_{n} \) converge si et seulement si \( \theta \notin {2\pi }\mathbb{Z} \) et \( \theta + \varphi \notin {2\pi }\mathbb{Z} \) . c) On généralise la méthode précédente. L'idée est de calculer un développement asymptotique de \( \left( {u}_{n}\right) \) jusqu’à un terme d’erreur de la forme \( O\left( {1/{n}^{a}}\right) \) avec \( a > 1 \) .

> Finally, we have shown that \( \sum {u}_{n} \) converges if and only if \( \theta \notin {2\pi }\mathbb{Z} \) and \( \theta + \varphi \notin {2\pi }\mathbb{Z} \) . c) We generalize the previous method. The idea is to calculate an asymptotic expansion of \( \left( {u}_{n}\right) \) up to an error term of the form \( O\left( {1/{n}^{a}}\right) \) with \( a > 1 \) .

Si \( \alpha > 1 \) , la série converge absolument donc converge, sinon \( 0 < \alpha \leq 1 \) et on note \( p = \left\lbrack {1/\alpha }\right\rbrack - 1 \; \left( {\lbrack 1/\alpha \rbrack }\right. \) est la partie entière de \( 1/\alpha ) \) , de sorte que \( \left( {p + 1}\right) \alpha \leq 1 < \left( {p + 2}\right) \alpha \) . On écrit

> If \( \alpha > 1 \) , the series converges absolutely and therefore converges, otherwise \( 0 < \alpha \leq 1 \) and we denote \( p = \left\lbrack {1/\alpha }\right\rbrack - 1 \; \left( {\lbrack 1/\alpha \rbrack }\right. \) as the integer part of \( 1/\alpha ) \) , such that \( \left( {p + 1}\right) \alpha \leq 1 < \left( {p + 2}\right) \alpha \) . We write

\[
{u}_{n} = \frac{{e}^{ni\theta }}{{n}^{\alpha }}\frac{1}{1 + {e}^{ni\varphi }{n}^{-\alpha }} = {u}_{n,0} + {u}_{n,1} + \cdots  + {u}_{n, p} + O\left( \frac{1}{{n}^{\left( {p + 2}\right) \alpha }}\right) ,\;{u}_{n, k} = {\left( -1\right) }^{k}\frac{{e}^{{ni}\left( {\theta  + {k\varphi }}\right) }}{{n}^{\left( {k + 1}\right) \alpha }}.
\]

Comme \( \left( {p + 2}\right) \alpha > 1 \) , ceci montre que

> Since \( \left( {p + 2}\right) \alpha > 1 \) , this shows that

\[
\text{ la série }\mathop{\sum }\limits_{n}{u}_{n}\text{ a même nature que la série }\mathop{\sum }\limits_{n}\left( {{u}_{n,0} + \cdots  + {u}_{n, p}}\right) \text{ . }
\]

(*)

> Deux cas se présentent :

Two cases arise:

> (i) Si pour tout \( k \in \{ 0,1,\ldots , p\} ,\theta + {k\varphi } \notin {2\pi }\mathbb{Z} \) , alors chacune des séries \( \mathop{\sum }\limits_{n}{u}_{n, k} \) converge (pour \( 0 \leq k \leq p \) ) d’après la règle d’Abel, donc \( \sum {u}_{n} \) converge d’après le principe (*).

(i) If for all \( k \in \{ 0,1,\ldots , p\} ,\theta + {k\varphi } \notin {2\pi }\mathbb{Z} \) , then each of the series \( \mathop{\sum }\limits_{n}{u}_{n, k} \) converges (for \( 0 \leq k \leq p \) ) according to Abel's test, therefore \( \sum {u}_{n} \) converges according to the principle (*).

> (ii) Sinon, il existe un plus petit entier \( k \) tel que \( \theta + {k\varphi } \in {2\pi }\mathbb{Z} \) . Comme \( \theta + \ell \varphi \notin {2\pi }\mathbb{Z} \) pour \( 0 \leq \ell < k \) , less séries \( \mathop{\sum }\limits_{n}{u}_{n,\ell }\left( {0 \leq \ell < k}\right) \) convergent, et on en déduit d’après (*) que \( \mathop{\sum }\limits_{n}{u}_{n} \) est de même nature que \( \mathop{\sum }\limits_{n}\left( {{u}_{n, k} + \cdots + {u}_{n, p}}\right) \) . Notons \( {v}_{n} = {u}_{n, k} + \cdots + {u}_{n, p} \) . On a

(ii) Otherwise, there exists a smallest integer \( k \) such that \( \theta + {k\varphi } \in {2\pi }\mathbb{Z} \) . Since \( \theta + \ell \varphi \notin {2\pi }\mathbb{Z} \) for \( 0 \leq \ell < k \) , the series \( \mathop{\sum }\limits_{n}{u}_{n,\ell }\left( {0 \leq \ell < k}\right) \) converge, and we deduce from (*) that \( \mathop{\sum }\limits_{n}{u}_{n} \) is of the same nature as \( \mathop{\sum }\limits_{n}\left( {{u}_{n, k} + \cdots + {u}_{n, p}}\right) \) . Let \( {v}_{n} = {u}_{n, k} + \cdots + {u}_{n, p} \) . We have

\[
{u}_{n, k} = \frac{{\left( -1\right) }^{k}}{{n}^{\left( {k + 1}\right) \alpha }}\text{ et }{u}_{n, k + 1} + \cdots  + {u}_{n, p} = O\left( \frac{1}{{n}^{\left( {k + 2}\right) \alpha }}\right) ,
\]

donc \( {v}_{n} \sim {\left( -1\right) }^{k}/{n}^{\left( {k + 1}\right) \alpha } \) . A ce stade, on ne peut conclure directement que \( \sum {v}_{n} \) diverge car \( {v}_{n} \) est un nombre complexe. Pour s’en tirer, on va considérer la partie réelle de \( {v}_{n} \) , en posant \( {x}_{n} = \Re \left( {v}_{n}\right) \) . Elle vérifie aussi \( {x}_{n} \sim {\left( -1\right) }^{k}/{n}^{\left( {k + 1}\right) \alpha } \) et comme \( {x}_{n} \) est de signe constant et que \( \left( {k + 1}\right) \alpha \leq 1,\sum {x}_{n} \) diverge. Donc \( \sum {v}_{n} \) diverge (une suite complexe converge si et seulement si ses parties réelles et imaginaires convergent), donc \( \sum {u}_{n} \) diverge.

> thus \( {v}_{n} \sim {\left( -1\right) }^{k}/{n}^{\left( {k + 1}\right) \alpha } \) . At this stage, we cannot directly conclude that \( \sum {v}_{n} \) diverges because \( {v}_{n} \) is a complex number. To get around this, we will consider the real part of \( {v}_{n} \) , by setting \( {x}_{n} = \Re \left( {v}_{n}\right) \) . It also satisfies \( {x}_{n} \sim {\left( -1\right) }^{k}/{n}^{\left( {k + 1}\right) \alpha } \) and since \( {x}_{n} \) is of constant sign and \( \left( {k + 1}\right) \alpha \leq 1,\sum {x}_{n} \) diverges. Therefore \( \sum {v}_{n} \) diverges (a complex sequence converges if and only if its real and imaginary parts converge), so \( \sum {u}_{n} \) diverges.

Finalement, nous avons montré que \( \sum {u}_{n} \) converge si et seulement si

> Finally, we have shown that \( \sum {u}_{n} \) converges if and only if

\[
\left( {\alpha  > 1}\right) \;\text{ ou }\;\left( {0 < \alpha  \leq  1\text{ et }\forall k \in  \mathbb{N}, k \leq  \left\lbrack  \frac{1}{\alpha }\right\rbrack   - 1,\;\theta  + {k\varphi } \notin  {2\pi }\mathbb{Z}}\right) .
\]

EXERCICE 8. Soit \( \sum {u}_{n} \) une série à termes positifs dont le terme général tend vers 0. On note \( {S}_{n} \) la somme partielle d’indice \( n \) de cette série. Montrer que si la suite \( \left( {{S}_{n} - n{u}_{n}}\right) \) est bornée, alors \( \sum {u}_{n} \) converge. La réciproque est-elle vraie ?

> EXERCISE 8. Let \( \sum {u}_{n} \) be a series with positive terms whose general term tends to 0. Let \( {S}_{n} \) be the partial sum of index \( n \) of this series. Show that if the sequence \( \left( {{S}_{n} - n{u}_{n}}\right) \) is bounded, then \( \sum {u}_{n} \) converges. Is the converse true?

Solution. Raisonnons par l’absurde en supposant la série \( \sum {u}_{n} \) divergente. Alors \( {S}_{n} \rightarrow + \infty \) donc l’estimation \( {S}_{n} - n{u}_{n} = O\left( 1\right) \) entraîne

> Solution. Let us reason by contradiction by assuming the series \( \sum {u}_{n} \) is divergent. Then \( {S}_{n} \rightarrow + \infty \) so the estimate \( {S}_{n} - n{u}_{n} = O\left( 1\right) \) leads to

\[
n{u}_{n} = {S}_{n} + O\left( 1\right) \text{ donc }\frac{{u}_{n}}{{S}_{n}} = \frac{1}{n} + O\left( \frac{1}{n{S}_{n}}\right)  \sim  \frac{1}{n}.
\]

(*)

> à ce stade, nous allons utiliser une technique classique : on écrit

at this stage, we will use a classic technique: we write

\[
\log \left( \frac{{S}_{n}}{{S}_{n - 1}}\right)  =  - \log \left( {1 - \frac{{u}_{n}}{{S}_{n}}}\right)  \sim  \frac{{u}_{n}}{{S}_{n}} \sim  \frac{1}{n}.
\]

On en déduit que la série \( \sum \log \left( {{S}_{n}/{S}_{n - 1}}\right) \) diverge, et on peut sommer terme à terme ces équivalents (voir le théorème 5 page 210), ce qui donne

> We deduce that the series \( \sum \log \left( {{S}_{n}/{S}_{n - 1}}\right) \) diverges, and we can sum these equivalents term by term (see theorem 5 page 210), which gives

\[
\log {S}_{n} - \log {S}_{0} = \mathop{\sum }\limits_{{k = 1}}^{n}\log \left( \frac{{S}_{k}}{{S}_{k - 1}}\right)  \sim  \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{k} \sim  \log n
\]

(ce dernier équivalent est hyper-classique, voir par exemple page 211), donc \( \log {S}_{n} \sim \log n \) . En particulier, il existe \( N \in \mathbb{N} \) tel que \( \log \left( {S}_{n}\right) \geq \left( {\log n}\right) /2 \) pour tout \( n \geq N \) , et donc \( {S}_{n} \geq \sqrt{n} \) pour tout \( n \geq N \) . On injecte cette minoration dans (*), ce qui donne

> (this last equivalent is highly classic, see for example page 211), so \( \log {S}_{n} \sim \log n \) . In particular, there exists \( N \in \mathbb{N} \) such that \( \log \left( {S}_{n}\right) \geq \left( {\log n}\right) /2 \) for all \( n \geq N \) , and thus \( {S}_{n} \geq \sqrt{n} \) for all \( n \geq N \) . We inject this lower bound into (*), which gives

\[
\frac{{u}_{n}}{{S}_{n}} = \frac{1}{n} + O\left( \frac{1}{n{S}_{n}}\right)  = \frac{1}{n} + O\left( \frac{1}{{n}^{3/2}}\right) .
\]

Nous possédons maintenant plus d'information que dans (*). Nous allons en tirer parti pour calculer un développement asymptotique à deux termes de \( \log {S}_{n} \) . On a

> We now possess more information than in (*). We will take advantage of this to calculate a two-term asymptotic expansion of \( \log {S}_{n} \) . We have

\[
\frac{1}{n} + \log \left( \frac{{S}_{n - 1}}{{S}_{n}}\right)  = \frac{1}{n} + \log \left( {1 - \frac{{u}_{n}}{{S}_{n}}}\right)  = \frac{1}{n} - \frac{{u}_{n}}{{S}_{n}} + O\left( \frac{{u}_{n}^{2}}{{S}_{n}^{2}}\right)  = O\left( \frac{1}{{n}^{3/2}}\right) ,
\]

donc la série \( \sum 1/n + \log \left( {{S}_{n - 1}/{S}_{n}}\right) \) converge. En notant \( \lambda \) sa somme, on a

> therefore the series \( \sum 1/n + \log \left( {{S}_{n - 1}/{S}_{n}}\right) \) converges. Denoting its sum by \( \lambda \), we have

\[
1 + \frac{1}{2} + \cdots  + \frac{1}{n} + \log {S}_{0} - \log {S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {\frac{1}{k} + \log \left( \frac{{S}_{k - 1}}{{S}_{k}}\right) }\right)  = \lambda  + o\left( 1\right) ,
\]

donc

> therefore

\[
\log {S}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} + \log {S}_{0} - \lambda  + o\left( 1\right)  = \log n + \gamma  + \log {S}_{0} - \lambda  + o\left( 1\right) ,
\]

où \( \gamma \) désigne la constante d’Euler. En passant aux exponentielles, on en déduit

> where \( \gamma \) denotes the Euler constant. Taking the exponentials, we deduce

\[
{S}_{n} \sim  {Kn},\;K = {e}^{\gamma  + \log {S}_{0} - \lambda } > 0.
\]

Comme \( {u}_{n} \sim {S}_{n}/n \) d’après (*), on en déduit que la suite \( \left( {u}_{n}\right) \) converge vers la constante non nulle \( K \) , ce qui est contraire aux hypothèses. La série \( \sum {u}_{n} \) converge donc.

> Since \( {u}_{n} \sim {S}_{n}/n \) according to (*), we deduce that the sequence \( \left( {u}_{n}\right) \) converges to the non-zero constant \( K \), which contradicts the hypotheses. The series \( \sum {u}_{n} \) therefore converges.

La réciproque est fausse. Par exemple, la suite \( \left( {u}_{n}\right) \) définie par

> The converse is false. For example, the sequence \( \left( {u}_{n}\right) \) defined by

\[
{u}_{n} = \left\{  \begin{array}{lll} 1/{n}^{2} & \text{ si } & n \notin  \left\{  {{2}^{k}, k \in  \mathbb{N}}\right\}  \\  1/\sqrt{n} & \text{ si } & n \in  \left\{  {{2}^{k}, k \in  \mathbb{N}}\right\}   \end{array}\right.
\]

est convergente mais \( \left( {{S}_{n} - n{u}_{n}}\right) \) n’est pas bornée.

> is convergent but \( \left( {{S}_{n} - n{u}_{n}}\right) \) is not bounded.

EXERCICE 9. Soit \( \sum {u}_{n} \) une série à termes positifs. Comparer la nature des séries \( \sum {u}_{n} \) et \( \sum {v}_{n} \) , où

> EXERCISE 9. Let \( \sum {u}_{n} \) be a series with positive terms. Compare the nature of the series \( \sum {u}_{n} \) and \( \sum {v}_{n} \), where

\[
\forall n \in  {\mathbb{N}}^{ * },\;{v}_{n} = \frac{1}{1 + {n}^{2}{u}_{n}}.
\]

Solution. Si \( \sum {u}_{n} \) diverge, on ne peut rien conclure quant à la nature de \( \sum {v}_{n} \) . Par exemple

> Solution. If \( \sum {u}_{n} \) diverges, we cannot conclude anything regarding the nature of \( \sum {v}_{n} \). For example

- si \( {u}_{n} = 1/n \) pour tout \( n \in  {\mathbb{N}}^{ * },\sum {u}_{n} \) diverge et \( {v}_{n} = 1/\left( {1 + n}\right)  \sim  1/n \) , donc \( \sum {v}_{n} \) diverge ;

> - if \( {u}_{n} = 1/n \) for all \( n \in  {\mathbb{N}}^{ * },\sum {u}_{n} \) diverges and \( {v}_{n} = 1/\left( {1 + n}\right)  \sim  1/n \), then \( \sum {v}_{n} \) diverges;

- si \( {u}_{n} = 1 \) pour tout \( n \in  {\mathbb{N}}^{ * },\sum {u}_{n} \) diverge et \( {v}_{n} = 1/\left( {1 + {n}^{2}}\right)  \sim  1/{n}^{2} \) , donc \( \sum {v}_{n} \) converge.

> - if \( {u}_{n} = 1 \) for all \( n \in  {\mathbb{N}}^{ * },\sum {u}_{n} \) diverges and \( {v}_{n} = 1/\left( {1 + {n}^{2}}\right)  \sim  1/{n}^{2} \), then \( \sum {v}_{n} \) converges.

Si \( \sum {u}_{n} \) converge, nous montrons que \( \sum {v}_{n} \) diverge. Deux cas se présentent :

> If \( \sum {u}_{n} \) converges, we show that \( \sum {v}_{n} \) diverges. Two cases arise:

(i) si \( \left( {{n}^{2}{u}_{n}}\right) \) ne tend vers pas \( + \infty \) , alors \( \left( {v}_{n}\right) \) ne tend pas vers 0 donc \( \sum {v}_{n} \) diverge ;

> (i) if \( \left( {{n}^{2}{u}_{n}}\right) \) does not tend to \( + \infty \), then \( \left( {v}_{n}\right) \) does not tend to 0, so \( \sum {v}_{n} \) diverges;

(ii) si \( \left( {{n}^{2}{u}_{n}}\right) \) tend vers \( + \infty \) , alors \( {v}_{n} \sim 1/\left( {{n}^{2}{u}_{n}}\right) \) , donc \( {\left( {u}_{n}{v}_{n}\right) }^{1/2} \sim 1/n \) , et donc \( \sum {\left( {u}_{n}{v}_{n}\right) }^{1/2} \) diverge. L'inégalité de Schwarz,

> (ii) if \( \left( {{n}^{2}{u}_{n}}\right) \) tends to \( + \infty \), then \( {v}_{n} \sim 1/\left( {{n}^{2}{u}_{n}}\right) \), so \( {\left( {u}_{n}{v}_{n}\right) }^{1/2} \sim 1/n \), and therefore \( \sum {\left( {u}_{n}{v}_{n}\right) }^{1/2} \) diverges. The Schwarz inequality,

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\left( \mathop{\sum }\limits_{{k = 1}}^{n}\sqrt{{u}_{n}{v}_{n}}\right) }^{2} \leq  \left( {\mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k}}\right) \left( {\mathop{\sum }\limits_{{k = 1}}^{n}{v}_{k}}\right) ,
\]

montre alors que les sommes partielles de \( \sum {v}_{n} \) divergent vers \( + \infty \) , donc \( \sum {v}_{n} \) diverge.

> then shows that the partial sums of \( \sum {v}_{n} \) diverge to \( + \infty \), so \( \sum {v}_{n} \) diverges.

EXERCICE 10. Pour tout \( k \in \mathbb{N} \) on note \( {\log }^{\left( k\right) } = \log \circ \cdots \circ \log \) le logarithme itéré \( k \) fois, et on note \( {n}_{k} \in \mathbb{N} \) un entier tel que \( {\log }^{\left( k\right) }n \) est défini et \( \geq 1 \) pour tout \( n \geq {n}_{k} \) . a) Soit \( k \in {\mathbb{N}}^{ * } \) et \( \beta > 0 \) . Discuter de la convergence de la série

> EXERCISE 10. For all \( k \in \mathbb{N} \), we denote by \( {\log }^{\left( k\right) } = \log \circ \cdots \circ \log \) the iterated logarithm \( k \) times, and we denote by \( {n}_{k} \in \mathbb{N} \) an integer such that \( {\log }^{\left( k\right) }n \) is defined and \( \geq 1 \) for all \( n \geq {n}_{k} \). a) Let \( k \in {\mathbb{N}}^{ * } \) and \( \beta > 0 \). Discuss the convergence of the series

\[
\mathop{\sum }\limits_{{n \geq  {n}_{k}}}\frac{1}{n \times  \log n \times  \cdots  \times  {\log }^{\left( k - 1\right) }n \times  {\left( {\log }^{\left( k\right) }n\right) }^{\beta }}
\]

en fonction de \( \beta \) , et donner un équivalent de ses sommes partielles lorsqu’elle diverge.

> as a function of \( \beta \), and provide an equivalent for its partial sums when it diverges.

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {k}_{n} \) le plus grand entier \( k \) tel que \( {\log }^{\left( k\right) }n \geq 1 \) . Donner la nature de la série \( \mathop{\sum }\limits_{{n \geq 1}}{u}_{n} \) où

> b) For any \( n \in {\mathbb{N}}^{ * } \), let \( {k}_{n} \) be the largest integer \( k \) such that \( {\log }^{\left( k\right) }n \geq 1 \). Determine the nature of the series \( \mathop{\sum }\limits_{{n \geq 1}}{u}_{n} \) where

\[
{u}_{n} = \frac{1}{n \times  \log n \times  \log \log n \times  \cdots  \times  {\log }^{\left( {k}_{n}\right) }n}
\]

et déterminer un équivalent des sommes partielles de cette dernière si elle diverge.

> and determine an equivalent for the partial sums of the latter if it diverges.

Solution. a) Il suffit d'appliquer la proposition 3 sur la comparaison série-intégrale, page 212, à la fonction décroissante \( {f}_{k,\beta } : \left\lbrack {{n}_{k}, + \infty \left\lbrack { \rightarrow \mathbb{R},\;x \mapsto 1/\left( {x \times \cdots \times {\log }^{\left( k - 1\right) }x \times {\left( {\log }^{\left( k\right) }x\right) }^{\beta }}\right) }\right. }\right. \) . Traitons d’abord le cas \( \beta = 1 \) . On montre facilement par récurrence sur \( k \) qu’une primitive de \( {f}_{k,1} \) est \( {\log }^{\left( k + 1\right) } \) , on en déduit que les sommes partielles de la série divergent car elles vérifient

> Solution. a) It suffices to apply proposition 3 on the series-integral comparison, page 212, to the decreasing function \( {f}_{k,\beta } : \left\lbrack {{n}_{k}, + \infty \left\lbrack { \rightarrow \mathbb{R},\;x \mapsto 1/\left( {x \times \cdots \times {\log }^{\left( k - 1\right) }x \times {\left( {\log }^{\left( k\right) }x\right) }^{\beta }}\right) }\right. }\right. \). Let us first treat the case \( \beta = 1 \). We easily show by induction on \( k \) that an antiderivative of \( {f}_{k,1} \) is \( {\log }^{\left( k + 1\right) } \), from which we deduce that the partial sums of the series diverge because they satisfy

\[
\mathop{\sum }\limits_{{p = {n}_{k}}}^{n}{f}_{k,1}\left( p\right)  = {\int }_{{n}_{k}}^{n}{f}_{k,1}\left( x\right) {dx} + O\left( 1\right)  = {\log }^{\left( k + 1\right) }n + O\left( 1\right) .
\]

Lorsque \( \beta \neq 1 \) , une primitive de la fonction \( {f}_{k,\beta } \) est donnée par \( {\left( 1 - \beta \right) }^{-1}{\left( {\log }^{\left( k\right) }x\right) }^{1 - \beta } \) , donc

> When \( \beta \neq 1 \), an antiderivative of the function \( {f}_{k,\beta } \) is given by \( {\left( 1 - \beta \right) }^{-1}{\left( {\log }^{\left( k\right) }x\right) }^{1 - \beta } \), therefore

\[
\mathop{\sum }\limits_{{p = {n}_{k}}}^{n}{f}_{k,\beta }\left( p\right)  = {\int }_{{n}_{k}}^{n}{f}_{k,\beta }\left( x\right) {dx} + O\left( 1\right)  = \frac{{\left( {\log }^{\left( k\right) }n\right) }^{1 - \beta }}{1 - \beta } + O\left( 1\right) .
\]

On en déduit que si \( \beta < 1 \) , la série diverge et ses sommes partielles sont équivalentes à \( {\left( {\log }^{\left( k\right) }n\right) }^{1 - \beta }/\left( {1 - \beta }\right) \) . Si \( \beta > 1 \) l’estimation précédente montre que les sommes partielles sont bornées, et comme la série est à termes positifs elle converge (notons que dans ce cas, on mon-trerait facilement que les restes de la série sont équivalents à \( {\left( \beta - 1\right) }^{-1}1/{\left( {\log }^{\left( k\right) }n\right) }^{\beta - 1} \) ).

> We deduce that if \( \beta < 1 \), the series diverges and its partial sums are equivalent to \( {\left( {\log }^{\left( k\right) }n\right) }^{1 - \beta }/\left( {1 - \beta }\right) \). If \( \beta > 1 \), the previous estimate shows that the partial sums are bounded, and since the series has positive terms, it converges (note that in this case, one could easily show that the remainders of the series are equivalent to \( {\left( \beta - 1\right) }^{-1}1/{\left( {\log }^{\left( k\right) }n\right) }^{\beta - 1} \)).

b) Définissons la suite \( \left( {e}_{k}\right) \) par \( {e}_{0} = 1 \) et \( {e}_{k + 1} = \exp \left( {e}_{k}\right) \) . Pour tout \( k \in \mathbb{N} \) , on considère la fonction continue décroissante \( {g}_{k} : \left\lbrack {{e}_{k},{e}_{k + 1}}\right\rbrack \rightarrow \mathbb{R},\;x \mapsto 1/\left( {x \times \log x \times \cdots \times {\log }^{\left( k\right) }x}\right) \) , puis on considère la fonction \( g : \lbrack 1, + \infty \lbrack \rightarrow \mathbb{R} \) définie par \( g\left( x\right) = {g}_{k}\left( x\right) \) sur chaque intervalle \( x \in \left\lbrack {{e}_{k},{e}_{k + 1}\left\lbrack \right. }\right. \) . L’identité log \( {}^{\left( k\right) }\left( {e}_{k}\right) = 1 \) entraîne \( {g}_{k - 1}\left( {e}_{k}\right) = {g}_{k}\left( {e}_{k}\right) \) donc \( g \) est continue, et comme chaque \( {g}_{k} \) est décroissante on en déduit que \( g \) est également décroissante. Par ailleurs, on a \( n \in \left\lbrack {{e}_{{k}_{n}},{e}_{{k}_{n} + 1}\left\lbrack \right. }\right. \) donc \( {u}_{n} = g\left( n\right) \) . On peut donc appliquer le résultat la comparaison série-intégrale, qui entraîne

> b) Let us define the sequence \( \left( {e}_{k}\right) \) by \( {e}_{0} = 1 \) and \( {e}_{k + 1} = \exp \left( {e}_{k}\right) \) . For all \( k \in \mathbb{N} \) , we consider the continuous decreasing function \( {g}_{k} : \left\lbrack {{e}_{k},{e}_{k + 1}}\right\rbrack \rightarrow \mathbb{R},\;x \mapsto 1/\left( {x \times \log x \times \cdots \times {\log }^{\left( k\right) }x}\right) \) , then we consider the function \( g : \lbrack 1, + \infty \lbrack \rightarrow \mathbb{R} \) defined by \( g\left( x\right) = {g}_{k}\left( x\right) \) on each interval \( x \in \left\lbrack {{e}_{k},{e}_{k + 1}\left\lbrack \right. }\right. \) . The identity log \( {}^{\left( k\right) }\left( {e}_{k}\right) = 1 \) implies \( {g}_{k - 1}\left( {e}_{k}\right) = {g}_{k}\left( {e}_{k}\right) \) so \( g \) is continuous, and since each \( {g}_{k} \) is decreasing, we deduce that \( g \) is also decreasing. Furthermore, we have \( n \in \left\lbrack {{e}_{{k}_{n}},{e}_{{k}_{n} + 1}\left\lbrack \right. }\right. \) so \( {u}_{n} = g\left( n\right) \) . We can therefore apply the integral test for convergence, which implies

\[
\mathop{\sum }\limits_{{p = 1}}^{n}{u}_{p} = {\int }_{1}^{n}g\left( x\right) {dx} + O\left( 1\right)  = \mathop{\sum }\limits_{{j = 0}}^{{{k}_{n} - 1}}{I}_{j} + {R}_{n} + O\left( 1\right)
\]

avec

> with

\[
{I}_{j} = {\int }_{{e}_{j}}^{{e}_{j + 1}}{g}_{j}\left( x\right) {dx},\;{R}_{n} = {\int }_{{e}_{{k}_{n}}}^{n}{g}_{{k}_{n}}\left( x\right) {dx}.
\]

Nous avons vu plus haut qu’une primitive de \( {g}_{j} \) est \( {\log }^{\left( j + 1\right) } \) , donc \( {I}_{j} = {\log }^{\left( j + 1\right) }{e}_{j + 1} - {\log }^{\left( j + 1\right) }{e}_{j} \) , et par récurrence sur \( j \) on en déduit facilemet \( {I}_{j} = 1 \) (on peut aussi procéder à partir du changement de variable \( t = {e}^{x} \) dans l’intégrale \( {I}_{j} \) qui montre que \( {I}_{j} = {I}_{j - 1} \) ). On a \( 0 \leq {R}_{n} \leq \; {I}_{{k}_{n}} = 1 \) , on en déduit donc \( \mathop{\sum }\limits_{{p = 1}}^{n}{u}_{p} = {k}_{n} + O\left( 1\right) \) . Ainsi la série diverge et les sommes partielles sont equivalentes à \( {k}_{n} \) .

> We saw above that an antiderivative of \( {g}_{j} \) is \( {\log }^{\left( j + 1\right) } \) , so \( {I}_{j} = {\log }^{\left( j + 1\right) }{e}_{j + 1} - {\log }^{\left( j + 1\right) }{e}_{j} \) , and by induction on \( j \) we easily deduce \( {I}_{j} = 1 \) (one can also proceed from the change of variable \( t = {e}^{x} \) in the integral \( {I}_{j} \) which shows that \( {I}_{j} = {I}_{j - 1} \) ). We have \( 0 \leq {R}_{n} \leq \; {I}_{{k}_{n}} = 1 \) , so we deduce \( \mathop{\sum }\limits_{{p = 1}}^{n}{u}_{p} = {k}_{n} + O\left( 1\right) \) . Thus the series diverges and the partial sums are equivalent to \( {k}_{n} \) .

EXERCICE 11. a) Soit \( \left( {u}_{n}\right) \) la suite définie par \( {u}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\log k/k \) . Montrer l’existence d’une constante \( C \in \mathbb{R} \) telle que \( {u}_{n} = \left( {{\log }^{2}n}\right) /2 + C + o\left( 1\right) \) .

> EXERCISE 11. a) Let \( \left( {u}_{n}\right) \) be the sequence defined by \( {u}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\log k/k \) . Show the existence of a constant \( C \in \mathbb{R} \) such that \( {u}_{n} = \left( {{\log }^{2}n}\right) /2 + C + o\left( 1\right) \) .

b) Démontrer la convergence de la série \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) et utiliser le résultat de la question précédente pour calculer la somme de cette série.

> b) Prove the convergence of the series \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) and use the result of the previous question to calculate the sum of this series.

Solution. a) Le plus simple est d'appliquer la proposition 3 sur la comparaison série-intégrale, page 212. Ici on a \( {u}_{n} = f\left( 0\right) + f\left( 1\right) + \cdots + f\left( {n - 1}\right) \) avec \( f\left( x\right) = \log \left( {x + 1}\right) /\left( {x + 1}\right) \) . La fonction \( f \) est dérivable et \( {f}^{\prime }\left( x\right) = \left( {1 - \log \left( {x + 1}\right) }\right) /{\left( x + 1\right) }^{2} \) donc \( f \) est décroissante à partir d’un certain rang. Comme indiqué dans la remarque 4 page 212, le résultat de la proposition 3 reste vérifié, on conclut que \( {u}_{n} - {\int }_{0}^{n}f\left( x\right) {dx} = {u}_{n} - \frac{1}{2}{\log }^{2}\left( {n + 1}\right) = {u}_{n} - \frac{1}{2}{\log }^{2}n + o\left( 1\right) \) converge, d’où le résultat.

> Solution. a) The simplest approach is to apply Proposition 3 on the series-integral comparison, page 212. Here we have \( {u}_{n} = f\left( 0\right) + f\left( 1\right) + \cdots + f\left( {n - 1}\right) \) with \( f\left( x\right) = \log \left( {x + 1}\right) /\left( {x + 1}\right) \) . The function \( f \) is differentiable and \( {f}^{\prime }\left( x\right) = \left( {1 - \log \left( {x + 1}\right) }\right) /{\left( x + 1\right) }^{2} \) , so \( f \) is decreasing from a certain rank. As indicated in Remark 4 on page 212, the result of Proposition 3 remains valid; we conclude that \( {u}_{n} - {\int }_{0}^{n}f\left( x\right) {dx} = {u}_{n} - \frac{1}{2}{\log }^{2}\left( {n + 1}\right) = {u}_{n} - \frac{1}{2}{\log }^{2}n + o\left( 1\right) \) converges, hence the result.

On aurait pu aussi procéder comme on l'a fait à la page 211 pour les sommes harmoniques : pour montrer la convergence de \( {v}_{n} = {u}_{n} - \left( {{\log }^{2}n}\right) /2 \) , on calcule l’estimation \( {v}_{n} - {v}_{n - 1} = \; O\left( {\log n/{n}^{2}}\right) \) , entraînant la convergence de \( \sum \left( {{v}_{n} - {v}_{n - 1}}\right) \) donc celle de la suite \( \left( {v}_{n}\right) \) .

> We could also have proceeded as we did on page 211 for harmonic sums: to show the convergence of \( {v}_{n} = {u}_{n} - \left( {{\log }^{2}n}\right) /2 \) , we calculate the estimate \( {v}_{n} - {v}_{n - 1} = \; O\left( {\log n/{n}^{2}}\right) \) , leading to the convergence of \( \sum \left( {{v}_{n} - {v}_{n - 1}}\right) \) and thus that of the sequence \( \left( {v}_{n}\right) \) .

b) Notons \( {a}_{n} = \mathop{\sum }\limits_{{k = 1}}^{{2n}}{\left( -1\right) }^{k}\log k/k \) . Pour montrer la convergence de \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) il suffit de montrer celle de \( \left( {a}_{n}\right) \) car le terme général de la série converge vers 0, et de plus la somme de la série égale la limite de \( \left( {a}_{n}\right) \) . On récrit \( {a}_{n} \) sous la forme

> b) Let \( {a}_{n} = \mathop{\sum }\limits_{{k = 1}}^{{2n}}{\left( -1\right) }^{k}\log k/k \) . To show the convergence of \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) , it suffices to show that of \( \left( {a}_{n}\right) \) because the general term of the series converges to 0, and furthermore, the sum of the series equals the limit of \( \left( {a}_{n}\right) \) . We rewrite \( {a}_{n} \) in the form

\[
{a}_{n} = 2\mathop{\sum }\limits_{{k = 1}}^{n}\frac{\log {2k}}{2k} - \mathop{\sum }\limits_{{k = 1}}^{{2n}}\frac{\log k}{k} = {H}_{n}\log 2 + {u}_{n} - {u}_{2n},\;\text{ avec }\;{H}_{n} = 1 + \cdots  + \frac{1}{n}.
\]

En utilisant l’asymptotique des sommes harmoniques \( {H}_{n} = \log n + \gamma + o\left( 1\right) \) (où \( \gamma \) est la constante d’Euler, voir la page 211), et celle de \( \left( {u}_{n}\right) \) , on en déduit

> Using the asymptotics of harmonic sums \( {H}_{n} = \log n + \gamma + o\left( 1\right) \) (where \( \gamma \) is the Euler constant, see page 211), and that of \( \left( {u}_{n}\right) \) , we deduce

\[
{a}_{n} = \log 2\log n + \gamma \log 2 + \frac{{\log }^{2}n - {\log }^{2}\left( {2n}\right) }{2} + o\left( 1\right)  = \gamma \log 2 - \frac{{\log }^{2}2}{2} + o\left( 1\right) .
\]

La série \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) converge donc et sa somme est égale à \( \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) .

> The series \( \mathop{\sum }\limits_{{n \geq 1}}{\left( -1\right) }^{n}\log n/n \) therefore converges and its sum is equal to \( \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) .

\( \rightarrow \) EXERCICE 12. 1/ Soit \( f : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{C} \) une application de classe \( {\mathcal{C}}^{1} \) telle que l’intégrale \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) converge.

> \( \rightarrow \) EXERCISE 12. 1/ Let \( f : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{C} \) be a \( {\mathcal{C}}^{1} \) class mapping such that the integral \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) converges.

a) Montrer que la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}f\left( n\right) \) a même nature que la suite \( {\left( {\int }_{1}^{n}f\left( t\right) dt\right) }_{n \in \mathbb{N}} \) .

> a) Show that the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}f\left( n\right) \) has the same nature as the sequence \( {\left( {\int }_{1}^{n}f\left( t\right) dt\right) }_{n \in \mathbb{N}} \) .

b) (Application.) Lorsque \( \alpha > 1/2 \) , donner la nature de la série

> b) (Application.) When \( \alpha > 1/2 \) , determine the nature of the series

\[
\mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\frac{{e}^{i\sqrt{n}}}{{n}^{\alpha }}.
\]

(*)

> 2 / En généralisant la technique précédente, donner la nature de la série (*) lorsque 0 < \( \alpha \leq 1/2 \) .

2 / By generalizing the previous technique, determine the nature of the series (*) when 0 < \( \alpha \leq 1/2 \) .

> Solution. 1/ a) Nous allons montrer que la suite \( \left( {s}_{n}\right) \) définie par

Solution. 1/ a) We will show that the sequence \( \left( {s}_{n}\right) \) defined by

\[
\forall n \in  {\mathbb{N}}^{ * },\;{s}_{n} = {\int }_{1}^{n + 1}f\left( t\right) {dt} - \mathop{\sum }\limits_{{p = 1}}^{n}f\left( p\right)
\]

est une suite convergente, ce qui montrera le résultat.

> is a convergent sequence, which will prove the result.

Soit \( n \in {\mathbb{N}}^{ * } \) . En appliquant la formule de Taylor avec reste intégral à la fonction \( x \mapsto \; {\int }_{n}^{x}f\left( t\right) {dt} \) à l’ordre 1, on a

> Let \( n \in {\mathbb{N}}^{ * } \) . By applying Taylor's formula with integral remainder to the function \( x \mapsto \; {\int }_{n}^{x}f\left( t\right) {dt} \) at order 1, we have

\[
{\int }_{n}^{n + 1}f\left( t\right) {dt} = f\left( n\right)  + {\int }_{n}^{n + 1}\left( {n + 1 - t}\right) {f}^{\prime }\left( t\right) {dt}\;\text{ donc }\;\left| {f\left( n\right)  - {\int }_{n}^{n + 1}f\left( t\right) {dt}}\right|  \leq  {\int }_{n}^{n + 1}\left| {{f}^{\prime }\left( t\right) }\right| {dt}.
\]

Ainsi, la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {f\left( n\right) - {\int }_{n}^{n + 1}f\left( t\right) {dt}}\right) \) converge absolument donc converge, c’est-à-dire que \( \left( {s}_{n}\right) \) converge, d’où le résultat.

> Thus, the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {f\left( n\right) - {\int }_{n}^{n + 1}f\left( t\right) {dt}}\right) \) converges absolutely and therefore converges, which means that \( \left( {s}_{n}\right) \) converges, hence the result.

b) Nous allons appliquer le résultat précédent à la fonction \( f\left( t\right) = {e}^{i\sqrt{t}}/{t}^{\alpha } \) . On a

> b) We will apply the previous result to the function \( f\left( t\right) = {e}^{i\sqrt{t}}/{t}^{\alpha } \) . We have

\[
\forall t > 0,\;\left| {{f}^{\prime }\left( t\right) }\right|  = \left| {\frac{i{e}^{i\sqrt{t}}}{2{t}^{\alpha  + 1/2}} - \alpha \frac{{e}^{i\sqrt{n}}}{{t}^{1 + \alpha }}}\right|  \leq  \frac{1}{2{t}^{\alpha  + 1/2}} + \frac{\alpha }{{t}^{\alpha  + 1}}
\]

et comme \( \alpha > 1/2 \) , cette expression montre que \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) converge. Ainsi, la série étudiée a même nature que la suite \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) . Nous allons montrer que l’intégrale \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converge, ce qui entraînera la convergence de la série. Le changement de variable \( v = {u}^{2} \) montre que cette dernière intégrale a même nature que \( {\int }_{1}^{+\infty }{e}^{iv}/{v}^{{2\alpha } - 1}{dv} \) , donc convergente car \( {2\alpha } - 1 > 0 \) (voir le début de la remarque 6 page 153).

> and since \( \alpha > 1/2 \) , this expression shows that \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) converges. Thus, the series studied has the same nature as the sequence \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) . We will show that the integral \( {\int }_{1}^{+\infty }f\left( t\right) {dt} \) converges, which will imply the convergence of the series. The change of variable \( v = {u}^{2} \) shows that this latter integral has the same nature as \( {\int }_{1}^{+\infty }{e}^{iv}/{v}^{{2\alpha } - 1}{dv} \) , therefore it is convergent because \( {2\alpha } - 1 > 0 \) (see the beginning of remark 6 on page 153).

2/On pose \( f\left( t\right) = {e}^{i\sqrt{t}}/{t}^{\alpha } \) . Ici, la technique précédente ne peut pas s’appliquer car l’intégrale \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) diverge. On généralise, en appliquant pour tout \( n \in {\mathbb{N}}^{ * } \) à la fonction \( x \mapsto {\int }_{n}^{x}f\left( t\right) {dt} \) la formule de Taylor avec reste intégral à l'ordre 2, ce qui donne

> 2/ Let \( f\left( t\right) = {e}^{i\sqrt{t}}/{t}^{\alpha } \) . Here, the previous technique cannot be applied because the integral \( {\int }_{1}^{+\infty }\left| {{f}^{\prime }\left( t\right) }\right| {dt} \) diverges. We generalize by applying Taylor's formula with integral remainder at order 2 to the function \( x \mapsto {\int }_{n}^{x}f\left( t\right) {dt} \) for all \( n \in {\mathbb{N}}^{ * } \) , which gives

\[
{\int }_{n}^{n + 1}f\left( t\right) {dt} = f\left( n\right)  + \frac{{f}^{\prime }\left( n\right) }{2} + {\int }_{n}^{n + 1}\frac{{\left( n + 1 - t\right) }^{2}}{2}{f}^{\prime \prime }\left( t\right) {dt},
\]

ce qui entraîne

> which implies

\[
\forall n \in  {\mathbb{N}}^{ * },\;\left| {{\int }_{n}^{n + 1}f\left( t\right) {dt} - f\left( n\right)  - \frac{{f}^{\prime }\left( n\right) }{2}}\right|  \leq  {\int }_{n}^{n + 1}\left| {{f}^{\prime \prime }\left( t\right) }\right| {dt}.
\]

(**)

> Ici, on a

Here, we have

\[
\forall t > 0,\;{f}^{\prime \prime }\left( t\right)  =  - \frac{{e}^{i\sqrt{t}}}{4{t}^{\alpha  + 1}} - \left( {\alpha  + \frac{1}{4}}\right) \frac{i{e}^{i\sqrt{t}}}{{t}^{\alpha  + 3/2}} + \alpha \left( {\alpha  + 1}\right) \frac{{e}^{i\sqrt{t}}}{{t}^{\alpha  + 2}} = O\left( \frac{1}{{t}^{\alpha  + 1}}\right) ,
\]

donc l’intégrale \( {\int }_{1}^{+\infty }\left| {{f}^{\prime \prime }\left( t\right) }\right| {dt} \) converge, donc d’après (**) la série \( \sum \left( {{\int }_{n}^{n + 1}f\left( t\right) {dt} - f\left( n\right) - }\right. \; \left. {{f}^{\prime }\left( n\right) /2}\right) \) converge. Or

> therefore the integral \( {\int }_{1}^{+\infty }\left| {{f}^{\prime \prime }\left( t\right) }\right| {dt} \) converges, so according to (**) the series \( \sum \left( {{\int }_{n}^{n + 1}f\left( t\right) {dt} - f\left( n\right) - }\right. \; \left. {{f}^{\prime }\left( n\right) /2}\right) \) converges. However

\[
\forall n \in  {\mathbb{N}}^{ * },\;{f}^{\prime }\left( n\right)  = \frac{i{e}^{i\sqrt{n}}}{2{n}^{\alpha  + 1/2}} - \alpha \frac{{e}^{i\sqrt{n}}}{{n}^{1 + \alpha }},
\]

et en appliquant le résultat de la question précédente, on voit que \( \sum {f}^{\prime }\left( n\right) \) converge. Finalement, la série \( \sum {\int }_{n}^{n + 1}f\left( t\right) {dt} - f\left( n\right) \) converge, en particulier, la suite \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) et la série \( \sum f\left( n\right) \) sont de même nature. En écrivant

> and by applying the result of the previous question, we see that \( \sum {f}^{\prime }\left( n\right) \) converges. Finally, the series \( \sum {\int }_{n}^{n + 1}f\left( t\right) {dt} - f\left( n\right) \) converges; in particular, the sequence \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) and the series \( \sum f\left( n\right) \) are of the same nature. By writing

\[
{\int }_{1}^{n}f\left( t\right) {dt} = {\int }_{1}^{\sqrt{n}}\frac{{e}^{iv}}{{v}^{{2\alpha } - 1}}{dv} = {\left\lbrack  \frac{{e}^{iv}}{i{v}^{{2\alpha } - 1}}\right\rbrack  }_{1}^{\sqrt{n}} - \frac{1 - {2\alpha }}{i}{\int }_{1}^{\sqrt{n}}\frac{{e}^{iv}}{{v}^{2\alpha }}{dv},
\]

on s’aperçoit que \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) diverge car \( \alpha \leq 1/2 \) . Finalement, nous venons de montrer que la série (*) diverge pour \( 0 < \alpha \leq 1/2 \) .

> we notice that \( \left( {{\int }_{1}^{n}f\left( t\right) {dt}}\right) \) diverges because \( \alpha \leq 1/2 \) . Finally, we have just shown that the series (*) diverges for \( 0 < \alpha \leq 1/2 \) .

Remarque. Cette technique de comparaison série-intégrale trouve une généralisation na-turelle avec la formule d'Euler-Maclaurin (voir le sujet d'étude 3 page 321).

> Remark. This series-integral comparison technique finds a natural generalization with the Euler-Maclaurin formula (see study topic 3, page 321).

EXERCICE 13. Soit \( \left( {u}_{n}\right) \) une suite vérifiant

> EXERCISE 13. Let \( \left( {u}_{n}\right) \) be a sequence satisfying

\[
\left. {\left. {{u}_{0} \in  }\right\rbrack  0,\frac{\pi }{2}}\right\rbrack  ,\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = \sin {u}_{n}.
\]

a) Montrer que \( \left( {u}_{n}\right) \) tend vers 0 puis donner un équivalent de \( \left( {u}_{n}\right) \) lorsque \( n \rightarrow + \infty \) . b) Donner un développement asymptotique à deux termes de \( \left( {u}_{n}\right) \) .

> a) Show that \( \left( {u}_{n}\right) \) tends to 0, then provide an equivalent for \( \left( {u}_{n}\right) \) as \( n \rightarrow + \infty \) . b) Provide a two-term asymptotic expansion of \( \left( {u}_{n}\right) \) .

Solution. Il faut avoir fait au moins une fois dans sa vie ce type d'exercice.

> Solution. One must have done this type of exercise at least once in their life.

a) L’intervalle \( \rbrack 0,\pi /2\rbrack \) est stable par la fonction sinus, donc \( {u}_{n} \in \rbrack 0,\pi /2\rbrack \) pour tout \( n \) . De plus, on a \( \sin x < x \) sur cet intervalle, donc la suite \( \left( {u}_{n}\right) \) est strictement décroissante. Par ailleurs, elle est minorée par 0, elle converge donc. Sa limite \( \ell \) vérifie \( \sin \left( \ell \right) = \ell \) , donc \( \ell = 0 \) .

> a) The interval \( \rbrack 0,\pi /2\rbrack \) is stable under the sine function, so \( {u}_{n} \in \rbrack 0,\pi /2\rbrack \) for all \( n \) . Furthermore, we have \( \sin x < x \) on this interval, so the sequence \( \left( {u}_{n}\right) \) is strictly decreasing. Moreover, it is bounded below by 0, so it converges. Its limit \( \ell \) satisfies \( \sin \left( \ell \right) = \ell \) , therefore \( \ell = 0 \) .

Donnons maintenant un équivalent de \( \left( {u}_{n}\right) \) . On utilise pour cela une jolie astuce (bravo si vous l'avez trouvée), en écrivant

> Let us now provide an equivalent for \( \left( {u}_{n}\right) \) . To do this, we use a nice trick (well done if you found it), by writing

\[
\frac{1}{{u}_{n + 1}^{2}} - \frac{1}{{u}_{n}^{2}} = \frac{1}{{\sin }^{2}{u}_{n}} - \frac{1}{{u}_{n}^{2}} = \frac{1}{{\left( {u}_{n} - {u}_{n}^{3}/6 + O\left( {u}_{n}^{4}\right) \right) }^{2}} - \frac{1}{{u}_{n}^{2}}
\]

\[
= \frac{1}{{u}_{n}^{2}}\left( {\frac{1}{1 - {u}_{n}^{2}/3 + O\left( {u}_{n}^{3}\right) } - 1}\right)  = \frac{1}{{u}_{n}^{2}}\left( {\frac{{u}_{n}^{2}}{3} + O\left( {u}_{n}^{3}\right) }\right)  = \frac{1}{3} + O\left( {u}_{n}\right)  \sim  \frac{1}{3}
\]

(on a bien le droit de faire ces développements limités car \( {u}_{n} \rightarrow 0 \) ). Cet équivalent montre que la série \( \sum \left( {1/{u}_{n + 1}^{2} - 1/{u}_{n}^{2}}\right) \) diverge, et en sommant les équivalents, on obtient (on a le droit, voir le théorème 5 page 210)

> (we are indeed allowed to perform these Taylor expansions because \( {u}_{n} \rightarrow 0 \) ). This equivalent shows that the series \( \sum \left( {1/{u}_{n + 1}^{2} - 1/{u}_{n}^{2}}\right) \) diverges, and by summing the equivalents, we obtain (we are allowed to, see theorem 5, page 210)

\[
\frac{1}{{u}_{n}^{2}} - \frac{1}{{u}_{0}^{2}} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {\frac{1}{{u}_{k + 1}^{2}} - \frac{1}{{u}_{k}^{2}}}\right)  \sim  \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{1}{3} = \frac{n}{3},
\]

autrement dit \( 1/{u}_{n}^{2} \sim n/3 \) donc \( {u}_{n} \sim \sqrt{3/n} \) .

> in other words \( 1/{u}_{n}^{2} \sim n/3 \) therefore \( {u}_{n} \sim \sqrt{3/n} \) .

b) On procède comme plus haut, en cherchant cette fois ci un développement asymptotique à deux termes de \( 1/{u}_{n + 1}^{2} - 1/{u}_{n}^{2} \) . On a

> b) We proceed as above, this time looking for a two-term asymptotic expansion of \( 1/{u}_{n + 1}^{2} - 1/{u}_{n}^{2} \) . We have

\[
{u}_{n + 1} = \sin {u}_{n} = {u}_{n} - \frac{{u}_{n}^{3}}{6} + \frac{{u}_{n}^{5}}{120} + o\left( {u}_{n}^{5}\right)  = {u}_{n}\left( {1 - \frac{{u}_{n}^{2}}{6} + \frac{{u}_{n}^{4}}{120} + o\left( {u}_{n}^{4}\right) }\right)
\]

donc

> therefore

\[
\frac{1}{{u}_{n + 1}^{2}} = \frac{1}{{u}_{n}^{2}}\left( {1 + \frac{{u}_{n}^{2}}{3} + \frac{{u}_{n}^{4}}{15} + o\left( {u}_{n}^{4}\right) }\right) \;\text{ d’où }\frac{1}{{u}_{n + 1}^{2}} - \frac{1}{{u}_{n}^{2}} - \frac{1}{3} = \frac{{u}_{n}^{2}}{15} + o\left( {u}_{n}^{2}\right)  \sim  \frac{{u}_{n}^{2}}{15} \sim  \frac{1}{5n}
\]

le dernier équivalent provenant du fait que \( {u}_{n} \sim \sqrt{3/n} \) . Comme précédemment, ces expressions sont les termes généraux de séries qui divergent, et on peut sommer les équivalents, ce qui donne

> the last equivalent coming from the fact that \( {u}_{n} \sim \sqrt{3/n} \) . As before, these expressions are the general terms of series that diverge, and we can sum the equivalents, which gives

\[
\frac{1}{{u}_{n}^{2}} - \frac{1}{{u}_{0}^{2}} - \frac{n}{3} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {\frac{1}{{u}_{k + 1}^{2}} - \frac{1}{{u}_{k}^{2}} - \frac{1}{3}}\right)  \sim  \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\frac{1}{5k} \sim  \frac{\log n}{5},
\]

et finalement

> and finally

\[
{u}_{n}^{2} = {\left( \frac{n}{3} + \frac{\log n}{5} + o\left( \log n\right) \right) }^{-1}\;\text{ d’où }\;{u}_{n} = \sqrt{\frac{3}{n}} - \frac{3\sqrt{3}}{10}\frac{\log n}{n\sqrt{n}} + o\left( \frac{\log n}{n\sqrt{n}}\right) .
\]

Remarque. On peut poursuivre le développement asymptotique en itérant la méthode. - On peut de même donner un équivalent de toute suite récurrente \( \left( {u}_{n}\right) \) qui tend vers 0 et vérifie \( {u}_{n + 1} = f\left( {u}_{n}\right) \) où \( f \) est une fonction vérifiant \( f\left( x\right) = x - A{x}^{\alpha } + o\left( {x}^{\alpha }\right) \) au voisinage de \( 0\left( {A > 0,\alpha > 1}\right) \) , en calculant un équivalent de \( {u}_{n + 1}^{1 - \alpha } - {u}_{n}^{1 - \alpha } \) lorsque \( n \rightarrow \infty \) .

> Remark. The asymptotic expansion can be continued by iterating the method. - Similarly, one can provide an equivalent for any recursive sequence \( \left( {u}_{n}\right) \) that tends to 0 and satisfies \( {u}_{n + 1} = f\left( {u}_{n}\right) \) where \( f \) is a function satisfying \( f\left( x\right) = x - A{x}^{\alpha } + o\left( {x}^{\alpha }\right) \) in the neighborhood of \( 0\left( {A > 0,\alpha > 1}\right) \), by calculating an equivalent of \( {u}_{n + 1}^{1 - \alpha } - {u}_{n}^{1 - \alpha } \) as \( n \rightarrow \infty \).

EXERCICE 14. Soit \( \Theta \) une bijection de \( {\mathbb{N}}^{ * } \) dans \( {\mathbb{N}}^{ * } \) .

> EXERCISE 14. Let \( \Theta \) be a bijection from \( {\mathbb{N}}^{ * } \) to \( {\mathbb{N}}^{ * } \).

1 / a) Montrer que la série \( \sum 1/\left( {{n\Theta }\left( n\right) }\right) \) converge, et donner la majoration la meilleure possible de la somme de cette série par une expression indépendante de \( \Theta \) .

> 1 / a) Show that the series \( \sum 1/\left( {{n\Theta }\left( n\right) }\right) \) converges, and provide the best possible upper bound for the sum of this series using an expression independent of \( \Theta \).

b) Montrer que la série \( \sum \Theta \left( n\right) /{n}^{2} \) diverge et donner la minoration la meilleure possible des sommes partielles de cette série par une expression indépendante de \( \Theta \) .

> b) Show that the series \( \sum \Theta \left( n\right) /{n}^{2} \) diverges and provide the best possible lower bound for the partial sums of this series using an expression independent of \( \Theta \).

c) Que peut-on dire sur la nature de la série \( \sum \Theta \left( n\right) /{n}^{3} \) ?

> c) What can be said about the nature of the series \( \sum \Theta \left( n\right) /{n}^{3} \)?

2/ a) (Inégalité de réarrangement). Soient \( n \in {\mathbb{N}}^{ * } \) et des réels \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) et \( {\left( {b}_{i}\right) }_{1 \leq i \leq n} \) tels que \( {a}_{1} \leq \ldots \leq {a}_{n} \) et \( {b}_{1} \leq \ldots \leq {b}_{n} \) . Montrer que pour toute permutation \( \sigma \in {\mathcal{S}}_{n} \) de \( \{ 1,\ldots , n\} \) , on a

> 2/ a) (Rearrangement inequality). Let \( n \in {\mathbb{N}}^{ * } \) and be real numbers \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) and \( {\left( {b}_{i}\right) }_{1 \leq i \leq n} \) such that \( {a}_{1} \leq \ldots \leq {a}_{n} \) and \( {b}_{1} \leq \ldots \leq {b}_{n} \) . Show that for any permutation \( \sigma \in {\mathcal{S}}_{n} \) of \( \{ 1,\ldots , n\} \) , we have

\[
{a}_{1}{b}_{\sigma \left( 1\right) } + \cdots  + {a}_{n}{b}_{\sigma \left( n\right) } \leq  {a}_{1}{b}_{1} + \cdots  + {a}_{n}{b}_{n}.
\]

(*)

> b) Soit \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite réelle positive décroissante telle que la série \( \sum {u}_{n} \) diverge. Montrer que la série \( \sum {u}_{n}\Theta \left( n\right) /n \) diverge.

b) Let \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a decreasing sequence of positive real numbers such that the series \( \sum {u}_{n} \) diverges. Show that the series \( \sum {u}_{n}\Theta \left( n\right) /n \) diverges.

> Solution. 1/ a) C'est tout simple. On utilise l'inégalité de Schwarz qui entraîne

Solution. 1/ a) It is quite simple. We use the Cauchy-Schwarz inequality, which implies

\[
\forall N \in  {\mathbb{N}}^{ * },\;{\left( \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n\Theta }\left( n\right) }\right) }^{2} \leq  \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{2}}}\right) \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{\Theta {\left( n\right) }^{2}}}\right) .
\]

(*)

> La série \( \sum 1/{n}^{2} \) converge, ainsi que \( \sum 1/\Theta {\left( n\right) }^{2} \) d’après le théorème 8 page 216 (et d’ailleurs, les sommes de ces deux séries sont égales). L'inégalité (*) montre donc que les sommes partielles de notre série sont majorées, donc elle converge, et en faisant \( N \rightarrow + \infty \) dans (*), on obtient

The series \( \sum 1/{n}^{2} \) converges, as does \( \sum 1/\Theta {\left( n\right) }^{2} \) according to Theorem 8 on page 216 (and, moreover, the sums of these two series are equal). Inequality (*) therefore shows that the partial sums of our series are bounded above, so it converges, and by letting \( N \rightarrow + \infty \) in (*), we obtain

\[
{\left( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n\Theta }\left( n\right) }\right) }^{2} \leq  \left( {\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}}}\right) \left( {\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{\Theta {\left( n\right) }^{2}}}\right)  = {\left( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}}\right) }^{2}\text{ donc }\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n\Theta }\left( n\right) } \leq  \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}}.
\]

Cette inégalité est la meilleure possible car il y a égalité lorsque \( \Theta \) est l’identité.

> This inequality is the best possible because equality holds when \( \Theta \) is the identity.

On aurait pu traiter cette question à partir de l’inégalité \( {ab} \leq \left( {{a}^{2} + {b}^{2}}\right) /2 \) appliquée à \( a = 1/\Theta \left( n\right) \) et \( b = 1/n. \)

> We could have addressed this question using the inequality \( {ab} \leq \left( {{a}^{2} + {b}^{2}}\right) /2 \) applied to \( a = 1/\Theta \left( n\right) \) and \( b = 1/n. \)

b) La manière la plus immédiate de montrer qu'il y a divergence est certainement de nier le critère de Cauchy, en écrivant

> b) The most immediate way to show that there is divergence is certainly to negate the Cauchy criterion by writing

\[
\forall N \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{n = N + 1}}^{{2N}}\frac{\Theta \left( n\right) }{{n}^{2}} \geq  \frac{1}{4{N}^{2}}\left( {\mathop{\sum }\limits_{{n = N + 1}}^{{2N}}\Theta \left( n\right) }\right)  \geq  \frac{1}{4{N}^{2}}\left( {\mathop{\sum }\limits_{{n = 1}}^{N}n}\right)  = \frac{N + 1}{8N} \geq  \frac{1}{8}.
\]

Si maintenant on veut une minoration fine des sommes partielles de cette série, on peut utiliser (encore !) l’inégalité de Schwarz qui entraîne, pour tout \( N \in {\mathbb{N}}^{ * } \)

> If we now want a sharp lower bound for the partial sums of this series, we can use (again!) the Cauchy-Schwarz inequality, which implies, for all \( N \in {\mathbb{N}}^{ * } \)

\[
{\left( \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n}\right) }^{2} = {\left( \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\sqrt{\Theta \left( n\right) }}{n}\frac{1}{\sqrt{\Theta \left( n\right) }}\right) }^{2} \leq  \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{\Theta \left( n\right) }{{n}^{2}}}\right) \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{\Theta \left( n\right) }}\right)  \leq  \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{\Theta \left( n\right) }{{n}^{2}}}\right) \left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n}}\right) ,
\]

donc \( \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\Theta \left( n\right) }{{n}^{2}} \geq \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n} \) . Cette minoration est optimale car il y a égalité lorsque \( \Theta \) est l’identité.

> thus \( \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\Theta \left( n\right) }{{n}^{2}} \geq \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n} \) . This lower bound is optimal because equality holds when \( \Theta \) is the identity.

c) On ne peut rien dire dans le cas général. Lorsque \( \Theta \) est l’identité, la série \( \sum \Theta \left( n\right) /{n}^{3} = \; \sum 1/{n}^{2} \) converge. Mais on peut construire \( \Theta \) tel que cette série diverge. Par exemple, notons \( A = \left\{ {{\left( 2n\right) }^{2} \mid n \in {\mathbb{N}}^{ * }}\right\} \) et \( B = {\mathbb{N}}^{ * } \smallsetminus A \) . On note \( {b}_{1} < {b}_{2} < {b}_{3} < \ldots \) les entiers de \( B \) rangés dans l’ordre croissant, et on définit \( \Theta \) par \( \Theta \left( {2n}\right) = {\left( 2n\right) }^{2} \) pour \( n \in {\mathbb{N}}^{ * } \) et \( \Theta \left( {{2n} + 1}\right) = {b}_{n} \) pour \( n \in \mathbb{N} \) . Avec ce choix \( \operatorname{de}\Theta \) , on voit que \( \sum \Theta \left( n\right) /{n}^{3} \) diverge car

> c) Nothing can be said in the general case. When \( \Theta \) is the identity, the series \( \sum \Theta \left( n\right) /{n}^{3} = \; \sum 1/{n}^{2} \) converges. However, one can construct \( \Theta \) such that this series diverges. For example, let us denote \( A = \left\{ {{\left( 2n\right) }^{2} \mid n \in {\mathbb{N}}^{ * }}\right\} \) and \( B = {\mathbb{N}}^{ * } \smallsetminus A \). Let \( {b}_{1} < {b}_{2} < {b}_{3} < \ldots \) be the integers of \( B \) arranged in increasing order, and define \( \Theta \) by \( \Theta \left( {2n}\right) = {\left( 2n\right) }^{2} \) for \( n \in {\mathbb{N}}^{ * } \) and \( \Theta \left( {{2n} + 1}\right) = {b}_{n} \) for \( n \in \mathbb{N} \). With this choice \( \operatorname{de}\Theta \), we see that \( \sum \Theta \left( n\right) /{n}^{3} \) diverges because

\[
\forall N \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{n = 1}}^{{2N}}\frac{\Theta \left( n\right) }{{n}^{3}} \geq  \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\Theta \left( {2n}\right) }{{\left( 2n\right) }^{3}} = \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{2n}.
\]

2/ a) C'est un classique. On procède par récurrence sur \( n \) . Pour \( n = 1 \) c’est évident. Supposons le résultat vrai pour \( n - 1 \) et montrons l’inégalité (*) pour \( n \) . Si \( \sigma \left( n\right) = n \) c’est évident, car dans ce cas la restriction de \( \sigma \) à \( \{ 1,\ldots , n - 1\} \) est une permutation de \( \{ 1,\ldots , n - 1\} \) et il suffit d’appliquer l’hypothèse de récurrence. Sinon, on a \( k = {\sigma }^{-1}\left( n\right) < n \) et \( \ell = \sigma \left( n\right) < n \) , et on définit la permutation \( {\sigma }^{\prime } \) de \( \{ 1,\ldots , n - 1\} \) par \( {\sigma }^{\prime }\left( i\right) = \sigma \left( i\right) \) si \( i \neq k \) , et \( {\sigma }^{\prime }\left( k\right) = \ell \) . On a \( \left( {{a}_{n} - {a}_{k}}\right) \left( {{b}_{n} - {b}_{\ell }}\right) \geq 0 \) donc \( {a}_{n}{b}_{\ell } + {a}_{k}{b}_{n} - {a}_{k}{b}_{\ell } \leq {a}_{n}{b}_{n} \) . On en déduit

> 2/ a) This is a classic. We proceed by induction on \( n \). For \( n = 1 \) it is obvious. Assume the result is true for \( n - 1 \) and show inequality (*) for \( n \). If \( \sigma \left( n\right) = n \) it is obvious, because in this case the restriction of \( \sigma \) to \( \{ 1,\ldots , n - 1\} \) is a permutation of \( \{ 1,\ldots , n - 1\} \) and it suffices to apply the induction hypothesis. Otherwise, we have \( k = {\sigma }^{-1}\left( n\right) < n \) and \( \ell = \sigma \left( n\right) < n \), and we define the permutation \( {\sigma }^{\prime } \) of \( \{ 1,\ldots , n - 1\} \) by \( {\sigma }^{\prime }\left( i\right) = \sigma \left( i\right) \) if \( i \neq k \), and \( {\sigma }^{\prime }\left( k\right) = \ell \). We have \( \left( {{a}_{n} - {a}_{k}}\right) \left( {{b}_{n} - {b}_{\ell }}\right) \geq 0 \) therefore \( {a}_{n}{b}_{\ell } + {a}_{k}{b}_{n} - {a}_{k}{b}_{\ell } \leq {a}_{n}{b}_{n} \). We deduce from this

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{b}_{\sigma \left( i\right) } = \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{{\sigma }^{\prime }\left( i\right) } + {a}_{n}{b}_{\ell } + {a}_{k}{b}_{n} - {a}_{k}{b}_{\ell } \leq  \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{{\sigma }^{\prime }\left( i\right) } + {a}_{n}{b}_{n}.
\]

Le résultat pour \( n \) en découle, car d’apres l’hypothèse de récurrence \( \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{{\sigma }^{\prime }\left( i\right) } \leq \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} \) . b) Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {b}_{1} < \ldots < {b}_{n} \) les valeurs de \( \Theta \left( 1\right) ,\ldots ,\Theta \left( n\right) \) rangées dans l’ordre croissant. Soit \( \sigma \in {\mathcal{S}}_{n} \) tel que \( {b}_{\sigma \left( k\right) } = \Theta \left( k\right) \) pour \( k = 1,\ldots , n \) . Soit \( {a}_{k} = - {u}_{k}/k \) . Comme \( \left( {u}_{k}\right) \) est positive et décroissante, \( \left( {{u}_{k}/k}\right) \) également donc on a \( {a}_{1} \leq \ldots \leq {a}_{n} \) . On en déduit, d’après le résultat de la question précédente et après changement de signe, que

> The result for \( n \) follows, because according to the induction hypothesis \( \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{{\sigma }^{\prime }\left( i\right) } \leq \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} \) . b) Let \( n \in {\mathbb{N}}^{ * } \) . We denote by \( {b}_{1} < \ldots < {b}_{n} \) the values of \( \Theta \left( 1\right) ,\ldots ,\Theta \left( n\right) \) arranged in increasing order. Let \( \sigma \in {\mathcal{S}}_{n} \) such that \( {b}_{\sigma \left( k\right) } = \Theta \left( k\right) \) for \( k = 1,\ldots , n \) . Let \( {a}_{k} = - {u}_{k}/k \) . Since \( \left( {u}_{k}\right) \) is positive and decreasing, \( \left( {{u}_{k}/k}\right) \) is as well, so we have \( {a}_{1} \leq \ldots \leq {a}_{n} \) . We deduce, from the result of the previous question and after a change of sign, that

\[
\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{u}_{k}}{k}{b}_{\sigma \left( k\right) } \geq  \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{u}_{k}}{k}{b}_{k}
\]

et comme \( {b}_{\sigma \left( k\right) } = \Theta \left( k\right) \) et \( {b}_{k} \geq k \) ceci implique

> and since \( {b}_{\sigma \left( k\right) } = \Theta \left( k\right) \) and \( {b}_{k} \geq k \) this implies

\[
\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{u}_{k}}{k}\Theta \left( k\right)  \geq  \mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k}
\]

On en déduit le résultat car \( \sum {u}_{n} \) diverge.

> We deduce the result because \( \sum {u}_{n} \) diverges.

Remarque. L'inégalité de réarrangement (parfois appelée inégalité de réordonnement) est classique. Nous aurions pu l'utiliser pour obtenir les résultats des questions 1/a) et 1/b). Elle entraîne de nombreuses inégalités, comme l'inégalité de Tchébycheff pour les sommes : \( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{y}_{i} \geq \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}}\right) \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}}\right) /n \) des que \( {x}_{1} \leq \ldots \leq {x}_{n} \) et \( {y}_{1} \geq \ldots \geq {y}_{n} \) . On peut aussi utiliser l'inégalité de réarrangement pour démontrer l'inégalité de Schwarz, ou pour démontrer que la moyenne géométrique est inférieure à la moyenne arithmétique.

> Remark. The rearrangement inequality (sometimes called the reordering inequality) is classic. We could have used it to obtain the results of questions 1/a) and 1/b). It leads to numerous inequalities, such as Chebyshev's sum inequality: \( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{y}_{i} \geq \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}}\right) \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}}\right) /n \) as soon as \( {x}_{1} \leq \ldots \leq {x}_{n} \) and \( {y}_{1} \geq \ldots \geq {y}_{n} \) . One can also use the rearrangement inequality to prove the Cauchy-Schwarz inequality, or to prove that the geometric mean is less than or equal to the arithmetic mean.
