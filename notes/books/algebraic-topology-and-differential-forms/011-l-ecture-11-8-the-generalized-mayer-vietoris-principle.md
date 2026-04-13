#### 11. 广义 MV 原理

代数拓扑与微分形式 §8 The Generalized Mayer-Vietoris Principle

11. 广义 MV 原理回忆 \( \mathrm{{MV}} \) 原理. 设 \( M = U \cup  V \) ,其中 \( U, V \) 是开集. 包含序列

\[
U \cup  V = M \leftarrow  U \coprod  V\overset{{\partial }_{0}}{\underset{{\partial }_{1}}{ = }}U \cap  V
\]

诱导 MV 序列

\[
0 \rightarrow  {\Omega }^{ * }\left( {U \cup  V}\right) \overset{r}{ \rightarrow  }{\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right) \overset{\delta }{ \rightarrow  }{\Omega }^{ * }\left( {U \cap  V}\right)  \rightarrow  0
\]

其中 \( r \) 是限制映射, \( \delta \) 是差分算子. MV 序列诱导上同调的长正合序列:

\[
\cdots  \rightarrow  {H}^{q}\left( {U \cup  V}\right)  \rightarrow  {H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right)  \rightarrow  {H}^{q}\left( {U \cap  V}\right)  \rightarrow  {H}^{q + 1}\left( {U \cup  V}\right)  \rightarrow  \ldots
\]

所以在许多情形可从开集 \( U \) , \( V \) 的上同调计算 \( U \cup  V \) 的上同调. 这节要把 MV 序列从两个开集推广到可数多个开集. 主要想法来自 Weil.

- 到可数多个开子集的推广

- 双复形

- 应用

到可数多个开子集的推广

设 \( M \) 是光滑流形, \( \{ {U}_{\alpha }{\} }_{\alpha  \in  I} \) 是 \( M \) 的开覆盖, \( I \) 是可数全序集. 则有以下包含的序列:

\[
M \leftarrow  \mathop{\coprod }\limits_{{\alpha }_{0}}{U}_{{\alpha }_{0}}\overset{\overset{{\beta }_{0}}{ \leftarrow  }}{\overset{{\beta }_{1}}{ \leftarrow  }}\mathop{\coprod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{U}_{{\alpha }_{0}{\alpha }_{1}}\underset{\overset{{\beta }_{2}}{ \leftarrow  }}{\overset{{\beta }_{1}}{ \leftarrow  }}\underset{{\alpha }_{0} < {\alpha }_{1} < {\alpha }_{2}}{\overset{{\alpha }_{0}}{ \leftarrow  }}{U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\overset{ \leftarrow  }{ \leftarrow  }\cdots
\]

此处 \( {\partial }_{i} \) 是包含映射,它 “忽略”(ignores)第 \( i \) 个开集; 例如包含映射

\[
{\partial }_{1} : {U}_{\alpha \beta \gamma } \hookrightarrow  {U}_{\alpha \gamma }
\]

作这样理解: \( {U}_{\alpha \beta \gamma } \) 表示三个开集 \( {U}_{\alpha },{U}_{\beta },{U}_{\gamma } \) 相交,忽略处在第 1 个位置的开集 \( {U}_{\beta } \) ,剩下处在第 0 个位置的 \( {U}_{\alpha } \) 与第 2 个位置的 \( {U}_{\gamma } \) 相交得 \( {U}_{\alpha \gamma } \) .

包含映射 \( {\partial }_{i} \) 诱导了限制映射 \( {\delta }_{i} \) ; 例如包含映射 \( {\partial }_{1} : {U}_{\alpha \beta \gamma } \rightarrow  {U}_{\alpha \gamma } \) 诱导了

\[
{\delta }_{1} : {\Omega }^{ * }\left( {U}_{\alpha \gamma }\right)  \rightarrow  {\Omega }^{ * }\left( {U}_{\alpha \beta \gamma }\right)
\]

\[
{\omega }_{\alpha \gamma }\; \mapsto  {\omega }_{\alpha \gamma }{\left| {U}_{\alpha \beta \gamma }\right| }^{ \cdot  }
\]

补充练习 1 . 在以下图的箭头上标上算子 \( {\delta }_{i} \) . 所以相应于包含的序列有以下微分形式限制的序列:

\[
{\Omega }^{ * }\left( M\right) \overset{r}{ \rightarrow  }\mathop{\prod }\limits_{{\alpha }_{0}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{{\delta }_{0}}{ \rightarrow  }\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \underset{\overset{{\delta }_{2}}{ \rightarrow  }}{\overset{{\delta }_{1}}{ \rightarrow  }}\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1} < {\alpha }_{2}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right) \begin{matrix}  \rightarrow  \\   \rightarrow  \\   \rightarrow  \\   \rightarrow  \\  \end{matrix}
\]

![bo_d7e85t491nqc73eqefm0_235_486_615_1337_608_0.jpg](images/fu_algebraic_topology_and_differential_forms_031_bod7e85t491nqc73eqefm023548661513376080.jpg)

定义差分算子

\[
\delta  : \mathop{\prod }\limits_{{{a}_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p + 1}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}\right) \tag{18}
\]

为交错和:

\[
\delta  = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\delta }_{i}
\]

定义 8.2. 若 \( \omega  \in  \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) ,则 \( \omega \) 有分量 \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \in  {\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) . 在(18)中的差分算子 \( \delta \) 定义为

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = {\left( \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\delta }_{i}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}
\]

\[
= \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}}{|}_{{U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}}
\]

看三个简单的情形以帮助理解记忆.

(a) \( p = 0 \) . 设 \( \omega  \in  \mathop{\prod }\limits_{{\alpha }_{0}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) ,\omega  = \left( {{\omega }_{0},{\omega }_{1},{\omega }_{2},{\omega }_{3},\ldots }\right) \) .

\[
\begin{array}{lllllllll} {U}_{01} & {U}_{02} & {U}_{03} & {U}_{12} & {U}_{04} & {U}_{13} & {U}_{05} & {U}_{14} & \ldots  \end{array}
\]

\[
{\delta }_{0}\omega  = \left( {{\left. {\omega }_{1}\right| }_{{U}_{01}},{\left. \;{\omega }_{2}\right| }_{{U}_{02}},{\left. \;{\omega }_{3}\right| }_{{U}_{03}},{\left. \;{\omega }_{2}\right| }_{{U}_{12}},{\left. \;{\omega }_{4}\right| }_{{U}_{04}},{\left. \;{\omega }_{3}\right| }_{{U}_{13}},{\left. \;{\omega }_{5}\right| }_{{U}_{05}},{\left. \;{\omega }_{4}\right| }_{{U}_{14}},\;\ldots }\right)
\]

\[
{\delta }_{1}\omega  = \left( {{\left. {\omega }_{0}\right| }_{{U}_{01}},{\left. \;{\omega }_{0}\right| }_{{U}_{02}},{\left. \;{\omega }_{0}\right| }_{{U}_{03}},{\left. \;{\omega }_{1}\right| }_{{U}_{12}},{\left. \;{\omega }_{0}\right| }_{{U}_{04}},{\left. \;{\omega }_{1}\right| }_{{U}_{13}},{\left. \;{\omega }_{0}\right| }_{{U}_{05}},{\left. \;{\omega }_{1}\right| }_{{U}_{14}},\;\cdots }\right)
\]

定义

\[
{\delta \omega } = \left( {{\delta }_{0} - {\delta }_{1}}\right) \omega  = {\delta }_{0}\omega  - {\delta }_{1}\omega
\]

\[
= \left( {{\omega }_{1}{\left| {}_{{U}_{01}} - {\omega }_{0}\right| }_{{U}_{01}},\;{\omega }_{2}{\left| {}_{{U}_{02}} - {\omega }_{0}\right| }_{{U}_{02}},\;{\omega }_{3}{\left| {}_{{U}_{03}} - {\omega }_{0}\right| }_{{U}_{03}},\;{\omega }_{2}{\left| {}_{{U}_{12}} - {\omega }_{1}\right| }_{{U}_{12}},\;\ldots }\right)
\]

\( {U}_{12} \)

(b) \( p = 1 \) . 设 \( \omega  \in  \mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) ,\omega  = \left( {{\omega }_{01},{\omega }_{02},{\omega }_{03},{\omega }_{12},{\omega }_{04},{\omega }_{13},\ldots }\right) \) .

\[
\begin{array}{lllllll} {U}_{012} & {U}_{013} & {U}_{014} & {U}_{023} & {U}_{015} & {U}_{024} & {U}_{123}\ldots  \end{array}
\]

\[
{\delta }_{0}\omega  = \begin{matrix} \left( {{\omega }_{12}{\left| {}_{{U}_{012}},\;{\omega }_{13}\right| }_{{U}_{013}},\;{\omega }_{14}{\left| {}_{{U}_{014}},\;{\omega }_{23}\right| }_{{U}_{023}},\;{\omega }_{15}{\left| {}_{{U}_{015}},\;{\omega }_{24}\right| }_{{U}_{024}},\;{\omega }_{23}{|}_{{U}_{123}},\;\ldots }\right)  \end{matrix}
\]

\[
{\delta }_{1}\omega  =  - \left( {{\omega }_{02}{\left| {}_{{U}_{012}},\;{\omega }_{03}\right| }_{{U}_{013}},\;{\omega }_{04}{\left| {}_{{U}_{014}},\;{\omega }_{03}\right| }_{{U}_{023}},\;{\omega }_{05}{\left| {}_{{U}_{015}},\;{\omega }_{04}\right| }_{{U}_{024}},\;{\omega }_{13}{|}_{{U}_{123}},\;\ldots }\right)
\]

\[
{\delta }_{2}\omega  =  - \left( {{\omega }_{01}{\left| {}_{{U}_{012}},\;{\omega }_{01}\right| }_{{U}_{013}},\;{\omega }_{01}{\left| {}_{{U}_{014}},\;{\omega }_{02}\right| }_{{U}_{023}},\;{\omega }_{01}{\left| {}_{{U}_{015}},\;{\omega }_{02}\right| }_{{U}_{024}},\;{\omega }_{12}{|}_{{U}_{123}},\;\ldots }\right)
\]

定义

\[
{\delta \omega } = \left( {{\delta }_{0} - {\delta }_{1} + {\delta }_{2}}\right) \omega  = {\delta }_{0}\omega  - {\delta }_{1}\omega  + {\delta }_{2}\omega
\]

\[
= \left( {{\omega }_{12} - {\omega }_{02} + {\omega }_{01},\;{\omega }_{13} - {\omega }_{03} + {\omega }_{01},\;{\omega }_{14} - {\omega }_{04} + {\omega }_{01},\;{\omega }_{23} - {\omega }_{03} + {\omega }_{02},\;\ldots }\right)
\]

\( {U}_{014} \) \( {U}_{023} \) (c) \( p = 2 \) .

补充练习 2 . 设 \( \omega  \in  \mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1} < {\alpha }_{2}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right) \) ,

\[
\omega  = \left( {{\omega }_{012},{\omega }_{013},{\omega }_{014},{\omega }_{023},{\omega }_{015},{\omega }_{024},{\omega }_{123},\ldots }\right) .
\]

分别写出 \( {\delta }_{0}\omega ,{\delta }_{1}\omega ,{\delta }_{2}\omega ,{\delta }_{3}\omega ,{\delta \omega } \) 在开集 \( {U}_{0123},{U}_{0124},{U}_{0125},{U}_{0134},{U}_{0126} \; {U}_{0135} \) 上的分量.

命题 8.3. \( {\delta }^{2} = 0 \) . 证. 概括地说,这是成立的因为在 \( {\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 2}} \) 中两次隐去一对指标 \( {\alpha }_{i},{\alpha }_{j} \) 且具相反符号. 准确地说,

\[
{\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 2}} = \sum {\left( -1\right) }^{i}{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 2}}
\]

\[
= \mathop{\sum }\limits_{{j < i}}{\left( -1\right) }^{j}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{j}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 2}}
\]

\[
+ \mathop{\sum }\limits_{{j > i}}{\left( -1\right) }^{j - 1}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\widehat{\alpha }}_{j}\ldots {\alpha }_{p + 2}}
\]

\[
= 0\text{ 在第二个和式中把指标 }i, j\text{ 互换. }
\]

注. 到现在为止,在 \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \) 中的下标要求 \( {\alpha }_{0} < {\alpha }_{1} < \cdots  < {\alpha }_{p} \) . 一般我们允许下标的顺序是任意的, 甚至可以重复, 这只需补充规则: 交换两个指标相差一个符号.

\[
{\omega }_{\ldots \alpha \ldots \beta \ldots } =  - {\omega }_{\ldots \beta \ldots \alpha \ldots }
\]

练习8.4. 假定 \( \alpha  < \beta \) . 则 \( {\left( \delta \omega \right) }_{\ldots \beta \ldots \alpha \ldots } \) 可定义为 \( - {\left( \delta \omega \right) }_{\ldots \alpha \ldots \beta \ldots } \) 或由差分算子公式 (8.2) 定义. 证明这两个定义相等.

命题 8.5. (广义 MV 序列) 序列

\( 0 \rightarrow  {\Omega }^{ * }\left( M\right) \overset{r}{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right)  \rightarrow  \cdots \) 是正合的；换句话说，这个复形的 \( \delta \) -上同调恒等于零.

证. (1) 显然 \( r \) 是单射.

(2)在 \( \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \) 处正合.

先证 \( \ker \delta  \subset  \operatorname{im}r \) . 设 \( \omega  \in  \mathop{\prod }\limits_{{\alpha }_{0}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) ,{\delta \omega } = 0 \) ,即对任意的 \( {\alpha }_{0} < {\alpha }_{1} \) ,

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}{\alpha }_{1}} = {\left. {\omega }_{{\alpha }_{1}}\right| }_{{U}_{{\alpha }_{0}{\alpha }_{1}}} - {\left. {\omega }_{{\alpha }_{0}}\right| }_{{U}_{{\alpha }_{0}{\alpha }_{1}}} = 0.
\]

所以 \( \omega  = {\left\{  {\omega }_{{\alpha }_{0}}\right\}  }_{{\alpha }_{0} \in  I} \) 能拼成 \( M \) 上一个形式 \( \eta \) ,即 \( r\left( \eta \right)  = \omega \) .

另一方面,显然有 \( {\delta r} = 0,\operatorname{im}r \subset  \ker \delta \) .

(3) 在 \( \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) , p \geq  1 \) 处正合.

由命题 8.3 知 \( \operatorname{im}\delta  \subset  \ker \delta \) . 需证反向的包含关系. 设

\[
\omega  \in  \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) ,\;{\delta \omega } = 0.
\]

设 \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) 为从属于开覆盖 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 的单位分解. 定义

\[
\tau  \in  \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p - 1}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right) ,
\]

\( {\tau }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{{\alpha  \in  I}}{j}_{ * }\left( {{\left. {\rho }_{\alpha }\right| }_{U{\alpha }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}}{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}}\right) \; \) 此处 \( {j}_{ * } \) 是到 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) 的零延拓 \( = \mathop{\sum }\limits_{{\alpha  \in  I}}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}\; \) 简写的版本，但不会引起误解.

![bo_d7e85t491nqc73eqefm0_241_609_1126_1100_592_0.jpg](images/fu_algebraic_topology_and_differential_forms_033_bod7e85t491nqc73eqefm0241609112611005920.jpg)

则

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \mathop{\sum }\limits_{{i = 0}}^{p}{\left( -1\right) }^{i}{\tau }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= \mathop{\sum }\limits_{{\alpha  \in  I}}\mathop{\sum }\limits_{{i = 0}}^{p}{\left( -1\right) }^{i}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

因为 \( {\delta \omega } = 0 \) ,它的每个分量

\[
{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}} = {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{{i = 0}}^{p}{\left( -1\right) }^{i + 1}{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\omega }}_{i}\ldots {\alpha }_{p}} = 0.
\]

所以

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \left( {\mathop{\sum }\limits_{{\alpha  \in  I}}{\rho }_{\alpha }}\right) {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} = {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}},
\]

即 \( {\delta \tau } = \omega \) . 这就证明了 \( \ker \delta  \subset  \operatorname{im}\delta \) .

所以 \( \ker \delta  = \operatorname{im}\delta \) .

在上述证明过程中 \( \tau \) 的定义其实在复形上给出了一个同伦算子. 用 \( {K\omega } \) 记 \( \tau \) :

(8.6)

\[
{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}.
\]

则

\[
{\left( \delta K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \sum {\left( -1\right) }^{i}{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= \sum {\left( -1\right) }^{i}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
{\left( K\delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \sum {\rho }_{\alpha }{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}}
\]

\[
= \left( {\sum {\rho }_{\alpha }}\right) {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \sum {\left( -1\right) }^{i + 1}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} - {\left( \delta K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}}.
\]

因此算子

\[
K : \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right)
\]

满足

(8.7)

\[
{\delta K} + {K\delta } = \mathrm{{id}}.
\]

与 Poincaré 引理证明相同, 如果在微分复形上存在同伦算子, 那么这个复形的上同调为零. 事实上,若 \( {\delta \phi } = 0 \) ,则由 (8.7), \( {\delta K\phi } = \phi \) . 所以对上闭链, \( K \) 是 \( \delta \) 的右逆. 给定这样的 \( \phi ,{\delta \xi } = \phi \) 的所有解 \( \xi \) 的集合由 \( {K\phi } + \delta \) -上边缘组成.

双复形以下为了方便记

\[
{K}^{p, q} = {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) .
\]

\( {K}^{p, q} \) 中的元 \( \omega \) 称为 “覆盖 \( \mathcal{U} \) 的 \( q \) -形式值的 \( p \) -上链” ( \( p \) -cochain of the cover \( \mathcal{U} \) with values in the \( q \) -forms),简称为 \( q \) -形式值的 \( p \) -上链.

对任一固定的 \( q \geq  0 \) ,命题 8.3 是说

\[
{K}^{0, q}\overset{\delta }{ \rightarrow  }{K}^{1, q}\overset{\delta }{ \rightarrow  }{K}^{2, q}\overset{\delta }{ \rightarrow  }\ldots \overset{\delta }{ \rightarrow  }{K}^{p, q}\overset{\delta }{ \rightarrow  }\ldots
\]

是复形. 若 \( {\delta \omega } = 0,\omega \) 称为 \( q \) -形式值的 \( p \) -上闭链 (cocycle); 若 \( \omega  = {\delta \tau },\omega \) 称为 \( q \) -形式值的 \( p \) -上边缘 (coboundary).

另一方面,对任一固定的 \( p \geq  0 \) ,有复形

\[
{K}^{p,0}\overset{d}{ \rightarrow  }{K}^{p,1}\overset{d}{ \rightarrow  }{K}^{p,2}\overset{d}{ \rightarrow  }{K}^{p,3}\overset{d}{ \rightarrow  }\ldots \overset{d}{ \rightarrow  }{K}^{p, q}\overset{d}{ \rightarrow  }\ldots
\]

显然

\[
{d\delta } = {\delta d}
\]

因为这无非是说先限制再外微分等于先外微分再限制. 所以 \( \{ {K}^{*, * }, d,\delta \} \) 是双复形.

![bo_d7e85t491nqc73eqefm0_245_583_639_1202_908_0.jpg](images/fu_algebraic_topology_and_differential_forms_034_bod7e85t491nqc73eqefm024558363912029080.jpg)

令

\[
{K}^{n} = { \oplus  }_{p + q = n}{K}^{p, q}
\]

\[
D = {D}^{\prime } + {D}^{\prime \prime }
\]

其中

\[
{D}^{\prime } = \delta ,\;{D}^{\prime \prime } = {\left( -1\right) }^{p}d : {K}^{p, q} \rightarrow  {K}^{p, q + 1}.
\]

则

\[
D : {K}^{n} \rightarrow  {K}^{n + 1},\;{D}^{2} = 0.
\]

所以 \( \left\{  {{K}^{ * }, D}\right\} \) 是一个复形,称为由双复形形成的复形.

定义. 双复形

\[
{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)  = { \oplus  }_{p, q \geq  0}{C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)
\]

称为 Čech-de Rham 复形，它的元称为 Čech-de Rham 上链，有时简称为 \( D \) -上链. 用 \( \left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) , D}\right\} \) 表示由双复形形成的复形,它的上同调记为

\[
{H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  \text{ . }
\]

现来理解 \( {D\phi } = 0 \) .

例如设 \( \phi  \in  {K}^{2},\phi  = {\phi }^{0,2} + {\phi }^{1,1} + {\phi }^{2,0},{\phi }^{p, q} \in  {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right) \) . 若 \( {D\phi } = 0 \) ,则将 \( {D\phi } \) 按型分解,可得

\[
{D}^{\prime \prime }{\phi }^{0,2} = 0
\]

\[
\delta {\phi }^{0,2} + {D}^{\prime \prime }{\phi }^{1,1} = 0
\]

\[
\delta {\phi }^{1,1} + {D}^{\prime \prime }{\phi }^{2,0} = 0
\]

\[
\delta {\phi }^{2,0} = 0.
\]

\( \left. \begin{matrix} 0 \\  {D}^{\prime \prime } \\   \end{matrix}\right.\uparrow \)

\( {\phi }^{1,1} \)

\[
{\phi }^{0,2}\overset{\delta }{ \rightarrow  }\delta {\phi }^{0,2} + {D}^{\prime \prime }{\phi }^{1,1} = 0
\]

\[
{D}^{\prime \prime } \uparrow
\]

\[
{D}^{\prime \prime } \uparrow
\]

\( {\phi }^{2,0} \; \overset{\delta }{ \rightarrow  }0 \)

接着理解 \( \phi  = {D\psi } \) .

例如设 \( \phi  \in  {K}^{2},\phi  = {D\psi } \) . 则

\[
\phi  = D\left( {{\psi }^{0,1} + {\psi }^{1,0}}\right)  = {D}^{\prime \prime }{\psi }^{0,1} + \left( {\delta {\psi }^{0,1} + {D}^{\prime \prime }{\psi }^{1,0}}\right)  + \delta {\psi }^{1,0},
\]

即

\[
{\phi }^{0,2} = {D}^{\prime \prime }{\psi }^{0,1}
\]

\[
{\phi }^{1,1} = \delta {\psi }^{0,1} + {D}^{\prime \prime }{\psi }^{1,0}
\]

\[
{\phi }^{2,0} = \delta {\psi }^{1,0}.
\]

\[
{D}^{\prime \prime }{\psi }^{0,1} = {\phi }^{0,2}
\]

\[
{D}^{\prime \prime } \uparrow
\]

\[
{\psi }^{0,1}\;\overset{\delta }{ \rightarrow  }\delta {\psi }^{0,1} + {D}^{\prime \prime }{\psi }^{1,0} = {\phi }^{1,1}
\]

\( \psi ,1,0 \)

MV 序列可排成以下增广 (列的) 双复形.

![bo_d7e85t491nqc73eqefm0_249_392_333_1429_627_0.jpg](images/fu_algebraic_topology_and_differential_forms_035_bod7e85t491nqc73eqefm024939233314296270.jpg)

由命题 8.5 知它的所有行正合, 这是证明以下命题的关键所在.

命题 8.8.(推广的 MV 原理)双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 计算 \( M \) 的 de Rham 上同调. 更精确地说,限制映射 \( r : {\Omega }^{ * }\left( M\right)  \rightarrow  {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 诱导上同调的同构:

\[
{r}^{ * } : {H}_{dR}^{ * }\left( M\right)  \rightarrow  {H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

证. 因为 \( {Dr} = \left( {\delta  + {D}^{\prime \prime }}\right) r = {dr} = {rd}, r \) 是链映射,所以 \( r \) 诱导了上同调的映射 \( {r}^{ * } : {r}^{ * }{\left\lbrack  \omega \right\rbrack  }_{d} = {\left\lbrack  r\left( \omega \right) \right\rbrack  }_{D}. \)

(1) \( {r}^{ * } \) 是满射. 例如,证 \( {r}^{ * } : {H}_{dR}^{2}\left( M\right)  \rightarrow  {H}_{D}^{2}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\} \) 是满射. 设

\[
\phi  = {\phi }^{0,2} + {\phi }^{1,1} + {\phi }^{2,0},\;{D\phi } = 0.
\]

由 \( \delta {\phi }^{2,0} = 0 \) 与 \( \delta \) 的正合性知存在 \( {\psi }^{1,0} \) ,使得 \( {\phi }^{2,0} = \delta {\psi }^{1,0} \) . 所以

\[
\phi  - D{\psi }^{1,0} = {\phi }^{0,2} + \left( {{\phi }^{1,1} - {D}^{\prime \prime }{\psi }^{1,0}}\right) .
\]

这样已把 \( \phi \) 的 \( \left( {2,0}\right) \) -分量截掉.

从 \( D\left( {\phi  - D{\psi }^{1,0}}\right)  = 0 \) 可得 \( \delta \left( {{\phi }^{1,1} - {D}^{\prime \prime }{\psi }^{1,0}}\right)  = 0 \) . 由 \( \delta \) 的正合性存在 \( {\psi }^{0,1} \) 使得

\[
\delta {\psi }^{0,1} = {\phi }^{1,1} - {D}^{\prime \prime }{\psi }^{1,0}.
\]

所以

\[
{\phi }^{\prime } \triangleq  \phi  - D\left( {{\psi }^{1,0} + {\psi }^{0,1}}\right)  = {\phi }^{0,2} - {D}^{\prime \prime }{\psi }^{0,1} \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{2}}\right) .
\]

\( {\phi }^{\prime } \) 只含有 \( \left( {0,2}\right) \) -分量.

因为 \( D{\phi }^{\prime } = 0 \) ,即 \( d{\phi }^{\prime } = 0 = \delta {\phi }^{\prime } \) ,所以 \( {\phi }^{\prime } \) 是 \( M \) 上整体定义的闭 2-形式. 因此 \( {r}^{ * } \) 是满射:

\[
{r}^{ * }{\left\lbrack  {\phi }^{\prime }\right\rbrack  }_{d} = {\left\lbrack  {\phi }^{\prime }\right\rbrack  }_{D} = {\left\lbrack  \phi \right\rbrack  }_{D}.
\]

![bo_d7e85t491nqc73eqefm0_251_172_536_2150_651_0.jpg](images/fu_algebraic_topology_and_differential_forms_036_bod7e85t491nqc73eqefm025117253621506510.jpg)

说明: 黑的图表是原 \( {D\phi } = 0 \) ，加入红的后把 \( \phi  \in  { \oplus  }_{p + q = 2}{C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right) \) 变成 \( {\phi }^{\prime } \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{2}}\right) \) 使得 \( {\left\lbrack  \phi \right\rbrack  }_{D} = {\left\lbrack  {\phi }^{\prime }\right\rbrack  }_{D} \) .

用 \( D \) -恰当上链相继把 \( \phi \) 的 \( \left( {2,0}\right) \) -分量 \( {\phi }^{2,0} \) 与 \( \left( {1,1}\right) \) -分量 \( {\phi }^{1,1} \) 截掉. (2) \( {r}^{ * } \) 是单射. 设 \( \omega  \in  {\Omega }^{q}\left( M\right) ,{d\omega } = 0 \) . 设 \( r\left( \omega \right)  = {D\phi } \) . 设

\[
\phi  = {\phi }^{0, q - 1} + {\phi }^{1, q - 2} + \cdots  + {\phi }^{q - 1,0}.
\]

相应地把 \( {D\phi } \) 按型进行分解:

(19)

\[
r\left( \omega \right)  = {D\phi } = {D}^{\prime \prime }{\phi }^{0, q - 1} + \left( {\delta {\phi }^{0, q - 1} + {D}^{\prime \prime }{\phi }^{1, q - 2}}\right)  + \ldots
\]

\[
+ \left( {\delta {\phi }^{q - 2,1} + {D}^{\prime \prime }{\phi }^{q - 1,0}}\right)  + \delta {\phi }^{q - 1,0}.
\]

按型比较, 我们发现在上述分解中除了第一项外每项都等于零.

由于 \( \delta {\phi }^{q - 1,0} = 0 \) ,存在 \( {\psi }^{q - 2,0} \) ,使得

\[
{\phi }^{q - 1,0} = \delta {\psi }^{q - 2,0}. \tag{20}
\]

所以

\[
\phi  - D{\psi }^{q - 2,0} = {\phi }^{0, q - 1} + \cdots  + {\phi }^{q - 3,2} + \left( {{\phi }^{q - 2,1} - {D}^{\prime \prime }{\psi }^{q - 2,0}}\right) . \tag{21}
\]

这样已把 \( \phi \) 的尾巴截掉.

计算:

\[
\delta \left( {{\phi }^{q - 2,1} - {D}^{\prime \prime }{\psi }^{q - 2,0}}\right)  = \delta {\phi }^{q - 2,1} + {D}^{\prime \prime }\delta {\psi }^{q - 2,0}
\]

\[
= \delta {\phi }^{q - 2,1} + {D}^{\prime \prime }{\phi }^{q - 1,0}\;\text{ 根据等式 (20) } \tag{22}
\]

\[
= 0\;\text{ 因为 (19) 的右边的倒数第二项为零. }
\]

由 \( \delta \) 的正合性知存在 \( {\psi }^{q - 3,1} \) ,使得

\[
{\phi }^{q - 2,1} - {D}^{\prime \prime }{\psi }^{q - 2,0} = \delta {\psi }^{q - 3,1}.
\]

所以

\[
\phi  - D\left( {{\psi }^{q - 2,0} + {\psi }^{q - 3,1}}\right)  = {\phi }^{0, q - 1} + \cdots  + \left( {{\phi }^{q - 3,2} - {D}^{\prime \prime }{\psi }^{q - 3,1}}\right) .
\]

这已把 \( \phi  - D\left( {\psi }^{q - 2,0}\right) \) 的尾巴截掉. 如此继续下去, 最终可得

\[
\psi  = {\psi }^{0, q - 2} + \cdots  + {\psi }^{q - 2,0}
\]

使得 \( {\phi }^{\prime } = \phi  - {D\psi } \) 仅含有最高次即 \( \left( {q - 1}\right) \) 次形式的分量

\[
{\phi }^{\prime } = {\phi }^{0, q - 1} - {D}^{\prime \prime }{\psi }^{0, q - 2} \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{q - 1}}\right) ,
\]

并且类似于(22)的推导可得

\[
\delta {\phi }^{\prime } = 0\text{ . } \tag{23}
\]

所以 \( {\phi }^{\prime } \) 是 \( M \) 上整体定义的形式. 因为

\[
r\left( \omega \right)  = {D\phi } = D{\phi }^{\prime } = d{\phi }^{\prime },
\]

所以 \( \omega  = d{\phi }^{\prime } \) ,即 \( \left\lbrack  \omega \right\rbrack   = 0 \) .

补充练习 3 . 证明等式 (23).

应用

上述命题的证明方法具有一般性, 由此可得

断言. 若一个增广双复形的每个行是正合的, 则复形的 \( D - \) 上同调同构于初始列即增广列的上同调.

记

\[
{C}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  = \ker \left\{  {d : {C}^{p}\left( {\mathcal{U},{\Omega }^{0}}\right)  \rightarrow  {C}^{p}\left( {\mathcal{U},{\Omega }^{1}}\right) }\right\}
\]

\[
= \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}\left\{  {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right\}  \text{ 上局部常值函数 }\} .
\]

记 \( i : {C}^{p}\left( {\mathcal{U},\mathbb{R}}\right)  \hookrightarrow  {C}^{p}\left( {\mathcal{U},{\Omega }^{0}}\right) \) 为包含映射. 于是有复形:

\[
0 \rightarrow  {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }{C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }{C}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }\ldots
\]

它的上同调 \( {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 称为开覆盖 \( \mathcal{U} \) 的 Čech 上同调. 这是纯组合对象. 考虑以下增广行的双复形: 与在 (8.8) 中讨论相同, 若双复形的每个增广列是正合的, 即对 \( q \geq  1 \) ,

\[
\mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  = 0 \tag{24}
\]

![bo_d7e85t491nqc73eqefm0_256_444_451_1443_981_0.jpg](images/fu_algebraic_topology_and_differential_forms_037_bod7e85t491nqc73eqefm025644445114439810.jpg)

则

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  {H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

于是，

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \simeq  {H}_{dR}^{ * }\left( M\right)
\]

由 Poincaré 引理, \( M \) 的好覆盖 \( \mathcal{U} \) 满足条件 (24),所以得到以下定理.

定理 8.9. 若 \( \mathcal{U} \) 是 \( M \) 的好覆盖，则 \( M \) 的 de Rham 上同调同构于好覆盖 \( \mathcal{U} \) 的 Čech 上同调

\[
{H}_{dR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) .
\]

我们重述前面的要点. 首先，包含的基本序列

\[
M \leftarrow  {U}_{\alpha } \leftleftarrows  {U}_{\alpha \beta }\overset{ \leftarrow  }{ \leftarrow  }{U}_{\alpha \beta \gamma }\overset{ \leftarrow  }{ \leftarrow  }\cdots
\]

产生图表

![bo_d7e85t491nqc73eqefm0_258_434_878_1448_482_0.jpg](images/fu_algebraic_topology_and_differential_forms_038_bod7e85t491nqc73eqefm025843487814484820.jpg)

左手边是 \( M \) 上形式的微分几何,底部是覆盖 \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) 的组合,两者融合在双复形. 因为复形是广义 MV 序列,增广行对任意开覆盖是正合的. 这就得到 \( M \) 的 de Rham 上同调总是同构于双复形的上同调:

\[
{H}_{dR}^{ * }\left( M\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

另外若 \( \mathcal{U} \) 是好覆盖，则由 Poincaré 引理知增广列是正合的. 在这种情形覆盖的 Čech 上同调也同构于双复形的上同调:

\[
{H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}  .
\]

因此在 de Rham 与 Čech 之间存在同构. 这个结果给我们提供一种利用组合计算 de Rham 上同调的方法, 因为从第 5 节知道每个流形有好覆盖. 所有这三个复形能给乘积结构使得上同调之间的同构是代数同构, 见定理 14.28. Along the left-hand side is the differential geometry of forms on \( M \) , along the bottom is the combinatorics of the cover \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) , and in the double complex itself the two are mixed. As the complex is the generalized Mayer-Vietoris sequence, the augmented rows are exact, for any cover, It follow that the de Rham cohomology of \( M \) is always isomorphic to the cohomology of the double complex. If in addition \( \mathcal{U} \) is a good cover, then by the Poincaré lemma the augmented columns are exact. In that case the Čech cohomology of the cover is also isomorphic to the cohomology of the double complex. Hence there is an isomorphism between de Rham and Čech. This result provides us with a way of computing the de Rham cohomology by means of combinatorics, since from Section 5 we know that every manifold has a good cover. All three complexes here can be given product structures, in which case the isomorphisms between them are actually isomorphisms of algebras, as will be shown in (14.28).

先验地没有理由认为对 \( M \) 的不同开覆盖会有相同的 Čech 上同调. 然而,从定理 8.9 可得

推论 8.9.1. Čech 上同调 \( {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 与好覆盖 \( \mathcal{U} \) 的选取无关.

若流形是紧的,则它有有限好覆盖. 对这样一个覆盖,Čech 上同调 \( {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) \) 显然是有限维的. 这样有

推论 8.9.2. 紧流形 \( M \) 的 de Rham 上同调 \( {H}_{dR}^{ * }\left( M\right) \) 是有限维的.

事实上,有

推论 8.9.3. 若 \( M \) 有一个有限好覆盖,则 \( {H}_{dR}^{ * }\left( M\right) \) 是有限维的.

此处关于 de Rham 上同调的有限维数的证明与第 5 节的归纳证明都依赖于 MV 序列, 但它们是彼此独立的.

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 练习 8.4.

4. 补充练习 3.

代数拓扑与微分形式
