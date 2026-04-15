#### 1.3. Taylor formulas

*Français : 1.3. Formules de Taylor*

Accroissements finis.

> Finite increments.

THÉORÉME 3 (INÉGALITÉ DES ACCROISSEMENTS FINIS). Soit \( f : U \subset E \rightarrow F \) , où \( E \) et \( F \) sont deux e.v.n et \( U \) un ouvert de \( E \) . Soit \( \left( {a, b}\right) \in {U}^{2} \) tel que le segment \( \left\lbrack {a, b}\right\rbrack = \; \{ {ta} + \left( {1 - t}\right) b, t \in \left\lbrack {0,1}\right\rbrack \} \) soit inclus dans U. Si \( f \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) , différentiable en tout point de \( \rbrack a, b\left\lbrack \right. \) et s’il existe \( M > 0 \) tel que \( \left. { \parallel d{f}_{c}}\right\rbrack \leq M \) pour tout \( c \in \rbrack a, b\lbrack \) , alors \( \parallel f\left( b\right) - f\left( a\right) \parallel \leq M\parallel b - a\parallel . \)

> THEOREM 3 (MEAN VALUE INEQUALITY). Let \( f : U \subset E \rightarrow F \), where \( E \) and \( F \) are two n.v.s. and \( U \) an open set of \( E \). Let \( \left( {a, b}\right) \in {U}^{2} \) such that the segment \( \left\lbrack {a, b}\right\rbrack = \; \{ {ta} + \left( {1 - t}\right) b, t \in \left\lbrack {0,1}\right\rbrack \} \) is included in U. If \( f \) is continuous on \( \left\lbrack {a, b}\right\rbrack \), differentiable at every point of \( \rbrack a, b\left\lbrack \right. \) and if there exists \( M > 0 \) such that \( \left. { \parallel d{f}_{c}}\right\rbrack \leq M \) for all \( c \in \rbrack a, b\lbrack \), then \( \parallel f\left( b\right) - f\left( a\right) \parallel \leq M\parallel b - a\parallel . \)

Démonstration. La fonction \( g : \left\lbrack {0,1}\right\rbrack \rightarrow F\;t \mapsto f\left( {a + t\left( {b - a}\right) }\right) \) est continue sur \( \left\lbrack {0,1}\right\rbrack \) , dérivable sur \( \rbrack 0,1\lbrack \) , et

> Proof. The function \( g : \left\lbrack {0,1}\right\rbrack \rightarrow F\;t \mapsto f\left( {a + t\left( {b - a}\right) }\right) \) is continuous on \( \left\lbrack {0,1}\right\rbrack \), differentiable on \( \rbrack 0,1\lbrack \), and

\[
\forall t \in  \rbrack 0,1\left\lbrack  {,\;{g}^{\prime }\left( t\right)  = d{f}_{a + t\left( {b - a}\right) }\left( {b - a}\right) }\right.
\]

(voir la remarque 8). On a donc \( \begin{Vmatrix}{{g}^{\prime }\left( t\right) }\end{Vmatrix} \leq M\parallel b - a\parallel \) sur \( \rbrack 0,1\lbrack \) , donc d’après le théorème 5 page 75,

> (see remark 8). We therefore have \( \begin{Vmatrix}{{g}^{\prime }\left( t\right) }\end{Vmatrix} \leq M\parallel b - a\parallel \) on \( \rbrack 0,1\lbrack \), so according to theorem 5 on page 75,

\[
\parallel f\left( b\right)  - f\left( a\right) \parallel  = \parallel g\left( 1\right)  - g\left( 0\right) \parallel  \leq  M\parallel b - a\parallel .
\]

Conséquence :

> Consequence:

- Si \( U \) est convexe, si \( f \) est différentiable sur \( U \) et si \( \begin{Vmatrix}{d{f}_{x}}\end{Vmatrix} \leq  M \) pour tout \( x \in  U \) , alors

> - If \( U \) is convex, if \( f \) is differentiable on \( U \) and if \( \begin{Vmatrix}{d{f}_{x}}\end{Vmatrix} \leq  M \) for all \( x \in  U \), then

\[
\forall \left( {a, b}\right)  \in  {U}^{2},\;\parallel f\left( b\right)  - f\left( a\right) \parallel  \leq  M\parallel b - a\parallel .
\]

- Si \( U \) est un ouvert connexe et \( d{f}_{x} = 0 \) pour tout \( x \in  U \) , alors \( f \) est constante sur \( U \) (en effet, \( U \) est connexe par lignes brisées - voir le théorème 5 page 42 - et \( f\left( a\right)  = f\left( b\right) \) pour tout segment \( \left\lbrack  {a, b}\right\rbrack   \subset  U) \) .

> - If \( U \) is a connected open set and \( d{f}_{x} = 0 \) for all \( x \in  U \) , then \( f \) is constant on \( U \) (indeed, \( U \) is polygonally connected - see theorem 5 page 42 - and \( f\left( a\right)  = f\left( b\right) \) for every segment \( \left\lbrack  {a, b}\right\rbrack   \subset  U) \) .

Remarque 9. Si \( f \) prend ses valeurs dans \( \mathbb{R} \) , si \( \left\lbrack {a, b}\right\rbrack \subset U \) , si \( f \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) et différentiable sur \( \rbrack a, b\lbrack \) , alors l’égalité des accroissements finis est valable et s’écrit

> Remark 9. If \( f \) takes its values in \( \mathbb{R} \) , if \( \left\lbrack {a, b}\right\rbrack \subset U \) , if \( f \) is continuous on \( \left\lbrack {a, b}\right\rbrack \) and differentiable on \( \rbrack a, b\lbrack \) , then the mean value equality holds and is written

\[
\exists c \in  \rbrack a, b\lbrack ,\;f\left( b\right)  = f\left( a\right)  + d{f}_{c}\left( {b - a}\right) .
\]

Comme nous l'avons vu dans la remarque 2 page 74, ceci est faux dès que la dimension de l'espace d'arrivée est \( > 1 \) et on utilise alors l'inégalité des accroissements finis.

> As we saw in remark 2 page 74, this is false as soon as the dimension of the target space is \( > 1 \) and we then use the mean value inequality.

Formules de Taylor. Notation. Soit \( f : U \subset {\mathbb{R}}^{q} \rightarrow {\mathbb{R}}^{p} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{q} \) ) une application de classe \( {\mathcal{C}}^{k} \) sur \( U \) . Par analogie avec le fait que

> Taylor formulas. Notation. Let \( f : U \subset {\mathbb{R}}^{q} \rightarrow {\mathbb{R}}^{p} \) (where \( U \) is an open set of \( {\mathbb{R}}^{q} \) ) be a mapping of class \( {\mathcal{C}}^{k} \) on \( U \) . By analogy with the fact that

\[
\forall \left( {{a}_{1},\ldots ,{a}_{q}}\right)  \in  {\mathbb{R}}^{q},\;{\left( {a}_{1} + \cdots  + {a}_{q}\right) }^{n} = \mathop{\sum }\limits_{{{i}_{1} + \cdots  + {i}_{q} = n}}\frac{n!}{{i}_{1}!\cdots {i}_{q}!}{a}_{1}^{{i}_{1}}\cdots {a}_{q}^{{i}_{q}}
\]

on note pour tout \( n \in \{ 1,\ldots , k\} \)

> we denote for all \( n \in \{ 1,\ldots , k\} \)

\[
{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \right\rbrack  }^{\left\lbrack  n\right\rbrack  } = \mathop{\sum }\limits_{{{i}_{1} + \cdots  + {i}_{q} = n}}\frac{n!}{{i}_{1}!\cdots {i}_{q}!}{h}_{1}^{{i}_{1}}\cdots {h}_{q}^{{i}_{q}}\frac{{\partial }^{n}f}{\partial {x}_{1}^{{i}_{1}}\cdots \partial {x}_{q}^{{i}_{q}}}\left( a\right) .
\]

Cette expression s’appelle puissance symbolique n-ième de \( \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \) . C’est la dérivée \( n \) -ième de la fonction de la variable réelle \( t \mapsto f\left( {a + {th}}\right) \) en \( t = 0 \) .

> This expression is called the n-th symbolic power of \( \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \). It is the \( n \)-th derivative of the function of the real variable \( t \mapsto f\left( {a + {th}}\right) \) at \( t = 0 \).

A partir de cette notation, nous allons énoncer les formules de Taylor relatives aux fonctions de plusieurs variables. On les démontre en appliquant à la fonction \( t \mapsto f\left( {x + {th}}\right) \; \left( {t \in \left\lbrack {0,1}\right\rbrack }\right) \) les formules de Taylor vraies pour les fonctions de la variable réelle.

> Starting from this notation, we will state the Taylor formulas relating to functions of several variables. They are proven by applying to the function \( t \mapsto f\left( {x + {th}}\right) \; \left( {t \in \left\lbrack {0,1}\right\rbrack }\right) \) the Taylor formulas true for functions of a real variable.

THÉORÉME 4 (FORMULE DE TAYLOR-LAGRANGE). Soit \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) ) une application de classe \( {\mathcal{C}}^{p} \) sur \( U \) et \( x \in {\mathbb{R}}^{n}, h = \left( {{h}_{1},\ldots ,{h}_{n}}\right) \in {\mathbb{R}}^{n} \) tels que le segment \( \left\lbrack {x, x + h}\right\rbrack = \{ x + {th}, t \in \left\lbrack {0,1}\right\rbrack \} \) soit inclus dans \( U \) . Alors il existe \( \theta \in \rbrack 0,1\lbrack \) tel que

> THEOREM 4 (TAYLOR-LAGRANGE FORMULA). Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) (where \( U \) is an open set of \( {\mathbb{R}}^{n} \) ) be a mapping of class \( {\mathcal{C}}^{p} \) on \( U \) and \( x \in {\mathbb{R}}^{n}, h = \left( {{h}_{1},\ldots ,{h}_{n}}\right) \in {\mathbb{R}}^{n} \) such that the segment \( \left\lbrack {x, x + h}\right\rbrack = \{ x + {th}, t \in \left\lbrack {0,1}\right\rbrack \} \) is included in \( U \) . Then there exists \( \theta \in \rbrack 0,1\lbrack \) such that

\[
f\left( {x + h}\right)  = f\left( x\right)  + \left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{n}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) }\right\rbrack   + \frac{1}{2!}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{n}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\left\lbrack  2\right\rbrack  } + \cdots
\]

\[
\cdots  + \frac{1}{\left( {p - 1}\right) !}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{n}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\left\lbrack  p - 1\right\rbrack  } + \frac{1}{p!}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{n}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x + \theta h\right) \right\rbrack  }^{\left\lbrack  p\right\rbrack  }
\]

Exemple 2. Si \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) est de classe \( {\mathcal{C}}^{2} \) , alors pour tout \( \left( {h, k}\right) \in {\mathbb{R}}^{2} \) , il existe \( \theta \in \rbrack 0,1\lbrack \) tel que

> Example 2. If \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) is of class \( {\mathcal{C}}^{2} \) , then for all \( \left( {h, k}\right) \in {\mathbb{R}}^{2} \) , there exists \( \theta \in \rbrack 0,1\lbrack \) such that

\[
f\left( {h, k}\right)  = f\left( {0,0}\right)  + h\frac{\partial f}{\partial x}\left( {0,0}\right)  + k\frac{\partial f}{\partial y}\left( {0,0}\right)
\]

\[
+ \frac{1}{2}\left\lbrack  {{h}^{2}\frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{\theta h},{\theta k}}\right)  + {2hk}\frac{{\partial }^{2}f}{\partial x\partial y}\left( {{\theta h},{\theta k}}\right)  + {k}^{2}\frac{{\partial }^{2}f}{\partial {y}^{2}}\left( {{\theta h},{\theta k}}\right) }\right\rbrack   + o\left( {\parallel \left( {h, k}\right) {\parallel }^{2}}\right) .
\]

Remarque 10. Attention, comme pour l'égalité des accroissements finis, ceci n'est vrai que pour des fonctions à valeurs réelles. Pour des fonctions à valeurs dans \( {\mathbb{R}}^{p} \) , on peut par contre utiliser la formule de Taylor avec reste intégral.

> Remark 10. Note that, as with the mean value theorem, this is only true for real-valued functions. For functions with values in \( {\mathbb{R}}^{p} \), however, one can use Taylor's formula with integral remainder.

THÉORÉME 5 (FORMULE DE TAYLOR AVEC RESTE INTÉGRAL). Soient \( f : U \subset {\mathbb{R}}^{q} \rightarrow \; {\mathbb{R}}^{p} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{q} \) ) une application de classe \( {\mathcal{C}}^{k} \) sur \( U, x \in {\mathbb{R}}^{q} \) et \( h = \; \left( {{h}_{1},\ldots ,{h}_{q}}\right) \in {\mathbb{R}}^{q} \) tels que \( \left\lbrack {x, x + h}\right\rbrack \subset U \) . Alors

> THEOREM 5 (TAYLOR'S FORMULA WITH INTEGRAL REMAINDER). Let \( f : U \subset {\mathbb{R}}^{q} \rightarrow \; {\mathbb{R}}^{p} \) (where \( U \) is an open subset of \( {\mathbb{R}}^{q} \)) be a function of class \( {\mathcal{C}}^{k} \) on \( U, x \in {\mathbb{R}}^{q} \) and \( h = \; \left( {{h}_{1},\ldots ,{h}_{q}}\right) \in {\mathbb{R}}^{q} \) such that \( \left\lbrack {x, x + h}\right\rbrack \subset U \). Then

\[
f\left( {x + h}\right)  = f\left( x\right)  + \left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) }\right\rbrack   + \frac{1}{2!}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\left\lbrack  2\right\rbrack  } + \cdots
\]

\[
\cdots  + \frac{1}{\left( {k - 1}\right) !}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\left\lbrack  k - 1\right\rbrack  } + {\int }_{0}^{1}\frac{{\left( 1 - t\right) }^{k - 1}}{\left( {k - 1}\right) !}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x + th\right) \right\rbrack  }^{\left\lbrack  k\right\rbrack  }{dt}.
\]

THÉORÉME 6 (FORMULE DE TAYLOR-YOUNG). Soit \( f : U \subset {\mathbb{R}}^{q} \rightarrow {\mathbb{R}}^{p} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{q} \) ) une application de classe \( {\mathcal{C}}^{k} \) et \( x \in U \) . Alors lorsque \( h = \left( {{h}_{1},\ldots ,{h}_{q}}\right) \in {\mathbb{R}}^{q} \) tend vers 0 ,

> THEOREM 6 (TAYLOR-YOUNG FORMULA). Let \( f : U \subset {\mathbb{R}}^{q} \rightarrow {\mathbb{R}}^{p} \) (where \( U \) is an open subset of \( {\mathbb{R}}^{q} \)) be a function of class \( {\mathcal{C}}^{k} \) and \( x \in U \). Then as \( h = \left( {{h}_{1},\ldots ,{h}_{q}}\right) \in {\mathbb{R}}^{q} \) tends to 0,

\[
f\left( {x + h}\right)  = f\left( x\right)  + \left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) }\right\rbrack   + \frac{1}{2!}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\lbrack 2\rbrack } + \cdots  + \frac{1}{k!}{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{q}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( x\right) \right\rbrack  }^{\lbrack k\rbrack } + o\left( {\parallel h{\parallel }^{k}}\right) .
\]
