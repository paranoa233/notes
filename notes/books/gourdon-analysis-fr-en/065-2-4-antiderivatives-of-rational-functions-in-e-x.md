#### 2.4. Antiderivatives of rational functions in \( {e}^{x} \)

*Français : 2.4. Primitives des fractions rationnelles en \( {e}^{x} \)*

Pour calculer la primitive une fonction de la forme \( R\left( {e}^{x}\right) \) où \( R \) est une fraction ration-nelle, on s’en sort toujours en posant \( t = {e}^{x} \) ; on se ramène alors au calcul de \( \int R\left( t\right) /{tdt} \) , primitive d'une fraction rationnelle.

> To calculate the antiderivative of a function of the form \( R\left( {e}^{x}\right) \) where \( R \) is a rational function, we can always succeed by setting \( t = {e}^{x} \) ; we then reduce it to the calculation of \( \int R\left( t\right) /{tdt} \) , the antiderivative of a rational function.

Fractions rationnelles en sinus et cosinus hyperbolique. Pour calculer une primitive de \( R\left( {\operatorname{sh}x,\operatorname{ch}x}\right) \) où \( R \) est une fraction rationnelle en deux variables, trois méthodes sont utilisables. On peut

> Rational functions in hyperbolic sine and cosine. To calculate an antiderivative of \( R\left( {\operatorname{sh}x,\operatorname{ch}x}\right) \) where \( R \) is a rational function in two variables, three methods can be used. One can

- faire le changement de variable \( t = \operatorname{th}\left( {x/2}\right) \) , ce qui ramène le calcul à celui de

> - perform the change of variable \( t = \operatorname{th}\left( {x/2}\right) \) , which reduces the calculation to that of

\[
\int R\left( {\frac{2t}{1 - {t}^{2}},\frac{1 + {t}^{2}}{1 - {t}^{2}}}\right) \frac{2dt}{1 - {t}^{2}}
\]

(technique à éviter si possible),

> (a technique to avoid if possible),

- tout exprimer en fonction de \( {e}^{x} \) ,

> - express everything in terms of \( {e}^{x} \) ,

- effectuer un éventuel changement de variable \( t = \operatorname{sh}x, t = \operatorname{ch}x \) ou \( t = \operatorname{th}x \) en procédant par analogie avec \( \int R\left( {\sin x,\cos x}\right) {dx} \) .

> - perform a possible change of variable \( t = \operatorname{sh}x, t = \operatorname{ch}x \) or \( t = \operatorname{th}x \) by proceeding by analogy with \( \int R\left( {\sin x,\cos x}\right) {dx} \) .

La première et/ou la seconde de ces méthodes donne les primitives classiques suivantes

> The first and/or the second of these methods yields the following classic antiderivatives

\[
\int \frac{dx}{\operatorname{ch}x} = 2\arctan \left( {e}^{x}\right)  + k\;\text{ et }\;\int \frac{dx}{\operatorname{sh}x} = \frac{1}{2}\log \left( \frac{\operatorname{ch}x - 1}{\operatorname{ch}x + 1}\right)  + k = \log \left| {\operatorname{th}\frac{x}{2}}\right|  + {k}^{\prime }.
\]
