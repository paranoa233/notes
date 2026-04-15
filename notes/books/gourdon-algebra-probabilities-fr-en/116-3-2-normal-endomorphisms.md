#### 3.2. Normal endomorphisms

*Français : 3.2. Endomorphismes normaux*

Les endomorphismes normaux généralisent les endomorphismes autoadjoints. Comme nous allons le voir, ils sont caractérisés par la propriété de diagonalisation dans une base orthonormée.

> Normal endomorphisms generalize self-adjoint endomorphisms. As we shall see, they are characterized by the property of diagonalization in an orthonormal basis.

Dans cette section, sauf mention explicite, \( E \) désigne un espace hermitien (on rappelle qu'un espace hermitien est nécessairement de dimension finie). DéFINITION 1. Soit \( u \in \mathcal{L}\left( E\right) \) . On dit que \( u \) est normal si \( u \) et \( {u}^{ * } \) commutent.

> In this section, unless explicitly stated otherwise, \( E \) denotes a Hermitian space (recall that a Hermitian space is necessarily finite-dimensional). DEFINITION 1. Let \( u \in \mathcal{L}\left( E\right) \). We say that \( u \) is normal if \( u \) and \( {u}^{ * } \) commute.

Une matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est dite normale si \( M \) et \( {M}^{ * } \) commutent.

> A matrix \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is said to be normal if \( M \) and \( {M}^{ * } \) commute.

Proposition 2. Soit \( u \in \mathcal{L}\left( E\right) \) un endomorphisme normal. Alors pour tout \( x \in E \) , \( \parallel u\left( x\right) \parallel = \begin{Vmatrix}{{u}^{ * }\left( x\right) }\end{Vmatrix}. \)

> Proposition 2. Let \( u \in \mathcal{L}\left( E\right) \) be a normal endomorphism. Then for all \( x \in E \), \( \parallel u\left( x\right) \parallel = \begin{Vmatrix}{{u}^{ * }\left( x\right) }\end{Vmatrix}. \)

Démonstration. Il suffit d'écrire que

> Proof. It suffices to write that

\[
\forall x \in  E,\;\parallel u\left( x\right) {\parallel }^{2} = u\left( x\right)  \cdot  u\left( x\right)  = x \cdot  {u}^{ * }\left\lbrack  {u\left( x\right) }\right\rbrack   = x \cdot  u\left\lbrack  {{u}^{ * }\left( x\right) }\right\rbrack   = {u}^{ * }\left( x\right)  \cdot  {u}^{ * }\left( x\right)  = {\begin{Vmatrix}{u}^{ * }\left( x\right) \end{Vmatrix}}^{2}.
\]

Nous allons montrer qu'un endomorphisme est normal si et seulement s'il se diago-nalise dans une base orthonormée. Les quelques résultats qui suivent nous serviront de préliminaires à la démonstration de ce théorème.

> We will show that an endomorphism is normal if and only if it is diagonalizable in an orthonormal basis. The following results will serve as preliminaries to the proof of this theorem.

LEMME 1. Soit \( u \in \mathcal{L}\left( E\right) \) et \( F \) un s.e.v de \( E \) stable par u. Alors \( {F}^{ \bot } \) est stable par \( {u}^{ * } \) .

> LEMMA 1. Let \( u \in \mathcal{L}\left( E\right) \) and \( F \) be a subspace of \( E \) invariant under u. Then \( {F}^{ \bot } \) is invariant under \( {u}^{ * } \) .

Démonstration. Soit \( x \in F \) . Par hypothèse, \( u\left( x\right) \in F \) donc

> Proof. Let \( x \in F \) . By hypothesis, \( u\left( x\right) \in F \) therefore

\[
\forall y \in  {F}^{ \bot  },\;0 = u\left( x\right)  \cdot  y = x \cdot  {u}^{ * }\left( y\right) .
\]

Ceci étant vrai pour tout \( x \in F \) , on a \( {u}^{ * }\left( y\right) \in {F}^{ \bot } \) . Or on peut choisir \( y \) comme l’on veut dans \( {F}^{ \bot } \) , et donc \( {F}^{ \bot } \) est stable par \( {u}^{ * } \) .

> Since this is true for all \( x \in F \) , we have \( {u}^{ * }\left( y\right) \in {F}^{ \bot } \) . However, we can choose \( y \) as we wish in \( {F}^{ \bot } \) , and thus \( {F}^{ \bot } \) is invariant under \( {u}^{ * } \) .

Remarque 3. Notez que ce résultat n'est pas spécifique aux endomorphismes normaux.

> Remark 3. Note that this result is not specific to normal endomorphisms.

LEMME 2. Soit \( u \in \mathcal{L}\left( E\right) \) un endomorphisme normal. Si \( {E}_{\lambda } \) est un sous-espace propre de \( u \) (associé à une valeur propre \( \lambda \) ), alors \( {E}_{\lambda }^{ \bot } \) est stable par \( u \) .

> LEMMA 2. Let \( u \in \mathcal{L}\left( E\right) \) be a normal endomorphism. If \( {E}_{\lambda } \) is an eigenspace of \( u \) (associated with an eigenvalue \( \lambda \) ), then \( {E}_{\lambda }^{ \bot } \) is invariant under \( u \) .

Démonstration. Comme \( u \) et \( {u}^{ * } \) commutent, \( {E}_{\lambda } \) est stable par \( {u}^{ * } \) (voir la proposition 7 page 175), donc d’après le lemme \( 1,{E}_{\lambda }^{ \bot } \) est stable par \( {\left( {u}^{ * }\right) }^{ * } = u \) .

> Proof. Since \( u \) and \( {u}^{ * } \) commute, \( {E}_{\lambda } \) is invariant under \( {u}^{ * } \) (see proposition 7 on page 175), so according to the lemma \( 1,{E}_{\lambda }^{ \bot } \) is invariant under \( {\left( {u}^{ * }\right) }^{ * } = u \) .

Nous pouvons maintenant énoncer et démontrer notre résultat principal.

> We can now state and prove our main result.

- THÉORÉME 3. Soit \( u \in  \mathcal{L}\left( E\right) \) . Les assertions (i),(ii) et (iii) sont équivalentes.

> - THEOREM 3. Let \( u \in  \mathcal{L}\left( E\right) \) . The assertions (i), (ii), and (iii) are equivalent.

(i) u est normal.

> (i) u is normal.

(ii) и se diagonalise dans une base orthonormale de E.

> (ii) u is diagonalizable in an orthonormal basis of E.

(iii) \( u \) et \( {u}^{ * } \) se diagonalisent dans une base orthonormale commune.

> (iii) \( u \) and \( {u}^{ * } \) are diagonalizable in a common orthonormal basis.

Démonstration. Nous montrerons (i) \( \Rightarrow \) (ii),(ii) \( \Rightarrow \) (iii) et (iii) \( \Rightarrow \) (i).

> Proof. We will show (i) \( \Rightarrow \) (ii), (ii) \( \Rightarrow \) (iii), and (iii) \( \Rightarrow \) (i).

- (i) \( \Rightarrow \) (ii). On procède par récurrence sur \( n = \dim E \) . Pour \( n = 1 \) , c’est évident. Sinon, supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Le corps de base de \( E \) est \( \mathbb{C} \) , donc \( u \) admet au moins une valeur propre \( \lambda \) . Soit \( {E}_{\lambda } \) le sous-espace propre correspondant. Le sous-espace \( F = {E}_{\lambda }^{ \bot  } \) est stable par \( u \) (lemme 2) et par \( {u}^{ * } \) (lemme 1). Comme \( {u}_{\mid F} \) et \( {\left( {u}_{\mid F}\right) }^{ * } = \; {\left( {u}^{ * }\right) }_{\mid F} \) commutent et que dim \( F \leq  n - 1 \) , il existe d’après l’hypothèse de récurrence une base orthonormale \( {B}_{1} \) de \( F \) qui diagonalise \( {u}_{\mid F} \) . Si maintenant \( {B}_{2} \) désigne une base orthonormale de \( {E}_{\lambda } \) , on voit que \( B = \left( {{B}_{1},{B}_{2}}\right) \) est une base orthonormale de \( E \) diagonalisant \( u \) .

> - (i) \( \Rightarrow \) (ii). We proceed by induction on \( n = \dim E \) . For \( n = 1 \) , it is obvious. Otherwise, assume the result is true up to rank \( n - 1 \) and show it for rank \( n \) . The base field of \( E \) is \( \mathbb{C} \) , so \( u \) admits at least one eigenvalue \( \lambda \) . Let \( {E}_{\lambda } \) be the corresponding eigenspace. The subspace \( F = {E}_{\lambda }^{ \bot  } \) is invariant under \( u \) (lemma 2) and under \( {u}^{ * } \) (lemma 1). Since \( {u}_{\mid F} \) and \( {\left( {u}_{\mid F}\right) }^{ * } = \; {\left( {u}^{ * }\right) }_{\mid F} \) commute and dim \( F \leq  n - 1 \) , there exists by the induction hypothesis an orthonormal basis \( {B}_{1} \) of \( F \) that diagonalizes \( {u}_{\mid F} \) . If \( {B}_{2} \) now denotes an orthonormal basis of \( {E}_{\lambda } \) , we see that \( B = \left( {{B}_{1},{B}_{2}}\right) \) is an orthonormal basis of \( E \) diagonalizing \( u \) .

- (ii) \( \Rightarrow \) (iii). Soit \( B \) une base orthonormale diagonalisant \( u, M \) la matrice de \( u \) dans \( B \) . La matrice de \( {u}^{ * } \) dans \( B \) est \( {M}^{ * } \) . La matrice \( M \) est diagonale donc \( {M}^{ * } \) est diagonale, ce qui entraîne que la base \( B \) diagonalise \( u \) et \( {u}^{ * } \) .

> - (ii) \( \Rightarrow \) (iii). Let \( B \) be an orthonormal basis diagonalizing \( u, M \) the matrix of \( u \) in \( B \) . The matrix of \( {u}^{ * } \) in \( B \) is \( {M}^{ * } \) . The matrix \( M \) is diagonal, so \( {M}^{ * } \) is diagonal, which implies that the basis \( B \) diagonalizes \( u \) and \( {u}^{ * } \) .

- (iii) \( \Rightarrow \) (i). Soit \( B \) une base orthonormale diagonalisant \( u \) et \( {u}^{ * } \) . Les matrice \( M = {\left\lbrack  u\right\rbrack  }_{B} \) et \( {M}^{ * } = {\left\lbrack  {u}^{ * }\right\rbrack  }_{B} \) étant diagonales, elles commutent, donc \( u \) et \( {u}^{ * } \) commutent.

> - (iii) \( \Rightarrow \) (i). Let \( B \) be an orthonormal basis diagonalizing \( u \) and \( {u}^{ * } \) . Since the matrices \( M = {\left\lbrack  u\right\rbrack  }_{B} \) and \( {M}^{ * } = {\left\lbrack  {u}^{ * }\right\rbrack  }_{B} \) are diagonal, they commute, therefore \( u \) and \( {u}^{ * } \) commute.

COROLLAIRE 2 (VERSION MATRICIELLE). Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice. Alors \( M \) est normale si et seulement s’il existe \( P \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) , P \) unitaire, telle que \( {P}^{ * }{MP} = {P}^{-1}{MP} \) est diagonale.

> COROLLARY 2 (MATRIX VERSION). Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a matrix. Then \( M \) is normal if and only if there exists a unitary matrix \( P \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) , P \) such that \( {P}^{ * }{MP} = {P}^{-1}{MP} \) is diagonal.

Démonstration. Notons \( B \) la base canonique de \( {\mathbb{C}}^{n} \) . On munit \( {\mathbb{C}}^{n} \) du produit scalaire hermitien usuel, et on désigne par \( u \) l’endomorphisme de \( {\mathbb{C}}^{n} \) tel que \( {\left\lbrack u\right\rbrack }_{B} = M \) .

> Proof. Let \( B \) denote the canonical basis of \( {\mathbb{C}}^{n} \) . We equip \( {\mathbb{C}}^{n} \) with the standard Hermitian inner product, and we denote by \( u \) the endomorphism of \( {\mathbb{C}}^{n} \) such that \( {\left\lbrack u\right\rbrack }_{B} = M \) .

On montre la condition nécessaire. Si \( M \) est normale, alors \( u \) est normal donc il existe une base \( {B}^{\prime } \) orthonormale qui diagonalise \( u \) . Si \( P \) désigne la matrice de passage de \( B \) à \( {B}^{\prime }, P \) est unitaire et \( {P}^{-1}{MP} \) est diagonale.

> We show the necessary condition. If \( M \) is normal, then \( u \) is normal, so there exists an orthonormal basis \( {B}^{\prime } \) that diagonalizes \( u \) . If \( P \) denotes the transition matrix from \( B \) to \( {B}^{\prime }, P \) , it is unitary and \( {P}^{-1}{MP} \) is diagonal.

La réciproque est immédiate, car si \( D = {P}^{ * }{MP}, D \) est diagonale, donc \( D \) et \( {D}^{ * } \) commutent, d'où

> The converse is immediate, because if \( D = {P}^{ * }{MP}, D \) is diagonal, then \( D \) and \( {D}^{ * } \) commute, hence

\[
\left( {{P}^{ * }{M}^{ * }P}\right) \left( {{P}^{ * }{MP}}\right)  = \left( {{P}^{ * }{MP}}\right) \left( {{P}^{ * }{M}^{ * }P}\right) \text{ donc }{P}^{ * }{M}^{ * }{MP} = {P}^{ * }M{M}^{ * }P,
\]

ce qui entraîne que \( M \) et \( {M}^{ * } \) commutent.

> which implies that \( M \) and \( {M}^{ * } \) commute.

Remarque 4. Attention, à la différence du cas autoadjoint, la matrice diagonale obtenue n'est pas forcément à coefficients réels.

> Remark 4. Note that, unlike the self-adjoint case, the resulting diagonal matrix does not necessarily have real coefficients.

Cas des matrices réelles. Lorsque \( M \) est une matrice normale à coefficients réels, il est intéressant d’avoir une réduction de \( M \) dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . C’est le but de ce qui suit. Nous commençons par un petit lemme.

> Case of real matrices. When \( M \) is a normal matrix with real coefficients, it is useful to have a reduction of \( M \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . This is the goal of what follows. We begin with a small lemma.

LEMME 3. Soit E un espace euclidien de dimension 2. Soit \( u \in \mathcal{L}\left( E\right) \) un endomorphisme normal n'admettant pas de valeurs propres réelles. Dans toute base B orthonormale de E, la matrice de u a la forme

> LEMMA 3. Let E be a 2-dimensional Euclidean space. Let \( u \in \mathcal{L}\left( E\right) \) be a normal endomorphism with no real eigenvalues. In any orthonormal basis B of E, the matrix of u has the form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} a &  - b \\  b & a \end{matrix}\right) ,\;\text{ avec }\;b \neq  0.
\]

Démonstration. Écrivons

> Proof. Let us write

\[
M = {\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} a & c \\  b & d \end{matrix}\right) .
\]

On a \( b \neq 0 \) puisque \( u \) est sans valeur propre réelle. Comme \( u \) est normal, \( {M}^{ * }M = M{M}^{ * } \) . Parmi les équations découlant de cette égalité, on trouve

> We have \( b \neq 0 \) since \( u \) has no real eigenvalues. As \( u \) is normal, \( {M}^{ * }M = M{M}^{ * } \) . Among the equations resulting from this equality, we find

\[
{a}^{2} + {c}^{2} = {a}^{2} + {b}^{2}\;\text{ et }\;{ab} + {cd} = {ac} + {bd}.
\]

(*)

> La première assertion de \( \left( *\right) \) entraîne \( b = c \) ou \( b = - c \) .

The first assertion of \( \left( *\right) \) implies \( b = c \) or \( b = - c \) .

> Si \( b = c \) , alors \( M \) est symétrique, ce qui est impossible puisque \( u \) est sans valeur propre réelle.

If \( b = c \) , then \( M \) is symmetric, which is impossible since \( u \) has no real eigenvalues.

> Donc \( b = - c \) . Maintenant, la deuxième assertion de \( \left( *\right) \) s’écrit \( 2\left( {a - d}\right) b = 0 \) , et comme \( b \neq 0 \) , on a \( a = d \) . Finalement, on a \( c = - b \) et \( d = a \) , on en déduit que la matrice de \( u \) dans la base \( B \) a bien la forme annoncée.

Thus \( b = - c \) . Now, the second assertion of \( \left( *\right) \) is written \( 2\left( {a - d}\right) b = 0 \) , and since \( b \neq 0 \) , we have \( a = d \) . Finally, we have \( c = - b \) and \( d = a \) , from which we deduce that the matrix of \( u \) in the basis \( B \) indeed has the announced form.

> THÉORÉME 4. Soit \( E \) un espace euclidien, et \( u \in \mathcal{L}\left( E\right) \) un endomorphisme normal. Alors il existe une base orthogonale \( B \) de \( E \) telle que

THEOREM 4. Let \( E \) be a Euclidean space, and \( u \in \mathcal{L}\left( E\right) \) a normal endomorphism. Then there exists an orthogonal basis \( B \) of \( E \) such that

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1} & & & & & \\   &  \ddots  & & & 0 & \\   & & {\lambda }_{r} & & & \\   & & & {\tau }_{1} & & \\   & 0 & & &  \ddots  & \\   & & & & & {\tau }_{r} \end{matrix}\right) ,
\]

(*)

> où pour tout \( i,{\lambda }_{i} \in \mathbb{R} \) et pour tout \( j,{\tau }_{j} = \left( \begin{matrix} {a}_{j} & - {b}_{j} \\ {b}_{j} & {a}_{j} \end{matrix}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) .

where for all \( i,{\lambda }_{i} \in \mathbb{R} \) and for all \( j,{\tau }_{j} = \left( \begin{matrix} {a}_{j} & - {b}_{j} \\ {b}_{j} & {a}_{j} \end{matrix}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) .

> Démonstration. On procède par récurrence sur \( n = \dim E \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Nous nous servirons des lemmes 1 et 2 qui restent vrais lorsque \( E \) est euclidien.

Proof. We proceed by induction on \( n = \dim E \) . For \( n = 1 \) , it is obvious. Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \) . We will use lemmas 1 and 2, which remain true when \( E \) is Euclidean.

> Si \( u \) admet au moins une valeur propre réelle \( \lambda \) , on pose \( {E}_{\lambda } = \operatorname{Ker}\left( {u - \lambda {\operatorname{Id}}_{E}}\right) \) . Le s.e.v \( F = {E}_{\lambda }^{ \bot } \) est stable par \( u \) (lemme 1) et par \( {u}^{ * } \) (lemme 2). Comme \( {u}_{\mid F} \) et \( {u}_{\mid F}^{ * } \) commutent et que \( \dim F \leq n - 1 \) , il existe d’après l’hypothèse de récurrence une base orthonormale \( {B}_{1} \) de \( F \) telle que \( {\left\lbrack {u}_{\mid F}\right\rbrack }_{{B}_{1}} \) a la forme (*). Si \( {B}_{2} \) désigne une base orthonormale de \( {E}_{\lambda } \) , on voit alors que \( B = \left( {{B}_{1},{B}_{2}}\right) \) est une base orthonormale de \( E \) dans laquelle \( {\left\lbrack u\right\rbrack }_{B} \) a la forme \( \left( *\right) \) .

If \( u \) admits at least one real eigenvalue \( \lambda \) , we set \( {E}_{\lambda } = \operatorname{Ker}\left( {u - \lambda {\operatorname{Id}}_{E}}\right) \) . The subspace \( F = {E}_{\lambda }^{ \bot } \) is stable under \( u \) (lemma 1) and under \( {u}^{ * } \) (lemma 2). Since \( {u}_{\mid F} \) and \( {u}_{\mid F}^{ * } \) commute and \( \dim F \leq n - 1 \) , there exists, by the induction hypothesis, an orthonormal basis \( {B}_{1} \) of \( F \) such that \( {\left\lbrack {u}_{\mid F}\right\rbrack }_{{B}_{1}} \) has the form (*). If \( {B}_{2} \) denotes an orthonormal basis of \( {E}_{\lambda } \) , we then see that \( B = \left( {{B}_{1},{B}_{2}}\right) \) is an orthonormal basis of \( E \) in which \( {\left\lbrack u\right\rbrack }_{B} \) has the form \( \left( *\right) \) .

> Sinon \( u \) est sans valeur propre réelle. Soit \( Q = {X}^{2} - {2\alpha X} + \beta \) un facteur irréductible dans \( \mathbb{R}\left\lbrack X\right\rbrack \) (on a donc \( {\alpha }^{2} - \beta < 0 \) ) du polynôme minimal \( {\pi }_{u} \) de \( u \) , et \( N = \operatorname{Ker}Q\left( u\right) \) .

Otherwise \( u \) has no real eigenvalue. Let \( Q = {X}^{2} - {2\alpha X} + \beta \) be an irreducible factor in \( \mathbb{R}\left\lbrack X\right\rbrack \) (we thus have \( {\alpha }^{2} - \beta < 0 \) ) of the minimal polynomial \( {\pi }_{u} \) of \( u \) , and \( N = \operatorname{Ker}Q\left( u\right) \) .

> On a \( N \neq \{ 0\} \) . En effet, si \( N = 0 \) alors \( Q\left( u\right) \) est inversible. En notant \( R \) le polynôme tel que \( {\pi }_{u} = {QR} \) , on a donc \( Q\left( u\right) R\left( u\right) = 0 \) donc \( R\left( u\right) = 0 \) par inversibilité de \( Q\left( u\right) \) , ce qui est absurde compte tenu de la définition du polynôme minimal de \( u \) .

We have \( N \neq \{ 0\} \) . Indeed, if \( N = 0 \) then \( Q\left( u\right) \) is invertible. By denoting \( R \) the polynomial such that \( {\pi }_{u} = {QR} \) , we thus have \( Q\left( u\right) R\left( u\right) = 0 \) , therefore \( R\left( u\right) = 0 \) by the invertibility of \( Q\left( u\right) \) , which is absurd given the definition of the minimal polynomial of \( u \) .

> Il est clair que \( N \) est stable par \( u \) . Le s.e.v \( N \) est également stable par \( {u}^{ * } \) car la commu-tativité de \( u \) et \( {u}^{ * } \) entraîne \( {u}^{ * }Q\left( u\right) = Q\left( u\right) {u}^{ * } \) . Posons \( v = {u}_{\mid N} \) . On a \( {v}^{ * } = {u}_{\mid N}^{ * } \) , de sorte que l’endomorphisme \( {v}^{ * }v = {\left( {u}^{ * }u\right) }_{\mid N} \) est symétrique et admet donc une valeur propre \( \mu \in \mathbb{R} \) . Soit \( x \in N, x \neq 0 \) , tel que \( {v}^{ * }v\left( x\right) = {\mu x} \) . Posons \( F = \operatorname{Vect}\left( {x, u\left( x\right) }\right) \) . Comme \( u \) n’admet pas de valeur propre réelle, \( x \) et \( u\left( x\right) \) forment une famille libre donc dim \( F = 2 \) . Le s.e.v \( F \) est stable par \( u \) puisque comme \( x \in N \) , on a \( {u}^{2}\left( x\right) = {2\alpha u}\left( x\right) - {\beta x}\;\left( {* * }\right) \) .

It is clear that \( N \) is stable under \( u \) . The subspace \( N \) is also stable under \( {u}^{ * } \) because the commutativity of \( u \) and \( {u}^{ * } \) implies \( {u}^{ * }Q\left( u\right) = Q\left( u\right) {u}^{ * } \) . Let \( v = {u}_{\mid N} \) . We have \( {v}^{ * } = {u}_{\mid N}^{ * } \) , so the endomorphism \( {v}^{ * }v = {\left( {u}^{ * }u\right) }_{\mid N} \) is symmetric and therefore admits an eigenvalue \( \mu \in \mathbb{R} \) . Let \( x \in N, x \neq 0 \) , such that \( {v}^{ * }v\left( x\right) = {\mu x} \) . Let \( F = \operatorname{Vect}\left( {x, u\left( x\right) }\right) \) . Since \( u \) does not admit a real eigenvalue, \( x \) and \( u\left( x\right) \) form a linearly independent family, so dim \( F = 2 \) . The subspace \( F \) is stable under \( u \) since, as \( x \in N \) , we have \( {u}^{2}\left( x\right) = {2\alpha u}\left( x\right) - {\beta x}\;\left( {* * }\right) \) .

> Nous allons montrer que \( F \) est également stable par \( {u}^{ * } \) . Remarquons tout d’abord que l’égalité \( \left( {* * }\right) \) entraîne \( F = \operatorname{Vect}\left( {u\left( x\right) ,{u}^{2}\left( x\right) }\right) \) (ceci car \( \beta \neq 0, Q \) étant irréductible sur \( \mathbb{R}\left\lbrack X\right\rbrack \) ). On écrit maintenant

We will show that \( F \) is also stable under \( {u}^{ * } \) . First, note that the equality \( \left( {* * }\right) \) implies \( F = \operatorname{Vect}\left( {u\left( x\right) ,{u}^{2}\left( x\right) }\right) \) (this is because \( \beta \neq 0, Q \) is irreducible over \( \mathbb{R}\left\lbrack X\right\rbrack \) ). We now write

\[
{u}^{ * }\left\lbrack  {u\left( x\right) }\right\rbrack   = {v}^{ * }v\left( x\right)  = {\mu x} \in  F
\]

et comme \( u \) et \( {u}^{ * } \) commutent,

> and since \( u \) and \( {u}^{ * } \) commute,

\[
{u}^{ * }\left\lbrack  {{u}^{2}\left( x\right) }\right\rbrack   = u \circ  {u}^{ * }\left\lbrack  {u\left( x\right) }\right\rbrack   = u\left( {\mu x}\right)  = {\mu u}\left( x\right)  \in  F,
\]

ce qui achève de montrer que \( F \) est stable par \( {u}^{ * } \) .

> which completes the proof that \( F \) is stable under \( {u}^{ * } \) .

Comme \( {\left( {u}_{\mid F}\right) }^{ * } = {\left( {u}^{ * }\right) }_{\mid F},{u}_{\mid F} \) est un endomorphisme normal. D’après le lemme 3, dans une base orthonormée \( {B}_{2} \) de \( F \) , la matrice de \( {u}_{\mid F} \) est de la forme

> Since \( {\left( {u}_{\mid F}\right) }^{ * } = {\left( {u}^{ * }\right) }_{\mid F},{u}_{\mid F} \) is a normal endomorphism. According to Lemma 3, in an orthonormal basis \( {B}_{2} \) of \( F \) , the matrix of \( {u}_{\mid F} \) is of the form

\[
\tau  = \left( \begin{matrix} a &  - b \\  b & a \end{matrix}\right)
\]

Maintenant, on a vu que \( F \) est stable par \( {u}^{ * } \) , donc \( {F}^{ \bot } \) est stable par \( {u}^{* * } = u \) d’après le lemme 1 . Le même lemme montre que, \( F \) étant stable par \( u,{F}^{ \bot } \) est stable par \( {u}^{ * } \) . Donc \( {\left( {u}_{\mid {F}^{ \bot }}\right) }^{ * } = {\left( {u}^{ * }\right) }_{\mid {F}^{ \bot }} \) , ce qui prouve que \( {u}_{\mid {F}^{ \bot }} \) est normal. Comme dim \( {F}^{ \bot } = n - 2 < n \) , l’hypothèse de récurrence assure l’existence d’une base \( {B}_{1} \) orthonormale de \( {F}^{ \bot } \) dans laquelle la matrice de \( u \) a la forme \( \left( *\right) \) .

> Now, we have seen that \( F \) is stable under \( {u}^{ * } \) , so \( {F}^{ \bot } \) is stable under \( {u}^{* * } = u \) according to Lemma 1. The same lemma shows that, since \( F \) is stable under \( u,{F}^{ \bot } \) , it is stable under \( {u}^{ * } \) . Thus \( {\left( {u}_{\mid {F}^{ \bot }}\right) }^{ * } = {\left( {u}^{ * }\right) }_{\mid {F}^{ \bot }} \) , which proves that \( {u}_{\mid {F}^{ \bot }} \) is normal. Since dim \( {F}^{ \bot } = n - 2 < n \) , the induction hypothesis ensures the existence of an orthonormal basis \( {B}_{1} \) of \( {F}^{ \bot } \) in which the matrix of \( u \) has the form \( \left( *\right) \) .

La base \( B = \left( {{B}_{1},{B}_{2}}\right) \) est alors une base orthonormale dans laquelle la matrice de \( u \) a la forme \( \left( *\right) \) .

> The basis \( B = \left( {{B}_{1},{B}_{2}}\right) \) is then an orthonormal basis in which the matrix of \( u \) has the form \( \left( *\right) \) .

Remarque 5. En termes de matrice, ce théorème s’exprime comme suit. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice normale. Alors il existe une matrice orthogonale \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que \( {P}^{-1}{MP} \) ait la forme \( \left( *\right) \) .

> Remark 5. In matrix terms, this theorem is expressed as follows. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a normal matrix. Then there exists an orthogonal matrix \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that \( {P}^{-1}{MP} \) has the form \( \left( *\right) \) .

Réduction des matrices antisymétriques. Les matrices réelles antisymétriques sont normales. Il est donc possible de leur appliquer les résultats précédents. Plus précisément, nous avons le théorème suivant.

> Reduction of skew-symmetric matrices. Real skew-symmetric matrices are normal. It is therefore possible to apply the previous results to them. More precisely, we have the following theorem.

THÉORÉME 5. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice vérifiant \( {M}^{ * } + M = 0 \) . Alors il existe une matrice unitaire \( U \) telle que \( {U}^{-1}{MU} = {U}^{ * }{MU} = D \) soit diagonale, et les coefficients de D sont imaginaires purs.

> THEOREM 5. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a matrix satisfying \( {M}^{ * } + M = 0 \) . Then there exists a unitary matrix \( U \) such that \( {U}^{-1}{MU} = {U}^{ * }{MU} = D \) is diagonal, and the coefficients of D are purely imaginary.

Démonstration. Comme \( {M}^{ * } = - M, M \) est une matrice normale, et d’après le corollaire du théorème 3, il existe une matrice unitaire \( U \) telle que

> Proof. Since \( {M}^{ * } = - M, M \) is a normal matrix, and according to the corollary of theorem 3, there exists a unitary matrix \( U \) such that

\[
D = {U}^{-1}{MU} = {U}^{ * }{MU} = \left( \begin{matrix} {\lambda }_{1} & & 0 \\   &  \ddots  & \\  0 & & {\lambda }_{n} \end{matrix}\right) ,
\]

avec pour tout \( i,{\lambda }_{i} \in \mathbb{C} \) . Comme

> with for all \( i,{\lambda }_{i} \in \mathbb{C} \) . Since

\[
{D}^{ * } + D = \left( \begin{matrix} {\lambda }_{1} + \overline{{\lambda }_{1}} & & 0 \\   &  \ddots  & \\  0 & & {\lambda }_{n} + \overline{{\lambda }_{n}} \end{matrix}\right)  = {U}^{ * }{M}^{ * }U + {U}^{ * }{MU} = {U}^{ * }\left( {{M}^{ * } + M}\right) U = 0,
\]

on a \( {\lambda }_{i} + \overline{{\lambda }_{i}} = 0 \) pour tout \( i \) , ce qui prouve que les \( {\lambda }_{i} \) sont imaginaires purs, d’où le résultat.

> we have \( {\lambda }_{i} + \overline{{\lambda }_{i}} = 0 \) for all \( i \) , which proves that the \( {\lambda }_{i} \) are purely imaginary, hence the result.

Remarque 6. Ce résultat est vrai en particulier pour les matrices réelles antisymétriques. Si on veut rester dans \( \mathbb{R} \) , on utilise le résultat qui suit.

> Remark 6. This result is true in particular for real skew-symmetric matrices. If we wish to remain in \( \mathbb{R} \) , we use the following result.

THÉORÉME 6 (Version réelle). Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice antisymétrique. Alors il existe une matrice orthogonale \( P \) telle que

> THEOREM 6 (Real version). Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a skew-symmetric matrix. Then there exists an orthogonal matrix \( P \) such that

\[
{P}^{-1}{MP} = {P}^{ * }{MP} = \left( \begin{matrix} 0 & & & & & \\   &  \ddots  & & & 0 & \\   & & 0 & & & \\   & & & {\tau }_{1} & & \\  0 & & & &  \ddots  & \\   & & & & & {\tau }_{r} \end{matrix}\right)
\]

où les \( {\tau }_{i} \) sont des matrices de \( {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) de la forme \( \left( \begin{matrix} 0 & b \\ - b & 0 \end{matrix}\right) \) , où \( b \in \mathbb{R} \) .

> where the \( {\tau }_{i} \) are matrices of \( {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) of the form \( \left( \begin{matrix} 0 & b \\ - b & 0 \end{matrix}\right) \) , where \( b \in \mathbb{R} \) .

Démonstration. Comme \( {M}^{ * } = - M, M \) est une matrice normale. On peut donc utiliser le théo-rème 4 qui assure l'existence d'une matrice orthogonale \( P \) telle que

> Proof. Since \( {M}^{ * } = - M, M \) is a normal matrix. We can therefore use theorem 4, which ensures the existence of an orthogonal matrix \( P \) such that

\[
{P}^{-1}{MP} = {P}^{ * }{MP} = \left( \begin{matrix} {\lambda }_{1} & & & & & \\   &  \ddots  & & & 0 & \\   & & {\lambda }_{r} & & & \\   & & & {\tau }_{1} & & \\   & 0 & & &  \ddots  & \\   & & & & & {\tau }_{s} \end{matrix}\right) ,
\]

où les \( {\lambda }_{i} \in \mathbb{R} \) et où \( {\tau }_{j} = \left( \begin{matrix} {a}_{j} & {b}_{j} \\ - {b}_{j} & {a}_{j} \end{matrix}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . Comme \( {D}^{ * } = {P}^{ * }{M}^{ * }P = - {P}^{ * }{MP} = - D \) , \( D \) est antisymétrique. Ses termes diagonaux sont donc nuls, c’est-à-dire \( {\lambda }_{i} = 0 \) pour tout \( i \) et \( {a}_{j} = 0 \) pour tout \( j \) , d’où le résultat.

> where the \( {\lambda }_{i} \in \mathbb{R} \) and where \( {\tau }_{j} = \left( \begin{matrix} {a}_{j} & {b}_{j} \\ - {b}_{j} & {a}_{j} \end{matrix}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . Since \( {D}^{ * } = {P}^{ * }{M}^{ * }P = - {P}^{ * }{MP} = - D \) , \( D \) is skew-symmetric. Its diagonal terms are therefore zero, that is to say \( {\lambda }_{i} = 0 \) for all \( i \) and \( {a}_{j} = 0 \) for all \( j \) , hence the result.

Remarque 7. Lorsqu’on applique le théorème pour \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) antisymétrique avec \( n \) impair, on voit qu’il doit y avoir au moins un zéro sur la diagonale de \( {P}^{-1}{MP} \) . La matrice \( M \) n’est donc pas inversible. On peut retrouver directement ce résultat en écrivant que \( \det M = \det \left( {{}^{\mathrm{t}}M}\right) = \det \left( {-M}\right) = {\left( -1\right) }^{n}\det \left( M\right) = - \det M \) , ce qui entraîne det \( M = 0 \) .

> Remark 7. When applying the theorem for \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) antisymmetric with \( n \) odd, we see that there must be at least one zero on the diagonal of \( {P}^{-1}{MP} \). The matrix \( M \) is therefore not invertible. This result can be recovered directly by writing that \( \det M = \det \left( {{}^{\mathrm{t}}M}\right) = \det \left( {-M}\right) = {\left( -1\right) }^{n}\det \left( M\right) = - \det M \), which implies det \( M = 0 \).

Les endomorphismes unitaires et les isométries sont aussi des endomorphismes nor-maux. En appliquant les théorèmes 3 et 4, on retrouve facilement les réductions obtenues dans la partie 3.1.

> Unitary endomorphisms and isometries are also normal endomorphisms. By applying theorems 3 and 4, we easily recover the reductions obtained in part 3.1.

Il est possible d'obtenir la réduction des matrices antisymétriques par des moyens plus directs, en utilisant des méthodes du même type que celles de la partie 3.1 (cela constitue un excellent exercice).

> It is possible to obtain the reduction of antisymmetric matrices by more direct means, using methods of the same type as those in part 3.1 (this constitutes an excellent exercise).
