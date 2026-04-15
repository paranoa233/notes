## §26.2 Laplace 算子与调和函数

#### 26.2.1 Laplace 算子

Laplace 算子 \( \Delta \) 的定义如下:

\[
\text{ 在 }{\mathbf{R}}^{2}\text{ 中: }\;{\Delta u} = \frac{{\partial }^{2}u}{\partial {x}^{2}} + \frac{{\partial }^{2}u}{\partial {y}^{2}}\text{ ; }
\]

\[
\text{ 在 }{\mathbf{R}}^{3}\text{ 中: }\;{\Delta u} = \frac{{\partial }^{2}u}{\partial {x}^{2}} + \frac{{\partial }^{2}u}{\partial {y}^{2}} + \frac{{\partial }^{2}u}{\partial {z}^{2}}\text{ . }
\]

简单的计算表明,

\[
{\Delta u} = \nabla  \cdot  \nabla u
\]

即 Laplace 算子对一个函数的作用等于这个函数的梯度的散度.

例题 26.2.1 (第一 Green 恒等式) 设 \( \sum \) 为区域 \( \Omega \) 的边界曲面,分片光滑, \( u, v \) 在 \( \overline{\Omega } \) 上二阶连续可微,证明:

\[
{\iiint }_{\Omega }{\Delta u} \cdot  v\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z + {\iiint }_{\Omega }\nabla u \cdot  \nabla v\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z = {\oiint }_{\sum }v\frac{\partial u}{\partial \mathbf{n}}\mathrm{d}S,
\]

其中 \( \mathbf{n} \) 为 \( \sum \) 上的单位外法向量, \( \frac{\partial u}{\partial \mathbf{n}} \) 是 \( u \) 在 \( \mathbf{n} \) 方向上的方向导数.

证 根据方向导数的计算公式,

\[
{\oiint }_{\sum }v\frac{\partial u}{\partial \mathbf{n}}\mathrm{d}S = {\oiint }_{\sum }v\left\lbrack  {\frac{\partial u}{\partial x}\cos \left( {\mathbf{n}, x}\right)  + \frac{\partial u}{\partial y}\cos \left( {\mathbf{n}, y}\right)  + \frac{\partial u}{\partial z}\cos \left( {\mathbf{n}, z}\right) }\right\rbrack  \mathrm{d}S.
\]

利用公式 (26.2), 则

\[
{\oiint }_{\sum }v\frac{\partial u}{\partial n}\mathrm{\;d}S = {\iiint }_{\Omega }\left\lbrack  {\frac{\partial }{\partial x}\left( {v{u}_{x}}\right)  + \frac{\partial }{\partial y}\left( {v{u}_{y}}\right)  + \frac{\partial }{\partial z}\left( {v{u}_{z}}\right) }\right\rbrack  \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z
\]

\[
= {\iiint }_{\Omega }{\Delta u} \cdot  v\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z + {\iiint }_{\Omega }\nabla u \cdot  \nabla v\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z.
\]

注 1 令 \( v = 1 \) ,则有

\[
{\oiint }_{\sum }\frac{\partial u}{\partial \mathbf{n}}\mathrm{d}S = {\iiint }_{\Omega }{\Delta u}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z. \tag{26.15}
\]

注 2 由第一 Green 恒等式可以证明第二 Green 恒等式, 见 26.2.4 小节的练习题 2.

例题 26.2.2 设 \( h\left( {x, y, z}\right) \) 在 \( {\mathbf{R}}^{3} \) 上二阶连续可微, \( \partial {B}_{r}\left( \mathbf{M}\right) \) 是以 \( \mathbf{M} = \left( {x, y, z}\right) \) 为心, \( r \) 为半径的球面,定义

\[
{\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = \frac{1}{{4\pi }{r}^{2}}{\oiint }_{\partial {B}_{r}\left( \mathbf{M}\right) }h\left( {\xi ,\eta ,\zeta }\right) \mathrm{d}{S}_{r},
\]

其中 \( r > 0 \) ,证明:

(1) \( {\mathbf{M}}_{h} \) 是 \( x, y, z, r \) 的二次连续可微函数;

(2) \( \Delta {\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = \left( {\frac{{\partial }^{2}}{\partial {r}^{2}} + \frac{2}{r}\frac{\partial }{\partial r}}\right) {\mathbf{M}}_{h}\left( {x, y, z, r}\right) \) , 其中 \( \Delta  = \frac{{\partial }^{2}}{\partial {x}^{2}} + \frac{{\partial }^{2}}{\partial {y}^{2}} + \frac{{\partial }^{2}}{\partial {z}^{2}} \) ;

(3) \( \mathop{\lim }\limits_{{r \rightarrow  {0}^{ + }}}\frac{\partial }{\partial r}{\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = 0 \) .

证 (1) 由 (25.27), \( {\mathbf{M}}_{h} \) 的表达式可改写为

\[
{\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = \frac{1}{4\pi }{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }h\left( {x + r{\alpha }_{1}, y + r{\alpha }_{2}, z + r{\alpha }_{3}}\right) \mathrm{d}{S}_{1},
\]

其中 \( \left( {{\alpha }_{1},{\alpha }_{2},{\alpha }_{3}}\right) \) 是球面 \( \partial {B}_{1}\left( \mathbf{0}\right) \) 的单位外法向量, \( \mathrm{d}{S}_{1} \) 是 \( \partial {B}_{1}\left( \mathbf{0}\right) \) 的面积元. 由含参变量积分的性质知 \( {\mathbf{M}}_{h} \) 是 \( x, y, z, r \) 的二次连续可微函数.

(2)由含参变量积分的求导公式得

\[
\Delta {\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = \frac{1}{4\pi }{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }{\Delta h}\left( {x + r{\alpha }_{1}, y + r{\alpha }_{2}, z + r{\alpha }_{3}}\right) \mathrm{d}{S}_{1}, \tag{26.16}
\]

\[
\frac{\partial {\mathbf{M}}_{h}}{\partial r} = \frac{1}{4\pi }{\oiint }_{\partial {B}_{1}\left( \mathbf{0}\right) }\left( {\frac{\partial h}{\partial x}{\alpha }_{1} + \frac{\partial h}{\partial y}{\alpha }_{2} + \frac{\partial h}{\partial z}{\alpha }_{3}}\right) \mathrm{d}{S}_{1}
\]

\[
= \frac{1}{{4\pi }{r}^{2}}{\oiint }_{\partial {B}_{r}\left( \mathbf{0}\right) }\left( {\frac{\partial h}{\partial x}{\alpha }_{1} + \frac{\partial h}{\partial y}{\alpha }_{2} + \frac{\partial h}{\partial z}{\alpha }_{3}}\right) \mathrm{d}{S}_{r}. \tag{26.17}
\]

应用 Gauss 公式 (26.2), 则

\[
\frac{\partial {\mathbf{M}}_{h}}{\partial r} = \frac{1}{{4\pi }{r}^{2}}{\iiint }_{{B}_{r}\left( \mathbf{M}\right) }{\Delta h}\left( {\xi ,\eta ,\zeta }\right) \mathrm{d}\xi \mathrm{d}\eta \mathrm{d}\zeta . \tag{26.18}
\]

应用例题 \( {25.5.3}\left( 2\right) \) 中的结果,则

\[
\frac{{\partial }^{2}{\mathbf{M}}_{h}}{\partial {r}^{2}} =  - \frac{1}{{2\pi }{r}^{3}}{\iiint }_{{B}_{r}\left( \mathbf{M}\right) }{\Delta h}\left( {\xi ,\eta ,\zeta }\right) \mathrm{d}\xi \mathrm{d}\eta \mathrm{d}\zeta  + \frac{1}{{4\pi }{r}^{2}}{\iiint }_{\partial {B}_{r}\left( \mathbf{M}\right) }{\Delta h}\left( {\xi ,\eta ,\zeta }\right) \mathrm{d}{S}_{r}. \tag{26.19}
\]

由 (26.18), (26.19) 得

\[
\frac{{\partial }^{2}{\mathbf{M}}_{h}}{\partial {r}^{2}} + \frac{2}{r}\frac{\partial {\mathbf{M}}_{h}}{\partial r} = \frac{1}{{4\pi }{r}^{2}}{\oiint }_{\partial {B}_{r}\left( \mathbf{M}\right) }{\Delta h}\left( {\xi ,\eta ,\zeta }\right) \mathrm{d}{S}_{r}
\]

\[
= \frac{1}{{4\pi }{r}^{2}}{\oiint }_{\partial {B}_{r}\left( \mathbf{0}\right) }{\Delta h}\left( {x + r{\alpha }_{1}, y + r{\alpha }_{2}, z + r{\alpha }_{3}}\right) \mathrm{d}{S}_{r}
\]

\[
= \Delta {\mathbf{M}}_{h}\left( {x, y, z, r}\right) .\;\left( {\text{ 由 }\left( {26.16}\right) }\right)
\]

( 3 )利用(26.18)以及积分中值定理可知

\[
\mathop{\lim }\limits_{{r \rightarrow  {0}^{ + }}}\frac{\partial }{\partial r}{\mathbf{M}}_{h}\left( {x, y, z, r}\right)  = \mathop{\lim }\limits_{{r \rightarrow  {0}^{ + }}}\frac{1}{{4\pi }{r}^{2}}{\Delta h}\left( {{\xi }^{ * },{\eta }^{ * },{\zeta }^{ * }}\right)  \cdot  \frac{4}{3}\pi {r}^{3} = 0,
\]

其中 \( \left( {{\xi }^{ * },{\eta }^{ * },{\zeta }^{ * }}\right)  \in  {B}_{r}\left( \mathbf{M}\right) \) .

#### 26.2.2 调和函数

如果在区域 \( \Omega \) 内 \( {\Delta u} = 0 \) ，则称 \( u \) 是 \( \Omega \) 上的调和函数. 调和函数有一些特殊的性质, 其中较重要的是下面的两条:

性质 1 (平均值公式) 记 \( {\mathbf{M}}_{0} = \left( {{x}_{0},{y}_{0},{z}_{0}}\right) \) ,设函数 \( u\left( {x, y, z}\right) \) 是某区域 \( \Omega \) 上的调和函数, \( {\mathbf{M}}_{0} \) 是 \( \Omega \) 中任一点. 以 \( {\mathbf{M}}_{0} \) 为心, \( R \) 为半径的球 \( {B}_{R}\left( {\mathbf{M}}_{0}\right) \) 完全落在 \( \Omega \) 的内部,则

\[
u\left( {\mathbf{M}}_{0}\right)  = \frac{1}{{4\pi }{R}^{2}}{\oiint }_{\partial {B}_{R}\left( {\mathbf{M}}_{0}\right) }u\left( {x, y, z}\right) \mathrm{d}S.
\]

证 对于 \( 0 < \rho  \leq  R \) ,由 Green 公式得

\[
{\oiint }_{\partial {B}_{\rho }\left( {\mathbf{M}}_{0}\right) }\frac{\partial u}{\partial \mathbf{n}}\left( {x, y, z}\right) \mathrm{d}S = {\iiint }_{{B}_{\rho }\left( {\mathbf{M}}_{0}\right) }{\Delta u}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z = 0,
\]

由例题 26.1.4 知结论成立.

性质 2 (极值原理) 记 \( \mathbf{M} = \left( {x, y, z}\right) \) ,设函数 \( u\left( \mathbf{M}\right) \) 是区域 \( \Omega \) 上的调和函数, 且不恒等于常数,则 \( u \) 在 \( \Omega \) 的任何内点上的值不可能达到它在 \( \Omega \) 上的上界或下界.

证 用反证法,设调和函数 \( u\left( \mathbf{M}\right) \) 不恒等于常数,且在区域 \( \Omega \) 上的上界为 \( K \) (这里假定函数 \( u\left( \mathbf{M}\right) \) 在 \( \Omega \) 上有上界,否则结论自然成立),而 \( u\left( \mathbf{M}\right) \) 在 \( \Omega \) 内某点 \( {\mathbf{M}}_{0} \) 取值为 \( K \) ,我们来找出矛盾.

因为 \( u\left( \mathbf{M}\right) \) 不恒等于常数,则至少存在一点 \( {\mathbf{M}}_{1} = \left( {{x}_{1},{y}_{1},{z}_{1}}\right)  \in  \Omega \) 使得 \( u\left( {\mathbf{M}}_{1}\right)  < K \) . 在 \( \Omega \) 中作一条连接 \( {\mathbf{M}}_{0},{\mathbf{M}}_{1} \) 的连续曲线 \( \Gamma \) (见图 26.1),设 \( \Gamma \) 的参数方程为

\[
\Gamma  : x = x\left( t\right) , y = y\left( t\right) , z = z\left( t\right) ,\;0 \leq  t \leq  T,
\]

并且

\[
x\left( 0\right)  = {x}_{0},\;y\left( 0\right)  = {y}_{0},\;z\left( 0\right)  = {z}_{0},
\]

\[
x\left( T\right)  = {x}_{1},\;y\left( T\right)  = {y}_{1},\;z\left( T\right)  = {z}_{1}.
\]

定义

\[
{t}^{ * } = \max \{ t \mid  0 \leq  t \leq  T, u\left( {x\left( t\right) , y\left( t\right) , z\left( t\right) }\right)  = K\} ,
\]

![bo_d7fsu8491nqc7381io7g_391_988_1332_511_422_0.jpg](images/xie_analysis_exercises_lower_035_bod7fsu8491nqc7381io7g39198813325114220.jpg)

图 26.1

则 \( 0 \leq  {t}^{ * } < T \) . 以 \( {\mathbf{M}}^{ * } = \left( {x\left( {t}^{ * }\right) , y\left( {t}^{ * }\right) , z\left( {t}^{ * }\right) }\right) \) 为心,充分小的 \( \delta \) 为半径,作一个完全落在 \( \Omega \) 内部的球 \( {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) \) ,并且曲线

\[
x = x\left( t\right) ,\;y = y\left( t\right) ,\;z = z\left( t\right) ,\;{t}^{ * } \leq  t \leq  T,
\]

与球面 \( \partial {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) \) 至少有一个交点 \( P \) (见图 26.1), 也就是说 \( u\left( P\right)  < K \) . 由函数 \( u\left( \mathbf{M}\right) \) 在 \( P \) 点的连续性知存在 \( P \) 点的一个邻域，使得在该邻域上 \( u\left( \mathbf{M}\right)  < K \) ,因此 \( u\left( \mathbf{M}\right) \) 在 \( \partial {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) \) 上的积分平均值

\[
\frac{1}{{4\pi }{\delta }^{2}}{\oiint }_{\partial {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) }u\left( {x, y, z}\right) \mathrm{d}S < \frac{1}{{4\pi }{\delta }^{2}}{\oiint }_{\partial {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) }K\mathrm{\;d}S = K.
\]

但由平均值公式有

\[
\frac{1}{{4\pi }{\delta }^{2}}{\oiint }_{\partial {B}_{\delta }\left( {\mathbf{M}}^{ * }\right) }u\left( {x, y, z}\right) \mathrm{d}S = u\left( {\mathbf{M}}^{ * }\right)  = K,
\]

由此得到矛盾. 同理可证 \( u \) 也不能在 \( \Omega \) 的内点取得 \( u \) 在 \( \Omega \) 上的下界.

注 1 上述两个性质对任意维数的调和函数都是成立的.

注 2 若 \( \Omega \) 是有界区域, \( u \) 在 \( \overline{\Omega } \) 上连续,在 \( \Omega \) 上调和,则 \( u \) 的最大最小值只能在 \( \Omega \) 的边界上达到.

#### 26.2.3 Poisson 积分公式

在这一节我们证明, 平面上每一个在单位圆周上的连续函数可惟一连续延拓成为单位开圆盘上的调和函数. 为此设 \( f\left( \theta \right) \) 是以 \( {2\pi } \) 为周期的连续函数,我们要在单位圆盘上证明存在惟一的连续函数

\[
u\left( {r\cos \theta , r\sin \theta }\right) ,
\]

当 \( 0 \leq  r < 1 \) 时是调和函数,且

\[
u\left( {\cos \theta ,\sin \theta }\right)  = f\left( \theta \right) .
\]

证惟一性. 设 \( u, v \) 都满足条件,则 \( w = u - v \) 当 \( 0 \leq  r < 1 \) 时是调和函数,且

\[
w\left( {\cos \theta ,\sin \theta }\right)  = 0,\;0 \leq  \theta  < {2\pi }.
\]

由极值原理 (性质 2) 知 \( w \equiv  0 \) ,于是惟一性成立.

存在性的证明要困难得多. 利用调和算子在极坐标系 \( \left( {r,\theta }\right) \) 中的表达式

\[
\Delta  \mathrel{\text{ := }} \frac{{\partial }^{2}}{\partial {x}^{2}} + \frac{{\partial }^{2}}{\partial {y}^{2}} = \frac{{\partial }^{2}}{\partial {r}^{2}} + \frac{1}{r}\frac{\partial }{\partial r} + \frac{1}{{r}^{2}}\frac{{\partial }^{2}}{\partial {\theta }^{2}},
\]

容易证明 \( \Delta \left( {{r}^{n}\cos {n\theta }}\right)  = \Delta \left( {{r}^{n}\sin {n\theta }}\right)  = 0, n = 0,1,2,\cdots \) . 由此,我们令

\[
u\left( {r\cos \theta , r\sin \theta }\right)  = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {n\theta } + {b}_{n}\sin {n\theta }}\right) {r}^{n}.
\]

令 \( r = 1 \) ,由已知条件得到

\[
f\left( \theta \right)  = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }\left( {{a}_{n}\cos {n\theta } + {b}_{n}\sin {n\theta }}\right) .
\]

由周期函数的 Fourier 级数理论知

\[
{a}_{n} = \frac{1}{\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \cos {n\varphi }\mathrm{d}\varphi ,{b}_{n} = \frac{1}{\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \sin {n\varphi }\mathrm{d}\varphi ,
\]

代入 \( u \) 的表达式中得到

\[
u\left( {r\cos \theta , r\sin \theta }\right)  = \frac{1}{\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \left\lbrack  {\frac{1}{2} + \mathop{\sum }\limits_{{n = 1}}^{\infty }{r}^{n}\cos n\left( {\theta  - \varphi }\right) }\right\rbrack  \mathrm{d}\varphi
\]

\[
= \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \operatorname{Re}\left\lbrack  \frac{1 + r{\mathrm{e}}^{\mathrm{i}\left( {\theta  - \varphi }\right) }}{1 - r{\mathrm{e}}^{\mathrm{i}\left( {\theta  - \varphi }\right) }}\right\rbrack  \mathrm{d}\varphi
\]

\[
= \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \frac{1 - {r}^{2}}{1 - {2r}\cos \left( {\theta  - \varphi }\right)  + {r}^{2}}\mathrm{\;d}\varphi .
\]

下面证明它的确提供了问题的解.

首先证明 \( u \) 在单位圆盘上是调和函数,这只是一个对含参变量常义积分求二阶偏导数的计算,所以留作练习,其中要将 \( u \) 的表达式改写为

\[
u\left( {x, y}\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \frac{1 - {x}^{2} - {y}^{2}}{1 - 2\left( {x\cos \varphi  + y\sin \varphi }\right)  + {x}^{2} + {y}^{2}}\mathrm{\;d}\varphi .
\]

最后证明对每一个 \( {\theta }_{0} \) ,

\[
\mathop{\lim }\limits_{{\left( {\theta , r}\right)  \rightarrow  \left( {{\theta }_{0},{1}^{ - }}\right) }}\frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \frac{1 - {r}^{2}}{1 - {2r}\cos \left( {\theta  - \varphi }\right)  + {r}^{2}}\mathrm{\;d}\varphi  = f\left( {\theta }_{0}\right) ,
\]

这件事我们已经在例题 18.2.4 中证明过了. 这就完成了下面命题的证明.

命题 26.2.1 若 \( f \) 是以 \( {2\pi } \) 为周期的连续函数，则

\[
u\left( {r\cos \theta , r\sin \theta }\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \frac{1 - {r}^{2}}{1 - {2r}\cos \left( {\theta  - \varphi }\right)  + {r}^{2}}\mathrm{\;d}\varphi
\]

是单位圆盘上的调和函数, 且

\[
\mathop{\lim }\limits_{{\left( {\theta , r}\right)  \rightarrow  \left( {{\theta }_{0},{1}^{ - }}\right) }}\frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( \varphi \right) \frac{1 - {r}^{2}}{1 - {2r}\cos \left( {\theta  - \varphi }\right)  + {r}^{2}}\mathrm{\;d}\varphi  = f\left( {\theta }_{0}\right) .
\]

推论 若 \( u \) 是半径为 \( R > 0 \) 的圆盘上的调和函数,则对于 \( 0 \leq  r < R \) 有

\[
u\left( {r\cos \theta , r\sin \theta }\right)
\]

\[
= \frac{1}{2\pi }{\int }_{0}^{2\pi }u\left( {R\cos \varphi , R\sin \varphi }\right) \frac{{R}^{2} - {r}^{2}}{{R}^{2} - {2Rr}\cos \left( {\theta  - \varphi }\right)  + {r}^{2}}\mathrm{\;d}\varphi . \tag{26.20}
\]

称 (26.20) 为 Poisson 积分公式.

证 若 \( R = 1 \) ,结论就是命题 26.2.1. 对于一般情形只需作一相似变换,具体细节留作练习.

#### 26.2.4 练习题

1. 证明:

(1) \( \nabla  \times  \left( {\nabla f}\right)  = \mathbf{0} \) ;

(2) \( \nabla \left( {\nabla  \cdot  \mathbf{a}}\right)  - \nabla  \times  \left( {\nabla  \times  \mathbf{a}}\right)  = \Delta \mathbf{a} \) ,其中 \( \Delta \mathbf{a} = \left( {\Delta {a}_{1},\Delta {a}_{2},\Delta {a}_{3}}\right) \) .

2. (第二 Green 恒等式) 设 \( \sum \) 为分片光滑封闭曲面,围成的区域为 \( \Omega , u, v \) 在 \( \overline{\Omega } \) 上二次连续可微. 证明:

\[
{\iiint }_{\Omega }\left( {{v\Delta u} - {u\Delta v}}\right) \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z = {\oiint }_{\sum }\left( {v\frac{\partial u}{\partial \mathbf{n}} - u\frac{\partial v}{\partial \mathbf{n}}}\right) \mathrm{d}S,
\]

其中 \( \mathbf{n} \) 为 \( \sum \) 的单位外法向量.

3. \( \sum \) 为分片光滑封闭曲面,围成的区域为 \( \Omega , u \) 在 \( \overline{\Omega } \) 上二次连续可微,在 \( \Omega \) 上调和. 证明:

\[
{\iiint }_{\Omega }{\left| \nabla u\right| }^{2}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z = {\oiint }_{\sum }u\frac{\partial u}{\partial \mathbf{n}}\mathrm{d}S,
\]

并由此证明调和函数的惟一性,即调和函数在 \( \Omega \) 内部的值由它在边界 \( \sum \) 上的值惟一确定.

4. 在调和函数性质 1 的条件下, 证明:

\[
u\left( {\mathbf{M}}_{0}\right)  = \frac{1}{\frac{4}{3}\pi {R}^{3}}{\iiint }_{{B}_{R}\left( {\mathbf{M}}_{0}\right) }u\left( {x, y, z}\right) \mathrm{d}x\mathrm{\;d}y\mathrm{\;d}z.
\]

5. 证明命题 26.2.1 的推论.

6. 证明: Poisson 积分公式 (26.20) 定义的函数是调和函数.

7. 证明: 调和函数无限次可微.

8. 若 \( f \) 和 \( g \circ  f \) 都是一连通开集上的调和函数, \( g \) 二阶连续可微, \( f \) 不是常值函数, 证明: \( g \) 是线性函数.

9. 证明: 问题

\[
{\Delta u} = f\left( {x, y, z}\right) ,\left( {x, y, z}\right)  \in  D,\frac{\partial u}{\partial \mathbf{n}} = g\left( {x, y, z}\right) ,\left( {x, y, z}\right)  \in  \partial D
\]

有解 \( u \) 的必要条件是

\[
{\iiint }_{D}f\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z = {\oiint }_{\partial D}g\mathrm{\;d}S.
\]
