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
