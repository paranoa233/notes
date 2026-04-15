#### 2.1. Exercises

*Français : 2.1. Exercices*

EXERCICE 1. Étudier les extremums relatifs puis les extremums absolus de la fonction

> EXERCISE 1. Study the relative extrema and then the absolute extrema of the function

\[
f : {\mathbb{R}}^{2} \rightarrow  \mathbb{R}\;\left( {x, y}\right)  \mapsto  {x}^{4} + {y}^{4} - 2{\left( x - y\right) }^{2}.
\]

---

Solution. La fonction \( f \) est de classe \( {\mathcal{C}}^{\infty } \) . Commençons par rechercher les extremums relatifs de \( f \) . Pour cela, on recherche ses points critiques \( \left( {x, y}\right) \) , qui vérifient \( d{f}_{\left( x, y\right) } = 0 \) , c’est-à-dire

> Solution. The function \( f \) is of class \( {\mathcal{C}}^{\infty } \) . Let us begin by searching for the relative extrema of \( f \) . To do this, we look for its critical points \( \left( {x, y}\right) \) , which satisfy \( d{f}_{\left( x, y\right) } = 0 \) , that is to say

\[
0 = \frac{\partial f}{\partial x} = 4{x}^{3} - 4\left( {x - y}\right) \;\text{ et }\;0 = \frac{\partial f}{\partial y} = 4{y}^{3} + 4\left( {x - y}\right) .
\]

Ce système de deux équations s'écrit aussi

> This system of two equations can also be written as

\[
\left\{  {\begin{array}{ll} {x}^{3} + {y}^{3} &  = 0 \\  {x}^{3} - \left( {x - y}\right) &  = 0 \end{array}\;\text{ ou encore }\left\{  {\begin{array}{ll} \left( {x + y}\right) \left( {{x}^{2} - {xy} + {y}^{2}}\right) &  = 0 \\  {x}^{3} - x + y &  = 0 \end{array}.}\right. }\right.
\]

Ce système admet la solution triviale \( \left( {x, y}\right) = \left( {0,0}\right) \) . Si \( \left( {x, y}\right) \neq \left( {0,0}\right) \) , alors \( {x}^{2} - {xy} + {y}^{2} = \; {\left( x - y\right) }^{2}/2 + {x}^{2}/2 + {y}^{2}/2 > 0 \) n’est pas nul, donc le système équivaut dans ce cas à

> This system admits the trivial solution \( \left( {x, y}\right) = \left( {0,0}\right) \) . If \( \left( {x, y}\right) \neq \left( {0,0}\right) \) , then \( {x}^{2} - {xy} + {y}^{2} = \; {\left( x - y\right) }^{2}/2 + {x}^{2}/2 + {y}^{2}/2 > 0 \) is not zero, so the system is equivalent in this case to

\( \left\{ {\begin{array}{ll} x + y & = 0 \\ {x}^{3} - {2x} & = 0 \end{array}\;\text{ dont les solutions non nulles sont }\;\left( {x, y}\right) = \left( {\sqrt{2}, - \sqrt{2}}\right) \;\text{ et }\;\left( {-\sqrt{2},\sqrt{2}}\right) .}\right. \)

> Finalement, \( f \) a trois points critiques : \( \left( {0,0}\right) ,\left( {\sqrt{2}, - \sqrt{2}}\right) \) et \( \left( {-\sqrt{2},\sqrt{2}}\right) \) .

Finally, \( f \) has three critical points: \( \left( {0,0}\right) ,\left( {\sqrt{2}, - \sqrt{2}}\right) \) and \( \left( {-\sqrt{2},\sqrt{2}}\right) \) .

> - Au point \( \left( {0,0}\right) \) , on voit facilement que la matrice hessienne de \( f \) est négative mais non définie négative (on a \( r = t =  - 4 \) et \( s = 4 \) ). On ne peut donc pas conclure en utilisant le théorème 1 page 336. On s’en sort en remarquant que \( f\left( {x, - x}\right)  = 2{x}^{4} - 8{x}^{2} =  - 2{x}^{2}(4 - \; \left. {x}^{2}\right)  < 0 \) pour \( 0 < \left| x\right|  < 2 \) . Par ailleurs \( f\left( {x, x}\right)  = 2{x}^{4} > 0 \) pour tout \( x \neq  0 \) . Ainsi, \( f \) ne présente ni maximum ni minimum relatif en \( \left( {0,0}\right) \) (on a affaire à un point col).

- At point \( \left( {0,0}\right) \), it is easy to see that the Hessian matrix of \( f \) is negative but not negative definite (we have \( r = t =  - 4 \) and \( s = 4 \)). Therefore, we cannot conclude using Theorem 1 on page 336. We can resolve this by noting that \( f\left( {x, - x}\right)  = 2{x}^{4} - 8{x}^{2} =  - 2{x}^{2}(4 - \; \left. {x}^{2}\right)  < 0 \) for \( 0 < \left| x\right|  < 2 \). Furthermore, \( f\left( {x, x}\right)  = 2{x}^{4} > 0 \) for all \( x \neq  0 \). Thus, \( f \) presents neither a relative maximum nor a relative minimum at \( \left( {0,0}\right) \) (we are dealing with a saddle point).

---

- Au point \( \left( {\sqrt{2}, - \sqrt{2}}\right) \) , comme \( \frac{{\partial }^{2}f}{\partial {x}^{2}} = {12}{x}^{2} - 4,\;\frac{{\partial }^{2}f}{\partial x\partial y} = 4,\;\frac{{\partial }^{2}f}{\partial {y}^{2}} = {12}{y}^{2} - 4 \) , on a \( r = {20} \) , \( s = 4 \) et \( t = {20} \) . Donc \( {rt} - {s}^{2} > 0 \) et \( r > 0 \) . La matrice hessienne de \( f \) en \( \left( {\sqrt{2}, - \sqrt{2}}\right) \) est donc définie positive, donc \( f \) admet un minimum relatif en ce point (égal à \( f\left( {\sqrt{2}, - \sqrt{2}}\right)  = \; - 8) \) .

> - At point \( \left( {\sqrt{2}, - \sqrt{2}}\right) \), since \( \frac{{\partial }^{2}f}{\partial {x}^{2}} = {12}{x}^{2} - 4,\;\frac{{\partial }^{2}f}{\partial x\partial y} = 4,\;\frac{{\partial }^{2}f}{\partial {y}^{2}} = {12}{y}^{2} - 4 \), we have \( r = {20} \), \( s = 4 \), and \( t = {20} \). Thus \( {rt} - {s}^{2} > 0 \) and \( r > 0 \). The Hessian matrix of \( f \) at \( \left( {\sqrt{2}, - \sqrt{2}}\right) \) is therefore positive definite, so \( f \) admits a relative minimum at this point (equal to \( f\left( {\sqrt{2}, - \sqrt{2}}\right)  = \; - 8) \)).

- Le résultat est identique en \( \left( {-\sqrt{2},\sqrt{2}}\right) \) car \( f \) vérifie la relation \( f\left( {x, y}\right)  = f\left( {-x, - y}\right) \) .

> - The result is identical at \( \left( {-\sqrt{2},\sqrt{2}}\right) \) because \( f \) satisfies the relation \( f\left( {x, y}\right)  = f\left( {-x, - y}\right) \).

Ainsi, les seuls extremums relatifs de \( f \) sont des minimums, atteints aux points \( \left( {\sqrt{2}, - \sqrt{2}}\right) \) et \( \left( {-\sqrt{2},\sqrt{2}}\right) \) . Nous allons prouver, par une technique générale, que ces minimums relatifs sont en fait des minimums absolus (c'est bien sûr faux dans le cas général). Il suffit pour cela de prouver que \( f \) admet bien un minimum absolu, car tout minimum absolu est un minimum relatif (et la valeur des deux minimums relatifs est la même dans notre cas).

> Thus, the only relative extremums of \( f \) are minimums, reached at points \( \left( {\sqrt{2}, - \sqrt{2}}\right) \) and \( \left( {-\sqrt{2},\sqrt{2}}\right) \). We will prove, using a general technique, that these relative minimums are in fact absolute minimums (this is of course false in the general case). It suffices to prove that \( f \) indeed admits an absolute minimum, because every absolute minimum is a relative minimum (and the value of the two relative minimums is the same in our case).

L’idée est de dire que lorsque \( \left| x\right| \) et \( \left| y\right| \) sont grands, \( 2{\left( x - y\right) }^{2} \) est petit par rapport à \( {x}^{4} + {y}^{4} \) . Pour cela, on utilise la norme \( \parallel \left( {x, y}\right) \parallel = \sup \{ \left| x\right| ,\left| y\right| \} \) et les inégalités

> The idea is to say that when \( \left| x\right| \) and \( \left| y\right| \) are large, \( 2{\left( x - y\right) }^{2} \) is small compared to \( {x}^{4} + {y}^{4} \). For this, we use the norm \( \parallel \left( {x, y}\right) \parallel = \sup \{ \left| x\right| ,\left| y\right| \} \) and the inequalities

\[
{x}^{4} + {y}^{4} \geq  \parallel \left( {x, y}\right) {\parallel }^{4},\;2{\left( x - y\right) }^{2} \leq  2{\left( 2\parallel \left( x, y\right) \parallel \right) }^{2} = 8\parallel \left( {x, y}\right) {\parallel }^{2}
\]

qui entraînent \( f\left( {x, y}\right) \geq \parallel \left( {x, y}\right) {\parallel }^{4} - 8\parallel \left( {x, y}\right) {\parallel }^{2} \) . Ainsi, \( \mathop{\lim }\limits_{{\parallel \left( {x, y}\right) \parallel \rightarrow + \infty }}f\left( {x, y}\right) = + \infty \) . On en déduit qu’il existe un compact \( K \) de \( {\mathbb{R}}^{2} \) tel que \( f\left( {x, y}\right) \geq 0 \) dès que \( \left( {x, y}\right) \notin K \) . La fonction \( f \) est continue sur le compact \( K \) , donc il existe \( \left( {a, b}\right) \in K \) tel que \( f\left( {a, b}\right) = \mathop{\inf }\limits_{{\left( {x, y}\right) \in K}}f\left( {x, y}\right) \) . Comme \( f\left( {-\sqrt{2},\sqrt{2}}\right) = - 8 \) , on a \( \left( {-\sqrt{2},\sqrt{2}}\right) \in K \) , et donc \( f\left( {a, b}\right) \leq - 8 \) . Comme \( f\left( {x, y}\right) \geq 0 \) pour \( \left( {x, y}\right) \notin K \) , on a en fait \( f\left( {x, y}\right) \geq f\left( {a, b}\right) \) pour tout \( \left( {x, y}\right) \in {\mathbb{R}}^{2} \) . Ainsi, \( f \) admet un minimum absolu sur \( {\mathbb{R}}^{2} \) , qui est donc un minimum relatif, donc égal à-8.

> which lead to \( f\left( {x, y}\right) \geq \parallel \left( {x, y}\right) {\parallel }^{4} - 8\parallel \left( {x, y}\right) {\parallel }^{2} \) . Thus, \( \mathop{\lim }\limits_{{\parallel \left( {x, y}\right) \parallel \rightarrow + \infty }}f\left( {x, y}\right) = + \infty \) . We deduce that there exists a compact set \( K \) of \( {\mathbb{R}}^{2} \) such that \( f\left( {x, y}\right) \geq 0 \) as soon as \( \left( {x, y}\right) \notin K \) . The function \( f \) is continuous on the compact set \( K \) , so there exists \( \left( {a, b}\right) \in K \) such that \( f\left( {a, b}\right) = \mathop{\inf }\limits_{{\left( {x, y}\right) \in K}}f\left( {x, y}\right) \) . Since \( f\left( {-\sqrt{2},\sqrt{2}}\right) = - 8 \) , we have \( \left( {-\sqrt{2},\sqrt{2}}\right) \in K \) , and therefore \( f\left( {a, b}\right) \leq - 8 \) . As \( f\left( {x, y}\right) \geq 0 \) for \( \left( {x, y}\right) \notin K \) , we actually have \( f\left( {x, y}\right) \geq f\left( {a, b}\right) \) for all \( \left( {x, y}\right) \in {\mathbb{R}}^{2} \) . Thus, \( f \) admits an absolute minimum on \( {\mathbb{R}}^{2} \) , which is therefore a relative minimum, and thus equal to -8.

Remarque. Pour montrer que \( f \) admet bien un minimum absolu égal à -8, on aurait pu montrer directement (en utilisant de bonnes minorations), que \( f\left( {x, y}\right) \geq - 8 \) pour tout \( \left( {x, y}\right) \in {\mathbb{R}}^{2} \) . L'avantage de la méthode que nous avons présentée est qu'elle est générale.

> Remark. To show that \( f \) indeed admits an absolute minimum equal to -8, we could have shown directly (using appropriate lower bounds) that \( f\left( {x, y}\right) \geq - 8 \) for all \( \left( {x, y}\right) \in {\mathbb{R}}^{2} \) . The advantage of the method we presented is that it is general.

EXERCICE 2. On note \( S = \left\{ {x \in {\mathbb{R}}^{n} \mid \parallel x\parallel = 1}\right\} \) la sphère unité de \( {\mathbb{R}}^{n} \) . Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction différentiable telle que \( {f}_{\mid S} \) (restriction de \( f \) à \( S \) ) soit constante. Montrer qu’il existe \( {x}_{0} \in {\mathbb{R}}^{n},\begin{Vmatrix}{x}_{0}\end{Vmatrix} < 1 \) , tel que \( d{f}_{{x}_{0}} = 0 \) .

> EXERCISE 2. Let \( S = \left\{ {x \in {\mathbb{R}}^{n} \mid \parallel x\parallel = 1}\right\} \) denote the unit sphere of \( {\mathbb{R}}^{n} \) . Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a differentiable function such that \( {f}_{\mid S} \) (the restriction of \( f \) to \( S \) ) is constant. Show that there exists \( {x}_{0} \in {\mathbb{R}}^{n},\begin{Vmatrix}{x}_{0}\end{Vmatrix} < 1 \) such that \( d{f}_{{x}_{0}} = 0 \) .

---

Solution. C’est l’équivalent du théorème de Rolle en dimension \( n \) . On procède comme sur \( \mathbb{R} \) .

> Solution. This is the equivalent of Rolle's theorem in dimension \( n \) . We proceed as on \( \mathbb{R} \) .

La boule unité fermée \( B \) de \( {\mathbb{R}}^{n} \) est compacte, et comme la fonction \( f \) est continue (car

> The closed unit ball \( B \) of \( {\mathbb{R}}^{n} \) is compact, and since the function \( f \) is continuous (because

différentiable), il existe \( {x}_{0} \in B \) tel que \( f\left( {x}_{0}\right) = \mathop{\min }\limits_{{x \in B}}f\left( x\right) = m \) et il existe \( {x}_{1} \in B \) tel que

> differentiable), there exists \( {x}_{0} \in B \) such that \( f\left( {x}_{0}\right) = \mathop{\min }\limits_{{x \in B}}f\left( x\right) = m \) and there exists \( {x}_{1} \in B \) such that

\( f\left( {x}_{1}\right) = \mathop{\max }\limits_{{x \in B}}f\left( x\right) = M. \)

> Si \( m = M \) , alors \( f \) est constante sur \( B \) , donc pour tout \( x \in {\mathbb{R}}^{n},\parallel x\parallel < 1, d{f}_{x} = 0 \) .

If \( m = M \) , then \( f \) is constant on \( B \) , so for all \( x \in {\mathbb{R}}^{n},\parallel x\parallel < 1, d{f}_{x} = 0 \) .

> Sinon, \( m < M \) , et comme \( f \) est constante sur \( S \) , l’un des points \( {x}_{0},{x}_{1} \) n’est pas dans \( S \) .

Otherwise, \( m < M \) , and since \( f \) is constant on \( S \) , one of the points \( {x}_{0},{x}_{1} \) is not in \( S \) .

> Supposons par exemple \( {x}_{0} \notin S \) . Alors \( \begin{Vmatrix}{x}_{0}\end{Vmatrix} < 1 \) , donc \( f \) prend sur l’ouvert \( B \) son minimum en

Suppose for example \( {x}_{0} \notin S \) . Then \( \begin{Vmatrix}{x}_{0}\end{Vmatrix} < 1 \) , so \( f \) attains its minimum on the open set \( B \) at

> \( {x}_{0} \) . Comme de plus \( f \) est différentiable en \( {x}_{0} \) , on en déduit \( d{f}_{{x}_{0}} = 0 \) .

\( {x}_{0} \) . Since, moreover, \( f \) is differentiable at \( {x}_{0} \) , we deduce \( d{f}_{{x}_{0}} = 0 \) .

---

EXERCICE 3 (PRINCIPE DU MAXIMUM). Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{2} \) . On définit le laplacien de \( f \) par

> EXERCISE 3 (MAXIMUM PRINCIPLE). Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{2} \) . We define the Laplacian of \( f \) by

\[
{\Delta f} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{\partial }^{2}f}{\partial {x}_{i}^{2}}.
\]

On note \( D \) la boule unité ouverte de \( {\mathbb{R}}^{n} \) et \( \bar{D} \) la boule unité fermée de \( {\mathbb{R}}^{n} \) . a) Si \( {\Delta f}\left( x\right) > 0 \) pour tout \( x \in D \) , montrer que pour tout \( x \in D, f\left( x\right) < \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . b) Si \( {\Delta f}\left( x\right) = 0 \) pour tout \( x \in D \) (on dit alors \( f \) est harmonique sur \( D \) ), montrer

> Let \( D \) denote the open unit ball of \( {\mathbb{R}}^{n} \) and \( \bar{D} \) the closed unit ball of \( {\mathbb{R}}^{n} \) . a) If \( {\Delta f}\left( x\right) > 0 \) for all \( x \in D \) , show that for all \( x \in D, f\left( x\right) < \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . b) If \( {\Delta f}\left( x\right) = 0 \) for all \( x \in D \) (we then say \( f \) is harmonic on \( D \) ), show

\[
\forall x \in  D,\;\mathop{\min }\limits_{{\parallel y\parallel  = 1}}f\left( y\right)  \leq  f\left( x\right)  \leq  \mathop{\max }\limits_{{\parallel y\parallel  = 1}}f\left( y\right) .
\]

Solution. a) Raisonnons par l’absurde en supposant l’existence de \( {x}_{0} \in D \) tel que \( f\left( {x}_{0}\right) \geq \; \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . L’application \( f \) est continue sur le compact \( \bar{D} \) , il existe donc \( x \in \bar{D} \) tel que \( f\left( x\right) = \mathop{\sup }\limits_{{y \in \bar{D}}}f\left( y\right) \) . Si \( f\left( x\right) = f\left( {x}_{0}\right) \) , on choisit \( x = {x}_{0} \) , sinon \( f\left( x\right) > f\left( {x}_{0}\right) \geq \mathop{\sup }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) , donc \( x \in D \) . Dans tous les cas, \( x \) appartient à l’ouvert \( D \) . On en déduit (voir le théorème 1 page 336) que \( d{f}_{x} = 0 \) et que la matrice hessienne

> Solution. a) Let us reason by contradiction by assuming the existence of \( {x}_{0} \in D \) such that \( f\left( {x}_{0}\right) \geq \; \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . The mapping \( f \) is continuous on the compact set \( \bar{D} \) , so there exists \( x \in \bar{D} \) such that \( f\left( x\right) = \mathop{\sup }\limits_{{y \in \bar{D}}}f\left( y\right) \) . If \( f\left( x\right) = f\left( {x}_{0}\right) \) , we choose \( x = {x}_{0} \) , otherwise \( f\left( x\right) > f\left( {x}_{0}\right) \geq \mathop{\sup }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) , so \( x \in D \) . In all cases, \( x \) belongs to the open set \( D \) . We deduce (see theorem 1 page 336) that \( d{f}_{x} = 0 \) and that the Hessian matrix

\[
A = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( x\right) \right) }_{1 \leq  i, j \leq  n}
\]

est négative. En particulier, la trace de \( A \) est négative (c’est la somme de ses valeurs propres), ce qui s’écrit \( {\Delta f}\left( x\right) \leq 0 \) . Ceci est contraire aux hypothèses, d’où le résultat.

> is negative. In particular, the trace of \( A \) is negative (it is the sum of its eigenvalues), which is written \( {\Delta f}\left( x\right) \leq 0 \) . This contradicts the hypotheses, hence the result.

b) Nous montrons que pour tout \( x \in D, f\left( x\right) \leq \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) , l’autre inégalité s’en déduisant ensuite en considérant \( - f \) .

> b) We show that for all \( x \in D, f\left( x\right) \leq \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) , the other inequality is then deduced by considering \( - f \) .

Soit \( \varepsilon > 0 \) . Considérons la fonction \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) définie par \( g\left( x\right) = f\left( x\right) + \varepsilon \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2}}\right) \) . On a \( {\Delta g} = {\Delta f} + {2n\varepsilon } \) , ce qui montre que \( {\Delta g} > 0 \) sur \( D \) . D’après la question précédente, on en déduit, pour tout \( x \in D \) ,

> Let \( \varepsilon > 0 \) . Consider the function \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) defined by \( g\left( x\right) = f\left( x\right) + \varepsilon \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2}}\right) \) . We have \( {\Delta g} = {\Delta f} + {2n\varepsilon } \) , which shows that \( {\Delta g} > 0 \) on \( D \) . From the previous question, we deduce, for all \( x \in D \) ,

\[
g\left( x\right)  < \mathop{\max }\limits_{{\parallel y\parallel  = 1}}g\left( y\right) \;\text{ donc }\;f\left( x\right)  + \varepsilon \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2}}\right)  < \mathop{\max }\limits_{{\parallel y\parallel  = 1}}f\left( y\right)  + \varepsilon \left( {\mathop{\max }\limits_{{\parallel y\parallel  = 1}}\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}^{2}}\right) .
\]

Ceci étant vrai pour tout \( \varepsilon > 0 \) , on en déduit que \( f\left( x\right) \leq \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . D’où le résultat.

> Since this is true for all \( \varepsilon > 0 \) , we deduce that \( f\left( x\right) \leq \mathop{\max }\limits_{{\parallel y\parallel = 1}}f\left( y\right) \) . Hence the result.

Remarque. Le résultat se généralise aisément sous la forme suivante : si \( f \) est continue sur un compact \( K \) et harmonique sur l’intérieur de \( K \) , alors \( f \) atteint son maximum et son minimum sur la frontière de \( K \) .

> Remark. The result generalizes easily in the following form: if \( f \) is continuous on a compact set \( K \) and harmonic on the interior of \( K \) , then \( f \) reaches its maximum and minimum on the boundary of \( K \) .

EXERCICE 4 (EXEMPLES D'APPLICATIONS DU THÉORÉME DES EXTREMUMS LIÉS).

> EXERCISE 4 (EXAMPLES OF APPLICATIONS OF THE THEOREM OF LAGRANGE MULTIPLIERS).

a) Soient \( n \in {\mathbb{N}}^{ * }, n \geq 2 \) , et \( s > 0 \) . Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1}\cdots {x}_{n} \) , et \( \Gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{ + }\right) }^{n} \mid \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = s}\right\} \) . Étudier le maximum global de \( {f}_{\mid \Gamma } \) , la restriction de \( f \) à \( \Gamma \) . Retrouver ainsi l’inégalité arithmético-géométrique.

> a) Let \( n \in {\mathbb{N}}^{ * }, n \geq 2 \) , and \( s > 0 \) . Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1}\cdots {x}_{n} \) , and \( \Gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{ + }\right) }^{n} \mid \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i} = s}\right\} \) . Study the global maximum of \( {f}_{\mid \Gamma } \) , the restriction of \( f \) to \( \Gamma \) . Thereby recover the arithmetic-geometric mean inequality.

b) On se donne un entier \( n \geq 2 \) et \( n \) réels strictement positifs \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) . On note

> b) Let \( n \geq 2 \) be an integer and \( n \) be strictly positive real numbers \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) . We denote

\[
\Gamma  = \left\{  {\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n} \mid  \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{x}_{i}^{4}}{{\lambda }_{i}^{4}} = 1}\right\}  .
\]

Si \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2} \) , déterminer le maximum global de \( {f}_{\mid \Gamma } \) . c) Soient \( {a}_{1},\ldots ,{a}_{n} \) des réels \( > 0 \) tels que \( {a}_{1} + \cdots + {a}_{n} = 1 \) (avec \( n \geq 2 \) ). Démontrer que

> If \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2} \) , determine the global maximum of \( {f}_{\mid \Gamma } \) . c) Let \( {a}_{1},\ldots ,{a}_{n} \) be real numbers \( > 0 \) such that \( {a}_{1} + \cdots + {a}_{n} = 1 \) (with \( n \geq 2 \) ). Prove that

\[
\mathop{\prod }\limits_{{i = 1}}^{n}{a}_{i}\left( {1 - {a}_{i}}\right)  \leq  \frac{{\left( n - 1\right) }^{n}}{{n}^{2n}}
\]

Solution. a) La fonction \( f \) étant continue sur le compact \( \Gamma ,{f}_{\mid \Gamma } \) admet un maximum global atteint en un point \( a \) de \( \Gamma \) . Si on note \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1} + \cdots + {x}_{n} - s \) et \( \gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid g\left( x\right) = 0}\right\} \) , alors \( a \in \Omega = \gamma \cap {\left( {\mathbb{R}}^{+ * }\right) }^{n} \subset \Gamma \) (car \( f\left( x\right) = 0 \) si l’un des \( {x}_{i} \) est nul, et \( f\left( x\right) > 0 \) si \( x \in \gamma ) \) . Par construction, \( {f}_{\mid \Omega } \) admet un extremum global en \( a \) , et comme \( \Omega \) est un ouvert de \( \gamma ,{f}_{\mid \gamma } \) atteint un extremum local en \( a \) . De plus, si \( a \in \gamma \) , alors \( d{g}_{a} \neq 0 \) , on peut donc appliquer le théorème des extremums liés qui entraîne l’existence de \( \lambda \in \mathbb{R} \) tel que \( d{f}_{a} = {\lambda d}{g}_{a} \) . On a donc

> Solution. a) Since the function \( f \) is continuous on the compact set \( \Gamma ,{f}_{\mid \Gamma } \), it admits a global maximum attained at a point \( a \) in \( \Gamma \). If we denote \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1} + \cdots + {x}_{n} - s \) and \( \gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid g\left( x\right) = 0}\right\} \), then \( a \in \Omega = \gamma \cap {\left( {\mathbb{R}}^{+ * }\right) }^{n} \subset \Gamma \) (because \( f\left( x\right) = 0 \) if one of the \( {x}_{i} \) is zero, and \( f\left( x\right) > 0 \) if \( x \in \gamma ) \). By construction, \( {f}_{\mid \Omega } \) admits a global extremum at \( a \), and since \( \Omega \) is an open subset of \( \gamma ,{f}_{\mid \gamma } \), it attains a local extremum at \( a \). Furthermore, if \( a \in \gamma \), then \( d{g}_{a} \neq 0 \), so we can apply the theorem of constrained extrema, which implies the existence of \( \lambda \in \mathbb{R} \) such that \( d{f}_{a} = {\lambda d}{g}_{a} \). We therefore have

\[
\forall i \in  \{ 1,\ldots , n\} ,\;\frac{\partial f}{\partial {x}_{i}}\left( a\right)  = \lambda \frac{\partial g}{\partial {x}_{i}} = \lambda \;\text{ c’est-à-dire }\;\frac{f\left( a\right) }{{a}_{i}} = \lambda .
\]

Or \( f\left( a\right) \neq 0 \) , on en déduit que tous les \( {a}_{i} \) sont égaux. Comme \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i} = s \) , on a \( {a}_{i} = s/n \) pour tout \( i \) . La valeur du maximum recherché est donc \( {\left( s/n\right) }^{n} \) .

> However, \( f\left( a\right) \neq 0 \), from which we deduce that all \( {a}_{i} \) are equal. Since \( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i} = s \), we have \( {a}_{i} = s/n \) for all \( i \). The value of the sought maximum is therefore \( {\left( s/n\right) }^{n} \).

Ceci s'écrit aussi

> This can also be written as

\[
\forall \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\left( {\mathbb{R}}^{ + }\right) }^{n},\;\mathop{\prod }\limits_{{i = 1}}^{n}{x}_{i} \leq  {\left( \frac{\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}}{n}\right) }^{n}\;\text{ c’est-à-dire }{\left( \mathop{\prod }\limits_{{i = 1}}^{n}{x}_{i}\right) }^{1/n} \leq  \frac{\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}}{n},
\]

ce qui n'est autre que l'inégalité arithmético-géométrique.

> which is none other than the arithmetic-geometric mean inequality.

b) La fonction \( f \) est continue sur le compact \( \Gamma \) , il existe donc \( a \in \Gamma \) tel que \( {f}_{\mid \Gamma } \) atteigne son maximum global en \( a \) .

> b) The function \( f \) is continuous on the compact set \( \Gamma \), so there exists \( a \in \Gamma \) such that \( {f}_{\mid \Gamma } \) attains its global maximum at \( a \).

On note \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{i}{x}_{i}^{4}/{\lambda }_{i}^{4} - 1 \) , de sorte que \( \Gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid g\left( x\right) = 0}\right\} \) . Comme \( g \) est de classe \( {\mathcal{C}}^{1} \) et que \( d{g}_{x} \neq 0 \) pour tout \( x \in \Gamma \) (si \( d{g}_{x} = 4\mathop{\sum }\limits_{i}\left( {{x}_{i}^{3}/{\lambda }_{i}^{4}}\right) d{x}_{i} = 0 \) , alors \( {x}_{i} = 0 \) pour tout \( i \) donc \( x \notin \Gamma \) ), on peut appliquer le théorème des extremums liés qui entraîne l’existence de \( \mu \in \mathbb{R} \) tel que \( d{f}_{a} = {\mu d}{g}_{a} \) . On en conclut

> Let \( g : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\sum }\limits_{i}{x}_{i}^{4}/{\lambda }_{i}^{4} - 1 \), such that \( \Gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid g\left( x\right) = 0}\right\} \). Since \( g \) is of class \( {\mathcal{C}}^{1} \) and \( d{g}_{x} \neq 0 \) for all \( x \in \Gamma \) (if \( d{g}_{x} = 4\mathop{\sum }\limits_{i}\left( {{x}_{i}^{3}/{\lambda }_{i}^{4}}\right) d{x}_{i} = 0 \), then \( {x}_{i} = 0 \) for all \( i \), so \( x \notin \Gamma \)), we can apply the theorem of constrained extrema, which implies the existence of \( \mu \in \mathbb{R} \) such that \( d{f}_{a} = {\mu d}{g}_{a} \). We conclude

\[
\forall i,\;2{a}_{i} = \frac{\partial f}{\partial {x}_{i}}\left( a\right)  = \mu \frac{\partial g}{\partial {x}_{i}}\left( a\right)  = \mu \frac{4{a}_{i}^{3}}{{\lambda }_{i}^{4}}\;\text{ donc }\;{a}_{i}\left( {1 - {2\mu }\frac{{a}_{i}^{2}}{{\lambda }_{i}^{4}}}\right)  = 0.
\]

Pour tout \( i \) , on en déduit que \( {a}_{i} = 0 \) ou \( {a}_{i}^{2} = {\lambda }_{i}^{4}/\left( {2\mu }\right) \) . Notons \( I \) l’ensemble des indices \( i \) pour lesquels \( {a}_{i} \neq 0 \) . L’ensemble \( I \) est non vide car \( a \neq 0 \) (car \( a \in \Gamma \) ). On a

> For all \( i \), we deduce that \( {a}_{i} = 0 \) or \( {a}_{i}^{2} = {\lambda }_{i}^{4}/\left( {2\mu }\right) \). Let \( I \) be the set of indices \( i \) for which \( {a}_{i} \neq 0 \). The set \( I \) is non-empty because \( a \neq 0 \) (since \( a \in \Gamma \)). We have

\[
\mathop{\sum }\limits_{{i = 1}}^{n}\frac{{a}_{i}^{4}}{{\lambda }_{i}^{4}} = 1 = \mathop{\sum }\limits_{{i \in  I}}\frac{{a}_{i}^{4}}{{\lambda }_{i}^{4}} = \mathop{\sum }\limits_{{i \in  I}}\frac{{\lambda }_{i}^{4}}{4{\mu }^{2}}\;\text{ donc }\;4{\mu }^{2} = \mathop{\sum }\limits_{{i \in  I}}{\lambda }_{i}^{4},
\]

et on en déduit

> and we deduce

\[
\forall i \in  I,\;{a}_{i}^{2} = \frac{{\lambda }_{i}^{4}}{2\mu } = \frac{{\lambda }_{i}^{4}}{\sqrt{\mathop{\sum }\limits_{{i \in  I}}{\lambda }_{i}^{4}}}\;\text{ donc }\;f\left( a\right)  = \mathop{\sum }\limits_{i}{a}_{i}^{2} = \sqrt{\mathop{\sum }\limits_{{i \in  I}}{\lambda }_{i}^{4}}.
\]

Résumons : nous avons montré que \( f\left( a\right) \) est nécessairement égal à \( \sqrt{\mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}^{4}} \) où \( I \) est un sous-ensemble de \( \{ 1,\ldots , n\} \) . Réciproquement, il est immédiat que tout élément de cette forme peut-être atteint (définir les \( {a}_{i} \) comme précédemment si \( i \in I,{a}_{i} = 0 \) si \( i \notin I \) ). Comme \( f\left( a\right) \) est maximal, ceci montre que le maximum de \( {f}_{\mid \Gamma } \) est atteint lorsque \( I = \{ 1,\ldots , n\} \) , donc égal à \( {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{4}\right) }^{1/2} \)

> In summary: we have shown that \( f\left( a\right) \) is necessarily equal to \( \sqrt{\mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}^{4}} \) where \( I \) is a subset of \( \{ 1,\ldots , n\} \). Conversely, it is immediate that any element of this form can be reached (define the \( {a}_{i} \) as before if \( i \in I,{a}_{i} = 0 \) if \( i \notin I \)). Since \( f\left( a\right) \) is maximal, this shows that the maximum of \( {f}_{\mid \Gamma } \) is reached when \( I = \{ 1,\ldots , n\} \), thus equal to \( {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{4}\right) }^{1/2} \)

c) Soit \( \varphi : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\prod }\limits_{{i = 1}}^{n}{x}_{i}\left( {1 - {x}_{i}}\right) \) . Il s’agit d’évaluer le maximum de \( {\varphi }_{\mid \Gamma } \) , où \( \Gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{+ * }\right) }^{n} \mid \mathop{\sum }\limits_{i}{x}_{i} = 1}\right\} \) . La fonction \( \varphi \) étant continue sur le compact \( \gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{ + }\right) }^{n} \mid \mathop{\sum }\limits_{i}{x}_{i} = 1}\right\} \) , il existe \( a \in \gamma \) tel que \( \varphi \left( a\right) = \mathop{\sup }\limits_{{x \in \gamma }}\varphi \left( x\right) \) . Si l’un des \( {a}_{i} \) est nul, alors \( \varphi \left( a\right) = 0 \) , ce qui contredit la maximalité de \( \varphi \left( a\right) \) . On a donc \( a \in \Gamma \) .

> c) Let \( \varphi : {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto \mathop{\prod }\limits_{{i = 1}}^{n}{x}_{i}\left( {1 - {x}_{i}}\right) \). We must evaluate the maximum of \( {\varphi }_{\mid \Gamma } \), where \( \Gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{+ * }\right) }^{n} \mid \mathop{\sum }\limits_{i}{x}_{i} = 1}\right\} \). Since the function \( \varphi \) is continuous on the compact set \( \gamma = \left\{ {\left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\left( {\mathbb{R}}^{ + }\right) }^{n} \mid \mathop{\sum }\limits_{i}{x}_{i} = 1}\right\} \), there exists \( a \in \gamma \) such that \( \varphi \left( a\right) = \mathop{\sup }\limits_{{x \in \gamma }}\varphi \left( x\right) \). If one of the \( {a}_{i} \) is zero, then \( \varphi \left( a\right) = 0 \), which contradicts the maximality of \( \varphi \left( a\right) \). We therefore have \( a \in \Gamma \).

En d’autres termes, si \( f \) désigne la restriction de \( \varphi \) à l’ouvert \( {\left( {\mathbb{R}}^{+ * }\right) }^{n} \) , nous avons montré l’existence de \( a \in \Gamma \) tel que \( f\left( a\right) = \varphi \left( a\right) = \mathop{\sup }\limits_{{x \in \Gamma }}f\left( x\right) \) .

> In other words, if \( f \) denotes the restriction of \( \varphi \) to the open set \( {\left( {\mathbb{R}}^{+ * }\right) }^{n} \), we have shown the existence of \( a \in \Gamma \) such that \( f\left( a\right) = \varphi \left( a\right) = \mathop{\sup }\limits_{{x \in \Gamma }}f\left( x\right) \).

Soit \( g \) la fonction \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1} + \cdots + {x}_{n} - 1 \) , de sorte que \( \Gamma = \left\{ {x \in {\left( {\mathbb{R}}^{+ * }\right) }^{n} \mid g\left( x\right) = 0}\right\} \) . La fonction \( g \) est de classe \( {\mathcal{C}}^{1} \) et \( d{g}_{x} \neq 0 \) pour tout \( x \in \Gamma \) , on peut donc appliquer le théorème des extremums liés qui entraîne l’existence de \( \lambda \in \mathbb{R} \) tel que \( d{f}_{a} = {\lambda d}{g}_{a} \) . Ceci entraîne, pour tout \( i \) ,

> Let \( g \) be the function \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{1} + \cdots + {x}_{n} - 1 \) , such that \( \Gamma = \left\{ {x \in {\left( {\mathbb{R}}^{+ * }\right) }^{n} \mid g\left( x\right) = 0}\right\} \) . The function \( g \) is of class \( {\mathcal{C}}^{1} \) and \( d{g}_{x} \neq 0 \) for all \( x \in \Gamma \) , so we can apply the theorem of constrained extrema which implies the existence of \( \lambda \in \mathbb{R} \) such that \( d{f}_{a} = {\lambda d}{g}_{a} \) . This implies, for all \( i \) ,

\[
\frac{\partial f}{\partial {x}_{i}}\left( a\right)  = \lambda \frac{\partial g}{\partial {x}_{i}}\;\text{ c’est-à-dire }\;\frac{f\left( a\right) }{{a}_{i}\left( {1 - {a}_{i}}\right) }\left( {1 - 2{a}_{i}}\right)  = \lambda .
\]

(*)

> Autrement dit, chaque \( {a}_{i} \) est solution de l’équation \( F\left( X\right) = \lambda {X}^{2} - {\lambda X} - {2f}\left( a\right) X + f\left( a\right) = 0 \) . Comme l’un au moins des \( {a}_{i} \) est inférieur à \( 1/n \) (car \( \mathop{\sum }\limits_{i}{a}_{i} = 1 \) ), donc inférieur à \( 1/2 \) , et que \( {a}_{i} \in \rbrack 0,1\left\lbrack \right. \) , la dernière égalité de (*) montre que \( \lambda \geq 0 \) . Si \( \lambda > 0, F \) est une fonction polynôme de degré 2 qui vérifie \( F\left( 0\right) = f\left( a\right) > 0, F\left( 1\right) = - f\left( a\right) < 0 \) et \( \mathop{\lim }\limits_{{X \rightarrow + \infty }}F\left( X\right) = + \infty \) , donc \( F \) a ses deux racines réelles, l’une dans \( \rbrack 0,1\left\lbrack \text{ , l’autre dans }\right\rbrack 1, + \infty \lbrack \) . Si \( \lambda = 0, F \) est affine donc a au plus une solution dans ]0,1 [. Dans tous les cas, \( F \) a donc au plus une solution dans ]0,1 [. Comme tous les \( {a}_{i} \) sont dans ]0,1 [, et que \( F\left( {a}_{i}\right) = 0 \) pour tout \( i \) , on en déduit que les \( {a}_{i} \) sont égaux. Leur somme est égal à 1, donc \( {a}_{i} = 1/n \) pour tout \( i \) .

In other words, each \( {a}_{i} \) is a solution to the equation \( F\left( X\right) = \lambda {X}^{2} - {\lambda X} - {2f}\left( a\right) X + f\left( a\right) = 0 \) . Since at least one of the \( {a}_{i} \) is less than \( 1/n \) (because \( \mathop{\sum }\limits_{i}{a}_{i} = 1 \) ), and thus less than \( 1/2 \) , and since \( {a}_{i} \in \rbrack 0,1\left\lbrack \right. \) , the last equality of (*) shows that \( \lambda \geq 0 \) . If \( \lambda > 0, F \) is a polynomial function of degree 2 that satisfies \( F\left( 0\right) = f\left( a\right) > 0, F\left( 1\right) = - f\left( a\right) < 0 \) and \( \mathop{\lim }\limits_{{X \rightarrow + \infty }}F\left( X\right) = + \infty \) , then \( F \) has its two real roots, one in \( \rbrack 0,1\left\lbrack \text{ , l’autre dans }\right\rbrack 1, + \infty \lbrack \) . If \( \lambda = 0, F \) is affine, it therefore has at most one solution in ]0,1 [. In any case, \( F \) therefore has at most one solution in ]0,1 [. Since all \( {a}_{i} \) are in ]0,1 [, and \( F\left( {a}_{i}\right) = 0 \) for all \( i \) , we deduce that the \( {a}_{i} \) are equal. Their sum is equal to 1, so \( {a}_{i} = 1/n \) for all \( i \) .

> Finalement, nous avons montré

Finally, we have shown

\[
\mathop{\max }\limits_{{x \in  \Gamma }}f\left( x\right)  = f\left( a\right)  = f\left( {\frac{1}{n},\ldots ,\frac{1}{n}}\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}\frac{1}{n}\left( {1 - \frac{1}{n}}\right)  = \frac{{\left( n - 1\right) }^{n}}{{n}^{2n}}.
\]

Remarque. On aura pu répondre à la question c) en appliquant l'inégalité arithmético-géométrique aux deux produits \( \mathop{\prod }\limits_{i}{a}_{i} \) et \( \mathop{\prod }\limits_{i}\left( {1 - {a}_{i}}\right) \) .

> Remark. One could have answered question c) by applying the arithmetic-geometric mean inequality to the two products \( \mathop{\prod }\limits_{i}{a}_{i} \) and \( \mathop{\prod }\limits_{i}\left( {1 - {a}_{i}}\right) \) .

EXERCICE 5. Soit \( n \in {\mathbb{N}}^{ * } \) . On munit \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) de la norme \( \parallel M{\parallel }_{2} = {\left( \mathop{\sum }\limits_{{i, j}}{m}_{i, j}^{2}\right) }^{1/2} \) , où les \( {m}_{i, j} \) sont les coefficients de la matrice \( M \) . Montrer que le groupe des matrices orthogonales directes \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) est l’ensemble des éléments de \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) : \det \left( M\right) = 1}\right\} \) de norme minimale.

> EXERCISE 5. Let \( n \in {\mathbb{N}}^{ * } \) . Equip \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) with the norm \( \parallel M{\parallel }_{2} = {\left( \mathop{\sum }\limits_{{i, j}}{m}_{i, j}^{2}\right) }^{1/2} \) , where the \( {m}_{i, j} \) are the coefficients of the matrix \( M \) . Show that the group of special orthogonal matrices \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) is the set of elements of \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) : \det \left( M\right) = 1}\right\} \) with minimal norm.

Solution. On remarque déjà que \( \parallel M{\parallel }_{2}^{2} = \operatorname{tr}\left( {{}^{t}{MM}}\right) \) . Il s’agit donc de minimiser \( f\left( M\right) = \; \operatorname{tr}\left( {{}^{t}{MM}}\right) \) sous la contrainte \( g\left( M\right) = 0 \) , avec \( g\left( M\right) = \det \left( M\right) - 1 \) .

> Solution. We first note that \( \parallel M{\parallel }_{2}^{2} = \operatorname{tr}\left( {{}^{t}{MM}}\right) \) . We must therefore minimize \( f\left( M\right) = \; \operatorname{tr}\left( {{}^{t}{MM}}\right) \) under the constraint \( g\left( M\right) = 0 \) , with \( g\left( M\right) = \det \left( M\right) - 1 \) .

L’application \( f \) est une forme quadratique et \( g \) est une forme multilinéaire sur un e.v de dimension finie, donc \( f \) et \( g \) sont continues. L’ensemble \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) = {g}^{-1}\left( {\{ 0\} }\right) \) est un fermé de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , donc le minimum de \( f \) sur \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) est atteint en un point \( A \) de \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) (en effet : dans tout e.v de dimension finie \( E \) , la distance \( d \) de 0 à un fermé \( F \) de \( E \) est toujours atteinte, puisqu’elle est atteinte sur le compact \( K \) des éléments \( x \) de \( F \) de norme \( \parallel x\parallel \leq d + 1 \) , et \( \parallel x\parallel > d + 1 \) en dehors de \( K \) ). La différentielle du déterminant a déjà été calculée dans l'exercice 6 page 332, et donne \( d{g}_{A}\left( H\right) = \operatorname{tr}\left( {{}^{t}{CH}}\right) \) où \( C \) est la comatrice de \( A \) . Ainsi, \( d{g}_{A} \) n’est pas nul, et le théorème des extremums liés nous assure donc l’existence de \( \lambda \in \mathbb{R} \) tel que les différentielles de \( f \) et \( g \) en \( A \) vérifient \( d{f}_{A} = {\lambda d}{g}_{A} \) .

> The map \( f \) is a quadratic form and \( g \) is a multilinear form on a finite-dimensional vector space, so \( f \) and \( g \) are continuous. The set \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) = {g}^{-1}\left( {\{ 0\} }\right) \) is a closed subset of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , so the minimum of \( f \) on \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) is attained at a point \( A \) in \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) (indeed: in any finite-dimensional vector space \( E \) , the distance \( d \) from 0 to a closed set \( F \) of \( E \) is always attained, since it is attained on the compact set \( K \) of elements \( x \) of \( F \) with norm \( \parallel x\parallel \leq d + 1 \) , and \( \parallel x\parallel > d + 1 \) outside \( K \) ). The differential of the determinant has already been calculated in exercise 6 on page 332, and gives \( d{g}_{A}\left( H\right) = \operatorname{tr}\left( {{}^{t}{CH}}\right) \) where \( C \) is the comatrix of \( A \) . Thus, \( d{g}_{A} \) is non-zero, and the theorem of constrained extrema therefore ensures the existence of \( \lambda \in \mathbb{R} \) such that the differentials of \( f \) and \( g \) at \( A \) satisfy \( d{f}_{A} = {\lambda d}{g}_{A} \) .

Compte tenu de l’expression \( f\left( {A + H}\right) = \operatorname{tr}\left( {{}^{t}{AA}}\right) + 2\operatorname{tr}\left( {{}^{t}{AH}}\right) + \operatorname{tr}\left( {{}^{t}{HH}}\right) = f\left( A\right) + 2\operatorname{tr}\left( {{}^{t}{AH}}\right) + \; \parallel H{\parallel }^{2} \) , on voit que \( d{f}_{A}\left( H\right) = 2\operatorname{tr}\left( {{}^{t}{AH}}\right) \) . Par ailleurs, on a vu que \( d{g}_{A}\left( H\right) = \operatorname{tr}\left( {{}^{t}{AH}}\right) \) donc \( 2\operatorname{tr}\left( {{}^{t}{AH}}\right) = \lambda \operatorname{tr}\left( {{}^{t}{CH}}\right) \) pour toute matrice \( H \) , ce qui entraîne \( {2A} = {\lambda C} \) (en remplaçant \( H \) par les matrices \( {E}_{i, j} \) dont tous les coefficients sont nuls sauf le \( \left( {i, j}\right) \) -ième qui vaut 1, on obtient l’égalité des \( \left( {i, j}\right) \) -ièmes coordonnées de \( {2A} \) et \( {\lambda C} \) ). Comme \( A \) est inversible et que \( \det \left( A\right) = 1 \) , sa comatrice s’exprime aussi sous la forme \( C = {}^{t}{A}^{-1} \) , donc on a \( 2{}^{t}{AA} = \lambda {I}_{n} \) . En composant par le déterminant, on en déduit \( {2}^{n} = {\lambda }^{n} \) et comme \( {}^{t}{AA} \) est une matrice positive, on a forcément \( \lambda > 0 \) donc \( \lambda = 2 \) . Ainsi, \( {}^{t}{AA} = {I}_{n} \) , c’est-à-dire \( A \in {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) . On a donc démontré que le minimum de \( f \) sur \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) était forcément atteint en un point \( A \) de \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) . Ce minimum est égal à \( \operatorname{tr}\left( {{}^{t}{AA}}\right) = \operatorname{tr}\left( {I}_{n}\right) = n \) . Réciproquement, tous les éléments \( M \) de \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) vérifient \( f\left( M\right) = n \) , d’où le résultat.

> Given the expression \( f\left( {A + H}\right) = \operatorname{tr}\left( {{}^{t}{AA}}\right) + 2\operatorname{tr}\left( {{}^{t}{AH}}\right) + \operatorname{tr}\left( {{}^{t}{HH}}\right) = f\left( A\right) + 2\operatorname{tr}\left( {{}^{t}{AH}}\right) + \; \parallel H{\parallel }^{2} \), we see that \( d{f}_{A}\left( H\right) = 2\operatorname{tr}\left( {{}^{t}{AH}}\right) \). Furthermore, we have seen that \( d{g}_{A}\left( H\right) = \operatorname{tr}\left( {{}^{t}{AH}}\right) \) therefore \( 2\operatorname{tr}\left( {{}^{t}{AH}}\right) = \lambda \operatorname{tr}\left( {{}^{t}{CH}}\right) \) for any matrix \( H \), which implies \( {2A} = {\lambda C} \) (by replacing \( H \) with the matrices \( {E}_{i, j} \) whose coefficients are all zero except the \( \left( {i, j}\right) \)-th which is 1, we obtain the equality of the \( \left( {i, j}\right) \)-th coordinates of \( {2A} \) and \( {\lambda C} \)). Since \( A \) is invertible and \( \det \left( A\right) = 1 \), its comatrix is also expressed in the form \( C = {}^{t}{A}^{-1} \), so we have \( 2{}^{t}{AA} = \lambda {I}_{n} \). By composing with the determinant, we deduce \( {2}^{n} = {\lambda }^{n} \) and since \( {}^{t}{AA} \) is a positive matrix, we necessarily have \( \lambda > 0 \) therefore \( \lambda = 2 \). Thus, \( {}^{t}{AA} = {I}_{n} \), that is to say \( A \in {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \). We have therefore shown that the minimum of \( f \) on \( {\mathcal{{SL}}}_{n}\left( \mathbb{R}\right) \) was necessarily reached at a point \( A \) of \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \). This minimum is equal to \( \operatorname{tr}\left( {{}^{t}{AA}}\right) = \operatorname{tr}\left( {I}_{n}\right) = n \). Conversely, all elements \( M \) of \( {\mathcal{{SO}}}_{n}\left( \mathbb{R}\right) \) satisfy \( f\left( M\right) = n \), hence the result.
