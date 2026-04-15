#### 3.4. Exercises

*Français : 3.4. Exercices*

EXERCICE 1. Déterminer les solutions maximales de l'équation différentielle suivante (E): \( x{y}^{\prime } - y = \sqrt{{x}^{2} + {y}^{2}} \) .

> EXERCISE 1. Determine the maximal solutions of the following differential equation (E): \( x{y}^{\prime } - y = \sqrt{{x}^{2} + {y}^{2}} \) .

Solution. On a affaire à une équation homogène du premier ordre. Soit \( y \) une solution maximale de \( \left( E\right) \) sur un intervalle \( I \) coupant \( {\mathbb{R}}^{+ * } \) . Alors \( x \mapsto y\left( {-x}\right) \) est aussi solution, on va donc se limiter dans un premier temps à étudier \( y \) sur \( J = I \cap {\mathbb{R}}^{+ * } \) .

> Solution. We are dealing with a first-order homogeneous equation. Let \( y \) be a maximal solution of \( \left( E\right) \) on an interval \( I \) intersecting \( {\mathbb{R}}^{+ * } \) . Then \( x \mapsto y\left( {-x}\right) \) is also a solution, so we will initially limit ourselves to studying \( y \) on \( J = I \cap {\mathbb{R}}^{+ * } \) .

Lorsque \( x \in J \) , on pose \( t = y/x \) , et l’équation \( \left( E\right) \) devient \( \left( {E}^{\prime }\right) : {t}^{\prime } = \frac{1}{x}\sqrt{1 + {t}^{2}} \) . On a donc

> When \( x \in J \) , we set \( t = y/x \) , and the equation \( \left( E\right) \) becomes \( \left( {E}^{\prime }\right) : {t}^{\prime } = \frac{1}{x}\sqrt{1 + {t}^{2}} \) . We therefore have

\[
\frac{dt}{\sqrt{1 + {t}^{2}}} = \frac{dx}{x},
\]

ce qui par intégration donne argsh \( t = \log \left( {x/\lambda }\right) \) , avec \( \lambda > 0 \) . Donc

> which by integration gives argsh \( t = \log \left( {x/\lambda }\right) \) , with \( \lambda > 0 \) . Thus

\[
\forall x \in  J,\;t\left( x\right)  = \operatorname{sh}\left\lbrack  {\log \left( \frac{x}{\lambda }\right) }\right\rbrack   = \frac{1}{2}\left( {\frac{x}{\lambda } - \frac{\lambda }{x}}\right) \;\text{ donc }\;y\left( x\right)  = {xt}\left( x\right)  = \frac{{x}^{2} - {\lambda }^{2}}{2\lambda }.
\]

La fonction \( x \mapsto \left( {{x}^{2} - {\lambda }^{2}}\right) /\left( {2\lambda }\right) \) est aussi solution sur \( \mathbb{R} \) , et comme la fonction \( y \) est une solution maximale, on en déduit \( J = {\mathbb{R}}^{+ * } \) , puis \( K = I \cap {\mathbb{R}}^{- * } \neq \varnothing \) (mais attention, a priori, cela ne veut pas dire que ce soit la seule solution maximale égale à \( y \) sur \( {\mathbb{R}}^{+ * } \) ). Par symétrie, on a

> The function \( x \mapsto \left( {{x}^{2} - {\lambda }^{2}}\right) /\left( {2\lambda }\right) \) is also a solution on \( \mathbb{R} \) , and since the function \( y \) is a maximal solution, we deduce \( J = {\mathbb{R}}^{+ * } \) , then \( K = I \cap {\mathbb{R}}^{- * } \neq \varnothing \) (but be careful, a priori, this does not mean it is the only maximal solution equal to \( y \) on \( {\mathbb{R}}^{+ * } \) ). By symmetry, we have

\[
\exists \mu  \in  \mathbb{R},\forall x \in  K,\;y\left( x\right)  = \frac{{x}^{2} - {\mu }^{2}}{2\mu }.
\]

Comme précédemment, on en déduit que \( K = {\mathbb{R}}^{- * } \) . Ainsi, \( I \) est un intervalle vérifiant \( I \cap {\mathbb{R}}^{+ * } = \; {\mathbb{R}}^{+ * } \) et \( I \cap {\mathbb{R}}^{- * } = {\mathbb{R}}^{- * } \) , donc \( I = \mathbb{R} \) . Comme \( y \) est continue, les limites à gauche et à droite de \( y \) en 0 coincident, ce qui entraîne \( - \mu /2 = - \lambda /2 \) , donc \( \mu = \lambda \) .

> As before, we deduce that \( K = {\mathbb{R}}^{- * } \) . Thus, \( I \) is an interval satisfying \( I \cap {\mathbb{R}}^{+ * } = \; {\mathbb{R}}^{+ * } \) and \( I \cap {\mathbb{R}}^{- * } = {\mathbb{R}}^{- * } \) , so \( I = \mathbb{R} \) . Since \( y \) is continuous, the left and right limits of \( y \) at 0 coincide, which implies \( - \mu /2 = - \lambda /2 \) , therefore \( \mu = \lambda \) .

Finalement, nous avons montré que toutes les solutions maximales de \( \left( E\right) \) sont définies sur \( \mathbb{R} \) et qu'elles sont de la forme

> Finally, we have shown that all maximal solutions of \( \left( E\right) \) are defined on \( \mathbb{R} \) and are of the form

\[
y : x \mapsto  \frac{{x}^{2} - {\lambda }^{2}}{2\lambda }.
\]

EXERCICE 2. Déterminer les solutions maximales à valeurs réelles de l'équation différen-tielle \( \left( R\right) : {y}^{\prime } + y + {y}^{2} + 1 = 0 \) .

> EXERCISE 2. Determine the real-valued maximal solutions of the differential equation \( \left( R\right) : {y}^{\prime } + y + {y}^{2} + 1 = 0 \) .

Solution. Il s'agit d'une équation de Ricatti. Cherchons en une solution particulière. La fonction constante \( t \mapsto \alpha \) est solution si et seulement si \( {\alpha }^{2} + \alpha + 1 = 0 \) , c’est-à-dire \( \alpha = j \) ou \( \alpha = {j}^{2} \; \left( {j = {e}^{{2i\pi }/3}}\right) \) . Ceci nous amène à commencer à rechercher les solutions complexes de \( \left( R\right) \) .

> Solution. This is a Riccati equation. Let us look for a particular solution. The constant function \( t \mapsto \alpha \) is a solution if and only if \( {\alpha }^{2} + \alpha + 1 = 0 \) , that is to say \( \alpha = j \) or \( \alpha = {j}^{2} \; \left( {j = {e}^{{2i\pi }/3}}\right) \) . This leads us to begin by searching for the complex solutions of \( \left( R\right) \) .

En posant \( z = y - j \) et en remplaçant dans \( \left( R\right) \) , on obtient \( {z}^{\prime } + \left( {{2j} + 1}\right) z + {z}^{2} = 0 \) . On a affaire à une équation résolue. Si \( z \) s’annule en un point, alors \( {z}^{\prime } \) aussi et d’après le théorème de Cauchy-Lipschitz, \( z \) doit être la fonction nulle. Si \( z \) n’est pas la fonction nulle, on en conclut que \( z \) ne s’annule pas, et on peut donc écrire l’équation sous la forme \( {z}^{\prime }/{z}^{2} + \left( {{2j} + 1}\right) /z + 1 = 0 \) , ou encore, en posant \( u = 1/z, - {u}^{\prime } + \left( {{2j} + 1}\right) u + 1 = 0 \) . Comme \( {2j} + 1 = i\sqrt{3} \) , cette équation s’écrit aussi \( \left( L\right) : - {u}^{\prime } + i\sqrt{3}u + 1 = 0 \) . La fonction constante \( t \mapsto i/\sqrt{3} \) est solution, et l’équation homogène associée est \( {v}^{\prime } = i\sqrt{3}v \) , dont les solutions sont \( v\left( t\right) = \lambda {e}^{i\sqrt{3}t},\lambda \in \mathbb{C} \) . Finalement, nous avons montré que si \( z \) n’est pas la fonction nulle, alors

> By setting \( z = y - j \) and substituting into \( \left( R\right) \), we obtain \( {z}^{\prime } + \left( {{2j} + 1}\right) z + {z}^{2} = 0 \). We are dealing with a solved equation. If \( z \) vanishes at a point, then \( {z}^{\prime } \) does as well, and according to the Cauchy-Lipschitz theorem, \( z \) must be the zero function. If \( z \) is not the zero function, we conclude that \( z \) does not vanish, and we can therefore write the equation in the form \( {z}^{\prime }/{z}^{2} + \left( {{2j} + 1}\right) /z + 1 = 0 \), or alternatively, by setting \( u = 1/z, - {u}^{\prime } + \left( {{2j} + 1}\right) u + 1 = 0 \). Since \( {2j} + 1 = i\sqrt{3} \), this equation can also be written as \( \left( L\right) : - {u}^{\prime } + i\sqrt{3}u + 1 = 0 \). The constant function \( t \mapsto i/\sqrt{3} \) is a solution, and the associated homogeneous equation is \( {v}^{\prime } = i\sqrt{3}v \), whose solutions are \( v\left( t\right) = \lambda {e}^{i\sqrt{3}t},\lambda \in \mathbb{C} \). Finally, we have shown that if \( z \) is not the zero function, then

\[
\frac{1}{z} = u = v + i\sqrt{3} = \lambda {e}^{i\sqrt{3}t} + \frac{i}{\sqrt{3}},\;\text{ donc }\;y = z + j = \frac{1}{\lambda {e}^{i\sqrt{3}t} + i/\sqrt{3}} + j.
\]

Mais nous voulions les solutions réelles de \( \left( E\right) \) . Pour cela, nous recherchons les \( \lambda \in \mathbb{C} \) tels que la partie imaginaire de la fonction précédente soit nulle pour tout \( t \) . Ceci se produit si et seulement si, pour tout \( t \) ,

> But we wanted the real solutions of \( \left( E\right) \). To do this, we look for the \( \lambda \in \mathbb{C} \) such that the imaginary part of the previous function is zero for all \( t \). This occurs if and only if, for all \( t \),

\[
- \frac{\sqrt{3}}{2} =  - \Im \left( j\right)  = \Im \left( \frac{1}{\lambda {e}^{i\sqrt{3}t} + i/\sqrt{3}}\right)  =  - \frac{\Im \left( {\lambda {e}^{i\sqrt{3}t} + i/\sqrt{3}}\right) }{{\left| \lambda {e}^{i\sqrt{3}t} + i/\sqrt{3}\right| }^{2}},
\]

et en notant \( I = \Im \left( {\lambda {e}^{i\sqrt{3}t}}\right) \) , ceci s’écrit aussi

> and by noting \( I = \Im \left( {\lambda {e}^{i\sqrt{3}t}}\right) \), this is also written as

\[
\left( {{\left| \lambda \right| }^{2} + \frac{1}{3} + \frac{2I}{\sqrt{3}}}\right) \frac{\sqrt{3}}{2} = I + \frac{1}{\sqrt{3}},
\]

ce qui équivaut à \( {\left| \lambda \right| }^{2} = 1/3 \) . En posant \( \lambda = {e}^{i\theta }/\sqrt{3},\left( {\theta \in \mathbb{R}}\right) \) , on voit que les solutions de \( \left( R\right) \) sont de la forme

> which is equivalent to \( {\left| \lambda \right| }^{2} = 1/3 \). By setting \( \lambda = {e}^{i\theta }/\sqrt{3},\left( {\theta \in \mathbb{R}}\right) \), we see that the solutions of \( \left( R\right) \) are of the form

\[
t \mapsto  j + \frac{\sqrt{3}}{{e}^{i\left( {\sqrt{3}t + \theta }\right) } + i} = \frac{1}{2} + \frac{\sqrt{3}}{2}\frac{\cos \left( {\sqrt{3}t + \theta }\right) }{1 + \sin \left( {\sqrt{3}t + \theta }\right) }.
\]

Les solutions maximales sont définies sur des intervalles ouverts de longueur \( {2\pi }/\sqrt{3} \) .

> The maximal solutions are defined on open intervals of length \( {2\pi }/\sqrt{3} \).

EXERCICE 3. Déterminer les solutions de l’équation différentielle \( \left( C\right) : y = t{y}^{\prime } - {y}^{\prime 2}/4 \) .

> EXERCISE 3. Determine the solutions of the differential equation \( \left( C\right) : y = t{y}^{\prime } - {y}^{\prime 2}/4 \).

Solution. Il s’agit d’une équation de Clairaut. On utilise le paramètre \( p = {y}^{\prime } \) . Ainsi, \( \left( C\right) \) s’écrit \( y = {tp} - {p}^{2}/4 \) , donc \( {dy} = {pdt} = {pdt} + {tdp} - {pdp}/2 \) , c’est-à-dire \( \left( {t - p/2}\right) {dp} = 0 \) .

> Solution. This is a Clairaut equation. We use the parameter \( p = {y}^{\prime } \). Thus, \( \left( C\right) \) is written as \( y = {tp} - {p}^{2}/4 \), therefore \( {dy} = {pdt} = {pdt} + {tdp} - {pdp}/2 \), that is to say \( \left( {t - p/2}\right) {dp} = 0 \).

- Lorsque \( {dp} = 0 \) , on trouve les solutions affines de \( \left( C\right) \) , qui sont de la forme \( t \mapsto  {mt} - {m}^{2}/4 \; \left( {m \in  \mathbb{R}}\right) \) .

> - When \( {dp} = 0 \), we find the affine solutions of \( \left( C\right) \), which are of the form \( t \mapsto  {mt} - {m}^{2}/4 \; \left( {m \in  \mathbb{R}}\right) \).

- Lorsque \( t - p/2 = 0 \) , on trouve la solution \( t \mapsto  {t}^{2} \) .

> - When \( t - p/2 = 0 \), we find the solution \( t \mapsto  {t}^{2} \).

On a ainsi trouvé les solutions de classe \( {\mathcal{C}}^{2} \) de \( \left( C\right) \) . On obtient maintenant toutes les solutions de classe \( {\mathcal{C}}^{1} \) par raccordement entre les solutions des deux types.

> We have thus found the \( {\mathcal{C}}^{2} \) class solutions of \( \left( C\right) \) . We now obtain all \( {\mathcal{C}}^{1} \) class solutions by connecting the solutions of the two types.
