#### 第13讲 Presheaves and ?ech Cohomology

§10 Presheaves and Čech Cohomology

13. Čech 上同调函子 \( {\Omega }^{ * } \) (   )对流形 \( M \) 的每个开集 \( U \) 赋予 \( {\Omega }^{ * }\left( U\right) \) ，即 \( U \) 上微分形式的全体. 这是预层的一个例子. 而 \( {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 是流形 \( M \) 的开覆盖 \( \mathcal{U} \) 的取值于常值预层 \( \mathbb{R} \) 的 Čech 上同调.

这节课先给出预层的定义,接着把这样的 Čech 上同调推广到开覆盖 \( \mathcal{U} \) 的取值于任意预层 \( \mathcal{F} \) 的 Čech 上同调 \( {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) . 然后通过取有向极限(direct limit)得到拓扑空间 \( X \) 的取值于预层 \( \mathcal{F} \) 的 Čech 上同调 \( {H}^{ * }\left( {X,\mathcal{F}}\right) \) . 最后证明流形的 de Rham 上同调与它的取值于常值预层 \( \mathbb{R} \) 的 Čech 上同调同构.

- 预层

- 开覆盖的 Čech 上同调

- 有向极限

- 拓扑空间的 Čech 上同调

预层

设 \( X \) 是拓扑空间, \( M \) 是流形.

定义. \( X \) 上一个预层 (presheaf) \( \mathcal{F} \) 是指: 对 \( X \) 的每个开集 \( U \) 赋予一个 abel 群 \( \mathcal{F}\left( U\right) \) ; 对 \( X \) 的每个开集的包含 \( V \subset  U \) 赋予一个群同态

\[
{\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right)
\]

并满足以下条件:

(a) \( {\rho }_{U}^{U} = \mathrm{{id}} \)

(b) 传递性: 若 \( W \subset  V \subset  U \) ,则 \( {\rho }_{W}^{V} \circ  {\rho }_{V}^{U} = {\rho }_{W}^{U} \) .

同态 \( {\rho }_{V}^{U} \) 称为限制 (restriction) .

例. 拓扑空间 \( X \) 上预层 \( {C}^{0} \) . 对 \( X \) 的任意开集 \( U \) ， \( {C}^{0}\left( U\right) \) 是 \( U \) 上连续函数的全体; 对 \( X \) 的任意开集的包含 \( V \subset  U \) ,限制 \( {\rho }_{V}^{U} : {C}^{0}\left( U\right)  \rightarrow  {C}^{0}\left( V\right) \) 是通常函数的限制.

同理,流形 \( M \) 上有预层 \( {C}^{0} \) , \( {C}^{k} \) , \( {C}^{\infty } \) , \( {C}^{\omega } \) 等. 此处 \( {C}^{\omega } \) 为 \( M \) 上实解析函数的预层.

例. 流形 \( M \) 上预层 \( {\Omega }^{ * } \) . 对 \( M \) 的任意开集 \( U \) ， \( {\Omega }^{ * }\left( U\right) \) 是 \( U \) 上微分形式的全体； 对 \( M \) 的任意开集的包含 \( V \subset  U \) ,限制 \( {\rho }_{V}^{U} : {\Omega }^{ * }\left( U\right)  \rightarrow  {\Omega }^{ * }\left( V\right) \) 是通常微分形式的限制. 特别地有预层 \( {\Omega }^{q},0 \leq  q \leq  \dim M \) ,其中 \( {\Omega }^{0} = {C}^{\infty } \) . 定义. 设 \( \mathcal{F},\mathcal{G} \) 是拓扑空间 \( X \) 上两个预层. 若对 \( X \) 的任意开集 \( U \) 存在同态

\[
{f}_{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{G}\left( U\right)
\]

使得对 \( X \) 的任意开集的包含 \( V \subset  U \) ，以下图表可交换:

![bo_d7e85t491nqc73eqefm0_290_874_609_575_365_0.jpg](images/fu_algebraic_topology_and_differential_forms_046_bod7e85t491nqc73eqefm02908746095753650.jpg)

则同态的集类 \( \left\{  {f}_{U}\right\} \) 称为从预层 \( \mathcal{F} \) 到 \( \mathcal{G} \) 的一个同态,记作 \( f : \mathcal{F} \rightarrow  \mathcal{G} \) . 如果每个同态 \( {f}_{U} \) 是同构,则称同态 \( f \) 为预层 \( \mathcal{F} \) 与 \( \mathcal{G} \) 的同构. 存在同构映射的两个预层 \( \mathcal{F} \) 与 \( \mathcal{G} \) 称为同构的,记作 \( \mathcal{F} \simeq  \mathcal{G} \) .

Open \( \left( X\right) \) 是范畴,它的对象是 \( X \) 中开集,态射是开集的包含. 用函子的语言讲, \( X \) 上一个预层不过是从范畴 \( \mathbf{{Open}}\left( X\right) \) 到 abel 群范畴的一个反变函子,两个预层的同态 \( f : \mathcal{F} \rightarrow  \mathcal{G} \) 是从函子 \( \mathcal{F} \) 到函子 \( \mathcal{G} \) 的一个自然变换.

定义. 拓扑空间 \( X \) 上预层 \( \mathcal{F} \) 称之为(取值于)abel 群 \( G \) 的常值预层,若对 \( X \) 的任意开集 \( U \) , \( \mathcal{F}\left( U\right) \) 是 \( U \) 上取值于 \( G \) 的局部常值函数的全体,并且若对 \( X \) 的任意开集的包含 \( V \subset  U \) ,限制 \( {\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) 是通常函数的限制.

所以若 \( U \) 连通,则 \( \mathcal{F}\left( U\right) \) 等同于 \( G \) ; 并且若 \( V \subset  U \) 是两个连通开集的包含,则 \( {\rho }_{V}^{U} = \mathsf{{id}} : G \rightarrow  G \) . 习惯把 abel 群 \( G \) 的常值预层简称为常值预层 \( G \) ,仍记为 \( G \) .

拓扑空间 \( X \) 上有常值预层 \( \mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C} \) 等.

例 10.1. 设 \( \pi  : E \rightarrow  M \) 是以 \( F \) 为纤维的纤维丛. 在 \( M \) 上定义预层 \( {\mathcal{H}}^{q} \) 如下: (a) 对 \( M \) 的任意开集 \( U \) ,令 \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right) \) ;

(b) 对 \( M \) 的任意开集的包含 \( V \subset  U \) ,限制

![bo_d7e85t491nqc73eqefm0_292_755_482_922_346_0.jpg](images/fu_algebraic_topology_and_differential_forms_047_bod7e85t491nqc73eqefm02927554829223460.jpg)

由包含映射 \( i : {\pi }^{-1}\left( V\right)  \rightarrow  {\pi }^{-1}\left( U\right) \) 诱导.

当 \( U \) 可缩时, \( {\pi }^{-1}\left( U\right)  \simeq  U \times  F \) ,所以由 Künneth 公式知

\[
{\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}\left( U\right) }\right)  \simeq  {H}^{q}\left( F\right) .
\]

此外,若 \( V \subset  U \) 是可缩开集的包含,则 \( {\rho }_{V}^{U} : {\mathcal{H}}^{q}\left( U\right)  \rightarrow  {\mathcal{H}}^{q}\left( V\right) \) 是同构.

预层 \( {\mathcal{H}}^{q} \) 是好覆盖上局部常值预层的一个例子,定义见第 13 节. 它在纤维化的谱序列中具有基本的重要性.

开覆盖的 Cech 上同调设 \( \mathcal{F} \) 是拓扑空间 \( X \) 上预层. \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( X \) 的开覆盖. 由良序原理可设 \( I \) 是全序集.

定义

\[
{C}^{0}\left( {\mathcal{U},\mathcal{F}}\right)  = \mathop{\prod }\limits_{{\alpha  \in  I}}\mathcal{F}\left( {U}_{\alpha }\right) .
\]

注意此处是直积,它的每个元可有无限多项不为零. 设 \( \omega  \in  {C}^{0}\left( {\mathcal{U},\mathcal{F}}\right) \) ,即对 \( \mathcal{U} \) 中每个开集 \( {U}_{\alpha } \) 指定 \( \mathcal{F}\left( {U}_{\alpha }\right) \) 中一个元 \( {\omega }_{\alpha } \) . \( \omega \) 称为开覆盖 \( \mathcal{U} \) 上取值于预层 \( \mathcal{F} \) 的一个 0-上链.

为了方便也可作如下理解. \( \omega \) 对每个下标 \( \alpha  \in  I \) 有分量 \( {\omega }_{\alpha } \in  \mathcal{F}\left( {U}_{\alpha }\right) \) .

定义

\[
{C}^{1}\left( {\mathcal{U},\mathcal{F}}\right)  = \mathop{\prod }\limits_{{\alpha  < \beta }}\mathcal{F}\left( {U}_{\alpha \beta }\right) .
\]

设 \( \omega  \in  {C}^{1}\left( {\mathcal{U},\mathcal{F}}\right) \) ,它称为1-上链. 对每对下标 \( \alpha  < \beta ,\omega \) 有分量 \( {\omega }_{\alpha \beta } \) . 一般地，定义

\[
{C}^{p}\left( {\mathcal{U},\mathcal{F}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}\mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) .
\]

它的每个元 \( \omega \) 称为 \( p \) -上链,它有分量 \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \in  \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) .

根据预层的定义,对开集的包含 \( V \subset  U \) 有限制 \( {\rho }_{V}^{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) . 对 \( {\omega }_{U} \in  \mathcal{F}\left( U\right) \) ,为简单计常常把 \( {\rho }_{V}^{U}\left( {\omega }_{U}\right) \) 记作 \( {\left. {\omega }_{U}\right| }_{V} \) ,读作 \( {\omega }_{U} \) 到开集 \( V \) 的限制. 有时甚至把限制 “ \( { \mid  }_{V} \) ” 也隐去,如能从上下文读出这个限制.

定义. 算子 \( \delta  : {C}^{p}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {C}^{p + 1}\left( {\mathcal{U},\mathcal{F}}\right) \) 定义如下. 对任意 \( \omega  \in  {C}^{p}\left( {\mathcal{U},\mathcal{F}}\right) \) ,定义 \( {\delta \omega } \in  {C}^{p + 1}\left( {\mathcal{U},\mathcal{F}}\right) \) ,它的分量

(10.2)

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}}.
\]

在定义的右边 \( {\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}} \) 到开集 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} \) 的限制被隐去了,这是因为我们能从等式的左边读出这个限制.

显然由限制的传递性可得 \( {\delta }^{2} = 0 \) .

定义. 复形 \( \left\{  {{C}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) ,\delta }\right\} \) 的上同调 \( {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) 称为覆盖 \( \mathcal{U} \) 的取值于预层 \( \mathcal{F} \) 的 Čech 上同调.

注记 10.3. 若 \( \mathcal{F} \) 是从范畴 \( \operatorname{Open}\left( X\right) \) 到 abel 群范畴的共变函子, \( \mathcal{U} \) 是 \( X \) 的开覆盖,则类似地可定义链复形 \( {C}_{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) 与它的同调 \( {H}_{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) . 除了箭头方向, 与预层的情形相比仅有的差别是上边缘算子 \( \delta  : {C}_{p}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {C}_{p - 1}\left( {\mathcal{U},\mathcal{F}}\right) \) 的定义, 现为

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \in  \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right) .
\]

容易验证这个 \( \delta \) 也满足 \( {\delta }^{2} = 0 \) . 对流形的任意开集 \( U \) 赋予它的紧上同调 \( {H}_{c}^{q}\left( U\right) \) 的函子 \( {\mathcal{H}}_{c}^{q} \) 是一个共变函子.

按惯例下标具有反称性，所以在上述公式中和式不带符号. 当然，如果在写每项 \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) 时把下标 \( \alpha \) 插入第 \( i \) 个位置,则会产生符号: \( \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots \alpha \ldots {\alpha }_{p - 1}} \) .

Remark 10.3. If \( \mathcal{F} \) is a covariant functor from the category \( \operatorname{Open}\left( X\right) \) to the category of Abelian groups, and \( \mathcal{U} \) is an open cover of \( X \) , one can define analogously a chain complex \( {C}_{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) and its homology \( {H}_{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) . Apart from the direction of the arrows, the only difference from the case of a presheaf is in the definition of the coboundary operator \( \delta  : {C}_{p}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {C}_{p - 1}\left( {\mathcal{U},\mathcal{F}}\right) \) , which is now given by

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \in  \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right) .
\]

One verifies easily that this \( \delta \) also satisfies \( {\delta }^{2} = 0 \) . The functor \( {\mathcal{H}}_{c}^{q} \) which associates to every open set \( U \) on a manifold the compact cohomology \( {H}_{c}^{q}\left( U\right) \) is covariant.

Because of the antisymmetry convention on the subscripts, in this formula there is no sign in the sum. Of course, if we had written each term \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) with the subscript \( \alpha \) inserted in the \( i \) -th place, then there would be a sign: \( \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots \alpha \ldots {\alpha }_{p - 1}} \) . 回到预层 \( \mathcal{F} \) 的 Čech 上同调的讨论. 回忆开覆盖加细的定义.

定义. 设 \( \mathcal{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J},\mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( X \) 的两个开覆盖. 若存在映射 \( \phi  : J \rightarrow  I \) 使得对任意的 \( \beta  \in  J,{V}_{\beta } \subset  {U}_{\phi \left( \beta \right) } \) ,则称 \( \mathcal{V} \) 是 \( \mathcal{U} \) 的一个加细,记作 \( \mathcal{U} < \mathcal{V} \) ,而 \( \phi \) 称为加细映射.

加细映射 \( \phi \) 诱导了映射

\[
{\phi }^{\# } : {C}^{q}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {C}^{q}\left( {\mathcal{V},\mathcal{F}}\right)
\]

\[
{\left( {\phi }^{\# }\omega \right) }_{{\beta }_{0}\ldots {\beta }_{q}} = {\omega }_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q}\right) }{ \mid  }_{{V}_{{\beta }_{0}\ldots {\beta }_{q}}}
\]

上述限制映射是有意义的，因为

\[
{\omega }_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q}\right) } \in  \mathcal{F}\left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q}\right) }\right)
\]

\[
{V}_{{\beta }_{0}\ldots {\beta }_{q}} \subset  {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q}\right) }
\]

引理 10.4.1. \( {\phi }^{\# } \) 是一个链映射,即 \( {\phi }^{\# }\delta  = \delta {\phi }^{\# } \) .

证.

\[
{\left( \delta {\phi }^{\# }\omega \right) }_{{\beta }_{0}\ldots {\beta }_{q + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{q + 1}}{\left( -1\right) }^{i}{\left( {\phi }^{\# }\omega \right) }_{{\beta }_{0}\ldots {\widehat{\beta }}_{i}\ldots {\beta }_{q + 1}}
\]

\[
= \mathop{\sum }\limits_{{i = 0}}^{{q + 1}}{\left( -1\right) }^{i}{\omega }_{\phi \left( {\beta }_{0}\right) \ldots \widehat{\phi \left( {\beta }_{i}\right) }\ldots \phi \left( {\beta }_{q + 1}\right) }.
\]

\[
{\left( {\phi }^{\# }\delta \omega \right) }_{{\beta }_{0}\ldots {\beta }_{q + 1}} = {\left( \delta \omega \right) }_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q + 1}\right) }
\]

\[
= \mathop{\sum }\limits_{{i = 0}}^{{q + 1}}{\left( -1\right) }^{i}{\omega }_{\phi \left( {\beta }_{0}\right) \ldots \widehat{\phi \left( {\beta }_{i}\right) }\ldots \phi \left( {\beta }_{q + 1}\right) }
\]

引理 10.4.2. 给定开覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 与它的加细 \( \mathcal{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) ,若 \( \phi ,\psi  : J \rightarrow  I \) 是两个加细映射,则 \( {\phi }^{\# },{\psi }^{\# } \) 链同伦.

证. 定义 \( K : {C}^{q}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {C}^{q - 1}\left( {\mathcal{V},\mathcal{F}}\right) \) 为

\[
{\left( K\omega \right) }_{{\beta }_{0}\ldots {\beta }_{q - 1}} = \mathop{\sum }\limits_{{i = 0}}^{{q - 1}}{\left( -1\right) }^{i}{\omega }_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{i}\right) \psi \left( {\beta }_{i}\right) \ldots \psi \left( {\beta }_{q - 1}\right) }.
\]

则可证明 \( K \) 是链同伦算子:

\[
{\psi }^{\# } - {\phi }^{\# } = {\delta K} + {K\delta }
\]

练习 10.5. 证明上述等式.

由上述两个引理得到

命题. 设开覆盖 \( \mathcal{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) 是 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 的一个加细, \( \phi  : J \rightarrow  I \) 是加细映射. 则 \( \phi \) 诱导了同态

\[
{\phi }^{\# } : {H}^{q}\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {H}^{q}\left( {\mathcal{V},\mathcal{F}}\right) ,
\]

它与加细映射 \( \phi \) 的选取无关.

有向极限

定义. 设在集合 \( I \) 上定义了一个偏序 “ \( < \) ”,它满足以下条件:

(a) 对任意的 \( a \in  I, a < a \) ;

(b) 对任意的 \( a, b, c \in  I \) ,若 \( a < b, b < c \) ,则 \( a < c \) ;

(c) 对任意的 \( a, b \in  I \) ,存在 \( c \in  I \) ,使得 \( a < c, b < c \) .

则称 \( I \) 是一个有向集 (directed set).

定义. 群的有向系 (direct system of groups) 是群的集类 \( {\left\{  {G}_{a}\right\}  }_{a \in  I} \) ,以有向集 \( I \) 为指标集,使得对每对指标 \( a < b \) 存在群同态 \( {f}_{b}^{a} : {G}_{a} \rightarrow  {G}_{b} \) 并满足以下条件:

(1) \( {f}_{a}^{a} = \mathrm{{id}} \)

(2) \( {f}_{c}^{a} = {f}_{c}^{b} \circ  {f}_{b}^{a} \) 若 \( a < b < c \) .

在不相交的并

\[
\mathop{\coprod }\limits_{{a \in  I}}{G}_{a}
\]

上引入等价关系 “ \( \sim \) ”: 对 \( {g}_{a} \in  {G}_{a} \) 与 \( {g}_{b} \in  {G}_{b},{g}_{a} \sim  {g}_{b} \) 若存在一个 \( c \in  I \) 使得 \( a < c, b < c \) ,且在 \( {G}_{c} \) 中

\[
{f}_{c}^{a}\left( {g}_{a}\right)  = {f}_{c}^{b}\left( {g}_{b}\right) . \tag{28}
\]

把 \( {g}_{a} \) 所在的等价类记作 \( \left\lbrack  {g}_{a}\right\rbrack \) . 所以 \( \left\lbrack  {g}_{a}\right\rbrack   = \left\lbrack  {g}_{b}\right\rbrack \) 当且仅当等式 (28) 成立,它们在路上已相等.

定义. 群的有向系 \( {\left\{  {G}_{a}\right\}  }_{a \in  I} \) 的有向极限 (direct limit) 定义为

\[
\mathop{\lim }\limits_{{a \in  I}}{G}_{a} = \left( {\mathop{\coprod }\limits_{{a \in  I}}{G}_{a}}\right) / \sim
\]

在其上定义加法: 因为对任意的 \( a, b \in  I \) 存在 \( c \in  I \) 使得 \( a < c, b < c \) ,所以定义

\[
\left\lbrack  {g}_{a}\right\rbrack   + \left\lbrack  {g}_{b}\right\rbrack   = \left\lbrack  {{f}_{c}^{a}\left( {g}_{a}\right)  + {f}_{c}^{b}\left( {g}_{b}\right) }\right\rbrack  .
\]

有向极限 \( \mathop{\lim }\limits_{{a \in  I}}{G}_{a} \) 在这个加法下是群.

拓扑空间的 Čech 上同调把上述理论应用到 \( {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) ,即拓扑空间 \( X \) 的开覆盖 \( \mathcal{U} \) 上取值于预层 \( \mathcal{F} \) 的 Čech 上同调, 有:

(a) 有向集为 \( X \) 的所有开覆盖的集合: \( I = \{ \mathcal{U},\mathcal{V},\mathcal{W},\ldots \} \) ;

(b) \( \mathcal{U} < \mathcal{V} \) 表示 \( \mathcal{V} \) 是 \( \mathcal{U} \) 的一个加细;

(c) \( {G}_{\mathcal{U}} = {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) ;

(d) 若 \( \phi  : \mathcal{V} \rightarrow  \mathcal{U} \) 是加细,则 \( {\phi }^{\# } : {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {H}^{ * }\left( {\mathcal{V},\mathcal{F}}\right) \) 是同态,见命题.

(e) 若 \( \psi  : \mathcal{W} \rightarrow  \mathcal{V},\phi  : \mathcal{V} \rightarrow  \mathcal{U} \) 是加细,则 \( \varphi  = \phi  \circ  \psi  : \mathcal{W} \rightarrow  \mathcal{U} \) 是加细,并且

\[
{\varphi }^{\# } = {\psi }^{\# } \circ  {\phi }^{\# } : {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right)  \rightarrow  {H}^{ * }\left( {\mathcal{W},\mathcal{F}}\right) .
\]

这样, \( {\left\{  {H}^{ * }\left( \mathcal{U},\mathcal{F}\right) \right\}  }_{\mathcal{U} \in  I} \) 是群的有向系,它的有向极限

\[
\mathop{\lim }\limits_{\mathcal{U}}{H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right)
\]

称为拓扑空间 \( X \) 的取值于预层 \( \mathcal{F} \) 的 Čech 上同调,记作 \( {H}^{ * }\left( {X,\mathcal{F}}\right) \) .

命题 10.6. 设 \( \mathbb{R} \) 是流形 \( M \) 上常值预层. 则

\[
{H}^{ * }\left( {M,\mathbb{R}}\right)  \simeq  {H}_{dR}^{ * }\left( M\right)
\]

证. 对流形 \( M \) 的任意开覆盖 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) ,存在好覆盖 \( \mathcal{V} \) 使得 \( \mathcal{V} \) 是 \( \mathcal{U} \) 的加细. 事实上, \( {U}_{\alpha } \) 中任一点 \( p \) 有测地凸邻域 \( {V}_{p} \subset  {U}_{\alpha } \) . 所以

\[
\mathcal{V} = \left\{  {{V}_{p} \mid  p \in  {U}_{\alpha },\alpha  \in  I}\right\}
\]

是好覆盖且是 \( \mathcal{U} \) 的加细. 由第二可数性公理我们还可假定 \( \mathcal{V} \) 的开集个数是可数的.

这样在取有向极限的过程中，因为两个等价类相等表示它们的代表元“在路上已相等”，所以只要考虑 \( M \) 的所有具可数多个开集的好覆盖(c.g.c)就行了:

\[
{H}^{ * }\left( {M,\mathbb{R}}\right)  = \mathop{\lim }\limits_{{c.g.c.\mathcal{U}}}{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) .
\]

但由定理 8.9 知,若 \( \mathcal{U} \) 是好覆盖且具有可数多个开集,则

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \simeq  {H}_{dR}^{ * }\left( M\right)
\]

显然这个同构与好覆盖的加细是相容的,即若 \( \mathcal{V} \) 也是一个可数好覆盖且是 \( \mathcal{U} \) 的一个加细, 则下列图表是可交换的:

![bo_d7e85t491nqc73eqefm0_305_577_705_1164_555_0.jpg](images/fu_algebraic_topology_and_differential_forms_048_bod7e85t491nqc73eqefm030557770511645550.jpg)

因此

\[
{H}^{ * }\left( {M,\mathbb{R}}\right)  = \mathop{\lim }\limits_{{c.g.c.\mathcal{U}}}{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \simeq  {H}_{dR}^{ * }\left( M\right) .
\]

练习 10.7.(扭(twisted)系数的上同调)设 \( \mathcal{F} \) 是 \( {S}^{1} \) 上预层,它对 \( {S}^{1} \) 的任意开集 \( U \) 赋予 \( \mathcal{F}\left( U\right)  = \mathbb{Z} \) . 在好覆盖 \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) 上定义限制同态为:

\[
{\rho }_{01}^{0} = {\rho }_{01}^{1} = 1
\]

\[
{\rho }_{12}^{1} = {\rho }_{12}^{2} = 1
\]

\[
{\rho }_{02}^{2} =  - 1,{\rho }_{02}^{0} = 1
\]

此处 \( {\rho }_{ij}^{i} : \mathcal{F}\left( {U}_{i}\right)  \rightarrow  \mathcal{F}\left( {U}_{ij}\right) \) . 计算 \( {H}^{ * }\left( {\mathcal{U},\mathcal{F}}\right) \) .

![bo_d7e85t491nqc73eqefm0_306_889_994_539_510_0.jpg](images/fu_algebraic_topology_and_differential_forms_049_bod7e85t491nqc73eqefm03068899945395100.jpg)

作业:

1. 练习 10.5.

2. 练习 10.7.

代数拓扑与微分形式
