#### 第27讲 Review of Homotopy Theory (2)

§17 Review of Homotopy Theory (2)

27. Hurewicz 同构定理这次课首先计算球面的一些低维同伦群. 计算的几何思想导致贴胞腔的同伦性质. 从一些点出发通过贴从低维到高维的胞腔得到的空间称为 \( \mathrm{{CW}} \) 复形. 接着讨论同伦与同调之间的关系, 应用同调谱序列证明 Hurewicz 同构定理, 作为推论直接得到球面的 \( q \leq  n \) 的同伦群 \( {\pi }_{q}\left( {S}^{n}\right) \) .

- 球面的一些同伦群

- 贴胞腔

- 同伦与同调的关系

球面的一些同伦群在这节对 \( q \leq  n \) 计算 \( {\pi }_{q}\left( {S}^{n}\right) \) . 虽然这些同伦群可从 Hurewicz 同构定理 (17.21) 直接得到，但是在这里给出的几何证明是重要的，它为接下来讨论贴胞腔的同伦性质 (17.11) 提供了一个范式.

命题 17.8. 两个流形间的连续映射连续同伦于一个光滑映射.

推论 17.8.1. 流形在光滑意义下的同伦群与在连续意义下的同伦群相等.

命题 17.9. 当 \( q < n \) 时, \( {\pi }_{q}\left( {S}^{n}\right)  = 0 \) .

证. 设连续映射 \( \alpha  : {S}^{q} \rightarrow  {S}^{n} \) 表示同伦类 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {S}^{n}\right) \) . 由命题 17.8,可设 \( \alpha \) 是光滑的. 因为 \( q < n,\alpha \) 的值都是临界值. 由 Sard 定理, \( \alpha \) 不是满射.

设 \( P \in  {S}^{n} - \alpha \left( {S}^{q}\right) , Q =  - P \in  {S}^{n} \) . 设 \( F \) 是从 \( {S}^{n} - P \) 到 \( Q \) 的形变收缩:

\[
{F}_{t} : {S}^{n} - P \rightarrow  {S}^{n} - P, t \in  \left\lbrack  {0,1}\right\rbrack
\]

\[
{F}_{0} = \mathrm{{id}} : {S}^{n} - P \rightarrow  {S}^{n} - P
\]

\[
{F}_{1} = \text{ 常值映射 }c : {S}^{n} - P \rightarrow  Q.
\]

则 \( {F}_{t} \circ  \alpha \) 是 \( {F}_{0} \circ  \alpha  = \alpha \) 与常值映射 \( {F}_{1} \circ  \alpha  = c \) 之间的同伦. 所以 \( \left\lbrack  \alpha \right\rbrack   = 0 \) .

![bo_d7e85t491nqc73eqefm0_632_853_1070_590_586_0.jpg](images/fu_algebraic_topology_and_differential_forms_195_bod7e85t491nqc73eqefm063285310705905860.jpg)

命题 17.10. \( {\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z} \) .

设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{n}\left( {S}^{n}\right) \) . 由命题 17.8,可设 \( \alpha  : {S}^{n} \rightarrow  {S}^{n} \) 是光滑的. 于是可定义 \( \alpha \) 的度 \( \deg \alpha \) . 因为度是同伦不变量,所以可定义映射

\[
\deg  : {\pi }_{n}\left( {S}^{n}\right)  \rightarrow  \mathbb{Z}\text{ . } \tag{57}
\]

有以下两个关键引理.

引理 17.10.1. 映射 \( \deg  : {\pi }_{n}\left( {S}^{n}\right)  \rightarrow  \mathbb{Z} \) 是群同态,即

\[
\deg \left( {\left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack  }\right)  = \deg \left\lbrack  \alpha \right\rbrack   + \deg \left\lbrack  \beta \right\rbrack  .
\]

引理 17.10.2. 设 \( \alpha ,\beta  : {S}^{n} \rightarrow  {S}^{n} \) 且 \( \deg \alpha  = \deg \beta \) . 则 \( \alpha  \sim  \beta \) .

命题的证明. 只要证明 (57) 是同构. 设 \( \alpha  = \mathrm{{id}} : {S}^{n} \rightarrow  {S}^{n} \) . 则 \( \deg \left\lbrack  \alpha \right\rbrack   = 1 \) . 所以对任意 \( k \in  \mathbb{Z} \) ,由引理 17.10.1 知 \( \deg \left( {\left\lbrack  \alpha \right\rbrack  }^{k}\right)  = k \) . 因此 \( \deg \) 是满射. 单射由引理 17.10.2 可得. 这是因为若 \( \deg \left\lbrack  \alpha \right\rbrack   = 0 \) ,则 \( \alpha \) 零伦. 因此 \( \left\lbrack  \alpha \right\rbrack   = 0 \in  {\pi }_{n}\left( {S}^{n}\right) \) .

引理 17.10.1 的证明. 设 \( \left\lbrack  \alpha \right\rbrack  ,\left\lbrack  \beta \right\rbrack   \in  {\pi }_{n}\left( {S}^{n}\right) \) . 设 \( \alpha ,\beta  : {S}^{n} \rightarrow  {S}^{n} \) 是光滑的. 不妨设 \( \alpha ,\beta \) 是满射. 否则若 \( \alpha \) 不是满射,则 \( \deg \alpha  = 0 \) ,且由命题 17.9 的证明知 \( \alpha \) 零伦. 所以 \( \left\lbrack  \alpha \right\rbrack   = 0 \) . 此时 \( \left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack   = \left\lbrack  \beta \right\rbrack \) ,

\[
\deg \left( {\left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack  }\right)  = \deg \left\lbrack  \beta \right\rbrack   = \deg \left\lbrack  \alpha \right\rbrack   + \deg \left\lbrack  \beta \right\rbrack  .
\]

由 Sard 定理,存在点 \( P \in  {S}^{n} \) 是 \( \alpha ,\beta \) 的正则值. 由于 \( \alpha ,\beta \) 是满射,所以 \( {\alpha }^{-1}\left( P\right) \) 与 \( {\beta }^{-1}\left( P\right) \) 非空. 由于 \( {S}^{n} \) 紧, \( {\alpha }^{-1}\left( P\right) \) 与 \( {\beta }^{-1}\left( P\right) \) 是有限点集. 由反函数定理, \( \alpha \) 与 \( \beta \) 在正则点附近是局部微分同胚. 所以存在点 \( P \) 的一个邻域 \( U \) 使得 \( {\alpha }^{-1}\left( U\right) \) 由有限多个互不相交的开集 \( {U}_{1},\ldots ,{U}_{{r}_{\alpha }} \) 组成, \( {\beta }^{-1}\left( U\right) \) 由互不相交的开集 \( {V}_{1},\ldots ,{V}_{{r}_{\beta }} \) 组成. \( \alpha ,\beta \) 限制在各自的这些开集是到 \( U \) 的微分同胚:

\[
{\left. \alpha \right| }_{{U}_{i}} : {U}_{i}\overset{ \sim  }{ \rightarrow  }U,{\left. \;\beta \right| }_{{V}_{j}} : {V}_{j}\overset{ \sim  }{ \rightarrow  }U.
\]

现考虑 \( \alpha  : {S}^{n} \rightarrow  {S}^{n} \) . 在 \( {S}^{n} - U \) 内固定一点 \( Q \) ,设它为基点. \( {S}^{n} - U \) 可形变收缩到点 \( Q \) ,记此收缩为 \( {c}_{Q} \) . 它将 \( \bar{U} \) 形变为 (一个新的) \( {S}^{n} \) . 定义 \( \widetilde{\alpha } = {c}_{Q} \circ  \alpha  : {S}^{n} \rightarrow  {S}^{n} \) . 所以 \( \alpha \) 与 \( \widetilde{\alpha } \) 同伦,并且 \( \widetilde{\alpha } \) 具有性质:

\[
\widetilde{\alpha } : {U}_{i}\overset{ \sim  }{ \rightarrow  }{S}^{n} - Q,\;\widetilde{\alpha } : {S}^{n} - { \cup  }_{i = 1}^{{r}_{\alpha }}{U}_{i} \rightarrow  Q.
\]

![bo_d7e85t491nqc73eqefm0_635_578_604_1182_1053_0.jpg](images/fu_algebraic_topology_and_differential_forms_196_bod7e85t491nqc73eqefm0635578604118210530.jpg)

![bo_d7e85t491nqc73eqefm0_636_650_205_1044_937_0.jpg](images/fu_algebraic_topology_and_differential_forms_197_bod7e85t491nqc73eqefm063665020510449370.jpg)

不妨设 \( \widetilde{\alpha } \) 是光滑的. 由于 \( \deg \) 是同伦不变量,所以 \( \deg \alpha  = \deg \widetilde{\alpha } \) ,而

\[
\deg \widetilde{\alpha } = {\int }_{{S}^{n}}{\widetilde{\alpha }}^{ * }\eta  = \mathop{\sum }\limits_{{i = 1}}^{{r}_{\alpha }}{\int }_{{U}_{i}}{\widetilde{\alpha }}^{ * }\left( {\left. \eta \right| }_{{S}^{n} - Q}\right)  = \mathop{\sum }\limits_{{i = 1}}^{{r}_{\alpha }} \pm  1,
\]

其中 \( \left\lbrack  \eta \right\rbrack   \in  {H}^{n}\left( {S}^{n}\right) \) 是正的生成元. 这是因为 \( {\left. \widetilde{\alpha }\right| }_{{U}_{i}} : {U}_{i} \rightarrow  {S}^{n} - Q \) 是微分同胚,重数 \( \pm  1 \) 的符号由 \( {\left. \widetilde{\alpha }\right| }_{{U}_{i}} \) 是保定向还是反定向确定. 同理,存在光滑映射 \( \widetilde{\beta } : {S}^{n} \rightarrow  {S}^{n} \) 使得 \( \widetilde{\beta } \) 与 \( \beta \) 同伦并且具有性质:

\[
\widetilde{\beta } : {V}_{j}\overset{ \sim  }{ \rightarrow  }{S}^{n} - Q
\]

\[
\widetilde{\beta } : {S}^{n} - \mathop{\bigcup }\limits_{{j = 1}}^{{r}_{\beta }}{V}_{j} \rightarrow  Q
\]

所以

\[
\deg \widetilde{\beta } = {\int }_{{S}^{n}}{\widetilde{\beta }}^{ * }\eta  = \mathop{\sum }\limits_{{j = 1}}^{{r}_{\beta }}{\int }_{{V}_{j}}{\widetilde{\beta }}^{ * }\left( {\left. \eta \right| }_{{S}^{n} - Q}\right)  = \mathop{\sum }\limits_{{j = 1}}^{{r}_{\beta }} \pm  1.
\]

![bo_d7e85t491nqc73eqefm0_638_260_233_1814_745_0.jpg](images/fu_algebraic_topology_and_differential_forms_198_bod7e85t491nqc73eqefm063826023318147450.jpg)

于是

\[
\deg \left( {\left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack  }\right)  = \deg \left( {\left\lbrack  \widetilde{\alpha }\right\rbrack  \left\lbrack  \widetilde{\beta }\right\rbrack  }\right)  = \deg \left\lbrack  \widetilde{\gamma }\right\rbrack
\]

\[
= \left( {\mathop{\sum }\limits_{{i = 1}}^{{r}_{\alpha }} \pm  1}\right)  + \left( {\mathop{\sum }\limits_{{j = 1}}^{{r}_{\beta }} \pm  1}\right)
\]

\[
= \deg \left\lbrack  \widetilde{\alpha }\right\rbrack   + \deg \left\lbrack  \widetilde{\beta }\right\rbrack
\]

\[
= \deg \left\lbrack  \alpha \right\rbrack   + \deg \left\lbrack  \beta \right\rbrack  .
\]

引理 17.10.2 的证明概要. 继续考虑 \( \widetilde{\alpha } \) ,有以下

断言. 若 \( {U}_{i} \) 与 \( {U}_{j} \) 分别有重数 1 与 -1 . 则 \( \widetilde{\alpha } \) 同伦于 \( {\widetilde{\alpha }}^{\prime } \) ,它将 \( {U}_{i} \cup  {U}_{j} \) 映为点 \( Q \) .

用一条道路 \( \gamma \) 连接 \( {U}_{i} \) 与 \( {U}_{j} \) . 当 \( n = 1 \) 时,上述断言是容易理解的. 但当 \( n \geq  2 \) 时, 要说清楚着实不易, 这可见 Whitney 1937 年的论文, 具体要用到 CW 复形.

用上述断言中的方法可将 \( \widetilde{\alpha } \) 中成对的 \( \pm  1 \) 杀掉使得只剩下全是正的或全是负的或为零. 这样就证明了若 \( \deg \left\lbrack  \alpha \right\rbrack   =  \pm  k \) , 则存在 \( k \) 个互不相交的开集 \( {U}_{1},\ldots ,{U}_{k} \) 与 \( \widetilde{\alpha } : {S}^{n} \rightarrow  {S}^{n} \) 使得

(a) \( \widetilde{\alpha } \sim  \alpha \)

(b) \( \widetilde{\alpha } : {U}_{i}\overset{ \sim  }{ \rightarrow  }{S}^{n} - Q \)

(c) \( \widetilde{\alpha } : {S}^{n} - { \cup  }_{i = 1}^{k}{U}_{i} \rightarrow  Q \)

(d) \( \widetilde{\alpha } \) 在每个 \( {U}_{i} \) 上的重数全是 1 或是 -1 .

因此若 \( \deg \left\lbrack  \alpha \right\rbrack   = \deg \left\lbrack  \beta \right\rbrack \) ,则 \( \alpha \) 和 \( \beta \) 分别与上述的这种 \( \widetilde{\alpha } \) 和 \( \widetilde{\beta } \) 同伦. 显然 \( \widetilde{\alpha } \) 与 \( \widetilde{\beta } \) 同伦,因此 \( \alpha \) 与 \( \beta \) 同伦.

贴胞腔

设 \( {e}^{n} \) 是 \( n \) 维闭单位圆盘, \( {S}^{n - 1} = \partial {e}^{n} \) . 给定拓扑空间 \( X \) 与映射 \( f : {S}^{n - 1} \rightarrow  X \) . 由 \( f \) 贴 \( n \) 一胞腔到 \( X \) 得到空间 \( Y = X{ \cup  }_{f}{e}^{n} \) :

\[
Y = X{ \cup  }_{f}{e}^{n} = X \coprod  {e}^{n}/f\left( u\right)  \sim  u\text{ ,对 }u \in  {S}^{n - 1}\text{ . }
\]

例如贴一个 2-胞腔到一点 \( p \) 得到一个 2-维球面 \( {S}^{2} \) :

\[
{S}^{2} = \{ p\} { \cup  }_{f}{e}^{2},\;f : \partial {e}^{2} = {S}^{1} \rightarrow  p.
\]

![bo_d7e85t491nqc73eqefm0_640_132_924_1100_466_0.jpg](images/fu_algebraic_topology_and_differential_forms_199_bod7e85t491nqc73eqefm064013292411004660.jpg)

![bo_d7e85t491nqc73eqefm0_640_1340_927_840_461_0.jpg](images/fu_algebraic_topology_and_differential_forms_200_bod7e85t491nqc73eqefm064013409278404610.jpg)

![bo_d7e85t491nqc73eqefm0_641_533_617_1256_441_0.jpg](images/fu_algebraic_topology_and_differential_forms_201_bod7e85t491nqc73eqefm064153361712564410.jpg)

补充练习 1. 证明若映射 \( f, g : {S}^{n - 1} \rightarrow  X \) 同伦,则 \( X{ \cup  }_{f}{e}^{n} \) 与 \( X{ \cup  }_{g}{e}^{n} \) 也同伦. \( \square \)

贴胞腔的最基本性质是以下命题.

命题 17.11. 贴一个 \( n \) -胞腔到 \( X \) 不会改变它的维数小于 \( n - 1 \) 的同伦群,但可能杀死 \( {\pi }_{n - 1}\left( X\right) \) 中的元; 更精确地说,包含映射 \( i : X \rightarrow  X{ \cup  }_{f}{e}^{n} \) 诱导了同构

\[
{\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q}\left( {X{ \cup  }_{f}{e}^{n}}\right) \;\text{ 对 }q < n - 1
\]

与满射

\[
{\pi }_{n - 1}\left( X\right)  \rightarrow  {\pi }_{n - 1}\left( {X{ \cup  }_{f}{e}^{n}}\right) .
\]

例如设 \( X = {\mathbb{R}}^{2} - {D}^{2} \) . 则 \( {\pi }_{1}\left( X\right)  = \mathbb{Z} \) . 但若贴一个 2-胞腔到 \( X \) 把 \( {D}^{2} \) 填满,即 \( X{ \cup  }_{f}{e}^{2} = {\mathbb{R}}^{2} \) ,则 \( {\pi }_{1}\left( {X{ \cup  }_{f}{e}^{2}}\right)  = 0 \) . 这就是说贴一个 2-胞腔到 \( X \) 把 \( X \) 的第一同伦群, 即基本群消灭了. 证. 设 \( q \leq  n - 1 \) . 设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X{ \cup  }_{f}{e}^{n}}\right) \) . 由于维数的原因,有以下

断言. \( \alpha \) 同伦于某个映射 \( {\alpha }^{\prime } : {S}^{q} \rightarrow  X{ \cup  }_{f}{e}^{n} \) 使得 \( {\alpha }^{\prime }\left( {S}^{q}\right) \) 不包含 \( {e}^{n} \) 的所有点.

事实上,当 \( \alpha \) 是光滑映射而 \( X{ \cup  }_{f}{e}^{n} \) 是光滑流形时,这可由 Sard 定理直接得到. 这是因为 \( q \leq  n - 1 \) , \( \dim \left( {X{ \cup  }_{f}{e}^{n}}\right)  \geq  n \) ,所以 \( \alpha \) 的所有值是临界值,而由 Sard 定理, 临界值集是零测集. 对一般情形的证明留作习题.

根据断言不妨设 \( \alpha \left( {S}^{q}\right) \) 不包含 \( {e}^{n} \) 的所有点,如图中点 \( p \) . 固定一个从 \( {e}^{n} - p \) 到 \( \partial {e}^{n} \) 的收缩 \( {c}_{t} \) . 这给出了一个从 \( X{ \cup  }_{f}\left( {{e}^{n} - p}\right) \) 到 \( X \) 的收缩,不妨仍记作 \( {c}_{t} \) . 则 \( {c}_{t} \circ  \alpha  : {S}^{q} \rightarrow  X{ \cup  }_{f}{e}^{n} \) 定义了一个从 \( \alpha  = {c}_{0} \circ  \alpha \) 到 \( {\alpha }^{\prime } = {c}_{1} \circ  \alpha  : {S}^{q} \rightarrow  X \) 的同伦. 所以 \( {\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q}\left( {X{ \cup  }_{f}{e}^{n}}\right) \) 是满射. 现设 \( q \leq  n - 2 \) . 要证 \( {i}_{ * } \) 是单射. 设 \( \left\lbrack  \alpha \right\rbrack  ,\left\lbrack  \beta \right\rbrack   \in  {\pi }_{q}\left( X\right) \) 使得 \( {i}_{ * }\left\lbrack  \alpha \right\rbrack   = {i}_{ * }\left\lbrack  \beta \right\rbrack   \in \; {\pi }_{q}\left( {X{ \cup  }_{f}{e}^{n}}\right) \) . 设 \( F : {S}^{q} \times  I \rightarrow  X{ \cup  }_{f}{e}^{n} \) 是 \( i \circ  \alpha \) 与 \( i \circ  \beta \) 之间的同伦. 由于 \( \dim \left( {{S}^{q} \times  I}\right)  < n \) , 与断言相同可假定在 \( {e}^{n} \) 的内部存在一点 \( p \) 使得 \( p \notin  F\left( {{S}^{q} \times  I}\right) \) . 这样利用 \( {e}^{n} - p \) 到 \( \partial {e}^{n} \) 的收缩 \( {c}_{t} \) 得到映射

\[
{c}_{t} \circ  F : {S}^{q} \times  I \rightarrow  X{ \cup  }_{f}{e}^{n}
\]

![bo_d7e85t491nqc73eqefm0_643_648_1166_1028_535_0.jpg](images/fu_algebraic_topology_and_differential_forms_202_bod7e85t491nqc73eqefm0643648116610285350.jpg)

使得 \( {c}_{1} \circ  F : {S}^{q} \times  I \rightarrow  X \) 是 \( \alpha \) 与 \( \beta \) 在 \( X \) 中的同伦. 因此 \( \left\lbrack  \alpha \right\rbrack   = \left\lbrack  \beta \right\rbrack \) .

![bo_d7e85t491nqc73eqefm0_644_1187_839_1017_426_0.jpg](images/fu_algebraic_topology_and_differential_forms_203_bod7e85t491nqc73eqefm0644118783910174260.jpg)

在 \( \mathrm{X} \) 中同伦 \( {\mathrm{c}}_{1} \) 。 \( \mathrm{\;F} \)

p

\( \alpha \)

\( \beta \)

在 XUe 中同伦 F

补充练习 2 . 证明断言. 至于同调, 应用两个开集的同调 MV 序列 (15.6) 可得

命题 17.12. 由映射 \( f \) 贴一个 \( n \) -胞腔到拓扑空间 \( X \) 不改变维数除了 \( n \) 与 \( n - 1 \) 之外的同调. 记 \( {X}_{f} \) 为 \( X{ \cup  }_{f}{e}^{n} \) ,则有正合序列

\[
0 \rightarrow  {H}_{n}\left( X\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( {X}_{f}\right)  \rightarrow  \mathbb{Z}\overset{{f}_{ * }}{ \rightarrow  }{H}_{n - 1}\left( X\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n - 1}\left( {X}_{f}\right)  \rightarrow  0
\]

其中 \( {f}_{ * } : {H}_{n - 1}\left( {S}^{n - 1}\right)  \rightarrow  {H}_{n - 1}\left( X\right) \) 是诱导映射. 所以由包含 \( i : X \rightarrow  {X}_{f} \) 诱导的映射 \( {i}_{ * } \) 在 \( n \) 维时是单射,在 \( n - 1 \) 维时是满射. 证. 设 \( p = 0 \in  {e}^{n}, U = {X}_{f} - p, V = \left\{  {x \in  {e}^{n}\left| \right| x\parallel  < 1/2}\right\} \) . 则 \( U \) 与 \( X \) 同伦, \( V \) 可缩, \( U \cap  V \) 与 \( {S}^{n - 1} \) 同伦, 且 \( \{ U, V\} \) 是 \( {X}_{f} \) 的开覆盖. 根据对两个开集的同调 MV 序列, 我们有正合序列

\( \ldots  \rightarrow  {H}_{q}\left( {U \cap  V}\right)  \rightarrow  {H}_{q}\left( U\right)  \oplus  {H}_{q}\left( V\right)  \rightarrow  {H}_{q}\left( {X}_{f}\right)  \rightarrow  {H}_{q - 1}\left( {U \cap  V}\right)  \rightarrow  \ldots \)

\( \begin{matrix} \parallel & & \parallel & & \parallel \\  {H}_{q}\left( {S}^{n - 1}\right) & & {H}_{q}\left( X\right) & & {H}_{q - 1}\left( {S}^{n - 1}\right)  \end{matrix} \)

因此对 \( q \neq  n - 1 \) 或 \( n,{H}_{q}\left( X\right) \overset{ \sim  }{ \rightarrow  }{H}_{q}\left( {X}_{f}\right) \) . 对 \( q = n \) ,有正合序列

\[
0 \rightarrow  {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( {X}_{f}\right)  \rightarrow  \mathbb{Z} \rightarrow  {H}_{n - 1}\left( X\right)  \rightarrow  {H}_{n - 1}\left( {X}_{f}\right)  \rightarrow  0.
\]

一个 CW 复形 \( Y \) 是拓扑空间:它从一个点集出发通过相继贴维数从小到大的胞腔得到的集合,并被赋予弱拓扑: 子集 \( K \subset  Y \) 是闭的当且仅当 \( K \) 与每个胞腔的交集是闭集. 在 CW 复形 \( Y \) 中维数不超过 \( n \) 的胞腔组成 \( Y \) 的 \( n \) -骨架. 显然每个可三角剖分的空间是 CW 复形. 每个流形也是 CW 复形; 这在 Morse 理论的框架下最容易理解.

对我们来说 CW 复形的重要性来自于以下命题.

命题17.13. 每个 CW 复形同伦等价于一个有好覆盖的空间.

这个命题成立是因为每个 CW 复形与一个单纯复形有相同的伦型, 而单纯复形顶点的星形构成了它的一个好覆盖.

由这个命题可知前面发展的谱序列的整个机制可用于 CW 复形.

同伦与同调的关系同伦函子与同调函子的关系是非常敏感的. 存在自然同态

\[
i : {\pi }_{q}\left( X\right)  \rightarrow  {H}_{q}\left( X\right)
\]

它的定义如下: 固定 \( {H}_{q}\left( {S}^{q}\right) \) 的一个生成元 \( \left\lbrack  u\right\rbrack \) ,对每个 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( X\right) \) ,因为 \( \alpha  : {S}^{q} \rightarrow  X,\alpha \) 诱导了同态 \( {\alpha }_{ * } : {H}_{q}\left( {S}^{q}\right)  \rightarrow  {H}_{q}\left( X\right) \) ,所以定义

\[
i\left( \left\lbrack  \alpha \right\rbrack  \right)  = {\alpha }_{ * }\left( \left\lbrack  u\right\rbrack  \right) .
\]

一般来讲 \( i \) 既不是单射也不是满射.

我们已经看到 \( {H}_{q} \) 的计算相对容易,而 \( {\pi }_{q} \) 的计算十分困难,因为对 \( {\pi }_{q} \) 没有类似的 MV 原理. 由于这个原因, 以下两个定理是同伦论的基石.

定理 17.20. 设 \( X \) 是道路连通空间. 则

\[
{H}_{1}\left( X\right)  = {\pi }_{1}\left( X\right) /\left\lbrack  {{\pi }_{1}\left( X\right) ,{\pi }_{1}\left( X\right) }\right\rbrack
\]

其中 \( \left\lbrack  {{\pi }_{1}\left( X\right) ,{\pi }_{1}\left( X\right) }\right\rbrack \) 是 \( {\pi }_{1}\left( X\right) \) 的换位子群.

作为高维类比有

定理 17.21. (Hurewicz 同构定理) 设 \( X \) 是单连通的道路连通 CW 复形. 则它的第一个不等于零的同伦群与同调群在相同维数出现并且相等,即给定整数 \( n \geq  2 \) , 若对 \( 1 \leq  q < n,{\pi }_{q}\left( X\right)  = 0 \) ,则对 \( 1 \leq  q < n,{H}_{q}\left( X\right)  = 0 \) 且 \( {H}_{n}\left( X\right)  = {\pi }_{n}\left( X\right) \) . \( \square \)

证. 用归纳法. 设 \( n = 2 \) . 则道路纤维化

![bo_d7e85t491nqc73eqefm0_649_958_739_409_272_0.jpg](images/fu_algebraic_topology_and_differential_forms_205_bod7e85t491nqc73eqefm06499587394092720.jpg)

的同调谱序列的 \( {E}^{2} \) 页是

![bo_d7e85t491nqc73eqefm0_649_593_1202_1134_517_0.jpg](images/fu_algebraic_topology_and_differential_forms_204_bod7e85t491nqc73eqefm0649593120211345170.jpg)

回顾:

沿着定理 14.18 的路线,若 \( \pi  : E \rightarrow  X \) 是纤维为 \( F \) 的纤维丛并且若 \( X \) 是一个具有好覆盖的单连通空间,则存在一个收敛于奇异同调 \( {H}_{ * }\left( E\right) \) 的谱序列,它的 \( {E}^{2} \) 页是

\[
{E}_{p, q}^{2} = {H}_{p}\left( {X,{H}_{q}\left( F\right) }\right) .
\]

这对纤维化也成立. 由于 \( {\pi }_{1}\left( X\right)  = 0 \) ,由定理 17.20 知 \( {H}_{1}\left( X\right)  = 0 \) . 又由于 \( {PX} \) 可缩,所以 \( {H}_{2}\left( X\right) \) 与 \( {H}_{1}\left( {\Omega X}\right) \) 只能被杀死. 所以

\[
{d}^{2} : {H}_{2}\left( X\right)  \rightarrow  {H}_{1}\left( {\Omega X}\right)
\]

是同构. 于是

\[
{H}_{2}\left( X\right)  = {H}_{1}\left( {\Omega X}\right)
\]

\[
= {\pi }_{1}\left( {\Omega X}\right)
\]

因为 \( {\pi }_{1}\left( {\Omega X}\right)  = {\pi }_{2}\left( X\right) \) 是 abel 群,它的换位子群为零, 所以根据定理 17.20 可得

\[
= {\pi }_{2}\left( X\right) \text{ 根据同伦群的性质 }
\]

现设 \( n > 2 \) 且定理对 \( n - 1 \) 成立. 由假定对 \( 1 \leq  q < n,{\pi }_{q}\left( X\right)  = 0 \) ,所以对 \( 1 \leq  q < n - 1,{\pi }_{q}\left( {\Omega X}\right)  = {\pi }_{q + 1}\left( X\right)  = 0 \) ,特别地 \( {\Omega X} \) 是单连通的. 若 \( X \) 是道路连通的 CW 复形,则 \( {\Omega X} \) 也是道路连通的 CW 复形. 于是可应用归纳假定 \( n - 1 \) 于 \( {\Omega X} \) ,得

\[
{H}_{q}\left( {\Omega X}\right)  = 0\;\text{ 对 }1 \leq  q < n - 1
\]

\[
{H}_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n}\left( X\right) .
\]

此时道路纤维化的同调谱序列的 \( {E}^{2} \) 页是

![bo_d7e85t491nqc73eqefm0_652_417_482_1502_500_0.jpg](images/fu_algebraic_topology_and_differential_forms_206_bod7e85t491nqc73eqefm065241748215025000.jpg)

因为 \( {PX} \) 可缩, \( {d}^{q} : {E}_{q,0}^{q} \rightarrow  {E}_{0, q - 1}^{q} \) 是同构. 所以

\[
{H}_{q}\left( X\right)  = {H}_{q - 1}\left( {\Omega X}\right)  = 0\;\text{ 对 }1 \leq  q \leq  n - 1
\]

\[
{H}_{n}\left( X\right)  = {H}_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n}\left( X\right)
\]

注记 17.21.1. 细心的读者应该已经注意到这个看似简单的证明是有点问题的:因为我们只对具有好覆盖的空间发展了 Leray 谱序列, 即定理 15.11 与它的同调类比,所以我们必须验证 \( X \) 与 \( {\Omega X} \) 都有好覆盖. 根据 (17.13), CW 复形 \( X \) 与具有好覆盖的空间是同伦等价的. 而 Milnor 定理告诉我们 CW 复形的圈空间也是 CW 复形. 所以 \( {\Omega X} \) 也与具好覆盖的空间同伦等价.

事实上, Hurewicz 定理对任意道路连通的拓扑空间成立, 这是因为有 CW-逼近定理,它可叙述成如下我们需要的形式: 对任意拓扑空间 \( X \) ,存在一个 CW 复形 \( K \) 与映射 \( f : K \rightarrow  X \) ,它诱导了所有维数的同调与同伦的同构:

\[
{f}_{ * } : {\pi }_{q}\left( K\right) \overset{ \sim  }{ \rightarrow  }{\pi }_{q}\left( X\right) ,\;{f}_{ * } : {H}_{q}\left( K\right) \overset{ \sim  }{ \rightarrow  }{H}_{q}\left( X\right) .
\]

这样,在 Hurewicz 同构定理中可去掉 \( X \) 是 CW 复形的假定.

Hurewicz 同构定理的谱序列证明是由 Serre 给出的. 事实上, Serre 的方法略微不同；Serre 通过发展更具普遍性的谱序列以避开拓扑空间上好覆盖的存在性问题. 当然, 必须付出与之相应的代价; 人们不得不更努力地建立 Serre 谱序列.

Remark 17.21.1. A careful reader should have noticed that there is a sleight of hand in this deceptively simple proof: because we developed the Leray spectral sequence for spaces with a good cover (Theorem 15.11 and its homology analogue), to be strictly correct, we must show that both \( X \) and \( {\Omega X} \) have good covers. By (17.13), the CW complex \( X \) is homotopy equivalent to a space with a good cover. Next we quote the theorem of Milnor that the loop space of a CW complex is again a CW complex (Milnor [1, Cor. 3, p. 276]). So, at least up to homotopy, \( {\Omega X} \) also has a good cover.

Actually the Hurewicz theorem is true for any path-connected topological space. This is a consequence of the CW-approximation theorem which, in the form that we need, states that given any topological space \( X \) there is a CW complex \( K \) and a map \( f : K \rightarrow  X \) which induces isomorphisms \( {f}_{ * } : {\pi }_{q}\left( X\right) \overset{ \sim  }{ \rightarrow  }{\pi }_{q}\left( X\right) \) and \( {f}_{ * } : {H}_{q}\left( K\right) \overset{ \sim  }{ \rightarrow  }{H}_{q}\left( X\right) \) in all homotopy and homology (Whitehead [1, Ch. V, Section 3, p. 219]). Thus, in the Hurewicz isomorphism theorem, we may drop the requirement that \( X \) be a CW complex.

The spectral sequence proof of the Hurewicz isomorphism theorem is due to Serre [2, pp. 271-274]. Actually, Serre's approach is slightly different; by developing a spectral sequence which is valid in much greater generality than ours, Serre could bypass the question of the existence of a good cover on a topological space. Of course, a price has to be paid for this greater generality; one has to work much harder to establish Serre's spectral sequence.

作为 Hurewicz 定理的第一个且非常重要的例子,再次考虑 \( {S}^{n} \) 的同伦群. 从 Hurewicz 定理与 \( {S}^{n} \) 的同调立即得到 \( {S}^{n} \) 的低维同伦群

\[
{\pi }_{q}\left( {S}^{n}\right)  = 0\;\text{ 对 }q < n
\]

与

\[
{\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z}\text{ . }
\]

另一方面, 利用 Hopf 纤维化

![bo_d7e85t491nqc73eqefm0_656_894_917_536_303_0.jpg](images/fu_algebraic_topology_and_differential_forms_207_bod7e85t491nqc73eqefm06568949175363030.jpg)

的正合同伦序列可计算 \( {\pi }_{3}\left( {S}^{2}\right) \) . 事实上,利用 \( {S}^{1} \) 的覆盖 \( \pi  : \mathbb{R} \rightarrow  {S}^{1} \) 的正合同伦序列可得 \( {\pi }_{q}\left( {S}^{1}\right)  = 0 \) 对 \( q \geq  2 \) . 于是从正合同伦序列

\[
\cdots  \rightarrow  {\pi }_{q}\left( {S}^{1}\right)  \rightarrow  {\pi }_{q}\left( {S}^{3}\right)  \rightarrow  {\pi }_{q}\left( {S}^{2}\right)  \rightarrow  {\pi }_{q - 1}\left( {S}^{1}\right)  \rightarrow  \cdots
\]

我们得到 \( {\pi }_{q}\left( {S}^{3}\right)  = {\pi }_{q}\left( {S}^{2}\right) \) 对 \( q \geq  3 \) . 特别有 \( {\pi }_{3}\left( {S}^{2}\right)  = \mathbb{Z} \) .

作业:

1. 补充练习 1.

2. 补充练习 2.

代数拓扑与微分形式
