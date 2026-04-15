#### 4.4. Classic functions defined as sums of power series

*Français : 4.4. Fonctions classiques définies comme sommes de série entières*

Fonction exponentielle complexe. La série entière \( \sum {z}^{n}/n \) ! a un rayon de convergence infini. On définit l'exponentielle complexe par

> Complex exponential function. The power series \( \sum {z}^{n}/n \) ! has an infinite radius of convergence. We define the complex exponential by

\[
\forall z \in  \mathbb{C},\;{e}^{z} = \exp \left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{n}}{n!}.
\]

Comme l’a vu, cette fonction coïncide sur \( \mathbb{R} \) avec la fonction exponentielle "classique". Comme sur \( \mathbb{R} \) , on a \( {e}^{{z}_{1} + {z}_{2}} = {e}^{{z}_{1}}{e}^{{z}_{2}} \) pour tout \( {z}_{1},{z}_{2} \in \mathbb{C} \) . Elle permet de définir la puissance complexe d’un nombre \( a > 0 \) , par \( {a}^{z} = \exp \left( {z\log a}\right) \) pour tout \( z \in \mathbb{C} \) .

> As seen, this function coincides on \( \mathbb{R} \) with the "classic" exponential function. As on \( \mathbb{R} \), we have \( {e}^{{z}_{1} + {z}_{2}} = {e}^{{z}_{1}}{e}^{{z}_{2}} \) for all \( {z}_{1},{z}_{2} \in \mathbb{C} \). It allows for the definition of the complex power of a number \( a > 0 \), by \( {a}^{z} = \exp \left( {z\log a}\right) \) for all \( z \in \mathbb{C} \).

Les parties paire et impaire de \( {e}^{z} \) sont les fonctions cosinus hyperbolique et sinus hyperbolique définies sur \( \mathbb{C} \) par

> The even and odd parts of \( {e}^{z} \) are the hyperbolic cosine and hyperbolic sine functions defined on \( \mathbb{C} \) by

\[
\operatorname{ch}z = \frac{{e}^{z} + {e}^{-z}}{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{2n}}{\left( {2n}\right) !}\;\text{ et }\;\operatorname{sh}z = \frac{{e}^{z} - {e}^{-z}}{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{{2n} + 1}}{\left( {{2n} + 1}\right) !}.
\]

Fonctions circulaires. On définit les fonctions circulaires cosinus et sinus sur \( \mathbb{C} \) par

> Circular functions. We define the circular cosine and sine functions on \( \mathbb{C} \) by

\[
\cos z = \frac{{e}^{iz} + {e}^{-{iz}}}{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}\frac{{z}^{2n}}{\left( {2n}\right) !}\;\text{ et }\;\sin z = \frac{{e}^{iz} - {e}^{-{iz}}}{2i} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}\frac{{z}^{{2n} + 1}}{\left( {{2n} + 1}\right) !}.
\]

Outre les formules trigonométriques usuelles, ces fonctions vérifient

> In addition to the usual trigonometric formulas, these functions satisfy

\[
\forall z \in  \mathbb{C},\;\cos z + i\sin z = {e}^{iz}.
\]
