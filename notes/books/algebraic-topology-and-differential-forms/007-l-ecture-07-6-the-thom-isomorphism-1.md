#### 7. 向量丛基础

代数拓扑与微分形式 §6 The Thom Isomorphism (1)

7. 向量丛基础到目前为止已定义了流形的两种光滑不变量， de Rham 上同调与紧上同调. 对向量丛的全空间另有一种不变量，即在垂直方向具紧支集的上同调，简称紧垂直上同调 (compact vertical cohomology) . Thom 同构是关于这个上同调的断言. 在这节应用 MV 方法证明定向向量丛的 Thom 同构. 接着解释为什么 Poincaré 对偶与 Thom 类其实是一回事, 即子流形的 Poincaré 对偶是法丛的 Thom 类. 应用这一事实，至少在法丛平凡时就很容易显式写下 Poincaré 对偶. 最后给出定向平面丛的 Thom 类的显式构造, 并在这个过程中引入角形式与欧拉类. 高秩的类比在第 11 节与第 12 节处理. 我们不打算讲这节最后的相对 de Rham 上同调, 所以也没有提及把 Thom 类作为相对类的例子. 讲这节需四次课. 这次课讲向量丛基础， 主要包括

- 向量丛的局部平凡化

- 结构群的约化

- 向量丛上运算

- 向量丛的同伦性 So far we have encountered two kinds of \( {C}^{\infty } \) invariants of a manifold, de Rham cohomology and compactly Supported cohomology. For vector bundles there is another invariant, namely, cohomology with compact Support in the vertical direction. The Thom isomorphism is a statement about this last-named cohomology. In this section we use the Mayer-Vietoris argument to prove the Thom isomorphism for an orientable vector bundle. We then explain why the Poincaré dual and the Thom class are in fact one and the same thing. Using the interpretation of the Poincaré dual of a submanifold as the Thom class of the normal bundle, it is easy to write down explicitly the Poincaré dual, at least when the normal bundle ie trivial. Next we give an explicit construction of the Thom class for an oriented rank 2 bundle, introducing along the way the global angular form and the Euler class. The higher-rank analogues will be taken up in Sections 11 and 12. We conclude this section with a brief discussion of the relative de Rham theory, citing the Thom class as an example of a relative class.

向量丛的局部平凡化定义. 设 \( E, M \) 是光滑流形, \( \pi  : E \rightarrow  M \) 是满射并且对 \( M \) 的每点 \( x \) ,纤维 \( {E}_{x} = {\pi }^{-1}\left( x\right) \) 是向量空间. 若存在 \( M \) 的开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) ,并对任意的 \( \alpha  \in  I \) 存在微分同胚

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} = {\pi }^{-1}\left( {U}_{\alpha }\right)  \rightarrow  {U}_{\alpha } \times  {\mathbb{R}}^{n},
\]

它把 \( {U}_{\alpha } \) 中每点 \( x \) 的纤维 \( {E}_{x} \) 映为纤维 \( \{ x\}  \times  {\mathbb{R}}^{n} \) 并且这个映射是向量空间的同构， 则称 \( \pi  : E \rightarrow  M \) 是秩为 \( n \) 的光滑(实)向量丛. \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 称为向量丛 \( E \) 的一个局部平凡化. 流形 \( E \) 与 \( M \) 分别称为全空间与底流形.

其实,向量丛是纤维为 \( {\mathbb{R}}^{n} \) ,结构群为 \( {GL}\left( {n,\mathbb{R}}\right) \) 的纤维丛. 纤维为 \( {\mathbb{C}}^{n} \) ,结构群为 \( {GL}\left( {n,\mathbb{C}}\right) \) 的向量丛称为复向量丛. 除非另作说明,我们在这里讲的向量丛都是光滑实向量丛.

设 \( U \) 是 \( M \) 的一个开集,光滑映射 \( s : U \rightarrow  E \) 称为向量丛 \( E \) 在 \( U \) 上的一个截面若 \( \pi  \circ  s : U \rightarrow  U \) 是恒等映射. \( E \) 在 \( U \) 上的所有截面的空间记为 \( \Gamma \left( {U, E}\right) \) . 注意每个向量丛 \( E \) 有零截面:

\[
s : M \rightarrow  E,\;s\left( x\right)  = {0}_{x} \in  {E}_{x},
\]

其中 \( {0}_{x} \) 是向量空间 \( {E}_{x} \) 的零向量. \( U \) 上 \( n \) 个截面 \( {s}_{1},\ldots ,{s}_{n} \) 称为 \( U \) 上一个标架若对 \( U \) 中每点 \( x \) , \( {s}_{1}\left( x\right) ,\ldots ,{s}_{n}\left( x\right) \) 是向量空间 \( {E}_{x} \) 的一组基.

对于局部平凡化 \( \{ \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) {\} }_{\alpha  \in  I} \) ,在 \( {U}_{\alpha } \) 上存在一个“自然”标架 \( {\varepsilon }_{1}^{\alpha },\ldots ,{\varepsilon }_{n}^{\alpha } \) : 对每点 \( x \in  {U}_{\alpha } \) ,令

\[
{\varepsilon }_{i}^{\alpha }\left( x\right)  = {\phi }_{\alpha }^{-1}\left( {x,{e}_{i}}\right) ,
\]

其中 \( {e}_{1},\ldots ,{e}_{n} \) 是 \( {\mathbb{R}}^{n} \) 上给定的标准单位正交基. 反之, \( U \) 上标架 \( {s}_{1},\ldots ,{s}_{n} \) 给出了 \( {\left. E\right| }_{U} \) 的平凡化:

\[
\phi  : {\left. E\right| }_{U}\overset{ \sim  }{ \rightarrow  }U \times  {\mathbb{R}}^{n}
\]

\[
\phi \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{v}_{i}{s}_{i}\left( x\right) }\right)  = \left( {x,{\left( {v}_{1},\ldots ,{v}_{n}\right) }^{t}}\right) .
\]

标架与局部平凡化之间的相互转化是研究向量丛的基本方法.

向量丛的本质是它的转移函数. 对任意点 \( x \in  {U}_{\alpha \beta } \) ,由于映射 \( {\left. {\phi }_{\alpha }\right| }_{{E}_{x}} : {E}_{x} \rightarrow \; \{ x\}  \times  {\mathbb{R}}^{n} \) 与映射 \( {\left. {\phi }_{\beta }\right| }_{{E}_{x}} : {E}_{x} \rightarrow  \{ x\}  \times  {\mathbb{R}}^{n} \) 是向量空间的同构,所以

\[
{\left. {\phi }_{\alpha }\right| }_{{E}_{x}} \circ  {\left( {\left. {\phi }_{\beta }\right| }_{{E}_{x}}\right) }^{-1} : \{ x\}  \times  {\mathbb{R}}^{n} \rightarrow  \{ x\}  \times  {\mathbb{R}}^{n}
\]

是向量空间 \( {\mathbb{R}}^{n} \) 的一个自同构,即存在 \( {g}_{\alpha \beta }\left( x\right)  \in  {GL}\left( {n,\mathbb{R}}\right) \) 使得对任意的 \( v \in  {\mathbb{R}}^{n} \) ,

\[
{\phi }_{\alpha }{\phi }_{\beta }^{-1}\left( {x, v}\right)  = \left( {x,{g}_{\alpha \beta }\left( x\right) v}\right) . \tag{3}
\]

由此定义了一个矩阵值的光滑映射 \( {g}_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  {GL}\left( {n,\mathbb{R}}\right) \) .

\[
\begin{array}{l} E{|}_{{U}_{\alpha \beta }}\overset{{\phi }_{\alpha }}{ \rightarrow  }{U}_{\alpha \beta } \times  {\mathbb{R}}^{n} \ni  \left( {x,{g}_{\alpha \beta }\left( x\right) v}\right) \\  E{|}_{{U}_{\alpha \beta }}\overset{ \uparrow  }{ \leftarrow  }{U}_{\alpha \beta } \times  {\mathbb{R}}^{n}\; \ni  \left( {x, v}\right) \\  \end{array}
\]

\( \left\{  {g}_{\alpha \beta }\right\} \) 称为向量丛 \( E \) 关于局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 的转移函数,满足以下的 cocycle 条件:

\[
{g}_{\alpha \beta } = {g}_{\beta \alpha }^{-1}\;\text{ on }{U}_{\alpha \beta }
\]

\[
{g}_{\alpha \beta } \circ  {g}_{\beta \gamma } = {g}_{\alpha \gamma }\;\text{ on }{U}_{\alpha \beta \gamma }
\]

它们依赖于平凡化的选取.

引理 6.1. 若向量丛 \( E \) 有另一平凡化 \( \{ \left( {{U}_{\alpha },{\phi }_{\alpha }^{\prime }}\right) {\} }_{\alpha  \in  I} \) ，它的转移函数是 \( \{ {g}_{\alpha \beta }^{\prime }\} \) ，则存在光滑的矩阵值映射 \( {\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  {GL}\left( {n,\mathbb{R}}\right) \) 使得在 \( {U}_{\alpha \beta } \) 上,

\[
{g}_{\alpha \beta }\left( x\right)  = {\lambda }_{\alpha }\left( x\right) {g}_{\alpha \beta }^{\prime }\left( x\right) {\lambda }_{\beta }^{-1}\left( x\right) .
\]

此处 \( {\lambda }_{\beta }^{-1}\left( x\right) \) 记矩阵 \( {\lambda }_{\beta }\left( x\right) \) 的逆矩阵.

证. 由于局部平凡化 \( {\phi }_{\alpha },{\phi }_{\alpha }^{\prime } \) 是保纤维的并且限制在纤维上是向量空间的同构,所以对任意的 \( x \in  {U}_{\alpha } \) ,映射 \( {\phi }_{\alpha } \circ  {\left( {\phi }_{\alpha }^{\prime }\right) }^{-1} : \{ x\}  \times  {\mathbb{R}}^{n} \rightarrow  \{ x\}  \times  {\mathbb{R}}^{n} \) 是 \( {\mathbb{R}}^{n} \) 的一个自同构, 即存在 \( {\lambda }_{\alpha }\left( x\right)  \in  {GL}\left( {n,\mathbb{R}}\right) \) 使得对任意的 \( v \in  {\mathbb{R}}^{n} \) ,

\[
{\phi }_{\alpha }{\left( {\phi }_{\alpha }^{\prime }\right) }^{-1}\left( {x, v}\right)  = \left( {x,{\lambda }_{\alpha }\left( x\right) v}\right) . \tag{4}
\]

显然矩阵值映射 \( {\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  {GL}\left( {n,{\mathbb{R}}^{n}}\right) \) 是光滑的. 由 (3),(4) 可作如下推导:

\[
\left( {x,{g}_{\alpha \beta }\left( x\right) v}\right)  = {\phi }_{\alpha }{\phi }_{\beta }^{-1}\left( {x, v}\right)
\]

\[
= {\phi }_{\alpha }{\left( {\phi }_{\alpha }^{\prime }\right) }^{-1}{\phi }_{\alpha }^{\prime }{\left( {\phi }_{\beta }^{\prime }\right) }^{-1}{\phi }_{\beta }^{\prime }{\phi }_{\beta }^{-1}\left( {x, v}\right)
\]

\[
= {\phi }_{\alpha }{\left( {\phi }_{\alpha }^{\prime }\right) }^{-1}{\phi }_{\alpha }^{\prime }{\left( {\phi }_{\beta }^{\prime }\right) }^{-1}\left( {x,{\lambda }_{\beta }^{-1}\left( x\right) v}\right)
\]

\[
= {\phi }_{\alpha }{\left( {\phi }_{\alpha }^{\prime }\right) }^{-1}\left( {x,{g}_{\alpha \beta }^{\prime }\left( x\right) {\lambda }_{\beta }^{-1}\left( x\right) v}\right)
\]

\[
= \left( {x,{\lambda }_{\alpha }\left( x\right) {g}_{\alpha \beta }^{\prime }\left( x\right) {\lambda }_{\beta }^{-1}\left( x\right) v}\right) .
\]

设秩为 \( n \) 的向量丛 \( \pi  : E \rightarrow  M \) 与 \( {\pi }^{\prime } : {E}^{\prime } \rightarrow  M \) 分别有局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 与 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }^{\prime }\right) \right\}  }_{\alpha  \in  I} \) . 若对任意 \( \alpha  \in  I \) ,存在光滑映射 \( {\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  {GL}\left( {n,\mathbb{R}}\right) \) 使得对任意的 \( x \in  {U}_{\alpha \beta } \) ,

\[
{g}_{\alpha \beta }\left( x\right)  = {\lambda }_{\alpha }\left( x\right) {g}_{\alpha \beta }^{\prime }\left( x\right) {\lambda }_{\beta }^{-1}\left( x\right) ,
\]

则称向量丛 \( E \) 与 \( {E}^{\prime } \) 的转移函数是等价的. 由上述引理知,同一个向量丛的不同平凡化的转移函数是等价的.

光滑映射 \( f : E \rightarrow  {E}^{\prime } \) 称为丛映射若它把 \( E \) 的每条纤维 \( {E}_{x} \) 线性地映为 \( {E}^{\prime } \) 的纤维 \( {E}_{x}^{\prime } \) . 若 \( f \) 限制在每条纤维上的线性映射是同构,则称 \( f \) 是同构. 此时称 \( E \) 与 \( {E}^{\prime } \) 同构.

丛映射 \( f : E \rightarrow  {E}^{\prime } \) 也称为从 \( E \) 到 \( {E}^{\prime } \) 的同态. 这种同态的全体记为 \( \operatorname{Hom}\left( {E,{E}^{\prime }}\right) \) .

练习 6.2. \( M \) 上两个向量丛同构当且仅当它们相对于某一开覆盖的局部平凡化的转移函数等价. 其实,先验地向量丛 \( \pi  : E \rightarrow  M \) 的局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 与向量丛 \( {\pi }^{\prime } : {E}^{\prime } \rightarrow \; M \) 的局部平凡化 \( \{ \left( {{U}_{i},{\phi }_{i}^{\prime }}\right) {\} }_{i \in  J} \) 的两个开覆盖 \( \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) 与 \( \{ {U}_{i}{\} }_{i \in  J} \) 可能不一样. 此时令

\[
\Lambda  = \left\{  {\left( {\alpha , i}\right)  \in  I \times  J \mid  {U}_{\alpha i} \neq  \varnothing }\right\}  .
\]

则 \( E,{E}^{\prime } \) 分别有平凡化

\[
{\left\{  \left( {U}_{\alpha i},{\left. {\phi }_{\alpha }\right| }_{{U}_{\alpha i}}\right) \right\}  }_{\left( {\alpha , i}\right)  \in  \Lambda },\;{\left\{  \left( {U}_{\alpha i},{\left. {\phi }_{i}^{\prime }\right| }_{{U}_{\alpha i}}\right) \right\}  }_{\left( {\alpha , i}\right)  \in  \Lambda }.
\]

于是可问这两个平凡化的转移函数是否等价. 如果它们等价,则向量丛 \( E \) , \( {E}^{\prime } \) 同构.

上述讨论使我们明白对 \( M \) 上两个向量丛的局部平凡化,我们总能假定 \( M \) 的两个开覆盖相同.

结构群的约化

定义. 如果向量丛 \( \pi  : E \rightarrow  M \) 存在一个局部平凡化,它的转移函数只取值于 \( {GL}\left( {n,\mathbb{R}}\right) \) 的子群 \( H \) ,则称向量丛 \( E \) 的结构群可约化到 \( H \) .

这就是说,对于给定的向量丛 \( E \) 的一个局部平凡化的转移函数 \( \left\{  {g}_{\alpha \beta }\right\} \) ,若能找到一个等价的转移函数 \( \{ {g}_{\alpha \beta }^{\prime }\} \) ,它们只取值于 \( {GL}\left( {n,\mathbb{R}}\right) \) 的子群 \( H \) ,则称向量丛 \( E \) 的结构群可约化到 \( H \) .

\( H \) 一般为

(a) 行列式正的线性变换群 \( G{L}^{ + }\left( {n,\mathbb{R}}\right) \) ,

(b) 正交群 \( O\left( n\right) \) ,或

(c) 特殊正交群 \( {SO}\left( n\right) \) . 定义. 若 \( E \) 的结构群可约化到 \( G{L}^{ + }\left( {n,\mathbb{R}}\right) \) ,则称 \( E \) 是可定向的. \( E \) 上一个局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 称为定向的若对任意的 \( \alpha ,\beta  \in  I \) , det \( {g}_{\alpha \beta } > 0 \) . 两个定向平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 与 \( {\left\{  \left( {U}_{\alpha },{\varphi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 称为等价的若对任意的 \( x \in  {U}_{\alpha } \) ,线性映射

\[
{\phi }_{\alpha } \circ  {\varphi }_{\alpha }^{-1}\left( x\right)  : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}
\]

的行列式是正的. 这样若 \( M \) 连通, \( M \) 上可定向向量丛 \( E \) 的所有定向平凡化分成两个等价类,每个等价类称为 \( E \) 的一个定向. 给定定向的可定向 (orientable) 向量丛称为定向 (oriented) 向量丛.

例 6.3. (切丛) 设 \( M \) 是光滑流形, \( {\left\{  \left( {U}_{\alpha },{\psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( M \) 的一个坐标图册. \( M \) 在每点 \( p \) 有切空间 \( {T}_{p}M \) . 令

\[
{TM} = \mathop{\bigcup }\limits_{{p \in  M}}{T}_{p}M
\]

微分同胚 \( {\psi }_{\alpha } : {U}_{\alpha } \rightarrow  {\psi }_{\alpha }\left( {U}_{\alpha }\right)  \subset  {\mathbb{R}}^{n} \) 诱导了切映射

\[
{\left( {\psi }_{\alpha }\right) }_{ * } : {\left. TM\right| }_{{U}_{\alpha }} = {\left. T{U}_{\alpha }\overset{ \sim  }{ \rightarrow  }T{\mathbb{R}}^{n}\right| }_{{\psi }_{\alpha }\left( {U}_{\alpha }\right) },
\]

它给出了切丛 \( {TM} \) 的局部平凡化:

\[
{\phi }_{\alpha } : {\left. TM\right| }_{{U}_{\alpha }}\overset{{\left( {\psi }_{\alpha }\right) }_{ * }}{ \rightarrow  }{\left. T{\mathbb{R}}^{n}\right| }_{{\psi }_{\alpha }\left( {U}_{\alpha }\right) }\overset{ \sim  }{ \rightarrow  }{\psi }_{\alpha }\left( {U}_{\alpha }\right)  \times  {\mathbb{R}}^{n}\xrightarrow[]{\left( {\psi }_{\alpha }^{-1},\mathrm{{id}}\right) }{U}_{\alpha } \times  {\mathbb{R}}^{n}.
\]

\( {\mathbb{R}}^{n} \) 的标准坐标 \( {x}_{1},\ldots ,{x}_{n} \) 给出了 \( {U}_{\alpha } \) 的局部坐标 \( {x}_{1}^{\alpha },\ldots ,{x}_{n}^{\alpha } \) ,其中 \( {x}_{i}^{\alpha } = {x}_{i} \circ  {\psi }_{\alpha } \) . \( {TM}{ \mid  }_{{U}_{\alpha }} \) 的一个标架是

\[
{\left\{  \frac{\partial }{\partial {x}_{i}^{\alpha }}\right\}  }_{1 \leq  i \leq  n},\;{\left( {\psi }_{\alpha }\right) }_{ * }\left( \frac{\partial }{\partial {x}_{i}^{\alpha }}\right)  = \frac{\partial }{\partial {x}_{i}}.
\]

所以转移函数是

\[
{g}_{\alpha \beta }\frac{\partial }{\partial {x}_{j}} = {\left( {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1}\right) }_{ * }\left( \frac{\partial }{\partial {x}_{j}}\right)  = \sum \frac{\partial {\left( {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1}\right) }_{i}}{\partial {x}_{j}}\frac{\partial }{\partial {x}_{i}},
\]

即 \( {g}_{\alpha \beta } \) 是微分同胚 \( {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1} : {\psi }_{\beta }\left( {U}_{\alpha \beta }\right)  \rightarrow  {\psi }_{\alpha }\left( {U}_{\alpha \beta }\right) \) 的 Jacobi 矩阵. 我们也可直接对标架用链规则,

\[
\frac{\partial }{\partial {x}_{j}^{\beta }} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial {x}_{i}^{\alpha }}{\partial {x}_{j}^{\beta }}\frac{\partial }{\partial {x}_{i}^{\alpha }},
\]

再用第 21 页第 10 行的定义得到

\[
\frac{\partial {x}_{i}^{\alpha }}{\partial {x}_{j}^{\beta }} = \frac{\partial \left( {{x}_{i}^{\alpha } \circ  {\psi }_{\beta }^{-1}}\right) }{\partial {x}_{j}} = \frac{\partial {\left( {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1}\right) }_{i}}{\partial {x}_{j}}.
\]

我们发现相同的结论(见补充练习 2).

于是流形 \( M \) 可定向当且仅当它的切丛 \( {TM} \) 可定向.

补充练习 1. 证明切丛 \( {TM} \) 的全空间即它作为流形总是可定向的.

命题 6.4. 秩 \( n \) 向量丛 \( E \) 的结构群总可约化到 \( O\left( n\right) \) ; 它能约化到 \( {SO}\left( n\right) \) 当且仅当 \( E \) 是可定向的.

证. 首先赋予 \( E \) 一个度量 \( \langle \) , \( \rangle \) ,即对任意纤维 \( {E}_{x} \) 赋予一个内积 \( \langle \) , \( \rangle x \) ,并且这个内积光滑依赖于点 \( x \) ,即对 \( E \) 的任意两个光滑截面 \( s \) 与 \( t \) , \( M \) 上函数

\[
\langle s\left( x\right) , t\left( x\right) {\rangle }_{x}
\]

是光滑的. 其实,对于 \( E \) 的局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) ,在 \( {\left. E\right| }_{{U}_{\alpha }} \) 上已定义了一组自然标架 \( {\varepsilon }_{1}^{\alpha },\ldots ,{\varepsilon }_{n}^{\alpha } \) . 对任意的 \( x \in  {U}_{\alpha } \) ,令

\[
{\left\langle  {\varepsilon }_{i}^{\alpha },{\varepsilon }_{j}^{\alpha }\right\rangle  }_{x} = {\delta }_{ij}.
\]

这样就在 \( {\left. E\right| }_{{U}_{\alpha }} \) 上定义了一个度量 \( \langle \;,{\rangle }_{\alpha } \) . 再令

\[
\langle \;,\;\rangle  = \sum {\rho }_{\alpha }\langle \;,\;{\rangle }_{\alpha },
\]

其中 \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) 是从属于开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 的单位分解. 则 \( \langle \) , \( \rangle \rangle \) 是 \( E \) 上一个度量.

接着对 \( E \) 重新局部平凡化. 在 \( E \) 上给定上述度量后, \( E{ \mid  }_{{U}_{\alpha }} \) 上的自然标架 \( {\varepsilon }_{1}^{\alpha },\ldots ,{\varepsilon }_{n}^{\alpha } \) 不一定是正交的,但我们可用 Gram-Schimit 正交化把它变成单位正交标架 \( {t}_{1}^{\alpha },\ldots ,{t}_{n}^{\alpha } \) . 这样可定义局部平凡化 \( {\phi }_{\alpha }^{\prime } : {\left. E\right| }_{{U}_{\alpha }} \rightarrow  {U}_{\alpha } \times  {\mathbb{R}}^{n} \) 使得它把标架 \( {t}_{1}^{\alpha },\ldots ,{t}_{n}^{\alpha } \) 变成 \( {\mathbb{R}}^{n} \) 的标准单位正交基 \( {e}_{1},\ldots ,{e}_{n} \) . 于是 \( {g}_{\alpha \beta }^{\prime }\left( x\right) \) 把 \( {\mathbb{R}}^{n} \) 的单位正交基变为单位正交基,即 \( {g}_{\alpha \beta }^{\prime }\left( x\right)  \in  O\left( n\right) \) . 这就证明了第一个结论.

因为 \( {SO}\left( n\right)  = O\left( n\right)  \cap  G{L}^{ + }\left( {n,\mathbb{R}}\right) \) ,所以第二个结论显然成立.

补充练习 2. 在上述证明过程中,试用矩阵 \( {g}_{\alpha \beta }^{\prime } \) 表示两组单位正交标架 \( {t}_{1}^{\alpha },\ldots ,{t}_{n}^{\alpha } \) 与 \( {t}_{1}^{\beta },\ldots ,{t}_{n}^{\beta } \) 限制在 \( {U}_{\alpha \beta } \) 上的关系.

练习 6.5.

(a) 证明 \( {GL}\left( {n,\mathbb{R}}\right)  = O\left( n\right)  \times  \{ \) 正定对称矩阵 \( \} \) .

(b) 应用 (a) 通过找引理 6.1 中的 \( {\lambda }_{\alpha } \) 证明向量丛的结构群可约化到 \( O\left( n\right) \) .

向量丛上运算

设 \( E \) : 秩 \( n,\left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\}  ,\left\{  {g}_{\alpha \beta }\right\}  ;{E}^{\prime } \) : 秩 \( m,\left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }^{\prime }}\right) \right\}  ,\left\{  {g}_{\alpha \beta }^{\prime }\right\} \) .

(1)直和 \( E \oplus  {E}^{\prime } \) . 秩: \( n + m \) ，局部平凡化:

\[
{\phi }_{\alpha } \oplus  {\phi }_{\alpha }^{\prime } : {\left. \left( E \oplus  {E}^{\prime }\right) \right| }_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  \left( {{\mathbb{R}}^{n} \oplus  {\mathbb{R}}^{m}}\right) ,
\]

转移函数: \( \left( \begin{matrix} {g}_{\alpha \beta } & 0 \\  0 & {g}_{\alpha \beta }^{\prime } \end{matrix}\right) \) .

(2)张量积 \( E \otimes  {E}^{\prime } \) . 秩: \( {nm} \) ,局部平凡化:

\[
{\phi }_{\alpha } \otimes  {\phi }_{\alpha }^{\prime } : E \otimes  {E}^{\prime }\left| {}_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  \left( {\mathbb{R}}^{n} \otimes  {\mathbb{R}}^{m}\right) \right|
\]

转移函数: \( \left\{  {{g}_{\alpha \beta } \otimes  {g}_{\alpha \beta }^{\prime }}\right\} \) .

(3) \( \operatorname{Hom}\left( {E,{E}^{\prime }}\right) \) . 这是从 \( E \) 到 \( {E}^{\prime } \) 的丛映射的集合. \( \operatorname{Hom}\left( {E,{E}^{\prime }}\right)  \simeq  {E}^{ * } \otimes  {E}^{\prime } \) .

(4) \( E \) 的对偶丛 \( {E}^{ * } \) .

设 \( V \) , \( W \) 是 \( n \) 维向量空间,各自的一组基为 \( \left\{  {{v}_{1},\ldots ,{v}_{n}}\right\}  ,\left\{  {{w}_{1},\ldots ,{w}_{n}}\right\} \) . 令 \( {V}^{ * } = \; \operatorname{Hom}\left( {V,\mathbb{R}}\right) \) 是 \( V \) 的对偶空间, 它是 \( V \) 上所有线性函数的空间. 设 \( \{ {v}_{1}^{ * },\ldots ,{v}_{n}^{ * }\} \) , \( \left\{  {{w}_{1}^{ * },\ldots ,{w}_{n}^{ * }}\right\} \) 是 \( {V}^{ * },{W}^{ * } \) 的各自对偶基,即 \( {v}_{i}^{ * }\left( {v}_{j}\right)  = {\delta }_{ij},{w}_{i}^{ * }\left( {w}_{j}\right)  = {\delta }_{ij} \) .

设 \( f : V \rightarrow  W \) 是线性映射, \( f\left( {v}_{i}\right)  = \sum {f}_{ij}{w}_{j}.f \) 诱导了线性映射 \( {f}^{ * } : {W}^{ * } \rightarrow  {V}^{ * } \) ,

\[
\left( {{f}^{ * }{w}^{ * }}\right) \left( v\right)  = {w}^{ * }\left( {f\left( v\right) }\right) .
\]

于是

\[
\left( {{f}^{ * }{w}_{i}^{ * }}\right) \left( {v}_{j}\right)  = {w}_{i}^{ * }\left( {f\left( {v}_{j}\right) }\right)  = {w}_{i}^{ * }\left( {\sum {f}_{jk}{w}_{k}}\right)  = {f}_{ji} = \sum {f}_{ki}{v}_{k}^{ * }\left( {v}_{j}\right) ,
\]

即

\[
{f}^{ * }{w}_{i}^{ * } = \sum {f}_{ji}{v}_{j}^{ * }.
\]

这就是说, \( {f}^{ * } \) 在给定的基下的表示矩阵是 \( f \) 的表示矩阵的转置. 我们用 \( {f}^{t} \) 来记 \( {f}^{ * } \) .

相对于 \( E \) 的局部平凡化

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  {\mathbb{R}}^{n}
\]

对偶丛 \( {E}^{ * } \) 的局部平凡化是

\[
{\left( {\phi }_{\alpha }^{t}\right) }^{-1} : {\left. {E}^{ * }\right| }_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  {\left( {\mathbb{R}}^{n}\right) }^{ * }.
\]

于是 \( {E}^{ * } \) 的转移函数是

\[
{\left( {\phi }_{\alpha }^{t}\right) }^{-1} \circ  {\phi }_{\beta }^{t} = {\left( {\left( {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1}\right) }^{t}\right) }^{-1} = {\left( {g}_{\alpha \beta }^{t}\right) }^{-1}.
\]

(5) 拉回丛. 设 \( \pi  : E \rightarrow  M \) 是向量丛, \( f : N \rightarrow  M \) 是光滑映射. 则可构造向量丛 \( \pi  : {f}^{-1}E \rightarrow  N \) ,称为 \( E \) 由 \( f \) 的拉回丛. 作为集合

\[
{f}^{-1}E = \{ \left( {y, e}\right)  \mid  f\left( y\right)  = \pi \left( e\right) \}  \subset  N \times  E.
\]

它是 \( N \times  E \) 的使得以下图表可交换的唯一最大子集:

![bo_d7e85t491nqc73eqefm0_152_943_741_443_339_0.jpg](images/fu_algebraic_topology_and_differential_forms_011_bod7e85t491nqc73eqefm01529437414433390.jpg)

\( {f}^{-1}E \) 在点 \( y \in  N \) 的纤维

\[
{\left( {f}^{-1}E\right) }_{y} \simeq  {E}_{f\left( y\right) }.
\]

这就是说, \( {\left( {f}^{-1}E\right) }_{y} \) 的向量空间结构由 \( {E}_{f\left( y\right) } \) 的向量空间结构诱导. 因为乘积丛的拉回是乘积丛,所以 \( {f}^{-1}E \) 是可局部平凡化的,因此是向量丛.

注记 6.7. 设 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( E \) 的局部平凡化. 则 \( {f}^{-1}E \) 的局部平凡化是 \( \left\{  \left( {{f}^{-1}\left( {U}_{\alpha }\right) ,{\psi }_{\alpha }}\right) \right\} \) ,其中 \( {\psi }_{\alpha } \) 定义为

\[
{\left. {f}^{-1}E\right| }_{{f}^{-1}\left( {U}_{\alpha }\right) }\overset{{\psi }_{\alpha }}{ \rightarrow  }{f}^{-1}\left( {U}_{\alpha }\right)  \times  {\mathbb{R}}^{n}
\]

\[
\left( {y, e}\right) \; \mapsto  \;\left( {y,{\left. {\phi }_{\alpha }\right| }_{{E}_{f\left( y\right) }}\left( e\right) }\right)
\]

此处 \( {\left. \phi \alpha \right| }_{{E}_{f}\left( y\right) } \) 理解为

\[
{E}_{f\left( y\right) } \rightarrow  \{ f\left( y\right) \}  \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}.
\]

于是 \( {f}^{-1}E \) 的转移函数为

\[
{g}_{\alpha \beta }^{\prime }\left( y\right)  = {\left. {\phi }_{\alpha }\right| }_{{E}_{f}\left( y\right) } \circ  {\left( {\left. {\phi }_{\beta }\right| }_{{E}_{f}\left( y\right) }\right) }^{-1}
\]

\[
= {\left. \left( {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1}\right) \right| }_{f\left( y\right) }
\]

\[
= {g}_{\alpha \beta }\left( {f\left( y\right) }\right)
\]

\[
= \left( {{f}^{ * }{g}_{\alpha \beta }}\right) \left( y\right) .
\]

所以 \( {f}^{-1}E \) 的转移函数是 \( {f}^{ * }{g}_{\alpha \beta } \) .

设 \( f : {M}^{\prime } \rightarrow  M, g : {M}^{\prime \prime } \rightarrow  {M}^{\prime } \) 是光滑映射, \( \pi  : E \rightarrow  M \) 是光滑向量丛. 则

\[
{\left( f \circ  g\right) }^{-1}E = {g}^{-1}\left( {{f}^{-1}E}\right) .
\]

这是因为这两个丛的转移函数都是

\[
{\left( f \circ  g\right) }^{ * }{g}_{\alpha \beta } = {g}^{ * }{f}^{ * }{g}_{\alpha \beta }.
\]

设 \( {\operatorname{Vect}}_{k}\left( M\right) \) 是 \( M \) 上秩 \( k \) 实向量丛的同构类的集合. 它以 \( M \) 上秩 \( k \) 平凡丛的同构类为基点. 对光滑映射 \( f : M \rightarrow  N \) ,设 \( {\operatorname{Vect}}_{k}\left( f\right)  = {f}^{-1} \) 是向量丛的拉回. 因为平凡丛的拉回丛是平凡丛,所以若 \( f : M \rightarrow  N \) 是光滑映射,则

\[
{f}^{-1} : {\operatorname{Vect}}_{k}\left( N\right)  \rightarrow  {\operatorname{Vect}}_{k}\left( M\right)
\]

是保基点的映射. 这样,对每个整数 \( k \) , \( {\mathsf{{Vect}}}_{k}\left(  \right) \) 成为一个从流形与光滑映射的范畴到带基点集合与保基点映射的范畴的反变函子.

向量丛的同伦性向量丛拉回的基本性质是以下定理. 事实上,当 \( Y \) 非紧时定理仍成立. 它的一个推论是可缩空间上的向量丛是平凡丛, 这在 Thom 同构的证明中是必需的.

定理 6.8.(向量丛的同伦性质)假定 \( Y \) 是紧流形. 若 \( {f}_{0},{f}_{1} : Y \rightarrow  X \) 同伦且 \( \pi  : E \rightarrow  X \) 是向量丛,则 \( {f}_{0}^{-1}E \) 同构于 \( {f}_{1}^{-1}E \) ,即同伦映射诱导了同构丛.

证. 空间 \( B \) 上两个秩 \( k \) 向量丛 \( V \) 与 \( W \) 之间同构的构造问题可转化为在 \( B \) 的一个纤维丛上构造截面的问题.

回忆 \( \operatorname{Hom}\left( {V, W}\right)  = {V}^{ * } \otimes  W \) 是 \( B \) 上向量丛,它在点 \( x \) 的纤维由所有从 \( {V}_{x} \) 到 \( {W}_{x} \) 的线性映射组成. 构造 \( \operatorname{Hom}\left( {V, W}\right) \) 的纤维子丛 \( \operatorname{Iso}\left( {V, W}\right) \) : 它在每点 \( x \) 的纤维由所有从 \( {V}_{x} \) 到 \( {W}_{x} \) 的线性同构组成,即它的纤维同构于 \( {GL}\left( {k,\mathbb{R}}\right) \) ; 并且 \( \operatorname{Iso}\left( {V, W}\right) \) 作为 \( \operatorname{Hom}\left( {V, W}\right) \) 的子集从 \( \operatorname{Hom}\left( {V, W}\right) \) 继承一个拓扑. 显然 \( V \) 与 \( W \) 之间的一个同构恰好是 \( \operatorname{Iso}\left( {V, W}\right) \) 的一个截面.

设 \( f : Y \times  I \rightarrow  X \) 是 \( {f}_{0} \) 与 \( {f}_{1} \) 之间的同伦映射,设 \( \pi  : Y \times  I \rightarrow  Y \) 是投射. 对 \( y \in  Y, t \in  I \) ,记 \( {f}_{t}\left( y\right)  = f\left( {y, t}\right) \) . 我们先证明: 对任意给定 \( {t}_{0} \in  I \) ,对 \( {t}_{0} \) 附近的每个 \( t,{f}_{t}^{-1}E \simeq  {f}_{{t}_{0}}^{-1}E \) .

令 \( F = {f}_{{t}_{0}}^{-1}E \) . 在 \( Y \times  I \) 上有两个拉回丛 \( {f}^{-1}E \) 与 \( {\pi }^{-1}F \) :

![bo_d7e85t491nqc73eqefm0_156_647_668_1043_342_0.jpg](images/fu_algebraic_topology_and_differential_forms_012_bod7e85t491nqc73eqefm015664766810433420.jpg)

因为

\[
{\left. {f}^{-1}E\right| }_{Y \times  \left\{  {t}_{0}\right\}  } \simeq  {f}_{{t}_{0}}^{-1}E = F \simeq  {\pi }^{-1}{\left. F\right| }_{Y \times  \left\{  {t}_{0}\right\}  },
\]

所以纤维丛

\[
{\left. \operatorname{Iso}\left( {f}^{-1}E,{\pi }^{-1}F\right) \right| }_{Y \times  \left\{  {t}_{0}\right\}  }
\]

有截面 \( s\left( {t}_{0}\right) \) . 由于 \( Y \) 紧,存在充分小的 \( {\epsilon }_{0} > 0 \) 使得 \( s\left( {t}_{0}\right) \) 可延拓为以下纤维丛的一个截面 \( s\left( t\right) \) , \( t \in  O\left( {{t}_{0},{\epsilon }_{0}}\right)  = \left( {{t}_{0} - {\epsilon }_{0},{t}_{0} + {\epsilon }_{0}}\right)  \cap  I \)

\[
{\left. \operatorname{Iso}\left( {f}^{-1}E,{\pi }^{-1}F\right) \right| }_{Y \times  O\left( {{t}_{0},{\epsilon }_{0}}\right) }\text{ . }
\]

所以对这样的 \( t \) ，

\[
{f}_{t}^{-1}E \simeq  {f}^{-1}{\left. E\right| }_{Y\times \{ t\} } \simeq  {\pi }^{-1}{\left. F\right| }_{Y\times \{ t\} } \simeq  F = {f}_{{t}_{0}}^{-1}E.
\]

这就是说,对任意的 \( {t}_{0} \in  I \) ,存在 \( {\epsilon }_{0} > 0 \) ,使得对任意的 \( {t}^{\prime },{t}^{\prime \prime } \in  O\left( {{t}_{0},{\epsilon }_{0}}\right) \) ,

\[
{f}_{{t}^{\prime }}^{-1}E \simeq  {f}_{{t}^{\prime \prime }}^{-1}E \tag{5}
\]

由 \( {t}_{0} \in  I \) 的任意性, \( I \) 的连通性与紧性,存在 \( I \) 中有限多个点 \( {t}_{1} < \cdots  < {t}_{n} \) 与相应的 \( {\epsilon }_{1} > 0,\ldots ,{\epsilon }_{n} > 0 \) 使得 \( {\left\{  O\left( {t}_{i},{\epsilon }_{i}\right) \right\}  }_{1 \leq  i \leq  n} \) 覆盖 \( I \) ,且对任意的 \( {t}^{\prime },{t}^{\prime \prime } \in  O\left( {{t}_{i},{\epsilon }_{i}}\right) \) , (5)成立. 于是

\[
{f}_{0}^{-1}E \simeq  {f}_{{t}_{1}^{\prime }}^{-1}E \simeq  {f}_{{t}_{2}^{\prime }}^{-1}E \simeq  \cdots  \simeq  {f}_{{t}_{n - 1}^{\prime }}^{-1}E \simeq  {f}_{1}^{-1}E,
\]

其中 \( {t}_{i}^{\prime } \in  O\left( {{t}_{i},{\epsilon }_{i}}\right)  \cap  O\left( {{t}_{i + 1},{\epsilon }_{i + 1}}\right) \) . 注记. 若 \( Y \) 非紧,也许不能找到 \( \epsilon  > 0 \) 使得 \( \operatorname{Iso}\left( {{f}^{-1}E,{f}^{-1}F}\right) \) 限制在如左下图的常宽的带状 \( Y \times  \left( {{t}_{0} - \epsilon ,{t}_{0} + \epsilon }\right) \) 有截面；带状看起来可能如右下图所示.

![bo_d7e85t491nqc73eqefm0_158_260_434_1763_454_0.jpg](images/fu_algebraic_topology_and_differential_forms_013_bod7e85t491nqc73eqefm015826043417634540.jpg)

但是相同的讨论能被改进使得定理对 \( Y \) 是仿紧空间也成立. 例如可参看 Husemoller [1]. \( Y \) 是仿紧的若 \( Y \) 的每个开覆盖 \( \mathcal{U} \) 有一个局部有限的加细 \( {\mathcal{U}}^{\prime } \) ,即 \( Y \) 中每点有一个只与 \( {\mathcal{U}}^{\prime } \) 中有限多个开集相交的邻域. 显然紧空间或离散空间是仿紧的. 根据 A. H. Stone 的一个定理, 度量空间是仿紧的. 对我们来说更重要的是每个流形是仿紧的. 这样向量丛的同伦性质, 即定理 6.8 对任意紧或非紧流形 \( Y \) 都成立.

定理 6.8’. 假定 \( Y \) 是流形. 若 \( {f}_{0},{f}_{1} : Y \rightarrow  X \) 同伦且 \( \pi  : E \rightarrow  X \) 是向量丛,则 \( {f}_{0}^{-1}E \) 与 \( {f}_{1}^{-1}E \) 同构. 这就是说,同伦映射诱导同构丛.

推论 6.9. 可缩流形上向量丛是平凡的. 证. 由于 \( M \) 可缩,存在映射 \( f : M \rightarrow \) point 与 \( g : \) point \( \rightarrow  M \) 使得 \( g \circ  f \simeq  {\mathsf{{id}}}_{M} \) . 设 \( E \) 是 \( M \) 上一个向量丛. 由向量丛的同伦性得到

\[
E \simeq  {\left( g \circ  f\right) }^{-1}E \simeq  {f}^{-1}\left( {{g}^{-1}E}\right) .
\]

因为 \( {g}^{-1}E \) 是一个点上的向量丛,它是平凡的,所以 \( {f}^{-1}\left( {{g}^{-1}E}\right) \) 也是平凡的. 所以对可缩流形 \( M \) , \( {\operatorname{Vect}}_{k}\left( M\right)  = 0 \) .

练习 6.10. 计算 \( {\operatorname{Vect}}_{k}\left( {S}^{1}\right) \) .

作业:

1. 练习 6.2.

2. 补充练习 1.

3. 补充练习 2.

4. 练习 6.5.

代数拓扑与微分形式
