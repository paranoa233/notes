#### 2.1. Generalities

*Français : 2.1. Généralités*

DéFINITION 1. Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v et \( f : E \rightarrow F \) une application. On dit que \( f \) est linéaire si

> DEFINITION 1. Let \( E \) and \( F \) be two \( \mathbb{K} \) -vector spaces and \( f : E \rightarrow F \) a map. We say that \( f \) is linear if

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\forall \left( {\lambda ,\mu }\right)  \in  {\mathbb{K}}^{2},\;f\left( {{\lambda x} + {\mu y}}\right)  = {\lambda f}\left( x\right)  + {\mu f}\left( y\right) .
\]

L’ensemble des applications linéaires de \( E \) dans \( F \) est un \( \mathbb{K} \) -e.v noté \( \mathcal{L}\left( {E, F}\right) \) .

> The set of linear maps from \( E \) to \( F \) is a \( \mathbb{K} \) -vector space denoted by \( \mathcal{L}\left( {E, F}\right) \) .

Exemple 1. - L’application \( \varphi : \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{0}^{1}f\left( t\right) {dt} \) est linéaire.

> Example 1. - The map \( \varphi : \mathcal{C}\left( {\left\lbrack {0,1}\right\rbrack ,\mathbb{R}}\right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{0}^{1}f\left( t\right) {dt} \) is linear.

- Si \( \lambda  \in  \mathbb{K} \) , lapplication \( \varphi  : E \rightarrow  E\;x \mapsto  {\lambda x} \) est linéaire.

> - If \( \lambda  \in  \mathbb{K} \), the map \( \varphi  : E \rightarrow  E\;x \mapsto  {\lambda x} \) is linear.

Remarque 1. - Une application linéaire de \( E \) dans \( \mathbb{K} \) est appelée forme linéaire.

> Remark 1. - A linear map from \( E \) to \( \mathbb{K} \) is called a linear form.

- Une application linéaire de \( E \) dans \( E \) est appelée endomorphisme.

> - A linear map from \( E \) to \( E \) is called an endomorphism.

- Si \( f \) est linéaire, alors \( f\left( 0\right)  = 0 \) .

> - If \( f \) is linear, then \( f\left( 0\right)  = 0 \).

- La composée de deux applications linéaires est linéaire.

> - The composition of two linear maps is linear.

- Si \( f : E \rightarrow  F \) est linéaire et bijective, on dit que \( f \) est un isomorphisme de \( \mathbb{K} \) -e.v. L’application \( {f}^{-1} : F \rightarrow  E \) est aussi linéaire.

> - If \( f : E \rightarrow  F \) is linear and bijective, we say that \( f \) is an isomorphism of \( \mathbb{K} \) -v.s. The map \( {f}^{-1} : F \rightarrow  E \) is also linear.

- Si \( f \in  \mathcal{L}\left( {E, F}\right) \) , la linéarité de \( f \) entraîne que pour connaître (resp. pour définir) \( f \) , il suffit de la connaître (resp. définir) sur une base de \( E \) .

> - If \( f \in  \mathcal{L}\left( {E, F}\right) \), the linearity of \( f \) implies that to know (resp. to define) \( f \), it is sufficient to know (resp. define) it on a basis of \( E \).

PROPOSITION 1. L'image (ou l'image réciproque) d'un s.e.v par une application linéaire est un s.e.v.

> PROPOSITION 1. The image (or inverse image) of a v.s.s. under a linear map is a v.s.s.

DéFINITION 2. Soient \( E \) et \( F \) des \( \mathbb{K} \) -e.v et \( f \in \mathcal{L}\left( {E, F}\right) \) . On appelle noyau de \( f \) l’ensemble noté Ker \( f = {f}^{-1}\left( {\{ 0\} }\right) = \{ x \in E \mid f\left( x\right) = 0\} \) . On appelle image de \( f \) l’ensemble noté \( \operatorname{Im}f = f\left( E\right) \) . Les ensembles Ker \( f \) et \( \operatorname{Im}f \) sont des s.e.v. Par ailleurs, \( f \) est injective si et seulement si Ker \( f = \{ 0\} \) .

> DEFINITION 2. Let \( E \) and \( F \) be \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( {E, F}\right) \). We call the kernel of \( f \) the set denoted by Ker \( f = {f}^{-1}\left( {\{ 0\} }\right) = \{ x \in E \mid f\left( x\right) = 0\} \). We call the image of \( f \) the set denoted by \( \operatorname{Im}f = f\left( E\right) \). The sets Ker \( f \) and \( \operatorname{Im}f \) are v.s.s. Furthermore, \( f \) is injective if and only if Ker \( f = \{ 0\} \).

DéFINITION 3. Soient \( E \) et \( F \) des \( \mathbb{K} \) -e.v et \( f \in \mathcal{L}\left( {E, F}\right) \) . Si Im \( f \) est de dimension finie, on dit que \( f \) est de rang fini, et l’entier dim \( \left( {\operatorname{Im}f}\right) \) est appelé rang de \( f \) , noté rg \( f \) .

> DEFINITION 3. Let \( E \) and \( F \) be \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( {E, F}\right) \). If Im \( f \) is finite-dimensional, we say that \( f \) is of finite rank, and the integer dim \( \left( {\operatorname{Im}f}\right) \) is called the rank of \( f \), denoted by rg \( f \).
