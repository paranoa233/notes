#### 2.6. Splitting field of a polynomial

*Français : 2.6. Corps des racines d'un polynôme*

Toutes les extensions de corps considérées dans cette sous partie seront commutatives. Notation. Si \( \mathbb{L} \) est une extension de corps de \( \mathbb{K} \) , pour tout \( A \subset \mathbb{L} \) on note \( \mathbb{K}\left( A\right) \) le plus petit sous-corps de \( \mathbb{L} \) contenant \( \mathbb{K} \) et \( A \) (il existe, c’est l’intersection des sous-corps de \( \mathbb{L} \) contenant \( \mathbb{K} \) et \( A \) ). Lorsque \( A = \left\{ {{a}_{1},\cdots ,{a}_{n}}\right\} \) est fini, on note souvent \( \mathbb{K}\left( A\right) = \; \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) pour alléger les notations.

> All field extensions considered in this subsection will be commutative. Notation. If \( \mathbb{L} \) is a field extension of \( \mathbb{K} \) , for any \( A \subset \mathbb{L} \) we denote by \( \mathbb{K}\left( A\right) \) the smallest subfield of \( \mathbb{L} \) containing \( \mathbb{K} \) and \( A \) (it exists, it is the intersection of the subfields of \( \mathbb{L} \) containing \( \mathbb{K} \) and \( A \) ). When \( A = \left\{ {{a}_{1},\cdots ,{a}_{n}}\right\} \) is finite, we often write \( \mathbb{K}\left( A\right) = \; \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) to simplify notation.

Remarque 10. Si \( A \) et \( B \) sont deux parties de \( \mathbb{L} \) , on a facilement \( \mathbb{K}\left( A\right) \left( B\right) = \mathbb{K}\left( {A \cup B}\right) \) .

> Remark 10. If \( A \) and \( B \) are two subsets of \( \mathbb{L} \) , we easily have \( \mathbb{K}\left( A\right) \left( B\right) = \mathbb{K}\left( {A \cup B}\right) \) .

PROPOSITION 5. Soit \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) . Il existe une extension \( \mathbb{L} \) de \( \mathbb{K} \) telle que \( P \) admette une racine \( x \) dans \( \mathbb{L} \) .

> PROPOSITION 5. Let \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) be irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) . There exists an extension \( \mathbb{L} \) of \( \mathbb{K} \) such that \( P \) admits a root \( x \) in \( \mathbb{L} \) .

Démonstration. D’après la proposition \( 4,\mathbb{L} = \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est un corps. L’injection canonique \( \varphi : \mathbb{K} \rightarrow \mathbb{L}\;a \mapsto \dot{a} \) (c’est une injection car \( \deg \left( P\right) \geq 1 \) ) permet d’identifier les éléments de \( \mathbb{K} \) et de \( \varphi \left( \mathbb{K}\right) \) . Ainsi, \( \mathbb{L} \) apparaît comme une extension de \( \mathbb{K} \) . En posant \( x = \dot{X} \in \mathbb{L} \) , on voit que \( P\left( x\right) = \dot{P} = 0. \)

> Proof. According to the proposition \( 4,\mathbb{L} = \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is a field. The canonical injection \( \varphi : \mathbb{K} \rightarrow \mathbb{L}\;a \mapsto \dot{a} \) (it is an injection because \( \deg \left( P\right) \geq 1 \) ) allows identifying the elements of \( \mathbb{K} \) and \( \varphi \left( \mathbb{K}\right) \) . Thus, \( \mathbb{L} \) appears as an extension of \( \mathbb{K} \) . By setting \( x = \dot{X} \in \mathbb{L} \) , we see that \( P\left( x\right) = \dot{P} = 0. \)

THÉORÉME 5. Soit \( F \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( F\right) \geq 1 \) . Alors il existe une extension \( \mathbb{L} \) de \( \mathbb{K} \) sur laquelle le polynôme \( F \) soit scindé.

> THEOREM 5. Let \( F \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( F\right) \geq 1 \) . Then there exists an extension \( \mathbb{L} \) of \( \mathbb{K} \) over which the polynomial \( F \) splits.

Démonstration. Nous allons procéder par récurrence sur \( n = \deg \left( F\right) \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai jusqu’à \( n - 1 \) et montrons le pour \( n \) . Soit \( G \) un facteur irréductible de \( F \) , et \( H \) tel que \( F = {GH} \) . D’après la proposition précédente, il existe une extension \( {\mathbb{L}}_{1} \) de \( \mathbb{K} \) dans laquelle \( G \) admette une racine \( {a}_{1} \) . On peut écrire \( G = \left( {X - {a}_{1}}\right) {G}_{1} \) avec \( {G}_{1} \in {\mathbb{L}}_{1}\left\lbrack X\right\rbrack \) , et donc \( F = \left( {X - {a}_{1}}\right) {F}_{1} \) avec \( {F}_{1} = {G}_{1}H \in {\mathbb{L}}_{1}\left\lbrack X\right\rbrack \) . Comme \( \deg \left( {F}_{1}\right) = n - 1 \) , il existe d’après l’hypothèse de récurrence une extension \( \mathbb{L} \) de \( {\mathbb{L}}_{1} \) telle que \( {F}_{1} \) soit scindé sur \( \mathbb{L} \) . Dans \( \mathbb{L}\left\lbrack X\right\rbrack , F \) est donc scindé.

> Proof. We will proceed by induction on \( n = \deg \left( F\right) \) . For \( n = 1 \) , it is obvious. Assume the result is true up to \( n - 1 \) and show it for \( n \) . Let \( G \) be an irreducible factor of \( F \) , and \( H \) such that \( F = {GH} \) . According to the previous proposition, there exists an extension \( {\mathbb{L}}_{1} \) of \( \mathbb{K} \) in which \( G \) has a root \( {a}_{1} \) . We can write \( G = \left( {X - {a}_{1}}\right) {G}_{1} \) with \( {G}_{1} \in {\mathbb{L}}_{1}\left\lbrack X\right\rbrack \) , and thus \( F = \left( {X - {a}_{1}}\right) {F}_{1} \) with \( {F}_{1} = {G}_{1}H \in {\mathbb{L}}_{1}\left\lbrack X\right\rbrack \) . Since \( \deg \left( {F}_{1}\right) = n - 1 \) , there exists by the induction hypothesis an extension \( \mathbb{L} \) of \( {\mathbb{L}}_{1} \) such that \( {F}_{1} \) splits over \( \mathbb{L} \) . In \( \mathbb{L}\left\lbrack X\right\rbrack , F \) is therefore split.

Remarque 11. Une telle extension \( \mathbb{L} \) de \( \mathbb{K} \) dans laquelle \( F \) soit scindé s’appelle un corps de dissociation de \( F \) . Dans ce corps, on peut écrire

> Remark 11. Such an extension \( \mathbb{L} \) of \( \mathbb{K} \) in which \( F \) splits is called a splitting field of \( F \) . In this field, we can write

\[
F = \lambda \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \;\text{ avec }\;\lambda  \in  {\mathbb{K}}^{ * }\text{ et }{a}_{1},\ldots ,{a}_{n} \in  \mathbb{L}.
\]

Le corps \( {\mathbb{L}}_{1} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) est le plus petit sous-corps de \( \mathbb{L} \) sur lequel \( F \) soit scindé. On peut montrer que \( {\mathbb{L}}_{1} \) ainsi défini est unique à un isomorphisme près (l’unicité n’est pas immédiate car il n’y a pas unicité du corps de dissociation \( \mathbb{L} \) ). On l’appelle corps des racines du polynôme \( F \) .

> The field \( {\mathbb{L}}_{1} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) is the smallest subfield of \( \mathbb{L} \) over which \( F \) splits. It can be shown that \( {\mathbb{L}}_{1} \) thus defined is unique up to isomorphism (uniqueness is not immediate because the splitting field \( \mathbb{L} \) is not unique). It is called the splitting field of the polynomial \( F \) .

DéFINITION 5. Un corps \( \mathbb{K} \) est dit algébriquement clos si tout polynôme de \( \mathbb{K}\left\lbrack X\right\rbrack \) de degré \( \geq 1 \) a au moins une racine dans \( \mathbb{K} \) .

> DEFINITION 5. A field \( \mathbb{K} \) is said to be algebraically closed if every polynomial in \( \mathbb{K}\left\lbrack X\right\rbrack \) of degree \( \geq 1 \) has at least one root in \( \mathbb{K} \) .

Remarque 12. Une récurrence immédiate sur le degré montre que si K est un corps algé- briquement clos, tout polynôme de \( \mathbb{K}\left\lbrack X\right\rbrack \) est scindé sur \( \mathbb{K} \) .

> Remark 12. An immediate induction on the degree shows that if K is an algebraically closed field, every polynomial in \( \mathbb{K}\left\lbrack X\right\rbrack \) splits over \( \mathbb{K} \) .

- On peut montrer que tout corps \( \mathbb{K} \) admet une extension \( \mathbb{L} \) algébriquement close (théo-rème de Steinitz). La plus petite extension \( \mathbb{L} \) vérifiant cette propriété est unique à un isomorphisme près, et on l'appelle clôture algébrique de \( \mathbb{K} \) . Nous ne démontrerons pas ce résultat. On a cependant le résultat suivant.

> - It can be shown that every field \( \mathbb{K} \) admits an algebraically closed extension \( \mathbb{L} \) (Steinitz's theorem). The smallest extension \( \mathbb{L} \) satisfying this property is unique up to isomorphism, and it is called the algebraic closure of \( \mathbb{K} \) . We will not prove this result. However, we have the following result.

THÉORÉME 6 (THÉORÉME FONDAMENTAL DE L'ALGEBRE). Le corps \( \mathbb{C} \) des nombres complexes est algébriquement clos.

> THEOREM 6 (FUNDAMENTAL THEOREM OF ALGEBRA). The field \( \mathbb{C} \) of complex numbers is algebraically closed.

Remarque 13. Deux preuves différentes de ce résultat sont proposées dans le problème 4 page 90.

> Remark 13. Two different proofs of this result are proposed in problem 4 on page 90.

- Le théorème fondamental de l'algèbre entraîne que les polynômes irréductibles de \( \mathbb{C}\left\lbrack  X\right\rbrack \) sont de degré 1. On montre que les polynômes irréductibles de \( \mathbb{R}\left\lbrack  X\right\rbrack \) sont les polynômes de degré 1 et les polynômes de la forme \( a{X}^{2} + {bX} + c \) avec \( {b}^{2} - {4ac} < 0 \) .

> - The fundamental theorem of algebra implies that the irreducible polynomials of \( \mathbb{C}\left\lbrack  X\right\rbrack \) are of degree 1. It can be shown that the irreducible polynomials of \( \mathbb{R}\left\lbrack  X\right\rbrack \) are the polynomials of degree 1 and the polynomials of the form \( a{X}^{2} + {bX} + c \) with \( {b}^{2} - {4ac} < 0 \) .
