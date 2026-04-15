## 第二组参考题

1. 给出旋转度性质 2 的一个不用曲线积分的证明.

2. 证明如下形式的高维中值定理: 设 \( f\left( \mathbf{x}\right) \) 为定义在以 \( r \) 为半径的球

\[
D = \left\{  {\mathbf{x} = \left( {{x}_{1},{x}_{2},\cdots ,{x}_{n}}\right)  \mid  {x}_{1}^{2} + {x}_{2}^{2} + \cdots  + {x}_{n}^{2} \leq  {r}^{2}}\right\}
\]

上的连续可微函数,则存在点 \( {\mathbf{p}}_{0} = \left( {{p}_{1}^{0},{p}_{2}^{0},\cdots ,{p}_{n}^{0}}\right)  \in  \operatorname{int}D \) ,使

\[
\mathop{\max }\limits_{{\mathbf{x} \in  D}}\{ f\left( \mathbf{x}\right) \}  - \mathop{\min }\limits_{{\mathbf{x} \in  D}}\{ f\left( \mathbf{x}\right) \}  = \left| {\nabla f\left( {\mathbf{p}}_{0}\right) }\right|  \cdot  {2r}.
\]

3. 设 \( \left( {{a}_{1},{b}_{1}}\right) ,\left( {{a}_{2},{b}_{2}}\right) ,\cdots ,\left( {{a}_{n},{b}_{n}}\right) \) 是 \( n \) 边形的 \( n \) 个顶点,而且原点在其内部,证明: 存在正实数 \( x \) 和 \( y \) ,使得

\[
\left( {{a}_{1},{b}_{1}}\right) {x}^{{a}_{1}}{y}^{{b}_{1}} + \left( {{a}_{2},{b}_{2}}\right) {x}^{{a}_{2}}{y}^{{b}_{2}} + \cdots  + \left( {{a}_{n},{b}_{n}}\right) {x}^{{a}_{n}}{y}^{{b}_{n}} = \left( {0,0}\right) .
\]

4. 设 \( D \) 是半径为 \( r \) 的一个圆所围成的平面区域,对 \( D \) 内的点 \( \left( {x, y}\right) \) ,用 \( l\left( {x, y}\right) \) 表示以 \( \left( {x, y}\right) \) 为圆心, \( \delta \) 为半径的圆在 \( D \) 外边的那段弧的长度. 试求

\[
\mathop{\lim }\limits_{{\delta  \rightarrow  0}}\frac{1}{{\delta }^{2}}{\iint }_{D}l\left( {x, y}\right) \mathrm{d}x\mathrm{\;d}y
\]

5. 设 \( B \) 是 \( {\mathbf{R}}^{2} \) 中的单位圆盘, \( C \) 是单位圆周. \( g : B \rightarrow  {\mathbf{R}}^{2} \smallsetminus  \{ 0\} \) 是二阶连续可微映射.

(1)用 Green 公式把 \( {\iint }_{B}\frac{\partial \left( {{g}_{1},{g}_{2}}\right) }{\partial \left( {{x}_{1},{x}_{2}}\right) }\mathrm{d}{x}_{1}\mathrm{\;d}{x}_{2} \) 表示成 \( C \) 上的第二型曲线积分;

(2)如果 \( \mathbf{g} \) 在 \( C \) 上的限制是恒等映射，即 \( \mathbf{g}\left( \mathbf{x}\right)  = \mathbf{x},\forall \mathbf{x} \in  C \) ,证明:

\[
{\oint }_{C}{x}_{1}\mathrm{\;d}{x}_{2} = {\oint }_{C}{g}_{1}\mathrm{\;d}{g}_{2} = {\oint }_{C}{g}_{1}\frac{\partial {g}_{2}}{\partial {x}_{1}}\mathrm{\;d}{x}_{1} + {g}_{1}\frac{\partial {g}_{2}}{\partial {x}_{2}}\mathrm{\;d}{x}_{2};
\]

(3) 证明: 不存在满足 \( \mathbf{g}\left( \mathbf{x}\right)  = \mathbf{x},\mathbf{x} \in  C \) 及 \( \mathbf{g}\left( B\right)  \subset  C \) 的二阶连续可微映射 \( \mathbf{g} \) ;

(4) 对上述命题给出一个几何上的解释.

6. (1) 设 \( B, C \) 与题 5 相同， \( \mathbf{f} : B \rightarrow  B \) 是二阶连续可微映射， \( \mathbf{f}\left( \mathbf{x}\right)  \neq  \mathbf{x},\forall \mathbf{x} \in  B \) ， 从几何上可见以 \( \mathbf{f}\left( \mathbf{x}\right) \) 为起点和 \( \mathbf{x} \) 为终点的有向线段与 \( B \) 的边界 \( C \) 相交， 则交点可表示为

\[
\mathbf{g}\left( \mathbf{x}\right)  = \mathbf{f}\left( \mathbf{x}\right)  + t\left( \mathbf{x}\right) \left( {\mathbf{x} - \mathbf{f}\left( \mathbf{x}\right) }\right) ,
\]

其中 \( t\left( \mathbf{x}\right) \) 是与 \( \mathbf{x} \) 有关的参数,证明: \( t\left( \mathbf{x}\right) \) 满足二次方程

\[
{t}^{2}\left( \mathbf{x}\right) {\left| \mathbf{x} - \mathbf{f}\left( \mathbf{x}\right) \right| }^{2} + {2t}\left( \mathbf{x}\right) \mathbf{f}\left( \mathbf{x}\right)  \cdot  \left( {\mathbf{x} - \mathbf{f}\left( \mathbf{x}\right) }\right)  + {\left| \mathbf{f}\left( \mathbf{x}\right) \right| }^{2} - 1 = 0;
\]

(2) 证明 (1) 中的 \( \mathbf{g} \) 满足 \( \mathbf{g}\left( \mathbf{x}\right)  = \mathbf{x},\mathbf{x} \in  C \) 及 \( \mathbf{g}\left( B\right)  \subset  C \) ;

(3) 结合上题证明满足 (1) 的 \( \mathbf{f} \) 是不存在的,即若 \( \mathbf{f} : B \rightarrow  B \) 是二阶连续可微映射,则 \( \exists \mathbf{\xi } \in  B \) ,使 \( \mathbf{f}\left( \mathbf{\xi }\right)  = \mathbf{\xi } \) . 我们得到了 Brouwer 不动点定理的另一个证明. 你能否举几个运用 Brouwer 不动点定理的实际例子.
