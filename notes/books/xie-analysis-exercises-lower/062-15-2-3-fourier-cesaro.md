#### 15.2.3 Fourier 级数的 Cesàro 求和

到目前为止,凡是说到无穷级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n} \) 收敛,就是指它的部分和数列收敛. 这就是由 Cauchy 提出的无穷级数的收敛定义. 但至少从 Euler 起, 就已经出现无穷级数的其他收敛定义. Cesàro 求和就是其中的一种, 它在 Fourier 级数理论中得到了重要的应用 (参见第十三章最后的几个参考题).

定义 设级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 的部分和数列为 \( {S}_{n} = {a}_{0} + {a}_{1} + \cdots  + {a}_{n}, n = 0,1,2,\cdots \) . 定义数列

\[
{\sigma }_{n} = \frac{{S}_{0} + {S}_{1} + \cdots  + {S}_{n - 1}}{n}, n = 1,2,\cdots .
\]

如果存在极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\sigma }_{n} = \sigma \) ,则称级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 在 Cesàro 意义下可求和,且定义 \( \sigma \) 为级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 的 Cesàro 和. 由 Cauchy 命题 (见上册 31 页) 知道,若数列 \( \left\{  {S}_{n}\right\} \) 收敛于数 \( S \) ，则其前 \( n \) 项的平均值 \( {\sigma }_{n} \) 构成的数列也收敛于 \( S \) ，但反之则不然. 因此若级数 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n} \) 在通常意义下收敛，则它在 Cesàro 意义下也收敛，且有相同的和. 这表明对于在通常意义下收敛的级数而言, Cesàro 求和没有给出新的结果.

然而在通常意义下的某些发散级数有可能在 Cesàro 意义下有和. 例如级数

\[
1 - 1 + 1 - 1 + \cdots  = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}
\]

的部分和数列为 \( {S}_{{2k} - 1} = 1,{S}_{2k} = 0, k = 1,2,\cdots \) ,因此该级数的 Cesàro 和为 \( \frac{1}{2} \) . 这就是 Euler 等数学家曾经提出过的和 (参见 \( \left\lbrack  {{26},{50}}\right\rbrack \) ).

初看起来这似乎有点荒谬, 为什么要考虑 (在通常意义下) 发散级数的和? 这样做有什么意义? 下面我们先观察 Cesàro 求和在 Fourier 级数理论中给我们带来什么结果.

命题 15.2.1 (Fejér 定理) 如果以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,并且在点 \( {x}_{0} \) 处有左、右极限 \( f\left( {x}_{0}^{ + }\right) \) 与 \( f\left( {x}_{0}^{ - }\right) \) ,则 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处在 Cesàro 意义下收敛于

\[
\frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  .
\]

特别是当 \( f \) 于点 \( {x}_{0} \) 连续时,则 Fourier 级数在点 \( {x}_{0} \) 的 Cesàro 和就等于 \( f\left( {x}_{0}\right) \) .

证 从部分和函数列 \( {S}_{n}\left( x\right) \) 的 Dirichlet 积分 (15.15) 出发计算 \( {\sigma }_{n}\left( x\right) \) ,经三角变换后可以得到 Fejér 积分:

\[
{\sigma }_{n}\left( x\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( {x + t}\right)  \cdot  \frac{1}{2n}{\left( \frac{\sin \frac{n}{2}t}{\sin \frac{1}{2}t}\right) }^{2}\mathrm{\;d}t
\]

\[
= {\int }_{0}^{\pi }\frac{f\left( {x + t}\right)  + f\left( {x - t}\right) }{2} \cdot  {F}_{n}\left( t\right) \mathrm{d}t,
\]

其中的非负函数

\[
{F}_{n}\left( t\right)  = \frac{1}{n\pi }{\left( \frac{\sin \frac{n}{2}t}{\sin \frac{1}{2}t}\right) }^{2} \tag{15.20}
\]

称为 Fejér 核. 用 \( f\left( x\right)  \equiv  1 \) 代入就得到恒等式 (见上册 330 页的题 10):

\[
{\int }_{a}^{\pi }{F}_{n}\left( t\right) \mathrm{d}t = 1 \tag{15.21}
\]

这样就可以利用 Fejér 积分和恒等式 (15.21) 将问题化为积分估计:

\[
\left| {{\sigma }_{n}\left( {x}_{0}\right)  - \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  }\right|
\]

\[
\leq  {\int }_{0}^{\pi }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t.
\]

现在对每个给定的 \( \varepsilon  > 0 \) 取 \( \delta  > 0 \) ,使得当 \( 0 \leq  t \leq  \delta \) 时,有 \( \left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  < \varepsilon \) 和 \( \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right|  < \varepsilon \) 成立,于是就有

\[
{\int }_{0}^{\delta }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t \leq  \varepsilon {\int }_{0}^{\delta }{F}_{n}\left( t\right) \mathrm{d}t \leq  \varepsilon ,
\]

这里利用了 Fejér 核的非负性和恒等式 (15.21). 再利用当 \( \delta  \leq  t \leq  \pi \) 时

\[
0 \leq  {F}_{n}\left( t\right)  \leq  \frac{1}{n\pi } \cdot  \frac{1}{{\left( \sin \frac{1}{2}\delta \right) }^{2}},
\]

就可以估计得到

\[
{\int }_{\delta }^{\pi }\left( \frac{\left| {f\left( {{x}_{0} + t}\right)  - f\left( {x}_{0}^{ + }\right) }\right|  + \left| {f\left( {{x}_{0} - t}\right)  - f\left( {x}_{0}^{ - }\right) }\right| }{2}\right) {F}_{n}\left( t\right) \mathrm{d}t = O\left( \frac{1}{n}\right) .
\]

因此存在 \( N \) ,使得当 \( n > N \) 时有

\[
\left| {{\sigma }_{n}\left( {x}_{0}\right)  - \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  }\right|  < {2\varepsilon },
\]

这就是

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\sigma }_{n}\left( {x}_{0}\right)  = \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack  .
\]

注 将 Fejér 积分的估计和 Dirichlet 积分的估计作比较, 可见这里要容易得多, 连 Riemann 引理也不需要用. 原因在于 Fejér 核是非负的, 而 Dirichlet 核则是变号的 (见图 15.2). 如前所示的 Gibbs 现象的根源都在于此. 读者可以将图 15.4 中的 Fejér 核的示意图与图 15.2 作比较. 此外, 还可以参考 [18] 第三卷的 740 小节关于正核的系统论述. 在下一章关于 Weierstrass 逼近定理的证明中我们将再次接触到这种核函数方法 (又称奇异积分方法).

由 Fejér 定理可以立即得到关于 Fourier 级数收敛的一个重要结果.

![bo_d7fsu8491nqc7381io7g_104_120_171_1244_639_0.jpg](images/xie_analysis_exercises_lower_002_bod7fsu8491nqc7381io7g10412017112446390.jpg)

图 15.4

命题 15.2.2 设以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,点 \( {x}_{0} \) 是 \( f \) 的连续点或第一类间断点,如果 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处收敛,则它一定收敛于 \( f\left( {x}_{0}\right) \) 或 \( \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack \) .

证 设 \( f \) 的 Fourier 级数在点 \( {x}_{0} \) 处收敛于 \( s \) ,则其 Cesàro 和也是 \( s \) . 但由 Fejér 定理 (命题 15.2.1) 可以知道它的 Cesàro 和为 \( f\left( {x}_{0}\right) \) 或 \( \frac{1}{2}\left\lbrack  {f\left( {x}_{0}^{ + }\right)  + f\left( {x}_{0}^{ - }\right) }\right\rbrack \) ,可见命题成立.

注 结合前面提到的 Carleson 的工作, 可以知道连续周期函数的 Fourier 级数展开式一定几乎处处成立.

对于连续的周期函数, 从 Fejér 定理还可以得到两个重要结论.

命题 15.2.3 (Fourier 级数的惟一性定理) 设 \( f \) 为周期 \( {2\pi } \) 的连续函数,且其 Fourier 系数均等于 0 : \( {a}_{0} = 0,{a}_{n} = {b}_{n} = 0, n = 1,2,\cdots \) ,则 \( f \) 必是恒等于 0 的常值函数.

证 这时 \( f \) 的 Fourier 级数的每一项都恒等于 0,因此部分和函数列 \( \left\{  {{S}_{n}\left( x\right) }\right\} \) 的每一项也都恒等于 0 . 由此就知道 \( {\sigma }_{n}\left( x\right)  \equiv  0, n = 1,2,\cdots \) . 从 Fejér 定理 (命题 15.2.1) 可见 \( f \equiv  0 \) .

注 由此可知若两个连续函数有相同的 Fourier 级数, 则这两个连续函数必相同. 注意: 这与 Taylor 级数很不一样 (参见命题 14.4.2, 67 页底注和上册 169 页的例题 6.2.4).

命题 15.2.4 (关于一致收敛的 Fejér 定理) 如果 \( f \) 是以 \( {2\pi } \) 为周期的连续函数,则它的 Fourier 级数在 Cesàro 意义下一致收敛于 \( f \) .

注 1 这只需要在命题 15.2.1 的证明中利用连续函数的 Cantor 定理 (见上册 §5.4) 即可.

注 2 由于 \( \left\{  {{\sigma }_{n}\left( x\right) }\right\} \) 是三角多项式函数列,因此已经得到了关于周期连续函数用三角多项式一致逼近的 Weierstrass 第二逼近定理. 这将在下一章中再作进一步介绍. (又见命题 15.2.8 的注和参考题 19.)
