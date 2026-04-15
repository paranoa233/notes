## 第二组参考题

1. 证明: 对任意 \( \varepsilon  > 0 \) ,

\[
{ab} \leq  \frac{\varepsilon {a}^{p}}{p} + \frac{{\varepsilon }^{-q/p}{b}^{q}}{q} \leq  \varepsilon {a}^{p} + {\varepsilon }^{-q/p}{b}^{q},
\]

其中 \( a \geq  0, b \geq  0, p, q > 0,\frac{1}{p} + \frac{1}{q} = 1 \) .

2. 利用上题以及例题 22.5.9 的结论证明内插不等式:

\[
\parallel u{\parallel }_{q} \leq  \varepsilon \parallel u{\parallel }_{r} + {\varepsilon }^{-\mu }\parallel u{\parallel }_{p},
\]

其中 \( \mu  = \left( {\frac{1}{p} - \frac{1}{q}}\right) /\left( {\frac{1}{q} - \frac{1}{r}}\right) ,0 < p < q < r,\varepsilon  > 0 \) .

3. 设 \( \Omega \) 是 \( {\mathbf{R}}^{2} \) 中有界闭区域, \( u\left( {x, y}\right) \) 在 \( \Omega \) 上连续且恒取正值,定义

\[
{\Phi }_{p}\left( u\right)  = \left( {\frac{1}{\left| \Omega \right| }{\iint }_{\Omega }{u}^{p}\mathrm{\;d}x\mathrm{\;d}y{)}^{\frac{1}{p}},}\right.
\]

其中 \( \left| \Omega \right| \) 是 \( \Omega \) 的面积,证明:

(1) \( \mathop{\lim }\limits_{{p \rightarrow   + \infty }}{\Phi }_{p}\left( u\right)  = \mathop{\max }\limits_{{\left( {x, y}\right)  \in  \Omega }}\{ u\left( {x, y}\right) \} \)

(2) \( \mathop{\lim }\limits_{{p \rightarrow   - \infty }}{\Phi }_{p}\left( u\right)  = \mathop{\min }\limits_{{\left( {x, y}\right)  \in  \Omega }}\{ u\left( {x, y}\right) \} \)

(3) \( \mathop{\lim }\limits_{{p \rightarrow  0}}{\Phi }_{p}\left( u\right)  = \exp \left\{  {\frac{1}{\left| \Omega \right| }{\iint }_{\Omega }\ln u\mathrm{\;d}x\mathrm{\;d}y}\right\} \) .

4. 设 \( {\mathbf{P}}_{0} \) 为半径等于 \( R \) 的球内的一定点,从点 \( {\mathbf{P}}_{0} \) 向球面上任意一点 \( \mathbf{Q} \) 处的切平面作垂线,垂足为点 \( \mathbf{P} \) . 当点 \( \mathbf{Q} \) 在球面上变动时,点 \( \mathbf{P} \) 的轨迹形成一封闭曲面.

(1)求此曲面所围成的立体的体积;

(2)问当点 \( {\mathbf{P}}_{0} \) 沿什么方向变化时,上述体积的变化率最大?

5. 证明不等式

\[
\frac{\sqrt{\pi }}{2}{\left( 1 - {\mathrm{e}}^{-{a}^{2}}\right) }^{\frac{1}{2}} < {\int }_{0}^{a}{\mathrm{e}}^{-{x}^{2}}\mathrm{\;d}x < \frac{\sqrt{\pi }}{2}{\left( 1 - {\mathrm{e}}^{-\frac{4{a}^{2}}{\pi }}\right) }^{\frac{1}{2}}.
\]

6. 设连续函数 \( f\left( {x, y}\right) \) 的等位线是简单封闭曲线, \( S\left( {{v}_{1},{v}_{2}}\right) \) 是由曲线 \( f\left( {x, y}\right)  = \; {v}_{1}, f\left( {x, y}\right)  = {v}_{2} \) 所围成的域. 证明 Catalan 公式

\[
{\iint }_{S\left( {{v}_{1},{v}_{2}}\right) }f\left( {x, y}\right) \mathrm{d}x\mathrm{\;d}y = {\int }_{{v}_{1}}^{{v}_{2}}v{F}^{\prime }\left( v\right) \mathrm{d}v
\]

其中 \( F\left( v\right) \) 为由曲线 \( f\left( {x, y}\right)  = {v}_{1}, f\left( {x, y}\right)  = v \) 所包围的面积,还假设 \( F\left( v\right) \) 可微且导函数 \( {F}^{\prime }\left( v\right) \) 可积.

注 题 6 即 [25] 的习题 3983, 它代表了重积分计算中的 Catalan 方法. 这种方法在一定的条件下可以将多重积分 (直接) 转化为单重积分. 较详细的介绍见 [55] 第三册 8.1.6 小节中的命题 8.1、8.2 与例题, 以及它们在 \( \text{ § }{8.6} \) (三重积分计算) 和 \( \text{ § }{8.10} \) ( \( n \) 重积分计算) 中的一系列应用. Catalan 方法也可用于求解本章中的若干积分计算题,例如 22.3.5 小节的练习题 7、8 和第一组参考题 5 等.
