## 第二组参考题

1. 先证明不等式 (12.8), 然后由

\[
{\int }_{0}^{1}{\left( 1 - {x}^{2}\right) }^{n}\mathrm{\;d}x \leq  {\int }_{0}^{+\infty }{\mathrm{e}}^{-n{x}^{2}}\mathrm{\;d}x \leq  {\int }_{0}^{+\infty }\frac{\mathrm{d}x}{{\left( 1 + {x}^{2}\right) }^{n}}
\]

出发, 用夹逼方法计算概率积分.

2. (Gordon 不等式) 证明: 函数 \( f\left( x\right)  = {\mathrm{e}}^{\frac{{x}^{2}}{2}}{\int }_{x}^{+\infty }{\mathrm{e}}^{-\frac{{t}^{2}}{2}}\mathrm{\;d}t \) 在 \( x > 0 \) 时严格单调减少, 且成立

\[
\frac{x}{{x}^{2} + 1} < f\left( x\right)  < \frac{1}{x}.
\]

3. 设 \( f \in  C\lbrack 0, + \infty ) \) 且平方可积,令 \( g\left( x\right)  = {\int }_{0}^{x}f\left( t\right) \mathrm{d}t \) ,证明: \( \frac{g\left( x\right) }{x} \) 在 \( \lbrack 0, + \infty ) \) 上平方可积, 且成立

\[
{\int }_{0}^{+\infty }\frac{{g}^{2}\left( x\right) }{{x}^{2}}\mathrm{\;d}x \leq  4{\int }_{0}^{+\infty }{f}^{2}\left( x\right) \mathrm{d}x.
\]

4. 设 \( f \) 在 \( \lbrack 0, + \infty ) \) 上二阶可微, \( f \) 和 \( {f}^{\prime \prime } \) 在这个区间上均平方可积,证明: \( {f}^{\prime } \) 在这个区间上也平方可积.

5. 设 \( f \in  {C}^{1}\lbrack 0, + \infty ) \) ,且 \( {xf}\left( x\right) \) 和 \( {f}^{\prime }\left( x\right) \) 在这个区间上均平方可积,证明:

(1) \( f \) 也在这个区间上平方可积;

(2)成立不等式

\[
{\int }_{0}^{+\infty }{f}^{2}\left( x\right) \mathrm{d}x \leq  2{\left( {\int }_{0}^{+\infty }{x}^{2}{f}^{2}\left( x\right) \mathrm{d}x{\int }_{0}^{+\infty }{\left( {f}^{\prime }\left( x\right) \right) }^{2}\mathrm{\;d}x\right) }^{\frac{1}{2}};
\]

(3)在上述不等式中成立等号的充分必要条件是 \( f\left( x\right)  = a{\mathrm{e}}^{-b{x}^{2}} \) ,其中 \( b > 0 \) .

6. 问 \( a, b \) 是怎样的正实数时,广义积分

\[
{\int }_{0}^{+\infty }\left( {\sqrt{\sqrt{x + a} - \sqrt{x}} - \sqrt{\sqrt{x} - \sqrt{x - b}}}\right) \mathrm{d}x
\]

是收敛的?

7. 设有理函数 \( f\left( x\right)  = P\left( x\right) /Q\left( x\right) \) 在 \( \left( {-\infty , + \infty }\right) \) 上可积,证明:

\[
{\int }_{-\infty }^{+\infty }\frac{P\left( x\right) }{Q\left( x\right) }\mathrm{d}x = {2\pi }\mathrm{i}\mathop{\sum }\limits_{k}{A}_{k},
\]

其中 \( {A}_{k} \) 是有理函数 \( f \) 的部分分式分解中 \( 1/{x}_{k} \) 项的系数, \( {x}_{k} \) 是分母 \( Q\left( x\right) \) 的零点,和式只对虚部大于 0 的 \( {x}_{k} \) 求和. 当 \( {x}_{k} \) 为单根时,有简单公式 \( {A}_{k} = \; P\left( {x}_{k}\right) /{Q}^{\prime }\left( {x}_{k}\right) . \)

8. 应用上题的结果于下列各小题:

(1) 证明: 对 \( n \in  {\mathbf{N}}_{ + } \) 成立 \( {\int }_{-\infty }^{+\infty }\frac{1}{1 + {x}^{2n}}\mathrm{\;d}x = \frac{\pi }{n}\csc \frac{\pi }{2n} \) ;

(2)证明:若 \( n, m \in  {\mathbf{N}}_{ + } \) 满足条件 \( {2m} + 1 < {2n} \) ,则成立

\[
{\int }_{-\infty }^{+\infty }\frac{{x}^{2m}}{1 + {x}^{2n}}\mathrm{\;d}x = \frac{\pi }{n}\csc \frac{\left( {{2m} + 1}\right) \pi }{2n};
\]

(3) 计算积分: (a) \( {\int }_{0}^{+\infty }\frac{{x}^{50}}{{x}^{100} + 1}\mathrm{\;d}x,\left( \mathrm{b}\right) {\int }_{0}^{+\infty }\frac{{x}^{30} + 1}{{x}^{60} + 1}\mathrm{\;d}x \) .

9. 设 \( f \) 是 \( \left( {-\infty , + \infty }\right) \) 上的非负函数,且满足以下条件:

\[
{\int }_{-\infty }^{+\infty }f\left( x\right) \mathrm{d}x = 1,{\int }_{-\infty }^{+\infty }{xf}\left( x\right) \mathrm{d}x = 0,{\int }_{-\infty }^{+\infty }{x}^{2}f\left( x\right) \mathrm{d}x = 1,
\]

证明:

(1)在 \( x > 0 \) 时，成立 \( {\int }_{-\infty }^{x}f\left( t\right) \mathrm{d}t \geq  \frac{{x}^{2}}{1 + {x}^{2}} \) ;

(2)在 \( x < 0 \) 时，成立 \( {\int }_{-\infty }^{x}f\left( t\right) \mathrm{d}t \leq  \frac{1}{1 + {x}^{2}} \) .

(本题是概率论中的基本不等式, 且不能再改进 (见 [30]). 它表明期望与方差有限的连续随机变量的分布函数 (在标准化之后) 所必须满足的限制.)

10. 设 \( p > 0 \) ,定义

\[
g\left( x\right)  = \left\{  \begin{array}{ll} p\left\lbrack  \frac{x}{p}\right\rbrack   + \frac{p}{2}, & x \geq  0, \\   - g\left( {-x}\right) , & x < 0. \end{array}\right.
\]

证明: 对所有 \( x \) ,成立

\[
\frac{p}{2\pi }{\int }_{-\infty }^{+\infty }\mathop{\sum }\limits_{{n =  - \left\lbrack  {x/p}\right\rbrack  }}^{\left\lbrack  x/p\right\rbrack  }\frac{\sin \left( {n + \frac{1}{2}}\right) {pt}}{\sin \frac{1}{2}{pt}} \cdot  \frac{\sin {xt}}{t}\mathrm{\;d}t = \frac{1}{2}\left\lbrack  {g\left( {x}^{ + }\right)  + g\left( {x}^{ - }\right) }\right\rbrack  .
\]

## 参考题提示
