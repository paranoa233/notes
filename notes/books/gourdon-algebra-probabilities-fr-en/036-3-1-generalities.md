#### 3.1. Generalities

*Français : 3.1. Généralités*

L’anneau \( \mathbb{K}\left\lbrack X\right\rbrack \) étant intègre, son corps des fractions existe bien. On le note \( \mathbb{K}\left( X\right) \) .

> Since the ring \( \mathbb{K}\left\lbrack X\right\rbrack \) is an integral domain, its field of fractions exists. It is denoted by \( \mathbb{K}\left( X\right) \).

Proposition 1. Soit \( F \in \mathbb{K}\left( X\right) , F \neq 0 \) . On peut écrire \( F = P/Q \) avec \( P \) et \( Q \in \mathbb{K}\left\lbrack X\right\rbrack , Q \) unitaire, \( P \) et \( Q \) premiers entre eux, et ceci de manière unique. L’écriture \( P/Q \) s’appelle la forme réduite \( {de}F \) .

> Proposition 1. Let \( F \in \mathbb{K}\left( X\right) , F \neq 0 \). We can write \( F = P/Q \) with \( P \) and \( Q \in \mathbb{K}\left\lbrack X\right\rbrack , Q \) monic, \( P \) and \( Q \) coprime, and this is unique. The expression \( P/Q \) is called the reduced form of \( {de}F \).

DéFINITION 1. Soit \( F \in \mathbb{K}\left( X\right) , F \neq 0, F = N/D \) sa forme réduite. Un élément \( a \in \mathbb{K} \) est dit pôle de \( F \) d’ordre \( h \) si \( a \) est racine de \( D \) d’ordre \( h \) .

> DEFINITION 1. Let \( F \in \mathbb{K}\left( X\right) , F \neq 0, F = N/D \) be its reduced form. An element \( a \in \mathbb{K} \) is called a pole of \( F \) of order \( h \) if \( a \) is a root of \( D \) of order \( h \).

De la même que pour les fonctions polynômes, on peut associer à toute fraction ra-tionnelle \( F = N/D \) une fonction rationnelle définie en tout point \( x \) de \( \mathbb{K} \) qui n’est pas un pôle de \( F \) , par \( x \mapsto F\left( x\right) = N\left( x\right) /D\left( x\right) \) . Si \( F, G \in \mathbb{K}\left( X\right) \) et \( x \in \mathbb{K} \) n’est pas pôle de \( F \) ou \( G \) , on a \( \left( {F + G}\right) \left( x\right) = F\left( x\right) + G\left( x\right) ,\left( {FG}\right) \left( x\right) = F\left( x\right) G\left( x\right) < \) .

> Just as with polynomial functions, we can associate with any rational fraction \( F = N/D \) a rational function defined at every point \( x \) of \( \mathbb{K} \) that is not a pole of \( F \), by \( x \mapsto F\left( x\right) = N\left( x\right) /D\left( x\right) \). If \( F, G \in \mathbb{K}\left( X\right) \) and \( x \in \mathbb{K} \) is not a pole of \( F \) or \( G \), we have \( \left( {F + G}\right) \left( x\right) = F\left( x\right) + G\left( x\right) ,\left( {FG}\right) \left( x\right) = F\left( x\right) G\left( x\right) < \).

\( \rightarrow \) THÉORÉME 1 (DÉCOMPOSITION EN ÉLÉMENTS SIMPLES). Soit \( F \in \mathbb{K}\left( X\right) , F \neq 0, N/D \) sa forme réduite. Soit \( D = {D}_{1}^{{\alpha }_{1}}\cdots {D}_{n}^{{\alpha }_{n}} \) la décomposition de \( D \) en facteurs irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) . On peut écrire, de manière unique

> \( \rightarrow \) THEOREM 1 (PARTIAL FRACTION DECOMPOSITION). Let \( F \in \mathbb{K}\left( X\right) , F \neq 0, N/D \) be its reduced form. Let \( D = {D}_{1}^{{\alpha }_{1}}\cdots {D}_{n}^{{\alpha }_{n}} \) be the decomposition of \( D \) into irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \). We can write, uniquely

\[
F = E + \mathop{\sum }\limits_{{i = 1}}^{n}\left( {\mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{A}_{i, j}}{{D}_{i}^{j}}}\right)
\]

avec \( E \in \mathbb{K}\left\lbrack X\right\rbrack ,{A}_{i, j} \in \mathbb{K}\left\lbrack X\right\rbrack \) et \( \deg \left( {A}_{i, j}\right) < \deg \left( {D}_{i}\right) \) . Le polynôme \( E \) s’appelle la partie entière de \( F \) et s’obtient comme le quotient de la division euclidienne de \( N \) par \( D \) .

> with \( E \in \mathbb{K}\left\lbrack X\right\rbrack ,{A}_{i, j} \in \mathbb{K}\left\lbrack X\right\rbrack \) and \( \deg \left( {A}_{i, j}\right) < \deg \left( {D}_{i}\right) \). The polynomial \( E \) is called the polynomial part of \( F \) and is obtained as the quotient of the Euclidean division of \( N \) by \( D \).

Les deux parties suivantes s'attachent à donner des méthodes de calcul des éléments simples \( {A}_{i, j}/{D}_{i}^{j} \) pour \( \mathbb{K} = \mathbb{C} \) et \( \mathbb{K} = \mathbb{R} \) .

> The following two parts focus on providing methods for calculating the partial fractions \( {A}_{i, j}/{D}_{i}^{j} \) for \( \mathbb{K} = \mathbb{C} \) and \( \mathbb{K} = \mathbb{R} \).
