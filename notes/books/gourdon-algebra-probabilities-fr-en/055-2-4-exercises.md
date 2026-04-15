#### 2.4. Exercises

*Français : 2.4. Exercices*

EXERCICE 1. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie et \( F \) un \( \mathbb{K} \) -e.v.

> EXERCISE 1. Let \( E \) be a finite-dimensional \( \mathbb{K} \)-v.s. and \( F \) be a \( \mathbb{K} \)-v.s.

a) Soient \( f, g \in \mathcal{L}\left( {E, F}\right) \) . Montrer les inégalités

> a) Let \( f, g \in \mathcal{L}\left( {E, F}\right) \). Show the inequalities

\[
\left| {\operatorname{rg}f - \operatorname{rg}g}\right|  \leq  \operatorname{rg}\left( {f + g}\right)  \leq  \operatorname{rg}f + \operatorname{rg}g
\]

b) Soient deux endomorphismes \( f, g \in \mathcal{L}\left( E\right) \) tels que \( {fg} = 0 \) et \( f + g \) est inversible. Montrer que \( \operatorname{rg}f + \operatorname{rg}g = \dim E \) .

> b) Let two endomorphisms \( f, g \in \mathcal{L}\left( E\right) \) such that \( {fg} = 0 \) and \( f + g \) is invertible. Show that \( \operatorname{rg}f + \operatorname{rg}g = \dim E \).

Solution. a) \( \operatorname{Im}\left( {f + g}\right) = \left( {f + g}\right) \left( E\right) \subset f\left( E\right) + g\left( E\right) \) , donc

> Solution. a) \( \operatorname{Im}\left( {f + g}\right) = \left( {f + g}\right) \left( E\right) \subset f\left( E\right) + g\left( E\right) \), therefore

\[
\operatorname{rg}\left( {f + g}\right)  = \dim \left( {\operatorname{Im}\left( {f + g}\right) }\right)  \leq  \dim \left\lbrack  {f\left( E\right)  + g\left( E\right) }\right\rbrack   \leq  \dim f\left( E\right)  + \dim g\left( E\right)  = \operatorname{rg}f + \operatorname{rg}g.
\]

Comme \( f = \left( {f + g}\right) + \left( {-g}\right) \) et que \( \operatorname{rg}g = \operatorname{rg}\left( {-g}\right) \) , on a aussi \( \operatorname{rg}f \leq \operatorname{rg}\left( {f + g}\right) + \operatorname{rg}g \) . De même, \( \operatorname{rg}g \leq \operatorname{rg}\left( {f + g}\right) + \operatorname{rg}f \) . On en déduit finalement que \( \left| {\operatorname{rg}f - \operatorname{rg}g}\right| \leq \operatorname{rg}\left( {f + g}\right) \) .

> Since \( f = \left( {f + g}\right) + \left( {-g}\right) \) and \( \operatorname{rg}g = \operatorname{rg}\left( {-g}\right) \), we also have \( \operatorname{rg}f \leq \operatorname{rg}\left( {f + g}\right) + \operatorname{rg}g \). Similarly, \( \operatorname{rg}g \leq \operatorname{rg}\left( {f + g}\right) + \operatorname{rg}f \). We finally deduce that \( \left| {\operatorname{rg}f - \operatorname{rg}g}\right| \leq \operatorname{rg}\left( {f + g}\right) \).

b) Comme \( f + g \) est inversible, \( \operatorname{rg}\left( {f + g}\right) = \dim E \) , donc d’après a),

> b) Since \( f + g \) is invertible, \( \operatorname{rg}\left( {f + g}\right) = \dim E \), therefore according to a),

\[
\operatorname{rg}f + \operatorname{rg}g \geq  \operatorname{rg}\left( {f + g}\right)  = \dim E.
\]

(*)

> Comme \( {fg} = 0 \) , on a \( \operatorname{Im}g \subset \operatorname{Ker}f \) , donc \( \operatorname{rg}g \leq \dim \left( {\operatorname{Ker}f}\right) = \dim E - \operatorname{rg}f \) , c’est-à-dire \( \operatorname{rg}f + \operatorname{rg}g \leq \dim E \) . Avec (*), on en déduit le résultat.

As \( {fg} = 0 \) , we have \( \operatorname{Im}g \subset \operatorname{Ker}f \) , therefore \( \operatorname{rg}g \leq \dim \left( {\operatorname{Ker}f}\right) = \dim E - \operatorname{rg}f \) , that is to say \( \operatorname{rg}f + \operatorname{rg}g \leq \dim E \) . With (*), we deduce the result.

> EXERCICE 2. Soit \( E \) un \( \mathbb{K} \) -e.v (où \( \mathbb{K} \) est de caractéristique différente de 2), et \( p, q \in \mathcal{L}\left( E\right) \) deux projecteurs.

EXERCISE 2. Let \( E \) be a \( \mathbb{K} \) -v.s. (where \( \mathbb{K} \) is of characteristic different from 2), and \( p, q \in \mathcal{L}\left( E\right) \) two projectors.

> a) Montrer que \( p + q \) est un projecteur si et seulement si \( p \circ q = q \circ p = 0 \) .

a) Show that \( p + q \) is a projector if and only if \( p \circ q = q \circ p = 0 \) .

> b) Montrer que si \( p + q \) est un projecteur,

b) Show that if \( p + q \) is a projector,

\[
\operatorname{Im}\left( {p + q}\right)  = \operatorname{Im}p \oplus  \operatorname{Im}q\;\text{ et }\;\operatorname{Ker}\left( {p + q}\right)  = \operatorname{Ker}p \cap  \operatorname{Ker}q.
\]

Solution. a) Condition nécessaire. Comme \( p + q \) est un projecteur, on a \( {\left( p + q\right) }^{2} = p + q \) , c’est-à- dire \( {p}^{2} + p \circ q + q \circ p + {q}^{2} = p + q \) . Or \( {p}^{2} = p \) et \( {q}^{2} = q \) , donc \( p \circ q + q \circ p = 0\;\left( *\right) \) . En composant (*) par \( p \) à droite, on obtient \( p \circ q \circ p + q \circ {p}^{2} = 0 = p \circ q \circ p + q \circ p \) . En composant (*) par \( p \) à gauche, on obtient \( {p}^{2} \circ q + p \circ q \circ p = 0 = p \circ q + p \circ q \circ p \) . On en déduit \( p \circ q = q \circ p \) , et d’après \( \left( *\right) ,\mathbb{K} \) étant de caractéristique différente de \( 2, p \circ q = q \circ p = 0 \) .

> Solution. a) Necessary condition. As \( p + q \) is a projector, we have \( {\left( p + q\right) }^{2} = p + q \) , that is to say \( {p}^{2} + p \circ q + q \circ p + {q}^{2} = p + q \) . Now \( {p}^{2} = p \) and \( {q}^{2} = q \) , therefore \( p \circ q + q \circ p = 0\;\left( *\right) \) . By composing (*) with \( p \) on the right, we obtain \( p \circ q \circ p + q \circ {p}^{2} = 0 = p \circ q \circ p + q \circ p \) . By composing (*) with \( p \) on the left, we obtain \( {p}^{2} \circ q + p \circ q \circ p = 0 = p \circ q + p \circ q \circ p \) . We deduce \( p \circ q = q \circ p \) , and according to \( \left( *\right) ,\mathbb{K} \) being of characteristic different from \( 2, p \circ q = q \circ p = 0 \) .

Condition suffisante. C’est immédiat car \( {\left( p + q\right) }^{2} = {p}^{2} + p \circ q + q \circ p + {q}^{2} = {p}^{2} + {q}^{2} = p + q \) .

> Sufficient condition. It is immediate because \( {\left( p + q\right) }^{2} = {p}^{2} + p \circ q + q \circ p + {q}^{2} = {p}^{2} + {q}^{2} = p + q \) .

b) Montrons que \( \operatorname{Im}\left( {p + q}\right) = \operatorname{Im}p \oplus \operatorname{Im}q \) .

> b) Let us show that \( \operatorname{Im}\left( {p + q}\right) = \operatorname{Im}p \oplus \operatorname{Im}q \) .

- On a déjà Im \( p \cap  \operatorname{Im}q = \{ 0\} \) . En effet. Soit \( y \in  \operatorname{Im}p \cap  \operatorname{Im}q \) . Il existe \( x \) et \( {x}^{\prime } \in  E \) tels que \( y = p\left( x\right)  = q\left( {x}^{\prime }\right) \) . Donc \( p\left( y\right)  = {p}^{2}\left( x\right)  = p \circ  q\left( {x}^{\prime }\right)  = 0 \) d’après la question précédente. Or \( {p}^{2}\left( x\right)  = p\left( x\right)  = y \) , donc \( y = 0 \) .

> - We already have Im \( p \cap  \operatorname{Im}q = \{ 0\} \) . Indeed. Let \( y \in  \operatorname{Im}p \cap  \operatorname{Im}q \) . There exist \( x \) and \( {x}^{\prime } \in  E \) such that \( y = p\left( x\right)  = q\left( {x}^{\prime }\right) \) . Therefore \( p\left( y\right)  = {p}^{2}\left( x\right)  = p \circ  q\left( {x}^{\prime }\right)  = 0 \) according to the previous question. Now \( {p}^{2}\left( x\right)  = p\left( x\right)  = y \) , therefore \( y = 0 \) .

- Il nous reste à montrer que \( \operatorname{Im}\left( {p + q}\right)  = \operatorname{Im}p + \operatorname{Im}q \) . L’inclusion \( \operatorname{Im}\left( {p + q}\right)  \subset  \operatorname{Im}p + \operatorname{Im}q \) est immédiate. Montrons l’inclusion réciproque. Soit \( y \in  \operatorname{Im}p + \operatorname{Im}q \) , de sorte qu’il existe \( x \) et \( {x}^{\prime } \in  E \) tels que \( y = p\left( x\right)  + q\left( {x}^{\prime }\right) \) . On a alors \( \left( {p + q}\right) \left( y\right)  = {p}^{2}\left( x\right)  + {qp}\left( x\right)  + {q}^{2}\left( {x}^{\prime }\right)  + {pq}\left( {x}^{\prime }\right)  = p\left( x\right)  + q\left( {x}^{\prime }\right)  = y \) , donc \( y = \left( {p + q}\right) \left( y\right)  \in  \operatorname{Im}\left( {p + q}\right) \) , d’où le résultat.

> - It remains for us to show that \( \operatorname{Im}\left( {p + q}\right)  = \operatorname{Im}p + \operatorname{Im}q \) . The inclusion \( \operatorname{Im}\left( {p + q}\right)  \subset  \operatorname{Im}p + \operatorname{Im}q \) is immediate. Let us show the reverse inclusion. Let \( y \in  \operatorname{Im}p + \operatorname{Im}q \) , such that there exist \( x \) and \( {x}^{\prime } \in  E \) with \( y = p\left( x\right)  + q\left( {x}^{\prime }\right) \) . We then have \( \left( {p + q}\right) \left( y\right)  = {p}^{2}\left( x\right)  + {qp}\left( x\right)  + {q}^{2}\left( {x}^{\prime }\right)  + {pq}\left( {x}^{\prime }\right)  = p\left( x\right)  + q\left( {x}^{\prime }\right)  = y \) , therefore \( y = \left( {p + q}\right) \left( y\right)  \in  \operatorname{Im}\left( {p + q}\right) \) , hence the result.

Montrons maintenant que \( \operatorname{Ker}\left( {p + q}\right) = \operatorname{Ker}p \cap \operatorname{Ker}q \) . L’inclusion \( \operatorname{Ker}p \cap \operatorname{Ker}q \subset \operatorname{Ker}\left( {p + q}\right) \) est immédiate. Montrons l’inclusion réciproque. Soit \( x \in \operatorname{Ker}\left( {p + q}\right) \) . Comme \( p\left( x\right) + q\left( x\right) = 0 \) , on a, en composant par \( p \) à droite \( {p}^{2}\left( x\right) + q \circ p\left( x\right) = 0 \) d’où \( p\left( x\right) = 0 \) . De même, en composant par \( q \) à droite, on obtient \( p \circ q\left( x\right) + {q}^{2}\left( x\right) = 0 = q\left( x\right) \) . Donc \( x \in \operatorname{Ker}p \cap \operatorname{Ker}q \) .

> Let us now show that \( \operatorname{Ker}\left( {p + q}\right) = \operatorname{Ker}p \cap \operatorname{Ker}q \) . The inclusion \( \operatorname{Ker}p \cap \operatorname{Ker}q \subset \operatorname{Ker}\left( {p + q}\right) \) is immediate. Let us show the reverse inclusion. Let \( x \in \operatorname{Ker}\left( {p + q}\right) \) . Since \( p\left( x\right) + q\left( x\right) = 0 \) , we have, by composing with \( p \) on the right \( {p}^{2}\left( x\right) + q \circ p\left( x\right) = 0 \) whence \( p\left( x\right) = 0 \) . Similarly, by composing with \( q \) on the right, we obtain \( p \circ q\left( x\right) + {q}^{2}\left( x\right) = 0 = q\left( x\right) \) . Thus \( x \in \operatorname{Ker}p \cap \operatorname{Ker}q \) .

EXERCICE 3. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, soit \( f \in \mathcal{L}\left( E\right) \) . Montrer l’équivalence

> EXERCISE 3. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., let \( f \in \mathcal{L}\left( E\right) \) . Show the equivalence

\[
\left( {E = \operatorname{Im}f \oplus  \operatorname{Ker}f}\right)  \Leftrightarrow  \left( {\operatorname{Im}f = \operatorname{Im}{f}^{2}}\right) .
\]

Cette équivalence reste-t-elle vraie en dimension infinie ?

> Does this equivalence remain true in infinite dimension?

Solution. Condition nécessaire. On a \( f\left( E\right) \subset E \) donc \( {f}^{2}\left( E\right) = f\left\lbrack {f\left( E\right) }\right\rbrack \subset f\left( E\right) \) , c’est-à-dire \( \operatorname{Im}{f}^{2} \subset \operatorname{Im}f \) . Montrons maintenant \( \operatorname{Im}f \subset \operatorname{Im}{f}^{2} \) . Soit \( y = f\left( x\right) \in \operatorname{Im}f \) . Il existe \( \left( {{x}_{1},{x}_{2}}\right) \in \) Im \( f \times \operatorname{Ker}f \) tel que \( x = {x}_{1} + {x}_{2} \) , donc \( y = f\left( x\right) = f\left( {x}_{1}\right) \in \operatorname{Im}{f}^{2} \) .

> Solution. Necessary condition. We have \( f\left( E\right) \subset E \) therefore \( {f}^{2}\left( E\right) = f\left\lbrack {f\left( E\right) }\right\rbrack \subset f\left( E\right) \) , that is to say \( \operatorname{Im}{f}^{2} \subset \operatorname{Im}f \) . Let us now show \( \operatorname{Im}f \subset \operatorname{Im}{f}^{2} \) . Let \( y = f\left( x\right) \in \operatorname{Im}f \) . There exists \( \left( {{x}_{1},{x}_{2}}\right) \in \) Im \( f \times \operatorname{Ker}f \) such that \( x = {x}_{1} + {x}_{2} \) , therefore \( y = f\left( x\right) = f\left( {x}_{1}\right) \in \operatorname{Im}{f}^{2} \) .

Condition suffisante. Soit \( x \in E \) . On a \( f\left( x\right) \in \operatorname{Im}f = \operatorname{Im}{f}^{2} \) donc il existe \( {x}^{\prime } \in E \) tel que \( f\left( x\right) = {f}^{2}\left( {x}^{\prime }\right) \) . Donc \( f\left\lbrack {x - f\left( {x}^{\prime }\right) }\right\rbrack = 0 \) , d’où \( y = x - f\left( {x}^{\prime }\right) \in \operatorname{Ker}f \) . Si \( z = f\left( {x}^{\prime }\right) \in \operatorname{Im}f \) , on a donc \( x = y + z \) avec \( y \in \operatorname{Ker}f \) et \( z \in \operatorname{Im}f \) . Autrement dit, on vient de montrer \( E = \operatorname{Im}f + \operatorname{Ker}f \) . Comme de plus \( \dim \left( {\operatorname{Im}f}\right) + \dim \left( {\operatorname{Ker}f}\right) = \dim E \) , on en déduit \( E = \operatorname{Im}f \oplus \operatorname{Ker}f \) (voir le corollaire 1 page 118).

> Sufficient condition. Let \( x \in E \) . We have \( f\left( x\right) \in \operatorname{Im}f = \operatorname{Im}{f}^{2} \) so there exists \( {x}^{\prime } \in E \) such that \( f\left( x\right) = {f}^{2}\left( {x}^{\prime }\right) \) . Thus \( f\left\lbrack {x - f\left( {x}^{\prime }\right) }\right\rbrack = 0 \) , hence \( y = x - f\left( {x}^{\prime }\right) \in \operatorname{Ker}f \) . If \( z = f\left( {x}^{\prime }\right) \in \operatorname{Im}f \) , we then have \( x = y + z \) with \( y \in \operatorname{Ker}f \) and \( z \in \operatorname{Im}f \) . In other words, we have just shown \( E = \operatorname{Im}f + \operatorname{Ker}f \) . Since, furthermore, \( \dim \left( {\operatorname{Im}f}\right) + \dim \left( {\operatorname{Ker}f}\right) = \dim E \) , we deduce \( E = \operatorname{Im}f \oplus \operatorname{Ker}f \) (see corollary 1 on page 118).

En dimension infinie, ce résultat est faux. Par exemple, si \( f \in \mathcal{L}\left( {\mathbb{R}\left\lbrack X\right\rbrack }\right) \) est définie par \( f\left( P\right) = {P}^{\prime } \) , on a \( \operatorname{Im}{f}^{2} = \mathbb{R}\left\lbrack X\right\rbrack = \operatorname{Im}f \) et pourtant \( \operatorname{Im}f \) et \( \operatorname{Ker}f \) ne sont pas en somme directe (Im \( f = \mathbb{R}\left\lbrack X\right\rbrack \) et \( \operatorname{Ker}f \neq \{ 0\} \) ).

> In infinite dimension, this result is false. For example, if \( f \in \mathcal{L}\left( {\mathbb{R}\left\lbrack X\right\rbrack }\right) \) is defined by \( f\left( P\right) = {P}^{\prime } \) , we have \( \operatorname{Im}{f}^{2} = \mathbb{R}\left\lbrack X\right\rbrack = \operatorname{Im}f \) and yet \( \operatorname{Im}f \) and \( \operatorname{Ker}f \) are not in direct sum (Im \( f = \mathbb{R}\left\lbrack X\right\rbrack \) and \( \operatorname{Ker}f \neq \{ 0\} \) ).

EXERCICE 4. Soit \( E \) un \( \mathbb{K} \) -e.v (de dimension quelconque), \( F \) et \( G \) deux s.e.v de \( E \) tels que (i) \( G \subset F \) et (ii) \( F \) et \( G \) sont de même codimension finie dans \( E \) . Montrer que \( F = G \) .

> EXERCISE 4. Let \( E \) be a \( \mathbb{K} \) -v.s. (of arbitrary dimension), \( F \) and \( G \) two s.v.s. of \( E \) such that (i) \( G \subset F \) and (ii) \( F \) and \( G \) have the same finite codimension in \( E \) . Show that \( F = G \) .

Solution. Pour tout \( x \in E \) , on note \( \bar{x} \) sa classe dans \( E/G,\dot{x} \) sa classe dans \( E/F \) . Si \( \bar{x} = \bar{y} \) , alors \( \dot{x} = \dot{y} \) (car \( \overline{x - y} = \overline{0} \) donc \( x - y \in G \) donc \( x - y \in F \) , c’est-à-dire \( \left. {\dot{x} = \dot{y}}\right) \) .

> Solution. For any \( x \in E \) , we denote by \( \bar{x} \) its class in \( E/G,\dot{x} \) its class in \( E/F \) . If \( \bar{x} = \bar{y} \) , then \( \dot{x} = \dot{y} \) (because \( \overline{x - y} = \overline{0} \) so \( x - y \in G \) so \( x - y \in F \) , that is to say \( \left. {\dot{x} = \dot{y}}\right) \) .

Considérons l’application \( f : E/G \rightarrow E/F\;\bar{x} \mapsto \dot{x} \) . Elle est linéaire et surjective donc bijective car \( E/G \) et \( E/F \) sont des \( \mathbb{K} \) -e.v de même dimension finie (voir le corollaire 2). L’application \( f \) est donc injective, de sorte que si \( x \in F,\dot{x} = \dot{0} \) alors \( \bar{x} = \overline{0}, i \) . e. \( x \in G \) . En d’autres termes, \( F \subset G \) . Comme \( G \subset F \) par hypothèse, on a \( F = G \) .

> Consider the map \( f : E/G \rightarrow E/F\;\bar{x} \mapsto \dot{x} \) . It is linear and surjective, therefore bijective because \( E/G \) and \( E/F \) are \( \mathbb{K} \) -v.s. of the same finite dimension (see corollary 2). The map \( f \) is therefore injective, so that if \( x \in F,\dot{x} = \dot{0} \) then \( \bar{x} = \overline{0}, i \) . i.e. \( x \in G \) . In other words, \( F \subset G \) . As \( G \subset F \) by hypothesis, we have \( F = G \) .

EXERCICE 5 (SUITES EXACTES). a) Soient \( {E}_{0},{E}_{1},\ldots ,{E}_{n} \) des \( \mathbb{K} \) -e.v de dimension finie; on note \( {\alpha }_{k} = \dim {E}_{k} \) . On suppose qu’il existe \( n \) applications linéaires \( {f}_{0},{f}_{1},\ldots ,{f}_{n - 1} \) telles que pour tout \( k,{f}_{k} \in \mathcal{L}\left( {{E}_{k},{E}_{k + 1}}\right) \) , et vérifiant

> EXERCISE 5 (EXACT SEQUENCES). a) Let \( {E}_{0},{E}_{1},\ldots ,{E}_{n} \) be finite-dimensional \( \mathbb{K} \) -v.s.; denote \( {\alpha }_{k} = \dim {E}_{k} \) . Assume there exist \( n \) linear maps \( {f}_{0},{f}_{1},\ldots ,{f}_{n - 1} \) such that for all \( k,{f}_{k} \in \mathcal{L}\left( {{E}_{k},{E}_{k + 1}}\right) \) , and satisfying

(i) \( {f}_{0} \) est injective,

> (i) \( {f}_{0} \) is injective,

(ii) \( \forall k,1 \leq k \leq n - 1 \) , \( \operatorname{Im}{f}_{k - 1} = \operatorname{Ker}{f}_{k} \) ,

> (ii) \( \forall k,1 \leq k \leq n - 1 \) , \( \operatorname{Im}{f}_{k - 1} = \operatorname{Ker}{f}_{k} \) ,

(iii) \( {f}_{n - 1} \) est surjective.

> (iii) \( {f}_{n - 1} \) is surjective.

(On dit que \( \left( {{f}_{0},\ldots ,{f}_{n - 1}}\right) \) constitue une suite exacte.) Montrer que \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{\alpha }_{k} = 0 \) . b) (Application). Soit \( E \) un \( \mathbb{K} \) -e.v, \( F \) et \( G \) deux s.e.v de \( E \) de codimension finie dans \( E \) . Montrer que \( F + G \) et \( F \cap G \) sont de codimension finie dans \( E \) et que

> (We say that \( \left( {{f}_{0},\ldots ,{f}_{n - 1}}\right) \) forms an exact sequence.) Show that \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{\alpha }_{k} = 0 \) . b) (Application). Let \( E \) be a \( \mathbb{K} \) -v.s., \( F \) and \( G \) two subspaces of \( E \) of finite codimension in \( E \) . Show that \( F + G \) and \( F \cap G \) are of finite codimension in \( E \) and that

\[
{\operatorname{codim}}_{E}\left( {F + G}\right)  = {\operatorname{codim}}_{E}F + {\operatorname{codim}}_{E}G - {\operatorname{codim}}_{E}\left( {F \cap  G}\right) .
\]

Solution. a) L’assertion (ii) entraîne \( \dim \left( {\operatorname{Ker}{f}_{k}}\right) = \operatorname{rg}{f}_{k - 1} \) pour \( 1 \leq k \leq n - 1 \) , donc

> Solution. a) Assertion (ii) implies \( \dim \left( {\operatorname{Ker}{f}_{k}}\right) = \operatorname{rg}{f}_{k - 1} \) for \( 1 \leq k \leq n - 1 \) , therefore

\[
\forall k,1 \leq  k \leq  n - 1,\;{\alpha }_{k} = \dim \left( {\operatorname{Ker}{f}_{k}}\right)  + \operatorname{rg}{f}_{k} = \operatorname{rg}{f}_{k - 1} + \operatorname{rg}{f}_{k}.
\]

Or \( {\alpha }_{0} = \operatorname{rg}{f}_{0} \) car \( {f}_{0} \) est injective, et \( {\alpha }_{n} = \operatorname{rg}{f}_{n - 1} \) car \( {f}_{n - 1} \) est surjective. On en déduit

> However, \( {\alpha }_{0} = \operatorname{rg}{f}_{0} \) because \( {f}_{0} \) is injective, and \( {\alpha }_{n} = \operatorname{rg}{f}_{n - 1} \) because \( {f}_{n - 1} \) is surjective. We deduce

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{\alpha }_{k} = \left( {\operatorname{rg}{f}_{0}}\right)  - \left( {\operatorname{rg}{f}_{0} + \operatorname{rg}{f}_{1}}\right)  + \cdots  + {\left( -1\right) }^{n - 1}\left( {\operatorname{rg}{f}_{n - 2} + \operatorname{rg}{f}_{n - 1}}\right)  + {\left( -1\right) }^{n}\operatorname{rg}{f}_{n - 1} = 0.
\]

b) Pour tout \( x \in E \) , on note \( \dot{x} \) sa classe dans \( E/\left( {F \cap G}\right) ,\bar{x} \) dans \( E/F,\widehat{x} \) dans \( E/G \) et \( \widetilde{x} \) dans \( E/\left( {F + G}\right) \) . Définissons

> b) For all \( x \in E \) , denote \( \dot{x} \) its class in \( E/\left( {F \cap G}\right) ,\bar{x} \) in \( E/F,\widehat{x} \) in \( E/G \) and \( \widetilde{x} \) in \( E/\left( {F + G}\right) \) . Let us define

\[
f : E/\left( {F \cap  G}\right)  \rightarrow  E/F \times  E/G\;\dot{x} \mapsto  \left( {\bar{x},\widehat{x}}\right)
\]

et

\[
g : E/F \times  E/G \rightarrow  E/\left( {F + G}\right) \;\left( {\bar{x},\widehat{y}}\right)  \mapsto  \left( \overset{\text{ ⏜ }}{x - y}\right) .
\]

Nous allons montrer que \( \left( {f, g}\right) \) constitue une suite exacte.

> We will show that \( \left( {f, g}\right) \) forms an exact sequence.

- \( f \) est bien une application, car si \( \dot{x} = \dot{y} \) , alors \( x - y \in  F \cap  G \) donc \( \bar{x} = \bar{y} \) (car \( x - y \in  F \) ) et \( \widehat{x} = \widehat{y} \) (car \( x - y \in  G \) ).

> - \( f \) is indeed a map, because if \( \dot{x} = \dot{y} \) , then \( x - y \in  F \cap  G \) so \( \bar{x} = \bar{y} \) (since \( x - y \in  F \) ) and \( \widehat{x} = \widehat{y} \) (since \( x - y \in  G \) ).

- \( g \) est aussi une application, car si \( \left( {\bar{x},\widehat{y}}\right)  = \left( {\overline{{x}^{\prime }},\widehat{{y}^{\prime }}}\right) \) , on a \( x - {x}^{\prime } \in  F \) et \( y - {y}^{\prime } \in  G \) , donc \( \left( {x - {x}^{\prime }}\right)  - \left( {y - {y}^{\prime }}\right)  = \left( {x - y}\right)  - \left( {{x}^{\prime } - {y}^{\prime }}\right)  \in  F + G \) , c’est-à-dire \( \overset{\text{ ⏜ }}{x - y} = \overset{\text{ ⏜ }}{{x}^{\prime } - {y}^{\prime }} \) .

> - \( g \) is also a map, because if \( \left( {\bar{x},\widehat{y}}\right)  = \left( {\overline{{x}^{\prime }},\widehat{{y}^{\prime }}}\right) \) , we have \( x - {x}^{\prime } \in  F \) and \( y - {y}^{\prime } \in  G \) , so \( \left( {x - {x}^{\prime }}\right)  - \left( {y - {y}^{\prime }}\right)  = \left( {x - y}\right)  - \left( {{x}^{\prime } - {y}^{\prime }}\right)  \in  F + G \) , that is to say \( \overset{\text{ ⏜ }}{x - y} = \overset{\text{ ⏜ }}{{x}^{\prime } - {y}^{\prime }} \) .

- Il est clair que \( f \) et \( g \) sont linéaires.

> - It is clear that \( f \) and \( g \) are linear.

- \( f \) est injective, car si \( \left( {\bar{x},\widehat{x}}\right)  = \left( {\overline{0},\widehat{0}}\right) , x \in  F \) et \( x \in  G \) donc \( x \in  F \cap  G \) , c’est-à-dire \( \dot{x} = \dot{0} \) . Comme \( E/F \times  E/G \) est de dimension finie (car \( E/F \) et \( E/G \) le sont), l’injectivité de \( f \) permet d’affirmer que \( F \cap  G \) est de codimension finie (en effet, si \( E/\left( {F \cap  G}\right) \) était de dimension infinie, on pourrait trouver dans \( E/\left( {F \cap  G}\right) \) une famille libre contenant plus d’éléments que la dimension de \( E/F \times  E/G \) , absurde car l’image de cette famille libre par \( f \) injective est aussi une famille libre).

> - \( f \) is injective, because if \( \left( {\bar{x},\widehat{x}}\right)  = \left( {\overline{0},\widehat{0}}\right) , x \in  F \) and \( x \in  G \) then \( x \in  F \cap  G \) , that is to say \( \dot{x} = \dot{0} \) . As \( E/F \times  E/G \) is of finite dimension (because \( E/F \) and \( E/G \) are), the injectivity of \( f \) allows us to state that \( F \cap  G \) is of finite codimension (indeed, if \( E/\left( {F \cap  G}\right) \) were of infinite dimension, we could find in \( E/\left( {F \cap  G}\right) \) a free family containing more elements than the dimension of \( E/F \times  E/G \) , which is absurd because the image of this free family by the injective \( f \) is also a free family).

- \( g \) est surjective car si \( \widetilde{z} \in  E/\left( {F + G}\right) ,\widetilde{z} = g\left( {\bar{z},\widehat{0}}\right) \) . Donc \( E/F \times  E/G \) étant de dimension finie, \( E/\left( {F + G}\right)  = g\left( {E/F \times  E/G}\right) \) est de dimension finie.

> - \( g \) is surjective because if \( \widetilde{z} \in  E/\left( {F + G}\right) ,\widetilde{z} = g\left( {\bar{z},\widehat{0}}\right) \) . Thus, \( E/F \times  E/G \) being of finite dimension, \( E/\left( {F + G}\right)  = g\left( {E/F \times  E/G}\right) \) is of finite dimension.

- \( \operatorname{Im}f = \operatorname{Ker}g \) . En effet, on a déjà \( \operatorname{Im}f \subset  \operatorname{Ker}g \) car \( g\left( {f\left( \dot{x}\right) }\right)  = g\left( {\bar{x},\widehat{x}}\right)  = \overline{x - x} = \widetilde{0} \) . On a également \( \operatorname{Ker}g \subset  \operatorname{Im}f \) car si \( \left( {\bar{x},\widehat{y}}\right)  \in  \operatorname{Ker}g, x - y \in  F + G \) donc il existe \( {x}_{1} \in  F \) et \( {y}_{1} \in  G \) tels que \( x - y = {x}_{1} - {y}_{1} \) . Donc \( x - {x}_{1} = y - {y}_{1} = u \) , d’où \( \bar{x} = \bar{u} \) et \( \widehat{y} = \widehat{u} \) , donc \( \left( {\bar{x},\widehat{y}}\right)  = f\left( \dot{u}\right)  \in  \operatorname{Im}f. \)

> - \( \operatorname{Im}f = \operatorname{Ker}g \) . Indeed, we already have \( \operatorname{Im}f \subset  \operatorname{Ker}g \) because \( g\left( {f\left( \dot{x}\right) }\right)  = g\left( {\bar{x},\widehat{x}}\right)  = \overline{x - x} = \widetilde{0} \) . We also have \( \operatorname{Ker}g \subset  \operatorname{Im}f \) because if \( \left( {\bar{x},\widehat{y}}\right)  \in  \operatorname{Ker}g, x - y \in  F + G \) then there exist \( {x}_{1} \in  F \) and \( {y}_{1} \in  G \) such that \( x - y = {x}_{1} - {y}_{1} \) . Thus \( x - {x}_{1} = y - {y}_{1} = u \) , hence \( \bar{x} = \bar{u} \) and \( \widehat{y} = \widehat{u} \) , therefore \( \left( {\bar{x},\widehat{y}}\right)  = f\left( \dot{u}\right)  \in  \operatorname{Im}f. \)

On est donc dans les conditions d'application de a), ce qui nous donne

> We are therefore in the conditions to apply a), which gives us

\[
\dim \left( {E/\left( {F \cap  G}\right) }\right)  - \dim \left( {E/F \times  E/G}\right)  + \dim \left( {E/\left( {F + G}\right) }\right)  = 0,
\]

d’où le résultat car \( \dim \left( {E/F \times E/G}\right) = \dim \left( {E/F}\right) + \dim \left( {E/G}\right) \) .

> hence the result because \( \dim \left( {E/F \times E/G}\right) = \dim \left( {E/F}\right) + \dim \left( {E/G}\right) \) .

EXERCICE 6 (CENTRE DU GROUPE LINÉAIRE). Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie. Quel est le centre du groupe linéaire \( \mathcal{G}\ell \left( E\right) \) (i. e. l’ensemble des \( f \in \mathcal{G}\ell \left( E\right) \) tels que \( \forall g \in \mathcal{G}\ell \left( E\right) \) , \( {fg} = {gf}) \) ?

> EXERCISE 6 (CENTER OF THE GENERAL LINEAR GROUP). Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space. What is the center of the general linear group \( \mathcal{G}\ell \left( E\right) \) (i.e., the set of \( f \in \mathcal{G}\ell \left( E\right) \) such that \( \forall g \in \mathcal{G}\ell \left( E\right) \) , \( {fg} = {gf}) \) ?

Solution. Nous allons montrer le résultat suivant. Si \( f \in \mathcal{L}\left( E\right) \) commute avec tous les éléments de \( \mathcal{G}\ell \left( E\right) \) , alors \( f \) est une homothétie. En particulier, le centre de \( \mathcal{G}\ell \left( E\right) \) est \( \left\{ {\lambda {\operatorname{Id}}_{E} \mid \lambda \in {\mathbb{K}}^{ * }}\right\} \) .

> Solution. We will show the following result. If \( f \in \mathcal{L}\left( E\right) \) commutes with all elements of \( \mathcal{G}\ell \left( E\right) \), then \( f \) is a homothety. In particular, the center of \( \mathcal{G}\ell \left( E\right) \) is \( \left\{ {\lambda {\operatorname{Id}}_{E} \mid \lambda \in {\mathbb{K}}^{ * }}\right\} \).

Soit \( f \in \mathcal{L}\left( E\right) \) tel que \( \forall g \in \mathcal{G}\ell \left( E\right) ,{gf} = {fg} \) . Supposons que \( f \) ne soit pas une homothétie. D’après la proposition 3 page 121, il existe \( u \in E, u \neq 0 \) , tel que la famille \( \left( {u, f\left( u\right) }\right) \) forme une famille libre. Complétons là en une base \( \left( {u, f\left( u\right) ,{e}_{3},\ldots ,{e}_{n}}\right) \) de \( E \) . Définissons \( g \in \mathcal{L}\left( E\right) \) sur cette base comme suit

> Let \( f \in \mathcal{L}\left( E\right) \) be such that \( \forall g \in \mathcal{G}\ell \left( E\right) ,{gf} = {fg} \). Suppose that \( f \) is not a homothety. According to proposition 3 on page 121, there exists \( u \in E, u \neq 0 \) such that the family \( \left( {u, f\left( u\right) }\right) \) forms a linearly independent family. Let us complete it into a basis \( \left( {u, f\left( u\right) ,{e}_{3},\ldots ,{e}_{n}}\right) \) of \( E \). Let us define \( g \in \mathcal{L}\left( E\right) \) on this basis as follows

\[
g\left( u\right)  = u,\;g\left( {f\left( u\right) }\right)  = u + f\left( u\right) ,\;\forall i \geq  3, g\left( {e}_{i}\right)  = {e}_{i}.
\]

On a \( g \in \mathcal{G}\ell \left( E\right) \) car \( g \) transforme une base de \( E \) en une base de \( E \) . Or \( g \circ f\left( u\right) = u + f\left( u\right) \) et \( f \circ g\left( u\right) = f\left( u\right) \) , donc \( f \circ g \neq g \circ f \) car \( u \neq 0 \) . Finalement, \( f \) est une homothétie.

> We have \( g \in \mathcal{G}\ell \left( E\right) \) because \( g \) transforms a basis of \( E \) into a basis of \( E \). However, \( g \circ f\left( u\right) = u + f\left( u\right) \) and \( f \circ g\left( u\right) = f\left( u\right) \), so \( f \circ g \neq g \circ f \) because \( u \neq 0 \). Finally, \( f \) is a homothety.

EXERCICE 7. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \) . Soit \( f \in \mathcal{L}\left( E\right) \) . On suppose qu’il existe \( {x}_{0} \in E \) tel que \( B = \left( {f\left( {x}_{0}\right) ,{f}^{2}\left( {x}_{0}\right) ,\ldots ,{f}^{n}\left( {x}_{0}\right) }\right) \) forme une base de \( E \) .

> EXERCISE 7. Let \( E \) be a finite-dimensional \( \mathbb{K} \)-vector space \( n \). Let \( f \in \mathcal{L}\left( E\right) \). Suppose there exists \( {x}_{0} \in E \) such that \( B = \left( {f\left( {x}_{0}\right) ,{f}^{2}\left( {x}_{0}\right) ,\ldots ,{f}^{n}\left( {x}_{0}\right) }\right) \) forms a basis of \( E \).

a) Montrer que \( f \) est bijective.

> a) Show that \( f \) is bijective.

b) Montrer qu’il existe \( \left( {{a}_{0},\ldots ,{a}_{n - 1}}\right) \in {\mathbb{K}}^{n} \) tel que \( {f}^{n} + {a}_{n - 1}{f}^{n - 1} + \cdots + {a}_{1}f + {a}_{0}{\operatorname{Id}}_{E} = 0 \) (sans utiliser, bien sûr, le théorème de Cayley-Hamilton).

> b) Show that there exists \( \left( {{a}_{0},\ldots ,{a}_{n - 1}}\right) \in {\mathbb{K}}^{n} \) such that \( {f}^{n} + {a}_{n - 1}{f}^{n - 1} + \cdots + {a}_{1}f + {a}_{0}{\operatorname{Id}}_{E} = 0 \) (without using, of course, the Cayley-Hamilton theorem).

Solution. a) Soit \( y \in E \) . Comme \( \left( {f\left( {x}_{0}\right) ,\ldots ,{f}^{n}\left( {x}_{0}\right) }\right) \) est une base de \( E \) , il existe \( {\left( {\lambda }_{i}\right) }_{1 < i < n} \in {\mathbb{K}}^{n} \) tels que \( y = {\lambda }_{1}f\left( {x}_{0}\right) + \cdots + {\lambda }_{n}{f}^{n}\left( {x}_{0}\right) \) , donc \( y = f\left\lbrack {{\lambda }_{1}{x}_{0} + {\lambda }_{2}f\left( {x}_{0}\right) + \cdots + {\lambda }_{n}{f}^{n - 1}\left( {x}_{0}\right) }\right\rbrack \in \operatorname{Im}\bar{f} \) , et ceci pour tout \( y \in E \) . L’application \( f \) est donc surjective, donc bijective car c’est un endomorphisme en dimension finie.

> Solution. a) Let \( y \in E \) . Since \( \left( {f\left( {x}_{0}\right) ,\ldots ,{f}^{n}\left( {x}_{0}\right) }\right) \) is a basis of \( E \) , there exist \( {\left( {\lambda }_{i}\right) }_{1 < i < n} \in {\mathbb{K}}^{n} \) such that \( y = {\lambda }_{1}f\left( {x}_{0}\right) + \cdots + {\lambda }_{n}{f}^{n}\left( {x}_{0}\right) \) , thus \( y = f\left\lbrack {{\lambda }_{1}{x}_{0} + {\lambda }_{2}f\left( {x}_{0}\right) + \cdots + {\lambda }_{n}{f}^{n - 1}\left( {x}_{0}\right) }\right\rbrack \in \operatorname{Im}\bar{f} \) , and this for any \( y \in E \) . The map \( f \) is therefore surjective, and thus bijective as it is an endomorphism in finite dimension.

b) Comme \( B \) forme une base de \( E \) , il existe \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{K} \) tels que \( {f}^{n + 1}\left( {x}_{0}\right) = {\lambda }_{n}{f}^{n}\left( {x}_{0}\right) + \cdots + \; {\lambda }_{1}f\left( {x}_{0}\right) \) . Posons \( g = {f}^{n + 1} - {\lambda }_{n}{f}^{n} - \cdots - {\lambda }_{1}f \) . On a \( g\left( {x}_{0}\right) = 0 \) . Or

> b) Since \( B \) forms a basis of \( E \) , there exist \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{K} \) such that \( {f}^{n + 1}\left( {x}_{0}\right) = {\lambda }_{n}{f}^{n}\left( {x}_{0}\right) + \cdots + \; {\lambda }_{1}f\left( {x}_{0}\right) \) . Let \( g = {f}^{n + 1} - {\lambda }_{n}{f}^{n} - \cdots - {\lambda }_{1}f \) . We have \( g\left( {x}_{0}\right) = 0 \) . However

\[
\forall i,1 \leq  i \leq  n,\;g\left\lbrack  {{f}^{i}\left( {x}_{0}\right) }\right\rbrack   = {f}^{n + i + 1}\left( {x}_{0}\right)  - {\lambda }_{n}{f}^{n + i}\left( {x}_{0}\right)  - \cdots  - {\lambda }_{1}{f}^{i + 1}\left( {x}_{0}\right)  = {f}^{i}\left\lbrack  {g\left( {x}_{0}\right) }\right\rbrack   = 0,
\]

autrement dit \( g \) s’annule sur la base \( B \) , donc \( g = 0 \) . En composant \( g \) à gauche par \( {f}^{-1} \) , on obtient \( {f}^{n} - {\lambda }_{n}{f}^{n - 1} - \cdots - {\lambda }_{1}{\mathrm{{Id}}}_{E} = 0. \)

> in other words \( g \) vanishes on the basis \( B \) , so \( g = 0 \) . By composing \( g \) on the left by \( {f}^{-1} \) , we obtain \( {f}^{n} - {\lambda }_{n}{f}^{n - 1} - \cdots - {\lambda }_{1}{\mathrm{{Id}}}_{E} = 0. \)
