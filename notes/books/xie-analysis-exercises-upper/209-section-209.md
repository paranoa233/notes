## 第二组参考题

1. 设 \( f \) 在 \( \left( {0, + \infty }\right) \) 上单调减少、可微,且满足不等式 \( 0 < f\left( x\right)  < \left| {{f}^{\prime }\left( x\right) }\right| \) ,证明: 当 \( 0 < x < 1 \) 时,成立不等式

\[
{xf}\left( x\right)  > \frac{1}{x}f\left( \frac{1}{x}\right) .
\]

2. 若 \( f\left( 0\right)  = 0 \) ,且存在 \( {f}^{\left( n + 1\right) }\left( 0\right) \) ,定义

\[
g\left( x\right)  = \left\{  \begin{array}{ll} \frac{f\left( x\right) }{x}, & x \neq  0, \\  {f}^{\prime }\left( 0\right) , & x = 0, \end{array}\right.
\]

证明: \( g\left( x\right) \) 的 \( n \) 阶导函数 \( {g}^{\left( n\right) }\left( x\right) \) 在 \( x = 0 \) 连续,且 \( {g}^{\left( n\right) }\left( 0\right)  = \frac{1}{n + 1}{f}^{\left( n + 1\right) }\left( 0\right) \) .

(例题 8.1.9 的推广.)

3. 设 \( f \) 在点 \( a \) 存在 \( {f}^{\left( n\right) }\left( a\right) \) ,且 \( f\left( a\right)  = 0 \) . 令 \( F\left( x\right)  = {\left\lbrack  f\left( x\right) \right\rbrack  }^{n} \) ,证明: 对于 \( k = \; 0,1,\cdots , n - 1,{F}^{\left( k\right) }\left( a\right)  = 0 \) . 又举例说明: 导数 \( {f}^{\left( n\right) }\left( a\right) \) 存在的条件不能去掉.

4. 记 \( {P}_{n}\left( x\right)  = 1 + \frac{x}{1!} + \frac{{x}^{2}}{2!} + \cdots  + \frac{{x}^{n}}{n!}, n \in  {\mathbf{N}}_{ + } \) ,证明:

(1) \( n \) 为偶数时， \( {P}_{n}\left( x\right)  > 0,\forall x \in  \mathbf{R} \) ；

( 2 ) \( n \) 为奇数时， \( {P}_{n}\left( x\right) \) 有唯一的实零点；

(3) 若将 \( {P}_{{2n} + 1}\left( x\right) \) 的零点记为 \( {x}_{n}, n \in  {\mathbf{N}}_{ + } \) ,则 \( \left\{  {x}_{n}\right\} \) 是严格单调减少的负无穷大量;

(4) 当 \( x < 0 \) 时,成立不等式 \( {P}_{2n}\left( x\right)  > {\mathrm{e}}^{x} > {P}_{{2n} + 1}\left( x\right) \) ;

(5) 当 \( x > 0 \) 时,成立不等式 \( {\mathrm{e}}^{x} > {P}_{n}\left( x\right)  \geq  {\left( 1 + \frac{x}{n}\right) }^{n} \) ;

(6) 对一切 \( x \in  \mathbf{R} \) ,成立 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{P}_{n}\left( x\right)  = {\mathrm{e}}^{x} \) .

5. 定义 \( {x}_{0} = a,{x}_{1} = b,{x}_{n + 1} = \frac{\left( {{2n} - 1}\right) {x}_{n} + {x}_{n - 1}}{2n} \) ,求 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} \) .

6. 设 \( 0 < {x}_{0} < {y}_{0} \leq  \frac{\pi }{2} \) ,并用递推公式 \( {x}_{n + 1} = \sin {x}_{n} \) 和 \( {y}_{n + 1} = \sin {y}_{n} \) 生成两个数列 \( \left\{  {x}_{n}\right\} \) 和 \( \left\{  {y}_{n}\right\} \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{n}}{{y}_{n}} = 1 \) .

7. 证明: 若函数 \( y = \frac{a{x}^{2} + {2bx} + c}{\alpha {x}^{2} + {2\beta x} + \gamma }\left( {\alpha  \neq  0}\right) \) 有三个拐点,则它们必在一条直线上.

8. 下凸函数的 Jensen 定义是: 称函数 \( f \) 在区间 \( I \) 上为下凸,如果对所有 \( {x}_{1},{x}_{2} \in \; I \) ,成立

\[
f\left( \frac{{x}_{1} + {x}_{2}}{2}\right)  \leq  \frac{1}{2}\left\lbrack  {f\left( {x}_{1}\right)  + f\left( {x}_{2}\right) }\right\rbrack  .
\]

证明: 对连续函数来说,下凸的 Jensen 定义和 \( \text{ § }{8.4} \) 中的下凸定义等价.

(确实存在按 Jensen 定义为下凸但不满足 \( \text{ § }{8.4} \) 中的下凸定义的函数,例题 5.1.3 的不连续解就是如此 (参见 \( \left\lbrack  {{54},{56},{58}}\right\rbrack \) ).)

9. 设 \( f \) 在区间 \( \left( {a, b}\right) \) 上按 Jensen 定义为下凸函数,且至多只有第一类间断点,证明: \( f \) 在 \( \left( {a, b}\right) \) 上连续.

10. 设 \( f \) 在区间 \( \left( {a, b}\right) \) 上按 Jensen 定义为下凸函数,且在 \( \left( {a, b}\right) \) 内的每个闭子区间上有界,证明: \( f \) 在 \( \left( {a, b}\right) \) 上连续.

11. 函数 \( f \) 在区间 \( \left( {-1,1}\right) \) 上二阶可微, \( f\left( 0\right)  = {f}^{\prime }\left( 0\right)  = 0 \) ,且在该区间上满足不等式 \( \left| {{f}^{\prime \prime }\left( x\right) }\right|  \leq  \left| {f\left( x\right) }\right|  + \left| {{f}^{\prime }\left( x\right) }\right| \) ,证明: \( f\left( x\right)  \equiv  0 \) .

12. 设 \( f\left( x\right) \) 为区间 \( I \) 上的可微函数,满足微分方程 \( {f}^{\prime }\left( x\right)  = g\left( {f\left( x\right) }\right) \) ,其中 \( g \) 是在 \( f \) 的值域上有定义的函数,证明: \( f \) 一定是单调函数.

13. 证明: 在 \( \left( {-\infty , + \infty }\right) \) 上二阶可微的函数 \( f \) 不可能对于一切 \( x \) ,同时满足不等式

\[
f\left( x\right)  > 0,{f}^{\prime }\left( x\right)  > 0,{f}^{\prime \prime }\left( x\right)  < 0.
\]

14. 设 \( f \) 在 \( \mathbf{R} \) 上三阶可微,证明: 存在一个点 \( a \) 使得

\[
f\left( a\right) {f}^{\prime }\left( a\right) {f}^{\prime \prime }\left( a\right) {f}^{\prime \prime \prime }\left( a\right)  \geq  0.
\]

15. 设 \( p\left( x\right) \) 是多项式,证明: 若对每个 \( x \) 成立不等式

\[
{p}^{\prime \prime \prime }\left( x\right)  - {p}^{\prime \prime }\left( x\right)  - {p}^{\prime }\left( x\right)  + p\left( x\right)  \geq  0,
\]

则 \( p\left( x\right)  \geq  0 \) 对每个 \( x \) 成立.

16. 设 \( P \) 为多项式, \( P\left( x\right)  = 0 \) 有 \( n \) 个大于 1 的互异实根,令

\[
Q\left( x\right)  = \left( {{x}^{2} + 1}\right) P\left( x\right) {P}^{\prime }\left( x\right)  + x\left\lbrack  {{\left( P\left( x\right) \right) }^{2} + {\left( {P}^{\prime }\left( x\right) \right) }^{2}}\right\rbrack  ,
\]

证明: \( Q\left( x\right)  = 0 \) 至少有 \( {2n} - 1 \) 个互异实根.

(下面两个题用于证明在第二章第二组参考题 18 中所用到的结论.)

17. 设 \( f\left( x\right)  = {a}^{x} \) ,证明:

(1)如 \( a > {\mathrm{e}}^{\frac{1}{\mathrm{e}}} \) ，则 \( f \) 无不动点；

(2)如 \( a = {\mathrm{e}}^{\frac{1}{\mathrm{e}}} \) ，则 \( f \) 恰有一个不动点；

(3) 如 \( 1 < a < {\mathrm{e}}^{\frac{1}{\mathrm{e}}} \) ，则 \( f \) 有两个不动点.

18. 设 \( g\left( x\right)  = {a}^{{a}^{x}} \) ,证明:

(1) 如 \( {\mathrm{e}}^{-\mathrm{e}} \leq  a < 1 \) ,则 \( g \) 只有一个不动点;

(2) 如 \( 0 < a < {\mathrm{e}}^{-\mathrm{e}} \) ,则 \( g \) 有三个不动点.

19. 讨论三角方程 \( a\sin \theta  + b\cos \theta  - \sin \theta \cos \theta  = 0 \) 在 \( \lbrack 0,{2\pi }) \) 中的实根个数.

20. 从平面上的一个定点向一个给定的椭圆可以引出多少条法线? 讨论在什么区域上法线的条数最多. (参见后面 412 页上关于本题所附的图 1 和图 2.)

(本题以及类似的问题最早是由 Apollonius (阿波罗尼奥斯, 约公元前 262 - 前 190 年) 提出和解决的. 又见于《数学译林》(1992) 第 4 期, 即 V. I. Arnold 给出的《构成对物理专业学生的最低限度的数学的一百个问题》中的第 7 题.)
