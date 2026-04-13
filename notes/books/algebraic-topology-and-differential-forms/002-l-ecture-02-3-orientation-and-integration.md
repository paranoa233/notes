#### 2. 流形上微积分

\( \text{ § }2 \) . The Mayer-Vietoris 序列 函子 \( {\Omega }^{ * } \) §3. Orientation and Integration

2. 流形上微积分

这次课讲书本第二节 Mayer-Vietoris 序列中函子 \( {\Omega }^{ * } \) 及第三节定向与积分，这属于微分流形的内容. 假定大家学过微分流形. 在这里我们不强调函子的概念.

- 流形上微分形式

- 单位分解

- 定向

·积分

流形上微分形式

设 \( {x}_{1},\ldots ,{x}_{n} \) 是 \( {\mathbb{R}}^{n} \) 上标准坐标, \( {y}_{1},\ldots ,{y}_{m} \) 是 \( {\mathbb{R}}^{m} \) 上标准坐标. 光滑映射 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{m} \) 诱导了拉回映射

\[
{f}^{ * } : {\Omega }^{0}\left( {\mathbb{R}}^{m}\right)  \rightarrow  {\Omega }^{0}\left( {\mathbb{R}}^{n}\right) ,\;{f}^{ * }\left( g\right)  = g \circ  f;
\]

也诱导了拉回映射

\[
{f}^{ * } : {\Omega }^{1}\left( {\mathbb{R}}^{m}\right)  \rightarrow  {\Omega }^{1}\left( {\mathbb{R}}^{n}\right) ,\;{f}^{ * }\left( {d{y}_{i}}\right)  = d\left( {{y}_{i} \circ  f}\right)  = d{f}_{i}.
\]

于是可将 \( {f}^{ * } \) 延拓，得到拉回映射

\[
{f}^{ * } : {\Omega }^{ * }\left( {\mathbb{R}}^{m}\right)  \rightarrow  {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)
\]

\[
{f}^{ * }\left( {{g}_{I}d{y}_{{i}_{1}} \land  \cdots  \land  d{y}_{{i}_{q}}}\right)  = {f}^{ * }\left( {g}_{I}\right) {f}^{ * }\left( {d{y}_{{i}_{1}}}\right)  \land  \cdots  \land  {f}^{ * }\left( {d{y}_{{i}_{q}}}\right)
\]

\[
= \left( {{g}_{I} \circ  f}\right) d{f}_{{i}_{1}} \land  \cdots  \land  d{f}_{{i}_{q}}.
\]

命题 2.1. \( d{f}^{ * } = {f}^{ * }d \) .

补充练习 1 . 证明上述命题.

设 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是微分同胚. 记

\[
{u}_{i} = {x}_{i} \circ  f = {f}_{i}.
\]

则 \( {u}_{1},\ldots ,{u}_{n} \) 是 \( {\mathbb{R}}^{n} \) 上新坐标,称为由微分同胚 \( f \) 定义的坐标.

若 \( g \) 是 \( {\mathbb{R}}^{n} \) 上一个光滑函数,根据链规则有

\[
{dg} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial g}{\partial {u}_{i}}d{u}_{i} = \mathop{\sum }\limits_{{i, j = 1}}^{n}\frac{\partial g}{\partial {u}_{i}}\frac{\partial {f}_{i}}{\partial {x}_{j}}d{x}_{j} = \mathop{\sum }\limits_{{j = 1}}^{n}\frac{\partial g}{\partial {x}_{j}}d{x}_{j} = {dg}.
\]

所以 \( {dg} \) 与坐标系无关,这就是一阶微分不变性. 更一般地,外微分 \( d \) 与 \( {\mathbb{R}}^{n} \) 上坐标系无关.

拉回映射与一阶微分不变性是流形上定义微分形式与外微分算子 \( d \) 的基础.

设 \( M \) 是光滑 \( n \) 维流形, \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  \Lambda } \) 是 \( M \) 的一个坐标图册. 为了方便用 \( {U}_{\alpha \beta } \) 记 \( {U}_{\alpha } \) 与 \( {U}_{\beta } \) 的非空交 \( {U}_{\alpha } \cap  {U}_{\beta } \) .

\( M \) 上一个微分形式 \( \omega \) 是微分形式的集类 \( {\left\{  {\omega }_{\alpha } \in  {\Omega }^{ * }\left( {U}_{\alpha }\right) \right\}  }_{\alpha  \in  \Lambda } \) ,它满足条件: 若 \( {i}_{\alpha } : {U}_{\alpha \beta } \rightarrow  {U}_{\alpha },{i}_{\beta } : {U}_{\alpha \beta } \rightarrow  {U}_{\beta } \) 是包含映射,则

\[
{i}_{\alpha }^{ * }{\omega }_{\alpha } = {i}_{\beta }^{ * }{\omega }_{\beta } \tag{1}
\]

我们也称微分形式的集类 \( \{ {\omega }_{\alpha }{\} }_{\alpha  \in  \Lambda } \) 能拼成 \( M \) 上一个微分形式 \( \omega \) . 有时为了方便把 \( {i}_{\alpha }^{ * }{\omega }_{\alpha } \) 记作 \( {\left. {\omega }_{\alpha }\right| }_{{U}_{\alpha \beta }} \) ,读作把 \( {U}_{\alpha } \) 上的微分形式 \( {\omega }_{\alpha } \) 限制到它的开子集 \( {U}_{\alpha \beta } \) 上. 这样条件 (1) 变为

\[
{\left. {\omega }_{\alpha }\right| }_{{U}_{\alpha \beta }} = {\left. {\omega }_{\beta }\right| }_{{U}_{\alpha \beta }}.
\]

\( M \) 上微分形式的全体记作 \( {\Omega }^{ * }\left( M\right) \) ,其上可定义外微分 \( d \) 与外积 \( \land \) . 例如对 \( \omega  = {\left\{  {\omega }_{\alpha }\right\}  }_{\alpha  \in  \Lambda } \) ,由于 \( d \) 与 \( {i}_{\alpha }^{ * },{i}_{\beta }^{ * } \) 可交换,所以

\[
{i}_{\alpha }^{ * }\left( {d{\omega }_{\alpha }}\right)  = {i}_{\beta }^{ * }\left( {d{\omega }_{\beta }}\right) .
\]

这就是说微分形式的集类 \( {\left\{  d{\omega }_{\alpha }\right\}  }_{\alpha  \in  \Lambda } \) 满足条件 (1),所以能拼成 \( M \) 上一个微分形式,把它定义为 \( {d\omega } \) .

我们有直和分解

\[
{\Omega }^{ * }\left( M\right)  = {\bigoplus }_{q = 0}^{n}{\Omega }^{q}\left( M\right)
\]

因为 \( {d}^{2} = 0 \) ,所以 \( \left\{  {{\Omega }^{ * }\left( M\right) , d}\right\} \) 是一个复形,称为 \( M \) 上 de Rham 复形. 定义

\[
{Z}^{q}\left( M\right)  = \left\{  {\omega  \in  {\Omega }^{q}\left( M\right)  \mid  {d\omega } = 0}\right\}   : \;M\text{ 的闭 }q\text{ -形式的全体; }
\]

\( {B}^{q}\left( M\right)  = \left\{  {{d\tau } \mid  \tau  \in  {\Omega }^{q - 1}\left( M\right) }\right\}   : \;M \) 的恰当 q-形式的全体; \( {H}^{q}\left( M\right)  = \frac{{Z}^{q}\left( M\right) }{{B}^{q}\left( M\right) } : \;M \) 的第 \( q \) 个 de Rham 上同调. 设 \( f : M \rightarrow  N \) 是光滑映射. \( f \) 诱导了拉回映射 \( {f}^{ * } : {\Omega }^{ * }\left( N\right)  \rightarrow  {\Omega }^{ * }\left( M\right) \) ,它与外微分 \( d \) 可交换: \( d{f}^{ * } = {f}^{ * }d \) . 所以 \( {f}^{ * } \) 诱导了映射

\[
{f}^{ * } : {H}^{ * }\left( N\right)  \rightarrow  {H}^{ * }\left( M\right) ,\;{f}^{ * }\left\lbrack  \omega \right\rbrack   = \left\lbrack  {{f}^{ * }\omega }\right\rbrack  .
\]

特别地,若 \( i : U \rightarrow  M \) 是开子集的包含映射,则 \( i \) 诱导了映射

\[
{i}^{ * } : {H}^{ * }\left( M\right)  \rightarrow  {H}^{ * }\left( U\right) ,\;{i}^{ * }\left\lbrack  \omega \right\rbrack   = \left\lbrack  {{i}^{ * }\omega }\right\rbrack   = \left\lbrack  {\left. \omega \right| }_{U}\right\rbrack  .
\]

有时也把 \( {i}^{ * }\left\lbrack  \omega \right\rbrack \) 记作 \( {\left. \left\lbrack  \omega \right\rbrack  \right| }_{U} \) . 所以

\[
{\left. \left\lbrack  \omega \right\rbrack  \right| }_{U} = \left\lbrack  {\left. \omega \right| }_{U}\right\rbrack
\]

设 \( \omega  \in  {\Omega }^{ * }\left( M\right) \) . 它的支集定义为

\[
\text{ Supp }\omega  = \overline{\{ x \in  M \mid  \omega \left( x\right)  \neq  0\} }\text{ . }
\]

如果 \( \operatorname{Supp}\omega \) 是 \( M \) 的紧子集,就称 \( \omega \) 是具紧支集的光滑形式. \( {\Omega }_{c}^{ * }\left( M\right) \) 是 \( M \) 上具紧支集的光滑形式的全体.

显然若 \( \omega  \in  {\Omega }_{c}^{q}\left( M\right) \) ,则 \( {d\omega } \in  {\Omega }_{c}^{q + 1}\left( M\right) \) . 所以 \( \left\{  {{\Omega }_{c}^{ * }\left( M\right) , d}\right\} \) 是一个复形. 与 \( {\mathbb{R}}^{n} \) 相同,可定义 \( M \) 的紧上同调:

\[
{H}_{c}^{q}\left( M\right)  = \frac{{Z}_{c}^{q}\left( M\right) }{{B}_{c}^{q}\left( M\right) }.
\]

单位分解

单位分解存在性是微分流形理论中最基本的工具.

定义. 流形 \( M \) 上一个单位分解是其上非负光滑函数的一个集类 \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  \Lambda } \) 使得

(a) \( M \) 的每点有一个邻域,限制在其上只有有限多个 \( {\rho }_{\alpha } \) 不为零,所以 \( \sum {\rho }_{\alpha } \) 是有意义的;

(b) \( \sum {\rho }_{\alpha } = 1 \) .

由于流形是仿紧的, 其上单位分解总是存在的, 它表现为以下两种形式.

(1)给定 \( M \) 的开覆盖 \( \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) ，存在单位分解 \( \{ {\rho }_{\alpha }{\} }_{\alpha  \in  I} \) 使得对任意的 \( \alpha  \in  I \) ， Supp \( {\rho }_{\alpha } \subset  {U}_{\alpha } \) . 这种单位分解称为从属于开覆盖 \( \left\{  {U}_{\alpha }\right\} \) 的单位分解.

(2)给定 \( M \) 的一个开覆盖 \( \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) ，存在单位分解 \( \{ {\rho }_{\beta }{\} }_{\beta  \in  J} \) 使得对任意的 \( \beta  \in  J \) ， Supp \( {\rho }_{\beta } \) 是紧集并且包含于某个 \( {U}_{\alpha } \) . 注意指标集 \( J \) 可能与 \( I \) 不同.

给定 \( M \) 的开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  \Lambda } \) ,问是否存在一个单位分解使得它同时具有 (1) 与 (2) 两种表现形式,即是否存在从属于开覆盖 \( \{ {U}_{\alpha }{\} }_{\alpha  \in  \Lambda } \) 的单位分解 \( \{ {\rho }_{\alpha }{\} }_{\alpha  \in  \Lambda } \) 使得每个 Supp \( {\rho }_{\alpha } \) 是紧集.

当 \( M \) 紧时,显然存在这样的单位分解. 但当 \( M \) 非紧时,一般不存在这样的单位分解. 例如当 \( M = {\mathbb{R}}^{1} \) 时,取它的一个开覆盖为由 \( {\mathbb{R}}^{1} \) 本身一个开集组成.

补充练习 2. 给出 \( {\mathbb{R}}^{1} \) 的一个开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  \mathbb{Z}} \) 使得存在一个从属于它的单位分解 \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  \mathbb{Z}} \) 并且每个 \( {\rho }_{\alpha } \) 的支集是紧集.

补充练习 3. 给定 \( M \) 的一个开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) ,将 \( \omega  \in  {\Omega }^{q}\left( M\right) \) 分解为 \( \omega  = \sum {\omega }_{\alpha } \) 使得对任意的 \( \alpha  \in  I \) , Supp \( {\omega }_{\alpha } \subset  {U}_{\alpha } \) .

补充练习 4 . 由单位分解的第一种形式推出单位分解的第二种形式.

定向设 \( {x}_{1},\ldots ,{x}_{n} \) 是 \( {\mathbb{R}}^{n} \) 上标准坐标. 设 \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是微分同胚. 记

\[
J\left( T\right)  = \det \left( {\partial {T}_{i}/\partial {x}_{j}}\right)
\]

为 \( T \) 的 Jacobi (矩阵的) 行列式. 当 \( J\left( T\right)  > 0 \) 时,称 \( T \) 是保定向的,当 \( J\left( T\right)  < 0 \) 时,称 \( T \) 是反定向的.

一般地,设 \( U, V \subset  {\mathbb{R}}^{n} \) 是开集, \( T : U \rightarrow  V \) 是微分同胚. 则 \( J\left( T\right) \) 在 \( U \) 的每个连通分支上恒正或恒负. 若 \( J\left( T\right) \) 在每个连通分支上都是正的,则称 \( T \) 是保定向的微分同胚.

设 \( M \) 是光滑流形. 它的一个坐标图册 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  \Lambda } \) 是定向的,若对任意的 \( \alpha ,\beta  \in  \Lambda \) ,当 \( {U}_{\alpha \beta } \) 非空时,微分同胚

\[
{\left. {\phi }_{\beta }\right| }_{{U}_{\alpha \beta }} \circ  {\phi }_{\alpha }^{-1}{ \mid  }_{{\phi }_{\alpha }\left( {U}_{\alpha \beta }\right) } : {\phi }_{\alpha }\left( {U}_{\alpha \beta }\right)  \rightarrow  {\phi }_{\beta }\left( {U}_{\alpha \beta }\right)
\]

是保定向的. 具有一个定向坐标图册的流形称为可定向的 (orientable) 流形.

![bo_d7e85t491nqc73eqefm0_36_592_743_1162_754_0.jpg](images/fu_algebraic_topology_and_differential_forms_066_bod7e85t491nqc73eqefm03659274311627540.jpg)

命题 3.2. \( n \) 维流形 \( M \) 是可定向的当且仅当它具有一个整体定义的处处非零的光滑 \( n \) -形式.

补充练习 5 . 证明命题 3.2.

在一个可定向 \( n \) 维流形上任意两个处处非零的 \( n \) -形式 \( \eta ,{\eta }^{\prime } \) 只相差一个处处非零的函数 \( f \) :

\[
\eta  = f{\eta }^{\prime }.
\]

若 \( M \) 是连通的,则 \( f \) 恒正或恒负. 若 \( f \) 是正的,就称 \( \eta ,{\eta }^{\prime } \) 是等价的. 这样,在一个连通可定向流形 \( M \) 上每个处处非零的 \( n \) -形式落在两个等价类中. 每个等价类称为 \( M \) 上一个定向,记作 \( \left\lbrack  M\right\rbrack \) . 例如, \( {\mathbb{R}}^{n} \) 上标准定向由 \( d{x}_{1} \land  \cdots  \land  d{x}_{n} \) 给定.

积分

设 \( {x}_{1},\ldots ,{x}_{n} \) 是 \( {\mathbb{R}}^{n} \) 上标准坐标. \( {\mathbb{R}}^{n} \) 上具紧支集的连续函数 \( f \) 的重积分定义为

\[
{\int }_{{\mathbb{R}}^{n}}f\left( x\right) d{x}_{1}\ldots d{x}_{n} = \mathop{\lim }\limits_{{\bigtriangleup {x}_{i} \rightarrow  0}}\sum f\bigtriangleup {x}_{1}\ldots \bigtriangleup {x}_{n}.
\]

设 \( \omega \) 是 \( {\mathbb{R}}^{n} \) 上一个具紧支集的光滑 \( n \) -形式:

\[
\omega  = f\left( x\right) d{x}_{1} \land  \cdots  \land  d{x}_{n},\;f \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{n}\right) .
\]

它的积分定义为 \( f \) 的重积分:

\[
{\int }_{{\mathbb{R}}^{n}}\omega  = {\int }_{{\mathbb{R}}^{n}}f\left( x\right) d{x}_{1}\ldots d{x}_{n}.
\]

设 \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是微分同胚. 它以如下方式定义 \( {\mathbb{R}}^{n} \) 上新坐标 \( {y}_{1},\ldots ,{y}_{n} \) :

\[
{x}_{i} = {T}_{i}\left( {{y}_{1},\ldots ,{y}_{n}}\right) .
\]

练习 3.1. 证明 \( d{T}_{1} \land  \cdots  \land  d{T}_{n} = J\left( T\right) d{y}_{1} \land  \cdots  \land  d{y}_{n} \) .

由练习 3.1 可得

\[
{T}^{ * }\omega  = \left( {f \circ  T}\right) d{T}_{1} \land  \cdots  \land  d{T}_{n} = \left( {f \circ  T}\right) J\left( T\right) d{y}_{1} \land  \cdots  \land  d{y}_{n}.
\]

所以

\[
{\int }_{{\mathbb{R}}^{n}}{T}^{ * }\omega  = {\int }_{{\mathbb{R}}^{n}}\left( {f \circ  T}\right) J\left( T\right) d{y}_{1}\ldots d{y}_{n}.
\]

另一方面，由积分变换公式可得

\[
{\int }_{{\mathbb{R}}^{n}}\omega  = {\int }_{{\mathbb{R}}^{n}}\left( {f \circ  T}\right) \left| {J\left( T\right) }\right| d{y}_{1}\ldots d{y}_{n}.
\]

因此

\[
{\int }_{{\mathbb{R}}^{n}}{T}^{ * }\omega  =  \pm  {\int }_{{\mathbb{R}}^{n}}\omega
\]

其中正负号由 \( J\left( T\right) \) 的正负号确定.

现设 \( M \) 是一个可定向流形. 在 \( M \) 上选定一个定向 \( \left\lbrack  M\right\rbrack \) 与相应的一个定向坐标图册 \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) . 我们要对任意的 \( \tau  \in  {\Omega }_{c}^{n}\left( M\right) \) 定义 \( {\int }_{\left\lbrack  M\right\rbrack  }\tau \) .

设 \( \left\{  {\rho }_{\alpha }\right\} \) 是从属于 \( \left\{  {U}_{\alpha }\right\} \) 的单位分解. 对 \( \tau  \in  {\Omega }_{c}^{n}\left( M\right) \) 有分解 \( \tau  = \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }\tau \) . 显然每个 \( {\rho }_{\alpha }\tau  \in  {\Omega }_{c}^{n}\left( M\right) \) 且只有有限多个 \( {\rho }_{\alpha }\tau \) 不为零. 所以理应

\[
{\int }_{\left\lbrack  M\right\rbrack  }\tau  = \mathop{\sum }\limits_{\alpha }{\int }_{\left\lbrack  M\right\rbrack  }{\rho }_{\alpha }\tau .
\]

因为 \( \operatorname{Supp}\left( {{\rho }_{\alpha }\tau }\right)  \subset  {U}_{\alpha } \) 并且它是紧的,所以理应

\[
{\int }_{\left\lbrack  M\right\rbrack  }{\rho }_{\alpha }\tau  = {\int }_{\left\lbrack  {U}_{\alpha }\right\rbrack  }\left( {{\rho }_{\alpha }\tau }\right) {|}_{{U}_{\alpha }}.
\]

后者积分中的 \( \left\lbrack  {U}_{\alpha }\right\rbrack \) 是诱导定向,因为 \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) 是定向 \( \left\lbrack  M\right\rbrack \) 相应的定向坐标图册. 但是借助微分同胚 \( {\phi }_{\alpha } : {U}_{\alpha } \rightarrow  {\phi }_{\alpha }\left( {U}_{\alpha }\right)  \subset  {\mathbb{R}}^{n} \) ,后者积分理应定义为

\[
{\int }_{{\phi }_{\alpha }\left( {U}_{\alpha }\right) }{\left( {\phi }_{\alpha }^{-1}\right) }^{ * }\left( {{\rho }_{\alpha }\tau }\right) {\left| {}_{{U}_{\alpha }} = {\int }_{{\mathbb{R}}^{n}}{\left( {\phi }_{\alpha }^{-1}\right) }^{ * }\left( {\rho }_{\alpha }\tau \right) \right| }_{{U}_{\alpha }}
\]

若将被积形式零延拓到整个 \( {\mathbb{R}}^{n} \) . 综上所述,我们将 \( \tau  \in  {\Omega }_{c}^{n}\left( M\right) \) 的积分定义为

\[
{\int }_{\left\lbrack  M\right\rbrack  }\tau  = \mathop{\sum }\limits_{\alpha }{\int }_{{\mathbb{R}}^{n}}{\left( {\phi }_{\alpha }^{-1}\right) }^{ * }\left( {{\rho }_{\alpha }\tau }\right) {|}_{{U}_{\alpha }}.
\]

![bo_d7e85t491nqc73eqefm0_41_416_149_1373_586_0.jpg](images/fu_algebraic_topology_and_differential_forms_095_bod7e85t491nqc73eqefm04141614913735860.jpg)

如果 \( M \) 上给定的定向是明了的,就把积分 \( {\int }_{\left\lbrack  M\right\rbrack  }\tau \) 记为 \( {\int }_{M}\tau \) . 改变 \( M \) 的定向导致积分相差一个符号.

命题 3.3. 积分 \( {\int }_{M}\tau \) 的定义与定向坐标图册及单位分解无关.

补充练习 6 . 证明命题 3.3.

\( n \) 维带边流形 \( M \) 由坐标图册 \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) 给定,其中每个 \( {U}_{\alpha } \) 微分同胚于 \( {\mathbb{R}}^{n} \) 或上半空间 \( {\mathbb{H}}^{n} = \left\{  {\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mid  {x}_{n} \geq  0}\right\}  .M \) 的边界 \( \partial M \) 是一个 \( \left( {n - 1}\right) \) 维流形. \( M \) 的一个定向坐标图册自然诱导了 \( \partial M \) 的一个定向坐标图册.

上半空间 \( {\mathbb{H}}^{n} \) 的标准定向是 \( d{x}_{1} \land  \cdots  \land  d{x}_{n} \) . 根据定义若 \( n > 1 \) ,边界 \( \partial {\mathbb{H}}^{n} \) 的诱导定向是 \( {\left( -1\right) }^{n}d{x}_{1} \land  \cdots  \land  d{x}_{n - 1} \) ; \( \partial {\mathbb{H}}^{1} \) 的诱导定向是-1. 为了使 Stokes 定理不带符号,符号 \( {\left( -1\right) }^{n} \) 是必需的.

一般地,对一个带边定向流形 \( M \) ,用以下方法在 \( \partial M \) 上定义诱导定向 \( \left\lbrack  {\partial M}\right\rbrack \) : 若 \( \phi \) 是从 \( M \) 的某个开集 \( U \) 到 \( {\mathbb{H}}^{n} \) 的保定向微分同胚,则

\[
{\phi }^{ * }\left\lbrack  {\partial {\mathbb{H}}^{n}}\right\rbrack   = \left\lbrack  {\partial M}\right\rbrack  {|}_{\partial U}
\]

其中 \( \partial U = \left( {\partial M}\right)  \cap  U \) . 例. 将 2 维单位球面沿赤道剪开, 得到两个半球面. 则它们边界的定向见下图.

![bo_d7e85t491nqc73eqefm0_43_922_406_702_525_0.jpg](images/fu_algebraic_topology_and_differential_forms_110_bod7e85t491nqc73eqefm0439224067025250.jpg)

定理 3.5.(Stokes 定理)设 \( M \) 是 \( n \) 维定向流形，它的边界 \( \partial M \) 取诱导定向. 则对任意的 \( \omega  \in  {\Omega }_{c}^{n - 1}\left( M\right) \) ,

\[
{\int }_{M}{d\omega } = {\int }_{\partial M}\omega {|}_{\partial M}
\]

特别地,若 \( M \) 是无边流形,即 \( \partial M = \varnothing \) ,则 \( {\int }_{M}{d\omega } = 0 \) .

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 补充练习 3.

4. 补充练习 4.

5. 补充练习 5.

6. 练习 3.1.

7. 补充练习 6.

代数拓扑与微分形式
