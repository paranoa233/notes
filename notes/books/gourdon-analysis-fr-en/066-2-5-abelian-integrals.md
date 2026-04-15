#### 2.5. Abelian integrals

*Français : 2.5. Intégrales abéliennes*

a). On veut calculer les primitives de la forme \( \int R\left( {x,\sqrt[n]{\frac{{ax} + b}{{cx} + d}}}\right) \) avec \( {ad} - {bc} \neq 0 \) et \( n \in {\mathbb{N}}^{ * } \) , où \( R \) est une fraction rationnelle en deux variables. On effectue le changement de variables

> a). We want to calculate antiderivatives of the form \( \int R\left( {x,\sqrt[n]{\frac{{ax} + b}{{cx} + d}}}\right) \) with \( {ad} - {bc} \neq 0 \) and \( n \in {\mathbb{N}}^{ * } \) , where \( R \) is a rational function in two variables. We perform the change of variables

\[
t = \sqrt[n]{\frac{{ax} + b}{{cx} + d}},\;\text{ de sorte que }\;x = g\left( t\right)  = \frac{d{t}^{n} - b}{a - {t}^{n}c}\;\text{ et }\;{dx} = {g}^{\prime }\left( t\right) {dt}.
\]

On se ramène ainsi à calculer \( \int R\left( {g\left( t\right) , t}\right) {g}^{\prime }\left( t\right) {dt} \) , primitive d’une fraction rationnelle.

> We thus reduce it to calculating \( \int R\left( {g\left( t\right) , t}\right) {g}^{\prime }\left( t\right) {dt} \) , the antiderivative of a rational function.

Exemple 3. On cherche à calculer

> Example 3. We seek to calculate

\[
\int \frac{dx}{\sqrt{1 + x} - \sqrt[3]{1 + x}}.
\]

On remarque que la fonction sous le signe \( \int \) est une fraction en \( \sqrt[6]{1 + x} \) . On pose donc \( t = \sqrt[6]{1 + x} \) , de sorte que \( {t}^{6} = 1 + x \) donc \( 6{t}^{5}{dt} = {dx} \) , et le calcul est ramené à celui de

> We note that the function under the \( \int \) sign is a fraction in \( \sqrt[6]{1 + x} \) . We therefore set \( t = \sqrt[6]{1 + x} \) , so that \( {t}^{6} = 1 + x \) thus \( 6{t}^{5}{dt} = {dx} \) , and the calculation is reduced to that of

\[
\int \frac{6{t}^{5}}{{t}^{3} - {t}^{2}}{dt}
\]

b). On veut calculer les primitives de la forme \( \int R\left( {x,\sqrt{a{x}^{2} + {bx} + c}}\right) \) avec \( a \neq 0,{b}^{2} - \; {4ac} \neq 0 \) , où \( R \) est une fraction rationnelle en deux variables. On traite plusieurs cas selon le signe de \( a \) et de \( {b}^{2} - {4ac} \) .

> b). We want to calculate antiderivatives of the form \( \int R\left( {x,\sqrt{a{x}^{2} + {bx} + c}}\right) \) with \( a \neq 0,{b}^{2} - \; {4ac} \neq 0 \) , where \( R \) is a rational function in two variables. We treat several cases according to the sign of \( a \) and \( {b}^{2} - {4ac} \) .

Si \( {b}^{2} - {4ac} > 0 \) , plusieurs cas se présentent.

> If \( {b}^{2} - {4ac} > 0 \) , several cases arise.

- Si \( a < 0 \) , on écrit \( y = \sqrt{a{x}^{2} + {bx} + c} \) sous la forme \( y = \sqrt{-a}\sqrt{{q}^{2} - {\left( x - p\right) }^{2}} \) , puis on effectue le changement de variable \( x - p = q\cos \theta \left( {y\text{ devient }q\sqrt{-a}\sin \theta }\right) \) . On se ramène alors au calcul de primitives de fractions rationnelles en sinus et cosinus.

> - If \( a < 0 \) , we write \( y = \sqrt{a{x}^{2} + {bx} + c} \) in the form \( y = \sqrt{-a}\sqrt{{q}^{2} - {\left( x - p\right) }^{2}} \) , then perform the change of variable \( x - p = q\cos \theta \left( {y\text{ devient }q\sqrt{-a}\sin \theta }\right) \) . This reduces the problem to calculating antiderivatives of rational functions in sine and cosine.

Exemple 4. Pour calculer \( \int \sqrt{1 - {x}^{2}}{dx} \) , on fait le changement de variable \( x = \cos \theta \) de sorte que \( {dx} = - \sin {\theta d\theta } \) , ce qui ramène le calcul à celui de

> Example 4. To calculate \( \int \sqrt{1 - {x}^{2}}{dx} \) , we perform the change of variable \( x = \cos \theta \) such that \( {dx} = - \sin {\theta d\theta } \) , which reduces the calculation to that of

\[
\int  - {\sin }^{2}{\theta d\theta } = \int \frac{\cos \left( {2\theta }\right)  - 1}{2}{d\theta } = \frac{\sin \left( {2\theta }\right) }{4} - \frac{\theta }{2} + k = \frac{\sin \theta \cos \theta  - \theta }{2}.
\]

Donc

> Therefore

\[
\int \sqrt{1 - {x}^{2}}{dx} = \frac{x\sqrt{1 - {x}^{2}} - \arccos x}{2} + k.
\]

- Si \( a > 0 \) , on écrit \( y = \sqrt{a{x}^{2} + {bx} + x} \) sous la forme \( y = \sqrt{a}\sqrt{{\left( x - p\right) }^{2} - {q}^{2}} \) , puis on effectue le changement de variable \( x - p = {q\varepsilon }\operatorname{ch}t \) avec \( \varepsilon  \in  \{  - 1,1\} \) ( \( y \) devient \( q\sqrt{a}\operatorname{sh}t) \) . On se ramène à calculer les primitives d’une fraction rationnelle en sinus et cosinus hyperbolique.

> - If \( a > 0 \) , we write \( y = \sqrt{a{x}^{2} + {bx} + x} \) in the form \( y = \sqrt{a}\sqrt{{\left( x - p\right) }^{2} - {q}^{2}} \) , then perform the change of variable \( x - p = {q\varepsilon }\operatorname{ch}t \) with \( \varepsilon  \in  \{  - 1,1\} \) ( \( y \) becomes \( q\sqrt{a}\operatorname{sh}t) \) . This reduces the problem to calculating the antiderivatives of a rational function in hyperbolic sine and cosine.

- Quel que soit le signe de \( a \) , une autre méthode est d’écrire \( a{x}^{2} + {bx} + c = a(x - \; \alpha )\left( {x - \beta }\right) \) où \( \alpha \) et \( \beta \) sont deux nombres réels distincts, puis

> - Regardless of the sign of \( a \) , another method is to write \( a{x}^{2} + {bx} + c = a(x - \; \alpha )\left( {x - \beta }\right) \) where \( \alpha \) and \( \beta \) are two distinct real numbers, then

\[
\sqrt{a{x}^{2} + {bx} + c} = \left| {x - \alpha }\right| \sqrt{a\left( \frac{x - \beta }{x - \alpha }\right) }
\]

et on se ramène aux primitives traitées dans la partie a).

> and we reduce the problem to the antiderivatives treated in part a).

Si \( {b}^{2} - {4ac} < 0 \) , alors \( a{x}^{2} + {bx} + c \) a le signe de \( a \) , on doit donc avoir \( a > 0 \) . On écrit \( y = \sqrt{a{x}^{2} + {bx} + c} \) sous la forme \( y = \sqrt{a}\sqrt{{q}^{2} + {\left( x - p\right) }^{2}} \) , puis on fait le changement de variable \( x - p = q\operatorname{sh}t\left( {y\text{ devient }q\sqrt{a}\operatorname{ch}t}\right) \) .

> If \( {b}^{2} - {4ac} < 0 \) , then \( a{x}^{2} + {bx} + c \) has the sign of \( a \) , so we must have \( a > 0 \) . We write \( y = \sqrt{a{x}^{2} + {bx} + c} \) in the form \( y = \sqrt{a}\sqrt{{q}^{2} + {\left( x - p\right) }^{2}} \) , then perform the change of variable \( x - p = q\operatorname{sh}t\left( {y\text{ devient }q\sqrt{a}\operatorname{ch}t}\right) \) .

Remarque 1. Lorsque \( a > 0 \) , on peut également faire le changement de variable

> Remark 1. When \( a > 0 \) , we can also perform the change of variable

\[
y = \sqrt{a{x}^{2} + {bx} + c} = x\sqrt{a} + t\;\left( {\text{ resp. } - x\sqrt{a} + t}\right) .
\]

L’idée sous-jacente est la paramétrisation de la partie d’hyperbole \( \mathcal{H} \) d’équation \( y = \; \sqrt{a{x}^{2} + {bx} + c} \) par une droite \( D \) parallèle à une asymptote de \( \mathcal{H} \) ( \( D \) coupe \( \mathcal{H} \) en un point unique). Ce type de droite a pour équation \( y = x\sqrt{a} + t \) ou \( y = - x\sqrt{a} + t, t \in \mathbb{R} \) .

> The underlying idea is the parametrization of the hyperbola branch \( \mathcal{H} \) with equation \( y = \; \sqrt{a{x}^{2} + {bx} + c} \) by a line \( D \) parallel to an asymptote of \( \mathcal{H} \) ( \( D \) intersects \( \mathcal{H} \) at a single point). This type of line has the equation \( y = x\sqrt{a} + t \) or \( y = - x\sqrt{a} + t, t \in \mathbb{R} \) .

##### Calculation tips.

*Français : Astuces de calcul.*

- Les primitives de la forme \( \int \sqrt{a{x}^{2} + {bx} + c} \) peuvent se calculer en intégrant par parties.

> - Antiderivatives of the form \( \int \sqrt{a{x}^{2} + {bx} + c} \) can be calculated by integrating by parts.

Exemple 5. On veut calculer \( \int \sqrt{{t}^{2} - 1}{dt} \) . En intégrant par parties, on a

> Example 5. We want to calculate \( \int \sqrt{{t}^{2} - 1}{dt} \) . By integrating by parts, we have

\[
\int \sqrt{{t}^{2} - 1}{dt} = t\sqrt{{t}^{2} - 1} - \int \frac{{t}^{2}}{\sqrt{{t}^{2} - 1}}{dt} = t\sqrt{{t}^{2} - 1} - \int \frac{\left( {{t}^{2} - 1}\right)  + 1}{\sqrt{{t}^{2} - 1}}{dt},
\]

d’où

> hence

\[
2\int \sqrt{{t}^{2} - 1}{dt} = t\sqrt{{t}^{2} - 1} - \int \frac{1}{\sqrt{{t}^{2} - 1}} = t\sqrt{{t}^{2} - 1} - \log \left| {t + \sqrt{{t}^{2} - 1}}\right|  + k.
\]

- Le calcul des primitives de fonctions de la forme \( R\left( {x,\sqrt{{\alpha x} + \beta },\sqrt{{\gamma x} + \delta }}\right) \) où \( R \) est une fraction rationnelle en trois variables se ramène, après le changement de variable \( t = \sqrt{{\gamma x} + \delta } \) ,à un calcul de primitives de la forme \( \int F\left( {t,\sqrt{a{t}^{2} + {bt} + c}}\right) \) où \( F \) est une fraction rationnelle.

> - Computing antiderivatives of functions of the form \( R\left( {x,\sqrt{{\alpha x} + \beta },\sqrt{{\gamma x} + \delta }}\right) \) where \( R \) is a rational function in three variables reduces, after the change of variable \( t = \sqrt{{\gamma x} + \delta } \), to computing antiderivatives of the form \( \int F\left( {t,\sqrt{a{t}^{2} + {bt} + c}}\right) \) where \( F \) is a rational function.

- Le calcul des primitives \( \int \frac{dx}{{\left( x + a\right) }^{n}\sqrt{\alpha {x}^{2} + {\beta x} + \gamma }} \) est considérablement simplifié en effectuant le changement de variable \( t = 1/\left( {x + a}\right) \) .

> - Computing antiderivatives of \( \int \frac{dx}{{\left( x + a\right) }^{n}\sqrt{\alpha {x}^{2} + {\beta x} + \gamma }} \) is considerably simplified by performing the change of variable \( t = 1/\left( {x + a}\right) \).
