## §25.3 Gauss 公式与 Stokes 公式

#### 25.3.1 Gauss 公式

Gauss 公式是将 \( {\mathbf{R}}^{3} \) 中某区域上的三重积分与这一区域的边界上特定的曲面积分建立联系的一个重要公式.

设 \( D \) 是 \( {\mathbf{R}}^{3} \) 内的一个有界区域,其边界 \( \partial D \) 由光滑曲面或逐片光滑曲面组成, 方向是外侧 (相对于区域 \( D \) 而言). 又设函数 \( P, Q, R \) 都在 \( D \) 上有关于 \( x, y, z \) 的连续偏导数，则成立下列 Gauss 公式:

\[
{\iint }_{D}\left( {\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}}\right) \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z = {\iint }_{\partial D}P\mathrm{\;d}y\mathrm{\;d}z + Q\mathrm{\;d}z\mathrm{\;d}x + R\mathrm{\;d}x\mathrm{\;d}y. \tag{25.5}
\]

利用两类曲面积分之间的关系, Gauss 公式也可以写成

\[
\begin{aligned}  & {\iiint }_{D}\left( {\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}}\right) \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z \\   = & {\iiint }_{\partial D}\left( {P\cos \left( {\mathbf{n}, x}\right)  + Q\cos \left( {\mathbf{n}, y}\right)  + R\cos \left( {\mathbf{n}, z}\right) }\right) \mathrm{d}S, \end{aligned} \tag{25.6}
\]

其中 \( \mathbf{n} \) 为曲面 \( \partial D \) 上的外法向量.

可以看出, Green 公式 (24.9) 与 Gauss 公式 (25.6) 的表达形式是类似的, 仅仅是空间的维数不同而已.

与 Green 公式相仿, Gauss 公式 (25.5) 与 (25.6) 为我们提供了一种新的计算曲面积分的方法.

例题 25.3.1 求

\[
I = {\iint }_{\sum }{4xz}\mathrm{\;d}y\mathrm{\;d}z - {2yz}\mathrm{\;d}z\mathrm{\;d}x + \left( {1 - {z}^{2}}\right) \mathrm{d}x\mathrm{\;d}y,
\]

其中 \( \sum \) 是曲线 \( z = {\mathrm{e}}^{y}\left( {0 \leq  y \leq  a}\right) \) 绕 \( z \) 轴旋转生成的旋转面,取下侧.

解 \( \sum \) 的方程为

\[
z = {\mathrm{e}}^{\sqrt{{x}^{2} + {y}^{2}}}\left( {{x}^{2} + {y}^{2} \leq  {a}^{2}}\right) .
\]

![bo_d7fsu8491nqc7381io7g_359_548_310_558_434_0.jpg](images/xie_analysis_exercises_lower_032_bod7fsu8491nqc7381io7g3595483105584340.jpg)

图 25.5

直接计算比较复杂. 考虑用 Gauss 公式. 由于 \( \sum \) 不闭,需要添加辅助面

\[
{\sum }_{1} : z = {\mathrm{e}}^{a}\left( {{x}^{2} + {y}^{2} \leq  {a}^{2}}\right) \text{ ,取上侧. }
\]

见图 25.5,设 \( \sum \) 与 \( {\sum }_{1} \) 围成的区域为 \( D \) . 令

\[
P = {4xz},\;Q =  - {2yz},\;R = 1 - {z}^{2},
\]

则

\[
\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = 0
\]

由公式 (25.5), 得

\[
I = \left( {{\iint }_{\sum } + {\iint }_{{\sum }_{1}} - {\iint }_{{\sum }_{1}}}\right) \left( {1 - {z}^{2}}\right) \mathrm{d}x\mathrm{\;d}y =  - {\iint }_{{\sum }_{1}}\left( {1 - {z}^{2}}\right) \mathrm{d}x\mathrm{\;d}y
\]

\[
= \left( {{\mathrm{e}}^{2a} - 1}\right) {\iint }_{{x}^{2} + {y}^{2} \leq  {a}^{2}}\mathrm{\;d}x\mathrm{\;d}y = \left( {{\mathrm{e}}^{2a} - 1}\right) \pi {a}^{2}.
\]

例题 25.3.2 计算曲面积分

\[
I = {\iint }_{S}\frac{x\mathrm{\;d}y\mathrm{\;d}z + y\mathrm{\;d}z\mathrm{\;d}x + z\mathrm{\;d}x\mathrm{\;d}y}{{\left( a{x}^{2} + b{y}^{2} + c{z}^{2}\right) }^{3/2}},
\]

其中 \( S \) 是球面 \( {x}^{2} + {y}^{2} + {z}^{2} = 1 \) ,取外侧 \( \left( {a > 0, b > 0, c > 0}\right) \) .

解 1 记 \( P\left( {x, y, z}\right)  = \frac{x}{{\left( a{x}^{2} + b{y}^{2} + c{z}^{2}\right) }^{3/2}}, Q\left( {x, y, z}\right)  = \frac{y}{{\left( a{x}^{2} + b{y}^{2} + c{z}^{2}\right) }^{3/2}} \) , \( R\left( {x, y, z}\right)  = \frac{z}{{\left( a{x}^{2} + b{y}^{2} + c{z}^{2}\right) }^{3/2}} \) ,则在不包含原点的任何区域上

\[
\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = 0
\]

为了利用 Gauss 公式,对充分小的 \( \varepsilon  > 0 \) ,作闭曲面

\[
{S}_{\varepsilon } = \left\{  {a{x}^{2} + b{y}^{2} + c{z}^{2} = {\varepsilon }^{2}}\right\}  ,
\]

取外侧. 由 Gauss 公式

\[
I = {\oiint }_{{S}_{\varepsilon }}\frac{x\mathrm{\;d}y\mathrm{\;d}z + y\mathrm{\;d}z\mathrm{\;d}x + z\mathrm{\;d}x\mathrm{\;d}y}{{\left( a{x}^{2} + b{y}^{2} + c{z}^{2}\right) }^{3/2}} = \frac{1}{{\varepsilon }^{3}}{\oiint }_{{S}_{\varepsilon }}x\mathrm{\;d}y\mathrm{\;d}z + y\mathrm{\;d}z\mathrm{\;d}x + z\mathrm{\;d}x\mathrm{\;d}y.
\]

上述积分在 \( {S}_{\varepsilon } \) 的外侧. 再一次用 Gauss 公式,则

\[
I = \frac{3}{{\varepsilon }^{3}}{\iiint }_{a{x}^{2} + b{y}^{2} + c{z}^{2} \leq  {\varepsilon }^{2}}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z = \frac{3}{{\varepsilon }^{3}} \cdot  \frac{4\pi }{3} \cdot  \frac{{\varepsilon }^{3}}{\sqrt{abc}} = \frac{4\pi }{\sqrt{abc}}.
\]

解 2 (不用 Gauss 公式而直接计算) 利用单位球面的参数方程

\[
x = \sin \varphi \cos \theta , y = \sin \varphi \sin \theta , z = \cos \varphi ,
\]

\[
0 \leq  \varphi  \leq  \pi ,0 \leq  \theta  \leq  {2\pi }
\]

计算得到

\[
A = \frac{\partial \left( {y, z}\right) }{\partial \left( {\varphi ,\theta }\right) } = {\sin }^{2}\varphi \cos \theta , B = \frac{\partial \left( {z, x}\right) }{\partial \left( {\varphi ,\theta }\right) } = {\sin }^{2}\varphi \sin \theta ,
\]

\[
C = \frac{\partial \left( {x, y}\right) }{\partial \left( {\varphi ,\theta }\right) } = \sin \varphi \cos \varphi .
\]

容易看出, \( \left( {A, B, C}\right) \) 的方向与单位球面外侧法线方向相同,故积分号前取 “+” 号, 由 (25.3) 得

\[
I = 8{\int }_{0}^{\pi /2}{\int }_{0}^{\pi /2}\frac{\sin \varphi \mathrm{d}\varphi \mathrm{d}\theta }{{\left( a{\sin }^{2}\varphi {\cos }^{2}\theta  + b{\sin }^{2}\varphi {\sin }^{2}\theta  + c{\cos }^{2}\varphi \right) }^{3/2}}.
\]

先计算对 \( \varphi \) 的积分,我们令 \( \cos \varphi  = t \) ,则

\[
{\int }_{0}^{\pi /2}\frac{\sin \varphi \mathrm{d}\varphi }{{\left( a{\sin }^{2}\varphi {\cos }^{2}\theta  + b{\sin }^{2}\varphi {\sin }^{2}\theta  + c{\cos }^{2}\varphi \right) }^{3/2}}
\]

\[
= {\int }_{0}^{1}\frac{\mathrm{d}t}{{\left\lbrack  \left( a{\cos }^{2}\theta  + b{\sin }^{2}\theta \right)  - \left( a{\cos }^{2}\theta  + b{\sin }^{2}\theta  - c\right) {t}^{2}\right\rbrack  }^{3/2}}
\]

\[
= \frac{1}{{\left( a{\cos }^{2}\theta  + b{\sin }^{2}\theta \right) }^{\prime }} \cdot  {\left. \frac{t}{{\left\lbrack  \left( a{\cos }^{2}\theta  + b{\sin }^{2}\theta \right)  - \left( a{\cos }^{2}\theta  + b{\sin }^{2}\theta  - c\right) {t}^{2}\right\rbrack  }^{1/2}}\right| }_{t = 0}^{t = t}
\]

\[
= \frac{1}{\sqrt{c}} \cdot  \frac{1}{a{\cos }^{2}\theta  + b{\sin }^{2}\theta }.
\]

最后得到

\[
I = \frac{8}{\sqrt{c}}{\int }_{0}^{\pi /2}\frac{\mathrm{d}\theta }{a{\cos }^{2}\theta  + b{\sin }^{2}\theta } = \frac{8}{\sqrt{c}}{\int }_{0}^{+\infty }\frac{\mathrm{d}t}{a + b{t}^{2}}\;\left( {t = \tan \theta }\right)
\]

\[
= {\left. \frac{8}{\sqrt{c}}\frac{1}{\sqrt{ab}}\arctan \left( \sqrt{\frac{b}{a}}t\right) \right| }_{0}^{+\infty } = \frac{4\pi }{\sqrt{abc}}.
\]

注 利用 Gauss 公式来计算曲面积分在很多情况下是一种有效的手段, 但要注意使用 Gauss 公式的条件,要弄清楚在什么情况下要“挖洞” (即用封闭曲面把 \( P \) , \( Q, R \) 无定义或不可微的点围住) 以及选择什么曲面 “挖洞” 计算更简便.

利用 Gauss 公式可导出用曲面积分表示 \( {\mathbf{R}}^{3} \) 中具有逐片光滑边界的有界闭区域 \( \Omega \) 的体积公式

\[
\left| \Omega \right|  = {\oiint }_{\partial \Omega }x\mathrm{\;d}y\mathrm{\;d}z = {\oiint }_{\partial \Omega }y\mathrm{\;d}z\mathrm{\;d}x = {\oiint }_{\partial \Omega }z\mathrm{\;d}x\mathrm{\;d}y
\]

\[
= \frac{1}{3}{\oiint }_{\partial \Omega }x\mathrm{\;d}y\mathrm{\;d}z + y\mathrm{\;d}z\mathrm{\;d}x + z\mathrm{\;d}x\mathrm{\;d}y \tag{25.7}
\]

上述积分在 \( \partial \Omega \) 的外侧进行. 由两类曲面积分之间的关系,又有

\[
\left| \Omega \right|  = \frac{1}{3}{\oiint }_{\partial \Omega }\left( {x\cos \alpha  + y\cos \beta  + z\cos \gamma }\right) \mathrm{d}S, \tag{25.8}
\]

其中 \( \left( {\cos \alpha ,\cos \beta ,\cos \gamma }\right) \) 为 \( \partial \Omega \) 的单位外法向量. 如果 \( \partial \Omega \) 有参数表示

\[
x = x\left( {u, v}\right) ,\;y = y\left( {u, v}\right) ,\;z = z\left( {u, v}\right) ,\;\left( {u, v}\right)  \in  D,
\]

\[
V = \frac{1}{3}\left| {{\iint }_{D}\left( {{Ax} + {By} + {Cz}}\right) \mathrm{d}u\mathrm{\;d}v}\right| \tag{25.9}
\]

则

其中

\[
A = \frac{\partial \left( {y, z}\right) }{\partial \left( {u, v}\right) },\;B = \frac{\partial \left( {z, x}\right) }{\partial \left( {u, v}\right) },\;C = \frac{\partial \left( {x, y}\right) }{\partial \left( {u, v}\right) }.
\]

(25.9) 也可以写为

\[
V = \frac{1}{3}\left| {{\iint }_{D}\left| \begin{matrix} x & y & z \\  {x}_{u} & {y}_{u} & {z}_{u} \\  {x}_{v} & {y}_{v} & {z}_{v} \end{matrix}\right| \mathrm{d}u\mathrm{\;d}v}\right| \tag{25.10}
\]

特别地, 若一个立体的表面在球坐标系中由方程

\[
r = r\left( {\varphi ,\theta }\right) ,\;\left( {\varphi ,\theta }\right)  \in  D
\]

给出，则

\( x = r\left( {\varphi ,\theta }\right) \sin \varphi \cos \theta , y = r\left( {\varphi ,\theta }\right) \sin \varphi \sin \theta , z = r\left( {\varphi ,\theta }\right) \cos \varphi ,\left( {\varphi ,\theta }\right)  \in  D \) .

代入公式 (25.10) 中得到

\[
V = \frac{1}{3}{\iint }_{D}{r}^{3}\left( {\varphi ,\theta }\right) \sin \varphi \mathrm{d}\varphi \mathrm{d}\theta . \tag{25.11}
\]

当然, 公式 (25.11) 也可以从三重积分中直接得到, 事实上

\[
V = {\iiint }_{\Omega }\mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z = {\iiint }_{\begin{matrix} {\left( {\varphi ,\theta }\right)  \in  D} \\  {0 \leq  \rho  \leq  r\left( {\theta ,\varphi }\right) } \end{matrix}}{\rho }^{2}\sin \varphi \mathrm{d}\rho \mathrm{d}\theta \mathrm{d}\varphi
\]

\[
= {\iint }_{D}\sin \varphi \mathrm{d}\varphi \mathrm{d}\theta {\int }_{0}^{r\left( {\varphi ,\theta }\right) }{\rho }^{2}\mathrm{\;d}\rho
\]

\[
= \frac{1}{3}{\iint }_{D}{r}^{3}\left( {\varphi ,\theta }\right) \sin \varphi \mathrm{d}\varphi \mathrm{d}\theta .
\]

#### 25.3.2 练习题

1. 利用 Gauss 公式计算积分:

(1) \( {\oiint }_{S}y\left( {x - z}\right) \mathrm{d}y\mathrm{\;d}z + {z}^{2}\mathrm{\;d}z\mathrm{\;d}x + \left( {{y}^{2} + {xz}}\right) \mathrm{d}x\mathrm{\;d}y \) ,其中 \( S \) 是正立方体 \( \{ \left( {x, y, z}\right)  \mid \; 0 \leq  x \leq  a,0 \leq  y \leq  a,0 \leq  z \leq  a\} \left( {a > 0}\right) \) 的表面,取内侧.

(2) \( {\oiint }_{\sum }\left( {{x}^{3} + x}\right) \mathrm{d}y\mathrm{\;d}z + \left( {{y}^{2} - {xz}}\right) \mathrm{d}z\mathrm{\;d}x + \left( {{z}^{3} + z}\right) \mathrm{d}x\mathrm{\;d}y \) ,其中 \( \sum \) 是球面 \( {x}^{2} + \; {y}^{2} + {z}^{2} = {2z} \) ,取外侧.

(3) 设 \( {A}_{1} = {x}^{3} - {x}^{2}y + {z}^{3},{A}_{2} = x{y}^{2} + {y}^{3},{A}_{3} = {xz} + {z}^{2},\sum \) 是由 \( {yOz} \) 平面上的抛物线 \( z = 1 - {y}^{2} \) 与 \( z = 0 \) 所围成的平面区域绕 \( z \) 轴旋转后所得的旋转体的表面, 取外侧. 试求

\[
{\oiint }_{\sum }\left( {\frac{\partial {A}_{3}}{\partial y} - \frac{\partial {A}_{2}}{\partial z}}\right) \mathrm{d}y\mathrm{d}z + \left( {\frac{\partial {A}_{1}}{\partial z} - \frac{\partial {A}_{3}}{\partial x}}\right) \mathrm{d}z\mathrm{d}x + \left( {\frac{\partial {A}_{2}}{\partial x} - \frac{\partial {A}_{1}}{\partial y}}\right) \mathrm{d}x\mathrm{d}y.
\]

2. 先添加辅助面, 再用 Gauss 公式计算下列曲面积分:

(1) \( {\iint }_{\sum }\left( {{x}^{2}\cos \alpha  + {y}^{2}\cos \beta  + {z}^{2}\cos \gamma }\right) \mathrm{d}S \) ,其中 \( \sum \) 是锥面 \( {z}^{2} = {x}^{2} + {y}^{2} \) 在 \( 0 \leq  z \leq  h \) 的一段， \( \left( {\cos \alpha ,\cos \beta ,\cos \gamma }\right) \) 为 \( \sum \) 上的单位法向量，其方向为下方.

(2) \( {\iint }_{\sum }{x}^{3}\mathrm{\;d}y\mathrm{\;d}z + {y}^{3}\mathrm{\;d}z\mathrm{\;d}x + {z}^{3}\mathrm{\;d}x\mathrm{\;d}y \) ,其中 \( \sum \) 为球面 \( {x}^{2} + {y}^{2} + {z}^{2} = {a}^{2} \) 之上半部分，取上侧.

(3) \( {\iint }_{\sum }\left( {\frac{{x}^{3}}{{a}^{3}} + {y}^{3}{z}^{3}}\right) \mathrm{d}y\mathrm{\;d}z + \left( {\frac{{y}^{3}}{{b}^{3}} + {z}^{3}{x}^{3}}\right) \mathrm{d}z\mathrm{\;d}x + \left( {\frac{{z}^{3}}{{c}^{3}} + {x}^{3}{y}^{3}}\right) \mathrm{d}x\mathrm{\;d}y \) ,其中 \( \sum \) 为椭球面 \( \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} + \frac{{z}^{2}}{{c}^{2}} = 1, x \geq  0 \) ,取后侧.

3. \( F\left( {x, y, z}\right) \) 是定义在 \( {\mathbf{R}}^{3} \) 上的光滑函数,且 \( F\left( {x, y, z}\right)  = 0 \) 是一个以原点为顶点的锥面 \( \sum \) ,如果 \( \sum \) 与平面 \( \Pi  : {Ax} + {By} + {Cz} = D \) 围成一个锥体,证明: 此锥体的体积

\[
V = \frac{1}{3}{SH}
\]

其中 \( S \) 为平面 \( \Pi \) 上锥底部分的面积, \( H \) 为顶点到锥底的高.

4. 求由曲面 \( {\left( {x}^{2} + {y}^{2} + {z}^{2}\right) }^{2} = {a}^{2}{xy} \) 所围成的立体的体积.

5. 求 \( {\iint }_{\sum }\left( {{x}^{3} + {y}^{3}}\right) \mathrm{d}y\mathrm{\;d}z + \left( {{x}^{3} + 2{x}^{2}y}\right) \mathrm{d}z\mathrm{\;d}x - {x}^{2}z\mathrm{\;d}x\mathrm{\;d}y \) ,其中 \( \sum \) 是单叶双曲面 \( {x}^{2} + {y}^{2} - {z}^{2} = 1 \) 在 \( 0 \leq  z \leq  \sqrt{3} \) 的部分,取外侧.

6. \( V = \left\{  {\left( {x, y, z}\right)  \mid  {x}^{2} + {y}^{2} < z < 1}\right\}  , S = \partial V \) ,求积分

\[
{\oiint }_{S}{yz}\mathrm{\;d}z\mathrm{\;d}x + \left( {{x}^{2} + {y}^{2}}\right) z\mathrm{\;d}x\mathrm{\;d}y
\]

积分沿外法线方向.

7. 求第二型曲面积分

\[
{\oiint }_{S}z\mathrm{\;d}y\mathrm{\;d}z + \cos y\mathrm{\;d}z\mathrm{\;d}x + \mathrm{d}x\mathrm{\;d}y
\]

其中 \( S \) 为 \( {x}^{2} + {y}^{2} + {z}^{2} = 1 \) 的外侧.

#### 25.3.3 Stokes 公式

Stokes 公式是将空间曲面上的第二型曲面积分与该曲面边界上的第二型曲线积分之间建立联系的一个重要公式.

设 \( D \) 是 \( {\mathbf{R}}^{3} \) 中的分片光滑曲面, \( D \) 的边界 \( \partial D \) 由分段光滑曲线组成,又设 \( P, Q, R \) 有关于 \( x, y, z \) 的连续偏导数,则成立下列 Stokes 公式:

\[
{\oint }_{\partial D}P\mathrm{\;d}x + Q\mathrm{\;d}y + R\mathrm{\;d}z = {\iint }_{D}\left| \begin{matrix} \mathrm{d}y\mathrm{\;d}z & \mathrm{\;d}z\mathrm{\;d}x & \mathrm{\;d}x\mathrm{\;d}y \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  P & Q & R \end{matrix}\right| , \tag{25.12}
\]

其中 \( \partial D \) 的方向和 \( D \) 的方向服从右手法则. 由两类曲面积分之间的关系 (25.4), (25.12) 又可以写为

\[
{\oint }_{\partial D}P\mathrm{\;d}x + Q\mathrm{\;d}y + R\mathrm{\;d}z = {\iint }_{D}\left| \begin{matrix} \cos \alpha & \cos \beta & \cos \gamma \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  P & Q & R \end{matrix}\right| \mathrm{d}S, \tag{25.13}
\]

其中 \( \cos \alpha ,\cos \beta ,\cos \gamma \) 是曲面 \( D \) 上法向量的方向余弦. 如果曲面 \( D \) 在 \( {xOy} \) 平面上, 则公式 (25.12), (25.13) 就是 Green 公式. 公式 (25.12) 与 (25.13) 给我们提供了一个求曲线积分与曲面积分的新方法.

例题 25.3.3 求

\[
I = {\oint }_{C}\left( {{y}^{2} - {z}^{2}}\right) \mathrm{d}x + \left( {{z}^{2} - {x}^{2}}\right) \mathrm{d}y + \left( {{x}^{2} - {y}^{2}}\right) \mathrm{d}z,
\]

其中 \( C \) 是立方体 \( \{ \left( {x, y, z}\right)  \mid  0 \leq  x \leq  a,0 \leq  y \leq  a,0 \leq  z \leq  a\} \) 的表面与平面 \( x + y + z = \frac{3}{2}a \) 的交线,取向从 \( z \) 轴正向看去是逆时针方向.

分析 见图 25.6,分六段积分的计算量很大,且 \( C \) 也不便于表示为一个统一的参数式. 因 \( C \) 为闭曲线,且 \( P = {y}^{2} - {z}^{2}, Q = {z}^{2} - {x}^{2}, R = {x}^{2} - {y}^{2} \) 连续可微,故考虑用 Stokes 公式.

![bo_d7fsu8491nqc7381io7g_364_892_235_553_548_0.jpg](images/xie_analysis_exercises_lower_034_bod7fsu8491nqc7381io7g3648922355535480.jpg)

图 25.6

解 令 \( \sum \) 为 \( x + y + z = \frac{3}{2}a \) 被 \( C \) 所围的一块,取上侧,则 \( C \) 的取向与 \( \sum \) 的取侧相容. 应用 Stokes 公式 (25.13),

\[
I = {\iint }_{\sum }\left| \begin{matrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  {y}^{2} - {z}^{2} & {z}^{2} - {x}^{2} & {x}^{2} - {y}^{2} \end{matrix}\right| \mathrm{d}S
\]

\[
= \frac{1}{\sqrt{3}}{\iint }_{\sum } - 4\left( {x + y + z}\right) \mathrm{d}S
\]

\[
=  - \frac{4}{\sqrt{3}}{\iint }_{\sum }\frac{3}{2}a\mathrm{\;d}S =  - 2\sqrt{3}a \cdot  \left| \sum \right|
\]

\[
=  - 2\sqrt{3}a \cdot  \frac{3\sqrt{3}}{4}{a}^{2} =  - \frac{9}{2}{a}^{3}.
\]

例题 25.3.4 设 \( \sum \) 是分片光滑的闭曲面, \( \mathbf{n} \) 为 \( \sum \) 上的单位外法向量,证明:

\[
I = {\oiint }_{\sum }\left| \begin{matrix} \cos \left( {\mathbf{n}, x}\right) & \cos \left( {\mathbf{n}, y}\right) & \cos \left( {\mathbf{n}, z}\right) \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  P & Q & R \end{matrix}\right| \mathrm{d}S = 0,
\]

其中分两种情形: (1) \( P, Q, R \) 在 \( \overline{\Omega } \) 上二阶连续可微, \( \Omega \) 为 \( \sum \) 所围的立体; (2) \( P, Q, R \) 在 \( \sum \) 上一阶连续可微.

![bo_d7fsu8491nqc7381io7g_364_1023_1350_422_536_0.jpg](images/xie_analysis_exercises_lower_033_bod7fsu8491nqc7381io7g364102313504225360.jpg)

图 25.7

证 对情形 (1) 用 Gauss 公式

\[
I = {\oiint }_{\sum }\left( {\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}}\right) \mathrm{d}y\mathrm{\;d}z + \left( {\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}}\right) \mathrm{d}z\mathrm{\;d}x
\]

\[
+ \left( {\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}}\right) \mathrm{d}x\mathrm{\;d}y
\]

\[
= {\iiint }_{\Omega }\left\lbrack  {\frac{\partial }{\partial x}\left( {\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}}\right)  + \frac{\partial }{\partial y}\left( {\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}}\right) }\right.
\]

\[
\left. {+\frac{\partial }{\partial z}\left( {\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}}\right) }\right\rbrack  \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z
\]

\[
= 0\text{ . }
\]

情形 (2) 参见图 25.7. 在 \( \sum \) 上任取一条逐段光滑的闭曲线 \( C, C \) 分 \( \sum \) 为两部分 \( {\sum }_{1} \) 与 \( {\sum }_{2} \) ,在 \( {\sum }_{1},{\sum }_{2} \) 上分别应用 Stokes 公式,则对于 \( i = 1,2 \) ,

\[
{\iint }_{{\sum }_{i}}\left| \begin{matrix} \cos \left( {\mathbf{n}, x}\right) & \cos \left( {\mathbf{n}, y}\right) & \cos \left( {\mathbf{n}, z}\right) \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  P & Q & R \end{matrix}\right| \mathrm{d}S = {\oint }_{{C}_{i}}P\mathrm{\;d}x + Q\mathrm{\;d}y + R\mathrm{\;d}z.
\]

因 \( {\sum }_{1},{\sum }_{2} \) 分居 \( C \) 两侧,故 \( {C}_{1},{C}_{2} \) 为同一条曲线 \( C \) ,只是它们的定向相反. 若记 \( {C}_{1} \) 为 \( {C}_{ + } \) ,则 \( {C}_{2} \) 为 \( {C}_{ - } \) ,从而

\[
I = \left( {{\iint }_{{\sum }_{1}} + {\iint }_{{\sum }_{2}}}\right) \left| \begin{matrix} \cos \left( {\mathbf{n}, x}\right) & \cos \left( {\mathbf{n}, y}\right) & \cos \left( {\mathbf{n}, z}\right) \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  P & Q & R \end{matrix}\right| \mathrm{d}S
\]

\[
= \left( {{\oint }_{{C}_{ + }} + {\oint }_{{C}_{ - }}}\right) P\mathrm{\;d}x + Q\mathrm{\;d}y + R\mathrm{\;d}z = 0.
\]

例题 25.3.5 试用 Stokes 公式计算

\[
I = {\oint }_{C}\left( {{y}^{2} + {z}^{2}}\right) \mathrm{d}x + \left( {{z}^{2} + {x}^{2}}\right) \mathrm{d}y + \left( {{x}^{2} + {y}^{2}}\right) \mathrm{d}z,
\]

其中 \( C \) 为 \( {x}^{2} + {y}^{2} + {z}^{2} = {2Rx} \) 与 \( {x}^{2} + {y}^{2} = {2rx} \) 的交线 \( \left( {0 < r < R, z > 0}\right) , C \) 的定向使得 \( C \) 所包围的球面上较小区域保持在左边.

解 见图 25.4,设 \( S \) 为球面 \( {x}^{2} + {y}^{2} + {z}^{2} = {2Rx} \) 被柱面 \( {x}^{2} + {y}^{2} = {2rx} \) 所截部分的外侧, 由 Stokes 公式 (25.13)

\[
I = {\iint }_{S}\left| \begin{matrix} \frac{x - R}{R} & \frac{y}{R} & \frac{z}{R} \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  {y}^{2} + {z}^{2} & {z}^{2} + {x}^{2} & {x}^{2} + {y}^{2} \end{matrix}\right| \mathrm{d}S
\]

\[
= \frac{2}{R}{\iint }_{S}\left\lbrack  {\left( {y - z}\right) \left( {x - R}\right)  + \left( {z - x}\right) y + \left( {x - y}\right) z}\right\rbrack  \mathrm{d}S
\]

\[
= 2{\iint }_{S}\left( {z - y}\right) \mathrm{d}S = 2{\iint }_{S}z\mathrm{\;d}S = {2R}{\iint }_{{x}^{2} + {y}^{2} \leq  {2rx}}\mathrm{\;d}x\mathrm{\;d}y = {2\pi }{r}^{2}R.
\]

#### 25.3.4 练习题

1. 设 \( C \) 是平面 \( x\cos \alpha  + y\cos \beta  + z\cos \gamma  - p = 0 \) 上逐段光滑的闭曲线, \( C \) 所界的面积为 \( S, C \) 的定向与 \( \left( {\cos \alpha ,\cos \beta ,\cos \gamma }\right) \) 成右手系,试计算积分

\[
{\oint }_{C}\left| \begin{matrix} \mathrm{d}x & \mathrm{\;d}y & \mathrm{\;d}z \\  \cos \alpha & \cos \beta & \cos \gamma \\  x & y & z \end{matrix}\right| .
\]

2. 求 \( {\oint }_{C}\left( {y - z}\right) \mathrm{d}x + \left( {z - x}\right) \mathrm{d}y + \left( {x - y}\right) \mathrm{d}z, C \) 为 \( {x}^{2} + {y}^{2} = 1 \) 与 \( x + y + z = 1 \) 的交线,从 \( x \) 轴正向看是逆时针方向.

3. 求 \( {\int }_{C}\left( {{z}^{3} + 3{x}^{2}y}\right) \mathrm{d}x + \left( {{x}^{3} + 3{y}^{2}z}\right) \mathrm{d}y + \left( {{y}^{3} + 3{z}^{2}x}\right) \mathrm{d}z \) ,其中 \( C \) 是 \( z = \sqrt{{a}^{2} - {x}^{2} - {y}^{2}} \) 与 \( x = y \) 的交线,自 \( A\left( {\frac{a}{\sqrt{2}},\frac{a}{\sqrt{2}},0}\right) \) 到 \( B\left( {-\frac{a}{\sqrt{2}}, - \frac{a}{\sqrt{2}},0}\right) \) .

4. 用 Stokes 公式求 \( {\int }_{C}{\mathrm{e}}^{x + z}\left\{  {\left\lbrack  {\left( {x + 1}\right) {y}^{2} + 1}\right\rbrack  \mathrm{d}x + {2xy}\mathrm{\;d}y + x{y}^{2}\mathrm{\;d}z}\right\} \) ,其中 \( C \) 是右半柱面 \( \left| x\right|  + \left| y\right|  = a\left( {y > 0}\right) \) 与平面 \( y = z \) 的交线上从 \( \left( {-a,0,0}\right) \) 到 \( \left( {a,0,0}\right) \) 的一段 \( \left( {a > 0}\right) \) .

5. 设 \( C \) 是空间任一逐段光滑的简单闭曲线, \( f\left( x\right) , g\left( x\right) , h\left( x\right) \) 是任意连续函数. 证明:

\[
{\oint }_{C}\left\lbrack  {f\left( x\right)  - {yz}}\right\rbrack  \mathrm{d}x + \left\lbrack  {g\left( y\right)  - {xz}}\right\rbrack  \mathrm{d}y + \left\lbrack  {h\left( z\right)  - {xy}}\right\rbrack  \mathrm{d}z = 0.
\]

6. 求

\[
{\iint }_{\sum }\left| \begin{matrix} \cos \alpha & \cos \beta & \cos \gamma \\  \frac{\partial }{\partial x} & \frac{\partial }{\partial y} & \frac{\partial }{\partial z} \\  x - z & {x}^{3} - {yz} &  - {3x}{y}^{2} \end{matrix}\right| \mathrm{d}S,
\]

其中 \( \sum \) 是 \( {x}^{2} + {y}^{2} + {z}^{2} = {R}^{2} \) 在 \( z \geq  0 \) 的部分, \( \left( {\cos \alpha ,\cos \beta ,\cos \gamma }\right) \) 是 \( \sum \) 下侧的单位法向量.

7. 求 \( {\oint }_{C}y\mathrm{\;d}x + z\mathrm{\;d}y + x\mathrm{\;d}z \) ,其中 \( C \) 是 \( {x}^{2} + {y}^{2} + {z}^{2} = {a}^{2} \) 与 \( x + y + z = 0 \) 的交线, 从 \( z \) 轴正向看是逆时针方向.

## \( {25.3.5}{\mathrm{R}}^{3} \) 中曲线积分与路径无关的条件

利用 Stokes 公式可将 24.3.2 小节中平面曲线积分与路径无关的条件推广到 \( {\mathbf{R}}^{3} \) 中,但首先要清楚什么是 \( {\mathbf{R}}^{3} \) 中的“单连通区域”,为此我们要求无论 \( L \) 是区域 \( \Omega \) 内的什么样的简单闭路,总存在一个以 \( L \) 为边界而且全部包含在 \( \Omega \) 内的曲面 \( S \) . 这时称空间区域 \( \Omega \) 是曲面单连通区域. 例如两个同心球面之间的部分是曲面单连通区域；一个球打了一个贯通的柱形孔洞后剩下的部分，如

\[
\Omega  = \left\{  {\left( {x, y, z}\right)  \mid  {x}^{2} + {y}^{2} + {z}^{2} \leq  1,{x}^{2} + {y}^{2} \geq  \frac{1}{2}}\right\}
\]

不是曲面单连通区域; \( {\mathbf{R}}^{3} \) 中的圆环面

\[
{T}^{2} : {\left( \sqrt{{x}^{2} + {y}^{2}} - a\right) }^{2} + {z}^{2} = {b}^{2}\;\left( {0 < b < a}\right)
\]

所围的区域也不是曲面单连通区域.

如果 \( D \) 是 \( {\mathbf{R}}^{3} \) 中的曲面单连通区域, \( w = P\left( {x, y, z}\right) \mathrm{d}x + Q\left( {x, y, z}\right) \mathrm{d}y + \; R\left( {x, y, z}\right) \mathrm{d}z \) ,其中 \( P, Q, R \) 都在 \( D \) 上有连续偏导数,则下列结论等价:

(1)对 \( D \) 内任意一条闭曲线 \( C \) ,有

\[
{\oint }_{C}w = 0
\]

(2)对 \( D \) 内的任意一条路径 \( C,{\int }_{C}w \) 仅与 \( C \) 的起点和终点有关，而与所沿的路径无关;

(3)在 \( D \) 内(处处)成立

\[
\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y},\frac{\partial R}{\partial y} = \frac{\partial Q}{\partial z},\frac{\partial P}{\partial z} = \frac{\partial R}{\partial x};
\]

(4) 存在势函数 \( \varphi \left( {x, y, z}\right) \) ,使得在 \( D \) 内成立

\[
\mathrm{d}\varphi \left( {x, y, z}\right)  = P\left( {x, y, z}\right) \mathrm{d}x + Q\left( {x, y, z}\right) \mathrm{d}y + R\left( {x, y, z}\right) \mathrm{d}z,
\]

且

\[
\varphi \left( {x, y, z}\right)  = {\int }_{{x}_{0}}^{x}P\left( {x, y, z}\right) \mathrm{d}x + {\int }_{{y}_{0}}^{y}Q\left( {{x}_{0}, y, z}\right) \mathrm{d}y
\]

\[
+ {\int }_{{z}_{0}}^{z}R\left( {{x}_{0},{y}_{0}, z}\right) \mathrm{d}z + C \tag{25.14}
\]

\[
{\int }_{\left( {x}_{0},{y}_{0},{z}_{0}\right) }^{\left( x, y, z\right) }P\mathrm{\;d}x + Q\mathrm{\;d}y + R\mathrm{\;d}z = {\left. \varphi \right| }_{\left( {x}_{0},{y}_{0},{z}_{0}\right) }^{\left( x, y, z\right) } = \varphi \left( {x, y, z}\right)  - \varphi \left( {{x}_{0},{y}_{0},{z}_{0}}\right) .
\]

例题 25.3.6 对于微分式

\[
z\left( {\frac{1}{{x}^{2}y} - \frac{1}{{x}^{2} + {z}^{2}}}\right) \mathrm{d}x + \frac{z}{x{y}^{2}}\mathrm{\;d}y + \left( {\frac{x}{{x}^{2} + {z}^{2}} - \frac{1}{xy}}\right) \mathrm{d}z,
\]

判断原函数的存在性并求出之.

解 1 容易验证

\[
\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} =  - \frac{z}{{x}^{2}{y}^{2}}
\]

\[
\frac{\partial Q}{\partial z} = \frac{\partial R}{\partial y} = \frac{1}{x{y}^{2}}
\]

\[
\frac{\partial R}{\partial x} = \frac{\partial P}{\partial z} = \frac{1}{{x}^{2}y} + \frac{{z}^{2} - {x}^{2}}{{\left( {x}^{2} + {z}^{2}\right) }^{2}}
\]

因此该微分式有原函数. 根据微分式的特点,为计算简单起见取 \( {z}_{0} = 0,{x}_{0},{y}_{0} > 0 \) , 积分路径为 \( \left( {{x}_{0},{y}_{0},0}\right)  \rightarrow  \left( {x,{y}_{0},0}\right)  \rightarrow  \left( {x, y,0}\right)  \rightarrow  \left( {x, y, z}\right) \) ,则

\[
\varphi \left( {x, y, z}\right)  = {\int }_{0}^{z}\left( {\frac{x}{{x}^{2} + {z}^{2}} - \frac{1}{xy}}\right) \mathrm{d}z + C = \arctan \frac{z}{x} - \frac{z}{xy} + C.
\]

解 2 求原函数时也可用下面求不定积分的方法: 由

\[
\frac{\partial \varphi }{\partial z} = \frac{x}{{x}^{2} + {z}^{2}} - \frac{1}{xy},
\]

则

\[
\varphi \left( {x, y, z}\right)  = \int \left( {\frac{x}{{x}^{2} + {z}^{2}} - \frac{1}{xy}}\right) \mathrm{d}z = \arctan \frac{z}{x} - \frac{z}{xy} + \psi \left( {x, y}\right) .
\]

由此得

\[
\frac{\partial \varphi }{\partial x} =  - \frac{z}{{x}^{2} + {z}^{2}} + \frac{z}{{x}^{2}y} + \frac{\partial \psi }{\partial x}
\]

\[
\frac{\partial \varphi }{\partial y} = \frac{z}{x{y}^{2}} + \frac{\partial \psi }{\partial y}
\]

由 \( \frac{\partial \varphi }{\partial x} = P,\frac{\partial \varphi }{\partial y} = Q \) ,得

\[
\frac{\partial \psi }{\partial x} = \frac{\partial \psi }{\partial y} = 0
\]

即 \( \psi \left( {x, y}\right) \) 为常数,所以

\[
\varphi \left( {x, y, z}\right)  = \arctan \frac{z}{x} - \frac{z}{xy} + C.
\]

#### 25.3.6 练习题

1. 证明: 下列微分式为全微分, 并求出其原函数:

(1) \( \left( {{x}^{2} - {2yz}}\right) \mathrm{d}x + \left( {{y}^{2} - {2xz}}\right) \mathrm{d}y + \left( {{z}^{2} - {2xy}}\right) \mathrm{d}z \) ;

(2) \( \left\lbrack  {\frac{x}{{\left( {x}^{2} - {y}^{2}\right) }^{2}} - \frac{1}{x} + 2{x}^{2}}\right\rbrack  \mathrm{d}x + \left\lbrack  {\frac{1}{y} - \frac{y}{{\left( {x}^{2} - {y}^{2}\right) }^{2}} + 3{y}^{3}}\right\rbrack  \mathrm{d}y + 5{z}^{3}\mathrm{\;d}z \) .

2. 求 \( {\int }_{\left( 1,2,3\right) }^{\left( 6,1,1\right) }{yz}\mathrm{\;d}x + {xz}\mathrm{\;d}y + {xy}\mathrm{\;d}z \) .

3. 设 \( C \) 是由球面 \( {x}^{2} + {y}^{2} + {z}^{2} = {a}^{2} \) 上的任一点沿任一路径运动到球面 \( {x}^{2} + {y}^{2} + {z}^{2} = \; {b}^{2}\left( {b > a}\right) \) 上的任一点的轨迹, \( C \) 分段光滑,证明:

\[
{\int }_{C}{r}^{3}\left( {x\mathrm{\;d}x + y\mathrm{\;d}y + z\mathrm{\;d}z}\right)  = \frac{1}{5}\left( {{b}^{5} - {a}^{5}}\right) ,
\]

其中 \( r = \sqrt{{x}^{2} + {y}^{2} + {z}^{2}} \) .
