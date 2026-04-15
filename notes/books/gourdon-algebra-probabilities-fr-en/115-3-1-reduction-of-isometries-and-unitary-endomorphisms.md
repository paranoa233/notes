#### 3.1. Reduction of isometries and unitary endomorphisms

*Français : 3.1. Réduction des isométries et des endomorphismes unitaires*

Les isométries et les endomorphismes unitaires, bien que n'étant pas autoadjoints, peuvent se réduire de manière intéressante dans une base orthonormale.

> Isometries and unitary endomorphisms, although not self-adjoint, can be reduced in an interesting way in an orthonormal basis.

Proposition 1. Soit \( E \) un espace euclidien (resp. hermitien) et \( u \in \mathcal{L}\left( E\right) \) une isométrie (resp un endomorphisme unitaire). Si F est un s.e.v de E stable par u, alors \( {F}^{ \bot } \) est stable par \( u \) .

> Proposition 1. Let \( E \) be a Euclidean (resp. Hermitian) space and \( u \in \mathcal{L}\left( E\right) \) an isometry (resp. a unitary endomorphism). If F is a subspace of E stable under u, then \( {F}^{ \bot } \) is stable under \( u \).

Démonstration. Il s’agit de montrer que pour tout \( x \in {F}^{ \bot } \) et pour tout \( y \in F, u\left( x\right) \cdot y = 0 \) . Comme \( {u}_{\mid F} \) est une isométrie, \( {u}_{\mid F} \) est bijective (on est en dimension finie), donc il existe \( {y}^{\prime } \in F \) tel que \( y = u\left( {y}^{\prime }\right) \) . On a maintenant

> Proof. We must show that for all \( x \in {F}^{ \bot } \) and for all \( y \in F, u\left( x\right) \cdot y = 0 \) . Since \( {u}_{\mid F} \) is an isometry, \( {u}_{\mid F} \) is bijective (we are in finite dimension), so there exists \( {y}^{\prime } \in F \) such that \( y = u\left( {y}^{\prime }\right) \) . We now have

\[
u\left( x\right)  \cdot  y = u\left( x\right)  \cdot  u\left( {y}^{\prime }\right)  = x \cdot  {y}^{\prime } = 0.
\]

Ceci étant vrai pour tout \( x \in {F}^{ \bot } \) et pour tout \( y \in F,{F}^{ \bot } \) est bien stable par \( u \) .

> Since this is true for all \( x \in {F}^{ \bot } \) and for all \( y \in F,{F}^{ \bot } \) is indeed stable by \( u \) .

Réduction des isométries.

> Reduction of isometries.

\( \rightarrow \) THÉORÉME 1. Soit \( E \) un espace euclidien et \( u \in \mathcal{L}\left( E\right) \) une isométrie. Alors il existe une base orthonormale \( B \) de \( E \) dans laquelle la matrice de u a la forme par blocs

> \( \rightarrow \) THEOREM 1. Let \( E \) be a Euclidean space and \( u \in \mathcal{L}\left( E\right) \) an isometry. Then there exists an orthonormal basis \( B \) of \( E \) in which the matrix of u has the block form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} R\left( {\theta }_{1}\right) & & & & & \\   &  \ddots  & & & 0 & \\   & & R\left( {\theta }_{r}\right) & & & \\   & & & {\varepsilon }_{1} & & \\   & 0 & & &  \ddots  & \\   & & & & & {\varepsilon }_{s} \end{matrix}\right) ,
\]

(*)

> où pour tout \( j,{\varepsilon }_{j} \in \{ - 1,1\} \) et pour tout \( i \) ,

where for all \( j,{\varepsilon }_{j} \in \{ - 1,1\} \) and for all \( i \) ,

\[
R\left( {\theta }_{i}\right)  = \left( \begin{matrix} \cos {\theta }_{i} &  - \sin {\theta }_{i} \\  \sin {\theta }_{i} & \cos {\theta }_{i} \end{matrix}\right)  \in  {\mathcal{M}}_{2}\left( \mathbb{R}\right) ,\;\text{ avec }\;{\theta }_{i} \in  \mathbb{R},{\theta }_{i} \text{ ≢ } 0\;\left( {\;\operatorname{mod}\;\pi }\right) .
\]

Démonstration. On procède par récurrence sur \( n = \dim E \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Nous traitons deux cas.

> Proof. We proceed by induction on \( n = \dim E \) . For \( n = 1 \) , it is obvious. Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \) . We consider two cases.

Premier cas. L’isométrie \( u \) admet au moins une valeur propre réelle \( \varepsilon \) . Soit \( x \) un vecteur propre normé associé. Comme \( \parallel u\left( x\right) \parallel = \parallel {\varepsilon x}\parallel = \left| \varepsilon \right| \parallel x\parallel \) et \( \parallel u\left( x\right) \parallel = \parallel x\parallel \) , on a \( \left| \varepsilon \right| = 1 \) . De plus \( \varepsilon \in \mathbb{R} \) , on en déduit \( \varepsilon \in \{ - 1,1\} \) . Maintenant, comme \( F = \operatorname{Vect}\left( x\right) \) est stable par \( u,{F}^{ \bot } \) est stable par \( u \) d’après la proposition 1. En appliquant l’hypothèse de récurrence à \( {u}_{\mid {F}^{ \bot }} \) , on trouve une base orthonormale \( {B}_{0} \) de \( {F}^{ \bot } \) dans laquelle la matrice de \( {u}_{\mid {F}^{ \bot }} \) a la forme \( \left( *\right) \) . En ajoutant \( x \) a la base \( {B}_{0} \) , on obtient une base orthonormale \( B \) de \( E \) dans laquelle la matrice de \( u \) a la forme \( \left( *\right) \) .

> First case. The isometry \( u \) admits at least one real eigenvalue \( \varepsilon \) . Let \( x \) be an associated normalized eigenvector. Since \( \parallel u\left( x\right) \parallel = \parallel {\varepsilon x}\parallel = \left| \varepsilon \right| \parallel x\parallel \) and \( \parallel u\left( x\right) \parallel = \parallel x\parallel \) , we have \( \left| \varepsilon \right| = 1 \) . Furthermore \( \varepsilon \in \mathbb{R} \) , we deduce \( \varepsilon \in \{ - 1,1\} \) . Now, since \( F = \operatorname{Vect}\left( x\right) \) is stable by \( u,{F}^{ \bot } \) is stable by \( u \) according to proposition 1. By applying the induction hypothesis to \( {u}_{\mid {F}^{ \bot }} \) , we find an orthonormal basis \( {B}_{0} \) of \( {F}^{ \bot } \) in which the matrix of \( {u}_{\mid {F}^{ \bot }} \) has the form \( \left( *\right) \) . By adding \( x \) to the basis \( {B}_{0} \) , we obtain an orthonormal basis \( B \) of \( E \) in which the matrix of \( u \) has the form \( \left( *\right) \) .

Second cas. L’isométrie \( u \) n’a aucune valeur propre réelle. On considère l’endomorphisme \( v = \; u + {u}^{ * } \) . Comme \( v \) est symétrique, \( v \) admet une valeur propre réelle \( \lambda \) associée à un vecteur propre \( x \) . On a \( \left( {u + {u}^{ * }}\right) \left( x\right) = {\lambda x} \) donc \( u\left( {u + {u}^{ * }}\right) \left( x\right) = {u}^{2}\left( x\right) + x = {\lambda u}\left( x\right) \) , d’où \( {u}^{2}\left( x\right) = {\lambda u}\left( x\right) - x\;\left( {* * }\right) \) . Par ailleurs, la famille \( \left( {x, u\left( x\right) }\right) \) est libre puisque \( u \) n’admet pas de valeur propre réelle. En posant \( F = \operatorname{Vect}\left( {x, u\left( x\right) }\right) \) , on voit que \( \dim F = 2 \) et que \( F \) est stable par \( u \) (d’après \( \left( {* * }\right) \) ). Soit \( N = \left( \begin{array}{ll} a & c \\ b & d \end{array}\right) \) la matrice de \( {u}_{\mid F} \) dans une base orthonormale \( {B}_{0} \) de \( F \) . Comme \( {u}_{\mid F} \) est une isométrie, \( {N}^{ * }N = {I}_{n} = N{N}^{ * } \) . Parmi les équations issues de ces égalités, on trouve

> Second case. The isometry \( u \) has no real eigenvalues. Consider the endomorphism \( v = \; u + {u}^{ * } \). Since \( v \) is symmetric, \( v \) admits a real eigenvalue \( \lambda \) associated with an eigenvector \( x \). We have \( \left( {u + {u}^{ * }}\right) \left( x\right) = {\lambda x} \) so \( u\left( {u + {u}^{ * }}\right) \left( x\right) = {u}^{2}\left( x\right) + x = {\lambda u}\left( x\right) \) , hence \( {u}^{2}\left( x\right) = {\lambda u}\left( x\right) - x\;\left( {* * }\right) \) . Furthermore, the family \( \left( {x, u\left( x\right) }\right) \) is linearly independent since \( u \) does not admit any real eigenvalue. By setting \( F = \operatorname{Vect}\left( {x, u\left( x\right) }\right) \) , we see that \( \dim F = 2 \) and that \( F \) is stable under \( u \) (according to \( \left( {* * }\right) \) ). Let \( N = \left( \begin{array}{ll} a & c \\ b & d \end{array}\right) \) be the matrix of \( {u}_{\mid F} \) in an orthonormal basis \( {B}_{0} \) of \( F \) . Since \( {u}_{\mid F} \) is an isometry, \( {N}^{ * }N = {I}_{n} = N{N}^{ * } \) . Among the equations resulting from these equalities, we find

\[
{a}^{2} + {b}^{2} = {a}^{2} + {c}^{2} = 1\;\text{ et }\;{ab} + {cd} = 0.
\]

(***)

> La première assertion de \( \left( {* * * }\right) \) entraîne \( c = \pm b \) . On ne peut pas avoir \( c = b \) car \( N \) serait symétrique ce qui est impossible car \( u \) n’admet pas de valeur propre réelle. Donc \( c = - b \neq 0 \) , et d’après la deuxième assertion de \( \left( {* * * }\right) , d = a \) . Comme de plus \( {a}^{2} + {b}^{2} = 1 \) , il existe \( \theta \in \mathbb{R} \) tel que \( a = \cos \theta \) et \( b = \sin \theta \) (et \( \theta \text{ ≢ } 0\left( {\;\operatorname{mod}\;\pi }\right) \) car \( b \neq 0 \) ). Finalement, la matrice \( N \) est de la forme

The first assertion of \( \left( {* * * }\right) \) implies \( c = \pm b \) . We cannot have \( c = b \) because \( N \) would be symmetric, which is impossible since \( u \) does not admit any real eigenvalue. Thus \( c = - b \neq 0 \) , and according to the second assertion of \( \left( {* * * }\right) , d = a \) . Since, moreover, \( {a}^{2} + {b}^{2} = 1 \) , there exists \( \theta \in \mathbb{R} \) such that \( a = \cos \theta \) and \( b = \sin \theta \) (and \( \theta \text{ ≢ } 0\left( {\;\operatorname{mod}\;\pi }\right) \) because \( b \neq 0 \) ). Finally, the matrix \( N \) is of the form

\[
R\left( \theta \right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) ,\;\theta  \in  \mathbb{R} \smallsetminus  \pi \mathbb{Z}.
\]

Maintenant, d’après la proposition 1 le s.e.v \( {F}^{ \bot } \) est stable par \( u \) , et \( {u}_{\mid {F}^{ \bot }} \) est une isométrie donc il existe d’après l’hypothèse de récurrence une base orthonormale \( {B}_{1} \) de \( {F}^{ \bot } \) qui diagonalise \( {u}_{\mid {F}^{ \bot }} \) . La base \( B \) obtenue en concaténant \( {B}_{0} \) et \( {B}_{1} \) est orthonormale et dans cette base, la matrice de \( u \) a la forme voulue, d’où le théorème.

> Now, according to proposition 1, the subspace \( {F}^{ \bot } \) is stable under \( u \) , and \( {u}_{\mid {F}^{ \bot }} \) is an isometry, so there exists, by the induction hypothesis, an orthonormal basis \( {B}_{1} \) of \( {F}^{ \bot } \) that diagonalizes \( {u}_{\mid {F}^{ \bot }} \) . The basis \( B \) obtained by concatenating \( {B}_{0} \) and \( {B}_{1} \) is orthonormal, and in this basis, the matrix of \( u \) has the desired form, hence the theorem.

Remarque 1. On retrouve ainsi la forme des isométries du plan et de l'espace :

> Remark 1. We thus recover the form of isometries of the plane and space:

- Les isométries directes du plan sont des rotations d'angle \( \theta \) (elles ont pour matrice \( R\left( \theta \right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) \) ), les isométries indirectes des symétries par rapport a des droites (matrice \( \left( \begin{matrix} 1 & 0 \\  0 &  - 1 \end{matrix}\right) \) ). Notez d’ailleurs la relation \( R\left( \theta \right) R\left( {\theta }^{\prime }\right)  = R\left( {\theta  + {\theta }^{\prime }}\right) \) , qui entraîne la commutativité des rotations dans le plan.

> - Direct isometries of the plane are rotations of angle \( \theta \) (they have matrix \( R\left( \theta \right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) \)), indirect isometries are reflections across lines (matrix \( \left( \begin{matrix} 1 & 0 \\  0 &  - 1 \end{matrix}\right) \)). Note also the relation \( R\left( \theta \right) R\left( {\theta }^{\prime }\right)  = R\left( {\theta  + {\theta }^{\prime }}\right) \), which implies the commutativity of rotations in the plane.

- Les isométries directes de l'espace sont des rotations d'angle \( \theta \) autour d'un axe (matrice \( \left( \begin{array}{rrr} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{array}\right) \) , le dernier vecteur de la base étant l’axe de rotation). Lorsque \( \theta  = \pi \) , on parle de retournement.

> - Direct isometries of space are rotations of angle \( \theta \) about an axis (matrix \( \left( \begin{array}{rrr} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{array}\right) \), the last vector of the basis being the axis of rotation). When \( \theta  = \pi \), it is called a half-turn.

Les isométries indirectes de l’espace ont pour matrice \( \left( \begin{matrix} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & - 1 \end{matrix}\right) \) . Lorsque \( \theta = 0 \) , on a affaire à une symétrie par rapport à un plan et on parle alors de réflexion.

> Indirect isometries of space have matrix \( \left( \begin{matrix} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & - 1 \end{matrix}\right) \). When \( \theta = 0 \), we are dealing with a symmetry with respect to a plane, which is then called a reflection.

Remarque 2. La version matricielle de ce théorème est la suivante. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice orthogonale. Alors il existe une matrice orthogonale \( P \) telle que \( {P}^{-1}{MP} = {P}^{ * }{MP} \) ait la forme \( \left( *\right) \) .

> Remark 2. The matrix version of this theorem is as follows. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be an orthogonal matrix. Then there exists an orthogonal matrix \( P \) such that \( {P}^{-1}{MP} = {P}^{ * }{MP} \) has the form \( \left( *\right) \).

##### Reduction of unitary endomorphisms.

*Français : Réduction des endomorphismes unitaires.*

\( \rightarrow \) THÉORÉME 2. Soit \( E \) un espace hermitien et \( u \in \mathcal{L}\left( E\right) \) un endomorphisme unitaire. Alors il existe une base orthonormale qui diagonalise \( u \) , et toutes les valeurs propres de \( u \) ont leur module égal à 1.

> \( \rightarrow \) THEOREM 2. Let \( E \) be a Hermitian space and \( u \in \mathcal{L}\left( E\right) \) a unitary endomorphism. Then there exists an orthonormal basis that diagonalizes \( u \), and all eigenvalues of \( u \) have a modulus equal to 1.

Démonstration. La preuve est plus simple que la précédente. Il est d'abord clair que toute valeur propre \( \lambda \) de \( u \) vérifie \( \left| \lambda \right| = 1 \) , car si \( u\left( x\right) = {\lambda x} \) avec \( x \neq 0 \) , on a \( \parallel x\parallel = \parallel u\left( x\right) \parallel = \left| \lambda \right| \parallel x\parallel \) . On procède ensuite par récurrence sur \( n = \dim E \) . Le cas \( n = 1 \) est immédiat, et le passage du rang \( n - 1 \) au rang \( n \) se fait comme suit.

> Proof. The proof is simpler than the previous one. It is first clear that any eigenvalue \( \lambda \) of \( u \) satisfies \( \left| \lambda \right| = 1 \), because if \( u\left( x\right) = {\lambda x} \) with \( x \neq 0 \), we have \( \parallel x\parallel = \parallel u\left( x\right) \parallel = \left| \lambda \right| \parallel x\parallel \). We then proceed by induction on \( n = \dim E \). The case \( n = 1 \) is immediate, and the step from rank \( n - 1 \) to rank \( n \) is done as follows.

Le corps de base \( \mathbb{C} \) étant algébriquement clos, \( u \) admet au moins une valeur propre complexe \( \lambda \) . Soit \( x \) un vecteur propre associé, \( \parallel x\parallel = 1 \) . La droite \( F = \operatorname{Vect}\left( x\right) \) est stable par \( u \) , donc d’après la proposition 1, l’hyperplan \( {F}^{ \bot } \) est également stable par \( u \) . L’endomorphisme \( {u}_{\mid {F}^{ \bot }} \) est unitaire, et d’après l’hypothèse de récurrence, il existe une base orthonormale \( {B}_{0} \) de \( {F}^{ \bot } \) qui diagonalise \( {u}_{\mid {F}^{ \bot }} \) . En ajoutant \( x \) à \( {B}_{0} \) , on obtient une base orthonormale de \( E \) qui diagonalise \( u \) et le théorème est prouvé.

> Since the base field \( \mathbb{C} \) is algebraically closed, \( u \) admits at least one complex eigenvalue \( \lambda \). Let \( x \) be an associated eigenvector, \( \parallel x\parallel = 1 \). The line \( F = \operatorname{Vect}\left( x\right) \) is stable under \( u \), so according to proposition 1, the hyperplane \( {F}^{ \bot } \) is also stable under \( u \). The endomorphism \( {u}_{\mid {F}^{ \bot }} \) is unitary, and according to the induction hypothesis, there exists an orthonormal basis \( {B}_{0} \) of \( {F}^{ \bot } \) that diagonalizes \( {u}_{\mid {F}^{ \bot }} \). By adding \( x \) to \( {B}_{0} \), we obtain an orthonormal basis of \( E \) that diagonalizes \( u \) and the theorem is proved.

COROLLAIRE 1 (Version matricielle). Soit \( U \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice unitaire. Alors il existe une matrice unitaire \( P \) telle que

> COROLLARY 1 (Matrix version). Let \( U \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a unitary matrix. Then there exists a unitary matrix \( P \) such that

\[
{P}^{-1}{UP} = {P}^{ * }{UP} = \left( \begin{matrix} {e}^{i{\theta }_{1}} & & 0 \\   & {e}^{i{\theta }_{2}} & \\  0 &  \ddots  & \\   & & {e}^{i{\theta }_{n}} \end{matrix}\right) ,
\]

où les \( {\theta }_{i} \) sont des nombres réels.

> where the \( {\theta }_{i} \) are real numbers.
