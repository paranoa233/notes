#### 3.5. Exercises

*Français : 3.5. Exercices*

EXERCICE 1. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que

> EXERCISE 1. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be such that

\[
\exists c > 0,\forall \left( {i, j}\right) ,\;\left| {a}_{i, j}\right|  \leq  c.
\]

Montrer que \( \left| {\det M}\right| \leq {c}^{n}{n}^{n/2} \) .

> Show that \( \left| {\det M}\right| \leq {c}^{n}{n}^{n/2} \) .

Solution. Il suffit d'utiliser l'inégalité d'Hadamard (qu'il faut, au besoin, savoir redémontrer). No-tons \( {A}_{1},\ldots ,{A}_{n} \) les vecteurs colonnes de \( A \) . D’après le théorème 7, on a let \( M\left| \leq \right| \begin{Vmatrix}{A}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{A}_{n}\end{Vmatrix} \) où pour tout \( j \) ,

> Solution. It suffices to use Hadamard's inequality (which one must know how to re-prove, if necessary). Let \( {A}_{1},\ldots ,{A}_{n} \) be the column vectors of \( A \) . According to Theorem 7, we have let \( M\left| \leq \right| \begin{Vmatrix}{A}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{A}_{n}\end{Vmatrix} \) where for all \( j \) ,

\[
\begin{Vmatrix}{A}_{j}\end{Vmatrix} = \sqrt{{A}_{j}^{ * }{A}_{j}} = \sqrt{\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, j}^{2}} \leq  \sqrt{n{c}^{2}} = \sqrt{n}c.
\]

On en déduit \( \left| {\det M}\right| \leq {\left( \sqrt{n}c\right) }^{n} = {c}^{n}{n}^{n/2} \) .

> We deduce from this \( \left| {\det M}\right| \leq {\left( \sqrt{n}c\right) }^{n} = {c}^{n}{n}^{n/2} \) .

EXERCICE 2. Soit \( E \) un espace euclidien de dimension \( n \in {\mathbb{N}}^{ * } \) .

> EXERCISE 2. Let \( E \) be a Euclidean space of dimension \( n \in {\mathbb{N}}^{ * } \) .

a) On suppose qu’il existe \( n + 1 \) vecteurs \( {u}_{1},\ldots ,{u}_{n + 1} \) de \( E \) de norme 1, vérifiant

> a) Suppose there exist \( n + 1 \) vectors \( {u}_{1},\ldots ,{u}_{n + 1} \) of \( E \) with norm 1, satisfying

\[
\exists \alpha  \in  \mathbb{R},\alpha  \neq  1,\;\text{ tel que }\;\forall i \neq  j,{u}_{i} \cdot  {u}_{j} = \alpha .
\]

Déterminer a. (Indication. On pourra utiliser les matrices de Gram.) b) Démontrer qu'il existe effectivement de tels vecteurs dans \( E \) .

> Determine a. (Hint: You may use Gram matrices.) b) Prove that such vectors indeed exist in \( E \) .

Solution. a) Notons \( M \) la matrice de Gram des vecteurs \( {u}_{1},\ldots ,{u}_{n + 1} \) (voir la partie 3.4). On a

> Solution. a) Let \( M \) be the Gram matrix of the vectors \( {u}_{1},\ldots ,{u}_{n + 1} \) (see section 3.4). We have

\[
M = \left( \begin{matrix} 1 & \alpha & \cdots & \alpha \\  \alpha & 1 &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & \alpha \\  \alpha & \cdots & \alpha & 1 \end{matrix}\right)  \in  {\mathcal{M}}_{n + 1}\left( \mathbb{R}\right) .
\]

(*)

> Par ailleurs, la famille \( \left( {{u}_{1},\ldots ,{u}_{n + 1}}\right) \) est liée \( \left( {n + 1\text{ vecteurs en dimension }n}\right) \) , donc d’après la proposition 3, det \( M = G\left( {{u}_{1},\ldots ,{u}_{n + 1}}\right) = 0 \) .

Furthermore, the family \( \left( {{u}_{1},\ldots ,{u}_{n + 1}}\right) \) is linearly dependent \( \left( {n + 1\text{ vecteurs en dimension }n}\right) \) , so according to Proposition 3, det \( M = G\left( {{u}_{1},\ldots ,{u}_{n + 1}}\right) = 0 \) .

> Calculons det \( M \) . En additionnant les \( n \) premières colonnes à la dernière, on obtient

Let us calculate det \( M \) . By adding the first \( n \) columns to the last one, we obtain

\[
\det M = \left| \begin{matrix} 1 & \alpha & \cdots & 1 + {n\alpha } \\  \alpha &  \ddots  &  \ddots  & \vdots \\  \vdots &  \ddots  & 1 & 1 + {n\alpha } \\  \alpha & \cdots & \alpha & 1 + {n\alpha } \end{matrix}\right|  = \left( {1 + {n\alpha }}\right) \left| \begin{matrix} 1 & \alpha & \cdots & 1 \\  \alpha &  \ddots  &  \ddots  & \vdots \\  \vdots &  \ddots  & 1 & 1 \\  \alpha & \cdots & \alpha & 1 \end{matrix}\right| .
\]

En retranchant ensuite \( \alpha \) fois la dernière colonne aux \( n \) premières, on en déduit

> Then, by subtracting \( \alpha \) times the last column from the first \( n \) columns, we deduce

\[
\det M = {\left( 1 - \alpha \right) }^{n}\left( {1 + {n\alpha }}\right) .
\]

\( \left( {* * }\right) \)

> (Ce résultat peut s'obtenir également à partir du résultat décrit dans le problème 1 page 214 donnant la liste des valeurs propres de \( M \) ).

(This result can also be obtained from the result described in problem 1 on page 214, which gives the list of eigenvalues of \( M \) ).

> Comme det \( M = 0 \) , l’égalité (**) montre \( \alpha = - 1/n \) car \( \alpha \neq 1 \) par hypothèse.

Since det \( M = 0 \) , equality (**) shows \( \alpha = - 1/n \) because \( \alpha \neq 1 \) by hypothesis.

> b) Notons \( M \) la matrice symétrique (*) dans laquelle on choisit \( \alpha = - 1/n \) . D’après le problème 1 page 214, les valeurs propres de \( M \) sont 0 et \( 1 - \alpha = 1 + \frac{1}{n} \) . Elles sont positives, donc \( M \) est une matrice positive. D'après la proposition 3, \( M \) est une matrice de Gram, c'est-à-dire qu'il existe \( n + 1 \) vecteurs \( {U}_{1},\ldots ,{U}_{n + 1} \) de \( {\mathbb{R}}^{n + 1} \) tels que \( M \) soit la matrice de Gram des \( {U}_{i} \) . Ainsi, les vecteurs \( {U}_{i} \) vérifient la condition de a) avec \( \alpha = - \frac{1}{n} \) . Comme det \( M = 0 = G\left( {{U}_{1},\ldots ,{U}_{n + 1}}\right) \) , la famille \( {\left( {U}_{i}\right) }_{1 \leq i \leq n + 1} \) est liée. Ainsi, il existe un s.e.v \( F \) de \( {\mathbb{R}}^{n + 1} \) de dimension \( n \) contenant les \( {U}_{i} \) .

b) Let \( M \) be the symmetric matrix (*) in which we choose \( \alpha = - 1/n \) . According to problem 1 on page 214, the eigenvalues of \( M \) are 0 and \( 1 - \alpha = 1 + \frac{1}{n} \) . They are positive, so \( M \) is a positive matrix. According to Proposition 3, \( M \) is a Gram matrix, meaning there exist \( n + 1 \) vectors \( {U}_{1},\ldots ,{U}_{n + 1} \) of \( {\mathbb{R}}^{n + 1} \) such that \( M \) is the Gram matrix of the \( {U}_{i} \) . Thus, the vectors \( {U}_{i} \) satisfy the condition of a) with \( \alpha = - \frac{1}{n} \) . Since det \( M = 0 = G\left( {{U}_{1},\ldots ,{U}_{n + 1}}\right) \) , the family \( {\left( {U}_{i}\right) }_{1 \leq i \leq n + 1} \) is linearly dependent. Thus, there exists a subspace \( F \) of \( {\mathbb{R}}^{n + 1} \) of dimension \( n \) containing the \( {U}_{i} \) .

> Résumons. Nous avons trouvé un espace euclidien de dimension \( n \) (ici \( F \) ) et \( n + 1 \) vecteurs de cet espace vérifiant la condition de la question a). Par isomorphisme d'espace euclidien, on peut donc trouver \( n + 1 \) vecteurs \( {u}_{1},\ldots ,{u}_{n + 1} \) dans \( E \) vérifiant cette condition.

Let us summarize. We have found a Euclidean space of dimension \( n \) (here \( F \) ) and \( n + 1 \) vectors of this space satisfying the condition of question a). By Euclidean space isomorphism, we can therefore find \( n + 1 \) vectors \( {u}_{1},\ldots ,{u}_{n + 1} \) in \( E \) satisfying this condition.

> EXERCICE 3. Soit \( E \) un espace hermitien et \( u \in \mathcal{L}\left( E\right) \) . Montrer que l’endomorphisme \( u \) est normal si et seulement s’il existe \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) tel que \( {u}^{ * } = P\left( u\right) \) .

EXERCISE 3. Let \( E \) be a Hermitian space and \( u \in \mathcal{L}\left( E\right) \) . Show that the endomorphism \( u \) is normal if and only if there exists \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) such that \( {u}^{ * } = P\left( u\right) \) .

> Solution. Tout polynôme en \( u \) commutant avec \( u \) , la condition suffisante est immédiate. Montrons maintenant la condition nécessaire. Supposons \( u \) normal. D’après le théorème 3, \( u \) se diagonalise dans une base \( B \) orthonormée de \( E \) . Autrement dit, il existe des nombres complexes distincts \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) tels que

Solution. Since any polynomial in \( u \) commutes with \( u \) , the sufficient condition is immediate. Let us now show the necessary condition. Suppose \( u \) is normal. According to Theorem 3, \( u \) is diagonalizable in an orthonormal basis \( B \) of \( E \) . In other words, there exist distinct complex numbers \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) such that

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1}{I}_{{\alpha }_{1}} & & 0 \\   &  \ddots  & \\  0 & & {\lambda }_{r}{I}_{{\alpha }_{r}} \end{matrix}\right) ,
\]

où les \( {\alpha }_{i} \) sont des entiers naturels non nuls. La base \( B \) étant orthonormée, on a

> where the \( {\alpha }_{i} \) are non-zero natural integers. Since the basis \( B \) is orthonormal, we have

\[
{\left\lbrack  {u}^{ * }\right\rbrack  }_{B} = {}^{\mathrm{t}}{\overline{\left\lbrack  u\right\rbrack  }}_{B} = \left( \begin{matrix} \overline{{\lambda }_{1}}{I}_{{\alpha }_{1}} & & 0 \\   &  \ddots  & \\  0 & & \overline{{\lambda }_{r}}{I}_{{\alpha }_{r}} \end{matrix}\right) .
\]

Notons \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) le polynôme de Lagrange (voir la partie 2.4 page 65) tel que \( P\left( {\lambda }_{i}\right) = \overline{{\lambda }_{i}} \) pour tout \( i \) (on peut car les \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq r} \) sont deux à deux distincts). On voit alors que \( P\left( {\left\lbrack u\right\rbrack }_{B}\right) = {\left\lbrack {u}^{ * }\right\rbrack }_{B} \) , donc \( P\left( u\right) = {u}^{ * } \) .

> Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) be the Lagrange polynomial (see part 2.4 page 65) such that \( P\left( {\lambda }_{i}\right) = \overline{{\lambda }_{i}} \) for all \( i \) (this is possible because the \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq r} \) are pairwise distinct). We then see that \( P\left( {\left\lbrack u\right\rbrack }_{B}\right) = {\left\lbrack {u}^{ * }\right\rbrack }_{B} \) , therefore \( P\left( u\right) = {u}^{ * } \) .

EXERCICE 4. a) Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice hermitienne définie positive. Démontrer que det \( A \leq {a}_{1,1}\cdots {a}_{n, n} \) . Donner une condition nécessaire et suffisante pour que cette inégalité soit une égalité.

> EXERCISE 4. a) Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a positive definite Hermitian matrix. Prove that det \( A \leq {a}_{1,1}\cdots {a}_{n, n} \) . Give a necessary and sufficient condition for this inequality to be an equality.

b) Soit \( p \in \mathbb{N} \) tel que \( 0 < p < n \) et \( q = n - p \) . On écrit \( A \) sous la forme

> b) Let \( p \in \mathbb{N} \) be such that \( 0 < p < n \) and \( q = n - p \) . We write \( A \) in the form

\[
A = \left( \begin{matrix} {A}_{1} & B \\  {B}^{ * } & {A}_{2} \end{matrix}\right) \;\text{ avec }\;{A}_{1} \in  {\mathcal{M}}_{p}\left( \mathbb{C}\right) \text{ et }{A}_{2} \in  {\mathcal{M}}_{q}\left( \mathbb{C}\right) .
\]

Montrer que \( \det A \leq \det {A}_{1} \cdot \det {A}_{2} \) .

> Show that \( \det A \leq \det {A}_{1} \cdot \det {A}_{2} \) .

Solution. a) D’après la proposition 3, on peut voir \( A \) comme la matrice de Gram de \( n \) vecteurs \( {U}_{1},\ldots ,{U}_{n} \) de \( {\mathbb{C}}^{n} \) . Si \( M \) désigne la matrice dont les vecteurs colonnes sont \( {U}_{1},\ldots ,{U}_{n} \) , on a \( A = {M}^{ * }M \) . D’après l’inégalité d’Hadamard (théorème 7), on a de \( M\left| { \leq \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{U}_{i}\end{Vmatrix}\text{ , où pour }}\right| \) tout \( i,{\begin{Vmatrix}{U}_{i}\end{Vmatrix}}^{2} = {U}_{i}^{ * }{U}_{i} = {a}_{i, i} \) . Finalement, on peut écrire

> Solution. a) According to Proposition 3, we can view \( A \) as the Gram matrix of \( n \) vectors \( {U}_{1},\ldots ,{U}_{n} \) of \( {\mathbb{C}}^{n} \) . If \( M \) denotes the matrix whose column vectors are \( {U}_{1},\ldots ,{U}_{n} \) , we have \( A = {M}^{ * }M \) . According to Hadamard's inequality (Theorem 7), we have from \( M\left| { \leq \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{U}_{i}\end{Vmatrix}\text{ , où pour }}\right| \) all \( i,{\begin{Vmatrix}{U}_{i}\end{Vmatrix}}^{2} = {U}_{i}^{ * }{U}_{i} = {a}_{i, i} \) . Finally, we can write

\[
\det A = {\left| \det M\right| }^{2} \leq  \mathop{\prod }\limits_{{i = 1}}^{n}{\begin{Vmatrix}{U}_{i}\end{Vmatrix}}^{2} = \mathop{\prod }\limits_{{i = 1}}^{n}{a}_{i, i}
\]

L’égalité se produit lorsque la matrice \( M \) vérifie \( \left| {\det M}\right| = \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{U}_{i}\end{Vmatrix} \) , c’est à dire lorsque les \( {U}_{i} \) sont orthogonaux entre eux deux à deux (voir le théorème 7), ce qui équivaut à dire que \( \forall i \neq j,{U}_{i} \cdot {U}_{j} = {a}_{i, j} = 0 \) , ou encore que \( A \) est diagonale.

> Equality occurs when the matrix \( M \) satisfies \( \left| {\det M}\right| = \mathop{\prod }\limits_{{i = 1}}^{n}\begin{Vmatrix}{U}_{i}\end{Vmatrix} \), that is, when the \( {U}_{i} \) are pairwise orthogonal (see theorem 7), which is equivalent to saying that \( \forall i \neq j,{U}_{i} \cdot {U}_{j} = {a}_{i, j} = 0 \), or that \( A \) is diagonal.

b) Nous nous ramenons d’abord au cas plus simple où \( {A}_{1} \) et \( {A}_{2} \) sont des matrices diagonales. Les matrices \( {A}_{1} \) et \( {A}_{2} \) sont symétriques, il existe donc deux matrices unitaires \( P \in {\mathcal{M}}_{p}\left( \mathbb{C}\right) \) et \( Q \in {\mathcal{M}}_{q}\left( \mathbb{C}\right) \) telles que \( {P}^{ * }{A}_{1}P = {D}_{1} \) et \( {Q}^{ * }{A}_{2}Q = {D}_{2} \) , où \( {D}_{1} \) et \( {D}_{2} \) sont deux matrices diagonales réelles. En définissant la matrice par blocs \( M = \left( \begin{array}{ll} P & 0 \\ 0 & Q \end{array}\right) \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , un calcul simple donne

> b) We first reduce to the simpler case where \( {A}_{1} \) and \( {A}_{2} \) are diagonal matrices. The matrices \( {A}_{1} \) and \( {A}_{2} \) are symmetric, so there exist two unitary matrices \( P \in {\mathcal{M}}_{p}\left( \mathbb{C}\right) \) and \( Q \in {\mathcal{M}}_{q}\left( \mathbb{C}\right) \) such that \( {P}^{ * }{A}_{1}P = {D}_{1} \) and \( {Q}^{ * }{A}_{2}Q = {D}_{2} \), where \( {D}_{1} \) and \( {D}_{2} \) are two real diagonal matrices. By defining the block matrix \( M = \left( \begin{array}{ll} P & 0 \\ 0 & Q \end{array}\right) \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), a simple calculation gives

\[
{M}^{ * }{AM} = \left( \begin{matrix} {P}^{ * }{A}_{1}P & {P}^{ * }{BQ} \\  {Q}^{ * }{B}^{ * }P & {Q}^{ * }{A}_{2}Q \end{matrix}\right)  = C\text{ avec }C = \left( \begin{matrix} {D}_{1} & {P}^{ * }{BQ} \\  {Q}^{ * }{B}^{ * }P & {D}_{2} \end{matrix}\right) .
\]

La matrice \( C \) est congrue à \( A \) , donc hermitienne définie positive, donc d’après le résultat de la question précédente, le déterminant de \( C \) est inférieur au produit de ses coefficients diagonaux. Comme \( {D}_{1} \) et \( {D}_{2} \) sont des matrices diagonales, ceci s’écrit det \( C \leq \det {D}_{1} \cdot \det {D}_{2} \) . Comme \( \det M = \det P \cdot \det Q = 1 \) ( \( M \) est même une matrice unitaire), on en déduit

> The matrix \( C \) is congruent to \( A \), therefore Hermitian positive definite, so according to the result of the previous question, the determinant of \( C \) is less than or equal to the product of its diagonal coefficients. As \( {D}_{1} \) and \( {D}_{2} \) are diagonal matrices, this is written as det \( C \leq \det {D}_{1} \cdot \det {D}_{2} \). Since \( \det M = \det P \cdot \det Q = 1 \) (\( M \) is even a unitary matrix), we deduce

\[
\det A = \det \left( {{M}^{ * }{AM}}\right)  = \det C \leq  \det {D}_{1} \cdot  \det {D}_{2} = \det {A}_{1} \cdot  \det {A}_{2}.
\]

EXERCICE 5 (EXPONENTIELLE D’UNE MATRICE ANTISYMÉTRIQUE). 1/ Soit \( \theta \in \mathbb{R} \) . Montrer l'égalité

> EXERCISE 5 (EXPONENTIAL OF A SKEW-SYMMETRIC MATRIX). 1/ Let \( \theta \in \mathbb{R} \). Show the equality

\[
\exp \left( \begin{matrix} 0 &  - \theta \\  \theta & 0 \end{matrix}\right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) .
\]

2/a) Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer que \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice orthogonale directe si et seulement s’il existe une matrice antisymétrique \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que \( P = \exp \left( A\right) \) . b) En déduire que le groupe spécial orthogonal \( {\mathcal{{SO}}}_{n} \) est connexe par arcs.

> 2/a) Let \( n \in {\mathbb{N}}^{ * } \). Show that \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is a direct orthogonal matrix if and only if there exists a skew-symmetric matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that \( P = \exp \left( A\right) \). b) Deduce that the special orthogonal group \( {\mathcal{{SO}}}_{n} \) is path-connected.

3/ (Cas de \( {\mathbb{R}}^{3} \) ) Soit \( v = \left( {a, b, c}\right) \) un vecteur non nul de l’espace euclidien \( {\mathbb{R}}^{3} \) . a) Montrer que l'exponentielle de la matrice antisymétrique

> 3/ (Case of \( {\mathbb{R}}^{3} \)) Let \( v = \left( {a, b, c}\right) \) be a non-zero vector of the Euclidean space \( {\mathbb{R}}^{3} \). a) Show that the exponential of the skew-symmetric matrix

\[
\widehat{v} = \left( \begin{matrix} 0 &  - c & b \\  c & 0 &  - a \\   - b & a & 0 \end{matrix}\right)
\]

est la matrice de la rotation d’axe \( e = v/\parallel v\parallel \) , d’angle \( \theta = \parallel v\parallel \) , où \( \parallel \cdot \parallel \) désigne la norme euclidienne (indication : remarquer que \( \widehat{v} \) est la matrice de l’endomorphisme \( X \mapsto v \land X \) , où ∧ désigne le produit vectoriel).

> is the matrix of the rotation with axis \( e = v/\parallel v\parallel \), angle \( \theta = \parallel v\parallel \), where \( \parallel \cdot \parallel \) denotes the Euclidean norm (hint: note that \( \widehat{v} \) is the matrix of the endomorphism \( X \mapsto v \land X \), where ∧ denotes the cross product).

b) Montrer la formule de Rodrigues

> b) Show the Rodrigues formula

\[
\exp \left( \widehat{v}\right)  = {I}_{3} + \frac{\sin \theta }{\theta }\widehat{v} + \frac{1 - \cos \theta }{{\theta }^{2}}{\widehat{v}}^{2}.
\]

Solution. 1/ Notons \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . Un calcul facile donne \( {J}^{2} = - {I}_{2} \) , ce qui entraîne pour tout \( n \in \mathbb{N} \) les égalités \( {J}^{2n} = {\left( -1\right) }^{n}{I}_{2} \) et \( {J}^{{2n} + 1} = {\left( -1\right) }^{n}J \) . On en déduit

> Solution. 1/ Let \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . An easy calculation gives \( {J}^{2} = - {I}_{2} \) , which implies for all \( n \in \mathbb{N} \) the equalities \( {J}^{2n} = {\left( -1\right) }^{n}{I}_{2} \) and \( {J}^{{2n} + 1} = {\left( -1\right) }^{n}J \) . We deduce from this

\[
\exp \left( {\theta J}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\theta }^{n}}{n!}{J}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}{\theta }^{2n}}{\left( {2n}\right) !}{I}_{2} + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}{\theta }^{{2n} + 1}}{\left( {{2n} + 1}\right) !}J = \left( {\cos \theta }\right) {I}_{2} + \left( {\sin \theta }\right) J,
\]

ce qui est précisément le résultat demandé.

> which is precisely the requested result.

2/a) La condition suffisante est immédiate : si \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice antisymétrique, alors la matrice \( P = \exp \left( A\right) \) vérifie \( {}^{\mathrm{t}}{PP} = \exp \left( {{}^{\mathrm{t}}A}\right) \exp \left( A\right) = \exp \left( {-A}\right) \exp \left( A\right) = {I}_{n} \) . Enfin, on a \( \det \left( P\right) = \det \left( {\exp \left( A\right) }\right) = \exp \left( {\operatorname{tr}A}\right) = 1 \) (voir l’exercice 2, page 196).

> 2/a) The sufficient condition is immediate: if \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is an antisymmetric matrix, then the matrix \( P = \exp \left( A\right) \) satisfies \( {}^{\mathrm{t}}{PP} = \exp \left( {{}^{\mathrm{t}}A}\right) \exp \left( A\right) = \exp \left( {-A}\right) \exp \left( A\right) = {I}_{n} \) . Finally, we have \( \det \left( P\right) = \det \left( {\exp \left( A\right) }\right) = \exp \left( {\operatorname{tr}A}\right) = 1 \) (see exercise 2, page 196).

Montrons maintenant la condition nécessaire. Soit \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice orthogonale directe, soit \( u \in \mathcal{L}\left( {\mathbb{R}}^{n}\right) \) son isométrie associée. D’après le théorème 1 page 268, il existe une base orthonormale \( B \) de \( {\mathbb{R}}^{n} \) dans laquelle la matrice de \( u \) a la forme

> Now let us show the necessary condition. Let \( P \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a direct orthogonal matrix, let \( u \in \mathcal{L}\left( {\mathbb{R}}^{n}\right) \) be its associated isometry. According to theorem 1 on page 268, there exists an orthonormal basis \( B \) of \( {\mathbb{R}}^{n} \) in which the matrix of \( u \) has the form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} R\left( {\theta }_{1}\right) & & & & & \\   &  \ddots  & & & 0 & \\   & & R\left( {\theta }_{r}\right) & & & \\   & & & {\varepsilon }_{1} & & \\   & 0 & & &  \ddots  & \\   & & & & & {\varepsilon }_{s} \end{matrix}\right) ,
\]

où pour tout \( i, R\left( {\theta }_{i}\right) \) est la matrice de rotation \( 2 \times 2 \) d’angle \( {\theta }_{i} \) , et où \( {\varepsilon }_{j} \in \{ - 1,1\} \) pour tout \( j \) . Par hypothèse, \( u \) est une isométrie directe donc det \( u = 1 \) . Le calcul de déterminant par blocs donne

> where for all \( i, R\left( {\theta }_{i}\right) \) is the rotation matrix \( 2 \times 2 \) of angle \( {\theta }_{i} \) , and where \( {\varepsilon }_{j} \in \{ - 1,1\} \) for all \( j \) . By hypothesis, \( u \) is a direct isometry, so det \( u = 1 \) . The block determinant calculation gives

\[
\det u = \det R\left( {\theta }_{1}\right) \cdots \det R\left( {\theta }_{r}\right) {\varepsilon }_{1}\cdots {\varepsilon }_{s} = {\varepsilon }_{1}\cdots {\varepsilon }_{s}.
\]

Ainsi, le produit des \( {\varepsilon }_{i} \) vaut 1, donc il y en a un nombre pair \( {2p} \) (avec \( p \in \mathbb{N} \) ) qui valent -1, et les \( q \) autres valent 1 (avec \( {2p} + q = s \) ). Quitte à permuter les \( s \) derniers vecteurs de la base \( B \) , on peut même supposer que les \( {2p} \) premiers \( {\varepsilon }_{j} \) valent -1, et les \( q \) derniers valent 1 . Comme la matrice \( \left( \begin{matrix} - 1 & 0 \\ 0 & - 1 \end{matrix}\right) \) est une matrice de rotation d’angle \( \pi \) , il revient au même de dire que la matrice de \( u \) dans \( B \) a la forme

> Thus, the product of the \( {\varepsilon }_{i} \) is 1, so there is an even number \( {2p} \) (with \( p \in \mathbb{N} \) ) that are equal to -1, and the \( q \) others are equal to 1 (with \( {2p} + q = s \) ). By permuting the last \( s \) vectors of the basis \( B \) , we can even assume that the first \( {2p} \) \( {\varepsilon }_{j} \) are equal to -1, and the last \( q \) are equal to 1. Since the matrix \( \left( \begin{matrix} - 1 & 0 \\ 0 & - 1 \end{matrix}\right) \) is a rotation matrix of angle \( \pi \) , it amounts to the same thing to say that the matrix of \( u \) in \( B \) has the form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} R\left( {\theta }_{1}\right) & & & 0 \\   &  \ddots  & & 0 \\   & 0 & & R\left( {\theta }_{m}\right)  \end{matrix}\right) ,
\]

avec \( {\theta }_{i} = \pi \) pour \( r < i \leq m = r + p \) . Le résultat de la question \( 1/ \) nous permet maintenant de remarquer que

> with \( {\theta }_{i} = \pi \) for \( r < i \leq m = r + p \) . The result of question \( 1/ \) now allows us to note that

\[
{\left\lbrack  u\right\rbrack  }_{B} = \exp \left( M\right) \;\text{ où }\;M = \left( \begin{matrix} {\theta }_{1}J & & 0 \\   &  \ddots  & 0 \\  0 & & {\theta }_{m}J \end{matrix}\right) ,
\]

avec \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . La matrice par blocs \( M \) est antisymétrique car \( J \) est antisymétrique.

> with \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . The block matrix \( M \) is antisymmetric because \( J \) is antisymmetric.

En notant \( Q \) la matrice de passage de la base canonique de \( {\mathbb{R}}^{n} \) à la base \( B \) (c’est une matrice orthogonale), on a donc montré que \( P = {}^{\mathrm{t}}Q\exp \left( M\right) Q \) . En posant \( A = {}^{\mathrm{t}}{QMQ} \) , on a donc \( P = \exp \left( A\right) \) et la matrice \( A \) est antisymétrique car \( {}^{\mathrm{t}}A = {}^{\mathrm{t}}Q{}^{\mathrm{t}}{MQ} = {}^{\mathrm{t}}Q\left( {-M}\right) Q = - A \) .

> By denoting \( Q \) the transition matrix from the canonical basis of \( {\mathbb{R}}^{n} \) to the basis \( B \) (it is an orthogonal matrix), we have therefore shown that \( P = {}^{\mathrm{t}}Q\exp \left( M\right) Q \) . By setting \( A = {}^{\mathrm{t}}{QMQ} \) , we thus have \( P = \exp \left( A\right) \) and the matrix \( A \) is antisymmetric because \( {}^{\mathrm{t}}A = {}^{\mathrm{t}}Q{}^{\mathrm{t}}{MQ} = {}^{\mathrm{t}}Q\left( {-M}\right) Q = - A \) .

b) Soient deux matrices \( P \) et \( Q \) dans \( {\mathcal{{SO}}}_{n} \) . On peut écrire \( P = \exp \left( A\right) \) et \( Q = \exp \left( B\right) \) avec \( A \) et \( B \) antisymétriques d’après la question précédente. La question précédente nous assure également que le chemin continu \( \left\lbrack {0,1}\right\rbrack \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;t \mapsto \exp \left( {\left( {1 - t}\right) A + {tB}}\right) \) est à valeur dans \( {\mathcal{{SO}}}_{n} \) (la matrice \( \left( {1 - t}\right) A + {tB} \) est antisymétrique), donc le groupe spécial orthogonal est bien connexe par arcs. 3/a) Suivons l’indication et considérons l’endomorphisme \( u : {\mathbb{R}}^{3} \rightarrow {\mathbb{R}}^{3}\;X \mapsto v \land X \) . On remarque aisément que la matrice de \( u \) dans la base canonique de \( {\mathbb{R}}^{3} \) est la matrice \( \widehat{v} \) . Partant du vecteur \( e = v/\parallel v\parallel = \frac{1}{\theta }v \) , on le complète avec deux vecteurs \( {e}_{1} \) et \( {e}_{2} \) de sorte que \( \left( {{e}_{1},{e}_{2}, e}\right) \) soit une base orthonormale directe de \( {\mathbb{R}}^{3} \) . Comme \( v = {\theta e} \) , on a

> b) Let two matrices \( P \) and \( Q \) be in \( {\mathcal{{SO}}}_{n} \) . We can write \( P = \exp \left( A\right) \) and \( Q = \exp \left( B\right) \) with \( A \) and \( B \) antisymmetric according to the previous question. The previous question also ensures that the continuous path \( \left\lbrack {0,1}\right\rbrack \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;t \mapsto \exp \left( {\left( {1 - t}\right) A + {tB}}\right) \) is valued in \( {\mathcal{{SO}}}_{n} \) (the matrix \( \left( {1 - t}\right) A + {tB} \) is antisymmetric), so the special orthogonal group is indeed path-connected. 3/a) Let us follow the hint and consider the endomorphism \( u : {\mathbb{R}}^{3} \rightarrow {\mathbb{R}}^{3}\;X \mapsto v \land X \) . We easily notice that the matrix of \( u \) in the canonical basis of \( {\mathbb{R}}^{3} \) is the matrix \( \widehat{v} \) . Starting from the vector \( e = v/\parallel v\parallel = \frac{1}{\theta }v \) , we complete it with two vectors \( {e}_{1} \) and \( {e}_{2} \) such that \( \left( {{e}_{1},{e}_{2}, e}\right) \) is a direct orthonormal basis of \( {\mathbb{R}}^{3} \) . Since \( v = {\theta e} \) , we have

\[
u\left( {e}_{1}\right)  = {\theta e} \land  {e}_{1} = \theta {e}_{2},\;u\left( {e}_{2}\right)  = {\theta e} \land  {e}_{2} =  - \theta {e}_{1},\;u\left( e\right)  = {\theta e} \land  e = 0,
\]

autrement dit la matrice de \( u \) dans la base \( B \) a la forme par blocs

> in other words, the matrix of \( u \) in the basis \( B \) has the block form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} {\theta J} & 0 \\  0 & 0 \end{matrix}\right)
\]

(*)

> où \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . Nous avons vu que \( \exp \left( {\theta J}\right) \) est la matrice \( 2 \times 2 \) de rotation d’angle \( \theta \) , donc

where \( J = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \) . We have seen that \( \exp \left( {\theta J}\right) \) is the rotation matrix \( 2 \times 2 \) with angle \( \theta \) , therefore

\[
\exp \left( {\left\lbrack  u\right\rbrack  }_{B}\right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{matrix}\right) .
\]

\( \left( {* * }\right) \)

> Comme \( \exp \left( {\left\lbrack u\right\rbrack }_{B}\right) \) est aussi la matrice de \( \exp \left( u\right) \) dans la base \( B \) , ceci entraîne que \( \exp \left( u\right) \) est la rotation autour du vecteur \( e \) d’angle \( \theta \) , d’où le résultat.

Since \( \exp \left( {\left\lbrack u\right\rbrack }_{B}\right) \) is also the matrix of \( \exp \left( u\right) \) in the basis \( B \) , this implies that \( \exp \left( u\right) \) is the rotation around the vector \( e \) with angle \( \theta \) , hence the result.

> b) En utilisant la forme par bloc \( \left( *\right) \) de la matrice de \( u \) dans la base \( B \) , on obtient

b) Using the block form \( \left( *\right) \) of the matrix of \( u \) in the basis \( B \) , we obtain

\[
{I}_{3} + \frac{\sin \theta }{\theta }{\left\lbrack  u\right\rbrack  }_{B} + \frac{1 - \cos \theta }{{\theta }^{2}}{\left( {\left\lbrack  u\right\rbrack  }_{B}\right) }^{2} = {I}_{3} + \sin \theta \left( \begin{array}{ll} J & 0 \\  0 & 0 \end{array}\right)  + \left( {1 - \cos \theta }\right) \left( \begin{matrix}  - {I}_{2} & 0 \\  0 & 0 \end{matrix}\right)
\]

ce qui s'écrit encore

> which can also be written as

\[
{I}_{3} + \frac{\sin \theta }{\theta }{\left\lbrack  u\right\rbrack  }_{B} + \frac{1 - \cos \theta }{{\theta }^{2}}{\left( {\left\lbrack  u\right\rbrack  }_{B}\right) }^{2} = \left( \begin{matrix} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{matrix}\right) .
\]

D’après la forme \( \left( {* * }\right) \) , ceci est précisément l’exponentielle de la matrice \( u \) dans la base \( B \) . D’où le résultat par changement de base.

> According to the form \( \left( {* * }\right) \) , this is precisely the exponential of the matrix \( u \) in the basis \( B \) . Hence the result by change of basis.

EXERCICE 6. 1/ Soit \( n \) un entier naturel non nul. Montrer que l’application

> EXERCISE 6. 1/ Let \( n \) be a non-zero natural number. Show that the mapping

\[
\varphi  : {\mathbb{R}}^{n} \rightarrow  \mathbb{R}\;\left( {{a}_{1},\ldots ,{a}_{n}}\right)  \mapsto  {\int }_{0}^{1}{\left( 1 + {a}_{1}x + \cdots  + {a}_{n}{x}^{n}\right) }^{2}{dx}.
\]

admet un minimum \( \mu \) , atteint en un point unique de \( {\mathbb{R}}^{n} \) , et calculer \( \mu \) en utilisant l’expression de la distance d'un point à un s.e.v en fonction des déterminants de Gram.

> admits a minimum \( \mu \) , attained at a unique point of \( {\mathbb{R}}^{n} \) , and calculate \( \mu \) using the expression for the distance from a point to a subspace in terms of Gram determinants.

2/ Retrouver la valeur de \( \mu \) directement, sans utiliser les déterminant de Gram.

> 2/ Find the value of \( \mu \) directly, without using Gram determinants.

Solution. 1/ Munissons le \( \mathbb{R} \) -e.v \( E = \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \) des fonctions continues de \( \left\lbrack {0,1}\right\rbrack \) dans \( \mathbb{R} \) du produit scalaire

> Solution. 1/ Equip the \( \mathbb{R} \) -v.s. \( E = \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \) of continuous functions from \( \left\lbrack {0,1}\right\rbrack \) to \( \mathbb{R} \) with the inner product

\[
\forall f, g \in  E,\;\langle f, g\rangle  = {\int }_{0}^{1}f\left( t\right) g\left( t\right) {dt}.
\]

Par commodité de notation, pour tout entier \( i \) on désigne par \( {x}^{i} \) la fonction \( \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{i} \) . En notant \( {E}_{n} = \operatorname{Vect}\left( {x,\ldots ,{x}^{n}}\right) \) , on remarque que

> For notational convenience, for any integer \( i \) we denote by \( {x}^{i} \) the function \( \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{i} \) . By noting \( {E}_{n} = \operatorname{Vect}\left( {x,\ldots ,{x}^{n}}\right) \) , we observe that

\[
\varphi \left( {{a}_{1},\ldots ,{a}_{n}}\right)  = \parallel 1 - P{\parallel }^{2},\;\text{ où }\;P =  - \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{x}^{i} \in  {E}_{n},
\]

et où \( \parallel .\parallel \) désigne la norme issue du produit scalaire \( \langle \) , \( \rangle .D \) éterminer \( \mu = \mathop{\inf }\limits_{{a \in {\mathbb{R}}^{n}}}\varphi \left( a\right) \) , c’est donc rechercher \( d{\left( 1,{E}_{n}\right) }^{2} = \mathop{\inf }\limits_{{P \in {E}_{n}}}\parallel 1 - P{\parallel }^{2} = \mu \) .

> and where \( \parallel .\parallel \) denotes the norm derived from the inner product \( \langle \) , \( \rangle .D \) etermining \( \mu = \mathop{\inf }\limits_{{a \in {\mathbb{R}}^{n}}}\varphi \left( a\right) \) , is therefore searching for \( d{\left( 1,{E}_{n}\right) }^{2} = \mathop{\inf }\limits_{{P \in {E}_{n}}}\parallel 1 - P{\parallel }^{2} = \mu \) .

La proposition 2 de la page 254 assure l’existence et l’unicité d’un point \( {P}_{0} \) de \( {E}_{n} \) tel que \( \begin{Vmatrix}{1 - {P}_{0}}\end{Vmatrix} = d\left( {1,{E}_{n}}\right) \) (de plus, \( {P}_{0} \) est la projection orthogonale de 1 sur \( {E}_{n} \) ). Le minimum de \( \varphi \) est donc atteint en un point unique de \( {\mathbb{R}}^{n} \) . D’après le théorème 8 sa valeur \( \mu \) est donnée par

> Proposition 2 on page 254 ensures the existence and uniqueness of a point \( {P}_{0} \) of \( {E}_{n} \) such that \( \begin{Vmatrix}{1 - {P}_{0}}\end{Vmatrix} = d\left( {1,{E}_{n}}\right) \) (furthermore, \( {P}_{0} \) is the orthogonal projection of 1 onto \( {E}_{n} \) ). The minimum of \( \varphi \) is therefore attained at a unique point of \( {\mathbb{R}}^{n} \) . According to theorem 8, its value \( \mu \) is given by

\[
\mu  = d{\left( 1,{E}_{n}\right) }^{2} = \frac{G\left( {1, x,\ldots ,{x}^{n}}\right) }{G\left( {x,\ldots ,{x}^{n}}\right) }.
\]

(*)

> Comme \( \left\langle {{x}^{i},{x}^{j}}\right\rangle = 1/\left( {i + j + 1}\right) \) , on a

Since \( \left\langle {{x}^{i},{x}^{j}}\right\rangle = 1/\left( {i + j + 1}\right) \) , we have

\[
G\left( {1, x,\ldots ,{x}^{n}}\right)  = \det {\left( \frac{1}{i + j - 1}\right) }_{1 \leq  i, j \leq  n + 1}\;\text{ et }\;G\left( {x,\ldots ,{x}^{n}}\right)  = \det {\left( \frac{1}{i + j + 1}\right) }_{1 \leq  i, j \leq  n}.
\]

Ces déterminants sont des déterminants de Cauchy (voir l'exercice 7, page 150) que l'on sait calculer. Ils valent respectivement

> These determinants are Cauchy determinants (see exercise 7, page 150) which we know how to calculate. They are respectively equal to

\[
G\left( {1, x,\ldots ,{x}^{n}}\right)  = \frac{\mathop{\prod }\limits_{{1 \leq  i < j \leq  n + 1}}{\left( i - j\right) }^{2}}{\mathop{\prod }\limits_{{1 \leq  i, j \leq  n + 1}}\left( {i + j - 1}\right) }\text{ et }G\left( {x,\ldots ,{x}^{n}}\right)  = \frac{\mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}{\left( i - j\right) }^{2}}{\mathop{\prod }\limits_{{1 \leq  i, j \leq  n}}\left( {i + j + 1}\right) }.
\]

En utilisant l’égalité \( \left( *\right) \) et l’identité \( \mathop{\prod }\limits_{{1 \leq i, j \leq n + 1}}\left( {i + j - 1}\right) = \mathop{\prod }\limits_{{0 \leq i, j \leq n}}\left( {i + j + 1}\right) \) , on a donc

> Using the equality \( \left( *\right) \) and the identity \( \mathop{\prod }\limits_{{1 \leq i, j \leq n + 1}}\left( {i + j - 1}\right) = \mathop{\prod }\limits_{{0 \leq i, j \leq n}}\left( {i + j + 1}\right) \) , we therefore have

\[
\mu  = \frac{\mathop{\prod }\limits_{{1 \leq  i \leq  n}}{\left\lbrack  i - \left( n + 1\right) \right\rbrack  }^{2}}{\left( {n + 1}\right) {!}^{2}} = \frac{n{!}^{2}}{\left( {n + 1}\right) {!}^{2}} = \frac{1}{{\left( n + 1\right) }^{2}}.
\]

2/ Calculons \( \mu \) sans utiliser (*). Notons \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in {\mathbb{R}}^{n} \) le point en lequel est atteint le minimum de \( \varphi \) . Nous avons vu que \( {P}_{0} = - \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{x}^{i} \) est la projection orthogonale de 1 sur \( {E}_{n} \) . Donc \( \left\langle {1 - {P}_{0},{x}^{k}}\right\rangle = 0 \) pour \( 1 \leq k \leq n \) , et \( \mu = \left\langle {1 - {P}_{0},1 - {P}_{0}}\right\rangle = \left\langle {1 - {P}_{0},1}\right\rangle \) . Autrement dit

> 2/ Let us calculate \( \mu \) without using (*). Let \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in {\mathbb{R}}^{n} \) be the point at which the minimum of \( \varphi \) is attained. We have seen that \( {P}_{0} = - \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{x}^{i} \) is the orthogonal projection of 1 onto \( {E}_{n} \) . Thus \( \left\langle {1 - {P}_{0},{x}^{k}}\right\rangle = 0 \) for \( 1 \leq k \leq n \) , and \( \mu = \left\langle {1 - {P}_{0},1 - {P}_{0}}\right\rangle = \left\langle {1 - {P}_{0},1}\right\rangle \) . In other words

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\frac{1}{k + 1} + \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{a}_{i}}{i + k + 1} = 0\;\text{ et }\;\mu  = 1 + \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{a}_{i}}{i + 1}.
\]

En considérant la fraction rationnelle \( F\left( X\right) = 1/\left( {X + 1}\right) + \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}/\left( {X + i + 1}\right) \) , ceci s’écrit aussi \( F\left( k\right) = 0 \) pour \( k = 1,\ldots , n \) et \( \mu = F\left( 0\right) \) . La forme réduite de \( F \) a donc la forme

> By considering the rational fraction \( F\left( X\right) = 1/\left( {X + 1}\right) + \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}/\left( {X + i + 1}\right) \), this can also be written as \( F\left( k\right) = 0 \) for \( k = 1,\ldots , n \) and \( \mu = F\left( 0\right) \). The reduced form of \( F \) therefore has the form

\[
F\left( X\right)  = \alpha \frac{\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - i}\right) }{\mathop{\prod }\limits_{{i = 0}}^{n}\left( {X + i + 1}\right) }.
\]

\( \left( {* * }\right) \)

> Pour déterminer \( \alpha \) , on multiplie \( F \) par \( X + 1 \) et on fait \( X = - 1 \) , ce qui fournit \( 1 = \alpha \mathop{\prod }\limits_{{i = 1}}^{n}\frac{-\left( {1 + i}\right) }{i} = \; {\left( -1\right) }^{n}\left( {n + 1}\right) \) donc \( \alpha = {\left( -1\right) }^{n}/\left( {n + 1}\right) \) . On conclut avec l’expression (**), en écrivant

To determine \( \alpha \), we multiply \( F \) by \( X + 1 \) and perform \( X = - 1 \), which yields \( 1 = \alpha \mathop{\prod }\limits_{{i = 1}}^{n}\frac{-\left( {1 + i}\right) }{i} = \; {\left( -1\right) }^{n}\left( {n + 1}\right) \) and thus \( \alpha = {\left( -1\right) }^{n}/\left( {n + 1}\right) \). We conclude with expression (**), by writing

\[
\mu  = F\left( 0\right)  = \alpha \frac{\mathop{\prod }\limits_{{i = 1}}^{n}\left( {-i}\right) }{\mathop{\prod }\limits_{{i = 0}}^{n}\left( {i + 1}\right) } = \alpha \frac{{\left( -1\right) }^{n}}{n + 1} = \frac{1}{{\left( n + 1\right) }^{2}}.
\]

Remarque. On pourrait de même calculer

> Remark. One could similarly calculate

\[
\mathop{\inf }\limits_{{\left( {{a}_{1},\ldots ,{a}_{n}}\right)  \in  {\mathbb{R}}^{n}}}{\int }_{0}^{+\infty }{e}^{-x}{\left( 1 + {a}_{1}x + \cdots  + {a}_{n}{x}^{n}\right) }^{2}{dx}.
\]

- Cet exercice est à rapprocher du problème du tome d'analyse portant sur le théorème de Müntz.

> - This exercise is to be compared with the problem in the analysis volume concerning the Müntz theorem.
