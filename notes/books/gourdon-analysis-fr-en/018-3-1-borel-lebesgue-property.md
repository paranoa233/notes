#### 3.1. Borel-Lebesgue property

*Français : 3.1. Propriété de Borel-Lebesgue*

DÉFINITION 1. Un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est dit compact si de tout recouvrement de \( E \) par des ouverts de \( E \) , on peut en extraire un sous-recouvrement fini. Autrement dit, si \( E = { \cup }_{i \in I}{O}_{i} \) avec \( {O}_{i} \) ouvert pour tout \( i \) , il existe \( J \subset I, J \) fini, tel que \( E = { \cup }_{i \in J}{O}_{i} \) .

> DEFINITION 1. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is said to be compact if from any covering of \( E \) by open sets of \( E \) , one can extract a finite subcovering. In other words, if \( E = { \cup }_{i \in I}{O}_{i} \) with \( {O}_{i} \) open for all \( i \) , there exists a finite \( J \subset I, J \) such that \( E = { \cup }_{i \in J}{O}_{i} \) .

Exemple 1. - Tout espace métrique fini est compact.

> Example 1. - Every finite metric space is compact.

- L'ensemble \( \mathbb{R} \) des nombres réels n'est pas compact (on ne peut pas extraire un sous-recouvrement fini du recouvrement \( \left. {\mathbb{R} = { \cup  }_{n \in  {\mathbb{N}}^{ * }}}\right\rbrack   - n, n\lbrack ) \) .

> - The set \( \mathbb{R} \) of real numbers is not compact (one cannot extract a finite subcovering from the covering \( \left. {\mathbb{R} = { \cup  }_{n \in  {\mathbb{N}}^{ * }}}\right\rbrack   - n, n\lbrack ) \) ).

Remarque 1. La notion de compacité peut être définie dans un espace topologique général. Si \( E \) est un espace topologique, \( E \) est dit compact s’il est séparé (voir la page 10) et s’il satisfait les propriétés de la définition 1. Les propositions 2, 3, 4 et 5 de cette partie 3.1 restent vraies pour les compacts d'un espace topologique. Mais attention ! La propriété de Bolzano-Weierstrass (voir la partie 3.2) n'est vraie que dans les espaces métriques.

> Remark 1. The notion of compactness can be defined in a general topological space. If \( E \) is a topological space, \( E \) is said to be compact if it is Hausdorff (see page 10) and if it satisfies the properties of definition 1. Propositions 2, 3, 4, and 5 of this part 3.1 remain true for compact sets in a topological space. But beware! The Bolzano-Weierstrass property (see part 3.2) is only true in metric spaces.

Proposition 1. Un espace métrique compact est borné.

> Proposition 1. A compact metric space is bounded.

Démonstration. C’est immédiat car si \( E \) est compact, si \( {x}_{0} \in E \) , en extrayant du recouvrement \( E = { \cup }_{n \in {\mathbb{N}}^{ * }}\mathrm{\;B}\left( {{x}_{0}, n}\right) \) un sous-recouvrement fini, on s’aperçoit que \( E \) est borné.

> Proof. This is immediate because if \( E \) is compact, if \( {x}_{0} \in E \) , by extracting a finite subcover from the cover \( E = { \cup }_{n \in {\mathbb{N}}^{ * }}\mathrm{\;B}\left( {{x}_{0}, n}\right) \) , we see that \( E \) is bounded.

Aspect dual de la propriété de Borel-Lebesgue. En passant au complémentaire de la définition 1, on obtient facilement le résultat qui suit.

> Dual aspect of the Borel-Lebesgue property. By passing to the complement of definition 1, we easily obtain the following result.

Proposition 2. Un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est compact si et seulement si de toute intersection vide de fermés de E, on peut en extraire une sous-famille finie d'intersection vide.

> Proposition 2. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is compact if and only if from any empty intersection of closed sets of E, one can extract a finite subfamily with an empty intersection.

Une conséquence immédiate est la suivante.

> An immediate consequence is the following.

Proposition 3. Si \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) est une suite décroissante de fermés non vides dans un compact \( E \) , alors \( { \cap }_{n \in \mathbb{N}}{F}_{n} \neq \varnothing \) .

> Proposition 3. If \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) is a decreasing sequence of non-empty closed sets in a compact space \( E \) , then \( { \cap }_{n \in \mathbb{N}}{F}_{n} \neq \varnothing \) .

Remarque 2. Nous avons vu plus haut (voir la proposition 9 page 20) que ce dernier résultat reste vrai dans un espace complet pourvu que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) . Si cette dernière condition n'est pas vérifiée, le résultat est faux dans un espace complet (par exemple, \( { \cap }_{n \in \mathbb{N}}\lbrack n, + \infty \lbrack = \varnothing ) \) .

> Remark 2. We saw above (see proposition 9 on page 20) that this last result remains true in a complete space provided that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) . If this latter condition is not satisfied, the result is false in a complete space (for example, \( { \cap }_{n \in \mathbb{N}}\lbrack n, + \infty \lbrack = \varnothing ) \) .

Parties compactes. Les propriétés des ouverts d'une topologie induite entraînent une caractérisation simple des parties compactes.

> Compact subsets. The properties of open sets in an induced topology lead to a simple characterization of compact subsets.

Proposition 4. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Une partie \( A \) de \( E \) est compacte si et seulement si de tout recouvrement de \( A \) par des ouverts de \( E\left( {A \subset { \cup }_{i \in I}{O}_{i}}\right. \) avec \( {O}_{i} \) ouvert de \( E \) pour tout i), il en existe un sous-recouvrement fini ( \( \exists J \subset I, J \) fini, tel que \( \left. {A \subset { \cup }_{i \in J}{O}_{i}}\right) \) .

> Proposition 4. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. A subset \( A \) of \( E \) is compact if and only if from any covering of \( A \) by open sets of \( E\left( {A \subset { \cup }_{i \in I}{O}_{i}}\right. \) (with \( {O}_{i} \) open in \( E \) for all i), there exists a finite subcover ( \( \exists J \subset I, J \) finite, such that \( \left. {A \subset { \cup }_{i \in J}{O}_{i}}\right) \) .

On en déduit facilement :

> We easily deduce from this:

Proposition 5. Une réunion finie de parties compactes est compacte.

> Proposition 5. A finite union of compact sets is compact.

Proposition 6. Une intersection de compacts est compacte.

> Proposition 6. An intersection of compact sets is compact.
