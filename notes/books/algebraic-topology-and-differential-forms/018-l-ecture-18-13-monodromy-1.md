#### 第18讲 Monodromy (1)

§13 Monodromy (1)

18. 单纯复形理论

在前一节看到秩 \( n \) 向量丛 \( E \) 的紧垂直上同调 \( {H}_{cv}^{ * }\left( E\right) \) 同构于 \( {H}^{* - n}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{n}}\right) \) ，即底流形 \( M \) 的好覆盖 \( \mathcal{U} \) 的系数在预层 \( {\mathcal{H}}_{cv}^{n} \) 的 Čech 上同调. 当预层 \( {\mathcal{H}}_{cv}^{n} \) 是常值预层 \( \mathbb{R} \) 时, \( {H}_{cv}^{ * }\left( E\right) \) 就可用底流形 \( M \) 的 de Rham 上同调 \( {H}^{* - n}\left( M\right) \) 表示. 此时 \( {H}_{cv}^{ * }\left( E\right) \) 的计算就被极大简化. 因此需确定在什么条件下一个局部常值预层如 \( {\mathcal{H}}_{cv}^{n} \) 是常值预层.

本节证明若连通拓扑空间的基本群平凡, 则它的任意好覆盖上的局部常值预层是常值预层. 这分为两个定理证明. 第一个定理是说若连通拓扑空间 \( X \) 的好覆盖 \( \mathcal{U} \) 的 nerve \( N\left( \mathcal{U}\right) \) (作为单纯复形) 的边路群 (edge path group) \( {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  = 0 \) , 则 \( \mathcal{U} \) 上局部常值预层是常值预层; 第二个定理是说 \( {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right) \) 同构于拓扑空间 \( X \) 的基本群 \( {\pi }_{1}\left( X\right) \) . 这次课讲第二个定理的证明,为此先对单纯复形的理论作简单的介绍. 下次课证明第一个定理并给出一些具体的例子.

- 单纯复形理论的简单介绍

- 关于基本群的一个定理

## 单纯复形理论的简单介绍

参考: M. A. Armstrong, Basic Topology, 孙以丰译.

- 设 \( {\sigma }_{n} \) 是 \( n \) -单纯形,它的 \( n + 1 \) 个顶点为 \( {v}_{0},{v}_{1},\ldots ,{v}_{n} \) . 对 \( n \) -单纯形有面的概念,如 \( {\sigma }_{2} \) 的面分为:

一 0 维的面,即顶点: \( {v}_{0},{v}_{1},{v}_{2} \) ;

-1 维的面,即边: \( \overline{{v}_{0}{v}_{1}},\overline{{v}_{0}{v}_{2}},\overline{{v}_{1}{v}_{2}} \) ;

-2 维的面,即面: \( \bigtriangleup {v}_{0}{v}_{1}{v}_{2} \) (包括内部).

![bo_d7e85t491nqc73eqefm0_402_498_875_407_422_0.jpg](images/fu_algebraic_topology_and_differential_forms_081_bod7e85t491nqc73eqefm04024988754074220.jpg)

![bo_d7e85t491nqc73eqefm0_402_1125_825_809_470_0.jpg](images/fu_algebraic_topology_and_differential_forms_080_bod7e85t491nqc73eqefm040211258258094700.jpg)

- 单纯复形 \( K \) 由满足以下条件的有限个单纯形组成:

— \( K \) 中每个单纯形的面也在 \( K \) 中;

— \( K \) 中任意两个单纯形 \( {\sigma }_{1},{\sigma }_{2} \) 或不相交或只相交于它们的公共面.

- \( n \) -单纯形 \( {\sigma }_{n} \) 的重心是

\[
\frac{{v}_{0} + {v}_{1} + \cdots  + {v}_{n}}{n + 1}
\]

![bo_d7e85t491nqc73eqefm0_403_1413_397_414_456_0.jpg](images/fu_algebraic_topology_and_differential_forms_082_bod7e85t491nqc73eqefm040314133974144560.jpg)

\( {\mathrm{v}}_{0} \; {\mathrm{v}}_{1} \)

\( {\sigma }_{0} \; {\sigma }_{1} \)

- 单纯形 \( {\sigma }_{n} \) 的第一次重心重分是一个单纯复形,它以 \( {\sigma }_{n} \) 的所有面的重心作为顶点. 例如单纯形 \( {\sigma }_{2} \) 的重心重分是单纯复形 \( K \) ,它由以下单纯形组成:

-7 个 0 一单纯形: \( {v}_{0},{v}_{1},{v}_{2},{v}_{01},{v}_{02},{v}_{12},{v}_{012} \) ;

— 12 个 1-单纯形: \( \overline{{v}_{0}{v}_{01}},\overline{{v}_{0}{v}_{02}},\overline{{v}_{1}{v}_{01}},\overline{{v}_{1}{v}_{12}},\overline{{v}_{2}{v}_{02}},\overline{{v}_{2}{v}_{12}},\overline{{v}_{0}{v}_{012}} \) , \( \overline{{v}_{1}{v}_{012}},\overline{{v}_{2}{v}_{012}},\overline{{v}_{01}{v}_{012}},\overline{{v}_{02}{v}_{012}},\overline{{v}_{12}{v}_{012}}; \)

— 6 个 2-单纯形: \( \bigtriangleup {v}_{0}{v}_{01}{v}_{012},\bigtriangleup {v}_{0}{v}_{02}{v}_{012},\bigtriangleup {v}_{1}{v}_{01}{v}_{012},\bigtriangleup {v}_{1}{v}_{12}{v}_{012} \) , \( \bigtriangleup {v}_{2}{v}_{12}{v}_{012},\bigtriangleup {v}_{2}{v}_{02}{v}_{012}. \)

- 一个单纯复形 \( K \) 的第一次重心重分是将 \( K \) 的所有单纯形作第一次重心重分得到的新单纯复形 \( {K}^{\prime } \) :

![bo_d7e85t491nqc73eqefm0_404_774_462_893_514_0.jpg](images/fu_algebraic_topology_and_differential_forms_083_bod7e85t491nqc73eqefm04047744628935140.jpg)

- \( K \) 的支撑(Support) \( \left| K\right| \) 是 \( K \) 的所有单纯形的并集(点集). 显然, \( \left| K\right|  = \; \left| {K}^{\prime }\right| .K \) 的 \( k \) -骨架(skeleton)是由 \( K \) 的所有维数小于等于 \( k \) 的单纯形组成的单纯复形. 顶点为 \( v \) 的星形 (star) st( \( v \) ) 是 \( K \) 中所有以 \( v \) 为顶点的单纯形的并集，它是 \( \left| K\right| \) 的闭子集. 例如前面图中单纯复形 \( K \) 的顶点 \( {v}_{0} \) 的星形是

\[
\operatorname{st}\left( {v}_{0}\right)  =  \vartriangle  {v}_{0}{v}_{1}{v}_{2} \cup  \overline{{v}_{0}{v}_{4}}.
\]

注记13.3. 两个单纯复形 \( K \) 与 \( L \) 之间的一个单纯映射是一个从 \( K \) 的顶点到 \( L \) 的顶点的映射 \( f \) 使得若 \( {v}_{0},\ldots ,{v}_{n} \) 张成 \( K \) 中一个单形,则 \( f\left( {v}_{0}\right) ,\ldots , f\left( {v}_{n}\right) \) 张成 \( L \) 中一个单形. 注意当 \( i \neq  j \) 时,可能 \( f\left( {v}_{i}\right)  = f\left( {v}_{j}\right) \) .

通过线性扩张,单纯映射 \( f \) 诱导了映射 \( f : \left| K\right|  \rightarrow  \left| L\right| \) :

\[
f\left( {\mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}{v}_{i}}\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}f\left( {v}_{i}\right) ,\;\text{ 其中 }\mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i} = 1,{\lambda }_{i} \geq  0.
\]

它把 \( K \) 的每个单纯形线性地映满 \( L \) 的某个单纯形. 我们也把这样的映射称为单纯映射.

- 设 \( K \) 是一个单纯复形. \( K \) 上一个圈 (loop) 是由 \( K \) 中首尾相连的 1-单纯形组成的. \( K \) 上一个边圈(bounding loop)是由 \( K \) 中一些 2-单纯形的边组成的圈.

如在下图的单纯复形 \( K \) 中,单纯形 \( \overline{{v}_{0}{v}_{4}},\overline{{v}_{4}{v}_{3}},\overline{{v}_{3}{v}_{2}},\overline{{v}_{2}{v}_{0}} \) 组成一个圈,记作 \( {v}_{0}{v}_{4}{v}_{3}{v}_{2}{v}_{0} \) . 它是一个以 \( {v}_{0} \) 为基点的圈. 它不是边圈. 单纯形 \( \overline{{v}_{0}{v}_{1}},\overline{{v}_{1}{v}_{3}} \) , \( \overline{{v}_{3}{v}_{2}},\overline{{v}_{2}{v}_{0}} \) 组成一个以 \( {v}_{0} \) 为顶点的边圈 \( {v}_{0}{v}_{1}{v}_{3}{v}_{2}{v}_{0} \) .

![bo_d7e85t491nqc73eqefm0_406_808_766_846_489_0.jpg](images/fu_algebraic_topology_and_differential_forms_084_bod7e85t491nqc73eqefm04068087668464890.jpg)

为了方便,约定在一个圈中的1-单纯形是可以退化的,即 0-单纯形是可以重复相继出现的,如圈 \( {v}_{0}{v}_{4}{v}_{3}{v}_{3}{v}_{2}{v}_{0} \) ,它等于圈 \( {v}_{0}{v}_{4}{v}_{3}{v}_{2}{v}_{0} \) . 边圈中的 2-单纯形也是可以退化的,如 \( {v}_{0}{v}_{1}{v}_{0} = {v}_{0}{v}_{1}{v}_{1}{v}_{0} \) 是一个边圈.

- 两个以 \( {v}_{0} \) 为顶点的圈是等价的若它们相差一个边圈. 这样圈 \( {v}_{0} \) 与圈 \( {v}_{0}{v}_{1}{v}_{0} \) 是等价的. 上图中的圈 \( {v}_{0}{v}_{4}{v}_{3}{v}_{1}{v}_{2}{v}_{0} \) 与圈 \( {v}_{0}{v}_{4}{v}_{3}{v}_{2}{v}_{0} \) 是等价的:

\[
{v}_{0}{v}_{4}{v}_{3}{v}_{1}{v}_{2}{v}_{0} \sim  {v}_{0}{v}_{4}{v}_{3}{v}_{1}{v}_{2}{v}_{3}{v}_{2}{v}_{0} \sim  {v}_{0}{v}_{4}{v}_{3}{v}_{2}{v}_{0},
\]

它们分别相差一个边圈 \( {v}_{2}{v}_{3}{v}_{2} \) 与 \( {v}_{3}{v}_{1}{v}_{2}{v}_{3} \) .

单纯复形 \( K \) 的以 \( {v}_{0} \) 为基点的边路群 (edge path group) 定义为

\[
{\pi }_{1}\left( K\right)  = \frac{\left\{  \text{ 所有以 }{v}_{0}\text{ 为基点的圈 }\right\}  }{\{ \text{ 所有边圈 }\} }.
\]

- 我们有以下事实:

(a) \( {\pi }_{1}\left( K\right)  = {\pi }_{1}\left( {K}_{2}\right) \) ,其中 \( {K}_{2} \) 是 \( K \) 的 2-骨架;

(b) \( {\pi }_{1}\left( K\right)  \simeq  {\pi }_{1}\left( \left| K\right| \right) \)

(c)(单纯逼近定理)设 \( K \) , \( L \) 是单纯复形. 任意映射 \( f : \left| K\right|  \rightarrow  \left| L\right| \) 同伦于某个单纯映射 \( g : \left| {K}^{\left( k\right) }\right|  \rightarrow  \left| L\right| \) ,此处 \( {K}^{\left( k\right) } \) 是 \( K \) 的 \( k \) 次重心重分.

这些事实基于以下来自障碍理论的非常直观的原理.

延拓原理. 设 \( {I}^{n} \) 是 \( n \) 维方体, \( X \) 是可缩拓扑空间. 则任意映射 \( f : \partial {I}^{n} \rightarrow  X \) 可延拓定义在整个 \( {I}^{n} \) 上,即存在映射 \( g : {I}^{n} \rightarrow  X \) 使得 \( {\left. g\right| }_{\partial {I}^{n}} = f \) .

旁白. 可把条件 \( X \) 是可缩空间减弱为对所有的 \( q \leq  n - 1 \) , \( X \) 的第 \( q \) 个同伦群 \( {\pi }_{q}\left( X\right)  = 0. \) 拓扑空间 \( X \) 的开覆盖 \( \mathcal{U} \) 称为好覆盖若其任意非空有限交是可缩的.

注记. 在流形上有两个好覆盖的概念. 注意这两个概念是不等价的. 把非紧无边的流形称为开流形. 存在可缩但不微分同胚于 \( {\mathbb{R}}^{3} \) 的开三维流形. 1935 年 J. H. C. Whitehead 发现了第一个这种例子. 1962 年 D. R. McMillan 构造了无穷多个例子. 一个流形的开覆盖是好覆盖，我们总是指其有限非空交微分同胚于 \( {\mathbb{R}}^{n} \) . 这是因为在证 Poincaré 对偶时，不论是用第 5 节的 MV 方法还是用第 12 节的 tic-tac-toe 引理, 都需要紧 Poincaré 引理 (推论 4.7) . 它对仅与 \( {\mathbb{R}}^{n} \) 同伦的开集不一定成立, 因为紧上同调不是同伦不变量.

Remark. Thus, on a manifold there are two notions of a good cover. These two notions are not equivalent. Let us call a noncompact boundaryless manifold an open manifold. Then there are contractible open 3-manifolds not homeomorphic to \( {\mathbb{R}}^{3} \) . In 1935 J. H. C. Whitehead found the first example of such a manifold [ ]. D. R. McMillan, Jr. constructed infinitely many more in [ ]. For an open cover on a manifold to be a good cover we will always require the most restrictive hypothesis that the finite nonempty intersections be diffeomorphic to \( {\mathbb{R}}^{n} \) , This is because in order to prove Poincaré duality, whether by the Mayer-Vietoris argument of Section 5 or by the tic-tac-toe game of Section 12, we need the compact Poincaré lemma, which is not always true for an open set with merely the homotopy type of \( {\mathbb{R}}^{n} \) .

关于基本群的一个定理

定理 13.4. 设拓扑空间 \( X \) 有好覆盖 \( \mathcal{U}, N\left( \mathcal{U}\right) \) 是 \( \mathcal{U} \) 的 nerve. 则

\[
{\pi }_{1}\left( X\right)  \simeq  {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)
\]

证. 记 \( {N}_{2}\left( \mathcal{U}\right) \) 为 \( N\left( \mathcal{U}\right) \) 的 2-骨架, \( {N}_{2}^{\prime }\left( \mathcal{U}\right) \) 为 \( {N}_{2}\left( \mathcal{U}\right) \) 的重心重分. 边 \( \overline{{U}_{i}{U}_{j}} \) 的重心记为 \( {U}_{ij} \) ,面 \( \bigtriangleup {U}_{i}{U}_{j}{U}_{k} \) 的重心记为 \( {U}_{ijk} \) .

![bo_d7e85t491nqc73eqefm0_411_302_796_582_479_0.jpg](images/fu_algebraic_topology_and_differential_forms_087_bod7e85t491nqc73eqefm04113027965824790.jpg)

![bo_d7e85t491nqc73eqefm0_411_1063_815_402_353_0.jpg](images/fu_algebraic_topology_and_differential_forms_085_bod7e85t491nqc73eqefm041110638154023530.jpg)

\( {\mathrm{N}}_{2}\left( \underline{\mathrm{U}}\right) \)

![bo_d7e85t491nqc73eqefm0_411_1594_821_404_364_0.jpg](images/fu_algebraic_topology_and_differential_forms_086_bod7e85t491nqc73eqefm041115948214043640.jpg)

\( {\mathrm{N}}_{2}{}^{\prime }\left( \underline{\mathrm{U}}\right) \)

以下定义映射 \( f : \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right|  \rightarrow  X \) 并证明它诱导基本群的同构. 这样,结合事实 (a) 与 (b) 可完成定理的证明:

\[
{\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  \simeq  {\pi }_{1}\left( {{N}_{2}\left( \mathcal{U}\right) }\right)  \simeq  {\pi }_{1}\left( \left| {{N}_{2}\left( \mathcal{U}\right) }\right| \right)  = {\pi }_{1}\left( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \right)  \simeq  {\pi }_{1}\left( X\right) .
\]

第一步: 定义 \( f : \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right|  \rightarrow  X \) .

为此在 \( \mathcal{U} \) 的每个开集 \( {U}_{i} \) 中固定一点 \( {p}_{i} \) ,在非空交 \( {U}_{ij} \) 中固定一点 \( {p}_{ij} \) ,在非空交 \( {U}_{ijk} \) 中固定一点 \( {p}_{ijk} \) . 由于 \( \mathcal{U} \) 是好覆盖, \( {U}_{i} \) 与 \( {U}_{ij} \) 可缩,分别固定一个收缩映射 \( {c}_{i} : {U}_{i} \rightarrow  {p}_{i} \) 与 \( {c}_{ij} : {U}_{ij} \rightarrow  {p}_{ij} \) . 于是对任意的 \( p \in  {U}_{i} \) ,由 \( {c}_{i} \) 定义了一条从 \( p \) 到 \( {p}_{i} \) 的道路,记作 \( {\sigma }_{i}\left( {p \rightarrow  {p}_{i}}\right) \) ; 对任意的 \( p \in  {U}_{ij} \) ,由 \( {c}_{ij} \) 定义了一条从 \( p \) 到 \( {p}_{ij} \) 的道路, 记作 \( {\sigma }_{ij}\left( {p \rightarrow  {p}_{ij}}\right) \) .

![bo_d7e85t491nqc73eqefm0_412_794_894_787_676_0.jpg](images/fu_algebraic_topology_and_differential_forms_088_bod7e85t491nqc73eqefm04127948947876760.jpg)

(i) 如左下图,定义从 \( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 的顶点到 \( X \) 的映射 \( f \) :

\[
f\left( {U}_{i}\right)  = {p}_{i},\;f\left( {U}_{ij}\right)  = {p}_{ij},\;f\left( {U}_{ijk}\right)  = {p}_{ijk}.
\]

![bo_d7e85t491nqc73eqefm0_413_479_468_1390_626_0.jpg](images/fu_algebraic_topology_and_differential_forms_089_bod7e85t491nqc73eqefm041347946813906260.jpg)

(ii) 如右上图,定义从 \( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 的边到 \( X \) 的映射 \( f \) :

\[
f\left( \overline{{U}_{ij}{U}_{i}}\right)  = {\sigma }_{i}\left( {{p}_{ij} \rightarrow  {p}_{i}}\right)
\]

\[
f\left( \overline{{U}_{ijk}{U}_{i}}\right)  = {\sigma }_{i}\left( {{p}_{ijk} \rightarrow  {p}_{i}}\right)
\]

\[
f\left( \overline{{U}_{ijk}{U}_{ij}}\right)  = {\sigma }_{ij}\left( {{p}_{ijk} \rightarrow  {p}_{ij}}\right) .
\]

(iii) 定义从 \( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 的面到 \( X \) 的映射 \( f \) . 给定面 \( \bigtriangleup {U}_{i}{U}_{ij}{U}_{ijk} \) . \( f \) 已对它的顶点与边有定义,并且像集包含在开集 \( {U}_{i} \) 中. 所以对任意点 \( Y \in  {U}_{ij}{U}_{ijk} \) , \( f\left( Y\right)  \in  {U}_{i} \) . 定义映射

\[
f : \overline{Y{U}_{i}} \rightarrow  {\sigma }_{i}\left( {f\left( Y\right)  \rightarrow  {p}_{i}}\right) .
\]

这就定义了从面 \( \bigtriangleup {U}_{i}{U}_{ij}{U}_{ijk} \) 到 \( X \) 的映射 \( f \) ，并且它的像恰好是一个曲边三角形 \( \bigtriangleup  {p}_{i}{p}_{ij}{p}_{ijk} \) . 这种曲边三角形有时可能是退化的,即它可能仅为一个点或一条曲线.

![bo_d7e85t491nqc73eqefm0_414_839_912_658_629_0.jpg](images/fu_algebraic_topology_and_differential_forms_090_bod7e85t491nqc73eqefm04148399126586290.jpg)

第二步: 证明 \( {f}_{ * } : {\pi }_{1}\left( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \right)  \rightarrow  {\pi }_{1}\left( X\right) \) 是满射. 将 \( {p}_{0} \in  {U}_{0} \) 作为 \( X \) 的基点. 设 \( \gamma  : {S}^{1} \rightarrow  X \) 是一个以 \( {p}_{0} \) 为基点的圈. 需作一个以 \( {U}_{0} \) 为基点的圈 \( \overline{\gamma } : {S}^{1} \rightarrow  \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 使得 \( f \circ  \overline{\gamma } \) 定点同伦于 \( \gamma \) .

设 \( {S}^{1} = I/\partial I \) . 将它 \( n \) 等分,变成一个单纯复形 \( K \) ,顶点为 \( {q}_{0},{q}_{1},\ldots ,{q}_{n} = {q}_{0} \) . 再将 \( K \) 重心重分,得 \( {K}^{\prime } \) . 当 \( n \) 充分大时, \( \gamma \) 将 \( {q}_{i} \in  K \) 在 \( {K}^{\prime } \) 中的星形 \( \operatorname{st}\left( {q}_{i}\right) \) 映到某个 \( {U}_{\alpha \left( i\right) } \) :

\[
\gamma \left( {\operatorname{st}\left( {q}_{i}\right) }\right)  \subset  {U}_{\alpha \left( i\right) }. \tag{45}
\]

记 \( {q}_{i}{q}_{i + 1} \) 的中点为 \( {q}_{i, i + 1} \) . 由包含 (45) 可知

\[
\gamma \left( {q}_{i, i + 1}\right)  \in  {U}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) }.
\]

![bo_d7e85t491nqc73eqefm0_415_177_1203_1960_508_0.jpg](images/fu_algebraic_topology_and_differential_forms_091_bod7e85t491nqc73eqefm0415177120319605080.jpg)

定义 \( \overline{\gamma } : {S}^{1} \rightarrow  \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 通过定义

\[
\overline{\gamma }\left( \overline{{q}_{i}{q}_{i + 1}}\right)  = \overline{{U}_{\alpha \left( i\right) }{U}_{\alpha \left( {i + 1}\right) }}
\]

并要求

\[
\overline{\gamma }\left( {q}_{i, i + 1}\right)  = {U}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) }.
\]

于是

\[
f \circ  \overline{\gamma }\left( {q}_{i}\right)  = {p}_{\alpha \left( i\right) },\;f \circ  \overline{\gamma }\left( {q}_{i, i + 1}\right)  = {p}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) }.
\]

注意若 \( \alpha \left( i\right)  = \alpha \left( {i + 1}\right) \) ,则 \( {p}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) } = {p}_{\alpha \left( i\right) } \) . 需证 \( \gamma \) 与 \( f \circ  \overline{\gamma } \) 定点同伦,即需构造映射 \( F : {I}^{2} \rightarrow  X \) 使得

\[
F\left( {s,0}\right)  = \gamma \left( s\right) ,\;F\left( {s,1}\right)  = \left( {f \circ  \overline{\gamma }}\right) \left( s\right) ,\;F\left( {0, t}\right)  = F\left( {1, t}\right)  = {p}_{0}.
\]

这就是说,若 \( {\left. F\right| }_{\partial {I}^{2}} \) 已由上述三个等式定义,我们要将它延拓到整个 \( {I}^{2} \) . 为此将 \( {I}^{2} \) 按单纯复形 \( {K}^{\prime } \) 的顶点进行垂直分割.

因为

\[
F\left( {{q}_{i},0}\right)  = \gamma \left( {q}_{i}\right)  \in  {U}_{\alpha \left( i\right) }
\]

\[
F\left( {{q}_{i},1}\right)  = \left( {f \circ  \overline{\gamma }}\right) \left( {q}_{i}\right)  = {p}_{\alpha \left( i\right) } \in  {U}_{\alpha \left( i\right) },
\]

由收缩 \( {c}_{\alpha \left( i\right) } \) 定义了一条从 \( \gamma \left( {q}_{i}\right) \) 到 \( {p}_{\alpha \left( i\right) } \) 的道路. 将此道路定义为 \( \left\{  {q}_{i}\right\}   \times  I \) 在 \( F \) 下的像.

由包含(45)知

\[
F\left( {{q}_{i, i + 1},0}\right)  = \gamma \left( {q}_{i, i + 1}\right)  \in  {U}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) },
\]

\[
F\left( {{q}_{i, i + 1},1}\right)  = \left( {f \circ  \overline{\gamma }}\right) \left( {q}_{i, i + 1}\right)  = {p}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) } \in  {U}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) }.
\]

由收缩 \( {c}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) } \) 定义了一条从 \( \gamma \left( {q}_{i, i + 1}\right) \) 到 \( {p}_{\alpha \left( i\right) \alpha \left( {i + 1}\right) } \) 的道路. 将此道路定义为 \( \left\{  {q}_{i, i + 1}\right\}   \times  I \) 在 \( F \) 下的像.

![bo_d7e85t491nqc73eqefm0_418_994_491_1038_605_0.jpg](images/fu_algebraic_topology_and_differential_forms_093_bod7e85t491nqc73eqefm041899449110386050.jpg)

![bo_d7e85t491nqc73eqefm0_418_317_493_622_517_0.jpg](images/fu_algebraic_topology_and_differential_forms_092_bod7e85t491nqc73eqefm04183174936225170.jpg)

\( {q}_{i}\;{q}_{i, i + 1} \)

这样我们已在每个小长方形的边界定义了 \( F \) ，且 \( F \) 将其映到某个可缩空间 \( {U}_{\alpha }\left( i\right) \) : 根据延拓原理, 可将 \( F \) 的定义延拓到每个小长方形, 这样也就延拓到整个 \( {I}^{2} \) .

第三步: 证明 \( {f}_{ * } : {\pi }_{1}\left( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \right)  \rightarrow  {\pi }_{1}\left( X\right) \) 是单射.

设 \( \overline{\gamma } : I \rightarrow  \left| {{N}_{2}\left( \mathcal{U}\right) }\right| \) 是一个以 \( {U}_{0} \) 为基点的圈使得 \( \gamma  = f \circ  \overline{\gamma } \) 在 \( X \) 中零伦,即存在如下图所示的映射 \( H : {I}^{2} \rightarrow  X \) .

![bo_d7e85t491nqc73eqefm0_419_901_640_525_548_0.jpg](images/fu_algebraic_topology_and_differential_forms_094_bod7e85t491nqc73eqefm04199016405255480.jpg)

记 \( {I}^{2} \) 的上边为 \( L,\overline{\gamma } : L \rightarrow  \left| {{N}_{2}\left( \mathcal{U}\right) }\right| \) . 由单纯逼近定理,不妨设 \( L \) 是 \( I = \left\lbrack  {0,1}\right\rbrack \) 经多次重心重分得到的单纯复形,而 \( \overline{\gamma } \) 是单纯映射: 若 \( {q}_{i} \) 是 \( L \) 的顶点,则 \( \gamma \left( {q}_{i}\right) \) 是 \( {N}_{2}\left( \mathcal{U}\right) \) 的顶点 \( {U}_{\alpha \left( i\right) } \) . 将 \( {I}^{2} \) 不断重心重分得到它的一个三角剖分 \( K \) ，它具有以下性质:

(1)若 \( {q}_{i} \) 是 \( K \) 的一个顶点,而 \( \operatorname{st}\left( {q}_{i}\right) \) 是 \( {q}_{i} \) 在 \( K \) 的重心重分 \( {K}^{\prime } \) 中的 star,则

\[
H\left( {\operatorname{st}\left( {q}_{i}\right) }\right)  \subset  {U}_{\alpha \left( i\right) }, \tag{46}
\]

其中 \( {U}_{\alpha \left( i\right) } \) 是开覆盖 \( \mathcal{U} \) 中的开集. 对每点 \( {q}_{i} \) ,固定 \( {U}_{\alpha \left( i\right) } \) .

(2)单纯复形 \( L \) 新增加的顶点仅是通过对其 1-单纯形不断平分得到.

定义单纯映射

\[
\bar{H} : {I}^{2} = \left| K\right|  \rightarrow  \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right|
\]

如下:

(1)若 \( {q}_{i} \) 是 \( L \) 的顶点,则 \( \bar{H}\left( {q}_{i}\right)  = \overline{\gamma }\left( {q}_{i}\right)  = {U}_{\alpha \left( i\right) } \) ;

(2) \( \bar{H} \) 将 \( L \) 上 1-单纯形 \( \overline{{q}_{i}{q}_{i + 1}} \) 的中点映为 1-单纯形 \( \overline{\overline{\gamma }\left( {q}_{i}\right) \overline{\gamma }\left( {q}_{i + 1}\right) } \) 的中点；

(3) 若 \( {q}_{k} \) 是 \( L \) 上新增加的顶点,它落在 1-单纯形 \( \overline{{q}_{i}{q}_{i + 1}} \) 上且在中点 \( {q}_{i, i + 1} \) 的左边,则 \( \bar{H}\left( {q}_{k}\right)  = \overline{\gamma }\left( {q}_{i}\right) \) ,若在 \( {q}_{i, i + 1} \) 的右边,则 \( \bar{H}\left( {q}_{k}\right)  = \overline{\gamma }\left( {q}_{i + 1}\right) \) ;

(4) \( \bar{H} \) 将 \( \partial {I}^{2} - L \) 上的顶点映为 \( \overline{\gamma }\left( {q}_{0}\right)  = {U}_{0} \) ，它是 \( \overline{\gamma } \) 的基点；

(5) \( \bar{H} \) 将 \( {I}^{2} - \partial {I}^{2} \) 的顶点 \( {q}_{i} \) 映为 (46) 中的 \( {U}_{\alpha \left( i\right) } \) ,视其为 \( {N}_{2}\left( \mathcal{U}\right) \) 的顶点.

令 \( \beta  = {\left. \bar{H}\right| }_{L} \) . 根据构造, \( \beta \) 与 \( \overline{\gamma } \) 在 \( L \) 的顶点有相同的定义, \( \beta \) 与 \( \overline{\gamma } \) 在 \( \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right| \) 中同伦; 又根据构造, \( \bar{H} \) 定义了 \( \beta \) 的一个零伦. 所以 \( \overline{\gamma } \sim  \beta  \sim  0,{f}_{ * } \) 是单射.

代数拓扑与微分形式
