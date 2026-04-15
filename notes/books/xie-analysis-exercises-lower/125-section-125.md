## 第一组参考题

1. 设 \( f\left( {x, y}\right) \) 关于 \( x \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上连续,且关于 \( y \) 单调增加. 如果有

\[
\mathop{\lim }\limits_{{y \rightarrow  {d}^{ - }}}f\left( {x, y}\right)  = f\left( {x, d}\right) , x \in  \left\lbrack  {a, b}\right\rbrack
\]

证明: 这一收敛关于 \( x \in  \left\lbrack  {a, b}\right\rbrack \) 是一致的,即 \( \forall \varepsilon  > 0 \) ,存在 \( \delta  > 0 \) ,当 \( 0 < d - y < \delta \) 时,对所有的 \( x \in  \left\lbrack  {a, b}\right\rbrack \) ,都有

\[
\left| {f\left( {x, y}\right)  - f\left( {x, d}\right) }\right|  < \varepsilon .
\]

2. 设 \( f \) 在 \( \left\lbrack  {a, b}\right\rbrack   \times  \left\lbrack  {a, b}\right\rbrack \) 上连续,定义

\[
\varphi \left( x\right)  = \mathop{\max }\limits_{{a \leq  \xi  \leq  x}}\{ \mathop{\max }\limits_{{a \leq  y \leq  \xi }}\{ f\left( {\xi , y}\right) \} \} ,
\]

证明: \( \varphi \left( x\right) \) 在 \( \left\lbrack  {a, b}\right\rbrack \) 上连续.

3. 设 \( D \) 是 \( {\mathbf{R}}^{n} \) 的紧子集, \( f \) 为定义在 \( D \) 上的函数,证明: \( f \) 在 \( D \) 上连续的充分必要条件是下列集合

\[
\left\{  {\left( {\mathbf{x}, y}\right)  \in  {\mathbf{R}}^{n + 1} \mid  y = f\left( \mathbf{x}\right) ,\mathbf{x} \in  D}\right\}
\]

是 \( {\mathbf{R}}^{n + 1} \) 中的紧集.

4. 设 \( {f}_{1},{f}_{2},\cdots ,{f}_{n} \) 是 \( \left\lbrack  {0,1}\right\rbrack \) 上的 \( n \) 个连续函数,称 \( {f}_{1},{f}_{2},\cdots ,{f}_{n} \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上线性相关,若存在不全为零的常数 \( {c}_{1},{c}_{2},\cdots ,{c}_{n} \) ,使得

\[
\mathop{\sum }\limits_{{j = 1}}^{n}{c}_{j}{f}_{j}\left( x\right)  \equiv  0, x \in  \left\lbrack  {0,1}\right\rbrack
\]

证明: \( {f}_{1},{f}_{2},\cdots ,{f}_{n} \) 在 \( \left\lbrack  {0,1}\right\rbrack \) 上线性相关的充分必要条件是

\[
\det \left( {\left\lbrack  {\int }_{0}^{1}{f}_{i}\left( x\right) {f}_{j}\left( x\right) \mathrm{d}x\right\rbrack  }_{n \times  n}\right)  = 0
\]

其中 \( \det \left( \mathbf{A}\right) \) 是 \( \mathbf{A} \) 的行列式.

5. 设 \( {\mathbf{p}}_{1},{\mathbf{p}}_{2},\cdots ,{\mathbf{p}}_{k} \) 是 \( {\mathbf{R}}^{2} \) 上的 \( k \) 个相异的点,证明: 存在一个最小半径的圆盘 \( B \) ,把这 \( k \) 个点覆盖. 对于 \( {\mathbf{R}}^{n} \) 中的点,也有类似的命题.

6. 设 \( \mathbf{A},\mathbf{B} \) 是两个 \( n \) 阶的实对称方阵,其中 \( \mathbf{B} \) 是正定矩阵. 设函数 \( G\left( \mathbf{x}\right)  = \; {\left( {\mathbf{x}}^{\mathrm{T}}\mathbf{B}\mathbf{x}\right) }^{-1}\left( {{\mathbf{x}}^{\mathrm{T}}\mathbf{A}\mathbf{x}}\right) \) 定义在 \( E = {\mathbf{R}}^{n} \smallsetminus  \{ \mathbf{0}\} \) 上,其中 \( {\mathbf{x}}^{\mathrm{T}} \) 是 \( \mathbf{x} \) 的转置. 证明:

(1) \( G\left( \mathbf{x}\right) \) 可以在 \( E \) 上取到最大值；

(2) \( G\left( \mathbf{x}\right) \) 的最大值点是与 \( \mathbf{A},\mathbf{B} \) 有关的某个矩阵的特征向量. 请写出这个矩阵.
