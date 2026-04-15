#### 16.3.2 Bernstein 证明的概率解释

目前许多教科书往往采取 Bernstein 的方法来证明 Weierstrass 逼近定理. 这个证明无疑具有一系列优点, 例如, 除了 Cantor 的一致连续性定理之外, 可以不用微积分工具, 又能给出逼近多项式的显式表达式等等. 但是初学者往往难以明白它的思想从何而来. 因为 Bernstein 是从概率论出发得到这个证明的 (1912). 下面我们不重复在许多教科书中关于 Bernstein 证明的细节, 而是致力于用通俗的语言来阐明它的概率意义. 希望这些解释会对初学者有点启发作用.

首先, 将证明的主要过程列出如下.

对于区间 \( \left\lbrack  {0,1}\right\rbrack \) 上的连续函数 \( f \) 写出 Bernstein 多项式

\[
{B}_{n}\left( f\right) \left( x\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}f\left( \frac{i}{n}\right) \left( \begin{matrix} n \\  i \end{matrix}\right) {x}^{i}{\left( 1 - x\right) }^{n - i},0 \leq  x \leq  1. \tag{16.16}
\]

这里可以将 \( {B}_{n} \) 看成是带有参数 \( n \) 的算子,它作用于 \( f \) 就得到一个多项式 \( {B}_{n}\left( f\right) \) .

利用恒等式

\[
\mathop{\sum }\limits_{{i = 0}}^{n}\left( \begin{array}{l} n \\  i \end{array}\right) {x}^{i}{\left( 1 - x\right) }^{n - i} = 1 \tag{16.17}
\]

就可以用拟合法得到:

\[
{B}_{n}\left( f\right) \left( x\right)  - f\left( x\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}\left\lbrack  {f\left( \frac{i}{n}\right)  - f\left( x\right) }\right\rbrack  \left( \begin{array}{l} n \\  i \end{array}\right) {x}^{i}{\left( 1 - x\right) }^{n - i}.
\]

利用 \( f \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上一致连续,对于每个给定的 \( \varepsilon  > 0 \) ,存在 \( \delta  > 0 \) ,使得当 \( x,{x}^{\prime } \in  \left\lbrack  {0,1}\right\rbrack \) , 且 \( \left| {x - {x}^{\prime }}\right|  < \delta \) 时成立 \( \left| {f\left( x\right)  - f\left( {x}^{\prime }\right) }\right|  < \varepsilon \) . 然后将上面的和式按照 \( \left| {x - i/n}\right|  < \delta \) 和 \( \left| {x - i/n}\right|  \geq  \delta \) 分拆,即有

\[
\left| {\mathop{\sum }\limits_{{i = 0}}^{n}\left\lbrack  {f\left( \frac{i}{n}\right)  - f\left( x\right) }\right\rbrack  \left( \begin{matrix} n \\  i \end{matrix}\right) {x}^{i}{\left( 1 - x\right) }^{n - i}}\right|  \leq  \left| \mathop{\sum }\limits_{{\left| {x - \frac{i}{n}}\right|  < \delta }}\right|  + \left| \mathop{\sum }\limits_{{\left| {x - \frac{i}{n}}\right|  \geq  \delta }}\right| .
\]

对于第一个和式利用一致连续性和 (16.17) 估计如下:

\[
\left| {\mathop{\sum }\limits_{{i = 1\ldots k}}\left\lbrack  {f\left( \frac{i}{n}\right)  - f\left( x\right) }\right\rbrack  \left( \begin{array}{l} n \\  i \end{array}\right) {x}^{i}{\left( 1 - x\right) }^{n - i}}\right|
\]

\[
\leq  \mathop{\sum }\limits_{{\left| {x - \frac{i}{n}}\right|  < \delta }}^{{\left| {x - \frac{i}{n}}\right|  < \delta }}\left| {f\left( \frac{i}{n}\right)  - f\left( x\right) }\right| \left( \begin{matrix} n \\  i \end{matrix}\right) {x}^{i}{\left( 1 - x\right) }^{n - i} \leq  \varepsilon .
\]

对第二个和式则需要用一个恒等式:

\[
\mathop{\sum }\limits_{{i = 0}}^{n}{\left( \frac{i}{n} - x\right) }^{2}\left( \begin{array}{l} n \\  i \end{array}\right) {x}^{i}{\left( 1 - x\right) }^{n - i} = \frac{x\left( {1 - x}\right) }{n}, \tag{16.18}
\]

又假设 \( \left| {f\left( x\right) }\right|  \leq  M,\forall x \in  \left\lbrack  {-1,1}\right\rbrack \) ,然后就不难证明存在 \( N \) (这里的细节见收有这个证明的教科书),使得当 \( n > N \) 时第二个和式的绝对值也小于 \( \varepsilon \) . 从而就在 \( n > N \) 时得到所要的估计:

\[
\mathop{\sup }\limits_{{x \in  \left\lbrack  {0,1}\right\rbrack  }}\left\{  \left| {f\left( x\right)  - {B}_{n}\left( f\right) \left( x\right) }\right| \right\}   < {2\varepsilon }.
\]

现在我们从概率角度来解释以上过程. 其中的有关知识可以在概率论的教科书中找到 (例如 [19]). 这里所用的概率模型是 Bernoulli 的独立试验序列概型. 其中设事件 \( A \) 的概率为 \( x \in  \left\lbrack  {0,1}\right\rbrack \) ,每一次试验只有两种结果,即 \( A \) 出现,或者 \( A \) 不出现. 假设作 \( n \) 次独立试验,于是其中事件 \( A \) 出现 \( i \) 次的概率就是

\[
{B}_{i}^{n}\left( x\right)  = \left( \begin{matrix} n \\  i \end{matrix}\right) {x}^{i}{\left( 1 - x\right) }^{n - i}. \tag{16.19}
\]

这里的组合数 \( \left( \begin{matrix} n \\  i \end{matrix}\right) \) 是在 \( n \) 次试验中事件 \( A \) 出现 \( i \) 次的可能情况的个数. 例如,在前 \( i \) 次接连出现 \( A \) 但以后就再不出现 \( A \) 就是其中的可能情况之一.

这样就可以理解恒等式 (16.17) 是什么意思了. 它简单地说就是事件 \( A \) 在 \( n \) 次试验中出现 0 次,1 次,直到出现 \( n \) 次的概率之和,当然就等于 1 .

下面的问题就是在估计 (16.16) 时为什么要将和式作分拆? 又为什么要根据 \( \left| {x - i/n}\right|  < \delta \) 和 \( \left| {x - i/n}\right|  \geq  \delta \) 来分拆？为此最好要观察概率 (16.19) 作为 \( i \) 的函数的变化规律. 在图 16.1 中取定 \( x = {0.2} \) 后对于 \( n = {20} \) 与 \( n = {100} \) 的两种情况作出示意图. 在每张图中作出了坐标为 \( \left( {i/n,{B}_{i}^{n}\left( {0.2}\right) }\right) \left( {i = 0,1,\cdots , n}\right) \) 的 \( n + 1 \) 个点.

![bo_d7fsu8491nqc7381io7g_135_235_1257_1222_584_0.jpg](images/xie_analysis_exercises_lower_003_bod7fsu8491nqc7381io7g135235125712225840.jpg)

图 16.1

从图上可以看出,将点 \( \left( {i/n,{B}_{i}^{n}\left( {0.2}\right) }\right) \left( {i = 0,1,\cdots , n}\right) \) 相连得到的是一条单峰曲线,它的最大值差不多就是 \( i/n \) 与 \( x = {0.2} \) 最接近的地方. 这一点从概率角度是很直观的事实. 我们往往称 \( i/n \) 为频率. 由于事件 \( A \) 出现的概率是 \( x = {0.2} \) ,平时我们就说成每 5 次独立试验时事件 \( A \) 出现 1 次. 这当然不可能是完全准确的预言. 但是当试验次数 \( n \) 越来越大时,频率应当接近 \( x = {0.2} \) . 这个直观的猜测在概率论中有理论上的证明, 这里从略.

对比图 16.1 的两种情况，可以看出当 \( n \) 从 \( n = {20} \) 增加到 \( n = {100} \) 时，峰变得越来越窄. 这就是说当 \( n \) 变大时,频率 \( i/n \) 越来越向概率值 \( x = {0.2} \) 靠拢. 这种现象在概率论中也有专门讨论.

此外, 还要注意恒等式 (16.18) 的概率意义是度量频率偏离概率的程度, 在概率论中称为方差. 这个恒等式可以用微分法或组合计算得到. 其右边的表达式表明当 \( n \) 增大时方差是如何降低的.

最后,将和式 (16.16) 分拆的处理表明,在和式中第一个和式是提供接近 \( f\left( x\right) \) 的主要部分, 原因就在于图 16.1 中的单峰现象. 而第二个和式则依赖于 (16.18) 来解决.

注 1 虽然 Bernstein 证明有着自己的特点, 但从本质上说仍然可以归纳入核函数方法之内. 只不过代替卷积的是离散的和式 (16.16). 核函数定义中的三个条件在这里都是满足的.

注 2 关于 Bernstein 多项式在逼近理论中的地位, 以及由于 Bézier (贝齐尔) 方法的出现而得到新的发展等可以参看数学分析教科书 [8] 的第一册第 5 章. 此外, 对 Weierstrass 逼近定理的 Bernstein 证明并不一定要从概率角度来理解. Korovkin (科罗夫金) 的证明 (1953) 完全从函数论出发, 可以参考教科书 [9].
