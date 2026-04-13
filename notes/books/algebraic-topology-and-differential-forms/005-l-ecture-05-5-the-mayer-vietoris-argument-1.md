#### 5. Poincaré 对偶

§5 The Mayer-Vietoris Argument (1)

5. Poincaré 对偶

MV 序列把开子集之并的上同调与开子集的上同调联系在一起. 它连同五引理给出一个对开覆盖的开集个数进行归纳的证明方法, 称为 MV 方法.

MV 方法是十分有用的, 如可用它导出 de Rham 上同调的维数有限性, Poincaré 对偶, Künneth 公式, Leray-Hirsch 定理, 及 Thom 同构. 所有这些需假定流形具有有限好覆盖. 这次课主要讲 Poincaré 对偶.

- 好覆盖的存在性

- de Rham 上同调的维数有限性

- 定向流形上 Poincaré 对偶

- 闭定向子流形的 Poincaré 对偶

好覆盖的存在性设 \( M \) 是 \( n \) 维流形. \( M \) 的开覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 称为好覆盖若任意非空有限交

\[
{U}_{{\alpha }_{0}} \cap  {U}_{{\alpha }_{1}} \cap  \cdots  \cap  {U}_{{\alpha }_{p}}
\]

微分同胚于 \( {\mathbb{R}}^{n} \) . 若指标集 \( I \) 中元素的个数 \( \left| I\right| \) 是有限的,则称 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是有限好覆盖.

为简单计,以后把交集 \( {U}_{{\alpha }_{0}} \cap  \cdots  \cap  {U}_{{\alpha }_{p}} \) 简记为 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) ,它可能是空集.

定理 5.1. 流形具有好覆盖. 紧流形具有有限好覆盖.

证. 赋予 \( M \) 一个黎曼度量. 对任意点 \( x \in  M \) ,令 \( {U}_{x} \) 是点 \( x \) 的一个测地凸邻域. 因为测地凸邻域微分同胚于 \( {\mathbb{R}}^{n} \) 且有限多个测地凸邻域的非空交也是测地凸邻域*，所以 \( {\left\{  {U}_{x}\right\}  }_{x \in  M} \) 是 \( M \) 的一个好覆盖.

当 \( M \) 紧时,取这个覆盖的有限子覆盖即成.

*测地凸邻域的结论在任何一本黎曼几何的教材中都有，例如见白正国，沈一兵等编著的《黎曼几何初步》的第四章.

给定两个开覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I},\mathcal{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) ,若每个 \( {V}_{\beta } \) 包含在某个 \( {U}_{\alpha } \) 中,则称 \( \mathcal{V} \) 是 \( \mathcal{U} \) 的一个加细 (refinement) 并记作 \( \mathcal{U} < \mathcal{V} \) . 更精确地说,我们指定一个加细是通过给定映射 \( \phi  : J \rightarrow  I \) 使得 \( {V}_{\beta } \subset  {U}_{\phi \left( \beta \right) } \) .

把上述证明稍作修改, 就能证明流形的每个开覆盖有一个加细的好覆盖. 这是因为一点的测地凸邻域可充分小, 只要在每点取一个测地凸邻域使得它包含在给定开覆盖的某个开集内.

de Rham 上同调的维数有限性

命题 5.3.1 若流形 \( M \) 具有有限好覆盖,则 \( \dim {H}^{ * }\left( M\right)  < \infty \) .

证. 记 \( {h}^{q}\left( M\right)  = \dim {H}^{q}\left( M\right) \) . 从 MV 序列

\[
\cdots  \rightarrow  {H}^{q - 1}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{q}\left( {U \cup  V}\right) \overset{r}{ \rightarrow  }{H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right)  \rightarrow  \cdots
\]

得

\[
{H}^{q}\left( {U \cup  V}\right)  \simeq  \ker r \oplus  \operatorname{im}r \simeq  \operatorname{im}{d}^{ * } \oplus  \operatorname{im}r
\]

所以有以下结论:

\( \left( {*1}\right) \) 若 \( {h}^{q}\left( U\right) ,{h}^{q}\left( V\right) ,{h}^{q - 1}\left( {U \cap  V}\right)  < \infty \) ,则 \( {h}^{q}\left( {U \cup  V}\right)  < \infty \) .

我们对有限好覆盖的开集个数进行归纳证明. 当个数为 1 时, \( M \) 微分同胚于 \( {\mathbb{R}}^{n} \) . 由 Poincaré 引理知结论成立.

假定:若一个流形具有开集个数不超过 \( p \) 的有限好覆盖，则它的上同调维数有限.

现设 \( M \) 具有有限好覆盖 \( \left\{  {{U}_{0},{U}_{1},\ldots ,{U}_{p}}\right\} \) . 令

\[
W = {U}_{0} \cup  \cdots  \cup  {U}_{p - 1},\;V = {U}_{p}.
\]

则

\[
W \cap  V = {U}_{0p} \cup  {U}_{1p} \cup  \cdots  \cup  {U}_{p - 1, p}.
\]

所以 \( W \cap  V \) 具有一个开集个数不超过 \( p \) 的有限好覆盖 \( \left\{  {{U}_{0p},\ldots {U}_{p - 1, p}}\right\} \) . 由归纳假定知 \( {h}^{ * }\left( {W \cap  V}\right)  < \infty ,{h}^{ * }\left( W\right)  < \infty ,{h}^{ * }\left( V\right)  < \infty \) . 于是由结论 \( \left( {*1}\right) \) 得 \( {h}^{ * }\left( {W \cup  V}\right)  < \infty \) ,即 \( {h}^{ * }\left( M\right)  < \infty \) .

同理可证

命题 5.3.2. 若流形 \( M \) 具有有限好覆盖,则 \( \dim {H}_{c}^{q}\left( M\right)  < \infty \) .

补充练习 1 . 证明命题 5.3.2.

定向流形上 Poincaré 对偶设 \( V \) , \( W \) 是两个有限维向量空间. \( V \) , \( W \) 之间的一个配对 (pairing)

\[
\langle \;,\;\rangle  : V{ \otimes  }_{\mathbb{R}}W \rightarrow  \mathbb{R}
\]

是一个双线性映射. 它诱导了两个线性映射:

\[
{l}_{V} : V \rightarrow  {W}^{ * },\;v \mapsto  \langle v,\rangle
\]

\[
{l}_{W} : W \rightarrow  {V}^{ * },\;w \mapsto  \langle , w\rangle
\]

此处 \( {V}^{ * } \) , \( {W}^{ * } \) 分别是 \( V \) , \( W \) 的对偶空间*. 如果这两个映射是单射,则称配对 \( \langle \) , \( \rangle \) 是非退化的.

引理. 两个有限维向量空间 \( V \) , \( W \) 之间的配对 \( \langle \) , \( \rangle \) 是非退化的当且仅当由它诱导的线性映射 \( {l}_{V} : V \rightarrow  {W}^{ * } \) 是同构.

\( {}^{ * }{V}^{ * } = \operatorname{Hom}\left( {V,\mathbb{R}}\right) \) ,它是由定义在 \( V \) 上的所有线性函数组成的.

证.

" \( \Rightarrow \) ":

\( \because {l}_{V} : V \rightarrow  {W}^{ * },{l}_{W} : W \rightarrow  {V}^{ * } \) 是单射且 \( V, W \) 是有限维的,

\( \therefore \dim V \leq  \dim {W}^{ * } = \dim W \leq  \dim {V}^{ * } = \dim V \) .

\( \therefore \dim V = \dim {W}^{ * },{l}_{V} : V \rightarrow  {W}^{ * } \) 是同构.

"==":

\( \because {l}_{V} : V \rightarrow  {W}^{ * } \) 是同构且 \( V, W \) 是有限维的,

\( \therefore {\left( {l}_{V}\right) }^{ * } : {\left( {W}^{ * }\right) }^{ * } \rightarrow  {V}^{ * } \) 也是同构.

\( \therefore \) 在典则同构 \( {\left( {W}^{ * }\right) }^{ * } \simeq  W \) 下,有下列交换图表:

(1)

![bo_d7e85t491nqc73eqefm0_100_1021_1018_524_389_0.jpg](images/fu_algebraic_topology_and_differential_forms_001_bod7e85t491nqc73eqefm0100102110185243890.jpg)

于是 \( {l}_{W} : W \rightarrow  {V}^{ * } \) 是同构.

补充练习 2 . 证明图表 (1) 的可交换性.

以下假定 \( M \) 是 \( n \) 维光滑流形,具有有限好覆盖. 所以 \( {H}^{q}\left( M\right) ,{H}_{c}^{n - q}\left( M\right) \) 是两个有限维向量空间. 假定 \( M \) 是定向流形. 定义这两个有限维向量空间的配对

\[
{\int }_{M} : {H}^{q}\left( M\right) { \otimes  }_{\mathbb{R}}{H}_{c}^{n - q}\left( M\right)  \rightarrow  \mathbb{R}
\]

\[
\left( {\left\lbrack  \omega \right\rbrack  ,\left\lbrack  \tau \right\rbrack  }\right) \; \mapsto  {\int }_{M}\omega  \land  \tau
\]

由 Stokes 定理上述配对是定义好的,即与 \( \left\lbrack  \omega \right\rbrack  ,\left\lbrack  \tau \right\rbrack \) 的代表元选取无关.

定理 5.4. (Poincaré 对偶) 若 \( M \) 是定向 \( n \) 维流形且具有有限好覆盖,则配对 \( {\int }_{M} \) 是非退化的. 等价地,

\[
{H}^{q}\left( M\right)  \simeq  {\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * }
\]

\[
{H}_{c}^{n - q}\left( M\right)  \simeq  {\left( {H}^{q}\left( M\right) \right) }^{ * }
\]

在证明此定理之前需做一些准备.

回忆两个 MV 序列:

\[
\rightarrow  {H}^{q}\left( {U \cup  V}\right) \xrightarrow[]{\text{ 限制 }}{H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right) \xrightarrow[]{\text{ 差 }}{H}^{q}\left( {U \cap  V}\right) \xrightarrow[]{{d}^{ * }}{H}^{q + 1}\left( {U \cup  V}\right)
\]

\[
\left( {\delta ,\tau }\right) \; \mapsto  \;\tau {\left| {}_{U \cap  V} - \delta \right| }_{U \cap  V}
\]

\[
\omega \; \mapsto  \left\{  \begin{array}{ll}  - d\left( {{\rho }_{V}\omega }\right) & \text{ on }U \\  d\left( {{\rho }_{U}\omega }\right) & \text{ on }V \end{array}\right.
\]

\[
{H}_{c}^{n - q}\left( {U \cup  V}\right) \overset{ \leftarrow  }{ \leftarrow  }{H}_{c}^{n - q}\left( U\right)  \oplus  {H}_{c}^{n - q}\left( V\right) \overset{{\zeta }_{n}}{ \leftarrow  }\overset{p - q}{ \leftarrow  }{H}_{c}^{n - q}\left( {U \cap  V}\right) \overset{{\zeta }_{n}}{ \leftarrow  }{H}_{c}^{n - q - 1}\left( {U \cup  V}\right)
\]

\[
\begin{array}{l} {\left. d{\rho }_{V} \land  \tau \right| }_{U \cap  V} \\  {\left. d{\rho }_{V} \land  \tau \right| }_{U \cap  V} \\  \end{array}
\]

此处 \( {j}_{ * } \) 是零延拓.

引理 5.6. 有以下带符号的交换图表*

![bo_d7e85t491nqc73eqefm0_103_208_154_1923_468_0.jpg](images/fu_algebraic_topology_and_differential_forms_002_bod7e85t491nqc73eqefm010320815419234680.jpg)

例如右边方块的带符号交换性是说,对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{q}\left( {U \cap  V}\right) ,\left\lbrack  \tau \right\rbrack   \in  {H}_{c}^{n - q - 1}(U \cup \; V) \) ,有

\[
{\int }_{U \cup  V}{d}^{ * }\omega  \land  \tau  =  \pm  {\int }_{U \cap  V}\omega  \land  {d}_{ * }\tau
\]

证. 只证上述等式. 根据定义有:

\[
{\int }_{U \cup  V}{d}^{ * }\omega  \land  \tau  =  - {\int }_{U \cup  V}d\left( {{\rho }_{V}\omega }\right)  \land  \tau  =  - {\int }_{U \cap  V}d{\rho }_{V} \land  \omega  \land  \tau ,
\]

最后一个等号是因为 \( \operatorname{\mathsf{S} upp}d{\rho }_{V} \subset  U \cap  V \) ；

\[
{\int }_{U \cap  V}\omega  \land  {d}_{ * }\tau  = {\int }_{U \cap  V}\omega  \land  d{\rho }_{V} \land  \tau  = {\left( -1\right) }^{q}{\int }_{U \cap  V}d{\rho }_{V} \land  \omega  \land  \tau .
\]

*规定:当 \( M \) 是定向流形时，它的开子集的定向与 \( M \) 的定向一致.

因为配对 \( \int \) 诱导了一个从上行正合序列到下行正合序列对偶的映射,所以引理 5.6 是说下列图表是带符号交换的:

![bo_d7e85t491nqc73eqefm0_104_123_503_2068_280_0.jpg](images/fu_algebraic_topology_and_differential_forms_003_bod7e85t491nqc73eqefm010412350320682800.jpg)

证明 Poincaré 对偶还需以下代数引理.

练习 5.5. (五引理) 给定下列 abel 群与同态的交换图表

![bo_d7e85t491nqc73eqefm0_104_428_1139_1490_289_0.jpg](images/fu_algebraic_topology_and_differential_forms_004_bod7e85t491nqc73eqefm0104428113914902890.jpg)

并且其行是正合的. 证明若 \( \alpha ,\beta ,\delta ,\epsilon \) 是同构,则 \( \gamma \) 也是同构.

定理 5.4 的证明. 结合上述交换图表与五引理, 得到结论:

(*2) 若 Poincaré 对偶对 \( U, V, U \cap  V \) 成立,则对 \( U \cup  V \) 也成立.

由此可对有限好覆盖的开集个数进行归纳证明. 设 \( M \) 有一个有限好覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) .

若 \( \left| I\right|  = 1 \) . 则 \( M \) 与 \( {\mathbb{R}}^{n} \) 微分同胚, Poincaré 对偶可由两个 Poincaré 引理得到.

假定 Poincaré 对偶对具有开集个数不超过 \( p \) 的有限好覆盖的流形成立. 现设 \( M \) 具有有限好覆盖 \( \left\{  {{U}_{0},{U}_{1},\ldots ,{U}_{p}}\right\} \) . 令

\[
W = {U}_{0} \cup  \cdots  \cup  {U}_{p - 1},\;V = {U}_{p}.
\]

则

\[
W \cap  V = {U}_{0p} \cup  {U}_{1p} \cup  \cdots  \cup  {U}_{p - 1, p}.
\]

所以 \( W \cap  V \) 具有开集个数不超过 \( p \) 的有限好覆盖 \( \left\{  {{U}_{0p},\ldots ,{U}_{p - 1, p}}\right\} \) . 由归纳假定，Poincaré 对偶对 \( W \) , \( V \) , \( W \cap  V \) 成立. 因为 \( M = W \cup  V \) , 由结论 (*2) 知 Poincaré 对偶对 \( M \) 也成立. 若把定理 5.4 中 “具有有限好覆盖” 的条件去掉, 则有以下定理.

定理 5.4’. (Poincaré 对偶) 若 \( M \) 是定向 \( n \) 维流形,它的上同调不必是有限维的, 则

\[
{H}^{q}\left( M\right)  \simeq  {\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * }.
\]

注记 5.7. 反之,同构 \( {H}_{c}^{q}\left( M\right)  \simeq  {\left( {H}^{n - q}\left( M\right) \right) }^{ * } \) 不一定成立. 不对称性来自于以下事实:直和的对偶是直积, 但直积的对偶不是直和. 例如, 设 \( {\left\{  {M}_{i}\right\}  }_{i \in  \mathbb{N}} \) 是一列具有有限好覆盖的定向 \( n \) 维流形. 考虑它们不相交的并 \( M = \mathop{\coprod }\limits_{{i \in  \mathbb{N}}}{M}_{i} \) . 则

\[
{H}^{q}\left( M\right)  = \mathop{\prod }\limits_{i}{H}^{q}\left( {M}_{i}\right) \;\text{ (直积); }
\]

\[
{H}_{c}^{n - q}\left( M\right)  = { \oplus  }_{i}{H}_{c}^{n - q}\left( {M}_{i}\right) \;\text{ (直和), }
\]

这是因为具紧支集的形式只能有有限多个分量不为零. 因为直和的对偶是直积且 Poincaré 对偶对每个 \( {M}_{i} \) 成立,所以

\[
{\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * } = \prod {\left( {H}_{c}^{n - q}\left( {M}_{i}\right) \right) }^{ * } \simeq  \prod {H}^{q}\left( {M}_{i}\right)  = {H}^{q}\left( M\right) .
\]

但是因为直积的对偶不是直和, 所以另一个同构不成立.

推论 5.8. 若 \( M \) 是连通定向 \( n \) 维流形,则 \( {H}_{c}^{n}\left( M\right)  \simeq  \mathbb{R} \) . 特别地,若 \( M \) 是连通紧定向流形,则 \( {H}^{n}\left( M\right)  \simeq  \mathbb{R} \) .

证. \( {\left( {H}_{c}^{n}\left( M\right) \right) }^{ * } \simeq  {H}^{0}\left( M\right)  \simeq  \mathbb{R} \) .

考虑两个紧定向 \( n \) 维流形之间映射的度. 设 \( M, N \) 是紧定向 \( n \) 维流形, \( f : M \rightarrow  N \) 是光滑映射. 设 \( \left\lbrack  \omega \right\rbrack \) 是 \( {H}^{n}\left( N\right) \) 的生成元. \( f \) 的度 (degree) 定义为

\[
\deg f = {\int }_{M}{f}^{ * }\omega
\]

则 \( \deg f \in  \mathbb{Z} \) .

在证明上述结论时需要用到以下形式的 Sard 定理.

定理 4.11. (Sard 定理) 光滑映射 \( f : M \rightarrow  N \) 的临界值集是零测集.

闭定向子流形的 Poincaré 对偶设 \( M \) 是 \( n \) 维定向流形.

(1)假定 \( i : S \rightarrow  M \) 是 \( k \) 维闭定向子流形，即 \( S \) 对于子空间拓扑是闭的且没有边界. 作为 \( {\mathbb{R}}^{2} - 0 \) 的子流形,下列左图是闭子流形而右图不是.

![bo_d7e85t491nqc73eqefm0_108_609_710_1082_325_0.jpg](images/fu_algebraic_topology_and_differential_forms_005_bod7e85t491nqc73eqefm010860971010823250.jpg)

设 \( \omega  \in  {Z}_{c}^{k}\left( M\right) \) ,即 \( \omega  \in  {\Omega }_{c}^{k}\left( M\right) \) 且 \( {d\omega } = 0 \) . 因为 \( S \) 是 \( M \) 的闭子集,所以 \( \operatorname{Supp}\left( {{i}^{ * }\omega }\right) \) 不仅是 \( S \) 的闭子集,也是 \( M \) 的闭子集. 因此 \( \operatorname{Supp}\left( {{i}^{ * }\omega }\right)  \subset  \operatorname{Supp}\omega \) 作为 \( M \) 中紧集的闭子集也是紧的. 于是 \( {i}^{ * }\omega \) 在 \( S \) 中也有紧支集，积分

\[
{\int }_{S}{i}^{ * }\omega
\]

是有意义的.

另一方面,设 \( \omega  \in  {B}_{c}^{k}\left( M\right) \) ,即 \( \omega  = {d\varphi } \) 且 \( \varphi  \in  {\Omega }_{c}^{k - 1}\left( M\right) \) . 同理 Supp \( \left( {{i}^{ * }\varphi }\right)  \subset  S \) 是紧集. 由 Stokes 定理,

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{S}{i}^{ * }\left( {d\varphi }\right)  = {\int }_{S}d\left( {{i}^{ * }\varphi }\right)  = 0.
\]

综上所述, \( {\int }_{S}{i}^{ * } \) 定义了 \( {H}_{c}^{k}\left( M\right) \) 上一个线性泛函,即

\[
{\int }_{S}{i}^{ * } \in  {\left( {H}_{c}^{k}\left( M\right) \right) }^{ * }.
\]

于是由定理 5.4′可知*, \( {\int }_{S}{i}^{ * } \) 对应于唯一的 \( \left\lbrack  {\eta }_{S}\right\rbrack   \in  {H}^{n - k}\left( M\right) \) 使得对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}_{c}^{k}\left( M\right) \) 有

(5.13)

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{M}\omega  \land  {\eta }_{S}
\]

\( \left\lbrack  {\eta }_{S}\right\rbrack \) 或它的任一代表元 \( {\eta }_{S} \) 称为 \( S \) 的 (闭) Poincaré 对偶.

*注意此处不需假定 \( M \) 具有有限好覆盖.

(2) 假定 \( i : S \rightarrow  M \) 是 \( k \) 维紧(致无边的)定向子流形. 因为 Hausdorff 空间的紧子集是闭子集, \( S \) 也是闭子流形. 由上述讨论知, \( S \) 有闭 Poincaré 对偶 \( \left\lbrack  {\eta }_{S}\right\rbrack   \in  {H}^{n - k}\left( M\right) . \)

另一方面,因为 \( S \) 是紧的,对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{k}\left( M\right) \) ,积分 \( {\int }_{S}{i}^{ * }\omega \) 有意义. 此时 \( {\int }_{S}{i}^{ * } \) 定义了 \( {H}^{k}\left( M\right) \) 上一个线性泛函,即 \( {\int }_{S}{i}^{ * } \in  {\left( {H}^{k}\left( M\right) \right) }^{ * } \) . 现假定 \( M \) 具有有限好覆盖. 则由定理 5.4 知, \( {\int }_{S}{i}^{ * } \) 对应于唯一的 \( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack   \in  {H}_{c}^{n - k}\left( M\right) \) 使得对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{k}\left( M\right) \) 有

(5.14)

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{M}\omega  \land  {\eta }_{S}^{\prime }
\]

\( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack \) 或 \( {\eta }_{S}^{\prime } \) 称为 \( S \) 的紧 Poincaré 对偶. 若 (5.14) 对任意闭 \( k \) -形式 \( \omega \) 成立,则它当然对任意具紧支集的闭 \( k \) -形式 \( \omega \) 成立. 所以作为一个形式, \( {\eta }_{S}^{\prime } \) 也是 \( S \) 的闭 Poincaré 对偶,即自然映射

\[
{H}_{c}^{n - k}\left( M\right)  \rightarrow  {H}^{n - k}\left( M\right)
\]

把紧 Poincapé 对偶映为闭 Poincaré 对偶. 因此我们总能要求紧定向子流形的闭 Poincaré 对偶有紧支集(即使 \( M \) 不具有有限好覆盖，具体见 (6.23) 的证明之后). 然而作为上同调类, \( \left\lbrack  {\eta }_{S}\right\rbrack   \in  {H}^{n - k}\left( M\right) \) 与 \( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack   \in  {H}_{c}^{n - k}\left( M\right) \) 可能是非常不同的. 我们把上面的讨论总结成一张图: 设 \( M \) 是定向流形.

\( S \) : 闭

![bo_d7e85t491nqc73eqefm0_112_636_377_1051_697_0.jpg](images/fu_algebraic_topology_and_differential_forms_006_bod7e85t491nqc73eqefm011263637710516970.jpg)

\( S \) : 紧

所以当 \( S \) 紧时, \( {\eta }_{S}^{\prime } \) 也是 \( S \) 的闭 Poincaré 对偶,但可能

\[
{H}_{c}^{n - k}\left( M\right)  \rightarrow  {H}^{n - k}\left( M\right)
\]

\[
{\left\lbrack  {\eta }_{S}^{\prime }\right\rbrack  }_{c} \neq  0\; \mapsto  \;{\left\lbrack  {\eta }_{S}^{\prime }\right\rbrack  }_{d} = 0
\]

例 5.15. \( \left( {\mathbb{R}}^{n}\right. \) 上一点 \( P \) 的 Poincaré 对偶)

因为 \( {H}^{n}\left( {\mathbb{R}}^{n}\right)  = 0 \) ,所以点 \( P \) 的闭 Poincaré 对偶 \( \left\lbrack  {\eta }_{P}\right\rbrack   = 0,{\eta }_{P} \) 可以是 \( {\mathbb{R}}^{n} \) 上任意的闭 \( n \) -形式.

又因为 \( f \in  {H}^{0}\left( {\mathbb{R}}^{n}\right) \) 是某个常值函数 \( c \) ,所以

\[
{\int }_{P}{i}^{ * }f = f\left( P\right)  = c,\;{\int }_{{\mathbb{R}}^{n}}f{\eta }_{P}^{\prime } = c{\int }_{{\mathbb{R}}^{n}}{\eta }_{P}^{\prime }.
\]

于是

\[
{\int }_{{\mathbb{R}}^{n}}{\eta }_{P}^{\prime } = 1
\]

这就是说,点 \( P \) 的紧 Poincaré 对偶可由积分为 1 的 bump \( n \) -形式 \( {\eta }_{P}^{\prime } \) 表示,它的上同调类 \( \left\lbrack  {\eta }_{P}^{\prime }\right\rbrack \) 是 \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 中的生成元.

例一练习 5.16. \( \left( {{\mathbb{R}}^{2} - 0}\right. \) 中射线与圆周的 Poincaré 对偶)

设 \( x, y \) 与 \( r,\theta \) 分别是 \( {\mathbb{R}}^{2} - 0 \) 上的标准坐标与极坐标. 注意 \( \theta \) 不是整体定义的,但 \( {d\theta } \) 是整体定义的.

因为 \( {S}^{1} \) 是 \( {\mathbb{R}}^{2} - 0 \) 的形变收缩,所以 \( {H}^{1}\left( {{\mathbb{R}}^{2} - 0}\right)  \simeq  {H}^{1}\left( {S}^{1}\right) \) 是 1 维的. 因为 \( {\int }_{{S}^{1}}\frac{d\theta }{2\pi } = 1 \) ,所以 \( \left\lbrack  \frac{d\theta }{2\pi }\right\rbrack   \in  {H}^{1}\left( {S}^{1}\right) \) 是生成元. \( \left\lbrack  \frac{d\theta }{2\pi }\right\rbrack \) 也可以看作是 \( {H}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 的生成元, 它没有紧支集.

另一方面,因为 \( {\mathbb{R}}^{2} - 0 \) 具有有限好覆盖,由 Poincaré 对偶知, \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2} - 0}\right)  \simeq \; {\left( {H}^{1}\left( {\mathbb{R}}^{2} - 0\right) \right) }^{ * } \) 是 1 维的. 设 \( \rho \left( r\right) \) 有紧支集, Supp \( \rho  \subset  \left( {0,\infty }\right) \) ,且 \( {\int }_{0}^{\infty }\rho \left( r\right) {dr} = \) 1. 则 \( \left\lbrack  {\rho \left( r\right) {dr}}\right\rbrack \) 是 \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 的生成元,但它在 \( {H}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 中为零.

(a) 射线的闭 Poincaré 对偶. 射线 \( l = \{ \left( {x,0}\right)  \mid  x > 0\} \) 是 \( {\mathbb{R}}^{2} - 0 \) 的闭子流形. 因为 \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 的生成元是 \( \left\lbrack  {\rho \left( r\right) {dr}}\right\rbrack \) ,计算

\[
{\int }_{{\mathbb{R}}^{2} - 0}\rho \left( r\right) {dr} \land  \frac{d\theta }{2\pi } = {\int }_{0}^{\infty }\rho \left( r\right) {dr}{\int }_{0}^{2\pi }\frac{d\theta }{2\pi } = 1 = {\int }_{l}\rho \left( r\right) {\left. dr\right| }_{l}.
\]

所以射线 \( l \) 的闭 Poincaré 对偶是 \( \left\lbrack  \frac{d\theta }{2\pi }\right\rbrack \) .

我们也可对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}_{c}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 直接进行验证: 应用 Stokes 定理,

\[
{\int }_{{\mathbb{R}}^{2} - 0}\omega  \land  {d\theta } =  - {\int }_{l \times  \left\lbrack  {{0}^{ + },2{\pi }^{ - }}\right\rbrack  }d\left( {\omega \theta }\right)
\]

\[
=  - {\left. {\int }_{{l}^{ + }}\left( \omega  \cdot  \theta \right) \right| }_{{l}^{ + }} - {\left. {\int }_{{l}^{ - }}\left( \omega  \cdot  \theta \right) \right| }_{{l}^{ - }} = {\left. 2\pi {\int }_{l}\omega \right| }_{l}.
\]

![bo_d7e85t491nqc73eqefm0_115_690_1251_916_346_0.jpg](images/fu_algebraic_topology_and_differential_forms_007_bod7e85t491nqc73eqefm011569012519163460.jpg)

(b) \( {S}^{1} \) 的闭 Poincaré 对偶. 因为 \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 的生成元是 \( \left\lbrack  {\rho \left( r\right) {dr}}\right\rbrack \) 且

\[
{\int }_{{S}^{1}}{i}^{ * }\left( {\rho \left( r\right) {dr}}\right)  = 0,
\]

所以 \( {S}^{1} \) 的闭 Poincaré 对偶 \( \left\lbrack  {\eta }_{{S}^{1}}\right\rbrack \) 为零.

(c) \( {S}^{1} \) 的紧 Poincaré 对偶. 因为 \( {H}^{1}\left( {{\mathbb{R}}^{2} - 0}\right) \) 的生成元是 \( \left\lbrack  \frac{d\theta }{2\pi }\right\rbrack \) ,

\[
{\int }_{{\mathbb{R}}^{2} - 0}\frac{d\theta }{2\pi } \land  \rho \left( r\right) {dr} =  - {\int }_{{\mathbb{R}}^{2} - 0}\rho \left( r\right) {dr} \land  \frac{d\theta }{2\pi } =  - 1 =  - {\int }_{{S}^{1}}\frac{d\theta }{2\pi }
\]

所以 \( {S}^{1} \) 的紧 Poincaré 对偶 \( \left\lbrack  {\eta }_{{S}^{1}}^{\prime }\right\rbrack \) 是 \( - \left\lbrack  {\rho \left( r\right) {dr}}\right\rbrack \) . Thus the generator of \( {H}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is represented by the ray and the generator of \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) by the circle.

![bo_d7e85t491nqc73eqefm0_116_426_1090_1278_520_0.jpg](images/fu_algebraic_topology_and_differential_forms_008_bod7e85t491nqc73eqefm0116426109012785200.jpg)

Remark 5.17. The two Poincaré duals of a compact oriented submanifold correspond to the two homology theories—closed homology and compact homology. Closed homology has now fallen into disuse, while compact homology is known these days as the homology of singular chains. In Example-Exercise 5.16, the generator of \( {H}_{1,\operatorname{closed}}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is the ray, while the generator of \( {H}_{1,\text{ compact }}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is the circle. (The circle is a boundary in closed homology since the punctured closed disk is a closed 2-chain in \( {\mathbb{R}}^{2} - \{ 0\} \) .) In general Poincaré duality sets up an isomorphism between closed homology and de Rham cohomology, and between compact homology and compact de Rham cohomology. 设 \( S \) 是 \( M \) 中紧定向 \( k \) 维子流形, \( W \) 是 \( M \) 中包含 \( S \) 的开子集. 所以 \( S \) 也是 \( W \) 中紧定向 \( k \) 维子流形. 设 \( \left\lbrack  {\eta }_{S, W}^{\prime }\right\rbrack   \in  {H}_{c}^{n - k}\left( W\right) \) 为 \( S \) 在 \( W \) 中的紧 Poincaré 对偶. 设 \( {\eta }_{S}^{\prime } \) 是把 \( {\eta }_{S, W}^{\prime } \) 零延拓到整个 \( M \) . 因为对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{k}\left( M\right) \) ,

\[
{\int }_{S}{i}^{ * }\omega  = {\left. {\int }_{W}\omega \right| }_{W} \land  {\eta }_{S, W}^{\prime } = {\int }_{M}\omega  \land  {\eta }_{S}^{\prime },
\]

所以 \( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack \) 是 \( S \) 在 \( M \) 中的紧 Poincaré 对偶. 这样就得到所谓的

局部化原理: \( S \) 在 \( M \) 中的紧 Poincaré 对偶的支集可缩小到 \( S \) 的任一开邻域中.

局部化原理对非紧闭定向子流形也成立. 以后我们会通过 Poincaré 对偶与 Thom 类的关系看到这点.

在本书 Poincaré 对偶指闭 Poincaré 对偶. 但是, 正如我们已经看到, 若子流形是紧的,我们能要求它的闭 Poincaré 对偶即使作为 \( {H}^{n - k}\left( M\right) \) 的上同调类有紧支集. 当然, 在紧流形上闭与紧 Poincaré 对偶是没有区别的.

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 练习 5.5.

代数拓扑与微分形式
