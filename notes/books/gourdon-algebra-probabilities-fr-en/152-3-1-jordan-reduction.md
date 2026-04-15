#### 3.1. Jordan reduction

*Français : 3.1. Réduction de Jordan*

Une fois que l'on sait réduire un endomorphisme nilpotent sous forme de Jordan, il n'est pas difficile de trouver la réduction de Jordan d'un endomorphisme quelconque (voir le théorème 5, page 209). Comme nous allons le voir, cette première tâche peut être réalisée au moyen de la théorie des invariants de similitude.

> Once one knows how to reduce a nilpotent endomorphism into Jordan form, it is not difficult to find the Jordan reduction of any endomorphism (see theorem 5, page 209). As we shall see, this first task can be accomplished by means of the theory of similarity invariants.

Soit \( f \in \mathcal{L}\left( E\right) \) un endomorphisme nilpotent. Désignons par \( {P}_{1},\ldots ,{P}_{r} \) la suite des invariants de similitude de \( f \) . Le produit \( {P}_{1}\cdots {P}_{r} \) est au signe près le polynôme carac-téristique de \( f \) , qui est \( {\left( -1\right) }^{n}{X}^{n} \) , ce qui montre que \( {P}_{i} \) est de la forme \( {X}^{{n}_{i}} \) pour tout \( i \) . Ainsi, \( \mathcal{C}\left( {P}_{i}\right) \) est la transposée d’un bloc de Jordan pour tout \( i \) , et on en déduit avec le théorème 2 l’existence d’une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) dans laquelle la matrice de \( f \) est de la forme

> Let \( f \in \mathcal{L}\left( E\right) \) be a nilpotent endomorphism. Let \( {P}_{1},\ldots ,{P}_{r} \) denote the sequence of similarity invariants of \( f \). The product \( {P}_{1}\cdots {P}_{r} \) is, up to a sign, the characteristic polynomial of \( f \), which is \( {\left( -1\right) }^{n}{X}^{n} \), showing that \( {P}_{i} \) is of the form \( {X}^{{n}_{i}} \) for every \( i \). Thus, \( \mathcal{C}\left( {P}_{i}\right) \) is the transpose of a Jordan block for every \( i \), and we deduce from theorem 2 the existence of a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) in which the matrix of \( f \) is of the form

\[
\left( \begin{matrix} 0 & \cdots & \cdots & 0 \\  {v}_{1} &  \ddots  & & \vdots \\   &  \ddots  &  \ddots  & \vdots \\  0 & & {v}_{n - 1} & 0 \end{matrix}\right) \;\text{ où }\;\forall i \in  \{ 1,\ldots , n - 1\} ,{v}_{i} \in  \{ 0,1\} .
\]

La matrice de \( f \) dans la base \( {B}^{\prime } = \left( {{e}_{n},\ldots ,{e}_{1}}\right) \) est

> The matrix of \( f \) in the basis \( {B}^{\prime } = \left( {{e}_{n},\ldots ,{e}_{1}}\right) \) is

\[
\left( \begin{matrix} 0 & {v}_{n - 1} & & 0 \\  \vdots &  \ddots  &  \ddots  & \\  \vdots & &  \ddots  & {v}_{1} \\  0 & \cdots & \cdots & 0 \end{matrix}\right)
\]

qui a bien la forme voulue.

> which indeed has the desired form.
