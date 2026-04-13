#### 第08讲 The Thom Isomorphism (2)

§6 The Thom Isomorphism (2)

8. Thom 同构

除了 de Rham 上同调与紧上同调这两种不变量，对向量丛的全空间另有一种不变量，即在垂直方向具紧支集的上同调，简称紧垂直上同调. Thom 同构是关于紧垂直上同调的，它由沿纤维的积分给出. 在这节课应用 MV 方法证明定向向量丛的 Thom 同构.

- 向量丛(的全空间)的紧上同调

- 紧垂直上同调与沿纤维的积分

- Thom 同构

向量丛 (的全空间) 的紧上同调 Poincaré 引理可看作关于 \( M \) 上平凡丛 \( M \times  {\mathbb{R}}^{n} \) 的上同调的结果.

\[
{H}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  \simeq  {H}^{ * }\left( M\right)
\]

\[
{H}_{c}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

更一般地,设 \( \pi  : E \rightarrow  M \) 是秩 \( n \) 的向量丛, \( s : M \rightarrow  E \) 是零截面,它把 \( M \) 嵌入到 E. 因为 \( s\left( M\right) \) 是 \( E \) 的形变收缩,由 de Rham 上同调的同伦公理可知

\[
{H}^{ * }\left( E\right)  \simeq  {H}^{ * }\left( {s\left( M\right) }\right)  \simeq  {H}^{ * }\left( M\right) .
\]

人们自然会问对紧上同调的同构是否也成立:

(6.11)

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

例. 设 \( E \) 是开 Möbius 带,把它看作 \( {S}^{1} \) 上秩 1 向量丛. 因为 \( {H}_{c}^{2}\left( E\right)  = 0 \) , \( {H}_{c}^{1}\left( {S}^{1}\right)  = {H}^{1}\left( {S}^{1}\right)  \simeq  \mathbb{R} \) ,所以公式 (6.11) 对 Möbius 带不成立.

引理. 设 \( \pi  : E \rightarrow  M \) 是秩 \( n \) 向量丛. 若 \( E, M \) 是可定向的有限型流形*,则公式 (6.11) 成立.

证. 设 \( M \) 的维数是 \( m \) . 则

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {\left( {H}^{m + n -  * }\left( E\right) \right) }^{ * }
\]

应用 \( E \) 上Poincaré对偶,因为 \( E \) 是可定向且有限型 \( \simeq  {\left( {H}^{m + n -  * }\left( M\right) \right) }^{ * }\; \) 根据同伦公理,因为 \( s\left( M\right) \) 是 \( E \) 的形变收缩 \( \simeq  {H}_{c}^{* - n}\left( M\right) \; \) 应用 \( M \) 上 Poincaré 对偶,因为 \( M \) 可定向且是有限型.

事实上,若 \( M \) 是有限型的,则 \( E \) 也是有限型的. 设 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( M \) 的一个有限好覆盖. 由于可缩空间上的向量丛是平凡的, 所以 \( \{ E{ \mid  }_{{U}_{\alpha }}{\} }_{\alpha  \in  I} \) 是 \( E \) 的一个有限好覆盖.

对于定向性, 我们有以下引理.

*从现在开始，我们把具有有限好覆盖的流形称为有限型流形.

引理 6.12. 可定向流形 \( M \) 上一个可定向向量丛 \( E \) 作为流形也是可定向的. 证. 按流形的可定向性的定义证. 设 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( M \) 的开覆盖,使得 \( {\left\{  \left( {U}_{\alpha },{\psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( M \) 的一个定向坐标图册, \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( E \) 的定向平凡化. 它们的转移函数分别是 \( {h}_{\alpha \beta } = {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1} \) 与 \( {g}_{\alpha \beta } \) . 所以 \( {h}_{\alpha \beta } \) 的 Jacobi 矩阵 \( D{h}_{\alpha \beta } \) 的行列式是正的,矩阵 \( {g}_{\alpha \beta } \) 的行列式也是正的. 复合映射

\[
{\Psi }_{\alpha } = \left( {{\psi }_{\alpha } \times  \mathrm{{id}}}\right)  \circ  {\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }}\overset{ \sim  }{ \rightarrow  }{U}_{\alpha } \times  {\mathbb{R}}^{n}\overset{ \sim  }{ \rightarrow  }{\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}
\]

构成了 \( E \) 的坐标图册 \( {\left\{  \left( {\left. E\right| }_{{U}_{\alpha }},{\Psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) . 它的转移函数为

(6)

\[
{\Psi }_{\alpha } \circ  {\Psi }_{\beta }^{-1} : {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}
\]

\[
\left( {x, v}\right)  \mapsto  \left( {{h}_{\alpha \beta }\left( x\right) ,{g}_{\alpha \beta }\left( {{\psi }_{\beta }^{-1}\left( x\right) }\right) v}\right) ,
\]

其 Jacobi 矩阵

\[
\left( \begin{matrix} D{h}_{\alpha \beta }\left( x\right) &  * \\  0 & {g}_{\alpha \beta }\left( {{\psi }_{\beta }^{-1}\left( x\right) }\right)  \end{matrix}\right)
\]

的行列式是正的. 因此 \( E \) 作为流形是可定向的, \( {\left\{  \left( {\left. E\right| }_{{U}_{\alpha }},{\Psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是其一个定向坐标图册.

补充练习 1 . 仔细检查转移函数 \( {\Psi }_{\alpha } \circ  {\Psi }_{\beta }^{-1} \) 的定义 (6).

由上述两个引理得到

命题 6.13. 若 \( M \) 是可定向的有限型流形, \( \pi  : E \rightarrow  M \) 是秩 \( n \) 可定向向量丛,则

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

注记 6.13.1. 事实上,流形 \( M \) 的可定向性假定是多余的,见练习 6.20. 注记 6.13.2. 在流形 \( E \) 上由引理 6.12 给出的定向称为局部乘积定向.

紧垂直上同调与沿纤维的积分对向量丛存在第三种上同调. 用在垂直方向具紧支集的微分形式的复形 \( {\Omega }_{cv}^{ * }\left( E\right) \) 代替具紧支集的微分形式的复形 \( {\Omega }_{c}^{ * }\left( E\right) .E \) 上一个光滑微分形式 \( \omega \) 属于 \( {\Omega }_{cv}^{ * }\left( E\right) \) 当且仅当对 \( M \) 中每个紧集 \( K \) ,集合

\[
\text{ Supp }\omega  \cap  {\pi }^{-1}\left( K\right)
\]

是紧的. 把这种形式称为在垂直方向具紧支集的微分形式. 复形 \( {\Omega }_{cv}^{ * }\left( E\right) \) 的上同调 \( {H}_{cv}^{ * }\left( E\right) \) 称为 \( E \) 的在垂直方向具紧支集的上同调,简称紧垂直上同调.

显然当 \( M \) 紧时, \( {\Omega }_{cv}^{ * }\left( E\right)  = {\Omega }_{c}^{ * }\left( E\right) \) . 显然若 \( \omega  \in  {\Omega }_{cv}^{ * }\left( E\right) \) ,则对 \( M \) 的每点 \( x \) , Supp \( \omega  \cap  {E}_{x} \) 是紧的. 特别地,因为

\[
\operatorname{Supp}\left( {\left. \omega \right| }_{{E}_{x}}\right)  \subset  \operatorname{Supp}\omega  \cap  {E}_{x}
\]

是紧集的闭集,所以 \( \operatorname{Supp}\left( {\left. \omega \right| }_{{E}_{x}}\right) \) 是紧的. 这样,虽然在 \( {\Omega }_{cv}^{ * }\left( E\right) \) 中的微分形式不必有紧支集, 但它到每个纤维的限制具紧支集, 故可沿纤维积分.

以下设 \( E \) 是秩 \( n \) 定向向量丛. 把在平凡线丛 \( M \times  {\mathbb{R}}^{1} \) 上由公式 (4.4) 定义的沿纤维积分 \( {\pi }_{ * } \) 推广,给出更一般的沿纤维积分

\[
{\pi }_{ * } : {\Omega }_{cv}^{ * }\left( E\right)  \rightarrow  {\Omega }^{* - n}\left( M\right)
\]

它把形式的次数降低纤维的维数 \( n \) .

首先考虑平凡丛 \( E = M \times  {\mathbb{R}}^{n} \) 的情形. 设 \( {t}_{1},\ldots ,{t}_{n} \) 是纤维 \( {\mathbb{R}}^{n} \) 的坐标. \( {\Omega }_{cv}^{q}\left( E\right) \) 中的形式 \( \omega \) 是下列型 (I),型 (II) 形式的线性组合:

(I) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{k}},\;0 \leq  k \leq  n - 1 \) , (II) \( {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n},\;k = n \) ,

其中 \( \phi  \in  {\Omega }^{q - k}\left( M\right) , f\left( {x, t}\right)  \in  {\Omega }_{cv}^{0}\left( E\right)  = {C}_{cv}^{\infty }\left( E\right) \) . 映射 \( {\pi }_{ * } \) 定义为

(I) \( \mapsto  0 \) ; (II) \( \mapsto  \phi  \cdot  {\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} \) .

因为对固定的 \( x \in  M \) ,函数 \( f\left( {x, \cdot  }\right)  \in  {C}_{c}^{\infty }\left( {\mathbb{R}}^{n}\right) \) ,所以积分有意义. 接着考虑任意定向向量丛 \( E \) 的情形. 设 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是其定向平凡化. 设 \( x = \left( {{x}_{1},\ldots ,{x}_{m}}\right) , y = \left( {{y}_{1},\ldots ,{y}_{m}}\right) \) 分别是 \( {U}_{\alpha },{U}_{\beta } \) 上坐标函数, \( t = \left( {{t}_{1},\ldots ,{t}_{n}}\right) \) , \( s = \left( {{s}_{1},\ldots ,{s}_{n}}\right) \) 分别是由 \( {\phi }_{\alpha } \) , \( {\phi }_{\beta } \) 给定的 \( {\left. E\right| }_{{U}_{\alpha }},{\left. E\right| }_{{U}_{\beta }} \) 的局部平凡化的纤维坐标.

设 \( \omega  \in  {\Omega }_{cv}^{ * }\left( E\right) \) . 记 \( {\omega }_{\alpha } = {\left. \omega \right| }_{E{ \mid  }_{{U}_{\alpha }}} \in  {\Omega }_{cv}^{ * }\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) . 由于 \( {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n} \) ,所以可按平凡化的情形定义 \( {\pi }_{ * }{\omega }_{\alpha } \) : 若 \( {\omega }_{\alpha } \) 是型 (I) 的,定义 \( {\pi }_{ * }{\omega }_{\alpha } = 0 \) ; 如果 \( {\omega }_{\alpha } \) 是型 (II) 的,我们也可定义 \( {\pi }_{ * }{\omega }_{\alpha } \) ,它属于 \( {\Omega }^{* - n}\left( {U}_{\alpha }\right) \) . 问题是当 \( {U}_{\alpha \beta } \neq  \varnothing \) ,以下等式是否成立:

\[
{\pi }_{ * }{\omega }_{\alpha }\left| {{U}_{\alpha \beta } = {\pi }_{ * }{\omega }_{\beta }}\right| {U}_{\alpha \beta }. \tag{7}
\]

如果等式成立,则 \( {\left\{  {\pi }_{ * }{\omega }_{\alpha }\right\}  }_{\alpha  \in  I} \) 可拼成 \( M \) 上一个微分形式,记作 \( {\pi }_{ * }\omega \) . 这就是型 (II) \( \omega \) 沿纤维积分的定义. 现在说明等式(7)成立. 其实，若设

\[
{\omega }_{\alpha } = {\pi }^{ * }{\phi }_{\alpha } \land  {f}_{\alpha }\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n}
\]

\[
{\omega }_{\beta } = {\pi }^{ * }{\phi }_{\beta } \land  {f}_{\beta }\left( {y, s}\right) d{s}_{1} \land  \cdots  \land  d{s}_{n}
\]

因为给定的向量丛 \( E \) 的平凡化是一个定向平凡化, \( \det {g}_{\alpha \beta } > 0 \) ,所以等式 (7) 可由重积分的积分变换公式直接得到.

在操作层面可作如下处理. 设 \( \{ {\rho }_{\alpha }{\} }_{\alpha  \in  I} \) 是从属于开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 的单位分解. 则 \( \{ {\pi }^{ * }{\rho }_{\alpha }{\} }_{\alpha  \in  I} \) 是从属于 \( E \) 的开覆盖 \( \{ E{|}_{{U}_{\alpha }}{\} }_{\alpha  \in  I} \) 的单位分解. 于是

\[
\omega  = \mathop{\sum }\limits_{\alpha }{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega
\]

所以

\[
{\pi }_{ * }\omega  = \mathop{\sum }\limits_{\alpha }{\pi }_{ * }\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right) . \tag{8}
\]

注意到 \( \operatorname{Supp}\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)  \subset  {\left. E\right| }_{{U}_{\alpha }},{\pi }_{ * }\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right) \) 可看作是定义在 \( {\left. E\right| }_{{U}_{\alpha }} \) 上沿纤维的积分.

命题 6.14. 沿纤维的积分 \( {\pi }_{ * } \) 是一个链映射,即 \( d{\pi }_{ * } = {\pi }_{ * }d \) . 因此沿纤维的积分诱导映射

\[
{\pi }_{ * } : {H}_{cv}^{ * }\left( E\right)  \rightarrow  {H}^{* - n}\left( M\right) .
\]

证. 鉴于等式 (8),由于映射 \( {\pi }_{ * } \) 与 \( d \) 都是线性的,只要在 \( {\left. E\right| }_{{U}_{\alpha }} \) 上证明

\[
{\pi }_{ * }d\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)  = d{\pi }_{ * }\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right) .
\]

因此可假定 \( E = M \times  {\mathbb{R}}^{n} \) 并分别对型 (I),(II) 的形式进行验证.

先对型 (II) 的形式进行验证. 设

\[
\omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n}
\]

\( \deg \phi  = q \) , \( \dim M = m \) . 则

\[
{\pi }_{ * }{d\omega } = {\pi }_{ * }\left( {{\pi }^{ * }{d\phi } \land  f\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n}}\right)
\]

\[
+ {\left( -1\right) }^{q}{\pi }_{ * }\left( {{\pi }^{ * }\phi \land \sum d{x}_{a} \land  \frac{\partial f\left( {x, t}\right) }{\partial {x}_{a}}d{t}_{1} \land  \cdots  \land  d{t}_{n}}\right)
\]

\[
= {d\phi } \cdot  {\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} + {\left( -1\right) }^{q}\phi  \land  \sum d{x}_{a}{\int }_{{\mathbb{R}}^{n}}\frac{\partial f\left( {x, t}\right) }{\partial {x}_{a}}d{t}_{1}\ldots d{t}_{n}
\]

\[
= {d\phi } \cdot  {\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\cdots d{t}_{n} + {\left( -1\right) }^{q}\phi  \cdot  d{\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n}
\]

\[
= d{\pi }_{ * }\omega \text{ . }
\]

接着对型 (I) 的形式进行验证. 设

\[
\omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{k}},\;0 \leq  k \leq  n - 1.
\]

则 \( d{\pi }_{ * }\omega  = 0 \) . 若 \( k < n - 1 \) ,显然有 \( {\pi }_{ * }{d\omega } = 0 \) . 若 \( k = n - 1 \) ,则

\[
{\pi }_{ * }{d\omega } = {\pi }_{ * }\left( {{\pi }^{ * }{d\phi } \land  f\left( {x, t}\right) d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{n - 1}}}\right)
\]

\[
+ {\left( -1\right) }^{q}{\pi }_{ * }\left( {{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{a = 1}}^{m}d{x}_{a} \land  \frac{\partial f\left( {x, t}\right) }{\partial {x}_{a}}d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{n - 1}}}\right)
\]

\[
+ {\left( -1\right) }^{q}{\pi }_{ * }\left( {{\pi }^{ * }\phi  \land  \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f\left( {x, t}\right) }{\partial {t}_{i}}d{t}_{i} \land  d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{n - 1}}}\right)
\]

\[
=  \pm  \phi  \cdot  {\int }_{{\mathbb{R}}^{n}}\frac{\partial f\left( {x, t}\right) }{\partial {t}_{i}}d{t}_{1}\ldots d{t}_{n}\;i \notin  \left\{  {{i}_{1},\ldots ,{i}_{n - 1}}\right\}
\]

\[
= 0\text{ , }
\]

最后一个等式是因为对给定的 \( x, f\left( {x, t}\right) \) 是关于变量 \( t \) 的具紧支集的函数，所以

\[
{\int }_{{\mathbb{R}}^{1}}\frac{\partial f\left( {x, t}\right) }{\partial {t}_{i}}d{t}_{i} = f\left( {\ldots ,\infty ,\ldots }\right)  - f\left( {\ldots , - \infty ,\ldots }\right)  = 0.
\]

命题 6.15. (投射公式) 设 \( \pi  : E \rightarrow  M \) 是秩 \( n \) 定向向量丛. (a) 设 \( \tau  \in  {\Omega }^{ * }\left( M\right) ,\omega  \in  {\Omega }_{cv}^{ * }\left( E\right) \) . 则

\[
{\pi }_{ * }\left( {{\pi }^{ * }\tau  \land  \omega }\right)  = \tau  \land  {\pi }_{ * }\omega
\]

(b) 设 \( M \) 是 \( m \) 维定向流形. 设 \( \omega  \in  {\Omega }_{cv}^{q}\left( E\right) ,\tau  \in  {\Omega }_{c}^{m + n - q}\left( M\right) .E \) 作为流形取局部乘积定向. 则

\[
{\int }_{E}{\pi }^{ * }\tau  \land  \omega  = {\int }_{M}\tau  \land  {\pi }_{ * }\omega .
\]

证. (a) 因为两个微分形式相等当且仅当它们局部相等,而 \( {\pi }_{ * } \) 是通过局部平凡化 \( {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n} \) 定义的,所以只要证明等式在 \( {U}_{\alpha } \times  {\mathbb{R}}^{n} \) 的情形成立. 对型 (I) 的微分形式 \( \omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{{i}_{1}} \land  \cdots  \land  d{t}_{{i}_{k}},0 \leq  k \leq  n - 1 \) ,根据 \( {\pi }_{ * } \) 的定义有

\[
{\pi }_{ * }\left( {{\pi }^{ * }\tau  \land  \omega }\right)  = 0 = \tau  \land  {\pi }_{ * }\omega
\]

对型 (II) 的微分形式 \( \omega  = {\pi }^{ * }\phi  \land  f\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n} \) ,根据 \( {\pi }_{ * } \) 的定义,

\[
{\pi }_{ * }\left( {{\pi }^{ * }\tau  \land  \omega }\right)  = {\pi }_{ * }\left( {{\pi }^{ * }\left( {\tau  \land  \phi }\right)  \land  f\left( {x, t}\right) d{t}_{1} \land  \cdots  \land  d{t}_{n}}\right)
\]

\[
= \tau  \land  \phi  \cdot  {\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} = \tau  \land  {\pi }_{ * }\omega .
\]

(b) 设 \( \{ \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) {\} }_{\alpha  \in  I} \) 是 \( E \) 的一个定向平凡化, \( \{ {\rho }_{\alpha }{\} }_{\alpha  \in  I} \) 是从属于开覆盖 \( \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) 的单位分解. 分解 \( \omega  = \mathop{\sum }\limits_{{\alpha  \in  I}}{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega \) ,其中 \( \operatorname{Supp}\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)  \subset  {\left. E\right| }_{{U}_{\alpha }} \) . 则

\[
{\int }_{E}\left( {{\pi }^{ * }\tau }\right)  \land  \omega  = \mathop{\sum }\limits_{\alpha }{\int }_{E{ \mid  }_{U\alpha }}{\pi }^{ * }\tau  \land  \left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)
\]

\[
{\int }_{M}\tau  \land  {\pi }_{ * }\omega  = \mathop{\sum }\limits_{\alpha }{\int }_{{U}_{\alpha }}\tau  \land  {\pi }_{ * }\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right) .
\]

此处 \( {\pi }^{ * }\tau  \land  \left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)  \in  {\Omega }_{c}^{m + n}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) 因为 \( K = \operatorname{Supp}\left( {{\rho }_{\alpha }\tau }\right) \) 是紧的且根据定义 Supp \( \omega  \cap  {\pi }^{-1}\left( K\right) \) 是紧的; \( \tau  \land  {\pi }_{ * }\left( {{\pi }^{ * }{\rho }_{\alpha } \cdot  \omega }\right)  \in  {\Omega }_{c}^{m}\left( {U}_{\alpha }\right) \) 因为它的支集是紧集 Supp \( \tau \) 的闭子集. 所以上述两个等式右边的积分是有意义的. 于是只要对 \( {U}_{\alpha } \times  {\mathbb{R}}^{n} \) 的情形进行证明,但这是 Fubini 定理. 注意 \( {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n} \) 作为流形取乘积定向.

Thom 同构对紧支集的 Poincaré 引理 (4.7) 的证明可逐字逐句照搬用来证明

命题 6.16. (对紧垂直支集的 Poincaré 引理) 沿纤维的积分 \( {\pi }_{ * } \) 定义同构

\[
{\pi }_{ * } : {H}_{cv}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  \rightarrow  {H}^{* - n}\left( M\right) .
\]

补充练习 2 . 证明上述命题.

这是以下 Thom 同构定理的特殊情形, 是归纳证明的基础.

定理 6.17.(Thom 同构)若 \( \pi  : E \rightarrow  M \) 是有限型流形 \( M \) 上秩 \( n \) 可定向向量丛, 则

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( M\right) .
\]

证. 设 \( U \) , \( V \) 是 \( M \) 的两个开子集. 如 (2.3) 应用从属于 \( \{ U, V\} \) 的单位分解可得复形的短正合序列

\[
0 \rightarrow  {\Omega }_{cv}^{ * }\left( {E{|}_{U \cup  V}}\right)  \rightarrow  {\Omega }_{cv}^{ * }\left( {E{|}_{U}}\right)  \oplus  {\Omega }_{cv}^{ * }\left( {E{|}_{V}}\right)  \rightarrow  {\Omega }_{cv}^{ * }\left( {E{|}_{U \cap  V}}\right)  \rightarrow  0.
\]

于是有以下 MV 序列的图:

\[
\rightarrow  {H}_{cv}^{ * }\left( {\left. E\right| }_{U \cup  V}\right)  \rightarrow  {H}_{cv}^{ * }\left( {\left. E\right| }_{U}\right)  \oplus  {H}_{cv}^{ * }\left( {\left. E\right| }_{V}\right)  \rightarrow  {H}_{cv}^{ * }\left( {\left. E\right| }_{U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}_{cv}^{* + 1}\left( {\left. E\right| }_{U \cup  V}\right)  \rightarrow
\]

\[
\rightarrow  {H}^{* - n}\left( {U \cup  V}\right)  \rightarrow  {H}^{* - n}\left( U\right)  \oplus  {H}^{* - n}\left( V\right)  \rightarrow  {H}^{* - n}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{* - n + 1}\left( {U \cup  V}\right)  \rightarrow
\]

图的左边两个方块的交换性是显然的, 我们验证右边方块的交换性. 其实, 应用连接同态 \( {d}^{ * } \) 的显式公式 (2.5) 与投射公式 6.15(a) 有

\[
{\pi }_{ * }{d}^{ * }\omega  = {\pi }_{ * }\left( {d\left( {{\pi }^{ * }{\rho }_{U}}\right)  \land  \omega }\right)  = {\pi }_{ * }\left( {{\pi }^{ * }d{\rho }_{U} \land  \omega }\right)  = d{\rho }_{U} \land  {\pi }_{ * }\omega  = {d}^{ * }\left( {{\pi }_{ * }\omega }\right) .
\]

所以上图是可交换的. 于是由五引理知,若 Thom 同构对 \( {\left. E\right| }_{U},{\left. E\right| }_{V},{\left. E\right| }_{U \cap  V} \) 成立, 则对 \( {\left. E\right| }_{U \cup  V} \) 也成立. 由此可对 \( M \) 的有限好覆盖的开集个数进行归纳证明. 当个数等于 1 时, \( M \) 微分同胚于 \( {\mathbb{R}}^{m} \) ,由推论 6.9 知 \( E \) 是平凡的,此时 Thom 同构就是对紧垂直支集的 Poincaré 引理, 即命题 6.16.

注记 6.17.1. 若 \( M \) 不是有限型的, Thom 同构定理仍成立. 在 (12.2.2) 中会对任意流形重新证明 Thom 同构定理.

记 \( \mathcal{T} \) 为 \( {\pi }_{ * } \) 的逆:

\[
{H}_{cv}^{* + n}\left( E\right) \underset{\mathcal{T}}{\overset{{\pi }_{ * }}{ \rightleftarrows  }}{H}^{ * }\left( M\right)
\]

\( \mathcal{T} \) 称为 Thom 同构. 特别地有 \( \mathcal{T} : {H}^{0}\left( M\right)  \rightarrow  {H}_{cv}^{n}\left( E\right) \) . 对 \( 1 \in  {H}^{0}\left( M\right) \) , \( \Phi  = \mathcal{T}\left( 1\right)  \in  {H}_{cv}^{n}\left( E\right) \) 称为定向向量丛 \( E \) 的 Thom 类.

因为 \( {\pi }_{ * }\Phi  = {\pi }_{ * }\mathcal{T}\left( 1\right)  = 1 \) ,根据投射公式 \( {6.15}\left( \mathrm{\;a}\right) \) ,对任意 \( \omega  \in  {H}^{ * }\left( M\right) \) ,

\[
{\pi }_{ * }\left( {{\pi }^{ * }\omega  \land  \Phi }\right)  = \omega  \land  {\pi }_{ * }\Phi  = \omega
\]

或

\[
\mathcal{T}\left( \omega \right)  = \mathcal{T}{\pi }_{ * }\left( {{\pi }^{ * }\omega  \land  \Phi }\right)  = {\pi }^{ * }\omega  \land  \Phi .
\]

所以 Thom 同构 \( \mathcal{T} \) 作为 \( {\pi }_{ * } \) 的逆映射定义为

\[
\mathcal{T}\left( \;\right)  = {\pi }^{ * }\left( \;\right)  \land  \Phi .
\]

命题 6.18. 秩 \( n \) 定向向量丛 \( E \) 的 Thom 类 \( \Phi \) 是 \( {H}_{cv}^{n}\left( E\right) \) 中唯一的上同调类, 它限制在每条纤维 \( {E}_{x} \) 上是 \( {H}_{c}^{n}\left( {E}_{x}\right) \) 的生成元.

证. 因为 \( {\pi }_{ * }\Phi  = 1 \) ,即

\[
\left( {{\pi }_{ * }\Phi }\right) \left( x\right)  = {\int }_{{E}_{x}}\Phi \left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} = 1,
\]

所以 \( {\left. \Phi \right| }_{{E}_{x}} \in  {H}_{c}^{n}\left( {E}_{x}\right) \) 是生成元.

若 \( {\Phi }^{\prime } \) 也满足这个性质,则

\[
{\pi }_{ * }\left( {{\pi }^{ * }\omega  \land  {\Phi }^{\prime }}\right)  = \omega  \land  {\pi }_{ * }{\Phi }^{\prime } = \omega .
\]

所以

\[
\mathcal{T}\left( \omega \right)  = {\pi }^{ * }\omega  \land  {\Phi }^{\prime }.
\]

因此

\[
{\Phi }^{\prime } = \mathcal{T}\left( 1\right)  = \Phi
\]

命题 6.19. 设 \( {\pi }_{1} : E \rightarrow  M,{\pi }_{2} : {E}^{\prime } \rightarrow  M \) 是流形 \( M \) 上两个定向向量丛. 则

\[
\Phi \left( {E \oplus  {E}^{\prime }}\right)  = {\mathrm{{pr}}}_{1}^{ * }\Phi \left( E\right)  \land  {\mathrm{{pr}}}_{2}^{ * }\Phi \left( {E}^{\prime }\right) ,
\]

其中 \( {\mathrm{{pr}}}_{1} : E \oplus  {E}^{\prime } \rightarrow  E,{\mathrm{{pr}}}_{2} : E \oplus  {E}^{\prime } \rightarrow  {E}^{\prime } \) 是两个投射.

证. 设 \( E,{E}^{\prime } \) 的秩分别为 \( {n}_{1},{n}_{2} \) . 则

\[
{\Phi }^{\prime } = {\mathrm{{pr}}}_{1}^{ * }\Phi \left( E\right)  \land  {\mathrm{{pr}}}_{2}^{ * }\Phi \left( {E}^{\prime }\right)  \in  {H}_{cv}^{{n}_{1} + {n}_{2}}\left( {E \oplus  {E}^{\prime }}\right)
\]

且

\[
{\int }_{{E}_{x} \oplus  {E}_{x}^{\prime }}{\Phi }^{\prime }{\left| {}_{{E}_{x} \oplus  {E}_{x}^{\prime }} = {\int }_{{E}_{x}}\Phi \left( E\right) \right| }_{{E}_{x}} \cdot  {\int }_{{E}_{x}^{\prime }}\Phi \left( {E}^{\prime }\right) {|}_{{E}_{x}^{\prime }} = 1.
\]

由命题 6.18 知 \( \Phi \left( {E \oplus  {E}^{\prime }}\right)  = {\Phi }^{\prime } \) .

补充练习 3 . (Thom 类的函子性) 设 \( f : N \rightarrow  M \) 是光滑映射, \( \pi  : E \rightarrow  M \) 是定向向量丛. 证明

\[
\Phi \left( {{f}^{-1}E}\right)  = {f}^{ * }\Phi \left( E\right) .
\]

练习 6.20. 仿照 Thom 同构即定理 6.17 的证明，应用 MV 方法证明若 \( \pi  : E \rightarrow  M \) 是有限型流形 \( M \) 上秩 \( n \) 定向向量丛,则

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

注意这是命题 6.13,但去掉了 \( M \) 的可定向性假定.

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 补充练习 3.

4. 练习 6.20.

代数拓扑与微分形式
