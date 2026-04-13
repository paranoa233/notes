#### 第09讲 The Thom Isomorphism (3)

§6 The Thom Isomorphism (3)

9. Poincaré 对偶与 Thom 类

设 \( M \) 是 \( n \) 维定向流形, \( S \) 是 \( M \) 的 \( k \) 维闭定向子流形. 由 (5.13), \( S \) 的 Poincaré 对偶是 \( M \) 上闭 \( \left( {n - k}\right) \) -形式 \( {\eta }_{S} \) 或它的上同调类,使得对任意 \( \left\lbrack  \omega \right\rbrack   \in  {H}_{c}^{k}\left( M\right) \) 有

(6.21)

\[
{\int }_{S}{\left. \omega \right| }_{S} = {\int }_{M}\omega  \land  {\eta }_{S}
\]

这节课解释子流形的 Poincaré 对偶是如何与子流形上一个向量丛的 Thom 类联系在一起的(命题 6.24). 为此首先要引进子流形 \( S \) 在 \( M \) 中的管状邻域,根据定义这是子流形 \( S \) 在 \( M \) 的开邻域,它微分同胚于 \( S \) 的法丛,使得 \( S \) 微分同胚于法丛的零截面. \( S \) 的法丛是作为 \( S \) 上两个向量丛的商丛出现的.

- 商丛

- 子流形的法丛与管状邻域定理

- Poincaré 对偶与 Thom 类

- 两个应用

## 商丛

设 \( \pi  : E \rightarrow  M \) 是 \( M \) 上秩 \( n \) 向量丛, \( F \) 是 \( E \) 的秩 \( k \) 子丛,即 \( F \) 是 \( M \) 上向量丛并对任意的 \( x \in  M \) ,向量空间 \( {F}_{x} \) 是 \( {E}_{x} \) 的子空间.

由向量丛 \( E \) 与它的子丛 \( F \) 可定义商丛 \( Q \) ,它是一个向量丛使得以下向量丛的序列是正合的:

\[
0 \rightarrow  F \rightarrow  E \rightarrow  Q \rightarrow  0
\]

即对每点 \( x \in  M \) ,存在点 \( x \) 的纤维作为向量空间的正合序列

\[
0 \rightarrow  {F}_{x} \rightarrow  {E}_{x} \rightarrow  {Q}_{x} \rightarrow  0
\]

所以 \( {Q}_{x} = {E}_{x}/{F}_{x} \) 是商空间,而

\[
Q = \mathop{\coprod }\limits_{{x \in  M}}{Q}_{x}.
\]

习惯把 \( Q \) 记为 \( E/F \) . 需研究商丛 \( Q \) 的结构. 首先,存在 \( E, F \) 的局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I},{\left\{  \left( {U}_{\alpha },{\psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 使得

\[
{\psi }_{\alpha } = {\left. {\phi }_{\alpha }\right| }_{{\left. F\right| }_{{U}_{\alpha }}}, \tag{9}
\]

即使得以下图表可交换:

![bo_d7e85t491nqc73eqefm0_186_873_702_599_400_0.jpg](images/fu_algebraic_topology_and_differential_forms_014_bod7e85t491nqc73eqefm01868737025994000.jpg)

其中 \( i : {\mathbb{R}}^{k} \rightarrow  {\mathbb{R}}^{n}, i\left( {{x}_{1},\ldots ,{x}_{k}}\right)  = \left( {{x}_{1},\ldots ,{x}_{k},0,\ldots ,0}\right) \) .

补充练习 1. 证明存在 \( E \) , \( F \) 的局部平凡化使得等式 (9) 成立. (提示: 应用标架.)

此时若设局部平凡化 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 的转移函数是 \( {g}_{\alpha \beta },{\left\{  \left( {U}_{\alpha },{\psi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 的转移函数是 \( {h}_{\alpha \beta } \) ,则有

\[
{g}_{\alpha \beta } = \left( \begin{matrix} {h}_{\alpha \beta } &  * \\  0 & {q}_{\alpha \beta } \end{matrix}\right) . \tag{10}
\]

注意此处采用列向量. 所以 \( Q \) 的转移函数是 \( {q}_{\alpha \beta } \) 并且

\[
\det {g}_{\alpha \beta } = \det {h}_{\alpha \beta } \cdot  \det {q}_{\alpha \beta }.
\]

若 \( E, F \) 是定向向量丛, \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\}  ,\left\{  \left( {{U}_{\alpha },{\psi }_{\alpha }}\right) \right\} \) 是 \( E, F \) 的定向平凡化,则

\[
\det {q}_{\alpha \beta } > 0\text{ . }
\]

所以 \( Q \) 也是可定向的并且给定了它的一个定向平凡化. 此时称给定 \( Q \) 的定向使得 \( E \) 的定向是直和定向. 另一方面,赋予 \( E \) 一个度量 \( \langle \) , \( \rangle \) . 则它诱导了 \( F \) 的度量. 对任意的 \( x \in  M \) ,定义

\[
{F}_{x}^{ \bot  } = \left\{  {v \in  {E}_{x}\mid \langle v, w\rangle  = 0\text{ 对任意的 }w \in  {F}_{x}}\right\}  .
\]

于是 \( {E}_{x} = {F}_{x} \oplus  {F}_{x}^{ \bot  } \) . 令

\[
{F}^{ \bot  } = \mathop{\coprod }\limits_{{x \in  M}}{F}_{x}^{ \bot  }.
\]

则 \( {F}^{ \bot  } \) 是 \( E \) 的子丛且满足 \( E = F \oplus  {F}^{ \bot  } \) . 当然,我们也有正合序列

\[
0 \rightarrow  F \rightarrow  E \rightarrow  {F}^{ \bot  } \rightarrow  0
\]

\( E \) 的度量 \( \langle \;,\;\rangle \) 诱导了 \( {F}^{ \bot  } \) 的度量. 显然,

\[
Q \simeq  {F}^{ \bot  }\text{ . }
\]

借此同构,可由 \( {F}^{ \bot  } \) 的度量赋予 \( Q \) 一个度量. 若 \( E \) , \( F \) 是定向向量丛,则 \( E \) , \( F \) 的定向给定了 \( {F}^{ \bot  } \) 的定向使得 \( E \) 的定向是直和定向.

子流形的法丛与管状邻域定理

设 \( i : S \hookrightarrow  M \) 是 \( n \) 维流形 \( M \) 的 \( k \) 维子流形. 在 \( S \) 上有两个向量丛,一个是 \( S \) 的切丛 \( {TS} \rightarrow  S \) ,另一个是 \( M \) 的切丛 \( {TM} \) 限制到 \( S \) 或用映射 \( i \) 拉回到 \( S \) :

![bo_d7e85t491nqc73eqefm0_189_787_608_751_330_0.jpg](images/fu_algebraic_topology_and_differential_forms_015_bod7e85t491nqc73eqefm01897876087513300.jpg)

显然 \( {TS} \) 是 \( {\left. TM\right| }_{S} \) 的子丛. 定义 \( S \) 在 \( M \) 中的法丛 \( {N}_{S/M} \) 为商丛:

(6.22)

\[
{\left. 0 \rightarrow  TS \rightarrow  TM\right| }_{S} \rightarrow  {N}_{S/M} \rightarrow  0
\]

在不致引起混淆时,把法丛 \( {N}_{S/M} \) 简记为 \( N \) .

若流形 \( M \) , \( S \) 可定向,则向量丛 \( {TM} \) 从而 \( {TM}{ \mid  }_{S} \) 与 \( {TS} \) 可定向. 于是 \( N \) 可定向, 并且 \( {TM}{ \mid  }_{S} \) 与 \( {TS} \) 的定向确定了 \( N \) 的定向使得 \( {TM}{ \mid  }_{S} \) 是直和定向.

我们说些子流形理论. 这方面最好的参考书是 Warner 的《微分流形与李群基础》.

对任意点 \( x \in  S \) ,存在点 \( x \) 在 \( M \) 中的坐标图 \( \left( {U,\phi }\right) \) , \( \phi  : U \rightarrow  {\mathbb{R}}^{n} \) 使得 \( {\left. \phi \right| }_{S \cap  U} \) 是点 \( x \) 在 \( S \) 中的坐标图,即存在 \( U \) 上坐标函数 \( {x}_{1},\ldots ,{x}_{n} \) 使得

\[
S \cap  U = \left\{  {{x}_{a} = 0 \mid  k + 1 \leq  a \leq  n}\right\}  ,
\]

即使得 \( {x}_{1},\ldots ,{x}_{k} \) 是 \( S \cap  U \) 的坐标函数.

约定以下指标:

\[
1 \leq  i, j,\cdots  \leq  k,\;k + 1 \leq  a, b,\cdots  \leq  n,\;1 \leq  A, B,\cdots  \leq  n.
\]

于是

\[
{TM}{ \mid  }_{{U}_{\alpha }}\text{ 的一组标架为 }{\left\{  \frac{\partial }{\partial {x}_{A}^{\alpha }}\right\}  }_{1 \leq  A \leq  n}\text{ , }
\]

\[
{\left. TS\right| }_{S \cap  {U}_{\alpha }}\text{ 的一组标架为 }{\left\{  \frac{\partial }{\partial {x}_{i}^{\alpha }}\right\}  }_{1 \leq  i \leq  k}\text{ , }
\]

\[
{\left. N\right| }_{S \cap  {U}_{\alpha }}\text{ 的一组标架为 }{\left\{  \left\lbrack  \frac{\partial }{\partial {x}_{a}^{\alpha }}\right\rbrack  \right\}  }_{k + 1 \leq  a \leq  n}\text{ . }
\]

在 \( S \cap  {U}_{\alpha \beta } \) 上,

\[
\frac{\partial }{\partial {x}_{i}^{\beta }} = \mathop{\sum }\limits_{{j = 1}}^{k}\frac{\partial {x}_{j}^{\alpha }}{\partial {x}_{i}^{\beta }}\frac{\partial }{\partial {x}_{j}^{\alpha }} + \mathop{\sum }\limits_{{a = k + 1}}^{n}\frac{\partial {x}_{a}^{\alpha }}{\partial {x}_{i}^{\beta }}\frac{\partial }{\partial {x}_{a}^{\alpha }}
\]

\[
\frac{\partial }{\partial {x}_{a}^{\beta }} = \mathop{\sum }\limits_{{j = 1}}^{k}\frac{\partial {x}_{j}^{\alpha }}{\partial {x}_{a}^{\beta }}\frac{\partial }{\partial {x}_{j}^{\alpha }} + \mathop{\sum }\limits_{{b = k + 1}}^{n}\frac{\partial {x}_{b}^{\alpha }}{\partial {x}_{a}^{\beta }}\frac{\partial }{\partial {x}_{b}^{\alpha }}
\]

按对局部坐标图的选取,在 \( S \cap  {U}_{\alpha \beta } \) 上 \( \partial {x}_{a}^{\alpha }/\partial {x}_{i}^{\beta } = 0 \) ,所以 \( {TS} \) 的转移函数是

\[
{h}_{\alpha \beta } = {\left( \frac{\partial {x}_{j}^{\alpha }}{\partial {x}_{i}^{\beta }}\right) }_{k \times  k}.
\]

但在 \( S \cap  {U}_{\alpha \beta } \) 上 \( \partial {x}_{j}^{\alpha }/\partial {x}_{a}^{\beta } \) 可能不为零,这些项需要 “抹” 掉. 所以 \( N \) 的转移函数是

\[
{q}_{\alpha \beta } = {\left( \frac{\partial {x}_{b}^{\alpha }}{\partial {x}_{a}^{\beta }}\right) }_{\left( {n - k}\right)  \times  \left( {n - k}\right) }.
\]

\( {\left. TM\right| }_{S} \) 的转移函数是

\[
{g}_{\alpha \beta } = \left( \begin{matrix} {h}_{\alpha \beta } &  * \\  0 & {q}_{\alpha \beta } \end{matrix}\right) ,\; *  = {\left( \frac{\partial {x}_{j}^{\alpha }}{\partial {x}_{a}^{\beta }}\right) }_{k \times  \left( {n - k}\right) }.
\]

定理. (管状邻域定理) 设 \( i : S \hookrightarrow  M \) 是子流形, \( N = {N}_{S/M} \) 是法丛. 则存在映射 \( j : N \rightarrow  M \) 使得下列条件满足:

(a) \( j\left( N\right)  \subset  M \) 是开集;

(b) \( j : N \rightarrow  j\left( N\right) \left( { \subset  M}\right) \) 是微分同胚;

(c) \( j \circ  s = i \) ,其中 \( s : S \rightarrow  N \) 是零截面.

\( j\left( N\right)  \subset  M \) 称为 \( S \) 在 \( M \) 中的管状邻域,以下记 \( T = j\left( N\right) \) .

![bo_d7e85t491nqc73eqefm0_192_818_943_631_727_0.jpg](images/fu_algebraic_topology_and_differential_forms_016_bod7e85t491nqc73eqefm01928189436317270.jpg)

Poincaré 对偶与 Thom 类记 \( \Phi \) 为 \( S \) 的法丛 \( N \) 的 Thom 类. 应用 Thom 同构定理于 \( N \) ,得映射的序列:

\[
{H}^{ * }\left( S\right) \underset{ \sim  }{ \rightarrow  }{H}_{cv}^{* + n - k}\left( N\right) \underset{ \sim  }{\overset{{\left( {j}^{-1}\right) }^{ * }}{ \rightarrow  }}{H}_{cv}^{* + n - k}\left( T\right) \overset{{j}_{ * }}{ \rightarrow  }{H}^{* + n - k}\left( M\right) ,
\]

其中最后一个映射 \( {j}_{ * } \) 是零延拓,它是有定义的因为 \( \operatorname{Supp}\Phi  \subset  T \) .

引理 6.23. \( n \) 维定向流形 \( M \) 的 \( k \) 维闭定向子流形 \( S \) 的 Poincaré 对偶 \( \left\lbrack  {\eta }_{S}\right\rbrack \) 是 \( S \) 的法丛 \( {N}_{S/M} \) 的 Thom 类,即

\[
\left\lbrack  {\eta }_{S}\right\rbrack   = {j}_{ * }\left( {\Phi  \land  1}\right)  = {j}_{ * }\Phi  \in  {H}^{n - k}\left( M\right) .
\]

证. 为了证明这个命题,只要证明 \( {j}_{ * }\Phi \) 满足用来定义 Poincaré 对偶的性质 (6.21). 设 \( \omega \) 是 \( M \) 上具紧支集的闭 \( k \) -形式. 设 \( \iota  : S \rightarrow  T \) 是包含,它可看作丛 \( \pi  : T \rightarrow  S \) 的零截面. 因为 \( \pi \) 是从 \( T \) 到 \( S \) 的形变收缩,所以 \( {\pi }^{ * } \) 与 \( {\iota }^{ * } \) 在上同调的层面是互逆的映射. 因此在形式的层面, \( {\left. \omega \right| }_{T} \) 与 \( {\pi }^{ * }{\iota }^{ * }\left( {\left. \omega \right| }_{T}\right) \) 相差一个恰当形式:

\[
{\left. \omega \right| }_{T} = {\pi }^{ * }{\iota }^{ * }\left( {\left. \omega \right| }_{T}\right)  + {d\tau },\;\tau  \in  {\Omega }^{k - 1}\left( T\right) .
\]

于是，

\[
{\int }_{M}\omega  \land  {j}_{ * }\Phi  = {\int }_{T}{\left. \omega \right| }_{T} \land  \Phi \;\text{ 因为 Supp }\Phi  \subset  T\text{ ,而 }{j}_{ * }\text{ 是零延拓 }
\]

\[
= {\int }_{T}{\pi }^{ * }{\iota }^{ * }\left( {\left. \omega \right| }_{T}\right)  \land  \Phi  + {\int }_{T}{d\tau } \land  \Phi
\]

\[
= {\int }_{T}{\pi }^{ * }{\iota }^{ * }\left( {\left. \omega \right| }_{T}\right)  \land  \Phi \;{\int }_{T}{d\tau } \land  \Phi  = {\int }_{T}d\left( {\tau  \land  \Phi }\right)  = 0
\]

因为由 Stokes 定理，

\[
= {\int }_{S}{\iota }^{ * }\left( {\left. \omega \right| }_{T}\right)  \land  {\pi }_{ * }\Phi \;\text{ 根据投射公式 (6.15(b)) }
\]

\[
= {\int }_{S}{i}^{ * }\omega \;\text{ 因为 }{\pi }_{ * }\Phi  = 1.
\]

这就完成了引理的证明.

注意若 \( S \) 是紧的,则法丛 \( N \) 的 Thom 类 \( \Phi \) 在 \( N \) 中具紧支集,即它在 \( T \) 中具紧支集,所以 \( {j}_{ * }\Phi \) 在 \( M \) 中也具紧支集. 这就是说,紧子流形的 Poincaré 对偶总可被具紧支集的形式表示.

现设 \( M \) 是定向流形, \( E \) 是 \( M \) 上定向向量丛. \( M \) 与 \( E \) 的零截面微分同胚,即可把 \( M \) 看作 \( E \) 的闭子流形. 则有正合序列

\[
{\left. 0 \rightarrow  TM \rightarrow  TE\right| }_{M} \rightarrow  E \rightarrow  0 \tag{11}
\]

即 \( M \) 在 \( E \) 中的法丛是 \( E \) 本身.

补充练习 2 . 证明序列 (11) 的正合性.

命题 6.24. (a) 定向流形 \( M \) 的闭定向子流形 \( S \) 的 Poincaré 对偶与 \( S \) 的法丛的 Thom 类可被相同的形式表示. 特别地,若 \( S \) 是紧的,则它的 Poincaré 对偶总可被具紧支集的形式表示.

(b) 定向流形 \( M \) 上定向向量丛 \( E \) 的 Thom 类与 \( E \) 的零截面的 Poincaré 对偶可被相同的形式表示.

因为子流形 \( S \) 在 \( M \) 中的管状邻域可充分小,我们得到

命题 6.25.(局部化原理)闭子流形 \( S \) 的 Poincaré 对偶的支集可缩小到 \( S \) 的任意给定的管状邻域中.

例 6.26. (a) \( n \) 维流形 \( M \) 中点 \( p \) 的 Poincaré 对偶. 点 \( p \) 的一个管状邻域 \( T \) 不过是点 \( p \) 的一个开球. \( {H}_{cv}^{n}\left( T\right) \) 的一个生成元是积分等于 1 的 bump \( n \) -形式. 所以一点的 Poincaré 对偶是 \( M \) 上一个 bump \( n \) -形式,这点不必属于这个形式的支集因为在连通流形上所有 bump \( n \) -形式的上同调类是相同的.

![bo_d7e85t491nqc73eqefm0_197_810_679_696_496_0.jpg](images/fu_algebraic_topology_and_differential_forms_017_bod7e85t491nqc73eqefm01978106796964960.jpg)

(b) \( M \) 的 Poincaré 对偶. 此时, \( T = M,{H}_{cv}^{ * }\left( T\right)  = {H}^{ * }\left( M\right) \) . 因为 \( \Phi  \in  {H}_{cv}^{0}\left( T\right) \) , \( {\pi }_{ * }\Phi  = 1 \) ,所以 \( \left\lbrack  {\eta }_{M}\right\rbrack   = \Phi \) 是 \( M \) 的常值函数 1 .

(c) 环面 \( {T}^{2} \) 上圆周 \( {S}^{1} \) 的 Poincaré 对偶. 如图, \( {S}^{1} \) 的 Poincaré 对偶是一个 bump 1-形式,它的支集在圆周 \( {S}^{1} \) 的管状邻域,且它限制在管状邻域的每条纤维的积分等于 1 .

![bo_d7e85t491nqc73eqefm0_198_879_335_580_427_0.jpg](images/fu_algebraic_topology_and_differential_forms_018_bod7e85t491nqc73eqefm01988793355804270.jpg)

环面 \( {T}^{2} \) 通常由一个正方形来表示,若圆周 \( {S}^{1} \) 是一个垂直线段,见下图的粗线,则它的 Poincaré 对偶是 \( \rho \left( x\right) {dx} \) ,其中 \( \rho \) 是一个积分等于 1 的 bump 函数.

![bo_d7e85t491nqc73eqefm0_198_912_1032_499_507_0.jpg](images/fu_algebraic_topology_and_differential_forms_019_bod7e85t491nqc73eqefm019891210324995070.jpg)

补充练习 3 . 证明上述 \( \left\lbrack  {\rho \left( x\right) {dx}}\right\rbrack \) 在 \( {H}^{1}\left( {\mathbb{R}}^{2}\right) \) 中等于零,但在 \( {H}^{1}\left( {T}^{2}\right) \) 中不等于零.

两个应用

应用 Poincaré 对偶作为法丛的 Thom 类的显式构造 \( {\eta }_{S} = {j}_{ * }\Phi \) ,我们证明 Poincaré 对偶的两个基本性质.

1. \( M \) 中两个子流形 \( R, S \) 称为横截相交的若对每点 \( x \in  R \cap  S \) ，

(6.27)

\[
{T}_{x}R + {T}_{x}S = {T}_{x}M.
\]

以下前两个图中的 \( R, S \) 横截相交,最后一个图中的 \( R, S \) 不是. 设 \( R, S \) 是流形 \( M \) 中横截相交的闭子流形. 则 \( R \cap  S \) 是 \( R, S, M \) 的闭子流形且

\[
\dim \left( {R \cap  S}\right)  = \dim R + \dim S - \dim M,\;\text{ 即 }
\]

(6.28)

\[
{\operatorname{codim}}_{M}\left( {R \cap  S}\right)  = {\operatorname{codim}}_{M}R + {\operatorname{codim}}_{M}S.
\]

![bo_d7e85t491nqc73eqefm0_199_209_1140_448_325_0.jpg](images/fu_algebraic_topology_and_differential_forms_021_bod7e85t491nqc73eqefm019920911404483250.jpg)

![bo_d7e85t491nqc73eqefm0_199_871_1090_499_378_0.jpg](images/fu_algebraic_topology_and_differential_forms_022_bod7e85t491nqc73eqefm019987110904993780.jpg)

![bo_d7e85t491nqc73eqefm0_199_1519_1122_585_313_0.jpg](images/fu_algebraic_topology_and_differential_forms_020_bod7e85t491nqc73eqefm0199151911225853130.jpg)

所以 \( R \cap  S \) 在 \( M \) 中的法丛

(6.29)

\[
{N}_{\left( {R \cap  S}\right) /M} = {\left. {N}_{R/M}\right| }_{R \cap  S} \oplus  {\left. {N}_{S/M}\right| }_{R \cap  S}.
\]

若 \( M \) , \( R \) , \( S \) 是定向流形, 则 \( {N}_{R/M}{\left| {}_{R \cap  S}\text{ , }{N}_{S/M}\right| }_{R \cap  S} \) 是定向向量丛. 由上述等式可给 \( {N}_{\left( {R \cap  S}\right) /M} \) 直和定向. 记定向向量丛 \( E \) 的 Thom 类为 \( \Phi \left( E\right) \) . 由 (6.19) 有

(6.30)

\[
\Phi \left( {N}_{\left( {R \cap  S}\right) /M}\right)  = \Phi \left( {\left. {N}_{R/M}\right| }_{R \cap  S}\right)  \land  \Phi \left( {\left. {N}_{S/M}\right| }_{R \cap  S}\right)
\]

\[
= \Phi \left( {N}_{R/M}\right)  \land  \Phi \left( {N}_{S/M}\right) .
\]

在上述等式中本来是有一些拉回映射的, 但当法丛看作管状邻域时, 这些映射都不见了. 因此

(6.31)

\[
{\eta }_{R \cap  S} = {\eta }_{R} \land  {\eta }_{S}
\]

命题. 两个横截相交的闭定向子流形的交的 Poincaré 对偶等于这两个子流形的 Poincaré 对偶的外积.

2. 设 \( f : {M}^{\prime } \rightarrow  M \) 是光滑映射, \( S \) 是 \( M \) 的闭子流形. 若对 \( {f}^{-1}\left( S\right) \) 中每点 \( x \) 有

\[
{f}_{ * }\left( {{T}_{x}{M}^{\prime }}\right)  + {T}_{f\left( x\right) }S = {T}_{f\left( x\right) }M,
\]

则称映射 \( f \) 横截于子流形 \( S \) . 这就是说, \( f\left( {M}^{\prime }\right) \) 与闭子流形 \( S \) 或不相交,或横截相交. 它具有以下性质.

命题. 若光滑映射 \( f : {M}^{\prime } \rightarrow  M \) 横截于 \( M \) 的闭子流形 \( S \) ,则 \( {f}^{-1}\left( S\right) \) 是 \( {M}^{\prime } \) 的光滑子流形并且对 \( S \) 在 \( M \) 中充分小管状邻域 \( T \) , \( {f}^{-1}T \) 是 \( {f}^{-1}\left( S\right) \) 的管状邻域. 此处 \( {f}^{-1}T \) 理解为拉回丛:

![bo_d7e85t491nqc73eqefm0_202_690_619_980_399_0.jpg](images/fu_algebraic_topology_and_differential_forms_023_bod7e85t491nqc73eqefm02026906199803990.jpg)

现设 \( {M}^{\prime } \) , \( M \) , \( S \) 是定向流形. 向量丛 \( {TM}{|}_{S} \) 与 \( {TS} \) 的定向确定了作为法丛 \( T \) 的定向使得 \( {\left. TM\right| }_{S} \) 的定向是直和定向. 于是 \( {f}^{-1}T \) 作为拉回丛有诱导定向. 向量丛 \( {\left. T{M}^{\prime }\right| }_{{f}^{-1}\left( S\right) } \) 与 \( {f}^{-1}T \) 的定向确定了 \( T{f}^{-1}\left( S\right) \) 的定向使得 \( {\left. T{M}^{\prime }\right| }_{{f}^{-1}\left( S\right) } \) 的定向是直和定向. 这样就确定了 \( {f}^{-1}\left( S\right) \) 的定向. 有了上述准备之后，我们有以下交换图表，其中 \( r \) 是子流形 \( S \) 的余维数.

![bo_d7e85t491nqc73eqefm0_203_361_475_1491_375_0.jpg](images/fu_algebraic_topology_and_differential_forms_024_bod7e85t491nqc73eqefm020336147514913750.jpg)

右边方块的交换性是显然的,左边方块的交换性是因为对任意的 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{ * }\left( S\right) \) 有

\( {f}^{ * }\mathcal{T}\left( \omega \right)  = {f}^{ * }\left( {{\pi }^{ * }\omega  \land  \Phi \left( T\right) }\right) \; \) 根据 Thom 同构 \( \mathcal{T} \) 的定义

\[
= {f}^{ * }{\pi }^{ * }\omega  \land  {f}^{ * }\Phi \left( T\right)
\]

\[
= {\left( {\pi }^{\prime }\right) }^{ * }{\left( {\left. f\right| }_{{f}^{-1}\left( S\right) }\right) }^{ * }\omega  \land  \Phi \left( {{f}^{-1}T}\right)
\]

根据前命题中的交换图表与 Thom 类的函子性 \( = \mathcal{T}\left( {{\left( {\left. f\right| }_{{f}^{-1}\left( S\right) }\right) }^{ * }\omega }\right) \; \) 根据 Thom 同构的定义. 综上所述，有

\( = {\eta }_{f} - 1\left( S\right) \)

\( {f}^{ * }{\eta }_{S} = {f}^{ * }{j}_{ * }\Phi \left( T\right) \; \) 根据命题 6.24(a),因为 \( T \) 是 \( S \) 的管状邻域 \( = {f}^{ * }{j}_{ * }\mathcal{T}\left( 1\right) \; \) 根据 Thom 类的定义 \( = {j}_{ * }\mathcal{T}{\left( {\left. f\right| }_{{f}^{-1}\left( S\right) }\right) }^{ * }\left( 1\right) \; \) 根据上述交换图表

\[
= {j}_{ * }\mathcal{T}\left( 1\right) \text{ 显然 }
\]

\( = {j}_{ * }\Phi \left( {{f}^{-1}T}\right) \; \) 根据 Thom 类的定义根据命题 \( {6.24}\left( \mathrm{a}\right) \) ,因为 \( {f}^{-1}T \) 是 \( {f}^{-1}\left( S\right) \) 的管状邻域.

这就是说，我们已证以下

命题. 设 \( M \) , \( {M}^{\prime } \) 是定向流形,光滑映射 \( f : {M}^{\prime } \rightarrow  M \) 横截于 \( M \) 的闭定向子流形 \( S \) . 若 \( \left\lbrack  {\eta }_{S}\right\rbrack \) 是 \( S \) 在 \( M \) 中的 Poincaré 对偶,则 \( {f}^{ * }\left\lbrack  {\eta }_{S}\right\rbrack \) 是 \( {f}^{-1}\left( S\right) \) 在 \( {M}^{\prime } \) 中的 Poincaré 对偶.

根据 Thom 的横截性同伦定理,任意光滑映射 \( f : {M}^{\prime } \rightarrow  M \) 光滑同伦于一个横截于 \( S \) 的光滑映射 \( {f}^{\prime } : {M}^{\prime } \rightarrow  M \) . 由于 Thom 类与闭子流形的 Poincaré 对偶是同伦不变量,所以上述命题中关于 \( f \) 的横截性假定其实是多余的.

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 补充练习 3.

代数拓扑与微分形式
