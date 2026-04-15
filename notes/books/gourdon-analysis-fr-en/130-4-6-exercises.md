#### 4.6. Exercises

*Français : 4.6. Exercices*

EXERCICE 1. Calculer les intégrales doubles \( {\iint }_{D}f\left( {x, y}\right) {dxdy} \) dans les cas suivants :

> EXERCISE 1. Calculate the double integrals \( {\iint }_{D}f\left( {x, y}\right) {dxdy} \) in the following cases:

\[
\text{ a) }f\left( {x, y}\right)  = {xy}\text{ et }D = \left\{  {\left( {x, y}\right)  \in  {\mathbb{R}}^{2} \mid  x \geq  0, y \geq  0, x + y \leq  1}\right\}  \text{ ; }
\]

b) \( f\left( {x, y}\right) = {x}^{2} \) et \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid {x}^{2} \leq y \leq x}\right\} \) ;

> b) \( f\left( {x, y}\right) = {x}^{2} \) and \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid {x}^{2} \leq y \leq x}\right\} \) ;

\[
\text{ c) }f\left( {x, y}\right)  = \left( {{x}^{2} - {y}^{2}}\right) {e}^{xy}\text{ et }D = \left\{  {\left( {x, y}\right)  \in  {\mathbb{R}}^{2} \mid  {x}^{2} + {y}^{2} \leq  1, x + y \geq  1, x \geq  y}\right\}  \text{ ; }
\]

d) \( f\left( {x, y}\right) = x\cos \left( \sqrt{{x}^{2} + {y}^{2}}\right) \) et \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid x \geq y \geq 0,{x}^{2} + {y}^{2} \leq \pi }\right\} \) .

> d) \( f\left( {x, y}\right) = x\cos \left( \sqrt{{x}^{2} + {y}^{2}}\right) \) and \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid x \geq y \geq 0,{x}^{2} + {y}^{2} \leq \pi }\right\} \) .

Solution.

> Solution.

a) On peut écrire \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq 1,0 \leq y \leq 1 - x}\right\} \) , et en appliquant le théorème de Fubini, on a

> a) We can write \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq 1,0 \leq y \leq 1 - x}\right\} \) , and by applying Fubini's theorem, we have

\[
{\iint }_{D}{xydxdy} = {\int }_{0}^{1}\left\lbrack  {{\int }_{0}^{1 - x}{xydy}}\right\rbrack  {dx} = {\int }_{0}^{1}x\frac{{\left( 1 - x\right) }^{2}}{2}{dx} = \frac{1}{24}.
\]

![bo_d7fjkrs91nqc73ereoog_363_1232_599_163_161_0.jpg](images/gourdon_analysis_fr_en_018_bod7fjkrs91nqc73ereoog36312325991631610.jpg)

b) On procède de la même manière. Si \( {x}^{2} \leq x \) , on a forcément \( 0 \leq x \leq 1 \) , donc \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq 1,{x}^{2} \leq y \leq x}\right\} \) . Le théorème de Fubini donne ensuite

> b) We proceed in the same way. If \( {x}^{2} \leq x \) , we necessarily have \( 0 \leq x \leq 1 \) , therefore \( D = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq 1,{x}^{2} \leq y \leq x}\right\} \) . Fubini's theorem then gives

\[
\iint {x}^{2}{dxdy} = {\int }_{0}^{1}\left\lbrack  {{\int }_{{x}^{2}}^{x}{x}^{2}{dy}}\right\rbrack  {dx} = {\int }_{0}^{1}\left( {x - {x}^{2}}\right) {x}^{2}{dx} = \frac{1}{20}.
\]

![bo_d7fjkrs91nqc73ereoog_363_1223_844_182_163_0.jpg](images/gourdon_analysis_fr_en_016_bod7fjkrs91nqc73ereoog36312238441821630.jpg)

c) La forme de \( D \) nous invite à changer de système de coordonnées. On effectue une transformation orthogonale, en écrivant \( x = \left( {X - Y}\right) /\sqrt{2} \) et \( y = \left( {X + Y}\right) /\sqrt{2} \) . Dans ce système de coordonnées, l’ensemble \( D \) devient \( {D}^{\prime } = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2}\left| {\; - \sqrt{2}/2 \leq Y \leq 0}\right. ,\sqrt{2}/2 \leq X \leq \sqrt{1 - {Y}^{2}}}\right\} \) . Le jacobien de la transformation est égal à 1 (transformation orthogonale), donc d'après le théorème du changement de variable

> c) The shape of \( D \) invites us to change the coordinate system. We perform an orthogonal transformation by writing \( x = \left( {X - Y}\right) /\sqrt{2} \) and \( y = \left( {X + Y}\right) /\sqrt{2} \) . In this coordinate system, the set \( D \) becomes \( {D}^{\prime } = \left\{ {\left( {X, Y}\right) \in {\mathbb{R}}^{2}\left| {\; - \sqrt{2}/2 \leq Y \leq 0}\right. ,\sqrt{2}/2 \leq X \leq \sqrt{1 - {Y}^{2}}}\right\} \) . The Jacobian of the transformation is equal to 1 (orthogonal transformation), so according to the change of variables theorem

\[
I = {\iint }_{D}\left( {{x}^{2} - {y}^{2}}\right) {e}^{xy}{dxdy} = {\iint }_{{D}^{\prime }}\left( {-{2XY}}\right) {e}^{\left( {{X}^{2} - {Y}^{2}}\right) /2}{dXdY},
\]

![bo_d7fjkrs91nqc73ereoog_363_1178_1140_221_171_0.jpg](images/gourdon_analysis_fr_en_015_bod7fjkrs91nqc73ereoog363117811402211710.jpg)

et d'après le théorème de Fubini

> and according to Fubini's theorem

\[
I = {\int }_{-\sqrt{2}/2}^{0}\left\lbrack  {{\int }_{\sqrt{2}/2}^{\sqrt{1 - {Y}^{2}}}\left( {-{2XY}}\right) {e}^{\left( {{X}^{2} - {Y}^{2}}\right) /2}{dX}}\right\rbrack  {dY}
\]

\[
= {\int }_{-\sqrt{2}/2}^{0}\left\lbrack  {-{2Y}\exp \left( {\frac{1}{2} - {Y}^{2}}\right)  + {2Y}\exp \left( {\frac{1}{4} - \frac{{Y}^{2}}{2}}\right) }\right\rbrack  {dY} = 1 - 2{e}^{1/4} + {e}^{1/2}.
\]

d) On va évidemment passer en coordonnées polaires. En polaires, on a \( D = \{ \left( {r,\theta }\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {0,\pi /4}\right\rbrack \} \) donc d’après le théorème du changement de variable

> d) We will obviously switch to polar coordinates. In polar coordinates, we have \( D = \{ \left( {r,\theta }\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {0,\pi /4}\right\rbrack \} \) so, according to the change of variables theorem

\[
I = {\iint }_{D}x\cos \left( \sqrt{{x}^{2} + {y}^{2}}\right) {dxdy} = {\iint }_{\left\lbrack  {0,\pi }\right\rbrack   \times  \left\lbrack  {0,\pi /4}\right\rbrack  }r\left( {\cos \theta }\right) \left( {\cos r}\right) {rdrd\theta },
\]

![bo_d7fjkrs91nqc73ereoog_363_1224_1747_168_163_0.jpg](images/gourdon_analysis_fr_en_017_bod7fjkrs91nqc73ereoog363122417471681630.jpg)

et d'après le théorème de Fubini

> and according to Fubini's theorem

\[
I = \left( {{\int }_{0}^{\pi }{r}^{2}\cos {rdr}}\right) \left( {{\int }_{0}^{\pi /4}\cos {\theta d\theta }}\right)  = \left( {-{2\pi }}\right) \left( \frac{\sqrt{2}}{2}\right)  =  - \sqrt{2}\pi .
\]

EXERCICE 2. Calculer les intégrales triples \( I = {\iiint }_{D}f\left( {x, y, z}\right) {dxdydz} \) dans les cas sui-vants.

> EXERCISE 2. Calculate the triple integrals \( I = {\iiint }_{D}f\left( {x, y, z}\right) {dxdydz} \) in the following cases.

\[
\text{ a) }f\left( {x, y, z}\right)  = {x}^{2} + {y}^{2} + {z}^{2}\text{ et }D = \left\{  {\left( {x, y, z}\right)  \in  {\mathbb{R}}^{3}\left| \right| x\left| +\right| y\left| +\right| z \mid   \leq  1}\right\}  \text{ ; }
\]

\[
\text{ b) }f\left( {x, y, z}\right)  = \left| z\right| \text{ et }D = \left\{  {\left( {x, y, z}\right)  \in  {\mathbb{R}}^{3} \mid  {x}^{2} + {y}^{2} + {z}^{2} \leq  1}\right\}  \text{ ; }
\]

\[
\text{ c) }f\left( {x, y, z}\right)  = \left( {{x}^{2} + {y}^{2} + {z}^{2}}\right) {e}^{z}\text{ et }D = \left\{  {\left( {x, y, z}\right)  \in  {\mathbb{R}}^{3}\left| \right| x\left| { \leq  1,}\right| y\left| { \leq  1,}\right| z \mid   \leq  1}\right\}  \text{ ; }
\]

\[
\text{ d) }f\left( {x, y, z}\right)  = {xyz}\text{ et }D = \left\{  {\left( {x, y, z}\right)  \in  {\mathbb{R}}^{3} \mid  x \geq  0, y \geq  0, z \geq  0,{x}^{2} + {y}^{2} + {z}^{2} \leq  1}\right\}  \text{ . }
\]

Solution. a) Vue la symétrie de \( D \) et de l’intégrande par rapport aux plans \( {Oxy},{Oxz} \) et \( {Oyz} \) , on a

> Solution. a) Given the symmetry of \( D \) and the integrand with respect to the planes \( {Oxy},{Oxz} \) and \( {Oyz} \), we have

\( I = 8{\iiint }_{{D}^{\prime }}\left( {{x}^{2} + {y}^{2} + {z}^{2}}\right) {dxdydz}\; \) où \( \;{D}^{\prime } = \left\{ {\left( {x, y, z}\right) \in {\mathbb{R}}^{3} \mid x \geq 0, y \geq 0, z \geq 0, x + y + z \leq 1}\right\} . \)

> \( I = 8{\iiint }_{{D}^{\prime }}\left( {{x}^{2} + {y}^{2} + {z}^{2}}\right) {dxdydz}\; \) where \( \;{D}^{\prime } = \left\{ {\left( {x, y, z}\right) \in {\mathbb{R}}^{3} \mid x \geq 0, y \geq 0, z \geq 0, x + y + z \leq 1}\right\} . \)

De même, la symétrie de \( {D}^{\prime } \) et de \( {x}^{2} + {y}^{2} + {z}^{2} \) par rapport aux plans \( x = y, x = z \) et \( y = z \) entraîne

> Similarly, the symmetry of \( {D}^{\prime } \) and \( {x}^{2} + {y}^{2} + {z}^{2} \) with respect to the planes \( x = y, x = z \) and \( y = z \) implies

\[
I = {24}{\iiint }_{{D}^{\prime }}{z}^{2}{dxdydz}.
\]

L’intégrande ne dépend plus que de \( z \) , nous allons donc effectuer une sommation par tranches. Si \( \left( {x, y, z}\right) \in {D}^{\prime } \) , on a \( 0 \leq z \leq 1 \) , et l’intersection de \( {D}^{\prime } \) avec le plan horizontal de côte \( z \) est \( {D}^{\prime }\left( z\right) = \{ \left( {x, y}\right) \in \; {\mathbb{R}}^{2} \mid x \geq 0, y \geq 0, x + y \leq 1 - z\} \) , par conséquent

> The integrand depends only on \( z \), so we will perform summation by slices. If \( \left( {x, y, z}\right) \in {D}^{\prime } \), we have \( 0 \leq z \leq 1 \), and the intersection of \( {D}^{\prime } \) with the horizontal plane at height \( z \) is \( {D}^{\prime }\left( z\right) = \{ \left( {x, y}\right) \in \; {\mathbb{R}}^{2} \mid x \geq 0, y \geq 0, x + y \leq 1 - z\} \), therefore

\[
I = {24}{\int }_{0}^{1}\left\lbrack  {{\iint }_{{D}^{\prime }\left( z\right) }{z}^{2}{dxdy}}\right\rbrack  {dz} = {24}{\int }_{0}^{1}{z}^{2}\left( \frac{{\left( 1 - z\right) }^{2}}{2}\right) {dz} = \frac{2}{5}.
\]

![bo_d7fjkrs91nqc73ereoog_364_1176_803_179_225_0.jpg](images/gourdon_analysis_fr_en_020_bod7fjkrs91nqc73ereoog36411768031792250.jpg)

b) La symétrie de \( D \) et de \( z \mapsto \left| z\right| \) par rapport au plan Oxy entraîne

> b) The symmetry of \( D \) and \( z \mapsto \left| z\right| \) with respect to the Oxy plane implies

\[
I = 2{\iiint }_{{D}^{\prime }}z\;{dxdydz}\;\text{ où }\;{D}^{\prime } = \left\{  {\left( {x, y, z}\right)  \in  {\mathbb{R}}^{3} \mid  {x}^{2} + {y}^{2} + {z}^{2} \leq  1, z \geq  0}\right\}  .
\]

L’intégrande ne dépend plus que de \( z \) , le plus simple est d’effectuer une sommation par tranches. Pour tout \( \left( {x, y, z}\right) \in {D}^{\prime } \) , on a \( 0 \leq z \leq 1 \) , et l’intersection de \( {D}^{\prime } \) avec le plan horizontal d’abscisse \( z \) est \( {D}^{\prime }\left( z\right) = \; \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid {x}^{2} + {y}^{2} \leq 1 - {z}^{2}}\right\} \) (disque de rayon \( \left. \sqrt{1 - {z}^{2}}\right) \) . On en déduit

> The integrand depends only on \( z \), the simplest approach is to perform summation by slices. For any \( \left( {x, y, z}\right) \in {D}^{\prime } \), we have \( 0 \leq z \leq 1 \), and the intersection of \( {D}^{\prime } \) with the horizontal plane at abscissa \( z \) is \( {D}^{\prime }\left( z\right) = \; \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid {x}^{2} + {y}^{2} \leq 1 - {z}^{2}}\right\} \) (a disk of radius \( \left. \sqrt{1 - {z}^{2}}\right) \)). We deduce

\[
I = 2{\int }_{0}^{1}\left\lbrack  {{\iint }_{{D}^{\prime }\left( z\right) }{zdxdy}}\right\rbrack  {dz} = 2{\int }_{0}^{1}z\left( {\pi \left( {1 - {z}^{2}}\right) }\right) {dz} = \frac{\pi }{2}.
\]

![bo_d7fjkrs91nqc73ereoog_364_1134_1245_253_196_0.jpg](images/gourdon_analysis_fr_en_019_bod7fjkrs91nqc73ereoog364113412452531960.jpg)

c) L’ensemble \( D \) est le pavé \( {\left\lbrack -1,1\right\rbrack }^{3} \) . On a \( I = J + K \) , où

> c) The set \( D \) is the box \( {\left\lbrack -1,1\right\rbrack }^{3} \). We have \( I = J + K \), where

\[
J = {\iiint }_{D}\left( {{x}^{2} + {y}^{2}}\right) {e}^{z}{dxdydz}\;\text{ et }\;K = {\iiint }_{D}{z}^{2}{e}^{z}{dxdydz}.
\]

On calcule \( J \) en appliquant le théorème de Fubini (voir le corollaire 1), qui entraîne

> We calculate \( J \) by applying Fubini's theorem (see corollary 1), which implies

\[
J = \left( {{\iint }_{{\left\lbrack  -1,1\right\rbrack  }^{2}}\left( {{x}^{2} + {y}^{2}}\right) {dxdy}}\right) \left( {{\int }_{-1}^{1}{e}^{z}{dz}}\right) ,
\]

et en appliquant une nouvelle fois le théorème de Fubini, on trouve que le premier terme du produit est

> and by applying Fubini's theorem once more, we find that the first term of the product is

\[
{\int }_{-1}^{1}\left\lbrack  {{\int }_{-1}^{1}\left( {{x}^{2} + {y}^{2}}\right) {dy}}\right\rbrack  {dx} = {\int }_{-1}^{1}\left( {2{x}^{2} + \frac{2}{3}}\right) {dx} = \frac{8}{3},
\]

donc finalement \( J = \frac{8}{3}\left( {e - 1/e}\right) \) .

> so finally \( J = \frac{8}{3}\left( {e - 1/e}\right) \).

Pour calculer \( K \) , on effectue une sommation par tranches (l’intégrande ne dépend que de \( z \) ), ce qui donne

> To calculate \( K \), we perform summation by slices (the integrand depends only on \( z \)), which gives

\[
K = {\int }_{-1}^{1}\left\lbrack  {{\iint }_{{\left\lbrack  -1,1\right\rbrack  }^{2}}{z}^{2}{e}^{z}{dxdy}}\right\rbrack  {dz} = 4{\int }_{-1}^{1}{z}^{2}{e}^{z}{dz} = 4\left( {e - \frac{5}{6}}\right) .
\]

Finalement, on trouve \( I = J + K = \frac{20}{3}e - \frac{52}{3}\frac{1}{e} \) .

> Finally, we find \( I = J + K = \frac{20}{3}e - \frac{52}{3}\frac{1}{e} \) .

d) La forme de \( D \) nous invite à passer en coordonnées sphériques. Dans ces coordonnées, \( D \) est le pavé \( \left\lbrack {0,1}\right\rbrack \times \left\lbrack {0,\pi /2}\right\rbrack \times \left\lbrack {0,\pi /2}\right\rbrack \) , donc d’après le théorème du changement de variable,

> d) The form of \( D \) invites us to switch to spherical coordinates. In these coordinates, \( D \) is the block \( \left\lbrack {0,1}\right\rbrack \times \left\lbrack {0,\pi /2}\right\rbrack \times \left\lbrack {0,\pi /2}\right\rbrack \) , so according to the change of variables theorem,

\[
I = {\iiint }_{\left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,\pi /2}\right\rbrack   \times  \left\lbrack  {0,\pi /2}\right\rbrack  }\left( {r\cos \theta \cos \varphi }\right) \left( {r\sin \theta \cos \varphi }\right) \left( {r\sin \varphi }\right) {r}^{2}\cos {\varphi drd\theta d\varphi }
\]

\[
= {\iiint }_{\left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,\pi /2}\right\rbrack   \times  \left\lbrack  {0,\pi /2}\right\rbrack  }{r}^{5}\left( {\cos \theta \sin \theta }\right) \left( {{\cos }^{3}\varphi \sin \varphi }\right) {drd\theta d\varphi },
\]

et d'après le théorème de Fubini,

> and according to Fubini's theorem,

\[
I = \left( {{\int }_{0}^{1}{r}^{5}{dr}}\right) \left( {{\int }_{0}^{\pi /2}\cos \theta \sin {\theta d\theta }}\right) \left( {{\int }_{0}^{\pi /2}{\cos }^{3}\varphi \sin {\varphi d\varphi }}\right)  = \frac{1}{6}\frac{1}{2}\frac{1}{4} = \frac{1}{48}.
\]

EXERCICE 3. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {D}_{n} \) le compact de \( {\mathbb{R}}^{n} \) défini par

> EXERCISE 3. For all \( n \in {\mathbb{N}}^{ * } \) , let \( {D}_{n} \) be the compact set of \( {\mathbb{R}}^{n} \) defined by

\[
{D}_{n} = \left\{  {\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n}\mid \forall i,{x}_{i} \geq  0\text{ et }{x}_{1} + \cdots  + {x}_{n} \leq  1}\right\}  .
\]

Pour tout \( \left( {{k}_{1},\ldots ,{k}_{n}}\right) \in {\mathbb{N}}^{n} \) , calculer \( {I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right) = \int \cdots {\int }_{{D}_{n}}{x}_{1}^{{k}_{1}}\cdots {x}_{n}^{{k}_{n}}d{x}_{1}\cdots d{x}_{n} \) .

> For all \( \left( {{k}_{1},\ldots ,{k}_{n}}\right) \in {\mathbb{N}}^{n} \) , calculate \( {I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right) = \int \cdots {\int }_{{D}_{n}}{x}_{1}^{{k}_{1}}\cdots {x}_{n}^{{k}_{n}}d{x}_{1}\cdots d{x}_{n} \) .

Solution. En notant \( D\left( {x}_{n}\right) = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n - 1}}\right) \in {\mathbb{R}}^{n - 1}\mid \forall i,{x}_{i} \geq 0,{x}_{1} + \cdots + {x}_{n - 1} \leq 1 - {x}_{n}}\right\} \) , une intégration par tranches fournit

> Solution. By denoting \( D\left( {x}_{n}\right) = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n - 1}}\right) \in {\mathbb{R}}^{n - 1}\mid \forall i,{x}_{i} \geq 0,{x}_{1} + \cdots + {x}_{n - 1} \leq 1 - {x}_{n}}\right\} \) , integration by slices provides

\[
{I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right)  = {\int }_{0}^{1}{x}_{n}^{{k}_{n}}\underset{ = K\left( {x}_{n}\right) }{\underbrace{\left\lbrack  \int \cdots {\int }_{D\left( {x}_{n}\right) }{x}_{1}^{{k}_{1}}\cdots {x}_{n - 1}^{{k}_{n - 1}}d{x}_{1}\cdots d{x}_{n - 1}\right\rbrack  }}d{x}_{n}.
\]

(*)

> Pour \( {x}_{n} \) fixé, le changement de variable \( {x}_{i} = {t}_{i}\left( {1 - {x}_{n}}\right) \left( {1 \leq i \leq n - 1}\right) \) donne, d’après le théorème du changement de variable

For fixed \( {x}_{n} \) , the change of variables \( {x}_{i} = {t}_{i}\left( {1 - {x}_{n}}\right) \left( {1 \leq i \leq n - 1}\right) \) gives, according to the change of variables theorem

\[
K\left( {x}_{n}\right)  = {\left( 1 - {x}_{n}\right) }^{{k}_{1} + \cdots  + {k}_{n - 1} + n - 1}\int \cdots {\int }_{{D}_{n - 1}}{t}_{1}^{{k}_{1}}\cdots {t}_{n - 1}^{{k}_{n - 1}}d{t}_{1}\cdots d{t}_{n - 1}
\]

\[
= {\left( 1 - {x}_{n}\right) }^{{k}_{1} + \cdots  + {k}_{n - 1} + n - 1}{I}_{n - 1}\left( {{k}_{1},\ldots ,{k}_{n - 1}}\right) .
\]

On en déduit d'après (*)

> We deduce from (*) that

\[
{I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right)  = {I}_{n - 1}\left( {{k}_{1},\ldots ,{k}_{n - 1}}\right) {\int }_{0}^{1}{x}_{n}^{{k}_{n}}{\left( 1 - {x}_{n}\right) }^{{k}_{1} + \cdots  + {k}_{n - 1} + n - 1}d{x}_{n}
\]

\[
= {I}_{n - 1}\left( {{k}_{1},\ldots ,{k}_{n - 1}}\right) J\left( {{k}_{n},{k}_{1} + \cdots  + {k}_{n - 1} + n - 1}\right)
\]

\( \left( {* * }\right) \)

> où pour tout \( \left( {p, q}\right) \in {\mathbb{N}}^{2}, J\left( {p, q}\right) = {\int }_{0}^{1}{x}^{p}{\left( 1 - x\right) }^{q}{dx} \) .

where for all \( \left( {p, q}\right) \in {\mathbb{N}}^{2}, J\left( {p, q}\right) = {\int }_{0}^{1}{x}^{p}{\left( 1 - x\right) }^{q}{dx} \) .

> Calculons \( J\left( {p, q}\right) \) . Une intégration par parties fournit, si \( q \geq 1 \) ,

Let us calculate \( J\left( {p, q}\right) \) . Integration by parts provides, if \( q \geq 1 \) ,

\[
J\left( {p, q}\right)  = {\int }_{0}^{1}{x}^{p}{\left( 1 - x\right) }^{q}{dx} = {\left\lbrack  \frac{{x}^{p + 1}}{p + 1}{\left( 1 - x\right) }^{q}\right\rbrack  }_{0}^{1} + \frac{q}{p + 1}{\int }_{0}^{1}{x}^{p + 1}{\left( 1 - x\right) }^{q - 1}{dx} = \frac{q}{p + 1}J\left( {p + 1, q - 1}\right) .
\]

Cette relation de récurrence permet d'affirmer

> This recurrence relation allows us to state

\[
J\left( {p, q}\right)  = \frac{q!}{\left( {p + 1}\right) \cdots \left( {p + q}\right) }J\left( {p + q,0}\right)  = \frac{p!q!}{\left( {p + q + 1}\right) !}.
\]

D’après (**), on a donc

> According to (**), we therefore have

\[
{I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right)  = {I}_{n - 1}\left( {{k}_{1},\ldots ,{k}_{n - 1}}\right) \frac{{k}_{n}!\left( {{k}_{1} + \cdots  + {k}_{n - 1} + n - 1}\right) !}{\left( {{k}_{1} + \cdots  + {k}_{n} + n}\right) !},
\]

et comme \( {I}_{1}\left( {k}_{1}\right) = 1/\left( {1 + {k}_{1}}\right) \) , on obtient après une récurrence facile

> and since \( {I}_{1}\left( {k}_{1}\right) = 1/\left( {1 + {k}_{1}}\right) \) , we obtain after an easy recurrence

\[
{I}_{n}\left( {{k}_{1},\ldots ,{k}_{n}}\right)  = \frac{{k}_{1}!\cdots {k}_{n}!}{\left( {{k}_{1} + \cdots  + {k}_{n} + n}\right) !}.
\]

EXERCICE 4. a) Calculer l'aire du compact \( K \) délimité par la boucle droite de la lemniscate de Bernoulli, dont l’équation polaire est \( {r}^{2} = {a}^{2}\cos {2\theta }, - \pi /4 \leq \theta \leq \pi /4, a > 0 \) .

> EXERCISE 4. a) Calculate the area of the compact set \( K \) delimited by the right loop of the lemniscate of Bernoulli, whose polar equation is \( {r}^{2} = {a}^{2}\cos {2\theta }, - \pi /4 \leq \theta \leq \pi /4, a > 0 \) .

b) Calculer l’aire du compact \( K \) délimité par la boucle de la strophoïde droite, dont l’équation polaire est \( r = - a\frac{\cos {2\theta }}{\cos \theta }\left( {-\pi /2 < \theta < \pi /2}\right) \) .

> b) Calculate the area of the compact set \( K \) delimited by the loop of the right strophoid, whose polar equation is \( r = - a\frac{\cos {2\theta }}{\cos \theta }\left( {-\pi /2 < \theta < \pi /2}\right) \) .

Solution.

> Solution.

a) Il suffit d'utiliser le théorème de Green-Riemann, plus précisément l’application qui le suit à la page 358, qui exprime l’aire de \( K \) par \( \mathcal{A} = \; \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta } \) , ce qui ici donne

> a) It suffices to use the Green-Riemann theorem, more precisely the application that follows it on page 358, which expresses the area of \( K \) by \( \mathcal{A} = \; \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta } \) , which here gives

\[
\mathcal{A} = \frac{1}{2}{\int }_{-\pi /4}^{\pi /4}{a}^{2}\cos {2\theta d\theta } = \frac{{a}^{2}}{2}.
\]

![bo_d7fjkrs91nqc73ereoog_366_1127_437_261_145_0.jpg](images/gourdon_analysis_fr_en_022_bod7fjkrs91nqc73ereoog36611274372611450.jpg)

![bo_d7fjkrs91nqc73ereoog_366_1116_655_283_272_0.jpg](images/gourdon_analysis_fr_en_021_bod7fjkrs91nqc73ereoog36611166552832720.jpg)

b) On utilise comme précédemment, la formule \( \mathcal{A} = \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta } \) . Le tout est de déterminer \( \partial {K}^{ + } \) . Le paramètre \( r \) s’annule lorsque \( \cos \left( {2\theta }\right) = \) 0, donc pour \( \theta = \pm \pi /4 \) . Un paramétrage de la frontière de \( K \) est donc \( r = - a\cos \left( {2\theta }\right) /\cos \theta , - \pi /4 \leq \theta \leq \pi /4 \) . L’orientation est bien directe, on peut donc écrire

> b) We use, as before, the formula \( \mathcal{A} = \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta } \) . The whole point is to determine \( \partial {K}^{ + } \) . The parameter \( r \) vanishes when \( \cos \left( {2\theta }\right) = \) 0, therefore for \( \theta = \pm \pi /4 \) . A parameterization of the boundary of \( K \) is thus \( r = - a\cos \left( {2\theta }\right) /\cos \theta , - \pi /4 \leq \theta \leq \pi /4 \) . The orientation is indeed direct, so we can write

\[
\mathcal{A} = \frac{1}{2}{\int }_{-\pi /4}^{\pi /4}{a}^{2}\frac{{\cos }^{2}{2\theta }}{{\cos }^{2}\theta }{d\theta }
\]

et comme \( \cos \left( {2\theta }\right) = 2{\cos }^{2}\theta - 1 \) ,

> and since \( \cos \left( {2\theta }\right) = 2{\cos }^{2}\theta - 1 \) ,

\[
\mathcal{A} = \frac{{a}^{2}}{2}{\int }_{-\pi /4}^{\pi /4}\left( {4{\cos }^{2}\theta  - 4 + \frac{1}{{\cos }^{2}\theta }}\right) {d\theta } = \frac{{a}^{2}}{2}{\left\lbrack  \left( 2\theta  + \sin 2\theta \right)  - 4\theta  + \tan \theta \right\rbrack  }_{-\pi /4}^{\pi /4} = \frac{{a}^{2}}{2}\left( {4 - \pi }\right) .
\]

EXERCICE 5 (CALCUL DE L’INTEGRALE DE FRESNEL). Pour tout \( t \geq 0 \) , on pose

> EXERCISE 5 (CALCULATION OF THE FRESNEL INTEGRAL). For all \( t \geq 0 \) , we define

\[
F\left( t\right)  = {\iint }_{{\left\lbrack  0, t\right\rbrack  }^{2}}{e}^{i\left( {{x}^{2} + {y}^{2}}\right) }{dxdy}\;\text{ et }\;f\left( t\right)  = {\int }_{0}^{t}{e}^{i{x}^{2}}{dx}.
\]

a) Exprimer \( F\left( t\right) \) de deux manières différentes (l’une en fonction de \( f\left( t\right) \) , l’autre par passage en coordonnées polaires).

> a) Express \( F\left( t\right) \) in two different ways (one as a function of \( f\left( t\right) \) , the other by switching to polar coordinates).

b) Pour \( T > 0 \) , on pose \( I\left( T\right) = \frac{1}{T}{\int }_{0}^{T}F\left( t\right) {dt} \) . Montrer que \( I\left( T\right) \) converge lorsque \( T \rightarrow + \infty \) et calculer sa limite. En déduire la valeur de l'intégrale de Fresnel

> b) For \( T > 0 \) , we define \( I\left( T\right) = \frac{1}{T}{\int }_{0}^{T}F\left( t\right) {dt} \) . Show that \( I\left( T\right) \) converges as \( T \rightarrow + \infty \) and calculate its limit. Deduce the value of the Fresnel integral

\[
\varphi  = {\int }_{0}^{+\infty }{e}^{i{x}^{2}}{dx}
\]

Solution. a) La relation \( {e}^{i\left( {{x}^{2} + {y}^{2}}\right) } = {e}^{i{x}^{2}}{e}^{i{y}^{2}} \) entraîne, par application du théorème de Fubini,

> Solution. a) The relation \( {e}^{i\left( {{x}^{2} + {y}^{2}}\right) } = {e}^{i{x}^{2}}{e}^{i{y}^{2}} \) implies, by application of Fubini's theorem,

\[
F\left( t\right)  = \left( {{\int }_{0}^{t}{e}^{i{x}^{2}}{dx}}\right) \left( {{\int }_{0}^{t}{e}^{i{y}^{2}}{dy}}\right)  = f{\left( t\right) }^{2}.
\]

Calculons maintenant \( F\left( t\right) \) de manière différente. Tout d’abord, la symétrie du domaine et de l’intégrande par rapport à la droite \( x = y \) permet d’affirmer

> Let us now calculate \( F\left( t\right) \) in a different way. First, the symmetry of the domain and the integrand with respect to the line \( x = y \) allows us to state

\[
F\left( t\right)  = 2{\iint }_{{\Delta }_{t}}{e}^{i\left( {{x}^{2} + {y}^{2}}\right) }{dxdy},
\]

où \( {\Delta }_{t} = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq t,0 \leq y \leq x}\right\} \) . L’intégrande s’exprime au moyen de \( {x}^{2} + {y}^{2} \) , on est amené à passer en coordonnées polaires. En polaires, le compact \( {\Delta }_{t} \) est représenté par l'ensemble

> where \( {\Delta }_{t} = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid 0 \leq x \leq t,0 \leq y \leq x}\right\} \) . The integrand is expressed by means of \( {x}^{2} + {y}^{2} \) , we are led to switch to polar coordinates. In polar coordinates, the compact \( {\Delta }_{t} \) is represented by the set

\[
{K}_{t} = \left\{  {\left( {r,\theta }\right)  \in  {\mathbb{R}}^{ + } \times  \left\lbrack  {0,{2\pi }}\right\rbrack   \mid  0 \leq  r\cos \theta  \leq  t\;\text{ et }\;\theta  \in  \left\lbrack  {0,\frac{\pi }{4}}\right\rbrack  }\right\}  ,
\]

et après passage en coordonnées polaires, puis d'après le théorème de Fubini

> and after switching to polar coordinates, then according to Fubini's theorem

\[
F\left( t\right)  = 2{\iint }_{{K}_{t}}{e}^{i{r}^{2}}{rdrd\theta } = 2{\int }_{0}^{\pi /4}\left\lbrack  {{\int }_{0}^{t/\cos \theta }{e}^{i{r}^{2}}{rdr}}\right\rbrack  {d\theta }
\]

\[
= {\int }_{0}^{\pi /4}\frac{1}{i}\left( {\exp \left( {i\frac{{t}^{2}}{{\cos }^{2}\theta }}\right)  - 1}\right) {d\theta } = \frac{i\pi }{4} - i{\int }_{0}^{\pi /4}\exp \left( {i\frac{{t}^{2}}{{\cos }^{2}\theta }}\right) {d\theta }.
\]

(*)

> b) La relation (*) permet d'affirmer

b) The relation (*) allows us to state

\[
I\left( T\right)  = \frac{i\pi }{4} - \frac{i}{T}{\int }_{0}^{T}\left\lbrack  {{\int }_{0}^{\pi /4}\exp \left( {i\frac{{t}^{2}}{{\cos }^{2}\theta }}\right) {d\theta }}\right\rbrack  {dt}.
\]

Le théorème de Fubini nous autorise à échanger l'ordre des signes d'intégration (puisqu'on a affaire à l’intégrale sur \( \left\lbrack {0, T}\right\rbrack \times \left\lbrack {0,\pi /4}\right\rbrack ) \) , donc

> Fubini's theorem allows us to exchange the order of the integration signs (since we are dealing with the integral over \( \left\lbrack {0, T}\right\rbrack \times \left\lbrack {0,\pi /4}\right\rbrack ) \) , therefore

\[
I\left( T\right)  = \frac{i\pi }{4} - \frac{i}{T}{\int }_{0}^{\pi /4}\left\lbrack  {{\int }_{0}^{T}\exp \left( {i\frac{{t}^{2}}{{\cos }^{2}\theta }}\right) {dt}}\right\rbrack  {d\theta } = \frac{i\pi }{4} - \frac{i}{T}{\int }_{0}^{\pi /4}\cos {\theta f}\left( \frac{T}{\cos \theta }\right) {d\theta }.
\]

\( \left( {* * * }\right) \)

> Or l’intégrale \( \varphi = {\int }_{0}^{+\infty }{e}^{i{x}^{2}}{dx} \) converge (en effectuant le changement de variable \( u = {x}^{2} \) , on remarque que \( f \) est de même nature que \( {\int }_{0}^{+\infty }\left( {e}^{iu}\right) {u}^{-1/2}{du} \) , qui converge - voir la remarque 6 page 153), donc la fonction \( t \mapsto f\left( t\right) \) est bornée en \( + \infty \) . Avec (***), on en déduit que \( I\left( T\right) \) converge vers \( {i\pi }/4 \) lorsque \( T \rightarrow + \infty \) .

However, the integral \( \varphi = {\int }_{0}^{+\infty }{e}^{i{x}^{2}}{dx} \) converges (by performing the change of variable \( u = {x}^{2} \), we note that \( f \) is of the same nature as \( {\int }_{0}^{+\infty }\left( {e}^{iu}\right) {u}^{-1/2}{du} \), which converges - see remark 6 on page 153), so the function \( t \mapsto f\left( t\right) \) is bounded at \( + \infty \). With (***), we deduce that \( I\left( T\right) \) converges to \( {i\pi }/4 \) as \( T \rightarrow + \infty \).

> Par ailleurs, la première relation trouvée à la question précédente entraîne, pour tout \( T > 0 \) , \( I\left( T\right) = \frac{1}{T}{\int }_{0}^{T}{f}^{2}\left( t\right) {dt} \) . Or la fonction \( t \mapsto {f}^{2}\left( t\right) \) converge vers \( {\varphi }^{2} \) lorsque \( t \rightarrow + \infty \) . On en déduit que \( I\left( T\right) \) converge vers \( {\varphi }^{2} \) lorsque \( T \rightarrow + \infty \) (si une fonction \( \psi \) converge vers \( \alpha \) en \( + \infty \) , sa moyenne de Césaro \( \frac{1}{T}{\int }_{0}^{T}\psi \) converge vers \( \alpha \) ). On en déduit finalement \( {\varphi }^{2} = {i\pi }/4 \) . On a donc déterminé \( \varphi \) au signe près. Or \( s = \Im \left( \varphi \right) = \frac{1}{2}{\int }_{0}^{+\infty }\sin \left( x\right) {x}^{-1/2}{dx} \geq 0 \) car

Furthermore, the first relation found in the previous question implies, for all \( T > 0 \), \( I\left( T\right) = \frac{1}{T}{\int }_{0}^{T}{f}^{2}\left( t\right) {dt} \). However, the function \( t \mapsto {f}^{2}\left( t\right) \) converges to \( {\varphi }^{2} \) as \( t \rightarrow + \infty \). We deduce that \( I\left( T\right) \) converges to \( {\varphi }^{2} \) as \( T \rightarrow + \infty \) (if a function \( \psi \) converges to \( \alpha \) at \( + \infty \), its Cesàro mean \( \frac{1}{T}{\int }_{0}^{T}\psi \) converges to \( \alpha \)). We finally deduce \( {\varphi }^{2} = {i\pi }/4 \). We have therefore determined \( \varphi \) up to the sign. However, \( s = \Im \left( \varphi \right) = \frac{1}{2}{\int }_{0}^{+\infty }\sin \left( x\right) {x}^{-1/2}{dx} \geq 0 \) because

\[
s = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n},\;\text{ où }\;{u}_{n} = {\int }_{2n\pi }^{2\left( {n + 1}\right) \pi }\frac{\sin u}{2\sqrt{u}}{du} = {\int }_{2n\pi }^{\left( {{2n} + 1}\right) \pi }\frac{\sin u}{2}\left( {\frac{1}{\sqrt{u}} - \frac{1}{\sqrt{u + \pi }}}\right) {du} \geq  0,
\]

on en déduit facilement \( \varphi = {e}^{{i\pi }/4}\frac{\sqrt{\pi }}{2} \) .

> we easily deduce \( \varphi = {e}^{{i\pi }/4}\frac{\sqrt{\pi }}{2} \).

Remarque. Un autre moyen de calculer \( \varphi \) est d’utiliser le résultat de la question 2/b) de l'exercice 4 page 168.

> Remark. Another way to calculate \( \varphi \) is to use the result of question 2/b) of exercise 4 on page 168.
