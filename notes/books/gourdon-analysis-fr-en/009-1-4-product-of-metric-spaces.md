#### 1.4. Product of metric spaces

*Français : 1.4. Produit d'espaces métriques*

On se donne un nombre fini \( n \) d’espaces métriques \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) et on pose \( E = {E}_{1} \times \cdots \times {E}_{n} \) . On veut faire de \( E \) un espace métrique. Un moyen naturel est de construire une distance d sur \( E \) à partir des distances \( {\mathrm{d}}_{i} \) . Par exemple si \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) et \( y = \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in E,\mathrm{\;d}\left( {x, y}\right) = \mathop{\max }\limits_{{1 \leq i \leq n}}{\mathrm{\;d}}_{i}\left( {{x}_{i},{y}_{i}}\right) \) définit une distance sur \( E \) . Cette distance est appelée distance produit sur \( E \) . Sauf mention contraire, c'est cette distance que nous utiliserons sur un produit d'espaces métriques.

> Let there be a finite number \( n \) of metric spaces \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) and let \( E = {E}_{1} \times \cdots \times {E}_{n} \) . We want to make \( E \) a metric space. A natural way is to construct a distance d on \( E \) from the distances \( {\mathrm{d}}_{i} \) . For example, if \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) and \( y = \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in E,\mathrm{\;d}\left( {x, y}\right) = \mathop{\max }\limits_{{1 \leq i \leq n}}{\mathrm{\;d}}_{i}\left( {{x}_{i},{y}_{i}}\right) \) defines a distance on \( E \) . This distance is called the product distance on \( E \) . Unless otherwise stated, this is the distance we will use on a product of metric spaces.

Remarque 15. - En posant

> Remark 15. - By setting

\[
{\mathrm{d}}^{\prime }\left( {x, y}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\mathrm{\;d}}_{i}\left( {{x}_{i},{y}_{i}}\right) \;\text{ et }\;{\mathrm{d}}^{\prime \prime }\left( {x, y}\right)  = \sqrt{\mathop{\sum }\limits_{{i = 1}}^{n}{\mathrm{\;d}}_{i}{\left( {x}_{i},{y}_{i}\right) }^{2}},
\]

on a également affaire à des distances sur \( E \) . Ces distances sont équivalentes à la distance produit d, car

> we are also dealing with distances on \( E \) . These distances are equivalent to the product distance d, because

\[
\forall x, y \in  E,\;\mathrm{\;d}\left( {x, y}\right)  \leq  {\mathrm{d}}^{\prime \prime }\left( {x, y}\right)  \leq  {\mathrm{d}}^{\prime }\left( {x, y}\right)  \leq  n\mathrm{\;d}\left( {x, y}\right) .
\]

Il est donc indifférent de travailler avec l'une ou l'autre de ces distances. C'est parce que la distance produit est plus souple d'utilisation que nous l'avons choisie.

> It is therefore indifferent to work with one or the other of these distances. It is because the product distance is more flexible to use that we have chosen it.

- Au sens de la distance produit d, la boule ouverte de centre \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) de rayon \( r > 0 \) vérifie

> - In the sense of the product distance d, the open ball with center \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) and radius \( r > 0 \) satisfies

\[
\mathrm{B}\left( {a, r}\right)  = \mathrm{B}\left( {{a}_{1}, r}\right)  \times  \cdots  \times  \mathrm{B}\left( {{a}_{n}, r}\right) .
\]

Proposition 11. Si \( {O}_{1},\ldots ,{O}_{n} \) sont des ouverts de \( {E}_{1},\ldots ,{E}_{n} \) , le produit \( {O}_{1} \times \cdots \times {O}_{n} \) est un ouvert de \( E \) appelé ouvert élémentaire.

> Proposition 11. If \( {O}_{1},\ldots ,{O}_{n} \) are open sets of \( {E}_{1},\ldots ,{E}_{n} \) , the product \( {O}_{1} \times \cdots \times {O}_{n} \) is an open set of \( E \) called an elementary open set.

Un ouvert de \( E \) n’est en général pas un ouvert élémentaire.

> An open set of \( E \) is generally not an elementary open set.

Proposition 12. La projection d'indice i, définie par

> Proposition 12. The projection of index i, defined by

\[
\mathop{\Pr }\limits_{i} : E = {E}_{1} \times  \cdots  \times  {E}_{n} \rightarrow  {E}_{i}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  {x}_{i}
\]

est une application continue et ouverte (une application est dite ouverte si l'image de tout ouvert par cette application est un ouvert).

> is a continuous and open map (a map is said to be open if the image of any open set under this map is an open set).

Proposition 13. Une application

> Proposition 13. A map

\[
f : \left( {F,\delta }\right)  \rightarrow  {E}_{1} \times  \cdots  \times  {E}_{n}\;x \mapsto  f\left( x\right)  = \left( {{f}_{1}\left( x\right) ,\cdots ,{f}_{n}\left( x\right) }\right) .
\]

est continue en \( a \in F \) si et seulement si pour tout \( i,{f}_{i} = \mathop{\Pr }\limits_{i} \circ f \) est continue en a.

> is continuous at \( a \in F \) if and only if for all \( i,{f}_{i} = \mathop{\Pr }\limits_{i} \circ f \) is continuous at a.

Proposition 14. Soit une application \( f : E = {E}_{1} \times \cdots \times {E}_{n} \rightarrow F \) et \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in E \) . Pour tout i, on note

> Proposition 14. Let a map \( f : E = {E}_{1} \times \cdots \times {E}_{n} \rightarrow F \) and \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in E \) . For all i, we denote

\[
{f}_{i} : {E}_{i} \rightarrow  F\;x \mapsto  f\left( {{a}_{1},\ldots ,{a}_{i - 1}, x,{a}_{i + 1},\ldots ,{a}_{n}}\right)
\]

( \( {f}_{i} \) est appelée application partielle d’indice \( i \) au point a). Si \( f \) est continue en a, alors pour tout \( i \) , l’application partielle \( {f}_{i} \) est continue en \( {a}_{i} \) .

> ( \( {f}_{i} \) is called the partial map of index \( i \) at point a). If \( f \) is continuous at a, then for all \( i \) , the partial map \( {f}_{i} \) is continuous at \( {a}_{i} \) .

Remarque 16. Attention ! La réciproque de ce dernier résultat est fausse. En d'autres termes, il se peut que tous les \( {f}_{i} \) soient continues en \( {a}_{i} \) sans que \( f \) soit continue en \( a \) . Par exemple, considérons l’application \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) définie par

> Remark 16. Warning! The converse of this last result is false. In other words, it is possible that all \( {f}_{i} \) are continuous at \( {a}_{i} \) without \( f \) being continuous at \( a \) . For example, consider the map \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) defined by

\[
f\left( {0,0}\right)  = 0\;\text{ et }\;\forall \left( {x, y}\right)  \neq  \left( {0,0}\right) , f\left( {x, y}\right)  = \frac{xy}{{x}^{2} + {y}^{2}}.
\]

Les applications partielles en \( \left( {0,0}\right) \) sont nulles, donc continues, et pourtant \( f \) n’est pas continue en \( \left( {0,0}\right) \) (sinon, l’application \( \varphi : x \mapsto f\left( {x, x}\right) \) serait continue - composée d’applications continues - ce qui est faux puisque \( \varphi \left( 0\right) = 0 \) et \( \varphi \left( x\right) = 1/2 \) dès que \( x \neq 0) \) .

> The partial maps at \( \left( {0,0}\right) \) are zero, hence continuous, yet \( f \) is not continuous at \( \left( {0,0}\right) \) (otherwise, the map \( \varphi : x \mapsto f\left( {x, x}\right) \) would be continuous - as a composition of continuous maps - which is false since \( \varphi \left( 0\right) = 0 \) and \( \varphi \left( x\right) = 1/2 \) as soon as \( x \neq 0) \) .

##### Continuity of the distance.

*Français : Continuité de la distance.*

Proposition 15. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Alors l’application distance \( \mathrm{d} : E \times \; E \rightarrow \mathbb{R} \) est lipschitzienne de rapport 2, en particulier continue.

> Proposition 15. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. Then the distance map \( \mathrm{d} : E \times \; E \rightarrow \mathbb{R} \) is 2-Lipschitz, and in particular continuous.

Conséquence : Soit \( a \in E \) et \( r > 0 \) . L’application \( \varphi : \;E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {a, x}\right) \) est continue d’après les deux dernières propositions. On en déduit que \( {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) = {\varphi }^{-1}\left( \left\lbrack {0, r}\right\rbrack \right) \) et \( \mathrm{S}\left( {a, r}\right) = {\varphi }^{-1}\left( {\{ r\} }\right) \) (sphère de centre \( a \) de rayon \( r \) ), images réciproques de fermés par une application continue, sont des fermés de \( E \) . On retrouve de même qu’une boule ouverte est un ouvert.

> Consequence: Let \( a \in E \) and \( r > 0 \) . The map \( \varphi : \;E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {a, x}\right) \) is continuous according to the last two propositions. We deduce that \( {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) = {\varphi }^{-1}\left( \left\lbrack {0, r}\right\rbrack \right) \) and \( \mathrm{S}\left( {a, r}\right) = {\varphi }^{-1}\left( {\{ r\} }\right) \) (sphere centered at \( a \) with radius \( r \) ), as inverse images of closed sets by a continuous map, are closed sets in \( E \) . We similarly recover that an open ball is an open set.

Continuité des opérations dans un e.v.n.

> Continuity of operations in a n.v.s.

Proposition 16. Soit \( E \) un e.v.n sur \( \mathbb{K} \) (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ). Les applications

> Proposition 16. Let \( E \) be a n.v.s. over \( \mathbb{K} \) (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) ). The maps

\[
E \times  E \rightarrow  E\;\left( {x, y}\right)  \mapsto  x + y\;\text{ et }\;\mathbb{K} \times  E \rightarrow  E\;\left( {\lambda , x}\right)  \mapsto  \lambda  \cdot  x
\]

sont continues.

> are continuous.

Algèbre normée.

> Normed algebra.

DéFINITION 20. On dit qu’une norme \( \parallel \cdot \parallel \) sur une \( \mathbb{K} \) -algèbre \( A \) (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ) est une norme d’algèbre si \( \parallel {xy}\parallel \leq \parallel x\parallel \cdot \parallel y\parallel \) pour tout \( \left( {x, y}\right) \in {A}^{2} \) . Munie d’une telle norme, \( A \) est appelée algèbre normée. L’application \( A \times A \rightarrow A\;\left( {x, y}\right) \mapsto {xy} \) est alors continue.

> DEFINITION 20. A norm \( \parallel \cdot \parallel \) on a \( \mathbb{K} \) -algebra \( A \) (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) ) is called an algebra norm if \( \parallel {xy}\parallel \leq \parallel x\parallel \cdot \parallel y\parallel \) for all \( \left( {x, y}\right) \in {A}^{2} \) . Equipped with such a norm, \( A \) is called a normed algebra. The map \( A \times A \rightarrow A\;\left( {x, y}\right) \mapsto {xy} \) is then continuous.

Proposition 17. Soit A un \( \mathbb{K} \) -e.v.n \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) et \( f, g : \left( {E,\mathrm{\;d}}\right) \rightarrow A \) deux applications continues en \( a \in E \) . Alors les applications \( f + g,{\lambda f} \) (pour tout \( \lambda \in \mathbb{K} \) fixé) sont continues en a. Si A est une algèbre normée, l’application fg est continue en a.

> Proposition 17. Let A be a \( \mathbb{K} \) -n.v.s. \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) and \( f, g : \left( {E,\mathrm{\;d}}\right) \rightarrow A \) be two maps continuous at \( a \in E \) . Then the maps \( f + g,{\lambda f} \) (for any fixed \( \lambda \in \mathbb{K} \) ) are continuous at a. If A is a normed algebra, the map fg is continuous at a.
