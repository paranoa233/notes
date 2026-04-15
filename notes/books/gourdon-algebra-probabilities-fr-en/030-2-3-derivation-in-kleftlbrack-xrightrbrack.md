#### 2.3. Derivation in \( \mathbb{K}\left\lbrack X\right\rbrack \)

*Français : 2.3. Dérivation dans \( \mathbb{K}\left\lbrack X\right\rbrack \)*

DÉFINITION 4. Soit \( F = {a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) . On appelle polynôme dérivé de \( F \) le polynôme \( {F}^{\prime } = {a}_{1} + 2{a}_{2}X + \cdots n{a}_{n}{X}^{n - 1} \) .

> DEFINITION 4. Let \( F = {a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) . The derivative polynomial of \( F \) is the polynomial \( {F}^{\prime } = {a}_{1} + 2{a}_{2}X + \cdots n{a}_{n}{X}^{n - 1} \) .

Remarque 5. - Si \( F \) est constant, \( {F}^{\prime } = 0 \) . La réciproque est vraie si \( \mathbb{K} \) est de caractéristique 0, fausse en caractéristique non nulle (par exemple si \( F = {X}^{2} + \dot{1} \in \; \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) , on a \( {F}^{\prime } = \dot{2}X = \dot{0} \) et pourtant \( F \) n’est pas une constante).

> Remark 5. - If \( F \) is constant, \( {F}^{\prime } = 0 \) . The converse is true if \( \mathbb{K} \) has characteristic 0, and false in non-zero characteristic (for example if \( F = {X}^{2} + \dot{1} \in \; \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) , we have \( {F}^{\prime } = \dot{2}X = \dot{0} \) and yet \( F \) is not a constant).

- Les règles de dérivations de somme, produit et composée pour les polynômes sont identiques aux règles de dérivations usuelles sur les fonctions dérivables. D'ailleurs, sur \( \mathbb{R}\left\lbrack  X\right\rbrack \) , la fonction polynôme dérivé coïncide avec la dérivée de la fonction po-lynôme. Comme pour les fonctions dérivées, on note \( {F}^{\prime \prime } \) le polynôme dérivé de \( {F}^{\prime } \) , et par récurrence sur \( n \in  \mathbb{N} * \) on définit \( {F}^{\left( n\right) } \) le polynôme dérivé de \( {F}^{\left( n - 1\right) } \) .

> - The derivation rules for sums, products, and compositions for polynomials are identical to the usual derivation rules for differentiable functions. Moreover, over \( \mathbb{R}\left\lbrack  X\right\rbrack \) , the derivative polynomial function coincides with the derivative of the polynomial function. As with derivative functions, we denote \( {F}^{\prime \prime } \) as the derivative polynomial of \( {F}^{\prime } \) , and by induction on \( n \in  \mathbb{N} * \) we define \( {F}^{\left( n\right) } \) as the derivative polynomial of \( {F}^{\left( n - 1\right) } \) .

THÉORÉME 2 (FORMULE DE TAYLOR). Si le corps \( \mathbb{K} \) est de caractéristique nulle, tout polynôme \( F \) de \( \mathbb{K}\left\lbrack X\right\rbrack \) de degré inférieur ou égal à n vérifie

> THEOREM 2 (TAYLOR'S FORMULA). If the field \( \mathbb{K} \) has characteristic zero, any polynomial \( F \) of \( \mathbb{K}\left\lbrack X\right\rbrack \) of degree less than or equal to n satisfies

\[
\forall a \in  \mathbb{K},\;F\left( X\right)  = F\left( a\right)  + \frac{\left( X - a\right) }{1!}{F}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( X - a\right) }^{n}}{n!}{F}^{\left( n\right) }\left( a\right) .
\]

Une conséquence importante de la formule de Taylor est la caractérisation de l'ordre d'une racine :

> An important consequence of Taylor's formula is the characterization of the order of a root:

\( \rightarrow \) THÉORÉME 3. Si le corps \( \mathbb{K} \) est de caractéristique 0, et si \( F \in \mathbb{K}\left\lbrack X\right\rbrack , F \neq 0 \) , alors \( a \in \mathbb{K} \) est racine d’ordre h de \( F \) si et seulement si

> \( \rightarrow \) THEOREM 3. If the field \( \mathbb{K} \) has characteristic 0, and if \( F \in \mathbb{K}\left\lbrack X\right\rbrack , F \neq 0 \) , then \( a \in \mathbb{K} \) is a root of order h of \( F \) if and only if

\[
\text{ (i) }\forall i,0 \leq  i \leq  h - 1,{F}^{\left( i\right) }\left( a\right)  = 0\;\text{ (ii) }{F}^{\left( h\right) }\left( a\right)  \neq  0\text{ . }
\]

Remarque 6. - Le cas de \( F = {X}^{3} \in \mathbb{Z}/3\mathbb{Z}\left\lbrack X\right\rbrack \) et \( a = \dot{0} \) montre que ceci est faux en caractéristique non nulle ( \( a \) est racine d’ordre 3 de \( F \) et pourtant \( {F}^{\left( 3\right) }\left( a\right) = \dot{0} \) ).

> Remark 6. - The case of \( F = {X}^{3} \in \mathbb{Z}/3\mathbb{Z}\left\lbrack X\right\rbrack \) and \( a = \dot{0} \) shows that this is false in non-zero characteristic ( \( a \) is a root of order 3 of \( F \) and yet \( {F}^{\left( 3\right) }\left( a\right) = \dot{0} \) ).

- Le résultat du théorème reste vrai en caractéristique quelconque pour caractériser les racines simples. Plus précisément, on a le résultat suivant.

> - The result of the theorem remains true in any characteristic for characterizing simple roots. More precisely, we have the following result.

\( {SiF} \in \mathbb{K}\left\lbrack X\right\rbrack , F \neq 0 \) , et si \( a \in \mathbb{K} \) , alors a est racine simple de \( F \) si et seulement si \( F\left( a\right) = 0 \) et \( {F}^{\prime }\left( a\right) \neq 0 \) .

> \( {SiF} \in \mathbb{K}\left\lbrack X\right\rbrack , F \neq 0 \) , and if \( a \in \mathbb{K} \) , then a is a simple root of \( F \) if and only if \( F\left( a\right) = 0 \) and \( {F}^{\prime }\left( a\right) \neq 0 \) .

En effet. Si \( F = \left( {X - a}\right) G \) , alors \( {F}^{\prime } = G + \left( {X - a}\right) {G}^{\prime } \) donc \( {F}^{\prime }\left( a\right) = G\left( a\right) \) et on en déduit facilement le résultat.

> Indeed. If \( F = \left( {X - a}\right) G \) , then \( {F}^{\prime } = G + \left( {X - a}\right) {G}^{\prime } \) so \( {F}^{\prime }\left( a\right) = G\left( a\right) \) and we easily deduce the result.
