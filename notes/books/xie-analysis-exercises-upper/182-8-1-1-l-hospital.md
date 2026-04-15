#### 8.1.1 L'Hospital 法则

从数学分析的学习开始, 极限计算就是一大难题. 这种状况在有了 L'Hospital 法则后才可以说有了根本的改变. 由于这个法则将求不定式极限归之于简单的导数计算, 而且 (在条件满足时) 可以连续使用, 许多看似复杂的问题就可迎刃而解. 关于 L'Hospital 法则的叙述、证明以及应用时的注意事项等在数学分析的教科书中都有详细的介绍,其基本思想又与 \( \text{ § }{2.4} \) 完全相同,这里不再重复 \( {}^{ \oplus  } \) . 因同样的理由, 也不准备举很多常规性的例题和练习题.

这里只强调指出一点, 即虽然 L'Hospital 法则确实是计算极限的强有力工具, 但毕竟“一花独放不是春”, 初学者要学会将 L'Hospital 法则的使用与其他工具相结合, 这样才能有更好的效果. 这里所说的其他工具包括在前面各章中已经介绍的多种方法，如等价量代换法、变量代换法、不定式因子的分离、各种恒等变换、无穷小增量公式等, 也包括在下一小节将要介绍的带 Peano 余项的 Taylor 公式等. 总之, 若初学者在用 L'Hospital 法则时出现复杂的计算或甚至失败, 原因往往不是 L'Hospital 法则不好, 而是你对于它的认识有误. 不要认为既然 L'Hospital 法则这样有力，那么其他(已经学过的)方法都可以不要了.

先看下面几个简单问题, 它们在第四章中很难解决, 现在用 L'Hospital 法则来做就成为容易的问题了 (回顾那里的例题 4.4.5). 但从下面又可看出, 这里也需要与其他工具结合.

---

① L'Hospital 法则的一个精彩的几何证明见 [59] 第一册的命题 2.10.

---

例题 8.1.1 计算极限 \( \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\sin x - x}{{x}^{3}} \) .

解 用 L'Hospital 法则可计算如下:

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\sin x - x}{{x}^{3}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\cos x - 1}{3{x}^{2}} =  - \frac{1}{6}.
\]

最后一步利用了已知的等价关系 \( 1 - \cos x \sim  \frac{1}{2}{x}^{2}\left( {x \rightarrow  0}\right) \) .

例题 8.1.2 计算极限 \( \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{x - \tan x}{{x}^{3}} \) .

解 1 不用其他工具, 连用三次 L'Hospital 法则就可以解决问题:

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{x - \tan x}{{x}^{3}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - {\sec }^{2}x}{3{x}^{2}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{-2{\sec }^{2}x\tan x}{6x}
\]

\[
=  - \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{2{\sec }^{2}x{\tan }^{2}x + {\sec }^{4}x}{3} =  - \frac{1}{3}.
\]

解 2 实际上用一次 L'Hospital 法则就够了:

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{x - \tan x}{{x}^{3}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - {\sec }^{2}x}{3{x}^{2}} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{-{\tan }^{2}x}{3{x}^{2}} =  - \frac{1}{3}.
\]

再举一个有多种解法的例子.

例题 8.1.3 计算 \( \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \cos {x}^{2}}{{x}^{3}\sin x} \) .

解 1 直接用 L'Hospital 法则三次, 得到

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \cos {x}^{2}}{{x}^{3}\sin x} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{2\sin {x}^{2}}{{3x}\sin x + {x}^{2}\cos x} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{{4x}\cos {x}^{2}}{\left( {3 - {x}^{2}}\right) \sin x + {5x}\cos x}
\]

\[
= \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{4\cos {x}^{2} - 8{x}^{2}\sin {x}^{2}}{\left( {8 - {x}^{2}}\right) \cos x - {7x}\sin x} = \frac{1}{2}.
\]

解 2 实际上不需要微分学知识, 用等价量代换法即可解决:

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \cos {x}^{2}}{{x}^{3}\sin x} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{2{\sin }^{2}\frac{{x}^{2}}{2}}{{x}^{3}\sin x}
\]

\[
= \mathop{\lim }\limits_{{x \rightarrow  0}}{\left( \frac{\sin \frac{{x}^{2}}{2}}{\frac{{x}^{2}}{2}}\right) }^{2} \cdot  \left( \frac{x}{2\sin x}\right)  = \frac{1}{2}.
\]

解 3 若利用当 \( x \rightarrow  0 \) 时成立 \( \cos {x}^{2} = 1 - \frac{{\left( {x}^{2}\right) }^{2}}{2} + o\left( {\left( {x}^{2}\right) }^{2}\right) \) 和 \( \sin x = x + o\left( x\right) \) , 则就有

\[
\mathop{\lim }\limits_{{x \rightarrow  0}}\frac{1 - \cos {x}^{2}}{{x}^{3}\sin x} = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\frac{{x}^{4}}{2} + o\left( {x}^{4}\right) }{{x}^{3}\left( {x + o\left( x\right) }\right) } = \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\frac{{x}^{4}}{2} + o\left( {x}^{4}\right) }{{x}^{4} + o\left( {x}^{4}\right) }
\]

\[
= \mathop{\lim }\limits_{{x \rightarrow  0}}\frac{\frac{1}{2} + o\left( 1\right) }{1 + o\left( 1\right) } = \frac{1}{2}.
\]

下面是在 \( \text{ § }{2.5} \) 计算数 e 时留下的问题,即证明公式 (2.15) 中的等价关系.

例题 8.1.4 设 \( {\delta }_{n} = \mathrm{e} - {\left( 1 + \frac{1}{n}\right) }^{n} \) ,计算极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n{\delta }_{n} \) .

解 根据第四章的 Heine 归结原理 (即命题 4.2.3), 只要计算函数极限

\[
\mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{\mathrm{e} - {\left( 1 + x\right) }^{\frac{1}{x}}}{x}.
\]

这是 \( \frac{0}{0} \) 型的不定式问题. 用 L’Hospital 法则,得到

\[
\mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{\mathrm{e} - {\left( 1 + x\right) }^{\frac{1}{x}}}{x} = \mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\left\{  {-\left\lbrack  {\left( 1 + x\right) }^{\frac{1}{x}}\right\rbrack   \cdot  \frac{\frac{x}{1 + x} - \ln \left( {1 + x}\right) }{{x}^{2}}}\right\}
\]

\[
=  - \mathrm{e} \cdot  \mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{\frac{x}{1 + x} - \ln \left( {1 + x}\right) }{{x}^{2}}
\]

\[
=  - \mathrm{e} \cdot  \mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{\frac{1}{{\left( 1 + x\right) }^{2}} - \frac{1}{1 + x}}{2x}
\]

\[
=  - \mathrm{e} \cdot  \mathop{\lim }\limits_{{x \rightarrow  {0}^{ + }}}\frac{-1}{2{\left( 1 + x\right) }^{2}} = \frac{\mathrm{e}}{2}.
\]

注 实际上本题的答案就是例题 7.2.4 中的函数 \( f\left( x\right) \) 的导数 \( {f}^{\prime }\left( 0\right) \) (乘 -1 ).

用 L'Hospital 法则可以对带 Peano 余项的 Taylor 公式给出新证明.

例题 8.1.5 用 L’Hospital 法则证明: 若 \( f \) 在点 \( {x}_{0} \) 存在 \( {f}^{\left( n\right) }\left( {x}_{0}\right) \) ,则有

\[
f\left( x\right)  = f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots
\]

\[
+ \frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n} + o\left( {\left( x - {x}_{0}\right) }^{n}\right) \left( {x \rightarrow  {x}_{0}}\right) .
\]

证 如在第七章的 (7.19) 那样引进余项

\[
{r}_{n}\left( x\right)  = f\left( x\right)  - \left\lbrack  {f\left( {x}_{0}\right)  + {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)  + \frac{{f}^{\prime \prime }\left( {x}_{0}\right) }{2!}{\left( x - {x}_{0}\right) }^{2} + \cdots }\right.
\]

\[
\left. {+\frac{{f}^{\left( n\right) }\left( {x}_{0}\right) }{n!}{\left( x - {x}_{0}\right) }^{n}}\right\rbrack
\]

它满足以下的 \( n + 1 \) 个条件:

\[
{r}_{n}\left( {x}_{0}\right)  = 0,{r}_{n}^{\prime }\left( {x}_{0}\right)  = 0,\cdots ,{r}_{n}^{\left( n\right) }\left( {x}_{0}\right)  = 0. \tag{8.1}
\]

只需要证明 \( \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{{r}_{n}\left( x\right) }{{\left( x - {x}_{0}\right) }^{n}} = 0 \) ,这是 \( \frac{0}{0} \) 型的不定式. 用 L’Hospital 法则如下:

\[
\mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{{r}_{n}\left( x\right) }{{\left( x - {x}_{0}\right) }^{n}} = \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{{r}_{n}^{\prime }\left( x\right) }{n{\left( x - {x}_{0}\right) }^{n - 1}} = \cdots  = \mathop{\lim }\limits_{{x \rightarrow  {x}_{0}}}\frac{{r}_{n}^{\left( n - 1\right) }\left( x\right) }{n!\left( {x - {x}_{0}}\right) }.
\]

在以上的 \( n - 1 \) 次应用 L’Hospital 法则中,利用了 (8.1) 中的前 \( n - 1 \) 个条件. 从条件 \( {r}_{n}^{\left( n - 1\right) }\left( {x}_{0}\right)  = 0 \) 可见上面的最后一式仍然是 \( \frac{0}{0} \) 型的不定式. 但这里不能再用 L’Hospital 法则. 与命题 7.2.2 中一样,从导数定义出发,即可利用条件 \( {r}^{\left( n\right) }\left( {x}_{0}\right)  = 0 \) 得到所要求证的结果.
