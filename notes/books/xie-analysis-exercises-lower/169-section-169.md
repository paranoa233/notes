## 第二组参考题

1. 试用压缩映射原理证明如下局部微分同胚定理: 设 \( U \) 是 \( {\mathbf{R}}^{n} \) 的开集, \( \mathbf{f} : U \rightarrow \; {\mathbf{R}}^{n} \) 是 \( {C}^{k} \) 映射, \( {\mathbf{x}}_{0} \in  U,\det J\mathbf{f}\left( {\mathbf{x}}_{0}\right)  \neq  0 \) . 则存在 \( {\mathbf{x}}_{0} \) 的邻域 \( W \subset  U \) 和 \( f\left( {\mathbf{x}}_{0}\right) \) 的邻域 \( V \) ,使得 \( \mathbf{f} : W \rightarrow  V \) 是 \( {C}^{k} \) 微分同胚.

2. 设 \( \mathbf{f} : {\mathbf{R}}^{n} \rightarrow  {\mathbf{R}}^{n} \) 是 \( {C}^{1} \) 映射,且存在 \( \alpha  > 0 \) 使 \( \forall \mathbf{x} \in  {\mathbf{R}}^{n} \) 有

\[
{\mathbf{u}}^{\mathrm{T}} \cdot  J\mathbf{f}\left( \mathbf{x}\right)  \cdot  \mathbf{u} \geq  \alpha {\left| \mathbf{u}\right| }^{2},\forall \mathbf{u} \in  {\mathbf{R}}^{n},
\]

其中 \( {\mathbf{u}}^{\mathrm{T}} \) 表示 \( \mathbf{u} \) 的转置. 证明:

\[
\left| {\mathbf{f}\left( \mathbf{x}\right)  - \mathbf{f}\left( \mathbf{y}\right) }\right|  \geq  \alpha \left| {\mathbf{x} - \mathbf{y}}\right| ,\forall \mathbf{x},\mathbf{y} \in  {\mathbf{R}}^{n},
\]

且 \( \mathbf{f} \) 是 \( {\mathbf{R}}^{n} \) 上的微分同胚.

3. 用映射的语言叙述隐函数组存在定理, 将它化为逆映射存在定理或直接用压缩映射原理证明.

4. 20.2.4 小节的逆映射存在性证明是构造性的, 它给出了逆映射的迭代构造格式. 设 \( \mathbf{y} \in  V \) ,取合适的初始点 \( {\mathbf{x}}_{0} \in  U \) ,则

\[
{\mathbf{x}}_{n} = {\mathbf{x}}_{n - 1} + {\left( {\mathbf{f}}^{\prime }\left( \mathbf{a}\right) \right) }^{-1}\left( {\mathbf{y} - \mathbf{f}\left( {\mathbf{x}}_{n - 1}\right) }\right)
\]

就给出了迭代列 \( \left\{  {\mathbf{x}}_{n}\right\} \) 的公式. 讨论映射

\[
\mathbf{T} : u = \frac{1}{2}\left( {{x}^{2} - {y}^{2}}\right) ,\;v = {xy}
\]

的逆映射. 设 \( \mathbf{a} = {\left( 1,1\right) }^{\mathrm{T}} \) . 先求

\[
{\mathbf{T}}^{\prime }\left( \mathbf{a}\right)  = {\left. \left( \begin{array}{ll} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\  \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{array}\right) \right| }_{\left( {x, y}\right)  = \left( {1,1}\right) },
\]

再利用迭代公式

\[
\left( \begin{array}{l} {x}_{n} \\  {y}_{n} \end{array}\right)  = \left( \begin{array}{l} {x}_{n - 1} \\  {y}_{n - 1} \end{array}\right)  + {\left( {\mathbf{T}}^{\prime }\left( \mathbf{a}\right) \right) }^{-1}\left\lbrack  {\left( \begin{array}{l} u \\  v \end{array}\right)  - \left( \begin{matrix} \frac{1}{2}\left( {{x}_{n - 1}^{2} - {y}_{n - 1}^{2}}\right) \\  {x}_{n - 1}{y}_{n - 1} \end{matrix}\right) }\right\rbrack
\]

在 \( \mathbf{a} \) 的邻域内求 \( {\mathbf{T}}^{-1} \) 的二次迭代解 \( {\left( {x}_{2},{y}_{2}\right) }^{\mathrm{T}} \) ,并用它与逆映射的一次微分近似

\[
{\mathbf{T}}^{-1}\left( \begin{array}{l} u \\  v \end{array}\right)  \approx  \left( \begin{array}{l} 1 \\  1 \end{array}\right)  + {\left( \begin{matrix} 1 &  - 1 \\  1 & 1 \end{matrix}\right) }^{-1}\left( \begin{matrix} u \\  v - 1 \end{matrix}\right)
\]

作比较.

5. 设 \( U \) 是 \( {\mathbf{R}}^{m} \) 的开集, \( \mathbf{f} : U \rightarrow  {\mathbf{R}}^{n} \) 是 \( {C}^{k} \) 映射,满足条件:

\[
\mathbf{f}\left( \mathbf{0}\right)  = \mathbf{0},\;J\mathbf{f}\left( \mathbf{0}\right) \text{ 的秩为 }m\left( {m \leq  n}\right) \text{ . }
\]

证明: 存在 \( {\mathbf{R}}^{n} \) 中含0的两个邻域 \( V \) 及 \( W,{C}^{k} \) 微分同胚 \( \mathbf{h} : V \rightarrow  W \) 使得 \( \mathbf{h}\left( \mathbf{0}\right)  = \mathbf{0} \) ,并且

\[
\mathbf{h} \circ  \mathbf{f}\left( {{x}_{1},{x}_{2},\cdots ,{x}_{m}}\right)  = \left( {{x}_{1},{x}_{2},\cdots ,{x}_{m},0,0,\cdots ,0}\right) ,\forall \left( {{x}_{1},{x}_{2},\cdots ,{x}_{m}}\right)  \in  {\mathbf{f}}^{-1}\left( V\right) .
\]

6. 设 \( U \) 是 \( {\mathbf{R}}^{m} \) 的开集, \( \mathbf{f} : U \rightarrow  {\mathbf{R}}^{n} \) 是 \( {C}^{k} \) 映射,满足条件:

\[
\mathbf{f}\left( \mathbf{0}\right)  = \mathbf{0},\;J\mathbf{f}\left( \mathbf{0}\right) \text{ 的秩为 }n\left( {m \geq  n}\right) \text{ . }
\]

证明: 存在 \( {\mathbf{R}}^{m} \) 中含0的两个邻域 \( V \) 及 \( W,{C}^{k} \) 微分同胚 \( \varphi  : V \rightarrow  W \) 使得 \( \varphi \left( \mathbf{0}\right)  = \mathbf{0} \) ,并且

\[
\mathbf{f} \circ  \mathbf{\varphi }\left( {{x}_{1},{x}_{2},\cdots ,{x}_{m}}\right)  = \left( {{x}_{1},{x}_{2},\cdots ,{x}_{n}}\right) ,\forall \left( {{x}_{1},{x}_{2},\cdots ,{x}_{m}}\right)  \in  V.
\]

(以上两个命题称为秩定理，如何对它们作一个简单的几何解释？)
