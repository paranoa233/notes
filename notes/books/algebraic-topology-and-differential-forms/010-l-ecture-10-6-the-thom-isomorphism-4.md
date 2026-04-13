#### 第10讲 The Thom Isomorphism (4)

§6 The Thom Isomorphism (4)

10. 平面丛的 Thom 类的显式表示

设 \( M \) 是 \( n \) 维流形, \( \pi  : E \rightarrow  M \) 是 \( M \) 上秩 \( k \) 定向向量丛. 设 \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( E \) 的定向平凡化, \( {g}_{\alpha \beta } \) 是其转移函数. 设 \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) 是从属于 \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) 的单位分解.

这次课讲当向量丛的秩等于 2 时,如何利用 \( \left\{  {\rho }_{\alpha }\right\}  ,\left\{  {g}_{\alpha \beta }\right\} \) 显式构造 \( E \) 的 Thom 类,即构造 \( \Phi  \in  {H}_{cv}^{2}\left( E\right) \) 满足

\[
{\int }_{{E}_{x}}\Phi { \mid  }_{{E}_{x}} = 1
\]

高秩的情形是类似的但更复杂, 它将在 (11.11) 与 (12.3) 处理. 对构造的最好理解是把 \( {H}^{n - 1}\left( {S}^{n - 1}\right) \) 生成元变为 \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) 生成元的过程推广到向量丛的情形. 所以先设法理解 \( {\mathbb{R}}^{n} \) 的情形.

- 整体角形式

- 平面丛欧拉类的显式表示

- 平面丛 Thom 类的显式表示

整体角形式在定向流形 \( M \) 上一个最高次微分形式称为正的若它在 \( M \) 的定向类中. 为了方便规定 \( {\mathbb{R}}^{n} \) 中单位球面 \( {S}^{n - 1} \) 的标准定向如下: 若 \( \left\lbrack  \sigma \right\rbrack \) 是 \( {H}^{n - 1}\left( {S}^{n - 1}\right) \) 的生成元且 \( p : {\mathbb{R}}^{n} - \{ 0\}  \rightarrow  {S}^{n - 1} \) 是形变收缩,则 \( \sigma \) 在 \( {S}^{n - 1} \) 上是正的当且仅当 \( {dr} \land  {p}^{ * }\sigma \) 在 \( {\mathbb{R}}^{n} - \{ 0\} \) 上是正的,即它在 \( {\mathbb{R}}^{n} - 0 \) 的标准定向类中.

其实在练习 4.3.1 中已在 \( {S}^{n - 1} \) 上定义了一个正的 \( \left( {n - 1}\right) \) -形式. 在 \( {\mathbb{R}}^{n} - \{ 0\} \) 上定义 \( \left( {n - 1}\right) \) -形式

\[
\omega  = \frac{1}{r}\mathop{\sum }\limits_{{i = 1}}^{n}{\left( -1\right) }^{i - 1}{x}_{i}d{x}_{1} \land  \cdots  \land  \widehat{d{x}_{i}} \land  \cdots  \land  d{x}_{n}.
\]

设 \( \sigma  = {\left. \omega \right| }_{{S}^{n - 1}} \) . 则 \( \sigma \) 是 \( {S}^{n - 1} \) 上正的形式,因为

\[
{dr} \land  {p}^{ * }\sigma  = {dr} \land  \frac{\omega }{{r}^{n - 1}} = \frac{1}{{r}^{n - 1}}d{x}_{1} \land  \cdots  \land  d{x}_{n}.
\]

注意 \( {p}^{ * }\left( {\left. d{x}_{i}\right| }_{{S}^{n - 1}}\right)  = d\left( {{x}_{i}/r}\right) \) .

## 练习 6.32.

(a) 证明若 \( \theta \) 是 \( {\mathbb{R}}^{2} \) 上逆时针方向的标准角函数，则 \( {d\theta } \) 限制在 \( {S}^{1} \) 上是正的.

(b) 证明若 \( \phi \) 与 \( \theta \) 如左下图是 \( {\mathbb{R}}^{3} \) 上球面坐标,则 \( {d\phi } \land  {d\theta } \) 在 \( {S}^{2} \) 上是正的; 若 \( \phi \) 与 \( \theta \) 如右下图是 \( {\mathbb{R}}^{3} \) 上球面坐标,则 \( {d\theta } \land  {d\phi } \) 在 \( {S}^{2} \) 上是正的. 证. (a) 设 \( x, y \) 是 \( {\mathbb{R}}^{2} \) 上标准坐标, \( r,\theta \) 是 \( {\mathbb{R}}^{2} - 0 \) 上极坐标,其中 \( \theta  \in  \left\lbrack  {0,{2\pi }}\right\rbrack \) . 则

\[
x = r\cos \theta
\]

\[
y = r\sin \theta
\]

\[
{dx} = \cos {\theta dr} - r\sin {\theta d\theta }
\]

\[
{dy} = \sin {\theta dr} + r\cos {\theta d\theta }
\]

\[
{dx} \land  {dy} = {rdr} \land  {d\theta }
\]

![bo_d7e85t491nqc73eqefm0_209_588_825_555_552_0.jpg](images/fu_algebraic_topology_and_differential_forms_026_bod7e85t491nqc73eqefm02095888255555520.jpg)

![bo_d7e85t491nqc73eqefm0_209_1229_814_567_555_0.jpg](images/fu_algebraic_topology_and_differential_forms_025_bod7e85t491nqc73eqefm020912298145675550.jpg)

所以 \( {d\theta } \) 在 \( {S}^{1} \) 上是正的.

(b) 设 \( x, y, z \) 是 \( {\mathbb{R}}^{3} \) 上标准坐标. 如左图,设 \( r,\phi ,\theta \) 是 \( {\mathbb{R}}^{3} - 0 \) 上球坐标,其中 \( \phi  \in  \left\lbrack  {0,\pi }\right\rbrack  ,\theta  \in  \left\lbrack  {0,{2\pi }}\right\rbrack \) . 则

\[
x = r\sin \phi \cos \theta
\]

\[
y = r\sin \phi \sin \theta
\]

\[
z = r\cos \phi
\]

\[
{dx} \land  {dy} \land  {dz} = {r}^{2}\sin {\phi dr} \land  {d\phi } \land  {d\theta }
\]

所以 \( {d\phi } \land  {d\theta } \) 在 \( {S}^{2} \) 上是正的. 如果 \( {\mathbb{R}}^{3} - 0 \) 上球坐标如右图为 \( r,\theta ,\phi \) ,其中 \( \phi  \in  \left\lbrack  {-\pi /2,\pi /2}\right\rbrack  ,\theta  \in  \left\lbrack  {0,{2\pi }}\right\rbrack \) ,则 \( {d\theta } \land  {d\phi } \) 在 \( {S}^{2} \) 上是正的,因为

\[
{dx} \land  {dy} \land  {dz} = {r}^{2}\cos {\phi dr} \land  {d\theta } \land  {d\phi }.
\]

设 \( \sigma \) 是 \( {S}^{k - 1} \) 上正形式且 \( {\int }_{{S}^{k - 1}}\sigma  = 1 \) . 则 \( \psi  = {p}^{ * }\sigma \) 称为 \( {\mathbb{R}}^{k} - 0 \) 上角形式. 注意 \( \left\lbrack  \sigma \right\rbrack   \in  {H}^{k - 1}\left( {S}^{k - 1}\right) \) 与 \( \left\lbrack  \psi \right\rbrack   \in  {H}^{k - 1}\left( {{\mathbb{R}}^{k} - 0}\right) \) 是生成元.

设 \( \rho \left( r\right) \) 是 \( r \geq  0 \) 的函数,定义如下图.

![bo_d7e85t491nqc73eqefm0_211_277_565_804_424_0.jpg](images/fu_algebraic_topology_and_differential_forms_028_bod7e85t491nqc73eqefm02112775658044240.jpg)

![bo_d7e85t491nqc73eqefm0_211_1240_566_804_423_0.jpg](images/fu_algebraic_topology_and_differential_forms_027_bod7e85t491nqc73eqefm021112405668044230.jpg)

则

\[
{\int }_{0}^{\infty }{\rho }^{\prime }\left( r\right) {dr} = \rho \left( \infty \right)  - \rho \left( 0\right)  = 1
\]

所以

\[
{d\rho } = {\rho }^{\prime }\left( r\right) {dr}
\]

是 \( {\mathbb{R}}^{1} \) 上一个 bump 形式,它的积分等于 1 .

虽然 \( \psi \) 在原点没有定义,但因为 \( {d\rho } \) 在 \( r = 0 \) 附近为零,所以可认为 \( {d\rho } \land  \psi \) 经零延拓定义在整个 \( {\mathbb{R}}^{k} \) 上. 显然 \( {d\rho } \land  \psi \) 具有紧支集且是闭的,所以

\[
\left\lbrack  {{d\rho } \land  \psi }\right\rbrack   \in  {H}_{c}^{k}\left( {\mathbb{R}}^{k}\right) .
\]

计算:

\[
{\int }_{{\mathbb{R}}^{k}}{d\rho } \land  \psi  = {\int }_{{B}_{R}\left( 0\right)  - {B}_{\epsilon }\left( 0\right) }{d\rho } \land  \psi \;\text{ 对充分大的 }R\text{ 与充分小的 }\epsilon  > 0
\]

\[
= {\int }_{{B}_{R}\left( 0\right)  - {B}_{\epsilon }\left( 0\right) }d\left( {\rho \psi }\right) \;\text{ 因为 }{d\psi } = 0
\]

\[
= {\int }_{{S}^{k - 1}\left( R\right) }\rho \left( R\right) {i}_{R}^{ * }\psi  - {\int }_{{S}^{k - 1}\left( \epsilon \right) }\rho \left( \epsilon \right) {i}_{\epsilon }^{ * }\psi \;\text{ 根: }
\]

\[
= {\int }_{{S}^{k - 1}\left( \epsilon \right) }{i}_{\epsilon }^{ * }{p}^{ * }\sigma \;\text{ 因为 }\rho \left( R\right)  = 0,\rho \left( \epsilon \right)  =  - 1,\psi  = {p}^{ * }\sigma \tag{12}
\]

\[
= {\int }_{{S}^{k - 1}\left( \epsilon \right) }{\left( p \circ  {i}_{\epsilon }\right) }^{ * }\sigma
\]

\[
= 1\text{ . }
\]

这就是说, \( \left\lbrack  {{d\rho } \land  \psi }\right\rbrack \) 是 \( {H}_{c}^{k}\left( {\mathbb{R}}^{k}\right) \) 的生成元. 现考虑 \( M \) 上秩 \( k \) 定向向量丛 \( \pi  : E \rightarrow  M \) . 记 \( {E}^{0} = E - s\left( E\right) \) ,其中 \( s \) 是零截面. 设 \( \langle \) , \( \rangle {\text{ 是 }E} \) 上一个度量. 对每条纤维 \( {E}_{x} \) 的每个向量 \( v \) ,定义

\[
{r}^{2}\left( v\right)  = \langle v, v\rangle .
\]

所以 \( r \) 在 \( E \) 上是有意义的,上述的 \( \rho \left( r\right) \) 可视为定义在 \( E \) 上的函数.

定义. \( {E}^{0} \) 的一个 \( \left( {k - 1}\right) \) -形式 \( \psi \) 称为整体角形式若 \( \psi \) 限制在每条纤维 \( {E}_{x}^{0} \simeq  {\mathbb{R}}^{k} - 0 \) 上是角形式并且 \( {d\psi } \) 能自然延拓成 \( E \) 的一个 \( k \) -形式.

若在 \( {E}^{0} \) 上存在整体角形式 \( \psi \) ,则 \( E \) 的 Thom 类是

\[
\Phi  = {d\rho } \land  \psi  + {\rho d\psi }
\]

这是因为 \( \left\lbrack  \Phi \right\rbrack   \in  {H}_{cv}^{k}\left( E\right) \) 并且由计算 (12) 知

\[
{\int }_{{E}_{x}}{\left. \Phi \right| }_{{E}_{x}} = {\int }_{{E}_{x}}{\left. \left( d\rho  \land  \psi \right) \right| }_{{E}_{x}} = 1.
\]

以下假定 \( E \) 是定向平面丛,即它的秩是 2. 设 \( \{ \left( {{U}_{\alpha },{\psi }_{\alpha }}\right) {\} }_{\alpha  \in  I} \) 是 \( M \) 的一个坐标图册, \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 是 \( E \) 的定向平凡化.

\[
{\left. E\right| }_{{U}_{\alpha }}\overset{{\phi }_{\alpha }}{ \rightarrow  }{U}_{\alpha } \times  {\mathbb{R}}^{2}\xrightarrow[]{\left( {\psi }_{\alpha },\mathrm{{id}}\right) }{\mathbb{R}}^{n} \times  {\mathbb{R}}^{2}.
\]

设 \( {x}_{1}^{\alpha },\ldots ,{x}_{n}^{\alpha } \) 是 \( {U}_{\alpha } \) 上坐标函数,即 \( {x}_{i}^{\alpha } = {x}_{i} \circ  {\psi }_{\alpha } \) .

相应于 \( {\mathbb{R}}^{2} - 0 \) 上极坐标 \( r,\theta \) ,在 \( {\left. {E}^{0}\right| }_{{U}_{\alpha }} \) 的每条纤维上定义了极坐标 \( {r}_{\alpha } = r \circ  {\phi }_{\alpha } \) 与 \( {\theta }_{\alpha } = \theta  \circ  {\phi }_{\alpha } \) . 于是在 \( {\left. {E}^{0}\right| }_{{U}_{\alpha }} \) 上有坐标函数 \( {\pi }^{ * }{x}_{1}^{\alpha },\cdots ,{\pi }^{ * }{x}_{n}^{\alpha },{r}_{\alpha },{\theta }_{\alpha } \) . 假定定向平凡化 \( \{ {\phi }_{\alpha }{\} }_{\alpha  \in  I} \) 对 \( E \) 上给定的度量是保内积的,即它的转移函数已约化到 \( {SO}\left( 2\right) \) . 则 \( {r}_{\alpha } = {r}_{\beta } \) 成立, \( {\left\{  {r}_{\alpha }\right\}  }_{\alpha  \in  I} \) 给出了 \( E \) 上一个函数,这就是前面已定义的函数 \( r \) .

但是 \( {\theta }_{\alpha },{\theta }_{\beta } \) 在 \( {U}_{\alpha \beta } \) 上相差一个旋转. 由于 \( E \) 的定向性,在每条纤维上说逆时针旋转是有意义的. 这使我们能定义唯一的(在相差 \( {2\pi } \) 整数倍的意义下) \( {\varphi }_{\alpha \beta } \) 作为从 \( \alpha \) -坐标系逆时针旋转到 \( \beta \) -坐标系时旋转的角度:

(6.34)

\[
{\theta }_{\beta } = {\theta }_{\alpha } + {\pi }^{ * }{\varphi }_{\alpha \beta },\;{\varphi }_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  \mathbb{R}.
\]

虽然在 \( {U}_{\alpha \beta \gamma } \) 上从 \( {\theta }_{\alpha } \) 旋转到 \( {\theta }_{\beta } \) 再从 \( {\theta }_{\beta } \) 旋转到 \( {\theta }_{\gamma } \) 等于从 \( {\theta }_{\alpha } \) 直接旋转到 \( {\theta }_{\gamma } \) ，但可能 \( {\varphi }_{\alpha \beta } + {\varphi }_{\beta \gamma } - {\varphi }_{\alpha \gamma } \neq  0 \) . 确实,我们能说的是在 \( {U}_{\alpha \beta \gamma } \) 上

\[
{\varphi }_{\beta \gamma } - {\varphi }_{\alpha \gamma } + {\varphi }_{\alpha \beta } \in  {2\pi }\mathbb{Z}. \tag{13}
\]

另一方面,当然在 \( {U}_{\alpha \beta } \) 上也成立

\[
{\varphi }_{\alpha \beta } + {\varphi }_{\beta \alpha } \in  {2\pi }\mathbb{Z}\text{ . }
\]

旁白. 对每个非空交 \( {U}_{\alpha \beta \gamma } \) 赋予一个整数:

(6.35)

\[
{\varepsilon }_{\alpha \beta \gamma } = \frac{1}{2\pi }\left( {{\varphi }_{\beta \gamma } - {\varphi }_{\alpha \gamma } + {\varphi }_{\alpha \beta }}\right) .
\]

这些整数的集类 \( \varepsilon  = \{ {\varepsilon }_{\alpha \beta \gamma }\} \) 用来衡量集类 \( \{ {\varphi }_{\alpha \beta }\} \) 是不是一个 cocycle. 另一方面，

\[
{\left( \delta \varepsilon \right) }_{\alpha \beta \gamma \delta } = {\varepsilon }_{\beta \gamma \delta } - {\varepsilon }_{\alpha \gamma \delta } + {\varepsilon }_{\alpha \beta \delta } - {\varepsilon }_{\alpha \beta \gamma }
\]

\[
= \frac{1}{2\pi }\left( {{\varphi }_{\gamma \delta } - {\varphi }_{\beta \delta } + {\varphi }_{\beta \gamma } - {\varphi }_{\gamma \delta } + {\varphi }_{\alpha \delta } - {\varphi }_{\alpha \gamma }}\right.
\]

\[
+ {\varphi }_{\beta \delta } - {\varphi }_{\alpha \delta } + {\varphi }_{\alpha \beta } - {\varphi }_{\beta \gamma } + {\varphi }_{\alpha \gamma } - {\varphi }_{\alpha \beta })
\]

\[
= 0\text{ , }
\]

即 \( \varepsilon  = \left\{  {\varepsilon }_{\alpha \beta \gamma }\right\} \) 是一个 cocycle. \( \left\lbrack  \varepsilon \right\rbrack \) 是开覆盖 \( \left\{  {U}_{\alpha }\right\} \) 的取值于常值预层 \( \mathbb{Z} \) 的一个 Čech 上同调类, 见第 11 节.

此处采用 de Rham 上同调的语言. 虽然 \( \left\{  {\varphi }_{\alpha \beta }\right\} \) 不满足 cocycle 条件,但是由 (13) 知 \( \left\{  {d{\varphi }_{\alpha \beta }}\right\} \) 满足 cocycle 条件:

\[
d{\varphi }_{\beta \gamma } - d{\varphi }_{\alpha \gamma } + d{\varphi }_{\alpha \beta } = 0. \tag{14}
\]

练习 6.36. 存在 \( {\xi }_{\alpha } \in  {\Omega }^{1}\left( {U}_{\alpha }\right) \) 使得在 \( {U}_{\alpha \beta } \) 上,

\[
\frac{1}{2\pi }d{\varphi }_{\alpha \beta } = {\left. {\xi }_{\beta }\right| }_{{U}_{\alpha \beta }} - {\left. {\xi }_{\alpha }\right| }_{{U}_{\alpha \beta }}.
\]

证. 令

\[
{\xi }_{\alpha } = \frac{1}{2\pi }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d{\varphi }_{\gamma \alpha } \in  {\Omega }^{1}\left( {U}_{\alpha }\right) . \tag{15}
\]

此处把定义在 \( {U}_{\gamma \alpha } \) 上的形式 \( {\rho }_{\gamma }d{\varphi }_{\gamma \alpha } \) 零延拓到 \( {U}_{\alpha } \) . 应用 cocycle 条件 (14) 得到

\[
{\left. {\xi }_{\beta }\right| }_{{U}_{\alpha \beta }} - {\left. {\xi }_{\alpha }\right| }_{{U}_{\alpha \beta }} = \frac{1}{2\pi }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }\left( {d{\varphi }_{\gamma \beta } - d{\varphi }_{\gamma \alpha }}\right)
\]

\[
= \frac{1}{2\pi }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d{\varphi }_{\alpha \beta } = \frac{1}{2\pi }d{\varphi }_{\alpha \beta }.
\]

所以在 \( {U}_{\alpha \beta } \) 上, \( d{\xi }_{\alpha } = d{\xi }_{\beta }.{\left\{  d{\xi }_{\alpha }\right\}  }_{\alpha  \in  I} \) 能拼成 \( M \) 上一个整体定义的 2-形式 \( e \) :

\[
{\left. e\right| }_{{U}_{\alpha }} = d{\xi }_{\alpha } \tag{16}
\]

显然 \( {de} = 0 \) .

断言. \( \left\lbrack  e\right\rbrack   \in  {H}^{2}\left( M\right) \) 与 \( \left\{  {\xi }_{\alpha }\right\} \) 的选取无关.

证. 设 \( \left\{  {\overline{\xi }}_{\alpha }\right\} \) 也满足条件: 在 \( {U}_{\alpha \beta } \) 上,

\[
\frac{1}{2\pi }d{\varphi }_{\alpha \beta } = {\overline{\xi }}_{\beta } - {\overline{\xi }}_{\alpha }
\]

则

\[
{\overline{\xi }}_{\beta } - {\xi }_{\beta } = {\overline{\xi }}_{\alpha } - {\xi }_{\alpha },
\]

即 \( {\left\{  {\overline{\xi }}_{\alpha } - {\xi }_{\alpha }\right\}  }_{\alpha  \in  I} \) 能拼成 \( M \) 上整体定义的 1-形式 \( \eta  : {\left. \eta \right| }_{{U}_{\alpha }} = {\overline{\xi }}_{\alpha } - {\xi }_{\alpha } \) . 所以

\[
{d\eta } = d{\overline{\xi }}_{\alpha } - d{\xi }_{\alpha },
\]

即 \( {\left\{  d{\xi }_{\alpha }\right\}  }_{\alpha  \in  I} \) 拼成的 2-形式 \( e \) 与 \( \left\{  {d{\overline{\xi }}_{\alpha }}\right\} \) 拼成的 2-形式 \( \bar{e} \) 相差一个恰当的 2-形式 \( {d\eta } \) . 所以 \( \left\lbrack  e\right\rbrack   = \left\lbrack  \bar{e}\right\rbrack \) .

定义. \( \left\lbrack  e\right\rbrack   \in  {H}^{2}\left( M\right) \) 称为平面丛 \( E \) 的欧拉类,有时也记作 \( e\left( E\right) \) .

给定 \( E \) 的一个定向平凡化, \( {g}_{\alpha \beta } : {U}_{\alpha \beta } \rightarrow  {SO}\left( 2\right) \) . 因为 \( {SO}\left( 2\right)  = {SU}\left( 1\right) \) ,所以

\[
{r}_{\alpha }{e}^{i{\theta }_{\alpha }} = {r}_{\beta }{e}^{i{\theta }_{\beta }}{\pi }^{ * }{g}_{\alpha \beta }
\]

或

\[
{\theta }_{\alpha } = {\theta }_{\beta } + \left( {1/i}\right) {\pi }^{ * }\log {g}_{\alpha \beta }.
\]

但是已设

\[
{\theta }_{\beta } = {\theta }_{\alpha } + {\pi }^{ * }{\varphi }_{\alpha \beta },
\]

所以

\[
{\pi }^{ * }{\varphi }_{\alpha \beta } =  - \left( {1/i}\right) {\pi }^{ * }\log {g}_{\alpha \beta }
\]

由于 \( {\pi }^{ * } \) 是单射，所以

\[
{\varphi }_{\alpha \beta } =  - \left( {1/i}\right) \log {g}_{\alpha \beta }.
\]

因此,结合 \( e \) 的定义 (16) 与 \( {\xi }_{\alpha } \) 的定义 (15),最终可得

(6.38)

\[
{\left. e\right| }_{{U}_{\alpha }} = d{\xi }_{\alpha } =  - \frac{1}{2\pi i}\mathop{\sum }\limits_{\gamma }d\left( {{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right) .
\]

这就是定向平面丛欧拉类的显式表示公式.

当 \( E \) 是乘积丛时，转移函数 \( {g}_{\alpha \beta } \) 是常值矩阵，所以它的欧拉类等于零. 从这个意义上来说欧拉类用来衡量定向向量丛 \( E \) 的扭曲程度.

命题 6.39. 设 \( f : N \rightarrow  M \) 是光滑映射, \( \pi  : E \rightarrow  M \) 是秩 2 定向向量丛. 则

\[
e\left( {{f}^{-1}E}\right)  = {f}^{ * }e\left( E\right)  \in  {H}^{2}\left( N\right) .
\]

证. 由于 \( {f}^{-1}E \) 的转移函数是 \( {f}^{ * }{g}_{\alpha \beta } = {g}_{\alpha \beta } \circ  f \) , 而 \( {\left\{  {f}^{ * }{\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) 是从属于 \( N \) 的开覆盖 \( {\left\{  {f}^{-1}\left( {U}_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) 的单位分解. 所以由表示公式 (6.38) 可得结论.

平面丛 Thom 类的显式表示现在回顾头来看 \( E \) 的 Thom 类 \( \Phi \) . 由 (6.34) 与 (6.36),在 \( {\left. {E}^{0}\right| }_{{U}_{\alpha \beta }} \) 上,

(6.36.1)

\[
\frac{d{\theta }_{\alpha }}{2\pi } - {\pi }^{ * }{\xi }_{\alpha } = \frac{d{\theta }_{\beta }}{2\pi } - {\pi }^{ * }{\xi }_{\beta }.
\]

所以 \( {\left\{  d{\theta }_{\alpha }/2\pi  - {\pi }^{ * }{\xi }_{\alpha }\right\}  }_{\alpha  \in  I} \) 定义了 \( {E}^{0} \) 上一个 1-形式 \( \psi \) . \( \psi \) 限制在每条纤维 \( {E}_{x}^{0} \) 上是 \( d{\theta }_{\alpha }/{2\pi } \) ,它是 \( {E}_{x}^{0} \) 的角形式; 同时

(6.37)

\[
{d\psi } =  - {\pi }^{ * }e
\]

在 \( E \) 上有定义. 所以由前面的讨论知 \( \psi \) 是整体角形式, \( E \) 的 Thom 类是

(6.40)

\[
\Phi  = {d\rho }\left( r\right)  \land  \psi  + \rho \left( r\right) {d\psi } = {d\rho }\left( r\right)  \land  \psi  - \rho \left( r\right) {\pi }^{ * }e.
\]

若 \( s : M \rightarrow  E \) 是 \( E \) 的零截面,则

\[
{s}^{ * }\Phi  = d\left( {\rho \left( 0\right) }\right)  \land  {s}^{ * }\psi  - \rho \left( 0\right) {s}^{ * }{\pi }^{ * }e = e.
\]

命题 6.41. 零截面把 Thom 类拉回为欧拉类.

因为

\[
{\left. \psi \right| }_{{U}_{\alpha }} = \frac{d{\theta }_{\alpha }}{2\pi } - {\pi }^{ * }{\xi }_{\alpha } = \frac{d{\theta }_{\alpha }}{2\pi } + \frac{1}{2\pi i}{\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha },
\]

所以在 \( {\left. E\right| }_{{U}_{\alpha }} \) 上,

\[
\Phi  = {d\rho }\left( r\right)  \land  \left( {\frac{d{\theta }_{\alpha }}{2\pi } + \frac{1}{2\pi i}{\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right)
\]

\[
+ \frac{1}{2\pi i}\rho \left( r\right) d\left( {{\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right)
\]

(6.42)

\[
= {d\rho }\left( r\right)  \land  \frac{d{\theta }_{\alpha }}{2\pi } + \frac{1}{2\pi i}d\left( {\rho \left( r\right) {\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right) .
\]

这是定向平面丛 Thom 类的显式表示公式.

练习 6.43. 设 \( \pi  : E \rightarrow  M \) 是定向平面丛, \( \Phi \) 是 \( E \) 的 Thom 类. 于是有同构

\[
\land  \Phi  : {H}^{ * }\left( M\right) \overset{ \sim  }{ \rightarrow  }{H}_{cv}^{* + 2}\left( E\right) .
\]

因此 \( E \) 上每个紧垂直上同调类是 \( \Phi \) 与 \( M \) 上一个上同调类的拉回的外积. 求上同调类 \( \left\lbrack  u\right\rbrack   \in  {H}^{ * }\left( M\right) \) 使得

\[
{\Phi }^{2} = \Phi  \land  {\pi }^{ * }\left\lbrack  u\right\rbrack   \in  {H}_{cv}^{ * }\left( E\right)
\]

练习 6.44. (复射影空间 \( \mathbb{C}{P}^{n} \) ) 设 \( Z = \left( {{Z}_{0},\ldots ,{Z}_{n}}\right) \) 是 \( {\mathbb{C}}^{n + 1} \) 的复坐标. 在 \( {\mathbb{C}}^{n + 1} - \{ 0\} \) 上定义等价关系 “ \( \sim \) ”:

\[
Z \sim  {\lambda Z}\text{ ,对 }Z \in  {\mathbb{C}}^{n + 1} - \{ 0\} \text{ 与 }\lambda  \in  \mathbb{C} - \{ 0\} \text{ . }
\]

定义商空间

\[
\mathbb{C}{P}^{n} = {\mathbb{C}}^{n + 1} - 0/ \sim
\]

并赋予商拓扑. \( \mathbb{C}{P}^{n} \) 称为复射影空间.

\( {\mathbb{C}}^{n + 1} \) 的复坐标 \( Z \) 给出了 \( \mathbb{C}{P}^{n} \) 的齐次坐标 \( \left\lbrack  Z\right\rbrack   = \left\lbrack  {{Z}_{0} : \cdots  : {Z}_{n}}\right\rbrack  ,{Z}_{i} \) 不全为零. 令 \( {U}_{i} = \left\{  {\left\lbrack  Z\right\rbrack   \mid  {Z}_{i} \neq  0}\right\} \) . 则 \( \mathbb{C}{P}^{n} = \mathop{\bigcup }\limits_{{i = 0}}^{n}{U}_{i} \) .

(a) 证明 \( \mathbb{C}{P}^{n} \) 是复流形.

(b) 求法丛 \( {N}_{\mathbb{C}{P}^{1}/\mathbb{C}{P}^{2}} \) 相对于 \( \mathbb{C}{P}^{1} \) 的上述标准开覆盖的转移函数.

解. (a) 定义映射 \( {\varphi }_{i} : {U}_{i} \rightarrow  {\mathbb{C}}^{n} \) 为

\[
{\varphi }_{i}\left( \left\lbrack  {{Z}_{0} : \cdots  : {Z}_{n}}\right\rbrack  \right)  = \left( {\frac{{Z}_{0}}{{Z}_{i}},\ldots ,\frac{{Z}_{i - 1}}{{Z}_{i}},\frac{{Z}_{i + 1}}{{Z}_{i}},\ldots ,\frac{{Z}_{n}}{{Z}_{i}}}\right) .
\]

容易验证 \( {\mathbb{C}}^{n} \) 的两个开集间的微分同胚

\[
{\varphi }_{i} \circ  {\varphi }_{j}^{-1} : {\varphi }_{j}\left( {U}_{ij}\right)  \rightarrow  {\varphi }_{i}\left( {U}_{ij}\right)
\]

是全纯映射. 所以 \( {\left\{  \left( {U}_{i},{\varphi }_{i}\right) \right\}  }_{i = 0}^{n} \) 是 \( \mathbb{C}{P}^{n} \) 的一个复坐标图册, \( \mathbb{C}{P}^{n} \) 是复维数为 \( n \) 的复流形.

(b) \( \mathbb{C}{P}^{1} \) 作为 \( \mathbb{C}{P}^{2} \) 的复子流形:

\[
\mathbb{C}{P}^{1} = \left\{  {\left\lbrack  {{Z}_{0} : {Z}_{1} : 0}\right\rbrack   \in  \mathbb{C}{P}^{2} \mid  {Z}_{0} \neq  0\text{ 或 }{Z}_{1} \neq  0}\right\}  .
\]

由 (a) 知 \( \mathbb{C}{P}^{2} \) 的一个复坐标图册为 \( {\left\{  \left( {U}_{i},{\varphi }_{i}\right) \right\}  }_{i = 0}^{2} \) ,其中

\[
{\varphi }_{0} : {U}_{0} \rightarrow  {\mathbb{C}}^{2},\;{\varphi }_{0}\left( \left\lbrack  {{Z}_{0} : {Z}_{1} : {Z}_{2}}\right\rbrack  \right)  = \left( {{Z}_{1}/{Z}_{0},{Z}_{2}/{Z}_{0}}\right)
\]

\[
{\varphi }_{1} : {U}_{1} \rightarrow  {\mathbb{C}}^{2},\;{\varphi }_{1}\left( \left\lbrack  {{Z}_{0} : {Z}_{1} : {Z}_{2}}\right\rbrack  \right)  = \left( {{Z}_{0}/{Z}_{1},{Z}_{2}/{Z}_{1}}\right)
\]

令 \( {V}_{0} = {U}_{0} \cap  \mathbb{C}{P}^{1},{V}_{1} = {U}_{1} \cap  \mathbb{C}{P}^{1} \) . 则 \( \left( {{V}_{0},{\left. {\varphi }_{0}\right| }_{{V}_{0}}}\right) ,\left( {{V}_{1},{\left. {\varphi }_{1}\right| }_{{V}_{1}}}\right) \) 构成了 \( \mathbb{C}{P}^{1} \) 的复坐标图册,其中 \( z = {Z}_{1}/{Z}_{0} \) 是 \( {V}_{0} \) 上复坐标, \( w = {Z}_{0}/{Z}_{1} \) 是 \( {V}_{1} \) 上复坐标. 所以在 \( {V}_{0} \cap  {V}_{1} \) 上,

\[
z = \frac{1}{w}
\]

而 \( {Z}_{2}/{Z}_{0},{Z}_{2}/{Z}_{1} \) 可分别看作子流形 \( \mathbb{C}{P}^{1} \) 的法丛 \( N \) 限制在 \( {V}_{0},{V}_{1} \) 的局部平凡化的复坐标. 根据转移函数 \( {g}_{01} : {V}_{0} \cap  {V}_{1} \rightarrow  \mathbb{C} \) 的定义有

\[
\frac{{Z}_{2}}{{Z}_{0}} = {g}_{01}\frac{{Z}_{2}}{{Z}_{1}}
\]

即

\[
{g}_{01} = \frac{{Z}_{1}}{{Z}_{0}} = z = \frac{1}{w}.
\]

例 6.44.1. ( \( \mathbb{C}{P}^{1} \) 在 \( \mathbb{C}{P}^{2} \) 中的法丛的欧拉类) 设 \( N = {N}_{\mathbb{C}{P}^{1}/\mathbb{C}{P}^{2}} \) 是 \( \mathbb{C}{P}^{1} \) 在 \( \mathbb{C}{P}^{2} \) 中的法丛. 因为 \( \mathbb{C}{P}^{1} \) 是实 2 维紧定向流形,它的最高维上同调是 \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right)  = \mathbb{R} \) . 所以 \( N \) 的欧拉类 \( e\left( N\right) \) 是 \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) 生成元的倍数.

设 \( \left\{  {{\rho }_{0},{\rho }_{1}}\right\} \) 是从属于开覆盖 \( \left\{  {{V}_{0},{V}_{1}}\right\} \) 的单位分解, \( {\rho }_{0} \) 在 \( {V}_{0} \simeq  {\mathbb{C}}^{1} \) 上原点的一个邻域为 1，在无穷远点的一个邻域为 0 . 由练习 6.44， \( {g}_{01} = z = 1/w \) . 根据欧拉类的显式表示公式 (6.38), \( N \) 的欧拉类为

\[
e\left( N\right)  =  - \frac{1}{2\pi i}d\left( {{\rho }_{0} \cdot  d\log \frac{1}{w}}\right) \;\text{ on }{V}_{1} \tag{17}
\]

\[
=  - \frac{1}{2\pi i}d\left( {{\rho }_{0} \cdot  d\log z}\right) \;\text{ on }{V}_{01} \simeq  \mathbb{C} - 0.
\]

所以

\[
{\int }_{\mathbb{C}{P}^{1}}e\left( N\right)  =  - \frac{1}{2\pi i}{\int }_{\mathbb{C}}d\left( {{\rho }_{0}{dz}/z}\right) .
\]

设 \( \operatorname{Supp}{\rho }_{0} \subset  {B}_{R}\left( 0\right) \) . 令 \( {A}_{r} = {B}_{R}\left( 0\right)  - {B}_{r}\left( 0\right) \) . 则 \( \partial {B}_{R}\left( 0\right) \) 与 \( \partial {B}_{r}\left( 0\right) \) 是 \( {A}_{r} \) 的边界且其上诱导定向分别是逆时针与顺时针. 计算

\[
{\int }_{\mathbb{C}}d\left( {{\rho }_{0} \cdot  \frac{dz}{z}}\right)  = \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{{A}_{r}}d\left( {{\rho }_{0}{dz}/z}\right)
\]

\[
= \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{\partial {B}_{R}\left( 0\right)  - \partial {B}_{r}\left( 0\right) }{\rho }_{0}{dz}/z\text{ 根据 Stokes 定理 }
\]

\[
=  - \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{\partial {B}_{r}\left( 0\right) }{dz}/z
\]

\[
=  - {2\pi i}\text{ . }
\]

![bo_d7e85t491nqc73eqefm0_228_800_188_737_617_0.jpg](images/fu_algebraic_topology_and_differential_forms_030_bod7e85t491nqc73eqefm02288001887376170.jpg)

因此

\[
{\int }_{\mathbb{C}{P}^{1}}e\left( N\right)  =  - \frac{1}{2\pi i}\left( {-{2\pi i}}\right)  = 1.
\]

补充练习 1. 仔细检查会发现公式 (17) 与公式 (6.38) 在形式上有点不同. 证明这两个公式其实相等.

练习 6.45. 在复射影空间 \( \mathbb{C}{P}^{n} \) 上有一个称之为万有子丛 (universal sub-bundle) 的 tautological 线丛(此处指复线丛，所以是平面丛) \( S \) ，它是乘积丛 \( \mathbb{C}{P}^{n} \times  {\mathbb{C}}^{n + 1} \) 的子丛,定义为

\[
S = \left\{  {\left( {l, z}\right)  \mid  l \in  \mathbb{C}{P}^{n}, z \in  l}\right\}  .
\]

所以 \( S \) 在点 \( l \in  \mathbb{C}{P}^{n} \) 上的纤维是由 \( l \) 表示的 \( {\mathbb{C}}^{n + 1} \) 中通过原点的复直线. 求 \( \mathbb{C}{P}^{1} \) 的万有子丛 \( S \) 相对于标准开覆盖的转移函数并计算它的欧拉类.

练习 6.46. 设 \( {S}^{n} \) 是 \( {\mathbb{R}}^{n + 1} \) 中单位球面, \( i : {S}^{n} \rightarrow  {S}^{n} \) 是对径映射:

\[
i : \left( {{x}_{1},\ldots ,{x}_{n + 1}}\right)  \mapsto  \left( {-{x}_{1},\ldots , - {x}_{n + 1}}\right) .
\]

对径映射 \( i \) 在 \( {S}^{n} \) 上定义了一个等价关系: 对 \( x \in  {S}^{n}, x \sim  i\left( x\right) \) . 由此等价关系定义 \( {S}^{n} \) 的商空间,即实射影空间 \( \mathbb{R}{P}^{n} \) .

(a) \( {S}^{n} \) 上一个微分形式 \( \omega \) 称为不变形式若它满足 \( {i}^{ * }\omega  = \omega .{S}^{n} \) 上所有不变形式组成的向量空间 \( {\Omega }^{ * }{\left( {S}^{n}\right) }^{I} \) 是一个微分复形,所以可定义 \( {S}^{n} \) 的不变上同调 \( {H}^{ * }{\left( {S}^{n}\right) }^{I} \) . 证明 \( {H}^{ * }\left( {\mathbb{R}{P}^{n}}\right)  \simeq  {H}^{ * }{\left( {S}^{n}\right) }^{I} \) .

(b) 证明自然映射 \( {H}^{ * }{\left( {S}^{n}\right) }^{I} \rightarrow  {H}^{ * }\left( {S}^{n}\right) \) 是单射.

(c) 给 \( {S}^{n} \) 标准定向. 证明对径映射 \( i : {S}^{n} \rightarrow  {S}^{n} \) 对奇数 \( n \) 是保定向的,对偶数 \( n \) 是反定向的. 因此若 \( \left\lbrack  \sigma \right\rbrack \) 是 \( {H}^{n}\left( {S}^{n}\right) \) 的一个生成元,则 \( \left\lbrack  \sigma \right\rbrack \) 是非平凡的不变上同调类当且仅当 \( n \) 是奇数.

(d) 证明 \( \mathbb{R}{P}^{n} \) 的 de Rham 上同调

\[
{H}^{q}\left( {\mathbb{R}{P}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ 对 }q = 0, \\  0 & \text{ 对 }0 < q < n. \\  \mathbb{R} & \text{ 对 }q = n\text{ 奇数, } \\  0 & \text{ 对 }q = n\text{ 偶数. } \end{array}\right.
\]

作业:

1. 练习 6.43.

2. 补充练习 1.

3. 练习 6.45.

4. 练习 6.46.
