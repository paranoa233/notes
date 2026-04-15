## 第二十二章 重积分 参考题提示

## 第一组参考题 (275 页)

1. \( f \) 是二元 Riemann 函数,可积的证明仿照一元 Riemann 函数的讨论.

2. 根据可积定义讨论.

3. (1) \( A = \frac{3}{32} + \frac{\ln 2}{8} \) ; (2) 用反证法,利用 (1).

4. 利用不等式 \( {100} + {\cos }^{2}x + {\cos }^{2}y \leq  \left( {{10} + \frac{{\cos }^{2}x}{10}}\right) \left( {{10} + \frac{{\cos }^{2}y}{10}}\right) \) .

5. 用正交变换.

6. 利用 \( f\left( {x, y}\right)  = {\int }_{\varphi \left( x\right) }^{y}\frac{\partial f\left( {x, t}\right) }{\partial t}\mathrm{\;d}t \) 及 Schwarz 不等式.

7. 利用 Hölder 不等式.

8. 取辅助函数 \( g\left( {x, y}\right)  = x\left( {1 - x}\right) y\left( {1 - y}\right) \) ,注意到

\[
{\iint }_{D}f\left( {x, y}\right) \mathrm{d}x\mathrm{\;d}y = \frac{1}{4}{\iint }_{D}\frac{{\partial }^{4}g}{\partial {x}^{2}\partial {y}^{2}}\left( {x, y}\right) f\left( {x, y}\right) \mathrm{d}x\mathrm{\;d}y.
\]

按不同的次序计算累次积分, 并用分部积分.

9. 证明存在 \( f\left( {x, y}\right) \) 的连续点 \( \left( {{x}_{0},{y}_{0}}\right) \) ,使 \( f\left( {{x}_{0},{y}_{0}}\right)  > 0 \) .

10. 设左端积分为 \( I.M, m \) 分别为 \( f \) 在 \( \Omega \) 上的最大最小值,则 \( m \leq  I/\Omega  \leq  M \) . 再应用多元函数介值定理 (命题 18.2.4).

11. 考虑差

\[
\Delta  = {\int }_{a}^{b}p\left( x\right) \mathrm{d}x{\int }_{a}^{b}p\left( x\right) f\left( x\right) g\left( x\right) \mathrm{d}x - {\int }_{a}^{b}p\left( x\right) f\left( x\right) \mathrm{d}x{\int }_{a}^{b}p\left( x\right) g\left( x\right) \mathrm{d}x.
\]

不同组合进行累次积分,得到 \( \Delta  \geq  0 \) .

12. 仿上题证明方法.

13. 利用第 10 题.

14. 作变量代换 \( x = x, u = {xyt}, s = {xyz} \) ,并计算累次积分对 \( t \) 的导数.

15. (1) \( x = f\left( s\right)  + t\sin \theta \left( s\right) , y = \varphi \left( s\right)  - t\cos \theta \left( s\right) ,0 \leq  s \leq  {2\pi l},0 < t < l \) ;

(2) 作变换 \( \left( {x, y}\right)  \mapsto  \left( {s, t}\right) \) ,再计算积分.

## 第二组参考题 (277 页)

1. 利用上册 259 页练习题 10.

2. 利用上题与例题 22.5.9.

3. (1) 证明 \( \forall \varepsilon  > 0, p \rightarrow   + \infty \) 时, \( {\Phi }_{p}\left( u\right) \) 的下极限 \( \geq  \mathop{\max }\limits_{{\left( {x, y}\right)  \in  \Omega }}\{ u\left( {x, y}\right) \}  - \varepsilon \) . (2) 利用 (1) 的结果. (3) 利用 \( \mathop{\lim }\limits_{{p \rightarrow  0}}\frac{{\iint }_{\Omega }{u}^{p}\mathrm{\;d}x\mathrm{\;d}y - \left| \Omega \right| }{p\left| \Omega \right| } = \frac{1}{\left| \Omega \right| }{\iint }_{\Omega }\ln u\mathrm{\;d}x\mathrm{\;d}y \) .

4. (1) 设球心是坐标原点, \( {P}_{0} = \left( {0,0, a}\right) , P \) 点的轨迹形成的封闭曲面的方程为 \( \left( {{x}^{2} + {y}^{2} + }\right. \; {\left. {z}^{2} - az\right) }^{2} = {R}^{2}\left\lbrack  {{x}^{2} + {y}^{2} + {\left( z - a\right) }^{2}}\right\rbrack \) ,所求体积 \( V = \frac{4\pi }{3}R\left( {{R}^{2} + {a}^{2}}\right) \) ,(2) 如果 \( {P}_{0} = \left( {x, y, z}\right) \) , 则 \( V = \frac{4\pi }{3}R\left( {{R}^{2} + {x}^{2} + {y}^{2} + {z}^{2}}\right) \) .

5. 利用 \( {\int }_{0}^{a}{\mathrm{e}}^{-{x}^{2}}\mathrm{\;d}x = {\left( {\iint }_{{Q}_{a}}{\mathrm{e}}^{-\left( {{x}^{2} + {y}^{2}}\right) }\mathrm{d}x\mathrm{\;d}y\right) }^{1/2} \) ,其中 \( {Q}_{a} = \{ 0 < x < a,0 < y < a\}  \supset \; {D}_{a} = \left\{  {{x}^{2} + {y}^{2} < {a}^{2}, x > 0, y > 0}\right\} \) . 证明右端不等式时与 \( {D}_{{2a}/\sqrt{\pi }} \) 上的二重积分比较,此时被积函数 \( {\mathrm{e}}^{-\left( {{x}^{2} + {y}^{2}}\right) } \) 是原点到 \( \left( {x, y}\right) \) 的距离的严格减少函数.

6. 用函数 \( f\left( {x, y}\right) \) 的无限接近的等位线把积分区域分为许多部分.
