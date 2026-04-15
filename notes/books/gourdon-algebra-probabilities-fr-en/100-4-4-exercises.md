#### 4.4. Exercises

*Français : 4.4. Exercices*

EXERCICE 1. Calculer l'exponentielle de la matrice

> EXERCISE 1. Calculate the exponential of the matrix

\[
M = \left( \begin{matrix} 1 & 4 &  - 2 \\  0 & 6 &  - 3 \\   - 1 & 4 & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{3}\left( \mathbb{R}\right) .
\]

---

Solution. Le polynôme caractéristique de \( M \) est \( {P}_{M} = - {\left( X - 2\right) }^{2}\left( {X - 3}\right) \) . Les valeurs propres de \( M \) sont donc \( {\lambda }_{1} = 2 \) et \( {\lambda }_{2} = 3 \) . Pour calculer l’exponentielle de \( M \) , nous allons utiliser la méthode décrite page 206, en employant les mêmes notations. On part ici du polynôme annulateur \( F = {\left( X - 2\right) }^{2}\left( {X - 3}\right) \) . On a ici \( {Q}_{1} = \left( {X - 3}\right) \) et \( {Q}_{2} = {\left( X - 2\right) }^{2} \) . On recherche maintenant

> Solution. The characteristic polynomial of \( M \) is \( {P}_{M} = - {\left( X - 2\right) }^{2}\left( {X - 3}\right) \) . The eigenvalues of \( M \) are therefore \( {\lambda }_{1} = 2 \) and \( {\lambda }_{2} = 3 \) . To calculate the exponential of \( M \) , we will use the method described on page 206, using the same notation. We start here with the annihilating polynomial \( F = {\left( X - 2\right) }^{2}\left( {X - 3}\right) \) . We have here \( {Q}_{1} = \left( {X - 3}\right) \) and \( {Q}_{2} = {\left( X - 2\right) }^{2} \) . We are now looking for

---

\( {U}_{1},{U}_{2} \in \mathbb{R}\left\lbrack X\right\rbrack \) tels que \( {U}_{1}{Q}_{1} + {U}_{2}{Q}_{2} = 1 \) . On effectue pour cela la décomposition de \( 1/F \) en éléments simples. Après calculs, on trouve

> \( {U}_{1},{U}_{2} \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( {U}_{1}{Q}_{1} + {U}_{2}{Q}_{2} = 1 \) . To do this, we perform the partial fraction decomposition of \( 1/F \) . After calculations, we find

\[
\frac{1}{F} = \frac{1}{{\left( X - 2\right) }^{2}\left( {X - 3}\right) } =  - \frac{1}{X - 2} - \frac{1}{{\left( X - 2\right) }^{2}} + \frac{1}{X - 3} = \frac{1}{X - 3} - \frac{X - 1}{{\left( X - 2\right) }^{2}}
\]

donc \( {\left( X - 2\right) }^{2} - \left( {X - 1}\right) \left( {X - 3}\right) = 1 \) , et donc \( {U}_{1} = - \left( {X - 1}\right) \) et \( {U}_{2} = 1 \) conviennent. Si maintenant \( {P}_{1} = {U}_{1}{Q}_{1} = - \left( {X - 1}\right) \left( {X - 3}\right) \) et \( {P}_{2} = {U}_{2}{Q}_{2} = {\left( X - 2\right) }^{2} \) , les projecteurs \( {p}_{1} \) et \( {p}_{2} \) sont donnés par \( {p}_{1} = {P}_{1}\left( M\right) \) et \( {p}_{2} = {P}_{2}\left( M\right) \) . On sait alors que

> therefore \( {\left( X - 2\right) }^{2} - \left( {X - 1}\right) \left( {X - 3}\right) = 1 \) , and thus \( {U}_{1} = - \left( {X - 1}\right) \) and \( {U}_{2} = 1 \) are suitable. If now \( {P}_{1} = {U}_{1}{Q}_{1} = - \left( {X - 1}\right) \left( {X - 3}\right) \) and \( {P}_{2} = {U}_{2}{Q}_{2} = {\left( X - 2\right) }^{2} \) , the projectors \( {p}_{1} \) and \( {p}_{2} \) are given by \( {p}_{1} = {P}_{1}\left( M\right) \) and \( {p}_{2} = {P}_{2}\left( M\right) \) . We then know that

\[
\exp \left( M\right)  = {e}^{{\lambda }_{1}}\left( {{I}_{3} + \frac{1}{1!}\left( {M - 2{I}_{3}}\right) }\right) {p}_{1} + {e}^{{\lambda }_{2}}{p}_{2} = {e}^{2}\left( {M - {I}_{3}}\right) {p}_{1} + {e}^{3}{p}_{2}.
\]

Un calcul donne

> A calculation gives

\[
{p}_{1} = {P}_{1}\left( M\right)  =  - \left( {M - {I}_{3}}\right) \left( {M - 3{I}_{3}}\right)  = \left( \begin{matrix}  - 2 &  - 4 & 6 \\   - 3 &  - 3 & 6 \\   - 3 &  - 4 & 7 \end{matrix}\right)
\]

et

\[
{p}_{2} = {P}_{2}\left( M\right)  = {\left( M - 2{I}_{3}\right) }^{2} = \left( \begin{matrix} 3 & 4 &  - 6 \\  3 & 4 &  - 6 \\  3 & 4 &  - 6 \end{matrix}\right) ,
\]

(au passage, on vérifie que \( {p}_{1} + {p}_{2} = {I}_{3} \) ), donc

> (incidentally, we verify that \( {p}_{1} + {p}_{2} = {I}_{3} \) ), therefore

\[
\exp \left( M\right)  = \left( \begin{matrix}  - 6{e}^{2} + 3{e}^{3} &  - 4{e}^{2} + 4{e}^{3} & {10}{e}^{2} - 6{e}^{3} \\   - 6{e}^{2} + 3{e}^{3} &  - 3{e}^{2} + 4{e}^{3} & 9{e}^{2} - 6{e}^{3} \\   - 7{e}^{2} + 3{e}^{3} &  - 4{e}^{2} + 4{e}^{3} & {11}{e}^{2} - 6{e}^{3} \end{matrix}\right) .
\]

EXERCICE 2. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Donner une condition nécessaire et suffisante sur la matrice \( M \) pour que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) .

> EXERCISE 2. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Give a necessary and sufficient condition on the matrix \( M \) such that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) .

Solution. Nous allons montrer que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) si et seulement si pour toute valeur propre \( \lambda \) de \( M \) , la partie réelle \( \Re \left( \lambda \right) \) de \( \lambda \) vérifie \( \Re \left( \lambda \right) < 0 \) .

> Solution. We will show that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) if and only if for every eigenvalue \( \lambda \) of \( M \) , the real part \( \Re \left( \lambda \right) \) of \( \lambda \) satisfies \( \Re \left( \lambda \right) < 0 \) .

Condition nécessaire. Supposons que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) . Soit \( \lambda \) une valeur propre de \( M \) , et \( X \) un vecteur propre associé. On a facilement

> Necessary condition. Suppose that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) . Let \( \lambda \) be an eigenvalue of \( M \) , and \( X \) an associated eigenvector. We easily have

\[
\forall p \in  \mathbb{N},\;{M}^{p}X = {\lambda }^{p}X
\]

donc

> therefore

\[
\forall t \in  \mathbb{R},\;{e}^{tM}X = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{t}^{p}}{p!}{M}^{p}X = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{t}^{p}}{p!}{\lambda }^{p}X = {e}^{t\lambda }X.
\]

Ainsi, \( \mathop{\lim }\limits_{{t \rightarrow \infty }}{e}^{t\lambda } = 0 \) , ce qui entraîne \( \Re \left( \lambda \right) < 0 \) .

> Thus, \( \mathop{\lim }\limits_{{t \rightarrow \infty }}{e}^{t\lambda } = 0 \) , which implies \( \Re \left( \lambda \right) < 0 \) .

Condition suffisante. Supposons que pour toute valeur propre \( \lambda \) de \( M \) , on ait \( \Re \left( \lambda \right) < 0 \) . Si \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , on pose \( \parallel A\parallel = \mathop{\sum }\limits_{{i, j}}\left| {a}_{i, j}\right| \) . La norme \( \parallel \cdot \parallel \) est une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Sufficient condition. Suppose that for every eigenvalue \( \lambda \) of \( M \), we have \( \Re \left( \lambda \right) < 0 \). If \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), we set \( \parallel A\parallel = \mathop{\sum }\limits_{{i, j}}\left| {a}_{i, j}\right| \). The norm \( \parallel \cdot \parallel \) is an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \).

D’après le théorème 2, on peut écrire \( M = D + N \) avec \( D \) diagonalisable, \( N \) nilpotente et \( {DN} = {ND} \) . Comme \( D \) et \( N \) commutent, on a \( \exp \left( M\right) = \exp \left( D\right) \exp \left( N\right) \) . Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tel que

> According to theorem 2, we can write \( M = D + N \) with \( D \) diagonalizable, \( N \) nilpotent, and \( {DN} = {ND} \). Since \( D \) and \( N \) commute, we have \( \exp \left( M\right) = \exp \left( D\right) \exp \left( N\right) \). Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) be such that

\[
{P}^{-1}{DP} = \left( \begin{matrix} {\lambda }_{1} & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & {\lambda }_{n} \end{matrix}\right)  = {D}^{\prime }.
\]

Les \( {\lambda }_{i} \) sont les valeurs propres de \( M \) , et par hypothèse \( \mu = \mathop{\sup }\limits_{i}\Re \left( {\lambda }_{i}\right) < 0 \) . On a

> The \( {\lambda }_{i} \) are the eigenvalues of \( M \), and by hypothesis \( \mu = \mathop{\sup }\limits_{i}\Re \left( {\lambda }_{i}\right) < 0 \). We have

\[
\forall t \in  \mathbb{R},\;\exp \left( {t{D}^{\prime }}\right)  = \left( \begin{matrix} {e}^{t{\lambda }_{1}} & & 0 \\   &  \ddots  & \\  0 & & {e}^{t{\lambda }_{n}} \end{matrix}\right) \;\text{ donc }\;\begin{Vmatrix}{\exp \left( {t{D}^{\prime }}\right) }\end{Vmatrix} = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {e}^{t{\lambda }_{i}}\right|  \leq  n{e}^{t\mu }.
\]

Comme \( \exp \left( {tD}\right) = {P}^{-1}\exp \left( {t{D}^{\prime }}\right) P \) , ceci entraîne

> Since \( \exp \left( {tD}\right) = {P}^{-1}\exp \left( {t{D}^{\prime }}\right) P \), this implies

\[
\parallel \exp \left( {tD}\right) \parallel  \leq  \begin{Vmatrix}{P}^{-1}\end{Vmatrix} \cdot  n{e}^{t\mu } \cdot  \parallel P\parallel  = K{e}^{t\mu },\;K = n\begin{Vmatrix}{P}^{-1}\end{Vmatrix} \cdot  \parallel P\parallel
\]

(*)

> Maintenant, \( N \) étant nilpotente, on a

Now, \( N \) being nilpotent, we have

\[
\forall t \geq  0,\;\exp \left( {tN}\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{{t}^{k}}{k!}{N}^{k}\;\text{ donc }\;\parallel \exp \left( {tN}\right) \parallel  \leq  \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{{t}^{k}}{k!}\parallel N{\parallel }^{k} = f\left( t\right) .
\]

Avec \( \left( *\right) \) , on peut maintenant écrire

> With \( \left( *\right) \), we can now write

\[
\parallel \exp \left( {tM}\right) \parallel  = \parallel \exp \left( {tD}\right) \exp \left( {tN}\right) \parallel  \leq  \parallel \exp \left( {tD}\right) \parallel  \cdot  \parallel \exp \left( {tN}\right) \parallel  \leq  K{e}^{t\mu }f\left( t\right) .
\]

Comme \( t \mapsto f\left( t\right) \) est polynomiale et \( \mu < 0 \) , on en déduit que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \) .

> Since \( t \mapsto f\left( t\right) \) is polynomial and \( \mu < 0 \), we deduce that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{e}^{tM} = 0 \).

EXERCICE 3. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Donner une condition nécessaire et suffisante sur \( M \) pour que \( M \) et \( {2M} \) soient semblables.

> EXERCISE 3. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \). Give a necessary and sufficient condition on \( M \) for \( M \) and \( {2M} \) to be similar.

Solution. Supposons \( M \) et \( {2M} \) semblables. Alors si \( \lambda \) est valeur propre de \( M,{2\lambda } \) est valeur propre de \( {2M} \) , donc de \( M \) (car \( M \) est semblable à \( {2M} \) ). De même, \( 2\left( {2\lambda }\right) \) est valeur propre de \( M \) . On itérant le procédé, on voit ainsi que pour tout \( p \in \mathbb{N},{2}^{p}\lambda \) est valeur propre de \( M \) . \( M \) n’ayant qu’un nombre fini de valeurs propres, on doit donc avoir \( \lambda = 0 \) pour toute valeur propre \( \lambda \) de \( M \) . Le corps de base \( \mathbb{C} \) étant algébriquement clos, on en déduit que la seule racine du polynôme caractéristique \( {P}_{M} \) de \( M \) est 0, donc \( {P}_{M} = {\left( -1\right) }^{n}{X}^{n} \) , et donc \( M \) est nilpotente d'après le théorème de Cayley-Hamilton.

> Solution. Suppose \( M \) and \( {2M} \) are similar. Then if \( \lambda \) is an eigenvalue of \( M,{2\lambda } \), it is an eigenvalue of \( {2M} \), and thus of \( M \) (since \( M \) is similar to \( {2M} \)). Similarly, \( 2\left( {2\lambda }\right) \) is an eigenvalue of \( M \). By iterating the process, we see that for all \( p \in \mathbb{N},{2}^{p}\lambda \), it is an eigenvalue of \( M \). Since \( M \) has only a finite number of eigenvalues, we must have \( \lambda = 0 \) for every eigenvalue \( \lambda \) of \( M \). The base field \( \mathbb{C} \) being algebraically closed, we deduce that the only root of the characteristic polynomial \( {P}_{M} \) of \( M \) is 0, so \( {P}_{M} = {\left( -1\right) }^{n}{X}^{n} \), and thus \( M \) is nilpotent according to the Cayley-Hamilton theorem.

Réciproquement, supposons \( M \) nilpotente. Soit \( f \) l’endomorphisme de \( {\mathbb{C}}^{n} \) dont la matrice dans la base canonique \( B \) de \( {\mathbb{C}}^{n} \) est \( M \) . On sait (théorème 4) qu’il existe une base \( {B}_{1} = \; \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{C}}^{n} \) telle que

> Conversely, suppose \( M \) is nilpotent. Let \( f \) be the endomorphism of \( {\mathbb{C}}^{n} \) whose matrix in the canonical basis \( B \) of \( {\mathbb{C}}^{n} \) is \( M \). We know (Theorem 4) that there exists a basis \( {B}_{1} = \; \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{C}}^{n} \) such that

\[
{\left\lbrack  f\right\rbrack  }_{{B}_{1}} = \left( \begin{matrix} 0 & {v}_{1} & & \left( 0\right) \\  0 & 0 &  \ddots  & \\  \vdots & &  \ddots  & {v}_{n - 1} \\  0 & \cdots & \cdots & 0 \end{matrix}\right) \;\text{ avec }\;\forall i,{v}_{i} \in  \{ 0,1\} .
\]

On note maintenant \( {B}_{2} \) la base \( {B}_{2} = \left( {{e}_{1},2{e}_{2},\ldots ,{2}^{n - 1}{e}_{n}}\right) \) . Pour tout \( i \in \{ 1,\ldots , n - 1\} \) , on a \( f\left( {e}_{i + 1}\right) = {v}_{i}{e}_{i} \) donc \( f\left( {{2}^{i}{e}_{i + 1}}\right) = \left( {2{v}_{i}}\right) \left( {{2}^{i - 1}{e}_{i}}\right) \) , et donc

> We now denote the basis \( {B}_{2} = \left( {{e}_{1},2{e}_{2},\ldots ,{2}^{n - 1}{e}_{n}}\right) \) as \( {B}_{2} \). For all \( i \in \{ 1,\ldots , n - 1\} \), we have \( f\left( {e}_{i + 1}\right) = {v}_{i}{e}_{i} \) therefore \( f\left( {{2}^{i}{e}_{i + 1}}\right) = \left( {2{v}_{i}}\right) \left( {{2}^{i - 1}{e}_{i}}\right) \), and thus

\[
{\left\lbrack  f\right\rbrack  }_{{B}_{2}} = \left( \begin{matrix} 0 & 2{v}_{1} & & \left( 0\right) \\  0 & 0 &  \ddots  & \\  \vdots & &  \ddots  & 2{v}_{n - 1} \\  0 & \cdots & \cdots & 0 \end{matrix}\right)  = 2{\left\lbrack  f\right\rbrack  }_{{B}_{1}}
\]

donc \( 2{\left\lbrack f\right\rbrack }_{{B}_{1}} \) et \( {\left\lbrack f\right\rbrack }_{{B}_{1}} \) sont semblables, donc \( {2M} \) et \( M \) sont semblables.

> therefore \( 2{\left\lbrack f\right\rbrack }_{{B}_{1}} \) and \( {\left\lbrack f\right\rbrack }_{{B}_{1}} \) are similar, so \( {2M} \) and \( M \) are similar.

En résumé, \( M \) et \( {2M} \) sont semblables si et seulement si \( M \) est nilpotente.

> In summary, \( M \) and \( {2M} \) are similar if and only if \( M \) is nilpotent.

EXERCICE 4 (TOUTE MATRICE EST SEMBLABLE À SA TRANSPOSÉE). a) Soit une matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer que \( M \) et \( {}^{\mathrm{t}}M \) sont semblables (on pensera à la réduction de Jordan). b) Que dire dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ?

> EXERCISE 4 (EVERY MATRIX IS SIMILAR TO ITS TRANSPOSE). a) Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a matrix. Show that \( M \) and \( {}^{\mathrm{t}}M \) are similar (consider the Jordan reduction). b) What can be said in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \)?

Solution. a) D'après le théorème 5 et la remarque 4, il existe \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) et des nombres complexes \( {\alpha }_{i} \) tels que

> Solution. a) According to Theorem 5 and Remark 4, there exists \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) and complex numbers \( {\alpha }_{i} \) such that

![bo_d7fjffs91nqc73erehlg_212_189_290_1181_195_0.jpg](images/gourdon_algebra_probabilities_fr_en_008_bod7fjffs91nqc73erehlg21218929011811950.jpg)

Pour tout \( i \) , on va montrer que \( {M}_{i} \) et \( {}^{\mathrm{t}}{M}_{i} \) sont semblables. Soit \( {n}_{i} \) la taille de la matrice \( {M}_{i} \) . Si \( {n}_{i} = 1 \) on a \( {M}_{i} = \left( {\alpha }_{i}\right) \) donc \( {M}_{i} = {}^{\mathrm{t}}{M}_{i} \) donc \( {M}_{i} \) et \( {}^{\mathrm{t}}{M}_{i} \) sont semblables. Si \( {n}_{i} > 1 \) , on considère l’endomorphisme \( {f}_{i} \) de \( {\mathbb{C}}^{{n}_{i}} \) dont \( {M}_{i} \) est la matrice dans la base canonique \( B = \left( {{e}_{1},\ldots ,{e}_{{n}_{i}}}\right) \) de \( {\mathbb{C}}^{{n}_{i}} \) . Soit \( {B}^{\prime } \) la base \( \left( {{e}_{{n}_{i}},\ldots ,{e}_{2},{e}_{1}}\right) \) de \( {\mathbb{C}}^{{n}_{i}} \) . On a facilement

> For all \( i \), we will show that \( {M}_{i} \) and \( {}^{\mathrm{t}}{M}_{i} \) are similar. Let \( {n}_{i} \) be the size of matrix \( {M}_{i} \). If \( {n}_{i} = 1 \), we have \( {M}_{i} = \left( {\alpha }_{i}\right) \) therefore \( {M}_{i} = {}^{\mathrm{t}}{M}_{i} \), so \( {M}_{i} \) and \( {}^{\mathrm{t}}{M}_{i} \) are similar. If \( {n}_{i} > 1 \), we consider the endomorphism \( {f}_{i} \) of \( {\mathbb{C}}^{{n}_{i}} \) whose matrix in the canonical basis \( B = \left( {{e}_{1},\ldots ,{e}_{{n}_{i}}}\right) \) of \( {\mathbb{C}}^{{n}_{i}} \) is \( {M}_{i} \). Let \( {B}^{\prime } \) be the basis \( \left( {{e}_{{n}_{i}},\ldots ,{e}_{2},{e}_{1}}\right) \) of \( {\mathbb{C}}^{{n}_{i}} \). We easily have

![bo_d7fjffs91nqc73erehlg_212_513_670_536_196_0.jpg](images/gourdon_algebra_probabilities_fr_en_009_bod7fjffs91nqc73erehlg2125136705361960.jpg)

donc \( {}^{\mathrm{t}}{M}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{{B}^{\prime }} \) est semblable à \( {M}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{B} \) .

> therefore \( {}^{\mathrm{t}}{M}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{{B}^{\prime }} \) is similar to \( {M}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{B} \).

Pour tout \( i \) , on peut donc trouver une matrice \( {P}_{i} \) inversible telle que \( {}^{\mathrm{t}}{M}_{i} = {P}_{i}^{-1}{M}_{i}{P}_{i} \) . La matrice \( P = \left( \begin{matrix} {P}_{1} & & 0 \\ & \ddots & \\ 0 & & {P}_{q} \end{matrix}\right) \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est inversible, son inverse est \( {P}^{-1} = \left( \begin{matrix} {P}_{1}^{-1} & & 0 \\ & \ddots & \\ 0 & & {P}_{q}^{-1} \end{matrix}\right) \) et on a

> For any \( i \), we can therefore find an invertible matrix \( {P}_{i} \) such that \( {}^{\mathrm{t}}{M}_{i} = {P}_{i}^{-1}{M}_{i}{P}_{i} \). The matrix \( P = \left( \begin{matrix} {P}_{1} & & 0 \\ & \ddots & \\ 0 & & {P}_{q} \end{matrix}\right) \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is invertible, its inverse is \( {P}^{-1} = \left( \begin{matrix} {P}_{1}^{-1} & & 0 \\ & \ddots & \\ 0 & & {P}_{q}^{-1} \end{matrix}\right) \), and we have

\[
{P}^{-1}{M}^{\prime }P = \left( \begin{matrix} {P}_{1}^{-1}{M}_{1}{P}_{1} & & 0 \\   &  \ddots  & \\  0 & & {P}_{q}^{-1}{M}_{q}{P}_{q} \end{matrix}\right)  = \left( \begin{matrix} {}^{\mathrm{t}}{M}_{1} & & 0 \\   &  \ddots  & \\  0 & & {}^{\mathrm{t}}{M}_{q} \end{matrix}\right)  = {}^{\mathrm{t}}{M}^{\prime }
\]

ce qui entraîne \( {}^{\mathrm{t}}\left( {{Q}^{-1}{MQ}}\right) = {P}^{-1}\left( {{Q}^{-1}{MQ}}\right) P \) donc \( {}^{\mathrm{t}}M = {R}^{-1}{MR} \) avec \( R = Q{P}^{\mathrm{t}}Q \) .

> which implies \( {}^{\mathrm{t}}\left( {{Q}^{-1}{MQ}}\right) = {P}^{-1}\left( {{Q}^{-1}{MQ}}\right) P \) therefore \( {}^{\mathrm{t}}M = {R}^{-1}{MR} \) with \( R = Q{P}^{\mathrm{t}}Q \).

b) Dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , on ne peut plus procéder comme plus haut car le corps de base \( \mathbb{R} \) n’est pas algébriquement clos et donc on n’est pas assuré de la réduction de Jordan de \( M \) .

> b) In \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), we can no longer proceed as above because the base field \( \mathbb{R} \) is not algebraically closed and therefore we are not guaranteed the Jordan reduction of \( M \).

On s’en tire autrement. Si \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \subset {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) alors d’après a), il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tel que \( {}^{\mathrm{t}}M = {P}^{-1}{MP} \) . On a vu au problème 14 page 167 que deux matrices réelles semblables dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) sont semblables sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , autrement dit, il existe \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) tel que \( {}^{\mathrm{t}}M = {Q}^{-1}{MQ} \) .

> We handle this differently. If \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \subset {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), then according to a), there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( {}^{\mathrm{t}}M = {P}^{-1}{MP} \). We saw in problem 14 on page 167 that two real matrices similar in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) are similar over \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), in other words, there exists \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that \( {}^{\mathrm{t}}M = {Q}^{-1}{MQ} \).

Remarque. Le résultat de a) reste vrai sur tout corps \( \mathbb{K} \) dès que \( {P}_{M} \) est scindé sur \( \mathbb{K} \) . On en déduit que pour tout corps \( \mathbb{K}, M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est semblable dans \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) à \( {}^{\mathrm{t}}M \) où \( \mathbb{L} \) désigne le corps des racines de \( {P}_{M} \) . Si \( \mathbb{K} \) est infini, on en déduit (toujours grâce au résultat du problème 14 page 167) que \( M \) et \( {}^{\mathrm{t}}M \) sont semblables dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . (En fait, ceci est vrai même si K est un corps fini - voir l’annexe B, partie 3.2.)

> Remark. The result of a) remains true over any field \( \mathbb{K} \) as soon as \( {P}_{M} \) splits over \( \mathbb{K} \). We deduce that for any field \( \mathbb{K}, M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is similar in \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) to \( {}^{\mathrm{t}}M \) where \( \mathbb{L} \) denotes the splitting field of \( {P}_{M} \). If \( \mathbb{K} \) is infinite, we deduce (still thanks to the result of problem 14 on page 167) that \( M \) and \( {}^{\mathrm{t}}M \) are similar in \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). (In fact, this is true even if K is a finite field - see Appendix B, part 3.2.)

EXERCICE 5 (LOGARITHME D’UNE MATRICE INVERSIBLE). 1/ a) Soit \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . Montrer qu’il existe \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) telle que \( \exp \left( A\right) = M \) .

> EXERCISE 5 (LOGARITHM OF AN INVERTIBLE MATRIX). 1/ a) Let \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \). Show that there exists \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( \exp \left( A\right) = M \).

b) Déterminer l’ensemble des matrices \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) telles que \( \exp \left( B\right) = {I}_{n} \) .

> b) Determine the set of matrices \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( \exp \left( B\right) = {I}_{n} \) .

2/ (Application). On se donne un entier \( p \geq 2 \) .

> 2/ (Application). Let \( p \geq 2 \) be an integer.

a) Soit \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . Montrer l’existence d’une matrice \( B \) telle que \( {B}^{p} = A \) .

> a) Let \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . Show the existence of a matrix \( B \) such that \( {B}^{p} = A \) .

b) Lorsque \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) n’est pas inversible, existe-t-il toujours une matrice \( B \) telle que \( A = {B}^{p} \) ?

> b) When \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is not invertible, does there always exist a matrix \( B \) such that \( A = {B}^{p} \) ?

\( \mathbf{3}/ \) (Seconde application). Montrer que \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) est connexe.

> \( \mathbf{3}/ \) (Second application). Show that \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) is connected.

Solution. 1/ a) D'après la conséquence du théorème 2, \( M \) est semblable à une matrice de la forme

> Solution. 1/ a) According to the consequence of theorem 2, \( M \) is similar to a matrix of the form

\[
{M}^{\prime } = \left( \begin{matrix} {B}_{1} & & & 0 \\   & {B}_{2} & & \\   & 0 &  \ddots  & \\   & & & {B}_{p} \end{matrix}\right) ,\;\text{ les blocs }{B}_{i}\text{ étant de la forme }\left( \begin{matrix} \lambda &  \times  & \cdots &  \times  \\  0 & \lambda &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & \lambda  \end{matrix}\right) .
\]

Soit \( B \in {\mathcal{M}}_{m}\left( \mathbb{C}\right) \) un tel bloc. On a \( \lambda \neq 0 \) puisque \( M \) est inversible. On peut écrire \( B = \lambda \left( {{I}_{m} + N}\right) \) où \( N \) est une matrice nilpotente. Posons \( C = {I}_{m} + N \) . Par analogie avec le fait que pour \( \left| t\right| < 1 \) , \( \log \left( {1 + t}\right) = t - \frac{{t}^{2}}{2} + \frac{{t}^{3}}{3} + \cdots \) , on pose

> Let \( B \in {\mathcal{M}}_{m}\left( \mathbb{C}\right) \) be such a block. We have \( \lambda \neq 0 \) since \( M \) is invertible. We can write \( B = \lambda \left( {{I}_{m} + N}\right) \) where \( N \) is a nilpotent matrix. Let us set \( C = {I}_{m} + N \) . By analogy with the fact that for \( \left| t\right| < 1 \) , \( \log \left( {1 + t}\right) = t - \frac{{t}^{2}}{2} + \frac{{t}^{3}}{3} + \cdots \) , we set

\[
D = N - \frac{{N}^{2}}{2} + \cdots  + {\left( -1\right) }^{m}\frac{{N}^{m - 1}}{m - 1}.
\]

Comme on s’y attend, nous allons montrer que \( \exp \left( D\right) = {I}_{m} + N = C \) . Ceci peut se déduire d’un calcul formel analogue au cas des séries entières sur \( \mathbb{C} \) . Pour le lecteur non convaincu, nous allons donner une autre démonstration. Pour tout \( t \in \mathbb{R} \) , on pose

> As expected, we will show that \( \exp \left( D\right) = {I}_{m} + N = C \) . This can be deduced from a formal calculation analogous to the case of power series over \( \mathbb{C} \) . For the unconvinced reader, we will provide another proof. For any \( t \in \mathbb{R} \) , we set

\[
D\left( t\right)  = {tN} - \frac{{t}^{2}}{2}{N}^{2} + \cdots  + {\left( -1\right) }^{m}\frac{{t}^{m - 1}}{m - 1}{N}^{m - 1}.
\]

Par dérivation, on obtient \( {D}^{\prime }\left( t\right) = N - t{N}^{2} + \cdots + {\left( -1\right) }^{m}{t}^{m - 2}{N}^{m - 1} \) , et comme \( {N}^{m} = 0 \) (car \( N \) est nilpotente), on a \( \left( {{I}_{m} + {tN}}\right) {D}^{\prime }\left( t\right) = N \) . Si \( S\left( t\right) = \exp \left\lbrack {D\left( t\right) }\right\rbrack \) , comme \( D \) et \( {D}^{\prime } \) commutent on a donc \( \left( {{I}_{m} + {tN}}\right) {S}^{\prime }\left( t\right) = {NS}\left( t\right) \;\left( *\right) \) , et en dérivant une nouvelle fois \( \left( {{I}_{m} + {tN}}\right) {S}^{\prime \prime }\left( t\right) = 0 \) , d’où on tire \( {S}^{\prime \prime }\left( t\right) = 0 \) car \( \left( {{I}_{m} + {tN}}\right) \) est toujours inversible (son inverse est \( {I}_{m} - {tN} + {t}^{2}{N}^{2} + \cdots + \; {\left( -1\right) }^{m - 1}{M}^{m - 1}) \) . Pour tout \( t,{S}^{\prime }\left( t\right) \) est donc une fonction constante,égale à \( {S}^{\prime }\left( 0\right) = N \) d’après \( \left( *\right) \) . Or \( S\left( 0\right) = {I}_{m} \) donc pour tout \( t, S\left( t\right) = {I}_{m} + {tN} \) . En particulier, \( C = S\left( 1\right) = \exp \left\lbrack {D\left( 1\right) }\right\rbrack = \exp \left( D\right) \) .

> By differentiation, we obtain \( {D}^{\prime }\left( t\right) = N - t{N}^{2} + \cdots + {\left( -1\right) }^{m}{t}^{m - 2}{N}^{m - 1} \), and since \( {N}^{m} = 0 \) (because \( N \) is nilpotent), we have \( \left( {{I}_{m} + {tN}}\right) {D}^{\prime }\left( t\right) = N \). If \( S\left( t\right) = \exp \left\lbrack {D\left( t\right) }\right\rbrack \), as \( D \) and \( {D}^{\prime } \) commute, we have \( \left( {{I}_{m} + {tN}}\right) {S}^{\prime }\left( t\right) = {NS}\left( t\right) \;\left( *\right) \), and by differentiating once more \( \left( {{I}_{m} + {tN}}\right) {S}^{\prime \prime }\left( t\right) = 0 \), from which we derive \( {S}^{\prime \prime }\left( t\right) = 0 \) because \( \left( {{I}_{m} + {tN}}\right) \) is always invertible (its inverse is \( {I}_{m} - {tN} + {t}^{2}{N}^{2} + \cdots + \; {\left( -1\right) }^{m - 1}{M}^{m - 1}) \)). For all \( t,{S}^{\prime }\left( t\right) \), it is therefore a constant function, equal to \( {S}^{\prime }\left( 0\right) = N \) according to \( \left( *\right) \). However, \( S\left( 0\right) = {I}_{m} \), so for all \( t, S\left( t\right) = {I}_{m} + {tN} \). In particular, \( C = S\left( 1\right) = \exp \left\lbrack {D\left( 1\right) }\right\rbrack = \exp \left( D\right) \).

Ceci étant, soit \( \mu \in \mathbb{C} \) tel que \( {e}^{\mu } = \lambda \) (si \( \lambda = \left| \lambda \right| {e}^{i\theta } \) , il suffit de prendre \( \mu = \log \left| \lambda \right| + {i\theta } \) ). Alors \( \exp \left( {\mu {I}_{m} + D}\right) = \exp \left( {\mu {I}_{m}}\right) \exp \left( D\right) = \left( {\lambda {I}_{m}}\right) C = B \) .

> That being said, let \( \mu \in \mathbb{C} \) be such that \( {e}^{\mu } = \lambda \) (if \( \lambda = \left| \lambda \right| {e}^{i\theta } \), it suffices to take \( \mu = \log \left| \lambda \right| + {i\theta } \)). Then \( \exp \left( {\mu {I}_{m} + D}\right) = \exp \left( {\mu {I}_{m}}\right) \exp \left( D\right) = \left( {\lambda {I}_{m}}\right) C = B \).

Ainsi, pour tout \( i \) , il existe une matrice \( {A}_{i} \) telle que \( \exp \left( {A}_{i}\right) = {B}_{i} \) . Si on note

> Thus, for all \( i \), there exists a matrix \( {A}_{i} \) such that \( \exp \left( {A}_{i}\right) = {B}_{i} \). If we denote

\[
{A}^{\prime } = \left( \begin{matrix} {A}_{1} & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & {A}_{p} \end{matrix}\right) \;\text{ on a }\;\exp \left( {A}^{\prime }\right)  = \left( \begin{matrix} \exp \left( {A}_{1}\right) & \left( 0\right) \\   \ddots  & \\  \left( 0\right) & \exp \left( {A}_{p}\right)  \end{matrix}\right)  = {M}^{\prime }.
\]

Si \( P \) est une matrice inversible telle que \( {P}^{-1}{M}^{\prime }P = M \) , on voit que la matrice \( A = {P}^{-1}{A}^{\prime }P \) vérifie \( \exp \left( A\right) = {P}^{-1}\exp \left( {A}^{\prime }\right) P = M \) .

> If \( P \) is an invertible matrix such that \( {P}^{-1}{M}^{\prime }P = M \), we see that the matrix \( A = {P}^{-1}{A}^{\prime }P \) satisfies \( \exp \left( A\right) = {P}^{-1}\exp \left( {A}^{\prime }\right) P = M \).

b) Considérons une matrice \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) telle que \( \exp \left( B\right) = {I}_{n} \) . On peut écrire \( B = D + N \) où \( D \) est une matrice diagonalisable, \( N \) une matrice nilpotente, avec \( {DN} = {ND} \) .

> b) Consider a matrix \( B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) such that \( \exp \left( B\right) = {I}_{n} \). We can write \( B = D + N \) where \( D \) is a diagonalizable matrix, \( N \) a nilpotent matrix, with \( {DN} = {ND} \).

Nous allons montrer que \( N = 0 \) . On a \( {I}_{n} = \exp \left( B\right) = \exp \left( D\right) \exp \left( N\right) \) donc \( \exp \left( N\right) = \; \exp {\left( D\right) }^{-1} = \exp \left( {-D}\right) \) . L’exponentielle d’une matrice diagonalisable étant diagonalisable (pour s'en convaincre, se placer dans une base de diagonalisation et remarquer que l'exponentielle d'une matrice diagonale est diagonale), \( \exp \left( N\right) = I + N + \cdots + {N}^{n - 1}/\left( {n - 1}\right) ! = \exp \left( {-D}\right) \) est donc diagonalisable. Si on pose \( Q = 1 + X + \cdots + {X}^{n - 1}/\left( {n - 1}\right) ! \in \mathbb{R}\left\lbrack X\right\rbrack \) , on a \( \exp \left( N\right) = Q\left( N\right) \) . Comme \( N \) est nilpotente, sa seule valeur propre est 0 donc la seule valeur propre de \( Q\left( N\right) \) est \( Q\left( 0\right) = 1 \) (voir la remarque 1 page 184). De plus, on a vu que \( Q\left( N\right) = \exp \left( N\right) \) est diagonalisable; elle est donc semblable à l’identité, donc égale à \( I \) , et donc \( N + \cdots + {N}^{n - 1}/\left( {n - 1}\right) ! = 0 \) . Autrement dit, le polynôme \( R = X + \cdots + {X}^{n - 1}/\left( {n - 1}\right) \) ! annule \( N \) . Le polynôme minimal \( {\Pi }_{N} \) de \( N \) est de la forme \( {\Pi }_{N} = {X}^{\alpha } \) puisque \( N \) est nilpotente. Comme \( R\left( N\right) = 0 \) , on a \( {\Pi }_{N} = {X}^{\alpha } \mid R \) , ce qui entraîne que \( \alpha = 1 \) . Finalement, \( 0 = {\Pi }_{N}\left( N\right) = N \) .

> We will show that \( N = 0 \) . We have \( {I}_{n} = \exp \left( B\right) = \exp \left( D\right) \exp \left( N\right) \) so \( \exp \left( N\right) = \; \exp {\left( D\right) }^{-1} = \exp \left( {-D}\right) \) . Since the exponential of a diagonalizable matrix is diagonalizable (to see this, consider a basis of diagonalization and note that the exponential of a diagonal matrix is diagonal), \( \exp \left( N\right) = I + N + \cdots + {N}^{n - 1}/\left( {n - 1}\right) ! = \exp \left( {-D}\right) \) is therefore diagonalizable. If we set \( Q = 1 + X + \cdots + {X}^{n - 1}/\left( {n - 1}\right) ! \in \mathbb{R}\left\lbrack X\right\rbrack \) , we have \( \exp \left( N\right) = Q\left( N\right) \) . Since \( N \) is nilpotent, its only eigenvalue is 0, so the only eigenvalue of \( Q\left( N\right) \) is \( Q\left( 0\right) = 1 \) (see remark 1 on page 184). Furthermore, we have seen that \( Q\left( N\right) = \exp \left( N\right) \) is diagonalizable; it is therefore similar to the identity, thus equal to \( I \) , and so \( N + \cdots + {N}^{n - 1}/\left( {n - 1}\right) ! = 0 \) . In other words, the polynomial \( R = X + \cdots + {X}^{n - 1}/\left( {n - 1}\right) \) ! annihilates \( N \) . The minimal polynomial \( {\Pi }_{N} \) of \( N \) is of the form \( {\Pi }_{N} = {X}^{\alpha } \) since \( N \) is nilpotent. As \( R\left( N\right) = 0 \) , we have \( {\Pi }_{N} = {X}^{\alpha } \mid R \) , which implies that \( \alpha = 1 \) . Finally, \( 0 = {\Pi }_{N}\left( N\right) = N \) .

En résumé, on a montré que \( B = D \) est diagonalisable. Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tel que

> In summary, we have shown that \( B = D \) is diagonalizable. Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) be such that

\[
{P}^{-1}{BP} = \left( \begin{matrix} {\lambda }_{1} & \left( 0\right) \\  \ldots & \\  \left( 0\right) & {\lambda }_{n} \end{matrix}\right) .
\]

On a

> We have

![bo_d7fjffs91nqc73erehlg_214_392_216_770_154_0.jpg](images/gourdon_algebra_probabilities_fr_en_010_bod7fjffs91nqc73erehlg2143922167701540.jpg)

donc pour tout \( j,{e}^{{\lambda }_{j}} = 1 \) , c’est-à-dire \( {\lambda }_{j} \in {2i\pi }\mathbb{Z} \) . Réciproquement, si \( B \) est diagonalisable à valeurs propres dans \( {2i\pi }\mathbb{Z} \) , on a facilement \( \exp \left( B\right) = {I}_{n} \) . Les matrices \( B \) telles que \( \exp \left( B\right) = {I}_{n} \) sont donc les matrices diagonalisables à valeurs propres dans \( {2i\pi }\mathbb{Z} \) .

> so for all \( j,{e}^{{\lambda }_{j}} = 1 \) , that is to say \( {\lambda }_{j} \in {2i\pi }\mathbb{Z} \) . Conversely, if \( B \) is diagonalizable with eigenvalues in \( {2i\pi }\mathbb{Z} \) , we easily have \( \exp \left( B\right) = {I}_{n} \) . The matrices \( B \) such that \( \exp \left( B\right) = {I}_{n} \) are therefore the diagonalizable matrices with eigenvalues in \( {2i\pi }\mathbb{Z} \) .

2 / a) Le résultat de la question 1/a) nous assure l’existence d’une matrice \( M \) telle que \( A = \; \exp \left( M\right) \) . En posant \( B = \exp \left( {M/p}\right) \) , on a \( {B}^{p} = \exp \left( M\right) = A \) .

> 2 / a) The result of question 1/a) ensures the existence of a matrix \( M \) such that \( A = \; \exp \left( M\right) \) . By setting \( B = \exp \left( {M/p}\right) \) , we have \( {B}^{p} = \exp \left( M\right) = A \) .

b) Non ! Considérons une matrice nilpotente \( A \) dont l’indice de nilpotence est \( n \) , i. e. vérifiant \( {A}^{n} = 0 \neq {A}^{n - 1} \) . Une telle matrice existe, par exemple le bloc de Jordan

> b) No! Consider a nilpotent matrix \( A \) whose index of nilpotency is \( n \) , i.e., satisfying \( {A}^{n} = 0 \neq {A}^{n - 1} \) . Such a matrix exists, for example the Jordan block

\[
A = \left( \begin{matrix} 0 & 1 & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  \vdots & &  \ddots  & 1 \\  0 & \cdots & \cdots & 0 \end{matrix}\right) .
\]

Si \( A = {B}^{p} \) , alors \( {A}^{n} = {B}^{np} = 0 \) donc \( B \) est une matrice nilpotente, donc \( {B}^{n} = 0 \) (en effet, d’après la remarque 6 page 187, \( {P}_{B} = {\left( -1\right) }^{n}{X}^{n} \) donc \( {B}^{n} = 0 \) d’après le théorème de Cayley-Hamilton). Or \( 0 \neq {A}^{n - 1} = {B}^{p\left( {n - 1}\right) } \) , donc forcément \( p\left( {n - 1}\right) < n \) , ce qui est impossible dès que \( n \geq 2 \) .

> If \( A = {B}^{p} \) , then \( {A}^{n} = {B}^{np} = 0 \) so \( B \) is a nilpotent matrix, thus \( {B}^{n} = 0 \) (indeed, according to remark 6 on page 187, \( {P}_{B} = {\left( -1\right) }^{n}{X}^{n} \) so \( {B}^{n} = 0 \) according to the Cayley-Hamilton theorem). However \( 0 \neq {A}^{n - 1} = {B}^{p\left( {n - 1}\right) } \) , so necessarily \( p\left( {n - 1}\right) < n \) , which is impossible as soon as \( n \geq 2 \) .

3 / Il suffit de montrer que \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) est connexe par arcs. Soient \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . Il existe deux matrices \( A \) et \( B \) telles que \( P = \exp \left( A\right) \) et \( Q = \exp \left( B\right) \) . Le chemin \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \;t \mapsto \; \exp \left( {{tA} + \left( {1 - t}\right) B}\right) \) relie continúment \( Q = \exp \left( B\right) \) à \( P = \exp \left( A\right) \) . De plus, pour tout \( t \in \left\lbrack {0,1}\right\rbrack \) , \( \varphi \left( t\right) \) est l’exponentielle d’une matrice, donc inversible. Finalement, \( \varphi \) relie continûment \( P \) et \( Q \) dans \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , d’où le résultat.

> 3 / It suffices to show that \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) is path-connected. Let \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . There exist two matrices \( A \) and \( B \) such that \( P = \exp \left( A\right) \) and \( Q = \exp \left( B\right) \) . The path \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \;t \mapsto \; \exp \left( {{tA} + \left( {1 - t}\right) B}\right) \) continuously connects \( Q = \exp \left( B\right) \) to \( P = \exp \left( A\right) \) . Moreover, for all \( t \in \left\lbrack {0,1}\right\rbrack \) , \( \varphi \left( t\right) \) is the exponential of a matrix, and thus invertible. Finally, \( \varphi \) continuously connects \( P \) and \( Q \) in \( \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , hence the result.

Remarque. Une matrice réelle inversible, même de déterminant positif, n'est pas forcément l'exponentielle d'une matrice réelle (voir l'exercice 2 page 196).

> Remark. An invertible real matrix, even with a positive determinant, is not necessarily the exponential of a real matrix (see exercise 2 on page 196).
