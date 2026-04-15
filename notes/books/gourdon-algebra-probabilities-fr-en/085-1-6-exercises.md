#### 1.6. Exercises

*Français : 1.6. Exercices*

EXERCICE 1. Diagonaliser ou trigonaliser dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , en donnant la matrice de passage, les matrices suivantes.

> EXERCISE 1. Diagonalize or trigonalize in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , providing the transition matrix, for the following matrices.

\[
\text{ a) }M = \left( \begin{array}{rrr} 0 & 2 &  - 1 \\  3 &  - 2 & 0 \\   - 2 & 2 & 1 \end{array}\right) \text{ . }
\]

b) \( M = \left( \begin{array}{rrrr} 0 & 0 & 0 & 1 \\ 0 & 0 & - 1 & 0 \\ 0 & 1 & 0 & 0 \\ - 1 & 0 & 0 & 0 \end{array}\right) \) .

\[
\text{ c) }M = \left( \begin{array}{rrr} 1 & 4 &  - 2 \\  0 & 6 &  - 3 \\   - 1 & 4 & 0 \end{array}\right) \text{ . }
\]

d) \( M = \left( \begin{array}{rrr} 2 & 2 & - 3 \\ 5 & 1 & - 5 \\ - 3 & 4 & 0 \end{array}\right) \) .

> Solution. a) On calcule le polynôme caractéristique de \( M \) :

Solution. a) We calculate the characteristic polynomial of \( M \) :

\[
{P}_{M} = \left| \begin{matrix}  - X & 2 &  - 1 \\  3 &  - 2 - X & 0 \\   - 2 & 2 & 1 - X \end{matrix}\right|  = \left| \begin{matrix} 1 - X & 2 &  - 1 \\  1 - X &  - 2 - X & 0 \\  1 - X & 2 & 1 - X \end{matrix}\right|  = \left( {1 - X}\right) \left| \begin{matrix} 1 & 2 &  - 1 \\  1 &  - 2 - X & 0 \\  1 & 2 & 1 - X \end{matrix}\right|
\]

\[
= \left( {1 - X}\right) \left| \begin{matrix} 1 & 0 & 0 \\  1 &  - 4 - X & 1 \\  1 & 0 & 2 - X \end{matrix}\right|  = \left( {1 - X}\right) \left| \begin{matrix}  - 4 - X & 1 \\  0 & 2 - X \end{matrix}\right|  =  - \left( {X - 1}\right) \left( {X - 2}\right) \left( {X + 4}\right) .
\]

D’après la proposition \( 1, M \) a donc trois valeurs propres qui sont1,2et -4 . Ces valeurs propres étant distinctes, \( M \) est donc diagonalisable d’après la proposition 4. Recherchons - Un vecteur propre \( {X}_{1} = \left( \begin{matrix} x \\ \frac{y}{z} \end{matrix}\right) \) associé à la valeur propre1:

> According to proposition \( 1, M \) , it therefore has three eigenvalues which are 1, 2, and -4. Since these eigenvalues are distinct, \( M \) is therefore diagonalizable according to proposition 4. Let us find - An eigenvector \( {X}_{1} = \left( \begin{matrix} x \\ \frac{y}{z} \end{matrix}\right) \) associated with the eigenvalue 1:

\[
M{X}_{1} = {X}_{1} \Leftrightarrow  \left\{  {\begin{matrix}  - x &  + {2y} &  - z = 0 \\  {3x} &  - {3y} &  = 0 \\   - {2x} &  + {2y} &  = 0 \end{matrix} \Leftrightarrow  \left\{  {\begin{array}{l} x = y \\  x = z \end{array}.}\right. }\right.
\]

Donc \( {X}_{1} = \left( \begin{array}{l} 1 \\ 1 \end{array}\right) \) convient. - Un vecteur propre \( {X}_{2} = \left( \begin{matrix} x \\ y \\ z \end{matrix}\right) \) associé à la valeur propre2:

> Thus \( {X}_{1} = \left( \begin{array}{l} 1 \\ 1 \end{array}\right) \) is suitable. - An eigenvector \( {X}_{2} = \left( \begin{matrix} x \\ y \\ z \end{matrix}\right) \) associated with the eigenvalue 2:

\[
M{X}_{2} = 2{X}_{2} \Leftrightarrow  \left\{  {\begin{matrix}  - {2x} + {2y} &  - z = 0 \\  {3x} - {4y} &  - {4y} = 0 \\   - {2x} + {2y} - z &  - z = 0 \end{matrix} \Leftrightarrow  \left\{  {\begin{matrix} {3x} =  - {4y} \\  z = 2\left( {y - x}\right)  \end{matrix}.}\right. }\right.
\]

Donc \( {X}_{2} = \left( \begin{matrix} 4 \\ 3 \\ - 2 \end{matrix}\right) \) convient.

> Thus \( {X}_{2} = \left( \begin{matrix} 4 \\ 3 \\ - 2 \end{matrix}\right) \) is suitable.

- Un vecteur propre \( {X}_{3} = \left( \begin{matrix} x \\  y \\  z \end{matrix}\right) \) associé à la valeur propre-4:

> - An eigenvector \( {X}_{3} = \left( \begin{matrix} x \\  y \\  z \end{matrix}\right) \) associated with the eigenvalue -4:

\[
M{X}_{3} =  - 4{X}_{3} \Leftrightarrow  \left\{  \begin{matrix} {4x} &  + {2y} &  - z = 0 \\  {3x} &  + {2y} &  = 0 \\   - {2x} &  + {2y} &  + {5z} = 0 \end{matrix}\right.  \Leftrightarrow  \left\{  \begin{matrix} {3x} + {2y} &  = 0 \\  x &  = z \end{matrix}\right.
\]

Donc \( {X}_{3} = \left( \begin{matrix} 2 \\ - 3 \end{matrix}\right) \) convient.

> Thus \( {X}_{3} = \left( \begin{matrix} 2 \\ - 3 \end{matrix}\right) \) is suitable.

- L’endomorphisme \( f \in  \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) ayant \( M \) pour matrice dans la base canonique de \( {\mathbb{C}}^{3} \) est donc diagonalisable, et \( B = \left( {{X}_{1},{X}_{2},{X}_{3}}\right) \) est une base de diagonalisation de \( f \) . On a

> - The endomorphism \( f \in  \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) having \( M \) as its matrix in the canonical basis of \( {\mathbb{C}}^{3} \) is therefore diagonalizable, and \( B = \left( {{X}_{1},{X}_{2},{X}_{3}}\right) \) is a basis of diagonalization for \( f \) . We have

\[
{\left\lbrack  f\right\rbrack  }_{B} = D = \left( \begin{array}{rrr} 1 & 0 & 0 \\  0 & 2 & 0 \\  0 & 0 &  - 4 \end{array}\right) \;\text{ donc }\;{P}^{-1}{MP} = D\;\text{ avec }\;P = \left( \begin{array}{rrr} 1 & 4 & 2 \\  1 & 3 &  - 3 \\  1 &  - 2 & 2 \end{array}\right) .
\]

( \( P \) est la matrice de passage de la base canonique de \( {\mathbb{C}}^{3} \) à la base \( B \) ).

> ( \( P \) is the transition matrix from the canonical basis of \( {\mathbb{C}}^{3} \) to the basis \( B \) ).

b) Un calcul donne \( {P}_{M} = {\left( {X}^{2} + 1\right) }^{2} = {\left( X + i\right) }^{2}{\left( X - i\right) }^{2} \) .

> b) A calculation gives \( {P}_{M} = {\left( {X}^{2} + 1\right) }^{2} = {\left( X + i\right) }^{2}{\left( X - i\right) }^{2} \) .

- On recherche \( {E}_{i} \) , le sous-espace propre associé à la valeur propre \( i \) . On a

> - We look for \( {E}_{i} \) , the eigenspace associated with the eigenvalue \( i \) . We have

\[
M - i{I}_{4} = \left( \begin{array}{rrrr}  - i & 0 & 0 & 1 \\  0 &  - i &  - 1 & 0 \\  0 & 1 &  - i & 0 \\   - 1 & 0 & 0 &  - i \end{array}\right) .
\]

On remarque que dans cette dernière matrice, la dernière colonne vaut \( i \) fois la première, c’est- à-dire qu’en sommant la première colonne à \( i \) fois la dernière, on tombe sur le vecteur nul.

> We note that in this last matrix, the last column is equal to \( i \) times the first, which means that by adding the first column to \( i \) times the last, we obtain the zero vector.

Autrement dit, \( \left( {M - i{I}_{4}}\right) \left( \begin{matrix} 1 \\ 0 \\ i \\ 0 \end{matrix}\right) = 0 \) . De même, on trouve \( \left( {M - i{I}_{4}}\right) \left( \begin{matrix} 0 \\ 1 \\ - i \\ 0 \end{matrix}\right) = 0 \) . On a donc

> In other words, \( \left( {M - i{I}_{4}}\right) \left( \begin{matrix} 1 \\ 0 \\ i \\ 0 \end{matrix}\right) = 0 \) . Similarly, we find \( \left( {M - i{I}_{4}}\right) \left( \begin{matrix} 0 \\ 1 \\ - i \\ 0 \end{matrix}\right) = 0 \) . We therefore have

\[
{E}_{i} = \operatorname{Vect}\left\{  {\left( \begin{matrix} 1 \\  0 \\  0 \\  i \end{matrix}\right) ,\left( \begin{matrix} 0 \\  1 \\   - i \\  0 \end{matrix}\right) }\right\}
\]

(ces deux vecteurs forment une famille libre de \( {E}_{i} \) , donc une base de \( {E}_{i} \) car d’après la proposition 5, on a \( \dim {E}_{i} \leq 2 \) ). On en déduit en particulier que \( \dim {E}_{i} = 2 \) .

> (these two vectors form a free family of \( {E}_{i} \) , and thus a basis of \( {E}_{i} \) because according to proposition 5, we have \( \dim {E}_{i} \leq 2 \) ). We deduce in particular that \( \dim {E}_{i} = 2 \) .

En procédant de la même manière, on trouve que dim \( {E}_{-i} = 2 \) et que

> By proceeding in the same way, we find that dim \( {E}_{-i} = 2 \) and that

\[
{E}_{-i} = \operatorname{Vect}\left\{  {\left( \begin{matrix} 1 \\  0 \\  0 \\   - i \end{matrix}\right) ,\left( \begin{matrix} 0 \\  1 \\  i \\  0 \end{matrix}\right) }\right\}  .
\]

D’après le théorème 2, \( M \) est donc diagonalisable et on a

> According to theorem 2, \( M \) is therefore diagonalizable and we have

\[
{P}^{-1}{MP} = D\text{ avec }D = \left( \begin{matrix} i & 0 & 0 & 0 \\  0 & i & 0 & 0 \\  0 & 0 &  - i & 0 \\  0 & 0 & 0 &  - i \end{matrix}\right) \;\text{ et }\;P = \left( \begin{matrix} 1 & 0 & 0 & 1 \\  0 & 1 & 1 & 0 \\  0 &  - i & i & 0 \\  i & 0 & 0 &  - i \end{matrix}\right) .
\]

c) Ici \( {P}_{M} = - \left( {X - 3}\right) {\left( X - 2\right) }^{2} \) . Comme \( {P}_{M} \) a une racine double, \( M \) n’est pas forcément diagonalisable.

> c) Here \( {P}_{M} = - \left( {X - 3}\right) {\left( X - 2\right) }^{2} \) . Since \( {P}_{M} \) has a double root, \( M \) is not necessarily diagonalizable.

- Recherchons \( {E}_{3} \) , le sous-espace propre associé à la valeur propre 3. La résolution du système \( {MX} = {3X} \) montre que \( {E}_{3} = \operatorname{Vect}\left\{  \left( \begin{matrix} 1 \\  1 \end{matrix}\right) \right\} \) . - Recherchons \( {E}_{2} \) , le sous-espace propre associé à la valeur propre 2. La résolution du système \( {MX} = {2X} \) montre que \( {E}_{2} = \operatorname{Vect}\left\{  \left( \begin{matrix} 4 \\  3 \end{matrix}\right) \right\} \) . Donc \( \dim {E}_{2} = 1 < 2 \) , et donc \( M \) n’est pas diagonali-sable.

> - Let us look for \( {E}_{3} \) , the eigenspace associated with the eigenvalue 3. Solving the system \( {MX} = {3X} \) shows that \( {E}_{3} = \operatorname{Vect}\left\{  \left( \begin{matrix} 1 \\  1 \end{matrix}\right) \right\} \) . - Let us look for \( {E}_{2} \) , the eigenspace associated with the eigenvalue 2. Solving the system \( {MX} = {2X} \) shows that \( {E}_{2} = \operatorname{Vect}\left\{  \left( \begin{matrix} 4 \\  3 \end{matrix}\right) \right\} \) . Thus \( \dim {E}_{2} = 1 < 2 \) , and therefore \( M \) is not diagonalizable.

On va donc trigonaliser \( M \) . Désignons par \( B \) la base canonique de \( {\mathbb{C}}^{3} \) , et soit \( f \in \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) telle que \( {\left\lbrack f\right\rbrack }_{B} = M \) . Soit

> We will therefore trigonalize \( M \) . Let \( B \) denote the canonical basis of \( {\mathbb{C}}^{3} \) , and let \( f \in \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) be such that \( {\left\lbrack f\right\rbrack }_{B} = M \) . Let

\[
{e}_{1} = \left( \begin{array}{l} 1 \\  1 \\  1 \end{array}\right) ,\;{e}_{2} = \left( \begin{array}{l} 4 \\  3 \\  4 \end{array}\right) ,\;{e}_{3} = \left( \begin{array}{l} 0 \\  0 \\  1 \end{array}\right)
\]

La famille \( {B}^{\prime } = \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) est une base, et on a \( {E}_{3} = \operatorname{Vect}{e}_{1} \) et \( {E}_{2} = \operatorname{Vect}{e}_{2} \) . On calcule les valeurs de \( f \) sur cette nouvelle base :

> The family \( {B}^{\prime } = \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) is a basis, and we have \( {E}_{3} = \operatorname{Vect}{e}_{1} \) and \( {E}_{2} = \operatorname{Vect}{e}_{2} \) . We calculate the values of \( f \) in this new basis:

\[
f\left( {e}_{1}\right)  = 3{e}_{1},\;f\left( {e}_{2}\right)  = 2{e}_{2},\;f\left( {e}_{3}\right)  = \left( \begin{matrix}  - 2 \\   - 3 \end{matrix}\right)  = {e}_{2} - 6{e}_{1} + 2{e}_{3},
\]

donc la matrice de \( f \) dans la base \( {B}^{\prime } \) est

> therefore the matrix of \( f \) in the basis \( {B}^{\prime } \) is

\[
{\left\lbrack  f\right\rbrack  }_{{B}^{\prime }} = T = \left( \begin{array}{rrr} 3 & 0 &  - 6 \\  0 & 2 & 1 \\  0 & 0 & 2 \end{array}\right)
\]

donc si \( P \) est la matrice de passage de la base \( B \) à la base \( {B}^{\prime } \) ,

> so if \( P \) is the transition matrix from basis \( B \) to basis \( {B}^{\prime } \) ,

\[
P = \left( \begin{array}{lll} 1 & 4 & 0 \\  1 & 3 & 0 \\  1 & 4 & 1 \end{array}\right)
\]

on a \( {P}^{-1}{\left\lbrack f\right\rbrack }_{B}P = {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) , ou encore \( {P}^{-1}{MP} = T \) . Au passage, on remarque que les termes de la diagonale principale de la matrice triangulaire \( T \) sont les racines du polynôme caractéristique de \( M \) , répétés avec la même multiplicité. Ceci est cohérent car \( T \) et \( M \) étant semblables, elles ont même polynôme caractéristique.

> we have \( {P}^{-1}{\left\lbrack f\right\rbrack }_{B}P = {\left\lbrack f\right\rbrack }_{{B}^{\prime }} \) , or also \( {P}^{-1}{MP} = T \) . Incidentally, we note that the terms on the main diagonal of the triangular matrix \( T \) are the roots of the characteristic polynomial of \( M \) , repeated with the same multiplicity. This is consistent because \( T \) and \( M \) are similar, so they have the same characteristic polynomial.

d) Ici, \( {P}_{M} = {\left( 1 - X\right) }^{3} \) . Un calcul donne \( \operatorname{rg}\left( {M - {I}_{3}}\right) = 2 \) , donc dim \( {E}_{1} = \dim \left\lbrack {\operatorname{Ker}\left( {M - {I}_{3}}\right) }\right\rbrack = \; 3 - \operatorname{rg}\left( {M - {I}_{3}}\right) = 1 \) . D’après le théorème \( 2, M \) n’est donc pas diagonalisable. Nous allons la trigonaliser. (C'est plus complexe qu'à la question précédente. Au c), on avait trouvé deux vecteurs propres indépendants. Il ne restait plus qu'à en trouver un troisième, formant une base avec les deux autres, puis à en exprimer l'image par \( M \) pour trigonaliser \( M \) . Ici il n’y a qu'un seul vecteur propre et cette méthode ne va pas fonctionner. Nous allons procéder comme dans la démonstration du théorème 3 de trigonalisation. Nous allons donner deux méthodes, correspondant chacune à l'une des deux démonstrations du théorème 3.)

> d) Here, \( {P}_{M} = {\left( 1 - X\right) }^{3} \) . A calculation gives \( \operatorname{rg}\left( {M - {I}_{3}}\right) = 2 \) , so dim \( {E}_{1} = \dim \left\lbrack {\operatorname{Ker}\left( {M - {I}_{3}}\right) }\right\rbrack = \; 3 - \operatorname{rg}\left( {M - {I}_{3}}\right) = 1 \) . According to the theorem, \( 2, M \) is therefore not diagonalizable. We will trigonalize it. (This is more complex than in the previous question. In c), we found two independent eigenvectors. All that remained was to find a third one, forming a basis with the other two, then to express its image by \( M \) to trigonalize \( M \) . Here there is only one eigenvector and this method will not work. We will proceed as in the proof of theorem 3 of trigonalization. We will provide two methods, each corresponding to one of the two proofs of theorem 3.)

- Première méthode. On note \( B \) la base canonique de \( {\mathbb{C}}^{3} \) . Soit \( f \in  \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) telle que \( {\left\lbrack  f\right\rbrack  }_{B} = M \) .

> - First method. Let \( B \) be the canonical basis of \( {\mathbb{C}}^{3} \) . Let \( f \in  \mathcal{L}\left( {\mathbb{C}}^{3}\right) \) be such that \( {\left\lbrack  f\right\rbrack  }_{B} = M \) .

On cherche un hyperplan stable par \( f \) . Soit \( {B}^{ * } \) la base duale de \( B \) , de sorte que \( {\left\lbrack {}^{\mathrm{t}}f\right\rbrack }_{{B}^{ * }} = {}^{\mathrm{t}}M \) . On a \( {P}_{{}^{t}f} = {P}_{{}^{t}M} = {P}_{M} = {\left( 1 - X\right) }^{3} \) ,1 est donc valeur propre de \( {}^{t}f \) . Recherchons en un vecteur propre \( u \) . Si \( U \) désigne la matrice colonne de \( u \) dont les éléments sont les coordonnées de \( u \) dans la base \( {B}^{ * } \) , on a \( {}^{\mathrm{t}}f\left( u\right) = u \Leftrightarrow {}^{\mathrm{t}}{MU} = U \) . En résolvant le système \( {}^{\mathrm{t}}{MU} = U \) , on trouve que \( U = \left( \begin{matrix} - 2 \\ 1 \\ 1 \end{matrix}\right) \) convient. L’orthogonal \( H \) de \( \mathbb{C}u \) dans \( {\mathbb{C}}^{3} \) est stable par \( f \) . On a \( H = \; \operatorname{Ker}u = \left\{ {\left( \begin{array}{l} x \\ y \\ z \end{array}\right) , - {2x} + y + z = 0}\right\} \) , dont \( {B}_{1} = \left( {{e}_{1},{e}_{2}}\right) = \left( {\left( \begin{array}{l} 1 \\ 0 \\ 2 \end{array}\right) ,\left( \begin{matrix} 0 \\ 1 \\ - 1 \end{matrix}\right) }\right) \) forme une base. On trouve \( f\left( {e}_{1}\right) = - 4{e}_{1} - 5{e}_{2} \) et \( f\left( {e}_{2}\right) = 5{e}_{1} + 6{e}_{2} \) , donc

> We are looking for a hyperplane stable by \( f \). Let \( {B}^{ * } \) be the dual basis of \( B \), such that \( {\left\lbrack {}^{\mathrm{t}}f\right\rbrack }_{{B}^{ * }} = {}^{\mathrm{t}}M \). We have \( {P}_{{}^{t}f} = {P}_{{}^{t}M} = {P}_{M} = {\left( 1 - X\right) }^{3} \), so 1 is an eigenvalue of \( {}^{t}f \). Let us look for an eigenvector \( u \). If \( U \) denotes the column matrix of \( u \) whose elements are the coordinates of \( u \) in the basis \( {B}^{ * } \), we have \( {}^{\mathrm{t}}f\left( u\right) = u \Leftrightarrow {}^{\mathrm{t}}{MU} = U \). By solving the system \( {}^{\mathrm{t}}{MU} = U \), we find that \( U = \left( \begin{matrix} - 2 \\ 1 \\ 1 \end{matrix}\right) \) is suitable. The orthogonal \( H \) of \( \mathbb{C}u \) in \( {\mathbb{C}}^{3} \) is stable by \( f \). We have \( H = \; \operatorname{Ker}u = \left\{ {\left( \begin{array}{l} x \\ y \\ z \end{array}\right) , - {2x} + y + z = 0}\right\} \), of which \( {B}_{1} = \left( {{e}_{1},{e}_{2}}\right) = \left( {\left( \begin{array}{l} 1 \\ 0 \\ 2 \end{array}\right) ,\left( \begin{matrix} 0 \\ 1 \\ - 1 \end{matrix}\right) }\right) \) forms a basis. We find \( f\left( {e}_{1}\right) = - 4{e}_{1} - 5{e}_{2} \) and \( f\left( {e}_{2}\right) = 5{e}_{1} + 6{e}_{2} \), therefore

\[
{\left\lbrack  {f}_{\mid H}\right\rbrack  }_{{B}_{1}} = \left( \begin{matrix}  - 4 & 5 \\   - 5 & 6 \end{matrix}\right)  = N.
\]

Au passage, on remarque que \( {P}_{N} = {\left( X - 1\right) }^{2} = {P}_{{f}_{\mid H}} \) divise \( {P}_{f} \) , conformément à la proposition 2.

> Incidentally, we note that \( {P}_{N} = {\left( X - 1\right) }^{2} = {P}_{{f}_{\mid H}} \) divides \( {P}_{f} \), in accordance with proposition 2.

Nous allons maintenant trigonaliser \( N \) . On recherche d’abord un vecteur propre de \( N \) (qui est associé à la seule valeur propre 1). En résolvant \( {NY} = Y \) , on trouve que \( Y = \left( \begin{array}{l} 1 \\ 1 \end{array}\right) \) convient, donc que \( f\left( {{e}_{1} + {e}_{2}}\right) = {e}_{1} + {e}_{2} \) . On pose

> We will now trigonalize \( N \). We first look for an eigenvector of \( N \) (which is associated with the only eigenvalue 1). By solving \( {NY} = Y \), we find that \( Y = \left( \begin{array}{l} 1 \\ 1 \end{array}\right) \) is suitable, so that \( f\left( {{e}_{1} + {e}_{2}}\right) = {e}_{1} + {e}_{2} \). We set

\[
{e}_{1}^{\prime } = {e}_{1} + {e}_{2} = \left( \begin{array}{l} 1 \\  1 \\  1 \end{array}\right) \;\text{ et }\;{e}_{2}^{\prime } = {e}_{2} = \left( \begin{matrix} 0 \\  1 \\   - 1 \end{matrix}\right) ,
\]

de sorte que \( \left( {{e}_{1}^{\prime },{e}_{2}^{\prime }}\right) \) est une autre base de \( H \) . Un petit calcul donne \( f\left( {e}_{1}^{\prime }\right) = {e}_{1}^{\prime } \) et \( f\left( {e}_{2}^{\prime }\right) = 5{e}_{1}^{\prime } + {e}_{2}^{\prime } \) . Si maintenant on pose \( {e}_{3}^{\prime } = \left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array}\right) ,{B}^{\prime } = \left( {{e}_{1}^{\prime },{e}_{2}^{\prime },{e}_{3}^{\prime }}\right) \) forme une base de \( {\mathbb{C}}^{3} \) et \( f\left( {e}_{3}^{\prime }\right) = - 3{e}_{1}^{\prime } - 2{e}_{2}^{\prime } + {e}_{3}^{\prime } \) , donc

> so that \( \left( {{e}_{1}^{\prime },{e}_{2}^{\prime }}\right) \) is another basis of \( H \) . A short calculation gives \( f\left( {e}_{1}^{\prime }\right) = {e}_{1}^{\prime } \) and \( f\left( {e}_{2}^{\prime }\right) = 5{e}_{1}^{\prime } + {e}_{2}^{\prime } \) . If we now set \( {e}_{3}^{\prime } = \left( \begin{array}{l} 0 \\ 0 \\ 1 \end{array}\right) ,{B}^{\prime } = \left( {{e}_{1}^{\prime },{e}_{2}^{\prime },{e}_{3}^{\prime }}\right) \) forms a basis of \( {\mathbb{C}}^{3} \) and \( f\left( {e}_{3}^{\prime }\right) = - 3{e}_{1}^{\prime } - 2{e}_{2}^{\prime } + {e}_{3}^{\prime } \) , therefore

\[
{\left\lbrack  f\right\rbrack  }_{{B}^{\prime }} = \left( \begin{matrix} 1 & 5 &  - 3 \\  0 & 1 &  - 2 \\  0 & 0 & 1 \end{matrix}\right)  = T = {P}^{-1}{\left\lbrack  f\right\rbrack  }_{B}P\;\text{ avec }\;P = \left( \begin{matrix} 1 & 0 & 0 \\  1 & 1 & 0 \\  1 &  - 1 & 1 \end{matrix}\right) ,
\]

et donc \( T = {P}^{-1}{MP} \) .

> and thus \( T = {P}^{-1}{MP} \) .

- Seconde méthode. Commençons par rechercher un vecteur propre \( {u}_{1} \) pour \( f \) associé à la valeur propre 1. Un petit calcul devenu maintenant routinier montre que \( {u}_{1} = \left( \begin{array}{l} 1 \\  1 \\  1 \end{array}\right) \) convient. On pose maintenant \( {u}_{2} = \left( \begin{array}{l} 0 \\  1 \\  0 \end{array}\right) \) et \( {u}_{3} = \left( \begin{array}{l} 0 \\  0 \\  1 \end{array}\right) \) , de sorte que \( {B}_{0} = \left( {{u}_{1},{u}_{2},{u}_{3}}\right) \) forme une base de \( {\mathbb{C}}^{3} \) . En exprimant les valeurs prises par \( f \) sur les vecteurs de \( {B}_{0} \) dans cette même base, on trouve

> - Second method. Let us start by looking for an eigenvector \( {u}_{1} \) for \( f \) associated with the eigenvalue 1. A short calculation, now routine, shows that \( {u}_{1} = \left( \begin{array}{l} 1 \\  1 \\  1 \end{array}\right) \) works. We now set \( {u}_{2} = \left( \begin{array}{l} 0 \\  1 \\  0 \end{array}\right) \) and \( {u}_{3} = \left( \begin{array}{l} 0 \\  0 \\  1 \end{array}\right) \) , so that \( {B}_{0} = \left( {{u}_{1},{u}_{2},{u}_{3}}\right) \) forms a basis of \( {\mathbb{C}}^{3} \) . By expressing the values taken by \( f \) on the vectors of \( {B}_{0} \) in this same basis, we find

\[
{\left\lbrack  f\right\rbrack  }_{{B}_{0}} = \left( \begin{matrix} 1 & 2 &  - 3 \\  0 &  - 1 &  - 2 \\  0 & 2 & 3 \end{matrix}\right)
\]

Soit \( H = \operatorname{Vect}\left( {{u}_{2},{u}_{3}}\right) \) et soit \( p \) la projection sur \( H \) parallèlement à \( \mathbb{C}{u}_{1} \) . Soit \( g = p \circ {f}_{\mid H} \in \; \mathcal{L}\left( H\right) \) . La matrice de \( g \) dans la base \( \left( {{u}_{2},{u}_{3}}\right) \) de \( H \) est

> Let \( H = \operatorname{Vect}\left( {{u}_{2},{u}_{3}}\right) \) and let \( p \) be the projection onto \( H \) parallel to \( \mathbb{C}{u}_{1} \) . Let \( g = p \circ {f}_{\mid H} \in \; \mathcal{L}\left( H\right) \) . The matrix of \( g \) in the basis \( \left( {{u}_{2},{u}_{3}}\right) \) of \( H \) is

\[
A = {\left\lbrack  g\right\rbrack  }_{\left( {u}_{2},{u}_{3}\right) } = \left( \begin{matrix}  - 1 &  - 2 \\  2 & 3 \end{matrix}\right) .
\]

On a \( {P}_{A} = {P}_{g} = {\left( X - 1\right) }^{2} \) . Recherchons un vecteur propre de \( g \) associé à la valeur propre 1 . On remarque que \( {u}_{2}^{\prime } = {u}_{2} - {u}_{3} \) convient. On pose alors \( {u}_{3}^{\prime } = {u}_{2} \) , de sorte que \( \left( {{u}_{2}^{\prime },{u}_{3}^{\prime }}\right) \) forme une nouvelle base de \( H \) . Dans la nouvelle base \( {B}_{0}^{\prime } = \left( {{u}_{1},{u}_{2}^{\prime },{u}_{3}^{\prime }}\right) \) de \( {\mathbb{C}}^{3} \) , on trouve

> We have \( {P}_{A} = {P}_{g} = {\left( X - 1\right) }^{2} \) . Let us look for an eigenvector of \( g \) associated with the eigenvalue 1 . We note that \( {u}_{2}^{\prime } = {u}_{2} - {u}_{3} \) works. We then set \( {u}_{3}^{\prime } = {u}_{2} \) , so that \( \left( {{u}_{2}^{\prime },{u}_{3}^{\prime }}\right) \) forms a new basis of \( H \) . In the new basis \( {B}_{0}^{\prime } = \left( {{u}_{1},{u}_{2}^{\prime },{u}_{3}^{\prime }}\right) \) of \( {\mathbb{C}}^{3} \) , we find

\[
{\left\lbrack  f\right\rbrack  }_{{B}_{0}^{\prime }} = \left( \begin{matrix} 1 & 5 & 2 \\  0 & 1 &  - 2 \\  0 & 0 & 1 \end{matrix}\right)  = T = {P}^{-1}{\left\lbrack  f\right\rbrack  }_{B}P\;\text{ avec }\;P = \left( \begin{matrix} 1 & 0 & 0 \\  1 & 1 & 1 \\  1 &  - 1 & 0 \end{matrix}\right) .
\]

Donc \( T = {P}^{-1}{MP} \) : on a trigonalisé \( M \) . On remarque au passage que les termes de la diagonale principale de la matrice triangulaire trouvée correspondent aux racines du polynôme caractéris-tique de la matrice \( M \) de départ.

> Thus \( T = {P}^{-1}{MP} \) : we have trigonalized \( M \) . We note in passing that the terms on the main diagonal of the triangular matrix found correspond to the roots of the characteristic polynomial of the initial matrix \( M \) .

Remarque. Pour suivre correctement les deux méthodes exposées au d), il est bon de relire les démonstrations du théorème 3. Bien sûr, on ne retrouve pas les mêmes matrices triangulaires et de passage à l'arrivée selon la méthode utilisée (il n'y a pas unicité).

> Remark. To correctly follow the two methods presented in d), it is good to reread the proofs of theorem 3. Of course, we do not obtain the same triangular and transition matrices at the end depending on the method used (there is no uniqueness).

EXERCICE 2. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie et \( f \in \mathcal{L}\left( E\right) \) un endomorphisme de rang 1. Donner une condition nécessaire et suffisante sur \( f \) pour que \( f \) soit diagonalisable. Que peut-on dire lorsque \( f \) n’est pas diagonalisable ?

> EXERCISE 2. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space and \( f \in \mathcal{L}\left( E\right) \) be an endomorphism of rank 1. Give a necessary and sufficient condition on \( f \) for \( f \) to be diagonalizable. What can be said when \( f \) is not diagonalizable?

Solution. On note \( n = \dim E \) . Par hypothèse, \( \dim \operatorname{Ker}f = n - \operatorname{rg}f = n - 1 \) , autrement dit 0 est une valeur propre de \( f \) d’ordre \( n - 1 \) , donc racine du polynôme caractéristique \( {P}_{f} \) de \( f \) d’ordre au moins \( n - 1 \) . Par conséquent, il existe \( \alpha \in \mathbb{K} \) tel que \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n - 1}\left( {X - \alpha }\right) \) . La somme des valeurs propres de \( f \) étant égale à la trace de \( f \) , on a \( \alpha = \operatorname{tr}f \) .

> Solution. Let \( n = \dim E \) . By hypothesis, \( \dim \operatorname{Ker}f = n - \operatorname{rg}f = n - 1 \) , in other words 0 is an eigenvalue of \( f \) of order \( n - 1 \) , and thus a root of the characteristic polynomial \( {P}_{f} \) of \( f \) of order at least \( n - 1 \) . Consequently, there exists \( \alpha \in \mathbb{K} \) such that \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n - 1}\left( {X - \alpha }\right) \) . Since the sum of the eigenvalues of \( f \) is equal to the trace of \( f \) , we have \( \alpha = \operatorname{tr}f \) .

Ainsi, si tr \( f \neq 0, f \) admet une valeur propre \( \alpha \neq 0 \) . Les sous-espaces propres \( {E}_{0} \) et \( {E}_{\alpha } \) de \( f \) vérifient alors \( \dim {E}_{0} + \dim {E}_{\alpha } = n \) donc \( f \) est diagonalisable.

> Thus, if tr \( f \neq 0, f \) admits an eigenvalue \( \alpha \neq 0 \) . The eigenspaces \( {E}_{0} \) and \( {E}_{\alpha } \) of \( f \) then satisfy \( \dim {E}_{0} + \dim {E}_{\alpha } = n \) , therefore \( f \) is diagonalizable.

Lorsque tr \( f = 0,0 \) est la seule valeur propre de \( f \) . Si \( f \) était diagonalisable, \( f \) serait nulle, ce qui est absurde. Finalement, \( f \) est diagonalisable si et seulement si tr \( f \neq 0 \) .

> When tr \( f = 0,0 \) is the only eigenvalue of \( f \) . If \( f \) were diagonalizable, \( f \) would be zero, which is absurd. Finally, \( f \) is diagonalizable if and only if tr \( f \neq 0 \) .

Lorsque \( f \) n’est pas diagonalisable, c’est-à-dire lorsque tr \( f = 0 \) , on a \( {f}^{2} = 0 \) . En effet. Soit \( {e}_{1} \in E \) tel que \( \operatorname{Im}f = \operatorname{Vect}{e}_{1} \) . Complétons \( {e}_{1} \) en une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . Dans cette base, la matrice de \( f \) a la forme

> When \( f \) is not diagonalizable, that is to say when tr \( f = 0 \) , we have \( {f}^{2} = 0 \) . Indeed. Let \( {e}_{1} \in E \) be such that \( \operatorname{Im}f = \operatorname{Vect}{e}_{1} \) . Complete \( {e}_{1} \) into a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . In this basis, the matrix of \( f \) has the form

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} {\alpha }_{1} & {\alpha }_{2} & \cdots & {\alpha }_{n} \\  0 & 0 & \cdots & 0 \\  \vdots & \vdots & & \vdots \\  0 & 0 & \cdots & 0 \end{matrix}\right) .
\]

Comme tr \( f = {\alpha }_{1} = 0 \) , on a \( {\left\lbrack f\right\rbrack }_{B}^{2} = 0 \) , c’est-à-dire \( {f}^{2} = 0 \) .

> Since tr \( f = {\alpha }_{1} = 0 \) , we have \( {\left\lbrack f\right\rbrack }_{B}^{2} = 0 \) , that is to say \( {f}^{2} = 0 \) .

EXERCICE 3. Soient \( {a}_{1},\ldots ,{a}_{n - 1} \) et \( {b}_{1},\ldots ,{b}_{n - 1} \) des nombres réels, avec \( n \geq 3 \) . Donner une condition nécessaire et suffisante pour que la matrice

> EXERCISE 3. Let \( {a}_{1},\ldots ,{a}_{n - 1} \) and \( {b}_{1},\ldots ,{b}_{n - 1} \) be real numbers, with \( n \geq 3 \) . Give a necessary and sufficient condition for the matrix

\[
A = \left( \begin{matrix} 0 & \cdots & 0 & {b}_{1} \\  \vdots & & \vdots & \vdots \\  0 & \cdots & 0 & {b}_{n - 1} \\  {a}_{1} & \cdots & {a}_{n - 1} & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right)
\]

soit diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> to be diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

Solution. Si tous les \( {a}_{i} \) sont nuls, \( A \) est une matrice triangulaire dont les valeurs propres sont données par ses éléments diagonaux, montrant ainsi que toutes les valeurs propres de \( A \) sont nulles. Si \( A \) est diagonalisable, \( A \) est donc nulle et tous les \( {b}_{i} \) sont nuls. De même, si tous les \( {b}_{i} \) sont nuls et si \( A \) est diagonalisable, alors tous les \( {a}_{i} \) sont nuls.

> Solution. If all \( {a}_{i} \) are zero, \( A \) is a triangular matrix whose eigenvalues are given by its diagonal elements, thus showing that all eigenvalues of \( A \) are zero. If \( A \) is diagonalizable, \( A \) is therefore zero and all \( {b}_{i} \) are zero. Similarly, if all \( {b}_{i} \) are zero and if \( A \) is diagonalizable, then all \( {a}_{i} \) are zero.

Supposons maintenant les \( {a}_{i} \) non tous nuls et les \( {b}_{i} \) non tous nuls. Alors le rang de \( A \) est 2, ce qui montre que 0 est valeur propre de \( A \) et que le sous-espace propre \( {E}_{0} \) associé est de dimension \( n - 2 \) . Notons \( {\lambda }_{1},{\lambda }_{2} \in \mathbb{C} \) les deux autres valeurs propres de \( A \) . La somme des valeurs propres de \( A \) est sa trace donc \( {\lambda }_{1} + {\lambda }_{2} = 0 \) . Il nous faut un autre renseignement pour pouvoir évaluer \( {\lambda }_{1} \) et \( {\lambda }_{2} \) . Pour cela, on remarque que les valeurs propres de \( {A}^{2} \) sont les carrés des valeurs propres de \( A \) (pour s’en persuader, trigonaliser \( A \) dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) ), donc \( {\lambda }_{1}^{2} + {\lambda }_{2}^{2} = \operatorname{tr}\left( {A}^{2}\right) \) . Un petit calcul donne \( \operatorname{tr}\left( {A}^{2}\right) = 2\left( {\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i}}\right) \) . Finalement on a montré

> Now suppose the \( {a}_{i} \) are not all zero and the \( {b}_{i} \) are not all zero. Then the rank of \( A \) is 2, which shows that 0 is an eigenvalue of \( A \) and that the associated eigenspace \( {E}_{0} \) has dimension \( n - 2 \). Let \( {\lambda }_{1},{\lambda }_{2} \in \mathbb{C} \) be the two other eigenvalues of \( A \). The sum of the eigenvalues of \( A \) is its trace, so \( {\lambda }_{1} + {\lambda }_{2} = 0 \). We need another piece of information to be able to evaluate \( {\lambda }_{1} \) and \( {\lambda }_{2} \). To do this, we note that the eigenvalues of \( {A}^{2} \) are the squares of the eigenvalues of \( A \) (to be convinced of this, trigonalize \( A \) in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \)), so \( {\lambda }_{1}^{2} + {\lambda }_{2}^{2} = \operatorname{tr}\left( {A}^{2}\right) \). A short calculation gives \( \operatorname{tr}\left( {A}^{2}\right) = 2\left( {\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i}}\right) \). Finally, we have shown

\[
{\lambda }_{1} + {\lambda }_{2} = 0\;\text{ et }\;{\lambda }_{1}^{2} + {\lambda }_{2}^{2} = 2\left( {\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i}}\right) .
\]

(*)

> Si \( \Delta = \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} < 0 \) ,(*) montre que \( {\lambda }_{1} \) et \( {\lambda }_{2} \) ne peuvent pas être des nombres réels (et donc \( A \) n’est pas diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ). Si maintenant \( \Delta \geq 0,\left( *\right) \) montre que \( {\lambda }_{1} = - {\lambda }_{2} = \sqrt{\Delta } \) . Si \( \Delta = 0,{\lambda }_{1} = {\lambda }_{2} = 0 \) et \( A \) n’est pas diagonalisable sinon \( A \) serait nulle (sa seule valeur propre est 0 ). Si \( \Delta > 0,{\lambda }_{1} \) et \( {\lambda }_{2} \) sont réelles, distinctes et non nulles, et les sous-espaces propres \( {E}_{{\lambda }_{1}},{E}_{{\lambda }_{2}} \) associés sont de dimension 1. Dans ce cas, \( \dim {E}_{0} + \dim {E}_{{\lambda }_{1}} + \dim {E}_{{\lambda }_{2}} = n \) , donc \( A \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

If \( \Delta = \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} < 0 \), (*) shows that \( {\lambda }_{1} \) and \( {\lambda }_{2} \) cannot be real numbers (and thus \( A \) is not diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \)). If now \( \Delta \geq 0,\left( *\right) \) shows that \( {\lambda }_{1} = - {\lambda }_{2} = \sqrt{\Delta } \). If \( \Delta = 0,{\lambda }_{1} = {\lambda }_{2} = 0 \) and \( A \) is not diagonalizable, otherwise \( A \) would be zero (its only eigenvalue is 0). If \( \Delta > 0,{\lambda }_{1} \) and \( {\lambda }_{2} \) are real, distinct, and non-zero, and the associated eigenspaces \( {E}_{{\lambda }_{1}},{E}_{{\lambda }_{2}} \) are of dimension 1. In this case, \( \dim {E}_{0} + \dim {E}_{{\lambda }_{1}} + \dim {E}_{{\lambda }_{2}} = n \), so \( A \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \).

> De tout ceci, le lecteur conclura facilement que \( A \) est diagonalisable dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) si et seule-ment si \( A = 0 \) ou \( \Delta = \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} > 0 \) .

From all this, the reader will easily conclude that \( A \) is diagonalizable in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) if and only if \( A = 0 \) or \( \Delta = \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}_{i}{b}_{i} > 0 \).

> EXERCICE 4. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . On considère une famille \( {\left( {f}_{i}\right) }_{i \in I} \) d’endomorphismes de \( E \) commutant deux à deux.

EXERCISE 4. Let \( E \) be a finite-dimensional \( \mathbb{K} \)-v.s. \( n \in {\mathbb{N}}^{ * } \). Consider a family \( {\left( {f}_{i}\right) }_{i \in I} \) of endomorphisms of \( E \) that commute with each other.

> a) Si les \( {f}_{i} \) sont diagonalisables, montrer que l’on peut les diagonaliser tous dans une même base.

a) If the \( {f}_{i} \) are diagonalizable, show that they can all be diagonalized in the same basis.

> b) Si les \( {f}_{i} \) sont trigonalisables, montrer que l’on peut les trigonaliser tous dans une même base.

b) If the \( {f}_{i} \) are trigonalizable, show that they can all be trigonalized in the same basis.

---

Solution. a) Procédons par récurrence sur \( n \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Si tous les \( {f}_{i} \) sont des homothéties, c’est terminé.

> Solution. a) Let us proceed by induction on \( n \) . For \( n = 1 \) , it is obvious. Assume the result holds up to rank \( n - 1 \) and show it for rank \( n \) . If all \( {f}_{i} \) are homotheties, we are done.

---

Sinon il existe \( {i}_{0} \) tel que \( {f}_{{i}_{0}} \) n’est pas une homothétie. Si on note \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) ses sous-espaces propres, on a donc \( r \geq 2 \) , et pour tout \( j \) , dim \( {E}_{{\lambda }_{j}} < n \) . Par ailleurs, d’après la proposition 7 page 175, pour tout \( j,{E}_{{\lambda }_{j}} \) est stable par tous les \( {f}_{i} \) , et chaque \( {f}_{i \mid {E}_{{\lambda }_{j}}} \) est diagonalisable d’après la proposition 6. Donc d’après l’hypothèse de récurrence il existe une base \( {B}_{j} \) de \( {E}_{{\lambda }_{j}} \) qui soit une base de diagonalisation de tous les \( {f}_{i \mid {E}_{{\lambda }_{j}}} \) . Donc \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) est une base de diagonalisation de tous les \( {\left( {f}_{i}\right) }_{i \in I} \) .

> Otherwise, there exists \( {i}_{0} \) such that \( {f}_{{i}_{0}} \) is not a homothety. If we denote its eigenspaces by \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) , we have \( r \geq 2 \) , and for all \( j \) , dim \( {E}_{{\lambda }_{j}} < n \) . Furthermore, according to proposition 7 on page 175, for all \( j,{E}_{{\lambda }_{j}} \) is stable under all \( {f}_{i} \) , and each \( {f}_{i \mid {E}_{{\lambda }_{j}}} \) is diagonalizable according to proposition 6. Thus, by the induction hypothesis, there exists a basis \( {B}_{j} \) of \( {E}_{{\lambda }_{j}} \) which is a basis of diagonalization for all \( {f}_{i \mid {E}_{{\lambda }_{j}}} \) . Therefore, \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) is a basis of diagonalization for all \( {\left( {f}_{i}\right) }_{i \in I} \) .

b) Commençons par montrer par récurrence sur \( n \) qu’il existe un vecteur propre commun à tous les \( {\left( {f}_{i}\right) }_{i \in I} \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Si tous les \( {f}_{i} \) sont des homothéties, c’est terminé. Sinon, il existe un endomorphisme \( f \) de la famille qui n’est pas une homothétie. Comme \( f \) est trigonalisable, \( f \) admet une valeur propre \( \lambda \) , donc un sous-espace propre correspondant \( {E}_{\lambda } \) . On a dim \( {E}_{\lambda } < n \) (car \( f \) n’est pas une homothétie) et \( {E}_{\lambda } \) est stable par tous les \( {f}_{i} \) . D’après l’hypothèse de récurrence, il existe donc un vecteur propre commun à tous les \( {f}_{i \mid {E}_{\lambda }} \) , qui est bien sûr un vecteur propre commun à tous les \( {f}_{i} \) .

> b) Let us begin by showing by induction on \( n \) that there exists a common eigenvector for all \( {\left( {f}_{i}\right) }_{i \in I} \) . For \( n = 1 \) , it is obvious. Assume the result holds up to rank \( n - 1 \) and show it for rank \( n \) . If all \( {f}_{i} \) are homotheties, we are done. Otherwise, there exists an endomorphism \( f \) in the family that is not a homothety. Since \( f \) is trigonalizable, \( f \) admits an eigenvalue \( \lambda \) , and thus a corresponding eigenspace \( {E}_{\lambda } \) . We have dim \( {E}_{\lambda } < n \) (since \( f \) is not a homothety) and \( {E}_{\lambda } \) is stable under all \( {f}_{i} \) . According to the induction hypothesis, there therefore exists a common eigenvector for all \( {f}_{i \mid {E}_{\lambda }} \) , which is naturally a common eigenvector for all \( {f}_{i} \) .

Achevons la démonstration par récurrence sur \( n \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . En appliquant le résultat précédent aux applications transposées \( {}^{\mathrm{t}}{f}_{i} \) (elles commutent également et sont également trigonalisables puisque \( {P}_{{t}_{{f}_{i}}} = {P}_{{f}_{i}} \) ), on voit qu’il existe \( x \in {E}^{ * } \) un vecteur propre commun à tous les \( {}^{\mathrm{t}}{f}_{i} \) . L’orthogonal \( H \) de \( \mathbb{K}x \) dans \( E \) est donc un hyperplan de \( E \) stable par tous les \( {f}_{i} \) . D’après l’hypothèse de récurrence, il existe une base \( B \) de \( H \) trigonalisant tous les \( {f}_{i \mid H} \) . Soit \( e \in E \) tel que \( {B}^{\prime } = \left( {B, e}\right) \) forme une base de \( E \) . On a pour tout \( i \in I \)

> Let us complete the proof by induction on \( n \). For \( n = 1 \), it is obvious. Assume the result is true at rank \( n - 1 \) and show it at rank \( n \). By applying the previous result to the transposed maps \( {}^{\mathrm{t}}{f}_{i} \) (they also commute and are also trigonalizable since \( {P}_{{t}_{{f}_{i}}} = {P}_{{f}_{i}} \)), we see that there exists \( x \in {E}^{ * } \) a common eigenvector for all \( {}^{\mathrm{t}}{f}_{i} \). The orthogonal \( H \) of \( \mathbb{K}x \) in \( E \) is therefore a hyperplane of \( E \) stable under all \( {f}_{i} \). According to the induction hypothesis, there exists a basis \( B \) of \( H \) trigonalizing all \( {f}_{i \mid H} \). Let \( e \in E \) be such that \( {B}^{\prime } = \left( {B, e}\right) \) forms a basis of \( E \). We have for all \( i \in I \)

\[
{\left\lbrack  {f}_{i}\right\rbrack  }_{{B}^{\prime }} = \left( \begin{matrix}  \times  & \cdots &  \times  &  \times  \\   &  \ddots  & \vdots & \vdots \\   & \left( 0\right) &  \times  &  \times  \\  0 & \cdots & 0 &  \times   \end{matrix}\right) ,
\]

donc la base \( {B}^{\prime } \) trigonalise tous les \( {f}_{i} \) .

> therefore the basis \( {B}^{\prime } \) trigonalizes all \( {f}_{i} \).

Remarque. Dans cette dernière partie de b), nous avons utilisé une technique analogue à celle de la première démonstration du théorème 5. On pourrait également procéder comme dans la seconde démonstration de ce théorème.

> Remark. In this last part of b), we used a technique analogous to that of the first proof of Theorem 5. One could also proceed as in the second proof of this theorem.

EXERCICE 5 (LEMME DE SCHUR). a) Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie. Soit \( Q \subset \mathcal{L}\left( E\right) \) irréductible, c’est-à-dire que les seuls sous-espaces de \( E \) stables par tous les éléments de \( Q \) sont \( \{ 0\} \) et \( E \) . Montrer que les seuls éléments commutant avec tous les éléments de \( Q \) sont les homothéties.

> EXERCISE 5 (SCHUR'S LEMMA). a) Let \( E \) be a finite-dimensional \( \mathbb{C} \)-v.s. Let \( Q \subset \mathcal{L}\left( E\right) \) be irreducible, meaning that the only subspaces of \( E \) stable under all elements of \( Q \) are \( \{ 0\} \) and \( E \). Show that the only elements commuting with all elements of \( Q \) are homotheties.

b) Si \( E \) est un \( \mathbb{R} \) -e.v de dimension finie, montrer que le résultat est faux dans le cas général. Quand peut-on dire qu'il est vrai ?

> b) If \( E \) is a finite-dimensional \( \mathbb{R} \)-v.s., show that the result is false in the general case. When can we say it is true?

Solution. a) Soit \( f \in \mathcal{L}\left( E\right) \) commutant avec tous les éléments de \( Q \) . Le corps \( \mathbb{C} \) étant algébrique-ment clos, \( f \) admet au moins une valeur propre \( \lambda \) . Soit \( {E}_{\lambda } \) le sous-espace propre correspondant. On a \( {E}_{\lambda } \neq \{ 0\} \) . Par hypothèse sur \( f \) , pour tout \( g \in Q \) , on a \( f \circ g = g \circ f \) . D’après la proposition 7 page 175, \( {E}_{\lambda } \) est stable par tous les éléments de \( Q \) . Comme \( {E}_{\lambda } \neq \{ 0\} \) et que \( Q \) est irréductible, ceci entraîne \( {E}_{\lambda } = E \) . Donc \( f = \lambda {\operatorname{Id}}_{E} \) est une homothétie.

> Solution. a) Let \( f \in \mathcal{L}\left( E\right) \) commute with all elements of \( Q \). Since the field \( \mathbb{C} \) is algebraically closed, \( f \) admits at least one eigenvalue \( \lambda \). Let \( {E}_{\lambda } \) be the corresponding eigenspace. We have \( {E}_{\lambda } \neq \{ 0\} \). By hypothesis on \( f \), for all \( g \in Q \), we have \( f \circ g = g \circ f \). According to Proposition 7 on page 175, \( {E}_{\lambda } \) is stable under all elements of \( Q \). Since \( {E}_{\lambda } \neq \{ 0\} \) and \( Q \) is irreducible, this implies \( {E}_{\lambda } = E \). Thus \( f = \lambda {\operatorname{Id}}_{E} \) is a homothety.

b) Sur un R-e.v, le résultat est faux dans le cas général. Par exemple, en dimension 2, l'ensemble \( Q \) des rotations (voir la remarque 1 page 269) est irréductible car aucune droite n’est stable par toutes les rotations. Or tous les éléments de \( Q \) commutent avec tous les éléments de \( Q \) . Il existe donc des éléments de \( \mathcal{L}\left( E\right) \) qui ne sont pas des homothéties qui commutent avec tous les éléments de \( Q \) .

> b) On an R-v.s., the result is false in the general case. For example, in dimension 2, the set \( Q \) of rotations (see remark 1 on page 269) is irreducible because no line is stable under all rotations. However, all elements of \( Q \) commute with all elements of \( Q \). There therefore exist elements of \( \mathcal{L}\left( E\right) \) that are not homotheties which commute with all elements of \( Q \).

Cependant, si \( n = \dim E \) est impair, le résultat reste vrai. En effet, soit \( f \in \mathcal{L}\left( E\right) \) commutant avec tous les éléments de \( Q \) . Le polynôme caractéristique \( {P}_{f} \) de \( f \) est un polynôme réel de degré impair, donc \( {P}_{f} \) admet au moins une racine réelle \( \lambda \) , donc \( f \) admet une valeur propre \( \lambda \) . En procédant comme au a), on en déduit que \( f \) est une homothétie.

> However, if \( n = \dim E \) is odd, the result remains true. Indeed, let \( f \in \mathcal{L}\left( E\right) \) commute with all elements of \( Q \). The characteristic polynomial \( {P}_{f} \) of \( f \) is a real polynomial of odd degree, so \( {P}_{f} \) admits at least one real root \( \lambda \), thus \( f \) admits an eigenvalue \( \lambda \). Proceeding as in a), we deduce that \( f \) is a homothety.

Remarque. On en déduit que sur un \( \mathbb{C} \) -espace vectoriel de dimension finie, les éléments commutant avec tout ceux de \( \mathcal{L}\left( E\right) \) sont les homothéties. Ce résultat est un cas particulier du résultat de l’exercice 6 page 124 dans le cas où \( \mathbb{K} = \mathbb{C} \) .

> Remark. We deduce that on a finite-dimensional \( \mathbb{C} \)-vector space, the elements commuting with all those of \( \mathcal{L}\left( E\right) \) are the homotheties. This result is a special case of the result of exercise 6 on page 124 in the case where \( \mathbb{K} = \mathbb{C} \).

EXERCICE 6. Soit \( \mathbb{K} \) un corps commutatif et \( A, B, C, D \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telles que \( {DC} = {CD} \) . Montrer que

> EXERCISE 6. Let \( \mathbb{K} \) be a commutative field and \( A, B, C, D \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) such that \( {DC} = {CD} \). Show that

\[
\det \left( \begin{array}{ll} A & B \\  C & D \end{array}\right)  = \det \left( {{AD} - {BC}}\right)
\]

a) si \( D \) est inversible,

> a) if \( D \) is invertible,

b) si K est de cardinal infini.

> b) if K has infinite cardinality.

Solution. a) On part de la relation

> Solution. a) We start from the relation

\[
\left( \begin{array}{ll} A & B \\  C & D \end{array}\right) \left( \begin{matrix} D & 0 \\   - C & {D}^{-1} \end{matrix}\right)  = \left( \begin{matrix} {AD} - {BC} & B{D}^{-1} \\  {CD} - {DC} & {I}_{n} \end{matrix}\right)  = \left( \begin{matrix} {AD} - {BC} & B{D}^{-1} \\  0 & {I}_{n} \end{matrix}\right) ,
\]

d'où l'égalité voulue en passant aux déterminants.

> whence the desired equality by passing to determinants.

b) Cette fois, \( D \) n’est pas supposée inversible. La matrice \( D \) n’ayant qu’un nombre fini de valeurs propres et \( \mathbb{K} \) étant infini, il existe une partie infinie \( \Gamma \) de \( \mathbb{K} \) telle que pour tout \( \lambda \in \Gamma , D - \lambda {I}_{n} \) soit inversible. D’après a), le polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) défini par

> b) This time, \( D \) is not assumed to be invertible. Since the matrix \( D \) has only a finite number of eigenvalues and \( \mathbb{K} \) is infinite, there exists an infinite subset \( \Gamma \) of \( \mathbb{K} \) such that for all \( \lambda \in \Gamma , D - \lambda {I}_{n} \) is invertible. According to a), the polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) defined by

\[
P\left( X\right)  = \det \left( \begin{matrix} A & B \\  C & D - X{I}_{n} \end{matrix}\right)  - \det \left\lbrack  {A\left( {D - X{I}_{n}}\right)  - {BC}}\right\rbrack
\]

s’annule sur tout \( \lambda \in \Gamma \) . Comme \( \Gamma \) est infini, \( P \) est nul et donc \( P\left( 0\right) = 0 \) , d’où le résultat.

> vanishes on all \( \lambda \in \Gamma \) . Since \( \Gamma \) is infinite, \( P \) is zero and thus \( P\left( 0\right) = 0 \) , whence the result.

Remarque. En fait, si \( \mathbb{K} \) est fini, le résultat reste vrai. En effet, \( \mathbb{K} \) se plonge dans un corps infini L (prendre par exemple pour \( \mathbb{L} \) le corps des fractions \( \mathbb{K}\left( X\right) \) ) et il suffit alors d’appliquer b) en remplaçant \( \mathbb{K} \) par \( \mathbb{L} \) .

> Remark. In fact, if \( \mathbb{K} \) is finite, the result remains true. Indeed, \( \mathbb{K} \) can be embedded into an infinite field L (take for example for \( \mathbb{L} \) the field of fractions \( \mathbb{K}\left( X\right) \) ) and it then suffices to apply b) by replacing \( \mathbb{K} \) with \( \mathbb{L} \) .

EXERCICE 7. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Si \( u, v \in \mathcal{L}\left( E\right) \) , on pose \( \left\lbrack {u, v}\right\rbrack = {uv} - {vu} \) (crochet de Lie de \( u \) et \( v \) ). Soient \( f \) et \( g \in \mathcal{L}\left( E\right) . \)

> EXERCISE 7. Let \( E \) be a finite-dimensional \( \mathbb{C} \) -v.s. \( n \in {\mathbb{N}}^{ * } \) . If \( u, v \in \mathcal{L}\left( E\right) \) , we define \( \left\lbrack {u, v}\right\rbrack = {uv} - {vu} \) (Lie bracket of \( u \) and \( v \) ). Let \( f \) and \( g \in \mathcal{L}\left( E\right) . \)

1/ On suppose qu’il existe \( \alpha \in {\mathbb{C}}^{ * } \) tel que \( \left\lbrack {f, g}\right\rbrack = {\alpha f} \) .

> 1/ Suppose there exists \( \alpha \in {\mathbb{C}}^{ * } \) such that \( \left\lbrack {f, g}\right\rbrack = {\alpha f} \) .

a) Montrer que \( f \) est nilpotente. (Indication. On pourra calculer \( \left\lbrack {{f}^{p}, g}\right\rbrack \) pour tout \( p \in {\mathbb{N}}^{ * } \) .) b) Montrer que \( f \) et \( g \) sont trigonalisables dans une même base.

> a) Show that \( f \) is nilpotent. (Hint. One may calculate \( \left\lbrack {{f}^{p}, g}\right\rbrack \) for all \( p \in {\mathbb{N}}^{ * } \) .) b) Show that \( f \) and \( g \) are simultaneously triangularizable.

2/ On suppose maintenant qu’il existe \( \alpha ,\beta \in {\mathbb{C}}^{ * } \) tels que \( \left\lbrack {f, g}\right\rbrack = {\alpha f} + {\beta g} \) . Montrer qu’également, \( f \) et \( g \) sont trigonalisables dans une même base.

> 2/ Now suppose there exist \( \alpha ,\beta \in {\mathbb{C}}^{ * } \) such that \( \left\lbrack {f, g}\right\rbrack = {\alpha f} + {\beta g} \) . Show that \( f \) and \( g \) are also simultaneously triangularizable.

Solution. 1/ a) Par récurrence sur \( p \in {\mathbb{N}}^{ * } \) , on obtient facilement \( \left\lbrack {{f}^{p}, g}\right\rbrack = {\alpha p}{f}^{p} \) . Comme l’endomorphisme de \( \mathcal{L}\left\lbrack {\mathcal{L}\left( E\right) }\right\rbrack \) défini par \( {L}_{g} : h \mapsto \left\lbrack {h, g}\right\rbrack \) n’a qu’un nombre fini de valeurs propres (on est en dimension finie) et que pour tout \( p \in {\mathbb{N}}^{ * },{L}_{g}\left( {f}^{p}\right) = {\alpha p}{f}^{p} \) avec \( \alpha \neq 0 \) , on en déduit qu’il existe \( p \in {\mathbb{N}}^{ * } \) tel que \( {f}^{p} = 0 \) .

> Solution. 1/ a) By induction on \( p \in {\mathbb{N}}^{ * } \) , we easily obtain \( \left\lbrack {{f}^{p}, g}\right\rbrack = {\alpha p}{f}^{p} \) . Since the endomorphism of \( \mathcal{L}\left\lbrack {\mathcal{L}\left( E\right) }\right\rbrack \) defined by \( {L}_{g} : h \mapsto \left\lbrack {h, g}\right\rbrack \) has only a finite number of eigenvalues (we are in finite dimension) and since for all \( p \in {\mathbb{N}}^{ * },{L}_{g}\left( {f}^{p}\right) = {\alpha p}{f}^{p} \) with \( \alpha \neq 0 \) , we deduce that there exists \( p \in {\mathbb{N}}^{ * } \) such that \( {f}^{p} = 0 \) .

b) Commençons par montrer que \( f \) et \( g \) ont un vecteur propre en commun. Le s.e.v Ker \( f \) est stable par \( g \) car

> b) Let us begin by showing that \( f \) and \( g \) have a common eigenvector. The subspace Ker \( f \) is stable under \( g \) because

\[
\forall x \in  \operatorname{Ker}f,\;f\left\lbrack  {g\left( x\right) }\right\rbrack   = g\left\lbrack  {f\left( x\right) }\right\rbrack   + {\alpha f}\left( x\right)  = 0.
\]

Or \( f \) étant nilpotente, on a Ker \( f \neq \{ 0\} \) . Le corps \( \mathbb{C} \) étant algébriquement clos, on en déduit que \( {g}_{\mid \operatorname{Ker}f} \) admet au moins un vecteur propre \( x \) . Le vecteur \( x \) est également propre pour \( f \) car \( x \in \operatorname{Ker}f \) .

> Since \( f \) is nilpotent, we have Ker \( f \neq \{ 0\} \) . As the field \( \mathbb{C} \) is algebraically closed, we deduce that \( {g}_{\mid \operatorname{Ker}f} \) admits at least one eigenvector \( x \) . The vector \( x \) is also an eigenvector for \( f \) because \( x \in \operatorname{Ker}f \) .

Ceci étant, montrons par récurrence sur \( n \in {\mathbb{N}}^{ * } \) que \( f \) et \( g \) sont trigonalisables dans une même base. Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Comme \( {fg} - {gf} = {\alpha f} \) , les applications transposées vérifient \( {}^{\mathrm{t}}{f}^{\mathrm{t}}g - {}^{\mathrm{t}}g{}^{\mathrm{t}}f = {\left( -\alpha \right) }^{\mathrm{t}}f \) . En appliquant le résultat précédent à \( {}^{\mathrm{t}}f \) et \( {}^{\mathrm{t}}g \) , on voit donc qu’il existe un vecteur propre \( x \in {E}^{ * } \) commun à \( {}^{\mathrm{t}}f \) et \( {}^{\mathrm{t}}g \) . L’orthogonal \( H \) de \( \mathbb{C}x \) dans \( E \) est donc un hyperplan stable par \( f \) et \( g \) . Or \( \left\lbrack {{f}_{\mid H},{g}_{\mid H}}\right\rbrack = \alpha {f}_{\mid H} \) , donc d’après l’hypothèse de récurrence il existe une base \( B \) de \( H \) dans laquelle \( {f}_{\mid H} \) et \( {g}_{\mid H} \) se trigonalisent. Soit \( e \in E \) tel que \( {B}^{\prime } = \left( {B, e}\right) \) soit une base de \( E \) . Alors

> This being said, let us show by induction on \( n \in {\mathbb{N}}^{ * } \) that \( f \) and \( g \) are simultaneously triangularizable. For \( n = 1 \) , it is obvious. Assume the result is true for rank \( n - 1 \) and show it for rank \( n \) . Since \( {fg} - {gf} = {\alpha f} \) , the transposed maps satisfy \( {}^{\mathrm{t}}{f}^{\mathrm{t}}g - {}^{\mathrm{t}}g{}^{\mathrm{t}}f = {\left( -\alpha \right) }^{\mathrm{t}}f \) . By applying the previous result to \( {}^{\mathrm{t}}f \) and \( {}^{\mathrm{t}}g \) , we see that there exists a common eigenvector \( x \in {E}^{ * } \) for \( {}^{\mathrm{t}}f \) and \( {}^{\mathrm{t}}g \) . The orthogonal \( H \) of \( \mathbb{C}x \) in \( E \) is therefore a hyperplane stable under \( f \) and \( g \) . Since \( \left\lbrack {{f}_{\mid H},{g}_{\mid H}}\right\rbrack = \alpha {f}_{\mid H} \) , by the induction hypothesis there exists a basis \( B \) of \( H \) in which \( {f}_{\mid H} \) and \( {g}_{\mid H} \) are triangularized. Let \( e \in E \) be such that \( {B}^{\prime } = \left( {B, e}\right) \) is a basis of \( E \) . Then

\[
{\left\lbrack  f\right\rbrack  }_{{B}^{\prime }} = \left( \begin{matrix}  & & & \\   & {\left\lbrack  {f}_{\mid H}\right\rbrack  }_{B} & & \vdots \\  0 & \cdots & 0 &  \times   \end{matrix}\right) ,
\]

donc la base \( B \) trigonalise \( f \) . On montrerait de même que la base \( B \) trigonalise \( g \) .

> therefore the basis \( B \) triangularizes \( f \) . We would show similarly that the basis \( B \) triangularizes \( g \) .

2/On pose \( {f}^{\prime } = f + \left( {\beta /\alpha }\right) g \) et on remarque que \( \left\lbrack {{f}^{\prime }, g}\right\rbrack = \alpha {f}^{\prime } \) . D’après \( 1/\mathrm{b}),{f}^{\prime } \) et \( g \) sont donc trigonalisables dans une même base. Il en est donc de même pour \( {f}^{\prime } - \left( {\beta /\alpha }\right) g = f \) et \( g \) .

> 2/ Let \( {f}^{\prime } = f + \left( {\beta /\alpha }\right) g \) and note that \( \left\lbrack {{f}^{\prime }, g}\right\rbrack = \alpha {f}^{\prime } \) . According to \( 1/\mathrm{b}),{f}^{\prime } \) and \( g \) are therefore simultaneously triangularizable. The same is true for \( {f}^{\prime } - \left( {\beta /\alpha }\right) g = f \) and \( g \) .
