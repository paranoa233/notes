#### 17. 再论 Thom 同构

§12 Thom Isomorphism and Poincaré Duality Revisited (2)

## 17. 再论 Thom 同构

这次课首先应用 tic-tac-toe 引理证明 Thom 同构: 设 \( E \) 是流形 \( M \) 上秩 \( n \) 向量丛. 则

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{n}}\right) ,
\]

其中 \( \mathcal{U} \) 是 \( M \) 的好覆盖, \( {\mathcal{H}}_{cv}^{n} \) 是 \( M \) 上预层: \( {\mathcal{H}}_{cv}^{n}\left( U\right)  = {H}_{cv}^{n}\left( {E{ \mid  }_{U}}\right) \) . 在这个同构中不需要假定 \( M \) 具有有限好覆盖，也不需要假定 \( E \) 可定向. 接着讲定向向量丛 \( E \) 的 Thom 类与欧拉类的一些性质. 最后把定理 11.17 推广到向量丛的秩不等于流形维数的情形, 证明定向向量丛的欧拉类 Poincaré 对偶于横截面的零点集(zero locus).

- Thom 同构

- Thom 类与欧拉类的性质

- 欧拉类与截面的零点集

Thom 同构

我们已证以下的 Thom 同构定理, 即命题 6.17.

定理. 设 \( M \) 是有限型流形, \( \pi  : E \rightarrow  M \) 是秩 \( n \) 定向向量丛. 则

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( M\right)
\]

我们要推广上述定理,把 \( M \) 的有限型条件与 \( E \) 的可定向性条件去掉. 设 \( \mathcal{U} \) 是 \( M \) 的好覆盖. 则 \( {\pi }^{-1}\mathcal{U} \) 也是 \( E \) 的好覆盖. 考虑双复形

\[
{C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }_{cv}^{q}\left( {\left. E\right| }_{{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)
\]

与增广双复形

\[
0 \rightarrow  {\Omega }_{cv}^{ * }\left( E\right)  \rightarrow  {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{ * }}\right) .
\]

应用从属于 \( \mathcal{U} \) 的单位分解,可证每个增广行是正合的. 因此用命题 8.8 的证明方法可证增广列的上同调同构于双复形形成的复形的 \( D \) -上同调:

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{ * }}\right) }\right\}  . \tag{38}
\]

另一方面，第 \( p \) 列的紧垂直 \( d \) -上同调是

\[
{H}_{d}^{q}\left\{  {{C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{ * }}\right) }\right\}   = {H}_{cv}^{q}\left( {\mathop{\coprod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}E{ \mid  }_{{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}}\right)
\]

\[
= \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}_{cv}^{q}\left( {\left. E\right| }_{{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)
\]

\[
= {C}^{p}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{q}}\right) .
\]

此处 \( {\mathcal{H}}_{cv}^{q} \) 是定义在 \( M \) 上的预层:对任意开集 \( U \subset  M \) ，

\[
{\mathcal{H}}_{cv}^{q}\left( U\right)  = {H}_{cv}^{q}\left( {\left. E\right| }_{U}\right) .
\]

于是有开覆盖 \( \mathcal{U} \) 的取值于预层 \( {\mathcal{H}}_{cv}^{q} \) 的 Čech 上同调:

\[
{H}_{\delta }^{p}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{q}}\right)  = {H}_{\delta }^{p}\left\{  {{C}^{ * }\left( {\mathcal{U},{\mathcal{H}}_{cv}^{q}}\right) }\right\}   = {H}_{\delta }^{p, q}{H}_{d}^{*, q}. \tag{39}
\]

若 \( U \) 可缩,则 \( {\left. E\right| }_{U} \simeq  U \times  {\mathbb{R}}^{n} \) 也可缩. 由对紧垂直支集的 Poincaré 引理,即命题 6.16 可得

\[
{\mathcal{H}}_{cv}^{q}\left( U\right)  = {H}_{cv}^{q}\left( {U \times  {\mathbb{R}}^{n}}\right)  \simeq  {H}^{q - n}\left( U\right)  = \left\{  \begin{array}{ll} \mathbb{R} & q = n \\  0 & q \neq  n. \end{array}\right.
\]

因此 \( {H}_{\delta }^{p, q}{H}_{d}^{*, q} = {H}_{\delta }^{p}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{q}}\right) \) 仅有一行即第 \( n \) 行不为零. 由命题 12.1,可得

\[
{H}_{D}^{ * }\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{ * }}\right) }\right\}   = { \oplus  }_{p + q =  * }{H}_{\delta }^{p}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{q}}\right)  = {H}_{\delta }^{* - n}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{n}}\right) .
\]

结合 (38), 得到

定理 12.2.(Thom 同构)设 \( \pi  : E \rightarrow  M \) 是 \( M \) 上秩 \( n \) 向量丛, \( \mathcal{U} \) 是 \( M \) 的好覆盖. 则

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( {\mathcal{U},{\mathcal{H}}_{cv}^{n}}\right) ,
\]

其中 \( {\mathcal{H}}_{cv}^{n} \) 是 \( M \) 上的预层: \( {\mathcal{H}}_{cv}^{n}\left( U\right)  = {H}_{cv}^{n}\left( {\left. E\right| }_{U}\right) \) . 现由上述定理推出 Thom 同构定理的可定向性版本 (6.17). \( {\mathcal{H}}_{cv}^{n} \) 是好覆盖 \( \mathcal{U} \) 上局部常值预层的例子. 当 \( E \) 可定向时它其实是常值预层 \( \mathbb{R} \) .

引理. 当 \( E \) 可定向时, \( {\mathcal{H}}_{cv}^{n} \) 是好覆盖 \( \mathcal{U} \) 上常值预层 \( \mathbb{R} \) .

由此引理,定理 12.2 即化为命题 6.17: 对秩 \( n \) 定向向量丛 \( E \) ,

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( {\mathcal{U},\mathbb{R}}\right)  \simeq  {H}^{* - n}\left( M\right) .
\]

特别当 \( M \) 单连通时, \( \pi  : E \rightarrow  M \) 总是可定向的,所以上述同构成立.

引理的证明. \( E \) 上一个度量定义了 \( E \) 上“距离”函数 \( r \) 与球面丛 \( S\left( E\right) \) . 由于 \( E \) 可定向,球面丛 \( S\left( E\right) \) 可定向,即可选取 \( {H}^{n - 1}\left( {S\left( E\right) {|}_{{U}_{\alpha }}}\right) \) 的生成元 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) 使得限制在 \( {\left. S\left( E\right) \right| }_{{U}_{\alpha \beta }} \) 上, \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {\sigma }_{\beta }\right\rbrack \) ,即

\[
{\sigma }_{\beta } - {\sigma }_{\alpha } = d{\tau }_{\alpha \beta },
\]

即

\[
{\delta \sigma } = {d\tau } =  - {D}^{\prime \prime }\tau
\]

利用形变收缩 \( p : {E}^{0} \rightarrow  S\left( E\right) \) 的拉回, \( {\sigma }_{\alpha },{\tau }_{\alpha \beta } \) 可分别视为 \( {\left. {E}^{0}\right| }_{{U}_{\alpha }},{\left. {E}^{0}\right| }_{{U}_{\alpha \beta }} \) 上的形式. 于是可定义

\[
{\sigma }_{\alpha }^{0, n} \mathrel{\text{ := }} {d\rho } \land  {\sigma }_{\alpha } \in  {C}^{0}\left( {{\left. E\right| }_{{U}_{\alpha }},{\mathbf{\Omega }}_{cv}^{n}}\right) ,
\]

\[
{\sigma }_{0} = {\sigma }^{0, n} = \left\{  {\sigma }_{\alpha }^{0, n}\right\}   \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{n}}\right)
\]

(40)

![bo_d7e85t491nqc73eqefm0_385_214_1238_804_421_0.jpg](images/fu_algebraic_topology_and_differential_forms_072_bod7e85t491nqc73eqefm038521412388044210.jpg)

![bo_d7e85t491nqc73eqefm0_385_1176_1239_802_425_0.jpg](images/fu_algebraic_topology_and_differential_forms_071_bod7e85t491nqc73eqefm0385117612398024250.jpg)

则

\[
d{\sigma }_{0} = 0
\]

\[
\delta {\sigma }_{0} = {d\rho } \land  {\delta \sigma } =  - {d\rho } \land  {D}^{\prime \prime }\tau  = {D}^{\prime \prime }\left( {{d\rho } \land  \tau }\right)
\]

定义

\[
{\sigma }_{1} \mathrel{\text{ := }}  - {d\rho } \land  \tau  \in  {C}^{1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }_{cv}^{n - 1}}\right) .
\]

则

\[
0{ \uparrow  }_{{D}^{\prime \prime }}
\]

\[
{\sigma }_{0} \rightarrow  \delta {\sigma }_{0} + {D}^{\prime \prime }{\sigma }_{1} = 0
\]

由此可知 \( \left\lbrack  {\sigma }_{0}\right\rbrack   \in  {H}_{\delta }^{0, n}{H}_{d}^{*, n} \) . 由命题 12.1 的证明过程可知存在

\[
\sigma  = {\sigma }_{0} + {\sigma }_{1} + \cdots  + {\sigma }_{n}
\]

使得

\[
{D\sigma } = 0\text{ . }
\]

由 collating 公式, \( {\left\lbrack  \sigma \right\rbrack  }_{D} \) 对应于一个整体闭 \( n \) -形式 \( \Phi  \in  {\Omega }_{cv}^{n}\left( E\right) \) ,并且对 \( x \in  {U}_{\alpha } \) ,

\[
{\int }_{{E}_{x}}{\left. \Phi \right| }_{{E}_{x}} = {\int }_{{E}_{x}}{\left. \left( d\rho  \land  {\sigma }_{\alpha }\right) \right| }_{{E}_{x}} = 1.
\]

所以 \( \Phi  \in  {H}_{cv}^{n}\left( E\right) \) 是 Thom 类.

对任意的 \( U \in \) Open \( \mathcal{U},{\mathcal{H}}_{cv}^{n}\left( U\right) \) 的生成元是 \( {\left. \Phi \right| }_{E{ \mid  }_{U}} \) ,简记为 \( {\left. \Phi \right| }_{U} \) ,并且对 \( \operatorname{Open}\mathcal{U} \) 中任意开集的包含 \( V \subset  U \) ,有

\[
{\mathcal{H}}_{cv}^{n}\left( U\right) \overset{{\rho }_{V}^{U}}{ \rightarrow  }{\mathcal{H}}_{cv}^{n}\left( V\right)
\]

\[
{\left. \Phi \right| }_{U} \mapsto  {\left. \left( {\left. \Phi \right| }_{U}\right) \right| }_{V} = {\left. \Phi \right| }_{V}
\]

于是可在好覆盖 \( \mathcal{U} \) 上的两个预层 \( {\mathcal{H}}_{cv}^{n} \) 与 \( \mathbb{R} \) 之间建立同构:

\[
{\mathcal{H}}_{cv}^{n}\left( U\right)  \rightarrow  \mathbb{R}\left( U\right)  = \mathbb{R}
\]

\[
{\left. \Phi \right| }_{U}\; \mapsto  1
\]

练习 12.11. 应用 Thom 同构 12.2 计算开 Möbius 带的紧上同调.

Thom 类与欧拉类的性质

设 \( M \) 是 \( n \) 维连通流形, \( \pi  : E \rightarrow  M \) 是秩 \( k \) 定向向量丛, \( {s}_{0} : M \rightarrow  E \) 是零截面, \( {E}^{0} = E - {s}_{0}\left( M\right) \) . 若 \( \psi  \in  {\Omega }^{k - 1}\left( {E}^{0}\right) \) 是 \( {E}^{0} \) 上整体角形式,并且 \( {d\psi } \) 能自然延拓为 \( E \) 上 \( k \) -形式,则 \( E \) 的 Thom 类为

\[
\Phi  = {d\rho }\left( r\right)  \land  \psi  + \rho \left( r\right) {d\psi }
\]

其中 \( \rho \left( r\right) \) 如下图所示.

![bo_d7e85t491nqc73eqefm0_388_279_1041_802_420_0.jpg](images/fu_algebraic_topology_and_differential_forms_074_bod7e85t491nqc73eqefm038827910418024200.jpg)

![bo_d7e85t491nqc73eqefm0_388_1242_1041_801_420_0.jpg](images/fu_algebraic_topology_and_differential_forms_073_bod7e85t491nqc73eqefm0388124210418014200.jpg)

设 \( \langle \) , \( \rangle {\text{ 是 }E} \) 上一个度量, \( S\left( E\right) \) 是相应的球面丛.

![bo_d7e85t491nqc73eqefm0_389_660_196_1007_545_0.jpg](images/fu_algebraic_topology_and_differential_forms_075_bod7e85t491nqc73eqefm038966019610075450.jpg)

\( S\left( E\right) \) 上存在整体角形式 \( \psi \) 使得

\[
{d\psi } =  - {\pi }_{1}^{ * }e
\]

其中 \( e \) 为 \( S\left( E\right) \) 的欧拉类,也是 \( E \) 的欧拉类. 则 \( {p}^{ * }\psi \) 为 \( {E}^{0} \) 上整体角形式且

\[
d{p}^{ * }\psi  = {p}^{ * }{d\psi } =  - {p}^{ * }{\pi }_{1}^{ * }e =  - {\pi }_{0}^{ * }e
\]

能自然延拓为 \( E \) 上 \( k \) -形式 \( - {\pi }^{ * }e \) . 所以得到

命题 12.3. 定向向量丛 \( E \) 的 Thom 类是

\[
\Phi  = {d\rho } \land  {p}^{ * }\psi  - \rho  \cdot  {\pi }^{ * }e \in  {\Omega }_{cv}^{k}\left( E\right)
\]

的上同调类.

由命题 12.3 可得

\[
{s}_{0}^{ * }\Phi  = {s}_{0}^{ * }\left( {{d\rho } \land  {p}^{ * }\psi }\right)  - \left( {\rho  \circ  {s}_{0}}\right)  \cdot  {s}_{0}^{ * }{\pi }^{ * }e = 0 + e = e.
\]

命题 12.4. 定向向量丛的零截面把 Thom 类拉回到底流形为欧拉类.

注记 12.4.1. 显然从 Thom 类的公式 (12.3) 可知当 \( \rho \left( r\right) \) 的支集充分靠近零时， Thom 类 \( \Phi \) 的支集可任意靠近向量丛的零截面.

注记 12.4.2. 事实上, 在命题 12.4 中任意截面把 Thom 类拉回为欧拉类. 设 \( s \) 是任一截面，它诱导了上同调的映射 \( {s}^{ * } : {H}_{cv}^{ * }\left( E\right)  \rightarrow  {H}^{ * }\left( M\right) \) . 把 \( {s}^{ * } \) 分解为

![bo_d7e85t491nqc73eqefm0_390_824_981_670_562_0.jpg](images/fu_algebraic_topology_and_differential_forms_076_bod7e85t491nqc73eqefm03908249816705620.jpg)

截面 \( s \) 与零截面 \( {s}_{0} \) 作为从 \( M \) 到 \( E \) 的映射同伦. 根据 de Rham 上同调的同伦公理, \( {\bar{s}}^{ * } = {\bar{s}}_{0}^{ * } \) . 因此 \( {s}^{ * } = {s}_{0}^{ * } \) .

应用命题 12.4 容易证明欧拉类的 Whitney 积公式.

定理 12.5.(欧拉类的 Whitney 积公式)若 \( E \) ， \( F \) 是两个定向向量丛，则

\[
e\left( {E \oplus  F}\right)  = e\left( E\right)  \land  e\left( F\right) .
\]

证. 由命题 6.19, \( E \oplus  F \) 的 Thom 类是

\[
\Phi \left( {E \oplus  F}\right)  = {\operatorname{pr}}_{1}^{ * }\Phi \left( E\right)  \land  {\operatorname{pr}}_{2}^{ * }\Phi \left( F\right)
\]

其中 \( {\mathrm{{pr}}}_{1} \) , \( {\mathrm{{pr}}}_{2} \) 分别是从 \( E \oplus  F \) 到 \( E \) , \( F \) 的投射. 设 \( s \) 是 \( E \oplus  F \) 的零截面. 则 \( {\mathrm{{pr}}}_{1} \circ  s,{\mathrm{{pr}}}_{2} \circ  s \) 分别是 \( E, F \) 的零截面. 由命题 12.4 得

\[
e\left( {E \oplus  F}\right)  = {s}^{ * }\Phi \left( {E \oplus  F}\right)  = {s}^{ * }{\mathrm{{pr}}}_{1}^{ * }\Phi \left( E\right)  \land  {s}^{ * }{\mathrm{{pr}}}_{2}^{ * }\Phi \left( F\right)  = e\left( E\right)  \land  e\left( F\right) .
\]

练习 12.6. 设 \( \pi  : E \rightarrow  M \) 是定向向量丛.

(a) 证明等式 \( {\pi }^{ * }e = \Phi \) 作为 \( {H}^{ * }\left( E\right) \) 中的上同调类成立,但作为 \( {H}_{cv}^{ * }\left( E\right) \) 中的上同调类不成立.

(b) 证明在 \( {H}_{cv}^{ * }\left( E\right) \) 中 \( \Phi  \land  \Phi  = \Phi  \land  {\pi }^{ * }e \) .

补充命题. 紧定向流形 \( M \) 上秩 \( k \) 定向向量丛 \( E \) 的欧拉类 \( e\left( E\right)  = 0 \) 当且仅当以下的自然映射为零映射:

\[
{H}_{c}^{k}\left( E\right)  \rightarrow  {H}^{k}\left( E\right) \overset{ \sim  }{ \rightarrow  }{H}^{k}\left( M\right)
\]

证. 因为 \( M \) 紧, \( {H}_{cv}^{ * }\left( E\right)  = {H}_{c}^{ * }\left( E\right) \) . 另一方面,由 Thom 同构, \( {H}_{cv}^{k}\left( E\right)  \simeq \; {H}^{0}\left( M\right)  = \mathbb{R} \) . 设 \( \Phi \) 是 \( {H}_{cv}^{k}\left( E\right) \) 的一个生成元.

\[
\Phi  = {d\rho } \land  {p}^{ * }\psi  - \rho  \cdot  {\pi }^{ * }e
\]

\[
= d\left( {\left( {\rho  + 1}\right)  \cdot  {p}^{ * }\psi }\right)  - \left( {\rho  + 1}\right)  \cdot  {p}^{ * }{d\psi } - \rho {\pi }^{ * }e
\]

\[
= d\left( {\left( {\rho  + 1}\right)  \cdot  {p}^{ * }\psi }\right)  + {\pi }^{ * }e.
\]

因为 \( {\pi }^{ * } \) 是单射,所以 \( {\left\lbrack  \Phi \right\rbrack  }_{d} = 0 \in  {H}^{k}\left( E\right) \) 当且仅当 \( \left\lbrack  e\right\rbrack   = 0 \in  {H}^{k}\left( M\right) \) . 一个流形称为仿射流形若它具有仿射坐标图册,即存在坐标图册 \( \left\{  \left( {{U}_{\alpha },{\varphi }_{\alpha }}\right) \right\} \) 使得

\[
{\varphi }_{\alpha } \circ  {\varphi }_{\beta } : {\varphi }_{\beta }^{-1}\left( {U}_{\alpha \beta }\right)  \rightarrow  {\varphi }_{\alpha }\left( {U}_{\alpha \beta }\right)
\]

是仿射变换. 关于仿射流形的欧拉类有以下著名的陈省身猜想.

猜想. (陈省身) 连通紧仿射流形的欧拉类为零.

欧拉类与截面的零点集

设 \( \pi  : E \rightarrow  M \) 是 \( n \) 维流形 \( M \) 上秩 \( r \) 向量丛, \( r \leq  n \) . \( E \) 的截面 \( s \) 是横截的若像 \( S = s\left( M\right) \) 与零截面的像 \( {S}_{0} = {s}_{0}\left( M\right) \) 作为 \( E \) 的子流形是横截相交的,即

(a) \( S \cap  {S}_{0} \) 是 \( S \) 与 \( {S}_{0} \) 的闭子流形;

(b) \( {\left. TS\right| }_{S \cap  {S}_{0}} + {\left. T{S}_{0}\right| }_{S \cap  {S}_{0}} = {\left. TE\right| }_{S \cap  {S}_{0}} \) .

所以 \( \dim \left( {S \cap  {S}_{0}}\right)  = n - r \) . 记 \( s \) 的零点集 (zero locus)

\[
Z = \{ x \in  M \mid  s\left( x\right)  = 0\}  = {s}^{-1}\left( {S \cap  {S}_{0}}\right) .
\]

由于 \( s : M \rightarrow  S \) 是微分同胚,所以 \( Z \) 是 \( M \) 的 \( \left( {n - r}\right) \) 维闭子流形.

我们要把定向向量丛的欧拉类解释为 \( Z \) 的 Poincaré 对偶. 这类比于定理 11.17, 但是有以下两个方面不同:

(1)对 \( E \) 的秩没有要求;

(2)截面假定是横截的.

命题 12.7. \( Z \) 是 \( M \) 的闭子流形且它的法丛

\[
{N}_{Z/M} \simeq  {\left. E\right| }_{Z}
\]

证. 为了计算 \( Z \) 的法丛,首先注意到因为 \( E \) 是局部平凡化的, \( E \) 的切丛 \( {TE} \) 限制到它的子流形 \( {S}_{0} \) 有典则分解

\[
{\left. TE\right| }_{{S}_{0}} \simeq  {\left( {s}_{0}^{-1}\right) }^{-1}E \oplus  T{S}_{0}, \tag{41}
\]

其中 \( {s}_{0} : M \rightarrow  {S}_{0} \) ,而 \( {\left( {s}_{0}^{-1}\right) }^{-1}E \) 表示 \( M \) 上向量丛 \( E \) 由 \( {s}_{0}^{-1} \) 拉回到 \( {S}_{0} \) 上. 补充练习 1. 从 \( E \) 的局部平凡化的局部坐标系出发证明同构 (41). 结合横截性条件 (b) 可得

\[
{\left. TS\right| }_{S \cap  {S}_{0}} + {\left. T{S}_{0}\right| }_{S \cap  {S}_{0}} \simeq  {\left( {s}_{0}^{-1}\right) }^{-1}{\left. E\right| }_{S \cap  {S}_{0}} \oplus  {\left. T{S}_{0}\right| }_{S \cap  {S}_{0}}.
\]

![bo_d7e85t491nqc73eqefm0_394_464_1074_1425_644_0.jpg](images/fu_algebraic_topology_and_differential_forms_077_bod7e85t491nqc73eqefm0394464107414256440.jpg)

因此, 映射

\[
{\left. TS\right| }_{S \cap  {S}_{0}} \rightarrow  {\left( {s}_{0}^{-1}\right) }^{-1}{\left. E\right| }_{S \cap  {S}_{0}}
\]

是满射，并且由横截性其核

\[
{\left. TS\right| }_{S \cap  {S}_{0}} \cap  {\left. T{S}_{0}\right| }_{S \cap  {S}_{0}} = T\left( {S \cap  {S}_{0}}\right) .
\]

所以有向量丛的正合序列:

\[
{\left. 0 \rightarrow  T\left( S \cap  {S}_{0}\right)  \rightarrow  TS\right| }_{S \cap  {S}_{0}} \rightarrow  {\left( {s}_{0}^{-1}\right) }^{-1}{\left. E\right| }_{S \cap  {S}_{0}} \rightarrow  0. \tag{42}
\]

借助于微分同胚 \( s : M \rightarrow  S \) 与 \( {\left. s\right| }_{Z} : Z \rightarrow  S \cap  {S}_{0} \) ,它等价于

\[
{\left. 0 \rightarrow  TZ \rightarrow  TM\right| }_{Z} \rightarrow  {\left. E\right| }_{Z} \rightarrow  0 \tag{43}
\]

所以

\[
{N}_{Z/M} \simeq  {\left. E\right| }_{Z}.
\]

补充练习 2. 证明从正合序列 (42) 推出正合序列 (43). 在上述命题中,如果 \( E, M \) 是定向的,则 \( Z \) 有一个自然的定向使得

\[
{\left. TM\right| }_{Z} \simeq  {\left. E\right| }_{Z} \oplus  {TZ}
\]

是直和定向.

命题 12.8. 设 \( \pi  : E \rightarrow  M \) 是定向流形 \( M \) 上的定向向量丛. 则 \( E \) 的欧拉类 \( e\left( E\right) \) Poincaré 对偶于横截面的零点集.

证. 将 \( M \) 与零截面的像 \( {S}_{0} \) 等同. 若 \( S \) 是横截面 \( s : M \rightarrow  E \) 的像,则 \( s \) 的零点集是 \( Z = S \cap  {S}_{0} \) . \( Z \) 是 \( M \) 的闭定向子流形并且根据命题 12.7,它的法丛 \( {N}_{Z/M} \simeq  {\left. E\right| }_{Z} \) . 因为 \( S \) 微分同胚于 \( M \) , \( Z \) 在 \( S \) 中的法丛也同构于 \( {\left. E\right| }_{Z} \) . 法丛 \( {N}_{Z/M},{N}_{Z/S} \) 分别等同于 \( Z \) 在 \( M, S \) 中的管状邻域. 由注记 12.4.1,若 \( \rho \left( r\right) \) 的支集充分小,则 \( E \) 的 Thom 类 \( \Phi \) 的支集充分靠近零截面使得 \( \Phi \) 限制到 \( Z \) 在 \( S \) 中的管状邻域 \( {N}_{Z/S} \) 在垂直方向有紧支集. 在下图中 \( \Phi \) 的支集在阴影区域中. 需证明 \( {s}^{ * }\Phi \) 是 \( Z \) 在 \( M \) 中管状邻域 \( {N}_{Z/M} \) 的 Thom 类. 设 \( {E}_{z},{S}_{z},{M}_{z} \) 分别是 \( {\left. E\right| }_{Z} \simeq  {N}_{Z/S} \simeq  {N}_{Z/M} \) 在点 \( z \in  Z \) 的纤维. 因为 \( \Phi \) 在 \( {S}_{z} \) 有紧支集,所以 \( {s}^{ * }\Phi \) 在 \( {M}_{z} \) 有紧支集. 而且,

\[
{\int }_{{M}_{z}}{s}^{ * }\Phi  = {\int }_{{S}_{z}}\Phi
\]

\[
= {\int }_{{E}_{z}}\Phi
\]

因为 \( {E}_{z} \) 同伦于 \( {S}_{z} \) ,本质上(44)应用 Stokes 定理 \( = 1\; \) 因为 \( \Phi \) 是 Thom 类.

![bo_d7e85t491nqc73eqefm0_396_721_1109_869_558_0.jpg](images/fu_algebraic_topology_and_differential_forms_078_bod7e85t491nqc73eqefm039672111098695580.jpg)

![bo_d7e85t491nqc73eqefm0_397_364_655_1594_766_0.jpg](images/fu_algebraic_topology_and_differential_forms_079_bod7e85t491nqc73eqefm039736465515947660.jpg)

补充练习 3 . 按你的理解详细写下 (44) 的第二个等式的证明.

所以 \( {s}^{ * }\Phi \) 是 \( {N}_{Z/M} \) 的 Thom 类. 根据命题 12.4, \( {s}^{ * }\Phi  = e\left( E\right) \) . 因为根据 (6.24) \( {N}_{Z/M} \) 的 Thom 类是 \( Z \) 在 \( M \) 中的 Poincaré 对偶,所以欧拉类 \( e\left( E\right) \) 是 \( Z \) 在 \( M \) 中的 Poincaré 对偶.

作业:

1. 练习 12.11.

2. 练习 12.6.

3. 补充练习 1.

4. 补充练习 2.

5. 补充练习 3.

代数拓扑与微分形式
