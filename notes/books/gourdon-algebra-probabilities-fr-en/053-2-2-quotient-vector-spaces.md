#### 2.2. Quotient vector spaces

*Français : 2.2. Espaces vectoriels quotients*

DéFINITION 4. Soit \( E \) un \( \mathbb{K} \) -e.v et \( F \) un s.e.v de \( E \) . La relation \( \mathcal{R} \) définie par \( (x\mathcal{R}y \Leftrightarrow \; x - y \in F \) ) est une relation d’équivalence sur \( E \) . L’espace quotient est noté \( E/F \) , et c’est un \( \mathbb{K} \) -e.v muni des lois \( \bar{x} + \bar{y} = \overline{x + y},\lambda \bar{x} = \overline{\lambda x} \) .

> DEFINITION 4. Let \( E \) be a \( \mathbb{K} \) -v.s. and \( F \) a v.s.s. of \( E \). The relation \( \mathcal{R} \) defined by \( (x\mathcal{R}y \Leftrightarrow \; x - y \in F \)) is an equivalence relation on \( E \). The quotient space is denoted by \( E/F \), and it is a \( \mathbb{K} \) -v.s. equipped with the operations \( \bar{x} + \bar{y} = \overline{x + y},\lambda \bar{x} = \overline{\lambda x} \).

DéFINITION 5. Soit \( E \) un \( \mathbb{K} \) -e.v, \( F \) un s.e.v de \( E \) . Si \( E/F \) est de dimension finie, on dit que \( F \) est de codimension finie dans \( E \) . On appelle alors codimension de \( F \) dans \( E \) l’entier \( {\operatorname{codim}}_{E}F = \dim \left( {E/F}\right) \) . Si \( {\operatorname{codim}}_{E}F = 1 \) , on dit que \( F \) est un hyperplan de \( E \) .

> DEFINITION 5. Let \( E \) be a \( \mathbb{K} \) -v.s., \( F \) a subspace of \( E \). If \( E/F \) is finite-dimensional, we say that \( F \) has finite codimension in \( E \). The integer \( {\operatorname{codim}}_{E}F = \dim \left( {E/F}\right) \) is then called the codimension of \( F \) in \( E \). If \( {\operatorname{codim}}_{E}F = 1 \), we say that \( F \) is a hyperplane of \( E \).

Proposition 2. Soit E un \( \mathbb{K} \) -e.v. Un s.e.v F de E est de codimension finie dans \( E \) si et seulement si \( F \) admet un supplémentaire \( S \) dans \( E \) de dimension finie. On a alors \( \dim S = {\operatorname{codim}}_{E}F \) .

> Proposition 2. Let E be a \( \mathbb{K} \) -v.s. A subspace F of E has finite codimension in \( E \) if and only if \( F \) admits a finite-dimensional supplementary subspace \( S \) in \( E \). We then have \( \dim S = {\operatorname{codim}}_{E}F \).

Démonstration. Condition nécessaire. Supposons \( E/F \) de dimension finie. Pour tout \( x \in E \) , on note \( \dot{x} \) sa classe dans \( E/F \) . Soit \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) une base de \( E/F \) . Soit \( S = \operatorname{Vect}{\left( {e}_{i}\right) }_{1 \leq i \leq n} \) . Alors

> Proof. Necessary condition. Suppose \( E/F \) is finite-dimensional. For any \( x \in E \), we denote by \( \dot{x} \) its class in \( E/F \). Let \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) be a basis of \( E/F \). Let \( S = \operatorname{Vect}{\left( {e}_{i}\right) }_{1 \leq i \leq n} \). Then

- \( F \cap  S = \{ 0\} \) car si \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \in  F \cap  S \) , alors \( \dot{x} = \dot{0} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\dot{e}}_{i} \) et donc pour tout \( i \) , \( {\lambda }_{i} = 0 \)

> - \( F \cap  S = \{ 0\} \) because if \( x = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \in  F \cap  S \), then \( \dot{x} = \dot{0} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\dot{e}}_{i} \) and thus for any \( i \), \( {\lambda }_{i} = 0 \)

- \( F + S = E \) . En effet, soit \( x \in  E \) . Il existe \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in  \mathbb{K} \) tels que \( \dot{x} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\dot{e}}_{i} \) . Si \( y = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \) , on a donc \( z = x - y \in  F\left( {\operatorname{car}\dot{z} = \dot{x} - \dot{y} = \dot{0}}\right) \) et \( x = z + y, y \in  S \) .

> - \( F + S = E \). Indeed, let \( x \in  E \). There exist \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in  \mathbb{K} \) such that \( \dot{x} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{\dot{e}}_{i} \). If \( y = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \), we therefore have \( z = x - y \in  F\left( {\operatorname{car}\dot{z} = \dot{x} - \dot{y} = \dot{0}}\right) \) and \( x = z + y, y \in  S \).

Donc \( F \oplus S = E \) , et \( \dim S = n = \dim \left( {E/F}\right) = {\operatorname{codim}}_{E}F \) .

> Thus \( F \oplus S = E \), and \( \dim S = n = \dim \left( {E/F}\right) = {\operatorname{codim}}_{E}F \).

Condition suffisante. Supposons \( F \oplus S = E \) , où \( S \) est de dimension finie \( n \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( S \) . Nous montrons que \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) est une base de \( E/F \) .

> Sufficient condition. Suppose \( F \oplus S = E \), where \( S \) is of finite dimension \( n \). Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( S \). We show that \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) is a basis of \( E/F \).

— \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) est une famille génératrice de \( E/F \) . En effet, si \( x \in E \) , il existe \( y \in F \) et \( z \in S \) tel que \( x = y + z \) et donc \( \dot{x} = \dot{y} + \dot{z} = \dot{z} \in \operatorname{Vect}\left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) .

> — \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) is a generating family of \( E/F \). Indeed, if \( x \in E \), there exist \( y \in F \) and \( z \in S \) such that \( x = y + z \) and thus \( \dot{x} = \dot{y} + \dot{z} = \dot{z} \in \operatorname{Vect}\left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \).

- \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) est une famille libre. En effet, si \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\dot{{e}_{i}} = \dot{0} \) , alors \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \in  F \) donc est nul car \( F \cap  S = \{ 0\} \) . Donc pour tout \( i,{\lambda }_{i} = 0 \) .

> - \( \left( {\dot{{e}_{1}},\ldots ,\dot{{e}_{n}}}\right) \) is a linearly independent family. Indeed, if \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\dot{{e}_{i}} = \dot{0} \) , then \( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i} \in  F \) therefore is zero because \( F \cap  S = \{ 0\} \) . Thus for all \( i,{\lambda }_{i} = 0 \) .

Finalement, on a donc codim \( {}_{E}F = \dim \left( {E/F}\right) = n = \dim S \) .

> Finally, we therefore have codim \( {}_{E}F = \dim \left( {E/F}\right) = n = \dim S \) .

COROLLAIRE 1. Si E est un \( \mathbb{K} \) -e.v de dimension finie, si \( F \) est un s.e.v de E, alors \( F \) est de codimension finie dans \( E \) et codim \( {}_{E}F = \dim E - \dim F \) .

> COROLLARY 1. If E is a finite-dimensional \( \mathbb{K} \) -v.s., if \( F \) is a v.s.s. of E, then \( F \) is of finite codimension in \( E \) and codim \( {}_{E}F = \dim E - \dim F \) .

##### Factorization of a linear map.

*Français : Factorisation d'une application linéaire.*

THÉORÉME 1. Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v et \( f \in \mathcal{L}\left( {E, F}\right) \) . Alors \( \operatorname{Im}f \) est isomorphe \( \dot{a} \; E/\operatorname{Ker}f \) .

> THEOREM 1. Let \( E \) and \( F \) be two \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( {E, F}\right) \) . Then \( \operatorname{Im}f \) is isomorphic to \( \dot{a} \; E/\operatorname{Ker}f \) .

\( \rightarrow \) THÉORÉME 2. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, \( F \) un \( \mathbb{K} \) -e.v et \( f \in \mathcal{L}\left( {E, F}\right) \) . Alors \( f \) est de rang fini et \( \dim E = \dim \left( {\operatorname{Ker}f}\right) + \dim \left( {\operatorname{Im}f}\right) = \dim \left( {\operatorname{Ker}f}\right) + \operatorname{rg}f \) .

> \( \rightarrow \) THEOREM 2. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., \( F \) a \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( {E, F}\right) \) . Then \( f \) is of finite rank and \( \dim E = \dim \left( {\operatorname{Ker}f}\right) + \dim \left( {\operatorname{Im}f}\right) = \dim \left( {\operatorname{Ker}f}\right) + \operatorname{rg}f \) .

COROLLAIRE 2. Soit \( f \in \mathcal{L}\left( {E, F}\right) \) où \( E \) et \( F \) sont deux \( \mathbb{K} \) -e.v de même dimension finie. Alors :

> COROLLARY 2. Let \( f \in \mathcal{L}\left( {E, F}\right) \) where \( E \) and \( F \) are two \( \mathbb{K} \) -v.s. of the same finite dimension. Then:

\[
\text{ (f est bijective) } \Leftrightarrow  \text{ (f est injective) } \Leftrightarrow  \text{ (f est surjective). }
\]

Remarque 2. Ce dernier résultat est très important. Il est faux en dimension infinie; par exemple, \( f : \mathbb{R}\left\lbrack X\right\rbrack \rightarrow \mathbb{R}\left\lbrack X\right\rbrack \;P \mapsto {P}^{\prime } \) est linéaire surjective mais pas bijective.

> Remark 2. This last result is very important. It is false in infinite dimension; for example, \( f : \mathbb{R}\left\lbrack X\right\rbrack \rightarrow \mathbb{R}\left\lbrack X\right\rbrack \;P \mapsto {P}^{\prime } \) is a surjective linear map but not bijective.
