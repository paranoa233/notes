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
