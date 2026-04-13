#### 29. π4(S3) 与 π5(S3) 的计算

§18. Applications to Homotopy Theory (2)

29. \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算

这次课讲 \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算,为此先讲 EM 空间 \( K\left( {\mathbb{Z},3}\right) \) 的上同调计算. 我们把 Postnikov 逼近与 Whitehead 塔这两种技巧揉合在 \( {\pi }_{4}\left( {S}^{3}\right) \) 与 \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算中.

- \( K\left( {\mathbb{Z},3}\right) \) 的上同调

- \( {\pi }_{4}\left( {S}^{3}\right) \) 的计算

- \( {\pi }_{5}\left( {S}^{3}\right) \) 的计算因为 \( {\pi }_{1}\left( {S}^{3}\right)  = {\pi }_{2}\left( {S}^{3}\right)  = 0,{\pi }_{3}\left( {S}^{3}\right)  = \mathbb{Z} \) ,人们自然会问是否对 \( q > 3,{\pi }_{q}\left( {S}^{3}\right)  = \) 0,即 \( {S}^{3} \) 是否就是 \( K\left( {\mathbb{Z},3}\right) \) . 要回答这个问题可先计算 \( K\left( {\mathbb{Z},3}\right) \) 的上同调.

首先观察到

\[
{\Omega K}\left( {\mathbb{Z},3}\right)  = K\left( {\mathbb{Z},2}\right)  = \mathbb{C}{P}^{\infty }.
\]

所以有道路纤维化

![bo_d7e85t491nqc73eqefm0_685_863_992_597_307_0.jpg](images/fu_algebraic_topology_and_differential_forms_227_bod7e85t491nqc73eqefm06858639925973070.jpg)

由练习 18.4, \( {H}^{ * }\left( {\mathbb{C}{P}^{\infty }}\right)  = \mathbb{Z}\left\lbrack  x\right\rbrack  ,\dim x = 2 \) . 由注记 17.13,每个 CW 复形有好覆盖. 所以 \( K\left( {\mathbb{Z},3}\right) \) 有好覆盖且它是单连通的,我们能应用此道路纤维化的谱序列计算 \( K\left( {\mathbb{Z},3}\right) \) 的上同调. 根据整系数的 Leray 定理 (15.11),谱序列的 \( {E}_{2} \) 页是

\[
{E}_{2}^{p, q} = {H}^{p}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \otimes  {H}^{q}\left( {\mathbb{C}{P}^{\infty }}\right)
\]

且积结构是张量积. 所以它的奇数行为零. 于是 \( {d}_{2} = 0,{E}_{3} = {E}_{2} \) . 由 Hurewicz 同构定理, 有

\[
{H}_{p}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = \left\{  \begin{array}{ll} 0 & p = 1,2 \\  \mathbb{Z} & p = 3. \end{array}\right.
\]

再由推论 15.14.1 , 得

\[
{H}^{p}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = \left\{  \begin{array}{ll} 0 & p = 1,2 \\  \mathbb{Z} & p = 3. \end{array}\right.
\]

## 所以有图

![bo_d7e85t491nqc73eqefm0_687_300_304_1727_1035_0.jpg](images/fu_algebraic_topology_and_differential_forms_228_bod7e85t491nqc73eqefm0687300304172710350.jpg)

因为全空间 \( {PK}\left( {\mathbb{Z},3}\right) \) 是可缩的, \( {E}_{\infty } \) 除了 \( {E}_{\infty }^{0,0} \) 之外全为零. 计划是在 \( {E}_{2} = {E}_{3} \) 的底部一行中“产生”必要的非零元用来杀掉谱序列中所有可能会永远活下去的非零元.

由于要将 \( a \) 与 \( s \) 杀掉,所以 \( {d}_{3} : {E}_{3}^{0,2} \rightarrow  {E}_{3}^{3,0} \) 是同构: \( {d}_{3}a = s \) . 于是

\[
{E}_{4}^{0,2} = {E}_{4}^{3,0} = 0
\]

计算

\[
{d}_{3}\left( {a}^{2}\right)  = {2a}{d}_{3}a = {2as} \neq  0.
\]

所以 \( {a}^{2} \) 不能活到 \( {E}_{4} \) ，

\[
{E}_{4}^{0,4} = 0\text{ . }
\]

但是 \( {d}_{3}\left( {as}\right)  \in  {E}_{3}^{6,0} \) 一定不为零,否则 \( {as} \in  {E}_{3}^{3,2} \) 将活到 \( {E}_{\infty } \) . 所以

\[
{d}_{3}\left( {as}\right)  = {d}_{3}a \cdot  s = {s}^{2} \neq  0.
\]

于是 \( {H}^{6}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \neq  0 \) . 这就证明了 \( {S}^{3} \) 不是 \( {EM} \) 空间 \( K\left( {\mathbb{Z},3}\right) \) . 继续计算 \( K\left( {\mathbb{Z},3}\right) \) 的上同调环. 显然对 \( k = 4,5 \) ,

\[
{H}^{k}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = 0
\]

因为否则无法被杀死. 又因为 \( 0 = {d}_{3}^{2}\left( {a}^{2}\right)  = {d}_{3}\left( {{2a} \cdot  s}\right)  = 2{s}^{2} \) ,所以

\[
{H}^{6}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = {\mathbb{Z}}_{2}
\]

\( {E}_{3}^{7,0} = {H}^{7}\left( {K\left( {\mathbb{Z},3}\right) }\right) \) 中一个非零元仅能被 \( {a}^{3} \) 在 \( {d}_{7} \) 下杀死. 但是

\[
{d}_{3}\left( {a}^{3}\right)  = 3{a}^{2}{d}_{3}a = 3{a}^{2} \cdot  s \neq  0,
\]

所以 \( {a}^{3} \) 不能活到 \( {E}_{4} \) . 因此 \( {H}^{7}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = 0 \) . 又因为 \( {d}_{3}\left( {{a}^{2}s}\right)  = {2a}{s}^{2} = 0 \) , \( {a}^{2}s \in  {E}_{4}^{3,4} \) . 显然 \( {d}_{4}\left( {{a}^{2}s}\right)  = 0 \) ,所以 \( {a}^{2}s \in  {E}_{5}^{3,4} \) . 这样 \( {a}^{2}s \) 将活到 \( {E}_{\infty } \) ,除非 \( {d}_{5}\left( {{a}^{2}s}\right)  = t \neq  0 \) . 但是为了杀死这个新增的 \( t,{d}_{5} : {E}_{5}^{3,4} \rightarrow  {E}_{5}^{8,0} \) 必须是同构. 因为 \( {E}_{5}^{3,4} = {E}_{4}^{3,4} = \frac{\ker {d}_{3}}{\operatorname{im}{d}_{3}} = {\mathbb{Z}}_{3} \) ,所以 \( {E}_{5}^{8,0} = {\mathbb{Z}}_{3} \) ,即 \( {H}^{8}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = {\mathbb{Z}}_{3} \) .

综上所述, 有(18.11)

<table><tr><td>q</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>\( \mathrm{{H}^{q}} \)</td><td>Z</td><td>0</td><td>0</td><td>Z</td><td>0</td><td>0</td><td>\( {\mathrm{Z}}_{2} \)</td><td>0</td><td>\( {\mathbf{Z}}_{3} \)</td></tr><tr><td>生成元</td><td>1</td><td></td><td></td><td>S</td><td></td><td></td><td>\( {\mathrm{s}}^{2} \)</td><td></td><td>t</td></tr></table>

\( {\pi }_{4}\left( {S}^{3}\right) \) 的计算

记 \( {\pi }_{q} = {\pi }_{q}\left( {S}^{3}\right) \) .

引理. 可用贴胞腔到 \( {S}^{3} \) 的方法得到空间 \( {Y}_{4} \) 使得

\[
{\pi }_{q}\left( {Y}_{4}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & q = 3 \\  {\pi }_{4} & q = 4 \\  0 & q \neq  3,4. \end{array}\right.
\]

证. 若 \( {\pi }_{5} \neq  0 \) ,用 \( \alpha  : {S}^{5} \rightarrow  {S}^{3} \) 表示一个 \( \left\lbrack  \alpha \right\rbrack   \neq  0 \in  {\pi }_{5} \) . 由 \( \alpha \) 可贴一个 6-胞腔到 \( {S}^{3} \) :

\[
X = {S}^{3}{ \cup  }_{\alpha }{e}^{6} = {S}^{3}\coprod {e}^{6}/\alpha \left( x\right)  \sim  x,\;x \in  {S}^{5} = \partial {e}^{6}.
\]

由贴胞腔的同伦群性质知对 \( q = 1,2,3,4,{\pi }_{q}\left( X\right)  = {\pi }_{q}\left( {S}^{3}\right) \) ,并且通过贴此胞腔把 \( \lbrack \alpha \rbrack \) 杀掉了,因为 \( \alpha \) 在 \( {e}^{6} \) 中同伦于零. 这样通过贴 6-胞腔可把 \( {\pi }_{5} \) 中所有非平凡元杀掉. 记这样的拓扑空间为 \( {X}_{5} \) ,它满足 \( {\pi }_{5}\left( {X}_{5}\right)  = 0 \) 且 \( {\pi }_{q}\left( {X}_{5}\right)  = {\pi }_{q}\left( {S}^{3}\right) \) 对 \( q \leq  4 \) .

可通过贴 7-胞腔到 \( {X}_{5} \) 杀掉 \( {\pi }_{6}\left( {X}_{5}\right) \) 的所有非平凡元而不改变 \( {\pi }_{q}\left( {X}_{5}\right) \) 对 \( q \leq  5 \) . 如此下去可能直至无穷,得到空间 \( {Y}_{4} \) 使得结论成立.

再对 \( {Y}_{4} \) 从贴 5-胞腔开始重复上述操作，可得 \( K\left( {\mathbb{Z},3}\right) \) . 由贴胞腔的性质知 \( {\pi }_{3}\left( {Y}_{4}\right)  \rightarrow  {\pi }_{3}\left( {K\left( {\mathbb{Z},3}\right) }\right) \) 是同构.

在同伦论中可将包含视为纤维化,所以可将包含 \( {Y}_{4} \hookrightarrow  K\left( {\mathbb{Z},3}\right) \) 整成纤维化.

(18.18) 纤维化. 设

\[
L = \left\{  {\mu  : I \rightarrow  K\left( {\mathbb{Z},3}\right)  \mid  \mu \left( 0\right)  \in  {Y}_{4}}\right\}  .
\]

由于 \( K\left( {\mathbb{Z},3}\right) \) 是道路连通的，通过收缩每条道路到它的起点，我们得到同伦等价

\[
L \simeq  {Y}_{4}\text{ . }
\]

另一方面，通过定义端点映射

\[
\pi  : L \rightarrow  K\left( {\mathbb{Z},3}\right) ,\;\pi \left( \mu \right)  = \mu \left( 1\right)
\]

![bo_d7e85t491nqc73eqefm0_691_789_1084_693_612_0.jpg](images/fu_algebraic_topology_and_differential_forms_229_bod7e85t491nqc73eqefm069178910846936120.jpg)

得到纤维化

\[
\begin{matrix} {\Omega }_{ * }^{{Y}_{4}} \rightarrow  L \simeq  {Y}_{4} \\  \pi  \mid  \\  K\left( {\mathbb{Z},3}\right)  \end{matrix}
\]

其中纤维 \( {\Omega }_{ * }^{{Y}_{4}} \) 是

\[
{\Omega }_{ * }^{{Y}_{4}} = {\pi }^{-1}\left( *\right)  = \{ \mu  \in  L \mid  \mu \left( 1\right)  =  * \} ,
\]

其中 * 是 \( K\left( {\mathbb{Z},3}\right) \) 中固定的一点. 应用纤维化的同伦序列:

\[
\cdots  \rightarrow  {\pi }_{i + 1}\left( {\Omega }_{ * }^{{Y}_{4}}\right)  \rightarrow  {\pi }_{i + 1}\left( {Y}_{4}\right)  \rightarrow  {\pi }_{i + 1}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \rightarrow
\]

\[
\rightarrow  {\pi }_{i}\left( {\Omega }_{ * }^{{Y}_{4}}\right)  \rightarrow  {\pi }_{i}\left( {Y}_{4}\right)  \rightarrow  {\pi }_{i}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \rightarrow  \ldots
\]

可得

\[
{\pi }_{q}\left( {\Omega }_{ * }^{{Y}_{4}}\right)  = \left\{  \begin{array}{ll} {\pi }_{4} & q = 4 \\  0 & q \neq  4, \end{array}\right.
\]

即 \( {\Omega }_{ * }^{{Y}_{4}} = K\left( {{\pi }_{4},4}\right) \) .

于是纤维化 (18.18) 在同伦等价的意义下可化为

![bo_d7e85t491nqc73eqefm0_693_833_1171_656_303_0.jpg](images/fu_algebraic_topology_and_differential_forms_230_bod7e85t491nqc73eqefm069383311716563030.jpg)

虽然 \( {Y}_{4} \neq  K\left( {\mathbb{Z},3}\right)  \times  K\left( {{\pi }_{4},4}\right) \) ,但可把它看作 “扭” 积. 应用推论 15.14.1,由 \( K\left( {\mathbb{Z},3}\right) \) 的一些上同调 (18.11) 可计算其同调:

\[
{H}_{k}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & k = 0,3 \\  0 & k = 1,2,4,6 \\  {\mathbb{Z}}_{2} & k = 5. \end{array}\right.
\]

再由 Hurewicz 同构定理可知 \( {H}_{q}\left( {K\left( {{\pi }_{4},4}\right) }\right) \) 当 \( q \leq  4 \) 时的值. 所以上述纤维化的同调谱序列的 \( {E}^{2} \) 页是

![bo_d7e85t491nqc73eqefm0_694_554_675_1209_544_0.jpg](images/fu_algebraic_topology_and_differential_forms_231_bod7e85t491nqc73eqefm069455467512095440.jpg)

K(Z,3)

另一方面,由于 \( {Y}_{4} \) 是在 \( {S}^{3} \) 上通过贴 6-胞腔,7-胞腔等得到的,由命题 17.12 可得 \( {H}_{4}\left( {Y}_{4}\right)  = {H}_{5}\left( {Y}_{4}\right)  = 0 \) . 于是

\[
{d}^{5} : {E}_{5,0}^{5} = {E}_{5,0}^{2}\overset{ \sim  }{ \rightarrow  }{E}_{0,4}^{5} = {E}_{0,4}^{2}.
\]

因此 \( {\pi }_{4} = {\mathbb{Z}}_{2} \) .

\( {\pi }_{5}\left( {S}^{3}\right) \) 的计算

设 \( X \) 是 \( n \) -连通空间,即对 \( 1 \leq  q \leq  n,{\pi }_{q}\left( X\right)  = 0 \) . 设 \( Y \) 是从 \( X \) 出发通过贴 \( \left( {n + 3}\right) \) -胞腔起把 \( X \) 的维数大于 \( n + 1 \) 的同伦群的非平凡元都杀死而得到的空间 \( K\left( {{\pi }_{n + 1}\left( X\right) , n + 1}\right) \) . 则 \( X \subset  Y \) . 设 \( *  \in  Y \) 并定义

\[
{\Omega }_{ * }^{X} = \{ \mu  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  Y \mid  \mu \left( 0\right)  =  * ,\mu \left( 1\right)  \in  X\} .
\]

![bo_d7e85t491nqc73eqefm0_695_859_697_620_459_0.jpg](images/fu_algebraic_topology_and_differential_forms_232_bod7e85t491nqc73eqefm06958596976204590.jpg)

在端点映射

\[
\pi  : {\Omega }_{ * }^{X} \rightarrow  X,\;\pi \left( \mu \right)  = \mu \left( 1\right)
\]

下 \( X \) 中每点的逆像同伦等价于 \( Y \) 的圈空间 \( {\Omega Y} \) ,即

\[
{\Omega Y} = {\Omega K}\left( {{\pi }_{n + 1}\left( X\right) , n + 1}\right)  = K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) .
\]

于是有纤维化

\[
K\left( {{\pi }_{n + 1}\left( X\right) , n}\right)  \rightarrow  {\Omega }_{ * }^{X}
\]

用纤维化同伦序列

\[
\cdots  \rightarrow  {\pi }_{q}\left( {K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) }\right)  \rightarrow  {\pi }_{q}\left( {\Omega }_{ * }^{X}\right)  \rightarrow  {\pi }_{q}\left( X\right)  \rightarrow
\]

\[
\rightarrow  {\pi }_{q - 1}\left( {K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) }\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega }_{ * }^{X}\right)  \rightarrow  {\pi }_{q - 1}\left( X\right)  \rightarrow  \ldots
\]

得到

\[
{\pi }_{q}\left( {\Omega }_{ * }^{X}\right)  = 0\;\text{ 当 }q \leq  n - 1,\;\text{ 因为 }{\pi }_{q}\left( X\right)  = {\pi }_{q}\left( {K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) }\right)  = 0;
\]

\[
{\pi }_{q}\left( {\Omega }_{ * }^{X}\right)  = {\pi }_{q}\left( X\right) \;\text{ 当 }q \geq  n + 2,
\]

\[
{\pi }_{n + 1}\left( {\Omega }_{ * }^{X}\right)  = {\pi }_{n}\left( {\Omega }_{ * }^{X}\right)  = 0.
\]

最后一个等式是由于在上述正合同伦序列中若 \( q = n + 1 \) ,映射

\[
{\pi }_{n + 1}\left( X\right)  \rightarrow  {\pi }_{n}\left( {K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) }\right)  = {\pi }_{n + 1}\left( X\right)
\]

是恒等映射并且由于 \( {\pi }_{n + 1}\left( {K\left( {{\pi }_{n + 1}\left( X\right) , n}\right) }\right)  = 0,{\pi }_{n}\left( X\right)  = 0 \) .

记 \( {X}_{n + 1} = {\Omega }_{ * }^{X} \) . 综上所述,有

断言. 设 \( {X}_{n} \) 是一个 \( n \) -连通的拓扑空间. 可构造一个 \( \left( {n + 1}\right) \) -连通空间 \( {X}_{n + 1} \) 使得它有纤维化

\[
K\left( {{\pi }_{n + 1}\left( {X}_{n}\right) , n}\right)  \rightarrow  {X}_{n + 1}
\]

并且当 \( q \geq  n + 2 \) 时, \( {\pi }_{q}\left( {X}_{n + 1}\right)  = {\pi }_{q}\left( {X}_{n}\right) \) .

因为 \( {S}^{3} \) 是 2-连通的,所以可构造纤维化

![bo_d7e85t491nqc73eqefm0_697_917_1166_497_298_0.jpg](images/fu_algebraic_topology_and_differential_forms_233_bod7e85t491nqc73eqefm069791711664972980.jpg)

使得 \( {X}_{3} \) 是 3-连通的且当 \( q \geq  4 \) 时, \( {\pi }_{q}\left( {X}_{3}\right)  = {\pi }_{q}\left( {S}^{3}\right) \) .

于是又可构造纤维化

![bo_d7e85t491nqc73eqefm0_698_902_156_533_299_0.jpg](images/fu_algebraic_topology_and_differential_forms_234_bod7e85t491nqc73eqefm06989021565332990.jpg)

使得 \( {X}_{4} \) 是 4-连通的且当 \( q \geq  5 \) 时, \( {\pi }_{q}\left( {X}_{4}\right)  = {\pi }_{q}\left( {X}_{3}\right) \) . 所以当 \( q \geq  5 \) 时, \( {\pi }_{q}\left( {S}^{3}\right)  = {\pi }_{q}\left( {X}_{4}\right) . \)

旁白. 把上述两个纤维化组装在一起:

![bo_d7e85t491nqc73eqefm0_698_903_803_532_504_0.jpg](images/fu_algebraic_topology_and_differential_forms_235_bod7e85t491nqc73eqefm06989038035325040.jpg)

当然可以继续这种纤维化, 最后得到 Whitehead 塔.

由于 \( {X}_{4} \) 是 4-连通的,由 Hurewicz 定理, \( {H}_{5}\left( {X}_{4}\right)  = {\pi }_{5}\left( {X}_{4}\right) \) . 所以

\[
{\pi }_{5}\left( {S}^{3}\right)  = {H}_{5}\left( {X}_{4}\right)
\]

于是要计算 \( {X}_{4} \) 的上同调. 首先计算 \( {X}_{3} \) 的上同调. 纤维化 \( K\left( {\mathbb{Z},2}\right)  \rightarrow  {X}_{3} \rightarrow  {S}^{3} \) 的上同调谱序列的 \( {E}_{2} \) 页是

![bo_d7e85t491nqc73eqefm0_699_684_369_917_791_0.jpg](images/fu_algebraic_topology_and_differential_forms_236_bod7e85t491nqc73eqefm06996843699177910.jpg)

由于 \( {E}_{2} \) 隔行为零,所以 \( {d}_{2} = 0,{E}_{3} = {E}_{2} \) . 因为 \( {X}_{3} \) 是 3-连通的,由 Hurewicz 同构定理知当 \( q = 1,2,3 \) 时, \( {H}_{q}\left( {X}_{3}\right)  = 0 \) . 由泛系数定理的推论知当 \( q = 1,2,3 \) 时, \( {H}^{q}\left( {X}_{3}\right)  = 0 \) . 所以 \( {d}_{3} : {E}_{3}^{0,2} \rightarrow  {E}_{3}^{3,0} \) 是同构, \( {d}_{3}x = u \) . 于是

\[
{d}_{3}\left( {x}^{n}\right)  = n{x}^{n - 1}{d}_{3}x = n{x}^{n - 1}u.
\]

这样我们得到

![bo_d7e85t491nqc73eqefm0_700_651_253_985_699_0.jpg](images/fu_algebraic_topology_and_differential_forms_238_bod7e85t491nqc73eqefm07006512539856990.jpg)

因此 \( {X}_{3} \) 的整系数上同调与同调是

<table><tr><td>q</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>\( {\mathrm{H}}^{\mathrm{q}}\left( {\mathrm{X}}_{3}\right) \)</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>0</td><td>\( {\mathrm{Z}}_{2} \)</td><td>0</td><td>\( {z}_{3} \)</td><td>0</td><td>\( {\mathrm{Z}}_{4} \)</td><td>0</td><td>\( {Z}_{5} \)</td></tr><tr><td>\( {\mathrm{H}}_{\mathrm{q}}\left( {\mathrm{X}}_{3}\right) \)</td><td>Z</td><td>0</td><td>0</td><td>0</td><td>\( {Z}_{2} \)</td><td>0</td><td>\( {\mathrm{Z}}_{3} \)</td><td>0</td><td>\( {\mathrm{Z}}_{4} \)</td><td>0</td><td>\( {\mathrm{Z}}_{5} \)</td><td>0</td></tr></table>

此处应用推论 15.14.1, 由上同调得到同调. 再考虑纤维化 \( K\left( {{\pi }_{4},3}\right)  \rightarrow  {X}_{4} \rightarrow  {X}_{3} \) 的同调谱序列,它的 \( {E}^{2} \) 页是

![bo_d7e85t491nqc73eqefm0_701_725_249_833_725_0.jpg](images/fu_algebraic_topology_and_differential_forms_239_bod7e85t491nqc73eqefm07017252498337250.jpg)

因为 \( {X}_{4} \) 是 4-连通的,所以对 \( q = 1,2,3,4,{H}_{q}\left( {X}_{4}\right)  = 0 \) . 所以 \( {d}^{4} : {E}_{4,0}^{4} \rightarrow  {E}_{0,3}^{4} \) 是同构. 于是 \( {\pi }_{4} = {\mathbb{Z}}_{2} \) .

由练习 18.16 知 \( {H}_{4}\left( {K\left( {{\mathbb{Z}}_{2},3}\right) }\right)  = 0,{H}_{5}\left( {K\left( {{\mathbb{Z}}_{2},3}\right) }\right)  = {\mathbb{Z}}_{2} \) . 因为从 \( {\mathbb{Z}}_{3} \) 到 \( {\mathbb{Z}}_{2} \) 的仅有同态是零映射,所以 \( {d}_{6} = 0 \) . 于是 \( {E}_{0,5}^{\infty } = {E}_{0,5}^{7} = {\mathbb{Z}}_{2},{H}_{5}\left( {X}_{4}\right)  = {\mathbb{Z}}_{2} \) . 因此

\[
{\pi }_{5}\left( {S}^{3}\right)  = {\pi }_{5}\left( {X}_{4}\right)  = {H}_{5}\left( {X}_{4}\right)  = {\mathbb{Z}}_{2}.
\]

作业:

练习 18.15. 计算上同调 \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},2}\right) ;{\mathbb{Z}}_{2}}\right) ,{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},2}\right) ;\mathbb{Z}}\right) \) 直到 6 维. 练习 18.16. 计算上同调 \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},3}\right) ;{\mathbb{Z}}_{2}}\right) ,{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},3}\right) ;\mathbb{Z}}\right) \) 直到 6 维. 练习 18.16.1. 计算同调 \( {H}_{ * }\left( {K\left( {{\mathbb{Z}}_{2},4}\right) ;\mathbb{Z}}\right) \) 直到 6 维.
