## 第二组参考题

1. 曲线 \( K \) 的极坐标方程为 \( \rho  = \rho \left( \theta \right) ,0 \leq  \theta  \leq  \pi ,\rho  \in  C\left\lbrack  {0,\pi }\right\rbrack \) ,且已知 \( K \) 上任何两点之间的距离不超过 1,证明: 由曲线 \( K \) 与射线 \( \theta  = 0,\theta  = \pi \) 围成的扇形面积

\[
S = \frac{1}{2}{\int }_{0}^{\pi }{\rho }^{2}\left( \theta \right) \mathrm{d}\theta  \leq  \frac{\pi }{4}.
\]

(由此可见,直径不超过 1 的图形面积最多为 \( \pi /4 \) .)

2. 设 \( f \in  C\left\lbrack  {a, b}\right\rbrack \) ,且处处大于 0 . 记 \( {f}_{kn} = f\left( {a + k{h}_{n}}\right) ,{h}_{n} = \left( {b - a}\right) /n, k = \; 1,2,\cdots , n \) . 证明:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{{f}_{1n}{f}_{2n}\cdots {f}_{nn}} = \exp \left\lbrack  {\frac{1}{b - a}{\int }_{a}^{b}\ln f\left( x\right) \mathrm{d}x}\right\rbrack  ,
\]

并用于证明 (Poisson 积分):

\[
\frac{1}{2\pi }{\int }_{0}^{2\pi }\ln \left( {1 - {2r}\cos x + {r}^{2}}\right) \mathrm{d}x = 2\ln r,
\]

其中 \( r > 1 \) .

3. 设 \( f \in  C\left\lbrack  {0,1}\right\rbrack  ,{\int }_{0}^{1}{x}^{2}f\left( x\right) \mathrm{d}x = 1 \) .

(1) 证明: \( \mathop{\max }\limits_{{0 \leq  x \leq  1}}\{ \left| {f\left( x\right) }\right| \}  \geq  3 \) ;

(2)又知 \( {\int }_{0}^{1}{xf}\left( x\right) \mathrm{d}x = 0 \) ,证明: \( \mathop{\max }\limits_{{0 \leq  x \leq  1}}\{ \left| {f\left( x\right) }\right| \}  > {10.2} \) .

4. 设 \( f \in  C\left\lbrack  {0,1}\right\rbrack \) ,如果对某个正整数 \( n > 1 \) ,成立

\[
{\int }_{0}^{1}f\left( x\right) \mathrm{d}x = {\int }_{0}^{1}{xf}\left( x\right) \mathrm{d}x = \cdots  = {\int }_{0}^{1}{x}^{n - 1}f\left( x\right) \mathrm{d}x = 0,{\int }_{0}^{1}{x}^{n}f\left( x\right) \mathrm{d}x = 1,
\]

求证: \( M = \mathop{\max }\limits_{{0 \leq  x \leq  1}}\{ \left| {f\left( x\right) }\right| \}  \geq  {2}^{n}\left( {n + 1}\right) \) .

5. 求出使不等式

\[
{c}_{1} \leq  {\int }_{a}^{b}\frac{\sin x}{x}\mathrm{\;d}x \leq  {c}_{2}
\]

成立的最佳常数 \( {c}_{1},{c}_{2} \) ,对其中的积分限分两种情况讨论: (1) \( 0 \leq  a < b \) ; (2) \( a < b \) .

6. 在命题 11.2.3 (即 Young 不等式) 中的可微条件可以去掉, 此外还可以得到另一个方向的不等式. 设 \( f \in  C\lbrack 0, + \infty ) \) ,严格单调增加,且 \( f\left( 0\right)  = 0 \) ,记其反函数为 \( g\left( y\right) \) . 对 \( a, b > 0 \) ,证明下列不等式并解释其几何意义:

\[
{ab} \leq  {\int }_{0}^{a}f\left( x\right) \mathrm{d}x + {\int }_{0}^{b}g\left( y\right) \mathrm{d}y \leq  {bg}\left( b\right)  + {af}\left( a\right)  - f\left( a\right) g\left( b\right) ,
\]

其中成立等号的充分必要条件是 \( b = f\left( a\right) \) (即 \( a = g\left( b\right) \) ).

7. 设 \( f \in  C\left( {a, b}\right) \) ,证明:

(1)若对任何 \( a < {x}_{1} < {x}_{2} < b \) 成立不等式

\[
f\left( \frac{{x}_{1} + {x}_{2}}{2}\right)  \leq  \frac{1}{{x}_{2} - {x}_{1}}{\int }_{{x}_{1}}^{{x}_{2}}f\left( x\right) \mathrm{d}x,
\]

则 \( f \) 为下凸函数;

(2)若对任何 \( a < {x}_{1} < {x}_{2} < b \) 成立不等式

\[
\frac{1}{{x}_{2} - {x}_{1}}{\int }_{{x}_{1}}^{{x}_{2}}f\left( x\right) \mathrm{d}x \leq  \frac{f\left( {x}_{1}\right)  + f\left( {x}_{2}\right) }{2},
\]

则 \( f \) 为下凸函数;

(3) 若以上两个不等式中的任何一个始终成立等号,则 \( f \) 只能是线性函数.

(因此 Hadamard 不等式 (11.7) 中的每个不等式都是 \( f \) 下凸的充分必要条件.)

8. 设 \( f \in  {C}^{1}\left\lbrack  {0, a}\right\rbrack  , f\left( 0\right)  = 0 \) .

(1) 证明:

\[
{\int }_{0}^{a}\left| {f\left( x\right) {f}^{\prime }\left( x\right) }\right| \mathrm{d}x \leq  \frac{a}{2}{\int }_{0}^{a}{\left| {f}^{\prime }\left( x\right) \right| }^{2}\mathrm{\;d}x,
\]

且其中成立等号当且仅当 \( f\left( x\right)  = {cx} \) ;

(2) (Opial 不等式) 增加条件 \( f\left( a\right)  = 0, f \) 在 \( \left( {0, a}\right) \) 上大于 0,证明:

\[
{\int }_{0}^{a}\left| {f\left( x\right) {f}^{\prime }\left( x\right) }\right| \mathrm{d}x \leq  \frac{a}{4}{\int }_{0}^{a}{\left| {f}^{\prime }\left( x\right) \right| }^{2}\mathrm{\;d}x.
\]

9. (Bellman-Gronwall 不等式) 设当 \( x \geq  0 \) 时 \( f\left( x\right) , g\left( x\right) \) 为非负连续函数,且有

\[
f\left( x\right)  \leq  A + {\int }_{0}^{x}f\left( t\right) g\left( t\right) \mathrm{d}t
\]

其中 \( A > 0 \) ,证明: 当 \( x \geq  0 \) 时

\[
f\left( x\right)  \leq  A\exp \left( {{\int }_{0}^{x}g\left( t\right) \mathrm{d}t}\right) .
\]

10. 设 \( f \in  {C}^{2}\left\lbrack  {0,1}\right\rbrack  , f\left( 0\right)  = f\left( 1\right)  = 0, f \) 在 \( \left( {0,1}\right) \) 中无零点,证明:

\[
{\int }_{0}^{1}\left| \frac{{f}^{\prime \prime }\left( x\right) }{f\left( x\right) }\right| \mathrm{d}x > 4,
\]

且其中 4 是最佳下界.

11. 设 \( f \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上可积,且有 \( 0 < m \leq  f\left( x\right)  \leq  M \) ,则有

\[
{\int }_{0}^{1}f\left( x\right) \mathrm{d}x{\int }_{0}^{1}\frac{1}{f\left( x\right) }\mathrm{d}x \leq  \frac{{\left( m + M\right) }^{2}}{4mM}.
\]

(这是 Cauchy-Schwarz 不等式的反向不等式, 也称为 Kantorovich (康托罗维奇) 不等式.)

12. 设非常值函数 \( f \) 在区间 \( \left\lbrack  {a, b}\right\rbrack \) 上可微,且 \( f\left( a\right)  = f\left( b\right)  = 0 \) ,证明: 在 \( \left\lbrack  {a, b}\right\rbrack \) 内至少存在一点 \( \xi \) ,使

\[
\left| {{f}^{\prime }\left( \xi \right) }\right|  > \frac{4}{{\left( b - a\right) }^{2}}{\int }_{a}^{b}\left| {f\left( x\right) }\right| \mathrm{d}x.
\]

13. 设 \( f \in  {C}^{2}\left\lbrack  {0,1}\right\rbrack  , f\left( 0\right)  = f\left( 1\right)  = {f}^{\prime }\left( 0\right)  = 0,{f}^{\prime }\left( 1\right)  = 1 \) ,证明:

\[
{\int }_{0}^{1}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}\mathrm{\;d}x \geq  4
\]

且其中成立等式当且仅当 \( f\left( x\right)  = {x}^{3} - {x}^{2} \) .

14. 设函数 \( f \) 在区间 \( \left\lbrack  {a, b}\right\rbrack \) 上处处大于 0,且对于 \( L > 0 \) 满足 Lipschitz 条件 \( \mid  f\left( {x}_{1}\right)  - \; f\left( {x}_{2}\right) \left| { \leq  L}\right| {x}_{1} - {x}_{2} \mid \) ,又已知对于 \( a \leq  c \leq  d \leq  b \) 有

\[
{\int }_{c}^{d}\frac{\mathrm{d}x}{f\left( x\right) } = \alpha ,\;{\int }_{a}^{b}\frac{\mathrm{d}x}{f\left( x\right) } = \beta ,
\]

证明下列积分不等式:

\[
{\int }_{a}^{b}f\left( x\right) \mathrm{d}x \leq  \frac{{\mathrm{e}}^{2L\beta } - 1}{2L\alpha }{\int }_{c}^{d}f\left( x\right) \mathrm{d}x.
\]

15. 先用微分学或其他方法证明: 当 \( 0 < x < 1 \) 时,成立不等式

\[
0 < \frac{1}{2}\ln \frac{1 + x}{1 - x} - x < \frac{{x}^{3}}{3\left( {1 - {x}^{2}}\right) },
\]

并用 \( x = 1/\left( {{2n} + 1}\right) \) 代入,得到比 (11.34) 更强的不等式. 然后证明比 (11.32) 更为精细的 Stirling 公式,也就是一般性公式 (11.31) 中 \( m = 0 \) 的情况:

\[
\ln n! = \ln \sqrt{2\pi } + \left( {n + \frac{1}{2}}\right) \ln n - n + \frac{{\theta }_{n}}{12n},
\]

或者其等价形式:

\[
n! = \sqrt{2\pi n}{\left( \frac{n}{\mathrm{e}}\right) }^{n}{\mathrm{e}}^{\frac{{\theta }_{n}}{12n}},
\]

其中 \( 0 < {\theta }_{n} < 1 \) .
