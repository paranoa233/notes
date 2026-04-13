#### 第03讲 The Mayer-Vietoris Sequence

§2. The Mayer-Vietoris Sequence

3. MV 序列

这节课介绍计算 de Rham 上同调的基本工具, Mayer-Vietoris 序列. 先讲 de Rham 上同调的 MV 序列,再讲紧上同调的 MV 序列,并都以 \( {S}^{1} \) 作为例子. 作为补充,最后给出另一种看待 \( {H}^{1}\left( {S}^{1}\right)  \simeq  \mathbb{R} \) 的方法,这种方法可被推广用来计算齐性空间的上同调.

- MV 序列

- 对紧支集的 MV 序列

- 再论 \( {H}^{1}\left( {S}^{1}\right)  \simeq  \mathbb{R} \)

MV 序列 MV 序列能用来计算两个开集之并的上同调.

设 \( U \) , \( V \) 是 \( M \) 的开子集, \( M = U \cup  V \) . 则 \( U \cap  V \) 也是开子集,并有包含映射

\[
{\partial }_{0} : U \cap  V \rightarrow  V,\;{\partial }_{1} : U \cap  V \rightarrow  U.
\]

对 \( U, V \) 作不相交的并 \( U \coprod  V \) ,并定义一个由包含映射 \( U \rightarrow  M, V \rightarrow  M \) 诱导的映射: \( U \coprod  V \rightarrow  M \) . 这样得到映射的序列:

\[
M \leftarrow  U \coprod  V\overset{{\partial }_{0}}{ \Leftarrow  }U \cap  V
\]

应用反变函子 \( {\Omega }^{ * } \) 到这个映射的序列,由于 \( {\Omega }^{ * }\left( {U \coprod  V}\right)  = {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right) \) ,我们得到一个关于形式限制的序列:

\[
{\Omega }^{ * }\left( M\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right) \overset{{\partial }_{0}^{ * }}{\underset{{\partial }_{1}^{ * }}{ \rightrightarrows  }}{\Omega }^{ * }\left( {U \cap  V}\right)
\]

Mayer-Vietoris 序列为(2.2)

\[
\left( {2.2}\right) \;0 \rightarrow  {\Omega }^{ * }\left( M\right) \overset{r}{ \rightarrow  }{\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right) \overset{\delta }{ \rightarrow  }{\Omega }^{ * }\left( {U \cap  V}\right) \; \rightarrow  0
\]

\[
\omega \; \mapsto  \;\left( {{\left. \omega \right| }_{U},{\left. \omega \right| }_{V}}\right)
\]

命题 2.3. MV 序列是复形的短正合序列. 证. 只证序列在 \( {\Omega }^{ * }\left( {U \cap  V}\right) \) 处正合,即证 \( \delta \) 是满射. 设 \( \omega  \in  {\Omega }^{q}\left( {U \cap  V}\right) \) . 设 \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) 是从属于 \( \{ U, V\} \) 的单位分解,即

\[
\text{ Supp }{\rho }_{U} \subset  U,\;\operatorname{Supp}{\rho }_{V} \subset  V,\;{\rho }_{U} + {\rho }_{V} = 1\text{ . }
\]

利用 \( \omega \) 与 \( {\rho }_{V} \) 在 \( U \) 上定义一个光滑 \( q \) -形式

\[
{\rho }_{V}\omega  = \left\{  \begin{array}{ll} {\left. {\rho }_{V}\right| }_{U \cap  V} \cdot  \omega & \text{ on }U \cap  V \\  0 & \text{ on }U \smallsetminus  U \cap  V, \end{array}\right.
\]

见下图. 用同样方法定义 \( {\rho }_{U}\omega  \in  {\Omega }^{q}\left( V\right) \) . 令 \( \xi  = \left( {-{\rho }_{V}\omega ,{\rho }_{U}\omega }\right) \) . 则

\[
{\delta \xi } = \left( {{\rho }_{U}\omega }\right) {\left| {}_{U \cap  V} - \left( -{\rho }_{V}\omega \right) \right| }_{U \cap  V} = \left( {{\rho }_{U} + {\rho }_{V}}\right) {|}_{U \cap  V} \cdot  \omega  = \omega .
\]

![bo_d7e85t491nqc73eqefm0_49_689_1039_939_634_0.jpg](images/fu_algebraic_topology_and_differential_forms_138_bod7e85t491nqc73eqefm04968910399396340.jpg)

MV 序列诱导了上同调群的长正合序列, 也称为 MV 序列:(2.4)

\[
\cdots  \rightarrow  {H}^{q}\left( M\right) \overset{r}{ \rightarrow  }{H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right) \overset{\delta }{ \rightarrow  }{H}^{q}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{q + 1}\left( M\right)  \rightarrow  \cdots
\]

\[
\left\lbrack  \omega \right\rbrack   \mapsto  \left( {\left\lbrack  {\left. \omega \right| }_{U}\right\rbrack  ,\left\lbrack  {\left. \omega \right| }_{V}\right\rbrack  }\right)
\]

\[
\left( {\left\lbrack  \omega \right\rbrack  ,\left\lbrack  \tau \right\rbrack  }\right) \; \mapsto  \left\lbrack  {{\left. \tau \right| }_{U \cap  V} - {\left. \omega \right| }_{U \cap  V}}\right\rbrack
\]

\[
\left\lbrack  \omega \right\rbrack  \; \mapsto  \;?
\]

连接同态 \( {d}^{ * } \) 的定义. 给定 \( \omega  \in  {\Omega }^{q}\left( {U \cap  V}\right) ,{d\omega } = 0 \) . 则

\[
\eta \underset{\left( 3\right) }{ \rightarrow  }{d\xi } = \left( {d\left( {-{\rho }_{V}\omega }\right) , d\left( {{\rho }_{U}\omega }\right) }\right) \overset{\delta }{ \rightarrow  }0
\]

因为 \( {\delta d\xi } = {d\delta \xi } = 0 \) ,所以 \( d\left( {-{\rho }_{V}\omega }\right) , d\left( {{\rho }_{U}\omega }\right) \) 限制在 \( U \cap  V \) 上相等. 这就是说, \( d\left( {-{\rho }_{V}\omega }\right) , d\left( {{\rho }_{U}\omega }\right) \) 可拼成 \( M \) 上一个 \( \left( {q + 1}\right) \) -形式 \( \eta \) :

\[
\eta  = \left\{  \begin{array}{ll} d\left( {-{\rho }_{V}\omega }\right) & \text{ on }U \\  d\left( {{\rho }_{U}\omega }\right) & \text{ on }V. \end{array}\right.
\]

显然, \( {d\eta } = 0 \) . 定义

\[
{d}^{ * }\left\lbrack  \omega \right\rbrack   = \left\lbrack  \eta \right\rbrack   \in  {H}^{q + 1}\left( M\right) .
\]

由定义知 \( \eta \) 的支集

\[
\operatorname{Supp}\eta  = \overline{\left\{  x \in  M \mid  \eta \left( x\right)  \neq  0\right\}  } \subset  U \cap  V.
\]

例 2.6.( \( {S}^{1} \) 的上同调)如下图 \( {S}^{1} \) 的开覆盖由开集 \( U \) ， \( V \) 组成. 考虑长正合序列:

\[
0 \rightarrow  {H}^{0}\left( {S}^{1}\right)  \rightarrow  {H}^{0}\left( U\right)  \oplus  {H}^{0}\left( V\right) \overset{\delta }{ \rightarrow  }{H}^{0}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{1}\left( {S}^{1}\right)
\]

\[
\rightarrow  {H}^{1}\left( U\right)  \oplus  {H}^{1}\left( V\right)  \rightarrow  {H}^{1}\left( {U \cap  V}\right)  \rightarrow  {H}^{2}\left( {S}^{1}\right)  \rightarrow  \cdots
\]

![bo_d7e85t491nqc73eqefm0_52_723_462_905_556_0.jpg](images/fu_algebraic_topology_and_differential_forms_155_bod7e85t491nqc73eqefm0527234629055560.jpg)

由 Poincaré 引理, 上述长正合序列变为

\[
0 \rightarrow  {H}^{0}\left( {S}^{1}\right)  \rightarrow  \mathbb{R} \oplus  \mathbb{R}\overset{\delta }{ \rightarrow  }\mathbb{R} \oplus  \mathbb{R}\overset{{d}^{ * }}{ \rightarrow  }{H}^{1}\left( {S}^{1}\right)  \rightarrow  0 \rightarrow  0 \rightarrow  \ldots
\]

因为

\[
\delta \left( {\omega ,\tau }\right)  = {\left. \tau \right| }_{U \cap  V} - {\left. \omega \right| }_{U \cap  V} = \left( {\tau  - \omega ,\tau  - \omega }\right) ,
\]

所以 \( \ker \delta  = \mathbb{R} \) , im \( \delta  = \mathbb{R} \) . 于是

\[
{H}^{0}\left( {S}^{1}\right)  = \ker \delta  = \mathbb{R},\;{H}^{1}\left( {S}^{1}\right)  = \mathbb{R} \oplus  \mathbb{R}/\ker {d}^{ * } = \mathbb{R}.
\]

考虑 \( {H}^{1}\left( {S}^{1}\right) \) 的生成元. 令 \( \alpha  \in  {\Omega }^{0}\left( {U \cap  V}\right) \) 如下图

![bo_d7e85t491nqc73eqefm0_53_822_297_688_679_0.jpg](images/fu_algebraic_topology_and_differential_forms_156_bod7e85t491nqc73eqefm0538222976886790.jpg)

则 \( \left\lbrack  \alpha \right\rbrack   \notin  \operatorname{im}\delta  = \ker {d}^{ * } \) . 所以 \( {d}^{ * }\left\lbrack  \alpha \right\rbrack   \neq  0 \in  {H}^{1}\left( {S}^{1}\right) \) . 其实,由构造可知 \( {d}^{ * }\left\lbrack  \alpha \right\rbrack   = \left\lbrack  \eta \right\rbrack \) ,

\[
\eta  = \left\{  \begin{array}{ll}  - d\left( {{\rho }_{V}\alpha }\right) & \text{ on }U \\  d\left( {{\rho }_{U}\alpha }\right) & \text{ on }V \end{array}\right.
\]

其中 \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) 是从属于 \( \{ U, V\} \) 的一个单位分解.

![bo_d7e85t491nqc73eqefm0_54_626_180_1093_1011_0.jpg](images/fu_algebraic_topology_and_differential_forms_159_bod7e85t491nqc73eqefm054626180109310110.jpg)

\( \eta \) 是一个 bump1-形式,它的支集包含在 \( U \cap  V \) 中. 所以如果 \( U \cap  V \) 充分小, \( \eta \) 的支集可充分小.

利用牛顿-莱布尼兹定理或 Stokes 定理计算

\[
{\int }_{{S}^{1}}\eta  =  - {\int }_{U}d\left( {{\rho }_{V}\alpha }\right)  =  - {\left. {\rho }_{V}\alpha \right| }_{{q}^{ - }}^{{p}^{ + }} = 1.
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

设 \( f : N \rightarrow  M \) 是 \( {C}^{\infty } \) 映射. 映射 \( {f}^{ * } : {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  {\Omega }_{c}^{ * }\left( N\right) \) 一般不成立. 此时,有以下两种方案可供选择.

(a) 若 \( f : N \rightarrow  M \) 是逆紧(proper)映射, 即紧集在 \( f \) 下的逆像是紧集, 则映射 \( {f}^{ * } : {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  {\Omega }_{c}^{ * }\left( N\right) \) 成立. 这是因为若 \( \omega  \in  {\Omega }_{c}^{ * }\left( M\right) \) ,则 \( \operatorname{Supp}{f}^{ * }\omega  \subset \; {f}^{-1}\left( {\operatorname{Supp}\omega }\right) \) 是紧集.

如果只考虑流形间的逆紧映射, \( {\Omega }_{c}^{ * } \) 是反变函子.

(b) 设 \( M \) 是流形, \( j : U \rightarrow  M \) 是开子集的包含映射. 定义

\[
{j}_{ * } : {\Omega }_{c}^{ * }\left( U\right)  \rightarrow  {\Omega }_{c}^{ * }\left( M\right)
\]

\[
{j}_{ * }\omega  = \left\{  \begin{array}{ll} \omega & \text{ on }U \\  0 & \text{ on }M - U \end{array}\right.
\]

即 \( {j}_{ * }\omega \) 为零延拓 (extension by zero).

如果只考虑开集间的包含映射, \( {\Omega }_{c}^{ * } \) 是共变函子.

以后要用函子 \( {\Omega }_{c}^{ * } \) 的共变性来证非紧流形的 Poincaré 对偶. 所以从现在起假定 \( {\Omega }_{c}^{ * } \) 是 (b) 中的共变函子. 对这个函子也有 MV 序列.

设 \( U, V \) 是 \( M \) 的两个开集且 \( U \cup  V = M \) . 由包含映射的序列

\[
U \cap  V \rightrightarrows  U \coprod  V \rightarrow  M
\]

可得序列

\[
{\Omega }_{c}^{ * }\left( {U \cap  V}\right) \xrightarrow[]{\text{ signed inclusion }}{\Omega }_{c}^{ * }\left( U\right)  \oplus  {\Omega }_{c}^{ * }\left( V\right) \xrightarrow[]{\text{ sum }}{\Omega }_{c}^{ * }\left( M\right)
\]

\( \omega \) I \( \rightarrow \; \left( {-{j}_{ * }\omega ,{j}_{ * }\omega }\right) \)

\[
\left( {\omega ,\tau }\right) \; \mapsto  \;{j}_{ * }\omega  + {j}_{ * }\tau .
\]

命题 2.7. 具紧支集形式的 MV 序列

\[
0 \rightarrow  {\Omega }_{c}^{ * }\left( {U \cap  V}\right)  \rightarrow  {\Omega }_{c}^{ * }\left( U\right)  \oplus  {\Omega }_{c}^{ * }\left( V\right)  \rightarrow  {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  0
\]

是正合的.

证. 只证在 \( {\Omega }_{c}^{ * }\left( M\right) \) 处正合.

设 \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) 是从属于开覆盖 \( \{ U, V\} \) 的单位分解. 设 \( \omega  \in  {\Omega }_{c}^{ * }\left( M\right) \) . 显然

\[
\operatorname{Supp}\left( {{\rho }_{U}\omega }\right)  \subset  \operatorname{Supp}{\rho }_{U} \cap  \operatorname{Supp}\omega  \subset  \operatorname{Supp}\omega .
\]

因为紧集的闭子集是紧集，所以 \( \operatorname{\mathsf{S} upp}\left( {{\rho }_{U}\omega }\right) \) 是紧集. 又因为

\[
\operatorname{Supp}\left( {{\rho }_{U}\omega }\right)  \subset  \operatorname{Supp}{\rho }_{U} \subset  U
\]

所以 \( {\left. \left( {\rho }_{U}\omega \right) \right| }_{U} \in  {\Omega }_{c}^{ * }\left( U\right) \) . 同理, \( {\left. \left( {\rho }_{V}\omega \right) \right| }_{V} \in  {\Omega }_{c}^{ * }\left( V\right) \) . 于是

\[
\left( {{\left. \left( {\rho }_{U}\omega \right) \right| }_{U},{\left. \left( {\rho }_{V}\omega \right) \right| }_{V}}\right)  \mapsto  {\rho }_{U}\omega  + {\rho }_{V}\omega  = \omega .
\]

由具紧支集的 MV 序列导出紧上同调的长正合序列:

\( \cdots  \rightarrow  {H}_{c}^{q}\left( {U \cap  V}\right) \overset{\delta }{ \rightarrow  }{H}_{c}^{q}\left( U\right)  \oplus  {H}_{c}^{q}\left( V\right) \overset{s}{ \rightarrow  }{H}_{c}^{q}\left( M\right) \;\overset{{d}_{ * }}{ \rightarrow  }{H}_{c}^{q + 1}(U \cap \)

\[
\left\lbrack  \omega \right\rbrack  \; \mapsto  \;\left( {\left\lbrack  {-{j}_{ * }\omega }\right\rbrack  ,\left\lbrack  {{j}_{ * }\omega }\right\rbrack  }\right)
\]

\[
\left( {\left\lbrack  \omega \right\rbrack  ,\left\lbrack  \tau \right\rbrack  }\right) \; \mapsto  \;\left\lbrack  {{j}_{ * }\omega  + {j}_{ * }\tau }\right\rbrack
\]

连接同态 \( {d}_{ * } \) 的定义. 给定 \( \omega  \in  {\Omega }_{c}^{q}\left( M\right) ,{d\omega } = 0 \) ,则

\[
\eta \underset{\left( 3\right) }{ \rightarrow  }{d\xi } = \left( {{\left. d\left( {\rho }_{U}\omega \right) \right| }_{U},{\left. d\left( {\rho }_{V}\omega \right) \right| }_{V}}\right) \underset{s}{ \rightarrow  }0
\]

\( \begin{matrix} d \uparrow  \left( 2\right) & d \uparrow  \\  \xi  = \left( {\left. \left( {\rho }_{U}\omega \right) {\left. \right| }_{U},\left( {\rho }_{V}\omega \right) \right| }_{V}\right) & \xrightarrow[\left( 1\right) ]{s}\omega  \end{matrix} \)

由于 \( {sd\xi } = {ds\xi } = {d\omega } = 0 \) ，所以

\[
- {\left. d\left( {\rho }_{U}\omega \right) \right| }_{U \cap  V} = {\left. d\left( {\rho }_{V}\omega \right) \right| }_{U \cap  V}.
\]

显然

\[
{\left. d\left( {\rho }_{U}\omega \right) \right| }_{U \cap  V},{\left. d\left( {\rho }_{V}\omega \right) \right| }_{U \cap  V} \in  {\Omega }_{c}^{q + 1}\left( {U \cap  V}\right) .
\]

所以可取

\[
\eta  =  - {\left. d\left( {\rho }_{U}\omega \right) \right| }_{U \cap  V}.
\]

定义

\[
{d}_{ * }\left( \left\lbrack  \omega \right\rbrack  \right)  = \left\lbrack  \eta \right\rbrack  .
\]

虽说 \( \eta \) 是一个恰当形式,但 \( {\left. \left( {\rho }_{U}\omega \right) \right| }_{U \cap  V} \) 不一定属于 \( {\Omega }_{c}^{q}\left( {U \cap  V}\right) \) ,所以 \( \left\lbrack  \eta \right\rbrack   \in \; {H}_{c}^{q + 1}\left( {U \cap  V}\right) \) 不一定为零.

例 2.8. \( \left( {S}^{1}\right. \) 的紧上同调) 因为 \( {S}^{1} \) 紧,所以 \( {H}_{c}^{ * }\left( {S}^{1}\right)  = {H}^{ * }\left( {S}^{1}\right) \) . 我们也可从紧支集的 MV 序列进行计算.

\[
0 \rightarrow  {H}_{c}^{0}\left( {U \cap  V}\right)  \rightarrow  {H}_{c}^{0}\left( U\right)  \oplus  {H}_{c}^{0}\left( V\right) \overset{s}{ \rightarrow  }{H}_{c}^{0}\left( {S}^{1}\right) \overset{{d}_{ * }}{ \rightarrow  }{H}_{c}^{1}\left( {U \cap  V}\right)
\]

\[
\overset{\delta }{ \rightarrow  }{H}_{c}^{1}\left( U\right)  \oplus  {H}_{c}^{1}\left( V\right) \overset{s}{ \rightarrow  }{H}_{c}^{1}\left( {S}^{1}\right)  \rightarrow  {H}_{c}^{2}\left( {U \cap  V}\right)  \rightarrow  {H}_{c}^{2}\left( U\right)  \oplus  {H}_{c}^{2}\left( V\right)  \rightarrow  \ldots
\]

由紧上同调的 Poincaré 引理, 此长正合序列化为

\( 0 \rightarrow  0 \rightarrow  0 \rightarrow  {H}_{c}^{0}\left( {S}^{1}\right) \overset{{d}_{ * }}{ \rightarrow  }\mathbb{R} \oplus  \mathbb{R}\overset{\delta }{ \rightarrow  }\mathbb{R} \oplus  \mathbb{R}\overset{s}{ \rightarrow  }{H}_{c}^{1}\left( {S}^{1}\right)  \rightarrow  0 \rightarrow  0 \rightarrow  \ldots \)

设 \( \left\lbrack  \omega \right\rbrack   = \left\lbrack  \left( {{\omega }_{1},{\omega }_{2}}\right) \right\rbrack   \in  {H}_{c}^{1}\left( {U \cap  V}\right) \) . 则

\[
\delta \left\lbrack  \omega \right\rbrack   = \left\lbrack  \left( {-{j}_{ * }\omega ,{j}_{ * }\omega }\right) \right\rbrack   \in  {H}_{c}^{1}\left( U\right)  \oplus  {H}_{c}^{1}\left( V\right) .
\]

所以 \( \operatorname{im}\delta \) 是 1 维的. 于是

\[
{H}_{c}^{0}\left( {S}^{1}\right)  = \operatorname{im}{d}_{ * } = \ker \delta  = \mathbb{R}
\]

\[
{H}_{c}^{1}\left( {S}^{1}\right)  = \mathbb{R} \oplus  \mathbb{R}/\ker s = \mathbb{R} \oplus  \mathbb{R}/\operatorname{im}\delta  = \mathbb{R}
\]

补充练习 1. 用具紧支集的 MV 序列计算 \( {H}_{c}^{ * }\left( {{\mathbb{R}}^{2} - P}\right) \) 与 \( {H}_{c}^{ * }\left( {{\mathbb{R}}^{2} - P - Q}\right) \) ,其中 \( P, Q \) 是 \( {\mathbb{R}}^{2} \) 中两点.

再论 \( {H}^{1}\left( {S}^{1}\right)  \simeq  \mathbb{R} \) .

在 \( {S}^{1} \) 上引入通常的局部坐标 \( \theta .\theta \) 只是局部坐标因为对任意的整数 \( n,\theta  + {2n\pi } \) 与 \( \theta \) 在 \( {S}^{1} \) 上表示同一个点. 但是, \( {d\theta } \) 是 \( {S}^{1} \) 上整体定义的 1-形式.

\( {S}^{1} \) 上 1-形式可表示为 \( \omega  = a\left( \theta \right) {d\theta } \) ,其中 \( a\left( \theta \right) \) 是 \( {\mathbb{R}}^{1} \) 上周期函数: \( a\left( {\theta  + {2\pi }}\right)  = \; a\left( \theta \right) \) . 因为 \( {S}^{1} \) 是 1 维的,我们总有 \( {d\omega } = 0 \) ,即

\[
{Z}^{1}\left( {S}^{1}\right)  = {\Omega }^{1}\left( {S}^{1}\right) .
\]

设 \( \omega  \in  {B}^{1}\left( {S}^{1}\right) ,\omega  = a\left( \theta \right) {d\theta } \) . 则存在周期函数 \( F\left( \theta \right) \) 使得 \( a\left( \theta \right) {d\theta } = {dF}\left( \theta \right) \) . 因为

\[
F\left( \theta \right)  = {\int }_{0}^{\theta }a\left( \phi \right) {d\phi } + \mathrm{C},
\]

所以 \( F\left( \theta \right) \) 是周期函数当且仅当 \( {\int }_{{S}^{1}}\omega  = 0 \) . 这就是说

\[
{B}^{1}\left( {S}^{1}\right)  = \ker {\int }_{{S}^{1}}
\]

其中 \( {\int }_{{S}^{1}} : {\Omega }^{1}\left( {S}^{1}\right)  \rightarrow  \mathbb{R} \) . 由此得到

\[
{H}^{1}\left( {S}^{1}\right)  \simeq  {\Omega }^{1}\left( {S}^{1}\right) /\ker {\int }_{{S}^{1}} \simeq  \mathbb{R}.
\]

我们指出另一种计算 \( {H}^{1}\left( {S}^{1}\right) \) 的方法. 这种方法可用来推广计算齐性空间的上同调.

对 \( {S}^{1} \) 上每个 1-形式 \( \omega \) 赋予它的平均 \( \widehat{\omega } \) :

\[
\widehat{\omega }\left( \theta \right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }\omega \left( {\theta  + \tau }\right) {d\tau } = \frac{1}{2\pi }\left( {{\int }_{0}^{2\pi }a\left( {\theta  + \tau }\right) {d\tau }}\right) {d\theta }.
\]

命题. 形式 \( \omega \) 与 \( \widehat{\omega } \) 属于同一个上同调类.

证. 对固定 \( \tau \) ,定义映射 \( f : {S}^{1} \rightarrow  {S}^{1} \) 为 \( f\left( \theta \right)  = \theta  + \tau \) . 则

\[
{f}^{ * }\left( {\omega \left( \theta \right) }\right)  = {f}^{ * }\left( {a\left( \theta \right) }\right) {f}^{ * }\left( {d\theta }\right)  = a\left( {\theta  + \tau }\right) {d\theta } = \omega \left( {\theta  + \tau }\right)
\]

因为 \( f \) 同伦于恒等映射,由 de Rham 上同调的同伦不变性知 \( \omega \left( \theta \right)  \sim  \omega \left( {\theta  + \tau }\right) \) , 此处记号 “ \( \sim \) ” 表示属于同一个上同调类. 因此作为积分的 \( \widehat{\omega } \) ,它的任一个黎曼和

\[
\frac{1}{2\pi }\mathop{\sum }\limits_{i}\omega \left( {\theta  + {\tau }_{i}}\right) \bigtriangleup {\tau }_{i} \sim  \omega \left( \theta \right)  \cdot  \frac{1}{2\pi }\mathop{\sum }\limits_{i}\bigtriangleup {\tau }_{i} = \omega \left( \theta \right) ,
\]

即 \( \widehat{\omega } \) 的任一黎曼和与 \( \omega \) 属于同一上同调类. 所以 \( \widehat{\omega } \) 也与 \( \omega \) 属于同一上同调类.

再注意到 \( \widehat{\omega } \) 为

\[
\widehat{\omega }\left( \theta \right)  = {\alpha d\theta },\;\text{ 其中 }\alpha  = C = \frac{1}{2\pi }{\int }_{0}^{2\pi }a\left( \phi \right) {d\phi }.
\]

这是因为

\[
\widehat{\omega }\left( \theta \right)  = \frac{1}{2\pi }\left( {{\int }_{0}^{2\pi }a\left( {\theta  + \tau }\right) {d\tau }}\right) {d\theta }
\]

\[
= \frac{1}{2\pi }\left( {{\int }_{\theta }^{{2\pi } + \theta }a\left( \phi \right) {d\phi }}\right) {d\theta }
\]

\[
= \frac{1}{2\pi }\left( {{\int }_{0}^{2\pi }a\left( \phi \right) {d\phi }}\right) {d\theta }.
\]

因此 \( \widehat{\omega }\left( \theta \right) \) 是旋转不变的，即对任意给定的 \( {\theta }_{0} \) ，

\[
\widehat{\omega }\left( {\theta  + {\theta }_{0}}\right)  = \widehat{\omega }\left( \theta \right) .
\]

综上所述,对应 \( \omega  \mapsto  \widehat{\omega } \) 本质上对每个 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{1}\left( {S}^{1}\right) \) 赋予了唯一的实数 \( \alpha \) . 这就是同构 \( {H}^{1}\left( {S}^{1}\right)  \simeq  \mathbb{R} \) 的一种实现.

作业:

1. 补充练习 1.

代数拓扑与微分形式
