#### 第25讲 The Path Fibration

代数拓扑与微分形式 §16 The Path Fibration

25. 道路纤维化我们继续在拓扑空间与连续映射的范畴研究. 除非另作说明, 此处所有的映射是连续映射, 所有的上同调是整系数上同调.

设 \( \pi  : E \rightarrow  X \) 是拓扑空间 \( X \) 上以 \( F \) 为纤维的纤维丛, \( \mathcal{U} \) 是 \( X \) 的好覆盖. 则存在收敛于全空间 \( E \) 的上同调 \( {H}^{ * }\left( E\right) \) 的谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) ，它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( F\right) }\right) ,
\]

其中 \( {\mathcal{H}}^{q}\left( F\right) \) 是 \( \mathcal{U} \) 上局部常值预层: 对任意的 \( U \in  \operatorname{Open}\mathcal{U} \) ,

\[
{\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{q}\left( F\right) .
\]

现假定 \( \pi  : E \rightarrow  X \) 仅是一个映射,不必有局部平凡化. 根据 Leray 构造,通过考虑 \( E \) 上奇异上链的双复形 \( K = {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{S}^{ * }}\right) \) 仍能得到谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) ,它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right)
\]

其中 \( {\mathcal{H}}^{q} \) 是好覆盖 \( \mathcal{U} \) 上预层: \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) ,它不一定是局部常值预层. 现假定 \( \pi  : E \rightarrow  X \) 具有性质:

## (16.1) 对某个固定空间 \( F \) 与对 \( X \) 的任意可缩开集 \( U,{H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{q}\left( F\right) \) .

此时 \( {\mathcal{H}}^{q} \) 是好覆盖 \( \mathcal{U} \) 上局部常值预层. 所以 \( {E}_{2} = {H}_{\delta }{H}_{d}\left( K\right) \) 与对纤维丛的情形完全相同. 因为谱序列是从 \( {H}_{\delta }{H}_{d} \) 到 \( {H}_{D} \simeq  {H}^{ * }\left( E\right) \) 的一种纯代数方法,所以这个双复形的谱序列又将收敛于 \( {H}^{ * }\left( E\right) \) .

今天要讲的道路纤维化就是这样一个例子. 在接下来的几节我们将看到 Serre 当初出人意料地应用谱序列到道路纤维化，在同伦论中取得了影响深远的成就.

- 道路纤维化

- \( {H}^{ * }\left( {\Omega {S}^{n}}\right) \) 的计算

- \( {H}^{ * }\left( {\Omega {S}^{n}}\right) \) 的环结构

道路纤维化

设 \( X \) 是道路连通空间，* 是基点; \( I = \left\lbrack  {0,1}\right\rbrack \) 是单位区间，0 是基点. \( X \) 的道路空间 \( {PX} \) 是由 \( X \) 中所有以 \( * \) 为始点的道路组成的:

\[
{PX} = \{ \text{ 映射 }\mu  : I \rightarrow  X \mid  \mu \left( 0\right)  =  * \} .
\]

赋予 \( {PX} \) 紧开拓扑如下. 对 \( I \) 的每个紧集 \( K \) 与 \( X \) 的每个开集 \( U \) ,令

\[
V\left( {K, U}\right)  = \{ \mu  \in  {PX} \mid  \mu \left( K\right)  \subset  U\} .
\]

所有这种 \( V\left( {K, U}\right) \) 组成 \( {PX} \) 的紧开拓扑的子基,即拓扑基是此子基的所有有限交. 在此拓扑下，自然投射

\[
\pi  : {PX} \rightarrow  X,\;\pi \left( \mu \right)  = \mu \left( 1\right)
\]

是连续的. 它在点 \( p \) 的纤维是所有从 \( * \) 到 \( p \) 的道路组成的. 特别地, 基点 * 的纤维是

\[
{\pi }^{-1}\left( *\right)  = \{ \mu  : I \rightarrow  X \mid  \mu \left( 0\right)  =  *  = \mu \left( 1\right) \} ,
\]

![bo_d7e85t491nqc73eqefm0_588_884_1253_530_459_0.jpg](images/fu_algebraic_topology_and_differential_forms_168_bod7e85t491nqc73eqefm058888412535304590.jpg)

即它是 \( X \) 的以 * 为基点的圈空间 (loop space) \( {\Omega X} \) .

引理. 自然投射 \( \pi  : {PX} \rightarrow  X \) 具有性质 (16.1). 事实上,对 \( X \) 的任意可缩开集 \( U \) ,

\[
{H}^{ * }\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{ * }\left( {\Omega X}\right)
\]

证. 设 \( U \) 是 \( X \) 的可缩开集. 给定 \( p \in  U \) ,设 \( i : {\pi }^{-1}\left( p\right)  \subset  {\pi }^{-1}\left( U\right) \) 是包含映射.

![bo_d7e85t491nqc73eqefm0_589_871_901_552_510_0.jpg](images/fu_algebraic_topology_and_differential_forms_169_bod7e85t491nqc73eqefm05898719015525100.jpg)

应用 \( U \) 到点 \( p \) 的收缩,可定义 \( i \) 的同伦逆

\[
\phi  : {\pi }^{-1}\left( U\right)  \rightarrow  {\pi }^{-1}\left( p\right) .
\]

事实上,对 \( \sigma  \in  {\pi }^{-1}\left( U\right) , U \) 到 \( p \) 的一个收缩定义了一条从 \( \sigma \left( 1\right) \) 到 \( p \) 的道路 \( {\tau }_{\sigma \left( 1\right) } \) , 从而定义

\[
\phi \left( \sigma \right)  = {\tau }_{\sigma \left( 1\right) } \circ  \sigma .
\]

![bo_d7e85t491nqc73eqefm0_590_812_614_700_436_0.jpg](images/fu_algebraic_topology_and_differential_forms_170_bod7e85t491nqc73eqefm05908126147004360.jpg)

容易验证 \( \phi \) 与 \( i \) 互为同伦逆:

\[
\phi  \circ  i = \mathrm{{id}} : {\pi }^{-1}\left( p\right)  \rightarrow  {\pi }^{-1}\left( p\right)
\]

\[
i \circ  \phi  \simeq  \mathrm{{id}} : {\pi }^{-1}\left( U\right)  \rightarrow  {\pi }^{-1}\left( U\right)
\]

此处同伦过程为曲线 \( {\tau }_{\sigma \left( 1\right) } \) 收缩成点 \( \sigma \left( 1\right) \) 的过程:

![bo_d7e85t491nqc73eqefm0_591_231_393_1843_424_0.jpg](images/fu_algebraic_topology_and_differential_forms_171_bod7e85t491nqc73eqefm059123139318434240.jpg)

所以 \( {\pi }^{-1}\left( U\right) \) 与 \( {\pi }^{-1}\left( p\right) \) 有相同的伦型.

另一方面,对 \( X \) 中任意两点 \( p, q \) ,从 \( p \) 到 \( q \) 的一条固定道路诱导了同伦等价 \( {\pi }^{-1}\left( p\right)  \simeq  {\pi }^{-1}\left( q\right) \) . 所以每条纤维 \( {\pi }^{-1}\left( p\right) \) 与 \( {\pi }^{-1}\left( *\right)  = {\Omega X} \) 有相同的伦型.

综上所述, \( {\pi }^{-1}\left( U\right) \) 与 \( {\pi }^{-1}\left( *\right)  = {\Omega X} \) 有相同的伦型. 所以

\[
{H}^{ * }\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{ * }\left( {\Omega X}\right)
\]

一类满足 (16.1) 的更一般的映射是纤维化 (fiberings, fibrations) . 满射 \( \pi \) : \( E \rightarrow  X \) 称为纤维化若它满足以下的覆盖同伦性质:(16.2)对给定的映射 \( f : Y \rightarrow  E \) 与映射 \( \bar{f} = \pi  \circ  f \) 在 \( X \) 中的一个同伦 \( {\bar{f}}_{t} \) ， 存在 \( f \) 在 \( E \) 中的同伦 \( {f}_{t} \) 使得 \( \pi  \circ  {f}_{t} = {\bar{f}}_{t} \) ，即它覆盖 \( {\bar{f}}_{t} \) .

![bo_d7e85t491nqc73eqefm0_592_752_750_820_492_0.jpg](images/fu_algebraic_topology_and_differential_forms_172_bod7e85t491nqc73eqefm05927527508204920.jpg)

若 \( X \) 带有基点 \( * \) ,我们称 \( {\pi }^{-1}\left( *\right) \) 为纤维化的纤维. 对任意 \( x \in  X \) ,我们称 \( {F}_{x} = {\pi }^{-1}\left( x\right) \) 为点 \( x \) 上纤维. 引理. 自然映射 \( \pi  : {PX} \rightarrow  X \) 为纤维化, \( {\Omega X} \) 是它的纤维.

证. 给定映射 \( f : Y \rightarrow  {PX} \) 与 \( \bar{f} = \pi  \circ  f \) 在 \( X \) 中一个同伦 \( {\bar{f}}_{t} \) . 对任意 \( y \in  Y \) , \( f\left( y\right)  \in  {PX} \) 表示 \( X \) 中一条从 * 出发的道路 \( \sigma \) . 所以

\[
{\bar{f}}_{0}\left( y\right)  = \pi \left( {f\left( y\right) }\right)  = \pi \left( \sigma \right)  = \sigma \left( 1\right) .
\]

而 \( {\bar{f}}_{t}\left( y\right) \) 是 \( {\bar{f}}_{0}\left( y\right) \) 在 \( X \) 中的一个同伦,它定义了 \( X \) 上一条从 \( {\bar{f}}_{0}\left( y\right)  = \sigma \left( 1\right) \) 到 \( {\bar{f}}_{1}\left( y\right) \) 的道路 \( {\tau }_{y} \) .

于是对给定的 \( y \in  Y \) 与 \( t \in  \left\lbrack  {0,1}\right\rbrack \) ,定义 \( {f}_{t}\left( y\right) \) 为一条从 * 出发沿着 \( \sigma \) 走到 \( {\bar{f}}_{0}\left( y\right) \) , 再沿着 \( {\tau }_{y} \) 走到 \( {\bar{f}}_{t}\left( y\right) \) 的道路. 显然 \( {f}_{t} \) 是 \( f \) 在 \( {PX} \) 中一个同伦且

\[
\pi  \circ  {f}_{t}\left( y\right)  = {\bar{f}}_{t}\left( y\right) .
\]

![bo_d7e85t491nqc73eqefm0_594_701_278_1013_929_0.jpg](images/fu_algebraic_topology_and_differential_forms_173_bod7e85t491nqc73eqefm059470127810139290.jpg)

纤维化 \( \pi  : {PX} \rightarrow  X \) 称为拓扑空间 \( X \) 的道路纤维化. 它在圈空间 \( {\Omega X} \) 的上同调计算中是基本的. 它的全空间 \( {PX} \) 是可缩空间,因为任何一条道路可沿着自己收缩到常值道路 \( \sigma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow   * \) ,这是 \( {PX} \) 的基点. 纤维化具有以下两个基本性质, 由此得到它具有性质 (16.1).

引理 16.3. (a) 道路连通空间上一个纤维化的任意两条纤维有相同的伦型.

(b) 每个可缩开集 \( U \) 的逆像 \( {\pi }^{-1}\left( U\right) \) 与 \( U \) 中每点 \( a \) 的纤维 \( {F}_{a} \) 有相同的伦型.

证. 略.

命题 16.5. 设 \( \pi  : E \rightarrow  X \) 是纤维化, \( X \) 是单连通的且 \( E \) 是道路连通的. 则纤维也是道路连通的.

证. 应用谱序列于纤维化. 显然 \( {E}_{2}^{0,0} = {E}_{\infty }^{0,0} \) . 所以 \( {E}_{2}^{0,0} = {H}^{0}\left( E\right)  = \mathbb{Z} \) . 另一方面,由于纤维化满足条件 (16.1) 并且 \( X \) 是单连通的,所以由对奇异上同调的 Leray 定理,

\[
{E}_{2}^{0,0} = {H}^{0}\left( {X,{H}^{0}\left( F\right) }\right)  = {H}^{0}\left( F\right) .
\]

因此 \( {H}^{0}\left( F\right)  = \mathbb{Z}, F \) 道路连通.

\( {H}^{ * }\left( {\Omega {S}^{n}}\right) \) 的计算

作为道路纤维化的谱序列的应用,我们计算 \( {S}^{n} \) 的圈空间 \( \Omega {S}^{n} \) 当 \( n \geq  2 \) 时的整上同调群.

由于 \( {S}^{n} \) 当 \( n \geq  2 \) 时是单连通的,根据对奇异上同调的 Leray 定理,道路纤维化

![bo_d7e85t491nqc73eqefm0_596_981_732_361_279_0.jpg](images/fu_algebraic_topology_and_differential_forms_174_bod7e85t491nqc73eqefm05969817323612790.jpg)

的谱序列的 \( {E}_{2} \) 页为

\[
{E}_{2}^{p, q} = {H}^{p}\left( {{S}^{n},{H}^{q}\left( {\Omega {S}^{n}}\right) }\right) .
\]

所以第 0 列

\[
{E}_{2}^{0, q} = {H}^{0}\left( {{S}^{n},{H}^{q}\left( {\Omega {S}^{n}}\right) }\right)  = {H}^{q}\left( {\Omega {S}^{n}}\right)
\]

是纤维的上同调.

由命题 \( {16.5},{H}^{0}\left( {\Omega {S}^{n}}\right)  = \mathbb{Z} \) ,所以底部一行

\[
{E}_{2}^{p,0} = {H}^{p}\left( {{S}^{n},{H}^{0}\left( {\Omega {S}^{n}}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & p = 0, n \\  0 & p \neq  0, n \end{array}\right.
\]

是 \( {S}^{n} \) 的上同调.

![bo_d7e85t491nqc73eqefm0_597_691_581_980_547_0.jpg](images/fu_algebraic_topology_and_differential_forms_175_bod7e85t491nqc73eqefm05976915819805470.jpg)

因为 \( {H}_{p - 1}\left( {S}^{n}\right)  = \mathbb{Z} \) 或 0,由泛系数定理 (15.14) 可得

\[
{E}_{2}^{p, q} = {H}^{p}\left( {{S}^{n};{H}^{q}\left( {\Omega {S}^{n}}\right) }\right)
\]

\[
= \operatorname{Hom}\left( {{H}_{p}\left( {S}^{n}\right) ,{H}^{q}\left( {\Omega {S}^{n}}\right) }\right)  \oplus  \operatorname{Ext}\left( {{H}_{p - 1}\left( {S}^{n}\right) ,{H}^{q}\left( {\Omega {S}^{n}}\right) }\right)
\]

\[
= \operatorname{Hom}\left( {{H}_{p}\left( {S}^{n}\right) ,{H}^{q}\left( {\Omega {S}^{n}}\right) }\right) .
\]

所以 \( {E}_{2} \) 除了 \( p = 0, n \) 之外的所有列全为零. 因此当 \( r \neq  n \) 时, \( {d}_{r} = 0 \) ,

\[
{E}_{2} = \cdots  = {E}_{n},\;{E}_{n + 1} = {E}_{\infty } \simeq  {H}^{ * }\left( {P{S}^{n}}\right) .
\]

因为道路空间 \( P{S}^{n} \) 是可缩的，所以

\[
{E}_{\infty }^{p, q} = \left\{  \begin{array}{ll} \mathbb{Z} & \left( {p, q}\right)  = \left( {0,0}\right) \\  0 & \left( {p, q}\right)  \neq  \left( {0,0}\right) . \end{array}\right.
\]

为了杀掉 \( {E}_{n}^{n,0} = {E}_{2}^{n,0} = \mathbb{Z} \) ,

\[
{d}_{n} : {E}_{n}^{0, n - 1} \rightarrow  {E}_{n}^{n,0}
\]

必须是同构. 所以 \( {E}_{n}^{0, n - 1} = \mathbb{Z} \) . 于是

\[
{E}_{n}^{n, n - 1} = {E}_{2}^{n, n - 1} = {H}^{n}\left( {{S}^{n},{H}^{n - 1}\left( {\Omega {S}^{n}}\right) }\right)  = {H}^{n}\left( {{S}^{n},\mathbb{Z}}\right)  = \mathbb{Z}.
\]

为了杀掉此 \( \mathbb{Z} \) ,

\[
{d}_{n} : {E}_{n}^{0,2\left( {n - 1}\right) } \rightarrow  {E}_{n}^{n, n - 1}
\]

必须是同构,所以 \( {E}_{n}^{0,2\left( {n - 1}\right) } = \mathbb{Z} \) . 于是 \( {E}_{n}^{n,2\left( {n - 1}\right) } = \mathbb{Z} \) . 如此下去,可得当 \( k \geq  1 \) 时, \( {E}_{n}^{0, k\left( {n - 1}\right) } = \mathbb{Z} \) .

![bo_d7e85t491nqc73eqefm0_599_711_196_895_631_0.jpg](images/fu_algebraic_topology_and_differential_forms_176_bod7e85t491nqc73eqefm05997111968956310.jpg)

另一方面,其余的 \( {E}_{n}^{0, q} \) 必须为零,因为它不可能被杀掉. 所以

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0, n - 1,2\left( {n - 1}\right) ,\ldots \\  0 & \text{ 其余情况 } \end{array}\right.
\]

例 16.6. (2-球面) 对 \( q \geq  0,{H}^{q}\left( {\Omega {S}^{2}}\right)  = \mathbb{Z} \) .

例 16.7. (3-球面)

\[
{H}^{q}\left( {\Omega {S}^{3}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & q = {2n} \geq  0 \\  0 & \text{ 其余情况. } \end{array}\right.
\]

我们先看 \( n = 2 \) 的情形.

设 \( u \in  {E}_{2}^{2,0} = {H}^{2}\left( {S}^{2}\right) \) 是一个生成元, \( x \in  {E}_{2}^{0,1} = {H}^{1}\left( {\Omega {S}^{2}}\right) \) 是一个生成元使得

\[
{d}_{2}\left( x\right)  = u
\]

因为 \( {E}_{2}^{p, q} = {H}^{q}\left( {\Omega {S}^{2}}\right)  \otimes  {H}^{p}\left( {S}^{2}\right) \) 具有环结构 “.”,所以

\[
\left( {x \otimes  1}\right)  \cdot  \left( {1 \otimes  u}\right)  \in  {E}_{2}^{2,1}
\]

是生成元. 将它简记为 \( x \cdot  u \) . 显然 \( x \cdot  u = u \cdot  x \) . 由于在 \( {H}^{ * }\left( {\Omega {S}^{2}}\right) \) 上已定义了环结构“.”，所以

\[
{x}^{2} = x \cdot  x \in  {E}_{2}^{0,2} = {H}^{2}\left( {\Omega {S}^{2}}\right) .
\]

又因为

\[
{d}_{2}\left( {x}^{2}\right)  = {d}_{2}x \cdot  x - x \cdot  {d}_{2}x = u \cdot  x - x \cdot  u = 0
\]

且 \( {d}_{2} \) 是同构,所以 \( {x}^{2} = 0 \) .

![bo_d7e85t491nqc73eqefm0_601_723_232_932_709_0.jpg](images/fu_algebraic_topology_and_differential_forms_177_bod7e85t491nqc73eqefm06017232329327090.jpg)

需在 \( {H}^{2}\left( {\Omega {S}^{2}}\right) \) 上引进一个与 \( x \) 无关的生成元 \( e \) 使得

\[
{d}_{2}\left( e\right)  = {xu}.
\]

现 \( e \cdot  u \in  {E}_{2}^{2,2} \) 是一个生成元,且

\[
{d}_{2}\left( {e \cdot  x}\right)  = {d}_{2}e \cdot  x + e \cdot  {d}_{2}x = x \cdot  u \cdot  x + e \cdot  u = e \cdot  u.
\]

由于 \( {d}_{2} \) 是同构,所以 \( e \cdot  x \in  {E}_{2}^{0,3} = {H}^{3}\left( {\Omega {S}^{2}}\right) \) 是生成元. 于是 \( e \cdot  x \cdot  u \in  {E}_{2}^{2,3} \) 是一个生成元.

因为

\[
{d}_{2}\left( {e}^{2}\right)  = {2e}{d}_{2}\left( e\right)  = {2e} \cdot  x \cdot  u,
\]

所以 \( {e}^{2}/2 \) 是 \( {E}_{2}^{0,4} = {H}^{4}\left( {\Omega {S}^{2}}\right) \) 的一个生成元. 应用归纳法我们证明断言. \( \frac{{e}^{k}}{k!} \) 是 \( {H}^{2k}\left( {\Omega {S}^{2}}\right) \) 的生成元, \( \frac{{e}^{k} \cdot  x}{k!} \) 是 \( {H}^{{2k} + 1}\left( {\Omega {S}^{2}}\right) \) 的生成元. 证. 假定断言对 \( \left( {k - 1}\right) \) 成立. 因为

\[
{d}_{2}\left( \frac{{e}^{k}}{k!}\right)  = \frac{{e}^{k - 1}}{\left( {k - 1}\right) !}{d}_{2}e = \frac{{e}^{k - 1} \cdot  x \cdot  u}{\left( {k - 1}\right) !}
\]

是 \( {E}_{2}^{2,{2k} - 1} \) 的一个生成元,所以 \( \frac{{e}^{k}}{k!} \) 是 \( {E}_{2}^{0,{2k}} = {H}^{2k}\left( {\Omega {S}^{2}}\right) \) 的一个生成元. 又因为

\[
{d}_{2}\left( \frac{{e}^{k} \cdot  x}{k!}\right)  = \frac{{e}^{k - 1} \cdot  x \cdot  u \cdot  x}{\left( {k - 1}\right) !} + \frac{{e}^{k} \cdot  u}{k!} = \frac{{e}^{k} \cdot  u}{k!}
\]

是 \( {E}_{2}^{2,{2k}} \) 的一个生成元,所以 \( \frac{{e}^{k} \cdot  x}{k!} \) 是 \( {H}^{{2k} + 1}\left( {\Omega {S}^{2}}\right) \) 的生成元.

定义. 外代数 \( E\left( x\right) \) 是环 \( \mathbb{Z}\left\lbrack  x\right\rbrack  /\left( {x}^{2}\right) \) . 以 \( e \) 为生成元的分次多项式代数 \( {Z}_{\gamma }\left( e\right) \) 是以 \( \left\{  {1, e,{e}^{2}/2!,{e}^{3}/3!,\ldots }\right\} \) 为加法基的 \( \mathbb{Z} \) -代数:

\[
{Z}_{\gamma }\left( e\right)  = {\operatorname{span}}_{\mathbb{Z}}\left\{  {1, e,{e}^{2}/2!,{e}^{3}/3!,\ldots }\right\}  .
\]

在上述定义下, 我们可把断言概括为

\[
{H}^{ * }\left( {\Omega {S}^{2}}\right)  = E\left( x\right) { \otimes  }_{\mathbb{Z}}{Z}_{\gamma }\left( e\right) ,\;\dim x = 1,\;\dim e = 2.
\]

类似于 \( {H}^{ * }\left( {\Omega {S}^{2}}\right) \) 的讨论，我们得到若 \( n \) 为偶数，则

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = E\left( x\right) { \otimes  }_{\mathbb{Z}}{Z}_{\gamma }\left( e\right) ,\;\dim x = n - 1,\;\dim e = 2\left( {n - 1}\right) .
\]

考虑 \( n \) 为奇数的情形. 设 \( u \) 是 \( {H}^{n}\left( {S}^{n}\right) \) 的生成元, \( e \) 是 \( {H}^{n - 1}\left( {\Omega {S}^{n}}\right) \) 的生成元使得

\[
{d}_{n}\left( e\right)  = u
\]

因为 \( {eu} \) 是 \( {H}^{n}\left( {S}^{n}\right)  \otimes  {H}^{n - 1}\left( {\Omega {S}^{n}}\right) \) 的生成元并且 \( {d}_{n}\left( {e}^{2}\right)  = {2eu} \) ,所以 \( {e}^{2}/2 \) 是 \( {H}^{2\left( {n - 1}\right) }\left( {\Omega {S}^{n}}\right) \) 的生成元. 一般地若 \( {e}^{k}/k! \) 是 \( {H}^{k\left( {n - 1}\right) }\left( {\Omega {S}^{n}}\right) \) 的生成元,则

\[
{d}_{n}\left( {{e}^{k + 1}/\left( {k + 1}\right) !}\right)  = \left( {{e}^{k}/k!}\right) u
\]

所以 \( {e}^{k + 1}/\left( {k + 1}\right) ! \) 是 \( {H}^{\left( {k + 1}\right) \left( {n - 1}\right) }\left( {\Omega {S}^{n}}\right) \) 的生成元. 这就证明了对奇数 \( n \) ,

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = {Z}_{\gamma }\left( e\right) ,\;\dim e = n - 1.
\]

![bo_d7e85t491nqc73eqefm0_604_715_985_919_737_0.jpg](images/fu_algebraic_topology_and_differential_forms_178_bod7e85t491nqc73eqefm06047159859197370.jpg)

作业:

代数拓扑与微分形式
