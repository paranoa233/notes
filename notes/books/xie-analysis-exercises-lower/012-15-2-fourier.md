## §15.2 Fourier 级数的收敛性

本节讨论 Fourier 级数在各种意义上的收敛性问题, 其中包括点收敛, 在 Cesàro 意义下的收敛, 平方平均收敛和一致收敛.

为方便起见,在以下的叙述中只考虑周期 \( {2\pi } \) 的情况,但通过简单变换就可以将结论推广到一般周期的情况.

#### 15.2.1 Dirichlet 核和点收敛性

Fourier 级数的点收敛性研究主要依赖于 Dirichlet 核 (参见上册 322 页). 利用 Euler-Fourier 公式和三角变换,将函数 \( f \) 的 Fourier 级数的部分和函数列

\[
{S}_{0}\left( x\right)  = \frac{{a}_{0}}{2},{S}_{n}\left( x\right)  = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}\cos {kx} + {b}_{k}\sin {kx}}\right) , n = 1,2,\cdots ,
\]

用 Dirichlet 积分表示出来:

\[
{S}_{n}\left( x\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( {x + t}\right) {D}_{n}\left( t\right) \mathrm{d}t = \frac{1}{\pi }{\int }_{0}^{\pi }\left\lbrack  {f\left( {x + t}\right)  + f\left( {x - t}\right) }\right\rbrack  {D}_{n}\left( t\right) \mathrm{d}t, \tag{15.15}
\]

其中 \( {D}_{n} \) 是 Dirichlet 核

\[
{D}_{n}\left( x\right)  = \frac{1}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\cos {kx} = \frac{\sin \left( {n + \frac{1}{2}}\right) x}{2\sin \frac{x}{2}}. \tag{15.16}
\]

\( {D}_{n}\left( x\right) \) 是周期为 \( {2\pi } \) 的函数,在一个周期上的积分值为 \( \pi \) (见上册 (10.12)):

\[
\frac{2}{\pi }{\int }_{0}^{\pi }{D}_{n}\left( x\right) \mathrm{d}x = 1 \tag{15.17}
\]

从方法上观察, 局部化定理以及各种常见判别法都可以通过对 Dirichlet 核的研究而得到. 在图 15.2 中作出了 \( {D}_{n}\left( x\right) \) 在区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上的示意图,其中取 \( n = 9 \) . \( x = 0 \) 为 \( {D}_{n}\left( x\right) \) 的可去间断点,其极限值为 \( n + \frac{1}{2} \) ,是曲线的主峰高度. \( {D}_{n}\left( x\right) \) 的绝对值最小的两个零点 \( \pm  \pi /\left( {n + \frac{1}{2}}\right) \) 之间的主峰下的面积当 \( n \rightarrow  \infty \) 时趋于 \( \pi \) ,而其余峰谷和横轴之间的面积之和则正负相消趋于 0 . 因此公式 (15.17) 中的积分值主要就是由这个最高的主峰提供的.

\( {D}_{n}\left( x\right) \) 的这些特性使得当函数 \( g\left( x\right) \) 在 \( x = 0 \) 处满足一定条件 (例如可导) 时, 就能够建立

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1}{\pi }{\int }_{-\pi }^{\pi }{D}_{n}\left( x\right) g\left( x\right) \mathrm{d}x = g\left( 0\right) .
\]

这就是 Dirichlet 核的作用,即通过积分运算和取极限 “提取” 出函数 \( g \) 在 \( x = 0 \) 的值. 若对 \( g \) 的自变量作平移就可以得到其他点的值.

由此得到的第一个结果就是局部化定理, 它是 Fourier 级数的一个特点. 由于函数 \( f \) 的 Fourier 系数是按照 Euler-Fourier 公式通过积分得到的,因此 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处的敛散性似乎理所当然地应当与 \( f \) 在整个区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上的性态有关. 但局部化定理对此给出了完全不同的论断. 有关点收敛的各种判别法也都是在这个基础上建立起来的.

![bo_d7fsu8491nqc7381io7g_99_210_260_1238_761_0.jpg](images/xie_analysis_exercises_lower_041_bod7fsu8491nqc7381io7g9921026012387610.jpg)

图 15.2

局部化定理即是对任意小的固定正数 \( \delta \) 有渐近等式:

\[
{S}_{n}\left( x\right)  = \frac{1}{\pi }{\int }_{0}^{\delta }\left\lbrack  {f\left( {x + t}\right)  + f\left( {x - t}\right) }\right\rbrack  {D}_{n}\left( t\right) \mathrm{d}t + o\left( 1\right) \;\left( {n \rightarrow  \infty }\right) .
\]

利用 (15.17)，对于任意 \( s \) 就有

\[
{S}_{n}\left( x\right)  - s = \frac{1}{\pi }{\int }_{0}^{\pi }\left\lbrack  {f\left( {x + t}\right)  + f\left( {x - t}\right)  - {2s}}\right\rbrack  {D}_{n}\left( t\right) \mathrm{d}t. \tag{15.18}
\]

这样就可以研究在什么条件下 \( f \) 的 Fourier 级数于点 \( x \) 处收敛于 \( s \) . 由于 (15.18) 的特殊形式,经常令 \( s = \frac{1}{2}\left\lbrack  {f\left( {x}^{ + }\right)  + f\left( {x}^{ - }\right) }\right\rbrack \) ,并在一系列条件下证明 \( f \) 的 Fourier 级数收敛于这个值. 这就是教科书中的一系列判别法, 当然它们都是充分性判别法. 本书在这里不再重复.

需要指出, Fourier 级数的点收敛性是一个十分困难的问题, 即使对于连续周期函数也是如此. 这里浏览一下已经取得的进展是适宜的.

Fourier 级数的点收敛的研究进展 早期进展是举出发散的例子. 要找到一个连续函数, 使得它的 Fourier 级数在一个点上发散, 这已经不是一个平凡的问题. 自从 Du Bois-Reymond (1873) 举出了这样的例子之后, 发散点处处稠密的连续函数例子也已经找到. 若在 Lebesgue 可积函数类中考虑问题, 则 Kolmogorov (柯尔莫哥洛夫) 举出了 \( f \) 的 Fourier 级数几乎处处发散 (1923) 和处处发散 (1926) 的例子. (几乎处处是实变函数论中的概念, 在上册 304 页已有解释.)

另一方面, Lusin (卢津) 则猜测连续函数的 Fourier 级数几乎处处收敛. 由于以上所举出的各反例, 在很长的时间内很少有人相信这个猜测是正确的. 这个猜测最终在 1966 年为 Carleson (卡勒松) 正面解决,他证明了包含连续函数在内的 \( L \) 平方可积函数的 Fourier 级数一定是几乎处处收敛的. 这是一个引起轰动的重大成果. (Carleson 是 1992 年 Wolf (沃尔夫) 奖的获得者.)

#### 15.2.2 Gibbs 现象

由于 Fourier 级数的每一项是连续函数, 因此容易知道, 如果 Fourier 级数的和函数在某点不连续, 则级数在该点的邻域上不可能是一致收敛的. 但是对于 Fourier 级数来说这里还有一个更为奇特的现象, 即所谓 Gibbs (吉布斯) 现象. 这里的要点是: 若 \( {x}_{0} \) 是和函数的一个 (第一类) 间断点,则当 \( {x}_{n} \) 趋于 \( {x}_{0} \) 的左侧或右侧时,部分和的值 \( {S}_{n}\left( {x}_{n}\right) \) 不会收敛于 \( S\left( {x}_{0}\right) \) . 不但如此,下面的分析表明,这里的误差不会因 \( n \) 的增加而减少.

为简单起见, 我们先讨论具有典型意义的一个特例:

\[
S\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\sin {nx}}{n} \tag{15.19}
\]

其中 \( S\left( x\right) \) 是周期 \( {2\pi } \) 的函数: \( S\left( x\right)  = \frac{\pi  - x}{2},\forall x \in  \left( {0,{2\pi }}\right) , S\left( 0\right)  = 0 \) .

在图 15.3 中作出了级数 (15.19) 的前 10 个部分和函数的示意图.

![bo_d7fsu8491nqc7381io7g_100_113_1189_1251_770_0.jpg](images/xie_analysis_exercises_lower_001_bod7fsu8491nqc7381io7g100113118912517700.jpg)

图 15.3

同时在图 15.3 中还用两段粗黑直线表示级数 (15.19) 的和函数 \( S\left( x\right)  = \frac{\pi  - x}{2} \) , \( x \in  \left\lbrack  {-\pi ,0)\cup (0,\pi }\right\rbrack \) . 从图中已经可以看出,虽然只观察了前 10 个部分和函数,但在点 \( x = 0 \) 附近的差值 \( \left| {{S}_{n}\left( x\right)  - S\left( x\right) }\right| \) 毫无趋于 0 的趋势,更为精确的性态刻画可以总结如下. (其中只叙述 \( 0 \leq  x \leq  \pi \) 的情况,对 \( - \pi  \leq  x \leq  0 \) 的结论是类似的.)

例题 15.2.1 (Gibbs 现象) 记 \( \left\{  {{S}_{n}\left( x\right) }\right\} \) 是 Fourier 级数 (15.19) 的部分和函数列, \( S\left( x\right)  = \frac{\pi  - x}{2} \) 为该级数在区间 \( \left( {0,{2\pi }}\right) \) 上的和函数,则有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\max }\limits_{{0 \leq  x \leq  \pi }}\left\{  {{S}_{n}\left( x\right)  - S\left( x\right) }\right\}   = {\int }_{0}^{\pi }\frac{\sin t}{t}\mathrm{\;d}t - \frac{\pi }{2} \approx  \frac{\pi }{2} \times  {0.17898}.
\]

证 研究误差 \( {\varepsilon }_{n}\left( x\right)  = {S}_{n}\left( x\right)  - S\left( x\right) \) 在 \( x = 0 \) 右侧的性态. 直接计算得到

\[
\frac{\mathrm{d}{\varepsilon }_{n}\left( x\right) }{\mathrm{d}x} = \frac{1}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\cos {kx}
\]

因此就有(见前面的(15.16)

\[
\frac{\mathrm{d}{\varepsilon }_{n}\left( x\right) }{\mathrm{d}x} = {D}_{n}\left( x\right)  = \frac{\sin \left( {n + \frac{1}{2}}\right) x}{2\sin \frac{1}{2}x}.
\]

可以看出误差 \( {\varepsilon }_{n}\left( x\right) \) 的极值点为 \( {x}_{n}^{\left( m\right) } = {\pi m}/\left( {n + \frac{1}{2}}\right) , m = 1,2,\cdots ,{2n} \) . 其中当 \( m \) 为奇数时是极大值点 \( {}^{ \oplus  } \) ,当 \( m \) 为偶数时是极小值点 (参见图 15.3).

直接计算在这些极值点上的误差值:

\[
{\varepsilon }_{n}\left( {x}_{n}^{\left( m\right) }\right)  = {S}_{n}\left( {x}_{n}^{\left( m\right) }\right)  - S\left( {x}_{n}^{\left( m\right) }\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{\sin \left( {k{x}_{n}^{\left( m\right) }}\right) }{k} - \frac{\pi  - {x}_{n}^{\left( m\right) }}{2}
\]

\[
= \left( {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{\sin \left( {k{x}_{n}^{\left( m\right) }}\right) }{k{x}_{n}^{\left( m\right) }} \cdot  \frac{\pi m}{n}}\right)  \cdot  \left( \frac{n}{n + 1/2}\right)  - \frac{\pi }{2} + \frac{\pi m}{{2n} + 1}
\]

\[
= \left( {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{\sin \left( {k{x}_{n}^{\left( m\right) }}\right) }{k{x}_{n}^{\left( m\right) }} \cdot  \frac{\pi m}{n}}\right)  - \frac{\pi }{2} + O\left( \frac{1}{n}\right) .
\]

由于右边第一项可看作为 Riemann 积分和式,因此当 \( n \rightarrow  \infty \) 时就得到

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\varepsilon }_{n}\left( {x}_{n}^{\left( m\right) }\right)  = {\int }_{0}^{m\pi }\frac{\sin t}{t}\mathrm{\;d}t - \frac{\pi }{2}.
\]

容易知道当 \( m = 1 \) 时的极限值最大 \( {}^{\text{ ② }} \) ,即得到

\[
{\int }_{0}^{\pi }\frac{\sin t}{t}\mathrm{\;d}t - \frac{\pi }{2} \approx  \frac{\pi }{2} \times  {0.17898}.
\]

注 1 若取 \( {x}_{n} = c/n, n = 1,2,\cdots \) ,则类似地有 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n}\left( \frac{c}{n}\right)  = {\int }_{0}^{c}\frac{\sin t}{t}\mathrm{\;d}t \) . 取不同的 \( c \) 值,这样的极限值就会形成一个闭区间 \( \left\lbrack  {{CS}\left( {0}^{ - }\right) ,{CS}\left( {0}^{ + }\right) }\right\rbrack \) ,其中 \( C = \; \frac{2}{\pi }{\int }_{0}^{\pi }\frac{\sin t}{t}\mathrm{\;d}t \approx  {1.17898} \) . 注意: 在图 15.3 上用 \( y \) 轴上的一个粗黑直线段来代表这个区间.

注 2 虽然以上只是一个特例, 但可以用它以及它的平移来吸收一般的和函数中的所有间断点. 因此以上所得的结论、常数 18% 以及注 1 中的内容都具有普遍意义.

---

① 可以证明 \( \mathop{\max }\limits_{{0 \leq  x \leq  \pi }}\left\{  {{S}_{n}\left( x\right)  - S\left( x\right) }\right\}   = {\varepsilon }_{n}\left( {x}_{n}^{\left( 1\right) }\right) \) ，例如参考 [18] 第三卷的 700-701 小节.

② 不难证明变上限积分 \( {\int }_{0}^{x}\frac{\sin t}{t}\mathrm{\;d}t \) 的最大值也就是在 \( x = \pi \) 处达到.

---

小结 若和函数有间断点,则不可能依靠 Fourier 级数的部分和函数 \( {S}_{n}\left( x\right) \) 的 \( n \) 增加来改进近似计算的精确程度. 这是在 Fourier 级数的应用中不能忽视的问题 (可以参考 [43] 的最后一章“三角级数之和”).

注 3 以上证明的思想来自《美国数学月刊》(1980) 第 87 卷 210-212 页.

#### 15.2.3 Fourier 级数的 Cesàro 求和

到目前为止,凡是说到无穷级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛,就是指它的部分和数列收敛. 这就是由 Cauchy 提出的无穷级数的收敛定义. 但至少从 Euler 起, 就已经出现无穷级数的其他收敛定义. Cesàro 求和就是其中的一种, 它在 Fourier 级数理论中得到了重要的应用 (参见第十三章最后的几个参考题).

定义 设级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 的部分和数列为 \( {S}_{n} = {a}_{0} + {a}_{1} + \cdots  + {a}_{n}, n = 0,1,2,\cdots \) . 定义数列

\[
{\sigma }_{n} = \frac{{S}_{0} + {S}_{1} + \cdots  + {S}_{n - 1}}{n}, n = 1,2,\cdots .
\]

如果存在极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\sigma }_{n} = \sigma \) ,则称级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 在 Cesàro 意义下可求和,且定义 \( \sigma \) 为级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 的 Cesàro 和. 由 Cauchy 命题 (见上册 31 页) 知道,若数列 \( \left\{  {S}_{n}\right\} \) 收敛于数 \( S \) ，则其前 \( n \) 项的平均值 \( {\sigma }_{n} \) 构成的数列也收敛于 \( S \) ，但反之则不然. 因此若级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 在通常意义下收敛，则它在 Cesàro 意义下也收敛，且有相同的和. 这表明对于在通常意义下收敛的级数而言, Cesàro 求和没有给出新的结果.

然而在通常意义下的某些发散级数有可能在 Cesàro 意义下有和. 例如级数

\[
1 - 1 + 1 - 1 + \cdots  = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}
\]

的部分和数列为 \( {S}_{{2k} - 1} = 1,{S}_{2k} = 0, k = 1,2,\cdots \) ,因此该级数的 Cesàro 和为 \( \frac{1}{2} \) . 这就是 Euler 等数学家曾经提出过的和 (参见 \( \left\lbrack  {{26},{50}}\right\rbrack \) ).

初看起来这似乎有点荒谬, 为什么要考虑 (在通常意义下) 发散级数的和? 这样做有什么意义? 下面我们先观察 Cesàro 求和在 Fourier 级数理论中给我们带来什么结果.

命题 15.2.1 (Fejér 定理) 如果以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,并且在点 \( {x}_{0} \) 处有左、右极限 \( f\left( {x}_{0}^{ + }\right) \) 与 \( f\left( {x}_{0}^{ - }\right) \) ,则 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处在 Cesàro 意义下收敛于

\[
\frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  .
\]

特别是当 \( f \) 于点 \( {x}_{0} \) 连续时,则 Fourier 级数在点 \( {x}_{0} \) 的 Cesàro 和就等于 \( f\left( {x}_{0}\right) \) .

证 从部分和函数列 \( {S}_{n}\left( x\right) \) 的 Dirichlet 积分 (15.15) 出发计算 \( {\sigma }_{n}\left( x\right) \) ,经三角变换后可以得到 Fejér 积分:

\[
{\sigma }_{n}\left( x\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( {x + t}\right)  \cdot  \frac{1}{2n}{\left( \frac{\sin \frac{n}{2}t}{\sin \frac{1}{2}t}\right) }^{2}\mathrm{\;d}t
\]

\[
= {\int }_{0}^{\pi }\frac{f\left( {x + t}\right)  + f\left( {x - t}\right) }{2} \cdot  {F}_{n}\left( t\right) \mathrm{d}t,
\]

其中的非负函数

\[
{F}_{n}\left( t\right)  = \frac{1}{n\pi }{\left( \frac{\sin \frac{n}{2}t}{\sin \frac{1}{2}t}\right) }^{2} \tag{15.20}
\]

称为 Fejér 核. 用 \( f\left( x\right)  \equiv  1 \) 代入就得到恒等式 (见上册 330 页的题 10):

\[
{\int }_{a}^{\pi }{F}_{n}\left( t\right) \mathrm{d}t = 1 \tag{15.21}
\]

这样就可以利用 Fejér 积分和恒等式 (15.21) 将问题化为积分估计:

\[
\left| {{\sigma }_{n}\left( {x}_{0}\right)  - \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  }\right|
\]

\[
\leq  {\int }_{0}^{\pi }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t.
\]

现在对每个给定的 \( \varepsilon  > 0 \) 取 \( \delta  > 0 \) ,使得当 \( 0 \leq  t \leq  \delta \) 时,有 \( \left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  < \varepsilon \) 和 \( \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right|  < \varepsilon \) 成立,于是就有

\[
{\int }_{0}^{\delta }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t \leq  \varepsilon {\int }_{0}^{\delta }{F}_{n}\left( t\right) \mathrm{d}t \leq  \varepsilon ,
\]

这里利用了 Fejér 核的非负性和恒等式 (15.21). 再利用当 \( \delta  \leq  t \leq  \pi \) 时

\[
0 \leq  {F}_{n}\left( t\right)  \leq  \frac{1}{n\pi } \cdot  \frac{1}{{\left( \sin \frac{1}{2}\delta \right) }^{2}},
\]

就可以估计得到

\[
{\int }_{\delta }^{\pi }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t = O\left( \frac{1}{n}\right) .
\]

因此存在 \( N \) ,使得当 \( n > N \) 时有

\[
\left| {{\sigma }_{n}\left( {x}_{0}\right)  - \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  }\right|  < {2\varepsilon },
\]

这就是

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\sigma }_{n}\left( {x}_{0}\right)  = \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  .
\]

注 将 Fejér 积分的估计和 Dirichlet 积分的估计作比较, 可见这里要容易得多, 连 Riemann 引理也不需要用. 原因在于 Fejér 核是非负的, 而 Dirichlet 核则是变号的 (见图 15.2). 如前所示的 Gibbs 现象的根源都在于此. 读者可以将图 15.4 中的 Fejér 核的示意图与图 15.2 作比较. 此外, 还可以参考 [18] 第三卷的 740 小节关于正核的系统论述. 在下一章关于 Weierstrass 逼近定理的证明中我们将再次接触到这种核函数方法 (又称奇异积分方法).

由 Fejér 定理可以立即得到关于 Fourier 级数收敛的一个重要结果.

![bo_d7fsu8491nqc7381io7g_104_120_171_1244_639_0.jpg](images/xie_analysis_exercises_lower_002_bod7fsu8491nqc7381io7g10412017112446390.jpg)

图 15.4

命题 15.2.2 设以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,点 \( {x}_{0} \) 是 \( f \) 的连续点或第一类间断点,如果 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处收敛,则它一定收敛于 \( f\left( {x}_{0}\right) \) 或 \( \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack \) .

证 设 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处收敛于 \( s \) ,则其 Cesàro 和也是 \( s \) . 但由 Fejér 定理 (命题 15.2.1) 可以知道它的 Cesàro 和为 \( f\left( {x}_{0}\right) \) 或 \( \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack \) ,可见命题成立.

注 结合前面提到的 Carleson 的工作, 可以知道连续周期函数的 Fourier 级数展开式一定几乎处处成立.

对于连续的周期函数, 从 Fejér 定理还可以得到两个重要结论.

命题 15.2.3 (Fourier 级数的惟一性定理) 设 \( f \) 为周期 \( {2\pi } \) 的连续函数,且其 Fourier 系数均等于 0 : \( {a}_{0} = 0,{a}_{n} = {b}_{n} = 0, n = 1,2,\cdots \) ,则 \( f \) 必是恒等于 0 的常值函数.

证 这时 \( f \) 的 Fourier 级数的每一项都恒等于 0,因此部分和函数列 \( \left\{  {{S}_{n}\left( x\right) }\right\} \) 的每一项也都恒等于 0 . 由此就知道 \( {\sigma }_{n}\left( x\right)  \equiv  0, n = 1,2,\cdots \) . 从 Fejér 定理 (命题 15.2.1) 可见 \( f \equiv  0 \) .

注 由此可知若两个连续函数有相同的 Fourier 级数, 则这两个连续函数必相同. 注意: 这与 Taylor 级数很不一样 (参见命题 14.4.2, 67 页底注和上册 169 页的例题 6.2.4).

命题 15.2.4 (关于一致收敛的 Fejér 定理) 如果 \( f \) 是以 \( {2\pi } \) 为周期的连续函数,则它的 Fourier 级数在 Cesàro 意义下一致收敛于 \( f \) .

注 1 这只需要在命题 15.2.1 的证明中利用连续函数的 Cantor 定理 (见上册 §5.4) 即可.

注 2 由于 \( \left\{  {{\sigma }_{n}\left( x\right) }\right\} \) 是三角多项式函数列,因此已经得到了关于周期连续函数用三角多项式一致逼近的 Weierstrass 第二逼近定理. 这将在下一章中再作进一步介绍. (又见命题 15.2.8 的注和参考题 19.)

#### 15.2.4 Fourier 级数的平方平均收敛

定义 称函数列 \( \left\{  {f}_{n}\right\} \) 于区间 \( \left\lbrack  {a, b}\right\rbrack \) 上平方平均收敛于 \( f \) ,若成立

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{a}^{b}{\left| {f}_{n}\left( x\right)  - f\left( x\right) \right| }^{2}\mathrm{\;d}x = 0.
\]

从 Bessel 不等式 (即命题 15.1.7) 的证明已知

\[
{2\pi }{d}^{2}\left( {f,{S}_{n}}\right)  = {\int }_{-\pi }^{\pi }{f}^{2} - \frac{\pi {a}_{0}^{2}}{2} - \pi \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}^{2} + {b}_{k}^{2}}\right) ,
\]

因此,若 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{d}^{2}\left( {f,{S}_{n}}\right)  = 0 \) ,则 Bessel 不等式中的不等号就可换为等号. 这就是 Parseval (帕塞瓦尔) 等式, 它又称为封闭性方程, 是 Fourier 级数中最重要的公式之一.

命题 15.2.5 (Parseval 等式) 设 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和平方可积, \( f\left( x\right)  \sim \; \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) ,则有下列 Parseval 等式成立:

\[
\frac{{a}_{0}^{2}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}^{2} + {b}_{n}^{2}}\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }{f}^{2}\left( x\right) \mathrm{d}x. \tag{15.22}
\]

证 这里只列出主要步骤, 细节从略.

(1)先用连续函数在平方平均意义上逼近 \( f \) (参见上册 333 页题 5 \( ) \) . 如果 \( f \) 为广义平方可积,则还需要先用常义可积函数在平方平均意义上逼近 \( f \) ,然后再用连续函数逼近.

(2) 对于连续函数, 根据一致收敛的 Fejér 定理 (即命题 15.2.4), 存在一个三角多项式 \( {T}_{n} \) 一致逼近这个连续函数.

(3) 然后再用 \( {S}_{n} \) 在所有 \( {T}_{n} \) 中的最优性 (即命题 15.1.6),并注意到 \( {d}^{2}\left( {f,{S}_{n}}\right) \) 随 \( n \) 增大而单调减少,可见成立 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{d}^{2}\left( {f,{S}_{n}}\right)  = 0 \) ,因此所求结论为真.

注 为了阐明 Parseval 等式的几何意义, 只需要将函数空间中从正交开始的几何类比进一步做下去. 将 \( {\int }_{-\pi }^{\pi }f\left( x\right) g\left( x\right) \mathrm{d}x \) 定义为 \( f \) 与 \( g \) 的内积,并记为 \( \left( {f, g}\right) \) , 然后就可以将 \( \sqrt{\left( f, f\right) } \) 定义为 \( f \) (作为向量) 的长度 (或称为模长). 这时三角函数系中的常值函数 1 的长度为 \( \sqrt{2\pi } \) ,其余函数的长度均为 \( \sqrt{\pi } \) . 于是在 \( f \) 的 Fourier 级数中各项的长度就是 \( \frac{\sqrt{2\pi }{a}_{0}}{2},\sqrt{\pi }{a}_{n} \) 和 \( \sqrt{\pi }{b}_{n}, n = 1,2,\cdots \) . 然后再观察 Parseval 等式 (15.22), 我们就会发现它就是平面几何与立体几何中的勾股定理在函数空间中的推广. 因此我们认为所讨论的函数空间是无限维空间, 而这就是泛函分析学科将要专门研究的领域.

下面我们举例说明 Parseval 等式的一些应用.

首先解决三角函数系的完备性问题. 这里的问题是: 是否存在三角函数系以外的可积和平方可积函数 \( \varphi \) ,使 \( \varphi \) 与三角函数系中的每个函数正交,且 \( {\int }_{-\pi }^{\pi }{\varphi }^{2} \neq  0 \) ? 如果不存在这样的函数 \( \varphi \) ,就称三角函数系在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上具有完备性.

命题 15.2.6 三角函数系 \( 1,\cos x,\sin x,\cdots ,\cos {nx},\sin {nx},\cdots \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上具有完备性.

证 用反证法. 假设存在与三角函数系中每个函数正交的可积和平方可积函数 \( \varphi \) ,则它的每个 Fourier 系数都等于 0 . 由 Parseval 等式 (15.22) 即有

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }{\varphi }^{2}\left( x\right) \mathrm{d}x = \frac{{a}_{0}^{2}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}^{2} + {b}_{n}^{2}}\right)  = 0.
\]

这与假设 \( {\int }_{-\pi }^{\pi }{\varphi }^{2}\left( x\right) \mathrm{d}x \neq  0 \) 矛盾.

注 1 完备性概念也来自于日常的二维平面和三维空间. 例如, 在三维空间中两个正交向量组成的向量系是不完备的, 但三个两两正交的向量组成的向量系则是完备的.

注 2 由此又可以得到惟一性定理 (即命题 15.2.3) 的一个新证明. 因为对 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上的连续函数 \( \varphi \) 来说,从 \( {\int }_{-\pi }^{\pi }{\varphi }^{2} = 0 \) 即可推出 \( \varphi \) 恒等于 0 .

Parseval 等式的下列推广也很有用.

命题 15.2.7 (Parseval 等式的推广) 设 \( f, g \) 均在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和平方可积, \( \left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\} \) 是 \( f \) 的 Fourier 系数, \( \left\{  {\alpha }_{n}\right\}  ,\left\{  {\beta }_{n}\right\} \) 是 \( g \) 的 Fourier 系数,则成立

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( x\right) g\left( x\right) \mathrm{d}x = \frac{{a}_{0}{\alpha }_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}{\alpha }_{n} + {b}_{n}{\beta }_{n}}\right) . \tag{15.23}
\]

证 写出 \( f + g \) 和 \( f - g \) 的 Parseval 等式,相减除以 4 即得.

#### 15.2.5 Fourier 级数的一致收敛性

下面我们用 Parseval 等式来证明 Fourier 级数的一致收敛性定理. 其思路是: 从 (15.22) 左边的级数收敛可以推出级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\left| {a}_{n}\right|  + \left| {b}_{n}\right| }{n} \) 收敛,然后从导函数的 Fourier 系数出发并利用命题 15.1.2.

命题 15.2.8 设 \( f \) 是以 \( {2\pi } \) 为周期的连续函数,并且在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上除有限个点以外可导,又设 \( {f}^{\prime } \) (在任意补充有限个点上的值之后) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和平方可积, 则 \( f \) 的 Fourier 级数绝对一致收敛于 \( f \) .

证 设 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) ,则由收敛性定理知该级数处处收敛于 \( f \) . 由 M-判别法可见,只需再证明级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 与 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n} \) 绝对收敛.

设 \( {f}^{\prime } \sim  \frac{{a}_{0}^{\prime }}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}^{\prime }\cos {nx} + {b}_{n}^{\prime }\sin {nx}}\right) \) ,则 \( {a}_{0}^{\prime } = 0 \) ,由 Parseval 等式有

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }{\left( {f}^{\prime }\left( x\right) \right) }^{2}\mathrm{\;d}x = \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}^{\prime }{}^{2} + {b}_{n}^{\prime }{}^{2}}\right) .
\]

可见级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}^{\prime }{}^{2} \) 与 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}^{\prime }{}^{2} \) 都收敛. 由命题 15.1.2 得到

\[
{a}_{n} =  - \frac{{b}_{n}^{\prime }}{n},{b}_{n} = \frac{{a}_{n}^{\prime }}{n}, n = 1,2,\cdots ,
\]

从不等式

\[
\left| {a}_{n}\right|  = \left| \frac{{b}_{n}^{\prime }}{n}\right|  \leq  \frac{1}{2}\left( {{b}_{n}^{\prime }{}^{2} + \frac{1}{{n}^{2}}}\right) , n = 1,2,\cdots
\]

可知级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 绝对收敛. 同样可证级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n} \) 也绝对收敛.

注 由于在区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上的连续周期函数可以先用分段线性连续函数一致逼近, 然后对于分段线性连续函数可以用本命题, 因此就提供了 Weierstrass 第二逼近定理的另一个证明 (参见命题 15.2.4 的注 2).

本小节当然要讨论 Fourier 级数的逐项积分与逐项微分问题. 但是这里都出现了与一般的函数项级数不同的结果. 其中逐项积分出现了令人感到意外的好结果: 不论 \( f \) 的 Fourier 级数的收敛情况如何，Fourier 级数逐项积分以后得到的级数必定收敛，而且还是一致收敛.

命题 15.2.9 (Fourier 级数的逐项积分定理) 设 \( f \) 为周期 \( {2\pi } \) 的函数，在区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,且 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) ,则级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n} \) 一定收敛,并且对于 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 中的任意 \( a, b \) 成立下列逐项积分公式:

\[
{\int }_{a}^{b}f\left( t\right) \mathrm{d}t = {\int }_{a}^{b}\frac{{a}_{0}}{2}\mathrm{\;d}t + \mathop{\sum }\limits_{{n = 1}}^{\infty }{\int }_{a}^{b}\left( {{a}_{n}\cos {nt} + {b}_{n}\sin {nt}}\right) \mathrm{d}t, \tag{15.24}
\]

对于 \( a = 0, b = x \) 可以得到

\[
{\int }_{0}^{x}\left\lbrack  {f\left( t\right)  - \frac{{a}_{0}}{2}}\right\rbrack  \mathrm{d}t = \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {-\frac{{b}_{n}}{n}\cos {nx} + \frac{{a}_{n}}{n}\sin {nx}}\right) , \tag{15.25}
\]

且其中右边为等号左边的 Fourier 级数.

证 以下只对 \( f \) 为可积和平方可积给出证明. 一般情况可见 \( \left\lbrack  {{18},{36}}\right\rbrack \) 等.

这时可用推广的 Parseval 等式 (15.23). 先将它改写为

\[
{\int }_{-\pi }^{\pi }f\left( x\right) g\left( x\right) \mathrm{d}x = \frac{1}{\pi }{\int }_{-\pi }^{\pi }\frac{{a}_{0}}{2}g\left( x\right) \mathrm{d}x + \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{\pi }{\int }_{-\pi }^{\pi }g\left( x\right) \left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \mathrm{d}x.
\]

然后令

\[
g\left( x\right)  = \left\{  \begin{array}{ll} 1, & x \in  \left\lbrack  {a, b}\right\rbrack  , \\  0, & x \in  \left\lbrack  {-\pi , a)\cup (b,\pi }\right\rbrack  , \end{array}\right.
\]

代入即得所求的 (15.24). 由于级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\left| {a}_{n}\right|  + \left| {b}_{n}\right| }{n} \) 收敛，因此其他结论显然成立， 而且最后的 Fourier 级数还是一致收敛的.

注 由 Fourier 级数的逐项积分定理可知: 一个三角级数 \( {a}_{0} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + }\right. \; \left. {{b}_{n}\sin {nx}}\right) \) 能够是某个可积和绝对可积函数的 Fourier 级数的必要条件是 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n} \) 收敛. 因此, 例如

\[
\mathop{\sum }\limits_{{n = 2}}^{\infty }\frac{\sin {nx}}{\ln n},\mathop{\sum }\limits_{{n = 9}}^{\infty }\frac{\sin {nx}}{\ln \ln n}
\]

之类的三角级数,由 Dirichlet 判别法知道它们在 \( \left( {-\infty , + \infty }\right) \) 上处处收敛,但它们都不可能是任何可积和绝对可积函数的 Fourier 级数.

但是 Fourier 级数逐项求导定理的条件却要强得多. 如果以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left( {-\pi ,\pi }\right) \) 上连续可微 (这时由收敛性定理知 \( f \) 的 Fourier 级数在 \( \left( {-\pi ,\pi }\right) \) 上处处收敛于 \( f \) ),仍然不能保证 \( f \) 的 Fourier 级数逐项求导以后得到的三角级数是 \( {f}^{\prime } \) 的 Fourier 级数 (见参考题 15).

命题 15.2.10 (Fourier 级数的逐项求导定理) 设 \( f \) 是以 \( {2\pi } \) 为周期的连续函数,在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上除了有限个点外处处可导,又设 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + }\right. \; \left. {{b}_{n}\sin {nx}}\right) ,{f}^{\prime } \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上分段光滑,则对一切实数 \( x \) 成立下列逐项求导公式:

\[
\frac{{f}^{\prime }\left( {x}^{ + }\right)  - {f}^{\prime }\left( {x}^{ - }\right) }{2} = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( {a}_{n}\cos nx + {b}_{n}\sin nx\right) }^{\prime } = \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {n{b}_{n}\cos {nx} - n{a}_{n}\sin {nx}}\right) .
\]

注 在命题 15.1.2 中已经证明,只要 \( f \) 为周期 \( {2\pi } \) 的连续函数,则在 \( f \) 与 \( {f}^{\prime } \) 的两个 Fourier 级数之间就有逐项求导关系. 那时并不考虑收敛性, 证明也很简单, 但所得的结果不能称为逐项微分定理. 现在有了 \( {f}^{\prime } \) 分段光滑条件之后,就知道求导后的 Fourier 级数收敛于 \( \left\lbrack  {{f}^{\prime }\left( {x}^{ + }\right)  + {f}^{\prime }\left( {x}^{ - }\right) }\right\rbrack  /2 \) . 如果 \( {f}^{\prime } \) 连续,则级数就处处收敛于导函数 \( {f}^{\prime } \) . 若对 \( f \) 加更多的条件,则 \( {f}^{\prime } \) 的 Fourier 级数可以一致收敛. 这里的情况与一般的函数项级数的逐项微分定理也是很不相同的.

小结 从本小节可以知道, 在一致收敛性、逐项求积和逐项求导方面, Fourier 级数与幂级数完全不同. 又从 Fourier 级数和三角级数之间的关系来看, 也与 Taylor 级数和幂级数之间的关系完全不同 (参见命题 14.4.2).

#### 15.2.6 例题

Fourier 级数展开和 Parseval 等式在求级数和中常有应用. 下面是几个例子.

例题 15.2.2 求级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{4}} \) 与 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{6}} \) 的和.

解 由 (15.13) 以及收敛性定理, 我们有

\[
{x}^{2} = \frac{{\pi }^{2}}{3} + 4\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\left( -1\right) }^{n}}{{n}^{2}}\cos {nx}, x \in  \left\lbrack  {-\pi ,\pi }\right\rbrack  ,
\]

用 \( x = \pi \) 代入就得到 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}} = \frac{{\pi }^{2}}{6} \) . 然后利用

\[
{a}_{0} = \frac{2{\pi }^{2}}{3},{a}_{n} = \frac{4 \cdot  {\left( -1\right) }^{n}}{{n}^{2}},{b}_{n} = 0, n = 1,2,\cdots ,
\]

由 Parseval 等式, 就得到

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }{x}^{4}\mathrm{d}x = \frac{1}{2}{\left( \frac{2{\pi }^{2}}{3}\right) }^{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{16}{{n}^{4}}.
\]

由此解得

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{4}} = \frac{{\pi }^{4}}{90}
\]

同样,对 \( f\left( x\right)  = {x}^{3}, x \in  \left( {-\pi ,\pi }\right) \) 的 Fourier 展开式

\[
{x}^{3} = 2\mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n}\left( {6 - {\pi }^{2}{n}^{2}}\right) \frac{\sin {nx}}{{n}^{3}}, x \in  \left( {-\pi ,\pi }\right)
\]

应用 Parseval 等式，可以得到

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }{x}^{6}\mathrm{\;d}x = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left\lbrack  2 \cdot  {\left( -1\right) }^{n}\left( 6 - {\pi }^{2}{n}^{2}\right) \frac{1}{{n}^{3}}\right\rbrack  }^{2},
\]

整理后得到

\[
\frac{2}{7}{\pi }^{6} = \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {\frac{4{\pi }^{4}}{{n}^{2}} - \frac{{48}{\pi }^{2}}{{n}^{4}} + \frac{144}{{n}^{6}}}\right) ,
\]

再利用 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{4}} = \frac{{\pi }^{4}}{90} \) 与 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}} = \frac{{\pi }^{2}}{6} \) ,即可解得 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{6}} = \frac{{\pi }^{6}}{945} \) .

例题 15.1.2 之解 3 在学了 Fourier 级数的逐项积分定理后可以如下求出在区间 \( \left( {-\pi ,\pi }\right) \) 上函数 \( {x}^{3} \) 的 Fourier 级数,并同时确定其收敛性.

第一步与过去一样, 先求出 (15.12). 然后逐项积分得到等式

\[
{x}^{2} = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}\frac{4}{{n}^{2}}\left( {1 - \cos {nx}}\right) ,
\]

其中的常数项虽是个无穷级数, 但可以不必去管它, 只需直接按照公式 (15.1) \( \left( {n = 0}\right) \) 就可以得到所要的常数项 \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{x}^{2}\mathrm{\;d}x = \frac{{\pi }^{2}}{3} \) ，因此就得到 Fourier 余弦级数展开式

\[
{x}^{2} = \frac{{\pi }^{2}}{3} + 4\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\left( -1\right) }^{n}}{{n}^{2}}\cos {nx}.
\]

再用逐项积分方法得到等式

\[
{x}^{3} = {\pi }^{2}x + {12}\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\left( -1\right) }^{n}}{{n}^{3}}\sin {nx}.
\]

在第一项中将 \( x \) 用它的 Fourier 级数代替,就得到与解 1 相同的答案.

下面将对于系数单调的 Fourier 级数作讨论, 其中的方法和结果都很有意义, 并与过去的许多讨论有联系. 这里的材料见 [18] 第三卷的 692 小节.

例题 15.2.3 设数列 \( \left\{  {b}_{n}\right\} \) 单调收敛于 0,且已知级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n} \) 收敛，则函数 \( f\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\sin {nx} \) 于区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积.

证 从函数项级数的 Dirichlet 一致收敛判别法知道 \( f \) 在 \( x \neq  0 \) 时连续,因此只有点 \( x = 0 \) 可能是瑕点. 以下只需要证明: 当点 \( x = 0 \) 为瑕点时 \( \left| f\right| \) 在 \( \left\lbrack  {0,\pi }\right\rbrack \) 上广义可积. 为此将下列积分作分拆:

\[
{\int }_{\pi /\left( {n + 1}\right) }^{\pi }\left| {f\left( x\right) }\right| \mathrm{d}x = \mathop{\sum }\limits_{{k = 1}}^{n}{\int }_{\pi /\left( {k + 1}\right) }^{\pi /k}\left| {f\left( x\right) }\right| \mathrm{d}x.
\]

对于 \( \pi /\left( {k + 1}\right)  \leq  x \leq  \pi /k \) 时的函数 \( f \) 作估计如下:

\[
\left| {f\left( x\right) }\right|  \leq  \left| {\mathop{\sum }\limits_{{i = 1}}^{k}{b}_{i}\sin {ix}}\right|  + \left| {\mathop{\sum }\limits_{{i = k + 1}}^{\infty }{b}_{i}\sin {ix}}\right| ,
\]

其中右边第一项不超过 \( {S}_{k} = {b}_{1} + {b}_{2} + \cdots  + {b}_{k} \) ,而第二项可利用 \( \left\{  {b}_{n}\right\} \) 非负单调减少的条件和 Abel 变换 (13.22) 估计如下 (参见例题 14.1.8):

\[
\left| {\mathop{\sum }\limits_{{i = k + 1}}^{\infty }{b}_{i}\sin {ix}}\right|  \leq  \frac{{b}_{k + 1}}{\left| \sin x/2\right| } \leq  \frac{{b}_{k + 1}}{\left| x/\pi \right| } \leq  \left( {k + 1}\right) {b}_{k + 1} \leq  \left( {k + 1}\right) {b}_{k}
\]

因此就有

\[
{\int }_{\pi /\left( {k + 1}\right) }^{\pi /k}\left| {f\left( x\right) }\right| \mathrm{d}x \leq  \left\lbrack  {{S}_{k} + \left( {k + 1}\right) {b}_{k}}\right\rbrack   \cdot  \frac{\pi }{k\left( {k + 1}\right) } = \pi \left\lbrack  {\frac{{S}_{k}}{k\left( {k + 1}\right) } + \frac{{b}_{k}}{k}}\right\rbrack  .
\]

令 \( k = 1,2,\cdots , n \) 代入并相加,就得到

\[
{\int }_{\pi /\left( {n + 1}\right) }^{\pi }\left| {f\left( x\right) }\right| \mathrm{d}x \leq  \pi \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{S}_{k}}{k\left( {k + 1}\right) } + \pi \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{b}_{k}}{k}.
\]

对右边第一项利用例题 13.2.7 中的类似方法可以得到

\[
\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{S}_{k}}{k\left( {k + 1}\right) } = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{k\left( {k + 1}\right) }\mathop{\sum }\limits_{{i = 1}}^{k}{b}_{i} = \mathop{\sum }\limits_{{i = 1}}^{n}{b}_{i}\mathop{\sum }\limits_{{k = i}}^{n}\frac{1}{k\left( {k + 1}\right) } = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{b}_{i}}{i} - \frac{{S}_{n}}{n + 1},
\]

从 \( {b}_{n} \rightarrow  0 \) (用 Cauchy 命题) 可见右边第二项当 \( n \rightarrow  \infty \) 时也趋于 0,因此有

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{S}_{n}}{n\left( {n + 1}\right) } = \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n}
\]

并最后估计得到

\[
{\int }_{\pi /\left( {n + 1}\right) }^{\pi }\left| {f\left( x\right) }\right| \mathrm{d}x \leq  {2\pi }\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n}
\]

因此积分 \( {\int }_{0}^{\pi }\left| {f\left( x\right) }\right| \mathrm{d}x \) 收敛.

例题 15.2.4 设数列 \( \left\{  {b}_{n}\right\} \) 单调收敛于 0,且已知 \( f\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\sin {nx} \) 于 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积,则 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\sin {nx} \) 是 \( f \) 的 Fourier 级数.

证 由于 \( f \) 于 \( x \neq  0 \) 时连续,只需讨论 \( x = 0 \) 为瑕点时的情况. 利用广义积分的 Abel 判别法可知积分 \( {\int }_{-\pi }^{\pi }f\left( x\right) \cos {nx}\mathrm{\;d}x \) 和 \( {\int }_{-\pi }^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x \) 均收敛. 由于 \( f \) 为奇函数,因此就得到 \( {a}_{n} = 0, n = 0,1,\cdots \) . 以下只要证明 \( {b}_{n} = 2{\int }_{0}^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x \) , \( n = 1,2,\cdots \) .

写出

\[
2{\int }_{0}^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x = 2{\int }_{0}^{\pi }\left( {\mathop{\sum }\limits_{{k = 1}}^{\infty }{b}_{k}\sin {kx}\sin {nx}}\right) \mathrm{d}x,
\]

从 \( \left\{  {b}_{k}\right\} \) 单调收敛于 0,又用三角变换和 Jordan 不等式可知对任意 \( m \geq  1 \) 有

\[
\left| {\mathop{\sum }\limits_{{k = 1}}^{m}\sin {kx}\sin {nx}}\right|  \leq  \left| \frac{\sin {nx}}{\sin \left( {x/2}\right) }\right|  \leq  \left| \frac{nx}{x/\pi }\right|  = {n\pi },
\]

因此从 Dirichlet 一致收敛判别法知道积分号下的级数在 \( \left\lbrack  {0,\pi }\right\rbrack \) 上一致收敛,用逐项积分计算就可以得到所求的结果.

非 Fourier 级数的三角级数 合并以上两个结果就可以知道当 \( \left\{  {b}_{n}\right\} \) 单调趋于 0 时,处处收敛的三角级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\sin {nx} \) 是其和函数 \( f \) 的 Fourier 级数的充分必要条件是数项级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n} \) 收敛 \( {}^{\text{ ① }} \) . 因此在 Bessel 不等式 (即命题 15.1.7) 后的注 2 中举出的例子 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\sin {nx}}{{n}^{p}}\left( {0 < p \leq  \frac{1}{2}}\right) \) 仍然是其和函数 \( f \) 的 Fourier 级数,当然 \( f \) 不平方可积. 不难证明该注中的另一个例子也是如此 \( {}^{\text{ ② }} \) .

但在命题 15.2.9 后所举的例子,如 \( \mathop{\sum }\limits_{{n = 2}}^{\infty }\frac{\sin {nx}}{\ln n} \) 等,则确实不是 Fourier 级数,而且它的和函数一定不是可积和绝对可积函数.

关于三角级数何时必为 Fourier 级数有下列著名结果, 上面的例题 15.2.4 只是它的一个特例.

---

① 这里可以与例题 14.1.7 和 14.1.8 的结果进行比较,可见要使得 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{n}\sin {nx} \) 在 \( \left( {-\infty , + \infty }\right) \) 上一致收敛的条件要强得多.

② 这是因为对于余弦三角级数有与例题 15.2.3 和 15.2.4 类似的结论, 证明也是类似的.

---

命题 15.2.11 (Du Bois-Reymond 定理) 在下列两种情况下的三角级数必是其和函数的 Fourier 级数: (1) 在区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上处处收敛的三角级数的和函数在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上常义可积; (2) 在区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上除有限个点外收敛的三角级数,其和函数在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上绝对可积.

在三角级数展开方面的重要结果还有展开的惟一性定理 (请与命题 15.2.3 在条件和结论两个方面进行比较).

命题 15.2.12 (Cantor 定理) 如果有两个三角级数 \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + }\right. \; \left. {{b}_{n}\sin {nx}}\right) \) 和 \( \frac{{\alpha }_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{\alpha }_{n}\cos {nx} + {\beta }_{n}\sin {nx}}\right) \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上收敛于同一个函数,则这两个三角级数必恒同: \( {a}_{n} = {\alpha }_{n}\left( {n = 0,1,\cdots }\right) ,{b}_{n} = {\beta }_{n}\left( {n = 1,2,\cdots }\right) \) .

小结 虽然我们不能在这里证明这些定理, 但还应当理解它们的重要意义 (证明见 [18] 第三卷的 750-751 小节): 这就是在理论上证明了, 在三角级数展开式中我们所见所用的绝大多数情况都是 Fourier 级数展开式.

#### 15.2.7 练习题

1. 定义函数 \( f\left( x\right)  = \left\{  \begin{array}{ll} x, & x \in  \left( {0,\frac{\pi }{2}}\right) , \\  \frac{\pi }{4}, & x = \frac{\pi }{2},\;\text{ 将 }f\text{ 展开为余弦级数,并求数项级数 } \\  x - \frac{\pi }{2}, & x \in  \left( {\frac{\pi }{2},\pi }\right) , \end{array}\right. \; \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\left( -1\right) }^{n - 1}}{{2n} - 1} \) 的值.

2. 设对于 \( a > 0 \) 有函数 \( f\left( x\right)  = \left\{  \begin{array}{ll} x, & x \in  \left\lbrack  {0,\frac{a}{2}}\right\rbrack  , \\  a - x, & x \in  \left( {\frac{a}{2}, a}\right\rbrack  , \end{array}\right. \) 将 \( f \) 展开为: (1) 余弦级数, (2) 正弦级数.

3. 设 \( \alpha \) 为非整数，利用 \( f\left( x\right)  = \cos {\alpha x}, x \in  \left\lbrack  {-\pi ,\pi }\right\rbrack \) 的 Fourier 展开式，证明下列关于余切函数和余割函数的部分分式展开式:

\[
\cot x = \frac{1}{x} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {\frac{1}{x - {n\pi }} + \frac{1}{x + {n\pi }}}\right)  = \frac{1}{x} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{2x}{{x}^{2} - {n}^{2}{\pi }^{2}},
\]

\[
\csc x = \frac{1}{x} + \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n}\left( {\frac{1}{x - {n\pi }} + \frac{1}{x + {n\pi }}}\right)  = \frac{1}{x} + \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n}\frac{2x}{{x}^{2} - {n}^{2}{\pi }^{2}},
\]

且求出级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2} - {\alpha }^{2}} \) 的和.

4. 将下列函数在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上展开为 Fourier 级数:

(1) \( f\left( x\right)  = \left| {\sin x}\right| ;\left( 2\right) f\left( x\right)  = \left\{  \begin{array}{ll} {ax}, & x \in  \lbrack  - \pi ,0), \\  {bx}, & x \in  \left\lbrack  {0,\pi }\right\rbrack  . \end{array}\right. \)

5. 将下列函数展开为正弦级数:

(1) \( f\left( x\right)  = {\mathrm{e}}^{-{2x}}, x \in  \left\lbrack  {0,\pi }\right\rbrack  ; \) (2) \( f\left( x\right)  = \left\{  \begin{array}{ll} \cos \frac{\pi x}{2}, & x \in  \lbrack 0,1), \\  0, & x \in  \left\lbrack  {1,2}\right\rbrack  . \end{array}\right. \)

6. 将下列函数展开为余弦级数:

(1) \( f\left( x\right)  = x\left( {\pi  - x}\right) , x \in  \left\lbrack  {0,\pi }\right\rbrack  ; \) (2) \( f\left( x\right)  = \left\{  \begin{array}{ll} \sin {2x}, & x \in  \left\lbrack  {0,\frac{\pi }{4}}\right) , \\  1, & x \in  \left\lbrack  {\frac{\pi }{4},\frac{\pi }{2}}\right\rbrack  . \end{array}\right. \)

7. 设函数

\[
f\left( x\right)  = \left\{  \begin{array}{ll} \pi  - x, & 0 < x \leq  \pi , \\  0, & x = 0, \\   - \pi  - x, &  - \pi  < x < 0, \end{array}\right.
\]

(1) 求 \( f \) 的 Fourier 展开式;

(2) 讨论 \( f \) 的 Fourier 级数在 \( ( - \pi ,\pi \rbrack \) 上是否收敛于 \( f \) ,是否一致收敛?

8. 设 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,证明: \( \forall \varepsilon  > 0 \) ,存在三角多项式 \( {P}_{n}\left( x\right)  = \; \mathop{\sum }\limits_{{k = 0}}^{n}\left( {{A}_{k}\cos {kx} + {B}_{k}\sin {kx}}\right) \) ,使

\[
{\int }_{-\pi }^{\pi }\left| {f\left( x\right)  - {P}_{n}\left( x\right) }\right| \mathrm{d}x < \varepsilon .
\]

9. 设 \( f \) 为周期 \( {2\pi } \) 的连续函数,且已知 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) ,证明: 若右边的级数一致收敛,则其和函数一定就是 \( f \) .

10. 设 \( 0 < a < \pi \) ，定义函数

\[
f\left( x\right)  = \left\{  \begin{array}{ll} 1, & \left| x\right|  < a, \\  0, & a \leq  \left| x\right|  < \pi . \end{array}\right.
\]

利用 \( f \) 的 Parseval 等式,求下列级数的和: \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\sin }^{2}{na}}{{n}^{2}},\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{\cos }^{2}{na}}{{n}^{2}} \) .
