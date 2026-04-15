#### 3.2. Expectation, variance, covariance

*Français : 3.2. Espérance, variance, covariance*

Espérance. La notion intuitive de moyenne (ou celle de centre de gravité), trouve une définition mathématique rigoureuse dans la notion d'espérance, dans la définition suivante.

> Expectation. The intuitive notion of average (or that of center of gravity) finds a rigorous mathematical definition in the notion of expectation, in the following definition.

DéFINITION 6 (ESPÉRANCE). Soit \( X \) une variable aléatoire discrète réelle sur \( \Omega \) . On dit que \( X \) admet une espérance (ou que \( X \) est d’espérance finie) si la famille \( ({xP}(X = \; x){)}_{x \in X\left( \Omega \right) } \) est sommable. Dans ce cas on appelle espérance de \( X \) la valeur notée \( E\left( X\right) \) définie par

> DEFINITION 6 (EXPECTATION). Let \( X \) be a discrete real random variable on \( \Omega \). We say that \( X \) admits an expectation (or that \( X \) has a finite expectation) if the family \( ({xP}(X = \; x){)}_{x \in X\left( \Omega \right) } \) is summable. In this case, the expectation of \( X \) is the value denoted by \( E\left( X\right) \) defined by

\[
E\left( X\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}{xP}\left( {X = x}\right) .
\]

Remarque 5. - Une variable aléatoire finie admet toujours une espérance.

> Remark 5. - A finite random variable always has an expectation.

— Une variable aléatoire bornée admet toujours une espérance.

> — A bounded random variable always has an expectation.

- La semi-convergence n'est pas suffisante pour admettre une espérance. En effet, l’ensemble \( X\left( \Omega \right) \) n’est pas ordonné, et la somme définissant l’espérance doit être indépendante de l'ordre de sommation.

> - Semi-convergence is not sufficient to have an expectation. Indeed, the set \( X\left( \Omega \right) \) is not ordered, and the sum defining the expectation must be independent of the order of summation.

— \( X \) admet une espérance si et seulement si \( \left| X\right| \) admet une espérance.

> — \( X \) has an expectation if and only if \( \left| X\right| \) has an expectation.

- Si \( A \subset  X\left( \Omega \right) \) , on a \( E\left( {\mathbf{1}}_{A}\right)  = P\left( A\right) \) en notant \( {\mathbf{1}}_{A} \) la fonction caractéristique de \( A \) .

> - If \( A \subset  X\left( \Omega \right) \) , we have \( E\left( {\mathbf{1}}_{A}\right)  = P\left( A\right) \) by denoting \( {\mathbf{1}}_{A} \) as the characteristic function of \( A \) .

— \( X \) est dite centrée si \( E\left( X\right) = 0 \) . Si \( X \) admet une espérance, alors la variable aléatoire \( X - E\left( X\right) \) également et \( X - E\left( X\right) \) est centrée.

> — \( X \) is said to be centered if \( E\left( X\right) = 0 \) . If \( X \) has an expectation, then the random variable \( X - E\left( X\right) \) does as well and \( X - E\left( X\right) \) is centered.

- On définit de même l’espérance d’un vecteur aléatoire discret \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) , il vérifie \( E\left( X\right)  = \left( {E\left( {X}_{1}\right) ,\ldots , E\left( {X}_{n}\right) }\right) \) . En particulier on peut définir l’espérance d'une variable aléatoire discrète à valeurs dans \( \mathbb{C} \) (ceci permettra plus tard de définir la fonction caractéristique de \( X \) , voir la définition 13 page 348).

> - The expectation of a discrete random vector \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) is defined similarly; it satisfies \( E\left( X\right)  = \left( {E\left( {X}_{1}\right) ,\ldots , E\left( {X}_{n}\right) }\right) \) . In particular, one can define the expectation of a discrete random variable taking values in \( \mathbb{C} \) (this will later allow defining the characteristic function of \( X \) , see definition 13 on page 348).

Proposition 4. Supposons \( \Omega \) fini ou dénombrable et soit \( X \) une variable aléatoire discrète réelle sur \( \Omega \) . Alors \( X \) admet une espérance si et seulement si la famille \( {\left( P\left( \{ \omega \} \right) X\left( \omega \right) \right) }_{\omega \in \Omega } \) est sommable, et on a alors

> Proposition 4. Suppose \( \Omega \) is finite or countable and let \( X \) be a real discrete random variable on \( \Omega \) . Then \( X \) has an expectation if and only if the family \( {\left( P\left( \{ \omega \} \right) X\left( \omega \right) \right) }_{\omega \in \Omega } \) is summable, and we then have

\[
E\left( X\right)  = \mathop{\sum }\limits_{{\omega  \in  \Omega }}P\left( {\{ \omega \} }\right) X\left( \omega \right) .
\]

Remarque 6. - Le résultat se généralise comme suit : si \( {\left( {A}_{n}\right) }_{n \in I} \) est une partition finie ou dénombrable de \( \Omega \) (où \( \Omega \) n’est pas supposé fini ou dénombrable) telle que \( X \) est constante sur chaque \( {A}_{n} \) ,égale à \( {x}_{n} \) , alors \( X \) admet une espérance si et seulement si \( {\left( P\left( {A}_{n}\right) {x}_{n}\right) }_{n \in I} \) est sommable, et on a

> Remark 6. - The result generalizes as follows: if \( {\left( {A}_{n}\right) }_{n \in I} \) is a finite or countable partition of \( \Omega \) (where \( \Omega \) is not assumed to be finite or countable) such that \( X \) is constant on each \( {A}_{n} \) , equal to \( {x}_{n} \) , then \( X \) has an expectation if and only if \( {\left( P\left( {A}_{n}\right) {x}_{n}\right) }_{n \in I} \) is summable, and we have

\[
E\left( X\right)  = \mathop{\sum }\limits_{{n \in  I}}{x}_{n}P\left( {A}_{n}\right) .
\]

La proposition précédente est un cas particulier de ce résultat lorsque \( \Omega \) est fini ou dénombrable, en choisissant \( I = \Omega \) et \( {A}_{n} = \{ n\} \) pour \( n \in \Omega \) .

> The previous proposition is a special case of this result when \( \Omega \) is finite or countable, by choosing \( I = \Omega \) and \( {A}_{n} = \{ n\} \) for \( n \in \Omega \) .

- Dans le cas d’une variable aléatoire réelle \( X \) admettant une densité \( f\left( x\right) \) , de sorte que \( P\left( {X \leq  x}\right)  = {\int }_{-\infty }^{x}f\left( t\right) {dt} \) (avec \( f \) continue sur \( \mathbb{R} \) sauf éventuellement en un nombre fini de points), si \( x \mapsto  {xf}\left( x\right) \) est intégrable sur \( \mathbb{R} \) , alors \( X \) admet une espérance définie par \( E\left( X\right)  = {\int }_{-\infty }^{+\infty }{xf}\left( x\right) {dx} \) . Ce résultat peut être vu comme une version continue de la formule de la proposition précédente.

> - In the case of a real random variable \( X \) admitting a density \( f\left( x\right) \) , such that \( P\left( {X \leq  x}\right)  = {\int }_{-\infty }^{x}f\left( t\right) {dt} \) (with \( f \) continuous on \( \mathbb{R} \) except possibly at a finite number of points), if \( x \mapsto  {xf}\left( x\right) \) is integrable on \( \mathbb{R} \) , then \( X \) has an expectation defined by \( E\left( X\right)  = {\int }_{-\infty }^{+\infty }{xf}\left( x\right) {dx} \) . This result can be seen as a continuous version of the formula from the previous proposition.

Proposition 5. Soient \( X \) et \( Y \) deux variables aléatoires discrètes réelles sur \( \Omega \) admettant une espérance. Alors

> Proposition 5. Let \( X \) and \( Y \) be two real discrete random variables on \( \Omega \) that have an expectation. Then

(i) \( X + Y \) admet une espérance qui vérifie \( E\left( {X + Y}\right) = E\left( X\right) + E\left( Y\right) \) ,

> (i) \( X + Y \) has an expectation that satisfies \( E\left( {X + Y}\right) = E\left( X\right) + E\left( Y\right) \) ,

(ii) pour tout \( \lambda \in \mathbb{R},{\lambda X} \) admet une espérance qui vérifie \( E\left( {\lambda X}\right) = {\lambda E}\left( X\right) \) ,

> (ii) for any \( \lambda \in \mathbb{R},{\lambda X} \) has an expectation that satisfies \( E\left( {\lambda X}\right) = {\lambda E}\left( X\right) \) ,

(iii) si \( X \geq 0 \) on a \( E\left( X\right) \geq 0 \) ,

> (iii) if \( X \geq 0 \) we have \( E\left( X\right) \geq 0 \) ,

(iv) si \( X \leq Y \) on a \( E\left( X\right) \leq E\left( Y\right) \) ,

> (iv) if \( X \leq Y \) we have \( E\left( X\right) \leq E\left( Y\right) \) ,

(v) on a \( \left| {E\left( X\right) }\right| \leq E\left( \left| X\right| \right) \) .

> (v) we have \( \left| {E\left( X\right) }\right| \leq E\left( \left| X\right| \right) \) .

(vi) Si \( X \) et \( Y \) sont indépendantes, \( {XY} \) admet une espérance et \( E\left( {XY}\right) = E\left( X\right) E\left( Y\right) \) .

> (vi) If \( X \) and \( Y \) are independent, \( {XY} \) has an expectation and \( E\left( {XY}\right) = E\left( X\right) E\left( Y\right) \) .

Remarque 7. - L’ensemble noté \( {\mathcal{L}}^{1}\left( {\Omega ,\mathbb{R}}\right) \) des variables aléatoires discrètes réelles sur \( \Omega \) est donc un espace vectoriel. L’espérance est une forme linéaire sur \( {\mathcal{L}}^{1}\left( {\Omega ,\mathbb{R}}\right) \) .

> Remark 7. - The set denoted \( {\mathcal{L}}^{1}\left( {\Omega ,\mathbb{R}}\right) \) of real discrete random variables on \( \Omega \) is therefore a vector space. The expectation is a linear form on \( {\mathcal{L}}^{1}\left( {\Omega ,\mathbb{R}}\right) \) .

- Si \( X \) et \( Y \) ne sont pas indépendantes, l’existence de \( E\left( {XY}\right) \) n’est pas garantie et le résultat (vi) est faux. La proposition 9 page 340 donne une condition suffisante d’existence de \( E\left( {XY}\right) \) et fournit une majoration de cette dernière.

> - If \( X \) and \( Y \) are not independent, the existence of \( E\left( {XY}\right) \) is not guaranteed and result (vi) is false. Proposition 9 on page 340 provides a sufficient condition for the existence of \( E\left( {XY}\right) \) and provides an upper bound for it.

- Les résultats (i), (ii) et (v) restent vrais sur les vecteurs aléatoires discrets (en remplaçant la valeur absolue par la norme pour (v)). La propriété (vi) reste vraie pour les variables aléatoires discrètes à valeur dans \( \mathbb{C} \) .

> - Results (i), (ii), and (v) remain true for discrete random vectors (replacing the absolute value with the norm for (v)). Property (vi) remains true for discrete random variables with values in \( \mathbb{C} \) .

PROPOSITION 6 (THÉORÉME DE TRANSFERT). Soit \( X \) une variable aléatoire discrète de \( \Omega \) sur \( E \) et \( f : E \rightarrow \mathbb{R} \) une fonction. La variable aléatoire discrete réelle \( f\left( X\right) \) admet une espérance si et seulement la famille \( {\left( f\left( x\right) P\left( X = x\right) \right) }_{x \in X\left( \Omega \right) } \) est sommable, et dans ce cas :

> PROPOSITION 6 (TRANSFER THEOREM). Let \( X \) be a discrete random variable from \( \Omega \) to \( E \) and \( f : E \rightarrow \mathbb{R} \) be a function. The real discrete random variable \( f\left( X\right) \) has an expectation if and only if the family \( {\left( f\left( x\right) P\left( X = x\right) \right) }_{x \in X\left( \Omega \right) } \) is summable, and in this case:

\[
E\left( {f\left( X\right) }\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}f\left( x\right) P\left( {X = x}\right) .
\]

Les résultats portant sur l'espérance qui suivent sont des compléments hors programme qu'il est utile de connaître.

> The following results concerning expectation are supplementary material outside the curriculum that are useful to know.

Proposition 7. Soit \( X : \Omega \rightarrow \mathbb{N} \) une variable aléatoire discrète. Alors \( X \) admet une espérance si et seulement si la famille \( {\left( P\left( X > n\right) \right) }_{n \in \mathbb{N}} \) est sommable, et on a

> Proposition 7. Let \( X : \Omega \rightarrow \mathbb{N} \) be a discrete random variable. Then \( X \) has an expectation if and only if the family \( {\left( P\left( X > n\right) \right) }_{n \in \mathbb{N}} \) is summable, and we have

\[
E\left( X\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {X > n}\right) .
\]

Démonstration. D'après le théorème de Fubini (cas particulier des résultats sur les familles som-mables), la somme double \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left( {\mathop{\sum }\limits_{{k > n}}P\left( {X = k}\right) }\right) \) converge absolument si et seulement si la somme double (obtenue par intervertion de sommation) \( \mathop{\sum }\limits_{{k > 0}}\left( {\mathop{\sum }\limits_{{n \in \mathbb{N}, n < k}}P\left( {X = k}\right) }\right) \) converge absolument, et alors les deux sommes sont égales. Comme \( \mathop{\sum }\limits_{{k > n}}P\left( {X = k}\right) = P\left( {X > n}\right) \) et \( \mathop{\sum }\limits_{{n \in \mathbb{N}, n < k}}P\left( {X = k}\right) = {kP}\left( k\right) \) , on en déduit que \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {X > n}\right) \) converge absolument si et seulement si \( \mathop{\sum }\limits_{{k > 0}}{kP}\left( k\right) \) converge absolument, et dans ce cas on a l’égalité des sommes, ce qui s’écrit \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {X > n}\right) = E\left( X\right) \) .

> Proof. According to Fubini's theorem (a special case of results on summable families), the double sum \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left( {\mathop{\sum }\limits_{{k > n}}P\left( {X = k}\right) }\right) \) converges absolutely if and only if the double sum (obtained by interchanging the order of summation) \( \mathop{\sum }\limits_{{k > 0}}\left( {\mathop{\sum }\limits_{{n \in \mathbb{N}, n < k}}P\left( {X = k}\right) }\right) \) converges absolutely, and in that case, the two sums are equal. Since \( \mathop{\sum }\limits_{{k > n}}P\left( {X = k}\right) = P\left( {X > n}\right) \) and \( \mathop{\sum }\limits_{{n \in \mathbb{N}, n < k}}P\left( {X = k}\right) = {kP}\left( k\right) \) , we deduce that \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {X > n}\right) \) converges absolutely if and only if \( \mathop{\sum }\limits_{{k > 0}}{kP}\left( k\right) \) converges absolutely, and in this case, the sums are equal, which is written as \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {X > n}\right) = E\left( X\right) \) .

Exemple 2. Soit \( m, n \in {\mathbb{N}}^{ * }, m \leq n \) , et \( Y \) une variable aléatoire sur \( \Omega = {\mathcal{P}}_{m}\left( {\{ 1,\ldots , n\} }\right) \) (ensemble des parties de \( \{ 1,\ldots , n\} \) à \( m \) éléments), muni d’une loi équiprobable, définie par \( Y = \min \omega \) . Nous souhaitons calculer \( E\left( Y\right) \) . La proposition précédente entraîne

> Example 2. Let \( m, n \in {\mathbb{N}}^{ * }, m \leq n \) , and \( Y \) be a random variable on \( \Omega = {\mathcal{P}}_{m}\left( {\{ 1,\ldots , n\} }\right) \) (the set of subsets of \( \{ 1,\ldots , n\} \) with \( m \) elements), equipped with a uniform probability distribution, defined by \( Y = \min \omega \) . We wish to calculate \( E\left( Y\right) \) . The previous proposition implies

\[
E\left( Y\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {Y > k}\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{matrix} n - k \\  m \end{matrix}\right) {\left( \begin{array}{l} n \\  m \end{array}\right) }^{-1} = \left( \begin{matrix} n + 1 \\  m + 1 \end{matrix}\right) {\left( \begin{array}{l} n \\  m \end{array}\right) }^{-1} = \frac{n + 1}{m + 1}
\]

(où nous avons utilisé la dernière assertion de la proposition 11 page 303).

> (where we used the last assertion of proposition 11 on page 303).

DÉFINITION 7. Soit \( A \) un événement non négligeable et \( X \) une variable aléatoire discrète réelle sur \( \Omega \) . On dit que \( X \) admet une espérance conditionnelle sachant \( A \) si \( X \) admet une espérance pour la loi de probabilité \( {P}_{A} \) , c’est-à-dire si la série

> DEFINITION 7. Let \( A \) be a non-negligible event and \( X \) be a real discrete random variable on \( \Omega \) . We say that \( X \) admits a conditional expectation given \( A \) if \( X \) admits an expectation for the probability distribution \( {P}_{A} \) , that is, if the series

\[
\mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}x{P}_{A}\left( {X = x}\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}{xP}\left( {X = x \mid  A}\right) ,
\]

est absolument convergente, et on note alors sa somme \( E\left( {X \mid A}\right) \) , appelée espérance conditionnelle de \( X \) sachant \( A \) .

> is absolutely convergent, and we then denote its sum by \( E\left( {X \mid A}\right) \) , called the conditional expectation of \( X \) given \( A \) .

Proposition 8. Soit \( {\left( {A}_{n}\right) }_{n \in I} \) une partition finie ou dénombrable d’événements non né- gligeables de \( \Omega \) , et \( X \) une variable aléatoire discrète réelle sur \( \Omega \) admettant une espérance. Alors pour tout \( n \in I, X \) admet une espérance conditionnelle sachant \( {A}_{n} \) et on a

> Proposition 8. Let \( {\left( {A}_{n}\right) }_{n \in I} \) be a finite or countable partition of non-negligible events of \( \Omega \) , and \( X \) be a real discrete random variable on \( \Omega \) admitting an expectation. Then for all \( n \in I, X \) , it admits a conditional expectation given \( {A}_{n} \) and we have

\[
E\left( X\right)  = \mathop{\sum }\limits_{{n \in  I}}E\left( {X \mid  {A}_{n}}\right) P\left( {A}_{n}\right) .
\]

Démonstration. Pour tout \( n \in I \) , la famille \( {\left( xP\left( X = x \mid {A}_{n}\right) P\left( {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) } \) est sommable car \( P\left( {X = x \mid {A}_{n}}\right) P\left( {A}_{n}\right) = P\left( {\{ X = x\} \cap {A}_{n}}\right) \leq P\left( {X = x}\right) \) , donc \( {\left( xP\left( X = x \mid {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) } \) est sommable ce qui assure l’existence de l’espérance conditionnelle de \( X \) sachant \( {A}_{n} \) . Or

> Proof. For any \( n \in I \), the family \( {\left( xP\left( X = x \mid {A}_{n}\right) P\left( {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) } \) is summable because \( P\left( {X = x \mid {A}_{n}}\right) P\left( {A}_{n}\right) = P\left( {\{ X = x\} \cap {A}_{n}}\right) \leq P\left( {X = x}\right) \), therefore \( {\left( xP\left( X = x \mid {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) } \) is summable, which ensures the existence of the conditional expectation of \( X \) given \( {A}_{n} \). Now

\[
\forall x \in  X\left( \Omega \right) ,\;\mathop{\sum }\limits_{{n \in  I}}P\left( {X = x \mid  {A}_{n}}\right) P\left( {A}_{n}\right)  = \mathop{\sum }\limits_{{n \in  I}}P\left( {\{ X = x\}  \cap  {A}_{n}}\right)  = P\left( {X = x}\right) ,
\]

et comme \( X \) admet une espérance on en déduit que \( {\left( xP\left( X = x \mid {A}_{n}\right) P\left( {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) , n \in I} \) est sommable. Le théorème de Fubini permet d'intervertir les signe de sommation, ce qui donne

> and since \( X \) has an expectation, we deduce that \( {\left( xP\left( X = x \mid {A}_{n}\right) P\left( {A}_{n}\right) \right) }_{x \in X\left( \Omega \right) , n \in I} \) is summable. Fubini's theorem allows us to interchange the summation signs, which gives

\[
\mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}{xP}\left( {X = x}\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}\mathop{\sum }\limits_{{n \in  I}}{xP}\left( {X = x \mid  {A}_{n}}\right) P\left( {A}_{n}\right)  = \mathop{\sum }\limits_{{n \in  I}}\mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}{xP}\left( {X = x \mid  {A}_{n}}\right) P\left( {A}_{n}\right) .
\]

Le terme de gauche est égal à \( E\left( X\right) \) , celui de droite à \( \mathop{\sum }\limits_{{n \in I}}E\left( {X \mid {A}_{n}}\right) P\left( {A}_{n}\right) \) , d’où le résultat.

> The term on the left is equal to \( E\left( X\right) \), the one on the right to \( \mathop{\sum }\limits_{{n \in I}}E\left( {X \mid {A}_{n}}\right) P\left( {A}_{n}\right) \), hence the result.

Moment. Avant d'introduire la variance, il est commode d'introduire les moments d'une variable aléatoire, et de montrer que l’ensemble \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) des variables aléatoires de carré sommable est un espace vectoriel.

> Moment. Before introducing variance, it is convenient to introduce the moments of a random variable and to show that the set \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) of square-summable random variables is a vector space.

DéFINITION 8 (MOMENT). Soit \( p \in {\mathbb{N}}^{ * } \) et \( X \) une variable aléatoire discrète réelle sur \( \Omega \) . On dit que \( X \) admet un moment d’ordre \( p \) lorsque \( {X}^{p} \) est sommable (c’est-à-dire lorsque la famille \( {\left( {x}^{p}P\left( X = x\right) \right) }_{x \in X\left( \Omega \right) } \) est sommable), ce qui équivaut à dire que \( {X}^{p} \) admet une espérance. On appelle alors moment d’ordre \( p \) de \( X \) la valeur

> DEFINITION 8 (MOMENT). Let \( p \in {\mathbb{N}}^{ * } \) and \( X \) be a real discrete random variable on \( \Omega \). We say that \( X \) has a moment of order \( p \) when \( {X}^{p} \) is summable (that is, when the family \( {\left( {x}^{p}P\left( X = x\right) \right) }_{x \in X\left( \Omega \right) } \) is summable), which is equivalent to saying that \( {X}^{p} \) has an expectation. The moment of order \( p \) of \( X \) is then called the value

\[
E\left( {X}^{p}\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}{x}^{p}P\left( {X = x}\right) .
\]

Remarque 8. - L’équivalence entre " \( {X}^{p} \) sommable" et " \( {X}^{p} \) admet une espérance" est une conséquence du théorème de transfert, ainsi que la formule de \( E\left( {X}^{p}\right) \) .

> Remark 8. - The equivalence between "\( {X}^{p} \) is summable" and "\( {X}^{p} \) has an expectation" is a consequence of the transfer theorem, as is the formula for \( E\left( {X}^{p}\right) \).

- Si \( X \) admet un moment d’ordre \( p \in  {\mathbb{N}}^{ * } \) , alors \( X \) admet un moment d’ordre \( q \) pour tout \( q \leq  p \) (ceci est une conséquence de l’inégalité \( {\left| X\right| }^{q} \leq  1 + {\left| X\right| }^{p} \) dès que \( q \leq  p \) .)

> - If \( X \) has a moment of order \( p \in  {\mathbb{N}}^{ * } \), then \( X \) has a moment of order \( q \) for any \( q \leq  p \) (this is a consequence of the inequality \( {\left| X\right| }^{q} \leq  1 + {\left| X\right| }^{p} \) as soon as \( q \leq  p \).)

- Ainsi, si \( X \) admet un moment d’ordre \( p \in  {\mathbb{N}}^{ * }, X \) admet un moment factoriel \( E\left( {X\left( {X - 1}\right) \cdots \left( {X - p + 1}\right) }\right) . \)

> - Thus, if \( X \) has a moment of order \( p \in  {\mathbb{N}}^{ * }, X \), it has a factorial moment \( E\left( {X\left( {X - 1}\right) \cdots \left( {X - p + 1}\right) }\right) . \)

Proposition 9. Soient \( X \) et \( Y \) deux variables aléatoires discrètes réelles sur \( \Omega \) , possédant un moment d'ordre 2. Alors \( {XY} \) admet une espérance, et on a

> Proposition 9. Let \( X \) and \( Y \) be two real discrete random variables on \( \Omega \) possessing a second-order moment. Then \( {XY} \) admits an expectation, and we have

\[
\left| {E\left( {XY}\right) }\right|  \leq  E{\left( {X}^{2}\right) }^{1/2}E{\left( {Y}^{2}\right) }^{1/2}.
\]

Démonstration. On peut démontrer l'inégalité directement à partir de l'expression de \( E\left( {XY}\right) \) sous forme d'une série mais nous proposons une preuve plus élégante qui s'appuie sur l'inégalité de Schwarz des formes quadratiques positives.

> Proof. One can prove the inequality directly from the expression of \( E\left( {XY}\right) \) in the form of a series, but we propose a more elegant proof based on the Schwarz inequality for positive quadratic forms.

L’inégalité \( \left| {XY}\right| \leq \left( {{X}^{2} + {Y}^{2}}\right) /2 \) assure que \( {XY} \) admet bien une espérance. En particulier si \( X, Y \) admettent un moment d’ordre 2, l’égalité \( {\left( X + Y\right) }^{2} = {X}^{2} + {2XY} + {Y}^{2} \) montre que \( X + Y \) admet également un moment d’ordre 2. Si \( X \) admet un moment d’ordre \( 2,{\lambda X} \) également, pour \( \lambda \in \mathbb{R} \) . Ainsi l’ensemble \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) des variables aléatoires discrètes réelles est un espace vectoriel.

> The inequality \( \left| {XY}\right| \leq \left( {{X}^{2} + {Y}^{2}}\right) /2 \) ensures that \( {XY} \) indeed admits an expectation. In particular, if \( X, Y \) admit a second-order moment, the equality \( {\left( X + Y\right) }^{2} = {X}^{2} + {2XY} + {Y}^{2} \) shows that \( X + Y \) also admits a second-order moment. If \( X \) admits a moment of order \( 2,{\lambda X} \) as well, for \( \lambda \in \mathbb{R} \) . Thus, the set \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) of real discrete random variables is a vector space.

L’application \( \varphi : {\left( {\mathcal{L}}^{2}\left( \Omega ,\mathbb{R}\right) \right) }^{2} \rightarrow \mathbb{R}\;\left( {A, B}\right) \mapsto E\left( {AB}\right) \) est bilinéaire et la forme quadratique associée \( \Phi \left( A\right) = E\left( {A}^{2}\right) \) est positive. On peut donc appliquer l’inégalité de Schwarz (voir le théorème 3 page 246) qui s’écrit \( \varphi {\left( X, Y\right) }^{2} \leq \Phi \left( X\right) \Phi \left( Y\right) \) , d’où le résultat.

> The mapping \( \varphi : {\left( {\mathcal{L}}^{2}\left( \Omega ,\mathbb{R}\right) \right) }^{2} \rightarrow \mathbb{R}\;\left( {A, B}\right) \mapsto E\left( {AB}\right) \) is bilinear and the associated quadratic form \( \Phi \left( A\right) = E\left( {A}^{2}\right) \) is positive. We can therefore apply the Schwarz inequality (see theorem 3 page 246) which is written \( \varphi {\left( X, Y\right) }^{2} \leq \Phi \left( X\right) \Phi \left( Y\right) \) , hence the result.

Remarque 9. Comme démontré dans la preuve de cette proposition, l’ensemble \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) des variables aléatoires discrètes réelles sur \( \Omega \) qui admettent un moment d’ordre 2, est un espace vectoriel. De plus, cette proposition entraîne que \( X \mapsto E{\left( {X}^{2}\right) }^{1/2} \) est une semi-norme sur \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) (on a \( E\left( {X}^{2}\right) = 0 \) si et seulement si \( X = 0 \) presque surement).

> Remark 9. As demonstrated in the proof of this proposition, the set \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) of real discrete random variables on \( \Omega \) that admit a second-order moment is a vector space. Furthermore, this proposition implies that \( X \mapsto E{\left( {X}^{2}\right) }^{1/2} \) is a semi-norm on \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) (we have \( E\left( {X}^{2}\right) = 0 \) if and only if \( X = 0 \) almost surely).

Variance. L'espérance donne la valeur moyenne d'une variable aléatoire, mais ne mesure pas sa dispersion autour de celle ci. Pour celà, on introduit la notion de variance, qui est la moyenne du carré de l'écart de la variable par rapport à sa moyenne.

> Variance. The expectation gives the average value of a random variable but does not measure its dispersion around it. For this, we introduce the notion of variance, which is the mean of the square of the deviation of the variable from its mean.

DéFINITION 9 (VARIANCE,ÉCART TYPE). Soit \( X \) une variable aléatoire discrète réelle sur \( \Omega \) , admettant un moment d’ordre 2. On appelle variance de \( X \) la valeur notée \( V\left( X\right) \) ou encore Var \( \left( X\right) \) définie par

> DEFINITION 9 (VARIANCE, STANDARD DEVIATION). Let \( X \) be a real discrete random variable on \( \Omega \) admitting a second-order moment. We call the variance of \( X \) the value denoted \( V\left( X\right) \) or Var \( \left( X\right) \) defined by

\[
V\left( X\right)  = E\left( {\left( X - E\left( X\right) \right) }^{2}\right) ,
\]

et on appelle écart type de \( X \) la valeur \( \sigma \left( X\right) = \sqrt{V\left( X\right) } \) .

> and we call the standard deviation of \( X \) the value \( \sigma \left( X\right) = \sqrt{V\left( X\right) } \) .

Remarque 10. - Une variable aléatoire admet une variance si elle admet un moment d'ordre 2. D'après la remarque 8, si \( X \) admet une variance alors elle admet une espérance.

> Remark 10. - A random variable admits a variance if it admits a second-order moment. According to remark 8, if \( X \) admits a variance, then it admits an expectation.

- On dit qu’une variable aléatoire discrète réelle \( X \) est centrée si \( E\left( X\right)  = 0 \) , réduite si \( V\left( X\right)  = 1 \) . Pour toute variable aléatoire discrète réelle \( X \) de variance non nulle, la variable aléatoire \( {X}^{ * } = \left( {X - E\left( X\right) }\right) /\sigma \left( X\right) \) est centrée réduite.

> - A real discrete random variable \( X \) is said to be centered if \( E\left( X\right)  = 0 \) , and reduced if \( V\left( X\right)  = 1 \) . For any real discrete random variable \( X \) with non-zero variance, the random variable \( {X}^{ * } = \left( {X - E\left( X\right) }\right) /\sigma \left( X\right) \) is centered and reduced.

Proposition 10. Soit \( X \) une variable aléatoire discrète réelle, admettant un moment d'ordre 2. Alors

> Proposition 10. Let \( X \) be a real discrete random variable admitting a second-order moment. Then

(i) On a \( V\left( {X}^{2}\right) = E\left( {X}^{2}\right) - E{\left( X\right) }^{2} \) (Théorème de Köenig-Huygens).

> (i) We have \( V\left( {X}^{2}\right) = E\left( {X}^{2}\right) - E{\left( X\right) }^{2} \) (Köenig-Huygens theorem).

(ii) Pour tout \( a, b \in \mathbb{R}, V\left( {{aX} + b}\right) = {a}^{2}V\left( X\right) \) .

> (ii) For any \( a, b \in \mathbb{R}, V\left( {{aX} + b}\right) = {a}^{2}V\left( X\right) \) .

Covariance.

> Covariance.

DéFINITION 10. Soient \( X \) et \( Y \) deux variables aléatoires discrètes réelles, admettant un moment d’ordre 2. On appelle covariance de \( X \) et \( Y \) la valeur notée \( \operatorname{Cov}\left( {XY}\right) \) définie par

> DEFINITION 10. Let \( X \) and \( Y \) be two real discrete random variables admitting a second-order moment. The covariance of \( X \) and \( Y \) is the value denoted by \( \operatorname{Cov}\left( {XY}\right) \) defined as

\[
\operatorname{Cov}\left( {X, Y}\right)  = E\left( {\left( {X - E\left( X\right) }\right) \left( {Y - E\left( Y\right) }\right) }\right) .
\]

Remarque 11. - On a \( \operatorname{Cov}\left( {X, X}\right) = V\left( X\right) \) .

> Remark 11. - We have \( \operatorname{Cov}\left( {X, X}\right) = V\left( X\right) \) .

- Si \( \operatorname{Cov}\left( {X, Y}\right)  > 0, X \) et \( Y \) ont "tendance" à être du même coté de leur espérance respective. Lorsque \( \operatorname{Cov}\left( {X, Y}\right)  = 0 \) on dit que les variables \( X \) et \( Y \) sont décorrélées. Le résultat plus bas affirme que les variables \( X \) et \( Y \) sont décorrélées si elles sont indépendantes, mais la réciproque est fausse.

> - If \( \operatorname{Cov}\left( {X, Y}\right)  > 0, X \) and \( Y \) have a "tendency" to be on the same side of their respective expectations. When \( \operatorname{Cov}\left( {X, Y}\right)  = 0 \) , the variables \( X \) and \( Y \) are said to be uncorrelated. The result below states that the variables \( X \) and \( Y \) are uncorrelated if they are independent, but the converse is false.

Proposition 11. Soient \( X \) et \( Y \) deux variables aléatoires discrètes réelles, admettant un moment d'ordre 2. Alors

> Proposition 11. Let \( X \) and \( Y \) be two real discrete random variables admitting a second-order moment. Then

(i) On a \( \operatorname{Cov}\left( {X, Y}\right) = E\left( {XY}\right) - E\left( X\right) E\left( Y\right) \) .

> (i) We have \( \operatorname{Cov}\left( {X, Y}\right) = E\left( {XY}\right) - E\left( X\right) E\left( Y\right) \) .

(ii) L’application \( \left( {X, Y}\right) \mapsto \operatorname{Cov}\left( {X, Y}\right) \) est bilinéaire symétrique sur \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) .

> (ii) The mapping \( \left( {X, Y}\right) \mapsto \operatorname{Cov}\left( {X, Y}\right) \) is symmetric bilinear on \( {\mathcal{L}}^{2}\left( {\Omega ,\mathbb{R}}\right) \) .

(iii) Si \( X \) et \( Y \) sont indépendantes, on a \( \operatorname{Cov}\left( {X, Y}\right) = 0 \) .

> (iii) If \( X \) and \( Y \) are independent, we have \( \operatorname{Cov}\left( {X, Y}\right) = 0 \) .

(iv) On a \( \left| {\operatorname{Cov}\left( {X, Y}\right) }\right| \leq \sigma \left( X\right) \sigma \left( Y\right) \) . Si \( \sigma \left( X\right) \sigma \left( Y\right) \neq 0 \) , le coefficient de corrélation de \( X \) et \( Y \) , défini par \( \rho \left( {X, Y}\right) = \frac{\operatorname{Cov}\left( {X, Y}\right) }{\sigma \left( X\right) \sigma \left( Y\right) } \) , vérifie \( - 1 \leq \rho \left( {X, Y}\right) \leq 1 \) .

> (iv) We have \( \left| {\operatorname{Cov}\left( {X, Y}\right) }\right| \leq \sigma \left( X\right) \sigma \left( Y\right) \) . If \( \sigma \left( X\right) \sigma \left( Y\right) \neq 0 \) , the correlation coefficient of \( X \) and \( Y \) , defined by \( \rho \left( {X, Y}\right) = \frac{\operatorname{Cov}\left( {X, Y}\right) }{\sigma \left( X\right) \sigma \left( Y\right) } \) , satisfies \( - 1 \leq \rho \left( {X, Y}\right) \leq 1 \) .

(v) On a \( V\left( {X + Y}\right) = V\left( X\right) + V\left( Y\right) + 2\operatorname{Cov}\left( {X, Y}\right) \) . En particulier si \( X \) et \( Y \) sont indépendantes, on a \( V\left( {X + Y}\right) = V\left( X\right) + V\left( Y\right) \) .

> (v) We have \( V\left( {X + Y}\right) = V\left( X\right) + V\left( Y\right) + 2\operatorname{Cov}\left( {X, Y}\right) \) . In particular, if \( X \) and \( Y \) are independent, we have \( V\left( {X + Y}\right) = V\left( X\right) + V\left( Y\right) \) .

Proposition 12. Soit \( n \in {\mathbb{N}}^{ * } \) et \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) un vecteur aléatoire discret à valeurs dans \( {\mathbb{R}}^{n} \) . On appelle matrice de covariance de \( {X}_{1},\ldots ,{X}_{n} \) la matrice symétrique \( n \times n \) définie par

> Proposition 12. Let \( n \in {\mathbb{N}}^{ * } \) and \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) be a discrete random vector with values in \( {\mathbb{R}}^{n} \) . The covariance matrix of \( {X}_{1},\ldots ,{X}_{n} \) is the symmetric matrix \( n \times n \) defined by

\[
V\left( X\right)  = {\left( \operatorname{Cov}\left( {X}_{i},{X}_{j}\right) \right) }_{1 \leq  i, j \leq  n}.
\]

Alors

> Then

- Pour tout \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \in  {\mathbb{R}}^{n} \) et \( \left( {{\mu }_{1},\ldots ,{\mu }_{n}}\right)  \in  {\mathbb{R}}^{n} \) on a

> - For all \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \in  {\mathbb{R}}^{n} \) and \( \left( {{\mu }_{1},\ldots ,{\mu }_{n}}\right)  \in  {\mathbb{R}}^{n} \) we have

\[
\operatorname{Cov}\left( {{\lambda }_{1}{X}_{1} + \cdots  + {\lambda }_{n}{X}_{n},{\mu }_{1}{X}_{1} + \cdots  + {\mu }_{n}{X}_{n}}\right)  = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) V\left( X\right) \left( \begin{matrix} {\mu }_{1} \\  \vdots \\  {\mu }_{n} \end{matrix}\right) .
\]

- Pour tout \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \in  {\mathbb{R}}^{n} \) on a

> - For all \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \in  {\mathbb{R}}^{n} \) we have

\[
V\left( {{\lambda }_{1}{X}_{1} + \cdots  + {\lambda }_{n}{X}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{2}V\left( {X}_{i}\right)  + 2\mathop{\sum }\limits_{{1 \leq  i < j \leq  n}}{\lambda }_{i}{\lambda }_{j}\operatorname{Cov}\left( {{X}_{i},{X}_{j}}\right)
\]

\[
= \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) V\left( X\right) \left( \begin{matrix} {\lambda }_{1} \\  \vdots \\  {\lambda }_{n} \end{matrix}\right) .
\]

- Si les variables \( {X}_{1},\ldots ,{X}_{n} \) sont indépendantes deux à deux, on a

> - If the variables \( {X}_{1},\ldots ,{X}_{n} \) are pairwise independent, we have

\[
V\left( {{X}_{1} + \cdots  + {X}_{n}}\right)  = V\left( {X}_{1}\right)  + \cdots  + V\left( {X}_{n}\right) .
\]
