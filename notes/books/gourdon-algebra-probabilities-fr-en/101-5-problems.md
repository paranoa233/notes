### 5. Problems

*Français : 5. Problèmes*

Problem 1. Soit un entier \( n \geq 2 \) et

> Problem 1. Let an integer \( n \geq 2 \) and

\[
M = \left( \begin{matrix} a & b & \cdots & b \\  b & a &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & b \\  b & \cdots & b & a \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\;\text{ avec }\;b \neq  0.
\]

a) Déterminer les valeurs propres de \( M \) et montrer que \( M \) est diagonalisable.

> a) Determine the eigenvalues of \( M \) and show that \( M \) is diagonalizable.

b) Lorsque \( M \) est inversible, calculer l’inverse de \( M \) .

> b) When \( M \) is invertible, calculate the inverse of \( M \) .

c) Pour tout \( p \in \mathbb{N} \) , calculer \( {M}^{p} \) .

> c) For all \( p \in \mathbb{N} \) , calculate \( {M}^{p} \) .

Solution. a) La matrice \( M - \left( {a - b}\right) {I}_{n} \) n’est constituée que de \( b \) , elle est donc de rang 1 . Autrement dit \( \dim \operatorname{Ker}\left\lbrack {M - \left( {a - b}\right) {I}_{n}}\right\rbrack = n - 1 \) , ce qui montre que \( a - b \) est valeur propre de \( M \) et que le sous-espace propre correspondant est de dimension \( n - 1 \) . Le polynôme caractéristique \( {P}_{M} \) de \( M \) s'écrit donc sous la forme

> Solution. a) The matrix \( M - \left( {a - b}\right) {I}_{n} \) consists only of \( b \) , so it is of rank 1. In other words \( \dim \operatorname{Ker}\left\lbrack {M - \left( {a - b}\right) {I}_{n}}\right\rbrack = n - 1 \) , which shows that \( a - b \) is an eigenvalue of \( M \) and that the corresponding eigenspace is of dimension \( n - 1 \) . The characteristic polynomial \( {P}_{M} \) of \( M \) can therefore be written in the form

\[
{P}_{M} = {\left( -1\right) }^{n}{\left\lbrack  X - \left( a - b\right) \right\rbrack  }^{n - 1}\left( {X - \alpha }\right) ,\;\alpha  \in  \mathbb{R}.
\]

On sait que \( \left( {n - 1}\right) \left( {a - b}\right) + \alpha = \operatorname{tr}M = {na} \) , donc \( \alpha = a + \left( {n - 1}\right) b \neq a - b \) , et \( \alpha \) est valeur propre de \( M \) . La somme des dimensions des sous-espaces propres trouvés est égal à \( n \) , ce qui prouve que

> We know that \( \left( {n - 1}\right) \left( {a - b}\right) + \alpha = \operatorname{tr}M = {na} \) , so \( \alpha = a + \left( {n - 1}\right) b \neq a - b \) , and \( \alpha \) is an eigenvalue of \( M \) . The sum of the dimensions of the eigenspaces found is equal to \( n \) , which proves that

\( M \) est diagonalisable, semblable à

> \( M \) is diagonalizable, similar to

\[
\left( \begin{matrix} a - b & & & 0 \\   &  \ddots  & & 0 \\   & 0 & & a - b \\   & & & a + \left( {n - 1}\right) b \end{matrix}\right) .
\]

Au passage, si \( b \neq 0 \) , le polynôme minimal de \( M \) est \( {\Pi }_{M} = \left\lbrack {X - \left( {a - b}\right) }\right\rbrack \left\lbrack {X - \left( {a + \left( {n - 1}\right) b}\right) }\right\rbrack \) .

> Incidentally, if \( b \neq 0 \) , the minimal polynomial of \( M \) is \( {\Pi }_{M} = \left\lbrack {X - \left( {a - b}\right) }\right\rbrack \left\lbrack {X - \left( {a + \left( {n - 1}\right) b}\right) }\right\rbrack \) .

b) La matrice \( M \) est inversible si et seulement si il n’a aucune valeur propre nulle, autrement dit si et seulement si \( a - b \neq 0 \) et \( a + \left( {n - 1}\right) b \neq 0 \) . Dans ce cas, la relation

> b) The matrix \( M \) is invertible if and only if it has no zero eigenvalue, in other words if and only if \( a - b \neq 0 \) and \( a + \left( {n - 1}\right) b \neq 0 \) . In this case, the relation

\[
{\Pi }_{M}\left( M\right)  = 0 = {M}^{2} - \left( {{2a} + \left( {n - 2}\right) b}\right) M + \left( {a - b}\right) \left( {a + \left( {n - 1}\right) b}\right) {I}_{n}
\]

entraîne

> implies

\[
M\left\lbrack  {M - \left( {{2a} + \left( {n - 2}\right) b}\right) {I}_{n}}\right\rbrack   = \left( {b - a}\right) \left( {a + \left( {n - 1}\right) b}\right) {I}_{n},
\]

donc

> therefore

\[
{M}^{-1} = \frac{1}{\left( {a - b}\right) \left( {a + \left( {n - 1}\right) b}\right) }\left\lbrack  {\left( {{2a} + \left( {n - 2}\right) b}\right) {I}_{n} - M}\right\rbrack  .
\]

c) On commence par effectuer la division euclidienne de \( {X}^{p} \) par \( {\Pi }_{M} \) . On sait que

> c) We begin by performing the Euclidean division of \( {X}^{p} \) by \( {\Pi }_{M} \) . We know that

\[
\left( {\exists D \in  \mathbb{R}\left\lbrack  X\right\rbrack  ,\exists {\alpha }_{p},{\beta }_{p} \in  \mathbb{R}}\right) ,\;{X}^{p} = {\Pi }_{M}\left( X\right) D\left( X\right)  + \left( {{\alpha }_{p}X + {\beta }_{p}}\right) .
\]

Dans cette dernière relation, en donnant à \( X \) les valeurs \( a - b \) et \( a + \left( {n - 1}\right) b \) , on obtient

> In this last relation, by assigning the values \( a - b \) and \( a + \left( {n - 1}\right) b \) to \( X \) , we obtain

\[
{\left( a - b\right) }^{p} = 0 + {\alpha }_{p}\left( {a - b}\right)  + {\beta }_{p}\;\text{ et }\;{\left( a + \left( n - 1\right) b\right) }^{p} = {\alpha }_{p}\left( {a + \left( {n - 1}\right) b}\right)  + {\beta }_{p},
\]

d’où

> hence

\[
{\alpha }_{p} = \frac{{\left( a + \left( n - 1\right) b\right) }^{p} - {\left( a - b\right) }^{p}}{nb}\;\text{ et }\;{\beta }_{p} = \frac{\left( {a + \left( {n - 1}\right) b}\right) {\left( a - b\right) }^{p} - \left( {a - b}\right) {\left( a + \left( n - 1\right) b\right) }^{p}}{nb}.
\]

Finalement, on a

> Finally, we have

\[
{M}^{p} = D\left( M\right) {\Pi }_{M}\left( M\right)  + {\alpha }_{p}M + {\beta }_{p}{I}_{n} = {\alpha }_{p}M + {\beta }_{p}{I}_{n}.
\]

Problem 2. Soit \( n \in {\mathbb{N}}^{ * } \) . Déterminer les matrices \( A \) de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) telles que \( A \) commute avec toutes ses matrices semblables.

> Problem 2. Let \( n \in {\mathbb{N}}^{ * } \) . Determine the matrices \( A \) of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( A \) commutes with all its similar matrices.

Solution. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice qui commute avec toutes ses matrices semblables. Soit \( \lambda \in \mathbb{C} \) une valeur propre de \( A \) et \( {E}_{\lambda } \) l’espace propre associé. Pour toute matrice \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) , A \) commute avec \( {P}^{-1}{AP} \) , donc \( {E}_{\lambda } \) est stable par \( {P}^{-1}{AP} \) . Autrement dit, \( {P}^{-1}{AP}{E}_{\lambda } \subset {E}_{\lambda } \) , donc \( {AP}{E}_{\lambda } \subset P{E}_{\lambda } \) . Ainsi, \( P{E}_{\lambda } \) est stable par \( A \) , et ceci pour toute matrice \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . En notant \( k = \dim {E}_{\lambda } \) , on en déduit que tout sous-espace vectoriel \( F \) de dimension \( k \) est stable par \( A \) (en effet, on peut toujours trouver \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tel que \( P{E}_{\lambda } = F \) ). Si \( k = n \) on a \( {E}_{\lambda } = {\mathbb{C}}^{n} \) donc \( A \) est une matrice scalaire. Si \( k < n \) on conclut avec le lemme suivant :

> Solution. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a matrix that commutes with all its similar matrices. Let \( \lambda \in \mathbb{C} \) be an eigenvalue of \( A \) and \( {E}_{\lambda } \) the associated eigenspace. For any matrix \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) , A \) commutes with \( {P}^{-1}{AP} \) , therefore \( {E}_{\lambda } \) is stable under \( {P}^{-1}{AP} \) . In other words, \( {P}^{-1}{AP}{E}_{\lambda } \subset {E}_{\lambda } \) , therefore \( {AP}{E}_{\lambda } \subset P{E}_{\lambda } \) . Thus, \( P{E}_{\lambda } \) is stable under \( A \) , and this for any matrix \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . By noting \( k = \dim {E}_{\lambda } \) , we deduce that any vector subspace \( F \) of dimension \( k \) is stable under \( A \) (indeed, we can always find \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( P{E}_{\lambda } = F \) ). If \( k = n \) we have \( {E}_{\lambda } = {\mathbb{C}}^{n} \) therefore \( A \) is a scalar matrix. If \( k < n \) we conclude with the following lemma:

Lemme. Soit \( E \) un \( \mathbb{K} \) -espace vectoriel de dimension finie \( n \) et \( f \in \mathcal{L}\left( E\right) \) , et supposons qu’il existe \( k \in {\mathbb{N}}^{ * }, k \leq n - 1 \) tel que \( f \) stabilise tout sous-espace vectoriel de dimension \( k \) . Alors \( f \) est une homothétie.

> Lemma. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space \( n \) and \( f \in \mathcal{L}\left( E\right) \) , and suppose there exists \( k \in {\mathbb{N}}^{ * }, k \leq n - 1 \) such that \( f \) stabilizes every vector subspace of dimension \( k \) . Then \( f \) is a homothety.

On prouve ce lemme par récurrence sur \( k \geq 1 \) . Pour \( k = 1 \) , c’est la proposition 3 page 121. Soit \( k \) tel que \( 2 \leq k \leq n - 1 \) et supposons le résultat vrai au rang \( k - 1 \) . Soit \( H \) un sous-espace vectoriel de dimension \( k - 1 \) . Soient \( u \) et \( v \) deux vecteurs tels que \( u, v \notin H \) et \( u \) et \( v \) forment une famille libre (c’est possible car \( \dim H \leq n - 2 \) ). Alors \( F = H \oplus \mathbb{C}u \) et \( G = H \oplus \mathbb{C}v \) sont des sous-espaces vectoriels de dimension \( k \) , donc stables par \( f \) . Donc \( F \cap G \) est stable par \( f \) , et comme \( F \cap G = H \) est un sous-espace vectoriel de dimension \( k - 1 \) , l’hypothèse de récurrence nous assure que \( f \) est une homothétie.

> We prove this lemma by induction on \( k \geq 1 \) . For \( k = 1 \) , it is proposition 3 on page 121. Let \( k \) be such that \( 2 \leq k \leq n - 1 \) and assume the result holds for rank \( k - 1 \) . Let \( H \) be a vector subspace of dimension \( k - 1 \) . Let \( u \) and \( v \) be two vectors such that \( u, v \notin H \) and \( u \) and \( v \) form a linearly independent family (this is possible because \( \dim H \leq n - 2 \) ). Then \( F = H \oplus \mathbb{C}u \) and \( G = H \oplus \mathbb{C}v \) are vector subspaces of dimension \( k \) , and thus stable under \( f \) . Therefore \( F \cap G \) is stable under \( f \) , and since \( F \cap G = H \) is a vector subspace of dimension \( k - 1 \) , the induction hypothesis ensures that \( f \) is a homothety.

En conclusion, les matrices répondant au problème sont les matrices scalaires.

> In conclusion, the matrices satisfying the problem are the scalar matrices.

Problem 3. a) Soit \( M \in {\mathcal{M}}_{2}\left( \mathbb{Z}\right) \) telle qu’il existe un entier \( m \in {\mathbb{N}}^{ * } \) vérifiant \( {M}^{m} = {I}_{n} \) . Montrer que \( {M}^{12} = {I}_{2} \) .

> Problem 3. a) Let \( M \in {\mathcal{M}}_{2}\left( \mathbb{Z}\right) \) be such that there exists an integer \( m \in {\mathbb{N}}^{ * } \) satisfying \( {M}^{m} = {I}_{n} \) . Show that \( {M}^{12} = {I}_{2} \) .

b) (Cas général). Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( \Gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \mid \exists m \in {\mathbb{N}}^{ * },{M}^{m} = {I}_{n}}\right\} \) . Montrer l’existence de \( r \in {\mathbb{N}}^{ * } \) tel que \( {M}^{r} = {I}_{n} \) pour tout \( M \in \Gamma \) .

> b) (General case). Let \( n \in {\mathbb{N}}^{ * } \) . Let \( \Gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \mid \exists m \in {\mathbb{N}}^{ * },{M}^{m} = {I}_{n}}\right\} \) . Show the existence of \( r \in {\mathbb{N}}^{ * } \) such that \( {M}^{r} = {I}_{n} \) for all \( M \in \Gamma \) .

Solution. a) Regardons \( M \) comme une matrice de \( {\mathcal{M}}_{2}\left( \mathbb{C}\right) \) . Le polynôme \( {X}^{m} - 1 \) annule \( M \) et comme il n’a que des racines simples dans \( \mathbb{C}, M \) est diagonalisable dans \( {\mathcal{M}}_{2}\left( \mathbb{C}\right) \) :

> Solution. a) Consider \( M \) as a matrix in \( {\mathcal{M}}_{2}\left( \mathbb{C}\right) \) . The polynomial \( {X}^{m} - 1 \) annihilates \( M \) and since it only has simple roots in \( \mathbb{C}, M \) it is diagonalizable in \( {\mathcal{M}}_{2}\left( \mathbb{C}\right) \) :

\[
\exists P \in  \mathcal{G}{\ell }_{2}\left( \mathbb{C}\right) ,\;{P}^{-1}{MP} = \left( \begin{matrix} \alpha & 0 \\  0 & \beta  \end{matrix}\right)  = D\;\text{ avec }\;\alpha ,\beta  \in  \mathbb{C}.
\]

Comme \( {M}^{m} = {I}_{2} \) , on a \( {D}^{m} = {I}_{2} \) , donc \( {\alpha }^{m} = {\beta }^{m} = 1 \) . En particulier, \( \left| \alpha \right| = \left| \beta \right| = 1\;\left( *\right) \) .

> Since \( {M}^{m} = {I}_{2} \) , we have \( {D}^{m} = {I}_{2} \) , thus \( {\alpha }^{m} = {\beta }^{m} = 1 \) . In particular, \( \left| \alpha \right| = \left| \beta \right| = 1\;\left( *\right) \) .

On a \( \alpha + \beta = \operatorname{tr}D = \operatorname{tr}M \in \mathbb{Z} \) . De (*), on tire \( \alpha + \beta \in \{ - 2, - 1,0,1,2\} \;\left( {* * }\right) \) . Par ailleurs \( \det M \in \mathbb{Z} \) donc d’après (*) on a \( \det M = {\alpha \beta } \in \{ - 1,1\} \) . Si \( {\alpha \beta } = - 1 \) on a \( \beta = - 1/\alpha = - \overline{\alpha } \) donc \( \alpha + \beta = \alpha - \overline{\alpha } \in i\mathbb{R} \) , donc forcément \( \alpha + \beta = 0 \) d’après (**). En résumé \( \alpha \) et \( \beta \) sont solution de l’équation du second degré \( {z}^{2} - {az} + b = 0 \) , avec \( a = \alpha + \beta \in \{ - 2, - 1,0,1,2\} \) et \( b = {\alpha \beta } = 1 \) si \( a \neq 0, b \in \{ - 1,1\} \) si \( a = 0 \) . Listant ces équations, on détermine les valeurs possibles de \( \alpha ,\beta \) :

> We have \( \alpha + \beta = \operatorname{tr}D = \operatorname{tr}M \in \mathbb{Z} \) . From (*), we derive \( \alpha + \beta \in \{ - 2, - 1,0,1,2\} \;\left( {* * }\right) \) . Furthermore, \( \det M \in \mathbb{Z} \) , so according to (*) we have \( \det M = {\alpha \beta } \in \{ - 1,1\} \) . If \( {\alpha \beta } = - 1 \) , we have \( \beta = - 1/\alpha = - \overline{\alpha } \) , so \( \alpha + \beta = \alpha - \overline{\alpha } \in i\mathbb{R} \) , and therefore necessarily \( \alpha + \beta = 0 \) according to (**). In summary, \( \alpha \) and \( \beta \) are solutions to the quadratic equation \( {z}^{2} - {az} + b = 0 \) , with \( a = \alpha + \beta \in \{ - 2, - 1,0,1,2\} \) and \( b = {\alpha \beta } = 1 \) if \( a \neq 0, b \in \{ - 1,1\} \) if \( a = 0 \) . By listing these equations, we determine the possible values of \( \alpha ,\beta \) :

\[
{z}^{2} + {2z} + 1 = 0\; \Rightarrow  \;\left( {\alpha ,\beta }\right)  = \left( {-1, - 1}\right)
\]

\[
{z}^{2} + z + 1 = 0 \Rightarrow  \;\left( {\alpha ,\beta }\right)  \in  \left\{  {\left( {{e}^{-{2i\pi }/3},{e}^{{2i\pi }/3}}\right) ,\left( {{e}^{{2i\pi }/3},{e}^{-{2i\pi }/3}}\right) }\right\}
\]

\[
{z}^{2} + 1 = 0 \Rightarrow  \;\left( {\alpha ,\beta }\right)  \in  \{ \left( {i, - i}\right) ,\left( {-i, i}\right) \}
\]

\[
{z}^{2} - 1 = 0 \Rightarrow  \;\left( {\alpha ,\beta }\right)  \in  \{ \left( {-1,1}\right) ,\left( {1, - 1}\right) \}
\]

\[
{z}^{2} - z + 1 = 0\; \Rightarrow  \;\left( {\alpha ,\beta }\right)  \in  \left\{  {\left( {{e}^{-{i\pi }/3},{e}^{{i\pi }/3}}\right) ,\left( {{e}^{{i\pi }/3},{e}^{-{i\pi }/3}}\right) }\right\}
\]

\[
{z}^{2} - {2z} + 1 = 0\; \Rightarrow  \;\left( {\alpha ,\beta }\right)  = \left( {1,1}\right)
\]

Dans tous les cas, on a \( {\alpha }^{12} = {\beta }^{12} = 1 \) , ce qui prouve que \( {D}^{12} = {I}_{2} \) et donc \( {M}^{12} = {I}_{2} \) .

> In all cases, we have \( {\alpha }^{12} = {\beta }^{12} = 1 \) , which proves that \( {D}^{12} = {I}_{2} \) and therefore \( {M}^{12} = {I}_{2} \) .

b) On procède comme dans le cas \( n = 2 \) . Si \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) vérifie \( {M}^{m} = {I}_{n} \) , alors le polynôme \( {X}^{m} - 1 \) annule \( M \) et comme il n’a que des racines simples dans \( \mathbb{C}, M \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Ses valeurs propres \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) vérifient toutes \( {\alpha }_{1}^{m} = \ldots = {\alpha }_{n}^{m} = 1 \) , donc \( \left| {\alpha }_{1}\right| = \ldots = \; \left| {\alpha }_{n}\right| = 1 \) . Notons \( {P}_{M} = {\left( -1\right) }^{m}\left( {{X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n}}\right) \) le polynôme caractéristique de \( M \) . L’expression des coefficients d’un polynôme en fonction de ses racines entraîne

> b) We proceed as in the case \( n = 2 \) . If \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) satisfies \( {M}^{m} = {I}_{n} \) , then the polynomial \( {X}^{m} - 1 \) annihilates \( M \) and since it only has simple roots in \( \mathbb{C}, M \) it is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Its eigenvalues \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) all satisfy \( {\alpha }_{1}^{m} = \ldots = {\alpha }_{n}^{m} = 1 \) , therefore \( \left| {\alpha }_{1}\right| = \ldots = \; \left| {\alpha }_{n}\right| = 1 \) . Let \( {P}_{M} = {\left( -1\right) }^{m}\left( {{X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n}}\right) \) be the characteristic polynomial of \( M \) . The expression of the coefficients of a polynomial as a function of its roots implies

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\left| {a}_{k}\right|  = \left| {\mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n\} } \\  {\left| J\right|  = k} }}\mathop{\prod }\limits_{\substack{{j \in  J} }}{\alpha }_{j}}\right|  \leq  \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n\} } \\  {\left| J\right|  = k} }}1 = \left( \begin{array}{l} n \\  k \end{array}\right) .
\]

Ainsi les coefficients de \( {P}_{M} \) sont bornés indépendamment de \( m \) . Comme \( M \) est à coefficients entiers, on a \( {P}_{M} = \det \left( {M - X{I}_{n}}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) , donc il n’y a qu’un nombre fini de polynômes caractéristiques possibles des matrices \( M \in \Gamma \) . Donc il n’y a qu’un nombre fini de valeurs propres possibles associées aux matrices \( M \in \Gamma \) , qui sont toutes des racines de l’unité. Notons \( r \) le ppcm des ordres de toutes les valeurs propres \( \alpha \) des matrices \( M \in \Gamma \) (l’ordre de \( \alpha \) étant le plus petit entier \( p > 0 \) tel que \( {\alpha }^{p} = 1 \) ). Pour \( M \in \Gamma \) , toute valeur propre \( \alpha \) de \( M \) vérifie \( {\alpha }^{r} = 1 \) , et comme \( M \) est diagonalisable on en déduit \( {M}^{r} = {I}_{n} \) .

> Thus the coefficients of \( {P}_{M} \) are bounded independently of \( m \) . Since \( M \) has integer coefficients, we have \( {P}_{M} = \det \left( {M - X{I}_{n}}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) , so there are only a finite number of possible characteristic polynomials for the matrices \( M \in \Gamma \) . Therefore, there are only a finite number of possible eigenvalues associated with the matrices \( M \in \Gamma \) , all of which are roots of unity. Let \( r \) be the lcm of the orders of all eigenvalues \( \alpha \) of the matrices \( M \in \Gamma \) (the order of \( \alpha \) being the smallest integer \( p > 0 \) such that \( {\alpha }^{p} = 1 \) ). For \( M \in \Gamma \) , every eigenvalue \( \alpha \) of \( M \) satisfies \( {\alpha }^{r} = 1 \) , and since \( M \) is diagonalizable, we deduce \( {M}^{r} = {I}_{n} \) .

Problem 4. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) .

> Problem 4. Let \( E \) be a finite-dimensional \( \mathbb{C} \) -vector space \( n \in {\mathbb{N}}^{ * } \) .

1/ a) Soit \( f \in \mathcal{L}\left( E\right) \) tel que \( \forall p,1 \leq p \leq n,\operatorname{tr}\left( {f}^{p}\right) = 0 \) . Montrer que \( f \) est nilpotente.

> 1/ a) Let \( f \in \mathcal{L}\left( E\right) \) be such that \( \forall p,1 \leq p \leq n,\operatorname{tr}\left( {f}^{p}\right) = 0 \) . Show that \( f \) is nilpotent.

b) Pour tout \( u, v \in \mathcal{L}\left( E\right) \) , on note \( \left\lbrack {u, v}\right\rbrack = {uv} - {vu} \) (crochet de Lie de \( u \) et \( v \) ). Soient \( f, g \in \mathcal{L}\left( E\right) \) tels que \( \left\lbrack {\left\lbrack {f, g}\right\rbrack , f}\right\rbrack = 0 \) . Montrer que \( \left\lbrack {f, g}\right\rbrack \) est nilpotente.

> b) For all \( u, v \in \mathcal{L}\left( E\right) \) , we denote \( \left\lbrack {u, v}\right\rbrack = {uv} - {vu} \) (Lie bracket of \( u \) and \( v \) ). Let \( f, g \in \mathcal{L}\left( E\right) \) be such that \( \left\lbrack {\left\lbrack {f, g}\right\rbrack , f}\right\rbrack = 0 \) . Show that \( \left\lbrack {f, g}\right\rbrack \) is nilpotent.

2/ Soient \( f, g \in \mathcal{L}\left( E\right) \) tels que pour tout \( p \in \{ 1,\ldots , n\} ,\operatorname{tr}\left( {f}^{p}\right) = \operatorname{tr}\left( {g}^{p}\right) \) . Montrer que \( f \) et \( g \) ont même polynôme caractéristique. (On pourra utiliser le résultat de la remarque de l'exercice 3 page 86.)

> 2/ Let \( f, g \in \mathcal{L}\left( E\right) \) be such that for all \( p \in \{ 1,\ldots , n\} ,\operatorname{tr}\left( {f}^{p}\right) = \operatorname{tr}\left( {g}^{p}\right) \) . Show that \( f \) and \( g \) have the same characteristic polynomial. (One may use the result from the remark in exercise 3 on page 86.)

Solution. 1/ a) Il suffit de montrer que toutes les valeurs propres de \( M \) sont nulles (voir la remarque 6 page 187).

> Solution. 1/ a) It suffices to show that all eigenvalues of \( M \) are zero (see remark 6 on page 187).

Comme le corps \( \mathbb{C} \) est algébriquement clos, il existe une base \( B \) qui trigonalise \( f \) . Notons \( {\lambda }_{1},\ldots ,{\lambda }_{q} \) les valeurs propres de \( f \) (distinctes deux à deux), et \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) leur ordre de multiplicité dans le polynôme caractéristique de \( f \) . Les termes de la diagonale principale de \( {\left\lbrack f\right\rbrack }_{B}^{p} \) sont les puissances \( p \) -ièmes des termes de la diagonale principale de \( {\left\lbrack f\right\rbrack }_{B} \) et on en déduit

> Since the field \( \mathbb{C} \) is algebraically closed, there exists a basis \( B \) that triangularizes \( f \) . Let \( {\lambda }_{1},\ldots ,{\lambda }_{q} \) be the eigenvalues of \( f \) (distinct from one another), and \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) their multiplicity in the characteristic polynomial of \( f \) . The terms on the main diagonal of \( {\left\lbrack f\right\rbrack }_{B}^{p} \) are the \( p \) -th powers of the terms on the main diagonal of \( {\left\lbrack f\right\rbrack }_{B} \) and we deduce

\[
\forall p,1 \leq  p \leq  n,\;\mathop{\sum }\limits_{{i = 1}}^{q}{\alpha }_{i}{\lambda }_{i}^{p} = \operatorname{tr}\left( {f}^{p}\right)  = 0.
\]

Raisonnons par l'absurde et supposons que \( f \) ait au moins une valeur propre non nulle. Quitte à renuméroter les \( {\lambda }_{i} \) , on peut supposer que les \( {\lambda }_{i} \) non nuls sont \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) (avec \( 1 \leq r \leq q \) ) ce qui donne

> Let us reason by contradiction and assume that \( f \) has at least one non-zero eigenvalue. By renumbering the \( {\lambda }_{i} \) , we can assume that the non-zero \( {\lambda }_{i} \) are \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) (with \( 1 \leq r \leq q \) ) which gives

\[
\forall p,1 \leq  p \leq  r,\;\mathop{\sum }\limits_{{i = 1}}^{r}{\alpha }_{i}{\lambda }_{i}^{p} = 0.
\]

Ceci s'écrit matriciellement sous la forme

> This can be written in matrix form as

\[
M\left( \begin{matrix} {\alpha }_{1} \\  \vdots \\  {\alpha }_{r} \end{matrix}\right)  = 0\text{ avec }M = \left( \begin{matrix} {\lambda }_{1} & {\lambda }_{2} & \cdots & {\lambda }_{r} \\  {\lambda }_{1}^{2} & {\lambda }_{2}^{2} & \cdots & {\lambda }_{r}^{2} \\  \vdots & \vdots & & \vdots \\  {\lambda }_{1}^{r} & {\lambda }_{2}^{r} & \cdots & {\lambda }_{r}^{r} \end{matrix}\right)  \in  {\mathcal{M}}_{r}\left( \mathbb{C}\right) .
\]

Ceci entraîne que \( M \) n’est pas injective et donc que det \( M = 0 \) . Or

> This implies that \( M \) is not injective and therefore that det \( M = 0 \) . However

\[
\det M = {\lambda }_{1}\cdots {\lambda }_{r}\left| \begin{matrix} 1 & 1 & & 1 \\  {\lambda }_{1} & {\lambda }_{2} & \cdots & {\lambda }_{r} \\  \vdots & \vdots & & \vdots \\  {\lambda }_{1}^{r - 1} & {\lambda }_{2}^{r - 1} & \cdots & {\lambda }_{r}^{r - 1} \end{matrix}\right|  = {\lambda }_{1}\cdots {\lambda }_{r}\mathop{\prod }\limits_{{1 \leq  i < j \leq  r}}\left( {{\lambda }_{j} - {\lambda }_{i}}\right)
\]

(on a affaire à un déterminant de Vandermonde). Comme det \( M = 0 \) et que les \( {\lambda }_{i}\left( {1 \leq i \leq r}\right) \) sont distincts deux à deux, on en déduit qu’il existe \( i \leq r \) tels que \( {\lambda }_{i} = 0 \) , ce qui est absurde car nous avions choisit les \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq r} \) non nuls. Les valeurs propres de \( f \) sont donc toutes nulles, et donc \( f \) est nilpotente.

> (we are dealing with a Vandermonde determinant). Since det \( M = 0 \) and the \( {\lambda }_{i}\left( {1 \leq i \leq r}\right) \) are distinct from one another, we deduce that there exist \( i \leq r \) such that \( {\lambda }_{i} = 0 \) , which is absurd because we had chosen the \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq r} \) to be non-zero. The eigenvalues of \( f \) are therefore all zero, and thus \( f \) is nilpotent.

b) La trace d’un crochet de Lie est toujours nulle car si \( u, v \in \mathcal{L}\left( E\right) ,\operatorname{tr}\left\lbrack {u, v}\right\rbrack = \operatorname{tr}\left( {{uv} - {vu}}\right) = \; \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0. \)

> b) The trace of a Lie bracket is always zero because if \( u, v \in \mathcal{L}\left( E\right) ,\operatorname{tr}\left\lbrack {u, v}\right\rbrack = \operatorname{tr}\left( {{uv} - {vu}}\right) = \; \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0. \)

Ceci étant, d'après la question précédente, pour montrer le résultat il suffit de montrer que pour tout \( p,1 \leq p \leq n,\operatorname{tr}\left( {\left\lbrack f, g\right\rbrack }^{p}\right) = \operatorname{tr}\left\lbrack {\left( fg - gf\right) }^{p}\right\rbrack = 0 \) . Fixons un tel entier \( p \) . On a

> Given this, according to the previous question, to show the result it suffices to show that for all \( p,1 \leq p \leq n,\operatorname{tr}\left( {\left\lbrack f, g\right\rbrack }^{p}\right) = \operatorname{tr}\left\lbrack {\left( fg - gf\right) }^{p}\right\rbrack = 0 \) . Let us fix such an integer \( p \) . We have

\[
{\left( fg - gf\right) }^{p} = {\left( fg - gf\right) }^{p - 1}\left( {{fg} - {gf}}\right)  = {\left( fg - gf\right) }^{p - 1}{fg} - {\left( fg - gf\right) }^{p - 1}{gf},
\]

et comme \( f \) et \( \left( {{fg} - {gf}}\right) \) commutent par hypothèse,

> and since \( f \) and \( \left( {{fg} - {gf}}\right) \) commute by hypothesis,

\[
{\left( fg - gf\right) }^{p} = f{\left( fg - gf\right) }^{p - 1}g - {\left( fg - gf\right) }^{p - 1}{gf} = \left\lbrack  {f,{\left( fg - gf\right) }^{p - 1}g}\right\rbrack  .
\]

D’après la remarque précédente, on a donc \( \operatorname{tr}\left\lbrack {\left( fg - gf\right) }^{p}\right\rbrack = 0 \) , et ceci pour tout \( p,1 \leq p \leq n \) , d'où le résultat.

> According to the previous remark, we therefore have \( \operatorname{tr}\left\lbrack {\left( fg - gf\right) }^{p}\right\rbrack = 0 \), and this for all \( p,1 \leq p \leq n \), hence the result.

2/ Notons \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) les valeurs propres de \( f \) (répétées avec leur ordre de multiplicité). Comme plus haut, on obtient, en trigonalisant \( f \) , que \( \operatorname{tr}\left( {f}^{p}\right) = {\lambda }_{1}^{p} + \cdots + {\lambda }_{n}^{p} \) . D’après les formules de Newton (voir l’exercice 3 page 86), les \( {\sigma }_{p} = \sum {X}_{1}\cdots {X}_{p} \) , polynômes symétriques élémentaires de \( \mathbb{C}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) , s’expriment en fonction des sommes de Newton \( {S}_{p} = \mathop{\sum }\limits_{{i = 1}}^{n}{X}_{i}^{p}\left( {1 \leq p \leq n}\right) \) . On peut donc exprimer les coefficients du polynôme \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {X}_{i}}\right) \) en fonction des \( {S}_{p}\left( {1 \leq p \leq n}\right) \) . On en déduit que les coefficients du polynôme caractéristique \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) de \( f \) s’expriment en fonction des \( \operatorname{tr}\left( {f}^{p}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{p}\left( {1 \leq p \leq n}\right) \) . Il en est de même pour \( g \) , et comme \( \operatorname{tr}\left( {f}^{p}\right) = \operatorname{tr}\left( {g}^{p}\right) \) pour \( 1 \leq p \leq n \) , on a \( {P}_{f} = {P}_{g} \) .

> 2/ Let \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) be the eigenvalues of \( f \) (repeated with their multiplicity). As above, by triangularizing \( f \), we obtain that \( \operatorname{tr}\left( {f}^{p}\right) = {\lambda }_{1}^{p} + \cdots + {\lambda }_{n}^{p} \). According to Newton's formulas (see exercise 3 page 86), the \( {\sigma }_{p} = \sum {X}_{1}\cdots {X}_{p} \), elementary symmetric polynomials of \( \mathbb{C}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \), are expressed in terms of Newton sums \( {S}_{p} = \mathop{\sum }\limits_{{i = 1}}^{n}{X}_{i}^{p}\left( {1 \leq p \leq n}\right) \). We can therefore express the coefficients of the polynomial \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {X}_{i}}\right) \) in terms of \( {S}_{p}\left( {1 \leq p \leq n}\right) \). We deduce that the coefficients of the characteristic polynomial \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) of \( f \) are expressed in terms of \( \operatorname{tr}\left( {f}^{p}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{p}\left( {1 \leq p \leq n}\right) \). The same applies to \( g \), and since \( \operatorname{tr}\left( {f}^{p}\right) = \operatorname{tr}\left( {g}^{p}\right) \) for \( 1 \leq p \leq n \), we have \( {P}_{f} = {P}_{g} \).

Problem 5 (ENDOMORPHISMES DE \( \mathcal{L}\left( E\right) \) ). Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \) . Si \( u, v \in \mathcal{L}\left( E\right) \) , on note \( {L}_{u} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) l’endomorphisme défini sur \( \mathcal{L}\left( E\right) \) par \( {L}_{u}\left( f\right) = u \circ f \) , et on note \( {R}_{v} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) celui défini par \( {R}_{v}\left( f\right) = f \circ v \) .

> Problem 5 (ENDOMORPHISMS OF \( \mathcal{L}\left( E\right) \)). Let \( E \) be a finite-dimensional \( \mathbb{K} \)-vector space \( n \). If \( u, v \in \mathcal{L}\left( E\right) \), we denote by \( {L}_{u} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) the endomorphism defined on \( \mathcal{L}\left( E\right) \) by \( {L}_{u}\left( f\right) = u \circ f \), and we denote by \( {R}_{v} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) the one defined by \( {R}_{v}\left( f\right) = f \circ v \).

1 / a) Calculer \( \dim \left( {\operatorname{Ker}{L}_{u}}\right) \) et \( \dim \left( {\operatorname{Ker}{R}_{v}}\right) \) en fonction de \( \dim \left( {\operatorname{Ker}u}\right) \) et de \( \dim \left( {\operatorname{Ker}v}\right) \) . b) Montrer que \( u \) (resp. \( v \) ) est diagonalisable si et seulement si \( {L}_{u} \) (resp. \( {R}_{v} \) ) est diago-nalisable.

> 1 / a) Calculate \( \dim \left( {\operatorname{Ker}{L}_{u}}\right) \) and \( \dim \left( {\operatorname{Ker}{R}_{v}}\right) \) in terms of \( \dim \left( {\operatorname{Ker}u}\right) \) and \( \dim \left( {\operatorname{Ker}v}\right) \). b) Show that \( u \) (resp. \( v \)) is diagonalizable if and only if \( {L}_{u} \) (resp. \( {R}_{v} \)) is diagonalizable.

c) Donner les matrices de \( {L}_{u} \) et \( {R}_{v} \) dans des bases commodes.

> c) Give the matrices of \( {L}_{u} \) and \( {R}_{v} \) in convenient bases.

2 / On note \( {A}_{u, v} = {L}_{u} - {R}_{v} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) .

> 2 / Let \( {A}_{u, v} = {L}_{u} - {R}_{v} \in \mathcal{L}\left( {\mathcal{L}\left( E\right) }\right) \) be denoted by .

a) Si \( u \) et \( v \) sont diagonalisables, montrer que \( {A}_{u, v} \) est diagonalisable.

> a) If \( u \) and \( v \) are diagonalizable, show that \( {A}_{u, v} \) is diagonalizable.

b) On suppose que \( {P}_{u} \) , le polynôme caractéristique de \( u \) , est scindé sur \( \mathbb{K} \) . Si \( {A}_{u, u} \) est diagonalisable, montrer que \( u \) est diagonalisable.

> b) Suppose that \( {P}_{u} \) , the characteristic polynomial of \( u \) , splits over \( \mathbb{K} \) . If \( {A}_{u, u} \) is diagonalizable, show that \( u \) is diagonalizable.

Solution. 1/ a) On a

> Solution. 1/ a) We have

\[
f \in  \operatorname{Ker}\left( {L}_{u}\right)  \Leftrightarrow  u \circ  f = 0 \Leftrightarrow  \operatorname{Im}f \subset  \operatorname{Ker}u,
\]

on en déduit \( \operatorname{Ker}\left( {L}_{u}\right) = \mathcal{L}\left( {E,\operatorname{Ker}u}\right) \) , d’où \( \dim \left( {\operatorname{Ker}{L}_{u}}\right) = n\dim \left( {\operatorname{Ker}u}\right) \) .

> we deduce \( \operatorname{Ker}\left( {L}_{u}\right) = \mathcal{L}\left( {E,\operatorname{Ker}u}\right) \) , hence \( \dim \left( {\operatorname{Ker}{L}_{u}}\right) = n\dim \left( {\operatorname{Ker}u}\right) \) .

Pour \( {R}_{v} \) , on a

> For \( {R}_{v} \) , we have

\[
f \in  \operatorname{Ker}\left( {R}_{v}\right)  \Leftrightarrow  f \circ  v = 0 \Leftrightarrow  \operatorname{Im}v \subset  \operatorname{Ker}f.
\]

Si \( S \) désigne un supplémentaire de \( \operatorname{Im}v \) dans \( E \) , \( \operatorname{Ker}{R}_{v} \) est donc isomorphe à \( \mathcal{L}\left( {S, E}\right) \) , d’où \( \dim \left( {\operatorname{Ker}{R}_{v}}\right) = n\dim S = n\left( {n - \dim \left( {\operatorname{Im}v}\right) }\right) = n\dim \left( {\operatorname{Ker}v}\right) . \)

> If \( S \) denotes a supplementary subspace of \( \operatorname{Im}v \) in \( E \) , \( \operatorname{Ker}{R}_{v} \) is therefore isomorphic to \( \mathcal{L}\left( {S, E}\right) \) , hence \( \dim \left( {\operatorname{Ker}{R}_{v}}\right) = n\dim S = n\left( {n - \dim \left( {\operatorname{Im}v}\right) }\right) = n\dim \left( {\operatorname{Ker}v}\right) . \)

b) Si \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , on vérifie facilement que \( P\left( {L}_{u}\right) = {L}_{P\left( u\right) } \) . On a donc l’équivalence

> b) If \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , it is easy to verify that \( P\left( {L}_{u}\right) = {L}_{P\left( u\right) } \) . We thus have the equivalence

\[
P\left( u\right)  = 0 \Leftrightarrow  \forall f, P\left( u\right)  \circ  f = 0 \Leftrightarrow  {L}_{P\left( u\right) } = 0 \Leftrightarrow  P\left( {L}_{u}\right)  = 0.
\]

On en déduit que \( u \) et \( {L}_{u} \) ont même polynôme minimal. Donc d’après le théorème 2 page 185, \( u \) est diagonalisable si et seulement si \( {L}_{u} \) est diagonalisable.

> We deduce that \( u \) and \( {L}_{u} \) have the same minimal polynomial. Therefore, according to theorem 2 on page 185, \( u \) is diagonalizable if and only if \( {L}_{u} \) is diagonalizable.

On procède de même pour \( {R}_{v} \) .

> We proceed in the same way for \( {R}_{v} \) .

c) Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . On définit la base \( {\left( {e}_{i, j}\right) }_{1 \leq i, j \leq n} \) de \( \mathcal{L}\left( E\right) \) par

> c) Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \) . We define the basis \( {\left( {e}_{i, j}\right) }_{1 \leq i, j \leq n} \) of \( \mathcal{L}\left( E\right) \) by

\[
{e}_{i, j}\left( {e}_{k}\right)  = {\delta }_{j, k}{e}_{i}\;\text{ avec }\;{\delta }_{j, k} = \left\{  \begin{array}{ll} 1 & \text{ si }j = k, \\  0 & \text{ sinon. } \end{array}\right.
\]

Notons \( {\left\lbrack u\right\rbrack }_{B} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) la matrice de \( u \) dans la base \( B \) . On a

> Let \( {\left\lbrack u\right\rbrack }_{B} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) be the matrix of \( u \) in the basis \( B \) . We have

\[
u \circ  {e}_{{i}_{0},{j}_{0}}\left( {e}_{k}\right)  = {\delta }_{{j}_{0}, k}u\left( {e}_{{i}_{0}}\right)  = {\delta }_{{j}_{0}, k}\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i,{i}_{0}}{e}_{i} = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i,{i}_{0}}{e}_{i,{j}_{0}}\left( {e}_{k}\right) ,
\]

donc \( {L}_{u}\left( {e}_{i, j}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k, i}{e}_{k, j} \) . Dans la base

> therefore \( {L}_{u}\left( {e}_{i, j}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k, i}{e}_{k, j} \) . In the basis

\[
{B}_{1} = \left( {{e}_{1,1},\ldots ,{e}_{n,1};{e}_{1,2},\ldots ,{e}_{n,2};\ldots ;{e}_{1, n},\ldots ,{e}_{n, n}}\right) ,
\]

la matrice de \( {L}_{u} \) s’écrit donc par blocs sous la forme

> the matrix of \( {L}_{u} \) is therefore written in block form as

\[
{\left\lbrack  {L}_{u}\right\rbrack  }_{{B}_{1}} = \left( \begin{matrix} M & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & M \end{matrix}\right) ,\;\text{ où }\;M = {\left\lbrack  u\right\rbrack  }_{B}.
\]

Si on écrit \( {\left\lbrack v\right\rbrack }_{B} = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \) , un calcul analogue donne \( {R}_{v}\left( {e}_{i, j}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{b}_{j, k}{e}_{i, k} \) . Ceci entraîne que dans la base

> If we write \( {\left\lbrack v\right\rbrack }_{B} = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \) , a similar calculation gives \( {R}_{v}\left( {e}_{i, j}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{b}_{j, k}{e}_{i, k} \) . This implies that in the basis

\[
{B}_{2} = \left( {{e}_{1,1},\ldots ,{e}_{1, n};{e}_{2,1},\ldots ,{e}_{2, n};\ldots ;{e}_{n,1},\ldots ,{e}_{n, n}}\right) ,
\]

la matrice de \( {R}_{v} \) s’écrit

> the matrix of \( {R}_{v} \) is written

\[
{\left\lbrack  {R}_{v}\right\rbrack  }_{{B}_{2}} = \left( \begin{matrix} {}^{\mathrm{t}}N & \left( 0\right) \\  \ldots & \\  \left( 0\right) & {}^{\mathrm{t}}N \end{matrix}\right) ,\;\text{ où }\;N = {\left\lbrack  v\right\rbrack  }_{B}.
\]

2 / a) On sait déjà que \( {L}_{u} \) et \( {R}_{v} \) sont diagonalisables d’après 1/b). Or

> 2 / a) We already know that \( {L}_{u} \) and \( {R}_{v} \) are diagonalizable according to 1/b). However

\[
\forall f \in  \mathcal{L}\left( E\right) ,\;{L}_{u} \circ  {R}_{v}\left( f\right)  = u \circ  f \circ  v = {R}_{v}\left( {u \circ  f}\right)  = {R}_{v} \circ  {L}_{u}\left( f\right) ,
\]

c’est-à-dire que \( {L}_{u} \) et \( {R}_{v} \) commutent. On peut donc les diagonaliser dans une même base, et cette base diagonalise \( {A}_{u, v} = {L}_{u} - {R}_{v} \) .

> that is to say that \( {L}_{u} \) and \( {R}_{v} \) commute. We can therefore diagonalize them in the same basis, and this basis diagonalizes \( {A}_{u, v} = {L}_{u} - {R}_{v} \) .

b) Comme \( {P}_{u} \) est scindé sur \( \mathbb{K} \) , on peut écrire (décomposition de Dunford, voir la partie 4.2 page 203) \( u = d + n, d \) diagonalisable, \( n \) nilpotente, avec \( n \circ d = d \circ n \) . Pour alléger les notations, on note, pour \( f \in \mathcal{L}\left( E\right) ,{A}_{f} = {A}_{f, f} \) .

> b) Since \( {P}_{u} \) splits over \( \mathbb{K} \) , we can write (Dunford decomposition, see part 4.2 page 203) \( u = d + n, d \) diagonalizable, \( n \) nilpotent, with \( n \circ d = d \circ n \) . To simplify notation, we denote, for \( f \in \mathcal{L}\left( E\right) ,{A}_{f} = {A}_{f, f} \) .

On a \( {A}_{u} = {A}_{d} + {A}_{n} \) . Or il existe \( p \in {\mathbb{N}}^{ * } \) tel que \( {n}^{p} = 0 \) , ce qui entraîne \( {\left( {A}_{n}\right) }^{p} = {A}_{{n}^{p}} = 0 \) , c’est-à-dire que \( {A}_{n} \) est nilpotent. D’après \( 2/ \) a), \( {A}_{d} \) est diagonalisable. Les endomorphismes \( d \) et \( n \) commutant, \( {L}_{d},{R}_{d},{L}_{n} \) et \( {R}_{n} \) commutent, donc \( {A}_{d} \) et \( {A}_{n} \) commutent.

> We have \( {A}_{u} = {A}_{d} + {A}_{n} \) . However, there exists \( p \in {\mathbb{N}}^{ * } \) such that \( {n}^{p} = 0 \) , which implies \( {\left( {A}_{n}\right) }^{p} = {A}_{{n}^{p}} = 0 \) , that is to say that \( {A}_{n} \) is nilpotent. According to \( 2/ \) a), \( {A}_{d} \) is diagonalizable. Since the endomorphisms \( d \) and \( n \) commute, \( {L}_{d},{R}_{d},{L}_{n} \) and \( {R}_{n} \) commute, therefore \( {A}_{d} \) and \( {A}_{n} \) commute.

\( {A}_{u} = {A}_{d} + {A}_{n} \) est donc l’unique décomposition de Dunford de \( {A}_{u} \) . Comme \( {A}_{u} \) est diagonali-sable, on a donc \( {A}_{n} = 0 \) , c’est-à-dire que pour tout \( f \in \mathcal{L}\left( E\right) , n \circ f - f \circ n = 0 \) . En d’autres termes, \( n \) commute avec tous les éléments de \( \mathcal{L}\left( E\right) \) ; c’est donc une homothétie. Or \( n \) est nilpotente, donc \( n = 0 \) , et donc \( u = d \) est diagonalisable.

> \( {A}_{u} = {A}_{d} + {A}_{n} \) is therefore the unique Dunford decomposition of \( {A}_{u} \) . Since \( {A}_{u} \) is diagonalizable, we therefore have \( {A}_{n} = 0 \) , that is to say that for all \( f \in \mathcal{L}\left( E\right) , n \circ f - f \circ n = 0 \) . In other words, \( n \) commutes with all elements of \( \mathcal{L}\left( E\right) \) ; it is therefore a homothety. However, \( n \) is nilpotent, so \( n = 0 \) , and therefore \( u = d \) is diagonalizable.

Remarque. Une conséquence de \( 1/ \) a) est que pour tout \( \lambda ,\dim \left( {\operatorname{Ker}\left( {{L}_{u} - \lambda \mathrm{{Id}}}\right) }\right) = \; n\dim \left( {\operatorname{Ker}\left( {u - \lambda \mathrm{{Id}}}\right) }\right) \) . Cette égalité permet également de montrer 1/b).

> Remark. A consequence of \( 1/ \) a) is that for all \( \lambda ,\dim \left( {\operatorname{Ker}\left( {{L}_{u} - \lambda \mathrm{{Id}}}\right) }\right) = \; n\dim \left( {\operatorname{Ker}\left( {u - \lambda \mathrm{{Id}}}\right) }\right) \) . This equality also allows us to show 1/b).

Avec 1/c), on aurait pu démontrer directement 1/a) et 1/b).

> With 1/c), we could have directly demonstrated 1/a) and 1/b).

PROBLÉME 6 (RÉSULTANT DE DEUX POLYNÖMES ET APPLICATION).

> PROBLEM 6 (RESULTANT OF TWO POLYNOMIALS AND APPLICATION).

1/ Résultant de deux polynômes. a) Soient \( P \) et \( Q \) deux polynômes non constants de \( \mathbb{C}\left\lbrack X\right\rbrack \) . Montrer que \( P \) et \( Q \) ont un facteur commun non constant si et seulement si

> 1/ Resultant of two polynomials. a) Let \( P \) and \( Q \) be two non-constant polynomials of \( \mathbb{C}\left\lbrack X\right\rbrack \) . Show that \( P \) and \( Q \) have a non-constant common factor if and only if

\[
\left( {\exists A, B \in  \mathbb{C}\left\lbrack  X\right\rbrack  , A \neq  0, B \neq  0}\right) ,\;{AP} = {BQ}\;\text{ avec }\;\deg \left( A\right)  < \deg \left( Q\right) ,\deg \left( B\right)  < \deg \left( P\right) .
\]

b) Pour tout \( r \in \mathbb{R} \) , on note \( {\Gamma }_{r} = \{ P \in \mathbb{C}\left\lbrack X\right\rbrack \mid \deg P = r\} \) . Pour tout \( m, n \in {\mathbb{N}}^{ * } \) , déterminer une fonction continue

> b) For all \( r \in \mathbb{R} \) , we denote \( {\Gamma }_{r} = \{ P \in \mathbb{C}\left\lbrack X\right\rbrack \mid \deg P = r\} \) . For all \( m, n \in {\mathbb{N}}^{ * } \) , determine a continuous function

\[
R : {\Gamma }_{m} \times  {\Gamma }_{n} \rightarrow  \mathbb{C}\;\left( {P, Q}\right)  \mapsto  R\left\lbrack  {P, Q}\right\rbrack
\]

vérifiant

> satisfying

\[
\left( {P\text{ et }Q\text{ sont premiers entre eux }}\right)  \Leftrightarrow  \left( {R\left\lbrack  {P, Q}\right\rbrack   \neq  0}\right) .
\]

2/ Soit \( n \in \mathbb{N}, n \geq 2 \) . On note \( D \) l’ensemble des matrices diagonalisables de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Quel est \( D \) , l’intérieur de \( D \) ?

> 2/ Let \( n \in \mathbb{N}, n \geq 2 \) . Let \( D \) be the set of diagonalizable matrices of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . What is \( D \) , the interior of \( D \) ?

Solution. 1/ a) Condition nécessaire. Supposons l’existence de \( R \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( R\right) \geq 1 \) , divisant \( P \) et \( Q \) . Soient \( {P}_{1} \) et \( {R}_{1} \in \mathbb{C}\left\lbrack X\right\rbrack \) tels que \( P = R{P}_{1} \) et \( Q = R{Q}_{1} \) . Si \( A = {Q}_{1} \) et \( B = {P}_{1} \) , on a \( {AP} = R{P}_{1}{Q}_{1} = {BQ} \) avec \( \deg \left( A\right) = \deg \left( {Q}_{1}\right) < \deg \left( Q\right) \) et \( \deg \left( B\right) = \deg \left( {P}_{1}\right) < \deg \left( P\right) . \)

> Solution. 1/ a) Necessary condition. Suppose the existence of \( R \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( R\right) \geq 1 \) , dividing \( P \) and \( Q \) . Let \( {P}_{1} \) and \( {R}_{1} \in \mathbb{C}\left\lbrack X\right\rbrack \) be such that \( P = R{P}_{1} \) and \( Q = R{Q}_{1} \) . If \( A = {Q}_{1} \) and \( B = {P}_{1} \) , we have \( {AP} = R{P}_{1}{Q}_{1} = {BQ} \) with \( \deg \left( A\right) = \deg \left( {Q}_{1}\right) < \deg \left( Q\right) \) and \( \deg \left( B\right) = \deg \left( {P}_{1}\right) < \deg \left( P\right) . \)

Condition suffisante. Supposons que \( P \) et \( Q \) n’aient aucun facteur commun non constant, c’est- à-dire que \( P \) et \( Q \) sont premiers entre eux. Si \( {AP} = {BQ} \) , d’après le théorème de Gauss, on a \( P \mid B \) . Comme \( B \neq 0 \) , ceci entraîne deg \( \left( B\right) \geq \deg \left( P\right) \) , ce qui est absurde.

> Sufficient condition. Suppose that \( P \) and \( Q \) have no non-constant common factor, that is to say that \( P \) and \( Q \) are coprime. If \( {AP} = {BQ} \) , according to Gauss's theorem, we have \( P \mid B \) . Since \( B \neq 0 \) , this implies deg \( \left( B\right) \geq \deg \left( P\right) \) , which is absurd.

b) Soit \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{m}{X}^{m} \in {\Gamma }_{m} \) et \( Q = {b}_{0} + {b}_{1}X + \cdots + {b}_{n}{X}^{n} \in {\Gamma }_{n} \) . D’après la question précédente, \( P \) et \( Q \) ont un facteur premier non constant si et seulement il existe \( A, B \in \mathbb{C}\left\lbrack X\right\rbrack \) non nuls, \( \deg \left( A\right) < \deg \left( Q\right) \) et \( \deg \left( B\right) < \deg \left( P\right) \) tels que \( {AP} = {BQ} \) , autrement dit si et seulement si les vecteurs \( P,{XP},\ldots ,{X}^{n - 1}P \) et \( Q,{XQ},\ldots ,{X}^{m - 1}Q \) forment une famille liée de \( \mathbb{C}\left\lbrack X\right\rbrack \) , c’est-à-dire si et seulement si

> b) Let \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{m}{X}^{m} \in {\Gamma }_{m} \) and \( Q = {b}_{0} + {b}_{1}X + \cdots + {b}_{n}{X}^{n} \in {\Gamma }_{n} \) . According to the previous question, \( P \) and \( Q \) have a non-constant prime factor if and only if there exist non-zero \( A, B \in \mathbb{C}\left\lbrack X\right\rbrack \) , \( \deg \left( A\right) < \deg \left( Q\right) \) and \( \deg \left( B\right) < \deg \left( P\right) \) such that \( {AP} = {BQ} \) , in other words if and only if the vectors \( P,{XP},\ldots ,{X}^{n - 1}P \) and \( Q,{XQ},\ldots ,{X}^{m - 1}Q \) form a linearly dependent family of \( \mathbb{C}\left\lbrack X\right\rbrack \) , that is to say if and only if

\[
\mathop{\det }\limits_{\mathcal{B}}\left( {P,{XP},\ldots ,{X}^{n - 1}P, Q,{XQ},\ldots ,{X}^{m - 1}Q}\right)  = 0,
\]

où \( \mathcal{B} \) désigne la base \( \left( {1, X,\ldots ,{X}^{m + n - 1}}\right) \) de \( {\mathbb{C}}_{m + n - 1}\left\lbrack X\right\rbrack \) . En d’autres termes, \( P \) et \( Q \) ne sont pas premiers entre eux si et seulement si le déterminant

> where \( \mathcal{B} \) denotes the basis \( \left( {1, X,\ldots ,{X}^{m + n - 1}}\right) \) of \( {\mathbb{C}}_{m + n - 1}\left\lbrack X\right\rbrack \) . In other words, \( P \) and \( Q \) are not coprime if and only if the determinant

\[
R\left\lbrack  {P, Q}\right\rbrack   = \left| \begin{matrix} {a}_{0} & {a}_{1} & \cdots & {a}_{m} & 0 & \cdots & 0 \\  0 & {a}_{0} & {a}_{1} & \cdots & {a}_{m} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \ddots  & &  \ddots  & 0 \\  0 & \cdots & 0 & {a}_{0} & {a}_{1} & \cdots & {a}_{m} \\  {b}_{0} & \cdots & {b}_{n - 1} & {b}_{n} & 0 & \cdots & 0 \\  0 & {b}_{0} & \cdots & {b}_{n - 1} & {b}_{n} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & &  \ddots  &  \ddots  & 0 \\  0 & \cdots & 0 & {b}_{n} & \cdots & {b}_{m} & {b}_{n} \end{matrix}\right|
\]

est nul (ce déterminant est appelé résultant de \( P \) et \( Q \) ). Ainsi définie sur \( {\Gamma }_{m} \times {\Gamma }_{n}, R \) est une fonction continue de \( P \) et \( Q \) (car polynomiale en les coefficients de \( P \) et \( Q \) ), et vérifie : \( P \) et \( Q \) sont premiers entre eux si et seulement si \( R\left\lbrack {P, Q}\right\rbrack \neq 0 \) .

> is zero (this determinant is called the resultant of \( P \) and \( Q \) ). Thus defined on \( {\Gamma }_{m} \times {\Gamma }_{n}, R \) is a continuous function of \( P \) and \( Q \) (because it is polynomial in the coefficients of \( P \) and \( Q \) ), and satisfies: \( P \) and \( Q \) are coprime if and only if \( R\left\lbrack {P, Q}\right\rbrack \neq 0 \) .

2 / Un peu d’intuition nous guide. Nous allons montrer que \( \overset{ \circ }{D} = \Gamma \) , où \( \Gamma \) désigne l’ensemble des matrices diagonalisables dont les valeurs propres sont toutes distinctes.

> 2 / A little intuition guides us. We will show that \( \overset{ \circ }{D} = \Gamma \) , where \( \Gamma \) denotes the set of diagonalizable matrices whose eigenvalues are all distinct.

Montrons \( \Gamma \subset D \) . Soit \( M \in \Gamma \) . Dire que \( M \in \Gamma \) équivaut à dire que le polynôme caractéris-tique \( {P}_{M} \) de \( M \) n’a que des racines simples, ou encore que \( {P}_{M} \) et \( {P}_{M}^{\prime } \) sont premiers entre eux, ou encore \( R\left\lbrack {{P}_{M},{P}_{M}^{\prime }}\right\rbrack \neq 0 \) . L’application

> Let us show \( \Gamma \subset D \) . Let \( M \in \Gamma \) . Saying that \( M \in \Gamma \) is equivalent to saying that the characteristic polynomial \( {P}_{M} \) of \( M \) has only simple roots, or that \( {P}_{M} \) and \( {P}_{M}^{\prime } \) are coprime, or else \( R\left\lbrack {{P}_{M},{P}_{M}^{\prime }}\right\rbrack \neq 0 \) . The map

\[
\varphi  : {\mathcal{M}}_{n}\left( \mathbb{C}\right)  \rightarrow  \mathbb{C}\;M \mapsto  R\left\lbrack  {{P}_{M},{P}_{M}^{\prime }}\right\rbrack
\]

est continue. On vient de voir que \( \Gamma = {\varphi }^{-1}\left( {\mathbb{C}}^{ * }\right) \) , et donc \( \Gamma \) est ouvert (image réciproque d’un ouvert par une fonction continue). Or \( \Gamma \subset D \) , donc \( \Gamma \subset D \) .

> is continuous. We have just seen that \( \Gamma = {\varphi }^{-1}\left( {\mathbb{C}}^{ * }\right) \) , and thus \( \Gamma \) is open (inverse image of an open set by a continuous function). Now \( \Gamma \subset D \) , so \( \Gamma \subset D \) .

Montrons \( \overset{ \circ }{D} \subset \Gamma \) . Soit \( M \in \overset{ \circ }{D} \) et supposons \( M \notin \Gamma \) . La matrice \( M \) est diagonalisable et admet une valeur propre multiple \( \lambda \) , de sorte qu’il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que

> Let us show \( \overset{ \circ }{D} \subset \Gamma \) . Let \( M \in \overset{ \circ }{D} \) and assume \( M \notin \Gamma \) . The matrix \( M \) is diagonalizable and admits a multiple eigenvalue \( \lambda \) , such that there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) where

\[
{P}^{-1}{MP} = \left( \begin{matrix} X & \left( 0\right) \\  \left( 0\right) & Y \end{matrix}\right) \;\text{ où }\;X = \left( \begin{array}{ll} \lambda & 0 \\  0 & \lambda  \end{array}\right) \;\text{ et }Y\text{ est une matrice diagonale. }
\]

Pour tout entier \( p > 0 \) , on pose

> For every integer \( p > 0 \) , we define

\[
{N}_{p} = \left( \begin{matrix} {X}_{p} & \left( 0\right) \\  \left( 0\right) & Y \end{matrix}\right) \;\text{ où }\;{X}_{p} = \left( \begin{matrix} \lambda & 1/p \\  0 & \lambda  \end{matrix}\right) .
\]

Pour tout \( p,{N}_{p} \) n’est pas diagonalisable, sinon la restriction \( {X}_{p} \) de \( {M}_{p} \) aux deux premiers vecteurs de la base canonique de \( {\mathbb{C}}^{n} \) serait diagonalisable, absurde car alors \( {X}_{p} \) serait semblabe à \( \lambda {I}_{2} \) , donc égale à \( \lambda {I}_{2} \) . Or \( M = \mathop{\lim }\limits_{{p \rightarrow + \infty }}P{N}_{p}{P}^{-1} \) , donc \( M \) est limite d’une suite de matrices n’appartenant pas à \( D \) , donc \( M \notin \overset{ \circ }{D} \) . Ceci est absurde, et on a donc avoir \( M \in \Gamma \) . D’où le résultat.

> For every \( p,{N}_{p} \) is not diagonalizable, otherwise the restriction \( {X}_{p} \) of \( {M}_{p} \) to the first two vectors of the canonical basis of \( {\mathbb{C}}^{n} \) would be diagonalizable, which is absurd because then \( {X}_{p} \) would be similar to \( \lambda {I}_{2} \) , and thus equal to \( \lambda {I}_{2} \) . Now \( M = \mathop{\lim }\limits_{{p \rightarrow + \infty }}P{N}_{p}{P}^{-1} \) , so \( M \) is the limit of a sequence of matrices not belonging to \( D \) , thus \( M \notin \overset{ \circ }{D} \) . This is absurd, and we must therefore have \( M \in \Gamma \) . Hence the result.

Remarque. On peut montrer (voir la démonstration de l’exercice 1 page 195) que \( \Gamma \) est dense dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Remark. One can show (see the proof of exercise 1 on page 195) that \( \Gamma \) is dense in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

Problem 7. Soit \( n \in \mathbb{N}, n \geq 2 \) . 1/ Montrer qu’il n’existe pas de norme \( \parallel \cdot \parallel \) sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) qui soit invariante par similitude, c'est-à-dire telle que

> Problem 7. Let \( n \in \mathbb{N}, n \geq 2 \) . 1/ Show that there is no norm \( \parallel \cdot \parallel \) on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) that is invariant under similarity, that is to say such that

\[
\forall \left( {A, P}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right)  \times  \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) ,\;\begin{Vmatrix}{{P}^{-1}{AP}}\end{Vmatrix} = \parallel A\parallel .
\]

(*)

> 2/ Déterminer les semi-normes sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) invariantes par similitude.

2/ Determine the semi-norms on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) invariant under similarity.

> Solution. 1 / Raisonnons par l'absurde en supposant qu'une telle norme existe. Donnons nous \( i, j \) quelconques tels que \( 1 \leq i, j \leq n \) avec \( i \neq j \) . Choisissons la matrice \( A = {E}_{i, j} \) de la base canonique de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (tous les coefficients de \( {E}_{i, j} \) sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1) et \( P \) la matrice diagonale dont le coefficient d’indice \( \left( {i, i}\right) \) est \( {2}^{i} \) . On a \( {P}^{-1}{E}_{i, j}P = {2}^{j - i}{E}_{i, j} \) , donc \( \begin{Vmatrix}{{P}^{-1}{E}_{i, j}P}\end{Vmatrix} = \begin{Vmatrix}{{2}^{i - j}{E}_{i, j}}\end{Vmatrix} = {2}^{j - i}\begin{Vmatrix}{E}_{i, j}\end{Vmatrix} \) . Si (*) est vérifié ceci entraine \( \begin{Vmatrix}{E}_{i, j}\end{Vmatrix} = \begin{Vmatrix}{{P}^{-1}{E}_{i, j}P}\end{Vmatrix} = \; {2}^{j - i}\begin{Vmatrix}{E}_{i, j}\end{Vmatrix} \) et comme \( i \neq j \) on a forcément \( \begin{Vmatrix}{E}_{i, j}\end{Vmatrix} = 0 \) ce qui est impossible puisque \( {E}_{i, j} \neq 0 \) .

Solution. 1 / Let us reason by contradiction by assuming that such a norm exists. Let \( i, j \) be arbitrary such that \( 1 \leq i, j \leq n \) with \( i \neq j \) . Let us choose the matrix \( A = {E}_{i, j} \) from the canonical basis of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (all coefficients of \( {E}_{i, j} \) are zero except the one with index \( \left( {i, j}\right) \) which is 1) and \( P \) the diagonal matrix whose coefficient with index \( \left( {i, i}\right) \) is \( {2}^{i} \) . We have \( {P}^{-1}{E}_{i, j}P = {2}^{j - i}{E}_{i, j} \) , therefore \( \begin{Vmatrix}{{P}^{-1}{E}_{i, j}P}\end{Vmatrix} = \begin{Vmatrix}{{2}^{i - j}{E}_{i, j}}\end{Vmatrix} = {2}^{j - i}\begin{Vmatrix}{E}_{i, j}\end{Vmatrix} \) . If (*) is satisfied, this implies \( \begin{Vmatrix}{E}_{i, j}\end{Vmatrix} = \begin{Vmatrix}{{P}^{-1}{E}_{i, j}P}\end{Vmatrix} = \; {2}^{j - i}\begin{Vmatrix}{E}_{i, j}\end{Vmatrix} \) and since \( i \neq j \) we necessarily have \( \begin{Vmatrix}{E}_{i, j}\end{Vmatrix} = 0 \) which is impossible since \( {E}_{i, j} \neq 0 \) .

> 2/ Soit \( N \) une semi-norme sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) invariante par similitude. On reprend le raisonnement précédent qui donne \( N\left( {E}_{i, j}\right) = 0 \) dès que \( i \neq j \) . Ainsi pour toute matrice \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , l’écriture \( A = \mathop{\sum }\limits_{{1 \leq i, j \leq n}}{a}_{i, j}{E}_{i, j} \) entraîne, grâce à l’inégalité triangulaire,

2/ Let \( N \) be a semi-norm on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) invariant by similarity. We repeat the previous reasoning which gives \( N\left( {E}_{i, j}\right) = 0 \) as soon as \( i \neq j \) . Thus for any matrix \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , the expression \( A = \mathop{\sum }\limits_{{1 \leq i, j \leq n}}{a}_{i, j}{E}_{i, j} \) implies, thanks to the triangle inequality,

\[
N\left( A\right)  \leq  \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}N\left( {{a}_{i, j}{E}_{i, j}}\right)  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}\left| {a}_{i, j}\right| N\left( {E}_{i, j}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {a}_{i, i}\right| N\left( {E}_{i, i}\right) .
\]

Ainsi si \( A \) a ses coefficients diagonaux nuls, on a \( N\left( A\right) = 0 \) . Il est classique que toute matrice de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) de trace nulle est similaire à une matrice dont tous les coefficients diagonaux sont nuls (voir l’exercice 6 page 131), ainsi pour toute matrice \( A \) de trace nulle on a \( N\left( A\right) = 0 \) . Si \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice quelconque, la matrice \( A = M - \alpha {I}_{n} \) , avec \( \alpha = \operatorname{tr}\left( M\right) /n \) , est de trace nulle, donc \( N\left( M\right) = N\left( {A + \alpha {I}_{n}}\right) \leq N\left( A\right) + N\left( {\alpha {I}_{n}}\right) = N\left( {\alpha {I}_{n}}\right) \) . On a aussi \( N\left( {\alpha {I}_{n}}\right) = \; N\left( {M - A}\right) \leq N\left( M\right) + N\left( A\right) = N\left( M\right) \) , donc \( N\left( M\right) = N\left( {\alpha {I}_{n}}\right) = \left| \alpha \right| N\left( {I}_{n}\right) = \beta \left| {\operatorname{tr}\left( M\right) }\right| \) , avec \( \beta = N\left( {I}_{n}\right) /n \) . Réciproquement, on vérifie facilement que \( M \mapsto \beta \left| {\operatorname{tr}M}\right| \) est une semi-norme invariante par similitude sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) dès que \( \beta \in {\mathbb{R}}^{ + } \) . En synthèse, les semi-normes sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) invariantes par similitude sont de la forme \( N\left( M\right) = \beta \left| {\operatorname{tr}\left( M\right) }\right| \) avec \( \beta \in {\mathbb{R}}^{ + } \) .

> Thus, if \( A \) has zero diagonal coefficients, we have \( N\left( A\right) = 0 \) . It is a classic result that any matrix in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) with zero trace is similar to a matrix whose diagonal coefficients are all zero (see exercise 6 on page 131), so for any matrix \( A \) with zero trace, we have \( N\left( A\right) = 0 \) . If \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is any matrix, the matrix \( A = M - \alpha {I}_{n} \) , with \( \alpha = \operatorname{tr}\left( M\right) /n \) , has zero trace, so \( N\left( M\right) = N\left( {A + \alpha {I}_{n}}\right) \leq N\left( A\right) + N\left( {\alpha {I}_{n}}\right) = N\left( {\alpha {I}_{n}}\right) \) . We also have \( N\left( {\alpha {I}_{n}}\right) = \; N\left( {M - A}\right) \leq N\left( M\right) + N\left( A\right) = N\left( M\right) \) , so \( N\left( M\right) = N\left( {\alpha {I}_{n}}\right) = \left| \alpha \right| N\left( {I}_{n}\right) = \beta \left| {\operatorname{tr}\left( M\right) }\right| \) , with \( \beta = N\left( {I}_{n}\right) /n \) . Conversely, it is easy to verify that \( M \mapsto \beta \left| {\operatorname{tr}M}\right| \) is a similarity-invariant seminorm on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) as soon as \( \beta \in {\mathbb{R}}^{ + } \) . In summary, the similarity-invariant seminorms on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) are of the form \( N\left( M\right) = \beta \left| {\operatorname{tr}\left( M\right) }\right| \) with \( \beta \in {\mathbb{R}}^{ + } \) .

PROBLÉME 8 (RAYON SPECTRAL D'UN ENDOMORPHISME CONTINU). Soit \( E \) une algèbre de Banach sur \( \mathbb{C} \) , munie d’une norme d’algèbre \( \parallel \cdot \parallel \) .

> PROBLEM 8 (SPECTRAL RADIUS OF A CONTINUOUS ENDOMORPHISM). Let \( E \) be a Banach algebra over \( \mathbb{C} \) , equipped with an algebra norm \( \parallel \cdot \parallel \) .

1/ Soit \( u \in E, u \neq 0 \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {U}_{n} = {\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n} \) . a) Soit \( m \in {\mathbb{N}}^{ * } \) fixé. Prouver que

> 1/ Let \( u \in E, u \neq 0 \) . For all \( n \in {\mathbb{N}}^{ * } \) , we denote \( {U}_{n} = {\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n} \) . a) Let \( m \in {\mathbb{N}}^{ * } \) be fixed. Prove that

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall n \geq  N,{U}_{n} \leq  {U}_{m}\left( {1 + \varepsilon }\right) .
\]

b) Soit \( \rho \left( u\right) = \inf \left\{ {{U}_{n} \mid n \in {\mathbb{N}}^{ * }}\right\} \) . Montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{U}_{n} = \rho \left( u\right) \) . c) Pour tout \( u, v \in E \) , montrer que \( \rho \left( {uv}\right) = \rho \left( {vu}\right) \) .

> b) Let \( \rho \left( u\right) = \inf \left\{ {{U}_{n} \mid n \in {\mathbb{N}}^{ * }}\right\} \) . Show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{U}_{n} = \rho \left( u\right) \) . c) For all \( u, v \in E \) , show that \( \rho \left( {uv}\right) = \rho \left( {vu}\right) \) .

2/ Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( R \in \rbrack 0, + \infty \rbrack \) . Soit \( u \in E \) . Si \( \rho \left( u\right) < R \) , montrer que \( \sum {a}_{n}{u}^{n} \) converge dans \( E \) . Si \( \rho \left( u\right) > R \) , montrer que \( \sum {a}_{n}{u}^{n} \) diverge.

> 2/ Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( R \in \rbrack 0, + \infty \rbrack \) . Let \( u \in E \) . If \( \rho \left( u\right) < R \) , show that \( \sum {a}_{n}{u}^{n} \) converges in \( E \) . If \( \rho \left( u\right) > R \) , show that \( \sum {a}_{n}{u}^{n} \) diverges.

3/ On considère ici le cas particulier où \( E = {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer que \( \rho \left( A\right) = \sup \{ \left| \lambda \right| \mid \lambda \) valeur propre de \( A\} \) . (Indication. On pourra utiliser le résultat a) de l'exercice 5 page 198.)

> 3/ We consider here the special case where \( E = {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Show that \( \rho \left( A\right) = \sup \{ \left| \lambda \right| \mid \lambda \) is an eigenvalue of \( A\} \) . (Hint: One may use the result of a) from exercise 5 on page 198.)

Solution. 1/ a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on considère \( n = q\left( n\right) m + r\left( n\right) ,0 \leq r\left( n\right) < m \) , la division euclidienne de \( n \) par \( m \) . On a

> Solution. 1/ a) For all \( n \in {\mathbb{N}}^{ * } \) , consider \( n = q\left( n\right) m + r\left( n\right) ,0 \leq r\left( n\right) < m \) , the Euclidean division of \( n \) by \( m \) . We have

\[
\forall n \in  {\mathbb{N}}^{ * },\;{U}_{n} = {\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n} = {\begin{Vmatrix}{u}^{q\left( n\right) m} \cdot  {u}^{r\left( n\right) }\end{Vmatrix}}^{1/n} \leq  {\begin{Vmatrix}{u}^{m}\end{Vmatrix}}^{q\left( n\right) /n} \cdot  \parallel u{\parallel }^{r\left( n\right) /n}.
\]

(*)

> Pour tout \( n,\left| {r\left( n\right) }\right| < m \) donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}r\left( n\right) /n = 0 \) et \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}q\left( n\right) /n = 1/m \) . Le terme de droite de \( \left( *\right) \) tend donc vers \( {U}_{m} \) lorsque \( n \) tend vers l’infini, d’où a).

For all \( n,\left| {r\left( n\right) }\right| < m \) thus \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}r\left( n\right) /n = 0 \) and \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}q\left( n\right) /n = 1/m \) . The right-hand side of \( \left( *\right) \) therefore tends to \( {U}_{m} \) as \( n \) tends to infinity, hence a).

> b) Soit \( \varepsilon > 0 \) . Par définition de \( \rho \left( u\right) \) , il existe \( m \in {\mathbb{N}}^{ * } \) tel que \( {U}_{m} \leq \rho \left( u\right) + \varepsilon \) . D’après a),

b) Let \( \varepsilon > 0 \) . By definition of \( \rho \left( u\right) \) , there exists \( m \in {\mathbb{N}}^{ * } \) such that \( {U}_{m} \leq \rho \left( u\right) + \varepsilon \) . According to a),

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\;{U}_{n} \leq  {U}_{m}\left( {1 + \varepsilon }\right)  \leq  \left( {\rho \left( u\right)  + \varepsilon }\right) \left( {1 + \varepsilon }\right)
\]

donc

> therefore

\[
\forall n \geq  N,\;\rho \left( u\right)  \leq  {U}_{n} \leq  \left( {\rho \left( u\right)  + \varepsilon }\right) \left( {1 + \varepsilon }\right) .
\]

On en déduit que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{U}_{n} = \rho \left( u\right) \) .

> We deduce that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{U}_{n} = \rho \left( u\right) \) .

c) Si \( u = 0 \) ou \( v = 0 \) , c’est évident. Sinon, l’égalité \( {\left( uv\right) }^{n} = u{\left( vu\right) }^{n - 1}v \) entraîne

> c) If \( u = 0 \) or \( v = 0 \) , it is obvious. Otherwise, the equality \( {\left( uv\right) }^{n} = u{\left( vu\right) }^{n - 1}v \) implies

\[
{\begin{Vmatrix}{\left( uv\right) }^{n}\end{Vmatrix}}^{1/n} = {\begin{Vmatrix}u{\left( vu\right) }^{n - 1}v\end{Vmatrix}}^{1/n} \leq  \parallel u{\parallel }^{1/n}{\begin{Vmatrix}{\left( vu\right) }^{n - 1}\end{Vmatrix}}^{1/n}\parallel v{\parallel }^{1/n}.
\]

\( \left( {* * }\right) \)

> Or \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\parallel u{\parallel }^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\parallel v{\parallel }^{1/n} = 1 \) et \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\begin{Vmatrix}{\left( vu\right) }^{n - 1}\end{Vmatrix}}^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left( {\begin{Vmatrix}{\left( vu\right) }^{n - 1}\end{Vmatrix}}^{1/\left( {n - 1}\right) }\right) }^{\left( {n - 1}\right) /n} = \; \rho \left( {vu}\right) \) . En faisant tendre \( n \) vers l’infini dans \( \left( {* * }\right) \) , on obtient donc \( \rho \left( {uv}\right) \leq \rho \left( {vu}\right) \) . Par symétrie, on a de même \( \rho \left( {vu}\right) \leq \rho \left( {uv}\right) \) , d’ou l’égalité recherchée.

However \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\parallel u{\parallel }^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\parallel v{\parallel }^{1/n} = 1 \) and \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\begin{Vmatrix}{\left( vu\right) }^{n - 1}\end{Vmatrix}}^{1/n} = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left( {\begin{Vmatrix}{\left( vu\right) }^{n - 1}\end{Vmatrix}}^{1/\left( {n - 1}\right) }\right) }^{\left( {n - 1}\right) /n} = \; \rho \left( {vu}\right) \) . By letting \( n \) tend to infinity in \( \left( {* * }\right) \) , we thus obtain \( \rho \left( {uv}\right) \leq \rho \left( {vu}\right) \) . By symmetry, we similarly have \( \rho \left( {vu}\right) \leq \rho \left( {uv}\right) \) , hence the desired equality.

> 2/ Supposons \( \rho \left( u\right) < R \) . Nous allons montrer que \( \sum \left| {a}_{n}\right| \cdot \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converge, ce qui entraînera que la suite \( {\left( \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{u}^{k}\right) }_{n \in {\mathbb{N}}^{ * }} \) est de Cauchy donc converge.

2/ Suppose \( \rho \left( u\right) < R \) . We will show that \( \sum \left| {a}_{n}\right| \cdot \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converges, which will imply that the sequence \( {\left( \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{u}^{k}\right) }_{n \in {\mathbb{N}}^{ * }} \) is Cauchy and therefore converges.

> Soit \( \mu \in \mathbb{R} \) tel que \( \rho \left( u\right) < \mu < R \) . Comme \( R \) est le rayon de convergence de la série entière \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n},\sum \left| {a}_{n}\right| {\mu }^{n} \) converge (voir le tome d’analyse sur les séries entières). Or il existe \( N \in {\mathbb{N}}^{ * } \) , tel que pour tout \( n \geq N,{\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n} < \mu \) , et donc \( \begin{Vmatrix}{u}^{n}\end{Vmatrix} < {\mu }^{n} \) . On en déduit que \( \mathop{\sum }\limits_{{n > N}}\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converge et donc \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converge.

Let \( \mu \in \mathbb{R} \) be such that \( \rho \left( u\right) < \mu < R \) . Since \( R \) is the radius of convergence of the power series \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n},\sum \left| {a}_{n}\right| {\mu }^{n} \) converges (see the analysis volume on power series). However, there exists \( N \in {\mathbb{N}}^{ * } \) such that for all \( n \geq N,{\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n} < \mu \) , and thus \( \begin{Vmatrix}{u}^{n}\end{Vmatrix} < {\mu }^{n} \) . We deduce from this that \( \mathop{\sum }\limits_{{n > N}}\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converges and therefore \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix} \) converges.

> Supposons maintenant \( \rho \left( u\right) > R \) . Alors la suite \( \left( {\left| {a}_{n}\right| \rho {\left( u\right) }^{n}}\right) \) n’est pas bornée. Comme \( \rho \left( u\right) = \; \inf \left\{ {\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n}\right\} \) on a pour tout \( n,\begin{Vmatrix}{u}^{n}\end{Vmatrix} \geq \rho {\left( u\right) }^{n} \) et donc la suite \( \left( {\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix}}\right) \) n’est pas bornée, ce qui entraîne la divergence de la série \( \sum {a}_{n}{u}^{n} \) .

Now suppose \( \rho \left( u\right) > R \) . Then the sequence \( \left( {\left| {a}_{n}\right| \rho {\left( u\right) }^{n}}\right) \) is not bounded. Since \( \rho \left( u\right) = \; \inf \left\{ {\begin{Vmatrix}{u}^{n}\end{Vmatrix}}^{1/n}\right\} \) we have for all \( n,\begin{Vmatrix}{u}^{n}\end{Vmatrix} \geq \rho {\left( u\right) }^{n} \) and thus the sequence \( \left( {\left| {a}_{n}\right| \begin{Vmatrix}{u}^{n}\end{Vmatrix}}\right) \) is not bounded, which leads to the divergence of the series \( \sum {a}_{n}{u}^{n} \) .

> 3 / Notons \( \mu \left( A\right) = \sup \{ \left| \lambda \right| \mid \lambda \) valeur propre de \( A\} \) . Remarquons ici que \( \rho \left( A\right) \) ne dépend pas de la norme d’algèbre choisie sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) (en effet, en dimension finie, les normes sont équivalentes et pour tout \( x > 0,\mathop{\lim }\limits_{{p \rightarrow + \infty }}{x}^{1/p} = 1 \) ). Toute l’astuce va consister en le choix d’une bonne norme d'algèbre pour montrer notre résultat.

3/ Let \( \mu \left( A\right) = \sup \{ \left| \lambda \right| \mid \lambda \) be an eigenvalue of \( A\} \) . Note here that \( \rho \left( A\right) \) does not depend on the algebra norm chosen on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) (indeed, in finite dimension, norms are equivalent and for all \( x > 0,\mathop{\lim }\limits_{{p \rightarrow + \infty }}{x}^{1/p} = 1 \) ). The whole trick will consist of choosing a good algebra norm to show our result.

> Soit \( \varepsilon > 0 \) . Montrons qu’il existe une norme d’algèbre \( \parallel \cdot \parallel \) sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) telle que \( \parallel A\parallel \leq \mu \left( A\right) + \varepsilon \) . Munissons \( {\mathbb{C}}^{n} \) de la norme \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) . Pour tout \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , \( \parallel M{\parallel }_{\infty } = \mathop{\sup }\limits_{{\parallel X{\parallel }_{\infty } = 1}}\parallel {MX}{\parallel }_{\infty } \) définit une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Un petit calcul donne d'ailleurs facilement

Let \( \varepsilon > 0 \) . Let us show that there exists an algebra norm \( \parallel \cdot \parallel \) on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( \parallel A\parallel \leq \mu \left( A\right) + \varepsilon \) . Equip \( {\mathbb{C}}^{n} \) with the norm \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) . For any \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , \( \parallel M{\parallel }_{\infty } = \mathop{\sup }\limits_{{\parallel X{\parallel }_{\infty } = 1}}\parallel {MX}{\parallel }_{\infty } \) defines an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . A short calculation easily gives

\[
\parallel M{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left( {\mathop{\sum }\limits_{j}\left| {m}_{i, j}\right| }\right) .
\]

\( \left( {* * * }\right) \)

> D’après la question a) de l’exercice 5 page 198, il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( {P}^{-1}{AP} = T = \left( {t}_{i, j}\right) \) soit triangulaire supérieure et vérifie \( \forall i < j,\left| {t}_{i, j}\right| < \varepsilon /n \) . Munissons \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) de la norme d’algèbre \( \parallel M\parallel = {\begin{Vmatrix}{P}^{-1}MP\end{Vmatrix}}_{\infty } \) . De (***), on tire facilement \( \parallel A\parallel = \parallel T{\parallel }_{\infty } < \mathop{\sup }\limits_{i}\left| {t}_{i, i}\right| + \varepsilon \) . Les \( {t}_{i, i} \) étant les valeurs propres de \( T \) donc de \( A \) , ceci s’écrit aussi \( \parallel A\parallel < \mu \left( A\right) + \varepsilon \) . Donc

According to question a) of exercise 5 on page 198, there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( {P}^{-1}{AP} = T = \left( {t}_{i, j}\right) \) is upper triangular and satisfies \( \forall i < j,\left| {t}_{i, j}\right| < \varepsilon /n \) . Equip \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) with the algebra norm \( \parallel M\parallel = {\begin{Vmatrix}{P}^{-1}MP\end{Vmatrix}}_{\infty } \) . From (***), we easily derive \( \parallel A\parallel = \parallel T{\parallel }_{\infty } < \mathop{\sup }\limits_{i}\left| {t}_{i, i}\right| + \varepsilon \) . Since the \( {t}_{i, i} \) are the eigenvalues of \( T \) and thus of \( A \) , this can also be written as \( \parallel A\parallel < \mu \left( A\right) + \varepsilon \) . Therefore

\[
\rho \left( A\right)  = \left\{  {\inf {\begin{Vmatrix}{A}^{p}\end{Vmatrix}}^{1/p}, p \in  {\mathbb{N}}^{ * }}\right\}   \leq  \parallel A\parallel  < \mu \left( A\right)  + \varepsilon .
\]

La matrice \( T = \left( {t}_{i, j}\right) \) étant triangulaire supérieure, les coefficients de la diagonale principale de la matrice \( {T}^{p} \) sont les \( {t}_{i, i}^{p} \) et donc d’après (***), pour tout \( p \) ,

> Since the matrix \( T = \left( {t}_{i, j}\right) \) is upper triangular, the coefficients of the main diagonal of the matrix \( {T}^{p} \) are the \( {t}_{i, i}^{p} \) and thus, according to (***), for any \( p \) ,

\[
\begin{Vmatrix}{A}^{p}\end{Vmatrix} = {\begin{Vmatrix}{T}^{p}\end{Vmatrix}}_{\infty } \geq  \mathop{\sup }\limits_{i}{\left| {t}_{i, i}\right| }^{p} = \mu {\left( A\right) }^{p},
\]

ce qui s’écrit aussi \( {\begin{Vmatrix}{A}^{p}\end{Vmatrix}}^{1/p} \geq \mu \left( A\right) \) . En faisant tendre \( p \) vers l’infini. on obtient \( \rho \left( A\right) \geq \mu \left( A\right) \) .

> which can also be written as \( {\begin{Vmatrix}{A}^{p}\end{Vmatrix}}^{1/p} \geq \mu \left( A\right) \) . By letting \( p \) tend to infinity, we obtain \( \rho \left( A\right) \geq \mu \left( A\right) \) .

Finalement, on a montré que \( \mu \left( A\right) \leq \rho \left( A\right) \leq \mu \left( A\right) + \varepsilon \) , et ceci pour tout \( \varepsilon > 0 \) , d’où l’égalité recherchée.

> Finally, we have shown that \( \mu \left( A\right) \leq \rho \left( A\right) \leq \mu \left( A\right) + \varepsilon \) , and this for any \( \varepsilon > 0 \) , hence the sought equality.

Remarque. Les résultats de 1/ et 2/ restent vrais sur l'algèbre des endomorphismes continus \( {\mathcal{L}}_{c}\left( E\right) \) sur un espace de Banach \( E \) (on sait en effet que \( {\mathcal{L}}_{c}\left( E\right) \) est une algèbre de Banach). On a ainsi généralisé le résultat de la proposition 3 page 193.

> Remark. The results of 1/ and 2/ remain true on the algebra of continuous endomorphisms \( {\mathcal{L}}_{c}\left( E\right) \) on a Banach space \( E \) (we know indeed that \( {\mathcal{L}}_{c}\left( E\right) \) is a Banach algebra). We have thus generalized the result of proposition 3 on page 193.

Problem 9. 1 / Soit \( A \) une \( \mathbb{K} \) -algèbre de dimension finie. Montrer qu’il existe \( d \in {\mathbb{N}}^{ * } \) tel que \( A \) est isomorphe à une sous-algèbre de \( {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) .

> Problem 9. 1/ Let \( A \) be a finite-dimensional \( \mathbb{K} \) -algebra. Show that there exists \( d \in {\mathbb{N}}^{ * } \) such that \( A \) is isomorphic to a subalgebra of \( {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) .

2/ Soit \( n \in {\mathbb{N}}^{ * } \) et \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) possédant \( n \) valeurs propres distinctes. Montrer qu’il n’existe qu’un nombre fini de sous-algèbres de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) contenant \( M \) .

> 2/ Let \( n \in {\mathbb{N}}^{ * } \) and \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) possess \( n \) distinct eigenvalues. Show that there are only a finite number of subalgebras of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) containing \( M \) .

Solution. 1/ A tout élément \( a \in A \) , on associe l’application \( \varphi \left( a\right) : A \rightarrow A,\;x \mapsto {ax} \) . On a \( \varphi \left( a\right) \in \mathcal{L}\left( A\right) \) , et l’application \( \varphi \) ainsi définie est linéaire de \( A \) vers \( \mathcal{L}\left( A\right) \) . De plus, pour tout \( a, b \in A \) on a

> Solution. 1/ To every element \( a \in A \) , we associate the map \( \varphi \left( a\right) : A \rightarrow A,\;x \mapsto {ax} \) . We have \( \varphi \left( a\right) \in \mathcal{L}\left( A\right) \) , and the map \( \varphi \) thus defined is linear from \( A \) to \( \mathcal{L}\left( A\right) \) . Furthermore, for every \( a, b \in A \) we have

\[
\forall x \in  A,\varphi \left( {ab}\right) \left( x\right)  = \left( {ab}\right) x = {a\varphi }\left( b\right) \left( x\right)  = \varphi \left( a\right) \varphi \left( b\right) \left( x\right)
\]

donc \( \varphi \left( {ab}\right) = \varphi \left( a\right) \varphi \left( b\right) \) . Ainsi \( \varphi \) est un morphisme d’algèbre. Il est injectif car si \( \varphi \left( a\right) = 0 \) , on a nécéssairement \( 0 = \varphi \left( a\right) \left( {1}_{A}\right) = a \) . Choisissons une base \( B = \left( {{e}_{1},\ldots ,{e}_{d}}\right) \) de \( A \) , où \( d \) est la dimension de \( A \) . L’application \( \psi : A \rightarrow {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) définie par \( \psi \left( a\right) = {\left\lbrack \varphi \left( a\right) \right\rbrack }_{B} \) (matrice de \( \varphi \left( a\right) \) dans la base \( B \) ) est un morphisme d’algèbre, injectif, et \( C = \operatorname{Im}\left( \psi \right) = \psi \left( A\right) \) est une sous-algèbre de \( {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) . Ainsi \( \psi \) est un isomorphisme d’algèbre de \( A \) vers \( C \) .

> therefore \( \varphi \left( {ab}\right) = \varphi \left( a\right) \varphi \left( b\right) \) . Thus \( \varphi \) is an algebra morphism. It is injective because if \( \varphi \left( a\right) = 0 \) , we necessarily have \( 0 = \varphi \left( a\right) \left( {1}_{A}\right) = a \) . Let us choose a basis \( B = \left( {{e}_{1},\ldots ,{e}_{d}}\right) \) of \( A \) , where \( d \) is the dimension of \( A \) . The map \( \psi : A \rightarrow {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) defined by \( \psi \left( a\right) = {\left\lbrack \varphi \left( a\right) \right\rbrack }_{B} \) (matrix of \( \varphi \left( a\right) \) in the basis \( B \) ) is an injective algebra morphism, and \( C = \operatorname{Im}\left( \psi \right) = \psi \left( A\right) \) is a subalgebra of \( {\mathcal{M}}_{d}\left( \mathbb{K}\right) \) . Thus \( \psi \) is an algebra isomorphism from \( A \) to \( C \) .

2/ Les \( n \) valeurs propres de \( M \) étant distinctes, \( M \) est diagonalisable. Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( M = {P}^{-1}{DP} \) , où \( D \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est une matrice diagonale, dont nous notons \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) ses termes diagonaux. Nous allons montrer qu’il n’y a qu’un nombre fini de sous-algèbres de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) contenant contenant \( D \) , on conclura facilement pour \( M \) . Soit \( A \) une sous-algèbre de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) contenant \( D \) . Notons \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) la base canonique de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \left( {{E}_{i, j}\text{ est la matrice }n \times n}\right. \) dont tous les coefficients sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1). Comme \( D \in A \) et que \( A \) est une algèbre, tout polynôme en \( D \) est dans \( A \) . Choisissons en particulier les polynômes d’interpolation de Lagrange définis par \( {L}_{i}\left( X\right) = \mathop{\prod }\limits_{{j \neq i}}\left( {X - {\lambda }_{j}}\right) /\left( {{\lambda }_{i} - {\lambda }_{j}}\right) \) et qui vérifient \( {L}_{i}\left( {\lambda }_{j}\right) = 0 \) si \( j \neq i, = 1 \) si \( j = i \) . On a \( {L}_{i}\left( D\right) = {E}_{i, i} \) , dont \( {E}_{i, i} \in A \) pour \( 1 \leq i \leq n \) . Pour toute matrice \( N \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , notons \( N\left( {i, j}\right) \) son coefficient d’indice \( \left( {i, j}\right) \) . Supposons maintenant \( i \neq j \) et qu’il existe une matrice \( N \in A \) tel que \( N\left( {i, j}\right) \neq 0 \) . Alors \( {E}_{i, j} = \left( {1/N\left( {i, j}\right) }\right) {E}_{i, i}N{E}_{j, j} \in A \) . Ainsi, l’ensemble d’indices \( \Gamma = \{ \left( {i, j}\right) \mid \exists N \in A, N\left( {i, j}\right) \neq 0\} \) vérifie la propriété \( \left( {i, j}\right) \in \Gamma \Leftrightarrow {E}_{i, j} \in A \) (c’est vrai aussi si \( i = j \) car on a vu plus haut que les \( {E}_{i, i} \) sont dans \( A \) ). Comme \( A \) est une algèbre on en déduit \( A = \operatorname{Vect}{\left( {E}_{i, j}\right) }_{\left( {i, j}\right) \in \Gamma } \) . Comme il n’y a qu’un nombre fini de parties \( \Gamma \) de \( \{ 1,\ldots , n{\} }^{2} \) , on en déduit qu’il n’y a qu’un nombre fini de sous-algèbres \( A \) de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) qui contiennent \( D \) .

> 2/ Since the \( n \) eigenvalues of \( M \) are distinct, \( M \) is diagonalizable. Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) be such that \( M = {P}^{-1}{DP} \), where \( D \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is a diagonal matrix, whose diagonal terms we denote by \( {\lambda }_{1},\ldots ,{\lambda }_{n} \). We will show that there is only a finite number of subalgebras of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) containing \( D \), from which we will easily conclude for \( M \). Let \( A \) be a subalgebra of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) containing \( D \). Let \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) denote the canonical basis of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \left( {{E}_{i, j}\text{ est la matrice }n \times n}\right. \) (all of whose coefficients are zero except for the one with index \( \left( {i, j}\right) \), which is 1). Since \( D \in A \) and \( A \) is an algebra, any polynomial in \( D \) is in \( A \). In particular, let us choose the Lagrange interpolation polynomials defined by \( {L}_{i}\left( X\right) = \mathop{\prod }\limits_{{j \neq i}}\left( {X - {\lambda }_{j}}\right) /\left( {{\lambda }_{i} - {\lambda }_{j}}\right) \) and which satisfy \( {L}_{i}\left( {\lambda }_{j}\right) = 0 \) if \( j \neq i, = 1 \) if \( j = i \). We have \( {L}_{i}\left( D\right) = {E}_{i, i} \), of which \( {E}_{i, i} \in A \) for \( 1 \leq i \leq n \). For any matrix \( N \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), let \( N\left( {i, j}\right) \) denote its coefficient with index \( \left( {i, j}\right) \). Now suppose \( i \neq j \) and that there exists a matrix \( N \in A \) such that \( N\left( {i, j}\right) \neq 0 \). Then \( {E}_{i, j} = \left( {1/N\left( {i, j}\right) }\right) {E}_{i, i}N{E}_{j, j} \in A \). Thus, the set of indices \( \Gamma = \{ \left( {i, j}\right) \mid \exists N \in A, N\left( {i, j}\right) \neq 0\} \) satisfies the property \( \left( {i, j}\right) \in \Gamma \Leftrightarrow {E}_{i, j} \in A \) (this is also true if \( i = j \) because we saw above that the \( {E}_{i, i} \) are in \( A \)). Since \( A \) is an algebra, we deduce \( A = \operatorname{Vect}{\left( {E}_{i, j}\right) }_{\left( {i, j}\right) \in \Gamma } \). As there is only a finite number of subsets \( \Gamma \) of \( \{ 1,\ldots , n{\} }^{2} \), we deduce that there is only a finite number of subalgebras \( A \) of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) that contain \( D \).

Revenons maintenant à la question initiale. Comme l’application \( \theta : N \mapsto {PN}{P}^{-1} \) est un automorphisme d’algèbre de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) , B \) est une sous-algèbre de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) contenant \( M \) si et seulement si \( A = {PB}{P}^{-1} = \theta \left( B\right) \) est une sous-algèbre contenant \( D \) , donc il n’y a qu’un nombre fini de sous-algèbres \( B \) de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) contenant \( M \) .

> Let us now return to the initial question. Since the map \( \theta : N \mapsto {PN}{P}^{-1} \) is an algebra automorphism of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) , B \) is a subalgebra of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) containing \( M \) if and only if \( A = {PB}{P}^{-1} = \theta \left( B\right) \) is a subalgebra containing \( D \), therefore there is only a finite number of subalgebras \( B \) of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) containing \( M \).

Problem 10. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie \( n \geq 2 \) . Soit \( A \) une sous-algèbre de \( \mathcal{L}\left( E\right) \) , unitaire,(i.e. \( {\operatorname{Id}}_{E} \in A \) ) et transitive (i.e. les seuls s.e.v de \( E \) stables par tous les éléments de \( A \) sont \( \{ 0\} \) et \( E \) ).

> Problem 10. Let \( E \) be a finite-dimensional \( \mathbb{C} \) -vector space \( n \geq 2 \) . Let \( A \) be a unital subalgebra of \( \mathcal{L}\left( E\right) \) (i.e. \( {\operatorname{Id}}_{E} \in A \) ) and transitive (i.e. the only subspaces of \( E \) stable under all elements of \( A \) are \( \{ 0\} \) and \( E \) ).

a) Soit \( x \in E, x \neq 0 \) . Montrer que \( \{ u\left( x\right) \mid u \in A\} = E \) .

> a) Let \( x \in E, x \neq 0 \) . Show that \( \{ u\left( x\right) \mid u \in A\} = E \) .

b) Soit \( u \in A,\operatorname{rg}u \geq 2 \) . Montrer qu’il existe \( v \in A \) tel que \( {uvu} \) et \( u \) forment une famille libre.

> b) Let \( u \in A,\operatorname{rg}u \geq 2 \) . Show that there exists \( v \in A \) such that \( {uvu} \) and \( u \) form a linearly independent family.

c) Montrer qu’il existe \( \lambda \in \mathbb{C} \) et \( z \in \operatorname{Im}u, z \neq 0 \) , tels que \( {uv}\left( z\right) = {\lambda z} \) .

> c) Show that there exist \( \lambda \in \mathbb{C} \) and \( z \in \operatorname{Im}u, z \neq 0 \) such that \( {uv}\left( z\right) = {\lambda z} \) .

d) Montrer que \( A \) contient au moins un élément de rang 1.

> d) Show that \( A \) contains at least one element of rank 1.

Conclure.

> Conclude.

Solution. a) On pose \( {F}_{x} = \{ u\left( x\right) \mid u \in A\} \) . Une sous-algèbre est un s.e.v de \( \mathcal{L}\left( E\right) \) , donc \( A \) est un s.e.v de \( \mathcal{L}\left( E\right) \) . On en déduit que \( {F}_{x} \) est un s.e.v de \( E \) .

> Solution. a) Let \( {F}_{x} = \{ u\left( x\right) \mid u \in A\} \) . A subalgebra is a subspace of \( \mathcal{L}\left( E\right) \) , so \( A \) is a subspace of \( \mathcal{L}\left( E\right) \) . We deduce that \( {F}_{x} \) is a subspace of \( E \) .

Pour tout \( v \in A, v\left( {F}_{x}\right) = \{ {vu}\left( x\right) \mid u \in A\} \subset {F}_{x} \) . En d’autres termes, \( {F}_{x} \) est stable par tous les éléments de \( A \) . Or \( {F}_{x} \neq \{ 0\} \) puisque \( x \in {F}_{x} \) (l’algèbre \( A \) est unitaire), et donc \( {F}_{x} = E \) .

> For all \( v \in A, v\left( {F}_{x}\right) = \{ {vu}\left( x\right) \mid u \in A\} \subset {F}_{x} \) . In other words, \( {F}_{x} \) is stable under all elements of \( A \) . However, \( {F}_{x} \neq \{ 0\} \) since \( x \in {F}_{x} \) (the algebra \( A \) is unital), and thus \( {F}_{x} = E \) .

b) Comme \( \operatorname{rg}u \geq 2 \) , il existe deux vecteurs \( {e}_{1},{e}_{2} \) de \( E \) tels que \( u\left( {e}_{1}\right) \) et \( u\left( {e}_{2}\right) \) forment une famille libre. En particulier, \( u\left( {e}_{1}\right) \neq 0 \) donc d’après a), il existe \( v \in A \) tel que \( v\left\lbrack {u\left( {e}_{1}\right) }\right\rbrack = {e}_{2} \) . La famille formée par \( {uvu} \) et \( u \) est donc libre car l’égalité \( \lambda \left( {uvu}\right) + {\mu u} = 0 \) entraîne \( \lambda \left( {uvu}\right) \left( {e}_{1}\right) + {\mu u}\left( {e}_{1}\right) = \; 0 = {\lambda u}\left( {e}_{2}\right) + {\mu u}\left( {e}_{1}\right) \) , et donc \( \lambda = \mu = 0 \) puisque par construction, la famille \( u\left( {e}_{1}\right) , u\left( {e}_{2}\right) \) est libre. c) Le corps \( \mathbb{C} \) est algébriquement clos et \( E \) est de dimension finie, l’endomorphisme \( {uv} \) admet donc au moins une valeur propre \( \lambda \) . On traite deux cas.

> b) Since \( \operatorname{rg}u \geq 2 \) , there exist two vectors \( {e}_{1},{e}_{2} \) of \( E \) such that \( u\left( {e}_{1}\right) \) and \( u\left( {e}_{2}\right) \) form a linearly independent family. In particular, \( u\left( {e}_{1}\right) \neq 0 \) so according to a), there exists \( v \in A \) such that \( v\left\lbrack {u\left( {e}_{1}\right) }\right\rbrack = {e}_{2} \) . The family formed by \( {uvu} \) and \( u \) is therefore linearly independent because the equality \( \lambda \left( {uvu}\right) + {\mu u} = 0 \) implies \( \lambda \left( {uvu}\right) \left( {e}_{1}\right) + {\mu u}\left( {e}_{1}\right) = \; 0 = {\lambda u}\left( {e}_{2}\right) + {\mu u}\left( {e}_{1}\right) \) , and thus \( \lambda = \mu = 0 \) since by construction, the family \( u\left( {e}_{1}\right) , u\left( {e}_{2}\right) \) is linearly independent. c) The field \( \mathbb{C} \) is algebraically closed and \( E \) is of finite dimension, the endomorphism \( {uv} \) therefore admits at least one eigenvalue \( \lambda \) . We consider two cases.

Premier cas : l’endomorphisme \( {uv} \) admet au moins une valeur propre \( \lambda \neq 0 \) associé à un vecteur propre \( z \neq 0 \) . Alors \( z = \frac{1}{\lambda }{uv}\left( z\right) \in \operatorname{Im}u \) et le résultat est montré.

> First case: the endomorphism \( {uv} \) admits at least one eigenvalue \( \lambda \neq 0 \) associated with an eigenvector \( z \neq 0 \) . Then \( z = \frac{1}{\lambda }{uv}\left( z\right) \in \operatorname{Im}u \) and the result is shown.

Second cas : toutes les valeurs propres de \( {uv} \) sont nulles. Dans ce cas, \( {uv} \) est nilpotent. Soit \( r \in {\mathbb{N}}^{ * } \) tel que \( {\left( uv\right) }^{r} = 0 \) et \( {\left( uv\right) }^{r - 1} \neq 0 \) . Soit \( z \in \operatorname{Im}{\left( uv\right) }^{r - 1}, z \neq 0 \) . Alors \( {uv}\left( z\right) = 0 \) car \( {uv}\left( z\right) \in \operatorname{Im}{\left( uv\right) }^{r} = \{ 0\} \) . Or \( r \geq 2 \) car d’après b), \( {uv} \neq 0 \) . Donc \( z \in \operatorname{Im}{\left( uv\right) }^{r - 1} \subset \operatorname{Im}u \) . En résumé, on a trouvé \( z \in \operatorname{Im}u, z \neq 0 \) , tel que \( {uv}\left( z\right) = 0 \) . d) L’algèbre \( A \) étant unitaire, il existe \( u \in A \) tel que \( \operatorname{rg}u \geq 2 \) . On a alors trouvé \( v \in A, v \neq 0 \) tel que \( {uvu} \) et \( u \) forment une famille libre, et tel que \( \left( {\exists z \in \operatorname{Im}u, z \neq 0,\exists \lambda \in \mathbb{C}}\right) ,\;{uv}\left( z\right) = {\lambda z} \) . Posons \( w = {uvu} - {\lambda u} \) . On a \( w \in A \) car \( A \) est une algèbre, et \( w \neq 0 \) d’après b).

> Second case: all eigenvalues of \( {uv} \) are zero. In this case, \( {uv} \) is nilpotent. Let \( r \in {\mathbb{N}}^{ * } \) be such that \( {\left( uv\right) }^{r} = 0 \) and \( {\left( uv\right) }^{r - 1} \neq 0 \) . Let \( z \in \operatorname{Im}{\left( uv\right) }^{r - 1}, z \neq 0 \) . Then \( {uv}\left( z\right) = 0 \) because \( {uv}\left( z\right) \in \operatorname{Im}{\left( uv\right) }^{r} = \{ 0\} \) . However, \( r \geq 2 \) because according to b), \( {uv} \neq 0 \) . Thus \( z \in \operatorname{Im}{\left( uv\right) }^{r - 1} \subset \operatorname{Im}u \) . In summary, we have found \( z \in \operatorname{Im}u, z \neq 0 \) such that \( {uv}\left( z\right) = 0 \) . d) Since the algebra \( A \) is unital, there exists \( u \in A \) such that \( \operatorname{rg}u \geq 2 \) . We have then found \( v \in A, v \neq 0 \) such that \( {uvu} \) and \( u \) form a linearly independent family, and such that \( \left( {\exists z \in \operatorname{Im}u, z \neq 0,\exists \lambda \in \mathbb{C}}\right) ,\;{uv}\left( z\right) = {\lambda z} \) . Let \( w = {uvu} - {\lambda u} \) . We have \( w \in A \) because \( A \) is an algebra, and \( w \neq 0 \) according to b).

On a Ker \( u \subset \operatorname{Ker}w \) car \( w = \left( {{uv} - \lambda \operatorname{Id}}\right) \circ u \) . Par ailleurs si \( y \in E \) est tel que \( z = u\left( y\right) \) , on a \( w\left( y\right) = {uv}\left( z\right) - {\lambda z} = 0 \) . L’inclusion Ker \( u \subset \operatorname{Ker}w \) est donc stricte, car \( y \notin \operatorname{Ker}u \) et \( y \in \operatorname{Ker}w \) . Donc dim(Ker \( u) < \dim \left( {\operatorname{Ker}w}\right) \) , et on conclue avec le théorème du rang que \( \operatorname{rg}w < \operatorname{rg}u \) .

> We have Ker \( u \subset \operatorname{Ker}w \) because \( w = \left( {{uv} - \lambda \operatorname{Id}}\right) \circ u \) . Furthermore, if \( y \in E \) is such that \( z = u\left( y\right) \) , we have \( w\left( y\right) = {uv}\left( z\right) - {\lambda z} = 0 \) . The inclusion Ker \( u \subset \operatorname{Ker}w \) is therefore strict, because \( y \notin \operatorname{Ker}u \) and \( y \in \operatorname{Ker}w \) . Thus dim(Ker \( u) < \dim \left( {\operatorname{Ker}w}\right) \) , and we conclude with the rank-nullity theorem that \( \operatorname{rg}w < \operatorname{rg}u \) .

Autrement dit, pour tout \( u \in A,\operatorname{rg}u \geq 2 \) , il existe \( w \in A,1 \leq \operatorname{rg}w \leq \operatorname{rg}u - 1 \) . Ceci suffit pour conclure que \( A \) contient au moins un élément de rang 1.

> In other words, for all \( u \in A,\operatorname{rg}u \geq 2 \) , there exists \( w \in A,1 \leq \operatorname{rg}w \leq \operatorname{rg}u - 1 \) . This is sufficient to conclude that \( A \) contains at least one element of rank 1.

e) On va montrer que \( A = \mathcal{L}\left( E\right) \) . Pour cela, il suffit de montrer que \( A \) contient tous les éléments de \( \mathcal{L}\left( E\right) \) de rang 1 . Le lemme suivant nous sera utile.

> e) We will show that \( A = \mathcal{L}\left( E\right) \) . To do this, it suffices to show that \( A \) contains all elements of \( \mathcal{L}\left( E\right) \) of rank 1. The following lemma will be useful to us.

LEMME Soit \( u \in \mathcal{L}\left( E\right) ,\operatorname{rg}u = 1 \) . Alors il existe \( a \in E, a \neq 0 \) , et il existe

> LEMMA Let \( u \in \mathcal{L}\left( E\right) ,\operatorname{rg}u = 1 \) . Then there exists \( a \in E, a \neq 0 \) , and there exists

\[
\varphi  \in  {E}^{ * }\text{ (dual de }E\text{ ), }\varphi  \neq  0\text{ , tels que }\forall x \in  E, u\left( x\right)  = \varphi \left( x\right)  \cdot  a\text{ . }
\]

En effet. Soit \( a \in E \) tel que \( \operatorname{Im}u = \operatorname{Vect}a \) . Pour tout \( x \in E, u\left( x\right) \in \operatorname{Im}u \) donc il existe \( \varphi \left( x\right) \in \mathbb{C} \) tel que \( u\left( x\right) = \varphi \left( x\right) \cdot a \) . La linéarité de \( u \) entraîne la linéarité de \( x \mapsto \varphi \left( x\right) \) . Autrement dit, \( \varphi \) est une application linéaire de \( E \) dans \( \mathbb{C} \) , c’est-à-dire \( \varphi \in {E}^{ * } \) .

> Indeed. Let \( a \in E \) be such that \( \operatorname{Im}u = \operatorname{Vect}a \) . For all \( x \in E, u\left( x\right) \in \operatorname{Im}u \) , there exists \( \varphi \left( x\right) \in \mathbb{C} \) such that \( u\left( x\right) = \varphi \left( x\right) \cdot a \) . The linearity of \( u \) implies the linearity of \( x \mapsto \varphi \left( x\right) \) . In other words, \( \varphi \) is a linear map from \( E \) to \( \mathbb{C} \) , that is to say \( \varphi \in {E}^{ * } \) .

Ceci étant, la question précédente assure l’existence de \( {u}_{0} \in A \) tel que \( \operatorname{rg}{u}_{0} = 1 \) . D’après notre lemme, il existe \( a \in E, a \neq 0 \) et \( \varphi \in {E}^{ * },\varphi \neq 0 \) , tels que \( {u}_{0} = \varphi \cdot a \) . Soit \( v \in \mathcal{L}\left( E\right) \) un autre élément de rang 1. On veut montrer \( v \in A \) . Écrivons \( v = \psi \cdot b \) , où \( b \in E \) et \( \psi \in {E}^{ * } \) .

> That being said, the previous question ensures the existence of \( {u}_{0} \in A \) such that \( \operatorname{rg}{u}_{0} = 1 \) . According to our lemma, there exist \( a \in E, a \neq 0 \) and \( \varphi \in {E}^{ * },\varphi \neq 0 \) such that \( {u}_{0} = \varphi \cdot a \) . Let \( v \in \mathcal{L}\left( E\right) \) be another element of rank 1. We want to show \( v \in A \) . Let us write \( v = \psi \cdot b \) , where \( b \in E \) and \( \psi \in {E}^{ * } \) .

On a \( a \neq 0 \) donc d’après a), il existe \( w \in A \) tel que \( w\left( a\right) = b \) .

> We have \( a \neq 0 \) , therefore according to a), there exists \( w \in A \) such that \( w\left( a\right) = b \) .

Considérons \( G = \{ \varphi \circ u \mid u \in A\} \) , s.e.v de \( {E}^{ * } \) . Soit \( x \) appartenant à l’orthogonal \( {G}^{ \circ } \) de \( G \) . Pour tout \( u \in A,\left( {\varphi \circ u}\right) \left( x\right) = 0 \) donc pour tout \( u \in A, u\left( x\right) \in \operatorname{Ker}\varphi \) . En d’autres termes, \( {F}_{x} = \{ u\left( x\right) \mid u \in A\} \subset \operatorname{Ker}\varphi \neq E \) . D’après a), on doit donc avoir \( x = 0 \) . Finalement, \( {G}^{ \circ } = \{ 0\} \) et donc \( G = {E}^{ * } \) .

> Consider \( G = \{ \varphi \circ u \mid u \in A\} \) , a subspace of \( {E}^{ * } \) . Let \( x \) belong to the orthogonal \( {G}^{ \circ } \) of \( G \) . For all \( u \in A,\left( {\varphi \circ u}\right) \left( x\right) = 0 \) , therefore for all \( u \in A, u\left( x\right) \in \operatorname{Ker}\varphi \) . In other words, \( {F}_{x} = \{ u\left( x\right) \mid u \in A\} \subset \operatorname{Ker}\varphi \neq E \) . According to a), we must therefore have \( x = 0 \) . Finally, \( {G}^{ \circ } = \{ 0\} \) and thus \( G = {E}^{ * } \) .

Il existe donc \( t \in A \) tel que \( \varphi \circ t = \psi \) . Alors pour tout \( x \in E,\left( {w{u}_{0}t}\right) \left( x\right) = w\left\lbrack {\left( {\varphi \circ t}\right) \left( x\right) a}\right\rbrack = \; \psi \left( x\right) w\left( a\right) = \psi \left( x\right) b = v\left( x\right) \) , donc \( v = w{u}_{0}t \in A \) . L’ensemble \( A \) contient donc tous les éléments de rang 1. Ceci suffit pour conclure que \( A = \mathcal{L}\left( E\right) \) (on montre en effet facilement que tout endomorphisme est somme d'endomorphismes de rang 1).

> There therefore exists \( t \in A \) such that \( \varphi \circ t = \psi \) . Then for all \( x \in E,\left( {w{u}_{0}t}\right) \left( x\right) = w\left\lbrack {\left( {\varphi \circ t}\right) \left( x\right) a}\right\rbrack = \; \psi \left( x\right) w\left( a\right) = \psi \left( x\right) b = v\left( x\right) \) , therefore \( v = w{u}_{0}t \in A \) . The set \( A \) thus contains all elements of rank 1. This is sufficient to conclude that \( A = \mathcal{L}\left( E\right) \) (we indeed easily show that any endomorphism is a sum of rank 1 endomorphisms).

Problem 11. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie, \( G \) un sous-groupe fini de \( \mathcal{G}\ell \left( E\right) \) . Soit \( F = \{ x \in E \mid \forall g \in G, g\left( x\right) = x\} \) . Si \( q = \operatorname{Card}\left( G\right) \) , montrer

> Problem 11. Let \( E \) be a finite-dimensional \( \mathbb{C} \) -v.s., \( G \) a finite subgroup of \( \mathcal{G}\ell \left( E\right) \) . Let \( F = \{ x \in E \mid \forall g \in G, g\left( x\right) = x\} \) . If \( q = \operatorname{Card}\left( G\right) \) , show

\[
q \cdot  \dim F = \mathop{\sum }\limits_{{g \in  G}}\operatorname{tr}\left( g\right) .
\]

Solution. Comme \( G \) est un groupe, pour tout \( h \in G \) , l’application \( G \rightarrow G\;g \mapsto h \circ g \) est bijective. Ceci entraîne

> Solution. Since \( G \) is a group, for any \( h \in G \) , the map \( G \rightarrow G\;g \mapsto h \circ g \) is bijective. This implies

\[
\forall h \in  G,\;\mathop{\sum }\limits_{{g \in  G}}g = \mathop{\sum }\limits_{{g \in  G}}h \circ  g,
\]

ce qui en posant \( f = \mathop{\sum }\limits_{{g \in G}}g \) s’écrit \( f = h \circ f \) , et ceci pour tout \( h \in G \) . On a donc

> which, by setting \( f = \mathop{\sum }\limits_{{g \in G}}g \) , is written as \( f = h \circ f \) , and this for all \( h \in G \) . We therefore have

\[
{qf} = \mathop{\sum }\limits_{{h \in  G}}f = \mathop{\sum }\limits_{{h \in  G}}h \circ  f = \left( {\mathop{\sum }\limits_{{h \in  G}}h}\right)  \circ  f = {f}^{2}.
\]

Le polynôme \( X\left( {X - q}\right) \) annule donc l’endomorphisme \( f \) . On en déduit que \( f \) est diagonalisable et que ses valeurs propres sont éléments de \( \{ 0, q\} \) . Si \( {E}_{q} \) désigne le sous-espace propre de \( f \) associé à la valeur propre \( q \) , on a alors \( q\dim {E}_{q} = \operatorname{tr}f = \mathop{\sum }\limits_{{g \in G}}\operatorname{tr}g \) .

> The polynomial \( X\left( {X - q}\right) \) therefore annihilates the endomorphism \( f \) . We deduce that \( f \) is diagonalizable and that its eigenvalues are elements of \( \{ 0, q\} \) . If \( {E}_{q} \) denotes the eigenspace of \( f \) associated with the eigenvalue \( q \) , then we have \( q\dim {E}_{q} = \operatorname{tr}f = \mathop{\sum }\limits_{{g \in G}}\operatorname{tr}g \) .

L’exercice sera donc résolu si on prouve \( {E}_{q} = F \) . On a déjà \( F \subset {E}_{q} \) . En effet,

> The exercise will therefore be solved if we prove \( {E}_{q} = F \) . We already have \( F \subset {E}_{q} \) . Indeed,

\[
\forall x \in  F,\forall g \in  G, g\left( x\right)  = x\;\text{ donc }\;f\left( x\right)  = \mathop{\sum }\limits_{{g \in  G}}g\left( x\right)  = \mathop{\sum }\limits_{{g \in  G}}x = {qx}.
\]

On conclut avec l’inclusion réciproque : si \( x \in {E}_{q} \) et \( g \in G, g \circ f\left( x\right) = g\left( {qx}\right) = {qg}\left( x\right) \) . Or \( g \circ f = f \) , donc \( \left( {g \circ f}\right) \left( x\right) = f\left( x\right) = {qx} \) , ce qui entraîne \( {qg}\left( x\right) = {qx} \) , et donc \( x \in F \) .

> We conclude with the reverse inclusion: if \( x \in {E}_{q} \) and \( g \in G, g \circ f\left( x\right) = g\left( {qx}\right) = {qg}\left( x\right) \) . However \( g \circ f = f \) , so \( \left( {g \circ f}\right) \left( x\right) = f\left( x\right) = {qx} \) , which implies \( {qg}\left( x\right) = {qx} \) , and therefore \( x \in F \) .

Problem 12. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension quelconque, et \( u, v \in \mathcal{L}\left( E\right) \) vérifiant

> Problem 12. Let \( E \) be a \( \mathbb{C} \) -v.s. of arbitrary dimension, and \( u, v \in \mathcal{L}\left( E\right) \) satisfying

\[
{uv} - {vu} = \alpha {\operatorname{Id}}_{E},\;\alpha  \in  \mathbb{C}.
\]

1/a) Si \( E \) est de dimension finie, montrer \( \alpha = 0 \) .

> 1/a) If \( E \) is finite-dimensional, show \( \alpha = 0 \) .

b) Si \( E \) est normé et \( u \) et \( v \) continus, montrer \( \alpha = 0 \) .

> b) If \( E \) is normed and \( u \) and \( v \) are continuous, show \( \alpha = 0 \) .

c) Si \( v \) admet un polynôme minimal, montrer \( \alpha = 0 \) .

> c) If \( v \) admits a minimal polynomial, show \( \alpha = 0 \) .

2/a) Exhiber deux endomorphismes \( u \) et \( v \) vérifiant \( {uv} - {vu} = {\operatorname{Id}}_{E} \) .

> 2/a) Exhibit two endomorphisms \( u \) and \( v \) satisfying \( {uv} - {vu} = {\operatorname{Id}}_{E} \) .

b) Soit \( p \) un nombre premier. On suppose ici que \( E \) est \( \mathbb{K} \) -e.v de dimension \( p \) , avec \( \mathbb{K} = \mathbb{Z}/p\mathbb{Z} \) . Soit \( v \in \mathcal{L}\left( E\right) \) défini sur une base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) de \( E \) par \( v\left( {e}_{k}\right) = {e}_{k + 1} \) pour \( 1 \leq k \leq p - 1 \) et \( v\left( {e}_{p}\right) = {e}_{1} \) . Montrer que l’ensemble \( {\Gamma }_{v} = \left\{ {u \in \mathcal{L}\left( E\right) \mid {uv} - {vu} = {\operatorname{Id}}_{E}}\right\} \) est non vide et déterminer \( {\Gamma }_{v} \) .

> b) Let \( p \) be a prime number. We assume here that \( E \) is a \( \mathbb{K} \) -v.s. of dimension \( p \) , with \( \mathbb{K} = \mathbb{Z}/p\mathbb{Z} \) . Let \( v \in \mathcal{L}\left( E\right) \) be defined on a basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) of \( E \) by \( v\left( {e}_{k}\right) = {e}_{k + 1} \) for \( 1 \leq k \leq p - 1 \) and \( v\left( {e}_{p}\right) = {e}_{1} \) . Show that the set \( {\Gamma }_{v} = \left\{ {u \in \mathcal{L}\left( E\right) \mid {uv} - {vu} = {\operatorname{Id}}_{E}}\right\} \) is non-empty and determine \( {\Gamma }_{v} \) .

Solution. \( 1/\mathbf{a}) \) Si \( {uv} - {vu} = \alpha {\operatorname{Id}}_{E} \) , alors \( \operatorname{tr}\left( {{uv} - {vu}}\right) = \alpha \operatorname{tr}\left( {\operatorname{Id}}_{E}\right) = \alpha \dim E \) . Or \( \operatorname{tr}\left( {{uv} - {vu}}\right) = \; \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0 \) , donc \( \alpha \dim E = 0 \) , ce qui entraîne \( \alpha = 0 \) .

> Solution. \( 1/\mathbf{a}) \) If \( {uv} - {vu} = \alpha {\operatorname{Id}}_{E} \) , then \( \operatorname{tr}\left( {{uv} - {vu}}\right) = \alpha \operatorname{tr}\left( {\operatorname{Id}}_{E}\right) = \alpha \dim E \) . However \( \operatorname{tr}\left( {{uv} - {vu}}\right) = \; \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0 \) , so \( \alpha \dim E = 0 \) , which implies \( \alpha = 0 \) .

b) Une récurrence facile donne la propriété

> b) An easy induction gives the property

\[
\forall k \in  {\mathbb{N}}^{ * },\;u{v}^{k} - {v}^{k}u = {k\alpha }{v}^{k - 1}.
\]

(*)

> Ceci étant, soit \( \parallel \cdot \parallel \) la norme d’algèbre sur \( {\mathcal{L}}_{c}\left( E\right) \) issue de la norme sur \( E\left( {\parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel }\right) \) . D'après (*), on a

That being said, let \( \parallel \cdot \parallel \) be the algebra norm on \( {\mathcal{L}}_{c}\left( E\right) \) derived from the norm on \( E\left( {\parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel }\right) \) . According to (*), we have

\[
\forall k \in  {\mathbb{N}}^{ * },\;k\left| \alpha \right|  \cdot  \begin{Vmatrix}{v}^{k - 1}\end{Vmatrix} \leq  \begin{Vmatrix}{u{v}^{k}}\end{Vmatrix} + \begin{Vmatrix}{{v}^{k}u}\end{Vmatrix} \leq  2\parallel u\parallel  \cdot  \begin{Vmatrix}{v}^{k}\end{Vmatrix} \leq  2\parallel u\parallel  \cdot  \parallel v\parallel  \cdot  \begin{Vmatrix}{v}^{k - 1}\end{Vmatrix}.
\]

\( \left( {* * }\right) \)

> Si pour tout \( k,{v}^{k} \neq 0 \) alors \( \left( {* * }\right) \) entraîne \( k\left| \alpha \right| \leq 2\parallel u\parallel \cdot \parallel v\parallel \) pour tout \( k \) , donc \( \alpha = 0 \) . Sinon, il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( {v}^{k} = 0 \) et \( {v}^{k - 1} \neq 0 \) . L’identité (*) entraîne alors \( {k\alpha } = 0 \) , donc \( \alpha = 0 \) .

If for all \( k,{v}^{k} \neq 0 \) then \( \left( {* * }\right) \) implies \( k\left| \alpha \right| \leq 2\parallel u\parallel \cdot \parallel v\parallel \) for all \( k \) , so \( \alpha = 0 \) . Otherwise, there exists \( k \in {\mathbb{N}}^{ * } \) such that \( {v}^{k} = 0 \) and \( {v}^{k - 1} \neq 0 \) . The identity (*) then implies \( {k\alpha } = 0 \) , so \( \alpha = 0 \) .

> c) Soit \( P \) le polynôme minimal de \( v \) . Par linéarité, l’identité (*) entraîne

c) Let \( P \) be the minimal polynomial of \( v \) . By linearity, the identity (*) implies

\[
0 = {uP}\left( v\right)  - P\left( v\right) u = \alpha {P}^{\prime }\left( v\right) .
\]

Or \( {P}^{\prime }\left( v\right) \neq 0 \) car \( P \) est le polynôme minimal de \( v \) . Donc \( \alpha = 0 \) .

> However \( {P}^{\prime }\left( v\right) \neq 0 \) because \( P \) is the minimal polynomial of \( v \) . So \( \alpha = 0 \) .

2/a) Les questions précédentes montrent déjà que l’on doit se placer en dimension infinie, consi-dérer des endomorphismes non continus et n'admettant pas de polynôme minimal.

> 2/a) The previous questions already show that one must work in infinite dimension, consider non-continuous endomorphisms, and those not admitting a minimal polynomial.

On choisit \( u \) et \( v \in \mathcal{L}\left( {\mathbb{C}\left\lbrack X\right\rbrack }\right) \) définis par \( u\left( P\right) = {P}^{\prime } \) et \( v\left( P\right) = {XP} \) . Alors pour tout \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) ,

> We choose \( u \) and \( v \in \mathcal{L}\left( {\mathbb{C}\left\lbrack X\right\rbrack }\right) \) defined by \( u\left( P\right) = {P}^{\prime } \) and \( v\left( P\right) = {XP} \) . Then for all \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) ,

\[
\left( {{uv} - {vu}}\right) \left( P\right)  = u\left( {XP}\right)  - v\left( {P}^{\prime }\right)  = \left( {P + X{P}^{\prime }}\right)  - X{P}^{\prime } = P,
\]

donc \( {uv} - {vu} = {\operatorname{Id}}_{\mathbb{C}\left\lbrack X\right\rbrack } \) .

> so \( {uv} - {vu} = {\operatorname{Id}}_{\mathbb{C}\left\lbrack X\right\rbrack } \) .

b) L’endomorphisme \( v \) étant fixé, l’équation \( {uv} - {vu} = {\mathrm{{Id}}}_{E} \) est une équation linéaire d’inconnue \( u \in \mathcal{L}\left( E\right) \) . On en cherche une solution particulière \( {u}_{0} \) , et on obtiendra les autres solutions en additionnant à \( {u}_{0} \) les solutions de l’équation homogène \( {uv} = {vu} \) , qui est le commutant de \( v \) (voir l’exercice 6 page 191). Par commodité notons \( {e}_{0} = {e}_{p} \) , de sorte que \( v\left( {e}_{k}\right) = {e}_{k + 1} \) pour \( 0 \leq k < p \) . Pour avoir \( {u}_{0}v - v{u}_{0} = {\operatorname{Id}}_{E} \) , on a nécessairement

> b) With the endomorphism \( v \) fixed, the equation \( {uv} - {vu} = {\mathrm{{Id}}}_{E} \) is a linear equation with unknown \( u \in \mathcal{L}\left( E\right) \) . We look for a particular solution \( {u}_{0} \) , and we will obtain the other solutions by adding to \( {u}_{0} \) the solutions of the homogeneous equation \( {uv} = {vu} \) , which is the commutant of \( v \) (see exercise 6 page 191). For convenience, let us denote \( {e}_{0} = {e}_{p} \) , so that \( v\left( {e}_{k}\right) = {e}_{k + 1} \) for \( 0 \leq k < p \) . To have \( {u}_{0}v - v{u}_{0} = {\operatorname{Id}}_{E} \) , we necessarily have

\[
\forall k \in  \{ 0,\ldots , p - 1\} ,\;{u}_{0}\left( {e}_{k + 1}\right)  = \left( {{u}_{0}v}\right) \left( {e}_{k}\right)  = v\left( {{u}_{0}\left( {e}_{k}\right) }\right)  + {e}_{k}.
\]

Il est naturel de chercher \( {u}_{0}\left( {e}_{k + 1}\right) \) de la forme \( {\lambda }_{k}{e}_{k} \) . Si ce choix convient, l’égalité précédente entraîne, pour \( 0 < k < p,{\lambda }_{k}{e}_{k} = {u}_{0}\left( {e}_{k + 1}\right) = {\lambda }_{k - 1}v\left( {e}_{k - 1}\right) + {e}_{k} = \left( {{\lambda }_{k - 1} + 1}\right) {e}_{k} \) , ce qui impose \( {\lambda }_{k} = {\lambda }_{k - 1} + 1 \) . On choisit \( {\lambda }_{k} = k \) , donc \( {u}_{0}\left( {e}_{k + 1}\right) = k{e}_{k} \) pour \( 0 \leq k < p \) . Réciproquement soit \( {u}_{0} \) défini sur la base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) par \( {u}_{0}\left( {e}_{k}\right) = \left( {k - 1}\right) {e}_{k - 1} \) , pour \( 1 \leq k \leq p \) . On a

> It is natural to look for \( {u}_{0}\left( {e}_{k + 1}\right) \) of the form \( {\lambda }_{k}{e}_{k} \) . If this choice is suitable, the previous equality leads to, for \( 0 < k < p,{\lambda }_{k}{e}_{k} = {u}_{0}\left( {e}_{k + 1}\right) = {\lambda }_{k - 1}v\left( {e}_{k - 1}\right) + {e}_{k} = \left( {{\lambda }_{k - 1} + 1}\right) {e}_{k} \) , which imposes \( {\lambda }_{k} = {\lambda }_{k - 1} + 1 \) . We choose \( {\lambda }_{k} = k \) , therefore \( {u}_{0}\left( {e}_{k + 1}\right) = k{e}_{k} \) for \( 0 \leq k < p \) . Conversely, let \( {u}_{0} \) be defined on the basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) by \( {u}_{0}\left( {e}_{k}\right) = \left( {k - 1}\right) {e}_{k - 1} \) , for \( 1 \leq k \leq p \) . We have

\[
\forall k \in  \{ 1,\ldots , p - 1\} ,\;\left( {{u}_{0}v - v{u}_{0}}\right) \left( {e}_{k}\right)  = {u}_{0}\left( {e}_{k + 1}\right)  - v\left( {\left( {k - 1}\right) {e}_{k - 1}}\right)  = k{e}_{k} - \left( {k - 1}\right) {e}_{k} = {e}_{k},
\]

\[
\text{ et }\;\left( {{u}_{0}v - v{u}_{0}}\right) \left( {e}_{p}\right)  = {u}_{0}\left( {e}_{1}\right)  - v\left( {\left( {p - 1}\right) {e}_{p - 1}}\right)  = 0 - \left( {p - 1}\right) {e}_{p} = {e}_{p},
\]

la dernière égalité découlant du fait que \( \mathbb{K} \) est de caractéristique \( p \) . On a donc bien \( {u}_{0} \in {\Gamma }_{v} \) . Il nous reste à définir les solutions \( u \) de l’équation homogène \( {uv} = {vu} \) . Remarquons que la matrice de \( v \) dans la base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) est une matrice circulante, de polynôme minimal \( {X}^{p} - 1 \) , de degré \( p = \dim E \) . La dernière question de l’exercice 6 page 191 affirme que le commutant de \( v \) est formé des polynômes en \( v \) , nous allons redémontrer ce résultat dans notre cas particulier. Soit \( u \) commutant avec \( v \) . Comme \( {v}^{k}\left( {e}_{1}\right) = {e}_{k + 1} \) pour \( 0 \leq k < p \) , la famille \( {\left( {v}^{k}\left( {e}_{1}\right) \right) }_{0 \leq k < p} \) est une base de \( E \) donc il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , \( \deg P < p \) , tel que \( u\left( {e}_{1}\right) = P\left( v\right) \left( {e}_{1}\right) \) . On en déduit, pour tout \( k \in \{ 1,\ldots , p\} \) ,

> the last equality following from the fact that \( \mathbb{K} \) has characteristic \( p \) . We therefore have \( {u}_{0} \in {\Gamma }_{v} \) . It remains for us to define the solutions \( u \) of the homogeneous equation \( {uv} = {vu} \) . Note that the matrix of \( v \) in the basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) is a circulant matrix, with minimal polynomial \( {X}^{p} - 1 \) , of degree \( p = \dim E \) . The last question of exercise 6 on page 191 states that the commutant of \( v \) is formed by polynomials in \( v \) ; we will re-prove this result in our particular case. Let \( u \) commute with \( v \) . Since \( {v}^{k}\left( {e}_{1}\right) = {e}_{k + 1} \) for \( 0 \leq k < p \) , the family \( {\left( {v}^{k}\left( {e}_{1}\right) \right) }_{0 \leq k < p} \) is a basis of \( E \) , so there exist \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , \( \deg P < p \) , such that \( u\left( {e}_{1}\right) = P\left( v\right) \left( {e}_{1}\right) \) . We deduce from this, for all \( k \in \{ 1,\ldots , p\} \) ,

\[
u\left( {e}_{k}\right)  = u\left( {{v}^{k - 1}\left( {e}_{1}\right) }\right)  = {v}^{k - 1}u\left( {e}_{1}\right)  = {v}^{k - 1}P\left( v\right) \left( {e}_{1}\right)  = P\left( v\right) \left( {{v}^{k - 1}\left( {e}_{1}\right) }\right)  = P\left( v\right) \left( {e}_{k}\right) .
\]

Donc \( u \) et \( P\left( v\right) \) sont égaux sur chaque vecteur de la base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) donc \( u = P\left( v\right) \) . Récipro-quement tout polynôme en \( v \) commute avec \( v \) . Donc le commutant de \( u \) est \( \{ P\left( v\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) , et finalement \( {\Gamma }_{v} = {u}_{0} + \{ P\left( v\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> Therefore \( u \) and \( P\left( v\right) \) are equal on each vector of the basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) , so \( u = P\left( v\right) \) . Conversely, any polynomial in \( v \) commutes with \( v \) . Thus the commutant of \( u \) is \( \{ P\left( v\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) , and finally \( {\Gamma }_{v} = {u}_{0} + \{ P\left( v\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

Remarque. Il n'y a aucun lien entre la continuité et le fait d'admettre un polynôme minimal. Munissons par exemple \( \mathbb{R}\left\lbrack X\right\rbrack \) de la norme \( \begin{Vmatrix}{\mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{x}^{k}}\end{Vmatrix} = \mathop{\sup }\limits_{k}\left| {a}_{k}\right| \) .

> Remark. There is no link between continuity and the existence of a minimal polynomial. For example, let us equip \( \mathbb{R}\left\lbrack X\right\rbrack \) with the norm \( \begin{Vmatrix}{\mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{x}^{k}}\end{Vmatrix} = \mathop{\sup }\limits_{k}\left| {a}_{k}\right| \) .

L’endomorphisme \( v \) de \( \mathbb{R}\left\lbrack X\right\rbrack \) défini sur la base canonique de \( \mathbb{R}\left\lbrack X\right\rbrack \) par \( v\left( {X}^{n}\right) = \; {X}^{n}/\left( {n + 1}\right) \) est continu mais il admet une infinité de valeurs propres, donc pas de poly-nôme minimal. L’endomorphisme \( v \) de \( \mathbb{R}\left\lbrack X\right\rbrack \) défini par \( v\left( {X}^{2n}\right) = n{X}^{{2n} + 1} \) et \( v\left( {X}^{{2n} + 1}\right) = 0 \) n’est pas continu mais admet un polynôme minimal car \( {v}^{2} = 0 \) .

> The endomorphism \( v \) of \( \mathbb{R}\left\lbrack X\right\rbrack \) defined on the canonical basis of \( \mathbb{R}\left\lbrack X\right\rbrack \) by \( v\left( {X}^{n}\right) = \; {X}^{n}/\left( {n + 1}\right) \) is continuous but admits an infinite number of eigenvalues, and therefore no minimal polynomial. The endomorphism \( v \) of \( \mathbb{R}\left\lbrack X\right\rbrack \) defined by \( v\left( {X}^{2n}\right) = n{X}^{{2n} + 1} \) and \( v\left( {X}^{{2n} + 1}\right) = 0 \) is not continuous but admits a minimal polynomial because \( {v}^{2} = 0 \) .

PROBLEME 13. Soit \( \mathbb{K} \) un corps commutatif et \( E \) un \( \mathbb{K} \) e.v de dimension \( n \geq 2 \) . Soient \( u, v \in \mathcal{L}\left( E\right) \) et \( w = {uv} - {vu} \) tel que \( \operatorname{rg}\left( w\right) = 1. \)

> PROBLEM 13. Let \( \mathbb{K} \) be a commutative field and \( E \) a \( \mathbb{K} \) vector space of dimension \( n \geq 2 \) . Let \( u, v \in \mathcal{L}\left( E\right) \) and \( w = {uv} - {vu} \) be such that \( \operatorname{rg}\left( w\right) = 1. \)

a) Soit \( x \in \operatorname{Im}w \) . Montrer que pour tout \( k \in \mathbb{N},{u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

> a) Let \( x \in \operatorname{Im}w \) . Show that for all \( k \in \mathbb{N},{u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

b) En déduire que le polynôme caractéristique \( {P}_{u} \) de \( u \) n’est pas irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> b) Deduce that the characteristic polynomial \( {P}_{u} \) of \( u \) is not irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) .

Solution. a) Commençons par remarquer que \( w \) est nilpotent (ceci découle de l’exercice 2 page 180, car \( \operatorname{rg}\left( w\right) = 1 \) et \( \operatorname{tr}\left( w\right) = \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0) \) . Ceci étant, soit \( k \in \mathbb{N} \) . On a \( w{u}^{k} = u\left( {v{u}^{k}}\right) - \left( {v{u}^{k}}\right) u \) donc \( \operatorname{tr}\left( {w{u}^{k}}\right) = 0. \)

> Solution. a) Let us begin by noting that \( w \) is nilpotent (this follows from exercise 2 on page 180, because \( \operatorname{rg}\left( w\right) = 1 \) and \( \operatorname{tr}\left( w\right) = \operatorname{tr}\left( {uv}\right) - \operatorname{tr}\left( {vu}\right) = 0) \) . Given this, let \( k \in \mathbb{N} \) . We have \( w{u}^{k} = u\left( {v{u}^{k}}\right) - \left( {v{u}^{k}}\right) u \) therefore \( \operatorname{tr}\left( {w{u}^{k}}\right) = 0. \)

Si \( w{u}^{k} = 0 \) , alors \( w{u}^{k}\left( x\right) = 0 \) , c’est-à-dire \( {u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

> If \( w{u}^{k} = 0 \) , then \( w{u}^{k}\left( x\right) = 0 \) , that is to say \( {u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

Sinon, \( \operatorname{rg}\left( {w{u}^{k}}\right) \geq 1 \) . Or \( \operatorname{Im}\left( {w{u}^{k}}\right) \subset \operatorname{Im}w \) , donc \( \operatorname{rg}\left( {w{u}^{k}}\right) \leq 1 \) . On a donc \( \operatorname{rg}\left( {w{u}^{k}}\right) = 1 \) , de sorte que comme \( \operatorname{tr}\left( {w{u}^{k}}\right) = 0, w{u}^{k} \) est nilpotente. Comme \( x \in \operatorname{Im}w \) , que \( w{u}^{k}\left( x\right) \in \operatorname{Im}w \) et que \( \dim \left( {\operatorname{Im}w}\right) = 1 \) , on voit que \( x \) est vecteur propre de \( w{u}^{k} \) . L’endomorphisme \( w{u}^{k} \) étant nilpotent, on en déduit que \( w{u}^{k}\left( x\right) = 0 \) , i. e. \( {u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

> Otherwise, \( \operatorname{rg}\left( {w{u}^{k}}\right) \geq 1 \) . But \( \operatorname{Im}\left( {w{u}^{k}}\right) \subset \operatorname{Im}w \) , so \( \operatorname{rg}\left( {w{u}^{k}}\right) \leq 1 \) . We thus have \( \operatorname{rg}\left( {w{u}^{k}}\right) = 1 \) , so that since \( \operatorname{tr}\left( {w{u}^{k}}\right) = 0, w{u}^{k} \) is nilpotent. As \( x \in \operatorname{Im}w \) , that \( w{u}^{k}\left( x\right) \in \operatorname{Im}w \) and that \( \dim \left( {\operatorname{Im}w}\right) = 1 \) , we see that \( x \) is an eigenvector of \( w{u}^{k} \) . Since the endomorphism \( w{u}^{k} \) is nilpotent, we deduce that \( w{u}^{k}\left( x\right) = 0 \) , i. e. \( {u}^{k}\left( x\right) \in \operatorname{Ker}w \) .

b) L’idée est de trouver un s.e.v strict de \( E \) stable par \( u \) . Fixons \( x \in \operatorname{Im}w, x \neq 0 \) . Soit \( F = \; \left\{ {{u}^{k}\left( x\right) \mid k \in \mathbb{N}}\right\} \) . Le s.e.v \( G = \operatorname{Vect}F \) est stable par \( u \) . Comme \( x \neq 0 \) , on a même \( G \neq \{ 0\} \) . Par ailleurs, d’après a), on a \( G \subset \operatorname{Ker}w \) . En notant \( p = \dim G \) , on en déduit

> b) The idea is to find a proper subspace of \( E \) stable under \( u \) . Let us fix \( x \in \operatorname{Im}w, x \neq 0 \) . Let \( F = \; \left\{ {{u}^{k}\left( x\right) \mid k \in \mathbb{N}}\right\} \) . The subspace \( G = \operatorname{Vect}F \) is stable under \( u \) . As \( x \neq 0 \) , we even have \( G \neq \{ 0\} \) . Furthermore, according to a), we have \( G \subset \operatorname{Ker}w \) . By denoting \( p = \dim G \) , we deduce

\[
1 \leq  p \leq  \dim \operatorname{Ker}w = n - \operatorname{rg}w = n - 1.
\]

Soit \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) une base de \( G \) complétée en une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . On a

> Let \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) be a basis of \( G \) extended to a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . We have

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} A & B \\  0 & C \end{matrix}\right) ,\;A \in  {\mathcal{M}}_{p}\left( \mathbb{K}\right) , C \in  {\mathcal{M}}_{n - p}\left( \mathbb{K}\right) ,
\]

donc \( {P}_{u} = {P}_{A} \cdot {P}_{C} \) n’est pas irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> therefore \( {P}_{u} = {P}_{A} \cdot {P}_{C} \) is not irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) .

Problem 14. Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . a) Montrer que

> Problem 14. Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . a) Show that

\[
\left( {\exists P \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) , P \neq  0}\right) ,\;{AP} = {PB}
\]

si et seulement si \( A \) et \( B \) ont au moins une valeur propre commune.

> if and only if \( A \) and \( B \) have at least one common eigenvalue.

b) Soit \( r \in \mathbb{N},0 < r \leq n \) . Montrer que s’il existe \( P \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) avec \( \operatorname{rg}P = r \) tel que \( {AP} = {PB} \) , alors les polynômes caractéristiques \( {P}_{A} \) et \( {P}_{B} \) de \( A \) et \( B \) vérifient \( \deg \left( {\operatorname{pgcd}\left( {{P}_{A},{P}_{B}}\right) }\right) \geq r \) . La réciproque est elle vraie?

> b) Let \( r \in \mathbb{N},0 < r \leq n \) . Show that if there exists \( P \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) with \( \operatorname{rg}P = r \) such that \( {AP} = {PB} \) , then the characteristic polynomials \( {P}_{A} \) and \( {P}_{B} \) of \( A \) and \( B \) satisfy \( \deg \left( {\operatorname{pgcd}\left( {{P}_{A},{P}_{B}}\right) }\right) \geq r \) . Is the converse true?

Solution. a) Remarquons déjà que si \( P \) est inversible, \( {AP} = {PB} \) s’écrit \( {P}^{-1}{AP} = B \) , donc \( A \) et \( B \) sont semblables et le résultat est évident. Le cas général est plus délicat.

> Solution. a) Let us first note that if \( P \) is invertible, \( {AP} = {PB} \) can be written as \( {P}^{-1}{AP} = B \) , so \( A \) and \( B \) are similar and the result is obvious. The general case is more delicate.

Condition nécessaire. Donnons deux méthodes.

> Necessary condition. Let us provide two methods.

Première méthode. Par récurrence sur \( k \in \mathbb{N} \) , on a facilement \( {A}^{k}P = P{B}^{k} \) , donc pour tout polynôme \( F \in \mathbb{C}\left\lbrack X\right\rbrack , F\left( A\right) P = {PF}\left( B\right) .\;\left( *\right) \)

> First method. By induction on \( k \in \mathbb{N} \), we easily have \( {A}^{k}P = P{B}^{k} \), so for any polynomial \( F \in \mathbb{C}\left\lbrack X\right\rbrack , F\left( A\right) P = {PF}\left( B\right) .\;\left( *\right) \)

Ceci étant, supposons que \( A \) et \( B \) n’ont aucune valeur propre commune. Alors les polynômes caractéristiques \( {P}_{A} \) et \( {P}_{B} \) de \( A \) et \( B \) n’ont aucune racine commune dans \( \mathbb{C} \) et sont donc premiers entre eux. D’après le théorème de Bezout, il existe donc \( U, V \in \mathbb{C}\left\lbrack X\right\rbrack \) tels que \( U{P}_{A} + V{P}_{B} = 1 \) . On a alors \( U\left( B\right) {P}_{A}\left( B\right) = {I}_{n} \) , et donc \( {P}_{A}\left( B\right) \) est inversible. Or \( {P}_{A}\left( A\right) P = P{P}_{A}\left( B\right) \) d’après \( \left( *\right) \) , donc \( P{P}_{A}\left( B\right) = 0 \) , et comme \( {P}_{A}\left( B\right) \) est inversible, ceci entraîne \( P = 0 \) . Ceci est absurde, d’où la condition nécessaire.

> That being said, suppose \( A \) and \( B \) have no common eigenvalue. Then the characteristic polynomials \( {P}_{A} \) and \( {P}_{B} \) of \( A \) and \( B \) have no common root in \( \mathbb{C} \) and are therefore coprime. According to Bezout's theorem, there exist \( U, V \in \mathbb{C}\left\lbrack X\right\rbrack \) such that \( U{P}_{A} + V{P}_{B} = 1 \). We then have \( U\left( B\right) {P}_{A}\left( B\right) = {I}_{n} \), and thus \( {P}_{A}\left( B\right) \) is invertible. However, \( {P}_{A}\left( A\right) P = P{P}_{A}\left( B\right) \) according to \( \left( *\right) \), so \( P{P}_{A}\left( B\right) = 0 \), and since \( {P}_{A}\left( B\right) \) is invertible, this implies \( P = 0 \). This is absurd, hence the necessary condition.

Seconde méthode. Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( {\mathbb{C}}^{n} \) qui triangularise la matrice \( B \) . Pour tout \( j \) , on a \( B{e}_{j} = {\lambda }_{j}{e}_{j} + \mathop{\sum }\limits_{{i < j}}{b}_{i, j}{e}_{i} \) . Soit \( j \) le plus petit indice tel que \( P{e}_{j} \neq 0 \) ( \( j \) existe, sinon \( P = 0 \) ). Alors

> Second method. Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( {\mathbb{C}}^{n} \) that triangularizes the matrix \( B \). For any \( j \), we have \( B{e}_{j} = {\lambda }_{j}{e}_{j} + \mathop{\sum }\limits_{{i < j}}{b}_{i, j}{e}_{i} \). Let \( j \) be the smallest index such that \( P{e}_{j} \neq 0 \) (\( j \) exists, otherwise \( P = 0 \)). Then

\[
{AP}{e}_{j} = {PB}{e}_{j} = P\left( {{\lambda }_{j}{e}_{j} + \mathop{\sum }\limits_{{i < j}}{b}_{i, j}{e}_{i}}\right)  = {\lambda }_{j}P{e}_{j},
\]

donc \( {\lambda }_{j} \) est valeur propre de \( A \) (un vecteur propre associé est \( P{e}_{j} \) ), donc valeur propre commune à \( A \) et \( B \) .

> therefore \( {\lambda }_{j} \) is an eigenvalue of \( A \) (an associated eigenvector is \( P{e}_{j} \)), and thus a common eigenvalue to \( A \) and \( B \).

Condition suffisante. Trigonalisons \( A \) supérieurement et \( B \) inférieurement, en supposant que \( \lambda \in \; \mathbb{C} \) est valeur propre commune à \( A \) et \( B \) : il existe \( {P}_{1},{P}_{2} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tels que

> Sufficient condition. Let us trigonalize \( A \) into an upper triangular matrix and \( B \) into a lower triangular matrix, assuming that \( \lambda \in \; \mathbb{C} \) is a common eigenvalue of \( A \) and \( B \): there exist \( {P}_{1},{P}_{2} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that

\[
T = {P}_{1}^{-1}A{P}_{1} = \left( \begin{matrix} \lambda &  \times  & \cdots &  \times  \\  0 &  \times  &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 &  \times   \end{matrix}\right) \;\text{ et }\;S = {P}_{2}^{-1}B{P}_{2} = \left( \begin{matrix} \lambda & 0 & \cdots & 0 \\   \times  &  \times  &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & 0 \\   \times  & \cdots &  \times  &  \times   \end{matrix}\right) .
\]

En désignant par \( Y \) la matrice dont tous les coefficients sont nuls sauf celui d’indice \( \left( {1,1}\right) \) qui vaut 1, on a \( {TY} = {\lambda Y} \) et \( {YS} = {\lambda Y} \) . Ainsi, \( \left( {{P}_{1}^{-1}A{P}_{1}}\right) Y = Y\left( {{P}_{2}^{-1}B{P}_{2}}\right) \) , et en multipliant à gauche par \( {P}_{1} \) et à droite par \( {P}_{2}^{-1} \) on obtient \( {AP} = {PB} \) avec \( P = {P}_{1}Y{P}_{2}^{-1} \neq 0 \) .

> By denoting as \( Y \) the matrix whose coefficients are all zero except for the one at index \( \left( {1,1}\right) \) which is 1, we have \( {TY} = {\lambda Y} \) and \( {YS} = {\lambda Y} \). Thus, \( \left( {{P}_{1}^{-1}A{P}_{1}}\right) Y = Y\left( {{P}_{2}^{-1}B{P}_{2}}\right) \), and by multiplying on the left by \( {P}_{1} \) and on the right by \( {P}_{2}^{-1} \) we obtain \( {AP} = {PB} \) with \( P = {P}_{1}Y{P}_{2}^{-1} \neq 0 \).

b) Le cas \( r = 1 \) est une conséquence du résultat de la question précédente, et lorsque \( r = n \) c’est immédiat car les matrices \( A \) et \( B \) sont alors semblables, donc ont même polynôme caractéristique. Pour traiter le cas général, on se ramène au cas plus simple où la matrice \( P \) est de la forme \( {J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) . Comme la matrice \( P \) est de rang \( r \) , elle est équivalente à la matrice \( {J}_{r} \) ce qui s’écrit \( P = Q{J}_{r}R \) avec \( Q, R \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . On a donc

> b) The case \( r = 1 \) is a consequence of the result from the previous question, and when \( r = n \) it is immediate because the matrices \( A \) and \( B \) are then similar, and thus have the same characteristic polynomial. To handle the general case, we reduce it to the simpler case where the matrix \( P \) is of the form \( {J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) . Since the matrix \( P \) has rank \( r \) , it is equivalent to the matrix \( {J}_{r} \) which is written as \( P = Q{J}_{r}R \) with \( Q, R \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . We therefore have

\[
A\left( {Q{J}_{r}R}\right)  = \left( {Q{J}_{r}R}\right) B\;\text{ donc }\;{A}^{\prime }{J}_{r} = {J}_{r}{B}^{\prime },\;\text{ avec }{A}^{\prime } = {Q}^{-1}{AQ}\text{ et }{B}^{\prime } = {RB}{R}^{-1}.
\]

La matrice \( {A}^{\prime } \) est semblable à \( A \) donc \( {P}_{{A}^{\prime }} = {P}_{A} \) , de même \( {P}_{{B}^{\prime }} = {P}_{B} \) . En écrivant les matrices \( {A}^{\prime } \) et \( {B}^{\prime } \) par blocs sous la forme \( {A}^{\prime } = \left( \begin{matrix} {A}_{0}^{\prime } & {A}_{1}^{\prime } \\ {A}_{2}^{\prime } & {A}_{3}^{\prime } \end{matrix}\right) \) et \( {B}^{\prime } = \left( \begin{matrix} {B}_{0}^{\prime } & {B}_{1}^{\prime } \\ {B}_{2}^{\prime } & {B}_{3}^{\prime } \end{matrix}\right) \) (avec \( {A}_{0}^{\prime } \) et \( {B}_{0}^{\prime } \) dans \( {\mathcal{M}}_{r}\left( \mathbb{C}\right) \) ) l’égalité \( {A}^{\prime }{J}_{r} = {J}_{r}{B}^{\prime } \) s’écrit

> The matrix \( {A}^{\prime } \) is similar to \( A \) so \( {P}_{{A}^{\prime }} = {P}_{A} \) , likewise \( {P}_{{B}^{\prime }} = {P}_{B} \) . By writing the matrices \( {A}^{\prime } \) and \( {B}^{\prime } \) in block form as \( {A}^{\prime } = \left( \begin{matrix} {A}_{0}^{\prime } & {A}_{1}^{\prime } \\ {A}_{2}^{\prime } & {A}_{3}^{\prime } \end{matrix}\right) \) and \( {B}^{\prime } = \left( \begin{matrix} {B}_{0}^{\prime } & {B}_{1}^{\prime } \\ {B}_{2}^{\prime } & {B}_{3}^{\prime } \end{matrix}\right) \) (with \( {A}_{0}^{\prime } \) and \( {B}_{0}^{\prime } \) in \( {\mathcal{M}}_{r}\left( \mathbb{C}\right) \) ) the equality \( {A}^{\prime }{J}_{r} = {J}_{r}{B}^{\prime } \) is written as

\[
\left( \begin{matrix} {A}_{0}^{\prime } & {A}_{1}^{\prime } \\  {A}_{2}^{\prime } & {A}_{3}^{\prime } \end{matrix}\right) \left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right)  = \left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right) \left( \begin{matrix} {B}_{0}^{\prime } & {B}_{1}^{\prime } \\  {B}_{2}^{\prime } & {B}_{3}^{\prime } \end{matrix}\right) \;\text{ donc }\;\left( \begin{matrix} {A}_{0}^{\prime } & 0 \\  {A}_{2}^{\prime } & 0 \end{matrix}\right)  = \left( \begin{matrix} {B}_{0}^{\prime } & {B}_{1}^{\prime } \\  0 & 0 \end{matrix}\right)
\]

ce qui entraîne \( {A}_{0}^{\prime } = {B}_{0}^{\prime },{A}_{2}^{\prime } = 0 \) et \( {B}_{1}^{\prime } = 0 \) . En notant \( S = {A}_{0}^{\prime } = {B}_{0}^{\prime } \) , on a donc

> which implies \( {A}_{0}^{\prime } = {B}_{0}^{\prime },{A}_{2}^{\prime } = 0 \) and \( {B}_{1}^{\prime } = 0 \) . By denoting \( S = {A}_{0}^{\prime } = {B}_{0}^{\prime } \) , we therefore have

\[
{A}^{\prime } = \left( \begin{matrix} S & {A}_{1}^{\prime } \\  0 & {A}_{3}^{\prime } \end{matrix}\right) \;\text{ et }\;{B}^{\prime } = \left( \begin{matrix} S & 0 \\  {B}_{2}^{\prime } & {B}_{3}^{\prime } \end{matrix}\right) .
\]

Ceci montre que \( {P}_{{A}^{\prime }} = {P}_{S}{P}_{{A}_{3}^{\prime }} \) et \( {P}_{{B}^{\prime }} = {P}_{S}{P}_{{B}_{3}^{\prime }} \) , donc le polynôme \( {P}_{S} \) divise \( {P}_{A} = {P}_{{A}^{\prime }} \) et \( {P}_{B} = {P}_{{B}^{\prime }} \) , et comme \( \deg \left( {P}_{S}\right) = r \) ceci entraîne bien \( \deg \left( {\operatorname{pgcd}\left( {{P}_{A},{P}_{B}}\right) }\right) \geq r \) .

> This shows that \( {P}_{{A}^{\prime }} = {P}_{S}{P}_{{A}_{3}^{\prime }} \) and \( {P}_{{B}^{\prime }} = {P}_{S}{P}_{{B}_{3}^{\prime }} \) , so the polynomial \( {P}_{S} \) divides \( {P}_{A} = {P}_{{A}^{\prime }} \) and \( {P}_{B} = {P}_{{B}^{\prime }} \) , and since \( \deg \left( {P}_{S}\right) = r \) this indeed implies \( \deg \left( {\operatorname{pgcd}\left( {{P}_{A},{P}_{B}}\right) }\right) \geq r \) .

La réciproque est vraie lorsque \( r = 1 \) (on a exhibé une matrice \( P \) de rang 1 vérifiant \( {AP} = {PB} \) dans la solution de la question précédente), mais fausse dans le cas général. Par exemple, lorsque \( r = n \) avec \( n \geq 2 \) , on peut avoir \( {P}_{A} = {P}_{B} \) sans que \( A \) et \( B \) vérifient \( {AP} = {PB} \) avec \( \operatorname{rg}\left( P\right) = n \) , car ceci impliquerait que \( P \) est inversible, donc \( A \) et \( B \) seraient semblables. Or deux matrices ayant même polynôme caractéristique ne sont pas forcément semblables, comme le montre le contre-exemple où \( A = 0 \) et \( B \) une matrice nilpotente non nulle.

> The converse is true when \( r = 1 \) (we exhibited a matrix \( P \) of rank 1 satisfying \( {AP} = {PB} \) in the solution to the previous question), but false in the general case. For example, when \( r = n \) with \( n \geq 2 \) , we can have \( {P}_{A} = {P}_{B} \) without \( A \) and \( B \) satisfying \( {AP} = {PB} \) with \( \operatorname{rg}\left( P\right) = n \) , because this would imply that \( P \) is invertible, so \( A \) and \( B \) would be similar. However, two matrices with the same characteristic polynomial are not necessarily similar, as shown by the counterexample where \( A = 0 \) and \( B \) is a non-zero nilpotent matrix.

Problem 15. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer que \( \det \left( {I + A\bar{A}}\right) \in {\mathbb{R}}^{ + } \) . (Indication : si \( U \) est un vecteur propre de \( A\bar{A} \) associé à une valeur propre \( \lambda \notin {\mathbb{R}}^{ + } \) , montrer que \( V = A\bar{U} \) est aussi un vecteur propre de \( A\bar{A} \) , et que la famille \( \left( {U, V}\right) \) est libre).

> Problem 15. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Show that \( \det \left( {I + A\bar{A}}\right) \in {\mathbb{R}}^{ + } \) . (Hint: if \( U \) is an eigenvector of \( A\bar{A} \) associated with an eigenvalue \( \lambda \notin {\mathbb{R}}^{ + } \) , show that \( V = A\bar{U} \) is also an eigenvector of \( A\bar{A} \) , and that the family \( \left( {U, V}\right) \) is linearly independent).

Solution. Nous procédons par récurrence sur \( n \) . Si \( n = 1 \) le résultat est immédiat. Supposons maintenant \( n \geq 2 \) . Si toutes les valeurs propres \( \left( {\lambda }_{i}\right) \) de \( A\bar{A} \) sont des nombres réels positifs, alors en trigonalisant \( A\bar{A} \) on s’aperçoit que \( \det \left( {I + A\bar{A}}\right) = \mathop{\prod }\limits_{i}\left( {1 + {\lambda }_{i}}\right) \) , donc a bien \( \det \left( {I + A\bar{A}}\right) \in {\mathbb{R}}^{ + } \) . Sinon, la matrice \( A\bar{A} \) a au moins une valeur propre \( \lambda \notin {\mathbb{R}}^{ + } \) . Soit \( U \) un vecteur propre associé. Le vecteur \( V = A\bar{U} \) vérifie

> Solution. We proceed by induction on \( n \) . If \( n = 1 \) the result is immediate. Now assume \( n \geq 2 \) . If all eigenvalues \( \left( {\lambda }_{i}\right) \) of \( A\bar{A} \) are positive real numbers, then by triangularizing \( A\bar{A} \) we see that \( \det \left( {I + A\bar{A}}\right) = \mathop{\prod }\limits_{i}\left( {1 + {\lambda }_{i}}\right) \) , so we indeed have \( \det \left( {I + A\bar{A}}\right) \in {\mathbb{R}}^{ + } \) . Otherwise, the matrix \( A\bar{A} \) has at least one eigenvalue \( \lambda \notin {\mathbb{R}}^{ + } \) . Let \( U \) be an associated eigenvector. The vector \( V = A\bar{U} \) satisfies

\[
A\bar{A}V = A\bar{A}A\bar{U} = A\overline{\left( A\bar{A}U\right) } = A\overline{\lambda U} = \overline{\lambda }V.
\]

La famille \( \left( {U, V}\right) \) est bien libre, car si on avait \( V = {\mu U} \) avec \( \mu \in \mathbb{C} \) , alors on aurait

> The family \( \left( {U, V}\right) \) is indeed linearly independent, because if we had \( V = {\mu U} \) with \( \mu \in \mathbb{C} \) , then we would have

\[
{\lambda U} = A\bar{A}U = A\bar{V} = \overline{\mu }A\bar{U} = \overline{\mu }V = {\left| \mu \right| }^{2}U
\]

donc \( \lambda = {\left| \mu \right| }^{2} \) ce qui est impossible puisque \( \lambda \notin {\mathbb{R}}^{ + } \) . Si \( n = 2 \) , la famille \( \left( {U, V}\right) \) est une base de vecteurs propres de \( A\bar{A} \) associés aux valeurs propres \( \lambda \) et \( \overline{\lambda } \) , et en diagonalisant \( A\bar{A} \) on obtient \( \det \left( {I + A\bar{A}}\right) = \left( {1 + \lambda }\right) \left( {1 + \overline{\lambda }}\right) = {\left| 1 + \lambda \right| }^{2} \in {\mathbb{R}}^{ + } \) . Sinon \( n > 2 \) , et on complete la famille \( \left( {U, V}\right) \) en une base \( \mathcal{B} \) de \( {\mathbb{C}}^{n} \) . Notons \( P \) la matrice de passage de la base canonique \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) de \( {\mathbb{C}}^{n} \) à la base \( \mathcal{B} \) . On a la forme par blocs \( {P}^{-1}A\bar{A}P = \left( \begin{matrix} \lambda & 0 \\ 0 & \overline{\lambda } \\ \left( 0\right) & \times \end{matrix}\right) \) mais pour appliquer l’hypothèse de récurrence, il faut montrer que le bloc inférieur droit est de la forme \( M\bar{M} \) , ce qui n’est pas immédiat a priori. Afin de montrer ce résultat, on remarque que \( {P}^{-1}A\bar{A}P = B\bar{B} \) où \( B = {P}^{-1}A\bar{P} \) . Les matrices \( B\bar{B} \) et \( A\bar{A} \) sont semblables, donc \( I + B\bar{B} \) et \( I + A\bar{A} \) également, d’où \( \det \left( {I + B\bar{B}}\right) = \det \left( {I + A\bar{A}}\right) \) . Comme \( P{E}_{1} = U \) et \( P{E}_{2} = V \) et que les vecteurs \( {E}_{1} \) et \( {E}_{2} \) ont leurs coordonnées réelles, on a

> so \( \lambda = {\left| \mu \right| }^{2} \) which is impossible since \( \lambda \notin {\mathbb{R}}^{ + } \) . If \( n = 2 \) , the family \( \left( {U, V}\right) \) is a basis of eigenvectors of \( A\bar{A} \) associated with eigenvalues \( \lambda \) and \( \overline{\lambda } \) , and by diagonalizing \( A\bar{A} \) we obtain \( \det \left( {I + A\bar{A}}\right) = \left( {1 + \lambda }\right) \left( {1 + \overline{\lambda }}\right) = {\left| 1 + \lambda \right| }^{2} \in {\mathbb{R}}^{ + } \) . Otherwise \( n > 2 \) , and we complete the family \( \left( {U, V}\right) \) into a basis \( \mathcal{B} \) of \( {\mathbb{C}}^{n} \) . Let \( P \) be the transition matrix from the canonical basis \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) of \( {\mathbb{C}}^{n} \) to the basis \( \mathcal{B} \) . We have the block form \( {P}^{-1}A\bar{A}P = \left( \begin{matrix} \lambda & 0 \\ 0 & \overline{\lambda } \\ \left( 0\right) & \times \end{matrix}\right) \) but to apply the induction hypothesis, we must show that the lower right block is of the form \( M\bar{M} \) , which is not immediate a priori. To show this result, we note that \( {P}^{-1}A\bar{A}P = B\bar{B} \) where \( B = {P}^{-1}A\bar{P} \) . The matrices \( B\bar{B} \) and \( A\bar{A} \) are similar, so \( I + B\bar{B} \) and \( I + A\bar{A} \) are as well, hence \( \det \left( {I + B\bar{B}}\right) = \det \left( {I + A\bar{A}}\right) \) . Since \( P{E}_{1} = U \) and \( P{E}_{2} = V \) and the vectors \( {E}_{1} \) and \( {E}_{2} \) have real coordinates, we have

\[
B{E}_{1} = {P}^{-1}A\bar{P}{E}_{1} = {P}^{-1}A\bar{U} = {P}^{-1}V = {E}_{2},
\]

\[
B{E}_{2} = {P}^{-1}A\bar{P}{E}_{2} = {P}^{-1}A\bar{V} = {P}^{-1}A\bar{A}U = \lambda {P}^{-1}U = \lambda {E}_{1}.
\]

Ceci montre que la matrice \( B \) a la forme par blocs

> This shows that the matrix \( B \) has the block form

\[
B = \left( \begin{matrix} 0 & \lambda & C \\  1 & 0 & D \end{matrix}\right) \;\text{ donc }\;B\bar{B} = \left( \begin{matrix} \lambda & 0 & E \\  0 & \overline{\lambda } & D \end{matrix}\right) .
\]

Cette écriture entraîne \( \det \left( {I + B\bar{B}}\right) = {\left| 1 + \lambda \right| }^{2}\det \left( {I + D\bar{D}}\right) \) , et ceci est bien un nombre réel positif d’après l’hypothèse de récurrence appliquée à la matrice \( D\bar{D} \) .

> This expression leads to \( \det \left( {I + B\bar{B}}\right) = {\left| 1 + \lambda \right| }^{2}\det \left( {I + D\bar{D}}\right) \) , and this is indeed a positive real number according to the induction hypothesis applied to the matrix \( D\bar{D} \) .

Remarque. D’après l’exercice 3 page 197, le polynôme caractéristique de \( A\bar{A} \) est égal à celui de \( \bar{A}A \) . Ceci entraîne \( {P}_{A\bar{A}} = {P}_{\bar{A}A} = \overline{{P}_{A\bar{A}}} \) , donc \( {P}_{A\bar{A}} \) a ses coefficients réels. En particulier, \( \det \left( {I + A\bar{A}}\right) = {P}_{A\bar{A}}\left( {-1}\right) \in \mathbb{R} \) , mais ceci est un résultat moins fort que \( \det (I + \; A\bar{A}) \in {\mathbb{R}}^{ + } \) .

> Remark. According to exercise 3 on page 197, the characteristic polynomial of \( A\bar{A} \) is equal to that of \( \bar{A}A \) . This leads to \( {P}_{A\bar{A}} = {P}_{\bar{A}A} = \overline{{P}_{A\bar{A}}} \) , so \( {P}_{A\bar{A}} \) has real coefficients. In particular, \( \det \left( {I + A\bar{A}}\right) = {P}_{A\bar{A}}\left( {-1}\right) \in \mathbb{R} \) , but this is a weaker result than \( \det (I + \; A\bar{A}) \in {\mathbb{R}}^{ + } \) .

Problème 16. Soit \( p \) un nombre premier. On considère la matrice

> Problem 16. Let \( p \) be a prime number. We consider the matrix

\[
A = \left( \begin{matrix} {a}_{0} & {a}_{1} & \cdots & {a}_{p - 2} & {a}_{p - 1} \\  {a}_{p - 1} & {a}_{0} & {a}_{1} & & {a}_{p - 2} \\  \vdots & {a}_{p - 1} & {a}_{0} &  \ddots  & \vdots \\  \vdots & &  \ddots  &  \ddots  & {a}_{1} \\  {a}_{1} & \cdots & \cdots & {a}_{p - 1} & {a}_{0} \end{matrix}\right)
\]

avec pour tout \( i,{a}_{i} \in \mathbb{Z} \) . Montrer que \( \det A \equiv {a}_{0} + {a}_{1} + \cdots + {a}_{p - 1}\left( {\;\operatorname{mod}\;p}\right) \) . Solution. Cela ressemble à l'exercice 4 page 190. On commence de la même manière. Soit

> with for all \( i,{a}_{i} \in \mathbb{Z} \) . Show that \( \det A \equiv {a}_{0} + {a}_{1} + \cdots + {a}_{p - 1}\left( {\;\operatorname{mod}\;p}\right) \) . Solution. This looks like exercise 4 on page 190. We start in the same way. Let

\[
J = \left( \begin{matrix} 0 & 1 & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  0 & &  \ddots  & 1 \\  1 & 0 & \cdots & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right)
\]

On avait montré à l’exercice 4 page 190 que le polynôme caractéristique de \( J \) est \( {P}_{J} = {\left( -1\right) }^{p}\left( {{X}^{p} - }\right. \) 1), et que \( A = Q\left( J\right) \) , où \( Q = {a}_{0} + {a}_{1}X + \cdots + {a}_{p - 1}{X}^{p - 1} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Regardons \( A \) et \( J \) comme des matrices à valeurs dans \( \mathbb{Z}/p\mathbb{Z} \) . Dans \( \mathbb{Z}/p\mathbb{Z},{P}_{J} = {\left( -1\right) }^{p}\left( {{X}^{p} - \dot{1}}\right) = {\left( -1\right) }^{p}{\left( X - \dot{1}\right) }^{p} \) . Comme \( A = Q\left( J\right) \) , on a alors \( {P}_{A} = {\left( -1\right) }^{p}{\left\lbrack X - Q\left( \dot{1}\right) \right\rbrack }^{p} \) (pour s’en rendre compte, trigonaliser \( J \) dans \( {\mathcal{M}}_{n}\left( {\mathbb{Z}/p\mathbb{Z}}\right) \) - voir la remarque 1 page 184), donc \( \det A \equiv {P}_{A}\left( 0\right) \equiv Q{\left( 1\right) }^{p} \equiv Q\left( 1\right) \equiv {a}_{0} + \cdots + {a}_{p - 1} \; \left( {\;\operatorname{mod}\;p}\right) \) .

> We showed in exercise 4 on page 190 that the characteristic polynomial of \( J \) is \( {P}_{J} = {\left( -1\right) }^{p}\left( {{X}^{p} - }\right. \) 1), and that \( A = Q\left( J\right) \) , where \( Q = {a}_{0} + {a}_{1}X + \cdots + {a}_{p - 1}{X}^{p - 1} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Let us view \( A \) and \( J \) as matrices with values in \( \mathbb{Z}/p\mathbb{Z} \) . In \( \mathbb{Z}/p\mathbb{Z},{P}_{J} = {\left( -1\right) }^{p}\left( {{X}^{p} - \dot{1}}\right) = {\left( -1\right) }^{p}{\left( X - \dot{1}\right) }^{p} \) . Since \( A = Q\left( J\right) \) , we then have \( {P}_{A} = {\left( -1\right) }^{p}{\left\lbrack X - Q\left( \dot{1}\right) \right\rbrack }^{p} \) (to see this, trigonalize \( J \) in \( {\mathcal{M}}_{n}\left( {\mathbb{Z}/p\mathbb{Z}}\right) \) - see remark 1 on page 184), therefore \( \det A \equiv {P}_{A}\left( 0\right) \equiv Q{\left( 1\right) }^{p} \equiv Q\left( 1\right) \equiv {a}_{0} + \cdots + {a}_{p - 1} \; \left( {\;\operatorname{mod}\;p}\right) \) .

Problème 17. Le polynôme caractéristique \( {P}_{A} \) d’une matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) peut s’écrire

> Problem 17. The characteristic polynomial \( {P}_{A} \) of a matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) can be written

\[
{P}_{A} = {\left( -1\right) }^{n}\left( {{X}^{n} + {f}_{1}\left( A\right) {X}^{n - 1} + \cdots  + {f}_{n - 1}\left( A\right) X + {f}_{n}\left( A\right) }\right) ,
\]

où les \( {f}_{i}\left( A\right) \) sont des polynômes en les coefficients de \( A \) .

> where the \( {f}_{i}\left( A\right) \) are polynomials in the coefficients of \( A \) .

a) Montrer que pour toutes matrices \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , on a \( {f}_{i}\left( {AB}\right) = {f}_{i}\left( {BA}\right) \) pour tout \( i \) . b) Réciproquement, soit \( Q : {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow \mathbb{C}\;A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \mapsto Q\left( A\right) \) une fonction polynôme en les coefficients \( {a}_{i, j} \) de \( A \) . Si pour toutes matrices \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , on a \( Q\left( {AB}\right) = Q\left( {BA}\right) \) , montrer qu’il existe un polynôme \( F \in \mathbb{C}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) tel que

> a) Show that for all matrices \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , we have \( {f}_{i}\left( {AB}\right) = {f}_{i}\left( {BA}\right) \) for all \( i \) . b) Conversely, let \( Q : {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow \mathbb{C}\;A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \mapsto Q\left( A\right) \) be a polynomial function in the coefficients \( {a}_{i, j} \) of \( A \) . If for all matrices \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , we have \( Q\left( {AB}\right) = Q\left( {BA}\right) \) , show that there exists a polynomial \( F \in \mathbb{C}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) such that

\[
\forall A \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;Q\left( A\right)  = F\left( {{f}_{1}\left( A\right) ,\ldots ,{f}_{n}\left( A\right) }\right) .
\]

Solution. a) Il s’agit de prouver que \( {P}_{AB} = {P}_{BA} \) pour tous \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , ce qui est précisément le résultat démontré dans l'exercice 3 page 197.

> Solution. a) It is a matter of proving that \( {P}_{AB} = {P}_{BA} \) for all \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , which is precisely the result demonstrated in exercise 3 on page 197.

b) C'est plus délicat. Commençons par noter que deux matrices semblables prennent la même valeur par \( Q \) (si \( B = {P}^{-1}{AP} \) avec \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , on a \( Q\left( B\right) = Q\left( {\left( {{P}^{-1}A}\right) P}\right) = Q\left( {P\left( {{P}^{-1}A}\right) }\right) = \; Q\left( A\right) ) \) . Cette remarque va nous permettre de traiter aisément le cas des matrices diagonalisables, puis de toutes les matrices par densité (les matrices diagonalisables forment un ensemble dense dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , voir l’exercice 1 page 195).

> b) This is more delicate. Let us begin by noting that two similar matrices take the same value via \( Q \) (if \( B = {P}^{-1}{AP} \) with \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , we have \( Q\left( B\right) = Q\left( {\left( {{P}^{-1}A}\right) P}\right) = Q\left( {P\left( {{P}^{-1}A}\right) }\right) = \; Q\left( A\right) ) \) . This remark will allow us to easily handle the case of diagonalizable matrices, then all matrices by density (diagonalizable matrices form a dense set in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , see exercise 1 on page 195).

Pour tout \( n \) -uplet \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) de \( {\mathbb{C}}^{n} \) , on note \( D\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) la matrice diagonale dont le coefficient d’indice \( \left( {i, i}\right) \) est \( {\lambda }_{i} \) . L’application \( {\mathbb{C}}^{n} \rightarrow \mathbb{C}\;\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \mapsto Q\left( {D\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) }\right) \) est une fonction polynôme en les \( {\lambda }_{i} \) que l’on note \( \Pi \) .

> For any \( n \) -tuple \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) of \( {\mathbb{C}}^{n} \) , we denote by \( D\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) the diagonal matrix whose coefficient of index \( \left( {i, i}\right) \) is \( {\lambda }_{i} \) . The mapping \( {\mathbb{C}}^{n} \rightarrow \mathbb{C}\;\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \mapsto Q\left( {D\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) }\right) \) is a polynomial function in the \( {\lambda }_{i} \) which we denote by \( \Pi \) .

Supposons maintenant \( A \) diagonalisable et notons \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) ses valeurs propres. Pour toute permutation \( \sigma \in {\mathcal{S}}_{n}, A \) est semblable à la matrice diagonale \( {A}_{\sigma } = D\left( {{\lambda }_{\sigma \left( 1\right) },\ldots ,{\lambda }_{\sigma \left( n\right) }}\right) \) , ce qui prouve que

> Now suppose \( A \) is diagonalizable and denote its eigenvalues by \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) . For any permutation \( \sigma \in {\mathcal{S}}_{n}, A \) is similar to the diagonal matrix \( {A}_{\sigma } = D\left( {{\lambda }_{\sigma \left( 1\right) },\ldots ,{\lambda }_{\sigma \left( n\right) }}\right) \) , which proves that

\[
Q\left( A\right)  = Q\left( {A}_{\sigma }\right)  = \Pi \left( {{\lambda }_{\sigma \left( 1\right) },\ldots ,{\lambda }_{\sigma \left( n\right) }}\right) .
\]

Ceci étant vrai pour tout \( \sigma \in {\mathcal{S}}_{n} \) et pour toute matrice diagonalisable \( A \) , on en déduit que II est un polynôme symétrique en ses \( n \) variables. On peut donc l’écrire comme un polynôme \( F \) en les polynômes symétriques élémentaires \( {\sum }_{1},\ldots ,{\sum }_{n} \) (voir le théorème 1 page 84). On sait que la valeur \( {\sigma }_{i} \) prise par \( {\sum }_{i} \) au point \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) est \( {\left( -1\right) }^{i}{\alpha }_{i} \) où \( {\alpha }_{i} \) est le coefficient de \( {X}^{i} \) dans le polynôme \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) . Ce dernier polynôme étant égal à \( {\left( -1\right) }^{n}{P}_{A} \) , on en déduit que \( {\sigma }_{i} = {\left( -1\right) }^{i}{f}_{i}\left( A\right) \) . Finalement,

> Since this is true for any \( \sigma \in {\mathcal{S}}_{n} \) and for any diagonalizable matrix \( A \) , we deduce that II is a symmetric polynomial in its \( n \) variables. We can therefore write it as a polynomial \( F \) in the elementary symmetric polynomials \( {\sum }_{1},\ldots ,{\sum }_{n} \) (see theorem 1 on page 84). We know that the value \( {\sigma }_{i} \) taken by \( {\sum }_{i} \) at point \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \) is \( {\left( -1\right) }^{i}{\alpha }_{i} \) where \( {\alpha }_{i} \) is the coefficient of \( {X}^{i} \) in the polynomial \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) . Since this latter polynomial is equal to \( {\left( -1\right) }^{n}{P}_{A} \) , we deduce that \( {\sigma }_{i} = {\left( -1\right) }^{i}{f}_{i}\left( A\right) \) . Finally,

\[
Q\left( A\right)  = F\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  = F\left( {-{f}_{1}\left( A\right) ,\ldots ,{\left( -1\right) }^{n}{f}_{n}\left( A\right) }\right) .
\]

(*)

> Cette égalité est vraie pour toute matrice diagonalisable \( A \) . Les matrices diagonalisables formant un ensemble dense dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , les applications de l’égalité (*) étant des fonctions continues de \( A \) (ce sont des fonctions polynômes), on en déduit que (*) est vrai pour toute matrice \( A \) de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

This equality holds for any diagonalizable matrix \( A \) . Since diagonalizable matrices form a dense set in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , and the mappings in equality (*) are continuous functions of \( A \) (they are polynomial functions), we deduce that (*) is true for any matrix \( A \) in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Probleme 18 (Dérivée d'un Détrenminant, ALGORITHME DE FADDÉEV). Le but du problème est de proposer une méthode pratique efficace pour calculer le polynôme caractéristique d'une matrice.

Problem 18 (Derivative of a Determinant, FADDÉEV ALGORITHM). The goal of this problem is to propose an efficient practical method for calculating the characteristic polynomial of a matrix.

> 1/ (Dérivée d'un déterminant). On considère

1/ (Derivative of a determinant). Consider

\[
A : \mathbb{R} \rightarrow  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;t \mapsto  A\left( t\right)  = {\left( {a}_{i, j}\left( t\right) \right) }_{1 \leq  i, j \leq  n}
\]

une application dérivable sur \( \mathbb{R} \) . Montrer que l’application \( \varphi : t \mapsto \det \left( {A\left( t\right) }\right) \) est dérivable sur \( \mathbb{R} \) et que

> a differentiable mapping on \( \mathbb{R} \) . Show that the mapping \( \varphi : t \mapsto \det \left( {A\left( t\right) }\right) \) is differentiable on \( \mathbb{R} \) and that

\[
{\varphi }^{\prime }\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{C}_{1}\left( t\right) ,\ldots ,{C}_{i - 1}\left( t\right) ,{C}_{i}^{\prime }\left( t\right) ,{C}_{i + 1}\left( t\right) ,\ldots ,{C}_{n}\left( t\right) }\right) ,
\]

où \( {C}_{1}\left( t\right) ,\ldots ,{C}_{n}\left( t\right) \) désignent les vecteurs colonnes de la matrice \( A\left( t\right) \) .

> where \( {C}_{1}\left( t\right) ,\ldots ,{C}_{n}\left( t\right) \) denote the column vectors of the matrix \( A\left( t\right) \) .

2/ (Méthode de Faddéev pour le calcul du polynôme caractéristique). Soient \( \mathbb{K} \) un corps commutatif et une matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On note \( {\chi }_{A} = \det \left( {X{I}_{n} - A}\right) \) .

> 2/ (Faddéev's method for calculating the characteristic polynomial). Let \( \mathbb{K} \) be a commutative field and a matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Let \( {\chi }_{A} = \det \left( {X{I}_{n} - A}\right) \) .

a) Montrer que \( {\chi }_{A}^{\prime } = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) \) où \( \operatorname{com}\left( {X{I}_{n} - A}\right) \) désigne la comatrice de \( X{I}_{n} - A \) . b) On définit des matrices \( {B}_{0},\ldots ,{B}_{n - 1} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) par

> a) Show that \( {\chi }_{A}^{\prime } = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) \) where \( \operatorname{com}\left( {X{I}_{n} - A}\right) \) denotes the comatrix of \( X{I}_{n} - A \) . b) Define matrices \( {B}_{0},\ldots ,{B}_{n - 1} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) by

\[
{B}_{0} = {I}_{n}\;\text{ et }\;\forall k,1 \leq  k \leq  n - 1,\;{B}_{k} = A{B}_{k - 1} - \frac{\operatorname{tr}\left( {A{B}_{k - 1}}\right) }{k}{I}_{n}.
\]

Montrer

> Show

\[
{\chi }_{A}\left( X\right)  = {X}^{n} - \operatorname{tr}\left( {A{B}_{0}}\right) {X}^{n - 1} - \frac{\operatorname{tr}\left( {A{B}_{1}}\right) }{2}{X}^{n - 2} - \cdots  - \frac{\operatorname{tr}\left( {A{B}_{n - 1}}\right) }{n},
\]

et si \( A \) est inversible,

> and if \( A \) is invertible,

\[
{A}^{-1} = \frac{n}{\operatorname{tr}\left( {A{B}_{n - 1}}\right) }{B}_{n - 1}.
\]

Solution. 1/ L'expression

> Solution. 1/ The expression

\[
\varphi \left( t\right)  = \det A\left( t\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {a}_{\sigma \left( 1\right) ,1}\left( t\right) \cdots {a}_{\sigma \left( n\right) , n}\left( t\right)
\]

montre que \( \varphi \) est dérivable et permet d’obtenir, par dérivation,

> shows that \( \varphi \) is differentiable and allows us to obtain, by differentiation,

\[
{\varphi }^{\prime }\left( t\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) \left\lbrack  {\mathop{\sum }\limits_{{k = 1}}^{n}{a}_{\sigma \left( 1\right) ,1}\left( t\right) \cdots {a}_{\sigma \left( {k - 1}\right) , k - 1}\left( t\right) {a}_{\sigma \left( k\right) , k}^{\prime }\left( t\right) {a}_{\sigma \left( {k + 1}\right) , k + 1}\left( t\right) \cdots {a}_{\sigma \left( n\right) , n}\left( t\right) }\right\rbrack
\]

ce qui, en échangeant l'ordre des signes sommes, est précisément le résultat demandé.

> which, by swapping the order of the summation signs, is precisely the requested result.

2/a) Le résultat de la question 1/ reste valable pour les polynômes dérivés (la démonstration peut être reprise telle quelle). En l’appliquant au polynôme dérivé de \( {\chi }_{A}\left( X\right) = \det \left( {X{I}_{n} - A}\right) \) , on s’aperçoit que \( {\chi }_{A}^{\prime }\left( X\right) \) est la somme des cofacteurs des éléments diagonaux de \( X{I}_{n} - A \) , autrement \( \operatorname{dit}{\chi }_{A}^{\prime }\left( X\right) = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) . \)

> 2/a) The result of question 1/ remains valid for derivative polynomials (the proof can be repeated as is). By applying it to the derivative polynomial of \( {\chi }_{A}\left( X\right) = \det \left( {X{I}_{n} - A}\right) \), we notice that \( {\chi }_{A}^{\prime }\left( X\right) \) is the sum of the cofactors of the diagonal elements of \( X{I}_{n} - A \), otherwise \( \operatorname{dit}{\chi }_{A}^{\prime }\left( X\right) = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) . \)

b) Écrivons \( {\chi }_{A} = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n} \) . Chaque cofacteur de la matrice \( X{I}_{n} - A \) est un polynôme en \( X \) de degré au plus \( n - 1 \) , ce qui montre l’existence de matrices \( {B}_{0},\ldots ,{B}_{n - 1} \) telles que

> b) Let us write \( {\chi }_{A} = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n} \). Each cofactor of the matrix \( X{I}_{n} - A \) is a polynomial in \( X \) of degree at most \( n - 1 \), which shows the existence of matrices \( {B}_{0},\ldots ,{B}_{n - 1} \) such that

\[
{}^{\mathrm{t}}\operatorname{com}\left( {X{I}_{n} - A}\right)  = {B}_{0}{X}^{n - 1} + {B}_{1}{X}^{n - 2} + \cdots  + {B}_{n - 1}.
\]

L’égalité \( {\chi }_{A}^{\prime } = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) = \operatorname{tr}\left( {{}^{\mathrm{t}}\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) \) entraîne

> The equality \( {\chi }_{A}^{\prime } = \operatorname{tr}\left( {\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) = \operatorname{tr}\left( {{}^{\mathrm{t}}\operatorname{com}\left( {X{I}_{n} - A}\right) }\right) \) implies

\[
\left( {n - 1}\right) {a}_{1} = \operatorname{tr}\left( {B}_{1}\right) ,\;\ldots ,\;1 \cdot  {a}_{n - 1} = \operatorname{tr}\left( {B}_{n - 1}\right) .
\]

(*)

> Ceci étant, la relation \( {\left( X{I}_{n} - A\right) }^{\mathrm{t}}\operatorname{com}\left( {X{I}_{n} - A}\right) = \det \left( {X{I}_{n} - A}\right) {I}_{n} \) s’écrit

Given this, the relation \( {\left( X{I}_{n} - A\right) }^{\mathrm{t}}\operatorname{com}\left( {X{I}_{n} - A}\right) = \det \left( {X{I}_{n} - A}\right) {I}_{n} \) is written

\[
{B}_{0}{X}^{n} + \left( {{B}_{1} - A{B}_{0}}\right) {X}^{n - 1} + \cdots  + \left( {{B}_{n - 1} - A{B}_{n - 2}}\right) X - A{B}_{n - 1} = {\chi }_{A}\left( X\right) {I}_{n},
\]

ce qui en identifiant les coefficients donne

> which, by identifying the coefficients, gives

\[
{B}_{0} = {I}_{n},\;{B}_{1} - A{B}_{0} = {a}_{1}{I}_{n},\;\ldots ,\;{B}_{n - 1} - A{B}_{n - 2} = {a}_{n - 1}{I}_{n},\; - A{B}_{n - 1} = {a}_{n}{I}_{n},
\]

\( \left( {* * }\right) \)

> donc en prenant la trace

therefore, by taking the trace

\[
n{a}_{1} = \operatorname{tr}\left( {B}_{1}\right)  - \operatorname{tr}\left( {A{B}_{0}}\right) ,\;\ldots ,\;n{a}_{n - 1} = \operatorname{tr}\left( {{B}_{n - 1} - A{B}_{n - 2}}\right) ,\;n{a}_{n} =  - \operatorname{tr}\left( {A{B}_{n - 1}}\right) .
\]

En retranchant à chacune de ces égalités celles de (*), on obtient

> By subtracting the equalities of (*) from each of these, we obtain

\[
1 \cdot  {a}_{1} =  - \operatorname{tr}\left( {A{B}_{0}}\right) ,\;\ldots ,\;\left( {n - 1}\right) {a}_{n - 1} =  - \operatorname{tr}\left( {A{B}_{n - 2}}\right) ,\;n{a}_{n} =  - \operatorname{tr}\left( {A{B}_{n - 1}}\right) .
\]

\( \left( {* * * }\right) \)

> Ainsi, on a \( {a}_{k} = - \operatorname{tr}\left( {A{B}_{k - 1}}\right) /k \) , et en reportant ceci dans \( \left( {* * }\right) \) on obtient

Thus, we have \( {a}_{k} = - \operatorname{tr}\left( {A{B}_{k - 1}}\right) /k \), and by substituting this into \( \left( {* * }\right) \) we obtain

\[
{B}_{0} = {I}_{n},\;{B}_{1} = A{B}_{0} - \frac{\operatorname{tr}\left( {A{B}_{0}}\right) }{1}{I}_{n},\;\ldots ,\;{B}_{n - 1} = A{B}_{n - 2} - \frac{\operatorname{tr}\left( {A{B}_{n - 2}}\right) }{n - 1}{I}_{n}.
\]

relations qui permettent de définir les matrices \( {B}_{k} \) par récurrence, et on obtient avec (***) la première partie du résultat.

> relations that allow defining the matrices \( {B}_{k} \) by recurrence, and we obtain with (***) the first part of the result.

Lorsque \( A \) est inversible, la dernière égalité de (**) entraîne

> When \( A \) is invertible, the last equality of (**) implies

\[
{A}^{-1} =  - \frac{1}{{a}_{n}}{B}_{n - 1} = \frac{n}{\operatorname{tr}\left( {A{B}_{n - 1}}\right) }{B}_{n - 1}.
\]

Remarque. Cet algorithme permet en particulier d’obtenir le déterminant \( {\left( -1\right) }^{n}{a}_{n} \) de \( A \) . C'est une méthode beaucoup plus rapide que celle consistant à calculer det \( A \) en dévelop-pant récursivement les déterminants par rapport à une ligne ou une colonne, technique qui demande d'effectuer \( n \) ! opérations (ce qui est très coûteux lorsque \( n \) est grand).

> Remark. This algorithm allows in particular to obtain the determinant \( {\left( -1\right) }^{n}{a}_{n} \) of \( A \). It is a much faster method than calculating det \( A \) by recursively expanding the determinants with respect to a row or a column, a technique that requires performing \( n \)! operations (which is very costly when \( n \) is large).

Problem 19. \( \mathbf{1}/ \) Soit \( n \in {\mathbb{N}}^{ * } \) et \( \Omega \) le sous-ensemble de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) des matrices \( M \) telles que \( {\Pi }_{M} \) (polynôme minimal de \( M \) ) égale, au signe près, \( {P}_{M} \) (le polynôme caractéristique de \( M) \) . Montrer que \( \Omega \) est ouvert dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> Problem 19. \( \mathbf{1}/ \) Let \( n \in {\mathbb{N}}^{ * } \) and \( \Omega \) be the subset of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) of matrices \( M \) such that \( {\Pi }_{M} \) (minimal polynomial of \( M \)) equals, up to a sign, \( {P}_{M} \) (the characteristic polynomial of \( M) \)). Show that \( \Omega \) is open in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \).

2/ Soit \( M \in \Omega \) et \( {\left( {M}_{m}\right) }_{m \in \mathbb{N}} \) une suite de matrices de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tendant vers \( M \) et telle que pour tout \( m,{M}_{m} \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> 2/ Let \( M \in \Omega \) and \( {\left( {M}_{m}\right) }_{m \in \mathbb{N}} \) be a sequence of matrices in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) converging to \( M \) and such that for all \( m,{M}_{m} \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

a) Montrer qu’il existe \( \ell \in \mathbb{N} \) tel que pour tout \( m \geq \ell ,{M}_{m} \) a \( n \) valeurs propres distinctes deux à deux.

> a) Show that there exists \( \ell \in \mathbb{N} \) such that for all \( m \geq \ell ,{M}_{m} \) has \( n \) pairwise distinct eigenvalues.

b) Montrer qu’il existe \( K > 0 \) tel que pour tout \( m \) et pour toute valeur propre \( \lambda \) de \( {M}_{m} \) , \( \left| \lambda \right| \leq K \) .

> b) Show that there exists \( K > 0 \) such that for all \( m \) and for any eigenvalue \( \lambda \) of \( {M}_{m} \) , \( \left| \lambda \right| \leq K \) .

c) Pour tout \( m \geq \ell \) , on note \( {\lambda }_{1}\left( m\right) < \cdots < {\lambda }_{n}\left( m\right) \) les \( n \) valeurs propres de \( {M}_{m} \) . Pour tout \( i \in \{ 1,\ldots , n\} \) montrer que \( {\lambda }_{i} = \mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i}\left( m\right) \) existe. Montrer également que \( {\lambda }_{1} \leq \; \cdots \leq {\lambda }_{n} \) et que \( {P}_{M} = {\left( -1\right) }^{n}\left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{n}}\right) \) .

> c) For all \( m \geq \ell \) , let \( {\lambda }_{1}\left( m\right) < \cdots < {\lambda }_{n}\left( m\right) \) denote the \( n \) eigenvalues of \( {M}_{m} \) . For all \( i \in \{ 1,\ldots , n\} \) show that \( {\lambda }_{i} = \mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i}\left( m\right) \) exists. Also show that \( {\lambda }_{1} \leq \; \cdots \leq {\lambda }_{n} \) and that \( {P}_{M} = {\left( -1\right) }^{n}\left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{n}}\right) \) .

Solution. 1/ Dire que \( {\Pi }_{M} = {\left( -1\right) }^{n}{P}_{M} \) équivaut à dire que deg \( {\Pi }_{M} = n \) (car \( {\Pi }_{M} \) divise \( {P}_{M} \) ), ou encore que \( \left( {{I}_{n}, M,\ldots ,{M}^{n - 1}}\right) \) forme une famille libre de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> Solution. 1/ Saying that \( {\Pi }_{M} = {\left( -1\right) }^{n}{P}_{M} \) is equivalent to saying that deg \( {\Pi }_{M} = n \) (since \( {\Pi }_{M} \) divides \( {P}_{M} \) ), or that \( \left( {{I}_{n}, M,\ldots ,{M}^{n - 1}}\right) \) forms a linearly independent family of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

Soit \( M \in \Omega \) . La famille \( \left( {{I}_{n}, M,\ldots ,{M}^{n - 1}}\right) \) étant libre, on peut la compléter en une base \( {B}_{0} = \left( {{I}_{n}, M,\ldots ,{M}^{n - 1},{E}_{n + 1},\ldots ,{E}_{{n}^{2}}}\right) \) de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Fixons une base \( B \) de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . On définit l'application

> Let \( M \in \Omega \) . Since the family \( \left( {{I}_{n}, M,\ldots ,{M}^{n - 1}}\right) \) is linearly independent, it can be extended to a basis \( {B}_{0} = \left( {{I}_{n}, M,\ldots ,{M}^{n - 1},{E}_{n + 1},\ldots ,{E}_{{n}^{2}}}\right) \) of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Let us fix a basis \( B \) of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . We define the map

\[
\varphi  : {\mathcal{M}}_{n}\left( \mathbb{R}\right)  \rightarrow  \mathbb{R}\;N \mapsto  \mathop{\det }\limits_{B}\left( {{I}_{n}, N,\ldots ,{N}^{n - 1},{E}_{n + 1},\ldots ,{E}_{{n}^{2}}}\right) .
\]

L’application \( \varphi \) est continue et par construction, \( \varphi \left( M\right) \neq 0 \) . Il existe donc un voisinage \( V \) de \( M \) dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tel que pour tout \( N \in V,\varphi \left( N\right) \neq 0 \) . Ceci entraîne que pour tout \( N \in V \) , \( \left( {{I}_{n}, N,\ldots ,{N}^{n - 1}}\right) \) forme une famille libre de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , et donc \( V \subset \Omega \) . L’ensemble \( \Omega \) est donc ouvert.

> The map \( \varphi \) is continuous and by construction, \( \varphi \left( M\right) \neq 0 \) . There exists therefore a neighborhood \( V \) of \( M \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that for all \( N \in V,\varphi \left( N\right) \neq 0 \) . This implies that for all \( N \in V \) , \( \left( {{I}_{n}, N,\ldots ,{N}^{n - 1}}\right) \) forms a linearly independent family of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , and thus \( V \subset \Omega \) . The set \( \Omega \) is therefore open.

2/a) On a \( M \in \Omega \) et \( M \) est la limite de la suite \( \left( {M}_{m}\right) \) . Comme \( \Omega \) est ouvert, il existe \( \ell \in \mathbb{N} \) tel que pour tout \( m \geq \ell ,{M}_{m} \in \Omega \) . Pour tout \( m,{M}_{m} \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et \( {\Pi }_{{M}_{m}} \) est donc scindé sur \( \mathbb{R} \) ,à racines toutes simples. Or pour \( m \geq \ell \) , \( \deg {\Pi }_{{M}_{m}} = n,{\Pi }_{{M}_{m}} \) a donc \( n \) racines distinctes qui sont les valeurs propres de \( {M}_{m} \) , d’où le résultat.

> 2/a) We have \( M \in \Omega \) and \( M \) is the limit of the sequence \( \left( {M}_{m}\right) \) . Since \( \Omega \) is open, there exists \( \ell \in \mathbb{N} \) such that for all \( m \geq \ell ,{M}_{m} \in \Omega \) . For all \( m,{M}_{m} \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and \( {\Pi }_{{M}_{m}} \) is therefore split over \( \mathbb{R} \) , with all simple roots. However, for \( m \geq \ell \) , \( \deg {\Pi }_{{M}_{m}} = n,{\Pi }_{{M}_{m}} \) therefore has \( n \) distinct roots which are the eigenvalues of \( {M}_{m} \) , hence the result.

b) Soit \( \parallel .\parallel \) une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . La suite \( {\left( {M}_{m}\right) }_{m \in \mathbb{N}} \) converge donc est bornée, i. e. il existe \( K > 0 \) tel que pour tout \( m \in \mathbb{N},\begin{Vmatrix}{M}_{m}\end{Vmatrix} \leq K \) . D’après la proposition 1 page 193, pour tout \( m \in \mathbb{N} \) et pour toute valeur propre \( \lambda \) de \( {M}_{m} \) , on a \( \left| \lambda \right| \leq \begin{Vmatrix}{M}_{m}\end{Vmatrix} \leq K \) . c) Montrons d’abord que \( {P}_{M} \) est scindé sur \( \mathbb{R} \) . La suite

> b) Let \( \parallel .\parallel \) be an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . The sequence \( {\left( {M}_{m}\right) }_{m \in \mathbb{N}} \) converges and is therefore bounded, i.e., there exists \( K > 0 \) such that for all \( m \in \mathbb{N},\begin{Vmatrix}{M}_{m}\end{Vmatrix} \leq K \) . According to proposition 1 on page 193, for all \( m \in \mathbb{N} \) and for any eigenvalue \( \lambda \) of \( {M}_{m} \) , we have \( \left| \lambda \right| \leq \begin{Vmatrix}{M}_{m}\end{Vmatrix} \leq K \) . c) Let us first show that \( {P}_{M} \) is split over \( \mathbb{R} \) . The sequence

\[
{\left( \lambda \left( m\right) \right) }_{m \geq  \ell } = {\left\lbrack  \left( {\lambda }_{1}\left( m\right) ,\ldots ,{\lambda }_{n}\left( m\right) \right) \right\rbrack  }_{m \geq  \ell }
\]

prend ses valeurs dans le compact \( {\left\lbrack -K, K\right\rbrack }^{n} \) . On peut donc en extraire une sous-suite converger \( \lambda {\left( \varphi \left( m\right) \right) }_{m \in \mathbb{N}} \) . Soit \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}\lambda \left( {\varphi \left( n\right) }\right) \) . Pour tout \( m \) ,

> takes its values in the compact \( {\left\lbrack -K, K\right\rbrack }^{n} \) . We can therefore extract a convergent subsequence \( \lambda {\left( \varphi \left( m\right) \right) }_{m \in \mathbb{N}} \) . Let \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}\lambda \left( {\varphi \left( n\right) }\right) \) . For all \( m \) ,

\[
{P}_{{M}_{\varphi \left( m\right) }} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left\lbrack  {X - {\lambda }_{i}\left( {\varphi \left( m\right) }\right) }\right\rbrack
\]

donc \( {P}_{M} = \mathop{\lim }\limits_{{m \rightarrow \infty }}{P}_{{M}_{\varphi \left( m\right) }} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) est scindé sur \( \mathbb{R} \) . Comme pour tout \( m \) , \( {\lambda }_{1}\left( {\varphi \left( m\right) }\right) < \cdots < {\lambda }_{n}\left( {\varphi \left( m\right) }\right) \) , on obtient en passant à la limite \( {\lambda }_{1} \leq \cdots \leq {\lambda }_{n} \) .

> therefore \( {P}_{M} = \mathop{\lim }\limits_{{m \rightarrow \infty }}{P}_{{M}_{\varphi \left( m\right) }} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) is split over \( \mathbb{R} \) . Since for all \( m \) , \( {\lambda }_{1}\left( {\varphi \left( m\right) }\right) < \cdots < {\lambda }_{n}\left( {\varphi \left( m\right) }\right) \) , we obtain by passing to the limit \( {\lambda }_{1} \leq \cdots \leq {\lambda }_{n} \) .

Montrons maintenant que la suite \( {\left( \lambda \left( m\right) \right) }_{m \geq \ell } \) converge. Cette suite étant à valeur dans un compact, il suffit de montrer qu’elle n’admet qu’une seule valeur d’adhérence. Soit \( \mu = \; \left( {{\mu }_{1},\ldots ,{\mu }_{n}}\right) \) une valeur d’adhérence de \( {\left( \lambda \left( m\right) \right) }_{m \geq \ell } \) . Il existe une sous-suite \( (\lambda \left( {\psi \left( m\right) }\right) \) convergeant vers \( \mu \) . On a \( {\mu }_{1} \leq \cdots \leq {\mu }_{n} \) et

> Let us now show that the sequence \( {\left( \lambda \left( m\right) \right) }_{m \geq \ell } \) converges. Since this sequence takes values in a compact set, it suffices to show that it has only one limit point. Let \( \mu = \; \left( {{\mu }_{1},\ldots ,{\mu }_{n}}\right) \) be a limit point of \( {\left( \lambda \left( m\right) \right) }_{m \geq \ell } \). There exists a subsequence \( (\lambda \left( {\psi \left( m\right) }\right) \) converging to \( \mu \). We have \( {\mu }_{1} \leq \cdots \leq {\mu }_{n} \) and

\[
{P}_{M} = \mathop{\lim }\limits_{{m \rightarrow  \infty }}{P}_{{M}_{\psi \left( m\right) }} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\mu }_{i}}\right) .
\]

Des relations

> From the relations

\[
\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\mu }_{i}}\right) ,\;{\lambda }_{1} \leq  \cdots  \leq  {\lambda }_{n}\text{ et }{\mu }_{1} \leq  \cdots  \leq  {\mu }_{n},
\]

on tire \( {\mu }_{1} = {\lambda }_{1},\ldots ,{\mu }_{n} = {\lambda }_{n} \) , i. e. \( \lambda = \mu \) . L’élément \( \lambda \) est donc la seule valeur d’adhérence de \( {\left( \lambda \left( m\right) \right) }_{m > \ell } \) , donc cette suite étant à valeur dans un compact, elle converge vers \( \lambda \) . Pour tout \( i \) , on a donc \( {\lambda }_{i} = \mathop{\lim }\limits_{{n \rightarrow \infty }}{\lambda }_{i}\left( m\right) \) et on a vu que \( {P}_{M} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) , d’où le résultat.

> we derive \( {\mu }_{1} = {\lambda }_{1},\ldots ,{\mu }_{n} = {\lambda }_{n} \), i.e., \( \lambda = \mu \). The element \( \lambda \) is therefore the only limit point of \( {\left( \lambda \left( m\right) \right) }_{m > \ell } \), so since this sequence takes values in a compact set, it converges to \( \lambda \). For all \( i \), we therefore have \( {\lambda }_{i} = \mathop{\lim }\limits_{{n \rightarrow \infty }}{\lambda }_{i}\left( m\right) \) and we have seen that \( {P}_{M} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \), hence the result.

Remarque. La méthode utilisée tout au long de 2/ est à retenir. On procède souvent ainsi lorsqu'un polynôme est limite d'une suite de polynômes.

> Remark. The method used throughout 2/ should be remembered. We often proceed this way when a polynomial is the limit of a sequence of polynomials.

Problem 20. Soit \( n \in {\mathbb{N}}^{ * } \) et \( \Gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \mid \exists p \in {\mathbb{N}}^{ * },{M}^{p} = {I}_{n}}\right\} \) . Déterminer l’adhérence \( \overline{\Gamma } \) de \( \Gamma \) dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Problem 20. Let \( n \in {\mathbb{N}}^{ * } \) and \( \Gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \mid \exists p \in {\mathbb{N}}^{ * },{M}^{p} = {I}_{n}}\right\} \). Determine the closure \( \overline{\Gamma } \) of \( \Gamma \) in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \).

Solution. Notons \( \gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \mid \text{ pour toute valeur propre }\lambda \text{ de }M,\left| \lambda \right| = 1}\right\} \) . Nous allons montrer que \( \overline{\Gamma } = \gamma \) .

> Solution. Let \( \gamma = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \mid \text{ pour toute valeur propre }\lambda \text{ de }M,\left| \lambda \right| = 1}\right\} \). We will show that \( \overline{\Gamma } = \gamma \).

Montrons d’abord \( \overline{\Gamma } \subset \gamma \) . Soit \( M \in \overline{\Gamma } \) . On peut trouver une suite \( {\left( {M}_{p}\right) }_{p \in \mathbb{N}} \) de \( \Gamma \) telle que \( \mathop{\lim }\limits_{{p \rightarrow \infty }}{M}_{p} = M \) . Pour tout \( p \) , il existe \( q \in {\mathbb{N}}^{ * } \) tel que \( {M}_{p}^{q} = {I}_{n} \) , i. e. le polynôme \( {X}^{q} - 1 \) annule \( {M}_{p} \) . Toute valeur propre de \( {M}_{p} \) est donc racine de ce polynôme, donc de module 1. Pour tout \( p \) , on note \( {\lambda }_{1}\left( p\right) ,\ldots ,{\lambda }_{n}\left( p\right) \) les racines de \( {P}_{{M}_{p}} \) (polynôme caractéristique de \( {M}_{p} \) ). Pour tout \( i \) , on a vu que \( \left| {{\lambda }_{i}\left( p\right) }\right| = 1 \) , la suite \( \lambda \left( p\right) = \left( {{\lambda }_{1}\left( p\right) ,\ldots ,{\lambda }_{n}\left( p\right) }\right) \) est donc à valeurs dans le compact \( {C}^{n} \) , où \( C \) désigne le cercle unité complexe. On peut donc en extraire une sous-suite convergente \( \lambda \left( {\varphi \left( p\right) }\right) \) convergeant vers \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {C}^{n} \) . Pour tout \( i \) , on a \( \left| {\lambda }_{i}\right| = \mathop{\lim }\limits_{{p \rightarrow \infty }}\left| {{\lambda }_{i}\left( p\right) }\right| = 1 \) , et comme \( M = \mathop{\lim }\limits_{{p \rightarrow \infty }}{M}_{\varphi \left( p\right) }, \)

> Let us first show \( \overline{\Gamma } \subset \gamma \) . Let \( M \in \overline{\Gamma } \) . We can find a sequence \( {\left( {M}_{p}\right) }_{p \in \mathbb{N}} \) of \( \Gamma \) such that \( \mathop{\lim }\limits_{{p \rightarrow \infty }}{M}_{p} = M \) . For all \( p \) , there exists \( q \in {\mathbb{N}}^{ * } \) such that \( {M}_{p}^{q} = {I}_{n} \) , i.e., the polynomial \( {X}^{q} - 1 \) annihilates \( {M}_{p} \) . Any eigenvalue of \( {M}_{p} \) is therefore a root of this polynomial, and thus has modulus 1. For all \( p \) , we denote by \( {\lambda }_{1}\left( p\right) ,\ldots ,{\lambda }_{n}\left( p\right) \) the roots of \( {P}_{{M}_{p}} \) (characteristic polynomial of \( {M}_{p} \) ). For all \( i \) , we have seen that \( \left| {{\lambda }_{i}\left( p\right) }\right| = 1 \) , the sequence \( \lambda \left( p\right) = \left( {{\lambda }_{1}\left( p\right) ,\ldots ,{\lambda }_{n}\left( p\right) }\right) \) is therefore valued in the compact set \( {C}^{n} \) , where \( C \) denotes the complex unit circle. We can therefore extract a convergent subsequence \( \lambda \left( {\varphi \left( p\right) }\right) \) converging to \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {C}^{n} \) . For all \( i \) , we have \( \left| {\lambda }_{i}\right| = \mathop{\lim }\limits_{{p \rightarrow \infty }}\left| {{\lambda }_{i}\left( p\right) }\right| = 1 \) , and since \( M = \mathop{\lim }\limits_{{p \rightarrow \infty }}{M}_{\varphi \left( p\right) }, \)

\[
{P}_{M} = \mathop{\lim }\limits_{{p \rightarrow  \infty }}{P}_{{M}_{\varphi \left( p\right) }} = \mathop{\lim }\limits_{{p \rightarrow  \infty }}\mathop{\prod }\limits_{{i = 1}}^{n}\left\lbrack  {X - {\lambda }_{i}\left( {\varphi \left( p\right) }\right) }\right\rbrack   = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) .
\]

Les valeurs propres de \( M \) sont donc les \( {\lambda }_{i} \) et ont leur module égal à 1. Donc \( M \in \gamma \) .

> The eigenvalues of \( M \) are therefore the \( {\lambda }_{i} \) and have a modulus equal to 1. Thus \( M \in \gamma \) .

Montrons maintenant l’inclusion réciproque \( \gamma \subset \overline{\Gamma } \) . Soit \( M \in \gamma \) . Il existe une matrice \( Q \in \; \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que

> Let us now show the reverse inclusion \( \gamma \subset \overline{\Gamma } \) . Let \( M \in \gamma \) . There exists a matrix \( Q \in \; \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that

\[
{Q}^{-1}{MQ} = \left( \begin{matrix} {\lambda }_{1} &  \times  & \cdots &  \times  \\  0 & {\lambda }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\lambda }_{n} \end{matrix}\right) .
\]

Pour tout \( i,{\lambda }_{i} \) est valeur propre de \( M \) donc \( \left| {\lambda }_{i}\right| = 1 \) car \( M \in \gamma \) . En réfléchissant un peu, on voit qu’il existe une suite \( {\mu }_{p} = \left( {{\mu }_{1}\left( p\right) ,\ldots ,{\mu }_{n}\left( p\right) }\right) \) de \( {\mathbb{C}}^{n} \) vérifiant, pour tout \( p \in \mathbb{N} \) :

> For all \( i,{\lambda }_{i} \) is an eigenvalue of \( M \) so \( \left| {\lambda }_{i}\right| = 1 \) because \( M \in \gamma \) . By reflecting a little, we see that there exists a sequence \( {\mu }_{p} = \left( {{\mu }_{1}\left( p\right) ,\ldots ,{\mu }_{n}\left( p\right) }\right) \) of \( {\mathbb{C}}^{n} \) satisfying, for all \( p \in \mathbb{N} \) :

- Pour tout \( j \) et pour tout \( p \) , il existe \( r \in  \mathbb{Q} \) tel que \( {\mu }_{j}\left( p\right)  = \exp \left( {2i\pi r}\right) \) .

> - For all \( j \) and for all \( p \) , there exists \( r \in  \mathbb{Q} \) such that \( {\mu }_{j}\left( p\right)  = \exp \left( {2i\pi r}\right) \) .

- Les \( {\left( {\mu }_{i}\left( p\right) \right) }_{1 \leq  i \leq  n} \) sont distincts deux à deux.

> - The \( {\left( {\mu }_{i}\left( p\right) \right) }_{1 \leq  i \leq  n} \) are pairwise distinct.

- Pour tout \( i,\mathop{\lim }\limits_{{p \rightarrow  \infty }}{\mu }_{i}\left( p\right)  = {\lambda }_{i} \) .

> - For all \( i,\mathop{\lim }\limits_{{p \rightarrow  \infty }}{\mu }_{i}\left( p\right)  = {\lambda }_{i} \) .

Pour tout \( p \) , on pose

> For all \( p \) , we set

\[
{M}_{p} = \left( \begin{matrix} {\mu }_{1}\left( p\right) &  \times  & \cdots &  \times  \\  0 & {\mu }_{2}\left( p\right) &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\mu }_{n}\left( p\right)  \end{matrix}\right)
\]

(où la partie triangulaire supérieure est celle de \( {Q}^{-1}{MQ} \) ). Les \( {\mu }_{i}{\left( p\right) }_{1 \leq i \leq n} \) étant distincts, \( {M}_{p} \) est diagonalisable, donc semblable à la matrice diagonale \( {D}_{p} \) dont les éléments diagonaux sont ceux de \( {M}_{p} \) . Pour une valeur de \( p \) donnée, pour tout \( j,1 \leq j \leq n \) , on peut écrire \( {\mu }_{j}\left( p\right) = \exp \left( {{2i\pi }{a}_{j}/{b}_{j}}\right) \) où \( \left( {{a}_{j},{b}_{j}}\right) \in \mathbb{Z} \times {\mathbb{N}}^{ * } \) . Si \( q = \operatorname{ppcm}\left( {{b}_{1},\ldots ,{b}_{n}}\right) \) , on a \( {\mu }_{j}{\left( p\right) }^{q} = 1 \) pour tout \( j \) , donc \( {D}_{p}^{q} = {I}_{n} \) , donc \( {M}_{p}^{q} = {I}_{n} \) , c’est-à-dire pour tout \( p,{M}_{p} \in \Gamma \) . Or par construction, \( M = \mathop{\lim }\limits_{{p \rightarrow \infty }}Q{M}_{p}{Q}^{-1} \) . Comme pour tout \( p, Q{M}_{p}{Q}^{-1} \in \Gamma \) , on en déduit \( M \in \overline{\Gamma } \) .

> (where the upper triangular part is that of \( {Q}^{-1}{MQ} \) ). Since the \( {\mu }_{i}{\left( p\right) }_{1 \leq i \leq n} \) are distinct, \( {M}_{p} \) is diagonalizable, and therefore similar to the diagonal matrix \( {D}_{p} \) whose diagonal elements are those of \( {M}_{p} \) . For a given value of \( p \) , for any \( j,1 \leq j \leq n \) , we can write \( {\mu }_{j}\left( p\right) = \exp \left( {{2i\pi }{a}_{j}/{b}_{j}}\right) \) where \( \left( {{a}_{j},{b}_{j}}\right) \in \mathbb{Z} \times {\mathbb{N}}^{ * } \) . If \( q = \operatorname{ppcm}\left( {{b}_{1},\ldots ,{b}_{n}}\right) \) , we have \( {\mu }_{j}{\left( p\right) }^{q} = 1 \) for any \( j \) , thus \( {D}_{p}^{q} = {I}_{n} \) , thus \( {M}_{p}^{q} = {I}_{n} \) , that is to say for any \( p,{M}_{p} \in \Gamma \) . However, by construction, \( M = \mathop{\lim }\limits_{{p \rightarrow \infty }}Q{M}_{p}{Q}^{-1} \) . As for any \( p, Q{M}_{p}{Q}^{-1} \in \Gamma \) , we deduce \( M \in \overline{\Gamma } \) .

Probleme 21 (Théorème de Perron, MATRICES STOCHASTIQUES). Si \( A = \left( {a}_{i, j}\right) \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice, on note \( A \geq 0 \) si \( {a}_{i, j} \geq 0 \) pour tout \( \left( {i, j}\right) \) , et on note \( A > 0 \) si \( {a}_{i, j} > 0 \) pour tout \( \left( {i, j}\right) \) . Pour un vecteur \( X \in {\mathbb{R}}^{n} \) , on définit de la même manière les notations \( X \geq 0 \) et \( X > 0 \) . Si \( X, Y \) sont deux vecteurs de \( {\mathbb{R}}^{n} \) , on note \( X \geq Y \) (resp. \( X > Y) \) lorsque \( X - Y \geq 0 \) (resp. \( X - Y > 0 \) ).

> Problem 21 (Perron's Theorem, STOCHASTIC MATRICES). If \( A = \left( {a}_{i, j}\right) \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is a matrix, we denote \( A \geq 0 \) if \( {a}_{i, j} \geq 0 \) for all \( \left( {i, j}\right) \) , and we denote \( A > 0 \) if \( {a}_{i, j} > 0 \) for all \( \left( {i, j}\right) \) . For a vector \( X \in {\mathbb{R}}^{n} \) , we define the notations \( X \geq 0 \) and \( X > 0 \) in the same way. If \( X, Y \) are two vectors of \( {\mathbb{R}}^{n} \) , we denote \( X \geq Y \) (resp. \( X > Y) \) when \( X - Y \geq 0 \) (resp. \( X - Y > 0 \) ).

1/ (Théorème de Perron). Soit une matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que \( A > 0 \) .

> 1/ (Perron's Theorem). Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a matrix such that \( A > 0 \) .

a) On note \( \mathcal{S} \) l’ensemble des vecteurs \( X = \left( {x}_{i}\right) \in {\mathbb{R}}^{n} \) tels que \( X \geq 0 \) et \( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = 1 \) (de tels vecteurs sont appelés vecteurs de probabilité). Montrer que l'ensemble

> a) Let \( \mathcal{S} \) be the set of vectors \( X = \left( {x}_{i}\right) \in {\mathbb{R}}^{n} \) such that \( X \geq 0 \) and \( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = 1 \) (such vectors are called probability vectors). Show that the set

\[
\Lambda  = \{ \lambda  \in  \mathbb{R} \mid  \left( {\exists X \in  \mathcal{S}}\right) ,{AX} \geq  {\lambda X}\}
\]

est majoré et que sa borne supérieure \( {\lambda }_{0} \) est une valeur propre de \( A \) strictement positive associée à un vecteur propre \( X > 0 \) .

> is bounded above and that its supremum \( {\lambda }_{0} \) is a strictly positive eigenvalue of \( A \) associated with an eigenvector \( X > 0 \) .

b) Montrer que pour toute valeur propre complexe \( \lambda \neq {\lambda }_{0} \) de \( A \) , on a \( \left| \lambda \right| < {\lambda }_{0} \) (on dit alors que \( {\lambda }_{0} \) est valeur propre dominante de \( A \) ).

> b) Show that for any complex eigenvalue \( \lambda \neq {\lambda }_{0} \) of \( A \) , we have \( \left| \lambda \right| < {\lambda }_{0} \) (we then say that \( {\lambda }_{0} \) is the dominant eigenvalue of \( A \) ).

c) Montrer que le sous-espace propre \( {E}_{{\lambda }_{0}} \) de \( A \) associé à la valeur propre \( {\lambda }_{0} \) est de dimension 1.

> c) Show that the eigenspace \( {E}_{{\lambda }_{0}} \) of \( A \) associated with the eigenvalue \( {\lambda }_{0} \) has dimension 1.

d) Montrer que \( {\lambda }_{0} \) est racine simple du polynôme caractéristique de \( A \) (on dit alors que \( {\lambda }_{0} \) est valeur propre simple de \( A \) ). (Indication : raisonner par l’absurde en considérant deux vecteurs indépendants \( X \) et \( Y \) tels que \( X > 0 \) avec \( {AX} = {\lambda }_{0}X \) et \( {AY} = {\lambda }_{0}Y + {\alpha X} \) , puis considérer \( \left. {{A}^{k}Y}\right) \) .

> d) Show that \( {\lambda }_{0} \) is a simple root of the characteristic polynomial of \( A \) (we then say that \( {\lambda }_{0} \) is a simple eigenvalue of \( A \)). (Hint: reason by contradiction by considering two independent vectors \( X \) and \( Y \) such that \( X > 0 \) with \( {AX} = {\lambda }_{0}X \) and \( {AY} = {\lambda }_{0}Y + {\alpha X} \), then consider \( \left. {{A}^{k}Y}\right) \).)

2/ (Matrices stochastiques) Soit \( A = \left( {a}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice vérifiant \( A \geq 0 \) et telle que pour tout \( i \) , on a \( \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j} = 1 \) (on dit que \( A \) est une matrice stochastique).

> 2/ (Stochastic matrices) Let \( A = \left( {a}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a matrix satisfying \( A \geq 0 \) and such that for all \( i \), we have \( \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j} = 1 \) (we say that \( A \) is a stochastic matrix).

a) Si \( A > 0 \) , montrer que 1 est valeur propre simple et dominante de \( A \) .

> a) If \( A > 0 \), show that 1 is a simple and dominant eigenvalue of \( A \).

b) S’il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( {A}^{k} > 0 \) (on dit alors que \( A \) est régulière), montrer que 1 est valeur propre simple et dominante de \( A \) .

> b) If there exists \( k \in {\mathbb{N}}^{ * } \) such that \( {A}^{k} > 0 \) (we then say that \( A \) is regular), show that 1 is a simple and dominant eigenvalue of \( A \).

c) Si \( A \) est régulière, montrer que la suite de matrices \( \left( {A}^{k}\right) \) converge, et que sa limite est un projecteur de rang 1.

> c) If \( A \) is regular, show that the sequence of matrices \( \left( {A}^{k}\right) \) converges, and that its limit is a projection of rank 1.

---

Solution. \( 1/ \) a) L’ensemble \( \Lambda \) est non vide (car \( 0 \in \Lambda \) ) et évidemment majoré (par exemple par la somme des éléments de \( A \) ).

> Solution. \( 1/ \) a) The set \( \Lambda \) is non-empty (since \( 0 \in \Lambda \)) and obviously bounded above (for example by the sum of the elements of \( A \)).

---

Par définition de \( {\lambda }_{0} \) , il existe une suite \( \left( {X}_{n}\right) \) de \( \mathcal{S} \) et \( \left( {\gamma }_{n}\right) \) de \( \Lambda \) telle que

> By definition of \( {\lambda }_{0} \), there exists a sequence \( \left( {X}_{n}\right) \) of \( \mathcal{S} \) and \( \left( {\gamma }_{n}\right) \) of \( \Lambda \) such that

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\gamma }_{n} = {\lambda }_{0}\;\text{ et }\;\forall n, A{X}_{n} \geq  {\gamma }_{n}{X}_{n}
\]

L’ensemble \( \mathcal{S} \) est un fermé borné de \( {\mathbb{R}}^{n} \) , donc compact, de sorte que l’on peut extraire de la suite \( \left( {X}_{n}\right) \) une sous-suite convergente \( \left( {X}_{\varphi \left( n\right) }\right) \) . Notons \( X \in \mathcal{S} \) sa limite. Comme \( A{X}_{\varphi \left( n\right) } \geq {\gamma }_{\varphi \left( n\right) }{X}_{\varphi \left( n\right) } \) pour tout \( n \) , on obtient en passant à la limite sur chaque composante la relation \( {AX} \geq {\lambda }_{0}X \) . Si \( {AX} \neq {\lambda }_{0}X \) , en composant par \( A \) à gauche, on obtient, du fait que \( A > 0 \) , l’inégalité \( {AY} > {\lambda }_{0}Y \) , où \( Y = {AX} \) . Il existe donc \( \varepsilon > 0 \) suffisamment petit tel que \( {AY} > \left( {{\lambda }_{0} + \varepsilon }\right) Y \) , ce qui contredit la définition de \( {\lambda }_{0} \) car quitte à multiplier \( Y \) par une constante positive non nulle, on peut supposer \( Y \in \mathcal{S} \)

> The set \( \mathcal{S} \) is a closed and bounded subset of \( {\mathbb{R}}^{n} \), therefore compact, so we can extract from the sequence \( \left( {X}_{n}\right) \) a convergent subsequence \( \left( {X}_{\varphi \left( n\right) }\right) \). Let \( X \in \mathcal{S} \) be its limit. Since \( A{X}_{\varphi \left( n\right) } \geq {\gamma }_{\varphi \left( n\right) }{X}_{\varphi \left( n\right) } \) for all \( n \), we obtain by passing to the limit on each component the relation \( {AX} \geq {\lambda }_{0}X \). If \( {AX} \neq {\lambda }_{0}X \), by composing with \( A \) on the left, we obtain, given that \( A > 0 \), the inequality \( {AY} > {\lambda }_{0}Y \), where \( Y = {AX} \). There therefore exists \( \varepsilon > 0 \) sufficiently small such that \( {AY} > \left( {{\lambda }_{0} + \varepsilon }\right) Y \), which contradicts the definition of \( {\lambda }_{0} \) because, by multiplying \( Y \) by a non-zero positive constant, we can assume \( Y \in \mathcal{S} \)

Ainsi, \( {AX} = {\lambda }_{0}X \) avec \( X \in \mathcal{S} \) . Le fait que \( A > 0 \) entraîne \( {AX} > 0 \) , donc \( {\lambda }_{0}X > 0 \) et on en déduit \( X > 0 \) et \( {\lambda }_{0} > 0 \) .

> Thus, \( {AX} = {\lambda }_{0}X \) with \( X \in \mathcal{S} \) . The fact that \( A > 0 \) implies \( {AX} > 0 \) , so \( {\lambda }_{0}X > 0 \) and we deduce \( X > 0 \) and \( {\lambda }_{0} > 0 \) .

b) Soit \( \lambda \) une valeur propre de \( A \) , et notons \( Z \) un vecteur propre associé. Les \( \left( {z}_{i}\right) \) désignant les composantes de \( Z \) , on a

> b) Let \( \lambda \) be an eigenvalue of \( A \) , and let \( Z \) denote an associated eigenvector. Letting \( \left( {z}_{i}\right) \) denote the components of \( Z \) , we have

\[
\forall i,\;\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}{z}_{j} = \lambda {z}_{i}\;\text{ donc }\;\forall i,\;\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}\left| {z}_{j}\right|  \geq  \left| \lambda \right|  \cdot  \left| {z}_{i}\right| .
\]

En d’autres termes, \( A\left| Z\right| \geq \left| \lambda \right| \left| Z\right| \) où \( \left| Z\right| \) désigne le vecteur dont les composantes sont les \( \left| {z}_{i}\right| \) , ce qui prouve que \( \left| \lambda \right| \in \Lambda \) (car quitte à multiplier \( \left| Z\right| \) par une constante non nulle, on peut supposer \( \left| Z\right| \in \mathcal{S}) \) , et donc \( \left| \lambda \right| \leq {\lambda }_{0} \) par définition de \( {\lambda }_{0} \) .

> In other words, \( A\left| Z\right| \geq \left| \lambda \right| \left| Z\right| \) where \( \left| Z\right| \) denotes the vector whose components are the \( \left| {z}_{i}\right| \) , which proves that \( \left| \lambda \right| \in \Lambda \) (since, by multiplying \( \left| Z\right| \) by a non-zero constant, we can assume \( \left| Z\right| \in \mathcal{S}) \) , and thus \( \left| \lambda \right| \leq {\lambda }_{0} \) by definition of \( {\lambda }_{0} \) .

Il nous reste à prouver que si \( \lambda \neq {\lambda }_{0} \) , alors \( \left| \lambda \right| < {\lambda }_{0} \) . Supposons \( \left| \lambda \right| = {\lambda }_{0} \) . Comme \( A > 0 \) , il existe \( \delta > 0 \) suffisamment petit tel que \( {A}_{\delta } = A - \delta {I}_{n} > 0 \) . Comme \( {\lambda }_{0} \) est la plus grande valeur propre réelle positive de \( A,{\lambda }_{0} - \delta \) est la plus grande valeur propre réelle positive de \( {A}_{\delta } \) . En répétant l’argument précédent à la matrice \( {A}_{\delta } \) et à la valeur propre \( \lambda - \delta \) , on obtient \( \left| {\lambda - \delta }\right| \leq {\lambda }_{0} - \delta \) . Mais

> It remains for us to prove that if \( \lambda \neq {\lambda }_{0} \) , then \( \left| \lambda \right| < {\lambda }_{0} \) . Suppose \( \left| \lambda \right| = {\lambda }_{0} \) . Since \( A > 0 \) , there exists \( \delta > 0 \) sufficiently small such that \( {A}_{\delta } = A - \delta {I}_{n} > 0 \) . Since \( {\lambda }_{0} \) is the largest positive real eigenvalue of \( A,{\lambda }_{0} - \delta \) is the largest positive real eigenvalue of \( {A}_{\delta } \) . By repeating the previous argument for the matrix \( {A}_{\delta } \) and the eigenvalue \( \lambda - \delta \) , we obtain \( \left| {\lambda - \delta }\right| \leq {\lambda }_{0} - \delta \) . But

\[
{\lambda }_{0} = \left| \lambda \right|  = \left| {\lambda  - \delta  + \delta }\right|  \leq  \left| {\lambda  - \delta }\right|  + \delta  \leq  {\lambda }_{0},
\]

de sorte que \( \left| \lambda \right| = \left| {\lambda - \delta }\right| + \delta \) , ce qui n’est possible que si \( \lambda \) est un réel positif. Donc \( \lambda = \left| \lambda \right| = {\lambda }_{0} \) , ce qui contredit le fait que \( \lambda \neq {\lambda }_{0} \) . Donc \( \left| \lambda \right| < {\lambda }_{0} \) .

> so that \( \left| \lambda \right| = \left| {\lambda - \delta }\right| + \delta \) , which is only possible if \( \lambda \) is a positive real number. Thus \( \lambda = \left| \lambda \right| = {\lambda }_{0} \) , which contradicts the fact that \( \lambda \neq {\lambda }_{0} \) . Therefore \( \left| \lambda \right| < {\lambda }_{0} \) .

c) D’après a), il existe \( X > 0 \) tel que \( X \in {E}_{{\lambda }_{0}} \) . Supposons dim \( {E}_{{\lambda }_{0}} \geq 2 \) , de sorte qu’il existe un vecteur réel \( Y \in {E}_{{\lambda }_{0}} \) tel que la famille \( \left( {X, Y}\right) \) soit libre. Choisissons \( \mu \) tel que \( X - {\mu Y} \geq 0 \) et \( X - {\mu Y} \ngtr 0 \) (on a \( \mu = \inf \left\{ {{x}_{i}/{y}_{i} \mid {y}_{i} \neq 0}\right\} \) ). Comme \( \left( {X, Y}\right) \) est une famille libre, \( X - {\mu Y} \) n’est pas nul, et comme \( A > 0 \) et \( X - {\mu Y} \geq 0 \) , on a facilement \( A\left( {X - {\mu Y}}\right) > 0 \) , c’est-à-dire \( {\lambda }_{0}\left( {X - {\mu Y}}\right) > 0 \) (c'est le même argument que dans a)), donc \( X - {\mu Y} > 0 \) . Ceci est en contradiction avec le choix de \( \mu \) . Ainsi, \( \dim {E}_{{\lambda }_{0}} = 1 \) .

> c) According to a), there exists \( X > 0 \) such that \( X \in {E}_{{\lambda }_{0}} \) . Suppose dim \( {E}_{{\lambda }_{0}} \geq 2 \) , so that there exists a real vector \( Y \in {E}_{{\lambda }_{0}} \) such that the family \( \left( {X, Y}\right) \) is linearly independent. Let us choose \( \mu \) such that \( X - {\mu Y} \geq 0 \) and \( X - {\mu Y} \ngtr 0 \) (we have \( \mu = \inf \left\{ {{x}_{i}/{y}_{i} \mid {y}_{i} \neq 0}\right\} \) ). Since \( \left( {X, Y}\right) \) is a linearly independent family, \( X - {\mu Y} \) is non-zero, and since \( A > 0 \) and \( X - {\mu Y} \geq 0 \) , we easily have \( A\left( {X - {\mu Y}}\right) > 0 \) , that is to say \( {\lambda }_{0}\left( {X - {\mu Y}}\right) > 0 \) (this is the same argument as in a)), therefore \( X - {\mu Y} > 0 \) . This contradicts the choice of \( \mu \) . Thus, \( \dim {E}_{{\lambda }_{0}} = 1 \) .

d) Supposons que \( {\lambda }_{0} \) est racine d’ordre \( \geq 2 \) de \( {P}_{A} \) . D’après \( 1/\mathrm{a} \) ), il existe un vecteur propre \( X \geq 0 \) de \( A \) vérifiant \( {AX} = {\lambda }_{0}X \) . Complétons \( X \) en une base \( \mathcal{B} = \left( {X,{X}_{2},\ldots ,{X}_{n}}\right) \) de \( {\mathbb{R}}^{n} \) et notons \( P \) la matrice dont les vecteurs colonnes sont ceux de \( \mathcal{B} \) . On a

> d) Suppose that \( {\lambda }_{0} \) is a root of order \( \geq 2 \) of \( {P}_{A} \) . According to \( 1/\mathrm{a} \) ), there exists an eigenvector \( X \geq 0 \) of \( A \) satisfying \( {AX} = {\lambda }_{0}X \) . Let us complete \( X \) into a basis \( \mathcal{B} = \left( {X,{X}_{2},\ldots ,{X}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) and denote by \( P \) the matrix whose column vectors are those of \( \mathcal{B} \) . We have

\[
{P}^{-1}{AP} = \left( \begin{matrix} \left. \begin{matrix} {\lambda }_{0} \\  0 \end{matrix}\right| &  \times  & \cdots &  \times  \\   \vdots  & B & & \\  0 & & &  \end{matrix}\right) \;\text{ avec }\;B \in  {\mathcal{M}}_{n - 1}\left( \mathbb{R}\right) .
\]

L’égalité \( {P}_{A} = \left( {{\lambda }_{0} - X}\right) {P}_{B} \) montre que \( {\lambda }_{0} \) est racine du polynôme caractéristique \( {P}_{B} \) de \( B \) (car \( {\lambda }_{0} \) est racine d’ordre \( \geq 2 \) de \( {P}_{A} \) par hypothèse), donc valeur propre de \( B \) . Ainsi, il existe \( Z \in {\mathbb{R}}^{n - 1} \) non nul tel que \( {BZ} = {\lambda }_{0}Z \) , donc le vecteur \( Y = P\left( \begin{array}{l} 0 \\ Z \end{array}\right) \) vérifie \( {AY} = {\lambda }_{0}Y + {\alpha X} \) avec \( \alpha \in \mathbb{R} \) (en d’autres termes, on a commencé à triangulariser la matrice \( A \) à partir de la valeur propre \( {\lambda }_{0} \) , et on a considéré les deux premiers vecteurs \( X \) et \( Y \) de la base correspondante). On a forcément \( \alpha \neq 0 \) sinon \( Y \) serait un vecteur propre de \( A \) , et comme la famille \( \left( {X, Y}\right) \) est libre, ceci est impossible compte tenu du résultat obtenu précédemment. Maintenant, l'égalité \( {AY} = {\lambda }_{0}Y + {\alpha X} \) donne facilement \( {A}^{k}Y = {\lambda }_{0}^{k}Y + {k\alpha }{\lambda }_{0}^{k - 1}X \) pour tout \( k \in {\mathbb{N}}^{ * } \) . Comme \( {A}^{k} \geq 0 \) , on en déduit

> The equality \( {P}_{A} = \left( {{\lambda }_{0} - X}\right) {P}_{B} \) shows that \( {\lambda }_{0} \) is a root of the characteristic polynomial \( {P}_{B} \) of \( B \) (since \( {\lambda }_{0} \) is a root of order \( \geq 2 \) of \( {P}_{A} \) by hypothesis), and therefore an eigenvalue of \( B \). Thus, there exists a non-zero \( Z \in {\mathbb{R}}^{n - 1} \) such that \( {BZ} = {\lambda }_{0}Z \), so the vector \( Y = P\left( \begin{array}{l} 0 \\ Z \end{array}\right) \) satisfies \( {AY} = {\lambda }_{0}Y + {\alpha X} \) with \( \alpha \in \mathbb{R} \) (in other words, we have begun to triangularize the matrix \( A \) starting from the eigenvalue \( {\lambda }_{0} \), and we have considered the first two vectors \( X \) and \( Y \) of the corresponding basis). We must have \( \alpha \neq 0 \), otherwise \( Y \) would be an eigenvector of \( A \), and since the family \( \left( {X, Y}\right) \) is linearly independent, this is impossible given the result obtained previously. Now, the equality \( {AY} = {\lambda }_{0}Y + {\alpha X} \) easily gives \( {A}^{k}Y = {\lambda }_{0}^{k}Y + {k\alpha }{\lambda }_{0}^{k - 1}X \) for all \( k \in {\mathbb{N}}^{ * } \). Since \( {A}^{k} \geq 0 \), we deduce

\[
{A}^{k}\left| Y\right|  \geq  \left| {{A}^{k}Y}\right|  = \left| {{\lambda }_{0}^{k}Y + {k\alpha }{\lambda }_{0}^{k - 1}X}\right|  \geq  \left| {{k\alpha }{\lambda }_{0}^{k - 1}X}\right|  - \left| {{\lambda }_{0}^{k}Y}\right|  = {\lambda }_{0}^{k - 1}\left( {k\left| {\alpha X}\right|  - {\lambda }_{0}\left| Y\right| }\right) .
\]

Comme \( \alpha \neq 0 \) et \( X > 0 \) , il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( k\left| {\alpha X}\right| - {\lambda }_{0}\left| Y\right| > {\lambda }_{0}\left| Y\right| \) , ce qui entraîne \( {A}^{k}\left| Y\right| > {\lambda }_{0}^{k}\left| Y\right| \) . Comme \( {A}^{k} > 0 \) , ceci entraîne, d’après le résultat de la question 1/a), que \( {A}^{k} \) a une valeur propre \( > {\lambda }_{0}^{k} \) . Or les valeurs propres de \( {A}^{k} \) sont les puissances \( k \) -ièmes des valeurs propres de \( A \) , et ces dernières sont de module \( \leq {\lambda }_{0} \) d’après \( 1/\mathrm{b} \) ), ce qui est absurde. Ainsi, \( {\lambda }_{0} \) est bien racine simple de \( {P}_{A} \) .

> Since \( \alpha \neq 0 \) and \( X > 0 \), there exists \( k \in {\mathbb{N}}^{ * } \) such that \( k\left| {\alpha X}\right| - {\lambda }_{0}\left| Y\right| > {\lambda }_{0}\left| Y\right| \), which implies \( {A}^{k}\left| Y\right| > {\lambda }_{0}^{k}\left| Y\right| \). Since \( {A}^{k} > 0 \), this implies, according to the result of question 1/a), that \( {A}^{k} \) has an eigenvalue \( > {\lambda }_{0}^{k} \). However, the eigenvalues of \( {A}^{k} \) are the \( k \)-th powers of the eigenvalues of \( A \), and the latter have modulus \( \leq {\lambda }_{0} \) according to \( 1/\mathrm{b} \), which is absurd. Thus, \( {\lambda }_{0} \) is indeed a simple root of \( {P}_{A} \).

2/a) La matrice \( A \) vérifiant \( A > 0 \) , on peut lui appliquer les résultats précédents. Soit \( X = \; {\left( {x}_{i}\right) }_{1 \leq i \leq n} \in \mathcal{S} \) un vecteur de probabilité. Soit \( k \) tel que \( {x}_{k} = \mathop{\sup }\limits_{i}{x}_{i} \) . Soit \( Y = \left( {y}_{i}\right) \) le vecteur \( Y = \overline{AX} \) . On a \( {y}_{k} = \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{k, j}{x}_{j} \leq \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{k, j}{x}_{k} = {x}_{k} \) . Ainsi, si \( {AX} \geq {\lambda X} \) avec \( \lambda \in \mathbb{R} \) , alors en extrayant la \( k \) -ième composante on en déduit \( {y}_{k} \geq \lambda {x}_{k} \) , donc \( \lambda \leq 1 \) car \( {y}_{k} \leq {x}_{k} \) . En reprenant les notations de la question \( 1/\mathrm{a} \) ), nous avons montré que sup \( \Lambda \leq 1 \) , donc la valeur propre \( {\lambda }_{0} \) vérifie \( {\lambda }_{0} \leq 1 \) . Maintenant on remarque que le vecteur \( {X}_{0} \) dont toutes les coordonnées sont égales à1 vérifie \( A{X}_{0} = {X}_{0} \) , donc 1 est valeur propre de \( A \) , donc on a forcément \( {\lambda }_{0} \geq 1 \) . Ainsi, on a \( {\lambda }_{0} = 1 \) , D'après le résultat de la question 1/b), on en déduit que 1 est valeur propre dominante de \( A \) , et d'après 1/c), que cette valeur propre est simple.

> 2/a) Since the matrix \( A \) satisfies \( A > 0 \), we can apply the previous results to it. Let \( X = \; {\left( {x}_{i}\right) }_{1 \leq i \leq n} \in \mathcal{S} \) be a probability vector. Let \( k \) be such that \( {x}_{k} = \mathop{\sup }\limits_{i}{x}_{i} \). Let \( Y = \left( {y}_{i}\right) \) be the vector \( Y = \overline{AX} \). We have \( {y}_{k} = \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{k, j}{x}_{j} \leq \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{k, j}{x}_{k} = {x}_{k} \). Thus, if \( {AX} \geq {\lambda X} \) with \( \lambda \in \mathbb{R} \), then by extracting the \( k \)-th component we deduce \( {y}_{k} \geq \lambda {x}_{k} \), therefore \( \lambda \leq 1 \) because \( {y}_{k} \leq {x}_{k} \). Returning to the notation from question \( 1/\mathrm{a} \)), we have shown that sup \( \Lambda \leq 1 \), so the eigenvalue \( {\lambda }_{0} \) satisfies \( {\lambda }_{0} \leq 1 \). Now we note that the vector \( {X}_{0} \) whose coordinates are all equal to 1 satisfies \( A{X}_{0} = {X}_{0} \), so 1 is an eigenvalue of \( A \), therefore we necessarily have \( {\lambda }_{0} \geq 1 \). Thus, we have \( {\lambda }_{0} = 1 \). Based on the result of question 1/b), we deduce that 1 is the dominant eigenvalue of \( A \), and according to 1/c), that this eigenvalue is simple.

b) Remarquons qu’une matrice \( A \geq 0 \) est stochastique si et seulement si elle vérifie \( A{X}_{0} = {X}_{0} \) , où \( {X}_{0} \) est le vecteur dont toutes les coordonnées sont égales à 1. Ainsi, si \( A \) et \( B \) sont deux matrices stochastiques, le produit \( {AB} \) vérifie \( {AB} \geq 0 \) (c’est immédiat) et de plus \( {AB}{X}_{0} = A{X}_{0} = {X}_{0} \) donc \( {AB} \) est stochastique. On en déduit que \( {A}^{k} \) est une matrice stochastique. Comme de plus \( {A}^{k} > 0 \) par hypothèse, le résultat de la question précédente entraîne que 1 est valeur propre simple et dominante de \( {A}^{k} \) .

> b) Note that a matrix \( A \geq 0 \) is stochastic if and only if it satisfies \( A{X}_{0} = {X}_{0} \), where \( {X}_{0} \) is the vector whose coordinates are all equal to 1. Thus, if \( A \) and \( B \) are two stochastic matrices, the product \( {AB} \) satisfies \( {AB} \geq 0 \) (this is immediate) and furthermore \( {AB}{X}_{0} = A{X}_{0} = {X}_{0} \), so \( {AB} \) is stochastic. We deduce that \( {A}^{k} \) is a stochastic matrix. Since, in addition, \( {A}^{k} > 0 \) by hypothesis, the result of the previous question implies that 1 is a simple and dominant eigenvalue of \( {A}^{k} \).

L’égalité \( A{X}_{0} = {X}_{0} \) montre que 1 est valeur propre de \( A \) . Si \( \lambda \neq 1 \) est une autre valeur propre de \( A \) associée à un vecteur propre \( {X}_{1} \) , alors \( {\lambda }^{k} \) est valeur propre de \( {A}^{k} \) associée au même vecteur propre, donc \( \left| {\lambda }^{k}\right| < 1 \) ou \( {\lambda }^{k} = 1 \) . Si \( {\lambda }^{k} = 1 \) alors \( {A}^{k}{X}_{1} = {X}_{1} \) , donc 1 serait valeur propre non simple de \( {A}^{k} \) (on a également \( {A}^{k}{X}_{0} = {X}_{0} \) et les vecteurs \( {X}_{0} \) et \( {X}_{1} \) sont bien indépendants car associés à des valeurs propres distinctes de \( A \) ), ce qui est absurde. Donc \( \left| {\lambda }^{k}\right| < 1 \) , ce qui montre que 1 est bien valeur propre dominante de \( A \) .

> The equality \( A{X}_{0} = {X}_{0} \) shows that 1 is an eigenvalue of \( A \). If \( \lambda \neq 1 \) is another eigenvalue of \( A \) associated with an eigenvector \( {X}_{1} \), then \( {\lambda }^{k} \) is an eigenvalue of \( {A}^{k} \) associated with the same eigenvector, so \( \left| {\lambda }^{k}\right| < 1 \) or \( {\lambda }^{k} = 1 \). If \( {\lambda }^{k} = 1 \), then \( {A}^{k}{X}_{1} = {X}_{1} \), so 1 would be a non-simple eigenvalue of \( {A}^{k} \) (we also have \( {A}^{k}{X}_{0} = {X}_{0} \) and the vectors \( {X}_{0} \) and \( {X}_{1} \) are indeed independent because they are associated with distinct eigenvalues of \( A \)), which is absurd. Therefore \( \left| {\lambda }^{k}\right| < 1 \), which shows that 1 is indeed the dominant eigenvalue of \( A \).

Enfin,1 est bien valeur propre simple de \( A \) , car en triangularisant \( A \) , on s’aperçoit que les valeurs propres de \( {A}^{k} \) (en comptant leur multiplicité dans le polynôme caractéristique) sont les puissances \( k \) -ièmes de celles de \( A \) . Ainsi, si 1 n’était pas valeur propre simple de \( A,1 \) ne serait pas valeur propre simple de \( {A}^{k} \) .

> Finally, 1 is indeed a simple eigenvalue of \( A \), because by triangularizing \( A \), we see that the eigenvalues of \( {A}^{k} \) (counting their multiplicity in the characteristic polynomial) are the \( k \)-th powers of those of \( A \). Thus, if 1 were not a simple eigenvalue of \( A,1 \), it would not be a simple eigenvalue of \( {A}^{k} \).

c) Comme 1 est valeur propre simple de \( A \) , la décomposition de Dunford assure l’existence d’une matrice \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que

> c) Since 1 is a simple eigenvalue of \( A \), the Dunford decomposition ensures the existence of a matrix \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that

\[
T = {P}^{-1}{AP} = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & B & \\  0 & & &  \end{matrix}\right) \;\text{ avec }\;B \in  {\mathcal{M}}_{n - 1}\left( \mathbb{R}\right) ,
\]

où \( B = D + N \) , avec \( D \) une matrice diagonale et \( N \) une matrice nilpotente, telles que \( {DN} = {ND} \) . Comme 1 est valeur propre dominante de \( A \) , les valeurs diagonales \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n - 1} \) de \( D \) vérifient \( \left| {\lambda }_{i}\right| < 1 \) . Comme les matrices \( D \) et \( N \) commutent, on a

> where \( B = D + N \), with \( D \) a diagonal matrix and \( N \) a nilpotent matrix, such that \( {DN} = {ND} \). Since 1 is the dominant eigenvalue of \( A \), the diagonal values \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n - 1} \) of \( D \) satisfy \( \left| {\lambda }_{i}\right| < 1 \). Since the matrices \( D \) and \( N \) commute, we have

\[
\forall k \geq  n,\;{B}^{k} = {\left( D + N\right) }^{k} = \mathop{\sum }\limits_{{j = 0}}^{k}\left( \begin{array}{l} k \\  j \end{array}\right) {D}^{k - j}{N}^{j} = \mathop{\sum }\limits_{{j = 0}}^{n}\left( \begin{array}{l} k \\  j \end{array}\right) {D}^{k - j}{N}^{j},
\]

car \( {N}^{j} = 0 \) pour \( j > n \) . Choisissons une norme quelconque de l’espace des vecteurs, et normons l’espace des matrices par la norme d’algèbre \( \parallel M\parallel = \mathop{\sup }\limits_{{\parallel X\parallel = 1}}\parallel {MX}\parallel \) . On a \( \parallel D\parallel < 1 \) car \( \parallel D\parallel \) est le maximum des modules \( \left| {\lambda }_{i}\right| \) de ses termes diagonaux. L’égalité précédente entraîne

> because \( {N}^{j} = 0 \) for \( j > n \). Let us choose any norm on the vector space, and norm the space of matrices by the algebra norm \( \parallel M\parallel = \mathop{\sup }\limits_{{\parallel X\parallel = 1}}\parallel {MX}\parallel \). We have \( \parallel D\parallel < 1 \) because \( \parallel D\parallel \) is the maximum of the moduli \( \left| {\lambda }_{i}\right| \) of its diagonal terms. The previous equality implies

\[
\begin{Vmatrix}{B}^{k}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{j = 0}}^{n}\left( \begin{array}{l} k \\  j \end{array}\right) \parallel D{\parallel }^{k - j}\parallel N{\parallel }^{j} \leq  \parallel D{\parallel }^{k - n}\mathop{\sum }\limits_{{j = 0}}^{n}\left( \begin{array}{l} k \\  j \end{array}\right) \parallel N{\parallel }^{j} \leq  \parallel D{\parallel }^{k - n}\mathop{\sum }\limits_{{j = 0}}^{n}{k}^{j}\parallel N{\parallel }^{j}.
\]

Ainsi, \( \begin{Vmatrix}{B}^{k}\end{Vmatrix} \) est majoré par \( \parallel D{\parallel }^{k - n}F\left( k\right) \) où \( F \) est une fonction polynôme. Comme \( \parallel D\parallel < 1 \) ceci entraîne \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{B}^{k} = 0 \) . On a

> Thus, \( \begin{Vmatrix}{B}^{k}\end{Vmatrix} \) is bounded by \( \parallel D{\parallel }^{k - n}F\left( k\right) \) where \( F \) is a polynomial function. Since \( \parallel D\parallel < 1 \), this implies \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{B}^{k} = 0 \). We have

\[
{A}^{k} = P\left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & {B}^{k} & \\  0 & & &  \end{matrix}\right) {P}^{-1}\text{ donc }\mathop{\lim }\limits_{{k \rightarrow  \infty }}{A}^{k} = \pi ,\;\pi  = P\left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & 0 & \\  0 & & &  \end{matrix}\right) {P}^{-1}.
\]

La matrice \( \pi \) est de rang 1 et vérifie \( {\pi }^{2} = \pi \) , c’est donc bien un projecteur.

> The matrix \( \pi \) has rank 1 and satisfies \( {\pi }^{2} = \pi \), so it is indeed a projector.

Remarque. Le théorème de Perron s’étend au cas où \( A \geq 0 \) , avec des résultats plus faibles. Il est également vrai sous des hypothèses différentes (théorème de Frobenius sur les matrices irréductibles). Les matrices stochastiques apparaissent dans l'étude des chaînes de Markov à espace d'états finis.

> Remark. Perron's theorem extends to the case where \( A \geq 0 \), with weaker results. It is also true under different hypotheses (Frobenius theorem on irreducible matrices). Stochastic matrices appear in the study of Markov chains with a finite state space.

Problem 22 (ENDOMORPHISMES SEMI-SIMPLES). Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie. On dit que \( f \in \mathcal{L}\left( E\right) \) est semi-simple si pour tout s.e.v \( F \) de \( E \) stable par \( f \) , il existe un supplémentaire \( S \) de \( F \) stable par \( f \) . Une matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est dite semi-simple si l’endomorphisme \( f \) de \( {\mathbb{K}}^{n} \) dont \( M \) est la matrice dans la base canonique de \( {\mathbb{K}}^{n} \) est semi-simple.

> Problem 22 (SEMI-SIMPLE ENDOMORPHISMS). Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s. We say that \( f \in \mathcal{L}\left( E\right) \) is semi-simple if for every \( f \) -invariant s.v.s \( F \) of \( E \), there exists a \( f \) -invariant supplementary \( S \) of \( F \). A matrix \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is said to be semi-simple if the endomorphism \( f \) of \( {\mathbb{K}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{K}}^{n} \) is \( M \) is semi-simple.

1 / Soit \( f \in \mathcal{L}\left( E\right) \) . On note \( {\Pi }_{f} \) son polynôme minimal. Soit \( {\Pi }_{f} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) la décomposition de \( {\Pi }_{f} \) en facteurs irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> 1 / Let \( f \in \mathcal{L}\left( E\right) \) . Let \( {\Pi }_{f} \) denote its minimal polynomial. Let \( {\Pi }_{f} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) be the decomposition of \( {\Pi }_{f} \) into irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \) .

a) Soit \( F \) un s.e.v stable par \( f \) . Montrer que

> a) Let \( F \) be a s.v.s invariant under \( f \) . Show that

\[
F = {\bigoplus }_{i = 1}^{r}\left\lbrack  {\operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right)  \cap  F}\right\rbrack
\]

b) Si \( {\Pi }_{f} \) est irréductible, montrer que \( f \) est semi-simple.

> b) If \( {\Pi }_{f} \) is irreducible, show that \( f \) is semi-simple.

c) Dans le cas général, montrer que \( f \) est semi-simple si et seulement si \( {\Pi }_{f} = {M}_{1}{M}_{2}\cdots {M}_{r} \) est produit de polynômes irréductibles unitaires distincts deux à deux.

> c) In the general case, show that \( f \) is semi-simple if and only if \( {\Pi }_{f} = {M}_{1}{M}_{2}\cdots {M}_{r} \) is a product of pairwise distinct monic irreducible polynomials.

d) Que dire si K est algébriquement clos ?

> d) What can be said if K is algebraically closed?

2/ Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . a) Montrer que \( M \) est semi-simple (dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ) si et seulement si \( M \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> 2/ Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . a) Show that \( M \) is semi-simple (in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ) if and only if \( M \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

b) On suppose \( M \) semi-simple. Montrer que \( M \) est semblable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) à une matrice de la forme \( \left( \begin{matrix} D & 0 \\ 0 & B \end{matrix}\right) \) , avec \( D \) diagonale et \( B \) constituée de blocs de la forme \( \left( \begin{matrix} \alpha & - \beta \\ \beta & \alpha \end{matrix}\right) \) centrés sur sa diagonale principale.

> b) Assume \( M \) is semi-simple. Show that \( M \) is similar in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) to a matrix of the form \( \left( \begin{matrix} D & 0 \\ 0 & B \end{matrix}\right) \) , with \( D \) diagonal and \( B \) consisting of blocks of the form \( \left( \begin{matrix} \alpha & - \beta \\ \beta & \alpha \end{matrix}\right) \) centered on its main diagonal.

Solution. 1/ a) Pour tout \( i \) , on note \( {F}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \) . On sait que \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \) . Pour tout \( i \in \{ 1,\ldots , r\} \) , on note \( {p}_{i} \) la projection sur \( {F}_{i} \) parallèlement à \( { \oplus }_{j \neq i}{F}_{j} \) . On a vu à la proposition 1 page 204 que pour tout \( i,{p}_{i} \) est un polynôme en \( f \) . Comme \( F \) est stable par \( f, F \) est donc stable par \( {p}_{i} \) , ce qui s’écrit \( {p}_{i}\left( F\right) \subset F \) . On a aussi \( {p}_{i}\left( F\right) \subset {p}_{i}\left( E\right) = {F}_{i} \) . Finalement, on a \( {p}_{i}\left( F\right) \subset {F}_{i} \cap F \) , et comme \( {\mathrm{{Id}}}_{E} = {p}_{1} + \cdots + {p}_{r} \) ,

> Solution. 1/ a) For any \( i \), let \( {F}_{i} = \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \). We know that \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \). For any \( i \in \{ 1,\ldots , r\} \), let \( {p}_{i} \) be the projection onto \( {F}_{i} \) parallel to \( { \oplus }_{j \neq i}{F}_{j} \). We saw in proposition 1 on page 204 that for any \( i,{p}_{i} \) is a polynomial in \( f \). Since \( F \) is stable by \( f, F \), it is therefore stable by \( {p}_{i} \), which is written as \( {p}_{i}\left( F\right) \subset F \). We also have \( {p}_{i}\left( F\right) \subset {p}_{i}\left( E\right) = {F}_{i} \). Finally, we have \( {p}_{i}\left( F\right) \subset {F}_{i} \cap F \), and since \( {\mathrm{{Id}}}_{E} = {p}_{1} + \cdots + {p}_{r} \),

\[
F \subset  {p}_{1}\left( F\right)  + \cdots  + {p}_{r}\left( F\right)  = {p}_{1}\left( F\right)  \oplus  \cdots  \oplus  {p}_{r}\left( F\right)  \subset  \left( {{F}_{1} \cap  F}\right)  \oplus  \cdots  \oplus  \left( {{F}_{r} \cap  F}\right) .
\]

L’inclusion réciproque est facile puisque pour tout \( i,{F}_{i} \cap F \subset F \) donc \( \left( {{F}_{1} \cap F}\right) \oplus \cdots \oplus \left( {{F}_{r} \cap F}\right) \subset F \) . b) Soit \( F \) un s.e.v stable par \( f \) . Il s’agit de montrer l’existence d’un supplémentaire \( S \) de \( F \) dans \( E \) stable par \( f \) .

> The reverse inclusion is easy since for any \( i,{F}_{i} \cap F \subset F \) therefore \( \left( {{F}_{1} \cap F}\right) \oplus \cdots \oplus \left( {{F}_{r} \cap F}\right) \subset F \). b) Let \( F \) be a subspace stable by \( f \). We must show the existence of a supplementary subspace \( S \) of \( F \) in \( E \) that is stable by \( f \).

Si \( F = E \) , c’est terminé avec \( S = \{ 0\} \) .

> If \( F = E \), we are done with \( S = \{ 0\} \).

Sinon, soit \( {x}_{1} \in E \smallsetminus F \) . On considère \( {E}_{{x}_{1}} = \left\{ {P\left( f\right) \left( {x}_{1}\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack }\right\} \) . Le s.e.v \( {E}_{{x}_{1}} \) est stable par \( f \) . Nous allons montrer que \( {E}_{{x}_{1}} \cap F = \{ 0\} \) .

> Otherwise, let \( {x}_{1} \in E \smallsetminus F \). Consider \( {E}_{{x}_{1}} = \left\{ {P\left( f\right) \left( {x}_{1}\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack }\right\} \). The subspace \( {E}_{{x}_{1}} \) is stable by \( f \). We will show that \( {E}_{{x}_{1}} \cap F = \{ 0\} \).

Soit \( {I}_{{x}_{1}} = \left\{ {P \in \mathbb{K}\left\lbrack X\right\rbrack \left| {\;P\left( f\right) \left( {x}_{1}\right) = 0}\right. }\right\} \) . C’est un idéal de \( \mathbb{K}\left\lbrack X\right\rbrack \) , non réduit à \( \{ 0\} \) car \( {\Pi }_{f} \in {I}_{{x}_{1}} \) , donc il existe un polynôme unitaire \( {\Pi }_{{x}_{1}} \) tel que \( {I}_{{x}_{1}} = \left( {\Pi }_{{x}_{1}}\right) = {\Pi }_{{x}_{1}}\mathbb{K}\left\lbrack X\right\rbrack \) . Comme

> Let \( {I}_{{x}_{1}} = \left\{ {P \in \mathbb{K}\left\lbrack X\right\rbrack \left| {\;P\left( f\right) \left( {x}_{1}\right) = 0}\right. }\right\} \). This is an ideal of \( \mathbb{K}\left\lbrack X\right\rbrack \), not reduced to \( \{ 0\} \) because \( {\Pi }_{f} \in {I}_{{x}_{1}} \), so there exists a monic polynomial \( {\Pi }_{{x}_{1}} \) such that \( {I}_{{x}_{1}} = \left( {\Pi }_{{x}_{1}}\right) = {\Pi }_{{x}_{1}}\mathbb{K}\left\lbrack X\right\rbrack \). Since

\( {\Pi }_{f} \in {I}_{{x}_{1}} \) , le polynôme \( {\Pi }_{{x}_{1}} \) divise \( {\Pi }_{f} \) , et \( {\Pi }_{f} \) étant irréductible, \( {\Pi }_{{x}_{1}} = {\Pi }_{f} \) . Le polynôme \( {\Pi }_{{x}_{1}} \) est donc irréductible.

> \( {\Pi }_{f} \in {I}_{{x}_{1}} \), the polynomial \( {\Pi }_{{x}_{1}} \) divides \( {\Pi }_{f} \), and since \( {\Pi }_{f} \) is irreducible, \( {\Pi }_{{x}_{1}} = {\Pi }_{f} \). The polynomial \( {\Pi }_{{x}_{1}} \) is therefore irreducible.

Soit \( y \in {E}_{{x}_{1}} \cap F \) . Il existe un polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( y = P\left( f\right) \left( {x}_{1}\right) \) . Si \( y \neq 0 \) , alors \( P \notin {I}_{{x}_{1}} = \left( {\Pi }_{{x}_{1}}\right) \) , donc \( {\Pi }_{{x}_{1}} \) ne divise pas \( P \) , et \( {\Pi }_{{x}_{1}} \) étant irréductible, \( {\Pi }_{{x}_{1}} \) et \( P \) sont premiers entre eux. D’après le théorème de Bezout, il existe donc \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( {UP} + V{\Pi }_{{x}_{1}} = 1 \) , donc

> Let \( y \in {E}_{{x}_{1}} \cap F \) . There exists a polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( y = P\left( f\right) \left( {x}_{1}\right) \) . If \( y \neq 0 \) , then \( P \notin {I}_{{x}_{1}} = \left( {\Pi }_{{x}_{1}}\right) \) , so \( {\Pi }_{{x}_{1}} \) does not divide \( P \) , and since \( {\Pi }_{{x}_{1}} \) is irreducible, \( {\Pi }_{{x}_{1}} \) and \( P \) are coprime. According to Bezout's theorem, there exist \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {UP} + V{\Pi }_{{x}_{1}} = 1 \) , therefore

\[
{x}_{1} = U\left( f\right)  \circ  P\left( f\right) \left( {x}_{1}\right)  + V\left( f\right)  \circ  {\Pi }_{{x}_{1}}\left( f\right) \left( {x}_{1}\right)  = U\left( f\right) \left( y\right) .
\]

Or \( y \in F \) et \( F \) est stable par \( f \) , donc \( {x}_{1} = U\left( f\right) \left( y\right) \in F \) . Ceci est absurde par construction de \( {x}_{1} \) . On a donc \( y = 0 \) et \( {E}_{{x}_{1}} \cap F = \{ 0\} \) .

> However, \( y \in F \) and \( F \) is stable under \( f \) , so \( {x}_{1} = U\left( f\right) \left( y\right) \in F \) . This is absurd by the construction of \( {x}_{1} \) . We therefore have \( y = 0 \) and \( {E}_{{x}_{1}} \cap F = \{ 0\} \) .

On vient de montrer que \( {E}_{{x}_{1}} \) et \( F \) sont en somme directe et \( {E}_{{x}_{1}} \) stable par \( f \) . Si \( F \oplus {E}_{{x}_{1}} = E \) , on choisit \( S = {E}_{{x}_{1}} \) et c’est terminé. Sinon, on choisit \( {x}_{2} \in E \smallsetminus \left( {F \oplus {E}_{{x}_{1}}}\right) \) et on recommence en remplaçant cette fois ci \( F \) par \( F \oplus {E}_{{x}_{1}} \) . Itérant ainsi le procédé, on voit qu’au bout d’un nombre fini d’itérations ( \( E \) est de dimension fini), on aura trouvé des vecteurs \( {x}_{1},\ldots ,{x}_{k} \) tels que \( E = F \oplus {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) et pour tout \( i,{E}_{{x}_{i}} \) stable par \( f \) . Le s.e.v \( S = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) est donc stable par \( f \) et vérifie \( F \oplus S = E \) .

> We have just shown that \( {E}_{{x}_{1}} \) and \( F \) are in direct sum and \( {E}_{{x}_{1}} \) is stable under \( f \) . If \( F \oplus {E}_{{x}_{1}} = E \) , we choose \( S = {E}_{{x}_{1}} \) and we are done. Otherwise, we choose \( {x}_{2} \in E \smallsetminus \left( {F \oplus {E}_{{x}_{1}}}\right) \) and start again, this time replacing \( F \) with \( F \oplus {E}_{{x}_{1}} \) . By iterating this process, we see that after a finite number of iterations ( \( E \) is of finite dimension), we will have found vectors \( {x}_{1},\ldots ,{x}_{k} \) such that \( E = F \oplus {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) and for all \( i,{E}_{{x}_{i}} \) stable under \( f \) . The subspace \( S = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) is therefore stable under \( f \) and satisfies \( F \oplus S = E \) .

c) Condition nécessaire. Supposons \( f \) semi-simple. Soit \( {\Pi }_{f} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) la décomposition de \( {\Pi }_{f} \) en facteurs irréductibles unitaires de \( \mathbb{K}\left\lbrack X\right\rbrack \) . Il s’agit de montrer que pour tout \( i,{\alpha }_{i} = 1 \) . Supposons au contraire qu’il existe \( i \) tel que \( {\alpha }_{i} \geq 2 \) . Notons \( M = {M}_{i} \) , de sorte qu’il existe \( N \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {\Pi }_{f} = {M}^{2}N \) .

> c) Necessary condition. Suppose \( f \) is semi-simple. Let \( {\Pi }_{f} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) be the decomposition of \( {\Pi }_{f} \) into monic irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \) . We must show that for all \( i,{\alpha }_{i} = 1 \) . Suppose on the contrary that there exists \( i \) such that \( {\alpha }_{i} \geq 2 \) . Let \( M = {M}_{i} \) , so that there exists \( N \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {\Pi }_{f} = {M}^{2}N \) .

Soit \( F = \operatorname{Ker}M\left( f\right) \) . Le s.e.v \( F \) est stable par \( f \) semi-simple donc il existe un supplémentaire \( S \) de \( F \) stable par \( f \) .

> Let \( F = \operatorname{Ker}M\left( f\right) \) . The subspace \( F \) is stable under the semi-simple \( f \) , so there exists a supplementary subspace \( S \) of \( F \) stable under \( f \) .

Montrons que \( {MN}\left( f\right) \) s’annule sur \( S \) . Si \( x \in S \) , alors \( {MN}\left( f\right) \left( x\right) \in F \) car \( M\left( f\right) \left\lbrack {{MN}\left( f\right) \left( x\right) }\right\rbrack = \; {\Pi }_{f}\left( f\right) \left( x\right) = 0 \) , et \( {MN}\left( f\right) \left( x\right) \in S \) car \( S \) est stable par \( f \) . Donc \( {MN}\left( f\right) \left( x\right) \in F \cap S = \{ 0\} \) , et donc \( {MN}\left( f\right) \left( x\right) = 0 \) .

> Let us show that \( {MN}\left( f\right) \) vanishes on \( S \) . If \( x \in S \) , then \( {MN}\left( f\right) \left( x\right) \in F \) because \( M\left( f\right) \left\lbrack {{MN}\left( f\right) \left( x\right) }\right\rbrack = \; {\Pi }_{f}\left( f\right) \left( x\right) = 0 \) , and \( {MN}\left( f\right) \left( x\right) \in S \) because \( S \) is stable under \( f \) . Thus \( {MN}\left( f\right) \left( x\right) \in F \cap S = \{ 0\} \) , and therefore \( {MN}\left( f\right) \left( x\right) = 0 \) .

L’endomorphisme \( {MN}\left( f\right) \) s’annule donc sur \( S \) . Il s’annule aussi sur \( F \) car si \( y \in F = \) Ker \( M\left( f\right) \) , alors \( {MN}\left( f\right) \left( y\right) = N\left\lbrack {M\left( f\right) \left( y\right) }\right\rbrack = 0 \) . Comme \( F \oplus S = E,{MN}\left( f\right) \) s’annule sur \( E \) tout entier, i. e. \( {MN}\left( f\right) = 0 \) . Ceci contredit la minimalité du degré du polynôme minimal \( {\Pi }_{f} = {M}^{2}N \) . D'où la condition nécessaire.

> The endomorphism \( {MN}\left( f\right) \) therefore vanishes on \( S \) . It also vanishes on \( F \) because if \( y \in F = \) Ker \( M\left( f\right) \) , then \( {MN}\left( f\right) \left( y\right) = N\left\lbrack {M\left( f\right) \left( y\right) }\right\rbrack = 0 \) . Since \( F \oplus S = E,{MN}\left( f\right) \) vanishes on the whole of \( E \) , i. e. \( {MN}\left( f\right) = 0 \) . This contradicts the minimality of the degree of the minimal polynomial \( {\Pi }_{f} = {M}^{2}N \) . Hence the necessary condition.

Condition suffisante. Supposons \( {\Pi }_{f} = {M}_{1}\cdots {M}_{r} \) avec les \( {M}_{i} \) irréductibles unitaires et distincts deux à deux. Soit \( F \) un s.e.v de \( E \) stable par \( f \) . Pour tout \( i \) , notons \( {F}_{i} = \operatorname{Ker}{M}_{i}\left( f\right) \) . On a \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \) , et on a vu à la question a) que \( F = { \oplus }_{i = 1}^{r}\left\lbrack {F \cap {F}_{i}}\right\rbrack \) .

> Sufficient condition. Suppose \( {\Pi }_{f} = {M}_{1}\cdots {M}_{r} \) with the \( {M}_{i} \) being irreducible, monic, and pairwise distinct. Let \( F \) be a subspace of \( E \) stable under \( f \) . For any \( i \) , let us denote \( {F}_{i} = \operatorname{Ker}{M}_{i}\left( f\right) \) . We have \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \) , and we saw in question a) that \( F = { \oplus }_{i = 1}^{r}\left\lbrack {F \cap {F}_{i}}\right\rbrack \) .

Pour tout \( i,{F}_{i} \) est stable par \( f \) . Notons \( {f}_{i} \in \mathcal{L}\left( {F}_{i}\right) \) la restriction de \( f \) à \( {F}_{i} \) . On a \( {M}_{i}\left( {f}_{i}\right) = 0 \) et \( {M}_{i} \) est irréductible, ce qui prouve que le polynôme minimal de \( {f}_{i} \) est \( {M}_{i} \) . D’après b), \( {f}_{i} \) est donc semi-simple. Or \( F \cap {F}_{i} \) est stable par \( {f}_{i} \) , donc il existe un s.e.v \( {S}_{i} \) stable par \( {f}_{i} \) (donc par \( f) \) tel que \( \left( {{F}_{i} \cap F}\right) \oplus {S}_{i} = {F}_{i} \) . Si maintenant on pose \( S = {S}_{1} \oplus \cdots \oplus {S}_{r} \) , on a

> For all \( i,{F}_{i} \) is stable by \( f \) . Let \( {f}_{i} \in \mathcal{L}\left( {F}_{i}\right) \) denote the restriction of \( f \) to \( {F}_{i} \) . We have \( {M}_{i}\left( {f}_{i}\right) = 0 \) and \( {M}_{i} \) is irreducible, which proves that the minimal polynomial of \( {f}_{i} \) is \( {M}_{i} \) . According to b), \( {f}_{i} \) is therefore semi-simple. However, \( F \cap {F}_{i} \) is stable by \( {f}_{i} \) , so there exists a subspace \( {S}_{i} \) stable by \( {f}_{i} \) (and thus by \( f) \) ) such that \( \left( {{F}_{i} \cap F}\right) \oplus {S}_{i} = {F}_{i} \) . If we now set \( S = {S}_{1} \oplus \cdots \oplus {S}_{r} \) , we have

\[
E = {F}_{1} \oplus  \cdots  \oplus  {F}_{r} = {\bigoplus }_{i = 1}^{r}\left\lbrack  {\left( {{F}_{i} \cap  F}\right)  \oplus  {S}_{i}}\right\rbrack   = \left\lbrack  {{\bigoplus }_{i = 1}^{r}\left( {{F}_{i} \cap  F}\right) }\right\rbrack   \oplus  \left\lbrack  {{\bigoplus }_{i = 1}^{r}{S}_{i}}\right\rbrack   = F \oplus  S,
\]

et \( S \) est stable par \( f \) . L’endomorphisme \( f \) est donc semi-simple.

> and \( S \) is stable by \( f \) . The endomorphism \( f \) is therefore semi-simple.

d) Si \( \mathbb{K} \) est algébriquement clos, les polynômes irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) sont les polynômes de degré 1. D’après c), \( f \) est donc semi-simple si et seulement si \( {\Pi }_{f} \) n’a que des racines simples dans \( \mathbb{K} \) , i. e. si et seulement si \( f \) est diagonalisable.

> d) If \( \mathbb{K} \) is algebraically closed, the irreducible polynomials of \( \mathbb{K}\left\lbrack X\right\rbrack \) are the polynomials of degree 1. According to c), \( f \) is therefore semi-simple if and only if \( {\Pi }_{f} \) has only simple roots in \( \mathbb{K} \) , i.e., if and only if \( f \) is diagonalizable.

2/a) Condition nécessaire. Supposons \( M \) semi-simple. D’après 1/c), \( {\Pi }_{M} \) peut s’écrire \( {\Pi }_{M} = \; {M}_{1}\cdots {M}_{r} \) où les \( {M}_{i} \) sont irréductibles dans \( \mathbb{R}\left\lbrack X\right\rbrack \) , unitaires et distincts deux à deux. Montrons que \( {\Pi }_{M} \) n’a que des racines simples dans \( \mathbb{C} \) . Soit \( \alpha \in \mathbb{C} \) une racine de \( {\Pi }_{M} \) . Il existe \( i \) tel que \( {M}_{i}\left( \alpha \right) = 0 \) , par exemple \( {M}_{1}\left( \alpha \right) = 0 \) . Comme \( {M}_{1} \) est irréductible dans \( \mathbb{R}\left\lbrack X\right\rbrack ,\alpha \) est racine simple de \( {M}_{1} \) (en effet, \( {M}_{1} \) étant irréductible dans \( \mathbb{R}\left\lbrack X\right\rbrack ,{M}_{1} \) et \( {M}_{1}^{\prime } \) sont premiers entre eux dans \( \mathbb{R}\left\lbrack X\right\rbrack \) donc il existe \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) tels que \( U{M}_{1} + V{M}_{1}^{\prime } = 1 \) . Cette relation appliquée à \( \alpha \) montre que \( {M}_{1}^{\prime }\left( \alpha \right) \neq 0) \) . Par ailleurs, si \( i \neq 1,{M}_{i}\left( \alpha \right) \neq 0 \) (en effet, \( {M}_{1} \) et \( {M}_{i} \) sont irréductibles dans \( \mathbb{R}\left\lbrack X\right\rbrack \) , unitaires et distincts, donc premiers entre eux dans \( \mathbb{R}\left\lbrack X\right\rbrack \) , donc il existe \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) tels que \( U{M}_{1} + V{M}_{i} = 1 \) . Cette relation appliquée à \( \alpha \) montre que \( {M}_{i}\left( \alpha \right) \neq 0) \) . En définitive, on a montré que \( \alpha \) est racine simple de \( {\Pi }_{M} \) .

> 2/a) Necessary condition. Suppose \( M \) is semi-simple. According to 1/c), \( {\Pi }_{M} \) can be written as \( {\Pi }_{M} = \; {M}_{1}\cdots {M}_{r} \) where the \( {M}_{i} \) are irreducible in \( \mathbb{R}\left\lbrack X\right\rbrack \), monic, and pairwise distinct. Let us show that \( {\Pi }_{M} \) has only simple roots in \( \mathbb{C} \). Let \( \alpha \in \mathbb{C} \) be a root of \( {\Pi }_{M} \). There exists \( i \) such that \( {M}_{i}\left( \alpha \right) = 0 \), for example \( {M}_{1}\left( \alpha \right) = 0 \). Since \( {M}_{1} \) is irreducible in \( \mathbb{R}\left\lbrack X\right\rbrack ,\alpha \), it is a simple root of \( {M}_{1} \) (indeed, since \( {M}_{1} \) is irreducible in \( \mathbb{R}\left\lbrack X\right\rbrack ,{M}_{1} \) and \( {M}_{1}^{\prime } \) are coprime in \( \mathbb{R}\left\lbrack X\right\rbrack \), there exist \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( U{M}_{1} + V{M}_{1}^{\prime } = 1 \). This relation applied to \( \alpha \) shows that \( {M}_{1}^{\prime }\left( \alpha \right) \neq 0) \). Furthermore, if \( i \neq 1,{M}_{i}\left( \alpha \right) \neq 0 \) (indeed, \( {M}_{1} \) and \( {M}_{i} \) are irreducible in \( \mathbb{R}\left\lbrack X\right\rbrack \), monic, and distinct, thus coprime in \( \mathbb{R}\left\lbrack X\right\rbrack \), so there exist \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( U{M}_{1} + V{M}_{i} = 1 \). This relation applied to \( \alpha \) shows that \( {M}_{i}\left( \alpha \right) \neq 0) \). Ultimately, we have shown that \( \alpha \) is a simple root of \( {\Pi }_{M} \).

Condition suffisante. Soit \( {\Pi }_{M} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) la décomposition de \( {\Pi }_{M} \) en facteurs irréductibles unitaires de \( \mathbb{R}\left\lbrack X\right\rbrack \) . D’après \( 1/\mathrm{c}) \) , il suffit de montrer que pour tout \( i,{\alpha }_{i} = 1 \) . Comme \( M \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,{\Pi }_{M} \) n’a que des racines simples dans \( \mathbb{C} \) (le polynôme minimal de \( M \) dans \( \mathbb{C}\left\lbrack X\right\rbrack \) est le même que dans \( \mathbb{R}\left\lbrack X\right\rbrack \) car si \( {M}^{p} + {a}_{1}{M}^{p - 1} + \cdots + {a}_{p}{I}_{n} = 0 \) avec les \( {a}_{i} \in \mathbb{C} \) , alors \( {M}^{p} + \Re \left( {a}_{1}\right) {M}^{p - 1} + \cdots + \Re \left( {a}_{p}\right) {I}_{n} = 0) \) . Ceci suffit à montrer que pour tout \( i,{\alpha }_{i} = 1 \) .

> Sufficient condition. Let \( {\Pi }_{M} = {M}_{1}^{{\alpha }_{1}}\cdots {M}_{r}^{{\alpha }_{r}} \) be the decomposition of \( {\Pi }_{M} \) into monic irreducible factors in \( \mathbb{R}\left\lbrack X\right\rbrack \). According to \( 1/\mathrm{c}) \), it suffices to show that for all \( i,{\alpha }_{i} = 1 \). Since \( M \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,{\Pi }_{M} \), it has only simple roots in \( \mathbb{C} \) (the minimal polynomial of \( M \) in \( \mathbb{C}\left\lbrack X\right\rbrack \) is the same as in \( \mathbb{R}\left\lbrack X\right\rbrack \) because if \( {M}^{p} + {a}_{1}{M}^{p - 1} + \cdots + {a}_{p}{I}_{n} = 0 \) with the \( {a}_{i} \in \mathbb{C} \), then \( {M}^{p} + \Re \left( {a}_{1}\right) {M}^{p - 1} + \cdots + \Re \left( {a}_{p}\right) {I}_{n} = 0) \)). This is sufficient to show that for all \( i,{\alpha }_{i} = 1 \).

b) On regarde \( M \) comme un endomorphisme de \( {\mathbb{R}}^{n} \) . Démontrons le résultat par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Si \( {\Pi }_{M} \) est scindé sur \( \mathbb{R} \) , c’est immédiat car alors \( {\Pi }_{M} \) est à racines simples d’après \( 1/\mathrm{c}) \) et donc \( M \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> b) We view \( M \) as an endomorphism of \( {\mathbb{R}}^{n} \). Let us prove the result by induction on \( n \in {\mathbb{N}}^{ * } \). For \( n = 1 \), it is obvious. Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \). If \( {\Pi }_{M} \) splits over \( \mathbb{R} \), it is immediate because then \( {\Pi }_{M} \) has simple roots according to \( 1/\mathrm{c}) \) and thus \( M \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \).

Sinon \( {\Pi }_{M} \) a au moins un facteur irréductible dans \( \mathbb{R}\left\lbrack X\right\rbrack \) de degré 2 de la forme \( \left\lbrack {{\left( X - \alpha \right) }^{2} + {\beta }^{2}}\right\rbrack \) , \( \alpha \in \mathbb{R} \) et \( \beta > 0 \) . On peut écrire \( {\Pi }_{M} = \left\lbrack {{\left( X - \alpha \right) }^{2} + {\beta }^{2}}\right\rbrack Q \) avec \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) . Posons \( E = \; \operatorname{Ker}\left\lbrack {{\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n}}\right\rbrack \) . On a \( E \neq \{ 0\} \) , sinon \( {\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n} \) est inversible et donc \( Q\left( M\right) = 0 \) , ce qui contredit la minimalité du degré de \( {\Pi }_{M} \) .

> Otherwise, \( {\Pi }_{M} \) has at least one irreducible factor in \( \mathbb{R}\left\lbrack X\right\rbrack \) of degree 2 of the form \( \left\lbrack {{\left( X - \alpha \right) }^{2} + {\beta }^{2}}\right\rbrack \), \( \alpha \in \mathbb{R} \) and \( \beta > 0 \). We can write \( {\Pi }_{M} = \left\lbrack {{\left( X - \alpha \right) }^{2} + {\beta }^{2}}\right\rbrack Q \) with \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \). Let \( E = \; \operatorname{Ker}\left\lbrack {{\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n}}\right\rbrack \). We have \( E \neq \{ 0\} \), otherwise \( {\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n} \) is invertible and thus \( Q\left( M\right) = 0 \), which contradicts the minimality of the degree of \( {\Pi }_{M} \).

Soit \( {e}_{1} \in E,{e}_{1} \neq 0 \) . Les vecteurs \( {e}_{1} \) et \( M{e}_{1} \) sont linéairement indépendants. En effet, s’il existe \( \lambda \in \mathbb{R} \) tel que \( M{e}_{1} = \lambda {e}_{1} \) , alors

> Let \( {e}_{1} \in E,{e}_{1} \neq 0 \) . The vectors \( {e}_{1} \) and \( M{e}_{1} \) are linearly independent. Indeed, if there exists \( \lambda \in \mathbb{R} \) such that \( M{e}_{1} = \lambda {e}_{1} \) , then

\[
0 = {\left( M - \alpha {I}_{n}\right) }^{2}\left( {e}_{1}\right)  + {\beta }^{2}{e}_{1} = {\left( \lambda  - \alpha \right) }^{2}{e}_{1} + {\beta }^{2}{e}_{1} = \left\lbrack  {{\left( \lambda  - \alpha \right) }^{2} + {\beta }^{2}}\right\rbrack  {e}_{1} \neq  0,
\]

ce qui est impossible.

> which is impossible.

Si on pose \( {e}_{2} = \frac{1}{\beta }\left\lbrack {M{e}_{1} - \alpha {e}_{1}}\right\rbrack \) , la famille \( \left( {{e}_{1},{e}_{2}}\right) \) est donc libre. Remarquons que \( M{e}_{1} = \; \alpha {e}_{1} + \beta {e}_{2} \) et comme \( {e}_{1} \in \operatorname{Ker}\left\lbrack {{\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n}}\right\rbrack \) , on a

> If we set \( {e}_{2} = \frac{1}{\beta }\left\lbrack {M{e}_{1} - \alpha {e}_{1}}\right\rbrack \) , the family \( \left( {{e}_{1},{e}_{2}}\right) \) is therefore linearly independent. Note that \( M{e}_{1} = \; \alpha {e}_{1} + \beta {e}_{2} \) and since \( {e}_{1} \in \operatorname{Ker}\left\lbrack {{\left( M - \alpha {I}_{n}\right) }^{2} + {\beta }^{2}{I}_{n}}\right\rbrack \) , we have

\[
M{e}_{2} = \left( {M - \alpha {I}_{n}}\right) \left( {e}_{2}\right)  + \alpha {e}_{2} = \frac{1}{\beta }{\left( M - \alpha {I}_{n}\right) }^{2}\left( {e}_{1}\right)  + \alpha {e}_{2} =  - \beta {e}_{1} + \alpha {e}_{2}.
\]

En résumé, \( F = \operatorname{Vect}\left( {{e}_{1},{e}_{2}}\right) \) est stable par \( M \) et

> In summary, \( F = \operatorname{Vect}\left( {{e}_{1},{e}_{2}}\right) \) is stable under \( M \) and

\[
M{e}_{1} = \alpha {e}_{1} + \beta {e}_{2},\;M{e}_{2} =  - \beta {e}_{1} + \alpha {e}_{2}.
\]

(*)

> La matrice \( M \) étant semi-simple, on peut trouver un s.e.v \( G \) de \( {\mathbb{R}}^{n} \) stable par \( M \) tel que \( F \oplus G = \; {\mathbb{R}}^{n} \) . Le restriction \( {M}_{\mid G} \) de \( M \) à \( G \) est semi-simple (son polynôme minimal vérifie \( 1/\mathrm{c} \) ) car il divise \( {\Pi }_{M} \) ). Or \( \dim G = n - \dim F = n - 2 \) , donc d’après l’hypothèse de récurrence il existe une base \( \mathcal{B} = \left( {{f}_{1},\ldots ,{f}_{n - 2}}\right) \) de \( G \) dans laquelle la matrice de \( {M}_{\mid G} \) ait la forme \( \left( \begin{matrix} D & 0 \\ 0 & B \end{matrix}\right) \) avec \( D \) diagonale et \( B \) constituée de blocs de la forme \( \left( \begin{matrix} a & - b \\ b & a \end{matrix}\right) \) centrés sur sa diagonale principale. Dans la base \( {\mathcal{B}}^{\prime } = \left( {\mathcal{B},{e}_{1},{e}_{2}}\right) \) , la matrice de \( M \) a donc la forme \( \left( \begin{array}{ll} D & B \\ \left( 0\right) & C \end{array}\right) \) , où \( C = \left( \begin{matrix} \alpha & - \beta \\ \beta & \alpha \end{matrix}\right) \) d’après (*). D’où le résultat.

Since the matrix \( M \) is semi-simple, we can find a subspace \( G \) of \( {\mathbb{R}}^{n} \) stable under \( M \) such that \( F \oplus G = \; {\mathbb{R}}^{n} \) . The restriction \( {M}_{\mid G} \) of \( M \) to \( G \) is semi-simple (its minimal polynomial satisfies \( 1/\mathrm{c} \) ) because it divides \( {\Pi }_{M} \) ). However, \( \dim G = n - \dim F = n - 2 \) , so by the induction hypothesis there exists a basis \( \mathcal{B} = \left( {{f}_{1},\ldots ,{f}_{n - 2}}\right) \) of \( G \) in which the matrix of \( {M}_{\mid G} \) has the form \( \left( \begin{matrix} D & 0 \\ 0 & B \end{matrix}\right) \) with \( D \) diagonal and \( B \) consisting of blocks of the form \( \left( \begin{matrix} a & - b \\ b & a \end{matrix}\right) \) centered on its main diagonal. In the basis \( {\mathcal{B}}^{\prime } = \left( {\mathcal{B},{e}_{1},{e}_{2}}\right) \) , the matrix of \( M \) therefore has the form \( \left( \begin{array}{ll} D & B \\ \left( 0\right) & C \end{array}\right) \) , where \( C = \left( \begin{matrix} \alpha & - \beta \\ \beta & \alpha \end{matrix}\right) \) according to (*). Hence the result.

> Remarque. - On peut montrer facilement que la réciproque de 2/b) est vraie.

Remark. - It can be easily shown that the converse of 2/b) is true.

> - On aurait pu montrer 2/b) en diagonalisant \( M \) dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) et en travaillant sur les parties réelles et imaginaires de ses vecteurs propres.

- We could have shown 2/b) by diagonalizing \( M \) in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) and working on the real and imaginary parts of its eigenvectors.

> - La semi-simplicité peut être vue comme une généralisation de la diagonalisabilité, dans le cas des corps non algébriquement clos. Dans cette idée, on peut montrer que si K est un corps commutatif quelconque, toute matrice \( M \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) peut s’écrire \( M = S + N \) avec \( {SN} = {NS}, S \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) semi-simple et \( N \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) nilpotente (résultat à rapprocher de la décomposition de Dunford, voir la partie 4.2 page 203).

- Semi-simplicity can be seen as a generalization of diagonalizability in the case of non-algebraically closed fields. With this in mind, one can show that if K is any commutative field, any matrix \( M \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) can be written as \( M = S + N \) with \( {SN} = {NS}, S \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) semi-simple and \( N \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) nilpotent (a result to be compared with the Dunford decomposition, see part 4.2 page 203).

> Chapitre 5

Chapter 5
