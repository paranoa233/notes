#### 4.4. Integrable functions

*Français : 4.4. Fonctions intégrables*

Comme pour les intégrales simples, on peut définir les fonctions de plusieurs variables intégrables. Nous nous limiterons au cas de fonctions définies sur un produit d'intervalles de \( {\mathbb{R}}^{n} \) . Dans toute cette sous-partie, \( {I}_{1},\ldots ,{I}_{n} \) désignent des intervalles quelconques de \( \mathbb{R} \) (non réduits à un singleton) et \( A \) la partie de \( {\mathbb{R}}^{n} \) définie par \( A = {I}_{1} \times \cdots \times {I}_{n} \)

> As with single integrals, we can define integrable functions of several variables. We will limit ourselves to the case of functions defined on a product of intervals of \( {\mathbb{R}}^{n} \). Throughout this subsection, \( {I}_{1},\ldots ,{I}_{n} \) denote arbitrary intervals of \( \mathbb{R} \) (not reduced to a singleton) and \( A \) the part of \( {\mathbb{R}}^{n} \) defined by \( A = {I}_{1} \times \cdots \times {I}_{n} \)

DÉFINITION 6. Soit \( f : A = {I}_{1} \times \cdots \times {I}_{n} \rightarrow \mathbb{R} \) une fonction continue positive. On dit que \( f \) est intégrable s’il existe \( M > 0 \) tel que pour tout pavé compact \( P \subset A \) , on a \( {\int }_{P}f \leq M \) . On appelle alors intégrale de \( f \) le nombre réel défini par

> DEFINITION 6. Let \( f : A = {I}_{1} \times \cdots \times {I}_{n} \rightarrow \mathbb{R} \) be a positive continuous function. We say that \( f \) is integrable if there exists \( M > 0 \) such that for every compact block \( P \subset A \), we have \( {\int }_{P}f \leq M \). The integral of \( f \) is then the real number defined by

\[
{\int }_{A}f = \mathop{\sup }\limits_{{P \subset  A}}{\int }_{P}f
\]

DÉFINITION 7. Une fonction continue \( f : A \rightarrow \mathbb{R} \) est dite intégrable si \( \left| f\right| \) est intégrable. Dans ce cas, pour toute suite croissante de pavés compacts \( \left( {P}_{k}\right) \) inclus dans \( A \) telle que \( { \cup }_{k}{P}_{k} = A \) , la limite de \( \left( {{\int }_{{P}_{k}}f}\right) \) existe et ne dépend pas du choix de la suite \( \left( {P}_{k}\right) \) . Cette limite s’appelle intégrale de \( f \) et est noté \( {\int }_{A}f \) .

> DEFINITION 7. A continuous function \( f : A \rightarrow \mathbb{R} \) is said to be integrable if \( \left| f\right| \) is integrable. In this case, for any increasing sequence of compact blocks \( \left( {P}_{k}\right) \) included in \( A \) such that \( { \cup }_{k}{P}_{k} = A \), the limit of \( \left( {{\int }_{{P}_{k}}f}\right) \) exists and does not depend on the choice of the sequence \( \left( {P}_{k}\right) \). This limit is called the integral of \( f \) and is denoted by \( {\int }_{A}f \).

Remarque 7. Une moyen équivalent de définir l'intégrale d'une fonction continue réelle intégrable est d’écrire \( {\int }_{A}f = {\int }_{A}{f}^{ + } - {\int }_{A}{f}^{ - } \) où \( {f}^{ + } = \sup \{ f,0\} \) et \( {f}^{ - } = \sup \{ - f,0\} \) .

> Remark 7. An equivalent way to define the integral of an integrable real continuous function is to write \( {\int }_{A}f = {\int }_{A}{f}^{ + } - {\int }_{A}{f}^{ - } \) where \( {f}^{ + } = \sup \{ f,0\} \) and \( {f}^{ - } = \sup \{ - f,0\} \).

- L'intégrale multiple des fonctions intégrables sur \( A \) satisfait les propriétés élémentaires de l’intégrale. L’ensemble \( {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \) des fonctions continues intégrables sur \( A \) est un e.v, et l’application \( {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right)  \rightarrow  \mathbb{R}\;f \mapsto  {\int }_{A}f \) est linéaire. Si \( f, g \in  {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \) et si \( f \leq  g \) , alors \( {\int }_{A}f \leq  {\int }_{A}g \) . Enfin, si \( f \in  {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \) alors \( \left| {{\int }_{A}f}\right|  \leq  {\int }_{A}\left| f\right| \) . Par ailleurs, si \( g \) est intégrable et si \( \left| f\right|  \leq  g \) , alors \( f \) est intégrable.

> - The multiple integral of integrable functions over \( A \) satisfies the elementary properties of the integral. The set \( {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \) of continuous integrable functions over \( A \) is a vector space, and the mapping \( {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right)  \rightarrow  \mathbb{R}\;f \mapsto  {\int }_{A}f \) is linear. If \( f, g \in  {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \) and if \( f \leq  g \), then \( {\int }_{A}f \leq  {\int }_{A}g \). Finally, if \( f \in  {\mathcal{L}}^{1}\left( {A,\mathbb{R}}\right) \), then \( \left| {{\int }_{A}f}\right|  \leq  {\int }_{A}\left| f\right| \). Furthermore, if \( g \) is integrable and if \( \left| f\right|  \leq  g \), then \( f \) is integrable.

Exprimons, dans le cas particulier des intégrales doubles, la généralisation du théorème de Fubini des fonctions intégrables.

> Let us express, in the particular case of double integrals, the generalization of Fubini's theorem for integrable functions.

THÉORÉME 5. Soit I et \( {I}^{\prime } \) deux intervalles de \( \mathbb{R} \) et \( f : I \times {I}^{\prime } \rightarrow \mathbb{R} \) une fonction continue sur \( I \times {I}^{\prime } \) . Si pour tout \( x \in I \) l’application \( f\left( {x,\text{ . }}\right) {est} \) intégrable et si l’application \( g : x \mapsto \; {\int }_{{I}^{\prime }}f\left( {x,\text{ . }}\right) {estcontinueparmorceauxetint}\acute{e}{nsal} \; {\int }_{I}g \) . De même, si pour tout \( y \in {I}^{\prime } \) la fonction \( f\left( {., y}\right) \) est intégrable et si \( h : y \mapsto {\int }_{I}f\left( {.y}\right) \) est continue par morceaux et intégrable, alors \( f \) est intégrable et \( {\iint }_{I \times {I}^{\prime }}f = {\int }_{{I}^{\prime }}h \) . En particulier on a \( {\int }_{I}\left( {{\int }_{{I}^{\prime }}f\left( {., y}\right) }\right) = {\int }_{{I}^{\prime }}\left( {{\int }_{I}f\left( {x,.}\right) }\right) \) .

> THEOREM 5. Let I and \( {I}^{\prime } \) be two intervals of \( \mathbb{R} \) and \( f : I \times {I}^{\prime } \rightarrow \mathbb{R} \) be a continuous function on \( I \times {I}^{\prime } \). If for all \( x \in I \) the mapping \( f\left( {x,\text{ . }}\right) {est} \) is integrable and if the mapping \( g : x \mapsto \; {\int }_{{I}^{\prime }}f\left( {x,\text{ . }}\right) {estcontinueparmorceauxetint}\acute{e}{nsal} \; {\int }_{I}g \). Likewise, if for all \( y \in {I}^{\prime } \) the function \( f\left( {., y}\right) \) is integrable and if \( h : y \mapsto {\int }_{I}f\left( {.y}\right) \) is piecewise continuous and integrable, then \( f \) is integrable and \( {\iint }_{I \times {I}^{\prime }}f = {\int }_{{I}^{\prime }}h \). In particular, we have \( {\int }_{I}\left( {{\int }_{{I}^{\prime }}f\left( {., y}\right) }\right) = {\int }_{{I}^{\prime }}\left( {{\int }_{I}f\left( {x,.}\right) }\right) \).
