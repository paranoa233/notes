## §5.4 一致连续性与 Cantor 定理

函数的一致连续性是一个比较精细的概念. 可以认为这个概念是由于数学分析内部理论发展的需要而产生的. 因此我们在下面先对这个概念列出要点, 提出几个思考题, 然后给出 Cantor (康托尔) 定理的证明, 并讨论其应用.

#### 5.4.1 内容提要

关于函数的一致连续性的要点如下.

1. 定义: 函数 \( f \) 在区间 \( I \) 上一致连续,如果对每一个 \( \varepsilon  > 0 \) ,存在 \( \delta  > 0 \) ,使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  I \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon \) .

2. 若 \( f \) 在区间 \( I \) 上一致连续,则 \( f \) 在 \( I \) 上一定连续.

3. 若 \( f \) 在区间 \( I \) 上一致连续,又有区间 \( J \subset  I \) ,则 \( f \) 在 \( J \) 上也一致连续.

4. 函数 \( f \) 在区间 \( I \) 上连续就是在 \( I \) 的每一点连续,因此这是一个逐点 (pointwise) 定义的概念. 从本质上看,连续性是个局部概念. 但是 \( f \) 在区间 \( I \) 上的一致连续性则是由 \( f \) 和 \( I \) 两者共同确定的整体性概念. 与此类似的是函数在区间上的有界性等概念.

5. Cantor 定理: 有界闭区间上的连续函数必在这个区间上一致连续.

6. 有界开区间 \( \left( {a, b}\right) \) 上的连续函数 \( f \) 在 \( \left( {a, b}\right) \) 上一致连续的充分必要条件是存在两个有限的单侧极限 \( f\left( {a}^{ + }\right) \) 和 \( f\left( {b}^{ - }\right) \) (见下面的例题 5.4.5).

7. 有界区间 (不论开或闭或半开半闭) 上的一致连续函数一定有界 (留作练习).

#### 5.4.2 思考题

1. 写出函数 \( f \) 在区间 \( I \) 上不一致连续的正面叙述.

2. 判断对或错: \( f \) 在区间 \( \lbrack a, b) \) 上连续,则 \( f \) 在 \( \lbrack a, b) \) 上一致连续.

3. 判断对或错: \( f \) 在区间 \( \left( {a, b}\right) \) 内的每一个闭子区间上连续,则 \( f \) 在 \( \left( {a, b}\right) \) 上一致连续.

4. 判断对或错: \( f \) 在区间 \( \left( {a, b}\right) \) 上连续,又有 \( a < c < d < b \) ,则 \( f \) 在区间 \( \left( {c, d}\right) \) 上一致连续.

#### 5.4.3 Cantor 定理的证明

例题 5.4.1 用覆盖定理证明 Cantor 定理.

证 \( \forall \varepsilon  > 0 \) 和 \( {x}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) ,由于 \( f \) 在 \( {x}_{0} \) 连续,存在 \( {\delta }_{0} > 0 \) ,当 \( x \in  {O}_{{\delta }_{0}}\left( {x}_{0}\right)  \cap  \left\lbrack  {a, b}\right\rbrack \) 时,成立 \( \left| {f\left( x\right)  - f\left( {x}_{0}\right) }\right|  < \frac{1}{2}\varepsilon \) . 因此当 \( {x}^{\prime },{x}^{\prime \prime } \in  {O}_{{\delta }_{0}}\left( {x}_{0}\right)  \cap  \left\lbrack  {a, b}\right\rbrack \) 时,就有

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  \leq  \left| {f\left( {x}^{\prime }\right)  - f\left( {x}_{0}\right) }\right|  + \left| {f\left( {x}_{0}\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \frac{1}{2}\varepsilon  + \frac{1}{2}\varepsilon  = \varepsilon .
\]

对每个点 \( x \in  \left\lbrack  {a, b}\right\rbrack \) 都这样做,就得到区间 \( \left\lbrack  {a, b}\right\rbrack \) 的一个开覆盖. 这里出现了一个困难. 即如果对这个开覆盖直接应用覆盖定理的话, 则难以完成定理的证明. (读者可以试一下, 看看困难何在.) 再次应用例题 3.5.3 (即加强形式的覆盖定理), 将其中的 Lebesgue 数记为 \( \eta \) . 当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left\lbrack  {a, b}\right\rbrack \) ,且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \eta \) 时,在开覆盖中存在一个开区间,它覆盖点 \( {x}^{\prime } \) 和 \( {x}^{\prime \prime } \) . 由上述构造方法,就知道成立

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon
\]

这样就已经证明了 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上一致连续.

例题 5.4.2 用凝聚定理证明 Cantor 定理.

证 用反证法. 设 \( f \in  C\left\lbrack  {a, b}\right\rbrack \) ,但在 \( \left\lbrack  {a, b}\right\rbrack \) 上不一致连续. 应用 \( \text{ § }{1.4} \) 的对偶法则, 可以得到不一致连续的正面叙述: \( \exists {\varepsilon }_{0} > 0,\forall \delta  > 0,\exists {x}^{\prime },{x}^{\prime \prime } \in  \left\lbrack  {a, b}\right\rbrack  ,\left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) , 使得 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  \geq  {\varepsilon }_{0} \) 成立.

取 \( {\delta }_{n} = 1/n \) ,将对应的点 \( {x}^{\prime },{x}^{\prime \prime } \) 记为 \( {x}_{n} \) 和 \( {x}_{n}^{\prime } \) . 并对每一个 \( n \in  {\mathbf{N}}_{ + } \) 都这样做, 就得到区间 \( \left\lbrack  {a, b}\right\rbrack \) 中的两个数列 \( \left\{  {x}_{n}\right\} \) 和 \( \left\{  {x}_{n}^{\prime }\right\} \) ,使得

\[
\left| {{x}_{n} - {x}_{n}^{\prime }}\right|  < \frac{1}{n},\left| {f\left( {x}_{n}\right)  - f\left( {x}_{n}^{\prime }\right) }\right|  \geq  {\varepsilon }_{0},\forall n \in  {\mathbf{N}}_{ + }.
\]

对数列 \( \left\{  {x}_{n}\right\} \) 用凝聚定理,知道存在收敛子列 \( \left\{  {x}_{{n}_{k}}\right\} \) . 记它的极限为 \( \xi \) ,即有

\[
\mathop{\lim }\limits_{{k \rightarrow  \infty }}{x}_{{n}_{k}} = \xi
\]

由于

\[
{x}_{{n}_{k}} - \frac{1}{{n}_{k}} < {x}_{{n}_{k}}^{\prime } < {x}_{{n}_{k}} + \frac{1}{{n}_{k}},
\]

以及 \( {n}_{k} \geq  k \) ，因此数列 \( \left\{  {x}_{n}^{\prime }\right\} \) 的对应子列 \( \left\{  {x}_{{n}_{k}}^{\prime }\right\} \) 也收敛于 \( \xi \) ，即有

\[
\mathop{\lim }\limits_{{k \rightarrow  \infty }}{x}_{{n}_{k}}^{\prime } = \xi
\]

由于 \( f \) 在点 \( \xi \) 连续,因此对 \( {\varepsilon }_{0} \) ,存在 \( \eta  > 0 \) ,当 \( {x}^{\prime },{x}^{\prime \prime } \in  {O}_{\eta }\left( \xi \right) \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < {\varepsilon }_{0} \) . 但当 \( k \) 充分大时,就有 \( {x}_{{n}_{k}},{x}_{{n}_{k}}^{\prime } \in  {O}_{\eta }\left( \xi \right) \) . 这样就和

\[
\left| {f\left( {x}_{{n}_{k}}\right)  - f\left( {x}_{{n}_{k}}^{\prime }\right) }\right|  \geq  {\varepsilon }_{0}
\]

矛盾.

#### 5.4.4 例题

例题 5.4.3 根据定义证明:

(1)对于满足 \( 0 < \eta  < 1 \) 的每个 \( \eta , f\left( x\right)  = \frac{1}{x} \) 在 \( \lbrack \eta ,1) \) 上一致连续;

(2) \( f\left( x\right)  = \frac{1}{x} \) 在开区间 \( \left( {0,1}\right) \) 上不一致连续.

证 (1) 对 \( {x}^{\prime },{x}^{\prime \prime } \in  \lbrack \eta ,1) \) ,有

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  = \left| {\frac{1}{{x}^{\prime }} - \frac{1}{{x}^{\prime \prime }}}\right|  = \frac{\left| {x}^{\prime } - {x}^{\prime \prime }\right| }{{x}^{\prime }{x}^{\prime \prime }} \leq  \frac{\left| {x}^{\prime } - {x}^{\prime \prime }\right| }{{\eta }^{2}}.
\]

因此对 \( \varepsilon  > 0 \) ,只要取

\[
\delta  = {\eta }^{2}\varepsilon
\]

就可以使得 \( {x}^{\prime },{x}^{\prime \prime } \in  \lbrack \eta ,1) \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {\frac{1}{{x}^{\prime }} - \frac{1}{{x}^{\prime \prime }}}\right|  < \varepsilon \) . 这表明 \( f\left( x\right)  = \frac{1}{x} \) 在区间 \( \lbrack \eta ,1) \) 上一致连续.

( 2 )用反证法. 设 \( f\left( x\right)  = \frac{1}{x} \) 在区间 \( \left( {0,1}\right) \) 上一致连续. 则对 \( \varepsilon  = 1 \) ，存在 \( \delta  > 0 \) ， 使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left( {0,1}\right) \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时，成立

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  = \left| {\frac{1}{{x}^{\prime }} - \frac{1}{{x}^{\prime \prime }}}\right|  = \frac{\left| {x}^{\prime } - {x}^{\prime \prime }\right| }{{x}^{\prime }{x}^{\prime \prime }} < 1.
\]

设 \( n \geq  2 \) ,并令

\[
{x}^{\prime } = \frac{1}{n},{x}^{\prime \prime } = \frac{1}{2n}
\]

则有

\[
\left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  = \frac{1}{2n},\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  = n \geq  2 > 1.
\]

因此只要取

\[
n > \frac{1}{2\delta }
\]

就引出矛盾,所以 \( f\left( x\right)  = \frac{1}{x} \) 在 \( \left( {0,1}\right) \) 上不一致连续.

注 1 若初学者对理解一致连续性概念有困难, 建议先将本例题彻底搞清楚. 利用 \( y = 1/x \) 的几何图形,可以体会出一致连续性与函数的“陡度”有关. 从证明也可看出,本例中的困难完全发生在点 \( x = 0 \) 的右侧邻近.

注 2 可以类比: 同一个函数 \( f\left( x\right)  = 1/x \) 在 \( \left( {0,1}\right) \) 上无界,但在 \( \left( {0,1}\right) \) 内的每一个闭子区间上有界. 由此可见, 有界性和一致连续性是属于同一类型的概念, 即整体性质, 也就是说与函数在整个区间上的性质有关. 而连续性、极限的存在性等是局部性质, 即只与所考虑的点附近的函数性质有关.

例题 5.4.4 若函数 \( f \) 在区间 \( (a, b\rbrack \) 和 \( \lbrack b, c) \) 上分别为一致连续,证明: \( f \) 在 \( \left( {a, c}\right) \) 上一致连续.

证 对 \( \varepsilon  > 0 \) ,由条件知道存在 \( {\delta }_{1} > 0 \) ,使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  (a, b\rbrack \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < {\delta }_{1} \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon /2 \) . 又存在 \( {\delta }_{2} > 0 \) ,使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  \lbrack b, c) \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < {\delta }_{2} \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon /2 \) .

取 \( \delta  = \min \left\{  {{\delta }_{1},{\delta }_{2}}\right\} \) . 我们断言: 当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left( {a, c}\right) \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon . \)

先考虑 \( {x}^{\prime } < b < {x}^{\prime \prime } \) 的情况. 这时从 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 推出 \( \left| {{x}^{\prime } - b}\right|  < {\delta }_{1},\left| {{x}^{\prime \prime } - b}\right|  < {\delta }_{2} \) 成立, 因此

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  \leq  \left| {f\left( {x}^{\prime }\right)  - f\left( b\right) }\right|  + \left| {f\left( b\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \frac{\varepsilon }{2} + \frac{\varepsilon }{2} = \varepsilon .
\]

对于其他情况,即 \( {x}^{\prime },{x}^{\prime \prime } \) 同属区间 \( (a, b\rbrack \) 或 \( \lbrack b, c) \) ,结论是明显的. 因此就证明了 \( f \) 在 \( \left( {a, c}\right) \) 上是一致连续的.

注 用下一个例题的结果可立即导致本题的结论. 但上面的证明只涉及一致连续性的定义, 完全是初等的. 而下一个例题的证明则需要用到 Cantor 定理和 Cauchy 收敛准则, 要 “高级” 得多.

例题 5.4.5 证明: 有界开区间 \( \left( {a, b}\right) \) 上的连续函数 \( f \) 在 \( \left( {a, b}\right) \) 上一致连续的充分必要条件是存在两个有限的单侧极限 \( f\left( {a}^{ + }\right) \) 和 \( f\left( {b}^{ - }\right) \) .

证 先证充分性. 在闭区间 \( \left\lbrack  {a, b}\right\rbrack \) 上构造辅助函数

\[
F\left( x\right)  = \left\{  \begin{array}{ll} f\left( {a}^{ + }\right) , & x = a, \\  f\left( x\right) , & x \in  \left( {a, b}\right) , \\  f\left( {b}^{ - }\right) , & x = b. \end{array}\right.
\]

则可以看出 \( F \in  C\left\lbrack  {a, b}\right\rbrack \) . 对 \( F \) 应用 Cantor 定理,可见 \( F \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上一致连续. 因此 \( f \) 在 \( \left( {a, b}\right) \) 上也一致连续. (这与例题 5.3.3 的第一个证明完全相同.)

再证必要性. 不妨只写出存在 \( f\left( {a}^{ + }\right) \) 的证明. 对 \( \varepsilon  > 0 \) ,由于 \( f \) 在 \( \left( {a, b}\right) \) 上一致连续,因此存在 \( \delta  > 0 \) ,使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left( {a, b}\right) \) ,且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon . \)

因此当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left( {a, a + \delta }\right) \) 时,就有 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon \) 成立. 应用关于右侧极限的 Cauchy 收敛准则 (命题 4.2.5),可见存在极限 \( f\left( {a}^{ + }\right) \) .

以下讨论在无限区间上函数的一致连续性. 首先有如下的一个基本结果.

例题 5.4.6 设 \( f \in  C\lbrack a, + \infty ) \) ,且存在有限极限 \( f\left( {+\infty }\right)  = A \) . 证明: \( f \) 在 \( \lbrack a, + \infty ) \) 上一致连续.

证 对 \( \varepsilon  > 0 \) ,存在 \( M > a \) ,当 \( x > M \) 时成立 \( \left| {f\left( x\right)  - A}\right|  < \frac{1}{2}\varepsilon \) . 又利用 Cantor 定理,知道 \( f \) 在 \( \left\lbrack  {a, M + 1}\right\rbrack \) 上一致连续. 因此对上述 \( \varepsilon \) ,存在 \( \delta  > 0 \) ,使得当 \( {x}^{\prime },{x}^{\prime \prime } \in  \left\lbrack  {a, M + 1}\right\rbrack \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon \) .

不妨假定上述 \( \delta  < 1 \) . 我们断言: 当 \( {x}^{\prime },{x}^{\prime \prime } \in  \lbrack a, + \infty ) \) 且 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta \) 时,成立 \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon . \)

实际上,如 \( {x}^{\prime },{x}^{\prime \prime } \in  \left\lbrack  {a, M + 1}\right\rbrack \) ,则已无问题. 又若 \( {x}^{\prime },{x}^{\prime \prime } > M \) ,则有

\[
\left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  \leq  \left| {f\left( {x}^{\prime }\right)  - A}\right|  + \left| {A - f\left( {x}^{\prime \prime }\right) }\right|  < \frac{\varepsilon }{2} + \frac{\varepsilon }{2} = \varepsilon .
\]

由于 \( \left| {{x}^{\prime } - {x}^{\prime \prime }}\right|  < \delta  < 1 \) ,只可能发生以上两种情况.

注 在教学中发现, 学生经常会对上述命题作出以下错误的证明:

“ \( \forall \varepsilon  > 0 \) ,由于 \( f\left( {+\infty }\right)  = A \) ,因此存在 \( M > a \) ,使当 \( {x}^{\prime },{x}^{\prime \prime } \in  \lbrack M, + \infty ) \) 时, \( \left| {f\left( {x}^{\prime }\right)  - f\left( {x}^{\prime \prime }\right) }\right|  < \varepsilon \) . 由 \( \varepsilon \) 的任意性,得 \( f \) 在 \( \lbrack M, + \infty ) \) 上一致连续. 再由 Cantor 定理, \( f \) 在 \( \left\lbrack  {a, M + 1}\right\rbrack \) 上一致连续,所以 \( f \) 在 \( \lbrack a, + \infty ) \) 上一致连续."

请读者思考上述证明错在哪里.

但是对于在无限区间上的函数的一致连续性来说,上述极限 \( f\left( {+\infty }\right) \) 的存在并非必要. 函数的有界性也不是必要的. 例如 \( f\left( x\right)  = {ax} + b \) 在 \( \left( {-\infty , + \infty }\right) \) 上一致连续. 再举一个更有意义的例题.

例题 5.4.7 证明: 函数 \( \sqrt{x} \) 在区间 \( \left( {0, + \infty }\right) \) 上一致连续.

证 1 先分别证明 \( \sqrt{x} \) 在区间 \( (0,1\rbrack \) 和 \( \lbrack 1, + \infty ) \) 上的一致连续性.

从例题 5.4.5 或在 \( \left\lbrack  {0,1}\right\rbrack \) 上用 Cantor 定理,就知道 \( \sqrt{x} \) 在 \( (0,1\rbrack \) 上一致连续.

在区间 \( \lbrack 1, + \infty ) \) 上,可以从

\[
\left| {\sqrt{{x}^{\prime }} - \sqrt{{x}^{\prime \prime }}}\right|  = \frac{\left| {x}^{\prime } - {x}^{\prime \prime }\right| }{\sqrt{{x}^{\prime }} + \sqrt{{x}^{\prime \prime }}} \leq  \frac{1}{2}\left| {{x}^{\prime } - {x}^{\prime \prime }}\right|
\]

推出 \( \sqrt{x} \) 在 \( \lbrack 1, + \infty ) \) 上一致连续.

然后可以用例题 5.4.4 中的方法合并两个区间，得到所要的结论 (从略).

证 2 利用一个可以直接验证的不等式,即当 \( 0 \leq  b \leq  a \) 时成立

\[
\sqrt{a} - \sqrt{b} \leq  \sqrt{a - b}
\]

就有对任何 \( {x}^{\prime },{x}^{\prime \prime } \geq  0 \) 成立的不等式

\[
\left| {\sqrt{{x}^{\prime }} - \sqrt{{x}^{\prime \prime }}}\right|  \leq  \sqrt{\left| {x}^{\prime } - {x}^{\prime \prime }\right| }.
\]

因此对 \( \varepsilon  > 0 \) ,只要取 \( \delta  = {\varepsilon }^{2} \) ,就可以直接得到所要的结论.

在无限区间上的有界函数也可以不一致连续. 下面就是一个典型例子.

![bo_d7fstb491nqc7381io20_159_328_536_904_297_0.jpg](images/xie_analysis_exercises_upper_004_bod7fstb491nqc7381io201593285369042970.jpg)

图 5.2

例题 5.4.8 证明: 函数 \( \sin {x}^{2} \) 在 \( \left( {-\infty , + \infty }\right) \) 上不一致连续.

证 用反证法. 设 \( \sin {x}^{2} \) (如图 5.2 所示) 在 \( \left( {-\infty , + \infty }\right) \) 上一致连续,则 \( \forall \varepsilon  > 0 \) , 存在 \( \delta  > 0 \) ,当 \( {x}_{1},{x}_{2} \) 满足 \( \left| {{x}_{1} - {x}_{2}}\right|  < \delta \) 时,成立

\[
\left| {\sin {x}_{1}^{2} - \sin {x}_{2}^{2}}\right|  < \varepsilon \tag{5.3}
\]

设 \( n \in  {\mathbf{N}}_{ + } \) ,令

\[
{x}_{1} = \sqrt{n\pi },{x}_{2} = \sqrt{{n\pi } + \frac{\pi }{2}},
\]

则 \( \sin {x}_{1}^{2} = 0,\sin {x}_{2}^{2} =  \pm  1 \) . 因此当 \( \varepsilon  < 1 \) 时,不等式 (5.3) 不能成立.

但又有

\[
\left| {{x}_{1} - {x}_{2}}\right|  = \frac{\frac{\pi }{2}}{\sqrt{n\pi } + \sqrt{{n\pi } + \frac{\pi }{2}}},
\]

因此可以看出,当 \( n \) 充分大时就有 \( \left| {{x}_{1} - {x}_{2}}\right|  < \delta \) 成立. 由此引出矛盾.

#### 5.4.5 练习题

1. 若 \( f \) 在区间 \( I \) 上定义,且存在 \( L > 0 \) ,使得对任意 \( {x}_{1},{x}_{2} \in  I \) 成立 \( \mid  f\left( {x}_{1}\right)  - \; f\left( {x}_{2}\right) \left| { \leq  L}\right| {x}_{1} - {x}_{2} \mid \) ,则称 \( f \) 在 \( I \) 上满足 Lipschitz (利普希茨) 条件. 证明: 在区间 \( I \) 上满足 Lipschitz 条件的函数必是一致连续函数.

2. 根据一致连续性的定义直接证明: 若 \( f \) 在 \( \left( {a, b}\right) \) 上一致连续,则 \( f \) 有界.

3. (1) 设 \( f, g \) 在区间 \( I \) 上均为一致连续,问: 它们的线性组合 \( {af} + {bg} \) 和乘积 \( {fg} \) 在 \( I \) 上是否一致连续?

(2) 设 \( f \) 在区间 \( {I}_{1} \) 上一致连续, \( g \) 在区间 \( {I}_{2} \) 上一致连续,且区间 \( {I}_{2} \) 包含了 \( f \) 的值域，问:复合函数 \( g \circ  f \) 在区间 \( {I}_{1} \) 上是否一致连续？

4. 设 \( f \in  C\left( {-\infty , + \infty }\right) \) ,且为周期函数. 证明: \( f \) 在 \( \left( {-\infty , + \infty }\right) \) 上一致连续.

5. (1) 设 \( f \in  C\lbrack 0, + \infty ) \) ,且有 \( \mathop{\lim }\limits_{{x \rightarrow   + \infty }}\left\lbrack  {f\left( x\right)  - \left( {{ax} + b}\right) }\right\rbrack   = 0 \) ,证明 \( f \) 在 \( \lbrack 0, + \infty ) \) 上一致连续;

(2)若将(1)中的 \( {ax} + b \) 换成 \( a{x}^{2} + {bx} + c \) ，结论是否成立？

(3) 又若将 \( {ax} + b \) 换成某个函数 \( g\left( x\right) \) ,问: 当 \( g\left( x\right) \) 具有什么性质时 (1) 中的结论仍成立?

6. 证明: 当 \( n > 1 \) 时, \( {x}^{n} \) 在 \( \lbrack 0, + \infty ) \) 上不一致连续.

7. 证明: \( f\left( x\right)  = \ln x \) 在 \( \left( {1, + \infty }\right) \) 一致连续,但在 \( \left( {0,1}\right) \) 上不一致连续.

8. (1) 证明: 函数 \( f\left( x\right)  = \left| {\sin x}\right| /x \) 在区间 \( \left( {-1,0}\right) \) 和 \( \left( {0,1}\right) \) 均为一致连续,但在 \( \left( {-1,0}\right)  \cup  \left( {0,1}\right) \) 上不一致连续 (注意 \( \left( {-1,0}\right)  \cup  \left( {0,1}\right) \) 不是一个区间);

(2)若函数 \( f \) 在区间 \( \left( {a, b}\right) \) 和 \( \lbrack b, c) \) 上分别为一致连续，问: \( f \) 在 \( \left( {a, c}\right) \) 上是否一致连续?

9. 讨论以下函数在指定区间上是否一致连续 (可参考图 4.2):

(1) 在区间 \( \left( {0,1}\right) \) 上的函数 \( x\sin \frac{1}{x} \) ;

(2)在区间 \( \lbrack 0, + \infty ) \) 上的函数 \( \frac{\sin x}{x} \) ;

(3)在区间 \( \lbrack 0, + \infty ) \) 上的函数 \( x\sin x \) .
