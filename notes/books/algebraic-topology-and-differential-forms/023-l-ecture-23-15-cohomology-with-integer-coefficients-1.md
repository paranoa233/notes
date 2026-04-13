#### 第23讲 Cohomology with Integer Coefficients (1)

代数拓扑与微分形式 §15 Cohomology with Integer Coefficients (1)

## 23. 整系数奇异同调

\( \mathbb{Z} \) -模中的元称为挠元若它的某一整数倍是零. de Rham 理论是实系数上同调,它没有挠元. 但是为了应用到同伦论, 研究挠元是无法避免的. 这节的目的是定义奇异上同调, 用奇异上链函子 \( {S}^{ * } \) 代替微分形式函子 \( {\Omega }^{ * } \) , 并证明前面的谱序列结果对整系数仍成立. 关键仍是可数多个开集的 MV 序列. 我们很自然地在拓扑空间与连续映射的范畴中研究奇异理论，而不是限制更强的 de Rham 理论这种微分流形与光滑映射的范畴. 除非另作申明, 我们以后将在连续范畴中研究.

这次课讲整系数的奇异同调, 下次讲奇异上同调.

- Extension 问题

- 奇异同调

- 锥构造

- 奇异链的 MV 序列 An element in a \( \mathbb{Z} \) -module is said to be torsion if some integral multiple of it is zero. Since the de Rham theory is a cohomology theory with real coefficients, it necessarily overlooks the torsion phenomena. For applications to homotopy theory, however, it is essential to investigate the torsion. The goal of this section is to replace the differential form functor \( {\Omega }^{ * } \) with the singular cochain functor \( {S}^{ * } \) , define the singular cohomology, and show that the preceding results on spectral sequences carry over to integer coefficients. The key as before is the Mayer-Vietoris sequence for countably many open sets. The natural setting for the singular theory is the category of topological spaces and continuous maps, rather than the more restrictive category of differentiable manifolds and \( {C}^{\infty } \) maps of de Rham theory. Unless otherwise indicated, from here till the end of Section 18 we will work in the continuous category. We begin with a review of the basic definitions of singular homology.

Extension 问题

注记 14.17. (Extension 问题) 设 \( V \) 是向量空间,向量空间的序列 \( {\left\{  {V}_{p}\right\}  }_{p = 0}^{\infty } \) 是 \( V \) 上一个滤列, \( {V}_{0} = V \) . 由于维数是向量空间的唯一不变量,所以相伴的分级向量空间同构于 \( V \) 本身.

\[
{GV} = {\bigoplus }_{p = 0}^{\infty }{V}_{p}/{V}_{p + 1} \simeq  V
\]

特别地,若双复形 \( K \) 是向量空间,则由它形成的单复形的上同调

\[
{H}_{D}^{n}\left( K\right)  \simeq  G{H}_{D}^{n}\left( K\right)  = \mathop{\bigoplus }\limits_{{p + q = n}}{E}_{\infty }^{p, q}.
\]

但在 abel 群范畴,相伴的分级群不能确定群本身. 例如群 \( {\mathbb{Z}}_{4},{\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \) 各有滤列

\[
{\mathbb{Z}}_{4} \supset  {\mathbb{Z}}_{2} \supset  0,\;{\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \supset  {\mathbb{Z}}_{2} \supset  0.
\]

这两个滤列的相伴分级群都同构于 \( {\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \) ,但是 \( {\mathbb{Z}}_{4} \) 与 \( {\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \) 不同构. 换句话说，在 abel 群的短正合序列

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \tag{53}
\]

\( A \) 与 \( C \) 不能唯一确定 \( B \) . 这种不确定性称为 extension 问题，它是同调代数的核心问题. 对我们来说, 只要熟悉以下的来自 extension 理论的基本事实就可以了.

命题 14.17.1. 在 abel 群的短正合序列

\[
0 \rightarrow  A\overset{f}{ \rightarrow  }B\overset{g}{ \rightarrow  }C \rightarrow  0 \tag{54}
\]

若 \( C \) 是自由 abel 群,即自由 \( \mathbb{Z} \) -模,则存在同态 \( s : C \rightarrow  B \) 使得 \( g \circ  s = \mathrm{{id}} \) 是 \( C \) 上恒等映射.

证. 对 \( C \) 的生成元定义 \( s \) 使得 \( g \circ  s = \mathrm{{id}} \) ,再作线性扩张.

推论 14.17.2. 在上述命题的假定下，

(a) 映射 \( \left( {f, s}\right)  : A \oplus  C \rightarrow  B \) 是同构,这就是说 \( B \) 是唯一确定的;

(b) 对任意 abel 群 \( G \) ,以下的诱导序列是正合的:

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  0
\]

(c) 对任意 abel 群 \( G \) ,以下序列是正合的:

\[
0 \rightarrow  A \otimes  G \rightarrow  B \otimes  G \rightarrow  C \otimes  G \rightarrow  0.
\]

练习 14.17.3. 证明若

\[
0 \rightarrow  {A}_{1} \rightarrow  {A}_{2} \rightarrow  {A}_{3} \rightarrow  \ldots
\]

是自由 abel 群的正合序列, \( G \) 是任意 abel 群,则以下两个序列是正合的.

\[
0 \leftarrow  \operatorname{Hom}\left( {{A}_{1}, G}\right)  \leftarrow  \operatorname{Hom}\left( {{A}_{2}, G}\right)  \leftarrow  \operatorname{Hom}\left( {{A}_{3}, G}\right)  \leftarrow  \ldots
\]

\[
0 \rightarrow  {A}_{1} \otimes  G \rightarrow  {A}_{2} \otimes  G \rightarrow  {A}_{3} \otimes  G \rightarrow  \ldots
\]

练习 14.17.4. 证明若

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0
\]

是 abel 群的短正合序列, \( G \) 是任意 abel 群,则以下两个序列是正合的.

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right) .
\]

\[
A \otimes  G \rightarrow  B \otimes  G \rightarrow  C \otimes  G \rightarrow  0.
\]

注记 15.13. 给定 abel 群 \( A \) ,设 \( F \) 是由 \( A \) 的一组生成元生成的自由 abel 群, \( R \) 是自然投射 \( p : F \rightarrow  A \) 的核. 则

(15.13.1)

\[
0 \rightarrow  R\overset{i}{ \rightarrow  }F\overset{p}{ \rightarrow  }A \rightarrow  0
\]

是 abel 群的短正合序列. 由于自由 abel 群的子群也是自由的,所以 \( R \) 是自由群. 如 (15.13.1) 的这种短正合序列称为 abel 群 \( A \) 的一个自由分解 (free resolution) .

设 \( G \) 是 abel 群. 根据练习 14.17.4,以下两个序列是正合的.

(15.13.2)

\[
0 \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  \operatorname{Hom}\left( {F, G}\right) \overset{{i}^{ * }}{ \rightarrow  }\operatorname{Hom}\left( {R, G}\right) .
\]

(15.13.3)

\[
R \otimes  G\xrightarrow[]{i \otimes  1}F \otimes  G \rightarrow  A \otimes  G \rightarrow  0.
\]

定义. 函子 Ext, Tor 分别定义为

\[
\operatorname{Ext}\left( {A, G}\right)  = \operatorname{coker}{i}^{ * } = \operatorname{Hom}\left( {R, G}\right) /\operatorname{im}{i}^{ * },
\]

\[
\operatorname{Tor}\left( {A, G}\right)  = \ker \left( {i \otimes  1}\right) .
\]

它们的定义与自由分解 \( \left( {15.13.1}\right) \) 的选取无关.

于是, Ext 与 Tor 用来衡量两个正合序列 (15.13.2) 与 (15.13.3) 是不是短正合序列. 根据定义, 以下两个序列是正合的.

\[
0 \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  \operatorname{Hom}\left( {F, G}\right) \overset{{i}^{ * }}{ \rightarrow  }\operatorname{Hom}\left( {R, G}\right)  \rightarrow  \operatorname{Ext}\left( {A, G}\right)  \rightarrow  0.
\]

\[
0 \rightarrow  \operatorname{Tor}\left( {A, G}\right)  \rightarrow  R \otimes  G\xrightarrow[]{i \otimes  1}F \otimes  G \rightarrow  A \otimes  G \rightarrow  0.
\]

练习 15.13.4. 若 \( m, n \) 是两个正整数,它们的最大公约数记为 \( \left( {m, n}\right) \) . 验证

<table><tr><td>Ext</td><td>\( \mathbb{Z} \)</td><td>\( \mathbb{Z}n \)</td></tr><tr><td>\( \mathbb{Z} \) <br> \( \mathbb{Z}m \)</td><td>0 <br> Zm</td><td>0 , <br> \( \mathbb{Z}\left( {m, n}\right) \)</td></tr></table>

<table><tr><td>Tor</td><td>\( \mathbb{Z} \)</td><td>\( \mathbb{Z}n \)</td></tr><tr><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td></tr><tr><td>\( \mathbb{Z}m \)</td><td>0</td><td>\( {\mathbb{Z}}_{\left( m, n\right) } \)</td></tr></table>

例如，

\[
\operatorname{Ext}\left( {{\mathbb{Z}}_{m},\mathbb{Z}}\right)  = {\mathbb{Z}}_{m},\;\operatorname{Tor}\left( {{\mathbb{Z}}_{m},{\mathbb{Z}}_{n}}\right)  = {\mathbb{Z}}_{\left( m, n\right) }.
\]

奇异同调

借助映射

\[
\left( {{x}_{1},{x}_{2},\ldots ,{x}_{n}}\right)  \mapsto  \left( {{x}_{1},{x}_{2},\ldots ,{x}_{n},0}\right) ,
\]

每个欧氏空间 \( {\mathbb{R}}^{n} \) 可自然包含在 \( {\mathbb{R}}^{n + 1} \) 中. 置

\[
{\mathbb{R}}^{\infty } = \mathop{\bigcup }\limits_{{n \geq  0}}{\mathbb{R}}^{n}
\]

记 \( {P}_{i} \) 是 \( {\mathbb{R}}^{\infty } \) 中第 \( i \) 个标准基向量，即它的第 \( i \) 个分量为 1，其他分量全为 0 . 记 \( {P}_{0} \) 为原点.

定义标准 \( q \) -单纯形 \( {\bigtriangleup }_{q} \) 为集合

\[
{\bigtriangleup }_{q} = \left\{  {\mathop{\sum }\limits_{{j = 0}}^{q}{t}_{j}{P}_{j} \mid  \mathop{\sum }\limits_{{j = 0}}^{q}{t}_{j} = 1,{t}_{j} \geq  0}\right\}  .
\]

若 \( X \) 是拓扑空间, \( X \) 中一个奇异 \( q \) -单纯形是连续映射 \( s : {\bigtriangleup }_{q} \rightarrow  X;X \) 中一个奇异 \( q \) -链 \( s \) 是奇异 \( q \) -单纯形的整系数的有限形式线性组合:

\[
s = \mathop{\sum }\limits_{{i = 1}}^{k}{n}_{i}{s}_{i}
\]

其中 \( {n}_{i} \in  \mathbb{Z},{s}_{i} \) 是奇异 \( q \) -单纯形.

\( X \) 中所有奇异 \( q \) -链形成一个 abel 群 \( {S}_{q}\left( X\right) \) ,称为 \( X \) 的奇异 \( q \) -链群. 记

\[
{S}_{ * }\left( X\right)  = { \oplus  }_{q \geq  0}{S}_{q}\left( X\right)
\]

为奇异链的分次群.

标准 \( q \) -单纯形的第 \( i \) 个面映射

\[
{\partial }_{q}^{i} : {\bigtriangleup }_{q - 1} \rightarrow  {\bigtriangleup }_{q}
\]

定义为

\[
{\partial }_{q}^{i}\left( {\mathop{\sum }\limits_{{j = 0}}^{{q - 1}}{t}_{j}{P}_{j}}\right)  = \mathop{\sum }\limits_{{j = 0}}^{{i - 1}}{t}_{j}{P}_{j} + \mathop{\sum }\limits_{{j = i + 1}}^{q}{t}_{j - 1}{P}_{j}
\]

它将标准 \( \left( {q - 1}\right) \) -单纯形映为标准 \( q \) -单纯形中第 \( i \) 个顶点所对应的面. 例如，

![bo_d7e85t491nqc73eqefm0_543_507_873_1267_727_0.jpg](images/fu_algebraic_topology_and_differential_forms_157_bod7e85t491nqc73eqefm054350787312677270.jpg)

定义边缘算子

\[
{\partial }_{q} : {S}_{q}\left( X\right)  \rightarrow  {S}_{q - 1}\left( X\right)
\]

\[
{\partial }_{q}s = \mathop{\sum }\limits_{{i = 0}}^{q}{\left( -1\right) }^{i}s \circ  {\partial }_{q}^{i}
\]

显然 \( {\partial }_{q - 1} \circ  {\partial }_{q} = 0 \) . 所以 \( \left\{  {{S}_{ * }\left( X\right) ,\partial }\right\} \) 是一个复形,它的同调是 \( X \) 的整系数奇异同调,记作 \( {H}_{ * }\left( X\right) \) 或 \( {H}_{ * }\left( {X;\mathbb{Z}}\right) \) :

\[
{H}_{q}\left( {X;\mathbb{Z}}\right)  = \ker {\partial }_{q}/\operatorname{im}{\partial }_{q + 1}.
\]

若在奇异 \( q \) -链的定义中组合系数 \( {n}_{i} \) 属于 abel 群 \( G \) ,我们就得到系数在群 \( G \) 的奇异同调, \( {H}_{ * }\left( {X;G}\right) \) . 例. 计算 \( {H}_{0}\left( X\right) \) .

定义奇异 0 -链 \( \sum {n}_{i}{P}_{i} \) 的度为 \( \sum {n}_{i} \) .

假定 \( X \) 是道路连通的. 若 \( - P \) 与 \( Q \) 在一个 0-链中,则任意从 \( P \) 到 \( Q \) 的道路是一个以 \( Q - P \) 为边缘的奇异 1-单纯形. 因此在道路连通空间中一个 0-链是一个 1-链的边缘当且仅当它的度是 0 . 所以有短正合序列

\[
0 \rightarrow  \operatorname{im}{\partial }_{1} \rightarrow  {S}_{0}\left( X\right) \xrightarrow[]{\deg }\mathbb{Z} \rightarrow  0
\]

由此可得

\[
{H}_{0}\left( X\right)  = \frac{{S}_{0}\left( X\right) }{\operatorname{im}{\partial }_{1}} \simeq  \frac{{S}_{0}\left( X\right) }{\ker \deg } \simeq  \mathbb{Z}.
\]

一般地, \( {H}_{0}\left( X\right) \) 是 \( X \) 的道路分支数个 \( \mathbb{Z} \) 的直和,直和对应于有限线性组合.

## 锥构造

这节的目的是计算 \( {H}_{ * }\left( {\mathbb{R}}^{n}\right) \) .

设 \( s : {\bigtriangleup }_{q} \rightarrow  {\mathbb{R}}^{n} \) 是 \( {\mathbb{R}}^{n} \) 中一个奇异 \( q \) -单纯形. 定义 \( s \) 上的锥为一个奇异 \( \left( {q + 1}\right) \) -单纯形 \( {Ks} : {\bigtriangleup }_{q + 1} \rightarrow  {\mathbb{R}}^{n} \) ,

\[
\left( {Ks}\right) \left( {\mathop{\sum }\limits_{{j = 0}}^{{q + 1}}{t}_{j}{P}_{j}}\right)  = \left\{  \begin{array}{ll} \left( {1 - {t}_{q + 1}}\right)  \cdot  s\left( {\mathop{\sum }\limits_{{j = 0}}^{q}\frac{{t}_{j}}{1 - {t}_{q + 1}}{P}_{j}}\right) & \;{t}_{q + 1} \neq  1 \\  0 & \;{t}_{q + 1} = 1. \end{array}\right.
\]

显然 \( {Ks} \) 在点 \( {P}_{q + 1} \) 处连续. 所以 \( {Ks} \) 连续. 直观上讲,这是 \( {\mathbb{R}}^{n} \) 中以 \( s \) 为底,以原点为顶点的锥. 为了理解这个公式, 我们把最后一个坐标 \( {t}_{q + 1} \) 看作“时间”; 当时间从 0 走到 1,锥 \( {Ks} \) 从 \( s \) 移动到原点.

例如当 \( q = 2 \) 时,奇异单纯形 \( s \) 如图所示,则锥 \( {Ks} \) 是一个 “多面体”.

\[
\left( {Ks}\right) \left( {P}_{0}\right)  = s\left( {P}_{0}\right) ,\;\left( {Ks}\right) \left( {P}_{1}\right)  = s\left( {P}_{1}\right) ,
\]

\[
\left( {Ks}\right) \left( {P}_{2}\right)  = s\left( {P}_{2}\right) ,\;\left( {Ks}\right) \left( {P}_{3}\right)  = O\text{ (原点). }
\]

\[
\partial {Ks} = 0\text{ th face - 1st face + 2nd face - }s\text{ , }
\]

\[
K\partial s = 0\text{ th face - 1st face + 2nd face. }
\]

![bo_d7e85t491nqc73eqefm0_547_716_212_923_780_0.jpg](images/fu_algebraic_topology_and_differential_forms_158_bod7e85t491nqc73eqefm05477162129237800.jpg)

所以

\[
\partial K - K\partial  =  - \mathrm{{id}}\text{ . }
\]

回到一般情形,将 \( K \) 线性延拓,得到锥构造 \( K : {S}_{q}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {S}_{q + 1}\left( {\mathbb{R}}^{n}\right) \) . 则有

命题 15.1. 当 \( q \geq  1 \) 时, \( \partial K - K\partial  = {\left( -1\right) }^{q + 1}\mathrm{{id}} : {S}_{q} \rightarrow  {S}_{q} \) .

证. 从上图来看几何思想是清楚的. 证明本身不难, 此处从略.

换句话说,当 \( q \geq  1 \) 时,锥构造 \( K \) 是 \( {S}_{q}\left( {\mathbb{R}}^{n}\right) \) 上恒等映射与零映射之间的同伦算子. 所以

\[
{H}_{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} 0 & q \geq  1 \\  \mathbb{Z} & q = 0. \end{array}\right.
\]

因为奇异同调是同伦不变量,所以若 \( X \) 是可缩空间,则 \( X \) 的奇异同调是

\[
{H}_{q}\left( X\right)  = \left\{  \begin{array}{ll} 0 & q \geq  1 \\  \mathbb{Z} & q = 0. \end{array}\right.
\]

当然也可直接证明,这需借助 \( X \) 到一点的收缩进行锥构造.

对奇异链的 MV 序列设 \( X \) 是拓扑空间, \( i : V \subset  U \) 是 \( X \) 中开集的包含. 则 \( i \) 诱导了一个自然映射

\[
{i}_{ * } : {S}_{q}\left( V\right)  \rightarrow  {S}_{q}\left( U\right)
\]

\[
{i}_{ * }\left( {\mathop{\sum }\limits_{{j = 1}}^{k}{n}_{j}{s}_{j}}\right)  = \mathop{\sum }\limits_{{j = 1}}^{k}{n}_{j}\left( {i \circ  {s}_{j}}\right)
\]

现设 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  J} \) 是 \( X \) 的开覆盖, \( J \) 是可数全序集. 包含序列

\[
X \leftarrow  \mathop{\coprod }\limits_{{\alpha }_{0}}{U}_{{\alpha }_{0}}\overset{ \leftarrow  }{ \leftarrow  }\mathop{\coprod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{U}_{{\alpha }_{0}{\alpha }_{1}}\overset{ \leftarrow  }{ \leftarrow  }\cdots
\]

诱导了一个 MV 序列

\[
0 \leftarrow  {S}_{q}\left( X\right)  \leftarrow  { \oplus  }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \leftarrow  }{ \oplus  }_{{\alpha }_{0} < {\alpha }_{1}}{S}_{q}\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \leftarrow  }\ldots
\]

需作以下几点说明.

(a) 由于技术上原因,为了证明序列在左端处是满射,需把 \( {S}_{q}\left( X\right) \) 改为 \( \mathcal{U} \) 一小的 \( q \) -链群 \( {S}_{q}^{\mathcal{U}}\left( X\right) \) .

\[
s = \sum {n}_{i}{s}_{i} \in  {S}_{q}^{\mathcal{U}}\left( X\right)  \Leftrightarrow  \text{ 对每个 }i,{s}_{i} : {\bigtriangleup }_{q} \rightarrow  {U}_{\alpha } \in  \mathcal{U}.
\]

包含映射

\[
i : {S}_{ * }^{\mathcal{U}}\left( X\right)  \rightarrow  {S}_{ * }\left( X\right)
\]

显然是链映射,即 \( i \circ  \partial  = \partial  \circ  i \) . 事实上它是一个链等价. 我们略去这个事实的繁琐证明,但它背后的想法是相当直观的: 为了得到一个逆链映射,重心重分 \( X \) 中每个链直到它变为 \( \mathcal{U} \) 一小的.

总之,为了计算 \( X \) 的奇异同调,只需用 \( \mathcal{U} \) 一小的链:

\[
{H}_{q}\left( X\right)  = {H}_{q}\left( {{S}_{ * }\left( X\right) }\right)  = {H}_{q}\left( {{S}_{ * }^{\mathcal{U}}\left( X\right) }\right) .
\]

However, for technical reasons which will become apparent in the proof of Proposition 15.2 (to show the surjectivity at one end of the Mayer-Vietoris sequence), we must consider here the group \( {S}_{ * }^{\mathcal{U}}\left( X\right) \) of \( \mathcal{U} \) -small chains in \( X \) ; these are chains made up of simplices each of which lies in some open set of the cover \( \mathcal{U} \) . The inclusion

\[
i : {S}_{ * }^{\mathcal{U}}\left( X\right)  \rightarrow  {S}_{ * }\left( X\right)
\]

is clearly a chain map, i.e., it commutes with the boundary operator \( \partial \) . Indeed, it is a chain equivalence. The proof of this fact is tedious and we will omit it (Vick [1, Appendix I, p. 207]), but the idea behind it is quite intuitive: to get an inverse chain map, subdivide each chain in \( X \) until it becomes \( \mathcal{U} \) -small. In any case the upshot is that to compute the singular homology of \( X \) it suffices to use \( \mathcal{U} \) -small chains: \( H\left( {{S}_{ * }\left( X\right) }\right)  = H\left( {{S}_{ * }^{\mathcal{U}}\left( X\right) }\right) \) .

(b) 用 “交错和公式” 定义 Čech 边缘算子

\[
\delta  : \mathop{\bigoplus }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{S}_{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  \mathop{\bigoplus }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p - 1}}}{S}_{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right)
\]

\[
{\left( \delta c\right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{c}_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

此处总是按惯例:交换 \( {c}_{{\alpha }_{0}{\alpha }_{1}\ldots {\alpha }_{p}} \) 中两个指标改变符号. 与命题 12.12 一样可证

\[
{\delta }^{2} = 0\text{ . }
\]

(c) 边缘算子 \( \delta  : {\bigoplus }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right)  \rightarrow  {S}_{q}^{\mathcal{U}}\left( X\right) \) 就是求和,记为 \( \varepsilon \) .

命题 15.2.(对奇异链的 MV 序列)以下序列是正合的.

\[
0 \leftarrow  {S}_{q}^{\mathcal{U}}\left( X\right) \overset{\varepsilon }{ \leftarrow  }{ \oplus  }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \leftarrow  }{ \oplus  }_{{\alpha }_{0} < {\alpha }_{1}}{S}_{q}\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \leftarrow  }\cdots .
\]

虽然这个序列看起来像对紧支集的广义 MV 序列, 即命题 12.12, 但是因为现在不能用单位分解, 所以不能用 (12.12) 的证明的第二部分.

证. 两个开子集的 MV 序列是

\[
0 \leftarrow  {S}_{q}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1}}\right) \overset{\operatorname{sum}}{ \leftarrow  }{S}_{q}\left( {U}_{0}\right)  \oplus  {S}_{q}\left( {U}_{1}\right) \overset{\delta }{ \leftarrow  }{S}_{q}\left( {U}_{01}\right)  \leftarrow  0
\]

\[
\left( {{c}_{10},{c}_{01}}\right) \; \leftarrow  \;{c}_{01}
\]

它的正合性直接从定义可得.

## 三个开子集的 MV 序列是

\[
0 \leftarrow  {S}_{q}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1} \cup  {U}_{2}}\right)  \leftarrow  {S}_{q}\left( {U}_{0}\right)  \oplus  {S}_{q}\left( {U}_{1}\right)  \oplus  {S}_{q}\left( {U}_{2}\right)  \leftarrow  {S}_{q}\left( {U}_{01}\right)  \oplus  {S}_{q}\left( {U}_{02}\right)  \oplus  {S}_{q}\left( {U}_{12}\right)  \leftarrow  {S}_{q}\left( {U}_{012}\right)  \leftarrow  0
\]

\[
\left( {{c}_{10} + {c}_{20},{c}_{01} + {c}_{21},{c}_{02} + {c}_{12}}\right)  \leftarrow  \;\left( {{c}_{01},{c}_{02},{c}_{12}}\right)
\]

\[
\left( {{c}_{201},{c}_{102},{c}_{012}}\right) \; \leftarrow  \;{c}_{012}
\]

把两个开集的 MV 序列插入三个开集的 MV 序列, 产生以下的列正合的交换图表:

![bo_d7e85t491nqc73eqefm0_554_52_267_2265_776_0.jpg](images/fu_algebraic_topology_and_differential_forms_160_bod7e85t491nqc73eqefm05545226722657760.jpg)

\( \mathcal{U} \) 在 \( {S}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1}}\right) \) 中是开覆盖 \( \left\{  {{U}_{0},{U}_{1}}\right\} \) ,而 \( \mathcal{U} \) 在 \( {S}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1} \cup  {U}_{2}}\right) \) 中是开覆盖 \( \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) . 所以群

\[
\frac{{S}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1} \cup  {U}_{2}}\right) }{{S}^{\mathcal{U}}\left( {{U}_{0} \cup  {U}_{1}}\right) }
\]

是由落在 \( {U}_{2} \) 中但不完全落在 \( {U}_{0} \) 或 \( {U}_{1} \) 中的单纯形生成. 见下图.

![bo_d7e85t491nqc73eqefm0_555_525_176_1253_728_0.jpg](images/fu_algebraic_topology_and_differential_forms_161_bod7e85t491nqc73eqefm055552517612537280.jpg)

现证交换图表中行的正合性. 底下一行几乎是开覆盖 \( \left\{  {{U}_{02},{U}_{12}}\right\} \) 的 MV 序列,除了在 \( S\left( {U}_{2}\right) \) 处的正合性需证明外在其余位置处的正合性是显然的. 显然 \( \beta  \circ  \delta  = 0 \) . 现若 \( c \in  S\left( {U}_{2}\right) \) 并且 \( \beta \left( c\right)  = 0 \) ,则 \( c \) 是 \( {U}_{2} \) 中的链且它的每个单纯形落在 \( {U}_{0} \) 或 \( {U}_{1} \) 中,即 \( c \in  \operatorname{im}\delta \) . 因此底下一行是正合的.

交换图表的每行是一个复形而交换图表可视为复形的短正合序列. 因为顶上一行的复形与底下一行的复形是正合的, 即它们是零调的, 由以下引理 15.3 知中间一行的复形也是零调的，即中间一行是正合的. 这就证明了对三个开集组成的开覆盖，MV 序列是正合的. 一般地,把 \( r \) 个开集的 MV 序列插入 \( \left( {r + 1}\right) \) 个开集的 MV 序列,再用上述技巧与归纳法不难证明有限开覆盖的 MV 序列是正合的.

现考虑可数开覆盖 \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) . 由直和的定义, \( \bigoplus S\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) 的一个元 \( c \) 仅有有限多个分量不等于零. 这些分量只涉及有限多个开集. 因此若 \( {\delta c} = 0 \) ,根据有限开覆盖的 MV 序列的正合性,存在 \( b \in  \bigoplus S\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}\right) \) 使得 \( c = {\delta b} \) . 这就证明了可数多个开集的 MV 序列的正合性.

引理 15.3. 设

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0
\]

是复形的短正合序列. 若三个复形中两个零调, 则第三个也零调.

证. 考虑同调的长正合序列

\[
\cdots  \rightarrow  {H}_{q}\left( A\right)  \rightarrow  {H}_{q}\left( B\right)  \rightarrow  {H}_{q}\left( C\right)  \rightarrow  {H}_{q - 1}\left( A\right)  \rightarrow  \ldots
\]

注记 15.4. 命题 15.2 的证明可逐字逐句照搬到系数在任一 abel 群 \( G \) 的情形. 现假定开覆盖 \( \mathcal{U} \) 由两个开集 \( U \) , \( V \) 组成. 根据命题 15.2,有奇异链的短正合序列

(15.5)

\[
0 \rightarrow  {S}_{q}\left( {U \cap  V}\right)  \rightarrow  {S}_{q}\left( U\right)  \oplus  {S}_{q}\left( V\right)  \rightarrow  {S}_{q}^{\mathcal{U}}\left( X\right)  \rightarrow  0.
\]

同调中相伴的长正合序列是通常的同调 MV 序列.

推论 15.6. (对两个开集的同调 MV 序列) 设 \( X = U \cup  V \) 是两个开集的并. 则存在同调的长正合序列

\[
\cdots  \rightarrow  {H}_{q}\left( {U \cap  V}\right) \overset{f}{ \rightarrow  }{H}_{q}\left( U\right)  \oplus  {H}_{q}\left( V\right) \overset{g}{ \rightarrow  }{H}_{q}\left( X\right)  \rightarrow  {H}_{q - 1}\left( {U \cap  V}\right)  \rightarrow  \cdots
\]

其中映射 \( f \) 由带符号的包含 \( a \mapsto  \left( {-a, a}\right) \) 诱导, \( g \) 是求和 \( \left( {a, b}\right)  \mapsto  a + b \) .

作业:

1. 练习 14.17.3.

2. 练习 14.17.4.

3. 练习 15.13.4.

4. 计算 \( {H}_{ * }\left( {{S}^{m} \vee  {S}^{n}}\right) \) .
