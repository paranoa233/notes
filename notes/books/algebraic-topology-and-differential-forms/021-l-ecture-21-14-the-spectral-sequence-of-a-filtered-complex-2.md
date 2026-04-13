#### 第21讲 The Spectral Sequence of a Filtered Complex (2)

§14 The Spectral Sequence of a Filtered Complex (2)

21. 双复形的谱序列

这次课考虑双复形 \( K = \bigoplus {K}^{p, q} \) 的谱序列. 由于它是双分次的且有两个微分算子 \( d \) 与 \( \delta \) ,所以可对这种特殊情形改进定理 14.6. 接着考虑纤维丛的谱序列,将改进的定理应用到纤维丛的双复形 \( {K}^{p, q} = {C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{q}}\right) \) ,得到关于 de Rham 上同调的 Leray 定理.

- 双复形的谱序列

- 纤维丛的谱序列

双复形的谱序列

设

\[
K = { \oplus  }_{p, q \geq  0}{K}^{p, q}
\]

是双复形，微分算子

\[
\delta  : {K}^{p, q} \rightarrow  {K}^{p + 1, q},\;d : {K}^{p, q} \rightarrow  {K}^{p, q + 1}
\]

满足 \( {\delta d} = {d\delta } \) . \( K \) 上有一个自然的滤列

(14.2)

\[
{K}_{p} = {\bigoplus }_{i \geq  p}{\bigoplus }_{q \geq  0}{K}^{i, q}
\]

与自然的分级

\[
K = {\bigoplus }_{n}{K}^{n},\;{K}^{n} = {\bigoplus }_{p + q = n}{K}^{p, q}
\]

\( {K}^{n} \) 上有自然滤列

\[
{K}_{p}^{n} = {K}^{n} \cap  {K}_{p}
\]

它的长度最多为 \( n \) .

![bo_d7e85t491nqc73eqefm0_475_668_372_968_674_0.jpg](images/fu_algebraic_topology_and_differential_forms_129_bod7e85t491nqc73eqefm04756683729686740.jpg)

双复形 \( K \) 的分级 \( K = {\bigoplus }_{n}{K}^{n} \) 可认为是由双复形 \( K \) 形成的单复形,其上微分算子为

\[
D = \delta  + {\left( -1\right) }^{p}d : {K}^{n} \rightarrow  {K}^{n + 1}.
\]

它的上同调 \( H\left( K\right) \) 有诱导滤列

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3} \supset  \ldots ,
\]

其中

\[
{F}_{p} = {i}^{p}H\left( {K}_{p}\right) .
\]

对每个维数 \( n,{H}^{n}\left( K\right) \) 有滤列

\[
{H}^{n}\left( K\right)  = {F}_{0}^{n} \supset  {F}_{1}^{n} \supset  {F}_{2}^{n} \supset  {F}_{3}^{n} \supset  \cdots  \supset  {F}_{n}^{n} \supset  0
\]

其中

\[
{F}_{p}^{n} \triangleq  {F}_{p} \cap  {H}^{n}\left( K\right)  = {i}^{p}{H}^{n}\left( {K}_{p}\right)  \subset  {H}^{n}\left( K\right) .
\]

由定理 14.6 知存在收敛于 \( H\left( K\right) \) 的谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) ,即

\[
{E}_{\infty } = {GH}\left( K\right)  = { \oplus  }_{p \geq  0}{F}_{p}/{F}_{p + 1},
\]

![bo_d7e85t491nqc73eqefm0_476_826_1090_635_628_0.jpg](images/fu_algebraic_topology_and_differential_forms_130_bod7e85t491nqc73eqefm047682610906356280.jpg)

并且

\[
{E}_{\infty } = { \oplus  }_{n}{E}_{\infty }^{n}
\]

\[
{E}_{\infty }^{n} = { \oplus  }_{p = 0}^{n}{F}_{p}^{n}/{F}_{p + 1}^{n} = G{H}^{n}\left( K\right)
\]

我们要改进上述分解,使得 \( {E}_{\infty }^{n} \) ,从而 \( {E}_{\infty } \) 也是双分次的. 直和 \( A = { \oplus  }_{p \geq  0}{K}_{p} \) 也是一个双复形. 它的元 \( a \in  A \) 可表示为

\[
a = \left( {{a}_{0},{a}_{1},{a}_{2},\cdots }\right) ,
\]

其中 \( {a}_{p} \in  {K}_{p} \) ,且 \( a \) 的分量只有有限多个不为零. 记 \( {A}^{k} \) 是由 \( A \) 中所有双次数之和等于 \( k \) 的元组成的. 元 \( a \in  {A}^{0} \) 为

\[
a = \left( {{a}_{0},0,\cdots }\right) ,
\]

其中 \( {a}_{0} \in  {K}^{0,0} \) . 元 \( a \in  {A}^{1} \) 为

\[
a = \left( {{a}_{0},{a}_{1},0,\cdots }\right) ,
\]

其中 \( {a}_{0} \in  {K}^{0,1} \oplus  {K}^{1,0},{a}_{1} \in  {K}^{1,0} \) . 元 \( a \in  {A}^{2} \) 为

\[
a = \left( {{a}_{0},{a}_{1},{a}_{2},0,\cdots }\right) ,
\]

其中 \( {a}_{0} \in  {K}^{0,2} \oplus  {K}^{1,1} \oplus  {K}^{2,0},{a}_{1} \in  {K}^{1,1} \oplus  {K}^{2,0},{a}_{2} \in  {K}^{2,0} \) . 如此等等. 这样 \( A \) 形成单复形

\[
A = { \oplus  }_{k}{A}^{k},\;D = \delta  + {\left( -1\right) }^{p}d : {A}^{k} \rightarrow  {A}^{k + 1}.
\]

如若 \( a = \left( {{a}_{0},{a}_{1},0,\cdots }\right)  \in  {A}^{1} \) ,则 \( {Da} = \left( {D{a}_{0}, D{a}_{1},0,\cdots }\right)  \in  {A}^{2} \) .

包含映射

\[
i : {A}^{k} \cap  {K}_{p + 1} \rightarrow  {A}^{k} \cap  {K}_{p}
\]

诱导了包含 \( i : {A}^{k} \rightarrow  {A}^{k} \) ,从而诱导了包含 \( i : A \rightarrow  A \) .

令 \( B = {\bigoplus }_{p}{K}_{p}/{K}_{p + 1} \) . 则 \( B \) 也是双复形. 它形成单复形

\[
B = { \oplus  }_{k}{B}^{k},\;D = {\left( -1\right) }^{p}d,
\]

这是因为 \( \delta \) 被模掉了. 所以

(14.7)

\[
{E}_{1} = {H}_{D}\left( B\right)  = {H}_{d}\left( K\right) .
\]

它是双分次的: \( {E}_{1}^{p, q} = {H}_{d}^{q}\left( {K}^{p, * }\right) \) . 复形的短正合序列

(14.3)

\[
0 \rightarrow  A\overset{i}{ \rightarrow  }A\overset{j}{ \rightarrow  }B \rightarrow  0
\]

诱导了上同调的长正合序列

\[
\cdots  \rightarrow  {H}^{k}\left( A\right) \overset{{i}_{1}}{ \rightarrow  }{H}^{k}\left( A\right) \overset{{j}_{1}}{ \rightarrow  }{H}^{k}\left( B\right) \overset{{k}_{1}}{ \rightarrow  }{H}^{k + 1}\left( A\right)  \rightarrow  \ldots
\]

把它写作正合偶的形式:

![bo_d7e85t491nqc73eqefm0_480_64_849_2181_566_0.jpg](images/fu_algebraic_topology_and_differential_forms_131_bod7e85t491nqc73eqefm04806484921815660.jpg)

于是有谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) . 需研究微分 \( {d}_{r} \) . 先看微分算子

\[
{d}_{1} = {j}_{1} \circ  {k}_{1} : {E}_{1} \rightarrow  {E}_{1}.
\]

回忆连接同态 \( {k}_{1} : {H}^{k}\left( B\right)  \rightarrow  {H}^{k + 1}\left( A\right) \) 的定义. 设 \( {\left\lbrack  b\right\rbrack  }_{1} \in  {E}_{1}^{k} = {H}^{k}\left( B\right) \) . 复形的短正合序列 \( \left( {14.3}\right) \) 为

(14.8) \( \uparrow  D \)

\( 0\; \rightarrow  {A}^{k + 1} \cap  {K}_{p + 1}\overset{i}{\underset{\left( 3\right) }{ \rightarrow  }}{A}^{k + 1} \cap  {K}_{p}\overset{j}{ \rightarrow  }{B}^{k + 1} \cap  {K}_{p}/{K}_{p + 1} \rightarrow  0 \) (2) \( \uparrow \) D \( 0\; \rightarrow  \;{A}^{k} \cap  {K}_{p + 1}\;\overset{i}{ \rightarrow  }\;{A}^{k} \cap  {K}_{p}\;\underset{\left( 1\right) }{\overset{j}{ \rightarrow  }}\;{B}^{k} \cap  {K}_{p}/{K}_{p + 1}\; \rightarrow  \;0 \)

\( \uparrow  D = {\left( -1\right) }^{p}d \)

设 \( b \in  {A}^{k} \cap  {K}_{p} \) 表示 在 \( {B}^{k} \cap  {K}_{p}/{K}_{p + 1} \) 中一个闭链 \( \left\lbrack  b\right\rbrack \) . 这对应于图中第 (1) 步. 为了得到 \( {k}_{1}\left( {\left\lbrack  b\right\rbrack  }_{1}\right) \) ,我们

(2)计算 \( {Db} \) 且

(3)取逆 \( {i}^{-1}\left( {Db}\right) \) .

因为 \( {\left\lbrack  b\right\rbrack  }_{1} \in  {E}_{1}^{k} = {H}_{D}^{k}\left( B\right)  = {H}_{d}^{k}\left( K\right) \) ,所以 \( {db} = 0 \) ,

\[
{Db} = {\delta b} \in  {A}^{k + 1} \cap  {K}_{\mathrm{p} + 1}.
\]

这就是说第(2)步与第(3)步其实是 “一步到位” 的. 于是

\[
{k}_{1}{\left\lbrack  b\right\rbrack  }_{1} = {\left\lbrack  \delta b\right\rbrack  }_{D} \in  {H}_{D}^{k + 1}\left( A\right) .
\]

由 \( {j}_{1} \) 的定义知

\[
{d}_{1}{\left\lbrack  b\right\rbrack  }_{1} = {j}_{1}{\left\lbrack  \delta b\right\rbrack  }_{D} = {\left\lbrack  \delta b\right\rbrack  }_{1}.
\]

为此定义

\[
\delta  : {H}_{D}^{k}\left( B\right)  \rightarrow  {H}_{D}^{k + 1}\left( B\right)
\]

为

\[
\delta {\left\lbrack  b\right\rbrack  }_{d} = {\left\lbrack  \delta b\right\rbrack  }_{d}.
\]

它是定义好的. 因此

(14.9)

\[
{E}_{2} = {H}_{\delta }{H}_{d}\left( K\right)
\]

它的元为记作 \( {\left\lbrack  {\left\lbrack  b\right\rbrack  }_{1}\right\rbrack  }_{2} \) 或 \( {\left\lbrack  b\right\rbrack  }_{2} \) . \( {E}_{2} \) 是双分次的: \( {E}_{2}^{p, q} = {H}_{\delta }^{p, q}{H}_{d} \) .

接着在 \( {E}_{2} \) 上计算 \( {d}_{2} = {j}_{2} \circ  {k}_{2} \) .

用 \( b \in  {A}^{k} \cap  {K}_{p} \) 表示一个闭链 \( {\left\lbrack  b\right\rbrack  }_{2} \) . 所以 \( {db} = 0,\delta {\left\lbrack  b\right\rbrack  }_{d} = 0 \) ,即

\( {db} = 0,\;{\delta b} =  - {D}^{\prime \prime }c \) 对某个 \( c \in  {A}^{k} \cap  {K}_{p + 1} \) .

![bo_d7e85t491nqc73eqefm0_483_787_520_732_665_0.jpg](images/fu_algebraic_topology_and_differential_forms_132_bod7e85t491nqc73eqefm04837875207326650.jpg)

从导出偶 (14.1) 的定义知

\[
{d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {j}_{2}{k}_{2}{\left\lbrack  {\left\lbrack  b\right\rbrack  }_{1}\right\rbrack  }_{2} = {j}_{2}{k}_{1}{\left\lbrack  b\right\rbrack  }_{1}\;\text{ 因为在 (14.1) 中 }{k}^{\prime }\left\lbrack  b\right\rbrack   = {kb}\text{ . }
\]

为了计算 \( {j}_{2}{k}_{1}{\left\lbrack  b\right\rbrack  }_{1} \) ,需要找一个 \( a \) 使得 \( {k}_{1}{\left\lbrack  b\right\rbrack  }_{1} = i{\left\lbrack  a\right\rbrack  }_{D} \) . 若这样,则

\[
{d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {j}_{2}\left( {i{\left\lbrack  a\right\rbrack  }_{D}}\right)  = {\left\lbrack  {j}_{1}{\left\lbrack  a\right\rbrack  }_{D}\right\rbrack  }_{2}\;\text{ 因为在 }\left( {14.1}\right) \text{ 中 }{j}^{\prime }{ia} = \left\lbrack  {ja}\right\rbrack  .
\]

因为 \( {k}_{1}{\left\lbrack  b\right\rbrack  }_{1} \in  {H}^{k + 1}\left( A\right) \) ,它用 \( {A}^{k + 1} \cap  {K}_{p + 1} \) 的元表示,所以 \( a \in  {A}^{k + 1} \cap  {K}_{p + 2} \) . 为此在第 (1) 步中用 \( b + c \in  {A}^{k} \cap  {K}_{p} \) 而不是用 \( b \) 表示闭链 \( {\left\lbrack  b\right\rbrack  }_{2} \) ，这是可以的因为 \( b \) 与 \( b + c \) 在投射 \( {K}_{p} \rightarrow  {K}_{p}/{K}_{p + 1} \) 下有相同的像. 重走第 (2) 与第 (3) 步,

\[
D\left( {b + c}\right)  = {\delta c} \in  {A}^{k + 1} \cap  {K}_{p + 2}.
\]

显然 \( D\left( {\delta c}\right)  = 0 \) . 所以 \( {\left\lbrack  \delta c\right\rbrack  }_{D} \in  {A}_{1} \) 且

\[
{k}_{1}{\left\lbrack  b\right\rbrack  }_{1} = i{\left\lbrack  \delta c\right\rbrack  }_{D}.
\]

因此

(14.10)

\[
{d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  {j}_{1}{\left\lbrack  \delta c\right\rbrack  }_{D}\right\rbrack  }_{2} = {\left\lbrack  {\left\lbrack  \delta c\right\rbrack  }_{1}\right\rbrack  }_{2} = {\left\lbrack  \delta c\right\rbrack  }_{2}.
\]

上述 \( {d}_{2} \) 的定义与 \( c \) 的选取无关. 事实上,若 \( {\delta b} =  - {D}^{\prime \prime }\bar{c} \) ,则 \( {D}^{\prime \prime }\left( {c - \bar{c}}\right)  = 0 \) . 所以

\[
{\left\lbrack  \delta \left( c - \bar{c}\right) \right\rbrack  }_{1} = \delta {\left\lbrack  c - \bar{c}\right\rbrack  }_{1}.
\]

于是

\[
{\left\lbrack  \delta c\right\rbrack  }_{2} - {\left\lbrack  \delta \overline{c}\right\rbrack  }_{2} = {\left\lbrack  {\left\lbrack  \delta c\right\rbrack  }_{1} - {\left\lbrack  \delta \overline{c}\right\rbrack  }_{1}\right\rbrack  }_{2} = {\left\lbrack  {\left\lbrack  \delta \left( c - \overline{c}\right) \right\rbrack  }_{1}\right\rbrack  }_{2} = {\left\lbrack  \delta {\left\lbrack  c - \overline{c}\right\rbrack  }_{1}\right\rbrack  }_{2} = 0.
\]

练习 14.11. 证明若 \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = 0 \) ,则存在 \( {c}_{1},{c}_{2} \) 使得 \( b \) 能延拓为如下的 zig-zag:

\[
{D}^{\prime \prime }b = 0
\]

\[
{\delta b} + {D}^{\prime \prime }{c}_{1} = 0
\]

\[
\delta {c}_{1} + {D}^{\prime \prime }{c}_{2} = 0.
\]

![bo_d7e85t491nqc73eqefm0_485_1086_419_793_731_0.jpg](images/fu_algebraic_topology_and_differential_forms_133_bod7e85t491nqc73eqefm048510864197937310.jpg)

若 \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = 0 \) ,定义 \( {\left\lbrack  b\right\rbrack  }_{3} = {\left\lbrack  {\left\lbrack  {\left\lbrack  b\right\rbrack  }_{1}\right\rbrack  }_{2}\right\rbrack  }_{3} \in  {E}_{3} \) . 归纳地,若 \( {\left\lbrack  b\right\rbrack  }_{r - 1} \in  {E}_{r - 1} \) 且 \( {d}_{r - 1}{\left\lbrack  b\right\rbrack  }_{r - 1} = 0 \) ,则 \( {\left\lbrack  b\right\rbrack  }_{r} \in  {E}_{r} \) 有定义. 此时我们说元 \( b \in  K \) 活到 \( {E}_{r} \) ,即 \( {\left\lbrack  b\right\rbrack  }_{i} \) 为 \( {E}_{i} \) 的上闭链, \( 1 \leq  i \leq  r - 1 \) . 这样 \( b \) 活到 \( {E}_{2} \) 若它能延拓为长度 2 的 zig-zag:

\[
{db} = 0
\]

\[
{\delta b} =  - {D}^{\prime \prime }{c}_{1}
\]

![bo_d7e85t491nqc73eqefm0_486_1311_239_289_447_0.jpg](images/fu_algebraic_topology_and_differential_forms_135_bod7e85t491nqc73eqefm048613112392894470.jpg)

且 \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  \delta {c}_{1}\right\rbrack  }_{2} \) . 一个 zig-zag 的长度是指它含有的项数.

\( b \) 活到 \( {E}_{3} \) 若它能延拓为长度 3 的 zig-zag:

\[
{db} = 0
\]

\[
{\delta b} =  - {D}^{\prime \prime }{c}_{1}
\]

\[
\delta {c}_{1} =  - {D}^{\prime \prime }{c}_{2}
\]

![bo_d7e85t491nqc73eqefm0_486_1194_995_555_651_0.jpg](images/fu_algebraic_topology_and_differential_forms_134_bod7e85t491nqc73eqefm048611949955556510.jpg)

计算 \( {d}_{3}{\left\lbrack  b\right\rbrack  }_{3} \) . 若 \( {k}_{2}{\left\lbrack  b\right\rbrack  }_{2} = i\left( {i{\left\lbrack  a\right\rbrack  }_{D}}\right)  \in  {i}^{2}{A}_{1} \) ,则

\[
{d}_{3}{\left\lbrack  b\right\rbrack  }_{3} = {j}_{3}{k}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  {j}_{2}{\left\lbrack  i{\left\lbrack  a\right\rbrack  }_{D}\right\rbrack  }_{2}\right\rbrack  }_{3} = {\left\lbrack  {\left\lbrack  {j}_{1}{\left\lbrack  a\right\rbrack  }_{D}\right\rbrack  }_{2}\right\rbrack  }_{3}.
\]

在第 (1) 步中用 \( b + {c}_{1} + {c}_{2} \in  {A}^{k} \cap  {K}_{p} \) 表示 \( {B}^{k} \cap  {K}_{p}/{K}_{p + 1} \) 中的闭链 \( \left\lbrack  b\right\rbrack \) ,则第 (2)步与第(3)步是

\[
D\left( {b + {c}_{1} + {c}_{2}}\right)  = \delta {c}_{2} \in  {A}^{k + 1} \cap  {K}_{p + 3}
\]

\[
{\left\lbrack  \delta {c}_{2}\right\rbrack  }_{D} \in  {i}^{2}{A}_{1}
\]

所以可取 \( {\left\lbrack  a\right\rbrack  }_{D} = {\left\lbrack  \delta c\right\rbrack  }_{D} \) ,

\[
{d}_{3}{\left\lbrack  b\right\rbrack  }_{3} = {\left\lbrack  \delta {c}_{2}\right\rbrack  }_{3}.
\]

一般地, 平行于上述讨论, \( b \in  {K}^{p, q} \) 活到 \( {E}_{r} \) 若它能延拓为长度 \( r \) 的 zig-zag:

![bo_d7e85t491nqc73eqefm0_488_578_244_1175_1130_0.jpg](images/fu_algebraic_topology_and_differential_forms_136_bod7e85t491nqc73eqefm0488578244117511300.jpg)

且 \( {E}_{r} \) 上微分 \( {d}_{r} \) 由 \( \delta \) 作用在 zig-zag 的尾巴得到:

(14.12)

\[
{d}_{r}{\left\lbrack  b\right\rbrack  }_{r} = {\left\lbrack  \delta {c}_{r - 1}\right\rbrack  }_{r}.
\]

所以双复形 \( K = \bigoplus {K}^{p, q} \) 的双次数 \( \left( {p, q}\right) \) 在谱序列中是保持的:

\[
{E}_{r} = { \oplus  }_{p, q \geq  0}{E}_{r}^{p, q}
\]

并且 \( {d}_{r} \) 把双次数 \( \left( {p, q}\right) \) 变为 \( \left( {p + r, q - r + 1}\right) \) ,

\[
{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1}.
\]

上同调 \( H\left( K\right)  =  \oplus  {H}^{n}\left( K\right) \) 上滤列

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3}\ldots
\]

诱导了每个分量 \( {H}^{n}\left( K\right) \) 上滤列

\[
{H}^{n}\left( K\right)  = \left( {{F}_{0} \cap  {H}^{n}}\right)  \supset  \left( {{F}_{1} \cap  {H}^{n}}\right)  \supset  \left( {{F}_{2} \cap  {H}^{n}}\right)  \supset  \cdots  \supset  \left( {{F}_{n} \cap  {H}^{n}}\right)  \supset  0.
\]

相继的商是 \( {E}_{\infty }^{0, n},{E}_{\infty }^{1, n - 1},\ldots ,{E}_{\infty }^{n,0} \) :

\[
\text{ (14.13) }{H}^{n}\left( K\right)  = \left( {{F}_{0} \cap  {H}^{n}}\right)  \supset  \left( {{F}_{1} \cap  {H}^{n}}\right)  \supset  \left( {{F}_{2} \cap  {H}^{n}}\right)  \supset  \cdots  \supset  \left( {{F}_{n} \cap  {H}^{n}}\right)  \supset  0
\]

\[
\xrightarrow[{E}_{\infty }^{0, n}]{}\xrightarrow[{E}_{\infty }^{1, n - 1}]{}\xrightarrow[{E}_{\infty }^{1, n - 1}]{}\cdots \xrightarrow[{E}_{\infty }^{n,0}]{}
\]

综上所述，我们已证明了以下的定理 14.6 的加强版.

![bo_d7e85t491nqc73eqefm0_490_503_441_1552_870_0.jpg](images/fu_algebraic_topology_and_differential_forms_137_bod7e85t491nqc73eqefm049050344115528700.jpg)

定理 14.14. 给定双复形 \( K = {\bigoplus }_{p, q \geq  0}{K}^{p, q} \) ,存在收敛于全上同调 \( {H}_{D}\left( K\right) \) 的谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) 使得每个 \( {E}_{r} \) 是双分次的,微分 \( {d}_{r} \) 为

\[
{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1},
\]

并且

\[
{E}_{1}^{p, q} = {H}_{d}^{p, q}\left( K\right)
\]

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p, q}{H}_{d}\left( K\right)
\]

此外, 全上同调的相伴分级复形为

\[
G{H}_{D}^{n}\left( K\right)  = {\bigoplus }_{p + q = n}{E}_{\infty }^{p, q}\left( K\right)
\]

注记 14.17. 因为维数是向量空间的唯一不变量,所以一个滤列向量空间 \( V \) 的相伴分级向量空间 \( {GV} \) 同构于 \( V \) . 现若双复形 \( K \) 是向量空间,则 \( {H}_{D}^{n}\left( K\right) , G{H}_{D}^{n}\left( K\right) \) , \( {E}_{\infty }^{p, q} \) 是向量空间. 所以

\[
{H}_{D}^{n}\left( K\right)  \simeq  G{H}_{D}^{n}\left( K\right)  \simeq  {\bigoplus }_{p + q = n}{E}_{\infty }^{p, q}
\]

但若 \( K \) 是群,则上述等式不一定成立,因为有挠元. 以后我们会讨论这点.

注记 14.15. 当然可用 \( K \) 上以下滤列代替滤列 (14.2):

\[
{K}_{q} = {\bigoplus }_{p \geq  0}{\bigoplus }_{j \geq  q}{K}^{p, j}
\]

它给出收敛于全上同调 \( {H}_{D}\left( K\right) \) 的第二谱序列 \( \left\{  {{E}_{r}^{\prime },{d}_{r}^{\prime }}\right\} \) ,但是具有

\[
{E}_{1}^{\prime } = {H}_{\delta }\left( K\right)
\]

\[
{E}_{2}^{\prime } = {H}_{d}{H}_{\delta }\left( K\right)
\]

与

\[
{d}_{r}^{\prime } : {E}_{r}^{\prime p, q} \rightarrow  {E}_{r}^{\prime p - r + 1, q + r}.
\]

定义. 谱序列称为在 \( {E}_{r} \) 页退化若 \( {d}_{r} = {d}_{r + 1} = \cdots  = 0 \) . 对这样的谱序列, \( {E}_{r} = {E}_{r + 1} = \cdots  = {E}_{\infty } \)

例 14.16. (MV 原理, de Rham 与 Čech 之间的同构) 设 \( M \) 是流形, \( \mathcal{U} \) 是它的好覆盖. 考虑双复形 \( K =  \oplus  {K}^{p, q} \) ,

\[
{K}^{p, q} = {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) .
\]

因为 \( K \) 的行是 MV 序列,所以第二谱序列的 \( {E}_{1} \) 页是

\[
{E}_{1}^{\prime } = {H}_{\delta } = \left| \begin{matrix}  & & & & & \\   & \left| \Delta \right| \left( M\right) & & & & \\   & & 0 & & & \\   & {\Omega }^{2}\left( M\right) & & 0 & & \\   & & 0 & & & \\   & {\Omega }^{1}\left( M\right) & & 0 & & \\   & {\Omega }^{0}\left( M\right) & & 0 & & \\   & & & & & \\   & & & & &  \end{matrix}\right| \;
\]

<table><tr><td></td><td>\( {H}_{dR}^{3}\left( M\right) \)</td><td>0</td><td></td><td></td></tr><tr><td>\( {E}_{2}^{\prime } = {H}_{d}{H}_{\delta } = \)</td><td>\( {H}_{dR}^{2}\left( M\right) \)</td><td>0</td><td></td><td></td></tr><tr><td></td><td>\( {H}_{dR}^{1}\left( M\right) \)</td><td>0</td><td></td><td></td></tr><tr><td></td><td>\( {H}_{dR}^{0}\left( M\right) \)</td><td>0</td><td></td><td></td></tr></table>

双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 的第二谱序列在 \( {E}_{2} \) 页退化又一次证明了 MV 原理:

(14.16.1)

\[
{H}_{dR}^{k}\left( M\right)  = { \oplus  }_{p + q = k}{H}_{D}^{p, q}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

现考虑 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 的第一谱序列. 它的 \( {E}_{1} \) 页是

\[
{E}_{1}^{p, q} = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  = \left\{  \begin{array}{ll} 0 & \text{ 若 }q > 0 \\  {C}^{p}\left( {\mathcal{U},\mathbb{R}}\right) & \text{ 若 }q = 0. \end{array}\right.
\]

\[
{E}_{1} = {H}_{d} = \left| \begin{matrix} 0 & 0 \\  0 & 0 \\  {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right) & {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) {C}^{2}\left( {\mathcal{U},\mathbb{R}}\right)  \end{matrix}\right|
\]

所以 \( {E}_{2} \) 页是

<table><tr><td>\( {E}_{2} = {H}_{\delta }{H}_{d} = \)</td><td>\( {H}^{0}\left( {\mathcal{U},\mathbb{R}}\right) \)</td><td>\( {H}^{1}\left( {\mathcal{U},\mathbb{R}}\right) \)</td><td>\( {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \)</td></tr></table>

这个谱序列退化给出了

\[
{H}^{k}\left( {\mathcal{U},\mathbb{R}}\right)  = { \oplus  }_{p + q = k}{E}_{2}^{p, q} = { \oplus  }_{p + q = k}{E}_{\infty }^{p, q} = {H}_{D}^{k}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

结合(14.16.1)得到

\[
{H}_{dR}^{k}\left( M\right)  = {H}^{k}\left( {\mathcal{U},\mathbb{R}}\right) .
\]

以上是 de Rham 与 Čech 之间同构 (定理 8.9) 的谱序列证明.

纤维丛的谱序列设 \( \pi  : E \rightarrow  M \) 是流形 \( M \) 上以 \( F \) 为纤维的纤维丛. 应用定理 14.14 给出了从 \( M \) 与 \( F \) 的上同调计算 \( E \) 的上同调的一般方法.

事实上,给定 \( M \) 的好覆盖 \( \mathcal{U} \) , \( {\pi }^{-1}\mathcal{U} \) 是 \( E \) 的覆盖,由此形成双复形

\[
{K}^{p, q} = {C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{q}\left( {{\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) }\right) ,
\]

它的 \( {E}_{1} \) 页是

\[
{E}_{1}^{p, q} = {H}_{d}^{p, q} = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}^{q}\left( {{\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) }\right)  = {C}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right) ,
\]

其中 \( {\mathcal{H}}^{q} \) 是 \( M \) 上预层 \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) . 为了强调起见有时把预层 \( {\mathcal{H}}^{q} \) 记作 \( {\mathcal{H}}^{q}\left( F\right) \) . 因为 \( \mathcal{U} \) 是好覆盖, \( {\mathcal{H}}^{q} \) 是 \( \mathcal{U} \) 上群为 \( {H}^{q}\left( F\right) \) 的局部常值预层. 因为在 \( {E}_{1} \) 上 \( {d}_{1} = \delta \) ,所以 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right) .
\]

根据定理 14.14, \( K \) 的谱序列收敛于 \( {H}_{D}^{ * }\left( K\right) \) ; 再根据广义 MV 原理(命题 8.8)， \( {H}_{D}^{ * }\left( K\right) \) 等于 \( {H}^{ * }\left( E\right) \) ,因为 \( {\pi }^{-1}\mathcal{U} \) 是 \( E \) 的覆盖.

当 \( M \) 单连通且 \( {H}^{q}\left( F\right) \) 有限维时，由定理 13.2 与 13.4 知 \( \mathcal{U} \) 上局部常值预层 \( {\mathcal{H}}^{q} \) 是常值预层 \( \mathbb{R}\bigoplus \cdots \bigoplus \mathbb{R} \) ,由 \( {h}^{q}\left( F\right) \) 个 \( \mathbb{R} \) 组成,其中 \( {h}^{q}\left( F\right)  = \dim {H}^{q}\left( F\right) \) . \( {E}_{2}^{p, q} \) 页作为向量空间同构于张量积 \( {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) \) ,因为

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},\mathbb{R} \oplus  \cdots  \oplus  \mathbb{R}}\right)  = {H}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  \otimes  {H}^{q}\left( F\right)  = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) ,
\]

最后一个等式应用了定理 8.9. 我们已经证明了以下定理.

定理 14.18.(对 de Rham 上同调的 Leray 定理)给定流形 \( M \) 上以 \( F \) 为纤维的纤维丛 \( \pi  : E \rightarrow  M \) 与 \( M \) 的好覆盖 \( \mathcal{U} \) ,存在一个收敛于全上同调 \( {H}^{ * }\left( E\right) \) 的谱序列 \( \left\{  {E}_{r}\right\} \) ，它的 \( {E}_{2} \) 页为

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}}\right)
\]

其中 \( {\mathcal{H}}^{q} \) 是 \( \mathcal{U} \) 上局部常值预层 \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) . 若 \( M \) 单连通且 \( {H}^{q}\left( F\right) \) 有限维, 则

\[
{E}_{2}^{p, q} = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) .
\]

作业:

1. 练习 14.11.

代数拓扑与微分形式
