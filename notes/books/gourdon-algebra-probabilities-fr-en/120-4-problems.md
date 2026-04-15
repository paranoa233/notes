### 4. Problems

*Français : 4. Problèmes*

Problem 1 (THÉORÉME DE FISHER-COCHRAN). Soit \( E \) un espace euclidien de dimension \( n \) et \( {u}_{1},\ldots ,{u}_{p} \) des endomorphismes symétriques de \( E \) . On suppose que

> Problem 1 (FISHER-COCHRAN THEOREM). Let \( E \) be a Euclidean space of dimension \( n \) and \( {u}_{1},\ldots ,{u}_{p} \) be symmetric endomorphisms of \( E \). We assume that

(i) \( \operatorname{rg}{u}_{1} + \cdots + \operatorname{rg}{u}_{p} = n \) .

> (ii) \( {q}_{1}\left( x\right) + \cdots + {q}_{p}\left( x\right) = x \cdot x \) , où \( {q}_{i} \) désigne la forme quadratique \( {q}_{i}\left( x\right) = {u}_{i}\left( x\right) \cdot x \) pour tout \( i \) .

(ii) \( {q}_{1}\left( x\right) + \cdots + {q}_{p}\left( x\right) = x \cdot x \), where \( {q}_{i} \) denotes the quadratic form \( {q}_{i}\left( x\right) = {u}_{i}\left( x\right) \cdot x \) for all \( i \).

> Montrer que \( E = \operatorname{Im}{u}_{1} \oplus \cdots \oplus \operatorname{Im}{u}_{p} \) , que les \( \operatorname{Im}{u}_{i} \) sont orthogonaux entre eux deux à deux, et que pour tout \( i,{u}_{i} \) est le projecteur orthogonal sur \( \operatorname{Im}{u}_{i} \) .

Show that \( E = \operatorname{Im}{u}_{1} \oplus \cdots \oplus \operatorname{Im}{u}_{p} \), that the \( \operatorname{Im}{u}_{i} \) are pairwise orthogonal, and that for all \( i,{u}_{i} \) is the orthogonal projector onto \( \operatorname{Im}{u}_{i} \).

> Solution. La relation (ii) s'écrit aussi

Solution. The relation (ii) can also be written as

\[
\forall x \in  E,\;\left( {{u}_{1} + \cdots  + {u}_{p} - {\operatorname{Id}}_{E}}\right) \left( x\right)  \cdot  x = 0.
\]

(*)

> L’endomorphisme \( v = {u}_{1} + \cdots + {u}_{p} - {\operatorname{Id}}_{E} \) étant symétrique,(*) entraîne \( v = 0 \) (en effet, \( v \) est diagonalisable et \( \left( *\right) \) montre que la seule valeur propre de \( v \) est 0 ). Donc \( {u}_{1} + \cdots + {u}_{p} = {\operatorname{Id}}_{E} \) , d’où on tire \( E = \operatorname{Im}{u}_{1} + \cdots + \operatorname{Im}{u}_{p} \) . Comme de plus \( \mathop{\sum }\limits_{{i = 1}}^{p}\dim \left( {\operatorname{Im}{u}_{i}}\right) = \dim E \) d’après (i), on a

Since the endomorphism \( v = {u}_{1} + \cdots + {u}_{p} - {\operatorname{Id}}_{E} \) is symmetric, (*) implies \( v = 0 \) (indeed, \( v \) is diagonalizable and \( \left( *\right) \) shows that the only eigenvalue of \( v \) is 0). Thus \( {u}_{1} + \cdots + {u}_{p} = {\operatorname{Id}}_{E} \), from which we derive \( E = \operatorname{Im}{u}_{1} + \cdots + \operatorname{Im}{u}_{p} \). As furthermore \( \mathop{\sum }\limits_{{i = 1}}^{p}\dim \left( {\operatorname{Im}{u}_{i}}\right) = \dim E \) according to (i), we have

\[
E = \operatorname{Im}{u}_{1} \oplus  \cdots  \oplus  \operatorname{Im}{u}_{p}
\]

(**)

> (voir la proposition 6 page 117).

(see proposition 6 on page 117).

> En appliquant maintenant l’égalité \( {\operatorname{Id}}_{E} = {u}_{1} + \cdots + {u}_{p} \) au vecteur \( {u}_{k}\left( x\right) \) , on obtient

By now applying the equality \( {\operatorname{Id}}_{E} = {u}_{1} + \cdots + {u}_{p} \) to the vector \( {u}_{k}\left( x\right) \), we obtain

\[
\forall k,\forall x \in  E,\;{u}_{k}\left( x\right)  = {u}_{1}{u}_{k}\left( x\right)  + \cdots  + {u}_{p}{u}_{k}\left( x\right) .
\]

(***)

> D’après \( \left( {* * }\right) \) , la décomposition d’un élément de \( \operatorname{Im}{u}_{k} \) se fait de manière unique dans \( { \oplus }_{i = 1}^{p}\operatorname{Im}{u}_{i} \) , d’où on déduit, avec \( \left( {* * * }\right) \) que \( {u}_{k}\left( x\right) = {u}_{k}^{2}\left( x\right) \) et \( \forall \ell \neq k,{u}_{k}{u}_{\ell }\left( x\right) = 0 \) . Ceci étant vrai pour tout \( x \in E \) , on en tire \( {u}_{k} = {u}_{k}^{2} \) et \( \forall \ell \neq k,{u}_{k}{u}_{\ell } = 0 \) . Les endomorphismes \( {u}_{k} \) sont donc des projecteurs, orthogonaux puisqu'ils sont symétriques (ses sous-espaces propres sont orthogonaux, et ce sont ici Ker \( {u}_{k} \) et \( \operatorname{Im}{u}_{k} \) ).

According to \( \left( {* * }\right) \), the decomposition of an element of \( \operatorname{Im}{u}_{k} \) is unique in \( { \oplus }_{i = 1}^{p}\operatorname{Im}{u}_{i} \), from which we deduce, with \( \left( {* * * }\right) \), that \( {u}_{k}\left( x\right) = {u}_{k}^{2}\left( x\right) \) and \( \forall \ell \neq k,{u}_{k}{u}_{\ell }\left( x\right) = 0 \). Since this is true for any \( x \in E \), we derive \( {u}_{k} = {u}_{k}^{2} \) and \( \forall \ell \neq k,{u}_{k}{u}_{\ell } = 0 \). The endomorphisms \( {u}_{k} \) are therefore orthogonal projectors, as they are symmetric (their eigenspaces are orthogonal, and here they are Ker \( {u}_{k} \) and \( \operatorname{Im}{u}_{k} \)).

> Il nous reste à montrer que les \( \operatorname{Im}{u}_{k} \) sont orthogonaux entre eux deux à deux. Pour \( k \neq \ell \) , on a vu \( {u}_{k}{u}_{\ell } = 0 \) , ce qui entraîne \( \operatorname{Im}{u}_{\ell } \subset \operatorname{Ker}{u}_{k} \) . L’endomorphisme \( {u}_{k} \) étant un projecteur orthogonal, on a Ker \( {u}_{k} = {\left( \operatorname{Im}{u}_{k}\right) }^{ \bot } \) , donc \( \operatorname{Im}{u}_{\ell } \subset {\left( \operatorname{Im}{u}_{k}\right) }^{ \bot } \) , ce qui prouve que \( \operatorname{Im}{u}_{\ell } \) et \( \operatorname{Im}{u}_{k} \) sont orthogonaux. Ceci est vrai dès que le couple \( \left( {k,\ell }\right) \) vérifie \( k \neq \ell \) , d’où le résultat.

It remains for us to show that the \( \operatorname{Im}{u}_{k} \) are pairwise orthogonal. For \( k \neq \ell \), we have seen \( {u}_{k}{u}_{\ell } = 0 \), which implies \( \operatorname{Im}{u}_{\ell } \subset \operatorname{Ker}{u}_{k} \). Since the endomorphism \( {u}_{k} \) is an orthogonal projector, we have Ker \( {u}_{k} = {\left( \operatorname{Im}{u}_{k}\right) }^{ \bot } \), thus \( \operatorname{Im}{u}_{\ell } \subset {\left( \operatorname{Im}{u}_{k}\right) }^{ \bot } \), which proves that \( \operatorname{Im}{u}_{\ell } \) and \( \operatorname{Im}{u}_{k} \) are orthogonal. This is true as soon as the pair \( \left( {k,\ell }\right) \) satisfies \( k \neq \ell \), hence the result.

> Problem 2. Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( \mathcal{S} \) le s.e.v des matrices symétriques de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Pour tout \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , on définit l’endomorphisme de \( \mathcal{S} \)

Problem 2. Let \( n \in {\mathbb{N}}^{ * } \). We denote by \( \mathcal{S} \) the subspace of symmetric matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). For any \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), we define the endomorphism of \( \mathcal{S} \)

\[
{\varphi }_{A} : \mathcal{S} \rightarrow  \mathcal{S}\;M \mapsto  {}^{\mathrm{t}}{AMA}.
\]

Montrer que \( \left| {\det {\varphi }_{A}}\right| = {\left| \det A\right| }^{n + 1} \) .

> Show that \( \left| {\det {\varphi }_{A}}\right| = {\left| \det A\right| }^{n + 1} \).

Solution. Commençons par traiter le cas où \( A \) est diagonale (cas qui semble intuitivement simple). Notons \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) les coefficients diagonaux de \( A \) . Considérons la base \( B \) de \( \mathcal{S} \) constituée des matrices de la forme \( {\left( {E}_{i, i}\right) }_{1 \leq i \leq n} \) et \( {\left( {E}_{i, j} + {E}_{j, i}\right) }_{1 \leq i < j \leq n} \) , où \( {E}_{i, j} \) désigne la matrice dont tous les coefficients sont nuls sauf celui d'indice \( \left( {i, j}\right) \) qui vaut 1 . Un calcul rapide montre que

> Solution. Let us begin by treating the case where \( A \) is diagonal (a case that seems intuitively simple). Let \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) denote the diagonal coefficients of \( A \). Consider the basis \( B \) of \( \mathcal{S} \) consisting of matrices of the form \( {\left( {E}_{i, i}\right) }_{1 \leq i \leq n} \) and \( {\left( {E}_{i, j} + {E}_{j, i}\right) }_{1 \leq i < j \leq n} \), where \( {E}_{i, j} \) denotes the matrix whose coefficients are all zero except for the one at index \( \left( {i, j}\right) \), which is 1. A quick calculation shows that

\[
\forall i,\;{\varphi }_{A}\left( {E}_{i, i}\right)  = {\lambda }_{i}^{2}{E}_{i, i}\;\text{ et }\;\forall i < j,\;{\varphi }_{A}\left( {{E}_{i, j} + {E}_{j, i}}\right)  = {\lambda }_{i}{\lambda }_{j}\left( {{E}_{i, j} + {E}_{j, i}}\right) .
\]

La base \( B \) diagonalise donc \( {\varphi }_{A} \) , les valeurs propres correspondantes étant \( {\lambda }_{i}{\lambda }_{j}\left( {1 \leq i \leq j \leq n}\right) \) , ce qui montre que

> The basis \( B \) therefore diagonalizes \( {\varphi }_{A} \), with the corresponding eigenvalues being \( {\lambda }_{i}{\lambda }_{j}\left( {1 \leq i \leq j \leq n}\right) \), which shows that

\[
\det {\varphi }_{A} = \mathop{\prod }\limits_{{1 \leq  i \leq  j \leq  n}}{\lambda }_{i}{\lambda }_{j} = {\left( \mathop{\prod }\limits_{{i = 1}}^{n}{\lambda }_{i}\right) }^{n + 1} = {\left( \det A\right) }^{n + 1}.
\]

(*)

> Traitons maintenant le cas général. Commençons par munir \( \mathcal{S} \) d’un produit scalaire. Si \( S, T \in \; \mathcal{S} \) , on définit le produit scalaire de \( \left( {S, T}\right) \) par \( \left( {S \mid T}\right) = \operatorname{tr}\left( {ST}\right) \) . Il s’agit bien d’un produit scalaire

Let us now treat the general case. Let us begin by equipping \( \mathcal{S} \) with a scalar product. If \( S, T \in \; \mathcal{S} \) , we define the scalar product of \( \left( {S, T}\right) \) by \( \left( {S \mid T}\right) = \operatorname{tr}\left( {ST}\right) \) . This is indeed a scalar product

> puisque c'est une forme bilinéaire symétrique, et la forme quadratique associée est définie positive car

since it is a symmetric bilinear form, and the associated quadratic form is positive definite because

\[
\forall S = {\left( {s}_{i, j}\right) }_{1 \leq  i, j \leq  n} \in  \mathcal{S},\;\operatorname{tr}\left( {S}^{2}\right)  = \mathop{\sum }\limits_{{i, j}}{s}_{i, j}{s}_{j, i} = \mathop{\sum }\limits_{{i, j}}{s}_{i, j}^{2}.
\]

L’introduction de la structure euclidienne sur \( \mathcal{S} \) va nous permettre de définir l’adjoint de \( {\varphi }_{A} \) . Comme

> The introduction of the Euclidean structure on \( \mathcal{S} \) will allow us to define the adjoint of \( {\varphi }_{A} \) . Since

\[
\forall S, T \in  \mathcal{S},\;\left( {{\varphi }_{A}\left( S\right)  \mid  T}\right)  = \operatorname{tr}\left( {{}^{\mathrm{t}}{ASAT}}\right)  = \operatorname{tr}\left( {A{T}^{\mathrm{t}}{AS}}\right)  = \left( {{\varphi }_{{}^{\mathrm{t}}A}\left( T\right)  \mid  S}\right) ,
\]

l’adjoint \( {\varphi }_{A}^{ * } \) de \( {\varphi }_{A} \) est \( {\varphi }_{{}^{t}A} \) . Maintenant, on remarque que \( {\varphi }_{A}^{ * } \circ {\varphi }_{A} = {\varphi }_{{}^{t}A} \circ {\varphi }_{A} = {\varphi }_{{A}^{ \dagger }A} \) . La formule

> the adjoint \( {\varphi }_{A}^{ * } \) of \( {\varphi }_{A} \) is \( {\varphi }_{{}^{t}A} \) . Now, we note that \( {\varphi }_{A}^{ * } \circ {\varphi }_{A} = {\varphi }_{{}^{t}A} \circ {\varphi }_{A} = {\varphi }_{{A}^{ \dagger }A} \) . The formula

\[
{\left( \det {\varphi }_{A}\right) }^{2} = \det {\varphi }_{A}^{ * }\det {\varphi }_{A} = \det \left( {{\varphi }_{A}^{ * }{\varphi }_{A}}\right)  = \det {\varphi }_{A}{}^{\mathrm{t}}A
\]

va nous permettre de trouver la valeur de \( \left| {\det {\varphi }_{A}}\right| \) . Posons \( M = {A}^{\mathrm{t}}A \) . C’est une matrice symé- trique, donc diagonalisable, de sorte qu’il existe une matrice orthogonale \( P \) telle que \( M = {}^{\mathrm{t}}{PDP} \) , où \( D \) est une matrice diagonale. On vérifie facilement que \( {\varphi }_{M} = {\varphi }_{P} \circ {\varphi }_{D} \circ {\varphi }_{{}^{\mathrm{t}}P} \) . Comme \( {\varphi }_{P} \circ {\varphi }_{{}^{\mathrm{t}}P} = {\varphi }_{{}^{\mathrm{t}}{PP}} = {\operatorname{Id}}_{\mathcal{S}},{\varphi }_{M} \) est semblable à \( {\varphi }_{D} \) donc det \( {\varphi }_{M} = \det {\varphi }_{D} = {\left( \det D\right) }^{n + 1} \) d’après (*). Comme det \( D = \det M = {\left( \det A\right) }^{2} \) , ceci s’écrit aussi

> will allow us to find the value of \( \left| {\det {\varphi }_{A}}\right| \) . Let us set \( M = {A}^{\mathrm{t}}A \) . It is a symmetric matrix, therefore diagonalizable, so there exists an orthogonal matrix \( P \) such that \( M = {}^{\mathrm{t}}{PDP} \) , where \( D \) is a diagonal matrix. We easily verify that \( {\varphi }_{M} = {\varphi }_{P} \circ {\varphi }_{D} \circ {\varphi }_{{}^{\mathrm{t}}P} \) . Since \( {\varphi }_{P} \circ {\varphi }_{{}^{\mathrm{t}}P} = {\varphi }_{{}^{\mathrm{t}}{PP}} = {\operatorname{Id}}_{\mathcal{S}},{\varphi }_{M} \) is similar to \( {\varphi }_{D} \) , then det \( {\varphi }_{M} = \det {\varphi }_{D} = {\left( \det D\right) }^{n + 1} \) according to (*). Since det \( D = \det M = {\left( \det A\right) }^{2} \) , this can also be written

\[
{\left( \det {\varphi }_{A}\right) }^{2} = \det {\varphi }_{M} = {\left( \det A\right) }^{2\left( {n + 1}\right) },
\]

d'où le résultat.

> hence the result.

Problem 3. a) Soit \( H \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une matrice hermitienne positive. On note \( \Gamma \) l’ensemble des matrices hermitiennes positives A telles que det \( A \geq 1 \) . Montrer

> Problem 3. a) Let \( H \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a positive Hermitian matrix. Let \( \Gamma \) denote the set of positive Hermitian matrices A such that det \( A \geq 1 \) . Show

\[
\mathop{\inf }\limits_{{A \in  \Gamma }}\operatorname{tr}\left( {AH}\right)  = n{\left( \det H\right) }^{1/n}.
\]

(On pourra utiliser l'inégalité de la question a) de l'exercice 4 page 277).

> (One may use the inequality from question a) of exercise 4 on page 277).

b) En déduire que pour deux matrices hermitiennes positives \( A \) et \( B \) , on a

> b) Deduce that for two positive Hermitian matrices \( A \) and \( B \) , we have

\[
{\left\lbrack  \det \left( A + B\right) \right\rbrack  }^{1/n} \geq  {\left( \det A\right) }^{1/n} + {\left( \det B\right) }^{1/n}.
\]

Retrouver ce résultat sans utiliser la question a).

> Recover this result without using question a).

Solution. a) Commençons par montrer que pour toute matrice \( A \in \Gamma ,\operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n} \) . Le problème étant invariant par changement de base orthonormale, on peut supposer \( H \) diagonale. Notons \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) les coefficients diagonaux de \( H \) et considérons \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \Gamma \) . On a \( \operatorname{tr}\left( {AH}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{a}_{i, i} \) . Le logarithme étant une fonction concave, on peut écrire

> Solution. a) Let us begin by showing that for any matrix \( A \in \Gamma ,\operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n} \) . Since the problem is invariant under a change of orthonormal basis, we can assume \( H \) is diagonal. Let \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) denote the diagonal coefficients of \( H \) and consider \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \Gamma \) . We have \( \operatorname{tr}\left( {AH}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{a}_{i, i} \) . Since the logarithm is a concave function, we can write

\[
\frac{1}{n}\left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\lambda }_{i}{a}_{i, i}}\right) }\right\rbrack   \geq  {\left\lbrack  \mathop{\prod }\limits_{{i = 1}}^{n}\left( {\lambda }_{i}{a}_{i, i}\right) \right\rbrack  }^{1/n} = {\left( \det H\right) }^{1/n}{\left( \mathop{\prod }\limits_{{i = 1}}^{n}{a}_{i, i}\right) }^{1/n},
\]

et comme \( 1 \leq \det A \leq \mathop{\prod }\limits_{{i = 1}}^{n}{a}_{i, i} \) d’après la question a) de l’exercice 4 page 277, ceci implique \( \operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n}. \)

> and since \( 1 \leq \det A \leq \mathop{\prod }\limits_{{i = 1}}^{n}{a}_{i, i} \) according to question a) of exercise 4 on page 277, this implies \( \operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n}. \)

Achevons notre raisonnement. Nous venons de montrer que \( \mathop{\inf }\limits_{{A \in \Gamma }}\operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n} \) . Il s'agit maintenant de prouver l'inégalité réciproque. Il y a deux cas.

> Let us complete our reasoning. We have just shown that \( \mathop{\inf }\limits_{{A \in \Gamma }}\operatorname{tr}\left( {AH}\right) \geq n{\left( \det H\right) }^{1/n} \) . We must now prove the reciprocal inequality. There are two cases.

Premier cas. Si \( H \) est définie, alors pour tout \( i,{\lambda }_{i} > 0 \) . Soit \( A \) la matrice définie par

> First case. If \( H \) is definite, then for all \( i,{\lambda }_{i} > 0 \) . Let \( A \) be the matrix defined by

\[
A = {\left( \det H\right) }^{1/n}\left( \begin{matrix} {\lambda }_{1}^{-1} & & 0 \\   &  \ddots  & \\  0 & & {\lambda }_{n}^{-1} \end{matrix}\right) .
\]

On a \( A \in \Gamma \) , et \( \operatorname{tr}\left( {AH}\right) = \operatorname{tr}\left\lbrack {{\left( \det H\right) }^{1/n}{I}_{n}}\right\rbrack = n{\left( \det H\right) }^{1/n} \) , d’où le résultat.

> We have \( A \in \Gamma \) , and \( \operatorname{tr}\left( {AH}\right) = \operatorname{tr}\left\lbrack {{\left( \det H\right) }^{1/n}{I}_{n}}\right\rbrack = n{\left( \det H\right) }^{1/n} \) , hence the result.

Second cas. Si la matrice \( H \) n’est pas définie, l’une au moins des valeurs propres \( {\lambda }_{i} \) est nulle, par exemple \( {\lambda }_{n} = 0 \) . Pour tout \( p \in {\mathbb{N}}^{ * } \) , on définit

> Second case. If the matrix \( H \) is not definite, at least one of the eigenvalues \( {\lambda }_{i} \) is zero, for example \( {\lambda }_{n} = 0 \) . For all \( p \in {\mathbb{N}}^{ * } \) , we define

\[
{A}_{p} = \left( \begin{matrix} {p}^{-1} & & & 0 \\   &  \ddots  & & \\   & 0 & & {p}^{-1} \end{matrix}\right)  \in  \Gamma .
\]

On a \( \operatorname{tr}\left( {{A}_{p}H}\right) = \frac{\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{\lambda }_{i}}{p} \) , donc \( \mathop{\lim }\limits_{{p \rightarrow \infty }}\operatorname{tr}\left( {{A}_{p}H}\right) = 0 = n{\left( \det H\right) }^{1/n} \) , ce qui prouve le résultat.

> We have \( \operatorname{tr}\left( {{A}_{p}H}\right) = \frac{\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{\lambda }_{i}}{p} \) , therefore \( \mathop{\lim }\limits_{{p \rightarrow \infty }}\operatorname{tr}\left( {{A}_{p}H}\right) = 0 = n{\left( \det H\right) }^{1/n} \) , which proves the result.

b) Pour toute matrice \( M \in \Gamma \) , on a

> b) For any matrix \( M \in \Gamma \) , we have

\[
\operatorname{tr}\left\lbrack  {\left( {A + B}\right) M}\right\rbrack   = \operatorname{tr}\left( {AM}\right)  + \operatorname{tr}\left( {BM}\right)  \geq  \mathop{\inf }\limits_{{M \in  \Gamma }}\operatorname{tr}\left( {AM}\right)  + \mathop{\inf }\limits_{{M \in  \Gamma }}\operatorname{tr}\left( {BM}\right) ,
\]

donc

> therefore

\[
\mathop{\inf }\limits_{{M \in  \Gamma }}\operatorname{tr}\left\lbrack  {\left( {A + B}\right) M}\right\rbrack   \geq  \mathop{\inf }\limits_{{M \in  \Gamma }}\operatorname{tr}\left( {AM}\right)  + \mathop{\inf }\limits_{{M \in  \Gamma }}\operatorname{tr}\left( {BM}\right)
\]

ce qui prouve le résultat en vertu de la question a).

> which proves the result by virtue of question a).

- Résolvons la question sans l’aide de a). Si \( A \) et \( B \) ne sont pas définies, c’est évident car \( \det A = \det B = 0 \) et comme \( A + B \) est positive, \( \det \left( {A + B}\right)  \geq  0 \) . Sinon, l’une des matrices \( A \) ou \( B \) est définie. Supposons par exemple \( A \) définie. Le corollaire 3 page 257 assure l’existence d’une matrice inversible \( P \) telle que \( A = {P}^{ * }P \) et \( B = {P}^{ * }{DP} \) , où \( D \) est une matrice diagonale. Ainsi, on se ramène à montrer que

> - Let us solve the question without the help of a). If \( A \) and \( B \) are not definite, it is obvious because \( \det A = \det B = 0 \) and since \( A + B \) is positive, \( \det \left( {A + B}\right)  \geq  0 \) . Otherwise, one of the matrices \( A \) or \( B \) is definite. Suppose for example \( A \) is definite. Corollary 3 on page 257 ensures the existence of an invertible matrix \( P \) such that \( A = {P}^{ * }P \) and \( B = {P}^{ * }{DP} \) , where \( D \) is a diagonal matrix. Thus, we reduce the problem to showing that

\[
{\left\lbrack  \det \left( {I}_{n} + D\right) \right\rbrack  }^{1/n} \geq  {\left( \det {I}_{n}\right) }^{1/n} + {\left( \det D\right) }^{1/n}.
\]

En notant \( {\lambda }_{i} \geq 0 \) les termes de la diagonale principale de \( D \) , cette inégalité s’écrit

> By denoting \( {\lambda }_{i} \geq 0 \) as the terms of the main diagonal of \( D \), this inequality is written

\[
{\left\lbrack  \mathop{\prod }\limits_{{i = 1}}^{n}\left( 1 + {\lambda }_{i}\right) \right\rbrack  }^{1/n} \geq  1 + {\left( \mathop{\prod }\limits_{{i = 1}}^{n}{\lambda }_{i}\right) }^{1/n}.
\]

(*)

> Nous allons prouver (*) en utilisant des critères de convexité. Considérons l'application

We will prove (*) using convexity criteria. Let us consider the mapping

\[
\varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  {\left\lbrack  \mathop{\prod }\limits_{{i = 1}}^{n}\left( t + {\lambda }_{i}\right) \right\rbrack  }^{1/n}.
\]

Il s’agit de montrer \( \varphi \left( 1\right) - \varphi \left( 0\right) \geq 1 \) , ce qui sera vrai si on prouve \( {\varphi }^{\prime }\left( t\right) \geq 1 \) pour \( \left. {t \in \rbrack 0,1}\right\rbrack \) . On a

> It is a matter of showing \( \varphi \left( 1\right) - \varphi \left( 0\right) \geq 1 \), which will be true if we prove \( {\varphi }^{\prime }\left( t\right) \geq 1 \) for \( \left. {t \in \rbrack 0,1}\right\rbrack \). We have

\[
\forall t \in  \rbrack 0,1\rbrack ,\;{\varphi }^{\prime }\left( t\right)  = \frac{1}{n}{\left\lbrack  \mathop{\prod }\limits_{{i = 1}}^{n}\left( t + {\lambda }_{i}\right) \right\rbrack  }^{1/n}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{t + {\lambda }_{i}}}\right) ,
\]

ou encore

> or also

\[
\forall t \in  \rbrack 0,1\rbrack ,\;\log {\varphi }^{\prime }\left( t\right)  = \log \left( {\frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{t + {\lambda }_{i}}}\right)  - \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}\log \frac{1}{t + {\lambda }_{i}},
\]

donc, en vertu de la concavité du logarithme, \( \log {\varphi }^{\prime }\left( t\right) \geq 0 \) , c’est à dire \( \left. {{\varphi }^{\prime }\left( t\right) \geq 1\text{ pour }t \in }\right\rbrack 0,1\rbrack \) , d'où le résultat.

> therefore, by virtue of the concavity of the logarithm, \( \log {\varphi }^{\prime }\left( t\right) \geq 0 \), that is to say \( \left. {{\varphi }^{\prime }\left( t\right) \geq 1\text{ pour }t \in }\right\rbrack 0,1\rbrack \), hence the result.

Remarque. Notez l'utilisation fructueuse du corollaire 3 page 257 dans la preuve directe de la question b).

> Remark. Note the fruitful use of corollary 3 on page 257 in the direct proof of question b).

Problem 4. Soit \( \left( {E,\parallel .\parallel }\right) \) un espace euclidien et \( u \) un projecteur de \( E \) tel que \( \parallel u\parallel \leq 1 \) (en notant \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) , norme d’algèbre sur \( \mathcal{L}\left( E\right) \) ). Montrer que \( u \) est un projecteur orthogonal.

> Problem 4. Let \( \left( {E,\parallel .\parallel }\right) \) be a Euclidean space and \( u \) a projector of \( E \) such that \( \parallel u\parallel \leq 1 \) (denoting \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \), the algebra norm on \( \mathcal{L}\left( E\right) \)). Show that \( u \) is an orthogonal projector.

Solution. Il s’agit de montrer que Ker \( u \) et Im \( u \) sont orthogonaux. Soit \( x \in \operatorname{Ker}u \) et \( y \in \operatorname{Im}u \) . Pour tout \( t \in \mathbb{R} \) , on a \( u\left( {y + {tx}}\right) = u\left( y\right) = y \) , et comme par hypothèse \( \parallel u\left( {y + {tx}}\right) \parallel \leq \parallel y + {tx}\parallel \) , on a

> Solution. It is a matter of showing that Ker \( u \) and Im \( u \) are orthogonal. Let \( x \in \operatorname{Ker}u \) and \( y \in \operatorname{Im}u \). For any \( t \in \mathbb{R} \), we have \( u\left( {y + {tx}}\right) = u\left( y\right) = y \), and since by hypothesis \( \parallel u\left( {y + {tx}}\right) \parallel \leq \parallel y + {tx}\parallel \), we have

\[
\forall t \in  \mathbb{R},\;\parallel y{\parallel }^{2} = \parallel u\left( {y + {tx}}\right) {\parallel }^{2} \leq  \parallel y + {tx}{\parallel }^{2} = \parallel y{\parallel }^{2} + {2t}\left( {x \cdot  y}\right)  + {t}^{2}\parallel x{\parallel }^{2}.
\]

Cette inégalité exprime que la fonction \( t \mapsto \parallel y{\parallel }^{2} + {2t}\left( {x \cdot y}\right) + {t}^{2}\parallel x{\parallel }^{2} \) atteint son minimum pour \( t = 0 \) . Sa dérivée en 0 est donc nulle, ce qui s’écrit \( x \cdot y = 0 \) . Ceci étant vrai pour tout \( x \in \operatorname{Ker}u \) et pour tout \( y \in \operatorname{Im}u \) , on en déduit que Ker \( u \) et \( \operatorname{Im}u \) sont orthogonaux.

> This inequality expresses that the function \( t \mapsto \parallel y{\parallel }^{2} + {2t}\left( {x \cdot y}\right) + {t}^{2}\parallel x{\parallel }^{2} \) reaches its minimum for \( t = 0 \). Its derivative at 0 is therefore zero, which is written \( x \cdot y = 0 \). Since this is true for any \( x \in \operatorname{Ker}u \) and for any \( y \in \operatorname{Im}u \), we deduce that Ker \( u \) and \( \operatorname{Im}u \) are orthogonal.

Remarque. Tout projecteur non nul \( u \) vérifie \( \parallel u\parallel \geq 1 \) . En effet, on a \( {u}^{2} = u \) donc \( \parallel u\parallel = \begin{Vmatrix}{u}^{2}\end{Vmatrix} \leq \parallel u{\parallel }^{2} \) , et le résultat car \( \parallel u\parallel \neq 0 \) . Un projecteur orthogonal non nul \( u \) vérifie \( \parallel u\parallel = 1. \)

> Remark. Any non-zero projector \( u \) satisfies \( \parallel u\parallel \geq 1 \). Indeed, we have \( {u}^{2} = u \) therefore \( \parallel u\parallel = \begin{Vmatrix}{u}^{2}\end{Vmatrix} \leq \parallel u{\parallel }^{2} \), and the result because \( \parallel u\parallel \neq 0 \). A non-zero orthogonal projector \( u \) satisfies \( \parallel u\parallel = 1. \)

PROBLÉME 5. Déterminer les matrices hermitiennes positives \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) à coefficients \( {a}_{i, j} \) tous non nuls, telles que la matrice \( B = {\left( 1/{a}_{i, j}\right) }_{1 \leq i, j \leq n} \) est aussi hermitienne positive.

> PROBLEM 5. Determine the positive Hermitian matrices \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) with all non-zero coefficients \( {a}_{i, j} \) such that the matrix \( B = {\left( 1/{a}_{i, j}\right) }_{1 \leq i, j \leq n} \) is also positive Hermitian.

Solution. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) une telle matrice. D’après la proposition 3 page 274, \( A \) est une matrice de Gram, c’est-à-dire qu’il existe \( n \) vecteurs \( {u}_{1},\ldots ,{u}_{n} \) de \( {\mathbb{C}}^{n} \) tels que \( \forall i, j,{a}_{i, j} = {u}_{i} \cdot {u}_{j} \) . D'après, l'inégalité de Schwarz, on a donc

> Solution. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) be such a matrix. According to proposition 3 on page 274, \( A \) is a Gram matrix, meaning there exist \( n \) vectors \( {u}_{1},\ldots ,{u}_{n} \) in \( {\mathbb{C}}^{n} \) such that \( \forall i, j,{a}_{i, j} = {u}_{i} \cdot {u}_{j} \) . According to the Schwarz inequality, we therefore have

\[
\forall i, j,\;{\left| {a}_{i, j}\right| }^{2} = {\left| {u}_{i} \cdot  {u}_{j}\right| }^{2} \leq  {\begin{Vmatrix}{u}_{i}\end{Vmatrix}}^{2}{\begin{Vmatrix}{u}_{j}\end{Vmatrix}}^{2} = {a}_{i, i}{a}_{j, j}.
\]

Cette inégalité, vraie pour toute matrice positive, l’est également pour la matrice \( B \) , ce qui s’écrit

> This inequality, true for any positive matrix, is also true for the matrix \( B \) , which is written as

\[
\forall i, j,\;\frac{1}{{\left| {a}_{i, j}\right| }^{2}} \leq  \frac{1}{{a}_{i, i}}\frac{1}{{a}_{j, j}}.
\]

On en déduit que \( {\left| {a}_{i, j}\right| }^{2} = {a}_{i, i}{a}_{j, j} \) pour tout \( i, j \) . Il y a donc égalité de Schwarz \( \left| {{u}_{i} \cdot {u}_{j}}\right| = \begin{Vmatrix}{u}_{i}\end{Vmatrix} \cdot \begin{Vmatrix}{u}_{j}\end{Vmatrix} \) , donc \( {u}_{i} \) et \( {u}_{j} \) sont liés. Ceci étant vrai pour tout \( i, j \) , le rang des vecteurs \( {u}_{1},\ldots ,{u}_{n} \) est 1 (ces vecteurs sont non nuls car \( A \neq 0 \) ). Ceci suffit pour affirmer \( \operatorname{rg}A = 1 \) .

> We deduce that \( {\left| {a}_{i, j}\right| }^{2} = {a}_{i, i}{a}_{j, j} \) for all \( i, j \) . There is therefore equality in Schwarz \( \left| {{u}_{i} \cdot {u}_{j}}\right| = \begin{Vmatrix}{u}_{i}\end{Vmatrix} \cdot \begin{Vmatrix}{u}_{j}\end{Vmatrix} \) , so \( {u}_{i} \) and \( {u}_{j} \) are linearly dependent. Since this is true for all \( i, j \) , the rank of the vectors \( {u}_{1},\ldots ,{u}_{n} \) is 1 (these vectors are non-zero because \( A \neq 0 \) ). This is sufficient to state \( \operatorname{rg}A = 1 \) .

Réciproquement supposons \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) hermitienne positive, de rang 1 et telle que \( {a}_{i, j} \neq 0 \) pour tout \( i, j \) . La signature de la forme quadratique \( X \mapsto {X}^{ * }{AX} \) est \( \left( {1,0}\right) \) , il existe donc une forme linéaire \( f\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{x}_{i} \) telle que

> Conversely, assume \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) is a positive Hermitian matrix of rank 1 such that \( {a}_{i, j} \neq 0 \) for all \( i, j \) . The signature of the quadratic form \( X \mapsto {X}^{ * }{AX} \) is \( \left( {1,0}\right) \) , so there exists a linear form \( f\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{x}_{i} \) such that

\[
\forall X,\;\mathop{\sum }\limits_{{i, j}}{a}_{i, j}\overline{{x}_{i}}{x}_{j} = {X}^{ * }{AX} = {\left| f\left( X\right) \right| }^{2} = \mathop{\sum }\limits_{{i, j}}\left( {\overline{{\lambda }_{i}}{\lambda }_{j}}\right) \overline{{x}_{i}}{x}_{j}.
\]

Ceci prouve que \( {a}_{i, j} = \overline{{\lambda }_{i}}{\lambda }_{j} \) pour tout \( i, j \) . On en déduit

> This proves that \( {a}_{i, j} = \overline{{\lambda }_{i}}{\lambda }_{j} \) for all \( i, j \) . We deduce

\[
B = {\left( \frac{1}{{a}_{i, j}}\right) }_{\begin{matrix} {1 \leq  i \leq  n} \\  {1 \leq  j \leq  n} \end{matrix}} = {\left\lbrack  \left( \frac{1}{\overline{{\lambda }_{i}}}\right) \left( \frac{1}{{\lambda }_{j}}\right) \right\rbrack  }_{\begin{matrix} {1 \leq  i \leq  n} \\  {1 \leq  j \leq  n} \end{matrix}}\;\text{ et }\;\forall X,\;{X}^{ * }{BX} = {\left| \mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{{\lambda }_{i}}{x}_{i}\right| }^{2} \geq  0.
\]

Ainsi, la matrice \( B \) est positive.

> Thus, the matrix \( B \) is positive.

En conclusion, les matrices positives cherchées sont celles à coefficients tous non nuls et de rang 1 .

> In conclusion, the positive matrices sought are those with all non-zero coefficients and rank 1.

PROBLEME 6. a) Montrer que si le coefficient diagonal d’indice \( \left( {i, i}\right) \) d’une matrice symé- trique positive \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est nul, alors la \( i \) -ième ligne de \( A \) est nulle.

> PROBLEM 6. a) Show that if the diagonal coefficient with index \( \left( {i, i}\right) \) of a positive symmetric matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is zero, then the \( i \) -th row of \( A \) is zero.

b) Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice symétrique positive. On écrit la matrice \( M \) sous la forme \( M = \left( \begin{matrix} A & B \\ {}^{\mathrm{t}}B & C \end{matrix}\right) \) avec \( A \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \left( {1 \leq p < n}\right) \) . Montrer que \( N = \left( \begin{matrix} A & B \\ 0 & 0 \end{matrix}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est diagonalisable.

> b) Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a positive symmetric matrix. We write the matrix \( M \) in the form \( M = \left( \begin{matrix} A & B \\ {}^{\mathrm{t}}B & C \end{matrix}\right) \) with \( A \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \left( {1 \leq p < n}\right) \) . Show that \( N = \left( \begin{matrix} A & B \\ 0 & 0 \end{matrix}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is diagonalizable.

Solution. a) Comme \( A \) est symétrique positive, \( A \) s’écrit comme la matrice de Gram de \( n \) vecteurs \( {u}_{1},\ldots ,{u}_{n} \) de \( {\mathbb{R}}^{n} \) . Le coefficient d’indice \( \left( {i, j}\right) \) de \( A \) vérifie donc \( {a}_{i, j} = {u}_{i} \cdot {u}_{j} \) pour tout \( \left( {i, j}\right) \) . Ainsi, si \( {a}_{i, i} = 0 \) on a \( {\begin{Vmatrix}{u}_{i}\end{Vmatrix}}^{2} = {a}_{i, i} = 0 \) donc \( {u}_{i} = 0 \) , donc \( {a}_{i, j} = {u}_{i} \cdot {u}_{j} = 0 \) pour tout \( j \) .

> Solution. a) Since \( A \) is positive symmetric, \( A \) can be written as the Gram matrix of \( n \) vectors \( {u}_{1},\ldots ,{u}_{n} \) of \( {\mathbb{R}}^{n} \) . The coefficient with index \( \left( {i, j}\right) \) of \( A \) therefore satisfies \( {a}_{i, j} = {u}_{i} \cdot {u}_{j} \) for all \( \left( {i, j}\right) \) . Thus, if \( {a}_{i, i} = 0 \) we have \( {\begin{Vmatrix}{u}_{i}\end{Vmatrix}}^{2} = {a}_{i, i} = 0 \) so \( {u}_{i} = 0 \) , therefore \( {a}_{i, j} = {u}_{i} \cdot {u}_{j} = 0 \) for all \( j \) .

b) Nous nous ramenons d’abord au cas où \( A \) est diagonale. Comme \( M \) est symétrique positive, \( A \) l’est également donc il existe une matrice orthogonale \( P \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) telle que \( D = {}^{\mathrm{t}}{PAP} \) soit une matrice diagonale. Quitte à changer l’ordre des vecteurs colonnes de \( P \) , on peut même supposer que les éventuels termes nuls de la diagonale de \( D \) sont les derniers (ce choix sera utile par la suite). Notons \( q = n - p \) et \( U = \left( \begin{matrix} P & 0 \\ 0 & {I}_{q} \end{matrix}\right) \) . La matrice \( U \) est orthogonale et un produit par blocs donne

> b) We first reduce to the case where \( A \) is diagonal. Since \( M \) is positive symmetric, \( A \) is as well, so there exists an orthogonal matrix \( P \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) such that \( D = {}^{\mathrm{t}}{PAP} \) is a diagonal matrix. By reordering the column vectors of \( P \) if necessary, we can even assume that any zero terms on the diagonal of \( D \) are the last ones (this choice will be useful later). Let \( q = n - p \) and \( U = \left( \begin{matrix} P & 0 \\ 0 & {I}_{q} \end{matrix}\right) \) . The matrix \( U \) is orthogonal and a block product gives

\[
{}^{\mathrm{t}}{UMU} = \left( \begin{matrix} D & {}^{\mathrm{t}}{PB} \\  {}^{\mathrm{t}}{BP} & C \end{matrix}\right) \;\text{ et }\;{}^{\mathrm{t}}{UNU} = \left( \begin{matrix} D & {}^{\mathrm{t}}{PB} \\  0 & 0 \end{matrix}\right) .
\]

La matrice \( {}^{\mathrm{t}}{UMU} \) est congrue à \( M \) , donc positive. Donc d’après la question a), pour chaque indice \( i \) tel que le \( i \) -ième coefficient diagonal de \( D \) est nul, toute la \( i \) -ième ligne de \( {}^{\mathrm{t}}{UMU} \) est nulle, en particulier la \( i \) -ième ligne de \( {}^{\mathrm{t}}{PB} \) est nulle. Par construction, les éventuels termes nuls de la diagonale de \( D \) sont les derniers. En désignant par \( r \) le nombre de coefficients non nuls de la diagonale de \( D \) , on voit donc que seules les \( r \) premières lignes de \( {}^{\mathrm{t}}{UNU} \) sont non nulles. En notant \( {D}^{\prime } \in {\mathcal{M}}_{r}\left( \mathbb{R}\right) \) la matrice formée des \( r \) premières lignes et colonnes de \( D \) , on voit donc que \( {}^{\mathrm{t}}{UNU} \) a la forme

> The matrix \( {}^{\mathrm{t}}{UMU} \) is congruent to \( M \) , and therefore positive. Thus, according to question a), for each index \( i \) such that the \( i \) -th diagonal coefficient of \( D \) is zero, the entire \( i \) -th row of \( {}^{\mathrm{t}}{UMU} \) is zero; in particular, the \( i \) -th row of \( {}^{\mathrm{t}}{PB} \) is zero. By construction, any zero terms on the diagonal of \( D \) are the last ones. By denoting \( r \) as the number of non-zero coefficients on the diagonal of \( D \) , we see that only the first \( r \) rows of \( {}^{\mathrm{t}}{UNU} \) are non-zero. By denoting \( {D}^{\prime } \in {\mathcal{M}}_{r}\left( \mathbb{R}\right) \) as the matrix formed by the first \( r \) rows and columns of \( D \) , we see that \( {}^{\mathrm{t}}{UNU} \) has the form

\[
{}^{\mathrm{t}}{UNU} = \left( \begin{matrix} {D}^{\prime } & E \\  0 & 0 \end{matrix}\right)
\]

(*)

> où \( E \) est une matrice à \( r \) lignes et \( n - r \) colonnes. Les \( r \) premiers vecteurs \( {e}_{1},\ldots ,{e}_{r} \) de la base canonique de \( {\mathbb{R}}^{n} \) sont des vecteurs propres de \( {}^{\mathrm{t}}{UNU} \) associés à des valeurs propres non nulles, et la forme de cette matrice montre que le rang de ses vecteurs lignes est \( r \) , donc son noyau est de dimension \( n - r \) . En désignant par \( {f}_{1},\ldots ,{f}_{n - r} \) une base de \( \operatorname{Ker}\left( {{}^{\mathrm{t}}{UNU}}\right) \) on voit facilement que \( \left( {{e}_{1},\ldots ,{e}_{r},{f}_{1},\ldots ,{f}_{n - r}}\right) \) est une base de vecteurs propres de \( {}^{\mathrm{t}}{UNU} \) . Ainsi \( {}^{\mathrm{t}}{UNU} \) est diagonalisable, et comme \( U \) est une matrice orthogonale ceci entraîne que \( N \) est diagonalisable.

where \( E \) is a matrix with \( r \) rows and \( n - r \) columns. The first \( r \) vectors \( {e}_{1},\ldots ,{e}_{r} \) of the canonical basis of \( {\mathbb{R}}^{n} \) are eigenvectors of \( {}^{\mathrm{t}}{UNU} \) associated with non-zero eigenvalues, and the form of this matrix shows that the rank of its row vectors is \( r \), so its kernel has dimension \( n - r \). By denoting by \( {f}_{1},\ldots ,{f}_{n - r} \) a basis of \( \operatorname{Ker}\left( {{}^{\mathrm{t}}{UNU}}\right) \), one easily sees that \( \left( {{e}_{1},\ldots ,{e}_{r},{f}_{1},\ldots ,{f}_{n - r}}\right) \) is a basis of eigenvectors of \( {}^{\mathrm{t}}{UNU} \). Thus \( {}^{\mathrm{t}}{UNU} \) is diagonalizable, and since \( U \) is an orthogonal matrix, this implies that \( N \) is diagonalizable.

> Remarque. On peut aussi montrer directement que la matrice de droite dans (*) est diagonalisable grâce à la formule \( \left( \begin{matrix} I & {D}^{\prime } & - I & E \\ 0 & I & I & 0 \end{matrix}\right) \left( \begin{matrix} {D}^{\prime } & E \\ 0 & 0 \end{matrix}\right) {\left( \begin{matrix} I & {D}^{\prime } - I \\ 0 & I \end{matrix}\right) }^{-1} = \left( \begin{matrix} {D}^{\prime } & 0 \\ 0 & 0 \end{matrix}\right) \) .

Remark. One can also show directly that the matrix on the right in (*) is diagonalizable using the formula \( \left( \begin{matrix} I & {D}^{\prime } & - I & E \\ 0 & I & I & 0 \end{matrix}\right) \left( \begin{matrix} {D}^{\prime } & E \\ 0 & 0 \end{matrix}\right) {\left( \begin{matrix} I & {D}^{\prime } - I \\ 0 & I \end{matrix}\right) }^{-1} = \left( \begin{matrix} {D}^{\prime } & 0 \\ 0 & 0 \end{matrix}\right) \).

> - Le résultat de la question b) est aussi une conséquence du résultat b) du problème 10 page 289 dans le cas particulier où \( A = \left( \begin{matrix} {I}_{p} & 0 \\  0 & 0 \end{matrix}\right) \) .

- The result of question b) is also a consequence of result b) of problem 10 on page 289 in the special case where \( A = \left( \begin{matrix} {I}_{p} & 0 \\  0 & 0 \end{matrix}\right) \).

> Problem 7 (RÉDUCTION DES MATRICES ANTISYMÉTRIQUES). 1/ Soit \( \mathbb{K} \) un corps commutatif de caractéristique différente de 2. a) Soit \( E \) un \( \mathbb{K} \) -espace vectoriel de dimension finie \( n \) et \( \varphi \) une forme bilinéaire antisymétrique sur \( E \) . Montrer qu’il existe une base \( B = {\left( {e}_{i}\right) }_{1 \leq i \leq n} \) de \( E \) et un entier \( r \leq n/2 \) tels que

Problem 7 (REDUCTION OF ANTISYMMETRIC MATRICES). 1/ Let \( \mathbb{K} \) be a commutative field with characteristic different from 2. a) Let \( E \) be a finite-dimensional \( \mathbb{K} \)-vector space \( n \) and \( \varphi \) an antisymmetric bilinear form on \( E \). Show that there exists a basis \( B = {\left( {e}_{i}\right) }_{1 \leq i \leq n} \) of \( E \) and an integer \( r \leq n/2 \) such that

\[
\forall \left( {x}_{i}\right) ,\left( {y}_{i}\right)  \in  {\mathbb{K}}^{n},\;\varphi \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i},\mathop{\sum }\limits_{{j = 1}}^{n}{y}_{j}{e}_{j}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}\left( {{x}_{{2k} - 1}{y}_{2k} - {x}_{2k}{y}_{{2k} - 1}}\right) .
\]

(*)

> b) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) une matrice antisymétrique. Montrer qu’il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) tel que

b) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be an antisymmetric matrix. Show that there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) such that

\[
{}^{\mathrm{t}}{PAP} = \left( \begin{matrix} J & & & & & \\   &  \ddots  & & & & \\   & & J & & & \\   & & & 0 & & \\   & & & &  \ddots  & \\   & & & & & 0 \end{matrix}\right) \;\text{ avec }\;J = \left( \begin{matrix} 0 & 1 \\   - 1 & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{2}\left( \mathbb{K}\right) .
\]

2/ Montrer que le déterminant d’une matrice antisymétrique \( A \) à coefficients entiers est le carré d'un entier.

> 2/ Show that the determinant of an antisymmetric matrix \( A \) with integer coefficients is the square of an integer.

Solution. 1/a) On procède par récurrence sur \( n = \dim E \) . Pour \( n = 1,\varphi \) est nulle et si \( n = 2 \) , le résultat est immédiat. Supposons donc \( n \geq 3 \) . Si \( \varphi = 0 \) le résultat est évident (dans ce cas \( r = 0 \) ), sinon il existe deux vecteurs \( {e}_{1} \) et \( {e}_{2} \) de \( E \) tels que \( \varphi \left( {{e}_{1},{e}_{2}}\right) \neq 0 \) . Quitte à multiplier \( {e}_{1} \) par \( 1/\varphi \left( {{e}_{1},{e}_{2}}\right) \) on peut supposer \( \varphi \left( {{e}_{1},{e}_{2}}\right) = 1 \) . Ces vecteurs sont forcément non nuls, et ils forment une famille libre car si \( {e}_{2} = \lambda {e}_{1} \) avec \( \lambda \in \mathbb{K} \) , on aurait \( \varphi \left( {{e}_{1},{e}_{2}}\right) = {\lambda \varphi }\left( {{e}_{1},{e}_{1}}\right) = 0 \) . Les formes linéaires \( {L}_{1} = \varphi \left( {{e}_{1}, \cdot }\right) \) et \( {L}_{2} = \varphi \left( {{e}_{2}, \cdot }\right) \) forment une famille libre car si \( {\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2} = 0 \) , alors \( 0 = \left( {{\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2}}\right) \left( {e}_{1}\right) = - {\lambda }_{2} \) , de même \( 0 = \left( {{\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2}}\right) \left( {e}_{2}\right) = {\lambda }_{1} \) . Donc le s.e.v \( F = \operatorname{Ker}{L}_{1} \cap \operatorname{Ker}{L}_{2} \) est de dimension \( n - 2 \) . D’après l’hypothèse de récurrence, on peut trouver une base \( \left( {{e}_{3},\ldots ,{e}_{n}}\right) \) de \( F \) et \( r \leq n/2 \) telle que la restriction \( \psi \) de \( \varphi \) à \( F \times F \) s’écrive

> Solution. 1/a) We proceed by induction on \( n = \dim E \) . For \( n = 1,\varphi \) it is zero and if \( n = 2 \) , the result is immediate. Let us therefore assume \( n \geq 3 \) . If \( \varphi = 0 \) the result is obvious (in this case \( r = 0 \) ), otherwise there exist two vectors \( {e}_{1} \) and \( {e}_{2} \) of \( E \) such that \( \varphi \left( {{e}_{1},{e}_{2}}\right) \neq 0 \) . By multiplying \( {e}_{1} \) by \( 1/\varphi \left( {{e}_{1},{e}_{2}}\right) \) if necessary, we can assume \( \varphi \left( {{e}_{1},{e}_{2}}\right) = 1 \) . These vectors are necessarily non-zero, and they form a linearly independent family because if \( {e}_{2} = \lambda {e}_{1} \) with \( \lambda \in \mathbb{K} \) , we would have \( \varphi \left( {{e}_{1},{e}_{2}}\right) = {\lambda \varphi }\left( {{e}_{1},{e}_{1}}\right) = 0 \) . The linear forms \( {L}_{1} = \varphi \left( {{e}_{1}, \cdot }\right) \) and \( {L}_{2} = \varphi \left( {{e}_{2}, \cdot }\right) \) form a linearly independent family because if \( {\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2} = 0 \) , then \( 0 = \left( {{\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2}}\right) \left( {e}_{1}\right) = - {\lambda }_{2} \) , likewise \( 0 = \left( {{\lambda }_{1}{L}_{1} + {\lambda }_{2}{L}_{2}}\right) \left( {e}_{2}\right) = {\lambda }_{1} \) . Thus the subspace \( F = \operatorname{Ker}{L}_{1} \cap \operatorname{Ker}{L}_{2} \) is of dimension \( n - 2 \) . According to the induction hypothesis, we can find a basis \( \left( {{e}_{3},\ldots ,{e}_{n}}\right) \) of \( F \) and \( r \leq n/2 \) such that the restriction \( \psi \) of \( \varphi \) to \( F \times F \) can be written

\[
\psi \left( {\mathop{\sum }\limits_{{i = 3}}^{n}{x}_{i}{e}_{i},\mathop{\sum }\limits_{{j = 3}}^{n}{y}_{i}{e}_{i}}\right)  = \mathop{\sum }\limits_{{i = 2}}^{r}\left( {{x}_{{2k} - 1}{y}_{2k} - {x}_{2k}{y}_{{2k} - 1}}\right) .
\]

\( \left( {* * }\right) \)

> Par ailleurs Vect \( \left( {{e}_{1},{e}_{2}}\right) \) est en somme directe avec \( F \) (si \( e = {\lambda }_{1}{e}_{1} + {\lambda }_{2}{e}_{2} \in F \) alors \( 0 = {L}_{2}\left( e\right) = \; {\lambda }_{1}\varphi \left( {{e}_{2},{e}_{1}}\right) + {\lambda }_{2}\varphi \left( {{e}_{2},{e}_{2}}\right) = - {\lambda }_{1} \) donc \( {\lambda }_{1} = 0 \) et de même \( \left. {0 = {L}_{1}\left( e\right) = {\lambda }_{2}}\right) \) , donc \( \left( {{e}_{1},{e}_{2},{e}_{3},\ldots ,{e}_{n}}\right) \) est une base de \( E \) . Par construction de \( F \) , on a \( \varphi \left( {x, y}\right) = \varphi \left( {y, x}\right) = 0 \) dès que \( x \in \operatorname{Vect}\left( {{e}_{1},{e}_{2}}\right) \) et \( y \in F \) , donc

Furthermore, Vect \( \left( {{e}_{1},{e}_{2}}\right) \) is in direct sum with \( F \) (if \( e = {\lambda }_{1}{e}_{1} + {\lambda }_{2}{e}_{2} \in F \) then \( 0 = {L}_{2}\left( e\right) = \; {\lambda }_{1}\varphi \left( {{e}_{2},{e}_{1}}\right) + {\lambda }_{2}\varphi \left( {{e}_{2},{e}_{2}}\right) = - {\lambda }_{1} \) so \( {\lambda }_{1} = 0 \) and likewise \( \left. {0 = {L}_{1}\left( e\right) = {\lambda }_{2}}\right) \) , so \( \left( {{e}_{1},{e}_{2},{e}_{3},\ldots ,{e}_{n}}\right) \) is a basis of \( E \) . By construction of \( F \) , we have \( \varphi \left( {x, y}\right) = \varphi \left( {y, x}\right) = 0 \) as soon as \( x \in \operatorname{Vect}\left( {{e}_{1},{e}_{2}}\right) \) and \( y \in F \) , therefore

\[
\varphi \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i},\mathop{\sum }\limits_{{j = 1}}^{n}{y}_{j}{e}_{j}}\right)  = \varphi \left( {{x}_{1}{e}_{1} + {x}_{2}{e}_{2},{y}_{1}{e}_{1} + {y}_{2}{e}_{2}}\right)  + \psi \left( {\mathop{\sum }\limits_{{i = 3}}^{n}{x}_{i}{e}_{i},\mathop{\sum }\limits_{{j = 3}}^{n}{y}_{j}{e}_{j}}\right) .
\]

Comme \( \varphi \left( {{x}_{1}{e}_{1} + {x}_{2}{e}_{2},{y}_{1}{e}_{1} + {y}_{2}{e}_{2}}\right) = {x}_{1}{y}_{2}\varphi \left( {{e}_{1},{e}_{2}}\right) + {x}_{2}{y}_{1}\varphi \left( {{e}_{2},{e}_{1}}\right) = {x}_{1}{y}_{2} - {x}_{2}{y}_{1} \) , on en déduit avec \( \left( {* * }\right) \) le résultat au rang \( n \) .

> As \( \varphi \left( {{x}_{1}{e}_{1} + {x}_{2}{e}_{2},{y}_{1}{e}_{1} + {y}_{2}{e}_{2}}\right) = {x}_{1}{y}_{2}\varphi \left( {{e}_{1},{e}_{2}}\right) + {x}_{2}{y}_{1}\varphi \left( {{e}_{2},{e}_{1}}\right) = {x}_{1}{y}_{2} - {x}_{2}{y}_{1} \), we deduce the result at rank \( n \) with \( \left( {* * }\right) \).

b) Soit \( \varphi \) la forme bilinéaire sur \( {\mathbb{K}}^{n} \) dont \( A \) est la matrice dans la base canonique \( \mathcal{B} \) de \( {\mathbb{K}}^{n} \) . La question précédente assure l’existence d’une base \( {\mathcal{B}}^{\prime } = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) et de \( r \leq n/2 \) dans laquelle \( \varphi \) s’écrive sous la forme \( \left( *\right) \) . En d’autres termes, la matrice \( M \) de \( \varphi \) dans la base \( {\mathcal{B}}^{\prime } \) est formée de \( r \) matrices \( J \) sur sa diagonale et de zéros partout ailleurs. En désignant par \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) la matrice de passage de la base \( \mathcal{B} \) à la base \( {\mathcal{B}}^{\prime } \) , on a donc \( {}^{\mathrm{t}}{PAP} = M \) , d’où le résultat.

> b) Let \( \varphi \) be the bilinear form on \( {\mathbb{K}}^{n} \) whose matrix in the canonical basis \( \mathcal{B} \) of \( {\mathbb{K}}^{n} \) is \( A \). The previous question ensures the existence of a basis \( {\mathcal{B}}^{\prime } = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) and \( r \leq n/2 \) in which \( \varphi \) is written in the form \( \left( *\right) \). In other words, the matrix \( M \) of \( \varphi \) in the basis \( {\mathcal{B}}^{\prime } \) is formed by \( r \) matrices \( J \) on its diagonal and zeros everywhere else. By denoting \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) as the transition matrix from basis \( \mathcal{B} \) to basis \( {\mathcal{B}}^{\prime } \), we have \( {}^{\mathrm{t}}{PAP} = M \), hence the result.

2 / Les coefficients de \( A \) sont dans le corps \( \mathbb{K} = \mathbb{Q} \) , donc la question précédente assure l’existence de \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{Q}\right) \) telle que \( {}^{\mathrm{t}}{PAP} = M \) où \( M \) est constituée de \( r \) matrices \( J \) sur sa diagonale et de zéros partout ailleurs. Si \( M \) a au moins un zéro sur la diagonale, alors det \( M = 0 \) donc det \( A = 0 \) donc det \( A = 0 \) est bien le carré d’un entier. Sinon, det \( M = {\left( \det J\right) }^{r} = 1 \) donc \( \det A = 1/{\left( \det P\right) }^{2} \) . Comme \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{Q}\right) \) on a det \( P \in \mathbb{Q} \) , donc det \( A \) est le carré d’un nombre rationnel. Comme \( A \) a des coefficients entiers, det \( A \) est un entier. Un entier qui est le carré d'un rationnel est forcément le carré d'un entier, donc det \( A \) est bien le carré d'un entier.

> 2 / The coefficients of \( A \) are in the field \( \mathbb{K} = \mathbb{Q} \), so the previous question ensures the existence of \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{Q}\right) \) such that \( {}^{\mathrm{t}}{PAP} = M \) where \( M \) consists of \( r \) matrices \( J \) on its diagonal and zeros everywhere else. If \( M \) has at least one zero on the diagonal, then det \( M = 0 \) so det \( A = 0 \) so det \( A = 0 \) is indeed the square of an integer. Otherwise, det \( M = {\left( \det J\right) }^{r} = 1 \) so \( \det A = 1/{\left( \det P\right) }^{2} \). As \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{Q}\right) \) we have det \( P \in \mathbb{Q} \), so det \( A \) is the square of a rational number. Since \( A \) has integer coefficients, det \( A \) is an integer. An integer that is the square of a rational is necessarily the square of an integer, so det \( A \) is indeed the square of an integer.

Remarque. Lorsque \( \mathbb{K} = \mathbb{R} \) , ce résultat (bien que légèrement différent) est plus faible que le théorème 6 page 273, mais il présente l'intérêt d'être vrai sur d'autres corps K.

> Remark. When \( \mathbb{K} = \mathbb{R} \), this result (although slightly different) is weaker than theorem 6 on page 273, but it has the advantage of being true over other fields K.

PROBLÉME 8 (PFAFFIEN). Soit \( \mathbb{K} \) un corps commutatif de caractéristique différente de 2. On désigne par \( {\mathcal{A}}_{n}\left( \mathbb{K}\right) \) l’e.v des matrices antisymétriques de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> PROBLEM 8 (PFAFFIAN). Let \( \mathbb{K} \) be a commutative field of characteristic other than 2. We denote by \( {\mathcal{A}}_{n}\left( \mathbb{K}\right) \) the vector space of antisymmetric matrices of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \).

a) Si \( A \in {\mathcal{A}}_{n}\left( \mathbb{K}\right) \) et si \( n \) est un entier impair, montrer que det \( A = 0 \) .

> a) If \( A \in {\mathcal{A}}_{n}\left( \mathbb{K}\right) \) and if \( n \) is an odd integer, show that det \( A = 0 \) .

b) Soit \( E \) un \( \mathbb{K} \) -espace vectoriel. Pour toute forme bilinéaire antisymétrique \( \varphi \) sur \( E \) , on définit une suite \( {\varphi }^{\left( p\right) } \) pour \( p \in {\mathbb{N}}^{ * } \) par la récurrence suivante : \( {\varphi }^{\left( 1\right) } = \varphi \) et pour \( p \geq 2 \) et \( \left( {{x}_{1},\ldots ,{x}_{2p}}\right) \in {E}^{2p}, \)

> b) Let \( E \) be a \( \mathbb{K} \) -vector space. For any antisymmetric bilinear form \( \varphi \) on \( E \) , we define a sequence \( {\varphi }^{\left( p\right) } \) for \( p \in {\mathbb{N}}^{ * } \) by the following recurrence: \( {\varphi }^{\left( 1\right) } = \varphi \) and for \( p \geq 2 \) and \( \left( {{x}_{1},\ldots ,{x}_{2p}}\right) \in {E}^{2p}, \)

\[
{\varphi }^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right)  = \mathop{\sum }\limits_{{i = 2}}^{{2p}}{\left( -1\right) }^{i}\varphi \left( {{x}_{1},{x}_{i}}\right) {\varphi }^{\left( p - 1\right) }\left( {{x}_{2},\ldots ,{x}_{i - 1},{x}_{i + 1},\ldots ,{x}_{2p}}\right) .
\]

(*)

> Montrer que \( {\varphi }^{\left( p\right) } \) est une forme \( {2p} \) -linéaire alternée. (Indication : traiter d’abord le cas \( p = 2 \) , puis montrer \( {\varphi }^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right) = 0 \) si \( {x}_{k} = {x}_{k + 1} \) - voir l’exercice 9 page 151.) c) Si \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , on désigne par \( {\varphi }_{A} \) la forme bilinéaire sur \( E = {\mathbb{K}}^{2m} \) dont \( A \) est la matrice dans la base canonique \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) de \( E \) , et on note \( \operatorname{Pf}\left( A\right) = {\varphi }_{A}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) (Pfaffien de A). Montrer que

Show that \( {\varphi }^{\left( p\right) } \) is an alternating \( {2p} \) -linear form. (Hint: first treat the case \( p = 2 \) , then show \( {\varphi }^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right) = 0 \) if \( {x}_{k} = {x}_{k + 1} \) - see exercise 9 on page 151.) c) If \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , we denote by \( {\varphi }_{A} \) the bilinear form on \( E = {\mathbb{K}}^{2m} \) whose matrix in the canonical basis \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) of \( E \) is \( A \) , and we denote \( \operatorname{Pf}\left( A\right) = {\varphi }_{A}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) (Pfaffian of A). Show that

\[
\forall \left( {{x}_{1},\ldots ,{x}_{2m}}\right)  \in  {E}^{2m},\;{\varphi }_{A}^{\left( m\right) }\left( {{x}_{1},\ldots ,{x}_{2m}}\right)  = \operatorname{Pf}\left( A\right) \mathop{\det }\limits_{\mathcal{B}}\left( {{x}_{1},\ldots ,{x}_{2m}}\right) ,
\]

où \( \mathop{\det }\limits_{\mathcal{B}} \) désigne le déterminant dans la base \( \mathcal{B} \) .

> where \( \mathop{\det }\limits_{\mathcal{B}} \) denotes the determinant in the basis \( \mathcal{B} \) .

d) Calculer \( \operatorname{Pf}\left( A\right) \) pour \( A \in {\mathcal{A}}_{4}\left( \mathbb{K}\right) \) , et montrer que \( \operatorname{Pf}\left( A\right) \) est un polynôme en les coefficients de \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) .

> d) Calculate \( \operatorname{Pf}\left( A\right) \) for \( A \in {\mathcal{A}}_{4}\left( \mathbb{K}\right) \) , and show that \( \operatorname{Pf}\left( A\right) \) is a polynomial in the coefficients of \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) .

e) Montrer que pour tout \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) et \( P \in {\mathcal{M}}_{2m}\left( \mathbb{K}\right) \) , on a \( \operatorname{Pf}\left( {{}^{\mathrm{t}}{PAP}}\right) = \det \left( P\right) \operatorname{Pf}\left( A\right) \) . f) Montrer que pour tout \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , on a \( \det \left( A\right) = \operatorname{Pf}{\left( A\right) }^{2} \) (on pourra utiliser le résultat de la question 1/b) du problème précédent).

> e) Show that for all \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) and \( P \in {\mathcal{M}}_{2m}\left( \mathbb{K}\right) \) , we have \( \operatorname{Pf}\left( {{}^{\mathrm{t}}{PAP}}\right) = \det \left( P\right) \operatorname{Pf}\left( A\right) \) . f) Show that for all \( A \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , we have \( \det \left( A\right) = \operatorname{Pf}{\left( A\right) }^{2} \) (one may use the result of question 1/b) of the previous problem).

Solution. a) Comme \( A = - {}^{\mathrm{t}}A \) , on a det \( A = {\left( -1\right) }^{n}\det {}^{\mathrm{t}}A = {\left( -1\right) }^{n}\det A = - \det A \) , donc det \( A = 0 \) . Ce résultat est aussi une conséquence du résultat du problème précédent qui entraîne que le rang d'une matrice antisymétrique est pair.

> Solution. a) Since \( A = - {}^{\mathrm{t}}A \) , we have det \( A = {\left( -1\right) }^{n}\det {}^{\mathrm{t}}A = {\left( -1\right) }^{n}\det A = - \det A \) , therefore det \( A = 0 \) . This result is also a consequence of the result of the previous problem which implies that the rank of an antisymmetric matrix is even.

b) La propriété de \( {2p} \) -linéarité de \( {\varphi }^{\left( p\right) } \) est immédiate par récurrence sur \( p \) . Montrons maintenant que \( {\varphi }^{\left( p\right) } \) est alternée. Il suffit pour cela de montrer par récurrence sur \( p \) que \( {\varphi }^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right) = 0 \) dès que \( {x}_{k} = {x}_{k + 1} \) (voir l’exercice 9 page 151). Pour \( p = 1 \) le résultat est immédiat car \( {\varphi }^{\left( 1\right) } = \varphi \) est antisymétrique. Pour \( p = 2 \) , on écrit

> b) The property of \( {2p} \) -linearity of \( {\varphi }^{\left( p\right) } \) is immediate by induction on \( p \) . Let us now show that \( {\varphi }^{\left( p\right) } \) is alternating. It suffices to show by induction on \( p \) that \( {\varphi }^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right) = 0 \) whenever \( {x}_{k} = {x}_{k + 1} \) (see exercise 9 on page 151). For \( p = 1 \) the result is immediate because \( {\varphi }^{\left( 1\right) } = \varphi \) is antisymmetric. For \( p = 2 \) , we write

\[
{\varphi }^{\left( 2\right) }\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right)  = \varphi \left( {{x}_{1},{x}_{2}}\right) \varphi \left( {{x}_{3},{x}_{4}}\right)  - \varphi \left( {{x}_{1},{x}_{3}}\right) \varphi \left( {{x}_{2},{x}_{4}}\right)  + \varphi \left( {{x}_{1},{x}_{4}}\right) \varphi \left( {{x}_{2},{x}_{3}}\right) .
\]

\( \left( {* * }\right) \)

> Dans chacun des cas \( {x}_{1} = {x}_{2},{x}_{2} = {x}_{3} \) et \( {x}_{3} = {x}_{4} \) , on remarque que l’un des termes de la somme est nulle et les deux autres opposés, donc \( {\varphi }^{\left( 2\right) } \) s’annule bien dans ces cas.

In each of the cases \( {x}_{1} = {x}_{2},{x}_{2} = {x}_{3} \) and \( {x}_{3} = {x}_{4} \) , we note that one of the terms of the sum is zero and the other two are opposites, so \( {\varphi }^{\left( 2\right) } \) indeed vanishes in these cases.

> Supposons maintenant \( p \geq 3 \) . Si \( {x}_{k} = {x}_{k + 1} \) avec \( 2 \leq k \leq p - 1 \) , les termes d’indices \( i \notin \{ k, k + 1\} \) et de la somme (*) s’annulent d’après l’hypothèse de récurrence, et les termes d’indices \( i = k \) et \( i = k + 1 \) sont opposés, donc \( {\varphi }^{\left( p\right) } \) est bien nul dans ce cas. Il nous reste à traiter le cas \( {x}_{1} = {x}_{2} \) . L’idée est d’exprimer \( {\varphi }^{\left( p\right) } \) en fonction de \( {\varphi }^{\left( p - 2\right) } \) . Par commodité, nous noterons \( x = \left( {{x}_{1},\ldots ,{x}_{2p}}\right) \) et si \( {i}_{1},\ldots ,{i}_{k} \) sont des indices distincts, on note \( {x}_{{i}_{1},\ldots ,{i}_{k}}^{ * } \) le \( \left( {p - k}\right) \) -uplet obtenu à partir de \( x \) en retirant les termes d’indices \( {i}_{1},\ldots ,{i}_{k} \) . Avec cette notation, \( \left( *\right) \) s’écrit

Now suppose \( p \geq 3 \) . If \( {x}_{k} = {x}_{k + 1} \) with \( 2 \leq k \leq p - 1 \) , the terms with indices \( i \notin \{ k, k + 1\} \) of the sum (*) cancel out according to the induction hypothesis, and the terms with indices \( i = k \) and \( i = k + 1 \) are opposites, so \( {\varphi }^{\left( p\right) } \) is indeed zero in this case. We have left to treat the case \( {x}_{1} = {x}_{2} \) . The idea is to express \( {\varphi }^{\left( p\right) } \) in terms of \( {\varphi }^{\left( p - 2\right) } \) . For convenience, we will denote \( x = \left( {{x}_{1},\ldots ,{x}_{2p}}\right) \) and if \( {i}_{1},\ldots ,{i}_{k} \) are distinct indices, we denote \( {x}_{{i}_{1},\ldots ,{i}_{k}}^{ * } \) as the \( \left( {p - k}\right) \) -tuple obtained from \( x \) by removing the terms with indices \( {i}_{1},\ldots ,{i}_{k} \) . With this notation, \( \left( *\right) \) is written

\[
{\varphi }^{\left( p\right) }\left( x\right)  = \mathop{\sum }\limits_{{i = 2}}^{{2p}}{\left( -1\right) }^{i}\varphi \left( {{x}_{1},{x}_{i}}\right) {\varphi }^{\left( p - 1\right) }\left( {x}_{1, i}^{ * }\right) .
\]

Si \( i \geq 3 \) , la récurrence définissant \( {\varphi }^{\left( p - 1\right) } \) donne

> If \( i \geq 3 \) , the recurrence defining \( {\varphi }^{\left( p - 1\right) } \) gives

\[
{\varphi }^{\left( p - 1\right) }\left( {x}_{1, i}^{ * }\right)  = \mathop{\sum }\limits_{{3 \leq  j < i}}{\left( -1\right) }^{j - 1}\varphi \left( {{x}_{2},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, j, i}^{ * }\right)  + \mathop{\sum }\limits_{{i < j \leq  {2p}}}{\left( -1\right) }^{j - 2}\varphi \left( {{x}_{2},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, i, j}^{ * }\right)
\]

(on a pris en compte le fait que \( {x}_{j} \) est la \( \left( {j - 1}\right) \) -ième coordonnée de \( {x}_{1, i}^{ * } \) si \( 3 \leq j < i \) , la \( \left( {j - 2}\right) \) -ième coordonnée si \( j > i \) ) donc

> (we have taken into account the fact that \( {x}_{j} \) is the \( \left( {j - 1}\right) \) -th coordinate of \( {x}_{1, i}^{ * } \) if \( 3 \leq j < i \) , the \( \left( {j - 2}\right) \) -th coordinate if \( j > i \) ) therefore

\[
{\varphi }^{\left( p\right) }\left( x\right)  = \varphi \left( {{x}_{1},{x}_{2}}\right) {\varphi }^{\left( p - 1\right) }\left( {{x}_{3},\ldots ,{x}_{2p}}\right)
\]

\[
+ \mathop{\sum }\limits_{\substack{{3 \leq  i \leq  {2p}} \\  {3 \leq  j < i} }}{\left( -1\right) }^{i + j - 1}\varphi \left( {{x}_{1},{x}_{i}}\right) \varphi \left( {{x}_{2},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, j, i}^{ * }\right)
\]

\[
+ \mathop{\sum }\limits_{\substack{{3 \leq  i \leq  {2p}} \\  {i < j \leq  {2p}} }}{\left( -1\right) }^{i + j - 2}\varphi \left( {{x}_{1},{x}_{i}}\right) \varphi \left( {{x}_{2},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, i, j}^{ * }\right) .
\]

Supposons \( {x}_{1} = {x}_{2} \) . Le premier terme de cette somme est nul, on peut donc écrire

> Suppose \( {x}_{1} = {x}_{2} \) . The first term of this sum is zero, so we can write

\[
{\varphi }^{\left( p\right) }\left( x\right)  = \mathop{\sum }\limits_{{3 \leq  j < i \leq  {2p}}}{\left( -1\right) }^{i + j - 1}\varphi \left( {{x}_{1},{x}_{i}}\right) \varphi \left( {{x}_{1},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, j, i}^{ * }\right)
\]

\[
+ \mathop{\sum }\limits_{{3 \leq  i < j \leq  {2p}}}{\left( -1\right) }^{i + j - 2}\varphi \left( {{x}_{1},{x}_{i}}\right) \varphi \left( {{x}_{1},{x}_{j}}\right) {\varphi }^{\left( p - 2\right) }\left( {x}_{1,2, i, j}^{ * }\right) .
\]

Chaque terme d’indice \( \left( {j, i}\right) \) de la première somme est l’opposé du terme d’indice \( \left( {i, j}\right) \) de la seconde, on en déduit \( {\varphi }^{\left( p\right) }\left( x\right) = 0 \) . c) L’ensemble des formes \( {2m} \) -linéaires alternées sur l’e.v \( E \) de dimension \( {2m} \) est un e.v de dimension 1 (voir le théorème 2 page 141). Comme \( {\varphi }_{A}^{\left( m\right) } \) et \( {\det }_{\mathcal{B}} \) sont des formes \( {2m} \) -linéaires alternées et que det \( {}_{\mathcal{B}} \) est non nul, on en déduit l’existence de \( \lambda \in \mathbb{K} \) tel que

> Each term with index \( \left( {j, i}\right) \) in the first sum is the opposite of the term with index \( \left( {i, j}\right) \) in the second; we deduce \( {\varphi }^{\left( p\right) }\left( x\right) = 0 \) . c) The set of alternating \( {2m} \) -linear forms on the vector space \( E \) of dimension \( {2m} \) is a vector space of dimension 1 (see theorem 2, page 141). Since \( {\varphi }_{A}^{\left( m\right) } \) and \( {\det }_{\mathcal{B}} \) are alternating \( {2m} \) -linear forms and det \( {}_{\mathcal{B}} \) is non-zero, we deduce the existence of \( \lambda \in \mathbb{K} \) such that

\[
\forall \left( {{x}_{1},\ldots ,{x}_{2m}}\right)  \in  {\mathrm{E}}^{2m},\;{\varphi }_{A}^{\left( m\right) }\left( {{x}_{1},\ldots ,{x}_{2m}}\right)  = \lambda \mathop{\det }\limits_{\mathcal{B}}\left( {{x}_{1},\ldots ,{x}_{2m}}\right) .
\]

En appliquant cette égalité pour \( {x}_{i} = {e}_{i}\left( {1 \leq i \leq {2m}}\right) \) , on obtient \( \lambda = \operatorname{Pf}\left( A\right) \) , d’où le résultat.

> By applying this equality for \( {x}_{i} = {e}_{i}\left( {1 \leq i \leq {2m}}\right) \) , we obtain \( \lambda = \operatorname{Pf}\left( A\right) \) , hence the result.

d) Lorsque \( A = \left( {a}_{i, j}\right) \in {\mathcal{A}}_{4}\left( \mathbb{K}\right) \) , on a \( m = 2 \) et l’expression \( \left( {* * }\right) \) entraîne \( \operatorname{Pf}\left( A\right) = {a}_{1,2}{a}_{3,4} - \; {a}_{1,3}{a}_{2,4} + {a}_{1,4}{a}_{2,3} \)

> d) When \( A = \left( {a}_{i, j}\right) \in {\mathcal{A}}_{4}\left( \mathbb{K}\right) \) , we have \( m = 2 \) and the expression \( \left( {* * }\right) \) leads to \( \operatorname{Pf}\left( A\right) = {a}_{1,2}{a}_{3,4} - \; {a}_{1,3}{a}_{2,4} + {a}_{1,4}{a}_{2,3} \)

Lorsque \( A = \left( {a}_{i, j}\right) \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , montrons maintenant que \( \operatorname{Pf}\left( A\right) \) est un polynôme en les coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) de \( A \) . Pour cela, nous allons prouver, en procédant par récurrence sur \( p \) , que si \( 1 \leq p \leq m \) et \( 1 \leq {k}_{1} < \ldots < {k}_{2p} \leq {2m} \) , alors \( {\varphi }_{A}^{\left( p\right) }\left( {{e}_{{k}_{1}},\ldots ,{e}_{{k}_{2p}}}\right) = {P}_{{k}_{1},\ldots ,{k}_{2p}}\left( A\right) \) où \( {P}_{{k}_{1},\ldots ,{k}_{2p}}\left( A\right) \) est un polynôme en les coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) de \( A \) . Cette propriété est vraie pour \( p = 1 \) car \( {\varphi }_{A}^{\left( 1\right) }\left( {{e}_{{k}_{1}},{e}_{{k}_{2}}}\right) = {a}_{{k}_{1},{k}_{2}} \) . Si elle est vraie pour \( p - 1 \) , alors l’écriture (*) entraîne

> When \( A = \left( {a}_{i, j}\right) \in {\mathcal{A}}_{2m}\left( \mathbb{K}\right) \) , let us now show that \( \operatorname{Pf}\left( A\right) \) is a polynomial in the coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) of \( A \) . To do this, we will prove, by proceeding by induction on \( p \) , that if \( 1 \leq p \leq m \) and \( 1 \leq {k}_{1} < \ldots < {k}_{2p} \leq {2m} \) , then \( {\varphi }_{A}^{\left( p\right) }\left( {{e}_{{k}_{1}},\ldots ,{e}_{{k}_{2p}}}\right) = {P}_{{k}_{1},\ldots ,{k}_{2p}}\left( A\right) \) where \( {P}_{{k}_{1},\ldots ,{k}_{2p}}\left( A\right) \) is a polynomial in the coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) of \( A \) . This property is true for \( p = 1 \) because \( {\varphi }_{A}^{\left( 1\right) }\left( {{e}_{{k}_{1}},{e}_{{k}_{2}}}\right) = {a}_{{k}_{1},{k}_{2}} \) . If it is true for \( p - 1 \) , then the expression (*) leads to

\[
{\varphi }_{A}^{\left( p\right) }\left( {{e}_{{k}_{1}},\ldots ,{e}_{{k}_{2p}}}\right)  = \mathop{\sum }\limits_{{i = 2}}^{{2p}}{\left( -1\right) }^{i}{\varphi }_{A}\left( {{e}_{{k}_{1}},{e}_{{k}_{i}}}\right) {\varphi }_{A}^{\left( p - 1\right) }\left( {{e}_{{k}_{2}},\ldots ,{e}_{{k}_{i - 1}},{e}_{{k}_{i + 1}},\ldots ,{e}_{{k}_{2p}}}\right)
\]

\[
= \mathop{\sum }\limits_{{i = 2}}^{{2p}}{\left( -1\right) }^{i}{a}_{{k}_{1},{k}_{i}}{P}_{{k}_{2},\ldots ,{k}_{i - 1},{k}_{i + 1},\ldots ,{k}_{2p}}\left( A\right) ,
\]

donc \( {\varphi }_{A}^{\left( p\right) }\left( {{e}_{{k}_{1}},\ldots ,{e}_{{k}_{2p}}}\right) \) est bien un polynôme en les coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) de \( A \) . La propriété souhaitée est donc démontrée pour tout \( p,1 \leq p \leq m \) . En particulier, elle est vraie pour \( p = m \) donc \( \operatorname{Pf}\left( A\right) = {\varphi }_{A}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) est un polynôme en les coefficients de \( A \) .

> therefore \( {\varphi }_{A}^{\left( p\right) }\left( {{e}_{{k}_{1}},\ldots ,{e}_{{k}_{2p}}}\right) \) is indeed a polynomial in the coefficients \( {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq {2m}} \) of \( A \) . The desired property is thus proven for all \( p,1 \leq p \leq m \) . In particular, it is true for \( p = m \) so \( \operatorname{Pf}\left( A\right) = {\varphi }_{A}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) is a polynomial in the coefficients of \( A \) .

e) Pour tout \( x, y \in E = {\mathbb{K}}^{2m} \) on a \( {\varphi }_{{}^{\mathrm{t}}{PAP}}\left( {x, y}\right) = {}^{\mathrm{t}}x{}^{\mathrm{t}}{PAPy} = {}^{\mathrm{t}}\left( {Px}\right) A\left( {Py}\right) = {\varphi }_{A}\left( {{Px},{Py}}\right) \) . Une récurrence immédiate sur \( p \) entraîne alors

> e) For all \( x, y \in E = {\mathbb{K}}^{2m} \) we have \( {\varphi }_{{}^{\mathrm{t}}{PAP}}\left( {x, y}\right) = {}^{\mathrm{t}}x{}^{\mathrm{t}}{PAPy} = {}^{\mathrm{t}}\left( {Px}\right) A\left( {Py}\right) = {\varphi }_{A}\left( {{Px},{Py}}\right) \) . An immediate induction on \( p \) then leads to

\[
\forall \left( {{x}_{1},\ldots ,{x}_{2p}}\right)  \in  {E}^{2p},\;{\varphi }_{{}^{\mathrm{t}}{PAP}}^{\left( p\right) }\left( {{x}_{1},\ldots ,{x}_{2p}}\right)  = {\varphi }_{A}^{\left( p\right) }\left( {P{x}_{1},\ldots , P{x}_{2p}}\right) .
\]

Ainsi, si \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) désigne la base canonique de \( {\mathbb{K}}^{2m} \) , on a

> Thus, if \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{2m}}\right) \) denotes the canonical basis of \( {\mathbb{K}}^{2m} \) , we have

\[
\operatorname{Pf}\left( {{}^{\mathrm{t}}{PAP}}\right)  = {\varphi }_{{}^{\mathrm{t}}{PAP}}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right)  = {\varphi }_{A}^{\left( m\right) }\left( {P{e}_{1},\ldots , P{e}_{2m}}\right)  = \operatorname{Pf}\left( A\right) \mathop{\det }\limits_{\mathcal{B}}\left( {P{e}_{1},\ldots , P{e}_{2m}}\right) .
\]

On conclut en remarquant que \( {\det }_{\mathcal{B}}\left( {P{e}_{1},\ldots , P{e}_{2m}}\right) = \det P \) .

> We conclude by noting that \( {\det }_{\mathcal{B}}\left( {P{e}_{1},\ldots , P{e}_{2m}}\right) = \det P \) .

f) Si \( A \) n’est pas inversible, alors il existe un vecteur \( {x}_{1} \neq 0 \) tel que \( A{x}_{1} = 0 \) donc \( {\varphi }_{A}\left( {{x}_{1}, y}\right) = 0 \) pour tout vecteur \( y \) . Complétons \( {x}_{1} \) en une base \( \left( {{x}_{1},\ldots ,{x}_{2m}}\right) \) de \( {\mathbb{K}}^{2m} \) . Comme \( {\varphi }_{A}\left( {{x}_{1},{x}_{i}}\right) = 0 \) pour tout \( i \geq 2 \) , l’égalité (*) donne \( {\varphi }_{A}^{\left( m\right) }\left( {{x}_{1},\ldots ,{x}_{2m}}\right) = 0 \) . D’après c), on a donc

> f) If \( A \) is not invertible, then there exists a vector \( {x}_{1} \neq 0 \) such that \( A{x}_{1} = 0 \) so \( {\varphi }_{A}\left( {{x}_{1}, y}\right) = 0 \) for any vector \( y \) . Let us complete \( {x}_{1} \) into a basis \( \left( {{x}_{1},\ldots ,{x}_{2m}}\right) \) of \( {\mathbb{K}}^{2m} \) . Since \( {\varphi }_{A}\left( {{x}_{1},{x}_{i}}\right) = 0 \) for all \( i \geq 2 \) , the equality (*) gives \( {\varphi }_{A}^{\left( m\right) }\left( {{x}_{1},\ldots ,{x}_{2m}}\right) = 0 \) . According to c), we therefore have

\[
0 = {\varphi }_{A}^{\left( m\right) }\left( {{x}_{1},\ldots ,{x}_{2m}}\right)  = \operatorname{Pf}\left( A\right) \mathop{\det }\limits_{\mathcal{B}}\left( {{x}_{1},\ldots ,{x}_{2m}}\right) .
\]

Comme \( \left( {{x}_{1},\ldots ,{x}_{2m}}\right) \) est une base, on a \( \mathop{\det }\limits_{\mathcal{B}}\left( {{x}_{1},\ldots ,{x}_{2m}}\right) \neq 0 \) donc l’égalité précédente entraîne \( \operatorname{Pf}\left( A\right) = 0 \) . Ainsi, on a bien \( \det A = \operatorname{Pf}{\left( A\right) }^{2} \) si \( A{\mathrm{n}}^{\prime } \) est pas inversible.

> Since \( \left( {{x}_{1},\ldots ,{x}_{2m}}\right) \) is a basis, we have \( \mathop{\det }\limits_{\mathcal{B}}\left( {{x}_{1},\ldots ,{x}_{2m}}\right) \neq 0 \) so the previous equality leads to \( \operatorname{Pf}\left( A\right) = 0 \) . Thus, we indeed have \( \det A = \operatorname{Pf}{\left( A\right) }^{2} \) if \( A{\mathrm{n}}^{\prime } \) is not invertible.

Si \( A \) est inversible, le résultat de la question b) du problème précédent nous assure l’existence de \( P \in \mathcal{G}{\ell }_{2m}\left( \mathbb{K}\right) \) tel que \( B = {}^{\mathrm{t}}{PAP} \) soit constituée de \( m \) matrices \( J = \left( \begin{matrix} 0 & 1 \\ - 1 & 0 \end{matrix}\right) \) sur sa diagonale et de 0 partout ailleurs. Le Pfaffien de \( B \) se calcule facilement. En effet, comme \( {\varphi }_{B}\left( {{e}_{1},{e}_{2}}\right) = 1 \) et \( {\varphi }_{B}\left( {{e}_{1},{e}_{i}}\right) = 0 \) si \( i \geq 3 \) , la relation \( \left( *\right) \) donne

> If \( A \) is invertible, the result of question b) of the previous problem ensures the existence of \( P \in \mathcal{G}{\ell }_{2m}\left( \mathbb{K}\right) \) such that \( B = {}^{\mathrm{t}}{PAP} \) consists of \( m \) matrices \( J = \left( \begin{matrix} 0 & 1 \\ - 1 & 0 \end{matrix}\right) \) on its diagonal and 0 elsewhere. The Pfaffian of \( B \) is easily calculated. Indeed, since \( {\varphi }_{B}\left( {{e}_{1},{e}_{2}}\right) = 1 \) and \( {\varphi }_{B}\left( {{e}_{1},{e}_{i}}\right) = 0 \) if \( i \geq 3 \) , the relation \( \left( *\right) \) gives

\[
{\varphi }_{B}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right)  = {\varphi }_{B}^{\left( m - 1\right) }\left( {{e}_{3},\ldots ,{e}_{2m}}\right) .
\]

En poursuivant, on en déduit ainsi \( {\varphi }_{B}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) = {\varphi }_{B}^{\left( 1\right) }\left( {{e}_{{2m} - 1},{e}_{2m}}\right) = 1 \) . Donc \( \operatorname{Pf}\left( B\right) = 1 \) et le résultat de la question précédente entraîne donc \( 1 = \operatorname{Pf}\left( B\right) = \operatorname{Pf}\left( {{}^{\mathrm{t}}{PAP}}\right) = \operatorname{Pf}\left( A\right) \det P \) . Par ailleurs, un calcul de déterminant par blocs donne \( \det B = {\left( \det J\right) }^{m} = 1 \) , et comme \( B = {}^{\mathrm{t}}{PAP} \) on en déduit det \( \left( A\right) \det {\left( P\right) }^{2} = 1 \) , donc det \( A = 1/\det {\left( P\right) }^{2} = \operatorname{Pf}{\left( A\right) }^{2} \) .

> Continuing, we thus deduce \( {\varphi }_{B}^{\left( m\right) }\left( {{e}_{1},\ldots ,{e}_{2m}}\right) = {\varphi }_{B}^{\left( 1\right) }\left( {{e}_{{2m} - 1},{e}_{2m}}\right) = 1 \) . Therefore \( \operatorname{Pf}\left( B\right) = 1 \) and the result of the previous question thus leads to \( 1 = \operatorname{Pf}\left( B\right) = \operatorname{Pf}\left( {{}^{\mathrm{t}}{PAP}}\right) = \operatorname{Pf}\left( A\right) \det P \) . Furthermore, a block determinant calculation gives \( \det B = {\left( \det J\right) }^{m} = 1 \) , and since \( B = {}^{\mathrm{t}}{PAP} \) we deduce det \( \left( A\right) \det {\left( P\right) }^{2} = 1 \) , thus det \( A = 1/\det {\left( P\right) }^{2} = \operatorname{Pf}{\left( A\right) }^{2} \) .

Remarque. Ainsi, le déterminant d’une matrice antisymétrique \( A \) d’ordre pair est le carré d’un polynôme en les coefficients de \( A \) (le Pfaffien). Ce résultat remarquable a été établi par Cayley au milieu du XIX-ième siècle.

> Remark. Thus, the determinant of an antisymmetric matrix \( A \) of even order is the square of a polynomial in the coefficients of \( A \) (the Pfaffian). This remarkable result was established by Cayley in the mid-19th century.

Problem 9. Soit \( \left( {E,\parallel .\parallel }\right) \) un \( \mathbb{R} \) -e.v normé de dimension \( n \in {\mathbb{N}}^{ * } \) . On note \( {B}_{p, q} \) l’ensemble des formes bilinéaires symétriques sur \( E \) de signature \( \left( {p, q}\right) \) . Si \( p + q = n \) , montrer que \( {B}_{p, q} \) est un ouvert de l’espace vectoriel \( \mathcal{B} \) des formes bilinéaires symétriques sur \( E \) .

> Problem 9. Let \( \left( {E,\parallel .\parallel }\right) \) be a normed \( \mathbb{R} \) -v.s. of dimension \( n \in {\mathbb{N}}^{ * } \) . Let \( {B}_{p, q} \) denote the set of symmetric bilinear forms on \( E \) with signature \( \left( {p, q}\right) \) . If \( p + q = n \) , show that \( {B}_{p, q} \) is an open subset of the vector space \( \mathcal{B} \) of symmetric bilinear forms on \( E \) .

Solution. Munissons \( \mathcal{B} \) de la norme \( \parallel .\parallel \) définie par \( \forall \varphi \in \mathcal{B},\;\parallel \varphi \parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel \varphi \left( {x, x}\right) \parallel (\mathcal{B} \) étant de dimension finie, toutes les normes y sont équivalentes).

> Solution. Let us equip \( \mathcal{B} \) with the norm \( \parallel .\parallel \) defined by \( \forall \varphi \in \mathcal{B},\;\parallel \varphi \parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel \varphi \left( {x, x}\right) \parallel (\mathcal{B} \) being finite-dimensional, all norms are equivalent there).

Donnons nous \( {\varphi }_{0} \in {B}_{p, q} \) , où \( p + q = n \) . La signature de \( {\varphi }_{0} \) étant \( \left( {p, q}\right) \) , il existe deux s.e.v \( {F}^{ + } \) et \( {F}^{ - } \) de \( E \) tels que

> Let us consider \( {\varphi }_{0} \in {B}_{p, q} \) , where \( p + q = n \) . The signature of \( {\varphi }_{0} \) being \( \left( {p, q}\right) \) , there exist two s.v.s. \( {F}^{ + } \) and \( {F}^{ - } \) of \( E \) such that

\[
\dim {F}^{ + } = p,\dim {F}^{ - } = q\;\text{ et }\;\left\{  {\begin{array}{lll} \forall x \in  {F}^{ + }, & x \neq  0 & {\varphi }_{0}\left( {x, x}\right)  > 0 \\  \forall x \in  {F}^{ - }, & x \neq  0 & {\varphi }_{0}\left( {x, x}\right)  < 0 \end{array}.}\right.
\]

Comme \( p + q = n \) , on a ici \( {F}^{ + } \oplus {F}^{ - } = E \) .

> As \( p + q = n \) , we have \( {F}^{ + } \oplus {F}^{ - } = E \) here.

L’ensemble \( {S}^{ + } = \left\{ {x \in {F}^{ + } \mid \parallel x\parallel = 1}\right\} \) est compact, donc \( {\varphi }_{0} \) étant continue

> The set \( {S}^{ + } = \left\{ {x \in {F}^{ + } \mid \parallel x\parallel = 1}\right\} \) is compact, so \( {\varphi }_{0} \) being continuous

\[
\exists x \in  {S}^{ + },\;{\varphi }_{0}\left( {x, x}\right)  = \mathop{\inf }\limits_{{y \in  {S}^{ + }}}{\varphi }_{0}\left( {y, y}\right) .
\]

En notant \( \alpha = {\varphi }_{0}\left( {x, x}\right) > 0 \) , on voit que pour tout \( y \in {S}^{ + },{\varphi }_{0}\left( {y, y}\right) \geq \alpha \) , donc pour tout \( y \in {F}^{ + } \) , \( {\varphi }_{0}\left( {y, y}\right) \geq \alpha \parallel y{\parallel }^{2} \) . On montrerait de même l’existence de \( \beta > 0 \) tel que tout \( y \in {F}^{ - } \) vérifie \( {\varphi }_{0}\left( {y, y}\right) \leq - \beta \parallel y{\parallel }^{2}. \)

> By noting \( \alpha = {\varphi }_{0}\left( {x, x}\right) > 0 \) , we see that for all \( y \in {S}^{ + },{\varphi }_{0}\left( {y, y}\right) \geq \alpha \) , thus for all \( y \in {F}^{ + } \) , \( {\varphi }_{0}\left( {y, y}\right) \geq \alpha \parallel y{\parallel }^{2} \) . We would similarly show the existence of \( \beta > 0 \) such that every \( y \in {F}^{ - } \) satisfies \( {\varphi }_{0}\left( {y, y}\right) \leq - \beta \parallel y{\parallel }^{2}. \)

Soit \( \gamma = \inf \left( {\alpha ,\beta }\right) \) et \( \psi \in \mathcal{B} \) tel que \( \parallel \psi \parallel \leq \gamma /2 \) . Alors \( \varphi = {\varphi }_{0} + \psi \) vérifie

> Let \( \gamma = \inf \left( {\alpha ,\beta }\right) \) and \( \psi \in \mathcal{B} \) be such that \( \parallel \psi \parallel \leq \gamma /2 \) . Then \( \varphi = {\varphi }_{0} + \psi \) satisfies

\[
\forall x \in  {F}^{ + },\;\varphi \left( {x, x}\right)  = {\varphi }_{0}\left( {x, x}\right)  + \psi \left( {x, x}\right)  \geq  \gamma \parallel x{\parallel }^{2} - \frac{\gamma }{2}\parallel x{\parallel }^{2} = \frac{\gamma }{2}\parallel x{\parallel }^{2}
\]

\[
\forall x \in  {F}^{ - },\;\varphi \left( {x, x}\right)  = {\varphi }_{0}\left( {x, x}\right)  + \psi \left( {x, x}\right)  \leq   - \gamma \parallel x{\parallel }^{2} + \frac{\gamma }{2}\parallel x{\parallel }^{2} =  - \frac{\gamma }{2}\parallel x{\parallel }^{2}
\]

On a donc \( \varphi \left( {x, x}\right) > 0 \) sur \( {F}^{ + } \smallsetminus \{ 0\} \) et \( \varphi \left( {x, x}\right) < 0 \) sur \( {F}^{ - } \smallsetminus \{ 0\} \) . Ceci suffit pour conclure que \( \varphi \) est de signature \( \left( {p, q}\right) \) (voir la remarque 9 page 246). La boule de centre \( {\varphi }_{0} \) de rayon \( \gamma /2 \) est donc incluse dans \( {B}_{p, q} \) , d’où le résultat.

> We thus have \( \varphi \left( {x, x}\right) > 0 \) on \( {F}^{ + } \smallsetminus \{ 0\} \) and \( \varphi \left( {x, x}\right) < 0 \) on \( {F}^{ - } \smallsetminus \{ 0\} \) . This is sufficient to conclude that \( \varphi \) has signature \( \left( {p, q}\right) \) (see remark 9 on page 246). The ball centered at \( {\varphi }_{0} \) with radius \( \gamma /2 \) is therefore included in \( {B}_{p, q} \) , hence the result.

PROBLÈME 10. Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) deux matrices hermitiennes positives.

> PROBLEM 10. Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be two positive Hermitian matrices.

a) Si \( A \) est définie, montrer que la matrice \( {AB} \) est diagonalisable,à valeurs propres réelles positives.

> a) If \( A \) is definite, show that the matrix \( {AB} \) is diagonalizable, with positive real eigenvalues.

b) Montrer que le résultat de la question précédente subsiste lorsque \( A \) n’est pas supposée définie.

> b) Show that the result of the previous question still holds when \( A \) is not assumed to be definite.

c) Soient \( 0 \leq {\lambda }_{1} \leq \cdots \leq {\lambda }_{n} \) les valeurs propres de \( A,0 \leq {\mu }_{1} \leq \cdots \leq {\mu }_{n} \) celles de \( B \) . Si \( \lambda \) est une valeur propre de \( {AB} \) , montrer \( {\lambda }_{1}{\mu }_{1} \leq \lambda \leq {\lambda }_{n}{\mu }_{n} \) .

> c) Let \( 0 \leq {\lambda }_{1} \leq \cdots \leq {\lambda }_{n} \) be the eigenvalues of \( A,0 \leq {\mu }_{1} \leq \cdots \leq {\mu }_{n} \) and those of \( B \) . If \( \lambda \) is an eigenvalue of \( {AB} \) , show \( {\lambda }_{1}{\mu }_{1} \leq \lambda \leq {\lambda }_{n}{\mu }_{n} \) .

Solution. a) La matrice \( A \) étant hermitienne positive, il existe une matrice \( a \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) hermi-tienne positive telle que \( A = {a}^{2} \) (c’est très classique, voir l’exercice 1 page 257). Comme \( A \) est définie, \( a \) est inversible. L’égalité \( {AB} = {a}^{2}B = a\left( {aBa}\right) {a}^{-1} \) montre que \( {AB} \) est semblable à \( {aBa} \) . Cette dernière matrice est hermitienne, et positive car la matrice \( B \) étant positive,

> Solution. a) Since the matrix \( A \) is positive Hermitian, there exists a positive Hermitian matrix \( a \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( A = {a}^{2} \) (this is very standard, see exercise 1 on page 257). As \( A \) is definite, \( a \) is invertible. The equality \( {AB} = {a}^{2}B = a\left( {aBa}\right) {a}^{-1} \) shows that \( {AB} \) is similar to \( {aBa} \) . This latter matrix is Hermitian, and positive because the matrix \( B \) being positive,

\[
\forall X,\;{X}^{ * }\left( {aBa}\right) X = {\left( aX\right) }^{ * }B\left( {aX}\right)  \geq  0.
\]

Finalement, on a montré que \( {AB} \) est semblable à une matrice hermitienne positive, ce qui suffit à montrer que \( {AB} \) est diagonalisable à valeurs propres réelles positives.

> Finally, we have shown that \( {AB} \) is similar to a positive Hermitian matrix, which is sufficient to show that \( {AB} \) is diagonalizable with positive real eigenvalues.

b) C'est plus délicat. Comme à la question précédente, nous allons passer par la matrice \( {aBa} \) .

> b) This is more delicate. As in the previous question, we will use the matrix \( {aBa} \) .

Soit \( k = \operatorname{rg}\left( {aBa}\right) \) . La matrice \( {aBa} \) étant hermitienne positive, on est assuré de l’existence d’une famille libre de \( k \) vecteurs propres \( {e}_{1},\ldots ,{e}_{k} \) associés à des valeurs propres strictement positives \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) . Pour tout \( i \in \{ 1,\ldots , k\} \) , l’égalité \( \left( {aBa}\right) {e}_{i} = {\lambda }_{i}{e}_{i} \) entraîne

> Let \( k = \operatorname{rg}\left( {aBa}\right) \) . Since the matrix \( {aBa} \) is positive Hermitian, we are guaranteed the existence of a linearly independent family of \( k \) eigenvectors \( {e}_{1},\ldots ,{e}_{k} \) associated with strictly positive eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) . For any \( i \in \{ 1,\ldots , k\} \) , the equality \( \left( {aBa}\right) {e}_{i} = {\lambda }_{i}{e}_{i} \) implies

\[
\left( {{a}^{2}{Ba}}\right) {e}_{i} = {\lambda }_{i}a{e}_{i}\;\text{ donc }\;\left( {AB}\right) {f}_{i} = {\lambda }_{i}{f}_{i},\;\text{ avec }\;{f}_{i} = a{e}_{i}.
\]

La famille \( {\left( {f}_{i}\right) }_{1 \leq i \leq k} \) est libre car

> The family \( {\left( {f}_{i}\right) }_{1 \leq i \leq k} \) is linearly independent because

\[
\mathop{\sum }\limits_{{i = 1}}^{k}{\mu }_{i}{f}_{i} = 0 \Rightarrow  0 = \mathop{\sum }\limits_{{i = 1}}^{k}{\mu }_{i}\left( {aB}\right) \left( {f}_{i}\right)  = \mathop{\sum }\limits_{{i = 1}}^{k}{\mu }_{i}{\lambda }_{i}{e}_{i} \Rightarrow  \forall i \in  \{ 1,\ldots , k\} ,{\mu }_{i}{\lambda }_{i} = 0,
\]

ce qui entraîne \( {\mu }_{i} = 0 \) lorsque \( 1 \leq i \leq k \) puisque \( {\lambda }_{i} \neq 0 \) . Finalement, on vient d’exhiber une famille libre \( {\left( {f}_{i}\right) }_{1 \leq i \leq k} \) à \( k \) éléments de vecteurs propres de \( {AB} \) associés à des valeurs propres non nulles.

> which implies \( {\mu }_{i} = 0 \) when \( 1 \leq i \leq k \) since \( {\lambda }_{i} \neq 0 \) . Finally, we have just exhibited a linearly independent family \( {\left( {f}_{i}\right) }_{1 \leq i \leq k} \) of \( k \) elements of eigenvectors of \( {AB} \) associated with non-zero eigenvalues.

Nous allons prouver que toutes les autres valeurs propres sont nulles. Pour cela, nous com-mençons par montrer \( \operatorname{rg}\left( {AB}\right) = \operatorname{rg}\left( {aBa}\right) = k \) . La matrice \( {aBa} \) est hermitienne positive (voir plus haut), donc \( X \in \operatorname{Ker}\left( {aBa}\right) \) si et seulement si \( {X}^{ * }\left( {aBa}\right) X = 0 \) . Comme \( B \) est positive, on en déduit

> We will prove that all other eigenvalues are zero. To do this, we begin by showing \( \operatorname{rg}\left( {AB}\right) = \operatorname{rg}\left( {aBa}\right) = k \) . The matrix \( {aBa} \) is positive Hermitian (see above), so \( X \in \operatorname{Ker}\left( {aBa}\right) \) if and only if \( {X}^{ * }\left( {aBa}\right) X = 0 \) . Since \( B \) is positive, we deduce

\[
X \in  \operatorname{Ker}\left( {aBa}\right)  \Leftrightarrow  0 = {X}^{ * }\left( {aBa}\right) X = {\left( aX\right) }^{ * }B\left( {aX}\right)  \Leftrightarrow  {aX} \in  \operatorname{Ker}\left( B\right)  \Leftrightarrow  X \in  \operatorname{Ker}\left( {Ba}\right) .
\]

Ainsi, \( \operatorname{Ker}\left( {aBa}\right) = \operatorname{Ker}\left( {Ba}\right) \) , donc \( \operatorname{rg}\left( {aBa}\right) = \operatorname{rg}\left( {Ba}\right) \) . La matrice \( a \) est hermitienne donc Im \( a = \; \operatorname{Im}{a}^{2} = \operatorname{Im}A \) (pour s’en convaincre, diagonaliser \( a \) dans une base orthonormale), donc \( \operatorname{Im}\left( {Ba}\right) = \; B\left( {\operatorname{Im}a}\right) = B\left( {\operatorname{Im}A}\right) = \operatorname{Im}\left( {BA}\right) \) , d’où \( \operatorname{rg}\left( {Ba}\right) = \operatorname{rg}\left( {BA}\right) \) . Finalement, on a montré \( \operatorname{rg}\left( {aBa}\right) = \; \operatorname{rg}\left( {BA}\right) \) . Le rang d’une matrice est égal à celui de sa transconjuguée, donc \( \operatorname{rg}\left( {BA}\right) = \operatorname{rg}\left\lbrack {\left( BA\right) }^{ * }\right\rbrack = \; \operatorname{rg}\left( {{A}^{ * }{B}^{ * }}\right) = \operatorname{rg}\left( {AB}\right) \) , et finalement on a bien \( \operatorname{rg}\left( {aBa}\right) = \operatorname{rg}\left( {AB}\right) = k \) .

> Thus, \( \operatorname{Ker}\left( {aBa}\right) = \operatorname{Ker}\left( {Ba}\right) \) , so \( \operatorname{rg}\left( {aBa}\right) = \operatorname{rg}\left( {Ba}\right) \) . The matrix \( a \) is Hermitian, so Im \( a = \; \operatorname{Im}{a}^{2} = \operatorname{Im}A \) (to be convinced of this, diagonalize \( a \) in an orthonormal basis), so \( \operatorname{Im}\left( {Ba}\right) = \; B\left( {\operatorname{Im}a}\right) = B\left( {\operatorname{Im}A}\right) = \operatorname{Im}\left( {BA}\right) \) , hence \( \operatorname{rg}\left( {Ba}\right) = \operatorname{rg}\left( {BA}\right) \) . Finally, we have shown \( \operatorname{rg}\left( {aBa}\right) = \; \operatorname{rg}\left( {BA}\right) \) . The rank of a matrix is equal to that of its conjugate transpose, so \( \operatorname{rg}\left( {BA}\right) = \operatorname{rg}\left\lbrack {\left( BA\right) }^{ * }\right\rbrack = \; \operatorname{rg}\left( {{A}^{ * }{B}^{ * }}\right) = \operatorname{rg}\left( {AB}\right) \) , and finally we indeed have \( \operatorname{rg}\left( {aBa}\right) = \operatorname{rg}\left( {AB}\right) = k \) .

Le fait que \( \dim \left( {\operatorname{Ker}\left( {AB}\right) }\right) = n - k \) nous permet de prendre une base \( \left( {{f}_{k + 1},\ldots ,{f}_{n}}\right) \) de \( \operatorname{Ker}\left( {AB}\right) \) . Ces \( n - k \) vecteurs correspondent à des vecteurs propres de \( {AB} \) associés à la valeur propre 0. Ainsi, les vecteurs \( {f}_{1},\ldots ,{f}_{k},{f}_{k + 1},\ldots ,{f}_{n} \) forment une famille libre à \( n \) éléments de vecteurs propres de \( {AB} \) , donc une base de vecteurs propres de \( {AB} \) . La matrice \( {AB} \) est donc diagonalisable, ses valeurs propres étant \( {\lambda }_{1},\ldots ,{\lambda }_{k} > 0 \) et 0 .

> The fact that \( \dim \left( {\operatorname{Ker}\left( {AB}\right) }\right) = n - k \) allows us to take a basis \( \left( {{f}_{k + 1},\ldots ,{f}_{n}}\right) \) of \( \operatorname{Ker}\left( {AB}\right) \) . These \( n - k \) vectors correspond to eigenvectors of \( {AB} \) associated with the eigenvalue 0. Thus, the vectors \( {f}_{1},\ldots ,{f}_{k},{f}_{k + 1},\ldots ,{f}_{n} \) form a linearly independent family of \( n \) elements of eigenvectors of \( {AB} \) , and therefore a basis of eigenvectors of \( {AB} \) . The matrix \( {AB} \) is thus diagonalizable, its eigenvalues being \( {\lambda }_{1},\ldots ,{\lambda }_{k} > 0 \) and 0 .

c) En désignant par \( \parallel \cdot \parallel \) la norme euclidienne usuelle sur \( {\mathbb{C}}^{n} \) , tout vecteur colonne \( X \) de \( {\mathbb{C}}^{n} \) vérifie

> c) By denoting by \( \parallel \cdot \parallel \) the usual Euclidean norm on \( {\mathbb{C}}^{n} \) , any column vector \( X \) of \( {\mathbb{C}}^{n} \) satisfies

\[
{\lambda }_{1}^{2}\parallel X{\parallel }^{2} \leq  \parallel {AX}{\parallel }^{2} \leq  {\lambda }_{n}^{2}\parallel X{\parallel }^{2}\;\text{ et }\;{\mu }_{1}^{2}\parallel X{\parallel }^{2} \leq  \parallel {BX}{\parallel }^{2} \leq  {\mu }_{n}^{2}\parallel X{\parallel }^{2}
\]

donc

> therefore

\[
{\lambda }_{1}^{2}{\mu }_{1}^{2}\parallel X{\parallel }^{2} \leq  {\lambda }_{1}^{2}\parallel {BX}{\parallel }^{2} \leq  \parallel {ABX}{\parallel }^{2} \leq  {\lambda }_{n}^{2}\parallel {BX}{\parallel }^{2} \leq  {\lambda }_{n}^{2}{\mu }_{n}^{2}\parallel X{\parallel }^{2}.
\]

(*)

> Si \( \lambda \) est une valeur propre de \( {AB} \) , on a \( \parallel {ABX}{\parallel }^{2} = {\left| \lambda \right| }^{2}\parallel X{\parallel }^{2} \) (où \( X \neq 0 \) est un vecteur propre associé), ce qui entraîne avec \( \left( *\right) \) la relation \( {\lambda }_{1}{\mu }_{1} \leq \left| \lambda \right| \leq {\lambda }_{n}{\mu }_{n} \) , d’où le résultat puisque l’on a vu que \( \lambda \) était réelle positive.

If \( \lambda \) is an eigenvalue of \( {AB} \) , we have \( \parallel {ABX}{\parallel }^{2} = {\left| \lambda \right| }^{2}\parallel X{\parallel }^{2} \) (where \( X \neq 0 \) is an associated eigenvector), which leads with \( \left( *\right) \) to the relation \( {\lambda }_{1}{\mu }_{1} \leq \left| \lambda \right| \leq {\lambda }_{n}{\mu }_{n} \) , hence the result since we have seen that \( \lambda \) was a positive real number.

---

PROBLEME 11. Soient \( R, S, T \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) trois matrices hermitiennes positives telles que la matrice \( M = {RST} \) est hermitienne. Montrer que \( M \) est positive.

> PROBLEM 11. Let \( R, S, T \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be three positive Hermitian matrices such that the matrix \( M = {RST} \) is Hermitian. Show that \( M \) is positive.

Solution. Il y a certainement beaucoup de façons de procéder. Celle que nous décrivons se décompose en trois étapes, selon les propriétés vérifiées par la matrice \( T \) .

> Solution. There are certainly many ways to proceed. The one we describe is broken down into three steps, according to the properties satisfied by the matrix \( T \) .

Première étape. Supposons \( T \) définie. Alors \( T \) est la matrice d’un produit scalaire, de sorte qu’il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( T = {P}^{ * }P \) . Comme \( {RST} \) est hermitienne, on a facilement \( {RST} = {TSR} \) donc

> First step. Suppose \( T \) is definite. Then \( T \) is the matrix of an inner product, so there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( T = {P}^{ * }P \) . Since \( {RST} \) is Hermitian, we easily have \( {RST} = {TSR} \) therefore

\[
{RS}{P}^{ * }P = {P}^{ * }{PSR}\text{ d’où }{\left( {P}^{ * }\right) }^{-1}{RS}{P}^{ * } = {PSR}{P}^{-1}\text{ ou encore }{R}^{\prime }{S}^{\prime } = {S}^{\prime }{R}^{\prime }
\]

avec \( {R}^{\prime } = {\left( {P}^{ * }\right) }^{-1}R{P}^{-1} \) et \( {S}^{\prime } = {PS}{P}^{ * } \) . Ainsi, les matrices \( {R}^{\prime } \) et \( {S}^{\prime } \) commutent. Comme elles sont diagonalisables (car hermitiennes), on peut les diagonaliser dans une même base. De plus, leurs valeurs propres sont positives ( \( {R}^{\prime } \) et \( {S}^{\prime } \) sont hermitiennes positives) donc les valeurs propres de \( {R}^{\prime }{S}^{\prime } \) sont positives. Ainsi, la matrice hermitienne \( {R}^{\prime }{S}^{\prime } \) est positive. Comme \( {RST} = {P}^{ * }\left( {{R}^{\prime }{S}^{\prime }}\right) P \) est congrue à \( {R}^{\prime }{S}^{\prime } \) , c’est aussi une matrice hermitienne positive.

> with \( {R}^{\prime } = {\left( {P}^{ * }\right) }^{-1}R{P}^{-1} \) and \( {S}^{\prime } = {PS}{P}^{ * } \) . Thus, the matrices \( {R}^{\prime } \) and \( {S}^{\prime } \) commute. Since they are diagonalizable (because they are Hermitian), they can be diagonalized in the same basis. Furthermore, their eigenvalues are positive ( \( {R}^{\prime } \) and \( {S}^{\prime } \) are positive Hermitian matrices) so the eigenvalues of \( {R}^{\prime }{S}^{\prime } \) are positive. Thus, the Hermitian matrix \( {R}^{\prime }{S}^{\prime } \) is positive. Since \( {RST} = {P}^{ * }\left( {{R}^{\prime }{S}^{\prime }}\right) P \) is congruent to \( {R}^{\prime }{S}^{\prime } \) , it is also a positive Hermitian matrix.

Deuxième étape. Supposons \( \operatorname{Ker}T \cap \operatorname{Ker}R = \{ 0\} \) . Pour tout \( \varepsilon > 0 \) , la matrice \( T + {\varepsilon R} \) est définie positive. En effet, elle est positive comme somme de matrices positives, et elle est définie car si \( {X}^{ * }\left( {T + {\varepsilon R}}\right) X = 0 \) , le fait que \( {X}^{ * }{TX} \geq 0 \) et \( {X}^{ * }{RX} \geq 0 \) entraîne \( {X}^{ * }{TX} = {X}^{ * }{RX} = 0 \) , donc \( X \in \operatorname{Ker}T \cap \operatorname{Ker}R = \{ 0\} . \)

> Second step. Suppose \( \operatorname{Ker}T \cap \operatorname{Ker}R = \{ 0\} \) . For any \( \varepsilon > 0 \) , the matrix \( T + {\varepsilon R} \) is positive definite. Indeed, it is positive as a sum of positive matrices, and it is definite because if \( {X}^{ * }\left( {T + {\varepsilon R}}\right) X = 0 \) , the fact that \( {X}^{ * }{TX} \geq 0 \) and \( {X}^{ * }{RX} \geq 0 \) implies \( {X}^{ * }{TX} = {X}^{ * }{RX} = 0 \) , therefore \( X \in \operatorname{Ker}T \cap \operatorname{Ker}R = \{ 0\} . \)

---

On peut donc appliquer le résultat de la première étape à la matrice hermitienne \( {RS}(T + \; {\varepsilon R}) = {RST} + {\varepsilon RSR} \) . Ainsi, pour tout \( X \in {\mathbb{C}}^{n} \) , pour tout \( \varepsilon > 0,{X}^{ * }{RS}\left( {T + {\varepsilon R}}\right) X \geq 0 \) donc en passant à la limite lorsque \( \varepsilon \rightarrow 0 \) on obtient \( {X}^{ * }{RSTX} \geq 0 \) . Ceci est vrai pour tout \( X \in {\mathbb{C}}^{n} \) , donc \( {RST} \) est positive.

> We can therefore apply the result of the first step to the Hermitian matrix \( {RS}(T + \; {\varepsilon R}) = {RST} + {\varepsilon RSR} \) . Thus, for any \( X \in {\mathbb{C}}^{n} \) , for any \( \varepsilon > 0,{X}^{ * }{RS}\left( {T + {\varepsilon R}}\right) X \geq 0 \) , so by taking the limit as \( \varepsilon \rightarrow 0 \) , we obtain \( {X}^{ * }{RSTX} \geq 0 \) . This is true for any \( X \in {\mathbb{C}}^{n} \) , so \( {RST} \) is positive.

Troisième étape. Il ne reste plus qu’à traiter le cas où \( F = \operatorname{Ker}T \cap \operatorname{Ker}R \neq \{ 0\} \) . Soit \( r \) tel que \( n - r = \dim F \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base orthonormale de \( {\mathbb{C}}^{n} \) telle que \( F = \operatorname{Vect}\left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) . Quitte à faire un changement de base orthonormale pour se ramener dans cette base, on voit que

> Third step. It only remains to treat the case where \( F = \operatorname{Ker}T \cap \operatorname{Ker}R \neq \{ 0\} \) . Let \( r \) be such that \( n - r = \dim F \) . Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be an orthonormal basis of \( {\mathbb{C}}^{n} \) such that \( F = \operatorname{Vect}\left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) . By performing a change of orthonormal basis to reduce to this basis, we see that

\[
R = \left( \begin{matrix} {R}_{1} & 0 \\  0 & 0 \end{matrix}\right) ,\;S = \left( \begin{matrix} {S}_{1} & {S}_{2}^{ * } \\  {S}_{2} & {S}_{3} \end{matrix}\right) ,\;\text{ et }\;T = \left( \begin{matrix} {T}_{1} & 0 \\  0 & 0 \end{matrix}\right) ,
\]

avec \( {R}_{1},{S}_{1},{T}_{1} \in {\mathcal{M}}_{r}\left( \mathbb{C}\right) \) et Ker \( {R}_{1} \cap \operatorname{Ker}{T}_{1} = \{ 0\} \) . La matrice \( M = {RST} \) étant hermitienne, on a facilement

> with \( {R}_{1},{S}_{1},{T}_{1} \in {\mathcal{M}}_{r}\left( \mathbb{C}\right) \) and Ker \( {R}_{1} \cap \operatorname{Ker}{T}_{1} = \{ 0\} \) . The matrix \( M = {RST} \) being Hermitian, we easily have

\[
M = \left( \begin{matrix} {R}_{1}{S}_{1}{T}_{1} & 0 \\  0 & 0 \end{matrix}\right)
\]

(*)

> où \( {R}_{1},{S}_{1},{T}_{1} \) vérifient les mêmes propriétés que \( R, S, T \) dans la deuxième étape. La matrice \( {R}_{1}{S}_{1}{T}_{1} \) est donc positive, donc d’après \( \left( *\right) M \) est positive.

where \( {R}_{1},{S}_{1},{T}_{1} \) satisfy the same properties as \( R, S, T \) in the second step. The matrix \( {R}_{1}{S}_{1}{T}_{1} \) is therefore positive, so according to \( \left( *\right) M \) it is positive.

> Problem 12. Soit \( n \in \mathbb{N}, n \geq 2 \) . Pour toute matrice symétrique \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , on note \( {\lambda }_{1}\left( A\right) ,\ldots ,{\lambda }_{n}\left( A\right) \) les valeurs propres de \( A \) numérotées telles que \( {\lambda }_{1}\left( A\right) \geq \cdots \geq {\lambda }_{n}\left( A\right) \) .

Problem 12. Let \( n \in \mathbb{N}, n \geq 2 \) . For any symmetric matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , we denote by \( {\lambda }_{1}\left( A\right) ,\ldots ,{\lambda }_{n}\left( A\right) \) the eigenvalues of \( A \) numbered such that \( {\lambda }_{1}\left( A\right) \geq \cdots \geq {\lambda }_{n}\left( A\right) \) .

> 1/a) Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice symétrique. Montrer

1/a) Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a symmetric matrix. Show

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\mathop{\sum }\limits_{{i = 1}}^{k}{a}_{i, i} \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( A\right) .
\]

(*)

> b) Lorsque \( k < n \) et \( {\lambda }_{k}\left( A\right) > {\lambda }_{k + 1}\left( A\right) \) , donner une condition nécessaire et suffisante sur la matrice \( A \) pour que l’inégalité (*) soit une égalité.

b) When \( k < n \) and \( {\lambda }_{k}\left( A\right) > {\lambda }_{k + 1}\left( A\right) \), provide a necessary and sufficient condition on matrix \( A \) for inequality (*) to be an equality.

> 2/ Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) deux matrices symétriques et \( C = A + B \) . Montrer

2/ Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be two symmetric matrices and \( C = A + B \). Show

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( C\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( A\right)  + \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( B\right) .
\]

Solution. 1/a) Pour simplifier on note \( {\lambda }_{i} = {\lambda }_{i}\left( A\right) \) dans la solution de la question 1/.

> Solution. 1/a) For simplicity, we denote \( {\lambda }_{i} = {\lambda }_{i}\left( A\right) \) in the solution to question 1/.

Lorsque \( k = n,\left( *\right) \) est une égalité car \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i} = \operatorname{tr}\left( A\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i} \) .

> When \( k = n,\left( *\right) \) is an equality because \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i} = \operatorname{tr}\left( A\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i} \).

Sinon on a \( k < n \) . Notons \( \Phi \) la forme quadratique sur \( {\mathbb{R}}^{n} \) dont \( A \) est la matrice dans la base canonique \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{R}}^{n} \) . Pour tout \( i \in \{ 1,\ldots , n\} \) , on a \( {a}_{i, i} = \Phi \left( {e}_{i}\right) \) . Soit \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) une base orthonormale de \( {\mathbb{R}}^{n} \) , orthogonale pour la forme quadratique \( \Phi \) , et telle que

> Otherwise, we have \( k < n \). Let \( \Phi \) be the quadratic form on \( {\mathbb{R}}^{n} \) whose matrix in the canonical basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) is \( A \). For all \( i \in \{ 1,\ldots , n\} \), we have \( {a}_{i, i} = \Phi \left( {e}_{i}\right) \). Let \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) be an orthonormal basis of \( {\mathbb{R}}^{n} \), orthogonal for the quadratic form \( \Phi \), and such that

\[
\forall i \in  \{ 1,\ldots , n\} ,\;{\lambda }_{i} = \Phi \left( {f}_{i}\right) .
\]

On note \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) la matrice (orthogonale) de passage de la base \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) à la base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , de sorte que \( {e}_{j} = \mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i, j}{f}_{i} \) pour tout \( j \) .

> Let \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be the (orthogonal) transition matrix from basis \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) to basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \), such that \( {e}_{j} = \mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i, j}{f}_{i} \) for all \( j \).

Pour donner l'idée de l'approche nous commençons par le cas \( k = 1 \) . Il suffit d'écrire

> To provide an idea of the approach, we begin with the case \( k = 1 \). It suffices to write

\[
{a}_{1,1} = \Phi \left( {e}_{1}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i,1}^{2}\Phi \left( {f}_{i}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{p}_{i,1}^{2} \leq  {\lambda }_{1}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i,1}^{2}}\right)  = {\lambda }_{1}{\begin{Vmatrix}{e}_{1}\end{Vmatrix}}^{2} = {\lambda }_{1}.
\]

Le cas général est plus délicat. On écrit

> The general case is more delicate. We write

\[
\mathop{\sum }\limits_{{j = 1}}^{k}{a}_{j, j} = \mathop{\sum }\limits_{{j = 1}}^{k}\Phi \left( {e}_{j}\right)  = \mathop{\sum }\limits_{{j = 1}}^{k}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{p}_{i, j}^{2}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( {\mathop{\sum }\limits_{{j = 1}}^{k}{p}_{i, j}^{2}}\right) .
\]

\( \left( {* * }\right) \)

> Notons \( {\mu }_{i} = \mathop{\sum }\limits_{{j = 1}}^{k}{p}_{i, j}^{2} \) . Les \( {\mu }_{i} \) vérifient les propriétés suivantes

Let \( {\mu }_{i} = \mathop{\sum }\limits_{{j = 1}}^{k}{p}_{i, j}^{2} \). The \( {\mu }_{i} \) satisfy the following properties

\[
\text{ (i) }\;\mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i} = \mathop{\sum }\limits_{{j = 1}}^{k}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{p}_{i, j}^{2}}\right)  = \mathop{\sum }\limits_{{j = 1}}^{k}{\begin{Vmatrix}{e}_{j}\end{Vmatrix}}^{2} = k\text{ , }
\]

\[
{\mu }_{i} = \mathop{\sum }\limits_{{j = 1}}^{k}{p}_{i, j}^{2} \leq  \mathop{\sum }\limits_{{j = 1}}^{n}{p}_{i, j}^{2} = 1
\]

(la dernière égalité résulte du fait que les vecteurs lignes de la matrice \( P \) forment également une base orthonormale). Ainsi,(**) apparaît comme une pondération des \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \) à coefficients positifs et \( \leq 1 \) , dont la somme des poids vaut \( k \) . La valeur maximale de cette pondération se produit lorsque les poids sont les plus grands possibles pour les plus grandes valeurs possibles de \( {\lambda }_{i} \) , ce qui est précisément le résultat attendu. On démontre ceci en partant de l’égalité (**) qui entraîne

> (the last equality results from the fact that the row vectors of matrix \( P \) also form an orthonormal basis). Thus, (**) appears as a weighted average of \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \) with positive coefficients and \( \leq 1 \), the sum of whose weights equals \( k \). The maximum value of this weighted average occurs when the weights are as large as possible for the largest possible values of \( {\lambda }_{i} \), which is precisely the expected result. We prove this by starting from equality (**) which implies

\[
\mathop{\sum }\limits_{{j = 1}}^{k}{a}_{j, j} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\mu }_{i} \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}{\mu }_{i} + {\lambda }_{k + 1}\left( {\mathop{\sum }\limits_{{i = k + 1}}^{n}{\mu }_{i}}\right) .
\]

L’assertion (ii) permet d’écrire chaque \( {\mu }_{i} \) sous la forme \( {\mu }_{i} = 1 - {\gamma }_{i} \) avec \( {\gamma }_{i} \geq 0 \) pour \( 1 \leq i \leq k \) , et d’après (i), \( \mathop{\sum }\limits_{{i = k + 1}}^{n}{\mu }_{i} = k - \left( {\mathop{\sum }\limits_{{i = 1}}^{k}{\mu }_{i}}\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{\gamma }_{i} \) . Finalement,

> Assertion (ii) allows us to write each \( {\mu }_{i} \) in the form \( {\mu }_{i} = 1 - {\gamma }_{i} \) with \( {\gamma }_{i} \geq 0 \) for \( 1 \leq i \leq k \) , and according to (i), \( \mathop{\sum }\limits_{{i = k + 1}}^{n}{\mu }_{i} = k - \left( {\mathop{\sum }\limits_{{i = 1}}^{k}{\mu }_{i}}\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{\gamma }_{i} \) . Finally,

\[
\mathop{\sum }\limits_{{j = 1}}^{k}{a}_{j, j} \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( {1 - {\gamma }_{i}}\right)  + {\lambda }_{k + 1}\left( {\mathop{\sum }\limits_{{i = 1}}^{k}{\gamma }_{i}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i} + \mathop{\sum }\limits_{{i = 1}}^{k}\left( {{\lambda }_{k + 1} - {\lambda }_{i}}\right) {\gamma }_{i} \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}.
\]

(***)

> b) Si (*) est une égalité, alors la dernière inégalité de (***) est une égalité, et compte tenu des hypothèses, ceci entraîne \( {\gamma }_{i} = 0 \) pour \( 1 \leq i \leq k \) . Autrement dit, \( {\mu }_{1} = \ldots = {\mu }_{k} = 1 \) ce qui en vertu de l’assertion (ii) entraîne \( {p}_{i, j} = 0 \) pour \( 1 \leq i \leq k \) et \( k + 1 \leq j \leq n \) . Ainsi, \( {e}_{j} = \mathop{\sum }\limits_{{i = 1}}^{k}{p}_{i, j}{f}_{i} \in \; \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) pour \( 1 \leq j \leq k \) , donc Vect \( \left( {{e}_{1},\ldots ,{e}_{k}}\right) = \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) . Les bases \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) et \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) étant orthogonales, on a alors \( \operatorname{Vect}\left( {{e}_{k + 1},\ldots ,{e}_{n}}\right) = \operatorname{Vect}\left( {{f}_{k + 1},\ldots ,{f}_{n}}\right) \) . Il n’en faut pas plus pour conclure que \( A \) , matrice de \( \Phi \) dans la base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , se met sous la forme

b) If (*) is an equality, then the last inequality of (***) is an equality, and given the hypotheses, this implies \( {\gamma }_{i} = 0 \) for \( 1 \leq i \leq k \) . In other words, \( {\mu }_{1} = \ldots = {\mu }_{k} = 1 \) which, by virtue of assertion (ii), implies \( {p}_{i, j} = 0 \) for \( 1 \leq i \leq k \) and \( k + 1 \leq j \leq n \) . Thus, \( {e}_{j} = \mathop{\sum }\limits_{{i = 1}}^{k}{p}_{i, j}{f}_{i} \in \; \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) for \( 1 \leq j \leq k \) , therefore Vect \( \left( {{e}_{1},\ldots ,{e}_{k}}\right) = \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) . Since the bases \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) and \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) are orthogonal, we then have \( \operatorname{Vect}\left( {{e}_{k + 1},\ldots ,{e}_{n}}\right) = \operatorname{Vect}\left( {{f}_{k + 1},\ldots ,{f}_{n}}\right) \) . This is sufficient to conclude that \( A \) , the matrix of \( \Phi \) in the basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , takes the form

\[
A = \left( \begin{matrix} {A}_{1} & 0 \\  0 & {A}_{2} \end{matrix}\right)
\]

où les valeurs propres de \( {A}_{1} \in {\mathcal{M}}_{k}\left( \mathbb{R}\right) \) sont \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) .

> where the eigenvalues of \( {A}_{1} \in {\mathcal{M}}_{k}\left( \mathbb{R}\right) \) are \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) .

Réciproquement, si la matrice \( A \) possède cette propriété, alors \( \mathop{\sum }\limits_{{i = 1}}^{k}{a}_{i, i} = \operatorname{tr}\left( {A}_{1}\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i} \) .

> Conversely, if the matrix \( A \) possesses this property, then \( \mathop{\sum }\limits_{{i = 1}}^{k}{a}_{i, i} = \operatorname{tr}\left( {A}_{1}\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i} \) .

2 / Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) une matrice orthogonale telle que \( D = {P}^{-1}{CP} \) est diagonale, ses coefficients diagonaux étant égaux à \( {\lambda }_{1}\left( C\right) ,\ldots ,{\lambda }_{n}\left( C\right) \) . Notons \( {A}^{\prime } = {P}^{-1}{AP} \) et \( {B}^{\prime } = {P}^{-1}{BP} \) . On a \( D = {A}^{\prime } + \; {B}^{\prime } \) et les matrices \( {A}^{\prime } \) et \( {B}^{\prime } \) sont semblables à \( A \) et \( B \) , on a donc \( {\lambda }_{i}\left( {A}^{\prime }\right) = {\lambda }_{i}\left( A\right) \) et \( {\lambda }_{i}\left( {B}^{\prime }\right) = {\lambda }_{i}\left( B\right) \) pour \( 1 \leq i \leq n \) . Pour simplifier les notations, pour toute matrice \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) on note \( {\operatorname{tr}}_{k}\left( M\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{m}_{i, i} \) . On conclut à partir du résultat de la question \( 1/\mathrm{a} \) ), en écrivant

> 2 / Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) be an orthogonal matrix such that \( D = {P}^{-1}{CP} \) is diagonal, with its diagonal coefficients equal to \( {\lambda }_{1}\left( C\right) ,\ldots ,{\lambda }_{n}\left( C\right) \) . Let \( {A}^{\prime } = {P}^{-1}{AP} \) and \( {B}^{\prime } = {P}^{-1}{BP} \) . We have \( D = {A}^{\prime } + \; {B}^{\prime } \) and the matrices \( {A}^{\prime } \) and \( {B}^{\prime } \) are similar to \( A \) and \( B \) , so we have \( {\lambda }_{i}\left( {A}^{\prime }\right) = {\lambda }_{i}\left( A\right) \) and \( {\lambda }_{i}\left( {B}^{\prime }\right) = {\lambda }_{i}\left( B\right) \) for \( 1 \leq i \leq n \) . To simplify notation, for any matrix \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) we denote \( {\operatorname{tr}}_{k}\left( M\right) = \mathop{\sum }\limits_{{i = 1}}^{k}{m}_{i, i} \) . We conclude from the result of question \( 1/\mathrm{a} \) ), by writing

\[
\forall k \in  \{ 1,\ldots , n\} ,\;\mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( C\right)  = {\operatorname{tr}}_{k}\left( D\right)  = {\operatorname{tr}}_{k}\left( {A}^{\prime }\right)  + {\operatorname{tr}}_{k}\left( {B}^{\prime }\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( A\right)  + \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( B\right) .
\]

Problem 13. Soit \( n \in \mathbb{N}, n \geq 2 \) , et \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) deux matrices symétriques. On suppose que pour tout \( k \in {\mathbb{N}}^{ * },\operatorname{tr}{\left( A + B\right) }^{k} = \operatorname{tr}{A}^{k} + \operatorname{tr}{B}^{k} \) . Montrer que \( {AB} = 0 \) .

> Problem 13. Let \( n \in \mathbb{N}, n \geq 2 \) and \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be two symmetric matrices. Suppose that for all \( k \in {\mathbb{N}}^{ * },\operatorname{tr}{\left( A + B\right) }^{k} = \operatorname{tr}{A}^{k} + \operatorname{tr}{B}^{k} \) . Show that \( {AB} = 0 \) .

Solution. Notons \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) les valeurs propres non nulles de \( A \) comptées avec multiplicité, \( {\mu }_{1},\ldots ,{\mu }_{q} \) celles de \( B \) et \( {\nu }_{1},\ldots ,{\nu }_{r} \) celles de \( C = A + B \) . L’hypothèse de l’énoncé s’écrit

> Solution. Let \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) be the non-zero eigenvalues of \( A \) counted with multiplicity, \( {\mu }_{1},\ldots ,{\mu }_{q} \) those of \( B \) , and \( {\nu }_{1},\ldots ,{\nu }_{r} \) those of \( C = A + B \) . The hypothesis of the statement is written

\[
\forall k \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{i = 1}}^{r}{\nu }_{i}^{k} = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}^{k} + \mathop{\sum }\limits_{{i = 1}}^{q}{\mu }_{i}^{k}.
\]

Autrement dit, les sommes de Newton de la \( r \) -liste \( \left( {{\nu }_{1},\ldots ,{\nu }_{r}}\right) \) sont égales à celles de la \( p + q \) -liste \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{p},{\mu }_{1},\ldots ,{\mu }_{q}}\right) \) . Le lemme suivant nous permet de conclure que \( p + q = r \) et que ces listes sont égales à une permutation prés.

> In other words, the Newton sums of the \( r \) -list \( \left( {{\nu }_{1},\ldots ,{\nu }_{r}}\right) \) are equal to those of the \( p + q \) -list \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{p},{\mu }_{1},\ldots ,{\mu }_{q}}\right) \) . The following lemma allows us to conclude that \( p + q = r \) and that these lists are equal up to a permutation.

Lemme. Soit \( s, t \in \mathbb{N} \) et \( \left( {{x}_{1},\ldots ,{x}_{s}}\right) ,\left( {{y}_{1},\ldots ,{y}_{t}}\right) \) deux listes de nombres réels non nuls, telles que

> Lemma. Let \( s, t \in \mathbb{N} \) and \( \left( {{x}_{1},\ldots ,{x}_{s}}\right) ,\left( {{y}_{1},\ldots ,{y}_{t}}\right) \) be two lists of non-zero real numbers, such that

\[
\forall k \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{i = 1}}^{s}{x}_{i}^{k} = \mathop{\sum }\limits_{{i = 1}}^{t}{y}_{i}^{k}.
\]

\( \left( *\right) \) .

> Alors \( t = s \) et les deux listes sont égales à une permutation près.

Then \( t = s \) and the two lists are equal up to a permutation.

> Montrons ce lemme par récurrence sur \( s \in \mathbb{N} \) . Si \( s = 0 \) , alors \( t = 0 \) sinon l’égalité (*) appliquée avec \( k = 2 \) entraînerait \( 0 = \mathop{\sum }\limits_{{i = 1}}^{t}{y}_{i}^{2} \) , donc les \( {y}_{i} \) seraient nuls, ce qui est contraire aux hypothèses. Supposons maintenant le lemme vrai jusqu’au rang \( s - 1 \) . Notons \( X = \mathop{\max }\limits_{i}\left| {x}_{i}\right| , Y = \mathop{\max }\limits_{i}\left| {y}_{i}\right| \) , puis \( I = \left\{ {i\left| \right| {x}_{i} \mid = X}\right\} , J = \left\{ {i\left| \right| {y}_{i} \mid = Y}\right\} \) . Les ensembles \( I \) et \( J \) sont non vides, et dans l’égalité (*) appliquée aux indices pairs \( k = 2\ell \) lorsque \( \ell \rightarrow + \infty \) , le terme de gauche est équivalent à \( \left| I\right| {X}^{2\ell } \) et celui de droite à \( \left| J\right| {Y}^{2\ell } \) . On en déduit \( X = Y \) puis \( \left| I\right| = \left| J\right| \) . En notant \( {I}^{\prime } = \left\{ {i \mid {x}_{i} = X}\right\} \) et \( {J}^{\prime } = \left\{ {i \mid {y}_{i} = X}\right\} \) , l’égalité (*) appliquée aux indices impairs \( k = 2\ell + 1 \) lorsque \( \ell \rightarrow + \infty \) donne \( \left| {I}^{\prime }\right| {X}^{2\ell + 1} - \left( {\left| I\right| - \left| {I}^{\prime }\right| }\right) {X}^{2\ell + 1} = \left| {J}^{\prime }\right| {X}^{2\ell + 1} - \left( {\left| J\right| - \left| {J}^{\prime }\right| }\right) {X}^{2\ell + 1} + o\left( {X}^{2\ell }\right) \) donc \( 2\left| {I}^{\prime }\right| - \left| I\right| = 2\left| {J}^{\prime }\right| - \left| J\right| , \) donc \( \left| {I}^{\prime }\right| = \left| {J}^{\prime }\right| \) . Ainsi, les listes \( {\left( {x}_{i}\right) }_{i \in I} \) et \( {\left( {y}_{i}\right) }_{i \in J} \) sont égales à une permutation prés. On conclut avec l’hypothèse de récurrence appliquée à \( {\left( {x}_{i}\right) }_{i \notin I} \) et \( {\left( {y}_{i}\right) }_{i \notin J} \) . (Une autre preuve de ce lemme, purement algébrique, consiste à utiliser l'expression des coefficients symétriques en fonction des sommes de Newton - voir l'exercice 3 page 86 -, en complétant préalablement l'une des deux listes avec des termes nuls pour qu'elles aient la même taille).

Let us prove this lemma by induction on \( s \in \mathbb{N} \) . If \( s = 0 \) , then \( t = 0 \) otherwise the equality (*) applied with \( k = 2 \) would imply \( 0 = \mathop{\sum }\limits_{{i = 1}}^{t}{y}_{i}^{2} \) , so the \( {y}_{i} \) would be zero, which contradicts the hypotheses. Now assume the lemma is true up to rank \( s - 1 \) . Let \( X = \mathop{\max }\limits_{i}\left| {x}_{i}\right| , Y = \mathop{\max }\limits_{i}\left| {y}_{i}\right| \) , then \( I = \left\{ {i\left| \right| {x}_{i} \mid = X}\right\} , J = \left\{ {i\left| \right| {y}_{i} \mid = Y}\right\} \) . The sets \( I \) and \( J \) are non-empty, and in the equality (*) applied to even indices \( k = 2\ell \) when \( \ell \rightarrow + \infty \) , the left-hand term is equivalent to \( \left| I\right| {X}^{2\ell } \) and the right-hand term to \( \left| J\right| {Y}^{2\ell } \) . We deduce \( X = Y \) then \( \left| I\right| = \left| J\right| \) . By noting \( {I}^{\prime } = \left\{ {i \mid {x}_{i} = X}\right\} \) and \( {J}^{\prime } = \left\{ {i \mid {y}_{i} = X}\right\} \) , the equality (*) applied to odd indices \( k = 2\ell + 1 \) when \( \ell \rightarrow + \infty \) gives \( \left| {I}^{\prime }\right| {X}^{2\ell + 1} - \left( {\left| I\right| - \left| {I}^{\prime }\right| }\right) {X}^{2\ell + 1} = \left| {J}^{\prime }\right| {X}^{2\ell + 1} - \left( {\left| J\right| - \left| {J}^{\prime }\right| }\right) {X}^{2\ell + 1} + o\left( {X}^{2\ell }\right) \) so \( 2\left| {I}^{\prime }\right| - \left| I\right| = 2\left| {J}^{\prime }\right| - \left| J\right| , \) so \( \left| {I}^{\prime }\right| = \left| {J}^{\prime }\right| \) . Thus, the lists \( {\left( {x}_{i}\right) }_{i \in I} \) and \( {\left( {y}_{i}\right) }_{i \in J} \) are equal up to a permutation. We conclude with the induction hypothesis applied to \( {\left( {x}_{i}\right) }_{i \notin I} \) and \( {\left( {y}_{i}\right) }_{i \notin J} \) . (Another proof of this lemma, purely algebraic, consists of using the expression of symmetric coefficients as a function of Newton sums - see exercise 3 page 86 -, by first padding one of the two lists with zero terms so that they have the same size).

> Considérons maintenant les endomorphismes \( a \) et \( b \) de \( {\mathbb{R}}^{n} \) dont \( A \) et \( B \) sont les matrices dans la base canonique de \( {\mathbb{R}}^{n} \) . On a \( \operatorname{rg}a = p,\operatorname{rg}b = q,\operatorname{rg}\left( {a + b}\right) = r = p + q \) donc

Let us now consider the endomorphisms \( a \) and \( b \) of \( {\mathbb{R}}^{n} \) whose matrices in the canonical basis of \( {\mathbb{R}}^{n} \) are \( A \) and \( B \). We have \( \operatorname{rg}a = p,\operatorname{rg}b = q,\operatorname{rg}\left( {a + b}\right) = r = p + q \) therefore

\[
\dim \left( {\operatorname{Im}a \cap  \operatorname{Im}b}\right)  = \operatorname{rg}a + \operatorname{rg}b - \dim \left( {\operatorname{Im}a + \operatorname{Im}b}\right)  \leq  p + q - \operatorname{rg}\left( {a + b}\right)  = 0.
\]

Donc Im \( a \cap \operatorname{Im}b = \{ 0\} \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) une base orthonormée de Im \( a \) , et \( \left( {{f}_{1},\ldots ,{f}_{q}}\right) \) une base orthonormée de \( \operatorname{Im}b \) , de sorte que \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{p},{f}_{1},\ldots ,{f}_{q}}\right) \) est une base de \( E = \operatorname{Im}a \oplus \operatorname{Im}b \) . Le sous-espace \( F = {E}^{ \bot } = \operatorname{Im}{a}^{ \bot } \cap \operatorname{Im}{b}^{ \bot } = \operatorname{Ker}a \cap \operatorname{Ker}b \) est stable par \( a \) et \( b \) (car \( a \) et \( b \) s’annulent sur \( F) \) , donc \( E = {F}^{ \bot } \) est stable par \( a \) et \( b \) . Ainsi si on monte que \( {a}^{\prime } = {a}_{\mid E} \) et \( {b}^{\prime } = {b}_{\mid E} \) vérifient \( {a}^{\prime }{b}^{\prime } = 0 \) , on aura prouvé le résultat puisque \( {ab} = 0 \) sur \( F \) et que \( E \oplus F = {\mathbb{R}}^{n} \) . Déterminons les coefficients des matrices de \( {a}^{\prime } \) et \( {b}^{\prime } \) dans la base \( \mathcal{B} \) . Comme \( a\left( {f}_{i}\right) \in \operatorname{Im}a \) et \( a\left( {e}_{j}\right) = {\lambda }_{j}{e}_{j} \) , puis \( b\left( {e}_{i}\right) \in \operatorname{Im}b \) et \( b\left( {f}_{j}\right) = {\mu }_{j}{f}_{j} \) , compte tenu du caractère auto-adjoint de \( a \) et \( b \) on a

> Thus Im \( a \cap \operatorname{Im}b = \{ 0\} \). Let \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) be an orthonormal basis of Im \( a \), and \( \left( {{f}_{1},\ldots ,{f}_{q}}\right) \) be an orthonormal basis of \( \operatorname{Im}b \), such that \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{p},{f}_{1},\ldots ,{f}_{q}}\right) \) is a basis of \( E = \operatorname{Im}a \oplus \operatorname{Im}b \). The subspace \( F = {E}^{ \bot } = \operatorname{Im}{a}^{ \bot } \cap \operatorname{Im}{b}^{ \bot } = \operatorname{Ker}a \cap \operatorname{Ker}b \) is stable under \( a \) and \( b \) (since \( a \) and \( b \) vanish on \( F) \), therefore \( E = {F}^{ \bot } \) is stable under \( a \) and \( b \). Thus, if we show that \( {a}^{\prime } = {a}_{\mid E} \) and \( {b}^{\prime } = {b}_{\mid E} \) satisfy \( {a}^{\prime }{b}^{\prime } = 0 \), we will have proven the result since \( {ab} = 0 \) on \( F \) and that \( E \oplus F = {\mathbb{R}}^{n} \). Let us determine the coefficients of the matrices of \( {a}^{\prime } \) and \( {b}^{\prime } \) in the basis \( \mathcal{B} \). As \( a\left( {f}_{i}\right) \in \operatorname{Im}a \) and \( a\left( {e}_{j}\right) = {\lambda }_{j}{e}_{j} \), then \( b\left( {e}_{i}\right) \in \operatorname{Im}b \) and \( b\left( {f}_{j}\right) = {\mu }_{j}{f}_{j} \), given the self-adjoint nature of \( a \) and \( b \), we have

\[
a\left( {f}_{i}\right)  = \mathop{\sum }\limits_{{j = 1}}^{p}\left\langle  {{e}_{j}, a\left( {f}_{i}\right) }\right\rangle  {e}_{j} = \mathop{\sum }\limits_{{j = 1}}^{p}\left\langle  {a\left( {e}_{j}\right) ,{f}_{i}}\right\rangle  {e}_{j} = \mathop{\sum }\limits_{{j = 1}}^{p}{\lambda }_{j}\left\langle  {{e}_{j},{f}_{i}}\right\rangle  {e}_{j},
\]

\[
b\left( {e}_{i}\right)  = \mathop{\sum }\limits_{{j = 1}}^{q}\left\langle  {{f}_{j}, b\left( {e}_{i}\right) }\right\rangle  {f}_{j} = \mathop{\sum }\limits_{{j = 1}}^{q}\left\langle  {b\left( {f}_{j}\right) ,{e}_{i}}\right\rangle  {f}_{j} = \mathop{\sum }\limits_{{j = 1}}^{q}{\mu }_{j}\left\langle  {{f}_{j},{e}_{i}}\right\rangle  {f}_{j}.
\]

Notons \( {D}_{\lambda } \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) et \( {D}_{\mu } \in {\mathcal{M}}_{q}\left( \mathbb{R}\right) \) les matrices diagonales dont les coefficients diagonaux sont \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) et \( {\mu }_{1},\ldots ,{\mu }_{q} \) , puis \( M = {\left( \left\langle {e}_{i},{f}_{j}\right\rangle \right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{R}\right) \) . Les matrices de \( {a}^{\prime },{b}^{\prime } \) et \( {c}^{\prime } = {a}^{\prime } + {b}^{\prime } \) dans la base \( \mathcal{B} \) sont alors

> Let \( {D}_{\lambda } \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) and \( {D}_{\mu } \in {\mathcal{M}}_{q}\left( \mathbb{R}\right) \) be the diagonal matrices whose diagonal coefficients are \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) and \( {\mu }_{1},\ldots ,{\mu }_{q} \), then \( M = {\left( \left\langle {e}_{i},{f}_{j}\right\rangle \right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{R}\right) \). The matrices of \( {a}^{\prime },{b}^{\prime } \) and \( {c}^{\prime } = {a}^{\prime } + {b}^{\prime } \) in the basis \( \mathcal{B} \) are then

\[
{\left\lbrack  {a}^{\prime }\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} {D}_{\lambda } & {D}_{\lambda }M \\  0 & 0 \end{matrix}\right) ,\;{\left\lbrack  {b}^{\prime }\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} 0 & 0 \\  {D}_{\mu }{}^{\mathrm{t}}M & {D}_{\mu } \end{matrix}\right) ,\;{\left\lbrack  {c}^{\prime }\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} {D}_{\lambda } & {D}_{\lambda }M \\  {D}_{\mu }{}^{\mathrm{t}}M & {D}_{\mu } \end{matrix}\right) .
\]

On va montrer \( M = 0 \) ce qui prouvera \( {\left\lbrack {a}^{\prime }\right\rbrack }_{\mathcal{B}}{\left\lbrack {b}^{\prime }\right\rbrack }_{\mathcal{B}} = 0 \) , donc \( {a}^{\prime }{b}^{\prime } = 0 \) . On remarque que

> We will show \( M = 0 \) which will prove \( {\left\lbrack {a}^{\prime }\right\rbrack }_{\mathcal{B}}{\left\lbrack {b}^{\prime }\right\rbrack }_{\mathcal{B}} = 0 \) , thus \( {a}^{\prime }{b}^{\prime } = 0 \) . We note that

\[
{\left\lbrack  {c}^{\prime }\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} {D}_{\lambda } & 0 \\  0 & {D}_{\mu } \end{matrix}\right) N\;\text{ où }\;N = \left( \begin{matrix} {I}_{p} & M \\  {}^{\mathrm{t}}M & {I}_{q} \end{matrix}\right) ,
\]

d’où on déduit det \( {c}^{\prime } = \det {D}_{\lambda } \cdot \det {D}_{\mu } \cdot \det N \) . Or \( {c}^{\prime } = {c}_{\mid E} \) où \( c = a + b \) a pour matrice \( C \) dans la base canonique de \( {\mathbb{R}}^{n} \) , donc \( {c}^{\prime } \) a les mêmes valeurs propres non nulles \( {\lambda }_{1},\ldots ,{\lambda }_{p},{\mu }_{1},\ldots ,{\mu }_{q} \) que la matrice \( C \) , donc

> from which we deduce det \( {c}^{\prime } = \det {D}_{\lambda } \cdot \det {D}_{\mu } \cdot \det N \) . Now \( {c}^{\prime } = {c}_{\mid E} \) where \( c = a + b \) has matrix \( C \) in the canonical basis of \( {\mathbb{R}}^{n} \) , thus \( {c}^{\prime } \) has the same non-zero eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{p},{\mu }_{1},\ldots ,{\mu }_{q} \) as the matrix \( C \) , therefore

\[
\det {c}^{\prime } = \mathop{\prod }\limits_{{i = 1}}^{p}{\lambda }_{i}\mathop{\prod }\limits_{{i = 1}}^{q}{\mu }_{i} = \det {D}_{\lambda } \cdot  \det {D}_{\mu },
\]

d’où on déduit det \( N = 1 \) car les \( {\lambda }_{i} \) et \( {\mu }_{i} \) sont non nuls. Compte tenu de l’égalité

> from which we deduce det \( N = 1 \) because the \( {\lambda }_{i} \) and \( {\mu }_{i} \) are non-zero. Given the equality

\[
N\left( \begin{matrix} {I}_{p} &  - M \\  0 & {I}_{q} \end{matrix}\right)  = \left( \begin{matrix} {I}_{p} & 0 \\  {}^{\mathrm{t}}M &  - {}^{\mathrm{t}}{MM} + {I}_{q} \end{matrix}\right) ,
\]

on obtient \( 1 = \det N = \det \left( {{I}_{q} - {}^{\mathrm{t}}{MM}}\right) \) . La matrice \( S = {}^{\mathrm{t}}{MM} \in {\mathcal{M}}_{q}\left( \mathbb{R}\right) \) est symétrique, et positive car pour tout vecteur colonne \( X \) on a \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) {MX} = \parallel {MX}{\parallel }_{2} \geq 0 \) . Les valeurs propres \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) de \( S \) sont donc positives. Par ailleurs, pour tout vecteur colonne \( X = {\left( {x}_{i}\right) }_{1 \leq i \leq q} \) , la \( i \) -ième coordonnée de \( Y = {MX} \) est égale à

> we obtain \( 1 = \det N = \det \left( {{I}_{q} - {}^{\mathrm{t}}{MM}}\right) \) . The matrix \( S = {}^{\mathrm{t}}{MM} \in {\mathcal{M}}_{q}\left( \mathbb{R}\right) \) is symmetric, and positive because for any column vector \( X \) we have \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) {MX} = \parallel {MX}{\parallel }_{2} \geq 0 \) . The eigenvalues \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) of \( S \) are therefore positive. Furthermore, for any column vector \( X = {\left( {x}_{i}\right) }_{1 \leq i \leq q} \) , the \( i \) -th coordinate of \( Y = {MX} \) is equal to

\[
{y}_{i} = \mathop{\sum }\limits_{{j = 1}}^{q}\left\langle  {{e}_{i},{f}_{j}}\right\rangle  {x}_{j} = \left\langle  {{e}_{i}, Z}\right\rangle  \;\text{ où }\;Z = \mathop{\sum }\limits_{{j = 1}}^{q}{x}_{j}{f}_{j}.
\]

Ainsi \( Y \) est le vecteur des coordonnées de la projection orthogonale de \( Z \) sur \( \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{p}}\right) \) exprimé dans la base orthonormée \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) , donc \( \parallel Y{\parallel }_{2}^{2} \leq \parallel Z{\parallel }_{2}^{2} = {x}_{1}^{2} + \cdots + {x}_{q}^{2} = \parallel X{\parallel }_{2}^{2} \) . On en déduit \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) \left( {MX}\right) = \parallel Y{\parallel }_{2}^{2} \leq \parallel X{\parallel }_{2}^{2} \) , donc on a \( {\alpha }_{i} \leq 1 \) pour tout \( i \) . Or \( \det N = \det \left( {{I}_{q} - S}\right) = \mathop{\prod }\limits_{{i = 1}}^{q}\left( {1 - {\alpha }_{i}}\right) \) , et comme det \( N = 1 \) et que \( 0 \leq {\alpha }_{i} \leq 1 \) pour tout \( i \) , les \( {\alpha }_{i} \) sont forcément tous nuls donc \( S = 0 \) , ce qui implique \( M = 0 \) (si \( M \neq 0 \) alors il existe un vecteur colonne \( X \) vérifiant \( {MX} \neq 0 \) , donc \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) {MX} > 0 \) , ce qui est impossible). Compte tenu de la forme des matrices de \( {a}^{\prime } \) et \( {b}^{\prime } \) dans la base \( \mathcal{B} \) , on en déduit que \( {a}^{\prime }{b}^{\prime } = 0 \) , d’où le résultat.

> Thus \( Y \) is the coordinate vector of the orthogonal projection of \( Z \) onto \( \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{p}}\right) \) expressed in the orthonormal basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \), so \( \parallel Y{\parallel }_{2}^{2} \leq \parallel Z{\parallel }_{2}^{2} = {x}_{1}^{2} + \cdots + {x}_{q}^{2} = \parallel X{\parallel }_{2}^{2} \). We deduce \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) \left( {MX}\right) = \parallel Y{\parallel }_{2}^{2} \leq \parallel X{\parallel }_{2}^{2} \), so we have \( {\alpha }_{i} \leq 1 \) for all \( i \). However \( \det N = \det \left( {{I}_{q} - S}\right) = \mathop{\prod }\limits_{{i = 1}}^{q}\left( {1 - {\alpha }_{i}}\right) \), and since det \( N = 1 \) and \( 0 \leq {\alpha }_{i} \leq 1 \) for all \( i \), the \( {\alpha }_{i} \) must all be zero, so \( S = 0 \), which implies \( M = 0 \) (if \( M \neq 0 \) then there exists a column vector \( X \) satisfying \( {MX} \neq 0 \), so \( {}^{\mathrm{t}}{XSX} = {}^{\mathrm{t}}\left( {MX}\right) {MX} > 0 \), which is impossible). Given the form of the matrices of \( {a}^{\prime } \) and \( {b}^{\prime } \) in the basis \( \mathcal{B} \), we deduce that \( {a}^{\prime }{b}^{\prime } = 0 \), hence the result.

Problem 14. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice symétrique définie positive. Montrer que la matrice

> Problem 14. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a symmetric positive definite matrix. Show that the matrix

\[
B = {\left( \frac{{a}_{i, j}}{i + j}\right) }_{1 \leq  i, j \leq  n}
\]

est définie positive.

> is positive definite.

Solution. On considère l'application

> Solution. Consider the mapping

\[
A : \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;t \mapsto  A\left( t\right)  = {\left( {a}_{i, j} \cdot  {t}^{i + j - 1}\right) }_{1 \leq  i, j \leq  n}.
\]

Si on montre que \( A\left( t\right) \) est définie positive pour tout \( t \in \rbrack 0,1\left\lbrack \right. \) , alors d’après l’exercice 5 page 260, on aura prouvé que la matrice

> If we show that \( A\left( t\right) \) is positive definite for all \( t \in \rbrack 0,1\left\lbrack \right. \), then according to exercise 5 on page 260, we will have proven that the matrix

\[
{\int }_{0}^{1}A\left( t\right) {dt} = {\left( {\int }_{0}^{1}{a}_{i, j}{t}^{i + j - 1}dt\right) }_{1 \leq  i, j \leq  n} = {\left( \frac{{a}_{i, j}}{i + j}\right) }_{1 \leq  i, j \leq  n} = B
\]

est définie positive.

> is positive definite.

Or si \( t > 0 \) on a, pour tout vecteur colonne non nul \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \) l’égalité

> However, if \( t > 0 \) we have, for any non-zero column vector \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \), the equality

\[
{}^{\mathrm{t}}{XA}\left( t\right) X = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{t}^{i + j - 1}{x}_{i}{x}_{j} = t \cdot  \mathop{\sum }\limits_{{i, j}}{a}_{i, j}\left( {{x}_{i}{t}^{i - 1}}\right) \left( {{x}_{j}{t}^{j - 1}}\right)  = t \cdot  \left( {{}^{\mathrm{t}}{X}_{t}A{X}_{t}}\right) ,\;{X}_{t} = \left( \begin{matrix} {x}_{1} \\  t{x}_{2} \\  \vdots \\  {t}^{n - 1}{x}_{n} \end{matrix}\right)
\]

et comme \( A \) est définie positive, on en déduit \( {}^{\mathrm{t}}{XA}\left( t\right) X = t\left( {{}^{\mathrm{t}}{X}_{t}A{X}_{t}}\right) > 0 \) . Ainsi, \( A\left( t\right) \) est bien définie positive pour tout \( t > 0 \) , d’où le résultat.

> and since \( A \) is positive definite, we deduce \( {}^{\mathrm{t}}{XA}\left( t\right) X = t\left( {{}^{\mathrm{t}}{X}_{t}A{X}_{t}}\right) > 0 \). Thus, \( A\left( t\right) \) is indeed positive definite for all \( t > 0 \), hence the result.

Problem 15. Soit \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) un polynôme de degré \( n \geq 1 \) , dont on note \( {\left( {\alpha }_{i}\right) }_{1 \leq i \leq n} \) les racines complexes. Pour tout \( k \in \mathbb{N} \) , on note \( {s}_{k} = \mathop{\sum }\limits_{{i = 1}}^{n}{\alpha }_{i}^{k} \) et on considère la matrice

> Problem 15. Let \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) be a polynomial of degree \( n \geq 1 \), whose complex roots are denoted by \( {\left( {\alpha }_{i}\right) }_{1 \leq i \leq n} \). For any \( k \in \mathbb{N} \), we denote \( {s}_{k} = \mathop{\sum }\limits_{{i = 1}}^{n}{\alpha }_{i}^{k} \) and consider the matrix

\[
A = \left( \begin{matrix} {s}_{0} & {s}_{1} & \cdots & {s}_{n - 1} \\  {s}_{1} & {s}_{2} & & {s}_{n} \\  \vdots & & & \vdots \\  {s}_{n - 1} & {s}_{n} & \cdots & {s}_{{2n} - 2} \end{matrix}\right) .
\]

On note \( q \) la forme quadratique dont \( A \) est la matrice dans la base canonique de \( {\mathbb{R}}^{n} \) . Montrer que la signature de \( q \) est égale à \( \left( {r + s, s}\right) \) où \( r \) est le nombre de racines réelles distinctes de \( P \) et \( {2s} \) le nombre de racines complexes non réelles distinctes de \( P \) .

> Let \( q \) be the quadratic form whose matrix in the canonical basis of \( {\mathbb{R}}^{n} \) is \( A \). Show that the signature of \( q \) is equal to \( \left( {r + s, s}\right) \), where \( r \) is the number of distinct real roots of \( P \) and \( {2s} \) is the number of distinct non-real complex roots of \( P \).

Solution. Notons \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) la base canonique de \( {\mathbb{R}}^{n} \) . On remarque tout d’abord que

> Solution. Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be the canonical basis of \( {\mathbb{R}}^{n} \). We first note that

\[
q\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i}}\right)  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}{s}_{i + j - 2}{x}_{i}{x}_{j} = \mathop{\sum }\limits_{{1 \leq  i, j, k \leq  n}}{\alpha }_{k}^{i + j - 2}{x}_{i}{x}_{j} = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( \mathop{\sum }\limits_{{\ell  = 1}}^{n}{\alpha }_{k}^{\ell  - 1}{x}_{\ell }\right) }^{2}.
\]

Autrement dit, on peut écrire

> In other words, we can write

\[
\forall x \in  {\mathbb{R}}^{n},\;q\left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}{f}_{{\alpha }_{k}}{\left( x\right) }^{2}\;\text{ où }\;{f}_{\alpha }\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i}}\right)  = \mathop{\sum }\limits_{{\ell  = 1}}^{n}{\alpha }^{\ell  - 1}{x}_{\ell }.
\]

Notons \( {\beta }_{1},\ldots ,{\beta }_{r} \) les racines réelles distinctes de \( P \) et \( {m}_{1},\ldots ,{m}_{r} \) leur ordre de multiplicité respectives, et \( {\gamma }_{1},{\overline{\gamma }}_{1},\ldots ,{\gamma }_{s},{\overline{\gamma }}_{s} \) les racines complexes non réelles distinctes de \( P \) , l’ordre de mul-tiplicité de \( {\gamma }_{i} \) étant noté \( {n}_{i} \) . On peut écrire

> Let \( {\beta }_{1},\ldots ,{\beta }_{r} \) be the distinct real roots of \( P \) and \( {m}_{1},\ldots ,{m}_{r} \) their respective multiplicities, and \( {\gamma }_{1},{\overline{\gamma }}_{1},\ldots ,{\gamma }_{s},{\overline{\gamma }}_{s} \) be the distinct non-real complex roots of \( P \), with the multiplicity of \( {\gamma }_{i} \) denoted by \( {n}_{i} \). We can write

\[
\forall x \in  {\mathbb{R}}^{n},\;q\left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}{m}_{k}{f}_{{\beta }_{k}}{\left( x\right) }^{2} + \mathop{\sum }\limits_{{k = 1}}^{s}{n}_{k}\left( {{f}_{{\gamma }_{k}}{\left( x\right) }^{2} + {f}_{{\overline{\gamma }}_{k}}{\left( x\right) }^{2}}\right) .
\]

Pour tout \( k,1 \leq k \leq s \) , notons \( {u}_{k} \) et \( {v}_{k} \) les parties réelles et imaginaires de \( {f}_{{\gamma }_{k}} \) , de sorte que \( {f}_{{\gamma }_{k}} = {u}_{k} + i{v}_{k} \) et \( {f}_{{\overline{\gamma }}_{k}} = {u}_{k} - i{v}_{k} \) . On a \( {f}_{{\gamma }_{k}}^{2} + {f}_{{\overline{\gamma }}_{k}}^{2} = 2{u}_{k}^{2} - 2{v}_{k}^{2} \) , donc finalement

> For any \( k,1 \leq k \leq s \), let \( {u}_{k} \) and \( {v}_{k} \) be the real and imaginary parts of \( {f}_{{\gamma }_{k}} \), such that \( {f}_{{\gamma }_{k}} = {u}_{k} + i{v}_{k} \) and \( {f}_{{\overline{\gamma }}_{k}} = {u}_{k} - i{v}_{k} \). We have \( {f}_{{\gamma }_{k}}^{2} + {f}_{{\overline{\gamma }}_{k}}^{2} = 2{u}_{k}^{2} - 2{v}_{k}^{2} \), so finally

\[
\forall x \in  {\mathbb{R}}^{n},\;q\left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{r}{m}_{k}{f}_{{\beta }_{k}}{\left( x\right) }^{2} + \mathop{\sum }\limits_{{k = 1}}^{s}2{n}_{k}\left( {{u}_{k}{\left( x\right) }^{2} - {v}_{k}{\left( x\right) }^{2}}\right) .
\]

Ainsi, \( q \) s’écrit sous la forme de la somme de \( r + s \) carrés de formes linéaires sur \( {\mathbb{R}}^{n} \) retranché à la somme de \( s \) carrés de formes linéaires sur \( {\mathbb{R}}^{n} \) . Nous allons montrer que les formes linéaires en présence sont linéairement indépendantes, ce qui prouvera que la signature de \( q \) est \( \left( {r + s, s}\right) \) .

> Thus, \( q \) is written as the sum of \( r + s \) squares of linear forms on \( {\mathbb{R}}^{n} \) minus the sum of \( s \) squares of linear forms on \( {\mathbb{R}}^{n} \). We will show that the linear forms involved are linearly independent, which will prove that the signature of \( q \) is \( \left( {r + s, s}\right) \).

Pour prouver que ces formes linéaires forment une famille libre dans \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) , il revient au même de montrer que les matrices de ces formes linéaires sont linéairement indépendantes. Notons \( {A}_{k} = \; \left( {1,{\beta }_{k},\ldots ,{\beta }_{k}^{n - 1}}\right) \) la matrice de \( {f}_{{\beta }_{k}} \) dans la base canonique de \( {\mathbb{R}}^{n},{U}_{k} \) celle de \( {u}_{k} \) et \( {V}_{k} \) celle de \( {v}_{k} \) . On a \( {U}_{k} + i{V}_{k} = \left( {1,{\gamma }_{k},\ldots ,{\gamma }_{k}^{n - 1}}\right) \) . Soit \( p = r + {2s} \) et considérons la matrice \( M \in {\mathcal{M}}_{p, n}\left( \mathbb{R}\right) \) dont les lignes sont constituées des matrices \( {A}_{k},{U}_{k} \) et \( {V}_{k} \) , ce que nous notons par commodité sous la forme \( M = L\left( {{A}_{1},\ldots ,{A}_{r},{U}_{1},\ldots ,{U}_{s},{V}_{1},\ldots ,{V}_{s}}\right) \) . Soit \( {M}^{\prime } \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) la matrice carrée extraite de \( M \) en ne conservant que les \( p \) premières colonnes. En notant \( {A}_{k}^{\prime },{U}_{k}^{\prime } \) et \( {V}_{k}^{\prime } \) les matrices lignes constituées des \( p \) premiers coefficients de \( {A}_{k},{U}_{k} \) et \( {V}_{k} \) , on a \( {M}^{\prime } = L\left( {{A}_{1}^{\prime },\ldots ,{A}_{r}^{\prime },{U}_{1}^{\prime },\ldots ,{U}_{s}^{\prime },{V}_{1}^{\prime },\ldots ,{V}_{s}^{\prime }}\right) \) . Regardons \( {M}^{\prime } \) comme une matrice complexe. Son rang est inchangé en ajoutant à une ligne une combinaison linéaire (à coefficients complexes) d'autres lignes, ou en multipliant une ligne par un scalaire non nul. Ainsi, \( {M}^{\prime } \) a le même rang que la matrice

> To prove that these linear forms constitute a linearly independent family in \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \), it is equivalent to show that the matrices of these linear forms are linearly independent. Let \( {A}_{k} = \; \left( {1,{\beta }_{k},\ldots ,{\beta }_{k}^{n - 1}}\right) \) be the matrix of \( {f}_{{\beta }_{k}} \) in the canonical basis of \( {\mathbb{R}}^{n},{U}_{k} \), that of \( {u}_{k} \), and \( {V}_{k} \) that of \( {v}_{k} \). We have \( {U}_{k} + i{V}_{k} = \left( {1,{\gamma }_{k},\ldots ,{\gamma }_{k}^{n - 1}}\right) \). Let \( p = r + {2s} \) and consider the matrix \( M \in {\mathcal{M}}_{p, n}\left( \mathbb{R}\right) \) whose rows are composed of the matrices \( {A}_{k},{U}_{k} \) and \( {V}_{k} \), which we denote for convenience as \( M = L\left( {{A}_{1},\ldots ,{A}_{r},{U}_{1},\ldots ,{U}_{s},{V}_{1},\ldots ,{V}_{s}}\right) \). Let \( {M}^{\prime } \in {\mathcal{M}}_{p}\left( \mathbb{R}\right) \) be the square matrix extracted from \( M \) by keeping only the first \( p \) columns. By denoting \( {A}_{k}^{\prime },{U}_{k}^{\prime } \) and \( {V}_{k}^{\prime } \) as the row matrices composed of the first \( p \) coefficients of \( {A}_{k},{U}_{k} \) and \( {V}_{k} \), we have \( {M}^{\prime } = L\left( {{A}_{1}^{\prime },\ldots ,{A}_{r}^{\prime },{U}_{1}^{\prime },\ldots ,{U}_{s}^{\prime },{V}_{1}^{\prime },\ldots ,{V}_{s}^{\prime }}\right) \). Let us view \( {M}^{\prime } \) as a complex matrix. Its rank remains unchanged by adding a linear combination (with complex coefficients) of other rows to a row, or by multiplying a row by a non-zero scalar. Thus, \( {M}^{\prime } \) has the same rank as the matrix

\[
N = L\left( {{A}_{1}^{\prime },\ldots ,{A}_{r}^{\prime },{U}_{1}^{\prime } + i{V}_{1}^{\prime },\ldots ,{U}_{s}^{\prime } + i{V}_{s}^{\prime },{U}_{1}^{\prime } - i{V}_{1}^{\prime },\ldots ,{U}_{s}^{\prime } - i{V}_{s}^{\prime }}\right) .
\]

Cette matrice est la matrice de Vandermonde \( V\left( {{\beta }_{1},\ldots ,{\beta }_{r},{\gamma }_{1},\ldots ,{\gamma }_{s},{\overline{\gamma }}_{1},\ldots ,{\overline{\gamma }}_{s}}\right) \) , et comme les \( {\beta }_{k} \) , les \( {\gamma }_{k} \) et \( {\overline{\gamma }}_{k} \) sont distincts deux à deux, on en déduit que \( N \) est inversible. Donc \( \operatorname{rg}\left( {M}^{\prime }\right) = \; \operatorname{rg}\left( N\right) = p \) , donc \( {M}^{\prime } \) est inversible dans \( {\mathcal{M}}_{p}\left( \mathbb{C}\right) \) . Comme \( {M}^{\prime } \) est une matrice réelle, son inverse est une matrice réelle, donc le rang de \( {M}^{\prime } \) vu comme une matrice réelle est aussi égal à \( p \) . Ainsi, on en déduit \( \operatorname{rg}\left( M\right) = p \) donc les formes linéaires \( {f}_{{\beta }_{k}},{u}_{k} \) et \( {v}_{k} \) forment bien une famille libre, d'où le résultat.

> This matrix is the Vandermonde matrix \( V\left( {{\beta }_{1},\ldots ,{\beta }_{r},{\gamma }_{1},\ldots ,{\gamma }_{s},{\overline{\gamma }}_{1},\ldots ,{\overline{\gamma }}_{s}}\right) \), and since the \( {\beta }_{k} \), the \( {\gamma }_{k} \), and the \( {\overline{\gamma }}_{k} \) are pairwise distinct, we deduce that \( N \) is invertible. Therefore \( \operatorname{rg}\left( {M}^{\prime }\right) = \; \operatorname{rg}\left( N\right) = p \), so \( {M}^{\prime } \) is invertible in \( {\mathcal{M}}_{p}\left( \mathbb{C}\right) \). Since \( {M}^{\prime } \) is a real matrix, its inverse is a real matrix, so the rank of \( {M}^{\prime } \) viewed as a real matrix is also equal to \( p \). Thus, we deduce \( \operatorname{rg}\left( M\right) = p \), so the linear forms \( {f}_{{\beta }_{k}},{u}_{k} \) and \( {v}_{k} \) indeed form a linearly independent family, hence the result.

Remarque. Les coefficients \( {s}_{k} \) sont les sommes de Newton des racines de \( P \) , et peuvent se calculer aisément à partir des coefficients de \( P \) grâce aux formules de Newton (voir l'exercice 3 page 86).

> Remark. The coefficients \( {s}_{k} \) are the Newton sums of the roots of \( P \), and can be easily calculated from the coefficients of \( P \) using Newton's formulas (see exercise 3 on page 86).

Problem 16. Soient \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) deux matrices réelles unitairement semblables, i.e.

> Problem 16. Let \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be two unitarily similar real matrices, i.e.

\[
\exists U \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) , U\text{ unitaire, }\;A = {}^{\mathrm{t}}\bar{U}{BU}.
\]

Montrer que \( A \) et \( B \) sont orthogonalement semblables, c’est-à-dire

> Show that \( A \) and \( B \) are orthogonally similar, that is to say

\[
\exists \Omega  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\Omega \text{ orthogonale, }\;A = {}^{\mathrm{t}}{\Omega B\Omega }\text{ . }
\]

(Indication : montrer l’existence de \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) telle que \( A = {P}^{-1}{BP}{\mathrm{{et}}}^{\mathrm{t}}A = {P}^{-1}{}^{\mathrm{t}}{BP} \) , puis considérer la décomposition polaire \( P = {\Omega S} \) , avec \( \Omega \) orthogonale et \( S \) symétrique - voir l'exercice 6 page 261.)

> (Hint: show the existence of \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that \( A = {P}^{-1}{BP}{\mathrm{{et}}}^{\mathrm{t}}A = {P}^{-1}{}^{\mathrm{t}}{BP} \), then consider the polar decomposition \( P = {\Omega S} \), with \( \Omega \) orthogonal and \( S \) symmetric - see exercise 6 on page 261.)

Solution. Suivons l'indication et commençons par montrer l'existence d'une matrice réelle inver-sible \( P \) telle que \( {PA} = {BP} \) et \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \) . Le principe ressemble à la solution de la question a) du problème 14 page 167 (c’est classique). On écrit la matrice unitaire \( U \) sous la forme \( U = {U}_{1} + i{U}_{2} \) , où \( {U}_{1},{U}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . L’égalité \( A = \bar{U}{BU} \) entraîne \( {UA} = {BU} \) et \( {U}^{\mathrm{t}}A = {}^{\mathrm{t}}{BU} \) , donc

> Solution. Let us follow the hint and begin by showing the existence of an invertible real matrix \( P \) such that \( {PA} = {BP} \) and \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \). The principle is similar to the solution of question a) of problem 14 on page 167 (it is standard). We write the unitary matrix \( U \) in the form \( U = {U}_{1} + i{U}_{2} \), where \( {U}_{1},{U}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). The equality \( A = \bar{U}{BU} \) implies \( {UA} = {BU} \) and \( {U}^{\mathrm{t}}A = {}^{\mathrm{t}}{BU} \), therefore

\[
{U}_{1}A = B{U}_{1},\;{U}_{2}A = B{U}_{2}\;\text{ et }\;{U}_{1}^{\mathrm{t}}A = {}^{\mathrm{t}}B{U}_{1},\;{U}_{2}^{\mathrm{t}}A = {}^{\mathrm{t}}B{U}_{2}.
\]

(*)

> Le polynôme \( \varphi \left( X\right) = \det \left( {{U}_{1} + X{U}_{2}}\right) \in \mathbb{R}\left\lbrack X\right\rbrack \) ne s’annule pas puisque \( \varphi \left( i\right) = \det U \neq 0 \) , donc n’a qu’un nombre fini de racines. En choisissant \( x \in \mathbb{R} \) tel que \( \varphi \left( x\right) \neq 0 \) , la matrice \( P = {U}_{1} + x{U}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est inversible et par linéarité, les égalités (*) donnent \( {PA} = {BP} \) et \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \) .

The polynomial \( \varphi \left( X\right) = \det \left( {{U}_{1} + X{U}_{2}}\right) \in \mathbb{R}\left\lbrack X\right\rbrack \) does not vanish since \( \varphi \left( i\right) = \det U \neq 0 \), and thus has only a finite number of roots. By choosing \( x \in \mathbb{R} \) such that \( \varphi \left( x\right) \neq 0 \), the matrix \( P = {U}_{1} + x{U}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is invertible and by linearity, the equalities (*) give \( {PA} = {BP} \) and \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \).

> Nous considérons maintenant la décomposition polaire de \( P \) . Nous la retrouvons ici dans le cas des matrices réelles (l'exercice 6 page 261 traite le cas des matrices complexes). La matrice \( {}^{\mathrm{t}}{PP} \) est symétrique positive (c’est classique, la positivité provient de l’identité \( {}^{\mathrm{t}}X\left( {{}^{\mathrm{t}}{PP}}\right) X = \; {}^{\mathrm{t}}\left( {PX}\right) \left( {PX}\right) = \parallel {PX}{\parallel }^{2} \) ), donc on peut trouver une matrice symétrique positive \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) telle que \( {}^{\mathrm{t}}{PP} = {S}^{2} \) (c’est également classique, il suffit de diagonaliser \( {}^{\mathrm{t}}{PP} \) dans une base orthonormée, voir l’exercice 1 page 257). Comme \( P \) est inversible, \( S \) l’est également et la matrice \( \Omega = P{S}^{-1} \) vérifie \( {}^{\mathrm{t}}{\Omega \Omega } = {S}^{-1}\left( {{}^{\mathrm{t}}{PP}}\right) {S}^{-1} = {I}_{n} \) , donc est orthogonale. Ainsi, on a \( P = {\Omega S} \) avec \( \Omega \) orthogonale et \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) symétrique définie positive.

We now consider the polar decomposition of \( P \). We revisit it here in the case of real matrices (exercise 6 on page 261 covers the case of complex matrices). The matrix \( {}^{\mathrm{t}}{PP} \) is symmetric positive (this is standard; positivity follows from the identity \( {}^{\mathrm{t}}X\left( {{}^{\mathrm{t}}{PP}}\right) X = \; {}^{\mathrm{t}}\left( {PX}\right) \left( {PX}\right) = \parallel {PX}{\parallel }^{2} \)), so we can find a symmetric positive matrix \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that \( {}^{\mathrm{t}}{PP} = {S}^{2} \) (this is also standard; it suffices to diagonalize \( {}^{\mathrm{t}}{PP} \) in an orthonormal basis, see exercise 1 on page 257). Since \( P \) is invertible, \( S \) is as well, and the matrix \( \Omega = P{S}^{-1} \) satisfies \( {}^{\mathrm{t}}{\Omega \Omega } = {S}^{-1}\left( {{}^{\mathrm{t}}{PP}}\right) {S}^{-1} = {I}_{n} \), thus it is orthogonal. Therefore, we have \( P = {\Omega S} \) with \( \Omega \) orthogonal and \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) symmetric positive definite.

> Achevons notre raisonnement. En prenant en compte la forme polaire de \( P \) , les égalités \( {PA} = {BP} \) et \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \) entraînent respectivement

Let us complete our reasoning. By taking into account the polar form of \( P \), the equalities \( {PA} = {BP} \) and \( {P}^{\mathrm{t}}A = {}^{\mathrm{t}}{BP} \) respectively lead to

\[
A = {P}^{-1}{BP} = {S}^{-1}{}^{\mathrm{t}}{\Omega B\Omega S}\;\text{ et }\;A = {}^{\mathrm{t}}P{B}^{\mathrm{t}}{P}^{-1} = {S}^{\mathrm{t}}{\Omega B\Omega }{S}^{-1}.
\]

On en déduit \( {SA}{S}^{-1} = {S}^{-1}{AS} \) , donc \( {S}^{2} \) commute avec \( A \) . Nous allons montrer que cela entraîne le fait que \( S \) et \( A \) commutent. Pour cela, désignons par \( 0 < {\lambda }_{1} < \ldots < {\lambda }_{r} \) les valeurs propres de \( S \) et \( {\left( {E}_{{\lambda }_{i}}\left( S\right) \right) }_{1 \leq i \leq r} \) les sous-espaces propres associés. En diagonalisant \( S \) , on s’aperçoit que \( S \) et \( {S}^{2} \) ont les mêmes sous-espaces propres : \( {E}_{{\lambda }_{i}}\left( S\right) = {E}_{{\lambda }_{i}^{2}}\left( {S}^{2}\right) \) . Maintenant, si \( x \in {E}_{{\lambda }_{i}}\left( S\right) \) , on a \( {S}^{2}{Ax} = A{S}^{2}x \) ce qui entraîne \( {S}^{2}\left( {Ax}\right) = {\lambda }_{i}^{2}\left( {Ax}\right) \) . On en déduit \( {Ax} \in {E}_{{\lambda }_{i}^{2}}\left( {S}^{2}\right) \) , donc \( {Ax} \in {E}_{{\lambda }_{i}}\left( S\right) \) , donc \( {SAx} = {\lambda }_{i}{Ax} = {ASx} \) . Ainsi, \( A \) et \( S \) commutent sur chaque sous-espace propre de \( S \) , donc sur \( {\mathbb{R}}^{n} \) tout entier. En repartant de \( A = {S}^{-1}{}^{\mathrm{t}}{\Omega B\Omega S} \) , on en déduit \( {AS} = {SA} = {}^{\mathrm{t}}{\Omega B\Omega S} \) , donc \( A = {}^{\mathrm{t}}{\Omega B\Omega } \) est orthogonalement semblable à \( B \) .

> We deduce \( {SA}{S}^{-1} = {S}^{-1}{AS} \), so \( {S}^{2} \) commutes with \( A \). We will show that this implies that \( S \) and \( A \) commute. To do this, let \( 0 < {\lambda }_{1} < \ldots < {\lambda }_{r} \) be the eigenvalues of \( S \) and \( {\left( {E}_{{\lambda }_{i}}\left( S\right) \right) }_{1 \leq i \leq r} \) the associated eigenspaces. By diagonalizing \( S \), we see that \( S \) and \( {S}^{2} \) have the same eigenspaces: \( {E}_{{\lambda }_{i}}\left( S\right) = {E}_{{\lambda }_{i}^{2}}\left( {S}^{2}\right) \). Now, if \( x \in {E}_{{\lambda }_{i}}\left( S\right) \), we have \( {S}^{2}{Ax} = A{S}^{2}x \) which implies \( {S}^{2}\left( {Ax}\right) = {\lambda }_{i}^{2}\left( {Ax}\right) \). We deduce \( {Ax} \in {E}_{{\lambda }_{i}^{2}}\left( {S}^{2}\right) \), so \( {Ax} \in {E}_{{\lambda }_{i}}\left( S\right) \), therefore \( {SAx} = {\lambda }_{i}{Ax} = {ASx} \). Thus, \( A \) and \( S \) commute on each eigenspace of \( S \), and therefore on \( {\mathbb{R}}^{n} \) as a whole. Starting again from \( A = {S}^{-1}{}^{\mathrm{t}}{\Omega B\Omega S} \), we deduce \( {AS} = {SA} = {}^{\mathrm{t}}{\Omega B\Omega S} \), so \( A = {}^{\mathrm{t}}{\Omega B\Omega } \) is orthogonally similar to \( B \).

Remarque. On montre de même que deux matrices symétriques réelles semblables sont orthogonalement semblables.

> Remark. It can be shown similarly that two similar real symmetric matrices are orthogonally similar.

PROBLEME 17 (HAUSDORFFIEN D'UNE APPLICATION LINEAIRE EN DIMENSION FINIE). Soit \( E \) un espace hermitien de dimension finie \( n \in {\mathbb{N}}^{ * } \) . 1 / Soit \( f \in \mathcal{L}\left( E\right) \) . On appelle Hausdorffien de \( f \) le sous-ensemble de \( \mathbb{C} \) défini par

> PROBLEM 17 (HAUSDORFFIAN OF A LINEAR MAP IN FINITE DIMENSION). Let \( E \) be a finite-dimensional Hermitian space \( n \in {\mathbb{N}}^{ * } \). 1 / Let \( f \in \mathcal{L}\left( E\right) \). The Hausdorffian of \( f \) is the subset of \( \mathbb{C} \) defined by

\[
H\left( f\right)  = \left\{  {\left. \frac{f\left( x\right)  \cdot  x}{x \cdot  x}\right| \;x \in  E\smallsetminus \{ 0\} }\right\}   = \{ f\left( x\right)  \cdot  x \mid  \parallel x\parallel  = 1\} .
\]

a) Montrer que \( H\left( f\right) \) est convexe et compact. (Indication : pour montrer que \( \left\lbrack {\xi ,\eta }\right\rbrack \subset H\left( f\right) \) si \( \xi ,\eta \in H\left( f\right) \) , on se ramènera à montrer que \( \left\lbrack {0,1}\right\rbrack \subset H\left( g\right) \) où \( g = {\alpha f} + \beta \) Id avec \( \alpha \) et \( \beta \) bien choisis. Puis on écrira \( g = u + {iv} \) , avec \( u \) et \( v \) autoadjoints.)

> a) Show that \( H\left( f\right) \) is convex and compact. (Hint: to show that \( \left\lbrack {\xi ,\eta }\right\rbrack \subset H\left( f\right) \) if \( \xi ,\eta \in H\left( f\right) \), reduce it to showing that \( \left\lbrack {0,1}\right\rbrack \subset H\left( g\right) \) where \( g = {\alpha f} + \beta \) Id with \( \alpha \) and \( \beta \) well chosen. Then write \( g = u + {iv} \), with \( u \) and \( v \) self-adjoint.)

b) Si \( f \) se diagonalise dans une base orthonormale, déterminer \( H\left( f\right) \) .

> b) If \( f \) diagonalizes in an orthonormal basis, determine \( H\left( f\right) \).

2 / Soit \( f \in \mathcal{L}\left( E\right) \) telle que tr \( f = 0 \) . Montrer l’existence d’une base \( B \) orthonormale de \( E \) dans laquelle la matrice de \( f \) ait tout ses termes diagonaux nuls.

> 2 / Let \( f \in \mathcal{L}\left( E\right) \) such that tr \( f = 0 \). Show the existence of an orthonormal basis \( B \) of \( E \) in which the matrix of \( f \) has all its diagonal terms equal to zero.

Solution. \( 1/ \) a) L’ensemble \( H\left( f\right) \) est compact car c’est l’image par l’application continue \( x \mapsto \; f\left( x\right) \cdot x \) du compact \( \{ x \in E,\parallel x\parallel = 1\} \) .

> Solution. \( 1/ \) a) The set \( H\left( f\right) \) is compact because it is the image under the continuous map \( x \mapsto \; f\left( x\right) \cdot x \) of the compact set \( \{ x \in E,\parallel x\parallel = 1\} \) .

Montrons que \( H\left( f\right) \) est convexe. Donnons nous \( x, y \in E,\parallel x\parallel = \parallel y\parallel = 1 \) et posons \( \xi = f\left( x\right) \cdot x \) et \( \eta = f\left( y\right) \cdot y \) . Il s’agit de montrer \( \left\lbrack {\xi ,\eta }\right\rbrack \subset H\left( f\right) \) . Si \( \xi = \eta \) c’est terminé. Sinon, \( \xi \neq \eta \) , et on va se ramener sur \( \left\lbrack {0,1}\right\rbrack \) . Il existe deux nombres complexes \( \alpha \) et \( \beta \) tels que

> Let us show that \( H\left( f\right) \) is convex. Let \( x, y \in E,\parallel x\parallel = \parallel y\parallel = 1 \) be given and let \( \xi = f\left( x\right) \cdot x \) and \( \eta = f\left( y\right) \cdot y \) . We must show \( \left\lbrack {\xi ,\eta }\right\rbrack \subset H\left( f\right) \) . If \( \xi = \eta \) we are done. Otherwise, \( \xi \neq \eta \) , and we will reduce to \( \left\lbrack {0,1}\right\rbrack \) . There exist two complex numbers \( \alpha \) and \( \beta \) such that

\[
{\alpha \xi } + \beta  = 1\;\text{ et }\;{\alpha \eta } + \beta  = 0.
\]

On pose \( g = {\alpha f} + \beta {\operatorname{Id}}_{E} \) . On a

> Let \( g = {\alpha f} + \beta {\operatorname{Id}}_{E} \) . We have

\[
\left\lbrack  {\xi ,\eta }\right\rbrack   \subset  H\left( f\right)  \Leftrightarrow  \forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\;{t\xi } + \left( {1 - t}\right) \eta  \in  H\left( f\right)
\]

\[
\Leftrightarrow  \forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\exists z \in  E,\parallel z\parallel  = 1,\;{t\xi } + \left( {1 - t}\right) \eta  = f\left( z\right)  \cdot  z
\]

\[
\Leftrightarrow  \forall t \in  \left\lbrack  {0,1}\right\rbrack  ,\exists z \in  E,\parallel z\parallel  = 1,\;t = \alpha \left( {{t\xi } + \left( {1 - t}\right) \eta }\right)  + \beta  = g\left( z\right)  \cdot  z
\]

\[
\Leftrightarrow  \left\lbrack  {0,1}\right\rbrack   \subset  H\left( g\right) \text{ . }
\]

Montrons donc \( \left\lbrack {0,1}\right\rbrack \subset H\left( g\right) \) . On sait que \( g\left( x\right) \cdot x = 1 \) et \( g\left( y\right) \cdot y = 0 \) . Écrivons \( g = u + {iv} \) avec \( u \) et \( v \) autoadjoints (il suffit de prendre \( u = \frac{1}{2}\left( {g + {g}^{ * }}\right) \) et \( v = \frac{i}{2}\left( {{g}^{ * } - g}\right) \) ). Quitte à multiplier \( x \) par \( \lambda \in \mathbb{C},\left| \lambda \right| = 1 \) , on peut supposer \( v\left( x\right) \cdot y \in i\mathbb{R} \) . Par ailleurs \( g\left( x\right) \cdot x = 1 = u\left( x\right) \cdot x - {iv}\left( x\right) \cdot x \) donc \( v\left( x\right) \cdot x = 0 \) (ceci car \( u \) et \( v \) étant autoadjoints, \( u\left( x\right) \cdot x \) et \( v\left( x\right) \cdot x \) sont des nombres réels). On a de même \( v\left( y\right) \cdot y = 0 \) .

> Let us therefore show \( \left\lbrack {0,1}\right\rbrack \subset H\left( g\right) \) . We know that \( g\left( x\right) \cdot x = 1 \) and \( g\left( y\right) \cdot y = 0 \) . Let us write \( g = u + {iv} \) with \( u \) and \( v \) self-adjoint (it suffices to take \( u = \frac{1}{2}\left( {g + {g}^{ * }}\right) \) and \( v = \frac{i}{2}\left( {{g}^{ * } - g}\right) \) ). By multiplying \( x \) by \( \lambda \in \mathbb{C},\left| \lambda \right| = 1 \) if necessary, we can assume \( v\left( x\right) \cdot y \in i\mathbb{R} \) . Furthermore \( g\left( x\right) \cdot x = 1 = u\left( x\right) \cdot x - {iv}\left( x\right) \cdot x \) so \( v\left( x\right) \cdot x = 0 \) (this is because \( u \) and \( v \) being self-adjoint, \( u\left( x\right) \cdot x \) and \( v\left( x\right) \cdot x \) are real numbers). We have similarly \( v\left( y\right) \cdot y = 0 \) .

Ceci étant, on pose \( h\left( t\right) = {tx} + \left( {1 - t}\right) y \) pour \( t \in \left\lbrack {0,1}\right\rbrack \) . Comme \( \xi = f\left( x\right) \cdot x \neq f\left( y\right) \cdot y = \eta \) , les vecteurs \( x \) et \( y \) forment une famille libre. Ceci prouve que \( h\left( t\right) \neq 0 \) pour tout \( t \in \left\lbrack {0,1}\right\rbrack \) et

> Given this, we set \( h\left( t\right) = {tx} + \left( {1 - t}\right) y \) for \( t \in \left\lbrack {0,1}\right\rbrack \) . Since \( \xi = f\left( x\right) \cdot x \neq f\left( y\right) \cdot y = \eta \) , the vectors \( x \) and \( y \) form a linearly independent family. This proves that \( h\left( t\right) \neq 0 \) for all \( t \in \left\lbrack {0,1}\right\rbrack \) and

\[
v\left\lbrack  {h\left( t\right) }\right\rbrack   \cdot  h\left( t\right)  = {t}^{2}v\left( x\right)  \cdot  x + t\left( {1 - t}\right) \left\lbrack  {v\left( x\right)  \cdot  y + \overline{v\left( x\right)  \cdot  y}}\right\rbrack   + {\left( 1 - t\right) }^{2}v\left( y\right)  \cdot  y = 0
\]

(car \( v\left( x\right) \cdot y \in i\mathbb{R} \) ). La fonction

> (because \( v\left( x\right) \cdot y \in i\mathbb{R} \) ). The function

\[
\psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{C}\;t \mapsto  \frac{g\left\lbrack  {h\left( t\right) }\right\rbrack   \cdot  h\left( t\right) }{\parallel h\left( t\right) {\parallel }^{2}}
\]

prend donc ses valeurs dans \( \mathbb{R} \) . De plus \( \psi \) est continue, \( \psi \left( 0\right) = 0 \) et \( \psi \left( 1\right) = 1 \) donc d’après le théorème des valeurs intermédiaires, \( \left\lbrack {0,1}\right\rbrack \subset \psi \left( \left\lbrack {0,1}\right\rbrack \right) \subset H\left( g\right) \) , d’où le résultat.

> therefore takes its values in \( \mathbb{R} \) . Furthermore, \( \psi \) is continuous, \( \psi \left( 0\right) = 0 \) and \( \psi \left( 1\right) = 1 \) , so according to the intermediate value theorem, \( \left\lbrack {0,1}\right\rbrack \subset \psi \left( \left\lbrack {0,1}\right\rbrack \right) \subset H\left( g\right) \) , hence the result.

b) Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base orthonormale de vecteurs propres de \( f \) , associés aux valeurs propres \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) de \( f \) . Pour tout \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \in E \) tel que \( \parallel x\parallel = 1 \) , on a

> b) Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be an orthonormal basis of eigenvectors of \( f \) , associated with the eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) of \( f \) . For any \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \in E \) such that \( \parallel x\parallel = 1 \) , we have

\[
f\left( x\right)  \cdot  x = f\left( {\mathop{\sum }\limits_{i}{x}_{i}{e}_{i}}\right)  \cdot  \mathop{\sum }\limits_{i}{x}_{i}{e}_{i} = \mathop{\sum }\limits_{i}{\left| {x}_{i}\right| }^{2}\overline{{\lambda }_{i}}.
\]

Comme \( \mathop{\sum }\limits_{i}{\left| {x}_{i}\right| }^{2} = 1 \) , on en conclue que \( H\left( f\right) \) est l’enveloppe convexe des \( \overline{{\lambda }_{i}} \) . Dans le plan complexe, on peut aussi voir \( H\left( f\right) \) comme l’intérieur du polygone convexe dont les sommets sont les \( \overline{{\lambda }_{i}} \) .

> Since \( \mathop{\sum }\limits_{i}{\left| {x}_{i}\right| }^{2} = 1 \) , we conclude that \( H\left( f\right) \) is the convex hull of the \( \overline{{\lambda }_{i}} \) . In the complex plane, one can also view \( H\left( f\right) \) as the interior of the convex polygon whose vertices are the \( \overline{{\lambda }_{i}} \) .

2 / On procède par récurrence sur \( n = \dim E \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) .

> 2 / We proceed by induction on \( n = \dim E \) . For \( n = 1 \) , it is obvious. Assume the result is true at rank \( n - 1 \) and show it at rank \( n \) .

Montrons déjà que \( 0 \in H\left( f\right) \) . Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base orthonormée et \( A \) la matrice de \( f \) dans cette base. Les termes de la diagonale principale \( {a}_{i, i} \) de \( A \) vérifient la relation \( \overline{{a}_{i, i}} = f\left( {e}_{i}\right) \cdot {e}_{i} \) , ce qui prouve que \( \overline{{a}_{i, i}} \in H\left( f\right) \) et \( H\left( f\right) \) étant convexe,

> Let us first show that \( 0 \in H\left( f\right) \) . Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be an orthonormal basis and \( A \) the matrix of \( f \) in this basis. The terms of the main diagonal \( {a}_{i, i} \) of \( A \) satisfy the relation \( \overline{{a}_{i, i}} = f\left( {e}_{i}\right) \cdot {e}_{i} \) , which proves that \( \overline{{a}_{i, i}} \in H\left( f\right) \) and \( H\left( f\right) \) being convex,

\[
\frac{1}{n}\mathop{\sum }\limits_{i}\overline{{a}_{i, i}} = \frac{1}{n}\overline{\operatorname{tr}f} = 0 \in  H\left( f\right) .
\]

Il existe donc un vecteur normé \( {f}_{1} \) tel que \( f\left( {f}_{1}\right) \cdot {f}_{1} = 0 \) . Notons \( F \) l’hyperplan \( {\left\{ {f}_{1}\right\} }^{ \bot } \) et \( g = {p}_{F} \circ {f}_{\mid F} \) , où \( {p}_{F} \) désigne la projection orthogonale sur \( F \) , de sorte que dans toute base \( {B}^{\prime } \) d \( F \)

> There therefore exists a normalized vector \( {f}_{1} \) such that \( f\left( {f}_{1}\right) \cdot {f}_{1} = 0 \) . Let \( F \) denote the hyperplane \( {\left\{ {f}_{1}\right\} }^{ \bot } \) and \( g = {p}_{F} \circ {f}_{\mid F} \) , where \( {p}_{F} \) denotes the orthogonal projection onto \( F \) , such that in any basis \( {B}^{\prime } \) of \( F \)

\[
{\left\lbrack  f\right\rbrack  }_{\left( {f}_{1},{B}^{\prime }\right) } = \left( \begin{matrix} 0 \times  \cdots  \times  \\   \times  \\  \vdots \\   \times   \end{matrix}\right) .
\]

On a donc tr \( g = 0 \) , donc d’après l’hypothèse de récurrence, il existe une base \( {B}^{\prime } \) orthonormale de \( F \) dans laquelle la matrice de \( g \) n’ait que des zéros sur la diagonale principale. Ainsi, la base \( B = \left( {{f}_{1},{B}^{\prime }}\right) \) est une base orthonormale de \( E\left( {\operatorname{car}{f}_{1} \in {F}^{ \bot }}\right) \) et

> We therefore have tr \( g = 0 \) , so according to the induction hypothesis, there exists an orthonormal basis \( {B}^{\prime } \) of \( F \) in which the matrix of \( g \) has only zeros on the main diagonal. Thus, the basis \( B = \left( {{f}_{1},{B}^{\prime }}\right) \) is an orthonormal basis of \( E\left( {\operatorname{car}{f}_{1} \in {F}^{ \bot }}\right) \) and

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} 0 &  \times  & \cdots &  \times  \\   \times  & & & \\  \vdots & & {\left\lbrack  g\right\rbrack  }_{{B}^{\prime }} & \\   \times  & & &  \end{matrix}\right)  = \left( \begin{matrix} 0 &  \times  & \cdots &  \times  \\   \times  & 0 &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\   \times  & \cdots &  \times  & 0 \end{matrix}\right) .
\]

Remarque. On peut répondre à la partie 2/ sans utiliser la partie 1/ si on suppose \( f \) autoadjoint.

> Remark. One can answer part 2/ without using part 1/ if one assumes \( f \) is self-adjoint.

Chapitre 6

> Chapter 6
