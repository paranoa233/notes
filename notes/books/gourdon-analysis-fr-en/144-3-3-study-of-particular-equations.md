#### 3.3. Study of particular equations

*Français : 3.3. Étude d'équations particulières*

Équations de Bernoulli. Il s'agit des équations différentielles du type

> Bernoulli equations. These are differential equations of the type

\[
{y}^{\prime } = a\left( t\right) y + b\left( t\right) {y}^{\alpha },\;\alpha  \in  \mathbb{R} \smallsetminus  \{ 0,1\} ,
\]

où \( a \) et \( b \) sont deux fonctions continues d’un intervalle \( J \) de \( \mathbb{R} \) dans \( \mathbb{R} \) (si \( \alpha = 0 \) ou \( \alpha = 1 \) , on a affaire à une équation linéaire, que l'on sait résoudre).

> where \( a \) and \( b \) are two continuous functions from an interval \( J \) of \( \mathbb{R} \) into \( \mathbb{R} \) (if \( \alpha = 0 \) or \( \alpha = 1 \) , we are dealing with a linear equation, which we know how to solve).

On cherche les solutions qui ne s’annulent pas (si \( \alpha \) n’est pas entier, on cherche les solutions > 0). L'équation peut s'écrire

> We look for solutions that do not vanish (if \( \alpha \) is not an integer, we look for solutions > 0). The equation can be written

\[
\frac{{y}^{\prime }}{{y}^{\alpha }} = a\left( t\right) \frac{1}{{y}^{\alpha  - 1}} + b\left( t\right) \;\text{ ou encore }\;\frac{1}{1 - \alpha }{z}^{\prime } = a\left( t\right) z + b\left( t\right) ,\;z = {y}^{1 - \alpha }.
\]

On s'est ainsi ramené à une équation linéaire d'ordre 1, que l'on sait résoudre.

> We have thus reduced it to a first-order linear equation, which we know how to solve.

Remarque 4. Si \( \alpha > 0 \) , la fonction nulle est solution. Si de plus \( \alpha \geq 1 \) , le théorème de Cauchy Lipschitz s’applique et montre qu’aucune autre solution ne s’annule ; si \( 0 < \alpha < 1 \) , on peut faire des raccords de classe \( {\mathcal{C}}^{1} \) avec la solution nulle.

> Remark 4. If \( \alpha > 0 \) , the zero function is a solution. If, in addition, \( \alpha \geq 1 \) , the Cauchy-Lipschitz theorem applies and shows that no other solution vanishes; if \( 0 < \alpha < 1 \) , we can perform connections of class \( {\mathcal{C}}^{1} \) with the zero solution.

Équations de Ricatti. Il s'agit des équations différentielles du type

> Riccati equations. These are differential equations of the type

\[
{y}^{\prime } = a\left( t\right) {y}^{2} + b\left( t\right) y + c\left( t\right) , \tag{R}
\]

où \( a, b \) et \( c \) sont des fonctions continues d’un intervalle de \( \mathbb{R} \) dans \( \mathbb{R} \) .

> where \( a, b \) and \( c \) are continuous functions from an interval of \( \mathbb{R} \) into \( \mathbb{R} \) .

Si on en connaît une solution particulière \( {\varphi }_{0} \) , on sait résoudre \( \left( R\right) \) : on pose \( y = {\varphi }_{0} + z \) , et en remplaçant dans \( \left( R\right) \) , on obtient

> If we know a particular solution \( {\varphi }_{0} \) , we know how to solve \( \left( R\right) \) : we set \( y = {\varphi }_{0} + z \) , and by substituting into \( \left( R\right) \) , we obtain

\[
{z}^{\prime } = \left\lbrack  {{2a}\left( t\right) {\varphi }_{0}\left( t\right)  + b\left( t\right) }\right\rbrack  z + a\left( t\right) {z}^{2},
\]

\( \left( {R}^{\prime }\right) \)

> (qui est une équation de Bernoulli).

(which is a Bernoulli equation).

> Le théorème de Cauchy Lipschitz montre qu'en dehors de la solution nulle, aucune solution de \( \left( {R}^{\prime }\right) \) ne s’annule. On peut donc poser \( z = 1/u \) , et on se ramène à une équation différentielle du premier ordre. Remarque 5. Ici, il n'y a pas de raccords de solutions à faire.

The Cauchy-Lipschitz theorem shows that, apart from the zero solution, no solution of \( \left( {R}^{\prime }\right) \) vanishes. We can therefore set \( z = 1/u \), and reduce it to a first-order differential equation. Remark 5. Here, there are no solution connections to be made.

> Équation de Lagrange. Il s'agit des équations différentielles du type

Lagrange equation. These are differential equations of the type

\[
y = a\left( {y}^{\prime }\right) t + b\left( {y}^{\prime }\right) ,
\]

où \( a \) et \( b \) sont des fonctions de classe \( {\mathcal{C}}^{1} \) sur un intervalle de \( \mathbb{R} \) .

> where \( a \) and \( b \) are functions of class \( {\mathcal{C}}^{1} \) on an interval of \( \mathbb{R} \).

On cherche d'abord les solutions affines. On voit facilement qu'elles sont de la forme \( t \mapsto {mt} + b\left( m\right) \) , avec \( a\left( m\right) = m \) .

> We first look for affine solutions. It is easy to see that they are of the form \( t \mapsto {mt} + b\left( m\right) \), with \( a\left( m\right) = m \).

On cherche ensuite les solutions de classe \( {\mathcal{C}}^{2} \) telle que \( {y}^{\prime \prime } \) ne s’annule pas. On recherche à paramétrer le graphe d’une telle solution avec la variable admissible \( p = {y}^{\prime } \) . En dérivant par rapport à \( t \) l’égalité \( y = a\left( p\right) t + b\left( p\right) \) , on obtient

> We then look for solutions of class \( {\mathcal{C}}^{2} \) such that \( {y}^{\prime \prime } \) does not vanish. We seek to parameterize the graph of such a solution with the admissible variable \( p = {y}^{\prime } \). By differentiating the equality \( y = a\left( p\right) t + b\left( p\right) \) with respect to \( t \), we obtain

\[
p = \frac{dy}{dt} = {a}^{\prime }\left( p\right) \frac{dp}{dt}t + a\left( p\right)  + {b}^{\prime }\left( p\right) \frac{dp}{dt}\;\text{ donc }\;\left\lbrack  {p - a\left( p\right) }\right\rbrack  \frac{dt}{dp} = {a}^{\prime }\left( p\right) t + {b}^{\prime }\left( p\right) .
\]

L’annulation de \( {y}^{\prime \prime } \) étant équivalente au fait que \( p = a\left( p\right) \) (on s’en rend compte en dérivant l'équation initiale), cette dernière équation différentielle est linéaire résolue du premier ordre tant que \( {y}^{\prime \prime } \) n’est pas nulle. On sait la résoudre, ce qui fournit la fonction \( p \mapsto t\left( p\right) \) , et on connaît alors \( y\left( p\right) \) grâce à l’équation initiale. Finalement, un paramétrage du graphe des solutions \( {\mathcal{C}}^{2} \) dont la dérivée seconde ne s’annule pas est \( p \mapsto \left( {t\left( p\right) , a\left( p\right) t\left( p\right) + b\left( p\right) }\right) \) .

> Since the vanishing of \( {y}^{\prime \prime } \) is equivalent to the fact that \( p = a\left( p\right) \) (as realized by differentiating the initial equation), this latter differential equation is a linear first-order equation as long as \( {y}^{\prime \prime } \) is not zero. We know how to solve it, which provides the function \( p \mapsto t\left( p\right) \), and we then know \( y\left( p\right) \) thanks to the initial equation. Finally, a parameterization of the graph of the solutions \( {\mathcal{C}}^{2} \) whose second derivative does not vanish is \( p \mapsto \left( {t\left( p\right) , a\left( p\right) t\left( p\right) + b\left( p\right) }\right) \).

Il ne reste plus qu’à effectuer des raccords de classe \( {\mathcal{C}}^{1} \) entre ces dernières solutions et les solutions affines.

> All that remains is to perform class \( {\mathcal{C}}^{1} \) connections between these latter solutions and the affine solutions.

Équation de Clairaut. Il s'agit des équations différentielles du type

> Clairaut equation. These are differential equations of the type

\[
y = {y}^{\prime }t + b\left( {y}^{\prime }\right) ,
\]

où \( b \) est une fonction de classe \( {\mathcal{C}}^{1} \) sur un intervalle de \( \mathbb{R} \) . Il s’agit d’un cas particulier dégénéré d’équation de Lagrange pour lequel \( a\left( m\right) = m \) pour tout \( m \) .

> where \( b \) is a function of class \( {\mathcal{C}}^{1} \) on an interval of \( \mathbb{R} \). This is a degenerate special case of the Lagrange equation for which \( a\left( m\right) = m \) for all \( m \).

Les solutions affines sont de la forme \( t \mapsto {mt} + b\left( m\right) , m \in I \) .

> The affine solutions are of the form \( t \mapsto {mt} + b\left( m\right) , m \in I \).

L’étude effectuée pour les équations de Lagrange montrent que les solutions \( {\mathcal{C}}^{2} \) dont la dérivée seconde ne s’annule pas peuvent se paramétrer sous la forme \( p \mapsto \left( {t\left( p\right) , y\left( {t\left( p\right) }\right) }\right) \) où \( t\left( p\right) = - {b}^{\prime }\left( p\right) \) et \( y\left( {t\left( p\right) }\right) = - p{b}^{\prime }\left( p\right) + b\left( p\right) \) .

> The study carried out for Lagrange equations shows that solutions \( {\mathcal{C}}^{2} \) whose second derivative does not vanish can be parameterized in the form \( p \mapsto \left( {t\left( p\right) , y\left( {t\left( p\right) }\right) }\right) \) where \( t\left( p\right) = - {b}^{\prime }\left( p\right) \) and \( y\left( {t\left( p\right) }\right) = - p{b}^{\prime }\left( p\right) + b\left( p\right) \).

L'arc ainsi paramétré possède la propriété suivante : les tangentes à cet arc sont aussi solution de l'équation différentielle (autrement dit, l'arc est l'enveloppe des solutions affines).

> The arc parameterized in this way has the following property: the tangents to this arc are also solutions to the differential equation (in other words, the arc is the envelope of the affine solutions).

Toutes les solutions s'obtiennent par raccordement des solutions des deux types.

> All solutions are obtained by connecting the solutions of the two types.
