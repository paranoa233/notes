#### 2.3. Antiderivatives of sine and cosine functions

*Français : 2.3. Primitives des fonctions en sinus et cosinus*

Polynômes en sinus et cosinus. On veut calculer les primitives \( \int {\sin }^{m}x{\cos }^{n}{xdx} \) , où \( m, n \in \mathbb{N} \) . Deux cas se présentent :

> Polynomials in sine and cosine. We want to calculate the antiderivatives \( \int {\sin }^{m}x{\cos }^{n}{xdx} \) , where \( m, n \in \mathbb{N} \) . Two cases arise:

- L’un des entiers \( m \) ou \( n \) est impair (par exemple \( n = {2p} + 1 \) ). On a alors

> - One of the integers \( m \) or \( n \) is odd (for example \( n = {2p} + 1 \) ). We then have

\[
\int {\sin }^{m}x{\cos }^{n}{xdx} = \int {\sin }^{m}x{\left( 1 - {\sin }^{2}x\right) }^{p}\cos {xdx}.
\]

En effectuant ensuite le changement de variable \( t = \sin x \) , on se ramène à la primitive \( \int {t}^{m}{\left( 1 - {t}^{2}\right) }^{p}{dt} \) qui est facile à calculer.

> By then performing the change of variable \( t = \sin x \) , we reduce it to the antiderivative \( \int {t}^{m}{\left( 1 - {t}^{2}\right) }^{p}{dt} \) which is easy to calculate.

- Les entiers \( m \) et \( n \) sont pairs. On linéarise, en exprimant \( {\sin }^{m}x{\cos }^{n}x \) comme combinaison linéaire de fonctions de la forme \( \cos {kx} \) et \( \sin {kx} \) . Par exemple, pour calculer une primitive de \( {\cos }^{4}x \) , on écrit

> - The integers \( m \) and \( n \) are even. We linearize by expressing \( {\sin }^{m}x{\cos }^{n}x \) as a linear combination of functions of the form \( \cos {kx} \) and \( \sin {kx} \) . For example, to calculate an antiderivative of \( {\cos }^{4}x \) , we write

\[
\cos x = \frac{{e}^{ix} + {e}^{-{ix}}}{2}\;\text{ d’où }
\]

\[
{\cos }^{4}x = \frac{1}{8}\left( {\frac{{e}^{4ix} + {e}^{-{4ix}}}{2} + 4\frac{{e}^{2ix} + {e}^{-{2ix}}}{2} + 3}\right)  = \frac{\cos {4x}}{8} + \frac{\cos {2x}}{2} + \frac{3}{8},
\]

d'où on déduit facilement la primitive recherchée.

> from which we easily deduce the sought antiderivative.

Fractions rationnelles en sinus et cosinus. On veut calculer une primitive d'une fonction de la forme \( R\left( {\sin x,\cos x}\right) \) où \( R \) est une fraction rationnelle en deux variables.

> Rational functions in sine and cosine. We want to calculate an antiderivative of a function of the form \( R\left( {\sin x,\cos x}\right) \) where \( R \) is a rational function in two variables.

On s’en sort toujours en effectuant le changement de variable \( t = \tan \left( {x/2}\right) \) . Comme \( {dt} = \frac{1}{2}\left( {1 + {t}^{2}}\right) {dx} \) , le calcul se ramène à celui de \( \int R\left( {\frac{2t}{1 + {t}^{2}},\frac{1 - {t}^{2}}{1 + {t}^{2}}}\right) \frac{2dt}{1 + {t}^{2}} \) , c’est-à-dire à celui d'une primitive d'une fraction rationnelle. En procédant de la sorte, on trouve les primitives suivantes, qu'il faut retenir :

> We can always manage by performing the change of variable \( t = \tan \left( {x/2}\right) \) . Since \( {dt} = \frac{1}{2}\left( {1 + {t}^{2}}\right) {dx} \) , the calculation reduces to that of \( \int R\left( {\frac{2t}{1 + {t}^{2}},\frac{1 - {t}^{2}}{1 + {t}^{2}}}\right) \frac{2dt}{1 + {t}^{2}} \) , that is to say, to that of an antiderivative of a rational function. By proceeding in this way, we find the following antiderivatives, which must be remembered:

\[
\int \frac{dx}{\sin x} = \log \left| {\tan \left( \frac{x}{2}\right) }\right| \;\text{ et }\;\int \frac{dx}{\cos x} = \log \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{4}}\right) }\right| .
\]

Cette méthode est souvent fastidieuse car elle amène à calculer des primitives de fractions rationnelles dont le dénominateur est de degré élevé. On commence en général par essayer d’effectuer l’un des changements de variable \( t = \sin x, t = \cos x \) ou \( t = \tan x \) qui simplifie parfois les calculs. On peut à ce sujet utiliser la règle de Bioche présentée ci dessous :

> This method is often tedious because it leads to calculating antiderivatives of rational functions whose denominator is of high degree. We generally start by trying to perform one of the changes of variable \( t = \sin x, t = \cos x \) or \( t = \tan x \) which sometimes simplifies the calculations. In this regard, one can use the Bioche rule presented below:

- si \( R\left( {\sin x,\cos x}\right) {dx} \) reste inchangé en changeant \( x \) en \( \pi  - x \) , on pose \( t = \sin x \) ;

> - if \( R\left( {\sin x,\cos x}\right) {dx} \) remains unchanged when changing \( x \) to \( \pi  - x \) , we set \( t = \sin x \) ;

- si \( R\left( {\sin x,\cos x}\right) {dx} \) reste inchangé en changeant \( x \) en \( - x \) , on pose \( t = \cos x \) ;

> - if \( R\left( {\sin x,\cos x}\right) {dx} \) remains unchanged when changing \( x \) to \( - x \) , we set \( t = \cos x \) ;

- si \( R\left( {\sin x,\cos x}\right) {dx} \) reste inchangé en changeant \( x \) en \( \pi  + x \) , on pose \( t = \tan x \) . N’oubliez pas que le terme \( {dx} \) doit faire parti de l’expression invariante !

> - if \( R\left( {\sin x,\cos x}\right) {dx} \) remains unchanged when changing \( x \) to \( \pi  + x \) , we set \( t = \tan x \) . Do not forget that the term \( {dx} \) must be part of the invariant expression!

Exemple 2. On veut calculer \( \int \frac{{\sin }^{3}x}{1 + {\cos }^{2}x}{dx} \) . Le terme sous le signe \( \int \) reste invariant en changeant \( x \) en \( - x \) (il faut prendre en compte le \( {dx} \) ), on pose donc \( t = \cos x \) . On a \( {dt} = - \sin {xdx} \) , donc le calcul se ramène à celui de la primitive

> Example 2. We want to calculate \( \int \frac{{\sin }^{3}x}{1 + {\cos }^{2}x}{dx} \) . The term under the \( \int \) sign remains invariant when changing \( x \) to \( - x \) (the \( {dx} \) must be taken into account), so we set \( t = \cos x \) . We have \( {dt} = - \sin {xdx} \) , so the calculation reduces to that of the antiderivative

\[
\int \frac{1 - {t}^{2}}{1 + {t}^{2}}\left( {-{dt}}\right)  = \int \left( {1 - \frac{2}{1 + {t}^{2}}}\right) {dt} = t - 2\arctan t + k.
\]

Il reste à remplacer \( t \) par \( \cos x \) , ce qui donne

> It remains to replace \( t \) with \( \cos x \) , which gives

\[
\int \frac{{\sin }^{3}x}{1 + {\cos }^{2}x}{dx} = \cos x - 2\arctan \left( {\cos x}\right)  + k.
\]
