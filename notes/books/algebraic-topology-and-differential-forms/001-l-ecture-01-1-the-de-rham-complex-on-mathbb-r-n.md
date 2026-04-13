#### 1. R^n 上 de Rham 复形

\( \text{ § }1 \) . The de Rham Complex on \( {\mathbb{R}}^{n} \)

1. \( {\mathbb{R}}^{n} \) 上 de Rham 复形 de Rham 上同调是流形最重要的微分同胚不变量.

这次课首先在 \( {\mathbb{R}}^{n} \) 上定义 de Rham 上同调并计算几个例子；接着在 \( {\mathbb{R}}^{n} \) 上定义紧上同调; 最后复习与微分复形有关的一些概念, 如复形的短正合序列, 上同调的长正合序列及连接同态.

- \( {\mathbb{R}}^{n} \) 的 de Rham 上同调

- 紧上同调

- 微分复形

\( {\mathbb{R}}^{n} \) 的 de Rham 上同调设 \( {\mathbb{R}}^{n} \) 是 \( n \) 维欧氏空间, \( {x}_{1},\ldots ,{x}_{n} \) 是其上线性坐标. 在自变量的微分 \( d{x}_{1},\ldots , d{x}_{n} \) 之间引入符号 \( \land \) ，它满足:

\[
d{x}_{i} \land  d{x}_{i} = 0
\]

\[
d{x}_{i} \land  d{x}_{j} =  - d{x}_{j} \land  d{x}_{i}, i \neq  j
\]

定义实向量空间

\[
{\Omega }^{ * } = {\operatorname{span}}_{\mathbb{R}}\left\{  {1, d{x}_{i}, d{x}_{i} \land  d{x}_{j}, d{x}_{i} \land  d{x}_{j} \land  d{x}_{k},\ldots , d{x}_{1} \land  \cdots  \land  d{x}_{n}}\right\}  .
\]

\[
i < j\;i < j < k
\]

它的维数是 \( {C}_{n}^{0} + {C}_{n}^{1} + \cdots  + {C}_{n}^{n} = {2}^{n} \) . 显然 \( {\Omega }^{ * } \) 有直和分解

\[
{\Omega }^{ * } = {\bigoplus }_{q = 0}^{n}{\Omega }^{q}
\]

其中

\[
{\Omega }^{q} = {\mathrm{{span}}}_{\mathbb{R}}\{ d{x}_{{i}_{1}} \land  d{x}_{{i}_{2}} \land  \cdots  \land  d{x}_{{i}_{q}} \mid  1 \leq  {i}_{1} < {i}_{2} < \cdots  < {i}_{q} \leq  n\} .
\]

定义张量积:

\[
{\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)  = {C}^{\infty }\left( {\mathbb{R}}^{n}\right) \underset{\mathbb{R}}{ \otimes  }{\Omega }^{ * }
\]

\[
{\Omega }^{q}\left( {\mathbb{R}}^{n}\right)  = {C}^{\infty }\left( {\mathbb{R}}^{n}\right) \underset{\mathbb{R}}{ \otimes  }{\Omega }^{q}
\]

相应于 \( {\Omega }^{ * } \) 的直和分解,有直和分解

\[
{\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)  = {\bigoplus }_{q = 0}^{n}{\Omega }^{q}\left( {\mathbb{R}}^{n}\right)
\]

\( {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right) \) 的元称为 \( {\mathbb{R}}^{n} \) 上光滑微分形式, \( {\Omega }^{q}\left( {\mathbb{R}}^{n}\right) \) 的元称为光滑 \( q \) -形式. 这样,可把 \( \omega  \in  {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right) \) 按型分解为

\[
\omega  = \mathop{\sum }\limits_{{q = 0}}^{n}{\omega }_{q},\;{\omega }_{q} \in  {\Omega }^{q}\left( {\mathbb{R}}^{n}\right) ,
\]

其中 \( {\omega }_{q} \) 是 \( {\mathbb{R}}^{n} \) 上 \( q \) -形式,它可唯一表示为

\[
{\omega }_{q} = \mathop{\sum }\limits_{{{i}_{1} < \cdots  < {i}_{q}}}{f}_{{i}_{1}\cdots {i}_{q}}d{x}_{{i}_{1}} \land  \cdots  \land  d{x}_{{i}_{q}} = \mathop{\sum }\limits_{{I : {i}_{1} < \cdots  < {i}_{q}}}{f}_{I}d{x}_{I}.
\]

例. 设 \( \omega \) 为 \( {\mathbb{R}}^{n} \) 上一个光滑 2-形式:

\[
\omega  = {h}_{12}\left( x\right) d{x}_{1} \land  d{x}_{2} + {h}_{21}\left( x\right) d{x}_{2} \land  d{x}_{1}
\]

\[
= \left( {{h}_{12}\left( x\right)  - {h}_{21}\left( x\right) }\right) d{x}_{1} \land  d{x}_{2}.
\]

所以 \( {f}_{12}\left( x\right)  = {h}_{12}\left( x\right)  - {h}_{21}\left( x\right) \) ,而对其余的 \( i < j,{f}_{ij}\left( x\right)  = 0 \) .

定义. 设

\[
\tau  = \mathop{\sum }\limits_{{I : {i}_{1} < \cdots  < {i}_{p}}}{f}_{I}d{x}_{I} \in  {\Omega }^{p}\left( {\mathbb{R}}^{n}\right) ,\;\omega  = \mathop{\sum }\limits_{{J : {j}_{1} < \cdots  < {j}_{q}}}{g}_{J}d{x}_{J} \in  {\Omega }^{q}\left( {\mathbb{R}}^{n}\right) .
\]

定义 \( \tau \) 与 \( \omega \) 的外积 \( \tau  \land  \omega  \in  {\Omega }^{p + q}\left( {\mathbb{R}}^{n}\right) \) 为

\[
\tau  \land  \omega  = \mathop{\sum }\limits_{{I, J}}{f}_{I}{g}_{J}d{x}_{I} \land  d{x}_{J} = \mathop{\sum }\limits_{{K : {k}_{1} < \cdots  < {k}_{p + q}}}{h}_{K}d{x}_{K}.
\]

补充练习 1. 用 \( {f}_{I},{g}_{J} \) 表示 \( {h}_{K} \) .

补充练习 2. 证明 \( \tau  \land  \omega  = {\left( -1\right) }^{pq}\omega  \land  \tau \) .

定义. 外微分算子

\[
d : {\Omega }^{q}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\Omega }^{q + 1}\left( {\mathbb{R}}^{n}\right) .
\]

定义如下.

(a) 若 \( f \in  {\Omega }^{0}\left( {\mathbb{R}}^{n}\right)  = {C}^{\infty }\left( {\mathbb{R}}^{n}\right) \) ,则

\[
{df} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}d{x}_{i}
\]

(b) 若 \( \omega  = \mathop{\sum }\limits_{I}{f}_{I}d{x}_{I} \) ,则

\[
{d\omega } = \mathop{\sum }\limits_{I}d{f}_{I} \land  d{x}_{I} = \mathop{\sum }\limits_{{i, I}}\frac{\partial {f}_{I}}{\partial {x}_{i}}d{x}_{i} \land  d{x}_{I}.
\]

命题 1.3. 若 \( \tau  \in  {\Omega }^{p}\left( {\mathbb{R}}^{n}\right) \) ,则

\[
d\left( {\tau  \land  \omega }\right)  = {d\tau } \land  \omega  + {\left( -1\right) }^{p}\tau  \land  {d\omega }.
\]

命题 1.4. \( {d}^{2} = 0 \) .

补充练习 3. 证明上述两个命题. 由于 \( {d}^{2} = 0,\left\{  {{\Omega }^{ * }\left( {\mathbb{R}}^{n}\right) , d}\right\} \) 形成一个复形:

\[
{\Omega }^{0}\left( {\mathbb{R}}^{n}\right) \overset{d}{ \rightarrow  }\cdots \overset{d}{ \rightarrow  }{\Omega }^{q - 1}\left( {\mathbb{R}}^{n}\right) \overset{d}{ \rightarrow  }{\Omega }^{q}\left( {\mathbb{R}}^{n}\right) \overset{d}{ \rightarrow  }{\Omega }^{q + 1}\left( {\mathbb{R}}^{n}\right) \overset{d}{ \rightarrow  }\cdots \overset{d}{ \rightarrow  }{\Omega }^{n}\left( {\mathbb{R}}^{n}\right) .
\]

它称为 \( {\mathbb{R}}^{n} \) 上 de Rham 复形. 如有必要,对 \( q < 0 \) 或 \( q > n \) 添加 \( {\Omega }^{q}\left( {\mathbb{R}}^{n}\right)  = 0 \) . 定义

\[
{Z}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  {\omega  \in  {\Omega }^{q}\left( {\mathbb{R}}^{n}\right)  \mid  {d\omega } = 0}\right\}  ,
\]

其元称为闭的 (closed) \( q \) -形式. 定义

\[
{B}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  {{d\tau } \mid  \tau  \in  {\Omega }^{q - 1}\left( {\mathbb{R}}^{n}\right) }\right\}  ,
\]

其元称为恰当的 (exact) \( q \) -形式. 特别地,

\[
{Z}^{n}\left( {\mathbb{R}}^{n}\right)  = {\Omega }^{n}\left( {\mathbb{R}}^{n}\right) ,\;{B}^{0}\left( {\mathbb{R}}^{n}\right)  = 0.
\]

因为 \( {d}^{2} = 0 \) ，所以

\[
{B}^{q}\left( {\mathbb{R}}^{n}\right)  \subset  {Z}^{q}\left( {\mathbb{R}}^{n}\right) .
\]

定义. \( {\mathbb{R}}^{n} \) 的第 \( q \) 个 de Rham 上同调是向量空间

\[
{H}_{dR}^{q}\left( {\mathbb{R}}^{n}\right)  = \frac{{Z}^{q}\left( {\mathbb{R}}^{n}\right) }{{B}^{q}\left( {\mathbb{R}}^{n}\right) }.
\]

在不致于引起歧义时,通常隐去下标 \( {dR} \) 而记作 \( {H}^{q}\left( {\mathbb{R}}^{n}\right) \) .

闭 \( q \) -形式 \( \omega \) (所在) 的上同调类记为 \( \left\lbrack  \omega \right\rbrack \) . 从

\[
\left\lbrack  {\omega }_{1}\right\rbrack   = \left\lbrack  {\omega }_{2}\right\rbrack   \in  {H}^{q}\left( {\mathbb{R}}^{n}\right)
\]

可读出

\[
d{\omega }_{1} = d{\omega }_{2} = 0,\;\text{ 且 }
\]

\[
{\omega }_{1} - {\omega }_{2} = {d\tau },\;\tau  \in  {\Omega }^{q - 1}\left( {\mathbb{R}}^{n}\right) .
\]

The complex \( {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right) \) together with the differential operator \( d \) is called the de Rham complex on \( {\mathbb{R}}^{n} \) . The kernel of \( d \) are the closed forms and the image of \( d \) , the exact forms. The de Rham complex may be viewed as a God-given set of differential equations, whose solutions are the closed forms. For instance, finding a closed 1-form \( {fdx} + {gdy} \) on \( {\mathbb{R}}^{2} \) is tantamount to solving the differential equation \( \partial g/\partial x - \partial f/\partial y = 0 \) . By Proposition 1.4 the exact forms are automatically closed; these are the trivial or "uninteresting" solutions. A measure of the size of the space of "interesting" solutions is the definition of the de Rham cohomology. 同理,对 \( {\mathbb{R}}^{n} \) 的开集 \( U \) 可定义

\[
{\Omega }^{ * }\left( U\right)  = {C}^{\infty }\left( U\right) \underset{\mathbb{R}}{ \otimes  }{\Omega }^{ * } = {\bigoplus }_{q = 0}^{n}{\Omega }^{q}\left( U\right)
\]

\[
\land  , d
\]

\[
{Z}^{q}\left( U\right)  = \left\{  {\omega  \in  {\Omega }^{q}\left( U\right)  \mid  {d\omega } = 0}\right\}
\]

\[
{B}^{q}\left( U\right)  = \left\{  {\omega  = {d\tau } \mid  \tau  \in  {\Omega }^{q - 1}\left( U\right) }\right\}  ,
\]

\[
{H}_{dR}^{q}\left( U\right)  = \frac{{Z}^{q}\left( U\right) }{{B}^{q}\left( U\right) }.
\]

例 1.5. \( {H}^{q}\left( {\mathbb{R}}^{n}\right) \) .

(a) \( n = 0 \) . 因为 \( {\Omega }^{0}\left( {\mathbb{R}}^{0}\right)  = \mathbb{R} \) ,且对 \( q \neq  0,{\Omega }^{q}\left( {\mathbb{R}}^{0}\right)  = 0 \) ,所以

\[
{H}^{q}\left( {\mathbb{R}}^{0}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0 \\  0 & q \neq  0 \end{array}\right.
\]

(b) \( n = 1 \) . 首先,因为 \( {Z}^{0}\left( {\mathbb{R}}^{1}\right)  = \left\{  {\mathbb{R}}^{1}\right. \) 上常值函数 \( \}  \simeq  \mathbb{R},{B}^{0}\left( {\mathbb{R}}^{1}\right)  = 0 \) ,所以

\[
{H}^{0}\left( {\mathbb{R}}^{1}\right)  = \mathbb{R}.
\]

其次,显然 \( {Z}^{1}\left( {\mathbb{R}}^{1}\right)  = {\Omega }^{1}\left( {\mathbb{R}}^{1}\right) \) . 另一方面又有 \( {B}^{1}\left( {\mathbb{R}}^{1}\right)  = {\Omega }^{1}\left( {\mathbb{R}}^{1}\right) \) . 这是因为对任意的 \( \omega  = g\left( x\right) {dx} \) ,若令

\[
f\left( x\right)  = {\int }_{0}^{x}g\left( t\right) {dt}
\]

则 \( {df}\left( x\right)  = g\left( x\right) {dx} \) . 因此

\[
{H}^{1}\left( {\mathbb{R}}^{1}\right)  = 0
\]

(c) 设 \( U \) 是 \( {\mathbb{R}}^{1} \) 上 \( m \) 个互不相交的开区间的并. 则

\[
{H}^{q}\left( U\right)  = \left\{  \begin{array}{ll} {\mathbb{R}}^{m} & q = 0 \\  0 & q > 0. \end{array}\right.
\]

(d) 一般地有以下 Poincaré 引理:

\[
{H}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0 \\  0 & q \neq  0. \end{array}\right.
\]

它的证明会在以后给出.

练习 1.7. 设 \( P, Q \) 是 \( {\mathbb{R}}^{2} \) 中两点. 计算 \( {H}^{ * }\left( {{\mathbb{R}}^{2} - P - Q}\right) \) 并求表示上同调类的闭形式.

紧上同调设 \( X \) 是拓扑空间, \( f \in  {C}^{0}\left( X\right) \) . 定义 \( f \) 的支集 (support) 为闭集

\[
\text{ Supp }f = \overline{\{ x \in  X \mid  f\left( x\right)  \neq  0\} }\text{ . }
\]

\( X \) 上具紧支集的连续函数的全体记为

\[
{C}_{c}^{0}\left( X\right)  = \left\{  {f \in  {C}^{0}\left( X\right)  \mid  \operatorname{Supp}f\text{ 是紧集 }}\right\}  .
\]

如果 \( M \) 为光滑流形，则 \( M \) 上具紧支集的光滑函数的全体记为

\[
{C}_{c}^{\infty }\left( M\right)  = {C}_{c}^{0}\left( M\right)  \cap  {C}^{\infty }\left( M\right) .
\]

记

\[
{\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  = {C}_{c}^{\infty }\left( {\mathbb{R}}^{n}\right) \mathop{\bigotimes }\limits_{\mathbb{R}}{\Omega }^{ * }
\]

它是 \( {\mathbb{R}}^{n} \) 上具紧支集的光滑形式的全体. 可将它按型分解为

\[
{\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  = {\bigoplus }_{q = 0}^{n}{\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right)
\]

其中 \( {\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right) \) 是 \( {\mathbb{R}}^{n} \) 上具紧支集的光滑 \( q \) -形式的全体.

设 \( \omega  \in  {\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right) \) ,它可表示为

\[
\omega  = \mathop{\sum }\limits_{{I : {i}_{1} < \cdots  < {i}_{q}}}{f}_{I}d{x}_{I},\;{f}_{I} \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{n}\right) .
\]

因为 \( \operatorname{Supp}\frac{\partial {f}_{I}}{\partial {x}_{i}} \subset  \operatorname{Supp}{f}_{I} \) ,且紧集的闭子集是紧集,所以 \( \frac{\partial {f}_{I}}{\partial {x}_{i}} \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{n}\right) \) . 于是 \( {d\omega } \in  {\Omega }_{c}^{q + 1}\left( {\mathbb{R}}^{n}\right) \) . 这就是说, \( \left\{  {{\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right) , d}\right\} \) 是一个复形,称为具紧支集的 de Rham 复形.

定义

\[
{Z}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  {\omega  \in  {\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right)  \mid  {d\omega } = 0}\right\}
\]

\[
{B}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  {{d\tau } \mid  \tau  \in  {\Omega }_{c}^{q - 1}\left( {\mathbb{R}}^{n}\right) }\right\}  ;
\]

\[
{H}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = \frac{{Z}_{c}^{q}\left( {\mathbb{R}}^{n}\right) }{{B}_{c}^{q}\left( {\mathbb{R}}^{n}\right) }
\]

\( {H}_{c}^{q}\left( {\mathbb{R}}^{n}\right) \) 称为 \( {\mathbb{R}}^{n} \) 的第 \( q \) 个具紧支集的上同调,简称紧上同调. 根据定义，

\[
{Z}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = {\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right)  \cap  {Z}^{q}\left( {\mathbb{R}}^{n}\right) ;
\]

但是等式

\[
{B}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = {B}^{q}\left( {\mathbb{R}}^{n}\right)  \cap  {\Omega }_{c}^{q}\left( {\mathbb{R}}^{n}\right)
\]

一般不成立.

例 1.6. \( {H}_{c}^{q}\left( {\mathbb{R}}^{n}\right) \) .

(a) \( n = 0 \) .

\[
{H}_{c}^{q}\left( {\mathbb{R}}^{0}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0 \\  0 & q \neq  0. \end{array}\right.
\]

(b) \( n = 1 \) .

\[
{H}_{c}^{q}\left( {\mathbb{R}}^{1}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 1 \\  0 & q \neq  1. \end{array}\right.
\]

证. 因为 \( {Z}_{c}^{0}\left( {\mathbb{R}}^{1}\right)  = 0 \) ,所以 \( {H}_{c}^{0}\left( {\mathbb{R}}^{1}\right)  = 0 \) .

为了计算 \( {H}_{c}^{1}\left( {\mathbb{R}}^{1}\right) \) ,考虑映射

\[
{\int }_{{\mathbb{R}}^{1}} : {\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right)  \rightarrow  \mathbb{R}.
\]

显然这个映射是满射,因为总存在 \( f\left( x\right)  \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{1}\right) \) 使得 \( {\int }_{{\mathbb{R}}^{1}}f\left( x\right) {dx} = 1 \) .

要证 \( \ker {\int }_{{\mathbb{R}}^{1}} = {B}_{c}^{1}\left( {\mathbb{R}}^{1}\right) \) . 先证 \( {B}_{c}^{1}\left( {\mathbb{R}}^{1}\right)  \subset  \ker {\int }_{{\mathbb{R}}^{1}} \) . 若 \( {df} \in  {B}_{c}^{1}\left( {\mathbb{R}}^{1}\right) \) ,则 Supp \( f \) 是紧的,设它包含于 \( \left\lbrack  {a, b}\right\rbrack \) . 所以

\[
{\int }_{{\mathbb{R}}^{1}}{df} = {\int }_{{\mathbb{R}}^{1}}{f}^{\prime }\left( x\right) {dx} = f\left( b\right)  - f\left( a\right)  = 0,
\]

即 \( {df} \in  \ker {\int }_{{\mathbb{R}}^{1}} \) .

再证 \( \ker {\int }_{{\mathbb{R}}^{1}} \subset  {B}_{c}^{1}\left( {\mathbb{R}}^{1}\right) \) . 设 \( g\left( x\right) {dx} \in  {\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right) \) 且 \( {\int }_{{\mathbb{R}}^{1}}g\left( x\right) {dx} = 0 \) . 令

\[
f\left( x\right)  = {\int }_{-\infty }^{x}g\left( t\right) {dt}
\]

则 \( f\left( x\right)  \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{1}\right) \) 且 \( {df}\left( x\right)  = g\left( x\right) {dx} \) .

综上所述, 有正合序列:

\[
0 \rightarrow  {\Omega }_{c}^{0}\left( {\mathbb{R}}^{1}\right) \overset{d}{ \rightarrow  }{\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right) \overset{{\int }_{\mathbb{R}}1}{ \rightarrow  }\mathbb{R} \rightarrow  0.
\]

于是

\[
{H}_{c}^{1}\left( {\mathbb{R}}^{1}\right)  = \frac{{Z}_{c}^{1}\left( {\mathbb{R}}^{1}\right) }{{B}_{c}^{1}\left( {\mathbb{R}}^{1}\right) } = \frac{{\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right) }{\ker {\int }_{{\mathbb{R}}^{1}}} \simeq  \mathbb{R}.
\]

(c) 对一般的 \( n \) ,有以下紧上同调的 Poincaré 引理.

\[
{H}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = n \\  0 & q \neq  n. \end{array}\right.
\]

它的证明会在以后给出.

\( {\mathbb{R}}^{n} \) 是可缩空间,即它与一点同伦等价. 上例表明紧上同调不是同伦不变量. 对 \( {\mathbb{R}}^{n} \) 的开子集 \( U \) ,同样可定义它的紧上同调 \( {H}_{c}^{ * }\left( U\right) \) .

微分复形向量空间的直和 \( C = {\bigoplus }_{q \in  \mathbb{Z}}{C}^{q} \) 称为微分复形若存在同态 \( d : C \rightarrow  C \) 使得

\[
d : {C}^{q} \rightarrow  {C}^{q + 1},\;{d}^{2} = 0
\]

复形 \( \{ C, d\} \) 的上同调是向量空间的直和

\[
H\left( C\right)  = {\bigoplus }_{q \in  \mathbb{Z}}{H}^{q}\left( C\right)
\]

其中 \( {H}^{q}\left( C\right) \) 是第 \( q \) 个上同调:

\[
{H}^{q}\left( C\right)  = \frac{\ker d \cap  {C}^{q}}{\operatorname{im}d \cap  {C}^{q}}
\]

定义. 设 \( \left\{  {A,{d}_{A}}\right\}  ,\left\{  {B,{d}_{B}}\right\} \) 是复形. 若对每个 \( q \in  \mathbb{Z} \) ,存在同态 \( {f}_{q} : {A}^{q} \rightarrow  {B}^{q} \) 使得

\[
{f}_{q + 1} \circ  {d}_{A} = {d}_{B} \circ  {f}_{q}
\]

即图表

![bo_d7e85t491nqc73eqefm0_21_915_669_520_352_0.jpg](images/fu_algebraic_topology_and_differential_forms_029_bod7e85t491nqc73eqefm0219156695203520.jpg)

可交换,则称两个复形之间的映射 \( f : A \rightarrow  B \) 是链映射.

若 \( f : A \rightarrow  B \) 是链映射,则存在诱导同态

\[
{f}_{q}^{ * } : {H}^{q}\left( A\right)  \rightarrow  {H}^{q}\left( B\right) ,\;{f}_{q}^{ * }\left( \left\lbrack  a\right\rbrack  \right)  = \left\lbrack  {{f}_{q}\left( a\right) }\right\rbrack  .
\]

定义. 设 \( \left\{  {A,{d}_{A}}\right\}  ,\left\{  {B,{d}_{B}}\right\}  ,\left\{  {C,{d}_{C}}\right\} \) 是复形, \( f : A \rightarrow  B, g : B \rightarrow  C \) 是链映射, 且对每个 \( q \in  \mathbb{Z} \) ,序列

\[
0 \rightarrow  {A}_{q}\overset{{f}_{q}}{ \rightarrow  }{B}_{q}\overset{{g}_{q}}{ \rightarrow  }{C}_{q} \rightarrow  0
\]

是正合的. 则称序列

\[
0 \rightarrow  A\overset{f}{ \rightarrow  }B\overset{g}{ \rightarrow  }C \rightarrow  0
\]

是复形的短正合序列.

给定复形的短正合序列

\[
0 \rightarrow  A\overset{f}{ \rightarrow  }B\overset{g}{ \rightarrow  }C \rightarrow  0
\]

存在上同调的长正合序列

\[
\cdots  \rightarrow  {H}^{q}\left( A\right) \overset{{f}_{q}^{ * }}{ \rightarrow  }{H}^{q}\left( B\right) \overset{{g}_{q}^{ * }}{ \rightarrow  }{H}^{q}\left( C\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{q + 1}\left( A\right)  \rightarrow  \cdots
\]

回忆连接同态 \( {d}^{ * } : {H}^{q}\left( C\right)  \rightarrow  {H}^{q + 1}\left( A\right) \) 的定义. 用图追踪:

![bo_d7e85t491nqc73eqefm0_23_481_262_1366_693_0.jpg](images/fu_algebraic_topology_and_differential_forms_032_bod7e85t491nqc73eqefm02348126213666930.jpg)

设 \( \left\lbrack  c\right\rbrack   \in  {H}^{q}\left( C\right) \) ,即 \( c \in  {C}^{q},{dc} = 0 \) . 因为 \( {g}_{q} \) 是满射,所以存在 \( b \in  {B}^{q} \) 使得 \( {g}_{q}\left( b\right)  = c \) . 因为 \( {g}_{q + 1}\left( {d\left( b\right) }\right)  = d{g}_{q}\left( b\right)  = {dc} = 0 \) 且 \( \operatorname{im}{f}_{q + 1} = \ker {g}_{q + 1} \) ,所以存在 \( a \in  {A}^{q + 1} \) 使得 \( {f}_{q + 1}\left( a\right)  = {db} \) . 又因为 \( {f}_{q + 2}\left( {da}\right)  = d{f}_{q + 1}\left( a\right)  = {d}^{2}b = 0 \) 且 \( {f}_{q + 2} \) 是单射,所以 \( {da} = 0,\left\lbrack  a\right\rbrack   \in  {H}^{q + 1}\left( A\right) \) . 定义

\[
{d}^{ * }\left( \left\lbrack  c\right\rbrack  \right)  = \left\lbrack  a\right\rbrack  \text{ . }
\]

补充练习 4. 证明 \( {d}^{ * } \) 是定义好的,即与 \( c, b, a \) 的选取无关.

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 补充练习 3.

4. 练习 1.7.

5. 补充练习 4.

代数拓扑与微分形式
