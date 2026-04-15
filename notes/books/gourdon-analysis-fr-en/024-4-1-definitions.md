#### 4.1. Definitions

Proposition 1. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Les assertions suivantes sont équiva-lentes.

> Proposition 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. The following assertions are equivalent.

(i) Il n'existe pas de partition de \( E \) en deux ouverts disjoints non vides.

> (i) There is no partition of \( E \) into two non-empty disjoint open sets.

(ii) Il n'existe pas de partition de \( E \) en deux fermés disjoints non vides. (iii) Les seules parties ouvertes et fermées de \( E \) sont \( \varnothing \) et \( E \) .

> (ii) There is no partition of \( E \) into two non-empty disjoint closed sets. (iii) The only open and closed subsets of \( E \) are \( \varnothing \) and \( E \) .

Démonstration. (i) \( \Rightarrow \) (ii). Supposons \( E = {F}_{1} \cup {F}_{2} \) où \( {F}_{1} \) et \( {F}_{2} \) sont deux fermés de \( E \) vérifiant \( {F}_{1} \cap {F}_{2} = \varnothing \) . Les ouverts \( {O}_{1} = E \smallsetminus {F}_{1} \) et \( {O}_{2} = E \smallsetminus {F}_{2} \) vérifient \( {O}_{1} \cup {O}_{2} = \varnothing \) et \( {O}_{1} \cap {O}_{2} = \varnothing \) , donc d’après (i), \( {O}_{1} = \varnothing \) ou \( {O}_{2} = \varnothing \) , donc \( {F}_{1} = E \) ou \( {F}_{2} = E \) , et comme \( {F}_{1} \cup {F}_{2} \) est une partition de \( E,{F}_{1} = \varnothing \) ou \( {F}_{2} = \varnothing \) .

> Proof. (i) \( \Rightarrow \) (ii). Suppose \( E = {F}_{1} \cup {F}_{2} \) where \( {F}_{1} \) and \( {F}_{2} \) are two closed sets of \( E \) satisfying \( {F}_{1} \cap {F}_{2} = \varnothing \) . The open sets \( {O}_{1} = E \smallsetminus {F}_{1} \) and \( {O}_{2} = E \smallsetminus {F}_{2} \) satisfy \( {O}_{1} \cup {O}_{2} = \varnothing \) and \( {O}_{1} \cap {O}_{2} = \varnothing \) , so according to (i), \( {O}_{1} = \varnothing \) or \( {O}_{2} = \varnothing \) , therefore \( {F}_{1} = E \) or \( {F}_{2} = E \) , and since \( {F}_{1} \cup {F}_{2} \) is a partition of \( E,{F}_{1} = \varnothing \) or \( {F}_{2} = \varnothing \) .

(ii) \( \Rightarrow \) (iii). Soit \( A \) une partie ouverte et fermée de \( E \) . Alors l’ensemble \( B = E \smallsetminus A \) est ouvert et fermé, et comme \( E = A \cup B \) avec \( A \cap B = \varnothing \) , on en déduit d’après (ii) que \( A = \varnothing \) ou \( B = \varnothing \) , c’est-à-dire \( A = \varnothing \) ou \( A = E \) .

> (ii) \( \Rightarrow \) (iii). Let \( A \) be an open and closed subset of \( E \) . Then the set \( B = E \smallsetminus A \) is open and closed, and since \( E = A \cup B \) with \( A \cap B = \varnothing \) , we deduce from (ii) that \( A = \varnothing \) or \( B = \varnothing \) , that is to say \( A = \varnothing \) or \( A = E \) .

(iii) \( \Rightarrow \) (i). Supposons \( E = {O}_{1} \cup {O}_{2} \) où \( {O}_{1} \) et \( {O}_{2} \) sont deux ouverts disjoints de \( E \) . L’ensemble \( {O}_{1} \) est fermé car \( {O}_{1} = E \smallsetminus {O}_{2} \) , donc \( {O}_{1} \) , ouvert et fermé de \( E \) , vérifie \( {O}_{1} = \varnothing \) ou \( {O}_{1} = E \) , d’où (i).

> (iii) \( \Rightarrow \) (i). Suppose \( E = {O}_{1} \cup {O}_{2} \) where \( {O}_{1} \) and \( {O}_{2} \) are two disjoint open sets of \( E \) . The set \( {O}_{1} \) is closed because \( {O}_{1} = E \smallsetminus {O}_{2} \) , therefore \( {O}_{1} \) , open and closed in \( E \) , satisfies \( {O}_{1} = \varnothing \) or \( {O}_{1} = E \) , hence (i).

DÉFINITION 1. Un espace métrique vérifiant l'une des assertions de la proposition précé- dente est dit connexe.

> DEFINITION 1. A metric space satisfying one of the assertions of the previous proposition is said to be connected.

Remarque 1. La notion de connexité est une notion topologique. Tous les résultats de cette partie restent vrais dans un espace topologique général (à l'exception du théorème 5).

> Remark 1. The notion of connectedness is a topological notion. All the results in this part remain true in a general topological space (with the exception of theorem 5).

Parties connexes. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( A \) une partie de \( E \) . On munit \( A \) de la distance d induite sur \( A \) . On veut savoir à quelle condition \( A \) est connexe. Les propriétés de la topologie induite sur \( A \) entraînent facilement le résultat qui suit.

> Connected subsets. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( A \) a subset of \( E \) . We equip \( A \) with the distance d induced on \( A \) . We want to know under what condition \( A \) is connected. The properties of the topology induced on \( A \) easily lead to the following result.

PROPOSITION 2. La partie \( A \) de \( E \) est connexe si et seulement si l’une des deux conditions suivantes est réalisée.

> PROPOSITION 2. The subset \( A \) of \( E \) is connected if and only if one of the following two conditions is met.

(i) Si \( A \subset {O}_{1} \cup {O}_{2} \) où \( {O}_{1} \) et \( {O}_{2} \) sont deux ouverts de \( E \) vérifiant \( A \cap {O}_{1} \cap {O}_{2} = \varnothing \) , alors

> (i) If \( A \subset {O}_{1} \cup {O}_{2} \) where \( {O}_{1} \) and \( {O}_{2} \) are two open sets of \( E \) satisfying \( A \cap {O}_{1} \cap {O}_{2} = \varnothing \) , then

\[
\left( {A \cap  {O}_{1} = \varnothing \text{ et }A \subset  {O}_{2}}\right) \text{ ou }\left( {A \cap  {O}_{2} = \varnothing \text{ et }A \subset  {O}_{1}}\right) .
\]

(ii) \( \operatorname{Si}A \subset {F}_{1} \cup {F}_{2} \) où \( {F}_{1} \) et \( {F}_{2} \) sont deux fermés de \( E \) vérifiant \( A \cap {F}_{1} \cap {F}_{2} = \varnothing \) , alors

> (ii) \( \operatorname{Si}A \subset {F}_{1} \cup {F}_{2} \) where \( {F}_{1} \) and \( {F}_{2} \) are two closed sets of \( E \) satisfying \( A \cap {F}_{1} \cap {F}_{2} = \varnothing \) , then

\[
\left( {A \cap  {F}_{1} = \varnothing \text{ et }A \subset  {F}_{2}}\right) \;\text{ ou }\;\left( {A \cap  {F}_{2} = \varnothing \text{ et }A \subset  {F}_{1}}\right) .
\]

Exemple 1. L’ensemble \( \mathbb{Q} \) des rationnels n’est pas un connexe de \( \mathbb{R} \) car si on se donne \( a \in \mathbb{R} \smallsetminus \mathbb{Q} \) , on a \( \mathbb{Q} \subset \rbrack - \infty , a\left\lbrack \cup \right\rbrack a, + \infty \lbrack \) .

> Example 1. The set \( \mathbb{Q} \) of rationals is not a connected subset of \( \mathbb{R} \) because if we take \( a \in \mathbb{R} \smallsetminus \mathbb{Q} \) , we have \( \mathbb{Q} \subset \rbrack - \infty , a\left\lbrack \cup \right\rbrack a, + \infty \lbrack \) .
