#### 2.4. Adjoint endomorphisms

*Français : 2.4. Endomorphismes adjoints*

DéFINITION 5 (ADJOINT). Soit \( E \) un espace euclidien (resp. hermitien) et \( f \) et \( g \in \mathcal{L}\left( E\right) \) . Les endomorphismes \( f \) et \( g \) sont dits adjoints si

> DEFINITION 5 (ADJOINT). Let \( E \) be a Euclidean (resp. Hermitian) space and \( f \) and \( g \in \mathcal{L}\left( E\right) \) . The endomorphisms \( f \) and \( g \) are said to be adjoint if

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;f\left( x\right)  \cdot  y = x \cdot  g\left( y\right) .
\]

(*)

> L’endomorphisme \( f \) étant donné, il existe au plus un endomorphisme \( g \) vérifiant \( \left( *\right) \) . Lorsqu’il existe, on l’appelle adjoint de \( f \) et on le note \( {f}^{ * } \) . Lorsque \( f = {f}^{ * }, f \) est dit autoadjoint.

Given the endomorphism \( f \), there exists at most one endomorphism \( g \) satisfying \( \left( *\right) \) . When it exists, it is called the adjoint of \( f \) and is denoted by \( {f}^{ * } \) . When \( f = {f}^{ * }, f \) it is said to be self-adjoint.

> Remarque 10. - L'adjoint \( {f}^{ * } \) d’un endomorphisme \( f \) n’existe pas toujours (nous ver-rons cependant qu'en dimension finie, et plus généralement dans un espace hilber-tien lorsque \( f \) est continu, l’adjoint de \( f \) existe).

Remark 10. - The adjoint \( {f}^{ * } \) of an endomorphism \( f \) does not always exist (we will see, however, that in finite dimension, and more generally in a Hilbert space when \( f \) is continuous, the adjoint of \( f \) exists).

> - Lorsque \( {f}^{ * } \) existe, \( {\left( {f}^{ * }\right) }^{ * } = {f}^{* * } \) existe et on a \( {f}^{* * } = f \) .

- When \( {f}^{ * } \) exists, \( {\left( {f}^{ * }\right) }^{ * } = {f}^{* * } \) exists and we have \( {f}^{* * } = f \) .

> Étude en dimension finie. Notation. Nous utiliserons la notation introduite dans la partie 1.2 : si \( M \) désigne une matrice complexe, on note \( {M}^{ * } = {}^{\mathrm{t}}\bar{M} \) sa transconjuguée. Ainsi, lorsque \( M \) est une matrice réelle, \( {M}^{ * } \) désignera simplement la transposée de \( M \) .

Study in finite dimension. Notation. We will use the notation introduced in part 1.2: if \( M \) denotes a complex matrix, we denote by \( {M}^{ * } = {}^{\mathrm{t}}\bar{M} \) its conjugate transpose. Thus, when \( M \) is a real matrix, \( {M}^{ * } \) will simply denote the transpose of \( M \) .

> Soit \( E \) un espace euclidien ou hermitien, \( B \) une base orthonormée de \( E \) . Soit \( f \in \mathcal{L}\left( E\right) \) , \( M \) la matrice de \( f \) dans la base \( B : M = {\left\lbrack f\right\rbrack }_{B} \) . On cherche un endomorphisme \( g \) qui soit l’adjoint de \( f \) . En notant \( N = {\left\lbrack g\right\rbrack }_{B} \) , on voit que \( \left( *\right) \) est vérifiée si et seulement si

Let \( E \) be a Euclidean or Hermitian space, \( B \) an orthonormal basis of \( E \). Let \( f \in \mathcal{L}\left( E\right) \), \( M \) be the matrix of \( f \) in the basis \( B : M = {\left\lbrack f\right\rbrack }_{B} \). We seek an endomorphism \( g \) that is the adjoint of \( f \). By denoting \( N = {\left\lbrack g\right\rbrack }_{B} \), we see that \( \left( *\right) \) is satisfied if and only if

> pour tous vecteurs \( X, Y,\;{\left( MX\right) }^{ * }Y = {X}^{ * }\left( {NY}\right) \) ou encore \( {X}^{ * }{M}^{ * }Y = {X}^{ * }{NY} \) .

for all vectors \( X, Y,\;{\left( MX\right) }^{ * }Y = {X}^{ * }\left( {NY}\right) \) or equivalently \( {X}^{ * }{M}^{ * }Y = {X}^{ * }{NY} \) .

> L’endomorphisme \( g \) est donc l’adjoint de \( f \) si et seulement sa matrice \( N \) dans la base \( B \) vérifie \( N = {M}^{ * } \) . En résumé, pour tout \( f \in \mathcal{L}\left( E\right) ,{f}^{ * } \) existe et \( {\left\lbrack {f}^{ * }\right\rbrack }_{B} = {\left\lbrack f\right\rbrack }_{B}^{ * } \) .

The endomorphism \( g \) is therefore the adjoint of \( f \) if and only if its matrix \( N \) in the basis \( B \) satisfies \( N = {M}^{ * } \) . In summary, for every \( f \in \mathcal{L}\left( E\right) ,{f}^{ * } \) exists and \( {\left\lbrack {f}^{ * }\right\rbrack }_{B} = {\left\lbrack f\right\rbrack }_{B}^{ * } \) .

> Remarque 11. - Attention, \( {\left\lbrack {f}^{ * }\right\rbrack }_{B} = {\left\lbrack f\right\rbrack }_{B}^{ * } \) seulement si la base \( B \) est orthonormée.

Remark 11. - Caution, \( {\left\lbrack {f}^{ * }\right\rbrack }_{B} = {\left\lbrack f\right\rbrack }_{B}^{ * } \) only if the basis \( B \) is orthonormal.

> - Si \( E \) est euclidien, un endomorphisme \( f \in  \mathcal{L}\left( E\right) \) est autoadjoint (on dit encore sy-métrique) si et seulement si la matrice de \( f \) dans une base orthonormée quelconque de \( E \) est symétrique.

- If \( E \) is Euclidean, an endomorphism \( f \in  \mathcal{L}\left( E\right) \) is self-adjoint (also called symmetric) if and only if the matrix of \( f \) in any orthonormal basis of \( E \) is symmetric.

> - Si \( E \) est hermitien, \( f \) est autoadjoint si et seulement si sa matrice \( M \) dans une base orthonormée de \( E \) est hermitienne (i.e si elle vérifie \( {}^{\mathrm{t}}\bar{M} = M \) ).

- If \( E \) is Hermitian, \( f \) is self-adjoint if and only if its matrix \( M \) in an orthonormal basis of \( E \) is Hermitian (i.e., if it satisfies \( {}^{\mathrm{t}}\bar{M} = M \) ).

> Réduction des endomorphismes autoadjoints. Nous aurons besoin de la proposition suivante.

Reduction of self-adjoint endomorphisms. We will need the following proposition.

> Proposition 7. Soit \( E \) un espace euclidien ou hermitien, et \( f \in \mathcal{L}\left( E\right) \) un endomorphisme autoadjoint. Si \( F \) est un s.e.v de \( E \) stable par \( f \) , alors \( {F}^{ \bot } \) est stable par \( f \) .

Proposition 7. Let \( E \) be a Euclidean or Hermitian space, and \( f \in \mathcal{L}\left( E\right) \) a self-adjoint endomorphism. If \( F \) is a subspace of \( E \) stable under \( f \), then \( {F}^{ \bot } \) is stable under \( f \).

> Démonstration. Il suffit d'écrire que

Proof. It suffices to write that

\[
\forall x \in  F,\forall y \in  {F}^{ \bot  },\;x \cdot  f\left( y\right)  = f\left( x\right)  \cdot  y = 0.
\]

\( \rightarrow \) THÉORÉME 3. Soit E un espace euclidien (resp. hermitien) et \( f \in \mathcal{L}\left( E\right) \) un endomor-phisme autoadjoint. Alors il existe une base orthonormée de vecteurs propres pour \( f \) , et de plus ses valeurs propres sont réelles.

> \( \rightarrow \) THEOREM 3. Let E be a Euclidean (resp. Hermitian) space and \( f \in \mathcal{L}\left( E\right) \) a self-adjoint endomorphism. Then there exists an orthonormal basis of eigenvectors for \( f \), and furthermore its eigenvalues are real.

Démonstration. On procède par récurrence sur la dimension \( n \) de \( E \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . On considère l’application \( \Phi : E \rightarrow \mathbb{R}\;x \mapsto x \cdot f\left( x\right) \) . C’est une forme quadratique (resp. hermitienne), de forme polaire \( \varphi \left( {x, y}\right) = x \cdot f\left( y\right) \) . Comme on est en dimension finie, la sphère unité \( S = \{ x \in E,\parallel x\parallel = 1\} \) de \( E \) est compacte, et \( \Phi \) étant continue (toujours parce que l’on est en dimension finie), il existe \( {x}_{0} \in S \) tel que \( \Phi \left( {x}_{0}\right) = \mathop{\sup }\limits_{{x \in S}}\Phi \left( x\right) = \lambda \) .

> Proof. We proceed by induction on the dimension \( n \) of \( E \). For \( n = 1 \), it is obvious. Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \). Consider the map \( \Phi : E \rightarrow \mathbb{R}\;x \mapsto x \cdot f\left( x\right) \). It is a quadratic (resp. Hermitian) form, with polar form \( \varphi \left( {x, y}\right) = x \cdot f\left( y\right) \). Since we are in finite dimension, the unit sphere \( S = \{ x \in E,\parallel x\parallel = 1\} \) of \( E \) is compact, and \( \Phi \) being continuous (still because we are in finite dimension), there exists \( {x}_{0} \in S \) such that \( \Phi \left( {x}_{0}\right) = \mathop{\sup }\limits_{{x \in S}}\Phi \left( x\right) = \lambda \).

Ceci étant, on considère la forme quadratique (resp. hermitienne) définie par \( {\Phi }_{1}\left( x\right) = \lambda \parallel x{\parallel }^{2} - \; \Phi \left( x\right) \) . La forme \( {\Phi }_{1} \) est positive par construction de \( \lambda \) . Or \( {\Phi }_{1}\left( {x}_{0}\right) = 0 \) , i.e \( {\Phi }_{1} \) n’est pas définie, et donc \( {\Phi }_{1} \) est dégénérée (rappelons qu’une forme positive est définie si et seulement si elle est non dégénérée, voir la conséquence de l’inégalité de Schwarz, partie 1.3). La forme polaire de \( {\Phi }_{1} \) étant \( {\varphi }_{1}\left( {x, y}\right) = x \cdot g\left( y\right) \) avec \( g = \lambda {\operatorname{Id}}_{E} - f \) , la dégénérescence de \( {\Phi }_{1} \) entraîne l’existence de \( x \neq 0 \) tel que pour tout \( y \in E,{\varphi }_{1}\left( {x, y}\right) = 0 = x \cdot g\left( y\right) \) . L’application \( g \) n’est donc pas surjective \( (x \) n’est pas atteint), donc non injective ( \( g \) est un endomorphisme en dimension finie), ce qui entraîne l’existence d’un vecteur normé \( {e}_{1} \) tel que \( g\left( {e}_{1}\right) = 0 = \lambda {e}_{1} - f\left( {e}_{1}\right) \) . Autrement dit, \( \lambda \in \mathbb{R} \) est valeur propre de \( f \) associée au vecteur propre \( {e}_{1} \) . Posons \( H = {\left( \operatorname{Vect}{e}_{1}\right) }^{ \bot } \) . D’après la proposition précédente, \( H \) est stable par \( f \) . La restriction de \( f \) à \( H \) étant autoadjointe, l’hypothèse de récurrence assure l’existence d’une base orthonormée \( \left( {{e}_{2},\ldots ,{e}_{n}}\right) \) de \( H \) qui diagonalise \( {f}_{\mid H} \) (à valeurs propres réelles). La base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est alors une base orthonormée qui diagonalise \( f \) , et les valeurs propres de \( f \) sont toutes réelles.

> Given this, consider the quadratic (resp. Hermitian) form defined by \( {\Phi }_{1}\left( x\right) = \lambda \parallel x{\parallel }^{2} - \; \Phi \left( x\right) \). The form \( {\Phi }_{1} \) is positive by construction of \( \lambda \). However, \( {\Phi }_{1}\left( {x}_{0}\right) = 0 \), i.e., \( {\Phi }_{1} \) is not definite, and therefore \( {\Phi }_{1} \) is degenerate (recall that a positive form is definite if and only if it is non-degenerate, see the consequence of the Schwarz inequality, part 1.3). Since the polar form of \( {\Phi }_{1} \) is \( {\varphi }_{1}\left( {x, y}\right) = x \cdot g\left( y\right) \) with \( g = \lambda {\operatorname{Id}}_{E} - f \), the degeneracy of \( {\Phi }_{1} \) implies the existence of \( x \neq 0 \) such that for all \( y \in E,{\varphi }_{1}\left( {x, y}\right) = 0 = x \cdot g\left( y\right) \). The map \( g \) is therefore not surjective (\( (x \) is not reached), and thus not injective (\( g \) is an endomorphism in finite dimension), which implies the existence of a normalized vector \( {e}_{1} \) such that \( g\left( {e}_{1}\right) = 0 = \lambda {e}_{1} - f\left( {e}_{1}\right) \). In other words, \( \lambda \in \mathbb{R} \) is an eigenvalue of \( f \) associated with the eigenvector \( {e}_{1} \). Let \( H = {\left( \operatorname{Vect}{e}_{1}\right) }^{ \bot } \). According to the previous proposition, \( H \) is stable under \( f \). Since the restriction of \( f \) to \( H \) is self-adjoint, the induction hypothesis ensures the existence of an orthonormal basis \( \left( {{e}_{2},\ldots ,{e}_{n}}\right) \) of \( H \) that diagonalizes \( {f}_{\mid H} \) (with real eigenvalues). The basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is then an orthonormal basis that diagonalizes \( f \), and the eigenvalues of \( f \) are all real.

La version matricielle de ce théorème est la suivante.

> The matrix version of this theorem is as follows.

- Corollaire 1. Soit \( M \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (resp. \( M \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) ) une matrice symétrique (resp. hermitienne). Alors il existe une matrice \( C \) orthogonale (resp. unitaire) telle que

> - Corollary 1. Let \( M \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (resp. \( M \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) ) be a symmetric (resp. Hermitian) matrix. Then there exists an orthogonal (resp. unitary) matrix \( C \) such that

\[
{C}^{-1}{MC} = {C}^{ * }{MC} = D,
\]

D étant une matrice diagonale réelle.

> D being a real diagonal matrix.

Démonstration. On note \( E = {\mathbb{R}}^{n} \) (resp. \( E = {\mathbb{C}}^{n} \) ). Munissons \( E \) du produit scalaire (resp. du produit scalaire hermitien) usuel :

> Proof. Let \( E = {\mathbb{R}}^{n} \) (resp. \( E = {\mathbb{C}}^{n} \) ) be given. Equip \( E \) with the standard inner product (resp. Hermitian inner product):

\[
\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \cdot  \left( {{y}_{1},\ldots ,{y}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{y}_{i}\;\text{ (resp. } = \mathop{\sum }\limits_{{i = 1}}^{n}\overline{{x}_{i}}{y}_{i}\text{ ). }
\]

Soit \( f \in \mathcal{L}\left( E\right) \) dont la matrice dans la base canonique \( B \) de \( E \) est \( M : {\left\lbrack f\right\rbrack }_{B} = M \) . Comme \( f \) est autoadjoint (car \( M \) est symétrique, resp. hermitienne), il existe d'après le théorème précédent une base \( {B}^{\prime } \) orthonormée de \( E \) telle que \( {\left\lbrack f\right\rbrack }_{{B}^{\prime }} = D \) soit diagonale réelle. Si on désigne par \( C \) la matrice de passage de la base \( B \) à la base \( {B}^{\prime }, C \) est une matrice orthogonale (resp. unitaire) et \( {C}^{-1}{MC} = {C}^{ * }{MC} = D. \)

> Let \( f \in \mathcal{L}\left( E\right) \) be such that its matrix in the canonical basis \( B \) of \( E \) is \( M : {\left\lbrack f\right\rbrack }_{B} = M \) . Since \( f \) is self-adjoint (because \( M \) is symmetric, resp. Hermitian), there exists by the previous theorem an orthonormal basis \( {B}^{\prime } \) of \( E \) such that \( {\left\lbrack f\right\rbrack }_{{B}^{\prime }} = D \) is real diagonal. If we denote by \( C \) the transition matrix from basis \( B \) to basis \( {B}^{\prime }, C \) , it is an orthogonal (resp. unitary) matrix and \( {C}^{-1}{MC} = {C}^{ * }{MC} = D. \)

Remarque 12. On rappelle qu'une matrice symétrique (resp. hermitienne) \( M \) est positive si la forme quadratique (resp. hermitienne) \( X \mapsto {X}^{ * }{MX} \) est positive. Elle est dite définie positive si cette forme quadratique est définie positive. Le corollaire montre que \( M \) est positive (resp. définie positive) si et seulement si toutes ses valeurs propres sont positives (resp. strictement positives).

> Remark 12. Recall that a symmetric (resp. Hermitian) matrix \( M \) is positive if the quadratic (resp. Hermitian) form \( X \mapsto {X}^{ * }{MX} \) is positive. It is said to be positive definite if this quadratic form is positive definite. The corollary shows that \( M \) is positive (resp. positive definite) if and only if all its eigenvalues are positive (resp. strictly positive).

COROLLAIRE 2. Soit \( \Phi \) une forme quadratique (resp. hermitienne) sur un espace euclidien (resp. hermitien) E. Alors il existe une base orthonormée de E dans laquelle la matrice de \( \Phi \) est diagonale réelle.

> COROLLARY 2. Let \( \Phi \) be a quadratic (resp. Hermitian) form on a Euclidean (resp. Hermitian) space E. Then there exists an orthonormal basis of E in which the matrix of \( \Phi \) is real diagonal.

Démonstration. Soit \( B \) une base orthonormée de \( E \) et soit \( M \) la matrice de \( \Phi \) dans la base \( B \) . La matrice \( M \) est symétrique (resp. hermitienne), et d’après le corollaire précédent, il existe une matrice \( C \) orthogonale (resp. unitaire) telle que \( {C}^{ * }{MC} = D \) est diagonale réelle. La matrice \( C \) défini un changement de base orthogonal qui fait passer de la base \( B \) à une base orthonormée \( {B}^{\prime } \) , et la matrice de \( \Phi \) dans la base \( {B}^{\prime } \) est \( D \) , d’où le résultat.

> Proof. Let \( B \) be an orthonormal basis of \( E \) and let \( M \) be the matrix of \( \Phi \) in the basis \( B \) . The matrix \( M \) is symmetric (resp. Hermitian), and according to the previous corollary, there exists an orthogonal (resp. unitary) matrix \( C \) such that \( {C}^{ * }{MC} = D \) is real diagonal. The matrix \( C \) defines an orthogonal change of basis that transforms the basis \( B \) into an orthonormal basis \( {B}^{\prime } \) , and the matrix of \( \Phi \) in the basis \( {B}^{\prime } \) is \( D \) , hence the result.

Remarque 13. Notez bien la différence entre ce dernier corollaire et le théorème 1 de la page 243. Ici, la base qui diagonalise \( \Phi \) a en plus la propriété d’être orthonormée pour le produit scalaire de l’espace \( E \) .

> Remark 13. Note well the difference between this last corollary and Theorem 1 on page 243. Here, the basis that diagonalizes \( \Phi \) also has the property of being orthonormal for the inner product of the space \( E \) .

- Corollaire 3. Soient \( M, N \) deux matrices symétriques (resp. hermitiennes), telles que la matrice \( M \) soit définie positive. Alors il existe une matrice \( C \) inversible telle que

> - Corollary 3. Let \( M, N \) be two symmetric (resp. Hermitian) matrices, such that the matrix \( M \) is positive definite. Then there exists an invertible matrix \( C \) such that

\[
{C}^{ * }{MC} = {I}_{n}\;\text{ et }\;{C}^{ * }{NC} = D,
\]

où D est une matrice diagonale réelle.

> where D is a real diagonal matrix.

Démonstration. Sur \( E = {\mathbb{R}}^{n} \) (resp. sur \( E = {\mathbb{C}}^{n} \) ), l’application \( \Phi : \left( {X, Y}\right) \mapsto {X}^{ * }{MY} \) défini un produit scalaire, et \( \Psi : X \mapsto {X}^{ * }{NX} \) une forme quadratique (resp. hermitienne). D’après le corollaire précédent, il existe une base \( B \) orthonormée (pour le produit scalaire \( \Phi \) ) telle que la matrice \( D \) de \( \Psi \) dans \( B \) soit diagonale réelle. En désignant par \( C \) la matrice de passage de la base canonique de \( E \) à la base \( B \) , on a \( {C}^{ * }{MC} = {I}_{n} \) et \( {C}^{ * }{NC} = D \) , d’où le résultat.

> Proof. On \( E = {\mathbb{R}}^{n} \) (resp. on \( E = {\mathbb{C}}^{n} \)), the map \( \Phi : \left( {X, Y}\right) \mapsto {X}^{ * }{MY} \) defines an inner product, and \( \Psi : X \mapsto {X}^{ * }{NX} \) a quadratic (resp. Hermitian) form. According to the previous corollary, there exists an orthonormal basis \( B \) (for the inner product \( \Phi \)) such that the matrix \( D \) of \( \Psi \) in \( B \) is real diagonal. By denoting \( C \) as the transition matrix from the canonical basis of \( E \) to the basis \( B \), we have \( {C}^{ * }{MC} = {I}_{n} \) and \( {C}^{ * }{NC} = D \), hence the result.

Remarque 14. Ce dernier corollaire rend parfois de précieux services. On peut le voir comme un résultat de pseudo-réduction simultanée. Prenez garde au fait que la matrice \( C \) n’est en général pas orthogonale (ou unitaire).

> Remark 14. This last corollary is sometimes very useful. It can be seen as a result of simultaneous pseudo-reduction. Be careful that the matrix \( C \) is generally not orthogonal (or unitary).
