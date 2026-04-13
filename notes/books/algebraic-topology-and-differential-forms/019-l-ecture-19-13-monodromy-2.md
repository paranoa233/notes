#### 第19讲 Monodromy (2)

§13 Monodromy (2)

19. 单值性这节课的主要目的是证明以下

定理. 若连通拓扑空间 \( X \) 的好覆盖 \( \mathcal{U} \) 的 nerve \( N\left( \mathcal{U}\right) \) 的边路群 \( {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  = 0 \) , 则 \( \mathcal{U} \) 上局部常值预层是常值预层.

在讲这个定理的证明之前，我们先回忆好覆盖 \( \mathcal{U} \) 上预层，局部常值预层与常值预层的定义; 接着给出局部常值预层 \( G \) 的单值表示,即同态 \( \rho  : {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  \rightarrow  \operatorname{Aut}\left( G\right) \) , 其中 \( \operatorname{Aut}\left( G\right) \) 是 \( G \) 的自同构群. 当所有的概念都弄清时,上述定理的证明就显得十分简单. 最后给出一些单值性的例子.

- 好覆盖 \( \mathcal{U} \) 上常值预层与局部常值预层

- 单值表示

- 单值性的例子

设 \( X \) 是拓扑空间.

- \( X \) 上一个预层 \( \mathcal{F} \) 是指: 对 \( X \) 的每个开集 \( U \subset  X \) 赋予一个 abel 群 \( \mathcal{F}\left( U\right) \) , 对 \( X \) 的任意开集的包含 \( V \subset  U \) 赋予群同态

\[
{\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right)
\]

并且满足以下条件:

(a) \( {\rho }_{U}^{U} = \mathrm{{id}} \)

(b) 若 \( W \subset  V \subset  U \) ,则 \( {\rho }_{W}^{V} \circ  {\rho }_{V}^{U} = {\rho }_{W}^{U} \) .

\( {\rho }_{V}^{U} \) 称之为限制.

- \( X \) 上预层 \( \mathcal{F} \) 称之为取值于 abel 群 \( G \) 的常值预层,若对 \( X \) 的任意开集 \( U \) , \( \mathcal{F}\left( U\right) \) 是 \( U \) 上取值于 \( G \) 的局部常值函数的全体,并且若对 \( X \) 的任意开集的包含 \( V \subset  U \) ,限制映射 \( {\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) 是通常函数的限制.

- 设 \( \mathcal{F},\mathcal{G} \) 是 \( X \) 上预层. 若对 \( X \) 的任意开集 \( U \) ,存在同态

\[
{f}_{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{G}\left( U\right)
\]

使得对任意开集的包含 \( V \subset  U \) 有以下交换图表:

![bo_d7e85t491nqc73eqefm0_426_951_568_537_365_0.jpg](images/fu_algebraic_topology_and_differential_forms_096_bod7e85t491nqc73eqefm04269515685373650.jpg)

则同态的集类 \( \left\{  {f}_{U}\right\} \) 称为从预层 \( \mathcal{F} \) 到 \( \mathcal{G} \) 的一个同态,记作 \( f : \mathcal{F} \rightarrow  \mathcal{G} \) . 如果每个同态 \( {f}_{U} \) 是同构,则称同态 \( f \) 为预层 \( \mathcal{F},\mathcal{G} \) 之间的同构. 存在同构映射的两个预层 \( \mathcal{F},\mathcal{G} \) 称为同构的预层,记作 \( \mathcal{F} \simeq  \mathcal{G} \) .

断言 1. 设 \( \mathcal{U} \) 是 \( X \) 的开覆盖, \( \mathcal{F} \) 与 \( \mathcal{G} \) 是 \( X \) 上预层. 若 \( \mathcal{F} \simeq  \mathcal{G} \) ,则 Čech 上同调

\[
{H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathcal{G}}\right) .
\]

- 设 \( \mathcal{U} \) 是 \( X \) 的一个开覆盖. 记 Open \( \mathcal{U} \) 为 \( \mathcal{U} \) 中有限多个开集的交集的全体. 于是有 \( \mathcal{U} \) 上预层, \( \mathcal{U} \) 上常值预层, \( \mathcal{U} \) 上两个预层之间的同态,同构等概念.

例如 \( \mathcal{U} \) 上预层 \( \mathcal{F} \) 是指: 对每个开集 \( U \in \) Open \( \mathcal{U} \) 赋予一个 abel 群 \( \mathcal{F}\left( U\right) \) ; 对 Open \( \mathcal{U} \) 中任意开集的包含 \( V \subset  U \) ,赋予同态 \( {\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) 使得它们满足预层定义中的两个条件.

- 设 \( \mathcal{F} \) 是 \( \mathcal{U} \) 上取值于 abel 群 \( G \) 的常值预层. 若 \( \mathcal{U} \) 是一个好覆盖,则所有的 \( U \in \) Open \( \mathcal{U} \) 是连通的. 于是 \( \mathcal{F}\left( U\right) \) 是 \( U \) 上取值于 \( G \) 的常值函数的全体,它自然等同于 \( G \) . 因此对好覆盖 \( \mathcal{U} \) 上取值于 abel 群 \( G \) 的常值预层,所有赋予的 abel 群是群 \( G \) ,所有的限制是恒等映射. 此时我们把 \( \mathcal{F} \) 简称为常值预层 \( G \) .

- 好覆盖 \( \mathcal{U} \) 上一个预层 \( \mathcal{F} \) 称之为局部常值预层,若所有赋予的 able 群同构,所有的限制是同构.

一个自然的问题是局部常值预层在什么条件下同构于常值预层.

例 13.1. ( \( \mathcal{U} \) 上局部常值预层不是常值预层) 给定 \( {S}^{1} \) 的好覆盖 \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) . 在 \( \mathcal{U} \) 上定义一个局部常值预层 \( \mathcal{F} \) : 对任意 \( U \in \) Open \( \mathcal{U} \) 赋予 \( \mathcal{F}\left( U\right)  = \mathbb{Z} \) ; 限制为

\[
{\rho }_{01}^{0} = {\rho }_{01}^{1} = {\rho }_{12}^{1} = {\rho }_{12}^{2} = 1
\]

\[
{\rho }_{02}^{2} =  - 1,{\rho }_{02}^{0} = 1
\]

此处 \( {\rho }_{ij}^{i} : \mathcal{F}\left( {U}_{i}\right)  \rightarrow  \mathcal{F}\left( {U}_{ij}\right) \) .

![bo_d7e85t491nqc73eqefm0_428_885_881_541_506_0.jpg](images/fu_algebraic_topology_and_differential_forms_097_bod7e85t491nqc73eqefm04288858815415060.jpg)

根据定义, \( \overline{\mathcal{F}} \) 是 \( \mathcal{U} \) 上局部常值预层而不是常值预层因为 \( {\rho }_{02}^{2} =  - 1 \) .

问题: \( \mathcal{F} \) 同构于常值预层 \( \mathbb{Z} \) 吗?

由练习 10.7 知,

所以由断言 1 知局部常值预层 \( \mathcal{F} \) 与常值预层 \( \mathbb{Z} \) 不同构. 事实上,

若 \( \mathcal{F} \) 同构于 \( \mathbb{Z} \) ， 我们看右边的图. 左右两列的映射是给定的. 左边的列为预层 \( \mathcal{F} \) , 右边的列表示常值预层 \( \mathbb{Z} \) . 若第一行的映射是恒等映射的话, 则为了使图可交换, 从第二行开始必须都是 -id. 这样最后一行的映射与第一行的映射不一样, 矛盾.

\[
{H}^{1}\left( {\mathcal{U},\mathcal{F}}\right)  = {\mathbb{Z}}_{2} \neq  \mathbb{Z} = {H}^{1}\left( {\mathcal{U},\mathbb{Z}}\right) .
\]

\( \mathcal{F} \) 与常值预层 \( \mathbb{Z} \) 不同构. 事实上,

![bo_d7e85t491nqc73eqefm0_429_979_524_569_1201_0.jpg](images/fu_algebraic_topology_and_differential_forms_098_bod7e85t491nqc73eqefm042997952456912010.jpg)

若我们把局部常值预层 \( \mathcal{F} \) 修改一下. 令

\[
{\rho }_{02}^{0} =  - 1
\]

这样得到的局部常值预层同构于常值预层 \( \mathbb{Z} \) ,因为对这样的局部常值预层, 右边图表从第三行开始是恒等映射， 不矛盾.

\( \mathcal{F}\left( {U}_{0}\right)  = \mathbb{Z}\overset{\text{ id }}{ \rightarrow  }\mathbb{Z} \) id \( \mathcal{F}\left( {U}_{01}\right)  = \mathbb{Z}\overset{\text{ id }}{ \rightarrow  }\mathbb{Z} \) id \( \uparrow  \; \uparrow \) id \( \mathcal{F}\left( {U}_{1}\right)  = \mathbb{Z}\overset{\text{ id }}{ \rightarrow  }\mathbb{Z} \) id

\( \mathcal{F}\left( {U}_{12}\right)  = \mathbb{Z}\overset{\text{ id }}{ \rightarrow  }\mathbb{Z} \)

\( \mathcal{F}\left( {U}_{2}\right)  = \mathbb{Z}\overset{\text{ id }}{ \rightarrow  }\mathbb{Z} \)

补充练习 1. 记修改后的预层为 \( {\mathcal{F}}^{\prime } \) . 直接验证 \( {H}^{ * }\left( {\mathcal{U},{\mathcal{F}}^{\prime }}\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{Z}}\right) \) .

## 单值表示

设 \( X \) 是拓扑空间, \( \mathcal{U} \) 是 \( X \) 的好覆盖. 记 \( N\left( \mathcal{U}\right) \) 是 \( \mathcal{U} \) 的 nerve,它是单纯复形. 设 \( \mathcal{F} \) 是定义在 \( \mathcal{U} \) 上的预层. 我们换一个观点看 \( \mathcal{F} \) .

对 \( N\left( \mathcal{U}\right) \) 进行重心重分,得到 \( {N}^{\prime }\left( \mathcal{U}\right) \) . 则 \( {N}^{\prime }\left( \mathcal{U}\right) \) 的每个顶点恰好就是 Open \( \mathcal{U} \) 的一个元. \( \mathcal{U} \) 上预层 \( \mathcal{F} \) 可以看作是对 \( {N}^{\prime }\left( \mathcal{U}\right) \) 的每个顶点赋予一个 abel 群,将 \( {N}^{\prime }\left( \mathcal{U}\right) \) 的每条边画上一个箭头表示限制. 于是限制的传递性等价于每条边上带箭头的 2-单形是一个交换图. 例如,

![bo_d7e85t491nqc73eqefm0_431_535_878_639_433_0.jpg](images/fu_algebraic_topology_and_differential_forms_102_bod7e85t491nqc73eqefm04315358786394330.jpg)

![bo_d7e85t491nqc73eqefm0_431_1250_878_588_369_0.jpg](images/fu_algebraic_topology_and_differential_forms_099_bod7e85t491nqc73eqefm043112508785883690.jpg)

![bo_d7e85t491nqc73eqefm0_431_512_1345_619_375_0.jpg](images/fu_algebraic_topology_and_differential_forms_101_bod7e85t491nqc73eqefm043151213456193750.jpg)

![bo_d7e85t491nqc73eqefm0_431_1306_1343_476_379_0.jpg](images/fu_algebraic_topology_and_differential_forms_100_bod7e85t491nqc73eqefm0431130613434763790.jpg)

现设 \( \mathcal{F} \) 是好覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 上 abel 群 \( G \) 的局部常值预层. 根据定义,对每个 \( \alpha  \in  I \) 存在同构

\[
{\phi }_{\alpha } : \mathcal{F}\left( {U}_{\alpha }\right) \overset{ \sim  }{ \rightarrow  }G
\]

若 \( {U}_{\alpha \beta } \neq  \varnothing \) ,则从图表

![bo_d7e85t491nqc73eqefm0_432_854_661_620_619_0.jpg](images/fu_algebraic_topology_and_differential_forms_103_bod7e85t491nqc73eqefm04328546616206190.jpg)

得

\[
{\phi }_{\beta } \circ  {\rho }_{\beta }^{\alpha } \circ  {\phi }_{\alpha }^{-1} \in  \operatorname{Aut}\left( G\right) ,\;\text{ 其中 }{\rho }_{\beta }^{\alpha } = {\left( {\rho }_{\alpha \beta }^{\beta }\right) }^{-1} \circ  {\rho }_{\alpha \beta }^{\alpha }.
\]

选取 \( N\left( \mathcal{U}\right) \) 的一个顶点 \( {U}_{0} \) 作为 \( N\left( \mathcal{U}\right) \) 的基点. 对以 \( {U}_{0} \) 为基点的圈 \( {U}_{0}{U}_{1}\cdots {U}_{r}{U}_{0} \) , 得到 \( G \) 的自同构

\[
{\phi }_{0}\left( {{\rho }_{0}^{r}{\rho }_{r}^{r - 1}\ldots {\rho }_{2}^{1}{\rho }_{1}^{0}}\right) {\phi }_{0}^{-1} \in  \operatorname{Aut}\left( G\right)
\]

![bo_d7e85t491nqc73eqefm0_433_895_406_505_1107_0.jpg](images/fu_algebraic_topology_and_differential_forms_104_bod7e85t491nqc73eqefm043389540650511070.jpg)

这样就定义了映射

\( \left( \overline{ * }\right) \; \overline{\rho } : \{ N\left( \mathcal{U}\right) \) 中以 \( {U}_{0} \) 为基点的圈 \( \}  \rightarrow  \operatorname{Aut}\left( G\right) . \)

断言 2. \( \overline{\rho } \) 将边圈映为 \( \operatorname{Aut}\left( G\right) \) 的单位元即恒等映射. 证. 例如对边圈 \( {U}_{0}{U}_{1}{U}_{2}{U}_{0} \) ,要证 \( {\phi }_{0}\left( {{\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0}}\right) {\phi }_{0}^{-1} = \mathrm{{id}} \) ,只要证 \( {\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0} = \mathrm{{id}} \) . 这个等式的证明见下图所演示, 其中映射分别是

\[
{\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0},\;{\rho }_{0}^{2}{\rho }_{2}^{1}{\left( {\rho }_{012}^{1}\right) }^{-1}{\rho }_{012}^{01}{\rho }_{01}^{0},\;{\rho }_{0}^{2}{\left( {\rho }_{12}^{2}\right) }^{-1}{\left( {\rho }_{012}^{12}\right) }^{-1}{\rho }_{012}^{01}{\rho }_{01}^{0},
\]

\[
{\rho }_{0}^{2}{\left( {\rho }_{012}^{2}\right) }^{-1}{\rho }_{012}^{01}{\rho }_{01}^{0}\;{\left( {\rho }_{02}^{0}\right) }^{-1}{\left( {\rho }_{012}^{02}\right) }^{-1}{\rho }_{012}^{01}{\rho }_{01}^{0},\;{\left( {\rho }_{012}^{0}\right) }^{-1}{\rho }_{012}^{01}{\rho }_{01}^{0}
\]

![bo_d7e85t491nqc73eqefm0_434_518_814_1303_695_0.jpg](images/fu_algebraic_topology_and_differential_forms_105_bod7e85t491nqc73eqefm043451881413036950.jpg)

用相同的过程可证沿着任意边圈的映射 \( {\rho }_{0}^{\alpha }\ldots {\rho }_{\beta }^{0} \) 是恒等映射. 由断言 2 知同态 \( \overline{\rho } \) 诱导了同态:

\[
\rho  : {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  = \frac{\left\{  \mathcal{U}{U}_{0}\text{ 为基点的圈 }\right\}  }{\{ \text{ 边圈 }\} } \rightarrow  \text{ Aut }\left( G\right) . \tag{47}
\]

\( \rho \) 称为局部常值预层 \( \mathcal{F} \) 的单值表示(monodromy representation).

定理 13.2. 设 \( \mathcal{U} \) 是连通拓扑空间 \( X \) 的好覆盖, \( N\left( \mathcal{U}\right) \) 是它的 nerve. 若 \( N\left( \mathcal{U}\right) \) 的边路群 \( {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  = 0 \) ,则 \( \mathcal{U} \) 上局部常值预层同构于常值预层. 证. 设 \( \mathcal{F} \) 是好覆盖 \( \mathcal{U} \) 上局部常值预层,即存在 abel 群 \( G \) 使得对任意 \( U \in \) Open \( \mathcal{U} \) ,存在同构 \( {\phi }_{U} : \mathcal{F}\left( U\right)  \rightarrow  G \) ; 对任意 Open \( \mathcal{U} \) 中包含 \( V \subset  U \) ,存在同构 \( {\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) . 从图表

![bo_d7e85t491nqc73eqefm0_436_870_536_587_581_0.jpg](images/fu_algebraic_topology_and_differential_forms_106_bod7e85t491nqc73eqefm04368705365875810.jpg)

定义了 \( G \) 的一个自同构

\[
{\phi }_{V}{\rho }_{V}^{U}{\phi }_{U}^{-1} \in  \operatorname{Aut}\left( G\right) \text{ . }
\]

如果所有的这种自同构都是恒等映射, \( \phi \) 就定义了 \( \mathcal{F} \) 与常值预层 \( G \) 的同构. 但这种自同构一般不是恒等映射.

为此需借助 \( \left\{  {\phi }_{U}\right\} \) 构造 \( \mathcal{F} \) 与常值预层 \( G \) 的同构 \( \psi \) ,即对任意的 \( U \in \) Open \( \mathcal{U} \) 构造同构

\[
{\psi }_{U} : \mathcal{F}\left( U\right)  \rightarrow  G
\]

使得对 \( \text{ ○ } \) pen \( \mathcal{U} \) 中任意包含 \( V \subset  U \) 满足

\[
{\psi }_{V}{\rho }_{V}^{U}{\psi }_{U}^{-1} = \mathrm{{id}} \tag{48}
\]

即下列图表是可交换的:

![bo_d7e85t491nqc73eqefm0_437_924_1023_511_403_0.jpg](images/fu_algebraic_topology_and_differential_forms_107_bod7e85t491nqc73eqefm043792410235114030.jpg)

选定 \( {U}_{0} \in  \mathcal{U} \) 作为基点并令

\[
{\psi }_{0} = {\phi }_{0} : \mathcal{F}\left( {U}_{0}\right) \overset{ \sim  }{ \rightarrow  }G.
\]

对每个 \( {U}_{\alpha } \in  \mathcal{U} \) ,选定一条从 \( {U}_{0} \) 到 \( {U}_{\alpha } \) 的道路,如 \( \sigma  = {U}_{0}{U}_{{\alpha }_{1}}\ldots {U}_{{\alpha }_{r}}{U}_{\alpha } \) ,定义同构

\[
{\psi }_{\alpha } : \mathcal{F}\left( {U}_{\alpha }\right)  \rightarrow  G
\]

\[
{\psi }_{\alpha } = {\phi }_{0}{\left( {\rho }_{\alpha }^{{\alpha }_{r}}\ldots {\rho }_{{\alpha }_{2}}^{{\alpha }_{1}}{\rho }_{{\alpha }_{1}}^{0}\right) }^{-1}
\]

![bo_d7e85t491nqc73eqefm0_438_927_863_597_558_0.jpg](images/fu_algebraic_topology_and_differential_forms_108_bod7e85t491nqc73eqefm04389278635975580.jpg)

由于 \( {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right)  = 0 \) ,即每个圈是边圈,所以由断言 2 知 \( {\psi }_{\alpha } \) 的定义与道路 \( \sigma \) 的选取无关, 即它是定义好的.

对 \( N\left( \mathcal{U}\right) \) 作重心重分得到新的单纯复形 \( {N}^{\prime }\left( \mathcal{U}\right) \) ,则 Open \( \mathcal{U} \) 中每个元 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) 对应于 \( {N}^{\prime }\left( \mathcal{U}\right) \) 的一个顶点. 由于

\[
{\pi }_{1}\left( {{N}^{\prime }\left( \mathcal{U}\right) }\right)  = {\pi }_{1}\left( {N\left( \mathcal{U}\right) }\right) ,
\]

对任意的 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \in  \operatorname{Open}\mathcal{U} \) ,选取一条从 \( {U}_{0} \) 到 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) 的道路,于是由预层 \( \mathcal{F} \) 的一系列限制诱导了同构

\[
{\chi }_{{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}} : \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \simeq  \mathcal{F}\left( {U}_{0}\right) .
\]

由此定义同构

\[
{\psi }_{{\alpha }_{0}\ldots {\alpha }_{p}} : \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  G,
\]

于是对 \( \operatorname{Open}\mathcal{U} \) 的任意开集的包含 \( V \subset  U \) 验证等式 (48).

\[
{\psi }_{V} \circ  {\rho }_{V}^{U} \circ  {\psi }_{U}^{-1}
\]

\[
= {\psi }_{V} \circ  {\rho }_{V}^{U} \circ  {\chi }_{U}^{-1} \circ  {\phi }_{0}^{-1}
\]

\( = {\psi }_{V} \circ  {\chi }_{V}^{-1} \circ  {\phi }_{0}^{-1}\; \)

\[
= {\phi }_{0} \circ  {\phi }_{0}^{-1}
\]

\[
\text{ =id. }
\]

![bo_d7e85t491nqc73eqefm0_439_835_1084_712_569_0.jpg](images/fu_algebraic_topology_and_differential_forms_109_bod7e85t491nqc73eqefm043983510847125690.jpg)

![bo_d7e85t491nqc73eqefm0_440_1047_263_1049_1037_0.jpg](images/fu_algebraic_topology_and_differential_forms_111_bod7e85t491nqc73eqefm04401047263104910370.jpg)

所以 \( \psi \) 定义了局部常值预层 \( \mathcal{F} \) 与常值预层 \( G \) 之间的同构.

注记 13.2.1. 若局部常值预层的群 \( G \) 满足 \( \operatorname{Aut}\left( G\right)  = \{ \mathrm{{id}}\} \) ,则没有单值性. 特别地,群 \( {\mathbb{Z}}_{2} \) 的局部常值预层是常值预层.

单值性的例子

例 13.5. 设 \( {S}^{1} \) 是复平面上单位圆周,具有好覆盖 \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) . 映射 \( \pi  : z \mapsto  {z}^{2} \) 定义了纤维丛 \( \pi  : {S}^{1} \rightarrow  {S}^{1} \) ，它的每个纤维是由两个不同的点组成的. 设 \( F = \{ A, B\} \) 是点1上的纤维. 由于维数的原因, \( F \) 的上同调只有 \( {H}^{0}\left( F\right) \) 不等于零, 它由定义在 \( \{ A, B\} \) 上的所有函数组成,即

\[
{H}^{0}\left( F\right)  = \left\{  {\left( {a, b}\right)  \in  {\mathbb{R}}^{2}}\right\}   \simeq  {\mathbb{R}}^{2}.
\]

![bo_d7e85t491nqc73eqefm0_441_536_852_541_504_0.jpg](images/fu_algebraic_topology_and_differential_forms_112_bod7e85t491nqc73eqefm04415368525415040.jpg)

\( {\mathrm{U}}_{0}^{\prime \prime } \)

\( {\mathrm{U}}_{0}^{\prime } \)

\( \pi \)

\( {\mathrm{U}}_{0} \)

考虑好覆盖 \( \mathcal{U} \) 上局部常值预层 \( {\mathcal{H}}^{0} \) . 固定一个同构

\[
{\mathcal{H}}^{0}\left( {U}_{0}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{0}\right) }\right)  \simeq  {H}^{0}\left( F\right) .
\]

因为 \( {H}^{0}\left( {{U}_{i}^{\prime } \cup  {U}_{i}^{\prime \prime }}\right)  \rightarrow  {H}^{0}\left( {\left( {{U}_{i}^{\prime } \cap  {U}_{j}^{\prime }}\right)  \cup  \left( {{U}_{i}^{\prime \prime } \cap  {U}_{j}^{\prime \prime }}\right) }\right) \) 是由包含映射诱导的,所以有图表

![bo_d7e85t491nqc73eqefm0_442_675_255_957_1407_0.jpg](images/fu_algebraic_topology_and_differential_forms_113_bod7e85t491nqc73eqefm044267525595714070.jpg)

若我们从 \( {H}^{ * }\left( F\right) \) 的元 \( \left( {a, b}\right) \) 开始沿着图表走,最后得到的不是 \( \left( {a, b}\right) \) 本身,而是 \( \left( {b, a}\right) \) . 因此 \( {\mathcal{H}}^{0} \) 不同构于常值预层 \( {\mathbb{R}}^{2} \) .

练习 13.6. 因为在例 13.5 中双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) 的上同调 \( {H}_{d} \) 仅有一行非零. 由广义 MV 原理与 Tic-Tac-Toe 引理可得

\[
{H}_{dR}^{ * }\left( {S}^{1}\right)  = {H}_{D}^{ * }\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}   = {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) .
\]

直接计算 Čech 上同调 \( {H}^{ * }\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) \) .

例 13.7. 映射 \( \pi \left( x\right)  = {e}^{2\pi ix} \) 定义了万有覆盖 \( \pi  : {\mathbb{R}}^{1} \rightarrow  {S}^{1} \) ,它是 \( {S}^{1} \) 上纤维丛, 纤维 \( F = {\pi }^{-1}\left( 1\right) \) 是可数点集. 底下逆时针兜一圈在同调 \( {H}_{0}\left( F\right) \) 上的作用是平移一个单位: \( x \mapsto  x + 1 \) . 它在上同调 \( {H}^{0}\left( F\right) \) 上的作用是把纤维上以 \( x \) 为支集的函数变为以 \( x + 1 \) 为支集的函数. 见下图.

![bo_d7e85t491nqc73eqefm0_444_950_470_417_809_0.jpg](images/fu_algebraic_topology_and_differential_forms_114_bod7e85t491nqc73eqefm04449504704178090.jpg)

练习 13.8. 设 \( \mathcal{U} \) 是 \( {S}^{1} \) 的好覆盖. 与例 13.5 相同，

\[
{H}_{dR}^{ * }\left( {\mathbb{R}}^{1}\right)  = {H}_{D}^{ * }\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}   = {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) .
\]

直接计算 \( {H}^{ * }\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) \) .

例 13.9. 在前面两个例子中,底流形的基本群作用在纤维的 \( {H}_{0} \) 上. 现给一个作用在 \( {H}_{2} \) 上的例子.

两个球面 \( {S}^{m} \) , \( {S}^{n} \) 的楔积 (wedge) \( {S}^{m} \vee  {S}^{n} \) 是这两个球面的并集且把一点等同. 设 \( X \) 如下图所示是 \( {S}^{1} \vee  {S}^{2} \) ,设 \( Y \) 是 \( X \) 的万有覆盖. 注意虽然 \( {H}^{ * }\left( X\right) \) 是有限的, 但 \( {H}^{ * }\left( Y\right) \) 是无限的. 在 \( {S}^{1} \) 上定义纤维为 \( Y \) 的纤维丛

\[
E = Y \times  I/\left( {x,0}\right)  \sim  \left( {s\left( x\right) ,1}\right) ,
\]

其中 \( s \) 是万有覆盖 \( Y \) 的 deck 变换,它把 \( Y \) 的每个点往上提一个单位. 投射 \( \pi  : E \rightarrow  {S}^{1} \) 为 \( \pi \left( {\widetilde{x}, t}\right)  = t \) . 底流形 \( {S}^{1} \) 的基本群 \( {\pi }_{1}\left( {S}^{1}\right) \) 在纤维 \( Y \) 的第二个同调 \( {H}_{2}\left( Y\right) \) 上的作用是把每个球面往上提一个单位.

练习 13.10. 求空间 \( E \) 的伦型.

![bo_d7e85t491nqc73eqefm0_446_493_210_1313_1320_0.jpg](images/fu_algebraic_topology_and_differential_forms_115_bod7e85t491nqc73eqefm0446493210131313200.jpg)

作业:

1. 补充练习 1.

2. 练习 13.6.

3. 练习 13.8.

4. 练习 13.10.

代数拓扑与微分形式
