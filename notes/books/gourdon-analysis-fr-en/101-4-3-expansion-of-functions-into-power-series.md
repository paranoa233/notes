#### 4.3. Expansion of functions into power series

*Français : 4.3. Développement de fonctions en séries entières*

Une fonction (de la variable réelle ou complexe) à valeurs complexes définie dans un voisinage de 0 est dite développable en série entière sur un voisinage de 0 si sur ce voisinage, \( f \) coincide avec la somme d’une série entière de rayon de convergence non nul.

> A function (of a real or complex variable) with complex values defined in a neighborhood of 0 is said to be expandable as a power series on a neighborhood of 0 if, on this neighborhood, \( f \) coincides with the sum of a power series with a non-zero radius of convergence.

Développement en série entière des fractions rationnelles. Soit \( F \) une fraction rationnelle à coefficients dans \( \mathbb{C} \) . Si \( 0\mathrm{n} \) ’est pas un pôle de \( F \) , nous voulons développer \( F \) en série entière. Après décomposition en éléments simples de \( F \) , on se ramène à développer en série entière les fractions de la forme \( 1/{\left( z - {z}_{0}\right) }^{p} \) où \( p \in {\mathbb{N}}^{ * } \) et \( {z}_{0} \neq 0 \) .

> Power series expansion of rational functions. Let \( F \) be a rational function with coefficients in \( \mathbb{C} \) . If \( 0\mathrm{n} \) is not a pole of \( F \) , we want to expand \( F \) into a power series. After decomposing \( F \) into partial fractions, we reduce the problem to expanding fractions of the form \( 1/{\left( z - {z}_{0}\right) }^{p} \) where \( p \in {\mathbb{N}}^{ * } \) and \( {z}_{0} \neq 0 \) .

Pour tout \( z \in \mathbb{C} \) tel que \( \left| z\right| < \left| {z}_{0}\right| \) , on a

> For any \( z \in \mathbb{C} \) such that \( \left| z\right| < \left| {z}_{0}\right| \) , we have

\[
\frac{1}{z - {z}_{0}} =  - \frac{1}{{z}_{0}}\frac{1}{1 - z/{z}_{0}} =  - \frac{1}{{z}_{0}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( \frac{z}{{z}_{0}}\right) }^{n}.
\]

Par produit de Cauchy, on voit donc que pour tout \( p \in {\mathbb{N}}^{ * },1/{\left( z - {z}_{0}\right) }^{p} \) est développable en série entière. Pour obtenir son développement en série entière, on dérive \( \left( {p - 1}\right) \) fois \( 1/\left( {x - {z}_{0}}\right) \) sur \( \rbrack - \left| {z}_{0}\right| ,\left| {z}_{0}\right| \lbrack \) , ce qui donne

> By the Cauchy product, we see that for any \( p \in {\mathbb{N}}^{ * },1/{\left( z - {z}_{0}\right) }^{p} \) is expandable as a power series. To obtain its power series expansion, we differentiate \( \left( {p - 1}\right) \) times \( 1/\left( {x - {z}_{0}}\right) \) on \( \rbrack - \left| {z}_{0}\right| ,\left| {z}_{0}\right| \lbrack \) , which gives

\[
\forall x \in  \rbrack  - \left| {z}_{0}\right| ,\left| {z}_{0}\right| \left\lbrack  \right. ,\;\frac{1}{{\left( x - {z}_{0}\right) }^{p}} = \frac{{\left( -1\right) }^{p}}{{z}_{0}^{p}\left( {p - 1}\right) !}\mathop{\sum }\limits_{{n = p - 1}}^{{+\infty }}\frac{n!}{\left( {n - p + 1}\right) !}{\left( \frac{x}{{z}_{0}}\right) }^{n - p + 1},
\]

et comme ces deux expressions coïncident sur un voisinage de 0 dans \( \mathbb{R} \) , elles coïncident sur tout le disque de convergence \( \left| z\right| < \left| {z}_{0}\right| \) (voir la conséquence du corollaire 1).

> and since these two expressions coincide on a neighborhood of 0 in \( \mathbb{R} \) , they coincide on the entire disk of convergence \( \left| z\right| < \left| {z}_{0}\right| \) (see the consequence of corollary 1).

Ainsi, toute fraction rationnelle complexe \( F \) dont 0 n’est pas un pôle est développable en série entière au voisinage de 0. On peut montrer que le rayon de convergence de cette dernière est égal au plus petit des modules des pôles de \( F \) .

> Thus, any complex rational function \( F \) for which 0 is not a pole is expandable as a power series in the neighborhood of 0. It can be shown that the radius of convergence of the latter is equal to the smallest of the moduli of the poles of \( F \) .

Développement en série entière d'une fonction à variable réelle. Soit \( f \) une fonction complexe de la variable réelle définie sur un voisinage de 0. Si \( f \) est développable en série entière, il existe \( \alpha > 0 \) tel que sur \( \rbrack - \alpha ,\alpha \lbrack \) , \( f \) coincide avec la somme d’une série entière \( \sum {a}_{n}{z}^{n} \) de rayon de convergence \( \geq \alpha \) . Ceci implique que \( f \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \rbrack - \alpha ,\alpha \left\lbrack \right. \) et que \( {a}_{n} = {f}^{\left( n\right) }\left( 0\right) /n! \) pour tout \( n \) . Ceci constitue la condition nécessaire de la proposition qui suit.

> Power series expansion of a real-variable function. Let \( f \) be a complex function of a real variable defined on a neighborhood of 0. If \( f \) is expandable as a power series, there exists \( \alpha > 0 \) such that on \( \rbrack - \alpha ,\alpha \lbrack \) , \( f \) coincides with the sum of a power series \( \sum {a}_{n}{z}^{n} \) with radius of convergence \( \geq \alpha \) . This implies that \( f \) is of class \( {\mathcal{C}}^{\infty } \) on \( \rbrack - \alpha ,\alpha \left\lbrack \right. \) and that \( {a}_{n} = {f}^{\left( n\right) }\left( 0\right) /n! \) for all \( n \) . This constitutes the necessary condition of the following proposition.

\( \rightarrow \) Proposition 4. Soit I un intervalle de \( \mathbb{R} \) contenant un voisinage de 0. Une fonction \( f : I \rightarrow \mathbb{C} \) de classe \( {\mathcal{C}}^{\infty } \) est développable en série entière sur un voisinage de 0 si et seulement s’il existe \( \alpha > 0 \) tel que la suite de fonctions \( \left( {R}_{n}\right) \) définie par

> \( \rightarrow \) Proposition 4. Let I be an interval of \( \mathbb{R} \) containing a neighborhood of 0. A function \( f : I \rightarrow \mathbb{C} \) of class \( {\mathcal{C}}^{\infty } \) is expandable as a power series in a neighborhood of 0 if and only if there exists \( \alpha > 0 \) such that the sequence of functions \( \left( {R}_{n}\right) \) defined by

\[
{R}_{n}\left( x\right)  = f\left( x\right)  - \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{f}^{\left( k\right) }\left( 0\right) }{k!}{x}^{k}
\]

tende simplement vers0sur \( \rbrack - \alpha ,\alpha \lbrack \) . La série entière

> converges pointwise to 0 on \( \rbrack - \alpha ,\alpha \lbrack \) . The power series

\[
\sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n}
\]

(*)

> a alors un rayon de convergence \( \geq \alpha \) et \( f \) est égale à la somme de cette série entière sur \( \rbrack - \alpha ,\alpha \lbrack \) .

then has a radius of convergence \( \geq \alpha \) and \( f \) is equal to the sum of this power series on \( \rbrack - \alpha ,\alpha \lbrack \) .

> Démonstration. Pour tout \( x \in \rbrack - \alpha ,\alpha \left\lbrack \right. \) la série \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{x}^{n} \) converge vers \( f\left( x\right) \) car \( {R}_{n}\left( x\right) \rightarrow 0 \) . En particulier, la suite \( \left( {{f}^{\left( n\right) }\left( 0\right) {x}^{n}/n!}\right) \) tend vers 0, donc est bornée, donc la série entière (*) a un rayon de convergence \( \geq \left| x\right| \) (voir la définition 2). Ceci étant vrai pour tout \( x \in \rbrack - \alpha ,\alpha \lbrack \) , on en déduit que le rayon de convergence de (*) est \( \geq \alpha \) .

Proof. For any \( x \in \rbrack - \alpha ,\alpha \left\lbrack \right. \), the series \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{x}^{n} \) converges to \( f\left( x\right) \) because \( {R}_{n}\left( x\right) \rightarrow 0 \). In particular, the sequence \( \left( {{f}^{\left( n\right) }\left( 0\right) {x}^{n}/n!}\right) \) tends to 0, and is therefore bounded, so the power series (*) has a radius of convergence \( \geq \left| x\right| \) (see definition 2). Since this is true for any \( x \in \rbrack - \alpha ,\alpha \lbrack \), we deduce that the radius of convergence of (*) is \( \geq \alpha \).

> Dans la pratique, pour montrer que \( \left( {R}_{n}\right) \) tend simplement vers 0, on peut utiliser la formule de Taylor qui permet d’écrire \( {R}_{n}\left( x\right) \) comme l’une des expressions

In practice, to show that \( \left( {R}_{n}\right) \) converges simply to 0, one can use Taylor's formula, which allows \( {R}_{n}\left( x\right) \) to be written as one of the expressions

\[
\frac{{x}^{n + 1}}{\left( {n + 1}\right) !}{f}^{\left( n + 1\right) }\left( {\theta x}\right) ,\;\left( {\theta  \in  \rbrack 0,1\lbrack }\right) \;\text{ ou }\;{\int }_{0}^{x}\frac{{\left( x - t\right) }^{n}}{n!}{f}^{\left( n + 1\right) }\left( t\right) {dt}
\]

(reste de Lagrange, reste intégral). Le reste intégral donne en général des résultats plus fructueux.

> (Lagrange remainder, integral remainder). The integral remainder generally yields more fruitful results.

Remarquez que pour montrer que \( f \) est développable en série entière, il est inutile de commencer par montrer que \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) a un rayon de convergence non nul. À l’inverse, si on montre que ce rayon de convergence est nul, alors cela montre que \( f \) n’est pas développable en série entière.

> Note that to show that \( f \) can be expanded as a power series, it is unnecessary to start by showing that \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) has a non-zero radius of convergence. Conversely, if one shows that this radius of convergence is zero, then it proves that \( f \) cannot be expanded as a power series.

Remarque 5. La série entière \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) peut avoir un rayon de convergence non nul et sa somme peut être différente de \( f \) (dans ce cas \( f \) n’est pas développable en série entière). Par exemple, la fonction

> Remark 5. The power series \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) may have a non-zero radius of convergence, yet its sum may differ from \( f \) (in which case \( f \) cannot be expanded as a power series). For example, the function

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \left\{  \begin{array}{lll} {e}^{-1/x} & \text{ si } & x > 0 \\  0 & \text{ si } & x \leq  0 \end{array}\right.
\]

est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) (voir l’exercice 3 page 79), et vérifie \( {f}^{\left( n\right) }\left( 0\right) = 0 \) pour tout \( n \) . La série entière \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) a donc un rayon de convergence infini, et pourtant pour tout \( \alpha > 0, f \) ne coïncide pas avec la somme de cette série entière sur \( \rbrack - \alpha ,\alpha \lbrack \) .

> is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) (see exercise 3 on page 79), and satisfies \( {f}^{\left( n\right) }\left( 0\right) = 0 \) for all \( n \). The power series \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) therefore has an infinite radius of convergence, yet for all \( \alpha > 0, f \), it does not coincide with the sum of this power series on \( \rbrack - \alpha ,\alpha \lbrack \).

- La série entière \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) peut également avoir un rayon de convergence nul bien que \( f \) soit de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) . On peut montrer par exemple que la fonction

> - The power series \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} \) may also have a zero radius of convergence even though \( f \) is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \). One can show, for example, that the function

\[
\varphi  : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R}\;x \mapsto  {\int }_{0}^{+\infty }\frac{{e}^{-t}}{1 + {xt}}{dt}
\]

est de classe \( {\mathcal{C}}^{\infty } \) sur \( {\mathbb{R}}^{ + } \) et vérifie \( {\varphi }^{\left( n\right) }\left( x\right) = {\left( -1\right) }^{n}n!{\int }_{0}^{+\infty }{e}^{-t}/{\left( 1 + xt\right) }^{n}{dt} \) . En particulier \( {\varphi }^{\left( n\right) }\left( 0\right) = {\left( -1\right) }^{n}n!\Gamma \left( {n + 1}\right) = {\left( -1\right) }^{n}{\left( n!\right) }^{2} \) . La fonction paire \( f\left( x\right) = \varphi \left( {x}^{2}\right) \) est \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) tout entier, et \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} = \sum \frac{{\varphi }^{\left( n\right) }\left( 0\right) }{n!}{z}^{2n} \) a un rayon de convergence nul. Plus généralement, pour n’importe quelle suite \( \left( {a}_{n}\right) \) (en particulier telle que \( \sum {a}_{n}{z}^{n} \) a un rayon de convergence nul) il existe une fonction \( f \) de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) telle que \( {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) (théorème de réalisation de Borel, voir le problème 16 page 295).

> is of class \( {\mathcal{C}}^{\infty } \) on \( {\mathbb{R}}^{ + } \) and satisfies \( {\varphi }^{\left( n\right) }\left( x\right) = {\left( -1\right) }^{n}n!{\int }_{0}^{+\infty }{e}^{-t}/{\left( 1 + xt\right) }^{n}{dt} \) . In particular \( {\varphi }^{\left( n\right) }\left( 0\right) = {\left( -1\right) }^{n}n!\Gamma \left( {n + 1}\right) = {\left( -1\right) }^{n}{\left( n!\right) }^{2} \) . The even function \( f\left( x\right) = \varphi \left( {x}^{2}\right) \) is \( {\mathcal{C}}^{\infty } \) on the entire \( \mathbb{R} \), and \( \sum \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{z}^{n} = \sum \frac{{\varphi }^{\left( n\right) }\left( 0\right) }{n!}{z}^{2n} \) has a radius of convergence of zero. More generally, for any sequence \( \left( {a}_{n}\right) \) (in particular such that \( \sum {a}_{n}{z}^{n} \) has a radius of convergence of zero) there exists a function \( f \) of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) such that \( {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) (Borel's realization theorem, see problem 16 page 295).

Exemple 2. La fonction \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{x} \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) et vérifie \( {f}^{\left( n\right) }\left( 0\right) = 1 \) pour tout \( n \) . D’après la formule de Taylor-Lagrange, on a

> Example 2. The function \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{x} \) is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) and satisfies \( {f}^{\left( n\right) }\left( 0\right) = 1 \) for all \( n \) . According to the Taylor-Lagrange formula, we have

\[
\forall n \in  \mathbb{N},\forall x \in  \mathbb{R},\exists \theta  \in  \rbrack 0,1\left\lbrack  {,\;{R}_{n}\left( x\right)  = f\left( x\right)  - \left( {1 + x + \cdots  + \frac{{x}^{n}}{n!}}\right)  = \frac{{x}^{n + 1}}{\left( {n + 1}\right) !}{e}^{\theta x}}\right.
\]

donc \( \left| {{R}_{n}\left( x\right) }\right| \leq {\left| x\right| }^{n + 1}{e}^{\left| x\right| }/\left( {n + 1}\right) \) !. On entire \( {R}_{n}\left( x\right) \rightarrow 0 \) , i. e. \( \left( {R}_{n}\right) \) tend simplement vers 0 sur \( \mathbb{R} \) , et on en déduit grâce à la proposition précédente que \( \sum {z}^{n}/n \) ! a un rayon de convergence infini et que

> thus \( \left| {{R}_{n}\left( x\right) }\right| \leq {\left| x\right| }^{n + 1}{e}^{\left| x\right| }/\left( {n + 1}\right) \) !. We entire \( {R}_{n}\left( x\right) \rightarrow 0 \) , i.e. \( \left( {R}_{n}\right) \) converges simply to 0 on \( \mathbb{R} \) , and we deduce from the previous proposition that \( \sum {z}^{n}/n \) ! has an infinite radius of convergence and that

\[
\forall x \in  \mathbb{R},\;{e}^{x} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{n}}{n!}.
\]

Cette expression nous invite à prolonger la fonction exponentielle sur \( \mathbb{C} \) tout entier par le biais de la fonction entière \( \sum {z}^{n}/n \) !. Ceci fait l’objet de la sous-partie suivante.

> This expression invites us to extend the exponential function to the entire \( \mathbb{C} \) by means of the entire function \( \sum {z}^{n}/n \) !. This is the subject of the following subsection.

Calcul d'un développement en série entière. Plusieurs méthodes permettent dans la pratique de calculer un développement en série entière.

> Calculating a power series expansion. In practice, several methods allow for the calculation of a power series expansion.

- On peut procéder directement à partir des développements en série entière des fonctions usuelles (voir plus bas) à l'aide des opérations de somme, produit de Cauchy, dérivation et intégration des séries entières.

> - One can proceed directly from the power series expansions of standard functions (see below) using the operations of sum, Cauchy product, differentiation, and integration of power series.

- On peut rechercher une équation différentielle satisfaite par la fonction que l'on veut développer en série entière ; on trouve ainsi les coefficients du développement en série entière en procédant par identification sur les coefficients de chaque terme de l'équation différentielle obtenue (voir par exemple l'exercice 3).

> - One can search for a differential equation satisfied by the function one wishes to expand into a power series; the coefficients of the power series expansion are thus found by identifying the coefficients of each term of the resulting differential equation (see for example exercise 3).

Développement en série entière des fonctions usuelles. En procédant comme on l'a fait dans l'exemple 2, on obtient les développements en série entière suivants :

> Power series expansion of standard functions. By proceeding as in example 2, we obtain the following power series expansions:

\[
\forall x \in  \mathbb{R},\;{e}^{x} = 1 + x + \frac{{x}^{2}}{2!} + \cdots  + \frac{{x}^{n}}{n!} + \cdots
\]

\[
\forall x \in  \mathbb{R},\;\sin x = x - \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} + \cdots  + {\left( -1\right) }^{p}\frac{{x}^{{2p} + 1}}{\left( {{2p} + 1}\right) !} + \cdots
\]

\[
\forall x \in  \mathbb{R},\;\cos x = 1 - \frac{{x}^{2}}{2!} + \frac{{x}^{4}}{4!} + \cdots  + {\left( -1\right) }^{p}\frac{{x}^{2p}}{\left( {2p}\right) !} + \cdots
\]

\[
\forall x \in  \mathbb{R},\;\operatorname{sh}x = x + \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} + \cdots  + \frac{{x}^{{2p} + 1}}{\left( {{2p} + 1}\right) !} + \cdots
\]

\[
\forall x \in  \mathbb{R},\;\operatorname{ch}x = 1 + \frac{{x}^{2}}{2!} + \frac{{x}^{4}}{4!} + \cdots  + \frac{{x}^{2p}}{\left( {2p}\right) !} + \cdots
\]

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;{\left( 1 + x\right) }^{\alpha } = 1 + \frac{\alpha }{1!}x + \frac{\alpha \left( {\alpha  - 1}\right) }{2!}{x}^{2} + \cdots  + \frac{\alpha \left( {\alpha  - 1}\right) \cdots \left( {\alpha  - n + 1}\right) }{n!}{x}^{n} + \cdots }\right.
\]

Le dernier développement est valable pour tout réel \( \alpha \) fixé. En particulier, pour tout \( x \in \rbrack - 1,1\lbrack \) ,

> The last expansion is valid for any fixed real \( \alpha \). In particular, for any \( x \in \rbrack - 1,1\lbrack \),

\[
\frac{1}{1 + x} = 1 - x + {x}^{2} - \cdots  + {\left( -1\right) }^{n}{x}^{n} + \cdots
\]

\[
\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{1}{2 \cdot  4}{x}^{2} + \frac{1 \cdot  3}{2 \cdot  4 \cdot  6}{x}^{3} + \cdots  + {\left( -1\right) }^{n - 1}\frac{1 \cdot  3\cdots \left( {{2n} - 3}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + \cdots
\]

\[
\frac{1}{\sqrt{1 + x}} = 1 - \frac{1}{2}x + \frac{1 \cdot  3}{2 \cdot  4}{x}^{2} + \cdots  + {\left( -1\right) }^{n}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + \cdots
\]

En intégrant respectivement les développements en série entière de \( \frac{1}{1 + x},\frac{1}{1 + {x}^{2}},\frac{1}{1 - {x}^{2}},\frac{1}{\sqrt{1 - {x}^{2}}} \) , \( \frac{1}{\sqrt{1 + {x}^{2}}} \) (qui sont connus grâce aux formules précédentes), on obtient

> By integrating the power series expansions of \( \frac{1}{1 + x},\frac{1}{1 + {x}^{2}},\frac{1}{1 - {x}^{2}},\frac{1}{\sqrt{1 - {x}^{2}}} \) and \( \frac{1}{\sqrt{1 + {x}^{2}}} \) respectively (which are known from the previous formulas), we obtain

\[
\forall x \in  \rbrack  - 1,1\lbrack ,\;\log \left( {1 + x}\right)  = x - \frac{{x}^{2}}{2} + \frac{{x}^{3}}{3} + \cdots  + {\left( -1\right) }^{n - 1}\frac{{x}^{n}}{n} + \cdots
\]

\[
\forall x \in  \mathbb{R},\;\arctan x = x - \frac{{x}^{3}}{3} + \frac{{x}^{5}}{5} + \cdots  + {\left( -1\right) }^{n}\frac{{x}^{{2n} + 1}}{{2n} + 1} + \cdots
\]

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;\operatorname{argth}x = x + \frac{{x}^{3}}{3} + \frac{{x}^{5}}{5} + \cdots  + \frac{{x}^{{2n} + 1}}{{2n} + 1} + \cdots }\right.
\]

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;\arcsin x = x + \frac{1}{2 \cdot  3}{x}^{3} + \cdots  + \frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right)  \cdot  \left( {{2n} + 1}\right) }{x}^{{2n} + 1} + \cdots }\right.
\]

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;\operatorname{argsh}x = x - \frac{1}{2 \cdot  3}{x}^{3} + \cdots  + {\left( -1\right) }^{n}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right)  \cdot  \left( {{2n} + 1}\right) }{x}^{{2n} + 1} + \cdots }\right.
\]

Remarque 6. Les fonctions circulaires sont en fait correctement définies à partir des séries entières (voir la partie qui suit).

> Remark 6. Circular functions are actually correctly defined using power series (see the following section).
