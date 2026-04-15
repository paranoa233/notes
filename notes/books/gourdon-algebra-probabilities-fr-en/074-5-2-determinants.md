#### 5.2. Determinants

Dorénavant, \( E \) est de dimension finie \( n \in {\mathbb{N}}^{ * } \) .

> From now on, \( E \) is of finite dimension \( n \in {\mathbb{N}}^{ * } \).

THÉORÉME 2. L'ensemble des formes n-linéaires alternées sur un \( \mathbb{K} \) -e.v \( E \) de dimension n est un \( \mathbb{K} \) -e.v de dimension 1. De plus, il existe une et une seule forme n-linéaire alternée prenant la valeur 1 sur une base donnée de \( E \) .

> THEOREM 2. The set of alternating n-linear forms on a \( \mathbb{K} \)-v.s. \( E \) of dimension n is a \( \mathbb{K} \)-v.s. of dimension 1. Furthermore, there exists one and only one alternating n-linear form taking the value 1 on a given basis of \( E \).

Démonstration. Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . On définit \( d \in {\mathcal{L}}_{n}\left( {E,\mathbb{K}}\right) \) par \( d\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \; {e}_{1}^{ * }\left( {x}_{1}\right) \cdots {e}_{n}^{ * }\left( {x}_{n}\right) \) , de sorte que si pour tout \( i,{x}_{i} = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{i, j}{e}_{j}, d\left( {{x}_{1},\ldots ,{x}_{n}}\right) = {x}_{1,1}\cdots {x}_{n, n} \) , et \( {d}^{\natural }\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \mathop{\sum }\limits_{{\sigma \in {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {x}_{\sigma \left( 1\right) ,1}\cdots {x}_{\sigma \left( n\right) , n} \) . On a en particulier \( {d}^{\natural }\left( {{e}_{1},\ldots ,{e}_{n}}\right) = 1 \) , donc \( {d}^{\natural } \neq 0 \) .

> Proof. Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \). We define \( d \in {\mathcal{L}}_{n}\left( {E,\mathbb{K}}\right) \) by \( d\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \; {e}_{1}^{ * }\left( {x}_{1}\right) \cdots {e}_{n}^{ * }\left( {x}_{n}\right) \), so that if for all \( i,{x}_{i} = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{i, j}{e}_{j}, d\left( {{x}_{1},\ldots ,{x}_{n}}\right) = {x}_{1,1}\cdots {x}_{n, n} \), and \( {d}^{\natural }\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \mathop{\sum }\limits_{{\sigma \in {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {x}_{\sigma \left( 1\right) ,1}\cdots {x}_{\sigma \left( n\right) , n} \). We have in particular \( {d}^{\natural }\left( {{e}_{1},\ldots ,{e}_{n}}\right) = 1 \), thus \( {d}^{\natural } \neq 0 \).

Soit \( f \in {\mathcal{L}}_{n}\left( {E,\mathbb{K}}\right) \) une forme \( n \) -linéaire alternée. La \( n \) -linéarité de \( f \) entraîne que

> Let \( f \in {\mathcal{L}}_{n}\left( {E,\mathbb{K}}\right) \) be an \( n \)-linear alternating form. The \( n \)-linearity of \( f \) implies that

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{{i}_{1},\ldots ,{i}_{n}}}{x}_{1,{i}_{1}}\cdots {x}_{n,{i}_{n}}f\left( {{e}_{{i}_{1}},\ldots ,{e}_{{i}_{n}}}\right) .
\]

Or si \( {i}_{k} = {i}_{l} \) pour \( k \neq l, f\left( {{e}_{{i}_{1}},\ldots ,{e}_{{i}_{n}}}\right) = 0 \) , et on a donc

> However, if \( {i}_{k} = {i}_{l} \) for \( k \neq l, f\left( {{e}_{{i}_{1}},\ldots ,{e}_{{i}_{n}}}\right) = 0 \), and we therefore have

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}{x}_{1,\sigma \left( 1\right) }\cdots {x}_{n,\sigma \left( n\right) }f\left( {{e}_{\sigma \left( 1\right) },\ldots ,{e}_{\sigma \left( n\right) }}\right)  = f\left( {{e}_{1},\ldots ,{e}_{n}}\right) {d}^{\mathfrak{d}}\left( {{x}_{1},\ldots ,{x}_{n}}\right) .
\]

(*)

> Donc \( f \in \operatorname{Vect}\left( {d}^{\natural }\right) \) , et comme \( {d}^{\natural } \neq 0 \) , ceci prouve que l’ensemble des formes \( n \) -linéaires alternées sur \( E \) est de dimension 1 .

Thus \( f \in \operatorname{Vect}\left( {d}^{\natural }\right) \), and since \( {d}^{\natural } \neq 0 \), this proves that the set of \( n \)-linear alternating forms on \( E \) is of dimension 1.

> Si \( f\left( {{e}_{1},\ldots ,{e}_{n}}\right) = 1 \) ,(*) prouve que \( f = {d}^{\natural } \) , d’où l’existence et l’unicité de la forme \( n \) -linéaire alternée valant 1 sur la base \( B \) .

If \( f\left( {{e}_{1},\ldots ,{e}_{n}}\right) = 1 \), (*) proves that \( f = {d}^{\natural } \), hence the existence and uniqueness of the \( n \)-linear alternating form equal to 1 on the basis \( B \).

> DéFINITION 4. Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . Le théorème précédent affirme qu’il existe une et une seule forme \( n \) -linéaire alternée sur \( E \) prenant la valeur 1 sur la base \( B \) . On l’appelle déterminant dans la base \( B \) et on la note \( \mathop{\det }\limits_{B} \) . Si \( {x}_{1},\ldots ,{x}_{n} \in E \; \left( {{x}_{i} = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{i, j}{e}_{j}}\right) \) , le déterminant de \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) dans la base \( B \) est

DEFINITION 4. Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \). The previous theorem states that there exists one and only one \( n \)-linear alternating form on \( E \) taking the value 1 on the basis \( B \). It is called the determinant in the basis \( B \) and is denoted by \( \mathop{\det }\limits_{B} \). If \( {x}_{1},\ldots ,{x}_{n} \in E \; \left( {{x}_{i} = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{i, j}{e}_{j}}\right) \), the determinant of \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) in the basis \( B \) is

\[
\mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {x}_{1,\sigma \left( 1\right) }\cdots {x}_{n,\sigma \left( n\right) }.
\]

Remarque 2. - En utilisant le théorème 2, on montre facilement que pour toute forme \( n \) -linéaire alternée \( f \) , on a \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = f\left( {{e}_{1},\ldots ,{e}_{n}}\right) {\det }_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) .

> Remark 2. - Using theorem 2, it is easily shown that for any \( n \)-linear alternating form \( f \), we have \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = f\left( {{e}_{1},\ldots ,{e}_{n}}\right) {\det }_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \).

- (Changement de base). En particulier, si \( B \) et \( {B}^{\prime } \) sont deux bases de \( E \) , alors \( \mathop{\det }\limits_{{B}^{\prime }}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\det }\limits_{{B}^{\prime }}B \cdot  \mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) . On en déduit \( \mathop{\det }\limits_{{B}^{\prime }}B \cdot  \mathop{\det }\limits_{B}{B}^{\prime } = 1 \) .

> - (Change of basis). In particular, if \( B \) and \( {B}^{\prime } \) are two bases of \( E \) , then \( \mathop{\det }\limits_{{B}^{\prime }}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\det }\limits_{{B}^{\prime }}B \cdot  \mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) . We deduce \( \mathop{\det }\limits_{{B}^{\prime }}B \cdot  \mathop{\det }\limits_{B}{B}^{\prime } = 1 \) .

THÉORÉME 3. Soient \( {x}_{1},\ldots ,{x}_{n} \in E \) . Les propositions suivantes sont équivalentes.

> THEOREM 3. Let \( {x}_{1},\ldots ,{x}_{n} \in E \) . The following statements are equivalent.

(i) Les vecteurs \( {x}_{1},\ldots ,{x}_{n} \) forment une famille liée.

> (i) The vectors \( {x}_{1},\ldots ,{x}_{n} \) form a linearly dependent family.

(ii) Pour toute base \( B \) de \( E,\mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) .

> (ii) For any base \( B \) of \( E,\mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) .

(iii) Il existe une base \( B \) de \( E \) telle que \( \mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) .

> (iii) There exists a base \( B \) of \( E \) such that \( \mathop{\det }\limits_{B}\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) .

##### Determinant of an endomorphism.

*Français : Déterminant d'un endomorphisme.*

DÉFINITION 5. Soit un endomorphisme \( f \in \mathcal{L}\left( E\right) \) et \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . Le scalaire \( \mathop{\det }\limits_{B}\left( {f\left( {e}_{1}\right) ,\ldots , f\left( {e}_{n}\right) }\right) \) ne dépend pas de la base \( B \) choisie. On l’appelle déterminant de \( f \) et on le note det \( f \) .

> DEFINITION 5. Let \( f \in \mathcal{L}\left( E\right) \) be an endomorphism and \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) a base of \( E \) . The scalar \( \mathop{\det }\limits_{B}\left( {f\left( {e}_{1}\right) ,\ldots , f\left( {e}_{n}\right) }\right) \) does not depend on the chosen base \( B \) . It is called the determinant of \( f \) and is denoted by det \( f \) .

Proposition 3. \( \;\left( i\right) \) Si \( f, g \in \mathcal{L}\left( E\right) ,\det \left( {f \circ g}\right) = \det f \times \det g \) .

> Proposition 3. \( \;\left( i\right) \) If \( f, g \in \mathcal{L}\left( E\right) ,\det \left( {f \circ g}\right) = \det f \times \det g \) .

(ii) \( \det {\mathrm{{Id}}}_{E} = 1 \) .

> (ii) \( \det {\mathrm{{Id}}}_{E} = 1 \) .

(iii) Soit \( f \in \mathcal{L}\left( E\right) \) . Alors \( \left( {f \in \mathcal{G}\ell \left( E\right) \Leftrightarrow \det f \neq 0}\right) \) et on a \( \det \left( {f}^{-1}\right) = {\left( \det f\right) }^{-1} \) .

> (iii) Let \( f \in \mathcal{L}\left( E\right) \) . Then \( \left( {f \in \mathcal{G}\ell \left( E\right) \Leftrightarrow \det f \neq 0}\right) \) and we have \( \det \left( {f}^{-1}\right) = {\left( \det f\right) }^{-1} \) .

Déterminant d'une matrice carrée.

> Determinant of a square matrix.

DéFINITION 6. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On appelle déterminant de \( A \) , et on noté det \( A \) , le déterminant de ses vecteurs colonnes dans la base canonique de \( {\mathbb{K}}^{n} \) . On a

> DEFINITION 6. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . The determinant of \( A \) , denoted by det \( A \) , is the determinant of its column vectors in the canonical base of \( {\mathbb{K}}^{n} \) . We have

\[
\det A = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {a}_{\sigma \left( 1\right) ,1}\cdots {a}_{\sigma \left( n\right) , n} = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{n}}}\varepsilon \left( \sigma \right) {a}_{1,\sigma \left( 1\right) }\cdots {a}_{n,\sigma \left( n\right) }.
\]

Remarque 3. Si \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on note aussi le déterminant de \( A \) en l’écrivant sous la forme

> Remark 3. If \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , the determinant of \( A \) is also denoted by writing it in the form

\[
\left| \begin{matrix} {a}_{1,1} & \cdots & {a}_{1, n} \\  \vdots & & \vdots \\  {a}_{n,1} & \cdots & {a}_{n, n} \end{matrix}\right|
\]

Propriétés. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Alors :

> Properties. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Then:

- \( \det A = \det \left( {{}^{\mathrm{t}}A}\right) \) .

> - det \( A \) dépend linéairement des colonnes (resp. des lignes) de \( A \) .

- det \( A \) depends linearly on the columns (resp. rows) of \( A \) .

> - Pour tout \( \lambda  \in  \mathbb{K} \) , \( \det \left( {\lambda A}\right)  = {\lambda }^{n}\det A \) .

- For any \( \lambda  \in  \mathbb{K} \) , \( \det \left( {\lambda A}\right)  = {\lambda }^{n}\det A \) .

> - On a (det \( A \neq  0 \Leftrightarrow  A \in  \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) ).

- We have (det \( A \neq  0 \Leftrightarrow  A \in  \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) ).

> - Si on effectue une permutation \( \sigma  \in  {\mathcal{S}}_{n} \) sur les colonnes (ou les lignes) de \( A \) , le déterminant de \( A \) est multiplié par \( \varepsilon \left( \sigma \right) \) (signature de \( \sigma \) ).

- If a permutation \( \sigma  \in  {\mathcal{S}}_{n} \) is performed on the columns (or rows) of \( A \) , the determinant of \( A \) is multiplied by \( \varepsilon \left( \sigma \right) \) (signature of \( \sigma \) ).

> - Si \( A \) est triangulaire, det \( A \) est le produit des éléments diagonaux de \( A \) .

- If \( A \) is triangular, det \( A \) is the product of the diagonal elements of \( A \) .

> — On ne change pas la valeur d'un déterminant en ajoutant à une colonne une com-binaison linéaire des autres colonnes. Même chose sur les lignes.

— The value of a determinant remains unchanged when adding a linear combination of other columns to a column. The same applies to rows.

> - Si \( A \) est la matrice de \( f \in  \mathcal{L}\left( E\right) \) dans une base de \( E \) , alors det \( f = \det A \) .

- If \( A \) is the matrix of \( f \in  \mathcal{L}\left( E\right) \) in a basis of \( E \) , then det \( f = \det A \) .

> - Si \( A, B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\det \left( {AB}\right)  = \det A \cdot  \det B \) .

- If \( A, B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\det \left( {AB}\right)  = \det A \cdot  \det B \) .

> - Deux matrices semblables ont même déterminant.

- Two similar matrices have the same determinant.

> — (Déterminant par blocs). Si

— (Block determinant). If

\[
M = \left( \begin{matrix} A & C \\  0 & B \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right)
\]

avec \( A \in {\mathcal{M}}_{p}\left( \mathbb{K}\right) \) et \( B \in {\mathcal{M}}_{n - p}\left( \mathbb{K}\right) \) , alors det \( M = \det A \cdot \det B \) .

> with \( A \in {\mathcal{M}}_{p}\left( \mathbb{K}\right) \) and \( B \in {\mathcal{M}}_{n - p}\left( \mathbb{K}\right) \) , then det \( M = \det A \cdot \det B \) .

Mineurs et cofacteurs.

> Minors and cofactors.

DéFINITION 7. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> DEFINITION 7. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

Pour tout \( \left( {i, j}\right) \) , on appelle mineur de l’élément \( {a}_{i, j} \) le déterminant \( {\Delta }_{i, j} \) de la matrice obtenue en supprimant la \( i \) -ième ligne et la \( j \) -ième colonne de la matrice \( A \) . Le scalaire \( {A}_{i, j} = {\left( -1\right) }^{i + j}{\Delta }_{i, j} \) s’appelle le cofacteur de \( {a}_{i, j} \) .

> For any \( \left( {i, j}\right) \) , the minor of the element \( {a}_{i, j} \) is the determinant \( {\Delta }_{i, j} \) of the matrix obtained by removing the \( i \) -th row and the \( j \) -th column of matrix \( A \) . The scalar \( {A}_{i, j} = {\left( -1\right) }^{i + j}{\Delta }_{i, j} \) is called the cofactor of \( {a}_{i, j} \) .

On appelle mineurs principaux de \( A \) les déterminants \( {\Delta }_{k} = \det {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq k} \) pour \( 1 \leq k \leq n \) .

> The principal minors of \( A \) are the determinants \( {\Delta }_{k} = \det {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq k} \) for \( 1 \leq k \leq n \) .

PROPOSITION 4 (DÉVELOPPEMENT SELON UNE LIGNE OU UNE COLONNE). Soit une matrice \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,{A}_{i, j} \) les cofacteurs des éléments de A. Alors :

> PROPOSITION 4 (EXPANSION ALONG A ROW OR COLUMN). Let a matrix \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,{A}_{i, j} \) be the cofactors of the elements of A. Then:

— (Développement par rapport à la j-ième colonne) \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, j}{A}_{i, j} = \det A \) .

> — (Expansion along the j-th column) \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, j}{A}_{i, j} = \det A \) .

- (Développement par rapport à la i-ième ligne) \( \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}{A}_{i, j} = \det A \) .

> - (Expansion along the i-th row) \( \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}{A}_{i, j} = \det A \) .

DéFINITION 8. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . La matrice \( {\left( {A}_{i, j}\right) }_{1 \leq i, j \leq n} \) des cofacteurs des éléments de \( A \) , est appelée comatrice de \( A \) et on la note com \( \left( A\right) \) ou encore \( \widetilde{A} \) .

> DEFINITION 8. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . The matrix \( {\left( {A}_{i, j}\right) }_{1 \leq i, j \leq n} \) of the cofactors of the elements of \( A \) is called the comatrix of \( A \) and is denoted by com \( \left( A\right) \) or \( \widetilde{A} \) .

Proposition 5. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Alors \( {A}^{\mathrm{t}}\widetilde{A} = {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) \cdot {I}_{n} \) .

> Proposition 5. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Then \( {A}^{\mathrm{t}}\widetilde{A} = {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) \cdot {I}_{n} \) .

Exemple 2. La proposition précédente entraîne que si une matrice \( A \) est inversible, alors \( {A}^{-1} = \left( {1/\det A}\right) \cdot {}^{\mathrm{t}}\widetilde{A} \) . Ce résultat appliqué aux matrices \( 2 \times 2 \) entraîne que si \( A = \left( \begin{array}{ll} a & b \\ c & d \end{array}\right) \in \; {\mathcal{M}}_{2}\left( \mathbb{K}\right) \) est inversible, alors son inverse s’obtient par la formule \( {A}^{-1} = \frac{1}{{ad} - {bc}}\left( \begin{matrix} d & - b \\ - c & a \end{matrix}\right) \) .

> Example 2. The previous proposition implies that if a matrix \( A \) is invertible, then \( {A}^{-1} = \left( {1/\det A}\right) \cdot {}^{\mathrm{t}}\widetilde{A} \) . This result applied to matrices \( 2 \times 2 \) implies that if \( A = \left( \begin{array}{ll} a & b \\ c & d \end{array}\right) \in \; {\mathcal{M}}_{2}\left( \mathbb{K}\right) \) is invertible, then its inverse is obtained by the formula \( {A}^{-1} = \frac{1}{{ad} - {bc}}\left( \begin{matrix} d & - b \\ - c & a \end{matrix}\right) \) .

Déterminant de Vandermonde. Beaucoup de déterminants sont classiques (voir les exercices). Nous allons étudier ici l'un des plus classiques appelé déterminant de Vander-monde. Pour \( n \geq 2 \) et pour tous \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) , on note

> Vandermonde determinant. Many determinants are classic (see the exercises). We will study here one of the most classic ones, called the Vandermonde determinant. For \( n \geq 2 \) and for all \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) , we denote

\[
V\left( {{a}_{1},\ldots ,{a}_{n}}\right)  = \left| \begin{matrix} 1 & {a}_{1} & {a}_{1}^{2} & \cdots & {a}_{1}^{n - 1} \\  1 & {a}_{2} & {a}_{2}^{2} & \cdots & {a}_{2}^{n - 1} \\  \vdots & & & & \vdots \\  1 & {a}_{n} & {a}_{n}^{2} & \cdots & {a}_{n}^{n - 1} \end{matrix}\right|
\]

(déterminant de Vandermonde de \( {a}_{1},\ldots ,{a}_{n} \) ). Nous allons montrer que

> (Vandermonde determinant of \( {a}_{1},\ldots ,{a}_{n} \) ). We will show that

\[
V\left( {{a}_{1},\ldots ,{a}_{n}}\right)  = \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{a}_{j} - {a}_{i}}\right) .
\]

Démonstration. On procède par récurrence sur \( n \) . Pour \( n = 2 \) , c’est évident. Supposons le résultat vrai pour \( n - 1 \) et montrons le pour \( n \) . Dans \( V\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , on retranche à chaque colonne \( {a}_{1} \) fois la précédente (en commençant par la dernière colonne). On obtient

> Proof. We proceed by induction on \( n \) . For \( n = 2 \) , it is obvious. Assume the result is true for \( n - 1 \) and show it for \( n \) . In \( V\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , we subtract \( {a}_{1} \) times the previous column from each column (starting from the last column). We obtain

\[
\left| \begin{matrix} 1 & 0 & 0 & \cdots & 0 \\  1 & {a}_{2} - {a}_{1} & {a}_{2}^{2} - {a}_{1}{a}_{2} & \cdots & {a}_{2}^{n - 1} - {a}_{1}{a}_{2}^{n - 2} \\  \vdots & \vdots & \vdots & & \vdots \\  1 & {a}_{n} - {a}_{1} & {a}_{n}^{2} - {a}_{1}{a}_{n} & \cdots & {a}_{n}^{n - 1} - {a}_{1}{a}_{n}^{n - 2} \end{matrix}\right|  = \left| \begin{matrix} {a}_{2} - {a}_{1} & {a}_{2}^{2} - {a}_{1}{a}_{2} & \cdots & {a}_{2}^{n - 1} - {a}_{1}{a}_{2}^{n - 2} \\  \vdots & \vdots & & \vdots \\  {a}_{n} - {a}_{1} & {a}_{n}^{2} - {a}_{1}{a}_{n} & \cdots & {a}_{n}^{n - 1} - {a}_{1}{a}_{n}^{n - 2} \end{matrix}\right|
\]

(après développement par rapport à la première ligne). On factorise ensuite chaque ligne par \( \left( {{a}_{i} - {a}_{1}}\right) \) , ce qui donne

> (after expansion along the first row). We then factor out \( \left( {{a}_{i} - {a}_{1}}\right) \) from each row, which gives

\[
V\left( {{a}_{1},\ldots ,{a}_{n}}\right)  = \left( {{a}_{2} - {a}_{1}}\right) \cdots \left( {{a}_{n} - {a}_{1}}\right)  \cdot  \left| \begin{matrix} 1 & {a}_{2} & \cdots & {a}_{2}^{n - 2} \\  \vdots & \vdots & & \vdots \\  1 & {a}_{n} & \cdots & {a}_{n}^{n - 2} \end{matrix}\right|  = \left\lbrack  {\mathop{\prod }\limits_{{i = 2}}^{n}\left( {{a}_{i} - {a}_{1}}\right) }\right\rbrack  V\left( {{a}_{2},\ldots ,{a}_{n}}\right)
\]

d’où le résultat car d’après l’hypothèse de récurrence, \( V\left( {{a}_{2},\ldots ,{a}_{n}}\right) = \mathop{\prod }\limits_{{2 \leq i < j \leq n}}\left( {{a}_{j} - {a}_{i}}\right) \) .

> whence the result, because according to the induction hypothesis, \( V\left( {{a}_{2},\ldots ,{a}_{n}}\right) = \mathop{\prod }\limits_{{2 \leq i < j \leq n}}\left( {{a}_{j} - {a}_{i}}\right) \) .
