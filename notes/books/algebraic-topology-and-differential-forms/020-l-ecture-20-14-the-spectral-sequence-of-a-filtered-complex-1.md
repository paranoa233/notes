#### 第20讲 The Spectral Sequence of a Filtered Complex (1)

§14. The Spectral Sequence of a Filtered Complex (1)

## 20. 谱序列

在第二章通过考虑开覆盖 \( \mathcal{U} \) 上微分形式的双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 推广了第一章的关键定理. 这个双复形是称为谱序列的代数构造的一个非常退化的实例. 谱序列是计算同调, 上同调, 甚至同伦群的有力工具. 在这章我们构造滤列复形的谱序列并给出它的各种应用，推广或重证许多以前的结果. 在构造谱序列的各种方法中，最简单的也许是 Massey 提出的通过正合偶的方法.

我们分三次课讲这一节. 这次课讲正合偶, 滤列复形的导出偶, 谱序列与谱序列的收敛. 我们在不分级的情形讲滤列复形的谱序列. 第二次课主要讲双复形的谱序列与纤维丛的谱序列, 导出 de Rham 上同调的 Leray 定理. 第三次课讲谱序列的一些应用,双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 上的积结构,以及 Leray 对一般映射的谱序列构造.

- 正合偶

- 滤列复形的导出偶

- 谱序列与谱序列的收敛

正合偶一个正合偶 (exact couple) 是如下形式的 abel 群的正合序列:

![bo_d7e85t491nqc73eqefm0_450_686_367_959_549_0.jpg](images/fu_algebraic_topology_and_differential_forms_116_bod7e85t491nqc73eqefm04506863679595490.jpg)

其中 \( i, j, k \) 是群同态. 所以

\[
\operatorname{im}i = \ker j,\;\operatorname{im}j = \ker k,\;\operatorname{im}k = \ker i.
\]

令

\[
d = j \circ  k : B \rightarrow  B.
\]

则 \( {d}^{2} = j \circ  \left( {k \circ  j}\right)  \circ  k = 0 \) . 定义

\[
H\left( B\right)  = \ker d/\mathrm{{im}}d
\]

从给定的正合偶可构造一个称为导出偶的新正合偶如下.(14.1)

![bo_d7e85t491nqc73eqefm0_451_737_253_974_557_0.jpg](images/fu_algebraic_topology_and_differential_forms_117_bod7e85t491nqc73eqefm04517372539745570.jpg)

(a) 令 \( {A}^{\prime } = i\left( A\right) ,{B}^{\prime } = H\left( B\right) \) .

(b) 定义 \( {i}^{\prime }\left( {ia}\right)  = {i}^{2}\left( a\right) \) .

(c) 对 \( {a}^{\prime } = {ia} \in  {A}^{\prime } \) ,定义 \( {j}^{\prime }\left( {a}^{\prime }\right)  = \left\lbrack  {ja}\right\rbrack \) . 检查 \( {j}^{\prime } \) 是定义好的.

(i) \( {ja} \) 是 \( d \) 闭的: \( d\left( {ja}\right)  = {jkja} = 0 \) ;

(ii) \( \left\lbrack  {ja}\right\rbrack \) 与 \( a \) 的选取无关: 若 \( {a}^{\prime } = i\bar{a} \) ,则 \( i\left( {a - \bar{a}}\right)  = 0 \) . 所以存在 \( b \in  B \) 使得 \( {kb} = a - \bar{a} \) . 这样 \( {ja} - j\bar{a} = {jkb} = {db} \) . 所以 \( \left\lbrack  {ja}\right\rbrack   = \left\lbrack  {j\bar{a}}\right\rbrack \) .

(d) 定义 \( {k}^{\prime }\left\lbrack  b\right\rbrack   = {kb} \in  i\left( A\right) \) . 这是因为 \( {jkb} = {db} = 0 \) ,所以存在 \( a \in  A \) 使得 \( {kb} = {ia} \) . 定义与 \( b \) 的选取无关:

\[
k\left( {b + {dc}}\right)  = {kb} + {kdc} = {kb} + {kjkc} = {kb}.
\]

(e) 验证 (14.1) 在 \( {B}^{\prime } \) 处正合.

(i) \( \operatorname{im}{j}^{\prime } \subset  \ker {k}^{\prime } \) .

\[
{k}^{\prime }{j}^{\prime }\left( {a}^{\prime }\right)  = {k}^{\prime }{j}^{\prime }\left( {ia}\right)  = {k}^{\prime }\left\lbrack  {ja}\right\rbrack   = {kja} = 0.
\]

(ii) \( \ker {k}^{\prime } \subset  \operatorname{im}{j}^{\prime } \) . 设 \( {k}^{\prime }\left\lbrack  b\right\rbrack   = {kb} = 0 \) . 所以存在 \( a \) 使得 \( b = {ja} \) ,

\[
\left\lbrack  b\right\rbrack   = \left\lbrack  {ja}\right\rbrack   = {j}^{\prime }\left( {ia}\right)  \in  \operatorname{im}{j}^{\prime }.
\]

(f) 验证 (14.1) 在两个 \( {A}^{\prime } \) 处正合.

补充练习 1 . 完成上述 (f).

滤列复形的导出偶设 \( \left( {K, D}\right) \) 是微分复形,即 \( K \) 是 abel 群, \( D : K \rightarrow  K \) 是群同态且 \( {D}^{2} = 0 \) . 定义

\[
{H}_{D}\left( K\right)  = \ker D/\operatorname{im}D\text{ . }
\]

若 \( {K}^{\prime } \) 是 \( K \) 的子群且 \( D{K}^{\prime } \subset  {K}^{\prime } \) ,则称 \( \left( {{K}^{\prime }, D}\right) \) 是 \( K \) 的子复形. 子复形的序列

\[
K = {K}_{0} \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  \cdots
\]

称为 \( K \) 上一个滤列 (filtration). 这使得 \( K \) 成为一个滤列复形 (filtered complex)，它的相伴分级复形是

\[
{GK} = { \oplus  }_{p = 0}^{\infty }{K}_{p}/{K}_{p + 1}.
\]

为了方便规定 \( {K}_{p} = K \) 对 \( p < 0 \) .

设

\[
A = { \oplus  }_{p \in  \mathbb{Z}}{K}_{p}
\]

则 \( \left( {A, D}\right) \) 也是一个微分复形. 定义 \( i : A \rightarrow  A \) 由包含映射 \( i : {K}_{p + 1} \hookrightarrow  {K}_{p} \) 诱导, 并定义商群 \( B \) :(14.3)

![bo_d7e85t491nqc73eqefm0_454_396_561_1784_313_0.jpg](images/fu_algebraic_topology_and_differential_forms_118_bod7e85t491nqc73eqefm045439656117843130.jpg)

所以 \( B \) 是 \( K \) 的相伴分级复形 \( {GK} \) . 每个 \( {K}_{p}/{K}_{p + 1} \) 上有诱导的微分算子 \( D \) : 对每个 \( a \in  {K}_{p} \) ,

\[
D\left( {a + {K}_{p + 1}}\right)  = {Da} + {K}_{p + 1}.
\]

所以 \( \left( {{K}_{p}/{K}_{p + 1}, D}\right) \) 是微分复形,从而 \( \left( {B, D}\right) \) 也是. 总之,有上同调

\[
{H}_{D}\left( A\right)  = { \oplus  }_{p \in  \mathbb{Z}}{H}_{D}\left( {K}_{p}\right)
\]

\[
{H}_{D}\left( B\right)  = { \oplus  }_{p \in  \mathbb{Z}}{H}_{D}\left( {{K}_{p}/{K}_{p + 1}}\right) .
\]

引理. 存在同态 \( {i}_{1},{j}_{1},{k}_{1} \) 使得(49)

![bo_d7e85t491nqc73eqefm0_455_630_306_1062_558_0.jpg](images/fu_algebraic_topology_and_differential_forms_120_bod7e85t491nqc73eqefm045563030610625580.jpg)

是正合偶. 事实上,对每个固定的 \( p \) 有正合偶(50)证. 定义 \( {i}_{1} : H\left( {K}_{p + 1}\right)  \rightarrow  H\left( {K}_{p}\right) \) 为

\[
{i}_{1}{\left\lbrack  a\right\rbrack  }_{D} = {\left\lbrack  ia\right\rbrack  }_{D}.
\]

![bo_d7e85t491nqc73eqefm0_455_591_1006_1143_574_0.jpg](images/fu_algebraic_topology_and_differential_forms_119_bod7e85t491nqc73eqefm0455591100611435740.jpg)

\( {i}_{1} \) 可能不是单射. 设 \( \left\lbrack  a\right\rbrack   \neq  0 \in  H\left( {K}_{p + 1}\right) \) ,即 \( a \) 在 \( {K}_{p + 1} \) 中是 \( D \) 闭的,但不是 \( D \) 恰当的. 但是 \( a \) 在 \( {K}_{p} \) 中可能是 \( D \) 恰当的,即 \( \left\lbrack  a\right\rbrack   = 0 \in  H\left( {K}_{p}\right) \) .

定义 \( {j}_{1} : H\left( {K}_{p}\right)  \rightarrow  H\left( {{K}_{p}/{K}_{p + 1}}\right) \) 为

\[
{j}_{1}{\left\lbrack  a\right\rbrack  }_{D} = {\left\lbrack  a + {K}_{p + 1}\right\rbrack  }_{D}.
\]

定义 \( {k}_{1} : H\left( {{K}_{p}/{K}_{p + 1}}\right)  \rightarrow  H\left( {K}_{p + 1}\right) \) 为连接同态: 对 \( a \in  {K}_{p},{Da} \in  {K}_{p + 1} \) ,定义

\[
{k}_{1}{\left\lbrack  a + {K}_{p + 1}\right\rbrack  }_{D} = {\left\lbrack  Da\right\rbrack  }_{D}.
\]

\( {Da} \) 在 \( {K}_{p + 1} \) 中不一定是 \( D \) 恰当的,所以 \( \left\lbrack  {Da}\right\rbrack \) 在 \( H\left( {K}_{p + 1}\right) \) 可能不为零. 补充练习 2 . 验证 (50) 是正合偶.

这样就完成了引理的证明. 所以我们有正合偶 (49), 把它重新记为

![bo_d7e85t491nqc73eqefm0_457_670_240_984_561_0.jpg](images/fu_algebraic_topology_and_differential_forms_121_bod7e85t491nqc73eqefm04576702409845610.jpg)

其中映射 \( i \) 不再是包含. 为了避免记号过于繁琐我们隐去了 \( {i}_{1} \) 的下标. 由于这个图表是正合偶, 按 (14.1) 可相继定义正合偶

![bo_d7e85t491nqc73eqefm0_457_675_1023_979_558_0.jpg](images/fu_algebraic_topology_and_differential_forms_122_bod7e85t491nqc73eqefm045767510239795580.jpg)

它是前一个正合偶的导出偶. 为了说明问题，考虑滤列复形

\[
\cdots  = {K}_{-1} = {K}_{0} \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  0.
\]

它在 \( {K}_{3} \) 之后终止. 则 \( {A}_{1} \) 是以下序列中所有项的直和:

\[
\ldots \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{i}{ \leftarrow  }H\left( {K}_{1}\right) \overset{i}{ \leftarrow  }H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }H\left( {K}_{3}\right)  \leftarrow  0.
\]

当然这不再是正合序列. 接着,根据定义 \( {A}_{2} \) 是 \( i : {A}_{1} \rightarrow  {A}_{1} \) 的像,所以是以下序列中所有项的直和:

\[
\ldots \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{ \sim  }{ \leftarrow  }H\left( K\right)  \supset  {iH}\left( {K}_{1}\right) \overset{i}{ \leftarrow  }{iH}\left( {K}_{2}\right) \overset{i}{ \leftarrow  }{iH}\left( {K}_{3}\right)  \leftarrow  0.
\]

注意此处映射 \( {iH}\left( {K}_{1}\right)  \subset  H\left( K\right) \) 是包含. 类似地 \( {A}_{3} \) 是以下序列中所有项的直和:

\[
\ldots \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{ \sim  }{ \leftarrow  }H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {i}^{2}H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }{i}^{2}H\left( {K}_{3}\right)  \leftarrow  0,
\]

而 \( {A}_{4} \) 是以下序列中所有项的直和:

\[
\ldots \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{ \sim  }{ \leftarrow  }H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {i}^{2}H\left( {K}_{2}\right)  \supset  {i}^{3}H\left( {K}_{3}\right)  \supset  0.
\]

因为在 \( {A}_{4} \) 中所有映射已是包含,所以在第四个导出偶之后,所有的 \( {A}_{r} \) 就固定不变了. 定义 \( {A}_{\infty } \) 为这个固定的值:

\[
{A}_{4} = {A}_{5} = {A}_{6} = \cdots  = {A}_{\infty }.
\]

其次，因为

![bo_d7e85t491nqc73eqefm0_459_669_575_987_558_0.jpg](images/fu_algebraic_topology_and_differential_forms_123_bod7e85t491nqc73eqefm04596695759875580.jpg)

是正合的且 \( i : {A}_{4} \rightarrow  {A}_{4} \) 是包含,所以 \( {k}_{4} = 0 : {B}_{4} \rightarrow  {A}_{4} \) . 于是 \( {d}_{4} = {j}_{4} \circ  {k}_{4} = 0 \) ,

\[
{B}_{5} = \ker {d}_{4}/\mathrm{{im}}{d}_{4} = {B}_{4}.
\]

由此可知

\[
{B}_{4} = {B}_{5} = {B}_{6} = \cdots  = {B}_{\infty }.
\]

在正合偶 \( {A}_{\infty } \) 是以下群的直和:

(14.4)

\[
\cdots  = H\left( K\right)  = H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {i}^{2}H\left( {K}_{2}\right)  \supset  {i}^{3}H\left( {K}_{3}\right)  \supset  0
\]

![bo_d7e85t491nqc73eqefm0_460_659_305_1009_563_0.jpg](images/fu_algebraic_topology_and_differential_forms_124_bod7e85t491nqc73eqefm046065930510095630.jpg)

并且包含 \( {i}_{\infty } \) 正如 (14.4) 所示. 因为 \( {B}_{\infty } \) 是 \( {i}_{\infty } \) 的商,所以它是包含序列 (14.4) 中相继商 (successive quotients) 的直和. 若我们设 (14.4) 是 \( H\left( K\right) \) 上滤列,则 \( {B}_{\infty } \) 是滤列复形 \( H\left( K\right) \) 的相伴分级复形:

\[
{B}_{\infty } = {GH}\left( K\right) \text{ . }
\]

小结.

给定 \( K \) 上滤列

\[
K = {K}_{0} \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  0
\]

得到上同调之间的映射

\[
H\left( K\right)  = H\left( {K}_{0}\right) \overset{i}{ \leftarrow  }H\left( {K}_{1}\right) \overset{i}{ \leftarrow  }H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }H\left( {K}_{3}\right)  \leftarrow  0,
\]

上同调的滤列

\[
H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {i}^{2}H\left( {K}_{2}\right)  \supset  {i}^{3}H\left( {K}_{3}\right)  \supset  0,
\]

以及它的相伴分级复形:

\[
{B}_{\infty } = H\left( K\right) /{iH}\left( {K}_{1}\right)
\]

\[
\oplus  \;{iH}\left( {K}_{1}\right) /{i}^{2}H\left( {K}_{2}\right)
\]

\[
\oplus  \;{i}^{2}H\left( {K}_{2}\right) /{i}^{3}H\left( {K}_{3}\right)
\]

\[
3{i}^{3}H\left( {K}_{3}\right)
\]

谱序列与谱序列的收敛现回到一般情形. \( K \) 的子复形序列

\[
\cdots  = K = K \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  \cdots
\]

诱导了上同调序列

\[
\cdots \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{ \sim  }{ \leftarrow  }H\left( K\right) \overset{i}{ \leftarrow  }H\left( {K}_{1}\right) \overset{i}{ \leftarrow  }H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }H\left( {K}_{3}\right)  \leftarrow  \cdots
\]

其中的映射 \( i \) 当然不再是包含. 设 \( {F}_{p} = {i}^{p}H\left( {K}_{p}\right) \) ,它是 \( H\left( {K}_{p}\right) \) 在 \( H\left( K\right) \) 中的像. 则有包含的序列

(14.5)

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3} \supset  \cdots ,
\]

使得 \( H\left( K\right) \) 成为一个滤列复形. 这个滤列称为 \( H\left( K\right) \) 上诱导滤列.

滤列复形 \( K \) 上一个滤列 \( \left\{  {K}_{p}\right\} \) 称为有长度 \( l \) 若 \( {K}_{l} \neq  0 \) 且对 \( p > l \) , \( {K}_{p} = 0 \) . 与上述特殊情形讨论相同,当 \( K \) 上滤列的长度有限时,则 \( {A}_{r} \) 与 \( {B}_{r} \) 最终会不变而不变的值 \( {B}_{\infty } \) 是 \( H\left( K\right) \) 上滤列 (14.5) 的相伴分级复形 \( \bigoplus {F}_{p}/{F}_{p + 1} \) . 习惯上把 \( {B}_{r} \) 记作 \( {E}_{r} \) . 因此，

\[
{E}_{1} = H\left( B\right) \text{ ,微分 }{d}_{1} = {j}_{1} \circ  {k}_{1}
\]

\[
{E}_{2} = H\left( {E}_{1}\right) \text{ ,微分 }{d}_{2} = {j}_{2} \circ  {k}_{2}
\]

\[
{E}_{3} = H\left( {E}_{2}\right) \text{ ,微分 }{d}_{3} = {j}_{3} \circ  {k}_{3}\text{ ; 等. }
\]

定义. 微分群的序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) 称为谱序列若每个 \( {E}_{r} \) 是前一个 \( {E}_{r - 1} \) 的同调. 若 \( {E}_{r} \) 最终不变了,记不变的值为 \( {E}_{\infty } \) ,并且若 \( {E}_{\infty } \) 等于某个滤列群 \( H \) 的相伴分级群,则称谱序列 \( \left\{  {{E}_{r},{d}_{r}}\right\} \) 收敛于 \( H \) ，记作

\[
\left\{  {{E}_{r},{d}_{r}}\right\}   \Rightarrow  H
\]

给定 \( K \) 上一个滤列 \( \left\{  {K}_{p}\right\} \) ,导出偶中的 \( {\left\{  {E}_{r},{d}_{r}\right\}  }_{r = 1}^{\infty } \) 是谱序列,并且当滤列 \( \left\{  {K}_{p}\right\} \) 的长度有限时,它收敛于 \( H\left( K\right) \) :

\[
\left\{  {{E}_{r},{d}_{r}}\right\}   \Rightarrow  H\left( K\right) .
\]

现假定滤列复形 \( K \) 是一个分级复形:

\[
K = {\bigoplus }_{n \in  \mathbb{Z}}{K}^{n},\;D : {K}^{n} \rightarrow  {K}^{n + 1}.
\]

为了区别分级次数 \( n \) 与滤列次数 \( p \) ,通常称 \( n \) 为维数. \( K \) 上滤列 \( \left\{  {K}_{p}\right\} \) 在每个维数诱导了一个滤列: 若令 \( {K}_{p}^{n} = {K}^{n} \cap  {K}_{p} \) ,则 \( \left\{  {K}_{p}^{n}\right\} \) 是 \( {K}^{n} \) 上一个滤列.

另一方面， \( K \) 的分级诱导了 \( {K}_{p} \) 的分级

\[
{K}_{p} = { \oplus  }_{n}{K}_{p}^{n}
\]

它也诱导了 \( {B}_{p} = {K}_{p}/{K}_{p + 1} \) 的分级*

\[
{B}_{p} = { \oplus  }_{n}{B}_{p}^{n},\;{B}_{p}^{n} = {K}_{p}^{n}/{K}_{p + 1}^{n}.
\]

于是有分级复形 \( \left( {{K}_{p}, D}\right) ,\left( {{B}_{p}, D}\right) \) 与分级复形的正合序列

\[
0 \rightarrow  {K}_{p + 1} \rightarrow  {K}_{p} \rightarrow  {B}_{p} \rightarrow  0
\]

它诱导了上同调群的长正合序列

\[
\cdots  \rightarrow  {H}^{n}\left( {K}_{p + 1}\right) \xrightarrow[]{{i}_{1}}{H}^{n}\left( {K}_{p}\right) \xrightarrow[]{{j}_{1}}{H}^{n}\left( {B}_{p}\right) \xrightarrow[]{{k}_{1}}{H}^{n + 1}\left( {K}_{p + 1}\right)  \rightarrow  \ldots
\]

*不要与前面的 \( {B}_{r} \) 混淆,现已把前面的 \( {B}_{r} \) 记作 \( {E}_{r} \) .

所以对固定的 \( p \) 有正合偶(51)

![bo_d7e85t491nqc73eqefm0_465_229_301_1836_567_0.jpg](images/fu_algebraic_topology_and_differential_forms_125_bod7e85t491nqc73eqefm046522930118365670.jpg)

对 \( p \) 求直和,有正合偶

![bo_d7e85t491nqc73eqefm0_465_236_1003_1838_583_0.jpg](images/fu_algebraic_topology_and_differential_forms_126_bod7e85t491nqc73eqefm0465236100318385830.jpg)

记 \( {A}_{1}^{n} = {\bigoplus }_{p}{H}^{n}\left( {K}_{p}\right) ,{E}_{1}^{n} = {\bigoplus }_{p}{H}^{n}\left( {B}_{p}\right) \) . 则

![bo_d7e85t491nqc73eqefm0_466_532_616_1256_575_0.jpg](images/fu_algebraic_topology_and_differential_forms_127_bod7e85t491nqc73eqefm046653261612565750.jpg)

其中 \( {k}_{1} : {E}_{1}^{n} \rightarrow  {A}_{1}^{n + 1} \) . 于是有相继的导出偶

![bo_d7e85t491nqc73eqefm0_467_409_332_1507_570_0.jpg](images/fu_algebraic_topology_and_differential_forms_128_bod7e85t491nqc73eqefm046740933215075700.jpg)

其中 \( {A}_{r}^{n} = {\bigoplus }_{p}{i}^{r - 1}{H}^{n}\left( {K}_{p}\right) \) ,而 \( {E}_{r}^{n} \) 是归纳定义的. 事实上,因为微分 \( {d}_{r} \) 是以下两个映射的复合

\[
{E}_{r}^{n}\overset{{k}_{r}}{ \rightarrow  }{A}_{r}^{n + 1}\overset{{j}_{r}}{ \rightarrow  }{E}_{r}^{n + 1}
\]

所以

\[
{E}_{r + 1}^{n} = \frac{\ker {d}_{r} : {E}_{r}^{n} \rightarrow  {E}_{r}^{n + 1}}{\operatorname{im}{d}_{r} : {E}_{r}^{n - 1} \rightarrow  {E}_{r}^{n}}.
\]

在实际应用中, \( K \) 上滤列不一定有有限长度,但对每个维数 \( n,{K}^{n} \) 上滤列 \( \left\{  {K}_{p}^{n}\right\} \) 有有限长度.

在上述假定下,设 \( l\left( n\right) \) 是 \( {\left\{  {K}_{p}^{n}\right\}  }_{p \in  \mathbb{Z}} \) 的长度. 相对于 \( H\left( K\right) \) 上滤列

\[
H\left( K\right)  \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3} \supset  \ldots ,
\]

\[
\text{ 其中 }{F}_{p} = {i}^{p}H\left( {K}_{p}\right)
\]

\( {H}^{n}\left( K\right) \) 上有长度不超过 \( l\left( n\right) \) 的滤列:

\[
{H}^{n}\left( K\right)  \supset  {F}_{1}^{n} \supset  {F}_{2}^{n} \supset  {F}_{3}^{n} \supset  \cdots  \supset  {F}_{l\left( n\right) }^{n} \supset  0
\]

\[
\text{ 其中 }{F}_{p}^{n} = {F}_{p} \cap  {H}^{n}\left( K\right)  = {i}^{p}{H}^{n}\left( {K}_{p}\right) \text{ . }
\]

固定 \( n \) ,则当 \( r \geq  l\left( {n + 1}\right)  + 1 \) 时,对任意的整数 \( p \) ,

\[
{i}^{r}{H}^{n + 1}\left( {K}_{p + 1}\right)  = {F}_{p + 1}^{n + 1}
\]

\[
i : {F}_{p + 1}^{n + 1} \rightarrow  {F}_{p}^{n + 1}\text{ 是包含. }
\]

所以 \( i : {A}_{r}^{n + 1} \rightarrow  {A}_{r}^{n + 1} \) 是包含, \( {k}_{r} : {E}_{r}^{n} \rightarrow  {A}_{r}^{n + 1} \) 是零映射. 于是 \( {d}_{r} = {j}_{r} \circ  {k}_{r} \) : \( {E}_{r}^{n} \rightarrow  {E}_{r}^{n + 1} \) 是零映射. 因此当 \( r \rightarrow  \infty \) 时, \( {E}_{r}^{n} \) 固定不变,用 \( {E}_{\infty }^{n} \) 记这个不变的值. 因为

\[
{A}_{\infty }^{n} =  \oplus  {F}_{p}^{n}
\]

且 \( {i}_{\infty } : {F}_{p + 1}^{n} \rightarrow  {F}_{p}^{n} \) 是包含,所以

\[
{E}_{\infty }^{n} = { \oplus  }_{p}{F}_{p}^{n}/{F}_{p + 1}^{n}.
\]

这就是说, \( {E}_{\infty }^{n} \) 是 \( {H}_{D}^{n}\left( K\right) \) 的相伴分级复形 \( { \oplus  }_{p}{F}_{p}^{n}/{F}_{p + 1}^{n} \) .

在上述意义下，我们说短正合序列

\[
0 \rightarrow  {\bigoplus }_{p}{K}_{p + 1} \rightarrow  {\bigoplus }_{p}{K}_{p} \rightarrow  {\bigoplus }_{p}{K}_{p}/{K}_{p + 1} \rightarrow  0
\]

诱导了一个收敛于 \( {H}_{D}^{ * }\left( K\right) \) 的谱序列. 这个收敛性比我们前面定义的收敛性要弱. 我们把前面的讨论总结成以下定理.

定理 14.6. 设 \( K = {\bigoplus }_{n \in  \mathbb{Z}}{K}^{n} \) 是滤列为 \( \left\{  {K}_{p}\right\} \) 的分级滤列复形,并且设 \( {H}_{D}^{ * }\left( K\right) \) 是 \( K \) 的上同调,具有滤列 (14.5):

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3} \supset  \cdots
\]

假定对每个维数 \( n \) ,滤列 \( \left\{  {K}_{p}^{n}\right\} \) 有有限长度. 则短正合序列

\[
0 \rightarrow   \oplus  {K}_{p + 1} \rightarrow   \oplus  {K}_{p} \rightarrow   \oplus  {K}_{p}/{K}_{p + 1} \rightarrow  0
\]

诱导了一个收敛于 \( {H}_{D}^{ * }\left( K\right) \) 的谱序列.

作业:

1. 补充练习 1.

2. 补充练习 2.

代数拓扑与微分形式
