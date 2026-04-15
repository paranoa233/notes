#### 1.4. Results on differentiability for functions with values in a n.v.s.

*Français : 1.4. Résultats relatifs à la dérivabilité pour les fonctions à valeurs dans un e.v.n*

Dans toute cette partie, \( E \) désigne un \( \mathbb{R} \) -e.v normé.

> Throughout this section, \( E \) denotes a normed \( \mathbb{R} \) -v.s.

Lorsque les applications sont à valeurs dans un \( \mathbb{R} \) -e.v.n, les formules de Taylor du paragraphe précédent ne sont plus vraies (voir par exemple la remarque 2). Par contre, il existe des résultats analogues faisant intervenir des inégalités. Le théorème qui suit est une inégalité fondamentale dont nous nous servirons beaucoup.

> When the mappings take values in a \( \mathbb{R} \) -n.v.s., the Taylor formulas from the previous paragraph are no longer true (see for example remark 2). However, there are analogous results involving inequalities. The following theorem is a fundamental inequality that we will use extensively.

THÉOREME 5. Soient \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) et \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) deux applications continues sur \( \left\lbrack {a, b}\right\rbrack \) , dérivables sur \( \rbrack a, b\left\lbrack {.{Si}\text{ pour tout }t \in }\right\rbrack a, b\left\lbrack \right. \) , on a \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \leq {g}^{\prime }\left( t\right) \) , alors \( \parallel F\left( b\right) - \; F\left( a\right) \parallel \leq g\left( b\right) - g\left( a\right) . \)

> THEOREM 5. Let \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) and \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be two continuous functions on \( \left\lbrack {a, b}\right\rbrack \) , differentiable on \( \rbrack a, b\left\lbrack {.{Si}\text{ pour tout }t \in }\right\rbrack a, b\left\lbrack \right. \) , we have \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \leq {g}^{\prime }\left( t\right) \) , then \( \parallel F\left( b\right) - \; F\left( a\right) \parallel \leq g\left( b\right) - g\left( a\right) . \)

Démonstration. Supposons dans un premier temps que \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < {g}^{\prime }\left( t\right) \) pour tout \( t \in \rbrack a, b\lbrack \) . Pour tout \( x \in \rbrack a, b\left\lbrack \right. \) , on a \( \mathop{\lim }\limits_{\substack{{t \rightarrow x} \\ {t > x} }}\begin{Vmatrix}\frac{F\left( t\right) - F\left( x\right) }{t - x}\end{Vmatrix} = \frac{g\left( t\right) - g\left( x\right) }{t - x} < 0 \) , donc

> Proof. Assume first that \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < {g}^{\prime }\left( t\right) \) for all \( t \in \rbrack a, b\lbrack \) . For all \( x \in \rbrack a, b\left\lbrack \right. \) , we have \( \mathop{\lim }\limits_{\substack{{t \rightarrow x} \\ {t > x} }}\begin{Vmatrix}\frac{F\left( t\right) - F\left( x\right) }{t - x}\end{Vmatrix} = \frac{g\left( t\right) - g\left( x\right) }{t - x} < 0 \) , therefore

\[
\forall x \in  \rbrack a, b\left\lbrack  {,\exists y > x,\forall t \in  }\right\rbrack  x, y\left\lbrack  {,\;\begin{Vmatrix}\frac{F\left( t\right)  - F\left( x\right) }{t - x}\end{Vmatrix} < \frac{g\left( t\right)  - g\left( x\right) }{t - x}}\right.
\]

de sorte que

> so that

\[
\forall x \in  \rbrack a, b\lbrack ,\exists y > x,\forall t \in  \left\lbrack  {x, y}\right\rbrack  ,\;\parallel F\left( t\right)  - F\left( x\right) \parallel  \leq  g\left( t\right)  - g\left( x\right) .
\]

(*)

> Soit \( \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \) et montrons

Let \( \left\lbrack {\alpha ,\beta }\right\rbrack \subset \rbrack a, b\lbrack \) and let us show

\[
\parallel F\left( \beta \right)  - F\left( \alpha \right) \parallel  \leq  g\left( \beta \right)  - g\left( \alpha \right) .
\]

\( \left( {* * }\right) \)

> Soit \( \Gamma = \{ \theta \in \rbrack \alpha ,\beta \rbrack ,\forall t \in \left\lbrack {\alpha ,\theta }\right\rbrack ,\parallel F\left( t\right) - F\left( \alpha \right) \parallel \leq g\left( t\right) - g\left( \alpha \right) \} \) . D’après (*), \( \Gamma \) est non vide. Soit \( \gamma = \sup \Gamma \) . Montrons \( \gamma = \beta \) , ce qui prouvera (**). Par continuité de \( F \) et \( g \) , on a \( \parallel F\left( \gamma \right) - F\left( \alpha \right) \parallel \leq \; g\left( \gamma \right) - g\left( \alpha \right) \) . Si \( \gamma < \beta \) , d’après (*),

Let \( \Gamma = \{ \theta \in \rbrack \alpha ,\beta \rbrack ,\forall t \in \left\lbrack {\alpha ,\theta }\right\rbrack ,\parallel F\left( t\right) - F\left( \alpha \right) \parallel \leq g\left( t\right) - g\left( \alpha \right) \} \) . According to (*), \( \Gamma \) is non-empty. Let \( \gamma = \sup \Gamma \) . Let us show \( \gamma = \beta \) , which will prove (**). By continuity of \( F \) and \( g \) , we have \( \parallel F\left( \gamma \right) - F\left( \alpha \right) \parallel \leq \; g\left( \gamma \right) - g\left( \alpha \right) \) . If \( \gamma < \beta \) , according to (*),

\[
\exists \delta  \in  \rbrack \gamma ,\beta \rbrack ,\forall t \in  \left\lbrack  {\gamma ,\delta }\right\rbrack  ,\;\parallel F\left( t\right)  - F\left( \gamma \right) \parallel  \leq  g\left( t\right)  - g\left( \gamma \right) ,
\]

donc

> therefore

\[
\forall t \in  \left\lbrack  {\gamma ,\delta }\right\rbrack  ,\;\parallel F\left( t\right)  - F\left( \alpha \right) \parallel  \leq  \parallel F\left( t\right)  - F\left( \gamma \right) \parallel  + \parallel F\left( \gamma \right)  - F\left( \alpha \right) \parallel  \leq  g\left( t\right)  - g\left( \alpha \right) .
\]

Ceci montre que \( \delta \in \Gamma \) , ce qui est absurde car \( \delta > \gamma = \sup \Gamma \) .

> This shows that \( \delta \in \Gamma \) , which is absurd because \( \delta > \gamma = \sup \Gamma \) .

L’assertion (**) est donc prouvée. En faisant tendre \( \alpha \) vers \( a \) puis \( \beta \) vers \( b \) , on en déduit, en vertu de la continuité de \( F \) et \( g \) , l’inégalité \( \parallel F\left( b\right) - F\left( a\right) \parallel \leq g\left( b\right) - g\left( a\right) \) .

> Assertion (**) is thus proven. By letting \( \alpha \) tend to \( a \) then \( \beta \) tend to \( b \) , we deduce, by virtue of the continuity of \( F \) and \( g \) , the inequality \( \parallel F\left( b\right) - F\left( a\right) \parallel \leq g\left( b\right) - g\left( a\right) \) .

- Ramenons nous au cas général. Pour tout \( \varepsilon  > 0 \) , on définit \( {g}_{\varepsilon }\left( t\right)  = g\left( t\right)  + {\varepsilon t} \) . Pour tout \( \varepsilon  > 0 \) , on a \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < {g}_{\varepsilon }\left( t\right) \) sur \( \rbrack a, b\lbrack \) , donc d’après ce que l’on vient de prouver, \( \parallel F\left( b\right)  - F\left( a\right) \parallel  \leq \; {g}_{\varepsilon }\left( b\right)  - {g}_{\varepsilon }\left( a\right) \) , d’où le résultat en faisant tendre \( \varepsilon \) vers 0 .

> - Let us reduce to the general case. For all \( \varepsilon  > 0 \), we define \( {g}_{\varepsilon }\left( t\right)  = g\left( t\right)  + {\varepsilon t} \). For all \( \varepsilon  > 0 \), we have \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < {g}_{\varepsilon }\left( t\right) \) on \( \rbrack a, b\lbrack \), so according to what we have just proven, \( \parallel F\left( b\right)  - F\left( a\right) \parallel  \leq \; {g}_{\varepsilon }\left( b\right)  - {g}_{\varepsilon }\left( a\right) \), hence the result by letting \( \varepsilon \) tend to 0.

Remarque 5. Lorsque \( F \) et \( g \) sont de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {a, b}\right\rbrack \) , le résultat s’obtient facilement par intégration, en écrivant \( \parallel F\left( b\right) - F\left( a\right) \parallel = \begin{Vmatrix}{{\int }_{a}^{b}{F}^{\prime }}\end{Vmatrix} \leq {\int }_{a}^{b}\begin{Vmatrix}{F}^{\prime }\end{Vmatrix} \leq {\int }_{a}^{b}{g}^{\prime } = g\left( b\right) - g\left( a\right) \) .

> Remark 5. When \( F \) and \( g \) are of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {a, b}\right\rbrack \), the result is easily obtained by integration, by writing \( \parallel F\left( b\right) - F\left( a\right) \parallel = \begin{Vmatrix}{{\int }_{a}^{b}{F}^{\prime }}\end{Vmatrix} \leq {\int }_{a}^{b}\begin{Vmatrix}{F}^{\prime }\end{Vmatrix} \leq {\int }_{a}^{b}{g}^{\prime } = g\left( b\right) - g\left( a\right) \).

THÉORÉME 6 (INÉGALITÉ DES ACCROISSEMENTS FINIS). Soit \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application continue sur \( \left\lbrack {a, b}\right\rbrack \) , dérivable sur \( \rbrack a, b\lbrack \) . S’il existe \( M > 0 \) tel que \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \leq M \) pour tout \( t \in \rbrack a, b\left\lbrack \right. \) , alors \( \parallel F\left( b\right) - F\left( a\right) \parallel \leq M\left( {b - a}\right) \) .

> THEOREM 6 (MEAN VALUE INEQUALITY). Let \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a continuous mapping on \( \left\lbrack {a, b}\right\rbrack \), differentiable on \( \rbrack a, b\lbrack \). If there exists \( M > 0 \) such that \( \begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \leq M \) for all \( t \in \rbrack a, b\left\lbrack \right. \), then \( \parallel F\left( b\right) - F\left( a\right) \parallel \leq M\left( {b - a}\right) \).

Démonstration. Il suffit d’appliquer le résultat précédent avec \( g\left( t\right) = {Mt} \) .

> Proof. It suffices to apply the previous result with \( g\left( t\right) = {Mt} \).

Remarque 6. Dans le cas d'une fonction à valeurs réelles, cette inégalité s'obtient direc-tement à partir de l'égalité des accroissements, sans utiliser le théorème précédent.

> Remark 6. In the case of a real-valued function, this inequality is obtained directly from the mean value theorem, without using the previous theorem.

Une conséquence importante de l'inégalité des accroissements finis est la suivante.

> An important consequence of the mean value inequality is the following.

\( \rightarrow \) Proposition 6. Soit \( F : \left\lbrack {a, b\lbrack \rightarrow E}\right. \) une application continue, dérivable sur \( \rbrack a, b\lbrack \) et telle que \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x > a} }}{F}^{\prime }\left( t\right) \) existe. Alors \( F \) est dérivable en a et \( {F}^{\prime }\left( a\right) = \ell \) .

> \( \rightarrow \) Proposition 6. Let \( F : \left\lbrack {a, b\lbrack \rightarrow E}\right. \) be a continuous mapping, differentiable on \( \rbrack a, b\lbrack \) and such that \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x > a} }}{F}^{\prime }\left( t\right) \) exists. Then \( F \) is differentiable at a and \( {F}^{\prime }\left( a\right) = \ell \).

Démonstration. Quitte à changer \( F \) en \( F\left( t\right) - t\ell \) on peut supposer \( \ell = 0 \) . Soit \( \varepsilon > 0 \) . Par hypothèse, il existe \( c \in \rbrack a, b\left\lbrack \right. \) tel que \( \left. {\begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < \varepsilon }\right\rbrack \) pour tout \( t \in \rbrack a, c\lbrack \) . L’inégalité des accroissements finis entraîne

> Proof. By replacing \( F \) with \( F\left( t\right) - t\ell \) we may assume \( \ell = 0 \) . Let \( \varepsilon > 0 \) . By hypothesis, there exists \( c \in \rbrack a, b\left\lbrack \right. \) such that \( \left. {\begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} < \varepsilon }\right\rbrack \) for all \( t \in \rbrack a, c\lbrack \) . The mean value inequality implies

\[
\forall t \in  \rbrack a, c\lbrack ,\;\begin{Vmatrix}\frac{F\left( t\right)  - F\left( a\right) }{t - a}\end{Vmatrix} \leq  \varepsilon .
\]

Ceci étant possible pour tout \( \varepsilon > 0 \) , on en déduit que \( \left\lbrack {F\left( t\right) - F\left( a\right) }\right\rbrack /\left( {t - a}\right) \) converge vers 0 lorsque \( t \) tend vers \( a, \) d’où le résultat.

> Since this is possible for any \( \varepsilon > 0 \) , we deduce that \( \left\lbrack {F\left( t\right) - F\left( a\right) }\right\rbrack /\left( {t - a}\right) \) converges to 0 as \( t \) tends to \( a, \) , hence the result.

Remarque 7. En plus de l’existence de \( {F}^{\prime }\left( a\right) \) , la proposition montre que la fonction dérivée \( {F}^{\prime } \) est continue en \( a \) .

> Remark 7. In addition to the existence of \( {F}^{\prime }\left( a\right) \) , the proposition shows that the derivative function \( {F}^{\prime } \) is continuous at \( a \) .

THÉORÉME 7 (INÉGALITÉ DE TAYLOR-LAGRANGE). Soit \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application de classe \( {\mathcal{C}}^{n} \) sur \( \left\lbrack {a, b}\right\rbrack , n + 1 \) fois dérivable sur \( \rbrack a, b\lbrack \) . On suppose qu’il existe \( M > 0 \) tel que \( \forall t \in \rbrack a, b\left\lbrack {,\begin{Vmatrix}{{F}^{\left( n + 1\right) }\left( t\right) }\end{Vmatrix} \leq M}\right. \) . Alors

> THEOREM 7 (TAYLOR-LAGRANGE INEQUALITY). Let \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) be a mapping of class \( {\mathcal{C}}^{n} \) on \( \left\lbrack {a, b}\right\rbrack , n + 1 \) and differentiable on \( \rbrack a, b\lbrack \) . Suppose there exists \( M > 0 \) such that \( \forall t \in \rbrack a, b\left\lbrack {,\begin{Vmatrix}{{F}^{\left( n + 1\right) }\left( t\right) }\end{Vmatrix} \leq M}\right. \) . Then

\[
\begin{Vmatrix}{F\left( b\right)  - F\left( a\right)  - \left( {b - a}\right) {F}^{\prime }\left( a\right)  - \cdots  - \frac{{\left( b - a\right) }^{n}}{n!}{F}^{\left( n\right) }\left( a\right) }\end{Vmatrix} \leq  M\frac{{\left( b - a\right) }^{n + 1}}{\left( {n + 1}\right) !}.
\]

Démonstration. Il suffit d'appliquer le théorème 5 aux fonctions

> Proof. It suffices to apply theorem 5 to the functions

\[
G\left( x\right)  = F\left( b\right)  - F\left( x\right)  - \left( {b - x}\right) {F}^{\prime }\left( x\right)  - \cdots  - \frac{{\left( b - x\right) }^{n}}{n!}{F}^{\left( n\right) }\left( x\right) \;\text{ et }\;g\left( x\right)  =  - M\frac{{\left( b - x\right) }^{n + 1}}{\left( {n + 1}\right) !}.
\]

\( \rightarrow \) THÉORÉME 8 (FORMULE DE TAYLOR-YOUNG). Soient \( n \in \mathbb{N} \) et \( F \) une fonction définie sur un intervalle \( I \) de \( \mathbb{R} \) ,à valeurs dans \( E \) , de classe \( {\mathcal{C}}^{n} \) sur \( I \) . Soit a \( \in I \) tel que \( {F}^{\left( n + 1\right) }\left( a\right) \) existe. Alors, lorsque \( h \rightarrow 0 \) on a

> \( \rightarrow \) THEOREM 8 (TAYLOR-YOUNG FORMULA). Let \( n \in \mathbb{N} \) and \( F \) be a function defined on an interval \( I \) of \( \mathbb{R} \) , with values in \( E \) , of class \( {\mathcal{C}}^{n} \) on \( I \) . Let a \( \in I \) such that \( {F}^{\left( n + 1\right) }\left( a\right) \) exists. Then, as \( h \rightarrow 0 \) we have

\[
F\left( {a + h}\right)  = F\left( a\right)  + h{F}^{\prime }\left( a\right)  + \cdots  + \frac{{h}^{n}}{n!}{F}^{\left( n\right) }\left( a\right)  + \frac{{h}^{n + 1}}{\left( {n + 1}\right) !}{F}^{\left( n + 1\right) }\left( a\right)  + o\left( {h}^{n + 1}\right) .
\]

Démonstration. On procède par récurrence sur \( n \in \mathbb{N} \) . Pour \( n = 0 \) , la formule \( F\left( {a + h}\right) = \; F\left( a\right) + h{F}^{\prime }\left( a\right) + o\left( h\right) \) résulte de la définition de \( {F}^{\prime }\left( a\right) \) . Supposons le résultat vrai au rang \( n - 1 \) , ce qui entraîne (en l’appliquant à \( {F}^{\prime } \) )

> Proof. We proceed by induction on \( n \in \mathbb{N} \) . For \( n = 0 \) , the formula \( F\left( {a + h}\right) = \; F\left( a\right) + h{F}^{\prime }\left( a\right) + o\left( h\right) \) follows from the definition of \( {F}^{\prime }\left( a\right) \) . Assume the result is true at rank \( n - 1 \) , which implies (by applying it to \( {F}^{\prime } \) )

\[
G\left( h\right)  = {F}^{\prime }\left( {a + h}\right)  - {F}^{\prime }\left( a\right)  - h{F}^{\prime \prime }\left( a\right)  - \cdots  - \frac{{h}^{n}}{n!}{F}^{\left( n + 1\right) }\left( a\right)  = o\left( {h}^{n}\right) ,
\]

et montrons le au rang \( n \) . La fonction \( G \) est la dérivée de l’application

> and let us show it at rank \( n \) . The function \( G \) is the derivative of the mapping

\[
H\left( h\right)  = F\left( {a + h}\right)  - F\left( a\right)  - h{F}^{\prime }\left( a\right)  - \cdots  - \frac{{h}^{n + 1}}{\left( {n + 1}\right) !}{F}^{\left( n + 1\right) }\left( a\right) ,
\]

et il s’agit de montrer que \( H\left( h\right) = o\left( {h}^{n + 1}\right) \) . Soit \( \varepsilon > 0 \) . Il existe \( \alpha > 0 \) tel que pour \( \left| h\right| < \alpha \) , \( \left| {G\left( h\right) }\right| < \varepsilon {\left| h\right| }^{n} \) . Si \( g\left( h\right) = \varepsilon {h}^{n + 1}/\left( {n + 1}\right) \) , on a donc

> and it remains to show that \( H\left( h\right) = o\left( {h}^{n + 1}\right) \) . Let \( \varepsilon > 0 \) . There exists \( \alpha > 0 \) such that for \( \left| h\right| < \alpha \) , \( \left| {G\left( h\right) }\right| < \varepsilon {\left| h\right| }^{n} \) . If \( g\left( h\right) = \varepsilon {h}^{n + 1}/\left( {n + 1}\right) \) , we therefore have

\[
\forall h,0 < h < \alpha ,\;\begin{Vmatrix}{{H}^{\prime }\left( h\right) }\end{Vmatrix} < {g}^{\prime }\left( h\right) .
\]

En appliquant le théorème 5 entre les points 0 et \( h \) , on en déduit

> By applying theorem 5 between points 0 and \( h \), we deduce

\[
\forall h,0 \leq  h < \alpha ,\;\parallel H\left( h\right) \parallel  = \parallel H\left( h\right)  - H\left( 0\right) \parallel  \leq  g\left( x\right)  - g\left( 0\right)  = \varepsilon \frac{{h}^{n + 1}}{n + 1}.
\]

On procéderait de même pour \( - \alpha < h \leq 0 \) , d’où le résultat.

> We would proceed in the same way for \( - \alpha < h \leq 0 \), hence the result.

Citons enfin une dernière formule de Taylor, qui rend parfois de précieux services car elle donne beaucoup d’informations sur le terme de reste. L’e.v.n \( E \) doit être ici un espace de Banach pour assurer l'existence de l'intégrale (voir la définition 4 page 124).

> Finally, let us cite one last Taylor formula, which is sometimes very useful as it provides a great deal of information about the remainder term. The n.v.s. \( E \) must be a Banach space here to ensure the existence of the integral (see definition 4 on page 124).

\( \rightarrow \) THÉORÉME 9 (FORMULE DE TAYLOR AVEC RESTE INTEGRAL). Soient \( n \in \mathbb{N} \) et une application \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) de classe \( {\mathcal{C}}^{n + 1} \) sur \( \left\lbrack {a, b}\right\rbrack \) , où \( E \) est un \( \mathbb{R} \) -espace de Banach. Alors

> \( \rightarrow \) THEOREM 9 (TAYLOR'S FORMULA WITH INTEGRAL REMAINDER). Let \( n \in \mathbb{N} \) and a mapping \( F : \left\lbrack {a, b}\right\rbrack \rightarrow E \) of class \( {\mathcal{C}}^{n + 1} \) on \( \left\lbrack {a, b}\right\rbrack \), where \( E \) is a \( \mathbb{R} \)-Banach space. Then

\[
F\left( b\right)  = F\left( a\right)  + \left( {b - a}\right) {F}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( b - a\right) }^{n}}{n!}{F}^{\left( n\right) }\left( a\right)  + {\int }_{a}^{b}\frac{{\left( b - t\right) }^{n}}{n!}{F}^{\left( n + 1\right) }\left( t\right) {dt}.
\]

La preuve est immédiate par récurrence sur \( n \) .

> The proof is immediate by induction on \( n \).
