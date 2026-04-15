## 第二组参考题

1. 设 \( \mathcal{T} \) 是 \( {\mathbf{R}}^{n} \) 到 \( {\mathbf{R}}^{n} \) 的一个映射,如果存在常数 \( \theta ,0 \leq  \theta  < 1 \) 以及正整数 \( {n}_{0} \) ,使得

\[
\left| {{\mathcal{T}}^{{n}_{0}}\mathbf{x} - {\mathcal{T}}^{{n}_{0}}\mathbf{y}}\right|  \leq  \theta \left| {\mathbf{x} - \mathbf{y}}\right| ,\forall \mathbf{x},\mathbf{y} \in  {\mathbf{R}}^{n},
\]

证明: 映射 \( \mathcal{T} \) 有惟一的不动点.

2. 设 \( \Omega \) 是 \( {\mathbf{R}}^{n} \) 中的有界闭集, \( \mathbf{f} \) 是 \( \Omega \) 到 \( \Omega \) 的一个映射,满足

\[
\left| {\mathbf{f}\left( \mathbf{x}\right)  - \mathbf{f}\left( \mathbf{y}\right) }\right|  < \left| {\mathbf{x} - \mathbf{y}}\right| ,\forall \mathbf{x},\mathbf{y} \in  \Omega ,\mathbf{x} \neq  \mathbf{y}.
\]

证明: \( f \) 在 \( \Omega \) 中存在惟一的不动点. 能否把命题中有界闭集的假设减弱为一般的有界集或无界的闭集?

3. 证明: 连续映射将连通集映为连通集.

4. 设 \( \Omega \) 是 \( {\mathbf{R}}^{n} \) 中的区域,函数 \( f \) 定义在 \( \Omega \) 上,对于点 \( {\mathbf{x}}_{0} \in  \Omega \) ,如果 \( \forall \varepsilon  > 0 \) ,存在 \( \delta  > 0 \) ,使得当点 \( \mathbf{x} \in  \Omega \) ,且 \( \left| {\mathbf{x} - {\mathbf{x}}_{0}}\right|  < \delta \) 时

\[
f\left( \mathbf{x}\right)  < f\left( {\mathbf{x}}_{0}\right)  + \varepsilon \;\left( {\text{ 或 }f\left( \mathbf{x}\right)  > f\left( {\mathbf{x}}_{0}\right)  - \varepsilon }\right) ,
\]

则称 \( f \) 在点 \( {\mathbf{x}}_{0} \) 处上半连续 (或下半连续). 证明:

(1) \( f \) 在点 \( {\mathbf{x}}_{0} \) 处上半连续的充分必要条件是 \( f \) 在点 \( {\mathbf{x}}_{0} \) 的邻近有上界,且

\[
\mathop{\lim }\limits_{{\Omega  \ni  \mathbf{x} \rightarrow  {\mathbf{x}}_{0}}}f\left( \mathbf{x}\right)  \leq  f\left( {\mathbf{x}}_{0}\right)
\]

(2) \( f \) 在点 \( {\mathbf{x}}_{0} \) 处下半连续的充分必要条件是 \( f \) 在点 \( {\mathbf{x}}_{0} \) 的邻近有下界，且

\[
\mathop{\lim }\limits_{{\Omega  \ni  \mathbf{x} \rightarrow  {\mathbf{x}}_{0}}}f\left( \mathbf{x}\right)  \geq  f\left( {\mathbf{x}}_{0}\right) .
\]

5. 设 \( \Omega \) 是 \( {\mathbf{R}}^{n} \) 中的紧集, \( f \) 是 \( \Omega \) 上的上半连续函数 (下半连续函数),则 \( f \) 在 \( \Omega \) 上有上界并达到最大值 (有下界并达到最小值).

6. 设 \( \left\{  {f}_{k}\right\} \) 是 \( {\mathbf{R}}^{n} \) 中紧集 \( \Omega \) 上的连续函数列,如果对每个点 \( \mathbf{x} \in  \Omega \) ,均有

\[
\mathop{\sup }\limits_{k}\left\{  {{f}_{k}\left( \mathbf{x}\right) }\right\}   <  + \infty
\]

证明: 函数

\[
f\left( \mathbf{x}\right)  = \mathop{\sup }\limits_{k}\left\{  {{f}_{k}\left( \mathbf{x}\right) }\right\}
\]

在 \( \Omega \) 上达最小值.

7. (Peano 曲线 \( {}^{ \oplus  } \) ) 设 \( \Delta \) 是 \( {\mathbf{R}}^{2} \) 中由 \( y = 0, y = \sqrt{3}x \) 和 \( y =  - \sqrt{3}x + \sqrt{3} \) 所围成的正三角形闭区域. 映射 \( {\mathbf{f}}_{0} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \Delta \) 定义为 \( {\mathbf{f}}_{0}\left( 0\right)  = \left( {0,0}\right) ,{\mathbf{f}}_{0}\left( \frac{1}{2}\right)  = \; \left( {\frac{1}{2},\frac{\sqrt{3}}{6}}\right) ,{\mathbf{f}}_{0}\left( 1\right)  = \left( {1,0}\right) \) ,其余线性联结. 则 \( {\mathbf{f}}_{0}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 是 \( \Delta \) 中从端点 \( A \) 到重心 \( K \) 再到端点 \( B \) 的一条折线 \( L \) (见图 18.1(a)).

---

① 关于 Peano 曲线这个名称的由来以及另一个例子见 16.4.2 小节.

---

然后将 \( \Delta \) 等分成四个边长为 \( \frac{1}{2} \) 的小正三角形区域 \( {\Delta }_{i}, i = 1,2,3,4, L \) 等分成长度为 \( \frac{\sqrt{3}}{6} \) 的四段 \( {L}_{i}, i = 1,2,3,4 \) . 设 \( {\mathbf{g}}_{0} : L \rightarrow  \Delta \) 以类似于 \( {\mathbf{f}}_{0} \) 的方式依次把 \( {L}_{i}, i = 1,2,3,4 \) 映到 \( {\Delta }_{i}, i = 1,2,3,4 \) 中. 令 \( {\mathbf{f}}_{1} = {\mathbf{g}}_{0} \circ  {\mathbf{f}}_{0} \) ,则 \( {\mathbf{f}}_{1}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 就是 \( \Delta \) 中一条联结 \( A, B \) 的折线，由 \( 2 \times  4 \) 段直线段连成 (见图 18.1(b)).

再设 \( {\mathbf{g}}_{1} \) 把 \( {\mathbf{f}}_{1}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 的每一段作类似于 \( {\mathbf{g}}_{0} \) 那样的变换. 令 \( {\mathbf{f}}_{2} = {\mathbf{g}}_{1} \circ  {\mathbf{f}}_{1} \) ,则 \( {\mathbf{f}}_{2}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 就如图所示是一条由 \( 2 \times  {4}^{2} \) 段直线段连成的折线 (见图 18.1(c)).

依类似的方式定义 \( {\mathbf{f}}_{k} = {\mathbf{g}}_{k - 1} \circ  {\mathbf{f}}_{k - 1} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \Delta , k = 3,4,\cdots \) ,使得 \( {\mathbf{f}}_{k}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 是一条由 \( 2 \times  {4}^{k} \) 段直线段连成的折线,每段直线分别位于边长为 \( \frac{1}{{2}^{k}} \) 的小正三角形区域中,且 \( {\mathbf{g}}_{k - 1} \) 保持 \( {\mathbf{f}}_{k - 1}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) 的点在它所在的小正三角形区域中.

![bo_d7fsu8491nqc7381io7g_176_107_991_1296_442_0.jpg](images/xie_analysis_exercises_lower_008_bod7fsu8491nqc7381io7g17610799112964420.jpg)

图 18.1

(1) 证明: 任取 \( n > m \) ,有 \( \left| {{\mathbf{f}}_{n}\left( t\right)  - {\mathbf{f}}_{m}\left( t\right) }\right|  \leq  \frac{1}{{2}^{m}} \) ,从而 \( {\mathbf{f}}_{n}\left( t\right) \left( {n = 1,2,\cdots }\right) \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上一致收敛. 设其极限映射为 \( \mathbf{f} \) ,证明 \( \mathbf{f} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \Delta \) 连续;

(2)证明: \( \mathbf{f}\left( \left\lbrack  {0,1}\right\rbrack  \right)  = \Delta \) ,即连续映射 \( \mathbf{f} \) 把一个区间 \( \left\lbrack  {0,1}\right\rbrack \) 映为 \( {\mathbf{R}}^{2} \) 中的一个面积为 \( \frac{\sqrt{3}}{4} \) 的区域 \( \Delta \) .

8. (Tietze (蒂策) 扩张定理) 设 \( D \subset  {\mathbf{R}}^{n} \) 为闭子集, \( f : D \rightarrow  \mathbf{R} \) 为连续函数,且 \( \left| {f\left( \mathbf{x}\right) }\right|  \leq  M,\mathbf{x} \in  D \) . 设 \( {g}_{0}\left( \mathbf{x}\right)  = 0,{g}_{k}\left( \mathbf{x}\right) \) 归纳定义为

\[
{g}_{k}\left( \mathbf{x}\right)  = \frac{{2}^{k - 1}d\left( {\mathbf{x},{A}_{k}}\right) }{{3}^{k}\left( {d\left( {\mathbf{x},{A}_{k}}\right)  + d\left( {\mathbf{x},{B}_{k}}\right) }\right) } - \frac{{2}^{k - 1}d\left( {\mathbf{x},{B}_{k}}\right) }{{3}^{k}\left( {d\left( {\mathbf{x},{A}_{k}}\right)  + d\left( {\mathbf{x},{B}_{k}}\right) }\right) },
\]

其中

\[
{A}_{k} = \left\{  {\mathbf{x} \in  D \mid  {\varphi }_{k}\left( \mathbf{x}\right)  \geq  \frac{{2}^{k - 1}}{{3}^{k}}M}\right\}
\]

\[
{B}_{k} = \left\{  {\mathbf{x} \in  D\left| {\;{\varphi }_{k}\left( \mathbf{x}\right)  \leq   - \frac{{2}^{k - 1}}{{3}^{k}}M}\right. }\right\}  ,
\]

而 \( {\varphi }_{k}\left( \mathbf{x}\right)  = f\left( \mathbf{x}\right)  - \left\lbrack  {{g}_{0}\left( \mathbf{x}\right)  + {g}_{1}\left( \mathbf{x}\right)  + \cdots  + {g}_{k - 1}\left( \mathbf{x}\right) }\right\rbrack  , k = 1,2,\cdots \) .

(1)证明: \( {g}_{k}\left( \mathbf{x}\right) \left( {k = 1,2,\cdots }\right) \) 连续，级数 \( \mathop{\sum }\limits_{{k = 1}}^{\infty }{g}_{k}\left( \mathbf{x}\right) \) 在 \( {\mathbf{R}}^{n} \) 上一致收敛到 \( {\mathbf{R}}^{n} \) 上的连续函数 \( g\left( \mathbf{x}\right) \) ,并且当 \( \mathbf{x} \in  D \) 时 \( g\left( \mathbf{x}\right)  = f\left( \mathbf{x}\right) \) . 因此 \( g \) 称为 \( f \) 在 \( {\mathbf{R}}^{n} \) 上的连续扩张, 也称连续开拓;

(2) 证明: (1) 的结论当 \( f \) 并不有界时也成立.

(以上两题取自 [2], 又见 [3] 之 §16.3.)

9. 是否能把开集上的连续函数连续扩张到全空间？一致连续函数呢? 考察 \( \mathbf{R} \) 中的例子.

10. 证明: 可以把定义在 \( {\mathbf{R}}^{n} \) 中有理点集上的一致连续函数惟一扩张到全空间.
