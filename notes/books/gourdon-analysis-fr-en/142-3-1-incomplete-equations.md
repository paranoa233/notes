#### 3.1. Incomplete equations

*Français : 3.1. Équations incomplètes*

On appelle ainsi les équations différentielles dans lesquelles \( x \) ou \( y \) ne figure pas.

> This is the name given to differential equations in which \( x \) or \( y \) does not appear.

Équations de la forme \( F\left( {x,{y}^{\prime }}\right) = 0 \) . On note \( \Gamma = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2} \mid F\left( {X, Y}\right) = 0}\right\} \) . Supposons connu un paramétrage de \( \Gamma \) de la forme \( t \mapsto \left( {\varphi \left( t\right) ,\psi \left( t\right) }\right) \) , où \( \varphi \) est un \( {\mathcal{C}}^{1} \) - difféomorphisme et où \( \psi \) est continue. L’équation \( F\left( {x,{y}^{\prime }}\right) = 0 \) s’écrit aussi

> Equations of the form \( F\left( {x,{y}^{\prime }}\right) = 0 \) . Let \( \Gamma = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2} \mid F\left( {X, Y}\right) = 0}\right\} \) . Suppose a parameterization of \( \Gamma \) is known in the form \( t \mapsto \left( {\varphi \left( t\right) ,\psi \left( t\right) }\right) \) , where \( \varphi \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism and where \( \psi \) is continuous. The equation \( F\left( {x,{y}^{\prime }}\right) = 0 \) can also be written

\[
\left\{  {\begin{matrix} x &  = \varphi \left( t\right) \\  {y}^{\prime } &  = \psi \left( t\right)  \end{matrix}\;\text{ donc }\;{dy} = \psi \left( t\right) {dx} = \psi \left( t\right) {\varphi }^{\prime }\left( t\right) {dt},}\right.
\]

et le graphe des solutions peut être paramétré par

> and the graph of the solutions can be parameterized by

\[
\left\{  {\begin{array}{l} x = \varphi \left( t\right) \\  y = {\int }_{{t}_{0}}^{t}\psi \left( u\right) {\varphi }^{\prime }\left( u\right) {du} + {y}_{0} \end{array}.}\right.
\]

Équations de la forme \( F\left( {y,{y}^{\prime }}\right) = 0 \) . Comme précédemment, on suppose connu un paramétrage de \( \Gamma = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2} \mid F\left( {X, Y}\right) = 0}\right\} \) de la forme \( t \mapsto \left( {\varphi \left( t\right) ,\psi \left( t\right) }\right) \) , où \( \varphi \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme et \( \psi \) est continue. Pour résoudre \( F\left( {y,{y}^{\prime }}\right) = 0 \) , on écrit

> Equations of the form \( F\left( {y,{y}^{\prime }}\right) = 0 \) . As before, we assume a parameterization of \( \Gamma = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2} \mid F\left( {X, Y}\right) = 0}\right\} \) of the form \( t \mapsto \left( {\varphi \left( t\right) ,\psi \left( t\right) }\right) \) is known, where \( \varphi \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism and \( \psi \) is continuous. To solve \( F\left( {y,{y}^{\prime }}\right) = 0 \) , we write

\[
\begin{cases} y = \varphi \left( t\right) \\  {y}^{\prime } = \psi \left( t\right)  \end{cases}\;\text{ donc }\;\left\{  \begin{array}{l} {dy} = {\varphi }^{\prime }\left( t\right) {dt} \\  {dy} = \psi \left( t\right) {dx} \end{array}\right. \;\text{ d’où }\;{dx} = \frac{{\varphi }^{\prime }\left( t\right) }{\psi \left( t\right) }{dt},
\]

puis on intègre, ce qui donne un paramétrage en \( t \) du graphe des solutions.

> then we integrate, which gives a parameterization in \( t \) of the graph of the solutions.

Remarque 1. Si \( \psi \) s’annule en un point \( {t}_{0} \) , la fonction \( t \mapsto \varphi \left( {t}_{0}\right) \) est solution. Elle peut se raccorder à des solutions dont la dérivée s'annule en \( {t}_{0} \) .

> Remark 1. If \( \psi \) vanishes at a point \( {t}_{0} \) , the function \( t \mapsto \varphi \left( {t}_{0}\right) \) is a solution. It can be joined to solutions whose derivative vanishes at \( {t}_{0} \) .

Équations de la forme \( F\left( {y,{y}^{\prime },{y}^{\prime \prime }}\right) = 0 \) . On cherche des solutions \( x \mapsto \varphi \left( x\right) \) telles que \( {\varphi }^{\prime } \) ne s’annule pas, de sorte que \( \varphi \) soit un \( {\mathcal{C}}^{2} \) -difféomorphisme.

> Equations of the form \( F\left( {y,{y}^{\prime },{y}^{\prime \prime }}\right) = 0 \) . We look for solutions \( x \mapsto \varphi \left( x\right) \) such that \( {\varphi }^{\prime } \) does not vanish, so that \( \varphi \) is a \( {\mathcal{C}}^{2} \) -diffeomorphism.

On cherche ensuite à paramétrer le graphe des solutions avec la variable \( y = \varphi \left( x\right) \) . On pose \( p = {y}^{\prime } \) et on regarde \( p \) comme une fonction de \( y \) . Comme

> We then seek to parameterize the graph of the solutions with the variable \( y = \varphi \left( x\right) \) . We set \( p = {y}^{\prime } \) and view \( p \) as a function of \( y \) . Since

\[
{y}^{\prime } = p\;\text{ et }\;{y}^{\prime \prime } = \frac{dp}{dx} = \frac{dy}{dx}\frac{dp}{dy} = {y}^{\prime }\frac{dp}{dy},
\]

la fonction \( p \) dépendante de \( y \) vérifie l’équation différentielle \( F\left( {y, p, p\frac{dp}{dy}}\right) = 0 \) ,équation du premier ordre en \( p \) . Si on sait la résoudre, on écrit \( {dx} = {dy}/p\left( y\right) \) puis par intégration, on en déduit \( x \) en fonction de \( y \) .

> the function \( p \) depending on \( y \) satisfies the differential equation \( F\left( {y, p, p\frac{dp}{dy}}\right) = 0 \) , a first-order equation in \( p \) . If we can solve it, we write \( {dx} = {dy}/p\left( y\right) \) then, by integration, we deduce \( x \) as a function of \( y \) .

Exemple 1. Pour résoudre l’équation \( \left( E\right) : {y}^{\prime \prime } + {\left( y{y}^{\prime }\right) }^{3} = 0 \) , on pose \( p = {y}^{\prime } \) , et on regarde \( p \) comme une fonction de \( y \) . L’équation \( \left( E\right) \) devient

> Example 1. To solve the equation \( \left( E\right) : {y}^{\prime \prime } + {\left( y{y}^{\prime }\right) }^{3} = 0 \) , we set \( p = {y}^{\prime } \) , and view \( p \) as a function of \( y \) . The equation \( \left( E\right) \) becomes

\[
p\frac{dp}{dy} + {\left( yp\right) }^{3} = 0\;\text{ donc }\;\frac{dp}{{p}^{2}} =  - {y}^{3}{dy},
\]

ce qui par intégration fournit \( 1/p = {y}^{4}/4 + \alpha ,\left( {\alpha \in \mathbb{R}}\right) \) ce qui entraîne

> which by integration provides \( 1/p = {y}^{4}/4 + \alpha ,\left( {\alpha \in \mathbb{R}}\right) \) , which leads to

\[
p = \frac{dy}{dx} = \frac{1}{{y}^{4}/4 + \alpha }\;\text{ ou encore }\;\left( {\frac{{y}^{4}}{4} + \alpha }\right) {dy} = {dx},
\]

donc après intégration, \( {y}^{5}/{20} + {\alpha y} + \beta = x\left( {\alpha ,\beta \in \mathbb{R}}\right) \) .

> therefore, after integration, \( {y}^{5}/{20} + {\alpha y} + \beta = x\left( {\alpha ,\beta \in \mathbb{R}}\right) \) .

Remarque 2. - S’il existe \( {y}_{0} \) tel que \( F\left( {{y}_{0},0,0}\right) = 0 \) , alors la fonction constante \( y = {y}_{0} \) est solution, et peut se raccorder avec les solutions trouvées précédemment.

> Remark 2. - If there exists \( {y}_{0} \) such that \( F\left( {{y}_{0},0,0}\right) = 0 \) , then the constant function \( y = {y}_{0} \) is a solution, and can be joined with the solutions found previously.

- La technique utilisée peut être généralisée aux équations incomplètes d'ordre \( n \) du type \( F\left( {y,{y}^{\prime },\ldots ,{y}^{\left( n\right) }}\right)  = 0 \) , pour abaisser d’une unité l’ordre de l’équation.

> - The technique used can be generalized to incomplete equations of order \( n \) of the type \( F\left( {y,{y}^{\prime },\ldots ,{y}^{\left( n\right) }}\right)  = 0 \) , to reduce the order of the equation by one.
