## §3.4 Cauchy 收敛准则

#### 3.4.1 基本内容

Cauchy 收敛准则是数列收敛的充分必要条件, 其中的基本概念和结论如下:

1. 定义: 称数列 \( \left\{  {x}_{n}\right\} \) 为基本数列 (或 Cauchy 数列),如果对每个 \( \varepsilon  > 0 \) ,存在 \( N \) ,使得对每一对正整数 \( n, m > N \) ,成立 \( \left| {{a}_{n} - {a}_{m}}\right|  < \varepsilon \) .

2. 基本数列的另一个等价定义是: 对每个 \( \varepsilon  > 0 \) ,存在 \( N \) ,对每个正整数 \( n > N \) 和每个正整数 \( p \) ,成立 \( \left| {{a}_{n + p} - {a}_{n}}\right|  < \varepsilon \) .

3. 收敛数列一定是基本数列.

4. 基本数列一定是有界数列.

5. Cauchy 收敛准则: 收敛数列 \( \Leftrightarrow \) 基本数列.

6. Cauchy 收敛准则在有理数集 \( \mathbf{Q} \) 中不成立 (作为思考题).

## 7. 评注

(1) 与收敛数列的定义相比, Cauchy 收敛准则完全从数列本身出发, 不需要假定极限的存在, 这是一个很大的进步. 实际上, 只有很少的数列例子可以先猜出极限, 然后用定义 (与适当放大法) 验证它收敛.

(2) 在第二章中介绍了许多有关数列收敛的条件, 但都有很大的局限性. 在其中单调有界数列的收敛定理是数列收敛的充分条件, 在应用时也不需要知道极限, 但它当然依赖于单调性. 其他如夹逼定理是数列收敛的充分条件, 在应用时局限性更大. 数列有界当然是数列收敛的必要条件, 但只能用于在无界时判定数列发散. 有一个与子列有关的数列收敛的充分必要条件，即数列收敛等价于它的一切子列收敛. 由于数列也是自身的子列, 所以这个结论的充分性部分等于什么也没说.

(3)在一般意义上来说，Cauchy 收敛准则是研究数列收敛的最有力工具， 但理解和使用有一定困难. 为此需要学习较多的例题.

(4) 纵观数学分析的全部内容, 在包括积分与级数的许多类型的极限中, 都有相应的 Cauchy 收敛准则, 而且往往是其他收敛判别法的基础. 因此, 它具有其他基本定理所不能代替的独特作用.

#### 3.4.2 基本命题

命题 3.4.1 收敛数列一定是基本数列.

证 设 \( \left\{  {a}_{n}\right\} \) 收敛于 \( a \) ,则对 \( \varepsilon  > 0 \) ,存在 \( N \) ,当 \( n > N \) 时,成立 \( \left| {{a}_{n} - a}\right|  < \frac{\varepsilon }{2} \) . 因此当 \( n, m > N \) 时,就有不等式

\[
\left| {{a}_{n} - {a}_{m}}\right|  \leq  \left| {{a}_{n} - a}\right|  + \left| {a - {a}_{m}}\right|  < \frac{\varepsilon }{2} + \frac{\varepsilon }{2} = \varepsilon ,
\]

即 \( \left\{  {a}_{n}\right\} \) 为基本数列.

命题 3.4.2 基本数列一定有界.

证 设 \( \left\{  {a}_{n}\right\} \) 为基本数列. 对 \( \varepsilon  = 1 \) ,存在 \( N \) ,当 \( n, m > N \) 时,成立 \( \left| {{a}_{n} - {a}_{m}}\right|  < \) 1. 取定 \( m = N + 1 \) ,则当 \( n > N \) 时,就有 \( \left| {a}_{n}\right|  \leq  \left| {{a}_{n} - {a}_{N + 1}}\right|  + \left| {a}_{N + 1}\right|  < \left| {a}_{N + 1}\right|  + 1 \) . 因此得到

\[
\left| {a}_{n}\right|  \leq  M = \max \left\{  {\left| {a}_{1}\right| ,\left| {a}_{2}\right| ,\cdots ,\left| {a}_{N}\right| ,\left| {a}_{N + 1}\right|  + 1}\right\}  ,\forall n \in  {\mathbf{N}}_{ + }.
\]

以下给出 Cauchy 收敛准则的两个证明.

命题 3.4.3 (Cauchy 收敛准则) 数列收敛的充分必要条件是该数列为基本数列.

证 1 (用凝聚定理) 必要性部分已在命题 3.4.1 中得到证明, 这里只需证明收敛准则的充分性部分. 设 \( \left\{  {a}_{n}\right\} \) 是基本数列. 从命题 3.4.2 知道这个数列有界. 用凝聚定理,数列 \( \left\{  {a}_{n}\right\} \) 有一个收敛子列,记为 \( \left\{  {a}_{{n}_{k}}\right\} \) . 又记这个子列的极限为 \( a \) . 显然,只要证明数列 \( \left\{  {a}_{n}\right\} \) 收敛于 \( a \) .

由于 \( \left\{  {a}_{n}\right\} \) 是基本数列,对 \( \varepsilon  > 0 \) ,存在 \( N \) ,当 \( n, m > N \) 时,成立 \( \left| {{a}_{n} - {a}_{m}}\right|  < \varepsilon /2 \) . 又因子列 \( \left\{  {a}_{{n}_{k}}\right\} \) 的下标总有 \( {n}_{k} \geq  k \) ,因此当 \( k > N \) 时就有 \( {n}_{k} > N \) . 用 \( {n}_{k} \) 代替 \( m \) , 就在 \( n > N \) 和 \( k > N \) 时得到不等式 \( \left| {{a}_{n} - {a}_{{n}_{k}}}\right|  < \varepsilon /2 \) . 在其中令 \( k \rightarrow  \infty \) ,就得出

\[
\left| {{a}_{n} - a}\right|  \leq  \frac{\varepsilon }{2} < \varepsilon ,\forall n > N.
\]

证 2 (用三分法构造闭区间套 (见 [41] 的 120 页)) 只需证明充分性部分. 设 \( \left\{  {x}_{n}\right\} \) 为基本数列,因此有界. 从而有常数 \( {a}_{1},{b}_{1} \) ,满足条件 \( {a}_{1} \leq  {x}_{n} \leq  {b}_{1}, n \in  {\mathbf{N}}_{ + } \) .

将闭区间 \( \left\lbrack  {{a}_{1},{b}_{1}}\right\rbrack \) 三等分. 令 \( {c}_{1} = \left( {2{a}_{1} + {b}_{1}}\right) /3,{c}_{2} = \left( {{a}_{1} + 2{b}_{1}}\right) /3 \) ,得到三个长度相同的子区间 \( \left\lbrack  {{a}_{1},{c}_{1}}\right\rbrack  ,\left\lbrack  {{c}_{1},{c}_{2}}\right\rbrack \) 和 \( \left\lbrack  {{c}_{2},{b}_{1}}\right\rbrack \) ,分别记为 \( {J}_{1},{J}_{2} \) 和 \( {J}_{3} \) . 根据它们在实数轴上的左、中、右位置和基本数列的定义就可以发现: 在左边的 \( {J}_{1} \) 和右边的 \( {J}_{3} \) 中, 至少有一个子区间只含有数列 \( \left\{  {x}_{n}\right\} \) 中的有限多项.

这从几何上看是很直观的. 如果在 \( {J}_{1} \) 和 \( {J}_{3} \) 中都有数列中的无穷多项,则可以在 \( {J}_{1} \) 中取 \( {x}_{n} \) ,在 \( {J}_{3} \) 中取 \( {x}_{m} \) ,使得 \( n, m \) 都可以任意大,同时满足不等式

\[
\left| {{x}_{n} - {x}_{m}}\right|  \geq  \frac{b - a}{3}.
\]

这与 \( \left\{  {x}_{n}\right\} \) 为基本数列的条件矛盾.

于是可以从 \( \left\lbrack  {{a}_{1},{b}_{1}}\right\rbrack \) 中去掉只含有 \( \left\{  {x}_{n}\right\} \) 中有限多项的子区间 \( {J}_{1} \) 或 \( {J}_{3} \) (如果两个子区间都是如此则任去其一),将得到的区间记为 \( \left\lbrack  {{a}_{2},{b}_{2}}\right\rbrack \) .

重复这个过程,就得到一个闭区间套 \( \left\{  \left\lbrack  {{a}_{k},{b}_{k}}\right\rbrack  \right\} \) ,它具有两个特殊性质: (1) 闭区间套中的每个区间的长度是前一个区间长度的三分之二; (2) 每一个 \( \left\lbrack  {{a}_{k},{b}_{k}}\right\rbrack \) 中含有数列 \( \left\{  {x}_{n}\right\} \) 从某项起的所有项. 性质 (1) 保证存在 \( \xi \) ,使得闭区间套的端点序列 \( \left\{  {a}_{k}\right\} \) 和 \( \left\{  {b}_{k}\right\} \) 从两侧分别单调地收敛于 \( \xi \) ,即有 \( \mathop{\lim }\limits_{{k \rightarrow  \infty }}{a}_{k} = \mathop{\lim }\limits_{{k \rightarrow  \infty }}{b}_{k} = \xi \) .

现在我们证明: 这个 \( \xi \) 就是基本数列 \( \left\{  {x}_{n}\right\} \) 的极限. 对给定的 \( \varepsilon  > 0 \) ,有 \( N \) ,使得 \( {a}_{N} \) 和 \( {b}_{N} \) 进入点 \( \xi \) 的 \( \varepsilon \) 邻域,也就是说有 \( \left\lbrack  {{a}_{N},{b}_{N}}\right\rbrack   \subset  \left( {\xi  - \varepsilon ,\xi  + \varepsilon }\right) \) . 由于闭区间 \( \left\lbrack  {{a}_{N},{b}_{N}}\right\rbrack \) 又具有性质 \( \left( 2\right) \) ,即含有数列 \( \left\{  {x}_{n}\right\} \) 中从某项之后的全部项,因此存在 \( {N}_{1} \) , 使得当 \( n > {N}_{1} \) 时,成立不等式 \( \left| {{x}_{n} - \xi }\right|  < \varepsilon \) .

注 本题也可以用例题 3.2.2 中的二分法来证明, 甚至可能更为简单. 请读者试之, 并与上面的三分法比较它们的异同之处. 注意基本数列的条件分别用于何处.

#### 3.4.3 例题

例题 3.4.1 设数列 \( \left\{  {b}_{n}\right\} \) 有界,令 \( {a}_{n} = \frac{{b}_{1}}{1 \cdot  2} + \frac{{b}_{2}}{2 \cdot  3} + \cdots  + \frac{{b}_{n}}{n\left( {n + 1}\right) }, n \in  {\mathbf{N}}_{ + } \) , 证明数列 \( \left\{  {a}_{n}\right\} \) 收敛.

证 取常数 \( M > 0 \) ,使得 \( \left| {b}_{n}\right|  \leq  M, n \in  {\mathbf{N}}_{ + } \) . 然后对任意 \( p \in  {\mathbf{N}}_{ + } \) 作估计:

\[
\left| {{a}_{n + p} - {a}_{n}}\right|  \leq  M\left\lbrack  {\frac{1}{\left( {n + 1}\right) \left( {n + 2}\right) } + \frac{1}{\left( {n + 2}\right) \left( {n + 3}\right) } + \cdots  + \frac{1}{\left( {n + p}\right) \left( {n + p + 1}\right) }}\right\rbrack
\]

\[
= M\left\lbrack  {\left( {\frac{1}{n + 1} - \frac{1}{n + 2}}\right)  + \cdots  + \left( {\frac{1}{n + p} - \frac{1}{n + p + 1}}\right) }\right\rbrack
\]

\[
= M\left( {\frac{1}{n + 1} - \frac{1}{n + p + 1}}\right)  < \frac{M}{n + 1}.
\]

因此对 \( \varepsilon  > 0 \) ,取 \( N = \left\lbrack  {M/\varepsilon }\right\rbrack \) ,就可使 \( n > N \) 和 \( p \in  {\mathbf{N}}_{ + } \) 时,成立 \( \left| {{a}_{n + p} - {a}_{n}}\right|  < \varepsilon \) . 这样就证明了 \( \left\{  {a}_{n}\right\} \) 是基本数列. 根据 Cauchy 收敛准则知道 \( \left\{  {a}_{n}\right\} \) 收敛.

注 由于 \( \left\{  {b}_{n}\right\} \) 除了有界性之外没有任何其他已知性质,因此 \( \left\{  {a}_{n}\right\} \) 谈不上有单调性, 从而第二章的主要方法, 即单调有界数列的收敛定理, 在这里完全失效. 可见 Cauchy 收敛准则是一个非常有力的工具.

下一个例题在第二章中已经有了 3 个证明 (见第二章例题 2.2.6). 现用本节的 Cauchy 收敛准则给出新的证明, 但也可以说是那里的第二个证明的改写:

例题 3.4.2 设 \( {S}_{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots  + \frac{1}{n}, n \in  {\mathbf{N}}_{ + } \) ,证明 \( \left\{  {S}_{n}\right\} \) 发散.

证 写出

\[
{S}_{2n} - {S}_{n} = \frac{1}{n + 1} + \frac{1}{n + 2} + \cdots  + \frac{1}{2n} \geq  n \cdot  \frac{1}{2n} = \frac{1}{2},
\]

可见对 \( \varepsilon  = \frac{1}{2} \) 和任意 \( N \) ,在 \( n, m > N \) 时,只要取 \( m = {2n} \) ,不等式 \( \left| {{S}_{n} - {S}_{m}}\right|  < \frac{1}{2} \) 就不可能成立. 这表明数列 \( \left\{  {S}_{n}\right\} \) 不是基本数列,因此发散.

同样, 对于例题 2.2.7, 可以用 Cauchy 收敛准则写出新的证明.

例题 3.4.3 证明数列 \( \{ \sin n\} \) 发散.

证 这个证明与例题 2.2.7 中的 (以几何观察为基础的) 第一个证明类似. 从那里的图 2.2 可见,对每个 \( k \in  {\mathbf{N}}_{ + } \) ,可以找到正整数 \( {n}_{k}^{\prime } \) 和 \( {n}_{k}^{\prime \prime } \) ,使 \( \sin {n}_{k}^{\prime } \geq  \sqrt{2}/2 \) , \( \sin {n}_{k}^{\prime \prime } \leq  0 \) . 因此, \( \sin {n}_{k}^{\prime } - \sin {n}_{k}^{\prime \prime } > 0 \) .5 . 由于 \( {n}_{k}^{\prime } \) 和 \( {n}_{k}^{\prime \prime } \) 可任意大,因此 \( \{ \sin n\} \) 不可能是基本数列, 根据 Cauchy 收敛准则知道它一定是发散数列.

#### 3.4.4 压缩映射原理

在第一章中介绍了用于迭代生成数列的几何方法. 应当指出, 这个方法完全依赖于实数的有序性 (即在实数轴上点有序), 也就是说它只能用于一维问题. 本节要介绍的压缩映射原理以 Cauchy 收敛准则为基础, 它在处理迭代生成数列时很有效, 而且可以推广到多维甚至无穷维的问题上去. 当然, 压缩映射原理在本质上是局部性结果, 对于大范围的非线性问题一般无效.

压缩映射的定义 设函数 \( f \) 在区间 \( \left\lbrack  {a, b}\right\rbrack \) 上定义, \( f\left( \left\lbrack  {a, b}\right\rbrack  \right)  \subset  \left\lbrack  {a, b}\right\rbrack \) ,并存在一个常数 \( k \) ,满足 \( 0 < k < 1 \) ,使得对一切 \( x, y \in  \left\lbrack  {a, b}\right\rbrack \) 成立不等式 \( \left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  k\left| {x - y}\right| \) , 则称 \( f \) 是 \( \left\lbrack  {a, b}\right\rbrack \) 上的一个压缩映射,称常数 \( k \) 为压缩常数.

命题 3.4.4 (压缩映射原理) 设 \( f \) 是 \( \left\lbrack  {a, b}\right\rbrack \) 上的一个压缩映射,则

(1) \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 中存在唯一的不动点 \( \xi  = f\left( \xi \right) \) ;

(2) 由任何初始值 \( {a}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) 和递推公式 \( {a}_{n + 1} = f\left( {a}_{n}\right) , n \in  {\mathbf{N}}_{ + } \) 生成的数列 \( \left\{  {a}_{n}\right\} \) 一定收敛于 \( \xi \) ；

(3)成立估计式 \( \left| {{a}_{n} - \xi }\right|  \leq  \frac{k}{1 - k}\left| {{a}_{n} - {a}_{n - 1}}\right| \) 和 \( \left| {{a}_{n} - \xi }\right|  \leq  \frac{{k}^{n}}{1 - k}\left| {{a}_{1} - {a}_{0}}\right| \) (即事后估计与先验估计).

证 (注意在这个证明中不需要函数 \( f \) 的连续性概念.) 由于 \( f\left( \left\lbrack  {a, b}\right\rbrack  \right)  \subset  \left\lbrack  {a, b}\right\rbrack \) , 因此 \( \left\{  {a}_{n}\right\} \) 必在 \( \left\lbrack  {a, b}\right\rbrack \) 中. 根据 Cauchy 收敛准则估计

\[
\left| {{a}_{n} - {a}_{n + p}}\right|  \leq  k\left| {{a}_{n - 1} - {a}_{n + p - 1}}\right|  \leq  {k}^{2}\left| {{a}_{n - 2} - {a}_{n + p - 2}}\right|
\]

\[
\leq  \cdots  \leq  {k}^{n}\left| {{a}_{0} - {a}_{p}}\right|  \leq  {k}^{n}\left( {b - a}\right) .
\]

可见对 \( \varepsilon  > 0 \) ,只要取 \( N = \left\lbrack  {\ln \left( {\varepsilon /\left( {b - a}\right) }\right) /\ln k}\right\rbrack \) ,当 \( n > N \) 和 \( p \in  {\mathbf{N}}_{ + } \) 时,就有 \( \left| {{a}_{n} - {a}_{n + p}}\right|  < \varepsilon \) . 因此 \( \left\{  {a}_{n}\right\} \) 是基本数列,从而收敛. 记其极限为 \( \xi  \in  \left\lbrack  {a, b}\right\rbrack \) . 为了证明这个 \( \xi \) 是 \( f \) 的不动点,需要研究第二个数列 \( \left\{  {f\left( {a}_{n}\right) }\right\} \) . 从不等式 \( \left| {f\left( {a}_{n}\right)  - f\left( \xi \right) }\right|  \leq \; k\left| {{a}_{n} - \xi }\right| \) 和 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} = \xi \) 可见,数列 \( \left\{  {f\left( {a}_{n}\right) }\right\} \) 收敛于 \( f\left( \xi \right) \) .

在 \( {a}_{n + 1} = f\left( {a}_{n}\right) \) 两边令 \( n \rightarrow  \infty \) ,就得到 \( \xi  = f\left( \xi \right) \) . 因此 \( \xi \) 是 \( f \) 的不动点.

如果 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 内还有不动点 \( \eta \) ,即 \( \eta  = f\left( \eta \right) \) ,则就有 \( \left| {\xi  - \eta }\right|  = \left| {f\left( \xi \right)  - f\left( \eta \right) }\right|  \leq \; k\left| {\xi  - \eta }\right| \) . 由于 \( 0 < k < 1 \) ,只能有 \( \xi  = \eta \) . 因此 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 内的不动点是唯一的. 这样就证明了命题的 (1) 和 (2).

命题之 (3) 的前一式可从估计式

\[
\left| {{a}_{n} - \xi }\right|  = \left| {f\left( {a}_{n - 1}\right)  - f\left( \xi \right) }\right|  \leq  k\left| {{a}_{n - 1} - \xi }\right|  \leq  k\left( {\left| {{a}_{n - 1} - {a}_{n}}\right|  + \left| {{a}_{n} - \xi }\right| }\right)
\]

得到:

\[
\left| {{a}_{n} - \xi }\right|  \leq  \frac{k}{1 - k}\left| {{a}_{n} - {a}_{n - 1}}\right| .
\]

又由上式出发,利用 \( \left| {{a}_{j} - {a}_{j - 1}}\right|  \leq  k\left| {{a}_{j - 1} - {a}_{j - 2}}\right| \) 就可以如下得到 (3) 的后一式:

\[
\left| {{a}_{n} - \xi }\right|  \leq  \frac{{k}^{2}}{1 - k}\left| {{a}_{n - 1} - {a}_{n - 2}}\right|  \leq  \cdots  \leq  \frac{{k}^{n}}{1 - k}\left| {{a}_{1} - {a}_{0}}\right| .
\]

注 在 (3) 中的两个不等式在实际计算中很有用处. 前一个不等式可以从相继的两次计算估计当前误差, 称为事后估计; 后一个不等式比前一个要粗一些, 但可以用于在计算之前估计要迭代多少次才能达到所要的精度, 称为先验估计.

下面介绍如何将压缩映射原理用于 §2.6 中的两个典型例题. 它们的解法和那里完全不同.

例题 3.4.4 设 \( {a}_{1} = \sqrt{2},{a}_{n + 1} = \sqrt{2 + {a}_{n}}, n \in  {\mathbf{N}}_{ + } \) . 讨论数列 \( \left\{  {a}_{n}\right\} \) 的敛散性, 若收敛则求出其极限.

解 这时 \( f\left( x\right)  = \sqrt{2 + x} \) . 取闭区间 \( \left\lbrack  {0,2}\right\rbrack \) ,则可实现 \( f\left( \left\lbrack  {0,2}\right\rbrack  \right)  \subset  \left\lbrack  {0,2}\right\rbrack \) . 从

\[
\left| {f\left( x\right)  - f\left( y\right) }\right|  = \left| {\sqrt{2 + x} - \sqrt{2 + y}}\right|  = \frac{\left| x - y\right| }{\sqrt{2 + x} + \sqrt{2 + y}}
\]

知道可取 \( k = 1/\left( {2\sqrt{2}}\right) \) 为压缩常数. 于是数列 \( \left\{  {a}_{n}\right\} \) 的收敛性已为压缩映射原理所保证,而且极限是 \( f \) 在 \( \left\lbrack  {0,2}\right\rbrack \) 内的唯一不动点 2 .

例题 3.4.5 数列 \( \left\{  {b}_{n}\right\} \) 由 \( {b}_{1} = 1 \) 和 \( {b}_{n + 1} = 1 + \frac{1}{{b}_{n}}\left( {n \in  {\mathbf{N}}_{ + }}\right) \) 生成. 讨论数列 \( \left\{  {b}_{n}\right\} \) 的敛散性,若收敛则求出其极限.

解 这里的函数 \( f\left( x\right)  = 1 + \frac{1}{x} \) . 观察

\[
\left| {f\left( x\right)  - f\left( y\right) }\right|  = \left| {\frac{1}{x} - \frac{1}{y}}\right|  = \frac{\left| x - y\right| }{\left| xy\right| },
\]

并考虑如何选择区间. 这里要利用函数 \( f \) 在 \( x > 0 \) 时单调减少,以及数列的前几项 \( {b}_{1} = 1,{b}_{2} = 2,{b}_{3} = {1.5},\cdots \) . 如果用以 \( {b}_{1} = 1 \) 和 \( {b}_{2} = 2 \) 为端点的闭区间 \( \left\lbrack  {1,2}\right\rbrack \) ,则可以实现 \( f\left( \left\lbrack  {1,2}\right\rbrack  \right)  = \left\lbrack  {{1.5},2}\right\rbrack   \subset  \left\lbrack  {1,2}\right\rbrack \) . 但在这个区间 \( \left\lbrack  {1,2}\right\rbrack \) 上不能取到在 0 和 1 之间的压缩常数. 再尝试以 \( {b}_{2} = 2 \) 和 \( {b}_{3} = {1.5} \) 为端点的区间 \( \left\lbrack  {{1.5},2}\right\rbrack \) ,发现有 \( f\left( \left\lbrack  {{1.5},2}\right\rbrack  \right)  \subset  \left\lbrack  {{1.5},2}\right\rbrack \) ,同时可以估计出

\[
\left| {f\left( x\right)  - f\left( y\right) }\right|  = \frac{\left| x - y\right| }{\left| xy\right| } \leq  \frac{1}{{1.5}^{2}}\left| {x - y}\right|  = \frac{4}{9}\left| {x - y}\right| ,\forall x, y \in  \left\lbrack  {{1.5},2}\right\rbrack  .
\]

由于数列 \( \left\{  {b}_{n}\right\} \) 从第二项起就进入 \( \left\lbrack  {{1.5},2}\right\rbrack \) ,因此由压缩映射原理保证了它的收敛性. 极限就是 \( f \) 在 \( x > 0 \) 中的唯一不动点 \( b = \left( {1 + \sqrt{5}}\right) /2 \) .

注 以上两个例题的解法都是去验证压缩映射原理的条件满足. 但实际上往往可以直接应用原理中的思想方法. 例如,在例题 3.4.5 中可以先证明从 \( n = 2 \) 起, \( {b}_{n} \in  \left\lbrack  {{1.5},2}\right\rbrack \) 成立. 然后得到 (利用公式 (2.17))

\[
\left| {{b}_{n + 2} - b}\right|  = \left| \frac{{b}_{n} - b}{\left( {{b}_{n} + 1}\right) \left( {b + 1}\right) }\right|  \leq  \frac{4}{25}\left| {{b}_{n} - b}\right| ,
\]

从而有 \( \left| {{b}_{2k} - b}\right|  \leq  \left| {{b}_{2} - b}\right|  \cdot  {\left( \frac{4}{25}\right) }^{k - 1} \) ,即知道 \( \left\{  {b}_{2k}\right\} \) 收敛于 \( b \) . 同理可证 \( \left\{  {b}_{{2k} - 1}\right\} \) 也收敛于 \( b \) .

#### 3.4.5 练习题

1. 满足以下条件的数列 \( \left\{  {x}_{n}\right\} \) 是否一定是基本数列? 若回答“是”,请作出证明; 若回答“不一定是”,请举出反例:

(1) 对每个 \( \varepsilon  > 0 \) ,存在 \( N \) ,当 \( n > N \) 时,成立 \( \left| {{x}_{n} - {x}_{N}}\right|  < \varepsilon \) ;

(2)对所有 \( n, p \in  {\mathbf{N}}_{ + } \) ，成立不等式 \( \left| {{x}_{n + p} - {x}_{n}}\right|  \leq  p/n \) ；

(3) 对所有 \( n, p \in  {\mathbf{N}}_{ + } \) ,成立不等式 \( \left| {{x}_{n + p} - {x}_{n}}\right|  \leq  p/{n}^{2} \) ;

(4) 对每个正整数 \( p \) ,成立 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{x}_{n} - {x}_{n + p}}\right)  = 0 \) .

2. 用对偶法则于数列收敛的 Cauchy 收敛准则, 以正面方式写出数列发散的充分必要条件.

3. 证明下列数列为基本数列, 因此都是收敛数列:

(1) \( {a}_{n} = 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{n!}, n \in  {\mathbf{N}}_{ + } \) ;

(2) \( {b}_{n} = 1 - \frac{1}{2} + \frac{1}{3} - \cdots  + {\left( -1\right) }^{n - 1}\frac{1}{n}, n \in  {\mathbf{N}}_{ + } \) ;

(3) \( {c}_{n} = \frac{\sin {2x}}{2\left( {2 + \sin {2x}}\right) } + \frac{\sin {3x}}{3\left( {3 + \sin {3x}}\right) } + \cdots  + \frac{\sin {nx}}{n\left( {n + \sin {nx}}\right) }, n \in  {\mathbf{N}}_{ + } \) .

4. 设 \( {a}_{n} = \sin 1 + \frac{\sin 2}{2!} + \cdots  + \frac{\sin n}{n!}, n \in  {\mathbf{N}}_{ + } \) ,证明:

(1)数列 \( \left\{  {a}_{n}\right\} \) 有界，但不单调；(2) \( \left\{  {a}_{n}\right\} \) 收敛.

5. 设从某个数列 \( \left\{  {a}_{n}\right\} \) 定义 \( {x}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k},{y}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}\left| {a}_{k}\right| , n \in  {\mathbf{N}}_{ + } \) ,若数列 \( \left\{  {y}_{n}\right\} \) 收敛, 证明数列 \( \left\{  {x}_{n}\right\} \) 也收敛.

(本题可以看成是上一题和例题 3.4.1 的推广.)

6. 设 \( {S}_{n} = 1 + \frac{1}{{2}^{p}} + \frac{1}{{3}^{p}} + \cdots  + \frac{1}{{n}^{p}}, n \in  {\mathbf{N}}_{ + } \) ,其中 \( p \leq  1 \) ,证明 \( \left\{  {S}_{n}\right\} \) 发散.

7. 天文学中的 Kepler (开普勒) 方程 \( x - q\sin x = a\left( {0 < q < 1}\right) \) 是一个超越方程, 没有求根公式 (见 [15] 的 22 和 72 页). 求近似解的一个方法是通过迭代. 取定 \( {x}_{1} \) ,然后用递推公式 \( {x}_{n + 1} = q\sin {x}_{n} + a, n \in  {\mathbf{N}}_{ + } \) . 证明这个方法的正确性.

(这个方程是 Kepler 在 1609 年左右研究行星运动规律时得到的方程. 从天体力学的角度来分析可以肯定, 对每个给定的 a, 方程存在唯一解. 这个解没有可用的显式表达式, 但可以用近似方法求解. 本题就是用迭代生成数列的方法求近似解. 在 [14] 第二卷的 452 小节有解的无穷级数表达式.)
