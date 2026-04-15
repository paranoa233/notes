### 1. General results on Hilbert spaces

*Français : 1. Résultats généraux sur les espaces de Hilbert*

Problem 1. Nous n’étudierons ici que les espaces de Hilbert sur \( \mathbb{R} \) (les propriétés des espaces de Hilbert sur \( \mathbb{C} \) sont analogues et se montrent de la même manière).

> Problem 1. We will only study Hilbert spaces over \( \mathbb{R} \) here (the properties of Hilbert spaces over \( \mathbb{C} \) are analogous and are shown in the same way).

Rappel. Un espace vectoriel est dit préhilbertien s'il est muni d'un produit scalaire. S'il est complet pour la norme issue du produit scalaire, on dit que c'est un espace de Hilbert (ou hilbertien).

> Reminder. A vector space is called pre-Hilbert if it is equipped with an inner product. If it is complete with respect to the norm derived from the inner product, it is called a Hilbert space.

Les e.v de dimension finie sont très maniables, mais beaucoup de leurs propriétés intéressantes ne sont plus vraies en dimension infinie. Les propriétés topologiques des espaces de Hilbert en font des espaces de dimension infinie très souples, comme nous allons le voir.

> Finite-dimensional vector spaces are very manageable, but many of their interesting properties are no longer true in infinite dimensions. The topological properties of Hilbert spaces make them very flexible infinite-dimensional spaces, as we shall see.

- Dans tout le problème, \( H \) désigne un espace de Hilbert de dimension infinie.

> - Throughout the problem, \( H \) denotes an infinite-dimensional Hilbert space.

- Le produit scalaire de deux éléments \( x, y \in  H \) est noté \( \langle x, y\rangle \) , la norme associée est \( \parallel x\parallel  = \sqrt{\langle x, x\rangle }. \)

> - The inner product of two elements \( x, y \in  H \) is denoted by \( \langle x, y\rangle \), the associated norm is \( \parallel x\parallel  = \sqrt{\langle x, x\rangle }. \)

1/ Théorème de projection sur un convexe fermé. Soit \( C \subset H \) un convexe fermé. a) Soit \( x \in H \) . Montrer qu’il existe un unique élément \( y \in C \) tel que \( \parallel x - y\parallel = \mathrm{d}\left( {x, C}\right) = \; \mathop{\inf }\limits_{{z \in C}}\parallel x - z\parallel . \)

> 1/ Projection theorem onto a closed convex set. Let \( C \subset H \) be a closed convex set. a) Let \( x \in H \). Show that there exists a unique element \( y \in C \) such that \( \parallel x - y\parallel = \mathrm{d}\left( {x, C}\right) = \; \mathop{\inf }\limits_{{z \in C}}\parallel x - z\parallel . \)

L’élément \( y \) s’appelle la projection orthogonale de \( x \) sur \( C \) , et on note \( y = {x}_{C} \) . b) Si \( x \in H \) , montrer que \( {x}_{C} \) est caractérisé par la propriété suivante :

> The element \( y \) is called the orthogonal projection of \( x \) onto \( C \), and is denoted by \( y = {x}_{C} \). b) If \( x \in H \), show that \( {x}_{C} \) is characterized by the following property:

\[
\forall z \in  C,\;\left\langle  {z - {x}_{C}, x - {x}_{C}}\right\rangle   \leq  0.
\]

2/ Orthogonal d’un sous-espace. On rappelle que l’orthogonal d’une partie \( A \) de \( H \) est

> 2/ Orthogonal of a subspace. Recall that the orthogonal of a subset \( A \) of \( H \) is

\[
{A}^{ \bot  } = \{ y \in  H \mid  \forall x \in  A,\langle x, y\rangle  = 0\} .
\]

a) Si \( A \subset H \) , montrer que \( {A}^{ \bot } \) est un s.e.v fermé de \( H \) .

> a) If \( A \subset H \), show that \( {A}^{ \bot } \) is a closed subspace of \( H \).

b) Soit \( F \) un s.e.v fermé de \( H \) . Montrer :

> b) Let \( F \) be a closed subspace of \( H \). Show that:

(i) \( F \oplus {F}^{ \bot } = H \) ;

> (ii) si \( x \in H,{x}_{F} = {p}_{F}\left( x\right) \) où \( {p}_{F} \) est la projection orthogonale sur \( F \) ;

(ii) if \( x \in H,{x}_{F} = {p}_{F}\left( x\right) \) where \( {p}_{F} \) is the orthogonal projection onto \( F \);

> (iii) \( F = {F}^{ \bot \bot } \) .

(iii) \( F = {F}^{ \bot \bot } \).

> c) Soit \( F \) un s.e.v quelconque de \( H \) . Montrer que \( \bar{F} = {F}^{ \bot \bot } \) .

c) Let \( F \) be any subspace of \( H \). Show that \( \bar{F} = {F}^{ \bot \bot } \).

> d) Montrer qu’un s.e.v \( F \) de \( H \) est dense si et seulement si \( {F}^{ \bot } = \{ 0\} \) .

d) Show that a subspace \( F \) of \( H \) is dense if and only if \( {F}^{ \bot } = \{ 0\} \).

> 3/ Théorème de représentation de Riesz. On note \( {H}^{\prime } \) le dual topologique de \( H \) , i. e. l’e.v des formes linéaires de \( H \) continues. a) Pour tout \( a \in H \) , on note \( {\varphi }_{a} \) la forme linéaire \( H \rightarrow \mathbb{R}\;x \mapsto \langle a, x\rangle \) . Montrer que l’application \( H \rightarrow {H}^{\prime }\;a \mapsto {\varphi }_{a} \) est un isomorphisme.

3/ Riesz representation theorem. Let \( {H}^{\prime } \) denote the topological dual of \( H \), i.e., the vector space of continuous linear forms on \( H \). a) For any \( a \in H \), let \( {\varphi }_{a} \) denote the linear form \( H \rightarrow \mathbb{R}\;x \mapsto \langle a, x\rangle \). Show that the map \( H \rightarrow {H}^{\prime }\;a \mapsto {\varphi }_{a} \) is an isomorphism.

> b) (Application : adjoint d’un endomorphisme). Soit \( u \in {\mathcal{L}}_{c}\left( H\right) \) un endomorphisme continu de \( H \) . Montrer que

b) (Application: adjoint of an endomorphism). Let \( u \in {\mathcal{L}}_{c}\left( H\right) \) be a continuous endomorphism of \( H \). Show that

\[
\exists !v \in  {\mathcal{L}}_{c}\left( E\right) ,\forall \left( {x, y}\right)  \in  {H}^{2},\;\langle u\left( x\right) , y\rangle  = \langle x, v\left( y\right) \rangle .
\]

L’endomorphisme \( v \) est appelé adjoint de \( u \) et est noté \( {u}^{ * } \) . Montrer que \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} = \parallel u\parallel \) (où \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel ). \)

> The endomorphism \( v \) is called the adjoint of \( u \) and is denoted by \( {u}^{ * } \). Show that \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} = \parallel u\parallel \) (where \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel ). \)

4/ Bases hilbertiennes.

> 4/ Hilbert bases.

a) Soit \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) une suite de vecteurs de \( H \) de norme 1, deux à deux orthogonaux. On note \( E = \overline{\operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}}} \) . Soit \( v \in H \) . Pour tout \( n \in \mathbb{N} \) , on note \( {\lambda }_{n} = \left\langle {v,{e}_{n}}\right\rangle \) . Montrer que la série \( \sum {\lambda }_{n}{e}_{n} \) converge, que sa somme \( w \) est la projection orthogonale de \( v \) sur \( E \) et que

> a) Let \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of vectors in \( H \) of norm 1, pairwise orthogonal. Let \( E = \overline{\operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}}} \). Let \( v \in H \). For any \( n \in \mathbb{N} \), let \( {\lambda }_{n} = \left\langle {v,{e}_{n}}\right\rangle \). Show that the series \( \sum {\lambda }_{n}{e}_{n} \) converges, that its sum \( w \) is the orthogonal projection of \( v \) onto \( E \), and that

\[
\parallel w{\parallel }^{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\lambda }_{n}^{2} \leq  \parallel v{\parallel }^{2}\;\text{ (inégalité de Bessel). }
\]

b) On dit que \( H \) est séparable s’il existe une suite \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) de vecteurs de \( H \) de norme 1, deux à deux orthogonaux, telle que \( \operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) soit dense dans \( H \) (on parle alors de base hilbertienne).

> b) We say that \( H \) is separable if there exists a sequence \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) of vectors in \( H \) of norm 1, pairwise orthogonal, such that \( \operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) is dense in \( H \) (this is called a Hilbert basis).

Montrer que si \( H \) est séparable, tout élément \( v \) de \( H \) s’écrit \( v = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\lambda }_{n}{e}_{n} \) où pour tout \( n,{\lambda }_{n} = \left\langle {v,{e}_{n}}\right\rangle \) , et que \( \parallel v{\parallel }^{2} = \mathop{\sum }\limits_{{n = 0}}^{\infty }{\lambda }_{n}^{2} \) .

> Show that if \( H \) is separable, every element \( v \) of \( H \) can be written as \( v = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\lambda }_{n}{e}_{n} \) where for all \( n,{\lambda }_{n} = \left\langle {v,{e}_{n}}\right\rangle \), and that \( \parallel v{\parallel }^{2} = \mathop{\sum }\limits_{{n = 0}}^{\infty }{\lambda }_{n}^{2} \).

Solution. 1/ a) Posons \( \delta = \mathrm{d}\left( {x, C}\right) = \mathop{\inf }\limits_{{z \in C}}\parallel x - z\parallel \) . Il existe une suite \( \left( {y}_{n}\right) \) de \( C \) telle que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) . En utilisant le fait que \( H \) est un espace de Hilbert, nous allons montrer que ceci entraîne la convergence de \( \left( {y}_{n}\right) \) . Comme \( H \) est complet, il suffit de montrer que \( \left( {y}_{n}\right) \) est de Cauchy.

> Solution. 1/ a) Let \( \delta = \mathrm{d}\left( {x, C}\right) = \mathop{\inf }\limits_{{z \in C}}\parallel x - z\parallel \) . There exists a sequence \( \left( {y}_{n}\right) \) of \( C \) such that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) . Using the fact that \( H \) is a Hilbert space, we will show that this implies the convergence of \( \left( {y}_{n}\right) \) . Since \( H \) is complete, it suffices to show that \( \left( {y}_{n}\right) \) is Cauchy.

Comme la norme \( \parallel .\parallel \) est issue d’un produit scalaire, elle vérifie l’identité du parallélogramme, donc

> Since the norm \( \parallel .\parallel \) is derived from an inner product, it satisfies the parallelogram identity, so

\[
\forall p, q \in  \mathbb{N},\;{\begin{Vmatrix}\left( x - {y}_{p}\right)  + \left( x - {y}_{q}\right) \end{Vmatrix}}^{2} + {\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} = 2\left( {{\begin{Vmatrix}x - {y}_{p}\end{Vmatrix}}^{2} + {\begin{Vmatrix}x - {y}_{q}\end{Vmatrix}}^{2}}\right) .
\]

(*)

> Or \( C \) est convexe, donc \( \left( {{y}_{p} + {y}_{q}}\right) /2 \in C \) pour tout \( p, q \in \mathbb{N} \) , donc \( \begin{Vmatrix}{x - \frac{{y}_{p} + {y}_{q}}{2}}\end{Vmatrix} \geq \delta \) , ou encore \( {\begin{Vmatrix}\left( x - {y}_{p}\right) + \left( x - {y}_{q}\right) \end{Vmatrix}}^{2} \geq 4{\delta }^{2} \) . Avec (*), on en déduit

Now \( C \) is convex, so \( \left( {{y}_{p} + {y}_{q}}\right) /2 \in C \) for all \( p, q \in \mathbb{N} \) , thus \( \begin{Vmatrix}{x - \frac{{y}_{p} + {y}_{q}}{2}}\end{Vmatrix} \geq \delta \) , or equivalently \( {\begin{Vmatrix}\left( x - {y}_{p}\right) + \left( x - {y}_{q}\right) \end{Vmatrix}}^{2} \geq 4{\delta }^{2} \) . With (*), we deduce

\[
\forall p, q \in  \mathbb{N},\;{\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} \leq  2\left\lbrack  {\left( {{\begin{Vmatrix}x - {y}_{p}\end{Vmatrix}}^{2} - {\delta }^{2}}\right)  + \left( {{\begin{Vmatrix}x - {y}_{q}\end{Vmatrix}}^{2} - {\delta }^{2}}\right) }\right\rbrack  ,
\]

et comme \( \begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} \) tend vers \( \delta \) , on voit que \( \left( {y}_{n}\right) \) est bien une suite de Cauchy.

> and since \( \begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} \) tends to \( \delta \) , we see that \( \left( {y}_{n}\right) \) is indeed a Cauchy sequence.

Soit \( y \) la limite de \( \left( {y}_{n}\right) \) . Comme \( C \) est fermé, on a \( y \in C \) et \( \parallel x - y\parallel = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \; \delta = \mathrm{d}\left( {x, C}\right) . \)

> Let \( y \) be the limit of \( \left( {y}_{n}\right) \) . Since \( C \) is closed, we have \( y \in C \) and \( \parallel x - y\parallel = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \; \delta = \mathrm{d}\left( {x, C}\right) . \)

Il nous reste à montrer que \( y \) est unique. Supposons \( \parallel x - z\parallel = \delta \) avec \( z \in C \) , et définissons une suite \( \left( {y}_{n}\right) \) de \( C \) par \( {y}_{n} = y \) si \( n \) est pair, \( {y}_{n} = z \) si \( n \) est impair. Cette suite vérifie \( \parallel x - {y}_{n}\parallel = \delta \) pour tout \( n \) , en particulier \( \begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} \) tend vers \( \delta \) , donc d’après ce que nous avons prouvé plus haut, \( \left( {y}_{n}\right) \) converge. Ceci entraîne \( z = y \) , d’où l’unicité.

> It remains to show that \( y \) is unique. Suppose \( \parallel x - z\parallel = \delta \) with \( z \in C \) , and define a sequence \( \left( {y}_{n}\right) \) of \( C \) by \( {y}_{n} = y \) if \( n \) is even, \( {y}_{n} = z \) if \( n \) is odd. This sequence satisfies \( \parallel x - {y}_{n}\parallel = \delta \) for all \( n \) , in particular \( \begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} \) tends to \( \delta \) , so according to what we proved above, \( \left( {y}_{n}\right) \) converges. This implies \( z = y \) , hence the uniqueness.

b) Supposons d’abord que pour \( y \in C \) , on ait

> b) Suppose first that for \( y \in C \) , we have

\[
\forall z \in  C,\;\langle z - y, x - y\rangle  \leq  0.
\]

Alors pour tout \( z \in C \) ,

> Then for all \( z \in C \) ,

\( \parallel z - x{\parallel }^{2} = \parallel \left( {z - y}\right) - \left( {x - y}\right) {\parallel }^{2} = \parallel z - y{\parallel }^{2} + \parallel x - y{\parallel }^{2} - 2\langle z - y, x - y\rangle \geq \parallel z - y{\parallel }^{2} + \parallel x - y{\parallel }^{2} \geq \parallel x - y{\parallel }^{2}, \) donc \( \parallel z - x\parallel \geq \parallel y - x\parallel \) pour tout \( z \in C \) . De plus \( y \in C \) , donc \( \parallel y - x\parallel = \mathrm{d}\left( {x, C}\right) \) , et d’après la question précédente, \( y = {x}_{C} \) .

> \( \parallel z - x{\parallel }^{2} = \parallel \left( {z - y}\right) - \left( {x - y}\right) {\parallel }^{2} = \parallel z - y{\parallel }^{2} + \parallel x - y{\parallel }^{2} - 2\langle z - y, x - y\rangle \geq \parallel z - y{\parallel }^{2} + \parallel x - y{\parallel }^{2} \geq \parallel x - y{\parallel }^{2}, \) so \( \parallel z - x\parallel \geq \parallel y - x\parallel \) for all \( z \in C \) . Furthermore \( y \in C \) , so \( \parallel y - x\parallel = \mathrm{d}\left( {x, C}\right) \) , and according to the previous question, \( y = {x}_{C} \) .

Montrons maintenant que la propriété est vérifiée pour \( y = {x}_{C} \) . Pour tout \( z \in C \) , on a \( \parallel x - z{\parallel }^{2} \geq {\begin{Vmatrix}x - {x}_{C}\end{Vmatrix}}^{2} \) , et en développant \( \parallel x - z{\parallel }^{2} = {\begin{Vmatrix}\left( x - {x}_{C}\right) - \left( z - {x}_{C}\right) \end{Vmatrix}}^{2} \) , on obtient donc

> Let us now show that the property holds for \( y = {x}_{C} \) . For all \( z \in C \) , we have \( \parallel x - z{\parallel }^{2} \geq {\begin{Vmatrix}x - {x}_{C}\end{Vmatrix}}^{2} \) , and by expanding \( \parallel x - z{\parallel }^{2} = {\begin{Vmatrix}\left( x - {x}_{C}\right) - \left( z - {x}_{C}\right) \end{Vmatrix}}^{2} \) , we thus obtain

\[
\forall z \in  C,\; - 2\left\langle  {x - {x}_{C}, z - {x}_{C}}\right\rangle   + {\begin{Vmatrix}z - {x}_{C}\end{Vmatrix}}^{2} \geq  0.
\]

\( \left( {* * }\right) \)

> Il s’agit de se débarrasser du terme en \( {\begin{Vmatrix}z - {x}_{C}\end{Vmatrix}}^{2} \) . L’idée est que lorsque \( z \) est proche de \( {x}_{C} \) , le terme \( {\begin{Vmatrix}z - {x}_{C}\end{Vmatrix}}^{2} \) est petit devant l’autre ; on va donc appliquer (**) a un point \( z \) qui tend vers \( {x}_{C} \) . Fixons \( {z}_{0} \in C \) . Comme \( C \) est convexe, on a \( z = \lambda {z}_{0} + \left( {1 - \lambda }\right) {x}_{C} \in C \) pour tout \( \lambda \in \left\lbrack {0,1}\right\rbrack \) , donc en appliquant (**) à \( z \) , on tire

The goal is to get rid of the term in \( {\begin{Vmatrix}z - {x}_{C}\end{Vmatrix}}^{2} \) . The idea is that when \( z \) is close to \( {x}_{C} \) , the term \( {\begin{Vmatrix}z - {x}_{C}\end{Vmatrix}}^{2} \) is small compared to the other; we will therefore apply (**) to a point \( z \) that tends towards \( {x}_{C} \) . Let us fix \( {z}_{0} \in C \) . Since \( C \) is convex, we have \( z = \lambda {z}_{0} + \left( {1 - \lambda }\right) {x}_{C} \in C \) for all \( \lambda \in \left\lbrack {0,1}\right\rbrack \) , so by applying (**) to \( z \) , we derive

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\; - {2\lambda }\left\langle  {x - {x}_{C},{z}_{0} - {x}_{C}}\right\rangle   + {\lambda }^{2}{\begin{Vmatrix}{z}_{0} - {x}_{C}\end{Vmatrix}}^{2} \geq  0,
\]

donc

> so

\[
\forall \lambda  \in  \rbrack 0,1\rbrack ,\; - 2\left\langle  {x - {x}_{C},{z}_{0} - {x}_{C}}\right\rangle   + \lambda {\begin{Vmatrix}{z}_{0} - {x}_{C}\end{Vmatrix}}^{2} \geq  0,
\]

et en faisant tendre \( \lambda \) vers 0 dans cette dernière inégalité, on obtient \( - 2\left\langle {x - {x}_{C},{z}_{0} - {x}_{C}}\right\rangle \geq 0 \) , et ceci pour tout \( {z}_{0} \in C \) , d’où le résultat.

> and by letting \( \lambda \) tend to 0 in this last inequality, we obtain \( - 2\left\langle {x - {x}_{C},{z}_{0} - {x}_{C}}\right\rangle \geq 0 \) , and this for all \( {z}_{0} \in C \) , hence the result.

2/ a) Le fait que \( {A}^{ \bot } \) soit un s.e.v de \( H \) est immédiat. Pour montrer que \( {A}^{ \bot } \) est fermé, on considère une suite \( \left( {x}_{n}\right) \) de \( {A}^{ \bot } \) qui converge vers un point \( x \) de \( H \) . Pour tout \( y \in A \) , on a \( \left\langle {{x}_{n}, y}\right\rangle = 0 \) , et par continuité du produit scalaire (qui provient de l’inégalité de Schwarz), on en déduit, en faisant \( n \rightarrow + \infty \) , que \( \langle x, y\rangle = 0 \) . Ceci est vrai pour tout \( y \in A \) , donc \( x \in {A}^{ \bot } \) .

> 2/ a) The fact that \( {A}^{ \bot } \) is a subspace of \( H \) is immediate. To show that \( {A}^{ \bot } \) is closed, we consider a sequence \( \left( {x}_{n}\right) \) in \( {A}^{ \bot } \) that converges to a point \( x \) in \( H \) . For all \( y \in A \) , we have \( \left\langle {{x}_{n}, y}\right\rangle = 0 \) , and by continuity of the scalar product (which follows from the Schwarz inequality), we deduce, by letting \( n \rightarrow + \infty \) , that \( \langle x, y\rangle = 0 \) . This is true for all \( y \in A \) , so \( x \in {A}^{ \bot } \) .

b) Montrons (i). Il est clair que \( F \cap {F}^{ \bot } = \{ 0\} \) , car si \( \langle x, x\rangle = 0 \) , on a \( x = 0 \) . Montrons maintenant \( F \oplus {F}^{ \bot } = H \) . Soit \( x \in H \) . Comme \( F \) , s.e.v fermé de \( H \) , est un convexe fermé de \( H \) , on peut appliquer les résultats de \( 1/ \) . Donc il existe un unique élément \( {x}_{F} \in F \) tel que \( \begin{Vmatrix}{x - {x}_{F}}\end{Vmatrix} = \mathrm{d}\left( {x, F}\right) \) , et on a

> b) Let us show (i). It is clear that \( F \cap {F}^{ \bot } = \{ 0\} \), because if \( \langle x, x\rangle = 0 \), we have \( x = 0 \). Let us now show \( F \oplus {F}^{ \bot } = H \). Let \( x \in H \). Since \( F \), a closed subspace of \( H \), is a closed convex set of \( H \), we can apply the results of \( 1/ \). Thus, there exists a unique element \( {x}_{F} \in F \) such that \( \begin{Vmatrix}{x - {x}_{F}}\end{Vmatrix} = \mathrm{d}\left( {x, F}\right) \), and we have

\[
\forall z \in  F,\;\left\langle  {z - {x}_{F}, x - {x}_{F}}\right\rangle   \leq  0.
\]

Comme \( F \) est un s.e.v, il est symétrique par rapport à \( {x}_{F} \in F \) , et cette dernière inégalité est donc une égalité. On en tire

> Since \( F \) is a subspace, it is symmetric with respect to \( {x}_{F} \in F \), and this last inequality is therefore an equality. From this, we derive

\[
\forall z \in  F,\;\left\langle  {z, x - {x}_{F}}\right\rangle   = \left\langle  {z - {x}_{F}, x - {x}_{F}}\right\rangle   - \left\langle  {0 - {x}_{F}, x - {x}_{F}}\right\rangle   = 0,
\]

donc \( x - {x}_{F} \in {F}^{ \bot } \) . En conclusion, on a \( x = {x}_{F} + \left( {x - {x}_{F}}\right) \) avec \( {x}_{F} \in F \) et \( x - {x}_{F} \in {F}^{ \bot } \) , donc \( x \in F \oplus {F}^{ \bot } \) , et ceci étant vrai pour tout \( x \in H \) , on a bien \( H = F \oplus {F}^{ \bot } \) . Du même coup, nous avons montré que \( {x}_{F} = {p}_{F}\left( x\right) \) , qui est l’assertion (ii).

> thus \( x - {x}_{F} \in {F}^{ \bot } \). In conclusion, we have \( x = {x}_{F} + \left( {x - {x}_{F}}\right) \) with \( {x}_{F} \in F \) and \( x - {x}_{F} \in {F}^{ \bot } \), so \( x \in F \oplus {F}^{ \bot } \), and since this is true for all \( x \in H \), we indeed have \( H = F \oplus {F}^{ \bot } \). At the same time, we have shown that \( {x}_{F} = {p}_{F}\left( x\right) \), which is assertion (ii).

Il nous reste à montrer (iii). Il est clair que \( F \subset {F}^{ \bot \bot } \) , car si \( x \in F \) , on a \( \langle x, y\rangle = 0 \) pour tout \( y \in {F}^{ \bot } \) , donc \( x \in {F}^{ \bot \bot } \) . Montrons l’inclusion réciproque. Soit \( x \in {F}^{ \bot \bot } \) . Comme \( F \oplus {F}^{ \bot } = H \) , il existe un unique couple \( \left( {{x}_{1},{x}_{2}}\right) \in F \times {F}^{ \bot } \) tel que \( x = {x}_{1} + {x}_{2} \) . Or \( x \) est orthogonal à \( {F}^{ \bot } \) , donc \( \left\langle {{x}_{2}, x}\right\rangle = 0 = \left\langle {{x}_{2},{x}_{1}}\right\rangle + \left\langle {{x}_{2},{x}_{2}}\right\rangle = {\begin{Vmatrix}{x}_{2}\end{Vmatrix}}^{2} \) , donc \( {x}_{2} = 0 \) , et finalement \( x = {x}_{1} \in F \) . On a donc \( {F}^{ \bot \bot } \subset F \) , d’où (iii).

> It remains for us to show (iii). It is clear that \( F \subset {F}^{ \bot \bot } \), because if \( x \in F \), we have \( \langle x, y\rangle = 0 \) for all \( y \in {F}^{ \bot } \), so \( x \in {F}^{ \bot \bot } \). Let us show the reverse inclusion. Let \( x \in {F}^{ \bot \bot } \). Since \( F \oplus {F}^{ \bot } = H \), there exists a unique pair \( \left( {{x}_{1},{x}_{2}}\right) \in F \times {F}^{ \bot } \) such that \( x = {x}_{1} + {x}_{2} \). However, \( x \) is orthogonal to \( {F}^{ \bot } \), so \( \left\langle {{x}_{2}, x}\right\rangle = 0 = \left\langle {{x}_{2},{x}_{1}}\right\rangle + \left\langle {{x}_{2},{x}_{2}}\right\rangle = {\begin{Vmatrix}{x}_{2}\end{Vmatrix}}^{2} \), so \( {x}_{2} = 0 \), and finally \( x = {x}_{1} \in F \). We therefore have \( {F}^{ \bot \bot } \subset F \), hence (iii).

c) L’ensemble \( \bar{F} \) est un s.e.v fermé de \( H \) , donc \( \bar{F} = {\left( \bar{F}\right) }^{ \bot \bot } \) . Or

> c) The set \( \bar{F} \) is a closed subspace of \( H \), so \( \bar{F} = {\left( \bar{F}\right) }^{ \bot \bot } \). However

\[
F \subset  \bar{F}\;\text{ donc }\;{\left( \bar{F}\right) }^{ \bot  } \subset  {F}^{ \bot  }\;\text{ donc }\;{F}^{ \bot   \bot  } \subset  {\left( \bar{F}\right) }^{ \bot   \bot  } = \bar{F}.
\]

\( \left( {* * * }\right) \)

> Par ailleurs, \( F \subset {F}^{ \bot \bot } \) , et comme un orthogonal est fermé, \( \bar{F} \subset {F}^{ \bot \bot } \) . Avec (***), on en déduit \( \bar{F} = {F}^{ \bot \bot } \) .

Furthermore, \( F \subset {F}^{ \bot \bot } \), and since an orthogonal complement is closed, \( \bar{F} \subset {F}^{ \bot \bot } \). With (***), we deduce \( \bar{F} = {F}^{ \bot \bot } \).

> d) Comme \( \bar{F} = {F}^{ \bot \bot } \) et que \( H = {F}^{ \bot } \oplus {F}^{ \bot \bot } \) (car \( {F}^{ \bot } \) est un s.e.v fermé), on a \( H = {F}^{ \bot } + \bar{F} \) , donc \( \bar{F} = H \) si et seulement si \( {F}^{ \bot } = \{ 0\} \) .

d) Since \( \bar{F} = {F}^{ \bot \bot } \) and \( H = {F}^{ \bot } \oplus {F}^{ \bot \bot } \) (because \( {F}^{ \bot } \) is a closed subspace), we have \( H = {F}^{ \bot } + \bar{F} \) , therefore \( \bar{F} = H \) if and only if \( {F}^{ \bot } = \{ 0\} \) .

> 3/ a) Remarquons tout d’abord que \( {\varphi }_{a} \) est bien une forme linéaire, et elle est continue d’après l'inégalité de Schwarz.

3/ a) First, let us note that \( {\varphi }_{a} \) is indeed a linear form, and it is continuous according to the Schwarz inequality.

> L’application \( H \rightarrow {H}^{\prime }\;a \mapsto {\varphi }_{a} \) est clairement linéaire. Elle est injective car si \( {\varphi }_{a} = 0 \) , alors \( 0 = {\varphi }_{a}\left( a\right) = \langle a, a\rangle = \parallel a{\parallel }^{2} \) , donc \( a = 0 \) .

The mapping \( H \rightarrow {H}^{\prime }\;a \mapsto {\varphi }_{a} \) is clearly linear. It is injective because if \( {\varphi }_{a} = 0 \) , then \( 0 = {\varphi }_{a}\left( a\right) = \langle a, a\rangle = \parallel a{\parallel }^{2} \) , therefore \( a = 0 \) .

> Il nous reste à montrer (c’est plus délicat) qu’elle est surjective. Soit \( L \in {H}^{\prime } \) . Si \( L = 0 \) , \( L = {\varphi }_{0} \) et c’est terminé. Sinon, \( L \neq 0 \) , et \( \operatorname{Ker}L = {L}^{-1}\left( {\{ 0\} }\right) \) est un s.e.v de \( H \) , fermé car \( L \) est continue. Donc d’après \( 2/\mathrm{a}),\left( {\operatorname{Ker}L}\right) \oplus {\left( \operatorname{Ker}L\right) }^{ \bot } = H \) . Si \( L \) était nulle sur \( {\left( \operatorname{Ker}L\right) }^{ \bot } \) , alors \( L \) serait nulle sur \( H \) ce qui est absurde par hypothèse. Donc il existe \( a \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) tel que \( L\left( a\right) \neq 0 \) .

It remains for us to show (this is more delicate) that it is surjective. Let \( L \in {H}^{\prime } \) . If \( L = 0 \) , \( L = {\varphi }_{0} \) and we are done. Otherwise, \( L \neq 0 \) , and \( \operatorname{Ker}L = {L}^{-1}\left( {\{ 0\} }\right) \) is a subspace of \( H \) , closed because \( L \) is continuous. Thus, according to \( 2/\mathrm{a}),\left( {\operatorname{Ker}L}\right) \oplus {\left( \operatorname{Ker}L\right) }^{ \bot } = H \) . If \( L \) were zero on \( {\left( \operatorname{Ker}L\right) }^{ \bot } \) , then \( L \) would be zero on \( H \) , which is absurd by hypothesis. Therefore, there exists \( a \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) such that \( L\left( a\right) \neq 0 \) .

> Montrons que \( {\left( \operatorname{Ker}L\right) }^{ \bot } = \operatorname{Vect}\left( a\right) \) . Soit \( v \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) . On pose

Let us show that \( {\left( \operatorname{Ker}L\right) }^{ \bot } = \operatorname{Vect}\left( a\right) \) . Let \( v \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) . We define

\[
w = v - \frac{L\left( v\right) }{L\left( a\right) }a\;\text{ qui vérifie }\;L\left( w\right)  = L\left( v\right)  - L\left( {\frac{L\left( v\right) }{L\left( a\right) }a}\right)  = L\left( v\right)  - \frac{L\left( v\right) }{L\left( a\right) }L\left( a\right)  = 0,
\]

donc \( w \in \operatorname{Ker}L \) . Par ailleurs, \( w \) est combinaison linéaire de deux éléments de ( \( \operatorname{Ker}L{)}^{ \bot } \) , donc \( w \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) . Finalement, \( w \in \left( {\operatorname{Ker}L}\right) \cap {\left( \operatorname{Ker}L\right) }^{ \bot } = \{ 0\} \) donc \( w = 0 \) , c’est-à-dire \( v = \frac{L\left( v\right) }{L\left( a\right) }a \in \; \operatorname{Vect}\left( a\right) \) . On a donc bien \( {\left( \operatorname{Ker}L\right) }^{ \bot } = \operatorname{Vect}\left( a\right) \) .

> therefore \( w \in \operatorname{Ker}L \) . Furthermore, \( w \) is a linear combination of two elements of \( \operatorname{Ker}L{)}^{ \bot } \) , therefore \( w \in {\left( \operatorname{Ker}L\right) }^{ \bot } \) . Finally, \( w \in \left( {\operatorname{Ker}L}\right) \cap {\left( \operatorname{Ker}L\right) }^{ \bot } = \{ 0\} \) therefore \( w = 0 \) , that is to say \( v = \frac{L\left( v\right) }{L\left( a\right) }a \in \; \operatorname{Vect}\left( a\right) \) . We have thus indeed \( {\left( \operatorname{Ker}L\right) }^{ \bot } = \operatorname{Vect}\left( a\right) \) .

Ceci étant, posons \( b = \frac{L\left( a\right) }{\parallel a{\parallel }^{2}}a \) . Nous allons montrer \( {\varphi }_{b} = L \) .

> This being said, let us set \( b = \frac{L\left( a\right) }{\parallel a{\parallel }^{2}}a \) . We will show \( {\varphi }_{b} = L \) .

- Pour tout \( x \in  \operatorname{Ker}L \) , on a \( {\varphi }_{b}\left( x\right)  = \frac{L\left( a\right) }{\parallel a{\parallel }^{2}}\langle a, x\rangle  = 0 \) car \( a \in  {\left( \operatorname{Ker}L\right) }^{ \bot  } \) .

> - For all \( x \in  \operatorname{Ker}L \) , we have \( {\varphi }_{b}\left( x\right)  = \frac{L\left( a\right) }{\parallel a{\parallel }^{2}}\langle a, x\rangle  = 0 \) because \( a \in  {\left( \operatorname{Ker}L\right) }^{ \bot  } \) .

- Si \( x \in  {\left( \operatorname{Ker}L\right) }^{ \bot  } \) , alors il existe \( \lambda  \in  \mathbb{R} \) tel que \( x = {\lambda a} \) , donc

> - If \( x \in  {\left( \operatorname{Ker}L\right) }^{ \bot  } \) , then there exists \( \lambda  \in  \mathbb{R} \) such that \( x = {\lambda a} \) , therefore

\[
{\varphi }_{b}\left( x\right)  = \lambda {\varphi }_{b}\left( a\right)  = \lambda \frac{L\left( a\right) }{\parallel a{\parallel }^{2}}\langle a, a\rangle  = {\lambda L}\left( a\right)  = L\left( {\lambda a}\right)  = L\left( x\right) .
\]

Finalement, nous avons montré que \( L \) et \( {\varphi }_{b} \) coïncident sur les deux espaces supplémentaires Ker \( L \) et (Ker \( L{)}^{ \bot } \) . Donc \( L = {\varphi }_{b} \) , d’où la surjectivité désirée.

> Finally, we have shown that \( L \) and \( {\varphi }_{b} \) coincide on the two supplementary spaces Ker \( L \) and (Ker \( L{)}^{ \bot } \) . Thus \( L = {\varphi }_{b} \) , whence the desired surjectivity.

b) Soit \( y \in H \) . L’application \( x \mapsto \langle u\left( x\right) , y\rangle \) est une forme linéaire continue, donc d’après \( 3/a \) ),

> b) Let \( y \in H \) . The mapping \( x \mapsto \langle u\left( x\right) , y\rangle \) is a continuous linear form, so according to \( 3/a \) ),

\[
\exists !{a}_{y} \in  H,\forall x \in  H,\;\langle u\left( x\right) , y\rangle  = \left\langle  {{a}_{y}, x}\right\rangle  .
\]

L’unicité de \( {a}_{y} \) entraîne que \( y \mapsto {a}_{y} \) est linéaire. Notons \( v \) l’endomorphisme de \( H \) défini par \( v\left( y\right) = {a}_{y} \) , de sorte que

> The uniqueness of \( {a}_{y} \) implies that \( y \mapsto {a}_{y} \) is linear. Let \( v \) denote the endomorphism of \( H \) defined by \( v\left( y\right) = {a}_{y} \) , so that

\[
\forall x, y \in  H,\;\langle u\left( x\right) , y\rangle  = \langle x, v\left( y\right) \rangle .
\]

L’unicité de \( {a}_{y} \) entraîne celle de \( v \) . Il nous reste à montrer que \( v \) est continu. Pour tout \( y \in H \) , on a

> The uniqueness of \( {a}_{y} \) implies that of \( v \) . It remains for us to show that \( v \) is continuous. For all \( y \in H \) , we have

\[
\parallel v\left( y\right) {\parallel }^{2} = \langle v\left( y\right) , v\left( y\right) \rangle  = \langle u\left\lbrack  {v\left( y\right) }\right\rbrack  , y\rangle  \leq  \parallel u\left\lbrack  {v\left( y\right) }\right\rbrack  \parallel  \cdot  \parallel y\parallel  \leq  \parallel u\parallel  \cdot  \parallel v\left( y\right) \parallel  \cdot  \parallel y\parallel ,
\]

donc \( \parallel v\left( y\right) \parallel \leq \parallel u\parallel \cdot \parallel y\parallel \) . Ceci étant vrai pour tout \( y \in H \) , on en déduit que \( v \) est continu et que \( \parallel v\parallel \leq \parallel u\parallel \)

> thus \( \parallel v\left( y\right) \parallel \leq \parallel u\parallel \cdot \parallel y\parallel \) . Since this is true for all \( y \in H \) , we deduce that \( v \) is continuous and that \( \parallel v\parallel \leq \parallel u\parallel \)

Nous avons donc prouvé l’existence et l’unicité de \( {u}^{ * } \) , et on a \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \leq \parallel u\parallel \) . De même, \( \begin{Vmatrix}{u}^{* * }\end{Vmatrix} \leq \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \) . L’unicité de l’adjoint entraîne \( {u}^{* * } = u \) , donc \( \parallel u\parallel \leq \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \) , et finalement, on a \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} = \parallel u\parallel . \)

> We have thus proven the existence and uniqueness of \( {u}^{ * } \) , and we have \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \leq \parallel u\parallel \) . Similarly, \( \begin{Vmatrix}{u}^{* * }\end{Vmatrix} \leq \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \) . The uniqueness of the adjoint implies \( {u}^{* * } = u \) , thus \( \parallel u\parallel \leq \begin{Vmatrix}{u}^{ * }\end{Vmatrix} \) , and finally, we have \( \begin{Vmatrix}{u}^{ * }\end{Vmatrix} = \parallel u\parallel . \)

4 / a) Pour tout \( n \) , notons \( {E}_{n} = \operatorname{Vect}{\left( {e}_{k}\right) }_{0 < k < n} \) , s.e.v de dimension finie de \( H \) , donc fermé. La projection orthogonale de \( v \) sur \( {E}_{n} \) est \( {p}_{{E}_{n}}\left( v\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{\lambda }_{k}{e}_{k} \) (en effet, si \( {p}_{{E}_{n}}\left( v\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{\mu }_{k}{e}_{k} \) , on a \( v - {p}_{{E}_{n}}\left( v\right) \in {E}_{n}^{ \bot } \) , donc pour tout \( k,0 \leq k \leq n,0 = \left\langle {v - {p}_{{E}_{n}}\left( v\right) ,{e}_{k}}\right\rangle = \left\langle {v,{e}_{k}}\right\rangle - {\mu }_{k} = {\lambda }_{k} - {\mu }_{k} \) ).

> 4 / a) For all \( n \) , let \( {E}_{n} = \operatorname{Vect}{\left( {e}_{k}\right) }_{0 < k < n} \) be a finite-dimensional subspace of \( H \) , and therefore closed. The orthogonal projection of \( v \) onto \( {E}_{n} \) is \( {p}_{{E}_{n}}\left( v\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{\lambda }_{k}{e}_{k} \) (indeed, if \( {p}_{{E}_{n}}\left( v\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{\mu }_{k}{e}_{k} \) , we have \( v - {p}_{{E}_{n}}\left( v\right) \in {E}_{n}^{ \bot } \) , thus for all \( k,0 \leq k \leq n,0 = \left\langle {v - {p}_{{E}_{n}}\left( v\right) ,{e}_{k}}\right\rangle = \left\langle {v,{e}_{k}}\right\rangle - {\mu }_{k} = {\lambda }_{k} - {\mu }_{k} \) ).

En particulier, \( {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{k = 0}}^{n}{\lambda }_{k}^{2} \) . Comme \( {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} \leq \parallel v{\parallel }^{2} \) (car \( \parallel v{\parallel }^{2} = {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} + \; {\left. {\begin{Vmatrix}v - {p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2}\right) }^{2} \) , on en déduit que la série \( \sum {\lambda }_{n}^{2} \) converge. Comme \( {\begin{Vmatrix}\mathop{\sum }\limits_{{n = p}}^{q}{\lambda }_{n}{e}_{n}\end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{n = p}}^{q}{\lambda }_{n}^{2} \) , la série \( \sum {\lambda }_{n}{e}_{n} \) est de Cauchy, donc elle converge car \( H \) est complet. Notons \( w \) sa somme.

> In particular, \( {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{k = 0}}^{n}{\lambda }_{k}^{2} \) . As \( {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} \leq \parallel v{\parallel }^{2} \) (since \( \parallel v{\parallel }^{2} = {\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} + \; {\left. {\begin{Vmatrix}v - {p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2}\right) }^{2} \) ), we deduce that the series \( \sum {\lambda }_{n}^{2} \) converges. As \( {\begin{Vmatrix}\mathop{\sum }\limits_{{n = p}}^{q}{\lambda }_{n}{e}_{n}\end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{n = p}}^{q}{\lambda }_{n}^{2} \) , the series \( \sum {\lambda }_{n}{e}_{n} \) is Cauchy, so it converges because \( H \) is complete. Let us denote its sum by \( w \) .

Pour tout \( n \in \mathbb{N} \) , on a \( \left\langle {v - w,{e}_{n}}\right\rangle = \left\langle {v,{e}_{n}}\right\rangle - \left\langle {w,{e}_{n}}\right\rangle = {\lambda }_{n} - {\lambda }_{n} = 0 \) , donc \( v - w \in {E}^{ \bot } \) . Or \( w \in E \) , donc \( w = {p}_{E}\left( v\right) \) .

> For all \( n \in \mathbb{N} \) , we have \( \left\langle {v - w,{e}_{n}}\right\rangle = \left\langle {v,{e}_{n}}\right\rangle - \left\langle {w,{e}_{n}}\right\rangle = {\lambda }_{n} - {\lambda }_{n} = 0 \) , so \( v - w \in {E}^{ \bot } \) . However, \( w \in E \) , therefore \( w = {p}_{E}\left( v\right) \) .

Comme \( w = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{p}_{{E}_{n}}\left( v\right) \) , on a \( \parallel w{\parallel }^{2} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\lambda }_{n}^{2} \) , et \( \parallel w{\parallel }^{2} = \; {\begin{Vmatrix}{p}_{E}\left( v\right) \end{Vmatrix}}^{2} \leq \parallel v{\parallel }^{2}. \)

> Since \( w = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{p}_{{E}_{n}}\left( v\right) \) , we have \( \parallel w{\parallel }^{2} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\begin{Vmatrix}{p}_{{E}_{n}}\left( v\right) \end{Vmatrix}}^{2} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\lambda }_{n}^{2} \) , and \( \parallel w{\parallel }^{2} = \; {\begin{Vmatrix}{p}_{E}\left( v\right) \end{Vmatrix}}^{2} \leq \parallel v{\parallel }^{2}. \)

b) Il suffit de remarquer que dans ce cas, \( E = H \) et \( w = {P}_{H}\left( v\right) = v \) .

> b) It suffices to note that in this case, \( E = H \) and \( w = {P}_{H}\left( v\right) = v \) .

Remarque. Les résultats des questions de 1/ (resp. de 2/b)) restent vrais dans un espace préhilbertien si \( C \) est supposé complet (resp. si \( F \) est complet, en particulier s’il est de dimension finie). Les démonstrations sont les mêmes.

> Remark. The results of the questions in 1/ (resp. 2/b)) remain true in a pre-Hilbert space if \( C \) is assumed to be complete (resp. if \( F \) is complete, in particular if it is finite-dimensional). The proofs are the same.

S’il existe une famille libre dénombrable de vecteurs \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) telle que \( \operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) soit dense dans \( H \) , alors \( H \) est séparable (appliquer le procédé d’orthonormalisation de Schmidt). La plupart des espaces de Hilbert dans lesquels on travaille sont séparables.

> If there exists a countable free family of vectors \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) such that \( \operatorname{Vect}{\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) is dense in \( H \) , then \( H \) is separable (apply the Gram-Schmidt orthonormalization process). Most Hilbert spaces we work with are separable.
