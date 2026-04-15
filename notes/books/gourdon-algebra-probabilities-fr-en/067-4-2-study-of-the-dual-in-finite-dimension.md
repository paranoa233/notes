#### 4.2. Study of the dual in finite dimension

*Français : 4.2. Étude du dual en dimension finie*

Dans cette sous-partie, sauf mention contraire, \( E \) est de dimension finie \( n \in {\mathbb{N}}^{ * } \) .

> In this subsection, unless otherwise stated, \( E \) is of finite dimension \( n \in {\mathbb{N}}^{ * } \) .

DéFINITION 3. Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . Pour tout \( i,1 \leq i \leq n \) , la forme linéaire \( {e}_{i}^{ * } \) définie sur \( B \) par \( {e}_{i}^{ * }\left( {e}_{j}\right) = 0 \) si \( j \neq i,{e}_{i}^{ * }\left( {e}_{i}\right) = 1 \) , s’appelle forme linéaire coordonnée d'indice \( i \) .

> DEFINITION 3. Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \) . For any \( i,1 \leq i \leq n \) , the linear form \( {e}_{i}^{ * } \) defined on \( B \) by \( {e}_{i}^{ * }\left( {e}_{j}\right) = 0 \) if \( j \neq i,{e}_{i}^{ * }\left( {e}_{i}\right) = 1 \) , is called the coordinate linear form of index \( i \) .

Remarque 1. Si \( E \) est de dimension infinie et \( {\left( {e}_{i}\right) }_{i \in I} \) une base de \( E \) , on définit de même les formes linéaires coordonnées \( {e}_{i}^{ * } \) pour \( i \in I \) .

> Remark 1. If \( E \) is of infinite dimension and \( {\left( {e}_{i}\right) }_{i \in I} \) is a basis of \( E \) , the coordinate linear forms \( {e}_{i}^{ * } \) for \( i \in I \) are defined in the same way.

THÉORÉME 1. Soit \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) . Alors \( {B}^{ * } = \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) est une base de \( {E}^{ * } \) appelée base duale de \( B \) , et donc dim \( {E}^{ * } = \dim E \) . Pour tout \( \varphi \in {E}^{ * } \) , on a \( \varphi = \mathop{\sum }\limits_{{i = 1}}^{n}\varphi \left( {e}_{i}\right) {e}_{i}^{ * }. \)

> THEOREM 1. Let \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \) . Then \( {B}^{ * } = \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) is a basis of \( {E}^{ * } \) called the dual basis of \( B \) , and thus dim \( {E}^{ * } = \dim E \) . For any \( \varphi \in {E}^{ * } \) , we have \( \varphi = \mathop{\sum }\limits_{{i = 1}}^{n}\varphi \left( {e}_{i}\right) {e}_{i}^{ * }. \)

Démonstration. La famille \( {B}^{ * } \) est libre, car l’égalité \( {\lambda }_{1}{e}_{1}^{ * } + \cdots + {\lambda }_{n}{e}_{n}^{ * } = 0 \) appliquée aux vecteurs \( {e}_{1},\ldots ,{e}_{n} \) de \( E \) donne \( {\lambda }_{1} = \cdots = {\lambda }_{n} = 0 \) .

> Proof. The family \( {B}^{ * } \) is linearly independent, because the equality \( {\lambda }_{1}{e}_{1}^{ * } + \cdots + {\lambda }_{n}{e}_{n}^{ * } = 0 \) applied to the vectors \( {e}_{1},\ldots ,{e}_{n} \) of \( E \) gives \( {\lambda }_{1} = \cdots = {\lambda }_{n} = 0 \) .

La famille \( {B}^{ * } \) est génératrice. En effet, si \( \varphi \in {E}^{ * } \) , alors pour tout \( x \in E, x = {\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n}{e}_{n} \) , on a

> The family \( {B}^{ * } \) is a spanning set. Indeed, if \( \varphi \in {E}^{ * } \) , then for any \( x \in E, x = {\lambda }_{1}{e}_{1} + \cdots + {\lambda }_{n}{e}_{n} \) , we have

\[
\varphi \left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\varphi \left( {e}_{i}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{e}_{i}^{ * }\left( x\right) \varphi \left( {e}_{i}\right) ,
\]

et ceci étant vrai pour tout \( x \in E \) , on a \( \varphi = \mathop{\sum }\limits_{{i = 1}}^{n}\varphi \left( {e}_{i}\right) {e}_{i}^{ * } \) .

> and since this is true for any \( x \in E \) , we have \( \varphi = \mathop{\sum }\limits_{{i = 1}}^{n}\varphi \left( {e}_{i}\right) {e}_{i}^{ * } \) .

Remarque 2. Si \( E \) est de dimension infinie et \( {\left( {e}_{i}\right) }_{i \in I} \) une base de \( E,{\left( {e}_{i}^{ * }\right) }_{i \in I} \) est une famille libre de \( {E}^{ * } \) mais non génératrice.

> Remark 2. If \( E \) is of infinite dimension and \( {\left( {e}_{i}\right) }_{i \in I} \) is a basis of \( E,{\left( {e}_{i}^{ * }\right) }_{i \in I} \) , it is a linearly independent family of \( {E}^{ * } \) but not a spanning set.

##### Bidual in finite dimension.

*Français : Bidual en dimension finie.*

THÉORÉME 2. Si \( x \in E \) , on note \( \widetilde{x} : {E}^{ * } \rightarrow \mathbb{K}\;\varphi \mapsto \varphi \left( x\right) \) . On a \( \widetilde{x} \in {E}^{* * } \) et l’application \( f : E \rightarrow {E}^{* * }\;x \mapsto \widetilde{x} \) est un isomorphisme.

> THEOREM 2. If \( x \in E \) , we denote \( \widetilde{x} : {E}^{ * } \rightarrow \mathbb{K}\;\varphi \mapsto \varphi \left( x\right) \) . We have \( \widetilde{x} \in {E}^{* * } \) and the map \( f : E \rightarrow {E}^{* * }\;x \mapsto \widetilde{x} \) is an isomorphism.

Démonstration. On vérifie facilement que \( \widetilde{x} \) est linéaire (i.e. que \( \widetilde{x} \in {E}^{* * } \) ), ainsі que \( f \) .

> Proof. It is easily verified that \( \widetilde{x} \) is linear (i.e. that \( \widetilde{x} \in {E}^{* * } \) ), as well as \( f \) .

Prouvons que \( f \) est injective. Soit \( x \in \operatorname{Ker}f \) . Si \( x \neq 0 \) , on peut compléter \( x \) en une base \( \left( {x,{e}_{2},\ldots ,{e}_{n}}\right) \) de \( E \) . On a alors \( {x}^{ * }\left( x\right) = 1 \) , autrement dit \( \widetilde{x}\left( {x}^{ * }\right) \neq 0 \) , donc \( \widetilde{x} \neq 0 \) . Donc Ker \( f = \; \{ 0\} \) .

> Let us prove that \( f \) is injective. Let \( x \in \operatorname{Ker}f \) . If \( x \neq 0 \) , we can complete \( x \) into a basis \( \left( {x,{e}_{2},\ldots ,{e}_{n}}\right) \) of \( E \) . We then have \( {x}^{ * }\left( x\right) = 1 \) , in other words \( \widetilde{x}\left( {x}^{ * }\right) \neq 0 \) , so \( \widetilde{x} \neq 0 \) . Thus Ker \( f = \; \{ 0\} \) .

D’après le théorème 1, dim \( {E}^{* * } = \dim {E}^{ * } = \dim E \) . Ainsi \( f \) est bijective, et c’est donc un isomorphisme.

> According to Theorem 1, dim \( {E}^{* * } = \dim {E}^{ * } = \dim E \) . Thus \( f \) is bijective, and is therefore an isomorphism.

Remarque 3. - Cet isomorphisme est canonique (i. e. il ne dépend pas du choix d'une base). On convient alors d’identifier \( E \) et \( {E}^{* * } \) en identifiant \( x \) à \( \widetilde{x} \) pour \( x \in E \) .

> Remark 3. - This isomorphism is canonical (i.e., it does not depend on the choice of a basis). We therefore agree to identify \( E \) and \( {E}^{* * } \) by identifying \( x \) with \( \widetilde{x} \) for \( x \in E \) .

- En dimension infinie, \( f : x \mapsto  \widetilde{x} \) est injective mais pas surjective.

> - In infinite dimension, \( f : x \mapsto  \widetilde{x} \) is injective but not surjective.

Base antéduale.

> Antidual basis.

Proposition 1. Soit \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) une base de \( {E}^{ * } \) . Il existe une unique base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de E telle que pour tout \( i,{e}_{i}^{ * } = {f}_{i} \) . Cette base s’appelle base antéduale \( {de}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \) .

> Proposition 1. Let \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) be a basis of \( {E}^{ * } \) . There exists a unique basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of E such that for all \( i,{e}_{i}^{ * } = {f}_{i} \) . This basis is called the antidual basis \( {de}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \) .

Démonstration. Existence. D’après le théorème 2, pour tout \( i \) , il existe \( {e}_{i} \in E \) tel que \( {f}_{i}^{ * } = {\widetilde{e}}_{i} \) . Donc pour tout \( j \neq i,{f}_{i}^{ * }\left( {f}_{j}\right) = 0 = {\widetilde{e}}_{i}\left( {f}_{j}\right) = {f}_{j}\left( {e}_{i}\right) \) et \( {f}_{i}^{ * }\left( {f}_{i}\right) = 1 = {f}_{i}\left( {e}_{i}\right) \) . En résumé, \( {f}_{i}\left( {e}_{j}\right) = 0 \) si \( j \neq i \) et \( {f}_{i}\left( {e}_{i}\right) = 1 \) . On voit donc que pour tout \( i,{f}_{i} = {e}_{i}^{ * } \) .

> Proof. Existence. According to Theorem 2, for all \( i \) , there exists \( {e}_{i} \in E \) such that \( {f}_{i}^{ * } = {\widetilde{e}}_{i} \) . Thus for all \( j \neq i,{f}_{i}^{ * }\left( {f}_{j}\right) = 0 = {\widetilde{e}}_{i}\left( {f}_{j}\right) = {f}_{j}\left( {e}_{i}\right) \) and \( {f}_{i}^{ * }\left( {f}_{i}\right) = 1 = {f}_{i}\left( {e}_{i}\right) \) . In summary, \( {f}_{i}\left( {e}_{j}\right) = 0 \) if \( j \neq i \) and \( {f}_{i}\left( {e}_{i}\right) = 1 \) . We therefore see that for all \( i,{f}_{i} = {e}_{i}^{ * } \) .

Unicité. Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) telle que pour tout \( i,{e}_{i}^{ * } = {f}_{i} \) . Si \( j \neq i,{e}_{i}^{ * }\left( {e}_{j}\right) = {f}_{i}\left( {e}_{j}\right) = \; 0 = \widetilde{{e}_{j}}\left( {f}_{i}\right) \) et pour tout \( i,{e}_{i}^{ * }\left( {e}_{i}\right) = {f}_{i}\left( {e}_{i}\right) = 1 = \widetilde{{e}_{i}}\left( {f}_{i}\right) \) . En résumé, on a montré que \( \widetilde{{e}_{i}}\left( {f}_{j}\right) = 0 \) si \( j \neq i, = 1 \) si \( j = i \) . Autrement dit, \( \widetilde{{e}_{i}} = {f}_{i}^{ * } \) . D’après le théorème 2, il existe un unique vecteur \( {e}_{i} \) de \( E \) vérifiant \( {\widetilde{e}}_{i} = {f}_{i}^{ * } \) ; les \( {e}_{i} \) sont donc uniques, d’où le théorème.

> Uniqueness. Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a basis of \( E \) such that for all \( i,{e}_{i}^{ * } = {f}_{i} \) . If \( j \neq i,{e}_{i}^{ * }\left( {e}_{j}\right) = {f}_{i}\left( {e}_{j}\right) = \; 0 = \widetilde{{e}_{j}}\left( {f}_{i}\right) \) and for all \( i,{e}_{i}^{ * }\left( {e}_{i}\right) = {f}_{i}\left( {e}_{i}\right) = 1 = \widetilde{{e}_{i}}\left( {f}_{i}\right) \) . In summary, we have shown that \( \widetilde{{e}_{i}}\left( {f}_{j}\right) = 0 \) if \( j \neq i, = 1 \) if \( j = i \) . In other words, \( \widetilde{{e}_{i}} = {f}_{i}^{ * } \) . According to Theorem 2, there exists a unique vector \( {e}_{i} \) of \( E \) satisfying \( {\widetilde{e}}_{i} = {f}_{i}^{ * } \) ; the \( {e}_{i} \) are therefore unique, hence the theorem.

Remarque 4. Nous verrons dans la partie 4.5 (page 136) des moyens de calcul de la base antéduale.

> Remark 4. We will see in section 4.5 (page 136) ways to calculate the dual basis.
