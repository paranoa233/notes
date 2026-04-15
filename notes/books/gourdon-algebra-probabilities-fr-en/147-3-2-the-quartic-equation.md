#### 3.2. The quartic equation

*Français : 3.2. L'équation du quatrième degré*

On note \( \alpha ,\beta ,\gamma ,\delta \) les racines de \( F = {z}^{4} + a{z}^{2} + {bz} + c \) . Le polynôme \( {XY} + {ZT} \) ne prend que trois valeurs par toutes les permutations effectuées sur \( \alpha ,\beta ,\gamma ,\delta \) , qui sont

> Let \( \alpha ,\beta ,\gamma ,\delta \) be the roots of \( F = {z}^{4} + a{z}^{2} + {bz} + c \). The polynomial \( {XY} + {ZT} \) takes only three values under all permutations performed on \( \alpha ,\beta ,\gamma ,\delta \), which are

\[
A = {\alpha \beta } + {\gamma \delta },\;B = {\alpha \gamma } + {\beta \delta },\;C = {\alpha \delta } + {\beta \gamma }.
\]

Ici, les fonctions symétriques des racines de \( F \) valent respectivement \( {\sigma }_{1} = 0,{\sigma }_{2} = a \) , \( {\sigma }_{3} = - b \) et \( {\sigma }_{4} = c \) . Les calculs qui suivent sont légèrement plus simples que ceux de la partie précédente.

> Here, the symmetric functions of the roots of \( F \) are equal to \( {\sigma }_{1} = 0,{\sigma }_{2} = a \), \( {\sigma }_{3} = - b \), and \( {\sigma }_{4} = c \) respectively. The following calculations are slightly simpler than those in the previous section.

\[
A + B + C = {\sigma }_{2} = a,
\]

\[
{AB} + {BC} + {CA} = {\sigma }_{1}{\sigma }_{3} - 4{\sigma }_{4} =  - {4c}
\]

et

\[
{ABC} = \left( {{\sigma }_{1}^{2} - 2{\sigma }_{2}}\right) {\sigma }_{4} + {\sigma }_{3}^{2} - 2{\sigma }_{2}{\sigma }_{4} = {b}^{2} - {4ac}.
\]

Ainsi \( A, B \) et \( C \) sont obtenus comme solutions de l’équation

> Thus \( A, B \) and \( C \) are obtained as solutions of the equation

\[
{z}^{3} - a{z}^{2} - {4cz} - {b}^{2} + {4ac} = 0,
\]

que l’on sait désormais résoudre. Si on note \( u, v, w \) ses racines, on est ramené à résoudre le système

> which we now know how to solve. If we denote its roots by \( u, v, w \), we are reduced to solving the system

\[
\begin{cases} \alpha  + \beta  + \gamma  + \delta &  = 0 \\  {\alpha \beta } + {\gamma \delta } &  = u \\  {\alpha \gamma } + {\beta \delta } &  = v \\  {\alpha \delta } + {\beta \gamma } &  = w \end{cases}\text{ qui équivaut à }\begin{cases} \alpha  + \beta  + \gamma  + \delta &  = 0 \\  \left( {\alpha  + \beta }\right) \left( {\gamma  + \delta }\right) &  = v + w \\  \left( {\alpha  + \delta }\right) \left( {\beta  + \gamma }\right) &  = u + v \\  \left( {\alpha  + \gamma }\right) \left( {\beta  + \delta }\right) &  = u + w \end{cases}
\]

à l'aide de deux premières équations de ce dernier système, on trouve

> using the first two equations of this latter system, we find

\[
\alpha  + \beta  = {\rho }_{1}\;\text{ et }\;\gamma  + \delta  =  - {\rho }_{1},\;\text{ où }\;{\rho }_{1} = \sqrt{-v - w},
\]

de même avec la première et la troisième équation

> likewise with the first and third equations

\[
\alpha  + \delta  = {\rho }_{2}\;\text{ et }\;\beta  + \gamma  =  - {\rho }_{2},\;\text{ où }\;{\rho }_{2} = \sqrt{-u - v}
\]

et avec la première et la dernière équation,

> and with the first and last equation,

\[
\alpha  + \gamma  = {\rho }_{3}\;\text{ et }\;\beta  + \delta  =  - {\rho }_{3},\;\text{ où }\;{\rho }_{3} = \sqrt{-u - w}.
\]

Pour qu'il y ait équivalence entre ces trois dernières assertions et le système précédent, il faut et il suffit que les déterminations des racines carrées \( {\rho }_{1},{\rho }_{2},{\rho }_{3} \) soient choisies de sorte que \( {\rho }_{1}{\rho }_{2}{\rho }_{3} = - b \) , compte tenu du fait que

> For there to be equivalence between these last three assertions and the previous system, it is necessary and sufficient that the determinations of the square roots \( {\rho }_{1},{\rho }_{2},{\rho }_{3} \) be chosen such that \( {\rho }_{1}{\rho }_{2}{\rho }_{3} = - b \) , given the fact that

\[
\left( {\alpha  + \beta }\right) \left( {\alpha  + \gamma }\right) \left( {\alpha  + \delta }\right)  = {\alpha }^{2}\left( {\alpha  + \beta  + \gamma  + \delta }\right)  + {\sigma }_{3} =  - b.
\]

Maintenant, on en déduit facilement que les solutions sont

> Now, we easily deduce that the solutions are

\[
\alpha  = \frac{1}{2}\left( {{\rho }_{1} + {\rho }_{2} + {\rho }_{3}}\right) ,\;\beta  = \frac{1}{2}\left( {{\rho }_{1} - {\rho }_{2} - {\rho }_{3}}\right) ,\;\gamma  = \frac{1}{2}\left( {-{\rho }_{1} - {\rho }_{2} + {\rho }_{3}}\right) ,\;\delta  = \frac{1}{2}\left( {-{\rho }_{1} + {\rho }_{2} - {\rho }_{3}}\right) .
\]
