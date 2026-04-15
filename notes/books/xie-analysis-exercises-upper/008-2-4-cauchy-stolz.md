## §2.4 Cauchy 命题与 Stolz 定理

求极限时困难往往在于处理不定式. 本节中介绍的几个命题就是处理 \( \frac{\infty }{\infty } \) 和 \( \frac{0}{0} \) 的有力工具. 其他类型的不定式往往可转化为这两种不定式.

应当指出, 本节的内容与单调有界数列的收敛定理无关. 从更一般的观点来看, 本节的结论和方法与实数系以及实数系的基本定理也没有关系. 因此在讲授时间的安排上有很大的灵活性. 这些内容往往可作为考研复习的起点.

#### 2.4.1 基本命题

由于以下几个命题中的证明方法很重要, 因此在列出命题的同时还给出完整的证明, 并在证明前后作一些分析, 以供读者参考.

命题 2.4.1 (Cauchy 命题) 设 \( \left\{  {x}_{n}\right\} \) 收敛于 \( l \) ,则它的前 \( n \) 项的算术平均值 (所成的数列) 也收敛于 \( l \) ,即有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} = l.
\]

分析 由于前面的各种方法, 包括夹逼定理、单调有界数列的收敛定理等, 对上述命题的证明似乎都用不上, 因此需要有新的方法.

直接观察表达式

\[
\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} \tag{2.7}
\]

可以想像,如果分子的每一项与 \( l \) 都充分接近,则它们的算术平均值也会与 \( l \) 充分接近. 由于 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = l \) ,只要令 \( \varepsilon  > 0 \) 充分小,则从某项 (即有 \( N \) ) 之后的每一项 (即 \( n > N \) 的所有 \( {x}_{n} \) ) 就会与 \( l \) 很接近,也就是满足要求 \( \left| {{x}_{n} - l}\right|  < \varepsilon \) . 因此可以将上述表达式分拆成两部分:

\[
\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} = \frac{{x}_{1} + \cdots  + {x}_{N}}{n} + \frac{{x}_{N + 1} + \cdots  + {x}_{n}}{n}. \tag{2.8}
\]

第二个分式中分子的每一项与 \( l \) 已充分接近. 由于一共有 \( n - N \) 项,如果分母不是 \( n \) ,而是 \( n - N \) ,则第二个分式的值就会与 \( l \) 充分接近了. 但这里并没有困难,因为由此引起的差异是一个小于 1 的因子 \( \left( {n - N}\right) /n \) ,且当 \( N \) 固定时,这个因子当 \( n \rightarrow  \infty \) 时的极限为 1 .

对于 (2.8) 右边的第一个分式, 可以看出, 由于我们对分子各项的大小完全不能控制,因此只有依靠分母 \( n \rightarrow  \infty \) .

于是在 (2.8) 中的两个分式的性质完全不同. 在取定 \( N \) 后只要取 \( n \) 充分大,第一部分的值将与 0 充分接近,而第二部分则与 \( l \) 充分接近.

但是为什么可以将 \( N \) 固定? 这里又需要回到极限的定义. 我们知道, \( N \) 虽然并不是 \( \varepsilon \) 的函数,但一般来说是与 \( \varepsilon \) 有关的. 如果 \( \varepsilon \) 取得越来越小,则一般来说相应的 \( N \) 就会越来越大. 然而对给定的一个 \( \varepsilon \) 而言,只要能取到一个 \( N \) 就够了. 为了证明表达式 (2.7) 的极限为 \( l \) ,根据极限定义,只要对于每个 \( \varepsilon  > 0 \) ,能有一个 \( N \) ,使得当 \( n > N \) 时该表达式与 \( l \) 之差的绝对值小于 \( \varepsilon \) 即可. 由分析可见,上面已取出的 \( N \) 是不够大的. 于是,我们可以在 \( N \) 的基础上再取更大的 \( {N}_{1} \) ,使得当 \( n > {N}_{1} \) 时 (2.7) 与 \( l \) 充分接近.

于是这里就发展出两步走的方法. 在这个方法中,先取 \( N \) 是必须的,否则就没有从 (2.7) 到 (2.8) 的分拆, 也无法控制第二项. 将它固定也是必须的, 否则就无法取出合乎要求的 \( {N}_{1} \) 去控制第一项.

根据以上分析, 我们可以写出证明如下.

证 根据条件 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = l \) ,可以对给定的 \( \varepsilon  > 0 \) 取定 \( N \) ,使得当 \( n > N \) 时成立 \( \left| {{x}_{n} - l}\right|  < \varepsilon \) . 然后可估计如下 (其中 \( n > N \) ):

\[
\left| {\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} - l}\right|  = \frac{\left| \left( {x}_{1} - l\right)  + \left( {x}_{2} - l\right)  + \cdots  + \left( {x}_{n} - l\right) \right| }{n}
\]

\[
\leq  \frac{\left| \left( {x}_{1} - l\right)  + \cdots  + \left( {x}_{N} - l\right) \right| }{n} + \frac{\left| {{x}_{N + 1} - l}\right|  + \cdots  + \left| {{x}_{n} - l}\right| }{n}
\]

\[
< \frac{M}{n} + \frac{n - N}{n}\varepsilon \tag{2.9}
\]

这里的 \( M = \left| {\left( {{x}_{1} - l}\right)  + \cdots  + \left( {{x}_{N} - l}\right) }\right| \) 是一个确定的数. 由此可见,只要取

\[
{N}_{1} = \max \left\{  {N,\left\lbrack  \frac{M}{\varepsilon }\right\rbrack  }\right\}  ,
\]

就保证当 \( n > {N}_{1} \) 时成立不等式

\[
\left| {\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} - l}\right|  < {2\varepsilon }.
\]

注 1 Cauchy命题中的证明方法非常有特色, 是极限理论中的基本方法之一. 回顾上面的分析和证明, 可以看出: 首先, 将 (2.7) 分成性质不同的两个部分是关键. (2.8) 中的第二个分式在 \( n \rightarrow  \infty \) (而 \( N \) 固定) 时的极限就是 \( l \) ,因此可以说是 “主要部分”, 而 (2.8) 中的第一个分式在这时为无穷小量, 因此可以说是 “次要部分”. 其次, 对这两个部分的处理方法是不同的, 可以说是 “分而治之”. 从最后写出的证明可见,只要对 \( \varepsilon  > 0 \) 取出 \( N \) ,就完成了对 (2.9) 的第二部分的估计. 但只有在取定 \( N \) 的基础上再取出 \( {N}_{1} \) 才能实现对 (2.9) 的第一部分的估计.

注 2 Cauchy 命题在数列 \( \left\{  {x}_{n}\right\} \) 为有确定符号的无穷大量时也是成立的 (这就是说在上述命题中的 \( l \) 可取为 \( + \infty \) 或 \( - \infty \) ). 读者应当至少对其中之一作出证明, 以此检验自己是否已经学会在 Cauchy 命题证明中的重要方法.

注 3 可以从数列变换的观点来理解 Cauchy 命题的意义. 这就是从 \( \left\{  {x}_{n}\right\} \) 出发构造出一个新数列,后者的通项,即第 \( n \) 项,是第一个数列的前 \( n \) 项的算术平均值. Cauchy 命题就是说当第一个数列收敛时，则第二个数列也收敛，且极限相同. 在极限理论中有以 Toeplitz (特普利茨) 定理 (见第二组参考题 10) 为代表的一系列命题, 它们都可以看成是 Cauchy 命题的推广, 即从一个数列变换为一个新数列, 然后讨论它们之间的敛散性关系. 这方面在 [48] 的第 I 篇第二章中有丰富的材料, 还可参考 [62] 的第 5 章和 [56] 等. 在本章的第二组参考题中也有几个题供训练用.

命题 \( {2.4.2}\left( \frac{0}{0}\right. \) 型的 Stolz 定理) 设 \( \left\{  {a}_{n}\right\} \) 和 \( \left\{  {b}_{n}\right\} \) 都是无穷小量,其中 \( \left\{  {a}_{n}\right\} \) 还是严格单调减少数列, 又存在

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{b}_{n + 1} - {b}_{n}}{{a}_{n + 1} - {a}_{n}} = l
\]

(其中 \( l \) 为有限或 \( \pm  \infty \) ),则有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{b}_{n}}{{a}_{n}} = l
\]

证 只对有限的 \( l \) 作证明. 根据条件对 \( \varepsilon  > 0 \) 存在 \( N \) ,使得当 \( n > N \) 时成立

\[
\left| {\frac{{b}_{n} - {b}_{n + 1}}{{a}_{n} - {a}_{n + 1}} - l}\right|  < \varepsilon
\]

由于对每个 \( n \) 都有 \( {a}_{n} > {a}_{n + 1} \) ,这样就有

\[
\left( {l - \varepsilon }\right) \left( {{a}_{n} - {a}_{n + 1}}\right)  < {b}_{n} - {b}_{n + 1} < \left( {l + \varepsilon }\right) \left( {{a}_{n} - {a}_{n + 1}}\right) .
\]

任取 \( m > n \) ,并且将上述不等式中的 \( n \) 换成 \( n + 1,\cdots \) ,直到 \( m - 1 \) ,然后将所有这些不等式相加, 就得到

\[
\left( {l - \varepsilon }\right) \left( {{a}_{n} - {a}_{m}}\right)  < {b}_{n} - {b}_{m} < \left( {l + \varepsilon }\right) \left( {{a}_{n} - {a}_{m}}\right) ,
\]

即

\[
\left| {\frac{{b}_{n} - {b}_{m}}{{a}_{n} - {a}_{m}} - l}\right|  < \varepsilon .
\]

令 \( m \rightarrow  \infty \) ,并利用条件 \( \mathop{\lim }\limits_{{m \rightarrow  \infty }}{a}_{m} = \mathop{\lim }\limits_{{m \rightarrow  \infty }}{b}_{m} = 0 \) ,就知道当 \( n > N \) 时成立

\[
\left| {\frac{{b}_{n}}{{a}_{n}} - l}\right|  \leq  \varepsilon
\]

命题 2.4.3 \( \left( \frac{ * }{\infty }\right. \) 型的 Stolz 定理) 设数列 \( \left\{  {a}_{n}\right\} \) 是严格单调增加的无穷大量, 又存在

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{b}_{n + 1} - {b}_{n}}{{a}_{n + 1} - {a}_{n}} = l
\]

(其中 \( l \) 为有限或 \( \pm  \infty \) ),则有

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{b}_{n}}{{a}_{n}} = l
\]

这个命题有时也称为 \( \frac{\infty }{\infty } \) 型的 Stolz 定理. 但从证明过程中可以发现实际上并不要求分子上的数列 \( \left\{  {b}_{n}\right\} \) 是无穷大量,因此这里称为 \( \frac{ * }{\infty } \) 型的 Stolz 定理. 这对于许多应用是很重要的.

证 只对 \( l \) 为有限的情况写出证明. 对 \( \varepsilon  > 0 \) 存在 \( N \) ,使得当 \( n \geq  N \) 时成立

\[
\left| {\frac{{b}_{n + 1} - {b}_{n}}{{a}_{n + 1} - {a}_{n}} - l}\right|  < \varepsilon .
\]

由于对每个 \( n \) 有 \( {a}_{n + 1} > {a}_{n} \) ,这样就有

\[
\left( {l - \varepsilon }\right) \left( {{a}_{n + 1} - {a}_{n}}\right)  < {b}_{n + 1} - {b}_{n} < \left( {l + \varepsilon }\right) \left( {{a}_{n + 1} - {a}_{n}}\right) .
\]

取定 \( N \) ,并且将上述不等式中的 \( n \) 换成 \( N, N + 1,\cdots \) ,直到 \( n - 1 \) ,然后将所有这些不等式相加, 就得到

\[
\left( {l - \varepsilon }\right) \left( {{a}_{n} - {a}_{N}}\right)  < {b}_{n} - {b}_{N} < \left( {l + \varepsilon }\right) \left( {{a}_{n} - {a}_{N}}\right) ,
\]

即

\[
\left| {\frac{{b}_{n} - {b}_{N}}{{a}_{n} - {a}_{N}} - l}\right|  < \varepsilon \tag{2.10}
\]

为了进一步得到关于 \( \left| {\frac{{b}_{n}}{{a}_{n}} - l}\right| \) 的估计,可以利用恒等式

\[
\frac{{b}_{n}}{{a}_{n}} - l = \left( {1 - \frac{{a}_{N}}{{a}_{n}}}\right)  \cdot  \left( {\frac{{b}_{n} - {b}_{N}}{{a}_{n} - {a}_{N}} - l}\right)  + \frac{{b}_{N} - l{a}_{N}}{{a}_{n}}. \tag{2.11}
\]

由于 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} =  + \infty \) ,存在 \( {N}_{1} \) ,使得当 \( n > {N}_{1} \) 时,成立

\[
0 < 1 - \frac{{a}_{N}}{{a}_{n}} < 2\text{ 和 }\left| \frac{{b}_{N} - l{a}_{N}}{{a}_{n}}\right|  < \varepsilon ,
\]

则在 \( n > \max \left\{  {N,{N}_{1}}\right\} \) 时就得到

\[
\left| {\frac{{b}_{n}}{{a}_{n}} - l}\right|  < {3\varepsilon }
\]

注 1 不难看出, Cauchy 命题是 \( \frac{ * }{\infty } \) 型的 Stolz 定理的一个特例. 为此只要将该定理中的 \( {b}_{n} \) 写成

\[
{b}_{n} = \left( {{b}_{n} - {b}_{n - 1}}\right)  + \cdots  + \left( {{b}_{2} - {b}_{1}}\right)  + {b}_{1},
\]

然后令 \( {x}_{1} = {b}_{1},{x}_{2} = {b}_{2} - {b}_{1},\cdots ,{x}_{n} = {b}_{n} - {b}_{n - 1} \) ,则就有 \( {b}_{n} = {x}_{1} + \cdots  + {x}_{n} \) ,再取 \( {a}_{n} = n \) 即可. 此外,在该定理中对分子上的 \( {b}_{n} \) 不加条件,这与 Cauchy 命题中对分子上的 \( {x}_{1} + \cdots  + {x}_{n} \) 不加条件也是完全一致的.

注 2 初学者第一次见到恒等式 (2.11) 时可能会觉得奇怪, 它是怎样想出来的? 回顾证明, 可见当时的问题完全在于如何从已经得到的估计式 (2.10) 出发去估计 \( \left| {\frac{{b}_{n}}{{a}_{n}} - l}\right| \) . 困难何在? 前一式的分母是 \( {a}_{n} - {a}_{N} \) ,而后一式的分母是 \( {a}_{n} \) . 恒等式 (2.11) 就是用于建立这两个分母不同的分式之间的联系. 打个比方来说, 怎样建立 \( 3/5 \) 和 \( 2/7 \) 之间的联系? 模仿恒等式 (2.11) 的内容就可以简单地得到

\[
\frac{3}{5} = \frac{7}{5} \cdot  \frac{2}{7} + \frac{1}{5}.
\]

注 3 读者可以将恒等式 (2.11) 与 Cauchy 命题证明中的分拆作比较. 如在 (2.11) 中令 \( {b}_{n} = {x}_{1} + \cdots  + {x}_{n},{a}_{n} = n \) 代入,可见完全一样.

注 4 这三个命题的逆命题都不成立. 以 Cauchy 命题为例,在数列 \( \left\{  {x}_{n}\right\} \) 发散 (但不是有确定符号的无穷大量) 时, 极限

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n}
\]

仍可能存在. 最简单的例子就是 \( \left\{  {\left( -1\right) }^{n - 1}\right\} \) ,这时上述极限为 0 .

思考题 若在这三个命题的条件中将极限值 \( l \) 改为不带符号的无穷大量 \( \infty \) , 则结论均不成立. 请读者举出反例.

#### 2.4.2 例题

首先重新处理例题2.2.4(即例题 2.3.6). 可是它现在已经是最平凡的题了.

例题 2.4.1 设 \( {a}_{n} = \frac{1! + 2! + \cdots  + n!}{n!}, n \in  {\mathbf{N}}_{ + } \) ,求 \( \left\{  {a}_{n}\right\} \) 的极限.

解 直接用 Stolz 定理计算如下:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1! + 2! + \cdots  + n!}{n!} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{\left( {n + 1}\right) !}{\left( {n + 1}\right) ! - n!} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{\left( {n + 1}\right) !}{n!n} = 1.
\]

例题 2.4.2 设 \( {a}_{1} > 0,{a}_{n + 1} = {a}_{n} + \frac{1}{{a}_{n}}, n \in  {\mathbf{N}}_{ + } \) ,证明 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}}{\sqrt{2n}} = 1 \) .

证 首先可看出 \( \left\{  {a}_{n}\right\} \) 为严格单调增加的正数列. 因此只有两种可能. 假定它有极限 \( a \) ,在递推公式

\[
{a}_{n + 1} = {a}_{n} + \frac{1}{{a}_{n}}
\]

的两边令 \( n \rightarrow  \infty \) ,得到 \( a = a + \frac{1}{a} \) ,这对任何有限数 \( a \) 都不可能成立. 因此知道 \( \left\{  {a}_{n}\right\} \) 只能是正无穷大量.

然后根据 2.1.5 小节的练习题 2, 只要用 Stolz 定理计算如下:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}^{2}}{2n} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n + 1}^{2} - {a}_{n}^{2}}{2\left( {n + 1}\right)  - {2n}} = \frac{1}{2}\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {2 + \frac{1}{{a}_{n}^{2}}}\right)  = 1.
\]

注 本例在以下几方面具有典型性: (1) 在 \( \left\{  {a}_{n}\right\} \) 为正无穷大量的基础上得到更为精确的结果: \( {a}_{n} \sim  \sqrt{2n} \) ; (2) 用 Stolz 定理时有一定的技巧性. 若对 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}}{\sqrt{2n}} \) 直接用 Stolz 定理就很不好做 (参见例题 8.1.10 和第八章第一组参考题 3 等).

例题 2.4.3 设已知 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} = a \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {a}_{k} = a \) .

证 利用 \( {2}^{n} = {\left( 1 + 1\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \) ,可以估计如下:

\[
\left| {\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {a}_{k} - a}\right|  = \left| {\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left( {{a}_{k} - a}\right) }\right|  \leq  \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right| .
\]

对 \( \varepsilon  > 0 \) ,存在 \( N \) ,当 \( k > N \) 时成立 \( \left| {{a}_{k} - a}\right|  < \varepsilon \) . 对 \( n > N \) 将最后一式作分拆:

\[
\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{N}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right|  + \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = N + 1}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right| . \tag{2.12}
\]

对其中的第二部分的估计是容易的:

\[
\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = N + 1}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right|  < \varepsilon  \cdot  \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = N + 1}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right)  < \varepsilon .
\]

对 (2.12) 中的第一部分的估计与 Cauchy 命题中不同, 因为这里的第一部分的分子也与 \( n \) 有关. 但可以发现实际上并不难. 固定 \( N \) ,存在 \( M > 0 \) ,使得 \( \left| {{a}_{k} - a}\right|  < M \) 对 \( k = 0,1,\cdots , N \) 成立. 再利用 \( \left( \begin{array}{l} n \\  k \end{array}\right)  < {n}^{k} \) ,就可以估计如下:

\[
\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{N}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right|  < \frac{M\left( {1 + n + \cdots  + {n}^{N}}\right) }{{2}^{n}}. \tag{2.13}
\]

因 \( N \) 已固定,右边当 \( n \rightarrow  \infty \) 时的极限为 0,因此存在 \( {N}_{1} > N \) ,当 \( n > {N}_{1} \) 时成立

\[
\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{N}\left( \begin{array}{l} n \\  k \end{array}\right) \left| {{a}_{k} - a}\right|  < \varepsilon .
\]

合并对两部分的估计,就得到当 \( n > {N}_{1} \) 时成立

\[
\left| {\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {a}_{k} - a}\right|  < {2\varepsilon }
\]

注 1 在这个例题中我们使用了 Cauchy 命题的证明方法, 而不是命题的结论. 此外,在一开始可以应用 \( {2}^{n} = {\left( 1 + 1\right) }^{n} \) 的二项式展开,将要求证明的极限等式右边的 \( a \) “无中生有”地写成与左边的表达式非常相似的形式，这是证明的主要手段. 实际上, 这就是数学中的一种常用方法, 可称为 “拟合法”.

注 2 在估计 (2.13) 时关键完全在于分母上有指数函数 \( {2}^{n} \) ,而分子只是项数固定的 \( n \) 的多项式,因此整个表达式一定是无穷小量,其他一切都是次要因素. 此外,最后我们并没有写出 \( {N}_{1} \) 的表达式. 再次回顾数列收敛定义,可见只要对每个 \( \varepsilon  > 0 \) “存在”满足要求的 \( N \) 即可,并不要求具体写出 \( N \) .

#### 2.4.3 练习题

1. 设 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} =  + \infty \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} =  + \infty \) .

2. 设 \( \left\{  {x}_{n}\right\} \) 单调增加, \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{1} + {x}_{2} + \cdots  + {x}_{n}}{n} = a \) ,证明: \( \left\{  {x}_{n}\right\} \) 收敛于 \( a \) .

3. 设 \( \left\{  {a}_{{2k} - 1}\right\} \) 收敛于 \( a,\left\{  {a}_{2k}\right\} \) 收敛于 \( b \) ，且 \( a \neq  b \) ，求 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{1} + {a}_{2} + \cdots  + {a}_{n}}{n}. \) (注意: 虽然数列 \( \left\{  {a}_{n}\right\} \) 发散,但前 \( n \) 项的算术平均值所成的数列仍可以有极限. 一个典型例子就是 \( \left. \left\{  {\left( -1\right) }^{n}\right\}  \right) \) .)

4. 若 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{a}_{n} - {a}_{n - 1}}\right)  = d \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n}}{n} = d \) .

(本题可以说是 Cauchy 命题的另一种形式, 也很有用.)

5. 设 \( \left\{  {a}_{n}\right\} \) 为正数列,且收敛于 \( A \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( {a}_{1}{a}_{2}\cdots {a}_{n}\right) }^{\frac{1}{n}} = A \) .

(本题与 Cauchy 命题的关系是明显的.)

6. 设 \( \left\{  {a}_{n}\right\} \) 为正数列,且存在极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n + 1}}{{a}_{n}} = l \) ,证明 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{{a}_{n}} = l \) .

(本题对类型为 \( \left\{  \sqrt[n]{{a}_{n}}\right\} \) 的极限问题很有用,可以说是例题 2.1.2 的一个发展. 这个结果在无穷级数的研究中也很重要.)

7. 设 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{x}_{n} - {x}_{n - 2}}\right)  = 0 \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{n}}{n} = 0 \) .

8. 设 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{x}_{n} - {x}_{n - 2}}\right)  = 0 \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{x}_{n} - {x}_{n - 1}}{n} = 0 \) .

(本题是 1970 年的 Putnam 竞赛题, 若没有题 7 的铺垫该如何做?)

9. 设数列 \( \left\{  {a}_{n}\right\} \) 满足条件 \( 0 < {a}_{1} < 1 \) 和 \( {a}_{n + 1} = {a}_{n}\left( {1 - {a}_{n}}\right) \left( {n \geq  1}\right) \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}n{a}_{n} = 1 \)

10. 若 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} = \alpha ,\mathop{\lim }\limits_{{n \rightarrow  \infty }}{b}_{n} = \beta \) ,证明: \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{1}{b}_{n} + {a}_{2}{b}_{n - 1} + \cdots  + {a}_{n}{b}_{1}}{n} = {\alpha \beta } \) .
