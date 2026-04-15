#### 2.4. Semi-convergent series

*Français : 2.4. Séries semi-convergentes*

On appelle ainsi les séries convergentes mais non absolument convergentes.

> This term refers to series that are convergent but not absolutely convergent.

Séries alternées. Ce sont les séries réelles \( \sum {u}_{n} \) dont les termes changent alternative-ment de signe. Au signe près, on peut les écrire \( \sum {\left( -1\right) }^{n}{a}_{n} \) où \( {a}_{n} \geq 0 \) pour tout \( n \) .

> Alternating series. These are real series \( \sum {u}_{n} \) whose terms alternate in sign. Up to a sign, they can be written as \( \sum {\left( -1\right) }^{n}{a}_{n} \) where \( {a}_{n} \geq 0 \) for all \( n \).

THÉORÉME 6. Soit \( \left( {a}_{n}\right) \) une suite à termes positifs, décroissante, tendant vers 0. Alors la série alternée \( \sum {\left( -1\right) }^{n}{a}_{n} \) converge, et les restes

> THEOREM 6. Let \( \left( {a}_{n}\right) \) be a sequence of positive, decreasing terms tending to 0. Then the alternating series \( \sum {\left( -1\right) }^{n}{a}_{n} \) converges, and the remainders

\[
\forall n \in  \mathbb{N},\;{R}_{n} = \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{\left( -1\right) }^{k}{a}_{k}\;\text{ vérífient }\left| {R}_{n}\right|  \leq  {a}_{n + 1}.
\]

Démonstration. Pour tout \( n \in \mathbb{N} \) , on note \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{a}_{k} \) . La suite \( \left( {a}_{n}\right) \) étant décroissante, on a

> Proof. For all \( n \in \mathbb{N} \), we denote \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{a}_{k} \). Since the sequence \( \left( {a}_{n}\right) \) is decreasing, we have

\[
\forall n \in  {\mathbb{N}}^{ * },\;{S}_{2n} - {S}_{{2n} - 2} = {a}_{2n} - {a}_{{2n} - 1} \leq  0,\;{S}_{{2n} + 1} - {S}_{{2n} - 1} = {a}_{2n} - {a}_{{2n} + 1} \geq  0.
\]

Autrement dit, la suite \( \left( {S}_{2n}\right) \) est décroissante, \( \left( {S}_{{2n} + 1}\right) \) est croissante. Or \( {S}_{{2n} + 1} - {S}_{2n} = - {a}_{{2n} + 1} \) , donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{{2n} + 1} - {S}_{2n} = 0 \) . Les suites \( \left( {S}_{2n}\right) \) et \( \left( {S}_{{2n} + 1}\right) \) sont donc adjacentes. Elles convergent donc vers une même limite \( S \) . La suite \( \left( {S}_{n}\right) \) converge donc vers \( S \) et

> In other words, the sequence \( \left( {S}_{2n}\right) \) is decreasing, \( \left( {S}_{{2n} + 1}\right) \) is increasing. Now \( {S}_{{2n} + 1} - {S}_{2n} = - {a}_{{2n} + 1} \), so \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{{2n} + 1} - {S}_{2n} = 0 \). The sequences \( \left( {S}_{2n}\right) \) and \( \left( {S}_{{2n} + 1}\right) \) are therefore adjacent. They thus converge to the same limit \( S \). The sequence \( \left( {S}_{n}\right) \) therefore converges to \( S \) and

\[
\forall n \in  \mathbb{N},\;{S}_{{2n} + 1} \leq  S \leq  {S}_{2n}.
\]

Ceci entraîne

> This implies

\[
\forall n \in  \mathbb{N},\;\left| {R}_{2n}\right|  = \left| {S - {S}_{2n}}\right|  \leq  {S}_{2n} - {S}_{{2n} + 1} = {a}_{{2n} + 1},
\]

de même

> similarly

\[
\forall n \in  {\mathbb{N}}^{ * },\;\left| {R}_{{2n} - 1}\right|  = \left| {S - {S}_{{2n} - 1}}\right|  \leq  {S}_{2n} - {S}_{{2n} - 1} = {a}_{2n},
\]

ce qui montre \( \left| {R}_{n}\right| \leq {a}_{n + 1} \) pour tout \( n \in \mathbb{N} \) .

> which shows \( \left| {R}_{n}\right| \leq {a}_{n + 1} \) for all \( n \in \mathbb{N} \).

Transformation d'Abel. La transformation d'Abel est aux séries ce que l'intégration par parties est aux intégrales. Soit une série \( \sum {u}_{n} \) avec \( {u}_{n} = {\alpha }_{n}{v}_{n} \) . On note \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \) . Effectuer une transformation \( d \) ’Abel sur la série \( \sum {u}_{n} \) c’est écrire, pour tout \( n \) ,

> Abel's transformation. Abel's transformation is to series what integration by parts is to integrals. Let there be a series \( \sum {u}_{n} \) with \( {u}_{n} = {\alpha }_{n}{v}_{n} \). We denote \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{v}_{k} \). Performing an \( d \) Abel transformation on the series \( \sum {u}_{n} \) means writing, for any \( n \),

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} = \mathop{\sum }\limits_{{k = 0}}^{n}{\alpha }_{k}{v}_{k} = {\alpha }_{0}{v}_{0} + \mathop{\sum }\limits_{{k = 1}}^{n}{\alpha }_{k}\left( {{S}_{k} - {S}_{k - 1}}\right)
\]

\[
= {\alpha }_{0}{v}_{0} + \mathop{\sum }\limits_{{k = 1}}^{n}{\alpha }_{k}{S}_{k} - \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{\alpha }_{k + 1}{S}_{k} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) {S}_{k} + {\alpha }_{n}{S}_{n}
\]

(on peut comparer cette expression à celle de l'intégration par parties, en disant que \( {\alpha }_{k + 1} - {\alpha }_{k} \) est la "dérivée" de \( \left( {\alpha }_{k}\right) \) et \( {S}_{n} \) est une "primitive" de \( \left( {v}_{n}\right) ) \) . Grâce à cette technique, on montre le résultat suivant. C'est la version pour les séries du théorème 5 de la page 152.

> (we can compare this expression to that of integration by parts, by saying that \( {\alpha }_{k + 1} - {\alpha }_{k} \) is the "derivative" of \( \left( {\alpha }_{k}\right) \) and \( {S}_{n} \) is an "antiderivative" of \( \left( {v}_{n}\right) ) \) . Thanks to this technique, we show the following result. This is the series version of theorem 5 on page 152.

THÉORÉME 7 (RÉGLE D'ABEL). Soit \( \sum {u}_{n} \) une série à valeurs dans un espace de Banach. On suppose que pour tout \( n,{u}_{n} = {\alpha }_{n}{v}_{n} \) où

> THEOREM 7 (ABEL'S TEST). Let \( \sum {u}_{n} \) be a series with values in a Banach space. We assume that for all \( n,{u}_{n} = {\alpha }_{n}{v}_{n} \) where

- ( \( {\alpha }_{n} \) ) est une suite positive, décroissante et tend vers0;

> - ( \( {\alpha }_{n} \) ) is a positive, decreasing sequence that tends to 0;

- la série \( \sum {v}_{n} \) est bornée.

> - the series \( \sum {v}_{n} \) is bounded.

Alors la série \( \overline{\sum }{u}_{n} \) est convergente.

> Then the series \( \overline{\sum }{u}_{n} \) is convergent.

Démonstration. Pour tout \( n \) , notons \( {S}_{n} = {v}_{0} + \cdots + {v}_{n} \) . Par hypothèse, il existe \( M > 0 \) tel que \( \begin{Vmatrix}{S}_{n}\end{Vmatrix} \leq M \) pour tout \( n \) . Une transformation d’Abel sur \( \sum {u}_{n} \) donne

> Proof. For any \( n \) , let \( {S}_{n} = {v}_{0} + \cdots + {v}_{n} \) . By hypothesis, there exists \( M > 0 \) such that \( \begin{Vmatrix}{S}_{n}\end{Vmatrix} \leq M \) for all \( n \) . An Abel transformation on \( \sum {u}_{n} \) gives

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) {S}_{k} + {\alpha }_{n}{S}_{n}.
\]

(*)

> La série \( \mathop{\sum }\limits_{k}\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) {S}_{k} \) converge absolument car

The series \( \mathop{\sum }\limits_{k}\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) {S}_{k} \) converges absolutely because

\[
\forall n \in  \mathbb{N},\;\mathop{\sum }\limits_{{k = 0}}^{n}\begin{Vmatrix}{\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) {S}_{k}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = 0}}^{n}\left( {{\alpha }_{k} - {\alpha }_{k + 1}}\right) M = \left( {{\alpha }_{0} - {\alpha }_{n + 1}}\right) M \leq  {\alpha }_{0}M
\]

Par ailleurs, \( \left( {{\alpha }_{n}{S}_{n}}\right) \) tend vers0car \( \left( {S}_{n}\right) \) est bornée et \( \left( {\alpha }_{n}\right) \) tend vers0. On en conclut avec l’expression (*) que la série \( \sum {u}_{n} \) converge.

> Furthermore, \( \left( {{\alpha }_{n}{S}_{n}}\right) \) tends to 0 because \( \left( {S}_{n}\right) \) is bounded and \( \left( {\alpha }_{n}\right) \) tends to 0. We conclude from expression (*) that the series \( \sum {u}_{n} \) converges.

Exemple 3. - En prenant \( {\alpha }_{n} = {a}_{n} \) et \( {v}_{n} = {\left( -1\right) }^{n} \) , on retrouve le résultat de convergence du théorème 6.

> Example 3. - By taking \( {\alpha }_{n} = {a}_{n} \) and \( {v}_{n} = {\left( -1\right) }^{n} \) , we recover the convergence result of theorem 6.

- Une série de la forme \( \sum {\alpha }_{n}{e}^{ni\theta } \) , où \( \left( {\alpha }_{n}\right) \) est une suite décroissante tendant vers 0 et où \( \theta  \in  \mathbb{R} \smallsetminus  {2\pi }\mathbb{Z} \) , converge. En effet, on a

> - A series of the form \( \sum {\alpha }_{n}{e}^{ni\theta } \) , where \( \left( {\alpha }_{n}\right) \) is a decreasing sequence tending to 0 and where \( \theta  \in  \mathbb{R} \smallsetminus  {2\pi }\mathbb{Z} \) , converges. Indeed, we have

\[
\forall n \in  \mathbb{N},\;\left| {1 + {e}^{i\theta } + \cdots  + {e}^{ni\theta }}\right|  = \left| \frac{1 - {e}^{\left( {n + 1}\right) {i\theta }}}{1 - {e}^{i\theta }}\right|  \leq  \frac{2}{\left| 1 - {e}^{i\theta }\right| } = \frac{1}{\left| \sin \left( \theta /2\right) \right| },
\]

donc la série converge d'après la règle d'Abel. On en déduit en particulier que la série \( \sum {e}^{ni\theta }/{n}^{\alpha } \) converge pour tout \( \alpha > 0 \) .

> therefore the series converges according to Abel's rule. We deduce in particular that the series \( \sum {e}^{ni\theta }/{n}^{\alpha } \) converges for all \( \alpha > 0 \) .
