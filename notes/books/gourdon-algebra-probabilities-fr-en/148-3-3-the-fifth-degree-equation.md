#### 3.3. The fifth-degree equation?

*Français : 3.3. L'équation du cinquième degré ?*

L'approche de Lagrange est une technique très efficace pour abaisser le degré d'une équation. Il est naturel de chercher à l'appliquer sur l'équation générale de degré cinq. La difficulté est ici de trouver un polynôme de cinq variables qui ne prend que quatre valeurs par toute permutation de ses variables.

> Lagrange's approach is a very effective technique for lowering the degree of an equation. It is natural to seek to apply it to the general equation of degree five. The difficulty here is to find a polynomial of five variables that takes only four values under any permutation of its variables.

En fait, un tel polynôme n'existe pas. Nous allons prouver ce résultat. Pour tout polynôme \( P \in \mathbb{C}\left\lbrack {{X}_{1},{X}_{2},{X}_{3},{X}_{4},{X}_{5}}\right\rbrack \) , pour toute permutation \( \sigma \in {\mathcal{S}}_{5} \) , on note

> In fact, such a polynomial does not exist. We will prove this result. For any polynomial \( P \in \mathbb{C}\left\lbrack {{X}_{1},{X}_{2},{X}_{3},{X}_{4},{X}_{5}}\right\rbrack \) , for any permutation \( \sigma \in {\mathcal{S}}_{5} \) , we denote

\[
{P}_{\sigma } = P\left( {{X}_{\sigma \left( 1\right) },{X}_{\sigma \left( 2\right) },{X}_{\sigma \left( 3\right) },{X}_{\sigma \left( 4\right) },{X}_{\sigma \left( 5\right) }}\right)
\]

Supposons que \( P \in \mathbb{C}\left\lbrack {{X}_{1},{X}_{2},{X}_{3},{X}_{4},{X}_{5}}\right\rbrack \) soit tel que l’ensemble \( \Gamma = \left\{ {{P}_{\sigma } \mid \sigma \in {\mathcal{S}}_{5}}\right\} \) vérifie \( \operatorname{Card}\left( \Gamma \right) = 4 \) . Le groupe des permutations \( {\mathcal{S}}_{5} \) opère sur \( \Gamma \) par le biais de la fonction

> Suppose that \( P \in \mathbb{C}\left\lbrack {{X}_{1},{X}_{2},{X}_{3},{X}_{4},{X}_{5}}\right\rbrack \) is such that the set \( \Gamma = \left\{ {{P}_{\sigma } \mid \sigma \in {\mathcal{S}}_{5}}\right\} \) satisfies \( \operatorname{Card}\left( \Gamma \right) = 4 \) . The permutation group \( {\mathcal{S}}_{5} \) acts on \( \Gamma \) through the function

\[
{\mathcal{S}}_{5} \times  \Gamma  \rightarrow  \Gamma \;\left( {\sigma , Q}\right)  \mapsto  {Q}_{\sigma }
\]

D’après le théorème 7 de la page 24, le stabilisateur \( H = \left\{ {\sigma \in {\mathcal{S}}_{5} \mid {P}_{\sigma } = P}\right\} \) de \( P \) est un sous groupe de \( {\mathcal{S}}_{5} \) d’indice 4 dans \( {\mathcal{S}}_{5} \) (puisque par construction, l’orbite de \( P \) est \( \Gamma \) tout entier, de cardinal 4). D'après l'exercice 8 de la page 27 ceci est impossible, d'où le résultat.

> According to theorem 7 on page 24, the stabilizer \( H = \left\{ {\sigma \in {\mathcal{S}}_{5} \mid {P}_{\sigma } = P}\right\} \) of \( P \) is a subgroup of \( {\mathcal{S}}_{5} \) of index 4 in \( {\mathcal{S}}_{5} \) (since by construction, the orbit of \( P \) is \( \Gamma \) itself, of cardinality 4). According to exercise 8 on page 27 this is impossible, hence the result.

Cette démonstration ne prouve pas qu'il est impossible de "résoudre" par des formules générales l'équation de degré cinq, mais elle montre simplement que la méthode de Lagrange ne s'applique pas. C'est Abel qui le premier montra que des formules générales pour les solutions de l'équation de degré cinq n'existent pas. Galois compléta quelques années plus tard ce résultat en donnant une condition nécessaire et suffisante sur un poly-nôme pour qu'il soit résoluble par radicaux (en termes intuitifs, on dit qu'une équation est résoluble par radicaux si ses solutions peuvent s'exprimer au moyen de "radicaux emboités les uns dans les autres").

> This proof does not prove that it is impossible to "solve" the fifth-degree equation using general formulas, but it simply shows that Lagrange's method does not apply. It was Abel who first showed that general formulas for the solutions of the fifth-degree equation do not exist. Galois completed this result a few years later by giving a necessary and sufficient condition for a polynomial to be solvable by radicals (in intuitive terms, we say that an equation is solvable by radicals if its solutions can be expressed by means of "radicals nested within one another").

Annexe B

> Appendix B

Invariants de similitude d'un endomorphisme et réduction de Frobenius

> Similarity invariants of an endomorphism and Frobenius reduction

Cette annexe présente la théorie des invariants de similitude des endomorphismes en dimension finie. Cette notion est assez éloignée de l'esprit du programme de mathéma-tiques spéciales, et c'est plus à titre de curiosité qu'elle est présentée. Comme nous allons le voir, elle propose un cadre agréable de réduction des endomorphismes qui permet une caractérisation simple de la classe des matrices semblables à une matrice donnée. En première lecture, les démonstrations des résultats énoncés peuvent être sautées.

> This appendix presents the theory of similarity invariants of endomorphisms in finite dimension. This notion is quite far from the spirit of the special mathematics curriculum, and it is presented more as a curiosity. As we shall see, it offers a pleasant framework for the reduction of endomorphisms that allows for a simple characterization of the class of matrices similar to a given matrix. On a first reading, the proofs of the stated results may be skipped.

Dans toute l’annexe, \( E \) désigne un espace vectoriel sur un corps commutatif \( \mathbb{K} \) de dimension finie \( n \) .

> Throughout the appendix, \( E \) denotes a vector space over a commutative field \( \mathbb{K} \) of finite dimension \( n \) .
