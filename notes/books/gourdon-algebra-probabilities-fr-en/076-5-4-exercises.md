#### 5.4. Exercises

*Français : 5.4. Exercices*

Il existe plusieurs déterminants classiques qu'il faut savoir calculer. Les méthodes de calcul sont parfois astucieuses; faites donc les exercices pour les connaître.

> There are several classic determinants that one must know how to calculate. Calculation methods are sometimes clever; therefore, do the exercises to learn them.

EXERCICE 1. Soit \( n \geq 2 \) un entier. Pour tout \( k,1 \leq k \leq n - 1 \) , on considère un polynôme \( {P}_{k} = {X}^{k} + {a}_{k,1}{X}^{k - 1} + \cdots + {a}_{k, k} \in \mathbb{R}\left\lbrack X\right\rbrack \) . Si \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{R} \) , calculer le déterminant

> EXERCISE 1. Let \( n \geq 2 \) be an integer. For any \( k,1 \leq k \leq n - 1 \) , consider a polynomial \( {P}_{k} = {X}^{k} + {a}_{k,1}{X}^{k - 1} + \cdots + {a}_{k, k} \in \mathbb{R}\left\lbrack X\right\rbrack \) . If \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{R} \) , calculate the determinant

\[
\Delta  = \left| \begin{matrix} 1 & {P}_{1}\left( {x}_{1}\right) & \cdots & {P}_{n - 1}\left( {x}_{1}\right) \\  1 & {P}_{1}\left( {x}_{2}\right) & \cdots & {P}_{n - 1}\left( {x}_{2}\right) \\  \vdots & \vdots & & \vdots \\  1 & {P}_{1}\left( {x}_{n}\right) & \cdots & {P}_{n - 1}\left( {x}_{n}\right)  \end{matrix}\right| .
\]

Solution. Après avoir retranché \( {a}_{1,1} \) fois la première colonne à la deuxième, on obtient

> Solution. After subtracting \( {a}_{1,1} \) times the first column from the second, we obtain

\[
\Delta  = \left| \begin{matrix} 1 & {x}_{1} & {P}_{2}\left( {x}_{1}\right) & \cdots & {P}_{n - 1}\left( {x}_{1}\right) \\  1 & {x}_{2} & {P}_{2}\left( {x}_{2}\right) & \cdots & {P}_{n - 1}\left( {x}_{2}\right) \\  \vdots & \vdots & \vdots & & \vdots \\  1 & {x}_{n} & {P}_{2}\left( {x}_{n}\right) & \cdots & {P}_{n - 1}\left( {x}_{n}\right)  \end{matrix}\right| .
\]

On retranche ensuite à la troisième colonne \( {a}_{2,2} \) fois la première et \( {a}_{2,1} \) fois la deuxième, et on remarque que la troisième colonne n’est plus composée que de \( {x}_{i}^{2} \) . On recommence ainsi jusqu’à parvenir à la dernière colonne, et on obtient finalement une expression en fonction du déterminant de Vandermonde

> We then subtract \( {a}_{2,2} \) times the first column and \( {a}_{2,1} \) times the second from the third column, and notice that the third column is now composed only of \( {x}_{i}^{2} \) . We repeat this process until reaching the last column, and finally obtain an expression in terms of the Vandermonde determinant

\[
\Delta  = \left| \begin{matrix} 1 & {x}_{1} & \cdots & {x}_{1}^{n - 1} \\  1 & {x}_{2} & \cdots & {x}_{2}^{n - 1} \\  \vdots & \vdots & & \vdots \\  1 & {x}_{n} & \cdots & {x}_{n}^{n - 1} \end{matrix}\right|  = V\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{x}_{j} - {x}_{i}}\right) .
\]

EXERCICE 2. Soient \( a, b \in \mathbb{K} \) et \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{K} \) . On définit le déterminant d’ordre \( n \)

> EXERCISE 2. Let \( a, b \in \mathbb{K} \) and \( {x}_{1},\ldots ,{x}_{n} \in \mathbb{K} \) . We define the determinant of order \( n \)

\[
{\Delta }_{n} = \left| \begin{matrix} {x}_{1} & a & \cdots & a \\  b & {x}_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & a \\  b & \cdots & b & {x}_{n} \end{matrix}\right| .
\]

a) Si \( a \neq b \) , calculer \( {\Delta }_{n} \) . (Indication : on pourra considérer le déterminant \( {\Delta }_{n}\left( x\right) \) obtenu à partir de \( {\Delta }_{n} \) en ajoutant \( x \) à chaque terme, et montrer que \( {\Delta }_{n}\left( x\right) \) peut se mettre sous la forme \( {Ax} + B \) .)

> a) If \( a \neq b \) , calculate \( {\Delta }_{n} \) . (Hint: one may consider the determinant \( {\Delta }_{n}\left( x\right) \) obtained from \( {\Delta }_{n} \) by adding \( x \) to each term, and show that \( {\Delta }_{n}\left( x\right) \) can be written in the form \( {Ax} + B \) .)

b) On suppose ici que \( \mathbb{K} = \mathbb{R} \) . Calculer \( {\Delta }_{n} \) si \( a = b \) .

> b) We assume here that \( \mathbb{K} = \mathbb{R} \) . Calculate \( {\Delta }_{n} \) if \( a = b \) .

c) Si \( a = b \) et \( \mathbb{K} \) est quelconque, calculer \( {\Delta }_{n} \) . Solution. a) Suivons l'indication et considérons, pour tout \( x \in \mathbb{K} \) , le déterminant

> c) If \( a = b \) and \( \mathbb{K} \) is arbitrary, calculate \( {\Delta }_{n} \) . Solution. a) Let us follow the hint and consider, for any \( x \in \mathbb{K} \) , the determinant

\[
{\Delta }_{n}\left( x\right)  = \left| \begin{matrix} {x}_{1} + x & a + x & \cdots & a + x \\  b + x & {x}_{2} + x &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & a + x \\  b + x & \cdots & b + x & {x}_{n} + x \end{matrix}\right| .
\]

En retranchant aux \( n - 1 \) premières colonnes la dernière, puis en développant par rapport à la dernière colonne, on voit qu’il existe \( A, B \in \mathbb{K} \) tels que pour tout \( x \in \mathbb{K},{\Delta }_{n}\left( x\right) = {Ax} + B \) . On remarque maintenant que \( {\Delta }_{n}\left( {-b}\right) \) est le déterminant d’une matrice triangulaire supérieure dont les coefficients diagonaux sont les \( {x}_{i} - b \) , donc \( {\Delta }_{n}\left( {-b}\right) = \left( {{x}_{1} - b}\right) \cdots \left( {{x}_{n} - b}\right) = - {Ab} + B \) . On obtient de même \( {\Delta }_{n}\left( {-a}\right) = \left( {{x}_{1} - a}\right) \cdots \left( {{x}_{n} - a}\right) = - {Aa} + B \) . De ces deux valeurs, on en déduit

> By subtracting the last column from the first \( n - 1 \) columns, then expanding with respect to the last column, we see that there exist \( A, B \in \mathbb{K} \) such that for any \( x \in \mathbb{K},{\Delta }_{n}\left( x\right) = {Ax} + B \) . We now note that \( {\Delta }_{n}\left( {-b}\right) \) is the determinant of an upper triangular matrix whose diagonal coefficients are the \( {x}_{i} - b \) , so \( {\Delta }_{n}\left( {-b}\right) = \left( {{x}_{1} - b}\right) \cdots \left( {{x}_{n} - b}\right) = - {Ab} + B \) . We obtain \( {\Delta }_{n}\left( {-a}\right) = \left( {{x}_{1} - a}\right) \cdots \left( {{x}_{n} - a}\right) = - {Aa} + B \) in the same way. From these two values, we deduce

\[
{\Delta }_{n} = B = \frac{b\mathop{\prod }\limits_{i}\left( {{x}_{i} - a}\right)  - a\mathop{\prod }\limits_{i}\left( {{x}_{i} - b}\right) }{b - a}.
\]

b) On fixe \( a \in \mathbb{R} \) , et on regarde \( {\Delta }_{n} \) comme une fonction de \( b \) que nous notons \( f\left( b\right) \) . L’expression d’un déterminant d’une matrice en fonction de ses coefficients montre que la fonction \( b \mapsto f\left( b\right) \) est continue sur \( \mathbb{R} \) . Maintenant, on a vu au a) que si \( b \neq a \) , alors

> b) We fix \( a \in \mathbb{R} \), and we view \( {\Delta }_{n} \) as a function of \( b \) which we denote by \( f\left( b\right) \). The expression of a matrix determinant in terms of its coefficients shows that the function \( b \mapsto f\left( b\right) \) is continuous on \( \mathbb{R} \). Now, we saw in a) that if \( b \neq a \), then

\[
f\left( b\right)  = \frac{{bP}\left( a\right)  - {aP}\left( b\right) }{b - a}\text{ où }P\left( x\right)  = \mathop{\prod }\limits_{i}\left( {{x}_{i} - x}\right) .
\]

Autrement dit, si \( Q\left( x\right) = {xP}\left( a\right) - {aP}\left( x\right) \) , on a \( f\left( b\right) = \frac{Q\left( b\right) - Q\left( a\right) }{b - a} \) . En faisant tendre \( b \) vers \( a \) , la continuité de \( f \) permet donc d’affirmer que

> In other words, if \( Q\left( x\right) = {xP}\left( a\right) - {aP}\left( x\right) \), we have \( f\left( b\right) = \frac{Q\left( b\right) - Q\left( a\right) }{b - a} \). By letting \( b \) approach \( a \), the continuity of \( f \) allows us to assert that

\[
{\Delta }_{n} = f\left( a\right)  = {Q}^{\prime }\left( a\right)  = P\left( a\right)  - a{P}^{\prime }\left( a\right)  = \mathop{\prod }\limits_{i}\left( {{x}_{i} - a}\right)  + a\left( {\mathop{\sum }\limits_{i}\mathop{\prod }\limits_{{j \neq  i}}\left( {{x}_{j} - a}\right) }\right) .
\]

(*)

> c) Ici on ne peut pas utiliser la méthode précédente. Donnons deux méthodes de résolution. La première méthode s’appuie sur les résultats précédents. Elle consiste, dans \( {\Delta }_{n} \) ,à substituer à \( b \) l’indéterminée \( X \) , donnant ainsi un déterminant que nous notons \( D \) . Le déterminant \( D \) a ses coefficients dans le corps \( \mathbb{K}\left( X\right) \) , et d’après a) (puisque \( X \) et \( a \) sont différents dans \( \mathbb{K}\left( X\right) \) ) :

c) Here we cannot use the previous method. Let us provide two methods of resolution. The first method relies on the previous results. It consists, in \( {\Delta }_{n} \), of substituting the indeterminate \( X \) for \( b \), thus giving a determinant that we denote by \( D \). The determinant \( D \) has its coefficients in the field \( \mathbb{K}\left( X\right) \), and according to a) (since \( X \) and \( a \) are different in \( \mathbb{K}\left( X\right) \)):

\[
D = \frac{{XP}\left( a\right)  - {aP}\left( X\right) }{X - a}\text{ où }P = \mathop{\prod }\limits_{i}\left( {{x}_{i} - X}\right)  \in  \mathbb{K}\left\lbrack  X\right\rbrack  .
\]

Posons \( Q\left( X\right) = {XP}\left( a\right) - {aP}\left( X\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) . Comme \( Q\left( a\right) = 0 \) , il existe \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( Q\left( X\right) = \; \left( {X - a}\right) R\left( X\right) \) , de sorte que \( D = R\left( X\right) \) . Par dérivation, on obtient \( {Q}^{\prime }\left( X\right) = R\left( X\right) + \left( {X - a}\right) {R}^{\prime }\left( X\right) \) , donc \( {Q}^{\prime }\left( a\right) = R\left( a\right) \) . Il ne reste plus qu’a substituer à \( X \) la constante \( a \) , ce qui entraîne \( {\Delta }_{n} = \; R\left( a\right) = {Q}^{\prime }\left( a\right) = P\left( a\right) - a{P}^{\prime }\left( a\right) \) , ce qui permet de retrouver l’expression (*).

> Let us set \( Q\left( X\right) = {XP}\left( a\right) - {aP}\left( X\right) \in \mathbb{K}\left\lbrack X\right\rbrack \). Since \( Q\left( a\right) = 0 \), there exists \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( Q\left( X\right) = \; \left( {X - a}\right) R\left( X\right) \), so that \( D = R\left( X\right) \). By differentiation, we obtain \( {Q}^{\prime }\left( X\right) = R\left( X\right) + \left( {X - a}\right) {R}^{\prime }\left( X\right) \), therefore \( {Q}^{\prime }\left( a\right) = R\left( a\right) \). It only remains to substitute the constant \( a \) for \( X \), which leads to \( {\Delta }_{n} = \; R\left( a\right) = {Q}^{\prime }\left( a\right) = P\left( a\right) - a{P}^{\prime }\left( a\right) \), allowing us to recover the expression (*).

Nous proposons une deuxième méthode, plus directe. Notons \( A \) le vecteur colonne constitué uniquement de \( a,\left( {{E}_{1},\ldots ,{E}_{n}}\right) \) la base canonique de \( {\mathbb{K}}^{n} \) , et \( {\alpha }_{k} = {x}_{k} - a \) . On a

> We propose a second, more direct method. Let \( A \) be the column vector consisting only of \( a,\left( {{E}_{1},\ldots ,{E}_{n}}\right) \) the canonical basis of \( {\mathbb{K}}^{n} \), and \( {\alpha }_{k} = {x}_{k} - a \). We have

\[
{\Delta }_{n} = \det \left( {A + {\alpha }_{1}{E}_{1},\ldots , A + {\alpha }_{n}{E}_{n}}\right)
\]

\[
= \det \left( {{\alpha }_{1}{E}_{1},\ldots ,{\alpha }_{n}{E}_{n}}\right)  + \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{\alpha }_{1}{E}_{1},\ldots ,{\alpha }_{i - 1}{E}_{i - 1}, A,{\alpha }_{i + 1}{E}_{i + 1},\ldots ,{\alpha }_{n}{E}_{n}}\right)
\]

\[
= {\alpha }_{1}\cdots {\alpha }_{n} + \mathop{\sum }\limits_{{i = 1}}^{n}{\alpha }_{1}\cdots {\alpha }_{i - 1}a{\alpha }_{i + 1}\cdots {\alpha }_{n}.
\]

Le passage à la deuxième ligne est obtenu par multilinearité du déterminant, en utilisant le fait que lorsque le vecteur colonne \( A \) apparait deux fois, le déterminant correspondant est nul. On en déduit le résultat (*) compte tenu de la valeur des \( {\alpha }_{i} \) .

> The transition to the second line is obtained by multilinearity of the determinant, using the fact that when the column vector \( A \) appears twice, the corresponding determinant is zero. We deduce the result (*) taking into account the value of the \( {\alpha }_{i} \).

EXERCICE 3. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) (i.e. une matrice à coefficients dans \( \mathbb{Z} \) ). Donner une condition nécessaire et suffisante pour que \( M \) soit inversible et que \( {M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) .

> EXERCISE 3. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) (i.e., a matrix with coefficients in \( \mathbb{Z} \)). Give a necessary and sufficient condition for \( M \) to be invertible and for \( {M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \).

Solution. Nous allons montrer que \( \left( {M\text{ est inversible et }{M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) }\right) \) si et seulement si (det \( M = \pm 1 \) ).

> Solution. We will show that \( \left( {M\text{ est inversible et }{M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) }\right) \) if and only if (det \( M = \pm 1 \) ).

Condition nécessaire. On a \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) donc \( \det \left( M\right) \in \mathbb{Z} \) . De même, \( {M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) donc \( \det \left( {M}^{-1}\right) = 1/\det \left( M\right) \in \mathbb{Z} \) . Ainsi, \( \det \left( M\right) \) est un entier d’inverse entier, d’où \( \det \left( M\right) = \pm 1 \) .

> Necessary condition. We have \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) so \( \det \left( M\right) \in \mathbb{Z} \) . Similarly, \( {M}^{-1} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) so \( \det \left( {M}^{-1}\right) = 1/\det \left( M\right) \in \mathbb{Z} \) . Thus, \( \det \left( M\right) \) is an integer with an integer inverse, hence \( \det \left( M\right) = \pm 1 \) .

Condition suffisante. On a \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) donc les cofacteurs de \( M \) sont des entiers, donc la comatrice \( \widetilde{M} \) de \( M \) vérifie \( \widetilde{M} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) . Or \( \det \left( M\right) = \pm 1 \) donc \( 1/\det \left( M\right) \in \mathbb{Z} \) . Donc \( M \) est inversible et :

> Sufficient condition. We have \( M \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) so the cofactors of \( M \) are integers, therefore the comatrix \( \widetilde{M} \) of \( M \) satisfies \( \widetilde{M} \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) . However, \( \det \left( M\right) = \pm 1 \) so \( 1/\det \left( M\right) \in \mathbb{Z} \) . Thus \( M \) is invertible and:

\[
{M}^{-1} = \frac{1}{\det \left( M\right) }{}^{\mathrm{t}}\widetilde{M} \in  {\mathcal{M}}_{n}\left( \mathbb{Z}\right) .
\]

EXERCICE 4. a) Soient \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) et \( {\beta }_{1},\ldots ,{\beta }_{n} \in \mathbb{R} \) . On note \( M \) la matrice

> EXERCISE 4. a) Let \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) and \( {\beta }_{1},\ldots ,{\beta }_{n} \in \mathbb{R} \) . Let \( M \) be the matrix

\[
M = \left( \begin{matrix} {\left( {\alpha }_{1} + {\beta }_{1}\right) }^{n - 1} & {\left( {\alpha }_{1} + {\beta }_{2}\right) }^{n - 1} & \cdots & {\left( {\alpha }_{1} + {\beta }_{n}\right) }^{n - 1} \\  {\left( {\alpha }_{2} + {\beta }_{1}\right) }^{n - 1} & {\left( {\alpha }_{2} + {\beta }_{2}\right) }^{n - 1} & \cdots & {\left( {\alpha }_{2} + {\beta }_{n}\right) }^{n - 1} \\  \vdots & \vdots & & \vdots \\  {\left( {\alpha }_{n} + {\beta }_{1}\right) }^{n - 1} & {\left( {\alpha }_{n} + {\beta }_{2}\right) }^{n - 1} & \cdots & {\left( {\alpha }_{n} + {\beta }_{n}\right) }^{n - 1} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) .
\]

Calculer le déterminant de \( M \) .

> Calculate the determinant of \( M \) .

b) Soit \( p \in \mathbb{N} \) et un entier \( n \) tel que \( n \geq p + 1 \) . Calculer \( \Delta = \det A \) où \( A \) est la matrice

> b) Let \( p \in \mathbb{N} \) and an integer \( n \) such that \( n \geq p + 1 \) . Calculate \( \Delta = \det A \) where \( A \) is the matrix

\[
A = \left( \begin{matrix} 1 & {2}^{p} & \cdots & {n}^{p} \\  {2}^{p} & {3}^{p} & \cdots & {\left( n + 1\right) }^{p} \\  \vdots & \vdots & & \vdots \\  {n}^{p} & {\left( n + 1\right) }^{p} & \cdots & {\left( 2n - 1\right) }^{p} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) .
\]

Solution. a) L’astuce est d’écrire \( M \) comme le produit de deux matrices. Si \( {m}_{i, j} \) désigne l’élément d’indice \( \left( {i, j}\right) \) dans la matrice \( M \) , on a

> Solution. a) The trick is to write \( M \) as the product of two matrices. If \( {m}_{i, j} \) denotes the element with index \( \left( {i, j}\right) \) in matrix \( M \) , we have

\[
{m}_{i, j} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{C}_{n - 1}^{k}{\alpha }_{i}^{k}{\beta }_{j}^{n - 1 - k} = \mathop{\sum }\limits_{{k = 1}}^{n}{p}_{i, k}{q}_{k, j}
\]

(*)

> où \( {p}_{i, k} = {C}_{n - 1}^{k - 1}{\alpha }_{i}^{k - 1} \) et \( {q}_{k, j} = {\beta }_{j}^{n - k} \) . En d’autres termes, si \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et \( Q = {\left( {q}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , la relation (*) s’écrit \( M = {PQ} \) . On a donc det \( M = \det P \cdot \det Q \) . Or le déterminant de \( P \) vaut

where \( {p}_{i, k} = {C}_{n - 1}^{k - 1}{\alpha }_{i}^{k - 1} \) and \( {q}_{k, j} = {\beta }_{j}^{n - k} \) . In other words, if \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and \( Q = {\left( {q}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , the relation (*) is written \( M = {PQ} \) . We therefore have det \( M = \det P \cdot \det Q \) . However, the determinant of \( P \) is equal to

\[
\left| \begin{matrix} {C}_{n - 1}^{0} & {C}_{n - 1}^{1}{\alpha }_{1} & \cdots & {C}_{n - 1}^{n - 1}{\alpha }_{1}^{n - 1} \\  {C}_{n - 1}^{0} & {C}_{n - 1}^{1}{\alpha }_{2} & \cdots & {C}_{n - 1}^{n - 1}{\alpha }_{2}^{n - 1} \\  \vdots & \vdots & & \vdots \\  {C}_{n - 1}^{0} & {C}_{n - 1}^{1}{\alpha }_{n} & \cdots & {C}_{n - 1}^{n - 1}{\alpha }_{n}^{n - 1} \end{matrix}\right|  = {C}_{n - 1}^{0}{C}_{n - 1}^{1}\cdots {C}_{n - 1}^{n - 1}\left| \begin{matrix} 1 & {\alpha }_{1} & \cdots & {\alpha }_{1}^{n - 1} \\  1 & {\alpha }_{2} & \cdots & {\alpha }_{2}^{n - 1} \\  \vdots & \vdots & & \vdots \\  1 & {\alpha }_{n} & \cdots & {\alpha }_{n}^{n - 1} \end{matrix}\right| ,
\]

donc \( \det P = {C}_{n - 1}^{0}\cdots {C}_{n - 1}^{n - 1}\mathop{\prod }\limits_{{i < j}}\left( {{\alpha }_{j} - {\alpha }_{i}}\right) \) . Par ailleurs,

> so \( \det P = {C}_{n - 1}^{0}\cdots {C}_{n - 1}^{n - 1}\mathop{\prod }\limits_{{i < j}}\left( {{\alpha }_{j} - {\alpha }_{i}}\right) \) . Furthermore,

\[
\det Q = \left| \begin{matrix} {\beta }_{1}^{n - 1} & \cdots & {\beta }_{n}^{n - 1} \\  \vdots & & \vdots \\  {\beta }_{1} & \cdots & {\beta }_{n} \\  1 & \cdots & 1 \end{matrix}\right|  = {\left( -1\right) }^{n\left( {n - 1}\right) /2}\left| \begin{matrix} 1 & \cdots & 1 \\  {\beta }_{1} & \cdots & {\beta }_{n} \\  \vdots & & \vdots \\  {\beta }_{1}^{n - 1} & \cdots & {\beta }_{n}^{n - 1} \end{matrix}\right|
\]

(cette dernière égalité s’obtient en effectuant \( \left( {n - 1}\right) + \cdots + 2 + 1 = n\left( {n - 1}\right) /2 \) transpositions sur les lignes), donc det \( Q = {\left( -1\right) }^{n\left( {n - 1}\right) /2}\mathop{\prod }\limits_{{i < j}}\left( {{\beta }_{j} - {\beta }_{i}}\right) \) .

> (this last equality is obtained by performing \( \left( {n - 1}\right) + \cdots + 2 + 1 = n\left( {n - 1}\right) /2 \) transpositions on the rows), therefore det \( Q = {\left( -1\right) }^{n\left( {n - 1}\right) /2}\mathop{\prod }\limits_{{i < j}}\left( {{\beta }_{j} - {\beta }_{i}}\right) \) .

On a donc

> We therefore have

\[
\det M = \det P \cdot  \det Q = \left( {\mathop{\prod }\limits_{{i = 0}}^{{n - 1}}{C}_{n - 1}^{i}}\right) {\left( -1\right) }^{n\left( {n - 1}\right) /2}\mathop{\prod }\limits_{{i < j}}\left\lbrack  {\left( {{\alpha }_{j} - {\alpha }_{i}}\right) \left( {{\beta }_{j} - {\beta }_{i}}\right) }\right\rbrack  .
\]

b) Si \( p + 1 = n \) , alors d’après la question précédente appliquée à la matrice \( M \) avec \( {\alpha }_{i} = i \) et \( {\beta }_{j} = j - 1 \) , on a

> b) If \( p + 1 = n \) , then according to the previous question applied to the matrix \( M \) with \( {\alpha }_{i} = i \) and \( {\beta }_{j} = j - 1 \) , we have

\[
\det A = \left( {\mathop{\prod }\limits_{{i = 0}}^{{n - 1}}{C}_{n - 1}^{i}}\right) {\left( -1\right) }^{n\left( {n - 1}\right) /2}\mathop{\prod }\limits_{{i < j}}\left\lbrack  {\left( j - i\right) }^{2}\right\rbrack  .
\]

Or

\[
\mathop{\prod }\limits_{{i < j}}\left( {j - i}\right)  = \mathop{\prod }\limits_{{j = 2}}^{n}\left\lbrack  {\mathop{\prod }\limits_{{i = 1}}^{{j - 1}}\left( {j - i}\right) }\right\rbrack   = \mathop{\prod }\limits_{{j = 2}}^{n}\left( {j - 1}\right) ! = \mathop{\prod }\limits_{{j = 1}}^{{n - 1}}j!
\]

et

\[
\left( {\mathop{\prod }\limits_{{i = 0}}^{{n - 1}}{C}_{n - 1}^{i}}\right)  = \mathop{\prod }\limits_{{i = 0}}^{{n - 1}}\left\lbrack  \frac{\left( {n - 1}\right) !}{i!\left( {n - 1 - i}\right) !}\right\rbrack   = \frac{{\left\lbrack  \left( n - 1\right) !\right\rbrack  }^{n}}{{\left( \mathop{\prod }\limits_{{i = 1}}^{{n - 1}}i!\right) }^{2}},
\]

donc finalement \( \Delta = {\left( -1\right) }^{n\left( {n - 1}\right) /2}{\left\lbrack \left( n - 1\right) !\right\rbrack }^{n} \) .

> so finally \( \Delta = {\left( -1\right) }^{n\left( {n - 1}\right) /2}{\left\lbrack \left( n - 1\right) !\right\rbrack }^{n} \) .

Si maintenant \( n > p + 1 \) , nous allons montrer que \( \Delta = 0 \) . Notons \( P = {X}^{p} \in \mathbb{R}\left\lbrack X\right\rbrack \) et pour tout \( i \in \{ 1,\ldots , n\} ,{P}_{i} = P\left( {X + i}\right) = {\left( X + i\right) }^{p} \) , de sorte que la matrice \( A \) s’écrit

> If now \( n > p + 1 \) , we will show that \( \Delta = 0 \) . Let \( P = {X}^{p} \in \mathbb{R}\left\lbrack X\right\rbrack \) and for all \( i \in \{ 1,\ldots , n\} ,{P}_{i} = P\left( {X + i}\right) = {\left( X + i\right) }^{p} \) , so that the matrix \( A \) is written

\[
A = \left( \begin{matrix} {P}_{1}\left( 0\right) & {P}_{1}\left( 1\right) & \cdots & {P}_{1}\left( {n - 1}\right) \\  {P}_{2}\left( 0\right) & {P}_{2}\left( 1\right) & \cdots & {P}_{2}\left( {n - 1}\right) \\  \vdots & \vdots & & \vdots \\  {P}_{n}\left( 0\right) & {P}_{n}\left( 1\right) & \cdots & {P}_{n}\left( {n - 1}\right)  \end{matrix}\right) .
\]

Pour tout \( i,{P}_{i} \in {\mathbb{R}}_{p}\left\lbrack X\right\rbrack = \{ Q \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg Q \leq p\} \) . Comme \( {\mathbb{R}}_{p}\left\lbrack X\right\rbrack \) est un \( \mathbb{R} \) -e.v de dimension \( p + 1\left( {\left( {1, X,\ldots ,{X}^{p}}\right) \text{ en est une base) et que }n > p + 1}\right. \) , on en déduit que \( {P}_{1},\ldots ,{P}_{n} \) forme une famille liée. Donc il existe \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{R} \) , non tous nuls, tels que \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{P}_{i} = 0 \) , et donc pour tout \( j,0 \leq j \leq n - 1,\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{P}_{i}\left( j\right) = 0 \) . Autrement dit, les vecteurs lignes de la matrice \( A \) sont linéairement dépendants, ce qui entraîne \( \Delta = \det A = 0 \) .

> For all \( i,{P}_{i} \in {\mathbb{R}}_{p}\left\lbrack X\right\rbrack = \{ Q \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg Q \leq p\} \) . As \( {\mathbb{R}}_{p}\left\lbrack X\right\rbrack \) is a \( \mathbb{R} \) -v.s of dimension \( p + 1\left( {\left( {1, X,\ldots ,{X}^{p}}\right) \text{ en est une base) et que }n > p + 1}\right. \) , we deduce that \( {P}_{1},\ldots ,{P}_{n} \) forms a linearly dependent family. Thus there exist \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{R} \) , not all zero, such that \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{P}_{i} = 0 \) , and therefore for all \( j,0 \leq j \leq n - 1,\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{P}_{i}\left( j\right) = 0 \) . In other words, the row vectors of the matrix \( A \) are linearly dependent, which implies \( \Delta = \det A = 0 \) .

EXERCICE 5. Soit \( n \in {\mathbb{N}}^{ * } \) . Lorsque \( p \leq n \) , calculer le déterminant d’ordre \( p + 1 \)

> EXERCISE 5. Let \( n \in {\mathbb{N}}^{ * } \) . When \( p \leq n \) , calculate the determinant of order \( p + 1 \)

\[
{\Delta }_{p} = \left| \begin{matrix} 1 & {C}_{n}^{1} & {C}_{n}^{2} & \cdots & {C}_{n}^{p} \\  1 & {C}_{n + 1}^{1} & {C}_{n + 1}^{2} & \cdots & {C}_{n + 1}^{p} \\  \vdots & \vdots & \vdots & & \vdots \\  1 & {C}_{n + p}^{1} & {C}_{n + p}^{2} & \cdots & {C}_{n + p}^{p} \end{matrix}\right| .
\]

Solution. En retranchant à chacune des \( p \) dernières lignes la précédente (en commençant par la dernière), on obtient :

> Solution. By subtracting the previous row from each of the \( p \) last rows (starting from the last one), we obtain:

\[
{\Delta }_{p} = \left| \begin{matrix} 1 & {C}_{n}^{1} & {C}_{n}^{2} & \cdots & {C}_{n}^{p} \\  0 & {C}_{n}^{0} & {C}_{n}^{1} & \cdots & {C}_{n}^{p - 1} \\  \vdots & \vdots & \vdots & & \vdots \\  0 & {C}_{n + p - 1}^{0} & {C}_{n + p - 1}^{1} & \cdots & {C}_{n + p - 1}^{p - 1} \end{matrix}\right|  = \left| \begin{matrix} {C}_{n}^{0} & {C}_{n}^{1} & \cdots & {C}_{n}^{p - 1} \\  \vdots & \vdots & & \vdots \\  {C}_{n + p - 1}^{0} & {C}_{n + p - 1}^{1} & \cdots & {C}_{n + p - 1}^{p - 1} \end{matrix}\right|  = {\Delta }_{p - 1}
\]

(on a utilisé la relation \( \left. {{C}_{k + 1}^{\ell + 1} - {C}_{k}^{\ell + 1} = {C}_{k}^{\ell }}\right) \) . Donc \( {\Delta }_{p} = {\Delta }_{p - 1} = \cdots = {\Delta }_{1} = 1 \) .

> (we used the relation \( \left. {{C}_{k + 1}^{\ell + 1} - {C}_{k}^{\ell + 1} = {C}_{k}^{\ell }}\right) \) . Therefore \( {\Delta }_{p} = {\Delta }_{p - 1} = \cdots = {\Delta }_{1} = 1 \) .

EXERCICE 6. a) Calculer le déterminant d’ordre \( n \) à coefficients dans \( \mathbb{K} \)

> EXERCISE 6. a) Calculate the determinant of order \( n \) with coefficients in \( \mathbb{K} \)

\[
{\Delta }_{n} = \left| \begin{matrix} {a}_{1} + {x}_{1} & {a}_{1} & \cdots & {a}_{1} \\  {a}_{2} & {a}_{2} + {x}_{2} & \cdots & {a}_{2} \\  \vdots & &  \ddots  & \vdots \\  {a}_{n} & \cdots & {a}_{n} & {a}_{n} + {x}_{n} \end{matrix}\right| .
\]

b) Calculer le déterminant d’ordre \( n + 1 \) à coefficients dans \( \mathbb{K} \)

> b) Calculate the determinant of order \( n + 1 \) with coefficients in \( \mathbb{K} \)

\[
{\Delta }_{n} = \left| \begin{matrix} x & {a}_{1} & {a}_{2} & \cdots & {a}_{n} \\  {a}_{1} & x & {a}_{2} & \cdots & {a}_{n} \\  \vdots & {a}_{2} &  \ddots  &  \ddots  & \vdots \\  \vdots & \vdots &  \ddots  &  \ddots  & {a}_{n} \\  {a}_{1} & {a}_{2} & \cdots & {a}_{n} & x \end{matrix}\right| .
\]

Solution. a) Nous allons prouver par récurrence sur \( n \) que \( {\Delta }_{n} = {x}_{1}\cdots {x}_{n} + \mathop{\sum }\limits_{{j = 1}}^{n}\left( {{a}_{j}\mathop{\prod }\limits_{{k \neq j}}{x}_{k}}\right) \) . Le résultat est évidemment vrai pour \( n = 1 \) . Supposons le vrai au rang \( n - 1 \) et montrons le au rang \( n \) . En utilisant la linéarité du déterminant par rapport à la dernière colonne, on voit que

> Solution. a) We will prove by induction on \( n \) that \( {\Delta }_{n} = {x}_{1}\cdots {x}_{n} + \mathop{\sum }\limits_{{j = 1}}^{n}\left( {{a}_{j}\mathop{\prod }\limits_{{k \neq j}}{x}_{k}}\right) \) . The result is obviously true for \( n = 1 \) . Assume it is true for rank \( n - 1 \) and show it for rank \( n \) . Using the linearity of the determinant with respect to the last column, we see that

\[
{\Delta }_{n} = \left| \begin{matrix} {a}_{1} + {x}_{1} & {a}_{1} & \cdots & {a}_{1} \\  {a}_{2} &  \ddots  & \cdots & {a}_{2} \\  \vdots & \cdots & {a}_{n - 1} + {x}_{n - 1} & \vdots \\  {a}_{n} & \cdots & {a}_{n} & {a}_{n} \end{matrix}\right|  + \left| \begin{matrix} {a}_{1} + {x}_{1} & {a}_{1} & \cdots & 0 \\  {a}_{2} &  \ddots  & \cdots & \vdots \\  \vdots & \cdots & {a}_{n - 1} + {x}_{n - 1} & 0 \\  {a}_{n} & \cdots & {a}_{n} & {x}_{n} \end{matrix}\right|  = {D}_{1} + {D}_{2}.
\]

Si on retranche, dans le déterminant \( {D}_{1} \) , la dernière colonne aux \( n - 1 \) premières, on s’aperçoit que \( {D}_{1} = {a}_{n}{x}_{1}\cdots {x}_{n - 1} \) . Par ailleurs, en développant \( {D}_{2} \) par rapport à la dernière colonne, on obtient \( {D}_{2} = {x}_{n}{\Delta }_{n - 1} \) . Finalement, \( {\Delta }_{n} \) est égal à

> If we subtract the last column from the first \( n - 1 \) columns in the determinant \( {D}_{1} \) , we notice that \( {D}_{1} = {a}_{n}{x}_{1}\cdots {x}_{n - 1} \) . Furthermore, by expanding \( {D}_{2} \) with respect to the last column, we obtain \( {D}_{2} = {x}_{n}{\Delta }_{n - 1} \) . Finally, \( {\Delta }_{n} \) is equal to

\[
{D}_{1} + {D}_{2} = {a}_{n}{x}_{1}\cdots {x}_{n - 1} + {x}_{n}\left\lbrack  {{x}_{1}\cdots {x}_{n - 1} + \mathop{\sum }\limits_{{j = 1}}^{{n - 1}}\left( {{a}_{j}\mathop{\prod }\limits_{\substack{{1 \leq  k \leq  n - 1} \\  {k \neq  j} }}{x}_{k}}\right) }\right\rbrack   = {x}_{1}\cdots {x}_{n} + \mathop{\sum }\limits_{{j = 1}}^{n}\left( {{a}_{j}\mathop{\prod }\limits_{{k \neq  j}}{x}_{k}}\right) .
\]

b) En ajoutant les \( n \) premières colonnes à la dernière, on obtient

> b) By adding the first \( n \) columns to the last one, we obtain

\[
{\Delta }_{n} = \left( {x + \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}}\right) \left| \begin{matrix} x & {a}_{1} & \cdots & {a}_{n - 1} & 1 \\  {a}_{1} & x & \cdots & \vdots & 1 \\  \vdots & {a}_{2} &  \ddots  & {a}_{n - 1} & \vdots \\  \vdots & \vdots &  \ddots  & x & \vdots \\  {a}_{1} & {a}_{2} & \cdots & {a}_{n} & 1 \end{matrix}\right| ,
\]

puis en retranchant, pour \( 1 \leq j \leq n \) ,à la \( j \) -ième colonne \( {a}_{j} \) fois la dernière,

> then by subtracting, for \( 1 \leq j \leq n \) , \( {a}_{j} \) times the last column from the \( j \) -th column,

\[
{\Delta }_{n} = \left( {x + \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}}\right) \left| \begin{matrix} x - {a}_{1} &  \times  & \cdots &  \times  & 1 \\  0 & x - {a}_{2} &  \ddots  & \vdots & \vdots \\  \vdots & 0 &  \ddots  &  \times  & \vdots \\  \vdots & \vdots &  \ddots  & x - {a}_{n} & 1 \\  0 & 0 & \cdots & 0 & 1 \end{matrix}\right|  = \left( {x + \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}}\right) \mathop{\prod }\limits_{{i = 1}}^{n}\left( {x - {a}_{i}}\right) .
\]

\( \rightarrow \) EXERCICE 7 (DÉTERMINANT DE CAUCHY). Soient \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) et \( {b}_{1},\ldots ,{b}_{n} \in \mathbb{K} \) tels que pour tout \( \left( {i, j}\right) ,{a}_{i} + {b}_{j} \neq 0 \) . Calculer le déterminant d’ordre \( n \)

> \( \rightarrow \) EXERCISE 7 (CAUCHY DETERMINANT). Let \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) and \( {b}_{1},\ldots ,{b}_{n} \in \mathbb{K} \) be such that for all \( \left( {i, j}\right) ,{a}_{i} + {b}_{j} \neq 0 \) . Calculate the determinant of order \( n \)

\[
{\Delta }_{n} = \det {\left( \frac{1}{{a}_{i} + {b}_{j}}\right) }_{1 \leq  i, j \leq  n}.
\]

Solution. C'est classique. Il y a plusieurs moyens de procéder. Nous donnons ici une solution assez générale. Supposons dans un premier temps les \( {a}_{i} \) distincts deux à deux et \( n \geq 2 \) . L’existence de la décomposition d'une fraction rationnelle en éléments simples permet d'affirmer

> Solution. This is a classic. There are several ways to proceed. We provide a fairly general solution here. Assume first that the \( {a}_{i} \) are pairwise distinct and \( n \geq 2 \) . The existence of the partial fraction decomposition of a rational function allows us to state

\[
\exists {\lambda }_{1},\ldots ,{\lambda }_{n} \in  \mathbb{K},\;R\left( X\right)  = \frac{\left( {{b}_{1} - X}\right) \cdots \left( {{b}_{n - 1} - X}\right) }{\left( {X + {a}_{1}}\right) \cdots \left( {X + {a}_{n}}\right) } = \frac{{\lambda }_{1}}{X + {a}_{1}} + \cdots  + \frac{{\lambda }_{n}}{X + {a}_{n}}.
\]

Le calcul des coefficients \( {\lambda }_{k} \) correspondant aux poles simples \( \left( {-{a}_{k}}\right) \) est classique et donne

> The calculation of the coefficients \( {\lambda }_{k} \) corresponding to the simple poles \( \left( {-{a}_{k}}\right) \) is standard and gives

\[
\forall k,\;{\lambda }_{k} = \frac{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( {{b}_{i} + {a}_{k}}\right) }{\mathop{\prod }\limits_{{i \neq  k}}\left( {{a}_{i} - {a}_{k}}\right) } \neq  0.
\]

Si maintenant on note \( {L}_{1},\ldots ,{L}_{n} \) les lignes de \( {\Delta }_{n} \) , on a

> If we now denote the rows of \( {\Delta }_{n} \) as \( {L}_{1},\ldots ,{L}_{n} \) , we have

\[
{\Delta }_{n} = \left| \begin{matrix} {L}_{1} \\  \vdots \\  {L}_{n - 1} \\  {L}_{n} \end{matrix}\right|  = \frac{1}{{\lambda }_{n}}\left| \begin{matrix} {L}_{1} \\  \vdots \\  {L}_{n - 1} \\  \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{L}_{i} \end{matrix}\right|  = \frac{1}{{\lambda }_{n}}\left| \begin{matrix} \frac{1}{{a}_{1} + {b}_{1}} & \cdots & \frac{1}{{a}_{1} + {b}_{n - 1}} & \frac{1}{{a}_{1} + {b}_{n}} \\  \vdots & & \vdots & \vdots \\  \frac{1}{{a}_{n - 1} + {b}_{1}} & \cdots & \frac{1}{{a}_{n - 1} + {b}_{n - 1}} & \frac{1}{{a}_{n - 1} + {b}_{n}} \\  R\left( {b}_{1}\right) & \cdots & R\left( {b}_{n - 1}\right) & R\left( {b}_{n}\right)  \end{matrix}\right| .
\]

Compte tenu des égalités \( R\left( {b}_{i}\right) = 0 \) pour \( 1 \leq i \leq n - 1 \) , le développement de ce dernier déterminant par rapport à la dernière ligne donne

> Given the equalities \( R\left( {b}_{i}\right) = 0 \) for \( 1 \leq i \leq n - 1 \) , the expansion of this last determinant with respect to the last row gives

\[
{\Delta }_{n} = \frac{R\left( {b}_{n}\right) }{{\lambda }_{n}}{\Delta }_{n - 1} = \frac{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( {{b}_{i} - {b}_{n}}\right) }{\mathop{\prod }\limits_{{i = 1}}^{n}\left( {{b}_{n} + {a}_{i}}\right) } \cdot  \frac{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( {{a}_{i} - {a}_{n}}\right) }{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( {{b}_{i} + {a}_{n}}\right) } \cdot  {\Delta }_{n - 1}.
\]

Sachant que \( {\Delta }_{1} = 1/\left( {{a}_{1} + {b}_{1}}\right) \) , une récurrence sur \( n \) donne

> Knowing that \( {\Delta }_{1} = 1/\left( {{a}_{1} + {b}_{1}}\right) \) , an induction on \( n \) gives

\[
{\Delta }_{n} = \frac{\mathop{\prod }\limits_{{i < j}}\left( {{a}_{j} - {a}_{i}}\right) \mathop{\prod }\limits_{{i < j}}\left( {{b}_{j} - {b}_{i}}\right) }{\mathop{\prod }\limits_{{i, j}}\left( {{a}_{i} + {b}_{j}}\right) }.
\]

(*)

> Rappelons que nous avions supposé que les \( {a}_{i} \) étaient distincts deux à deux. Si maintenant deux des \( {a}_{i} \) sont égaux alors les deux lignes correspondantes dans \( {\Delta }_{n} \) sont égales et donc \( {\Delta }_{n} = 0 \) . L'égalité (*) est donc vraie dans tous les cas.

Recall that we had assumed the \( {a}_{i} \) were pairwise distinct. If two of the \( {a}_{i} \) are now equal, then the two corresponding rows in \( {\Delta }_{n} \) are equal and thus \( {\Delta }_{n} = 0 \) . The equality (*) is therefore true in all cases.

> Remarque. Cette méthode, ainsi que le résultat, sont à retenir. On peut par exemple calculer par cette technique un déterminant de Vandermonde.

Remark. This method, as well as the result, should be remembered. For example, one can calculate a Vandermonde determinant using this technique.

> - Grâce à ce résultat et à la formule \( {A}^{-1} = {}^{\mathrm{t}}\widetilde{A}/\left( {\det A}\right) \) , il est facile d’inverser une matrice dont l’élément d’indice \( \left( {i, j}\right) \) est \( 1/\left( {{a}_{i} + {b}_{j}}\right) \) puisque les mineurs d’une telle matrice sont aussi des déterminants de Cauchy.

- Thanks to this result and the formula \( {A}^{-1} = {}^{\mathrm{t}}\widetilde{A}/\left( {\det A}\right) \) , it is easy to invert a matrix whose element with index \( \left( {i, j}\right) \) is \( 1/\left( {{a}_{i} + {b}_{j}}\right) \) since the minors of such a matrix are also Cauchy determinants.

> EXERCICE 8. Soient \( {\alpha }_{1},\ldots ,{\alpha }_{n} \in \mathbb{K} \) . Calculer le déterminant

EXERCISE 8. Let \( {\alpha }_{1},\ldots ,{\alpha }_{n} \in \mathbb{K} \) . Calculate the determinant

\[
\Delta  = \left| \begin{matrix} 1 & {\alpha }_{1} & \cdots & {\alpha }_{1}^{k - 1} & {\alpha }_{1}^{k + 1} & \cdots & {\alpha }_{1}^{n} \\  1 & {\alpha }_{2} & \cdots & {\alpha }_{2}^{k - 1} & {\alpha }_{2}^{k + 1} & \cdots & {\alpha }_{2}^{n} \\  \vdots & \vdots & & \vdots & \vdots & & \vdots \\  1 & {\alpha }_{n} & \cdots & {\alpha }_{n}^{k - 1} & {\alpha }_{n}^{k + 1} & \cdots & {\alpha }_{n}^{n} \end{matrix}\right| .
\]

Solution. On introduit l’indéterminée \( X \) et on considère le déterminant

> Solution. We introduce the indeterminate \( X \) and consider the determinant

\[
\Delta \left( X\right)  = \left| \begin{matrix} 1 & {\alpha }_{1} & \cdots & {\alpha }_{1}^{k - 1} & {\alpha }_{1}^{k} & {\alpha }_{1}^{k + 1} & \cdots & {\alpha }_{1}^{n} \\  \vdots & \vdots & & \vdots & \vdots & & \vdots & \\  1 & {\alpha }_{n} & \cdots & {\alpha }_{n}^{k - 1} & {\alpha }_{n}^{k} & {\alpha }_{n}^{k + 1} & \cdots & {\alpha }_{n}^{n} \\  1 & X & \cdots & {X}^{k - 1} & {X}^{k} & {X}^{k + 1} & \cdots & {X}^{n} \end{matrix}\right|  \in  \mathbb{K}\left\lbrack  X\right\rbrack
\]

Le déterminant \( \Delta \) apparaît comme le mineur de l’élément \( {X}^{k} \) dans \( \Delta \left( X\right) \) . En développant \( \Delta \left( X\right) \) par rapport à sa dernière ligne, on s’aperçoit que \( \Delta \) est le coefficient de \( {X}^{k} \) multiplié par \( {\left( -1\right) }^{n + k} \) dans le polynôme \( \Delta \left( X\right) \) . Or \( \Delta \left( X\right) \) est un déterminant de Vandermonde :

> The determinant \( \Delta \) appears as the minor of the element \( {X}^{k} \) in \( \Delta \left( X\right) \) . By expanding \( \Delta \left( X\right) \) along its last row, we see that \( \Delta \) is the coefficient of \( {X}^{k} \) multiplied by \( {\left( -1\right) }^{n + k} \) in the polynomial \( \Delta \left( X\right) \) . However, \( \Delta \left( X\right) \) is a Vandermonde determinant:

\[
\Delta \left( X\right)  = V\left( {{\alpha }_{1},\ldots ,{\alpha }_{n}, X}\right)  = \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{\alpha }_{j} - {\alpha }_{i}}\right) \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\alpha }_{i}}\right) .
\]

D'après ce que l'on a dit plus haut, on a donc l'égalité

> Based on what was said above, we therefore have the equality

\[
\Delta  = {\left( -1\right) }^{n + k}{\left( -1\right) }^{n - k}{\sigma }_{n - k} \cdot  \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{\alpha }_{j} - {\alpha }_{i}}\right)  = {\sigma }_{n - k} \cdot  \mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{\alpha }_{j} - {\alpha }_{i}}\right) ,
\]

où \( {\sigma }_{n - k} \) désigne la valeur prise au point \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) par le polynôme symétrique élémentaire \( \sum {X}_{1}\cdots {X}_{n - k} \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack . \)

> where \( {\sigma }_{n - k} \) denotes the value taken at point \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) by the elementary symmetric polynomial \( \sum {X}_{1}\cdots {X}_{n - k} \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack . \)

Remarque. On peut ainsi connaître les cofacteurs d'une matrice de Vandermonde, donc inverser une matrice de Vandermonde.

> Remark. We can thus determine the cofactors of a Vandermonde matrix, and therefore invert a Vandermonde matrix.

EXERCICE 9. Soit \( E \) un \( \mathbb{K} \) -espace-vectoriel, où \( \mathbb{K} \) est un corps commutatif de caractéris-tique différente de 2, et soit \( p \in {\mathbb{N}}^{ * } \) . Soit \( f : {E}^{p} \rightarrow \mathbb{K} \) une forme \( p \) -linéaire. On suppose que \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) = 0 \) dès qu’il existe \( k \in {\mathbb{N}}^{ * }, k < p \) , tel que \( {x}_{k} = {x}_{k + 1} \) . Montrer que la forme \( p \) -linéaire \( f \) est alternée.

> EXERCISE 9. Let \( E \) be a \( \mathbb{K} \) -vector space, where \( \mathbb{K} \) is a commutative field of characteristic different from 2, and let \( p \in {\mathbb{N}}^{ * } \) . Let \( f : {E}^{p} \rightarrow \mathbb{K} \) be a \( p \) -linear form. Suppose that \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) = 0 \) whenever there exists \( k \in {\mathbb{N}}^{ * }, k < p \) such that \( {x}_{k} = {x}_{k + 1} \) . Show that the \( p \) -linear form \( f \) is alternating.

Solution. Soit \( x = \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {E}^{p} \) . Soit \( k \in {\mathbb{N}}^{ * }, k < p \) . L’application

> Solution. Let \( x = \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {E}^{p} \) . Let \( k \in {\mathbb{N}}^{ * }, k < p \) . The mapping

\[
\varphi  : {E}^{2} \rightarrow  \mathbb{K}\;\left( {u, v}\right)  \mapsto  f\left( {{x}_{1},\ldots ,{x}_{k - 1}, u, v,{x}_{k + 2},\ldots ,{x}_{p}}\right)
\]

est une forme bilinéaire, et elle est alternée d'après les hypothèses, donc antisymétrique (en effet, \( \varphi \left( {u + v, u + v}\right) = 0 = \varphi \left( {u, u}\right) + \varphi \left( {u, v}\right) + \varphi \left( {v, u}\right) + \varphi \left( {v, v}\right) \) entraine \( \varphi \left( {u, v}\right) = - \varphi \left( {v, u}\right) \) ; c’est un cas particulier du théorème 1 page 141). Pour tout \( \sigma \in {\mathcal{S}}_{p} \) (groupe des permutations de \( \{ 1,\ldots , p\} \) ), on note \( {x}_{\sigma } = \left( {{x}_{\sigma \left( 1\right) },\ldots ,{x}_{\sigma \left( p\right) }}\right) \) . L’égalité \( \varphi \left( {{x}_{k},{x}_{k + 1}}\right) = - \varphi \left( {{x}_{k + 1},{x}_{k}}\right) \) s’écrit aussi \( f\left( {x}_{\sigma }\right) = - f\left( x\right) = \varepsilon \left( \sigma \right) f\left( x\right) \) , où \( \sigma \) est la transposition \( \left( {k, k + 1}\right) \) . Or les transpositions de la forme \( \left( {k, k + 1}\right) \) engendrent \( {\mathcal{S}}_{p} \) (voir l’exercice 6 page 26), c’est-à-dire que pour tout \( \sigma \in {\mathcal{S}}_{p} \) , on peut écrire \( \sigma = {\tau }_{1}\cdots {\tau }_{n} \) où \( {\tau }_{i} \) est une transposition de la forme \( \left( {k, k + 1}\right) \) , donc

> is a bilinear form, and it is alternating according to the hypotheses, therefore antisymmetric (indeed, \( \varphi \left( {u + v, u + v}\right) = 0 = \varphi \left( {u, u}\right) + \varphi \left( {u, v}\right) + \varphi \left( {v, u}\right) + \varphi \left( {v, v}\right) \) implies \( \varphi \left( {u, v}\right) = - \varphi \left( {v, u}\right) \); this is a special case of theorem 1 on page 141). For any \( \sigma \in {\mathcal{S}}_{p} \) (group of permutations of \( \{ 1,\ldots , p\} \)), we denote \( {x}_{\sigma } = \left( {{x}_{\sigma \left( 1\right) },\ldots ,{x}_{\sigma \left( p\right) }}\right) \). The equality \( \varphi \left( {{x}_{k},{x}_{k + 1}}\right) = - \varphi \left( {{x}_{k + 1},{x}_{k}}\right) \) is also written \( f\left( {x}_{\sigma }\right) = - f\left( x\right) = \varepsilon \left( \sigma \right) f\left( x\right) \), where \( \sigma \) is the transposition \( \left( {k, k + 1}\right) \). However, transpositions of the form \( \left( {k, k + 1}\right) \) generate \( {\mathcal{S}}_{p} \) (see exercise 6 on page 26), meaning that for any \( \sigma \in {\mathcal{S}}_{p} \), we can write \( \sigma = {\tau }_{1}\cdots {\tau }_{n} \) where \( {\tau }_{i} \) is a transposition of the form \( \left( {k, k + 1}\right) \), therefore

\[
f\left( {x}_{\sigma }\right)  = f\left( {x}_{{\tau }_{1}\cdots {\tau }_{n}}\right)  = \varepsilon \left( {\tau }_{1}\right) f\left( {x}_{{\tau }_{2}\cdots {\tau }_{n}}\right)  = \cdots  = \varepsilon \left( {\tau }_{1}\right) \cdots \varepsilon \left( {\tau }_{n}\right) f\left( x\right)
\]

autrement dit \( f\left( {x}_{\sigma }\right) = \varepsilon \left( \sigma \right) f\left( x\right) \) . Ceci est vrai pour tout \( \sigma \in {\mathcal{S}}_{p} \) donc la forme \( p \) -linéaire \( f \) est antisymétrique, donc alternée d'après le théorème 1 page 141.

> in other words \( f\left( {x}_{\sigma }\right) = \varepsilon \left( \sigma \right) f\left( x\right) \). This is true for any \( \sigma \in {\mathcal{S}}_{p} \) therefore the \( p \)-linear form \( f \) is antisymmetric, and thus alternating according to theorem 1 on page 141.

EXERCICE 10. Soit \( E \) un \( \mathbb{K} \) -espace vectoriel de dimension \( n \in {\mathbb{N}}^{ * } \) , où \( \mathbb{K} \) est un corps commutatif de caractéristique différente de 2. Soit \( f \) une forme \( n \) -linéaire alternée sur \( E \) . Pour tout \( u \in \mathcal{L}\left( E\right) \) , on définit :

> EXERCISE 10. Let \( E \) be a \( \mathbb{K} \)-vector space of dimension \( n \in {\mathbb{N}}^{ * } \), where \( \mathbb{K} \) is a commutative field of characteristic different from 2. Let \( f \) be an alternating \( n \)-linear form on \( E \). For any \( u \in \mathcal{L}\left( E\right) \), we define:

\[
{f}_{u} : {E}^{n} \rightarrow  \mathbb{K}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  \mathop{\sum }\limits_{{i = 1}}^{n}f\left( {{x}_{1},\ldots ,{x}_{i - 1}, u\left( {x}_{i}\right) ,{x}_{i + 1},\ldots ,{x}_{n}}\right) .
\]

Montrer que \( {f}_{u} = \operatorname{tr}\left( u\right) f \) .

> Show that \( {f}_{u} = \operatorname{tr}\left( u\right) f \).

Solution. Fixons \( u \in \mathcal{L}\left( E\right) \) . L’application \( {f}_{u} \) est une forme \( n \) -linéaire alternée comme on le vérifie facilement ; l’ensemble \( F \) des formes \( n \) -linéaires alternées de \( E \) étant un \( \mathbb{K} \) -espace vectoriel de dimension 1, on a donc :

> Solution. Let us fix \( u \in \mathcal{L}\left( E\right) \). The mapping \( {f}_{u} \) is an alternating \( n \)-linear form as can be easily verified; the set \( F \) of alternating \( n \)-linear forms of \( E \) being a \( \mathbb{K} \)-vector space of dimension 1, we therefore have:

\[
\left( {\forall f \in  F, f \neq  0,\exists !{\lambda }_{f} \in  \mathbb{K}}\right) ,\;{f}_{u} = {\lambda }_{f} \cdot  f.
\]

Soit \( g \neq 0 \) une autre forme \( n \) -linéaire alternée. Il existe \( \mu \in {\mathbb{K}}^{ * } \) tel que \( f = {\mu g} \) . Donc \( {\lambda }_{f}f = {f}_{u} = \; \mu {g}_{u} = \left( {\mu {\lambda }_{g}}\right) g \) , et comme \( f = {\mu g} \) , on tire \( {\lambda }_{f} = {\lambda }_{g} \) . Le scalaire \( {\lambda }_{f} \) ne dépend donc pas de \( f \in F \) , mais seulement de \( u \) . On peut donc écrire :

> Let \( g \neq 0 \) be another alternating \( n \)-linear form. There exists \( \mu \in {\mathbb{K}}^{ * } \) such that \( f = {\mu g} \). Thus \( {\lambda }_{f}f = {f}_{u} = \; \mu {g}_{u} = \left( {\mu {\lambda }_{g}}\right) g \), and since \( f = {\mu g} \), we deduce \( {\lambda }_{f} = {\lambda }_{g} \). The scalar \( {\lambda }_{f} \) therefore does not depend on \( f \in F \), but only on \( u \). We can therefore write:

\[
\exists {\lambda }_{u} \in  \mathbb{K},\forall f \in  F,\;{f}_{u} = {\lambda }_{u}f.
\]

(*)

> Montrons maintenant que \( {\lambda }_{u} = \operatorname{tr}\left( u\right) \) . Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E, A = {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq n} \) la matrice de \( u \) dans cette base. En appliquant (*) à l’application det (déterminant dans la base \( B \) ), qui est bien une forme \( n \) -linéaire alternée, on obtient \( \mathop{\det }\limits_{u} = {\lambda }_{u}\det \) , donc \( {\lambda }_{u} = \; {\lambda }_{u}\det \left( {{e}_{1},\ldots ,{e}_{n}}\right) = \mathop{\det }\limits_{u}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , donc

Let us now show that \( {\lambda }_{u} = \operatorname{tr}\left( u\right) \). Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E, A = {\left( {a}_{i, j}\right) }_{1 \leq i < j \leq n} \) the matrix of \( u \) in this basis. By applying (*) to the map det (determinant in the basis \( B \)), which is indeed an alternating \( n \)-linear form, we obtain \( \mathop{\det }\limits_{u} = {\lambda }_{u}\det \), therefore \( {\lambda }_{u} = \; {\lambda }_{u}\det \left( {{e}_{1},\ldots ,{e}_{n}}\right) = \mathop{\det }\limits_{u}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \), thus

\[
{\lambda }_{u} = \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{e}_{1},\ldots ,{e}_{i - 1}, u\left( {e}_{i}\right) ,{e}_{i + 1},\ldots ,{e}_{n}}\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{e}_{1},\ldots ,{e}_{i - 1},\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{j, i}{e}_{j},{e}_{i + 1},\ldots ,{e}_{n}}\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{n}\left( {\mathop{\sum }\limits_{{j = 1}}^{n}{a}_{j, i}{\det }_{B}\left( {{e}_{1},\ldots ,{e}_{i - 1},{e}_{j},{e}_{i + 1},\ldots ,{e}_{n}}\right) }\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i} = \operatorname{tr}\left( u\right) .
\]

EXERCICE 11. a) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . On note \( \widetilde{A} \) sa comatrice. Donner le rang de \( \widetilde{A} \) en fonction du rang de \( A \) .

> EXERCISE 11. a) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). Let \( \widetilde{A} \) denote its comatrix. Give the rank of \( \widetilde{A} \) as a function of the rank of \( A \).

b) Si \( n \geq 3 \) , resoudre dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) l’équation \( A = \widetilde{A} \) .

> b) If \( n \geq 3 \), solve the equation \( A = \widetilde{A} \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \).

Solution. a) Si rg \( A = n \) , l’égalité \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} \) entraîne \( \widetilde{A} = {\left( \det A\right) }^{\mathrm{t}}{A}^{-1} \) , donc comme \( \det A \neq 0,\operatorname{rg}\widetilde{A} = n \) .

> Solution. a) If rg \( A = n \), the equality \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} \) implies \( \widetilde{A} = {\left( \det A\right) }^{\mathrm{t}}{A}^{-1} \), therefore as \( \det A \neq 0,\operatorname{rg}\widetilde{A} = n \).

Si \( \operatorname{rg}A = n - 1 \) , alors il existe un mineur d’un élément de \( A \) non nul (d’après le théo-rème 2 page 128), donc \( \widetilde{A} \neq 0 \) . De plus, on a \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} = 0 \) donc Im \( A \subset \operatorname{Ker}{}^{\mathrm{t}}\widetilde{A} \) , donc \( \dim \left( {\operatorname{Ker}{}^{\mathrm{t}}\widetilde{A}}\right) \geq n - 1 \) et doncr \( {\mathrm{{rg}}}^{\mathrm{t}}\widetilde{A} = \operatorname{rg}\widetilde{A} = n - \dim \left( {\operatorname{Ker}{}^{\mathrm{t}}\widetilde{A}}\right) \leq 1 \) . Comme on a vu que \( \widetilde{A} \neq 0 \) , ceci entraîne rg \( \widetilde{A} = 1 \) .

> If \( \operatorname{rg}A = n - 1 \), then there exists a non-zero minor of an element of \( A \) (according to theorem 2 on page 128), so \( \widetilde{A} \neq 0 \). Furthermore, we have \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} = 0 \) so Im \( A \subset \operatorname{Ker}{}^{\mathrm{t}}\widetilde{A} \), so \( \dim \left( {\operatorname{Ker}{}^{\mathrm{t}}\widetilde{A}}\right) \geq n - 1 \) and thus rg \( {\mathrm{{rg}}}^{\mathrm{t}}\widetilde{A} = \operatorname{rg}\widetilde{A} = n - \dim \left( {\operatorname{Ker}{}^{\mathrm{t}}\widetilde{A}}\right) \leq 1 \). As we have seen that \( \widetilde{A} \neq 0 \), this implies rg \( \widetilde{A} = 1 \).

Si rg \( A \leq n - 2 \) , alors tous les cofacteurs de \( A \) sont nuls, donc rg \( \widetilde{A} = 0 \) .

> If rg \( A \leq n - 2 \), then all cofactors of \( A \) are zero, so rg \( \widetilde{A} = 0 \).

b) L’égalité \( A = \widetilde{A} \) entraîne l’égalité rg \( A = \operatorname{rg}\widetilde{A} \) .

> b) The equality \( A = \widetilde{A} \) implies the equality rg \( A = \operatorname{rg}\widetilde{A} \) .

Si rg \( A \leq n - 2 \) , alors d’après a), rg \( \widetilde{A} = 0 \) , donc rg \( A = 0 \) , donc \( A = 0 \) .

> If rg \( A \leq n - 2 \) , then according to a), rg \( \widetilde{A} = 0 \) , so rg \( A = 0 \) , so \( A = 0 \) .

Si \( \operatorname{rg}A = n - 1 \) , alors \( \operatorname{rg}\widetilde{A} = 1 \) , et donc \( n - 1 = \operatorname{rg}A = \operatorname{rg}\widetilde{A} = 1 \) donc \( n = 2 \) , contraire aux hypothèses.

> If \( \operatorname{rg}A = n - 1 \) , then \( \operatorname{rg}\widetilde{A} = 1 \) , and thus \( n - 1 = \operatorname{rg}A = \operatorname{rg}\widetilde{A} = 1 \) so \( n = 2 \) , contrary to the hypotheses.

Si rg \( A = n \) , alors \( \left( {\det A}\right) {I}_{n} = {}^{\mathrm{t}}\widetilde{A}A = {}^{\mathrm{t}}{AA} \) . Or \( \det \left( {{}^{\mathrm{t}}{AA}}\right) = \det \left( {{}^{\mathrm{t}}A}\right) \det \left( A\right) = {\left( \det A\right) }^{2} \) et \( \det \left\lbrack {\left( {\det A}\right) {I}_{n}}\right\rbrack = {\left( \det A\right) }^{n} \) . Comme \( \det A \neq 0 \) , on en déduit (det \( A{)}^{n - 2} = 1 \) , et donc det \( A \in \; \{ - 1,1\} \operatorname{car}\det A \in \mathbb{R} \) . Si \( A = \left( {a}_{i, j}\right) \) , le terme d’indice \( \left( {1,1}\right) {\mathrm{{de}}}^{\mathrm{t}}{AA} \) est \( \mathop{\sum }\limits_{j}{a}_{1, j}^{2} \geq 0 \) , et comme \( {}^{\mathrm{t}}{AA} = \left( {\det A}\right) {I}_{n} \) , ce terme vaut det \( A \) . Donc det \( A \geq 0 \) , et donc det \( A = 1 \) .

> If rg \( A = n \) , then \( \left( {\det A}\right) {I}_{n} = {}^{\mathrm{t}}\widetilde{A}A = {}^{\mathrm{t}}{AA} \) . However \( \det \left( {{}^{\mathrm{t}}{AA}}\right) = \det \left( {{}^{\mathrm{t}}A}\right) \det \left( A\right) = {\left( \det A\right) }^{2} \) and \( \det \left\lbrack {\left( {\det A}\right) {I}_{n}}\right\rbrack = {\left( \det A\right) }^{n} \) . Since \( \det A \neq 0 \) , we deduce (det \( A{)}^{n - 2} = 1 \) , and thus det \( A \in \; \{ - 1,1\} \operatorname{car}\det A \in \mathbb{R} \) . If \( A = \left( {a}_{i, j}\right) \) , the term with index \( \left( {1,1}\right) {\mathrm{{de}}}^{\mathrm{t}}{AA} \) is \( \mathop{\sum }\limits_{j}{a}_{1, j}^{2} \geq 0 \) , and since \( {}^{\mathrm{t}}{AA} = \left( {\det A}\right) {I}_{n} \) , this term equals det \( A \) . Thus det \( A \geq 0 \) , and thus det \( A = 1 \) .

Finalement, on a montré que \( \det A = 1 \) et \( {}^{\mathrm{t}}{AA} = {I}_{n} \) . Réciproquement, si \( {}^{\mathrm{t}}{AA} = {I}_{n} \) et \( \det A = 1 \) , comme \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} = {I}_{n} \) , on a \( \widetilde{A} = A \) car \( A \) est inversible.

> Finally, we have shown that \( \det A = 1 \) and \( {}^{\mathrm{t}}{AA} = {I}_{n} \) . Conversely, if \( {}^{\mathrm{t}}{AA} = {I}_{n} \) and \( \det A = 1 \) , since \( {}^{\mathrm{t}}\widetilde{A}A = \left( {\det A}\right) {I}_{n} = {I}_{n} \) , we have \( \widetilde{A} = A \) because \( A \) is invertible.

Les matrices \( A \) vérifiant \( \widetilde{A} = A \) sont donc la matrice nulle et les matrices \( A \) telles que \( \det A = 1 \) et \( {}^{\mathrm{t}}{AA} = {I}_{n} \) (ces dernières forment l’ensemble \( {\mathcal{O}}_{n}^{ + } \) des matrices orthogonales de déterminant 1, i. e. le groupe spécial orthogonal).

> The matrices \( A \) satisfying \( \widetilde{A} = A \) are therefore the zero matrix and the matrices \( A \) such that \( \det A = 1 \) and \( {}^{\mathrm{t}}{AA} = {I}_{n} \) (the latter form the set \( {\mathcal{O}}_{n}^{ + } \) of orthogonal matrices with determinant 1, i. e. the special orthogonal group).

EXERCICE 12 (DÉTERMINANT CIRCULANT). Soit \( n \in {\mathbb{N}}^{ * } \) et \( \omega = {e}^{{2i\pi }/n} \) . On considère la matrice \( \Omega = {\left( {\omega }^{\left( {i - 1}\right) \left( {j - 1}\right) }\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> EXERCISE 12 (CIRCULANT DETERMINANT). Let \( n \in {\mathbb{N}}^{ * } \) and \( \omega = {e}^{{2i\pi }/n} \) . Consider the matrix \( \Omega = {\left( {\omega }^{\left( {i - 1}\right) \left( {j - 1}\right) }\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

a) Soient \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{C} \) et

> a) Let \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{C} \) and

\[
A = \left( \begin{matrix} {a}_{1} & {a}_{2} & {a}_{3} & \cdots & {a}_{n} \\  {a}_{n} & {a}_{1} & {a}_{2} & \cdots & {a}_{n - 1} \\  {a}_{n - 1} & {a}_{n} & {a}_{1} & \cdots & {a}_{n - 2} \\  \vdots & \vdots & \vdots & & \vdots \\  {a}_{2} & {a}_{3} & {a}_{4} & \cdots & {a}_{1} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) .
\]

Calculer \( \det \left( {A\Omega }\right) \) et en déduire la valeur de \( \det A \) .

> Calculate \( \det \left( {A\Omega }\right) \) and deduce the value of \( \det A \) .

b) (Application). Si \( \theta \in \mathbb{R} \) , calculer le déterminant \( n \times n \)

> b) (Application). If \( \theta \in \mathbb{R} \) , calculate the determinant \( n \times n \)

\[
\Delta \left( \theta \right)  = \left| \begin{matrix} \cos \theta & \cos {2\theta } & \cdots & \cos {n\theta } \\  \cos {n\theta } & \cos \theta & \cdots & \cos \left( {n - 1}\right) \theta \\  \vdots & \vdots & & \vdots \\  \cos {2\theta } & \cos {3\theta } & \cdots & \cos \theta  \end{matrix}\right| .
\]

Solution. a) Un peu d'attention montre que le coefficient d'indice \( \left( {i, j}\right) \) du produit \( {A\Omega } \) est \( {\omega }^{\left( {i - 1}\right) \left( {j - 1}\right) }P\left( {\omega }^{j - 1}\right) \) où \( P \) désigne le polynôme \( P = {a}_{1} + {a}_{2}X + \cdots + {a}_{n}{X}^{n - 1} \) . Autrement dit,

> Solution. a) A little attention shows that the coefficient with index \( \left( {i, j}\right) \) of the product \( {A\Omega } \) is \( {\omega }^{\left( {i - 1}\right) \left( {j - 1}\right) }P\left( {\omega }^{j - 1}\right) \) where \( P \) denotes the polynomial \( P = {a}_{1} + {a}_{2}X + \cdots + {a}_{n}{X}^{n - 1} \) . In other words,

\[
{A\Omega } = \left( \begin{matrix} P\left( 1\right) & P\left( \omega \right) & \cdots & P\left( {\omega }^{n - 1}\right) \\  P\left( 1\right) & {\omega P}\left( \omega \right) & \cdots & {\omega }^{n - 1}P\left( {\omega }^{n - 1}\right) \\  \vdots & \vdots & & \vdots \\  P\left( 1\right) & {\omega }^{n - 1}P\left( \omega \right) & \cdots & {\omega }^{\left( {n - 1}\right) \left( {n - 1}\right) }P\left( {\omega }^{n - 1}\right)  \end{matrix}\right) .
\]

On en déduit

> We deduce from this

\[
\det \left( {A\Omega }\right)  = P\left( 1\right) P\left( \omega \right) \cdots P\left( {\omega }^{n - 1}\right) \left| \begin{matrix} 1 & 1 & \cdots & 1 \\  1 & \omega & \cdots & {\omega }^{n - 1} \\  \vdots & \vdots & & \vdots \\  1 & {\omega }^{n - 1} & \cdots & {\omega }^{\left( {n - 1}\right) \left( {n - 1}\right) } \end{matrix}\right|  = P\left( 1\right) P\left( \omega \right) \cdots P\left( {\omega }^{n - 1}\right) \det \Omega .
\]

Comme det \( \Omega \neq 0 \) (c’est un Vandermonde dont les paramètres sont deux à deux distincts), on en déduit det \( A = P\left( 1\right) P\left( \omega \right) \cdots P\left( {\omega }^{n - 1}\right) \) .

> Since det \( \Omega \neq 0 \) (it is a Vandermonde determinant whose parameters are pairwise distinct), we deduce det \( A = P\left( 1\right) P\left( \omega \right) \cdots P\left( {\omega }^{n - 1}\right) \) .

b) On pose \( {U}_{n} = \left\{ {{e}^{{2ik\pi }/n} \mid k \in \mathbb{Z}}\right\} \) . Le résultat de la question précédente entraîne

> b) Let \( {U}_{n} = \left\{ {{e}^{{2ik\pi }/n} \mid k \in \mathbb{Z}}\right\} \) . The result of the previous question implies

\[
\Delta \left( \theta \right)  = \mathop{\prod }\limits_{{\omega  \in  {U}_{n}}}\left( {\cos \theta  + \omega \cos {2\theta } + \cdots  + {\omega }^{n - 1}\cos {n\theta }}\right) .
\]

(*)

> Supposons dans un premier temps \( \theta \notin \frac{2\pi }{n}\mathbb{Z} \) . Si \( \omega \in {U}_{n} \) , on pose

Assume initially \( \theta \notin \frac{2\pi }{n}\mathbb{Z} \) . If \( \omega \in {U}_{n} \) , we set

> \( S\left( \omega \right) = \cos \theta + \omega \cos {2\theta } + \cdots + {\omega }^{n - 1}\cos {n\theta }\; \) et \( \;T\left( \omega \right) = \sin \theta + \omega \sin {2\theta } + \cdots + {\omega }^{n - 1}\sin {n\theta }. \)

\( S\left( \omega \right) = \cos \theta + \omega \cos {2\theta } + \cdots + {\omega }^{n - 1}\cos {n\theta }\; \) and \( \;T\left( \omega \right) = \sin \theta + \omega \sin {2\theta } + \cdots + {\omega }^{n - 1}\sin {n\theta }. \)

> On a

We have

\[
S\left( \omega \right)  + {iT}\left( \omega \right)  = \frac{1}{\omega }\mathop{\sum }\limits_{{k = 1}}^{n}{\left( \omega {e}^{i\theta }\right) }^{k} = {e}^{i\theta }\frac{1 - {e}^{in\theta }}{1 - \omega {e}^{i\theta }}\;\text{ et }\;S\left( \omega \right)  - {iT}\left( \omega \right)  = {e}^{-{i\theta }}\frac{1 - {e}^{-{in\theta }}}{1 - \omega {e}^{-{i\theta }}}.
\]

En effectuant la demi-somme des deux expressions précédentes, on en déduit, après calculs, que

> By taking the half-sum of the two previous expressions, we deduce, after calculations, that

\[
S\left( \omega \right)  = 2\sin \left( \frac{n\theta }{2}\right)  \cdot  \frac{\sin \left( {\frac{n + 2}{2}\theta }\right)  - \omega \sin \left( \frac{n\theta }{2}\right) }{\left( {1 - \omega {e}^{i\theta }}\right) \left( {1 - \omega {e}^{-{i\theta }}}\right) }.
\]

(**)

> Avec la formule \( \left( *\right) \) , on en déduit

Using the formula \( \left( *\right) \) , we deduce

\[
\Delta \left( \theta \right)  = \mathop{\prod }\limits_{{\omega  \in  {U}_{n}}}S\left( \omega \right)  = {2}^{n}{\sin }^{n}\left( \frac{n\theta }{2}\right) \frac{\mathop{\prod }\limits_{{\omega  \in  {U}_{n}}}\left( {\sin \left( {\frac{n + 2}{2}\theta }\right)  - \omega \sin \left( \frac{n\theta }{2}\right) }\right) }{\mathop{\prod }\limits_{{\omega  \in  {U}_{n}}}\left( {1 - \omega {e}^{i\theta }}\right) \mathop{\prod }\limits_{{\omega  \in  {U}_{n}}}\left( {1 - \omega {e}^{-{i\theta }}}\right) }
\]

Lorsque \( a \in {\mathbb{C}}^{ * } \) , le polynôme \( {X}^{n} - {a}^{n} \) a \( n \) racines simples qui sont les \( {\omega a} \) avec \( \omega \in {U}_{n} \) , donc \( {X}^{n} - {a}^{n} = \mathop{\prod }\limits_{{\omega \in {U}_{n}}}\left( {X - {\omega a}}\right) \) . En utilisant cette identité pour \( a = \sin \frac{n\theta }{2} \) puis \( a = {e}^{i\theta } \) et \( a = {e}^{-{i\theta }} \) , on en déduit

> When \( a \in {\mathbb{C}}^{ * } \) , the polynomial \( {X}^{n} - {a}^{n} \) has \( n \) simple roots which are the \( {\omega a} \) with \( \omega \in {U}_{n} \) , therefore \( {X}^{n} - {a}^{n} = \mathop{\prod }\limits_{{\omega \in {U}_{n}}}\left( {X - {\omega a}}\right) \) . Using this identity for \( a = \sin \frac{n\theta }{2} \) then \( a = {e}^{i\theta } \) and \( a = {e}^{-{i\theta }} \) , we deduce

\[
\Delta \left( \theta \right)  = {2}^{n}{\sin }^{n}\left( \frac{n\theta }{2}\right) \frac{{\sin }^{n}\left( \frac{\left( {n + 2}\right) \theta }{2}\right)  - {\sin }^{n}\left( \frac{n\theta }{2}\right) }{\left( {1 - {e}^{ni\theta }}\right) \left( {1 - {e}^{-{ni\theta }}}\right) }
\]

et comme \( \left( {1 - {e}^{ni\theta }}\right) \left( {1 - {e}^{-{ni\theta }}}\right) = 4{\sin }^{2}\left( \frac{n\theta }{2}\right) \) on a finalement

> and since \( \left( {1 - {e}^{ni\theta }}\right) \left( {1 - {e}^{-{ni\theta }}}\right) = 4{\sin }^{2}\left( \frac{n\theta }{2}\right) \) we finally have

\[
\Delta \left( \theta \right)  = {2}^{n - 2}{\sin }^{n - 2}\left( \frac{n\theta }{2}\right) \left\lbrack  {{\sin }^{n}\left( {\frac{n + 2}{2}\theta }\right)  - {\sin }^{n}\left( \frac{n\theta }{2}\right) }\right\rbrack  .
\]

Nous avons démontré cette relation pour \( \theta \notin \frac{2\pi }{n}\mathbb{Z} \) . Le déterminant étant une fonction continue de ses coefficients (c’est un polynôme en ses coefficients), la fonction \( \theta \mapsto \Delta \left( \theta \right) \) est continue, et par continuité on en déduit que la relation trouvée est valable pour tout \( \theta \in \mathbb{R} \) .

> We have proven this relation for \( \theta \notin \frac{2\pi }{n}\mathbb{Z} \) . Since the determinant is a continuous function of its coefficients (it is a polynomial in its coefficients), the function \( \theta \mapsto \Delta \left( \theta \right) \) is continuous, and by continuity we deduce that the relation found is valid for all \( \theta \in \mathbb{R} \) .

Remarque. Une autre démonstration de a) fait l'objet de l'exercice 4 page 190.

> Remark. Another proof of a) is the subject of exercise 4 on page 190.

EXERCICE 13. Soient \( a, b \in \mathbb{K} \) avec \( a \neq b \) . On pose

> EXERCISE 13. Let \( a, b \in \mathbb{K} \) with \( a \neq b \) . We set

\[
{A}_{n} = \left( \begin{matrix} a + b & {ab} & 0 & \cdots & 0 \\  1 & a + b & {ab} &  \ddots  & \vdots \\  0 & 1 & a + b &  \ddots  & 0 \\  \vdots &  \ddots  &  \ddots  &  \ddots  & {ab} \\  0 & \cdots & 0 & 1 & a + b \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) .
\]

Calculer det \( {A}_{n} \) .

> Calculate det \( {A}_{n} \) .

Solution. Supposons \( n \geq 3 \) . En développant par rapport à la première ligne on obtient

> Solution. Assume \( n \geq 3 \) . By expanding along the first row we obtain

\[
\det {A}_{n} = \left( {a + b}\right) \det {A}_{n - 1} - {ab}\left| \begin{matrix} 1 & {ab} & 0 & \cdots & 0 \\  0 & a + b & {ab} &  \ddots  & \vdots \\  0 & 1 & a + b &  \ddots  & 0 \\  \vdots & 0 &  \ddots  &  \ddots  & {ab} \\  0 & \cdots &  \ddots  & 1 & a + b \end{matrix}\right| ,
\]

puis en développant le dernier déterminant de cette égalité par rapport à la première colonne, \( \det {A}_{n} = \left( {a + b}\right) \det {A}_{n - 1} - {ab}\det {A}_{n - 2} \) . Sachant que

> then by expanding the last determinant of this equality with respect to the first column, \( \det {A}_{n} = \left( {a + b}\right) \det {A}_{n - 1} - {ab}\det {A}_{n - 2} \) . Knowing that

\[
\det {A}_{1} = a + b = \frac{{a}^{2} - {b}^{2}}{a - b}\;\text{ et }\;\det {A}_{2} = {a}^{2} + {ab} + {b}^{2} = \frac{{a}^{3} - {b}^{3}}{a - b},
\]

on démontre facilement par récurrence sur \( n \) que \( \det {A}_{n} = \frac{{a}^{n + 1} - {b}^{n + 1}}{a - b} \) .

> we easily prove by induction on \( n \) that \( \det {A}_{n} = \frac{{a}^{n + 1} - {b}^{n + 1}}{a - b} \) .

Remarque. Si \( a = b \) , une récurrence donne det \( {A}_{n} = \left( {n + 1}\right) {a}^{n} \) .

> Remark. If \( a = b \) , an induction gives det \( {A}_{n} = \left( {n + 1}\right) {a}^{n} \) .

- À partir du résultat de cet exercice, on peut facilement calculer les déterminants de la forme

> - From the result of this exercise, one can easily calculate determinants of the form

\[
\left| \begin{matrix} \beta & \gamma & \left( 0\right) \\  \alpha &  \ddots  &  \ddots  \\   \ddots  &  \ddots  & \gamma \\  \left( 0\right) & \alpha & \beta  \end{matrix}\right| .
\]
