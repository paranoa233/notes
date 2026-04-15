## 第二组参考题

1. 证明: 处处满足平均值公式的连续函数一定是调和函数.

2. 设 \( {u}_{n}\left( {x, y}\right) \) 是定义在圆盘 \( {B}_{R} \) 上的调和函数序列,都在 \( {\bar{B}}_{R} \) 上连续,若 \( {u}_{n}\left( {x, y}\right) \) 在 \( {B}_{R} \) 的边界 \( \partial {B}_{R} \) 上一致收敛,则 \( {u}_{n}\left( {x, y}\right) \) 在 \( {B}_{R} \) 上也一致收敛,并且极限函数也是调和函数.

3. 设 \( u\left( {x, y, z}\right) \) 在区域 \( D \) 上二阶连续可微,证明: \( {\Delta u} \geq  0\left( {\forall \left( {x, y, z}\right)  \in  D}\right) \) 的充分必要条件是

\[
u\left( {\mathbf{M}}_{0}\right)  \leq  \frac{1}{{4\pi }{R}^{2}}{\oiint }_{\partial {B}_{R}\left( {\mathbf{M}}_{0}\right) }u\left( {x, y, z}\right) \mathrm{d}S,\;\forall {B}_{R}\left( {\mathbf{M}}_{0}\right)  \subset  D.
\]

4. 设 \( u\left( {x, y, z}\right) \) 是由光滑曲面 \( S \) 所包围的有界区域 \( \Omega \) 上的调和函数,则

\[
u\left( {x, y, z}\right)  = \frac{1}{4\pi }{\oiint }_{S}\left\lbrack  {u\left( {\xi ,\eta ,\zeta }\right) \frac{\cos \left( {\mathbf{r},\mathbf{n}}\right) }{{r}^{2}} + \frac{1}{r}\frac{\partial u\left( {\xi ,\eta ,\zeta }\right) }{\partial \mathbf{n}}}\right\rbrack  \mathrm{d}S,
\]

其中 \( \mathbf{r} = \left( {\xi  - x,\eta  - y,\zeta  - z}\right) , r = \left| \mathbf{r}\right| \) .

5. 利用 Poisson 积分公式证明不等式

\[
\frac{R - r}{R + r}u\left( {{x}_{0},{y}_{0}}\right)  \leq  u\left( {x, y}\right)  \leq  \frac{R + r}{R - r}u\left( {{x}_{0},{y}_{0}}\right) ,
\]

其中 \( u \) 是以 \( R \) 为半径, \( \left( {{x}_{0},{y}_{0}}\right) \) 为圆心的开圆盘上的非负调和函数, \( r < R \) 是 \( \left( {x, y}\right) \) 与 \( \left( {{x}_{0},{y}_{0}}\right) \) 的距离.

6. 证明: 全平面上有界的调和函数一定是常数.

## 参考题提示

第十三章 数项级数

## 第一组参考题 (36 页)

1. 将该分式记为 \( {u}_{n} \) ，一种方法是用裂项法证明级数 \( \sum {u}_{n} \) 收敛，另一种方法是利用 \( {u}_{n} \) 的分母单调增加,直接证明 \( {u}_{n} \rightarrow  0 \) .

2. 与上册例题 12.4.2 作类比, 参考其证明的基本思路.

3. 可利用题 2.

4. (1) 比较两个级数的部份和,并考虑题 2 的结论. (2) 试考虑当 \( n \) 为平方数时令 \( {a}_{n} = 1/n \) , 否则令 \( {a}_{n} = 0 \) .

5. 对级数用等价量判别法.

6. (1) 记括号内为 \( {d}_{n} \) ,证明 \( 0 \leq  {d}_{n} \leq  f\left( 1\right) \) ,且单调减少. (2) 是 (1) 的应用.

7. 对级数用等价量判别法即可.

8. 两者都是正项级数. (2) 可用题 6 , 也可从 (1) 推出.

9. 先证右边内层级数对每个 \( k \) 收敛.

10. 用积分方法估计 \( {s}_{m} \) ,证明 \( \mathop{\sum }\limits_{{m = 2}}^{\infty }{s}_{m} \) 收敛,然后利用题 9 .

11. 定义合适的二重数列 \( \left\{  {a}_{n, k}\right\} \) 后即可利用题 9. 另一种方法是对 \( n < m \) ,有 \( \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k} - }\right. \; \left. {a}_{m}\right)  \leq  \mathop{\sum }\limits_{{k = 1}}^{m}\left( {{a}_{k} - {a}_{m}}\right) \) ,利用右边有界去估计 \( \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k} \) .

12. 可利用 \( {a}_{n}^{2} = \mathop{\sum }\limits_{{k = n}}^{\infty }\left( {{a}_{k}^{2} - {a}_{k + 1}^{2}}\right)  \leq  \left( {{a}_{n} - {a}_{n + 1}}\right) \mathop{\sum }\limits_{{k = n}}^{\infty }\left( {{a}_{k} + {a}_{k + 1}}\right) \) .

13. 与题 2 类似, 又与上册 12.4.2 小节题 4 类似.

14. 若能证明 \( {a}_{n + 1}/{a}_{n} \) 大于 \( 3/2 \) 即可用 d’Alembert 判别法.

15. 从 \( {a}_{n + 1} = \left( {{a}_{n} - {a}_{n + 1}}\right) /{a}_{n}^{p} \) 出发用微分中值定理 (参考例题 13.2.1 之证 1 和例题 13.2.5).

16. 前半题用平均值不等式或 Cauchy 不等式均可.

17. 只要证明级数通项不趋于 0 即可. 对于 (1),若 \( \sin n \rightarrow  0 \) ,则 \( \sin \left( {n + 1}\right)  \rightarrow  0,{\cos }^{2}n \rightarrow  1 \) , 由此即可引出矛盾. (2) 与此类似.

18. (1) 收敛，(3) 发散，但对于 (2)，(4)，收敛和发散都是可能的，请举例.

19. (1) 为上册 57 页题 7 之特例, 用 Abel 变换即可. (2) 参考例题 13.2.7 中的证明.

20. 用反证法. 设有 \( M \) ,使得 \( \left| {n - f\left( n\right) }\right|  \leq  M \) 对一切 \( n \) 成立. 然后估计两个级数的部分和之差 \( \left| {{S}_{n} - {S}_{n}^{\prime }}\right| \) .

## 第二组参考题 (38 页)

1. 设 \( {A}_{n} = {a}_{1} + {a}_{2} + \cdots  + {a}_{n} \) ,将通项写为 \( \frac{{n}^{2}\left( {{A}_{n} - {A}_{n - 1}}\right) }{{A}_{n}^{2}} \leq  \frac{{n}^{2}\left( {{A}_{n} - {A}_{n - 1}}\right) }{{A}_{n}{A}_{n - 1}} \) 作估计, 然后利用例题 13.2.6 即可.

2. 记 \( {A}_{n} = {a}_{1} + {a}_{2} + \cdots  + {a}_{n} \) ,则级数通项为 \( \left( {{A}_{n} - {A}_{n - 1}}\right) /{A}_{n}^{3/2} \) . 以下可参考例题 13.2.5.

3. 对固定的 \( k \) ,考虑使 \( {a}_{k} \leq  M{a}_{n} \) 成立的所有可能 \( n \) ,然后将不等式相加,并用级数的 Cauchy 收敛准则.

4. 先取两个通项单调减少趋于 0 的正项级数 \( \sum {c}_{n} \) 和 \( \sum {d}_{n} \) ,使得前者收敛,后者发散. 又使 \( {d}_{n} > {c}_{n},\forall n \in  {\mathbf{N}}_{ + } \) 成立. 然后用它们的片段交替拼接成所求的两个级数. (见 [22] 之题 309.)

5. 取对数后分析.

6. 这时级数与 \( {\int }_{1}^{+\infty }f\left( x\right) \mathrm{d}x \) 同敛散. 可试取满足 \( {x}_{n} = {\mathrm{e}}^{{x}_{n - 1}} \) 的数列,用命题 13.1.2.

7. 利用 \( \left\{  {a}_{n}\right\} \) 单调减少趋于 0,可见 \( k > {b}_{n} \) 时 \( {a}_{k} < \frac{1}{{2}^{n}} \) ,而 \( k \leq  {b}_{n} \) 时 \( {a}_{k} \geq  \frac{1}{{2}^{n}} \) ,利用这些对两个级数部分和作估计.

8. (1) 猜测部分乘积并作归纳证明; (2) 归纳得到 \( 2\mathop{\prod }\limits_{{n = 1}}^{\infty }{\left\{  \frac{1}{2}{\left\lbrack  \frac{\left( {{2}^{n - 1} - 1}\right) !!\left( {2}^{n}\right) !!}{\left( {2}^{n - 1}\right) !!\left( {{2}^{n} - 1}\right) !!}\right\rbrack  }^{2}\right\}  }^{\frac{1}{{2}^{n}}} \; = 2\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left\{  {2}^{n{2}^{n} + 1}{\left\lbrack  \frac{\left( {2}^{n - 1}\right) !}{\left( {2}^{n}\right) !}\right\rbrack  }^{2}\right\}  }^{\frac{1}{{2}^{n}}} \) ,然后用 Stirling 公式即可.

9. 利用 \( \ln \left( {n + 1}\right)  - \ln \left( n\right)  \sim  \frac{1}{n} \) ,即相邻的 \( \ln n \) 值之间的距离趋于 0,因此使得级数通项的分子大于 \( 1/2 \) 的成片的正整数列的长度无上界. 利用级数的 Cauchy 收敛准则. (见 [22] 之题 255.)

10. (1) 将级数改写为 \( \mathop{\sum }\limits_{{n = k + 1}}^{\infty }\left( {n - k}\right) {a}_{n} = \mathop{\sum }\limits_{{n = k + 1}}^{\infty }n{a}_{n}\left( {1 - \frac{k}{n}}\right) \) ,然后用 Abel 判别法; (2) 可以用 Abel 变换估计 (例如用 (13.23)).

11. 反证法, 利用 Abel 定理 (即命题 13.2.5 (2)).

12. 利用上题的结果.

13. 正项级数和交错级数肯定都不行. 试用 \( {a}_{n} - \frac{1}{n}{a}_{n} - \cdots  - \frac{1}{n}{a}_{n} \) 作为接连的 \( n + 1 \) 项组成的级数.

14. 估计 \( \left| {{\int }_{k}^{k + 1}f\left( t\right) \mathrm{d}t - f\left( k\right) }\right| \) .

15. 利用 \( 1/{x}^{p} \) 为下凸函数,对 \( n = {4k} - 1,{4k},{4k} + 1 \) 三项作估计,证明 \( {S}_{{4n} + 1} > 1 - \frac{1}{{2}^{p}}{S}_{2n} \) , 然后取极限, 并对级数和作估计.

16. 与上册 57 页题 7 完全等价, 关键是用 Abel 变换.

17. 用上题即可.

18. 用 Cauchy 命题 (上册 31 页).

19. 用 \( {a}_{n} = {S}_{n} - {S}_{n - 1} \) 代入即可.

20. (2) 不满足题 19 的必要条件. 其他题的答案为: (1) \( 1/2 \) ; (3) \( 2/3 \) ; (4) \( \frac{1}{2}\tan \frac{x}{2} \) .

21. 观察 \( {S}_{n} - {\sigma }_{n} \) .

22. 必要性已见于第一组参考题 19 (1), 与可否 Cesàro 求和无关. 充分性只要将该表达式用 \( {S}_{n} \) 和 \( {\sigma }_{n} \) 表出即得.
