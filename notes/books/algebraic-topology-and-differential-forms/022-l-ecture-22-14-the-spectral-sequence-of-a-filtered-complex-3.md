#### 22. 谱序列的应用

\( \text{ § }{14} \) The Spectral Sequence of a Filtered Complex (3)

## 22. 谱序列的应用

我们已经讲了谱序列与它的收敛性, 双复形的谱序列, de Rham 上同调的 Leray 定理. 这次课讲谱序列的一些应用, 积结构以及 Leray 构造.

- 一些应用

- 积结构

- Leray 构造

一些应用

例 14.19. (Künneth 公式与 Leray-Hirsch 定理) 现给出 Künneth 公式 (5.9) 的谱序列证明.

设 \( M \) , \( F \) 是流形, \( \mathcal{U} \) 是 \( M \) 的好覆盖. 假定 \( F \) 有有限维上同调. 根据 Leray 定理 (14.18), \( M \) 上以 \( F \) 为纤维的平凡丛 \( M \times  F \rightarrow  M \) 的双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) 的谱序列的 \( {E}_{2} \) 页为

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( F\right) }\right) .
\]

因为 \( M \times  F \) 是 \( M \) 上平凡丛,预层 \( {\mathcal{H}}^{q}\left( F\right) \) 是常值预层 \( {H}^{q}\left( F\right) \) . 又因为 \( F \) 有有限维上同调, 所以

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  \otimes  {H}^{q}\left( F\right)  = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) .
\]

对 \( b \in  {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) , \( b \) 能活到最后当且仅当 \( b \) 能延拓为一个 \( D \) -上闭链,而 \( {d}_{r}{\left\lbrack  b\right\rbrack  }_{r} = \left\lbrack  {\delta {c}_{r - 1}}\right\rbrack   = 0 \) 表示活到 \( {E}_{r} \) 的元 \( b \) 能继续活下去,即在延拓为一个 \( D \) -上闭链的路上能再向前走一步.

现因为 \( {E}_{2} \) 页的每个元已经是 \( M \times  F \) 上一个整体闭形式,所以对 \( {\left\lbrack  b\right\rbrack  }_{2} \in  {E}_{2}^{p, q} \) ,存在 \( {c}_{1} \in  {C}^{p + 1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{q - 1}}\right) \) 使得 \( b + {c}_{1} \) 已经是一个 \( D \) -上闭链了,即

![bo_d7e85t491nqc73eqefm0_504_845_616_569_531_0.jpg](images/fu_algebraic_topology_and_differential_forms_139_bod7e85t491nqc73eqefm05048456165695310.jpg)

根据 \( {d}_{r} \) 的定义, \( {d}_{2} = {d}_{3} = \cdots  = 0 \) . 于是 \( {E}_{2} = {E}_{\infty } \) . 根据定理 14.18, \( {E}_{\infty } = {H}^{ * }\left( {M \times  F}\right) \) . 因此有 Künneth 公式

\[
{H}^{ * }\left( {M \times  F}\right)  = {E}_{\infty } = {E}_{2} = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

Leray-Hirsch 定理的证明是类似的.

注记 14.20. (球面丛的可定向性与欧拉类) 设 \( \pi  : E \rightarrow  M \) 是流形 \( M \) 上 \( {S}^{n} \) -丛, \( \mathcal{U} \) 是 \( M \) 的好覆盖. 因为

\[
{\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = 0, n \\  0 & q \neq  0, n \end{array}\right.
\]

所以这个纤维丛的谱序列的 \( {E}_{1} \) 页为

\[
{E}_{1}^{p, q} = {H}_{d}^{p, q} = {C}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( {S}^{n}\right) }\right)  =
\]

![bo_d7e85t491nqc73eqefm0_505_1180_676_857_745_0.jpg](images/fu_algebraic_topology_and_differential_forms_140_bod7e85t491nqc73eqefm050511806768577450.jpg)

设 \( {\left\lbrack  \sigma \right\rbrack  }_{1} \in  {E}_{1}^{0, n} = {C}^{0}\left( {\mathcal{U},{\mathcal{H}}^{n}\left( {S}^{n}\right) }\right) \) 对应于球面丛 \( E \) 上局部角形式. \( E \) 是可定向的当且仅当存在这样的 \( {\left\lbrack  \sigma \right\rbrack  }_{1} \) 使得 \( {d}_{1}{\left\lbrack  \sigma \right\rbrack  }_{1} = 0 \) ,即 \( {\left\lbrack  \sigma \right\rbrack  }_{2} \in  {E}_{2}^{0, n} \) .

现设 \( E \) 是可定向的, \( {\left\lbrack  \sigma \right\rbrack  }_{1} \in  {E}_{1}^{0, n} \) 是一个定向. 所以 \( {\left\lbrack  \sigma \right\rbrack  }_{2} \in  {E}_{2}^{0, n} \) . 因为 \( {E}_{1} \) 页只有第 \( n \) 行与第 0 行非零,所以 \( {d}_{2} = \cdots  = {d}_{n} = 0 \) . 于是

\[
{E}_{n + 1} = {E}_{2} = {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathcal{U},{\mathcal{H}}^{ * }\left( {S}^{n}\right) }\right)  =
\]

![bo_d7e85t491nqc73eqefm0_506_1322_575_841_701_0.jpg](images/fu_algebraic_topology_and_differential_forms_141_bod7e85t491nqc73eqefm050613225758417010.jpg)

\( \sigma \) 能活到 \( {E}_{n + 1},{\left\lbrack  \sigma \right\rbrack  }_{n + 1} \in  {E}_{n + 1}^{0, n} \) .

因为

\[
{d}_{n + 1} : {E}_{n + 1}^{0, n} \rightarrow  {E}_{n + 1}^{n + 1,0} = {E}_{2}^{n + 1,0} = {H}_{\delta }^{n + 1}\left( {\mathcal{U},{\mathcal{H}}^{0}\left( {S}^{n}\right) }\right)
\]

\[
= {H}^{n + 1}\left( {{\pi }^{-1}\mathcal{U},\mathbb{R}}\right)  = {H}^{n + 1}\left( M\right) ,
\]

所以

\[
- {d}_{n + 1}{\left\lbrack  \sigma \right\rbrack  }_{n + 1} = {\left\lbrack  -\delta {\sigma }_{n}\right\rbrack  }_{n + 1} \in  {H}^{n + 1}\left( M\right)
\]

是球面丛的欧拉类. 它是否等于零当且仅当 \( \sigma \) 能否延拓为一个 \( D \) -上闭链,即球面丛上整体闭 \( n \) -形式.

例 14.21. (单连通流形的可定向性) 设 \( M \) 是 \( n \) 维单连通流形, \( S\left( {TM}\right) \) 是其单位切丛. 根据对 de Rham 上同调的 Leray 定理, 纤维丛

![bo_d7e85t491nqc73eqefm0_508_888_329_549_296_0.jpg](images/fu_algebraic_topology_and_differential_forms_142_bod7e85t491nqc73eqefm05088883295492960.jpg)

的谱序列的 \( {E}_{2} \) 页为

\[
\begin{matrix} {E}_{2}^{p, q} = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( {S}^{n - 1}\right)  = \\   \\  0 \end{matrix}\left\lbrack  \begin{matrix}  & & & & \\   & \mathbf{R} & & & \\   & & & & \\   & \mathbf{R} & & 0 & \\   & & & & \\   & & & & 0 \end{matrix}\right\rbrack
\]

因此 \( \dim {E}_{2}^{0, n - 1} = 1 \) . 设 \( {\left\lbrack  \sigma \right\rbrack  }_{2} \in  {E}_{2}^{0, n - 1} \) 是生成元. 则 \( {\left\lbrack  \sigma \right\rbrack  }_{1} \neq  0 \in  {E}_{1}^{0, n - 1} \) 且 \( {d}_{1}{\left\lbrack  \sigma \right\rbrack  }_{1} = {\left\lbrack  \delta \sigma \right\rbrack  }_{1} = 0 \) ,即 \( {d\sigma } = 0 \) 且 \( {\delta \sigma } =  - {D}^{\prime \prime }{\sigma }_{1} \) . 所以 \( {\left\lbrack  \sigma \right\rbrack  }_{1} \) 是 \( S\left( {TM}\right) \) 的一个定向. 因此 \( S\left( {TM}\right) \) 可定向,即 \( {TM} \) 可定向,从而 \( M \) 可定向. 这是用谱序列方法证明单连通流形的可定向性(推论 11.6).

例 14.22.(复射影空间的上同调)对纤维丛可用全空间的上同调与纤维的上同调计算底流形的上同调,我们来看一个例子. 考虑 \( {\mathbb{C}}^{n + 1} \) 中单位球面

\[
{S}^{{2n} + 1} = \{ \left( {{z}_{0},\ldots ,{z}_{n}}\right)  \in  {\mathbb{C}}^{n + 1} \mid  {\left| {z}_{0}\right| }^{2} + \cdots  + {\left| {z}_{n}\right| }^{2} = 1\} .
\]

设 \( {S}^{1} \) 在 \( {S}^{{2n} + 1} \) 上的作用为

\[
\left( {{z}_{0},\ldots ,{z}_{n}}\right)  \mapsto  \left( {\lambda {z}_{0},\ldots ,\lambda {z}_{n}}\right)
\]

其中 \( \lambda  \in  {S}^{1} \) 是模长为 1 的复数. \( {S}^{{2n} + 1} \) 在这个作用下的商空间是复射影空间 \( \mathbb{C}{P}^{n} \) . 所以 \( {S}^{{2n} + 1} \) 是 \( \mathbb{C}{P}^{n} \) 上圆周丛:

![bo_d7e85t491nqc73eqefm0_509_930_932_460_289_0.jpg](images/fu_algebraic_topology_and_differential_forms_143_bod7e85t491nqc73eqefm05099309324602890.jpg)

以后从纤维化的同伦正合序列 (17.4) 可知 \( \mathbb{C}{P}^{n} \) 是单连通的. 这样根据对 de Rham 上同调的 Leray 定理,

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathbb{C}{P}^{n}}\right)  \otimes  {H}^{q}\left( {S}^{1}\right) .
\]

所以 \( {E}_{2} \) 仅有两行,即当 \( q = 0,1 \) 时非零,并且两行都等于 \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) .

设 \( n = 2 \) . 则 \( {E}_{2} \) 页是

![bo_d7e85t491nqc73eqefm0_510_688_326_991_462_0.jpg](images/fu_algebraic_topology_and_differential_forms_144_bod7e85t491nqc73eqefm05106883269914620.jpg)

其中第 0 行是 \( \mathbb{C}{P}^{2} \) 的上同调,第 0 列是纤维 \( {S}^{1} \) 的上同调. 因为 \( \mathbb{C}{P}^{2} \) 是 4 维流形,所以对 \( p \geq  5,{H}^{p}\left( {\mathbb{C}{P}^{2}}\right)  = 0 \) . 因为 \( {d}_{3} \) 往下移两行,所以 \( {d}_{3} = 0 \) . 同理,

\[
{d}_{4} = {d}_{5} = \cdots  = 0\text{ . }
\]

所以谱序列在 \( {E}_{3} \) 页退化并且 \( {E}_{3} = {E}_{4} = \cdots  = {E}_{\infty } = {H}^{ * }\left( {S}^{5}\right) \) . 又因为

\[
{H}^{5}\left( {S}^{5}\right)  = {E}_{\infty }^{4,1} = {E}_{3}^{4,1},\;{H}^{0}\left( {S}^{5}\right)  = {E}_{\infty }^{0,0} = {E}_{3}^{0,0},
\]

所以 \( {E}_{3} \) 页是

<table><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>\( \mathbb{R} \)</td><td>0</td><td></td></tr><tr><td>0</td><td>\( \mathbb{R} \)</td><td>0</td><td>0</td><td>0</td><td></td><td>0</td><td></td></tr><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td></tr></table>

因为 \( {d}_{2} : {E}_{2}^{p,1} \rightarrow  {E}_{2}^{p + 2,0} \) ,而 \( {E}_{3} = \ker {d}_{2}/\mathrm{{im}}{d}_{2} \) ,所以

\[
{d}_{2} : \mathbb{R} \rightarrow  B,\;B \rightarrow  D,\;A \rightarrow  C,\;C \rightarrow  0
\]

都必须是同构. 于是 \( {E}_{2} \) 页是

![bo_d7e85t491nqc73eqefm0_512_683_448_998_469_0.jpg](images/fu_algebraic_topology_and_differential_forms_145_bod7e85t491nqc73eqefm05126834489984690.jpg)

因此

\[
{H}^{ * }\left( {\mathbb{C}{P}^{2}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} &  *  = 0,2,4 \\  0 &  *  \neq  0,2,4. \end{array}\right.
\]

练习 14.22.1. 证明

\[
{H}^{ * }\left( {\mathbb{C}{P}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} &  *  = 0,2,4,\ldots ,{2n} \\  0 &  *  = \text{ 其余情况 } \end{array}\right.
\]

积 (product) 结构这节我们在 Čech-de Rham 复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) , de Rham 上同调,与 Čech 上同调上定义积结构, 并证明 de Rham 与 Čech 之间的同构是分次代数的同构; 我们也在谱序列上讨论积结构. 设 \( M \) 是流形, \( \mathcal{U} \) 是其好覆盖.

(a) \( {\Omega }^{ * }\left( M\right) \) 上积结构: 外积 “ \( \land \) ”.

\[
\land   : {\Omega }^{q}\left( M\right)  \otimes  {\Omega }^{s}\left( M\right)  \rightarrow  {\Omega }^{q + s}\left( M\right) ,
\]

\[
\omega  \otimes  \eta  \mapsto  \omega  \land  \eta
\]

因为 \( d \) 是反导子(anti-derivation):

\[
d\left( {\omega  \land  \eta }\right)  = {d\omega } \land  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \land  {d\eta },
\]

所以 \( \land \) 诱导了 de Rham 上同调 \( {H}^{ * }\left( M\right) \) 上积结构 “ \( \land \) ” 使它成为分次代数.

\[
\land   : {H}^{q}\left( M\right)  \otimes  {H}^{s}\left( M\right)  \rightarrow  {H}^{q + s}\left( M\right)
\]

\[
\left\lbrack  \omega \right\rbrack   \otimes  \left\lbrack  \eta \right\rbrack   \mapsto  \left\lbrack  {\omega  \land  \eta }\right\rbrack
\]

(b) \( {C}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 上积结构: 乘法 ".".

\[
\cdot   : {C}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  \otimes  {C}^{r}\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  {C}^{p + r}\left( {\mathcal{U},\mathbb{R}}\right) ,
\]

\[
\omega  \otimes  \eta  \mapsto  \omega  \cdot  \eta
\]

(14.27)

\[
{\left( \omega  \cdot  \eta \right) }_{{\alpha }_{0}{\alpha }_{1}\ldots {\alpha }_{p + r}} = {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \cdot  {\eta }_{{\alpha }_{p}\ldots {\alpha }_{p + r}},
\]

其中右边的乘法是普通乘法.

微分算子 \( \delta \) 相对于乘法 “.” 是反导子:

\[
\delta \left( {\omega  \cdot  \eta }\right)  = {\delta \omega } \cdot  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cdot  {\delta \eta }.
\]

因此乘法 “.” 诱导了 \( {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 上积结构 “.” 使之成为分次代数.

\[
\cdot   : {H}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  \otimes  {H}^{r}\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  {H}^{p + r}\left( {\mathcal{U},\mathbb{R}}\right)
\]

\[
\left\lbrack  \omega \right\rbrack   \otimes  \left\lbrack  \eta \right\rbrack   \mapsto  \left\lbrack  {\omega  \cdot  \eta }\right\rbrack
\]

微分算子 \( \delta \) 相对于乘法 “.” 是反导子的证明.

\[
{\left( \delta \left( \omega  \cdot  \eta \right) \right) }_{{\alpha }_{0}{\alpha }_{1}\ldots {\alpha }_{p + r}{\alpha }_{p + r + 1}}
\]

\[
= \mathop{\sum }\limits_{{0 \leq  i \leq  p + r + 1}}{\left( -1\right) }^{i}{\left( \omega  \cdot  \eta \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\cdots {\alpha }_{p + r + 1}}
\]

\[
= \mathop{\sum }\limits_{{0 \leq  i \leq  p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}} \cdot  {\eta }_{{\alpha }_{p + 1}\ldots {\alpha }_{p + r + 1}}
\]

\[
+ \mathop{\sum }\limits_{{p \leq  i \leq  p + r + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \cdot  {\eta }_{{\alpha }_{p}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + r + 1}}
\]

\[
= {\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} \cdot  {\eta }_{{\alpha }_{p + 1}\ldots {\alpha }_{p + r + 1}} + {\left( -1\right) }^{\deg \omega }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \cdot  {\left( \delta \eta \right) }_{{\alpha }_{p}\ldots {\alpha }_{p + r + 1}}
\]

\[
= {\left( \delta \omega  \cdot  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cdot  \delta \eta \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + r + 1}}.
\]

(c) \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 上积结构: 杯积 " \( \cup \) ".

\[
\cup   : {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)  \otimes  {C}^{r}\left( {\mathcal{U},{\Omega }^{s}}\right)  \rightarrow  {C}^{p + r}\left( {\mathcal{U},{\Omega }^{q + s}}\right)
\]

\[
{4.24})\;{\left( \omega  \cup  \eta \right) }_{{\alpha }_{0}...{\alpha }_{p + r}} = {\left( -1\right) }^{qr}{\omega }_{{\alpha }_{0}...{\alpha }_{p}}{\left| {}_{{U}_{{\alpha }_{0}...{\alpha }_{p + r}}} \land  {\eta }_{{\alpha }_{p}...{\alpha }_{p + r}}\right| }_{{U}_{{\alpha }_{0}...{\alpha }_{p + r}}}.
\]

注记 14.25. 符号 \( {\left( -1\right) }^{qr} \) 是分次代数的需要,因为要把指标的顺序 \( \left( {p, q}\right) ,\left( {r, s}\right) \) 变成顺序 \( \left( {p, r}\right) ,\left( {q, s}\right) \) .

练习 14.26. 设 \( \omega  \in  {K}^{p, q},\eta  \in  {K}^{r, s},\deg \omega  = p + q \) . 证明:

1) \( \delta \left( {\omega  \cup  \eta }\right)  = {\delta \omega } \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {\delta \eta } \)

2) \( {D}^{\prime \prime }\left( {\omega  \cup  \eta }\right)  = {D}^{\prime \prime }\omega  \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {D}^{\prime \prime }\eta \)

3) \( D\left( {\omega  \cup  \eta }\right)  = {D\omega } \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {D\eta } \)

4) \( \delta {D}^{\prime \prime } + {D}^{\prime \prime }\delta  = 0 \) .

因此 U 诱导了 \( {H}_{D}^{ * }\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\} \) 上积结构. 显然,由构造知当 \( \cup \) 限制到 \( {\Omega }^{ * } \) 上,即为其上积结构 \( \land \) ; 限制到 \( {C}^{p}\left( {\mathcal{U},\mathbb{R}}\right) \) 上,即为其上积结构. . 这就是说, 包含映射

\[
r : {\Omega }^{ * }\left( M\right)  \rightarrow  {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)
\]

\[
i : {C}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)
\]

是代数同态. 所以对好覆盖 \( \mathcal{U} \) ,它们诱导的同构

\[
{H}_{dR}^{ * }\left( M\right) \overset{ \sim  }{ \rightarrow  }{H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}
\]

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \overset{ \sim  }{ \rightarrow  }{H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}
\]

是代数同构. 又因为对好覆盖 \( \mathcal{U},{H}^{ * }\left( {M,\mathbb{R}}\right)  = {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) ,所以我们有以下定理.

定理 14.28. de Rham 与 Čech 之间的同构

\[
{H}_{dR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {M,\mathbb{R}}\right)
\]

是分次代数的同构. 若双复形 \( K \) 有积结构且它的微分 \( D \) 相对于此积结构是反导子,则谱序列中的每个群 \( {E}_{r} \) 也有积结构且微分算子 \( {dr} \) 相对于此积结构也是反导子,这是因为 \( {E}_{r} \) 是 \( {E}_{r - 1} \) 的同调且 \( {d}_{r} \) 从 \( D \) 诱导而来. 附加上积结构,双复形的谱序列定理 14.14 变为

定理 14.29. 设 \( K \) 是双复形,具有一个积结构且微分算子 \( D \) 相对于这个积结构是反导子. 则存在收敛于 \( {H}_{D}\left( K\right) \) 的谱序列

\[
\left\{  {{E}_{r},{d}_{r}}\right\}  ,\;\text{ 其中 }{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1},
\]

具有以下性质:

1) \( {E}_{2}^{p, q} \) 页是 \( {H}_{\delta }^{p, q}{H}_{d}\left( K\right) \) ;

2) 作为前一个 \( {E}_{r - 1} \) 的同调,每个 \( {E}_{r} \) 从 \( {E}_{r - 1} \) 继承了一个积结构. \( {d}_{r} \) 相对于此积结构是反导子.

警示. 虽然 \( {E}_{\infty } \) 与 \( {H}_{D}\left( K\right) \) 都从 \( K \) 继承了它们的环结构,但它们作为环一般是不同构的.

练习 14.30. 在两个分次环 \( A \) 与 \( B \) 的张量积 \( A \otimes  B \) 上定义积结构:对 \( a, c \in  A \) ， \( b, d \in  B, \)

\[
\left( {a \otimes  b}\right) \left( {c \otimes  d}\right)  = {\left( -1\right) }^{\left( {\deg b}\right) \left( {\deg c}\right) }\left( {{ac} \otimes  {bd}}\right) .
\]

证明若 \( \pi  : E \rightarrow  M \) 是单连通流形 \( M \) 上以 \( F \) 为纤维的纤维丛,且 \( F \) 的上同调维数是有限的,则谱序列的 \( {E}_{2} \) 页与 \( {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) 的同构是分次代数的同构.

注记 14.31. 这样,在 Leray 定理,即定理 14.18 中每个群 \( {E}_{r} \) 是一个代数而 \( {d}_{r} \) 相对于此代数结构是反导子; 另外,若 \( M \) 是单连通的且 \( F \) 的上同调维数是有限的, 则同构 \( {E}_{2} \simeq  {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) 是分次代数的同构.

例 14.32. \( \left( {{H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) }\right. \) 的环结构) 假定 \( n = 2 \) . 在例 14.22 中,通过应用纤维丛

![bo_d7e85t491nqc73eqefm0_520_968_410_389_293_0.jpg](images/fu_algebraic_topology_and_differential_forms_147_bod7e85t491nqc73eqefm05209684103892930.jpg)

的谱序列计算了分次代数 \( {H}^{ * }\left( {\mathbb{C}{P}^{2}}\right) \) 的加法结构,发现 \( {E}_{2} \) 页是

![bo_d7e85t491nqc73eqefm0_520_657_870_1005_469_0.jpg](images/fu_algebraic_topology_and_differential_forms_146_bod7e85t491nqc73eqefm052065787010054690.jpg)

并且如上所示的两个 \( {d}_{2} \) 都是同构.

设 \( a \) 是

\[
{E}_{2}^{0,1} \simeq  {H}^{0}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{1}\left( {S}^{1}\right)  \simeq  {H}^{1}\left( {S}^{1}\right)
\]

的生成元. 则 \( {d}_{2}a = x \) 是

\[
{E}_{2}^{2,0} \simeq  {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{0}\left( {S}^{1}\right)  \simeq  {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)
\]

的生成元, \( x \cup  a \) 是

\[
{E}_{2}^{2,1} = {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{1}\left( {S}^{1}\right)
\]

的生成元.

![bo_d7e85t491nqc73eqefm0_521_658_1122_1004_468_0.jpg](images/fu_algebraic_topology_and_differential_forms_148_bod7e85t491nqc73eqefm0521658112210044680.jpg)

因为 \( {d}_{2} : {E}_{2}^{2,1} \rightarrow  {E}_{2}^{4,0} \) 是同构,所以 \( {E}_{2}^{4,0} = {H}^{4}\left( {\mathbb{C}{P}^{2}}\right) \) 的生成元是

\[
{d}_{2}\left( {x \cup  a}\right)  = {d}_{2}x \cup  a + x \cup  {d}_{2}a
\]

\( = x \cup  x \) 作为 \( {E}_{2}^{4,0} \) 的元 \( = x \land  x \) 作为 \( {H}^{4}\left( {\mathbb{C}{P}^{2}}\right) \) 的元 \( = x \cdot  x \) 作为 \( {H}^{4}\left( {\mathcal{U},\mathbb{R}}\right) \) 的元

\[
= {x}^{2}\text{ . }
\]

所以作为环

\[
{H}^{ * }\left( {\mathbb{C}{P}^{2}}\right)  = \mathbb{R}\left\lbrack  x\right\rbrack  /\left( {x}^{3}\right) ,\;\dim x = 2.
\]

一般地,用相同的讨论可得 \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) 的环结构:

\[
{H}^{ * }\left( {\mathbb{C}{P}^{n}}\right)  = \mathbb{R}\left\lbrack  x\right\rbrack  /\left( {x}^{n + 1}\right) ,\;\dim x = 2.
\]

Leray 构造现考虑任意光滑映射 \( \pi  : X \rightarrow  Y \) ,研究 \( X \) 的上同调如何与 \( Y \) 的上同调相联系.

设 \( \mathcal{U} \) 是 \( Y \) 的开覆盖,不必是好覆盖. 则 \( {\pi }^{-1}\mathcal{U} \) 是 \( X \) 的开覆盖. 根据 MV 原理, 即命题 8.8 或 14.16，

\[
{H}^{ * }\left( X\right)  = {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

根据定理 14.14,若 \( K \) 记 \( X \) 上双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) ,则 \( K \) 的谱序列有

\[
{E}_{\infty } = {H}_{D}\left( K\right)
\]

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p, q}{H}_{d}\left( K\right)
\]

此处

\[
{H}_{d}^{p, q}\left( K\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}^{q}\left( {{\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) }\right)  = {C}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right) ,
\]

其中 \( {\mathcal{H}}^{q} \) 是 \( Y \) 上预层,定义为 \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) . 总之,存在一个收敛于 \( {H}^{ * }\left( X\right) \) 的谱序列,它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right) .
\]

这种情形与纤维丛情形之间的主要差别在于预层 \( {\mathcal{H}}^{q} \) 不再是 \( \mathcal{U} \) 上局部常值预层； 确实,对不同的可缩开集 \( U \) ,上同调 \( {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) 一般是不同的.

例 14.34. 考虑从圆周 \( {S}^{1} \) 到线段 \( I \) 的投射. 如图用三个开集 \( {U}_{0},{U}_{1},{U}_{2} \) 组成了 \( I \) 的一个开覆盖 \( \mathcal{U} \) .

![bo_d7e85t491nqc73eqefm0_524_930_850_457_444_0.jpg](images/fu_algebraic_topology_and_differential_forms_150_bod7e85t491nqc73eqefm05249308504574440.jpg)

![bo_d7e85t491nqc73eqefm0_524_922_1320_482_210_0.jpg](images/fu_algebraic_topology_and_differential_forms_149_bod7e85t491nqc73eqefm052492213204822100.jpg)

\( {\mathrm{U}}_{1} \)

\( \mathcal{U} \) 上预层 \( {\mathcal{H}}^{0} \) 对 nerve \( N\left( \mathcal{U}\right) \) 的每个顶点与每条边赋予群如下:

\[
{\mathcal{H}}^{0}\left( {U}_{0}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{0}\right) }\right)  = \mathbb{R}
\]

\[
{\mathcal{H}}^{0}\left( {U}_{1}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{1}\right) }\right)  = {\mathbb{R}}^{2}
\]

\[
{\mathcal{H}}^{0}\left( {U}_{2}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{2}\right) }\right)  = \mathbb{R}
\]

\[
{\mathcal{H}}^{0}\left( {U}_{01}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{01}\right) }\right)  = {\mathbb{R}}^{2}
\]

\[
{\mathcal{H}}^{0}\left( {U}_{12}\right)  = {H}^{0}\left( {{\pi }^{-1}\left( {U}_{12}\right) }\right)  = {\mathbb{R}}^{2}
\]

![bo_d7e85t491nqc73eqefm0_525_803_227_738_253_0.jpg](images/fu_algebraic_topology_and_differential_forms_151_bod7e85t491nqc73eqefm05258032277382530.jpg)

双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) 的 \( {H}_{d} \) 是

\[
{H}_{d}^{q}\left\{  {{C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}   = \left\{  \begin{array}{ll} {C}^{p}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) & p = 0,1, q = 0 \\  0 & \text{ 其余情形, } \end{array}\right.
\]

其中

\[
{C}^{0}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right)  = \mathbb{R} \oplus  {\mathbb{R}}^{2} \oplus  \mathbb{R}
\]

\[
{C}^{1}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right)  = {\mathbb{R}}^{2} \oplus  {\mathbb{R}}^{2}
\]

并且微分算子 \( \delta  : {C}^{0}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right)  \rightarrow  {C}^{1}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) \) 为

\[
\delta \left( {b,\left( {{c}_{1},{c}_{2}}\right) , d}\right)  = \left( {\left( {{c}_{1} - b,{c}_{2} - b}\right) ,\left( {d - {c}_{1}, d - {c}_{2}}\right) }\right) . \tag{52}
\]

所以

\[
\ker \delta  = \{ \left( {b,\left( {b, b}\right) , b}\right) \}  = \mathbb{R},\;\operatorname{im}\delta  = {\mathbb{R}}^{3}.
\]

于是

\[
{H}_{\delta }^{0,0}{H}_{d} = \mathbb{R},\;{H}_{\delta }^{1,0}{H}_{d} = \mathbb{R}.
\]

在这种情形 \( {E}_{2} = {E}_{\infty } \) 并由此得到 \( {S}^{1} \) 的上同调.

在 \( {C}^{1}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) \) 中找一个表示 \( {H}^{1}\left( {S}^{1}\right) \) 生成元的 1-上链. 在 \( {C}^{1}\left( {\mathcal{U},{\mathcal{H}}^{0}}\right) \) 中 \( 1 - \) 上链由四元组 \( \left( {\left( {r, s}\right) ,\left( {t, u}\right) }\right) \) 给定. 由 (52) 可读出这样一个四元组是恰当的当且仅当 \( r - s = u - t \) . 因此作为 \( {H}^{1}\left( {S}^{1}\right) \) 的一个生成元可取

\[
\left( {\left( {1,0}\right) ,\left( {0,0}\right) }\right) \text{ , }
\]

见下图，即一个 1-上链 \( \tau \) 使得

\[
\tau \left( {U}_{01}\right)  = \left( {1,0}\right)
\]

\[
\tau \left( {U}_{12}\right)  = \left( {0,0}\right)
\]

此处本来该用 \( {\tau }_{01} \) 等表示分量,但因为这种分量是局部常值函数,所以才有上述记号.

![bo_d7e85t491nqc73eqefm0_527_899_955_494_767_0.jpg](images/fu_algebraic_topology_and_differential_forms_152_bod7e85t491nqc73eqefm05278999554947670.jpg)

练习 14.35. 把球面 \( {S}^{2} \) 投射到单位圆盘 \( D \) 并用 Leray 方法计算 \( {H}^{ * }\left( {S}^{2}\right) \) .

![bo_d7e85t491nqc73eqefm0_528_983_588_367_360_0.jpg](images/fu_algebraic_topology_and_differential_forms_153_bod7e85t491nqc73eqefm05289835883673600.jpg)

![bo_d7e85t491nqc73eqefm0_528_992_964_354_332_0.jpg](images/fu_algebraic_topology_and_differential_forms_154_bod7e85t491nqc73eqefm05289929643543320.jpg)

练习 14.36. 设 \( Y \) 是流形，具有有限好覆盖 \( \mathcal{U} \) . 用 \( {\beta }_{p} \) 记 \( \left( {p + 1}\right) \) -重非空交 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) 的个数. 证明

\[
\chi \left( Y\right)  = \sum {\left( -1\right) }^{p}{\beta }_{p}
\]

练习 14.37. 设 \( \pi  : X \rightarrow  Y \) 是任意映射, \( \mathcal{U} \) 是 \( Y \) 的一个有限好覆盖. 证明

\[
\chi \left( X\right)  = \mathop{\sum }\limits_{{p, q}}\mathop{\sum }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\left( -1\right) }^{p + q}\dim {H}^{q}\left( {{\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) }\right) .
\]

证明若 \( \pi  : X \rightarrow  Y \) 是以 \( F \) 为纤维的纤维丛, \( Y \) 具有有限好覆盖且 \( F \) 具有有限维上同调, 则

\[
\chi \left( X\right)  = \chi \left( F\right) \chi \left( Y\right)
\]

作业:

1. 练习 14.22.1.

2. 练习 14.26.

3. 练习 14.30.

4. 练习 14.35

5. 练习 14.36

6. 练习 14.37.
