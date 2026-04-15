#### 2.1. Cardano's method for solving the cubic equation

*Français : 2.1. Méthode de Cardan pour la résolution de l'équation du troisième degré*

On veut résoudre l’équation \( {z}^{3} + {pz} + q = 0 \) . Si on pose \( z = u + v \) , l’équation sera vérifiée si

> We want to solve the equation \( {z}^{3} + {pz} + q = 0 \) . If we set \( z = u + v \) , the equation will be satisfied if

\[
{u}^{3} + {v}^{3} + 3{u}^{2}v + {3u}{v}^{2} + {pu} + {pv} + q = 0 = {u}^{3} + {v}^{3} + \left( {u + v}\right) \left( {{3uv} + p}\right)  + q = 0.
\]

Ceci sera vérifié si on a

> This will be satisfied if we have

\[
\left\{  \begin{array}{l} {u}^{3} + {v}^{3} =  - q \\  {uv} =  - p/3 \end{array}\right.
\]

c’est-à-dire si \( {u}^{3} + {v}^{3} = - q \) et \( {u}^{3}{v}^{3} = - {p}^{3}/{27} \) , les déterminations des racines cubiques de \( u \) et \( v \) étant choisies telles que \( {uv} = - p/3 \) . En d’autres termes, il suffit que \( {u}^{3} \) et \( {v}^{3} \) soient racines de

> that is to say if \( {u}^{3} + {v}^{3} = - q \) and \( {u}^{3}{v}^{3} = - {p}^{3}/{27} \) , the determinations of the cube roots of \( u \) and \( v \) being chosen such that \( {uv} = - p/3 \) . In other words, it suffices that \( {u}^{3} \) and \( {v}^{3} \) are roots of

\[
{z}^{2} + {qz} - \frac{{p}^{3}}{27} = 0\;\text{ avec }\;{uv} =  - p/3.
\]

(*)

> Si on note \( {z}_{1},{z}_{2} \) les racines de cette équation du second degré, si \( u \) et \( v \) sont des racines cubiques de \( {z}_{1} \) et \( {z}_{2} \) telles que \( {uv} = - p/3 \) , les racines recherchées sont alors

If we denote \( {z}_{1},{z}_{2} \) as the roots of this quadratic equation, if \( u \) and \( v \) are cube roots of \( {z}_{1} \) and \( {z}_{2} \) such that \( {uv} = - p/3 \) , the sought roots are then

\[
u + v,\;{uj} + v{j}^{2},\;u{j}^{2} + {vj}\;\text{ où }\;j = {e}^{{2i\pi }/3}.
\]

Lorsque \( \left( {p, q}\right) \in {\mathbb{R}}^{2} \) , le nombre de racines réelles de l’équation \( {z}^{3} + {pz} + q = 0 \) peut être discuté. Celui-ci dépend du signe du discriminant de l'équation du second degré (*), qui est du signe de \( 4{p}^{3} + {27}{q}^{2} \) . On montre facilement que

> When \( \left( {p, q}\right) \in {\mathbb{R}}^{2} \) , the number of real roots of the equation \( {z}^{3} + {pz} + q = 0 \) can be discussed. This depends on the sign of the discriminant of the quadratic equation (*), which has the sign of \( 4{p}^{3} + {27}{q}^{2} \) . It is easily shown that

(i) Si \( 4{p}^{3} + {27}{q}^{2} > 0 \) , il y a une racine réelle et deux racines complexes conjuguées.

> (i) If \( 4{p}^{3} + {27}{q}^{2} > 0 \) , there is one real root and two complex conjugate roots.

(ii) Si \( 4{p}^{3} + {27}{q}^{2} = 0 \) , il y a une racine triple0si \( q = 0 \) , une racine réelle double et une réelle simple si \( q \neq 0 \) .

> (ii) If \( 4{p}^{3} + {27}{q}^{2} = 0 \) , there is a triple root; if \( q = 0 \) , a double real root and a simple real root if \( q \neq 0 \) .

(iii) Si \( 4{p}^{3} + {27}{q}^{2} < 0 \) , il y a trois racines réelles. Ce dernier résultat est à rapprocher de celui de l'exercice 2 de la page 85.

> (iii) If \( 4{p}^{3} + {27}{q}^{2} < 0 \) , there are three real roots. This last result is to be compared with that of exercise 2 on page 85.
