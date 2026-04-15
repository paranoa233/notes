#### 3.7. Trace of an endomorphism

*Français : 3.7. Trace d'un endomorphisme*

DéFINITION 10. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On appelle trace de \( A \) le scalaire \( \operatorname{tr}A = \; \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i} \) . L’application \( A \mapsto \operatorname{tr}A \) est une forme linéaire.

> DEFINITION 10. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . The trace of \( A \) is the scalar \( \operatorname{tr}A = \; \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, i} \) . The map \( A \mapsto \operatorname{tr}A \) is a linear form.

Proposition 6. - Si A et \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\operatorname{tr}\left( {AB}\right) = \operatorname{tr}\left( {BA}\right) \) .

> Proposition 6. - If A and \( B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\operatorname{tr}\left( {AB}\right) = \operatorname{tr}\left( {BA}\right) \) .

- Si \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , \( \operatorname{tr}A = \operatorname{tr}\left( {{}^{\mathrm{t}}A}\right) \) .

> - If \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , \( \operatorname{tr}A = \operatorname{tr}\left( {{}^{\mathrm{t}}A}\right) \) .

- Si A et \( B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) sont semblables, alors \( \operatorname{tr}A = \operatorname{tr}B \) .

> - If A and \( B \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) are similar, then \( \operatorname{tr}A = \operatorname{tr}B \) .

Remarque 9. La trace d'un produit de deux matrices ne dépend pas de l'ordre dans lequel on les multiplie, mais ceci n'est pas vrai lorsque le produit a trois termes ou plus. On peut écrire \( \operatorname{tr}\left( {ABC}\right) = \operatorname{tr}\left( {CAB}\right) = \operatorname{tr}\left( {BCA}\right) \) , mais en général on a \( \operatorname{tr}\left( {ABC}\right) \neq \operatorname{tr}\left( {ACB}\right) \) .

> Remark 9. The trace of a product of two matrices does not depend on the order in which they are multiplied, but this is not true when the product has three or more terms. We can write \( \operatorname{tr}\left( {ABC}\right) = \operatorname{tr}\left( {CAB}\right) = \operatorname{tr}\left( {BCA}\right) \) , but in general we have \( \operatorname{tr}\left( {ABC}\right) \neq \operatorname{tr}\left( {ACB}\right) \) .

La dernière assertion de la proposition précédente permet la définition suivante.

> The last assertion of the previous proposition allows for the following definition.

DéFINITION 11. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, \( B \) une base de \( E \) et \( f \in \mathcal{L}\left( E\right) \) . Alors la trace de la matrice \( {\left\lbrack f\right\rbrack }_{B} \) ne dépend pas de la base \( B \) choisie. Cette valeur s’appelle la trace de \( f \) et est notée tr \( f \) .

> DEFINITION 11. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., \( B \) a basis of \( E \) and \( f \in \mathcal{L}\left( E\right) \) . Then the trace of the matrix \( {\left\lbrack f\right\rbrack }_{B} \) does not depend on the chosen basis \( B \) . This value is called the trace of \( f \) and is denoted tr \( f \) .

Proposition 7. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, \( p \in \mathcal{L}\left( E\right) \) un projecteur. Alors \( \operatorname{tr}p = \left( {\operatorname{rg}p}\right) {1}_{\mathbb{K}} \) (où \( {1}_{\mathbb{K}} \) désigne l’élément unité de \( \mathbb{K} \) ). En particulier, si \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{K} = \mathbb{C} \) alors \( \operatorname{tr}p = \operatorname{rg}p \) .

> Proposition 7. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., \( p \in \mathcal{L}\left( E\right) \) a projector. Then \( \operatorname{tr}p = \left( {\operatorname{rg}p}\right) {1}_{\mathbb{K}} \) (where \( {1}_{\mathbb{K}} \) denotes the identity element of \( \mathbb{K} \) ). In particular, if \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{K} = \mathbb{C} \) then \( \operatorname{tr}p = \operatorname{rg}p \) .

Démonstration. Comme \( p \) est un projecteur, \( \operatorname{Im}p \oplus \operatorname{Ker}p = E \) . Soit \( r = \operatorname{rg}p,\left( {{e}_{1},\ldots ,{e}_{r}}\right) \) une base de \( \operatorname{Im}p \) et \( \left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) une base de Ker \( p \) . Alors \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est une base de \( E \) et la matrice de \( p \) dans cette base est \( {\left\lbrack p\right\rbrack }_{B} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , donc tr \( p = \left( {\operatorname{rg}p}\right) {1}_{\mathbb{K}} \) .

> Proof. Since \( p \) is a projector, \( \operatorname{Im}p \oplus \operatorname{Ker}p = E \) . Let \( r = \operatorname{rg}p,\left( {{e}_{1},\ldots ,{e}_{r}}\right) \) be a basis of \( \operatorname{Im}p \) and \( \left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) be a basis of Ker \( p \) . Then \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is a basis of \( E \) and the matrix of \( p \) in this basis is \( {\left\lbrack p\right\rbrack }_{B} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , so tr \( p = \left( {\operatorname{rg}p}\right) {1}_{\mathbb{K}} \) .
