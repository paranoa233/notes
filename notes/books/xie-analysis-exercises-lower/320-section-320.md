## 第十六章 无穷级数的应用 参考题提示

## 参考题 (134 页)

1. 参考例题 16.2.1 中的方法.

2. 参考上册 55 页 Catalan 恒等式中的技巧. 答案为 \( - \gamma \ln 2 + \frac{1}{2}{\ln }^{2}2 \approx   - {0.159869} \) .

3. 将通项分解为 \( \frac{1}{2m}\left( {\frac{1}{m + n} - \frac{1}{m - n}}\right) \) ,然后通过计算内层级数的部分和求出内层的级数和.

4. 开始有 \( \mathop{\sum }\limits_{q}\frac{1}{q - 1} = \mathop{\sum }\limits_{{n \geq  2}}\frac{1}{{n}^{2} - 1} + \mathop{\sum }\limits_{{n \geq  2}}\frac{1}{{n}^{3} - 1} + \cdots \) ,其中 \( n \) 取不是乘幂的所有大于 2 的正整数. 将此写成二重求和, 并将其内层再写成二重求和并交换顺序.

5. 证明 \( {a}_{n}^{2} - {a}_{n + 1}{a}_{n - 1} = 4,\forall n \geq  2 \) ,然后用裂项相消法 (见 [22] 之题 26).

6. 通项可写成 \( \frac{1}{{2}^{n - 1}}{\int }_{0}^{\pi /2}{\cos }^{{2n} + 1}x\mathrm{\;d}x \) ,也可写成 \( {2}^{n + 1}{\int }_{0}^{1}{x}^{n}{\left( 1 - x\right) }^{n}\mathrm{\;d}x \) .

7. 试用多项式序列一致逼近 \( f \) ,并用数列的 Cauchy 收敛准则.

8. 先证明结论对 \( g \) 为多项式时成立,然后用逼近定理.

9. 先证明 \( \left( {f \circ  g}\right) {g}^{\prime } \) 有原函数,然后用上题即可.

10. 参考上册 323 页例题 10.4.4.

11. 参考上册 140 页例题 5.4.5 和例题 14.1.3.

12. 作变量代换 \( y = 1/x \) .

13. 作变量代换 \( y = {\mathrm{e}}^{-x} \) .

14. 连续性的证明不难,这里只对于可微性作简述. 对 \( x \in  \left( {0,1}\right) \) ,构造点列 \( \left\{  {x}^{\left( n\right) }\right\} \) ,记 \( f\left( {x}^{\left( n\right) }\right)  = \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{u}_{k}^{\prime }}{{2}^{k}} \) ,使得 \( f\left( x\right) \) 和 \( f\left( {x}^{\left( n\right) }\right) \) 满足条件:

\[
{u}_{k}^{\prime } = {u}_{k},\forall 1 \leq  k \leq  n,{u}_{n + 1}^{\prime } = 1 - {u}_{n + 1},{u}_{n + 2}^{\prime } = {u}_{n + 2},
\]

然后估计差商 \( \frac{f\left( {x}^{\left( n\right) }\right)  - f\left( x\right) }{{x}^{\left( n\right) } - x} \) . 实现上述条件的方法是: 在 \( {x}^{\left( n\right) } = \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{x}_{k}^{\prime }}{{10}^{k}} \) 中,对于 \( k = n + 1, n + 2 \) 采用以下规定:

\[
{x}_{n + 1}^{\prime }\left\{  {\begin{array}{l}  \neq  {x}_{n},\;{u}_{n + 1} = {u}_{n}, \\   = {x}_{n},\;{u}_{n + 1} \neq  {u}_{n}, \end{array}\;{x}_{n + 2}^{\prime }\left\{  \begin{array}{l}  \neq  {x}_{n + 1}^{\prime },\;{u}_{n + 2} = {u}_{n + 1}, \\   = {x}_{n + 1}^{\prime },\;{u}_{n + 2} \neq  {u}_{n + 1}. \end{array}\right. }\right.
\]

15. 利用 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{u}_{n}\left( x\right) \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上一致收敛.

16. 用上题即可.

17. 验证条件逐项求导.
