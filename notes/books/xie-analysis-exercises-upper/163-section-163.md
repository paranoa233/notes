## 第二组参考题

1. (1) 求 \( \mathop{\sum }\limits_{{k = 1}}^{n}\sin {kx} \) 和 \( \mathop{\sum }\limits_{{k = 1}}^{n}\cos {kx} \) ;

(2) 求 \( \mathop{\sum }\limits_{{k = 1}}^{n}k\sin {kx} \) 和 \( \mathop{\sum }\limits_{{k = 1}}^{n}k\cos {kx} \) .

2. 证明: (例题 5.1.4 中的) Riemann 函数 \( R\left( x\right) \) 处处不可导.

3. 若从点 \( \left( {{x}_{0},{y}_{0}}\right) \) 向抛物线 \( y = a{x}^{2} + {bx} + c \) 能够作出两条切线,或只能作出一条切线,或不能作出切线,问: 在这三种情况中的 \( \left( {{x}_{0},{y}_{0}}\right) \) 的位置与抛物线有什么关系?

4. 证明: Legendre 多项式 \( {P}_{n}\left( x\right)  = \frac{1}{{2}^{n}n!}\frac{{\mathrm{d}}^{n}}{\mathrm{\;d}{x}^{n}}{\left( {x}^{2} - 1\right) }^{n} \) 满足方程

\[
{P}_{n + 1}^{\prime }\left( x\right)  - {P}_{n - 1}^{\prime }\left( x\right)  = \left( {{2n} + 1}\right) {P}_{n}\left( x\right) .
\]

5. 证明: Legendre 多项式满足方程

\[
\left( {1 - {x}^{2}}\right) {P}_{n}^{\prime \prime }\left( x\right)  - {2x}{P}_{n}^{\prime }\left( x\right)  + n\left( {n + 1}\right) {P}_{n}\left( x\right)  = 0.
\]

6. 分析三项式 \( {\left( u + v + w\right) }^{n} \) 展开的系数规律,猜测并证明 \( {\left( uvw\right) }^{\left( n\right) } \) 的一般计算公式.

7. 设 \( f\left( x\right)  = a{x}^{2} + {bx} + c \) ,当 \( \left| x\right|  \leq  1 \) 时, \( \left| {f\left( x\right) }\right|  \leq  1 \) . 证明: 当 \( \left| x\right|  \leq  1 \) 时, \( \left| {{f}^{\prime }\left( x\right) }\right|  \leq  4 \) .

8. 证明: 对每个正整数 \( n \) ,成立

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\  k \end{array}\right) {k}^{m} = \left\{  \begin{array}{ll} 0, & 0 \leq  m \leq  n - 1, \\  {\left( -1\right) }^{n}n!, & m = n. \end{array}\right.
\]

9. 设 \( f\left( x\right)  = {x}^{n}\ln x, n \in  {\mathbf{N}}_{ + } \) ,求 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{f}^{\left( n\right) }\left( {1/n}\right) }{n!} \) .

10. 设 \( f \) 在 \( x = 0 \) 处连续,且存在极限 \( \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{f\left( {2x}\right)  - f\left( x\right) }{x} = A \) . 证明: \( {f}^{\prime }\left( 0\right)  = A \) .

11. 设 \( y = {\left( 1 + \sqrt{x}\right) }^{{2n} + 2}, n \in  {\mathbf{N}}_{ + } \) ,求 \( {y}^{\left( n\right) }\left( 1\right) \) .

12. 设 \( f\left( x\right) \) 在区间 \( I \) 上三阶可导, \( {f}^{\prime }\left( x\right)  \neq  0 \) ,则可以定义 \( f\left( x\right) \) 的 Schwarz 导数如下:

\[
S\left( {f, x}\right)  = \frac{{f}^{\prime \prime \prime }\left( x\right) }{{f}^{\prime }\left( x\right) } - \frac{3}{2}{\left( \frac{{f}^{\prime \prime }\left( x\right) }{{f}^{\prime }\left( x\right) }\right) }^{2} = {\left( \frac{{f}^{\prime \prime }\left( x\right) }{{f}^{\prime }\left( x\right) }\right) }^{\prime } - \frac{1}{2}{\left( \frac{{f}^{\prime \prime }\left( x\right) }{{f}^{\prime }\left( x\right) }\right) }^{2}.
\]

证明:

(1) 若 \( f\left( x\right)  = \left( {{ax} + b}\right) /\left( {{cx} + d}\right) \) ,即分式线性函数,则 \( S\left( {f, x}\right)  = 0 \) ;

(2)若 \( p\left( x\right) \) 是 \( x \) 的多项式,且 \( {p}^{\prime }\left( x\right)  = 0 \) 的根都是互不相等的实数,则 \( S\left( {p, x}\right)  < \) 0 ;

(3) 若 \( f, g \) 具有所需的各阶导数,则 \( S\left( {f \circ  g, x}\right)  = S\left( {f, g\left( x\right) }\right) {\left( {g}^{\prime }\left( x\right) \right) }^{2} + S\left( {g, x}\right) \) ;

(4) 若 \( S\left( {f, x}\right)  < 0, S\left( {g, x}\right)  < 0 \) ,则 \( S\left( {f \circ  g, x}\right)  < 0 \) ;

(5) 若 \( S\left( {f, x}\right)  < 0 \) ,又记 \( {f}^{n} = \underset{n\text{ 个 }f}{\underbrace{f \circ  f \circ  \cdots  \circ  f}} \) ,则 \( S\left( {{f}^{n}, x}\right)  < 0 \) .
