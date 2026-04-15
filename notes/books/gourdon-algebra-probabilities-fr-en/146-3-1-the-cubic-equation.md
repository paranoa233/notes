#### 3.1. The cubic equation

*Français : 3.1. L'équation du troisième degré*

Notons \( \alpha ,\beta ,\gamma \) les racines de \( F = {z}^{3} + {pz} + q \) . Le polynôme \( {\left( X + jY + {j}^{2}Z\right) }^{3} \) ne prend que deux valeurs par toutes les permutations effectuées sur \( \alpha ,\beta ,\gamma \) , qui sont

> Let \( \alpha ,\beta ,\gamma \) be the roots of \( F = {z}^{3} + {pz} + q \). The polynomial \( {\left( X + jY + {j}^{2}Z\right) }^{3} \) takes only two values under all permutations performed on \( \alpha ,\beta ,\gamma \), which are

\[
A = {\left( \alpha  + j\beta  + {j}^{2}\gamma \right) }^{3}\text{ et }B = {\left( \alpha  + j\gamma  + {j}^{2}\beta \right) }^{3}.
\]

Compte tenu du théorème 1 de la page 64, on a

> Given Theorem 1 on page 64, we have

\[
{\sigma }_{1} = \alpha  + \beta  + \gamma  = 0,\;{\sigma }_{2} = {\alpha \beta } + {\beta \gamma } + {\gamma \alpha } = p,\;{\sigma }_{3} = {\alpha \beta \gamma } =  - q.
\]

Un calcul donne

> A calculation gives

\[
A + B = 2\left( {{\alpha }^{3} + {\beta }^{3} + {\gamma }^{3}}\right)  - 3\left( {{\alpha }^{2}\beta  + {\beta }^{2}\gamma  + {\gamma }^{2}\alpha  + {\alpha }^{2}\gamma  + {\beta }^{2}\alpha  + {\gamma }^{2}\beta }\right)  + {12\alpha \beta \gamma }
\]

\[
= 2\left( {{\sigma }_{1} - 3{\sigma }_{1}{\sigma }_{2} + 3{\sigma }_{3}}\right)  - 3\left( {{\sigma }_{1}{\sigma }_{2} - 3{\sigma }_{3}}\right)  + {12}{\sigma }_{3} =  - {27q}
\]

et

\[
{AB} = {\left( {\alpha }^{2} + {\beta }^{2} + {\gamma }^{2} - \alpha \beta  - \beta \gamma  - \gamma \alpha \right) }^{3} = {\left( {\sigma }_{1}^{2} - 2{\sigma }_{2} - {\sigma }_{2}\right) }^{3} =  - {27}{p}^{3}.
\]

Ainsi, \( A \) et \( B \) sont trouvées simplement comme solutions de

> Thus, \( A \) and \( B \) are found simply as solutions of

\[
{z}^{2} + {27qz} - {27}{p}^{3} = 0.
\]

(***)

> Si on note \( u \) (resp. \( v \) ) une racine cubique de \( A \) (resp. de \( B \) ), les déterminations étant choisies telles que \( {uv} = \left( {\alpha + {j\beta } + {j}^{2}\gamma }\right) \left( {\alpha + {j\gamma } + {j}^{2}\beta }\right) = - {3p} \) , on s’est ramené à résoudre le système

If we denote by \( u \) (resp. \( v \)) a cube root of \( A \) (resp. of \( B \)), with the determinations chosen such that \( {uv} = \left( {\alpha + {j\beta } + {j}^{2}\gamma }\right) \left( {\alpha + {j\gamma } + {j}^{2}\beta }\right) = - {3p} \), we have reduced the problem to solving the system

\[
\left\{  \begin{array}{l} \alpha  + \beta  + \gamma  = 0 \\  \alpha  + {j\beta } + {j}^{2}\gamma  = u\;\text{ dont les solutions sont }\left\{  \begin{array}{l} \alpha  = \frac{1}{3}\left( {u + v}\right) \\  \beta  = \frac{1}{3}\left( {u{j}^{2} + {vj}}\right) \\  \gamma  = \frac{1}{3}\left( {u{j}^{2} + {vj}}\right)  \end{array}\right. . \end{array}\right.
\]

Noter que le test du nombre de racines réelles s'effectue simplement grâce au discriminant de l’équation (***) qui est \( {27}\left( {4{p}^{3} + {27}{q}^{2}}\right) \) .

> Note that the test for the number of real roots is performed simply using the discriminant of equation (***), which is \( {27}\left( {4{p}^{3} + {27}{q}^{2}}\right) \).
