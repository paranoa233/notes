#### 第14讲 Sphere Bundles (1)

§11 Sphere Bundles (1)

14. 球面丛

设 \( \pi  : E \rightarrow  M \) 是秩 \( \left( {n + 1}\right) \) 向量丛. \( E \) 上给定一个度量 \( \langle \) , \( \rangle .\text{ サ } \) . 对 \( E \) 的每条纤维 \( {E}_{x} \) 上每个向量 \( v \) ,定义

\[
{r}^{2}\left( v\right)  = \langle v, v\rangle .
\]

置

\[
S{\left( E\right) }_{x} = \left\{  {v \in  {E}_{x} \mid  r\left( v\right)  = 1}\right\}   \simeq  {S}^{n},\;x \in  M;
\]

\[
S\left( E\right)  = \mathop{\coprod }\limits_{{x \in  M}}S{\left( E\right) }_{x}
\]

则 \( S\left( E\right) \) 是 \( M \) 上纤维为 \( {S}^{n} \) 的纤维丛,它的结构群是 \( O\left( {n + 1}\right) \) .

把纤维为球面 \( {S}^{n} \) 的纤维丛称为 \( n \) 维球面丛或 \( {S}^{n} \) -丛. 它的结构群是 \( {S}^{n} \) 的微分同胚群 \( \operatorname{Diff}\left( {S}^{n}\right) \) . 上述由向量丛定义的球面丛的结构群是 \( O\left( {n + 1}\right) \) ,它是 \( \operatorname{Diff}\left( {S}^{n}\right) \) 的子群. 但是有例子表明球面丛的结构群不是总能约化到正交群 \( O\left( {n + 1}\right) \) ,即球面丛不一定是由某个向量丛定义的, 这是存在拓扑障碍的.

现设 \( \pi  : E \rightarrow  M \) 是 \( n \) 维球面丛, \( n \geq  1 \) . 根据 Leray-Hirsch 定理,若在 \( E \) 上存在一个闭的整体 \( n \) -形式，它到每条纤维的限制生成纤维的上同调，则 \( E \) 的上同调是

\[
{H}^{ * }\left( E\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( {S}^{n}\right) .
\]

因此一个自然的问题是何时这种整体形式存在. 第 6 节在定向平面丛上已构造整体角形式 \( \psi \) ，它具有以下两个性质:

(a) \( \psi \) 限制在每条纤维是角形式 \( \frac{1}{2\pi }{d\theta } \) ;

(b) \( {d\psi } =  - {\pi }^{ * }e \) ,其中 \( e \) 是欧拉类.

相同的过程可定义结构群为 \( {SO}\left( 2\right) \) 的圆周丛的角形式与欧拉类. 因此,若这种丛的欧拉类为零,则整体角形式 \( \psi \) 是闭的且满足 Leray-Hirsch 定理的条件.

更一般地考虑结构群为 \( \operatorname{Diff}\left( {S}^{n}\right) \) 或 \( O\left( {n + 1}\right) \) 的球面丛,我们将看到存在上述整体形式需克服两个障碍:可定向性与欧拉类.

- 可定向性

- 欧拉类

- 整体角形式

可定向性设 \( \pi  : E \rightarrow  M \) 是 \( n \) 维球面丛, \( n \geq  1 \) . 在这节假定 \( M \) 是连通的. 设 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( M \) 的好覆盖. 因为 \( {\left. E\right| }_{{U}_{\alpha }} \) 微分同胚于 \( {U}_{\alpha } \times  {S}^{n} \) ,所以 \( \dim {H}^{n}\left( {\left. E\right| }_{{U}_{\alpha }}\right)  = 1 \) . 设 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) 是 \( {H}^{n}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) 的一个生成元. 先验地,

\[
{\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{{\left. E\right| }_{{U}_{\alpha \beta }}} =  \pm  {\left\lbrack  {\sigma }_{\beta }\right\rbrack  }_{{\left. E\right| }_{{U}_{\alpha \beta }}}.
\]

定义. 若对任意的 \( \alpha  \in  I \) ,存在 \( {H}^{n}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) 的生成元 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) 使得

\[
\left\lbrack  {\sigma }_{\alpha }\right\rbrack  {\left| {}_{E}\right| }_{{U}_{\alpha \beta }} = {\left\lbrack  {\sigma }_{\beta }\right\rbrack  }_{{\left. E\right| }_{{U}_{\alpha \beta }}}, \tag{29}
\]

则称 \( E \) 是可定向的.

它等价于对每条纤维 \( {E}_{x} \) ,可选取 \( {H}^{n}\left( {E}_{x}\right) \) 的生成元 \( \left\lbrack  {\sigma }_{x}\right\rbrack \) 满足以下的局部相容性条件: \( M \) 的每点有一个邻域 \( U \) 与 \( {H}^{n}\left( {\left. E\right| }_{U}\right) \) 的一个生成元 \( \left\lbrack  {\sigma }_{U}\right\rbrack \) 使得对任意的 \( x \in  U \) , \( {\left. \left\lbrack  {\sigma }_{U}\right\rbrack  \right| }_{{E}_{x}} = \left\lbrack  {\sigma }_{x}\right\rbrack  . \) 相容性条件 (29) 等价于

\[
{\left. {\sigma }_{\beta }\right| }_{{\left. E\right| }_{{U}_{\alpha \beta }}} - {\left. {\sigma }_{\alpha }\right| }_{{\left. E\right| }_{{U}_{\alpha \beta }}} = d{\sigma }_{\alpha \beta },\;{\sigma }_{\alpha \beta } \in  {\Omega }^{n - 1}\left( {\left. E\right| }_{{U}_{\alpha \beta }}\right) . \tag{30}
\]

这是讨论球面丛欧拉类的出发点.

对可定向球面丛，有两组相容的生成元，选定一组就给球面丛一个定向. 给定一个定向的可定向球面丛称为定向球面丛. 流形 \( M \) 上一个 \( {S}^{0} \) -丛是 \( M \) 的二重覆盖. 如果 \( M \) 是连通的,这种丛是可定向的当且仅当它有两个连通分支.

在第 6 节中称秩 \( \left( {n + 1}\right) \) 向量丛是可定向的当且仅当它的结构群可约化到 \( {SO}(n + \) 1). 现研究向量丛 \( E \) 的可定向性与它的球面丛 \( S\left( E\right) \) 的可定向性之间的关系.

注记 11.1. 固定 \( {S}^{n} \) 的一个定向. 设 \( \left\lbrack  \sigma \right\rbrack   \in  {H}^{n}\left( {S}^{n}\right) \) 是生成元满足 \( {\int }_{{S}^{n}}\sigma  = 1 \) . 若 \( g \in  {SO}\left( {n + 1}\right) \) ,则像 \( g\left( {S}^{n}\right) \) 是球面 \( {S}^{n} \) 并具有相同的定向. 所以

\[
{\int }_{{S}^{n}}{g}^{ * }\sigma  = {\int }_{g\left( {S}^{n}\right) }\sigma  = {\int }_{{S}^{n}}\sigma  = 1.
\]

这样,对正交变换 \( g,{g}^{ * }\sigma \) 与 \( \sigma \) 表示相同的上同调类当且仅当 \( g \) 的行列式为正.

命题 11.2. 向量丛 \( E \) 是可定向的当且仅当它的球面丛 \( S\left( E\right) \) 是可定向的. 证. 在 \( E \) 上给一个度量. 给 \( E \) 一个局部平凡化 \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) 使得每个 \( {\phi }_{\alpha } \) 限制在纤维是保内积的,见命题 6.4 的证明. 所以它的转移函数 \( {g}_{\alpha \beta } \) 在 \( O\left( {n + 1}\right) \) 中取值并诱导了球面丛 \( S\left( E\right) \) 的一个局部平凡化 \( \left\{  \left( {{U}_{\alpha },{\varphi }_{\alpha }}\right) \right\} \) :

![bo_d7e85t491nqc73eqefm0_313_783_543_752_359_0.jpg](images/fu_algebraic_topology_and_differential_forms_050_bod7e85t491nqc73eqefm03137835437523590.jpg)

所以 \( S\left( E\right) \) 的结构群也是 \( {g}_{\alpha \beta } \) . 注意 \( {\varphi }_{\alpha } \) 是 \( {\phi }_{\alpha } \) 在 \( {\left. S\left( E\right) \right| }_{{U}_{\alpha }} \) 的限制.

设 \( {\rho }_{\alpha } : {U}_{\alpha } \times  {S}^{n} \rightarrow  {S}^{n} \) 是投射. 设 \( \left\lbrack  \sigma \right\rbrack   \in  {H}^{n}\left( {S}^{n}\right) \) 是生成元且 \( {\int }_{{S}^{n}}\sigma  = 1 \) . 定义

\[
\left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {{\varphi }_{\alpha }^{ * }{\rho }_{\alpha }^{ * }\sigma }\right\rbrack   \in  {H}^{n}\left( {\left. S\left( E\right) \right| }_{{U}_{\alpha }}\right) . \tag{31}
\]

为简单计,把 \( {\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{{E}_{x}} \) 简记为 \( {\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{x} \) ,把 \( {\left. {\varphi }_{\alpha }\right| }_{{E}_{x}} \) 简记为 \( {\left. {\varphi }_{\alpha }\right| }_{x} \) ,而把 \( \left( {{\rho }_{\alpha } \circ  {\varphi }_{\alpha }}\right) { \mid  }_{{E}_{x}} \) 简记为 \( {\left. {\psi }_{\alpha }\right| }_{x} \) . 于是对 \( {U}_{\alpha } \) 中的点 \( x \) ,将等式 (31) 限制在纤维 \( {E}_{x} \) 上,得到

\[
\left\lbrack  {\sigma }_{\alpha }\right\rbrack  {|}_{x} = \left\lbrack  {\left. {\sigma }_{\alpha }\right| }_{x}\right\rbrack   = {\left( {\left. {\psi }_{\alpha }\right| }_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack  .
\]

于是对任意 \( x \in  {U}_{\alpha \beta } \) ,

\[
\left\lbrack  {\sigma }_{\alpha }\right\rbrack  {\left| {}_{x} = \left\lbrack  {\sigma }_{\beta }\right\rbrack  \right| }_{x}
\]

\[
\Leftrightarrow  {\left( {\psi }_{\alpha }{|}_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack   = {\left( {\psi }_{\beta }{|}_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack
\]

\[
\Leftrightarrow  \left\lbrack  \sigma \right\rbrack   = {\left( {\left( {\psi }_{\beta }{|}_{x}\right) }^{ * }\right) }^{-1}{\left( {\psi }_{\alpha }{|}_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack
\]

\[
\Leftrightarrow  \left\lbrack  \sigma \right\rbrack   = {\left( {\varphi }_{\alpha }{|}_{x} \circ  {\left( {\varphi }_{\beta }{|}_{x}\right) }^{-1}\right) }^{ * }\left\lbrack  \sigma \right\rbrack
\]

\[
\Leftrightarrow  \left\lbrack  \sigma \right\rbrack   = {g}_{\alpha \beta }{\left( x\right) }^{ * }\left\lbrack  \sigma \right\rbrack  \text{ . }
\]

先证充分性. 若 \( E \) 可定向,给 \( E \) 平凡化使得 \( {g}_{\alpha \beta }\left( x\right)  \in  {SO}\left( {n + 1}\right) \) . 由注 11.1 知 \( \left\lbrack  \sigma \right\rbrack   = {g}_{\alpha \beta }{\left( x\right) }^{ * }\left\lbrack  \sigma \right\rbrack \) . 因此 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack  {\left| {}_{x} = \left\lbrack  {\sigma }_{\beta }\right\rbrack  \right| }_{x} \) ,即 \( S\left( E\right) \) 是可定向的.

再证必要性. 设球面丛 \( S\left( E\right) \) 可定向. 设 \( {\left\{  \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right\}  }_{\alpha  \in  I} \) 是球面丛 \( S\left( E\right) \) 的一个定向*. 则由 \( \left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| x = {\left. \left\lbrack  {\sigma }_{\beta }\right\rbrack  \right| }_{x} \) 可得 \( \left\lbrack  \sigma \right\rbrack   = {g}_{\alpha \beta }{\left( x\right) }^{ * }\left\lbrack  \sigma \right\rbrack \) . 于是由注 11.1 知 \( {g}_{\alpha \beta }\left( x\right)  \in \; {SO}\left( {n + 1}\right) \) . 因此 \( E \) 是可定向的.

*给定的向量丛 \( E \) 的局部平凡化的开覆盖与 \( S\left( E\right) \) 的定向的开覆盖一般是不一样的,但我们总可以假定它们是一样的.

注记 11.3. 因为 \( {SO}\left( 1\right)  = \{ 1\} \) ,连通流形 \( M \) 上线丛 \( \pi  : L \rightarrow  M \) 是可定向的当且仅当它是平凡的. 此时球面丛 \( S\left( L\right) \) 有两个连通分支.

命题 11.4. 向量丛 \( E \) 可定向当且仅当它的行列式丛 \( \det E \) 可定向.

证. 设 \( \left\{  {g}_{\alpha \beta }\right\} \) 是 \( E \) 的局部平凡化的转移函数. 则 \( \left\{  {\det {g}_{\alpha \beta }}\right\} \) 是 \( \det E \) 的相应局部平凡化的转移函数. 正交矩阵 \( {g}_{\alpha \beta } \) 属于 \( {SO}\left( {n + 1}\right) \) 当且仅当 \( \det {g}_{\alpha \beta } > 0 \) ,所以命题成立.

不论 \( E \) 是否可定向, 0-球面丛 \( S\left( {\det E}\right) \) 是 \( M \) 的二重覆盖,结合注 11.3 与命题 11.4 可知连通流形上向量丛 \( E \) 可定向当且仅当 \( S\left( {\det E}\right) \) 不是连通的. 因为单连通流形不可能有重数大于 1 的连通覆盖空间, 所以有以下命题.

命题 11.5. 单连通流形上每个向量丛是可定向的.

推论 11.6. 单连通流形是可定向的.

定向球面丛的欧拉类设 \( \pi  : E \rightarrow  M \) 是 \( {S}^{n} \) -丛, \( \mathcal{U} = \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) 是 \( M \) 的好覆盖. \( E \) 是可定向的当且仅当存在 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   \in  {H}^{n}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) 使得 (30) 成立,即

\[
{\left. {\sigma }_{\beta }\right| }_{{\left. E\right| }_{{U}_{\alpha \beta }}} - {\left. {\sigma }_{\alpha }\right| }_{{\left. E\right| }_{{U}_{\alpha \beta }}} = d{\sigma }_{\alpha \beta },\;{\sigma }_{\alpha \beta } \in  {\Omega }^{n - 1}\left( {\left. E\right| }_{{U}_{\alpha \beta }}\right) .
\]

这些 \( {\sigma }_{\alpha } \) 定义了一个 0-上链 (0-cochain)

\[
{\sigma }^{0, n} = \left( {{\sigma }_{\alpha },{\sigma }_{\beta },\ldots }\right)  \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n}}\right) ;
\]

而 \( {\sigma }_{\alpha \beta } \) 定义了一个 1-上链

\[
{\sigma }^{1, n - 1} = \left( {{\sigma }_{\alpha \beta },{\sigma }_{\alpha \gamma },\ldots }\right)  \in  {C}^{1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n - 1}}\right) .
\]

上链 \( {\sigma }^{0, n} \) 与 \( {\sigma }^{1, n - 1} \) 满足

\[
d{\sigma }^{0, n} = 0
\]

\[
\delta {\sigma }^{0, n} = d{\sigma }^{1, n - 1} =  - {D}^{\prime \prime }{\sigma }^{1, n - 1}.
\]

![bo_d7e85t491nqc73eqefm0_316_1213_1188_956_516_0.jpg](images/fu_algebraic_topology_and_differential_forms_051_bod7e85t491nqc73eqefm0316121311889565160.jpg)

换句话说, \( {S}^{n} \) -丛 \( E \) 可定向当且仅当存在一个 0 -上链 \( {\sigma }^{0, n} \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n}}\right) \) , 它在可能变为一个 \( D \) -上闭链的路上向前迈出了一步.

走出第一步之后就可继续往前走了. 事实上，因为 \( \mathcal{U} \) 是好覆盖，所以当 \( 0 < i < n \) 时, 由 Künneth 公式可得

\[
{H}^{i}\left( {{U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \times  {S}^{n}}\right)  = 0,
\]

或

\[
{H}_{d}^{i}\left\{  {{C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}   = 0. \tag{32}
\]

因为

\[
d\left( {\delta {\sigma }^{1, n - 1}}\right)  = {\delta d}{\sigma }^{1, n - 1} = {\delta }^{2}{\sigma }^{0, n} = 0,
\]

由(32)知存在 \( {\sigma }^{2, n - 2} \in  {C}^{2}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n - 2}}\right) \) 使得

\[
\delta {\sigma }^{1, n - 1} =  - d{\sigma }^{2, n - 2} =  - {D}^{\prime \prime }{\sigma }^{2, n - 2}.
\]

继续如此操作,直到存在 \( {\sigma }^{n,0} \in  {C}^{n}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{0}}\right) \) 使得

\[
\delta {\sigma }^{n - 1,1} = {\left( -1\right) }^{n + 1}d{\sigma }^{n,0} =  - {D}^{\prime \prime }{\sigma }^{n,0}.
\]

令

\[
\sigma  = {\sigma }^{0, n} + {\sigma }^{1, n - 1} + \cdots  + {\sigma }^{n,0}.
\]

则由构造知

\[
{D\sigma } = {D}^{\prime \prime }{\sigma }^{0, n} + \left( {\delta {\sigma }^{0, n} + {D}^{\prime \prime }{\sigma }^{1, n - 1}}\right)  + \cdots  + \left( {\delta {\sigma }^{n - 1,1} + {D}^{\prime \prime }{\sigma }^{n,0}}\right)  + \delta {\sigma }^{n,0}
\]

\[
= \delta {\sigma }^{n,0}\text{ . }
\]

因为

\[
d\left( {\delta {\sigma }^{n,0}}\right)  = {\delta d}{\sigma }^{n,0} =  \pm  {\delta }^{2}{\sigma }^{n - 1,1} = 0,
\]

即 \( \delta {\sigma }^{n,0} \) 是局部常值函数，所以

\[
{D\sigma } = \delta {\sigma }^{n,0} = i\left( {-\varepsilon }\right) ,
\]

其中 \( i \) 是包含映射 \( {C}^{n + 1}\left( {{\pi }^{-1}\mathcal{U},\mathbb{R}}\right)  \rightarrow  {C}^{n + 1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{0}}\right) \) ,而

\[
\varepsilon  \in  {C}^{n + 1}\left( {{\pi }^{-1}\mathcal{U},\mathbb{R}}\right)  \simeq  {C}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right) .
\]

显然 \( {\delta \varepsilon } = 0 \) . 所以 \( \left\lbrack  \varepsilon \right\rbrack   \in  {H}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right) \) . 因为 \( \mathcal{U} \) 是好覆盖, \( {H}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right)  \simeq \; {H}_{dR}^{n + 1}\left( M\right) \) ,记 \( e\left( E\right) \) 或 \( e \) 为由 Čech 上同调类 \( \left\lbrack  \varepsilon \right\rbrack \) 所对应的 de Rham 上同调类.

\[
\exists {\sigma }^{n - 1,1}\overset{\delta }{ \rightarrow  }\begin{array}{l} \delta {\sigma }^{n - 1,1} + \\  {D}^{\prime \prime }{\sigma }^{n,0} = 0 \end{array}
\]

![bo_d7e85t491nqc73eqefm0_319_103_257_1137_695_0.jpg](images/fu_algebraic_topology_and_differential_forms_052_bod7e85t491nqc73eqefm031910325711376950.jpg)

\( {D}^{\prime \prime } \uparrow \)

\( \exists {\sigma }^{n,0} \; \delta {\sigma }^{n,0} \)

\( i \uparrow \)

\( \exists  - \varepsilon \)

定向性

\[
{H}_{d}^{i}\left\{  {{C}^{p}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) }\right\}   = 0
\]

欧拉类定义. \( e\left( E\right)  \in  {H}^{n + 1}\left( M\right) \) 称为可定向 \( {S}^{n} - \) 丛 \( E \) 的相对于定向 \( {\sigma }^{0, n} \) 的欧拉类. \( E \) 的另一定向的欧拉类为 \( - e\left( E\right) \) .

若 \( E \) 是定向向量丛, 零截面的补 \( {E}^{0} \) 与定向球面丛有相同的伦型. \( E \) 的欧拉类定义为 \( {E}^{0} \) 的欧拉类. 等价地,若给 \( E \) 一个度量,则 \( E \) 的单位球面丛 \( S\left( E\right) \) 是有意义的,定义 \( E \) 的欧拉类为 \( S\left( E\right) \) 的欧拉类. 显然后者的定义与度量无关,并且事实上与借助 \( {E}^{0} \) 的定义相等, 因为对 \( E \) 的任意度量, 单位球面丛与 \( {E}^{0} \) 有相同的伦型.

回到 \( E \) 是 \( n \) -维球面丛的情形,我们证明 \( E \) 的欧拉类 \( e\left( E\right) \) 是定义好的,需证以下两个命题.

命题 11.7. 对一个给定的定向 \( \left\{  \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right\} \) ，欧拉类与 \( {\sigma }^{j, n - j} \) ， \( j = 0,1,\ldots , n \) 的选取无关.

证. 设 \( {\overline{\sigma }}^{0, n} \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n}}\right) \) 也表示定向 \( \left\{  \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right\} \) . 如法炮制有

\[
\overline{\sigma } = {\overline{\sigma }}^{0, n} + {\overline{\sigma }}^{1, n - 1} + \cdots  + {\overline{\sigma }}^{n,0}
\]

\[
D\overline{\sigma } = \delta {\overline{\sigma }}^{n,0} =  - i\left( \overline{\varepsilon }\right) .
\]

需证 \( \left\lbrack  \overline{\varepsilon }\right\rbrack   = \left\lbrack  \varepsilon \right\rbrack \) .

因为 \( {\sigma }^{0, n} \) 与 \( {\overline{\sigma }}^{0, n} \) 表示相同的定向,所以

\[
{\overline{\sigma }}^{0, n} - {\sigma }^{0, n} = d{\tau }^{n - 1},\;{\tau }^{n - 1} \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n - 1}}\right) .
\]

又因为

\[
d\left( {\delta {\tau }^{n - 1}}\right)  = {\delta d}{\tau }^{n - 1} = \delta \left( {{\overline{\sigma }}^{0, n} - {\sigma }^{0, n}}\right)  = d\left( {{\overline{\sigma }}^{1, n - 1} - {\sigma }^{1, n - 1}}\right) ,
\]

所以

\[
\delta {\tau }^{n - 1} - \left( {{\overline{\sigma }}^{1, n - 1} - {\sigma }^{1, n - 1}}\right)  = d{\tau }^{n - 2},\;{\tau }^{n - 2} \in  {C}^{1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n - 2}}\right) .
\]

如法炮制，最终可得

\[
\delta {\tau }^{1} - \left( {{\overline{\sigma }}^{n - 1,1} - {\sigma }^{n - 1,1}}\right)  = d{\tau }^{0},\;{\tau }^{0} \in  {C}^{n - 1}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{0}}\right) .
\]

因为

\[
{d\delta }{\tau }^{0} = {\delta d}{\tau }^{0} = {\delta }^{2}{\tau }^{1} - \delta \left( {{\overline{\sigma }}^{n - 1,1} - {\sigma }^{n - 1,1}}\right)  = {\left( -1\right) }^{n}d\left( {{\overline{\sigma }}^{n,0} - {\sigma }^{n,0}}\right) ,
\]

所以

\[
{\left( -1\right) }^{n}\delta {\tau }^{0} - \left( {{\overline{\sigma }}^{n,0} - {\sigma }^{n,0}}\right)  = {i\tau },\;\tau  \in  {C}^{n}\left( {{\pi }^{-1}\mathcal{U},\mathbb{R}}\right) .
\]

两边用 \( \delta \) 作用，得

\[
{i\delta \tau } =  - \delta \left( {{\overline{\sigma }}^{n,0} - {\sigma }^{n,0}}\right)  = i\overline{\varepsilon } - {i\varepsilon }
\]

或

\[
{\delta \tau } = \overline{\varepsilon } - \varepsilon .
\]

所以

\[
\left\lbrack  \overrightarrow{\varepsilon }\right\rbrack   = \left\lbrack  \varepsilon \right\rbrack   \in  {H}^{n + 1}\left( M\right) .
\]

命题 11.8. 欧拉类 \( e\left( E\right) \) 与好覆盖的选取无关. 证. 记利用好覆盖 \( \mathcal{U} \) 定义的欧拉类为 \( {e}_{\mathcal{U}} \) . 它的一个上闭链表示为 \( {\varepsilon }_{\mathcal{U}} \) . 若 \( \mathcal{V} \) 是 \( \mathcal{U} \) 的一个加细且是好覆盖,则有下列交换图:

![bo_d7e85t491nqc73eqefm0_323_530_488_1259_557_0.jpg](images/fu_algebraic_topology_and_differential_forms_053_bod7e85t491nqc73eqefm032353048812595570.jpg)

设 \( {\varepsilon }_{\mathcal{U}} \) 由 \( {\sigma }^{0, n} \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n}}\right) \) 出发计算得到. 则 \( {\varepsilon }_{\mathcal{V}} \) 由 \( {\sigma }^{0, n} \) 先限制在 \( {\pi }^{-1}\mathcal{V} \) 上再出发计算得到. 所以 \( {\varepsilon }_{\mathcal{V}} \) 是 \( {\varepsilon }_{\mathcal{U}} \in  {C}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right) \) 到 \( \mathcal{V} \) 上的限制. 这样 \( {\varepsilon }_{\mathcal{U}} \) 与 \( {\varepsilon }_{\mathcal{V}} \) 定义了相同的 Čech 上同调类, 从而定义了相同的 de Rham 上同调类.

设 \( \mathcal{U},\mathcal{V} \) 是 \( M \) 的任意两个好覆盖. 设 \( \mathcal{W} \) 是 \( \mathcal{U},\mathcal{V} \) 的公共加细且是好覆盖. 则

\[
\left\lbrack  {\varepsilon }_{\mathcal{U}}\right\rbrack   = \left\lbrack  {\varepsilon }_{\mathcal{W}}\right\rbrack   = \left\lbrack  {\varepsilon }_{\mathcal{V}}\right\rbrack
\]

现来回答这节刚开始时提出的问题. 若欧拉类 \( e\left( E\right)  \in  {H}^{n + 1}\left( M\right) \) 等于零,则它对应的 Čech 上同调类的代表元 \( \varepsilon  \in  {C}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right) \) 是一个 \( \delta \) -上边缘,即存在 \( \tau  \in  {C}^{n}\left( {\mathcal{U},\mathbb{R}}\right) \) 使得 \( \varepsilon  = {\delta \tau } \) . 因为

\[
\delta \left( {{\sigma }^{n,0} + {i\tau }}\right)  =  - {i\varepsilon } + {i\varepsilon } = 0,
\]

所以可用 \( {\sigma }^{n,0} + {i\tau } \) 来代替 \( {\sigma }^{n,0} \) . 这样, \( \delta {\sigma }^{n,0} = 0 \) ,从而 \( {D\sigma } = 0 \) . 由 collating 公式, \( \sigma \) 对应于 \( E \) 上一个整体闭 \( n \) -形式 \( \eta \) 使得 \( \left\lbrack  {\left. \eta \right| }_{E{ \mid  }_{{U}_{\alpha }}}\right\rbrack \) 就是 \( {\sigma }^{0, n} \) 中的 \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) . 于是 \( \eta \) 限制在每条纤维上是生成元. 综上所述有

球面丛 \( E \) 是可定向的且它的欧拉类为零当且仅当在 \( E \) 上存在一个限制在每条纤维上是生成元的整体闭形式.

对乘积丛 \( E \) ，因为 \( {\sigma }^{n,0} \) 是整体定义的, \( \delta {\sigma }^{n,0} = 0 \) , 所以 \( \epsilon  = 0 \) . 从这个意义上来讲, 欧拉类用来衡量定向向量丛的扭曲程度. 然而, 以下命题表明欧拉类为零的定向向量丛不一定是乘积丛.

命题 11.9. 若定向球面丛 \( E \) 有截面，则它的欧拉类为零.

证. 若 \( E \) 有截面 \( s \) ,则 \( \pi  \circ  s = \mathrm{{id}},{s}^{ * } \circ  {\pi }^{ * } = \mathrm{{id}} \) . 在欧拉类的构造中看到

\[
- {\pi }^{ * }\varepsilon  = {D\sigma }
\]

将 \( {s}^{ * } \) 作用在等式两边得到

\[
- \varepsilon  = D{s}^{ * }\sigma
\]

所以欧拉类为零.

这个命题的逆不成立. 事实上, 上同调类是一个非常“粗糙的”不变量以至于不能得到关于几何构造存在性的信息. 在 (23.16) 将证明存在欧拉类为零的球面丛, 但它不具有截面.

补充练习 1. 在第 6 节讲过定向平面丛的欧拉类是由 \( M \) 上 2-形式 \( \eta \) 定义的,其中 \( {\left. \eta \right| }_{{U}_{\alpha }} = d{\xi }_{\alpha } \) . 在这次课中定向平面丛的欧拉类是通过 Čech 上同调类 \( \left\lbrack  \varepsilon \right\rbrack   \in  {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \) 定义的. 试研究这两者之间的关系,见 P. 120.

整体角形式

设 \( \pi  : E \rightarrow  M \) 是定向 \( {S}^{n} \) -丛. 问是否存在 \( \psi  \in  {\Omega }^{n}\left( E\right) \) 使得

(a) \( \left\lbrack  {\left. \psi \right| }_{{E}_{x}}\right\rbrack   \in  {H}^{n}\left( {E}_{x}\right) \) 是生成元;

(b) \( {d\psi } =  - {\pi }^{ * }e, e \) 是欧拉类.

回忆 \( e \) 的定义. 设 \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) 是 \( M \) 的好覆盖, \( {\alpha }_{0} \in  {C}^{0}\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{n}}\right) \) 是 \( E \) 的定向. 此处为了方便用 \( {\alpha }_{i} \) 代替 \( {\sigma }^{i, n - i} \) . 则

\[
d{\alpha }_{0} = 0,\;\delta {\alpha }_{i} =  - {D}^{\prime \prime }{\alpha }_{i + 1},0 \leq  i \leq  n - 1,\;\delta {\alpha }_{n} =  - {\pi }^{ * }\varepsilon .
\]

因此,

\[
D\left( {{\alpha }_{0} + \cdots  + {\alpha }_{n}}\right)  =  - {\pi }^{ * }\varepsilon .
\]

定义欧拉类 \( e\left( E\right) \) 为

\[
\left\lbrack  \varepsilon \right\rbrack   \in  {H}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right)  \mapsto  e\left( E\right)  \in  {H}_{dR}^{n + 1}\left( M\right) .
\]

由 collating 公式,

\[
e = {\left( -1\right) }^{n + 1}{\left( {D}^{\prime \prime }K\right) }^{n + 1}\varepsilon . \tag{33}
\]

设 \( \left\{  {\rho }_{\alpha }\right\} \) 是从属于 \( \mathcal{U} \) 的单位分解. 则 \( \left\{  {{\pi }^{ * }{\rho }_{\alpha }}\right\} \) 是从属于 \( {\pi }^{-1}\mathcal{U} = \left\{  {{\pi }^{-1}\left( {U}_{\alpha }\right) }\right\} \) 的单位分解. 同伦算子 \( K \) 既定义在 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 上,也定义在 \( {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right) \) 上,它们满足以下性质.

(a) \( {\delta K} + {K\delta } = 1 \) .

(b) \( K{\pi }^{ * } = {\pi }^{ * }K \) ,这是因为

\[
{\left( K{\pi }^{ * }\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \sum \left( {{\pi }^{ * }{\rho }_{\alpha }}\right) {\left( {\pi }^{ * }\omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

\[
= {\pi }^{ * }\sum {\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

\[
= {\left( {\pi }^{ * }K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\text{ . }
\]

(c) 若 \( s : M \rightarrow  E \) 是截面,则 \( K{s}^{ * } = {s}^{ * }K \) . 此处

\[
{s}^{ * } : {C}^{ * }\left( {{\pi }^{-1}\mathcal{U},{\Omega }^{ * }}\right)  \rightarrow  {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) .
\]

练习 11.10. 证明上述结论. 令 \( \alpha  = {\alpha }_{0} + {\alpha }_{1} + \cdots  + {\alpha }_{n} \) . 则 \( {D\alpha } =  - {\pi }^{ * }\varepsilon \) . 由 collating 公式 (9.5) 知

(11.11)

\[
\psi  = f\left( \alpha \right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} + {\left( -1\right) }^{n + 1}K{\left( {D}^{\prime \prime }K\right) }^{n}\left( {-{\pi }^{ * }\varepsilon }\right)
\]

是 \( E \) 上整体定义的 \( n \) -形式,并且

\[
{d\psi } = {\left( -1\right) }^{n}{dK}{\left( {D}^{\prime \prime }K\right) }^{n}\left( {{\pi }^{ * }\varepsilon }\right)
\]

因为 \( d{\alpha }_{0} = 0 \) ，而另外的项为零是因为它们是 \( {D}^{\prime \prime } \) -恰当的

\[
=  - {\pi }^{ * }\left( {{\left( -1\right) }^{n + 1}{\left( {D}^{\prime \prime }K\right) }^{n + 1}\varepsilon }\right) \;\text{ 因为 }{\pi }^{ * }\text{ 与 }{D}^{\prime \prime }K\text{ 可交换 }
\]

(11.12)

在公式 (11.11) 中，因为项

\[
{\left( -1\right) }^{n + 1}K{\left( {D}^{\prime \prime }K\right) }^{n}\left( {-{\pi }^{ * }\varepsilon }\right)  = {\pi }^{ * }\left( {{\left( -1\right) }^{n}K{\left( {D}^{\prime \prime }K\right) }^{n}\varepsilon }\right)
\]

限制在纤维 \( {E}_{X} \) 上为零,所以整体形式 \( \psi \) 限制到每条纤维 \( {E}_{X} \) 是 \( d \) -上同调于 \( {\left. {\alpha }_{0}\right| }_{{E}_{x}} \) , 因此 \( \left\lbrack  {\left. \psi \right| }_{{E}_{x}}\right\rbrack   = \left\lbrack  {\left. {\alpha }_{0}\right| }_{{E}_{x}}\right\rbrack   \in  {H}^{n}\left( {E}_{x}\right) \) 是生成元. 球面丛 \( E \) 上整体 \( n \) - 形式 \( \psi \) 满足前面提到的性质 (a) 与 (b). \( \psi \) 称为球面丛 \( E \) 上整体角形式.

注记 11.12.1. 设 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( M \) 的开覆盖,它局部平凡化 \( n \) 维球面丛 \( E \) . 设 \( \psi \) , \( e \) 分别由 (11.11),(11.12) 定义. 则

\[
\text{ Supp }{d\psi } \subset  \bigcup {\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{n}}\right) ,\;\text{ Supp }e \subset  \bigcup {U}_{{\alpha }_{0}\ldots {\alpha }_{n}}\text{ . }
\]

证. 由 (11.12),只要证后者即可. 注意 \( \varepsilon  \in  {C}^{n + 1}\left( {\mathcal{U},\mathbb{R}}\right) \) ,即 \( \varepsilon \) 的分量 \( {\varepsilon }_{{\alpha }_{0}\ldots {\alpha }_{n + 1}} \) 是定义在 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{n + 1}} \) 上的局部常值函数. 因为 \( e = {\left( -1\right) }^{n + 1}{\left( {D}^{\prime \prime }K\right) }^{n + 1}\varepsilon \) ,根据 \( K \) 的定义,

\[
{\left. e\right| }_{{U}_{\alpha }} =  \pm  \sum {\varepsilon }_{{\alpha }_{0}\ldots {\alpha }_{n}\alpha }d{\rho }_{{\alpha }_{0}} \land  \cdots  \land  d{\rho }_{{\alpha }_{n}}.
\]

又因为 \( \operatorname{Supp}{\rho }_{{\alpha }_{i}} \subset  {U}_{{\alpha }_{i}} \) ,所以 \( \operatorname{Supp}\left( {d{\rho }_{0} \land  \cdots  \land  d{\rho }_{n}}\right)  \subset  {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \) . 于是 \( \operatorname{Supp}e \subset \; \cup  {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \)

练习 11.13. 应用整体角形式 \( \psi \) 的存在性证明命题 11.9.

作业:

1. 补充练习 1.

2. 练习 11.10.

3. 练习 11.13.
