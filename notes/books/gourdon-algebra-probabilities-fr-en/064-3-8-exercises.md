#### 3.8. Exercises

*Français : 3.8. Exercices*

EXERCICE 1 (MATRICES DIAGONALEMENT DOMINANTES). On considère une matrice \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) vérifiant

> EXERCISE 1 (DIAGONALLY DOMINANT MATRICES). Consider a matrix \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) satisfying

\[
\forall i,1 \leq  i \leq  n,\;\mathop{\sum }\limits_{\substack{{1 \leq  j \leq  n} \\  {j \neq  i} }}\left| {a}_{i, j}\right|  < \left| {a}_{i, i}\right| .
\]

Montrer que \( A \) est inversible.

> Show that \( A \) is invertible.

Solution. Il s’agit de montrer que rg \( A = n \) , c’est-à-dire que les \( n \) vecteurs colonnes de \( A \) forment une famille libre. Pour cela, raisonnons par l’absurde en supposant ces \( n \) vecteurs liés, ce qui s'écrit

> Solution. We must show that rg \( A = n \) , that is, the \( n \) column vectors of \( A \) form a linearly independent family. To do this, we reason by contradiction by assuming these \( n \) vectors are linearly dependent, which is written

\[
\exists {\lambda }_{1},\ldots ,{\lambda }_{n} \in  \mathbb{C}\text{ tels que }\forall i \in  \{ 1,\ldots , n\} ,\mathop{\sum }\limits_{{j = 1}}^{n}{\lambda }_{j}{a}_{i, j} = 0,
\]

les \( {\lambda }_{i} \) étant non tous nuls. Soit \( k \) tel que \( \left| {\lambda }_{k}\right| = \mathop{\sup }\limits_{{1 \leq j \leq n}}\left| {\lambda }_{j}\right| \) . Alors \( {\lambda }_{k} \neq 0 \) et

> the \( {\lambda }_{i} \) not all being zero. Let \( k \) be such that \( \left| {\lambda }_{k}\right| = \mathop{\sup }\limits_{{1 \leq j \leq n}}\left| {\lambda }_{j}\right| \) . Then \( {\lambda }_{k} \neq 0 \) and

\[
\mathop{\sum }\limits_{{j = 1}}^{n}{\lambda }_{j}{a}_{k, j} = 0\text{ donc }{a}_{k, k} =  - \mathop{\sum }\limits_{\substack{{1 \leq  j \leq  n} \\  {j \neq  k} }}\frac{{\lambda }_{j}}{{\lambda }_{k}}{a}_{k, j},\;\text{ d’où }\left| {a}_{k, k}\right|  \leq  \mathop{\sum }\limits_{\substack{{1 \leq  j \leq  n} \\  {j \neq  k} }}\frac{\left| {\lambda }_{j}\right| }{\left| {\lambda }_{k}\right| }\left| {a}_{k, j}\right|  \leq  \mathop{\sum }\limits_{\substack{{1 \leq  j \leq  n} \\  {j \neq  k} }}\left| {a}_{k, j}\right| ,
\]

ce qui est contraire aux hypothèses.

> which contradicts the hypotheses.

EXERCICE 2. Soit \( n \in {\mathbb{N}}^{ * } \) et soit la matrice

> EXERCISE 2. Let \( n \in {\mathbb{N}}^{ * } \) and let the matrix be

\[
M = \left( \begin{matrix} 1 & 1 & 1 & \cdots & 1 \\  0 & {C}_{1}^{1} & {C}_{2}^{1} & \cdots & {C}_{n}^{1} \\  \vdots &  \ddots  & {C}_{2}^{2} & \cdots & {C}_{n}^{2} \\  \vdots & &  \ddots  &  \ddots  & \vdots \\  0 & \cdots & \cdots & 0 & {C}_{n}^{n} \end{matrix}\right)  \in  {\mathcal{M}}_{n + 1}\left( \mathbb{R}\right) .
\]

Montrer que \( M \) est inversible et calculer \( {M}^{-1} \) .

> Show that \( M \) is invertible and calculate \( {M}^{-1} \) .

Solution. On note \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Soit l’endomorphisme \( f : {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \rightarrow \; {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \;P\left( X\right) \mapsto P\left( {X + 1}\right) \) . La famille \( B = \left( {1, X,\ldots ,{X}^{n}}\right) \) est une base de \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) , et on voit facilement que \( M \) est la matrice de \( f \) dans la base \( B \) . Or \( f \) est inversible, son inverse étant \( g : P\left( X\right) \mapsto P\left( {X - 1}\right) \) . Donc \( M \) est inversible, et

> Solution. Let \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Let the endomorphism be \( f : {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \rightarrow \; {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \;P\left( X\right) \mapsto P\left( {X + 1}\right) \) . The family \( B = \left( {1, X,\ldots ,{X}^{n}}\right) \) is a basis of \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) , and it is easy to see that \( M \) is the matrix of \( f \) in the basis \( B \) . Now \( f \) is invertible, its inverse being \( g : P\left( X\right) \mapsto P\left( {X - 1}\right) \) . Therefore \( M \) is invertible, and

\[
{M}^{-1} = {\left\lbrack  {f}^{-1}\right\rbrack  }_{B} = {\left\lbrack  g\right\rbrack  }_{B} = \left( \begin{matrix} 1 &  - 1 & 1 & \cdots & {\left( -1\right) }^{n} \\  0 & {C}_{1}^{1} &  - {C}_{2}^{1} & \cdots & {\left( -1\right) }^{n - 1}{C}_{n}^{1} \\  \vdots &  \ddots  & {C}_{2}^{2} & \cdots & {\left( -1\right) }^{n - 2}{C}_{n}^{2} \\  \vdots & &  \ddots  &  \ddots  & \vdots \\  0 & \cdots & \cdots & 0 & {C}_{n}^{n} \end{matrix}\right) .
\]

EXERCICE 3. Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telles que \( {AB} = A + B \) . Montrer que \( A \) et \( B \) commutent (i.e. montrer que \( {AB} = {BA} \) ).

> EXERCISE 3. Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be such that \( {AB} = A + B \) . Show that \( A \) and \( B \) commute (i.e. show that \( {AB} = {BA} \) ).

Solution. Comme \( {AB} = A + B \) , on a \( {I}_{n} - A - B + {AB} = {I}_{n} \) donc \( \left( {{I}_{n} - A}\right) \left( {{I}_{n} - B}\right) = {I}_{n} \) . Donc \( {I}_{n} - A \) est inversible, son inverse est \( \left( {{I}_{n} - B}\right) \) , donc \( \left( {{I}_{n} - B}\right) \left( {{I}_{n} - A}\right) = {I}_{n} \) , ce qui en développant donne \( {BA} = B + A = A + B \) .

> Solution. Since \( {AB} = A + B \) , we have \( {I}_{n} - A - B + {AB} = {I}_{n} \) therefore \( \left( {{I}_{n} - A}\right) \left( {{I}_{n} - B}\right) = {I}_{n} \) . Thus \( {I}_{n} - A \) is invertible, its inverse is \( \left( {{I}_{n} - B}\right) \) , so \( \left( {{I}_{n} - B}\right) \left( {{I}_{n} - A}\right) = {I}_{n} \) , which when expanded gives \( {BA} = B + A = A + B \) .

EXERCICE 4. a) On considère la matrice

> EXERCISE 4. a) Consider the matrix

\[
M = \left( \begin{matrix} 0 & {m}_{1,2} & \cdots & {m}_{1, n} \\  \vdots & 0 &  \ddots  & \vdots \\  \vdots & &  \ddots  & {m}_{n - 1, n} \\  0 & \cdots & \cdots & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) .
\]

Montrer (sans utiliser le théorème de Cayley-Hamilton) que \( M \) est nilpotente.

> Show (without using the Cayley-Hamilton theorem) that \( M \) is nilpotent.

b) Soit \( M = \left( \begin{array}{lll} 3 & 1 & 0 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{array}\right) \in {\mathcal{M}}_{3}\left( \mathbb{R}\right) \) . Pour tout entier \( p \geq 1 \) , calculer \( {M}^{p} \) .

> b) Let \( M = \left( \begin{array}{lll} 3 & 1 & 0 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{array}\right) \in {\mathcal{M}}_{3}\left( \mathbb{R}\right) \) . For any integer \( p \geq 1 \) , calculate \( {M}^{p} \) .

Solution. a) Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) la base canonique de \( {\mathbb{R}}^{n} \) ( \( {e}_{i} \) est le vecteur colonne dont tous les éléments sont nuls sauf le \( i \) -ième qui vaut 1). La forme de la matrice \( M \) montre que

> Solution. a) Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be the standard basis of \( {\mathbb{R}}^{n} \) ( \( {e}_{i} \) is the column vector where all elements are zero except the \( i \) -th which is 1). The form of matrix \( M \) shows that

\[
M{e}_{1} = 0\;\text{ et }\;\forall i \geq  2, M{e}_{i} = \mathop{\sum }\limits_{{k = 1}}^{{i - 1}}{m}_{k, i}{e}_{k} \in  \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{i - 1}}\right) .
\]

Montrons par récurrence sur \( p \in \{ 1,\ldots , n\} \) que pour tout \( i,1 \leq i \leq p \) , on a \( {M}^{p}{e}_{i} = 0 \) . Pour \( p = 1 \) c’est vrai car \( M{e}_{1} = 0 \) . Supposons le résultat vrai au rang \( p - 1 \) , montrons le au rang \( p \) . Si \( 1 \leq i \leq p - 1 \) , l’égalité \( {M}^{p - 1}{e}_{i} = 0 \) entraîne \( {M}^{p}{e}_{i} = 0 \) , et si \( i = p \) :

> Let us show by induction on \( p \in \{ 1,\ldots , n\} \) that for all \( i,1 \leq i \leq p \) , we have \( {M}^{p}{e}_{i} = 0 \) . For \( p = 1 \) it is true because \( M{e}_{1} = 0 \) . Assume the result is true at rank \( p - 1 \) , let us show it at rank \( p \) . If \( 1 \leq i \leq p - 1 \) , the equality \( {M}^{p - 1}{e}_{i} = 0 \) implies \( {M}^{p}{e}_{i} = 0 \) , and if \( i = p \) :

\[
{M}^{p}{e}_{p} = {M}^{p - 1}\left( {M{e}_{p}}\right)  = {M}^{p - 1}\left( {\mathop{\sum }\limits_{{k = 1}}^{{p - 1}}{m}_{k, p}{e}_{k}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{{p - 1}}{m}_{k, p}\left( {{M}^{p - 1}{e}_{k}}\right)  = 0.
\]

- En particulier, le résultat est vrai pour \( p = n \) ce qui entraîne que \( {M}^{n} \) s’annule sur tous les vecteurs de la base canonique de \( {\mathbb{R}}^{n} \) , donc est nul.

> - In particular, the result is true for \( p = n \) which implies that \( {M}^{n} \) vanishes on all vectors of the standard basis of \( {\mathbb{R}}^{n} \) , and is therefore zero.

b) On écrit \( M = 3{I}_{3} + N \) où \( N = \left( \begin{array}{lll} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array}\right) \) . D’après la question précédente, \( {N}^{3} = 0 \) .

> b) We write \( M = 3{I}_{3} + N \) where \( N = \left( \begin{array}{lll} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array}\right) \) . According to the previous question, \( {N}^{3} = 0 \) .

Comme \( {I}_{3} \) et \( N \) commutent, on peut écrire

> Since \( {I}_{3} \) and \( N \) commute, we can write

\[
\forall p \in  {\mathbb{N}}^{ * },{M}^{p} = \mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} p \\  k \end{array}\right) {N}^{k}{\left( 3{I}_{3}\right) }^{p - k} = {3}^{p}{I}_{3} + p{3}^{p - 1}N + \frac{p\left( {p - 1}\right) }{2}{3}^{p - 2}{N}^{2}.
\]

Comme \( N = \left( \begin{array}{lll} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array}\right) \) et \( {N}^{2} = \left( \begin{array}{lll} 0 & 0 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array}\right) \) , ceci donne \( {M}^{p} = {3}^{p - 2}\left( \begin{matrix} 9 & {3p} & p\left( {p - 1}\right) \\ 0 & 9 & {6p} \\ 0 & 0 & 9 \end{matrix}\right) \) .

> Since \( N = \left( \begin{array}{lll} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{array}\right) \) and \( {N}^{2} = \left( \begin{array}{lll} 0 & 0 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array}\right) \) , this gives \( {M}^{p} = {3}^{p - 2}\left( \begin{matrix} 9 & {3p} & p\left( {p - 1}\right) \\ 0 & 9 & {6p} \\ 0 & 0 & 9 \end{matrix}\right) \) .

Remarque. Au a), une étude plus poussée aurait permis de montrer que la matrice \( {M}^{p} \) a tout ses coefficients nuls en dehors de la partie triangulaire supérieure des \( n - p \) premières lignes et \( n - p \) dernières colonnes. Autrement dit,

> Remark. In a), a more in-depth study would have shown that matrix \( {M}^{p} \) has all its coefficients equal to zero outside the upper triangular part of the first \( n - p \) rows and last \( n - p \) columns. In other words,

\[
\forall p,1 \leq  p \leq  n - 1,\;\text{ on a }{M}^{p} = {\left. \left. \left( \begin{matrix}  \times  & \cdots &  \times  \\   &  \ddots  & \vdots \\  \left( 0\right) & &  \times  \\   & &  \end{matrix}\right) \right\}  \right\}  }_{p\text{ lignes }}.
\]

EXERCICE 5. Quelles sont les matrices \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telles que \( {A}^{2} = 0 \) ?

> EXERCISE 5. What are the matrices \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) such that \( {A}^{2} = 0 \)?

Solution. Soit \( f \) l’endomorphisme de \( {\mathbb{K}}^{n} \) dont \( A \) est la matrice dans la base canonique de \( {\mathbb{K}}^{n} \) . On a \( {f}^{2} = 0 \) , donc Im \( f \subset \operatorname{Ker}f \) . Soit \( r = \operatorname{rg}f \) . Si \( r = 0 \) , on a \( f = 0 \) . Sinon \( r \geq 1 \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) une base de Im \( f \) . Comme Im \( f \subset \operatorname{Ker}f \) , on peut compléter cette base en une base \( \left( {{e}_{1},\ldots ,{e}_{n - r}}\right) \) de Ker \( f \) (au passage, on remarque que \( r \leq n - r \) donc \( r \leq n/2 \) ). Pour \( 1 \leq i \leq r,{e}_{i} \in \operatorname{Im}f \) donc il existe \( {u}_{i} \in {\mathbb{K}}^{n} \) tel que \( f\left( {u}_{i}\right) = {e}_{i} \) .

> Solution. Let \( f \) be the endomorphism of \( {\mathbb{K}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{K}}^{n} \) is \( A \). We have \( {f}^{2} = 0 \), so Im \( f \subset \operatorname{Ker}f \). Let \( r = \operatorname{rg}f \). If \( r = 0 \), we have \( f = 0 \). Otherwise \( r \geq 1 \). Let \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) be a basis of Im \( f \). Since Im \( f \subset \operatorname{Ker}f \), we can complete this basis into a basis \( \left( {{e}_{1},\ldots ,{e}_{n - r}}\right) \) of Ker \( f \) (incidentally, we note that \( r \leq n - r \) so \( r \leq n/2 \)). For \( 1 \leq i \leq r,{e}_{i} \in \operatorname{Im}f \) so there exists \( {u}_{i} \in {\mathbb{K}}^{n} \) such that \( f\left( {u}_{i}\right) = {e}_{i} \).

Montrons que \( B = \left( {{e}_{1},\ldots ,{e}_{n - r},{u}_{1},\ldots ,{u}_{r}}\right) \) est une base de \( {\mathbb{K}}^{n} \) . Il suffit de montrer que c’est une famille libre (il y a \( n \) éléments). Supposons \( \left( {{\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n - r}{e}_{n - r}}\right) + \left( {{\mu }_{1}{u}_{1} + \cdots + {\mu }_{r}{u}_{r}}\right) = 0 \) où les \( {\lambda }_{i},{\mu }_{j} \in \mathbb{K} \) . En composant par \( f \) , on trouve \( {\mu }_{1}{e}_{1} + \cdots + {\mu }_{r}{e}_{r} = 0 \) , donc \( \forall i,{\mu }_{i} = 0 \) . Donc \( {\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n - r}{e}_{n - r} = 0 \) , et donc \( \forall i,{\lambda }_{i} = 0.B \) est donc bien une base de \( {\mathbb{K}}^{n} \) . Dans cette base, \( f \) a pour matrice \( {M}_{r} = \left( \begin{matrix} 0 & {I}_{r} \\ 0 & 0 \end{matrix}\right) \) , avec \( r \leq n/2 \) , et \( A \) est donc semblable à \( M \) .

> Let us show that \( B = \left( {{e}_{1},\ldots ,{e}_{n - r},{u}_{1},\ldots ,{u}_{r}}\right) \) is a basis of \( {\mathbb{K}}^{n} \). It suffices to show that it is a linearly independent family (there are \( n \) elements). Suppose \( \left( {{\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n - r}{e}_{n - r}}\right) + \left( {{\mu }_{1}{u}_{1} + \cdots + {\mu }_{r}{u}_{r}}\right) = 0 \) where the \( {\lambda }_{i},{\mu }_{j} \in \mathbb{K} \). By composing with \( f \), we find \( {\mu }_{1}{e}_{1} + \cdots + {\mu }_{r}{e}_{r} = 0 \), so \( \forall i,{\mu }_{i} = 0 \). Thus \( {\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n - r}{e}_{n - r} = 0 \), and therefore \( \forall i,{\lambda }_{i} = 0.B \) is indeed a basis of \( {\mathbb{K}}^{n} \). In this basis, \( f \) has the matrix \( {M}_{r} = \left( \begin{matrix} 0 & {I}_{r} \\ 0 & 0 \end{matrix}\right) \), with \( r \leq n/2 \), and \( A \) is therefore similar to \( M \).

Réciproquement, si \( {Au0} \) ou si \( A \) est semblable à \( {M}_{r} \) avec \( r \leq n/2 \) , alors \( {A}^{2} = 0 \) . Les matrices recherchées sont donc celles semblables à \( {M}_{r} \) avec \( r \leq n/2 \) et la matrice nulle.

> Conversely, if \( {Au0} \) or if \( A \) is similar to \( {M}_{r} \) with \( r \leq n/2 \), then \( {A}^{2} = 0 \). The matrices sought are therefore those similar to \( {M}_{r} \) with \( r \leq n/2 \) and the zero matrix.

EXERCICE 6. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice de trace nulle.

> EXERCISE 6. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a matrix with zero trace.

a) Montrer que \( M \) est semblable à une matrice n’ayant que des 0 sur la diagonale princi-pale.

> a) Show that \( M \) is similar to a matrix having only 0s on the main diagonal.

b) Montrer qu’il existe \( X \) et \( Y \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tels que \( M = {XY} - {YX} \) .

> b) Show that there exist \( X \) and \( Y \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that \( M = {XY} - {YX} \) .

Solution. a) On va montrer ce résultat par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) c’est évident car \( M = \left( {\operatorname{tr}M}\right) = \left( 0\right) \) . Supposons le résultat vérifié au rang \( n - 1 \) et montrons le au rang \( n \) . Soit \( f \) l’endomorphisme de \( {\mathbb{R}}^{n} \) dont \( M \) est la matrice dans la base canonique de \( {\mathbb{R}}^{n} \) . Si \( \forall x \in {\mathbb{R}}^{n} \) , la famille \( \left( {x, f\left( x\right) }\right) \) est liée, alors \( f \) est une homothétie (voir la proposition 3 de la partie 2.3), c’est-à-dire qu’il existe \( \lambda \in \mathbb{R} \) tel que \( f = \lambda {\operatorname{Id}}_{E} \) . Or \( {n\lambda } = \operatorname{tr}f = \operatorname{tr}M = 0 \) donc \( \lambda = 0 \) et donc \( f = 0 \) , ce qui entraîne que la matrice \( M \) est nulle.

> Solution. a) We will prove this result by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) it is obvious because \( M = \left( {\operatorname{tr}M}\right) = \left( 0\right) \) . Assume the result holds at rank \( n - 1 \) and show it at rank \( n \) . Let \( f \) be the endomorphism of \( {\mathbb{R}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{R}}^{n} \) is \( M \) . If \( \forall x \in {\mathbb{R}}^{n} \) , the family \( \left( {x, f\left( x\right) }\right) \) is linearly dependent, then \( f \) is a homothety (see proposition 3 of part 2.3), that is, there exists \( \lambda \in \mathbb{R} \) such that \( f = \lambda {\operatorname{Id}}_{E} \) . However, \( {n\lambda } = \operatorname{tr}f = \operatorname{tr}M = 0 \) therefore \( \lambda = 0 \) and thus \( f = 0 \) , which implies that the matrix \( M \) is zero.

Sinon, il existe \( x \in {\mathbb{R}}^{n} \) tel que la famille \( \left( {x, f\left( x\right) }\right) \) soit libre. Complétons cette famille en une base \( B = \left( {x, f\left( x\right) ,{e}_{3},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{R}}^{n} \) . Dans cette base, on a

> Otherwise, there exists \( x \in {\mathbb{R}}^{n} \) such that the family \( \left( {x, f\left( x\right) }\right) \) is linearly independent. Complete this family into a basis \( B = \left( {x, f\left( x\right) ,{e}_{3},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) . In this basis, we have

\[
N = {\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} 0 &  \times  & \cdots &  \times  \\  0 & & {N}^{\prime } & \\  0 & & {N}^{\prime } & \\  \vdots & & &  \end{matrix}\right) .
\]

Or \( 0 = \operatorname{tr}f = \operatorname{tr}N = \operatorname{tr}{N}^{\prime } \) donc d’après l’hypothèse de récurrence, il existe \( Q \in \mathcal{G}{\ell }_{n - 1}\left( \mathbb{R}\right) \) telle que \( {Q}^{-1}{N}^{\prime }Q \) n’ait que des zéros sur la diagonale principale. Si \( P = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & Q & \\ 0 & & & \end{matrix}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , on a donc

> However, \( 0 = \operatorname{tr}f = \operatorname{tr}N = \operatorname{tr}{N}^{\prime } \) therefore, according to the induction hypothesis, there exists \( Q \in \mathcal{G}{\ell }_{n - 1}\left( \mathbb{R}\right) \) such that \( {Q}^{-1}{N}^{\prime }Q \) has only zeros on the main diagonal. If \( P = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\ 0 & & & \\ \vdots & & Q & \\ 0 & & & \end{matrix}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , we then have

\[
{P}^{-1}{NP} = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & \left| {Q}^{-1}\right| & & N \\  \vdots & &  \ddots  &  \ddots  \\  0 & & & 0 \end{matrix}\right) N\left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & Q & \\  0 & & &  \end{matrix}\right)  = \left( \begin{matrix} 0 &  \times  & \cdots &  \times  \\   \times  & 0 &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\   \times  & \cdots &  \times  & 0 \end{matrix}\right)
\]

La matrice \( M \) , semblable à \( N \) , est donc semblable à cette dernière matrice, d’où le résultat.

> The matrix \( M \) , similar to \( N \) , is therefore similar to this latter matrix, hence the result.

b) D’après a), il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) telle que \( M = {P}^{-1}{NP} \) où \( N \) est une matrice n’ayant que des zéros sur la diagonale principale. Notons \( {b}_{i, j} \) les coefficients de la matrice \( N \) . Fixons

> b) According to a), there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that \( M = {P}^{-1}{NP} \) where \( N \) is a matrix having only zeros on the main diagonal. Let \( {b}_{i, j} \) denote the coefficients of the matrix \( N \) . Let us fix

\[
X = \left( \begin{matrix} {\alpha }_{1} & 0 & \cdots & 0 \\  0 & {\alpha }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & 0 \\  0 & \cdots & 0 & {\alpha }_{n} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\;\text{ avec }\;{\alpha }_{i} \neq  {\alpha }_{j}\;\text{ si }\;i \neq  j.
\]

Si \( Y = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , un calcul rapide montre que \( {XY} - {YX} = {\left( {\alpha }_{i}{a}_{i, j} - {\alpha }_{j}{a}_{i, j}\right) }_{1 \leq i, j \leq n} \) . En choisissant \( {a}_{i, i} = 0 \) pour tout \( i \) , et \( {a}_{i, j} = {b}_{i, j}/\left( {{\alpha }_{i} - {\alpha }_{j}}\right) \) si \( i \neq j \) , on voit que \( {XY} - {YX} = N \) , donc \( M = \left( {{P}^{-1}{XP}}\right) \left( {{P}^{-1}{YP}}\right) - \left( {{P}^{-1}{YP}}\right) \left( {{P}^{-1}{XP}}\right) \) .

> If \( Y = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , a quick calculation shows that \( {XY} - {YX} = {\left( {\alpha }_{i}{a}_{i, j} - {\alpha }_{j}{a}_{i, j}\right) }_{1 \leq i, j \leq n} \) . By choosing \( {a}_{i, i} = 0 \) for all \( i \) , and \( {a}_{i, j} = {b}_{i, j}/\left( {{\alpha }_{i} - {\alpha }_{j}}\right) \) if \( i \neq j \) , we see that \( {XY} - {YX} = N \) , therefore \( M = \left( {{P}^{-1}{XP}}\right) \left( {{P}^{-1}{YP}}\right) - \left( {{P}^{-1}{YP}}\right) \left( {{P}^{-1}{XP}}\right) \) .

EXERCICE 7. Soit \( E \) un \( \mathbb{R} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Soient \( {p}_{1},\ldots ,{p}_{k} \in \mathcal{L}\left( E\right) \) des projecteurs. Montrer que \( p = {p}_{1} + \cdots + {p}_{k} \) est un projecteur si et seulement si \( {p}_{i} \circ {p}_{j} = 0 \) pour tout \( \left( {i, j}\right) \) tel que \( i \neq j \) .

> EXERCISE 7. Let \( E \) be a finite-dimensional \( \mathbb{R} \) -vector space \( n \in {\mathbb{N}}^{ * } \) . Let \( {p}_{1},\ldots ,{p}_{k} \in \mathcal{L}\left( E\right) \) be projectors. Show that \( p = {p}_{1} + \cdots + {p}_{k} \) is a projector if and only if \( {p}_{i} \circ {p}_{j} = 0 \) for all \( \left( {i, j}\right) \) such that \( i \neq j \) .

Solution. Condition suffisante. Il suffit de remarquer que

> Solution. Sufficient condition. It suffices to note that

\[
{p}^{2} = {p}_{1}^{2} + \cdots  + {p}_{k}^{2} + \mathop{\sum }\limits_{{i \neq  j}}{p}_{i} \circ  {p}_{j} = {p}_{1}^{2} + \cdots  + {p}_{k}^{2} = {p}_{1} + \cdots  + {p}_{k} = p.
\]

Condition nécessaire. D'après la proposition 7, le rang d'un projecteur égale sa trace, donc

> Necessary condition. According to proposition 7, the rank of a projector equals its trace, so

\[
\operatorname{rg}p = \operatorname{tr}p = \mathop{\sum }\limits_{{i = 1}}^{k}\operatorname{tr}{p}_{i} = \mathop{\sum }\limits_{{i = 1}}^{k}\operatorname{rg}{p}_{i}.
\]

On a aussi

> We also have

\[
\operatorname{Im}p = \left( {{p}_{1} + \cdots  + {p}_{k}}\right) \left( E\right)  \subset  {p}_{1}\left( E\right)  + \cdots  + {p}_{k}\left( E\right)  = \operatorname{Im}{p}_{1} + \cdots  + \operatorname{Im}{p}_{k}.
\]

Ces deux dernières assertions permettent de conclure que

> These last two assertions allow us to conclude that

\[
\operatorname{Im}p = \operatorname{Im}{p}_{1} \oplus  \cdots  \oplus  \operatorname{Im}{p}_{k}.
\]

(*)

> Ceci étant, fixons \( i,1 \leq i \leq k \) . D’après \( \left( *\right) \) , si \( x \in E,{p}_{i}\left( x\right) \in \operatorname{Im}p \) donc

This being said, let us fix \( i,1 \leq i \leq k \) . According to \( \left( *\right) \) , if \( x \in E,{p}_{i}\left( x\right) \in \operatorname{Im}p \) therefore

\[
{p}_{i}\left( x\right)  = p\left( {{p}_{i}\left( x\right) }\right)  = {p}_{1} \circ  {p}_{i}\left( x\right)  + \cdots  + {p}_{i} \circ  {p}_{i}\left( x\right)  + \cdots  + {p}_{k} \circ  {p}_{i}\left( x\right) .
\]

Comme \( {p}_{i} \circ {p}_{i}\left( x\right) = {p}_{i}\left( x\right) \) , on en déduit \( \mathop{\sum }\limits_{{j \neq i}}{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) . Or pour tout \( j,{p}_{j} \circ {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{j} \) donc d’après \( \left( *\right) \) , l’écriture \( \mathop{\sum }\limits_{{j \neq i}}{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) entraîne \( \forall j \neq i,{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) . Ceci est vrai pour tout \( x \in E \) , donc si \( j \neq i,{p}_{j} \circ {p}_{i} = 0 \) , d’où le résultat.

> Since \( {p}_{i} \circ {p}_{i}\left( x\right) = {p}_{i}\left( x\right) \) , we deduce \( \mathop{\sum }\limits_{{j \neq i}}{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) . However, for all \( j,{p}_{j} \circ {p}_{i}\left( x\right) \in \operatorname{Im}{p}_{j} \) therefore according to \( \left( *\right) \) , the expression \( \mathop{\sum }\limits_{{j \neq i}}{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) implies \( \forall j \neq i,{p}_{j} \circ {p}_{i}\left( x\right) = 0 \) . This is true for all \( x \in E \) , so if \( j \neq i,{p}_{j} \circ {p}_{i} = 0 \) , hence the result.
