#### 1.5. Exercises

*Français : 1.5. Exercices*

EXERCICE 1. Démontrer les inégalités suivantes.

> EXERCISE 1. Prove the following inequalities.

\[
\text{ a) }\;\forall x \geq  0,\;x - \frac{{x}^{2}}{2} \leq  \log \left( {1 + x}\right)  \leq  x - \frac{{x}^{2}}{2} + \frac{{x}^{3}}{3}\text{ . }
\]

\[
\text{ b) }\;\forall x \geq  0,\;x - \frac{{x}^{3}}{6} \leq  \sin x \leq  x - \frac{{x}^{3}}{6} + \frac{{x}^{5}}{120}\text{ . }
\]

\[
\text{ c) }\;\forall x \in  \mathbb{R},\;1 - \frac{{x}^{2}}{2} \leq  \cos x \leq  1 - \frac{{x}^{2}}{2} + \frac{{x}^{4}}{24}\text{ . }
\]

Solution. a) D’après la formule de Taylor-Lagrange appliquée à la fonction \( f : x \mapsto \log \left( {1 + x}\right) \) :

> Solution. a) According to the Taylor-Lagrange formula applied to the function \( f : x \mapsto \log \left( {1 + x}\right) \):

\[
\forall x \geq  0,\exists \theta  \in  \rbrack 0,1\lbrack ,\;\log \left( {1 + x}\right)  = f\left( x\right)  = f\left( 0\right)  + x{f}^{\prime }\left( 0\right)  + \frac{{x}^{2}}{2}{f}^{\prime \prime }\left( 0\right)  + \frac{{x}^{3}}{6}{f}^{\prime \prime \prime }\left( {\theta x}\right) .
\]

(*)

> Comme

Since

\[
f\left( x\right)  = \log \left( {1 + x}\right) ,\;{f}^{\prime }\left( x\right)  = \frac{1}{1 + x},\;{f}^{\prime \prime }\left( x\right)  =  - \frac{1}{{\left( 1 + x\right) }^{2}},\;{f}^{\prime \prime \prime }\left( x\right)  = \frac{2}{{\left( 1 + x\right) }^{3}},
\]

on a \( f\left( 0\right) = 0,{f}^{\prime }\left( 0\right) = 1,{f}^{\prime \prime }\left( 0\right) = 2 \) et \( 0 \leq {f}^{\prime \prime \prime }\left( {\theta x}\right) \leq 2 \) , ce qui en remplaçant dans (*) donne le résultat demandé.

> we have \( f\left( 0\right) = 0,{f}^{\prime }\left( 0\right) = 1,{f}^{\prime \prime }\left( 0\right) = 2 \) and \( 0 \leq {f}^{\prime \prime \prime }\left( {\theta x}\right) \leq 2 \), which, when substituted into (*), gives the requested result.

b) On procède de la même manière : on considère le développement de Taylor-Lagrange de \( x \mapsto \sin x \) à l’ordre 3 pour prouver l’inégalité de gauche,à l’ordre 5 pour celle de droite.

> b) We proceed in the same way: we consider the Taylor-Lagrange expansion of \( x \mapsto \sin x \) to order 3 to prove the left inequality, and to order 5 for the right one.

c) Pareil en développant à l'ordre 2 puis à l'ordre 4.

> c) Same by expanding to order 2 then to order 4.

EXERCICE 2. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application dérivable en 0 et nulle en 0. Soit \( \ell \in {\mathbb{N}}^{ * } \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on pose

> EXERCISE 2. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a mapping differentiable at 0 and zero at 0. Let \( \ell \in {\mathbb{N}}^{ * } \). For all \( n \in {\mathbb{N}}^{ * } \), we define

\[
{S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{{n\ell }}f\left( \frac{k}{{n}^{2}}\right) .
\]

Montrer que la suite \( {\left( {S}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) converge et calculer sa limite.

> Show that the sequence \( {\left( {S}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) converges and calculate its limit.

Solution. Le principe est le suivant. Lorsque \( n \) est grand, chacun des termes \( k/{n}^{2} \) pour \( 0 \leq \; k \leq n\ell \) est petit, donc au premier ordre, on a l’approximation \( f\left( \frac{k}{{n}^{2}}\right) \approx {f}^{\prime }\left( 0\right) \frac{k}{{n}^{2}} \) , de sorte que \( {S}_{n} \approx \frac{{f}^{\prime }\left( 0\right) }{{n}^{2}}\mathop{\sum }\limits_{{k = 0}}^{{n\ell }}k \approx {\ell }^{2}/2{f}^{\prime }\left( 0\right) \) . Nous allons mettre rigoureusement en forme cette idée.

> Solution. The principle is as follows. When \( n \) is large, each of the terms \( k/{n}^{2} \) for \( 0 \leq \; k \leq n\ell \) is small, so to the first order, we have the approximation \( f\left( \frac{k}{{n}^{2}}\right) \approx {f}^{\prime }\left( 0\right) \frac{k}{{n}^{2}} \), such that \( {S}_{n} \approx \frac{{f}^{\prime }\left( 0\right) }{{n}^{2}}\mathop{\sum }\limits_{{k = 0}}^{{n\ell }}k \approx {\ell }^{2}/2{f}^{\prime }\left( 0\right) \). We will formalize this idea rigorously.

L’application \( f \) est dérivable en 0, donc \( f\left( x\right) = f\left( 0\right) + x{f}^{\prime }\left( 0\right) + o\left( x\right) = x{f}^{\prime }\left( 0\right) + o\left( x\right) \) . Ainsi, si on se donne \( \varepsilon > 0 \) ,

> The mapping \( f \) is differentiable at 0, so \( f\left( x\right) = f\left( 0\right) + x{f}^{\prime }\left( 0\right) + o\left( x\right) = x{f}^{\prime }\left( 0\right) + o\left( x\right) \). Thus, if we are given \( \varepsilon > 0 \),

\[
\exists \eta  > 0,\forall x \in  \left\lbrack  {0,\eta \left\lbrack  {,\;\left| {f\left( x\right)  - x{f}^{\prime }\left( 0\right) }\right|  \leq  {\varepsilon x}.}\right. }\right.
\]

Soit \( N \in {\mathbb{N}}^{ * } \) tel que \( \ell /N < \eta \) . Pour tout \( n \geq N \) et pour tout entier \( k \) vérifiant \( 0 \leq k \leq n\ell \) , on a

> Let \( N \in {\mathbb{N}}^{ * } \) be such that \( \ell /N < \eta \) . For all \( n \geq N \) and for all integers \( k \) satisfying \( 0 \leq k \leq n\ell \) , we have

\[
0 \leq  \frac{k}{{n}^{2}} \leq  \frac{n\ell }{{n}^{2}} = \frac{\ell }{n} \leq  \frac{\ell }{N} < \eta
\]

donc

> therefore

\[
\forall n \geq  N,\forall k,0 \leq  k \leq  n\ell ,\;\left| {f\left( \frac{k}{{n}^{2}}\right)  - \frac{k}{{n}^{2}}{f}^{\prime }\left( 0\right) }\right|  \leq  \varepsilon \frac{k}{{n}^{2}},
\]

de sorte que

> so that

\[
\forall n \geq  N,\;\left| {\mathop{\sum }\limits_{{k = 0}}^{{n\ell }}f\left( \frac{k}{{n}^{2}}\right)  - {f}^{\prime }\left( 0\right) \mathop{\sum }\limits_{{k = 0}}^{{n\ell }}\frac{k}{{n}^{2}}}\right|  \leq  \mathop{\sum }\limits_{{k = 0}}^{{n\ell }}\left| {f\left( \frac{k}{{n}^{2}}\right)  - {f}^{\prime }\left( 0\right) \frac{k}{{n}^{2}}}\right|  \leq  \varepsilon \mathop{\sum }\limits_{{k = 0}}^{{n\ell }}\frac{k}{{n}^{2}}.
\]

(*)

> Or

\[
\mathop{\sum }\limits_{{k = 0}}^{{n\ell }}\frac{k}{{n}^{2}} = \frac{1}{{n}^{2}}\frac{n\ell \left( {n\ell  + 1}\right) }{2} = \frac{{\ell }^{2}}{2} + \frac{\ell }{2n},
\]

donc (*) s'écrit aussi

> thus (*) can also be written as

\[
\forall n \geq  N,\;\left| {{S}_{n} - {f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2} - {f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2n}}\right|  \leq  \varepsilon \left( {\frac{{\ell }^{2}}{2} + \frac{{\ell }^{2}}{2n}}\right)  \leq  {\ell }^{2}\varepsilon .
\]

On a donc

> We therefore have

\[
\left| {{S}_{n} - {f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2}}\right|  \leq  \left| {{S}_{n} - {f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2} - {f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2n}}\right|  + \left| {{f}^{\prime }\left( 0\right) \frac{{\ell }^{2}}{2n}}\right|  \leq  {\ell }^{2}\varepsilon  + \frac{\left| {{f}^{\prime }\left( 0\right) }\right| {\ell }^{2}}{2n}.
\]

Si on choisit \( {N}_{1} \geq N \) tel que \( \left| {{f}^{\prime }\left( 0\right) }\right| /\left( {2{N}_{1}}\right) < \varepsilon \) , on a donc \( \left| {{S}_{n} - {f}^{\prime }\left( 0\right) {\ell }^{2}/2}\right| < 2{\ell }^{2}\varepsilon \) pour tout \( n \geq {N}_{1} \) , ce qui prouve que \( \left( {S}_{n}\right) \) converge et tend vers \( {f}^{\prime }\left( 0\right) {\ell }^{2}/2 \) .

> If we choose \( {N}_{1} \geq N \) such that \( \left| {{f}^{\prime }\left( 0\right) }\right| /\left( {2{N}_{1}}\right) < \varepsilon \) , we then have \( \left| {{S}_{n} - {f}^{\prime }\left( 0\right) {\ell }^{2}/2}\right| < 2{\ell }^{2}\varepsilon \) for all \( n \geq {N}_{1} \) , which proves that \( \left( {S}_{n}\right) \) converges and tends to \( {f}^{\prime }\left( 0\right) {\ell }^{2}/2 \) .

EXERCICE 3. a) Soit l’application \( f : \mathbb{R} \rightarrow \mathbb{R} \) définie par \( f\left( x\right) = 0 \) si \( x \leq 0 \) , et par \( f\left( x\right) = {e}^{-1/x} \) si \( x > 0 \) . Démontrer que \( f \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) .

> EXERCISE 3. a) Let the mapping \( f : \mathbb{R} \rightarrow \mathbb{R} \) be defined by \( f\left( x\right) = 0 \) if \( x \leq 0 \) , and by \( f\left( x\right) = {e}^{-1/x} \) if \( x > 0 \) . Prove that \( f \) is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) .

b) Démontrer qu’il existe une fonction \( \varphi \) de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) telle que

> b) Prove that there exists a function \( \varphi \) of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) such that

\[
\forall x \in  \left\lbrack  {-1,1}\right\rbrack  ,\varphi \left( x\right)  = 1\;\text{ et }\;\forall x \in  \mathbb{R},\left| x\right|  \geq  2,\varphi \left( x\right)  = 0.
\]

![bo_d7fjkrs91nqc73ereoog_83_389_426_893_225_0.jpg](images/gourdon_analysis_fr_en_031_bod7fjkrs91nqc73ereoog833894268932250.jpg)

FIGURE 3. Le graphe de la fonction \( \varphi \) .

> FIGURE 3. The graph of the function \( \varphi \) .

Solution. a) Il est clair que \( f \) est de classe \( {\mathcal{C}}^{\infty } \) sur chacun des intervalles \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \) . Il nous reste donc à prouver l’existence de \( {f}^{\left( n\right) }\left( 0\right) \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> Solution. a) It is clear that \( f \) is of class \( {\mathcal{C}}^{\infty } \) on each of the intervals \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \) . It remains for us to prove the existence of \( {f}^{\left( n\right) }\left( 0\right) \) for all \( n \in {\mathbb{N}}^{ * } \) .

Commençons par montrer par récurrence sur \( n \) que

> Let us begin by showing by induction on \( n \) that

\[
\forall n \in  \mathbb{N},\exists {P}_{n} \in  \mathbb{R}\left\lbrack  X\right\rbrack  ,\forall x > 0,\;{f}^{\left( n\right) }\left( x\right)  = {e}^{-1/x}{P}_{n}\left( \frac{1}{x}\right) .
\]

(*)

> Pour \( n = 0 \) c’est vrai avec \( {P}_{0} = 1 \) . Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Il suffit d’écrire

For \( n = 0 \) it is true with \( {P}_{0} = 1 \) . Assume the result is true at rank \( n - 1 \) and show it at rank \( n \) . It suffices to write

\[
\forall x > 0,\;{f}^{\left( n\right) }\left( x\right)  = {\left( {f}^{\left( n - 1\right) }\right) }^{\prime }\left( x\right)  = \frac{1}{{x}^{2}}{e}^{-1/x}{P}_{n - 1}\left( \frac{1}{x}\right)  - \frac{1}{{x}^{2}}{e}^{-1/x}{P}_{n - 1}^{\prime }\left( \frac{1}{x}\right)  = {e}^{-1/x}{P}_{n}\left( \frac{1}{x}\right)
\]

avec \( {P}_{n}\left( X\right) = {X}^{2}{P}_{n - 1}\left( X\right) - {X}^{2}{P}_{n - 1}^{\prime }\left( X\right) \) .

> with \( {P}_{n}\left( X\right) = {X}^{2}{P}_{n - 1}\left( X\right) - {X}^{2}{P}_{n - 1}^{\prime }\left( X\right) \) .

On déduit de (*) que \( \mathop{\lim }\limits_{{x \rightarrow 0}}{f}^{\left( n\right) }\left( x\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Or pour \( x < 0,{f}^{\left( n\right) }\left( x\right) = 0 \) , donc

> We deduce from (*) that \( \mathop{\lim }\limits_{{x \rightarrow 0}}{f}^{\left( n\right) }\left( x\right) = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) . However, for \( x < 0,{f}^{\left( n\right) }\left( x\right) = 0 \) , therefore

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x \neq  0} }}{f}^{\left( n\right) }\left( x\right)  = 0.
\]

En utilisant maintenant la proposition 6 page 76 par récurrence sur \( n \) , on en déduit que \( {f}^{\left( n\right) }\left( 0\right) \) existe pour tout \( n \) et \( {f}^{\left( n\right) }\left( 0\right) = 0 \) . Finalement, \( f \) est bien de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) .

> Using now proposition 6 on page 76 by induction on \( n \) , we deduce that \( {f}^{\left( n\right) }\left( 0\right) \) exists for all \( n \) and \( {f}^{\left( n\right) }\left( 0\right) = 0 \) . Finally, \( f \) is indeed of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) .

b) Nous allons donner deux manières de construire une telle fonction.

> b) We will provide two ways to construct such a function.

Première méthode. Considérons l'application

> First method. Let us consider the mapping

\[
g : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \frac{f\left( {f\left( 1\right)  - f\left( x\right) }\right) }{f\left( {f\left( 1\right) }\right) }.
\]

![bo_d7fjkrs91nqc73ereoog_83_388_1674_861_225_0.jpg](images/gourdon_analysis_fr_en_030_bod7fjkrs91nqc73ereoog8338816748612250.jpg)

Figure 4. Le graphe de la fonction \( g \) .

> Figure 4. The graph of the function \( g \) .

L’application \( g \) , composée de fonctions de classe \( {\mathcal{C}}^{\infty } \) , est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) . Par ailleurs,

> The mapping \( g \) , composed of \( {\mathcal{C}}^{\infty } \) class functions, is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) . Furthermore,

\[
\forall x \leq  0,\;g\left( x\right)  = \frac{f\left( {f\left( 1\right)  - 0}\right) }{f\left( {f\left( 1\right) }\right) } = 1
\]

\[
\forall x \geq  1,\;f\left( 1\right)  - f\left( x\right)  \leq  0 \Rightarrow  f\left( {f\left( 1\right)  - f\left( x\right) }\right)  = 0 \Rightarrow  g\left( x\right)  = 0.
\]

On voit maintenant facilement que l’application \( \varphi : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto g\left( {x - 1}\right) g\left( {-x - 1}\right) \) convient. Seconde méthode. L’application \( g : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto f\left( {x + 1}\right) f\left( {-x + 1}\right) \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) et

> It is now easy to see that the mapping \( \varphi : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto g\left( {x - 1}\right) g\left( {-x - 1}\right) \) is suitable. Second method. The mapping \( g : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto f\left( {x + 1}\right) f\left( {-x + 1}\right) \) is of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) and

\[
\forall x \in  \rbrack  - 1,1\lbrack ,\;g\left( x\right)  > 0,\;\forall x \in  \mathbb{R},\left| x\right|  \geq  1,\;g\left( x\right)  = 0.
\]

![bo_d7fjkrs91nqc73ereoog_84_387_344_909_203_0.jpg](images/gourdon_analysis_fr_en_032_bod7fjkrs91nqc73ereoog843873449092030.jpg)

Figure 5. Le graphe de la fonction \( g \) (seconde méthode).

> Figure 5. The graph of the function \( g \) (second method).

On pose maintenant \( h : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \frac{1}{K}{\int }_{-\infty }^{x}g\left( t\right) {dt} \) , où \( K = {\int }_{-\infty }^{+\infty }g\left( t\right) {dt} \) . Cette application est de classe \( {\mathcal{C}}^{\infty } \) et vérifie \( h\left( x\right) = 0 \) pour \( x \leq - 1 \) et \( h\left( x\right) = 1 \) pour \( x \geq 1 \) . On termine en choisissant pour \( \varphi \) l’application

> We now set \( h : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \frac{1}{K}{\int }_{-\infty }^{x}g\left( t\right) {dt} \) , where \( K = {\int }_{-\infty }^{+\infty }g\left( t\right) {dt} \) . This mapping is of class \( {\mathcal{C}}^{\infty } \) and satisfies \( h\left( x\right) = 0 \) for \( x \leq - 1 \) and \( h\left( x\right) = 1 \) for \( x \geq 1 \) . We conclude by choosing for \( \varphi \) the mapping

\[
\varphi  : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  h\left( {{2x} + 3}\right) h\left( {-{2x} + 3}\right) .
\]

EXERCICE 4 (THÉORÉME DE DARBOUX). Par commodité de notation, on désigne par \( \left( {t, u}\right) \) l’intervalle \( \left\lbrack {t, u}\right\rbrack \) si \( t \leq u \) , l’intervalle \( \left\lbrack {u, t}\right\rbrack \) si \( u < t \) .

> EXERCISE 4 (DARBOUX'S THEOREM). For convenience of notation, we denote by \( \left( {t, u}\right) \) the interval \( \left\lbrack {t, u}\right\rbrack \) if \( t \leq u \) , the interval \( \left\lbrack {u, t}\right\rbrack \) if \( u < t \) .

Soit \( I \) un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application dérivable sur \( I \) . On veut montrer que \( {f}^{\prime } \) vérifie la propriété des valeurs intermédiaires, c’est-à-dire que \( {f}^{\prime }\left( I\right) \) est un intervalle.

> Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a differentiable mapping on \( I \) . We want to show that \( {f}^{\prime } \) satisfies the intermediate value property, that is to say that \( {f}^{\prime }\left( I\right) \) is an interval.

On se donne \( \left( {a, b}\right) \in {I}^{2} \) tel que \( a < b \) et \( y \in \left( {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right) \) . Il s’agit donc de montrer qu’il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( {f}^{\prime }\left( c\right) = y \) . Nous proposons deux méthodes pour obtenir ce résultat.

> We are given \( \left( {a, b}\right) \in {I}^{2} \) such that \( a < b \) and \( y \in \left( {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right) \) . It is therefore a matter of showing that there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( {f}^{\prime }\left( c\right) = y \) . We propose two methods to obtain this result.

1/ (Première méthode.) On considère les deux applications

> 1/ (First method.) Consider the two mappings

\[
\varphi  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;\varphi \left( x\right)  = \frac{f\left( x\right)  - f\left( a\right) }{x - a}\;\text{ si }x \neq  a,\;\varphi \left( a\right)  = {f}^{\prime }\left( a\right)
\]

\[
\psi  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;\psi \left( x\right)  = \frac{f\left( b\right)  - f\left( x\right) }{b - x}\;\text{ si }x \neq  b,\;\psi \left( b\right)  = {f}^{\prime }\left( b\right) .
\]

Montrer que \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \cup \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) . En déduire l’existence de \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( y = {f}^{\prime }\left( c\right) \) . 2/ (Seconde méthode.) a) Soit \( g : I \rightarrow \mathbb{R} \) une application vérifiant \( {g}^{\prime }\left( a\right) \geq 0 \) et \( {g}^{\prime }\left( b\right) \leq 0 \) . Montrer l’existence de \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( {g}^{\prime }\left( c\right) = 0 \) .

> Show that \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \cup \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) . Deduce the existence of \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( y = {f}^{\prime }\left( c\right) \) . 2/ (Second method.) a) Let \( g : I \rightarrow \mathbb{R} \) be a mapping satisfying \( {g}^{\prime }\left( a\right) \geq 0 \) and \( {g}^{\prime }\left( b\right) \leq 0 \) . Show the existence of \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( {g}^{\prime }\left( c\right) = 0 \) .

b) En déduire qu’il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( {f}^{\prime }\left( c\right) = y \) .

> b) Deduce that there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( {f}^{\prime }\left( c\right) = y \) .

Solution. 1/ L’application \( \varphi \) est clairement continue sur \( \rbrack a, b\rbrack \) , et elle est continue en \( a \) par définition de \( {f}^{\prime }\left( a\right) \) . Elle est donc continue sur \( \left\lbrack {a, b}\right\rbrack \) , ce qui avec le théorème des valeurs in-termédiaires entraîne

> Solution. 1/ The mapping \( \varphi \) is clearly continuous on \( \rbrack a, b\rbrack \) , and it is continuous at \( a \) by the definition of \( {f}^{\prime }\left( a\right) \) . It is therefore continuous on \( \left\lbrack {a, b}\right\rbrack \) , which, along with the intermediate value theorem, implies

\[
\left( {\varphi \left( a\right) ,\varphi \left( b\right) }\right)  = \left( {{f}^{\prime }\left( a\right) ,\frac{f\left( b\right)  - f\left( a\right) }{b - a}}\right)  \subset  \varphi \left( \left\lbrack  {a, b}\right\rbrack  \right) .
\]

De même,

> Similarly,

\[
\left( {\psi \left( a\right) ,\psi \left( b\right) }\right)  = \left( {\frac{f\left( b\right)  - f\left( a\right) }{b - a},{f}^{\prime }\left( b\right) }\right)  \subset  \psi \left( \left\lbrack  {a, b}\right\rbrack  \right) .
\]

On en déduit

> We deduce

\[
\left( {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right)  \subset  \left( {{f}^{\prime }\left( a\right) ,\frac{f\left( b\right)  - f\left( a\right) }{b - a}}\right)  \cup  \left( {\frac{f\left( b\right)  - f\left( a\right) }{b - a},{f}^{\prime }\left( b\right) }\right)  \subset  \varphi \left( \left\lbrack  {a, b}\right\rbrack  \right)  \cup  \psi \left( \left\lbrack  {a, b}\right\rbrack  \right) .
\]

Or \( y \in \left( {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right) \) , donc \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \cup \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) .

> However \( y \in \left( {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right) \) , so \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \cup \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) .

Si \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \) , deux cas se présentent.

> If \( y \in \varphi \left( \left\lbrack {a, b}\right\rbrack \right) \) , two cases arise.

(i) Soit \( y = {f}^{\prime }\left( a\right) \) , et alors c’est terminé avec \( c = a \) .

> (i) Either \( y = {f}^{\prime }\left( a\right) \) , and then we are done with \( c = a \) .

(ii) Soit \( \exists x \in \rbrack a, b\rbrack ,\;y = \varphi \left( x\right) = \frac{f\left( x\right) - f\left( a\right) }{x - a} \) et d’après le théorème des accroissements finis, il existe \( c \in \rbrack a, x\left\lbrack { \subset \left\lbrack {a, b}\right\rbrack }\right. \) tel que \( y = {f}^{\prime }\left( c\right) \) .

> (ii) Or \( \exists x \in \rbrack a, b\rbrack ,\;y = \varphi \left( x\right) = \frac{f\left( x\right) - f\left( a\right) }{x - a} \) and, by the mean value theorem, there exists \( c \in \rbrack a, x\left\lbrack { \subset \left\lbrack {a, b}\right\rbrack }\right. \) such that \( y = {f}^{\prime }\left( c\right) \) .

On procéderait de même si \( y \in \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) , d’où le résultat.

> We would proceed similarly if \( y \in \psi \left( \left\lbrack {a, b}\right\rbrack \right) \) , hence the result.

2/ a) Si \( {g}^{\prime }\left( a\right) = 0 \) ou \( {g}^{\prime }\left( b\right) = 0 \) , c’est évident avec \( c = a \) ou \( c = b \) . Sinon \( {g}^{\prime }\left( a\right) > 0 \) et \( {g}^{\prime }\left( b\right) < 0 \) . Considérons le développement de Taylor-Young de \( g \) à l’ordre 1 au voisinage de \( a \)

> 2/ a) If \( {g}^{\prime }\left( a\right) = 0 \) or \( {g}^{\prime }\left( b\right) = 0 \) , it is obvious with \( c = a \) or \( c = b \) . Otherwise \( {g}^{\prime }\left( a\right) > 0 \) and \( {g}^{\prime }\left( b\right) < 0 \) . Consider the Taylor-Young expansion of \( g \) to order 1 in the neighborhood of \( a \)

\[
g\left( x\right)  = g\left( a\right)  + \left( {x - a}\right) {g}^{\prime }\left( a\right)  + o\left( {x - a}\right)  = g\left( a\right)  + \left( {x - a}\right) \left( {{g}^{\prime }\left( a\right)  + \varepsilon \left( {x - a}\right) }\right) ,\;\varepsilon \left( {x - a}\right)  = o\left( 1\right) .
\]

Il existe \( \eta > 0 \) tel que \( \varepsilon \left( {x - a}\right) < {g}^{\prime }\left( a\right) /2 \) sur \( \left\lbrack {a, a + \eta }\right\rbrack \) , donc \( g\left( x\right) \geq g\left( a\right) + \left( {x - a}\right) {g}^{\prime }\left( a\right) /2 > g\left( a\right) \) sur \( \rbrack a, a + \eta \rbrack \) . On démontrerait de même l’existence d’un \( \alpha > 0 \) tel que \( g\left( x\right) > g\left( b\right) \) sur \( \lbrack b - \alpha , b\lbrack \) .

> There exists \( \eta > 0 \) such that \( \varepsilon \left( {x - a}\right) < {g}^{\prime }\left( a\right) /2 \) on \( \left\lbrack {a, a + \eta }\right\rbrack \) , so \( g\left( x\right) \geq g\left( a\right) + \left( {x - a}\right) {g}^{\prime }\left( a\right) /2 > g\left( a\right) \) on \( \rbrack a, a + \eta \rbrack \) . One could similarly demonstrate the existence of a \( \alpha > 0 \) such that \( g\left( x\right) > g\left( b\right) \) on \( \lbrack b - \alpha , b\lbrack \) .

L’application \( g \) est continue sur le compact \( \left\lbrack {a, b}\right\rbrack \) , donc il existe \( c \in \left\lbrack {a, b}\right\rbrack \) vérifiant \( g\left( c\right) = \; \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}g\left( x\right) \) . D’après ce que l’on vient de voir, on a \( c \neq a \) et \( c \neq b \) . Donc \( c \in \rbrack a, b\lbrack \) , et on en déduit que \( {g}^{\prime }\left( c\right) = 0 \) , d’où le résultat.

> The mapping \( g \) is continuous on the compact set \( \left\lbrack {a, b}\right\rbrack \) , so there exists \( c \in \left\lbrack {a, b}\right\rbrack \) satisfying \( g\left( c\right) = \; \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}g\left( x\right) \) . According to what we have just seen, we have \( c \neq a \) and \( c \neq b \) . Thus \( c \in \rbrack a, b\lbrack \) , and we deduce that \( {g}^{\prime }\left( c\right) = 0 \) , hence the result.

b) Considérons l’application \( g : I \rightarrow \mathbb{R}\;x \mapsto {yx} - f\left( x\right) \) . Quitte à changer \( f \) en \( - f \) , on peut supposer \( {f}^{\prime }\left( b\right) \geq {f}^{\prime }\left( a\right) \) . Comme \( y \in \left\lbrack {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right\rbrack \) , on a \( {g}^{\prime }\left( a\right) = y - {f}^{\prime }\left( a\right) \geq 0 \) et \( {g}^{\prime }\left( b\right) = y - {f}^{\prime }\left( b\right) \leq \) 0. Le résultat de la question précédente entraîne alors l’existence de \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( {g}^{\prime }\left( c\right) = 0 \) . On a donc \( y - {f}^{\prime }\left( c\right) = 0 \) , donc \( y = {f}^{\prime }\left( c\right) \) .

> b) Consider the mapping \( g : I \rightarrow \mathbb{R}\;x \mapsto {yx} - f\left( x\right) \) . By changing \( f \) to \( - f \) if necessary, we can assume \( {f}^{\prime }\left( b\right) \geq {f}^{\prime }\left( a\right) \) . Since \( y \in \left\lbrack {{f}^{\prime }\left( a\right) ,{f}^{\prime }\left( b\right) }\right\rbrack \) , we have \( {g}^{\prime }\left( a\right) = y - {f}^{\prime }\left( a\right) \geq 0 \) and \( {g}^{\prime }\left( b\right) = y - {f}^{\prime }\left( b\right) \leq \) 0. The result of the previous question then implies the existence of \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( {g}^{\prime }\left( c\right) = 0 \) . We therefore have \( y - {f}^{\prime }\left( c\right) = 0 \) , so \( y = {f}^{\prime }\left( c\right) \) .

Remarque. Si \( f \) est de classe \( {\mathcal{C}}^{1} \) , ce théorème résulte tout simplement du théorème des valeurs intermédiaires appliqué à la fonction dérivée \( {f}^{\prime } \) . Mais une fonction dérivée n’est pas forcément continue (voir la remarque 1 page 71).

> Remark. If \( f \) is of class \( {\mathcal{C}}^{1} \) , this theorem follows quite simply from the intermediate value theorem applied to the derivative function \( {f}^{\prime } \) . However, a derivative function is not necessarily continuous (see remark 1 on page 71).

- Une démonstration de nature plus topologique de ce théorème fait l'objet de l'exercice 9 page 47.

> - A more topological proof of this theorem is the subject of exercise 9 on page 47.

- La réciproque du théorème de Darboux est fausse : une fonction vérifiant la propriété des valeurs intermédiaires n'est pas forcément une fonction dérivée.

> - The converse of Darboux's theorem is false: a function satisfying the intermediate value property is not necessarily a derivative function.

EXERCICE 5 (FORMULE DE SIMPSON). a) Soit \( \alpha > 0 \) et \( g : \left\lbrack {-\alpha ,\alpha }\right\rbrack \rightarrow \mathbb{R} \) une application impaire 5 fois dérivable sur \( \left\lbrack {-\alpha ,\alpha }\right\rbrack \) . Montrer

> EXERCISE 5 (SIMPSON'S FORMULA). a) Let \( \alpha > 0 \) and \( g : \left\lbrack {-\alpha ,\alpha }\right\rbrack \rightarrow \mathbb{R} \) be an odd mapping 5 times differentiable on \( \left\lbrack {-\alpha ,\alpha }\right\rbrack \) . Show

\[
\exists \theta  \in  \rbrack 0,\alpha \lbrack ,\;g\left( \alpha \right)  = \frac{\alpha }{3}\left( {{g}^{\prime }\left( \alpha \right)  + 2{g}^{\prime }\left( 0\right) }\right)  - \frac{{\alpha }^{5}}{180}{g}^{\left( 5\right) }\left( \theta \right) .
\]

b) Soient \( a, b \in \mathbb{R}, a < b \) , et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{5} \) sur \( \left\lbrack {a, b}\right\rbrack \) . Montrer

> b) Let \( a, b \in \mathbb{R}, a < b \) and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a map of class \( {\mathcal{C}}^{5} \) on \( \left\lbrack {a, b}\right\rbrack \) . Show

\[
\exists \theta  \in  \rbrack a, b\lbrack ,\;f\left( b\right)  - f\left( a\right)  = \frac{b - a}{6}\left\lbrack  {{f}^{\prime }\left( a\right)  + {f}^{\prime }\left( b\right)  + 4{f}^{\prime }\left( \frac{a + b}{2}\right) }\right\rbrack   - \frac{{\left( b - a\right) }^{5}}{2880}{f}^{\left( 5\right) }\left( \theta \right) .
\]

c) (Application.) Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{4} \) . Soit \( n \in {\mathbb{N}}^{ * } \) . On considère la subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{2n} = b \) telle que \( {x}_{i} = a + i\frac{b - a}{2n} \) pour tout \( i \) . Si \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\left( 4\right) }\left( x\right) }\right| \) , montrer

> c) (Application.) Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a map of class \( {\mathcal{C}}^{4} \) . Let \( n \in {\mathbb{N}}^{ * } \) . Consider the subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{2n} = b \) such that \( {x}_{i} = a + i\frac{b - a}{2n} \) for all \( i \) . If \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\left( 4\right) }\left( x\right) }\right| \) , show

\[
\left| {\;{\int }_{a}^{b}f\left( t\right) {dt} - \frac{b - a}{6n}\left\lbrack  {f\left( a\right)  + {4f}\left( {x}_{1}\right)  + {2f}\left( {x}_{2}\right)  + {4f}\left( {x}_{3}\right)  + \cdots }\right. }\right.
\]

\[
\left. {\cdots  + {2f}\left( {x}_{{2n} - 2}\right)  + {4f}\left( {x}_{{2n} - 1}\right)  + f\left( b\right) }\right\rbrack   \leq  \frac{{\left( b - a\right) }^{5}}{{n}^{4}} \cdot  \frac{M}{2880}.
\]

Solution. a) On considère l'application

> Solution. a) Consider the map

\[
\varphi  : \left\lbrack  {-\alpha ,\alpha }\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  g\left( t\right)  - \frac{t}{3}\left( {{g}^{\prime }\left( t\right)  + 2{g}^{\prime }\left( 0\right) }\right)  + \frac{A{t}^{5}}{180},
\]

la constante \( A \) étant choisie telle que \( \varphi \left( \alpha \right) = 0 \) . L’application \( \varphi \) est trois fois dérivable et on a

> the constant \( A \) being chosen such that \( \varphi \left( \alpha \right) = 0 \) . The map \( \varphi \) is three times differentiable and we have

\[
{\varphi }^{\prime }\left( t\right)  = \frac{2}{3}{g}^{\prime }\left( t\right)  - \frac{2}{3}{g}^{\prime }\left( 0\right)  - \frac{t}{3}{g}^{\prime \prime }\left( t\right)  + \frac{{t}^{4}}{36}A,
\]

\[
{\varphi }^{\prime \prime }\left( t\right)  = \frac{1}{3}{g}^{\prime \prime }\left( t\right)  - \frac{t}{3}{g}^{\prime \prime \prime }\left( t\right)  + \frac{{t}^{3}}{9}A,
\]

\[
{\varphi }^{\prime \prime \prime }\left( t\right)  =  - \frac{t}{3}{g}^{\left( 4\right) }\left( t\right)  + \frac{{t}^{2}}{3}A.
\]

Comme \( \varphi \left( 0\right) = \varphi \left( \alpha \right) = 0 \) le théorème de Rolle nous assure l’existence de \( {\alpha }_{1} \in \rbrack 0,\alpha \lbrack \) tel que \( {\varphi }^{\prime }\left( {\alpha }_{1}\right) = 0 \) .

> Since \( \varphi \left( 0\right) = \varphi \left( \alpha \right) = 0 \) Rolle's theorem ensures the existence of \( {\alpha }_{1} \in \rbrack 0,\alpha \lbrack \) such that \( {\varphi }^{\prime }\left( {\alpha }_{1}\right) = 0 \) .

De même, l’égalité \( {\varphi }^{\prime }\left( 0\right) = {\varphi }^{\prime }\left( {\alpha }_{1}\right) = 0 \) entraîne l’existence de \( {\alpha }_{2} \in \rbrack 0,{\alpha }_{1}\left\lbrack \right. \) tel que \( {\varphi }^{\prime \prime }\left( {\alpha }_{2}\right) = 0 \) .

> Similarly, the equality \( {\varphi }^{\prime }\left( 0\right) = {\varphi }^{\prime }\left( {\alpha }_{1}\right) = 0 \) implies the existence of \( {\alpha }_{2} \in \rbrack 0,{\alpha }_{1}\left\lbrack \right. \) such that \( {\varphi }^{\prime \prime }\left( {\alpha }_{2}\right) = 0 \) .

Comme \( g \) est impaire, \( {g}^{\prime \prime } \) est impaire donc \( {g}^{\prime \prime }\left( 0\right) = 0 \) , donc \( {\varphi }^{\prime \prime }\left( 0\right) = {\varphi }^{\prime \prime }\left( {\alpha }_{2}\right) = 0 \) , de sorte qu’il existe \( {\alpha }_{3} \in \rbrack 0,{\alpha }_{2}\left\lbrack \right. \) tel que \( {\varphi }^{\prime \prime \prime }\left( {\alpha }_{3}\right) = 0 \) .

> Since \( g \) is odd, \( {g}^{\prime \prime } \) is odd so \( {g}^{\prime \prime }\left( 0\right) = 0 \) , so \( {\varphi }^{\prime \prime }\left( 0\right) = {\varphi }^{\prime \prime }\left( {\alpha }_{2}\right) = 0 \) , such that there exists \( {\alpha }_{3} \in \rbrack 0,{\alpha }_{2}\left\lbrack \right. \) where \( {\varphi }^{\prime \prime \prime }\left( {\alpha }_{3}\right) = 0 \) .

Finalement, on a trouvé \( {\alpha }_{3} \in \rbrack 0,\alpha \lbrack \) tel que

> Finally, we have found \( {\alpha }_{3} \in \rbrack 0,\alpha \lbrack \) such that

\[
A = \frac{1}{{\alpha }_{3}}{g}^{\left( 4\right) }\left( {\alpha }_{3}\right)  = \frac{{g}^{\left( 4\right) }\left( {\alpha }_{3}\right)  - {g}^{\left( 4\right) }\left( 0\right) }{{\alpha }_{3} - 0}
\]

(on a \( {g}^{\left( 4\right) }\left( 0\right) = 0 \) car \( g \) est impaire), et d’après le théorème des accroissements finis appliqué à \( {g}^{\left( 4\right) } \) , on en déduit l’existence de \( \theta \in \rbrack 0,{\alpha }_{3}\left\lbrack \subset \right\rbrack 0,\alpha \left\lbrack \right. \) tel que \( A = {g}^{\left( 5\right) }\left( \theta \right) \) . Le résultat est ainsi prouvé car \( \varphi \left( \alpha \right) = 0 \) .

> (we have \( {g}^{\left( 4\right) }\left( 0\right) = 0 \) because \( g \) is odd), and by the mean value theorem applied to \( {g}^{\left( 4\right) } \) , we deduce the existence of \( \theta \in \rbrack 0,{\alpha }_{3}\left\lbrack \subset \right\rbrack 0,\alpha \left\lbrack \right. \) such that \( A = {g}^{\left( 5\right) }\left( \theta \right) \) . The result is thus proven because \( \varphi \left( \alpha \right) = 0 \) .

b) On pose \( \alpha = \frac{b - a}{2} \) et \( g : \left\lbrack {-\alpha ,\alpha }\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( {x + \frac{a + b}{2}}\right) - f\left( {-x + \frac{a + b}{2}}\right) \) . Ainsi définie, \( g \) est impaire, et après avoir appliqué à \( g \) le résultat de la question précédente, on obtient

> b) Let \( \alpha = \frac{b - a}{2} \) and \( g : \left\lbrack {-\alpha ,\alpha }\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( {x + \frac{a + b}{2}}\right) - f\left( {-x + \frac{a + b}{2}}\right) \) . Thus defined, \( g \) is odd, and after applying the result of the previous question to \( g \) , we obtain

\[
\exists \theta  \in  \rbrack 0,\frac{b - a}{2}\left\lbrack  {,\;f\left( b\right)  - f\left( a\right)  = \frac{b - a}{6}\left\lbrack  {{f}^{\prime }\left( a\right)  + {f}^{\prime }\left( b\right)  + 4{f}^{\prime }\left( \frac{a + b}{2}\right) }\right\rbrack  }\right.
\]

\[
- \frac{{\left( b - a\right) }^{5}}{{180} \cdot  {2}^{5}}\left\lbrack  {{f}^{\left( 5\right) }\left( {\theta  + \frac{a + b}{2}}\right)  + {f}^{\left( 5\right) }\left( {-\theta  + \frac{a + b}{2}}\right) }\right\rbrack  .
\]

(*)

> L’application \( f \) étant de classe \( {\mathcal{C}}^{5},{f}^{\left( 5\right) } \) est continue donc vérifie la propriété des valeurs in-termédiaires, donc \( {f}^{\left( 5\right) }\left( {\rbrack a, b\lbrack }\right) \) est un intervalle. Comme

The mapping \( f \) being of class \( {\mathcal{C}}^{5},{f}^{\left( 5\right) } \) is continuous, therefore it satisfies the intermediate value property, so \( {f}^{\left( 5\right) }\left( {\rbrack a, b\lbrack }\right) \) is an interval. Since

\[
{f}^{\left( 5\right) }\left( {\theta  + \frac{a + b}{2}}\right)  \in  {f}^{\left( 5\right) }\left( {\rbrack a, b\lbrack }\right) \;\text{ et }\;{f}^{\left( 5\right) }\left( {-\theta  + \frac{a + b}{2}}\right)  \in  {f}^{\left( 5\right) }\left( {\rbrack a, b\lbrack }\right) ,
\]

on en déduit

> we deduce

\[
\frac{1}{2}\left\lbrack  {{f}^{\left( 5\right) }\left( {\theta  + \frac{a + b}{2}}\right)  + {f}^{\left( 5\right) }\left( {-\theta  + \frac{a + b}{2}}\right) }\right\rbrack   \in  {f}^{\left( 5\right) }\left( {\rbrack a, b\lbrack }\right) ,
\]

donc

> therefore

\[
\left. {\exists {\theta }^{\prime } \in  }\right\rbrack  a, b\left\lbrack  {,\;\frac{1}{2}\left\lbrack  {{f}^{\left( 5\right) }\left( {\theta  + \frac{a + b}{2}}\right)  + {f}^{\left( 5\right) }\left( {-\theta  + \frac{a + b}{2}}\right) }\right\rbrack   = {f}^{\left( 5\right) }\left( {\theta }^{\prime }\right) ,}\right.
\]

d'où le résultat avec (*).

> hence the result with (*).

c) En appliquant le résultat de la question précédente à une primitive \( F \) de \( f \) sur \( \left\lbrack {{x}_{{2i} - 2},{x}_{2i}}\right\rbrack \) pour tout \( i \in \{ 1,\ldots , n\} \) , on obtient l’existence de \( {\theta }_{i} \in \rbrack {x}_{{2i} - 2},{x}_{2i}\lbrack \) tel que

> c) By applying the result of the previous question to an antiderivative \( F \) of \( f \) on \( \left\lbrack {{x}_{{2i} - 2},{x}_{2i}}\right\rbrack \) for all \( i \in \{ 1,\ldots , n\} \) , we obtain the existence of \( {\theta }_{i} \in \rbrack {x}_{{2i} - 2},{x}_{2i}\lbrack \) such that

\[
{\int }_{{x}_{{2i} - 2}}^{{x}_{2i}}f\left( t\right) {dt} - \frac{b - a}{6n}\left( {f\left( {x}_{{2i} - 2}\right)  + {4f}\left( {x}_{{2i} - 1}\right)  + f\left( {x}_{2i}\right) }\right)  = \frac{{\left( {x}_{2i} - {x}_{{2i} - 2}\right) }^{5}}{2880}{f}^{\left( 5\right) }\left( {\theta }_{i}\right) ,
\]

done

> therefore

\[
\left| {{\int }_{{x}_{{2i} - 2}}^{{x}_{2i}}f\left( t\right) {dt} - \frac{b - a}{6n}\left( {f\left( {x}_{{2i} - 2}\right)  + {4f}\left( {x}_{{2i} - 1}\right)  + f\left( {x}_{2i}\right) }\right) }\right|  \leq  \frac{{\left( b - a\right) }^{5}}{{2880}{n}^{5}}M.
\]

Il ne reste plus qu'à sommer cette relation sur \( i \) et à utiliser l’inégalité triangulaire pour en déduire le résultat.

> It only remains to sum this relation over \( i \) and use the triangle inequality to deduce the result.

Remarque. Le résultat de la question b) reste vrai si \( f \) est seulement supposée 5 fois dérivable. En effet, le caractère continue de \( {f}^{\left( 5\right) } \) a été utilisé pour montrer que \( {f}^{\left( 5\right) } \) vérifie la propriété des valeurs intermédiaires et on sait d'après le théorème de Darboux (voir l'exercice 4) que ceci est vérifié pour toute fonction dérivée.

> Remark. The result of question b) remains true if \( f \) is only assumed to be 5 times differentiable. Indeed, the continuity of \( {f}^{\left( 5\right) } \) was used to show that \( {f}^{\left( 5\right) } \) satisfies the intermediate value property, and we know from Darboux's theorem (see exercise 4) that this holds for any derivative function.

EXERCICE 6. Soient \( m \geq 2 \) un entier, \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{m} \) et \( n \in {\mathbb{N}}^{ * } \) , \( n < m \) . On suppose qu’il existe un entier \( k, n < k \leq m \) , tel que \( {f}^{\left( k\right) }\left( 0\right) \neq 0 \) . D’après l'égalité de Taylor-Lagrange,

> EXERCISE 6. Let \( m \geq 2 \) be an integer, \( f : \mathbb{R} \rightarrow \mathbb{R} \) a mapping of class \( {\mathcal{C}}^{m} \) and \( n \in {\mathbb{N}}^{ * } \) , \( n < m \) . Suppose there exists an integer \( k, n < k \leq m \) such that \( {f}^{\left( k\right) }\left( 0\right) \neq 0 \) . According to the Taylor-Lagrange equality,

\[
\left. {\forall x \in  \mathbb{R},\exists {\theta }_{x} \in  }\right\rbrack  0,1\lbrack ,\;f\left( x\right)  = f\left( 0\right)  + x{f}^{\prime }\left( 0\right)  + \cdots  + \frac{{x}^{n - 1}}{\left( {n - 1}\right) !}{f}^{\left( n - 1\right) }\left( 0\right)  + \frac{{x}^{n}}{n!}{f}^{\left( n\right) }\left( {{\theta }_{x}x}\right) .
\]

Montrer l’existence et donner la valeur de \( \mathop{\lim }\limits_{\substack{{x \rightarrow 0} \\ {x \neq 0} }}{\theta }_{x} \) .

> Show the existence and give the value of \( \mathop{\lim }\limits_{\substack{{x \rightarrow 0} \\ {x \neq 0} }}{\theta }_{x} \) .

Solution. Les hypothèses vérifiées par \( f \) entraînent l’existence d’un plus petit entier \( p > n \) tel que \( {f}^{\left( p\right) }\left( 0\right) \neq 0 \) . La formule de Taylor-Young appliquée à \( f \) à l’ordre \( p \) donne, lorsque \( x \rightarrow 0 \) ,

> Solution. The hypotheses satisfied by \( f \) imply the existence of a smallest integer \( p > n \) such that \( {f}^{\left( p\right) }\left( 0\right) \neq 0 \) . Taylor-Young's formula applied to \( f \) at order \( p \) gives, as \( x \rightarrow 0 \) ,

\[
f\left( x\right)  = f\left( 0\right)  + x{f}^{\prime }\left( 0\right)  + \cdots  + \frac{{x}^{n}}{n!}{f}^{\left( n\right) }\left( 0\right)  + \frac{{x}^{p}}{p!}{f}^{\left( p\right) }\left( 0\right)  + o\left( {x}^{p}\right) ,
\]

donc

> therefore

\[
\frac{{x}^{n}}{n!}{f}^{\left( n\right) }\left( {{\theta }_{x}x}\right)  = \frac{{x}^{n}}{n!}{f}^{\left( n\right) }\left( 0\right)  + \frac{{x}^{p}}{p!}{f}^{\left( p\right) }\left( 0\right)  + o\left( {x}^{p}\right) ,
\]

donc lorsque \( x \rightarrow 0, x \neq 0 \) ,

> therefore as \( x \rightarrow 0, x \neq 0 \) ,

\[
{f}^{\left( n\right) }\left( {{\theta }_{x}x}\right)  - {f}^{\left( n\right) }\left( 0\right)  = {x}^{p - n}\frac{n!}{p!}{f}^{\left( p\right) }\left( 0\right)  + o\left( {x}^{p - n}\right)  \sim  {x}^{p - n}\frac{n!}{p!}{f}^{\left( p\right) }\left( 0\right) .
\]

(*)

> L’égalité de Taylor-Young appliquée à \( {f}^{\left( n\right) } \) donne, lorsque \( x \rightarrow 0, x \neq 0 \) ,

Taylor-Young's equality applied to \( {f}^{\left( n\right) } \) gives, as \( x \rightarrow 0, x \neq 0 \) ,

\[
{f}^{\left( n\right) }\left( {{\theta }_{x}x}\right)  - {f}^{\left( n\right) }\left( 0\right)  = \frac{{\left( {\theta }_{x}x\right) }^{p - n}}{\left( {p - n}\right) !}{f}^{\left( p\right) }\left( 0\right)  + o\left( {x}^{p - n}\right)  \sim  \frac{{\left( {\theta }_{x}x\right) }^{p - n}}{\left( {p - n}\right) !}{f}^{\left( p\right) }\left( 0\right) .
\]

Avec (*), on en déduit

> With (*), we deduce

\[
\frac{{\left( {\theta }_{x}x\right) }^{p - n}}{\left( {p - n}\right) !}\mathop{\sum }\limits_{\substack{{x \rightarrow  0} \\  {x \neq  0} }}\frac{{x}^{p - n}n!}{p!}\text{ donc }\mathop{\lim }\limits_{\substack{{x \rightarrow  0} \\  {x \neq  0} }}{\theta }_{x} = {\left( \frac{\left( {p - n}\right) !n!}{p!}\right) }^{1/\left( {p - n}\right) } = {\left( {C}_{p}^{n}\right) }^{-1/\left( {p - n}\right) }.
\]

\( \rightarrow \) EXERCICE 7. Soient \( a, b \in \mathbb{R}, a < b \) , et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{n} \) avec \( n \geq 2 \) . On suppose qu’il existe des réels \( {\left( {x}_{i}\right) }_{1 \leq i \leq n}, a \leq {x}_{1} < {x}_{2} < \cdots < {x}_{n} \leq b \) , tels que \( f\left( {x}_{i}\right) = 0 \) pour tout \( i \in \{ 1,\ldots , n\} \) .

> \( \rightarrow \) EXERCISE 7. Let \( a, b \in \mathbb{R}, a < b \) , and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{n} \) class function with \( n \geq 2 \) . Suppose there exist real numbers \( {\left( {x}_{i}\right) }_{1 \leq i \leq n}, a \leq {x}_{1} < {x}_{2} < \cdots < {x}_{n} \leq b \) , such that \( f\left( {x}_{i}\right) = 0 \) for all \( i \in \{ 1,\ldots , n\} \) .

a) Montrer

> a) Show

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\exists u \in  \left\lbrack  {a, b}\right\rbrack  ,\;f\left( x\right)  = \frac{{f}^{\left( n\right) }\left( u\right) }{n!}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {x - {x}_{i}}\right) .
\]

b) Soit \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\left( n\right) }\left( t\right) }\right| \) . Montrer que

> b) Let \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}\left| {{f}^{\left( n\right) }\left( t\right) }\right| \) . Show that

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;\left| {f\left( x\right) }\right|  \leq  \frac{M}{n!}\mathop{\prod }\limits_{{i = 1}}^{n}\left| {x - {x}_{i}}\right| .
\]

c) Montrer que

> c) Show that

\[
\forall i \in  \{ 1,\ldots , n\} ,\;\left| {{f}^{\prime }\left( {x}_{i}\right) }\right|  \leq  \frac{M}{n!}\mathop{\prod }\limits_{{j \neq  i}}\left| {{x}_{i} - {x}_{j}}\right| .
\]

d) Plus généralement, montrer que

> d) More generally, show that

\[
\forall x \in  \left\lbrack  {a, b}\right\rbrack  ,\;\left| {{f}^{\prime }\left( x\right) }\right|  \leq  \frac{M}{n!}\mathop{\sum }\limits_{{i = 1}}^{n}\left( {\mathop{\prod }\limits_{{j \neq  i}}\left| {x - {x}_{j}}\right| }\right) .
\]

Que dire si \( n = 2, a = {x}_{1} \) et \( b = {x}_{2} \) ? Solution. a) S’il existe \( i \) tel que \( x = {x}_{i} \) , c’est terminé. Sinon, on considère l’application

> What can be said if \( n = 2, a = {x}_{1} \) and \( b = {x}_{2} \) ? Solution. a) If there exists \( i \) such that \( x = {x}_{i} \) , we are done. Otherwise, consider the mapping

\[
{\varphi }_{x} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  f\left( t\right)  - A\mathop{\prod }\limits_{{i = 1}}^{n}\left( {t - {x}_{i}}\right) ,
\]

où la constante \( A \) est choisie telle que \( {\varphi }_{x}\left( x\right) = 0 \) . Cette application est de classe \( {\mathcal{C}}^{n} \) et s’annule (au moins) en \( n + 1 \) points distincts \( \left( {x\text{ et les }{\left( {x}_{i}\right) }_{1 \leq i \leq n}}\right) \) . En appliquant le théorème de Rolle, on en déduit que \( {\varphi }_{x}^{\prime } \) s’annule en \( n \) points distincts. En l’appliquant ensuite à \( {\varphi }_{x}^{\prime } \) , on en déduit en \( {\varphi }_{x}^{\prime \prime } \) s’annule en \( n - 1 \) points distincts. En poursuivant ainsi, on s’aperçoit que \( {\varphi }_{x}^{\left( n\right) } \) s’annule en au moins un point \( u \) . On en déduit \( {\varphi }_{x}^{\left( n\right) }\left( u\right) = 0 = {f}^{\left( n\right) }\left( u\right) - {An} \) !, donc \( A = {f}^{\left( n\right) }\left( u\right) /n \) !, et comme \( {\varphi }_{x}\left( x\right) = 0 \) , on en déduit le résultat.

> where the constant \( A \) is chosen such that \( {\varphi }_{x}\left( x\right) = 0 \) . This mapping is of class \( {\mathcal{C}}^{n} \) and vanishes (at least) at \( n + 1 \) distinct points \( \left( {x\text{ et les }{\left( {x}_{i}\right) }_{1 \leq i \leq n}}\right) \) . By applying Rolle's theorem, we deduce that \( {\varphi }_{x}^{\prime } \) vanishes at \( n \) distinct points. By then applying it to \( {\varphi }_{x}^{\prime } \) , we deduce that \( {\varphi }_{x}^{\prime \prime } \) vanishes at \( n - 1 \) distinct points. Continuing in this way, we see that \( {\varphi }_{x}^{\left( n\right) } \) vanishes at at least one point \( u \) . We deduce \( {\varphi }_{x}^{\left( n\right) }\left( u\right) = 0 = {f}^{\left( n\right) }\left( u\right) - {An} \) !, so \( A = {f}^{\left( n\right) }\left( u\right) /n \) !, and since \( {\varphi }_{x}\left( x\right) = 0 \) , we deduce the result.

b) C'est une conséquence immédiate du résultat de la question précédente.

> b) This is an immediate consequence of the result from the previous question.

c) D’après la question précédente, pour tout \( x \neq {x}_{i} \) on a

> c) According to the previous question, for all \( x \neq {x}_{i} \) we have

\[
\left| \frac{f\left( x\right)  - f\left( {x}_{i}\right) }{x - {x}_{i}}\right|  = \left| \frac{f\left( x\right) }{x - {x}_{i}}\right|  \leq  \frac{M}{n!}\mathop{\prod }\limits_{{j \neq  i}}\left| {x - {x}_{j}}\right| ,
\]

d’où le résultat en faisant tendre \( x \) vers \( {x}_{i} \) .

> from which the result follows by letting \( x \) tend to \( {x}_{i} \) .

d) S’il existe \( i \) tel que \( x = {x}_{i} \) , c’est terminé d’après la question précédente. Sinon, nous allons construire une application qui s’annule en \( n \) points dont \( x \) et lui appliquer le résultat de la question c). Posons

> d) If there exists \( i \) such that \( x = {x}_{i} \) , we are done according to the previous question. Otherwise, we will construct a mapping that vanishes at \( n \) points including \( x \) and apply the result of question c) to it. Let us define

\[
{\psi }_{x} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;t \mapsto  f\left( t\right)  - f\left( x\right) \mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( \frac{t - {x}_{i}}{x - {x}_{i}}\right) .
\]

Cette application s’annule aux \( n \) points \( {x}_{1},\ldots ,{x}_{n - 1} \) et \( x \) , donc en lui appliquant c) au point \( x \) , on en déduit

> This mapping vanishes at the \( n \) points \( {x}_{1},\ldots ,{x}_{n - 1} \) and \( x \) , so by applying c) to it at point \( x \) , we deduce

\[
\left| {{\psi }_{x}^{\prime }\left( x\right) }\right|  \leq  \frac{M}{n!}\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left| {x - {x}_{i}}\right|
\]

(car \( {\psi }_{x}^{\left( n\right) } = {f}^{\left( n\right) } \) , donc \( \left| {{\psi }_{x}^{\left( n\right) }\left( x\right) }\right| \leq M \) pour tout \( \left. x\right) \) . Ceci s’écrit aussi

> (since \( {\psi }_{x}^{\left( n\right) } = {f}^{\left( n\right) } \) , therefore \( \left| {{\psi }_{x}^{\left( n\right) }\left( x\right) }\right| \leq M \) for all \( \left. x\right) \) . This is also written

\[
\left| {{f}^{\prime }\left( x\right)  - \frac{f\left( x\right) }{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left( {x - {x}_{i}}\right) }\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {\mathop{\prod }\limits_{\substack{{j \neq  i} \\  {j \neq  n} }}\left( {x - {x}_{j}}\right) }\right) }\right|  \leq  \frac{M}{n!}\mathop{\prod }\limits_{{i \neq  n}}\left| {x - {x}_{i}}\right|
\]

ce qui entraîne

> which implies

\[
\left| {{f}^{\prime }\left( x\right) }\right|  \leq  \frac{\left| f\left( x\right) \right| }{\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left| {x - {x}_{i}}\right| }\left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {\mathop{\prod }\limits_{\substack{{j \neq  i} \\  {j \neq  n} }}\left| {x - {x}_{j}}\right| }\right) }\right\rbrack   + \frac{M}{n!}\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left| {x - {x}_{i}}\right|
\]

\[
\leq  \frac{M}{n!}\left| {x - {x}_{n}}\right| \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}\left( {\mathop{\prod }\limits_{\substack{{j \neq  i} \\  {j \neq  n} }}\left| {x - {x}_{j}}\right| }\right)  + \frac{M}{n!}\mathop{\prod }\limits_{{i = 1}}^{{n - 1}}\left| {x - {x}_{i}}\right|  = \frac{M}{n!}\mathop{\sum }\limits_{{i = 1}}^{n}\left( {\mathop{\prod }\limits_{{j \neq  i}}\left| {x - {x}_{j}}\right| }\right) .
\]

Lorsque \( n = 2,{x}_{1} = a \) et \( {x}_{2} = b \) , ceci s’écrit

> When \( n = 2,{x}_{1} = a \) and \( {x}_{2} = b \) , this is written

\[
\left| {{f}^{\prime }\left( x\right) }\right|  \leq  \frac{M}{2}\left\lbrack  {\left( {x - a}\right)  + \left( {b - x}\right) }\right\rbrack   = M\frac{b - a}{2}.
\]

EXERCICE 8. Soient \( n \geq 2 \) un entier et \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{n} \) . Pour tout entier \( k,0 \leq k \leq n \) , on note \( {M}_{k} = \mathop{\sup }\limits_{{t \in \mathbb{R}}}\left| {{f}^{\left( k\right) }\left( t\right) }\right| \in {\mathbb{R}}^{ + } \cup \{ + \infty \} \) . On suppose que \( {M}_{0} \) et \( {M}_{n} \) ont des valeurs finies.

> EXERCISE 8. Let \( n \geq 2 \) be an integer and \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{n} \) class mapping. For any integer \( k,0 \leq k \leq n \) , we denote \( {M}_{k} = \mathop{\sup }\limits_{{t \in \mathbb{R}}}\left| {{f}^{\left( k\right) }\left( t\right) }\right| \in {\mathbb{R}}^{ + } \cup \{ + \infty \} \) . Suppose that \( {M}_{0} \) and \( {M}_{n} \) have finite values.

a) Montrer que pour tout entier \( k,0 < k < n,{M}_{k} \) a une valeur finie.

> a) Show that for any integer \( k,0 < k < n,{M}_{k} \) has a finite value.

b) Montrer que si \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\left( n\right) }\left( t\right) = 0 \) , alors \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\left( k\right) }\left( t\right) = 0 \) pour tout entier \( k \) tel que \( 0 < k < n \) .

> b) Show that if \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\left( n\right) }\left( t\right) = 0 \) , then \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\left( k\right) }\left( t\right) = 0 \) for any integer \( k \) such that \( 0 < k < n \) .

c) Montrer que pour tout entier \( m,1 \leq m \leq n \) , et pour tout entier \( k,0 \leq k \leq m \) ,

> c) Show that for any integer \( m,1 \leq m \leq n \) , and for any integer \( k,0 \leq k \leq m \) ,

\[
{M}_{k} \leq  {2}^{k\left( {m - k}\right) /2}{M}_{0}^{1 - k/m}{M}_{m}^{k/m}.
\]

(Indication. On pourra commencer par montrer que \( {M}_{1} \leq \sqrt{2{M}_{0}{M}_{2}} \) .)

> (Hint. One may start by showing that \( {M}_{1} \leq \sqrt{2{M}_{0}{M}_{2}} \) .)

Solution. a) Soit \( x \in \mathbb{R} \) . Pour tout \( i \in \{ 1,\ldots , n - 1\} \) , il existe d’après le théorème de Taylor-Lagrange \( \left. {{\theta }_{i, x} \in }\right\rbrack 0, i\lbrack \) tel que

> Solution. a) Let \( x \in \mathbb{R} \) . For any \( i \in \{ 1,\ldots , n - 1\} \) , there exists by the Taylor-Lagrange theorem \( \left. {{\theta }_{i, x} \in }\right\rbrack 0, i\lbrack \) such that

\[
f\left( {x + i}\right)  = f\left( x\right)  + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{i}^{k}\frac{{f}^{\left( k\right) }\left( x\right) }{k!} + {i}^{n}\frac{{f}^{\left( n\right) }\left( {x + {\theta }_{i, x}}\right) }{n!},
\]

ce qui, en posant

> which, by setting

\[
{X}_{i}\left( x\right)  = f\left( {x + i}\right)  - f\left( x\right)  - \frac{{i}^{n}}{n!}{f}^{\left( n\right) }\left( {x + {\theta }_{i, x}}\right) \;\text{ et }\;{Y}_{k}\left( x\right)  = \frac{{f}^{\left( k\right) }\left( x\right) }{k!}
\]

s’écrit \( {X}_{i}\left( x\right) = \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{i}^{k}{Y}_{k}\left( x\right) \) . En notant \( X\left( x\right) \) (resp. \( Y\left( x\right) \) ) le vecteur colonne de \( {\mathbb{R}}^{n - 1} \) dont les composantes sont les \( {X}_{i}\left( x\right) \) (resp. \( {Y}_{i}\left( x\right) \) ), ceci s’écrit matriciellement \( X\left( x\right) = {MY}\left( x\right) \) avec

> is written \( {X}_{i}\left( x\right) = \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{i}^{k}{Y}_{k}\left( x\right) \) . By denoting \( X\left( x\right) \) (resp. \( Y\left( x\right) \) ) the column vector of \( {\mathbb{R}}^{n - 1} \) whose components are the \( {X}_{i}\left( x\right) \) (resp. \( {Y}_{i}\left( x\right) \) ), this is written in matrix form \( X\left( x\right) = {MY}\left( x\right) \) with

\[
M = \left( \begin{matrix} 1 & 1 & \cdots & 1 \\  2 & {2}^{2} & \cdots & {2}^{n - 1} \\  3 & {3}^{2} & \cdots & {3}^{n - 1} \\  \vdots & \vdots & & \vdots \\  \left( {n - 1}\right) & {\left( n - 1\right) }^{2} & \cdots & {\left( n - 1\right) }^{n - 1} \end{matrix}\right)
\]

On a \( \det \left( M\right) = \) Vandermonde \( \left( {1,2,\ldots , n - 1}\right) \neq 0 \) , donc \( M \) est inversible. L’application linéaire \( {\mathbb{R}}^{n - 1} \rightarrow {\mathbb{R}}^{n - 1}\;X \mapsto {M}^{-1}X \) est continue (on est en dimension finie) donc il existe \( A > 0 \) tel que \( \begin{Vmatrix}{{M}^{-1}X}\end{Vmatrix} \leq A\parallel X\parallel \) pour tout \( X \in {\mathbb{R}}^{n - 1} \) . Les hypothèses sur \( f \) entraînent que \( x \mapsto X\left( x\right) \) est bornée, et comme \( \parallel Y\left( x\right) \parallel = \begin{Vmatrix}{{M}^{-1}X\left( x\right) }\end{Vmatrix} \leq A\parallel X\left( x\right) \parallel \) , on en déduit que \( x \mapsto Y\left( x\right) \) est bornée, ce qu'il fallait démontrer.

> We have \( \det \left( M\right) = \) Vandermonde \( \left( {1,2,\ldots , n - 1}\right) \neq 0 \) , so \( M \) is invertible. The linear map \( {\mathbb{R}}^{n - 1} \rightarrow {\mathbb{R}}^{n - 1}\;X \mapsto {M}^{-1}X \) is continuous (we are in finite dimension) so there exists \( A > 0 \) such that \( \begin{Vmatrix}{{M}^{-1}X}\end{Vmatrix} \leq A\parallel X\parallel \) for all \( X \in {\mathbb{R}}^{n - 1} \) . The hypotheses on \( f \) imply that \( x \mapsto X\left( x\right) \) is bounded, and since \( \parallel Y\left( x\right) \parallel = \begin{Vmatrix}{{M}^{-1}X\left( x\right) }\end{Vmatrix} \leq A\parallel X\left( x\right) \parallel \) , we deduce that \( x \mapsto Y\left( x\right) \) is bounded, which was to be demonstrated.

b) Comme \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\parallel X\left( x\right) \parallel = 0 \) , et que \( \parallel Y\left( x\right) \parallel \leq A\parallel X\left( x\right) \parallel \) , on en déduit \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\parallel Y\left( x\right) \parallel = 0 \) . c) Comme indiqué, nous commençons par montrer

> b) Since \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\parallel X\left( x\right) \parallel = 0 \) , and \( \parallel Y\left( x\right) \parallel \leq A\parallel X\left( x\right) \parallel \) , we deduce \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}\parallel Y\left( x\right) \parallel = 0 \) . c) As indicated, we begin by showing

\[
{M}_{1} \leq  \sqrt{2{M}_{0}{M}_{2}}
\]

(**)

> Soit \( x \in \mathbb{R} \) . Pour tout \( h > 0 \) ,

Let \( x \in \mathbb{R} \) . For all \( h > 0 \) ,

\[
\left\{  \begin{array}{ll} \exists {\theta }_{1} \in  \rbrack 0,1\lbrack & f\left( {x + h}\right)  = f\left( x\right)  + h{f}^{\prime }\left( x\right)  + \frac{{h}^{2}}{2}{f}^{\prime \prime }\left( {x + {\theta }_{1}h}\right) \\  \left. {\exists {\theta }_{2} \in  \rbrack 0,1\lbrack }\right\rbrack  & f\left( {x - h}\right)  = f\left( x\right)  - h{f}^{\prime }\left( x\right)  + \frac{{h}^{2}}{2}{f}^{\prime \prime }\left( {x - {\theta }_{2}h}\right)  \end{array}\right.
\]

Ceci entraîne

> This implies

\[
{f}^{\prime }\left( x\right)  = \frac{f\left( {x + h}\right)  - f\left( {x - h}\right) }{2h} + \frac{h}{4}\left\lbrack  {{f}^{\prime \prime }\left( {x - {\theta }_{2}h}\right)  - {f}^{\prime \prime }\left( {x + {\theta }_{1}h}\right) }\right\rbrack  ,
\]

donc

> therefore

\[
\left| {{f}^{\prime }\left( x\right) }\right|  \leq  \frac{2{M}_{0}}{2h} + \frac{h}{4}2{M}_{2} = \frac{{M}_{0}}{h} + \frac{h}{2}{M}_{2}.
\]

Ceci est vrai pour tout \( h > 0 \) . On va donc choisir \( h \) tel que \( \frac{{M}_{0}}{h} + \frac{h}{2}{M}_{2} \) soit minimal. Une rapide étude de la fonction \( \psi : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}, h \mapsto \frac{{M}_{0}}{h} + \frac{h}{2}{M}_{2} \) montre qu’elle atteint son minimum pour \( h = \sqrt{\frac{2{M}_{0}}{{M}_{2}}} \) , point en lequel elle vaut \( \sqrt{2{M}_{0}{M}_{2}} \) . Cette majoration étant vraie pour tout \( x \) , on en déduit (**).

> This is true for all \( h > 0 \) . We will therefore choose \( h \) such that \( \frac{{M}_{0}}{h} + \frac{h}{2}{M}_{2} \) is minimal. A quick study of the function \( \psi : {\mathbb{R}}^{ + } \rightarrow \mathbb{R}, h \mapsto \frac{{M}_{0}}{h} + \frac{h}{2}{M}_{2} \) shows that it reaches its minimum at \( h = \sqrt{\frac{2{M}_{0}}{{M}_{2}}} \) , point at which it is equal to \( \sqrt{2{M}_{0}{M}_{2}} \) . Since this upper bound is true for all \( x \) , we deduce (**).

Montrons maintenant le résultat demandé. Nous procédons par récurrence sur \( m \) . Si \( m = 1 \) , c'est évident, et le cas \( m = 2 \) est une conséquence de (**). Supposons le résultat vrai jus-qu’au rang \( m \) et montrons le au rang \( m + 1 \) . En appliquant (**) à \( {f}^{\left( m - 1\right) } \) , on obtient \( {M}_{m} \leq \; \sqrt{2{M}_{m - 1}{M}_{m + 1}} \) . Or \( {M}_{m - 1} \leq {2}^{\left( {m - 1}\right) /2}{M}_{0}^{1/m}{M}_{m}^{\left( {m - 1}\right) /m} \) , donc

> Let us now show the requested result. We proceed by induction on \( m \) . If \( m = 1 \) , it is obvious, and the case \( m = 2 \) is a consequence of (**). Assume the result is true up to rank \( m \) and show it for rank \( m + 1 \) . By applying (**) to \( {f}^{\left( m - 1\right) } \) , we obtain \( {M}_{m} \leq \; \sqrt{2{M}_{m - 1}{M}_{m + 1}} \) . However \( {M}_{m - 1} \leq {2}^{\left( {m - 1}\right) /2}{M}_{0}^{1/m}{M}_{m}^{\left( {m - 1}\right) /m} \) , therefore

\[
{M}_{m}^{2} \leq  2{M}_{m - 1}{M}_{m + 1} \leq  {2}^{\left( {m + 1}\right) /2}{M}_{0}^{1/m}{M}_{m}^{\left( {m - 1}\right) /m}{M}_{m + 1}.
\]

Si \( {M}_{m} = 0 \) , alors \( f \) est polynomiale de degré \( < m \) et la propriété est trivialement vérifiée au rang \( m + 1 \) . Sinon la dernière inégalité entraîne

> If \( {M}_{m} = 0 \) , then \( f \) is polynomial of degree \( < m \) and the property is trivially verified at rank \( m + 1 \) . Otherwise the last inequality implies

\[
{M}_{m}^{1 + 1/m} \leq  {2}^{\left( {m + 1}\right) /2}{M}_{0}^{1/m}{M}_{m + 1}.
\]

\( \left( {* * * }\right) \)

> Soit \( k,0 \leq k \leq m + 1 \) . Si \( k = m + 1 \) , le résultat est évident, sinon d’après l’hypothèse de récurrence,

Let \( k,0 \leq k \leq m + 1 \) . If \( k = m + 1 \) , the result is obvious, otherwise according to the induction hypothesis,

\[
{M}_{k} \leq  {2}^{k\left( {m - k}\right) /2}{M}_{0}^{1 - k/m}{M}_{m}^{k/m},
\]

et en élevant (***) à la puissance \( k/\left( {m + 1}\right) \) puis en remplaçant dans cette dernière inégalité, on obtient

> and by raising (***) to the power \( k/\left( {m + 1}\right) \) then substituting into this last inequality, we obtain

\[
{M}_{k} \leq  {2}^{k\left( {m + 1 - k}\right) /2}{M}_{0}^{1 - k/\left( {m + 1}\right) }{M}_{m + 1}^{k/m + 1},
\]

d'où le résultat.

> hence the result.

EXERCICE 9 (UNE FONCTION CONTINUE, NULLE PART DÉRIVABLE). On note \( \Delta \) la fonction définie sur \( \mathbb{R} \) ,1-périodique, dont la restriction à \( \left\lbrack {-1/2,1/2}\right\rbrack \) vérifie \( \Delta \left( x\right) = \left| x\right| \) . Montrer que la fonction

> EXERCISE 9 (A CONTINUOUS, NOWHERE DIFFERENTIABLE FUNCTION). Let \( \Delta \) be the function defined on \( \mathbb{R} \) ,1-periodic, whose restriction to \( \left\lbrack {-1/2,1/2}\right\rbrack \) satisfies \( \Delta \left( x\right) = \left| x\right| \) . Show that the function

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{1}{{2}^{p}}\Delta \left( {{2}^{p}x}\right)
\]

est continue mais n’est dérivable en aucun point de \( \mathbb{R} \) .

> is continuous but is not differentiable at any point of \( \mathbb{R} \) .

Solution. Pour tout \( x \in \mathbb{R} \) , on a \( \left| {\Delta \left( x\right) }\right| \leq 1/2 \) donc la série de fonctions \( \sum \frac{1}{{2}^{p}}\Delta \left( {{2}^{p}x}\right) \) converge normalement sur \( \mathbb{R} \) . Ainsi, \( f \) est bien définie sur \( \mathbb{R} \) , et comme \( \Delta \) est continue, \( f \) est aussi continue.

> Solution. For all \( x \in \mathbb{R} \) , we have \( \left| {\Delta \left( x\right) }\right| \leq 1/2 \) so the series of functions \( \sum \frac{1}{{2}^{p}}\Delta \left( {{2}^{p}x}\right) \) converges normally on \( \mathbb{R} \) . Thus, \( f \) is well-defined on \( \mathbb{R} \) , and since \( \Delta \) is continuous, \( f \) is also continuous.

Montrons maintenant que \( f \) n’est dérivable en aucun point de \( \mathbb{R} \) . Comme \( f \) est 1-périodique, il suffit de montrer que \( f \) n’est dérivable en aucun point de \( \lbrack 0,1\lbrack \) . Soit \( {x}_{0} \in \lbrack 0,1\lbrack \) . On considère l’écriture diadique de \( {x}_{0} : {x}_{0} = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{\varepsilon }_{k}}{{2}^{k}} \) , où \( {\varepsilon }_{k} \in \{ 0,1\} \) pour tout \( k \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on pose

> Let us now show that \( f \) is not differentiable at any point of \( \mathbb{R} \) . Since \( f \) is 1-periodic, it suffices to show that \( f \) is not differentiable at any point of \( \lbrack 0,1\lbrack \) . Let \( {x}_{0} \in \lbrack 0,1\lbrack \) . Consider the dyadic representation of \( {x}_{0} : {x}_{0} = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{\varepsilon }_{k}}{{2}^{k}} \) , where \( {\varepsilon }_{k} \in \{ 0,1\} \) for all \( k \) . For all \( n \in {\mathbb{N}}^{ * } \) , we set

\[
{x}_{n}^{\prime } = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{\varepsilon }_{k}}{{2}^{k}}\;\text{ et }\;{x}_{n}^{\prime \prime } = {x}_{n}^{\prime } + \frac{1}{{2}^{n}}.
\]

Les suites \( \left( {x}_{n}^{\prime }\right) \) et \( \left( {x}_{n}^{\prime \prime }\right) \) tendent vers \( {x}_{0} \) . Lorsque \( p \geq n \) , les nombres \( {2}^{p}{x}_{n}^{\prime } \) et \( {2}^{p}{x}_{n}^{\prime \prime } \) sont des entiers, donc \( \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right) = \Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right) = 0 \) . Maintenant, si \( p < n \) , on a

> The sequences \( \left( {x}_{n}^{\prime }\right) \) and \( \left( {x}_{n}^{\prime \prime }\right) \) tend to \( {x}_{0} \) . When \( p \geq n \) , the numbers \( {2}^{p}{x}_{n}^{\prime } \) and \( {2}^{p}{x}_{n}^{\prime \prime } \) are integers, so \( \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right) = \Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right) = 0 \) . Now, if \( p < n \) , we have

\[
{2}^{p}{x}_{n}^{\prime } = N + \mathop{\sum }\limits_{{k = p + 1}}^{n}\frac{{\varepsilon }_{k}}{{2}^{k - p}}\text{ où }N = \mathop{\sum }\limits_{{k = 1}}^{p}{2}^{p - k}{\varepsilon }_{k}\;\text{ est un entier, }
\]

donc

> therefore

\[
\Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right)  = \Delta \left( {\mathop{\sum }\limits_{{k = p + 1}}^{n}\frac{{\varepsilon }_{k}}{{2}^{k - p}}}\right) ,\;\text{ et de même }\;\Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right)  = \Delta \left( {\mathop{\sum }\limits_{{k = p + 1}}^{n}\frac{{\varepsilon }_{k}}{{2}^{k - p}} + \frac{1}{{2}^{n - p}}}\right) .
\]

(*)

> Si \( {\varepsilon }_{p + 1} = 0 \) , l’encadrement

If \( {\varepsilon }_{p + 1} = 0 \) , the inequality

\[
0 \leq  \mathop{\sum }\limits_{{k = p + 1}}^{n}\frac{{\varepsilon }_{k}}{{2}^{k - p}} + \frac{1}{{2}^{n - p}} \leq  \mathop{\sum }\limits_{{k = p + 2}}^{n}\frac{1}{{2}^{k - p}} + \frac{1}{{2}^{n - p}} = \frac{1}{2}
\]

montre que dans (*), les valeurs de \( \Delta \) sont prises sur un intervalle où \( \Delta \) croit, et étant donnée la forme de \( \Delta \) , on en déduit finalement

> shows that in (*), the values of \( \Delta \) are taken on an interval where \( \Delta \) is increasing, and given the form of \( \Delta \) , we finally deduce

\[
\text{ si }{\varepsilon }_{p + 1} = 0,\;\Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right)  - \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right)  = {2}^{p}\left( {{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }}\right)  = \frac{1}{{2}^{n - p}}\text{ . }
\]

On montrerait de même

> We would show similarly

\[
\text{ si }{\varepsilon }_{p + 1} = 1,\;\Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right)  - \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right)  =  - \frac{1}{{2}^{n - p}}\text{ . }
\]

En résumé, on a \( \Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right) - \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right) = {\left( -1\right) }^{{\varepsilon }_{p + 1}}/{2}^{n - p} \) pour \( 0 \leq p < n \) , donc finalement

> In summary, we have \( \Delta \left( {{2}^{p}{x}_{n}^{\prime \prime }}\right) - \Delta \left( {{2}^{p}{x}_{n}^{\prime }}\right) = {\left( -1\right) }^{{\varepsilon }_{p + 1}}/{2}^{n - p} \) for \( 0 \leq p < n \) , so finally

\[
f\left( {x}_{n}^{\prime \prime }\right)  - f\left( {x}_{n}^{\prime }\right)  = \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}\frac{{\left( -1\right) }^{{\varepsilon }_{p + 1}}}{{2}^{n}}\;\text{ ou encore }\;\frac{f\left( {x}_{n}^{\prime \prime }\right)  - f\left( {x}_{n}^{\prime }\right) }{{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }} = \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}{\left( -1\right) }^{{\varepsilon }_{p + 1}},
\]

ce qui montre que la suite \( \left( {y}_{n}\right) \) définie par \( {y}_{n} = \frac{f\left( {x}_{n}^{\prime \prime }\right) - f\left( {x}_{n}^{\prime }\right) }{{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }} \) ne converge pas. Si maintenant \( f \) est dérivable en \( {x}_{0} \) , on a

> which shows that the sequence \( \left( {y}_{n}\right) \) defined by \( {y}_{n} = \frac{f\left( {x}_{n}^{\prime \prime }\right) - f\left( {x}_{n}^{\prime }\right) }{{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }} \) does not converge. If now \( f \) is differentiable at \( {x}_{0} \) , we have

\[
f\left( {x}_{n}^{\prime }\right)  - f\left( {x}_{0}\right)  = \left( {{x}_{n}^{\prime } - {x}_{0}}\right) \left\lbrack  {{f}^{\prime }\left( {x}_{0}\right)  + {\varepsilon }_{n}^{\prime }}\right\rbrack  \;\text{ et }\;f\left( {x}_{n}^{\prime \prime }\right)  - f\left( {x}_{0}\right)  = \left( {{x}_{n}^{\prime \prime } - {x}_{0}}\right) \left\lbrack  {{f}^{\prime }\left( {x}_{0}\right)  + {\varepsilon }_{n}^{\prime \prime }}\right\rbrack
\]

où les suites \( \left( {\varepsilon }_{n}^{\prime }\right) \) et \( \left( {\varepsilon }_{n}^{\prime \prime }\right) \) tendent vers0. Par différence, on a

> where the sequences \( \left( {\varepsilon }_{n}^{\prime }\right) \) and \( \left( {\varepsilon }_{n}^{\prime \prime }\right) \) tend to 0. By subtraction, we have

\[
f\left( {x}_{n}^{\prime \prime }\right)  - f\left( {x}_{n}^{\prime }\right)  = \left( {{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }}\right) {f}^{\prime }\left( {x}_{0}\right)  + \left( {{x}_{0} - {x}_{n}^{\prime }}\right) {\varepsilon }_{n}^{\prime } + \left( {{x}_{n}^{\prime \prime } - {x}_{0}}\right) {\varepsilon }_{n}^{\prime \prime },
\]

et comme \( {x}_{n}^{\prime } \leq {x}_{0} \leq {x}_{n}^{\prime \prime } \) , ceci entraîne

> and since \( {x}_{n}^{\prime } \leq {x}_{0} \leq {x}_{n}^{\prime \prime } \) , this implies

\[
\left| {f\left( {x}_{n}^{\prime \prime }\right)  - f\left( {x}_{n}^{\prime }\right)  - \left( {{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }}\right) {f}^{\prime }\left( {x}_{0}\right) }\right|  \leq  \left( {{x}_{n}^{\prime \prime } - {x}_{n}^{\prime }}\right) \left( {{\varepsilon }_{n}^{\prime } + {\varepsilon }_{n}^{\prime \prime }}\right) \;\text{ donc }\;\left| {{y}_{n} - {f}^{\prime }\left( {x}_{0}\right) }\right|  \leq  {\varepsilon }_{n}^{\prime } + {\varepsilon }_{n}^{\prime \prime },
\]

donc \( \left( {y}_{n}\right) \) converge vers \( {f}^{\prime }\left( {x}_{0}\right) \) , ce qui est contradictoire. Donc \( f \) n’est pas dérivable en \( {x}_{0} \) , d’où le résultat.

> therefore \( \left( {y}_{n}\right) \) converges to \( {f}^{\prime }\left( {x}_{0}\right) \) , which is contradictory. Thus \( f \) is not differentiable at \( {x}_{0} \) , hence the result.

Remarque. Une méthode non constructive de la preuve de l'existence d'une fonction continue jamais dérivable est donnée à l'exercice 4 page 421.

> Remark. A non-constructive method for proving the existence of a continuous function that is nowhere differentiable is given in exercise 4 on page 421.
