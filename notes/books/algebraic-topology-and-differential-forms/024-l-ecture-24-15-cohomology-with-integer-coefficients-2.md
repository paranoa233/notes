#### 24. 奇异上同调

# 代数拓扑与微分形式 §15 Cohomology with Integer Coefficients (2)

24. 奇异上同调

上次课讲了拓扑空间 \( X \) 的整系数奇异同调 \( {H}_{ * }\left( X\right) \) 的定义,计算了可缩空间的奇异同调, 并证明了可数开覆盖的奇异链的 MV 序列是正合的. 特别地, 两个开集的奇异链的 MV 序列诱导了同调的长正合序列. 由此可计算一些拓扑空间如 \( m \) 维球面 \( {S}^{m} \) ,两个球面的楔积 \( {S}^{m} \vee  {S}^{n} \) 的整系数奇异同调.

这次课讲整系数的奇异上同调. 用函子 Hom( \( ,\mathbb{Z} \) ) 应用到奇异链的 MV 序列,得到奇异上链的 MV 序列,并由此建立双复形 \( \{ {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) ,{\delta }^{ * }, d\} \) . 于是可对此双复形按 Cech-de Rham 双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 的路数重新走一遍,弄清哪些结果是可推广的, 哪些结果是不能推广的, 特别地得到奇异上同调的 Leray 定理. 最后讲同调谱序列.

- 整系数的奇异上同调

- 奇异上链的 MV 序列

- 奇异上同调的 Leray 定理

- 同调谱序列

整系数的奇异上同调

设 \( X \) 是拓扑空间. \( X \) 上一个奇异 \( q \) -上链是奇异 \( q \) -链的 \( \mathbb{Z} \) -模 \( {S}_{q}\left( X\right) \) 上一个线性泛函. 这样,奇异 \( q \) -上链群为

\[
{S}^{q}\left( X\right)  = \operatorname{Hom}\left( {{S}_{q}\left( X\right) ,\mathbb{Z}}\right) ;
\]

奇异上链分次群为

\[
{S}^{ * }\left( X\right)  = { \oplus  }_{q \geq  0}{S}^{q}\left( X\right)
\]

定义上边缘算子 \( d : {S}^{q}\left( X\right)  \rightarrow  {S}^{q + 1}\left( X\right) \) 为边缘算子 \( \partial \) 的伴随:

\[
\left( {d\omega }\right) \left( c\right)  = \omega \left( {\partial c}\right) .
\]

由 \( {\partial }^{2} = 0 \) 可得 \( {d}^{2} = 0 \) . 所以 \( \left\{  {{S}^{ * }\left( X\right) , d}\right\} \) 是一个复形. 这个复形的上同调是 \( X \) 的整系数奇异上同调,记为 \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) 或 \( {H}^{ * }\left( X\right) \) .

若把整数群 \( \mathbb{Z} \) 换成 abel 群 \( G \) ,则有系数在 \( G \) 中的奇异上同调 \( {H}^{ * }\left( {X;G}\right) \) .

以下约定几个上同调的记号:

\( {H}^{ * }\left( X\right) \) : 拓扑空间 \( X \) 的整系数奇异上同调;

\( {H}_{dR}^{ * }\left( M\right) \) : 流形 \( M \) 的 de Rham 上同调;

\( {H}^{ * }\left( {X,\mathbb{Z}}\right) \) : 拓扑空间 \( X \) 的常值预层 \( \mathbb{Z} \) 的 Čech 上同调.

例. 计算 \( {H}^{0}\left( X\right) \) . 设 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{0}\left( X\right) \) . 则 \( \omega  \in  {S}^{0}\left( X\right) \) 且 \( {d\omega } = 0 \) . 这就是说 \( \omega  : {S}_{0}\left( X\right)  \rightarrow  \mathbb{Z} \) 并且对任意 \( c \in  {S}_{1}\left( X\right) ,\omega \left( {\partial c}\right)  = 0 \) ; 即 \( \omega \) 在 \( X \) 的每个道路分支上是常值函数. 因此, \( {H}^{0}\left( X\right) \) 是道路分支数个 \( \mathbb{Z} \) 的直积:

\[
{H}^{0}\left( X\right)  = \underset{\text{ 道路分支数 }}{\underbrace{\mathbb{Z} \times  \mathbb{Z} \times  \cdots  \times  \mathbb{Z}}}.
\]

此处道路分支数可能是无限的.

注. 奇异上同调与 Čech 上同调不总是相等的. 例如,

\[
\dim {H}^{0}\left( X\right)  = X\text{ 的道路分支数, }
\]

\[
\dim {H}^{0}\left( {X,\mathbb{Z}}\right)  = X\text{ 的连通分支数. }
\]

例. 计算 \( {H}^{ * }\left( {\mathbb{R}}^{n}\right) \) . 定义锥构造 \( K \) 的伴随算子

\[
L : {S}^{q}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {S}^{q - 1}\left( {\mathbb{R}}^{n}\right)
\]

如下. 对任意 \( \sigma  \in  {S}^{q}\left( {\mathbb{R}}^{n}\right) \) 与 \( c \in  {S}_{q - 1}\left( {\mathbb{R}}^{n}\right) \) ,

\[
\left( {L\sigma }\right) \left( c\right)  = \sigma \left( {Kc}\right) .
\]

则由 \( \partial K - K\partial  = {\left( -1\right) }^{q + 1}\mathrm{\;{id}} \) 容易验证: 对 \( q \geq  1 \) ,在 \( {S}^{q}\left( {\mathbb{R}}^{n}\right) \) 上

\[
{dL} - {Ld} = {\left( -1\right) }^{q + 1}\mathrm{{id}}.
\]

所以

\[
{H}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & q = 0 \\  0 & q \neq  0. \end{array}\right.
\]

应用函子 \( \operatorname{Hom}\left( {,\mathbb{Z}}\right) \) 到对奇异链的 MV 序列

\[
0 \leftarrow  {S}_{q}^{\mathcal{U}}\left( X\right) \overset{\varepsilon }{ \leftarrow  }{ \oplus  }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \leftarrow  }{ \oplus  }_{{\alpha }_{0} < {\alpha }_{1}}{S}_{q}\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \leftarrow  }\ldots
\]

得到对奇异上链的 MV 序列

(15.7)

\[
0 \rightarrow  {S}_{\mathcal{U}}^{q}\left( X\right) \overset{{\varepsilon }^{ * }}{ \rightarrow  }\mathop{\prod }\limits_{{\alpha }_{0}}{S}^{q}\left( {U}_{{\alpha }_{0}}\right) \overset{{\delta }^{ * }}{ \rightarrow  }\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{S}^{q}\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{{\delta }^{ * }}{ \rightarrow  }\ldots
\]

其中

\[
{S}_{\mathcal{U}}^{q}\left( X\right)  = \operatorname{Hom}\left( {{S}_{q}^{\mathcal{U}}\left( X\right) ,\mathbb{Z}}\right)
\]

\[
\mathop{\prod }\limits_{{\alpha }_{0}}{S}^{q}\left( {U}_{{\alpha }_{0}}\right)  = \mathop{\prod }\limits_{{\alpha }_{0}}\operatorname{Hom}\left( {{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right)
\]

\[
\overset{ \sim  }{\underset{t}{ \rightarrow  }}\operatorname{Hom}\left( {{\bigoplus }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right)
\]

...

由练习 14.17.3 知函子 Hom( \( ,\mathbb{Z} \) ) 把自由 \( \mathbb{Z} \) -模的正合序列映为正合序列,所以 (15.7) 是正合的. 回忆同构 \( t \) . 对任意的

\[
\omega  = \left( {{\omega }_{{\alpha }_{0}},{\omega }_{{\alpha }_{1}},\ldots }\right)  \in  \mathop{\prod }\limits_{{\alpha }_{0}}\operatorname{Hom}\left( {{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right) ,
\]

存在唯一的

\[
\widetilde{\omega } \in  \operatorname{Hom}\left( {{\bigoplus }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right)
\]

使得对包含 \( {\iota }_{{\alpha }_{0}} : {S}_{ * }\left( {U}_{{\alpha }_{0}}\right)  \rightarrow  { \oplus  }_{{\alpha }_{0}}{S}_{ * }\left( {U}_{{\alpha }_{0}}\right) \) ,

\[
{\omega }_{{\alpha }_{0}} = \widetilde{\omega } \circ  {\iota }_{{\alpha }_{0}};
\]

反之,对任意的 \( \widetilde{\omega } \in  \operatorname{Hom}\left( {{ \oplus  }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right) \) ,令 \( {\omega }_{{\alpha }_{0}} = \widetilde{\omega } \circ  {\iota }_{{\alpha }_{0}} \) . 则

\[
\omega  = \left( {{\omega }_{{\alpha }_{0}},{\omega }_{{\alpha }_{1}},\ldots }\right)  \in  \mathop{\prod }\limits_{{\alpha }_{0}}\operatorname{Hom}\left( {{S}_{q}\left( {U}_{{\alpha }_{0}}\right) ,\mathbb{Z}}\right) .
\]

练习 15.7.1. 证明 \( {\varepsilon }^{ * } \) 是限制映射,而 \( {\delta }^{ * } \) 为交错和

\[
{\left( {\delta }^{ * }\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = {\sum }_{i = 0}^{p + 1}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}}.
\]

一旦有了 MV 序列 (15.7),就可建立双复形 \( \left\{  {{C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) ,{\delta }^{ * }, d}\right\} \) .

(a) 用双复形 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 计算 \( {H}^{ * }\left( X\right) \) .

这与 de Rham 理论相同. 因为根据 MV 序列 (15.7) 的正合性, 这个双复形的 \( {H}_{{\delta }^{ * }} \) 仅有一列不等于零

![bo_d7e85t491nqc73eqefm0_566_557_523_1163_886_0.jpg](images/fu_algebraic_topology_and_differential_forms_162_bod7e85t491nqc73eqefm056655752311638860.jpg)

所以谱序列在 \( {E}_{2} \) 页退化且

\[
H\left\{  {{C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) }\right\}   = {H}_{d}{H}_{{\delta }^{ * }} = {H}^{ * }\left( X\right) .
\]

(b) 用双复形 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 计算 \( {H}^{ * }\left( {X,\mathbb{Z}}\right) \) .

此时要求 \( X \) 具有好覆盖. \( X \) 是具有好覆盖的若它具有一个三角剖分,即与一个单纯复形 \( K \) 的支撑 \( \left| K\right| \) 同胚，因为三角剖分的所有顶点的开星形构成一个好覆盖. 通过对三角剖分的不断重心重分，我们可无限地加细星形. 因此，正如流形的情形，可三角剖分的空间 \( X \) 的任意开覆盖一定有一个好覆盖的加细. 这顺便给出了流形具有好覆盖的另一证明, 因为流形是可三角剖分的.

"To complete the analogy we will need the existence of a good cover on the topological space \( X \) . This presents no problem if \( X \) admits a triangulation, i.e., a homeomorphism with the support of a simplicial complex, since the open stars of the vertices of the triangulation form a good cover. By taking barycentric subdivisions of the triangulation we can refine its star ad infinitum. Hence just as in the case of manifolds, the good covers on a triangularizable space \( X \) are cofinal in the set of all covers of \( X \) . We note in passing that this gives an alternative proof of the existence of a good cover on a manifold since it is known that every manifold admits a triangulation."

若 \( \mathcal{U} \) 是 \( X \) 的好覆盖,则双复形 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 的上同调 \( {H}_{d} \) 是

\[
{H}^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & q = 0 \\  0 & q > 0. \end{array}\right.
\]

\[
\left| \begin{matrix}  \\   \\  0 \\   \\  {C}^{0}\left( {\mathcal{U},\mathbb{Z}}\right)  \end{matrix}\right|  \leq  \left| \begin{matrix}  \\   \\  0 \\   \\  {C}^{1}\left( {\mathcal{U},\mathbb{Z}}\right)  \end{matrix}\right|  \leq  {C}^{1}\left( {\mathcal{U},\mathbb{Z}}\right)  \leq  {C}^{2}\left( {\mathcal{U},\mathbb{Z}}\right)
\]

由练习 15.7.1 知此时 \( {\delta }^{ * } \) 就是在 Čech 上同调中的 \( \delta \) . 所以

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{Z}}\right)  = {H}_{\delta }{H}_{d} = H\left\{  {{C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) }\right\}  .
\]

(c) 所以在奇异上同调与好覆盖的系数在常值预层 \( \mathbb{Z} \) 的 Čech 上同调之间存在同构

\[
{H}^{ * }\left( X\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{Z}}\right) .
\]

假定 \( X \) 是可三角剖分的空间. 因为 \( X \) 的任意开覆盖可被好覆盖加细,所以

\[
{H}^{ * }\left( {X,\mathbb{Z}}\right)  = {H}^{ * }\left( {\mathcal{U},\mathbb{Z}}\right) .
\]

因此有

定理 15.8. 可三角剖分的空间 \( X \) 的奇异上同调同构于系数在常值预层 \( \mathbb{Z} \) 的 Čech 上同调. 若 \( \mathcal{U} \) 是 \( X \) 的好覆盖,则

\[
{H}^{ * }\left( X\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{Z}}\right)  \simeq  {H}^{ * }\left( {X,\mathbb{Z}}\right) .
\]

对奇异上同调的 Leray 定理

设 \( X \) 是可三角剖分的空间, \( \mathcal{U} \) 是其好覆盖. 设 \( \pi  : E \rightarrow  X \) 是以 \( F \) 为纤维的纤维丛.

首先,与定理 14.18 相同,从 \( E \) 上双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{S}^{ * }}\right) \) 出发可得到收敛于奇异上同调 \( {H}^{ * }\left( E\right) \) 的谱序列,它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( F\right) }\right) ,
\]

其中 \( {\mathcal{H}}^{q}\left( F\right) \) 是 \( \mathcal{U} \) 上局部常值预层

\[
{\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{q}\left( {U \times  F}\right)  \simeq  {H}^{q}\left( F\right) .
\]

若 \( {\mathcal{H}}^{q}\left( F\right) \) 是 \( \mathcal{U} \) 上常值预层 \( {H}^{q}\left( F\right) \) 且是有限生成的自由 \( \mathbb{Z} \) -模: \( \mathbb{Z} \oplus  \cdots  \oplus  \mathbb{Z} \) ,则

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},\underset{{h}^{q}\left( F\right) }{\underbrace{\mathbb{Z}) \oplus  \cdots  \oplus  {H}^{p}}}\left( {\mathcal{U},\mathbb{Z}}\right) }\right)
\]

\[
= {H}^{p}\left( X\right)  \oplus  \cdots  \oplus  {H}^{p}\left( X\right)
\]

\[
= {H}^{p}\left( X\right)  \otimes  {H}^{q}\left( F\right) .
\]

其次,在奇异上同调 \( {H}^{ * }\left( X\right) \) 上定义乘积结构.

设 \( {c}_{{01}\cdots q + s} : {\bigtriangleup }_{q + s} \rightarrow  X \) 是 \( X \) 中一个奇异 \( \left( {q + s}\right) \) -单纯形. 它的前 \( q \) -面 \( {c}_{{01}\cdots q} : {\bigtriangleup }_{q} \rightarrow  X \) 是由 \( {c}_{{01}\cdots q + s} \) 限制到 \( {\bigtriangleup }_{q + s} \) 的前 \( q \) -面 \( {\bigtriangleup }_{0\cdots q} \) 得到,后 \( s \) -面 \( {c}_{q\cdots q + s} : {\bigtriangleup }_{s} \rightarrow  X \) 是由 \( {c}_{{01}\cdots q + s} \) 限制到 \( {\bigtriangleup }_{q + s} \) 的后 \( s \) -面 \( {\bigtriangleup }_{q\cdots q + s} \) 得到.

对 \( \omega  \in  {S}^{q}\left( X\right) ,\eta  \in  {S}^{s}\left( X\right) \) ,定义 \( \omega \) 与 \( \eta \) 的杯积 (cup product)

\[
\omega  \cup  \eta  \in  {S}^{q + s}\left( X\right)
\]

如下. 对奇异 \( q + s \) -单纯形 \( {c}_{{01}\cdots q + s} \in  {S}_{q + s}\left( X\right) \) ,定义

(15.9)

\[
\left( {\omega  \cup  \eta }\right) \left( {c}_{{01}\cdots q + s}\right)  = \omega \left( {c}_{{01}\cdots q}\right) \eta \left( {c}_{q\cdots q + s}\right) ,
\]

其中右边表示两个整数相乘；再作线性扩张.

练习 15.10. 证明上边缘算子 \( d \) 相对于杯积是反导子:

\[
d\left( {\omega  \cup  \eta }\right)  = {d\omega } \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {d\eta }.
\]

所以杯积定义了奇异上同调 \( {H}^{ * }\left( X\right) \) 的一个乘积结构:

\[
\cup   : {H}^{q}\left( X\right)  \otimes  {H}^{s}\left( X\right)  \rightarrow  {H}^{q + s}\left( X\right)
\]

\[
\left( {\left\lbrack  \omega \right\rbrack  ,\left\lbrack  \eta \right\rbrack  }\right) \; \mapsto  \;\left\lbrack  {\omega  \cup  \eta }\right\rbrack
\]

最后,在 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 上定义杯积 \( \cup \) .

对 \( \omega  \in  {C}^{p}\left( {\mathcal{U},{S}^{q}}\right) ,\eta  \in  {C}^{r}\left( {\mathcal{U},{S}^{s}}\right) \) ,定义 \( \omega \) 与 \( \eta \) 的杯积

\[
\omega  \cup  \eta  \in  {C}^{p + r}\left( {\mathcal{U},{S}^{q + s}}\right)
\]

如下. 对 \( {c}_{{01}\cdots q + s} \in  {S}_{q + s}\left( {U}_{{\alpha }_{0}\cdots {\alpha }_{p + r}}\right) \) ,

\[
{\left( \omega  \cup  \eta \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + r}}\left( {c}_{{01}\cdots q + s}\right)  = {\left( -1\right) }^{qr}{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}}\left( {c}_{{01}\cdots q}\right)  \cdot  {\eta }_{{\alpha }_{p}\ldots {\alpha }_{p + r}}\left( {c}_{q\cdots q + s}\right) . \tag{55}
\]

可验证 \( d \) , \( {\delta }^{ * } \) 是反导子. 所以这个乘积结构诱导了 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 的谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) 的乘积结构并且 \( {d}_{r} \) 对此乘积结构是反导子. 我们要把上述系数在整数群 \( \mathbb{Z} \) 的理论推广到系数在交换环 \( A \) 的情形.

设 \( A \) 是交换环. 我们有系数在 \( A \) 的奇异上同调 \( {H}^{ * }\left( {X;A}\right) \) . 应用函子 \( \operatorname{Hom}\left( {\cdot , A}\right) \) 到奇异链的 MV 序列 (15.2) 得到系数在 \( A \) 的奇异上链的 MV 序列; 然后得到系数在 \( A \) 的 Čech-奇异复形 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 与它的谱序列. 在杯积的定义 (15.9) 中用交换环乘法 “.” 代替普通整数乘法, 这样就在上述这些对象上定义了相应的乘积结构. 因此对系数在 \( A \) 的奇异上同调的谱序列结果还是成立的. 但对纤维丛的谱序列需多说几句.

设 \( \pi  : E \rightarrow  X \) 是以 \( F \) 为纤维的纤维丛, \( \mathcal{U} \) 是 \( X \) 的开覆盖. 则有 \( E \) 上系数在 \( A \) 的双复形 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{S}^{ * }}\right) \) ,于是就有谱序列,它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( {F;A}\right) }\right) ,
\]

其中 \( {\mathcal{H}}^{q}\left( {F;A}\right) \) 是 \( \mathcal{U} \) 上预层: 对 \( U \in  \operatorname{Open}\mathcal{U} \) ,

\[
{\mathcal{H}}^{q}\left( {F;A}\right) \left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) ;A}\right) .
\]

若 \( \mathcal{U} \) 是好覆盖，则 \( {\mathcal{H}}^{q}\left( {F;A}\right) \) 是局部常值预层；并且若 \( X \) 是单连通的，则 \( {\mathcal{H}}^{q}\left( {F;A}\right) \) 是常值预层 \( {H}^{q}\left( {F;A}\right) \) . 因此,

\[
{E}_{2}^{p, q} = {H}^{p}\left( {X;{H}^{q}\left( {F;A}\right) }\right) .
\]

此时,若 \( {H}^{ * }\left( {F;A}\right) \) 是有限生成的自由 \( A \) -模: \( A \oplus  \cdots  \oplus  A \) ,则

\[
{E}_{2}^{p, q} = {H}^{p}\left( {X;A}\right) { \otimes  }_{A}{H}^{q}\left( {F;A}\right) .
\]

综上所述，以下定理成立.

定理 15.11. (对系数在交换环 \( A \) 的奇异上同调的 Leray 定理) 设 \( \pi  : E \rightarrow  X \) 是拓扑空间 \( X \) 上以 \( F \) 为纤维的纤维丛, \( \mathcal{U} \) 是 \( X \) 的开覆盖. 则存在一个收敛于 \( {H}^{ * }\left( {E;A}\right) \) 的谱序列,它的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathcal{U},{\mathcal{H}}^{q}\left( {F;A}\right) }\right) .
\]

谱序列中每个 \( {E}_{r} \) 能给一个乘积结构使得微分 \( {d}_{r} \) 对此乘积结构是反导子. 若 \( X \) 是单连通的且有好覆盖, 则

\[
{E}_{2}^{p, q} = {H}^{p}\left( {X,{H}^{q}\left( {F;A}\right) }\right) .
\]

另若 \( {H}^{ * }\left( {F;A}\right) \) 是有限生成的自由 \( A \) -模，则作为 \( A \) 上代数

\[
{E}_{2} = {H}^{ * }\left( {X;A}\right)  \otimes  {H}^{ * }\left( {F;A}\right) .
\]

练习 15.12.(关于奇异上同调的 Künneth 公式)若 \( X \) 是具有好覆盖的拓扑空间,如可三角剖分的空间, \( Y \) 是任意拓扑空间,应用纤维丛 \( \pi  : X \times  Y \rightarrow  X \) 的谱序列证明

\[
{H}^{n}\left( {X \times  Y}\right)  = { \oplus  }_{p + q = n}{H}^{p}\left( {X,{H}^{q}\left( Y\right) }\right) .
\]

我们检查如何把 de Rham 理论中一些定理搬到奇异理论. 用奇异复形 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 代替 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) ,第 5 节的 MV 方法与第 9 节的 tic-tac-toe 证明对整系数奇异上同调的 Leray-Hirsch 定理都通得过. 然而,因为在 \( {H}^{q}\left( F\right) \) 中可能有挠元,关于整系数上同调形如 \( {H}^{ * }\left( {M \times  F}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) 的 Künneth 公式不成立; MV 方法行不通是因为与 \( {H}^{ * }\left( F\right) \) 作张量积不一定保持正合性, tic-tac-toe 证明也行不通是因为 \( {H}^{ * }\left( F\right)  \otimes  {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 不一定是有限多个 \( {C}^{ * }\left( {\mathcal{U},{S}^{ * }}\right) \) 的拷贝的直和. 这些困难在 Leray-Hirsch 定理中不会产生,因为它本身要假定纤维的上同调 \( {H}^{ * }\left( F\right) \) 是自由 \( \mathbb{Z} \) -模.

应用 Ext, Tor 这些完全代数的函子可得奇异理论依赖它的系数群的以下描述. 定理 15.14. (泛系数定理) 对任意空间 \( X \) 与 abel 群 \( G \) , (a) \( X \) 的系数在 \( G \) 的同调有分裂:

\[
{H}_{q}\left( {X;G}\right)  \simeq  {H}_{q}\left( X\right)  \otimes  G \oplus  \operatorname{Tor}\left( {{H}_{q - 1}\left( X\right) , G}\right) ;
\]

(b) \( X \) 的系数在 \( G \) 的上同调也有分裂:

\[
{H}^{q}\left( {X;G}\right)  \simeq  \operatorname{Hom}\left( {{H}_{q}\left( X\right) , G}\right)  \oplus  \operatorname{Ext}\left( {{H}_{q - 1}\left( X\right) , G}\right) .
\]

应用 \( \left( \mathrm{b}\right) \) 到 \( G = \mathbb{Z} \) ,再根据练习15.13.4有

推论 15.14.1. 对任意空间 \( X \) ,若 \( {H}_{q}\left( X\right) \) 与 \( {H}_{q - 1}\left( X\right) \) 是有限生成的 \( \mathbb{Z} \) -模,则

\[
{H}^{q}\left( X\right)  \simeq  {F}_{q} \oplus  {T}_{q - 1},
\]

其中 \( {F}_{q} \) 是 \( {H}_{q}\left( X\right) \) 的自由部分, \( {T}_{q - 1} \) 是 \( {H}_{q - 1}\left( X\right) \) 的挠部.

例 15.15. (球面的单位切丛的奇异上同调) \( {\mathbb{R}}^{3} \) 中单位球面 \( {S}^{2} \) 的单位切丛是 \( {S}^{2} \) 上以 \( {S}^{1} \) 为纤维的纤维丛

![bo_d7e85t491nqc73eqefm0_578_912_321_496_309_0.jpg](images/fu_algebraic_topology_and_differential_forms_164_bod7e85t491nqc73eqefm05789123214963090.jpg)

由于 \( {S}^{2} \) 单连通,由奇异上同调的 Leray 定理 (15.11) 知谱序列的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {S}^{2}\right)  \otimes  {H}^{q}\left( {S}^{1}\right) .
\]

![bo_d7e85t491nqc73eqefm0_578_610_945_1129_594_0.jpg](images/fu_algebraic_topology_and_differential_forms_163_bod7e85t491nqc73eqefm057861094511295940.jpg)

考虑到维数的原因, \( {d}_{3} = {d}_{4} = \cdots  = 0 \) . 所以 \( {E}_{3} = {E}_{\infty } \) .

根据注记 14.20,上图中微分 \( {d}_{2} \) 定义了圆周丛 \( S\left( {T{S}^{2}}\right) \) 的欧拉类. 因为 \( S\left( {T{S}^{2}}\right) \) 的欧拉类是 \( {H}^{2}\left( {S}^{2}\right) \) 生成元的 2 倍，所以这个微分 \( {d}_{2} \) 是乘以 2 . 于是

\[
{E}_{\infty }^{p, q} = \left\{  \begin{array}{ll} \mathbb{Z} & \left( {p, q}\right)  = \left( {0,0}\right) ,\left( {2,1}\right) \\  {\mathbb{Z}}_{2} & \left( {p, q}\right)  = \left( {2,0}\right) \\  0 & \left( {p, q}\right)  = \text{ 其余情形. } \end{array}\right.
\]

又因为 \( G{H}^{n} = { \oplus  }_{p + q = n}{E}_{\infty }^{p, q} \) ,并且考虑到其中最多只有一个 \( {E}_{\infty }^{p, q} \) 不为零,所以

\[
{H}^{ * }\left( {S\left( {T{S}^{2}}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} &  *  = 0,3 \\  {\mathbb{Z}}_{2} &  *  = 2 \\  0 &  *  = \text{ 其余情形 } \end{array}\right.
\]

练习 15.15.1. 计算单位切丛 \( S\left( {T{S}^{n}}\right) \) 的上同调.

注记 15.15.2. \( S\left( {T{S}^{2}}\right) \) 与 \( {SO}\left( 3\right) \) 微分同胚， \( {SO}\left( 3\right) \) 与 \( \mathbb{R}{P}^{3} \) 微分同胚.

练习 15.16. ( \( {SO}\left( 4\right) \) 的上同调) 特殊正交群 \( {SO}\left( n\right) \) 可迁作用在 \( {\mathbb{R}}^{n} \) 的单位球面 \( {S}^{n - 1} \) 上并且保持一点不变的子群是 \( {SO}\left( {n - 1}\right) \) . 因此 \( {S}^{n - 1} = {SO}\left( n\right) /{SO}\left( {n - 1}\right) \) . 由李群理论知若 \( H \) 是李群 \( G \) 的闭子群,则 \( \pi  : G \rightarrow  G/H \) 是纤维为 \( H \) 的纤维丛. 应用纤维丛

![bo_d7e85t491nqc73eqefm0_580_887_520_555_302_0.jpg](images/fu_algebraic_topology_and_differential_forms_166_bod7e85t491nqc73eqefm05808875205553020.jpg)

的谱序列计算 \( {SO}\left( 4\right) \) 的上同调.

练习 15.17.(酉群的上同调)酉群 \( U\left( n\right) \) 可迁作用在 \( {\mathbb{C}}^{n} \) 的单位球面 \( {S}^{{2n} - 1} \) 上并且保持一点不变的子群是 \( U\left( {n - 1}\right) \) . 因此 \( U\left( n\right) /U\left( {n - 1}\right)  = {S}^{{2n} - 1} \) . 应用纤维丛

![bo_d7e85t491nqc73eqefm0_580_850_1206_624_306_0.jpg](images/fu_algebraic_topology_and_differential_forms_165_bod7e85t491nqc73eqefm058085012066243060.jpg)

的谱序列计算 \( U\left( n\right) \) 的上同调.

## 同调谱序列

虽然本书主要涉及上同调, 但是为了应用到同伦论, 使用纤维化的同调谱序列常常会体现出方便. 因为这种谱序列构造类似于对上同调的谱序列构造, 所以讨论被简化.

应用奇异链函子 \( {S}_{ * } \) 代替微分形式函子 \( {\Omega }^{ * } \) ，得到一个双复形 \( {C}_{ * }\left( {\mathcal{U},{S}_{ * }}\right) \) ，它有微分算子 \( \partial \) 与 \( \delta \) . 定义 \( D = \delta  + {\left( -1\right) }^{p}\partial \) .

![bo_d7e85t491nqc73eqefm0_581_769_915_876_567_0.jpg](images/fu_algebraic_topology_and_differential_forms_167_bod7e85t491nqc73eqefm05817699158765670.jpg)

与第 14 节相同,这个双复形产生一个收敛于全同调 \( {H}_{D}\left\{  {{C}_{ * }\left( {\mathcal{U},{S}_{ * }}\right) }\right\} \) 的谱序列 \( \left\{  {E}^{r}\right\} \) . 考虑到箭头 \( \partial \) 与 \( \delta \) 的方向,微分 \( {d}^{r} \) 的方向与上同调谱序列的微分的方向相反；更精确地说，

\[
{d}^{r} : {E}_{p, q}^{r} \rightarrow  {E}_{p - r, q + r - 1}^{r}.
\]

根据奇异链的 MV 序列 (15.2) 的正合性,谱序列在 \( {E}^{2} \) 页退化且

\[
{E}^{2} = {H}_{\partial }{H}_{\delta } = {H}_{ * }\left( X\right) .
\]

命题 15.18. 对拓扑空间 \( X \) 的任意覆盖 \( \mathcal{U} \) ,双复形 \( {C}_{ * }\left( {\mathcal{U},{S}_{ * }}\right) \) 计算 \( X \) 的奇异同调:

\[
{H}_{D}\left\{  {{C}_{ * }\left( {\mathcal{U},{S}_{ * }}\right) }\right\}   = {H}_{ * }\left( X\right) .
\]

为了避免与上同调谱序列搞混淆,在同调谱序列中把 \( r \) 写作上标而把 \( p \) , \( q \) 写作下标:

\[
{E}_{p, q}^{r}\text{ . }
\]

现假定 \( \mathcal{U} \) 是 \( X \) 的一个好覆盖. 交换 \( \partial \) 与 \( \delta \) 的角色产生另一个谱序列,它也收敛于 \( {H}_{D}\left\{  {{C}_{ * }\left( {\mathcal{U},{S}_{ * }}\right) }\right\} \) . 此时,

(15.19)

\[
{E}^{\infty } = {E}^{2} = {H}_{\delta }{H}_{\partial } = {H}_{ * }\left( {\mathcal{U},\mathbb{Z}}\right) ,
\]

其中 \( \mathbb{Z} \) 是常值预层. 比较 (15.18) 与 (15.19) 就得到奇异同调与好覆盖的 Čech 同调 \( {H}_{ * }\left( {\mathcal{U},\mathbb{Z}}\right) \) 之间的同构.

沿着定理 14.18 的路线,若 \( \pi  : E \rightarrow  X \) 是纤维为 \( F \) 的纤维丛并且若 \( X \) 是一个具有好覆盖的单连通空间,则存在一个收敛于奇异同调 \( {H}_{ * }\left( E\right) \) 的谱序列,它的 \( {E}^{2} \) 页是

\[
{E}_{p, q}^{2} = {H}_{p}\left( {X,{H}_{q}\left( F\right) }\right) .
\]

另若 \( {H}_{q}\left( F\right) \) 是自由 \( \mathbb{Z} \) -模,则 \( {E}^{2} \) 页与张量积 \( {H}_{p}\left( X\right)  \otimes  {H}_{q}\left( F\right) \) 作为 \( \mathbb{Z} \) -模同构. 不像上同调谱序列, 在同调中一般没有乘积结构.

作业:

1. 练习 15.7.1.

2. 练习 15.10.

3. 练习 15.12.

4. 练习 15.15.1.

5. 练习 15.16.

6. 练习 15.17.
