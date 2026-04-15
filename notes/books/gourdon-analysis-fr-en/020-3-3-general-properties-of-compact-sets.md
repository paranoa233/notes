#### 3.3. General properties of compact sets

*Français : 3.3. Propriétés générales des compacts*

Proposition 7. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique.

> Proposition 7. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space.

- Si E est compact et si A est une partie fermée de E, A est compacte.

> - If E is compact and A is a closed subset of E, then A is compact.

- Si A est une partie compacte de E, A est fermée et bornée.

> - If A is a compact subset of E, then A is closed and bounded.

Proposition 8. Un espace compact est complet.

> Proposition 8. A compact space is complete.

Proposition 9. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique compact et \( \left( {x}_{n}\right) \) une suite de E admettant une et une seule valeur d’adhérence \( x \) . Alors \( \left( {x}_{n}\right) \) converge vers \( x \) .

> Proposition 9. Let \( \left( {E,\mathrm{\;d}}\right) \) be a compact metric space and \( \left( {x}_{n}\right) \) be a sequence in E admitting one and only one cluster point \( x \). Then \( \left( {x}_{n}\right) \) converges to \( x \).

Démonstration. Supposons le contraire. Alors

> Proof. Suppose the contrary. Then

\[
\exists \varepsilon  > 0,\forall N,\exists n \geq  N,\;\mathrm{\;d}\left( {{x}_{n}, x}\right)  \geq  \varepsilon .
\]

On peut donc construire une sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) telle que pour tout \( n,\mathrm{\;d}\left( {{x}_{\varphi \left( n\right) }, x}\right) \geq \varepsilon \) . Comme \( E \) est compact, on peut extraire de la sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) une nouvelle sous-suite \( \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \) convergente. Si \( y \) est sa limite, on a \( \mathrm{d}\left( {x, y}\right) \geq \varepsilon \) , donc \( x \neq y \) . Ceci est absurde car \( y \) est une valeur d’adhérence de \( \left( {x}_{n}\right) \) , d’où le résultat.

> We can therefore construct a subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) such that for all \( n,\mathrm{\;d}\left( {{x}_{\varphi \left( n\right) }, x}\right) \geq \varepsilon \) . Since \( E \) is compact, we can extract from the subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) a new convergent subsequence \( \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \) . If \( y \) is its limit, we have \( \mathrm{d}\left( {x, y}\right) \geq \varepsilon \) , so \( x \neq y \) . This is absurd because \( y \) is a cluster point of \( \left( {x}_{n}\right) \) , hence the result.

Remarque 3. Ce résultat peut s'avérer parfois bien pratique.

> Remark 3. This result can sometimes prove to be very practical.

Proposition 10. Soient \( {E}_{1},\ldots ,{E}_{n} \) un nombre fini d’espaces métriques. L’ensemble \( E = \; {E}_{1} \times \cdots \times {E}_{n} \) est compact si et seulement si \( {E}_{i} \) est compact pour tout i.

> Proposition 10. Let \( {E}_{1},\ldots ,{E}_{n} \) be a finite number of metric spaces. The set \( E = \; {E}_{1} \times \cdots \times {E}_{n} \) is compact if and only if \( {E}_{i} \) is compact for all i.

Remarque 4. Étant données deux suites \( \left( {x}_{n}\right) \) et \( \left( {y}_{n}\right) \) à valeurs dans un même compact \( E \) , cette proposition montre l’existence d’une injection croissante \( \varphi \) de \( \mathbb{N} \) dans \( \mathbb{N} \) telle que les deux suites \( \left( {x}_{\varphi \left( n\right) }\right) \) et \( \left( {y}_{\varphi \left( n\right) }\right) \) convergent (ceci car \( \left( {{x}_{n},{y}_{n}}\right) \) est une suite dans le compact \( E \times E) \) .

> Remark 4. Given two sequences \( \left( {x}_{n}\right) \) and \( \left( {y}_{n}\right) \) with values in the same compact set \( E \) , this proposition shows the existence of an increasing injection \( \varphi \) from \( \mathbb{N} \) to \( \mathbb{N} \) such that both sequences \( \left( {x}_{\varphi \left( n\right) }\right) \) and \( \left( {y}_{\varphi \left( n\right) }\right) \) converge (this is because \( \left( {{x}_{n},{y}_{n}}\right) \) is a sequence in the compact set \( E \times E) \) ).

\( \rightarrow \) Proposition 11. Les parties compactes de \( {\mathbb{R}}^{n} \) (muni de la distance produit usuelle, avec \( n \in {\mathbb{N}}^{ * } \) ) sont les fermés bornés de \( {\mathbb{R}}^{n} \) .

> \( \rightarrow \) Proposition 11. The compact subsets of \( {\mathbb{R}}^{n} \) (equipped with the usual product distance, with \( n \in {\mathbb{N}}^{ * } \) ) are the closed and bounded sets of \( {\mathbb{R}}^{n} \) .

Remarque 5. Comme nous le verrons à la partie 5.3, toutes les normes d'un \( \mathbb{R} \) -e.v.n de dimension finie sont équivalentes. Ceci nous permettra d'affirmer que le résultat de cette proposition reste vrai dans tout \( \mathbb{R} \) -espace vectoriel normé de dimension finie. Par contre, il est faux en dimension infinie (voir le théorème de Riesz à l'exercice 9 de la page 56).

> Remark 5. As we will see in part 5.3, all norms of a finite-dimensional \( \mathbb{R} \) -n.v.s. are equivalent. This will allow us to state that the result of this proposition remains true in any finite-dimensional \( \mathbb{R} \) -normed vector space. However, it is false in infinite dimension (see Riesz's theorem in exercise 9 on page 56).

\( \rightarrow \) Proposition 12. Soit \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) une suite convergente d’un espace métrique \( \left( {E,\mathrm{\;d}}\right) ,\ell \) sa limite. Alors l’ensemble \( \Gamma = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \cup \{ \ell \} \) est compact.

> \( \rightarrow \) Proposition 12. Let \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) be a convergent sequence in a metric space \( \left( {E,\mathrm{\;d}}\right) ,\ell \) its limit. Then the set \( \Gamma = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \cup \{ \ell \} \) is compact.

Démonstration. Nous sommes dans un des rares cas ou il est plus facile de montrer la compacité de \( \Gamma \) en prouvant qu’il vérifie la propriété de Borel-Lebesgue (la caractérisation par la propriété de Bolzano-Weierstrass donnerait ici une preuve bancale et peu satisfaisante). Cette preuve faisant appel uniquement à la topologie de \( E \) montrera qu’en fait le résultat reste vrai dans un espace topologique séparé général.

> Proof. We are in one of the rare cases where it is easier to show the compactness of \( \Gamma \) by proving that it satisfies the Borel-Lebesgue property (the characterization by the Bolzano-Weierstrass property would yield a shaky and unsatisfactory proof here). This proof, relying solely on the topology of \( E \) , will show that the result actually remains true in a general Hausdorff topological space.

Soit \( {\left( {O}_{i}\right) }_{i \in I} \) un recouvrement de \( \Gamma \) par des ouverts de \( E \) . Comme \( \ell \in \Gamma \) , il existe \( {i}_{0} \in I \) tel que \( \ell \in {O}_{{i}_{0}} \) , et comme \( {O}_{{i}_{0}} \) est ouvert et que \( \left( {x}_{n}\right) \) tend vers \( \ell \) ,

> Let \( {\left( {O}_{i}\right) }_{i \in I} \) be an open cover of \( \Gamma \) by open sets of \( E \) . Since \( \ell \in \Gamma \) , there exists \( {i}_{0} \in I \) such that \( \ell \in {O}_{{i}_{0}} \) , and since \( {O}_{{i}_{0}} \) is open and \( \left( {x}_{n}\right) \) converges to \( \ell \) ,

\[
\exists N \in  \mathbb{N},\forall n > N,\;{x}_{n} \in  {O}_{{i}_{0}}.
\]

Pour tout \( n \leq N \) , il existe \( {j}_{n} \in I \) tel que \( {x}_{n} \in {O}_{{j}_{n}} \) . En notant \( J = \left\{ {{j}_{n}, n \leq N}\right\} \cup \left\{ {i}_{0}\right\} \) , on s’aperçoit que \( \Gamma \subset { \cup }_{j \in J}{O}_{j} \) , et comme \( J \) est fini, le résultat est prouvé.

> For all \( n \leq N \) , there exists \( {j}_{n} \in I \) such that \( {x}_{n} \in {O}_{{j}_{n}} \) . By noting \( J = \left\{ {{j}_{n}, n \leq N}\right\} \cup \left\{ {i}_{0}\right\} \) , we see that \( \Gamma \subset { \cup }_{j \in J}{O}_{j} \) , and since \( J \) is finite, the result is proven.
