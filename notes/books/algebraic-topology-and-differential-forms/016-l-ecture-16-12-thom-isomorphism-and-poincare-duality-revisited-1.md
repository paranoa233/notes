#### 16. 再论 Poincaré 对偶

§12 Thom Isomorphism and Poincaré Duality Revisited (1)

## 16. 再论 Poincaré 对偶

这节从 tic-tac-toe 的观点研究 Thom 同构与 Poincaré 对偶, 从以下两个方面推广第 5,6 节的结果:

(a) 不需要假定流形 \( M \) 具有有限好覆盖;

(b) 不需要假定向量丛 \( E \) 可定向.

这次课先讲一个 tic-tac-toe 引理, 它是一个在第二页退化的谱序列的例子; 在此基础上把 Poincaré 对偶推广为

\[
{H}_{c}^{ * }\left( M\right)  \simeq  {H}_{n -  * }\left( {\mathcal{U},{\mathcal{H}}_{c}^{n}}\right) ,
\]

其中 \( {\mathcal{H}}_{c}^{n} \) 是共变函子 \( {\mathcal{H}}_{c}^{n}\left( U\right)  = {H}_{c}^{n}\left( U\right) \) . 在这个同构中不需要假定流形可定向与具有有限好覆盖，但对开覆盖需加一个比有限好覆盖弱的局部有限条件. 下次课讲 Thom 同构, Thom 类与欧拉类的性质, 以及欧拉类与截面的零点集.

- 一个 tic-tac-toe 引理

- Poincaré 对偶

一个 tic-tac-toe 引理设 \( \left\{  {{K}^{*, * }, d,\delta }\right\} \) 是双复形,它形成单复形 \( \left\{  {{K}^{ * }, D}\right\} \) ,其中

\[
{K}^{n} = { \oplus  }_{p + q = n}{K}^{p, q},\;D = {D}^{\prime } + {D}^{\prime \prime },
\]

其中

\[
{D}^{\prime } = \delta ,\;{D}^{\prime \prime } = {\left( -1\right) }^{p}d : {K}^{p, q} \rightarrow  {K}^{p, q + 1}.
\]

它的第 \( n \) 个上同调记为 \( {H}_{D}^{n}\left( {K}^{ * }\right) \) ,简记为 \( {H}_{D}^{n} \) .

另一方面,对固定的 \( p \) , \( \{ {K}^{p, * }, d\} \) 是单复形,它的第 \( q \) 个上同调为 \( {H}_{d}^{q}\left( {K}^{p, * }\right) \) ,简记为 \( {H}_{d}^{p, q} \cdot  {\left\lbrack  \phi \right\rbrack  }_{d} \in  {H}_{d}^{p, q} \) 表示 \( \phi  \in  {K}^{p, q} \) 且 \( {d\phi } = 0 \) .

再对固定的 \( q \) ,定义 \( \delta  : {H}_{d}^{p, q} \rightarrow  {H}_{d}^{p + 1, q} \) 为

\[
\delta {\left\lbrack  \phi \right\rbrack  }_{d} = {\left\lbrack  \delta \phi \right\rbrack  }_{d}.
\]

需检查 \( \delta \) 是定义好的:

(a) \( {\delta \phi } \) 是 \( d \) -闭的: \( {d\delta \phi } = {\delta d\phi } = 0 \) ;

(b) 与代表元 \( \phi \) 的选取无关: \( \delta \left( {\phi  + d{\phi }_{1}}\right)  = {\delta \phi } + d\left( {\delta {\phi }_{1}}\right) \) .

显然对这样定义的 \( \delta ,{\delta }^{2} = 0 \) . 所以对固定的 \( q,\left\{  {{H}_{d}^{*, q},\delta }\right\} \) 是复形. 于是可定义上同调 \( {H}_{\delta }^{p}{H}_{d}^{q}\left( {K}^{*, * }\right) \) ,简记为 \( {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) . 这就是说,若 \( {\left\lbrack  \phi \right\rbrack  }_{d} \in  {H}_{d}^{q}\left( {K}^{p, * }\right) \) , \( \delta {\left\lbrack  \phi \right\rbrack  }_{d} = {\left\lbrack  \delta \phi \right\rbrack  }_{d} = 0 \) ,则定义

\[
{\left\lbrack  {\left\lbrack  \phi \right\rbrack  }_{d}\right\rbrack  }_{\delta } \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q}.
\]

在不致于引起混淆时把 \( {\left\lbrack  {\left\lbrack  \phi \right\rbrack  }_{d}\right\rbrack  }_{\delta } \) 简记为 \( \left\lbrack  \phi \right\rbrack \) .

若 \( \left\lbrack  \phi \right\rbrack   \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) ,则由定义知 \( \phi  \in  {K}^{p, q} \) 满足

\[
{D}^{\prime \prime }\phi  = 0\text{ 且 }{\left\lbrack  \delta \phi \right\rbrack  }_{d} = 0.
\]

后者表示存在 \( {\phi }_{1} \in  {K}^{p + 1, q - 1} \) 使得

\[
{\delta \phi } =  - {D}^{\prime \prime }{\phi }_{1}.
\]

所以 \( \left\lbrack  \phi \right\rbrack   \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) 当且仅当 \( \phi  \in  {K}^{p, q} \) 满足: 存在 \( {\phi }_{1} \in  {K}^{p + 1, q - 1} \) 使得(34)若 \( \left\lbrack  \phi \right\rbrack   = 0 \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) ,则 \( \phi  \in  {K}^{p, q} \) 满足

\[
{D}^{\prime \prime }\phi  = 0\text{ 且 }{\left\lbrack  \phi \right\rbrack  }_{d} = \delta {\left\lbrack  {\phi }_{1}\right\rbrack  }_{d} = {\left\lbrack  \delta {\phi }_{1}\right\rbrack  }_{d},
\]

![bo_d7e85t491nqc73eqefm0_357_763_1000_735_513_0.jpg](images/fu_algebraic_topology_and_differential_forms_058_bod7e85t491nqc73eqefm035776310007355130.jpg)

即

\[
\phi  = \delta {\phi }_{1} + {D}^{\prime \prime }{\phi }_{2},\;{D}^{\prime \prime }{\phi }_{1} = 0.
\]

所以 \( \left\lbrack  \phi \right\rbrack   = 0 \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) 当且仅当 \( \phi  \in  {K}^{p, q} \) 满足: 存在 \( {\phi }_{1} \in  {K}^{p - 1, q},{\phi }_{2} \in \; {K}^{p, q - 1} \) 使得(35)

![bo_d7e85t491nqc73eqefm0_358_739_1014_794_513_0.jpg](images/fu_algebraic_topology_and_differential_forms_059_bod7e85t491nqc73eqefm035873910147945130.jpg)

命题 12.1. 给定双复形 \( \left\{  {{K}^{*, * }, d,\delta }\right\} \) ,若 \( {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) 仅有一行可能不为零,则

\[
{ \oplus  }_{p + q = n}{H}_{\delta }^{p, q}{H}_{d}^{*, q} \simeq  {H}_{D}^{n}.
\]

这是一个退化谱序列的例子, 它在第二页退化.

证. 设此行是第 \( q \) 行. 证明分四步.

第一步. 定义 \( h : {H}_{\delta }{H}_{d} \rightarrow  {H}_{D} \) . 因为 \( {H}_{\delta }{H}_{d} \) 只有第 \( q \) 行不为零,所以只要对 \( {H}_{\delta }^{p, q}{H}_{d}^{*, q} \) 中的元给出定义就可以了.

设 \( \left\lbrack  \phi \right\rbrack   \in  {H}_{\delta }^{p, q}{H}_{d}^{*, q}, p + q = n \) . 则由 (34) 可得: 存在 \( {\phi }_{1} \in  {K}^{p + 1, q - 1} \) 使得(36)

![bo_d7e85t491nqc73eqefm0_359_620_1174_1008_493_0.jpg](images/fu_algebraic_topology_and_differential_forms_060_bod7e85t491nqc73eqefm0359620117410084930.jpg)

因为 \( {d\delta }{\phi }_{1} = {\delta d}{\phi }_{1} =  \pm  {\delta }^{2}\phi  = 0 \) ,所以

\[
{\left\lbrack  \delta {\phi }_{1}\right\rbrack  }_{d} \in  {H}_{d}^{q - 1}\left( {K}^{p + 2, * }\right) .
\]

又因为 \( \delta \left( {\delta {\phi }_{1}}\right)  = 0 \) ,所以

\[
{\left\lbrack  {\left\lbrack  \delta {\phi }_{1}\right\rbrack  }_{d}\right\rbrack  }_{\delta } \in  {H}_{\delta }^{p + 2, q - 1}{H}_{d}^{*, q - 1}.
\]

但 \( {H}_{\delta }^{p + 2, q - 1}{H}_{d}^{*, q - 1} = 0 \) ，所以由 (35) 可得:存在 \( {\phi }_{1}^{\prime } \) 与 \( {\phi }_{2} \) 使得(37)

![bo_d7e85t491nqc73eqefm0_360_688_958_895_516_0.jpg](images/fu_algebraic_topology_and_differential_forms_061_bod7e85t491nqc73eqefm03606889588955160.jpg)

拼装(36)与(37)，得

\[
0 \uparrow  {D}^{\prime \prime }
\]

\[
\phi \overset{\delta }{ \rightarrow  }{\delta \phi } + {D}^{\prime \prime }\left( {{\phi }_{1} + {\phi }_{1}^{\prime }}\right)  = 0
\]

\[
{D}^{\prime \prime }
\]

\( {\phi }_{1} + {\phi }_{1}^{\prime } \; + {\phi }_{1}^{\prime }\;\overset{\delta }{ \rightarrow  }\delta \left( {{\phi }_{1} + {\phi }_{1}^{\prime }}\right)  + {D}^{\prime \prime }{\phi }_{2} = 0 \)

用 \( {\phi }_{1} \) 代替 \( {\phi }_{1} + {\phi }_{1}^{\prime } \) ,即有

\( {}^{0} \)

\( {\phi }_{1} \)

\[
\phi \overset{\delta }{ \rightarrow  }{\delta \phi } + {D}^{\prime \prime }{\phi }_{1} = 0
\]

\[
{D}^{\prime \prime } \uparrow
\]

\[
\left. {D}^{\prime \prime }\right\rbrack
\]

如此操作，直到 \( {\phi }_{q} \) . 因为

\[
{\left\lbrack  {\left\lbrack  \delta {\phi }_{q}\right\rbrack  }_{d}\right\rbrack  }_{\delta } \in  {H}_{\delta }^{n + 1,0}{H}_{d}^{*,0} = 0
\]

所以 \( \delta {\phi }_{q} =  - \delta {\phi }_{q}^{\prime },{D}^{\prime \prime }{\phi }_{q}^{\prime } = 0 \) . 用 \( {\phi }_{q} \) 代替 \( {\phi }_{q} + {\phi }_{q}^{\prime } \) ,则最终得到以下图.

\[
\phi  \in  {K}^{p, q} \rightarrow  {\delta \phi } + {D}^{\prime \prime }{\phi }_{1} = 0
\]

\[
{\phi }_{1}\; \rightarrow
\]

\( {D}^{\prime \prime } \)

\[
{\phi }_{q - 1}\overset{\delta }{ \rightarrow  }\delta {\phi }_{q - 1} + {D}^{\prime \prime }{\phi }_{q} = 0
\]

\[
{\phi }_{q} \in  {K}^{n,0}\;\overset{\delta }{ \rightarrow  }\delta {\phi }_{q} = 0
\]

这样,得到一个 \( D \) -上闭链 \( \phi  + {\phi }_{1} + \cdots  + {\phi }_{q} \) . 因此定义

\[
h\left( \left\lbrack  \phi \right\rbrack  \right)  = {\left\lbrack  \phi  + {\phi }_{1} + \cdots  + {\phi }_{q}\right\rbrack  }_{D}.
\]

第二步: 定义 \( g : {H}_{D} \rightarrow  {H}_{\delta }{H}_{d} \) . 设 \( \left\lbrack  \omega \right\rbrack   \in  {H}_{D}^{n} \) ,

\[
\omega  = {\sigma }^{0, n} + {\sigma }^{1, n - 1} + \cdots  + {\sigma }^{n,0}.
\]

(i) 若 \( n < q \) ,定义 \( g\left( \left\lbrack  \omega \right\rbrack  \right)  = 0 \) .

(ii) 若 \( n = q \) ,因为 \( {D\omega } = 0 \) ,所以

\( \left. \begin{matrix} 0 \\  {D}^{\prime \prime } \\   \end{matrix}\right\urcorner \)

\[
{\sigma }^{0, n}\overset{\delta }{ \rightarrow  }\delta {\sigma }^{0, n} + {D}^{\prime \prime }{\sigma }^{1, n - 1} = 0
\]

\[
{D}^{\prime \prime } \uparrow
\]

\( {\sigma }^{1, n - 1} \) .

由 (34) 得 \( \left\lbrack  {\sigma }^{0, n}\right\rbrack   \in  {H}_{\delta }^{0, n}{H}_{d}^{*, n} \) . 定义

\[
g\left( \left\lbrack  \omega \right\rbrack  \right)  = \left\lbrack  {\sigma }^{0, n}\right\rbrack  .
\]

(iii) 若 \( n > q \) ,同理可得 \( \left\lbrack  {\sigma }^{0, n}\right\rbrack   \in  {H}_{\delta }^{0, n}{H}_{d}^{*, n} \) . 由假定 \( \left\lbrack  {\sigma }^{0, n}\right\rbrack   = 0 \) ,所以由 (35) 得

![bo_d7e85t491nqc73eqefm0_365_966_287_387_295_0.jpg](images/fu_algebraic_topology_and_differential_forms_063_bod7e85t491nqc73eqefm03659662873872950.jpg)

于是 \( {\left\lbrack  \omega \right\rbrack  }_{D} = {\left\lbrack  \omega  - D{\sigma }_{1}\right\rbrack  }_{D},\omega  - D{\sigma }_{1} \) 没有第 0 列分量. 所以不妨设

\[
\omega  = {\sigma }^{1, n - 1} + {\sigma }^{2, n - 2} + \ldots
\]

若 \( n - 1 > q \) ,同理可得 \( \left\lbrack  {\sigma }^{1, n - 1}\right\rbrack   \in  {H}_{\delta }{H}_{d} \) . 由于 \( \left\lbrack  {\sigma }^{1, n - 1}\right\rbrack   = 0 \) ,得

![bo_d7e85t491nqc73eqefm0_365_730_982_869_479_0.jpg](images/fu_algebraic_topology_and_differential_forms_062_bod7e85t491nqc73eqefm03657309828694790.jpg)

于是 \( {\left\lbrack  \omega \right\rbrack  }_{D} = {\left\lbrack  \omega  - D\left( {\sigma }_{2} + {\sigma }_{3}\right) \right\rbrack  }_{D},\omega  - D\left( {{\sigma }_{2} + {\sigma }_{3}}\right) \) 没有第 0,1 列,即没有第 \( n \) , \( n - 1 \) 行分量. 如此操作，可设 \( \omega \) 位于第 \( q \) 行之上的所有分量为零:

\[
\omega  = {\sigma }^{n - q, q} + {\sigma }^{n - q + 1, q - 1} + \ldots
\]

定义

\[
g\left( \left\lbrack  \omega \right\rbrack  \right)  = \left\lbrack  {\sigma }^{n - q, q}\right\rbrack  .
\]

第三步: 验证 \( h, g \) 是定义好的.

练习 12.9. 证明 \( h, g \) 是定义好的.

第四步: 验证 \( h, g \) 互逆. 这是显然的.

综上所述，我们已证

\[
{H}_{D}^{n}\overset{ \sim  }{ \rightarrow  }{ \oplus  }_{p + q = n}{H}_{\delta }^{p, q}{H}_{d}^{*, q}.
\]

应用命题 12.1 可给第 8 节的主要结果一个更简练的证明. 设 \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) 是流形 \( M \) 的开覆盖, \( {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)  = \prod {\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) . 根据 MV 序列的正合性,Čech-de Rham 复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 的 \( {H}_{\delta } \) 与 \( {H}_{d}{H}_{\delta } \) 分别是

![bo_d7e85t491nqc73eqefm0_367_141_543_960_550_0.jpg](images/fu_algebraic_topology_and_differential_forms_065_bod7e85t491nqc73eqefm03671415439605500.jpg)

![bo_d7e85t491nqc73eqefm0_367_1182_543_998_549_0.jpg](images/fu_algebraic_topology_and_differential_forms_064_bod7e85t491nqc73eqefm036711825439985490.jpg)

因为 \( {H}_{d}{H}_{\delta } \) 仅有一列非零,所以由命题 12.1 得到对任意开覆盖 \( \mathcal{U} \) ,

\[
{H}_{D}^{ * }\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}   \simeq  {H}_{dR}^{ * }\left( M\right) .
\]

这是推广的 MV 原理, 即命题 8.8 . 如果 \( \mathcal{U} \) 是好覆盖，由 Poincaré 引理 \( {H}_{d} \) 与 \( {H}_{\delta }{H}_{d} \) 分别是

\[
{H}_{d} = \left\lbrack  \begin{matrix} q \\   \\   \\   \\  {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right) {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) {C}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \\   \\  0\;1\;2 \end{matrix}\right\rbrack  \;{H}_{\delta }{H}_{d} = \left\lbrack  \begin{matrix} q \\   \\   \\  {H}_{\delta }{H}_{d} \\   \\   \\  {H}^{0}\left( {\mathcal{U},\mathbb{R}}\right) {H}^{1}\left( {\mathcal{U},\mathbb{R}}\right) {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \\   \\  0\;1\;2 \end{matrix}\right\rbrack  ,
\]

又因为 \( {H}_{\delta }{H}_{d} \) 仅有一行非零,于是由命题 12.1 得

\[
{H}_{D}^{ * }\left\{  {{C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) }\right\}   \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) .
\]

结合这两个同构给出了

\[
{H}_{dR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {\mathcal{U},\mathbb{R}}\right) .
\]

练习 12.10. 设

\[
Z = \left\lbrack  {{Z}_{0} : {Z}_{1} : \cdots  : {Z}_{n}}\right\rbrack
\]

是 \( \mathbb{C}{P}^{n} \) 的齐次坐标. 定义

\[
{U}_{i} = \left\{  {Z \mid  {Z}_{i} \neq  0}\right\}  \text{ . }
\]

则 \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},\ldots ,{U}_{n}}\right\} \) 是 \( \mathbb{C}{P}^{n} \) 的开覆盖,但不是好覆盖. 从双复形 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 计算 \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) . 求在 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 中的元,它表示 \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) 的生成元.

Poincaré 对偶注记 10.3 讲了共变函子的情形. 现应用共变函子 \( {\Omega }_{c}^{ * } \) . 设 \( M \) 是 \( n \) 维流形, \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) 是 \( M \) 的开覆盖. 定义上边缘算子

\[
\delta  : \bigoplus {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  \bigoplus {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right)
\]

为

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}},
\]

其中右边表示的是把定义在 \( {U}_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \) 上的形式 \( {\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \) 零延拓到 \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) 上. 为了保证 \( {\delta \omega } \) 的每个分量有紧支集,此处的群是直和而不是直积,所以根据定义 \( \omega  \in   \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) 仅有有限多个分量不为零.

命题 12.12. (对紧支集的广义 MV 序列) 假定 \( M \) 的开覆盖 \( \mathcal{U} = \left\{  {U}_{\alpha }\right\} \) 满足局部有限条件:

(*) 每个开集 \( {U}_{\alpha } \) 仅与有限多个 \( {U}_{\beta } \) 相交.

则序列

\[
0 \leftarrow  {\Omega }_{c}^{ * }\left( M\right) \overset{\mathrm{{sum}}}{ \leftarrow  } \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \leftarrow  } \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \leftarrow  }\cdots \overset{\delta }{ \leftarrow  } \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \overset{\delta }{ \leftarrow  }\ldots
\]

是正合的.

证. 首先证明 \( {\delta }^{2} = 0 \) . 设 \( \omega  \in   \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) . 则

\[
{\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 2}} = \mathop{\sum }\limits_{\alpha }{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 2}} = \mathop{\sum }\limits_{\alpha }\mathop{\sum }\limits_{\beta }{\omega }_{{\beta \alpha }{\alpha }_{0}\ldots {\alpha }_{p - 2}} = 0,
\]

因为 \( {\omega }_{{\alpha \beta }\ldots } =  - {\omega }_{{\beta \alpha }\ldots } \) . 现假定 \( \omega  \in  \bigoplus {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) 满足 \( {\delta \omega } = 0 \) . 需证明 \( \omega \) 是 \( \delta \) -上边缘的. 设 \( \left\{  {\rho }_{\alpha }\right\} \) 是从属于开覆盖 \( \mathcal{U} \) 的单位分解. 定义

\[
{\tau }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\rho }_{{\alpha }_{i}}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}}.
\]

需检查 \( \tau  \in  \bigoplus {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}...{\alpha }_{p + 1}}\right) \) . 首先注意到 \( {\tau }_{{\alpha }_{0}...{\alpha }_{p + 1}} \) 有紧支集. 其次,因为 \( \omega \) 只有有限多个分量 \( {\omega }_{{\alpha }_{0}...{\alpha }_{p}} \neq  0 \) ,而根据局部有限条件 \( \left( *\right) \) 每个 \( {U}_{{\alpha }_{0}...{\alpha }_{p}} \subset  {U}_{{\alpha }_{0}} \) 只与有限多个 \( {U}_{\beta } \) 相交,所以只有有限多个 \( {\rho }_{\beta }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \neq  0 \) . 这样 \( \tau \) 只有有限多个分量不为零.

接着检查 \( {\delta \tau } = \omega \) :

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \mathop{\sum }\limits_{\alpha }{\tau }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}}
\]

\[
= \mathop{\sum }\limits_{\alpha }\left( {{\rho }_{\alpha }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{\rho }_{{\alpha }_{i}}{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}}\right)
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{\rho }_{{\alpha }_{i}}{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}}
\]

练习 12.12.1. 证明 \( \tau \) 的定义给出了对紧 MV 序列 (12.12) 的同伦算子. 更精确地说，若对 \( \omega  \in   \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) 定义

\[
{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\rho }_{{\alpha }_{i}}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}},
\]

则

\[
{\delta K} + {K\delta } = 1.
\]

设 \( \mathcal{U} \) 满足局部有限条件 \( \left( *\right) \) . 考虑双复形 \( {C}^{p}\left( {\mathcal{U},{\Omega }_{c}^{q}}\right) \) :

![bo_d7e85t491nqc73eqefm0_374_343_283_1633_550_0.jpg](images/fu_algebraic_topology_and_differential_forms_067_bod7e85t491nqc73eqefm037434328316335500.jpg)

在这个双复形中算子 \( \delta \) 的方向相反,所以定义新复形

\[
{K}^{-p, q} = {C}^{p}\left( {\mathcal{U},{\Omega }_{c}^{q}}\right) .
\]

根据行的正合性, \( {H}_{\delta }\left( K\right) \) 是

![bo_d7e85t491nqc73eqefm0_374_355_1206_1707_471_0.jpg](images/fu_algebraic_topology_and_differential_forms_068_bod7e85t491nqc73eqefm0374355120617074710.jpg)

![bo_d7e85t491nqc73eqefm0_375_393_517_1538_556_0.jpg](images/fu_algebraic_topology_and_differential_forms_069_bod7e85t491nqc73eqefm037539351715385560.jpg)

因为 \( {H}_{d}{H}_{\delta } \) 仅有一列非零,由命题 12.1 得到

(12.13)

\[
{H}_{D}\left( K\right)  = {H}_{d}{H}_{\delta }\left( K\right)  = {H}_{c}\left( M\right) .
\]

另一方面,若 \( \mathcal{U} \) 是好覆盖,则 \( {H}_{d}\left( K\right) \) 是

\[
{H}_{d}^{-p, q}\left( K\right)  = {C}^{p}\left( {\mathcal{U},{\mathcal{H}}_{c}^{q}}\right)
\]

其中 \( {\mathcal{H}}_{c}^{q} \) 是共变函子,它对每个开集 \( U \) 赋予紧上同调 \( {H}_{c}^{q}\left( U\right) \) ,并对每个包含 \( i,{i}_{ * } \) 是零延拓. 由对紧支集的 Poincaré 引理,

\[
{H}_{d}^{-p, q}\left( K\right)  = \left\{  \begin{array}{ll} 0 & q \neq  n; \\  {\bigoplus }_{{\alpha }_{0} < \cdots  < {\alpha }_{p}}\mathbb{R} & q = n. \end{array}\right.
\]

![bo_d7e85t491nqc73eqefm0_376_267_765_1793_464_0.jpg](images/fu_algebraic_topology_and_differential_forms_070_bod7e85t491nqc73eqefm037626776517934640.jpg)

再根据命题 12.1,

(12.14)

\[
{H}_{D}^{ * }\left( K\right)  = {H}_{\delta }^{* - n, n}{H}_{d} = {H}_{n -  * }\left( {\mathcal{U},{\mathcal{H}}_{c}^{n}}\right) .
\]

此处 \( {H}_{n -  * }\left( {\mathcal{U},{\mathcal{H}}_{c}^{n}}\right) \) 是覆盖 \( \mathcal{U} \) 的系数在共变函子 \( {\mathcal{H}}_{c}^{n} \) 的第 \( \left( {n -  * }\right) \) 个 Čech 同调, 参考注记 10.3.

比较 (12.13) 与 (12.14) 得到

定理 12.15. (Poincaré 对偶) 设 \( M \) 是 \( n \) 维流形, \( \mathcal{U} \) 是 \( M \) 的好覆盖且满足命题 12.12 的局部有限条件 \( \left( *\right) \) . 此处不需假定 \( M \) 是可定向的. 则

\[
{H}_{c}^{ * }\left( M\right)  \simeq  {H}_{n -  * }\left( {\mathcal{U},{\mathcal{H}}_{c}^{n}}\right) ,
\]

其中 \( {\mathcal{H}}_{c}^{n} \) 是共变函子 \( {\mathcal{H}}_{c}^{n}\left( U\right)  = {H}_{c}^{n}\left( U\right) \) .

练习 12.16. 应用 Poincaré 对偶 (12.15) 计算开 Möbinus 带的紧上同调, 参考练习 4.8.

作业:

1. 练习 12.9.

2. 练习 12.10.

3. 练习 12.12.1.

4. 练习 12.16.

代数拓扑与微分形式
