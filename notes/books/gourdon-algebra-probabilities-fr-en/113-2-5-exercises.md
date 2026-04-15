#### 2.5. Exercises

*Français : 2.5. Exercices*

\( \rightarrow \) EXERCICE 1 (RACINE CARRÉE D’UNE MATRICE HERMITIENNE POSITIVE). Soit \( H \in \; {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice hermitienne positive. Montrer qu’il existe une unique matrice \( R \) hermitienne positive telle que \( H = {R}^{2} \) .

> \( \rightarrow \) EXERCISE 1 (SQUARE ROOT OF A POSITIVE HERMITIAN MATRIX). Let \( H \in \; {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a positive Hermitian matrix. Show that there exists a unique positive Hermitian matrix \( R \) such that \( H = {R}^{2} \).

Solution. Existence. La matrice \( H \) étant hermitienne, il existe une matrice unitaire \( C \) telle que

> Solution. Existence. Since the matrix \( H \) is Hermitian, there exists a unitary matrix \( C \) such that

![bo_d7fjffs91nqc73erehlg_257_482_1697_600_146_0.jpg](images/gourdon_algebra_probabilities_fr_en_011_bod7fjffs91nqc73erehlg25748216976001460.jpg)

\( D \) étant diagonale réelle. Comme \( H \) est positive, tous les \( {\lambda }_{i} \) sont positifs donc pour tout \( i \) , il existe \( {\mu }_{i} \geq 0 \) tel que \( {\lambda }_{i} = {\mu }_{i}^{2} \) . En posant

> \( D \) being real diagonal. As \( H \) is positive, all \( {\lambda }_{i} \) are positive, so for every \( i \), there exists \( {\mu }_{i} \geq 0 \) such that \( {\lambda }_{i} = {\mu }_{i}^{2} \). By setting

\[
{D}^{\prime } = \left( \begin{matrix} {\mu }_{1} & \left( 0\right) \\  \ldots & \\  \left( 0\right) & {\mu }_{n} \end{matrix}\right) ,
\]

on a \( {D}^{\prime 2} = D \) de sorte que \( R = C{D}^{\prime }{C}^{-1} = C{D}^{\prime }{}^{\mathrm{t}}\bar{C} \) est hermitienne positive et vérifie

> we have \( {D}^{\prime 2} = D \) such that \( R = C{D}^{\prime }{C}^{-1} = C{D}^{\prime }{}^{\mathrm{t}}\bar{C} \) is a positive Hermitian matrix and satisfies

\[
{R}^{2} = C{D}^{\prime 2}{C}^{-1} = {CD}{C}^{-1} = H.
\]

Unicité. Soit \( R \) hermitienne positive telle que \( {R}^{2} = H \) . Soient \( h \) et \( r \) les endomorphismes de \( {\mathbb{C}}^{n} \) dont \( H \) et \( R \) sont les matrices dans la base canonique de \( {\mathbb{C}}^{n} \) . Comme \( H \) est hermitienne, \( h \) est autoadjoint. Ses valeurs propres \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) sont positives car \( H \) est positive. Notons \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{p}} \) les sous-espaces propres correspondants. Comme \( r \) commute avec \( {r}^{2} = h \) , chaque \( {E}_{{\lambda }_{i}} \) est stable par \( r \) (voir la proposition 7 page 175). On note \( {r}_{i} = {r}_{\mid {E}_{{\lambda }_{i}}} \) . On a \( {r}_{i}^{2} = {\lambda }_{i}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) , et \( {r}_{i} \) est autoadjoint positif ; toute valeur propre \( \mu \) de \( {r}_{i} \) vérifie \( {\mu }^{2} = {\lambda }_{i} \) , donc \( \mu = \sqrt{{\lambda }_{i}} \) est la seule valeur propre possible de \( {r}_{i} \) (car les valeurs propres de \( {r}_{i} \) , qui sont des valeurs propres de \( r \) donc de \( R \) , sont positives). Comme \( {r}_{i} \) est de plus diagonalisable (car autoadjoint), on en déduit \( {r}_{i} = \sqrt{{\lambda }_{i}}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) .

> Uniqueness. Let \( R \) be a positive Hermitian matrix such that \( {R}^{2} = H \) . Let \( h \) and \( r \) be the endomorphisms of \( {\mathbb{C}}^{n} \) whose matrices in the canonical basis of \( {\mathbb{C}}^{n} \) are \( H \) and \( R \) . Since \( H \) is Hermitian, \( h \) is self-adjoint. Its eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) are positive because \( H \) is positive. Let \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{p}} \) denote the corresponding eigenspaces. Since \( r \) commutes with \( {r}^{2} = h \) , each \( {E}_{{\lambda }_{i}} \) is stable under \( r \) (see proposition 7 on page 175). Let \( {r}_{i} = {r}_{\mid {E}_{{\lambda }_{i}}} \) . We have \( {r}_{i}^{2} = {\lambda }_{i}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) , and \( {r}_{i} \) is a positive self-adjoint operator; any eigenvalue \( \mu \) of \( {r}_{i} \) satisfies \( {\mu }^{2} = {\lambda }_{i} \) , so \( \mu = \sqrt{{\lambda }_{i}} \) is the only possible eigenvalue of \( {r}_{i} \) (since the eigenvalues of \( {r}_{i} \) , which are eigenvalues of \( r \) and thus of \( R \) , are positive). As \( {r}_{i} \) is also diagonalizable (being self-adjoint), we deduce \( {r}_{i} = \sqrt{{\lambda }_{i}}{\operatorname{Id}}_{{E}_{{\lambda }_{i}}} \) .

Résumons. Si \( {r}^{2} = h \) , alors forcément pour tout \( i,{r}_{\mid {E}_{{\lambda }_{i}}} = \sqrt{{\lambda }_{i}}{\operatorname{Id}}_{\mid {E}_{{\lambda }_{i}}} \) , ce qui définit \( r \) de manière unique, d’où l’unicité de \( R \) .

> To summarize. If \( {r}^{2} = h \) , then necessarily for all \( i,{r}_{\mid {E}_{{\lambda }_{i}}} = \sqrt{{\lambda }_{i}}{\operatorname{Id}}_{\mid {E}_{{\lambda }_{i}}} \) , which uniquely defines \( r \) , hence the uniqueness of \( R \) .

EXERCICE 2. Soit \( E \) un espace hermitien et \( f \) et \( g \) deux endomorphismes autoadjoints de \( \mathcal{L}\left( E\right) \) tels que \( {fg} = {gf} \) . Montrer que \( f \) et \( g \) sont diagonalisables dans une base commune de vecteurs propres orthonormés.

> EXERCISE 2. Let \( E \) be a Hermitian space and \( f \) and \( g \) be two self-adjoint endomorphisms of \( \mathcal{L}\left( E\right) \) such that \( {fg} = {gf} \) . Show that \( f \) and \( g \) are diagonalizable in a common orthonormal basis of eigenvectors.

Solution. Les endomorphismes \( f \) et \( g \) étant autoadjoints, on sait déjà qu’ils se diagonalisent chacun dans une base orthonormée. Il nous reste à montrer que l'on peut prendre la même base pour les deux.

> Solution. Since the endomorphisms \( f \) and \( g \) are self-adjoint, we already know that each is diagonalizable in an orthonormal basis. It remains to show that the same basis can be used for both.

Notons \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) les valeurs propres (distinctes) de \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) les sous-espaces propres correspondants. Les \( {E}_{{\lambda }_{i}} \) sont deux à deux orthogonaux (pour s’en persuader, diagonaliser \( f \) dans une base orthonormée). Comme \( f \) et \( g \) commutent, les \( {E}_{{\lambda }_{i}} \) sont stables par \( g \) . La restriction de \( g \) à \( {E}_{{\lambda }_{i}} \) étant autoadjointe, il existe une base orthonormée \( {B}_{i} \) de \( {E}_{{\lambda }_{i}} \) diagonalisant \( {g}_{\mid {E}_{{\lambda }_{i}}} \) . Les \( {E}_{{\lambda }_{i}} \) étant deux à deux orthogonaux, on en déduit que \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) est une base orthonormée. Cette base diagonalise \( g \) par construction ainsi que \( f \) puisque chaque vecteur \( e \) de \( {B}_{i} \) vérifie \( f\left( e\right) = {\lambda }_{i}e. \)

> Let \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) be the (distinct) eigenvalues of \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) the corresponding eigenspaces. The \( {E}_{{\lambda }_{i}} \) are pairwise orthogonal (to convince yourself of this, diagonalize \( f \) in an orthonormal basis). Since \( f \) and \( g \) commute, the \( {E}_{{\lambda }_{i}} \) are stable under \( g \). As the restriction of \( g \) to \( {E}_{{\lambda }_{i}} \) is self-adjoint, there exists an orthonormal basis \( {B}_{i} \) of \( {E}_{{\lambda }_{i}} \) diagonalizing \( {g}_{\mid {E}_{{\lambda }_{i}}} \). Since the \( {E}_{{\lambda }_{i}} \) are pairwise orthogonal, we deduce that \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) is an orthonormal basis. This basis diagonalizes \( g \) by construction, as well as \( f \), since each vector \( e \) of \( {B}_{i} \) satisfies \( f\left( e\right) = {\lambda }_{i}e. \)

Remarque. De la même manière que dans l'exercice 4 page 181, ce résultat se généralise à toute famille \( {\left( {f}_{i}\right) }_{i \in I} \) d’endomorphismes autoadjoints commutant deux à deux.

> Remark. In the same way as in exercise 4 on page 181, this result generalizes to any family \( {\left( {f}_{i}\right) }_{i \in I} \) of pairwise commuting self-adjoint endomorphisms.

EXERCICE 3. Soit \( E \) un espace hermitien et \( f \in \mathcal{L}\left( E\right) \) .

> EXERCISE 3. Let \( E \) be a Hermitian space and \( f \in \mathcal{L}\left( E\right) \) .

a) Montrer que \( f \) est trigonalisable dans une base orthonormée de \( E \) .

> a) Show that \( f \) is trigonalizable in an orthonormal basis of \( E \) .

b) Si \( f \) et \( g \in \mathcal{L}\left( E\right) \) commutent, montrer qu’il existe une base orthonormée de \( E \) trigo-nalisant à la fois \( f \) et \( g \) .

> b) If \( f \) and \( g \in \mathcal{L}\left( E\right) \) commute, show that there exists an orthonormal basis of \( E \) trigonalizing both \( f \) and \( g \) .

Solution. a) Nous allons donner deux moyens de procéder.

> Solution. a) We will provide two ways to proceed.

Première méthode. Le corps \( \mathbb{C} \) étant algébriquement clos, \( f \) est trigonalisable dans une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) , et donc pour tout \( k, f\left( {e}_{k}\right) \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \) . Soit \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) la base orthonormée de Schmidt associée à \( B \) (voir page 253). Pour tout \( k \) , on a \( \operatorname{Vect}\left( {{u}_{1},\ldots ,{u}_{k}}\right) = \; \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \) , et donc

> First method. Since the field \( \mathbb{C} \) is algebraically closed, \( f \) is trigonalizable in a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) , and thus for all \( k, f\left( {e}_{k}\right) \in \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \) . Let \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) be the Schmidt orthonormal basis associated with \( B \) (see page 253). For all \( k \) , we have \( \operatorname{Vect}\left( {{u}_{1},\ldots ,{u}_{k}}\right) = \; \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) \) , and thus

\[
\forall k,1 \leq  k \leq  n,\;f\left( {u}_{k}\right)  \in  f\left( {\operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) }\right)  \subset  \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right)  = \operatorname{Vect}\left( {{u}_{1},\ldots ,{u}_{k}}\right) .
\]

Ceci prouve que la matrice de \( f \) dans la base orthonormée \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) est triangulaire supérieure. Second methode. On procède par récurrence sur la dimension \( n \) de \( E \) . Si \( n = 1 \) , c’est évident. Supposons maintenant le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Soit \( \lambda \in \mathbb{C} \) une valeur propre de \( {f}^{ * } \) et \( e \) un vecteur propre normé associé. Alors

> This proves that the matrix of \( f \) in the orthonormal basis \( \left( {{u}_{1},\ldots ,{u}_{n}}\right) \) is upper triangular. Second method. We proceed by induction on the dimension \( n \) of \( E \) . If \( n = 1 \) , it is obvious. Now assume the result is true at rank \( n - 1 \) and show it at rank \( n \) . Let \( \lambda \in \mathbb{C} \) be an eigenvalue of \( {f}^{ * } \) and \( e \) a normalized eigenvector associated with it. Then

\[
\forall x \in  {\left( \operatorname{Vect}e\right) }^{ \bot  },\;f\left( x\right)  \cdot  e = x \cdot  {f}^{ * }\left( e\right)  = x \cdot  {\lambda e} = \lambda \left( {x \cdot  e}\right)  = 0,
\]

autrement dit l’hyperplan \( H = {\left( \operatorname{Vect}e\right) }^{ \bot } \) est stable par \( f \) . On peut donc appliquer l’hypothèse de récurrence à \( {f}_{\mid H} \) , ce qui montre l’existence d’une base orthonormée \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) de \( H \) qui trigonalise \( {f}_{\mid H} \) . La matrice de \( f \) dans la base orthonormée \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, e}\right) \) (elle est orthonormée car \( e \) est orthogonal à \( H \) ) de \( E \) est donc de la forme

> in other words, the hyperplane \( H = {\left( \operatorname{Vect}e\right) }^{ \bot } \) is stable under \( f \). We can therefore apply the induction hypothesis to \( {f}_{\mid H} \), which shows the existence of an orthonormal basis \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) of \( H \) that triangularizes \( {f}_{\mid H} \). The matrix of \( f \) in the orthonormal basis \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, e}\right) \) (it is orthonormal because \( e \) is orthogonal to \( H \)) of \( E \) is therefore of the form

\[
\left( \begin{matrix}  \times  & \cdots &  \times  &  \times  \\  0 &  \ddots  & \vdots & \vdots \\  \vdots &  \ddots  &  \times  &  \times  \\  0 & \cdots & 0 &  \times   \end{matrix}\right) ,
\]

donc triangulaire supérieure, d'où le résultat.

> thus upper triangular, hence the result.

b) Nous allons ici aussi donner deux méthodes.

> b) Here too, we will provide two methods.

Première méthode. D'après le théorème 5 page 176, il existe une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) trigonalisant \( f \) et \( g \) . Pour les mêmes raisons que dans la première solution de la question a), la base de Schmidt orthonormée associée à \( B \) trigonalise \( f \) , ainsi que \( g \) , d’où le résultat.

> First method. According to theorem 5 on page 176, there exists a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) triangularizing \( f \) and \( g \). For the same reasons as in the first solution to question a), the orthonormal Schmidt basis associated with \( B \) triangularizes \( f \), as well as \( g \), hence the result.

Seconde méthode. Procédons par récurrence sur la dimension \( n \) de \( E \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Dans une base orthonormée de \( E \) , les matrices de \( {f}^{ * } \) et \( {g}^{ * } \) sont les transposées de celles de \( f \) et \( g \) donc elles commutent, ce qui entraîne que \( {f}^{ * } \) et \( {g}^{ * } \) commutent. Il existe donc un vecteur propre \( e \) normé commun à \( {f}^{ * } \) et \( {g}^{ * } \) (c’est classique, voir le préliminaire de la preuve du théorème de trigonalisation simultanée page 176). Pour les mêmes raisons que dans la deuxième solution de la question a), \( H = {\left( \operatorname{Vect}e\right) }^{ \bot } \) est un hyperplan de \( E \) stable par \( f \) et \( g \) . Comme \( {f}_{\mid H} \) et \( {g}_{\mid H} \) commutent, l’hypothèse de récurrence entraîne l’existence d’une base orthonormée \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) de \( H \) trigonalisant \( {f}_{\mid H} \) et \( {g}_{\mid H} \) . La base \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, e}\right) \) est orthonormée et on voit facilement qu’elle trigonalise \( f \) et \( g \) .

> Second method. Let us proceed by induction on the dimension \( n \) of \( E \). For \( n = 1 \), it is obvious. Assume the result is true at rank \( n - 1 \) and show it at rank \( n \). In an orthonormal basis of \( E \), the matrices of \( {f}^{ * } \) and \( {g}^{ * } \) are the transposes of those of \( f \) and \( g \), so they commute, which implies that \( {f}^{ * } \) and \( {g}^{ * } \) commute. There therefore exists a common normalized eigenvector \( e \) for \( {f}^{ * } \) and \( {g}^{ * } \) (this is standard, see the preliminary to the proof of the simultaneous triangularization theorem on page 176). For the same reasons as in the second solution to question a), \( H = {\left( \operatorname{Vect}e\right) }^{ \bot } \) is a hyperplane of \( E \) stable under \( f \) and \( g \). Since \( {f}_{\mid H} \) and \( {g}_{\mid H} \) commute, the induction hypothesis implies the existence of an orthonormal basis \( \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) of \( H \) triangularizing \( {f}_{\mid H} \) and \( {g}_{\mid H} \). The basis \( \left( {{e}_{1},\ldots ,{e}_{n - 1}, e}\right) \) is orthonormal and it is easy to see that it triangularizes \( f \) and \( g \).

Remarque. De la même manière qu'à l'exercice 4 page 181, le résultat b) se généralise à une famille quelconque \( {\left( {f}_{i}\right) }_{i \in I} \) d’endomorphismes commutant deux à deux.

> Remark. In the same way as in exercise 4 on page 181, result b) generalizes to any family \( {\left( {f}_{i}\right) }_{i \in I} \) of pairwise commuting endomorphisms.

\( \rightarrow \) EXERCICE 4 (CARACTÉRISATION DES MATRICES POSITIVES). Soit \( M = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice symétrique.

> \( \rightarrow \) EXERCISE 4 (CHARACTERIZATION OF POSITIVE MATRICES). Let \( M = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a symmetric matrix.

a) (Critère de Sylvester). Pour tout \( k \in \{ 1,\ldots , n\} \) , on note \( {M}_{k} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq k} \in {\mathcal{M}}_{k}\left( \mathbb{R}\right) \) . Montrer que \( M \) est définie positive si et seulement si pour tout \( k \in \{ 1,\ldots , n\} \) , det \( {M}_{k} > 0 \) . b) Pour tout \( I \subset \{ 1,\ldots , n\} \) , on note \( {M}_{I} = {\left( {a}_{i, j}\right) }_{\left( {i, j}\right) \in {I}^{2}} \) . Montrer que \( M \) est une matrice positive si et seulement si pour tout \( I \) , det \( {M}_{I} \geq 0 \) .

> a) (Sylvester's criterion). For any \( k \in \{ 1,\ldots , n\} \), let \( {M}_{k} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq k} \in {\mathcal{M}}_{k}\left( \mathbb{R}\right) \) be denoted. Show that \( M \) is positive definite if and only if for all \( k \in \{ 1,\ldots , n\} \), det \( {M}_{k} > 0 \). b) For any \( I \subset \{ 1,\ldots , n\} \), let \( {M}_{I} = {\left( {a}_{i, j}\right) }_{\left( {i, j}\right) \in {I}^{2}} \) be denoted. Show that \( M \) is a positive matrix if and only if for all \( I \), det \( {M}_{I} \geq 0 \).

Solution. a) Condition nécessaire. Notons \( q \) la forme quadratique dont \( M \) est la matrice dans la base canonique \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{R}}^{n} \) . Pour tout \( k,{M}_{k} \) est la matrice de la restriction de \( q \) à Vect \( \left( {{e}_{1},\ldots ,{e}_{k}}\right) \) . Cette restriction est, comme \( q \) , définie positive, donc \( {M}_{k} \) est une matrice définie positive, d’où on tire det \( {M}_{k} > 0 \) , et ceci pour tout \( k \) .

> Solution. a) Necessary condition. Let \( q \) be the quadratic form whose matrix in the canonical basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) is \( M \). For any \( k,{M}_{k} \), it is the matrix of the restriction of \( q \) to Vect \( \left( {{e}_{1},\ldots ,{e}_{k}}\right) \). This restriction is, like \( q \), positive definite, so \( {M}_{k} \) is a positive definite matrix, from which we derive det \( {M}_{k} > 0 \), and this for all \( k \).

Condition suffisante. Raisonnons par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Notons \( H \) l’hyperplan défini par \( H = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) . D’après l’hypothèse de récurrence, la restriction \( {q}_{\mid H} \) de \( q \) à \( H \) est définie positive. Désignons par \( \left( {{e}_{1}^{\prime },\ldots ,{e}_{n - 1}^{\prime }}\right) \) une base orthonormée pour \( {q}_{\mid H} \) . D’après la proposition 7 page 245, l’orthogonal \( {H}^{ \bot } \) de \( H \) (l’orthogonal est ici par rapport à la forme quadratique \( q \) ) vérifie \( H \oplus {H}^{ \bot } = {\mathbb{R}}^{n} \) . Ainsi, si \( {e}_{n}^{\prime } \) désigne un vecteur non nul de \( {H}^{ \bot } \) , la famille \( B = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n - 1}^{\prime },{e}_{n}^{\prime }}\right) \) est une base de \( {\mathbb{R}}^{n} \) et la matrice de \( q \) dans cette base s’écrit sous la forme

> Sufficient condition. Let us reason by induction on \( n \in {\mathbb{N}}^{ * } \). For \( n = 1 \), it is obvious. Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \). Let \( H \) be the hyperplane defined by \( H = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \). According to the induction hypothesis, the restriction \( {q}_{\mid H} \) of \( q \) to \( H \) is positive definite. Let \( \left( {{e}_{1}^{\prime },\ldots ,{e}_{n - 1}^{\prime }}\right) \) denote an orthonormal basis for \( {q}_{\mid H} \). According to proposition 7 on page 245, the orthogonal \( {H}^{ \bot } \) of \( H \) (the orthogonal is here with respect to the quadratic form \( q \)) satisfies \( H \oplus {H}^{ \bot } = {\mathbb{R}}^{n} \). Thus, if \( {e}_{n}^{\prime } \) denotes a non-zero vector of \( {H}^{ \bot } \), the family \( B = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n - 1}^{\prime },{e}_{n}^{\prime }}\right) \) is a basis of \( {\mathbb{R}}^{n} \) and the matrix of \( q \) in this basis is written in the form

\[
N = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 &  \ddots  &  \ddots  & \vdots \\  \vdots &  \ddots  & 1 & 0 \\  0 & \cdots & 0 & \alpha  \end{matrix}\right) ,
\]

Si \( P \) désigne la matrice de passage de la base canonique de \( {\mathbb{R}}^{n} \) à la base \( B \) , on a \( N = {}^{\mathrm{t}}{PMP} \) , donc det \( N = {\left( \det P\right) }^{2}\det M > 0 \) . Ainsi, \( \alpha = \det N > 0 \) , ce qui prouve que \( q \) est définie positive. La matrice \( M \) est donc définie positive.

> If \( P \) denotes the transition matrix from the canonical basis of \( {\mathbb{R}}^{n} \) to the basis \( B \), we have \( N = {}^{\mathrm{t}}{PMP} \), therefore det \( N = {\left( \det P\right) }^{2}\det M > 0 \). Thus, \( \alpha = \det N > 0 \), which proves that \( q \) is positive definite. The matrix \( M \) is therefore positive definite.

b) Condition nécessaire. On désigne toujours par \( q \) la forme quadratique de \( {\mathbb{R}}^{n} \) dont \( M \) est la matrice dans la base canonique \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{R}}^{n} \) . Pour tout \( I,{M}_{I} \) est la matrice de la restriction de \( q \) à \( \operatorname{Vect}{\left( {e}_{i}\right) }_{i \in I} \) , qui est positive. La matrice \( {M}_{I} \) est donc positive, ce qui entraîne det \( {M}_{I} \geq 0 \) . Condition suffisante. Commençons par montrer

> b) Necessary condition. We still denote by \( q \) the quadratic form of \( {\mathbb{R}}^{n} \) whose matrix in the canonical basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) is \( M \). For any \( I,{M}_{I} \) is the matrix of the restriction of \( q \) to \( \operatorname{Vect}{\left( {e}_{i}\right) }_{i \in I} \), which is positive. The matrix \( {M}_{I} \) is therefore positive, which implies det \( {M}_{I} \geq 0 \). Sufficient condition. Let us begin by showing

\[
\forall x > 0,\;\det \left( {M + x{I}_{n}}\right)  > 0.
\]

(*)

> On sait que l'on a (voir page 172)

We know that we have (see page 172)

\[
\det \left( {M + x{I}_{n}}\right)  = {x}^{n} + {\beta }_{1}{x}^{n - 1} + \cdots  + {\beta }_{n - 1}x + {\beta }_{n},
\]

où pour tout \( i,{\beta }_{i} \) est la somme des mineurs principaux d’ordre \( i \) . D’après les hypothèses, on a donc \( {\beta }_{i} = \mathop{\sum }\limits_{{\text{ Card }I = i}} \) det \( {M}_{I} \geq 0 \) . La positivité des \( {\beta }_{i} \) entraîne alors \( \left( *\right) \) .

> where for any \( i,{\beta }_{i} \) is the sum of the principal minors of order \( i \). According to the hypotheses, we therefore have \( {\beta }_{i} = \mathop{\sum }\limits_{{\text{ Card }I = i}} \) det \( {M}_{I} \geq 0 \). The positivity of the \( {\beta }_{i} \) then implies \( \left( *\right) \).

On applique maintenant le résultat \( \left( *\right) \) à chacune des matrices \( {M}_{k} \) (on peut, les hypothèses sont vérifiées car tout mineur principal de \( {M}_{k} \) est un mineur principal de \( M \) ), ce qui donne

> We now apply result \( \left( *\right) \) to each of the matrices \( {M}_{k} \) (we can, the hypotheses are verified because any principal minor of \( {M}_{k} \) is a principal minor of \( M \)), which gives

\[
\forall x > 0,\forall k \in  \{ 1,\ldots , n\} ,\;\det \left( {{M}_{k} + x{I}_{k}}\right)  > 0.
\]

En appliquant le résultat de la question a), On en déduit que pour tout \( x > 0 \) , la matrice \( M + x{I}_{n} \) est définie positive. Autrement dit, pour tout \( x > 0 \) , on a

> By applying the result of question a), we deduce that for any \( x > 0 \), the matrix \( M + x{I}_{n} \) is positive definite. In other words, for any \( x > 0 \), we have

\[
\forall X \in  {\mathbb{R}}^{n},\;{}^{\mathrm{t}}X\left( {M + x{I}_{n}}\right) X \geq  0.
\]

En fixant \( X \) et en faisant tendre \( x \) vers 0, cette inégalité entraîne \( {}^{\mathrm{t}}{XMX} \geq 0 \) , et ceci pour tout \( X \in {\mathbb{R}}^{n} \) , donc \( M \) est positive.

> By fixing \( X \) and letting \( x \) tend to 0, this inequality implies \( {}^{\mathrm{t}}{XMX} \geq 0 \), and this for any \( X \in {\mathbb{R}}^{n} \), therefore \( M \) is positive.

Remarque. Le critère de Sylvester peut s'avéer utile ; il est donc souhaitable de le connaître et de savoir le redémontrer.

> Remark. Sylvester's criterion can prove useful; it is therefore desirable to know it and to know how to re-prove it.

EXERCICE 5. a) Soit une application continue

> EXERCISE 5. a) Let a continuous mapping

\[
M : \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;t \mapsto  M\left( t\right)  = {\left\lbrack  {a}_{i, j}\left( t\right) \right\rbrack  }_{1 \leq  i, j \leq  n},
\]

telle que pour tout \( t \in \rbrack 0,1\lbrack , M\left( t\right) \) est symétrique définie positive. Montrer que la matrice

> such that for any \( t \in \rbrack 0,1\lbrack , M\left( t\right) \) is symmetric positive definite. Show that the matrix

\[
A = {\int }_{0}^{1}M\left( t\right) {dt} = {\left( {\int }_{0}^{1}{a}_{i, j}\left( t\right) dt\right) }_{1 \leq  i, j \leq  n}
\]

est symétrique définie positive.

> is symmetric positive definite.

b) Application. Montrer que la matrice

> b) Application. Show that the matrix

\[
A = {\left( \frac{1}{1 + \left| {i - j}\right| }\right) }_{1 \leq  i, j \leq  n}
\]

est définie positive (on pourra utiliser le critère de Sylvester, voir l'exercice précédent).

> is positive definite (one may use Sylvester's criterion, see the previous exercise).

Solution. a) Il est clair que la matrice \( A \) est symétrique. Maintenant, remarquons qu’une somme finie de matrices \( {\left( {M}_{i}\right) }_{1 \leq i \leq p} \) symétriques définies positives est définie positive. En effet, il suffit de remarquer que pour tout vecteur colonne \( X \neq 0 \) de \( {\mathbb{R}}^{n} \) , on a

> Solution. a) It is clear that the matrix \( A \) is symmetric. Now, let us note that a finite sum of symmetric positive definite matrices \( {\left( {M}_{i}\right) }_{1 \leq i \leq p} \) is positive definite. Indeed, it suffices to note that for any column vector \( X \neq 0 \) of \( {\mathbb{R}}^{n} \), we have

\[
\forall i,{}^{\mathrm{t}}X{M}_{i}X > 0\;\text{ donc }\;\mathop{\sum }\limits_{{i = 1}}^{p}{}^{\mathrm{t}}X{M}_{i}X = {}^{\mathrm{t}}X\left( {\mathop{\sum }\limits_{{i = 1}}^{p}{M}_{i}}\right) X > 0.
\]

Ceci étant vrai pour tout \( X \neq 0 \) , on a prouvé que \( \mathop{\sum }\limits_{i}{M}_{i} \) est définie positive.

> This being true for any \( X \neq 0 \), we have proven that \( \mathop{\sum }\limits_{i}{M}_{i} \) is positive definite.

Ici, on a affaire non pas à une somme finie, mais une somme continue. On procède de la même manière. Fixons un vecteur colonne \( X \) de \( {\mathbb{R}}^{n}, X \neq 0 \) . Pour tout \( t \in \rbrack 0,1\lbrack \) , on a \( {}^{\mathrm{t}}{XM}\left( t\right) X > 0 \) , donc par continuité de \( t \mapsto {}^{\mathrm{t}}{XM}\left( t\right) X \)

> Here, we are dealing not with a finite sum, but a continuous sum. We proceed in the same way. Let us fix a column vector \( X \) of \( {\mathbb{R}}^{n}, X \neq 0 \). For any \( t \in \rbrack 0,1\lbrack \), we have \( {}^{\mathrm{t}}{XM}\left( t\right) X > 0 \), therefore by continuity of \( t \mapsto {}^{\mathrm{t}}{XM}\left( t\right) X \)

\[
{\int }_{0}^{1}{}^{\mathrm{t}}{XM}\left( t\right) {Xdt} > 0\;\text{ ou encore }\;{}^{\mathrm{t}}X\left( {{\int }_{0}^{1}M\left( t\right) {dt}}\right) X = {}^{\mathrm{t}}{XAX} > 0.
\]

Ceci étant vrai pour tout \( X \neq 0, A \) est définie positive.

> This being true for any \( X \neq 0, A \) is positive definite.

b) On remarque que

> b) We note that

\[
\frac{1}{1 + \left| {i - j}\right| } = {\int }_{0}^{1}{t}^{\left| i - j\right| }{dt}
\]

D’après a), le résultat sera prouvé si on montre que pour tout \( t \in \rbrack 0,1\lbrack \) , la matrice symétrique \( M\left( t\right) = {\left( {t}^{\left| i - j\right| }\right) }_{1 < i, j < n} \) est définie positive.

> According to a), the result will be proven if we show that for all \( t \in \rbrack 0,1\lbrack \), the symmetric matrix \( M\left( t\right) = {\left( {t}^{\left| i - j\right| }\right) }_{1 < i, j < n} \) is positive definite.

Pour tout \( r,1 \leq r \leq n \) , on pose \( {D}_{r}\left( t\right) = \det {\left( {t}^{\left| i - j\right| }\right) }_{1 < i, j < r} \) . Nous allons prouver que \( {D}_{r}\left( t\right) = \; {\left( 1 - {t}^{2}\right) }^{r - 1} \) ce qui prouvera, en vertu du critère de Sylvester, que \( M\left( t\right) \) est définie positive pour \( t \in \rbrack 0,1\lbrack \) .

> For all \( r,1 \leq r \leq n \), let \( {D}_{r}\left( t\right) = \det {\left( {t}^{\left| i - j\right| }\right) }_{1 < i, j < r} \). We will prove that \( {D}_{r}\left( t\right) = \; {\left( 1 - {t}^{2}\right) }^{r - 1} \), which will prove, by Sylvester's criterion, that \( M\left( t\right) \) is positive definite for \( t \in \rbrack 0,1\lbrack \).

On procède par récurrence sur \( r \) . Pour \( r = 1 \) , c’est évident car \( {D}_{1}\left( t\right) = 1 \) . Supposons le résultat vrai au rang \( r \) et montrons le au rang \( r + 1 \) . En retranchant à la dernière colonne \( t \) fois l'avant dernière, on obtient

> We proceed by induction on \( r \). For \( r = 1 \), it is obvious because \( {D}_{1}\left( t\right) = 1 \). Assume the result is true at rank \( r \) and show it at rank \( r + 1 \). By subtracting \( t \) times the penultimate column from the last column, we obtain

\[
{D}_{r + 1}\left( t\right)  = \left| \begin{matrix} 1 & t & \cdots & {t}^{r - 1} & {t}^{r} \\  t & 1 &  \ddots  &  \ddots  & {t}^{r - 1} \\  \vdots &  \ddots  &  \ddots  &  \ddots  & \vdots \\  {t}^{r - 1} &  \ddots  &  \ddots  & 1 & t \\  {t}^{r} & {t}^{r - 1} & \cdots & t & 1 \end{matrix}\right|  = \left| \begin{matrix} 1 & t & \cdots & {t}^{r - 1} & 0 \\  t & 1 &  \ddots  &  \ddots  & 0 \\  \vdots &  \ddots  &  \ddots  &  \ddots  & \vdots \\  {t}^{r - 1} &  \ddots  &  \ddots  & 1 & 0 \\  {t}^{r} & {t}^{r - 1} & \cdots & t & 1 - {t}^{2} \end{matrix}\right|  = \left( {1 - {t}^{2}}\right) {D}_{r}\left( t\right) ,
\]

d'où le résultat.

> hence the result.

\( \rightarrow \) EXERCICE 6 (DÉCOMPOSITION POLAIRE). Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer qu’il existe un couple de matrices \( \left( {U, H}\right) , U \) étant unitaire et \( H \) hermitienne positive, tel que \( A = {UH} \) . Si \( A \) est inversible, montrer que le couple \( \left( {U, H}\right) \) ainsi défini est unique.

> \( \rightarrow \) EXERCISE 6 (POLAR DECOMPOSITION). Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \). Show that there exists a pair of matrices \( \left( {U, H}\right) , U \) being unitary and \( H \) being positive Hermitian, such that \( A = {UH} \). If \( A \) is invertible, show that the pair \( \left( {U, H}\right) \) thus defined is unique.

Solution. C'est très classique.

> Solution. This is very classic.

Existence. Si \( A = {UH} \) , alors \( {A}^{ * } = H{U}^{-1} \) donc \( {A}^{ * }A = {H}^{2} \) (on rappelle que la notation \( {A}^{ * } \) désigne la matrice \( {}^{\mathrm{t}}\bar{A} \) ). Nous allons par conséquent commencer par chercher une matrice hermitienne \( H \) vérifiant \( {A}^{ * }A = {H}^{2} \) .

> Existence. If \( A = {UH} \), then \( {A}^{ * } = H{U}^{-1} \) so \( {A}^{ * }A = {H}^{2} \) (recall that the notation \( {A}^{ * } \) denotes the matrix \( {}^{\mathrm{t}}\bar{A} \)). We will therefore begin by looking for a Hermitian matrix \( H \) satisfying \( {A}^{ * }A = {H}^{2} \).

La matrice \( {A}^{ * }A \) est hermitienne car \( {\left( {A}^{ * }A\right) }^{ * } = {A}^{ * }{A}^{* * } = {A}^{ * }A \) . Par ailleurs, pour tout vecteur colonne \( X \) , on a

> The matrix \( {A}^{ * }A \) is Hermitian because \( {\left( {A}^{ * }A\right) }^{ * } = {A}^{ * }{A}^{* * } = {A}^{ * }A \). Furthermore, for any column vector \( X \), we have

\[
{X}^{ * }\left( {{A}^{ * }A}\right) X = {\left( AX\right) }^{ * }{AX} = \parallel {AX}{\parallel }^{2} \geq  0
\]

(∥.∥ désignant la norme hermitienne standard sur \( {\mathbb{C}}^{n} \) ), ce qui prouve que \( {A}^{ * }A \) est positive. D’après l’exercice 1 page 257, il existe donc une matrice hermitienne \( H \) positive telle que \( {A}^{ * }A = \; {H}^{2} \) .

> (∥.∥ denoting the standard Hermitian norm on \( {\mathbb{C}}^{n} \)), which proves that \( {A}^{ * }A \) is positive. According to exercise 1 on page 257, there therefore exists a positive Hermitian matrix \( H \) such that \( {A}^{ * }A = \; {H}^{2} \).

Supposons maintenant \( A \) inversible. Alors \( H \) est inversible, et en posant \( U = A{H}^{-1} \) , on a \( {U}^{ * }U = {H}^{-1}{A}^{ * }A{H}^{-1} = {I}_{n} \) , donc \( U \) est unitaire et \( A = {UH} \) , d’où l’existence.

> Now suppose \( A \) is invertible. Then \( H \) is invertible, and by setting \( U = A{H}^{-1} \), we have \( {U}^{ * }U = {H}^{-1}{A}^{ * }A{H}^{-1} = {I}_{n} \), so \( U \) is unitary and \( A = {UH} \), hence the existence.

Si \( A \) n’est pas inversible, c’est un peu plus délicat. Nous allons donner deux méthodes, la première étant de nature constructive, la seconde de nature topologique.

> If \( A \) is not invertible, it is a bit more delicate. We will provide two methods, the first being constructive in nature, the second being topological in nature.

Première méthode. Notons \( a \) et \( h \) les endomorphismes de \( {\mathbb{C}}^{n} \) dont les matrices dans la base canonique de \( {\mathbb{C}}^{n} \) sont \( A \) et \( H \) . Comme \( {a}^{ * }a = {h}^{2} \) avec \( h \) autoadjoint, on a

> First method. Let \( a \) and \( h \) be the endomorphisms of \( {\mathbb{C}}^{n} \) whose matrices in the canonical basis of \( {\mathbb{C}}^{n} \) are \( A \) and \( H \) . Since \( {a}^{ * }a = {h}^{2} \) with \( h \) self-adjoint, we have

\[
\forall x \in  {\mathbb{C}}^{n},\;\parallel a\left( x\right) {\parallel }^{2} = a\left( x\right)  \cdot  a\left( x\right)  = x \cdot  {a}^{ * }a\left( x\right)  = x \cdot  {h}^{2}\left( x\right)  = h\left( x\right)  \cdot  h\left( x\right)  = \parallel h\left( x\right) {\parallel }^{2},
\]

(*)

> donc \( \operatorname{Ker}h = \operatorname{Ker}a \) . En diagonalisant \( h \) dans une base orthonormée on s’aperçoit que \( \operatorname{Im}h = \; {\left( \operatorname{Ker}h\right) }^{ \bot } \) et \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , et que la restriction de \( h \) à \( \operatorname{Im}h \) est un automorphisme de \( \operatorname{Im}h \) .

therefore \( \operatorname{Ker}h = \operatorname{Ker}a \) . By diagonalizing \( h \) in an orthonormal basis, we notice that \( \operatorname{Im}h = \; {\left( \operatorname{Ker}h\right) }^{ \bot } \) and \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , and that the restriction of \( h \) to \( \operatorname{Im}h \) is an automorphism of \( \operatorname{Im}h \) .

> Pour que \( a = u \circ h \) sur \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , il suffit que cette égalité soit vraie sur \( \operatorname{Im}h \) puisque si \( x \in \operatorname{Ker}h = \operatorname{Ker}a \) , l’égalité \( a\left( x\right) = u \circ h\left( x\right) \) est toujours vraie (les termes sont nuls dans ce cas). Pour cette raison, nous définissons \( u \) par \( u\left( x\right) = a \circ {h}_{\mid \operatorname{Im}h}^{-1}\left( x\right) \) lorsque \( x \in \operatorname{Im}h \) . Pour que \( u \) soit unitaire, il faut que lorsque \( x \in \operatorname{Ker}h \) le vecteur \( u\left( x\right) \) soit orthogonal à \( \operatorname{Im}a \) . Si \( {u}_{0} \) désigne un isomorphisme unitaire fixé qui envoie Ker \( h \) sur \( {\left( \operatorname{Im}a\right) }^{ \bot } \) (c’est possible puisque dim \( \operatorname{Ker}h = \dim \operatorname{Ker}a = \dim {\left( \operatorname{Im}a\right) }^{ \bot } \) ), on pose donc \( u\left( x\right) = {u}_{0}\left( x\right) \) lorsque \( x \in \operatorname{Ker}h \) . En résumé, on a définit \( u \) sur \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) par

For \( a = u \circ h \) on \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , it suffices that this equality holds on \( \operatorname{Im}h \) since if \( x \in \operatorname{Ker}h = \operatorname{Ker}a \) , the equality \( a\left( x\right) = u \circ h\left( x\right) \) is always true (the terms are zero in this case). For this reason, we define \( u \) by \( u\left( x\right) = a \circ {h}_{\mid \operatorname{Im}h}^{-1}\left( x\right) \) when \( x \in \operatorname{Im}h \) . For \( u \) to be unitary, it is necessary that when \( x \in \operatorname{Ker}h \) the vector \( u\left( x\right) \) is orthogonal to \( \operatorname{Im}a \) . If \( {u}_{0} \) denotes a fixed unitary isomorphism that maps Ker \( h \) onto \( {\left( \operatorname{Im}a\right) }^{ \bot } \) (this is possible since dim \( \operatorname{Ker}h = \dim \operatorname{Ker}a = \dim {\left( \operatorname{Im}a\right) }^{ \bot } \) ), we therefore set \( u\left( x\right) = {u}_{0}\left( x\right) \) when \( x \in \operatorname{Ker}h \) . In summary, we have defined \( u \) on \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) by

\[
\left\{  {\begin{array}{ll} \forall x \in  \operatorname{Im}h, & u\left( x\right)  = a \circ  {h}_{\mid \operatorname{Im}h}^{-1}\left( x\right) \\  \forall x \in  \operatorname{Ker}h, & u\left( x\right)  = {u}_{0}\left( x\right)  \end{array}.}\right.
\]

Par construction, on a bien \( a = u \circ h \) . Il reste à vérifier que \( u \) est bien unitaire. Pour cela, donnons nous un vecteur \( z \in {\mathbb{C}}^{n} \) . Comme \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , il existe \( x \in {\mathbb{C}}^{n} \) et \( y \in \operatorname{Ker}h \) tels que \( z = h\left( x\right) + y \) . On a alors \( u\left( z\right) = u\left( {h\left( x\right) }\right) + u\left( y\right) = a\left( x\right) + {u}_{0}\left( y\right) \) , et comme \( {u}_{0}\left( y\right) \in {\left( \operatorname{Im}a\right) }^{ \bot } \)

> By construction, we indeed have \( a = u \circ h \) . It remains to verify that \( u \) is indeed unitary. To do this, let us take a vector \( z \in {\mathbb{C}}^{n} \) . Since \( {\mathbb{C}}^{n} = \operatorname{Im}h \oplus \operatorname{Ker}h \) , there exist \( x \in {\mathbb{C}}^{n} \) and \( y \in \operatorname{Ker}h \) such that \( z = h\left( x\right) + y \) . We then have \( u\left( z\right) = u\left( {h\left( x\right) }\right) + u\left( y\right) = a\left( x\right) + {u}_{0}\left( y\right) \) , and since \( {u}_{0}\left( y\right) \in {\left( \operatorname{Im}a\right) }^{ \bot } \)

\[
\parallel u\left( z\right) {\parallel }^{2} = \parallel a\left( x\right) {\parallel }^{2} + {\begin{Vmatrix}{u}_{0}\left( y\right) \end{Vmatrix}}^{2}.
\]

Par construction de \( {u}_{0} \) , on a \( \begin{Vmatrix}{{u}_{0}\left( y\right) }\end{Vmatrix} = \parallel y\parallel \) . Comme de plus \( \parallel a\left( x\right) \parallel = \parallel h\left( x\right) \parallel \) d’après l’iden-tité \( \left( *\right) \) , l’orthogonalité de \( h\left( x\right) \in \operatorname{Im}h \) et \( y \in \operatorname{Ker}h \) entraîne finalement

> By construction of \( {u}_{0} \), we have \( \begin{Vmatrix}{{u}_{0}\left( y\right) }\end{Vmatrix} = \parallel y\parallel \). Since, moreover, \( \parallel a\left( x\right) \parallel = \parallel h\left( x\right) \parallel \) according to the identity \( \left( *\right) \), the orthogonality of \( h\left( x\right) \in \operatorname{Im}h \) and \( y \in \operatorname{Ker}h \) finally entails

\[
\parallel u\left( z\right) {\parallel }^{2} = \parallel h\left( x\right) {\parallel }^{2} + \parallel y{\parallel }^{2} = \parallel z{\parallel }^{2}.
\]

Notons \( U \) la matrice de \( u \) dans la base canonique de \( {\mathbb{C}}^{n} \) . On a \( a = u \circ h \) donc \( A = {UH} \) , avec \( U \) unitaire, d’où le résultat.

> Let \( U \) be the matrix of \( u \) in the canonical basis of \( {\mathbb{C}}^{n} \). We have \( a = u \circ h \) therefore \( A = {UH} \), with \( U \) unitary, hence the result.

Seconde méthode. L’ensemble des matrices inversibles étant dense dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) (voir la proposition 2, page 193), on peut écrire \( A \) comme une limite de matrices inversibles \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \) . Le cas \( A \) inversible nous permet d’affirmer que pour tout \( p \in \mathbb{N} \) , il existe deux matrices \( {U}_{p} \) unitaire et \( {H}_{p} \) hermitienne positive telles que \( {A}_{p} = {U}_{p}{H}_{p} \) . L’ensemble des matrices unitaires étant compact (c’est un fermé borné de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , fermé comme image réciproque de \( \left\{ {I}_{n}\right\} \) par l’application continue \( U \mapsto {U}^{ * }U \) , borné car tous les vecteurs colonnes d’une matrice unitaire sont de norme 1), il existe une sous-suite \( \left( {U}_{\varphi \left( p\right) }\right) \) de \( \left( {U}_{p}\right) \) qui converge. Notons \( U \) sa limite ( \( U \) est unitaire). L’égalité \( {H}_{\varphi \left( p\right) } = {U}_{\varphi \left( p\right) }^{ * }{A}_{\varphi \left( p\right) } \) entraine la convergence de la suite \( \left( {H}_{\varphi \left( p\right) }\right) \) vers \( H = {UA} \) , et comme \( {H}_{\varphi \left( p\right) } \) est hermitienne positive pour tout \( p, H \) est hermitienne positive (en effet, \( H \) est clairement hermitienne, et positive car pour tout \( X \in {\mathbb{C}}^{n} \) fixé, on a \( {X}^{ * }{H}_{\varphi \left( p\right) }X \geq 0 \) , donc en faisant tendre \( p \) vers l’infini on obtient \( {X}^{ * }{HX} \geq 0 \) , et ceci est vrai pour tout \( X \) ). Finalement, on a \( A = {UH} \) avec \( U \) unitaire et \( H \) hermitienne positive.

> Second method. Since the set of invertible matrices is dense in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) (see proposition 2, page 193), we can write \( A \) as a limit of invertible matrices \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \). The case where \( A \) is invertible allows us to state that for any \( p \in \mathbb{N} \), there exist two matrices, \( {U}_{p} \) unitary and \( {H}_{p} \) positive Hermitian, such that \( {A}_{p} = {U}_{p}{H}_{p} \). Since the set of unitary matrices is compact (it is a closed bounded subset of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), closed as the inverse image of \( \left\{ {I}_{n}\right\} \) by the continuous map \( U \mapsto {U}^{ * }U \), bounded because all column vectors of a unitary matrix have norm 1), there exists a subsequence \( \left( {U}_{\varphi \left( p\right) }\right) \) of \( \left( {U}_{p}\right) \) that converges. Let \( U \) be its limit (\( U \) is unitary). The equality \( {H}_{\varphi \left( p\right) } = {U}_{\varphi \left( p\right) }^{ * }{A}_{\varphi \left( p\right) } \) entails the convergence of the sequence \( \left( {H}_{\varphi \left( p\right) }\right) \) to \( H = {UA} \), and since \( {H}_{\varphi \left( p\right) } \) is positive Hermitian for all \( p, H \), it is positive Hermitian (indeed, \( H \) is clearly Hermitian, and positive because for any fixed \( X \in {\mathbb{C}}^{n} \), we have \( {X}^{ * }{H}_{\varphi \left( p\right) }X \geq 0 \), so by letting \( p \) tend to infinity we obtain \( {X}^{ * }{HX} \geq 0 \), and this is true for any \( X \)). Finally, we have \( A = {UH} \) with \( U \) unitary and \( H \) positive Hermitian.

Unicité (lorsque \( A \) est inversible). D’après l’exercice 1 page 257, il existe une unique matrice \( H \) hermitienne positive telle que \( {A}^{ * }A = {H}^{2} \) (rappelons que \( {A}^{ * }A \) est hermitienne positive), ce qui prouve l’unicité de \( H \) , donc de \( U \) car \( U = A{H}^{-1} \) .

> Uniqueness (when \( A \) is invertible). According to exercise 1 on page 257, there exists a unique positive Hermitian matrix \( H \) such that \( {A}^{ * }A = {H}^{2} \) (recall that \( {A}^{ * }A \) is positive Hermitian), which proves the uniqueness of \( H \), and therefore of \( U \) because \( U = A{H}^{-1} \).

EXERCICE 7 (DÉCOMPOSITION D’IWASAWA). a) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice hermi-tienne définie positive. Montrer qu’il existe une unique matrice triangulaire supérieure \( T \) à coefficients diagonaux positifs, telle que \( A = {T}^{ * }T \) .

> EXERCISE 7 (IWASAWA DECOMPOSITION). a) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a positive definite Hermitian matrix. Show that there exists a unique upper triangular matrix \( T \) with positive diagonal coefficients such that \( A = {T}^{ * }T \) .

b) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice inversible. Montrer qu’il existe un unique couple de matrices \( \left( {U, T}\right) \) , avec \( U \) unitaire et \( T \) triangulaire supérieure à coefficients diagonaux positifs, tel que \( A = {UT} \) .

> b) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be an invertible matrix. Show that there exists a unique pair of matrices \( \left( {U, T}\right) \) , with \( U \) unitary and \( T \) upper triangular with positive diagonal coefficients, such that \( A = {UT} \) .

Solution. a) Comme \( A \) est hermitienne définie positive, \( A \) est la matrice d’un produit scalaire hermitien dans la base canonique \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{C}}^{n} \) . Écrire \( A = {P}^{ * }P \) , c’est dire que \( P \) est la matrice de passage d’une base \( {B}^{\prime } \) orthonormée pour ce produit scalaire à la base \( B \) .

> Solution. a) Since \( A \) is positive definite Hermitian, \( A \) is the matrix of a Hermitian inner product in the canonical basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{C}}^{n} \) . Writing \( A = {P}^{ * }P \) means that \( P \) is the transition matrix from a basis \( {B}^{\prime } \) orthonormal for this inner product to the basis \( B \) .

Il s’agit par conséquent de déterminer les bases \( {B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n}^{\prime }}\right) \) orthonormées pour ce produit scalaire telles que la matrice de passage \( P \) de \( {B}^{\prime } \) à \( B \) soit triangulaire supérieure et à coefficients diagonaux positifs, ce qui s'écrit

> It is therefore a matter of determining the bases \( {B}^{\prime } = \left( {{e}_{1}^{\prime },\ldots ,{e}_{n}^{\prime }}\right) \) orthonormal for this inner product such that the transition matrix \( P \) from \( {B}^{\prime } \) to \( B \) is upper triangular and has positive diagonal coefficients, which is written

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\left\{  \begin{array}{l} \operatorname{Vect}\left( {{e}_{1}^{\prime },\ldots ,{e}_{k}^{\prime }}\right)  = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{k}}\right) , \\  {e}_{k}^{\prime } \cdot  {e}_{k} > 0. \end{array}\right.
\]

Le procédé d'orthonormalisation de Schmidt assure l'existence et l'unicité d'une telle base, d'où l’existence et l’unicité de \( T \) .

> The Gram-Schmidt orthonormalization process ensures the existence and uniqueness of such a basis, hence the existence and uniqueness of \( T \) .

b) Comme on l’a vu à l’exercice précédent, la matrice \( {A}^{ * }A \) est hermitienne positive. Comme \( A \) est inversible, \( {A}^{ * }A \) est inversible, et c’est donc une matrice hermitienne définie positive. D’après la question a), il existe une matrice \( T \) triangulaire supérieure à coefficients diagonaux positifs telle que \( {A}^{ * }A = {T}^{ * }T \) . Soit \( U = A{T}^{-1} \) . Alors \( {U}^{ * }U = {\left( {T}^{ * }\right) }^{-1}{A}^{ * }A{T}^{-1} = I \) . Donc \( U \) est unitaire et \( A = {UT} \) , d’où l’existence du couple \( \left( {U, T}\right) \) .

> b) As seen in the previous exercise, the matrix \( {A}^{ * }A \) is positive Hermitian. Since \( A \) is invertible, \( {A}^{ * }A \) is invertible, and is therefore a positive definite Hermitian matrix. According to question a), there exists an upper triangular matrix \( T \) with positive diagonal coefficients such that \( {A}^{ * }A = {T}^{ * }T \) . Let \( U = A{T}^{-1} \) . Then \( {U}^{ * }U = {\left( {T}^{ * }\right) }^{-1}{A}^{ * }A{T}^{-1} = I \) . Thus \( U \) is unitary and \( A = {UT} \) , hence the existence of the pair \( \left( {U, T}\right) \) .

Unicité. Si \( A = {UT} \) , alors \( {A}^{ * }A = {T}^{ * }T \) , donc d’après a), \( T \) est déterminée de façon unique ; il en est de même pour \( U = A{T}^{-1} \) .

> Uniqueness. If \( A = {UT} \) , then \( {A}^{ * }A = {T}^{ * }T \) , so according to a), \( T \) is uniquely determined; the same holds for \( U = A{T}^{-1} \) .

Remarque. On peut montrer que le résultat reste vrai lorsque \( A \) n’est pas supposée inversible, mais il n’y a plus unicité du couple \( \left( {U, T}\right) \) . (On peut par exemple procéder en utilisant des critères de nature topologique comme dans la seconde méthode de la preuve de l'existence dans l'exercice précédent).

> Remark. It can be shown that the result remains true when \( A \) is not assumed to be invertible, but the pair \( \left( {U, T}\right) \) is no longer unique. (One can, for example, proceed by using topological criteria as in the second method of the existence proof in the previous exercise).

EXERCICE 8. À partir de la norme euclidienne standard \( \parallel \cdot {\parallel }_{2} \) sur \( {\mathbb{R}}^{n} \)

> EXERCISE 8. Starting from the standard Euclidean norm \( \parallel \cdot {\parallel }_{2} \) on \( {\mathbb{R}}^{n} \)

\[
\forall X = \left( \begin{matrix} {x}_{1} \\  \vdots \\  {x}_{n} \end{matrix}\right)  \in  {\mathbb{R}}^{n},\;\parallel X{\parallel }_{2} = \sqrt{{x}_{1}^{2} + \cdots  + {x}_{n}^{2}},
\]

on norme \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) en posant, pour tout \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\parallel A{\parallel }_{2} = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}\parallel {AX}{\parallel }_{2} \) .

> we normalize \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) by setting, for all \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\parallel A{\parallel }_{2} = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}\parallel {AX}{\parallel }_{2} \) .

Montrer que \( \parallel A{\parallel }_{2} = \sqrt{\rho \left( {{A}^{ * }A}\right) } \) , où \( \rho \left( {{A}^{ * }A}\right) = \sup \{ \left| \lambda \right| \mid \lambda \) valeur propre de \( {A}^{ * }A\} \) .

> Show that \( \parallel A{\parallel }_{2} = \sqrt{\rho \left( {{A}^{ * }A}\right) } \) , where \( \rho \left( {{A}^{ * }A}\right) = \sup \{ \left| \lambda \right| \mid \lambda \) is an eigenvalue of \( {A}^{ * }A\} \) .

Solution. On remarque déjà que pour tout \( X \in {\mathbb{R}}^{n},\parallel X{\parallel }_{2} = \sqrt{{X}^{ * }X} \) , de sorte que

> Solution. We first note that for all \( X \in {\mathbb{R}}^{n},\parallel X{\parallel }_{2} = \sqrt{{X}^{ * }X} \) , so that

\[
\parallel A{\parallel }_{2}^{2} = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}{\left( AX\right) }^{ * }{AX} = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}{X}^{ * }\left( {{A}^{ * }A}\right) X.
\]

La matrice \( {A}^{ * }A \) est symétrique positive (c’est hyper-classique, elle est symétrique car \( {\left( {A}^{ * }A\right) }^{ * } = \; {A}^{ * }{A}^{* * } = {A}^{ * }A \) , positive car \( \forall X \in {\mathbb{R}}^{n},{X}^{ * }\left( {{A}^{ * }A}\right) X = {\left( AX\right) }^{ * }{AX} = \parallel {AX}{\parallel }_{2}^{2} \geq 0 \) ). Il existe donc une matrice orthogonale \( P \) telle que \( {A}^{ * }A = {P}^{-1}{DP} = {P}^{ * }{DP} \) où \( D \) est une matrice diagonale. On a

> The matrix \( {A}^{ * }A \) is symmetric positive (this is standard, it is symmetric because \( {\left( {A}^{ * }A\right) }^{ * } = \; {A}^{ * }{A}^{* * } = {A}^{ * }A \) , and positive because \( \forall X \in {\mathbb{R}}^{n},{X}^{ * }\left( {{A}^{ * }A}\right) X = {\left( AX\right) }^{ * }{AX} = \parallel {AX}{\parallel }_{2}^{2} \geq 0 \) ). There exists an orthogonal matrix \( P \) such that \( {A}^{ * }A = {P}^{-1}{DP} = {P}^{ * }{DP} \) where \( D \) is a diagonal matrix. We have

\[
\parallel A{\parallel }_{2}^{2} = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}{X}^{ * }\left( {{P}^{ * }{DP}}\right) X = \mathop{\sup }\limits_{{\parallel X{\parallel }_{2} = 1}}{\left( PX\right) }^{ * }D\left( {PX}\right) .
\]

L’application \( X \mapsto {PX} \) étant une isométrie de \( {\mathbb{R}}^{n} \) , ceci s’écrit aussi

> Since the map \( X \mapsto {PX} \) is an isometry of \( {\mathbb{R}}^{n} \) , this can also be written as

\[
\parallel A{\parallel }_{2}^{2} = \mathop{\sup }\limits_{{\parallel Y{\parallel }_{2} = 1}}{Y}^{ * }{DY}.
\]

(*)

> En notant \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) les coefficients diagonaux de \( D \) (ce sont les valeurs propres de la matrice définie positive \( {A}^{ * }A \) , donc positives, et vérifient \( {\sup }_{i}{\lambda }_{i} = \rho \left( {{A}^{ * }A}\right) \) ), on a

By denoting \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) as the diagonal coefficients of \( D \) (these are the eigenvalues of the positive definite matrix \( {A}^{ * }A \) , hence positive, and satisfy \( {\sup }_{i}{\lambda }_{i} = \rho \left( {{A}^{ * }A}\right) \) ), we have

\[
\forall Y = \left( \begin{matrix} {y}_{1} \\  \vdots \\  {y}_{n} \end{matrix}\right)  \in  {\mathbb{R}}^{n}\text{ tel que }\parallel Y{\parallel }_{2} = 1,\;{Y}^{ * }{DY} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{y}_{i}^{2} \leq  \rho \left( {{A}^{ * }A}\right) \mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}^{2} = \rho \left( {{A}^{ * }A}\right) ,
\]

donc d’après \( \left( *\right) ,\parallel A{\parallel }_{2}^{2} \leq \rho \left( {{A}^{ * }A}\right) \) . En choisissant \( k \) tel que \( {\lambda }_{k} = \rho \left( {{A}^{ * }A}\right) \) et par \( {E}_{k} \) le \( k \) -ième vecteur de la base canonique de \( {\mathbb{R}}^{n} \) , on a \( {\begin{Vmatrix}{E}_{k}\end{Vmatrix}}_{2} = 1 \) et \( {E}_{k}^{ * }D{E}_{k} = {\lambda }_{k} = \rho \left( {{A}^{ * }A}\right) \) , donc d’après \( \left( *\right) \) on a \( \parallel A{\parallel }_{2}^{2} \geq \rho \left( {{A}^{ * }A}\right) \) . Finalement, on a montré \( \parallel A{\parallel }_{2}^{2} = \rho \left( {{A}^{ * }A}\right) \) .

> therefore according to \( \left( *\right) ,\parallel A{\parallel }_{2}^{2} \leq \rho \left( {{A}^{ * }A}\right) \) . By choosing \( k \) such that \( {\lambda }_{k} = \rho \left( {{A}^{ * }A}\right) \) and letting \( {E}_{k} \) be the \( k \) -th vector of the canonical basis of \( {\mathbb{R}}^{n} \) , we have \( {\begin{Vmatrix}{E}_{k}\end{Vmatrix}}_{2} = 1 \) and \( {E}_{k}^{ * }D{E}_{k} = {\lambda }_{k} = \rho \left( {{A}^{ * }A}\right) \) , so according to \( \left( *\right) \) we have \( \parallel A{\parallel }_{2}^{2} \geq \rho \left( {{A}^{ * }A}\right) \) . Finally, we have shown \( \parallel A{\parallel }_{2}^{2} = \rho \left( {{A}^{ * }A}\right) \) .

EXERCICE 9. Soit \( E \) un \( \mathbb{R} \) -espace vectoriel normé et vérifiant

> EXERCISE 9. Let \( E \) be a normed \( \mathbb{R} \) -vector space satisfying

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\parallel x + y{\parallel }^{2} + \parallel x - y{\parallel }^{2} = 2\parallel x{\parallel }^{2} + 2\parallel y{\parallel }^{2}.
\]

(*)

> Montrer que \( E \) est préhilbertien réel (i.e la norme est issue d’un produit scalaire).

Show that \( E \) is a real pre-Hilbert space (i.e., the norm is derived from an inner product).

> Solution. Il s’agit de montrer qu’il existe un produit scalaire \( \left( {x, y}\right) \mapsto \varphi \left( {x, y}\right) \) sur \( E \) tel que pour tout \( x \in E,\varphi \left( {x, x}\right) = \parallel x{\parallel }^{2} \) .

Solution. We must show that there exists an inner product \( \left( {x, y}\right) \mapsto \varphi \left( {x, y}\right) \) on \( E \) such that for all \( x \in E,\varphi \left( {x, x}\right) = \parallel x{\parallel }^{2} \) .

> On raisonne par conditions nécessaires. Si un tel produit scalaire existe, alors

We reason by necessary conditions. If such an inner product exists, then

\[
\forall x, y \in  E,\;{4\varphi }\left( {x, y}\right)  = \varphi \left( {x + y, x + y}\right)  - \varphi \left( {x - y, x - y}\right)  = \parallel x + y{\parallel }^{2} - \parallel x - y{\parallel }^{2}.
\]

On définit donc \( \varphi \) par

> We therefore define \( \varphi \) by

\[
\varphi  : E \times  E \rightarrow  \mathbb{R}\;\left( {x, y}\right)  \mapsto  \frac{1}{4}\parallel x + y{\parallel }^{2} - \frac{1}{4}\parallel x - y{\parallel }^{2}.
\]

Nous allons montrer que \( \psi = {4\varphi } \) est un produit scalaire, ce qui montrera le résultat pour \( \varphi \) .

> We will show that \( \psi = {4\varphi } \) is an inner product, which will prove the result for \( \varphi \) .

Montrons que \( \psi \) est bilinéaire. Comme \( \psi \) est symétrique en ses arguments, il suffit de démontrer la linéarité pour l'un d'entre eux, par exemple le premier.

> Let us show that \( \psi \) is bilinear. Since \( \psi \) is symmetric in its arguments, it suffices to demonstrate linearity for one of them, for example the first.

- Montrons que \( \psi \) est additive par rapport à son premier argument. Pour tout \( x, y, z \in  E \) , on a

> - Let us show that \( \psi \) is additive with respect to its first argument. For all \( x, y, z \in  E \) , we have

\[
2\left( {\psi \left( {x, z}\right)  + \psi \left( {y, z}\right) }\right)  = \left( {2\parallel x + z{\parallel }^{2} + 2\parallel y + z{\parallel }^{2}}\right)  - \left( {2\parallel x - z{\parallel }^{2} + 2\parallel y - z{\parallel }^{2}}\right) ,
\]

\[
= \left( {\parallel x + y + {2z}{\parallel }^{2} + \parallel x - y{\parallel }^{2}}\right)  - \left( {\parallel x + y - {2z}{\parallel }^{2} + \parallel x - y{\parallel }^{2}}\right)  = \psi \left( {x + y,{2z}}\right) ,
\]

où nous avons utilisé l’identité \( \left( *\right) \) . Posons alors \( {x}_{0} = x + y \) :

> where we have used the identity \( \left( *\right) \) . Let us then set \( {x}_{0} = x + y \) :

\[
\psi \left( {{x}_{0},{2z}}\right)  = {\begin{Vmatrix}{x}_{0} + 2z\end{Vmatrix}}^{2} - {\begin{Vmatrix}{x}_{0} - 2z\end{Vmatrix}}^{2} = \left( {{\begin{Vmatrix}{x}_{0} + 2z\end{Vmatrix}}^{2} + {\begin{Vmatrix}{x}_{0}\end{Vmatrix}}^{2}}\right)  - \left( {{\begin{Vmatrix}{x}_{0} - 2z\end{Vmatrix}}^{2} + {\begin{Vmatrix}{x}_{0}\end{Vmatrix}}^{2}}\right)
\]

\[
= \left( {2{\begin{Vmatrix}{x}_{0} + z\end{Vmatrix}}^{2} + 2\parallel z{\parallel }^{2}}\right)  - \left( {2{\begin{Vmatrix}{x}_{0} - z\end{Vmatrix}}^{2} + 2\parallel z{\parallel }^{2}}\right)  = {2\psi }\left( {{x}_{0}, z}\right) .
\]

Finalement, on a

> Finally, we have

\[
2\left( {\psi \left( {x, z}\right)  + \psi \left( {y, z}\right) }\right)  = \psi \left( {{x}_{0},{2z}}\right)  = {2\psi }\left( {{x}_{0}, z}\right)  = {2\psi }\left( {x + y, z}\right)
\]

donc \( \psi \left( {x, z}\right) + \psi \left( {y, z}\right) = \psi \left( {x + y, z}\right) .\;\left( {* * }\right) \)

> therefore \( \psi \left( {x, z}\right) + \psi \left( {y, z}\right) = \psi \left( {x + y, z}\right) .\;\left( {* * }\right) \)

Il nous reste à montrer que pour \( x, z \in E \) et \( \lambda \in \mathbb{R},\psi \left( {{\lambda x}, z}\right) = {\lambda \psi }\left( {x, z}\right) \) . C’est classique !

> It remains for us to show that for \( x, z \in E \) and \( \lambda \in \mathbb{R},\psi \left( {{\lambda x}, z}\right) = {\lambda \psi }\left( {x, z}\right) \) . This is standard!

- Si \( p \in  {\mathbb{N}}^{ * } \) , alors \( \psi \left( {{px}, z}\right)  = \psi \left( {x + \cdots  + x, z}\right)  = {p\psi }\left( {x, z}\right) \) d’après \( \left( {* * }\right) \) . Or \( \psi \left( {0, z}\right)  = 0 = \; \psi \left( {x - x, z}\right)  = \psi \left( {x, z}\right)  + \psi \left( {-x, z}\right) \) , donc \( \psi \left( {-x, z}\right)  =  - \psi \left( {x, z}\right) \) . Finalement, pour tout \( p \in  \mathbb{Z} \) , \( \psi \left( {{px}, z}\right)  = {p\psi }\left( {x, z}\right) . \)

> - If \( p \in  {\mathbb{N}}^{ * } \) , then \( \psi \left( {{px}, z}\right)  = \psi \left( {x + \cdots  + x, z}\right)  = {p\psi }\left( {x, z}\right) \) according to \( \left( {* * }\right) \) . However \( \psi \left( {0, z}\right)  = 0 = \; \psi \left( {x - x, z}\right)  = \psi \left( {x, z}\right)  + \psi \left( {-x, z}\right) \) , therefore \( \psi \left( {-x, z}\right)  =  - \psi \left( {x, z}\right) \) . Finally, for all \( p \in  \mathbb{Z} \) , \( \psi \left( {{px}, z}\right)  = {p\psi }\left( {x, z}\right) . \)

- Soit \( q \in  {\mathbb{N}}^{ * } \) . Alors

> - Let \( q \in  {\mathbb{N}}^{ * } \) . Then

\[
\psi \left( {x, z}\right)  = \psi \left( {q \cdot  \frac{1}{q}x, z}\right)  = {q\psi }\left( {\frac{1}{q}x, z}\right) \;\text{ donc }\;\psi \left( {\frac{1}{q}x, z}\right)  = \frac{1}{q}\psi \left( {x, z}\right) .
\]

- Pour tout \( r \in  \mathbb{Q}, r = \frac{p}{q} \) , on a

> - For all \( r \in  \mathbb{Q}, r = \frac{p}{q} \) , we have

\[
\psi \left( {{rx}, z}\right)  = \psi \left( {p \cdot  \frac{1}{q}x, z}\right)  = {p\psi }\left( {\frac{1}{q}x, z}\right)  = p\frac{1}{q}\psi \left( {x, z}\right)  = {r\psi }\left( {x, z}\right) .
\]

(***)

> Par construction, \( \psi \) est continue, et comme \( \mathbb{Q} \) est dense dans \( \mathbb{R},\left( {* * * }\right) \) entraîne

By construction, \( \psi \) is continuous, and since \( \mathbb{Q} \) is dense in \( \mathbb{R},\left( {* * * }\right) \) implies

\[
\forall \lambda  \in  \mathbb{R},\;\psi \left( {{\lambda x}, z}\right)  = {\lambda \psi }\left( {x, z}\right) .
\]

(****)

> Les relations (**) et (****) assurent la bilinéarité de \( \psi \) . Comme \( \psi \) est symétrique et définie positive (on a \( \psi \left( {x, x}\right) = 4\parallel x{\parallel }^{2} \) ), \( \psi \) définit bien un produit scalaire. Il en est donc de même de \( \varphi = \frac{1}{4}\psi \) , et comme \( \parallel x{\parallel }^{2} = \varphi \left( {x, x}\right) ,\parallel \cdot \parallel \) est bien une norme euclidienne.

The relations (**) and (****) ensure the bilinearity of \( \psi \). Since \( \psi \) is symmetric and positive definite (we have \( \psi \left( {x, x}\right) = 4\parallel x{\parallel }^{2} \)), \( \psi \) indeed defines an inner product. The same is therefore true for \( \varphi = \frac{1}{4}\psi \), and as \( \parallel x{\parallel }^{2} = \varphi \left( {x, x}\right) ,\parallel \cdot \parallel \) is indeed a Euclidean norm.

> EXERCICE 10. Soit \( A \) et \( B \) deux matrices symétriques de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . On note \( {a}_{1} \geq \ldots \geq {a}_{n} \) les valeurs propres de \( A,{b}_{1} \geq \ldots \geq {b}_{n} \) celles de \( B \) , et \( {c}_{1} \geq \ldots \geq {c}_{n} \) celles de la matrice \( C = A + B \) . Montrer que pour tout \( k \) , on a \( {c}_{k} \geq {a}_{k} + {b}_{n} \) .

EXERCISE 10. Let \( A \) and \( B \) be two symmetric matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). We denote \( {a}_{1} \geq \ldots \geq {a}_{n} \) the eigenvalues of \( A,{b}_{1} \geq \ldots \geq {b}_{n} \), those of \( B \), and \( {c}_{1} \geq \ldots \geq {c}_{n} \) those of the matrix \( C = A + B \). Show that for all \( k \), we have \( {c}_{k} \geq {a}_{k} + {b}_{n} \).

> Solution. Quitte à remplacer la matrice \( B \) par \( B - {b}_{n}{I}_{n} \) , on peut supposer \( {b}_{n} = 0 \) . Il s’agit donc de montrer \( {c}_{k} \geq {a}_{k} \) . Comme toutes les valeurs propres de \( B \) sont positives, \( B \) est une matrice positive.

Solution. By replacing matrix \( B \) with \( B - {b}_{n}{I}_{n} \), we can assume \( {b}_{n} = 0 \). It is therefore a matter of showing \( {c}_{k} \geq {a}_{k} \). Since all eigenvalues of \( B \) are positive, \( B \) is a positive matrix.

> En notant \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) une base orthonormée de vecteurs propres de \( A \) associés aux valeurs propres \( {a}_{1} \geq \ldots \geq {a}_{n} \) , on a

By denoting \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) as an orthonormal basis of eigenvectors of \( A \) associated with the eigenvalues \( {a}_{1} \geq \ldots \geq {a}_{n} \), we have

\[
\forall X \in  \operatorname{Vect}\left( {{E}_{1},\ldots ,{E}_{k}}\right) ,\;{}^{\mathrm{t}}X\left( {A + B}\right) X = {}^{\mathrm{t}}{XAX} + {}^{\mathrm{t}}{XBX} \geq  {}^{\mathrm{t}}{XAX} \geq  {a}_{k}\parallel X{\parallel }^{2}
\]

(*)

> car si \( X = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}{E}_{i} \) , on a \( {}^{\mathrm{t}}{XAX} = \mathop{\sum }\limits_{{i = 1}}^{k}{a}_{i}{\lambda }_{i}^{2} \geq {a}_{k}\mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}^{2} = {a}_{k}\parallel X{\parallel }^{2} \) . Si \( \left( {{F}_{1},\ldots ,{F}_{n}}\right) \) désigne une base orthonormée de vecteurs propres de \( C \) associés aux valeurs propres \( {c}_{1} \geq \ldots \geq {c}_{n} \) , on obtient de manière similaire l'inégalité

because if \( X = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}{E}_{i} \), we have \( {}^{\mathrm{t}}{XAX} = \mathop{\sum }\limits_{{i = 1}}^{k}{a}_{i}{\lambda }_{i}^{2} \geq {a}_{k}\mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}^{2} = {a}_{k}\parallel X{\parallel }^{2} \). If \( \left( {{F}_{1},\ldots ,{F}_{n}}\right) \) denotes an orthonormal basis of eigenvectors of \( C \) associated with the eigenvalues \( {c}_{1} \geq \ldots \geq {c}_{n} \), we similarly obtain the inequality

\[
\forall X \in  \operatorname{Vect}\left( {{F}_{k},\ldots ,{F}_{n}}\right) ,\;{}^{\mathrm{t}}{XCX} \leq  {c}_{k}\parallel X{\parallel }^{2}.
\]

\( \left( {* * }\right) \)

> Comme dim \( \operatorname{Vect}\left( {{E}_{1},\ldots ,{E}_{k}}\right) + \dim \operatorname{Vect}\left( {{F}_{k},\ldots ,{F}_{n}}\right) = k + \left( {n - k + 1}\right) = n + 1 \) , les deux sous-espaces vectoriels \( \operatorname{Vect}\left( {{E}_{1},\ldots ,{E}_{k}}\right) \) et \( \operatorname{Vect}\left( {{F}_{k},\ldots ,{F}_{n}}\right) \) ont une intersection non réduite à \( \{ 0\} \) , donc il existe un vecteur \( X \) non nul appartenant à ces deux sous-espaces. Pour ce vecteur \( X \) , les inégalités (*) et (**) entraînent \( {a}_{k}\parallel X{\parallel }^{2} \leq {}^{\mathrm{t}}X\left( {A + B}\right) X = {}^{\mathrm{t}}{XCX} \leq {c}_{k}\parallel X{\parallel }^{2} \) , donc \( {a}_{k} \leq {c}_{k} \) .

Since dim \( \operatorname{Vect}\left( {{E}_{1},\ldots ,{E}_{k}}\right) + \dim \operatorname{Vect}\left( {{F}_{k},\ldots ,{F}_{n}}\right) = k + \left( {n - k + 1}\right) = n + 1 \) , the two vector subspaces \( \operatorname{Vect}\left( {{E}_{1},\ldots ,{E}_{k}}\right) \) and \( \operatorname{Vect}\left( {{F}_{k},\ldots ,{F}_{n}}\right) \) have an intersection not reduced to \( \{ 0\} \) , so there exists a non-zero vector \( X \) belonging to these two subspaces. For this vector \( X \) , the inequalities (*) and (**) imply \( {a}_{k}\parallel X{\parallel }^{2} \leq {}^{\mathrm{t}}X\left( {A + B}\right) X = {}^{\mathrm{t}}{XCX} \leq {c}_{k}\parallel X{\parallel }^{2} \) , therefore \( {a}_{k} \leq {c}_{k} \) .

> \( \rightarrow \) EXERCICE 11 (PROJECTION ORTHOGONALE DANS UN ESPACE PRÉHILBERTIEN RÉEL). Soit \( E \) un espace préhilbertien réel et \( F \) un s.e.v de \( E \) .

\( \rightarrow \) EXERCISE 11 (ORTHOGONAL PROJECTION IN A REAL PRE-HILBERTIAN SPACE). Let \( E \) be a real pre-Hilbert space and \( F \) a subspace of \( E \) .

> 1/ Pour tout \( x \in E \) , on note

1/ For any \( x \in E \) , we denote

\[
{F}_{x} = \{ y \in  F \mid  \parallel x - y\parallel  = d\left( {x, F}\right)  = \mathop{\inf }\limits_{{z \in  F}}\parallel x - z\parallel \} .
\]

a) Montrer que \( y \in {F}_{x} \) si et seulement si \( x - y \in {F}^{ \bot } \) .

> a) Show that \( y \in {F}_{x} \) if and only if \( x - y \in {F}^{ \bot } \) .

b) Montrer que \( {F}_{x} \) a au plus un élément.

> b) Show that \( {F}_{x} \) has at most one element.

2/ On suppose ici que \( F \) est complet.

> 2/ We assume here that \( F \) is complete.

a) Pour tout \( x \in E \) , montrer que \( {F}_{x} \) a exactement un élément. On le note \( {x}_{F} \) .

> a) For any \( x \in E \) , show that \( {F}_{x} \) has exactly one element. We denote it \( {x}_{F} \) .

b) Montrer que \( E = F \oplus {F}^{ \bot } \) et que \( x \mapsto {P}_{F}\left( x\right) = {x}_{F} \) s’identifie à la projection orthogonale sur \( F \) .

> b) Show that \( E = F \oplus {F}^{ \bot } \) and that \( x \mapsto {P}_{F}\left( x\right) = {x}_{F} \) is identified with the orthogonal projection onto \( F \) .

c) Montrer que \( F = {F}^{ \bot \bot } \) .

> c) Show that \( F = {F}^{ \bot \bot } \) .

3 / On considère ici \( E = \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \) (fonctions à valeurs réelles continues sur \( \left\lbrack {0,1}\right\rbrack \) ), muni du produit scalaire

> 3 / We consider here \( E = \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \) (continuous real-valued functions on \( \left\lbrack {0,1}\right\rbrack \) ), equipped with the inner product

\[
\left( {f \mid  g}\right)  = {\int }_{0}^{1}f\left( t\right) g\left( t\right) {dt}
\]

Soit \( F = \{ f \in E \mid f\left( 0\right) = 0\} \) . Que représente \( {F}^{ \bot } \) ? Conclure.

> Let \( F = \{ f \in E \mid f\left( 0\right) = 0\} \) . What does \( {F}^{ \bot } \) represent? Conclude.

Solution. 1/ a) Condition nécessaire. Soit \( y \in {F}_{x} \) . Posons \( z = x - y \) et considérons \( w \in F \) . Pour tout \( \rho \in \mathbb{R} \) , on a \( \parallel z + {\rho w}\parallel \geq \parallel z\parallel \operatorname{car}z + {\rho w} = x - \left( {y - {\rho w}}\right) \) et \( y - {\rho w} \in F \) . On réécrit ceci en

> Solution. 1/ a) Necessary condition. Let \( y \in {F}_{x} \) . Let \( z = x - y \) and consider \( w \in F \) . For any \( \rho \in \mathbb{R} \) , we have \( \parallel z + {\rho w}\parallel \geq \parallel z\parallel \operatorname{car}z + {\rho w} = x - \left( {y - {\rho w}}\right) \) and \( y - {\rho w} \in F \) . We rewrite this as

\[
\forall \rho  \in  \mathbb{R},\;\parallel z + {\rho w}{\parallel }^{2} = \parallel z{\parallel }^{2} + {2\rho }\left( {z \cdot  w}\right)  + {\rho }^{2}\parallel w{\parallel }^{2} \geq  \parallel z{\parallel }^{2}.
\]

Cette inégalité exprime que la fonction \( \rho \mapsto \parallel z{\parallel }^{2} + {2\rho }\left( {z \cdot w}\right) + {\rho }^{2}\parallel w{\parallel }^{2} \) atteint son minimum en \( \rho = 0 \) , donc sa dérivée par rapport à \( \rho \) en 0 est nulle, ce qui s’écrit \( z \cdot w = 0 \) . Ceci étant vrai pour tout \( w \in F \) , on en déduit que \( z = x - y \in {F}^{ \bot } \) .

> This inequality expresses that the function \( \rho \mapsto \parallel z{\parallel }^{2} + {2\rho }\left( {z \cdot w}\right) + {\rho }^{2}\parallel w{\parallel }^{2} \) reaches its minimum at \( \rho = 0 \) , so its derivative with respect to \( \rho \) at 0 is zero, which is written \( z \cdot w = 0 \) . Since this is true for any \( w \in F \) , we deduce that \( z = x - y \in {F}^{ \bot } \) .

Condition suffisante. Soit \( y \in F \) tel que \( x - y \in {F}^{ \bot } \) . On a

> Sufficient condition. Let \( y \in F \) be such that \( x - y \in {F}^{ \bot } \) . We have

\[
\forall z \in  F,\;\parallel x - z{\parallel }^{2} = \parallel \left( {x - y}\right)  + \left( {y - z}\right) {\parallel }^{2} = \parallel x - y{\parallel }^{2} + \parallel z - y{\parallel }^{2}
\]

(*)

> (car \( x - y \in {F}^{ \bot } \) et \( z - y \in F \) ). La relation (*) entraîne \( \parallel x - y\parallel = \mathop{\inf }\limits_{{z \in F}}\parallel x - z\parallel \) , donc \( y \in {F}_{x} \) .

(since \( x - y \in {F}^{ \bot } \) and \( z - y \in F \) ). The relation (*) implies \( \parallel x - y\parallel = \mathop{\inf }\limits_{{z \in F}}\parallel x - z\parallel \) , therefore \( y \in {F}_{x} \) .

> b) Supposons que \( {F}_{x} \) ait deux éléments \( y \) et \( z \) . Alors \( x - y \) et \( x - z \in {F}^{ \bot } \) d’après a), et donc \( y - z = \left( {x - z}\right) - \left( {x - y}\right) \in {F}^{ \bot } \) . Or \( y - z \in F \) . Comme \( F \cap {F}^{ \bot } = \{ 0\} \) , on en déduit \( y - z = 0 \) , d'où le résultat.

b) Suppose \( {F}_{x} \) has two elements \( y \) and \( z \) . Then \( x - y \) and \( x - z \in {F}^{ \bot } \) according to a), and therefore \( y - z = \left( {x - z}\right) - \left( {x - y}\right) \in {F}^{ \bot } \) . However \( y - z \in F \) . Since \( F \cap {F}^{ \bot } = \{ 0\} \) , we deduce \( y - z = 0 \) , hence the result.

> 2/a) L'idée est d'utiliser le fait que \( F \) soit complet. Nous allons construire une suite de Cauchy, et montrer que sa limite vérifie la condition requise.

2/a) The idea is to use the fact that \( F \) is complete. We will construct a Cauchy sequence and show that its limit satisfies the required condition.

> Soit \( \delta = \mathop{\inf }\limits_{{z \in F}}\parallel x - z\parallel \) . Par définition de \( \delta \) , il existe une suite \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) de points de \( F \) telle que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) , et donc \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\begin{Vmatrix}x - {y}_{n}\end{Vmatrix}}^{2} = {\delta }^{2} \) .

Let \( \delta = \mathop{\inf }\limits_{{z \in F}}\parallel x - z\parallel \) . By definition of \( \delta \) , there exists a sequence \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) of points in \( F \) such that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) , and therefore \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\begin{Vmatrix}x - {y}_{n}\end{Vmatrix}}^{2} = {\delta }^{2} \) .

> Dans un e.v.n général, cette relation n’entraîne pas la convergence de \( \left( {y}_{n}\right) \) . C’est le caractère préhilbertien de \( E \) qui va nous permettre de montrer qu’elle converge (comme le montre un dessin). Nous allons pour cela montrer que \( \left( {y}_{n}\right) \) est une suite de Cauchy. La clé est d'utiliser le théorème de la médiane (voir le théorème 1 page 253), qui entraîne

In a general n.v.s., this relation does not imply the convergence of \( \left( {y}_{n}\right) \) . It is the pre-Hilbertian nature of \( E \) that will allow us to show that it converges (as shown in a drawing). To do this, we will show that \( \left( {y}_{n}\right) \) is a Cauchy sequence. The key is to use the parallelogram law (see theorem 1 page 253), which implies

\[
\forall p, q \in  \mathbb{N},\;{\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} + {\begin{Vmatrix}\left( x - {y}_{p}\right)  + \left( x - {y}_{q}\right) \end{Vmatrix}}^{2} = 2{\begin{Vmatrix}x - {y}_{p}\end{Vmatrix}}^{2} + 2{\begin{Vmatrix}x - {y}_{q}\end{Vmatrix}}^{2},
\]

donc

> therefore

\[
{\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} = 2{\begin{Vmatrix}x - {y}_{p}\end{Vmatrix}}^{2} + 2{\begin{Vmatrix}x - {y}_{q}\end{Vmatrix}}^{2} - 4{\begin{Vmatrix}x - \frac{{y}_{p} + {y}_{q}}{2}\end{Vmatrix}}^{2}.
\]

Soit \( \varepsilon > 0 \) . Il existe \( N \in \mathbb{N} \) tel que pour tout \( n \geq N,{\begin{Vmatrix}x - {y}_{n}\end{Vmatrix}}^{2} \leq {\delta }^{2} + \varepsilon \) , donc

> Let \( \varepsilon > 0 \) . There exists \( N \in \mathbb{N} \) such that for all \( n \geq N,{\begin{Vmatrix}x - {y}_{n}\end{Vmatrix}}^{2} \leq {\delta }^{2} + \varepsilon \) , therefore

\[
\forall p, q \geq  N,\;{\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} \leq  2\left( {{\delta }^{2} + \varepsilon }\right)  + 2\left( {{\delta }^{2} + \varepsilon }\right)  - 4{\begin{Vmatrix}x - \frac{{y}_{p} + {y}_{q}}{2}\end{Vmatrix}}^{2}.
\]

Or \( \frac{{y}_{p} + {y}_{q}}{2} \in F \) , donc \( \begin{Vmatrix}{x - \frac{{y}_{p} + {y}_{q}}{2}}\end{Vmatrix} \geq \delta \) , d’où

> However \( \frac{{y}_{p} + {y}_{q}}{2} \in F \) , therefore \( \begin{Vmatrix}{x - \frac{{y}_{p} + {y}_{q}}{2}}\end{Vmatrix} \geq \delta \) , hence

\[
\forall p, q \geq  N,\;{\begin{Vmatrix}{y}_{p} - {y}_{q}\end{Vmatrix}}^{2} \leq  2\left( {{\delta }^{2} + \varepsilon }\right)  + 2\left( {{\delta }^{2} + \varepsilon }\right)  - 4{\delta }^{2} = {4\varepsilon }.
\]

Ceci suffit à prouver que \( \left( {y}_{n}\right) \) est une suite de Cauchy. Comme \( F \) est complet, cette suite converge vers une valeur \( y \in F \) . La continuité de la norme assure le fait que \( \parallel x - y\parallel = \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) , donc \( y \in {F}_{x} \) . L’ensemble \( {F}_{x} \) est donc non vide, et a donc un seul élément d’après \( 1/ \) b).

> This is sufficient to prove that \( \left( {y}_{n}\right) \) is a Cauchy sequence. Since \( F \) is complete, this sequence converges to a value \( y \in F \) . The continuity of the norm ensures that \( \parallel x - y\parallel = \mathop{\lim }\limits_{{n \rightarrow \infty }}\begin{Vmatrix}{x - {y}_{n}}\end{Vmatrix} = \delta \) , therefore \( y \in {F}_{x} \) . The set \( {F}_{x} \) is therefore non-empty, and thus has a single element according to \( 1/ \) b).

b) On sait que \( F \cap {F}^{ \bot } = \{ 0\} \) . Il reste à montrer \( E = F + {F}^{ \bot } \) , ce qui découle du fait que pour tout \( x \in E, x = {x}_{F} + \left( {x - {x}_{F}}\right) \) avec \( {x}_{F} \in {F}_{x} \subset F \) et \( x - {x}_{F} \in {F}^{ \bot } \) d’après \( 1/ \) a).

> b) We know that \( F \cap {F}^{ \bot } = \{ 0\} \) . It remains to show \( E = F + {F}^{ \bot } \) , which follows from the fact that for all \( x \in E, x = {x}_{F} + \left( {x - {x}_{F}}\right) \) with \( {x}_{F} \in {F}_{x} \subset F \) and \( x - {x}_{F} \in {F}^{ \bot } \) according to \( 1/ \) a).

Pour tout \( x \in E \) , la décomposition de \( x \) selon \( F \oplus {F}^{ \bot } \) est \( x = {x}_{F} + \left( {x - {x}_{F}}\right) \) , ce qui prouve que \( x \mapsto {x}_{F} \) est la projection orthogonale sur \( F \) .

> For all \( x \in E \) , the decomposition of \( x \) according to \( F \oplus {F}^{ \bot } \) is \( x = {x}_{F} + \left( {x - {x}_{F}}\right) \) , which proves that \( x \mapsto {x}_{F} \) is the orthogonal projection onto \( F \) .

c) On sait que \( F \subset {F}^{ \bot \bot } \) . Il reste à montrer \( {F}^{ \bot \bot } \subset F \) . Soit \( x \in {F}^{ \bot \bot } \) . Comme \( F \oplus {F}^{ \bot } = E \) , il existe \( \left( {y, z}\right) \in F \times {F}^{ \bot } \) tels que \( x = y + z \) . Or \( z \in {F}^{ \bot } \) donc \( 0 = x \cdot z = y \cdot z + \parallel z{\parallel }^{2} = \parallel z{\parallel }^{2} \) , donc \( z = 0 \) , donc \( x = y \in F \) . Finalement, on a montré \( F = {F}^{ \bot \bot } \) .

> c) We know that \( F \subset {F}^{ \bot \bot } \) . It remains to show \( {F}^{ \bot \bot } \subset F \) . Let \( x \in {F}^{ \bot \bot } \) . Since \( F \oplus {F}^{ \bot } = E \) , there exist \( \left( {y, z}\right) \in F \times {F}^{ \bot } \) such that \( x = y + z \) . However, \( z \in {F}^{ \bot } \) so \( 0 = x \cdot z = y \cdot z + \parallel z{\parallel }^{2} = \parallel z{\parallel }^{2} \) , so \( z = 0 \) , so \( x = y \in F \) . Finally, we have shown \( F = {F}^{ \bot \bot } \) .

3 / Nous allons montrer que \( {F}^{ \bot } = \{ 0\} \) . Soit \( f \in {F}^{ \bot } \) . Soit \( g : x \mapsto {xf}\left( x\right) \) . On a \( g \in F \) , donc

> 3 / We will show that \( {F}^{ \bot } = \{ 0\} \) . Let \( f \in {F}^{ \bot } \) . Let \( g : x \mapsto {xf}\left( x\right) \) . We have \( g \in F \) , therefore

\[
\left( {f \mid  g}\right)  = {\int }_{0}^{1}x{f}^{2}\left( x\right) {dx} = 0.
\]

Comme \( x \mapsto x{f}^{2}\left( x\right) \) est continue et positive, ceci entraîne que pour tout \( x \in \left\lbrack {0,1}\right\rbrack , x{f}^{2}\left( x\right) = 0 \) , donc pour tout \( x \in \rbrack 0,1\rbrack , f\left( x\right) = 0 \) , donc \( f = 0 \) car \( f \) est continue.

> Since \( x \mapsto x{f}^{2}\left( x\right) \) is continuous and positive, this implies that for all \( x \in \left\lbrack {0,1}\right\rbrack , x{f}^{2}\left( x\right) = 0 \) , therefore for all \( x \in \rbrack 0,1\rbrack , f\left( x\right) = 0 \) , therefore \( f = 0 \) because \( f \) is continuous.

On a donc \( F \oplus {F}^{ \bot } \neq E \) , ce qui montre que le résultat \( 2/ \) b) est faux lorsque \( F \) n’est pas supposé complet.

> We therefore have \( F \oplus {F}^{ \bot } \neq E \) , which shows that the result \( 2/ \) b) is false when \( F \) is not assumed to be complete.

Remarque. Ces résultats font des espaces hilbertiens (espaces préhilbertiens complets) des espaces vectoriels très maniables, même en dimension infinie. Une étude plus approfondie de ces espaces fait l'objet d'une annexe dans le tome d'analyse.

> Remark. These results make Hilbert spaces (complete pre-Hilbert spaces) very manageable vector spaces, even in infinite dimension. A more in-depth study of these spaces is the subject of an appendix in the analysis volume.

EXERCICE 12 (PRODUIT DE SCHUR DE DEUX MATRICES). Soient \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) et \( B = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) deux matrices symétriques. Le produit de Schur de \( A \) et \( B \) est défini par la matrice symétrique \( A \circ B = {\left( {a}_{i, j}{b}_{i, j}\right) }_{1 \leq i, j \leq n} \) .

> EXERCISE 12 (SCHUR PRODUCT OF TWO MATRICES). Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) and \( B = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be two symmetric matrices. The Schur product of \( A \) and \( B \) is defined by the symmetric matrix \( A \circ B = {\left( {a}_{i, j}{b}_{i, j}\right) }_{1 \leq i, j \leq n} \) .

a) Si \( A \) et \( B \) sont positives, montrer que la matrice \( A \circ B \) est positive.

> a) If \( A \) and \( B \) are positive, show that the matrix \( A \circ B \) is positive.

b) Si de plus \( A \) et \( B \) sont définies, montrer que \( A \circ B \) est définie.

> b) If, in addition, \( A \) and \( B \) are definite, show that \( A \circ B \) is definite.

c) Si \( A \) est positive, montrer que la matrice \( E = {\left( {e}^{{a}_{i, j}}\right) }_{1 \leq i, j \leq n} \) est positive, et qu’elle est définie si \( A \) est définie.

> c) If \( A \) is positive, show that the matrix \( E = {\left( {e}^{{a}_{i, j}}\right) }_{1 \leq i, j \leq n} \) is positive, and that it is definite if \( A \) is definite.

Solution. a) On montre d’abord le résultat lorsque \( \operatorname{rg}A = \operatorname{rg}B = 1 \) . La signature des formes quadratiques \( X \mapsto {X}^{ * }{AX} \) et \( X \mapsto {X}^{ * }{BX} \) est \( \left( {1,0}\right) \) , donc il existe deux formes linéaires \( f\left( X\right) = \; \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{x}_{i} \) et \( g\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{x}_{i} \) telles que

> Solution. a) We first show the result when \( \operatorname{rg}A = \operatorname{rg}B = 1 \) . The signature of the quadratic forms \( X \mapsto {X}^{ * }{AX} \) and \( X \mapsto {X}^{ * }{BX} \) is \( \left( {1,0}\right) \) , so there exist two linear forms \( f\left( X\right) = \; \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{x}_{i} \) and \( g\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{x}_{i} \) such that

\[
{X}^{ * }{AX} = {f}^{2}\left( X\right) \;\text{ et }\;{X}^{ * }{BX} = {g}^{2}\left( X\right) .
\]

En développant \( {f}^{2} \) et \( {g}^{2} \) , on s’aperçoit alors que \( A = {\left( {\lambda }_{i}{\lambda }_{j}\right) }_{1 \leq i, j \leq n} \) et \( B = {\left( {\mu }_{i}{\mu }_{j}\right) }_{1 \leq i, j \leq n} \) . Donc \( A \circ B = {\left\lbrack \left( {\lambda }_{i}{\mu }_{i}\right) \left( {\lambda }_{j}{\mu }_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) , donc cette matrice est positive car

> By expanding \( {f}^{2} \) and \( {g}^{2} \) , we then notice that \( A = {\left( {\lambda }_{i}{\lambda }_{j}\right) }_{1 \leq i, j \leq n} \) and \( B = {\left( {\mu }_{i}{\mu }_{j}\right) }_{1 \leq i, j \leq n} \) . Thus \( A \circ B = {\left\lbrack \left( {\lambda }_{i}{\mu }_{i}\right) \left( {\lambda }_{j}{\mu }_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) , so this matrix is positive because

\[
{X}^{ * }\left( {A \circ  B}\right) X = {h}^{2}\left( X\right)  \geq  0\;\text{ avec }\;h\left( X\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\lambda }_{i}{\mu }_{i}}\right) {x}_{i}.
\]

Traitons maintenant le cas général. L’entier \( r \) désignant le rang de \( A \) , on peut écrire

> Let us now treat the general case. Letting the integer \( r \) denote the rank of \( A \) , we can write

\[
{X}^{ * }{AX} = \mathop{\sum }\limits_{{i = 1}}^{r}{f}_{i}{\left( X\right) }^{2}
\]

où \( {f}_{1},\ldots ,{f}_{r} \) sont des formes linéaires indépendantes (ceci parce que la signature de \( A \) est \( \left( {r,0}\right) \) ). Pour tout \( i,1 \leq i \leq r \) , notons \( {A}_{i} \) la matrice de la forme quadratique \( {f}_{i}^{2} \) , de sorte que \( {X}^{ * }{A}_{i}X = \; {f}_{i}^{2}\left( X\right) \) . Les matrices \( {A}_{i} \) sont symétriques positives et de rang 1 (leur signature est \( \left( {1,0}\right) \) ) et \( A = \mathop{\sum }\limits_{{i = 1}}^{r}{A}_{i} \) . On écrirait de même \( B \) sous la forme \( B = \mathop{\sum }\limits_{{j = 1}}^{s}{B}_{j} \) où \( s = \operatorname{rg}B \) et où les \( {B}_{j} \) sont des matrices symétriques positives de rang 1 . Donc \( A \circ B = \mathop{\sum }\limits_{{i, j}}{A}_{i} \circ {B}_{j} \) , somme de matrices positives, est positive.

> where \( {f}_{1},\ldots ,{f}_{r} \) are independent linear forms (this is because the signature of \( A \) is \( \left( {r,0}\right) \) ). For any \( i,1 \leq i \leq r \) , let \( {A}_{i} \) denote the matrix of the quadratic form \( {f}_{i}^{2} \) , such that \( {X}^{ * }{A}_{i}X = \; {f}_{i}^{2}\left( X\right) \) . The matrices \( {A}_{i} \) are symmetric positive and of rank 1 (their signature is \( \left( {1,0}\right) \) ) and \( A = \mathop{\sum }\limits_{{i = 1}}^{r}{A}_{i} \) . We would similarly write \( B \) in the form \( B = \mathop{\sum }\limits_{{j = 1}}^{s}{B}_{j} \) where \( s = \operatorname{rg}B \) and where the \( {B}_{j} \) are symmetric positive matrices of rank 1. Thus \( A \circ B = \mathop{\sum }\limits_{{i, j}}{A}_{i} \circ {B}_{j} \) , as a sum of positive matrices, is positive.

b) Les matrices \( A \) et \( B \) étant définies positives, on peut écrire

> b) Since the matrices \( A \) and \( B \) are positive definite, we can write

\[
{X}^{ * }{AX} = \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{i}^{2}\left( X\right) \;\text{ et }\;{X}^{ * }{BX} = \mathop{\sum }\limits_{{j = 1}}^{n}{g}_{j}^{2}\left( X\right) ,
\]

où les formes linéaires \( {\left( {f}_{i}\right) }_{1 \leq i \leq n} \) sont linéairement indépendantes, ainsi que les \( {\left( {g}_{j}\right) }_{1 \leq j \leq n} \) . Notons \( {\left( {\lambda }_{k, i}\right) }_{i} \) les coefficients de \( {f}_{k},{\left( {\mu }_{\ell , j}\right) }_{j} \) ceux de \( {g}_{\ell } \) , de sorte que

> where the linear forms \( {\left( {f}_{i}\right) }_{1 \leq i \leq n} \) are linearly independent, as are the \( {\left( {g}_{j}\right) }_{1 \leq j \leq n} \) . Let \( {\left( {\lambda }_{k, i}\right) }_{i} \) be the coefficients of \( {f}_{k},{\left( {\mu }_{\ell , j}\right) }_{j} \) and those of \( {g}_{\ell } \) , such that

\[
{f}_{k}\left( X\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{k, i}{x}_{i}\;\text{ et }\;{g}_{\ell }\left( X\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}{\mu }_{\ell , j}{x}_{j}.
\]

Les matrices des formes quadratiques \( {f}_{k}^{2} \) et \( {g}_{\ell }^{2} \) sont \( {A}_{k} = {\left( {\lambda }_{k, i}{\lambda }_{k, j}\right) }_{i, j} \) et \( {B}_{\ell } = {\left( {\mu }_{\ell , i}{\mu }_{\ell , j}\right) }_{i, j} \) , et on a \( A = \mathop{\sum }\limits_{{k = 1}}^{n}{A}_{k} \) et \( B = \mathop{\sum }\limits_{{\ell = 1}}^{n}{B}_{\ell } \) . Ainsi, \( A \circ B = \mathop{\sum }\limits_{{k,\ell }}{A}_{k} \circ {B}_{\ell } \) . Maintenant, l’égalité \( {X}^{ * }\left( {A \circ B}\right) X = 0 \) entraîne \( \mathop{\sum }\limits_{{k,\ell }}{X}^{ * }\left( {{A}_{k} \circ {B}_{\ell }}\right) X = 0 \) , et les matrices \( {A}_{k} \circ {B}_{\ell } \) étant positives,

> The matrices of the quadratic forms \( {f}_{k}^{2} \) and \( {g}_{\ell }^{2} \) are \( {A}_{k} = {\left( {\lambda }_{k, i}{\lambda }_{k, j}\right) }_{i, j} \) and \( {B}_{\ell } = {\left( {\mu }_{\ell , i}{\mu }_{\ell , j}\right) }_{i, j} \), and we have \( A = \mathop{\sum }\limits_{{k = 1}}^{n}{A}_{k} \) and \( B = \mathop{\sum }\limits_{{\ell = 1}}^{n}{B}_{\ell } \). Thus, \( A \circ B = \mathop{\sum }\limits_{{k,\ell }}{A}_{k} \circ {B}_{\ell } \). Now, the equality \( {X}^{ * }\left( {A \circ B}\right) X = 0 \) implies \( \mathop{\sum }\limits_{{k,\ell }}{X}^{ * }\left( {{A}_{k} \circ {B}_{\ell }}\right) X = 0 \), and since the matrices \( {A}_{k} \circ {B}_{\ell } \) are positive,

\[
\forall k,\ell ,\;{X}^{ * }\left( {{A}_{k} \circ  {B}_{\ell }}\right) X = 0 = {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{k, i}{\mu }_{\ell , i}{x}_{i}\right) }^{2}.
\]

(*)

> Fixons \( \ell \) . L’égalité (*) entraîne

Let us fix \( \ell \). The equality (*) implies

\[
\forall k,\;\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{k, i}\left( {{\mu }_{\ell , i}{x}_{i}}\right)  = 0\;\text{ ou encore }\;{f}_{k}\left( {Y}_{\ell }\right)  = 0\;\text{ avec }\;{Y}_{\ell } = \left( \begin{matrix} {\mu }_{\ell ,1}{x}_{1} \\  \vdots \\  {\mu }_{\ell , n}{x}_{n} \end{matrix}\right) .
\]

Les \( n \) formes linéaires \( {\left( {f}_{k}\right) }_{1 \leq k \leq n} \) étant linéairement indépendantes, ceci entraîne \( {Y}_{\ell } = 0 \) , donc \( {\mu }_{\ell , i}{x}_{i} = 0 \) pour tout \( i \) , et par sommation \( {g}_{\ell }\left( X\right) = 0 \) . Ceci étant vrai pour tout \( \ell \) , comme les formes linéaires \( {\left( {g}_{\ell }\right) }_{1 \leq \ell \leq n} \) sont linéairement indépendantes, on a nécessairement \( X = 0 \) , ce qui prouve que \( A \circ B \) est définie.

> Since the \( n \) linear forms \( {\left( {f}_{k}\right) }_{1 \leq k \leq n} \) are linearly independent, this implies \( {Y}_{\ell } = 0 \), therefore \( {\mu }_{\ell , i}{x}_{i} = 0 \) for all \( i \), and by summation \( {g}_{\ell }\left( X\right) = 0 \). Since this is true for all \( \ell \), and as the linear forms \( {\left( {g}_{\ell }\right) }_{1 \leq \ell \leq n} \) are linearly independent, we necessarily have \( X = 0 \), which proves that \( A \circ B \) is definite.

c) En utilisant le résultat de la question a), on a facilement par récurrence sur \( m \in \mathbb{N} \) que la matrice \( {A}_{m} = {\left( {a}_{i, j}^{m}\right) }_{1 \leq i, j \leq n} \) est positive. Maintenant, pour tout entier \( M \) positif, on a

> c) Using the result from question a), we easily have by induction on \( m \in \mathbb{N} \) that the matrix \( {A}_{m} = {\left( {a}_{i, j}^{m}\right) }_{1 \leq i, j \leq n} \) is positive. Now, for any positive integer \( M \), we have

\[
\forall X \in  {\mathbb{R}}^{n},\;{X}^{ * }\left( {\mathop{\sum }\limits_{{m = 0}}^{M}\frac{1}{m!}{A}_{m}}\right) X = \mathop{\sum }\limits_{{m = 0}}^{M}\frac{1}{m!}{X}^{ * }{A}_{m}X \geq  0.
\]

En passant à la limite lorsque \( M \) tend vers l’infini, on obtient \( {X}^{ * }{EX} \geq 0 \) , et ceci pour tout \( X \) , ce qui prouve que \( E \) est positive.

> By taking the limit as \( M \) tends to infinity, we obtain \( {X}^{ * }{EX} \geq 0 \), and this for all \( X \), which proves that \( E \) is positive.

Si de plus \( A \) est définie, alors \( E \) est définie car

> If, in addition, \( A \) is definite, then \( E \) is definite because

\[
\forall X \neq  0,\;{X}^{ * }{EX} \geq  {X}^{ * }{AX} > 0.
\]
