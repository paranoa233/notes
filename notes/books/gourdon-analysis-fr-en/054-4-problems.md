### 4. Problems

*Français : 4. Problèmes*

Problem 1. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une application continue en 0 vérifiant

> Problem 1. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a mapping continuous at 0 satisfying

\[
\exists k \in  \rbrack 0,1\lbrack ,\;\ell  = \mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x > 0} }}\frac{f\left( x\right)  - f\left( {kx}\right) }{x}\;\text{ existe. }
\]

Montrer que \( f \) est dérivable en 0 et exprimer \( {f}^{\prime }\left( 0\right) \) en fonction de \( \ell \) et de \( k \) .

> Show that \( f \) is differentiable at 0 and express \( {f}^{\prime }\left( 0\right) \) in terms of \( \ell \) and \( k \) .

Solution. Soit \( \varepsilon > 0 \) . D’après les hypothèses,

> Solution. Let \( \varepsilon > 0 \) . According to the hypotheses,

\[
\exists \eta  > 0,\forall t \in  \rbrack 0,\eta \rbrack ,\;\left| {\frac{f\left( {kt}\right)  - f\left( t\right) }{t} - \ell }\right|  < \varepsilon .
\]

Ainsi, si \( x \in \rbrack 0,\eta \rbrack \) , on a

> Thus, if \( x \in \rbrack 0,\eta \rbrack \) , we have

\[
\forall n \in  \mathbb{N},\;\left| {\frac{f\left( {{k}^{n}x}\right)  - f\left( {k\left( {{k}^{n}x}\right) }\right) }{{k}^{n}x} - \ell }\right|  \leq  \varepsilon \;\text{ ou encore }\;\left| {\frac{f\left( {{k}^{n}x}\right)  - f\left( {{k}^{n + 1}x}\right) }{x} - {k}^{n}\ell }\right|  \leq  {k}^{n}\varepsilon
\]

donc

> therefore

\[
\forall n \in  \mathbb{N},\;\left| {\frac{f\left( x\right)  - f\left( {{k}^{n}x}\right) }{x} - \left( {\mathop{\sum }\limits_{{i = 0}}^{{n - 1}}{k}^{i}}\right) \ell }\right|  \leq  \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left| {\frac{f\left( {{k}^{i}x}\right)  - f\left( {{k}^{i + 1}x}\right) }{x} - {k}^{i}\ell }\right|  \leq  \varepsilon \left( {\mathop{\sum }\limits_{{i = 0}}^{{n - 1}}{k}^{i}}\right) ,
\]

ce qui en faisant tendre \( n \) vers \( + \infty \) entraîne, en vertu de la continuité de \( f \) en 0

> which, by letting \( n \) tend to \( + \infty \) , implies, by virtue of the continuity of \( f \) at 0

\[
\left| {\frac{f\left( x\right)  - f\left( 0\right) }{x} - \frac{\ell }{1 - k}}\right|  \leq  \frac{\varepsilon }{1 - k}.
\]

Ceci étant vrai pour tout \( x \in \rbrack 0,\eta \rbrack \) , on en déduit la dérivabilité de \( f \) en 0 et \( {f}^{\prime }\left( 0\right) = \frac{\ell }{1 - k} \) .

> Since this is true for all \( x \in \rbrack 0,\eta \rbrack \) , we deduce the differentiability of \( f \) at 0 and \( {f}^{\prime }\left( 0\right) = \frac{\ell }{1 - k} \) .

Problem 2. Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une application dérivable telle que \( f\left( 0\right) = {f}^{\prime }\left( 0\right) = 0 \) et \( {f}^{\prime }\left( 1\right) = 0 \) . Montrer

> Problem 2. Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a differentiable mapping such that \( f\left( 0\right) = {f}^{\prime }\left( 0\right) = 0 \) and \( {f}^{\prime }\left( 1\right) = 0 \) . Show

\[
\exists c \in  \rbrack 0,1\rbrack ,\;{f}^{\prime }\left( c\right)  = \frac{f\left( c\right) }{c}.
\]

Solution. Commençons par donner l’idée de la preuve. L’égalité \( {f}^{\prime }\left( c\right) = f\left( c\right) /c \) exprime le

> Solution. Let us begin by giving the idea of the proof. The equality \( {f}^{\prime }\left( c\right) = f\left( c\right) /c \) expresses the

![bo_d7fjkrs91nqc73ereoog_108_467_1253_543_388_0.jpg](images/gourdon_analysis_fr_en_005_bod7fjkrs91nqc73ereoog10846712535433880.jpg)

Figure 8. à l’abscisse \( c \) , la tangente du graphe de \( f \) passe par l’origine.

> Figure 8. at the abscissa \( c \) , the tangent to the graph of \( f \) passes through the origin.

fait que la droite passant par l’origine et le point \( \left( {c, f\left( c\right) }\right) \) est tangente au graphe de \( f \) (voir la figure ci-contre). En regardant la figure, on s'aperçoit d'ailleurs que le point correspondant est un extremum relatif de la fonction "pente" \( x \mapsto f\left( x\right) /x \) .

> fact that the line passing through the origin and the point \( \left( {c, f\left( c\right) }\right) \) is tangent to the graph of \( f \) (see the figure opposite). By looking at the figure, we also notice that the corresponding point is a relative extremum of the "slope" function \( x \mapsto f\left( x\right) /x \) .

Cette remarque nous invite à considérer l'application

> This remark invites us to consider the mapping

\[
g : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \frac{f\left( x\right) }{x}\text{ si }x \neq  0,\;g\left( 0\right)  = {f}^{\prime }\left( 0\right)  = 0,
\]

qui est continue sur \( \left\lbrack {0,1}\right\rbrack \) et dérivable sur \( \rbrack 0,1\rbrack \) , avec

> which is continuous on \( \left\lbrack {0,1}\right\rbrack \) and differentiable on \( \rbrack 0,1\rbrack \) , with

\[
\forall x \in  \rbrack 0,1\rbrack ,\;{g}^{\prime }\left( x\right)  = \frac{x{f}^{\prime }\left( x\right)  - f\left( x\right) }{{x}^{2}}.
\]

(*)

> Si \( f\left( 1\right) = 0 \) le résultat est évident en prenant \( c = 1 \) . Sinon, nous allons prouver que \( g \) admet un extremum en point intérieur à \( \left\lbrack {0,1}\right\rbrack \) . Quitte à considérer \( - g \) , on peut supposer \( g\left( 1\right) > 0 \) . Soit \( c \in \left\lbrack {0,1}\right\rbrack \) tel que \( g\left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}g\left( x\right) \) (un tel point \( c \) existe car \( g \) est continue sur le compact \( \left\lbrack {0,1}\right\rbrack ) \) . On a \( c \neq 1 \) sinon on aurait \( {g}^{\prime }\left( 1\right) = \mathop{\lim }\limits_{{x \rightarrow 1}}\frac{g\left( 1\right) - g\left( x\right) }{1 - x} \geq 0 \) , ce qui est absurde vu que \( {g}^{\prime }\left( 1\right) = - f\left( 1\right) < 0 \) . On a aussi \( c \neq 0 \) car \( g\left( c\right) \geq g\left( 1\right) > 0 = g\left( 0\right) \) . Ainsi, \( c \) est un point intérieur à \( \left\lbrack {0,1}\right\rbrack \) où \( g \) atteint son maximum, donc \( {g}^{\prime }\left( c\right) = 0 \) , ce qui donne \( {f}^{\prime }\left( c\right) = f\left( c\right) /c \) grâce à l’expression (*).

If \( f\left( 1\right) = 0 \) the result is obvious by taking \( c = 1 \) . Otherwise, we will prove that \( g \) admits an extremum at an interior point of \( \left\lbrack {0,1}\right\rbrack \) . By considering \( - g \) , we can assume \( g\left( 1\right) > 0 \) . Let \( c \in \left\lbrack {0,1}\right\rbrack \) be such that \( g\left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}g\left( x\right) \) (such a point \( c \) exists because \( g \) is continuous on the compact set \( \left\lbrack {0,1}\right\rbrack ) \) ). We have \( c \neq 1 \) otherwise we would have \( {g}^{\prime }\left( 1\right) = \mathop{\lim }\limits_{{x \rightarrow 1}}\frac{g\left( 1\right) - g\left( x\right) }{1 - x} \geq 0 \) , which is absurd given that \( {g}^{\prime }\left( 1\right) = - f\left( 1\right) < 0 \) . We also have \( c \neq 0 \) because \( g\left( c\right) \geq g\left( 1\right) > 0 = g\left( 0\right) \) . Thus, \( c \) is an interior point of \( \left\lbrack {0,1}\right\rbrack \) where \( g \) reaches its maximum, so \( {g}^{\prime }\left( c\right) = 0 \) , which gives \( {f}^{\prime }\left( c\right) = f\left( c\right) /c \) thanks to expression (*).

> Problem 2 (e N’EST PAS ALGÉBRIQUE D’ORDRE 2). Montrer que \( e \) n’est pas algébrique d’ordre 2, c’est-à-dire qu’on ne peut pas trouver trois entiers \( a, b, c \) non tous nuls tels que \( a{e}^{2} + {be} + c = 0 \) . (Indication : raisonnez par l’absurde en considérant le développement de Taylor de la fonction \( f\left( x\right) = a{e}^{x} + c{e}^{-x} \) ).

Problem 2 (e IS NOT ALGEBRAIC OF ORDER 2). Show that \( e \) is not algebraic of order 2, that is to say, one cannot find three integers \( a, b, c \) not all zero such that \( a{e}^{2} + {be} + c = 0 \) . (Hint: reason by contradiction by considering the Taylor expansion of the function \( f\left( x\right) = a{e}^{x} + c{e}^{-x} \) ).

> Solution. La preuve est en quelque sorte une généralisation de la démonstration de l'irrationalité de \( e \) à partir de son expression en terme d’une série. Supposons \( a{e}^{2} + {be} + c = 0 \) , où \( a, b, c \) sont trois entiers non tous nuls. En désignant par \( f \) la fonction \( f : x \mapsto a{e}^{x} + c{e}^{-x} \) , ceci entraîne que \( f\left( 1\right) \) est entier. Nous allons prouver que cette dernière assertion est absurde.

Solution. The proof is in a way a generalization of the proof of the irrationality of \( e \) based on its expression in terms of a series. Suppose \( a{e}^{2} + {be} + c = 0 \) , where \( a, b, c \) are three integers not all zero. By denoting by \( f \) the function \( f : x \mapsto a{e}^{x} + c{e}^{-x} \) , this implies that \( f\left( 1\right) \) is an integer. We will prove that this last assertion is absurd.

> L'égalité de Taylor-Lagrange appliquée à \( f \) entraîne

The Taylor-Lagrange equality applied to \( f \) implies

\[
\left. {\forall n \in  {\mathbb{N}}^{ * },\exists {\theta }_{n} \in  }\right\rbrack  0,1\lbrack ,\;f\left( 1\right)  = f\left( 0\right)  + \frac{{f}^{\prime }\left( 0\right) }{1!} + \cdots  + \frac{{f}^{\left( n - 1\right) }\left( 0\right) }{\left( {n - 1}\right) !} + \frac{{f}^{\left( n\right) }\left( {\theta }_{n}\right) }{n!}.
\]

Or pour tout entier naturel \( k,{f}^{\left( k\right) }\left( x\right) = a{e}^{x} + {\left( -1\right) }^{k}c{e}^{-x} \) , en particulier \( {f}^{\left( k\right) }\left( 0\right) = a + {\left( -1\right) }^{k}c \) est entier. On en déduit

> However, for any natural integer \( k,{f}^{\left( k\right) }\left( x\right) = a{e}^{x} + {\left( -1\right) }^{k}c{e}^{-x} \) , in particular \( {f}^{\left( k\right) }\left( 0\right) = a + {\left( -1\right) }^{k}c \) is an integer. We deduce from this

\[
\forall n \in  {\mathbb{N}}^{ * },\;\frac{{f}^{\left( n\right) }\left( {\theta }_{n}\right) }{n} = \left( {n - 1}\right) !f\left( 1\right)  - \left( {n - 1}\right) !f\left( 0\right)  - \frac{\left( {n - 1}\right) !}{1!}{f}^{\prime }\left( 0\right)  - \cdots  - \frac{\left( {n - 1}\right) !}{\left( {n - 1}\right) !}{f}^{\left( n - 1\right) }\left( 0\right)  \in  \mathbb{Z}.
\]

(*)

> La majoration \( \left| {{f}^{\left( n\right) }\left( {\theta }_{n}\right) }\right| = \left| {a{e}^{{\theta }_{n}} + {\left( -1\right) }^{n}c{e}^{-{\theta }_{n}}}\right| \leq \left| a\right| e + \left| c\right| \) montre que \( {f}^{\left( n\right) }\left( {\theta }_{n}\right) \) est bornée, donc \( {f}^{\left( n\right) }\left( {\theta }_{n}\right) /n \) tend vers 0 lorsque \( n \) tend vers + ∞. D’après (*), ce terme est toujours entier, il est donc nul à partir d'un certain rang, c'est-à-dire

The upper bound \( \left| {{f}^{\left( n\right) }\left( {\theta }_{n}\right) }\right| = \left| {a{e}^{{\theta }_{n}} + {\left( -1\right) }^{n}c{e}^{-{\theta }_{n}}}\right| \leq \left| a\right| e + \left| c\right| \) shows that \( {f}^{\left( n\right) }\left( {\theta }_{n}\right) \) is bounded, so \( {f}^{\left( n\right) }\left( {\theta }_{n}\right) /n \) tends to 0 as \( n \) tends to + ∞. According to (*), this term is always an integer, so it is zero from a certain rank onwards, that is to say

\[
\exists N \in  {\mathbb{N}}^{ * },\forall n \geq  N,\;{f}^{\left( n\right) }\left( {\theta }_{n}\right)  = a{e}^{{\theta }_{n}} + {\left( -1\right) }^{n}c{e}^{-{\theta }_{n}} = 0.
\]

On en conclut que pour tout \( n \geq N \) , \( a \) et \( {\left( -1\right) }^{n}c \) sont de signe opposés, ce qui n’est possible que si \( a = c = 0 \) , et donc \( b = 0 \) . Ceci est en contradiction avec les hypothèses de l’énoncé, d’où le résultat.

> We conclude that for all \( n \geq N \), \( a \) and \( {\left( -1\right) }^{n}c \) have opposite signs, which is only possible if \( a = c = 0 \), and therefore \( b = 0 \). This contradicts the hypotheses of the statement, hence the result.

Remarque. On en déduit en particulier que \( e \) est irrationnel. En fait, \( e \) est même un nombre transcendant (voir le tome Algèbre).

> Remark. We deduce in particular that \( e \) is irrational. In fact, \( e \) is even a transcendental number (see the Algebra volume).

Problem 4 (ZÉROS D'UN POLYNÖME LACUNAIRE). Soit \( P = {X}^{n} + {a}_{n - 1}{X}^{n - 1} + \cdots + \; {a}_{1}X + {a}_{0} \) un polynôme à coefficients réels.

> Problem 4 (ZEROS OF A LACUNARY POLYNOMIAL). Let \( P = {X}^{n} + {a}_{n - 1}{X}^{n - 1} + \cdots + \; {a}_{1}X + {a}_{0} \) be a polynomial with real coefficients.

a) On suppose qu’il existe \( p \in {\mathbb{N}}^{ * }, p < n \) , tel que \( {a}_{n - 1} = \ldots = {a}_{n - p} = 0 \) et \( {a}_{n - p - 1} \neq 0 \) (on dit que \( P \) présente une lacune de longueur \( p \) ). Si \( p \) est pair, montrer que, comptées avec leur ordre de multiplicité, \( P \) admet au plus \( n - p \) racines réelles ; si \( p \) est impair et \( {a}_{n - p - 1} > 0 \) , montrer que \( P \) admet au plus \( n - p - 1 \) racines réelles; si \( p \) est impair et \( {a}_{n - p - 1} < 0 \) , montrer que \( P \) admet au plus \( n - p + 1 \) racines réelles.

> a) Suppose there exists \( p \in {\mathbb{N}}^{ * }, p < n \), such that \( {a}_{n - 1} = \ldots = {a}_{n - p} = 0 \) and \( {a}_{n - p - 1} \neq 0 \) (we say that \( P \) has a gap of length \( p \)). If \( p \) is even, show that, counted with their multiplicity, \( P \) has at most \( n - p \) real roots; if \( p \) is odd and \( {a}_{n - p - 1} > 0 \), show that \( P \) has at most \( n - p - 1 \) real roots; if \( p \) is odd and \( {a}_{n - p - 1} < 0 \), show that \( P \) has at most \( n - p + 1 \) real roots.

b) Étudier le cas plus général où \( p \) coefficients consécutifs \( {a}_{i} \) de \( P \) sont nuls, c’est-à-dire \( {a}_{m} = {a}_{m + 1} = \ldots = {a}_{m + p - 1} = 0 \) et \( {a}_{m - 1} \neq 0,{a}_{m + p} \neq 0. \)

> b) Study the more general case where \( p \) consecutive coefficients \( {a}_{i} \) of \( P \) are zero, that is to say \( {a}_{m} = {a}_{m + 1} = \ldots = {a}_{m + p - 1} = 0 \) and \( {a}_{m - 1} \neq 0,{a}_{m + p} \neq 0. \)

Solution. a) Tout repose sur le principe suivant : si un polynôme \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) a \( r \) racines réelles (comptées avec leur ordre de multiplicité), alors son polynôme dérivé \( {Q}^{\prime } \) a au moins \( r - 1 \) racines réelles. En effet, si \( {u}_{1} < \cdots < {u}_{k} \) sont les racines réelles d’un polynôme \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) d’ordre de multiplicité respectifs \( {\alpha }_{1},\ldots ,{\alpha }_{k} \) , alors pour tout \( i \in \{ 1\ldots , k - 1\} ,{Q}^{\prime } \) a au moins une racine réelle \( {v}_{i} \) dans l’intervalle \( \rbrack {u}_{i},{u}_{i + 1}\left\lbrack \right. \) d’après le théorème de Rolle. De plus, si \( {\alpha }_{i} \geq 2 \) , alors \( {u}_{i} \) est une racine de \( {Q}^{\prime } \) d’ordre de multiplicité \( {\alpha }_{i} - 1 \) . Finalement, nous avons exhibé \( \left( {k - 1}\right) + \mathop{\sum }\limits_{i}\left( {{\alpha }_{i} - 1}\right) = \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right) - 1 \) racines de \( {Q}^{\prime } \) , ce qui prouve notre remarque.

> Solution. a) Everything relies on the following principle: if a polynomial \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) has \( r \) real roots (counted with their multiplicity), then its derivative polynomial \( {Q}^{\prime } \) has at least \( r - 1 \) real roots. Indeed, if \( {u}_{1} < \cdots < {u}_{k} \) are the real roots of a polynomial \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) with respective multiplicities \( {\alpha }_{1},\ldots ,{\alpha }_{k} \), then for every \( i \in \{ 1\ldots , k - 1\} ,{Q}^{\prime } \) there is at least one real root \( {v}_{i} \) in the interval \( \rbrack {u}_{i},{u}_{i + 1}\left\lbrack \right. \) according to Rolle's theorem. Furthermore, if \( {\alpha }_{i} \geq 2 \), then \( {u}_{i} \) is a root of \( {Q}^{\prime } \) with multiplicity \( {\alpha }_{i} - 1 \). Finally, we have exhibited \( \left( {k - 1}\right) + \mathop{\sum }\limits_{i}\left( {{\alpha }_{i} - 1}\right) = \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right) - 1 \) roots of \( {Q}^{\prime } \), which proves our remark.

Maintenant, notons \( r \) le nombre de racines réelles de \( P \) (comptées avec leur ordre de multi-plicité). Nous venons de voir que \( {P}^{\prime } \) a au moins \( r - 1 \) racines réelles, et en itérant le procédé, on s’aperçoit que \( {P}^{\left( n - p - 1\right) } \) a au moins \( r - \left( {n - p - 1}\right) = r - n + p + 1 \) racines réelles. Comme \( {a}_{n - 1} = \ldots = {a}_{n - p} = 0 \) , on a

> Now, let \( r \) be the number of real roots of \( P \) (counted with their multiplicity). We have just seen that \( {P}^{\prime } \) has at least \( r - 1 \) real roots, and by iterating the process, we notice that \( {P}^{\left( n - p - 1\right) } \) has at least \( r - \left( {n - p - 1}\right) = r - n + p + 1 \) real roots. Since \( {a}_{n - 1} = \ldots = {a}_{n - p} = 0 \), we have

\[
{P}^{\left( n - p - 1\right) } = n\left( {n - 1}\right) \ldots \left( {p + 2}\right) {X}^{p + 1} + \left( {n - p - 1}\right) !{a}_{n - p - 1}.
\]

(*)

> Si \( p \) est pair, la forme de ce dernier polynôme montre qu’il a exactement une racine réelle, et comme nous avons montré qu’il en a au moins \( r - n + p + 1 \) , on a \( r - n + p + 1 \leq 1 \) , cl’est- à-dire \( r \leq n - p \) . Si \( p \) est impair et \( {a}_{p + 1} > 0 \) , le polynôme (*) n’a aucune racine réelle, donc \( r - n + p + 1 \leq 0 \) , c’est-à-dire \( r \leq n - p - 1 \) . Si \( p \) est impair et \( {a}_{p + 1} < 0 \) ,(*) a exactement deux racines réelles donc \( r - n + p + 1 \leq 2 \) , c’est-à-dire \( r \leq n - p + 1 \) .

If \( p \) is even, the form of this last polynomial shows that it has exactly one real root, and since we have shown that it has at least \( r - n + p + 1 \) of them, we have \( r - n + p + 1 \leq 1 \), that is to say \( r \leq n - p \). If \( p \) is odd and \( {a}_{p + 1} > 0 \), the polynomial (*) has no real roots, so \( r - n + p + 1 \leq 0 \), that is to say \( r \leq n - p - 1 \). If \( p \) is odd and \( {a}_{p + 1} < 0 \), (*) has exactly two real roots, so \( r - n + p + 1 \leq 2 \), that is to say \( r \leq n - p + 1 \).

> b) Remarquons tout d’abord que pour tout polynôme \( Q \) de degré \( d \) , dont le terme constant est non nul, le polynôme \( {Q}^{ * } = {X}^{d}Q\left( {1/X}\right) \) (appelé polynôme réciproque de \( Q \) ) a le même nombre de racines réelles que \( Q : \) en effet, si \( Q = \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {u}_{i}\right) }^{{\alpha }_{i}} \) est la factorisation de \( Q \) dans \( \mathbb{C}\left\lbrack X\right\rbrack \) , on a \( {Q}^{ * } = \mathop{\prod }\limits_{{i = 1}}^{k}{\left( 1 - {u}_{i}X\right) }^{{\alpha }_{i}} \) (les racines de \( {Q}^{ * } \) sont les inverses des racines de \( Q \) , avec le même ordre de multiplicité).

b) First, let us note that for any polynomial \( Q \) of degree \( d \) whose constant term is non-zero, the polynomial \( {Q}^{ * } = {X}^{d}Q\left( {1/X}\right) \) (called the reciprocal polynomial of \( Q \)) has the same number of real roots as \( Q : \); indeed, if \( Q = \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {u}_{i}\right) }^{{\alpha }_{i}} \) is the factorization of \( Q \) in \( \mathbb{C}\left\lbrack X\right\rbrack \), we have \( {Q}^{ * } = \mathop{\prod }\limits_{{i = 1}}^{k}{\left( 1 - {u}_{i}X\right) }^{{\alpha }_{i}} \) (the roots of \( {Q}^{ * } \) are the inverses of the roots of \( Q \), with the same multiplicity).

> Ceci étant, notons \( Q = {P}^{\left( m - 1\right) } \) . On a

Given this, let us denote \( Q = {P}^{\left( m - 1\right) } \). We have

\[
Q = n\left( {n - 1}\right) \ldots \left( {n - m - 2}\right) {X}^{n - m + 1} + \cdots  + \left( {m + p}\right) \cdots \left( {p + 2}\right) {a}_{m + p}{X}^{p + 1} + \left( {m - 1}\right) !{a}_{m - 1},
\]

le polynôme réciproque de \( Q \) est

> the reciprocal polynomial of \( Q \) is

\[
{Q}^{ * } = \left( {m - 1}\right) !{a}_{m - 1}{X}^{n - m + 1} + \left( {m + p}\right) \cdots \left( {p + 2}\right) {a}_{m + p}{X}^{n - m - p} + \cdots  + n\left( {n - 1}\right) \cdots \left( {n - m - 2}\right) .
\]

D’après la question précédente, \( {Q}^{ * } \) a au plus \( \left( {n - m + 1}\right) - p \) racines réelles si \( p \) est pair, au plus \( \left( {n - m + 1}\right) - p - 1 \) si \( p \) est impair et \( {a}_{m + p}{a}_{m - 1} > 0 \) , au plus \( \left( {n - m + 1}\right) - p + 1 \) si \( p \) est impair et \( {a}_{m + p}{a}_{m - 1} < 0 \) . Le nombre de racines réelles de \( Q \) est égal au nombre de racines réelles de \( {Q}^{ * } \) , donc ceci vaut pour \( {P}^{\left( m - 1\right) } \) . On en déduit, d’après le principe général énoncé plus haut, que \( P \) a au plus \( m - 1 + \left\lbrack {\left( {n - m + 1}\right) - p}\right\rbrack = n - p \) racines réelles si \( p \) est pair, au plus \( m - 1 + \left\lbrack {\left( {n - m + 1}\right) - p}\right\rbrack - 1 = n - p - 1 \) si \( p \) est impair et \( {a}_{m + p}{a}_{m - 1} > 0 \) , au plus \( n - p + 1 \) si \( p \) est impair et \( {a}_{m + p}{a}_{m - 1} < 0 \) .

> According to the previous question, \( {Q}^{ * } \) has at most \( \left( {n - m + 1}\right) - p \) real roots if \( p \) is even, at most \( \left( {n - m + 1}\right) - p - 1 \) if \( p \) is odd and \( {a}_{m + p}{a}_{m - 1} > 0 \), and at most \( \left( {n - m + 1}\right) - p + 1 \) if \( p \) is odd and \( {a}_{m + p}{a}_{m - 1} < 0 \). The number of real roots of \( Q \) is equal to the number of real roots of \( {Q}^{ * } \), so this holds for \( {P}^{\left( m - 1\right) } \). We deduce, according to the general principle stated above, that \( P \) has at most \( m - 1 + \left\lbrack {\left( {n - m + 1}\right) - p}\right\rbrack = n - p \) real roots if \( p \) is even, at most \( m - 1 + \left\lbrack {\left( {n - m + 1}\right) - p}\right\rbrack - 1 = n - p - 1 \) if \( p \) is odd and \( {a}_{m + p}{a}_{m - 1} > 0 \), and at most \( n - p + 1 \) if \( p \) is odd and \( {a}_{m + p}{a}_{m - 1} < 0 \).

Problem 5. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{\infty } \) telle que

> Problem 5. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{\infty } \) class mapping such that

\[
f\left( 0\right)  = 0\;\text{ et }\;\mathop{\lim }\limits_{{x \rightarrow   + \infty }}f\left( x\right)  = 0.
\]

Démontrer l’existence d’une suite \( \left( {x}_{n}\right) \) strictement croissante à valeurs positives telle que \( {f}^{\left( n\right) }\left( {x}_{n}\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> Prove the existence of a strictly increasing sequence \( \left( {x}_{n}\right) \) with positive values such that \( {f}^{\left( n\right) }\left( {x}_{n}\right) = 0 \) for all \( n \in {\mathbb{N}}^{ * } \).

Solution. Nous allons construire cette suite par récurrence. Commençons par \( n = 1 \) . La fonction \( f \) étant nulle à l’origine et tendant vers 0 en \( + \infty \) , elle n’est pas strictement monotone. Ainsi, la fonction dérivée \( {f}^{\prime } \) prend des valeurs positives et négatives, ce qui entraîne qu’elle s’annule en au moins un point \( {x}_{1} \in {\mathbb{R}}^{ + } \) d’après le théorème des valeurs intermédiaires et en vertu de la continuité de \( {f}^{\prime } \) . Ainsi, nous avons construit \( {x}_{1} \geq 0 \) tel que \( {f}^{\prime }\left( {x}_{1}\right) = 0 \) .

> Solution. We will construct this sequence by induction. Let us start with \( n = 1 \). Since the function \( f \) is zero at the origin and tends to 0 at \( + \infty \), it is not strictly monotonic. Thus, the derivative function \( {f}^{\prime } \) takes both positive and negative values, which implies that it vanishes at at least one point \( {x}_{1} \in {\mathbb{R}}^{ + } \) according to the intermediate value theorem and by virtue of the continuity of \( {f}^{\prime } \). Thus, we have constructed \( {x}_{1} \geq 0 \) such that \( {f}^{\prime }\left( {x}_{1}\right) = 0 \).

Pour passer du rang \( n \geq 1 \) au rang \( n + 1 \) , on généralise la technique utilisée pour \( n = 1 \) . Supposons \( {x}_{n} \) construit et montrons l’existence de \( {x}_{n + 1} > {x}_{n} \) tel que \( {f}^{\left( n + 1\right) }\left( {x}_{n + 1}\right) = 0 \) . Pour cela, raisonnons par l’absurde en supposant \( {f}^{\left( n + 1\right) }\left( x\right) \neq 0 \) pour tout \( x > {x}_{n} \) . La continuité de \( {f}^{\left( n + 1\right) } \) entraîne que \( {f}^{\left( n + 1\right) } \) garde un signe constant sur \( \rbrack {x}_{n}, + \infty \lbrack \) , par exemple strictement positif (quitte à changer \( f \) en \( - f \) ). Ainsi, \( {f}^{\left( n\right) } \) est une fonction strictement croissante sur \( \left\lbrack {{x}_{n}, + \infty }\right\rbrack \) . Fixons un réel \( a > {x}_{n} \) . D’après l’égalité de Taylor-Lagrange,

> To move from rank \( n \geq 1 \) to rank \( n + 1 \), we generalize the technique used for \( n = 1 \). Suppose \( {x}_{n} \) is constructed and let us show the existence of \( {x}_{n + 1} > {x}_{n} \) such that \( {f}^{\left( n + 1\right) }\left( {x}_{n + 1}\right) = 0 \). To do this, let us reason by contradiction by assuming \( {f}^{\left( n + 1\right) }\left( x\right) \neq 0 \) for all \( x > {x}_{n} \). The continuity of \( {f}^{\left( n + 1\right) } \) implies that \( {f}^{\left( n + 1\right) } \) maintains a constant sign on \( \rbrack {x}_{n}, + \infty \lbrack \), for example strictly positive (by changing \( f \) to \( - f \) if necessary). Thus, \( {f}^{\left( n\right) } \) is a strictly increasing function on \( \left\lbrack {{x}_{n}, + \infty }\right\rbrack \). Let us fix a real number \( a > {x}_{n} \). According to the Taylor-Lagrange equality,

\[
\forall x \geq  a,\exists y \in  \left\lbrack  {a, x}\right\rbrack  ,\;f\left( x\right)  = f\left( a\right)  + \left( {x - a}\right) {f}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( x - a\right) }^{n - 1}}{\left( {n - 1}\right) !}{f}^{\left( n - 1\right) }\left( a\right)  + \frac{{\left( x - a\right) }^{n}}{n!}{f}^{\left( n\right) }\left( y\right) ,
\]

ce qui entraîne, en vertu du caractère croissant de \( {f}^{\left( n\right) } \) sur \( \left\lbrack {{x}_{n}, + \infty \lbrack }\right. \) et du fait que \( \alpha = {f}^{\left( n\right) }\left( a\right) > \; {f}^{\left( n\right) }\left( {x}_{n}\right) = 0 \)

> which implies, by virtue of the increasing nature of \( {f}^{\left( n\right) } \) on \( \left\lbrack {{x}_{n}, + \infty \lbrack }\right. \) and the fact that \( \alpha = {f}^{\left( n\right) }\left( a\right) > \; {f}^{\left( n\right) }\left( {x}_{n}\right) = 0 \)

\[
\forall x \geq  a,\;f\left( x\right)  \geq  f\left( a\right)  + \left( {x - a}\right) {f}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( x - a\right) }^{n - 1}}{\left( {n - 1}\right) !}{f}^{\left( n - 1\right) }\left( a\right)  + \alpha \frac{{\left( x - a\right) }^{n}}{n!}.
\]

Le terme de droite de cette dernière expression diverge vers \( + \infty \) lorsque \( x \rightarrow + \infty \) , il en est donc de même pour \( f\left( x\right) \) , ce qui est contraire aux hypothèses. Ainsi, il existe bien un réel \( {x}_{n + 1} > {x}_{n} \) tel que \( {f}^{\left( n + 1\right) }\left( {x}_{n + 1}\right) = 0 \) et le résultat est prouvé.

> The term on the right of this last expression diverges to \( + \infty \) as \( x \rightarrow + \infty \), so the same is true for \( f\left( x\right) \), which contradicts the hypotheses. Thus, there indeed exists a real number \( {x}_{n + 1} > {x}_{n} \) such that \( {f}^{\left( n + 1\right) }\left( {x}_{n + 1}\right) = 0 \) and the result is proven.

Problem 6. Soit une application continue \( g : \mathbb{R} \rightarrow \mathbb{R} \) telle que

> Problem 6. Let \( g : \mathbb{R} \rightarrow \mathbb{R} \) be a continuous mapping such that

\[
\forall x \in  \mathbb{R},\;{g}^{2}\left( x\right)  = g \circ  g\left( x\right)  = {2g}\left( x\right)  - x.
\]

a) Montrer que \( g \) est une bijection croissante de \( \mathbb{R} \) sur \( \mathbb{R} \) .

> a) Show that \( g \) is an increasing bijection from \( \mathbb{R} \) onto \( \mathbb{R} \).

b) Déterminer la forme de \( g \) . (Indication : on pourra exprimer \( {g}^{n} = g \circ g \circ \cdots \) en fonction de \( g \) pour tout entier naturel \( n \) ).

> b) Determine the form of \( g \). (Hint: one may express \( {g}^{n} = g \circ g \circ \cdots \) as a function of \( g \) for any natural number \( n \)).

Solution. a) L'injectivité de \( g \) est immédiate puisque

> Solution. a) The injectivity of \( g \) is immediate since

\[
g\left( x\right)  = g\left( y\right)  \Rightarrow  {g}^{2}\left( x\right)  = {g}^{2}\left( y\right)  \Rightarrow  x = {2g}\left( x\right)  - {g}^{2}\left( x\right)  = {2g}\left( y\right)  - {g}^{2}\left( y\right)  = y.
\]

Montrons la surjectivité de \( g \) . Une application injective et continue sur \( \mathbb{R} \) est strictement monotone, donc \( g \) est strictement monotone (c'est classique par le théorème des valeurs in-termédiaires). L'application \( g \circ g \) est strictement croissante (composée de deux fonctions de même monotonie) donc \( g = \left( {{g}^{2}\left( x\right) + x}\right) /2 \) est strictement croissante. Le caractère croissant de \( {g}^{2} \) entraîne d’ailleurs

> Let us show the surjectivity of \( g \) . An injective and continuous mapping on \( \mathbb{R} \) is strictly monotonic, so \( g \) is strictly monotonic (this is a classic result from the intermediate value theorem). The mapping \( g \circ g \) is strictly increasing (a composition of two functions with the same monotonicity), so \( g = \left( {{g}^{2}\left( x\right) + x}\right) /2 \) is strictly increasing. The increasing nature of \( {g}^{2} \) also implies

\[
\forall x \geq  0,\;g\left( x\right)  = \frac{{g}^{2}\left( x\right)  + x}{2} \geq  \frac{{g}^{2}\left( 0\right)  + x}{2}\;\text{ donc }\;\mathop{\lim }\limits_{{x \rightarrow   + \infty }}g\left( x\right)  =  + \infty .
\]

On montrerait de même que \( \mathop{\lim }\limits_{{x \rightarrow - \infty }}g\left( x\right) = - \infty \) . Tout ceci permet de conclure que \( g \) est une bijection de \( \mathbb{R} \) sur \( \mathbb{R} \) .

> We would show in the same way that \( \mathop{\lim }\limits_{{x \rightarrow - \infty }}g\left( x\right) = - \infty \) . All this allows us to conclude that \( g \) is a bijection from \( \mathbb{R} \) onto \( \mathbb{R} \) .

b) Par récurrence sur \( n \) on obtient

> b) By induction on \( n \) we obtain

\[
\forall n \in  {\mathbb{N}}^{ * },\forall x \in  \mathbb{R},\;{g}^{n}\left( x\right)  = {ng}\left( x\right)  - \left( {n - 1}\right) x.
\]

(*)

> En effet, la relation est vraie pour \( n = 1 \) ; pour passer du rang \( n \) au rang \( n + 1 \) on part de la relation (*) dans laquelle on remplace \( x \) par \( g\left( x\right) \) , ce qui donne

Indeed, the relation is true for \( n = 1 \) ; to move from rank \( n \) to rank \( n + 1 \) we start from relation (*) in which we replace \( x \) by \( g\left( x\right) \) , which gives

> \( \forall x \in \mathbb{R},\;{g}^{n + 1}\left( x\right) = n{g}^{2}\left( x\right) - \left( {n - 1}\right) g\left( x\right) = n\left( {{2g}\left( x\right) - x}\right) - \left( {n - 1}\right) g\left( x\right) = \left( {n + 1}\right) g\left( x\right) - {nx}. \)

On peut récrire la relation (*) sous la forme

> We can rewrite relation (*) in the form

\[
\forall x \in  \mathbb{R},\forall n \in  {\mathbb{N}}^{ * },\;\frac{{g}^{n}\left( x\right)  - {g}^{n}\left( 0\right) }{n} = g\left( x\right)  - g\left( 0\right)  - x + \frac{x}{n}.
\]

Comme \( g \) est croissante, \( {g}^{n} \) également donc pour tout \( n \in {\mathbb{N}}^{ * } \)

> Since \( g \) is increasing, \( {g}^{n} \) is as well, so for all \( n \in {\mathbb{N}}^{ * } \)

\[
\forall x \geq  0,\;g\left( x\right)  - g\left( 0\right)  - x + \frac{x}{n} \geq  0\;\text{ et }\;\forall x \leq  0,\;g\left( x\right)  - g\left( 0\right)  - x + \frac{x}{n} \leq  0.
\]

En fixant \( x \) puis en faisant tendre \( n \) vers l’infini, on obtient

> By fixing \( x \) and then letting \( n \) tend to infinity, we obtain

\[
\forall x \geq  0,\;g\left( x\right)  - g\left( 0\right)  - x \geq  0\;\text{ et }\;\forall x \leq  0,\;g\left( x\right)  - g\left( 0\right)  - x \leq  0.
\]

\( \left( {* * }\right) \)

> Nous avons démontré à la question précédente que \( g \) est une bijection de \( \mathbb{R} \) sur \( \mathbb{R} \) . Sa bijection réciproque \( {g}^{-1} \) est continue et vérifie

We demonstrated in the previous question that \( g \) is a bijection from \( \mathbb{R} \) onto \( \mathbb{R} \) . Its inverse bijection \( {g}^{-1} \) is continuous and satisfies

\[
\forall x \in  \mathbb{R},\;{g}^{2}\left\lbrack  {{g}^{-2}\left( x\right) }\right\rbrack   = {2g}\left\lbrack  {{g}^{-2}\left( x\right) }\right\rbrack   - {g}^{-2}\left( x\right) \;\text{ ou encore }\;{g}^{-2}\left( x\right)  = 2{g}^{-1}\left( x\right)  - x.
\]

Autrement dit, \( {g}^{-1} \) vérifie les mêmes hypothèses que \( g \) . On en conclut que (**) est vrai pour \( {g}^{-1} \) , ce qui s’écrit

> In other words, \( {g}^{-1} \) satisfies the same hypotheses as \( g \) . We conclude that (**) is true for \( {g}^{-1} \) , which is written

\[
\forall x \geq  0,\;{g}^{-1}\left( x\right)  - {g}^{-1}\left( 0\right)  - x \geq  0\;\text{ et }\;\forall x \leq  0,\;{g}^{-1}\left( x\right)  - {g}^{-1}\left( 0\right)  - x \leq  0.
\]

En utilisant la relation \( {g}^{-1}\left( x\right) = {2x} - g\left( x\right) \) (qui découle de \( {g}^{2} = {2g} - \) Id après composition à droite par \( {g}^{-1} \) ), on en déduit

> Using the relation \( {g}^{-1}\left( x\right) = {2x} - g\left( x\right) \) (which follows from \( {g}^{2} = {2g} - \) Id after composition on the right by \( {g}^{-1} \) ), we deduce

\[
\forall x \geq  0,\;g\left( x\right)  - g\left( 0\right)  - x \leq  0\;\text{ et }\;\forall x \leq  0,\;g\left( x\right)  - g\left( 0\right)  - x \geq  0.
\]

(***)

> Avec (**), on en conclut que \( g\left( x\right) = x + g\left( 0\right) \) pour tout \( x \in \mathbb{R} \) .

With (**), we conclude that \( g\left( x\right) = x + g\left( 0\right) \) for all \( x \in \mathbb{R} \) .

> Réciproquement, on vérifie facilement que toute fonction de la forme \( g : x \mapsto x + K \) vérifie les hypothèses de l'énoncé.

Conversely, it is easy to verify that any function of the form \( g : x \mapsto x + K \) satisfies the hypotheses of the statement.

> Problems 7 (DéRIVÉE SELON SCHWARZ). Soit \( I \) un intervalle ouvert non vide de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une fonction continue, telle que pour tout \( x \in I \) , la limite

Problems 7 (SCHWARZ DERIVATIVE). Let \( I \) be a non-empty open interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a continuous function, such that for all \( x \in I \) , the limit

\[
{f}^{S}\left( x\right)  = \mathop{\lim }\limits_{\substack{{h \rightarrow  0} \\  {h \neq  0} }}\frac{f\left( {x + h}\right)  - f\left( {x - h}\right) }{2h}
\]

existe (on dit que \( f \) est dérivable selon Schwarz, ou encore pseudo-dérivable, et \( {f}^{S}\left( x\right) \) est appelé la dérivée symétrique de \( f \) en \( x \) ).

> exists (we say that \( f \) is differentiable in the sense of Schwarz, or pseudo-differentiable, and \( {f}^{S}\left( x\right) \) is called the symmetric derivative of \( f \) at \( x \) ).

a) Montrer que si \( {f}^{S} \geq 0 \) , alors \( f \) est croissante (on commencera par le cas \( {f}^{S} \geq \alpha > 0 \) ). b) Montrer que si \( {f}^{S} \) est continue en \( a \in I \) , alors \( f \) est dérivable en \( a \) et \( {f}^{\prime }\left( a\right) = {f}^{S}\left( a\right) \) .

> a) Show that if \( {f}^{S} \geq 0 \) , then \( f \) is increasing (start with the case \( {f}^{S} \geq \alpha > 0 \) ). b) Show that if \( {f}^{S} \) is continuous at \( a \in I \) , then \( f \) is differentiable at \( a \) and \( {f}^{\prime }\left( a\right) = {f}^{S}\left( a\right) \) .

Solution. a) Suivons l’indication et supposons d’abord \( {f}^{S} \geq \alpha > 0 \) sur \( I \) . On raisonne par l’absurde en supposant que \( f\mathrm{n} \) ’est pas croissante, ce qui implique l’existence de \( a, b \in I, a < b \) , tels que \( f\left( a\right) > f\left( b\right) \) . L’idée est de déterminer une abscisse \( c \) tel que \( f\left( {c + h}\right) \leq f\left( {c - h}\right) \) pour des valeurs de \( h \) tendant vers 0 .

> Solution. a) Let us follow the hint and first assume \( {f}^{S} \geq \alpha > 0 \) on \( I \) . We reason by contradiction by assuming that \( f\mathrm{n} \) is not increasing, which implies the existence of \( a, b \in I, a < b \) , such that \( f\left( a\right) > f\left( b\right) \) . The idea is to determine an abscissa \( c \) such that \( f\left( {c + h}\right) \leq f\left( {c - h}\right) \) for values of \( h \) tending to 0 .

On choisit \( y \) tel que \( f\left( b\right) < y < f\left( a\right) \) et on considère l’ouvert \( O = \{ x \in \rbrack a, b\left\lbrack \right\rbrack f\left( x\right) > y\} \) . Comme \( f\left( a\right) > y \) et que \( f \) est continue, \( O \) est non vide. Donc \( c = \sup O \) est bien défini et \( c > a \) . On a \( c < b \) , puisque sur un voisinage de \( b, f\left( x\right) < y \) . Par définition de \( c \) , on a \( f\left( x\right) \leq y \) dès que \( x \in \left\lbrack {c, b\left\lbrack \right. }\right. \) . Comme \( c = \sup O \) , il existe une suite \( \left( {h}_{n}\right) \) de valeurs \( > 0 \) tendant vers 0 telle que les \( c - {h}_{n} \in O \) pour tout \( n \) , et donc telle que \( f\left( {c - {h}_{n}}\right) > y \) . Lorsque \( n \) est suffisamment grand on a \( c + {h}_{n} < b \) donc \( f\left( {c + {h}_{n}}\right) \leq y \) . Ainsi, on a \( \left( {f\left( {c + {h}_{n}}\right) - f\left( {c - {h}_{n}}\right) }\right) /\left( {2{h}_{n}}\right) \leq 0 \) , et par passage à la limite lorsque \( n \rightarrow \infty \) on en déduit \( {f}^{S}\left( c\right) \leq 0 \) , ce qui est contradictoire. On a donc bien démontré que \( f \) est croissante sur \( I \) .

> We choose \( y \) such that \( f\left( b\right) < y < f\left( a\right) \) and consider the open set \( O = \{ x \in \rbrack a, b\left\lbrack \right\rbrack f\left( x\right) > y\} \). Since \( f\left( a\right) > y \) and \( f \) is continuous, \( O \) is non-empty. Thus \( c = \sup O \) is well-defined and \( c > a \). We have \( c < b \), since on a neighborhood of \( b, f\left( x\right) < y \). By definition of \( c \), we have \( f\left( x\right) \leq y \) as soon as \( x \in \left\lbrack {c, b\left\lbrack \right. }\right. \). Since \( c = \sup O \), there exists a sequence \( \left( {h}_{n}\right) \) of values \( > 0 \) tending to 0 such that \( c - {h}_{n} \in O \) for all \( n \), and thus such that \( f\left( {c - {h}_{n}}\right) > y \). When \( n \) is sufficiently large, we have \( c + {h}_{n} < b \) so \( f\left( {c + {h}_{n}}\right) \leq y \). Thus, we have \( \left( {f\left( {c + {h}_{n}}\right) - f\left( {c - {h}_{n}}\right) }\right) /\left( {2{h}_{n}}\right) \leq 0 \), and by passing to the limit as \( n \rightarrow \infty \), we deduce \( {f}^{S}\left( c\right) \leq 0 \), which is a contradiction. We have therefore successfully demonstrated that \( f \) is increasing on \( I \).

Passons maintenant au cas où on a simplement \( {f}^{S} \geq 0 \) . Pour tout \( \alpha > 0 \) , la fonction \( {f}_{\alpha } : x \mapsto f\left( x\right) + {\alpha x} \) est dérivable selon Schwarz sur \( I \) et on a \( {f}_{\alpha }^{S}\left( x\right) = {f}^{S}\left( x\right) + \alpha \geq \alpha \) , donc d’après ce qu’on vient de montrer, \( {f}_{\alpha } \) est croissante. Ceci implique, pour tout \( a, b \in I \) tels que \( a < b \) , l’inégalité \( {f}_{\alpha }\left( a\right) \leq {f}_{\alpha }\left( b\right) \) , et ceci étant vrai pour tout \( \alpha > 0 \) on obtient \( f\left( a\right) \leq f\left( b\right) \) . Donc \( f \) est bien croissante.

> Let us now move on to the case where we simply have \( {f}^{S} \geq 0 \). For all \( \alpha > 0 \), the function \( {f}_{\alpha } : x \mapsto f\left( x\right) + {\alpha x} \) is Schwarz differentiable on \( I \) and we have \( {f}_{\alpha }^{S}\left( x\right) = {f}^{S}\left( x\right) + \alpha \geq \alpha \), so according to what we have just shown, \( {f}_{\alpha } \) is increasing. This implies, for all \( a, b \in I \) such that \( a < b \), the inequality \( {f}_{\alpha }\left( a\right) \leq {f}_{\alpha }\left( b\right) \), and since this is true for all \( \alpha > 0 \), we obtain \( f\left( a\right) \leq f\left( b\right) \). Therefore, \( f \) is indeed increasing.

b) Nous allons commencer par montrer un résultat intermédiaire, qui est l'équivalent de l'inégalité des accroissements finis pour les fonctions dérivables selon Schwarz. Supposons qu'il existe un intervalle ouvert \( J \subset I \) et \( {M}_{1},{M}_{2} \in \mathbb{R} \) tels que \( \forall x \in J;{M}_{1} \leq {f}^{S}\left( x\right) \leq {M}_{2} \) . Alors

> b) We will begin by showing an intermediate result, which is the equivalent of the mean value inequality for Schwarz differentiable functions. Suppose there exists an open interval \( J \subset I \) and \( {M}_{1},{M}_{2} \in \mathbb{R} \) such that \( \forall x \in J;{M}_{1} \leq {f}^{S}\left( x\right) \leq {M}_{2} \). Then

\[
\forall \alpha ,\beta  \in  J;\alpha  < \beta ,\;\left( {\beta  - \alpha }\right) {M}_{1} \leq  f\left( \beta \right)  - f\left( \alpha \right)  \leq  \left( {\beta  - \alpha }\right) {M}_{2}.
\]

(*)

> On montre la première inégalité en appliquant le résultat de la question précédente à la fonction \( g\left( x\right) = f\left( x\right) - {M}_{1}x \) . La fonction \( g \) est continue et dérivable selon Schwarz sur \( J \) , et \( {g}^{S} = \; {f}^{S} - {M}_{1} \geq 0 \) sur \( J \) donc \( g \) est croissante sur \( J \) , ce qui implique \( g\left( \beta \right) \geq g\left( \alpha \right) \) , prouvant ainsi la première inégalité. On montre la seconde inégalité de la même manière en considérant la fonction \( h\left( x\right) = {M}_{2}x - f\left( x\right) . \)

The first inequality is shown by applying the result of the previous question to the function \( g\left( x\right) = f\left( x\right) - {M}_{1}x \). The function \( g \) is continuous and differentiable in the sense of Schwarz on \( J \), and \( {g}^{S} = \; {f}^{S} - {M}_{1} \geq 0 \) on \( J \), so \( g \) is increasing on \( J \), which implies \( g\left( \beta \right) \geq g\left( \alpha \right) \), thus proving the first inequality. The second inequality is shown in the same way by considering the function \( h\left( x\right) = {M}_{2}x - f\left( x\right) . \).

> Prouvons maintenant la dérivabilité de \( f \) en \( a \) . Soit \( \varepsilon > 0 \) . La continuité de \( {f}^{S} \) en \( a \) implique l’existence de \( \eta > 0 \) tel que

Let us now prove the differentiability of \( f \) at \( a \). Let \( \varepsilon > 0 \). The continuity of \( {f}^{S} \) at \( a \) implies the existence of \( \eta > 0 \) such that

\[
\forall x \in  \rbrack a - \eta , a + \eta \lbrack ,\;{f}^{S}\left( a\right)  - \varepsilon  \leq  {f}^{S}\left( x\right)  \leq  {f}^{S}\left( a\right)  + \varepsilon .
\]

On en déduit, avec le résultat (*), que

> We deduce from this, with result (*), that

\[
\forall x \in  \rbrack a - \eta , a + \eta \lbrack , x \neq  a,\;{f}^{S}\left( a\right)  - \varepsilon  \leq  \frac{f\left( x\right)  - f\left( a\right) }{x - a} \leq  {f}^{S}\left( a\right)  + \varepsilon .
\]

L’existence d’un tel \( \eta > 0 \) est possible pour tout \( \varepsilon > 0 \) , ce qui prouve que \( f \) est bien dérivable en \( a \) , et on a \( {f}^{\prime }\left( a\right) = {f}^{S}\left( a\right) \) .

> The existence of such a \( \eta > 0 \) is possible for any \( \varepsilon > 0 \), which proves that \( f \) is indeed differentiable at \( a \), and we have \( {f}^{\prime }\left( a\right) = {f}^{S}\left( a\right) \).

Problem 8. On note \( E \) l’ensemble des fonctions \( f \) de classe \( {\mathcal{C}}^{1} \) bijectives de \( \rbrack 0, + \infty \lbrack \) dans \( \rbrack 0, + \infty \left\lbrack \right. \) telles que \( {f}^{\prime } = {f}^{-1} \) .

> Problem 8. Let \( E \) denote the set of \( f \) functions of class \( {\mathcal{C}}^{1} \) that are bijective from \( \rbrack 0, + \infty \lbrack \) to \( \rbrack 0, + \infty \left\lbrack \right. \) such that \( {f}^{\prime } = {f}^{-1} \).

a) Trouver un élément \( f \) de \( E \) de la forme \( x \mapsto \alpha {x}^{\beta } \) , avec \( \alpha ,\beta \in \mathbb{R} \) .

> a) Find an element \( f \) of \( E \) of the form \( x \mapsto \alpha {x}^{\beta } \), with \( \alpha ,\beta \in \mathbb{R} \).

b) Si \( f \in E \) , déterminer la limite en0de \( f \) et de \( {f}^{-1} \) .

> b) If \( f \in E \), determine the limit at 0 of \( f \) and \( {f}^{-1} \).

c) Montrer que si \( f \in E \) , alors \( f \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( \rbrack 0, + \infty \lbrack \) dans ] \( 0, + \infty \lbrack \) .

> c) Show that if \( f \in E \), then \( f \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism from \( \rbrack 0, + \infty \lbrack \) to ]\( 0, + \infty \lbrack \).

d) Montrer que toute fonction \( f \in E \) admet un unique point fixe.

> d) Show that every function \( f \in E \) admits a unique fixed point.

e) Soit \( f \) et \( g \) deux élément de \( E \) . Montrer que \( f \) et \( g \) admettent le même point fixe.

> e) Let \( f \) and \( g \) be two elements of \( E \). Show that \( f \) and \( g \) admit the same fixed point.

Solution. a) Si \( f\left( x\right) = \alpha {x}^{\beta } \) , alors \( {f}^{\prime }\left( x\right) = {\alpha \beta }{x}^{\beta - 1} \) et \( {f}^{-1}\left( x\right) = {\left( x/\alpha \right) }^{1/\beta } = {\left( 1/\alpha \right) }^{1/\beta }{x}^{1/\beta } \) . Remarquons que \( f > 0 \) donc \( \alpha = f\left( 1\right) > 0 \) . On a également \( {f}^{\prime } = {f}^{-1} > 0 \) , donc \( {f}^{\prime }\left( 1\right) = {\alpha \beta } > 0 \) ce qui entraîne \( \beta > 0 \) .

> Solution. a) If \( f\left( x\right) = \alpha {x}^{\beta } \), then \( {f}^{\prime }\left( x\right) = {\alpha \beta }{x}^{\beta - 1} \) and \( {f}^{-1}\left( x\right) = {\left( x/\alpha \right) }^{1/\beta } = {\left( 1/\alpha \right) }^{1/\beta }{x}^{1/\beta } \). Note that \( f > 0 \) so \( \alpha = f\left( 1\right) > 0 \). We also have \( {f}^{\prime } = {f}^{-1} > 0 \), so \( {f}^{\prime }\left( 1\right) = {\alpha \beta } > 0 \) which leads to \( \beta > 0 \).

On aura \( {f}^{\prime } = {f}^{-1} \) si \( {\alpha \beta } = {\left( 1/\alpha \right) }^{1/\beta } \) et si \( \beta - 1 = 1/\beta \) . La dernière équation s’écrit aussi \( {\beta }^{2} - \beta - 1 = 0 \) , dont \( \beta = \varphi = \frac{1 + \sqrt{5}}{2} \) est la seule solution positive. L’autre équation admet la solution \( \alpha = {\varphi }^{-\varphi /\left( {\varphi + 1}\right) } \) (comme \( \varphi + 1 = {\varphi }^{2} \) on a l’expression plus simple \( \alpha = {\varphi }^{-1/\varphi } \) ). Ainsi choisis, \( \alpha \) et \( \beta \) répondent bien au problème.

> We will have \( {f}^{\prime } = {f}^{-1} \) if \( {\alpha \beta } = {\left( 1/\alpha \right) }^{1/\beta } \) and if \( \beta - 1 = 1/\beta \) . The last equation can also be written as \( {\beta }^{2} - \beta - 1 = 0 \) , of which \( \beta = \varphi = \frac{1 + \sqrt{5}}{2} \) is the only positive solution. The other equation admits the solution \( \alpha = {\varphi }^{-\varphi /\left( {\varphi + 1}\right) } \) (as \( \varphi + 1 = {\varphi }^{2} \) we have the simpler expression \( \alpha = {\varphi }^{-1/\varphi } \) ). Thus chosen, \( \alpha \) and \( \beta \) satisfy the problem.

b) Si \( f \in E \) alors \( {f}^{-1} > 0 \) donc \( {f}^{\prime } = {f}^{-1} \) est positive. Donc \( f \) est croissante, et donc \( f\left( x\right) \) converge forcément vers \( \ell = \mathop{\inf }\limits_{{x > 0}}f\left( x\right) \) lorsque \( x \rightarrow 0\left( {x > 0}\right) \) . Comme \( f \) est positive, on a \( \ell \geq 0 \) . Par ailleurs, \( f\left( x\right) \geq \ell \) pour tout \( x > 0 \) , et comme \( f \) est une bijection dans \( \rbrack 0, + \infty \lbrack \) on en déduit nécessairement \( \ell = 0 \) . On montrerait de même que \( \mathop{\lim }\limits_{{x \rightarrow 0, x > 0}}{f}^{-1}\left( x\right) = 0 \) (on peut également obtenir ce dernier résultat en prolongeant \( f \) en une fonction \( \widetilde{f} \) sur \( {\mathbb{R}}^{ + } \) avec \( \widetilde{f}\left( 0\right) = 0 \) . L’application \( \widetilde{f} \) est continue et bijective de \( {\mathbb{R}}^{ + } \) dans \( {\mathbb{R}}^{ + } \) ; sa fonction réciproque est continue, en particulier en \( x = 0 \) ou elle vaut \( {\widetilde{f}}^{-1}\left( 0\right) = 0 \) ).

> b) If \( f \in E \) then \( {f}^{-1} > 0 \) so \( {f}^{\prime } = {f}^{-1} \) is positive. Thus \( f \) is increasing, and therefore \( f\left( x\right) \) necessarily converges to \( \ell = \mathop{\inf }\limits_{{x > 0}}f\left( x\right) \) as \( x \rightarrow 0\left( {x > 0}\right) \) . Since \( f \) is positive, we have \( \ell \geq 0 \) . Furthermore, \( f\left( x\right) \geq \ell \) for all \( x > 0 \) , and since \( f \) is a bijection in \( \rbrack 0, + \infty \lbrack \) we necessarily deduce \( \ell = 0 \) . We could show similarly that \( \mathop{\lim }\limits_{{x \rightarrow 0, x > 0}}{f}^{-1}\left( x\right) = 0 \) (one can also obtain this last result by extending \( f \) into a function \( \widetilde{f} \) on \( {\mathbb{R}}^{ + } \) with \( \widetilde{f}\left( 0\right) = 0 \) . The mapping \( \widetilde{f} \) is continuous and bijective from \( {\mathbb{R}}^{ + } \) to \( {\mathbb{R}}^{ + } \) ; its inverse function is continuous, in particular at \( x = 0 \) where it equals \( {\widetilde{f}}^{-1}\left( 0\right) = 0 \) ).

c) Montrons par récurrence sur \( n \in {\mathbb{N}}^{ * } \) que \( f \) est un \( {\mathcal{C}}^{n} \) difféomorphisme. Pour \( n = 1 \) , on sait par hypothèse que \( f \) est \( {\mathcal{C}}^{1} \) . Or \( {f}^{-1} > 0 \) , donc \( {f}^{\prime } = {f}^{-1} \) ne s’annule pas. On en déduit, d’après la proposition 4 page 73 sur les homéomorphismes dérivables, que \( {f}^{-1} \) est également de classe \( {\mathcal{C}}^{1} \) . Supposons maintenant \( n \geq 1 \) et que \( f \) est un \( {\mathcal{C}}^{n} \) difféomorphisme (hypothèse de récurrence). Alors \( {f}^{\prime } = {f}^{-1} \) est de classe \( {\mathcal{C}}^{n} \) , donc \( f \) est de classe \( {\mathcal{C}}^{n + 1} \) , et là encore, la proposition sur les homéomorphismes dérivables implique que \( {f}^{-1} \) est également de classe \( {\mathcal{C}}^{n + 1} \) .

> c) Let us show by induction on \( n \in {\mathbb{N}}^{ * } \) that \( f \) is a \( {\mathcal{C}}^{n} \) diffeomorphism. For \( n = 1 \) , we know by hypothesis that \( f \) is \( {\mathcal{C}}^{1} \) . However \( {f}^{-1} > 0 \) , so \( {f}^{\prime } = {f}^{-1} \) does not vanish. We deduce from this, according to proposition 4 on page 73 regarding differentiable homeomorphisms, that \( {f}^{-1} \) is also of class \( {\mathcal{C}}^{1} \) . Now assume \( n \geq 1 \) and that \( f \) is a \( {\mathcal{C}}^{n} \) diffeomorphism (induction hypothesis). Then \( {f}^{\prime } = {f}^{-1} \) is of class \( {\mathcal{C}}^{n} \) , so \( f \) is of class \( {\mathcal{C}}^{n + 1} \) , and here again, the proposition on differentiable homeomorphisms implies that \( {f}^{-1} \) is also of class \( {\mathcal{C}}^{n + 1} \) .

d) Comme \( {f}^{\prime } = {f}^{-1} \) , on a \( \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}{f}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}{f}^{-1}\left( x\right) = 0 \) . Ainsi, le prolongement \( \widetilde{f} \) par continuité de \( f \) en 0, défini en 0 par \( \widetilde{f}\left( 0\right) = 0 \) , est dérivable en 0 et \( {\widetilde{f}}^{\prime }\left( 0\right) = 0 \) (voir la proposition 6 page 76). Ceci montre que \( f\left( x\right) = o\left( x\right) \) lorsque \( x \rightarrow 0\left( {x > 0}\right) \) . En particulier, il existe \( a > 0 \) tel que \( f\left( a\right) < a/2 \) , donc \( f\left( a\right) - a < 0 \) .

> d) Since \( {f}^{\prime } = {f}^{-1} \) , we have \( \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}{f}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}{f}^{-1}\left( x\right) = 0 \) . Thus, the continuous extension \( \widetilde{f} \) of \( f \) at 0, defined at 0 by \( \widetilde{f}\left( 0\right) = 0 \) , is differentiable at 0 and \( {\widetilde{f}}^{\prime }\left( 0\right) = 0 \) (see proposition 6 on page 76). This shows that \( f\left( x\right) = o\left( x\right) \) as \( x \rightarrow 0\left( {x > 0}\right) \) . In particular, there exists \( a > 0 \) such that \( f\left( a\right) < a/2 \) , so \( f\left( a\right) - a < 0 \) .

Par ailleurs, \( {f}^{-1} \) étant croissante on a \( {f}^{\prime }\left( x\right) = {f}^{-1}\left( x\right) \geq {f}^{-1}\left( \alpha \right) = 2 \) pour \( x \geq \alpha = f\left( 2\right) \) . Lorsque \( x \geq \alpha \) , l’égalité des accroissements finis entraîne \( f\left( x\right) - f\left( \alpha \right) \geq 2\left( {x - \alpha }\right) \) , d’où on déduit \( f\left( x\right) - x \geq f\left( \alpha \right) + x - {2\alpha } \) . Ainsi, \( b = {2\alpha } \) vérifie \( f\left( b\right) - b > 0 \) .

> Furthermore, since \( {f}^{-1} \) is increasing, we have \( {f}^{\prime }\left( x\right) = {f}^{-1}\left( x\right) \geq {f}^{-1}\left( \alpha \right) = 2 \) for \( x \geq \alpha = f\left( 2\right) \) . When \( x \geq \alpha \) , the mean value theorem implies \( f\left( x\right) - f\left( \alpha \right) \geq 2\left( {x - \alpha }\right) \) , from which we deduce \( f\left( x\right) - x \geq f\left( \alpha \right) + x - {2\alpha } \) . Thus, \( b = {2\alpha } \) satisfies \( f\left( b\right) - b > 0 \) .

Ainsi, nous avons montré que la fonction continue \( f\left( x\right) - x \) change de signe sur \( \left\lbrack {a, b}\right\rbrack \) , elle s’annule donc en un point \( c \) de cet intervalle, qui est un point fixe de \( f \) .

> Thus, we have shown that the continuous function \( f\left( x\right) - x \) changes sign on \( \left\lbrack {a, b}\right\rbrack \) , so it vanishes at a point \( c \) in this interval, which is a fixed point of \( f \) .

Montrons que le point fixe de \( f \) est unique. Un dessin nous suggère d’utiliser la convexité de \( f \) . Si \( f \) admet deux points fixes \( c \) et \( d \) (avec \( 0 < c < d \) ), alors \( f \) étant convexe \( \left( {{f}^{\prime } = {f}^{-1}}\right. \) est croissante), elle vérifie \( f\left( x\right) \geq f\left( c\right) + \left( {x - c}\right) {f}^{\prime }\left( c\right) = c + \left( {x - c}\right) {f}^{\prime }\left( c\right) \) pour tout \( x > 0 \) . En faisant tendre \( x \) vers 0 on en déduit \( 0 \geq c\left( {1 - {f}^{\prime }\left( c\right) }\right) \) , donc \( {f}^{\prime }\left( c\right) \geq 1 \) . On a même \( {f}^{\prime }\left( c\right) > 1 \) car si \( {f}^{\prime }\left( c\right) = 1 \) , alors \( f\left( x\right) \geq c + \left( {x - c}\right) {f}^{\prime }\left( c\right) = x \) , ce qui est incompatible avec \( f\left( x\right) = o\left( x\right) \) lorsque \( x \rightarrow 0 \) . Ceci implique \( f\left( d\right) \geq c + \left( {d - c}\right) {f}^{\prime }\left( c\right) > d \) donc \( d \) ne peut pas être un deuxième point fixe de \( f \) . e) Nous utiliserons le lemme suivant :

> Let us show that the fixed point of \( f \) is unique. A drawing suggests we use the convexity of \( f \). If \( f \) admits two fixed points \( c \) and \( d \) (with \( 0 < c < d \) ), then since \( f \) is convex \( \left( {{f}^{\prime } = {f}^{-1}}\right. \) is increasing), it satisfies \( f\left( x\right) \geq f\left( c\right) + \left( {x - c}\right) {f}^{\prime }\left( c\right) = c + \left( {x - c}\right) {f}^{\prime }\left( c\right) \) for all \( x > 0 \) . By letting \( x \) tend to 0, we deduce \( 0 \geq c\left( {1 - {f}^{\prime }\left( c\right) }\right) \) , therefore \( {f}^{\prime }\left( c\right) \geq 1 \) . We even have \( {f}^{\prime }\left( c\right) > 1 \) because if \( {f}^{\prime }\left( c\right) = 1 \) , then \( f\left( x\right) \geq c + \left( {x - c}\right) {f}^{\prime }\left( c\right) = x \) , which is incompatible with \( f\left( x\right) = o\left( x\right) \) when \( x \rightarrow 0 \) . This implies \( f\left( d\right) \geq c + \left( {d - c}\right) {f}^{\prime }\left( c\right) > d \) so \( d \) cannot be a second fixed point of \( f \) . e) We will use the following lemma:

LEMME 1. Soit \( f \in E \) et \( \lambda > 0 \) le point fixe de \( f \) . Alors on a \( f\left( x\right) < x \) pour \( 0 < x < \lambda \) et \( f\left( x\right) > x \) pour \( x > \lambda . \)

> LEMMA 1. Let \( f \in E \) and \( \lambda > 0 \) be the fixed point of \( f \) . Then we have \( f\left( x\right) < x \) for \( 0 < x < \lambda \) and \( f\left( x\right) > x \) for \( x > \lambda . \)

En effet, \( f \) n’a que le seul point fixe \( \lambda \) , donc \( f\left( x\right) - x \) garde un signe constant non nul sur \( \rbrack 0,\lambda \left\lbrack \right. \) , et comme \( f\left( x\right) = o\left( x\right) \) lorsque \( x \rightarrow 0, f\left( x\right) - x \) est forcément négatif sur cet intervalle. De même, \( f\left( x\right) - x \) garde un signe constant non nul pour \( x > \lambda \) . Nous avons vu plus haut qu’il existe \( \mu > 0 \) tel que \( f\left( \mu \right) - \mu > 0 \) . On a donc forcément \( \mu > \lambda \) , et finalement le signe de \( f\left( x\right) - x \) est strictement positif sur \( \rbrack \lambda , + \infty \lbrack \) .

> Indeed, \( f \) has only the single fixed point \( \lambda \) , so \( f\left( x\right) - x \) maintains a constant non-zero sign on \( \rbrack 0,\lambda \left\lbrack \right. \) , and since \( f\left( x\right) = o\left( x\right) \) when \( x \rightarrow 0, f\left( x\right) - x \) it is necessarily negative on this interval. Similarly, \( f\left( x\right) - x \) maintains a constant non-zero sign for \( x > \lambda \) . We saw above that there exists \( \mu > 0 \) such that \( f\left( \mu \right) - \mu > 0 \) . We therefore necessarily have \( \mu > \lambda \) , and finally the sign of \( f\left( x\right) - x \) is strictly positive on \( \rbrack \lambda , + \infty \lbrack \) .

![bo_d7fjkrs91nqc73ereoog_114_455_610_679_632_0.jpg](images/gourdon_analysis_fr_en_006_bod7fjkrs91nqc73ereoog1144556106796320.jpg)

Figure 9. Le graphe des applications \( f \) et \( g \) et leurs fonctions inverses

> Figure 9. The graph of the mappings \( f \) and \( g \) and their inverse functions

Raisonnons maintenant par l’absurde et supposons l’existence de \( f, g \in E \) tels que \( f\left( a\right) = a \) et \( g\left( b\right) = b \) avec \( a \neq b \) , par exemple \( a < b \) (voir la figure ci-contre). D’après le lemme, on a \( g\left( x\right) < x \) sur \( \rbrack 0, b\lbrack \) , en particulier \( g\left( a\right) < a = f\left( a\right) \) . Toujours d’après le lemme, on a \( x \leq f\left( x\right) \) pour \( x \in \left\lbrack {a, b}\right\rbrack \) , et finalement \( g\left( x\right) < x \leq f\left( x\right) \) pour \( x \in \lbrack a, b\lbrack \) . Soit \( c \) le plus petit réel positif tel que \( g\left( x\right) < f\left( x\right) \) sur l’intervalle \( \rbrack c, b\lbrack \) (on a \( 0 \leq c < a \) ).

> Let us now reason by contradiction and assume the existence of \( f, g \in E \) such that \( f\left( a\right) = a \) and \( g\left( b\right) = b \) with \( a \neq b \) , for example \( a < b \) (see the figure opposite). According to the lemma, we have \( g\left( x\right) < x \) on \( \rbrack 0, b\lbrack \) , in particular \( g\left( a\right) < a = f\left( a\right) \) . Still according to the lemma, we have \( x \leq f\left( x\right) \) for \( x \in \left\lbrack {a, b}\right\rbrack \) , and finally \( g\left( x\right) < x \leq f\left( x\right) \) for \( x \in \lbrack a, b\lbrack \) . Let \( c \) be the smallest positive real number such that \( g\left( x\right) < f\left( x\right) \) on the interval \( \rbrack c, b\lbrack \) (we have \( 0 \leq c < a \) ).

Montrons maintenant que \( {g}^{-1} > {f}^{-1} \) sur \( \rbrack c, b\lbrack \) (on le voit sur la figure). Tout d’abord, on remarque que \( \rbrack c, b\left\lbrack { \subset f\left( {\rbrack c, b\lbrack }\right) \text{ car d’après le lemme, }f\left( c\right) < c}\right. \) et \( f\left( b\right) > b \) . Ceci entraîne \( {f}^{-1}\left( {\rbrack c, b\left\lbrack \right\rbrack \subset }\right) c, b\lbrack \) . On montre aussi facilement que \( {g}^{-1}\left( {\rbrack c, b\left\lbrack \right\rbrack \subset }\right) c, b\lbrack \) . Considérons maintenant \( c < y < b \) . Comme \( x = {f}^{-1}\left( y\right) \in \rbrack c, b\lbrack \) , on a \( g\left( x\right) < f\left( x\right) \) . Ceci s’écrit aussi \( g\left( {{f}^{-1}\left( y\right) }\right) < y \) , c’est-à-dire \( g\left( {{f}^{-1}\left( y\right) }\right) < g\left( {{g}^{-1}\left( y\right) }\right) \) et comme \( g \) est strictement croissante, on a nécessairement \( {f}^{-1}\left( y\right) < {g}^{-1}\left( y\right) . \)

> Let us now show that \( {g}^{-1} > {f}^{-1} \) on \( \rbrack c, b\lbrack \) (we can see it in the figure). First of all, we note that \( \rbrack c, b\left\lbrack { \subset f\left( {\rbrack c, b\lbrack }\right) \text{ car d’après le lemme, }f\left( c\right) < c}\right. \) and \( f\left( b\right) > b \) . This implies \( {f}^{-1}\left( {\rbrack c, b\left\lbrack \right\rbrack \subset }\right) c, b\lbrack \) . We also easily show that \( {g}^{-1}\left( {\rbrack c, b\left\lbrack \right\rbrack \subset }\right) c, b\lbrack \) . Let us now consider \( c < y < b \) . Since \( x = {f}^{-1}\left( y\right) \in \rbrack c, b\lbrack \) , we have \( g\left( x\right) < f\left( x\right) \) . This can also be written as \( g\left( {{f}^{-1}\left( y\right) }\right) < y \) , that is to say \( g\left( {{f}^{-1}\left( y\right) }\right) < g\left( {{g}^{-1}\left( y\right) }\right) \) and since \( g \) is strictly increasing, we necessarily have \( {f}^{-1}\left( y\right) < {g}^{-1}\left( y\right) . \)

Terminons la démonstration. Comme \( {g}^{\prime } = {g}^{-1} \) et \( {f}^{\prime } = {f}^{-1} \) , ce que nous venons de mon-trer s’écrit \( {g}^{\prime } > {f}^{\prime } \) sur \( \rbrack c, b\left\lbrack {\text{ , donc }g - f\text{ est strictement croissante sur }}\right\rbrack c, b\lbrack \) . En particulier, \( \mathop{\lim }\limits_{{x \rightarrow c}}g\left( x\right) - f\left( x\right) < g\left( b\right) - f\left( b\right) \leq 0 \) . Ceci entraîne \( c > 0 \) (car \( g\left( x\right) - f\left( x\right) \) tend vers 0 lorsque \( x \rightarrow 0 \) ), donc \( g\left( c\right) - f\left( c\right) < 0 \) , ce qui est incompatible avec la définition de \( c \) .

> Let us finish the proof. As \( {g}^{\prime } = {g}^{-1} \) and \( {f}^{\prime } = {f}^{-1} \), what we have just shown can be written as \( {g}^{\prime } > {f}^{\prime } \) on \( \rbrack c, b\left\lbrack {\text{ , donc }g - f\text{ est strictement croissante sur }}\right\rbrack c, b\lbrack \). In particular, \( \mathop{\lim }\limits_{{x \rightarrow c}}g\left( x\right) - f\left( x\right) < g\left( b\right) - f\left( b\right) \leq 0 \). This implies \( c > 0 \) (since \( g\left( x\right) - f\left( x\right) \) tends to 0 as \( x \rightarrow 0 \)), therefore \( g\left( c\right) - f\left( c\right) < 0 \), which is incompatible with the definition of \( c \).

Ainsi, toutes les fonctions \( f \) de \( E \) ont le même point fixe \( \lambda \) . C’est donc celui de la fonction \( F\left( x\right) = {\varphi }^{-1/\varphi }{x}^{\varphi } \) que nous avons construite dans la question a). On calcule ce point fixe en résolvant l’équation \( F\left( \lambda \right) = \lambda \) :

> Thus, all functions \( f \) of \( E \) have the same fixed point \( \lambda \). It is therefore that of the function \( F\left( x\right) = {\varphi }^{-1/\varphi }{x}^{\varphi } \) which we constructed in question a). We calculate this fixed point by solving the equation \( F\left( \lambda \right) = \lambda \):

\[
F\left( \lambda \right)  = \lambda  \Leftrightarrow  {\varphi }^{-1/\varphi }{\lambda }^{\varphi  - 1} = 1 \Leftrightarrow  \lambda  = {\varphi }^{1/\left( {\varphi \left( {\varphi  - 1}\right) }\right) }
\]

et comme \( {\varphi }^{2} - \varphi = 1 \) , on trouve que le point fixe des applications de \( E \) est le nombre d’or \( \lambda = \varphi = \frac{1 + \sqrt{5}}{2}. \)

> and since \( {\varphi }^{2} - \varphi = 1 \), we find that the fixed point of the mappings of \( E \) is the golden ratio \( \lambda = \varphi = \frac{1 + \sqrt{5}}{2}. \)

Problem 9 (THÉORÉME DE SARKOWSKI). Soit \( I \) un segment de \( \mathbb{R} \) et \( f : I \rightarrow I \) une fonction continue.

> Problem 9 (SARKOWSKII'S THEOREM). Let \( I \) be a segment of \( \mathbb{R} \) and \( f : I \rightarrow I \) a continuous function.

a) Pour tout segment \( K \) inclus dans \( f\left( I\right) \) , montrer qu’il existe un segment \( J \) inclus dans \( I \) tel que \( K = f\left( J\right) \) .

> a) For any segment \( K \) included in \( f\left( I\right) \), show that there exists a segment \( J \) included in \( I \) such that \( K = f\left( J\right) \).

b) Si \( {S}_{1} \) et \( {S}_{2} \) sont deux segments de \( I \) tels que \( {S}_{2} \subset f\left( {S}_{1}\right) \) on note \( {S}_{1} \rightarrow {S}_{2} \) . Supposons qu’il existe \( n \in {\mathbb{N}}^{ * } \) segments \( {I}_{0},\ldots ,{I}_{n - 1} \) de \( I \) tels que \( {I}_{0} \rightarrow {I}_{1} \rightarrow \ldots {I}_{n - 1} \rightarrow {I}_{0} \) . Montrer que la fonction \( {f}^{n} = f \circ f \circ \cdots \circ f \) admet un point fixe \( {x}_{0} \) tel que \( {f}^{k}\left( {x}_{0}\right) \in {I}_{k} \) pour \( k = 0,1,\ldots , n - 1 \) .

> b) If \( {S}_{1} \) and \( {S}_{2} \) are two segments of \( I \) such that \( {S}_{2} \subset f\left( {S}_{1}\right) \), we denote \( {S}_{1} \rightarrow {S}_{2} \). Suppose there exist \( n \in {\mathbb{N}}^{ * } \) segments \( {I}_{0},\ldots ,{I}_{n - 1} \) of \( I \) such that \( {I}_{0} \rightarrow {I}_{1} \rightarrow \ldots {I}_{n - 1} \rightarrow {I}_{0} \). Show that the function \( {f}^{n} = f \circ f \circ \cdots \circ f \) admits a fixed point \( {x}_{0} \) such that \( {f}^{k}\left( {x}_{0}\right) \in {I}_{k} \) for \( k = 0,1,\ldots , n - 1 \).

c) Pour \( n \in {\mathbb{N}}^{ * } \) , si \( x \in I \) vérifie \( {f}^{n}\left( x\right) = x \) et \( {f}^{k}\left( x\right) \neq x \) pour \( 1 \leq k \leq n - 1 \) , on dit que \( x \) est un point \( n \) -périodique. S’il existe un point 3-périodique pour \( f \) , montrer qu’il existe des points \( n \) -périodiques pour tout \( n \in {\mathbb{N}}^{ * } \) . a \( {x}_{n} \leq b \leq {f}^{k}\left( {x}_{n}\right) \) pour \( k = 1,\ldots , n - 1 \) et on ne peut pas avoir \( {x}_{n} = b \) (sinon \( {f}^{2}\left( {x}_{n}\right) = a \) ce qui est impossible car \( {f}^{2}\left( {x}_{n}\right) \geq b) \) donc \( {x}_{n} \) est bien un point \( n \) -périodique de \( f \) .

> c) For \( n \in {\mathbb{N}}^{ * } \), if \( x \in I \) satisfies \( {f}^{n}\left( x\right) = x \) and \( {f}^{k}\left( x\right) \neq x \) for \( 1 \leq k \leq n - 1 \), we say that \( x \) is a \( n \)-periodic point. If there exists a 3-periodic point for \( f \), show that there exist \( n \)-periodic points for all \( n \in {\mathbb{N}}^{ * } \). a \( {x}_{n} \leq b \leq {f}^{k}\left( {x}_{n}\right) \) for \( k = 1,\ldots , n - 1 \) and we cannot have \( {x}_{n} = b \) (otherwise \( {f}^{2}\left( {x}_{n}\right) = a \) which is impossible because \( {f}^{2}\left( {x}_{n}\right) \geq b) \) therefore \( {x}_{n} \) is indeed a \( n \)-periodic point of \( f \).

---

Solution. a) Soit \( \alpha ,\beta \in \mathbb{R} \) tels que \( K = \left\lbrack {\alpha ,\beta }\right\rbrack \) . L’hypothèse \( K \subset f\left( I\right) \) implique l’existence de \( a, b \in I \) tels que \( \alpha = f\left( a\right) \) et \( \beta = f\left( b\right) \) . Si \( \alpha = \beta \) le résultat est immédiat, en choissant \( J = \{ a\} \) . Dans le cas \( \alpha < \beta \) , on a \( a \neq b \) .

> Solution. a) Let \( \alpha ,\beta \in \mathbb{R} \) be such that \( K = \left\lbrack {\alpha ,\beta }\right\rbrack \). The hypothesis \( K \subset f\left( I\right) \) implies the existence of \( a, b \in I \) such that \( \alpha = f\left( a\right) \) and \( \beta = f\left( b\right) \). If \( \alpha = \beta \) the result is immediate, by choosing \( J = \{ a\} \). In the case \( \alpha < \beta \), we have \( a \neq b \).

Commençons par le cas \( a < b \) . L’idée est de déterminer des antécédents de \( \alpha \) et \( \beta \) , de sorte qu’entre les deux, il n’y ait pas d’autres antécédents de \( \alpha \) et \( \beta \) . On considère l’ensemble \( A = \{ x \in \left\lbrack {a, b}\right\rbrack \mid f\left( x\right) = \beta \} \) , fermé non vide (il contient \( b \) ) et minoré par \( a \) . On peut donc définir \( v = \inf A \) , et on a \( f\left( v\right) = \beta \) . L’ensemble \( B = \{ x \in \left\lbrack {a, v}\right\rbrack \mid f\left( x\right) = \alpha \} \) est aussi un fermé non vide (il contient \( a \) ) et majoré par \( v \) . On peut donc définir \( u = \sup B \) , et on a \( f\left( u\right) = \alpha \) et \( u < v \) . Le segment \( J = \left\lbrack {u, v}\right\rbrack \) vérifie bien \( f\left( J\right) = K \) : comme \( f\left( u\right) = \alpha \) et \( f\left( v\right) = \beta \) , le théorème des valeurs intermédiaires assure que \( K \subset f\left( J\right) \) . On a bien l’égalité sinon il existerait \( w \in J \) tel que \( f\left( w\right) \notin K \) . Si \( f\left( w\right) > \beta \) , alors par continuité de \( f \) il existerait \( x \in \lbrack u, w\lbrack \) (donc \( x < v \) ) tel que \( f\left( x\right) = \beta \) ce qui est en contradiction avec la définition de \( v \) ; si \( f\left( w\right) < \alpha \) alors il existerait \( x \in \rbrack w, v\rbrack \) (donc \( x > u \) ) tel que \( f\left( x\right) = \alpha \) ce qui est en contradiction avec la définition de \( u \) .

> Let us start with the case \( a < b \) . The idea is to determine antecedents of \( \alpha \) and \( \beta \) such that there are no other antecedents of \( \alpha \) and \( \beta \) between them. Consider the set \( A = \{ x \in \left\lbrack {a, b}\right\rbrack \mid f\left( x\right) = \beta \} \) , which is closed, non-empty (it contains \( b \) ), and bounded below by \( a \) . We can therefore define \( v = \inf A \) , and we have \( f\left( v\right) = \beta \) . The set \( B = \{ x \in \left\lbrack {a, v}\right\rbrack \mid f\left( x\right) = \alpha \} \) is also closed, non-empty (it contains \( a \) ), and bounded above by \( v \) . We can therefore define \( u = \sup B \) , and we have \( f\left( u\right) = \alpha \) and \( u < v \) . The segment \( J = \left\lbrack {u, v}\right\rbrack \) satisfies \( f\left( J\right) = K \) : since \( f\left( u\right) = \alpha \) and \( f\left( v\right) = \beta \) , the intermediate value theorem ensures that \( K \subset f\left( J\right) \) . We indeed have equality, otherwise there would exist \( w \in J \) such that \( f\left( w\right) \notin K \) . If \( f\left( w\right) > \beta \) , then by continuity of \( f \) there would exist \( x \in \lbrack u, w\lbrack \) (thus \( x < v \) ) such that \( f\left( x\right) = \beta \) , which contradicts the definition of \( v \) ; if \( f\left( w\right) < \alpha \) , then there would exist \( x \in \rbrack w, v\rbrack \) (thus \( x > u \) ) such that \( f\left( x\right) = \alpha \) , which contradicts the definition of \( u \) .

On traite le cas \( a > b \) de la même manière en prenant cette fois \( u = \sup \{ x \in \left\lbrack {b, a}\right\rbrack \mid f\left( x\right) = \beta \} \) puis \( v = \inf \{ x \in \left\lbrack {u, a}\right\rbrack \mid f\left( x\right) = \alpha \} \) .

> We treat the case \( a > b \) in the same way by taking \( u = \sup \{ x \in \left\lbrack {b, a}\right\rbrack \mid f\left( x\right) = \beta \} \) then \( v = \inf \{ x \in \left\lbrack {u, a}\right\rbrack \mid f\left( x\right) = \alpha \} \) this time.

b) On commence par le cas \( n = 1 \) .Supposons \( {I}_{0} \subset f\left( {I}_{0}\right) \) et notons \( {I}_{0} = \left\lbrack {\alpha ,\beta }\right\rbrack \) . Il existe \( a, b \in \left\lbrack {\alpha ,\beta }\right\rbrack \) tel que \( f\left( a\right) \leq \alpha \) et \( f\left( b\right) \geq \beta \) . Ainsi la fonction \( g\left( x\right) = f\left( x\right) - x \) vérifie \( g\left( a\right) \leq 0 \) et \( g\left( b\right) \geq 0 \) . Cette fonction est continue et change de signe sur \( {I}_{0} \) , il existe donc \( {x}_{0} \in {I}_{0} \) tel que \( g\left( {x}_{0}\right) = 0 \) , c’est-à-dire \( f\left( {x}_{0}\right) = {x}_{0} \) .

> b) We begin with the case \( n = 1 \) . Suppose \( {I}_{0} \subset f\left( {I}_{0}\right) \) and let \( {I}_{0} = \left\lbrack {\alpha ,\beta }\right\rbrack \) . There exists \( a, b \in \left\lbrack {\alpha ,\beta }\right\rbrack \) such that \( f\left( a\right) \leq \alpha \) and \( f\left( b\right) \geq \beta \) . Thus the function \( g\left( x\right) = f\left( x\right) - x \) satisfies \( g\left( a\right) \leq 0 \) and \( g\left( b\right) \geq 0 \) . This function is continuous and changes sign on \( {I}_{0} \) , so there exists \( {x}_{0} \in {I}_{0} \) such that \( g\left( {x}_{0}\right) = 0 \) , that is to say \( f\left( {x}_{0}\right) = {x}_{0} \) .

Traitons maintenant le cas \( n = 2 \) , en supposant que \( {I}_{0} \rightarrow {I}_{1} \rightarrow {I}_{0} \) . On a \( {I}_{1} \subset f\left( {I}_{0}\right) \) donc le résultat de la question précédente assure l’existence d’un segment \( J \subset {I}_{0} \) tel que \( {I}_{1} = f\left( J\right) \) . Comme \( {I}_{0} \subset f\left( {I}_{1}\right) \) , on en déduit \( J \subset {I}_{0} \subset {f}^{2}\left( J\right) \) . Le cas \( n = 1 \) appliqué à la fonction \( {f}^{2} \) montre l’existence d’un point fixe \( {x}_{0} \in J \) de \( {f}^{2} \) . On a bien \( {x}_{0} \in {I}_{0} \) et \( f\left( {x}_{0}\right) \in f\left( J\right) = {I}_{1} \) , nous avons donc démontré le cas \( n = 2 \) .

> Let us now treat the case \( n = 2 \), assuming that \( {I}_{0} \rightarrow {I}_{1} \rightarrow {I}_{0} \). We have \( {I}_{1} \subset f\left( {I}_{0}\right) \), so the result of the previous question ensures the existence of a segment \( J \subset {I}_{0} \) such that \( {I}_{1} = f\left( J\right) \). Since \( {I}_{0} \subset f\left( {I}_{1}\right) \), we deduce \( J \subset {I}_{0} \subset {f}^{2}\left( J\right) \). The case \( n = 1 \) applied to the function \( {f}^{2} \) shows the existence of a fixed point \( {x}_{0} \in J \) of \( {f}^{2} \). We indeed have \( {x}_{0} \in {I}_{0} \) and \( f\left( {x}_{0}\right) \in f\left( J\right) = {I}_{1} \), so we have proven the case \( n = 2 \).

Voyons maintenant le cas général \( n \geq 3 \) . Comme \( {I}_{1} \subset f\left( {I}_{0}\right) \) il existe un segment \( {J}_{1} \subset {I}_{0} \) tel que \( f\left( {J}_{1}\right) = {I}_{1} \) . On a alors \( {I}_{2} \subset f\left( {I}_{1}\right) = {f}^{2}\left( {J}_{1}\right) \) , donc il existe un segment \( {J}_{2} \subset {J}_{1} \) tel que \( {f}^{2}\left( {J}_{2}\right) = {I}_{2} \) . On construit ainsi des segments \( {J}_{3},\ldots ,{J}_{n - 1} \) tels que \( {J}_{n - 1} \subset \ldots \subset {J}_{2} \subset {J}_{1} \subset {I}_{0} \) et \( {f}^{k}\left( {J}_{k}\right) = {I}_{k} \) pour \( k = 1,\ldots , n - 1 \) . Comme \( {I}_{0} \subset {I}_{n - 1} = {f}^{n}\left( {J}_{n - 1}\right) \) , il existe un segment \( {J}_{n} \subset {J}_{n - 1} \) tel que \( {f}^{n}\left( {J}_{n}\right) = {I}_{0} \) . On a \( {J}_{n} \subset {I}_{0} = {f}^{n}\left( {J}_{n}\right) \) , et donc \( {f}^{n} \) admet un point fixe \( {x}_{0} \in {J}_{n} \subset {I}_{0} \) . Par construction on a \( {f}^{k}\left( {x}_{0}\right) \in {I}_{k} \) pour \( k = 1,\ldots , n - 1 \) .

> Let us now look at the general case \( n \geq 3 \). Since \( {I}_{1} \subset f\left( {I}_{0}\right) \), there exists a segment \( {J}_{1} \subset {I}_{0} \) such that \( f\left( {J}_{1}\right) = {I}_{1} \). We then have \( {I}_{2} \subset f\left( {I}_{1}\right) = {f}^{2}\left( {J}_{1}\right) \), so there exists a segment \( {J}_{2} \subset {J}_{1} \) such that \( {f}^{2}\left( {J}_{2}\right) = {I}_{2} \). We thus construct segments \( {J}_{3},\ldots ,{J}_{n - 1} \) such that \( {J}_{n - 1} \subset \ldots \subset {J}_{2} \subset {J}_{1} \subset {I}_{0} \) and \( {f}^{k}\left( {J}_{k}\right) = {I}_{k} \) for \( k = 1,\ldots , n - 1 \). Since \( {I}_{0} \subset {I}_{n - 1} = {f}^{n}\left( {J}_{n - 1}\right) \), there exists a segment \( {J}_{n} \subset {J}_{n - 1} \) such that \( {f}^{n}\left( {J}_{n}\right) = {I}_{0} \). We have \( {J}_{n} \subset {I}_{0} = {f}^{n}\left( {J}_{n}\right) \), and therefore \( {f}^{n} \) admits a fixed point \( {x}_{0} \in {J}_{n} \subset {I}_{0} \). By construction, we have \( {f}^{k}\left( {x}_{0}\right) \in {I}_{k} \) for \( k = 1,\ldots , n - 1 \).

c) Notons \( a \) un point 3-périodique de \( f \) , et \( b = f\left( a\right) , c = {f}^{2}\left( a\right) \) . Tous les points \( a, b \) et \( c \) sont 3-periodiques donc quitte à remplacer \( a \) par \( b \) ou \( c \) , on peut supposer \( a < b \) et \( a < c \) .

> c) Let \( a \) be a 3-periodic point of \( f \), and \( b = f\left( a\right) , c = {f}^{2}\left( a\right) \). All points \( a, b \) and \( c \) are 3-periodic, so by replacing \( a \) with \( b \) or \( c \) if necessary, we can assume \( a < b \) and \( a < c \).

- Supposons \( b < c \) , de sorte que \( a < b < c \) . Soit \( {I}_{0} = \left\lbrack  {a, b}\right\rbrack \) et \( {I}_{1} = \left\lbrack  {b, c}\right\rbrack \) . Comme \( b = f\left( a\right) \) et \( c = f\left( b\right) \) , le théorème des valeurs intermédiaires assure que \( {I}_{1} \subset  f\left( {I}_{0}\right) \) , c’est-à-dire \( {I}_{0} \rightarrow  {I}_{1} \) . De même, \( f\left( b\right)  = c \) et \( f\left( c\right)  = a \) donc \( \left\lbrack  {a, c}\right\rbrack   \subset  f\left( {I}_{1}\right) \) ce qui implique \( {I}_{1} \rightarrow  {I}_{0} \) et \( {I}_{1} \rightarrow  {I}_{1} \) . La propriété \( {I}_{1} \rightarrow  {I}_{1} \) entraîne l’existence d’un point fixe de \( f \) dans \( {I}_{1} \) . On a \( {I}_{0} \rightarrow  {I}_{1} \rightarrow  {I}_{0} \) et ceci entraîne l’existence d’un point fixe \( {x}_{2} \in  {I}_{0} \) de \( {f}^{2} \) tel que \( f\left( {x}_{2}\right)  \in  {I}_{1} \) . On a bien \( {x}_{2} \neq  f\left( {x}_{2}\right) \) (car \( {x}_{2} \in  {I}_{0} \) et \( f\left( {x}_{2}\right)  \in  {I}_{1} \) , donc \( {x}_{2} \leq  b \leq  f\left( {x}_{2}\right) \) donc si \( {x}_{2} = f\left( {x}_{2}\right) \) on aurait \( {x}_{2} = b \) ce qui est impossible puisque \( b \) est un point 3-périodique de \( f \) ). Ainsi, \( {x}_{2} \) est un point 2-périodique de \( f \) . Pour \( n \geq  4 \) , le cycle \( {I}_{0} \rightarrow  {I}_{1} \rightarrow  {I}_{1} \rightarrow  \ldots  \rightarrow  {I}_{1} \rightarrow  {I}_{0} \) , où l’intervalle \( {I}_{1} \) figure \( n - 1 \) fois, montre l’existence d’un point fixe \( {x}_{n} \in  {I}_{0} \) de \( {f}^{n} \) tel que \( {f}^{k}\left( {x}_{n}\right)  \in  {I}_{1} \) pour \( k = 1,\ldots , n - 1 \) . Ici aussi, on

> - Suppose \( b < c \) , so that \( a < b < c \) . Let \( {I}_{0} = \left\lbrack  {a, b}\right\rbrack \) and \( {I}_{1} = \left\lbrack  {b, c}\right\rbrack \) . Since \( b = f\left( a\right) \) and \( c = f\left( b\right) \) , the intermediate value theorem ensures that \( {I}_{1} \subset  f\left( {I}_{0}\right) \) , that is \( {I}_{0} \rightarrow  {I}_{1} \) . Similarly, \( f\left( b\right)  = c \) and \( f\left( c\right)  = a \) so \( \left\lbrack  {a, c}\right\rbrack   \subset  f\left( {I}_{1}\right) \) which implies \( {I}_{1} \rightarrow  {I}_{0} \) and \( {I}_{1} \rightarrow  {I}_{1} \) . The property \( {I}_{1} \rightarrow  {I}_{1} \) leads to the existence of a fixed point of \( f \) in \( {I}_{1} \) . We have \( {I}_{0} \rightarrow  {I}_{1} \rightarrow  {I}_{0} \) and this leads to the existence of a fixed point \( {x}_{2} \in  {I}_{0} \) of \( {f}^{2} \) such that \( f\left( {x}_{2}\right)  \in  {I}_{1} \) . We indeed have \( {x}_{2} \neq  f\left( {x}_{2}\right) \) (because \( {x}_{2} \in  {I}_{0} \) and \( f\left( {x}_{2}\right)  \in  {I}_{1} \) , so \( {x}_{2} \leq  b \leq  f\left( {x}_{2}\right) \) so if \( {x}_{2} = f\left( {x}_{2}\right) \) we would have \( {x}_{2} = b \) which is impossible since \( b \) is a 3-periodic point of \( f \) ). Thus, \( {x}_{2} \) is a 2-periodic point of \( f \) . For \( n \geq  4 \) , the cycle \( {I}_{0} \rightarrow  {I}_{1} \rightarrow  {I}_{1} \rightarrow  \ldots  \rightarrow  {I}_{1} \rightarrow  {I}_{0} \) , where the interval \( {I}_{1} \) appears \( n - 1 \) times, shows the existence of a fixed point \( {x}_{n} \in  {I}_{0} \) of \( {f}^{n} \) such that \( {f}^{k}\left( {x}_{n}\right)  \in  {I}_{1} \) for \( k = 1,\ldots , n - 1 \) . Here too, we

---

- Le cas \( a < c < b \) se traite de la même manière en posant \( {I}_{0} = \left\lbrack  {a, c}\right\rbrack \) et \( {I}_{1} = \left\lbrack  {c, b}\right\rbrack \) . On a ici \( {I}_{1} \rightarrow  {I}_{0},{I}_{0} \rightarrow  {I}_{1} \) et \( {I}_{0} \rightarrow  {I}_{0} \) . En échangeant le rôle de \( {I}_{0} \) et \( {I}_{1} \) dans le raisonnement précédent on démontre également l’existence d’un point \( n \) -périodique de \( f \) pour tout \( n \in  {\mathbb{N}}^{ * } \) .

> - The case \( a < c < b \) is handled in the same way by setting \( {I}_{0} = \left\lbrack  {a, c}\right\rbrack \) and \( {I}_{1} = \left\lbrack  {c, b}\right\rbrack \) . We have here \( {I}_{1} \rightarrow  {I}_{0},{I}_{0} \rightarrow  {I}_{1} \) and \( {I}_{0} \rightarrow  {I}_{0} \) . By swapping the roles of \( {I}_{0} \) and \( {I}_{1} \) in the previous reasoning, we also demonstrate the existence of a \( n \) -periodic point of \( f \) for all \( n \in  {\mathbb{N}}^{ * } \) .

Problem 10 (Courbe DE PÉANO - REMPLISSANT UN CARRÉ). On se donne deux fonctions \( f, g : \mathbb{R} \rightarrow \mathbb{R} \) continues,à valeurs dans \( \left\lbrack {0,1}\right\rbrack ,1 \) -périodiques et vérifiant :

> Problem 10 (PEANO CURVE - FILLING A SQUARE). Let two continuous functions \( f, g : \mathbb{R} \rightarrow \mathbb{R} \) be given, with values in \( \left\lbrack {0,1}\right\rbrack ,1 \) -periodic and satisfying:

\[
\left\{  {\begin{array}{l} \forall t \in  \left\lbrack  {\frac{1}{10},\frac{2}{10}}\right\rbrack  , f\left( t\right)  = g\left( t\right)  = 0 \\  \forall t \in  \left\lbrack  {\frac{3}{10},\frac{4}{10}}\right\rbrack  , f\left( t\right)  = 0, g\left( t\right)  = 1 \end{array}\;\left\{  \begin{array}{l} \forall t \in  \left\lbrack  {\frac{5}{10},\frac{6}{10}}\right\rbrack  , f\left( t\right)  = 1, g\left( t\right)  = 0 \\  \forall t \in  \left\lbrack  {\frac{7}{10},\frac{8}{10}}\right\rbrack  , f\left( t\right)  = g\left( t\right)  = 1 \end{array}\right. }\right.
\]

(voir la figure ci-dessous).

> (see the figure below).

![bo_d7fjkrs91nqc73ereoog_116_218_791_943_300_0.jpg](images/gourdon_analysis_fr_en_007_bod7fjkrs91nqc73ereoog1162187919433000.jpg)

De telles fonctions \( f \) et \( g \) existent bien, il suffit par exemple de relier les extrémités des segments en gras sur la figure par des segments de droite.

> Such functions \( f \) and \( g \) do indeed exist; it suffices, for example, to connect the ends of the bold segments in the figure with straight line segments.

On considère ensuite les fonctions

> We then consider the functions

\[
\alpha  : \mathbb{R} \rightarrow  \mathbb{R}\;t \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{f\left( {{10}^{n - 1}t}\right) }{{2}^{n}},\;\beta  : \mathbb{R} \rightarrow  \mathbb{R}\;t \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{g\left( {{10}^{n - 1}t}\right) }{{2}^{n}}
\]

et

\[
F : \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathbb{R}}^{2}\;t \mapsto  \left( {\alpha \left( t\right) ,\beta \left( t\right) }\right) .
\]

a) Montrer l’existence et la continuité de \( F \) .

> a) Show the existence and continuity of \( F \) .

b) Montrer que \( F \) est une surjection de \( \left\lbrack {0,1}\right\rbrack \) sur \( {\left\lbrack 0,1\right\rbrack }^{2} \) (autrement dit, le graphe de \( F \) remplit totalement le carré \( {\left\lbrack 0,1\right\rbrack }^{2} \) ).

> b) Show that \( F \) is a surjection from \( \left\lbrack {0,1}\right\rbrack \) onto \( {\left\lbrack 0,1\right\rbrack }^{2} \) (in other words, the graph of \( F \) completely fills the square \( {\left\lbrack 0,1\right\rbrack }^{2} \) ).

c) Existe-t-il une fonction \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathbb{R}}^{2} \) de classe \( {\mathcal{C}}^{1} \) et vérifiant la propriété de la question b) ?

> c) Does there exist a function \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathbb{R}}^{2} \) of class \( {\mathcal{C}}^{1} \) satisfying the property in question b)?

d) Existe-t-il une fonction \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathbb{R}}^{2} \) continue et bijective de \( \left\lbrack {0,1}\right\rbrack \) sur \( {\left\lbrack 0,1\right\rbrack }^{2} \) ?

> d) Does there exist a continuous and bijective function \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\mathbb{R}}^{2} \) from \( \left\lbrack {0,1}\right\rbrack \) onto \( {\left\lbrack 0,1\right\rbrack }^{2} \) ?

Solution. a) La fonction \( f \) est à valeurs dans \( \left\lbrack {0,1}\right\rbrack \) , donc

> Solution. a) The function \( f \) takes values in \( \left\lbrack {0,1}\right\rbrack \) , therefore

\[
\forall n \in  {\mathbb{N}}^{ * },\forall t \in  \mathbb{R},\;\left| \frac{f\left( {{10}^{n - 1}t}\right) }{{2}^{n}}\right|  \leq  \frac{1}{{2}^{n}}.
\]

Ainsi, la série de fonction \( \mathop{\sum }\limits_{{n > 1}}f\left( {{10}^{n - 1}t}\right) /{2}^{n} \) converge normalement sur \( \mathbb{R} \) , d’où l’existence et la continuité de \( \alpha \) . On procéderait de même pour \( \beta \) .

> Thus, the series of functions \( \mathop{\sum }\limits_{{n > 1}}f\left( {{10}^{n - 1}t}\right) /{2}^{n} \) converges normally on \( \mathbb{R} \) , hence the existence and continuity of \( \alpha \) . We would proceed similarly for \( \beta \) .

b) Commençons par considérer \( t \in \lbrack 0,1\lbrack \) , et écrivons sa décomposition décimale :

> b) Let us begin by considering \( t \in \lbrack 0,1\lbrack \) , and write its decimal expansion:

\[
t = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{t}_{n}}{{10}^{n}},\;\left( {{t}_{n} \in  \{ 0,1,\ldots ,9\} \;\forall n \in  {\mathbb{N}}^{ * }}\right)
\]

de sorte que

> so that

\[
\forall n \in  {\mathbb{N}}^{ * },\;{10}^{n - 1}t = {N}_{n} + \frac{{t}_{n}}{10} + {R}_{n}\;\text{ avec }\;{N}_{n} \in  \mathbb{N}\text{ et }{R}_{n} = \mathop{\sum }\limits_{{i = n + 1}}^{{+\infty }}\frac{{t}_{i}}{{10}^{i + 1 - n}} \in  \left\lbrack  {0,\frac{1}{10}\lbrack }\right.
\]

(cette dernière assertion est vraie car les \( {t}_{n} \) ne sont jamais stationnaires à 9 à partir d'un certain rang) donc, les fonctions \( f \) et \( g \) étant 1-périodiques,

> (this last assertion is true because the \( {t}_{n} \) are never stationary at 9 from a certain rank) therefore, the functions \( f \) and \( g \) being 1-periodic,

\[
\forall n \in  {\mathbb{N}}^{ * },\;\left\{  {\begin{array}{l} {2}^{-n}f\left( {{10}^{n - 1}t}\right)  = {2}^{-n}f\left( {\frac{{t}_{n}}{10} + {R}_{n}}\right) \\  {2}^{-n}g\left( {{10}^{n - 1}t}\right)  = {2}^{-n}g\left( {\frac{{t}_{n}}{10} + {R}_{n}}\right)  \end{array}\;\text{ avec }\;{R}_{n} \in  \left\lbrack  {0,\frac{1}{10}\lbrack .}\right. }\right.
\]

(*)

> Ceci étant, donnons nous \( \left( {x, y}\right) \in {\left\lbrack 0,1\right\rbrack }^{2} \) et écrivons la décomposition diadique de \( x \) et \( y \) :

Given this, let us take \( \left( {x, y}\right) \in {\left\lbrack 0,1\right\rbrack }^{2} \) and write the dyadic expansion of \( x \) and \( y \) :

\[
x = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{x}_{k}}{{2}^{k}},\;y = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{y}_{k}}{{2}^{k}},\;\left( {{x}_{k},{y}_{k} \in  \{ 0,1\} }\right) .
\]

Si \( x = 1 \) on choisit \( {x}_{k} = 1 \) pour tout \( k \) , de même pour \( y \) . Nous allons construire \( t \in \lbrack 0,1\lbrack \) à partir de sa décomposition décimale pour avoir \( f\left( {{10}^{k - 1}t}\right) = {x}_{k} \) et \( g\left( {{10}^{k - 1}t}\right) = {y}_{k} \) pour tout \( k \) , ce qui montrera que \( F\left( t\right) = \left( {x, y}\right) \) . Soit \( k \in {\mathbb{N}}^{ * } \) ,

> If \( x = 1 \) we choose \( {x}_{k} = 1 \) for all \( k \) , likewise for \( y \) . We will construct \( t \in \lbrack 0,1\lbrack \) from its decimal expansion to have \( f\left( {{10}^{k - 1}t}\right) = {x}_{k} \) and \( g\left( {{10}^{k - 1}t}\right) = {y}_{k} \) for all \( k \) , which will show that \( F\left( t\right) = \left( {x, y}\right) \) . Let \( k \in {\mathbb{N}}^{ * } \) ,

- si \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {0,0}\right) \) , on choisit \( {t}_{k} = 1 \) ;

> - if \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {0,0}\right) \) , we choose \( {t}_{k} = 1 \) ;

- si \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {0,1}\right) \) , on choisit \( {t}_{k} = 3 \) ;

> - if \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {0,1}\right) \) , we choose \( {t}_{k} = 3 \) ;

- si \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {1,0}\right) \) , on choisit \( {t}_{k} = 5 \) ;

> - if \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {1,0}\right) \) , we choose \( {t}_{k} = 5 \) ;

- si \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {1,1}\right) \) , on choisit \( {t}_{k} = 7 \) .

> - if \( \left( {{x}_{k},{y}_{k}}\right)  = \left( {1,1}\right) \) , we choose \( {t}_{k} = 7 \) .

L’écriture \( t = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{t}_{k}/{10}^{k} \) est bien un développement décimal, et \( t \) vérifie la propriété requise d’après (*) et d’après la forme des fonctions \( f \) et \( g \) . Nous venons donc de prouver que \( {\left\lbrack 0,1\right\rbrack }^{2} \subset \; F\left( \left\lbrack {0,1}\right\rbrack \right) \) . L’inclusion réciproque est immédiate, donc finalement, \( F\left( \left\lbrack {0,1}\right\rbrack \right) = {\left\lbrack 0,1\right\rbrack }^{2} \) .

> The expression \( t = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{t}_{k}/{10}^{k} \) is indeed a decimal expansion, and \( t \) satisfies the required property according to (*) and the form of the functions \( f \) and \( g \) . We have thus just proven that \( {\left\lbrack 0,1\right\rbrack }^{2} \subset \; F\left( \left\lbrack {0,1}\right\rbrack \right) \) . The reverse inclusion is immediate, so finally, \( F\left( \left\lbrack {0,1}\right\rbrack \right) = {\left\lbrack 0,1\right\rbrack }^{2} \) .

c) Non ! Raisonnons par l'absurde en supposant qu'une telle fonction existe. Nous allons re-couvrir \( F\left( \left\lbrack {0,1}\right\rbrack \right) \) par une surface dont l’aire est inférieure à celle du carré \( {\left\lbrack 0,1\right\rbrack }^{2} \) , d’où découlera l'absurdité désirée.

> c) No! Let us reason by contradiction by assuming that such a function exists. We will cover \( F\left( \left\lbrack {0,1}\right\rbrack \right) \) with a surface whose area is less than that of the square \( {\left\lbrack 0,1\right\rbrack }^{2} \) , from which the desired absurdity will follow.

On note \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}\begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \) (où \( \parallel \) . \( \parallel \) désigne la norme du sup : \( \parallel \left( {x, y}\right) \parallel = \sup \{ \left| x\right| ,\left| y\right| \} \) ). On considère un entier naturel non nul quelconque \( n \) et la subdivision \( 0 < \frac{1}{n} < \cdots < \frac{n - 1}{n} < 1 \) de \( \left\lbrack {0,1}\right\rbrack \) . Pour tout entier \( k,0 \leq k \leq n - 1 \) , on a d’après l’inégalité des accroissements finis

> Let \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}\begin{Vmatrix}{{F}^{\prime }\left( t\right) }\end{Vmatrix} \) be denoted (where \( \parallel \) . \( \parallel \) denotes the sup norm: \( \parallel \left( {x, y}\right) \parallel = \sup \{ \left| x\right| ,\left| y\right| \} \) ). Consider any non-zero natural number \( n \) and the subdivision \( 0 < \frac{1}{n} < \cdots < \frac{n - 1}{n} < 1 \) of \( \left\lbrack {0,1}\right\rbrack \) . For any integer \( k,0 \leq k \leq n - 1 \) , we have according to the mean value inequality

\[
\forall t \in  \left\lbrack  {\frac{k}{n},\frac{k + 1}{n}}\right\rbrack  ,\;\begin{Vmatrix}{F\left( t\right)  - F\left( \frac{k + \frac{1}{2}}{n}\right) }\end{Vmatrix} \leq  M\left| {t - \frac{k + \frac{1}{2}}{n}}\right|  \leq  \frac{M}{2n}.
\]

Ainsi, \( F\left( \left\lbrack {\frac{k}{n},\frac{k + 1}{n}}\right\rbrack \right) \) est inclus dans le carré de centre \( F\left( \frac{k + \frac{1}{2}}{n}\right) \) de demi-côté \( \frac{M}{2n} \) , que nous noterons \( {C}_{n, k} \) . On a donc

> Thus, \( F\left( \left\lbrack {\frac{k}{n},\frac{k + 1}{n}}\right\rbrack \right) \) is included in the square centered at \( F\left( \frac{k + \frac{1}{2}}{n}\right) \) with half-side \( \frac{M}{2n} \) , which we will denote as \( {C}_{n, k} \) . We therefore have

\[
F\left( \left\lbrack  {0,1}\right\rbrack  \right)  = \mathop{\bigcup }\limits_{{k = 0}}^{{n - 1}}F\left( \left\lbrack  {\frac{k}{n},\frac{k + 1}{n}}\right\rbrack  \right)  \subset  \mathop{\bigcup }\limits_{{k = 0}}^{{n - 1}}{C}_{n, k} = {S}_{n}.
\]

L’aire \( \mathcal{A}\left( {S}_{n}\right) \) de \( {S}_{n} \) est inférieure à la somme des aires des carrés \( {C}_{n, k} \) , ce qui s’écrit

> The area \( \mathcal{A}\left( {S}_{n}\right) \) of \( {S}_{n} \) is less than the sum of the areas of the squares \( {C}_{n, k} \) , which is written

\[
\mathcal{A}\left( {S}_{n}\right)  \leq  \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\mathcal{A}\left( {C}_{n, k}\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{\left( \frac{M}{n}\right) }^{2} = \frac{{M}^{2}}{n}.
\]

On choisit maintenant \( n \) tel que \( n > {M}^{2} \) . Alors \( \mathcal{A}\left( {S}_{n}\right) < 1 \) , donc \( {\left\lbrack 0,1\right\rbrack }^{2} \text{ ⊄ } {S}_{n} \) , et comme \( F\left( \left\lbrack {0,1}\right\rbrack \right) \subset {S}_{n} \) on en déduit \( {\left\lbrack 0,1\right\rbrack }^{2} \text{ ⊄ } F\left( \left\lbrack {0,1}\right\rbrack \right) \) . Ceci est impossible, d’où le résultat.

> We now choose \( n \) such that \( n > {M}^{2} \) . Then \( \mathcal{A}\left( {S}_{n}\right) < 1 \) , so \( {\left\lbrack 0,1\right\rbrack }^{2} \text{ ⊄ } {S}_{n} \) , and since \( F\left( \left\lbrack {0,1}\right\rbrack \right) \subset {S}_{n} \) we deduce \( {\left\lbrack 0,1\right\rbrack }^{2} \text{ ⊄ } F\left( \left\lbrack {0,1}\right\rbrack \right) \) . This is impossible, hence the result.

d) C'est dans un cadre légèrement différent la même chose que l'exercice 8 page 47. On raisonne par l’absurde en supposant qu’une telle bijection \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\left\lbrack 0,1\right\rbrack }^{2} \) existe. L’application \( F \) est continue sur un compact, son application réciproque \( {F}^{-1} : {\left\lbrack 0,1\right\rbrack }^{2} \rightarrow \left\lbrack {0,1}\right\rbrack \) est donc continue (voir la proposition 14 page 31). Donnons nous un point quelconque \( c \) dans ]0,1[. L’ensemble

> d) In a slightly different context, this is the same as exercise 8 on page 47. We reason by contradiction by assuming that such a bijection \( F : \left\lbrack {0,1}\right\rbrack \rightarrow {\left\lbrack 0,1\right\rbrack }^{2} \) exists. The map \( F \) is continuous on a compact set, so its inverse map \( {F}^{-1} : {\left\lbrack 0,1\right\rbrack }^{2} \rightarrow \left\lbrack {0,1}\right\rbrack \) is therefore continuous (see proposition 14 on page 31). Let us take any point \( c \) in ]0,1[. The set

\( {\left\lbrack 0,1\right\rbrack }^{2} \smallsetminus \{ F\left( c\right) \} \) est connexe (car connexe par arcs comme on le vérifie facilement), donc \( {F}^{-1} \) étant continue, \( {F}^{-1}\left( {{\left\lbrack 0,1\right\rbrack }^{2}\smallsetminus \{ F\left( c\right) \} }\right) \) est connexe. On a affaire à une bijection, donc

> \( {\left\lbrack 0,1\right\rbrack }^{2} \smallsetminus \{ F\left( c\right) \} \) is connected (as it is path-connected, as can be easily verified), so \( {F}^{-1} \) being continuous, \( {F}^{-1}\left( {{\left\lbrack 0,1\right\rbrack }^{2}\smallsetminus \{ F\left( c\right) \} }\right) \) is connected. We are dealing with a bijection, so

\[
{F}^{-1}\left( {{\left\lbrack  0,1\right\rbrack  }^{2}\smallsetminus \{ F\left( c\right) \} }\right)  = {F}^{-1}\left( {\left\lbrack  0,1\right\rbrack  }^{2}\right)  \smallsetminus  \{ c\}  = \left\lbrack  {0,1}\right\rbrack   \smallsetminus  \{ c\}  = \left\lbrack  {0, c\left\lbrack  \cup \right\rbrack  c,1}\right\rbrack  ,
\]

qui n'est pas connexe ! Ceci est absurde, d'où le résultat.

> which is not connected! This is absurd, hence the result.

Problem 11 (FONCTION DE WEIERSTRASS). On définit une application \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) par

> Problem 11 (WEIERSTRASS FUNCTION). We define a map \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) by

\[
f\left( x\right)  = \frac{1}{q}\;\text{ si }\;x = \frac{p}{q} \in  \mathbb{Q}\;\left( {p \in  \mathbb{N}, q \in  {\mathbb{N}}^{ * }, p \land  q = 1}\right) ,
\]

(fonction introduite par Weierstrass).

> (function introduced by Weierstrass).

a) Déterminer l’ensemble des points où \( f \) est continue.

> a) Determine the set of points where \( f \) is continuous.

b) Montrer que \( f \) est une fonction réglée.

> b) Show that \( f \) is a regulated function.

Solution. a) Nous allons montrer que cette étrange fonction est discontinue en tout point rationnel et continue en tout point irrationnel.

> Solution. a) We will show that this strange function is discontinuous at every rational point and continuous at every irrational point.

Soit \( x \in \left\lbrack {0,1}\right\rbrack \) un rationnel et supposons (on raisonne par l’absurde) que \( f \) soit continue en \( x \) . Comme les irrationnels sont denses dans \( \mathbb{R} \) , il existe une suite \( \left( {x}_{n}\right) \) de points irrationnels de \( \left\lbrack {0,1}\right\rbrack \) qui converge vers \( x \) . On a alors \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) \) , ce qui est impossible car \( f\left( x\right) \neq 0 \) et \( f\left( {x}_{n}\right) = 0 \) pour tout \( n \) . Ainsi, \( f \) est discontinue en tout point rationnel de \( \left\lbrack {0,1}\right\rbrack \) .

> Let \( x \in \left\lbrack {0,1}\right\rbrack \) be a rational number and assume (reasoning by contradiction) that \( f \) is continuous at \( x \) . Since the irrationals are dense in \( \mathbb{R} \) , there exists a sequence \( \left( {x}_{n}\right) \) of irrational points in \( \left\lbrack {0,1}\right\rbrack \) that converges to \( x \) . We then have \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) \) , which is impossible because \( f\left( x\right) \neq 0 \) and \( f\left( {x}_{n}\right) = 0 \) for all \( n \) . Thus, \( f \) is discontinuous at every rational point in \( \left\lbrack {0,1}\right\rbrack \) .

Soit \( x \in \left\lbrack {0,1}\right\rbrack \) un irrationnel. Nous allons montrer la continuité de \( f \) en \( x \) . Donnons nous \( \varepsilon > 0 \) et fixons un entier naturel non nul \( N \) tel que \( 1/N < \varepsilon \) . L’ensemble \( \Gamma \) des rationnels de \( \left\lbrack {0,1}\right\rbrack \) qui peuvent s’écrire sous la forme \( p/q \) avec \( p \in \mathbb{N}, q \in {\mathbb{N}}^{ * } \) et \( q < N \) est fini. Comme de plus \( x \notin \Gamma \) , le réel \( \alpha = \mathop{\inf }\limits_{{y \in \Gamma }}\left| {x - y}\right| \) est non nul. Considérons maintenant un élément quelconque \( y \in \left\lbrack {0,1}\right\rbrack \) tel que \( \left| {x - y}\right| < \alpha \) . Si \( y \) est irrationnel, on a \( f\left( y\right) = 0 \) donc \( \left| {f\left( x\right) - f\left( y\right) }\right| < \varepsilon \) . Si \( y = p/q \) est rationnel, on a \( q \geq N \) car \( y \notin \Gamma \) par construction de \( \alpha \) , donc \( \left| {f\left( x\right) - f\left( y\right) }\right| = 1/q < \varepsilon \) . Ainsi,

> Let \( x \in \left\lbrack {0,1}\right\rbrack \) be an irrational number. We will show the continuity of \( f \) at \( x \) . Let \( \varepsilon > 0 \) be given and fix a non-zero natural number \( N \) such that \( 1/N < \varepsilon \) . The set \( \Gamma \) of rationals in \( \left\lbrack {0,1}\right\rbrack \) that can be written in the form \( p/q \) with \( p \in \mathbb{N}, q \in {\mathbb{N}}^{ * } \) and \( q < N \) is finite. Since, moreover, \( x \notin \Gamma \) , the real number \( \alpha = \mathop{\inf }\limits_{{y \in \Gamma }}\left| {x - y}\right| \) is non-zero. Now consider any element \( y \in \left\lbrack {0,1}\right\rbrack \) such that \( \left| {x - y}\right| < \alpha \) . If \( y \) is irrational, we have \( f\left( y\right) = 0 \) so \( \left| {f\left( x\right) - f\left( y\right) }\right| < \varepsilon \) . If \( y = p/q \) is rational, we have \( q \geq N \) because \( y \notin \Gamma \) by construction of \( \alpha \) , so \( \left| {f\left( x\right) - f\left( y\right) }\right| = 1/q < \varepsilon \) . Thus,

\[
\forall y \in  \left\lbrack  {0,1}\right\rbrack  ,\left| {x - y}\right|  < \alpha ,\;\left| {f\left( x\right)  - f\left( y\right) }\right|  < \varepsilon ,
\]

ce qui prouve bien la continuité de \( f \) en \( x \) .

> which indeed proves the continuity of \( f \) at \( x \) .

b) Il s’agit de construire une suite de fonctions en escaliers \( {\left( {\varphi }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) qui converge uniformément vers \( f \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on définit \( {\varphi }_{n} : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) par

> b) The goal is to construct a sequence of step functions \( {\left( {\varphi }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) that converges uniformly to \( f \) . For all \( n \in {\mathbb{N}}^{ * } \) , we define \( {\varphi }_{n} : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) by

\[
\left\{  \begin{array}{ll} {\varphi }_{n}\left( x\right)  = f\left( x\right) & \text{ si }\exists \left( {p, q}\right)  \in  \mathbb{N} \times  {\mathbb{N}}^{ * }, p \land  q = 1, q \leq  n,\;x = p/q, \\  {\varphi }_{n}\left( x\right)  = 0 & \text{ sinon. } \end{array}\right.
\]

Pour tout \( n,{\varphi }_{n} \) est nulle partout sauf en un nombre fini de points, c’est donc une fonction en escalier. Par ailleurs, on a

> For all \( n,{\varphi }_{n} \) is zero everywhere except at a finite number of points, it is therefore a step function. Furthermore, we have

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;\left| {f\left( x\right)  - {\varphi }_{n}\left( x\right) }\right|  < \frac{1}{n}.
\]

En effet,

> Indeed,

- si \( x \in  \mathbb{R} \smallsetminus  \mathbb{Q},{\varphi }_{n}\left( x\right)  = f\left( x\right)  = 0 \) ,

> - if \( x \in  \mathbb{R} \smallsetminus  \mathbb{Q},{\varphi }_{n}\left( x\right)  = f\left( x\right)  = 0 \) ,

- si \( x = p/q \) avec \( p \land  q = 1 \) et \( q \leq  n \) , on a \( {\varphi }_{n}\left( x\right)  = f\left( x\right) \) ,

> - if \( x = p/q \) with \( p \land  q = 1 \) and \( q \leq  n \) , we have \( {\varphi }_{n}\left( x\right)  = f\left( x\right) \) ,

- si \( x = p/q \) avec \( p \land  q = 1 \) et \( q > n \) , on a \( {\varphi }_{n}\left( x\right)  = 0 \) et \( f\left( x\right)  = 1/q < 1/n \) .

> - if \( x = p/q \) with \( p \land  q = 1 \) and \( q > n \) , we have \( {\varphi }_{n}\left( x\right)  = 0 \) and \( f\left( x\right)  = 1/q < 1/n \) .

Ainsi, la suite de fonctions en escaliers \( \left( {\varphi }_{n}\right) \) converge uniformément vers \( f \) , donc \( f \) est une fonction réglée.

> Thus, the sequence of step functions \( \left( {\varphi }_{n}\right) \) converges uniformly to \( f \) , so \( f \) is a regulated function.

Remarque. Comme \( f \) est réglée, elle vérifie les assertions du théorème 4 de la page 99, ce qui entraîne que l'ensemble des points de discontinuité de \( f \) est au plus dénombrable. Ceci est en accord avec le résultat de la question a).

> Remark. Since \( f \) is regulated, it satisfies the assertions of theorem 4 on page 99, which implies that the set of discontinuity points of \( f \) is at most countable. This is in agreement with the result of question a).

- On peut prouver (en utilisant le théorème de Baire décrit dans l'annexe A) qu'il n'existe pas de fonction continue en tout point de \( \mathbb{Q} \) et discontinue en tout point de \( \mathbb{R} \smallsetminus  \mathbb{Q} \) .

> - One can prove (using the Baire category theorem described in appendix A) that there exists no function continuous at every point of \( \mathbb{Q} \) and discontinuous at every point of \( \mathbb{R} \smallsetminus  \mathbb{Q} \) .

Problem 12 (FONCTIONS POSITIVEMENT HOMOGENES). La lettre \( E \) désigne un \( \mathbb{R} \) - espace vectoriel. Une application \( f : E \rightarrow \mathbb{R} \) est dite positivement homogène de degré \( \alpha \) (avec \( \alpha > 0 \) ) si

> Problem 12 (POSITIVELY HOMOGENEOUS FUNCTIONS). The letter \( E \) denotes a \( \mathbb{R} \) - vector space. A mapping \( f : E \rightarrow \mathbb{R} \) is said to be positively homogeneous of degree \( \alpha \) (with \( \alpha > 0 \) ) if

\[
\forall x \in  E,\forall \lambda  \in  {\mathbb{R}}^{ + },\;f\left( {\lambda x}\right)  = {\lambda }^{\alpha }f\left( x\right) .
\]

Une application \( g : E \rightarrow \mathbb{R} \) est dite convexe si

> A mapping \( g : E \rightarrow \mathbb{R} \) is said to be convex if

\[
\forall x, y \in  E,\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;g\left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right)  \leq  {\lambda g}\left( x\right)  + \left( {1 - \lambda }\right) g\left( y\right) .
\]

On rappelle qu’une semi-norme sur \( E \) est une application \( N \) de \( E \) dans \( {\mathbb{R}}^{ + } \) qui vérifie les propriétés d’une norme sauf la propriété \( \left( {N\left( x\right) = 0 \Leftrightarrow x = 0}\right) \) (voir la remarque 1 page 8). On s'intéressera ici aux fonctions positivement homogènes de degré 1.

> Recall that a seminorm on \( E \) is a mapping \( N \) from \( E \) to \( {\mathbb{R}}^{ + } \) that satisfies the properties of a norm except for property \( \left( {N\left( x\right) = 0 \Leftrightarrow x = 0}\right) \) (see remark 1 on page 8). We will focus here on positively homogeneous functions of degree 1.

1 / Soit \( f : E \rightarrow \mathbb{R} \) une fonction positivement homogène de degré 1.

> 1 / Let \( f : E \rightarrow \mathbb{R} \) be a positively homogeneous function of degree 1.

a) Montrer que \( f \) est convexe sur \( E \) si et seulement si

> a) Show that \( f \) is convex on \( E \) if and only if

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;f\left( {x + y}\right)  \leq  f\left( x\right)  + f\left( y\right) .
\]

b) Si \( f \) est à valeurs positives, montrer que \( f \) est convexe sur \( E \) si et seulement si l’ensemble \( C = \{ x \in E \mid f\left( x\right) \leq 1\} \) est convexe.

> b) If \( f \) is positive-valued, show that \( f \) is convex on \( E \) if and only if the set \( C = \{ x \in E \mid f\left( x\right) \leq 1\} \) is convex.

c) Si \( f \) est convexe,à valeurs positives et si elle est paire, montrer que \( f \) est une semi-norme.

> c) If \( f \) is convex, positive-valued, and even, show that \( f \) is a seminorm.

d) On suppose ici que \( E \) est de dimension finie. Soit \( \Omega \) un ouvert borné non vide de \( E \) . Montrer qu’il existe une norme \( N \) sur \( E \) telle que \( \Omega = {\mathrm{B}}_{N}\left( {0,1}\right) = \{ x \in E \mid N\left( x\right) < 1\} \) si et seulement si \( \Omega \) est convexe et admet 0 comme centre de symétrie.

> d) We assume here that \( E \) is finite-dimensional. Let \( \Omega \) be a non-empty bounded open set of \( E \). Show that there exists a norm \( N \) on \( E \) such that \( \Omega = {\mathrm{B}}_{N}\left( {0,1}\right) = \{ x \in E \mid N\left( x\right) < 1\} \) if and only if \( \Omega \) is convex and admits 0 as a center of symmetry.

2/ (Étude de normes particulières.) Soit un réel \( \alpha \geq 1 \) . Montrer, sans utiliser l’inégalité de Minkowsky, que l'application

> 2/ (Study of particular norms.) Let \( \alpha \geq 1 \) be a real number. Show, without using Minkowski's inequality, that the mapping

\[
{N}_{\alpha } : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{ + }\;\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  {\left( {\left| {x}_{1}\right| }^{\alpha } + \cdots  + {\left| {x}_{n}\right| }^{\alpha }\right) }^{1/\alpha }
\]

définit une norme sur \( {\mathbb{R}}^{n} \) .

> defines a norm on \( {\mathbb{R}}^{n} \) .

Solution. 1/ a) Condition nécessaire. Si \( f \) est convexe sur \( E \) , alors

> Solution. 1/ a) Necessary condition. If \( f \) is convex on \( E \) , then

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\frac{1}{2}f\left( {x + y}\right)  = f\left( \frac{x + y}{2}\right)  \leq  \frac{1}{2}\left( {f\left( x\right)  + f\left( y\right) }\right) \;\text{ donc }\;f\left( {x + y}\right)  \leq  f\left( x\right)  + f\left( y\right) .
\]

Condition suffisante. Il suffit d’écrire que pour \( \left( {x, y}\right) \in {E}^{2} \) et \( \lambda \in \left\lbrack {0,1}\right\rbrack \) , on a

> Sufficient condition. It suffices to write that for \( \left( {x, y}\right) \in {E}^{2} \) and \( \lambda \in \left\lbrack {0,1}\right\rbrack \) , we have

\[
f\left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right)  \leq  f\left( {\lambda x}\right)  + f\left( {\left( {1 - \lambda }\right) y}\right)  = {\lambda f}\left( x\right)  + \left( {1 - \lambda }\right) f\left( y\right) .
\]

b) Condition nécessaire. Si \( f \) est convexe, alors pour tout \( \left( {x, y}\right) \in {C}^{2} \) et pour tout \( \lambda \in \left\lbrack {0,1}\right\rbrack \) ,

> b) Necessary condition. If \( f \) is convex, then for all \( \left( {x, y}\right) \in {C}^{2} \) and for all \( \lambda \in \left\lbrack {0,1}\right\rbrack \) ,

\[
f\left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right)  \leq  {\lambda f}\left( x\right)  + \left( {1 - \lambda }\right) f\left( y\right)  \leq  \lambda  + \left( {1 - \lambda }\right)  = 1,\;\text{ donc }\;{\lambda x} + \left( {1 - \lambda }\right) y \in  C.
\]

Condition suffisante. C’est un peu plus délicat. Soit \( \left( {x, y}\right) \in {E}^{2} \) . Pour tout \( \varepsilon > 0 \) , on a

> Sufficient condition. This is a bit more delicate. Let \( \left( {x, y}\right) \in {E}^{2} \) . For all \( \varepsilon > 0 \) , we have

\[
\frac{x}{f\left( x\right)  + \varepsilon },\frac{y}{f\left( y\right)  + \varepsilon } \in  C\;\operatorname{car}f\left( \frac{x}{f\left( x\right)  + \varepsilon }\right)  = \frac{1}{f\left( x\right)  + \varepsilon }f\left( x\right)  < 1\;\text{ (de même pour }y\text{ ) }
\]

(le paramètre \( \varepsilon \) a été introduit pour éviter de diviser par 0) donc \( C \) étant convexe par hypothèse,

> (the parameter \( \varepsilon \) was introduced to avoid division by 0) therefore, since \( C \) is convex by hypothesis,

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;f\left( {\frac{\lambda x}{f\left( x\right)  + \varepsilon } + \frac{\left( {1 - \lambda }\right) y}{f\left( y\right)  + \varepsilon }}\right)  \leq  1.
\]

(*)

> Si on choisit \( \lambda \) tel que

If we choose \( \lambda \) such that

\[
\frac{\lambda }{f\left( x\right)  + \varepsilon } = \frac{\left( 1 - \lambda \right) }{f\left( y\right)  + \varepsilon }\;\left( {\text{ c’est-à-dire }\lambda  = \frac{f\left( x\right)  + \varepsilon }{f\left( x\right)  + f\left( y\right)  + {2\varepsilon }} \in  \left\lbrack  {0,1}\right\rbrack  }\right) ,
\]

on obtient en remplaçant dans (*)

> we obtain by substituting into (*)

\[
f\left( \frac{x + y}{f\left( x\right)  + f\left( y\right)  + {2\varepsilon }}\right)  \leq  1\;\text{ donc }\;f\left( {x + y}\right)  \leq  f\left( x\right)  + f\left( y\right)  + {2\varepsilon }.
\]

Ceci dernier résultat est vrai pour tout \( \varepsilon > 0 \) , donc \( f\left( {x + y}\right) \leq f\left( x\right) + f\left( y\right) \) . On en conclut maintenant avec a) que \( f \) est convexe.

> This last result is true for all \( \varepsilon > 0 \) , so \( f\left( {x + y}\right) \leq f\left( x\right) + f\left( y\right) \) . We now conclude with a) that \( f \) is convex.

c) Comme \( f \) est convexe, l’inégalité triangulaire est vérifiée d’après le résultat de la question a). Il faut maintenant montrer que pour tout \( x \in E \) et pour tout \( \lambda \in \mathbb{R}, f\left( {\lambda x}\right) = \left| \lambda \right| f\left( x\right) \) . Si \( \lambda \geq 0 \) , ceci résulte du fait que \( f \) est positivement homogène de degré 1. Si \( \lambda < 0 \) , ceci est une conséquence de l'hypothèse de parité vérifiée par \( f \) car

> c) Since \( f \) is convex, the triangle inequality is satisfied according to the result of question a). We must now show that for all \( x \in E \) and for all \( \lambda \in \mathbb{R}, f\left( {\lambda x}\right) = \left| \lambda \right| f\left( x\right) \) . If \( \lambda \geq 0 \) , this follows from the fact that \( f \) is positively homogeneous of degree 1. If \( \lambda < 0 \) , this is a consequence of the parity hypothesis satisfied by \( f \) because

\[
f\left( {\lambda x}\right)  = f\left( {\left( {-\lambda }\right) x}\right)  = \left( {-\lambda }\right) f\left( x\right)  = \left| \lambda \right| f\left( x\right) .
\]

d) Condition nécessaire. Une norme est une fonction positivement homogène de degré 1, est convexe d'après a) car elle vérifie l'inégalité triangulaire, et est de plus à valeurs positives. On en conclut grâce à b) que \( C = \overline{{\mathrm{B}}_{N}\left( {0,1}\right) } \) est convexe. L’intérieur d’un convexe est convexe, donc \( \overset{ \circ }{C} = \Omega \) est convexe. La symétrie de \( \Omega \) par rapport à 0 est immédiate puisque

> d) Necessary condition. A norm is a positively homogeneous function of degree 1, is convex according to a) because it satisfies the triangle inequality, and is furthermore positive-valued. We conclude thanks to b) that \( C = \overline{{\mathrm{B}}_{N}\left( {0,1}\right) } \) is convex. The interior of a convex set is convex, so \( \overset{ \circ }{C} = \Omega \) is convex. The symmetry of \( \Omega \) with respect to 0 is immediate since

\[
\forall x \in  \Omega ,\;N\left( {-x}\right)  = N\left( x\right)  < 1\;\text{ donc }\; - x \in  \Omega .
\]

Condition suffisante. Commençons par définir \( N \) . On pose \( N\left( 0\right) = 0 \) . Soit \( x \in E, x \neq 0 \) . Nous allons définir \( N\left( x\right) \) comme étant égal à \( 1/{\mu }_{x} \) , où \( {\mu }_{x} > 0 \) est tel que \( {\mu }_{x}x \) appartient à la frontière de \( \Omega \) (ceci car \( N\left( {{\mu }_{x}x}\right) = 1 \) ) - voir la figure ci-contre.

> Sufficient condition. Let us begin by defining \( N \) . We set \( N\left( 0\right) = 0 \) . Let \( x \in E, x \neq 0 \) . We will define \( N\left( x\right) \) as being equal to \( 1/{\mu }_{x} \) , where \( {\mu }_{x} > 0 \) is such that \( {\mu }_{x}x \) belongs to the boundary of \( \Omega \) (this is because \( N\left( {{\mu }_{x}x}\right) = 1 \) ) - see the figure opposite.

![bo_d7fjkrs91nqc73ereoog_120_653_861_300_350_0.jpg](images/gourdon_analysis_fr_en_008_bod7fjkrs91nqc73ereoog1206538613003500.jpg)

Figure 10. L’ensemble \( \Omega \) et la construction de \( {\mu }_{x} \) pour un \( x \) donné.

> Figure 10. The set \( \Omega \) and the construction of \( {\mu }_{x} \) for a given \( x \) .

On pose \( {\Gamma }_{x} = \{ \lambda > 0 \mid {\lambda x} \in \overline{\Omega }\} \) . Comme \( \Omega \) est ouvert et contient 0 (il est non vide, symétrique par rapport à 0 et convexe), \( {\Gamma }_{x} \) est non vide. De plus, \( \Omega \) est borné donc \( {\Gamma }_{x} \) est majoré. Ainsi, \( {\mu }_{x} = \sup {\Gamma }_{x} \) est bien défini, et on pose \( N\left( x\right) = 1/{\mu }_{x} \) . Remarquons que \( \overline{\Omega } \) étant fermé, on a \( {\mu }_{x} \in {\Gamma }_{x} \) .

> We set \( {\Gamma }_{x} = \{ \lambda > 0 \mid {\lambda x} \in \overline{\Omega }\} \) . Since \( \Omega \) is open and contains 0 (it is non-empty, symmetric with respect to 0, and convex), \( {\Gamma }_{x} \) is non-empty. Furthermore, \( \Omega \) is bounded, so \( {\Gamma }_{x} \) is bounded above. Thus, \( {\mu }_{x} = \sup {\Gamma }_{x} \) is well-defined, and we set \( N\left( x\right) = 1/{\mu }_{x} \) . Note that since \( \overline{\Omega } \) is closed, we have \( {\mu }_{x} \in {\Gamma }_{x} \) .

Ainsi construite, on vérifie facilement que \( N \) est positivement homogène de degré 1, paire et vérifie \( N\left( x\right) = 0 \Leftrightarrow x = 0 \) . Par ailleurs,

> Constructed in this way, it is easy to verify that \( N \) is positively homogeneous of degree 1, even, and satisfies \( N\left( x\right) = 0 \Leftrightarrow x = 0 \) . Furthermore,

\[
N\left( x\right)  \leq  1 \Leftrightarrow  {\mu }_{x} \geq  1 \Leftrightarrow  1 \in  {\Gamma }_{x} \Leftrightarrow  x \in  \overline{\Omega },
\]

donc \( C = \{ x \in E \mid N\left( x\right) \leq 1\} = \overline{\Omega } \) est convexe. En utilisant le résultat de la question c), on en déduit que \( N \) est une norme.

> so \( C = \{ x \in E \mid N\left( x\right) \leq 1\} = \overline{\Omega } \) is convex. Using the result of question c), we deduce that \( N \) is a norm.

2/ Soit \( \alpha \geq 1 \) . Il est immédiat que l’application \( {N}_{\alpha } \) est positivement homogène de degré 1, positive et paire, et vérifie \( {N}_{\alpha }\left( x\right) = 0 \Leftrightarrow x = 0 \) . Pour prouver que c’est une norme, il suffit de vérifier, en vertu du résultat de la question 1/c), que l'ensemble

> 2/ Let \( \alpha \geq 1 \) . It is immediate that the mapping \( {N}_{\alpha } \) is positively homogeneous of degree 1, positive and even, and satisfies \( {N}_{\alpha }\left( x\right) = 0 \Leftrightarrow x = 0 \) . To prove that it is a norm, it suffices to verify, by virtue of the result in question 1/c), that the set

\[
C = \left\{  {x \in  {\mathbb{R}}^{n} \mid  {N}_{\alpha }\left( x\right)  \leq  1}\right\}   = \left\{  {\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n} \mid  {\left| {x}_{1}\right| }^{\alpha } + \cdots  + {\left| {x}_{n}\right| }^{\alpha } \leq  1}\right\}
\]

est convexe. Pour prouver ceci, on remarque que l’application \( {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto {x}^{\alpha } \) est convexe (elle est dérivable et sa fonction dérivée \( x \mapsto \alpha {x}^{\alpha - 1} \) est croissante), ce qui entraîne pour \( x, y \in C \; \forall \lambda \in \left\lbrack {0,1}\right\rbrack ,\forall i \in \{ 1,\ldots , n\} ,\;{\left| \lambda {x}_{i} + \left( 1 - \lambda \right) {y}_{i}\right| }^{\alpha } \leq {\left( \lambda \left| {x}_{i}\left| +\left( 1 - \lambda \right) \right| {y}_{i}\right| \right) }^{\alpha } \leq \lambda {\left| {x}_{i}\right| }^{\alpha } + \left( {1 - \lambda }\right) {\left| {y}_{i}\right| }^{\alpha }, \) donc par sommation sur \( i = 1,\ldots , n \)

> is convex. To prove this, we note that the mapping \( {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto {x}^{\alpha } \) is convex (it is differentiable and its derivative function \( x \mapsto \alpha {x}^{\alpha - 1} \) is increasing), which implies for \( x, y \in C \; \forall \lambda \in \left\lbrack {0,1}\right\rbrack ,\forall i \in \{ 1,\ldots , n\} ,\;{\left| \lambda {x}_{i} + \left( 1 - \lambda \right) {y}_{i}\right| }^{\alpha } \leq {\left( \lambda \left| {x}_{i}\left| +\left( 1 - \lambda \right) \right| {y}_{i}\right| \right) }^{\alpha } \leq \lambda {\left| {x}_{i}\right| }^{\alpha } + \left( {1 - \lambda }\right) {\left| {y}_{i}\right| }^{\alpha }, \) and thus by summation over \( i = 1,\ldots , n \)

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\left| \lambda {x}_{i} + \left( 1 - \lambda \right) {y}_{i}\right| }^{\alpha } \leq  \lambda \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{\alpha }}\right)  + \left( {1 - \lambda }\right) \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\left| {y}_{i}\right| }^{\alpha }}\right)  \leq  \lambda  + \left( {1 - \lambda }\right)  = 1.
\]

En d’autres termes, \( {\lambda x} + \left( {1 - \lambda }\right) y \in C \) . Ainsi, \( C \) est convexe et le résultat est prouvé.

> In other words, \( {\lambda x} + \left( {1 - \lambda }\right) y \in C \) . Thus, \( C \) is convex and the result is proven.

Problem 13 (MOYENNES). Soient \( I \) et \( J \) deux intervalles de \( \mathbb{R} \) et \( f \) un homéomorphisme de \( I \) dans \( J \) . Soient \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n}n \) couples de \( I \times {\mathbb{R}}^{+ * } \) . On dit que \( y \in I \) est la moyenne selon \( f \) de \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) si

> Problem 13 (MEANS). Let \( I \) and \( J \) be two intervals of \( \mathbb{R} \) and \( f \) be a homeomorphism from \( I \) to \( J \) . Let \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n}n \) be pairs of \( I \times {\mathbb{R}}^{+ * } \) . We say that \( y \in I \) is the mean according to \( f \) of \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) if

\[
f\left( y\right)  = \frac{{\alpha }_{1}f\left( {x}_{1}\right)  + \cdots  + {\alpha }_{n}f\left( {x}_{n}\right) }{{\alpha }_{1} + \cdots  + {\alpha }_{n}}\;\text{ ou encore }\;y = {f}^{-1}\left( \frac{{\alpha }_{1}f\left( {x}_{1}\right)  + \cdots  + {\alpha }_{n}f\left( {x}_{n}\right) }{{\alpha }_{1} + \cdots  + {\alpha }_{n}}\right) .
\]

(Par exemple, si \( {\alpha }_{i} = 1 \) pour tout \( i \) , la moyenne selon \( f\left( x\right) = x \) est la moyenne arithméti-que, la moyenne selon \( f\left( x\right) = \log x \) est la moyenne géométrique, la moyenne selon \( f\left( x\right) = \; 1/x \) est la moyenne harmonique.)

> (For example, if \( {\alpha }_{i} = 1 \) for all \( i \) , the mean according to \( f\left( x\right) = x \) is the arithmetic mean, the mean according to \( f\left( x\right) = \log x \) is the geometric mean, the mean according to \( f\left( x\right) = \; 1/x \) is the harmonic mean.)

a) Soient \( I, J, K \) trois intervalles de \( \mathbb{R} \) et \( f : I \rightarrow J, g : I \rightarrow K \) deux homéomorphismes. On dit que la moyenne selon \( f \) est inférieure à la moyenne selon \( g \) si pour toute famille finie de couples \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) de \( I \times {\mathbb{R}}^{+ * } \) , la moyenne selon \( f \) de cette famille est inférieure à la moyenne selon \( g \) de cette famille. Si \( f \) est croissante, montrer que la moyenne selon \( f \) est inférieure à la moyenne selon \( g \) si et seulement si \( h = f \circ {g}^{-1} \) est concave. Que dire si \( f \) est décroissante ?

> a) Let \( I, J, K \) be three intervals of \( \mathbb{R} \) and \( f : I \rightarrow J, g : I \rightarrow K \) be two homeomorphisms. We say that the mean according to \( f \) is less than the mean according to \( g \) if for any finite family of pairs \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) of \( I \times {\mathbb{R}}^{+ * } \) , the mean according to \( f \) of this family is less than the mean according to \( g \) of this family. If \( f \) is increasing, show that the mean according to \( f \) is less than the mean according to \( g \) if and only if \( h = f \circ {g}^{-1} \) is concave. What can be said if \( f \) is decreasing?

b) (Application.) Rappelons que pour tout \( \alpha \geq 1 \) , l’application

> b) (Application.) Recall that for all \( \alpha \geq 1 \) , the mapping

\[
{N}_{\alpha } : {\mathbb{R}}^{n} \rightarrow  \mathbb{R}\;\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  {\left( {\left| {x}_{1}\right| }^{\alpha } + \cdots  + {\left| {x}_{n}\right| }^{\alpha }\right) }^{1/\alpha }
\]

définit une norme sur \( {\mathbb{R}}^{n} \) (voir par exemple la question 2/ du problème précédent). Soient \( \alpha ,\beta \) deux nombres réels tels que \( 1 \leq \alpha \leq \beta \) . Montrer que

> defines a norm on \( {\mathbb{R}}^{n} \) (see for example question 2/ of the previous problem). Let \( \alpha ,\beta \) be two real numbers such that \( 1 \leq \alpha \leq \beta \) . Show that

\[
\forall x \in  {\mathbb{R}}^{n},\;{N}_{\beta }\left( x\right)  \leq  {N}_{\alpha }\left( x\right)  \leq  {n}^{\frac{1}{\alpha } - \frac{1}{\beta }}{N}_{\beta }\left( x\right) .
\]

Solution. a) Soit \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) une famille finie de \( I \times {\mathbb{R}}^{+ * }, y \) sa moyenne selon \( f, z \) sa moyenne selon \( g \) . La fonction \( f \) étant croissante, on a

> Solution. a) Let \( {\left( {x}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) be a finite family of \( I \times {\mathbb{R}}^{+ * }, y \) its mean according to \( f, z \) its mean according to \( g \) . Since the function \( f \) is increasing, we have

\[
\left( {y \leq  z}\right)  \Leftrightarrow  \left( {f\left( y\right)  \leq  f\left( z\right) }\right) .
\]

Pour tout \( i \) , posons \( {z}_{i} = g\left( {x}_{i}\right) \) , de sorte que \( f\left( {x}_{i}\right) = f \circ {g}^{-1}\left( {z}_{i}\right) = h\left( {z}_{i}\right) \) . On a

> For all \( i \) , let us set \( {z}_{i} = g\left( {x}_{i}\right) \) , such that \( f\left( {x}_{i}\right) = f \circ {g}^{-1}\left( {z}_{i}\right) = h\left( {z}_{i}\right) \) . We have

\[
f\left( y\right)  = \frac{{\alpha }_{1}h\left( {z}_{1}\right)  + \cdots  + {\alpha }_{n}h\left( {z}_{n}\right) }{{\alpha }_{1} + \cdots  + {\alpha }_{n}}\;\text{ et }\;f\left( z\right)  = h\left( \frac{{\alpha }_{1}{z}_{1} + \cdots  + {\alpha }_{n}{z}_{n}}{{\alpha }_{1} + \cdots  + {\alpha }_{n}}\right) .
\]

Ces deux expressions montrent que \( f\left( y\right) \leq f\left( z\right) \) si et seulement si l’inégalité caractérisant la concavité de \( h \) est vérifiée pour la famille \( {\left( {z}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) . On en conclut facilement que la moyenne selon \( f \) est inférieure à la moyenne selon \( g \) si et seulement si \( h = f \circ {g}^{-1} \) est concave.

> These two expressions show that \( f\left( y\right) \leq f\left( z\right) \) if and only if the inequality characterizing the concavity of \( h \) is satisfied for the family \( {\left( {z}_{i},{\alpha }_{i}\right) }_{1 \leq i \leq n} \) . We easily conclude that the mean according to \( f \) is less than the mean according to \( g \) if and only if \( h = f \circ {g}^{-1} \) is concave.

Si \( f \) est décroissante, la fonction \( - f \) est croissante. La moyenne selon \( f \) étant la même que la moyenne selon \( - f \) (revoir les définitions), on en conclut que la moyenne selon \( f \) est inférieure à la moyenne selon \( g \) si et seulement si \( \left( {-f}\right) \circ {g}^{-1} \) est concave, c’est-à-dire \( f \circ {g}^{-1} \) est convexe. b) Démontrons \( {N}_{\beta } \leq {N}_{\alpha } \) . Lorsque \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) vérifie \( {N}_{\alpha }\left( x\right) = 1 \) , on a \( \left| {x}_{i}\right| \leq 1 \) pour tout \( i \) et comme \( \alpha \leq \beta \) ceci entraîne \( {\left| {x}_{i}\right| }^{\beta } \leq {\left| {x}_{i}\right| }^{\alpha } \) pour tout \( i \) , donc

> If \( f \) is decreasing, the function \( - f \) is increasing. Since the mean according to \( f \) is the same as the mean according to \( - f \) (review the definitions), we conclude that the mean according to \( f \) is less than the mean according to \( g \) if and only if \( \left( {-f}\right) \circ {g}^{-1} \) is concave, that is to say \( f \circ {g}^{-1} \) is convex. b) Let us prove \( {N}_{\beta } \leq {N}_{\alpha } \) . When \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) satisfies \( {N}_{\alpha }\left( x\right) = 1 \) , we have \( \left| {x}_{i}\right| \leq 1 \) for all \( i \) and since \( \alpha \leq \beta \) this implies \( {\left| {x}_{i}\right| }^{\beta } \leq {\left| {x}_{i}\right| }^{\alpha } \) for all \( i \) , therefore

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{\beta } \leq  \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{\alpha } = 1
\]

et donc \( {N}_{\beta }\left( x\right) \leq 1 \) . Traitons le cas général. Si \( x = 0 \) , l’inégalité est triviale, sinon, en notant \( \lambda = 1/{N}_{\alpha }\left( x\right) \) , on a

> and therefore \( {N}_{\beta }\left( x\right) \leq 1 \) . Let us treat the general case. If \( x = 0 \) , the inequality is trivial, otherwise, by noting \( \lambda = 1/{N}_{\alpha }\left( x\right) \) , we have

\[
{N}_{\alpha }\left( {\lambda x}\right)  = 1\;\text{ donc }\;{N}_{\beta }\left( x\right)  = \frac{1}{\lambda }{N}_{\beta }\left( {\lambda x}\right)  \leq  \frac{1}{\lambda } = {N}_{\alpha }\left( x\right) .
\]

Démontrons maintenant l’inégalité \( {N}_{\alpha } \leq {n}^{\frac{1}{\alpha } - \frac{1}{\beta }}{N}_{\beta } \) . Soit \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) . On remarque que

> Let us now prove the inequality \( {N}_{\alpha } \leq {n}^{\frac{1}{\alpha } - \frac{1}{\beta }}{N}_{\beta } \) . Let \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{R}}^{n} \) . We note that

\[
\frac{{N}_{\alpha }\left( x\right) }{{n}^{1/\alpha }} = {\left( \frac{{\left| {x}_{1}\right| }^{\alpha } + \cdots  + {\left| {x}_{n}\right| }^{\alpha }}{n}\right) }^{1/\alpha }
\]

est la moyenne de la famille \( {\left( \left| {x}_{i}\right| ,1\right) }_{1 \leq i \leq n} \) selon la fonction \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto {x}^{\alpha } \) . De même, \( {N}_{\beta }\left( x\right) /{n}^{1/\beta } \) est la moyenne de cette même famille selon \( g : x \mapsto {x}^{\beta } \) . Comme \( f \circ {g}^{-1} = {x}^{\alpha /\beta } \) est une fonction concave (la fonction dérivée \( x \mapsto \left( {\alpha /\beta }\right) {x}^{\alpha /\beta - 1} \) est décroissante car \( \alpha \leq \beta \) ), et que \( f \) est croissante, le résultat de la question précédente entraîne que la moyenne selon \( f \) est inférieure à la moyenne selon \( g \) , en particulier

> is the mean of the family \( {\left( \left| {x}_{i}\right| ,1\right) }_{1 \leq i \leq n} \) according to the function \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}\;x \mapsto {x}^{\alpha } \) . Similarly, \( {N}_{\beta }\left( x\right) /{n}^{1/\beta } \) is the mean of this same family according to \( g : x \mapsto {x}^{\beta } \) . Since \( f \circ {g}^{-1} = {x}^{\alpha /\beta } \) is a concave function (the derivative function \( x \mapsto \left( {\alpha /\beta }\right) {x}^{\alpha /\beta - 1} \) is decreasing because \( \alpha \leq \beta \) ), and since \( f \) is increasing, the result of the previous question implies that the mean according to \( f \) is less than the mean according to \( g \) , in particular

\[
\frac{{N}_{\alpha }\left( x\right) }{{n}^{1/\alpha }} \leq  \frac{{N}_{\beta }\left( x\right) }{{n}^{1/\beta }}
\]

d'où l'inégalité désirée.

> whence the desired inequality.

Remarque. La dernière inégalité est une égalité pour \( x = \left( {1,\ldots ,1}\right) \) , on ne peut donc pas remplacer \( {n}^{1/\alpha - 1/\beta } \) par une constante plus petite. Remarquez d’ailleurs qu’il aurait été difficile de prouver cette inégalité sans utiliser le résultat de la question a).

> Remark. The last inequality is an equality for \( x = \left( {1,\ldots ,1}\right) \) , so one cannot replace \( {n}^{1/\alpha - 1/\beta } \) with a smaller constant. Note, moreover, that it would have been difficult to prove this inequality without using the result of question a).

PROBLEME 14 (FONCTIONS À VARIATION BORNÉE). Pour tout segment \( \left\lbrack {a, b}\right\rbrack \) de \( \mathbb{R} \) , on note sub( \( \left\lbrack {a, b}\right\rbrack \) ) l’ensemble des subdivisions \( \sigma \) de \( \left\lbrack {a, b}\right\rbrack : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) . Soit une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) . Pour toute subdivision \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) , on note

> PROBLEM 14 (FUNCTIONS OF BOUNDED VARIATION). For any segment \( \left\lbrack {a, b}\right\rbrack \) of \( \mathbb{R} \) , we denote by sub( \( \left\lbrack {a, b}\right\rbrack \) ) the set of subdivisions \( \sigma \) of \( \left\lbrack {a, b}\right\rbrack : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) . Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a mapping. For any subdivision \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) , we denote

\[
{\operatorname{Var}}_{\sigma }\left( f\right)  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left| {f\left( {x}_{i + 1}\right)  - f\left( {x}_{i}\right) }\right| .
\]

On suppose qu’il existe \( M > 0 \) tel que \( {\operatorname{Var}}_{\sigma }\left( f\right) \leq M \) pour toute subdivision \( \sigma \) de \( \left\lbrack {a, b}\right\rbrack \) (on dit alors que \( f \) est à variation bornée) et on pose

> We assume that there exists \( M > 0 \) such that \( {\operatorname{Var}}_{\sigma }\left( f\right) \leq M \) for any subdivision \( \sigma \) of \( \left\lbrack {a, b}\right\rbrack \) (we then say that \( f \) is of bounded variation) and we set

\[
\mathop{\bigvee }\limits_{a}^{b}f = \mathop{\sup }\limits_{{\sigma  \in  \operatorname{sub}\left( \left\lbrack  {a, b}\right\rbrack  \right) }}{\operatorname{Var}}_{\sigma }\left( f\right) .
\]

1 / a) Soit \( I = \left\lbrack {c, d}\right\rbrack \) un segment inclus dans \( \left\lbrack {a, b}\right\rbrack \) . Montrer que la restriction \( {f}_{\mid I} \) de \( f \) à \( I \) est à variation bornée. On peut ainsi définir

> 1 / a) Let \( I = \left\lbrack {c, d}\right\rbrack \) be a segment included in \( \left\lbrack {a, b}\right\rbrack \) . Show that the restriction \( {f}_{\mid I} \) of \( f \) to \( I \) is of bounded variation. We can thus define

\[
{\bigvee }_{c}^{d}f = \mathop{\sup }\limits_{{\sigma  \in  \operatorname{sub}\left( \left\lbrack  {c, d}\right\rbrack  \right) }}{\operatorname{Var}}_{\sigma }\left( {f}_{\mid I}\right) .
\]

b) Si \( a \leq x < y < z \leq b \) , montrer la relation de Chasles \( \mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f = \mathop{\bigvee }\limits_{x}^{z}f \) .

> b) If \( a \leq x < y < z \leq b \) , show the Chasles relation \( \mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f = \mathop{\bigvee }\limits_{x}^{z}f \) .

c) Si \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) est de classe \( {\mathcal{C}}^{1} \) , montrer que \( g \) est à variation bornée et que

> c) If \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is of class \( {\mathcal{C}}^{1} \) , show that \( g \) is of bounded variation and that

\[
{\bigvee }_{a}^{b}g = {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt}
\]

2 / On considère une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) .

> 2 / We consider a mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) .

a) Montrer que \( f \) est à variation bornée si et seulement s’il existe deux fonctions croissantes \( g, h : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) telles que \( f = g - h \) .

> a) Show that \( f \) is of bounded variation if and only if there exist two increasing functions \( g, h : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) such that \( f = g - h \) .

b) Montrer que si \( f \) est à variation bornée, \( f \) est une fonction réglée.

> b) Show that if \( f \) is of bounded variation, \( f \) is a regulated function.

3/ (Un exemple de fonction continue qui n'est pas à variation bornée.) Montrer que l'application

> 3/ (An example of a continuous function that is not of bounded variation.) Show that the mapping

\[
f : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R},\;f\left( x\right)  = x\cos \left( \frac{1}{x}\right) \text{ si }x \neq  0\;\text{ et }\;f\left( 0\right)  = 0
\]

n'est pas à variation bornée bien qu'elle soit continue.

> is not of bounded variation even though it is continuous.

Solution. 1/ a) Soit \( \sigma : c = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = d \) une subdivision de \( \left\lbrack {c, d}\right\rbrack \) . Alors \( {\sigma }^{\prime } : a \leq {x}_{0} < \cdots < {x}_{n} \leq b \) est une subdivision de \( \left\lbrack {a, b}\right\rbrack \) et donc

> Solution. 1/ a) Let \( \sigma : c = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = d \) be a subdivision of \( \left\lbrack {c, d}\right\rbrack \) . Then \( {\sigma }^{\prime } : a \leq {x}_{0} < \cdots < {x}_{n} \leq b \) is a subdivision of \( \left\lbrack {a, b}\right\rbrack \) and therefore

\[
{\operatorname{Var}}_{\sigma }\left( {f}_{\mid I}\right)  \leq  {\operatorname{Var}}_{{\sigma }^{\prime }}\left( f\right)  \leq  M.
\]

Cette majoration étant valable pour tout \( \sigma \in \operatorname{sub}\left( \left\lbrack {c, d}\right\rbrack \right) \) , on en déduit que \( {f}_{\mid I} \) est à variation bornée.

> Since this upper bound is valid for all \( \sigma \in \operatorname{sub}\left( \left\lbrack {c, d}\right\rbrack \right) \) , we deduce that \( {f}_{\mid I} \) is of bounded variation.

b) On considère deux subdivisions

> b) Consider two subdivisions

\[
{\sigma }_{1} : x = {x}_{0} < {x}_{1} < \cdots  < {x}_{p} = y \in  \operatorname{sub}\left( \left\lbrack  {x, y}\right\rbrack  \right) \;{\sigma }_{2} : y = {y}_{0} < {y}_{1} < \cdots  < {y}_{q} = z \in  \operatorname{sub}\left( \left\lbrack  {y, z}\right\rbrack  \right) .
\]

En les concaténant, on obtient une subdivision \( \sigma : x = {x}_{0} < \cdots < {x}_{p} = {y}_{0} < {y}_{1} < \cdots < {y}_{q} = z \) de \( \left\lbrack {x, z}\right\rbrack \) . Ainsi

> By concatenating them, we obtain a subdivision \( \sigma : x = {x}_{0} < \cdots < {x}_{p} = {y}_{0} < {y}_{1} < \cdots < {y}_{q} = z \) of \( \left\lbrack {x, z}\right\rbrack \) . Thus

\[
{\operatorname{Var}}_{{\sigma }_{1}}\left( f\right)  + {\operatorname{Var}}_{{\sigma }_{2}}\left( f\right)  = {\operatorname{Var}}_{\sigma }\left( f\right)  \leq  \mathop{\bigvee }\limits_{x}^{z}f.
\]

Cette majoration étant valable pour tout \( {\sigma }_{1} \in \operatorname{sub}\left( \left\lbrack {x, y}\right\rbrack \right) \) et \( {\sigma }_{2} \in \operatorname{sub}\left( \left\lbrack {y, z}\right\rbrack \right) \) , on en déduit

> Since this upper bound is valid for all \( {\sigma }_{1} \in \operatorname{sub}\left( \left\lbrack {x, y}\right\rbrack \right) \) and \( {\sigma }_{2} \in \operatorname{sub}\left( \left\lbrack {y, z}\right\rbrack \right) \) , we deduce

\[
\mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f \leq  \mathop{\bigvee }\limits_{x}^{z}f
\]

(*)

> Considérons maintenant une subdivision \( \sigma \) de \( \left\lbrack {x, z}\right\rbrack \) . En lui ajoutant le point \( y \) (s’il ne fait pas déjà parti de \( \sigma \) ), on obtient une subdivision \( {\sigma }^{\prime } \) de \( \left\lbrack {x, z}\right\rbrack \) qui vérifie \( {\operatorname{Var}}_{\sigma }\left( f\right) \leq {\operatorname{Var}}_{{\sigma }^{\prime }}\left( f\right) \) . On peut noter \( {\sigma }^{\prime } \) sous la forme

Now consider a subdivision \( \sigma \) of \( \left\lbrack {x, z}\right\rbrack \) . By adding the point \( y \) to it (if it is not already part of \( \sigma \) ), we obtain a subdivision \( {\sigma }^{\prime } \) of \( \left\lbrack {x, z}\right\rbrack \) which satisfies \( {\operatorname{Var}}_{\sigma }\left( f\right) \leq {\operatorname{Var}}_{{\sigma }^{\prime }}\left( f\right) \) . We can denote \( {\sigma }^{\prime } \) in the form

\[
{\sigma }^{\prime } : x = {x}_{0} < {x}_{1} < \cdots  < {x}_{p} = y = {y}_{0} < \cdots  < {y}_{q} = z.
\]

Considérons alors les subdivisions

> Consider then the subdivisions

\( {\sigma }_{1} : x = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = y \in \operatorname{sub}\left( \left\lbrack {x, y}\right\rbrack \right) \;{\sigma }_{2} : y = {y}_{0} < {y}_{1} < \cdots < {y}_{q} = z \in \operatorname{sub}\left( \left\lbrack {y, z}\right\rbrack \right) . \) On a

> \( {\sigma }_{1} : x = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = y \in \operatorname{sub}\left( \left\lbrack {x, y}\right\rbrack \right) \;{\sigma }_{2} : y = {y}_{0} < {y}_{1} < \cdots < {y}_{q} = z \in \operatorname{sub}\left( \left\lbrack {y, z}\right\rbrack \right) . \) We have

\[
{\operatorname{Var}}_{\sigma }\left( f\right)  \leq  {\operatorname{Var}}_{{\sigma }^{\prime }}\left( f\right)  = {\operatorname{Var}}_{{\sigma }_{1}}\left( f\right)  + {\operatorname{Var}}_{{\sigma }_{2}}\left( f\right)  \leq  \mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f.
\]

Ceci étant vrai pour toute subdivision \( \sigma \) de \( \left\lbrack {x, z}\right\rbrack \) , on en déduit \( \mathop{\bigvee }\limits_{x}^{z}f \leq \mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f \) , d’où le résultat avec (*).

> Since this is true for any subdivision \( \sigma \) of \( \left\lbrack {x, z}\right\rbrack \) , we deduce \( \mathop{\bigvee }\limits_{x}^{z}f \leq \mathop{\bigvee }\limits_{x}^{y}f + \mathop{\bigvee }\limits_{y}^{z}f \) , hence the result with (*).

c) Soit \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) une subdivision de \( \left\lbrack {a, b}\right\rbrack \) . Pour tout \( i \) , on a

> c) Let \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) be a subdivision of \( \left\lbrack {a, b}\right\rbrack \) . For all \( i \) , we have

\[
\left| {g\left( {x}_{i + 1}\right)  - g\left( {x}_{i}\right) }\right|  = \left| {{\int }_{{x}_{i}}^{{x}_{i + 1}}{g}^{\prime }\left( t\right) {dt}}\right|  \leq  {\int }_{{x}_{i}}^{{x}_{i + 1}}\left| {{g}^{\prime }\left( t\right) }\right| {dt}
\]

donc par sommation sur \( i,{\operatorname{Var}}_{\sigma }\left( g\right) \leq {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \) . Ceci étant vrai pour tout \( \sigma \in \operatorname{sub}\left( \left\lbrack {a, b}\right\rbrack \right) \) on en déduit que \( g \) est à variation bornée et que

> so by summation over \( i,{\operatorname{Var}}_{\sigma }\left( g\right) \leq {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \) . Since this is true for all \( \sigma \in \operatorname{sub}\left( \left\lbrack {a, b}\right\rbrack \right) \) we deduce that \( g \) is of bounded variation and that

\[
\mathop{\bigvee }\limits_{a}^{b}g \leq  {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt}
\]

\( \left( {* * }\right) \)

> Il nous faut maintenant prouver l’inégalité réciproque. Si \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) est une subdivision de \( \left\lbrack {a, b}\right\rbrack \) , on peut écrire pour tout \( i \) , en vertu du théorème des accroissements finis,

We must now prove the reverse inequality. If \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) is a subdivision of \( \left\lbrack {a, b}\right\rbrack \) , we can write for all \( i \) , by the mean value theorem,

\[
g\left( {x}_{i + 1}\right)  - g\left( {x}_{i}\right)  = \left( {{x}_{i + 1} - {x}_{i}}\right) {g}^{\prime }\left( {\theta }_{i}\right) \;\text{ avec }\;{\theta }_{i} \in  \rbrack {x}_{i},{x}_{i + 1}\lbrack ,
\]

de sorte que

> so that

\[
{\operatorname{Var}}_{\sigma }\left( g\right)  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left( {{x}_{i + 1} - {x}_{i}}\right) \left| {{g}^{\prime }\left( {\theta }_{i}\right) }\right| \;\text{ avec }\;\forall i,{\theta }_{i} \in  \rbrack {x}_{i},{x}_{i + 1}\lbrack .
\]

Cette dernière expression est une somme de Riemann relative à la subdivision \( \sigma \) pour la fonction \( \left| {g}^{\prime }\right| \) . En faisant tendre le pas de \( \sigma \) vers 0, on voit donc que \( {\operatorname{Var}}_{\sigma }\left( g\right) \) tend vers \( {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \) , d’où \( {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \leq \mathop{\bigvee }\limits_{a}^{b}g \) . On en déduit avec (**) le résultat.

> This last expression is a Riemann sum relative to the subdivision \( \sigma \) for the function \( \left| {g}^{\prime }\right| \) . By letting the mesh of \( \sigma \) tend to 0, we see that \( {\operatorname{Var}}_{\sigma }\left( g\right) \) tends to \( {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \) , hence \( {\int }_{a}^{b}\left| {{g}^{\prime }\left( t\right) }\right| {dt} \leq \mathop{\bigvee }\limits_{a}^{b}g \) . We deduce the result from (**).

2/ a) Condition suffisante. Une fonction croissante \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) est à variation bornée car pour toute subdivision \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) de \( \left\lbrack {a, b}\right\rbrack \) ,

> 2/ a) Sufficient condition. An increasing function \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is of bounded variation because for any subdivision \( \sigma : a = {x}_{0} < {x}_{1} < \cdots < {x}_{n} = b \) of \( \left\lbrack {a, b}\right\rbrack \) ,

\[
{\operatorname{Var}}_{\sigma }\left( f\right)  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left| {f\left( {x}_{i + 1}\right)  - f\left( {x}_{i}\right) }\right|  = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left\lbrack  {f\left( {x}_{i + 1}\right)  - f\left( {x}_{i}\right) }\right\rbrack   = f\left( b\right)  - f\left( a\right) .
\]

La différence de deux fonctions à variation bornée étant à variation bornée (c'est immédiat), on en déduit que \( f = g - h \) est à variation bornée.

> Since the difference of two functions of bounded variation is of bounded variation (this is immediate), we deduce that \( f = g - h \) is of bounded variation.

Condition nécessaire. Soit \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \mathop{\bigvee }\limits_{a}^{x}f \) . D’après le résultat de la question 1/ b), \( g \) est une fonction croissante. Posons \( h = g - f \) . La fonction \( h \) est croissante car

> Necessary condition. Let \( g : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto \mathop{\bigvee }\limits_{a}^{x}f \) . According to the result of question 1/ b), \( g \) is an increasing function. Let \( h = g - f \) . The function \( h \) is increasing because

\[
\forall x < y,\;h\left( y\right)  - h\left( x\right)  = \mathop{\bigvee }\limits_{x}^{y}f - \left\lbrack  {f\left( y\right)  - f\left( x\right) }\right\rbrack   \geq  0\;\text{ car }\;\left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  \mathop{\bigvee }\limits_{x}^{y}f
\]

(cette dernière assertion est vraie car \( \sigma : x < y \) est une subdivision de \( \left\lbrack {x, y}\right\rbrack \) ). Ainsi, \( f = g - h \) est la différence de deux fonctions croissantes.

> (this last assertion is true because \( \sigma : x < y \) is a subdivision of \( \left\lbrack {x, y}\right\rbrack \) ). Thus, \( f = g - h \) is the difference of two increasing functions.

b) D’après la question précédente, on peut écrire \( f = g - h \) où \( g \) et \( h \) sont deux fonctions croissantes. Une fonction monotone est réglée (voir la conséquence du théorème 4 page 99), donc \( f \) , différence de deux fonctions réglées, est une fonction réglée.

> b) According to the previous question, we can write \( f = g - h \) where \( g \) and \( h \) are two increasing functions. A monotonic function is regulated (see the consequence of theorem 4 on page 99), so \( f \) , the difference of two regulated functions, is a regulated function.

3 / Considérons pour tout entier \( n \geq 2 \) la subdivision de \( \left\lbrack {0,1}\right\rbrack \) définie par

> 3 / Consider for every integer \( n \geq 2 \) the subdivision of \( \left\lbrack {0,1}\right\rbrack \) defined by

\[
{\sigma }_{n} : 0 < \frac{1}{n\pi } < \frac{1}{\left( {n - 1}\right) \pi } < \cdots  < \frac{1}{2\pi } < \frac{1}{\pi } < 1.
\]

Pour tout \( k \) on a \( f\left( \frac{1}{k\pi }\right) = \cos \left( {k\pi }\right) /\left( {k\pi }\right) = {\left( -1\right) }^{k}/\left( {k\pi }\right) \) donc

> For all \( k \) we have \( f\left( \frac{1}{k\pi }\right) = \cos \left( {k\pi }\right) /\left( {k\pi }\right) = {\left( -1\right) }^{k}/\left( {k\pi }\right) \) therefore

\[
{\operatorname{Var}}_{{\sigma }_{n}}\left( f\right)  \geq  \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\left| {f\left( \frac{1}{\left( {k + 1}\right) \pi }\right)  - f\left( \frac{1}{k\pi }\right) }\right|  = \frac{1}{\pi }\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\left( {\frac{1}{k + 1} + \frac{1}{k}}\right)  \geq  \frac{1}{\pi }\mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\frac{2}{k + 1}.
\]

La série \( \mathop{\sum }\limits_{k}\frac{1}{k + 1} \) diverge, donc l’ensemble \( {\left( {\operatorname{Var}}_{\sigma }\right) }_{\sigma \in \operatorname{sub}\left( \left\lbrack {0,1}\right\rbrack \right) } \) n’est pas majoré, ce qui prouve que \( f \) n’est pas à variation bornée.

> The series \( \mathop{\sum }\limits_{k}\frac{1}{k + 1} \) diverges, so the set \( {\left( {\operatorname{Var}}_{\sigma }\right) }_{\sigma \in \operatorname{sub}\left( \left\lbrack {0,1}\right\rbrack \right) } \) is not bounded above, which proves that \( f \) is not of bounded variation.

Problems 15 (FONCTIONS PRESQUE-PÉRIODIQUES). Soit \( E \) un espace vectoriel normé (sur \( \mathbb{R} \) ou \( \mathbb{C} \) ). On note \( \mathcal{F} \) l’ensemble des fonctions de \( \mathbb{R} \) dans \( E \) . Pour tout \( f \in \mathcal{F} \) , on note

> Problems 15 (ALMOST-PERIODIC FUNCTIONS). Let \( E \) be a normed vector space (over \( \mathbb{R} \) or \( \mathbb{C} \)). We denote by \( \mathcal{F} \) the set of functions from \( \mathbb{R} \) to \( E \). For any \( f \in \mathcal{F} \), we denote

\[
\parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in  \mathbb{R}}}\parallel f\left( x\right) \parallel  \in  {\mathbb{R}}^{ + } \cup  \{  + \infty \} \text{ et }\forall \tau  \in  \mathbb{R},{f}_{\tau } : \mathbb{R} \rightarrow  {Ex} \mapsto  f\left( {x + \tau }\right) .
\]

On dit que \( f \in \mathcal{F} \) est presque-périodique si \( f \) est continue sur \( \mathbb{R} \) et si

> \( f \in \mathcal{F} \) is said to be almost-periodic if \( f \) is continuous on \( \mathbb{R} \) and if

\[
\forall \varepsilon  > 0,\exists \Lambda  > 0,\forall \alpha  \in  \mathbb{R},\exists \tau  \in  \left\lbrack  {\alpha ,\alpha  + \Lambda }\right\lbrack  ,\;{\begin{Vmatrix}f - {f}_{\tau }\end{Vmatrix}}_{\infty } < \varepsilon .
\]

(*)

> On note \( \mathcal{P} \) le sous-ensemble de \( \mathcal{F} \) constitué des fonctions presque-périodiques.

We denote by \( \mathcal{P} \) the subset of \( \mathcal{F} \) consisting of almost-periodic functions.

> a) Donner une classe de fonctions classique incluse dans \( \mathcal{P} \) .

a) Give a classical class of functions included in \( \mathcal{P} \).

> b) Si \( f \in \mathcal{P} \) , montrer que \( f \) est bornée et uniformément continue sur \( \mathbb{R} \) .

b) If \( f \in \mathcal{P} \), show that \( f \) is bounded and uniformly continuous on \( \mathbb{R} \).

> c) On note \( \mathcal{B} \) le s.e.v de \( \mathcal{F} \) constitué des fonctions continues et bornées, et on munit \( \mathcal{B} \) de la norme \( \parallel .{\parallel }_{\infty } \) . Pour tout \( f \in \mathcal{B} \) , on note \( A\left( f\right) = \left\{ {{f}_{a}, a \in \mathbb{R}}\right\} \) . Si \( f \in \mathcal{B} \) , montrer l’équivalence

c) We denote by \( \mathcal{B} \) the subspace of \( \mathcal{F} \) consisting of continuous and bounded functions, and we equip \( \mathcal{B} \) with the norm \( \parallel .{\parallel }_{\infty } \). For any \( f \in \mathcal{B} \), we denote \( A\left( f\right) = \left\{ {{f}_{a}, a \in \mathbb{R}}\right\} \). If \( f \in \mathcal{B} \), show the equivalence

\[
\left( {f \in  \mathcal{P}}\right)  \Leftrightarrow  \left( {A\left( f\right) \text{ est précompact dans }\mathcal{B}}\right) .
\]

(La précompacité est définie dans la preuve du théorème de Bolzano-Weierstrass, page 29). d) Soient \( f, g \in \mathcal{P} \) . Montrer que \( f + g \in \mathcal{P} \) et \( {fg} \in \mathcal{P} \) si \( E \) est une algèbre normée. e) Montrer que \( \mathcal{P} \) est une partie fermée de \( \mathcal{B} \) .

> (Precompactness is defined in the proof of the Bolzano-Weierstrass theorem, page 29). d) Let \( f, g \in \mathcal{P} \). Show that \( f + g \in \mathcal{P} \) and \( {fg} \in \mathcal{P} \) if \( E \) is a normed algebra. e) Show that \( \mathcal{P} \) is a closed subset of \( \mathcal{B} \).

Solution. a) Il est clair que la classe des fonctions continues périodiques est incluse dans \( \mathcal{P} \) (il suffit, dans (*), de choisir \( \Lambda \) égal à la période).

> Solution. a) It is clear that the class of continuous periodic functions is included in \( \mathcal{P} \) (it suffices, in (*), to choose \( \Lambda \) equal to the period).

b) Une fonction presque-périodique \( f \) est bornée. En effet, en choisissant \( \varepsilon = 1 \) dans (*) et en considérant le \( \Lambda \) correspondant, on a pour tout nombre réel \( x \)

> b) An almost-periodic function \( f \) is bounded. Indeed, by choosing \( \varepsilon = 1 \) in (*) and considering the corresponding \( \Lambda \), we have for any real number \( x \)

\[
\exists y \in  \lbrack x - \Lambda , x\lbrack ,\;{\begin{Vmatrix}f - {f}_{y}\end{Vmatrix}}_{\infty } < 1
\]

donc \( \parallel f\left( {x - y}\right) - f\left( x\right) \parallel < 1 \) ce qui entraîne

> therefore \( \parallel f\left( {x - y}\right) - f\left( x\right) \parallel < 1 \) which implies

\[
\parallel f\left( x\right) \parallel  < 1 + \parallel f\left( {x - y}\right) \parallel  \leq  1 + \mathop{\sup }\limits_{{t \in  \left\lbrack  {0,\Lambda }\right\rbrack  }}\parallel f\left( t\right) \parallel \operatorname{car}x - y \in  \left\lbrack  {0,\Lambda }\right\rbrack  ,
\]

et ceci pour tout \( x \in \mathbb{R} \) d’où le caractère borné de \( f \) .

> and this for any \( x \in \mathbb{R} \), hence the bounded nature of \( f \).

Montrons maintenant qu'une fonction presque-périodique \( f \) est uniformément continue. Soit \( \varepsilon > 0 \) et considérons le \( \Lambda \) correspondant dans (*). La fonction \( f \) étant continue sur le compact \( \left\lbrack {0,\Lambda + 1}\right\rbrack \) , elle \( y \) est uniformément continue donc

> Let us now show that an almost-periodic function \( f \) is uniformly continuous. Let \( \varepsilon > 0 \) and consider the corresponding \( \Lambda \) in (*). Since the function \( f \) is continuous on the compact set \( \left\lbrack {0,\Lambda + 1}\right\rbrack \), it \( y \) is uniformly continuous, therefore

\[
\exists \eta  \in  \rbrack 0,1\left\lbrack  {,\forall x,{x}^{\prime } \in  \left\lbrack  {0,\Lambda  + 1}\right\rbrack  ,\left| {x - {x}^{\prime }}\right|  < \eta ,\;\begin{Vmatrix}{f\left( x\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix} < \varepsilon .}\right.
\]

Considérons alors deux réels \( x,{x}^{\prime } \) tels que \( \left| {x - {x}^{\prime }}\right| < \eta \) , avec \( x \leq {x}^{\prime } \) . La fonction \( f \) étant presque périodique,

> Let us then consider two real numbers \( x,{x}^{\prime } \) such that \( \left| {x - {x}^{\prime }}\right| < \eta \), with \( x \leq {x}^{\prime } \). Since the function \( f \) is almost-periodic,

\[
\exists \tau  \in  \lbrack x - \Lambda , x\lbrack ,\;{\begin{Vmatrix}f - {f}_{\tau }\end{Vmatrix}}_{\infty } < \varepsilon .
\]

Ceci entraîne

> This implies

\[
\parallel f\left( {x - \tau }\right)  - f\left( x\right) \parallel  < \varepsilon \;\text{ et }\;\begin{Vmatrix}{f\left( {{x}^{\prime } - \tau }\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix} < \varepsilon ,
\]

donc comme \( x - \tau \) et \( {x}^{\prime } - \tau \) appartiennent à \( \left\lbrack {0,\Lambda + 1}\right\rbrack \) ,

> so since \( x - \tau \) and \( {x}^{\prime } - \tau \) belong to \( \left\lbrack {0,\Lambda + 1}\right\rbrack \) ,

\[
\begin{Vmatrix}{f\left( x\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix} \leq  \parallel f\left( x\right)  - f\left( {x - \tau }\right) \parallel  + \begin{Vmatrix}{f\left( {x - \tau }\right)  - f\left( {{x}^{\prime } - \tau }\right) }\end{Vmatrix} + \begin{Vmatrix}{f\left( {{x}^{\prime } - \tau }\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix} < \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon }.
\]

Ceci est vrai pour tout couple \( \left( {x,{x}^{\prime }}\right) \) de réels tel que \( \left| {x - {x}^{\prime }}\right| < \eta \) , d’où l’uniforme continuité de \( f \) sur \( \mathbb{R} \) .

> This is true for any pair \( \left( {x,{x}^{\prime }}\right) \) of real numbers such that \( \left| {x - {x}^{\prime }}\right| < \eta \) , hence the uniform continuity of \( f \) on \( \mathbb{R} \) .

c) Condition nécessaire. Soit \( f \in \mathcal{P},\varepsilon > 0 \) et le \( \Lambda \) correspondant dans (*). Comme \( f \) est uniformément continue sur \( \mathbb{R} \) , on voit que

> c) Necessary condition. Let \( f \in \mathcal{P},\varepsilon > 0 \) and the corresponding \( \Lambda \) in (*). Since \( f \) is uniformly continuous on \( \mathbb{R} \) , we see that

\[
\exists \left( {{\eta }_{1},\ldots ,{\eta }_{n}}\right)  \in  {\left\lbrack  0,\Lambda \right\rbrack  }^{n},\forall {y}_{0} \in  \left\lbrack  {0,\Lambda }\right\rbrack  ,\exists i,\;{\begin{Vmatrix}{f}_{{y}_{0}} - {f}_{{\eta }_{i}}\end{Vmatrix}}_{\infty } < \varepsilon .
\]

\( \left( {* * }\right) \)

> Maintenant, soit \( y \in \mathbb{R} \) . D’après (*), il existe \( \tau \in \left\lbrack {-y, - y + \Lambda \left\lbrack \right. }\right. \) tel que \( \parallel f - {f}_{\tau }{\parallel }_{\infty } < \varepsilon \) . Ceci s’écrit aussi \( {\begin{Vmatrix}{f}_{y} - {f}_{\rho }\end{Vmatrix}}_{\infty } < \varepsilon \) avec \( \rho = \tau + y \in \lbrack 0,\Lambda \lbrack \) . D’après (**), il existe \( i \in \{ 1,\ldots , n\} \) tel que \( {\begin{Vmatrix}{f}_{\rho } - {f}_{{\eta }_{i}}\end{Vmatrix}}_{\infty } < \varepsilon \) , et on en déduit

Now, let \( y \in \mathbb{R} \) . According to (*), there exists \( \tau \in \left\lbrack {-y, - y + \Lambda \left\lbrack \right. }\right. \) such that \( \parallel f - {f}_{\tau }{\parallel }_{\infty } < \varepsilon \) . This can also be written as \( {\begin{Vmatrix}{f}_{y} - {f}_{\rho }\end{Vmatrix}}_{\infty } < \varepsilon \) with \( \rho = \tau + y \in \lbrack 0,\Lambda \lbrack \) . According to (**), there exists \( i \in \{ 1,\ldots , n\} \) such that \( {\begin{Vmatrix}{f}_{\rho } - {f}_{{\eta }_{i}}\end{Vmatrix}}_{\infty } < \varepsilon \) , and we deduce from this

\[
{\begin{Vmatrix}{f}_{y} - {f}_{{\eta }_{i}}\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}{f}_{y} - {f}_{\rho }\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}{f}_{\rho } - {f}_{{\eta }_{i}}\end{Vmatrix}}_{\infty } < \varepsilon  + \varepsilon  = {2\varepsilon }.
\]

En d’autres termes on a \( A\left( f\right) \subset \mathop{\bigcup }\limits_{{i = 1}}^{n}\mathrm{\;B}\left( {{f}_{{\eta }_{i}},{2\varepsilon }}\right) \) , d’où la précompacité de \( A\left( f\right) \) dans \( \mathcal{B} \) .

> In other words, we have \( A\left( f\right) \subset \mathop{\bigcup }\limits_{{i = 1}}^{n}\mathrm{\;B}\left( {{f}_{{\eta }_{i}},{2\varepsilon }}\right) \) , hence the precompactness of \( A\left( f\right) \) in \( \mathcal{B} \) .

Condition suffisante. Soit \( \varepsilon > 0 \) . Par hypothèse, il existe une famille finie \( {\left( {f}_{{a}_{i}}\right) }_{1 \leq i \leq n} \) de \( A\left( f\right) \) telle que

> Sufficient condition. Let \( \varepsilon > 0 \) . By hypothesis, there exists a finite family \( {\left( {f}_{{a}_{i}}\right) }_{1 \leq i \leq n} \) of \( A\left( f\right) \) such that

\[
A\left( f\right)  \subset  \mathop{\bigcup }\limits_{{i = 1}}^{n}\mathrm{\;B}\left( {{f}_{{a}_{i}},\varepsilon }\right) .
\]

\( \left( {* * * }\right) \)

> Posons \( \Lambda = 1 + {2\mu } \) où \( \mu = \sup \left\{ {\left| {a}_{1}\right| ,\ldots ,\left| {a}_{n}\right| }\right\} \) et considérons maintenant un réel quelconque \( \alpha \) . D'après (***),

Let us set \( \Lambda = 1 + {2\mu } \) where \( \mu = \sup \left\{ {\left| {a}_{1}\right| ,\ldots ,\left| {a}_{n}\right| }\right\} \) and now consider any real number \( \alpha \) . According to (***),

\[
\exists i \in  \{ 1,\ldots , n\} ,\;{\begin{Vmatrix}{f}_{\alpha  + \mu } - {f}_{{a}_{i}}\end{Vmatrix}}_{\infty } < \varepsilon \text{ ce qui équivaut à }{\begin{Vmatrix}{f}_{\alpha  + \mu  - {a}_{i}} - f\end{Vmatrix}}_{\infty } < \varepsilon .
\]

Ainsi, pour tout réel \( \alpha \) , nous avons trouvé \( y \in \left\lbrack {\alpha ,\alpha + \Lambda \left\lbrack \right. }\right. \) (ici \( y = \alpha + \mu - {a}_{i} \) ) tel que \( {\begin{Vmatrix}{f}_{y} - f\end{Vmatrix}}_{\infty } < \varepsilon \) . Ceci suffit pour montrer que \( f \) est presque-périodique.

> Thus, for any real number \( \alpha \) , we have found \( y \in \left\lbrack {\alpha ,\alpha + \Lambda \left\lbrack \right. }\right. \) (here \( y = \alpha + \mu - {a}_{i} \) ) such that \( {\begin{Vmatrix}{f}_{y} - f\end{Vmatrix}}_{\infty } < \varepsilon \) . This is sufficient to show that \( f \) is almost periodic.

d) D’après la question précédente, \( A\left( f\right) \) et \( A\left( g\right) \) sont précompacts. Ainsi, si on considère \( \varepsilon > 0 \) , il existe deux familles finies \( {\left( {f}_{{a}_{i}}\right) }_{1 \leq i \leq m} \) de \( A\left( f\right) \) et \( {\left( {g}_{{b}_{j}}\right) }_{1 \leq j \leq n} \) de \( A\left( g\right) \) telles que

> d) According to the previous question, \( A\left( f\right) \) and \( A\left( g\right) \) are precompact. Thus, if we consider \( \varepsilon > 0 \) , there exist two finite families \( {\left( {f}_{{a}_{i}}\right) }_{1 \leq i \leq m} \) of \( A\left( f\right) \) and \( {\left( {g}_{{b}_{j}}\right) }_{1 \leq j \leq n} \) of \( A\left( g\right) \) such that

\[
A\left( f\right)  \subset  \mathop{\bigcup }\limits_{{i = 1}}^{m}\mathrm{\;B}\left( {{f}_{{a}_{i}},\varepsilon }\right) \;\text{ et }\;A\left( g\right)  \subset  \mathop{\bigcup }\limits_{{j = 1}}^{n}\mathrm{\;B}\left( {{g}_{{b}_{j}},\varepsilon }\right) .
\]

On en conclut

> We conclude that

\[
A\left( {f + g}\right)  \subset  A\left( f\right)  + A\left( g\right)  \subset  \mathop{\bigcup }\limits_{\substack{{1 \leq  i \leq  m} \\  {1 \leq  j \leq  n} }}\mathrm{\;B}\left( {{f}_{{a}_{i}} + {g}_{{b}_{j}},{2\varepsilon }}\right) ,
\]

donc \( A\left( {f + g}\right) \) est précompact, donc \( f + g \in \mathcal{P} \) d’après la question précédente.

> therefore \( A\left( {f + g}\right) \) is precompact, so \( f + g \in \mathcal{P} \) according to the previous question.

Supposons maintenant que \( E \) soit une algèbre normée. Comme \( f \) et \( g \) sont bornées, \( M = \; \parallel f{\parallel }_{\infty } \) et \( N = \parallel g{\parallel }_{\infty } \) sont finis. Soient \( a \in \mathbb{R} \) et \( i, j \) tels que \( {\begin{Vmatrix}{f}_{a} - {f}_{{a}_{i}}\end{Vmatrix}}_{\infty } < \varepsilon \) et \( {\begin{Vmatrix}{g}_{a} - {g}_{{b}_{j}}\end{Vmatrix}}_{\infty } < \varepsilon \) . L'inégalité

> Now suppose that \( E \) is a normed algebra. Since \( f \) and \( g \) are bounded, \( M = \; \parallel f{\parallel }_{\infty } \) and \( N = \parallel g{\parallel }_{\infty } \) are finite. Let \( a \in \mathbb{R} \) and \( i, j \) be such that \( {\begin{Vmatrix}{f}_{a} - {f}_{{a}_{i}}\end{Vmatrix}}_{\infty } < \varepsilon \) and \( {\begin{Vmatrix}{g}_{a} - {g}_{{b}_{j}}\end{Vmatrix}}_{\infty } < \varepsilon \) . The inequality

\[
\begin{Vmatrix}{{f}_{a}{g}_{a}\left( x\right)  - {f}_{{a}_{i}}{g}_{{b}_{j}}\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{f}_{a}{g}_{a}\left( x\right)  - {f}_{{a}_{i}}{g}_{a}\left( x\right) }\end{Vmatrix} + \begin{Vmatrix}{{f}_{{a}_{i}}{g}_{a}\left( x\right)  - {f}_{{a}_{i}}{g}_{{b}_{j}}\left( x\right) }\end{Vmatrix}
\]

\[
\leq  \begin{Vmatrix}{{f}_{a}\left( x\right)  - {f}_{{a}_{i}}\left( x\right) }\end{Vmatrix} \cdot  \begin{Vmatrix}{{g}_{a}\left( x\right) }\end{Vmatrix} + \begin{Vmatrix}{{f}_{{a}_{i}}\left( x\right) }\end{Vmatrix} \cdot  \begin{Vmatrix}{{g}_{a}\left( x\right)  - {g}_{{b}_{j}}\left( x\right) }\end{Vmatrix} \leq  {N\varepsilon } + {M\varepsilon }
\]

montre que

> shows that

\[
A\left( {fg}\right)  \subset  \mathop{\bigcup }\limits_{\substack{{1 \leq  i \leq  m} \\  {1 \leq  j \leq  n} }}\mathrm{\;B}\left( {{f}_{{a}_{i}}{g}_{{b}_{j}},\left( {M + N}\right) \varepsilon }\right) ,
\]

donc comme précédemment \( A\left( {fg}\right) \) est précompact, donc \( {fg} \in \mathcal{P} \) .

> therefore, as before, \( A\left( {fg}\right) \) is precompact, so \( {fg} \in \mathcal{P} \) .

e) Soit \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( \mathcal{P} \) qui converge vers \( f \in \mathcal{B} \) . Montrons que \( f \in \mathcal{P} \) . Soit \( \varepsilon > 0 \) et \( N \in \mathbb{N} \) tel que \( {\begin{Vmatrix}f - {f}_{N}\end{Vmatrix}}_{\infty } < \varepsilon \) . Comme \( {f}_{N} \) est presque-périodique,

> e) Let \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of \( \mathcal{P} \) that converges to \( f \in \mathcal{B} \) . Let us show that \( f \in \mathcal{P} \) . Let \( \varepsilon > 0 \) and \( N \in \mathbb{N} \) be such that \( {\begin{Vmatrix}f - {f}_{N}\end{Vmatrix}}_{\infty } < \varepsilon \) . Since \( {f}_{N} \) is almost periodic,

\[
\exists \Lambda  > 0,\forall \alpha  \in  \mathbb{R},\exists \tau  \in  \lbrack \alpha ,\alpha  + \Lambda \lbrack ,\;{\begin{Vmatrix}\left( {f}_{N}\right)  - {\left( {f}_{N}\right) }_{\tau }\end{Vmatrix}}_{\infty } < \varepsilon
\]

donc

> therefore

\[
{\begin{Vmatrix}f - {f}_{\tau }\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}f - {f}_{N}\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}\left( {f}_{N}\right)  - {\left( {f}_{N}\right) }_{\tau }\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}{\left( {f}_{N}\right) }_{\tau } - {f}_{\tau }\end{Vmatrix}}_{\infty } < \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon },
\]

ce qui suffit pour prouver que \( f \in \mathcal{P} \) .

> which is sufficient to prove that \( f \in \mathcal{P} \) .

Remarque. Les fonctions presque périodiques ont été introduites par Bohr au début du vingtième siècle, dans le cadre de l’étude des séries de Dirichlet \( \sum {a}_{n}/{n}^{s} \) , et généralisent les séries de Fourier. On peut montrer que pour toute fonction presque périodique \( f \) , la limite \( M\left( f\right) = \mathop{\lim }\limits_{{T \rightarrow \infty }}\frac{1}{T}{\int }_{0}^{T}f\left( t\right) {dt} \) existe (on l’appelle valeur moyenne de \( f \) ). Une fonction complexe \( f \) est presque périodique si et seulement si on peut écrire

> Remark. Almost periodic functions were introduced by Bohr at the beginning of the twentieth century in the context of the study of Dirichlet series \( \sum {a}_{n}/{n}^{s} \) , and they generalize Fourier series. It can be shown that for any almost periodic function \( f \) , the limit \( M\left( f\right) = \mathop{\lim }\limits_{{T \rightarrow \infty }}\frac{1}{T}{\int }_{0}^{T}f\left( t\right) {dt} \) exists (it is called the mean value of \( f \) ). A complex function \( f \) is almost periodic if and only if it can be written

\[
f\left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{e}^{i{\lambda }_{n}t},\;\text{ avec }\;\forall n \in  \mathbb{N}\;{a}_{n} \in  \mathbb{C},\;{\lambda }_{n} \in  \mathbb{R},
\]

où la convergence est uniforme sur \( \mathbb{R} \) (la condition suffisante de ce résultat est une conséquence des résultats démontrés dans ce problème), et on a l'équivalent de l'inégalité de Bessel \( \sum {\left| {a}_{n}\right| }^{2} \leq M\left( {f}^{2}\right) \) . Un exemple typique de fonction presque périodique est \( t \mapsto \zeta \left( {\sigma + {it}}\right) \) (avec \( \sigma > 1 \) donné). Ceci entraîne par exemple que pour tout \( \varepsilon > 0 \) et pour tout \( T > 0 \) , il existe \( t > T \) tel que \( \zeta \left( \sigma \right) - \varepsilon < \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq \zeta \left( \sigma \right) \) .

> where the convergence is uniform on \( \mathbb{R} \) (the sufficient condition for this result is a consequence of the results proven in this problem), and we have the equivalent of Bessel's inequality \( \sum {\left| {a}_{n}\right| }^{2} \leq M\left( {f}^{2}\right) \) . A typical example of an almost periodic function is \( t \mapsto \zeta \left( {\sigma + {it}}\right) \) (with \( \sigma > 1 \) given). This implies, for example, that for any \( \varepsilon > 0 \) and for any \( T > 0 \) , there exists \( t > T \) such that \( \zeta \left( \sigma \right) - \varepsilon < \left| {\zeta \left( {\sigma + {it}}\right) }\right| \leq \zeta \left( \sigma \right) \) .
