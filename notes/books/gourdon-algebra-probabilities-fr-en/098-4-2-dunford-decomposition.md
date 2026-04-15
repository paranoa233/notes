#### 4.2. Dunford decomposition

*Français : 4.2. Décomposition de Dunford*

Nous allons maintenant donner une nouvelle réduction plus poussée que la simple trigo-nalisation (mais moins que la réduction de Jordan), appelée décomposition de Dunford. Nous donnerons deux moyens d'y parvenir.

> We will now provide a new reduction that is more advanced than simple triangularization (but less so than Jordan reduction), called the Dunford decomposition. We will provide two ways to achieve it.

\( \rightarrow \) THÉORÉME 2 (DÉCOMPOSITION DE DUNFORD). Soit \( f \in \mathcal{L}\left( E\right) \) tel que le polynôme caractéristique \( {P}_{f} \) de \( f \) est scindé sur \( \mathbb{K} \) . Il existe un unique couple \( \left( {d, n}\right) \in {\left( \mathcal{L}\left( E\right) \right) }^{2} \) avec d diagonalisable et \( n \) nilpotente, tel que

> \( \rightarrow \) THEOREM 2 (DUNFORD DECOMPOSITION). Let \( f \in \mathcal{L}\left( E\right) \) be such that the characteristic polynomial \( {P}_{f} \) of \( f \) splits over \( \mathbb{K} \) . There exists a unique pair \( \left( {d, n}\right) \in {\left( \mathcal{L}\left( E\right) \right) }^{2} \) with d diagonalizable and \( n \) nilpotent, such that

\[
\text{ (i) }f = d + n\;\text{ (ii) }n \circ  d = d \circ  n\text{ . }
\]

Démonstration. On écrit \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) , et pour tout \( i \) , on note \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) less ous-espaces caractéristiques de \( f \) .

> Proof. We write \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) , and for all \( i \) , we denote \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) the characteristic subspaces of \( f \) .

Existence. Comme \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , il suffit de définir \( d \) et \( n \) sur chaque \( {N}_{i} \) . On les définit comme suit :

> Existence. Since \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , it suffices to define \( d \) and \( n \) on each \( {N}_{i} \) . We define them as follows:

\[
\forall i,\forall x \in  {N}_{i},\;d\left( x\right)  = {\lambda }_{i}x\;\text{ et }\;n\left( x\right)  = f\left( x\right)  - {\lambda }_{i}x.
\]

Autrement dit, pour tout \( i \) on a \( {d}_{i} = {d}_{\mid {N}_{i}} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) et \( {n}_{i} = {n}_{\mid {N}_{i}} = {f}_{\mid {N}_{i}} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) . Les \( {d}_{i} \) et \( {n}_{i} \) sont des endomorphismes de \( {N}_{i} \) car \( {N}_{i} \) est stable par \( f \) donc par \( d \) et \( n \) .

> In other words, for all \( i \) we have \( {d}_{i} = {d}_{\mid {N}_{i}} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) and \( {n}_{i} = {n}_{\mid {N}_{i}} = {f}_{\mid {N}_{i}} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) . The \( {d}_{i} \) and \( {n}_{i} \) are endomorphisms of \( {N}_{i} \) because \( {N}_{i} \) is stable by \( f \) and therefore by \( d \) and \( n \) .

Ainsi définie, \( d \) est diagonalisable. Pour tout \( i \) , on a \( {n}_{i}^{{\alpha }_{i}} = 0 \) (puisque par définition de \( {N}_{i} \) , pour tout \( x \in {N}_{i},{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( x\right) = 0) \) . Si \( \alpha = \mathop{\sup }\limits_{i}{\alpha }_{i},{n}^{\alpha } \) s’annule donc sur chaque \( {N}_{i} \) donc sur \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) , c’est-à-dire \( {n}^{\alpha } = 0 \) .

> Defined this way, \( d \) is diagonalizable. For any \( i \) , we have \( {n}_{i}^{{\alpha }_{i}} = 0 \) (since by definition of \( {N}_{i} \) , for any \( x \in {N}_{i},{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( x\right) = 0) \) . If \( \alpha = \mathop{\sup }\limits_{i}{\alpha }_{i},{n}^{\alpha } \) therefore vanishes on each \( {N}_{i} \) , it vanishes on \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) , that is to say \( {n}^{\alpha } = 0 \) .

Il reste à montrer que \( d \) et \( n \) commutent. Pour tout \( i \) , on a \( {d}_{i} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) donc \( {n}_{i} \circ {d}_{i} = {d}_{i} \circ {n}_{i} \) , c’est-à-dire que \( d \) et \( n \) commutent sur chaque \( {N}_{i} \) , donc sur \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) .

> It remains to show that \( d \) and \( n \) commute. For any \( i \) , we have \( {d}_{i} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) so \( {n}_{i} \circ {d}_{i} = {d}_{i} \circ {n}_{i} \) , which means that \( d \) and \( n \) commute on each \( {N}_{i} \) , and therefore on \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) .

Unicité. Soit \( \left( {{d}^{\prime },{n}^{\prime }}\right) \) un autre couple vérifiant les conditions. On remarque d’abord que \( f \circ {d}^{\prime } = \; {d}^{\prime } \circ f \) , donc pour tout \( i,{N}_{i} \) est stable par \( {d}^{\prime } \) (pour tout \( x \in {N}_{i},{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left\lbrack {{d}^{\prime }\left( x\right) }\right\rbrack = {d}^{\prime } \circ (f - \; {\left. {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( x\right) = 0) \) . Comme \( {d}_{\mid {N}_{i}} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) , on en déduit que \( d \circ {d}^{\prime } = {d}^{\prime } \circ d \) sur \( {N}_{i} \) . Ceci étant vrai pour tout \( i \) , comme \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) , on en déduit que \( d \) et \( {d}^{\prime } \) commutent. De plus \( d \) et \( {d}^{\prime } \) sont diagonalisables, on peut donc les diagonaliser dans une même base, ce qui prouve que \( {d}^{\prime } - d \) est diagonalisable.

> Uniqueness. Let \( \left( {{d}^{\prime },{n}^{\prime }}\right) \) be another pair satisfying the conditions. We first note that \( f \circ {d}^{\prime } = \; {d}^{\prime } \circ f \) , so for any \( i,{N}_{i} \) is stable by \( {d}^{\prime } \) (for any \( x \in {N}_{i},{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left\lbrack {{d}^{\prime }\left( x\right) }\right\rbrack = {d}^{\prime } \circ (f - \; {\left. {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( x\right) = 0) \) . As \( {d}_{\mid {N}_{i}} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) , we deduce that \( d \circ {d}^{\prime } = {d}^{\prime } \circ d \) on \( {N}_{i} \) . Since this is true for any \( i \) , as \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) , we deduce that \( d \) and \( {d}^{\prime } \) commute. Furthermore, \( d \) and \( {d}^{\prime } \) are diagonalizable, so we can diagonalize them in the same basis, which proves that \( {d}^{\prime } - d \) is diagonalizable.

Comme \( n = f - d,{n}^{\prime } = f - {d}^{\prime } \) et que \( d \circ {d}^{\prime } = {d}^{\prime } \circ d, n \) et \( {n}^{\prime } \) commutent. Si on choisit \( p \) et \( q \) tels que \( {n}^{p} = {n}^{\prime q} = 0 \) , on a donc

> Since \( n = f - d,{n}^{\prime } = f - {d}^{\prime } \) and \( d \circ {d}^{\prime } = {d}^{\prime } \circ d, n \) and \( {n}^{\prime } \) commute. If we choose \( p \) and \( q \) such that \( {n}^{p} = {n}^{\prime q} = 0 \) , we therefore have

\[
{\left( n - {n}^{\prime }\right) }^{p + q} = \mathop{\sum }\limits_{{i + j = p + q}}\left( \begin{matrix} p + q \\  i \end{matrix}\right) {n}^{i}{\left( -1\right) }^{j}{n}^{\prime j} = 0
\]

(dans chaque terme de la somme, on a soit \( i \geq p \) , soit \( j \geq q \) ). Donc \( n - {n}^{\prime } = {d}^{\prime } - d \) est nilpotent. Or nous avions montré que \( {d}^{\prime } - d \) est diagonalisable, donc \( {d}^{\prime } - d = 0 \) . Autrement dit, \( d = {d}^{\prime } \) et donc \( n = {n}^{\prime } \) .

> (in each term of the sum, we have either \( i \geq p \) or \( j \geq q \) ). Thus \( n - {n}^{\prime } = {d}^{\prime } - d \) is nilpotent. However, we had shown that \( {d}^{\prime } - d \) is diagonalizable, so \( {d}^{\prime } - d = 0 \) . In other words, \( d = {d}^{\prime } \) and therefore \( n = {n}^{\prime } \) .

Conséquence. Soit \( f \in \mathcal{L}\left( E\right) \) avec \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) scindé sur K. Reprenons les notations utilisées dans la démonstration. Pour tout \( i,{f}_{i} = {f}_{\mid {N}_{i}} \in \mathcal{L}\left( {N}_{i}\right) \) est trigonalisable et \( {\lambda }_{i} \) est sa seule valeur propre (car \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} = {n}_{i} \) est nilpotente) et donc il existe une base \( {B}_{i} \) de \( {N}_{i} \) dans laquelle la matrice de \( {f}_{i} \) a la forme

> Consequence. Let \( f \in \mathcal{L}\left( E\right) \) with \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) split over K. Let us resume the notation used in the proof. For any \( i,{f}_{i} = {f}_{\mid {N}_{i}} \in \mathcal{L}\left( {N}_{i}\right) \) is trigonalizable and \( {\lambda }_{i} \) is its only eigenvalue (since \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} = {n}_{i} \) is nilpotent) and therefore there exists a basis \( {B}_{i} \) of \( {N}_{i} \) in which the matrix of \( {f}_{i} \) has the form

\[
{\left\lbrack  {f}_{i}\right\rbrack  }_{{B}_{i}} = {A}_{i} = \left( \begin{matrix} {\lambda }_{i} & \left( \times \right) \\   \ddots  & \\  \left( 0\right) & {\lambda }_{i} \end{matrix}\right) .
\]

Comme \( E = { \oplus }_{i = 1}^{s}{N}_{i} \) , on voit que \( B = \left( {{B}_{1},\ldots ,{B}_{s}}\right) \) est une base de \( E \) dans laquelle la matrice de \( f \) a la forme

> As \( E = { \oplus }_{i = 1}^{s}{N}_{i} \), we see that \( B = \left( {{B}_{1},\ldots ,{B}_{s}}\right) \) is a basis of \( E \) in which the matrix of \( f \) has the form

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} {A}_{1} & \left( 0\right) \\  \ldots & \\  \left( 0\right) & {A}_{s} \end{matrix}\right) .
\]

Cette réduction est plus poussée que la simple trigonalisation que nous avions vue au théorème 3 page 174.

> This reduction is more advanced than the simple trigonalization we saw in theorem 3 on page 174.

Un autre moyen d'aboutir à la décomposition de Dunford. Nous présentons une autre technique pour aboutir à la décomposition de Dunford, qui présente l'avantage de montrer que les endomorphismes \( d \) et \( n \) sont des polynômes en \( f \) . Nous aurons besoin pour cela d'un résultat préliminaire qui fait l'objet de la proposition ci dessous.

> Another way to arrive at the Dunford decomposition. We present another technique to arrive at the Dunford decomposition, which has the advantage of showing that the endomorphisms \( d \) and \( n \) are polynomials in \( f \). For this, we will need a preliminary result which is the subject of the proposition below.

Proposition 1. Soit \( f \in \mathcal{L}\left( E\right) \) et \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) un polynôme annulateur de \( f \) . Soit \( F = \; \beta {M}_{1}^{{\alpha }_{1}}\cdots {M}_{s}^{{\alpha }_{s}} \) la décomposition en facteurs irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) du polynôme \( F \) . Pour tout \( i \) , on note \( {N}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \) . On a alors \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) et pour tout \( i \) , la projection sur \( {N}_{i} \) parallèlement à \( { \oplus }_{j \neq i}{N}_{j} \) est un polynôme en \( f \) .

> Proposition 1. Let \( f \in \mathcal{L}\left( E\right) \) and \( F \in \mathbb{K}\left\lbrack X\right\rbrack \) be an annihilating polynomial of \( f \). Let \( F = \; \beta {M}_{1}^{{\alpha }_{1}}\cdots {M}_{s}^{{\alpha }_{s}} \) be the decomposition into irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \) of the polynomial \( F \). For any \( i \), we denote \( {N}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \). We then have \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) and for any \( i \), the projection onto \( {N}_{i} \) parallel to \( { \oplus }_{j \neq i}{N}_{j} \) is a polynomial in \( f \).

Démonstration. La propriété \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) résulte du théorème de décomposition des noyaux.

> Proof. The property \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) results from the primary decomposition theorem.

Pour tout \( i \) , notons \( {Q}_{i} = \mathop{\prod }\limits_{{j \neq i}}{M}_{j}^{{\alpha }_{j}} \) . Aucun facteur n’est commun à tous les \( {Q}_{i} \) , c’est-à-dire que les \( {Q}_{i} \) sont premiers entre eux dans leur ensemble. En appliquant l’égalité de Bezout, on voit qu’il existe \( {U}_{1},\ldots ,{U}_{s} \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( {U}_{1}{Q}_{1} + \cdots + {U}_{s}{Q}_{s} = 1 \) , de sorte que

> For any \( i \), let us denote \( {Q}_{i} = \mathop{\prod }\limits_{{j \neq i}}{M}_{j}^{{\alpha }_{j}} \). No factor is common to all \( {Q}_{i} \), that is to say that the \( {Q}_{i} \) are coprime as a whole. By applying Bezout's identity, we see that there exist \( {U}_{1},\ldots ,{U}_{s} \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {U}_{1}{Q}_{1} + \cdots + {U}_{s}{Q}_{s} = 1 \), so that

\[
{\operatorname{Id}}_{E} = {U}_{1}\left( f\right)  \circ  {Q}_{1}\left( f\right)  + \cdots  + {U}_{s}\left( f\right)  \circ  {Q}_{s}\left( f\right) .
\]

Pour tout \( i \) , on note \( {P}_{i} = {U}_{i}{Q}_{i} \) et \( {p}_{i} = {P}_{i}\left( f\right) \) . On a Id \( = \mathop{\sum }\limits_{{i = 1}}^{s}{p}_{i}\;\left( *\right) \) . Par ailleurs, pour tout \( j \neq i, F \) divise \( {Q}_{i}{Q}_{j} \) donc

> For any \( i \), we denote \( {P}_{i} = {U}_{i}{Q}_{i} \) and \( {p}_{i} = {P}_{i}\left( f\right) \). We have Id \( = \mathop{\sum }\limits_{{i = 1}}^{s}{p}_{i}\;\left( *\right) \). Furthermore, for any \( j \neq i, F \) divides \( {Q}_{i}{Q}_{j} \) therefore

\[
\forall j \neq  i,\;{p}_{i} \circ  {p}_{j} = {Q}_{i}{Q}_{j}\left( f\right)  \circ  {U}_{i}{U}_{j}\left( f\right)  = 0.
\]

\( \left( {* * }\right) \)

> On déduit de \( \left( *\right) \) que pour tout \( i,{p}_{i} = \mathop{\sum }\limits_{{i = 1}}^{s}{p}_{i} \circ {p}_{j} \) et donc d’après \( \left( {* * }\right) ,{p}_{i} = {p}_{i}^{2} \) . Les \( {p}_{i} \) sont donc des projecteurs.

We deduce from \( \left( *\right) \) that for any \( i,{p}_{i} = \mathop{\sum }\limits_{{i = 1}}^{s}{p}_{i} \circ {p}_{j} \) and thus according to \( \left( {* * }\right) ,{p}_{i} = {p}_{i}^{2} \). The \( {p}_{i} \) are therefore projectors.

> - Montrons que pour tout \( i,\operatorname{Im}{p}_{i} = {N}_{i} \) .

- Let us show that for any \( i,\operatorname{Im}{p}_{i} = {N}_{i} \).

> Soit \( y = {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{i} \) . On a

Let \( y = {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{i} \). We have

\[
{M}_{i}^{{\alpha }_{i}}\left( f\right) \left( y\right)  = {M}_{i}^{{\alpha }_{i}}\left( f\right)  \circ  {P}_{i}\left( f\right) \left( x\right)  = {U}_{i}\left( f\right)  \circ  F\left( f\right) \left( x\right)  = 0,
\]

ce qui prouve que \( \operatorname{Im}{p}_{i} \subset \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) = {N}_{i} \) .

> which proves that \( \operatorname{Im}{p}_{i} \subset \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) = {N}_{i} \).

Il reste à montrer l’inclusion réciproque. Soit \( x \in {N}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \) . D’après \( \left( *\right) , x = \; {p}_{1}\left( x\right) + \cdots + {p}_{s}\left( x\right) \) . Or pour tout \( j \neq i,{p}_{j}\left( x\right) = {U}_{j}\left( f\right) \circ {Q}_{j}\left( f\right) \left( x\right) = 0 \) car \( {M}_{i}^{{\alpha }_{i}} \) divise \( {Q}_{j} \) , donc finalement \( x = {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{i} \) . Donc \( \operatorname{Im}{p}_{i} = {N}_{i} \) .

> It remains to show the reverse inclusion. Let \( x \in {N}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \). According to \( \left( *\right) , x = \; {p}_{1}\left( x\right) + \cdots + {p}_{s}\left( x\right) \). However, for any \( j \neq i,{p}_{j}\left( x\right) = {U}_{j}\left( f\right) \circ {Q}_{j}\left( f\right) \left( x\right) = 0 \) because \( {M}_{i}^{{\alpha }_{i}} \) divides \( {Q}_{j} \), so finally \( x = {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{i} \). Therefore \( \operatorname{Im}{p}_{i} = {N}_{i} \).

- Il ne reste plus qu’à montrer que pour tout \( i \) , \( \operatorname{Ker}{p}_{i} = { \oplus  }_{j \neq  i}{N}_{j} \) .

> - It only remains to show that for any \( i \), \( \operatorname{Ker}{p}_{i} = { \oplus  }_{j \neq  i}{N}_{j} \).

Pour tout \( j \neq i \) , on a \( {N}_{j} \subset \operatorname{Ker}{p}_{i} \) car si \( x \in {N}_{j} \) , alors \( {p}_{i}\left( x\right) = {U}_{i}\left( f\right) \circ {Q}_{i}\left( f\right) \left( x\right) = 0 \) car \( {M}_{j}^{{\alpha }_{j}} \) divise \( {Q}_{j} \) . On en déduit que \( { \oplus }_{j \neq i}{N}_{j} \subset \operatorname{Ker}{p}_{i} \) .

> For any \( j \neq i \), we have \( {N}_{j} \subset \operatorname{Ker}{p}_{i} \) because if \( x \in {N}_{j} \), then \( {p}_{i}\left( x\right) = {U}_{i}\left( f\right) \circ {Q}_{i}\left( f\right) \left( x\right) = 0 \) because \( {M}_{j}^{{\alpha }_{j}} \) divides \( {Q}_{j} \). We deduce that \( { \oplus }_{j \neq i}{N}_{j} \subset \operatorname{Ker}{p}_{i} \).

Soit maintenant \( x \in \operatorname{Ker}{p}_{i} \) . D’après \( \left( *\right) , x = \mathop{\sum }\limits_{{j \neq i}}{p}_{j}\left( x\right) \) donc \( x \in { \oplus }_{j \neq i}{N}_{j} \) . Finalement, \( \operatorname{Ker}{p}_{i} = { \oplus }_{j \neq i}{N}_{j}. \)

> Now let \( x \in \operatorname{Ker}{p}_{i} \). According to \( \left( *\right) , x = \mathop{\sum }\limits_{{j \neq i}}{p}_{j}\left( x\right) \) therefore \( x \in { \oplus }_{j \neq i}{N}_{j} \). Finally, \( \operatorname{Ker}{p}_{i} = { \oplus }_{j \neq i}{N}_{j}. \)

La démonstration est terminée puisque par construction, les projecteurs \( {p}_{i} \) sont des polynômes en \( f \) .

> The proof is complete since by construction, the projectors \( {p}_{i} \) are polynomials in \( f \).

\( \rightarrow \) THÉORÉME 3 (DÉCOMPOSITION DE DUNFORD, BIS). Soit un endomorphisme \( f \in \mathcal{L}\left( E\right) \) tel que son polynôme caractéristique \( {P}_{f} \) soit scindé sur \( \mathbb{K} \) . Il existe un unique couple \( \left( {d, n}\right) \) d'endomorphismes tel que

> \( \rightarrow \) THEOREM 3 (DUNFORD DECOMPOSITION, BIS). Let \( f \in \mathcal{L}\left( E\right) \) be an endomorphism such that its characteristic polynomial \( {P}_{f} \) splits over \( \mathbb{K} \) . There exists a unique pair \( \left( {d, n}\right) \) of endomorphisms such that

(i) d est diagonalisable, n est nilpotente.

> (i) d is diagonalizable, n is nilpotent.

(ii) \( f = d + n \) et \( d \circ n = n \circ d \) .

> (ii) \( f = d + n \) and \( d \circ n = n \circ d \) .

De plus, \( d \) et \( n \) sont des polynômes en \( f \) .

> Furthermore, \( d \) and \( n \) are polynomials in \( f \) .

Démonstration. Existence. Écrivons \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) et pour tout \( i \) , notons \( {N}_{i} = \; \operatorname{Ker}{\left( f - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) . La proposition précédente s’applique avec \( F = {P}_{f} \) et pour tout \( i,{M}_{i} = \left( {X - {\lambda }_{i}}\right) \) . En utilisant les notations précédentes, pour tout \( i,{p}_{i} = {P}_{i}\left( f\right) \) est le projecteur sur \( {N}_{i} \) parallèlement à \( { \oplus }_{j \neq i}{N}_{j} \) . Posons \( d = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}{p}_{i} \) (ainsi construit, \( d \) est diagonalisable) et \( n = f - d = \mathop{\sum }\limits_{{i = 1}}^{s}(f - \; {\lambda }_{i} \) Id \( ){p}_{i} \) . En utilisant le fait que les \( {p}_{i} \) sont des projecteurs, que \( {p}_{i} \circ {p}_{j} = 0 \) si \( i \neq j \) , et que les \( {p}_{i} \) commutent avec \( f \) (ce sont des polynômes en \( f \) ), on obtient facilement par récurrence sur \( q \)

> Proof. Existence. Let us write \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) and for every \( i \) , let us denote \( {N}_{i} = \; \operatorname{Ker}{\left( f - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) . The previous proposition applies with \( F = {P}_{f} \) and for every \( i,{M}_{i} = \left( {X - {\lambda }_{i}}\right) \) . Using the previous notations, for every \( i,{p}_{i} = {P}_{i}\left( f\right) \) is the projector onto \( {N}_{i} \) parallel to \( { \oplus }_{j \neq i}{N}_{j} \) . Let us set \( d = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}{p}_{i} \) (thus constructed, \( d \) is diagonalizable) and \( n = f - d = \mathop{\sum }\limits_{{i = 1}}^{s}(f - \; {\lambda }_{i} \) Id \( ){p}_{i} \) . Using the fact that the \( {p}_{i} \) are projectors, that \( {p}_{i} \circ {p}_{j} = 0 \) if \( i \neq j \) , and that the \( {p}_{i} \) commute with \( f \) (they are polynomials in \( f \) ), we easily obtain by induction on \( q \)

\[
\forall q \in  {\mathbb{N}}^{ * },\;{n}^{q} = \mathop{\sum }\limits_{{i = 1}}^{s}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{q}{p}_{i}.
\]

Or si \( q = \mathop{\sup }\limits_{i}{\alpha }_{i} \) , on a \( {\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{q}{p}_{i} = \left\lbrack {{\left( X - {\lambda }_{i}\right) }^{q}{P}_{i}}\right\rbrack \left( f\right) = 0 \) pour tout \( i \) car \( {P}_{f} \) divise \( {\left( X - {\lambda }_{i}\right) }^{q}{P}_{i} \) , donc \( {n}^{q} = 0 \) .

> Now if \( q = \mathop{\sup }\limits_{i}{\alpha }_{i} \) , we have \( {\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{q}{p}_{i} = \left\lbrack {{\left( X - {\lambda }_{i}\right) }^{q}{P}_{i}}\right\rbrack \left( f\right) = 0 \) for every \( i \) because \( {P}_{f} \) divides \( {\left( X - {\lambda }_{i}\right) }^{q}{P}_{i} \) , therefore \( {n}^{q} = 0 \) .

Ainsi construits, \( d \) et \( n \) sont des polynômes en \( f \) vérifiant (i) et (ii).

> Thus constructed, \( d \) and \( n \) are polynomials in \( f \) satisfying (i) and (ii).

Unicité. Soit \( \left( {{d}^{\prime },{n}^{\prime }}\right) \) un autre couple vérifiant (i) et (ii). Les endomorphismes \( {d}^{\prime } \) et \( {n}^{\prime } \) com-mutent avec \( {d}^{\prime } + {n}^{\prime } = f \) donc avec \( d \) et \( n \) qui sont des polynômes en \( f \) . Ainsi, \( d \) et \( {d}^{\prime } \) sont diagonalisables dans une même base, ce qui entraîne que \( d - {d}^{\prime } \) est diagonalisable. Comme \( d - {d}^{\prime } = {n}^{\prime } - n \) est nilpotente (on montre ceci comme dans la démonstration du théorème 2), on en déduit que \( d - {d}^{\prime } = {n}^{\prime } - n = 0 \) .

> Uniqueness. Let \( \left( {{d}^{\prime },{n}^{\prime }}\right) \) be another pair satisfying (i) and (ii). The endomorphisms \( {d}^{\prime } \) and \( {n}^{\prime } \) commute with \( {d}^{\prime } + {n}^{\prime } = f \) and therefore with \( d \) and \( n \), which are polynomials in \( f \). Thus, \( d \) and \( {d}^{\prime } \) are diagonalizable in the same basis, which implies that \( d - {d}^{\prime } \) is diagonalizable. Since \( d - {d}^{\prime } = {n}^{\prime } - n \) is nilpotent (shown as in the proof of Theorem 2), we deduce that \( d - {d}^{\prime } = {n}^{\prime } - n = 0 \).

Calcul pratique de la décomposition de Dunford. Nous allons donner un moyen pratique de calculer les endomorphismes \( d \) et \( n \) donnés par la décomposition de Dunford. Nous allons pour cela calculer les projecteurs \( {p}_{i} \) , et il suffira ensuite d’écrire que

> Practical calculation of the Dunford decomposition. We will provide a practical way to calculate the endomorphisms \( d \) and \( n \) given by the Dunford decomposition. To do this, we will calculate the projectors \( {p}_{i} \), and it will then suffice to write that

\[
d = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}{p}_{i}\;\text{ et }\;n = f - d.
\]

Commençons par remarquer que dans la démonstration du théorème précédent (partie existence), on aurait pu remplacer \( {P}_{f} \) par n’importe quel polynôme \( F \) annulant \( f \) et ayant les mêmes facteurs premiers que \( {P}_{f} \) , en particulier par le polynôme minimal \( {\Pi }_{f} \) de \( f \) . Si \( F = \mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}} \) est un tel polynôme, on commence par décomposer \( 1/F \) en éléments simples dans \( \mathbb{K}\left( X\right) \) :

> Let us begin by noting that in the proof of the previous theorem (existence part), we could have replaced \( {P}_{f} \) with any polynomial \( F \) annihilating \( f \) and having the same prime factors as \( {P}_{f} \), in particular with the minimal polynomial \( {\Pi }_{f} \) of \( f \). If \( F = \mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}} \) is such a polynomial, we start by decomposing \( 1/F \) into partial fractions in \( \mathbb{K}\left( X\right) \):

\[
\frac{1}{F} = \mathop{\sum }\limits_{{i = 1}}^{s}\left\lbrack  {\mathop{\sum }\limits_{{j = 1}}^{{r}_{i}}\frac{{x}_{i, j}}{{\left( X - {\lambda }_{i}\right) }^{j}}}\right\rbrack  .
\]

Pour tout \( i \) , on pose ensuite \( {U}_{i} = \mathop{\sum }\limits_{{j = 1}}^{{r}_{i}}{x}_{i, j}{\left( X - {\lambda }_{i}\right) }^{{r}_{i} - j} \) , de sorte que

> For all \( i \), we then set \( {U}_{i} = \mathop{\sum }\limits_{{j = 1}}^{{r}_{i}}{x}_{i, j}{\left( X - {\lambda }_{i}\right) }^{{r}_{i} - j} \), such that

\[
\frac{1}{F} = \mathop{\sum }\limits_{{i = 1}}^{s}\frac{{U}_{i}}{{\left( X - {\lambda }_{i}\right) }^{{r}_{i}}}\;\text{ ou encore }\;1 = \mathop{\sum }\limits_{{i = 1}}^{s}{U}_{i}{Q}_{i},
\]

où \( {Q}_{i} = \mathop{\prod }\limits_{{j \neq i}}{\left( X - {\lambda }_{j}\right) }^{{r}_{j}} \) . Les projecteurs \( {p}_{i} \) sont alors donnés par \( {p}_{i} = {P}_{i}\left( f\right) \) où \( {P}_{i} = {U}_{i}{Q}_{i} \) (voir la démonstration de la proposition 1).

> where \( {Q}_{i} = \mathop{\prod }\limits_{{j \neq i}}{\left( X - {\lambda }_{j}\right) }^{{r}_{j}} \). The projectors \( {p}_{i} \) are then given by \( {p}_{i} = {P}_{i}\left( f\right) \) where \( {P}_{i} = {U}_{i}{Q}_{i} \) (see the proof of Proposition 1).

Il est en général préférable de prendre pour le polynôme \( F \) le polynôme minimal \( {\Pi }_{f} \) de \( f \) (les degrés des polynômes intermédiaires sont moins élevés). Mais le calcul de \( {\Pi }_{f} \) peut être assez long, c’est pourquoi on choisit parfois de prendre \( F = {P}_{f} \) .

> It is generally preferable to use the minimal polynomial \( {\Pi }_{f} \) of \( f \) as the polynomial \( F \) (the degrees of the intermediate polynomials are lower). However, calculating \( {\Pi }_{f} \) can be quite long, which is why one sometimes chooses to take \( F = {P}_{f} \).

Application au calcul d'exponentielle. L'écriture \( f = d + n \) donnée par la décomposition de Dunford est intéressante car \( d \) et \( n \) commutant, on peut utiliser la formule du binôme pour calculer \( {f}^{p} \) :

> Application to exponential calculation. The expression \( f = d + n \) given by the Dunford decomposition is useful because \( d \) and \( n \) commute, allowing us to use the binomial formula to calculate \( {f}^{p} \):

\[
{f}^{p} = {\left( d + n\right) }^{p} = \mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} p \\  k \end{array}\right) {d}^{k} \circ  {n}^{p - k}.
\]

Dans l’expression ci dessus, on peut retirer les termes de la somme pour lesquels \( p - k \) est plus grand que l’indice de nilpotence de \( n \) .

> In the expression above, we can remove the terms of the sum for which \( p - k \) is greater than the index of nilpotence of \( n \).

Un autre intérêt est le calcul d’exponentielle. En effet, \( d \) et \( n \) commutant, on a \( \exp \left( f\right) = \; \exp \left( {d + n}\right) = \exp \left( d\right) \exp \left( n\right) \) . Le calcul de \( \exp \left( d\right) \) est simple si une base \( B \) de diagonalisation de \( d \) est connue :

> Another benefit is the calculation of the exponential. Indeed, since \( d \) and \( n \) commute, we have \( \exp \left( f\right) = \; \exp \left( {d + n}\right) = \exp \left( d\right) \exp \left( n\right) \). The calculation of \( \exp \left( d\right) \) is simple if a diagonalization basis \( B \) for \( d \) is known:

\[
\operatorname{si}{\left\lbrack  d\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1} & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & {\lambda }_{n} \end{matrix}\right) ,\;{\left\lbrack  \exp \left( d\right) \right\rbrack  }_{B} = \exp \left( {\left\lbrack  d\right\rbrack  }_{B}\right)  = \left( \begin{matrix} {e}^{{\lambda }_{1}} & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & {e}^{{\lambda }_{n}} \end{matrix}\right)
\]

Quant à \( \exp \left( n\right) \) , il suffit d’écrire \( \exp \left( n\right) = \mathop{\sum }\limits_{{p = 0}}^{{q - 1}}\frac{1}{p!}{n}^{p} \) où \( q \) est l’indice de nilpotence de \( n \) .

> As for \( \exp \left( n\right) \), it suffices to write \( \exp \left( n\right) = \mathop{\sum }\limits_{{p = 0}}^{{q - 1}}\frac{1}{p!}{n}^{p} \) where \( q \) is the index of nilpotence of \( n \).

Dans la pratique, on calcule \( d \) et \( n \) grâce à la méthode décrite plus haut. Avec les notations précédentes, rappelons que

> In practice, we calculate \( d \) and \( n \) using the method described above. With the previous notations, let us recall that

\[
d = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}{p}_{i}\;\text{ et }\;n = \mathop{\sum }\limits_{{i = 1}}^{s}\left( {f - {\lambda }_{i}\mathrm{{Id}}}\right) {p}_{i}.
\]

On peut alors calculer \( \exp \left( f\right) \) sans diagonaliser \( d \) ,à partir des projecteurs \( {p}_{i} \) . En effet, les relations sur les \( {p}_{i} \) entraînent que pour tout \( p,{d}^{p} = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}^{p}{p}_{i} \) donc

> We can then calculate \( \exp \left( f\right) \) without diagonalizing \( d \), using the projectors \( {p}_{i} \). Indeed, the relations on the \( {p}_{i} \) imply that for all \( p,{d}^{p} = \mathop{\sum }\limits_{{i = 1}}^{s}{\lambda }_{i}^{p}{p}_{i} \) therefore

\[
\exp \left( d\right)  = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{d}^{p}}{p!} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{s}\frac{{\lambda }_{i}^{p}}{p!}{p}_{i}}\right\rbrack   = \mathop{\sum }\limits_{{i = 1}}^{s}\left\lbrack  {\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{\lambda }_{i}^{p}}{p!}}\right\rbrack  {p}_{i} = \mathop{\sum }\limits_{{i = 1}}^{s}{e}^{{\lambda }_{i}}{p}_{i}.
\]

Par ailleurs,

> Furthermore,

\[
\exp \left( n\right)  = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{n}^{p}}{p!} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{s}\frac{{\left( f - {\lambda }_{i}\mathrm{{Id}}\right) }^{p}}{p!}{p}_{i}}\right\rbrack   = \mathop{\sum }\limits_{{i = 1}}^{s}\left\lbrack  {\mathop{\sum }\limits_{{p = 0}}^{{{r}_{i} - 1}}\frac{{\left( f - {\lambda }_{i}\mathrm{{Id}}\right) }^{p}}{p!}}\right\rbrack  {p}_{i}.
\]

Finalement, on en déduit

> Finally, we deduce

\[
\exp \left( f\right)  = \exp \left( d\right) \exp \left( n\right)  = \mathop{\sum }\limits_{{i = 1}}^{s}{e}^{{\lambda }_{i}}\left\lbrack  {\mathop{\sum }\limits_{{p = 0}}^{{{r}_{i} - 1}}\frac{{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{p}}{p!}}\right\rbrack  {p}_{i}.
\]

(Un calcul d'exponentielle de matrice est traité à l'exercice 1 page 209).

> (A matrix exponential calculation is covered in exercise 1 on page 209).
