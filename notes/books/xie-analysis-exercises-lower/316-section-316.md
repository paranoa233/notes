## 第一组参考题

1. 设 \( \mathbf{A},\mathbf{B} \) 为光滑向量场. 证明:

(1) \( \nabla \left( {\mathbf{A} \cdot  \mathbf{B}}\right)  = \mathbf{A} \times  \left( {\nabla  \times  \mathbf{B}}\right)  + \mathbf{B} \times  \left( {\nabla  \times  \mathbf{A}}\right)  + \left( {\mathbf{B} \cdot  \nabla }\right) \mathbf{A} + \left( {\mathbf{A} \cdot  \nabla }\right) \mathbf{B} \) ;

(2) \( \nabla  \times  \left( {\mathbf{A} \times  \mathbf{B}}\right)  = \left( {\mathbf{B} \cdot  \nabla }\right) \mathbf{A} - \left( {\mathbf{A} \cdot  \nabla }\right) \mathbf{B} + \left( {\nabla  \cdot  \mathbf{B}}\right) \mathbf{A} - \left( {\nabla  \cdot  \mathbf{A}}\right) \mathbf{B} \) .

2. 设 \( G \) 是 \( {\mathbf{R}}^{3} \) 中关于原点 \( O \) 的星形区域, \( \mathbf{F}\left( {x, y, z}\right) \) 为 \( G \) 上的光滑无源场. 定义

\[
\mathbf{A}\left( {x, y, z}\right)  = {\int }_{0}^{1}\left\lbrack  {t\mathbf{F}\left( {{tx},{ty},{tz}}\right)  \times  \mathbf{r}}\right\rbrack  \mathrm{d}t.
\]

利用上题 (2) 证明:

\[
\nabla  \times  \mathbf{A} = \mathbf{F}.
\]

3. 设 \( \mathbf{A} \) 是 \( {\mathbf{R}}^{3} \) 上的光滑向量场, \( \mathbf{B} \) 是 \( {\mathbf{R}}^{3} \) 上二次连续可微的向量场,满足

\[
\nabla  \times  \mathbf{B} = \frac{1}{r}\left( {\nabla r \times  \mathbf{A}}\right) ,
\]

其中 \( r = \sqrt{{x}^{2} + {y}^{2} + {z}^{2}} \) ,证明:

\[
{\oint }_{L}\mathbf{A} \cdot  \tau \mathrm{d}s = 0
\]

其中 \( L \) 是以原点为中心的球面上的封闭光滑简单定向曲线, \( \tau \) 是 \( L \) 上与其方向一致的单位切向量.

4. 设长度为 \( l \) 的平面简单闭曲线 \( C \) 由方程 \( F\left( {x, y}\right)  = 0 \) 确定. \( F\left( {x, y}\right) \) 二阶连续可微,且 \( \nabla F\left( {x, y}\right)  \neq  \mathbf{0} \) ,设 \( D = \{ \left( {x, y}\right)  \mid  F\left( {x, y}\right)  > 0\} \) 为曲线 \( C \) 围成的区域,计算二重积分

\[
{\iint }_{D}\nabla  \cdot  \left( \frac{\nabla F}{\left| \nabla F\right| }\right) \mathrm{d}x\mathrm{\;d}y
\]

5. 设 \( u\left( {x, y, z}\right) \) 是连续函数,它在 \( \mathbf{M}\left( {{x}_{0},{y}_{0},{z}_{0}}\right) \) 处有连续二阶偏导数,记

\[
F\left( R\right)  = \frac{1}{{4\pi }{R}^{2}}{\oiint }_{\partial {B}_{R}\left( \mathbf{M}\right) }u\left( {x, y, z}\right) \mathrm{d}S,
\]

其中 \( \partial {B}_{R}\left( \mathbf{M}\right) \) 是以 \( \mathbf{M} \) 为心, \( R \) 为半径的球面. 证明:

\[
\mathop{\lim }\limits_{{R \rightarrow  0}}F\left( R\right)  = u\left( \mathbf{M}\right) .
\]

若 \( {\Delta u}\left( \mathbf{M}\right) \) 不等于零,求无穷小量 \( F\left( R\right)  - u\left( \mathbf{M}\right) \) 的主要部分.

6. 设 \( u, v \) 在 \( \overline{\Omega } \) 上二阶连续可微,且在 \( \Omega \) 的边界上 \( u = v \) . 如果 \( u \) 是调和函数,则

\[
{\iiint }_{\Omega }{\left| \nabla u\right| }^{2}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z \leq  {\iiint }_{\Omega }{\left| \nabla v\right| }^{2}\mathrm{\;d}x\mathrm{\;d}y\mathrm{\;d}z.
\]

7. 设 \( u\left( {x, y}\right) \) 在 \( {x}^{2} + {y}^{2} < 1 \) 二阶连续可微,且 \( {\Delta u} = {\mathrm{e}}^{-\left( {{x}^{2} + {y}^{2}}\right) } \) ,证明:

\[
{\iint }_{{x}^{2} + {y}^{2} < 1}\left( {x\frac{\partial u}{\partial x} + y\frac{\partial u}{\partial y}}\right) \mathrm{d}x\mathrm{\;d}y = \frac{\pi }{2\mathrm{e}}.
\]
