#### 2.2. Roots of a polynomial

*Français : 2.2. Racines d'un polynôme*

DéFINITION 1. Soit \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) et \( \mathbb{L} \) une extension de \( \mathbb{K} \) . On dit que \( a \in \mathbb{L} \) est une racine (ou un zéro) de \( F \) si \( F\left( a\right) = 0 \) .

> DEFINITION 1. Let \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) and \( \mathbb{L} \) be an extension of \( \mathbb{K} \). We say that \( a \in \mathbb{L} \) is a root (or a zero) of \( F \) if \( F\left( a\right) = 0 \).

Proposition 1. Soit \( a \in \mathbb{K} \) et \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) . L’élément a est une racine de \( F \) si et seulement si \( X - a \) divise \( F \) .

> Proposition 1. Let \( a \in \mathbb{K} \) and \( F \in \mathbb{K}\left\lbrack X\right\rbrack \). The element a is a root of \( F \) if and only if \( X - a \) divides \( F \).

DÉFINITION 2. Soit \( F \in \mathbb{K}\left\lbrack X\right\rbrack , a \in \mathbb{K} \) et \( h \in {\mathbb{N}}^{ * } \) . On dit que \( a \) est une racine d’ordre \( h \) de \( F \) si \( {\left( X - a\right) }^{h} \mid F \) et \( {\left( X - a\right) }^{h + 1} \nmid F \) .

> DEFINITION 2. Let \( F \in \mathbb{K}\left\lbrack X\right\rbrack , a \in \mathbb{K} \) and \( h \in {\mathbb{N}}^{ * } \). We say that \( a \) is a root of order \( h \) of \( F \) if \( {\left( X - a\right) }^{h} \mid F \) and \( {\left( X - a\right) }^{h + 1} \nmid F \).

\( \rightarrow \) Proposition 2. Soit \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) et \( {a}_{1},\ldots ,{a}_{r} \in \mathbb{K} \) des racines de \( {Fd} \) ’ordre \( {h}_{1},\ldots ,{h}_{r} \) (les \( {a}_{i} \) étant deux à deux distincts). Alors il existe \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que

> \( \rightarrow \) Proposition 2. Let \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) and \( {a}_{1},\ldots ,{a}_{r} \in \mathbb{K} \) be roots of \( {Fd} \) of order \( {h}_{1},\ldots ,{h}_{r} \) (the \( {a}_{i} \) being pairwise distinct). Then there exists \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) such that

\[
F\left( X\right)  = {\left( X - {a}_{1}\right) }^{{h}_{1}}\cdots {\left( X - {a}_{r}\right) }^{{h}_{r}}Q\left( X\right) \;\text{ et }\;\forall i, Q\left( {a}_{i}\right)  \neq  0.
\]

Conséquence. Si \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) est de degré \( n \geq 1 \) , alors \( F \) a au plus \( n \) racines (comptées avec leur ordre de multiplicité).

> Consequence. If \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) is of degree \( n \geq 1 \), then \( F \) has at most \( n \) roots (counted with their multiplicity).

Remarque 2. Attention ! La proposition précédente est fausse lorsque l'on remplace le corps \( \mathbb{K} \) par un anneau. Par exemple, dans \( \mathbb{Z}/8\mathbb{Z} \) , le polynôme \( F = \dot{4}X \in \mathbb{Z}/8\mathbb{Z}\left\lbrack X\right\rbrack \) a 3 racines \( \dot{0},\dot{2} \) et \( \dot{4} \) , mais \( \deg \left( F\right) = 1 \) .

> Remark 2. Warning! The previous proposition is false when replacing the field \( \mathbb{K} \) with a ring. For example, in \( \mathbb{Z}/8\mathbb{Z} \), the polynomial \( F = \dot{4}X \in \mathbb{Z}/8\mathbb{Z}\left\lbrack X\right\rbrack \) has 3 roots \( \dot{0},\dot{2} \) and \( \dot{4} \), but \( \deg \left( F\right) = 1 \).

Proposition 3. Soit \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que pour tout \( x \in \mathbb{K}, F\left( x\right) = 0.{Si}\mathbb{K} \) est infini, on a \( F = 0. \)

> Proposition 3. Let \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) be such that for all \( x \in \mathbb{K}, F\left( x\right) = 0.{Si}\mathbb{K} \) is infinite, we have \( F = 0. \)

Remarque 3. Si \( \mathbb{K} \) est fini, le résultat précédent est faux. Par exemple, si on note \( {a}_{1},\ldots ,{a}_{n} \) les éléments de \( \mathbb{K} \) , le polynôme \( F = \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) est non nul et pourtant tous les éléments \( x \) de \( \mathbb{K} \) vérifient \( P\left( x\right) = 0 \) . Il ne faut donc pas confondre polynôme et fonction polynôme. Par contre, si K est infini, la proposition précédente nous dit qu'il y a bijection entre \( \mathbb{K}\left\lbrack X\right\rbrack \) et les fonctions polynômes de \( \mathbb{K} \) dans \( \mathbb{K} \) .

> Remark 3. If \( \mathbb{K} \) is finite, the previous result is false. For example, if we denote \( {a}_{1},\ldots ,{a}_{n} \) as the elements of \( \mathbb{K} \), the polynomial \( F = \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) is non-zero and yet all elements \( x \) of \( \mathbb{K} \) satisfy \( P\left( x\right) = 0 \). One must therefore not confuse a polynomial with a polynomial function. However, if K is infinite, the previous proposition tells us that there is a bijection between \( \mathbb{K}\left\lbrack X\right\rbrack \) and the polynomial functions from \( \mathbb{K} \) to \( \mathbb{K} \).

Définition 3. Un polynôme \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) est dit scindé (ou dissocié) sur \( \mathbb{K} \) si on peut écrire

> Definition 3. A polynomial \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) is said to be split (or factored) over \( \mathbb{K} \) if it can be written

\[
F = \lambda {\left( X - {a}_{1}\right) }^{{h}_{1}}\cdots {\left( X - {a}_{r}\right) }^{{h}_{r}}
\]

avec \( \lambda \in \mathbb{K} \) et pour tout \( i,{a}_{i} \in \mathbb{K} \) et \( {h}_{i} \in {\mathbb{N}}^{ * } \) .

> with \( \lambda \in \mathbb{K} \) and for all \( i,{a}_{i} \in \mathbb{K} \) and \( {h}_{i} \in {\mathbb{N}}^{ * } \) .

Remarque 4. Deux polynômes \( F \) et \( G \) de \( \mathbb{K}\left\lbrack X\right\rbrack \) scindés sur \( \mathbb{K} \) sont premiers entre eux si et seulement s'ils n'ont aucune racine commune.

> Remark 4. Two polynomials \( F \) and \( G \) of \( \mathbb{K}\left\lbrack X\right\rbrack \) split over \( \mathbb{K} \) are coprime if and only if they have no common root.

THÉORÉME 1 (RELATIONS ENTRE COEFFICIENTS ET RACINES). Soit un polynôme

> THEOREM 1 (RELATIONS BETWEEN COEFFICIENTS AND ROOTS). Let a polynomial

\[
P = {a}_{0}{X}^{n} + {a}_{1}{X}^{n - 1} + \cdots  + {a}_{n - 1}X + {a}_{n} \in  \mathbb{K}\left\lbrack  X\right\rbrack  ,\;{a}_{0} \neq  0,
\]

scindé sur \( \mathbb{K} \) , dont les racines (comptées avec leur ordre de multiplicité) sont \( {x}_{1},\ldots ,{x}_{n} \) (de sorte que \( P = {a}_{0}\left( {X - {x}_{1}}\right) \cdots \left( {X - {x}_{n}}\right) \) ). Alors

> split over \( \mathbb{K} \) , whose roots (counted with their multiplicity) are \( {x}_{1},\ldots ,{x}_{n} \) (such that \( P = {a}_{0}\left( {X - {x}_{1}}\right) \cdots \left( {X - {x}_{n}}\right) \) ). Then

\[
\forall p \in  \{ 1,\ldots , n\} ,\;{\sigma }_{p} = \mathop{\sum }\limits_{{1 \leq  {i}_{1} < \cdots  < {i}_{p} \leq  n}}{x}_{{i}_{1}}\cdots {x}_{{i}_{p}} = {\left( -1\right) }^{p}\frac{{a}_{p}}{{a}_{0}}.
\]

En particulier

> In particular

\[
{\sigma }_{1} = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} =  - \frac{{a}_{1}}{{a}_{0}},\;{\sigma }_{2} = \mathop{\sum }\limits_{{1 \leq  i < j \leq  n}}{x}_{i}{x}_{j} = \frac{{a}_{2}}{{a}_{0}},\;{\sigma }_{n} = \mathop{\prod }\limits_{{i = 1}}^{n}{x}_{i} = {\left( -1\right) }^{n}\frac{{a}_{n}}{{a}_{0}}.
\]
