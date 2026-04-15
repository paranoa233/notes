#### 4.2. Properties of power series

*Français : 4.2. Propriétés des séries entières*

Dans toute cette sous-partie, \( \sum {a}_{n}{z}^{n} \) désigne une série entière de rayon de convergence \( R > 0 \) .

> Throughout this subsection, \( \sum {a}_{n}{z}^{n} \) denotes a power series with radius of convergence \( R > 0 \).

Continuité.

> Continuity.

THÉORÉME 1. L’application \( z \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) est continue sur le disque de convergence \( \{ z \in \mathbb{C},\left| z\right| < R\} \)

> THEOREM 1. The mapping \( z \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) is continuous on the disk of convergence \( \{ z \in \mathbb{C},\left| z\right| < R\} \).

Démonstration. Pour tout \( r \in \rbrack 0, R\left\lbrack {,\sum {a}_{n}{z}^{n}}\right. \) converge normalement sur \( \left| z\right| \leq r \) , sa somme est donc continue sur \( \left| z\right| \leq r \) (chaque somme partielle est continue), et ceci pour tout \( r < R \) , d’où le résultat.

> Proof. For any \( r \in \rbrack 0, R\left\lbrack {,\sum {a}_{n}{z}^{n}}\right. \), it converges normally on \( \left| z\right| \leq r \), so its sum is continuous on \( \left| z\right| \leq r \) (each partial sum is continuous), and this holds for any \( r < R \), hence the result.

##### Differentiation.

*Français : Dérivation.*

THÉORÉME 2. L’application \( f : \rbrack - R, R\lbrack \rightarrow \mathbb{C}\;x \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n} \) est de classe \( {\mathcal{C}}^{1} \) . La série entière \( \sum n{a}_{n}{z}^{n - 1} \) a même rayon de convergence que \( \sum {a}_{n}{z}^{n} \) , et on a

> THEOREM 2. The mapping \( f : \rbrack - R, R\lbrack \rightarrow \mathbb{C}\;x \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n} \) is of class \( {\mathcal{C}}^{1} \). The power series \( \sum n{a}_{n}{z}^{n - 1} \) has the same radius of convergence as \( \sum {a}_{n}{z}^{n} \), and we have

\[
\forall x \in  \rbrack  - R, R\left\lbrack  {,\;{f}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{a}_{n}{x}^{n - 1}.}\right.
\]

Démonstration. Notons \( {R}^{\prime } \) le rayon de convergence de \( \sum n{a}_{n}{z}^{n - 1} \) . Soit \( r,0 \leq r < {R}^{\prime } \) . La suite \( \left( {n{a}_{n}{r}^{n}}\right) \) est bornée, donc \( \left( {{a}_{n}{r}^{n}}\right) \) est bornée donc \( r \leq \bar{R} \) . Ceci étant vrai pour tout \( r < {R}^{\prime } \) , on en déduit \( {R}^{\prime } \leq R \) . Maintenant, soit \( r < R \) . Si on fixe \( {r}_{0} \) tel que \( r < {r}_{0} < R \) , la suite \( \left( {{a}_{n}{r}_{0}^{n}}\right) \) est bornée, donc la suite \( \left( {n{a}_{n}{r}^{n}}\right) \) tend vers 0 car \( n{a}_{n}{r}^{n} = n\left( {{a}_{n}{r}_{0}^{n}}\right) {\left( r/{r}_{0}\right) }^{n} \) avec \( r/{r}_{0} < 1 \) . On en conclut \( r < {R}^{\prime } \) , et ceci pour tout \( r < R \) donc \( R \leq {R}^{\prime } \) . Finalement, on a donc \( R = {R}^{\prime } \) .

> Proof. Let \( {R}^{\prime } \) be the radius of convergence of \( \sum n{a}_{n}{z}^{n - 1} \). Let \( r,0 \leq r < {R}^{\prime } \). The sequence \( \left( {n{a}_{n}{r}^{n}}\right) \) is bounded, so \( \left( {{a}_{n}{r}^{n}}\right) \) is bounded, therefore \( r \leq \bar{R} \). Since this is true for any \( r < {R}^{\prime } \), we deduce \( {R}^{\prime } \leq R \). Now, let \( r < R \). If we fix \( {r}_{0} \) such that \( r < {r}_{0} < R \), the sequence \( \left( {{a}_{n}{r}_{0}^{n}}\right) \) is bounded, so the sequence \( \left( {n{a}_{n}{r}^{n}}\right) \) tends to 0 because \( n{a}_{n}{r}^{n} = n\left( {{a}_{n}{r}_{0}^{n}}\right) {\left( r/{r}_{0}\right) }^{n} \) with \( r/{r}_{0} < 1 \). We conclude \( r < {R}^{\prime } \), and this for any \( r < R \), so \( R \leq {R}^{\prime } \). Finally, we have \( R = {R}^{\prime } \).

La dérivabilité de \( f \) et la valeur de \( {f}^{\prime } \) sont une conséquence du théorème de dérivabilité des suites de fonctions.

> The differentiability of \( f \) and the value of \( {f}^{\prime } \) are a consequence of the theorem on the differentiability of sequences of functions.

En appliquant ce théorème par récurrence, on obtient le résultat qui suit.

> By applying this theorem by induction, we obtain the following result.

COROLLAIRE 1. La somme \( f \) de la série entière \( \sum {a}_{n}{z}^{n} \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \rbrack - R, R\lbrack \) . De plus, pour tout \( p \in \mathbb{N},{f}^{\left( p\right) } \) est la somme sur \( \rbrack - R, R\lbrack \) d’une série entière de rayon de convergence \( R > 0 \) . En outre,

> COROLLARY 1. The sum \( f \) of the power series \( \sum {a}_{n}{z}^{n} \) is of class \( {\mathcal{C}}^{\infty } \) on \( \rbrack - R, R\lbrack \) . Furthermore, for any \( p \in \mathbb{N},{f}^{\left( p\right) } \) is the sum on \( \rbrack - R, R\lbrack \) of a power series with radius of convergence \( R > 0 \) . In addition,

\[
\forall p \in  \mathbb{N},\;{a}_{p} = \frac{{f}^{\left( p\right) }\left( 0\right) }{p!}\;\text{ donc }\;\forall z \in  \mathbb{C},\;f\left( z\right)  = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{f}^{\left( p\right) }\left( 0\right) }{p!}{z}^{p}.
\]

Conséquence :

> Consequence:

- La série entière \( \sum \frac{{a}_{n}}{n + 1}{z}^{n + 1} \) a pour rayon de convergence \( R \) et si \( F \) désigne la somme de cette dernière, on a \( {F}^{\prime } = f \) sur \( \rbrack  - R, R\lbrack \) .

> - The power series \( \sum \frac{{a}_{n}}{n + 1}{z}^{n + 1} \) has radius of convergence \( R \) and if \( F \) denotes the sum of the latter, we have \( {F}^{\prime } = f \) on \( \rbrack  - R, R\lbrack \) .

- Si \( g \) est la somme d’une série entière \( \sum {b}_{n}{z}^{n} \) sur \( \left\{  {z,\left| z\right|  < {R}^{\prime }}\right\} \) (avec \( {R}^{\prime } > 0 \) ) et si \( f \) et \( g \) coïncident sur un voisinage de 0 dans \( \mathbb{R} \) , alors pour tout \( n,{b}_{n} = {g}^{\left( n\right) }\left( 0\right) /n! = \; {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) . Ceci reste valable si \( f \) et \( g \) coïncident sur un intervalle de la forme ]0, \( \alpha \) [.

> - If \( g \) is the sum of a power series \( \sum {b}_{n}{z}^{n} \) on \( \left\{  {z,\left| z\right|  < {R}^{\prime }}\right\} \) (with \( {R}^{\prime } > 0 \) ) and if \( f \) and \( g \) coincide on a neighborhood of 0 in \( \mathbb{R} \) , then for all \( n,{b}_{n} = {g}^{\left( n\right) }\left( 0\right) /n! = \; {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) . This remains valid if \( f \) and \( g \) coincide on an interval of the form ]0, \( \alpha \) [.

Remarque 4 (Dérivation par rapport à la variable complexe). On montre que les fonctions \( f \) définies par des séries entières sont dérivables par rapport à la variable complexe sur leur disque de convergence \( D \) , c’est-à-dire que pour tout \( {z}_{0} \in D \) , la limite de \( (f\left( {{z}_{0} + u}\right) - \; f\left( {z}_{0}\right) )/u \) existe lorsque \( u \) tend vers 0 dans \( \mathbb{C} \) en restant non nul.

> Remark 4 (Differentiation with respect to the complex variable). It can be shown that functions \( f \) defined by power series are differentiable with respect to the complex variable on their disk of convergence \( D \) , that is to say that for all \( {z}_{0} \in D \) , the limit of \( (f\left( {{z}_{0} + u}\right) - \; f\left( {z}_{0}\right) )/u \) exists as \( u \) tends to 0 in \( \mathbb{C} \) while remaining non-zero.

Comme on s’y attend, la dérivée de la restriction \( \widetilde{f} \) de \( f \) à l’axe réel et celle de \( f \) (au sens complexe) coincident sur \( \mathbb{R} \) .

> As expected, the derivative of the restriction \( \widetilde{f} \) of \( f \) to the real axis and that of \( f \) (in the complex sense) coincide on \( \mathbb{R} \) .

La condition de dérivabilité par rapport à la variable complexe est très forte. Il ne suffit pas qu'une fonction de \( \mathbb{C} \) dans \( \mathbb{C} \) soit différentiable pour qu'elle soit dérivable par rapport à la variable complexe (voir l'exercice 8 page 333), mais la réciproque est vraie. On peut montrer qu’une fonction \( g : D = \{ z,\left| z\right| < R\} \rightarrow \mathbb{C} \) continûment dérivable par rapport à la variable complexe sur \( D \) (on dit alors que \( g \) est holomorphe) est la somme d’une série entière sur \( D \) (voir l’exercice 13 page 265).

> The condition of differentiability with respect to the complex variable is very strong. It is not sufficient for a function from \( \mathbb{C} \) to \( \mathbb{C} \) to be differentiable for it to be differentiable with respect to the complex variable (see exercise 8 page 333), but the converse is true. It can be shown that a function \( g : D = \{ z,\left| z\right| < R\} \rightarrow \mathbb{C} \) continuously differentiable with respect to the complex variable on \( D \) (we then say that \( g \) is holomorphic) is the sum of a power series on \( D \) (see exercise 13 page 265).

##### Isolated zeros principle.

*Français : Principe des zéros isolés.*

THÉORÉME 3. Soit \( f \) la somme de la série entière \( \sum {a}_{n}{z}^{n} \) sur son disque de convergence. S’il existe une suite \( \left( {z}_{p}\right) \) de nombres complexes non nuls tendant vers 0 telle que \( f\left( {z}_{p}\right) = 0 \) pour tout \( p \) , alors \( {a}_{n} = 0 \) pour tout \( n \) .

> THEOREM 3. Let \( f \) be the sum of the power series \( \sum {a}_{n}{z}^{n} \) on its disk of convergence. If there exists a sequence \( \left( {z}_{p}\right) \) of non-zero complex numbers tending to 0 such that \( f\left( {z}_{p}\right) = 0 \) for all \( p \) , then \( {a}_{n} = 0 \) for all \( n \) .

Démonstration. Supposons que l’un des \( {a}_{n} \) ne soit pas nul, et notons \( q \) le plus petit entier naturel tel que \( {a}_{q} \neq 0 \) . On peut écrire, sur \( D \) ,

> Proof. Suppose that one of the \( {a}_{n} \) is non-zero, and let \( q \) be the smallest natural integer such that \( {a}_{q} \neq 0 \) . We can write, on \( D \) ,

\[
f\left( z\right)  = {z}^{q}g\left( z\right) \;\text{ avec }\;g\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n + q}{z}^{n}.
\]

D’après les hypothèses, \( g\left( {z}_{p}\right) = 0 \) pour tout \( p \) , et comme \( g \) est continue en 0 (c’est la somme d’une série entière de rayon de convergence \( R > 0 \) ), on a

> According to the hypotheses, \( g\left( {z}_{p}\right) = 0 \) for all \( p \) , and since \( g \) is continuous at 0 (it is the sum of a power series with radius of convergence \( R > 0 \) ), we have

\[
{a}_{q} = g\left( 0\right)  = \mathop{\lim }\limits_{{p \rightarrow   + \infty }}g\left( {z}_{p}\right)  = 0,
\]

ce qui est absurde. Donc \( {a}_{n} = 0 \) pour tout \( n \) .

> which is absurd. Therefore \( {a}_{n} = 0 \) for all \( n \) .

Conséquence : Si les sommes \( f \) et \( g \) de deux séries entières \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) vérifient \( f\left( {z}_{p}\right) = g\left( {z}_{p}\right) \) pour une suite \( \left( {z}_{p}\right) \) de nombres complexes non nuls tendant vers 0, alors \( {a}_{n} = {b}_{n} \) pour tout \( n \) (appliquer le théorème à \( f - g \) ). En particulier, deux séries entières dont les sommes coïncident sur un voisinage de 0 dans \( \mathbb{R} \) sont égales. On retrouve ainsi le résultat énoncé dans la conséquence du corollaire 1.

> Consequence: If the sums \( f \) and \( g \) of two power series \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \) satisfy \( f\left( {z}_{p}\right) = g\left( {z}_{p}\right) \) for a sequence \( \left( {z}_{p}\right) \) of non-zero complex numbers tending to 0, then \( {a}_{n} = {b}_{n} \) for all \( n \) (apply the theorem to \( f - g \) ). In particular, two power series whose sums coincide on a neighborhood of 0 in \( \mathbb{R} \) are equal. This recovers the result stated in the consequence of corollary 1.

Formule de Cauchy. La formule suivante n'est pas au programme des classes de mathématiques spéciales mais elle est d'une importance capitale. On s'en sert souvent dans les exercices et les problèmes.

> Cauchy's formula. The following formula is not in the mathematics special classes curriculum, but it is of capital importance. It is often used in exercises and problems.

\( \rightarrow \) THÉORÉME 4 (FORMULE DE CAUCHY). Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( R > 0 \) , et \( f \) la somme de cette série entière sur son disque de convergence. Alors

> \( \rightarrow \) THEOREM 4 (CAUCHY'S FORMULA). Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( R > 0 \) , and \( f \) be the sum of this power series on its disk of convergence. Then

\[
\forall r \in  \rbrack 0, R\lbrack ,\forall n \in  \mathbb{N},\;{2\pi }{r}^{n}{a}_{n} = {\int }_{0}^{2\pi }f\left( {r{e}^{i\theta }}\right) {e}^{-{ni\theta }}{d\theta }.
\]

Démonstration. Fixons \( r \in \rbrack 0, R\lbrack \) et \( n \in \mathbb{N} \) . Il suffit décrire

> Proof. Let us fix \( r \in \rbrack 0, R\lbrack \) and \( n \in \mathbb{N} \) . It suffices to write

\[
{\int }_{0}^{2\pi }f\left( {r{e}^{i\theta }}\right) {e}^{-{ni\theta }}{d\theta } = {\int }_{0}^{2\pi }\left( {\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{a}_{p}{r}^{p}{e}^{i\left( {p - n}\right) \theta }}\right) {d\theta } = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{a}_{p}{r}^{p}{\int }_{0}^{2\pi }{e}^{i\left( {p - n}\right) \theta }{d\theta }
\]

(*)

> (on a le droit d’inverser les signes de sommation car la série de fonctions \( \mathop{\sum }\limits_{p}{a}_{p}{r}^{p}{e}^{i\left( {p - n}\right) \theta } \) est normalement convergente sur \( \left\lbrack {0,{2\pi }}\right\rbrack \) , ceci parce que \( \sum \left| {a}_{p}\right| {r}^{p} \) converge, le réel \( r \) vérifiant \( 0 \leq \; r < R) \) . On conclut à partir de (*) en remarquant que \( {\int }_{0}^{2\pi }{e}^{i\left( {p - n}\right) \theta }{d\theta } = 0 \) si \( p \neq n, = {2\pi } \) si \( p = n \) .

(we are allowed to swap the summation signs because the series of functions \( \mathop{\sum }\limits_{p}{a}_{p}{r}^{p}{e}^{i\left( {p - n}\right) \theta } \) converges normally on \( \left\lbrack {0,{2\pi }}\right\rbrack \) , this is because \( \sum \left| {a}_{p}\right| {r}^{p} \) converges, with the real number \( r \) satisfying \( 0 \leq \; r < R) \) . We conclude from (*) by noting that \( {\int }_{0}^{2\pi }{e}^{i\left( {p - n}\right) \theta }{d\theta } = 0 \) if \( p \neq n, = {2\pi } \) if \( p = n \) .

> Égalité de Parseval. Le résultat qui suit est la version "série entière" du théorème 1 page 270 (en l’appliquant à la série trigonométrique \( f\left( {r{e}^{i\theta }}\right) \) ).

Parseval's identity. The following result is the "power series" version of theorem 1 on page 270 (by applying it to the trigonometric series \( f\left( {r{e}^{i\theta }}\right) \) ).

> THÉORÉME 5. Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( R > 0 \) , et \( f \) la somme de cette série entière sur son disque de convergence. Alors pour tout \( r \in \rbrack 0, R\lbrack \) , la série \( \sum {\left| {a}_{n}\right| }^{2}{r}^{2n} \) converge et on a

THEOREM 5. Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( R > 0 \) , and \( f \) be the sum of this power series on its disk of convergence. Then for all \( r \in \rbrack 0, R\lbrack \) , the series \( \sum {\left| {a}_{n}\right| }^{2}{r}^{2n} \) converges and we have

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left| {a}_{n}\right| }^{2}{r}^{2n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( r{e}^{i\theta }\right) \right| }^{2}{d\theta }.
\]
