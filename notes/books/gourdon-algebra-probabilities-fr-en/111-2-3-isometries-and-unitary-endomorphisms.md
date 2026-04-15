#### 2.3. Isometries and unitary endomorphisms

*Français : 2.3. Isométries et endomorphismes unitaires*

DéFINITION 2. Soit \( E \) un espace préhilbertien et \( f \in \mathcal{L}\left( E\right) \) telle que pour tout \( x \in E \) , \( \parallel f\left( x\right) \parallel = \parallel x\parallel . \)

> DEFINITION 2. Let \( E \) be a pre-Hilbert space and \( f \in \mathcal{L}\left( E\right) \) such that for all \( x \in E \), \( \parallel f\left( x\right) \parallel = \parallel x\parallel . \)

- Si \( E \) est préhilbertien réel, \( f \) est appelé isométrie (on dit aussi endomorphisme orthogonal).

> - If \( E \) is a real pre-Hilbert space, \( f \) is called an isometry (also called an orthogonal endomorphism).

- Si \( E \) est préhilbertien complexe, \( f \) est appelé endomorphisme unitaire.

> - If \( E \) is a complex pre-Hilbert space, \( f \) is called a unitary endomorphism.

Proposition 3. Soit E un espace préhilbertien et f une application de E dans E. Alors f est une isométrie (resp. un endomorphisme unitaire) si et seulement si

> Proposition 3. Let E be a pre-Hilbert space and f a mapping from E to E. Then f is an isometry (resp. a unitary endomorphism) if and only if

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;f\left( x\right)  \cdot  f\left( y\right)  = x \cdot  y.
\]

(*)

> Remarque 8. Noter que la propriété (*) implique la linéarité de \( f \) .

Remark 8. Note that property (*) implies the linearity of \( f \).

> Proposition 4. Si \( f \in \mathcal{L}\left( E\right) \) est une isométrie (resp. un endomorphisme unitaire) alors f est injective. Si de plus E est de dimension finie alors f est bijective.

Proposition 4. If \( f \in \mathcal{L}\left( E\right) \) is an isometry (resp. a unitary endomorphism) then f is injective. If, in addition, E is finite-dimensional, then f is bijective.

> Proposition 5. - L'ensemble des isométries d'un espace euclidien E est un groupe (muni de la loi o de composition), appelé groupe orthogonal de \( E \) et noté \( \mathcal{O}\left( E\right) \) .

Proposition 5. - The set of isometries of a Euclidean space E is a group (equipped with the composition law o), called the orthogonal group of \( E \) and denoted by \( \mathcal{O}\left( E\right) \).

> - L'ensemble des endomorphismes unitaires d'un espace hermitien E est un groupe appelé groupe unitaire de \( E \) et noté \( \mathcal{U}\left( E\right) \) .

- The set of unitary endomorphisms of a Hermitian space E is a group called the unitary group of \( E \) and denoted by \( \mathcal{U}\left( E\right) \).

##### Matrix properties of isometries and unitary endomorphisms.

*Français : Propriétés matricielles des isométries et des endomorphismes unitaires.*

Proposition 6. Soit \( E \) un espace euclidien (resp. hermitien) et \( f \in \mathcal{L}\left( E\right) \) . Alors \( f \) est une isométrie (ou un endomorphisme unitaire) si et seulement si l'image d'une base orthonormale de \( E \) par \( f \) est une base orthonormale de \( E \) .

> Proposition 6. Let \( E \) be a Euclidean (resp. Hermitian) space and \( f \in \mathcal{L}\left( E\right) \). Then \( f \) is an isometry (or a unitary endomorphism) if and only if the image of an orthonormal basis of \( E \) under \( f \) is an orthonormal basis of \( E \).

Conséquence. Soit \( B \) une base orthonormale de \( E \) et \( f \in \mathcal{L}\left( E\right) \) . Soit \( A \) la matrice de \( f \) dans \( B \) . Alors \( f \) une isométrie (resp. un endomorphisme unitaire) si et seulement si

> Consequence. Let \( B \) be an orthonormal basis of \( E \) and \( f \in \mathcal{L}\left( E\right) \). Let \( A \) be the matrix of \( f \) in \( B \). Then \( f \) is an isometry (resp. a unitary endomorphism) if and only if

\[
{}^{\mathrm{t}}{AA} = {A}^{\mathrm{t}}A = {I}_{n}\text{ (resp. }{}^{\mathrm{t}}\bar{A}A = {A}^{\mathrm{t}}\bar{A} = {I}_{n}\text{ ). }
\]

On en déduit que det \( {}^{\mathrm{t}}A \cdot \det A = 1 = {\left( \det A\right) }^{2} \) (resp. det \( {}^{\mathrm{t}}\bar{A} \cdot \det \left( A\right) = 1 = {\left| \det A\right| }^{2} \) ).

> We deduce that det \( {}^{\mathrm{t}}A \cdot \det A = 1 = {\left( \det A\right) }^{2} \) (resp. det \( {}^{\mathrm{t}}\bar{A} \cdot \det \left( A\right) = 1 = {\left| \det A\right| }^{2} \)).

- Si \( f \) est une isométrie, on a donc \( {\left( \det f\right) }^{2} = 1 \) , ou encore det \( f \in  \{  - 1,1\} \) .

> - If \( f \) is an isometry, then we have \( {\left( \det f\right) }^{2} = 1 \) , or equivalently det \( f \in  \{  - 1,1\} \) .

- Si \( f \) est un endomorphisme unitaire, on a det \( f{ \mid  }^{2} = 1 \) , donc det \( f \mid   = 1 \) .

> - If \( f \) is a unitary endomorphism, we have det \( f{ \mid  }^{2} = 1 \) , so det \( f \mid   = 1 \) .

DéFINITION 3. - Si \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) vérifie \( {}^{\mathrm{t}}{AA} = {I}_{n}, A \) s’appelle une matrice orthogo-nale.

> DEFINITION 3. - If \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) satisfies \( {}^{\mathrm{t}}{AA} = {I}_{n}, A \) it is called an orthogonal matrix.

- Si \( A \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) vérifie \( {}^{\mathrm{t}}\bar{A}A = {I}_{n}, A \) s’appelle une matrice unitaire.

> - If \( A \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) satisfies \( {}^{\mathrm{t}}\bar{A}A = {I}_{n}, A \) it is called a unitary matrix.

- L’ensemble des matrices orthogonales de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) constitue un groupe noté \( {\mathcal{O}}_{n} \) , celui des matrices unitaires de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est un groupe noté \( {\mathcal{U}}_{n} \) .

> - The set of orthogonal matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) forms a group denoted \( {\mathcal{O}}_{n} \) , that of unitary matrices of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is a group denoted \( {\mathcal{U}}_{n} \) .

DéFINITION 4. - Soit \( f \) une isométrie d’un espace euclidien \( E \) . On dit que \( f \) est une isométrie directe si det \( f = 1 \) , une isométrie indirecte si det \( f = - 1 \) .

> DEFINITION 4. - Let \( f \) be an isometry of a Euclidean space \( E \) . We say that \( f \) is a direct isometry if det \( f = 1 \) , an indirect isometry if det \( f = - 1 \) .

- L’ensemble \( \{ f \in  \mathcal{O}\left( E\right)  \mid  \det f = 1\} \) est un sous-groupe distingué de \( \mathcal{O}\left( E\right) \) appelé groupe spécial orthogonal de \( E \) et noté \( {\mathcal{O}}^{ + }\left( E\right) \) (on le note encore \( \mathcal{{SO}}\left( E\right) \) ).

> - The set \( \{ f \in  \mathcal{O}\left( E\right)  \mid  \det f = 1\} \) is a normal subgroup of \( \mathcal{O}\left( E\right) \) called the special orthogonal group of \( E \) and denoted \( {\mathcal{O}}^{ + }\left( E\right) \) (also denoted \( \mathcal{{SO}}\left( E\right) \) ).

- Si \( E \) est hermitien, l’ensemble \( \{ f \in  \mathcal{U}\left( E\right)  \mid  \det f = 1\} \) est un sous-groupe distingué de \( \mathcal{U}\left( E\right) \) noté \( \mathcal{{SU}}\left( E\right) \) .

> - If \( E \) is Hermitian, the set \( \{ f \in  \mathcal{U}\left( E\right)  \mid  \det f = 1\} \) is a normal subgroup of \( \mathcal{U}\left( E\right) \) denoted \( \mathcal{{SU}}\left( E\right) \) .

- Pour les matrices, on note également

> - For matrices, we also denote

\[
{\mathcal{{SO}}}_{n} = {\mathcal{O}}_{n}^{ + } = \left\{  {A \in  {\mathcal{O}}_{n} \mid  \det A = 1}\right\}  \text{ et }{\mathcal{{SU}}}_{n} = \left\{  {A \in  {\mathcal{U}}_{n} \mid  \det A = 1}\right\}  .
\]

L’ensemble \( {\mathcal{{SO}}}_{n} \) est un sous-groupe distingué de \( {\mathcal{O}}_{n},{\mathcal{{SU}}}_{n} \) un sous-groupe distingué de \( {\mathcal{U}}_{n} \) .

> The set \( {\mathcal{{SO}}}_{n} \) is a normal subgroup of \( {\mathcal{O}}_{n},{\mathcal{{SU}}}_{n} \) a normal subgroup of \( {\mathcal{U}}_{n} \) .

Remarque 9. La réduction des endomorphismes orthogonaux ou unitaires fait l'objet de la partie 3.1. Dans le cas particulier du plan ou de l'espace, on trouve les résultats classiques suivant :

> Remark 9. The reduction of orthogonal or unitary endomorphisms is the subject of section 3.1. In the specific case of the plane or space, we find the following classical results:

- La matrice d'une isométrie directe du plan s'écrit dans toute base orthonormale \( B \) sous la forme \( R\left( \theta \right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) \) avec \( \theta  \in  \mathbb{R} \) (rotation d’angle \( \theta \) ).

> - The matrix of a direct isometry of the plane is written in any orthonormal basis \( B \) in the form \( R\left( \theta \right)  = \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right) \) with \( \theta  \in  \mathbb{R} \) (rotation by angle \( \theta \) ).

- La matrice d’une isométrie directe de l’espace s’écrit sous la forme \( \left( \begin{matrix} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{matrix}\right) \) dans une base orthonormale \( B \) bien choisie (rotation d’angle \( \theta \) autour du dernier vecteur de la base \( B \) ).

> - The matrix of a direct isometry of space is written in the form \( \left( \begin{matrix} \cos \theta &  - \sin \theta & 0 \\  \sin \theta & \cos \theta & 0 \\  0 & 0 & 1 \end{matrix}\right) \) in a well-chosen orthonormal basis \( B \) (rotation by angle \( \theta \) around the last vector of the basis \( B \) ).
