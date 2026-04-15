## 第二章 数列极限 参考题提示

## 第一组参考题 (55 页)

1. 设前两个子列收敛于 \( \alpha \) 和 \( \beta \) ,利用第三个条件取适当的子列证明 \( \alpha  = \beta \) .

2. 利用单调有界数列收敛定理和上一题的结论.

3. 用极限的和差运算法则即可.

4. 试用反证法.

5. 试用夹逼定理.

6. 将 \( n \) 写成素数因子的乘积,由此对 \( p\left( n\right) \) 作出估计.

7. 用拟合法 (参考例题 2.4.3 及其注 1). 答案为 0 .

8. 利用 \( 0 < k < 1 \) 和 \( x > 0 \) 时成立的不等式 \( {\left( 1 + x\right) }^{k} < 1 + x \) .

9. (1) 答案是不一定收敛, 甚至可以是无穷大量; (2) 用反证法, 并利用例题 2.2.6.

10. (1) 用反证法,注意至少从某项开始, \( \left\{  {a}_{n}\right\} \) 是递增的; (2) 用反证法,对 \( {a}_{n} \) 作出估计.

11. 可用数学归纳法.

12. 可用数学归纳法.

13. (1) 可用数学归纳法; 由 (1) 即可得 (2); 对于 (3), 可模仿命题 2.5.4 对误差作出估计.

14. 证明数列递减且有下界. 此题今后还可用积分法做 (见第十一章第一组参考题 10).

15. 将 \( \frac{{a}_{n}}{n} \) 用算术平均值表示出来.

16. 可用夹逼定理,也可取对数后用 Stolz 定理. (此题还可以推广: 设 \( {a}_{n} > 0,{a}_{n + 1}/{a}_{n} \rightarrow \; a \) ,则有 \( {\left( {a}_{1}{a}_{2}\cdots {a}_{n}\right) }^{1/{n}^{2}} \rightarrow  \sqrt{a} \) . 用两次 Stolz 定理即可.)

17. 注意 \( \left\{  {x}_{n}\right\} \) 至少从第二项起大于 0 . 证明 \( \left\{  {x}_{n}\right\} \) 单调增加有上界. 极限为 \( 1/2 \) .

18. 此题解法非常多. 一种方法是归纳地证明 \( {a}_{2k} \searrow  ,{a}_{{2k} - 1} \nearrow \) ,且有相同极限. 答案为 \( \left( {b + {2c}}\right) /3 \) .

19. 注意对每个 \( n \) 成立 \( {a}_{n} + {b}_{n} + {c}_{n} = a + b + c = A \) . 答案为 \( A/3 \) .

20. (1) 证明 \( {b}_{n} \nearrow  ,{a}_{n} \searrow \) ,且有相同极限; (2) 在题中已有提示. 极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n\sin \frac{\pi }{n} = \pi \) 可从命题 1.3.6 的不等式得到.

## 第二组参考题 (57 页)

1. 有很多方法可以证明 \( \left\{  {a}_{n}\right\} \) 有界,其中较有推广价值的一种方法是先利用

\[
\sqrt{n - 1 + \sqrt{n}} \leq  \sqrt{n - 1 + 2\sqrt{n - 1} + 1} = \sqrt{n - 1} + 1,
\]

然后用 \( \sqrt{n - 1} < 2\sqrt{n - 2}\left( {n \geq  3}\right) \) 从里向外将根号逐个脱去.

2. 将左边展开,并利用一个辅助不等式 (见 1.3.2 小节的练习题 \( 1\left( 3\right) \) ):

\[
\left( {1 - \frac{1}{2}}\right) \left( {1 - \frac{1}{3}}\right) \cdots \left( {1 - \frac{1}{k}}\right)  \geq  1 - \frac{1}{2} - \frac{1}{3} - \cdots  - \frac{1}{k}.
\]

3. 利用命题 2.5.4 和夹逼定理. 答案为 \( {2\pi } \) .

4. 利用命题 2.5.6. 答案为 e.

5. 用两次 Stolz 定理. 答案为 \( 1/2 \) .

6. (1) 用二项式定理; (2) 取对数后用两次 Stolz 定理.

7. 作 Abel 变换 (见下册 (13.21)): 用 \( {a}_{1} = {A}_{1},{a}_{k} = {A}_{k} - {A}_{k - 1}, k = 2,\cdots , n \) 整理得到

\[
\frac{{p}_{1}{a}_{1} + {p}_{2}{a}_{2} + \cdots  + {p}_{n}{a}_{n}}{{p}_{n}} = \frac{\left( {{p}_{1} - {p}_{2}}\right) {A}_{1} + \cdots  + \left( {{p}_{n - 1} - {p}_{n}}\right) {A}_{n - 1}}{{p}_{n}} + {A}_{n}.
\]

若 \( \left\{  {p}_{n}\right\} \) 严格单调增加,对右边第一项用 Stolz 定理即可; 否则用 Cauchy 命题的证明方法, 或用下面题 10 提供的 Toeplitz 定理.

8. 先证明 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}^{2} =  + \infty \) ,然后再用 Stolz 定理计算 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n{a}_{n}^{3} \) .

9. 先找出 \( {u}_{n} \) 与 \( {u}_{n + 1} \) 的关系. 由此可知,若 \( {u}_{0} > 0 \) ,则每个 \( {u}_{n} > 0 \) ,数列 \( \left\{  {u}_{n}\right\} \) 严格单调减少趋于 0 . 用 Stolz 定理证明 \( {u}_{n} \sim  \frac{1}{n} \) ,引出矛盾.

10. 用 Cauchy 命题的证明方法即可.

11. 将 \( \frac{{a}_{n}}{{b}_{n}} \) 用 \( \frac{{a}_{i} - {a}_{i - 1}}{{b}_{i} - {b}_{i - 1}}\left( {i = 2,\cdots , n}\right) \) 的线性组合表示出来.

12. 试用拟合法 (参考例题 2.4.3).

13. 先推出 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{y}_{n} = 0 \) (参见例题 2.2.9),然后用 Cauchy 命题的证明方法. 反例可考虑 \( {x}_{n} = {y}_{n} = 1/\sqrt{n}, n \in  {\mathbf{N}}_{ + }. \)

14. 可以直接写出 \( \left\{  {x}_{n}\right\} \) 的表达式,然后用上一题的结论. 本题的其他解法见例题 3.6.3.

15. 可求出通项 \( {a}_{n} \) 的表达式. 答案是 \( {a}_{0} = 1/5 \) .

16. 分别考虑奇数项子列和偶数项子列, 证明它们均收敛于 2 .

17. 试作变量代换 \( {y}_{0} = x + {x}^{-1} \) ,然后用 \( x \) 将 \( {y}_{n} \) 和 \( {S}_{n} \) 表示出来.

18. 用迭代生成数列一节的结论即可. (关于函数性质的讨论可以在学了微分学后再做.)

19. 注意 \( b = 1 + \sqrt{5} \) 时 \( \left\{  {x}_{n}\right\} \) 本身恰为一个周期 2 轨.

20. 本题有多种证法, 这里提示两种.

(1)记 \( n \) 维空间 \( {\mathbf{R}}^{n} \) 中的点 \( \mathbf{x} = \left( {{x}_{1},\cdots ,{x}_{n}}\right) \) ，证明对点 \( \mathbf{x} \) 反复作题示的线性变换的极限是每个分量等于 \( {x}_{1},\cdots ,{x}_{n} \) 的平均值 \( \overline{\mathbf{x}} \) 的点. 写出线性变换的矩阵 \( \mathbf{A} \) ,计算出其特征方程,即可发现所有特征值均匀分布在复平面上以点 \( \left( {1/2,0}\right) \) 为圆心,半径为 \( 1/2 \) 的圆周上,其中有一个单重特征值 1,其余特征值的模均小于 1,由此可以计算得到 \( \mathop{\lim }\limits_{{k \rightarrow  \infty }}{\mathbf{A}}^{k}\mathbf{x} = \overline{\mathbf{x}}\mathbf{e} \) ,其中 \( \mathbf{e} = \left( {1,\cdots ,1}\right) . \)

(2) 令 \( f\left( \varepsilon \right)  = {x}_{1} + {x}_{2}\varepsilon  + \cdots  + {x}_{n}{\varepsilon }^{n - 1},{f}^{\left( k\right) }\left( \varepsilon \right)  = {x}_{1}^{\left( k\right) } + {x}_{2}^{\left( k\right) }\varepsilon  + \cdots  + {x}_{n}^{\left( k\right) }{\varepsilon }^{n - 1}, k \in  {\mathbf{N}}_{ + } \) , 其中 \( \varepsilon \) 是 1 的 \( n \) 次原根 (即 \( {\varepsilon }^{i}, i = 0,1,\cdots , n - 1 \) ,给出了方程 \( {x}^{n} = 1 \) 的所有 \( n \) 个根). 这样就可以得到 \( {f}^{\left( k\right) }\left( \varepsilon \right)  = f\left( \varepsilon \right) {\left( 1 + \varepsilon \right) }^{k}/{2}^{k} \) . 由此将 \( {x}_{i}^{\left( k\right) }\left( {i = 1,\cdots , n}\right) \) 写为 \( {x}_{1},\cdots ,{x}_{n} \) 的线性组合,可以发现问题归结为证明在二项式系数 \( 1,{\mathrm{C}}_{k}^{1},\cdots ,{\mathrm{C}}_{k}^{k} \) 中将相隔 \( n \) 项的各项取和后除以 \( {2}^{k} \) ,当 \( k \rightarrow  \infty \) 时极限均为 \( \frac{1}{n} \) . (参见 [19] 之题 77.)
