#### 4. Poincaré 引理

§4 Poincaré Lemmas

4. Poincaré 引理

这节计算 \( {\mathbb{R}}^{n} \) 的 de Rham 上同调与紧上同调. 为此把 \( {\mathbb{R}}^{n + 1} \) 看作 \( {\mathbb{R}}^{n} \) 上以 \( {\mathbb{R}}^{1} \) 为纤维的纤维丛,建立 \( {\mathbb{R}}^{n + 1} \) 的上同调与 \( {\mathbb{R}}^{n} \) 的上同调之间的关系. 为此需定义一个称为同伦算子的映射; 对紧上同调的情形,这个映射称为沿纤维的积分. 最后,作为 \( {\mathbb{R}}^{n} \) 紧上同调的应用,证明 \( {\mathbb{R}}^{n} \) 之间逆紧映射的度是整数.

- de Rham 上同调的 Poincaré 引理

- 紧上同调的 Poincaré 引理

- 逆紧映射的度

de Rham 上同调的 Poincaré 引理

\[
{H}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \simeq  {H}^{ * }\left( {\mathbb{R}}^{n}\right) .
\]

设 \( \pi  : {\mathbb{R}}^{n} \times  {\mathbb{R}}^{1} \rightarrow  {\mathbb{R}}^{n} \) 是投射, \( s : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \times  {\mathbb{R}}^{1} \) 是零截面.

![bo_d7e85t491nqc73eqefm0_69_1388_682_382_287_0.jpg](images/fu_algebraic_topology_and_differential_forms_237_bod7e85t491nqc73eqefm06913886823822870.jpg)

\( {\mathbb{R}}^{n} \times  {\mathbb{R}}^{1} \)

\[
\pi \left( {x, t}\right)  = x
\]

\[
s\left( x\right)  = \left( {x,0}\right)
\]

于是有拉回映射:

\[
{\pi }^{ * } : {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)
\]

\[
{s}^{ * } : {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)
\]

因为 \( \pi  \circ  s = \mathrm{{id}} \) ，所以

\[
{s}^{ * } \circ  {\pi }^{ * } = \mathrm{{id}} : {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)
\]

\[
{s}^{ * } \circ  {\pi }^{ * } = \mathrm{{id}} : {H}^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {H}^{ * }\left( {\mathbb{R}}^{n}\right) .
\]

反之,因为 \( s \circ  \pi  \neq  \mathrm{{id}} \) ,所以

\[
{\pi }^{ * } \circ  {s}^{ * } \neq  \mathrm{{id}} : {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) .
\]

我们要证明等式

\[
{\pi }^{ * } \circ  {s}^{ * } = \mathrm{{id}} : {H}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \tag{2}
\]

成立. 为此要引进同伦算子.

定义. 若映射

\[
K : {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }^{* - 1}\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)
\]

满足

\[
\text{ id } - {\pi }^{ * } \circ  {s}^{ * } =  \pm  \left( {{dK} \pm  {Kd}}\right) \text{ , }
\]

则称 \( K \) 是同伦算子. 此时称 \( {\pi }^{ * } \circ  {s}^{ * } \) 链同伦于恒等映射.

显然,若能构造这样一个同伦算子,则等式 (2) 成立. 这是因为对任意的闭形式 \( \omega \) ,

\[
\left( {\mathrm{{id}} - {\pi }^{ * } \circ  {s}^{ * }}\right) \left( \omega \right)  =  \pm  {dK}\left( \omega \right)
\]

是恰当形式.

以下构造同伦算子 \( K \) . 每个 \( \omega  \in  {\Omega }^{q}\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \) 可唯一地表示为以下两种形式的线性组合:

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) ,\;\phi  \in  {\Omega }^{q}\left( {\mathbb{R}}^{n}\right) \) ; (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt},\;\phi  \in  {\Omega }^{q - 1}\left( {\mathbb{R}}^{n}\right) \) .

定义 \( K : {\Omega }^{q}\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }^{q - 1}\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \) 为

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right)  \mapsto  0 \) (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \mapsto  {\pi }^{ * }\phi  \cdot  {\int }_{0}^{t}f\left( {x, u}\right) {du} \) .

引理. \( K \) 确实是同伦算子,即

\[
\text{ id } - {\pi }^{ * } \circ  {s}^{ * } = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right) .
\]

证. (I) 设 \( \omega  = {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) ,\deg \omega  = q \) .

\[
{d\omega } = {\pi }^{ * }{d\phi } \cdot  f\left( {x, t}\right)  + {\left( -1\right) }^{q}{\pi }^{ * }\phi  \land  \left( {\mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f\left( {x, t}\right) }{\partial {x}_{i}}d{x}_{i} + \frac{\partial f\left( {x, t}\right) }{\partial t}{dt}}\right)
\]

\[
\left( {\mathrm{{id}} - {\pi }^{ * }{s}^{ * }}\right) \omega  = {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right)  - {\pi }^{ * }\phi  \cdot  f\left( {x,0}\right)
\]

\[
\left( {{dK} - {Kd}}\right) \omega  =  - {Kd\omega } = {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \cdot  {\int }_{0}^{t}\frac{\partial f\left( {x, u}\right) }{\partial u}{du}
\]

\[
= {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \cdot  \left( {f\left( {x, t}\right)  - f\left( {x,0}\right) }\right) .
\]

(II) 设 \( \omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \) , \( \deg \omega  = q - 1 \) .

\[
{d\omega } = {\pi }^{ * }{d\phi } \land  f\left( {x, t}\right) {dt} + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}\left( {d{x}_{i} \land  \frac{\partial f\left( {x, t}\right) }{\partial {x}_{i}}{dt}}\right) .
\]

\( \left( {\mathrm{{id}} - {\pi }^{ * } \circ  {s}^{ * }}\right) \omega  = \omega ,\; \) 因为 \( {s}^{ * }{dt} = d\left( {t \circ  s}\right)  = {d0} = 0; \)

\[
{Kd\omega } = {\pi }^{ * }{d\phi } \cdot  {\int }_{0}^{t}f\left( {x, u}\right) {du} + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i}{\int }_{0}^{t}\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}
\]

\[
{dK\omega } = d\left( {{\pi }^{ * }\phi  \cdot  {\int }_{0}^{t}f\left( {x, u}\right) {du}}\right)
\]

\[
= {\pi }^{ * }{d\phi } \cdot  {\int }_{0}^{t}f\left( {x, u}\right) {du} + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \left( {f\left( {x, t}\right) {dt} + \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i}{\int }_{0}^{t}\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}}\right)
\]

\[
= {\left( -1\right) }^{q - 1}\omega  + {\pi }^{ * }{d\phi } \cdot  {\int }_{0}^{t}f\left( {x, u}\right) {du} + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i}{\int }_{0}^{t}\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}.
\]

命题 4.1. 映射 \( {\pi }^{ * } \) 与 \( {s}^{ * } \) 互为同构:

\[
{H}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \underset{{s}^{ * }}{\overset{{\pi }^{ * }}{ \leftrightarrows  }}{H}^{ * }\left( {\mathbb{R}}^{n}\right) .
\]

推论 4.1.1. (Poincaré 引理)

\[
{H}^{q}\left( {\mathbb{R}}^{n}\right)  = {H}^{q}\left( \cdot \right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0 \\  0 & q \neq  0. \end{array}\right.
\]

更一般地，映射

\[
M \times  {\mathbb{R}}^{1}\underset{s}{\overset{\pi }{ \rightleftarrows  }}M
\]

诱导了互为同构的映射 \( {\pi }^{ * },{s}^{ * } \) :

\[
{H}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \simeq  {H}^{ * }\left( M\right)
\]

这可从以下更一般的同伦不变性得到.

定理. (推论 4.1.2, de Rham 上同调的同伦公理) 设 \( M, N \) 是光滑流形, \( f, g \) : \( M \rightarrow  N \) 是光滑同伦的两个光滑映射. 则

\[
{f}^{ * } = {g}^{ * } : {H}^{ * }\left( N\right)  \rightarrow  {H}^{ * }\left( M\right)
\]

证. 设 \( F : M \times  I \rightarrow  N \) 是 \( f \) 与 \( g \) 的光滑同伦, \( I \) 是区间 \( \left\lbrack  {0,1}\right\rbrack  , F\left( {x,0}\right)  = f\left( x\right) \) , \( F\left( {x,1}\right)  = g\left( x\right) \) . 设 \( \omega  \in  {\Omega }^{q}\left( N\right) \) . 则 \( {F}^{ * }\omega  \in  {\Omega }^{q}\left( {M \times  I}\right) \) . 利用 \( M \) 的局部坐标 \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) 与单位分解, \( {F}^{ * }\omega \) 可分解为

\[
{F}^{ * }\omega  = {\omega }_{1} + {\omega }_{2} \land  {dt}
\]

其中 \( {\omega }_{1} \in  {\Omega }^{q}\left( {M \times  I}\right) ,{\omega }_{2} \in  {\Omega }^{q - 1}\left( {M \times  I}\right) \) 可局部表示为

\[
{\omega }_{1} = \mathop{\sum }\limits_{{I : {i}_{1} < \cdots  < {i}_{q}}}{a}_{I}\left( {x, t}\right) d{x}_{I}
\]

\[
{\omega }_{2} = \mathop{\sum }\limits_{{J : {j}_{1} < \cdots  < {j}_{q - 1}}}{b}_{J}\left( {x, t}\right) d{x}_{J}
\]

容易证明 \( M \) 上局部定义的 \( \left( {q - 1}\right) \) 次微分形式

\[
\mathop{\sum }\limits_{{J : {j}_{1} < \cdots  < {j}_{q - 1}}}\left( {{\int }_{0}^{1}{b}_{J}\left( {x, t}\right) {dt}}\right) d{x}_{J}
\]

能拼成 \( M \) 上一个整体定义的微分形式,记为 \( K\left( {{F}^{ * }\omega }\right) \) ,并且 \( K \) 其实就是同伦算子:

\[
{dK}\left( {{F}^{ * }\omega }\right)  \pm  K\left( {d{F}^{ * }\omega }\right)  = {g}^{ * }\omega  - {f}^{ * }\omega .
\]

当 \( {d\omega } = 0 \) 时,因为 \( d{F}^{ * }\omega  = {F}^{ * }{d\omega } = 0 \) ,所以

\[
{g}^{ * }\omega  - {f}^{ * }\omega  = {dK}\left( {{F}^{ * }\omega }\right)
\]

是一个恰当形式. 于是

\[
{f}^{ * } = {g}^{ * } : {H}^{ * }\left( N\right)  \rightarrow  {H}^{ * }\left( M\right)
\]

推论 4.1.2.1. 同伦等价的两个流形有相同的 de Rham 上同调.

由于 \( M \) 的形变收缩 \( A \) 与 \( M \) 同伦等价,所以有

推论 4.1.2.2. 若 \( A \) 是 \( M \) 的形变收缩,则 \( A \) 与 \( M \) 有相同的 de Rham 上同调.

练习 4.2. 证明 \( r : {\mathbb{R}}^{2} - 0 \rightarrow  {S}^{1}, r\left( x\right)  = x/\parallel x\parallel \) 是一个形变收缩.

练习 4.3. (n 维球面 \( {S}^{n} \) 的上同调) 如图用两个开集 \( U \) 与 \( V \) 覆盖 \( {S}^{n} \) ,其中 \( U \) 比北半球大一些而 \( V \) 比南半球大一些. 则 \( U \cap  V \) 微分同胚于 \( {S}^{n - 1} \times  {\mathbb{R}}^{1} \) , 其中 \( {S}^{n - 1} \) 是赤道. 应用 MV 序列证明

\[
{H}^{q}\left( {S}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0, n \\  0 & q \neq  0, n. \end{array}\right.
\]

![bo_d7e85t491nqc73eqefm0_76_852_1146_585_514_0.jpg](images/fu_algebraic_topology_and_differential_forms_240_bod7e85t491nqc73eqefm07685211465855140.jpg)

考虑 \( {H}^{n}\left( {S}^{n}\right) \) 的生成元.

回顾 \( n = 1 \) 的情形. \( {H}^{1}\left( {S}^{1}\right) \) 的一个生成元为 \( \left\lbrack  \eta \right\rbrack  ,\eta \) 是 bump1-形式:

\[
{\int }_{{S}^{1}}\eta  = 1
\]

且 Supp \( \eta \) 的支集可充分小.

![bo_d7e85t491nqc73eqefm0_77_542_772_1239_462_0.jpg](images/fu_algebraic_topology_and_differential_forms_241_bod7e85t491nqc73eqefm07754277212394620.jpg)

其实, \( \eta \) 可取定义在 \( \left\lbrack  {0,{2\pi }}\right\rbrack \) 的 1-形式 \( \eta  = f\left( \theta \right) {d\theta } \) 满足:

\( f\left( \theta \right)  \geq  0,\;\operatorname{Supp}f \subset  \left( {0,{2\pi }}\right) \) 充分小, \( \;{\int }_{0}^{2\pi }f\left( \theta \right) {d\theta } = 1. \)

当 \( n = 2 \) 时,有长正合序列:

\[
\rightarrow  {H}^{1}\left( {S}^{2}\right) \overset{r}{ \rightarrow  }{H}^{1}\left( U\right)  \oplus  {H}^{1}\left( V\right) \overset{\delta }{ \rightarrow  }{H}^{1}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{2}\left( {S}^{2}\right)  \rightarrow  \cdots
\]

记 \( r : U \cap  V \rightarrow  {S}^{1} \) 是形变收缩.

![bo_d7e85t491nqc73eqefm0_78_444_715_1440_333_0.jpg](images/fu_algebraic_topology_and_differential_forms_242_bod7e85t491nqc73eqefm07844471514403330.jpg)

则 \( \left\lbrack  {{r}^{ * }\eta }\right\rbrack   \in  {H}^{1}\left( {U \cap  V}\right) \) 是生成元. 于是 \( {H}^{2}\left( {S}^{2}\right) \) 的生成元是

\[
{\eta }_{2} = \left\{  \begin{array}{ll}  - d\left( {{\rho }_{V}{r}^{ * }\eta }\right) & \text{ on }U \\  d\left( {{\rho }_{U}{r}^{ * }\eta }\right) & \text{ on }V. \end{array}\right.
\]

它是一个 bump 2-形式,支集包含在 \( U \cap  V \) 中.

根据 Stokes 定理计算:

\[
{\int }_{{S}^{2}}{\eta }_{2} = {\int }_{\overline{U}} - d\left( {{\rho }_{V}{r}^{ * }\eta }\right) {|}_{\overline{U}} =  - {\int }_{\partial \overline{U}}{r}^{ * }\eta {|}_{\partial \overline{U}} =  - {\int }_{r\left( {\partial \overline{U}}\right) }\eta  =  - {\int }_{{S}^{1}}\eta  =  - 1.
\]

![bo_d7e85t491nqc73eqefm0_79_801_697_732_514_0.jpg](images/fu_algebraic_topology_and_differential_forms_243_bod7e85t491nqc73eqefm0798016977325140.jpg)

补充练习 1. 利用上述 \( {H}^{2}\left( {S}^{2}\right) \) 的生成元写出 \( {H}^{3}\left( {S}^{3}\right) \) 的一个生成元.

练习 4.3.1. ( \( n \) 维球面 \( {S}^{n} \) 的体积形式) 设 \( {S}^{n}\left( r\right) \) 是 \( {\mathbb{R}}^{n + 1} \) 中半径为 \( r \) 的球面

\[
{x}_{1}^{2} + \cdots  + {x}_{n + 1}^{2} = {r}^{2}
\]

记包含映射为 \( {i}_{r} \) 并记 \( i = {i}_{1} \) . 在 \( {\mathbb{R}}^{n + 1} - 0 \) 上定义 \( n \) -形式

\[
\omega  = \frac{1}{r}\mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\left( -1\right) }^{i - 1}{x}_{i}d{x}_{1} \land  \cdots  \land  \widehat{d{x}_{i}} \land  \cdots  \land  d{x}_{n + 1}.
\]

(a) 记 \( {S}^{n} = {S}^{n}\left( 1\right) \) . 计算积分 \( {\int }_{{S}^{n}}{i}^{ * }\omega \) ,并由此证明 \( {i}^{ * }\omega \) 不是恰当形式.

(b) 把 \( r \) 看作 \( {\mathbb{R}}^{n + 1} - 0 \) 上函数,证明 \( {dr} \land  \omega  = d{x}_{1} \land  \cdots  \land  d{x}_{n + 1} \) ,即 \( {i}_{r}^{ * }\omega \) 是球面 \( {S}^{n}\left( r\right) \) 上欧氏体积形式.

从 (a) 我们得到 \( {S}^{n} \) 的最高次上同调的生成元的显式公式,虽然它不是一个 bump 形式. 例如, \( {H}^{2}\left( {S}^{2}\right) \) 的生成元可表示为

\[
\sigma  = \frac{1}{4\pi }\left( {{x}_{1}d{x}_{2} \land  d{x}_{3} - {x}_{2}d{x}_{1} \land  d{x}_{3} + {x}_{3}d{x}_{1} \land  d{x}_{2}}\right) .
\]

紧上同调的 Poincaré 引理

我们要证明

\[
{H}_{c}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \simeq  {H}_{c}^{* - 1}\left( {\mathbb{R}}^{n}\right) .
\]

更一般地,考虑 \( \pi  : M \times  {\mathbb{R}}^{1} \rightarrow  M \) . 注意映射 \( {\pi }^{ * } : {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) \) 是没有意义的. 为此, 定义一个称为沿纤维积分的新映射

\[
{\pi }_{ * } : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{* - 1}\left( M\right) .
\]

首先注意到任意的 \( \omega  \in  {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) \) 是以下两种形式的 (有限) 线性组合:

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) \) , (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \)

其中 \( \phi  \in  {\Omega }^{ * }\left( M\right) , f\left( {x, t}\right)  \in  {C}_{c}^{\infty }\left( {M \times  {\mathbb{R}}^{1}}\right) \) .

补充练习 2 . 证明上述断言.

定义 \( {\pi }_{ * } \) 为

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right)  \mapsto  0 \) , (4.4) (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \mapsto  \phi  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt} \) .

练习 4.5. 证明 \( d{\pi }_{ * } = {\pi }_{ * }d \) ,即 \( {\pi }_{ * } \) 是链映射.

所以 \( {\pi }_{ * } \) 诱导了映射:

\[
{\pi }_{ * } : {H}_{c}^{q}\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {H}_{c}^{q - 1}\left( M\right) .
\]

需定义 \( {\pi }_{ * } \) 的逆映射.

为此定义映射

\[
{e}_{ * } : {\Omega }_{c}^{q}\left( M\right)  \rightarrow  {\Omega }_{c}^{q + 1}\left( {M \times  {\mathbb{R}}^{1}}\right)
\]

\[
{e}_{ * }\left( \phi \right)  = {\pi }^{ * }\phi  \land  e
\]

其中

\[
e = e\left( t\right) {dt} \in  {\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right) ,\;{\int }_{-\infty }^{\infty }e\left( t\right) {dt} = 1.
\]

则 \( {e}_{ * } \) 是链映射:

\[
d\left( {{e}_{ * }\left( \phi \right) }\right)  = d\left( {{\pi }^{ * }\phi  \land  e}\right)  = d{\pi }^{ * }\phi  \land  e = {\pi }^{ * }{d\phi } \land  e = {e}_{ * }\left( {d\phi }\right) .
\]

所以 \( {e}_{ * } \) 诱导了映射

\[
{e}_{ * } : {H}_{c}^{q}\left( M\right)  \rightarrow  {H}_{c}^{q + 1}\left( {M \times  {\mathbb{R}}^{1}}\right) ,\;{e}_{ * }\left( \left\lbrack  \phi \right\rbrack  \right)  = \left\lbrack  {{\pi }^{ * }\phi  \land  e}\right\rbrack  .
\]

显然有

\[
{\pi }_{ * } \circ  {e}_{ * } = \mathrm{{id}} : {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  {\Omega }_{c}^{ * }\left( M\right) .
\]

所以

\[
{\pi }_{ * } \circ  {e}_{ * } = \mathrm{{id}} : {H}_{c}^{ * }\left( M\right)  \rightarrow  {H}_{c}^{ * }\left( M\right) .
\]

但是,

\[
{e}_{ * } \circ  {\pi }_{ * } \neq  \mathrm{{id}} : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) .
\]

为此定义同伦算子 \( K : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{* - 1}\left( {M \times  {\mathbb{R}}^{1}}\right) \) 为

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right)  \mapsto  0 \) (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \mapsto  {\pi }^{ * }\phi  \cdot  {\int }_{-\infty }^{t}f\left( {x, u}\right) {du} \)

\[
- {\pi }^{ * }\phi  \cdot  A\left( t\right)  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}
\]

其中 \( A\left( t\right)  = {\int }_{-\infty }^{t}e\left( u\right) {du} \) .

命题 4.6. \( K \) 确实是同伦算子.

\[
{id} - {e}_{ * } \circ  {\pi }_{ * } = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right)  : {\Omega }_{c}^{q}\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{q}\left( {M \times  {\mathbb{R}}^{1}}\right) .
\]

证. (I) \( \omega  = {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) ,\deg \phi  = q \) .

\( \left( {1 - {e}_{ * }{\pi }_{ * }}\right) \omega  = \omega . \)

\[
\left( {{dK} - {Kd}}\right) \omega  =  - K\left( {{\pi }^{ * }{d\phi } \cdot  f\left( {x, t}\right)  + {\left( -1\right) }^{q}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f\left( {x, t}\right) }{\partial {x}_{i}}d{x}_{i}}\right.
\]

\[
\left. {+{\left( -1\right) }^{q}{\pi }^{ * }\phi  \land  \frac{\partial f\left( {x, t}\right) }{\partial t}{dt}}\right)
\]

\[
=  - K\left( {{\left( -1\right) }^{q}{\pi }^{ * }\phi  \land  \frac{\partial f\left( {x, t}\right) }{\partial t}{dt}}\right)
\]

\[
= {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi {\int }_{-\infty }^{t}\frac{\partial f\left( {x, u}\right) }{\partial u}{du}
\]

\[
+ {\left( -1\right) }^{q}{\pi }^{ * }\phi  \cdot  A\left( t\right)  \cdot  {\int }_{-\infty }^{\infty }\frac{\partial f\left( {x, t}\right) }{\partial t}{dt}
\]

\[
= {\left( -1\right) }^{q - 1}\omega .
\]

因为 \( f\left( {x, t}\right) \) 有紧支集,所以对给定的 \( x \in  M \) ,

(II) \( \omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt} \) , deg \( \phi  = q - 1 \) .

\[
\left( {1 - {e}_{ * }{\pi }_{ * }}\right) \left( \omega \right)  = \omega  - {\pi }^{ * }\left( {\phi  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}}\right)  \land  e.
\]

\[
{dK}\left( \omega \right)  = d\left( {{\pi }^{ * }\phi  \cdot  {\int }_{-\infty }^{t}f\left( {x, u}\right) {du} - {\pi }^{ * }\phi  \cdot  A\left( t\right)  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}}\right)
\]

\[
= {\pi }^{ * }{d\phi } \cdot  {\int }_{-\infty }^{t}f\left( {x, u}\right) {du}\left( 1\right)  + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  f\left( {x, t}\right) {dt}\left( { = \omega }\right)
\]

\[
+ {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i} \cdot  {\int }_{-\infty }^{t}\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}\left( 2\right)
\]

\[
- {\pi }^{ * }{d\phi } \cdot  A\left( t\right)  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}\left( 3\right)  + {\left( -1\right) }^{q}{\pi }^{ * }\phi  \land  e \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}
\]

\[
+ {\left( -1\right) }^{q}{\pi }^{ * }\phi  \cdot  A\left( t\right)  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i} \cdot  {\int }_{-\infty }^{\infty }\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}\left( 4\right) ;
\]

\[
{Kd}\left( \omega \right)  = K\left( {{\pi }^{ * }{d\phi } \land  f\left( {x, t}\right) {dt} + {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i} \land  \frac{\partial f\left( {x, t}\right) }{\partial {x}_{i}}{dt}}\right.
\]

\[
= {\pi }^{ * }{d\phi }{\int }_{-\infty }^{t}f\left( {x, u}\right) {du}\left( 1\right)  - {\pi }^{ * }{d\phi } \cdot  A\left( t\right)  \cdot  {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}\left( 3\right)
\]

\[
+ {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i} \cdot  {\int }_{-\infty }^{t}\frac{\partial f\left( {x, u}\right) }{\partial {x}_{i}}{du}\left( 2\right)
\]

\[
+ {\left( -1\right) }^{q}{\pi }^{ * }\phi  \cdot  A\left( t\right)  \cdot  \mathop{\sum }\limits_{{i = 1}}^{n}d{x}_{i} \cdot  {\int }_{-\infty }^{\infty }\frac{\partial f\left( {x, t}\right) }{\partial {x}_{i}}{dt}\left( 4\right) .
\]

命题 4.7. \( {H}_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) \overset{{\pi }_{ * }}{\underset{{e}_{ * }}{ \rightleftarrows  }}{H}_{c}^{* - 1}\left( M\right) \) 是同构.

推论 4.7.1.(紧支集的 Poincaré 引理)

\[
{H}_{c}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = n \\  0 & q \neq  n. \end{array}\right.
\]

此处同构 \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right)  \simeq  \mathbb{R} \) 是通过将重积分化为累次积分实现的. 反之,由上述构造可知, \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 的生成元 \( \left\lbrack  \alpha \right\rbrack \) 的代表元 \( \alpha  \in  {\Omega }_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 可用以下方法得到.

\[
{\Omega }_{c}^{0}\left( \cdot \right) \overset{{e}_{ * }}{ \rightarrow  }{\Omega }_{c}^{1}\left( {\mathbb{R}}^{1}\right) \overset{{e}_{ * }}{ \rightarrow  }{\Omega }_{c}^{2}\left( {\mathbb{R}}^{2}\right) \overset{{e}_{ * }}{ \rightarrow  }\cdots \overset{{e}_{ * }}{ \rightarrow  }{\Omega }_{c}^{n}\left( {\mathbb{R}}^{n}\right) .
\]

\( 1 \mapsto  e\left( {x}_{1}\right) d{x}_{1} \mapsto  e\left( {x}_{1}\right) e\left( {x}_{2}\right) d{x}_{1} \land  d{x}_{2} \mapsto  \cdots  \mapsto  e\left( {x}_{1}\right) \ldots e\left( {x}_{n}\right) d{x}_{1} \land  \cdots  \land  d{x}_{n}. \)

\[
\alpha  = e\left( {x}_{1}\right) \ldots e\left( {x}_{n}\right) d{x}_{1} \land  \cdots  \land  d{x}_{n}.
\]

它是 \( {\mathbb{R}}^{n} \) 上一个 bump \( n \) -形式且 \( {\int }_{{\mathbb{R}}^{n}}\alpha  = 1 \) . 因为每个 \( e\left( {x}_{i}\right) \) 的支集可任意小,所以 \( \alpha \) 的支集可任意小.

练习 4.8. 设 \( M \) 是开 Möbius 带. 计算 \( {H}^{ * }\left( M\right) \) ， \( {H}_{c}^{ * }\left( M\right) \) .

逆紧映射的度作为对紧支集的 Poincaré 引理的一个应用，引进相同维数的两个欧氏空间之间的逆紧映射的一个光滑不变量. 在 Poincaré 对偶之后, 这个不变量将被推广到任意两个相同维数的定向流形之间的逆紧映射. 对紧流形逆紧性的假定显然是多余的.

设 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是光滑逆紧映射. 则 \( {f}^{ * } : {\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right) \) . 它诱导映射

\[
{f}^{ * } : {H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right) .
\]

设 \( \left\lbrack  \alpha \right\rbrack   \in  {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 是生成元，即 \( \left\lbrack  \alpha \right\rbrack \) 有代表元 \( \alpha \) ，它是具紧支集的闭 \( n \) -形式且 \( {\int }_{{\mathbb{R}}^{n}}\alpha  = 1 \) . 则 \( {f}^{ * }\left\lbrack  \alpha \right\rbrack   = c\left\lbrack  \alpha \right\rbrack \) . 常数 \( c \) 称为映射 \( f \) 的度 (degree),记作 deg \( f \) . 显然

\[
\deg f = {\int }_{{\mathbb{R}}^{n}}{f}^{ * }\alpha
\]

先验地 \( \deg f \in  \mathbb{R} \) . 令人神奇的是

\[
\deg f \in  \mathbb{Z}\text{ . }
\]

证明需用 Sard 定理. 设 \( f : {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{n} \) 是光滑映射. 记 \( {f}_{*p} \) 为 \( f \) 在点 \( p \) 的切映射, 它把点 \( p \) 的切向量映为点 \( f\left( p\right) \) 的切向量,即 \( {f}_{*p} : {T}_{p}{\mathbb{R}}^{m} \rightarrow  {T}_{f\left( p\right) }{\mathbb{R}}^{n} \) . 它是线性映射. 若 \( {f}_{*p} \) 不是满射,则称点 \( p \) 是 \( f \) 的临界点, \( f\left( p\right) \) 是临界值. \( {\mathbb{R}}^{n} \) 中不是临界值的点称为正则值. 所以正则值的逆像可能是空集.

定理 4.9. (对 \( {\mathbb{R}}^{n} \) 的 Sard 定理) 对任意正整数 \( m \) , \( n \) ,光滑映射 \( f : {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{n} \) 的临界值集是 \( {\mathbb{R}}^{n} \) 的零测集.

命题 4.10. 设 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是光滑逆紧映射. 若 \( f \) 不是满射,则 \( \deg f = 0 \) .

证. 因为 \( f \) 是逆紧映射,所以 \( f\left( {\mathbb{R}}^{n}\right) \) 是闭集,即 \( {\mathbb{R}}^{n} - f\left( {\mathbb{R}}^{n}\right) \) 是开集. 若 \( f \) 不是满射,则存在点 \( q \in  {\mathbb{R}}^{n} - f\left( {\mathbb{R}}^{n}\right) \) . 所以存在开集 \( U \) 使得 \( U \subset  {\mathbb{R}}^{n} - f\left( {\mathbb{R}}^{n}\right) \) . 选取生成元 \( \left\lbrack  \alpha \right\rbrack   \in  {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 的代表元 \( \alpha \) 使得 Supp \( \alpha  \subset  U \) . 则 \( {f}^{ * }\alpha  = 0 \) . 故 \( \deg f = {\int }_{{\mathbb{R}}^{n}}{f}^{ * }\alpha  = 0. \)

练习 4.10.1. 证明逆紧映射 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 的像 \( f\left( {\mathbb{R}}^{n}\right) \) 是闭集. 命题. 设 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是光滑逆紧映射. 则 \( \deg f \in  \mathbb{Z} \) .

证. 现设 \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) 是满射. 由 Sard 定理, \( f\left( {\mathbb{R}}^{n}\right) \) 中几乎处处所有的点是正则值. 设 \( q \in  f\left( {\mathbb{R}}^{n}\right) \) 是 \( f \) 的正则值. 由假定知 \( {f}^{-1}\left( q\right) \) 非空. 设 \( p \in  {f}^{-1}\left( q\right) \) .

因为 \( {f}_{*p} \) 是线性映射且是满射,所以 \( {f}_{*p} \) 是同构. 根据反函数定理, \( f \) 在点 \( p \) 附近是一个局部微分同胚. 所以 \( {f}^{-1}\left( q\right) \) 是离散集. 又因为 \( f \) 逆紧, \( {f}^{-1}\left( q\right) \) 是紧集,所以 \( {f}^{-1}\left( q\right) \) 只能是有限点集,设为

\[
{f}^{-1}\left( q\right)  = \left\{  {{p}_{1},\ldots ,{p}_{N}}\right\}  .
\]

因为 \( f \) 在点 \( {p}_{i} \) 附近是局部微分同胚,即存在包含点 \( {p}_{i} \) 的开集 \( {U}_{i} \) 使得 \( f : {U}_{i} \rightarrow \; f\left( {U}_{i}\right) \) 是微分同胚. 选取每个 \( {U}_{i} \) 充分小使得对任意的 \( i \neq  j,{U}_{i} \cap  {U}_{j} = \varnothing \) .

因为 \( f \) 逆紧，存在点 \( q \) 的充分小邻域 \( V \) 使得

\[
{f}^{-1}\left( V\right)  \subset  \mathop{\bigcup }\limits_{{i = 1}}^{N}{U}_{i}
\]

选取生成元 \( \left\lbrack  \alpha \right\rbrack   \in  {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 的代表元 \( \alpha \) 使得 \( \operatorname{Supp}\alpha  \subset  V \) . 则

\[
\text{ Supp }{f}^{ * }\alpha  \subset  \mathop{\bigcup }\limits_{{i = 1}}^{N}{U}_{i}\text{ . }
\]

又因为 \( {\left. f\right| }_{{U}_{i}} \) 是微分同胚，所以

\[
{\int }_{{U}_{i}}{f}^{ * }\alpha  =  \pm  {\int }_{f\left( {U}_{i}\right) }\alpha  =  \pm  1,
\]

此处正负号由微分同胚 \( {\left. f\right| }_{{U}_{i}} \) 的 Jacobi 行列式的正负号确定. 于是

\[
{\int }_{{\mathbb{R}}^{n}}{f}^{ * }\alpha  = \mathop{\sum }\limits_{{i = 1}}^{N}{\int }_{{U}_{i}}{f}^{ * }\alpha  = \mathop{\sum }\limits_{{{f}^{-1}\left( q\right) }} \pm  1 \in  \mathbb{Z}.
\]

作业:

1. 练习 4.2.

2. 练习 4.3.

3. 补充练习 1.

4. 练习 4.3.1.

5. 补充练习 2.

6. 练习 4.5.

7. 练习 4.8.

8. 练习 4.10.1.

代数拓扑与微分形式
