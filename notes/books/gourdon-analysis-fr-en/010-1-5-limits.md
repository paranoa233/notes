#### 1.5. Limits

*Français : 1.5. Limites*

DéFINITION 21. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques et une application \( f : D \subset \; E \rightarrow F \) . Soient \( A \subset D \) et \( a \in \bar{A},\ell \in F \) . On dit que \( f\left( x\right) \) tend vers \( \ell \) quand \( x \) tend vers a selon \( A \) , et on note \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = \ell \) , si pour tout voisinage \( W \) de \( \ell \) , il existe un voisinage \( V \) de \( a \) tel que \( f\left( {A \cap V}\right) \subset W \) . Ceci s’écrit aussi

> DEFINITION 21. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces and a map \( f : D \subset \; E \rightarrow F \) . Let \( A \subset D \) and \( a \in \bar{A},\ell \in F \) . We say that \( f\left( x\right) \) tends to \( \ell \) as \( x \) tends to a along \( A \) , and we denote it \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = \ell \) , if for every neighborhood \( W \) of \( \ell \) , there exists a neighborhood \( V \) of \( a \) such that \( f\left( {A \cap V}\right) \subset W \) . This is also written

\[
\forall \varepsilon  > 0,\exists \alpha  > 0\text{ tel que }\forall x \in  A\text{ vérifiant }\mathrm{d}\left( {a, x}\right)  < \alpha ,\;\text{ on a }\;\delta \left( {f\left( x\right) ,\ell }\right)  < \varepsilon .
\]

Remarque 17. Si \( \ell \) existe, \( \ell \) est unique et on a \( \ell \in \overline{f\left( A\right) };\ell \) est alors appelée la limite de \( f \) en a selon \( A \) .

> Remark 17. If \( \ell \) exists, \( \ell \) is unique and we have \( \ell \in \overline{f\left( A\right) };\ell \) is then called the limit of \( f \) at a along \( A \) .

Exemple 12. - Limite usuelle. Si a est point d’accumulation de \( D \) , si \( A = D \smallsetminus \{ a\} \) , \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }} \) est encore noté \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }} \) .

> Example 12. - Usual limit. If a is an accumulation point of \( D \) , if \( A = D \smallsetminus \{ a\} \) , \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }} \) is also denoted \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }} \) .

- Limite \( \dot{a} \) gauche. Soit \( f \) une fonction de la variable réelle \( x \in  I \) , et \( a \in  \bar{I} \) . Lorsque \( A = \rbrack  - \infty , a\lbrack  \cap  I \) , la limite \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x \in  A} }}f\left( x\right) \) , si elle existe, est encore notée \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x < a} }}f\left( x\right) \) (ou \( \mathop{\lim }\limits_{{x \rightarrow  {a}^{ - }}}f\left( x\right) \) , ou encore \( f\left( {a - }\right) ) \) et appelée limite à gauche de \( f \) en \( a \) . On définit de même lim \( f\left( x\right) \) (encore notée \( \mathop{\lim }\limits_{{x \rightarrow  {a}^{ + }}}f\left( x\right) \) ou \( f\left( {a + }\right) \) ) la limite à droite de \( f \) en \( a \) .

> - Left \( \dot{a} \) limit. Let \( f \) be a function of the real variable \( x \in  I \) , and \( a \in  \bar{I} \) . As \( A = \rbrack  - \infty , a\lbrack  \cap  I \) , the limit \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x \in  A} }}f\left( x\right) \) , if it exists, is also denoted \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x < a} }}f\left( x\right) \) (or \( \mathop{\lim }\limits_{{x \rightarrow  {a}^{ - }}}f\left( x\right) \) , or even \( f\left( {a - }\right) ) \) and called the left-hand limit of \( f \) at \( a \) . We similarly define lim \( f\left( x\right) \) (also denoted \( \mathop{\lim }\limits_{{x \rightarrow  {a}^{ + }}}f\left( x\right) \) or \( f\left( {a + }\right) \) ) the right-hand limit of \( f \) at \( a \) .

- Limite en \( + \infty \) . On note \( \overline{\mathbb{R}} \) l’ensemble \( \mathbb{R} \cup  \{  - \infty , + \infty \} \) (cet ensemble est appelé \( \mathbb{R} \) achevé). Sur \( \overline{\mathbb{R}} \) , on définit

> - Limit at \( + \infty \) . We denote \( \overline{\mathbb{R}} \) the set \( \mathbb{R} \cup  \{  - \infty , + \infty \} \) (this set is called the extended \( \mathbb{R} \) ). On \( \overline{\mathbb{R}} \) , we define

\[
\varphi \left( x\right)  = \frac{x}{1 + \left| x\right| }\;\text{ si }\;x \in  \mathbb{R},\;\varphi \left( {+\infty }\right)  = 1,\varphi \left( {-\infty }\right)  =  - 1.
\]

On vérifie facilement que \( \mathrm{d}\left( {x, y}\right) = \left| {\varphi \left( x\right) - \varphi \left( y\right) }\right| \) définit une distance sur \( \overline{\mathbb{R}} \) . Cette distance fait de \( \overline{\mathbb{R}} \) un espace métrique et nous autorise à parler de limite en \( + \infty \) ou en \( - \infty \) . Lorsqu’une fonction de la variable réelle \( f \) est définie sur \( \rbrack c, + \infty \lbrack \) , il est évidemment très lourd de caractériser la limite de \( f \) en \( + \infty \) grâce à la distance d sur \( \overline{\mathbb{R}} \) . On montre facilement que \( f\left( x\right) \) tend vers \( \ell \) en \( + \infty \) si et seulement si

> It is easy to verify that \( \mathrm{d}\left( {x, y}\right) = \left| {\varphi \left( x\right) - \varphi \left( y\right) }\right| \) defines a distance on \( \overline{\mathbb{R}} \) . This distance makes \( \overline{\mathbb{R}} \) a metric space and allows us to speak of a limit at \( + \infty \) or at \( - \infty \) . When a function of the real variable \( f \) is defined on \( \rbrack c, + \infty \lbrack \) , it is obviously very cumbersome to characterize the limit of \( f \) at \( + \infty \) using the distance d on \( \overline{\mathbb{R}} \) . It is easily shown that \( f\left( x\right) \) tends to \( \ell \) at \( + \infty \) if and only if

\[
\left( {\forall \varepsilon  > 0,\exists C > c,\forall x > C}\right) ,\;\mathrm{d}\left( {f\left( x\right) ,\ell }\right)  < \varepsilon ,
\]

et on note alors \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) = \ell \) . On caractériserait de même la limite en \( - \infty \) . Noter que l’on peut de la même manière caractériser la limite d’une suite \( \mathbb{N} \rightarrow \; \left( {E,\mathrm{\;d}}\right) \) en \( + \infty \) .

> and we then denote it \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}f\left( x\right) = \ell \) . The limit at \( - \infty \) could be characterized in the same way. Note that the limit of a sequence \( \mathbb{N} \rightarrow \; \left( {E,\mathrm{\;d}}\right) \) at \( + \infty \) can be characterized in the same manner.

- Limite infinie. Lorsqu’une fonction \( f \) est à valeurs réelles, il est possible de caractériser simplement les limites infinies de \( f \) . Par exemple, \( f \) tend vers \( + \infty \) lorsque \( x \) tend vers \( a \) selon \( A \) si et seulement si

> - Infinite limit. When a function \( f \) is real-valued, it is possible to simply characterize the infinite limits of \( f \) . For example, \( f \) tends to \( + \infty \) as \( x \) tends to \( a \) along \( A \) if and only if

\[
\left( {\forall C > 0,\exists \alpha  > 0,\forall x \in  A}\right) ,\;\left( {\mathrm{d}\left( {a, x}\right)  < \alpha  \Rightarrow  f\left( x\right)  > C}\right) .
\]

On note alors \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = + \infty \) .

> We then denote it \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = + \infty \) .

- Le lecteur pourra de même caractériser simplement une limite infinie prise à l'infini.

> - The reader may similarly characterize an infinite limit taken at infinity.

##### Composition of limits.

*Français : Composition des limites.*

Proposition 18. Soient \( f : {D}_{1} \subset \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) et \( g : {D}_{2} \subset \left( {F,{\mathrm{\;d}}^{\prime }}\right) \rightarrow \left( {G,{\mathrm{\;d}}^{\prime \prime }}\right) \) telles que \( f\left( {D}_{1}\right) \subset {D}_{2} \) . Soient \( A \subset {D}_{1}, a \in \bar{A};B \subset {D}_{2} \) et \( b \in \bar{B} \) . On suppose que

> Proposition 18. Let \( f : {D}_{1} \subset \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) and \( g : {D}_{2} \subset \left( {F,{\mathrm{\;d}}^{\prime }}\right) \rightarrow \left( {G,{\mathrm{\;d}}^{\prime \prime }}\right) \) be such that \( f\left( {D}_{1}\right) \subset {D}_{2} \) . Let \( A \subset {D}_{1}, a \in \bar{A};B \subset {D}_{2} \) and \( b \in \bar{B} \) . We assume that

\[
f\left( A\right)  \subset  B,\;\mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x \in  A} }}f\left( x\right)  = b\;\text{ et }\;\mathop{\lim }\limits_{\substack{{y \rightarrow  b} \\  {y \in  B} }}g\left( y\right)  = c.
\]

Alors l’application composée \( h = g \circ f \) vérifie \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}h\left( x\right) = c \) .

> Then the composed map \( h = g \circ f \) satisfies \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}h\left( x\right) = c \) .

Proposition 19. Soient \( f, g : D \subset \left( {E,\mathrm{\;d}}\right) \rightarrow F \) , où \( F \) est un \( \mathbb{K} \) e.v.n \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) . Soient \( A \subset D \) et \( a \in \bar{A} \) . On suppose \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = \ell \) et \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}g\left( x\right) = {\ell }^{\prime } \) . Alors, lorsque \( x \) tend vers a selon \( A \) ,

> Proposition 19. Let \( f, g : D \subset \left( {E,\mathrm{\;d}}\right) \rightarrow F \) , where \( F \) is a \( \mathbb{K} \) n.v.s \( \left( {\mathbb{K} = \mathbb{R}\text{ ou }\mathbb{C}}\right) \) . Let \( A \subset D \) and \( a \in \bar{A} \) . We assume \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}f\left( x\right) = \ell \) and \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \in A} }}g\left( x\right) = {\ell }^{\prime } \) . Then, as \( x \) tends to a along \( A \) ,

(i) \( \left( {f + g}\right) \left( x\right) \) tend vers \( \ell + {\ell }^{\prime } \) ,

> (i) \( \left( {f + g}\right) \left( x\right) \) converges to \( \ell + {\ell }^{\prime } \) ,

(ii) pour tout \( \lambda \in \mathbb{K},\left( {\lambda f}\right) \left( x\right) \) tend vers \( \lambda \ell \) ,

> (ii) for all \( \lambda \in \mathbb{K},\left( {\lambda f}\right) \left( x\right) \) converges to \( \lambda \ell \) ,

(iii) \( \parallel f\left( x\right) \parallel \) tend vers \( \parallel \ell \parallel \) ,

> (iii) \( \parallel f\left( x\right) \parallel \) converges to \( \parallel \ell \parallel \) ,

(iv) si F est une algèbre normée, \( \left( {fg}\right) \left( x\right) \) tend vers \( \ell {\ell }^{\prime } \) ,

> (iv) if F is a normed algebra, \( \left( {fg}\right) \left( x\right) \) converges to \( \ell {\ell }^{\prime } \) ,

(v) si \( F = \mathbb{R} \) et si \( f\left( x\right) \leq g\left( x\right) \) sur un voisinage de a dans \( A,\ell \leq {\ell }^{\prime } \) ,

> (v) if \( F = \mathbb{R} \) and if \( f\left( x\right) \leq g\left( x\right) \) on a neighborhood of a in \( A,\ell \leq {\ell }^{\prime } \) ,

(vi) si \( F = \mathbb{R} \) , si pour une fonction \( h : \;D \rightarrow \mathbb{R} \) on a \( f\left( x\right) \leq h\left( x\right) \leq g\left( x\right) \) dans un voisinage de a dans \( A \) et si \( \ell = {\ell }^{\prime } \) , alors \( h\left( x\right) \) tend vers \( \ell \) .

> (vi) if \( F = \mathbb{R} \) , if for a function \( h : \;D \rightarrow \mathbb{R} \) we have \( f\left( x\right) \leq h\left( x\right) \leq g\left( x\right) \) in a neighborhood of a in \( A \) and if \( \ell = {\ell }^{\prime } \) , then \( h\left( x\right) \) converges to \( \ell \) .

##### Limit and continuity at a point.

*Français : Limite et continuité en un point.*

Proposition 20. Soient \( f : D \subset \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) et \( a \in D \) un point d’accumulation de D. L’application \( f \) est continue en a si et seulement si \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) = f\left( a\right) \) .

> Proposition 20. Let \( f : D \subset \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) and \( a \in D \) be an accumulation point of D. The map \( f \) is continuous at a if and only if \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) = f\left( a\right) \) .

Remarque 18. Lorsque \( f \) n’est pas définie en \( a \) et lorsque \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) = \ell \) , la fonction \( g \) définie sur \( D \cup \{ a\} \) par \( g\left( x\right) = f\left( x\right) \) sur \( D \) et \( g\left( a\right) = \ell \) est continue en \( a \) et est appelée prolongement par continuité de \( f \) en a.

> Remark 18. When \( f \) is not defined at \( a \) and when \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) = \ell \) , the function \( g \) defined on \( D \cup \{ a\} \) by \( g\left( x\right) = f\left( x\right) \) on \( D \) and \( g\left( a\right) = \ell \) is continuous at \( a \) and is called the continuous extension of \( f \) at a.

DéFINITION 22. Soit \( f : D \subset \mathbb{R} \rightarrow \left( {E,\mathrm{\;d}}\right) \) et \( a \in \overset{ \circ }{D} \) . On dit que

> DEFINITION 22. Let \( f : D \subset \mathbb{R} \rightarrow \left( {E,\mathrm{\;d}}\right) \) and \( a \in \overset{ \circ }{D} \) . We say that

- \( f \) est continue à droite en \( a \) si \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x > a} }}f\left( x\right)  = f\left( a\right) \) .

> - \( f \) is right-continuous at \( a \) if \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x > a} }}f\left( x\right)  = f\left( a\right) \) .

- \( f \) est continue à gauche en \( a \) si \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x < a} }}f\left( x\right)  = f\left( a\right) \) .

> - \( f \) is left-continuous at \( a \) if \( \mathop{\lim }\limits_{\substack{{x \rightarrow  a} \\  {x < a} }}f\left( x\right)  = f\left( a\right) \) .

On dit que \( f \) présente une discontinuité de première espèce en \( a \) si \( {\ell }_{g} = \mathop{\lim }\limits_{{x \rightarrow a}}f\left( x\right) \) et \( {\ell }_{d} = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x > a} }}f\left( x\right) \) existent, et si \( {\ell }_{g} \neq {\ell }_{d} \) .

> We say that \( f \) has a jump discontinuity at \( a \) if \( {\ell }_{g} = \mathop{\lim }\limits_{{x \rightarrow a}}f\left( x\right) \) and \( {\ell }_{d} = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x > a} }}f\left( x\right) \) exist, and if \( {\ell }_{g} \neq {\ell }_{d} \) .
