#### 第28讲 Applications to Homotopy Theory (1)

§18. Applications to Homotopy Theory (1)

28. EM 空间

Leray 谱序列是计算纤维化的同调与上同调的基本工具. 根据定义, Eilenberg-MacLane (EM) 空间 \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) 是第 \( n \) 个同伦群为 \( {\pi }_{q}\left( X\right) \) ,而其余(大于零的)维数的同伦群为零的道路连通空间. 由 Hurewicz 同构定理, \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \; \left( {n \geq  2}\right) \) 的第一个非零同调是 \( {\pi }_{q}\left( X\right) \) . 所以如能把 \( \mathrm{{EM}} \) 空间 \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) 作为纤维化的纤维, 就有可能用谱序列计算同伦群. Postnikov 逼近与 Whitehead 塔提供了这种纤维化, 它们是 EM 空间的扭积, 在某种程度上同伦逼近给定的空间. 作为例子我们在这节计算 \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) .

这次课主要讲 EM 空间的定义与通过套叠构造得到许多有用的 EM 空间. 下次课讲 \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算,为此先讲 EM 空间 \( K\left( {\mathbb{Z},3}\right) \) 的上同调的计算. 我们把 Postnikov 逼近与 Whitehead 塔这两种技巧揉合在 \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算中.

- Eilenberg-MacLane 空间

- 套叠构造

The Leray spectral sequence is basically a tool for computing the homology or cohomology of a fibration. However, since by the Hurewicz isomorphism theorem, the first nontrivial homology of the Eilenberg-MacLane space \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) is \( {\pi }_{q}\left( X\right) \) , if one can fit the Eilenberg-MacLane space \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) into a fibering, it may be possible to apply the spectral sequence to compute the homotopy groups. Such fiberings are provided by the Postnikov approximation and the Whitehead tower, two twisted products of Eilenberg-MacLane spaces which in some way approximate a given space in homotopy. As examples of how this works, we compute in this section \( {\pi }_{4}\left( {S}^{3}\right) \) and \( {\pi }_{5}\left( {S}^{3}\right) \) .

Eilenberg-MacLane 空间

定义. 设 \( A \) 是一个群. 道路连通空间 \( Y \) 是一个 Eilenberg-MacLane (EM) 空间 \( K\left( {A, n}\right) \) 若

\[
{\pi }_{q}\left( Y\right)  = \left\{  \begin{array}{ll} A & q = n \\  0 & q \neq  n. \end{array}\right.
\]

除非另作说明,我们不考虑 \( {\pi }_{0} \) . 当 \( n > 1 \) 时自动要求 \( A \) 是 abel 群. 对任意群 \( A \) 与任意整数 \( n \geq  1 \) ，这种空间在 CW 复形的范畴中存在并且在同伦等价的意义下是唯一的. 所以如果仅考虑 CW 复形,记号 \( K\left( {A, n}\right) \) 是不会引起歧义的.

例 18.1. (a) 考虑覆盖空间

\[
\pi  : {\mathbb{R}}^{1} \rightarrow  {S}^{1} \subset  \mathbb{C},\;\pi \left( x\right)  = {e}^{2\pi ix}.
\]

它是具有离散纤维的纤维化. 根据纤维化的正合同伦序列知,对 \( q \geq  2 \) 有

\[
{\pi }_{q}\left( {S}^{1}\right)  = {\pi }_{q}\left( {\mathbb{R}}^{1}\right)  = 0
\]

又因为 \( {\pi }_{1}\left( {S}^{1}\right)  = \mathbb{Z} \) ,所以 \( {S}^{1} \) 是 \( K\left( {\mathbb{Z},1}\right) \) .

(b) 若 \( F \) 是自由群,则 \( K\left( {F,1}\right) \) 是一束 \( {S}^{1} \) ,每个 \( {S}^{1} \) 对应一个生成元.

![bo_d7e85t491nqc73eqefm0_662_971_199_415_444_0.jpg](images/fu_algebraic_topology_and_differential_forms_210_bod7e85t491nqc73eqefm06629711994154440.jpg)

(c) 设 \( S \) 是亏格 \( g \geq  1 \) 的黎曼面. 它的基本群 \( \pi \) 有 \( {2g} \) 个生成元 \( {a}_{1},{b}_{1},\ldots ,{a}_{g},{b}_{g} \) 且满足关系式

\[
{a}_{1}{b}_{1}{a}_{1}^{-1}{b}_{1}^{-1}\ldots {a}_{g}{b}_{g}{a}_{g}^{-1}{b}_{g}^{-1} = 1.
\]

根据复变函数论的单值化定理, 亏格 \( g \geq  1 \) 的黎曼面的万有覆盖空间是可缩的. 由纤维化的正合同伦序列知对 \( q \geq  2,{\pi }_{q}\left( S\right)  = 0 \) . 因此黎曼面 \( S \) 是 EM 空间 \( K\left( {\pi ,1}\right) \) .

![bo_d7e85t491nqc73eqefm0_662_437_1336_750_242_0.jpg](images/fu_algebraic_topology_and_differential_forms_209_bod7e85t491nqc73eqefm066243713367502420.jpg)

![bo_d7e85t491nqc73eqefm0_662_1355_1203_485_524_0.jpg](images/fu_algebraic_topology_and_differential_forms_208_bod7e85t491nqc73eqefm0662135512034855240.jpg)

(d) \( {\Omega K}\left( {A, n}\right)  = K\left( {A, n - 1}\right) \) . 这是因为根据命题 17.2 有

\[
{\pi }_{q}\left( {{\Omega K}\left( {A, n}\right) }\right)  = {\pi }_{q + 1}\left( {K\left( {A, n}\right) }\right)  = \left\{  \begin{array}{ll} A & q = n - 1 \\  0 & q \neq  n - 1. \end{array}\right.
\]

(e) 因为 \( {\pi }_{q}\left( {S}^{n}\right)  = 0 \) 对 \( 1 \leq  q \leq  n - 1 \) 且 \( {\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z} \) ,所以通过杀掉 \( {S}^{n} \) 的所有 \( q > n \) 的 \( {\pi }_{q}\left( {S}^{n}\right) \) 我们可构造 EM 空间 \( K\left( {\mathbb{Z}, n}\right) \) . 杀掉同伦群的方法将在 Postnikov 逼近这节讨论.

(f) 若 \( A, B \) 是两个群,则

\[
K\left( {A, n}\right)  \times  K\left( {B, n}\right)  = K\left( {A \times  B, n}\right) .
\]

这是因为根据同伦群的性质 (17.1.a) 有

\[
{\pi }_{q}\left( {K\left( {A, n}\right)  \times  K\left( {B, n}\right) }\right)  = {\pi }_{q}\left( {K\left( {A, n}\right) }\right)  \times  {\pi }_{q}\left( {K\left( {B, n}\right) }\right)
\]

\[
= \left\{  \begin{array}{ll} A \times  B & q = n \\  0 & q \neq  n \end{array}\right.
\]

套叠构造

这节给出构造某种 EM 空间的技巧, 它称为套叠 (telescoping) 构造. 现举例说明.

例 18.2.(无穷射影空间)实射影空间 \( \mathbb{R}{P}^{n} \) 是球面 \( {S}^{n} \) 通过等同 \( {S}^{n} \) 的对径点得到的商空间. 由包含序列

\[
{\mathbb{R}}^{1} \rightarrow  {\mathbb{R}}^{2} \rightarrow  {\mathbb{R}}^{3} \rightarrow  \cdots  \rightarrow  {\mathbb{R}}^{n + 1} \rightarrow  {\mathbb{R}}^{n + 2} \rightarrow  \cdots
\]

诱导了包含序列

\[
{S}^{0} \rightarrow  {S}^{1} \rightarrow  {S}^{2} \rightarrow  \cdots  \rightarrow  {S}^{n} \rightarrow  {S}^{n + 1} \rightarrow  \cdots ,
\]

从而诱导了自然包含序列

\[
\mathbb{R}{P}^{0}\overset{i}{ \rightarrow  }\mathbb{R}{P}^{1}\overset{i}{ \rightarrow  }\mathbb{R}{P}^{2}\overset{i}{ \rightarrow  }\cdots \overset{i}{ \rightarrow  }\mathbb{R}{P}^{n}\overset{i}{ \rightarrow  }\mathbb{R}{P}^{n + 1} \rightarrow  \cdots
\]

定义无穷实射影空间 \( \mathbb{R}{P}^{\infty } \) 为

\[
\mathbb{R}{P}^{\infty } = \left( {\mathop{\coprod }\limits_{{n \geq  0}}\mathbb{R}{P}^{n} \times  I}\right) /\left( {x,1}\right)  \sim  \left( {i\left( x\right) ,0}\right) ,
\]

即借助上述自然包含把所有有限维实射影空间粘合在一起. \( \mathbb{R}{P}^{\infty } \) 直观上看起来像一个无穷望远镜. 断言. 对 \( q > 1,{\pi }_{q}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) . 证. 因为 \( {S}^{n} \rightarrow  \mathbb{R}{P}^{n} \) 是二重覆盖,由纤维化的正合同伦序列知对 \( 1 < q < n \) , \( {\pi }_{q}\left( {\mathbb{R}{P}^{n}}\right)  = {\pi }_{q}\left( {S}^{n}\right)  = 0 \) . 现证对 \( q > 1,{\pi }_{q}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) . 我们以 \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) 为例. 假定 \( f : {S}^{15} \rightarrow  \mathbb{R}{P}^{\infty } \) 表示 \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right) \) 的一个元. 因为 \( f\left( {S}^{15}\right) \) 是紧的, 它必落在有限多个 \( \mathbb{R}{P}^{i} \times  I \) 的并中. 因为每个 \( \mathbb{R}{P}^{i} \) 可通过 \( I \) 滑到 \( \mathbb{R}{P}^{i + 1} \) 中， 我们能把 \( f\left( {S}^{15}\right) \) 滑进一个维数较高 (n > 15) 的 \( \mathbb{R}{P}^{n} \) 中,也就是说 \( f \) 与某个 \( {f}^{\prime } : {S}^{15} \rightarrow  \mathbb{R}{P}^{n} \) 同伦. 但是因为当 \( n > {15} \) 时, \( {\pi }_{15}\left( {\mathbb{R}{P}^{n}}\right)  = 0 \) ,所以 \( {f}^{\prime } \) 从而 \( f \) 零伦. 因此 \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) . 通过把球面的像滑进一个维数足够高的射影空间,我们明白这个套叠杀掉所有的高维同伦群. 应用套叠构造于球面的序列

\[
{S}^{0}\overset{i}{ \rightarrow  }{S}^{1}\overset{i}{ \rightarrow  }{S}^{2}\overset{i}{ \rightarrow  }\ldots \overset{i}{ \rightarrow  }{S}^{n}\overset{i}{ \rightarrow  }{S}^{n + 1}\overset{i}{ \rightarrow  }\ldots
\]

![bo_d7e85t491nqc73eqefm0_665_208_899_1824_565_0.jpg](images/fu_algebraic_topology_and_differential_forms_211_bod7e85t491nqc73eqefm066520889918245650.jpg)

![bo_d7e85t491nqc73eqefm0_666_488_998_1268_638_0.jpg](images/fu_algebraic_topology_and_differential_forms_212_bod7e85t491nqc73eqefm066648899812686380.jpg)

得到无穷球面

\[
{S}^{\infty } = \left( {\mathop{\coprod }\limits_{{n \geq  0}}{S}^{n} \times  I}\right) /\left( {x,1}\right)  \sim  \left( {i\left( x\right) ,0}\right) .
\]

它是 \( \mathbb{R}{P}^{\infty } \) 的二重覆盖. 同理可证对 \( q \geq  1,{\pi }_{q}\left( {S}^{\infty }\right)  = 0 \) .

断言. \( {\pi }_{1}\left( {\mathbb{R}{P}^{\infty }}\right)  = {\mathbb{Z}}_{2} \) .

证. 由纤维化的正合同伦序列

\[
\ldots {\pi }_{1}\left( {S}^{\infty }\right)  \rightarrow  {\pi }_{1}\left( {\mathbb{R}{P}^{\infty }}\right)  \rightarrow  {\pi }_{0}\left( {\{ \cdot , \cdot  \} }\right)  \rightarrow  {\pi }_{0}\left( {S}^{\infty }\right)  \rightarrow  {\pi }_{0}\left( {\mathbb{R}{P}^{\infty }}\right)  \rightarrow  0
\]

0 \( \{  \cdot  \} \)

知 \( {\pi }_{1}\left( {\mathbb{R}{P}^{\infty }}\right) \) 是由两个元组成的群,即 \( {\mathbb{Z}}_{2} \) .

上述两个断言表明 \( \mathbb{R}{P}^{\infty } \) 是 EM 空间 \( K\left( {{\mathbb{Z}}_{2},1}\right) \) .

例18.3.(无穷复射影空间)应用套叠构造到序列

![bo_d7e85t491nqc73eqefm0_668_727_222_867_311_0.jpg](images/fu_algebraic_topology_and_differential_forms_213_bod7e85t491nqc73eqefm06687272228673110.jpg)

得到纤维化

(18.3.1)

![bo_d7e85t491nqc73eqefm0_668_952_655_413_281_0.jpg](images/fu_algebraic_topology_and_differential_forms_214_bod7e85t491nqc73eqefm06689526554132810.jpg)

其中 \( \mathbb{C}{P}^{\infty } \) 如上例把所有有限维的复射影空间 \( \mathbb{C}{P}^{n} \) 粘合在一起得到. 因为当 \( q \geq  1 \) 时, \( {\pi }_{q}\left( {S}^{\infty }\right)  = 0 \) ,所以从纤维化的正合同伦序列

\[
\cdots  \rightarrow  {\pi }_{k}\left( {S}^{\infty }\right)  \rightarrow  {\pi }_{k}\left( {\mathbb{C}{P}^{\infty }}\right)  \rightarrow  {\pi }_{k - 1}\left( {S}^{1}\right)  \rightarrow  {\pi }_{k - 1}\left( {S}^{\infty }\right)  \rightarrow  \ldots
\]

可得

\[
{\pi }_{k}\left( {\mathbb{C}{P}^{\infty }}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & k = 2 \\  0 & \text{ 其余情形. } \end{array}\right.
\]

因此 \( \mathbb{C}{P}^{\infty } \) 是 \( \mathrm{{EM}} \) 空间 \( K\left( {\mathbb{Z},2}\right) \) .

练习 18.4. 由于对 \( k \geq  1 \) , \( {\pi }_{k}\left( {S}^{\infty }\right)  = 0 \) ,由 Hurewicz 同构定理知对 \( k \geq  1 \) , \( {H}_{k}\left( {S}^{\infty }\right)  = 0 \) . 应用纤维化 (18.3.1) 的谱序列证明 \( \mathbb{C}{P}^{\infty } \) 的上同调环是具有一个 2 维生成元的多项式代数:

\[
{H}^{ * }\left( {\mathbb{C}{P}^{\infty }}\right)  = \mathbb{Z}\left\lbrack  x\right\rbrack  ,\;\dim x = 2.
\]

例18.5.(透镜空间)设 \( {S}^{{2n} + 1} \) 是 \( {\mathbb{C}}^{n + 1} \) 中单位球面. \( {S}^{1} \) 自由作用在 \( {S}^{{2n} + 1} \) 上: 对任意 \( 0 \leq  \theta  \leq  1 \) ,

\[
{e}^{2\pi i\theta } \cdot  \left( {{z}_{0},\ldots ,{z}_{n}}\right)  = \left( {{e}^{2\pi i\theta }{z}_{0},\ldots ,{e}^{2\pi i\theta }{z}_{n}}\right) .
\]

所以 \( {S}^{1} \) 的任意子群也自由作用在 \( {S}^{{2n} + 1} \) 上. 例如, \( {\mathbb{Z}}_{5} \) 作用在 \( {S}^{{2n} + 1} \) 上: 当 \( k = 0,1,2,3,4 \) 时,

\[
{e}^{{2\pi ik}/5} \cdot  \left( {{z}_{0},\ldots ,{z}_{n}}\right)  = \left( {{e}^{{2\pi ik}/5}{z}_{0},\ldots ,{e}^{{2\pi ik}/5}{z}_{n}}\right) .
\]

\( {S}^{{2n} + 1} \) 由 \( {\mathbb{Z}}_{5} \) 作用得到的商空间是透镜空间 \( L\left( {n,5}\right) \) . 应用套叠构造

![bo_d7e85t491nqc73eqefm0_670_536_183_1252_309_0.jpg](images/fu_algebraic_topology_and_differential_forms_215_bod7e85t491nqc73eqefm067053618312523090.jpg)

得到一个五层覆盖的纤维化

![bo_d7e85t491nqc73eqefm0_670_908_613_507_304_0.jpg](images/fu_algebraic_topology_and_differential_forms_216_bod7e85t491nqc73eqefm06709086135073040.jpg)

因此,

\[
{\pi }_{k}\left( {L\left( {\infty ,5}\right) }\right)  = \left\{  \begin{array}{ll} {\mathbb{Z}}_{5} & k = 1 \\  0 & k > 1. \end{array}\right.
\]

确实当 \( k = 1 \) 时, \( {\pi }_{1}\left( {L\left( {\infty ,5}\right) }\right) \) 同构于由五个元组成的群,它只能是 \( {\mathbb{Z}}_{5} \) . 所以无穷透镜空间 \( L\left( {\infty ,5}\right) \) 是 EM 空间 \( K\left( {{\mathbb{Z}}_{5},1}\right) \) . 对任意正整数 \( q \) ,可同样构造无穷透镜空间 \( L\left( {\infty , q}\right) \) 并证明 \( L\left( {\infty , q}\right)  = K\left( {{\mathbb{Z}}_{q},1}\right) \) .

注记 18.5.1. 透镜空间 \( L\left( {n,2}\right) \) 是实射影空间 \( \mathbb{R}{P}^{{2n} + 1} \) ，无穷透镜空间 \( L\left( {\infty ,2}\right) \) 是 \( \mathbb{R}{P}^{\infty } \) . 注. 若 \( q \) 不是素数,在证明 \( L\left( {\infty , q}\right)  = K\left( {{\mathbb{Z}}_{q},1}\right) \) 时需作一点额外的处理. 事实上, 由纤维化的同伦序列与相对同伦序列可得: 当 \( k > 1 \) 时 \( {\pi }_{k}\left( {L\left( {\infty , q}\right) }\right)  = 0 \) 且存在双射

\[
\psi  : {\pi }_{1}\left( {{S}^{\infty },{\mathbb{Z}}_{q} \cdot  {x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {L\left( {\infty , q}\right) }\right) ,
\]

其中 \( {x}_{0} \in  {S}^{\infty } \) 是基点. 回忆 \( \psi \) 的定义. 对 \( \left\lbrack  \gamma \right\rbrack   \in  {\pi }_{1}\left( {{S}^{\infty },{\mathbb{Z}}_{q} \cdot  {x}_{0}}\right) ,\gamma \) 是 \( {S}^{\infty } \) 中一条起点为 \( {x}_{0} \) 终点在 \( {\mathbb{Z}}_{q} \cdot  {x}_{0} \) 中的道路,则 \( \psi \left( \left\lbrack  \gamma \right\rbrack  \right)  = \left\lbrack  {\pi  \circ  \gamma }\right\rbrack   \in  {\pi }_{1}\left( {L\left( {\infty , q}\right) }\right) \) .

由 \( \psi \) 诱导映射 \( \phi  : {\mathbb{Z}}_{q} \rightarrow  {\pi }_{1}\left( {L\left( {\infty , q}\right) }\right. \) . 对 \( g \in  {\mathbb{Z}}_{q} \) ,令 \( \gamma \) 是连接 \( {x}_{0} \) 与 \( g \cdot  {x}_{0} \) 的道路,定义 \( \phi \left( g\right)  = \left\lbrack  {\psi  \circ  \gamma }\right\rbrack \) . 由于 \( {S}^{\infty } \) 是单连通的,这个定义与道路 \( \gamma \) 的选取无关. 显然 \( \phi \) 是双射,我们只要证明 \( \phi \) 是同态,但这差不多也是显然的.

在《基础拓扑学》(Armstrong 著, 孙以丰译) 可找到如下更一般的定理.

定理. 若 \( G \) 是群,作用在单连通空间 \( X \) ,并且若 \( X \) 的每点 \( x \) 有邻域 \( U \) 使得对任意的 \( g \in  G, U \cap  g \cdot  U = \varnothing \) ，则 \( {\pi }_{1}\left( {X/G}\right) \) 与 \( G \) 同构.

计算透镜空间如 \( L\left( {n,5}\right) \) 的上同调. 因为透镜空间 \( L\left( {n,5}\right) \) 不是单连通的,纤维化 \( {\mathbb{Z}}_{5} \rightarrow  {S}^{{2n} + 1} \rightarrow  L\left( {n,5}\right) \) 在上同调的计算中没用. 需用交换图

![bo_d7e85t491nqc73eqefm0_672_637_273_1051_978_0.jpg](images/fu_algebraic_topology_and_differential_forms_217_bod7e85t491nqc73eqefm067263727310519780.jpg)

所以 \( {S}^{1} \) 在 \( {S}^{{2n} + 1} \) 上的作用可降到在 \( L\left( {n,5}\right) \) 上的作用,从而有纤维丛用正合同伦序列知 \( \mathbb{C}{P}^{n} \) 是单连通的, 所以这个纤维丛的 Leray 谱序列的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathbb{C}{P}^{n}}\right)  \otimes  {H}^{q}\left( {S}^{1}\right) .
\]

(18.5.2)

![bo_d7e85t491nqc73eqefm0_672_978_1396_375_296_0.jpg](images/fu_algebraic_topology_and_differential_forms_218_bod7e85t491nqc73eqefm067297813963752960.jpg)

![bo_d7e85t491nqc73eqefm0_673_575_403_1423_551_0.jpg](images/fu_algebraic_topology_and_differential_forms_219_bod7e85t491nqc73eqefm067357540314235510.jpg)

为了确定微分 \( {d}_{2} \) ,比较纤维丛 \( {S}^{1} \rightarrow  {S}^{{2n} + 1} \rightarrow  \mathbb{C}{P}^{n} \) 的谱序列. 丛映射

\[
\rho  : {S}^{{2n} + 1}\xrightarrow[]{5 : 1}L\left( {n,5}\right)
\]

诱导了双复形的链映射

\[
{\rho }^{ * } : {C}^{ * }\left( {{\pi }_{L}^{-1}\mathcal{U},{S}^{ * }}\right)  \rightarrow  {C}^{ * }\left( {{\pi }_{S}^{-1}\mathcal{U},{S}^{ * }}\right) .
\]

此处 \( \mathcal{U} \) 是 \( \mathbb{C}{P}^{n} \) 的一个好覆盖. 设 \( {a}_{L} \) 与 \( {a}_{S} \) 分别是这两个双复形的 \( {E}_{2}^{0,1} \) 的生成元, \( x \) 是 \( {H}^{2}\left( {\mathbb{C}{P}^{n}}\right) \) 的生成元. 由于 \( \deg \rho  = 5 \) ,所以 \( {\rho }^{ * }{a}_{L} = 5{a}_{S} \) .

因此

\[
{\rho }^{ * }\left( {{d}_{2}{a}_{L}}\right)  = {d}_{2}{\rho }^{ * }{a}_{L} = {d}_{2}\left( {5{a}_{S}}\right)  = 5{d}_{2}{a}_{S} = {5x}.
\]

所以在 (18.5.2) 中 \( {d}_{2}{a}_{L} = {5x} \) . 于是,

![bo_d7e85t491nqc73eqefm0_674_451_509_1456_511_0.jpg](images/fu_algebraic_topology_and_differential_forms_220_bod7e85t491nqc73eqefm067445150914565110.jpg)

因为 \( G{H}^{k} = { \oplus  }_{p + q = k}{E}_{\infty }^{p, q} \) ,而在 \( { \oplus  }_{p + q = k}{E}_{\infty }^{p, q} \) 中最多只出现一项非零,或为 \( {\mathbb{Z}}_{5} \) , 或为 \( \mathbb{Z} \) ,所以 \( {H}^{k} = G{H}^{k} \) .

\[
{H}^{ * }\left( {L\left( {n,5}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0 \\  {\mathbb{Z}}_{5} &  *  = 2,4,\ldots ,{2n} \\  \mathbb{Z} &  *  = {2n} + 1 \\  0 &  *  = \text{ 其余情形 } \end{array}\right.
\]

注记 18.5.3. (18.5.2) 中的微分 \( {d}_{2} \) 也可确定如下. 因为 \( {\pi }_{1}\left( {L\left( {n,5}\right) }\right)  = {\mathbb{Z}}_{5} \) ,所以 \( {H}_{1}\left( {L\left( {n,5}\right) }\right)  = {\mathbb{Z}}_{5} \) . 由推论 15.14.1,

\[
{H}^{2}\left( {L\left( {n,5}\right) }\right)  \simeq  {\mathbb{Z}}_{5} \oplus  {H}_{2}\text{ 的自由部分 }
\]

因为 \( {H}^{2}\left( {L\left( {n,5}\right) }\right)  = \mathbb{Z}/\mathrm{{im}}{d}_{2} \) ,所以 \( {H}^{2}\left( {L\left( {n,5}\right) }\right)  = {\mathbb{Z}}_{5},{d}_{2}a \) 等于 \( {5x} \) . 用相同方法可得透镜空间 \( L\left( {n, q}\right) \) 的上同调:

(18.6)

\[
{H}^{ * }\left( {L\left( {n, q}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0 \\  {\mathbb{Z}}_{q} &  *  = 2,4,\ldots ,{2n} \\  \mathbb{Z} &  *  = {2n} + 1 \\  0 &  *  = \text{ 其余情形 } \end{array}\right.
\]

练习 18.7. 证明透镜空间 \( L\left( {n, q}\right) \) 是可定向流形.

练习 18.8. 设 \( q > 1 \) 是整数, \( p \) 是素数. (a) 证明

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;\mathbb{Z}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0 \\  {\mathbb{Z}}_{q} &  *  = \text{ 正偶数 } \\  0 &  *  = \text{ 其余情况. } \end{array}\right.
\]

(b) 应用纤维化 \( {S}^{1} \rightarrow  K\left( {{\mathbb{Z}}_{q},1}\right)  \rightarrow  \mathbb{C}{P}^{\infty } \) 计算 \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right) \) . 解. (a) 应用纤维化

![bo_d7e85t491nqc73eqefm0_676_590_773_1143_821_0.jpg](images/fu_algebraic_topology_and_differential_forms_221_bod7e85t491nqc73eqefm067659077311438210.jpg)

的谱序列, 有

![bo_d7e85t491nqc73eqefm0_677_481_19_1377_571_0.jpg](images/fu_algebraic_topology_and_differential_forms_223_bod7e85t491nqc73eqefm06774811913775710.jpg)

由于 \( {S}^{\infty } \rightarrow  L\left( {\infty , q}\right) \) 是 \( q \) -重覆盖, \( {d}_{2}\left( a\right)  = {qa} \) ,所以

![bo_d7e85t491nqc73eqefm0_677_475_793_1195_457_0.jpg](images/fu_algebraic_topology_and_differential_forms_222_bod7e85t491nqc73eqefm067747579311954570.jpg)

由于谱序列收敛于 \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) }\right) \) ,由上图性质可得

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0 \\  {\mathbb{Z}}_{q} &  *  = 2,4,6,\ldots \\  0 &  *  = \text{ 其余情形 } \end{array}\right.
\]

(b) 由系数在交换环的奇异上同调的 Leray 定理 (15.11),纤维化谱序列的 \( {E}_{2} \) 页是

\[
{E}_{2}^{r, s} = {H}^{r}\left( {\mathbb{C}{P}^{\infty };{H}^{s}\left( {{S}^{1};{\mathbb{Z}}_{p}}\right) }\right) .
\]

由泛系数定理(15.14)

\[
{H}^{0}\left( {{S}^{1};{\mathbb{Z}}_{p}}\right)  = \operatorname{Hom}\left( {{H}_{0}\left( {S}^{1}\right) ,{\mathbb{Z}}_{p}}\right)  = \operatorname{Hom}\left( {\mathbb{Z},{\mathbb{Z}}_{p}}\right)  = {\mathbb{Z}}_{p}
\]

\[
{H}^{1}\left( {{S}^{1};{\mathbb{Z}}_{p}}\right)  = \operatorname{Hom}\left( {{H}_{1}\left( {S}^{1}\right) ,{\mathbb{Z}}_{p}}\right) \bigoplus \operatorname{Ext}\left( {{H}_{0}\left( {S}^{1}\right) ,{\mathbb{Z}}_{p}}\right)  = {\mathbb{Z}}_{p}.
\]

所以对 \( s = 0,1 \) ,由练习 18.4 可得

\[
{H}^{r}\left( {\mathbb{C}{P}^{\infty };{H}^{s}\left( {{S}^{1};{\mathbb{Z}}_{p}}\right) }\right)  = {H}^{r}\left( {\mathbb{C}{P}^{\infty };{\mathbb{Z}}_{p}}\right)
\]

\[
= \operatorname{Hom}\left( {{H}_{r}\left( {\mathbb{C}{P}^{\infty }}\right) ,{\mathbb{Z}}_{p}}\right) \bigoplus \operatorname{Ext}\left( {{H}_{r - 1}\left( {\mathbb{C}{P}^{\infty }}\right) ,{\mathbb{Z}}_{p}}\right)
\]

\[
= \left\{  \begin{array}{ll} {\mathbb{Z}}_{p} & r = \text{ 偶数 } \\  0 & r = \text{ 奇数 } \end{array}\right.
\]

所以 \( {E}_{2} \) 页是

![bo_d7e85t491nqc73eqefm0_679_535_341_1324_515_0.jpg](images/fu_algebraic_topology_and_differential_forms_225_bod7e85t491nqc73eqefm067953534113245150.jpg)

其中 \( {d}_{2}a = {qx} \) . 当质数 \( p \) 不能整除 \( q \) 时, \( {d}_{2} \) 是同构. 所以

![bo_d7e85t491nqc73eqefm0_679_511_1051_1358_473_0.jpg](images/fu_algebraic_topology_and_differential_forms_224_bod7e85t491nqc73eqefm0679511105113584730.jpg)

当 \( p \) 能整除 \( q \) 时, \( {d}_{2} \) 是零映射. 所以

![bo_d7e85t491nqc73eqefm0_680_630_381_1151_489_0.jpg](images/fu_algebraic_topology_and_differential_forms_226_bod7e85t491nqc73eqefm068063038111514890.jpg)

于是当 \( p \nmid  q \) 时,

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right)  = \left\{  \begin{array}{ll} {\mathbb{Z}}_{p} &  *  = 0 \\  0 & \text{ 其余情况 } \end{array}\right.
\]

当 \( p \mid  q \) 时,

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right)  = {\mathbb{Z}}_{p},\; *  \geq  0.
\]

练习 18.9. 设 \( n, q \) 是正整数. 证明

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q}, n}\right) ;\mathbb{Q}}\right)  = \left\{  \begin{array}{ll} \mathbb{Q} &  *  = 0 \\  0 &  *  = \text{ 其余情况 } \end{array}\right.
\]

因此, 根据有限生成的 abel 群的结构定理, 对有限生成的挠 abel 群 \( A \) , EM 空间 \( K\left( {A, n}\right) \) 的有理上同调是平凡的. 提示: 用归纳法. 对一般的 \( n \) ,要用纤维化

\[
K\left( {{\mathbb{Z}}_{q}, n - 1}\right)  \rightarrow  {PK}\left( {{\mathbb{Z}}_{q}, n}\right)
\]

\( K\left( {{\mathbb{Z}}_{q}, n}\right) \)

练习 18.10. 确定 \( {H}^{ * }\left( {L\left( {n, q}\right) }\right) ,{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) }\right) \) 与 \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right) \) 的积结构. 特别地, 证明

\[
{H}^{ * }\left( {\mathbb{R}{P}^{\infty }}\right)  = \mathbb{Z}\left\lbrack  x\right\rbrack  /\left( {2x}\right) ,\;\dim x = 2,
\]

\[
{H}^{ * }\left( {\mathbb{R}{P}^{\infty };{\mathbb{Z}}_{2}}\right)  = {\mathbb{Z}}_{2}\left\lbrack  x\right\rbrack  ,\;\dim x = 1.
\]

作业:

1. 练习 18.4.

2. 练习 18.7.

3. 练习 18.8. (不需做)

4. 练习 18.9.

5. 练习 18.10.

代数拓扑与微分形式
