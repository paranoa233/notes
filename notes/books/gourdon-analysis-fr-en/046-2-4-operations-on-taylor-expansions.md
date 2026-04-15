#### 2.4. Operations on Taylor expansions

*Français : 2.4. Opérations sur les développements limités*

Intégration terme à terme.

> Term-by-term integration.

Proposition 11. Soit \( f : I \rightarrow E \) (avec \( 0 \in I \) ) une application dérivable sur I telle qu’au voisinage de 0

> Proposition 11. Let \( f : I \rightarrow E \) (with \( 0 \in I \) ) be a mapping differentiable on I such that in the neighborhood of 0

\[
{f}^{\prime }\left( x\right)  = {a}_{0} + {a}_{1}x + \cdots  + {a}_{n}{x}^{n} + o\left( {x}^{n}\right) .
\]

Alors l’application \( f \) admet au voisinage de 0 le développement limité d’ordre \( n + 1 \) suivant

> Then the mapping \( f \) admits the following Taylor expansion of order \( n + 1 \) in the neighborhood of 0

\[
f\left( x\right)  = f\left( 0\right)  + {a}_{0}x + \frac{{a}_{1}}{2}{x}^{2} + \cdots  + \frac{{a}_{n}}{n + 1}{x}^{n + 1} + o\left( {x}^{n + 1}\right) .
\]

Dérivation d'un développement de Taylor.

> Differentiation of a Taylor expansion.

Proposition 12. Soit \( f : I \rightarrow E \) (avec \( 0 \in I \) ) une application \( n \geq 2 \) fois dérivable en 0. Si au voisinage de 0, on a

> Proposition 12. Let \( f : I \rightarrow E \) (with \( 0 \in I \) ) be a mapping \( n \geq 2 \) times differentiable at 0. If in the neighborhood of 0, we have

\[
f\left( x\right)  = {a}_{0} + {a}_{1}x + \cdots  + {a}_{n}{x}^{n} + o\left( {x}^{n}\right) ,
\]

alors au voisinage de 0 ,

> then in the neighborhood of 0,

\[
{f}^{\prime }\left( x\right)  = {a}_{1} + 2{a}_{2}x + \cdots  + n{a}_{n}{x}^{n - 1} + o\left( {x}^{n - 1}\right) .
\]

Remarque 12. Sans l’hypothèse d’existence de \( {f}^{\left( n\right) }\left( 0\right) \) , le résultat est faux. Considérez par exemple l’application \( f \) introduite à la remarque \( {11} : f \) admet un développement limité d’ordre 2 et pourtant, \( {f}^{\prime }\left( x\right) \) qui existe sur un voisinage de 0, n’admet pas de développement limité au voisinage de \( 0\left( {f}^{\prime }\right. \) n’a pas de limite en \( \left. 0\right) \) .

> Remark 12. Without the assumption of the existence of \( {f}^{\left( n\right) }\left( 0\right) \) , the result is false. Consider for example the mapping \( f \) introduced in remark \( {11} : f \) which admits a Taylor expansion of order 2, and yet, \( {f}^{\prime }\left( x\right) \) which exists in a neighborhood of 0, does not admit a Taylor expansion in the neighborhood of \( 0\left( {f}^{\prime }\right. \) and has no limit at \( \left. 0\right) \) .

##### Sum, product, quotient of Taylor expansions.

*Français : Somme, produit, quotient de développements limités.*

Proposition 13. Soient \( f \) et \( g : I \rightarrow E \) (avec \( 0 \in I \) ) deux applications admettant au voisinage de 0 un développement limité d’ordre \( n \) :

> Proposition 13. Let \( f \) and \( g : I \rightarrow E \) (with \( 0 \in I \) ) be two mappings admitting a Taylor expansion of order \( n \) in the neighborhood of 0:

\[
f\left( x\right)  = {P}_{n}\left( x\right)  + o\left( {x}^{n}\right) ,\;g\left( x\right)  = {Q}_{n}\left( x\right)  + o\left( {x}^{n}\right) ,
\]

où \( {P}_{n} \) et \( {Q}_{n} \) sont deux fonctions polynomiales de degré \( \leq n \) . Alors

> where \( {P}_{n} \) and \( {Q}_{n} \) are two polynomial functions of degree \( \leq n \) . Then

- la somme \( f + g \) admet un développement limité d’ordre \( n \) donné par \( \left( {f + g}\right) \left( x\right)  = \; \left( {{P}_{n} + {Q}_{n}}\right) \left( x\right)  + o\left( {x}^{n}\right) , \)

> - the sum \( f + g \) admits a Taylor expansion of order \( n \) given by \( \left( {f + g}\right) \left( x\right)  = \; \left( {{P}_{n} + {Q}_{n}}\right) \left( x\right)  + o\left( {x}^{n}\right) , \)

- Si E est une algèbre normée, le produit fg admet un développement limité d'ordre n donné par \( \left( {fg}\right) \left( x\right)  = {R}_{n}\left( x\right)  + o\left( {x}^{n}\right) \) , où \( {R}_{n} \) est le reste de la division euclidienne de \( {P}_{n}{Q}_{n} \) par \( {X}^{n + 1} : {P}_{n}{Q}_{n} = {R}_{n} + {X}^{n + 1}{S}_{n} \) avec \( \deg \left( {R}_{n}\right)  \leq  n \) ,

> - If E is a normed algebra, the product fg admits a Taylor expansion of order n given by \( \left( {fg}\right) \left( x\right)  = {R}_{n}\left( x\right)  + o\left( {x}^{n}\right) \) , where \( {R}_{n} \) is the remainder of the Euclidean division of \( {P}_{n}{Q}_{n} \) by \( {X}^{n + 1} : {P}_{n}{Q}_{n} = {R}_{n} + {X}^{n + 1}{S}_{n} \) with \( \deg \left( {R}_{n}\right)  \leq  n \) ,

- Si \( E = \mathbb{R} \) on \( E = \mathbb{C} \) , et si \( g\left( 0\right)  = Q\left( 0\right)  \neq  0 \) , le quotient \( f/g \) admet un développement limité d’ordre n donné par \( \left( {f/g}\right) \left( x\right)  = {R}_{n}\left( x\right)  + o\left( {x}^{n}\right) \) , où \( {R}_{n} \) est le quotient de la division selon les puissances croissantes de \( {P}_{n} \) par \( {Q}_{n} \) à l’ordre n.

> - If \( E = \mathbb{R} \) as \( E = \mathbb{C} \) , and if \( g\left( 0\right)  = Q\left( 0\right)  \neq  0 \) , the quotient \( f/g \) admits a Taylor expansion of order n given by \( \left( {f/g}\right) \left( x\right)  = {R}_{n}\left( x\right)  + o\left( {x}^{n}\right) \) , where \( {R}_{n} \) is the quotient of the division of \( {P}_{n} \) by \( {Q}_{n} \) in increasing powers up to order n.

##### Taylor expansion of a composite function.

*Français : Développement limité d'une fonction composée.*

Proposition 14. Soient \( g : \;I \rightarrow \mathbb{R} \) (avec \( 0 \in I \) ) une application admettant un développement limité d’ordre \( n \) au voisinage de 0, et \( f : J \rightarrow E \) (où \( J \) est un inter-valle de \( \mathbb{R} \) tel que \( g\left( I\right) \subset J \) ) une application admettant un développement limité d’ordre \( n \) au voisinage de \( {g}_{0} = g\left( 0\right) \) . On écrit, au voisinage de 0,

> Proposition 14. Let \( g : \;I \rightarrow \mathbb{R} \) (with \( 0 \in I \) ) be a mapping admitting a Taylor expansion of order \( n \) in the neighborhood of 0, and \( f : J \rightarrow E \) (where \( J \) is an interval of \( \mathbb{R} \) such that \( g\left( I\right) \subset J \) ) be a mapping admitting a Taylor expansion of order \( n \) in the neighborhood of \( {g}_{0} = g\left( 0\right) \) . We write, in the neighborhood of 0,

\[
g\left( x\right)  = {g}_{0} + {P}_{n}\left( x\right)  + o\left( {x}^{n}\right) \;\text{ et }\;f\left( {{g}_{0} + t}\right)  = {Q}_{n}\left( t\right)  + o\left( {t}^{n}\right) ,
\]

où \( {P}_{n} \) et \( {Q}_{n} \) sont deux polynómes de degré \( \leq n \) avec \( {P}_{n}\left( 0\right) = 0 \) . Alors la fonction composée \( f \circ g \) admet au voisinage de 0 un développement limité d’ordre \( n : f \circ g\left( x\right) = R,\left( x\right) + o\left( {x}^{n}\right) \) , où \( {R}_{n} \) est le reste de la division euclidienne de \( {P}_{n} \circ {Q}_{n} \) par \( {X}^{n + 1}\left( {{P}_{n} \circ {Q}_{n} = {R}_{n} + {X}^{n + 1}{S}_{n}}\right. \) , \( \left. {\deg \left( {R}_{n}\right) \leq n}\right) \) .

> where \( {P}_{n} \) and \( {Q}_{n} \) are two polynomials of degree \( \leq n \) with \( {P}_{n}\left( 0\right) = 0 \) . Then the composite function \( f \circ g \) admits a Taylor expansion of order \( n : f \circ g\left( x\right) = R,\left( x\right) + o\left( {x}^{n}\right) \) in the neighborhood of 0, where \( {R}_{n} \) is the remainder of the Euclidean division of \( {P}_{n} \circ {Q}_{n} \) by \( {X}^{n + 1}\left( {{P}_{n} \circ {Q}_{n} = {R}_{n} + {X}^{n + 1}{S}_{n}}\right. \) , \( \left. {\deg \left( {R}_{n}\right) \leq n}\right) \) .
