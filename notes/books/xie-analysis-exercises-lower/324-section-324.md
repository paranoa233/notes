## 第二十章 隐函数存在定理与隐函数求导 参考题提示

## 第一组参考题 (205 页)

1. 令 \( F\left( {x, t}\right)  = f\left( {x,{\int }_{0}^{t}\sin x\mathrm{\;d}x}\right) ,{F}_{t} = {f}_{y}\sin t,{F}_{t}\left( {0,\frac{\pi }{2}}\right)  = {f}_{y}\left( {0,1}\right) \) .

2. 利用命题 20.4.1, 或用上册 145 页的反函数存在定理及 162 页的求导法则.

3. 用隐函数存在定理.

4. 当 \( x > 0 \) 时, \( F\left( {x,0}\right)  > 0, F\left( {x, - \infty }\right)  =  - \infty \) ,且当 \( y < 0 \) 时 \( {F}_{y}\left( {x, y}\right)  = \left( {3 - y}\right) {y}^{2}{\mathrm{e}}^{-y} > 0 \) , 于是存在惟一的 \( y = y\left( x\right) \) 使得 \( F\left( {x, y\left( x\right) }\right)  = 0 \) .

5. 用介值定理惟一确定函数 \( y = y\left( x\right) \) .

6. (1) 当 \( \frac{\partial f}{\partial x}\left( {{x}_{0},{y}_{0}}\right)  \neq  0 \) 时,在点 \( \left( {{x}_{0},{y}_{0}}\right) \) 附近对 \( u = f\left( {x, y}\right) \) 用隐函数存在定理解出 \( x \) , 再用题设条件证明 \( g\left( {x\left( {u, y}\right) , y}\right) \) 与 \( y \) 无关; 从而找出 \( F\left( {u, v}\right) \) . 其他情况类似; (2) 对 \( F \) 求 \( x, y \) 的偏导数,并用齐次线性方程组有非零解的条件.

7. 把问题归结为证明满足 \( E \) 中前两个关系式的局部连续隐函数 \( t = t\left( {x, y}\right) \) 存在.

---

① 这来自矩阵论中的 Perron (佩龙) 定理,可简证如下. 在 \( {\mathbf{R}}^{n} \) 中定义点集

\[
S = \left\{  {\left( {{x}_{1},{x}_{2},\cdots ,{x}_{n}}\right)  \mid  {x}_{i} \geq  0, i = 1,2,\cdots , n,\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = 1}\right\}  ,
\]

则 \( S \) 为凸紧集. 若存在 \( {\mathbf{x}}_{0} \in  S \) 使得 \( \mathbf{A}{\mathbf{x}}_{0} = \mathbf{0} \) ,则 \( \mathbf{A} \) 有特征值 \( 0,{\mathbf{x}}_{0} \) 为相应的特征向量. 否则,在 \( S \) 上定义映射 \( \mathbf{f}\left( \mathbf{x}\right)  = {\left( \lambda \left( \mathbf{x}\right) \right) }^{-1}\mathbf{A}\mathbf{x} \) ,其中 \( \lambda \left( \mathbf{x}\right) \) 是 \( \mathbf{A}\mathbf{x} \) 的 \( n \) 个分量之和,则 \( \mathbf{f}\left( S\right)  \subset  S \) . 用 (329 页上的) Brouwer 不动点定理即可得到所要的特征值和特征向量.

---

8. 用反证法、聚点定理与隐函数存在定理.

9. 检验.

10. 用反证法. 由隐函数存在定理及题设证明 \( f\left( {{\mathbf{R}}^{2} \smallsetminus  \left\{  {{\mathbf{x}}_{1},{\mathbf{x}}_{2},\cdots ,{\mathbf{x}}_{r}}\right\}  }\right) \) 与 \( {\mathbf{R}}^{2} \smallsetminus  f\left( {\mathbf{R}}^{2}\right) \) 均是非空开集. 再用 \( f\left( \left\{  {{\mathbf{x}}_{1},{\mathbf{x}}_{2},\cdots ,{\mathbf{x}}_{r}}\right\}  \right) \) 的有限性找到联结 \( f\left( {{\mathbf{R}}^{2} \smallsetminus  \left\{  {{\mathbf{x}}_{1},{\mathbf{x}}_{2},\cdots ,{\mathbf{x}}_{r}}\right\}  }\right) \) 中点与 \( {\mathbf{R}}^{2} \smallsetminus  f\left( {\mathbf{R}}^{2}\right) \) 中点的线段,由连通性推出矛盾.

11. 利用映射的无穷小增量公式与局部逆映射存在定理.

## 第二组参考题 (207 页)

1. 可微性的证明根据定义检验.

2. 由例题 19.4.1 及 Schwarz 不等式.

3. 依照命题 20.2.3 的注.

4. 自己动手做一遍就有体会.

5. 利用局部逆映射定理把 \( \mathbf{h} \) 找出来.

6. 几何上的解释可局部地把 \( \mathbf{f} \) 看成线性映射.
