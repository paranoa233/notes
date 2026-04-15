#### 2.2. Linear differential equations with constant coefficients

*Français : 2.2. Équations différentielles linéaires à coefficients constants*

Lorsque \( A\left( t\right) \) est une matrice constante \( A \) , il est possible de résoudre l’équation différentielle \( {Y}^{\prime } = {AY} \) en utilisant une exponentielle de matrice (voir le tome Algèbre). Rappelons que pour \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on note \( \exp \left( A\right) = {e}^{A} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{A}^{n}/n! \) .

> When \( A\left( t\right) \) is a constant matrix \( A \), it is possible to solve the differential equation \( {Y}^{\prime } = {AY} \) using a matrix exponential (see the Algebra volume). Recall that for \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), we denote \( \exp \left( A\right) = {e}^{A} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{A}^{n}/n! \).

Proposition 2. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . L’équation différentielle \( \left( H\right) : {Y}^{\prime } = {AY} \) a ses solutions maximales définies sur \( \mathbb{R} \) , et la solution prenant une valeur donnée \( {V}_{0} \in {\mathbb{R}}^{n} \) en \( t = 0 \) est \( V : \mathbb{R} \rightarrow {\mathbb{R}}^{n}\;t \mapsto {e}^{tA}{V}_{0}, o\dot{u}{V}_{0} \in {\mathbb{K}}^{n} \) .

> Proposition 2. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). The differential equation \( \left( H\right) : {Y}^{\prime } = {AY} \) has its maximal solutions defined on \( \mathbb{R} \), and the solution taking a given value \( {V}_{0} \in {\mathbb{R}}^{n} \) at \( t = 0 \) is \( V : \mathbb{R} \rightarrow {\mathbb{R}}^{n}\;t \mapsto {e}^{tA}{V}_{0}, o\dot{u}{V}_{0} \in {\mathbb{K}}^{n} \).

Démonstration. La fonction \( V \) prend bien la valeur \( {V}_{0} \) en 0 car l’exponentielle de la matrice nulle est la matrice identité. Par ailleurs, on peut écrire \( V \) sous la forme \( V\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{n}}{n!}\left( {{A}^{n}{V}_{0}}\right) \) . Par les techniques usuelles sur les séries de fonctions, on montre que \( V \) est de classe \( {\mathcal{C}}^{1} \) sur \( \mathbb{R} \) et que

> Proof. The function \( V \) indeed takes the value \( {V}_{0} \) at 0 because the exponential of the zero matrix is the identity matrix. Furthermore, we can write \( V \) in the form \( V\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{n}}{n!}\left( {{A}^{n}{V}_{0}}\right) \). Using standard techniques for series of functions, we show that \( V \) is of class \( {\mathcal{C}}^{1} \) on \( \mathbb{R} \) and that

\[
\forall t \in  \mathbb{R},\;{V}^{\prime }\left( t\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{t}^{n - 1}}{\left( {n - 1}\right) !}\left( {{A}^{n}{V}_{0}}\right)  = A\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{n}}{n!}\left( {{A}^{n}{V}_{0}}\right) }\right)  = {AV}\left( t\right) .
\]

Remarque 5. - En réduisant la matrice \( A \) , on peut donc avoir de précieux renseigne-ments sur les solutions de \( \left( H\right) \) .

> Remark 5. - By reducing the matrix \( A \), we can therefore obtain valuable information about the solutions of \( \left( H\right) \).

- Lorsque l’on travaille sur le corps \( \mathbb{K} = \mathbb{R} \) , on peut réduire la matrice \( A \) dans \( \mathbb{C} \) , puis écrire les solutions de \( \left( H\right) \) sous la forme \( \varphi \left( t\right)  + \overline{\varphi \left( t\right) } \) où \( \varphi \) est une solution complexe de \( \left( H\right) \) .

> - When working over the field \( \mathbb{K} = \mathbb{R} \), we can reduce the matrix \( A \) in \( \mathbb{C} \), then write the solutions of \( \left( H\right) \) in the form \( \varphi \left( t\right)  + \overline{\varphi \left( t\right) } \) where \( \varphi \) is a complex solution of \( \left( H\right) \).

Un cas particulier intéressant est celui des équations différentielles linéaires homogènes d’ordre \( p \) sur \( \mathbb{K} \) ,à coefficients constants :

> An interesting special case is that of homogeneous linear differential equations of order \( p \) over \( \mathbb{K} \), with constant coefficients:

\[
{y}^{\left( p\right) } + {a}_{1}{y}^{\left( p - 1\right) } + \cdots  + {a}_{p}y = 0. \tag{E}
\]

En se ramenant au cas matriciel, on peut montrer le résultat suivant (dans le cas \( \mathbb{K} = \mathbb{C} \) ).

> By reducing it to the matrix case, one can show the following result (in the case \( \mathbb{K} = \mathbb{C} \) ).

On considère le polynôme \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) (appelé polynôme caractéristique de \( E \) ), puis on le factorise sous la forme \( \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {r}_{i}\right) }^{{m}_{i}} \) . Les solutions de \( \left( E\right) \) sont les applications

> We consider the polynomial \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) (called the characteristic polynomial of \( E \) ), then we factor it in the form \( \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {r}_{i}\right) }^{{m}_{i}} \) . The solutions of \( \left( E\right) \) are the mappings

\[
t \mapsto  \mathop{\sum }\limits_{{i = 1}}^{k}{e}^{{r}_{i}t}{P}_{i}\left( t\right)
\]

où les \( {P}_{i} \) sont des polynômes de degré \( < {m}_{i} \) . Ce résultat fait l’objet de l’exercice 4 page 385. Il généralise les résultats connus pour l'ordre 1 et l'ordre 2. Rappelons ceux du deuxième ordre. Soit \( \left( H\right) : {y}^{\prime \prime } + a{y}^{\prime } + {by} = 0 \) et \( P = {X}^{2} + {aX} + b \) . Alors

> where the \( {P}_{i} \) are polynomials of degree \( < {m}_{i} \) . This result is the subject of exercise 4 on page 385. It generalizes the results known for order 1 and order 2. Let us recall those of the second order. Let \( \left( H\right) : {y}^{\prime \prime } + a{y}^{\prime } + {by} = 0 \) and \( P = {X}^{2} + {aX} + b \) . Then

- Si \( P \) a deux racines distinctes \( {r}_{1} \) et \( {r}_{2} \) , les solutions de \( \left( H\right) \) sont les fonctions \( t \mapsto  {\lambda }_{1}{e}^{{r}_{1}t} + {\lambda }_{2}{e}^{{r}_{2}t},\left( {{\lambda }_{1},{\lambda }_{2}}\right)  \in  {\mathbb{C}}^{2} \) (si on est sur \( \mathbb{R} \) et si les \( {r}_{i} \) sont complexes, il faut conjuguer les expressions);

> - If \( P \) has two distinct roots \( {r}_{1} \) and \( {r}_{2} \) , the solutions of \( \left( H\right) \) are the functions \( t \mapsto  {\lambda }_{1}{e}^{{r}_{1}t} + {\lambda }_{2}{e}^{{r}_{2}t},\left( {{\lambda }_{1},{\lambda }_{2}}\right)  \in  {\mathbb{C}}^{2} \) (if we are on \( \mathbb{R} \) and if the \( {r}_{i} \) are complex, the expressions must be conjugated);

- Si \( P \) a une racine double \( r \) , les solutions sont les fonctions \( t \mapsto  \left( {{\lambda t} + \mu }\right) {e}^{rt},\left( {\lambda ,\mu }\right)  \in \; {\mathbb{K}}^{2} \) .

> - If \( P \) has a double root \( r \) , the solutions are the functions \( t \mapsto  \left( {{\lambda t} + \mu }\right) {e}^{rt},\left( {\lambda ,\mu }\right)  \in \; {\mathbb{K}}^{2} \) .
