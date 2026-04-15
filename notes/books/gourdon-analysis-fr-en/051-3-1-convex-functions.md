#### 3.1. Convex functions

*Français : 3.1. Fonctions convexes*

Dans toute cette sous-partie, \( I \) désigne un intervalle de \( \mathbb{R} \) non réduit à un singleton.

> Throughout this subsection, \( I \) denotes an interval of \( \mathbb{R} \) not reduced to a singleton.

DéFINITION 1. Une application \( f : I \rightarrow \mathbb{R} \) est dite convexe si

> DEFINITION 1. A mapping \( f : I \rightarrow \mathbb{R} \) is said to be convex if

\[
\forall \left( {a, b}\right)  \in  {I}^{2},\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;f\left\lbrack  {\left( {1 - \lambda }\right) a + {\lambda b}}\right\rbrack   \leq  \left( {1 - \lambda }\right) f\left( a\right)  + {\lambda f}\left( b\right) .
\]

(*)

> Elle est dite concave si - \( f \) est convexe.

It is said to be concave if - \( f \) is convex.

> Remarque 1. - Lorsque l’inégalité (*) est stricte pour tout \( \lambda \in \rbrack 0,1\lbrack \) (lorsque \( a \neq b \) ) on dit que \( f \) est strictement convexe.

Remark 1. - When the inequality (*) is strict for all \( \lambda \in \rbrack 0,1\lbrack \) (when \( a \neq b \) ) we say that \( f \) is strictly convex.

> - La fonction \( f \) est convexe si et seulement si l’ensemble \( \{ \left( {x, y}\right)  \in  I \times  \mathbb{R} \mid  y \geq  f\left( x\right) \} \) est convexe.

- The function \( f \) is convex if and only if the set \( \{ \left( {x, y}\right)  \in  I \times  \mathbb{R} \mid  y \geq  f\left( x\right) \} \) is convex.

> - L'inégalité (*) exprime le fait que tous les points du segment \( \left\lbrack  {\left( {a, f\left( a\right) }\right) ,\left( {b, f\left( b\right) }\right) }\right\rbrack \) sont au dessus du graphe de \( f \) .

- The inequality (*) expresses the fact that all points of the segment \( \left\lbrack  {\left( {a, f\left( a\right) }\right) ,\left( {b, f\left( b\right) }\right) }\right\rbrack \) are above the graph of \( f \) .

> Proposition 1. Une application \( f : I \rightarrow \mathbb{R} \) est convexe si et seulement si pour tout \( {x}_{0} \in I \) , l’application

Proposition 1. A mapping \( f : I \rightarrow \mathbb{R} \) is convex if and only if for all \( {x}_{0} \in I \) , the mapping

\[
{g}_{{x}_{0}} : I \smallsetminus  \left\{  {x}_{0}\right\}   \rightarrow  \mathbb{R}\;x \mapsto  {g}_{{x}_{0}}\left( x\right)  = \frac{f\left( x\right)  - f\left( {x}_{0}\right) }{x - {x}_{0}}
\]

![bo_d7fjkrs91nqc73ereoog_100_557_235_564_261_0.jpg](images/gourdon_analysis_fr_en_004_bod7fjkrs91nqc73ereoog1005572355642610.jpg)

Figure 6. Entre \( a \) et \( b \) , les points du graphe de la fonction convexe \( f \) se trouvent en dessous de la corde reliant les points \( \left( {a, f\left( a\right) }\right) \) et \( \left( {b, f\left( b\right) }\right) \) .

> Figure 6. Between \( a \) and \( b \) , the points of the graph of the convex function \( f \) lie below the chord connecting points \( \left( {a, f\left( a\right) }\right) \) and \( \left( {b, f\left( b\right) }\right) \) .

est croissante.

> is increasing.

Conséquence : Si \( f : I \rightarrow \mathbb{R} \) est convexe et si \( a, b, c \in I \) , avec \( a < b < c \) , on a (en appliquant la proposition précédente à \( {g}_{a} \) puis à \( {g}_{c} \) ) l’inégalité suivante entre les taux de variation (voir aussi la figure ci-contre)

> Consequence: If \( f : I \rightarrow \mathbb{R} \) is convex and if \( a, b, c \in I \) , with \( a < b < c \) , we have (by applying the previous proposition to \( {g}_{a} \) then to \( {g}_{c} \) ) the following inequality between the rates of change (see also the figure opposite)

\[
\frac{f\left( b\right)  - f\left( a\right) }{b - a} \leq  \frac{f\left( c\right)  - f\left( a\right) }{c - a} \leq  \frac{f\left( c\right)  - f\left( b\right) }{c - b}.
\]

![bo_d7fjkrs91nqc73ereoog_100_525_958_616_329_0.jpg](images/gourdon_analysis_fr_en_003_bod7fjkrs91nqc73ereoog1005259586163290.jpg)

Figure 7. La propriété de croissance de la pente des cordes pour une fonction convexe \( f \) .

> Figure 7. The property of increasing chord slopes for a convex function \( f \) .

La proposition précédente entraîne aussi le résultat qui suit.

> The previous proposition also leads to the following result.

Proposition 2. Une fonction convexe \( f : I \rightarrow \mathbb{R} \) possède en tout point de \( I \) une dérivée à droite et une dérivée à gauche. Elle est donc continue sur \( I \) (pas forcément aux bornes de I). De plus, les applications \( {f}_{\mathrm{g}}^{\prime } \) et \( {f}_{\mathrm{d}}^{\prime } \) sont croissantes sur \( I \) et \( {f}_{\mathrm{g}}^{\prime }\left( x\right) \leq {f}_{\mathrm{d}}^{\prime }\left( x\right) \) pour tout \( x \in \overset{ \circ }{I} \) .

> Proposition 2. A convex function \( f : I \rightarrow \mathbb{R} \) has a right-hand derivative and a left-hand derivative at every point in \( I \) . It is therefore continuous on \( I \) (not necessarily at the endpoints of I). Furthermore, the mappings \( {f}_{\mathrm{g}}^{\prime } \) and \( {f}_{\mathrm{d}}^{\prime } \) are increasing on \( I \) and \( {f}_{\mathrm{g}}^{\prime }\left( x\right) \leq {f}_{\mathrm{d}}^{\prime }\left( x\right) \) for all \( x \in \overset{ \circ }{I} \) .

THÉORÉME 1. Soit \( f : I \rightarrow \mathbb{R} \) une application dérivable sur I. Les assertions suivantes sont équivalentes

> THEOREM 1. Let \( f : I \rightarrow \mathbb{R} \) be a differentiable mapping on I. The following assertions are equivalent

(i) \( f \) est convexe.

> (i) \( f \) is convex.

(ii) \( {f}^{\prime } \) est croissante.

> (ii) \( {f}^{\prime } \) is increasing.

(iii) La courbe représentative de \( f \) est au dessus de ses tangentes.

> (iii) The representative curve of \( f \) lies above its tangents.

COROLLAIRE 1. Une application \( f : I \rightarrow \mathbb{R} \) deux fois dérivable est convexe si et seulement si \( {f}^{\prime \prime }\left( x\right) \geq 0 \) pour tout \( x \in I \) .

> COROLLARY 1. A twice-differentiable mapping \( f : I \rightarrow \mathbb{R} \) is convex if and only if \( {f}^{\prime \prime }\left( x\right) \geq 0 \) for all \( x \in I \) .

Proposition 3. Soit une application \( f : I \rightarrow \mathbb{R} \) convexe. Alors

> Proposition 3. Let \( f : I \rightarrow \mathbb{R} \) be a convex mapping. Then

\[
\forall {x}_{1},\ldots ,{x}_{n} \in  I,\forall {\alpha }_{1},\ldots ,{\alpha }_{n} > 0,\;f\left( \frac{{\alpha }_{1}{x}_{1} + \cdots  + {\alpha }_{n}{x}_{n}}{{\alpha }_{1} + \cdots  + {\alpha }_{n}}\right)  \leq  \frac{{\alpha }_{1}f\left( {x}_{1}\right)  + \cdots  + {\alpha }_{n}f\left( {x}_{n}\right) }{{\alpha }_{1} + \cdots  + {\alpha }_{n}}.
\]

Inégalités classiques. THÉORÉME 1 (INÉGALITÉ ARITHMÉTICO-GÉOMÉTRIQUE). Soient \( {x}_{1},\ldots ,{x}_{n} \) des nombres réels positifs. On a

> Classical inequalities. THEOREM 1 (ARITHMETIC-GEOMETRIC MEAN INEQUALITY). Let \( {x}_{1},\ldots ,{x}_{n} \) be positive real numbers. We have

\[
{\left( {x}_{1}\cdots {x}_{n}\right) }^{1/n} \leq  \frac{{x}_{1} + \cdots  + {x}_{n}}{n}.
\]

Démonstration. Cela provient de la concavité de la fonction logarithme. Soit \( f : {\mathbb{R}}^{+ * } \rightarrow \mathbb{R}\;x \mapsto \; - \log x \) . Cette application est deux fois dérivable et \( {f}^{\prime \prime }\left( x\right) = 1/{x}^{2} > 0 \) pour tout \( x > 0 \) . C’est donc une fonction convexe, ce qui entraîne

> Proof. This follows from the concavity of the logarithm function. Let \( f : {\mathbb{R}}^{+ * } \rightarrow \mathbb{R}\;x \mapsto \; - \log x \) . This mapping is twice differentiable and \( {f}^{\prime \prime }\left( x\right) = 1/{x}^{2} > 0 \) for all \( x > 0 \) . It is therefore a concave function, which implies

\[
f\left( \frac{{x}_{1} + \cdots  + {x}_{n}}{n}\right)  \leq  \frac{f\left( {x}_{1}\right)  + \cdots  + f\left( {x}_{n}\right) }{n}
\]

d'après la proposition 3, c'est-à-dire

> according to proposition 3, that is to say

\[
\log \left( \frac{{x}_{1} + \cdots  + {x}_{n}}{n}\right)  \geq  \log \left\lbrack  {\left( {x}_{1}\cdots {x}_{n}\right) }^{1/n}\right\rbrack  ,
\]

et la fonction logarithme étant croissante, on en déduit le théorème.

> and since the logarithm function is increasing, we deduce the theorem.

THÉORÉME 2 (INÉGALITÉ DE HÖLDER). Soient deux nombres réels \( p, q > 0 \) tels que \( \frac{1}{p} + \frac{1}{q} = 1 \) . Pour tous nombres réels positifs \( {a}_{1},\ldots ,{a}_{n} \) et \( {b}_{1},\ldots ,{b}_{n} \) on a

> THEOREM 2 (HÖLDER'S INEQUALITY). Let two real numbers \( p, q > 0 \) be such that \( \frac{1}{p} + \frac{1}{q} = 1 \) . For all positive real numbers \( {a}_{1},\ldots ,{a}_{n} \) and \( {b}_{1},\ldots ,{b}_{n} \) we have

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{b}_{i} \leq  {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}^{p}\right) }^{1/p}{\left( \mathop{\sum }\limits_{{i = 1}}^{n}{b}_{i}^{q}\right) }^{1/q}.
\]

Démonstration. La concavité de la fonction logarithme entraîne

> Proof. The concavity of the logarithm function implies

\[
\forall x, y > 0,\;\frac{\log x}{p} + \frac{\log y}{q} \leq  \log \left( {\frac{x}{p} + \frac{y}{q}}\right) \;\text{ donc }\;{x}^{1/p}{y}^{1/q} \leq  \frac{x}{p} + \frac{y}{q},
\]

inégalité qui reste vraie lorsque \( x \) ou \( y \) est nul. En choisissant

> an inequality that remains true when \( x \) or \( y \) is zero. By choosing

\[
x = \frac{{a}_{i}^{p}}{\mathop{\sum }\limits_{j}{a}_{j}^{p}}\;\text{ et }\;y = \frac{{b}_{i}^{q}}{\mathop{\sum }\limits_{j}{b}_{j}^{q}},
\]

(on peut supposer qu’au moins l’un des \( {a}_{i} \) et l’un des \( {b}_{j} \) sont non nuls, sinon l’inégalité de Hölder est immédiate) on tire

> (we can assume that at least one of the \( {a}_{i} \) and one of the \( {b}_{j} \) are non-zero, otherwise Hölder's inequality is immediate) we obtain

\[
\frac{{a}_{i}}{{\left( \mathop{\sum }\limits_{j}{a}_{j}^{p}\right) }^{1/p}} \cdot  \frac{{b}_{i}}{{\left( \mathop{\sum }\limits_{j}{b}_{j}^{q}\right) }^{1/q}} \leq  \frac{{a}_{i}^{p}}{p\left( {\mathop{\sum }\limits_{j}{a}_{j}^{p}}\right) } + \frac{{b}_{i}^{q}}{q\left( {\mathop{\sum }\limits_{j}{b}_{j}^{q}}\right) },
\]

puis en sommant sur \( i \)

> then by summing over \( i \)

\[
\frac{\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{b}_{i}}{{\left( \mathop{\sum }\limits_{j}{a}_{j}^{p}\right) }^{1/p}{\left( \mathop{\sum }\limits_{j}{b}_{j}^{q}\right) }^{1/q}} \leq  \frac{1}{p} + \frac{1}{q} = 1,
\]

d'où l'inégalité désirée.

> whence the desired inequality.

Remarque 2. Lorsque \( p = q = 2 \) , on retrouve l’inégalité de Schwarz.

> Remark 2. When \( p = q = 2 \) , we recover the Cauchy-Schwarz inequality.

THÉORÉME 3 (INÉGALITÉ DE MINKOWSKY). Soient \( p \geq 1 \) un nombre réel et \( {x}_{1},\ldots ,{x}_{n} \) , \( {y}_{1},\ldots ,{y}_{n} \) des nombres réels positifs. Alors

> THEOREM 3 (MINKOWSKI'S INEQUALITY). Let \( p \geq 1 \) be a real number and \( {x}_{1},\ldots ,{x}_{n} \) , \( {y}_{1},\ldots ,{y}_{n} \) be positive real numbers. Then

\[
{\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{p}\right) }^{1/p} \leq  {\left( \mathop{\sum }\limits_{{i = i}}^{n}{x}_{i}^{p}\right) }^{1/p} + {\left( \mathop{\sum }\limits_{{i = i}}^{n}{y}_{i}^{p}\right) }^{1/p}.
\]

Démonstration. Si \( p = 1 \) , c’est évident. Sinon, on pose \( q = \frac{p}{p - 1} \) , de sorte que \( \frac{1}{p} + \frac{1}{q} = 1 \) . D’après l'inégalité de Hölder

> Proof. If \( p = 1 \) , it is obvious. Otherwise, we set \( q = \frac{p}{p - 1} \) , so that \( \frac{1}{p} + \frac{1}{q} = 1 \) . According to Hölder's inequality

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{\left( {x}_{i} + {y}_{i}\right) }^{p - 1} \leq  {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{p}\right) }^{1/p}{\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{q\left( {p - 1}\right) }\right) }^{1/q}
\]

et

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}{\left( {x}_{i} + {y}_{i}\right) }^{p - 1} \leq  {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}^{p}\right) }^{1/p}{\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{q\left( {p - 1}\right) }\right) }^{1/q},
\]

ce qui par sommation entraîne (sachant que \( q\left( {p - 1}\right) = p \) )

> which by summation leads to (knowing that \( q\left( {p - 1}\right) = p \) )

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{p} \leq  \left\lbrack  {{\left( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{p}\right) }^{1/p} + {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}^{p}\right) }^{1/p}}\right\rbrack  {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{p}\right) }^{1/q}
\]

donc

> therefore

\[
{\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} + {y}_{i}\right) }^{p}\right\rbrack  }^{1 - 1/q} \leq  {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{p}\right) }^{1/p} + {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}^{p}\right) }^{1/p},
\]

(on peut supposer que les \( {x}_{i} \) et \( {y}_{j} \) sont non tous nuls - sinon l’inégalité est évidente - ce qui autorise à simplifier) d’où le résultat car \( 1 - 1/q = 1/p \) .

> (we can assume that the \( {x}_{i} \) and \( {y}_{j} \) are not all zero - otherwise the inequality is obvious - which allows for simplification) hence the result because \( 1 - 1/q = 1/p \) .

Conséquence : Pour tout \( p \geq 1 \) , considérons la fonction de \( {\mathbb{R}}^{n} \) dans \( \mathbb{R} \) définie par

> Consequence: For any \( p \geq 1 \) , consider the function from \( {\mathbb{R}}^{n} \) to \( \mathbb{R} \) defined by

\[
N\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{p}\right) }^{1/p}.
\]

L'inégalité de Minkowsky entraîne que \( N \) vérifie l’inégalité triangulaire. On en déduit facilement que \( N \) est une norme sur \( {\mathbb{R}}^{n} \) . On la note souvent \( \parallel .{\parallel }_{p} \) . Remarquons aussi que

> Minkowski's inequality implies that \( N \) satisfies the triangle inequality. We easily deduce that \( N \) is a norm on \( {\mathbb{R}}^{n} \) . It is often denoted by \( \parallel .{\parallel }_{p} \) . Let us also note that

\[
\mathop{\sup }\limits_{i}\left| {x}_{i}\right|  = {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\lim }\limits_{{p \rightarrow  \infty }}{\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{p}.
\]
