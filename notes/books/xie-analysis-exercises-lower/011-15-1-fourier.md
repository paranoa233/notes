## §15.1 Fourier 系数

Fourier 级数是一类特殊的三角级数, 它的特殊性在于其系数是从某个可积函数出发经过 Euler-Fourier 公式计算出来的.

#### 15.1.1 Fourier 系数的计算公式

设 \( f \) 是以 \( {2\pi } \) 为周期的函数且在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积. (若 \( f \) 为常义可积, 则可积蕴含绝对可积,又若 \( f \) 为广义可积,则绝对可积蕴含可积.)

计算 \( f \) 的 Fourier 系数的 Euler-Fourier 公式是:

\[
{a}_{n} = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( x\right) \cos {nx}\mathrm{\;d}x, n = 0,1,2,\cdots ; \tag{15.1}
\]

\[
{b}_{n} = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x, n = 1,2,\cdots . \tag{15.2}
\]

如果三角级数 \( \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) 中的系数满足公式 (15.1) 和 (15.2),则称该三角级数是 \( f \) 的 Fourier 级数,记为

\[
f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) . \tag{15.3}
\]

注意: 上述公式只表明右边的系数 \( {a}_{n},{b}_{n} \) 与左边的函数 \( f \) 之间满足公式 (15.1) 和 (15.2). 记号 “ \( \sim \) ” 没有其他含义,公式 (15.3) 右边的级数是否收敛,以及在收敛时其和函数是否等于 \( f \) ,都是需要另行讨论的问题.

回顾教科书中导出 Euler-Fourier 公式的过程,其出发点是在 \( \left( {-\infty , + \infty }\right) \) 上一致收敛(也就是在一个周期长度的闭区间上一致收敛)的一个三角级数，然后通过逐项求积导出上述公式. 由此就得到 Fourier 级数学习中的第一个基本定理 (其中对一致收敛的范围理解如上):

命题 15.1.1 一致收敛的三角级数必是其和函数的 Fourier 级数.

虽然用 Euler-Fourier 公式得到的 Fourier 级数未必一致收敛，但这个命题仍然是很有用的一个基本结果.

注 1 虽然只有周期函数才可能有 Fourier 级数,但当 \( f \) 的定义域是某个长度为 \( {2\pi } \) 的区间时，可先将其延拓成周期函数，且把延拓后的周期函数的 Fourier 级数称为 \( f \) 在该区间上的 Fourier 级数. 对于周期不是 \( {2\pi } \) 的周期函数或只在长度不是 \( {2\pi } \) 的区间上定义的函数,也可用类似的方法定义它们的 Fourier 级数.

注 2 当 \( f \) 为偶函数或奇函数时, \( f \) 的 Fourier 级数有较为简单的形式: 当 \( f \) 为偶函数时,所有的 \( {b}_{n} \) 均为 0,并且 (15.1) 成为

\[
{a}_{n} = \frac{2}{\pi }{\int }_{0}^{\pi }f\left( x\right) \cos {nx}\mathrm{\;d}x, n = 0,1,2,\cdots , \tag{15.4}
\]

当 \( f \) 为奇函数时,所有的 \( {a}_{n} \) 均为 0,并且 (15.2) 成为

\[
{b}_{n} = \frac{2}{\pi }{\int }_{0}^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x, n = 1,2,\cdots . \tag{15.5}
\]

这时 \( f \) 的 Fourier 级数中只出现含有余弦函数的项与常数项或只出现含有正弦函数的项, 分别称为余弦级数或正弦级数.

注 3 从公式 (15.4) 不难看出,如果 \( f \) 在 \( \left\lbrack  {0,\pi }\right\rbrack \) 上具有某种对称性,例如关于点 \( \left( {\frac{\pi }{2},0}\right) \) 为偶函数 (奇函数),则可以证明在公式 (15.4) 中当 \( n \) 为奇数 (偶数) 时积分为 0 . 对于公式 (15.5) 有类似的结论 (参见上册 10.4.3 小节中的命题和例题).

下一个命题建立 \( f \) 的 Fourier 系数与其导函数 \( {f}^{\prime } \) 的 Fourier 系数之间的联系. 这也是 Fourier 系数的基本性质之一.

命题 15.1.2 设以 \( {2\pi } \) 为周期的连续函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上除了有限个点以外可导,又设 (在任意补充有限个点上的值之后) \( {f}^{\prime } \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,则从 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) 就有

\[
{f}^{\prime }\left( x\right)  \sim  {\left( \frac{{a}_{0}}{2}\right) }^{\prime } + \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( {a}_{n}\cos nx + {b}_{n}\sin nx\right) }^{\prime }
\]

\[
= \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {n{b}_{n}\cos {nx} - n{a}_{n}\sin {nx}}\right) .
\]

若用 \( {a}_{n}^{\prime },{b}_{n}^{\prime } \) 记 \( {f}^{\prime } \) 的 Fourier 系数,这就等价于

\[
{a}_{0}^{\prime } = 0,{a}_{n}^{\prime } = n{b}_{n},{b}_{n}^{\prime } =  - n{a}_{n}, n = 1,2,\cdots . \tag{15.6}
\]

证 因为 \( f \) 是以 \( {2\pi } \) 为周期的连续函数,因此 \( f\left( {-\pi }\right)  = f\left( \pi \right) \) ,由此即可推出 \( {a}_{0}^{\prime } = 0 \) . 然后由分部积分公式 \( {}^{\text{ ① }} \) 可得

\[
\pi {a}_{n}^{\prime } = {\int }_{-\pi }^{\pi }{f}^{\prime }\left( x\right) \cos {nx}\mathrm{\;d}x = {\left. f\left( x\right) \cos nx\right| }_{-\pi }^{\pi } - {\int }_{-\pi }^{\pi }f\left( x\right) \mathrm{d}\cos {nx}
\]

\[
= n{\int }_{-\pi }^{\pi }f\left( x\right) \sin {nx}\mathrm{\;d}x = {n\pi }{b}_{n}.
\]

这就是 \( {b}_{n} = \frac{{a}_{n}^{\prime }}{n} \) . 类似地可以证明 \( {a}_{n} =  - \frac{{b}_{n}^{\prime }}{n} \) .

---

① 这里需要将上册 319 页的分部积分公式 (10.11) 稍作推广, 并参见上册 315 页注 2.

---

注 对于满足条件的 \( f \) ,公式 (15.6) 可以用于从 \( f \) 的 Fourier 系数得到 \( {f}^{\prime } \) 的 Fourier 系数. 这里只需要形式上的“逐项求导”即可.

反之,能否从 \( {f}^{\prime } \) 的 Fourier 系数得到 \( f \) 的 Fourier 系数? 从命题的证明可知, 如果 \( f \in  C\left\lbrack  {-\pi ,\pi }\right\rbrack \) 但不满足 \( f\left( \pi \right)  = f\left( {-\pi }\right) \) ,则肯定不行. 这时 \( {a}_{0}^{\prime } \neq  0 \) . 但是有一个方法可以解决这个问题. 这就是将 \( f \) 写成

\[
f\left( x\right)  = \left\lbrack  {f\left( x\right)  - \frac{{a}_{0}^{\prime }}{2}x}\right\rbrack   + \frac{{a}_{0}^{\prime }}{2}x, \tag{15.7}
\]

这时右边第一项满足命题中的条件,其导函数为 \( {f}^{\prime }\left( x\right)  - {a}_{0}^{\prime }/2 \) ,因此可用 (15.6). 至于右边的第二项，则可直接计算它的 Fourier 系数. 最后将两个结果合并. 当然 \( f \) 的 Fourier 系数 \( {a}_{0} \) 需要直接计算得到 (见后面的例题 15.1.2 之解 2).

#### 15.1.2 Fourier 系数的渐近性质

由 Riemann 引理 (上册的例题 10.2.6) 就得到这方面的第一个性质:

命题 15.1.3 若 \( f \) 为周期 \( {2\pi } \) 的可积和绝对可积函数,则其 Fourier 系数 \( \left\{  {a}_{n}\right\} \) 和 \( \left\{  {b}_{n}\right\} \) 必为无穷小量: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{b}_{n} = 0 \) .

利用命题 15.1.2 可知在 \( f \) 的可导性与其 Fourier 系数的渐近性态之间的联系:

命题 15.1.4 设以 \( {2\pi } \) 为周期的函数 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上除了有限个点以外均有 \( k + 1 \) 阶导数. 如果其 \( k \) 阶导函数 \( {f}^{\left( k\right) } \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上处处连续且 \( {f}^{\left( k + 1\right) } \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积, 则有

\[
{a}_{n} = o\left( \frac{1}{{n}^{k + 1}}\right) ,{b}_{n} = o\left( \frac{1}{{n}^{k + 1}}\right) .
\]

命题 15.1.5 设 \( f \) 是以 \( {2\pi } \) 为周期的函数且存在 \( \alpha  \in  (0,1\rbrack \) ,使 \( f \) 满足 \( \alpha \) 阶 Lipschitz 条件:

\[
\left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  L{\left| x - y\right| }^{\alpha },
\]

其中 \( L \) 为常数 \( {}^{\text{ ① }} \) ,则成立:

\[
{a}_{n} = O\left( \frac{1}{{n}^{\alpha }}\right) ,{b}_{n} = O\left( \frac{1}{{n}^{\alpha }}\right) .
\]

证 由本题的条件知, \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上连续,因此其 Fourier 系数存在. 在 Fourier 系数公式

\[
{a}_{n} = \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( x\right) \cos {nx}\mathrm{\;d}x \tag{15.8}
\]

中令 \( x = t + \frac{\pi }{n} \) ,可得

\[
{a}_{n} = \frac{1}{\pi }{\int }_{-\pi  - \frac{\pi }{n}}^{\pi  - \frac{\pi }{n}}f\left( {t + \frac{\pi }{n}}\right) \cos \left( {{nt} + \pi }\right) \mathrm{d}t =  - \frac{1}{\pi }{\int }_{-\pi }^{\pi }f\left( {t + \frac{\pi }{n}}\right) \cos {nt}\mathrm{\;d}t.
\]

---

① \( \alpha  > 1 \) 是没有意义的，见上册 153 页题 10.

---

将上式与 (15.8) 取平均得到 \( {a}_{n} = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left\lbrack  {f\left( x\right)  - f\left( {x + \frac{\pi }{n}}\right) }\right\rbrack  \cos {nx}\mathrm{\;d}x \) . 然后可以估计如下:

\[
\left| {a}_{n}\right|  \leq  \frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left| {f\left( x\right)  - f\left( {x + \frac{\pi }{n}}\right) }\right|  \cdot  \left| {\cos {nx}}\right| \mathrm{d}x
\]

\[
\leq  \frac{1}{2\pi }L{\left( \frac{\pi }{n}\right) }^{\alpha }{\int }_{-\pi }^{\pi }\left| {\cos {nx}}\right| \mathrm{d}x \leq  L{\left( \frac{\pi }{n}\right) }^{\alpha }.
\]

这就证明了 \( {a}_{n} = O\left( \frac{1}{{n}^{\alpha }}\right) \) . 类似地可证明 \( {b}_{n} = O\left( \frac{1}{{n}^{\alpha }}\right) \) .

#### 15.1.3 Fourier 系数的几何意义

初学者一定会感到奇怪, Fourier 系数的计算公式 (15.1), (15.2) 完全是积分运算, 怎么会有什么几何意义?

实际上这里的几何意义是人们的一种想像或者一种类比, 即将满足一定条件的函数集合想像为空间, 并将几何学中的正交 (即垂直) 概念推广到函数之间. 泛函分析等学科的发展充分证明这种方法具有极强的生命力. 对于 Fourier 级数来说, 这种观点也是非常本质的. 本小节就是要用几何观点来解释 Fourier 系数和 Fourier 级数的意义.

这里的函数空间是周期 \( {2\pi } \) 的可积和绝对可积函数集合,其中有函数之间相加以及函数与实数的乘法. 按照线性代数这就是一个线性空间或向量空间.

然后在这个空间中引进正交概念. 考虑空间中的两个函数 \( f \) 与 \( g \) ,如果有

\[
{\int }_{-\pi }^{\pi }f\left( x\right) g\left( x\right) \mathrm{d}x = 0,
\]

就称 \( f \) 和 \( g \) 正交. 在这个定义下,三角函数系

\[
1,\cos x,\sin x,\cos {2x},\sin {2x},\cdots ,\cos {nx},\sin {nx},\cdots
\]

中任何两个函数正交, 因此称为正交函数系.

现在考虑用三角多项式

\[
{T}_{n}\left( x\right)  = \frac{{A}_{0}}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{A}_{k}\cos {kx} + {B}_{k}\sin {kx}}\right) \tag{15.9}
\]

来逼近函数 \( f \) ,其中的逼近误差,也就是 \( {T}_{n} \) 与 \( f \) 之间的距离,是按照平方平均意义来定义的:

\[
{d}^{2}\left( {f,{T}_{n}}\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\left\lbrack  f\left( x\right)  - {T}_{n}\left( x\right) \right\rbrack  }^{2}\mathrm{\;d}x. \tag{15.10}
\]

这时就可以证明下列结论.

命题 15.1.6 (Fourier 系数的最优性) 设 \( f \) 是区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上的可积和平方可积函数 \( {}^{\text{ ①, }}{T}_{n}\left( x\right) \) 是 (15.9) 中的任意 \( n \) 次三角多项式, \( {S}_{n}\left( x\right) \) 是 \( f \) 的 Fourier 级数 (15.3) 的部分和函数

\[
{S}_{n}\left( x\right)  = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) ,
\]

则有

\[
{d}^{2}\left( {f,{S}_{n}}\right)  \leq  {d}^{2}\left( {f,{T}_{n}}\right)
\]

其中成立等号当且仅当 \( {A}_{0} = {a}_{0},{A}_{k} = {a}_{k},{B}_{k} = {b}_{k}, k = 1,2,\cdots , n \) .

证 直接按照定义 (15.10) 计算并作配方得到

\[
{2\pi }{d}^{2}\left( {f,{T}_{n}}\right)  = {\int }_{-\pi }^{\pi }{f}^{2} - \pi {a}_{0}{A}_{0} - {2\pi }\mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}{A}_{k} + {b}_{k}{B}_{k}}\right)  + \frac{\pi {A}_{0}^{2}}{2} + \pi \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{A}_{k}^{2} + {B}_{k}^{2}}\right)
\]

\[
= {\int }_{-\pi }^{\pi }{f}^{2} - \frac{\pi {a}_{0}^{2}}{2} - \pi \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}^{2} + {b}_{k}^{2}}\right)
\]

\[
+ \pi \left\{  {\frac{{\left( {A}_{0} - {a}_{0}\right) }^{2}}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\left\lbrack  {{\left( {A}_{k} - {a}_{k}\right) }^{2} + {\left( {B}_{k} - {b}_{k}\right) }^{2}}\right\rbrack  }\right\}
\]

\[
\geq  {\int }_{-\pi }^{\pi }{f}^{2} - \frac{\pi {a}_{0}^{2}}{2} - \pi \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}^{2} + {b}_{k}^{2}}\right)  = {2\pi }{d}^{2}\left( {f,{S}_{n}}\right) .
\]

注 在右边的图 15.1 中作出了命题的几何意义的示意图. 如果考虑由所有 \( {T}_{n} \) 构成的集合,问题就是要从中找出与 \( f \) 距离最小的一个三角多项式. 这个问题的解就是 \( {S}_{n} \) . 其原因在于, Euler-Fourier 公式在几何上就是 \( f \) 到三角函数系的正交投影, 而 \( {S}_{n} \) 就是 \( f \) 到所有 \( {T}_{n} \) 的集合上的正交投影,因此 \( {S}_{n} \) 到 \( f \) 的距离最短.

![bo_d7fsu8491nqc7381io7g_94_852_1354_570_308_0.jpg](images/xie_analysis_exercises_lower_040_bod7fsu8491nqc7381io7g9485213545703080.jpg)

图 15.1

由命题 15.1.6 还可以得到

命题 15.1.7 (Bessel 不等式) 若 \( f \) 于区间 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和平方可积,且 \( f\left( x\right)  \sim  \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {nx} + {b}_{n}\sin {nx}}\right) \) ,则有

\[
\frac{{a}_{0}^{2}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}^{2} + {b}_{n}^{2}}\right)  \leq  \frac{1}{\pi }{\int }_{-\pi }^{\pi }{f}^{2}\left( x\right) \mathrm{d}x. \tag{15.11}
\]

---

① 关于 \( f \) 的条件要作些解释. 若 \( f \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上常义可积,则也绝对可积和平方可积. 否则，从 \( {f}^{2} \) 在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上广义可积,由不等式 \( \left| {f\left( x\right) }\right|  \leq  \frac{1 + f{\left( x\right) }^{2}}{2} \) 可以推知 \( f \) 可积与绝对可积.

---

证 从命题 15.1.6 得到

\[
{2\pi }{d}^{2}\left( {f,{S}_{n}}\right)  = {\int }_{-\pi }^{\pi }{f}^{2} - \frac{\pi {a}_{0}^{2}}{2} - \pi \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}^{2} + {b}_{k}^{2}}\right)  \geq  0.
\]

由于这对每个 \( n \) 成立,因此 (15.11) 左边的正项级数的每个部分和均以右边的积分为上界, 从而收敛, 且使该不等式成立.

注 1 这个结果与 Fourier 级数的收敛性没有关系,由此就可以得到 \( {a}_{n} = o\left( 1\right) \) , \( {b}_{n} = o\left( 1\right) \) ,这里也不需要用 Riemann 引理.

注 2 由此可知,在 \( 0 < p \leq  \frac{1}{2} \) 时,三角级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\sin {nx}}{{n}^{p}},\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{\cos {nx}}{{n}^{p}} \) 不可能是可积和平方可积函数的 Fourier 级数 \( {}^{\text{ ① }} \) .

#### 15.1.4 例题

例题 15.1.1 证明: 三角多项式 \( {P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( {{A}_{k}\cos {kx} + {B}_{k}\sin {kx}}\right) \) 的 Fourier 级数就是其本身.

证 三角多项式可看成是只含有限个非零项的三角级数,因此在 \( \left( {-\infty , + \infty }\right) \) 上一致收敛，引用命题 15.1.1 即得. (本题的另一个解法当然是直接计算.)

在用公式计算 Fourier 系数时，即使对于相当简单的 \( f \) ，也可能要作多次分部积分运算，计算量相当大. 因此，除了要细心地按公式计算之外，还应该学习(或发明) 一些较为灵活的计算方法. 为此在下面列举几种非常规方法供参考. 此外, 在学了逐项积分定理后还会有新的计算方法.

例题 15.1.2 设函数 \( f\left( x\right)  = {x}^{3}, x \in  \left( {-\pi ,\pi }\right) \) ,求 \( f \) 的 Fourier 级数,

解 1 利用 Euler 公式 \( {\mathrm{e}}^{\mathrm{i}\theta } = \cos \theta  + \mathrm{i}\sin \theta \) 在复数域进行计算往往是很有效的方法. 对本题可以计算如下:

\[
\frac{1}{\pi }{\int }_{-\pi }^{\pi }{x}^{3}\left( {\cos {nx} + \mathrm{i}\sin {nx}}\right) \mathrm{d}x = \frac{1}{\pi }{\int }_{-\pi }^{\pi }{x}^{3}{\mathrm{e}}^{\mathrm{i}{nx}}\mathrm{\;d}x
\]

\[
= {\left. \frac{1}{\pi }\left( \frac{{x}^{3}}{\mathrm{i}n}{\mathrm{e}}^{\mathrm{i}{nx}} - \frac{3{x}^{2}}{{\left( \mathrm{i}n\right) }^{2}}{\mathrm{e}}^{\mathrm{i}{nx}} + \frac{6x}{{\left( \mathrm{i}n\right) }^{3}}{\mathrm{e}}^{\mathrm{i}{nx}} - \frac{6}{{\left( \mathrm{i}n\right) }^{4}}{\mathrm{e}}^{\mathrm{i}{nx}}\right) \right| }_{-\pi }^{\pi }
\]

\[
= \mathrm{i}\frac{2{\left( -1\right) }^{n}}{\pi }\left( {-\frac{{\pi }^{3}}{n} + \frac{6\pi }{{n}^{3}}}\right)  = \mathrm{i}{\left( -1\right) }^{n - 1}\left( {\frac{2{\pi }^{2}}{n} - \frac{12}{{n}^{3}}}\right) .
\]

于是所求的 Fourier 级数为

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}\left( {\frac{2{\pi }^{2}}{n} - \frac{12}{{n}^{3}}}\right) \sin {nx}
\]

---

① 但是这两个三角级数仍然是其和函数的 Fourier 级数，它们的和函数不平方可积，但可积和绝对可积. 见后面的例题 15.2.3 和 15.2.4.

---

解 2 这里的工具是命题 15.1.2. 先用公式 (15.2) 直接计算出在 \( \left( {-\pi ,\pi }\right) \) 上函数 \( x \) 的 Fourier 级数:

\[
x \sim  \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{2{\left( -1\right) }^{n - 1}}{n}\sin {nx} \tag{15.12}
\]

然后从 \( {\left( {x}^{2}\right) }^{\prime } = {2x} \) 和公式 (15.6) 得到

\[
{x}^{2} \sim  \frac{{\pi }^{2}}{3} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{4{\left( -1\right) }^{n}}{{n}^{2}}\cos {nx} \tag{15.13}
\]

其中常数项是直接计算得到的.

由于在区间 \( \left( {-\pi ,\pi }\right) \) 上的 \( {x}^{3} \) 不可能连续延拓为周期 \( {2\pi } \) 的连续函数,因此不能直接用命题 15.1.2,但可以采用技巧 (15.7) 将 \( {x}^{3} \) 分解为:

\[
{x}^{3} = \left( {{x}^{3} - {\pi }^{2}x}\right)  + {\pi }^{2}x. \tag{15.14}
\]

右边第一项可以延拓为满足命题 15.1.2 的周期 \( {2\pi } \) 的连续函数，其导函数为 \( 3{x}^{2} \) ，因此就可以用公式 (15.6) 和 (15.12) 得到 \( {x}^{3} \) 的正弦级数中 \( \sin {nx} \) 的系数为

\[
3 \cdot  \frac{4{\left( -1\right) }^{n}}{{n}^{3}} + {\pi }^{2} \cdot  \frac{2{\left( -1\right) }^{n - 1}}{n} = \frac{{\left( -1\right) }^{n}{12}}{{n}^{3}} + \frac{{\left( -1\right) }^{n - 1}2{\pi }^{2}}{n}.
\]

例题 15.1.3 设 \( f \) 为 \( \left( {0,\frac{\pi }{2}}\right) \) 上的可积和绝对可积函数. 问: 如何将 \( f \) 延拓到区间 \( \left( {-\pi ,\pi }\right) \) 上,使其 Fourier 级数具有如下的形式:

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{{2n} - 1}\cos \left( {{2n} - 1}\right) x
\]

解 由题意要求 \( {a}_{2n} = 0 \) ,从公式 \( {a}_{2n} = \frac{2}{\pi }{\int }_{0}^{\pi }f\left( x\right) \cos {2nx}\mathrm{\;d}x \) 可见,由于 \( \cos {2nx} \) 在 \( \left\lbrack  {0,\pi }\right\rbrack \) 上关于其中点为偶函数,根据上册 324 页命题 10.4.5,只要有 \( f\left( x\right)  =  - f\left( {\pi  - x}\right) \) 成立就可以使上述积分为 0 . 这决定了 \( f \) 在 \( \left( {\frac{\pi }{2},\pi }\right) \) 上的延拓. 定义 \( f\left( 0\right)  = f\left( \frac{\pi }{2}\right)  = 0 \) ,然后用偶延拓 \( f\left( {-x}\right)  = f\left( x\right) \) 将 \( f \) 延拓到 \( \left( {-\pi ,0}\right) \) 上即可.

结论: 将 \( f \) 以如下方式延拓:

\[
F\left( x\right)  = \left\{  \begin{array}{ll} f\left( x\right) , & x \in  \left( {0,\frac{\pi }{2}}\right) , \\   - f\left( {\pi  - x}\right) , & x \in  \left( {\frac{\pi }{2},\pi }\right) , \\  0, & x = 0,\frac{\pi }{2}, \\  f\left( {-x}\right) , & x \in  \left( {-\pi ,0}\right) . \end{array}\right.
\]

#### 15.1.5 练习题

1. 求下列函数的 Fourier 级数:

(1) \( {\sin }^{3}x + {\cos }^{4}x \)

(2) \( a{x}^{3} + b{x}^{2} + {cx} + d, x \in  \left( {-\pi ,\pi }\right) \) .

2. 将定义在 \( \left( {0,\frac{\pi }{2}}\right) \) 上的可积和绝对可积函数 \( f \) 延拓到区间 \( \left( {-\pi ,\pi }\right) \) 上,使其 Fourier 级数具有如下的形式: \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{b}_{{2n} - 1}\sin \left( {{2n} - 1}\right) x \) .

3. 证明: 函数

\[
f\left( x\right)  = \left\{  \begin{array}{ll} c, & 0 < x \leq  \pi , \\  0, & x = 0, \\   - c, &  - \pi  < x < 0 \end{array}\right.
\]

的 Fourier 级数的前 \( {2n} + 1 \) 项的和 \( {S}_{n}\left( x\right)  = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{a}_{k}\cos {kx} + {b}_{k}\sin {kx}}\right) \) 具有形式

\[
{S}_{n}\left( x\right)  = \frac{2c}{\pi }{\int }_{0}^{x}\frac{\sin {2nt}}{\sin t}\mathrm{\;d}t.
\]

4. 设 \( f \in  {C}^{1}\left\lbrack  {-\pi ,\pi }\right\rbrack \) ,证明:

\[
{a}_{n} = o\left( \frac{1}{n}\right) ,{b}_{n} = O\left( \frac{1}{n}\right) ;
\]

如果又有 \( f\left( \pi \right)  = f\left( {-\pi }\right) \) ,则 \( {b}_{n} = o\left( \frac{1}{n}\right) \) .

5. 设 \( f \) 是以 \( {2\pi } \) 为周期的有界函数且在 \( \left( {-\pi ,\pi }\right) \) 上逐段单调,证明:

\[
{a}_{n} = O\left( \frac{1}{n}\right) ,{b}_{n} = O\left( \frac{1}{n}\right) .
\]

(可在每个单调区间上用积分第二中值定理 (见上册的命题 10.2.2).)

6. 设 \( f \) 是以 \( {2\pi } \) 为周期的函数且在 \( \left\lbrack  {-\pi ,\pi }\right\rbrack \) 上可积和绝对可积,证明: 用 \( \sin x \) 去乘 \( f \) 的 Fourier 级数的每一项所得的三角级数就是 \( f\left( x\right) \sin x \) 的 Fourier 级数.

7. 设 \( \left\lbrack  {a, b}\right\rbrack \) 上的连续函数系 \( \left\{  {e}_{n}\right\} \) 满足条件 \( {\int }_{a}^{b}{e}_{i}\left( x\right) {e}_{j}\left( x\right) \mathrm{d}x = {\delta }_{ij} \) ,其中 \( {\delta }_{ij} = \; 0,\forall i \neq  j,{\delta }_{ii} = 1 \) ,则称该函数系在 \( \left\lbrack  {a, b}\right\rbrack \) 上为规范正交系. 设 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上可积和平方可积,定义 \( {c}_{n} = {\int }_{a}^{b}f\left( x\right) {e}_{n}\left( x\right) \mathrm{d}x \) 为 \( f \) 关于 \( {e}_{n} \) 的 Fourier 系数, \( n = 1,2,\cdots \) . 证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{c}_{n}^{2} \) 收敛. 又问: 当 \( n \) 固定时, \( {a}_{1},{a}_{2},\cdots ,{a}_{n} \) 取什么值时, 平方平均误差

\[
{\int }_{a}^{b}{\left\lbrack  f\left( x\right)  - \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}{e}_{k}\left( x\right) \right\rbrack  }^{2}\mathrm{\;d}x
\]

最小?

8. 设 \( g \) 是周期为 1 的连续函数且 \( {\int }_{0}^{1}g\left( x\right) \mathrm{d}x = 0 \) ,函数 \( f \in  {C}^{1}\left\lbrack  {0,1}\right\rbrack \) ,令

\[
{a}_{n} = {\int }_{0}^{1}f\left( x\right) g\left( {nx}\right) \mathrm{d}x, n = 1,2,\cdots ,
\]

证明: 级数 \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n}^{2} \) 收敛.
