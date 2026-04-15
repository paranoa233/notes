#### 5.3. Finite-dimensional normed vector spaces

*Français : 5.3. Espaces vectoriels normés de dimension finie*

Comme nous allons le voir, en dimension finie, "tout est continu". Les notions de la sous-partie précédente présentent donc moins d'intérêt en dimension finie.

> As we shall see, in finite dimension, "everything is continuous". The concepts from the previous subsection are therefore of less interest in finite dimension.

\( \rightarrow \) THÉORÉME 3. Dans un e.v.n de dimension finie, toutes les normes sont équivalentes.

> \( \rightarrow \) THEOREM 3. In a finite-dimensional n.v.s., all norms are equivalent.

Démonstration. Soit \( E \) un \( \mathbb{K} \) -e.v \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) de dimension finie, \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . Pour tout \( x = \mathop{\sum }\limits_{i}{x}_{i}{e}_{i},{N}_{0}\left( x\right) = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) définit une norme sur \( E \) .

> Proof. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s. \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) , \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) a basis of \( E \) . For any \( x = \mathop{\sum }\limits_{i}{x}_{i}{e}_{i},{N}_{0}\left( x\right) = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) defines a norm on \( E \) .

Montrons que toutes les normes sur \( E \) sont équivalentes à \( {N}_{0} \) . Soit \( N \) une norme sur \( E \) . En désignant par \( a \) le réel \( \mathop{\sum }\limits_{i}N\left( {e}_{i}\right) \) , on a pour tout \( x = \mathop{\sum }\limits_{i}{x}_{i}{e}_{i} \in E \)

> Let us show that all norms on \( E \) are equivalent to \( {N}_{0} \) . Let \( N \) be a norm on \( E \) . By denoting by \( a \) the real number \( \mathop{\sum }\limits_{i}N\left( {e}_{i}\right) \) , we have for all \( x = \mathop{\sum }\limits_{i}{x}_{i}{e}_{i} \in E \)

\[
N\left( x\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}N\left( {{x}_{i}{e}_{i}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right| N\left( {e}_{i}\right)  \leq  a{N}_{0}\left( x\right) .
\]

(*)

> Munissons \( {\mathbb{K}}^{n} \) de la norme produit \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) . L’application \( \varphi : \left( {{\mathbb{K}}^{n},\parallel .{\parallel }_{\infty }}\right) \rightarrow \; \left( {E,{N}_{0}}\right) \;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{i}{x}_{i}{e}_{i} \) est une isométrie, donc \( S = \left\{ {x \in E \mid {N}_{0}\left( x\right) = 1}\right\} \) est un compact de \( \left( {E,{N}_{0}}\right) \) (image de la sphère unité de \( {\mathbb{K}}^{n} \) - qui est compacte car fermée bornée dans \( {\mathbb{K}}^{n} \) - par \( \varphi \) qui est continue car isométrique). D’après (*), on a \( \left| {N\left( x\right) - N\left( y\right) }\right| \leq N\left( {x - y}\right) \leq \) a \( {N}_{0}\left( {x - y}\right) \) , donc \( N : \left( {E,{N}_{0}}\right) \rightarrow \mathbb{R} \) est continue. Comme \( S \) est un compact de \( \left( {E,{N}_{0}}\right) \) , on en déduit \( b = \mathop{\inf }\limits_{{{N}_{0}\left( x\right) = 1}}N\left( x\right) \neq 0 \) . Ainsi,

Let us equip \( {\mathbb{K}}^{n} \) with the product norm \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \). The map \( \varphi : \left( {{\mathbb{K}}^{n},\parallel .{\parallel }_{\infty }}\right) \rightarrow \; \left( {E,{N}_{0}}\right) \;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{i}{x}_{i}{e}_{i} \) is an isometry, so \( S = \left\{ {x \in E \mid {N}_{0}\left( x\right) = 1}\right\} \) is a compact subset of \( \left( {E,{N}_{0}}\right) \) (the image of the unit sphere of \( {\mathbb{K}}^{n} \) - which is compact because it is closed and bounded in \( {\mathbb{K}}^{n} \) - under \( \varphi \), which is continuous because it is an isometry). According to (*), we have \( \left| {N\left( x\right) - N\left( y\right) }\right| \leq N\left( {x - y}\right) \leq \) a \( {N}_{0}\left( {x - y}\right) \), so \( N : \left( {E,{N}_{0}}\right) \rightarrow \mathbb{R} \) is continuous. Since \( S \) is a compact subset of \( \left( {E,{N}_{0}}\right) \), we deduce \( b = \mathop{\inf }\limits_{{{N}_{0}\left( x\right) = 1}}N\left( x\right) \neq 0 \). Thus,

\[
\forall x \in  E, x \neq  0,\;N\left( x\right)  = {N}_{0}\left( x\right)  \cdot  N\left( \frac{x}{{N}_{0}\left( x\right) }\right)  \geq  b{N}_{0}\left( x\right) .
\]

Avec (*), on en déduit le théorème.

> With (*), we deduce the theorem.

Ce théorème est important. Il permet de choisir la norme que l'on veut sur un e.v.n de dimension finie. Voici des corollaires.

> This theorem is important. It allows us to choose any norm we want on a finite-dimensional n.v.s. Here are some corollaries.

COROLLAIRE 1. Toute application linéaire d'un e.v.n de dimension finie dans un e.v.n (quelconque) est continue.

> COROLLARY 1. Any linear map from a finite-dimensional n.v.s. to an (arbitrary) n.v.s. is continuous.

COROLLAIRE 2. Tout e.v.n de dimension finie est complet.

> COROLLARY 2. Every finite-dimensional n.v.s. is complete.

COROLLAIRE 3. Tout s.e.v de dimension finie d'un e.v.n est fermé.

> COROLLARY 3. Every finite-dimensional subspace of an n.v.s. is closed.

COROLLAIRE 4. Les parties compactes d'un e.v.n de dimension finie sont les parties fermées bornées.

> COROLLARY 4. The compact subsets of a finite-dimensional n.v.s. are the closed and bounded subsets.

Remarque 5. Tous ces corollaires sont faux en dimension infinie. Par exemple :

> Remark 5. All these corollaries are false in infinite dimension. For example:

- Munissons l’espace vectoriel des polynômes réels \( \mathbb{R}\left\lbrack  X\right\rbrack \) de la norme \( \begin{Vmatrix}{\mathop{\sum }\limits_{i}{a}_{i}{X}^{i}}\end{Vmatrix} = \; \mathop{\sup }\limits_{i}\left| {a}_{i}\right| \) . L’application linéaire \( f : \mathbb{R}\left\lbrack  X\right\rbrack   \rightarrow  \mathbb{R}\left\lbrack  X\right\rbrack  \;P \mapsto  {P}^{\prime } \) n’est pas continue (en effet, \( f\left( {X}^{n}\right)  = n \) et \( \begin{Vmatrix}{X}^{n}\end{Vmatrix} = 1 \) donc l’assertion (iii) du théorème 1 n’est pas vérifiée).

> - Let us equip the vector space of real polynomials \( \mathbb{R}\left\lbrack  X\right\rbrack \) with the norm \( \begin{Vmatrix}{\mathop{\sum }\limits_{i}{a}_{i}{X}^{i}}\end{Vmatrix} = \; \mathop{\sup }\limits_{i}\left| {a}_{i}\right| \). The linear map \( f : \mathbb{R}\left\lbrack  X\right\rbrack   \rightarrow  \mathbb{R}\left\lbrack  X\right\rbrack  \;P \mapsto  {P}^{\prime } \) is not continuous (indeed, \( f\left( {X}^{n}\right)  = n \) and \( \begin{Vmatrix}{X}^{n}\end{Vmatrix} = 1 \), so assertion (iii) of theorem 1 is not satisfied).

— Tout e.v.n à base dénombrable n'est pas complet (voir l'exercice 8).

> — Not every n.v.s. with a countable basis is complete (see exercise 8).

- La boule unité fermée d'un e.v.n de dimension infinie n'est pas compacte (théorème de Riesz, voir l'exercice 9).

> - The closed unit ball of an infinite-dimensional n.v.s. is not compact (Riesz's theorem, see exercise 9).
