#### 26.1.3 Hamilton 算子 \( \nabla \)

\( \nabla \) 是一个算子符号,称为 Hamilton (哈密顿) 算子. 它的定义是

\[
\nabla  = \mathbf{i}\frac{\partial }{\partial x} + \mathbf{j}\frac{\partial }{\partial y} + \mathbf{k}\frac{\partial }{\partial z}.
\]

其具体含义如下: 设 \( f \) 是一个可微函数,则

\[
\nabla f = \mathbf{i}\frac{\partial f}{\partial x} + \mathbf{j}\frac{\partial f}{\partial y} + \mathbf{k}\frac{\partial f}{\partial z},
\]

即

\[
\nabla f = \operatorname{grad}f\;\left( {f\text{ 的梯度 }}\right) .
\]

设 \( \mathbf{a} \) 是一个向量场, \( \mathbf{a} = P\mathbf{i} + Q\mathbf{j} + R\mathbf{k} \) ,则

\[
\nabla  \cdot  \mathbf{a} = \operatorname{div}\mathbf{a}
\]

\[
\nabla  \times  \mathbf{a} = \operatorname{curl}\mathbf{a}.
\]

因此,我们也常用 \( \nabla  \cdot  \mathbf{a} \) 和 \( \nabla  \times  \mathbf{a} \) 分别表示 \( \mathbf{a} \) 的散度与旋度. 直接运算可以证明下列关系式 (其中 \( \alpha ,\beta \) 为常数, \( f, g \) 为数量函数, \( \mathbf{a},\mathbf{b} \) 为向量函数):

\[
\nabla \left( {{\alpha f} + {\beta g}}\right)  = \alpha \nabla f + \beta \nabla g, \tag{26.7}
\]

\[
\nabla  \cdot  \left( {\alpha \mathbf{a} + \beta \mathbf{b}}\right)  = \alpha \nabla  \cdot  \mathbf{a} + \beta \nabla  \cdot  \mathbf{b}, \tag{26.8}
\]

\[
\nabla  \times  \left( {\alpha \mathbf{a} + \beta \mathbf{b}}\right)  = \alpha \nabla  \times  \mathbf{a} + \beta \nabla  \times  \mathbf{b}, \tag{26.9}
\]

\[
\nabla \left( {fg}\right)  = \left( {\nabla f}\right) g + f\left( {\nabla g}\right) , \tag{26.10}
\]

\[
\nabla  \cdot  \left( {f\mathbf{a}}\right)  = f\left( {\nabla  \cdot  \mathbf{a}}\right)  + \left( {\nabla f}\right)  \cdot  \mathbf{a}, \tag{26.11}
\]

\[
\nabla  \times  \left( {f\mathbf{a}}\right)  = f\left( {\nabla  \times  \mathbf{a}}\right)  + \left( {\nabla f}\right)  \times  \mathbf{a}, \tag{26.12}
\]

\[
\nabla  \cdot  \left( {\nabla  \times  \mathbf{a}}\right)  = 0\;\text{ (即任一向量函数的旋度的散度为零), } \tag{26.13}
\]

\( \nabla  \times  \left( {\nabla f}\right)  = \mathbf{0}\; \) (即任一数量函数的梯度的旋度为零向量).(26.14)

例题 26.1.3 \( \mathbf{A},\mathbf{B} \) 为可微的向量函数,则

\[
\nabla  \cdot  \left( {\mathbf{A} \times  \mathbf{B}}\right)  = \mathbf{B} \cdot  \left( {\nabla  \times  \mathbf{A}}\right)  - \mathbf{A} \cdot  \left( {\nabla  \times  \mathbf{B}}\right) .
\]

证 设 \( \mathbf{A} = \left( {{a}_{1},{a}_{2},{a}_{3}}\right) ,\mathbf{B} = \left( {{b}_{1},{b}_{2},{b}_{3}}\right) \) ,则有

\[
\mathbf{A} \times  \mathbf{B} = \left| \begin{matrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\  {a}_{1} & {a}_{2} & {a}_{3} \\  {b}_{1} & {b}_{2} & {b}_{3} \end{matrix}\right|
\]

于是

\[
\nabla  \cdot  \left( {\mathbf{A} \times  \mathbf{B}}\right)  = \frac{\partial }{\partial x}\left| \begin{array}{ll} {a}_{2} & {a}_{3} \\  {b}_{2} & {b}_{3} \end{array}\right|  - \frac{\partial }{\partial y}\left| \begin{array}{ll} {a}_{1} & {a}_{3} \\  {b}_{1} & {b}_{3} \end{array}\right|  + \frac{\partial }{\partial z}\left| \begin{array}{ll} {a}_{1} & {a}_{2} \\  {b}_{1} & {b}_{2} \end{array}\right|
\]

\[
= \left| \begin{matrix} {\partial }_{x}{a}_{2} & {\partial }_{x}{a}_{3} \\  {b}_{2} & {b}_{3} \end{matrix}\right|  - \left| \begin{matrix} {\partial }_{y}{a}_{1} & {\partial }_{y}{a}_{3} \\  {b}_{1} & {b}_{3} \end{matrix}\right|  + \left| \begin{matrix} {\partial }_{z}{a}_{1} & {\partial }_{z}{a}_{2} \\  {b}_{1} & {b}_{2} \end{matrix}\right|
\]

\[
+ \left| \begin{matrix} {a}_{2} & {a}_{3} \\  {\partial }_{x}{b}_{2} & {\partial }_{x}{b}_{3} \end{matrix}\right|  - \left| \begin{matrix} {a}_{1} & {a}_{3} \\  {\partial }_{y}{b}_{1} & {\partial }_{y}{b}_{3} \end{matrix}\right|  + \left| \begin{matrix} {a}_{1} & {a}_{2} \\  {\partial }_{z}{b}_{1} & {\partial }_{z}{b}_{2} \end{matrix}\right|
\]

\[
= {I}_{1} + {I}_{2},
\]

其中 \( {I}_{1} \) 为前三项, \( {I}_{2} \) 为后三项. 经计算验证有

\[
{I}_{1} = {b}_{1}\left( {{\partial }_{y}{a}_{3} - {\partial }_{z}{a}_{2}}\right)  + {b}_{2}\left( {{\partial }_{z}{a}_{1} - {\partial }_{x}{a}_{3}}\right)  + {b}_{3}\left( {{\partial }_{x}{a}_{2} - {\partial }_{y}{a}_{1}}\right)  = \mathbf{B} \cdot  \left( {\nabla  \times  \mathbf{A}}\right) ,
\]

同理可证

\[
{I}_{2} =  - \mathbf{A} \cdot  \left( {\nabla  \times  \mathbf{B}}\right) .
\]

例题 26.1.4 设 \( u\left( {x, y, z}\right) \) 在 \( {\bar{B}}_{R}\left( {\mathbf{M}}_{0}\right) \) 上二阶连续可微,其中 \( {\mathbf{M}}_{0} = \left( {{x}_{0},{y}_{0},{z}_{0}}\right) \) , \( {B}_{R}\left( {\mathbf{M}}_{0}\right) \) 是以 \( {\mathbf{M}}_{0} \) 为心,以 \( R \) 为半径的球. 对于 \( 0 < \rho  \leq  R \) ,如果都有

\[
{\oiint }_{\partial {B}_{\rho }\left( {\mathbf{M}}_{0}\right) }\frac{\partial u}{\partial \mathbf{n}}\left( {x, y, z}\right) \mathrm{d}S = 0,
\]

其中 \( \partial {B}_{\rho }\left( {\mathbf{M}}_{0}\right) \) 是以 \( {\mathbf{M}}_{0} \) 为心,以 \( \rho \) 为半径的球面, \( \mathbf{n} \) 是球面上的单位外法向量,则

\[
u\left( {\mathbf{M}}_{0}\right)  = \frac{1}{{4\pi }{R}^{2}}{\oiint }_{\partial {B}_{R}\left( {\mathbf{M}}_{0}\right) }u\left( {x, y, z}\right) \mathrm{d}S.
\]

即球心的值等于球面上的积分平均值.

证 令

\[
x = {x}_{0} + \rho \sin \varphi \cos \theta ,\;y = {y}_{0} + \rho \sin \varphi \sin \theta ,\;z = {z}_{0} + \rho \cos \varphi ,
\]

\[
0 \leq  \theta  \leq  {2\pi },\;0 \leq  \varphi  \leq  \pi
\]

则在 \( \partial {B}_{\rho }\left( {\mathbf{M}}_{0}\right) \) 上有

\[
\frac{\partial u}{\partial n}\left( {x, y, z}\right)  = \nabla u \cdot  \mathbf{n}
\]

\[
= \frac{\mathrm{d}u}{\mathrm{\;d}\rho }\left( {{x}_{0} + \rho \sin \varphi \cos \theta ,{y}_{0} + \rho \sin \varphi \sin \theta ,{z}_{0} + \rho \cos \varphi }\right)
\]

\[
= \frac{\mathrm{d}u}{\mathrm{\;d}\rho }\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) .
\]

于是

\[
0 = {\oiint }_{\partial {B}_{\rho }\left( {\mathbf{M}}_{0}\right) }\frac{\partial u}{\partial \mathbf{n}}\left( {x, y, z}\right) \mathrm{d}S = {\rho }^{2}{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }\frac{\mathrm{d}u}{\mathrm{\;d}\rho }\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{1}\;\text{ (由 }\left( {25.28}\right)
\]

(由 (25.28))

\[
= {\rho }^{2}\frac{\mathrm{d}}{\mathrm{d}\rho }{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{1}.
\]

由此可得到

\[
\frac{\mathrm{d}}{\mathrm{d}\rho }{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{1} = 0,
\]

即

\[
\frac{\mathrm{d}}{\mathrm{d}\rho }\left\lbrack  {{\rho }^{-2}{\oiint }_{\partial {B}_{\rho }\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{\rho }}\right\rbrack   = 0.
\]

因此对于 \( 0 < \rho  \leq  R \) ,

\[
{\rho }^{-2}{\oiint }_{\partial {B}_{\rho }\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{\rho } = {R}^{-2}{\oiint }_{\partial {B}_{R}\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + R\mathbf{n}}\right) \mathrm{d}{S}_{R}.
\]

另一方面,当 \( \rho  \rightarrow  {0}^{ + } \) 时,

\[
{\rho }^{-2}{\oiint }_{\partial {B}_{\rho }\left( \mathbf{0}\right) }u\left( {{\mathbf{M}}_{0} + \rho \mathbf{n}}\right) \mathrm{d}{S}_{\rho } \rightarrow  {4\pi u}\left( {\mathbf{M}}_{0}\right) .
\]
