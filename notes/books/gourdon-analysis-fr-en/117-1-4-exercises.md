#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1. a) Montrer que la fonction \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) définie par \( f\left( {x, y}\right) = {y}^{2}/x \) si \( x \neq 0 \) , \( f\left( {0, y}\right) = y \) , est dérivable selon tout vecteur au point \( \left( {0,0}\right) \) , mais n’est pas continue en \( \left( {0,0}\right) \) .

> EXERCISE 1. a) Show that the function \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) defined by \( f\left( {x, y}\right) = {y}^{2}/x \) if \( x \neq 0 \), \( f\left( {0, y}\right) = y \), is differentiable along any vector at point \( \left( {0,0}\right) \), but is not continuous at \( \left( {0,0}\right) \).

b) On considère l'application

> b) Consider the mapping

\[
f : {\mathbb{R}}^{2} \rightarrow  \mathbb{R}\;f\left( {x, y}\right)  = {xy}\frac{{x}^{2} - {y}^{2}}{{x}^{2} + {y}^{2}}\;\text{ si }\;\left( {x, y}\right)  \neq  \left( {0,0}\right) ,\;f\left( {0,0}\right)  = 0.
\]

Montrer que les dérivées partielles \( \frac{{\partial }^{2}f}{\partial x\partial y}\left( {0,0}\right) \) et \( \frac{{\partial }^{2}f}{\partial y\partial x}\left( {0,0}\right) \) existent mais ne sont pas égales (exemple dû à Péano).

> Show that the partial derivatives \( \frac{{\partial }^{2}f}{\partial x\partial y}\left( {0,0}\right) \) and \( \frac{{\partial }^{2}f}{\partial y\partial x}\left( {0,0}\right) \) exist but are not equal (example due to Peano).

Solution. a) Soit \( \left( {a, b}\right) \) un vecteur de \( {\mathbb{R}}^{2} \) . Si \( a \neq 0 \) , on a

> Solution. a) Let \( \left( {a, b}\right) \) be a vector of \( {\mathbb{R}}^{2} \). If \( a \neq 0 \), we have

\[
\forall t \in  {\mathbb{R}}^{ * },\;f\left( {{ta},{tb}}\right)  - f\left( {0,0}\right)  = \frac{{t}^{2}{b}^{2}}{ta} = \frac{{b}^{2}}{a}t,
\]

ce qui montre que \( f \) est dérivable en \( \left( {0,0}\right) \) selon le vecteur \( \left( {a, b}\right) \) et que \( {f}_{\left( a, b\right) }^{\prime }\left( {0,0}\right) = {b}^{2}/a \) .

> which shows that \( f \) is differentiable at \( \left( {0,0}\right) \) along the vector \( \left( {a, b}\right) \) and that \( {f}_{\left( a, b\right) }^{\prime }\left( {0,0}\right) = {b}^{2}/a \).

Si \( a = 0 \) , on a \( f\left( {0,{tb}}\right) = {tb} \) pour tout \( t \in \mathbb{R} \) , donc \( f \) est dérivable en \( \left( {0,0}\right) \) selon le vecteur \( \left( {a, b}\right) \) et \( {f}_{\left( a, b\right) }^{\prime }\left( {0,0}\right) = b. \)

> If \( a = 0 \), we have \( f\left( {0,{tb}}\right) = {tb} \) for all \( t \in \mathbb{R} \), so \( f \) is differentiable at \( \left( {0,0}\right) \) along the vector \( \left( {a, b}\right) \) and \( {f}_{\left( a, b\right) }^{\prime }\left( {0,0}\right) = b. \)

Cependant, \( f \) n’est pas continue en \( \left( {0,0}\right) \) car pour tout \( n \in {\mathbb{N}}^{ * }, f\left( {1/{n}^{3},1/n}\right) = n \) tend vers \( + \infty \) lorsque \( n \rightarrow + \infty \) , alors que \( \left( {1/{n}^{3},1/n}\right) \) tend vers \( \left( {0,0}\right) \) .

> However, \( f \) is not continuous at \( \left( {0,0}\right) \) because for any \( n \in {\mathbb{N}}^{ * }, f\left( {1/{n}^{3},1/n}\right) = n \) it tends to \( + \infty \) as \( n \rightarrow + \infty \) , whereas \( \left( {1/{n}^{3},1/n}\right) \) tends to \( \left( {0,0}\right) \) .

b) Pour tout \( x \in \mathbb{R} \) , on a

> b) For any \( x \in \mathbb{R} \) , we have

\[
\forall y \neq  0,\;\frac{f\left( {x, y}\right)  - f\left( {x,0}\right) }{y} = x\frac{{x}^{2} - {y}^{2}}{{x}^{2} + {y}^{2}}.
\]

En faisant tendre \( y \) vers 0, on en déduit si \( x \neq 0 \) que \( \frac{\partial f}{\partial y}\left( {x,0}\right) \) existe et vaut \( x \) ; si \( x = 0 \) , on voit de même que \( \frac{\partial f}{\partial y}\left( {0,0}\right) \) existe et vaut 0 . Finalement, on a \( \frac{\partial f}{\partial y}\left( {x,0}\right) = x \) pour tout \( x \in \mathbb{R} \) . On en conclut que \( \frac{{\partial }^{2}f}{\partial x\partial y}\left( {0,0}\right) \) existe et vaut 1 .

> By letting \( y \) tend to 0, we deduce if \( x \neq 0 \) that \( \frac{\partial f}{\partial y}\left( {x,0}\right) \) exists and equals \( x \) ; if \( x = 0 \) , we see similarly that \( \frac{\partial f}{\partial y}\left( {0,0}\right) \) exists and equals 0 . Finally, we have \( \frac{\partial f}{\partial y}\left( {x,0}\right) = x \) for any \( x \in \mathbb{R} \) . We conclude that \( \frac{{\partial }^{2}f}{\partial x\partial y}\left( {0,0}\right) \) exists and equals 1 .

Maintenant, on en déduit, grâce à la relation d’antisymétrie \( f\left( {y, x}\right) = - f\left( {x, y}\right) \) le fait que \( \frac{{\partial }^{2}f}{\partial y\partial x}\left( {0,0}\right) \) existe et vaut -1 . D’où le résultat.

> Now, we deduce, thanks to the antisymmetry relation \( f\left( {y, x}\right) = - f\left( {x, y}\right) \) , the fact that \( \frac{{\partial }^{2}f}{\partial y\partial x}\left( {0,0}\right) \) exists and equals -1 . Hence the result.

EXERCICE 2. Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une application différentiable en 0 et telle que

> EXERCISE 2. Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a mapping differentiable at 0 and such that

\[
\forall x \in  {\mathbb{R}}^{n},\left( {x \neq  0}\right) ,\forall t \in  {\mathbb{R}}^{+ * },\;f\left( {tx}\right)  = {tf}\left( x\right) .
\]

Montrer que \( f \) est linéaire.

> Show that \( f \) is linear.

Solution. Fixons un vecteur \( x \neq 0 \) quelconque de \( {\mathbb{R}}^{n} \) . La relation \( f\left( {tx}\right) = {tf}\left( x\right) \) pour tout \( t > 0 \) montre que \( f\left( {tx}\right) \) tend vers 0 lorsque \( t \rightarrow 0 \) , et comme \( f \) est continue en 0 (car elle est différentiable en 0), on en conclut \( f\left( 0\right) = 0 \) . Maintenant, la différentiabilité de \( f \) en 0 entraîne, lorsque \( t \rightarrow {0}^{ + } \) ,

> Solution. Let us fix an arbitrary vector \( x \neq 0 \) in \( {\mathbb{R}}^{n} \) . The relation \( f\left( {tx}\right) = {tf}\left( x\right) \) for any \( t > 0 \) shows that \( f\left( {tx}\right) \) tends to 0 as \( t \rightarrow 0 \) , and since \( f \) is continuous at 0 (because it is differentiable at 0), we conclude \( f\left( 0\right) = 0 \) . Now, the differentiability of \( f \) at 0 implies, as \( t \rightarrow {0}^{ + } \) ,

\[
f\left( {tx}\right)  = f\left( 0\right)  + d{f}_{0}\left( {tx}\right)  + o\left( {\parallel {tx}\parallel }\right)  = {td}{f}_{0}\left( x\right)  + {t\varepsilon }\left( t\right) \;\text{ donc }\;f\left( x\right)  = d{f}_{0}\left( x\right)  + \varepsilon \left( t\right)
\]

avec \( \varepsilon \left( t\right) \rightarrow 0 \) lorsque \( t \rightarrow {0}^{ + } \) . En faisant tendre \( t \) vers 0, on en déduit \( f\left( x\right) = d{f}_{0}\left( x\right) \) . Ceci est vrai pour tout \( x \in {\mathbb{R}}^{n} \) non nul, et est vrai également pour \( x = 0 \) car nous avons montré \( f\left( 0\right) = 0 \) . Finalement, \( f = d{f}_{0} \) est linéaire.

> with \( \varepsilon \left( t\right) \rightarrow 0 \) as \( t \rightarrow {0}^{ + } \) . By letting \( t \) tend to 0, we deduce \( f\left( x\right) = d{f}_{0}\left( x\right) \) . This is true for any non-zero \( x \in {\mathbb{R}}^{n} \) , and is also true for \( x = 0 \) because we have shown \( f\left( 0\right) = 0 \) . Finally, \( f = d{f}_{0} \) is linear.

EXERCICE 3. 1 / Soient \( E, F, G \) des e.v.n et \( \varphi : E \times F \rightarrow G \) une application bilinéaire. On suppose que \( \varphi \) est continue, de sorte qu’il existe \( C > 0 \) tel que \( \parallel \varphi \left( {x, y}\right) \parallel \leq C\parallel x\parallel \parallel y\parallel \) pour tout \( \left( {x, y}\right) \in E \times F \) . Montrer que \( \varphi \) est différentiable sur \( E \times F \) et calculer sa différentielle \( {d\varphi } \) .

> EXERCISE 3. 1 / Let \( E, F, G \) be normed vector spaces and \( \varphi : E \times F \rightarrow G \) a bilinear mapping. Suppose that \( \varphi \) is continuous, so there exists \( C > 0 \) such that \( \parallel \varphi \left( {x, y}\right) \parallel \leq C\parallel x\parallel \parallel y\parallel \) for all \( \left( {x, y}\right) \in E \times F \) . Show that \( \varphi \) is differentiable on \( E \times F \) and calculate its differential \( {d\varphi } \) .

2/ (Applications.) a) Soit \( E \) un espace préhilbertien réel. Montrer la différentiabilité et calculer la différentielle de l’application produit scalaire \( \Phi : {E}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto x \cdot y \) . b) Soit \( n \in {\mathbb{N}}^{ * } \) . Pour tout \( p \in {\mathbb{N}}^{ * } \) , montrer que l’application \( {\varphi }_{p} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) définie par \( \varphi \left( M\right) = {M}^{p} \) est différentiable et calculer sa différentielle \( d{\varphi }_{p} \) .

> 2/ (Applications.) a) Let \( E \) be a real pre-Hilbert space. Show the differentiability and calculate the differential of the scalar product map \( \Phi : {E}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto x \cdot y \) . b) Let \( n \in {\mathbb{N}}^{ * } \) . For all \( p \in {\mathbb{N}}^{ * } \) , show that the map \( {\varphi }_{p} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) defined by \( \varphi \left( M\right) = {M}^{p} \) is differentiable and calculate its differential \( d{\varphi }_{p} \) .

Solution. 1/ Fixons \( \left( {x, y}\right) \in E \times F \) . Pour tout \( \left( {h, k}\right) \in E \times F \) , on a

> Solution. 1/ Let us fix \( \left( {x, y}\right) \in E \times F \) . For all \( \left( {h, k}\right) \in E \times F \) , we have

\[
\varphi \left( {x + h, y + k}\right)  = \varphi \left( {x, y + k}\right)  + \varphi \left( {h, y + k}\right)  = \varphi \left( {x, y}\right)  + \varphi \left( {x, k}\right)  + \varphi \left( {h, y}\right)  + \varphi \left( {h, k}\right) ,
\]

donc si \( L\left( {h, k}\right) = \varphi \left( {x, k}\right) + \varphi \left( {h, y}\right) , L \) est linéaire et

> so if \( L\left( {h, k}\right) = \varphi \left( {x, k}\right) + \varphi \left( {h, y}\right) , L \) is linear and

\[
\parallel \varphi \left( {x + h, y + k}\right)  - \varphi \left( {x, y}\right)  - L\left( {h, k}\right) \parallel  = \parallel \varphi \left( {h, k}\right) \parallel  \leq  C\parallel h\parallel \parallel k\parallel  = o\left( {\parallel \left( {h, k}\right) \parallel }\right)
\]

(en prenant par exemple \( \parallel \left( {h, k}\right) \parallel = \sup \{ \parallel h\parallel ,\parallel k\parallel \} \) ). Donc \( \varphi \) est différentiable en \( \left( {x, y}\right) \) et \( d{\varphi }_{\left( x, y\right) } = L \) , c’est-à-dire \( d{\varphi }_{\left( x, y\right) } : \left( {h, k}\right) \mapsto \varphi \left( {x, k}\right) + \varphi \left( {h, y}\right) \) .

> (by taking, for example, \( \parallel \left( {h, k}\right) \parallel = \sup \{ \parallel h\parallel ,\parallel k\parallel \} \) ). Thus \( \varphi \) is differentiable at \( \left( {x, y}\right) \) and \( d{\varphi }_{\left( x, y\right) } = L \) , that is to say \( d{\varphi }_{\left( x, y\right) } : \left( {h, k}\right) \mapsto \varphi \left( {x, k}\right) + \varphi \left( {h, y}\right) \) .

2/ a) L’application \( \Phi \) est bilinéaire et continue car d’après l’inégalité de Schwarz, \( \left| {\Phi \left( {x, y}\right) }\right| \leq \; \parallel x\parallel \parallel y\parallel \) pour tout \( \left( {x, y}\right) \in {E}^{2} \) . En appliquant le résultat de la question précédente, on en déduit que \( \Phi \) est différentiable sur \( {E}^{2} \) et que \( d{\Phi }_{\left( x, y\right) } : \left( {h, k}\right) \mapsto x \cdot h + y \cdot k \) pour tout \( \left( {x, y}\right) \in {E}^{2} \) .

> 2/ a) The map \( \Phi \) is bilinear and continuous because, according to the Schwarz inequality, \( \left| {\Phi \left( {x, y}\right) }\right| \leq \; \parallel x\parallel \parallel y\parallel \) for all \( \left( {x, y}\right) \in {E}^{2} \) . By applying the result of the previous question, we deduce that \( \Phi \) is differentiable on \( {E}^{2} \) and that \( d{\Phi }_{\left( x, y\right) } : \left( {h, k}\right) \mapsto x \cdot h + y \cdot k \) for all \( \left( {x, y}\right) \in {E}^{2} \) .

b) Notons \( \Psi \) l’application bilinéaire continue \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {A, B}\right) \mapsto {AB} \) . D’après la question \( 1/,\Psi \) est différentiable et \( d{\Psi }_{\left( A, B\right) }\left( {H, K}\right) = {HB} + {AK} \) pour tout \( \left( {A, B}\right) \) .

> b) Let \( \Psi \) denote the continuous bilinear map \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {A, B}\right) \mapsto {AB} \) . According to the question, \( 1/,\Psi \) is differentiable and \( d{\Psi }_{\left( A, B\right) }\left( {H, K}\right) = {HB} + {AK} \) for all \( \left( {A, B}\right) \) .

Ceci étant, montrons par récurrence sur \( p \in {\mathbb{N}}^{ * } \) que \( {\varphi }_{p} \) est différentiable sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et vérifie

> This being so, let us show by induction on \( p \in {\mathbb{N}}^{ * } \) that \( {\varphi }_{p} \) is differentiable on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and satisfies

\[
\forall M, H \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\;d{\varphi }_{p, M}\left( H\right)  = \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}{M}^{i}H{M}^{\left( {p - 1}\right)  - i}.
\]

Pour \( p = 1 \) , c’est évident car \( {\varphi }_{1} \) est linéaire. Supposons le résultat vrai au rang \( p \) et montrons le au rang \( p + 1 \) . On a \( {\varphi }_{p + 1} = {\varphi }_{1}{\varphi }_{p} = \Psi \left( {{\varphi }_{1},{\varphi }_{p}}\right) \) , donc composée d’applications différentiables, donc \( {\varphi }_{p + 1} \) est différentiable et \( d{\varphi }_{p + 1, M} = d{\Psi }_{{\varphi }_{1}\left( M\right) ,{\varphi }_{p}\left( M\right) }\left\lbrack {d{\varphi }_{1, M}, d{\varphi }_{p, M}}\right\rbrack \) c’est-à-dire

> For \( p = 1 \), it is obvious because \( {\varphi }_{1} \) is linear. Assume the result is true at rank \( p \) and show it at rank \( p + 1 \). We have \( {\varphi }_{p + 1} = {\varphi }_{1}{\varphi }_{p} = \Psi \left( {{\varphi }_{1},{\varphi }_{p}}\right) \), thus it is a composition of differentiable mappings, so \( {\varphi }_{p + 1} \) is differentiable and \( d{\varphi }_{p + 1, M} = d{\Psi }_{{\varphi }_{1}\left( M\right) ,{\varphi }_{p}\left( M\right) }\left\lbrack {d{\varphi }_{1, M}, d{\varphi }_{p, M}}\right\rbrack \) that is to say

\[
d{\varphi }_{p + 1, M}\left( H\right)  = d{\varphi }_{1, M}\left( H\right) {\varphi }_{p}\left( M\right)  + {\varphi }_{1}\left( M\right) d{\varphi }_{p, M}\left( H\right)
\]

\[
= H{M}^{p} + M\mathop{\sum }\limits_{{i = 0}}^{{p - 1}}{M}^{i}H{M}^{\left( {p - 1}\right)  - i} = \mathop{\sum }\limits_{{i = 0}}^{p}{M}^{i}H{M}^{p - i},
\]

d'où le résultat.

> hence the result.

- EXERCICE 4 (LEMME D’HADAMARD). Soit \( f : {\mathbb{R}}^{n} \rightarrow  \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{\infty } \) . a) On suppose \( f\left( 0\right)  = 0 \) . Montrer que l’on peut écrire

> - EXERCISE 4 (HADAMARD'S LEMMA). Let \( f : {\mathbb{R}}^{n} \rightarrow  \mathbb{R} \) be a function of class \( {\mathcal{C}}^{\infty } \). a) Assume \( f\left( 0\right)  = 0 \). Show that one can write

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{g}_{i}\left( {{x}_{1},\ldots ,{x}_{n}}\right)
\]

où pour tout \( i,{g}_{i} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) est une fonction de classe \( {\mathcal{C}}^{\infty } \) .

> where for all \( i,{g}_{i} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) is a function of class \( {\mathcal{C}}^{\infty } \).

b) Si de plus \( d{f}_{0} = 0 \) , montrer que l’on peut écrire

> b) If in addition \( d{f}_{0} = 0 \), show that one can write

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{\substack{{1 \leq  i \leq  n} \\  {1 \leq  j \leq  n} }}{x}_{i}{x}_{j}{h}_{i, j}\left( {{x}_{1},\ldots ,{x}_{n}}\right)
\]

où pour tout \( \left( {i, j}\right) ,{h}_{i, j} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) est une fonction de classe \( {\mathcal{C}}^{\infty } \) .

> where for all \( \left( {i, j}\right) ,{h}_{i, j} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) is a function of class \( {\mathcal{C}}^{\infty } \).

Solution. a) On commence par écrire la formule de Taylor avec reste intégral à l'ordre 1, qui s’écrit ici, pour tout \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) ,

> Solution. a) We begin by writing Taylor's formula with integral remainder at order 1, which is written here, for all \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \),

\[
f\left( x\right)  = {\int }_{0}^{1}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}\frac{\partial f}{\partial {x}_{i}}\left( {tx}\right) }\right) {dt} = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{g}_{i}\left( x\right) \;\text{ avec }\;{g}_{i}\left( x\right)  = {\int }_{0}^{1}\frac{\partial f}{\partial {x}_{i}}\left( {tx}\right) {dt}.
\]

Il suffit ensuite de remarquer, grâce au théorème de dérivation sous le signe intégral, que les fonctions \( {g}_{i} \) ainsi définies sont de classe \( {\mathcal{C}}^{\infty } \) .

> It then suffices to note, thanks to the theorem of differentiation under the integral sign, that the functions \( {g}_{i} \) thus defined are of class \( {\mathcal{C}}^{\infty } \).

b) Si de plus \( d{f}_{0} = 0 \) , alors \( \frac{\partial f}{\partial {x}_{i}}\left( 0\right) = {g}_{i}\left( 0\right) = 0 \) pour tout \( i \) . Comme les fonctions \( {g}_{i} \) sont de classe \( {\mathcal{C}}^{\infty } \) , on peut leur appliquer le résultat précédent qui montre que pour tout \( i \) , on peut trouver des fonctions \( {\left( {h}_{i, j}\right) }_{1 \leq j \leq n} \) de classe \( {\mathcal{C}}^{\infty } \) telles que \( {g}_{i}\left( x\right) = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{j}{h}_{i, j}\left( x\right) \) pour tout \( x \in {\mathbb{R}}^{n} \) . Ainsi,

> b) If in addition \( d{f}_{0} = 0 \), then \( \frac{\partial f}{\partial {x}_{i}}\left( 0\right) = {g}_{i}\left( 0\right) = 0 \) for all \( i \). Since the functions \( {g}_{i} \) are of class \( {\mathcal{C}}^{\infty } \), we can apply the previous result to them, which shows that for all \( i \), we can find functions \( {\left( {h}_{i, j}\right) }_{1 \leq j \leq n} \) of class \( {\mathcal{C}}^{\infty } \) such that \( {g}_{i}\left( x\right) = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{j}{h}_{i, j}\left( x\right) \) for all \( x \in {\mathbb{R}}^{n} \). Thus,

\[
\forall x = \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n},\;f\left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}\left( {\mathop{\sum }\limits_{{j = 1}}^{n}{x}_{j}{h}_{i, j}\left( x\right) }\right)  = \mathop{\sum }\limits_{\substack{{1 \leq  i \leq  n} \\  {1 \leq  j \leq  n} }}{x}_{i}{x}_{j}{h}_{i, j}\left( x\right) ,
\]

d'où le résultat.

> hence the result.

Remarque. On aurait pu aussi démontrer le résultat de la question b) directement en utilisant la formule de Taylor avec reste intégral à l'ordre 2.

> Remark. One could also have proven the result of question b) directly by using Taylor's formula with integral remainder at order 2.

EXERCICE 5 (DIFFÉRENTIELLE DE L’INVERSE). 1/ a) Soit \( n \in {\mathbb{N}}^{ * } \) .Montrer que l’application Inv : \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \;M \mapsto {M}^{-1} \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) .

> EXERCISE 5 (DIFFERENTIAL OF THE INVERSE). 1/ a) Let \( n \in {\mathbb{N}}^{ * } \) .Show that the mapping Inv : \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \;M \mapsto {M}^{-1} \) is of class \( {\mathcal{C}}^{\infty } \) on \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) .

b) En calculant les dérivées partielles de Inv au point \( {I}_{n} \) , calculer la différentielle \( D \) Inv de Inv au point \( {I}_{n} \) .

> b) By calculating the partial derivatives of Inv at point \( {I}_{n} \) , calculate the differential \( D \) Inv of Inv at point \( {I}_{n} \) .

c) En déduire la valeur de la différentielle de Inv en tout point de \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) .

> c) Deduce the value of the differential of Inv at any point of \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) .

2 / On veut généraliser le résultat précédent en dimension infinie. Soit \( E \) un espace de Banach. On note \( \mathcal{G}{\ell }_{c}\left( E\right) \) l’ensemble des endomorphismes inversibles \( u \) de \( E \) tels que \( u \) et \( {u}^{-1} \) soient continus. La norme utilisée sur \( {\mathcal{L}}_{c}\left( E\right) \) est \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) . On rappelle (voir l’exercice 4 page 52) que \( \mathcal{G}{\ell }_{c}\left( E\right) \) est un ouvert de \( {\mathcal{L}}_{c}\left( E\right) \) .

> 2 / We wish to generalize the previous result to infinite dimensions. Let \( E \) be a Banach space. Let \( \mathcal{G}{\ell }_{c}\left( E\right) \) denote the set of invertible endomorphisms \( u \) of \( E \) such that \( u \) and \( {u}^{-1} \) are continuous. The norm used on \( {\mathcal{L}}_{c}\left( E\right) \) is \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) . Recall (see exercise 4, page 52) that \( \mathcal{G}{\ell }_{c}\left( E\right) \) is an open subset of \( {\mathcal{L}}_{c}\left( E\right) \) .

a) Montrer que l’application Inv : \( \mathcal{G}{\ell }_{c}\left( E\right) \rightarrow \mathcal{G}{\ell }_{c}\left( E\right) \;u \mapsto {u}^{-1} \) est différentiable au point \( {\operatorname{Id}}_{E} \) et calculer la différentielle de Inv en ce point.

> a) Show that the map Inv : \( \mathcal{G}{\ell }_{c}\left( E\right) \rightarrow \mathcal{G}{\ell }_{c}\left( E\right) \;u \mapsto {u}^{-1} \) is differentiable at point \( {\operatorname{Id}}_{E} \) and calculate the differential of Inv at this point.

b) Montrer que Inv est différentiable en tout point de \( \mathcal{G}{\ell }_{c}\left( E\right) \) et calculer sa différentielle.

> b) Show that Inv is differentiable at any point of \( \mathcal{G}{\ell }_{c}\left( E\right) \) and calculate its differential.

Solution. 1/ a) Remarquons tout d’abord que \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) est un ouvert de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (c’est l’image réciproque de l’ouvert \( {\mathbb{R}}^{ * } \) par l’application déterminant, qui est continue).

> Solution. 1/ a) First, note that \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) is an open subset of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (it is the preimage of the open set \( {\mathbb{R}}^{ * } \) under the determinant map, which is continuous).

Pour tout \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , on a \( {M}^{-1} = {\left( \det M\right) }^{-1}{}^{t}\widetilde{M} \) où \( \widetilde{M} \) désigne la comatrice de \( M \) . Cette expression montre que les coefficients de \( {M}^{-1} \) sont des fractions rationnelles en les coefficients de \( M \) , ce qui prouve que Inv est de classe \( {\mathcal{C}}^{\infty } \) .

> For all \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , we have \( {M}^{-1} = {\left( \det M\right) }^{-1}{}^{t}\widetilde{M} \) where \( \widetilde{M} \) denotes the comatrix of \( M \) . This expression shows that the coefficients of \( {M}^{-1} \) are rational fractions of the coefficients of \( M \) , which proves that Inv is of class \( {\mathcal{C}}^{\infty } \) .

b) On désigne par \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) la base canonique de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \left( {{E}_{i, j}\text{ est la matrice dont tous }}\right. \) les termes sont nuls sauf celui d'indice \( \left( {i, j}\right) \) qui vaut 1). En notant les matrices sous la forme \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) , calculons

> b) Let \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) denote the canonical basis of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \left( {{E}_{i, j}\text{ est la matrice dont tous }}\right. \) (the terms are zero except for the one with index \( \left( {i, j}\right) \) , which equals 1). Denoting the matrices in the form \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) , let us calculate

\[
\frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right)  = \mathop{\lim }\limits_{{t \rightarrow  0}}\frac{1}{t}\left\lbrack  {{\left( {I}_{n} + t{E}_{i, j}\right) }^{-1} - {I}_{n}}\right\rbrack  .
\]

Si \( i = j \) , on a

> If \( i = j \) , we have

\[
\frac{1}{t}\left\lbrack  {{\left( {I}_{n} + t{E}_{i, i}\right) }^{-1} - {I}_{n}}\right\rbrack   = \frac{1}{t}\left( {\frac{1}{t + 1} - 1}\right) {E}_{i, i} =  - \frac{1}{t + 1}{E}_{i, i}\;\text{ donc }\;\frac{\partial \operatorname{Inv}}{\partial {m}_{i, i}}\left( {I}_{n}\right)  =  - {E}_{i, i}.
\]

Si \( i \neq j \) , la matrice \( {E}_{i, j} \) vérifie \( {E}_{i, j}^{2} = 0 \) donc pour tout \( t \in \mathbb{R},{\left( {I}_{n} + t{E}_{i, j}\right) }^{-1} = {I}_{n} - t{E}_{i, j} \; \left( {\operatorname{car}\left( {{I}_{n} - t{E}_{i, j}}\right) \left( {{I}_{n} + t{E}_{i, j}}\right) = {I}_{n} - {t}^{2}{E}_{i, j}^{2} = {I}_{n}}\right) \) , et on en déduit \( \frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right) = - {E}_{i, j} \) .

> If \( i \neq j \) , the matrix \( {E}_{i, j} \) satisfies \( {E}_{i, j}^{2} = 0 \) so for all \( t \in \mathbb{R},{\left( {I}_{n} + t{E}_{i, j}\right) }^{-1} = {I}_{n} - t{E}_{i, j} \; \left( {\operatorname{car}\left( {{I}_{n} - t{E}_{i, j}}\right) \left( {{I}_{n} + t{E}_{i, j}}\right) = {I}_{n} - {t}^{2}{E}_{i, j}^{2} = {I}_{n}}\right) \) , and we deduce \( \frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right) = - {E}_{i, j} \) .

En résumé, nous avons montré \( \frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right) = - {E}_{i, j} \) pour tout \( \left( {i, j}\right) \) . On en déduit que la différentielle \( D{\operatorname{Inv}}_{{I}_{n}} \) de Inv au point \( {I}_{n} \) vérifie

> In summary, we have shown \( \frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right) = - {E}_{i, j} \) for all \( \left( {i, j}\right) \) . We deduce that the differential \( D{\operatorname{Inv}}_{{I}_{n}} \) of Inv at point \( {I}_{n} \) satisfies

\[
\forall M = {\left( {m}_{i, j}\right) }_{1 \leq  i, j \leq  n} \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,\;D{\operatorname{Inv}}_{{I}_{n}}\left( M\right)  = \mathop{\sum }\limits_{{i, j}}{m}_{i, j}\frac{\partial \operatorname{Inv}}{\partial {m}_{i, j}}\left( {I}_{n}\right)  =  - M,
\]

d'où le résultat.

> hence the result.

c) Soit \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) . Lorsque \( H \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tend vers 0, on a \( M + H \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) pour \( H \) suffisam-ment petit (car \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) est ouvert) et

> c) Let \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) . As \( H \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tends to 0, we have \( M + H \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) for \( H \) sufficiently small (since \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) is open) and

\[
\operatorname{Inv}\left( {M + H}\right)  = {\left( M + H\right) }^{-1} = {\left( {I}_{n} + {M}^{-1}H\right) }^{-1}{M}^{-1} = \left\lbrack  {{I}_{n} + D{\operatorname{Inv}}_{{I}_{n}}\left( {{M}^{-1}H}\right)  + o\left( {\parallel H\parallel }\right) }\right\rbrack  {M}^{-1}
\]

\[
= \left\lbrack  {{I}_{n} - {M}^{-1}H + o\left( {\parallel H\parallel }\right) }\right\rbrack  {M}^{-1} = \operatorname{Inv}\left( M\right)  - {M}^{-1}H{M}^{-1} + o\left( {\parallel H\parallel }\right)
\]

On en déduit \( D{\operatorname{Inv}}_{M}\left( H\right) = - {M}^{-1}H{M}^{-1} \) pour tout \( H \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> We deduce \( D{\operatorname{Inv}}_{M}\left( H\right) = - {M}^{-1}H{M}^{-1} \) for all \( H \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

2/ a) Pour tout \( h \in {\mathcal{L}}_{c}\left( E\right) ,\parallel h\parallel < 1 \) , on sait (voir la proposition 2 page 49) que Id \( + h \) est inversible et que \( {\left( \operatorname{Id} + h\right) }^{-1} = \operatorname{Id} - h + {h}^{2} - {h}^{3} + \cdots + {\left( -1\right) }^{n}{h}^{n} + \cdots \) . Comme \( \begin{Vmatrix}{\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}{\left( -1\right) }^{n}{h}^{n}}\end{Vmatrix} \leq \; \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\parallel h{\parallel }^{n} = \parallel h{\parallel }^{2}/\left( {1 - \parallel h\parallel }\right) \) , on en déduit que lorsque \( h \rightarrow 0 \) , \( \operatorname{Inv}\left( {\operatorname{Id} + h}\right) = \operatorname{Id} - h + o\left( {\parallel h\parallel }\right) \) . Ainsi, Inv est différentiable au point Id et \( D{\operatorname{Inv}}_{\mathrm{{Id}}}\left( h\right) = - h \) .

> 2/ a) For all \( h \in {\mathcal{L}}_{c}\left( E\right) ,\parallel h\parallel < 1 \) , we know (see proposition 2 page 49) that Id \( + h \) is invertible and that \( {\left( \operatorname{Id} + h\right) }^{-1} = \operatorname{Id} - h + {h}^{2} - {h}^{3} + \cdots + {\left( -1\right) }^{n}{h}^{n} + \cdots \) . As \( \begin{Vmatrix}{\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}{\left( -1\right) }^{n}{h}^{n}}\end{Vmatrix} \leq \; \mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\parallel h{\parallel }^{n} = \parallel h{\parallel }^{2}/\left( {1 - \parallel h\parallel }\right) \) , we deduce that when \( h \rightarrow 0 \) , \( \operatorname{Inv}\left( {\operatorname{Id} + h}\right) = \operatorname{Id} - h + o\left( {\parallel h\parallel }\right) \) . Thus, Inv is differentiable at point Id and \( D{\operatorname{Inv}}_{\mathrm{{Id}}}\left( h\right) = - h \) .

b) On procède comme dans la question 1/c). Soit \( u \in \mathcal{G}{\ell }_{c}\left( E\right) \) . Comme \( \mathcal{G}{\ell }_{c}\left( E\right) \) est ouvert (voir l’exercice 4 page 52), on a \( u + h \in \mathcal{G}{\ell }_{c}\left( E\right) \) lorsque \( h \) est suffisamment petit, et lorsque \( h \rightarrow 0 \) ,

> b) We proceed as in question 1/c). Let \( u \in \mathcal{G}{\ell }_{c}\left( E\right) \). Since \( \mathcal{G}{\ell }_{c}\left( E\right) \) is open (see exercise 4 on page 52), we have \( u + h \in \mathcal{G}{\ell }_{c}\left( E\right) \) when \( h \) is sufficiently small, and when \( h \rightarrow 0 \),

\[
{\left( u + h\right) }^{-1} = {\left( \operatorname{Id} + {u}^{-1}h\right) }^{-1}{u}^{-1} = \left( {\operatorname{Id} - {u}^{-1}h + o\left( {\parallel h\parallel }\right) }\right) {u}^{-1} = {u}^{-1} - {u}^{-1}h{u}^{-1} + o\left( {\parallel h\parallel }\right) .
\]

De plus, l’application linéaire \( h \mapsto - {u}^{-1}h{u}^{-1} \) est continue car pour tout \( h \in {\mathcal{L}}_{c}\left( E\right) ,\begin{Vmatrix}{{u}^{-1}h{u}^{-1}}\end{Vmatrix} \leq \; \begin{Vmatrix}{u}^{-1}\end{Vmatrix}\parallel h\parallel \begin{Vmatrix}{u}^{-1}\end{Vmatrix} \) . En définitive, Inv est différentiable au point \( u \) et \( D{\operatorname{Inv}}_{u}\left( h\right) = - {u}^{-1}h{u}^{-1} \) pour tout \( h \in {\mathcal{L}}_{c}\left( E\right) \) .

> Furthermore, the linear map \( h \mapsto - {u}^{-1}h{u}^{-1} \) is continuous because for all \( h \in {\mathcal{L}}_{c}\left( E\right) ,\begin{Vmatrix}{{u}^{-1}h{u}^{-1}}\end{Vmatrix} \leq \; \begin{Vmatrix}{u}^{-1}\end{Vmatrix}\parallel h\parallel \begin{Vmatrix}{u}^{-1}\end{Vmatrix} \). Ultimately, Inv is differentiable at point \( u \) and \( D{\operatorname{Inv}}_{u}\left( h\right) = - {u}^{-1}h{u}^{-1} \) for all \( h \in {\mathcal{L}}_{c}\left( E\right) \).

EXERCICE 6 (DIFFÉRENTIELLE DU DÉTERMINANT). Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer que l’application déterminant définie par det : \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;M \mapsto \det M \) est de classe \( {\mathcal{C}}^{\infty } \) et calculer sa différentielle \( D \) det.

> EXERCISE 6 (DIFFERENTIAL OF THE DETERMINANT). Let \( n \in {\mathbb{N}}^{ * } \). Show that the determinant map defined by det : \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;M \mapsto \det M \) is of class \( {\mathcal{C}}^{\infty } \) and calculate its differential \( D \) det.

Solution. Le déterminant d'une matrice est un polynôme en ses coefficients, on en déduit que l’application \( M \mapsto \det M \) est de classe \( {\mathcal{C}}^{\infty } \) .

> Solution. The determinant of a matrix is a polynomial in its coefficients; we deduce that the map \( M \mapsto \det M \) is of class \( {\mathcal{C}}^{\infty } \).

Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Pour calculer \( D\mathop{\det }\limits_{M} \) (différentielle de det au point \( M \) ), nous allons calculer les dérivées partielles de det au point \( M \) . Désignons par \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) la base canonique de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . En notant \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) les éléments de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , il s’agit donc de calculer les \( \frac{\partial \det }{\partial {a}_{i, j}}\left( M\right) \) . En désignant par \( C = {\left( {C}_{i, j}\right) }_{1 \leq i, j \leq n} \) la comatrice de \( M \) (de sorte que \( {C}_{i, j} \) est le cofacteur de l’élément d’indice \( \left( {i, j}\right) \) de \( M \) ), la \( n \) -linéarité du déterminant entraîne, pour tout \( \left( {i, j}\right) \) et pour tout \( t \in \mathbb{R} \) ,

> Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). To calculate \( D\mathop{\det }\limits_{M} \) (differential of det at point \( M \)), we will calculate the partial derivatives of det at point \( M \). Let \( {\left( {E}_{i, j}\right) }_{1 \leq i, j \leq n} \) denote the canonical basis of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). By denoting \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) as the elements of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), we must therefore calculate the \( \frac{\partial \det }{\partial {a}_{i, j}}\left( M\right) \). By denoting \( C = {\left( {C}_{i, j}\right) }_{1 \leq i, j \leq n} \) as the comatrix of \( M \) (so that \( {C}_{i, j} \) is the cofactor of the element with index \( \left( {i, j}\right) \) of \( M \)), the \( n \)-linearity of the determinant implies, for all \( \left( {i, j}\right) \) and for all \( t \in \mathbb{R} \),

\[
\det \left( {M + t{E}_{i, j}}\right)  = \left( {\det M}\right)  + t{C}_{i, j}\;\text{ donc }\;\frac{\partial \det }{\partial {a}_{i, j}}\left( M\right)  = \mathop{\lim }\limits_{\substack{{t \rightarrow  0} \\  {t \neq  0} }}\frac{\det \left( {M + t{E}_{i, j}}\right)  - \det M}{t} = {C}_{i, j}.
\]

Ainsi, si \( H = \left( {h}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , on a

> Thus, if \( H = \left( {h}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), we have

\[
D{\det }_{M}\left( H\right)  = \mathop{\sum }\limits_{{i, j}}{h}_{i, j}\frac{\partial \det }{\partial {a}_{i, j}}\left( M\right)  = \mathop{\sum }\limits_{{i, j}}{h}_{i, j}{C}_{i, j} = \operatorname{tr}\left( {{}^{t}{CH}}\right) .
\]

Lorsque \( M \) est inversible, on peut obtenir une autre expression de \( D\mathop{\det }\limits_{M} \) en utilisant l’identité \( {}^{t}C = \left( {\det M}\right) {M}^{-1} \) qui entraîne \( D{\det }_{M}\left( H\right) = \left( {\det M}\right) \operatorname{tr}\left( {{M}^{-1}H}\right) \) pour tout \( H \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> When \( M \) is invertible, we can obtain another expression for \( D\mathop{\det }\limits_{M} \) using the identity \( {}^{t}C = \left( {\det M}\right) {M}^{-1} \) which leads to \( D{\det }_{M}\left( H\right) = \left( {\det M}\right) \operatorname{tr}\left( {{M}^{-1}H}\right) \) for all \( H \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

EXERCICE 7. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{1} \) . On définit l’application

> EXERCISE 7. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) class mapping. We define the mapping

\[
F : {\mathbb{R}}^{2} \rightarrow  \mathbb{R}\;F\left( {x, y}\right)  = \frac{f\left( x\right)  - f\left( y\right) }{x - y}\;\text{ si }\;x \neq  y,\;F\left( {x, x}\right)  = {f}^{\prime }\left( x\right) .
\]

a) Montrer que \( F \) est continue.

> a) Show that \( F \) is continuous.

b) Si \( f \) est de classe \( {\mathcal{C}}^{2} \) , montrer que \( F \) est de classe \( {\mathcal{C}}^{1} \) .

> b) If \( f \) is of class \( {\mathcal{C}}^{2} \) , show that \( F \) is of class \( {\mathcal{C}}^{1} \) .

Solution. a) Si \( x \neq y \) , on a

> Solution. a) If \( x \neq y \) , we have

\[
F\left( {x, y}\right)  = \frac{1}{y - x}{\int }_{x}^{y}{f}^{\prime }\left( u\right) {du} = {\int }_{0}^{1}{f}^{\prime }\left\lbrack  {x + t\left( {y - x}\right) }\right\rbrack  {dt},
\]

(*)

> égalité qui reste évidemment vraie pour \( x = y \) . Comme \( f \) est de classe \( {\mathcal{C}}^{1} \) , la dernière intégrale de (*) a son intégrande qui est continue en \( \left( {x, y}\right) \) sur \( {\mathbb{R}}^{2} \) , donc d’après le théorème de continuité sous le signe intégral, \( F \) est continue sur \( {\mathbb{R}}^{2} \) .

an equality that obviously remains true for \( x = y \) . Since \( f \) is of class \( {\mathcal{C}}^{1} \) , the integrand of the last integral in (*) is continuous in \( \left( {x, y}\right) \) on \( {\mathbb{R}}^{2} \) , therefore, according to the theorem of continuity under the integral sign, \( F \) is continuous on \( {\mathbb{R}}^{2} \) .

> b) Notre point de départ est toujours la relation (*). L’intégrande \( {f}^{\prime }\left( {x + t\left( {y - x}\right) }\right) \) est continúment dérivable par rapport à \( x \) , on peut donc appliquer le théorème de dérivation sous le signe intégral qui montre que \( F \) admet une dérivée partielle par rapport à \( x \) sur \( {\mathbb{R}}^{2} \) qui vérifie

b) Our starting point is still the relation (*). The integrand \( {f}^{\prime }\left( {x + t\left( {y - x}\right) }\right) \) is continuously differentiable with respect to \( x \) , so we can apply the theorem of differentiation under the integral sign, which shows that \( F \) admits a partial derivative with respect to \( x \) on \( {\mathbb{R}}^{2} \) that satisfies

\[
\forall \left( {x, y}\right)  \in  {\mathbb{R}}^{2},\;\frac{\partial F}{\partial x}\left( {x, y}\right)  = {\int }_{0}^{1}\frac{\partial }{\partial x}\left( {{f}^{\prime }\left\lbrack  {x + t\left( {y - x}\right) }\right\rbrack  }\right) {dt} = {\int }_{0}^{1}\left( {1 - t}\right) {f}^{\prime \prime }\left\lbrack  {x + t\left( {y - x}\right) }\right\rbrack  {dt},
\]

fonction de \( \left( {x, y}\right) \) qui est bien continue sur \( {\mathbb{R}}^{2} \) . De même, \( F \) admet une dérivée partielle par rapport à \( y \) continue sur \( {\mathbb{R}}^{2} \) . On en conclut que \( F \) est de classe \( {\mathcal{C}}^{1} \) .

> a function of \( \left( {x, y}\right) \) which is indeed continuous on \( {\mathbb{R}}^{2} \) . Similarly, \( F \) admits a partial derivative with respect to \( y \) that is continuous on \( {\mathbb{R}}^{2} \) . We conclude that \( F \) is of class \( {\mathcal{C}}^{1} \) .

Remarque. On peut également résoudre l’exercice sans exprimer \( F \) par l’intégrale (*), mais c'est plus difficile.

> Remark. One can also solve the exercise without expressing \( F \) via the integral (*), but it is more difficult.

EXERCICE 8 (FONCTIONS HOLOMORPHES, FONCTIONS HARMONIQUES). On note \( D = \; \{ z \in \mathbb{C},\left| z\right| < 1\} \) le disque unité ouvert complexe. Par commodité, on identifie les nombres complexes \( x + {iy} \) avec les couples \( \left( {x, y}\right) \) (avec \( x, y \in \mathbb{R} \) ).

> EXERCISE 8 (HOLOMORPHIC FUNCTIONS, HARMONIC FUNCTIONS). Let \( D = \; \{ z \in \mathbb{C},\left| z\right| < 1\} \) denote the open complex unit disk. For convenience, we identify complex numbers \( x + {iy} \) with pairs \( \left( {x, y}\right) \) (with \( x, y \in \mathbb{R} \) ).

1 / Soit \( f : D \rightarrow \mathbb{C} \) une application, et \( u, v \) les deux applications définies sur \( D \) ,à valeurs réelles, telles que \( f\left( {x + {iy}}\right) = u\left( {x, y}\right) + {iv}\left( {x, y}\right) \) . On dit que \( f \) est holomorphe sur \( D \) si elle est continûment dérivable par rapport à la variable complexe \( z \) , c’est-à-dire si

> 1 / Let \( f : D \rightarrow \mathbb{C} \) be a mapping, and \( u, v \) be the two real-valued mappings defined on \( D \) such that \( f\left( {x + {iy}}\right) = u\left( {x, y}\right) + {iv}\left( {x, y}\right) \) . We say that \( f \) is holomorphic on \( D \) if it is continuously differentiable with respect to the complex variable \( z \) , that is to say if

(i) pour tout \( {z}_{0} \in D,\left( {f\left( {{z}_{0} + h}\right) - f\left( {z}_{0}\right) }\right) /h \) converge lorsque \( h \in {\mathbb{C}}^{ * } \) tend vers 0 (cette limite est notée \( \left. {{f}^{\prime }\left( {z}_{0}\right) }\right) \) ,

> (i) for all \( {z}_{0} \in D,\left( {f\left( {{z}_{0} + h}\right) - f\left( {z}_{0}\right) }\right) /h \) converges as \( h \in {\mathbb{C}}^{ * } \) tends to 0 (this limit is denoted \( \left. {{f}^{\prime }\left( {z}_{0}\right) }\right) \) ,

(ii) l’application \( z \mapsto {f}^{\prime }\left( z\right) \) est continue sur \( D \) .

> (ii) the mapping \( z \mapsto {f}^{\prime }\left( z\right) \) is continuous on \( D \) .

a) Montrer que \( f \) est holomorphe si et seulement si les applications \( u \) et \( v \) sont de classe \( {\mathcal{C}}^{1} \) sur \( D \) et vérifient les conditions de Cauchy

> a) Show that \( f \) is holomorphic if and only if the mappings \( u \) and \( v \) are of class \( {\mathcal{C}}^{1} \) on \( D \) and satisfy the Cauchy-Riemann equations

\[
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y},\;\frac{\partial u}{\partial y} =  - \frac{\partial v}{\partial x}.
\]

b) Si \( f \) est holomorphe et si \( u \) et \( v \) sont de classe \( {\mathcal{C}}^{2} \) alors montrer que \( u \) et \( v \) sont harmoniques, c'est-à-dire

> b) If \( f \) is holomorphic and if \( u \) and \( v \) are of class \( {\mathcal{C}}^{2} \) then show that \( u \) and \( v \) are harmonic, that is to say

\[
\frac{{\partial }^{2}u}{\partial {x}^{2}} + \frac{{\partial }^{2}u}{\partial {y}^{2}} = 0,\;\frac{{\partial }^{2}v}{\partial {x}^{2}} + \frac{{\partial }^{2}v}{\partial {y}^{2}} = 0.
\]

2 / On considère une fonction \( u : D \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{2} \) et harmonique.

> 2 / Consider a function \( u : D \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{2} \) and harmonic.

a) Montrer que \( \partial u/\partial x \) est la partie réelle d’une fonction holomorphe.

> a) Show that \( \partial u/\partial x \) is the real part of a holomorphic function.

b) Montrer que \( u \) est la partie réelle d’une fonction holomorphe.

> b) Show that \( u \) is the real part of a holomorphic function.

Solution. 1/ a) On remarque tout d'abord que les conditions de Cauchy sont équivalentes à l’identité \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) .

> Solution. 1/ a) We first note that the Cauchy-Riemann equations are equivalent to the identity \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) .

Supposons \( f \) holomorphe. Soit \( z = x + {iy} \in D \) (avec \( x, y \in \mathbb{R} \) ). Lorsqu’on fait tendre le nombre réel \( s \) vers 0 dans l’expression

> Suppose \( f \) is holomorphic. Let \( z = x + {iy} \in D \) (with \( x, y \in \mathbb{R} \) ). When we let the real number \( s \) tend to 0 in the expression

\[
\frac{f\left( {z + s}\right)  - f\left( z\right) }{s} = \frac{f\left( {x + s, y}\right)  - f\left( {x, y}\right) }{s}
\]

le membre de gauche converge vers \( {f}^{\prime }\left( z\right) \) , donc celui de droite converge, ce qui montre l’existence de \( \frac{\partial f}{\partial x}\left( {x, y}\right) \) et de plus, \( {f}^{\prime }\left( z\right) = \frac{\partial f}{\partial x}\left( {x, y}\right) \) . Lorsque cette fois ci, on fait tendre le nombre réel \( t \) ver 0 dans l'expression

> the left-hand side converges to \( {f}^{\prime }\left( z\right) \) , therefore the right-hand side converges, which shows the existence of \( \frac{\partial f}{\partial x}\left( {x, y}\right) \) and furthermore, \( {f}^{\prime }\left( z\right) = \frac{\partial f}{\partial x}\left( {x, y}\right) \) . When this time we let the real number \( t \) tend to 0 in the expression

\[
\frac{f\left( {z + {it}}\right)  - f\left( z\right) }{it} = \frac{1}{i}\frac{f\left( {x, y + t}\right)  - f\left( {x, y}\right) }{t}
\]

on aboutit à l’existence de \( \frac{\partial f}{\partial y}\left( {x, y}\right) \) et à l’égalité \( {f}^{\prime }\left( z\right) = - i\frac{\partial f}{\partial y}\left( {x, y}\right) \) . Ainsi, on a montré \( \frac{\partial f}{\partial x}\left( {x, y}\right) + \; i\frac{\partial f}{\partial y}\left( {x, y}\right) = 0 \) . Par ailleurs, \( {f}^{\prime } \) étant continue, les égalités \( \frac{\partial f}{\partial x} = {f}^{\prime } \) et \( \frac{\partial f}{\partial y} = i{f}^{\prime } \) , entraînent que les dérivées partielles de \( f \) sont bien continues, donc \( f \) (et donc \( u \) et \( v \) ) est de classe \( {\mathcal{C}}^{1} \) .

> we arrive at the existence of \( \frac{\partial f}{\partial y}\left( {x, y}\right) \) and the equality \( {f}^{\prime }\left( z\right) = - i\frac{\partial f}{\partial y}\left( {x, y}\right) \) . Thus, we have shown \( \frac{\partial f}{\partial x}\left( {x, y}\right) + \; i\frac{\partial f}{\partial y}\left( {x, y}\right) = 0 \) . Furthermore, since \( {f}^{\prime } \) is continuous, the equalities \( \frac{\partial f}{\partial x} = {f}^{\prime } \) and \( \frac{\partial f}{\partial y} = i{f}^{\prime } \) imply that the partial derivatives of \( f \) are indeed continuous, so \( f \) (and thus \( u \) and \( v \) ) is of class \( {\mathcal{C}}^{1} \) .

Réciproquement, supposons \( f = u + {iv} \) de classe \( {\mathcal{C}}^{1} \) et vérifiant \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) . Soit \( z \in D \) . L’application \( f \) est différentiable en \( z = x + {iy} \) donc la formule de Taylor-Young entraîne, lorsque les nombres réels \( s \) et \( t \) tendent vers 0

> Conversely, suppose \( f = u + {iv} \) is of class \( {\mathcal{C}}^{1} \) and satisfies \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) . Let \( z \in D \) . The mapping \( f \) is differentiable at \( z = x + {iy} \) so Taylor-Young's formula implies, when the real numbers \( s \) and \( t \) tend to 0

\[
f\left( {x + s, y + t}\right)  - f\left( {x, y}\right)  = s\frac{\partial f}{\partial x}\left( {x, y}\right)  + t\frac{\partial f}{\partial y}\left( {x, y}\right)  + o\left( \left| {s + {it}}\right| \right) .
\]

Comme \( \frac{\partial f}{\partial y} = i\frac{\partial f}{\partial x} \) ceci entraîne

> Since \( \frac{\partial f}{\partial y} = i\frac{\partial f}{\partial x} \) this implies

\[
f\left( {x + s, y + t}\right)  - f\left( {x, y}\right)  = s\frac{\partial f}{\partial x}\left( {x, y}\right)  + {it}\frac{\partial f}{\partial x}\left( {x, y}\right)  + o\left( \left| {s + {it}}\right| \right)  = \left( {s + {it}}\right) \frac{\partial f}{\partial x}\left( {x, y}\right)  + o\left( \left| {s + {it}}\right| \right) .
\]

Ceci montre que la limite \( \left( {f\left( {z + h}\right) - f\left( z\right) }\right) /h \) converge vers \( \frac{\partial f}{\partial x}\left( {x, y}\right) \) lorsque \( h = s + {it} \) tend vers 0. Donc \( f \) est dérivable par rapport à la variable complexe \( z \) et de plus, \( {f}^{\prime }\left( z\right) = \frac{\partial f}{\partial x}\left( {x, y}\right) \) . Cette dernière égalité entraîne la continuité de \( {f}^{\prime } \) , donc \( f \) est bien holomorphe.

> This shows that the limit \( \left( {f\left( {z + h}\right) - f\left( z\right) }\right) /h \) converges to \( \frac{\partial f}{\partial x}\left( {x, y}\right) \) as \( h = s + {it} \) tends to 0. Thus \( f \) is differentiable with respect to the complex variable \( z \) and furthermore, \( {f}^{\prime }\left( z\right) = \frac{\partial f}{\partial x}\left( {x, y}\right) \) . This last equality implies the continuity of \( {f}^{\prime } \) , so \( f \) is indeed holomorphic.

b) Les conditions de Cauchy et l'indépendance des dérivées partielles à l'ordre de dérivation entraînent

> b) The Cauchy conditions and the independence of partial derivatives from the order of differentiation imply

\[
\frac{{\partial }^{2}u}{\partial {x}^{2}} = \frac{\partial }{\partial x}\left( \frac{\partial u}{\partial x}\right)  = \frac{\partial }{\partial x}\left( \frac{\partial v}{\partial y}\right)  = \frac{{\partial }^{2}v}{\partial {xy}} = \frac{\partial }{\partial y}\left( \frac{\partial v}{\partial x}\right)  =  - \frac{\partial }{\partial y}\left( \frac{\partial u}{\partial y}\right)  =  - \frac{{\partial }^{2}u}{\partial {y}^{2}}.
\]

Donc \( u \) est harmonique. On montrerait de même que \( v \) est harmonique.

> Therefore \( u \) is harmonic. We could show in the same way that \( v \) is harmonic.

2/a) On va montrer que \( f = \frac{\partial u}{\partial x} - i\frac{\partial u}{\partial y} \) est holomorphe. La fonction \( f \) est bien de classe \( {\mathcal{C}}^{1} \) et comme \( u \) est harmonique, on peut écrire

> 2/a) We will show that \( f = \frac{\partial u}{\partial x} - i\frac{\partial u}{\partial y} \) is holomorphic. The function \( f \) is indeed of class \( {\mathcal{C}}^{1} \) and since \( u \) is harmonic, we can write

\[
\frac{\partial f}{\partial y} = \frac{{\partial }^{2}u}{\partial {yx}} - i\frac{{\partial }^{2}u}{\partial {y}^{2}} = \frac{{\partial }^{2}u}{\partial {xy}} + i\frac{{\partial }^{2}u}{\partial {x}^{2}} = i\frac{\partial f}{\partial x}.
\]

Ainsi, les conditions de Cauchy sont vérifiées, donc \( f \) est bien holomorphe.

> Thus, the Cauchy conditions are satisfied, so \( f \) is indeed holomorphic.

b) Il faut en quelque sorte exhiber une primitive de \( f = \frac{\partial u}{\partial x} - i\frac{\partial u}{\partial y} \) . Pour tout \( z \in D \) , on va considérer l’intégrale curviligne de \( f \) le long d’un segment joignant 0 à \( z \) (c’est possible car le domaine \( D \) est une partie étoilée par rapport à 0 ), en posant

> b) We must in a way exhibit a primitive of \( f = \frac{\partial u}{\partial x} - i\frac{\partial u}{\partial y} \) . For any \( z \in D \) , we will consider the line integral of \( f \) along a segment joining 0 to \( z \) (this is possible because the domain \( D \) is a star-shaped set with respect to 0 ), by setting

\[
g\left( z\right)  = z{\int }_{0}^{1}f\left( {tz}\right) {dt} = \left( {x + {iy}}\right) {\int }_{0}^{1}f\left( {{tx},{ty}}\right) {dt}.
\]

Le théorème de dérivation sous le signe intégral nous assure que \( g \) est continûment dérivable par rapport à \( x \) et par rapport à \( y \) et que

> The theorem of differentiation under the integral sign ensures that \( g \) is continuously differentiable with respect to \( x \) and with respect to \( y \) and that

\[
\frac{\partial g}{\partial x}\left( {x, y}\right)  = {\int }_{0}^{1}f\left( {{tx},{ty}}\right) {dt} + \left( {x + {iy}}\right) {\int }_{0}^{1}t\frac{\partial f}{\partial x}\left( {{tx},{ty}}\right) {dt}
\]

\[
\frac{\partial g}{\partial y}\left( {x, y}\right)  = i{\int }_{0}^{1}f\left( {{tx},{ty}}\right) {dt} + \left( {x + {iy}}\right) {\int }_{0}^{1}t\frac{\partial f}{\partial y}\left( {{tx},{ty}}\right) {dt}.
\]

On en déduit

> We deduce from this

\[
\frac{\partial g}{\partial x}\left( {x, y}\right)  + i\frac{\partial g}{\partial y}\left( {x, y}\right)  = \left( {x + {iy}}\right) {\int }_{0}^{1}t\left( {\frac{\partial f}{\partial x}\left( {{tx},{ty}}\right)  + i\frac{\partial f}{\partial y}\left( {{tx},{ty}}\right) }\right) {dt}.
\]

et comme \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) , on en déduit \( \frac{\partial g}{\partial x} + i\frac{\partial g}{\partial y} = 0 \) . Ainsi la fonction \( g \) est holomorphe. Calculons sa partie réelle. On a

> and since \( \frac{\partial f}{\partial x} + i\frac{\partial f}{\partial y} = 0 \) , we deduce \( \frac{\partial g}{\partial x} + i\frac{\partial g}{\partial y} = 0 \) . Thus the function \( g \) is holomorphic. Let us calculate its real part. We have

\[
g\left( z\right)  = \left( {x + {iy}}\right) {\int }_{0}^{1}\left( {\frac{\partial u}{\partial x} - i\frac{\partial u}{\partial y}}\right) \left( {{tx},{ty}}\right) {dt}
\]

done

> therefore

\[
\Re \left( g\right) \left( z\right)  = {\int }_{0}^{1}\left( {x\frac{\partial u}{\partial x}\left( {{tx},{ty}}\right)  + y\frac{\partial u}{\partial y}\left( {{tx},{ty}}\right) }\right) {dt}.
\]

L’intégrande n’est autre que la dérivée par rapport à \( t \) de l’application \( t \mapsto u\left( {{tx},{ty}}\right) \) , on en déduit \( \Re \left( g\right) \left( z\right) = {\left\lbrack u\left( tx, ty\right) \right\rbrack }_{0}^{1} = u\left( {x, y}\right) - u\left( {0,0}\right) \) . Ainsi, la fonction \( h = g + u\left( {0,0}\right) \) est holomorphe (la propriété d’holomorphie ne change pas si on ajoute une constante à \( g \) ) et sa partie réelle est bien égale à \( u \) .

> The integrand is none other than the derivative with respect to \( t \) of the mapping \( t \mapsto u\left( {{tx},{ty}}\right) \) , we deduce \( \Re \left( g\right) \left( z\right) = {\left\lbrack u\left( tx, ty\right) \right\rbrack }_{0}^{1} = u\left( {x, y}\right) - u\left( {0,0}\right) \) . Thus, the function \( h = g + u\left( {0,0}\right) \) is holomorphic (the property of holomorphy does not change if one adds a constant to \( g \) ) and its real part is indeed equal to \( u \) .

Remarque. Les fonctions holomorphes font aussi l'objet de l'exercice 13 page 265. Dans la remarque à la fin de cet exercice, il est montré qu'une fonction holomorphe est analytique. On en déduit qu’une fonction holomorphe est forcément de classe \( {\mathcal{C}}^{\infty } \) .

> Remark. Holomorphic functions are also the subject of exercise 13 on page 265. In the remark at the end of that exercise, it is shown that a holomorphic function is analytic. We deduce from this that a holomorphic function is necessarily of class \( {\mathcal{C}}^{\infty } \) .

- Lorsque le domaine \( D \) de définition contient des trous (plus précisément s'il n'est pas simplement connexe, c'est-à-dire qu'un lacet dans \( D \) n'est pas continûment déformable en un point tout en restant dans \( D \) ), une fonction harmonique n'est pas forcément la partie réelle d'une fonction holomorphe.

> - When the domain \( D \) of definition contains holes (more precisely if it is not simply connected, that is to say that a loop in \( D \) is not continuously deformable to a point while remaining in \( D \) ), a harmonic function is not necessarily the real part of a holomorphic function.
