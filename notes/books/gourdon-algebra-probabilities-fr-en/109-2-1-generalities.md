#### 2.1. Generalities

*Français : 2.1. Généralités*

Soit \( \Phi \) une forme quadratique (resp. hermitienne) sur un \( \mathbb{R} \) -e.v (resp. un \( \mathbb{C} \) -e.v) \( E \) . On rappelle que \( \Phi \) est positive si pour tout \( x \in E,\Phi \left( x\right) \geq 0 \) .

> Let \( \Phi \) be a quadratic (resp. Hermitian) form on an \( \mathbb{R} \)-v.s. (resp. a \( \mathbb{C} \)-v.s.) \( E \). Recall that \( \Phi \) is positive if for all \( x \in E,\Phi \left( x\right) \geq 0 \) .

Supposons \( \Phi \) définie positive. Sa forme polaire \( \varphi \) s’appelle un produit scalaire (resp. un produit scalaire hermitien). On note souvent \( \varphi \left( {x, y}\right) = x \cdot y \) (ou \( \left( {x \mid y}\right) \) , ou encore \( \langle x, y\rangle \) ). On a \( x \cdot y = y \cdot x \) (resp. \( x \cdot y = \overline{y \cdot x} \) ). On écrit souvent \( {x}^{2} \) pour \( x \cdot x \) .

> Suppose \( \Phi \) is positive definite. Its polar form \( \varphi \) is called an inner product (resp. a Hermitian inner product). It is often denoted by \( \varphi \left( {x, y}\right) = x \cdot y \) (or \( \left( {x \mid y}\right) \), or \( \langle x, y\rangle \)). We have \( x \cdot y = y \cdot x \) (resp. \( x \cdot y = \overline{y \cdot x} \)). We often write \( {x}^{2} \) for \( x \cdot x \).

Dans ce cas, l'inégalité de Minkowsky (voir le corollaire 2 de la partie précédente) montre que \( \parallel x\parallel = \sqrt{\Phi \left( x\right) } = \sqrt{x \cdot x} \) définit une norme sur \( E \) . Cette norme s’appelle norme euclidienne (resp. norme hermitienne) et fait de \( E \) un e.v normé.

> In this case, Minkowski's inequality (see corollary 2 of the previous section) shows that \( \parallel x\parallel = \sqrt{\Phi \left( x\right) } = \sqrt{x \cdot x} \) defines a norm on \( E \). This norm is called the Euclidean norm (resp. Hermitian norm) and makes \( E \) a normed v.s.

Un R-e.v muni d'un produit scalaire s'appelle un espace préhilbertien réel (s'il est de plus complet - pour la norme issue du produit scalaire - on dit que c'est un espace hilbertien réel). S'il est de dimension finie, on l'appelle également espace euclidien. Sauf mention explicite, la norme utilisée sur un espace préhiblertien est la norme euclidienne.

> An R-v.s. equipped with an inner product is called a real pre-Hilbert space (if it is also complete—for the norm derived from the inner product—it is called a real Hilbert space). If it is finite-dimensional, it is also called a Euclidean space. Unless explicitly stated otherwise, the norm used on a pre-Hilbert space is the Euclidean norm.

Un C-e.v muni d'un produit scalaire hermitien s'appelle un espace préhilbertien com-plexe. S'il est de dimension finie, on l'appelle également espace hermitien.

> A C-v.s. equipped with a Hermitian inner product is called a complex pre-Hilbert space. If it is finite-dimensional, it is also called a Hermitian space.

L'inégalité de Schwarz

> The Cauchy-Schwarz inequality

\[
\forall x, y \in  E,\;\left| {x \cdot  y}\right|  \leq  \parallel x\parallel  \cdot  \parallel y\parallel
\]

entraîne la continuité du produit scalaire dans l’espace préhibertien \( E \) . Si \( E \) est un espace préhilbertien réel, cette inégalité entraîne

> implies the continuity of the inner product in the pre-Hilbert space \( E \). If \( E \) is a real pre-Hilbert space, this inequality implies

\[
\forall x, y \in  E, x \neq  0, y \neq  0,\exists !\theta  \in  \left\lbrack  {0,\pi }\right\rbrack  ,\;\cos \theta  = \frac{x \cdot  y}{\parallel x\parallel  \cdot  \parallel y\parallel }.
\]

Le nombre réel \( \theta \) s’appelle l’écart angulaire de \( x \) et \( y \) .

> The real number \( \theta \) is called the angular deviation of \( x \) and \( y \).

Remarque 1. On ne définit pas l'écart angulaire dans un espace préhilbertien complexe.

> Remark 1. The angular deviation is not defined in a complex pre-Hilbert space.

Dans toute la suite, nous utiliserons ces notations.

> Throughout the following, we will use these notations.
