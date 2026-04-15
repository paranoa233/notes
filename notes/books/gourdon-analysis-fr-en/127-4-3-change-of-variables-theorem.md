#### 4.3. Change of variables theorem

*Français : 4.3. Théorème du changement de variable*

Rappel. Soit \( U \) un ouvert de \( {\mathbb{R}}^{n} \) et \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) : U \rightarrow {\mathbb{R}}^{n}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \; \varphi \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) une fonction de classe \( {\mathcal{C}}^{1} \) . Pour tout \( x \in U \) , le jacobien de \( \varphi \) en \( x \) est

> Recall. Let \( U \) be an open set of \( {\mathbb{R}}^{n} \) and \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) : U \rightarrow {\mathbb{R}}^{n}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \; \varphi \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) be a function of class \( {\mathcal{C}}^{1} \) . For any \( x \in U \) , the Jacobian of \( \varphi \) at \( x \) is

\[
J\left( \varphi \right) \left( x\right)  = \det {\left( \frac{\partial {\varphi }_{i}}{\partial {x}_{j}}\left( x\right) \right) }_{1 \leq  i, j \leq  n},\;\text{ également noté }\frac{D\left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) }{D\left( {{x}_{1},\ldots ,{x}_{n}}\right) }.
\]

\( \rightarrow \) THÉORÉME 4 (DU CHANGEMENT DE VARIABLES). Soient \( U \) un ensemble mesurable compact de \( {\mathbb{R}}^{n} \) , et \( \varphi \) un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( U \) sur \( \varphi \left( U\right) \) , tel que \( \varphi \) et son jacobien \( J\left( \varphi \right) \) se prolongent continúment sur \( U \) . Alors \( V = \varphi \left( U\right) \) est un compact mesurable et pour toute fonction continue \( f : V \rightarrow \mathbb{R} \) , on a

> \( \rightarrow \) THEOREM 4 (CHANGE OF VARIABLES). Let \( U \) be a compact measurable set of \( {\mathbb{R}}^{n} \) , and \( \varphi \) be a \( {\mathcal{C}}^{1} \) -diffeomorphism from \( U \) onto \( \varphi \left( U\right) \) , such that \( \varphi \) and its Jacobian \( J\left( \varphi \right) \) extend continuously to \( U \) . Then \( V = \varphi \left( U\right) \) is a compact measurable set and for any continuous function \( f : V \rightarrow \mathbb{R} \) , we have

\[
{\int }_{V}f\left( v\right) {dv} = {\int }_{U}f\left( {\varphi \left( u\right) }\right) \left| {J\left( \varphi \right) \left( u\right) }\right| {du}.
\]

Remarque 6. Le résultat du théorème s'écrit aussi sous la forme

> Remark 6. The result of the theorem can also be written in the form

\[
\int \cdots {\int }_{V}f\left( {{v}_{1},\ldots ,{v}_{n}}\right) d{v}_{1}\cdots d{v}_{n} = \int \cdots {\int }_{U}F\left( {{u}_{1},\ldots ,{u}_{n}}\right) \left| \frac{D\left( {{v}_{1},\ldots ,{v}_{n}}\right) }{D\left( {{u}_{1},\ldots ,{u}_{n}}\right) }\right| d{u}_{1}\cdots d{u}_{n},
\]

où \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) \) désigne \( f\left\lbrack {\varphi \left( {{u}_{1},\ldots ,{u}_{n}}\right) }\right\rbrack \) et où \( \frac{D\left( {{v}_{1},\ldots ,{v}_{n}}\right) }{D\left( {{u}_{1},\ldots ,{u}_{n}}\right) } \) désigne \( \frac{D\left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) }{D\left( {{u}_{1},\ldots ,{u}_{n}}\right) } \) .

> where \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) \) denotes \( f\left\lbrack {\varphi \left( {{u}_{1},\ldots ,{u}_{n}}\right) }\right\rbrack \) and where \( \frac{D\left( {{v}_{1},\ldots ,{v}_{n}}\right) }{D\left( {{u}_{1},\ldots ,{u}_{n}}\right) } \) denotes \( \frac{D\left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) }{D\left( {{u}_{1},\ldots ,{u}_{n}}\right) } \) .

Voyons maintenant les applications les plus courantes du théorème du changement de variable.

> Let us now look at the most common applications of the change of variables theorem.

Passage en coordonnées polaires dans le plan. On se place dans le plan \( {\mathbb{R}}^{2} \) , où on désigne par \( \left( {r,\theta }\right) \in {\mathbb{R}}^{ + } \times \left\lbrack {0,{2\pi }}\right\rbrack \) les coordonnées polaires et \( \left( {x, y}\right) = \left( {r\cos \theta , r\sin \theta }\right) \) les coordonnées cartésiennes. Si un domaine compact quarrable de \( {\mathbb{R}}^{2} \) est représenté par \( D \) en coordonnées cartésiennes et par \( \Delta \) en coordonnées polaires, toute fonction continue \( f \) sur \( D \) vérifie

> Switching to polar coordinates in the plane. We consider the plane \( {\mathbb{R}}^{2} \) , where \( \left( {r,\theta }\right) \in {\mathbb{R}}^{ + } \times \left\lbrack {0,{2\pi }}\right\rbrack \) denotes polar coordinates and \( \left( {x, y}\right) = \left( {r\cos \theta , r\sin \theta }\right) \) denotes Cartesian coordinates. If a compact squarable domain of \( {\mathbb{R}}^{2} \) is represented by \( D \) in Cartesian coordinates and by \( \Delta \) in polar coordinates, any continuous function \( f \) on \( D \) satisfies

\[
{\iint }_{D}f\left( {x, y}\right) {dxdy} = {\iint }_{\Delta }f\left( {r\cos \theta , r\sin \theta }\right) {rdrd\theta }.
\]

En effet, il suffit d'appliquer le théorème du changement de variable et de remarquer que

> Indeed, it suffices to apply the change of variables theorem and note that

\[
\frac{D\left( {x, y}\right) }{D\left( {r,\theta }\right) } = \left| \begin{array}{ll} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta } \\  \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta } \end{array}\right|  = \left| \begin{matrix} \cos \theta &  - r\sin \theta \\  \sin \theta & r\cos \theta  \end{matrix}\right|  = r.
\]

Exemple 2. Comme conséquence de ce résultat, nous allons donner une méthode classique pour calculer l’intégrale de Gauss \( {\int }_{-\infty }^{+\infty }{e}^{-{x}^{2}}{dx} \) . Pour tout \( a > 0 \) , on note

> Example 2. As a consequence of this result, we will provide a classic method for calculating the Gaussian integral \( {\int }_{-\infty }^{+\infty }{e}^{-{x}^{2}}{dx} \) . For any \( a > 0 \) , we denote

\[
{D}_{a} = \left\{  {\left( {x, y}\right)  \in  {\mathbb{R}}^{2} \mid  {x}^{2} + {y}^{2} \leq  {a}^{2}}\right\}  ,\;{C}_{a} = {\left\lbrack  -a, a\right\rbrack  }^{2}\;\text{ et }\;{I}_{a} = {\iint }_{{D}_{a}}{e}^{-\left( {{x}^{2} + {y}^{2}}\right) }{dxdy}.
\]

En passant en coordonnées polaires puis en appliquant le corollaire du théorème de Fubini, on a

> By switching to polar coordinates and then applying the corollary of Fubini's theorem, we have

\[
\forall a > 0,\;{I}_{a} = {\iint }_{\left\lbrack  {0, a}\right\rbrack   \times  \left\lbrack  {0,{2\pi }}\right\rbrack  }{e}^{-{r}^{2}}{rdrd\theta } = \left( {{\int }_{\left\lbrack  0, a\right\rbrack  }{e}^{-{r}^{2}}{rdr}}\right) \left( {{\int }_{\left\lbrack  0,2\pi \right\rbrack  }{d\theta }}\right)  = \pi \left( {1 - {e}^{-{a}^{2}}}\right) .
\]

En notant \( {J}_{a} = {\iint }_{{C}_{a}}{e}^{-\left( {{x}^{2} + {y}^{2}}\right) }{dxdy} \) , on a (toujours d’après le théorème de Fubini),

> By denoting \( {J}_{a} = {\iint }_{{C}_{a}}{e}^{-\left( {{x}^{2} + {y}^{2}}\right) }{dxdy} \), we have (still according to Fubini's theorem),

\[
{J}_{a} = \left( {{\int }_{\left\lbrack  -a, a\right\rbrack  }{e}^{-{x}^{2}}{dx}}\right) \left( {{\int }_{\left\lbrack  -a, a\right\rbrack  }{e}^{-{y}^{2}}{dy}}\right)  = {\left( {\int }_{-a}^{a}{e}^{-{x}^{2}}dx\right) }^{2}.
\]

Or \( {D}_{a} \subset {C}_{a} \subset {D}_{\sqrt{2}a} \) , et la fonction intégrée étant positive, on en déduit \( {I}_{a} \leq {J}_{a} \leq {J}_{\sqrt{2}a} \) , ce qui s'écrit encore

> However \( {D}_{a} \subset {C}_{a} \subset {D}_{\sqrt{2}a} \), and since the integrand is positive, we deduce \( {I}_{a} \leq {J}_{a} \leq {J}_{\sqrt{2}a} \), which can also be written

\[
\forall a > 0,\;\pi \left( {1 - {e}^{-{a}^{2}}}\right)  \leq  {\left( {\int }_{-a}^{a}{e}^{-{x}^{2}}dx\right) }^{2} \leq  \pi \left( {1 - {e}^{-2{a}^{2}}}\right) .
\]

En faisant tendre \( a \) vers \( + \infty \) , on en déduit \( {\int }_{-\infty }^{+\infty }{e}^{-{x}^{2}}{dx} = \sqrt{\pi } \) .

> By letting \( a \) tend towards \( + \infty \), we deduce \( {\int }_{-\infty }^{+\infty }{e}^{-{x}^{2}}{dx} = \sqrt{\pi } \).

Passage en coordonnées cylindriques dans l'espace. Nous nous plaçons dans l'espace \( {\mathbb{R}}^{3} \) , dans lequel on écrit \( \left( {x, y, z}\right) = \left( {r\cos \theta , r\sin \theta , z}\right) \) avec \( r \geq 0 \) et \( \theta \in \left\lbrack {0,{2\pi }}\right\rbrack \) . Avec les notations précédentes, on a

> Switching to cylindrical coordinates in space. We consider the space \( {\mathbb{R}}^{3} \), in which we write \( \left( {x, y, z}\right) = \left( {r\cos \theta , r\sin \theta , z}\right) \) with \( r \geq 0 \) and \( \theta \in \left\lbrack {0,{2\pi }}\right\rbrack \). With the previous notations, we have

\[
{\iiint }_{D}f\left( {x, y, z}\right) {dxdydz} = {\iiint }_{\Delta }f\left( {r\cos \theta , r\sin \theta , z}\right) {rdrd\theta dz}.
\]

Passage en coordonnées sphériques dans l'espace. On écrit

> Switching to spherical coordinates in space. We write

\[
\left\{  \begin{array}{l} x = r\cos \varphi \cos \theta \\  y = r\cos \varphi \sin \theta \\  z = r\sin \varphi  \end{array}\right. ,\;r \geq  0,\;\theta  \in  \left\lbrack  {0,{2\pi }}\right\rbrack  ,\;\varphi  \in  \left\lbrack  {-\frac{\pi }{2},\frac{\pi }{2}}\right\rbrack  .
\]

Après calcul du jacobien, on obtient

> After calculating the Jacobian, we obtain

\[
{\iiint }_{D}f\left( {x, y, z}\right) {dxdydz} = {\iiint }_{\Delta }f\left( {r\cos \varphi \cos \theta , r\cos \varphi \sin \theta , r\sin \varphi }\right) {r}^{2}\cos {\varphi drd\varphi d\theta }.
\]
