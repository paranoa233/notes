#### 11.4.2 Wallis 公式与 Stirling 公式

本小节将介绍与阶乘 \( n! \) 有关的两个重要公式,它们在处理有关阶乘的极限问题时非常有用.

第一个公式是数学家 Wallis 得到的 (1655 年)，因此称为 Wallis 公式 (其原文见 [4]). 它与 Viète 公式 (见 4.3.4 小节题 5) 都是关于圆周率的无穷乘积公式, 但在 Wallis 公式中只需要乘除运算,连开方运算也不需要. Wallis 公式对于 \( \pi \) 的近似计算没有直接影响，但是在导出 Stirling 公式中将起重要作用.

命题 11.4.1 (Wallis 公式)

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1}{{2n} + 1}{\left\lbrack  \frac{2 \cdot  4 \cdot  \cdots  \cdot  \left( {2n}\right) }{1 \cdot  3 \cdot  \cdots  \cdot  \left( {{2n} - 1}\right) }\right\rbrack  }^{2} = \frac{\pi }{2}. \tag{11.27}
\]

分析 回顾 2.3.2 小节的练习题 8 和 9，我们看到 (11.27) 左边的极限存在性是容易证明的, 困难在于求出这个极限.

从例题 10.4.9 的积分计算已知 \( {I}_{n} = {\int }_{0}^{\pi /2}{\sin }^{n}x\mathrm{\;d}x \) 的表达式为

\[
{I}_{2n} = \frac{\left( {{2n} - 1}\right) !!}{\left( {2n}\right) !!} \cdot  \frac{\pi }{2},\;{I}_{{2n} + 1} = \frac{\left( {2n}\right) !!}{\left( {{2n} + 1}\right) !!}. \tag{11.28}
\]

这里的差异是显著的,圆周率 \( \pi \) 只出现在一个公式中!

将 \( {I}_{n} \) 作为一个数列的通项,则从例题 10.2.4 已知 \( \left\{  {I}_{n}\right\} \) 是无穷小量: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{I}_{n} = \) 0. 可以想像,当 \( n \) 充分大时, \( {I}_{n} \) 与 \( {I}_{n + 1} \) 之间的差是更高阶的无穷小量 (见 310 页的图 10.3),从而 \( {I}_{{2n} + 1}/{I}_{2n} \) 的极限很有可能是 1 . 如果真是如此,则就有可能得到关于 \( \pi \) 的某种结果. 当然这里又遇到了 \( 0/0 \) 型的不定式,但是由于有表达式 (11.28), 因此不难处理.

证 在 \( 0 < x < \frac{\pi }{2} \) 时有 \( 0 < \sin x < 1 \) ,因此就有 \( {\sin }^{{2n} + 2}x < {\sin }^{{2n} + 1}x < \; {\sin }^{2n}x \) . 这样就成立 (积分) 不等式 \( {I}_{{2n} + 2} < {I}_{{2n} + 1} < {I}_{2n} \) . 利用 (11.28),得到

\[
{I}_{{2n} + 2} = \frac{{2n} + 1}{{2n} + 2} \cdot  {I}_{2n} < {I}_{{2n} + 1} < {I}_{2n}.
\]

两边除以 \( {I}_{2n} \) ,并取极限 (即夹逼),可见确实有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{I}_{{2n} + 1}}{{I}_{2n}} = 1
\]

再用 (11.28) 代入，就得到所要的结果:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1}{{2n} + 1}{\left\lbrack  \frac{\left( {2n}\right) !!}{\left( {{2n} - 1}\right) !!}\right\rbrack  }^{2} \cdot  \frac{2}{\pi } = 1
\]

注 在应用中, Wallis 公式的几个等价形式有时更为方便, 例如:

\[
\frac{\left( {2n}\right) !!}{\left( {{2n} - 1}\right) !!} \sim  \sqrt{\pi n} \tag{11.29}
\]

\[
\frac{{\left( n!\right) }^{2}{2}^{2n}}{\left( {2n}\right) !} \sim  \sqrt{\pi n} \tag{11.30}
\]

特别是公式 (11.29) 刻画了双阶乘 \( \left( {2n}\right) !! \) 与 \( \left( {{2n} - 1}\right) !! \) 之比的渐近性态,是 Wallis 公式的一种便于使用的形式.

Stirling 公式 是关于阶乘 \( n \) ! 的重要结果,具有广泛的应用. 其一般形式为

\[
\ln n! = \ln \sqrt{2\pi } + \left( {n + \frac{1}{2}}\right) \ln n - n + \frac{{B}_{2}}{1 \cdot  {2n}} + \frac{{B}_{4}}{3 \cdot  4{n}^{3}} + \cdots
\]

\[
+ \frac{{B}_{2m}}{\left( {{2m} - 1}\right) \left( {2m}\right) {n}^{{2m} - 1}} + {\theta }_{n} \cdot  \frac{{B}_{{2m} + 2}}{\left( {{2m} + 1}\right) \left( {{2m} + 2}\right) {n}^{{2m} + 1}}, \tag{11.31}
\]

其中 \( 0 < {\theta }_{n} < 1,{B}_{2n} \) 是 Bernoulli 数 (见 7.2.3 小节).

本书只给出含有上述公式右边前三项的最简单形式的 Stirling 公式的证明, 而在第二组参考题 15 中指出如何可以得到更为精细的下一个公式的证明. 一般形式的 Stirling 公式 (11.31) 可以从 Euler-Maclaurin 公式 (11.22) 推出. 其他证明方法还有很多, 有兴趣的读者可以参看近年来在《美国数学月刊》上发表的许多新方法.

命题 11.4.2 (最简单形式的 Stirling 公式) 关于阶乘 \( n \) ! 有渐近公式:

\[
n! \sim  \sqrt{2\pi n}{\left( \frac{n}{\mathrm{e}}\right) }^{n}\left( {n \rightarrow  \infty }\right) . \tag{11.32}
\]

分析 关于阶乘 \( n \) ! 的结果很多. 就本书来说,在前面的 1.3.2,2.5.5,2.7.3 各小节中都有关于 \( n \) ! 的不等式,此外还有许多与极限有关的结果. 在 2.7.1 小节中还有对于 \( n \) ! 作为无穷大量的比较: \( {a}^{n} \ll  n! \ll  {n}^{n}\left( {a > 1}\right) \) . 但如何确切地刻画 \( n! \) 的渐近性态, 当时还是不清楚. 这就是 Stirling 公式要解决的问题.

从以前的结果出发, 可以得到许多启示. 首先, 从 2.5.5 小节练习题 7 就有对每个 \( n \in  {\mathbf{N}}_{ + } \) 成立的不等式:

\[
{\left( 1 + \frac{1}{n}\right) }^{n} < {b}_{n} = \frac{n!{\mathrm{e}}^{n}}{{n}^{n}} < n \cdot  {\left( 1 + \frac{1}{n}\right) }^{n + 1}.
\]

为了研究 \( \left\{  {b}_{n}\right\} \) 的性态,自然要观察它的前后项之比,这样就有

\[
\frac{{b}_{n}}{{b}_{n + 1}} = \frac{1}{\mathrm{e}}{\left( 1 + \frac{1}{n}\right) }^{n} < 1,
\]

因此数列 \( \left\{  {b}_{n}\right\} \) 严格单调增加. 这里只不过利用了关于数 e 的最初讨论 (见命题 2.5.1). 再利用例题 8.2.3 的结论,可见以 \( {\left( 1 + \frac{1}{n}\right) }^{n + \frac{1}{2}} \) 为通项的数列严格单调减少, 且收敛于 e. 这样就得到

\[
\frac{{b}_{n}\sqrt{n + 1}}{{b}_{n + 1}\sqrt{n}} = \frac{{b}_{n}}{{b}_{n + 1}}{\left( 1 + \frac{1}{n}\right) }^{\frac{1}{2}} = \frac{1}{\mathrm{e}}{\left( 1 + \frac{1}{n}\right) }^{n + \frac{1}{2}} > 1,
\]

它就是下面证明的出发点.

证 定义数列

\[
{a}_{n} = \frac{n!{\mathrm{e}}^{n}}{{n}^{n + \frac{1}{2}}},\;n \in  {\mathbf{N}}_{ + },
\]

则只需证明 \( \left\{  {a}_{n}\right\} \) 收敛于 \( \sqrt{2\pi } \) . 为此写出其前后项之比:

\[
\frac{{a}_{n}}{{a}_{n + 1}} = \frac{1}{\mathrm{e}}{\left( 1 + \frac{1}{n}\right) }^{n + \frac{1}{2}}. \tag{11.33}
\]

利用 \( f\left( x\right)  = 1/x \) 下凸,在 Hadamard 不等式 (例题 11.2.1) 中,令 \( {x}_{1} = n,{x}_{2} = n + 1 \) 代入，得到不等式:

\[
\frac{1}{n + \frac{1}{2}} \leq  \ln \left( {1 + \frac{1}{n}}\right)  \leq  \frac{1}{2}\left( {\frac{1}{n} + \frac{1}{n + 1}}\right) .
\]

将上式乘 \( \left( {n + \frac{1}{2}}\right) \) 并作整理,得到等价的不等式:

\[
0 \leq  \left( {n + \frac{1}{2}}\right) \ln \left( {1 + \frac{1}{n}}\right)  - 1 \leq  \frac{1}{4}\left( {\frac{1}{n} - \frac{1}{n + 1}}\right) . \tag{11.34}
\]

将它与 (11.33) 作比较, 就有

\[
1 \leq  \frac{{a}_{n}}{{a}_{n + 1}} \leq  {\mathrm{e}}^{\frac{1}{4}\left( {\frac{1}{n} - \frac{1}{n + 1}}\right) }. \tag{11.35}
\]

这表明正数列 \( \left\{  {a}_{n}\right\} \) 单调减少,因此收敛,记其极限为 \( \alpha \) . 同时从 (11.35) 的右边不等式又知道另一个正数列 \( \left\{  {{a}_{n}{\mathrm{e}}^{-\frac{1}{4n}}}\right\} \) 单调增加. 由于它的极限也是 \( \alpha \) ,这样就证明了 \( \alpha  > 0 \) .

利用 Wallis 公式 (11.27) 或 (11.30),并用 \( n! = {a}_{n} \cdot  \frac{{n}^{n + \frac{1}{2}}}{{\mathrm{e}}^{n}} \) 代入,就有

\[
\sqrt{\pi } = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{\left( n!\right) }^{2}{2}^{2n}}{\left( {2n}\right) !\sqrt{n}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}^{2}}{{a}_{2n}\sqrt{2}} = \frac{{\alpha }^{2}}{\alpha \sqrt{2}}, \tag{11.36}
\]

可见极限 \( \alpha  = \sqrt{2\pi } \) .

注 对于数列 \( \left\{  {a}_{n}\right\} \) 不仅要证明它收敛,而且还必须证明其极限 \( \alpha  > 0 \) ,否则 (11.36) 的最后一步通不过. 有不少文献忽略了这一点. 上述证明来自 [8].
