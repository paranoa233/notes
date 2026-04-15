#### 2.3. Some recipes

*Français : 2.3. Quelques recettes*

PROPOSITION 4. Soient \( \sum {u}_{n} \) et \( \sum {v}_{n} \) deux séries à termes strictement positifs, telles qu’à partir d’un certain rang, on ait \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \) . Alors

> PROPOSITION 4. Let \( \sum {u}_{n} \) and \( \sum {v}_{n} \) be two series with strictly positive terms, such that from a certain rank, we have \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \). Then

(i) si \( \sum {u}_{n} \) converge, \( \sum {v}_{n} \) converge;

> (i) if \( \sum {u}_{n} \) converges, \( \sum {v}_{n} \) converges;

(ii) si \( \sum {v}_{n} \) diverge, \( \sum {u}_{n} \) diverge.

> (ii) if \( \sum {v}_{n} \) diverges, \( \sum {u}_{n} \) diverges.

Démonstration. Soit \( N \in \mathbb{N} \) tel que \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \) pour tout \( n \geq N \) . Une récurrence immédiate montre que

> Proof. Let \( N \in \mathbb{N} \) be such that \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \) for all \( n \geq N \). An immediate recurrence shows that

\[
\forall n \geq  N,\;\frac{{u}_{n}}{{u}_{N}} \geq  \frac{{v}_{n}}{{v}_{N}}\;\text{ ou encore }\;{u}_{n} \geq  K{v}_{n}\;\text{ avec }\;K = \frac{{u}_{N}}{{v}_{N}}.
\]

On conclut facilement en appliquant le théorème 3 page 209.

> We conclude easily by applying theorem 3 page 209.

COROLLAIRE 2. Soit \( \sum {u}_{n} \) une série à termes strictement positifs vérifiant

> COROLLARY 2. Let \( \sum {u}_{n} \) be a series with strictly positive terms satisfying

\[
\frac{{u}_{n + 1}}{{u}_{n}} = \frac{1}{1 + a/n + o\left( {1/n}\right) },\;a \in  \mathbb{R},\;n \rightarrow   + \infty .
\]

Alors si a \( > 1 \) , la série \( \sum {u}_{n} \) converge ; si \( a < 1 \) , la série diverge.

> Then if \( > 1 \), the series \( \sum {u}_{n} \) converges; if \( a < 1 \), the series diverges.

Démonstration. Supposons \( a > 1 \) , et fixons un nombre réel \( b \) tel que \( 1 < b < a \) . Considérons la suite \( \left( {v}_{n}\right) \) définie par \( {v}_{n} = {n}^{-b} \) . La série \( \sum {v}_{n} \) converge et

> Proof. Suppose \( a > 1 \), and fix a real number \( b \) such that \( 1 < b < a \). Consider the sequence \( \left( {v}_{n}\right) \) defined by \( {v}_{n} = {n}^{-b} \). The series \( \sum {v}_{n} \) converges and

\[
\frac{{v}_{n + 1}}{{v}_{n}} = \frac{1}{{\left( 1 + 1/n\right) }^{b}} = \frac{1}{1 + b/n + o\left( {1/n}\right) }.
\]

Comme \( b < a \) , on en déduit qu’à partir d’un certain rang, \( {v}_{n + 1}/{v}_{n} \geq {u}_{n + 1}/{u}_{n} \) , donc \( \sum {u}_{n} \) converge d'après la proposition précédente.

> Since \( b < a \), we deduce that from a certain rank, \( {v}_{n + 1}/{v}_{n} \geq {u}_{n + 1}/{u}_{n} \), therefore \( \sum {u}_{n} \) converges according to the previous proposition.

Si \( a < 1 \) , on montrerait en procédant de la même manière qu'à partir d'un certain rang, \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \) où \( {v}_{n} = {n}^{-b}, b \) étant fixé tel que \( a < b < 1 \) . Comme \( \sum {v}_{n} \) diverge, on en déduit toujours avec la proposition précédente que \( \sum {u}_{n} \) diverge.

> If \( a < 1 \), we would show by proceeding in the same way that from a certain rank, \( {u}_{n + 1}/{u}_{n} \geq {v}_{n + 1}/{v}_{n} \) where \( {v}_{n} = {n}^{-b}, b \) is fixed such that \( a < b < 1 \). Since \( \sum {v}_{n} \) diverges, we deduce again with the previous proposition that \( \sum {u}_{n} \) diverges.

Remarque 5. Si a =1, on ne peut pas conclure quant à la nature de la série. Considérons par exemple la série de Bertrand \( \sum {u}_{n} \) avec \( {u}_{n} = {n}^{-1}{\log }^{\beta }n \) . Lorsque \( \beta < - 1,\sum {u}_{n} \) converge; lorsque \( \beta \geq - 1,\sum {u}_{n} \) diverge, et on a pour tout \( \beta \)

> Remark 5. If a =1, we cannot conclude the nature of the series. Consider for example the Bertrand series \( \sum {u}_{n} \) with \( {u}_{n} = {n}^{-1}{\log }^{\beta }n \) . When \( \beta < - 1,\sum {u}_{n} \) converges; when \( \beta \geq - 1,\sum {u}_{n} \) diverges, and we have for all \( \beta \)

\[
\frac{{u}_{n + 1}}{{u}_{n}} = {\left( 1 + \frac{1}{n} + \frac{\beta }{n\log n} + o\left( \frac{1}{n\log n}\right) \right) }^{-1} = {\left( 1 + \frac{1}{n} + o\left( \frac{1}{n}\right) \right) }^{-1}.
\]

Règle de Raab-Duhamel. Proposition 5 (RÉGLE DE RAAB-DUHAMEL). Soit \( \left( {u}_{n}\right) \) une série à termes \( > 0 \) telle que

> Raabe-Duhamel's Rule. Proposition 5 (RAABE-DUHAMEL'S RULE). Let \( \left( {u}_{n}\right) \) be a series with \( > 0 \) terms such that

\[
\frac{{u}_{n + 1}}{{u}_{n}} = \frac{1}{1 + a/n + O\left( {1/{n}^{2}}\right) }\;n \rightarrow   + \infty .
\]

Alors il existe \( \lambda > 0 \) tel que \( {u}_{n} \sim \lambda /{n}^{a} \) lorsque \( n \rightarrow + \infty \) .

> Then there exists \( \lambda > 0 \) such that \( {u}_{n} \sim \lambda /{n}^{a} \) when \( n \rightarrow + \infty \) .

Démonstration. Il s’agit de montrer que la suite \( \left( {{n}^{a}{u}_{n}}\right) \) converge et a une limite \( > 0 \) . Pour cela, on considère la suite \( \left( {v}_{n}\right) \) définie par \( {v}_{n} = \log \left( {{n}^{a}{u}_{n}}\right) \) . Pour l’étudier, on considère la série \( \sum {w}_{n} \) où pour tout \( n,{w}_{n} = {v}_{n + 1} - {v}_{n} \) . On a

> Proof. We must show that the sequence \( \left( {{n}^{a}{u}_{n}}\right) \) converges and has a limit \( > 0 \) . To do this, we consider the sequence \( \left( {v}_{n}\right) \) defined by \( {v}_{n} = \log \left( {{n}^{a}{u}_{n}}\right) \) . To study it, we consider the series \( \sum {w}_{n} \) where for all \( n,{w}_{n} = {v}_{n + 1} - {v}_{n} \) . We have

\[
{w}_{n} = \log \left\lbrack  {\left( \frac{n + 1}{n}\right) }^{a}\right\rbrack   + \log \left( \frac{{u}_{n + 1}}{{u}_{n}}\right)  = a\log \left( {1 + \frac{1}{n}}\right)  - \log \left( {1 + \frac{a}{n} + O\left( \frac{1}{{n}^{2}}\right) }\right)
\]

\[
= \frac{a}{n} + O\left( \frac{1}{{n}^{2}}\right)  - \left( {\frac{a}{n} + O\left( \frac{1}{{n}^{2}}\right) }\right)  = O\left( \frac{1}{{n}^{2}}\right) ,
\]

donc la série \( \sum {w}_{n} \) converge. Comme \( {w}_{1} + \cdots + {w}_{n} = {v}_{n + 1} - {v}_{1} \) , la suite \( \left( {v}_{n}\right) \) converge. Donc \( {n}^{a}{u}_{n} = \exp \left( {v}_{n}\right) \) converge vers une limite \( > 0 \) , d’où le résultat.

> therefore the series \( \sum {w}_{n} \) converges. Since \( {w}_{1} + \cdots + {w}_{n} = {v}_{n + 1} - {v}_{1} \) , the sequence \( \left( {v}_{n}\right) \) converges. Thus \( {n}^{a}{u}_{n} = \exp \left( {v}_{n}\right) \) converges to a limit \( > 0 \) , hence the result.

Remarque 6. - Cette règle permet de déterminer la nature de la série \( \sum {u}_{n} \) : elle converge si et seulement si \( a > 1 \) .

> Remark 6. - This rule allows us to determine the nature of the series \( \sum {u}_{n} \) : it converges if and only if \( a > 1 \) .

- Sans la présence du \( O\left( {1/{n}^{2}}\right) \) , le résultat est faux (nous avons vu à la remarque 5 le cas d’une série convergente \( \sum {u}_{n} \) pour laquelle \( {u}_{n + 1}/{u}_{n} = {\left( 1 + 1/n + o\left( 1/n\right) \right) }^{-1} \) ).

> - Without the presence of \( O\left( {1/{n}^{2}}\right) \) , the result is false (we saw in remark 5 the case of a convergent series \( \sum {u}_{n} \) for which \( {u}_{n + 1}/{u}_{n} = {\left( 1 + 1/n + o\left( 1/n\right) \right) }^{-1} \) ).

- La règle de Raab-Duhamel reste vérifiée lorsqu’on remplace \( O\left( {1/{n}^{2}}\right) \) par \( O\left( {1/{n}^{\alpha }}\right) \) avec \( \alpha  > 1 \) (pour s’en persuader, reprendre la preuve dans ce cas).

> - Raabe-Duhamel's rule remains valid when replacing \( O\left( {1/{n}^{2}}\right) \) with \( O\left( {1/{n}^{\alpha }}\right) \) with \( \alpha  > 1 \) (to be convinced, re-examine the proof in this case).

Règle de d'Alembert, règle de Cauchy.

> d'Alembert's rule, Cauchy's rule.

Proposition 6 (REQLE DE D'ALEMBERT). Soit \( \sum {u}_{n} \) une série à termes \( > 0 \) telle que

> Proposition 6 (D'ALEMBERT'S RULE). Let \( \sum {u}_{n} \) be a series with \( > 0 \) terms such that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{u}_{n + 1}}{{u}_{n}} = \lambda ,\;\lambda  \in  \left\lbrack  {0, + \infty }\right\rbrack
\]

Alors

> Then

(i) si \( \lambda < 1,\sum {u}_{n} \) converge ;

> (i) if \( \lambda < 1,\sum {u}_{n} \) converges;

(ii) si \( \lambda > 1,\sum {u}_{n} \) diverge ;

> (ii) if \( \lambda > 1,\sum {u}_{n} \) diverges;

(iii) si \( \lambda = {1}^{ + } \) (i.e. \( {si}{u}_{n + 1}/{u}_{n} \) tend vers 1 en restant supérieur à 1), \( \sum {u}_{n} \) diverge.

> (iii) if \( \lambda = {1}^{ + } \) (i.e. \( {si}{u}_{n + 1}/{u}_{n} \) tends to 1 while remaining greater than 1), \( \sum {u}_{n} \) diverges.

Proposition 7 (RÉGLE DE CAUCHY). Soit \( \sum {u}_{n} \) une série à termes \( > 0 \) telle que

> Proposition 7 (CAUCHY'S RULE). Let \( \sum {u}_{n} \) be a series with \( > 0 \) terms such that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\sqrt[n]{{u}_{n}} = \lambda ,\;\lambda  \in  \left\lbrack  {0, + \infty }\right\rbrack
\]

Alors

> Then

(i) si \( \lambda < 1,\sum {u}_{n} \) converge ;

> (i) if \( \lambda < 1,\sum {u}_{n} \) converges;

(ii) si \( \lambda > 1,\sum {u}_{n} \) diverge;

> (ii) if \( \lambda > 1,\sum {u}_{n} \) diverges;

(iii) si \( \lambda = {1}^{ + } \) (i.e. \( {si}{\left( {u}_{n}\right) }^{1/n} \) tend vers 1 en restant supérieur à 1), \( \sum {u}_{n} \) diverge.

> (iii) if \( \lambda = {1}^{ + } \) (i.e. \( {si}{\left( {u}_{n}\right) }^{1/n} \) tends to 1 while remaining greater than 1), \( \sum {u}_{n} \) diverges.

Remarque 7. On peut montrer que si \( {u}_{n + 1}/{u}_{n} \rightarrow \lambda \) , alors \( {\left( {u}_{n}\right) }^{1/n} \rightarrow \lambda \) . La réciproque est fausse (par exemple, la suite \( {u}_{n} = 2 + {\left( -1\right) }^{n} \) vérifie \( {\left( {u}_{n}\right) }^{1/n} \rightarrow 1 \) mais \( {u}_{n + 1}/{u}_{n} \) ne converge pas).

> Remark 7. It can be shown that if \( {u}_{n + 1}/{u}_{n} \rightarrow \lambda \), then \( {\left( {u}_{n}\right) }^{1/n} \rightarrow \lambda \). The converse is false (for example, the sequence \( {u}_{n} = 2 + {\left( -1\right) }^{n} \) satisfies \( {\left( {u}_{n}\right) }^{1/n} \rightarrow 1 \) but \( {u}_{n + 1}/{u}_{n} \) does not converge).
