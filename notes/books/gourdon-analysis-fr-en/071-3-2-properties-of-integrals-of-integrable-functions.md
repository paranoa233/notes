#### 3.2. Properties of integrals of integrable functions

*Français : 3.2. Propriétés des intégrales de fonctions intégrables*

Comme pour les intégrales sur un segment de \( \mathbb{R} \) , les intégrales des fonctions intégrables possèdent les propriétés qui suivent.

> As with integrals over a segment of \( \mathbb{R} \) , the integrals of integrable functions possess the following properties.

THÉORÉME 1 (CHANGEMENT DE VARIABLE). Soit \( f : J \rightarrow E \) une fonction continue par morceaux sur \( J \) , et \( \varphi : I \rightarrow J \) une bijection de classe \( {\mathcal{C}}^{1} \) où \( J \) est un intervalle de \( \mathbb{R} \) . Alors \( f \) est intégrable sur \( J \) si et seulement si \( \left( {f \circ \varphi }\right) \times {\varphi }^{\prime } \) l’est sur I. De plus, en notant a et \( b \) les extremités de l’intervalle \( I \) et \( \varphi \left( a\right) \) et \( \varphi \left( b\right) \) les limites de \( \varphi \) en a et \( b \) , on a

> THEOREM 1 (CHANGE OF VARIABLE). Let \( f : J \rightarrow E \) be a piecewise continuous function on \( J \) , and \( \varphi : I \rightarrow J \) be a bijection of class \( {\mathcal{C}}^{1} \) where \( J \) is an interval of \( \mathbb{R} \) . Then \( f \) is integrable on \( J \) if and only if \( \left( {f \circ \varphi }\right) \times {\varphi }^{\prime } \) is on I. Furthermore, by denoting a and \( b \) as the endpoints of the interval \( I \) and \( \varphi \left( a\right) \) and \( \varphi \left( b\right) \) as the limits of \( \varphi \) at a and \( b \) , we have

\[
{\int }_{a}^{b}f\left( {\varphi \left( t\right) }\right) {\varphi }^{\prime }\left( t\right) {dt} = {\int }_{\varphi \left( a\right) }^{\varphi \left( b\right) }f\left( x\right) {dx}.
\]

THÉORÉME 2 (INÉGALITÉ DE SCHWARZ). Soient \( f, g : I \rightarrow \mathbb{K} \) deux applications continues par morceaux et telles que \( {f}^{2} \) et \( {g}^{2} \) sont intégrables sur I. Alors fg est intégrable sur I et on a

> THEOREM 2 (SCHWARZ INEQUALITY). Let \( f, g : I \rightarrow \mathbb{K} \) be two piecewise continuous mappings such that \( {f}^{2} \) and \( {g}^{2} \) are integrable on I. Then fg is integrable on I and we have

\[
{\left| {\int }_{I}\bar{f}g\right| }^{2} \leq  \left( {{\int }_{I}{\left| f\right| }^{2}}\right)  \cdot  \left( {{\int }_{I}{\left| g\right| }^{2}}\right) .
\]

Conséquence : On en déduit en particulier que si \( {f}^{2} \) et \( {g}^{2} \) sont intégrables, alors \( f + g \) est également de carré intégrable.

> Consequence: We deduce in particular that if \( {f}^{2} \) and \( {g}^{2} \) are integrable, then \( f + g \) is also square-integrable.

##### Mean convergence, quadratic convergence.

*Français : Convergence en moyenne, convergence quadratique.*

Proposition 7 (Norme de la convergence en moyenne). \( L \) ’ensemble \( {\mathcal{L}}_{c}^{1}\left( {I, E}\right) \) des fonc-tions continues de I dans \( E \) et intégrables sur I est un espace vectoriel. L'application

> Proposition 7 (Mean convergence norm). \( L \) The set \( {\mathcal{L}}_{c}^{1}\left( {I, E}\right) \) of continuous functions from I to \( E \) that are integrable on I is a vector space. The mapping

\[
{N}_{1} : {\mathcal{L}}_{c}^{1}\left( {I, E}\right)  \rightarrow  {\mathbb{R}}^{ + }\;f \mapsto  {\int }_{I}\parallel f\parallel
\]

est une norme sur \( {\mathcal{L}}_{c}^{1}\left( {I, E}\right) \) , appelée norme de la convergence en moyenne.

> is a norm on \( {\mathcal{L}}_{c}^{1}\left( {I, E}\right) \), called the mean convergence norm.

PROPOSITION 8 (Norme de la convergence en moyenne quadratique). L’ensemble \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \; \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) des fonctions continues de I dans \( \mathbb{K} \) de carré intégrable (i.e. \( {f}^{2} \) intégrable) sur I est un espace vectoriel. L'application

> PROPOSITION 8 (Quadratic mean convergence norm). The set \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \; \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) of continuous functions from I to \( \mathbb{K} \) that are square-integrable (i.e., \( {f}^{2} \) is integrable) on I is a vector space. The mapping

\[
{\mathcal{L}}_{c}^{2}{\left( I,\mathbb{K}\right) }^{2} \rightarrow  \mathbb{K},\;\left( {f, g}\right)  \mapsto  {\int }_{I}\bar{f}g
\]

est un produit scalaire sur \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \) qui fait de \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \) un espace préhilbertien. La norme associée est l'application

> is an inner product on \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \) that makes \( {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right) \) a pre-Hilbert space. The associated norm is the mapping

\[
{N}_{2} : {\mathcal{L}}_{c}^{2}\left( {I,\mathbb{K}}\right)  \rightarrow  {\mathbb{R}}^{ + }\;f \mapsto  \sqrt{{\int }_{I}{\left| f\right| }^{2}}
\]

appelée norme de la convergence en moyenne quadratique.

> called the quadratic mean convergence norm.

Théorème de convergence dominée. Voici maintenant le théorème le plus important du chapitre. Il correspond à une version aménagée, au niveau des classes préparatoire, du théorème plus général de convergence dominée dans le cadre de l'intégrale de Lebesgue. Il est puissant et très commode à utiliser, là où des approches fondées sur la convergence uniforme sont souvent plus fastidieuses.

> Dominated convergence theorem. Here is the most important theorem of the chapter. It corresponds to a version of the more general Lebesgue dominated convergence theorem adapted for preparatory classes. It is powerful and very convenient to use, where approaches based on uniform convergence are often more tedious.

- THÉORÉME 3 (CONVERGENCE DOMINÉE). Soit \( \left( {f}_{n}\right) \) une suite de fonctions continues par morceaux de I dans E, vérifiant les conditions suivantes

> - THEOREM 3 (DOMINATED CONVERGENCE). Let \( \left( {f}_{n}\right) \) be a sequence of piecewise continuous functions from I to E, satisfying the following conditions

(i) Il existe une fonction positive \( \varphi \) , continue par morceaux, intégrable sur I telle que \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq \varphi \) pour tout \( n \) (Hypothèse de domination).

> (i) There exists a positive, piecewise continuous function \( \varphi \) integrable on I such that \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq \varphi \) for all \( n \) (Domination hypothesis).

(ii) La suite de fonctions \( \left( {f}_{n}\right) \) converge simplement vers une fonction \( f : I \rightarrow E \) continue par morceaux,

> (ii) The sequence of functions \( \left( {f}_{n}\right) \) converges pointwise to a piecewise continuous function \( f : I \rightarrow E \),

Alors les \( {f}_{n} \) et \( f \) sont intégrables sur I et on a

> Then \( {f}_{n} \) and \( f \) are integrable on I and we have

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{I}{f}_{n} = {\int }_{I}f
\]

La preuve de ce résultat est hors programme des classes préparatoires. On en trouvera deux démonstrations différentes dans les problèmes 20 page 194 et 21 page 196.

> The proof of this result is outside the scope of the preparatory classes curriculum. Two different proofs can be found in problems 20 on page 194 and 21 on page 196.
