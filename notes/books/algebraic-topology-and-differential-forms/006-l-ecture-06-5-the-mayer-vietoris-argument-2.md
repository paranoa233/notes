#### 6. Künneth 公式

§5 The Mayer-Vietoris Argument (2)

6. Künneth 公式

这节课用 MV 方法证明 Künneth 公式与 Leray-Hirsch 定理.

- Künneth 公式

- Leray-Hirsch 定理

Künneth 公式

命题 5.9. 设 \( M \) , \( F \) 是流形且 \( M \) 的 de Rham 上同调的维数是有限的. 则对每个非负整数 \( n \) ，

\[
{H}^{n}\left( {M \times  F}\right)  = {\bigoplus }_{p + q = n}{H}^{p}\left( M\right) { \otimes  }_{\mathbb{R}}{H}^{q}\left( F\right) .
\]

证. 假定 \( M \) 具有有限好覆盖,一般的情形留待以后.

设两个自然投射为

![bo_d7e85t491nqc73eqefm0_122_945_1003_438_294_0.jpg](images/fu_algebraic_topology_and_differential_forms_009_bod7e85t491nqc73eqefm012294510034382940.jpg)

它们诱导了映射

\[
\psi  : {\Omega }^{ * }\left( M\right)  \otimes  {\Omega }^{ * }\left( F\right)  \rightarrow  {\Omega }^{ * }\left( {M \times  F}\right)
\]

\[
\psi \left( {\omega  \otimes  \phi }\right)  = {\pi }^{ * }\omega  \land  {\rho }^{ * }\phi .
\]

因为 \( {\pi }^{ * } \) , \( {\rho }^{ * } \) 与 \( d \) 可交换, \( \psi \) 可约化到上同调群之间的映射,即

\[
\psi  : {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right)  \rightarrow  {H}^{ * }\left( {M \times  F}\right)
\]

\[
\psi \left( {\left\lbrack  \omega \right\rbrack   \otimes  \left\lbrack  \phi \right\rbrack  }\right)  = \left\lbrack  {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right\rbrack  .
\]

需证 \( \psi \) 是同构.

若 \( M \) 与 \( {\mathbb{R}}^{m} \) 微分同胚，则 Künneth 公式即为 Poincaré 引理:

\[
{H}^{ * }\left( {{\mathbb{R}}^{m} \times  F}\right)  = {H}^{ * }\left( {{\mathbb{R}}^{m - 1} \times  F}\right)  = \cdots  = {H}^{ * }\left( F\right)  = {H}^{ * }\left( {\mathbb{R}}^{m}\right)  \otimes  {H}^{ * }\left( F\right) .
\]

现设 \( U, V \) 是 \( M \) 的开子集, \( n \) 是固定的正整数. 对 \( \mathrm{{MV}} \) 序列

\( \cdots  \rightarrow  {H}^{p}\left( {U \cup  V}\right)  \rightarrow  {H}^{p}\left( U\right)  \oplus  {H}^{p}\left( V\right)  \rightarrow  {H}^{p}\left( {U \cap  V}\right)  \rightarrow  {H}^{p + 1}\left( {U \cup  V}\right)  \rightarrow  \ldots \) 与 \( {H}^{n - p}\left( F\right) \) 作张量积,再对所有整数 \( p \) 求直和*,得

* 为了方便，我们规定:对一个 \( m \) 维流形，当 \( q < 0 \) 或 \( q > m \) , \( {\Omega }^{q}\left( M\right)  = 0 \) . 这样出现在 \( { \oplus  }_{p}{H}^{p + 1}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right) \) 中可能不为零的直和加项为 \( p \) 从-1到 \( n \) 的项.

\[
{ \oplus  }_{p}{H}^{p}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

\[
{ \oplus  }_{p}\left( {{H}^{p}\left( U\right)  \otimes  {H}^{n - p}\left( F\right)  \oplus  {H}^{p}\left( V\right)  \otimes  {H}^{n - p}\left( F\right) }\right)
\]

\[
{ \oplus  }_{p}{H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

\[
{ \oplus  }_{p}{H}^{p + 1}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

\[
\text{ ↓ }
\]

于是有下列交换图表:

\[
{ \oplus  }_{p}{H}^{p}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right) \;\overset{\psi }{ \rightarrow  }\;{H}^{n}\left( {\left( {U \cup  V}\right)  \times  F}\right)
\]

\[
{ \oplus  }_{p}\left( {{H}^{p}\left( U\right)  \otimes  {H}^{n - p}\left( F\right)  \oplus  {H}^{p}\left( V\right)  \otimes  {H}^{n - p}\left( F\right) }\right) \overset{\psi }{ \rightarrow  }{H}^{n}\left( {U \times  F}\right)  \oplus  {H}^{n}\left( {V \times  F}\right)
\]

\[
{ \oplus  }_{p}{H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

\[
{d}^{ * } \otimes  \mathrm{{id}}
\]

\[
{ \oplus  }_{p}{H}^{p + 1}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

泄单宽达到 \( {150}{\mathrm{\;m}}^{3}/\left( {\mathrm{s} \cdot  \mathrm{m}}\right) \)

从上到下第一与第二个方块的交换性是显然的, 以下验证第三个方块的交换性.

设 \( \left\lbrack  \omega \right\rbrack   \otimes  \left\lbrack  \phi \right\rbrack   \in  {H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right) \) . 则

\[
\psi \left( {{d}^{ * } \otimes  \mathrm{{id}}}\right) \left( {\omega  \otimes  \phi }\right)  = \psi \left( {{d}^{ * }\omega  \otimes  \phi }\right)  = {\pi }^{ * }\left( {{d}^{ * }\omega }\right)  \land  {\rho }^{ * }\phi
\]

\[
{d}^{ * }\psi \left( {\omega  \otimes  \phi }\right)  = {d}^{ * }\left( {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right) .
\]

回忆若 \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) 是从属于 \( \{ U, V\} \) 的一个单位分解,则

\[
{d}^{ * }\omega  = \left\{  \begin{array}{ll}  - d\left( {{\rho }_{V}\omega }\right) & \text{ on }U \\  d\left( {{\rho }_{U}\omega }\right) & \text{ on }V. \end{array}\right.
\]

因为 \( \left\{  {{\pi }^{ * }{\rho }_{U},{\pi }^{ * }{\rho }_{V}}\right\} \) 是从属于 \( \{ U \times  F, V \times  F\} \) 的单位分解,所以在 \( \left( {U \cap  V}\right)  \times  F \) 上,

\[
{d}^{ * }\left( {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right)  = d\left( {\left( {{\pi }^{ * }{\rho }_{U}}\right) \left( {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right) }\right)
\]

\[
= d\left( {{\pi }^{ * }\left( {{\rho }_{U}\omega }\right) }\right)  \land  {\rho }^{ * }\phi
\]

\[
= {\pi }^{ * }d\left( {{\rho }_{U}\omega }\right)  \land  {\rho }^{ * }\phi
\]

\[
= {\pi }^{ * }\left( {{d}^{ * }\omega }\right)  \land  {\rho }^{ * }\phi .
\]

因此 \( \psi {d}^{ * }\left( {\omega  \otimes  \phi }\right)  = {d}^{ * }\psi \left( {\omega  \otimes  \phi }\right) \) ,第三个方块确实可交换.

于是由五引理得到

(*3) 若 Künneth 公式对开集 \( U \) , \( V \) , \( U \cap  V \) 成立, 则它对 \( U \cup  V \) 也成立. 现可对有限好覆盖的开集个数进行归纳证明 Künneth 公式.

Leray-Hirsch 定理

\( M \times  F \) 可看作 \( M \) 上以 \( F \) 为纤维的平凡纤维丛. 在这节要把 Künneth 公式推广到一般纤维丛, 这就是 Leray-Hirsch 定理. 首先介绍一些与纤维丛有关的概念.

定义. 设 \( F \) 是拓扑空间, \( G \) 是拓扑群. \( G \) 对 \( F \) 的一个左作用是指: 任意元 \( g \in  G \) 定义了一个连续同胚 \( g : F \rightarrow  F \) 使得对任意的 \( {g}_{1},{g}_{2} \in  G \) 与 \( v \in  F \) 有

\[
{g}_{1}\left( {{g}_{2}\left( v\right) }\right)  = \left( {{g}_{1}{g}_{2}}\right) \left( v\right) .
\]

\( G \) 对 \( F \) 的作用称为有效的 (effective) 若 \( G \) 中对 \( F \) 平凡作用的元只有单位元,即若 \( g \in  G \) 满足对任意的 \( y \in  F, g\left( y\right)  = y \) ,则 \( g = 1 \in  G \) . 定义. 设 \( G \) 是拓扑群,有效左作用于拓扑空间 \( F \) . 设 \( E, B \) 是拓扑空间, \( \pi  : E \rightarrow  B \) 是连续满射. 设 \( B \) 有开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 满足以下条件:

(1)对每个 \( \alpha  \in  I \) 存在保纤维的同胚

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \triangleq  {\pi }^{-1}\left( {U}_{\alpha }\right)  \rightarrow  {U}_{\alpha } \times  F,
\]

即 \( {\phi }_{\alpha } \) 是同胚且图表

![bo_d7e85t491nqc73eqefm0_128_944_664_551_349_0.jpg](images/fu_algebraic_topology_and_differential_forms_010_bod7e85t491nqc73eqefm01289446645513490.jpg)

是可交换的;

(2)由 \( {\phi }_{\alpha },{\phi }_{\beta } \) 诱导了连续映射 \( {g}_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  G \) 使得

\[
\left( {{\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1}}\right) \left( {x, v}\right)  = \left( {x,{g}_{\alpha \beta }\left( x\right) \left( v\right) }\right) .
\]

则称 \( \pi  : E \rightarrow  B \) 是以 \( F \) 为纤维的纤维丛,它的结构群是 \( G \) ,底空间是 \( B \) ,全空间是 E. \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 称为纤维丛的一个局部平凡化. 对 \( x \in  B,{\pi }^{-1}\left( x\right) \) 称为点 \( x \) 的纤维,记作 \( {E}_{x} \) .

因为 de Rham 理论的范畴是光滑范畴,所以我们假定 \( E \) , \( B \) , \( F \) 是光滑流形, \( G \) 是李群,并且所有的映射包括左作用是光滑的. 因为结构群 \( G \) 的左作用是有效的,所以 \( G \) 是 \( F \) 的微分同胚群 \( \operatorname{Diff}\left( F\right) \) 的子群. 如果不特别提及结构群 \( G \) ,就默认它是 \( \operatorname{Diff}\left( F\right) \) .

习惯上称映射 \( {g}_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  G \) 为纤维丛的转移函数,满足以下 cocycle 条件:

\[
{g}_{\beta \alpha } = {g}_{\alpha \beta }^{-1}\;\text{ on }{U}_{\alpha \beta }
\]

\[
{g}_{\alpha \beta }{g}_{\beta \gamma } = {g}_{\alpha \gamma }\;\text{ on }{U}_{\alpha \beta \gamma }
\]

反之,给定满足 cocycle 条件的 \( {g}_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  G \) ,可构造以 \( \left\{  {g}_{\alpha \beta }\right\} \) 为转移函数的纤维丛 \( E \) :

(5.10)

\[
E = \left( {\mathop{\coprod }\limits_{{\alpha  \in  I}}\left( {{U}_{\alpha } \times  F}\right) }\right) / \sim  .
\]

此处等价关系 \( \sim \) 定义为: 对 \( \left( {x, y}\right)  \in  {U}_{\alpha } \times  F,\left( {{x}^{\prime },{y}^{\prime }}\right)  \in  {U}_{\beta } \times  F \) ,

\[
\left( {x, y}\right)  \sim  \left( {{x}^{\prime },{y}^{\prime }}\right)  \Leftrightarrow  x = {x}^{\prime }, y = {g}_{\alpha \beta }\left( x\right) {y}^{\prime }.
\]

设 \( \pi  : E \rightarrow  M \) 是以 \( F \) 为纤维的光滑纤维丛. 假定 \( E \) 上存在上同调类 \( {e}_{1},\ldots ,{e}_{r} \) , 它们限制在每条纤维 \( {E}_{x} \) 上形成了 \( {H}^{ * }\left( {E}_{x}\right) \) 的一组基. 则可定义映射:

\[
\psi  : {H}^{ * }\left( M\right)  \otimes  \mathbb{R}\left\{  {{e}_{1},\ldots ,{e}_{r}}\right\}   \rightarrow  {H}^{ * }\left( E\right) .
\]

定理 5.11. (Leray-Hirsch) 在上述假定下并假定 \( M \) 具有有限好覆盖,则上述映射 \( \psi \) 是同构,即 \( {H}^{ * }\left( E\right) \) 是 \( {H}^{ * }\left( M\right) \) 上以 \( \left\{  {{e}_{1},\ldots ,{e}_{r}}\right\} \) 为基的自由模,即

\[
{H}^{ * }\left( E\right)  \simeq  {H}^{ * }\left( M\right)  \otimes  \mathbb{R}\left\{  {{e}_{1},\ldots ,{e}_{r}}\right\}   \simeq  {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

证. 设 \( \left\{  {U}_{\alpha }\right\} \) 是 \( M \) 的一个有限好覆盖. 因为 \( {U}_{\alpha } \) 微分同胚于 \( {\mathbb{R}}^{n} \) ,而可缩空间上的纤维丛是平凡的,所以 \( {\left. E\right| }_{{U}_{\alpha }} = {\pi }^{-1}\left( {U}_{\alpha }\right) \) 是平凡的,即存在微分同胚 \( {\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \rightarrow \; {U}_{\alpha } \times  F \) . 所以 \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) 是 \( E \) 的一个局部平凡化.

因为 de Rham 上同调是微分同胚不变量,所以对 \( {\left. E\right| }_{{U}_{\alpha }} \) 的 Leray-Hirsch 定理即为对 \( {U}_{\alpha } \times  F \) 的 Künneth 公式,它是成立的.

用 MV 序列与五引理可证:

(*4) 若 Leray-Hirsch 定理对 \( E{\left| {}_{U}, E\right| }_{V},{\left. E\right| }_{U \cap  V} \) 成立,则它对 \( {\left. E\right| }_{U \cup  V} \) 也成立. 于是可对有限开覆盖的开集个数进行归纳证明.

练习 5.12. (对紧上同调的 Künneth 公式) 这个公式是说对具有有限好覆盖的流形 \( M \) 与 \( N \) ,

\[
{H}_{c}^{ * }\left( {M \times  N}\right)  = {H}_{c}^{ * }\left( M\right)  \otimes  {H}_{c}^{ * }\left( N\right) .
\]

(a) 若 \( M \) , \( N \) 可定向,用 Poincaré 对偶与 de Rham 上同调的 Künneth 公式证明上述公式.

(b) 用 MV 方法证明上述公式.

作业:

1. 练习 5.12.
