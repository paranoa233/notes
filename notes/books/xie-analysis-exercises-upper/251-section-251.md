## 第二组参考题

1. (连续量的平均值) 设 \( f \) 为 \( \lbrack 0, + \infty ) \) 上的单调函数,定义 \( f \) 的平均值为

\[
F\left( x\right)  = \left\{  \begin{array}{ll} f\left( {0}^{ + }\right) , & x = 0, \\  \frac{1}{x}{\int }_{0}^{x}f\left( t\right) \mathrm{d}t, & x > 0. \end{array}\right.
\]

证明: (1) \( F \) 在 \( \lbrack 0, + \infty ) \) 上为单调连续函数,且与 \( f \) 具有相同的单调性; (2) \( F\left( {+\infty }\right)  = f\left( {+\infty }\right) . \)

2. 证明: \( f \in  R\left\lbrack  {a, b}\right\rbrack \) 且 \( {\int }_{a}^{b}f = I \) 的充分必要条件是存在 \( \left\lbrack  {a, b}\right\rbrack \) 的一个分划序列 \( {\left\{  {P}_{k}\right\}  }_{k \in  {\mathbf{N}}_{ + }} \) ,满足条件 \( \mathop{\lim }\limits_{{k \rightarrow  \infty }}\begin{Vmatrix}{P}_{k}\end{Vmatrix} = 0 \) ,使得 \( \mathop{\lim }\limits_{{k \rightarrow  \infty }}\mathop{\sum }\limits_{{i = 1}}^{{n}_{k}}f\left( {\xi }_{k, i}\right) \Delta {x}_{k, i} = I \) ,而且极限值不依赖于介点集的选取.

(本题表明在 Riemann 积分的定义中分划的任意性要求可以降低. 例如用等距分划也是可以的.)

3. 设 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上有界,证明: 如果存在常数 \( I \) ,使对每个 \( \varepsilon  > 0 \) ,存在 \( \delta  > 0 \) ,对 \( \left\lbrack  {a, b}\right\rbrack \) 的任意分划 \( P = \left\{  {{x}_{0},{x}_{1},\cdots ,{x}_{n}}\right\} \) ,只要 \( \parallel P\parallel  < \delta \) ,就有 \( \left| {\mathop{\sum }\limits_{{i = 1}}^{n}f\left( {x}_{i}\right) \Delta {x}_{i} - I}\right|  < \varepsilon \) , 则 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) 且 \( {\int }_{a}^{b}f = I \) .

(不引入介点集来定义的积分在历史上称为 Cauchy 积分. 本题表明对于有界函数来说, Cauchy 积分与 Riemann 积分一致.)

4. (Riemann 定理) 设 \( f \in  R\left\lbrack  {a, b}\right\rbrack  , g \) 以 \( T \) 为周期且在 \( \left\lbrack  {0, T}\right\rbrack \) 上可积,证明:

\[
\mathop{\lim }\limits_{{p \rightarrow   + \infty }}{\int }_{a}^{b}f\left( x\right) g\left( {px}\right) \mathrm{d}x = \frac{1}{T}{\int }_{0}^{T}g\left( x\right) \mathrm{d}x{\int }_{a}^{b}f\left( x\right) \mathrm{d}x.
\]

5. 设 \( f \) 是一个 \( n \) 次多项式,且满足条件 \( {\int }_{0}^{1}{x}^{k}f\left( x\right) \mathrm{d}x = 0, k = 1,2,\cdots , n \) ,证明:

\[
{\int }_{0}^{1}{f}^{2}\left( x\right) \mathrm{d}x = {\left( n + 1\right) }^{2}{\left( {\int }_{0}^{1}f\left( x\right) \mathrm{d}x\right) }^{2}.
\]

6. 计算下列积分:

(1) \( {\int }_{0}^{\pi /2}{\cos }^{n}x\cos {nx}\mathrm{\;d}x \) (2) \( {\int }_{0}^{\pi /2}{\cos }^{n}x\sin {nx}\mathrm{\;d}x \) .

7. 证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{0}^{1}{\cos }^{n}\frac{1}{x}\mathrm{\;d}x = 0 \) .

8. 1996 年发现了计算圆周率的全新算法, 它可以计算圆周率在任意指定位数上的数字, 而不必求出在这一位之前的每一位数字. 这种算法的基础是关于圆周率的新公式. 它涉及一个积分的两种计算方法. 下面的问题就是其中的前一半. 其余部分见下册的例题 16.2.6.

证明:

\[
{\int }_{0}^{1/\sqrt{2}}\frac{4\sqrt{2} - 8{x}^{3} - 4\sqrt{2}{x}^{4} - 8{x}^{5}}{1 - {x}^{8}}\mathrm{\;d}x = \pi .
\]
