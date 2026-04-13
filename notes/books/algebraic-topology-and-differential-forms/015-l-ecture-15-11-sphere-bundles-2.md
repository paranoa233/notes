#### 15. Hopf 指标定理

代数拓扑与微分形式 §11 Sphere Bundles (2)

15. Hopf 指标定理

这次课讲定向球面丛当纤维的维数比底流形维数小 1 时的欧拉数与截面的孤立奇点， 以及定向流形的欧拉示性数与 Hopf 指标定理. 当然这两者之间是有关系的, 定向流形的单位切丛正是这种球面丛. 对一般球面丛的情形在第 12 节讲.

- 欧拉数与截面的孤立奇点

- 欧拉示性数与 Hopf 指标定理

欧拉数与截面的孤立奇点

假定 \( M \) 是紧定向 \( n \) 维流形, \( \pi  : E \rightarrow  M \) 是定向 \( {S}^{n - 1} \) –丛,且 \( E \) 的结构群可约化到 \( O\left( n\right) \) ,也就是说它是某个秩 \( n \) 定向向量丛的球面丛.

由于 \( e\left( E\right)  \in  {H}^{n}\left( M\right) \) 且 \( {H}^{n}\left( M\right)  \simeq  \mathbb{R} \) ,所以 \( e\left( E\right) \) 与 \( E \) 的欧拉数 \( {\int }_{M}e\left( E\right) \) 等同, 它依赖于 \( E, M \) 定向的选取. 定义 \( M \) 的欧拉数为

\[
{\int }_{M}e\left( {TM}\right) .
\]

它与 \( M \) 的定向选取无关,因为若改变 \( M \) 的定向,切丛 \( {TM} \) 的定向从而单位切丛 \( S\left( {TM}\right) \) 的定向也改变.

球面丛 \( E \) 一般没有整体截面，但在 \( M \) 去掉有限多个点 \( {x}_{1},\ldots ,{x}_{q} \) 的补集上有截面 s. 事实上,正如以下命题 11.14 所证,若球面丛有结构群 \( O\left( n\right) \) ,则这种 “不完全” 截面 \( s \) 总存在. 我们将解释如何利用截面 \( s \) 在奇点 \( {x}_{1},\ldots ,{x}_{q} \) 附近的行为计算 \( E \) 的欧拉类.

命题 11.14. 设 \( \pi  : E \rightarrow  M \) 是 \( n \) 维紧流形 \( M \) 上 \( {S}^{n - 1} \) -丛. 假定 \( E \) 的结构群可约化到 \( O\left( n\right) \) . 则 \( E \) 限制在 \( M - \left\{  {{x}_{1},\ldots ,{x}_{q}}\right\} \) 上有截面,其中 \( {x}_{1},\ldots ,{x}_{q} \) 是 \( M \) 中某些点.

证. 因为 \( E \) 的结构群是 \( O\left( n\right) \) ,所以存在秩 \( n \) 向量丛 \( {E}^{\prime } \) 与其上度量 \( \langle \) , \( \rangle \) 使得 \( E = S\left( {E}^{\prime }\right) \) . 设 \( {s}^{\prime } : M \rightarrow  {E}^{\prime } \) 是截面. 若 \( {s}^{\prime }\left( x\right)  \neq  0 \) ,则

\[
s\left( x\right)  = \frac{{s}^{\prime }\left( x\right) }{\begin{Vmatrix}{s}^{\prime }\left( x\right) \end{Vmatrix}} \in  {E}_{x}.
\]

所以只要证明存在截面 \( {s}^{\prime } : M \rightarrow  {E}^{\prime } \) 使得它只有有限多个零点. 需要以下的

横截性定理. 设 \( X \) 是紧流形, \( Z \) 是流形 \( Y \) 的闭子流形, \( {f}^{\prime } : X \rightarrow  Y \) 是光滑映射. 则存在 \( {f}^{\prime } \) 的充分小扰动 \( f : X \rightarrow  Y \) 使得 \( f \) 与 \( Z \) 横截,即对任意点 \( x \in  {f}^{-1}\left( Z\right) \) ,

\[
{f}_{ * }\left( {{T}_{x}X}\right)  + {T}_{f\left( x\right) }Z = {T}_{f\left( x\right) }Y
\]

设 \( {s}_{0} : M \rightarrow  {E}^{\prime } \) 是零截面. 则 \( {S}_{0} = {s}_{0}\left( M\right)  \subset  {E}^{\prime } \) 是闭子流形. 由横截性定理知存在 \( {s}_{0} \) 的充分小扰动 \( f : M \rightarrow  {E}^{\prime } \) 使得 \( f \) 与 \( {S}_{0} \) 横截. 此时因为 \( g = \pi  \circ  f : M \rightarrow  M \) 是 \( \pi  \circ  {s}_{0} = \mathrm{{id}} : M \rightarrow  M \) 的充分小扰动,所以 \( g : M \rightarrow  M \) 是微分同胚. 定义 \( {s}^{\prime } : M \rightarrow  {E}^{\prime } \) 为

\[
{s}^{\prime }\left( x\right)  = f\left( {{g}^{-1}\left( x\right) }\right) .
\]

则 \( \pi  \circ  {s}^{\prime } = \) id，即 \( {s}^{\prime } \) 是截面. 并且由于 \( f \) 横截于 \( {S}_{0} \) ，所以 \( {s}^{\prime } \) 横截于 \( {S}_{0} \) ，即 \( S = {s}^{\prime }\left( M\right) \) 与 \( {S}_{0} \) 横截相交. 因为

\[
\dim S + \dim {S}_{0} = {2n} = \dim {E}^{\prime },
\]

所以 \( \dim \left( {S \cap  {S}_{0}}\right)  = 0 \) . 又因为 \( S \cap  {S}_{0} \) 是紧的,所以 \( S \cap  {S}_{0} \) 只有有限多个点. 这就是说,截面 \( {s}^{\prime } : M \rightarrow  {E}^{\prime } \) 只有有限多个零点.

注记 11.15. 由障碍性理论的基本原理知, 即使球面丛的结构群不能约化到正交群, 上述命题仍然成立. 对障碍性理论的解释可参考 Steenrod 书的第三部分. 设 \( s \) 是 \( {\left. E\right| }_{M - \left\{  {{x}_{1},\ldots ,{x}_{q}}\right\}  } \) 的一个截面. 取 \( M \) 的一个开覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 使得

(a) \( {\psi }_{\alpha } : {U}_{\alpha }\overset{ \sim  }{ \rightarrow  }{\mathbb{R}}^{n} \) 是坐标图;

(b) \( {\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  {S}^{n - 1} \) 是平凡化;

(c) 每个 \( {U}_{\alpha } \) 最多包含一点 \( {x}_{i} \) .

根据以下引理,可把 (c) 改成

(c’) 每点 \( {x}_{i} \) 有邻域 \( {W}_{i} \) ,它只包含于某个 \( {U}_{\alpha } \in  \mathcal{U} \) .

引理. 存在 \( \mathcal{U} \) 的一个加细 \( \mathcal{V} = {\left\{  {V}_{\alpha }\right\}  }_{\alpha  \in  I} \) 使得 \( {V}_{\alpha } \subset  {U}_{\alpha } \) 且每点 \( {x}_{i} \) 有一个邻域 \( {W}_{i} \) ,它只与某个 \( {V}_{\alpha } \) 相交.

证. 不妨设 \( {x}_{1} \in  {U}_{1} \) . 设 \( {W}_{1} \) 是 \( {x}_{1} \) 的开邻域使得 \( {\bar{W}}_{1} \subset  {U}_{1} \) . 定义一个新的开覆盖 \( {\left\{  {U}_{\alpha }^{\prime }\right\}  }_{\alpha  \in  I} \) 如下. 设

\[
{U}_{1}^{\prime } = {U}_{1},\;{U}_{\alpha }^{\prime } = {U}_{\alpha } - {\bar{W}}_{1},\alpha  \neq  1.
\]

则 \( {x}_{1} \in  {W}_{1} \subset  {U}_{1}^{\prime } \) ,但 \( {W}_{1} \cap  {U}_{\alpha }^{\prime } = \varnothing ,\alpha  \neq  1 \) .

![bo_d7e85t491nqc73eqefm0_337_804_180_724_611_0.jpg](images/fu_algebraic_topology_and_differential_forms_054_bod7e85t491nqc73eqefm03378041807246110.jpg)

不妨设 \( {x}_{2} \in  {U}_{2}^{\prime } \) . 设 \( {W}_{2} \) 是 \( {x}_{2} \) 的开邻域使得 \( {\bar{W}}_{2} \subset  {U}_{2}^{\prime } \) . 再定义 \( M \) 的一个开覆盖 \( {\left\{  {U}_{\alpha }^{\prime \prime }\right\}  }_{\alpha  \in  I} \) 如下. 设

\[
{U}_{2}^{\prime \prime } = {U}_{2}^{\prime },\;{U}_{\alpha }^{\prime \prime } = {U}_{\alpha }^{\prime } - {\bar{W}}_{2},\alpha  \neq  2.
\]

因为 \( {U}_{\alpha }^{\prime \prime } \subset  {U}_{\alpha }^{\prime },{W}_{1} \) 与 \( {U}_{\alpha }^{\prime \prime },\alpha  \neq  1 \) 不相交. 根据定义, \( {W}_{2} \) 与 \( {U}_{\alpha }^{\prime \prime },\alpha  \neq  2 \) 也不相交. 显然 \( {W}_{1} \subset  {U}_{1}^{\prime \prime },{W}_{2} \subset  {U}_{2}^{\prime \prime } \) .

相继对 \( {x}_{3},\ldots ,{x}_{q} \) 进行操作,可得引理中的开覆盖 \( {\left\{  {V}_{\alpha }\right\}  }_{\alpha  \in  I} \) :

\[
{V}_{\alpha } = {U}_{\alpha }{}^{\prime \prime }\cdots {}^{\prime }.
\]

承上,设 \( {x}_{i} \in  {W}_{i} \subset  {U}_{{\alpha }_{i}} \) 是 \( s \) 的奇点. 选取点 \( {x}_{i} \) 的充分小开邻域 \( {D}_{i} \) 使得 \( {D}_{i} \subset  {W}_{i} \) 且 \( {\psi }_{{\alpha }_{i}}\left( {D}_{i}\right)  \subset  {\mathbb{R}}^{n} \) 是半径为 \( {r}_{i} \) 的开圆盘. 所以 \( \partial {\bar{D}}_{i} \) 微分同胚于 \( {S}^{n - 1} \) . 于是有以下映射的序列:

\[
\partial {\bar{D}}_{i}\xrightarrow[]{{\left. s\right| }_{\partial {\bar{D}}_{i}}}{\left. E\right| }_{\partial {\bar{D}}_{i}}\overset{i}{ \rightarrow  }{\left. E\right| }_{{\bar{D}}_{i}}\overset{{\phi }_{{\alpha }_{i}}}{ \rightarrow  }{\bar{D}}_{i} \times  {S}^{n - 1}\overset{p{r}_{2}}{ \rightarrow  }{S}^{n - 1}.
\]

记 \( {s}_{i} \) 为前两个映射的复合, \( {\rho }_{i} \) 为后两个映射的复合.

\( M \) 的定向诱导了 \( {D}_{i} \) 的定向. 在 \( {S}^{n - 1} \) 上选取一个定向使得微分同胚

\[
{\left. E\right| }_{{D}_{i}} \simeq  {D}_{i} \times  {S}^{n - 1}
\]

是保定向的,或者说使得 \( {\left. E\right| }_{{D}_{i}} \) 的定向是直和定向. 这样,选取 \( \sigma  \in  {H}^{n - 1}\left( {S}^{n - 1}\right) \) 是正的生成元. 截面 \( s \) 在点 \( {x}_{i} \) 的局部度数(local degree)定义为

\[
\text{ l.d. }\left( {x}_{i}\right)  \mathrel{\text{ := }} {\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }{\rho }_{i}^{ * }\sigma .
\]

定理 11.16. 设 \( \pi  : E \rightarrow  M \) 是紧定向 \( n \) 维流形 \( M \) 上定向 \( {S}^{n - 1} \) -丛. 若 \( E \) 限制在 \( M - \left\{  {{x}_{1},\ldots ,{x}_{q}}\right\} \) 上有截面 \( s \) ,则 \( E \) 的欧拉数

\[
{\int }_{M}e\left( E\right)  = \mathop{\sum }\limits_{{i = 1}}^{q}\text{ l.d. }\left( {x}_{i}\right) .
\]

证. 由注记 11.12.1 知 \( \operatorname{Supp}e \subset  \bigcup {U}_{{\alpha }_{0}\ldots {\alpha }_{n - 1}} \) . 因此 \( e{ \mid  }_{{W}_{i}} = 0, i = 1,\ldots , q \) . 于是

11.16.1) \( \;{\int }_{M}e = {\int }_{M -  \cup  {D}_{i}}e\; \) 因为 \( {\bar{D}}_{i} \subset  {W}_{i} \)

\[
= {\int }_{M -  \cup  {D}_{i}}{s}^{ * }{\pi }^{ * }e\;\text{ 因为 }{s}^{ * }{\pi }^{ * } = \mathrm{{id}}
\]

\[
=  - {\int }_{M -  \cup  {D}_{i}}{s}^{ * }{d\psi }\;\text{ 因为 }{\pi }^{ * }e =  - {d\psi }
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{q}{\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }\psi \;\text{ 根据 Stokes 定理,因为 }{s}_{i} = {\left. i \circ  s\right| }_{\partial {\bar{D}}_{i}}.
\]

虽然整体角形式 \( \psi \) 不一定是闭的，但是

\[
{\left. d\psi \right| }_{E{ \mid  }_{{W}_{i}}} =  - {\left. \left( {\pi }^{ * }e\right) \right| }_{E{ \mid  }_{{W}_{i}}} =  - {\pi }^{ * }\left( {\left. e\right| }_{{W}_{i}}\right)  = 0.
\]

所以 \( {\left\lbrack  {\left. \psi \right| }_{{\left. E\right| }_{{W}_{i}}}\right\rbrack  }_{i} \in  {H}^{n - 1}\left( {\left. E\right| }_{{W}_{i}}\right) \) 并且它是生成元,这是因为 \( \psi \) 限制在每条纤维上是生成元. 另一方面,设 \( \left\lbrack  \sigma \right\rbrack   \in  {H}^{n - 1}\left( {S}^{n - 1}\right) \) 是生成元,则 \( \left\lbrack  {\left. \psi \right| }_{{\left. E\right| }_{{W}_{i}}}\right\rbrack   = \left\lbrack  {{\widetilde{\rho }}_{i}^{ * }\sigma }\right\rbrack \) ,其中 \( {\widetilde{\rho }}_{i} : {\left. E\right| }_{{W}_{i}} \rightarrow  {W}_{i} \times  {S}^{n - 1} \rightarrow  {S}^{n - 1} \) . 所以

\[
{\left. \psi \right| }_{E{ \mid  }_{{W}_{i}}} = {\widetilde{\rho }}_{i}^{ * }\sigma  + d{\tau }_{i},\;{\tau }_{i} \in  {\Omega }^{n - 2}\left( {\left. E\right| }_{{W}_{i}}\right) .
\]

限制到 \( {\left. E\right| }_{{D}_{i}} \) 再用 \( {s}_{i} \) 拉回到 \( \partial {\bar{D}}_{i} \) 上,

\[
{s}_{i}^{ * }\psi  = {s}_{i}^{ * }{\rho }_{i}^{ * }\sigma  + {s}_{i}^{ * }d{\tau }_{i}
\]

等式两边在 \( \partial {\bar{D}}_{i} \) 上积分，根据 Stokes 定理，

\[
{\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }\psi  = {\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }{\rho }_{i}^{ * }\sigma  + {\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }d{\tau }_{i} = {\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }{\rho }_{i}^{ * }\sigma  = \text{ I.d. }\left( {x}_{i}\right) .
\]

再结合 (11.16.1), 得到

\[
{\int }_{M}e = \mathop{\sum }\limits_{{i = 1}}^{q}{\int }_{\partial {\bar{D}}_{i}}{s}_{i}^{ * }\psi  = \mathop{\sum }\limits_{{i = 1}}^{q}\text{ l.d. }\left( {x}_{i}\right) .
\]

上述定理也可叙述成向量丛的形式. 设 \( \pi  : E \rightarrow  M \) 是紧定向 \( n \) 维流形上秩 \( n \) 定向向量丛, \( s \) 是 \( E \) 的具有有限多个零点的截面. \( s \) 在零点 \( x \) 的重数定义为 \( E \) 的单位球面丛 \( S\left( E\right) \) 的奇异截面 \( s/\parallel s\parallel \) 在奇点 \( x \) 的局部度数. 此处单位球面丛是相对于 \( E \) 上某一度量而言. 显然重数的这个定义与度量的选取无关因为局部度数是同伦不变量. 由于 \( E \) 的欧拉类是 \( M \) 上 \( n \) -形式,它 Poincaré 对偶于 \( {mP} \) ,其中 \( m \) 是 \( E \) 的欧拉数, \( P \) 是 \( M \) 上点. 这样就得到

定理 11.17. 设 \( \pi  : E \rightarrow  M \) 是紧定向 \( n \) 维流形 \( M \) 上秩 \( n \) 定向向量丛. 设 \( s \) 是 \( E \) 的具有限多个零点的截面. 则 \( E \) 的欧拉类 Poincaré 对偶于 \( s \) 的零点的形式线性组合, 组合系数为重数.

证. 设 \( s \) 的零点为 \( {x}_{1},\ldots ,{x}_{q} \) . 由定理 11.16,

\[
{\int }_{M}e\left( E\right)  = {\int }_{M}e\left( {S\left( E\right) }\right)  = \mathop{\sum }\limits_{{i = 1}}^{q}{n}_{i},
\]

其中 \( {n}_{i} \) 是 \( s/\parallel s\parallel \) 在点 \( {x}_{i} \) 的局部度数. 另一方面,因为 \( e\left( E\right)  \in  {H}^{n}\left( M\right) \) , 它 Poincaré 对偶于 \( \left( {\mathop{\sum }\limits_{{i = 1}}^{q}{n}_{i}}\right) P \) ，其中 \( P \in  M \) ，它当然也 Poincaré 对偶于 \( \mathop{\sum }\limits_{{i = 1}}^{q}{n}_{i}{x}_{i} \)

例 11.18. ( \( {S}^{2} \) 的单位切丛的欧拉类) 设 \( S\left( {T{S}^{2}}\right) \) 是 \( {S}^{2} \) 的单位切丛. 它是 \( {S}^{2} \) 上一个圆周丛:

![bo_d7e85t491nqc73eqefm0_342_919_236_481_309_0.jpg](images/fu_algebraic_topology_and_differential_forms_056_bod7e85t491nqc73eqefm03429192364813090.jpg)

记 \( N \) 为北极而 \( S \) 为南极. 固定 \( {S}^{2} \) 在北极 \( N \) 的一个单位切向量 \( \overrightarrow{v}.\overrightarrow{v} \) 沿大圆作平行移动定义了 \( {S}^{2} - \{ S\} \) 上一个光滑向量场. 它的定义如下. 任给 \( P \in  {S}^{2} - \{ N, S\} \) , 则 \( P \) 与 \( N \) 可由唯一的大圆弧(劣弧) \( C\left( t\right) \) 连接， \( 0 \leq  t \leq  {t}_{0} \) ，其中 \( C\left( 0\right)  = N \) ， \( C\left( {t}_{0}\right)  = P \) . 在 \( P \) 点存在唯一的单位切向量 \( {\overrightarrow{v}}_{P} \) 使得它与曲线 \( C\left( t\right) \) 在点 \( P \) 的单位切向量的夹角等于 \( \overrightarrow{v} \) 与曲线 \( C\left( t\right) \) 在点 \( N \) 的单位切向量的夹角.

![bo_d7e85t491nqc73eqefm0_342_881_1049_558_667_0.jpg](images/fu_algebraic_topology_and_differential_forms_055_bod7e85t491nqc73eqefm034288110495586670.jpg)

在围绕南极的小圆周上向量场看起来如下图所示,即当我们绕圆走 \( {90}^{ \circ  } \) 时,向量场绕了 180°. 因此向量场 \( s \) 在南极的局部度数是 2. 由定理 11.16, \( {S}^{2} \) 的单位切丛的欧拉数是 2 .

![bo_d7e85t491nqc73eqefm0_343_605_362_1134_401_0.jpg](images/fu_algebraic_topology_and_differential_forms_057_bod7e85t491nqc73eqefm034360536211344010.jpg)

练习 11.19. 证明偶维数纤维的定向球面丛的欧拉类为零.

因为欧拉类是在定向球面丛上存在闭整体角形式的障碍, 根据 Leray-Hirsch 定理有练习 11.19 的以下推论.

命题 11.20. 若 \( \pi  : E \rightarrow  M \) 是定向 \( {S}^{2n} - \) 丛,则

\[
{H}^{ * }\left( E\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( {S}^{2n}\right) .
\]

练习 11.21. 在球面 \( {S}^{n} \) 上找一个向量场并计算它的局部度数，从而计算球面 \( {S}^{n} \) 的单位切丛的欧拉类.

欧拉示性数与 Hopf 指标定理

设 \( M \) 是紧定向 \( n \) 维流形. 在这节要证明 \( M \) 的欧拉数 \( {\int }_{M}e\left( {TM}\right) \) 等于它的欧拉示性数:

\[
\chi \left( M\right)  = \mathop{\sum }\limits_{{q = 0}}^{n}{\left( -1\right) }^{q}\dim {H}^{q}\left( M\right)
\]

并由此导出 Hopf 指标定理.

设 \( \left\{  {\omega }_{i}\right\} \) 是向量空间 \( {H}^{ * }\left( M\right) \) 的一组基, \( \left\{  {\tau }_{j}\right\} \) 是在 Poincaré 对偶下的对偶基,即

\[
{\int }_{M}{\omega }_{i} \land  {\tau }_{j} = {\delta }_{ij}
\]

设 \( \pi ,\rho  : M \times  M \rightarrow  M \) 分别是两个投射. 由 Künneth 公式得

\[
{H}^{ * }\left( {M \times  M}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( M\right) .
\]

它的一组基为 \( \left\{  {{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{j}}\right\} \) ,

\( M \times  M \) 的对角流形为

\[
\Delta  = \{ \left( {x, x}\right)  \in  M \times  M \mid  x \in  M\}  \subset  M \times  M.
\]

作为 \( M \times  M \) 的子流形, \( \bigtriangleup \) 的 Poincaré 对偶 \( {\eta }_{\bigtriangleup } \) 可表示为线性组合

\[
{\eta }_{\bigtriangleup } = \mathop{\sum }\limits_{{i, j}}{c}_{ij}{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{j}
\]

引理 11.22. \( {\eta }_{\bigtriangleup } = \sum {\left( -1\right) }^{\deg {\omega }_{i}}{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{i} \) .

证. 用两种方法计算 \( {\int }_{\bigtriangleup }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \) . 一方面,借助对角映射 \( \iota  : M \rightarrow  \bigtriangleup \) 把积分拉回到 \( M \) :

\[
{\int }_{\bigtriangleup }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} = {\int }_{M}{\iota }^{ * }{\pi }^{ * }{\tau }_{k} \land  {\iota }^{ * }{\rho }^{ * }{\omega }_{l} = {\int }_{M}{\tau }_{k} \land  {\omega }_{l} = {\left( -1\right) }^{\left( {\deg {\tau }_{k}}\right) \left( {\deg {\omega }_{l}}\right) }{\delta }_{lk}.
\]

另一方面，根据闭定向子流形的 Poincaré 对偶的定义，

\[
{\int }_{\bigtriangleup }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} = {\int }_{M \times  M}{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \land  {\eta }_{\bigtriangleup }
\]

\[
= \mathop{\sum }\limits_{{i, j}}{c}_{ij}{\int }_{M \times  M}{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \land  {\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{j}
\]

\[
= \mathop{\sum }\limits_{{i, j}}{\left( -1\right) }^{\left( {\deg {\omega }_{i}}\right) \left( {\deg {\tau }_{k} + \deg {\omega }_{l}}\right) }{c}_{ij}{\int }_{M \times  M}{\pi }^{ * }\left( {{\omega }_{i} \land  {\tau }_{k}}\right)  \land  {\rho }^{ * }\left( {{\omega }_{l} \land  {\tau }_{j}}\right)
\]

\[
= \mathop{\sum }\limits_{{i, j}}{\left( -1\right) }^{\left( {\deg {\omega }_{i}}\right) \left( {\deg {\omega }_{l} + \deg {\tau }_{k}}\right) }{c}_{ij}{\delta }_{ik}{\delta }_{lj}
\]

\[
= {\left( -1\right) }^{\left( {\deg {\omega }_{k}}\right) \left( {\deg {\omega }_{l} + \deg {\tau }_{k}}\right) }{c}_{kl}.
\]

因此,

\[
{c}_{kl} = \left\{  \begin{array}{ll} 0 & k \neq  l \\  {\left( -1\right) }^{\deg {\omega }_{k}} & k = l. \end{array}\right.
\]

引理 11.23. \( {N}_{\bigtriangleup /M \times  M} \simeq  T\bigtriangleup \) .

证. 因为对角映射 \( \iota  : M \rightarrow  \bigtriangleup \) 是微分同胚,所以 \( {\iota }^{-1}T\bigtriangleup  \simeq  {TM} \) . 于是从交换图

\[
\left( {v, v}\right)  \mapsto  \;\left( {v, v}\right)
\]

\[
0 \rightarrow  T\bigtriangleup  \rightarrow  T\left( {M \times  M}\right) {\left| \bigtriangleup  \rightarrow  {N}_{\bigtriangleup /M \times  M} \rightarrow  0\right| }_{.}
\]

得到

\[
{N}_{\bigtriangleup /M \times  M} \simeq  {TM} \oplus  {TM}/{TM} \simeq  {TM} \simeq  T\bigtriangleup .
\]

命题 11.24. 对紧定向流形 \( M,{\int }_{M}e\left( {TM}\right)  = \chi \left( M\right) \) . 证. 设 \( i : \bigtriangleup  \rightarrow  M \times  M \) 是包含映射. 则

\[
{\int }_{\bigtriangleup }{i}^{ * }{\eta }_{\bigtriangleup } = {\int }_{\bigtriangleup }{i}^{ * }\Phi \left( {N}_{\bigtriangleup }\right)
\]

\[
= {\int }_{\bigtriangleup }e\left( {N}_{\bigtriangleup }\right)
\]

\[
= {\int }_{\bigtriangleup }e\left( {T\bigtriangleup }\right)
\]

\[
= {\int }_{M}e\left( {TM}\right)
\]

闭子流形 \( \bigtriangleup \) 的 Poincaré 对偶与管状邻

域 \( {N}_{\bigtriangleup } \) 的 Thom 类可由同一形式表示 \( i \) 视为零截面. 根据命题 12.4, Thom 类限制到向量丛的零截面是欧拉类.

根据引理 11.23

因为 \( \iota  : M \rightarrow  \bigtriangleup \) 是微分同胚.

根据 Poincaré 对偶,

\[
{\int }_{\bigtriangleup }{i}^{ * }{\eta }_{\bigtriangleup } = {\int }_{M \times  M}{\eta }_{\bigtriangleup } \land  {\eta }_{\bigtriangleup }
\]

是对角流形 \( \bigtriangleup \) 在 \( M \times  M \) 中的自相交数. 所以对角流形 \( \bigtriangleup \) 在 \( M \times  M \) 中的自相交数是 \( M \) 的欧拉数. 另一方面，引理 11.22 的等式两边在 \( \bigtriangleup \) 上积分，得到

\[
{\int }_{ \bigtriangleup  }{i}^{ * }{\eta }_{ \bigtriangleup  } = \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{ \bigtriangleup  }{i}^{ * }{\pi }^{ * }{\omega }_{i} \land  {i}^{ * }{\rho }^{ * }{\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{M}{\iota }^{ * }{i}^{ * }{\pi }^{ * }{\omega }_{i} \land  {\iota }^{ * }{i}^{ * }{\rho }^{ * }{\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{M}{\omega }_{i} \land  {\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}
\]

\[
= \mathop{\sum }\limits_{q}{\left( -1\right) }^{q}\dim {H}^{q}\left( M\right) \;\text{ 因为 }\left\lbrack  {\omega }_{i}\right\rbrack   \in  {H}^{q}\left( M\right) \text{ 对某个 }q
\]

\[
= \chi \left( M\right) \text{ . }
\]

因此

\[
{\int }_{M}e\left( {TM}\right)  = \chi \left( M\right)
\]

现导出 Hopf 指标定理显得十分简单. 设 \( V \) 是 \( M \) 上具有孤立零点的向量场. \( V \) 在零点 \( x \) 的指标定义为 \( V/\parallel V\parallel \) 在奇点 \( x \) 的局部度数,其中 \( V/\parallel V\parallel \) 作为 \( M \) 相对于某一黎曼度量的单位切丛上的截面. 根据定理 11.16, \( V \) 的指标和是 \( M \) 的欧拉数. 再根据上述命题， \( M \) 的欧拉数与欧拉示性数相等. 这样就得到

定理 11.25.(Hopf 指标定理)紧定向流形 \( M \) 上光滑向量场的指标和等于 \( M \) 的欧拉示性数.

练习 11.26. (Lefschetz 不动点公式) 设 \( M \) 是紧定向流形, \( f : M \rightarrow  M \) 是光滑映射. \( f \) 的 Lefschetz 数定义为

\[
L\left( f\right)  = \mathop{\sum }\limits_{q}{\left( -1\right) }^{q}\operatorname{trace}{H}^{q}\left( f\right) ,
\]

其中 \( {H}^{q}\left( f\right)  : {H}^{q}\left( M\right)  \rightarrow  {H}^{q}\left( M\right) \) 记由 \( f \) 诱导的映射. 设 \( \Gamma  = \{ \left( {x, f\left( x\right) }\right)  \mid  x \in  M\} \) 是 \( f \) 在 \( M \times  M \) 的图.

(a) 证明

\[
{\int }_{\Delta }{\eta }_{\Gamma } = L\left( f\right)
\]

(b) 证明若 \( f \) 没有不动点,则 \( L\left( f\right) \) 等于零.

(c) \( f \) 在不动点 \( p \) 的切映射 \( {f}_{*p} \) 是切空间 \( {T}_{p}M \) 的自同态. 不动点 \( p \) 的重数定义为

\[
{\sigma }_{p} = \operatorname{sgn}\det \left( {I - {f}_{*p}}\right) .\;\text{ (注意与书本不一致) }
\]

证明若图 \( \Gamma \) 横截于 \( M \times  M \) 中对角流形 \( \bigtriangleup \) ,则

\[
L\left( f\right)  = \mathop{\sum }\limits_{p}{\sigma }_{p}
\]

此处是对 \( f \) 的所有不动点 \( p \) 求和.

作业:

1. 练习 11.19.

2. 练习 11.21.

3. 练习 11.26.

代数拓扑与微分形式
