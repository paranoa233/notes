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
