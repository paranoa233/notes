## \( \text{ § }{2.5} \) 自然对数的底 \( \mathrm{e} \) 和 Euler 常数 \( \gamma \)

在数学分析中数 \( \mathrm{e} \) 是通过数列极限而引进的一个常数,近似值为 \( \mathrm{e} \approx  {2.71828} \) . 数 e 在数学以及一般科学中的重要性决不亚于圆周率 \( \pi \) .

#### 2.5.1 与数 e 有关的两个问题

虽然数 e 不如圆周率 \( \pi \) 那样容易理解,但仍然有与 \( \mathrm{e} \) 密切有关的简单例子.

例题 2.5.1 如果一笔钱在银行里存入时间 \( T \) 后增值一倍,存入时间 \( T/2 \) 后增值 50%，那么顾客就可以采取以下策略:将同样的钱先存入时间 \( T/2 \) ，然后取出， 再存入时间 \( T/2 \) ，最后得到的钱是原来的 \( {1.5}^{2} = {2.25} \) 倍，即增值 125%. 现在将条件进一步理想化,设银行利率不随存入时间长短而改变,即存入时间 \( T/3 \) 后增值 33.33%，存入时间 \( T/4 \) 后增值 25%，依此类推. 问:用以上缩短存入时间并多次重复的方法能在时间 \( T \) 后得到的最大增值是多少?

不妨令 \( T = 1 \) 为单位时间. 设存取 \( n \) 次,每次存入时间分别为 \( {x}_{1},{x}_{2},\cdots ,{x}_{n} \) , 满足条件 \( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = 1 \) (即时间总和为 \( T \) ). 从平均值不等式有

\[
\left( {1 + {x}_{1}}\right) \left( {1 + {x}_{2}}\right) \cdots \left( {1 + {x}_{n}}\right)  \leq  {\left( \frac{n + {x}_{1} + \cdots  + {x}_{n}}{n}\right) }^{n} = {\left( 1 + \frac{1}{n}\right) }^{n},
\]

且当 \( {x}_{1} = \cdots  = {x}_{n} \) 时成立等号. 这表明在固定次数存取的前提下以等时间安排最为有利. 于是问题归结为研究数列

\[
\left\{  {\left( 1 + \frac{1}{n}\right) }^{n}\right\}
\]

的性质. 这个问题直接引向本节的主题 e. 从下面的分析和数 \( \mathrm{e} \approx  {2.71828} \) 可知,最大增值不会超过原有钱数的 171.83%.

例题 2.5.2 已知正数 \( a \) ,把它分成若干部分,如果要使它们的乘积达到最大, 应该怎样分法? 容易知道,将 \( a \) 分成相等的若干部分最为有利,这是平均值不等式的又一次应用. 但平均值不等式并不能告诉我们应该将数 \( a \) 分成几部分最好? 以 \( a = {10} \) 为例,可以试算出以下几个结果:

\[
{\left( \frac{10}{2}\right) }^{2} = {25},{\left( \frac{10}{3}\right) }^{3} \approx  {37.037},{\left( \frac{10}{4}\right) }^{4} = {39.0625},{\left( \frac{10}{5}\right) }^{5} = {32}.
\]

今后可以证明: 当等分而成的每一部分的值与数 e 最接近的时候, 它们的乘积最大. 对 \( a = {10} \) 来说,就是将它等分成四部分时所得到的乘积最大.

注 以上的第二个例子取自著名的中学生课外读物 [3]. 我们将在例题 8.3.3 中证明以上结论. 在那里的注 1 中还解决了与此密切相关的另一个问题,即如果对 \( a \) 以及所分的每一部分都限制为正整数时, 应当怎样分才能使乘积最大?

#### 2.5.2 关于数 e 的基本结果

命题 2.5.1 设 \( {a}_{n} = {\left( 1 + \frac{1}{n}\right) }^{n}, n \in  {\mathbf{N}}_{ + } \) ,则 \( \left\{  {a}_{n}\right\} \) 严格单调增加且收敛.

证 1 数列 \( \left\{  {a}_{n}\right\} \) 的通项就是一个数自乘 \( n \) 次,如再乘上 1,就可看成为 \( n + 1 \) 个数的乘积. 利用平均值不等式, 就有

\[
{a}_{n} = 1 \cdot  {\left( 1 + \frac{1}{n}\right) }^{n} < {\left\lbrack  \frac{n\left( {1 + \frac{1}{n}}\right)  + 1}{n + 1}\right\rbrack  }^{n + 1} = {\left( \frac{n + 2}{n + 1}\right) }^{n + 1} = {a}_{n + 1}.
\]

因此数列 \( \left\{  {a}_{n}\right\} \) 严格单调增加.

引入第二个数列 \( {b}_{n} = {\left( 1 + \frac{1}{n}\right) }^{n + 1}, n \in  {\mathbf{N}}_{ + } \) ,再用平均值不等式,得到

\[
\frac{1}{{b}_{n}} = 1 \cdot  {\left( \frac{n}{n + 1}\right) }^{n + 1} < {\left\lbrack  \frac{\left( {n + 1}\right) \left( \frac{n}{n + 1}\right)  + 1}{n + 2}\right\rbrack  }^{n + 2} = {\left( \frac{n + 1}{n + 2}\right) }^{n + 2} = \frac{1}{{b}_{n + 1}}.
\]

又由于对每个 \( n \) 有不等式 \( {a}_{n} < {b}_{n} \) ,可见 \( \left\{  {a}_{n}\right\} \) 严格单调增加,且以每一个 \( {b}_{n} \) 为上界; 同时 \( \left\{  {b}_{n}\right\} \) 严格单调减少,且以每一个 \( {a}_{n} \) 为下界,因此两个数列都收敛. 利用 \( {a}_{n}\left( {1 + 1/n}\right)  = {b}_{n} \) ,可见它们的极限相同.

在图 2.3 中将 \( \left\{  {a}_{n}\right\} \) 和 \( \left\{  {b}_{n}\right\} \) 的表达式看成是 \( n \) 的函数,分别用小圆点作出它们的前 10 项. 它们的极限就是 \( \mathrm{e} \) ,在图中用水平虚线的高度表示.

![bo_d7fstb491nqc7381io20_56_396_1256_780_438_0.jpg](images/xie_analysis_exercises_upper_043_bod7fstb491nqc7381io205639612567804380.jpg)

图 2.3

注 同时考虑两个数列的方法有一个优点, 即可以得到后面的不等式 (2.16). 若只要证 \( \left\{  {a}_{n}\right\} \) 有上界,则有很多其他方法. 例如,下面的构思见 [41]: 由于

\[
{\left( 1 + \frac{1}{n}\right) }^{n} \cdot  \frac{1}{2} \cdot  \frac{1}{2} < {\left\lbrack  \frac{n\left( {1 + \frac{1}{n}}\right)  + 2 \cdot  \frac{1}{2}}{n + 2}\right\rbrack  }^{n + 2} = 1,
\]

可知 \( \left\{  {a}_{n}\right\} \) 以 4 为上界. (用此法还可证明 \( \left\{  {a}_{n}\right\} \) 以 \( \left\{  {b}_{n}\right\} \) 的每一项为上界,其中即有 \( \left. {{b}_{1} = 4\text{ . }}\right) \)

证 2 将数列的通项 \( {a}_{n} \) 用二项式展开,得到

\[
{a}_{n} = 1 + \mathop{\sum }\limits_{{k = 1}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \frac{1}{{n}^{k}}
\]

\[
= 1 + 1 + \frac{1}{2!}\left( {1 - \frac{1}{n}}\right)  + \frac{1}{3!}\left( {1 - \frac{1}{n}}\right) \left( {1 - \frac{2}{n}}\right)  + \cdots
\]

\[
+ \frac{1}{n!}\left( {1 - \frac{1}{n}}\right) \left( {1 - \frac{2}{n}}\right) \cdots \left( {1 - \frac{n - 1}{n}}\right) .
\]

比较 \( {a}_{n} \) 和 \( {a}_{n + 1} \) 的类似展开式,可以看出前两项相同,而从第三项起, \( {a}_{n + 1} \) 的展开式中的每一项都比 \( {a}_{n} \) 的展开式中的相应项来得大,而且最后还要多出一个正项, 因此 \( \left\{  {a}_{n}\right\} \) 是严格单调增加数列. 又可以用上述展开式作如下估计:

\[
{a}_{n} < 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{n!} < 1 + 1 + \frac{1}{2} + \frac{1}{{2}^{2}} + \cdots  + \frac{1}{{2}^{n - 1}} < 3,
\]

因此 \( \left\{  {a}_{n}\right\} \) 有上界,从而收敛.

将上一命题中确定的极限记为 \( \mathrm{e} \) ,它的近似值是 \( {2.718281828}\cdots \) . 在 1728 年大数学家 Euler 引入 e 作为自然对数的底 (见 [29]). 在本书中将自然对数 \( {\log }_{\mathrm{e}}x \) 记为 \( \ln x \) ,在其他文献中也有记为 \( \log x \) 的. 从以后的学习中可以看到,虽然在日常计算中一般用常用对数, 但在数学中用自然对数更为 “自然” 和方便得多.

下一命题表明数 e 又是另一个数列的极限, 它也称为 e 的无穷级数展开式.

命题 2.5.2 证明数

\[
\mathrm{e} = \mathop{\sum }\limits_{{n = 0}}^{\infty }\frac{1}{n!} = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{n!} + \cdots .
\]

(记号 \( \mathop{\sum }\limits_{{n = 0}}^{\infty }\frac{1}{n!} \) 是以 \( \frac{1}{n!} \) 为通项的无穷级数,其中 \( 0! = 1 \) . 级数的和定义为部分和数列 \( \left\{  {s}_{n}\right\} \) 的极限,其中 \( {s}_{n} = 1 + \frac{1}{1!} + \frac{1}{2!} + \cdots  + \frac{1}{n!} \) . 参见例题 2.2.9 的注.)

证 从上一命题中已知 \( \left\{  {s}_{n}\right\} \) 以 3 为上界,又因 \( \left\{  {s}_{n}\right\} \) 严格单调增加,因此收敛. 记其极限为 \( s \) ,则从 \( {a}_{n} < {s}_{n} \) 得到 \( \mathrm{e} \leq  s \) . 固定正整数 \( m \) ,并令 \( n > m \) ,就有

\[
{a}_{n} = 1 + 1 + \frac{1}{2!}\left( {1 - \frac{1}{n}}\right)  + \cdots  + \frac{1}{n!}\left( {1 - \frac{1}{n}}\right) \left( {1 - \frac{2}{n}}\right) \cdots \left( {1 - \frac{n - 1}{n}}\right)
\]

\[
> 1 + 1 + \frac{1}{2!}\left( {1 - \frac{1}{n}}\right)  + \cdots  + \frac{1}{m!}\left( {1 - \frac{1}{n}}\right) \left( {1 - \frac{2}{n}}\right) \cdots \left( {1 - \frac{m - 1}{n}}\right) .
\]

其中不等号右边的和式是从 \( {a}_{n} \) 的表达式中去掉后 \( n - m \) 个正项得到的. 令 \( n \rightarrow  \infty \) , 就有

\[
\mathrm{e} \geq  1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{m!} = {s}_{m}.
\]

再令 \( m \rightarrow  \infty \) ,得到 \( \mathrm{e} \geq  s \) . 因此有 \( s = \mathrm{e} \) .

命题 2.5.3 记 \( {\varepsilon }_{n} = \mathrm{e} - \left( {1 + 1 + \frac{1}{2!} + \cdots  + \frac{1}{n!}}\right) \) ,则有 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\varepsilon }_{n}\left( {n + 1}\right) ! = 1 \) .

证 写出

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\varepsilon }_{n}\left( {n + 1}\right) ! = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{\varepsilon }_{n}}{\frac{1}{\left( {n + 1}\right) !}},
\]

然后用 \( \frac{0}{0} \) 型的 Stolz 定理 (即命题 2.4.2),这时

\[
{\varepsilon }_{n + 1} - {\varepsilon }_{n} =  - \frac{1}{\left( {n + 1}\right) !},\;\frac{1}{\left( {n + 2}\right) !} - \frac{1}{\left( {n + 1}\right) !} =  - \frac{1}{n!\left( {n + 2}\right) },
\]

可见所求的极限为 1 .

这个结果也可以从下面更为精细的估计得出.

命题 2.5.4 对于上述 \( {\varepsilon }_{n} \) 成立不等式 \( \frac{1}{\left( {n + 1}\right) !} < {\varepsilon }_{n} < \frac{1}{n!n} \) .

证 从 \( {\varepsilon }_{n} = \mathop{\sum }\limits_{{k = n + 1}}^{\infty }\frac{1}{k!} \) 可见 \( {\varepsilon }_{n} > \frac{1}{\left( {n + 1}\right) !} \) 成立. 对任意的 \( m > n \) ,估计

\[
\frac{1}{\left( {n + 1}\right) !} + \frac{1}{\left( {n + 2}\right) !} + \cdots  + \frac{1}{m!} < \frac{1}{\left( {n + 1}\right) !}\left( {1 + \frac{1}{n + 2} + \cdots  + \frac{1}{{\left( n + 2\right) }^{k}} + \cdots }\right)
\]

\[
= \frac{1}{\left( {n + 1}\right) !}\left( \frac{1}{1 - \frac{1}{n + 2}}\right)
\]

\[
= \frac{n + 2}{\left( {n + 1}\right) !\left( {n + 1}\right) } < \frac{1}{n!n},
\]

再令 \( m \rightarrow  \infty \) ,就得到所求的第二个不等式.

现在证明关于数 e 的一个基本结果, 它也是 Euler 首先得到的.

命题 2.5.5 自然对数的底 e 是无理数.

证 用反证法. 如果 \( \mathrm{e} \) 是有理数,则可写为 \( \mathrm{e} = p/q \) ,这里 \( p \) 和 \( q \) 是正整数. 从上两个命题知道,对于正整数 \( q \) ,可以将 \( \mathrm{e} \) 的无穷级数展开式写成为两项之和,即从级数的第一项到 \( 1/q \) ! 为第一部分,余下的 \( {\varepsilon }_{q} \) 为第二部分:

\[
\mathrm{e} = \frac{p}{q} = \left( {1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{q!}}\right)  + {\varepsilon }_{q}. \tag{2.14}
\]

由此可见, \( {\varepsilon }_{q} \) 一定是 \( 1/q \) ! 的整数倍. 但从上一个例题对 \( {\varepsilon }_{q} \) 的估计知道,有

\[
0 < {\varepsilon }_{q} < \frac{1}{q!q}
\]

因此这是不可能的.

注 1 换一个写法, 对不等式

\[
0 < \frac{p}{q} - \left( {1 + \frac{1}{1!} + \frac{1}{2!} + \cdots  + \frac{1}{q!}}\right)  < \frac{1}{q!q}
\]

的两边同乘 \( q!q \) ,则可见在中间的一个整数的值介于 0 和 1 之间,引出矛盾.

注 2 在 1873 年数学家 Hermite (埃尔米特) 进一步证明 e 是超越数, 也就是说 e 不是任何一个整系数代数方程的根. 这个证明可以在 [53, 55] 中找到.

本小节的前两个命题给出了以 \( \mathrm{e} \) 为极限的两个数列. 在计算 \( \mathrm{e} \) 的近似值时用它的无穷级数展开式的前有限项之和有很多优点: 计算方便, 收敛快, 又有很好的误差估计. 如果用 \( {a}_{n} = {\left( 1 + \frac{1}{n}\right) }^{n} \) 来计算 \( \mathrm{e} \) ,情况很不一样. 若令

\[
{\delta }_{n} = \mathrm{e} - {\left( 1 + \frac{1}{n}\right) }^{n},
\]

那么从本小节的命题 2.5.1 的证 1 可知

\[
{\delta }_{n} < {\left( 1 + \frac{1}{n}\right) }^{n + 1} - {\left( 1 + \frac{1}{n}\right) }^{n} = {\left( 1 + \frac{1}{n}\right) }^{n} \cdot  \frac{1}{n} < \frac{\mathrm{e}}{n} < \frac{3}{n}.
\]

进一步还可以得到

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{2n}{\delta }_{n}}{\mathrm{e}} = 1
\]

也就是说有

\[
{\delta }_{n} \sim  \frac{\mathrm{e}}{2n} \tag{2.15}
\]

其证明见例题 8.1.4.

用 \( \left\{  {a}_{n}\right\} \) 计算 \( \mathrm{e} \) 的近似值的实际例子: 在取 \( n = {100} \) 时, \( {a}_{100} = {2.70}\cdots \) ,只有两位数字是正确的. 又取 \( n = {10}^{4} \) ,则有 \( {a}_{{10}^{4}} = {2.71814}\cdots \) ,也只有四位数字是正确的. 这里的误差与公式 (2.15) 的估计是一致的. 另一方面, 若用

\[
{s}_{n} = 1 + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \cdots  + \frac{1}{n!}
\]

来求 \( \mathrm{e} \) 的近似值,则在取 \( n = {10} \) 时就有 \( {s}_{10} = {2.7182818}\cdots \) ,所写出的八位数字都是正确的. 这与命题 2.5.4 给出的误差估计也是一致的. 关于收敛的速度和计算效率的研究将会在计算方法课程中学习. 数学分析为此提供了基础.

小结 数 e 的引进和研究是一个重要范例. 这表明通过极限理论可以发现新的数. 应当指出, 由于这些数是通过极限来定义的, 对它们的研究就很不容易. 在这方面还有许多我们所不了解的东西, 有待今后的研究. 例如, 虽然已经证明了e 和 \( \pi \) 都是无理数和超越数,但迄今为止还没有人能证明 \( \mathrm{e} + \pi \) 是无理数.

#### 2.5.3 Euler 常数 \( \gamma \)

命题 2.5.6 数列 \( \left\{  {c}_{n}\right\} \) 收敛,其中 \( {c}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln n, n \in  {\mathbf{N}}_{ + } \) .

证 这里需要用不等式

\[
\frac{1}{n + 1} < \ln \left( {1 + \frac{1}{n}}\right)  < \frac{1}{n} \tag{2.16}
\]

这可从命题 2.5.1 中建立的 \( {\left( 1 + \frac{1}{n}\right) }^{n} < \mathrm{e} < {\left( 1 + \frac{1}{n}\right) }^{n + 1} \) 取自然对数得到.

现在研究数列 \( \left\{  {c}_{n}\right\} \) 的前后两项之差. 由 (2.16) 的第一个不等式可见

\[
{c}_{n + 1} - {c}_{n} = \frac{1}{n + 1} - \ln \left( {n + 1}\right)  + \ln n = \frac{1}{n + 1} - \ln \left( {1 + \frac{1}{n}}\right)  < 0,
\]

因此 \( \left\{  {c}_{n}\right\} \) 是严格单调减少数列. 以下只要证明这个数列有下界即可.

在 (2.16) 的右边的不等式中将 \( n \) 用 \( 1,2,\cdots , n \) 代入,然后将这些不等式相加, 就得到

\[
1 + \frac{1}{2} + \cdots  + \frac{1}{n} > \ln \left( {n + 1}\right)  = \ln n + \ln \left( {1 + \frac{1}{n}}\right)  > \ln n + \frac{1}{n + 1}.
\]

因此有

\[
{c}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln n > \frac{1}{n + 1} > 0,
\]

可见数列 \( \left\{  {c}_{n}\right\} \) 为正数列,因此收敛.

注 在确立了数列 \( \left\{  {c}_{n}\right\} \) 单调减少之后,也可以如同命题 2.5.1 的证 1 那样,引入第二个数列 \( \left\{  {d}_{n}\right\} \) ,其中 \( {d}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln \left( {n + 1}\right) , n \in  {\mathbf{N}}_{ + } \) . 这时有 \( {d}_{n} < {c}_{n},\forall n \in  {\mathbf{N}}_{ + } \) ,且由 (2.16) 知 \( {c}_{n} - {d}_{n} \rightarrow  0 \) . 同样可由 (2.16) 得到

\[
{d}_{n + 1} - {d}_{n} = \frac{1}{n + 1} - \ln \left( {n + 2}\right)  + \ln \left( {n + 1}\right)  = \frac{1}{n + 1} - \ln \left( {1 + \frac{1}{n + 1}}\right)  > 0.
\]

因此 \( \left\{  {d}_{n}\right\} \) 是严格单调增加数列,且有 \( {d}_{1} < \cdots  < {d}_{n} < {c}_{n} < \cdots  < {c}_{1},\forall n \in  {\mathbf{N}}_{ + } \) . 因此数列 \( \left\{  {c}_{n}\right\} \) 以每个 \( {d}_{n} \) 为下界,且和 \( \left\{  {d}_{n}\right\} \) 收敛于同一极限.

称以上数列 \( \left\{  {c}_{n}\right\} \) 的极限为 Euler 常数 (或 Euler-Mascheroni (马斯凯罗尼) 常数), 记为

\[
\gamma  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln n}\right)  \approx  {0.577215664}.
\]

由上述命题, 我们得到

\[
1 + \frac{1}{2} + \cdots  + \frac{1}{n} = \ln n + \gamma  + o\left( 1\right) .
\]

用这个公式和 Euler 常数的近似值就可以近似估计例题 2.2.6 中的发散数列 \( \left\{  {S}_{n}\right\} \) 当 \( n \) 很大时的值. 例如,在 \( n = {10}^{6} \) 时,从

\[
{S}_{{10}^{6}} = \mathop{\sum }\limits_{{k = 1}}^{{10}^{6}}\frac{1}{k} \approx  6\ln {10} + \gamma
\]

就得到 \( {S}_{{10}^{6}} \approx  {14.392726} \) . 用 Mathematica 软件验算,知道这 8 位数字都是准确的. 实际上如用近似公式

\[
1 + \frac{1}{2} + \cdots  + \frac{1}{n} \approx  \ln n + \gamma  + \frac{1}{2n}
\]

则效果还要好得多. 关于这方面的材料可以参考 [66].

一个尚未解决的问题是: Euler 常数 \( \gamma \) 是否是无理数? 类似的问题在数学中还有很多. 有人称 Euler 常数是其中“最大的谜” (见 [9] 中的 260 和 262 页).

#### 2.5.4 例题

例题 2.5.3 证明 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{n}{\sqrt[n]{n!}} = \mathrm{e} \) .

证 1 将 \( \frac{n}{\sqrt[n]{n!}} \) 取对数,则只需证明其极限等于 1 . 经整理后得到

\[
\ln \frac{n}{\sqrt[n]{n!}} = \frac{n\ln n - \left( {\ln 2 + \ln 3 + \cdots  + \ln n}\right) }{n} = \frac{{b}_{n}}{n}.
\]

用 Cauchy 命题即知 (也就是 2.4.3 小节的题 4):

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{b}_{n + 1} - {b}_{n}}\right)  = l \Rightarrow  \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{b}_{n}}{n} = l,
\]

计算得到 \( {b}_{n + 1} - {b}_{n} = n\ln \left( {1 + \frac{1}{n}}\right)  = \ln {\left( 1 + \frac{1}{n}\right) }^{n} \) ,可见极限为 1 .

证 2 将 \( \frac{n}{\sqrt[n]{n!}} \) 改写为 \( \sqrt[n]{\frac{{n}^{n}}{n!}} \) ,就可以用 2.4.3 小节题 6 中的方法来做. 这时记 \( {a}_{n} = \frac{{n}^{n}}{n!} \) ,因此只需计算后项与前项之比的极限:

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}_{n + 1}}{{a}_{n}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{\left( n + 1\right) }^{n + 1}}{\left( {n + 1}\right) !} \cdot  \frac{n!}{{n}^{n}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{n}\right) }^{n} = \mathrm{e}
\]

注 利用下一小节题 7 中的不等式可以得到本题的又一个解法. 此外, 本题还有积分学解法 (例题 11.4.2).

例题 2.5.4 计算极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {\frac{1}{n + 1} + \frac{1}{n + 2} + \cdots  + \frac{1}{2n}}\right) \) .

解 从 Euler 常数的讨论知道, 以

\[
{c}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \ln n
\]

为通项的数列收敛. 因此就知道 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{c}_{2n} - {c}_{n}}\right)  = 0 \) ,又有

\[
{c}_{2n} - {c}_{n} = \frac{1}{n + 1} + \frac{1}{n + 2} + \cdots  + \frac{1}{2n} - \ln 2,
\]

因此就求出

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {\frac{1}{n + 1} + \frac{1}{n + 2} + \cdots  + \frac{1}{2n}}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{c}_{2n} - {c}_{n}}\right)  + \ln 2 = \ln 2.
\]

注 此题的另一巧妙解法见 2.8.3 小节中的例题 4. 此外本题在学了积分学后就只是一个常规练习题 (参见例题 11.4.1).

#### 2.5.5 练习题

1. 计算下列极限:

(1) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 - \frac{1}{n}\right) }^{n} \) (2) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{2n}\right) }^{n} \)

(3) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{2}{n}\right) }^{n} \) (4) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{n}\right) }^{{n}^{2}} \)

(5) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{{n}^{2}}\right) }^{n} \) (6) \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{n} + \frac{1}{{n}^{2}}\right) }^{n} \) .

注 在计算中可以应用 2.1.5 小节题 4 中有关连续性的结果. 但是要请读者注意, 在现阶段如下的做法是缺乏根据的 (以题 (3) 为例):

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{2}{n}\right) }^{n} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left\lbrack  {\left( 1 + \frac{2}{n}\right) }^{\frac{n}{2}}\right\rbrack  }^{2} = {\mathrm{e}}^{2}.
\]

2. 设 \( k \in  {\mathbf{N}}_{ + } \) ,证明: \( \frac{k}{n + k} < \ln \left( {1 + \frac{k}{n}}\right)  < \frac{k}{n} \) .

3. 求 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {1 + \frac{1}{{n}^{2}}}\right) \left( {1 + \frac{2}{{n}^{2}}}\right) \cdots \left( {1 + \frac{n}{{n}^{2}}}\right) \) .

4. 设 \( \left\{  {p}_{n}\right\} \) 是正数列,且 \( {p}_{n} \rightarrow   + \infty \) ,计算 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( 1 + \frac{1}{{p}_{n}}\right) }^{{p}_{n}} \) .

5. 求 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{n!{2}^{n}}{{n}^{n}} \) .

6. 求极限 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{\ln n}{1 + \frac{1}{2} + \cdots  + \frac{1}{n}} \) .

7. 证明: \( {\left( \frac{n + 1}{\mathrm{e}}\right) }^{n} < n! < \mathrm{e}{\left( \frac{n + 1}{\mathrm{e}}\right) }^{n + 1} \) .

(由此又可得到 \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{n}{\sqrt[n]{n!}} = \mathrm{e} \) .)

8. 设 \( {S}_{n} = 1 + {2}^{2} + {3}^{3} + \cdots  + {n}^{n}, n \in  {\mathbf{N}}_{ + } \) . 证明: 对 \( n \geq  2 \) ,成立不等式

\[
{n}^{n}\left\lbrack  {1 + \frac{1}{4\left( {n - 1}\right) }}\right\rbrack   \leq  {S}_{n} < {n}^{n}\left\lbrack  {1 + \frac{2}{\mathrm{e}\left( {n - 1}\right) }}\right\rbrack  .
\]

9. 设有 \( {a}_{1} = 1,{a}_{n} = n\left( {{a}_{n - 1} + 1}\right) , n = 2,3,\cdots \) ,又设 \( {x}_{n} = \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + \frac{1}{{a}_{k}}}\right) , n \in  {\mathbf{N}}_{ + } \) , 求数列 \( \left\{  {x}_{n}\right\} \) 的极限.
