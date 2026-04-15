#### 5.1. Multilinear forms

*Français : 5.1. Formes multilinéaires*

DéFINITION 1. Soient des \( \mathbb{K} \) -e.v \( {E}_{1},\ldots ,{E}_{p} \) et \( F \) . Une application

> DEFINITION 1. Let \( \mathbb{K} \) -v.s. be \( {E}_{1},\ldots ,{E}_{p} \) and \( F \) . A map

\[
f : {E}_{1} \times  \cdots  \times  {E}_{p} \rightarrow  F\;\left( {{x}_{1},\ldots ,{x}_{p}}\right)  \mapsto  f\left( {{x}_{1},\ldots ,{x}_{p}}\right)
\]

est dite \( p \) -linéaire si en tout point les \( p \) applications partielles sont linéaires. Si \( p = 2 \) , \( f \) est dite bilinéaire. L’ensemble de ces applications est noté \( \mathcal{L}\left( {{E}_{1},\ldots ,{E}_{p}, F}\right) \) . C’est un \( \mathbb{K} \) -e.v. Si \( {E}_{1} = \cdots = {E}_{p} = E \) et \( F = \mathbb{K} \) , on parle de forme p-linéaire sur \( E \) , et l’ensemble des formes \( p \) -linéaires sur \( E \) est noté \( {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) .

> is said to be \( p \) -linear if at every point the \( p \) partial maps are linear. If \( p = 2 \) , \( f \) is said to be bilinear. The set of these maps is denoted by \( \mathcal{L}\left( {{E}_{1},\ldots ,{E}_{p}, F}\right) \) . It is a \( \mathbb{K} \) -v.s. If \( {E}_{1} = \cdots = {E}_{p} = E \) and \( F = \mathbb{K} \) , we speak of a p-linear form on \( E \) , and the set of \( p \) -linear forms on \( E \) is denoted by \( {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) .

Exemple 1. - L’application \( {E}^{ * } \times E \rightarrow \mathbb{K}\;\left( {\varphi , x}\right) \mapsto \varphi \left( x\right) = \langle \varphi , x\rangle \) est une forme bilinéaire.

> Example 1. - The map \( {E}^{ * } \times E \rightarrow \mathbb{K}\;\left( {\varphi , x}\right) \mapsto \varphi \left( x\right) = \langle \varphi , x\rangle \) is a bilinear form.

- Si \( {\varphi }_{1},\ldots ,{\varphi }_{p} \in  {E}^{ * } \) , l’application \( {E}^{p} \rightarrow  \mathbb{K}\;\left( {{x}_{1},\ldots ,{x}_{p}}\right)  \mapsto  {\varphi }_{1}\left( {x}_{1}\right) \cdots {\varphi }_{p}\left( {x}_{p}\right) \) est une forme \( p \) -linéaire sur \( E \) .

> - If \( {\varphi }_{1},\ldots ,{\varphi }_{p} \in  {E}^{ * } \) , the map \( {E}^{p} \rightarrow  \mathbb{K}\;\left( {{x}_{1},\ldots ,{x}_{p}}\right)  \mapsto  {\varphi }_{1}\left( {x}_{1}\right) \cdots {\varphi }_{p}\left( {x}_{p}\right) \) is a \( p \) -linear form on \( E \) .

Proposition 1. \( \dim {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) = {\left( \dim E\right) }^{p} \) .

> Proposition 1. \( \dim {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) = {\left( \dim E\right) }^{p} \) .

DéFINITION 2. Soit \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) .

> DEFINITION 2. Let \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) .

- \( f \) est dite alternée si \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right)  = 0 \) dès que deux vecteurs parmi les \( {x}_{i} \) sont égaux.

> - \( f \) is said to be alternating if \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right)  = 0 \) whenever two vectors among the \( {x}_{i} \) are equal.

- \( f \) est dite antisymétrique si l’échange de deux vecteurs dans la suite \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) donne à \( f \) des valeurs opposées.

> - \( f \) is said to be antisymmetric if swapping two vectors in the sequence \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) gives \( f \) opposite values.

Remarque 1. On montre facilement que \( f \) est antisymétrique si et seulement si pour tout \( \sigma \in {\mathcal{S}}_{p} \) (groupe des permutations de \( \{ 1,\ldots , p\} \) ) et pour tout \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {E}^{p} \) , on a

> Remark 1. It is easily shown that \( f \) is antisymmetric if and only if for all \( \sigma \in {\mathcal{S}}_{p} \) (group of permutations of \( \{ 1,\ldots , p\} \)) and for all \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {E}^{p} \), we have

\[
f\left( {{x}_{\sigma \left( 1\right) },\ldots ,{x}_{\sigma \left( p\right) }}\right)  = \varepsilon \left( \sigma \right) f\left( {{x}_{1},\ldots ,{x}_{p}}\right) ,
\]

\( \varepsilon \left( \sigma \right) \) étant la signature de \( \sigma \) .

> \( \varepsilon \left( \sigma \right) \) being the signature of \( \sigma \).

THÉORÉME 1. Soient \( \mathbb{K} \) un corps commutatif de caractéristique différente de 2, \( E \) un \( \mathbb{K} \) -e.v et \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) . Alors \( f \) est antisymétrique si et seulement si \( f \) est alternée.

> THEOREM 1. Let \( \mathbb{K} \) be a commutative field of characteristic other than 2, \( E \) a \( \mathbb{K} \)-v.s. and \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \). Then \( f \) is antisymmetric if and only if \( f \) is alternating.

Proposition 2. Soit \( E \) un \( \mathbb{K} \) -e.v, \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) alternée. \( {Si}\left( {{x}_{1},\ldots ,{x}_{p}}\right) \) est un système lié, alors \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) = 0 \) .

> Proposition 2. Let \( E \) be a \( \mathbb{K} \)-v.s., \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) alternating. \( {Si}\left( {{x}_{1},\ldots ,{x}_{p}}\right) \) is a linearly dependent system, then \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) = 0 \).

COROLLAIRE 1. Soit \( f \) une forme p-linéaire alternée sur E. On ne change pas la valeur de \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) \) en ajoutant à un des vecteurs \( {x}_{i} \) une combinaison linéaire des autres vecteurs.

> COROLLARY 1. Let \( f \) be an alternating p-linear form on E. The value of \( f\left( {{x}_{1},\ldots ,{x}_{p}}\right) \) remains unchanged if a linear combination of the other vectors is added to one of the vectors \( {x}_{i} \).

DÉFINITION 3 (ANTISYMÉTRISATION D'UNE FORME p-LINÉAIRE). Pour toute forme \( p \) -linéaire \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \) , on note

> DEFINITION 3 (ANTISYMMETRIZATION OF A p-LINEAR FORM). For any \( p \)-linear form \( f \in {\mathcal{L}}_{p}\left( {E,\mathbb{K}}\right) \), we denote

\[
{f}^{\natural } : {E}^{p} \rightarrow  \mathbb{K}\;\left( {{x}_{1},\ldots ,{x}_{p}}\right)  \mapsto  \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{p}}}\varepsilon \left( \sigma \right) f\left( {{x}_{\sigma \left( 1\right) },\ldots ,{x}_{\sigma \left( p\right) }}\right) .
\]

Ainsi construite, \( {f}^{\natural } \) est une forme \( p \) -linéaire alternée.

> Constructed in this way, \( {f}^{\natural } \) is an alternating \( p \)-linear form.
