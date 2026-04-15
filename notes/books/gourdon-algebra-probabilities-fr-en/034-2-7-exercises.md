#### 2.7. Exercises

*Français : 2.7. Exercices*

EXERCICE 1. Montrer qu'un corps fini n'est pas algébriquement clos.

> EXERCISE 1. Show that a finite field is not algebraically closed.

Solution. Soit \( \mathbb{K} = \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \) un corps fini. Le polynôme \( P = 1 + \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) vérifie \( P\left( {a}_{i}\right) = 1 \) pour tout \( i \) . Donc \( P\mathrm{n} \) ’a pas de racine dans \( \mathbb{K} \) , et \( \mathbb{K}\mathrm{n} \) ’est pas algébriquement clos.

> Solution. Let \( \mathbb{K} = \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \) be a finite field. The polynomial \( P = 1 + \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) satisfies \( P\left( {a}_{i}\right) = 1 \) for all \( i \) . Thus \( P\mathrm{n} \) has no root in \( \mathbb{K} \) , and \( \mathbb{K}\mathrm{n} \) is not algebraically closed.

EXERCICE 2. a) Si \( n \in \mathbb{N}, n \geq 2 \) , factoriser \( {P}_{n} = {\left( X + 1\right) }^{n} - {\left( X - 1\right) }^{n} \) dans \( \mathbb{C}\left\lbrack X\right\rbrack \) . b) En déduire pour tout \( p \in {\mathbb{N}}^{ * } \) la valeur de

> EXERCISE 2. a) If \( n \in \mathbb{N}, n \geq 2 \) , factor \( {P}_{n} = {\left( X + 1\right) }^{n} - {\left( X - 1\right) }^{n} \) in \( \mathbb{C}\left\lbrack X\right\rbrack \) . b) Deduce for all \( p \in {\mathbb{N}}^{ * } \) the value of

\[
{A}_{p} = \mathop{\sum }\limits_{{k = 1}}^{p}{\cot }^{2}\left( \frac{k\pi }{{2p} + 1}\right) \;\text{ et }\;{B}_{p} = \mathop{\prod }\limits_{{k = 1}}^{p}\cot \left( \frac{k\pi }{{2p} + 1}\right) .
\]

Solution. a) Il s’agit de trouver les racines de \( {P}_{n} \) . Comme 1 n’est pas racine de \( {P}_{n} \) , on peut écrire

> Solution. a) It is a matter of finding the roots of \( {P}_{n} \) . Since 1 is not a root of \( {P}_{n} \) , we can write

\[
{P}_{n}\left( z\right)  = 0 \Leftrightarrow  {\left( \frac{z + 1}{z - 1}\right) }^{n} = 1 \Leftrightarrow  \exists k,0 \leq  k \leq  n - 1,\;\frac{z - 1}{z + 1} = {e}^{{2ik\pi }/n}.
\]

Le cas \( k = 0 \) est à exclure car on ne peut pas avoir \( \frac{z - 1}{z + 1} = 1 \) . Si \( 1 \leq k \leq n - 1 \) , l’équivalence

> The case \( k = 0 \) must be excluded because we cannot have \( \frac{z - 1}{z + 1} = 1 \) . If \( 1 \leq k \leq n - 1 \) , the equivalence

\[
\frac{z + 1}{z - 1} = {e}^{{2ik\pi }/n} \Leftrightarrow  z = \frac{{e}^{{2ik\pi }/n} + 1}{{e}^{{2ik\pi }/n} - 1} = \frac{{e}^{{ik\pi }/n} + {e}^{-{ik\pi }/n}}{{e}^{{ik\pi }/n} - {e}^{-{ik\pi }/n}} =  - i\cot \left( \frac{k\pi }{n}\right) ,
\]

montre que \( z \) est une racine de \( {P}_{n} \) si et seulement s’il existe \( k \in \{ 1,\ldots , n - 1\} \) tel que \( z = \; - i\cot \left( \frac{k\pi }{n}\right) \) . Ainsi on a trouvé \( n - 1 \) racines distinctes de \( {P}_{n} \) . Le monôme de plus haut degré de \( {P}_{n} \) étant \( {2n}{X}^{n - 1},{P}_{n} \) est de degré \( n - 1 \) et

> shows that \( z \) is a root of \( {P}_{n} \) if and only if there exists \( k \in \{ 1,\ldots , n - 1\} \) such that \( z = \; - i\cot \left( \frac{k\pi }{n}\right) \) . Thus we have found \( n - 1 \) distinct roots of \( {P}_{n} \) . The leading monomial of \( {P}_{n} \) being \( {2n}{X}^{n - 1},{P}_{n} \) is of degree \( n - 1 \) and

\[
{P}_{n} = {2n}\mathop{\prod }\limits_{{k = 1}}^{{n - 1}}\left( {X + i\cot \left( \frac{k\pi }{n}\right) }\right) .
\]

b) Notons

> b) Let us denote

\[
{c}_{k} = \cot \left( \frac{k\pi }{{2p} + 1}\right) .
\]

La relation de symétrie \( {c}_{{2p} + 1 - k} = - {c}_{k} \) montre que \( {A}_{p} = \frac{1}{2}\mathop{\sum }\limits_{{k = 1}}^{{2p}}{c}_{k}^{2} \) . Les racines de \( {P}_{{2p} + 1} \) sont les \( {u}_{k} = - i{c}_{k} \) (avec \( 1 \leq k \leq {2p} \) ). Comme

> The symmetry relation \( {c}_{{2p} + 1 - k} = - {c}_{k} \) shows that \( {A}_{p} = \frac{1}{2}\mathop{\sum }\limits_{{k = 1}}^{{2p}}{c}_{k}^{2} \) . The roots of \( {P}_{{2p} + 1} \) are the \( {u}_{k} = - i{c}_{k} \) (with \( 1 \leq k \leq {2p} \) ). Since

\[
{P}_{{2p} + 1}\left( X\right)  = 2\left( {{2p} + 1}\right) {X}^{2p} + 2\left( \begin{matrix} {2p} + 1 \\  3 \end{matrix}\right) {X}^{{2p} - 2} + \cdots
\]

les relations entre coefficients et racines (voir le théorème 1 page 64) montrent que

> the relations between coefficients and roots (see theorem 1 page 64) show that

\[
{\sigma }_{1} = \mathop{\sum }\limits_{{k = 1}}^{{2p}}{u}_{k} = 0\;\text{ et }\;{\sigma }_{2} = \mathop{\sum }\limits_{{1 \leq  k < \ell  \leq  {2p}}}{u}_{k}{u}_{l} = \frac{2\left( \begin{matrix} {2p} + 1 \\  3 \end{matrix}\right) }{2\left( {{2p} + 1}\right) } = \frac{p\left( {{2p} - 1}\right) }{3}.
\]

Donc

> Therefore

\[
{A}_{p} = \frac{1}{2}\mathop{\sum }\limits_{{k = 1}}^{{2p}}{c}_{k}^{2} =  - \frac{1}{2}\mathop{\sum }\limits_{{k = 1}}^{{2p}}{u}_{k}^{2} =  - \frac{1}{2}\left( {{\sigma }_{1}^{2} - 2{\sigma }_{2}}\right)  = \frac{p\left( {{2p} - 1}\right) }{3}.
\]

- Par ailleurs, le terme constant de \( {P}_{{2p} + 1} \) est 2 et son coefficient dominant est \( 2\left( {{2p} + 1}\right) \) , donc le produit de ses racines est \( 2/\left( {2\left( {{2p} + 1}\right) }\right)  = 1/\left( {{2p} + 1}\right) \) , donc

> - Furthermore, the constant term of \( {P}_{{2p} + 1} \) is 2 and its leading coefficient is \( 2\left( {{2p} + 1}\right) \) , so the product of its roots is \( 2/\left( {2\left( {{2p} + 1}\right) }\right)  = 1/\left( {{2p} + 1}\right) \) , therefore

\[
{B}_{p} = \mathop{\prod }\limits_{{k = 1}}^{p}\cot \left( \frac{k\pi }{{2p} + 1}\right)  = {\left( {\left( -1\right) }^{p}\mathop{\prod }\limits_{{k = 1}}^{{2p}}\cot \left( \frac{k\pi }{{2p} + 1}\right) \right) }^{1/2} = {\left( \mathop{\prod }\limits_{{k = 1}}^{{2p}}{u}_{k}\right) }^{1/2} = \frac{1}{\sqrt{{2p} + 1}}.
\]

EXERCICE 3. a) Montrer que pour tout \( n \in \mathbb{N}, n \geq 2 \) , le polynôme

> EXERCISE 3. a) Show that for all \( n \in \mathbb{N}, n \geq 2 \) , the polynomial

\[
{P}_{n} = 1 + \frac{1}{1!}X + \frac{1}{2!}{X}^{2} + \cdots  + \frac{1}{n!}{X}^{n}
\]

n’a que des racines simples dans \( \mathbb{C} \) .

> has only simple roots in \( \mathbb{C} \) .

b) Montrer que pour tout \( n \geq 2 \) , le polynôme \( {P}_{n} = {X}^{n} - X + 1 \) n’a que des racines simples dans \( \mathbb{C} \) .

> b) Show that for all \( n \geq 2 \) , the polynomial \( {P}_{n} = {X}^{n} - X + 1 \) has only simple roots in \( \mathbb{C} \) .

Solution. a) Supposons que \( {P}_{n} \) ait une racine multiple \( {z}_{0} \in \mathbb{C} \) . Alors \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}^{\prime }\left( {z}_{0}\right) = 0 \) et comme \( {P}_{n}^{\prime } = {P}_{n - 1} \) , on a \( {P}_{n - 1}\left( {z}_{0}\right) = 0 \) , donc \( {z}_{0}^{n}/n! = \left( {{P}_{n} - {P}_{n - 1}}\right) \left( {z}_{0}\right) = 0 \) d’où \( {z}_{0} = 0 \) . Ceci entraîne \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}\left( 0\right) = 1 \neq 0 \) , ce qui est absurde. Le polynôme \( {P}_{n} \) n’a donc que des racines simples dans \( \mathbb{C} \) .

> Solution. a) Suppose that \( {P}_{n} \) has a multiple root \( {z}_{0} \in \mathbb{C} \) . Then \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}^{\prime }\left( {z}_{0}\right) = 0 \) and since \( {P}_{n}^{\prime } = {P}_{n - 1} \) , we have \( {P}_{n - 1}\left( {z}_{0}\right) = 0 \) , therefore \( {z}_{0}^{n}/n! = \left( {{P}_{n} - {P}_{n - 1}}\right) \left( {z}_{0}\right) = 0 \) whence \( {z}_{0} = 0 \) . This implies \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}\left( 0\right) = 1 \neq 0 \) , which is absurd. The polynomial \( {P}_{n} \) therefore has only simple roots in \( \mathbb{C} \) .

b) Supposons que \( {P}_{n} \) ait une racine multiple \( {z}_{0} \in \mathbb{C} \) . Alors \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}^{\prime }\left( {z}_{0}\right) = 0 \) , c’est-à-dire \( {z}_{0}^{n} - {z}_{0} + 1 = n{z}_{0}^{n - 1} - 1 = 0 \) . Donc \( {z}_{0}^{n} - {z}_{0} + 1 = 0 \) et \( {z}_{0}^{n} = {z}_{0}/n \) , d’où \( {z}_{0}\left( {1/n - 1}\right) + 1 = 0 \) , c’est-à-dire \( {z}_{0} = n/\left( {n - 1}\right) \) . Ceci entraîne

> b) Suppose that \( {P}_{n} \) has a multiple root \( {z}_{0} \in \mathbb{C} \) . Then \( {P}_{n}\left( {z}_{0}\right) = {P}_{n}^{\prime }\left( {z}_{0}\right) = 0 \) , that is to say \( {z}_{0}^{n} - {z}_{0} + 1 = n{z}_{0}^{n - 1} - 1 = 0 \) . Thus \( {z}_{0}^{n} - {z}_{0} + 1 = 0 \) and \( {z}_{0}^{n} = {z}_{0}/n \) , whence \( {z}_{0}\left( {1/n - 1}\right) + 1 = 0 \) , that is to say \( {z}_{0} = n/\left( {n - 1}\right) \) . This implies

\[
{P}_{n}^{\prime }\left( {z}_{0}\right)  = n{z}_{0}^{n - 1} - 1 = n{\left( \frac{n}{n - 1}\right) }^{n - 1} - 1 > n - 1 > 0,
\]

ce qui est absurde. Le polynôme \( {P}_{n} \) n’a donc que des racines simples dans \( \mathbb{C} \) .

> which is absurd. The polynomial \( {P}_{n} \) therefore only has simple roots in \( \mathbb{C} \) .

EXERCICE 4. 1/ Soit \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Montrer que \( P \) n’a que des racines simples dans \( \mathbb{C} \) .

> EXERCISE 4. 1/ Let \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) be irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Show that \( P \) only has simple roots in \( \mathbb{C} \) .

2/ (Deux applications) a) Soit \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) un polynôme ayant une racine \( \lambda \in \mathbb{C} \) d’ordre de multiplicité \( \mu > \deg \left( P\right) /2 \) . Montrer que \( \lambda \in \mathbb{Q} \) .

> 2/ (Two applications) a) Let \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) be a polynomial having a root \( \lambda \in \mathbb{C} \) of multiplicity \( \mu > \deg \left( P\right) /2 \) . Show that \( \lambda \in \mathbb{Q} \) .

b) Soit \( P \in \mathbb{Q}\left\lbrack X\right\rbrack ,\deg \left( P\right) = {2n} + 1 \) avec \( n \in {\mathbb{N}}^{ * } \) , tel que \( P \) admette une racine d’ordre \( n \) . Si \( n \geq 2 \) , montrer que \( P \) admet une racine dans \( \mathbb{Q} \) .

> b) Let \( P \in \mathbb{Q}\left\lbrack X\right\rbrack ,\deg \left( P\right) = {2n} + 1 \) with \( n \in {\mathbb{N}}^{ * } \) , such that \( P \) admits a root of order \( n \) . If \( n \geq 2 \) , show that \( P \) admits a root in \( \mathbb{Q} \) .

Solution. 1 / Il suffit de montrer d’après le théorème 3 que \( P \) et \( {P}^{\prime } \) n’ont aucune racine commune, ce qui équivaut (voir la remarque 4) à montrer que \( P \) et \( {P}^{\prime } \) sont premiers entre eux dans \( \mathbb{C}\left\lbrack X\right\rbrack \) , ce qui n'est qu'un cas particulier du résultat plus général suivant (d'ailleurs utile !).

> Solution. 1 / It suffices to show according to theorem 3 that \( P \) and \( {P}^{\prime } \) have no common root, which is equivalent (see remark 4) to showing that \( P \) and \( {P}^{\prime } \) are coprime in \( \mathbb{C}\left\lbrack X\right\rbrack \) , which is only a special case of the following more general result (which is useful, by the way!).

LEMME. Soit \( \mathbb{K} \) un corps commutatif, \( \mathbb{L} \) un surcorps commutatif de \( \mathbb{K} \) . Soient \( P \) et \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) deux polynômes premiers entre eux dans \( \mathbb{K}\left\lbrack X\right\rbrack \) . Alors \( P \) et \( Q \) sont premiers entre eux dans \( \mathbb{L}\left\lbrack X\right\rbrack \) .

> LEMMA. Let \( \mathbb{K} \) be a commutative field, \( \mathbb{L} \) a commutative extension field of \( \mathbb{K} \) . Let \( P \) and \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) be two coprime polynomials in \( \mathbb{K}\left\lbrack X\right\rbrack \) . Then \( P \) and \( Q \) are coprime in \( \mathbb{L}\left\lbrack X\right\rbrack \) .

En effet, cela provient de l’égalité de Bezout. Il existe \( U \) et \( V \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {UP} + {VQ} = 1 \) , égalité qui reste évidemment vraie dans \( \mathbb{L}\left\lbrack X\right\rbrack \) , d’où le lemme. Maintenant le polynôme \( P \) étant irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack , P \) et \( {P}^{\prime } \) sont premiers entre eux dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) (car \( \deg \left( {P}^{\prime }\right) < \deg \left( P\right) \) ) donc dans \( \mathbb{C}\left\lbrack X\right\rbrack \) d’après le lemme précédent.

> Indeed, this follows from Bézout's identity. There exist \( U \) and \( V \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {UP} + {VQ} = 1 \), an equality that obviously remains true in \( \mathbb{L}\left\lbrack X\right\rbrack \), hence the lemma. Now, since the polynomial \( P \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack , P \) and \( {P}^{\prime } \) are coprime in \( \mathbb{Q}\left\lbrack X\right\rbrack \) (because \( \deg \left( {P}^{\prime }\right) < \deg \left( P\right) \)), they are therefore in \( \mathbb{C}\left\lbrack X\right\rbrack \) according to the previous lemma.

2/a) Soit \( P = \alpha {P}_{1}\cdots {P}_{k} \) la décomposition de \( P \) en facteurs irréductibles de \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Parmi \( {P}_{1},\ldots ,{P}_{k} \) , il y a \( r \) polynômes dont \( \lambda \) soit racine, par exemple \( {P}_{1},\ldots ,{P}_{r} \) . Si \( \lambda \notin \mathbb{Q} \) , comme

> 2/a) Let \( P = \alpha {P}_{1}\cdots {P}_{k} \) be the decomposition of \( P \) into irreducible factors of \( \mathbb{Q}\left\lbrack X\right\rbrack \). Among \( {P}_{1},\ldots ,{P}_{k} \), there are \( r \) polynomials for which \( \lambda \) is a root, for example \( {P}_{1},\ldots ,{P}_{r} \). If \( \lambda \notin \mathbb{Q} \), as

\( {P}_{1},\cdots ,{P}_{r} \) sont à coefficients rationnels, on a \( \deg \left( {P}_{i}\right) \geq 2 \) pour \( 1 \leq i \leq r \) . Or d’après \( 1/ \) , les \( {P}_{i} \) étant irréductibles, \( \lambda \) est racine simple de \( {P}_{i} \) pour \( 1 \leq i \leq r \) . Donc \( \mu = r \) . Donc

> \( {P}_{1},\cdots ,{P}_{r} \) have rational coefficients, we have \( \deg \left( {P}_{i}\right) \geq 2 \) for \( 1 \leq i \leq r \). However, according to \( 1/ \), since the \( {P}_{i} \) are irreducible, \( \lambda \) is a simple root of \( {P}_{i} \) for \( 1 \leq i \leq r \). Thus \( \mu = r \). Therefore

\[
\deg \left( P\right)  = \mathop{\sum }\limits_{{i = 1}}^{k}\deg \left( {P}_{i}\right)  \geq  \mathop{\sum }\limits_{{i = 1}}^{r}\deg \left( {P}_{i}\right)  \geq  {2r} = {2\mu },
\]

ce qui est contraire aux hypothèses car \( \mu > \deg \left( P\right) /2 \) . On a donc forcément \( \lambda \in \mathbb{Q} \) .

> which contradicts the hypotheses because \( \mu > \deg \left( P\right) /2 \). We must therefore have \( \lambda \in \mathbb{Q} \).

b) Par hypothèse, il existe une racine \( \lambda \in \mathbb{C} \) d’ordre \( n \) de \( P \) . Supposons que \( P \) n’ait aucune racine dans \( \mathbb{Q} \) . Alors dans la factorisation de \( P \) en facteurs irréductibles de \( \mathbb{Q}\left\lbrack X\right\rbrack , P = \alpha {P}_{1}\cdots {P}_{k} \) , on a \( \deg \left( {P}_{i}\right) \geq 2 \) pour tout \( i \) .

> b) By hypothesis, there exists a root \( \lambda \in \mathbb{C} \) of order \( n \) of \( P \). Suppose that \( P \) has no root in \( \mathbb{Q} \). Then in the factorization of \( P \) into irreducible factors of \( \mathbb{Q}\left\lbrack X\right\rbrack , P = \alpha {P}_{1}\cdots {P}_{k} \), we have \( \deg \left( {P}_{i}\right) \geq 2 \) for all \( i \).

Parmi \( {P}_{1},\ldots ,{P}_{k} \) , il y a \( r \) polynômes dont \( \lambda \) soit racine, par exemple \( {P}_{1},\ldots ,{P}_{r} \) . D’après \( 1/ \) , les \( {P}_{i} \) étant irréductibles, \( \lambda \) est racine simple de \( {P}_{i} \) pour \( 1 \leq i \leq r \) . Donc \( r = n \) (et donc \( k \geq r = n) \) .

> Among \( {P}_{1},\ldots ,{P}_{k} \), there are \( r \) polynomials for which \( \lambda \) is a root, for example \( {P}_{1},\ldots ,{P}_{r} \). According to \( 1/ \), since the \( {P}_{i} \) are irreducible, \( \lambda \) is a simple root of \( {P}_{i} \) for \( 1 \leq i \leq r \). Thus \( r = n \) (and therefore \( k \geq r = n) \).

- On a \( k = n \) . En effet. Si \( k > n \) , alors

> - We have \( k = n \). Indeed. If \( k > n \), then

\[
\deg P = \mathop{\sum }\limits_{{i = 1}}^{k}\deg \left( {P}_{i}\right)  \geq  {2k} \geq  {2n} + 2,
\]

ce qui est incompatible avec l’hypothèse deg \( P \leq {2n} + 1 \) .

> which is incompatible with the hypothesis deg \( P \leq {2n} + 1 \).

- Donc \( P = \alpha {P}_{1}\cdots {P}_{n} \) . Le degré de \( P \) étant impair, il existe un polynôme \( {P}_{i} \) de degré impair, par exemple \( \deg \left( {P}_{1}\right) \) impair. Comme de plus \( \deg \left( {P}_{1}\right)  \geq  2 \) , on a \( \deg \left( {P}_{1}\right)  \geq  3 \) .

> - Thus \( P = \alpha {P}_{1}\cdots {P}_{n} \) . Since the degree of \( P \) is odd, there exists a polynomial \( {P}_{i} \) of odd degree, for example \( \deg \left( {P}_{1}\right) \) odd. Furthermore, as \( \deg \left( {P}_{1}\right)  \geq  2 \) , we have \( \deg \left( {P}_{1}\right)  \geq  3 \) .

- Il existe un polynôme \( {P}_{i} \) de degré 2 (sinon pour tout \( i,\deg \left( {P}_{i}\right)  \geq  3 \) donc \( {2n} + 1 = \deg \left( P\right)  = \; \mathop{\sum }\limits_{{i = 1}}^{n}\deg \left( {P}_{i}\right)  \geq  {3n} \) , absurde car \( n \geq  2 \) ), par exemple \( \deg \left( {P}_{2}\right)  = 2 \) . Effectuons la division eu-clidienne de \( {P}_{1} \) par \( {P}_{2} : {P}_{1} = Q{P}_{2} + R \) , avec \( R \in  \mathbb{Q}\left\lbrack  X\right\rbrack \) et \( \deg \left( R\right)  < \deg \left( {P}_{2}\right)  = 2 \) . On a \( R \neq  0 \) car \( {P}_{1} \) est irréductible et \( \deg \left( {P}_{1}\right)  > \deg \left( {P}_{2}\right) \) . Or \( \lambda \) est racine de \( R \) (car \( {P}_{1}\left( \lambda \right)  = 0 = \; Q\left( \lambda \right) {P}_{2}\left( \lambda \right)  + R\left( \lambda \right)  = R\left( \lambda \right) ) \) , donc comme \( R \neq  0 \) et \( \deg \left( R\right)  \leq  1 \) , on en déduit \( \lambda  \in  \mathbb{Q} \) , ce qui est contradictoire. Le polynôme \( P \) admet donc au moins une racine rationnelle.

> - There exists a polynomial \( {P}_{i} \) of degree 2 (otherwise for all \( i,\deg \left( {P}_{i}\right)  \geq  3 \) thus \( {2n} + 1 = \deg \left( P\right)  = \; \mathop{\sum }\limits_{{i = 1}}^{n}\deg \left( {P}_{i}\right)  \geq  {3n} \) , which is absurd as \( n \geq  2 \) ), for example \( \deg \left( {P}_{2}\right)  = 2 \) . Let us perform the Euclidean division of \( {P}_{1} \) by \( {P}_{2} : {P}_{1} = Q{P}_{2} + R \) , with \( R \in  \mathbb{Q}\left\lbrack  X\right\rbrack \) and \( \deg \left( R\right)  < \deg \left( {P}_{2}\right)  = 2 \) . We have \( R \neq  0 \) because \( {P}_{1} \) is irreducible and \( \deg \left( {P}_{1}\right)  > \deg \left( {P}_{2}\right) \) . However, \( \lambda \) is a root of \( R \) (since \( {P}_{1}\left( \lambda \right)  = 0 = \; Q\left( \lambda \right) {P}_{2}\left( \lambda \right)  + R\left( \lambda \right)  = R\left( \lambda \right) ) \) , so as \( R \neq  0 \) and \( \deg \left( R\right)  \leq  1 \) , we deduce \( \lambda  \in  \mathbb{Q} \) , which is contradictory. The polynomial \( P \) therefore admits at least one rational root.

Remarque. Si \( n = 1 \) , le résultat \( 2/\mathrm{b} \) ) est faux (prendre par exemple \( P = {X}^{3} - 2 \) ).

> Remark. If \( n = 1 \) , the result \( 2/\mathrm{b} \) ) is false (take for example \( P = {X}^{3} - 2 \) ).

EXERCICE 5. Déterminer les polynômes \( P \) non constants de \( \mathbb{C}\left\lbrack X\right\rbrack \) vérifiant

> EXERCISE 5. Determine the non-constant polynomials \( P \) of \( \mathbb{C}\left\lbrack X\right\rbrack \) satisfying

\[
P\left( {X}^{2}\right)  = P\left( X\right) P\left( {X + 1}\right) .
\]

(*)

> Solution. Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) vérifiant (*) avec \( \deg \left( P\right) \geq 1 \) . Soit \( \alpha \) une racine de \( P \) .

Solution. Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) satisfy (*) with \( \deg \left( P\right) \geq 1 \) . Let \( \alpha \) be a root of \( P \) .

> Comme \( P\left( {\alpha }^{2}\right) = P\left( \alpha \right) P\left( {\alpha + 1}\right) = 0,{\alpha }^{2} \) est une racine de \( P \) . En itérant le procédé, on voit que \( {\alpha }^{2},{\alpha }^{4},\ldots ,{\alpha }^{{2}^{n}},\ldots \) sont des racines de \( P \) . Le polynôme \( P \) n’ayant qu’un nombre fini de racines, on doit avoir

Since \( P\left( {\alpha }^{2}\right) = P\left( \alpha \right) P\left( {\alpha + 1}\right) = 0,{\alpha }^{2} \) is a root of \( P \) . By iterating the process, we see that \( {\alpha }^{2},{\alpha }^{4},\ldots ,{\alpha }^{{2}^{n}},\ldots \) are roots of \( P \) . As the polynomial \( P \) has only a finite number of roots, we must have

\[
\alpha  = 0\;\text{ ou }\;\left| \alpha \right|  = 1.
\]

\( \left( {* * }\right) \)

> D’après \( \left( *\right) , P\left\lbrack {\left( \alpha - 1\right) }^{2}\right\rbrack = P\left( {\alpha - 1}\right) P\left( \alpha \right) = 0 \) , donc \( {\left( \alpha - 1\right) }^{2} \) est une racine de \( P \) . D’après \( \left( {* * }\right) \) , on doit avoir \( \left| {\left( \alpha - 1\right) }^{2}\right| = 0 \) ou \( \left| {\left( \alpha - 1\right) }^{2}\right| = 1 \) , c’est-à-dire

According to \( \left( *\right) , P\left\lbrack {\left( \alpha - 1\right) }^{2}\right\rbrack = P\left( {\alpha - 1}\right) P\left( \alpha \right) = 0 \) , therefore \( {\left( \alpha - 1\right) }^{2} \) is a root of \( P \) . According to \( \left( {* * }\right) \) , we must have \( \left| {\left( \alpha - 1\right) }^{2}\right| = 0 \) or \( \left| {\left( \alpha - 1\right) }^{2}\right| = 1 \) , that is to say

\[
\alpha  = 1\text{ ou }\left| {\alpha  - 1}\right|  = 1.
\]

\( \left( {* * * }\right) \)

> D’après \( \left( {* * }\right) \) et \( \left( {* * * }\right) \) , on a soit (i) \( \alpha = 0 \) , soit (ii) \( \alpha = 1 \) , soit (iii) \( \left| {\alpha - 1}\right| = \left| \alpha \right| = 1 \) . On vérifie facilement que la condition (iii) s’écrit aussi \( \alpha = 1 + j \) ou \( \alpha = 1 + {j}^{2} \) où \( j = \exp \left( {{2i\pi }/3}\right) \) . Or \( {\left( \alpha - 1\right) }^{2} \) est une racine de \( P \) donc d’après \( \left( {* * }\right) ,\left| {{\left( \alpha - 1\right) }^{2} - 1}\right| \in \{ 0,1\} \) , et comme \( \left| {{j}^{2} - 1}\right| > 1 \) et \( \left| {{\left( {j}^{2}\right) }^{2} - 1}\right| = \left| {j - 1}\right| > 1 \) , on voit que les solutions (iii) ne conviennent pas.

According to \( \left( {* * }\right) \) and \( \left( {* * * }\right) \) , we have either (i) \( \alpha = 0 \) , or (ii) \( \alpha = 1 \) , or (iii) \( \left| {\alpha - 1}\right| = \left| \alpha \right| = 1 \) . We easily verify that condition (iii) can also be written as \( \alpha = 1 + j \) or \( \alpha = 1 + {j}^{2} \) where \( j = \exp \left( {{2i\pi }/3}\right) \) . However, \( {\left( \alpha - 1\right) }^{2} \) is a root of \( P \) so according to \( \left( {* * }\right) ,\left| {{\left( \alpha - 1\right) }^{2} - 1}\right| \in \{ 0,1\} \) , and since \( \left| {{j}^{2} - 1}\right| > 1 \) and \( \left| {{\left( {j}^{2}\right) }^{2} - 1}\right| = \left| {j - 1}\right| > 1 \) , we see that solutions (iii) are not suitable.

> Nécessairement, on a donc \( \alpha \in \{ 0,1\} \) . Ainsi, le polynôme \( P \) est de la forme \( P = \lambda {X}^{p}{\left( X - 1\right) }^{q} \) , \( \lambda \in {\mathbb{C}}^{ * } \) . Comme \( P \) vérifie \( \left( *\right) \) , on a

Necessarily, we therefore have \( \alpha \in \{ 0,1\} \) . Thus, the polynomial \( P \) is of the form \( P = \lambda {X}^{p}{\left( X - 1\right) }^{q} \) , \( \lambda \in {\mathbb{C}}^{ * } \) . Since \( P \) satisfies \( \left( *\right) \) , we have

\[
\lambda {X}^{2p}{\left( {X}^{2} - 1\right) }^{q} = {\lambda }^{2}{X}^{p}{\left( X - 1\right) }^{q}{\left( X + 1\right) }^{p}{X}^{q},
\]

d’où on déduit \( p = q \) et \( \lambda = 1 \) .

> from which we deduce \( p = q \) and \( \lambda = 1 \) .

Réciproquement, si \( P \) est de la forme \( {X}^{p}{\left( X - 1\right) }^{p} \) , on vérifie facilement que \( P \) vérifie \( \left( *\right) \) . Les solutions sont donc les polynômes de la forme \( {X}^{p}{\left( X - 1\right) }^{p}, p \in {\mathbb{N}}^{ * } \) .

> Conversely, if \( P \) is of the form \( {X}^{p}{\left( X - 1\right) }^{p} \) , it is easy to verify that \( P \) satisfies \( \left( *\right) \) . The solutions are therefore the polynomials of the form \( {X}^{p}{\left( X - 1\right) }^{p}, p \in {\mathbb{N}}^{ * } \) .

\( \rightarrow \) EXERCICE 6. a) Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 2 \) . Montrer que les racines de \( {P}^{\prime } \) appartiennent à l’enveloppe convexe des racines de \( P \) .

> \( \rightarrow \) EXERCISE 6. a) Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 2 \) . Show that the roots of \( {P}^{\prime } \) belong to the convex hull of the roots of \( P \) .

b) Que dire sur les racines de \( {P}^{\prime } \) si \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) a toutes ses racines réelles ?

> b) What can be said about the roots of \( {P}^{\prime } \) if \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) has all its roots real?

Solution. a) Soient \( {a}_{1},\ldots ,{a}_{n} \) les racines de \( P \) , comptées avec leur ordre de multiplicité, de sorte que si \( \beta \) désigne le coefficient dominant de \( P, P = \beta \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) . On a facilement

> Solution. a) Let \( {a}_{1},\ldots ,{a}_{n} \) be the roots of \( P \) , counted with their multiplicity, such that if \( \beta \) denotes the leading coefficient of \( P, P = \beta \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) \) . We easily have

\[
\frac{{P}^{\prime }\left( X\right) }{P\left( X\right) } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{X - {a}_{i}}.
\]

Soit \( a \) une racine de \( {P}^{\prime } \) . Si \( a \) est une racine de \( P \) , le résultat est évident. Sinon

> Let \( a \) be a root of \( {P}^{\prime } \) . If \( a \) is a root of \( P \) , the result is obvious. Otherwise

\[
0 = \frac{{P}^{\prime }\left( a\right) }{P\left( a\right) } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{a - {a}_{i}} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\bar{a} - \overline{{a}_{i}}}{{\left| a - {a}_{i}\right| }^{2}},
\]

et en passant au conjugué

> and by taking the conjugate

\[
\mathop{\sum }\limits_{{i = 1}}^{n}\frac{a - {a}_{i}}{{\left| a - {a}_{i}\right| }^{2}} = 0\;\text{ donc }\;\left( {\mathop{\sum }\limits_{{i = 1}}^{n}\frac{1}{{\left| a - {a}_{i}\right| }^{2}}}\right) a = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{a}_{i}}{{\left| a - {a}_{i}\right| }^{2}},
\]

d'où le résultat.

> hence the result.

b) D’après a), les racines de \( {P}^{\prime } \) sont réelles. On a même plus de renseignements sur leur localisation. Soient \( {a}_{1},\ldots ,{a}_{p} \) les racines de \( P \) avec \( {a}_{1} < \cdots < {a}_{p} \) , d’ordre de multiplicité \( {\alpha }_{1},\cdots ,{\alpha }_{p} \) , de sorte que si \( \beta \) est le coefficient dominant de \( P, P = \beta {\left( X - {a}_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {a}_{p}\right) }^{{\alpha }_{p}} \) . D’après le théorème de Rolle, pour tout \( i \in \{ 1,\ldots p - 1\} \) , il existe \( {b}_{i} \in \rbrack {a}_{i},{a}_{i + 1}\left\lbrack \right. \) tel que \( {P}^{\prime }\left( {b}_{i}\right) = 0 \) . On a ainsi trouvé \( p - 1 \) racines de \( {P}^{\prime } \) .

> b) According to a), the roots of \( {P}^{\prime } \) are real. We even have more information on their location. Let \( {a}_{1},\ldots ,{a}_{p} \) be the roots of \( P \) with \( {a}_{1} < \cdots < {a}_{p} \) , of multiplicity \( {\alpha }_{1},\cdots ,{\alpha }_{p} \) , such that if \( \beta \) is the leading coefficient of \( P, P = \beta {\left( X - {a}_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {a}_{p}\right) }^{{\alpha }_{p}} \) . According to Rolle's theorem, for all \( i \in \{ 1,\ldots p - 1\} \) , there exists \( {b}_{i} \in \rbrack {a}_{i},{a}_{i + 1}\left\lbrack \right. \) such that \( {P}^{\prime }\left( {b}_{i}\right) = 0 \) . We have thus found \( p - 1 \) roots of \( {P}^{\prime } \) .

- Pour tout \( i \) tel que \( {\alpha }_{i} \geq  2,{a}_{i} \) est racine de \( {P}^{\prime } \) d’ordre de multiplicité \( {\alpha }_{i} - 1 \) (voir le théorème 3). Comptées avec leur ordre de multiplicité, on a ainsi localisé \( \left( {p - 1}\right)  + \mathop{\sum }\limits_{{i = 1}}^{p}\left( {{\alpha }_{i} - 1}\right)  = \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right)  - 1 = \; \deg \left( P\right)  - 1 = \deg \left( {P}^{\prime }\right) \) racines. On a donc localisé toutes les racines de \( {P}^{\prime } \) : ce sont les \( {b}_{i} \in  \rbrack {a}_{i},{a}_{i + 1}\lbrack \) et les \( {a}_{i} \) tels que \( {\alpha }_{i} \geq  2 \) .

> - For any \( i \) such that \( {\alpha }_{i} \geq  2,{a}_{i} \) is a root of \( {P}^{\prime } \) with multiplicity \( {\alpha }_{i} - 1 \) (see theorem 3). Counting with their multiplicity, we have thus located \( \left( {p - 1}\right)  + \mathop{\sum }\limits_{{i = 1}}^{p}\left( {{\alpha }_{i} - 1}\right)  = \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right)  - 1 = \; \deg \left( P\right)  - 1 = \deg \left( {P}^{\prime }\right) \) roots. We have therefore located all the roots of \( {P}^{\prime } \): they are the \( {b}_{i} \in  \rbrack {a}_{i},{a}_{i + 1}\lbrack \) and the \( {a}_{i} \) such that \( {\alpha }_{i} \geq  2 \) .

\( \rightarrow \) EXERCICE 7 (INTERPOLATION DE HERMITE). Soit \( p \in {\mathbb{N}}^{ * }, p \) entiers naturels non nuls \( {n}_{1},\ldots ,{n}_{p} \) et \( n = \mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i} \) .

> \( \rightarrow \) EXERCISE 7 (HERMITE INTERPOLATION). Let \( p \in {\mathbb{N}}^{ * }, p \) be non-zero natural integers \( {n}_{1},\ldots ,{n}_{p} \) and \( n = \mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i} \) .

a) Soit \( \mathbb{K} \) un corps commutatif de caractéristique nulle, et \( {x}_{1},\ldots ,{x}_{p} \in \mathbb{K} \) , deux à deux distincts. Soient des points \( {y}_{i, k} \) de \( \mathbb{K} \) , définis pour \( 1 \leq i \leq p \) et \( 0 \leq k < {n}_{i} \) . Montrer qu’il existe un unique polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( \deg \left( P\right) < n \) et tel que

> a) Let \( \mathbb{K} \) be a commutative field of characteristic zero, and \( {x}_{1},\ldots ,{x}_{p} \in \mathbb{K} \) , pairwise distinct. Let \( {y}_{i, k} \) be points of \( \mathbb{K} \) , defined for \( 1 \leq i \leq p \) and \( 0 \leq k < {n}_{i} \) . Show that there exists a unique polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( \deg \left( P\right) < n \) and such that

\[
\forall \left( {i, k}\right)  \in  {\mathbb{N}}^{ * } \times  \mathbb{N},1 \leq  i \leq  p,0 \leq  k < {n}_{i},\;{P}^{\left( k\right) }\left( {x}_{i}\right)  = {y}_{i, k}.
\]

b) Soit \( I \) un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{n} \) . On considère \( p \) points \( {x}_{1} < \ldots < {x}_{p} \) de \( I \) . Si \( P \) est le polynôme d’interpolation de Hermite de degré \( < n \) vérifiant \( {P}^{\left( k\right) }\left( {x}_{i}\right) = {f}^{\left( k\right) }\left( {x}_{i}\right) \) pour \( 1 \leq i \leq p \) et \( 0 \leq k < {n}_{i} \) , montrer que

> b) Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a function of class \( {\mathcal{C}}^{n} \) . Consider \( p \) points \( {x}_{1} < \ldots < {x}_{p} \) of \( I \) . If \( P \) is the Hermite interpolation polynomial of degree \( < n \) satisfying \( {P}^{\left( k\right) }\left( {x}_{i}\right) = {f}^{\left( k\right) }\left( {x}_{i}\right) \) for \( 1 \leq i \leq p \) and \( 0 \leq k < {n}_{i} \) , show that

\[
\forall x \in  I,\exists \xi  \in  I,\;f\left( x\right)  - P\left( x\right)  = \frac{{f}^{\left( n\right) }\left( \xi \right) }{n!}\mathop{\prod }\limits_{{i = 1}}^{p}{\left( x - {x}_{i}\right) }^{{n}_{i}}.
\]

(*)

> Solution. a) Notons \( {\mathcal{P}}_{n} \) le s.e.v des polynômes de \( \mathbb{K}\left\lbrack X\right\rbrack \) de degré \( < n \) , et considérons l’application linéaire

Solution. a) Let \( {\mathcal{P}}_{n} \) be the vector subspace of polynomials of \( \mathbb{K}\left\lbrack X\right\rbrack \) of degree \( < n \) , and consider the linear map

\[
\varphi  : {\mathcal{P}}_{n} \rightarrow  {\mathbb{K}}^{n}\;P \mapsto  \left( {P\left( {x}_{1}\right) ,\ldots ,{P}^{\left( {n}_{1} - 1\right) }\left( {x}_{1}\right) ;\ldots ;P\left( {x}_{p}\right) ,\ldots ,{P}^{\left( {n}_{p} - 1\right) }\left( {x}_{p}\right) }\right) .
\]

Il s’agit de montrer que \( \varphi \) est bijective. Calculons son noyau Ker \( \varphi \) . Supposons \( \varphi \left( P\right) = 0 \) avec \( P \in {\mathcal{P}}_{n} \) . Pour \( i = 1,\ldots , p \) , on a \( {P}^{\left( k\right) }\left( {x}_{i}\right) = 0 \) pour \( 0 \leq k < {n}_{i} \) , donc \( {x}_{i} \) est une racine d’ordre

> It is a matter of showing that \( \varphi \) is bijective. Let us calculate its kernel Ker \( \varphi \) . Suppose \( \varphi \left( P\right) = 0 \) with \( P \in {\mathcal{P}}_{n} \) . For \( i = 1,\ldots , p \) , we have \( {P}^{\left( k\right) }\left( {x}_{i}\right) = 0 \) for \( 0 \leq k < {n}_{i} \) , so \( {x}_{i} \) is a root of order

\( {h}_{i} \geq {n}_{i} \) d’après le théorème 3 page 64 . Ceci étant vrai pour tout \( i \) , on peut donc écrire \( P \) sous la forme

> \( {h}_{i} \geq {n}_{i} \) according to theorem 3 page 64 . Since this is true for all \( i \) , we can therefore write \( P \) in the form

\[
P = Q\mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {x}_{i}\right) }^{{h}_{i}}\;\text{ avec }\;Q \in  \mathbb{K}\left\lbrack  X\right\rbrack  .
\]

Si \( Q \neq 0 \) , on a deg \( P \geq \mathop{\sum }\limits_{{i = 1}}^{p}{h}_{i} \geq \mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i} = n \) , ce qui est impossible puisque \( P \in {\mathcal{P}}_{n} \) . Donc \( Q = 0 \) , ce qui entraîne Ker \( \varphi = \{ 0\} \) . Donc \( \varphi \) est injective. Comme l’e.v d’arrivée \( {\mathbb{K}}^{n} \) de l’application linéaire \( \varphi \) a même dimension que son e.v de départ \( {\mathcal{P}}_{n} \) , on en déduit d’après le théorème du rang que \( \varphi \) est bijective.

> If \( Q \neq 0 \) , we have deg \( P \geq \mathop{\sum }\limits_{{i = 1}}^{p}{h}_{i} \geq \mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i} = n \) , which is impossible since \( P \in {\mathcal{P}}_{n} \) . Thus \( Q = 0 \) , which implies Ker \( \varphi = \{ 0\} \) . Therefore \( \varphi \) is injective. Since the target vector space \( {\mathbb{K}}^{n} \) of the linear map \( \varphi \) has the same dimension as its source vector space \( {\mathcal{P}}_{n} \) , we deduce from the rank-nullity theorem that \( \varphi \) is bijective.

b) Soit \( x \in I \) . S’il existe \( i \) tel que \( x = {x}_{i} \) le résultat (*) est immédiat puisque \( f\left( {x}_{i}\right) = P\left( {x}_{i}\right) \) . Dans le cas contraire, on considère \( A \in \mathbb{R} \) tel que

> b) Let \( x \in I \) . If there exists \( i \) such that \( x = {x}_{i} \) the result (*) is immediate since \( f\left( {x}_{i}\right) = P\left( {x}_{i}\right) \) . Otherwise, we consider \( A \in \mathbb{R} \) such that

\[
{\varphi }_{x} : I \rightarrow  \mathbb{R}\;t \mapsto  f\left( t\right)  - P\left( t\right)  - A\mathop{\prod }\limits_{{i = 1}}^{p}{\left( t - {x}_{i}\right) }^{{n}_{i}}
\]

vérifie \( {\varphi }_{x}\left( x\right) = 0 \) . La fonction \( {\varphi }_{x} \) est de classe \( {\mathcal{C}}^{n} \) . En comptant avec les ordres de multiplicité, (l’ordre de multiplicité \( k \) d’un zéro \( \alpha \) d’une fonction \( g \) de classe \( {\mathcal{C}}^{n} \) est le plus grand entier \( k \leq n \) tel que \( g\left( \alpha \right) = \ldots = {g}^{\left( k - 1\right) }\left( \alpha \right) = 0){\varphi }_{x} \) a au moins \( n + 1 \) zéros car \( {\varphi }_{x}\left( x\right) = 0 \) par construction, et \( {\varphi }_{x}^{\left( k\right) }\left( {x}_{i}\right) = 0 \) pour \( 1 \leq i \leq p \) et \( 0 \leq k < {n}_{i} \) . On remarque maintenant que pour toute fonction \( g : I \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{m} \) , qui a au moins \( m + 1 \) zéros sur \( I \) , la fonction \( {g}^{\prime } \) a au moins \( m \) zéros sur \( I \) (la preuve est immédiate en remarquant qu’un zéro de \( g \) d’ordre \( k \geq 2 \) , est un zéro de \( {g}^{\prime } \) d’ordre \( k - 1 \) , et qu’entre deux zéros de \( g \) il y a au moins un zéro de \( {g}^{\prime } \) d’après le théorème de Rolle). Ainsi \( {\varphi }_{x}^{\prime } \) a au moins \( n \) zéros sur \( I,{\varphi }_{x}^{\prime \prime } \) au moins \( n - 1 \) zéros, \( \ldots ,{\varphi }_{x}^{\left( n\right) } \) a au moins 1 zéro sur \( I \) . Donc il existe \( \xi \in I \) tel que \( {\varphi }_{x}^{\left( n\right) }\left( \xi \right) = 0 \) , ce qui s’écrit aussi \( {f}^{\left( n\right) }\left( \xi \right) - n!A = 0 \) , d’où le résultat.

> satisfies \( {\varphi }_{x}\left( x\right) = 0 \) . The function \( {\varphi }_{x} \) is of class \( {\mathcal{C}}^{n} \) . Counting with multiplicities, (the multiplicity \( k \) of a zero \( \alpha \) of a function \( g \) of class \( {\mathcal{C}}^{n} \) is the largest integer \( k \leq n \) such that \( g\left( \alpha \right) = \ldots = {g}^{\left( k - 1\right) }\left( \alpha \right) = 0){\varphi }_{x} \) has at least \( n + 1 \) zeros because \( {\varphi }_{x}\left( x\right) = 0 \) by construction, and \( {\varphi }_{x}^{\left( k\right) }\left( {x}_{i}\right) = 0 \) for \( 1 \leq i \leq p \) and \( 0 \leq k < {n}_{i} \) . We now note that for any function \( g : I \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{m} \) , which has at least \( m + 1 \) zeros on \( I \) , the function \( {g}^{\prime } \) has at least \( m \) zeros on \( I \) (the proof is immediate by noting that a zero of \( g \) of order \( k \geq 2 \) , is a zero of \( {g}^{\prime } \) of order \( k - 1 \) , and that between two zeros of \( g \) there is at least one zero of \( {g}^{\prime } \) according to Rolle's theorem). Thus \( {\varphi }_{x}^{\prime } \) has at least \( n \) zeros on \( I,{\varphi }_{x}^{\prime \prime } \) at least \( n - 1 \) zeros, \( \ldots ,{\varphi }_{x}^{\left( n\right) } \) has at least 1 zero on \( I \) . Therefore there exists \( \xi \in I \) such that \( {\varphi }_{x}^{\left( n\right) }\left( \xi \right) = 0 \) , which is also written \( {f}^{\left( n\right) }\left( \xi \right) - n!A = 0 \) , hence the result.

EXERCICE 8. Donner la forme des polynômes \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) scindés sur \( \mathbb{R} \) , de degré \( n \geq 2 \) ,à racines toutes distinctes \( {a}_{1} < {a}_{2} < \cdots < {a}_{n} \) , tels que

> EXERCISE 8. Give the form of polynomials \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) split over \( \mathbb{R} \) , of degree \( n \geq 2 \) , with all distinct roots \( {a}_{1} < {a}_{2} < \cdots < {a}_{n} \) , such that

\[
\forall i,1 \leq  i \leq  n - 1,\;{P}^{\prime }\left( \frac{{a}_{i} + {a}_{i + 1}}{2}\right)  = 0.
\]

(*)

> Solution. Nous allons montrer que les polynômes vérifiant la condition sont ceux de degré 2. Si \( P = \alpha \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) \) est de degré 2 (avec \( {a}_{1} < {a}_{2} \) et \( \alpha \in \mathbb{R} \) ), on a \( {P}^{\prime } = \alpha \left( {{2X} - {a}_{1} - {a}_{2}}\right) \) donc \( P \) vérifie la condition \( \left( *\right) \) .

Solution. We will show that the polynomials satisfying the condition are those of degree 2. If \( P = \alpha \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) \) is of degree 2 (with \( {a}_{1} < {a}_{2} \) and \( \alpha \in \mathbb{R} \) ), we have \( {P}^{\prime } = \alpha \left( {{2X} - {a}_{1} - {a}_{2}}\right) \) so \( P \) satisfies the condition \( \left( *\right) \) .

> Si maintenant \( P = \alpha \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {a}_{i}}\right) \) est de degré \( n \geq 3\left( {{a}_{1} < \cdots < {a}_{n},\alpha \neq 0}\right) \) , on écrit \( P = \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) Q \) avec \( Q = \alpha \mathop{\prod }\limits_{{i = 3}}^{n}\left( {X - {a}_{i}}\right) \) . Par dérivation, on obtient

If now \( P = \alpha \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {a}_{i}}\right) \) is of degree \( n \geq 3\left( {{a}_{1} < \cdots < {a}_{n},\alpha \neq 0}\right) \) , we write \( P = \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) Q \) with \( Q = \alpha \mathop{\prod }\limits_{{i = 3}}^{n}\left( {X - {a}_{i}}\right) \) . By differentiation, we obtain

\[
{P}^{\prime }\left( X\right)  = \left( {{2X} - {a}_{1} - {a}_{2}}\right) Q\left( X\right)  + \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) {Q}^{\prime }\left( X\right) .
\]

Si \( P \) vérifie (*), on a donc \( {Q}^{\prime }\left( \frac{{a}_{1} + {a}_{2}}{2}\right) = 0 \) , ce qui est impossible car

> If \( P \) satisfies (*), we then have \( {Q}^{\prime }\left( \frac{{a}_{1} + {a}_{2}}{2}\right) = 0 \) , which is impossible because

- Si \( \deg \left( Q\right)  = 1,{Q}^{\prime } \) est une constante non nulle.

> - If \( \deg \left( Q\right)  = 1,{Q}^{\prime } \) is a non-zero constant.

- Si \( \deg \left( Q\right)  \geq  2,{Q}^{\prime } \) s’annule au moins une fois sur chaque intervalle \( \rbrack {a}_{i},{a}_{i + 1}\lbrack \left( {2 \leq  i \leq  n - 1}\right) \) d’après le théorème de Rolle, donc \( {Q}^{\prime } \) a au moins \( n - 3 \) racines distinctes dans l’intervalle \( \left\rbrack  {{a}_{2},{a}_{n}\left\lbrack  \right. }\right. \) . Comme \( \deg \left( {Q}^{\prime }\right)  = n - 3 \) , on en déduit que toutes les racines de \( {Q}^{\prime } \) sont dans \( \rbrack {a}_{2},{a}_{n}\left\lbrack  {\text{ et comme }\frac{{a}_{1} + {a}_{2}}{2} \notin  }\right\rbrack  {a}_{2},{a}_{n}\lbrack \) , on aboutit à une contradiction.

> - If \( \deg \left( Q\right)  \geq  2,{Q}^{\prime } \) vanishes at least once on each interval \( \rbrack {a}_{i},{a}_{i + 1}\lbrack \left( {2 \leq  i \leq  n - 1}\right) \) according to Rolle's theorem, so \( {Q}^{\prime } \) has at least \( n - 3 \) distinct roots in the interval \( \left\rbrack  {{a}_{2},{a}_{n}\left\lbrack  \right. }\right. \) . Since \( \deg \left( {Q}^{\prime }\right)  = n - 3 \) , we deduce that all the roots of \( {Q}^{\prime } \) are in \( \rbrack {a}_{2},{a}_{n}\left\lbrack  {\text{ et comme }\frac{{a}_{1} + {a}_{2}}{2} \notin  }\right\rbrack  {a}_{2},{a}_{n}\lbrack \) , we reach a contradiction.

EXERCICE 9 (PRINCIPE DU MAXIMUM). Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) un polynôme non constant. Soit \( r > 0 \) . Montrer

> EXERCISE 9 (MAXIMUM PRINCIPLE). Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) be a non-constant polynomial. Let \( r > 0 \) . Show

\[
\forall {z}_{0} \in  \mathbb{C},\left| {z}_{0}\right|  < r,\;\left| {P\left( {z}_{0}\right) }\right|  < \mathop{\sup }\limits_{{\left| z\right|  = r}}\left| {P\left( z\right) }\right| .
\]

Solution. Tout découle du résultat suivant.

> Solution. Everything follows from the following result.

Lemme. \( \forall a \in \mathbb{C},\forall \rho > 0,\exists b \in \mathbb{C},\left| {b - a}\right| < \rho \) tel que \( \left| {P\left( b\right) }\right| > \left| {P\left( a\right) }\right| \) .

> Lemma. \( \forall a \in \mathbb{C},\forall \rho > 0,\exists b \in \mathbb{C},\left| {b - a}\right| < \rho \) such that \( \left| {P\left( b\right) }\right| > \left| {P\left( a\right) }\right| \) .

En effet. Quitte à multiplier \( P \) par \( {e}^{i\psi } \) avec \( \psi \in \mathbb{R} \) bien choisi, on peut supposer \( P\left( a\right) \in {\mathbb{R}}^{ + } \) . Soit \( n = \deg P \) , et posons \( Q\left( X\right) = P\left( {X + a}\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{q}_{i}{X}^{i} \) . On a \( {q}_{0} = Q\left( 0\right) = P\left( a\right) \in {\mathbb{R}}^{ + } \) . Par ailleurs, \( {q}_{n} \neq 0 \) de sorte que \( k = \inf \left\{ {i \mid 1 \leq i \leq n,{q}_{i} \neq 0}\right\} \) existe. On peut écrire

> Indeed. By multiplying \( P \) by a well-chosen \( {e}^{i\psi } \) with \( \psi \in \mathbb{R} \), we can assume \( P\left( a\right) \in {\mathbb{R}}^{ + } \). Let \( n = \deg P \), and let us set \( Q\left( X\right) = P\left( {X + a}\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{q}_{i}{X}^{i} \). We have \( {q}_{0} = Q\left( 0\right) = P\left( a\right) \in {\mathbb{R}}^{ + } \). Furthermore, \( {q}_{n} \neq 0 \) so that \( k = \inf \left\{ {i \mid 1 \leq i \leq n,{q}_{i} \neq 0}\right\} \) exists. We can write

\[
Q\left( z\right)  = {q}_{0} + {q}_{k}{z}^{k}\left( {1 + \varphi \left( z\right) }\right) \;\text{ avec }\;\mathop{\lim }\limits_{{z \rightarrow  0}}\varphi \left( z\right)  = 0.
\]

Il existe \( {\rho }^{\prime },0 < {\rho }^{\prime } < \rho \) tel que \( \forall z \in \mathbb{C},\left| z\right| \leq {\rho }^{\prime },\left| {\varphi \left( z\right) }\right| \leq 1/2 \) . Écrivons \( {q}_{k} = \left| {q}_{k}\right| {e}^{i\theta },\theta \in \mathbb{R} \) . Soit \( {z}_{0} = {\rho }^{\prime }{e}^{-{i\theta }/k} \) . On a \( Q\left( {z}_{0}\right) = {q}_{0} + \left| {q}_{k}\right| {\rho }^{\prime k}\left\lbrack {1 + \varphi \left( {z}_{0}\right) }\right\rbrack \) , donc comme \( {q}_{0} \in {\mathbb{R}}^{ + } \) :

> There exists \( {\rho }^{\prime },0 < {\rho }^{\prime } < \rho \) such that \( \forall z \in \mathbb{C},\left| z\right| \leq {\rho }^{\prime },\left| {\varphi \left( z\right) }\right| \leq 1/2 \). Let us write \( {q}_{k} = \left| {q}_{k}\right| {e}^{i\theta },\theta \in \mathbb{R} \). Let \( {z}_{0} = {\rho }^{\prime }{e}^{-{i\theta }/k} \). We have \( Q\left( {z}_{0}\right) = {q}_{0} + \left| {q}_{k}\right| {\rho }^{\prime k}\left\lbrack {1 + \varphi \left( {z}_{0}\right) }\right\rbrack \), so since \( {q}_{0} \in {\mathbb{R}}^{ + } \):

\[
\left| {Q\left( {z}_{0}\right) }\right|  \geq  \left| {{q}_{0} + \left| {q}_{k}\right| {\rho }^{\prime k}}\right|  - \left| {\left| {q}_{k}\right| {\rho }^{\prime k}\varphi \left( {z}_{0}\right) }\right|  \geq  {q}_{0} + \left| {q}_{k}\right| {\rho }^{\prime k} - \frac{1}{2}\left| {q}_{k}\right| {\rho }^{\prime k} = {q}_{0} + \frac{1}{2}\left| {q}_{k}\right| {\rho }^{\prime k} > {q}_{0} = \left| {Q\left( 0\right) }\right| .
\]

Si \( b = a + {z}_{0} \) , on a donc \( \left| {b - a}\right| = {\rho }^{\prime } < \rho \) et \( \left| {P\left( b\right) }\right| = \left| {Q\left( {z}_{0}\right) }\right| > \left| {Q\left( 0\right) }\right| = \left| {P\left( a\right) }\right| \) , d’où le lemme.

> If \( b = a + {z}_{0} \), we therefore have \( \left| {b - a}\right| = {\rho }^{\prime } < \rho \) and \( \left| {P\left( b\right) }\right| = \left| {Q\left( {z}_{0}\right) }\right| > \left| {Q\left( 0\right) }\right| = \left| {P\left( a\right) }\right| \), hence the lemma.

Montrons maintenant le résultat demandé. L’ensemble \( C = \{ z \in \mathbb{C},\left| z\right| \leq r\} \) est compact, et l’application \( z \mapsto \left| {P\left( z\right) }\right| \) étant continue

> Let us now show the requested result. The set \( C = \{ z \in \mathbb{C},\left| z\right| \leq r\} \) is compact, and the mapping \( z \mapsto \left| {P\left( z\right) }\right| \) being continuous

\[
\exists {z}_{1} \in  \mathbb{C},\left| {z}_{1}\right|  \leq  r,\;\left| {P\left( {z}_{1}\right) }\right|  = \mathop{\sup }\limits_{{\left| z\right|  \leq  r}}\left| {P\left( z\right) }\right| .
\]

\( \left( *\right) \)

> Si \( \left| {z}_{1}\right| < r \) , le lemme entraîne l’existence de \( {z}_{2} \in \mathbb{C},\left| {z}_{2}\right| < r \) tel que \( \left| {P\left( {z}_{2}\right) }\right| > \left| {P\left( {z}_{1}\right) }\right| \) , ce qui est absurde d’après (*). Donc \( \left| {z}_{1}\right| = r \) et donc sup \( {}_{\left| z\right| \leq r}\left| {P\left( z\right) }\right| = \mathop{\sup }\limits_{{\left| z\right| = r}}\left| {P\left( z\right) }\right| \) , d’où : Si \( {z}_{0} \in \mathbb{C} \) , \( \left| {z}_{0}\right| < r,\left| {P\left( {z}_{0}\right) }\right| < \mathop{\sup }\limits_{{\left| z\right| \leq r}}\left| {P\left( z\right) }\right| = \mathop{\sup }\limits_{{\left| z\right| = r}}\left| {P\left( z\right) }\right| . \)

If \( \left| {z}_{1}\right| < r \) , the lemma implies the existence of \( {z}_{2} \in \mathbb{C},\left| {z}_{2}\right| < r \) such that \( \left| {P\left( {z}_{2}\right) }\right| > \left| {P\left( {z}_{1}\right) }\right| \) , which is absurd according to (*). Therefore \( \left| {z}_{1}\right| = r \) and thus sup \( {}_{\left| z\right| \leq r}\left| {P\left( z\right) }\right| = \mathop{\sup }\limits_{{\left| z\right| = r}}\left| {P\left( z\right) }\right| \) , whence: If \( {z}_{0} \in \mathbb{C} \) , \( \left| {z}_{0}\right| < r,\left| {P\left( {z}_{0}\right) }\right| < \mathop{\sup }\limits_{{\left| z\right| \leq r}}\left| {P\left( z\right) }\right| = \mathop{\sup }\limits_{{\left| z\right| = r}}\left| {P\left( z\right) }\right| . \)

> Remarque. On trouve dans le tome d'analyse (voir le chapitre sur les fonctions de plusieurs variables) un résultat équivalent sur les fonctions harmoniques.

Remark. An equivalent result for harmonic functions can be found in the analysis volume (see the chapter on functions of several variables).

> - Plus généralement, le lemme permet également de montrer que pour tout compact \( C \subset  \mathbb{C} \) , on a : \( \forall {z}_{0} \in  \overset{ \circ  }{C},\left| {P\left( {z}_{0}\right) }\right|  < \mathop{\sup }\limits_{{z \in  \operatorname{Fr}\left( C\right) }}\left| {P\left( z\right) }\right| \) où \( \operatorname{Fr}\left( C\right) \) désigne la frontière de \( C \) .

- More generally, the lemma also allows us to show that for any compact \( C \subset  \mathbb{C} \) , we have: \( \forall {z}_{0} \in  \overset{ \circ  }{C},\left| {P\left( {z}_{0}\right) }\right|  < \mathop{\sup }\limits_{{z \in  \operatorname{Fr}\left( C\right) }}\left| {P\left( z\right) }\right| \) where \( \operatorname{Fr}\left( C\right) \) denotes the boundary of \( C \) .

> EXERCICE 10. Soit \( n \in {\mathbb{N}}^{ * } \) et \( {z}_{1},\ldots ,{z}_{n} \) des nombres complexes de module 1. Montrer qu’il existe \( z \in \mathbb{C} \) , de module 1, tel que \( \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) .

EXERCISE 10. Let \( n \in {\mathbb{N}}^{ * } \) and \( {z}_{1},\ldots ,{z}_{n} \) be complex numbers with modulus 1. Show that there exists \( z \in \mathbb{C} \) , of modulus 1, such that \( \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) .

> Solution. Soit le polynôme \( P\left( X\right) = \mathop{\prod }\limits_{{k = 1}}^{n}\left( {X - {z}_{k}}\right) \) . On a \( \left| {P\left( 0\right) }\right| = \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) , et d’après le principe du maximum (voir l’exercice précédent) on en déduit \( \mathop{\sup }\limits_{{\left| z\right| = 1}}\left| {P\left( z\right) }\right| > \left| {P\left( 0\right) }\right| = 1 \) . Donc il existe \( {z}_{0} \in \mathbb{C},\left| {z}_{0}\right| = 1 \) , tel que \( \left| {P\left( {z}_{0}\right) }\right| > 1 \) . Soit \( \alpha ,\beta \in \mathbb{R} \) tel que \( {z}_{0} = {e}^{i\alpha } \) et \( {z}_{1} = {e}^{i\beta } \) . La fonction \( f : \mathbb{R} \rightarrow \mathbb{R}\;\theta \mapsto \left| {P\left( {e}^{i\theta }\right) }\right| \) est continue. Comme \( f\left( \alpha \right) = 0 \) et \( f\left( \beta \right) > 1 \) , le théorème des valeurs intermédiaires nous assure l’existence de \( \theta \in \mathbb{R} \) tel que \( f\left( \theta \right) = 1 \) . En notant \( z = {e}^{i\theta } \) ceci s’écrit \( \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) .

Solution. Let the polynomial be \( P\left( X\right) = \mathop{\prod }\limits_{{k = 1}}^{n}\left( {X - {z}_{k}}\right) \) . We have \( \left| {P\left( 0\right) }\right| = \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) , and according to the maximum principle (see the previous exercise) we deduce \( \mathop{\sup }\limits_{{\left| z\right| = 1}}\left| {P\left( z\right) }\right| > \left| {P\left( 0\right) }\right| = 1 \) . Thus there exists \( {z}_{0} \in \mathbb{C},\left| {z}_{0}\right| = 1 \) , such that \( \left| {P\left( {z}_{0}\right) }\right| > 1 \) . Let \( \alpha ,\beta \in \mathbb{R} \) be such that \( {z}_{0} = {e}^{i\alpha } \) and \( {z}_{1} = {e}^{i\beta } \) . The function \( f : \mathbb{R} \rightarrow \mathbb{R}\;\theta \mapsto \left| {P\left( {e}^{i\theta }\right) }\right| \) is continuous. Since \( f\left( \alpha \right) = 0 \) and \( f\left( \beta \right) > 1 \) , the intermediate value theorem ensures the existence of \( \theta \in \mathbb{R} \) such that \( f\left( \theta \right) = 1 \) . By denoting \( z = {e}^{i\theta } \) this is written as \( \mathop{\prod }\limits_{{k = 1}}^{n}\left| {z - {z}_{k}}\right| = 1 \) .

> Remarque. La clé de l'exercice est l'inégalité

Remark. The key to the exercise is the inequality

\[
\left| {P\left( 0\right) }\right|  \leq  \mathop{\sup }\limits_{{\left| z\right|  = 1}}\left| {P\left( z\right) }\right|
\]

\( \left( *\right) \)

> On peut la retrouver sans utiliser le principe du maximum,à partir de l’identité \( P\left( 0\right) = \; \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( {e}^{i\theta }\right) {d\theta } \) , qui est un cas particulier \( \left( {k = 0}\right) \) de l’identité suivante

It can be found without using the maximum principle, starting from the identity \( P\left( 0\right) = \; \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( {e}^{i\theta }\right) {d\theta } \) , which is a special case \( \left( {k = 0}\right) \) of the following identity

\[
\forall P = \mathop{\sum }\limits_{{j = 0}}^{n}{a}_{j}{X}^{j} \in  \mathbb{C}\left\lbrack  X\right\rbrack  ,\;\forall k \in  \{ 0,\ldots , n\} ,\;{a}_{k} = \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( {e}^{i\theta }\right) {e}^{-{ik\theta }}{d\theta }.
\]

(à rapprocher de l'identité (*) de la remarque 18 page 348, sur les fonctions caractéris-tiques). La preuve est immédiate, il suffit d'écrire

> (to be compared with identity (*) in remark 18 on page 348, regarding characteristic functions). The proof is immediate; it suffices to write

\[
{\int }_{0}^{2\pi }P\left( {e}^{i\theta }\right) {e}^{-{ik\theta }}{d\theta } = \mathop{\sum }\limits_{{j = 0}}^{n}{a}_{j}{\int }_{0}^{2\pi }{e}^{ij\theta }{e}^{-{ik\theta }}{d\theta } = \mathop{\sum }\limits_{{j = 0}}^{n}{a}_{j}{\int }_{0}^{2\pi }{e}^{i\left( {j - k}\right) \theta }{d\theta }
\]

puis de remarquer que \( {\int }_{0}^{2\pi }{e}^{i\ell \theta }{d\theta } = {2\pi } \) si \( \ell = 0, = 0 \) si \( \ell \in {\mathbb{Z}}^{ * } \) . On peut également prouver l’inégalité (*) à partir de l’identité \( P\left( 0\right) = \frac{1}{m}\mathop{\sum }\limits_{{k = 0}}^{{m - 1}}P\left( {\omega }^{k}\right) \) avec \( \omega = {e}^{{2i\pi }/m} \) (qu’on retrouve dans le problème 1 page 87 sur la transformée de Fourier discrète d'un polynôme) vraie dès que \( m > n \) , qui montre l’existence de \( k \) tel que \( \left| {P\left( 0\right) }\right| \leq \left| {P\left( {\omega }^{k}\right) }\right| \) . .

> then to note that \( {\int }_{0}^{2\pi }{e}^{i\ell \theta }{d\theta } = {2\pi } \) if \( \ell = 0, = 0 \) if \( \ell \in {\mathbb{Z}}^{ * } \) . One can also prove inequality (*) starting from the identity \( P\left( 0\right) = \frac{1}{m}\mathop{\sum }\limits_{{k = 0}}^{{m - 1}}P\left( {\omega }^{k}\right) \) with \( \omega = {e}^{{2i\pi }/m} \) (which is found in problem 1 on page 87 regarding the discrete Fourier transform of a polynomial) true as soon as \( m > n \) , which shows the existence of \( k \) such that \( \left| {P\left( 0\right) }\right| \leq \left| {P\left( {\omega }^{k}\right) }\right| \) .

EXERCICE 11. On considère \( n \) entiers distincts \( {a}_{1},{a}_{2},\cdots ,{a}_{n} \) .

> EXERCISE 11. Consider \( n \) distinct integers \( {a}_{1},{a}_{2},\cdots ,{a}_{n} \) .

a) Prouver que \( P = \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) \cdots \left( {X - {a}_{n}}\right) - 1 \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) (c’est- à-dire que si \( P = {FG} \) avec \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack \) , alors \( F \) ou \( G \) est constant).

> a) Prove that \( P = \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) \cdots \left( {X - {a}_{n}}\right) - 1 \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) (i.e., if \( P = {FG} \) with \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack \), then \( F \) or \( G \) is constant).

b) Prouver que \( P = {\left( X - {a}_{1}\right) }^{2}{\left( X - {a}_{2}\right) }^{2}\cdots {\left( X - {a}_{n}\right) }^{2} + 1 \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) .

> b) Prove that \( P = {\left( X - {a}_{1}\right) }^{2}{\left( X - {a}_{2}\right) }^{2}\cdots {\left( X - {a}_{n}\right) }^{2} + 1 \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \).

Solution. a) Supposons \( P \) réductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Il existe deux polynômes \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( F\right) < \; n \) et \( \deg \left( G\right) < n \) , tels que

> Solution. a) Suppose \( P \) is reducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \). There exist two polynomials \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( F\right) < \; n \) and \( \deg \left( G\right) < n \) such that

\[
P\left( X\right)  = \left( {X - {a}_{1}}\right) \left( {X - {a}_{2}}\right) \cdots \left( {X - {a}_{n}}\right)  - 1 = F\left( X\right) G\left( X\right) .
\]

Pour tout \( i,1 \leq i \leq n \) , on a \( F\left( {a}_{i}\right) G\left( {a}_{i}\right) = - 1\;\left( *\right) \) . Comme \( F \) et \( G \) sont à coefficients entiers, \( F\left( {a}_{i}\right) \) et \( G\left( {a}_{i}\right) \) sont entiers. Avec (*), on en déduit que pour \( 1 \leq i \leq n, F\left( {a}_{i}\right) = - G\left( {a}_{i}\right) = \pm 1 \) . Le polynôme \( F + G \) s’annule donc aux points \( {a}_{i},1 \leq i \leq n \) . Or \( \deg \left( {F + G}\right) \leq \sup \{ \deg \left( F\right) ,\deg \left( G\right) \} < \; n \) , ce qui entraîne la nullité de \( F + G \) . Donc \( F = - G \) , d’où \( P = - {F}^{2} \) . Cette dernière égalité est impossible puisque \( P \) est unitaire et que \( - {F}^{2} \) ne l’est pas. D’où le résultat.

> For all \( i,1 \leq i \leq n \), we have \( F\left( {a}_{i}\right) G\left( {a}_{i}\right) = - 1\;\left( *\right) \). Since \( F \) and \( G \) have integer coefficients, \( F\left( {a}_{i}\right) \) and \( G\left( {a}_{i}\right) \) are integers. From (*), we deduce that for \( 1 \leq i \leq n, F\left( {a}_{i}\right) = - G\left( {a}_{i}\right) = \pm 1 \). The polynomial \( F + G \) therefore vanishes at points \( {a}_{i},1 \leq i \leq n \). However, \( \deg \left( {F + G}\right) \leq \sup \{ \deg \left( F\right) ,\deg \left( G\right) \} < \; n \), which implies that \( F + G \) is zero. Thus \( F = - G \), hence \( P = - {F}^{2} \). This last equality is impossible since \( P \) is monic and \( - {F}^{2} \) is not. Hence the result.

b) Supposons \( P \) réductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Il existe \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( F\right) \geq 1 \) et \( \deg \left( G\right) \geq 1 \) , tels que

> b) Suppose \( P \) is reducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \). There exist \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( F\right) \geq 1 \) and \( \deg \left( G\right) \geq 1 \) such that

\[
P = {\left( X - {a}_{1}\right) }^{2}{\left( X - {a}_{2}\right) }^{2}\cdots {\left( X - {a}_{n}\right) }^{2} + 1 = F\left( X\right) G\left( X\right) .
\]

On peut supposer \( F \) et \( G \) unitaires (l’égalité précédente entraîne que les coefficients dominants de \( F \) et \( G \) sont égaux tout deux soit à 1, soit à -1). Soit \( k = \deg \left( F\right) ,\ell = \deg \left( G\right) \) , \( \ell = \deg \left( G\right) \) , de sorte que \( k + \ell = {2n}. \)

> We can assume \( F \) and \( G \) are monic (the previous equality implies that the leading coefficients of \( F \) and \( G \) are both equal to either 1 or -1). Let \( k = \deg \left( F\right) ,\ell = \deg \left( G\right) \), \( \ell = \deg \left( G\right) \), such that \( k + \ell = {2n}. \)

La forme de \( P \) montre que pour tout réel \( x, P\left( x\right) \geq 1 \) . Ainsi, \( P \) ne s’annule pas sur \( \mathbb{R} \) , il en est donc de même de \( F \) et \( G \) qui alors gardent un signe constant sur \( \mathbb{R} \) . De plus \( F \) et \( G \) sont unitaires et prennent donc des valeurs \( > 0 \) sur \( \mathbb{R} \) .

> The form of \( P \) shows that for any real \( x, P\left( x\right) \geq 1 \) . Thus, \( P \) does not vanish on \( \mathbb{R} \) , and the same holds for \( F \) and \( G \) , which therefore maintain a constant sign on \( \mathbb{R} \) . Furthermore, \( F \) and \( G \) are monic and thus take \( > 0 \) values on \( \mathbb{R} \) .

Pour tout \( i,1 \leq i \leq n, F\left( {a}_{i}\right) G\left( {a}_{i}\right) = 1\;\left( {* * }\right) \) . Comme de plus \( F\left( {a}_{i}\right) \) et \( G\left( {a}_{i}\right) \) sont entiers et positifs, on en déduit que pour tout \( i, F\left( {a}_{i}\right) = G\left( {a}_{i}\right) = 1 \) .

> For any \( i,1 \leq i \leq n, F\left( {a}_{i}\right) G\left( {a}_{i}\right) = 1\;\left( {* * }\right) \) . Since, moreover, \( F\left( {a}_{i}\right) \) and \( G\left( {a}_{i}\right) \) are integers and positive, we deduce that for any \( i, F\left( {a}_{i}\right) = G\left( {a}_{i}\right) = 1 \) .

Si \( k = \deg \left( F\right) < \ell = \deg \left( G\right) \) , alors \( k < n \) . Or pour tout \( i, F\left( {a}_{i}\right) = 1 \) ; autrement dit, le polynôme \( F - 1 \) s’annule en \( n \) points donc est nul (son degré est \( < n \) ). Finalement \( F = 1 \) , ce qui est absurde car \( \deg \left( F\right) \geq 1 \) . De même l’inégalité \( \ell < k \) est impossible. On a donc \( \deg \left( F\right) = \; \deg \left( G\right) = n \) .

> If \( k = \deg \left( F\right) < \ell = \deg \left( G\right) \) , then \( k < n \) . However, for any \( i, F\left( {a}_{i}\right) = 1 \) ; in other words, the polynomial \( F - 1 \) vanishes at \( n \) points and is therefore zero (its degree is \( < n \) ). Finally \( F = 1 \) , which is absurd because \( \deg \left( F\right) \geq 1 \) . Similarly, the inequality \( \ell < k \) is impossible. We therefore have \( \deg \left( F\right) = \; \deg \left( G\right) = n \) .

D’après \( \left( {* * }\right) \) , pour tout \( i,1 \leq i \leq n, F\left( {a}_{i}\right) = G\left( {a}_{i}\right) \) . Le polynôme \( F - G \) s’annule donc en \( n \) points. Or \( \deg \left( {F - G}\right) \leq n - 1 \) ( \( F \) et \( G \) sont de degré \( n \) et sont tout deux unitaires), donc \( F - G = 0 \) . Donc \( F = G \) . Finalement, on a \( P\left( X\right) = F{\left( X\right) }^{2} \) , c’est-à-dire \( F{\left( X\right) }^{2} - {\left( X - {a}_{1}\right) }^{2}\cdots {\left( X - {a}_{n}\right) }^{2} = 1 \) ou encore

> According to \( \left( {* * }\right) \) , for any \( i,1 \leq i \leq n, F\left( {a}_{i}\right) = G\left( {a}_{i}\right) \) . The polynomial \( F - G \) therefore vanishes at \( n \) points. However \( \deg \left( {F - G}\right) \leq n - 1 \) ( \( F \) and \( G \) are of degree \( n \) and are both monic), so \( F - G = 0 \) . Thus \( F = G \) . Finally, we have \( P\left( X\right) = F{\left( X\right) }^{2} \) , that is to say \( F{\left( X\right) }^{2} - {\left( X - {a}_{1}\right) }^{2}\cdots {\left( X - {a}_{n}\right) }^{2} = 1 \) or even

\[
\left\lbrack  {F - \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) }\right\rbrack  \left\lbrack  {F + \left( {X - {a}_{1}}\right) \cdots \left( {X - {a}_{n}}\right) }\right\rbrack   = 1,
\]

égalité impossible à réaliser. Le polynôme \( P \) est donc irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) .

> equality impossible to achieve. The polynomial \( P \) is therefore irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) .

Remarque. On peut également montrer que \( {\left( X - {a}_{1}\right) }^{4}\cdots {\left( X - {a}_{n}\right) }^{4} + 1 \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , mais c’est plus difficile.

> Remark. One can also show that \( {\left( X - {a}_{1}\right) }^{4}\cdots {\left( X - {a}_{n}\right) }^{4} + 1 \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) , but it is more difficult.

- En fait, les polynômes exhibés sont irréductibles dans \( \mathbb{Q}\left\lbrack  X\right\rbrack \) . En effet, d’après le lemme de Gauss (voir l’exercice 4 page 62) tout polynôme de \( \mathbb{Z}\left\lbrack  X\right\rbrack \) irréductible dans \( \mathbb{Z}\left\lbrack  X\right\rbrack \) est irréductible dans \( \mathbb{Q}\left\lbrack  X\right\rbrack \) .

> - In fact, the polynomials exhibited are irreducible in \( \mathbb{Q}\left\lbrack  X\right\rbrack \) . Indeed, according to Gauss's lemma (see exercise 4 page 62), any polynomial in \( \mathbb{Z}\left\lbrack  X\right\rbrack \) irreducible in \( \mathbb{Z}\left\lbrack  X\right\rbrack \) is irreducible in \( \mathbb{Q}\left\lbrack  X\right\rbrack \) .

EXERCICE 12 (QUELQUES POLYNÖMES IRRÉDUCTIBLES). Si \( F = {a}_{0} + {a}_{1}X + \cdots {a}_{n}{X}^{n} \in \; \mathbb{Z}\left\lbrack X\right\rbrack \) , on note (pour \( p \in {\mathbb{N}}^{ * } \) ), \( \bar{F} = \overline{{a}_{0}} + \overline{{a}_{1}}X + \cdots + \overline{{a}_{n}}{X}^{n} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) où pour tout \( i,\overline{{a}_{i}} \) désigne la classe de \( {a}_{i} \) dans \( \mathbb{Z}/p\mathbb{Z} \) .

> EXERCISE 12 (SOME IRREDUCIBLE POLYNOMIALS). If \( F = {a}_{0} + {a}_{1}X + \cdots {a}_{n}{X}^{n} \in \; \mathbb{Z}\left\lbrack X\right\rbrack \), we denote (for \( p \in {\mathbb{N}}^{ * } \)), \( \bar{F} = \overline{{a}_{0}} + \overline{{a}_{1}}X + \cdots + \overline{{a}_{n}}{X}^{n} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) where for all \( i,\overline{{a}_{i}} \) denotes the class of \( {a}_{i} \) in \( \mathbb{Z}/p\mathbb{Z} \).

1/ \( \operatorname{Si}P \in \mathbb{Z}\left\lbrack X\right\rbrack \) , unitaire, est tel que \( \bar{P} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) est irréductible dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , montrer que \( P \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . La réciproque est elle vraie ?

> 1/ \( \operatorname{Si}P \in \mathbb{Z}\left\lbrack X\right\rbrack \), monic, is such that \( \bar{P} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) is irreducible in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \), show that \( P \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \). Is the converse true?

2/ Montrer que \( F = {X}^{4} + X + 1 \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) .

> 2/ Show that \( F = {X}^{4} + X + 1 \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \).

3/ Soit \( p \in {\mathbb{N}}^{ * } \) un nombre premier et \( F = {X}^{p} - X - 1 \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

> 3/ Let \( p \in {\mathbb{N}}^{ * } \) be a prime number and \( F = {X}^{p} - X - 1 \in \mathbb{Z}\left\lbrack X\right\rbrack \).

a) Soit \( \alpha \) une racine de \( \bar{F} \) dans le corps des racines de \( \bar{F} \) . Montrer que les racines de \( \bar{F} \) sont exactement \( \alpha ,\alpha + \overline{1},\cdots ,\alpha + \overline{p - 1} \) .

> a) Let \( \alpha \) be a root of \( \bar{F} \) in the splitting field of \( \bar{F} \). Show that the roots of \( \bar{F} \) are exactly \( \alpha ,\alpha + \overline{1},\cdots ,\alpha + \overline{p - 1} \).

b) En déduire que \( \bar{F} \) est irréductible dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , et que \( F \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) .

> b) Deduce that \( \bar{F} \) is irreducible in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \), and that \( F \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \).

Solution. 1/ C’est immédiat. Si \( P = {FG} \) avec \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack \) , unitaires, alors \( \bar{P} = \bar{F}\bar{G} \) dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . Comme \( \bar{P} \) est irréductible dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , ceci entraîne \( \deg \left( \bar{F}\right) = 0 \) ou \( \deg \left( \bar{G}\right) = 0 \) . Les polynômes \( F \) et \( G \) étant unitaires, on a \( \deg \left( F\right) = \deg \left( \bar{F}\right) \) et \( \deg \left( G\right) = \deg \left( \bar{G}\right) \) et donc \( F \) ou \( G \) est constant, ce qui prouve l’irréductibilité de \( P \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) ( \( P \) est alors irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) , voir l’exercice 4 page 62). La réciproque est fausse. Par exemple, \( P = {X}^{2} - {2X} - 1 \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) et pourtant \( \bar{P} = {\left( \bar{X} - \overline{1}\right) }^{2} \) n’est pas irréductible dans \( \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) .

> Solution. 1/ It is immediate. If \( P = {FG} \) with \( F, G \in \mathbb{Z}\left\lbrack X\right\rbrack \) monic, then \( \bar{P} = \bar{F}\bar{G} \) in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . Since \( \bar{P} \) is irreducible in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , this implies \( \deg \left( \bar{F}\right) = 0 \) or \( \deg \left( \bar{G}\right) = 0 \) . As the polynomials \( F \) and \( G \) are monic, we have \( \deg \left( F\right) = \deg \left( \bar{F}\right) \) and \( \deg \left( G\right) = \deg \left( \bar{G}\right) \) and thus \( F \) or \( G \) is constant, which proves the irreducibility of \( P \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) ( \( P \) is then irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) , see exercise 4 on page 62). The converse is false. For example, \( P = {X}^{2} - {2X} - 1 \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) yet \( \bar{P} = {\left( \bar{X} - \overline{1}\right) }^{2} \) is not irreducible in \( \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) .

2 / On va montrer que \( \bar{F} \) est irréductible dans \( \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) , ce qui prouvera le résultat en vertu de 1 /. Supposons \( \bar{F} = {PQ} \) avec \( P, Q \in \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1,\deg \left( Q\right) \geq 1 \) .

> 2/ We will show that \( \bar{F} \) is irreducible in \( \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack \) , which will prove the result by virtue of 1/. Suppose \( \bar{F} = {PQ} \) with \( P, Q \in \mathbb{Z}/2\mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1,\deg \left( Q\right) \geq 1 \) .

Le polynôme \( \bar{F} \) n’a aucune racine dans \( \mathbb{Z}/2\mathbb{Z} \) , donc \( \deg \left( P\right) = \deg \left( Q\right) = 2 \) .

> The polynomial \( \bar{F} \) has no roots in \( \mathbb{Z}/2\mathbb{Z} \) , therefore \( \deg \left( P\right) = \deg \left( Q\right) = 2 \) .

Le coefficient dominant et le coefficient constant de \( \bar{F} \) étant égaux à \( \overline{1}, P \) et \( Q \) sont néces-sairement de la forme

> The leading coefficient and the constant coefficient of \( \bar{F} \) being equal to \( \overline{1}, P \) and \( Q \) are necessarily of the form

\[
P = {X}^{2} + {aX} + \overline{1}\;\text{ et }\;Q = {X}^{2} + {bX} + \overline{1},\;a, b \in  \mathbb{Z}/2\mathbb{Z}.
\]

Donc \( \bar{F} = {X}^{4} + X + \overline{1} = {PQ} = {X}^{4} + \left( {a + b}\right) \left( {{X}^{3} + X}\right) + \left( {\overline{2} + {ab}}\right) {X}^{2} + \overline{1} \) , et donc le coefficient de \( {X}^{3} \) est égal à celui de \( X \) dans \( \bar{F} \) , ce qui est absurde étant donnée la forme de \( \bar{F} \) .

> Thus \( \bar{F} = {X}^{4} + X + \overline{1} = {PQ} = {X}^{4} + \left( {a + b}\right) \left( {{X}^{3} + X}\right) + \left( {\overline{2} + {ab}}\right) {X}^{2} + \overline{1} \) , and therefore the coefficient of \( {X}^{3} \) is equal to that of \( X \) in \( \bar{F} \) , which is absurd given the form of \( \bar{F} \) .

3/a) Notons \( \mathbb{K} \) le corps des racines de \( \bar{F},\alpha \) une racine de \( \bar{F} \) dans \( \mathbb{K} \) . Le corps \( \mathbb{K} \) étant de caractéristique \( p \) (car surcorps de \( \mathbb{Z}/p\mathbb{Z} \) ), on a

> 3/a) Let \( \mathbb{K} \) be the splitting field of \( \bar{F},\alpha \) and a root of \( \bar{F} \) in \( \mathbb{K} \) . Since the field \( \mathbb{K} \) has characteristic \( p \) (as an extension field of \( \mathbb{Z}/p\mathbb{Z} \) ), we have

\[
\forall x \in  \mathbb{K},\;\bar{F}\left( x\right)  = \bar{F}\left( x\right)  - \bar{F}\left( \alpha \right)  = {x}^{p} - {\alpha }^{p} - \left( {x - \alpha }\right)  = {\left( x - \alpha \right) }^{p} - \left( {x - \alpha }\right)
\]

(pour se convaincre de la dernière égalité, développer \( {\left( x - \alpha \right) }^{p} \) par la formule du binôme et utiliser le fait que \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) si \( 1 \leq k \leq p - 1 \) ). Donc \( x \in \mathbb{K} \) est une racine de \( \bar{F} \) si et seulement si \( x - \alpha \) est une racine de \( {X}^{p} - X \) , c’est-à-dire si et seulement si \( x - \alpha \in \{ \overline{0},\overline{1},\ldots ,\overline{p - 1}\} \) (les racines du polynôme \( {X}^{p} - X \) sont \( \overline{0},\overline{1},\ldots ,\overline{p - 1} \) en vertu du théorème de Fermat).

> (to convince yourself of the last equality, expand \( {\left( x - \alpha \right) }^{p} \) using the binomial theorem and use the fact that \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) if \( 1 \leq k \leq p - 1 \) ). Thus \( x \in \mathbb{K} \) is a root of \( \bar{F} \) if and only if \( x - \alpha \) is a root of \( {X}^{p} - X \) , that is to say if and only if \( x - \alpha \in \{ \overline{0},\overline{1},\ldots ,\overline{p - 1}\} \) (the roots of the polynomial \( {X}^{p} - X \) are \( \overline{0},\overline{1},\ldots ,\overline{p - 1} \) by Fermat's theorem).

b) Soit \( G \) un facteur irréductible unitaire de \( \bar{F} \) dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . Notons \( k = \deg \left( G\right) \) . D’après la question précédente, les racines de \( G \) dans \( \mathbb{K} \) sont de la forme \( \alpha + {a}_{1},\cdots ,\alpha + {a}_{k} \) où les \( {a}_{i} \) sont dans \( \mathbb{Z}/p\mathbb{Z} \) . De plus \( G \) étant unitaire, le coefficient du monôme de degré \( k - 1 \) de \( G \) est au signe près la somme de ses racines. Comme \( G \) a ses coefficients dans \( \mathbb{Z}/p\mathbb{Z} \) , on en déduit que \( \mathop{\sum }\limits_{{i = 1}}^{k}\left( {\alpha + {a}_{i}}\right) \in \mathbb{Z}/p\mathbb{Z} \) , et comme les \( {a}_{i} \in \mathbb{Z}/p\mathbb{Z},{k\alpha } \in \mathbb{Z}/p\mathbb{Z} \) . Or \( \alpha \notin \mathbb{Z}/p\mathbb{Z} \) (sinon \( \bar{F}\left( \alpha \right) = \; \left. {\left( {{\alpha }^{p} - \alpha }\right) + \overline{1} = \overline{1} \neq \overline{0}}\right) \) . Le fait que \( {k\alpha } \in \mathbb{Z}/p\mathbb{Z} \) entraîne donc que \( \bar{k} = \overline{0} \) et donc \( k = p \) puisque \( 1 \leq k \leq p \) . Donc \( G \) est de degré \( p \) ce qui entraîne que \( \bar{F} = G \) est irréductible dans \( \mathbb{Z}/p\mathbb{Z} \) . Donc \( F \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) d’après la question \( 1/ \) .

> b) Let \( G \) be a monic irreducible factor of \( \bar{F} \) in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . Let \( k = \deg \left( G\right) \) . According to the previous question, the roots of \( G \) in \( \mathbb{K} \) are of the form \( \alpha + {a}_{1},\cdots ,\alpha + {a}_{k} \) where the \( {a}_{i} \) are in \( \mathbb{Z}/p\mathbb{Z} \) . Furthermore, since \( G \) is monic, the coefficient of the monomial of degree \( k - 1 \) of \( G \) is, up to a sign, the sum of its roots. As \( G \) has its coefficients in \( \mathbb{Z}/p\mathbb{Z} \) , we deduce that \( \mathop{\sum }\limits_{{i = 1}}^{k}\left( {\alpha + {a}_{i}}\right) \in \mathbb{Z}/p\mathbb{Z} \) , and since the \( {a}_{i} \in \mathbb{Z}/p\mathbb{Z},{k\alpha } \in \mathbb{Z}/p\mathbb{Z} \) . However \( \alpha \notin \mathbb{Z}/p\mathbb{Z} \) (otherwise \( \bar{F}\left( \alpha \right) = \; \left. {\left( {{\alpha }^{p} - \alpha }\right) + \overline{1} = \overline{1} \neq \overline{0}}\right) \) . The fact that \( {k\alpha } \in \mathbb{Z}/p\mathbb{Z} \) therefore implies that \( \bar{k} = \overline{0} \) and thus \( k = p \) since \( 1 \leq k \leq p \) . So \( G \) is of degree \( p \) which implies that \( \bar{F} = G \) is irreducible in \( \mathbb{Z}/p\mathbb{Z} \) . Thus \( F \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) according to question \( 1/ \) .

EXERCICE 13 (POLYNÔMES DE TCHÉBYCHEFF). a) Montrer que pour tout \( n \in {\mathbb{N}}^{ * } \) , il existe un unique polynôme \( {T}_{n} \in \mathbb{R}\left\lbrack X\right\rbrack \) tel que \( \forall \theta \in \mathbb{R},{T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) et calculer le coefficient dominant de \( {T}_{n} \) (les \( {T}_{n} \) s’appellent les polynômes de Tchébycheff).

> EXERCISE 13 (CHEBYSHEV POLYNOMIALS). a) Show that for all \( n \in {\mathbb{N}}^{ * } \) , there exists a unique polynomial \( {T}_{n} \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( \forall \theta \in \mathbb{R},{T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) and calculate the leading coefficient of \( {T}_{n} \) (the \( {T}_{n} \) are called Chebyshev polynomials).

b) Montrer que tout \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) unitaire de degré \( n \in {\mathbb{N}}^{ * } \) , on a \( \parallel P{\parallel }_{\infty } \geq {2}^{1 - n} \) où on note \( \parallel P{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in \left\lbrack {-1,1}\right\rbrack }}\left| {P\left( t\right) }\right| . \)

> b) Show that for any monic \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) of degree \( n \in {\mathbb{N}}^{ * } \), we have \( \parallel P{\parallel }_{\infty } \geq {2}^{1 - n} \) where we denote \( \parallel P{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in \left\lbrack {-1,1}\right\rbrack }}\left| {P\left( t\right) }\right| . \)

Solution. a) En posant \( x = \cos \theta \) , on voit que \( {T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) si et seulement si

> Solution. a) By setting \( x = \cos \theta \), we see that \( {T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) if and only if

\[
{T}_{n}\left( x\right)  = \Re \left\lbrack  {\left( \cos \theta  + i\sin \theta \right) }^{n}\right\rbrack   = \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }{C}_{n}^{2k}{\cos }^{n - {2k}}\theta {\left( -{\sin }^{2}\theta \right) }^{k} = \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }{C}_{n}^{2k}{x}^{n - {2k}}{\left( {x}^{2} - 1\right) }^{k}.
\]

(*)

> Ceci montre l'existence et l'unicité de \( {T}_{n} \) , dont la forme polynomiale est donnée par le dernier membre de \( \left( *\right) \) . D’après \( \left( *\right) ,{T}_{n} \) est de degré \( n \) et son coefficient dominant est \( \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack n/2\right\rbrack }{C}_{n}^{2k} = {2}^{n - 1} \) . b) Remarquons déjà que l’identité \( {T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) entraîne \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = 1 \) . Donc le polynôme unitaire \( {U}_{n} = {2}^{1 - n}{T}_{n} \) vérifie \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } = {2}^{1 - n} \) . Soit \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) unitaire et de degré \( n \) . Raisonnons par l’absurde et supposons \( \parallel P{\parallel }_{\infty } < {2}^{1 - n} = {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) . Le polynôme \( Q = {U}_{n} - P \) est de degré \( \leq n - 1 \) (car \( P \) et \( {U}_{n} \) sont unitaires et de degré \( n \) ). En posant \( {x}_{k} = \cos {k\pi }/n \) , on remarque maintenant que \( {T}_{n}\left( {x}_{k}\right) = \cos {k\pi } = {\left( -1\right) }^{k} \) pour \( 0 \leq k \leq n \) . Donc \( Q\left( {x}_{k}\right) = {\left( -1\right) }^{k}{2}^{1 - n} - P\left( {x}_{k}\right) \) , et comme \( \left| {P\left( {x}_{k}\right) }\right| \leq \parallel P{\parallel }_{\infty } < {2}^{1 - n} \) ceci montre que \( Q\left( {x}_{k}\right) \) est non nul et a le signe de \( {\left( -1\right) }^{k} \) . Ainsi, les \( n + 1 \) points \( {\left( {x}_{k}\right) }_{0 \leq k \leq n} \) vérifient \( - 1 = {x}_{n} < {x}_{n - 1} < \ldots < {x}_{1} < {x}_{0} = 1 \) et \( Q \) change de signe entre \( {x}_{k + 1} \) et \( {x}_{k} \) (pour \( 0 \leq k \leq n - 1 \) ). Donc \( Q \) a au moins \( n \) racines, et comme deg \( \left( Q\right) < n \) on a forcément \( Q = 0 \) , donc \( P = {U}_{n} \) ce qui est absurde puisque \( \parallel P{\parallel }_{\infty } < {2}^{1 - n} \) par hypothèse.

This shows the existence and uniqueness of \( {T}_{n} \), whose polynomial form is given by the last term of \( \left( *\right) \). According to \( \left( *\right) ,{T}_{n} \), it is of degree \( n \) and its leading coefficient is \( \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack n/2\right\rbrack }{C}_{n}^{2k} = {2}^{n - 1} \). b) Let us already note that the identity \( {T}_{n}\left( {\cos \theta }\right) = \cos {n\theta } \) implies \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = 1 \). Thus, the monic polynomial \( {U}_{n} = {2}^{1 - n}{T}_{n} \) satisfies \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } = {2}^{1 - n} \). Let \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) be monic and of degree \( n \). Let us reason by contradiction and assume \( \parallel P{\parallel }_{\infty } < {2}^{1 - n} = {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \). The polynomial \( Q = {U}_{n} - P \) is of degree \( \leq n - 1 \) (since \( P \) and \( {U}_{n} \) are monic and of degree \( n \)). By setting \( {x}_{k} = \cos {k\pi }/n \), we now observe that \( {T}_{n}\left( {x}_{k}\right) = \cos {k\pi } = {\left( -1\right) }^{k} \) for \( 0 \leq k \leq n \). Thus \( Q\left( {x}_{k}\right) = {\left( -1\right) }^{k}{2}^{1 - n} - P\left( {x}_{k}\right) \), and since \( \left| {P\left( {x}_{k}\right) }\right| \leq \parallel P{\parallel }_{\infty } < {2}^{1 - n} \), this shows that \( Q\left( {x}_{k}\right) \) is non-zero and has the sign of \( {\left( -1\right) }^{k} \). Thus, the \( n + 1 \) points \( {\left( {x}_{k}\right) }_{0 \leq k \leq n} \) satisfy \( - 1 = {x}_{n} < {x}_{n - 1} < \ldots < {x}_{1} < {x}_{0} = 1 \) and \( Q \) changes sign between \( {x}_{k + 1} \) and \( {x}_{k} \) (for \( 0 \leq k \leq n - 1 \)). Therefore, \( Q \) has at least \( n \) roots, and since deg \( \left( Q\right) < n \), we necessarily have \( Q = 0 \), so \( P = {U}_{n} \), which is absurd since \( \parallel P{\parallel }_{\infty } < {2}^{1 - n} \) by hypothesis.

> Remarque. La propriété de mini-max \( \parallel P{\parallel }_{\infty } \geq {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) pour tout \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) unitaire et de degré \( n \) est remarquable, et fait de la famille \( \left( {T}_{n}\right) \) des polynômes de Tchébycheff une base commode pour l'interpolation polynomiale.

Remark. The mini-max property \( \parallel P{\parallel }_{\infty } \geq {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) for any \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) monic and of degree \( n \) is remarkable, and makes the family \( \left( {T}_{n}\right) \) of Chebyshev polynomials a convenient basis for polynomial interpolation.
