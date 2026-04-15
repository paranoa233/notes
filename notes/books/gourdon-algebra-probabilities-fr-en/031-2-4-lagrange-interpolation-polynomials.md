#### 2.4. Lagrange interpolation polynomials

*Français : 2.4. Polynômes d'interpolation de Lagrange*

Soient \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) , deux à deux distincts, et \( {b}_{1},\ldots ,{b}_{n} \in \mathbb{K} \) . Nous allons prouver qu’il existe un unique polynôme \( L \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( L\right) \leq n - 1 \) , tel que \( \forall i, L\left( {a}_{i}\right) = {b}_{i} \) .

> Let \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{K} \) be pairwise distinct, and \( {b}_{1},\ldots ,{b}_{n} \in \mathbb{K} \) . We will prove that there exists a unique polynomial \( L \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( L\right) \leq n - 1 \) such that \( \forall i, L\left( {a}_{i}\right) = {b}_{i} \) .

- Existence. Pour \( 1 \leq  i \leq  n \) , on pose

> - Existence. For \( 1 \leq  i \leq  n \) , we define

\[
{L}_{i} = \frac{\left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{i - 1}}\right) \left( {X - {a}_{i + 1}}\right) \cdots \left( {X - {a}_{n}}\right) }{\left( {{a}_{i} - {a}_{1}}\right) \cdots \left( {{a}_{i} - {a}_{i - 1}}\right) \left( {{a}_{i} - {a}_{i + 1}}\right) \cdots \left( {{a}_{i} - {a}_{n}}\right) }
\]

(les polynômes \( {L}_{i} \) s’appellent des polynômes d’interpolation de Lagrange). On a \( {L}_{i}\left( {a}_{i}\right) = 1 \) et pour tout \( j \neq i,{L}_{i}\left( {a}_{j}\right) = 0 \) . Si \( L = \mathop{\sum }\limits_{{i = 1}}^{n}{b}_{i}{L}_{i} \) , on a alors \( L\left( {a}_{i}\right) = \; {b}_{i}{L}_{i}\left( {a}_{i}\right) = {b}_{i} \) pour tout \( i \) et comme \( \deg \left( L\right) \leq n - 1, L \) convient.

> (the polynomials \( {L}_{i} \) are called Lagrange interpolation polynomials). We have \( {L}_{i}\left( {a}_{i}\right) = 1 \) and for all \( j \neq i,{L}_{i}\left( {a}_{j}\right) = 0 \) . If \( L = \mathop{\sum }\limits_{{i = 1}}^{n}{b}_{i}{L}_{i} \) , then we have \( L\left( {a}_{i}\right) = \; {b}_{i}{L}_{i}\left( {a}_{i}\right) = {b}_{i} \) for all \( i \) and since \( \deg \left( L\right) \leq n - 1, L \) works.

- Unicité. Supposons que \( F \) et \( G \) conviennent. On pose \( H = F - G \) . Pour tout \( i,1 \leq  i \leq  n \) , on a \( H\left( {a}_{i}\right)  = F\left( {a}_{i}\right)  - G\left( {a}_{i}\right)  = {b}_{i} - {b}_{i} = 0 \) . Le polynôme \( H \) a donc au moins \( n \) racines. Or \( \deg \left( H\right)  \leq  n - 1 \) , donc d’après la conséquence de la proposition \( 2, H = 0 \) , c’est-à-dire \( F = G \) .

> - Uniqueness. Suppose \( F \) and \( G \) are suitable. Let \( H = F - G \) . For all \( i,1 \leq  i \leq  n \) , we have \( H\left( {a}_{i}\right)  = F\left( {a}_{i}\right)  - G\left( {a}_{i}\right)  = {b}_{i} - {b}_{i} = 0 \) . The polynomial \( H \) therefore has at least \( n \) roots. However, \( \deg \left( H\right)  \leq  n - 1 \) , so according to the consequence of proposition \( 2, H = 0 \) , that is \( F = G \) .

Remarque 7. Il existe une autre expression utile de \( L \) . Posons \( \Phi = \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) et pour tout \( i,1 \leq i \leq n,{\Phi }_{i} \) le polynôme tel que \( \Phi = \left( {X - {a}_{i}}\right) {\Phi }_{i} \) . Par dérivation, on obtient \( {\Phi }^{\prime } = {\Phi }_{i} + \left( {X - {a}_{i}}\right) {\Phi }_{i}^{\prime } \) et donc \( {\Phi }^{\prime }\left( {a}_{i}\right) = {\Phi }_{i}\left( {a}_{i}\right) \) , d’où on tire

> Remark 7. There is another useful expression for \( L \) . Let \( \Phi = \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) and for all \( i,1 \leq i \leq n,{\Phi }_{i} \) the polynomial such that \( \Phi = \left( {X - {a}_{i}}\right) {\Phi }_{i} \) . By differentiation, we obtain \( {\Phi }^{\prime } = {\Phi }_{i} + \left( {X - {a}_{i}}\right) {\Phi }_{i}^{\prime } \) and thus \( {\Phi }^{\prime }\left( {a}_{i}\right) = {\Phi }_{i}\left( {a}_{i}\right) \) , from which we derive

\[
{L}_{i}\left( X\right)  = \frac{{\Phi }_{i}\left( X\right) }{{\Phi }_{i}\left( {a}_{i}\right) } = \frac{\Phi \left( X\right) }{\left( {X - {a}_{i}}\right) {\Phi }^{\prime }\left( {a}_{i}\right) }\;\text{ donc }\;L\left( X\right)  = \Phi \left( X\right) \left( {\mathop{\sum }\limits_{{i = 1}}^{n}\frac{{b}_{i}}{\left( {X - {a}_{i}}\right) {\Phi }^{\prime }\left( {a}_{i}\right) }}\right) .
\]

Remarque 8. Plus généralement, on peut définir l'interpolation de Hermite en imposant au polynôme interpolant des conditions sur l'évaluation et les dérivées aux abscisses \( {a}_{i} \) (voir l'exercice 7 page 70).

> Remark 8. More generally, one can define Hermite interpolation by imposing conditions on the interpolating polynomial regarding the evaluation and derivatives at the abscissae \( {a}_{i} \) (see exercise 7 on page 70).
