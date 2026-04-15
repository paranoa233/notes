#### 2.3. Taylor expansions

*Français : 2.3. Développements limités*

Dans la suite de cette partie, \( I \) désigne un intervalle de \( \mathbb{R} \) non réduit à un singleton.

> In the remainder of this section, \( I \) denotes an interval of \( \mathbb{R} \) not reduced to a singleton.

DéFINITION 5. Soit \( f : I \rightarrow E \) une application, et supposons \( 0 \in I \) . Si \( n \in {\mathbb{N}}^{ * } \) , on dit que \( f \) admet un développement limité d’ordre \( n \) au voisinage de 0 s’il existe \( {a}_{0},{a}_{1},\ldots ,{a}_{n} \in E \) tels que, au voisinage de 0 ,

> DEFINITION 5. Let \( f : I \rightarrow E \) be a mapping, and assume \( 0 \in I \). If \( n \in {\mathbb{N}}^{ * } \), we say that \( f \) admits a Taylor expansion of order \( n \) in the neighborhood of 0 if there exist \( {a}_{0},{a}_{1},\ldots ,{a}_{n} \in E \) such that, in the neighborhood of 0,

\[
f\left( x\right)  = {a}_{0} + {a}_{1}x + \cdots  + {a}_{n}{x}^{n} + o\left( {x}^{n}\right) .
\]

Remarque 10. - Une définition équivalente est \( f\left( x\right) = {P}_{n}\left( x\right) + o\left( {x}^{n}\right) \) où \( {P}_{n} \) est une fonction polynomiale de degré \( \leq n \) .

> Remark 10. - An equivalent definition is \( f\left( x\right) = {P}_{n}\left( x\right) + o\left( {x}^{n}\right) \) where \( {P}_{n} \) is a polynomial function of degree \( \leq n \).

- On pourrait de même définir les développements limités au voisinage d'un point quelconque \( a \) de \( \bar{I} \) (en développant avec des termes de la forme \( \alpha {\left( x - a\right) }^{k} \) - ou \( 1/{x}^{k}, k \in  \mathbb{N} \) , lorsque \( a =  \pm  \infty ) \) . Nous avons choisi de nous limiter à \( a = 0 \) pour alléger les notations.

> - One could similarly define Taylor expansions in the neighborhood of any point \( a \) of \( \bar{I} \) (by expanding with terms of the form \( \alpha {\left( x - a\right) }^{k} \) - or \( 1/{x}^{k}, k \in  \mathbb{N} \), when \( a =  \pm  \infty ) \). We have chosen to limit ourselves to \( a = 0 \) to simplify the notation.

- Un développement limité est aussi un développement asymptotique par rapport à l’échelle de comparaison constituée des fonctions de la forme \( {x}^{n}\left( {n \in  \mathbb{N}}\right) \) .

> - A Taylor expansion is also an asymptotic expansion with respect to the comparison scale consisting of functions of the form \( {x}^{n}\left( {n \in  \mathbb{N}}\right) \).

Il découle de l'unicité d'un développement asymptotique le résultat suivant.

> The following result follows from the uniqueness of an asymptotic expansion.

Proposition 7. Si \( f \) admet un développement limité d’ordre \( n \in {\mathbb{N}}^{ * } \) , il est unique.

> Proposition 7. If \( f \) admits a Taylor expansion of order \( n \in {\mathbb{N}}^{ * } \), it is unique.

Proposition 8. Si \( f \) admet un développement limité d’ordre \( n \geq 1 \) au voisinage de 0

> Proposition 8. If \( f \) admits a Taylor expansion of order \( n \geq 1 \) in the neighborhood of 0

\[
f\left( x\right)  = {a}_{0} + {a}_{1}x + \cdots  + {a}_{n}{x}^{n} + o\left( {x}^{n}\right) ,
\]

alors \( f\left( 0\right) = {a}_{0}, f \) est dérivable en 0 et \( {f}^{\prime }\left( 0\right) = {a}_{1} \) .

> then \( f\left( 0\right) = {a}_{0}, f \) is differentiable at 0 and \( {f}^{\prime }\left( 0\right) = {a}_{1} \).

Remarque 11. Attention ! Même lorsque \( n \geq 2 \) , l’existence d’un développement limité d’ordre \( n \) n’assure pas l’existence de \( {f}^{\prime \prime }\left( 0\right) \) . Par exemple, la fonction \( f \) définie par

> Remark 11. Warning! Even when \( n \geq 2 \), the existence of a Taylor expansion of order \( n \) does not guarantee the existence of \( {f}^{\prime \prime }\left( 0\right) \). For example, the function \( f \) defined by

\[
f\left( x\right)  = 1 + x + {x}^{2} + {x}^{3}\sin \left( \frac{1}{{x}^{2}}\right) \;\text{ si }\;x \neq  0,\;f\left( 0\right)  = 1,
\]

n’est pas deux fois dérivable en 0, et pourtant elle vérifie \( f\left( x\right) = 1 + x + {x}^{2} + o\left( {x}^{2}\right) \) au voisinage de 0.

> is not twice differentiable at 0, and yet it satisfies \( f\left( x\right) = 1 + x + {x}^{2} + o\left( {x}^{2}\right) \) in the neighborhood of 0.

Proposition 9. Soit \( a > 0 \) et \( f : \rbrack - a, a\lbrack \rightarrow E \) une application admettant au voisinage de 0 un développement limité d’ordre \( n \in {\mathbb{N}}^{ * } \) :

> Proposition 9. Let \( a > 0 \) and \( f : \rbrack - a, a\lbrack \rightarrow E \) be a mapping admitting in the neighborhood of 0 a Taylor expansion of order \( n \in {\mathbb{N}}^{ * } \):

\[
f\left( x\right)  = {a}_{0} + {a}_{1}x + \cdots  + {a}_{n}{x}^{n} + o\left( {x}^{n}\right) .
\]

- Si \( f \) est paire, tous les termes \( {a}_{k} \) d’indices \( k \) impairs sont nuls.

> - If \( f \) is even, all terms \( {a}_{k} \) with odd indices \( k \) are zero.

- Si f est impaire, tous les termes \( {a}_{k} \) d’indices \( k \) pairs sont nuls.

> - If f is odd, all terms \( {a}_{k} \) with even indices \( k \) are zero.

Condition suffisante de l'existence d'un développement limité. La formule de Taylor-Young entraîne immédiatement le résultat suivant.

> Sufficient condition for the existence of a Taylor expansion. Taylor-Young's formula immediately implies the following result.

\( \rightarrow \) Proposition 10. Si \( f : I \rightarrow E \) est une application \( n \) fois dérivable en 0, alors \( f \) admet au voisinage de 0 le développement limité d’ordre \( n \) suivant :

> \( \rightarrow \) Proposition 10. If \( f : I \rightarrow E \) is a mapping that is \( n \) times differentiable at 0, then \( f \) admits the following Taylor expansion of order \( n \) in the neighborhood of 0:

\[
f\left( x\right)  = f\left( 0\right)  + {f}^{\prime }\left( 0\right) x + \cdots  + \frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{x}^{n} + o\left( {x}^{n}\right) .
\]
