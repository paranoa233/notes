#### 第12讲 More Examples and Applications of the Mayer-Vietoris Principle

§9 More Examples and Applications of the Mayer-Vietoris Principle

## 12. 显式同构

上次课应用 MV 原理证明流形的 de Rham 上同调与好覆盖的 Čech 上同调同构， 并由此得到各种推论. 这次课首先给出利用好覆盖的组合计算 de Rham 上同调的一些例子；接着作为显式同构的例子给出从 \( {H}_{dR}^{2}\left( M\right) \) 到 \( {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \) ，再从 \( {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \) 到 \( {H}_{dR}^{2}\left( M\right) \) 的显式同构；最后给出从 Čech 到 de Rham 的显式同构:给定一个 Čech 上闭链, 利用建立在同伦算子 \( K \) 基础上的 collating 公式可构造对应的整体闭微分形式.

我们没有讲书本这节的最后部分，即作为 MV 原理的另一应用证明 Künneth 公式. 相比以前的结果把底流形具有有限好覆盖的条件减弱为具有有限维上同调.

- 例子:从好覆盖的组合计算 de Rham 上同调

- 显式同构的一个例子: \( {H}_{dR}^{2}\left( M\right)  \simeq  {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \)

- 显式同构

例子:从好覆盖的组合计算 de Rham 上同调设 \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 是 \( M \) 的开覆盖. \( \mathcal{U} \) 的 nerve \( N\left( \mathcal{U}\right) \) 是按以下定义的单纯复形:对每个 \( {U}_{\alpha } \in  \mathcal{U} \) ，赋予一个顶点 \( \alpha \) ；若 \( {U}_{\alpha \beta } \neq  \varnothing \) ，则用一条线段连接 \( \alpha \) ， \( \beta \) ；若 \( {U}_{\alpha \beta \gamma } \neq  \varnothing \) ,则填满三角形 \( {\alpha \beta \gamma } \) 的内部; 如此下去得到 \( \mathcal{U} \) 的 nerve.

例 9.1. \( \left( {S}^{1}\right) \) 如图,取 \( {S}^{1} \) 的一个好覆盖 \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) .

![bo_d7e85t491nqc73eqefm0_265_594_989_516_488_0.jpg](images/fu_algebraic_topology_and_differential_forms_040_bod7e85t491nqc73eqefm02655949895164880.jpg)

![bo_d7e85t491nqc73eqefm0_265_1273_975_443_381_0.jpg](images/fu_algebraic_topology_and_differential_forms_039_bod7e85t491nqc73eqefm026512739754433810.jpg)

Cech 复形为

\[
0 \rightarrow  {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }{C}^{1}\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  0.
\]

因为 \( {U}_{\alpha },{U}_{\alpha \beta } \) 连通,所以

\[
{C}^{0}\left( {\mathcal{U},\mathbb{R}}\right)  = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2}}\right)  \mid  {\omega }_{\alpha }}\right\}   \text{ ⫫ } {U}_{\alpha }\text{ 上常值函数 }\}  = \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R};
\]

\( {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right)  = \left\{  {\left( {{\eta }_{01},{\eta }_{02},{\eta }_{12}}\right)  \mid  {\eta }_{\alpha \beta }}\right\} \) 是 \( {U}_{\alpha \beta } \) 上常值函数 \( \}  = \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \) . 上边缘算子

\[
\delta  : {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right)  \rightarrow  {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) ,\;{\left( \delta \omega \right) }_{\alpha \beta } = {\omega }_{\beta } - {\omega }_{\alpha }.
\]

因此

\[
\ker \delta  = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2}}\right)  \mid  {\omega }_{0} = {\omega }_{1} = {\omega }_{2}}\right\}   \simeq  \mathbb{R}
\]

\[
\operatorname{im}\delta  = {\mathbb{R}}^{2}
\]

\[
{H}^{0}\left( {S}^{1}\right)  = \ker \delta  \simeq  \mathbb{R}
\]

\[
{H}^{1}\left( {S}^{1}\right)  = {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) /\operatorname{im}\delta  \simeq  \mathbb{R}.
\]

例 9.2.( \( {S}^{1} \) 上非平凡的 1-上闭链)若 1-上闭链 \( \eta  = \left( {{\eta }_{01},{\eta }_{02},{\eta }_{12}}\right)  = {\delta \omega } \) ,即

\[
{\eta }_{01} = {\left( \delta \omega \right) }_{01} = {\omega }_{1} - {\omega }_{0}
\]

\[
{\eta }_{02} = {\left( \delta \omega \right) }_{02} = {\omega }_{2} - {\omega }_{0}
\]

\[
{\eta }_{12} = {\left( \delta \omega \right) }_{12} = {\omega }_{2} - {\omega }_{1}
\]

则

\[
{\eta }_{01} - {\eta }_{02} + {\eta }_{12} = 0
\]

所以 \( \eta  = \left( {1,0,0}\right) \) 是 \( {S}^{1} \) 上非平凡的 \( 1 - \) 上闭链. 设 \( {\eta }^{\prime } = \left( {0,1,0}\right) \) . 因为

\[
\eta  + {\eta }^{\prime } = \left( {1,1,0}\right)  = \delta \left( {-1,0,0}\right) ,
\]

所以 \( {\left\lbrack  {\eta }^{\prime }\right\rbrack  }_{\delta } =  - {\left\lbrack  \eta \right\rbrack  }_{\delta } \) . 同理若设 \( {\eta }^{\prime \prime } = \left( {0,0,1}\right) \) ,则 \( {\left\lbrack  {\eta }^{\prime \prime }\right\rbrack  }_{\delta } = {\left\lbrack  \eta \right\rbrack  }_{\delta } \) . 于是

\[
{\left\lbrack  \left( a, b, c\right) \right\rbrack  }_{\delta } = \left( {a - b + c}\right) {\left\lbrack  \eta \right\rbrack  }_{\delta }.
\]

例 9.3. \( \left( {S}^{2}\right) \) 如图， \( \mathcal{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2},{U}_{3}}\right\} \) 构成了 \( {S}^{2} \) 的一个好覆盖,其中 \( {U}_{0} \) 是上半球面,而 \( \left\{  {{U}_{1},{U}_{2},{U}_{3}}\right\} \) 覆盖下半球面.

![bo_d7e85t491nqc73eqefm0_268_324_331_415_422_0.jpg](images/fu_algebraic_topology_and_differential_forms_042_bod7e85t491nqc73eqefm02683243314154220.jpg)

![bo_d7e85t491nqc73eqefm0_268_828_305_504_486_0.jpg](images/fu_algebraic_topology_and_differential_forms_043_bod7e85t491nqc73eqefm02688283055044860.jpg)

![bo_d7e85t491nqc73eqefm0_268_1432_318_560_454_0.jpg](images/fu_algebraic_topology_and_differential_forms_041_bod7e85t491nqc73eqefm026814323185604540.jpg)

Čech 复形是

\( {C}^{0}\left( {\mathcal{U},\mathbb{R}}\right) \; \xrightarrow[]{{\delta }_{0}} \; {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) \; \xrightarrow[]{{\delta }_{1}} \; {C}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \) 0

11 11 11

\( \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \; \mathbb{R} \oplus  \mathbb{R}\;\mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \; \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \)

显然

\[
\ker {\delta }_{0} = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2},{\omega }_{3}}\right)  \mid  {\omega }_{0} = {\omega }_{1} = {\omega }_{2} = {\omega }_{3}}\right\}   \simeq  \mathbb{R}.
\]

所以

\[
{H}^{0}\left( {S}^{2}\right)  = \mathbb{R},\;\text{ im }{\delta }_{0} \simeq  {\mathbb{R}}^{3}.
\]

设

\[
\eta  = \left( {{\eta }_{01},{\eta }_{02},{\eta }_{03},{\eta }_{12},{\eta }_{13},{\eta }_{23}}\right)  \in  {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) ,\;{\delta }_{1}\eta  = 0,
\]

即

\[
{\left( {\delta }_{1}\eta \right) }_{012} = {\eta }_{12} - {\eta }_{02} + {\eta }_{01} = 0 \Rightarrow  {\eta }_{12} = {\eta }_{02} - {\eta }_{01}
\]

\[
{\left( {\delta }_{1}\eta \right) }_{013} = {\eta }_{13} - {\eta }_{03} + {\eta }_{01} = 0 \Rightarrow  {\eta }_{13} = {\eta }_{03} - {\eta }_{01};
\]

\[
{\left( {\delta }_{1}\eta \right) }_{023} = {\eta }_{23} - {\eta }_{03} + {\eta }_{02} = 0 \Rightarrow  {\eta }_{23} = {\eta }_{03} - {\eta }_{02};
\]

\[
{\left( {\delta }_{1}\eta \right) }_{123} = {\eta }_{23} - {\eta }_{13} + {\eta }_{12} = 0 \Rightarrow  {\eta }_{23} = {\eta }_{13} - {\eta }_{12} = {\eta }_{03} - {\eta }_{02}.
\]

这就是说 \( \eta \) 是完全由 \( {\eta }_{01},{\eta }_{02},{\eta }_{03} \) 确定的. 所以

\[
\ker {\delta }_{1} \simeq  {\mathbb{R}}^{3},\;\operatorname{im}{\delta }_{1} \simeq  {\mathbb{R}}^{3}.
\]

因此

\[
{H}^{1}\left( {S}^{2}\right)  = \ker {\delta }_{1}/\operatorname{im}{\delta }_{0} = 0
\]

\[
{H}^{2}\left( {S}^{2}\right)  = {\mathbb{R}}^{4}/\operatorname{im}{\delta }_{1} = \mathbb{R}.
\]

显式同构的一个例子: \( {H}_{dR}^{2}\left( M\right)  \simeq  {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \)

这个例子在几何中是极端重要的. 设 \( \left\lbrack  \omega \right\rbrack   \in  {H}^{2}\left( M\right) \) . 记 \( {\omega }_{\alpha } = {\left. \omega \right| }_{{U}_{\alpha }} \) . 因为 \( d{\omega }_{\alpha } = 0 \) 且 \( {U}_{\alpha } \) 可缩,由 Poincaré 引理知存在 \( {\xi }_{\alpha } \in  {\Omega }^{1}\left( {U}_{\alpha }\right) \) 使得

\[
d{\xi }_{\alpha } = {\omega }_{\alpha }.
\]

所以

\[
{\left\lbrack  \omega \right\rbrack  }_{D} = {\left\lbrack  \omega  - D\xi \right\rbrack  }_{D} = {\left\lbrack  -\delta \xi \right\rbrack  }_{D}.
\]

因为 \( {U}_{\alpha \beta } \) 可缩且

\[
d\left( {{\left. {\xi }_{\alpha }\right| }_{{U}_{\alpha \beta }} - {\left. {\xi }_{\beta }\right| }_{{U}_{\alpha \beta }}}\right)  = {\left. {\omega }_{\alpha }\right| }_{{U}_{\alpha \beta }} - {\left. {\omega }_{\beta }\right| }_{{U}_{\alpha \beta }} = {\left. \omega \right| }_{{U}_{\alpha \beta }} - {\left. \omega \right| }_{{U}_{\alpha \beta }} = 0,
\]

所以由 Poincaré 引理知存在 \( {\eta }_{\alpha \beta } \in  {\Omega }^{0}\left( {U}_{\alpha \beta }\right) \) 使得

\[
d{\eta }_{\alpha \beta } = {\left. {\xi }_{\alpha }\right| }_{{U}_{\alpha \beta }} - {\left. {\xi }_{\beta }\right| }_{{U}_{\alpha \beta }}.
\]

因为 \( {D}^{\prime \prime } = {\left( -1\right) }^{p}d, p = 1 \) ,所以

\[
{\left\lbrack  \omega \right\rbrack  }_{D} = {\left\lbrack  -\delta \xi \right\rbrack  }_{D} = {\left\lbrack  -\delta \xi  + D\eta \right\rbrack  }_{D} = {\left\lbrack  \delta \eta \right\rbrack  }_{D}.
\]

令 \( c = {\delta \eta } \in  {C}^{2}\left( {\mathcal{U},{\Omega }^{0}}\right) \) ,即

\[
{c}_{\alpha \beta \gamma } = {\left( \delta \eta \right) }_{\alpha \beta \gamma } = {\eta }_{\beta \gamma } - {\eta }_{\alpha \gamma } + {\eta }_{\alpha \beta }.
\]

则

\[
d{c}_{\alpha \beta \gamma } = d{\eta }_{\beta \gamma } - d{\eta }_{\alpha \gamma } + d{\eta }_{\alpha \beta } = {\xi }_{\beta } - {\xi }_{\gamma } - {\xi }_{\alpha } + {\xi }_{\gamma } + {\xi }_{\alpha } - {\xi }_{\beta } = 0,
\]

即 \( {c}_{\alpha \beta \gamma } \) 是 \( {U}_{\alpha \beta \gamma } \) 上的常值函数. 所以

\[
c = \left\{  {c}_{\alpha \beta \gamma }\right\}   \in  {C}^{2}\left( {\mathcal{U},\mathbb{R}}\right) .
\]

又因为

\[
{\delta c} = {\delta }^{2}\eta  = 0,
\]

所以

\[
c \in  {H}^{2}\left( {\mathcal{U},\mathbb{R}}\right) \text{ . }
\]

于是

\[
{\left\lbrack  \omega \right\rbrack  }_{d} \mapsto  {\left\lbrack  \omega \right\rbrack  }_{D} = {\left\lbrack  \delta \eta \right\rbrack  }_{D} \mapsto  {\left\lbrack  c\right\rbrack  }_{\delta }.
\]

\[
{\Omega }^{2}\left( M\right) \overset{r}{ \rightarrow  }{C}^{0}\left( {\mathcal{U},{\Omega }^{2}}\right)  \oplus  {C}^{1}\left( {\mathcal{U},{\Omega }^{1}}\right)  \oplus  {C}^{2}\left( {\mathcal{U},{\Omega }^{0}}\right) \;\overset{i}{ \leftarrow  }\;{C}^{2}\left( {\mathcal{U},\mathbb{R}}\right)
\]

\[
{D}^{\prime \prime } = d
\]

\[
\exists {\xi }_{\alpha }\;\overset{\delta }{ \rightarrow  }{\left( \delta \xi \right) }_{\alpha \beta }\;\overset{\delta }{ \rightarrow  }\;0
\]

\[
{D}^{\prime \prime } =  - d\left. {\;{D}^{\prime \prime } = d}\right\rbrack
\]

\[
{c}_{\alpha \beta \gamma }\overset{\delta }{ \rightarrow  }0
\]

w

\[
\begin{matrix} \left\{  {\omega }_{\alpha }\right\}  & \left\{  {-{\left( \delta \xi \right) }_{\alpha \beta }}\right\}  & \left\{  {\left( \delta \eta \right) }_{\alpha \beta \gamma }\right\}  \\   & \overset{\text{ ।। }}{ = } & \overset{\text{ ।। }}{ - }{\omega }_{\alpha } - {\xi }_{\beta } \\   & & \\   & & {\omega }_{\alpha \beta } - {\xi }_{\beta } \\   & & {\omega }_{\alpha \beta } + {\eta }_{\alpha \beta } \\   & & {\omega }_{\alpha \beta \gamma } - {\eta }_{\alpha \beta \gamma } + {\eta }_{\alpha \beta \gamma } \\   & & \\   & & i{\left( {c}_{\alpha \beta \gamma }\right) }^{ \intercal  } \end{matrix}
\]

\[
{\left\lbrack  \omega \right\rbrack  }_{d}\; \mapsto  \;{\left\lbrack  \left\{  {\omega }_{\alpha }\right\}  \right\rbrack  }_{D} = {\left\lbrack  \left\{  -{\left( \delta \xi \right) }_{\alpha \beta }\right\}  \right\rbrack  }_{D} = {\left\lbrack  \left\{  {\left( \delta \eta \right) }_{\alpha \beta \gamma }\right\}  \right\rbrack  }_{D}\; \mapsto  \;{\left\lbrack  c\right\rbrack  }_{\delta }
\]

反之,设 \( c \in  {C}^{2}\left( {\mathcal{U},\mathbb{R}}\right)  \subset  {C}^{2}\left( {\mathcal{U},{\Omega }^{0}}\right) ,{\delta c} = 0 \) . 所以 \( {Dc} = 0 \) . 我们要用同伦算子 \( K : {C}^{p}\left( {\mathcal{U},{\Omega }^{q}}\right)  \rightarrow  {C}^{p - 1}\left( {\mathcal{U},{\Omega }^{q}}\right) \) ,它满足 \( {\delta K} + {K\delta } = 1 \) . 因为

\[
{\delta Kc} = c - {K\delta c} = c,
\]

所以

\[
c - {DKc} =  - {D}^{\prime \prime }{Kc}
\]

于是

\[
{\left\lbrack  c\right\rbrack  }_{D} = {\left\lbrack  -{D}^{\prime \prime }Kc\right\rbrack  }_{D}. \tag{25}
\]

计算:

\[
- {D}^{\prime \prime }{Kc} + {DK}{D}^{\prime \prime }{Kc}
\]

\[
=  - {D}^{\prime \prime }{Kc} + {\delta K}{D}^{\prime \prime }{Kc} + {\left( {D}^{\prime \prime }K\right) }^{2}c\;\text{ 因为 }D = \delta  + {D}^{\prime \prime }
\]

\[
=  - {K\delta }{D}^{\prime \prime }{Kc} + {\left( {D}^{\prime \prime }K\right) }^{2}c\;\text{ 因为 }{\delta K} = 1 - {K\delta }
\]

\[
= K{D}^{\prime \prime }{\delta Kc} + {\left( {D}^{\prime \prime }K\right) }^{2}c\;\text{ 因为 }\delta {D}^{\prime \prime } =  - {D}^{\prime \prime }\delta
\]

\[
= K{D}^{\prime \prime }c - K{D}^{\prime \prime }{K\delta c} + {\left( {D}^{\prime \prime }K\right) }^{2}c\;\text{ 因为 }{\delta K} = 1 - {K\delta }
\]

\[
= {\left( {D}^{\prime \prime }K\right) }^{2}c\;\text{ 因为 }{D}^{\prime \prime }c = 0,{\delta c} = 0.
\]

所以

\[
{\left\lbrack  -{D}^{\prime \prime }Kc\right\rbrack  }_{D} = {\left\lbrack  {\left( {D}^{\prime \prime }K\right) }^{2}c\right\rbrack  }_{D}. \tag{26}
\]

注意 \( {\left( {D}^{\prime \prime }K\right) }^{2}c \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{2}}\right) \) . 因为

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{2}c
\]

\[
=  - {D}^{\prime \prime }{\delta K}{D}^{\prime \prime }{Kc}
\]

\[
=  - {D}^{\prime \prime }\left( {1 - {K\delta }}\right) {D}^{\prime \prime }{Kc}
\]

\[
= {D}^{\prime \prime }{K\delta }{D}^{\prime \prime }{Kc} \tag{27}
\]

\[
=  - {D}^{\prime \prime }K{D}^{\prime \prime }{\delta Kc}
\]

\[
=  - {D}^{\prime \prime }K{D}^{\prime \prime }\left( {1 - {K\delta }}\right) c
\]

\[
= 0\text{ , }
\]

所以 \( {\left( {D}^{\prime \prime }K\right) }^{2}c \) 定义了 \( M \) 上一个整体 2-形式 \( \omega \) . 显然它是闭的. 于是由(25)，(26)可得

\[
{\left\lbrack  c\right\rbrack  }_{\delta } \mapsto  {\left\lbrack  c\right\rbrack  }_{D} = {\left\lbrack  -{D}^{\prime \prime }Kc\right\rbrack  }_{D} = {\left\lbrack  {\left( {D}^{\prime \prime }K\right) }^{2}c\right\rbrack  }_{D} \mapsto  {\left\lbrack  \omega \right\rbrack  }_{d}.
\]

补充练习 1 . 写出 (27) 中每个等式成立的理由.

\( \omega \) 的显式构造. 利用 \( K \) 的定义有

\[
{\left( Kc\right) }_{\beta \alpha } = \sum {\rho }_{\gamma }{c}_{\gamma \beta \alpha }.
\]

所以

\[
{\left( {D}^{\prime \prime }Kc\right) }_{\beta \alpha } = {D}^{\prime \prime }{\left( Kc\right) }_{\beta \alpha } =  - d\left( {\sum {\rho }_{\gamma }{c}_{\gamma \beta \alpha }}\right)  =  - \sum d{\rho }_{\gamma } \cdot  {c}_{\gamma \beta \alpha } \in  {C}^{1}\left( {U}_{\alpha \beta }\right) .
\]

再利用 \( K \) 的定义有

\[
{\left( K{D}^{\prime \prime }Kc\right) }_{\alpha } = \sum {\rho }_{\beta }{\left( {D}^{\prime \prime }Kc\right) }_{\beta \alpha } =  - \sum {\rho }_{\beta }\left( {d{\rho }_{\gamma } \cdot  {c}_{\gamma \beta \alpha }}\right) .
\]

所以

\[
{\left( {\left( {D}^{\prime \prime }K\right) }^{2}c\right) }_{\alpha } = \sum {c}_{\gamma \beta \alpha }d{\rho }_{\gamma } \land  d{\rho }_{\beta } \in  {\Omega }^{2}\left( {U}_{\alpha }\right) .
\]

补充练习 2. 验证限制在 \( {U}_{\alpha \beta } \) 上

\[
{\left( {\left( {D}^{\prime \prime }K\right) }^{2}c\right) }_{\alpha } = {\left( {\left( {D}^{\prime \prime }K\right) }^{2}c\right) }_{\beta }.
\]

所以

\[
{\left. \omega \right| }_{{U}_{\alpha }} = \mathop{\sum }\limits_{{\beta ,\gamma }}{c}_{\beta \gamma \alpha }d{\rho }_{\beta } \land  d{\rho }_{\gamma }.
\]

显式同构

更一般地有以下

命题 9.8. (de Rham 与 Čech 间的显式同构) 若 \( \eta  \in  {C}^{n}\left( {\mathcal{U},\mathbb{R}}\right) ,{\delta \eta } = 0 \) ,则 \( \eta \) 对应的整体定义的闭 \( n \) -形式为

\[
{\left( -1\right) }^{n}{\left( {D}^{\prime \prime }K\right) }^{n}\eta
\]

证. 需以下引理, 它的证明放在命题的证明之后.

引理 9.6. 对 \( i \geq  1 \) ,

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} = {\left( {D}^{\prime \prime }K\right) }^{i}\delta  - {\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime }.
\]

首先，与等式 (25) 的证明相同有

\[
{\left\lbrack  \eta \right\rbrack  }_{\delta } = {\left\lbrack  \eta \right\rbrack  }_{D} = {\left\lbrack  \eta  - DK\eta \right\rbrack  }_{D} = {\left\lbrack  \eta  - \delta K\eta  - {D}^{\prime \prime }K\eta \right\rbrack  }_{D}
\]

\[
= {\left\lbrack  K\delta \eta  - {D}^{\prime \prime }K\eta \right\rbrack  }_{D} = {\left\lbrack  -{D}^{\prime \prime }K\eta \right\rbrack  }_{D}.
\]

再对 \( {\left\lbrack  -{D}^{\prime \prime }K\eta \right\rbrack  }_{D} \) 施以操作,

\[
{\left\lbrack  -{D}^{\prime \prime }K\eta \right\rbrack  }_{D}
\]

\[
= {\left\lbrack  -{D}^{\prime \prime }K\eta  + DK{D}^{\prime \prime }K\eta \right\rbrack  }_{D}
\]

\[
= {\left\lbrack  -{D}^{\prime \prime }K\eta  + \delta K{D}^{\prime \prime }K\eta  + {\left( {D}^{\prime \prime }K\right) }^{2}\eta \right\rbrack  }_{D}\;\text{ 因为 }D = \delta  + {D}^{\prime \prime }
\]

\[
= {\left\lbrack  -K\delta {D}^{\prime \prime }K\eta  + {\left( {D}^{\prime \prime }K\right) }^{2}\eta \right\rbrack  }_{D}\;\text{ 因为 }{\delta K} + {K\delta } = 1
\]

\[
= {\left\lbrack  -K{D}^{\prime \prime }K\delta \eta  + K{D}^{\prime \prime }\eta  + {\left( {D}^{\prime \prime }K\right) }^{2}\eta \right\rbrack  }_{D}\;\text{ 根据引理 9.6 }
\]

\[
= {\left\lbrack  {\left( {D}^{\prime \prime }K\right) }^{2}\eta \right\rbrack  }_{D}\;\text{ 因为 }{\delta \eta } = 0 = {D}^{\prime \prime }\eta .
\]

由引理 9.6 可如此反复操作，最后得到

\[
{\left\lbrack  \eta \right\rbrack  }_{D} = {\left\lbrack  \omega \right\rbrack  }_{D},\;\omega  = {\left( -1\right) }^{n}{\left( {D}^{\prime \prime }K\right) }^{n}\eta  \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{n}}\right) .
\]

根据引理 9.6 又有

\[
{\delta \omega } = {\left( -1\right) }^{n}\delta {\left( {D}^{\prime \prime }K\right) }^{n}\eta  = {\left( -1\right) }^{n}{\left( {D}^{\prime \prime }K\right) }^{n}{\delta \eta } - {\left( -1\right) }^{n}{\left( {D}^{\prime \prime }K\right) }^{n - 1}{D}^{\prime \prime }\eta  = 0.
\]

显然 \( {d\omega } = 0 \) . 所以 \( \omega \) 确实是 \( M \) 上整体定义的闭 \( n \) -形式.

引理 9.6 的证明. 因为

\[
\delta {D}^{\prime \prime } =  - {D}^{\prime \prime }\delta ,\;{\delta K} + {K\delta } = 1,
\]

所以

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} = \delta \left( {{D}^{\prime \prime }K}\right) {\left( {D}^{\prime \prime }K\right) }^{i - 1}
\]

\[
=  - {D}^{\prime \prime }{\delta K}{\left( {D}^{\prime \prime }K\right) }^{i - 1}
\]

\[
=  - {D}^{\prime \prime }{\left( {D}^{\prime \prime }K\right) }^{i - 1} + \left( {{D}^{\prime \prime }K}\right) \delta {\left( {D}^{\prime \prime }K\right) }^{i - 1}.
\]

当 \( i = 1 \) 时,已完成引理的证明.

当 \( i > 1 \) 时，由于右边第一项等于零，可继续上述操作直到

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} = {\left( {D}^{\prime \prime }K\right) }^{i - 1}\delta \left( {{D}^{\prime \prime }K}\right)
\]

于是,应用 \( i = 1 \) 的情形得到

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} =  - {\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime } + {\left( {D}^{\prime \prime }K\right) }^{i}\delta .
\]

因为 \( {\Omega }^{ * }\left( M\right) \) 与 \( {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right) \) 有相同的上同调,按上同调理论这两个复形是链同伦的, 即存在一个链映射

(9.4)

\[
f : {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)  \rightarrow  {\Omega }^{ * }\left( M\right)
\]

使得

(a) \( f \circ  r = \mathrm{{id}} \) ; 且

(b) \( r \circ  f \) 链同伦于 id.

我们先构造链映射,再构造链同伦. 给定一个 \( n \) -上链:

\[
\alpha  = \mathop{\sum }\limits_{{i = 0}}^{n}{\alpha }_{i},\;{\alpha }_{i} \in  {C}^{i}\left( {\mathcal{U},{\Omega }^{n - i}}\right) .
\]

对每个 \( {\alpha }_{i} \) 定义

\[
f\left( {\alpha }_{i}\right)  = \left( {1 - {K\delta }}\right) {\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} \in  {C}^{0}\left( {\mathcal{U},{\Omega }^{n}}\right) .
\]

因为 \( 1 - {K\delta } = {\delta K} \) ,所以 \( {\delta f}\left( {\alpha }_{i}\right)  = 0 \) ,即 \( f\left( {\alpha }_{i}\right) \) 是整体定义的 \( n \) -形式.

引理 1. \( f\left( \alpha \right)  = \mathop{\sum }\limits_{{i = 0}}^{n}f\left( {\alpha }_{i}\right) \) 是整体定义的 \( n \) -形式.

引理 2. 记 \( {D\alpha } = \beta  = \mathop{\sum }\limits_{{i = 0}}^{{n + 1}}{\beta }_{i} \) . 则

\[
f\left( \alpha \right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}K{\left( -{D}^{\prime \prime }K\right) }^{i - 1}{\beta }_{i}.
\]

证. 应用引理 9.6,当 \( i \geq  1 \) 时有

\[
f\left( {\alpha }_{i}\right)  = {\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - {\left( -1\right) }^{i}{K\delta }{\left( {D}^{\prime \prime }K\right) }^{i}{\alpha }_{i}
\]

\[
= {\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - {\left( -1\right) }^{i}K{\left( {D}^{\prime \prime }K\right) }^{i}\delta {\alpha }_{i} + {\left( -1\right) }^{i}K{\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime }{\alpha }_{i}
\]

\[
= {\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - K{\left( -{D}^{\prime \prime }K\right) }^{i}\delta {\alpha }_{i} - K{\left( -{D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime }{\alpha }_{i}.
\]

注意到 \( f\left( {\alpha }_{0}\right)  = {\alpha }_{0} - {K\delta }{\alpha }_{0} \) ,所以

\[
f\left( \alpha \right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}K{\left( -{D}^{\prime \prime }K\right) }^{i - 1}\left( {\delta {\alpha }_{i - 1} + {D}^{\prime \prime }{\alpha }_{i}}\right) \;\text{ 因为 }{\alpha }_{n + 1} = 0
\]

\[
= \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}K{\left( -{D}^{\prime \prime }K\right) }^{i - 1}{\beta }_{i}\;\text{ 因为 }{\beta }_{i} = \delta {\alpha }_{i - 1} + {D}^{\prime \prime }{\alpha }_{i}.
\]

引理 3. \( f \) 是链映射且 \( f \circ  r = \mathrm{{id}} \) .

证. 因为 \( {D\beta } = 0 \) ,所以由引理 2 可得

\[
f\left( {D\alpha }\right)  = f\left( \beta \right)  = \mathop{\sum }\limits_{{i = 0}}^{{n + 1}}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\beta }_{i}.
\]

又由引理 2,因为 \( {D}^{\prime \prime }{\alpha }_{0} = {\beta }_{0} \) ,所以

\[
{df}\left( \alpha \right)  = {D}^{\prime \prime }f\left( \alpha \right)  = {D}^{\prime \prime }{\alpha }_{0} + \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\beta }_{i}
\]

\[
= \mathop{\sum }\limits_{{i = 0}}^{{n + 1}}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\beta }_{i}
\]

这就证明了 \( f \) 是链映射.

由 \( f \) 的定义知 \( f \circ  r = \mathrm{{id}} \) 显然成立.

引理 4. 满足 \( 1 - r \circ  f = {DL} + {LD} \) 的同伦算子

\[
L : {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)  \rightarrow  {C}^{ * }\left( {\mathcal{U},{\Omega }^{ * }}\right)
\]

定义为对 \( n \) -上链 \( \alpha  = \mathop{\sum }\limits_{{i = 0}}^{n}{\alpha }_{i} \) ,

\( {L\alpha } = \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}{\left( L\alpha \right) }_{p},\; \) 其中

\[
{\left( L\alpha \right) }_{p} = \mathop{\sum }\limits_{{i = p + 1}}^{n}K{\left( -{D}^{\prime \prime }K\right) }^{i - \left( {p + 1}\right) }{\alpha }_{i} \in  {C}^{p}\left( {\mathcal{U},{\Omega }^{n - 1 - p}}\right) .
\]

证. 略.

命题 9.5. (Collating 公式) 引理 1, 2, 3, 4 组成了 collating 公式.

练习 9.10. 实射影平面 \( \mathbb{R}{P}^{2} \) 可按左下图所示粘合圆盘的边得到. 求 \( \mathbb{R}{P}^{2} \) 的一个好覆盖, 并从覆盖的组合计算它的 de Rham 上同调. 右下图给出了一个好覆盖的 nerve.

![bo_d7e85t491nqc73eqefm0_284_637_368_1039_513_0.jpg](images/fu_algebraic_topology_and_differential_forms_045_bod7e85t491nqc73eqefm028463736810395130.jpg)

练习 9.11. 下图是环面 \( {T}^{2} \) 上一个好覆盖 \( \mathcal{U} \) 的 nerve,箭头表明了顶点的排序. 求在 \( {C}^{1}\left( {\mathcal{U},\mathbb{R}}\right) \) 中一个非平凡的 1-上闭链.

![bo_d7e85t491nqc73eqefm0_284_581_1194_1166_543_0.jpg](images/fu_algebraic_topology_and_differential_forms_044_bod7e85t491nqc73eqefm0284581119411665430.jpg)

作业:

1. 补充练习 1.

2. 补充练习 2.

3. 练习 9.10.

4. 练习 9.11.

代数拓扑与微分形式
