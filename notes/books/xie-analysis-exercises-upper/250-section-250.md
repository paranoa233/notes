## 第一组参考题

1. 设 \( m \) 为正整数, \( 0 < a < b \) ,试从定积分的定义出发计算 \( {\int }_{a}^{b}{x}^{m}\mathrm{\;d}x \) .

2. (1) 举例: 从 \( \left| f\right|  \in  R\left\lbrack  {a, b}\right\rbrack \) 未必能推出 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) ;

(2) 证明: 若 \( f \) 是导函数,则当 \( \left| f\right|  \in  R\left\lbrack  {a, b}\right\rbrack \) 时,就一定有 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) .

3. 设 \( f, g \in  R\left\lbrack  {a, b}\right\rbrack  ,\xi \) 和 \( {\xi }^{\prime } \) 是从属于分划 \( P \) 的两个不同介点集,证明:

\[
\mathop{\lim }\limits_{{\parallel P\parallel  \rightarrow  0}}\mathop{\sum }\limits_{{k = 1}}^{n}f\left( {\xi }_{k}\right) g\left( {\xi }_{k}^{\prime }\right) \Delta {x}_{k} = {\int }_{a}^{b}f\left( x\right) g\left( x\right) \mathrm{d}x.
\]

4. 设 \( f \) 在区间 \( I = \left( {a, b}\right) \) 上为下凸函数,证明: \( f \) 的两个单侧导函数 \( {f}_{ - }^{\prime }\left( x\right) \) 和 \( {f}_{ + }^{\prime }\left( x\right) \) 在 \( I \) 中的任意有界闭区间 \( \left\lbrack  {c, d}\right\rbrack \) 上可积,且成立 Newton-Leibniz 公式:

\[
f\left( d\right)  - f\left( c\right)  = {\int }_{c}^{d}{f}_{ - }^{\prime }\left( x\right) \mathrm{d}x = {\int }_{c}^{d}{f}_{ + }^{\prime }\left( x\right) \mathrm{d}x.
\]

5. 设 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) ,证明: 对于每一个给定的 \( \varepsilon  > 0 \) ,存在函数 \( g \) ,使得

\[
{\int }_{a}^{b}\left| {f\left( x\right)  - g\left( x\right) }\right| \mathrm{d}x < \varepsilon ,
\]

其中的 \( g \) 是:(1) 阶梯函数; (2) 折线函数; (3) 连续函数; (4) 连续可微函数.

6. 证明积分的连续性命题: 设 \( f \in  R\left\lbrack  {a - \delta , b + \delta }\right\rbrack \) ,其中 \( \delta  > 0 \) ,则有

\[
\mathop{\lim }\limits_{{h \rightarrow  0}}{\int }_{a}^{b}\left| {f\left( {x + h}\right)  - f\left( x\right) }\right| \mathrm{d}x = 0.
\]

7. 设 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) ,证明: \( \forall \varepsilon  > 0,\exists \left\lbrack  {c, d}\right\rbrack   \subseteq  \left\lbrack  {a, b}\right\rbrack \) ,使 \( f \) 在子区间 \( \left\lbrack  {c, d}\right\rbrack \) 上的振幅 \( {\omega }_{f\left\lbrack  {c, d}\right\rbrack  } < \varepsilon \)

8. 设 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) ,证明: \( f \) 的连续点在 \( \left\lbrack  {a, b}\right\rbrack \) 中稠密 (即 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 的每个子区间 \( \left( {c, d}\right) \) 中有连续点).

9. 设非负函数 \( f \in  R\left\lbrack  {a, b}\right\rbrack \) ,求证: 积分 \( {\int }_{a}^{b}f\left( x\right) \mathrm{d}x = 0 \) 的充分必要条件是 \( f \) 在所有连续点处的值都等于 0 .

10. 设 \( f, g \in  R\left\lbrack  {a, b}\right\rbrack \) ,且在 \( \left\lbrack  {a, b}\right\rbrack \) 的每个子区间中有 \( x \) 使 \( f\left( x\right)  = g\left( x\right) \) ,证明:

\[
{\int }_{a}^{b}f\left( x\right) \mathrm{d}x = {\int }_{a}^{b}g\left( x\right) \mathrm{d}x.
\]

11. (积分第一中值定理的一种推广) 证明: 设 \( f, g \in  R\left\lbrack  {a, b}\right\rbrack \) ,其中 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上有原函数, \( g \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上不变号,则存在 \( \xi  \in  \left( {a, b}\right) \) ,使

\[
{\int }_{a}^{b}f\left( x\right) g\left( x\right) \mathrm{d}x = f\left( \xi \right) {\int }_{a}^{b}g\left( x\right) \mathrm{d}x.
\]

12. 计算以下渐近等式

\[
{\int }_{0}^{1}\frac{{x}^{n - 1}}{1 + x}\mathrm{\;d}x = \frac{a}{n} + \frac{b}{{n}^{2}} + o\left( \frac{1}{{n}^{2}}\right) \left( {n \rightarrow  \infty }\right)
\]

中的待定常数 \( a, b \) .

13. 设非负严格单调增加函数 \( f \) 在区间 \( \left\lbrack  {a, b}\right\rbrack \) 上连续. 由积分中值定理,对于每个 \( p > 0 \) ,存在唯一的 \( {x}_{p} \in  \left( {a, b}\right) \) ,使

\[
{f}^{p}\left( {x}_{p}\right)  = \frac{1}{b - a}{\int }_{a}^{b}{f}^{p}\left( t\right) \mathrm{d}t.
\]

试求 \( \mathop{\lim }\limits_{{p \rightarrow   + \infty }}{x}_{p} \) .

14. 设 \( f \in  C\lbrack 0, + \infty ), a > 0 \) ,且存在有限极限 \( \mathop{\lim }\limits_{{x \rightarrow   + \infty }}\left( {f\left( x\right)  + a{\int }_{0}^{x}f\left( t\right) \mathrm{d}t}\right) \) ,证明: \( f\left( {+\infty }\right)  = 0. \)

15. 设 \( f \in  C\left( {-\infty , + \infty }\right) \) ,定义 \( F\left( x\right)  = {\int }_{a}^{b}f\left( {x + t}\right) \cos t\mathrm{\;d}t, a \leq  x \leq  b \) .

(1) 证明 \( F \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上可导; (2) 计算 \( {F}^{\prime }\left( x\right) \) .

16. 设 \( n \in  {\mathbf{N}}_{ + } \) ,计算积分 \( {\int }_{0}^{\pi /2}\frac{\sin {nx}}{\sin x}\mathrm{\;d}x \) .

17. 令 \( B\left( {m, n}\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{\mathrm{C}}_{n}^{k}\frac{{\left( -1\right) }^{k}}{m + k + 1}, m, n \in  {\mathbf{N}}_{ + } \) .

(1) 证明 \( B\left( {m, n}\right)  = B\left( {n, m}\right) \) ; (2) 计算 \( B\left( {m, n}\right) \) .

18. 证明: 当 \( m < 2 \) 时, \( \mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{1}{{x}^{m}}{\int }_{0}^{x}\sin \frac{1}{t}\mathrm{\;d}t = 0 \) .

19. 证明: 当 \( \lambda  < 1 \) 时, \( \mathop{\lim }\limits_{{R \rightarrow   + \infty }}{R}^{\lambda }{\int }_{0}^{\pi /2}{\mathrm{e}}^{-R\sin \theta }\mathrm{d}\theta  = 0 \) .

20. 设 \( f \in  {C}^{2}\left\lbrack  {0,\pi }\right\rbrack \) ,且 \( f\left( \pi \right)  = 2,{\int }_{0}^{\pi }\left( {f\left( x\right)  + {f}^{\prime \prime }\left( x\right) }\right) \sin x\mathrm{\;d}x = 5 \) ,求 \( f\left( 0\right) \) .

21. 寻找同时满足以下三个条件:

\[
{\int }_{0}^{1}f\left( x\right) \mathrm{d}x = 1,{\int }_{0}^{1}{xf}\left( x\right) \mathrm{d}x = a,{\int }_{0}^{1}{x}^{2}f\left( x\right) \mathrm{d}x = {a}^{2}
\]

的非负连续函数 \( f \) ,其中 \( a \) 为给定实数.

22. 设 \( f \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上可微,且满足条件 \( f\left( 1\right)  = 3{\int }_{0}^{1/3}{\mathrm{e}}^{x - 1}f\left( x\right) \mathrm{d}x \) ,证明: 存在 \( \xi  \in  \left( {0,1}\right) \) ,使得 \( f\left( \xi \right)  + {f}^{\prime }\left( \xi \right)  = 0 \) .

23. 设 \( f \) 于 \( \left\lbrack  {0,1}\right\rbrack \) 上非负连续,且 \( {f}^{2}\left( t\right)  \leq  1 + 2{\int }_{0}^{t}f\left( s\right) \mathrm{d}s \) ,证明: \( f\left( t\right)  \leq  1 + t \) .

24. 设 \( f \in  {C}^{1}\lbrack 1, + \infty ), f\left( 1\right)  = 1 \) ,且当 \( x \geq  1 \) 时有 \( {f}^{\prime }\left( x\right)  = \frac{1}{{x}^{2} + {f}^{2}\left( x\right) } \) ,证明: 存在有限极限 \( f\left( {+\infty }\right) \) ,且 \( f\left( {+\infty }\right)  < 1 + \frac{1}{4}\pi \) .

(本题与 8.5.3 小节题 13 相同, 当然这里可以用积分方法做.)

25. 证明: \( {\int }_{0}^{2\pi }\left( {{\int }_{x}^{2\pi }\frac{\sin t}{t}\mathrm{\;d}t}\right) \mathrm{d}x = 0 \) .
