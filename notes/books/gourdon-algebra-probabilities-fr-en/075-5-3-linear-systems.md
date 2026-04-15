#### 5.3. Linear systems

*Français : 5.3. Systèmes linéaires*

On considère le système de \( p \) équations à \( q \) inconnues suivant :

> Consider the following system of \( p \) equations with \( q \) unknowns:

\[
\left\{  \begin{matrix} {a}_{1,1}{x}_{1} &  + & {a}_{1,2}{x}_{2} &  + & \cdots &  + & {a}_{1, q}{x}_{q} &  = {b}_{1} \\  {a}_{2,1}{x}_{1} &  + & {a}_{2,2}{x}_{2} &  + & \cdots &  + & {a}_{2, q}{x}_{q} &  = {b}_{2} \\  \cdots & & & & & \cdots & \cdots & \cdots \\  {a}_{p,1}{x}_{1} &  + & {a}_{p,2}{x}_{2} &  + & \cdots &  + & {a}_{p, q}{x}_{q} &  = {b}_{p} \end{matrix}\right. . \tag{S}
\]

Systèmes de Cramer. Supposons que dans le système (S), \( p = q = n \) . Posons \( A = \; {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , B \) la matrice colonne dont les composantes sont les \( {\left( {b}_{i}\right) }_{1 \leq i \leq n} \) et \( X \) la matrice colonne dont les composantes sont les \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) . Le système (S) s’écrit aussi \( {AX} = B \) , et on voit donc que (S) admet une unique solution \( X \) pour tout \( B \) si et seulement si det \( A \neq 0 \) . Dans ce cas, comme \( B = {x}_{1}{A}_{1} + \cdots + {x}_{n}{A}_{n} \) (les \( {A}_{i} \) désignant les vecteurs colonnes de la matrice \( A \) ), on a, \( {B}_{0} \) désignant la base canonique de \( {\mathbb{K}}^{n} \) ,

> Cramer systems. Suppose that in system (S), \( p = q = n \) . Let \( A = \; {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , B \) be the column matrix whose components are the \( {\left( {b}_{i}\right) }_{1 \leq i \leq n} \) and \( X \) be the column matrix whose components are the \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) . System (S) can also be written as \( {AX} = B \) , and we thus see that (S) admits a unique solution \( X \) for any \( B \) if and only if det \( A \neq 0 \) . In this case, since \( B = {x}_{1}{A}_{1} + \cdots + {x}_{n}{A}_{n} \) (the \( {A}_{i} \) denoting the column vectors of matrix \( A \) ), we have, with \( {B}_{0} \) denoting the canonical basis of \( {\mathbb{K}}^{n} \) ,

\[
\mathop{\det }\limits_{{B}_{0}}\left( {{A}_{1},\ldots ,{A}_{i - 1}, B,{A}_{i + 1},\ldots ,{A}_{n}}\right)  = {x}_{i}\mathop{\det }\limits_{{B}_{0}}\left( {{A}_{1},\ldots ,{A}_{n}}\right)  = {x}_{i}\det A.
\]

On en déduit que les composantes \( {x}_{i} \) de \( X \) sont données par

> We deduce that the components \( {x}_{i} \) of \( X \) are given by

\[
{x}_{i} = \frac{\mathop{\det }\limits_{{B}_{0}}\left( {{A}_{1},\ldots ,{A}_{i - 1}, B,{A}_{i + 1},\ldots ,{A}_{n}}\right) }{\det A}
\]

(formules connues sous le nom de formules de Cramer).

> (formulas known as Cramer's rules).

Cas général. On note \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . Soit \( r = \operatorname{rg}A \) . Il existe un déterminant \( \Delta \) d’ordre \( r \) non nul extrait de \( A \) (d’après le théorème 2 page 128). Ainsi choisi, \( \Delta \) s’appelle le déterminant principal du système (S) (il n'est en général pas unique).

> General case. Let \( A = {\left( {a}_{i, j}\right) }_{\begin{matrix} {1 \leq i \leq p} \\ {1 \leq j \leq q} \end{matrix}} \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) . Let \( r = \operatorname{rg}A \) . There exists a non-zero determinant \( \Delta \) of order \( r \) extracted from \( A \) (according to theorem 2 on page 128). Chosen this way, \( \Delta \) is called the principal determinant of system (S) (it is generally not unique).

- Les équations dont les indices sont ceux des lignes de \( \Delta \) s’appellent les équations principales.

> - The equations whose indices are those of the rows of \( \Delta \) are called the principal equations.

- Les inconnues dont les indices sont ceux des colonnes de \( \Delta \) s’appellent les inconnues principales.

> - The unknowns whose indices are those of the columns of \( \Delta \) are called the principal unknowns.

Notons \( I \) (resp. \( J \) ) les indices des lignes (resp. des colonnes) de \( \Delta \) , de sorte \( \Delta = \det {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) .

> Let \( I \) (resp. \( J \) ) be the indices of the rows (resp. columns) of \( \Delta \) , such that \( \Delta = \det {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) .

On appelle déterminants caractéristiques les déterminants d’ordre \( r + 1 \) de la forme

> We call characteristic determinants the determinants of order \( r + 1 \) of the form

\[
\left| \begin{matrix} {\left( {a}_{i, j}\right) }_{j \in  J} & {\left( {b}_{i}\right) }_{i \in  I} \\  {\left( {a}_{k, j}\right) }_{j \in  J} & {b}_{k} \end{matrix}\right| \;\text{ avec }\;k \notin  J.
\]

Les déterminants caractéristiques n’existent que si \( r < p \) , et il y en a alors \( p - r \) .

> Characteristic determinants only exist if \( r < p \) , and there are then \( p - r \) of them.

Avec les notations que nous venons d'introduire, on a le

> With the notations we have just introduced, we have the

THÉORÉME 4 (ROUCHÉ - FONTENÉ). Le système (S) admet des solutions si et seulement si \( p = r \) ou les \( p - r \) déterminants caractéristiques sont nuls. Le système est alors équivalent au système des équations principales, les inconnues principales étant déterminées par un système de Cramer à l'aide des inconnues non principales.

> THEOREM 4 (ROUCHÉ - FONTENÉ). System (S) admits solutions if and only if \( p = r \) or the \( p - r \) characteristic determinants are zero. The system is then equivalent to the system of principal equations, with the principal unknowns determined by a Cramer system using the non-principal unknowns.

Exemple 3. Soit le système (S) :

> Example 3. Let the system (S) be:

\[
\begin{cases} {x}_{1} + 2{x}_{2} - {x}_{3} + {x}_{4} &  = 1 \\  {x}_{1} &  - {x}_{3} - {x}_{4} = 1 \\   - {x}_{1} + {x}_{2} + {x}_{3} + 2{x}_{4} &  = m \end{cases}
\]

Ici on a

> Here we have

\[
A = \left( \begin{array}{rrrr} 1 & 2 &  - 1 & 1 \\  1 & 0 &  - 1 &  - 1 \\   - 1 & 1 & 1 & 2 \end{array}\right)
\]

Un calcul rapide montre que rg \( A = 2 \) . Nous choisissons le déterminant principal \( \left| \begin{array}{ll} 1 & 2 \\ 1 & 0 \end{array}\right| \) , issu de la matrice \( A \) en considérant ses deux premières lignes et ses deux premières colonnes. Il n'y a ici qu'un seul déterminant caractéristique, qui est

> A quick calculation shows that rg \( A = 2 \) . We choose the principal determinant \( \left| \begin{array}{ll} 1 & 2 \\ 1 & 0 \end{array}\right| \) , derived from matrix \( A \) by considering its first two rows and its first two columns. There is only one characteristic determinant here, which is

\[
\left| \begin{array}{rrr} 1 & 2 & 1 \\  1 & 0 & 1 \\   - 1 & 1 & m \end{array}\right|  =  - 2\left( {m + 1}\right)
\]

D'après le théorème de Rouché-Fontené, (S) admet des solutions si et seulement si \( m = \) -1, et dans ce cas, le système (S) est équivalent au système

> According to the Rouché-Fontené theorem, (S) has solutions if and only if \( m = \) -1, and in this case, the system (S) is equivalent to the system

\[
\left\{  {\begin{array}{l} {x}_{1} + 2{x}_{2} = 1 + {x}_{3} - {x}_{4} \\  {x}_{1} = 1 + {x}_{3} + {x}_{4} \end{array} \Leftrightarrow  \left\{  {\begin{array}{l} {x}_{1} = 1 + {x}_{3} + {x}_{4} \\  {x}_{2} =  - {x}_{4} \end{array}.}\right. }\right.
\]
