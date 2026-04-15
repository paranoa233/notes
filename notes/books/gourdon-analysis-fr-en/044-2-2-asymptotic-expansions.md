#### 2.2. Asymptotic expansions

*Français : 2.2. Développements asymptotiques*

##### Comparison scale.

*Français : Échelle de comparaison.*

DéFINITION 3. Soit \( X \) un espace métrique et \( {x}_{0} \in X \) . On appelle échelle de comparaison un ensemble \( \mathcal{E} \) de fonctions définies au voisinage de \( {x}_{0} \) dans \( X \) sauf éventuellement en \( {x}_{0} \) , et vérifiant la propriété suivante : si \( f, g \in \mathcal{E} \) , alors \( f = g \) ou bien \( f = o\left( g\right) \) ou bien \( g = o\left( f\right) \) .

> DEFINITION 3. Let \( X \) be a metric space and \( {x}_{0} \in X \) . A comparison scale is a set \( \mathcal{E} \) of functions defined in a neighborhood of \( {x}_{0} \) in \( X \) , except possibly at \( {x}_{0} \) , satisfying the following property: if \( f, g \in \mathcal{E} \) , then \( f = g \) or \( f = o\left( g\right) \) or \( g = o\left( f\right) \) .

Exemple 1. Au voisinage de \( + \infty \) pour les fonctions de la variable réelle, les échelles de comparaison les plus courantes sont les suivantes :

> Example 1. In the neighborhood of \( + \infty \) for functions of a real variable, the most common comparison scales are the following:

- celles constituées des fonctions du type \( {x}^{\alpha }\left( {\alpha  \in  \mathbb{R}}\right) \) ,

> - those consisting of functions of the type \( {x}^{\alpha }\left( {\alpha  \in  \mathbb{R}}\right) \) ,

- plus généralement celles constituées des fonctions du type \( {x}^{\alpha }{\left( \log x\right) }^{\beta }\left( {\alpha ,\beta  \in  \mathbb{R}}\right) \)

> - more generally, those consisting of functions of the type \( {x}^{\alpha }{\left( \log x\right) }^{\beta }\left( {\alpha ,\beta  \in  \mathbb{R}}\right) \)

- plus généralement celles constituées des fonctions du type \( {x}^{\alpha }{\left( \log x\right) }^{\beta }{e}^{c{x}^{\gamma }}(\alpha ,\beta , c \in \; \mathbb{R},\gamma  > 0) \) .

> - more generally, those consisting of functions of the type \( {x}^{\alpha }{\left( \log x\right) }^{\beta }{e}^{c{x}^{\gamma }}(\alpha ,\beta , c \in \; \mathbb{R},\gamma  > 0) \) .

De même, au voisinage de 0, une échelle de comparaison courante est celle contenant les fonctions du type \( {x}^{\alpha }{\log }^{\beta }x\left( {\alpha ,\beta \in \mathbb{R}}\right) \) .

> Similarly, in the neighborhood of 0, a common comparison scale is the one containing functions of the type \( {x}^{\alpha }{\log }^{\beta }x\left( {\alpha ,\beta \in \mathbb{R}}\right) \) .

##### Asymptotic expansions.

*Français : Développements asymptotiques.*

DéFINITION 4. Soit \( X \) un espace métrique. Soient \( f : D \subset X \rightarrow E \) une application, \( {x}_{0} \) un point d’accumulation de \( D \) dans \( X \) et \( k \) un entier naturel non nul. On appelle développement asymptotique à \( k \) termes de \( f \) par rapport à une échelle de comparaison \( \mathcal{E} \) au voisinage de \( {x}_{0} \) toute expression de la forme

> DEFINITION 4. Let \( X \) be a metric space. Let \( f : D \subset X \rightarrow E \) be a mapping, \( {x}_{0} \) an accumulation point of \( D \) in \( X \) , and \( k \) a non-zero natural integer. An asymptotic expansion with \( k \) terms of \( f \) with respect to a comparison scale \( \mathcal{E} \) in the neighborhood of \( {x}_{0} \) is any expression of the form

\[
{c}_{1}{f}_{1} + {c}_{2}{f}_{2} + \cdots  + {c}_{k}{f}_{k}
\]

vérifiant

> satisfying

(i) \( {c}_{1},\ldots ,{c}_{k} \in E \) sont des constantes multiplicatives,

> (i) \( {c}_{1},\ldots ,{c}_{k} \in E \) are multiplicative constants,

(ii) \( {f}_{1},\ldots ,{f}_{k} \in \mathcal{E} \) avec pour tout \( i,{f}_{i + 1}\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }o\left( {{f}_{i}\left( x\right) }\right) \) ,

> (ii) \( {f}_{1},\ldots ,{f}_{k} \in \mathcal{E} \) with for all \( i,{f}_{i + 1}\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }o\left( {{f}_{i}\left( x\right) }\right) \) ,

(iii) \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }{c}_{1}{f}_{1}\left( x\right) + {c}_{2}{f}_{2}\left( x\right) + \cdots + {c}_{k}{f}_{k}\left( x\right) + o\left( {{f}_{k}\left( x\right) }\right) \) .

> (iii) \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }{c}_{1}{f}_{1}\left( x\right) + {c}_{2}{f}_{2}\left( x\right) + \cdots + {c}_{k}{f}_{k}\left( x\right) + o\left( {{f}_{k}\left( x\right) }\right) \) .

Lorsque qu’un tel développement par rapport à \( \mathcal{E} \) existe pour \( f \) , il est unique. On a en particulier \( f\left( x\right) \sim {c}_{1}{f}_{1}\left( x\right) \) , et on dit que \( {c}_{1}{f}_{1} \) est la partie principale (ou l’équivalent) de \( f \) au voisinage de \( {x}_{0} \) .

> When such an expansion with respect to \( \mathcal{E} \) exists for \( f \) , it is unique. In particular, we have \( f\left( x\right) \sim {c}_{1}{f}_{1}\left( x\right) \) , and we say that \( {c}_{1}{f}_{1} \) is the principal part (or the equivalent) of \( f \) in the neighborhood of \( {x}_{0} \) .

L'unicité découle facilement des propriétés vérifiées par une échelle de comparaison.

> Uniqueness follows easily from the properties satisfied by a comparison scale.

Remarque 9. Lorsque l'on ne précise pas l'échelle de comparaison par rapport à laquelle on veut un développement asymptotique, c'est en général une des échelles usuelles décrites dans l'exemple 1.

> Remark 9. When the comparison scale for which an asymptotic expansion is desired is not specified, it is generally one of the standard scales described in Example 1.

Exemple 2. On peut démontrer, pour tout \( k \in {\mathbb{N}}^{ * } \) , le développement asymptotique sui-vant, lorsque \( x \rightarrow + \infty \) :

> Example 2. One can prove, for any \( k \in {\mathbb{N}}^{ * } \), the following asymptotic expansion, as \( x \rightarrow + \infty \):

\[
{\int }_{2}^{x}\frac{dt}{\log t} = \frac{x}{\log x} + \frac{1!x}{{\log }^{2}x} + \cdots  + \frac{\left( {k - 1}\right) !x}{{\log }^{k}x} + o\left( \frac{x}{{\log }^{k}x}\right) .
\]

(voir l'exercice 8 page 173).

> (see exercise 8 on page 173).
