#### 4.3. Exercises

*Français : 4.3. Exercices*

EXERCICE 1. Exprimer les polynômes \( P \) suivants comme un polynôme \( \Phi \) en les polynômes symétriques élémentaires \( {\sigma }_{i} \) .

> EXERCISE 1. Express the following polynomials \( P \) as a polynomial \( \Phi \) in the elementary symmetric polynomials \( {\sigma }_{i} \) .

a) \( P = {X}^{3} + {Y}^{3} + {Z}^{3} \in \mathbb{R}\left\lbrack {X, Y, Z}\right\rbrack \) .

> b) \( P = \sum {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \in \mathbb{R}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) pour \( n \geq 5 \) .

b) \( P = \sum {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \in \mathbb{R}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) for \( n \geq 5 \) .

> Solution. a) On a \( {\left( X + Y + Z\right) }^{3} = {X}^{3} + {Y}^{3} + {Z}^{3} + 3{X}^{2}Y + 3{X}^{2}Z + 3{Y}^{2}X + 3{Y}^{2}Z + 3{Z}^{2}X + \; 3{Z}^{2}Y + {6XYZ} \) , et donc \( {X}^{3} + {Y}^{3} + {Z}^{3} = {\sum }_{1}^{3} - 6{\sum }_{3} - 3\sum {X}^{2}Y \) . Or \( \sum {X}^{2}Y = {\sum }_{1}{\sum }_{2} - 3{\sum }_{3} \) . Finalement, on a \( P = {\sum }_{1}^{3} - 3{\sum }_{1}{\sum }_{2} + 3{\sum }_{3} \) .

Solution. We have \( {\left( X + Y + Z\right) }^{3} = {X}^{3} + {Y}^{3} + {Z}^{3} + 3{X}^{2}Y + 3{X}^{2}Z + 3{Y}^{2}X + 3{Y}^{2}Z + 3{Z}^{2}X + \; 3{Z}^{2}Y + {6XYZ} \) , and thus \( {X}^{3} + {Y}^{3} + {Z}^{3} = {\sum }_{1}^{3} - 6{\sum }_{3} - 3\sum {X}^{2}Y \) . However, \( \sum {X}^{2}Y = {\sum }_{1}{\sum }_{2} - 3{\sum }_{3} \) . Finally, we have \( P = {\sum }_{1}^{3} - 3{\sum }_{1}{\sum }_{2} + 3{\sum }_{3} \) .

> b) Rappelons que la méthode générale (méthode de Waring) pour trouver le polynôme \( \Phi \) consiste à faire diminuer la hauteur de \( P \) (la hauteur de \( P \) est la plus grande des hauteurs de ses monômes, la hauteur d’un monôme \( a{X}_{1}^{{\alpha }_{1}}\cdots {X}_{n}^{{\alpha }_{n}} \) étant \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) , ordonnée par l’ordre lexicographique).

b) Recall that the general method (Waring's method) for finding the polynomial \( \Phi \) consists of decreasing the height of \( P \) (the height of \( P \) is the largest of the heights of its monomials, the height of a monomial \( a{X}_{1}^{{\alpha }_{1}}\cdots {X}_{n}^{{\alpha }_{n}} \) being \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) , ordered by lexicographical order).

> Ici, le monôme le plus haut de \( P \) est \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) . On va donc commencer par retrancher \( P \) à \( \left( {\sum {X}_{1}{X}_{2}}\right) \left( {\sum {X}_{1}{X}_{2}{X}_{3}}\right) = {\sum }_{2}{\sum }_{3} \) . Calculons ce dernier terme. Chaque monôme de \( {\sum }_{2}{\sum }_{3} \) est de degré total 5 (produit de deux monômes de degré total 2 et 3) et est moins haut que \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) . On peut donc écrire

Here, the highest monomial of \( P \) is \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) . We will therefore start by subtracting \( P \) from \( \left( {\sum {X}_{1}{X}_{2}}\right) \left( {\sum {X}_{1}{X}_{2}{X}_{3}}\right) = {\sum }_{2}{\sum }_{3} \) . Let us calculate this last term. Each monomial of \( {\sum }_{2}{\sum }_{3} \) has a total degree of 5 (product of two monomials of total degree 2 and 3) and is lower than \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) . We can therefore write

\[
\exists a, b, c,\;{\sum }_{2}{\sum }_{3} = a\sum {X}_{1}^{2}{X}_{2}^{2}{X}_{3} + b\sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} + c\sum {X}_{1}{X}_{2}{X}_{3}{X}_{4}{X}_{5}.
\]

Le nombre \( a \) est le coefficient de \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) dans \( {\sum }_{2}{\sum }_{3} \) . C’est donc le nombre de manières de former \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) par un monôme de \( {\sum }_{2} \) multiplié par un monôme de \( {\sum }_{3} \) . Il n’y a qu’une seule façon de faire ceci. C’est \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} = \left( {{X}_{1}{X}_{2}}\right) \left( {{X}_{1}{X}_{2}{X}_{3}}\right) \) , donc \( a = 1 \) .

> The number \( a \) is the coefficient of \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) in \( {\sum }_{2}{\sum }_{3} \) . It is therefore the number of ways to form \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} \) by a monomial of \( {\sum }_{2} \) multiplied by a monomial of \( {\sum }_{3} \) . There is only one way to do this. It is \( {X}_{1}^{2}{X}_{2}^{2}{X}_{3} = \left( {{X}_{1}{X}_{2}}\right) \left( {{X}_{1}{X}_{2}{X}_{3}}\right) \) , so \( a = 1 \) .

- De même, on a \( b = 3 \) car les façons d’écrire \( {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} \) comme le produit d’un monôme de \( {\sum }_{2} \) par un monôme de \( {\sum }_{3} \) sont

> - Similarly, we have \( b = 3 \) because the ways to write \( {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} \) as the product of a monomial of \( {\sum }_{2} \) by a monomial of \( {\sum }_{3} \) are

\[
{X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} = \left( {{X}_{1}{X}_{2}}\right) \left( {{X}_{1}{X}_{3}{X}_{4}}\right)  = \left( {{X}_{1}{X}_{3}}\right) \left( {{X}_{1}{X}_{2}{X}_{4}}\right)  = \left( {{X}_{1}{X}_{4}}\right) \left( {{X}_{1}{X}_{2}{X}_{3}}\right) .
\]

- On trouve de même \( c = \left( \begin{array}{l} 5 \\  2 \end{array}\right)  = {10} \) .

> - We find similarly \( c = \left( \begin{array}{l} 5 \\  2 \end{array}\right)  = {10} \) .

- Finalement, on a \( P - {\sum }_{2}{\sum }_{3} =  - 3\sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} - {10}\sum {X}_{1}{X}_{2}{X}_{3}{X}_{4}{X}_{5} \) . Par des méthodes analogues aux précédentes, on trouve

> - Finally, we have \( P - {\sum }_{2}{\sum }_{3} =  - 3\sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} - {10}\sum {X}_{1}{X}_{2}{X}_{3}{X}_{4}{X}_{5} \) . By methods analogous to the previous ones, we find

\[
{\sum }_{1}{\sum }_{4} = \sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} + 5\sum {X}_{1}{X}_{2}{X}_{3}{X}_{4}{X}_{5},
\]

et donc \( \sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} = {\sum }_{1}{\sum }_{4} - 5{\sum }_{5} \) . Finalement, on a

> and therefore \( \sum {X}_{1}^{2}{X}_{2}{X}_{3}{X}_{4} = {\sum }_{1}{\sum }_{4} - 5{\sum }_{5} \) . Finally, we have

\[
P = {\sum }_{2}{\sum }_{3} - 3\left( {{\sum }_{1}{\sum }_{4} - 5{\sum }_{5}}\right)  - {10}{\sum }_{5} = {\sum }_{2}{\sum }_{3} - 3{\sum }_{1}{\sum }_{4} + 5{\sum }_{5}.
\]

Remarque. Il est conseillé dans ce type de calcul de vérifier les résultats, en donnant par exemple à \( n,{X}_{1},\ldots ,{X}_{n} \) des valeurs particulières.

> Remark. It is advisable in this type of calculation to verify the results, for example by giving \( n,{X}_{1},\ldots ,{X}_{n} \) particular values.

EXERCICE 2. Soit \( P = {X}^{3} + {pX} + q \in \mathbb{R}\left\lbrack X\right\rbrack \) et \( \alpha ,\beta ,\gamma \) ses racines complexes.

> EXERCISE 2. Let \( P = {X}^{3} + {pX} + q \in \mathbb{R}\left\lbrack X\right\rbrack \) and \( \alpha ,\beta ,\gamma \) be its complex roots.

a) Calculer \( \Delta = {\left( \alpha - \beta \right) }^{2}{\left( \beta - \gamma \right) }^{2}{\left( \gamma - \alpha \right) }^{2} \) en fonction de \( p \) et \( q \) .

> a) Calculate \( \Delta = {\left( \alpha - \beta \right) }^{2}{\left( \beta - \gamma \right) }^{2}{\left( \gamma - \alpha \right) }^{2} \) in terms of \( p \) and \( q \) .

b) En déduire une condition nécessaire et suffisante portant sur \( p \) et \( q \) pour que \( P \) ait trois racines réelles.

> b) Deduce a necessary and sufficient condition on \( p \) and \( q \) for \( P \) to have three real roots.

Solution. a) Posons \( {\sigma }_{1} = \alpha + \beta + \gamma ,{\sigma }_{2} = {\alpha \beta } + {\beta \gamma } + {\gamma \alpha },{\sigma }_{3} = {\alpha \beta \gamma } \) . La relation entre coefficients et racines d’un polynôme (voir le théorème 1 page 64) donne \( {\sigma }_{1} = 0,{\sigma }_{2} = p \) et \( {\sigma }_{3} = - q \) .

> Solution. a) Let \( {\sigma }_{1} = \alpha + \beta + \gamma ,{\sigma }_{2} = {\alpha \beta } + {\beta \gamma } + {\gamma \alpha },{\sigma }_{3} = {\alpha \beta \gamma } \) . The relationship between coefficients and roots of a polynomial (see theorem 1 page 64) gives \( {\sigma }_{1} = 0,{\sigma }_{2} = p \) and \( {\sigma }_{3} = - q \) .

Comme \( \Delta \) est symétrique en \( \alpha ,\beta ,\gamma \) , on peut l’exprimer comme un polynôme en \( {\sigma }_{1},{\sigma }_{2},{\sigma }_{3} \) . Plutôt que de calculer directement ce polynôme (les manipulations sont lourdes), nous allons utiliser une technique dont les calculs sont plus simples.

> Since \( \Delta \) is symmetric in \( \alpha ,\beta ,\gamma \), it can be expressed as a polynomial in \( {\sigma }_{1},{\sigma }_{2},{\sigma }_{3} \). Rather than calculating this polynomial directly (the manipulations are cumbersome), we will use a technique with simpler calculations.

Supposons dans un premier temps \( q \neq 0 \) , c’est-à-dire \( {\alpha \beta \gamma } = {\sigma }_{3} \neq 0 \) , de sorte que \( \alpha ,\beta \) et \( \gamma \) sont non nuls. On a \( {\left( \alpha - \beta \right) }^{2} = {\alpha }^{2} + {\beta }^{2} - {2\alpha \beta } \) . Or \( {\alpha }^{2} + {\beta }^{2} + {\gamma }^{2} = {\sigma }_{1}^{2} - 2{\sigma }_{2} = - {2p} \) , donc

> Assume initially \( q \neq 0 \), that is \( {\alpha \beta \gamma } = {\sigma }_{3} \neq 0 \), such that \( \alpha ,\beta \) and \( \gamma \) are non-zero. We have \( {\left( \alpha - \beta \right) }^{2} = {\alpha }^{2} + {\beta }^{2} - {2\alpha \beta } \). However, \( {\alpha }^{2} + {\beta }^{2} + {\gamma }^{2} = {\sigma }_{1}^{2} - 2{\sigma }_{2} = - {2p} \), therefore

\[
{\left( \alpha  - \beta \right) }^{2} =  - {2p} - {\gamma }^{2} - {2\alpha \beta } =  - {2p} - {\gamma }^{2} + \frac{2q}{\gamma }.
\]

On montrerait de même

> We would show similarly

\[
{\left( \beta  - \gamma \right) }^{2} =  - {2p} - {\alpha }^{2} + \frac{2q}{\alpha }\;\text{ et }\;{\left( \gamma  - \alpha \right) }^{2} =  - {2p} - {\beta }^{2} + \frac{2p}{\beta }.
\]

Finalement, on a

> Finally, we have

\[
\Delta  = \mathop{\prod }\limits_{{x\text{ racine de }P}}\left( {-{2p} - {x}^{2} + \frac{2q}{x}}\right) .
\]

Recherchons un polynôme \( Q \) dont les racines sont les \( y = - {2p} - {x}^{2} + {2q}/x\left( {x = \alpha ,\beta ,\gamma }\right) \) .

> Let us look for a polynomial \( Q \) whose roots are the \( y = - {2p} - {x}^{2} + {2q}/x\left( {x = \alpha ,\beta ,\gamma }\right) \).

\[
\left\{  {\begin{aligned} {x}^{3} + {px} + q &  = 0 \\   - {2p} - {x}^{2} + {2q}/x &  = y \end{aligned} \Leftrightarrow  \left\{  {\begin{aligned} {x}^{2} &  = &  - p - q/x \\  y &  = &  - p + {3q}/x \end{aligned} \Leftrightarrow  \left\{  \begin{array}{lll} 0 &  = & 1 + p/{x}^{2} + q/{x}^{3} \\  x &  = & {3q}/\left( {y + p}\right)  \end{array}\right. }\right. }\right.
\]

\[
\Leftrightarrow  1 + p{\left( \frac{y + p}{3q}\right) }^{2} + q{\left( \frac{y + p}{3q}\right) }^{3} = 0 \Leftrightarrow  {y}^{3} + {6p}{y}^{2} + 9{p}^{2}y + \left( {4{p}^{3} + {27}{q}^{2}}\right)  = 0.
\]

Donc \( Q = {X}^{3} + {6p}{X}^{2} + 9{p}^{2}X + \left( {4{p}^{3} + {27}{q}^{2}}\right) \) . Le nombre \( \Delta \) apparaissant comme le produit des racines de \( Q \) , on en déduit \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \) .

> Thus \( Q = {X}^{3} + {6p}{X}^{2} + 9{p}^{2}X + \left( {4{p}^{3} + {27}{q}^{2}}\right) \). The number \( \Delta \) appearing as the product of the roots of \( Q \), we deduce \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \).

Ceci est vrai pour \( q \neq 0 \) . Si \( q = 0 \) , alors une des racines de \( P \) est nulle, par exemple \( \alpha \) , et alors \( \Delta = {\beta }^{2}{\gamma }^{2}{\left( \beta - \gamma \right) }^{2} \) . Or \( {\sigma }_{1} = 0 = \beta + \gamma \) , donc \( \gamma = - \beta \) et donc \( \Delta = {\beta }^{4} \cdot {\left( 2\beta \right) }^{2} = 4{\beta }^{6} \) . Il ne reste plus qu’à remarquer que \( p = {\sigma }_{2} = {\beta \gamma } = - {\beta }^{2} \) , et donc \( \Delta = - 4{p}^{3} \) .

> This is true for \( q \neq 0 \). If \( q = 0 \), then one of the roots of \( P \) is zero, for example \( \alpha \), and then \( \Delta = {\beta }^{2}{\gamma }^{2}{\left( \beta - \gamma \right) }^{2} \). However, \( {\sigma }_{1} = 0 = \beta + \gamma \), so \( \gamma = - \beta \) and therefore \( \Delta = {\beta }^{4} \cdot {\left( 2\beta \right) }^{2} = 4{\beta }^{6} \). It only remains to note that \( p = {\sigma }_{2} = {\beta \gamma } = - {\beta }^{2} \), and thus \( \Delta = - 4{p}^{3} \).

Finalement, dans tous les cas, \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \) .

> Finally, in all cases, \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \).

b) Le polynôme \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) est de degré impair et admet donc au moins une racine dans \( \mathbb{R} \) (c’est classique ! Comme \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}P\left( x\right) P\left( {-x}\right) = - \infty \) , il existe \( a > 0 \) tel que \( P\left( a\right) \) et \( P\left( {-a}\right) \) aient des signes opposés, et \( P \) étant continue, il existe \( x \in \rbrack - a, a\left\lbrack \right. \) tel que \( P\left( x\right) = 0 \) d’après le théorème des valeurs intermédiaires). Notons par exemple \( \alpha \) une telle racine réelle. Deux cas se présentent.

> b) The polynomial \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) is of odd degree and therefore admits at least one root in \( \mathbb{R} \) (this is standard! Since \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}P\left( x\right) P\left( {-x}\right) = - \infty \), there exists \( a > 0 \) such that \( P\left( a\right) \) and \( P\left( {-a}\right) \) have opposite signs, and \( P \) being continuous, there exists \( x \in \rbrack - a, a\left\lbrack \right. \) such that \( P\left( x\right) = 0 \) according to the intermediate value theorem). Let us denote, for example, \( \alpha \) as such a real root. Two cases arise.

- Premier cas. \( \beta \) et \( \gamma \) sont réelles. Alors \( \Delta  = {\left( \alpha  - \beta \right) }^{2}{\left( \beta  - \alpha \right) }^{2}{\left( \gamma  - \alpha \right) }^{2} \geq  0 \) .

> - First case. \( \beta \) and \( \gamma \) are real. Then \( \Delta  = {\left( \alpha  - \beta \right) }^{2}{\left( \beta  - \alpha \right) }^{2}{\left( \gamma  - \alpha \right) }^{2} \geq  0 \) .

- Second cas. \( \beta \) et \( \gamma \) sont non réelles. Alors elles sont complexes conjuguées. Autrement dit, on peut écrire \( \beta  = x + {iy} \) et \( \gamma  = x - {iy} \) avec \( x, y \in  \mathbb{R}, y \neq  0 \) . On a alors

> - Second case. \( \beta \) and \( \gamma \) are non-real. Then they are complex conjugates. In other words, we can write \( \beta  = x + {iy} \) and \( \gamma  = x - {iy} \) with \( x, y \in  \mathbb{R}, y \neq  0 \) . We then have

\[
\Delta  = {\left( \left( \alpha  - \beta \right) \left( \alpha  - \gamma \right) \right) }^{2}{\left( \beta  - \gamma \right) }^{2} = {\left( {\left| \alpha  - \beta \right| }^{2}\right) }^{2}{\left( 2iy\right) }^{2} =  - 4{y}^{2}{\left| \alpha  - \beta \right| }^{4} < 0.
\]

Finalement, on voit que \( P \) a trois racines réelles si et seulement si \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \geq 0 \) .

> Finally, we see that \( P \) has three real roots if and only if \( \Delta = - \left( {4{p}^{3} + {27}{q}^{2}}\right) \geq 0 \) .

Remarque. Ce dernier résultat peut également s'obtenir à partir des formules de Cardan donnant les racines de \( P \) en fonction de ses coefficients (voir l’annexe A).

> Remark. This last result can also be obtained from Cardano's formulas giving the roots of \( P \) in terms of its coefficients (see Appendix A).

- Le nombre \( \Delta \) s’appelle le discriminant de \( P \) . De manière générale, pour tout polynôme \( Q \) de degré \( n \geq  2 \) dont on note \( {x}_{1},\ldots ,{x}_{n} \) les racines, le discriminant de \( Q \) est défini par \( \Delta  = \mathop{\prod }\limits_{{i < j}}{\left( {x}_{i} - {x}_{j}\right) }^{2} \) . Comme \( \Delta \) est symétrique en les \( {x}_{i} \) , il s’exprime comme un polynôme en les coefficients de \( Q \) . On voit par ailleurs que \( Q \) n’admet que des racines simples si et seulement si \( \Delta  \neq  0 \) .

> - The number \( \Delta \) is called the discriminant of \( P \) . In general, for any polynomial \( Q \) of degree \( n \geq  2 \) whose roots are denoted by \( {x}_{1},\ldots ,{x}_{n} \) , the discriminant of \( Q \) is defined by \( \Delta  = \mathop{\prod }\limits_{{i < j}}{\left( {x}_{i} - {x}_{j}\right) }^{2} \) . Since \( \Delta \) is symmetric in the \( {x}_{i} \) , it can be expressed as a polynomial in the coefficients of \( Q \) . We also see that \( Q \) has only simple roots if and only if \( \Delta  \neq  0 \) .

\( \rightarrow \) EXERCICE 3 (IDENTITÉS DE NEWTON). Soit un entier \( n \geq 2 \) . On appelle sommes de Newton les polynômes

> \( \rightarrow \) EXERCISE 3 (NEWTON'S IDENTITIES). Let \( n \geq 2 \) be an integer. The Newton sums are the polynomials

\[
{S}_{p} = \mathop{\sum }\limits_{{i = 1}}^{n}{X}_{i}^{p} \in  \mathbb{R}\left\lbrack  {{X}_{1},\ldots ,{X}_{n}}\right\rbrack
\]

Comme \( {S}_{p} \) est symétrique, il s’exprime comme polynôme en les polynômes symétriques élémentaires : \( {S}_{p} = {\Phi }_{p}\left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) \) . On se propose de donner des formules simples per-mettant de calculer le polynôme \( {\Phi }_{p} \) .

> Since \( {S}_{p} \) is symmetric, it can be expressed as a polynomial in the elementary symmetric polynomials: \( {S}_{p} = {\Phi }_{p}\left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) \) . We propose to provide simple formulas for calculating the polynomial \( {\Phi }_{p} \) .

a) Soit \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) . Pour tout \( p \in {\mathbb{N}}^{ * } \) , on pose \( {s}_{p} = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{p} \) et pour tout \( i \) , on pose \( {\sigma }_{i} = {\sum }_{i}\left( {{x}_{1},\ldots ,{x}_{n}}\right) ,{\sigma }_{i}^{\prime } = {\left( -1\right) }^{i}{\sigma }_{i} \) . Soit \( P = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {x}_{i}}\right) \) . En partant de l’identité \( {P}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{P}{X - {x}_{i}} \) , montrer

> a) Let \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) . For all \( p \in {\mathbb{N}}^{ * } \) , let \( {s}_{p} = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{p} \) and for all \( i \) , let \( {\sigma }_{i} = {\sum }_{i}\left( {{x}_{1},\ldots ,{x}_{n}}\right) ,{\sigma }_{i}^{\prime } = {\left( -1\right) }^{i}{\sigma }_{i} \) . Let \( P = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {x}_{i}}\right) \) . Starting from the identity \( {P}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{P}{X - {x}_{i}} \) , show

\[
\forall k,1 \leq  k \leq  n - 1,\;{S}_{k} - {\sum }_{1}{S}_{k - 1} + \cdots  + {\left( -1\right) }^{k - 1}{\sum }_{k - 1}{S}_{1} + {\left( -1\right) }^{k}k{\sum }_{k} = 0.
\]

(*)

> b) Pour tout \( p \in \mathbb{N} \) , donner une relation entre \( {S}_{n + p},{S}_{n + p - 1},\ldots ,{S}_{p} \) .

b) For all \( p \in \mathbb{N} \) , give a relation between \( {S}_{n + p},{S}_{n + p - 1},\ldots ,{S}_{p} \) .

> Solution. On a \( P = {X}^{n} + {\sigma }_{1}^{\prime }{X}^{n - 1} + \cdots + {\sigma }_{n - 1}^{\prime }X + {\sigma }_{n}^{\prime } \) . Pour tout \( i \) , la division euclidienne de \( P \) par \( X - {x}_{i} \) donne

Solution. We have \( P = {X}^{n} + {\sigma }_{1}^{\prime }{X}^{n - 1} + \cdots + {\sigma }_{n - 1}^{\prime }X + {\sigma }_{n}^{\prime } \) . For any \( i \) , the Euclidean division of \( P \) by \( X - {x}_{i} \) gives

\[
\frac{P}{X - {x}_{i}} = {X}^{n - 1} + \left( {{x}_{i} + {\sigma }_{1}^{\prime }}\right) {X}^{n - 2} + \left( {{x}_{i}^{2} + {\sigma }_{1}^{\prime }{x}_{i} + {\sigma }_{2}^{\prime }}\right) {X}^{n - 3} + \cdots
\]

\[
\cdots  + \left( {{x}_{i}^{n - 1} + {\sigma }_{1}^{\prime }{x}_{i}^{n - 2} + \cdots  + {\sigma }_{n - 2}^{\prime }{x}_{i} + {\sigma }_{n - 1}^{\prime }}\right) .
\]

(**)

> En sommant l’égalité (**) pour \( 1 \leq i \leq n \) , on trouve

By summing the equality (**) for \( 1 \leq i \leq n \) , we find

\[
{P}^{\prime } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{P}{X - {x}_{i}} = n{X}^{n - 1} + \left( {{s}_{1} + n{\sigma }_{1}^{\prime }}\right) {X}^{n - 2} + \left( {{s}_{2} + {\sigma }_{1}^{\prime }{s}_{1} + n{\sigma }_{2}^{\prime }}\right) {X}^{n - 3} + \cdots
\]

\[
\cdots  + \left( {{s}_{n - 1} + {\sigma }_{1}^{\prime }{s}_{n - 2} + \cdots  + {\sigma }_{n - 2}^{\prime }{s}_{1} + n{\sigma }_{n - 1}^{\prime }}\right) .
\]

Or on sait que \( {P}^{\prime } = n{X}^{n - 1} + \left( {n - 1}\right) {\sigma }_{1}^{\prime }{X}^{n - 2} + \cdots + {\sigma }_{n - 1}^{\prime } \) . En identifiant les coefficients, on trouve

> However, we know that \( {P}^{\prime } = n{X}^{n - 1} + \left( {n - 1}\right) {\sigma }_{1}^{\prime }{X}^{n - 2} + \cdots + {\sigma }_{n - 1}^{\prime } \) . By identifying the coefficients, we find

\[
\forall k,1 \leq  k \leq  n - 1,\;{s}_{k} + {s}_{k - 1}{\sigma }_{1}^{\prime } + \cdots  + {s}_{1}{\sigma }_{k - 1}^{\prime } + k{\sigma }_{k}^{\prime } = 0.
\]

Autrement dit, si \( {P}_{k} = {S}_{k} - {S}_{k - 1}{\sum }_{1} + \cdots + {\left( -1\right) }^{k - 1}{S}_{1}{\sum }_{k - 1} + {\left( -1\right) }^{k}k{\sum }_{k} \) , on a \( {P}_{k}\left( {{x}_{1},\cdots ,{x}_{n}}\right) = 0 \) , et ceci pour tout \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) , donc \( {P}_{k} = 0\left( {1 \leq k \leq n - 1}\right) \) d’où le résultat.

> In other words, if \( {P}_{k} = {S}_{k} - {S}_{k - 1}{\sum }_{1} + \cdots + {\left( -1\right) }^{k - 1}{S}_{1}{\sum }_{k - 1} + {\left( -1\right) }^{k}k{\sum }_{k} \) , we have \( {P}_{k}\left( {{x}_{1},\cdots ,{x}_{n}}\right) = 0 \) , and this for all \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) , therefore \( {P}_{k} = 0\left( {1 \leq k \leq n - 1}\right) \) , hence the result.

b) Il suffit de remarquer que

> b) It suffices to note that

\[
\forall i,\;{x}_{i}^{p + n} + {\sigma }_{1}^{\prime }{x}_{i}^{p + n - 1} + \cdots  + {\sigma }_{n - 1}^{\prime }{x}_{i}^{p + 1} + {\sigma }_{n}^{\prime }{x}_{i}^{p} = {x}_{i}^{p}P\left( {x}_{i}\right)  = 0,
\]

et en sommant cette égalité pour \( 1 \leq i \leq n \) :

> and by summing this equality for \( 1 \leq i \leq n \) :

\[
{s}_{p + n} + {\sigma }_{1}^{\prime }{s}_{p + n - 1} + \cdots  + {\sigma }_{n - 1}^{\prime }{s}_{p + 1} + {\sigma }_{n}^{\prime }{s}_{p} = 0.
\]

Ceci étant vrai pour tout \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) , on en déduit que

> Since this is true for all \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) , we deduce that

\[
{S}_{p + n} - {\sum }_{1}{S}_{p + n - 1} + \cdots  + {\left( -1\right) }^{n - 1}{\sum }_{n - 1}{S}_{p + 1} + {\left( -1\right) }^{n}{\sum }_{n}{S}_{p} = 0.
\]

Remarque. En procédant par récurrence sur \( p \) , ces formules permettent de trouver fa-cilement les polynômes en \( {\sum }_{1},\ldots ,{\sum }_{n} \) égaux à \( {S}_{p} \) . Elles peuvent en particulier s’inverser (pour \( 1 \leq p \leq n \) ), ce qui prouve que les \( {\sum }_{i}\left( {1 \leq i \leq n}\right) \) s’expriment comme des polynômes en les \( {S}_{i}\left( {1 \leq i \leq n}\right) \) . Donc tout polynôme symétrique de \( \mathbb{R}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) peut s’exprimer comme un polynôme en les sommes de Newton \( {S}_{1},\ldots ,{S}_{n} \) .

> Remark. By proceeding by induction on \( p \) , these formulas allow for easily finding the polynomials in \( {\sum }_{1},\ldots ,{\sum }_{n} \) equal to \( {S}_{p} \) . They can in particular be inverted (for \( 1 \leq p \leq n \) ), which proves that the \( {\sum }_{i}\left( {1 \leq i \leq n}\right) \) can be expressed as polynomials in the \( {S}_{i}\left( {1 \leq i \leq n}\right) \) . Thus, any symmetric polynomial of \( \mathbb{R}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) can be expressed as a polynomial in the Newton sums \( {S}_{1},\ldots ,{S}_{n} \) .
