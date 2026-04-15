## §7.2 Taylor 定理

这一节主要是两个 Taylor 公式 (也称为 Taylor 展开式), 即分别带有 Peano 余项和 Lagrange 余项的 Taylor 公式, 统称为 Taylor 定理. 前者是上一章中的无穷小增量公式的推广, 而后者是 Lagrange 中值定理 (即有限增量公式) 的推广.

Taylor 定理的内容和证明对初学者有一定的困难. 仅仅从两个公式的复杂形式看, 就有点使人望而生畏. 因此我们将对它们的内容和证明做一定的剖析. 实际上这里的根本问题就是怎样用多项式来逼近函数. 但是从方法上来说, 则只是上一节中已用过多次的方法的重复 (参见例题 7.1.3 的两个证明).

在以上内容的基础上, 本节还要介绍带 Cauchy 余项的 Taylor 公式. 在 7.2.3 小节中将介绍 Euler 数和 Bernoulli 数, 以供读者参考.

#### 7.2.1 基本定理

这里要解决的基本问题就是用多项式来逼近一个函数.

实际上, 如果局限于一次多项式, 即线性函数, 则在前面已经讨论过这个问题. 回顾第六章中的无穷小增量公式 (6.1),可见它就是用线性函数 \( f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) (x - \; {x}_{0} \) ) 来逼近 \( f\left( x\right) \) . 例题 6.1.3 则严格建立了这个函数在所有线性函数中在一定意义上所具有的最优性质.

命题 7.2.2 可看成是公式 (6.1) 的推广. 命题 7.2.5 则是例题 6.1.3 的推广.

为此先做一项准备工作,即证明在下列意义上于某点 \( {x}_{0} \) 附近逼近一个函数 \( f\left( x\right) \) 的多项式如果存在,则一定是唯一的.

命题 7.2.1 (唯一性引理) 设 \( f \) 在点 \( {x}_{0} \) 的某邻域 \( O\left( {x}_{0}\right) \) 上有定义,且有

\[
f\left( x\right)  = {c}_{0} + {c}_{1}\left( {x - {x}_{0}}\right)  + \cdots  + {c}_{n}{\left( x - {x}_{0}\right) }^{n} + o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) ,
\]

则其中的系数 \( {c}_{0},{c}_{1},\cdots ,{c}_{n} \) 是唯一确定的.

证 根据条件可以知道以下表达式右边的极限都是存在的. 又根据极限的唯一性定理, 可见所有这些系数都是唯一确定的.

\[
{c}_{0} = \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}f\left( x\right)
\]

\[
{c}_{1} = \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{f\left( x\right)  - {c}_{0}}{x - {x}_{0}}
\]

............

\[
{c}_{n} = \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{f\left( x\right)  - \left\lbrack  {{c}_{0} + {c}_{1}\left( {x - {x}_{0}}\right)  + \cdots  + {c}_{n - 1}{\left( x - {x}_{0}\right) }^{n - 1}}\right\rbrack  }{{\left( x - {x}_{0}\right) }^{n}}.
\]

下面的第一个 Taylor 公式, 即带有 Peano 余项的 Taylor 公式, 肯定了当函数 \( f\left( x\right) \) 在点 \( {x}_{0} \) 有 \( n \) 阶导数时,满足唯一性引理的条件的 \( n \) 次多项式是存在的,同时还给出了系数 \( {c}_{0},{c}_{1},\cdots ,{c}_{n} \) 的计算公式.

命题 7.2.2 (带 Peano 余项的 Taylor 公式) 若函数 \( f \) 在点 \( {x}_{0} \) 存在 \( n \) 阶导数 \( {f}^{\left( n\right) }\left( {x}_{0}\right) \) ,则有

\[
f\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots
\]

\[
+ \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n} + o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) .
\]

证 首先要对于条件有准确的理解. 从函数 \( f \) 在点 \( {x}_{0} \) 有 \( n \) 阶导数可推出 \( f \) 在该点的某邻域上存在所有的 \( k\left( { < n}\right) \) 阶导函数,但是 \( {f}^{\left( n\right) }\left( x\right) \) 只知在点 \( {x}_{0} \) 存在.

引入多项式

\[
{p}_{n}\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots  + \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n} \tag{7.18}
\]

和

\[
{r}_{n}\left( x\right)  = f\left( x\right)  - {p}_{n}\left( x\right) . \tag{7.19}
\]

今后称多项式 \( {p}_{n}\left( x\right) \) 为 \( f\left( x\right) \) 在点 \( {x}_{0} \) 处的 \( n \) 阶 Taylor 多项式,称 \( {r}_{n}\left( x\right) \) 为 (第 \( n \) 次) 余项,即用多项式 \( {p}_{n}\left( x\right) \) 代替 \( f\left( x\right) \) 所带来的误差项.

可以看出, 证明的目的只不过是要建立以下的极限关系:

\[
\mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{{r}_{n}\left( x\right) }{{\left( x - {x}_{0}\right) }^{n}} = 0. \tag{7.20}
\]

由 (7.19) 可见,余项的可微性质与 \( f \) 完全相同. 直接验证以下等式 (具体计算从略),

\[
{p}_{n}\left( {x}_{0}\right)  = f\left( {x}_{0}\right) ,{p}_{n}^{\prime }\left( {x}_{0}\right)  = {f}^{\prime }\left( {x}_{0}\right) ,\cdots ,{p}_{n}^{\left( n\right) }\left( {x}_{0}\right)  = {f}^{\left( n\right) }\left( {x}_{0}\right) , \tag{7.21}
\]

就知道余项 \( {r}_{n}\left( x\right) \) 满足条件

\[
{r}_{n}\left( {x}_{0}\right)  = 0,{r}_{n}^{\prime }\left( {x}_{0}\right)  = 0,\cdots ,{r}^{\left( n\right) }\left( {x}_{0}\right)  = 0. \tag{7.22}
\]

反复使用 Cauchy 中值定理并在最后令 \( x \rightarrow  {x}_{0} \) ,就可以得到所要的结果:

\[
\frac{{r}_{n}\left( x\right) }{{\left( x - {x}_{0}\right) }^{n}} = \frac{{r}_{n}\left( x\right)  - {r}_{n}\left( {x}_{0}\right) }{{\left( x - {x}_{0}\right) }^{n}} = \frac{{r}_{n}^{\prime }\left( {\xi }_{1}\right) }{n{\left( {\xi }_{1} - {x}_{0}\right) }^{n - 1}}
\]

\[
= \frac{{r}_{n}^{\prime }\left( {\xi }_{1}\right)  - {r}_{n}^{\prime }\left( {x}_{0}\right) }{n{\left( {\xi }_{1} - {x}_{0}\right) }^{n - 1}} = \frac{{r}_{n}^{\prime \prime }\left( {\xi }_{2}\right) }{n\left( {n - 1}\right) {\left( {\xi }_{2} - {x}_{0}\right) }^{n - 2}}
\]

............

\[
= \frac{{r}_{n}^{\left( n - 1\right) }\left( {\xi }_{n - 1}\right)  - {r}_{n}^{\left( n - 1\right) }\left( {x}_{0}\right) }{n!\left( {{\xi }_{n - 1} - {x}_{0}}\right) } \rightarrow  \frac{{r}^{\left( n\right) }\left( {x}_{0}\right) }{n!} = 0\left( {x \rightarrow  {x}_{0}}\right) .
\]

这里依次利用了余项 \( {r}_{n}\left( x\right) \) 所具有的性质 (7.22) 中的每一个等式. 在反复使用 Cauchy 中值定理时得到的 “中值” \( {\xi }_{1},{\xi }_{2},\cdots ,{\xi }_{n - 1} \) 是在 \( x \) 与 \( {x}_{0} \) 之间的单调点列. 例如当 \( {x}_{0} < x \) 时,从上面的推导可以看出有

\[
{x}_{0} < {\xi }_{n - 1} < \cdots  < {\xi }_{2} < {\xi }_{1} < x.
\]

因此当 \( x \rightarrow  {x}_{0} \) 时也有 \( {\xi }_{n - 1} \rightarrow  {x}_{0} \) .

还要注意最后一步与前面不同. 由于只知道 \( {r}_{n}\left( x\right) \) 在点 \( {x}_{0} \) 处有 \( n \) 阶导数,所以最后一步不能用中值定理,而只能用定义,也就是说,导数 \( {r}_{n}^{\left( n\right) }\left( {x}_{0}\right) \) 是 \( {r}_{n}\left( x\right) \) 的 \( n - 1 \) 阶导函数 \( {r}_{n}^{\left( n - 1\right) }\left( x\right) \) 在点 \( {x}_{0} \) 处的导数.

注 1 称 \( {r}_{n}\left( x\right)  = o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) \) 为 Peano (型) 余项. 容易看出当 \( n = 1 \) 时带 Peano 余项的 Taylor 公式就是上一章中的无穷小增量公式 (6.1). 由于这样的公式并非普通的等式, 而是反映了极限性质的渐近等式, 因此带有 Peano 余项的 Taylor 公式在求极限时很有用处, 对余项可以提供无穷小量的阶的估计. 但是 Peano 余项并不能提供误差的定量估计. 带 Peano 余项的 Taylor 公式的这些特点与无穷小增量公式 (6.1) 完全相同. 因此可以将它称为局部 Taylor 公式.

注 2 带 Peano 余项的 Taylor 公式的证明方法很多, 例如, 用数学归纳法、中值定理和下一章的 L'Hospital 法则 (见例题 8.1.5) 都可以给出证明.

现在给出第二个 Taylor 公式. 在其中的余项有确定的表达式. 这就为误差估计提供了理论依据. 当然, 其中也有不确定的因素, 即出现了在每个中值定理中都有的“中值”. 因此这个结果也可以称为 Taylor 中值定理. 读者可以看出, 在下面的公式中若 \( n = 0 \) ,则就是 Lagrange 中值定理. 如果将 Cauchy 中值定理看成是 Lagrange 中值定理在两个函数情况的推广, 则 Taylor 中值定理就是 Lagrange 中值定理在高阶导数情况的推广.

命题 7.2.3 (带 Lagrange 余项的 Taylor 公式) 若 \( f \) 在点 \( {x}_{0} \) 的某邻域 \( O\left( {x}_{0}\right) \) 上 \( n + 1 \) 阶可微,则对每个 \( x \in  O\left( {x}_{0}\right) , x \neq  {x}_{0} \) ,在 \( {x}_{0} \) 和 \( x \) 之间存在 \( \xi \) ,使得

\[
f\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots  + \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n} + {r}_{n}\left( x\right) ,
\]

其中

\[
{r}_{n}\left( x\right)  = \frac{{f}^{\left( n + 1\right) }\left( \xi \right) }{\left( {n + 1}\right) !}{\left( x - {x}_{0}\right) }^{n + 1}.
\]

证 1 可以与带 Peano 余项的 Taylor 公式的上述证明几乎一样来做, 即反复使用 Cauchy 中值定理, 但在最后一次是用 Lagrange 中值定理. 原因是在这里的函数 \( f\left( x\right) \) (因而 \( {r}_{n}\left( x\right) \) ) 在邻域 \( O\left( {x}_{0}\right) \) 上有 \( n + 1 \) 阶导函数,条件要强得多了. 证明的主要过程如下:

\[
\frac{{r}_{n}\left( x\right) }{{\left( x - {x}_{0}\right) }^{n + 1}} = \frac{{r}_{n}\left( x\right)  - {r}_{n}\left( {x}_{0}\right) }{{\left( x - {x}_{0}\right) }^{n + 1}} = \frac{{r}_{n}^{\prime }\left( {\xi }_{1}\right) }{\left( {n + 1}\right) {\left( {\xi }_{1} - {x}_{0}\right) }^{n}}
\]

\[
= \frac{{r}_{n}^{\prime }\left( {\xi }_{1}\right)  - {r}_{n}^{\prime }\left( {x}_{0}\right) }{\left( {n + 1}\right) {\left( {\xi }_{1} - {x}_{0}\right) }^{n}} = \frac{{r}_{n}^{\prime \prime }\left( {\xi }_{2}\right) }{\left( {n + 1}\right) n{\left( {\xi }_{2} - {x}_{0}\right) }^{n - 1}}
\]

......

\[
= \frac{{r}_{n}^{\left( n\right) }\left( {\xi }_{n}\right)  - {r}_{n}^{\left( n\right) }\left( {x}_{0}\right) }{\left( {n + 1}\right) !\left( {{\xi }_{n} - {x}_{0}}\right) } = \frac{{r}^{\left( n + 1\right) }\left( \xi \right) }{\left( {n + 1}\right) !}.
\]

回顾例题 7.1.3 的两种不同方法, 可以知道用辅助函数方法也能成功. 实际上, 在那里已经分析过这两个方法, 它们在本质上是完全一样的. 下面就是用辅助函数方法证明第二个 Taylor 公式.

证 2 对给定的 \( x \neq  {x}_{0} \) ,定义

\[
\lambda  = \frac{{r}_{n}\left( x\right) \left( {n + 1}\right) !}{{\left( x - {x}_{0}\right) }^{n + 1}}.
\]

于是只要证明在 \( x \) 和 \( {x}_{0} \) 之间存在 \( \xi \) ,使得

\[
{r}_{n}^{\left( n + 1\right) }\left( \xi \right)  = \lambda
\]

即可. 不妨只考虑 \( {x}_{0} < x \) 的情况. 现在固定 \( x \) ,在区间 \( \left\lbrack  {{x}_{0}, x}\right\rbrack \) 上构造辅助函数

\[
F\left( t\right)  = {r}_{n}\left( t\right)  - \frac{\lambda }{\left( {n + 1}\right) !}{\left( t - {x}_{0}\right) }^{n + 1},{x}_{0} \leq  t \leq  x.
\]

可见只要证明存在 \( \xi  \in  \left( {{x}_{0}, x}\right) \) ,使得 \( {F}^{\left( n + 1\right) }\left( \xi \right)  = 0 \) .

从条件 (7.22) 和 \( \lambda \) 的定义知,辅助函数 \( F \) 具有性质

\[
F\left( {x}_{0}\right)  = 0,{F}^{\prime }\left( {x}_{0}\right)  = 0,\cdots ,{F}^{\left( n\right) }\left( {x}_{0}\right)  = 0\text{ 和 }F\left( x\right)  = 0.
\]

在区间 \( \left\lbrack  {{x}_{0}, x}\right\rbrack \) 上对 \( F \) 用 Rolle 定理,有 \( {\xi }_{1} \in  \left( {{x}_{0}, x}\right) \) ,使得 \( {F}^{\prime }\left( {\xi }_{1}\right)  = 0 \) . 然后由于 \( {F}^{\prime }\left( {x}_{0}\right)  = 0 \) ,在区间 \( \left\lbrack  {{x}_{0},{\xi }_{1}}\right\rbrack \) 上对 \( {F}^{\prime } \) 用 Rolle 定理,有 \( {\xi }_{2} \in  \left( {{x}_{0},{\xi }_{1}}\right) \) ,使得 \( {F}^{\prime \prime }\left( {\xi }_{2}\right)  = 0 \) . 这样进行下去,在做了 \( n \) 次后,就有

\[
{x}_{0} < {\xi }_{n} < {\xi }_{n - 1} < \cdots  < {\xi }_{1} < x
\]

以及 \( {F}^{\left( n\right) }\left( {\xi }_{n}\right)  = 0 \) . 最后再利用 \( {F}^{\left( n\right) }\left( {x}_{0}\right)  = 0 \) ,在区间 \( \left\lbrack  {{x}_{0},{\xi }_{n}}\right\rbrack \) 上对 \( {F}^{\left( n\right) }\left( x\right) \) 用 Rolle 定理,就得到 \( \xi  \in  \left( {{x}_{0},{\xi }_{n}}\right)  \subset  \left( {{x}_{0}, x}\right) \) ,使得 \( {F}^{\left( n + 1\right) }\left( \xi \right)  = 0 \) . 这样我们就完成了命题的证明.

注 在上述命题中我们要求 \( x \neq  {x}_{0} \) . 实际上在 \( x = {x}_{0} \) 时 Taylor 公式自然成立,这时的中值 \( \xi \) 可以任取. 此外,从证明可以看出,并不要求 \( {f}^{\left( n + 1\right) }\left( {x}_{0}\right) \) 存在,也就是说只要 \( f \) 在 \( O\left( {x}_{0}\right) \) 上 \( n \) 阶可微,又在 \( O\left( {x}_{0}\right)  - \left\{  {x}_{0}\right\} \) 上存在 \( {f}^{\left( n + 1\right) }\left( x\right) \) 即可. 这对下一个命题也是如此.

以上介绍了余项的两种不同形式, 即 Peano 余项和 Lagrange 余项. 实际上还有很多不同的其他余项形式, 其中对今后较为有用的是 Cauchy 余项和积分型余项. 后者见 11.4.3 小节. 下面是 Cauchy 余项及其证明.

命题 7.2.4 (带 Cauchy 余项的 Taylor 公式) 若 \( f \) 在点 \( {x}_{0} \) 的某邻域 \( O\left( {x}_{0}\right) \) 上 \( n + 1 \) 阶可微,则对每个 \( x \in  O\left( {x}_{0}\right) , x \neq  {x}_{0} \) ,在 \( {x}_{0} \) 和 \( x \) 之间存在 \( \eta \) ,使得

\[
f\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \cdots  + \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n} + {r}_{n}\left( x\right) ,
\]

其中

\[
{r}_{n}\left( x\right)  = \frac{{f}^{\left( n + 1\right) }\left( \eta \right) }{n!}{\left( x - \eta \right) }^{n}\left( {x - {x}_{0}}\right) .
\]

证 固定 \( x \) ,在余项

\[
{r}_{n}\left( x\right)  = f\left( x\right)  - {p}_{n}\left( x\right)
\]

\[
= f\left( x\right)  - \left\lbrack  {f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \cdots  + \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n}}\right\rbrack
\]

的右边将 \( {x}_{0} \) 换为变量 \( t \in  \left\lbrack  {{x}_{0}, x}\right\rbrack \) ,定义函数

\[
\Phi \left( t\right)  = f\left( x\right)  - \left\lbrack  {f\left( t\right)  + {f}^{\prime }\left( t\right) \left( {x - t}\right)  + \cdots  + \frac{{f}^{\left( n\right) }\left( t\right) }{n!}{\left( x - t\right) }^{n}}\right\rbrack  .
\]

可以看出有

\[
\Phi \left( {x}_{0}\right)  = {r}_{n}\left( x\right) ,\Phi \left( x\right)  = 0.
\]

通过直接计算可以得到

\[
{\Phi }^{\prime }\left( t\right)  =  - \frac{{f}^{\left( n + 1\right) }\left( t\right) }{n!}{\left( x - t\right) }^{n}.
\]

在区间 \( \left\lbrack  {{x}_{0}, x}\right\rbrack \) 上对 \( \Phi \left( t\right) \) 用 Lagrange 中值定理,就有 \( \eta  \in  \left( {x,{x}_{0}}\right) \) ,使得

\[
{r}_{n}\left( x\right)  = \Phi \left( {x}_{0}\right)  - \Phi \left( x\right)  = {\Phi }^{\prime }\left( \eta \right) \left( {{x}_{0} - x}\right) .
\]

将 \( {\Phi }^{\prime }\left( \eta \right) \) 的表达式代入就得到所要求证的 Cauchy 余项.

注 用这个方法也可以得到其他余项形式 (见 [14] 的第一卷 126 小节).

到此为止本小节已介绍了 Taylor 公式的主要理论. 我们看到,若函数 \( f\left( x\right) \) 在点 \( {x}_{0} \) 有 \( n \) 阶导数,则就有一个 \( n \) 次多项式 (7.18),即 Taylor 多项式,它与 \( f\left( x\right) \) 的差 (即余项 (7.19)) 当 \( x \rightarrow  {x}_{0} \) 时是比 \( {\left( x - {x}_{0}\right) }^{n} \) 更高阶的无穷小量. 命题 7.2.1 肯定了这样的多项式是唯一的, 命题 7.2.2 则解决了它的存在性. 命题 7.2.3 和 7.2.4 给出了余项的更为精确的表达式,当然这时对 \( f \) 要有更多的条件.

可将例题 6.1.3 推广得到下列命题. 它确切地刻画了 Taylor 多项式在局部逼近方面的最优性质.

命题 7.2.5 (Taylor 多项式的逼近性质) 设函数 \( f \) 在点 \( {x}_{0} \) 存在 \( {f}^{\left( n\right) }\left( {x}_{0}\right) \) , \( {p}_{n}\left( x\right) \) 是由公式 (7.18) 定义的 Taylor 多项式. 对于和 \( {p}_{n}\left( x\right) \) 不相等的每一个不超过 \( n \) 次的多项式 \( p\left( x\right) \) ,存在 \( \delta  > 0 \) ,使得当 \( 0 < \left| {x - {x}_{0}}\right|  < \delta \) 时,成立不等式

\[
\left| {f\left( x\right)  - {p}_{n}\left( x\right) }\right|  < \left| {f\left( x\right)  - p\left( x\right) }\right| .
\]

证 先将给定的多项式 \( p\left( x\right) \) 转换成用 \( \left( {x - {x}_{0}}\right) \) 的方幂表示的升幂多项式:

\[
p\left( x\right)  = {a}_{0} + {a}_{1}\left( {x - {x}_{0}}\right)  + \cdots  + {a}_{n}{\left( x - {x}_{0}\right) }^{n}. \tag{7.23}
\]

根据命题 7.2.2,可以将 \( p\left( x\right) \) 看成那里的 \( f\left( x\right) \) ,然后用公式 (7.21) 直接求出 \( {a}_{i} = \; {p}^{\left( i\right) }\left( {x}_{0}\right) /i!, i = 0,1,\cdots , n \) . (当然也可以用代数方法计算,这里从略.)

将 (7.23) 与 Taylor 多项式

\[
{p}_{n}\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots  + \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n}
\]

进行比较. 如果 \( {a}_{0} \neq  f\left( {x}_{0}\right) \) ,则同例题 6.1.3 的情况 (1) 完全一样,证明是容易的. 否则,根据这两个多项式不相等的假设条件,两者又均已表示为以 \( \left( {x - {x}_{0}}\right) \) 为幂次的升幂多项式,因此一定存在一个正整数 \( k \) ,满足 \( 0 < k \leq  n \) 和

\[
{a}_{0} = f\left( {x}_{0}\right) ,\cdots ,{a}_{k - 1} = {f}^{\left( k - 1\right) }\left( {x}_{0}\right) /\left( {k - 1}\right) !\text{ ,但是 }{a}_{k} \neq  {f}^{\left( k\right) }\left( {x}_{0}\right) /k!\text{ . }
\]

利用命题 7.2.2 (即带 Peano 余项的 Taylor 公式), 有

\[
f\left( x\right)  - {p}_{n}\left( x\right)  = o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) ,
\]

\[
f\left( x\right)  - p\left( x\right)  = \left\lbrack  {f\left( x\right)  - {p}_{n}\left( x\right) }\right\rbrack   + \left\lbrack  {{p}_{n}\left( x\right)  - p\left( x\right) }\right\rbrack
\]

\[
= \left\lbrack  {{f}^{\left( k\right) }\left( {x}_{0}\right) /k! - {a}_{k}}\right\rbrack  {\left( x - {x}_{0}\right) }^{k} + o\left( {\left( x - {x}_{0}\right) }^{k}\right) \left( {x \rightarrow  {x}_{0}}\right) .
\]

其中的项 \( o\left( {\left( x - {x}_{0}\right) }^{k}\right) \) 是对于在多项式 \( \left\lbrack  {{p}_{n}\left( x\right)  - p\left( x\right) }\right\rbrack \) 中次数 \( i > k \) 的所有 \( {\left( x - {x}_{0}\right) }^{i} \) 项和余项 \( f\left( x\right)  - {p}_{n}\left( x\right) \) 之和的一个刻画.

于是有

\[
\frac{f\left( x\right)  - {p}_{n}\left( x\right) }{f\left( x\right)  - p\left( x\right) } = \frac{o\left( {\left( x - {x}_{0}\right) }^{n}\right) }{\left\lbrack  {{f}^{\left( k\right) }\left( {x}_{0}\right) /k! - {a}_{k}}\right\rbrack  {\left( x - {x}_{0}\right) }^{k} + o\left( {\left( x - {x}_{0}\right) }^{k}\right) }\left( {x \rightarrow  {x}_{0}}\right) .
\]

由于 \( {f}^{\left( k\right) }\left( {x}_{0}\right) /k! \neq  {a}_{k} \) 和 \( k \leq  n \) ,可见

\[
\frac{f\left( x\right)  - {p}_{n}\left( x\right) }{f\left( x\right)  - p\left( x\right) } = o\left( 1\right) \left( {x \rightarrow  {x}_{0}}\right) .
\]

从而存在 \( \delta  > 0 \) ,使得当 \( 0 < \left| {x - {x}_{0}}\right|  < \delta \) 时,成立

\[
\left| \frac{f\left( x\right)  - {p}_{n}\left( x\right) }{f\left( x\right)  - p\left( x\right) }\right|  < 1,
\]

![bo_d7fstb491nqc7381io20_225_807_1617_619_553_0.jpg](images/xie_analysis_exercises_upper_017_bod7fstb491nqc7381io2022580716176195530.jpg)

图 7.6

这就是所要求证的不等式.

在图 7.6 中可以看到函数 \( {\mathrm{e}}^{x} \) 以及它的 1 次到 4 次的 Taylor 多项式的图像,其中粗黑曲线是 \( {\mathrm{e}}^{x} \) 的图像. 又为清楚起见,在每一个 Taylor 多项式的图像两端都用记号 \( {P}_{n}\left( x\right) \) 作了标记. 这里的 \( {P}_{n}\left( x\right) \) 是 \( {\mathrm{e}}^{x} \) 在点 \( x = 0 \) 处的 \( n \) 阶 Taylor 多项式:

\[
1 + x + \frac{{x}^{2}}{2!} + \frac{{x}^{3}}{3!} + \cdots  + \frac{{x}^{n}}{n!}.
\]

我们看到,对于 \( n = 3,4 \) , Taylor 多项式在 \( \left| x\right| \) 不很大时已提供了对 \( {\mathrm{e}}^{x} \) 的较好的逼近. 但是当 \( \left| x\right| \) 足够大时,情况完全不是如此. 例如,当 \( n \) 为奇数时 \( {P}_{n}\left( x\right) \) 都有零点. 关于 \( {\mathrm{e}}^{x} \) 的 Taylor 多项式的一般性结论可参看第八章的第二组参考题 4.

#### 7.2.2 例题

当 Taylor 公式中的点 \( {x}_{0} = 0 \) 时,由于历史原因也称为 Maclaurin 公式. 在各种微积分教科书中都要介绍几个基本初等函数的 Maclaurin 公式, 其中包括 \( \sin x,\cos x,\arctan x,{\mathrm{e}}^{x},\ln \left( {1 + x}\right) ,{\left( 1 + x\right) }^{\alpha }\left( {\alpha  \neq  0}\right) \) 等,这里不再重复.

在求以上几个基本初等函数的 Maclaurin 公式时, 一般的方法是直接计算函数在点 \( x = 0 \) 处的 \( n \) 阶导数的通式,这样就可以得到带 Peano 余项的 Maclaurin 公式. 为了得到带 Lagrange 余项的相应公式,则需要得到 \( n \) 阶导函数的表达式,这就困难得多了. 在上一章中关于高阶导数的不少训练与此有关.

在本小节介绍求 Taylor (或 Maclaurin) 公式的间接法. 这在很多求 Taylor 公式的问题中有效，且具有很大的灵活性. 实际上， \( \ln \left( {1 + x}\right) \) 和 \( \arctan x \) 的 Maclaurin 公式也都可以用间接法得到. 但是间接法是以若干个已知的 Taylor 公式为基础的. 如果连基本的 Taylor 公式都不知道, 也就不可能用间接法.

在本小节中除了 Taylor 公式的计算外, 还将介绍 Taylor 公式的其他应用, 特别是不能归入下一章的一些问题.

在下面有关 Taylor (或 Maclaurin) 公式的计算题中, 如不另作说明, 则均指带 Peano 余项的公式.

例题 7.2.1 计算 \( f\left( x\right)  = \arcsin x \) 的 Maclaurin 公式直到 \( {x}^{5} \) 项.

解 1 对 \( f \) 求导,并利用二项式展开公式,就有

\[
{f}^{\prime }\left( x\right)  = {\left( 1 - {x}^{2}\right) }^{-\frac{1}{2}} = 1 + \frac{1}{2}{x}^{2} + \frac{3}{8}{x}^{4} + o\left( {x}^{5}\right) \left( {x \rightarrow  0}\right) .
\]

根据上一小节的唯一性引理和带 Peano 余项的 Taylor 公式,可见上式就是 \( {f}^{\prime }\left( x\right) \) 的 Maclaurin 公式. 利用 Taylor 公式中的系数公式, 就可以从上式右边的已知系数反过来求出 \( {f}^{\prime }\left( x\right) \) 在 \( x = 0 \) 处的值和各阶导数值:

\[
1 = {f}^{\prime }\left( 0\right) ,0 = {f}^{\prime \prime }\left( 0\right) ,\frac{1}{2} = \frac{{f}^{\prime \prime \prime }\left( 0\right) }{2},0 = {f}^{\left( 4\right) }\left( 0\right) ,\frac{3}{8} = \frac{{f}^{\left( 5\right) }\left( 0\right) }{4!},0 = {f}^{\left( 6\right) }\left( 0\right) .
\]

这样就求出所需要的前 6 阶导数:

\[
{f}^{\prime }\left( 0\right)  = 1,{f}^{\prime \prime }\left( 0\right)  = 0,{f}^{\prime \prime \prime }\left( 0\right)  = 1,{f}^{\left( 4\right) }\left( 0\right)  = 0,{f}^{\left( 5\right) }\left( 0\right)  = 9,{f}^{\left( 6\right) }\left( 0\right)  = 0.
\]

再利用 \( f\left( 0\right)  = 0 \) ,就得到所要的 Maclaurin 公式:

\[
\arcsin x = x + \frac{1}{3!}{x}^{3} + \frac{9}{5!}{x}^{5} + o\left( {x}^{6}\right)
\]

\[
= x + \frac{1}{6}{x}^{3} + \frac{3}{40}{x}^{5} + o\left( {x}^{6}\right) \left( {x \rightarrow  0}\right) .
\]

注 若将以上的解法发展一步，就可以写出 \( \arcsin x \) 的一般的 Maclaurin 公式， 而无须求出这个函数在 \( x = 0 \) 处的任意阶导数值. 再往前一步，我们可以提出求高阶导数的一种间接计算法. 从 \( f\left( x\right)  = \arcsin x \) 的导函数出发，计算

\[
{f}^{\prime }\left( x\right)  = {\left( 1 - {x}^{2}\right) }^{-\frac{1}{2}}
\]

\[
= 1 + \mathop{\sum }\limits_{{k = 1}}^{n}\frac{\left( {-\frac{1}{2}}\right) \left( {-\frac{3}{2}}\right) \cdots \left( {-\frac{1}{2} - k + 1}\right) }{k!}{\left( -{x}^{2}\right) }^{k} + o\left( {x}^{{2k} + 1}\right)
\]

\[
= 1 + \mathop{\sum }\limits_{{k = 1}}^{n}\frac{\left( {{2k} - 1}\right) !!}{{2}^{k}k!}{x}^{2k} + o\left( {x}^{{2k} + 1}\right) \left( {x \rightarrow  0}\right) ,
\]

就可以对任意正整数 \( k \) 得到 \( {f}^{\left( 2k\right) }\left( 0\right)  = 0 \) 和

\[
{f}^{\left( 2k + 1\right) }\left( 0\right)  = \left( {2k}\right) !\frac{\left( {{2k} - 1}\right) !!}{{2}^{k}k!} = {\left\lbrack  \left( 2k - 1\right) !!\right\rbrack  }^{2}.
\]

这就是在例题 6.2.3 已经得到的结果.

请读者试用这种新方法计算 \( \arctan x \) 和 \( \ln \left( {1 + x}\right) \) 的 Maclaurin 公式和它们在 \( x = 0 \) 处的任意阶导数值.

解 2 由于 \( f\left( x\right)  = \arcsin x \) 是奇函数，又有 \( {f}^{\prime }\left( 0\right)  = 1 \) ，因此它的 Maclaurin 公式的形式如下:

\[
\arcsin x = x + a{x}^{3} + b{x}^{5} + o\left( {x}^{6}\right) \left( {x \rightarrow  0}\right) .
\]

这里只有两个系数 \( a \) 和 \( b \) 需要确定. 利用 \( \arcsin x \) 是 \( \sin x \) 的反函数,又利用 \( \sin x \) 的 Maclaurin 公式, 就有

\[
x = \sin \left( {\arcsin x}\right)
\]

\[
= \arcsin x - \frac{1}{6}{\left( \arcsin x\right) }^{3} + \frac{1}{120}{\left( \arcsin x\right) }^{5} + o\left( {x}^{6}\right)
\]

\[
= \left( {x + a{x}^{3} + b{x}^{5}}\right)  - \frac{1}{6}{\left( x + a{x}^{3}\right) }^{3} + \frac{1}{120}{x}^{5} + o\left( {x}^{6}\right) \left( {x \rightarrow  0}\right) .
\]

比较两边同次幂项的系数, 就有方程

\[
a - \frac{1}{6} = 0, b - \frac{1}{6} \cdot  {3a} + \frac{1}{120} = 0.
\]

这样就可解出

\[
a = \frac{1}{6}, b = \frac{3}{40}.
\]

例题 7.2.2 计算 \( f\left( x\right)  = \sqrt[3]{2 - \cos x} \) 的 Maclaurin 公式直到 \( {x}^{5} \) 项.

解 1 将根式内的表达式写成 \( 1 + \left( {1 - \cos x}\right) \) ，并利用

\[
1 - \cos x = \frac{{x}^{2}}{2} - \frac{{x}^{4}}{24} + o\left( {x}^{5}\right) \left( {x \rightarrow  0}\right) ,
\]

就可以计算如下:

\[
f\left( x\right)  = \sqrt[3]{1 + \left( {1 - \cos x}\right) }
\]

\[
= 1 + \frac{1 - \cos x}{3} - \frac{{\left( 1 - \cos x\right) }^{2}}{9} + O\left( {\left( 1 - \cos x\right) }^{3}\right)
\]

\[
= 1 + \left( {\frac{{x}^{2}}{6} - \frac{{x}^{4}}{72}}\right)  - \frac{{x}^{4}}{36} + o\left( {x}^{5}\right)
\]

\[
= 1 + \frac{{x}^{2}}{6} - \frac{{x}^{4}}{24} + o\left( {x}^{5}\right) \left( {x \rightarrow  0}\right) .
\]

解 2 利用 \( f \) 为偶函数,因此所要求的公式的形状已可确定为

\[
f\left( x\right)  = 1 + a{x}^{2} + b{x}^{4} + o\left( {x}^{5}\right) \left( {x \rightarrow  0}\right) .
\]

为确定 \( a \) 和 \( b \) ，只要将上式代入

\[
{\left\lbrack  f\left( x\right) \right\rbrack  }^{3} = 2 - \cos x = 1 + \frac{{x}^{2}}{2} - \frac{{x}^{4}}{24} + o\left( {x}^{5}\right) \left( {x \rightarrow  0}\right) ,
\]

就得到关于待定系数的方程

\[
{3a} = \frac{1}{2},{3b} + 3{a}^{2} =  - \frac{1}{24}.
\]

从中解出

\[
a = \frac{1}{6}, b =  - \frac{1}{24}.
\]

例题 7.2.3 计算 \( f\left( x\right)  = \ln \frac{\sin x}{x} \) 的 Maclaurin 公式直到 \( {x}^{6} \) 项. 这里 \( f\left( x\right) \) 在 \( x = 0 \) 的值用函数在该点的极限值 0 来定义.

解 从正弦函数的展开式开始，有

\[
\sin x = x - \frac{1}{3!}{x}^{3} + \frac{1}{5!}{x}^{5} - \frac{1}{7!}{x}^{7} + o\left( {x}^{8}\right) \left( {x \rightarrow  0}\right) ,
\]

就有

\[
\frac{\sin x}{x} = 1 - \frac{1}{3!}{x}^{2} + \frac{1}{5!}{x}^{4} - \frac{1}{7!}{x}^{6} + o\left( {x}^{7}\right) \left( {x \rightarrow  0}\right) .
\]

记 \( y =  - \frac{1}{3!}{x}^{2} + \frac{1}{5!}{x}^{4} - \frac{1}{7!}{x}^{6} + o\left( {x}^{7}\right) \left( {x \rightarrow  0}\right) \) ,则 \( y = O\left( {x}^{2}\right) \left( {x \rightarrow  0}\right) \) . 然后有

\[
\ln \frac{\sin x}{x} = \ln \left( {1 + y}\right)
\]

\[
= y - \frac{1}{2}{y}^{2} + \frac{1}{3}{y}^{3} + O\left( {y}^{4}\right)
\]

\[
= \left( {-\frac{1}{3!}{x}^{2} + \frac{1}{5!}{x}^{4} - \frac{1}{7!}{x}^{6}}\right)  - \frac{1}{2}\left( {\frac{1}{36}{x}^{4} - \frac{2}{3!5!}{x}^{6}}\right)  + \frac{1}{3}\left( {-\frac{1}{216}{x}^{6}}\right)  + o\left( {x}^{7}\right)
\]

\[
=  - \frac{1}{6}{x}^{2} - \frac{1}{180}{x}^{4} - \frac{1}{2835}{x}^{6} + o\left( {x}^{7}\right) \left( {x \rightarrow  0}\right) .
\]

例题 7.2.4 设已知函数 (参考图 4.1)

\[
f\left( x\right)  = \left\{  \begin{array}{ll} {\left( 1 + x\right) }^{\frac{1}{x}}, & x \neq  0, \\  \mathrm{e}, & x = 0 \end{array}\right.
\]

在 \( x = 0 \) 无穷次可微,计算 \( f\left( x\right) \) 的 Maclaurin 公式直到 \( {x}^{4} \) 项.

解 在 \( x \neq  0 \) 时,将函数 \( f \) 写为

\[
f\left( x\right)  = \exp \left( {\ln f\left( x\right) }\right) ,
\]

然后写出

\[
\ln f\left( x\right)  = \frac{\ln \left( {1 + x}\right) }{x} = 1 - \frac{x}{2} + \frac{{x}^{2}}{3} - \frac{{x}^{3}}{4} + \frac{{x}^{4}}{5} + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) .
\]

将上式右边记为 \( 1 + y \) ,就有

\[
f\left( x\right)  = {\mathrm{e}}^{1 + y} = \mathrm{e} \cdot  {\mathrm{e}}^{y} = \mathrm{e}\left( {1 + y + \frac{{y}^{2}}{2!} + \frac{{y}^{3}}{3!} + \frac{{y}^{4}}{4!}}\right)  + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) ,
\]

其中

\[
y =  - \frac{x}{2} + \frac{{x}^{2}}{3} - \frac{{x}^{3}}{4} + \frac{{x}^{4}}{5} + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) .
\]

分别计算出

\[
{y}^{2} = \frac{1}{4}{x}^{2} - \frac{1}{3}{x}^{3} + \frac{13}{36}{x}^{4} + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) ,
\]

\[
{y}^{3} =  - \frac{1}{8}{x}^{3} + \frac{1}{4}{x}^{4} + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) ,
\]

\[
{y}^{4} = \frac{1}{16}{x}^{4} + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) ,
\]

代入前面的表达式中, 最后得到

\[
f\left( x\right)  = \mathrm{e}\left( {1 - \frac{1}{2}x + \frac{11}{24}{x}^{2} - \frac{7}{16}{x}^{3} + \frac{2447}{5760}{x}^{4}}\right)  + o\left( {x}^{4}\right) \left( {x \rightarrow  0}\right) .
\]

注 在上面两个例题中都没有验证函数在 \( {x}_{0} = 0 \) 处存在任意阶导数. 这是在使用间接法时经常会遇到的问题. 实际上这里涉及与幂级数(或解析函数)的四则运算和复合运算有关的一些理论问题, 在学幂级数之前作讨论是比较困难的. 因此在例题和练习题中我们将注意力集中在计算上，而将有关的理论问题留待以后解决. 此外,这里还从 \( \sin x \) 和 \( \ln \left( {1 + x}\right) \) 的 Maclaurin 公式出发除以 \( x \) ,得到函数 \( \frac{\sin x}{x} \) 和 \( \frac{\ln \left( {1 + x}\right) }{x} \) (在 \( x = 0 \) 处由极限定义) 的 Maclaurin 公式,这里的理论根据可在下一章得到解决 (见例题 8.1.9 的第 3 个注解). (对此有兴趣的读者还可以参考 [73] 中对于这些问题的严格处理.)

例题 7.2.5 设 \( f \) 在 \( \left( {0, + \infty }\right) \) 上二阶可微,且已知

\[
{M}_{0} = \sup \{ \left| {f\left( x\right) }\right|  \mid  x \in  \left( {0, + \infty }\right) \} \text{ 和 }{M}_{2} = \sup \left\{  {\left| {{f}^{\prime \prime }\left( x\right) }\right|  \mid  x \in  \left( {0, + \infty }\right) }\right\}
\]

为有限数. 证明 \( {M}_{1} = \sup \left\{  {\left| {{f}^{\prime }\left( x\right) }\right|  \mid  x \in  \left( {0, + \infty }\right) }\right\} \) 也是有限数,并满足不等式

\[
{M}_{1} \leq  2\sqrt{{M}_{0}{M}_{2}}
\]

证 写出

\[
f\left( {x + t}\right)  = f\left( x\right)  + {f}^{\prime }\left( x\right) t + \frac{{f}^{\prime \prime }\left( \xi \right) }{2}{t}^{2},
\]

其中 \( x, t > 0,\xi  \in  \left( {x, x + t}\right) \) . 由此有估计

\[
\left| {t{f}^{\prime }\left( x\right) }\right|  \leq  \left| {f\left( {x + t}\right)  - f\left( x\right)  - \frac{{t}^{2}}{2}{f}^{\prime \prime }\left( \xi \right) }\right|  \leq  2{M}_{0} + \frac{{t}^{2}}{2}{M}_{2}.
\]

这样就得到

\[
\left| {{f}^{\prime }\left( x\right) }\right|  \leq  \frac{2{M}_{0}}{t} + \frac{t}{2}{M}_{2}.
\]

这对每个 \( x \in  \left( {0, + \infty }\right) \) 成立. 取上确界,就有

\[
{M}_{1} \leq  \frac{2{M}_{0}}{t} + \frac{t}{2}{M}_{2} \tag{7.24}
\]

因此 \( {M}_{1} \) 为有限数. 由于这对每个 \( t > 0 \) 成立,为了得到最好的估计,可以取 \( t = 2\sqrt{{M}_{0}/{M}_{2}} \) ,使右边的和达到最小,即有

\[
{M}_{1} \leq  2\sqrt{{M}_{0}{M}_{2}}
\]

注 本题有许多推广和研究, 例如见本章的第一组参考题 17、第二组参考题 15 等. 比较详细的资料见 [30].

例题 7.2.6 设 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上二阶可微. 证明: 存在 \( \xi  \in  \left( {a, b}\right) \) ,使得

\[
f\left( a\right)  - {2f}\left( \frac{a + b}{2}\right)  + f\left( b\right)  = \frac{1}{4}{\left( b - a\right) }^{2}{f}^{\prime \prime }\left( \xi \right) .
\]

证 写出 \( f\left( a\right) , f\left( b\right) \) 在点 \( \frac{a + b}{2} \) 的 Taylor 展开式:

\[
f\left( a\right)  = f\left( \frac{a + b}{2}\right)  + {f}^{\prime }\left( \frac{a + b}{2}\right) \left( \frac{a - b}{2}\right)  + \frac{1}{2}{f}^{\prime \prime }\left( {\eta }_{1}\right) {\left( \frac{b - a}{2}\right) }^{2},
\]

\[
f\left( b\right)  = f\left( \frac{a + b}{2}\right)  + {f}^{\prime }\left( \frac{a + b}{2}\right) \left( \frac{b - a}{2}\right)  + \frac{1}{2}{f}^{\prime \prime }\left( {\eta }_{2}\right) {\left( \frac{b - a}{2}\right) }^{2},
\]

然后将两式相加, 就有

\[
f\left( a\right)  - {2f}\left( \frac{a + b}{2}\right)  + f\left( b\right)  = \frac{1}{8}{\left( b - a\right) }^{2}\left\lbrack  {{f}^{\prime \prime }\left( {\eta }_{1}\right)  + {f}^{\prime \prime }\left( {\eta }_{2}\right) }\right\rbrack  .
\]

对 \( {f}^{\prime \prime } \) 用 Darboux 定理 (命题 7.1.6),即有 \( \xi  \in  \left( {a, b}\right) \) ,使得

\[
{f}^{\prime \prime }\left( \xi \right)  = \frac{1}{2}\left\lbrack  {{f}^{\prime \prime }\left( {\eta }_{1}\right)  + {f}^{\prime \prime }\left( {\eta }_{2}\right) }\right\rbrack  .
\]

注 本题的证明方法很多, 除了用 Taylor 公式为主要工具的上述证明外, 这里再简述两种证明方法.

1. 令 \( \lambda  = \frac{f\left( a\right)  + f\left( b\right)  - {2f}\left( \frac{a + b}{2}\right) }{\frac{{\left( b - a\right) }^{2}}{4}} \) ,构造辅助函数

\[
F\left( t\right)  = f\left( t\right)  + f\left( a\right)  - {2f}\left( \frac{t + a}{2}\right)  - \lambda \frac{{\left( t - a\right) }^{2}}{4},
\]

以下与例题 7.1.3 相同.

2. 作辅助函数

\[
\varphi \left( x\right)  = f\left( {x + \frac{b - a}{2}}\right)  - f\left( x\right) ,
\]

然后考虑差 \( \varphi \left( \frac{a + b}{2}\right)  - \varphi \left( a\right) \) .

#### 7.2.3 Euler 数与 Bernoulli 数

在初等函数的 Taylor 展开式中有几个例子,如 \( \sec x \) 和 \( \tan x \) ,一般难以求出通式. 原因在于其中出现了著名的 Euler 数和 Bernoulli 数.

例题 7.2.7 计算 \( \sec x \) 的 Maclaurin 展开式.

解 由于 \( \sec x \) 是偶函数，可以假定有

\[
\sec x = {c}_{0} + {c}_{2}{x}^{2} + {c}_{4}{x}^{4} + \cdots  + {c}_{2n}{x}^{2n} + o\left( {x}^{{2n} + 1}\right) \left( {x \rightarrow  0}\right) .
\]

现在令

\[
{c}_{2n} = {\left( -1\right) }^{n}\frac{{E}_{2n}}{\left( {2n}\right) !}, n \in  {\mathbf{N}}_{ + },
\]

写出

\[
\sec x = {E}_{0} - \frac{{E}_{2}}{2!}{x}^{2} + \frac{{E}_{4}}{4!}{x}^{4} + \cdots  + {\left( -1\right) }^{n}\frac{{E}_{2n}}{\left( {2n}\right) !}{x}^{2n} + o\left( {x}^{{2n} + 1}\right) \left( {x \rightarrow  0}\right) . \tag{7.25}
\]

将公式 (7.25) 和 \( \cos x \) 的 Maclaurin 公式一起代入恒等式 \( \cos x\sec x \equiv  1 \) 中,就可以得到确定数列 \( \left\{  {E}_{2n}\right\} \) 的递推公式:

\[
{E}_{0} = 1,{E}_{2} + {E}_{0} = 1,{E}_{4} + \frac{4!}{2!2!}{E}_{2} + {E}_{0} = 0,
\]

............

\[
{E}_{2n} + \left( \begin{matrix} {2n} \\  2 \end{matrix}\right) {E}_{{2n} - 2} + \left( \begin{matrix} {2n} \\  4 \end{matrix}\right) {E}_{{2n} - 4} + \cdots  + {E}_{0} = 0.
\]

从而可以得出

\[
{E}_{2} =  - 1,{E}_{4} = 5,{E}_{6} =  - {61},{E}_{8} = {1385},{E}_{10} =  - {50521},\cdots .
\]

例如, 这样就可以写出直到前 6 项系数的公式:

\[
\sec x = 1 + \frac{{x}^{2}}{2} + \frac{5}{24}{x}^{4} + \frac{61}{720}{x}^{6} + \frac{277}{8064}{x}^{8} + \frac{50521}{3628800}{x}^{10} + o\left( {x}^{11}\right) \left( {x \rightarrow  0}\right) .
\]

称 \( {E}_{2n} \) 为 Euler 数. 当 \( n \) 为偶数时, \( {E}_{2n} \) 为正奇数,且除 \( {E}_{0} \) 外,其个位数字都是 5 ; 当 \( n \) 为奇数时, \( {E}_{2n} \) 为负奇数,其个位数字都是 1 .

注 1 又有

\[
\operatorname{sech}x = \frac{2}{{\mathrm{e}}^{x} + {\mathrm{e}}^{-x}} = {E}_{0} + \frac{{E}_{2}}{2!}{x}^{2} + \cdots  + \frac{{E}_{2n}}{\left( {2n}\right) !}{x}^{2n} + o\left( {x}^{{2n} + 1}\right) \left( {x \rightarrow  0}\right) ,
\]

其中的函数 \( \operatorname{sech}x \) 称为双曲正割.

注 2 令 \( {E}_{2n} = {\left( -1\right) }^{n}{\bar{E}}_{n} \) ,也有将 \( {\bar{E}}_{n} \) 称为 Euler 数的.

Bernoulli 数是 Jacob Bernoulli 研究前 \( n \) 个正整数的 \( p \) 次方幂之和

\[
{1}^{p} + {2}^{p} + {3}^{p} + \cdots  + {n}^{p}
\]

的计算公式时得到的 (其原文的中译文见 [35] 的 299-302 页). 对于 \( p = 1,2,3 \) 的公式,学生在中学里都已经知道. Jacob Bernoulli 的目的是要对一切正整数 \( p \) 求出一般的计算公式. 他发现

\[
{1}^{p} + {2}^{p} + \cdots  + {n}^{p} = \frac{1}{p + 1}{n}^{p + 1} + \frac{1}{2}{n}^{p} + \frac{p}{2}A{n}^{p - 1} + \frac{p\left( {p - 1}\right) \left( {p - 2}\right) }{4!}B{n}^{p - 3}
\]

\[
+ \frac{p\left( {p - 1}\right) \left( {p - 2}\right) \left( {p - 3}\right) \left( {p - 4}\right) }{6!}C{n}^{p - 5} + \cdots ,
\]

其中右边的项直写到 \( n \) 或 \( {n}^{2} \) 项为止. 公式中出现的常数

\[
A = \frac{1}{6}, B =  - \frac{1}{30}, C = \frac{1}{42},\cdots
\]

就是 Bernoulli 数.

以下采用目前的标准方法来引入 Bernoulli 数. 考虑计算函数

\[
f\left( x\right)  = \left\{  \begin{array}{ll} \frac{x}{{\mathrm{e}}^{x} - 1}, & x \neq  0, \\  1, & x = 0 \end{array}\right.
\]

的 Maclaurin 展开式. 令

\[
f\left( x\right)  = {B}_{0} + \frac{{B}_{1}}{1!}x + \frac{{B}_{2}}{2!}{x}^{2} + \cdots  + \frac{{B}_{n}}{n!}{x}^{n} + o\left( {x}^{n}\right) \left( {x \rightarrow  0}\right) ,
\]

并将它代入恒等式

\[
f\left( x\right)  \cdot  \frac{{\mathrm{e}}^{x} - 1}{x} = f\left( x\right) \left\lbrack  {1 + \frac{x}{2!} + \frac{{x}^{2}}{3!} + \cdots  + \frac{{x}^{n}}{\left( {n + 1}\right) !} + o\left( {x}^{n}\right) }\right\rbrack   \equiv  1
\]

中，就可以得到确定数列 \( \left\{  {B}_{n}\right\} \) 的递推公式:

\[
{B}_{0} = 1,\frac{1}{2!}{B}_{0} + {B}_{1} = 0,\frac{1}{3!}{B}_{0} + \frac{1}{2!1!}{B}_{1} + \frac{1}{2!}{B}_{2} = 0,
\]

............

\[
\left( \begin{array}{l} n \\  0 \end{array}\right) {B}_{0} + \left( \begin{array}{l} n \\  1 \end{array}\right) {B}_{1} + \left( \begin{array}{l} n \\  2 \end{array}\right) {B}_{2} + \cdots  + \left( \begin{matrix} n \\  n - 1 \end{matrix}\right) {B}_{n - 1} = 0.
\]

从而可以得出

\[
{B}_{1} =  - \frac{1}{2},{B}_{2} = \frac{1}{6},{B}_{4} =  - \frac{1}{30},{B}_{6} = \frac{1}{42},{B}_{8} =  - \frac{1}{30},
\]

\[
{B}_{10} = \frac{5}{66},{B}_{12} =  - \frac{691}{2730},{B}_{14} = \frac{7}{6},\cdots ,
\]

当 \( n \) 为大于 1 的奇数时 \( {B}_{n} = 0 \) .

注 令 \( {B}_{2n} = {\left( -1\right) }^{n - 1}{\bar{B}}_{n}\left( {n \geq  1}\right) \) ,也有称 \( {\bar{B}}_{n} \) 为 Bernoulli 数的. 注意所有 \( {\bar{B}}_{n} > 0 \)

例题 7.2.8 计算 \( x\cot x \) 的 Maclaurin 展开式,在 \( x = 0 \) 处的函数值补充定义为 1 .

解 以下运算越出了实数的范围,还用到了 Euler 公式 \( {\mathrm{e}}^{\mathrm{i}x} = \cos x + \mathrm{i}\sin x \) ,其合理性将在复变函数论中得到解释.

\[
x\cot x = x \cdot  \frac{\cos x}{\sin x} = \mathrm{i}x \cdot  \frac{{\mathrm{e}}^{\mathrm{i}x} + {\mathrm{e}}^{-\mathrm{i}x}}{{\mathrm{e}}^{\mathrm{i}x} - {\mathrm{e}}^{-\mathrm{i}x}} = \mathrm{i}x + \frac{2\mathrm{i}x}{{\mathrm{e}}^{2\mathrm{i}x} - 1}
\]

\[
= \mathrm{i}x + {B}_{0} + \frac{{B}_{1}}{1!}2\mathrm{i}x + \frac{{B}_{2}}{2!}{\left( 2\mathrm{i}x\right) }^{2} + \cdots  + \frac{{B}_{2n}}{\left( {2n}\right) !}{\left( 2\mathrm{i}x\right) }^{2n} + o\left( {x}^{2n}\right)
\]

\[
= \operatorname{Re}\left\lbrack  {\mathrm{i}x + {B}_{0} + \frac{{B}_{1}}{1!}2\mathrm{i}x + \frac{{B}_{2}}{2!}{\left( 2\mathrm{i}x\right) }^{2} + \cdots  + \frac{{B}_{2n}}{\left( {2n}\right) !}{\left( 2\mathrm{i}x\right) }^{2n} + o\left( {x}^{2n}\right) }\right\rbrack
\]

\[
= 1 - \frac{{\bar{B}}_{1}{2}^{2}}{2!}{x}^{2} - \frac{{\bar{B}}_{2}{2}^{4}}{4!}{x}^{4} + \cdots  - \frac{{\bar{B}}_{n}{2}^{2n}}{\left( {2n}\right) !}{x}^{2n} + o\left( {x}^{{2n} + 1}\right) \left( {x \rightarrow  0}\right) .
\]

写出其前 5 项的系数，即有

\[
x\cot x = 1 - \frac{1}{3}{x}^{2} - \frac{1}{45}{x}^{4} - \frac{2}{945}{x}^{6} - \frac{1}{4725}{x}^{8} + o\left( {x}^{9}\right) \left( {x \rightarrow  0}\right) .
\]

例题 7.2.9 计算函数 \( \tan x \) 的 Maclaurin 展开式.

解 利用恒等式 \( \tan x = \cot x - 2\cot {2x} \) ,当 \( x = 0 \) 时将右边取其极限 0 . 这样就有

\[
\tan x = \frac{x\cot x - {2x}\cot {2x}}{x}
\]

\[
= \frac{{\bar{B}}_{1}\left( {{2}^{2} - 1}\right) {2}^{2}}{2!}x + \frac{{\bar{B}}_{2}\left( {{2}^{4} - 1}\right) {2}^{4}}{4!}{x}^{3} + \cdots
\]

\[
+ \frac{{\bar{B}}_{n}\left( {{2}^{2n} - 1}\right) {2}^{2n}}{\left( {2n}\right) !}{x}^{{2n} - 1} + o\left( {x}^{2n}\right) \left( {x \rightarrow  0}\right) .
\]

写出其前 5 项的系数, 即有

\[
\tan x = x + \frac{1}{3}{x}^{3} + \frac{2}{15}{x}^{5} + \frac{17}{315}{x}^{7} + \frac{62}{2835}{x}^{9} + o\left( {x}^{10}\right) \left( {x \rightarrow  0}\right) .
\]

这样的例子还有很多,例如在 \( x\csc x,\ln \cos x,\ln \left( {\sin x/x}\right) \) 的 Maclaurin 公式中都出现 Bernoulli 数. 此外, Bernoulli 数还出现在以下无穷级数的求和公式中:

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2k}} = \frac{{\bar{B}}_{k}}{2} \cdot  \frac{{\left( 2\pi \right) }^{2k}}{\left( {2k}\right) !} \tag{7.26}
\]

其中 \( k \) 为正整数. 这个公式可以从例题 7.2.8 的结果得到 (见《数学译林》(1991) 第 10 期 348 页). 从第二章 2.3.2 小节的题 6 已经知道, 无穷级数

\[
1 + \frac{1}{{2}^{p}} + \frac{1}{{3}^{p}} + \cdots  + \frac{1}{{n}^{p}} + \cdots
\]

在 \( p > 1 \) 时收敛. 公式 (7.26) 给出了当 \( p = {2k} \) 为偶数时的求和公式. 它是 Euler 发现的. 公式 (7.26) 的证明见本书下册的例题 16.2.3.

当 \( k = 1 \) 时就可从公式 (7.26) 得到数学分析中的一个重要结果:

\[
\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{1}{{n}^{2}} = 1 + \frac{1}{4} + \frac{1}{9} + \cdots  + \frac{1}{{n}^{2}} + \cdots  = \frac{{\pi }^{2}}{6}.
\]

求这个级数和就是所谓的 Basel 问题. 在 Euler 之前没有人想到它的答案中会出现圆周率 \( \pi \) . 有兴趣的读者可以从 [12] 的第九章中了解与此有关的故事.

在积分学的积分近似计算和 Stirling 公式中我们还会遇到 Bernoulli 数 (见 11.3.2 和 11.4.2 小节).

#### 7.2.4 练习题

1. 计算 \( x\csc x,\ln \cos x,\ln \left( \frac{\sin x}{x}\right) \) 的 Maclaurin 公式.

2. 能否用 Taylor 公式作如下计算:

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\sin x}{x} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{x + o\left( {x}^{2}\right) }{x} = 1
\]

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \cos x}{{x}^{2}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \left( {1 - \frac{1}{2}{x}^{2} + o\left( {x}^{3}\right) }\right) }{{x}^{2}} = \frac{1}{2},
\]

为什么?

3. 试对函数 \( f\left( x\right)  = {\left( x + a\right) }^{n}\left( {a \neq  0}\right) \) 和 \( {x}_{0} = 0 \) 计算它的 Taylor 多项式,从而得到二项式展开定理的一个新证明.

4. 设 \( f \) 在 \( {x}_{0} \) 处存在 \( {f}^{\left( n\right) }\left( {x}_{0}\right) \) ,且有 \( f\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{\left( x - {x}_{0}\right) }^{k} + o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) \) , 证明: \( {f}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {k + 1}\right) {a}_{k + 1}{\left( x - {x}_{0}\right) }^{k} + o\left( {\left( x - {x}_{0}\right) }^{n - 1}\right) \left( {x \rightarrow  {x}_{0}}\right) \) .

5. 用间接法求函数 \( f\left( x\right)  = \sqrt[3]{\sin {x}^{3}} \) 的带 Peano 余项的 Maclaurin 公式,要求写出直到 \( {x}^{13} \) 项的系数. 然后利用这个公式计算出函数 \( f\left( x\right) \) 在点 \( x = 0 \) 的直到 13 阶的各阶导数值.

6. 计算 \( \arcsin x \) 的带 Peano 余项的 Maclaurin 公式.

7. 计算 \( f\left( x\right)  = \frac{\arcsin x}{\sqrt{1 - {x}^{2}}} \) 的带 Peano 余项的 Maclaurin 公式.

8. 估计下列近似公式的绝对误差:

(1) \( {\mathrm{e}}^{x} \approx  1 + x + \frac{{x}^{2}}{2!} + \cdots  + \frac{{x}^{n}}{n!} \) ,当 \( 0 \leq  x \leq  1 \) ;

(2) \( \sin x \approx  x - \frac{{x}^{3}}{6} \) ，当 \( \left| x\right|  \leq  \frac{1}{2} \) ；

(3) \( \tan x \approx  x + \frac{{x}^{3}}{3} \) ,当 \( \left| x\right|  \leq  \frac{1}{10} \) ;

(4) \( \sqrt{1 + x} \approx  1 + \frac{x}{2} - \frac{{x}^{2}}{8} \) ,当 \( 0 \leq  x \leq  1 \) .

9. 若函数 \( f \) 在某点 \( {x}_{0} \) 的任意阶 Taylor 多项式均恒等于 0,是否可推出 \( f\left( x\right)  \equiv  0 \) ? (参考例题 6.2.4 的结论.)

10. 设 \( f \) 在 \( \left\lbrack  {-1,1}\right\rbrack \) 上有任意阶导数, \( {f}^{\left( n\right) }\left( 0\right)  = 0,\forall n \in  {\mathbf{N}}_{ + } \) ,且存在常数 \( C \geq  0 \) ,使得对所有 \( n \in  {\mathbf{N}}_{ + } \) 和 \( x \in  \left\lbrack  {-1,1}\right\rbrack \) 成立不等式 \( \left| {{f}^{\left( n\right) }\left( x\right) }\right|  \leq  n!{C}^{n} \) . 证明: \( f\left( x\right)  \equiv  0 \) .

11. 设 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上二阶可微,且 \( {f}^{\prime }\left( a\right)  = {f}^{\prime }\left( b\right)  = 0 \) . 证明: 存在 \( \xi  \in  \left( {a, b}\right) \) ,使得成立

\[
\left| {{f}^{\prime \prime }\left( \xi \right) }\right|  \geq  \frac{4}{{\left( b - a\right) }^{2}}\left| {f\left( b\right)  - f\left( a\right) }\right| .
\]

12. (1) 设 \( f \) 在 \( \left( {a, b}\right) \) 上可微. 试问对每个点 \( \xi  \in  \left( {a, b}\right) \) ,是否一定存在两个点 \( {x}_{1},{x}_{2} \in  \left( {a, b}\right) \) ,使得

\[
\frac{f\left( {x}_{2}\right)  - f\left( {x}_{1}\right) }{{x}_{2} - {x}_{1}} = {f}^{\prime }\left( \xi \right) ?
\]

(2) 设 \( f \) 在 \( \left( {a, b}\right) \) 上可微,且在某点 \( \xi  \in  \left( {a, b}\right) \) 处有 \( {f}^{\prime \prime }\left( \xi \right)  > 0 \) . 证明: 存在两个点 \( {x}_{1},{x}_{2} \in  \left( {a, b}\right) \) ,使得成立

\[
\frac{f\left( {x}_{2}\right)  - f\left( {x}_{1}\right) }{{x}_{2} - {x}_{1}} = {f}^{\prime }\left( \xi \right) .
\]

13. 设 \( f \) 在 \( \lbrack a, + \infty ) \) 上二阶可微,且 \( f\left( x\right)  \geq  0,{f}^{\prime \prime }\left( x\right)  \leq  0 \) ,证明: 在 \( x \geq  a \) 时 \( {f}^{\prime }\left( x\right)  \geq  0 \)

14. 设 \( f \) 在 \( \left( {-1,1}\right) \) 上 \( n + 1 \) 阶可微, \( {f}^{\left( n + 1\right) }\left( 0\right)  \neq  0, n \in  {\mathbf{N}}_{ + } \) ,在 \( 0 < \left| x\right|  < 1 \) 上有

\[
f\left( x\right)  = f\left( 0\right)  + {f}^{\prime }\left( 0\right) x + \cdots  + \frac{{f}^{\left( n - 1\right) }\left( 0\right) }{\left( {n - 1}\right) !}{x}^{n - 1} + \frac{{f}^{\left( n\right) }\left( {\theta x}\right) }{n!}{x}^{n},
\]

其中 \( 0 < \theta  < 1 \) ,证明: \( \mathop{\lim }\limits_{{x \rightarrow  0}}\theta  = \frac{1}{n + 1} \) .

15. 证明: 在 \( \left| x\right|  \leq  1 \) 时存在 \( \theta  \in  \left( {0,1}\right) \) ,使得 \( \arcsin x = \frac{x}{\sqrt{1 - {\left( \theta x\right) }^{2}}} \) ,且有

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\theta  = \frac{1}{\sqrt{3}}
\]

16. 设 \( f \) 在 \( {O}_{\delta }\left( {x}_{0}\right) \) 上 \( n \) 阶可微,且 \( {f}^{\prime \prime }\left( {x}_{0}\right)  = \cdots  = {f}^{\left( n - 1\right) }\left( {x}_{0}\right)  = 0,{f}^{\left( n\right) }\left( {x}_{0}\right)  \neq  0 \) . 证明: 当 \( 0 < \left| h\right|  < \delta \) 时,成立 \( f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right)  = h{f}^{\prime }\left( {{x}_{0} + {\theta h}}\right) ,0 < \theta  < 1 \) ,且成立

\[
\mathop{\lim }\limits_{{h \rightarrow  0}}\theta  = \frac{1}{{n}^{\frac{1}{n - 1}}}
\]
