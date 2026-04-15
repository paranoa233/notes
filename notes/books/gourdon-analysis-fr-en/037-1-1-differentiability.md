#### 1.1. Differentiability

*Français : 1.1. Dérivabilité*

DéFINITION 1. Soient \( E \) un \( \mathbb{R} \) -e.v.n, \( I \) un intervalle de \( \mathbb{R}, f : I \rightarrow E \) une application et \( a \in I \) . On dit que \( f \) est dérivable en \( a \) si

> DEFINITION 1. Let \( E \) be a \( \mathbb{R} \) -normed vector space, \( I \) an interval of \( \mathbb{R}, f : I \rightarrow E \) , a mapping, and \( a \in I \) . We say that \( f \) is differentiable at \( a \) if

\[
\mathop{\lim }\limits_{\substack{{t \rightarrow  a} \\  {t \in  I\smallsetminus \{ a\} } }}\frac{f\left( t\right)  - f\left( a\right) }{t - a}
\]

existe. Lorsqu’elle existe, cette limite est notée \( {f}^{\prime }\left( a\right) \) (ou \( \frac{df}{dx}\left( a\right) \) ).

> exists. When it exists, this limit is denoted \( {f}^{\prime }\left( a\right) \) (or \( \frac{df}{dx}\left( a\right) \) ).

On dit que \( f \) est dérivable à gauche (resp. \( \dot{a} \) droite) en \( a \) si la limite

> We say that \( f \) is differentiable on the left (resp. \( \dot{a} \) right) at \( a \) if the limit

\[
\mathop{\lim }\limits_{\substack{{t \rightarrow  a} \\  {t \in  I} }}\frac{f\left( t\right)  - f\left( a\right) }{t - a}\;\left( {\text{ resp. }\mathop{\lim }\limits_{\substack{{t \rightarrow  a} \\  {t \in  I} }}\frac{f\left( t\right)  - f\left( a\right) }{t - a}}\right)
\]

existe. On la note alors \( {f}_{\mathrm{g}}^{\prime }\left( a\right) \) (resp. \( {f}_{\mathrm{d}}^{\prime }\left( a\right) \) ).

> exists. It is then denoted \( {f}_{\mathrm{g}}^{\prime }\left( a\right) \) (resp. \( {f}_{\mathrm{d}}^{\prime }\left( a\right) \) ).

Remarque 1. - Si \( a \in I, f \) est dérivable en \( a \) si et seulement si \( f \) est dérivable à gauche, dérivable à droite en \( a \) et \( {f}_{\mathrm{g}}^{\prime }\left( a\right) = {f}_{\mathrm{d}}^{\prime }\left( a\right) \) .

> Remark 1. - \( a \in I, f \) is differentiable at \( a \) if and only if \( f \) is differentiable on the left, differentiable on the right at \( a \) , and \( {f}_{\mathrm{g}}^{\prime }\left( a\right) = {f}_{\mathrm{d}}^{\prime }\left( a\right) \) .

- Si \( f \) est dérivable en \( a, f \) est continue en \( a \) .

> - If \( f \) is differentiable at \( a, f \) , it is continuous at \( a \) .

- Sur l’ensemble \( D \) des points où \( f \) est dérivable, on peut définir l’application \( a \mapsto \; {f}^{\prime }\left( a\right) \) appelée application dérivée de \( f \) et notée \( {f}^{\prime } \) .

> - On the set \( D \) of points where \( f \) is differentiable, we can define the mapping \( a \mapsto \; {f}^{\prime }\left( a\right) \) called the derivative mapping of \( f \) and denoted \( {f}^{\prime } \) .

- L’application \( f \) est dérivable en \( a \) si et seulement si

> - The mapping \( f \) is differentiable at \( a \) if and only if

\[
\exists \ell  \in  E,\;f\left( x\right)  = f\left( a\right)  + \left( {x - a}\right) \ell  + o\left( {x - a}\right) \;\left( {x \rightarrow  a}\right) .
\]

On a alors \( \ell = {f}^{\prime }\left( a\right) \) .

> We then have \( \ell = {f}^{\prime }\left( a\right) \) .

- Une fonction dérivée n'est pas forcément continue. Considérons par exemple

> - A derivative function is not necessarily continuous. Consider for example

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  {x}^{2}\sin \left( {1/x}\right) \text{ si }x \neq  0,\;0 \mapsto  0.
\]

Si \( x \neq 0, f \) est dérivable en \( x \) et on a \( {f}^{\prime }\left( x\right) = {2x}\sin \left( {1/x}\right) - \cos \left( {1/x}\right) \) . En 0, comme \( - {x}^{2} \leq f\left( x\right) \leq {x}^{2} \) pour tout \( x \) , on a

> If \( x \neq 0, f \) is differentiable at \( x \) and we have \( {f}^{\prime }\left( x\right) = {2x}\sin \left( {1/x}\right) - \cos \left( {1/x}\right) \) . At 0, since \( - {x}^{2} \leq f\left( x\right) \leq {x}^{2} \) for all \( x \) , we have

\[
- x \leq  \frac{f\left( x\right)  - f\left( 0\right) }{x - 0} \leq  x\;\text{ donc }\;\mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x \neq  0} }}\frac{f\left( x\right)  - f\left( 0\right) }{x} = 0,
\]

en d’autres termes, \( {f}^{\prime }\left( 0\right) \) existe et vaut 0 . Cependant, on voit que \( {f}^{\prime }\left( x\right) \) n’admet pas de limite lorsque \( x \) tend vers 0 .

> in other words, \( {f}^{\prime }\left( 0\right) \) exists and equals 0. However, we see that \( {f}^{\prime }\left( x\right) \) does not have a limit as \( x \) approaches 0.

— Nous verrons cependant qu'une fonction dérivée vérifie toujours la propriété des va-leurs intermédiaires (théorème de Darboux, voir l'exercice 4 page 80) et est continue sur un ensemble dense (voir l'exercice 2 page 419). Par contre, il existe des fonctions dérivées discontinues sur un ensemble dense (voir l'exercice 9 page 244).

> — We will see, however, that a derivative function always satisfies the intermediate value property (Darboux's theorem, see exercise 4 page 80) and is continuous on a dense set (see exercise 2 page 419). Conversely, there exist derivative functions that are discontinuous on a dense set (see exercise 9 page 244).

- Une fonction dérivée, même bornée, n'est pas nécessairement Riemann-intégrable.

> - A derivative function, even if bounded, is not necessarily Riemann-integrable.

Par récurrence, on peut définir la fonction dérivée \( n \) -ième (lorsqu’elle existe) par

> By induction, one can define the \( n \)-th derivative function (when it exists) by

\[
{f}^{\prime \prime } = {\left( {f}^{\prime }\right) }^{\prime },\;{f}^{\prime \prime \prime } = {\left( {f}^{\prime \prime }\right) }^{\prime },\ldots ,{f}^{\left( n\right) } = {\left( {f}^{\left( n - 1\right) }\right) }^{\prime },\ldots .
\]

Une application \( f : I \rightarrow E \) est dite de classe \( {\mathcal{C}}^{n} \) si \( {f}^{\left( n\right) } \) existe sur \( I \) et y est continue. On note parfois \( {\mathcal{C}}^{n}\left( {I, E}\right) \) l’ensemble des applications de classe \( {\mathcal{C}}^{n} \) de \( I \) dans \( E \) . Lorsque \( f \) est de classe \( {\mathcal{C}}^{n} \) pour tout \( n \) , on dit que \( f \) est de classe \( {\mathcal{C}}^{\infty } \) .

> A mapping \( f : I \rightarrow E \) is said to be of class \( {\mathcal{C}}^{n} \) if \( {f}^{\left( n\right) } \) exists on \( I \) and is continuous there. We sometimes denote by \( {\mathcal{C}}^{n}\left( {I, E}\right) \) the set of mappings of class \( {\mathcal{C}}^{n} \) from \( I \) to \( E \). When \( f \) is of class \( {\mathcal{C}}^{n} \) for all \( n \), we say that \( f \) is of class \( {\mathcal{C}}^{\infty } \).

Proposition 1. Soient \( I \) un intervalle de \( \mathbb{R}, f \) et \( g \) deux applications de \( I \) dans \( E \) (où \( E \) est un \( \mathbb{R} \) -e.v.n), dérivables en \( a \in I \) . Alors

> Proposition 1. Let \( I \) be an interval of \( \mathbb{R}, f \) and \( g \) be two mappings from \( I \) to \( E \) (where \( E \) is a \( \mathbb{R} \)-n.v.s.), differentiable at \( a \in I \). Then

(i) Pour tout \( \lambda ,\mu \in \mathbb{R},{\lambda f} + {\mu g} \) est dérivable en a et \( {\left( \lambda f + \mu g\right) }^{\prime }\left( a\right) = \lambda {f}^{\prime }\left( a\right) + \mu {g}^{\prime }\left( a\right) \) .

> (i) For all \( \lambda ,\mu \in \mathbb{R},{\lambda f} + {\mu g} \), it is differentiable at a and \( {\left( \lambda f + \mu g\right) }^{\prime }\left( a\right) = \lambda {f}^{\prime }\left( a\right) + \mu {g}^{\prime }\left( a\right) \).

(ii) \( {SiE} \) est une \( \mathbb{R} \) -algèbre normée, le produit \( {fg} \) est dérivable en a et

> (ii) \( {SiE} \) is a \( \mathbb{R} \)-normed algebra, the product \( {fg} \) is differentiable at a and

\[
{\left( fg\right) }^{\prime }\left( a\right)  = {f}^{\prime }\left( a\right) g\left( a\right)  + f\left( a\right) {g}^{\prime }\left( a\right) .
\]

(iii) \( {SiE} = \mathbb{R} \) ou \( \mathbb{C} \) et si \( g\left( a\right) \neq 0 \) , le rapport \( f/g \) est dérivable en a et

> (iii) \( {SiE} = \mathbb{R} \) or \( \mathbb{C} \) and if \( g\left( a\right) \neq 0 \), the ratio \( f/g \) is differentiable at a and

\[
{\left( \frac{f}{g}\right) }^{\prime }\left( a\right)  = \frac{{f}^{\prime }\left( a\right) g\left( a\right)  - f\left( a\right) {g}^{\prime }\left( a\right) }{g{\left( a\right) }^{2}}.
\]

Conséquence : En procédant par récurrence, on en déduit que la somme, le produit, le rapport de deux fonctions de classe \( {\mathcal{C}}^{n} \) est de classe \( {\mathcal{C}}^{n} \) .

> Consequence: By proceeding by induction, we deduce that the sum, product, and ratio of two functions of class \( {\mathcal{C}}^{n} \) are of class \( {\mathcal{C}}^{n} \).

Proposition 2 (FORMULE DE LEIBNIZ). Soient I un intervalle de \( \mathbb{R} \) , \( f \) et \( g \) deux applications de I dans une \( \mathbb{R} \) -algèbre normée \( E \) et \( a \in I \) tel que \( {f}^{\left( n\right) }\left( a\right) \) et \( {g}^{\left( n\right) }\left( a\right) \) existent. Alors le produit \( {fg} \) est \( n \) fois dérivable en a et

> Proposition 2 (LEIBNIZ FORMULA). Let I be an interval of \( \mathbb{R} \), \( f \) and \( g \) be two mappings from I into a \( \mathbb{R} \)-normed algebra \( E \), and \( a \in I \) such that \( {f}^{\left( n\right) }\left( a\right) \) and \( {g}^{\left( n\right) }\left( a\right) \) exist. Then the product \( {fg} \) is \( n \) times differentiable at a and

\[
{\left( fg\right) }^{\left( n\right) }\left( a\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{f}^{\left( k\right) }\left( a\right) {g}^{\left( n - k\right) }\left( a\right) ,
\]

où par convention \( {f}^{\left( 0\right) } = f \) et \( {g}^{\left( 0\right) } = g \) .

> where by convention \( {f}^{\left( 0\right) } = f \) and \( {g}^{\left( 0\right) } = g \).

Proposition 3. Soient I et \( J \) deux intervalles de \( \mathbb{R}, E \) un \( \mathbb{R} \) -e.v.n, \( f : J \rightarrow E \) et \( g : I \rightarrow J \) deux applications, et \( a \in I \) tel que \( f \) est dérivable en a et \( g \) dérivable en \( f\left( a\right) \) . L’application composée \( f \circ g \) est dérivable en a et on a

> Proposition 3. Let I and \( J \) be two intervals of \( \mathbb{R}, E \), a \( \mathbb{R} \)-n.v.s., \( f : J \rightarrow E \) and \( g : I \rightarrow J \) two mappings, and \( a \in I \) such that \( f \) is differentiable at a and \( g \) is differentiable at \( f\left( a\right) \). The composite mapping \( f \circ g \) is differentiable at a and we have

\[
{\left( f \circ  g\right) }^{\prime }\left( a\right)  = {g}^{\prime }\left( a\right)  \cdot  \left( {{f}^{\prime } \circ  g}\right) \left( a\right) .
\]

Conséquence : On en déduit que la composée de deux applications de classe \( {\mathcal{C}}^{n} \) est de classe \( {\mathcal{C}}^{n} \) (procéder par récurrence sur \( n \) ).

> Consequence: We deduce that the composition of two mappings of class \( {\mathcal{C}}^{n} \) is of class \( {\mathcal{C}}^{n} \) (proceed by induction on \( n \)).

Homéomorphismes dérivables. Les lettres \( I \) et \( J \) désignent deux intervalles de \( \mathbb{R} \) .

> Differentiable homeomorphisms. The letters \( I \) and \( J \) denote two intervals of \( \mathbb{R} \).

DÉFINITION 2. Soient \( f : I \rightarrow J \) une bijection et \( n \in {\mathbb{N}}^{ * } \) . On dit que \( f \) est un \( {\mathcal{C}}^{n} \) - difféomorphisme si \( f \) et \( {f}^{-1} \) sont de classe \( {\mathcal{C}}^{n} \) .

> DEFINITION 2. Let \( f : I \rightarrow J \) be a bijection and \( n \in {\mathbb{N}}^{ * } \) . We say that \( f \) is a \( {\mathcal{C}}^{n} \) -diffeomorphism if \( f \) and \( {f}^{-1} \) are of class \( {\mathcal{C}}^{n} \) .

Proposition 4. Soit \( f \) une bijection de I dans \( J \) , dérivable en \( a \in I \) . L’application \( {f}^{-1} \) est dérivable en \( b = f\left( a\right) \) si et seulement si \( {f}^{\prime }\left( a\right) \neq 0 \) , et on a

> Proposition 4. Let \( f \) be a bijection from I to \( J \) , differentiable at \( a \in I \) . The map \( {f}^{-1} \) is differentiable at \( b = f\left( a\right) \) if and only if \( {f}^{\prime }\left( a\right) \neq 0 \) , and we have

\[
{\left( {f}^{-1}\right) }^{\prime }\left( b\right)  = \frac{1}{{f}^{\prime }\left( a\right) } = \frac{1}{{f}^{\prime }\left( {{f}^{-1}\left( b\right) }\right) }.
\]

Conséquence : Une fonction surjective \( f \) de \( I \) dans \( J \) est un \( {\mathcal{C}}^{n} \) -difféomorphisme si et seulement si \( f \) et de classe \( {\mathcal{C}}^{n} \) et vérifie \( {f}^{\prime }\left( a\right) \neq 0 \) pour tout \( a \in I \) (l’injectivité découle du théorème de Rolle).

> Consequence: A surjective function \( f \) from \( I \) to \( J \) is a \( {\mathcal{C}}^{n} \) -diffeomorphism if and only if \( f \) is of class \( {\mathcal{C}}^{n} \) and satisfies \( {f}^{\prime }\left( a\right) \neq 0 \) for all \( a \in I \) (injectivity follows from Rolle's theorem).
