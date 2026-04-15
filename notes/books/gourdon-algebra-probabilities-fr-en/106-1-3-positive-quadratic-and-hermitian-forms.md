#### 1.3. Positive quadratic and Hermitian forms

*Français : 1.3. Formes quadratiques et hermitiennes positives*

Ici aussi, \( \Phi \) désigne une forme quadratique sur un \( \mathbb{R} \) -e.v \( E \) ou une forme hermitienne sur un \( \mathbb{C} \) -e.v \( E \) , associé à la forme polaire \( \varphi \) . On dira que \( \Phi \) est positive si pour tout \( x \in E,\Phi \left( x\right) \geq 0 \) . En dimension finie, la signature d’une forme positive est de la forme \( \left( {p,0}\right) \) .

> Here again, \( \Phi \) denotes a quadratic form on an \( \mathbb{R} \) -v.s. \( E \) or a Hermitian form on a \( \mathbb{C} \) -v.s. \( E \) , associated with the polar form \( \varphi \) . We say that \( \Phi \) is positive if for all \( x \in E,\Phi \left( x\right) \geq 0 \) . In finite dimension, the signature of a positive form is of the form \( \left( {p,0}\right) \) .

\( \rightarrow \) THÉORÉME 3 (INÉGALITÉ DE SCHWARZ). Si \( \Phi \) est positive, alors

> \( \rightarrow \) THEOREM 3 (SCHWARZ INEQUALITY). If \( \Phi \) is positive, then

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;{\left| \varphi \left( x, y\right) \right| }^{2} \leq  \Phi \left( x\right) \Phi \left( y\right) .
\]

(*)

> Si de plus \( \Phi \) est définie, il y a égalité si et seulement si x et y forment une famille liée.

If, furthermore, \( \Phi \) is definite, equality holds if and only if x and y are linearly dependent.

> Démonstration. Même si \( \Phi \) est une forme hermitienne, on peut supposer \( \varphi \left( {x, y}\right) \in \mathbb{R} \) , quitte à multiplier \( x \) par \( {e}^{i\theta } \) avec \( \theta \in \mathbb{R} \) bien choisi. On a

Proof. Even if \( \Phi \) is a Hermitian form, we can assume \( \varphi \left( {x, y}\right) \in \mathbb{R} \) , by multiplying \( x \) by \( {e}^{i\theta } \) with a well-chosen \( \theta \in \mathbb{R} \) . We have

\[
\forall \lambda  \in  \mathbb{R},\;\Phi \left( {{\lambda x} + y}\right)  = {\lambda }^{2}\Phi \left( x\right)  + {2\lambda \varphi }\left( {x, y}\right)  + \Phi \left( y\right)  \geq  0.
\]

\( \left( {* * }\right) \)

> Si \( \Phi \left( x\right) = 0 \) , pour tout \( \lambda \in \mathbb{R} \) , \( \left( {* * }\right) \) s’écrit \( {2\lambda \varphi }\left( {x, y}\right) + \Phi \left( y\right) \geq 0 \) , ce qui entraîne \( \varphi \left( {x, y}\right) = 0 \) .

If \( \Phi \left( x\right) = 0 \) , for all \( \lambda \in \mathbb{R} \) , \( \left( {* * }\right) \) is written as \( {2\lambda \varphi }\left( {x, y}\right) + \Phi \left( y\right) \geq 0 \) , which implies \( \varphi \left( {x, y}\right) = 0 \) .

> Sinon \( \Phi \left( x\right) \neq 0 \) , et le trinôme du second degré \( \left( {* * }\right) \) en \( \lambda \) a un discriminant négatif, ce qui s’écrit \( \varphi {\left( x, y\right) }^{2} - \Phi \left( x\right) \Phi \left( y\right) \leq 0 \) , d’où l’inégalité.

Otherwise \( \Phi \left( x\right) \neq 0 \) , and the second-degree trinomial \( \left( {* * }\right) \) in \( \lambda \) has a negative discriminant, which is written as \( \varphi {\left( x, y\right) }^{2} - \Phi \left( x\right) \Phi \left( y\right) \leq 0 \) , hence the inequality.

> Supposons \( \Phi \) définie et \( x \neq 0 \) (le cas \( x = 0 \) est trivial). Alors \( \Phi \left( x\right) \neq 0 \) , de sorte que \( \left( *\right) \) est une égalité si et seulement si le discriminant de \( \left( {* * }\right) \) est nul, c'est à dire si et seulement s'il existe \( {\lambda }_{0} \in \mathbb{R} \) tel que \( \Phi \left( {{\lambda }_{0}x + y}\right) = 0 \) , ce qui équivaut à \( {\lambda }_{0}x + y = 0 \) puisque \( \Phi \) est définie, c’est-à-dire que la famille \( \left( {x, y}\right) \) est liée.

Suppose \( \Phi \) is definite and \( x \neq 0 \) (the case \( x = 0 \) is trivial). Then \( \Phi \left( x\right) \neq 0 \) , so that \( \left( *\right) \) is an equality if and only if the discriminant of \( \left( {* * }\right) \) is zero, that is if and only if there exists \( {\lambda }_{0} \in \mathbb{R} \) such that \( \Phi \left( {{\lambda }_{0}x + y}\right) = 0 \) , which is equivalent to \( {\lambda }_{0}x + y = 0 \) since \( \Phi \) is definite, meaning that the family \( \left( {x, y}\right) \) is linearly dependent.

> Conséquence. Si \( \Phi \) est positive, alors \( {C}_{\Phi } = \operatorname{Ker}\Phi ,{C}_{\Phi } \) désignant le cône isotrope de \( \Phi \) . En particulier, une forme positive \( \Phi \) est définie si et seulement si elle est non dégénérée.

Consequence. If \( \Phi \) is positive, then \( {C}_{\Phi } = \operatorname{Ker}\Phi ,{C}_{\Phi } \) denotes the isotropic cone of \( \Phi \) . In particular, a positive form \( \Phi \) is definite if and only if it is non-degenerate.

> COROLLAIRE 2 (Inégalité de Minkowsky). Si \( \Phi \) est positive, alors

COROLLARY 2 (Minkowski's inequality). If \( \Phi \) is positive, then

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\sqrt{\Phi \left( {x + y}\right) } \leq  \sqrt{\Phi \left( x\right) } + \sqrt{\Phi \left( y\right) }.
\]

L'inégalité de Minkowsky est une conséquence immédiate de l'inégalité de Schwarz. Elle exprime que si \( \Phi \) est positive, \( S\left( x\right) = \sqrt{\Phi \left( x\right) } \) définit une semi-norme. Si de plus \( \Phi \) est définie, \( S \) est une norme (on dit alors que \( \varphi \) est un produit scalaire, voir la section 2).

> Minkowski's inequality is an immediate consequence of the Schwarz inequality. It states that if \( \Phi \) is positive, \( S\left( x\right) = \sqrt{\Phi \left( x\right) } \) defines a semi-norm. If, in addition, \( \Phi \) is definite, \( S \) is a norm (we then say that \( \varphi \) is an inner product, see section 2).
