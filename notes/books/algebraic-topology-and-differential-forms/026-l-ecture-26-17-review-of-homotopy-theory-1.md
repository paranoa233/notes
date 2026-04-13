#### 第26讲 Review of Homotopy Theory (1)

§17 Review of Homotopy Theory (1)

26. 纤维化的同伦序列为接下来的谱序列应用铺平道路，在这节简单介绍同伦论. 首先给出同伦群的定义与基本性质, 计算球面的一些低维同伦群. 计算的几何思想导致贴胞腔的同伦性质. 从一些点出发通过贴从低维到高维的胞腔所构造的空间称为 CW 复形. 接着讨论同伦与同调之间的关系,应用同调谱序列证明 Hurewicz 同构定理. 作为推论直接得到 \( n \) 维球面的 \( q \leq  n \) 的同伦群 \( {\pi }_{q}\left( {S}^{n}\right) \) . 由于时间关系,我们不准备与书本一样离题去讲 Morse 理论, 它主要用来证明流形具有 CW 复形的伦型. 我们也不准备用微分形式的语言去讨论 Hopf 不变量,它与同伦群 \( {\pi }_{{2n} - 1}\left( {S}^{n}\right) \) 有关.

我们分两次课讲这节. 这次课讲

- 同伦群

- 纤维化的同伦序列

- 相对同伦序列

- 自由同伦群

同伦群

设 \( X \) 是拓扑空间, \( * \) 是基点. 记 \( {I}^{q} \) 为 \( q \) 维方体,它的边界记作 \( \partial {I}^{q} \) . 对 \( q \geq  1 \) ,记 \( {\pi }_{q}\left( X\right) \) 为 \( X \) 的第 \( q \) 个同伦群,它的元 \( \left\lbrack  \alpha \right\rbrack \) 是以下映射 \( \alpha \) 的同伦类:

\[
\alpha  : {I}^{q} \rightarrow  X,{\left. \;\alpha \right| }_{\partial {I}^{q}} =  * .
\]

此处同伦是指定点同伦,即它的两个元 \( \left\lbrack  \alpha \right\rbrack   = \left\lbrack  \beta \right\rbrack \) 当且仅当存在映射 \( F : {I}^{q} \times  I \rightarrow  X \) 使得

\[
{\left. F\right| }_{{I}^{q}\times \{ 0\} } = {\left. \alpha ,\;F\right| }_{{I}^{q}\times \{ 1\} } = \beta ,\;F\left( {\partial {I}^{q} \times  I}\right)  =  * .
\]

当然 \( {\pi }_{q}\left( X\right) \) 也可看作从 \( q \) 维球面 \( {S}^{q} \) 到 \( X \) 的保基点映射的同伦类的全体.

可在 \( {\pi }_{q}\left( X\right) \) 上定义群的运算. 若 \( \left\lbrack  \alpha \right\rbrack  ,\left\lbrack  \beta \right\rbrack   \in  {\pi }_{q}\left( X\right) \) ,定义乘积 \( \left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack   \in  {\pi }_{q}\left( X\right) \) 为映射 \( \gamma  : {I}^{q} \rightarrow  X \) 的同伦类,其中

\[
\gamma \left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \left\{  \begin{array}{ll} \alpha \left( {2{t}_{1},{t}_{2},\ldots ,{t}_{q}}\right) , & \text{ 对 }0 \leq  {t}_{1} \leq  1/2, \\  \beta \left( {2{t}_{1} - 1,{t}_{2},\ldots ,{t}_{q}}\right) , & \text{ 对 }1/2 \leq  {t}_{1} \leq  1. \end{array}\right.
\]

习惯上将 \( \gamma \) 记作 \( {\alpha \beta } \) .

![bo_d7e85t491nqc73eqefm0_609_575_644_1199_1078_0.jpg](images/fu_algebraic_topology_and_differential_forms_179_bod7e85t491nqc73eqefm0609575644119910780.jpg)

命题 17.1. (a) \( {\pi }_{q}\left( {X \times  Y}\right)  = {\pi }_{q}\left( X\right)  \times  {\pi }_{q}\left( Y\right) \) .

(b) 对 \( q \geq  2,{\pi }_{q}\left( X\right) \) 是一个 abel 群.

证. (a) \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X \times  Y}\right) \) 的代表元 \( \alpha  : {I}^{q} \rightarrow  X \times  Y \) 可分解为 \( \alpha  = \left( {{\alpha }_{1},{\alpha }_{2}}\right) \) ,其中 \( {\alpha }_{1} \) 是 \( \alpha \) 与投射 \( {\pi }_{1} : X \times  Y \rightarrow  X \) 的复合, \( {\alpha }_{2} \) 是 \( \alpha \) 与投射 \( {\pi }_{2} : X \times  Y \rightarrow  Y \) 的复合. 所以存在自然映射

\[
{\pi }_{q}\left( {X \times  Y}\right)  \rightarrow  {\pi }_{q}\left( X\right)  \times  {\pi }_{q}\left( Y\right)
\]

\[
\left\lbrack  \alpha \right\rbrack   \mapsto  \left( {\left\lbrack  {\alpha }_{1}\right\rbrack  ,\left\lbrack  {\alpha }_{2}\right\rbrack  }\right)
\]

显然这个映射是双射，并且由于

\[
\left( {{\alpha }_{1},{\alpha }_{2}}\right) \left( {{\beta }_{1},{\beta }_{2}}\right)  = \left( {{\alpha }_{1}{\beta }_{1},{\alpha }_{2}{\beta }_{2}}\right)
\]

所以这个双射是群同构.

(b) 设 \( \left\lbrack  \alpha \right\rbrack  ,\left\lbrack  \beta \right\rbrack   \in  {\pi }_{q}\left( X\right) .\left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack \) 的一个代表元是 \( \gamma \) :

\[
\gamma \left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \left\{  \begin{array}{ll} \alpha \left( {2{t}_{1},{t}_{2},\ldots ,{t}_{q}}\right) , & 0 \leq  {t}_{1} \leq  1/2, \\  \beta \left( {2{t}_{1} - 1,{t}_{2},\ldots ,{t}_{q}}\right) , & 1/2 \leq  {t}_{1} \leq  1. \end{array}\right.
\]

\( \alpha \; \beta \)

\( \gamma \) 同伦于 \( {\delta }_{1} \) :

\[
\begin{array}{l} \text{ “ }\beta \\  \text{ “ }\beta \\  \end{array}\;{\delta }_{1}\left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \begin{cases} \alpha \left( {2{t}_{1},2{t}_{2} - 1,\ldots ,{t}_{q}}\right) , & \\  0 \leq  {t}_{1} \leq  1/2,1/2 \leq  {t}_{2} \leq  1, & \\  \beta \left( {2{t}_{1} - 1,2{t}_{2},\ldots ,{t}_{q}}\right) , & \\  1/2 \leq  {t}_{1} \leq  1,0 \leq  {t}_{2} \leq  1/2, & \\  \text{ 基点 } * , & \text{ 其余情形. } \end{cases}
\]

\( {\delta }_{1} \) 依次同伦于以下图中的 \( {\delta }_{2},{\delta }_{3},{\delta }_{4} \) :

![bo_d7e85t491nqc73eqefm0_611_470_1278_1340_277_0.jpg](images/fu_algebraic_topology_and_differential_forms_180_bod7e85t491nqc73eqefm0611470127813402770.jpg)

所以 \( \left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack   = \left\lbrack  {\alpha \beta }\right\rbrack   = \left\lbrack  {\beta \alpha }\right\rbrack   = \left\lbrack  \beta \right\rbrack  \left\lbrack  \alpha \right\rbrack \) .

610 补充练习 1 . 写出从 \( {\delta }_{1} \) 到 \( {\delta }_{2} \) 的同伦.

补充练习 2 . 当 \( q \geq  2 \) 时,对 \( t \in  \left\lbrack  {0,1}\right\rbrack \) ,定义微分同胚 \( {h}_{t} : {S}^{q} \rightarrow  {S}^{q} \) ,

\[
{h}_{t}\left( x\right)  = \left( {{x}_{0}\cos \left( {t\pi }\right)  - {x}_{1}\sin \left( {t\pi }\right) ,{x}_{0}\sin \left( {t\pi }\right)  + {x}_{1}\cos \left( {t\pi }\right) ,{x}_{2},\ldots ,{x}_{q}}\right) .
\]

试用 \( {h}_{t} \) 给出命题 17.1(b) 的一个更直接的证明.

引入 \( {\pi }_{0}\left( X\right) \) 通常是有用的,把它定义为 \( X \) 的所有道路分支的集合. 它有一个特殊元,即 \( X \) 的基点所在的道路分支,也把它称为 \( {\pi }_{0}\left( X\right) \) 的基点. 一个流形的道路分支与连通分支是相同的. 一般来说, \( {\pi }_{0}\left( X\right) \) 不是群. 但若 \( G \) 是李群,则 \( {\pi }_{0}\left( G\right) \) 有群结构.

命题 17.3. 李群 \( G \) 的单位(元所在的)连通分支 \( H \) 是 \( G \) 的正规子群. 因此 \( {\pi }_{0}\left( G\right)  = G/H \) 是群.

证. 李群 \( G \) 是流形且具有群结构使得群的运算,即乘法与逆是光滑映射. 设 \( a, b \in  H \) . 因为 \( {bH} \) 连通且 \( b \in  {bH} \cap  H \) ,所以 \( {bH} \subset  H \) . 于是 \( {abH} \subset  {aH} \subset  H \) . 由此可得 \( {ab} \in  H \) . 同理,因为 \( {a}^{-1}H \) 连通且 \( 1 \in  {a}^{-1}H \cap  H \) ,所以 \( {a}^{-1}H \subset  H \) . 由此可得 \( {a}^{-1} \in  H \) . 综上所述, \( H \) 是子群.

设 \( g \in  G \) . 因为 \( {gH}{g}^{-1} \) 连通且 \( 1 \in  {gH}{g}^{-1} \cap  H \) ,所以 \( {gH}{g}^{-1} \subset  H \) . 由此可得 \( H \) 是正规子群. 于是 \( G/H \) 是群.

由于 \( g : G \rightarrow  G \) 是同胚,所以陪集 \( {gH} \) 是连通的. 因为不同的陪集不相交,所以 \( G/H \) 恰好由 \( G \) 的连通分支组成. 因此 \( {\pi }_{0}\left( G\right)  = G/H \) 是群.

纤维化的同伦序列设 \( \pi  : E \rightarrow  B \) 是以 \( F \) 为纤维的纤维化, \( F = {\pi }^{-1}\left( *\right) \) . 设 \( E \) 的基点在 \( F \) 上,它也是 \( F \) 的基点. 则有以下同伦群的正合序列,称为纤维化的同伦序列:

(17.4)

\[
\cdots  \rightarrow  {\pi }_{q}\left( F\right) \overset{{i}_{ * }}{ \rightarrow  }{\pi }_{q}\left( E\right) \overset{{\pi }_{ * }}{ \rightarrow  }{\pi }_{q}\left( B\right) \overset{\partial }{ \rightarrow  }{\pi }_{q - 1}\left( F\right)  \rightarrow  \ldots
\]

\[
\cdots  \rightarrow  {\pi }_{1}\left( B\right)  \rightarrow  {\pi }_{0}\left( F\right)  \rightarrow  {\pi }_{0}\left( E\right)  \rightarrow  {\pi }_{0}\left( B\right)  \rightarrow  0.
\]

对序列的正合性不作证明，但给出以下一些解释.

(a) \( {i}_{ * } \) 与 \( {\pi }_{ * } \) 是由包含映射 \( i : F \rightarrow  E \) 与投射 \( \pi  : E \rightarrow  B \) 自然诱导.

(b) 最后三个映射

\[
{\pi }_{1}\left( B\right) \overset{\partial }{ \rightarrow  }{\pi }_{0}\left( F\right) \overset{{i}_{ * }}{ \rightarrow  }{\pi }_{0}\left( E\right) \overset{{\pi }_{ * }}{ \rightarrow  }{\pi }_{0}\left( B\right)
\]

只是集合的映射，映射的核定义为基点的逆像. 所以正合性还是理解为 “像等于核”. 例如,当 \( n \geq  2 \) 时,纤维化 \( \pi  : {S}^{n} \rightarrow  \mathbb{R}{P}^{n} \) 的正合同伦序列为

\[
\rightarrow  {\pi }_{1}\left( {S}^{n}\right)  \rightarrow  {\pi }_{1}\left( {\mathbb{R}{P}^{n}}\right)  \rightarrow  {\pi }_{0}\left( {\{ \cdot , \cdot  \} }\right)  \rightarrow  {\pi }_{0}\left( {S}^{n}\right)  \rightarrow  {\pi }_{0}\left( {\mathbb{R}{P}^{n}}\right)  \rightarrow  0
\]

II II II

0 \{·\} \( \{  \cdot  \} \)

所以 \( {\pi }_{1}\left( {\mathbb{R}{P}^{n}}\right) \) 是含有两个元的群,即 \( {\mathbb{Z}}_{2} \) .

(c) \( \partial \) 的定义.

当 \( q = 1 \) 时,设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{1}\left( B\right) \) ,即 \( \alpha  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  B,\alpha \left( 0\right)  = \alpha \left( 1\right)  =  * \) . 对 \( Y \) 是一点的情形用覆盖同伦性质,所以存在映射 \( \overline{\alpha } : \left\lbrack  {0,1}\right\rbrack   \rightarrow  E \) 使得 \( \overline{\alpha }\left( 0\right)  = { * }_{F},\pi  \circ  \overline{\alpha } = \alpha \) . 所以 \( \overline{\alpha }\left( 1\right)  \in  F \) . 定义

\( \partial \left( \left\lbrack  \alpha \right\rbrack  \right)  = F \) 的 \( \overline{\alpha }\left( 1\right) \) 所在的道路分支 \( \in  {\pi }_{0}\left( F\right) \) .

当 \( q = 2 \) 时,设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{2}\left( B\right) \) ,即 \( \alpha  : {I}^{2} \rightarrow  B,{\left. \alpha \right| }_{\partial {I}^{2}} =  * \) . 需用覆盖同伦性质. 此时, \( Y = I, f : I \rightarrow  E \) 是从 \( I \) 到 \( F \) 的基点 \( { * }_{F} \) 的常值映射. 所以 \( \bar{f} : I \rightarrow  B \) 是从 \( I \) 到 \( B \) 的基点 \( * \) 的常值映射,而由 \( {\bar{f}}_{t}\left( s\right)  = \alpha \left( {s, t}\right) \) 定义的 \( {\bar{f}}_{t} \) 是 \( \bar{f} \) 的一个同伦. 由覆盖同伦性质知存在 \( f \) 的同伦 \( {f}_{t} : I \rightarrow  E \) 使得 \( \pi  \circ  {f}_{t} = {\bar{f}}_{t} \) . 令

\[
\widetilde{\alpha }\left( {s, t}\right)  = {f}_{t}\left( s\right) .
\]

则

\[
\pi  \circ  \widetilde{\alpha } = \alpha ,\;\widetilde{\alpha }\left( {s,0}\right)  = f\left( s\right)  = { * }_{F}.
\]

设 \( g : {I}^{2} \rightarrow  {I}^{2} \) 是同胚,它将由 \( \partial {I}^{2} \) 的底边与左右边组成的 \( {J}^{1} \) 映到 \( \partial {I}^{2} \) 的底边, 见下图. 令 \( \overline{\alpha } = \widetilde{\alpha } \circ  g : {I}^{2} \rightarrow  E \) . 则 \( \pi  \circ  \overline{\alpha } = \alpha  \circ  g \) . 于是

\[
{\left. \overline{\alpha }\right| }_{{J}^{1}} = { * }_{F},\;\overline{\alpha }\left( {s,1}\right)  \in  {\pi }^{-1}\left( *\right)  = F.
\]

定义

\[
\partial \left( \left\lbrack  \alpha \right\rbrack  \right)  = \left\lbrack  {\left. \overline{\alpha }\right| }_{I\times \{ 1\} }\right\rbrack   \in  {\pi }_{1}\left( F\right) . \tag{56}
\]

![bo_d7e85t491nqc73eqefm0_617_592_774_1149_681_0.jpg](images/fu_algebraic_topology_and_differential_forms_181_bod7e85t491nqc73eqefm061759277411496810.jpg)

当 \( q \geq  3 \) 时,类似地可定义 \( \partial \) .

例 17.5. 覆盖空间 \( \pi  : E \rightarrow  B \) 是一个具有离散纤维的纤维化. 因为对 \( q \geq  1 \) ， \( {\pi }_{q}\left( F\right)  = 0 \) ,所以根据纤维化的同伦序列,有

\[
{\pi }_{q}\left( E\right)  = {\pi }_{q}\left( B\right) \;\text{ 对 }q \geq  2,
\]

与单射

\[
{\pi }_{1}\left( E\right)  \hookrightarrow  {\pi }_{1}\left( B\right)
\]

命题 17.2. 对 \( q \geq  2,{\pi }_{q - 1}\left( {\Omega X}\right)  = {\pi }_{q}\left( X\right) \) .

证. 应用纤维为 \( {\Omega X} \) 的纤维化 \( \pi  : {PX} \rightarrow  X \) 的同伦序列

\[
\cdots  \rightarrow  {\pi }_{q}\left( {PX}\right)  \rightarrow  {\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega X}\right)  \rightarrow  {\pi }_{q - 1}\left( {PX}\right)  \rightarrow  \ldots
\]

由于 \( {PX} \) 可缩,所以当 \( q \geq  1 \) 时, \( {\pi }_{q}\left( {PX}\right)  = 0 \) . 于是对 \( q \geq  2 \) ,

\[
{\pi }_{q}\left( X\right)  = {\pi }_{q - 1}\left( {\Omega X}\right)
\]

上述命题有直观的几何解释. 当 \( q = 2 \) 时,设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{2}\left( X\right) \) ,即

\[
\alpha  : {I}^{2} \rightarrow  X,{\left. \;\alpha \right| }_{\partial {I}^{2}} =  *
\]

则对任意 \( t \in  \left\lbrack  {0,1}\right\rbrack  ,\alpha \left( {\cdot , t}\right)  : I \rightarrow  X \) 是 \( X \) 中以 \( * \) 为基点的一个圈. 所以

\[
\widetilde{\alpha }\left( t\right)  = \alpha \left( {\cdot , t}\right)  \in  {\Omega X},
\]

其中 \( \widetilde{\alpha }\left( 0\right)  = \widetilde{\alpha }\left( 1\right)  = \overline{ * } \in  {\Omega X} \) 是 \( X \) 中一条常值道路 \( * \) . 这就是说 \( \widetilde{\alpha } : I \rightarrow  {\Omega X} \) 是 \( {\Omega X} \) 中一条以 \( \overline{ * } \) 为基点的一个圈. 所以有自然映射 \( {\pi }_{2}\left( X\right)  \rightarrow  {\pi }_{1}\left( {\Omega X}\right) ,\left\lbrack  \alpha \right\rbrack   \mapsto  \left\lbrack  \widetilde{\alpha }\right\rbrack \) . 一般的情况是类似的,可将从 \( {I}^{q} \) 到 \( X \) 的映射视为从 \( {I}^{q - 1} \) 到 \( {\Omega X} \) 的映射.

![bo_d7e85t491nqc73eqefm0_619_512_1114_397_385_0.jpg](images/fu_algebraic_topology_and_differential_forms_183_bod7e85t491nqc73eqefm061951211143973850.jpg)

![bo_d7e85t491nqc73eqefm0_619_1079_986_703_608_0.jpg](images/fu_algebraic_topology_and_differential_forms_182_bod7e85t491nqc73eqefm061910799867036080.jpg)

相对同伦序列设 \( X \) 是道路连通空间, \( A \subset  X \) 是子集, \( *  \in  A \) 是基点. 定义

\[
{\Omega }_{ * }^{A} = \{ \sigma  : I \rightarrow  X \mid  \sigma \left( 0\right)  =  * ,\sigma \left( 1\right)  \in  A\} .
\]

端点映射 \( e : {\Omega }_{ * }^{A} \rightarrow  A \) 为 \( e\left( \sigma \right)  = \sigma \left( 1\right)  \in  A \) . 所以有纤维化这个纤维化的同伦序列是

\[
\cdots  \rightarrow  {\pi }_{q}\left( A\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega X}\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega }_{ * }^{A}\right)  \rightarrow  {\pi }_{q - 1}\left( A\right)  \rightarrow  \ldots
\]

\[
\ldots  \rightarrow  {\pi }_{1}\left( A\right)  \rightarrow  {\pi }_{0}\left( {\Omega X}\right)  \rightarrow  {\pi }_{0}\left( {\Omega }_{ * }^{A}\right)  \rightarrow  {\pi }_{0}\left( A\right)  \rightarrow  0.
\]

![bo_d7e85t491nqc73eqefm0_620_965_689_401_294_0.jpg](images/fu_algebraic_topology_and_differential_forms_185_bod7e85t491nqc73eqefm06209656894012940.jpg)

![bo_d7e85t491nqc73eqefm0_620_808_1073_699_568_0.jpg](images/fu_algebraic_topology_and_differential_forms_184_bod7e85t491nqc73eqefm062080810736995680.jpg)

定义相对同伦群 \( {\pi }_{q}\left( {X, A}\right) \) 为 \( {\pi }_{q - 1}\left( {\Omega }_{ * }^{A}\right) \) . 则上述序列变成 \( A \) 在 \( X \) 中的相对同伦序列:

(17.7)

\[
\cdots  \rightarrow  {\pi }_{q}\left( A\right)  \rightarrow  {\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q}\left( {X, A}\right) \overset{\overline{\partial }}{ \rightarrow  }{\pi }_{q - 1}\left( A\right)  \rightarrow  \ldots
\]

\[
\ldots  \rightarrow  {\pi }_{1}\left( X\right)  \rightarrow  {\pi }_{1}\left( {X, A}\right)  \rightarrow  {\pi }_{0}\left( A\right)  \rightarrow  0.
\]

注意 \( {\pi }_{q}\left( {X, A}\right) \) 对 \( q \geq  3 \) 是 abel 群, \( {\pi }_{2}\left( {X, A}\right) \) 是群,而 \( {\pi }_{1}\left( {X, A}\right) \) 仅是一个集合. 事实上, \( {\pi }_{q}\left( {X, A}\right) \) 可定义如下:

\[
{\pi }_{q}\left( {X, A}\right)  = \left\{  {\left\lbrack  \alpha \right\rbrack   \mid  \alpha  : {I}^{q} \rightarrow  X,\alpha  : {I}^{q - 1} \rightarrow  A,\alpha  : {J}^{q - 1} \rightarrow   * }\right\}
\]

其中，

\[
{I}^{q - 1} = \left\{  {\left( {{x}_{1},\ldots ,{x}_{q - 1},1}\right)  \in  {I}^{q}}\right\}  ,\;{J}^{q - 1} = \overline{\partial {I}^{q} - {I}^{q - 1}}.
\]

映射 \( \overline{\partial } : {\pi }_{q}\left( {X, A}\right)  \rightarrow  {\pi }_{q - 1}\left( A\right) \) 定义为

\[
\overline{\partial }\left( \left\lbrack  \alpha \right\rbrack  \right)  = \left\lbrack  {\left. \alpha \right| }_{{I}^{q - 1}}\right\rbrack  .
\]

对纤维化 \( F \rightarrow  E \rightarrow  B \) ,在 (17.7) 中令 \( A = F, X = E \) ,再与 (17.4) 比较,得到 \( {\pi }_{q}\left( B\right)  \simeq  {\pi }_{q}\left( {E, F}\right) \) . 我们在构造正合序列 (17.4) 时,对 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( B\right) \) 构造了 \( \overline{\alpha } \in  {\pi }_{q}\left( {E, F}\right) \) ,而 \( \partial \left\lbrack  \alpha \right\rbrack   = \overline{\partial }\left\lbrack  \overline{\alpha }\right\rbrack \) . 这就是说,映射 \( \partial  : {\pi }_{q}\left( B\right)  \rightarrow  {\pi }_{q - 1}\left( F\right) \) 可分解为

![bo_d7e85t491nqc73eqefm0_622_606_1125_1110_569_0.jpg](images/fu_algebraic_topology_and_differential_forms_186_bod7e85t491nqc73eqefm0622606112511105690.jpg)

自由同伦群

警示 17.6. (基点的依赖性) 设 \( X \) 是道路连通空间, \( x, y \in  X \) . 考虑分别以 \( x \) 与 \( y \) 为基点的同伦群 \( {\pi }_{q}\left( {X, x}\right) \) 与 \( {\pi }_{q}\left( {X, y}\right) \) . 一条从 \( x \) 到 \( y \) 的道路 \( \gamma \) 通过共轭诱导了从以 \( x \) 为基点的圈空间 \( {\Omega }_{x}X \) 到以 \( y \) 为基点的圈空间 \( {\Omega }_{y}X \) 的映射

\[
{\gamma }_{\# } : {\Omega }_{x}X \rightarrow  {\Omega }_{y}X,\;{\gamma }_{\# }\left( \lambda \right)  = {\gamma \lambda }{\gamma }^{-1}.
\]

![bo_d7e85t491nqc73eqefm0_623_836_738_681_418_0.jpg](images/fu_algebraic_topology_and_differential_forms_188_bod7e85t491nqc73eqefm06238367386814180.jpg)

这又诱导了同伦群之间的映射

![bo_d7e85t491nqc73eqefm0_623_610_1329_1102_279_0.jpg](images/fu_algebraic_topology_and_differential_forms_187_bod7e85t491nqc73eqefm0623610132911022790.jpg)

其中 \( \bar{x} \) 与 \( \bar{y} \) 分别是到 \( x \) 与 \( y \) 的常值映射. 显然 \( {\gamma }_{ * } \) 是同构,它的逆是 \( {\left( {\gamma }^{-1}\right) }_{ * } \) . 可显式描述 \( {\gamma }_{ * } \) 如下. 设 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X, x}\right) \) . 需定义映射

\[
F : {I}^{q + 1} = {I}^{q} \times  I \rightarrow  X
\]

使得 \( F \) 限制在 \( {I}^{q + 1} \) 的底面 \( {I}^{q} \times  \{ 0\} \) 为 \( \alpha \) ,限制在垂直面 \( \partial {I}^{q} \times  I \) 为 \( \gamma \) ,即若 \( \left( {u, t}\right)  \in  {I}^{q} \times  I \) ,则

\[
F\left( {u,0}\right)  = \alpha \left( u\right) ,\;\text{ 对 }u \in  {I}^{q}
\]

\[
F\left( {u, t}\right)  = \gamma \left( t\right) ,\;\text{ 对 }u \in  \partial {I}^{q}.
\]

![bo_d7e85t491nqc73eqefm0_624_799_821_731_729_0.jpg](images/fu_algebraic_topology_and_differential_forms_189_bod7e85t491nqc73eqefm06247998217317290.jpg)

障碍性理论的另一延拓原理把 \( F \) 延拓到整个 \( {I}^{q + 1} \) . \( F \) 到顶面的限制表示 \( {\gamma }_{ * }\left\lbrack  \alpha \right\rbrack \) . \( {\gamma }_{ * } \) 仅依赖于 \( \gamma \) 在所有从 \( x \) 到 \( y \) 的道路中的同伦类,所以当 \( x = y \) 时,映射 \( \left\lbrack  \gamma \right\rbrack   \mapsto  {\gamma }_{ * } \) 定义了 \( {\pi }_{1}\left( {X, x}\right) \) 在 \( {\pi }_{q}\left( {X, x}\right) \) 上一个作用. 只有当这个作用平凡时,就不需要特别指出基点而直接把同伦群记作 \( {\pi }_{q}\left( X\right) \) . 也只有在这时,可把自由同伦群 \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) 等同于 \( {\pi }_{q}\left( X\right) \) ; 此处自由同伦是指不必保基点的同伦. 但是一般来讲 \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) 不是群,它与 \( {\pi }_{q}\left( X\right) \) 的关系如下.

命题 17.6.1. 设 \( X \) 是一个道路连通空间. 忘基点映射(从保基点映射到所有映射的集合的包含)诱导了一个双射

\[
{\pi }_{q}\left( {X, x}\right) /{\pi }_{1}\left( {X, x}\right) \overset{ \sim  }{ \rightarrow  }\left\lbrack  {{S}^{q}, X}\right\rbrack
\]

其中左边记号表明等价关系: \( \left\lbrack  \alpha \right\rbrack   \sim  {\gamma }_{ * }\left\lbrack  \alpha \right\rbrack \) 对 \( \left\lbrack  \gamma \right\rbrack   \in  {\pi }_{1}\left( {X, x}\right) \) .

证. 设 \( h : {\pi }_{q}\left( {X, x}\right)  \rightarrow  \left\lbrack  {{S}^{q}, X}\right\rbrack \) 由忘基点映射诱导. 若 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X, x}\right) ,\left\lbrack  \gamma \right\rbrack   \in \; {\pi }_{1}\left( {X, x}\right) \) ,费力但不难写下 \( \alpha \) 与 \( {\gamma }_{ * }\alpha \) 之间的显式自由同伦. 事实上,只要将 \( \gamma \) 与 \( {\gamma }^{-1} \) 同伦收缩到一点即可,因为现在是不需要保持基点的. 下图分别表示 \( q = 1 \) 与 \( q = 2 \) 的情形.

![bo_d7e85t491nqc73eqefm0_626_602_321_362_456_0.jpg](images/fu_algebraic_topology_and_differential_forms_192_bod7e85t491nqc73eqefm06266023213624560.jpg)

![bo_d7e85t491nqc73eqefm0_626_1129_208_610_607_0.jpg](images/fu_algebraic_topology_and_differential_forms_190_bod7e85t491nqc73eqefm062611292086106070.jpg)

因此通过 \( {\pi }_{1}\left( {X, x}\right) \) 在 \( {\pi }_{q}\left( {X, x}\right) \) 上的作用可将映射 \( h \) 分解并且定义映射 \( H \) :

![bo_d7e85t491nqc73eqefm0_626_568_1126_1189_569_0.jpg](images/fu_algebraic_topology_and_differential_forms_191_bod7e85t491nqc73eqefm0626568112611895690.jpg)

因为 \( X \) 是道路连通的,在 \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) 中的任意映射可被形变到一个保基点的映射,所以 \( H \) 是满射. 为了证明 \( H \) 是单射,假定 \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X, x}\right) \) 在 \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) 中是零伦的, 即存在一个映射 \( F : {I}^{q + 1} \rightarrow  X \) 使得 \( F \) 限制在顶面是 \( \alpha \) ,限制在底面是常值点 \( \bar{x} \) , 并且 \( F \) 限制在每个水平切片的边上是常值的.

![bo_d7e85t491nqc73eqefm0_627_419_735_689_601_0.jpg](images/fu_algebraic_topology_and_differential_forms_194_bod7e85t491nqc73eqefm06274197356896010.jpg)

![bo_d7e85t491nqc73eqefm0_627_1275_657_546_740_0.jpg](images/fu_algebraic_topology_and_differential_forms_193_bod7e85t491nqc73eqefm062712756575467400.jpg)

设 \( \gamma \) 是 \( F \) 到垂直线段的限制. 则 \( \left\lbrack  \alpha \right\rbrack   = {\gamma }_{ * }\left( \left\lbrack  \bar{x}\right\rbrack  \right) \) . 因此 \( H \) 是单射.

作业:

1. 补充练习 1.

2. 补充练习 2.

代数拓扑与微分形式
