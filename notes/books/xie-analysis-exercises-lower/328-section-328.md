## 第二十四章 曲线积分 参考题提示

## 第一组参考题 (333 页)

1. 利用两型曲线积分之间的关系.

2. 可以直接计算,也可以对 \( R \) 求导后计算,答案为:

(1) \( {2\pi R}\ln R \) 当 \( \left| a\right|  < R,{2\pi R}\ln \left| a\right| \) 当 \( \left| a\right|  > R \) .

(2) \( {2\pi R}\ln R \) 当 \( {a}^{2} + {b}^{2} < {R}^{2},{2\pi R}\ln \sqrt{{a}^{2} + {b}^{2}} \) 当 \( {a}^{2} + {b}^{2} > {R}^{2} \) .

3. \( \mathop{\lim }\limits_{{{x}^{2} + {y}^{2} \rightarrow   + \infty }}\left\lbrack  {\ln \sqrt{{x}^{2} + {y}^{2}} - \ln \sqrt{{\left( x - \xi \right) }^{2} + {\left( y - \eta \right) }^{2}}}\right\rbrack   = 0 \) 对 \( \left( {\xi ,\eta }\right)  \in  L \) 一致地成立.

4. 等式两边乘以分母后求导或者积分.

5. 利用 Green 公式得 \( {\iint }_{G}f\mathrm{\;d}x\mathrm{\;d}y =  - {\iint }_{G}x{f}_{x}\mathrm{\;d}x\mathrm{\;d}y =  - {\iint }_{G}y{f}_{y}\mathrm{\;d}x\mathrm{\;d}y \) ,于是

\[
\left| {{\iint }_{G}f\mathrm{\;d}x\mathrm{\;d}y}\right|  = \frac{1}{2}\left| {{\iint }_{G}\left( {x{f}_{x} + y{f}_{y}}\right) \mathrm{d}x\mathrm{\;d}y}\right|  \leq  \frac{1}{2}{\iint }_{G}{\left( {f}_{x} + {f}_{y}\right) }^{1/2}\sqrt{{x}^{2} + {y}^{2}}\mathrm{\;d}x\mathrm{\;d}y.
\]

6. 利用 Green 公式与中值定理.

## 第二组参考题 (334 页)

1. 先考虑对于任一点 \( \left( {x, y}\right)  \in  D \) ,存在以 \( \left( {x, y}\right) \) 为中心的开矩形,使对于任一条位于开矩形及其边界上的逐段光滑定向闭曲线 \( \Gamma \) 有性质

\[
\frac{\mathbf{F}\left( {{x}_{1},{y}_{1}}\right) }{\left| \mathbf{F}\left( {x}_{1},{y}_{1}\right) \right| } \neq   - \frac{\mathbf{F}\left( {{x}_{2},{y}_{2}}\right) }{\left| \mathbf{F}\left( {x}_{2},{y}_{2}\right) \right| },\;\forall \left( {{x}_{1},{y}_{1}}\right) ,\left( {{x}_{2},{y}_{2}}\right)  \in  \Gamma .
\]

从而有 \( \gamma \left( {\mathbf{F},\Gamma }\right)  = 0 \) ,然后用有限覆盖定理.

2. 证明 \( \mathop{\min }\limits_{{\mathbf{x} \in  D}}\{ \left| {\nabla f\left( \mathbf{x}\right) }\right| \}  \leq  \frac{1}{2r}\left( {\mathop{\max }\limits_{{\mathbf{x} \in  D}}\{ f\left( \mathbf{x}\right) \}  - \mathop{\min }\limits_{{\mathbf{x} \in  D}}\{ f\left( \mathbf{x}\right) \} }\right)  \leq  \mathop{\max }\limits_{{\mathbf{x} \in  D}}\{ \left| {\nabla f\left( \mathbf{x}\right) }\right| \} \) ,再用多元函数介值定理. 可借助梯度曲线讨论.

3. 设 \( f\left( \mathbf{v}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\mathrm{e}}^{\left( {{a}_{i},{b}_{i}}\right)  \cdot  \mathbf{v}} \) ,当 \( \left| u\right|  + \left| v\right| \) 充分大时有 \( \left( {u, v}\right)  \cdot  \nabla f\left( {u, v}\right)  > 0 \) ,用旋转度证明 \( \nabla f\left( \mathbf{v}\right) \) 有零点.

4. 不妨取 \( \left( {x, y}\right) \) 的极坐标为 \( \left( {\rho ,0}\right) \) ,并计算出 \( l\left( {x, y}\right)  = L\left( \rho \right) \) . 设小圆外弧对应的圆心角为 \( {2\varphi } \) ,则 \( L\left( \rho \right)  = 0,0 \leq  \rho  \leq  r - \delta ;L\left( \rho \right)  = {2\delta \varphi }, r - \delta  \leq  \rho  \leq  r \) . 再利用余弦定理表达出 \( \varphi \) , 并在积分号下取 \( \delta  \rightarrow  0 \) ，得极限值为 \( {4\pi r} \) .

5. (1) 利用 Green 公式; (2) 检验; (3) 对 \( {g}_{1}^{2}\left( \mathbf{x}\right)  + {g}_{2}^{2}\left( \mathbf{x}\right)  = 1 \) 两边求微分,并用不同的方法计算 \( {\iint }_{B}\frac{\partial \left( {{g}_{1},{g}_{2}}\right) }{\partial \left( {{x}_{1},{x}_{2}}\right) }\mathrm{d}{x}_{1}\mathrm{\;d}{x}_{2} \) ; (4) 设曲面定义在圆盘上,并保持边界圆周不动. 则这样的曲面不能退缩到边界上, 除非撕破曲面.

6. 利用上题.
