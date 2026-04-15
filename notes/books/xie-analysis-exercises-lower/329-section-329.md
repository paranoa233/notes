## 第二十五章 曲面积分 参考题提示

## 参考题 (369 页)

1. 坐标旋转,使 \( x + y + z = 0 \) 变为坐标平面.

2. 所求积分等于 \( {\oiint }_{{u}^{2} + {v}^{2} + {w}^{2} = 1}{\mathrm{e}}^{u - v}\mathrm{\;d}S \) ,然后作坐标旋转.

3. \( f \) 是 -3 次齐次函数,即 \( {3f} + x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} + z\frac{\partial f}{\partial z} = 0 \) .

4. 记以 \( \left( {{x}_{0},{y}_{0},{z}_{0}}\right) \) 为心,以 \( \varepsilon \) 为半径的球为 \( {B}_{\varepsilon } \) ,在 \( \Omega  \smallsetminus  {B}_{\varepsilon } \) 上用 Gauss 公式,然后证 \( \mathop{\lim }\limits_{{\varepsilon  \rightarrow  0}}{\oiint }_{\partial {B}_{\varepsilon }}\cos \left( {\mathbf{n},\mathbf{r}}\right) \mathrm{d}S = 0. \)

5. 用 Stokes 公式.

6. 记 \( A = \left( {\xi  - x}\right) /{r}^{3}, B = \left( {\eta  - y}\right) /{r}^{3}, C = \left( {\zeta  - z}\right) /{r}^{3} \) ,则 \( {A}_{\xi } + {B}_{\eta } + {C}_{\zeta } = 0,{A}_{x} + {B}_{y} + {C}_{z} = 0 \) . 于是 \( {P}_{y} = {\oint }_{\Gamma }{C}_{y}\mathrm{\;d}\eta  - {B}_{y}\mathrm{\;d}\zeta  = {\oint }_{\Gamma }\left( {{C}_{y}\mathrm{\;d}\eta  + {C}_{z}\mathrm{\;d}\zeta }\right)  + {A}_{x}\mathrm{\;d}\zeta  = {\oint }_{\Gamma } - \left( {{C}_{\eta }\mathrm{d}\eta  + {C}_{\zeta }\mathrm{d}\zeta }\right)  + {A}_{x}\mathrm{\;d}\zeta  = \; {\oint }_{\Gamma }{C}_{\xi }\mathrm{d}\xi  + {A}_{x}\mathrm{\;d}\zeta  = {\oint }_{\Gamma } - {C}_{x}\mathrm{\;d}\xi  + {A}_{x}\mathrm{\;d}\zeta  = {Q}_{x}. \)

7. 设 \( S \) 是以 \( \Gamma \) 为边界的光滑曲面, \( \left( {x, y, z}\right)  \notin  S \) ,由 Stokes 公式

\[
P = {\iint }_{S}\left( {-{B}_{\eta } - {C}_{\zeta }}\right) \mathrm{d}\eta \mathrm{d}\zeta  + {B}_{\xi }\mathrm{d}\zeta \mathrm{d}\xi  + {C}_{\xi }\mathrm{d}\xi \mathrm{d}\eta
\]

\[
= {\iint }_{S}{A}_{\xi }\mathrm{d}\eta \mathrm{d}\zeta  + {B}_{\xi }\mathrm{d}\zeta \mathrm{d}\xi  + {C}_{\xi }\mathrm{d}\xi \mathrm{d}\eta
\]

\[
=  - \frac{\partial }{\partial x}{\iint }_{S}A\mathrm{\;d}\eta \mathrm{d}\zeta  + B\mathrm{\;d}\zeta \mathrm{d}\xi  + C\mathrm{\;d}\xi \mathrm{d}\eta
\]

8. 设液体表面为 \( {xOy} \) 平面， \( z \) 轴方向向下，液体比重为 \( \rho \) ，物体表面面积元 \( \mathrm{d}S \) 的深度为 \( z \) ， 则这一元素所受液体压力为 \( {\rho z}\mathrm{\;d}S \) ,它在 \( z \) 轴方向的分力为 \( - {\rho z}\cos \left( {\mathbf{n}, z}\right) \mathrm{d}S \) ,于是在 \( z \) 轴方向受力 \( = {\oiint }_{S} - {\rho z}\cos \left( {\mathbf{n}, z}\right) \mathrm{d}S =  - \rho {\iiint }_{V}\mathrm{\;d}V =  - {\rho V} \) .
