#### 4.2. Fubini's theorems

*Français : 4.2. Théorèmes de Fubini*

Nous n'énoncerons ce théorème que dans certains cas particuliers qui nous suffiront.

> We shall state this theorem only in certain particular cases which will suffice for our purposes.

THÉORÉME 1. Soient \( P \) et \( Q \) deux pavés compacts de \( {\mathbb{R}}^{p} \) et \( {\mathbb{R}}^{q} \) respectivement. Soit \( f : P \times Q \rightarrow \mathbb{R} \) une fonction continue. Alors

> THEOREM 1. Let \( P \) and \( Q \) be two compact rectangles of \( {\mathbb{R}}^{p} \) and \( {\mathbb{R}}^{q} \) respectively. Let \( f : P \times Q \rightarrow \mathbb{R} \) be a continuous function. Then

\[
{\int }_{P \times  Q}f\left( {x, y}\right) {dxdy} = {\int }_{P}\left( {{\int }_{Q}f\left( {x, y}\right) {dy}}\right) {dx} = {\int }_{Q}\left( {{\int }_{P}f\left( {x, y}\right) {dx}}\right) {dy}.
\]

Remarque 4. Par applications successives de ce théorème, on obtient facilement, si \( P = \; \left\lbrack {{a}_{1},{b}_{1}}\right\rbrack \times \cdots \times \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack , \)

> Remark 4. By successive applications of this theorem, one easily obtains, if \( P = \; \left\lbrack {{a}_{1},{b}_{1}}\right\rbrack \times \cdots \times \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack , \)

\[
{\int }_{P}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) d{x}_{1}\cdots d{x}_{n} = {\int }_{{a}_{1}}^{{b}_{1}}\left\lbrack  {{\int }_{{a}_{2}}^{{b}_{2}}\left\lbrack  {\cdots \left\lbrack  {{\int }_{{a}_{n}}^{{b}_{n}}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) d{x}_{n}}\right\rbrack  \cdots }\right\rbrack  d{x}_{2}}\right\rbrack  d{x}_{1},
\]

(égalité qui exprime les intégrales multiples en fonctions d'intégrales simples, ce qui permet de les calculer dans la pratique). Ce dernier terme est parfois noté

> (an equality that expresses multiple integrals as functions of simple integrals, which allows them to be calculated in practice). This last term is sometimes denoted

\[
{\int }_{{a}_{1}}^{{b}_{1}}d{x}_{1}{\int }_{{a}_{2}}^{{b}_{2}}d{x}_{2}\cdots {\int }_{{a}_{n}}^{{b}_{n}}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) d{x}_{n}.
\]

L'ordre d'intégration (sur les \( {x}_{i} \) ) est indifférent, et dans la pratique, on s'arrange pour intégrer dans un ordre qui facile les intégrations.

> The order of integration (over the \( {x}_{i} \) ) is irrelevant, and in practice, one arranges to integrate in an order that facilitates the integrations.

Citons un corollaire important de ce théorème :

> Let us cite an important corollary of this theorem:

COROLLAIRE 1. Soient \( P \) et \( Q \) deux pavés compacts de \( {\mathbb{R}}^{p} \) et \( {\mathbb{R}}^{q} \) , et soient \( g : P \rightarrow \mathbb{R} \) et \( h : Q \rightarrow \mathbb{R} \) deux fonctions continues. Alors

> COROLLARY 1. Let \( P \) and \( Q \) be two compact rectangles of \( {\mathbb{R}}^{p} \) and \( {\mathbb{R}}^{q} \) , and let \( g : P \rightarrow \mathbb{R} \) and \( h : Q \rightarrow \mathbb{R} \) be two continuous functions. Then

\[
{\int }_{P \times  Q}g\left( x\right) h\left( y\right) {dxdy} = \left( {{\int }_{P}g\left( x\right) {dx}}\right)  \cdot  \left( {{\int }_{Q}h\left( y\right) {dy}}\right) .
\]

Le théorème 1 ne permet de calculer des intégrales multiples que sur des pavés. Pour calculer des intégrales multiples sur d'autres ensembles, on utilise les deux théorèmes qui suivent.

> Theorem 1 only allows for the calculation of multiple integrals over rectangles. To calculate multiple integrals over other sets, the two following theorems are used.

##### Summation by stacks, summation by slices.

*Français : Sommation par piles, sommation par tranches.*

THÉORÉME 2 (SOMMATION PAR PILES). Soit B un ensemble mesurable compact de \( {\mathbb{R}}^{n - 1} \) , et deux applications continues \( {\varphi }_{1},{\varphi }_{2} : B \rightarrow \mathbb{R} \) telles que \( {\varphi }_{1} \leq {\varphi }_{2} \) . Alors l’ensemble

> THEOREM 2 (SUMMATION BY STACKS). Let B be a compact measurable set of \( {\mathbb{R}}^{n - 1} \) , and two continuous mappings \( {\varphi }_{1},{\varphi }_{2} : B \rightarrow \mathbb{R} \) such that \( {\varphi }_{1} \leq {\varphi }_{2} \) . Then the set

\[
A = \left\{  {\left( {x,{x}_{n}}\right)  \in  B \times  \mathbb{R} \mid  {\varphi }_{1}\left( x\right)  \leq  {x}_{n} \leq  {\varphi }_{2}\left( x\right) }\right\}
\]

est mesurable sur \( {\mathbb{R}}^{n} \) et pour toute fonction continue \( f : A \rightarrow \mathbb{R} \) , on a

> is measurable on \( {\mathbb{R}}^{n} \) and for any continuous function \( f : A \rightarrow \mathbb{R} \) , we have

\[
{\iint }_{A}f\left( {x,{x}_{n}}\right) {dxd}{x}_{n} = {\int }_{B}\left\lbrack  {{\int }_{{\varphi }_{1}\left( x\right) }^{{\varphi }_{2}\left( x\right) }f\left( {x,{x}_{n}}\right) d{x}_{n}}\right\rbrack  {dx}.
\]

![bo_d7fjkrs91nqc73ereoog_358_332_222_975_503_0.jpg](images/gourdon_analysis_fr_en_013_bod7fjkrs91nqc73ereoog3583322229755030.jpg)

FIGURE 1. à gauche, illustration d'une sommation par piles ; à droite, d'une sommation par tranches.

> FIGURE 1. on the left, illustration of a summation by stacks; on the right, of a summation by slices.

THÉORÉME 3 (SOMMATION PAR TRANCHES). Soit A un ensemble mesurable compact de \( {\mathbb{R}}^{n} \) tel que pour tout \( \left( {x,{x}_{n}}\right) \in {\mathbb{R}}^{n - 1} \times \mathbb{R} \) vérifiant \( \left( {x,{x}_{n}}\right) \in A \) , on ait \( a \leq {x}_{n} \leq b \) . Si pour tout \( {x}_{n} \in \left\lbrack {a, b}\right\rbrack \) , l’ensemble \( A\left( {x}_{n}\right) = \left\{ {x \in {\mathbb{R}}^{n - 1} \mid \left( {x,{x}_{n}}\right) \in A}\right\} \) est mesurable dans \( {\mathbb{R}}^{n - 1} \) , alors pour toute fonction continue \( f : A \rightarrow \mathbb{R} \) , on a

> THEOREM 3 (SUMMATION BY SLICES). Let A be a compact measurable set of \( {\mathbb{R}}^{n} \) such that for any \( \left( {x,{x}_{n}}\right) \in {\mathbb{R}}^{n - 1} \times \mathbb{R} \) satisfying \( \left( {x,{x}_{n}}\right) \in A \) , we have \( a \leq {x}_{n} \leq b \) . If for any \( {x}_{n} \in \left\lbrack {a, b}\right\rbrack \) , the set \( A\left( {x}_{n}\right) = \left\{ {x \in {\mathbb{R}}^{n - 1} \mid \left( {x,{x}_{n}}\right) \in A}\right\} \) is measurable in \( {\mathbb{R}}^{n - 1} \) , then for any continuous function \( f : A \rightarrow \mathbb{R} \) , we have

\[
{\iint }_{A}f\left( {x,{x}_{n}}\right) {dxd}{x}_{n} = {\int }_{a}^{b}\left\lbrack  {{\int }_{A\left( {x}_{n}\right) }f\left( {x,{x}_{n}}\right) {dx}}\right\rbrack  d{x}_{n}.
\]

Remarque 5. - Le résultat de ces deux théorèmes reste évidemment vrai si l’on rem-place la variable \( {x}_{n} \) par l’une des autres variables \( {x}_{i} \) .

> Remark 5. - The result of these two theorems obviously remains true if the variable \( {x}_{n} \) is replaced by one of the other variables \( {x}_{i} \) .

— Ainsi, on dispose de deux méthodes pour réduire le calcul d'intégrales multiples. Selon les cas, l’une peut s’avérer plus pratique que l’autre. Si \( n = 2 \) , ces résultats sont équivalents, et peuvent s'exprimer comme suit.

> — Thus, we have two methods available to reduce the calculation of multiple integrals. Depending on the case, one may prove more practical than the other. If \( n = 2 \) , these results are equivalent, and can be expressed as follows.

Soit \( K \) un compact de \( {\mathbb{R}}^{2} \) de la forme

> Let \( K \) be a compact set of \( {\mathbb{R}}^{2} \) of the form

\[
K = \left\{  {\left( {x, y}\right)  \in  \left\lbrack  {a, b}\right\rbrack   \times  \mathbb{R} \mid  {\varphi }_{1}\left( x\right)  \leq  y \leq  {\varphi }_{2}\left( x\right) }\right\}  ,
\]

où \( {\varphi }_{1} \) et \( {\varphi }_{2} \) sont des applications continues de \( \left\lbrack {a, b}\right\rbrack \) dans \( \mathbb{R} \) . Alors \( K \) est mesurable, et pour toute fonction continue \( f : K \rightarrow \mathbb{R} \) , on a

> where \( {\varphi }_{1} \) and \( {\varphi }_{2} \) are continuous mappings from \( \left\lbrack {a, b}\right\rbrack \) to \( \mathbb{R} \) . Then \( K \) is measurable, and for any continuous function \( f : K \rightarrow \mathbb{R} \) , we have

\[
{\iint }_{K}f\left( {x, y}\right) {dxdy} = {\int }_{a}^{b}\left\lbrack  {{\int }_{{\varphi }_{1}\left( x\right) }^{{\varphi }_{2}\left( x\right) }f\left( {x, y}\right) {dy}}\right\rbrack  {dx}.
\]
