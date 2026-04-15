## 第七章 微分学的基本定理 参考题提示

## 第一组参考题 (221 页)

1. 仿例题 7.1.2.

2. 令方程左边为 \( f\left( x\right) \) ,分析 \( {f}^{\prime }\left( x\right) \) ,讨论 \( f \) 的单调性.

3. 与上题的方法类似.

4. 试作辅助函数 \( F\left( x\right)  = {\mathrm{e}}^{-{kx}}f\left( x\right) \) .

5. 试用数学归纳法.

6. (1) 试作辅助函数 \( F\left( x\right)  = {f}^{2}\left( x\right) f\left( {1 - x}\right) \) ; (2) 类似.

7. 先从几何意义搞清楚本题要证明什么?

8. 与上一题类似.

9. 这 4 小题都可用于复习在例题 7.1.3 中的方法.

10. 设法用 Cauchy 中值定理.

11. 实际上与题 9 类似.

12. 试用反证法.

13. 可用 Cauchy 中值定理和函数 \( \sqrt{x} \) 在 \( \lbrack 0, + \infty ) \) 上一致连续.

14. 可用第四章参考题 12. 本题是下一章的 L'Hospital 法则的特例.

15. 设法利用例题 7.1.5 的结论.

16. 设 \( 0 < x < 2 \) ,写出 \( f\left( 0\right) , f\left( 2\right) \) 在点 \( x \) 处的 Taylor 展开式.

17. 注意在例题 7.2.5 中只能用 \( t > 0 \) 作估计. (在 [59] 第一册 332 页对本题给出了一个有强烈几何直观意义的证明.)

18. 在 \( \left( {0, a}\right) \) 中的最大值点当然是极大值点,因此在该点的导数为 0 . 如何利用这个条件?

## 第二组参考题 (223 页)

1. 若 \( {f}^{\prime } \in  C\left\lbrack  {a, b}\right\rbrack \) ,则用 Lagrange 中值定理即可. 本题的意义在于对导函数来说,连续性的要求不是必要的.

2. 可研究辅助函数 \( g\left( x\right)  = f\left( x\right)  - \frac{1}{1 + {x}^{2}} \) .

3. 试用变换 \( y = \frac{1}{x} \) 后再作合适的辅助函数.

4. 用反证法. 若 \( {f}^{\prime \prime } \) 无零点,则保号. 然后用 Taylor 公式导出矛盾.

5. 考虑本题的几何意义. 可试用辅助函数

\[
F\left( x\right)  = \left\{  \begin{array}{ll} \frac{f\left( x\right)  - f\left( a\right) }{x - a}, & a < x \leq  b, \\  {f}^{\prime }\left( a\right) , & x = a. \end{array}\right.
\]

6. 试用辅助函数 \( F\left( x\right)  = \left\lbrack  {f\left( x\right)  - f\left( a\right) }\right\rbrack   \cdot  {\mathrm{e}}^{-\frac{x}{b - a}} \) .

7. 可以只考虑 \( \alpha  > 1 \) . 试用辅助函数 \( F\left( x\right)  = \ln f\left( x\right) , a < x < b \) .

8. 试用辅助函数 \( F\left( x\right)  = {f}^{2}\left( x\right)  + {\left\lbrack  {f}^{\prime }\left( x\right) \right\rbrack  }^{2} \) .

9. 本题给出了关于 \( x, h \) 的一个恒等式,条件很强. 试固定 \( x \) 后对 \( h \) 求导,先证明 \( {f}^{\prime } \) 为线性函数.

10. 对线性函数和二次函数, 广义二阶导数与普通的二阶导数是一样的. 试用辅助函数

\[
F\left( x\right)  =  \pm  \left\lbrack  {f\left( x\right)  - f\left( a\right)  - \frac{f\left( b\right)  - f\left( a\right) }{b - a}\left( {x - a}\right) }\right\rbrack   - \varepsilon \left( {x - a}\right) \left( {b - x}\right) \rbrack ,
\]

其中 \( \varepsilon  > 0 \) . 设法证明 \( F\left( x\right)  \leq  0 \) .

11. 可以先证明在区间 \( \left\lbrack  {0,\frac{1}{2c}}\right\rbrack \) 上 \( f\left( x\right)  \equiv  0 \) .

12. 注意在条件中蕴涵了 \( {f}^{\left( n\right) }\left( 0\right)  = 0,\forall n \geq  0 \) .

13. 上题的提示在这里也是对的.

14. 一阶导数是差商的极限. 本题是其推广. 试用带 Peano 余项的 Taylor 公式. 还可以利用第六章第二组参考题 8.

15. 利用例题 7.2.5 的方法, 写出带 Lagrange 余项的 Taylor 公式:

\[
f\left( {x + h}\right)  = f\left( x\right)  + {f}^{\prime }\left( x\right) h + \frac{{f}^{\prime \prime }\left( x\right) }{2!}{h}^{2} + \cdots  + \frac{{f}^{\left( n - 1\right) }\left( x\right) }{\left( {n - 1}\right) !}{h}^{n - 1} + \frac{{f}^{\left( n\right) }\left( {x + {\theta h}}\right) }{n!}{h}^{n}.
\]

取互异的 \( {h}_{1},\cdots ,{h}_{n - 1} \) 代替上面的 \( h \) ,然后从中解出 \( {f}^{\prime }\left( x\right) ,\cdots ,{f}^{\left( n - 1\right) }\left( x\right) \) .

16. 不妨设已有 \( f\left( {+\infty }\right)  = 0 \) . 设法证明 \( {f}^{\left( n\right) }\left( {+\infty }\right)  = 0 \) . 然后可以借用上题中的思路.

17. (1) 本题可以从例题 7.2.5 得到. 实际上 (1) 可从 (2)(ii) 推出.

(2) 从几何上不难考虑. 对 (ii) 试用反证法. 这里需要关于极限类型为 \( x \rightarrow   + \infty \) 的 Cauchy 收敛准则.

(在学了积分学后可以知道本题所讨论的问题等价于: 在区间 \( \lbrack a, + \infty ) \) 上广义可积的函数当 \( x \rightarrow   + \infty \) 时是否一定收敛于 0 .)

18. 写出 \( f\left( {x + r}\right) \) 在点 \( x \) 的带 Lagrange 余项的 Taylor 公式,利用单调性作估计.

19. 在上题的基础上已不难得到. (参见《美国数学月刊》(1983) 第 90 卷 130-131 页.)
