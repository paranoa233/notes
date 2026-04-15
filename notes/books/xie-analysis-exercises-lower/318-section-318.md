## 第十四章 函数项级数与幂级数 参考题提示

## 第一组参考题 (75 页)

1. 例如,设 \( D\left( x\right) \) 为 \( \left\lbrack  {0,1}\right\rbrack \) 上的 Dirichlet 函数 (见上册 103 页及索引),令 \( {S}_{n}\left( x\right)  = \frac{1}{n}D\left( x\right) \; \left( {n = 1,2,\cdots }\right) \) 即可.

2. 这里的要点是可微性为局部性质, 只要在所讨论的点的一个邻域上满足逐项可微定理的条件即可.

3. 这里需要 Dedekind 切割 (参见上册 96 页题 2).

4. 先求出极限函数,并利用 \( \left\{  {x}^{n}\right\} \) 于 \( \lbrack 0,1) \) 内闭一致收敛.

5. (2) 证明在无理点处可逐项求导, 而在每个有理点处除了一项之外也可逐项求导.

6. 按条件存在 \( {x}_{0} \in  \left( {0,1}\right) \) ,使得 \( f\left( {x}_{0}\right)  \neq  0 \) . 利用带 Lagrange 余项的 Taylor 公式,对每个 \( n \) 有 \( f\left( {x}_{0}\right)  = \frac{1}{n!}{f}^{\left( n\right) }\left( {\theta {x}_{0}}\right) {x}_{0}^{n},0 < \theta  < 1 \) .

7. 用 Abel 第二定理 (参见 59 页底注).

8. (1) 由于 \( \arcsin x \) 在 \( \left\lbrack  {-1,1}\right\rbrack \) 上可展开为 Maclaurin 级数,因此 \( {\left( \arcsin x\right) }^{2} \) 至少在 \( \left( {-1,1}\right) \) 上可以展开为 Maclaurin 级数,它可以从计算 \( {\left( \arcsin x\right) }^{2} \) 在 \( x = 0 \) 的所有高阶导数值 (见 6.2.4 小节题 3) 得到. 然后逐项求导.

9. 用 Abel 第二定理 (参见 59 页底注).

10. 利用在 \( \left( {-\infty , + \infty }\right) \) 上有界的多项式只能是 0 次多项式,即常数.

11. 可从常数项开始,证明 \( {P}_{n} \) 的同次幂项系数分别收敛.

12. 必要性部分用第 10 题.

13. 被积表达式是全微分.

14. 将通项分解为两个分式之差. 答案为 \( 9/{32} \) .

15. 将甲成功的事件分解为第一次成功, 第二次成功等等, 然后分别计算它们的概率并相加. 答案为 \( \frac{6}{11} \) .

16. 计算出第 \( n \) 年的 \( n \) 万元对应于一开始的钱是多少,然后相加. 答案为 \( {\left( {100} + a\right) }^{2}/{a}^{2} \) .

## 第二组参考题 (76 页)

1. 在 Arzelà 定理 (即命题 14.2.4) 的证明中将一开始定义的集合 \( {A}_{n} \) 改为

\[
{B}_{n} = \left\{  {x \in  \left\lbrack  {a, b}\right\rbrack  \mid \exists i, j \geq  n\text{ 使得 }\left| {{f}_{i}\left( x\right)  - {f}_{j}\left( x\right) }\right|  \geq  \varepsilon }\right\}  ,
\]

然后做下去.

2. 这里当然主要证明 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) . 除了用可积条件 (见上册 301 页) 的传统证法外,也可试用 Lebesgue 定理 (见上册 304 页).

3. 先证明极限函数单调. 然后将区间作分划来做.

4. 用反证法. 对后两个问题的答案均为否定, 不难构造反例.

5. 先证明有一个子函数列在一个点上收敛,这个点可取为 \( \left\{  {x}_{n}\right\} \) 的一个极限点.

6. 本题若用准一致收敛概念和 Arzelà-Borel 定理 (命题 14.2.3) 则非常方便.

7. 学习例题 14.1.8 的方法,可取 \( k = \left\lbrack  {\sqrt{\pi }/x}\right\rbrack \) . 若只要证明一致有界性,则还可以用 Dirichlet 积分的方法.

8. 展开后比较同次乘幂项的系数即可.

9. 其中需要在 \( 1 \leq  k \leq  n \) 时成立不等式 \( \left( {1 - \frac{1}{n}}\right) \left( {1 - \frac{2}{n}}\right) \cdots \left( {1 - \frac{k - 1}{n}}\right)  \geq  1 - \frac{k\left( {k - 1}\right) }{n} \) . 这是上册 1.3.2 小节题 \( 1\left( 3\right) \) 之特例.

10. (1) 利用第十三章第二组参考题 19 知 \( {a}_{n} = o\left( n\right) \) ，从而知收敛半径不小于 1. (2) 然后用级数乘积. (3) 令 \( {a}_{0} = 1,{a}_{n} = 0\left( {n = 1,2,\cdots }\right) \) ,就从 (1) 得到在 \( \left( {-1,1}\right) \) 上的恒等式 \( 1 = {\left( 1 - x\right) }^{2}\mathop{\sum }\limits_{{n = 0}}^{\infty }\left( {n + 1}\right) {x}^{n} \) ,然后乘以 \( S \) ,用拟合法估计 \( \left| {S\left( x\right)  - S}\right| \) .

11. 利用 Cauchy 命题的证明方法 (见上册 31 页).

12. 这是 \( {c}_{n} \geq  0 \) 条件下的 Abel 第二定理. 最简单的方法是用 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{c}_{n} \) 为优级数.

13. 本题为 Bernstein 定理, 但这里的结果比上册 225 页题 19 更好一些, 见《美国数学月刊》(1983) 第 90 卷 130-131 页. 用 Taylor 公式的积分型余项 (见 11.4.3 小节) 证明在 \( x \in  \left\lbrack  {0, r}\right\rbrack \) 时 \( \frac{{R}_{n}\left( x\right) }{{x}^{n + 1}} \leq  \frac{{R}_{n}\left( r\right) }{{r}^{n + 1}} \) ,又有 \( {R}_{n}\left( r\right)  \leq  f\left( r\right) \) . 于是得到 \( {R}_{n}\left( x\right)  \leq  {\left( \frac{x}{r}\right) }^{n + 1}f\left( r\right) \) , 因此在 \( 0 \leq  x < r \) 时 \( {R}_{n}\left( x\right)  \rightarrow  0 \) .

14. 先从 \( \left\{  {a}_{n}\right\} \) 的递推公式导出 \( f\left( x\right)  = 1/\left( {1 - x - {x}^{2}}\right) \) ,将它作部分分式分解后再展开,就得到 Fibonacci 数列的 Binet (比内)-Lucas (卢卡斯) 公式:

\[
{a}_{n} = \frac{1}{\sqrt{5}}\left\lbrack  {{\left( \frac{1 + \sqrt{5}}{2}\right) }^{n + 1} - {\left( \frac{1 - \sqrt{5}}{2}\right) }^{n + 1}}\right\rbrack  , n = 0,1,\cdots ,
\]

由此可见 (或利用 \( f \) 的幂级数展开式的收敛半径), \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n + 1}}{{a}_{n}} = \frac{1 + \sqrt{5}}{2} \approx  {1.618} \) .

15. 本题的三个数列的生成函数为 \( {\left( 1 + x\right) }^{\alpha },{\left( 1 + x\right) }^{\beta } \) 和 \( {\left( 1 + x\right) }^{\alpha  + \beta } \) .
