#### 5.5. Exercises

*Français : 5.5. Exercices*

EXERCICE 1. Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) la fonction \( {2\pi } \) -périodique égale à \( 1 - {x}^{2}/{\pi }^{2} \) sur \( \left\lbrack {-\pi ,\pi }\right\rbrack \) . Calculer les coefficients de Fourier de \( f \) . En déduire les valeurs de

> EXERCISE 1. Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be the \( {2\pi } \) -periodic function equal to \( 1 - {x}^{2}/{\pi }^{2} \) on \( \left\lbrack {-\pi ,\pi }\right\rbrack \) . Calculate the Fourier coefficients of \( f \) . Deduce the values of

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{2}},\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{\left( 2n - 1\right) }^{2}},\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{4}}.
\]

Solution. La fonction \( f \) est paire. Les coefficients \( {b}_{n} = {b}_{n}\left( f\right) \) sont donc nuls. Par ailleurs,

> Solution. The function \( f \) is even. The coefficients \( {b}_{n} = {b}_{n}\left( f\right) \) are therefore zero. Furthermore,

\[
{a}_{0} = {a}_{0}\left( f\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }\left( {1 - \frac{{t}^{2}}{{\pi }^{2}}}\right) {dt} = \frac{4}{3}
\]

et

\[
\forall n \in  {\mathbb{N}}^{ * },\;{a}_{n} = {a}_{n}\left( f\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }\left( {1 - \frac{{t}^{2}}{{\pi }^{2}}}\right) \cos {ntdt} =  - \frac{2}{{\pi }^{3}}{\int }_{0}^{\pi }{t}^{2}\cos {ntdt} = {\left( -1\right) }^{n + 1}\frac{4}{{n}^{2}{\pi }^{2}}
\]

(après une double intégration par parties).

> (after a double integration by parts).

La fonction \( f \) est continue et \( {\mathcal{C}}^{1} \) par morceaux. Sa série de Fourier converge donc simplement (et même uniformément) vers \( f \) , ce qui s’écrit

> The function \( f \) is continuous and piecewise \( {\mathcal{C}}^{1} \) . Its Fourier series therefore converges simply (and even uniformly) to \( f \) , which is written

\[
\forall x \in  \left\lbrack  {-\pi ,\pi }\right\rbrack  ,\;f\left( x\right)  = 1 - \frac{{x}^{2}}{{\pi }^{2}} = \frac{{a}_{0}}{2} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{a}_{n}\cos {nx} = \frac{2}{3} - \frac{4}{{\pi }^{2}}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\frac{\cos {nx}}{{n}^{2}}.
\]

(*)

> - En faisant \( x = \pi \) dans (*), on trouve

- By setting \( x = \pi \) in (*), we find

\[
0 = \frac{2}{3} - \frac{4}{{\pi }^{2}}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{2}}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{2}} = \frac{{\pi }^{2}}{6}.
\]

- En faisant \( x = 0 \) dans (*), on trouve

> - By setting \( x = 0 \) in (*), we find

\[
1 = \frac{2}{3} - \frac{4}{{\pi }^{2}}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{n}^{2}}\text{ d’où }\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{n}^{2}} =  - \frac{{\pi }^{2}}{12},
\]

donc

> therefore

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{\left( 2n - 1\right) }^{2}} = \frac{1}{2}\left( {\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{2}} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{n}^{2}}}\right)  = \frac{1}{2}\left( {\frac{{\pi }^{2}}{6} + \frac{{\pi }^{2}}{12}}\right)  = \frac{{\pi }^{2}}{8}.
\]

— Enfin l'égalité de Parseval s'écrit

> — Finally, Parseval's identity is written

\[
\frac{4}{9} + \frac{1}{2}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{16}{{n}^{4}{\pi }^{4}} = \frac{8}{15}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{4}} = \frac{{\pi }^{4}}{90}.
\]

EXERCICE 2. Soit \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Z} \) . On désigne par \( {f}_{\alpha } \) l’application \( {2\pi } \) -périodique sur \( \mathbb{R} \) telle que

> EXERCISE 2. Let \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Z} \) . We denote by \( {f}_{\alpha } \) the \( {2\pi } \) -periodic mapping on \( \mathbb{R} \) such that

\[
\forall t \in  \rbrack  - \pi ,\pi \rbrack ,\;{f}_{\alpha }\left( t\right)  = \cos {\alpha t}
\]

a) Calculer la série de Fourier de \( {f}_{\alpha } \) . En déduire

> a) Calculate the Fourier series of \( {f}_{\alpha } \) . Deduce

\[
\forall t \in  \mathbb{R} \smallsetminus  \pi \mathbb{Z},\;\operatorname{cotan}t = \frac{1}{t} + {2t}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{t}^{2} - {n}^{2}{\pi }^{2}}.
\]

b) Montrer alors

> b) Then show

\[
\forall t \in  \rbrack  - \pi ,\pi \lbrack ,\;\sin t = t\mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left( {1 - \frac{{t}^{2}}{{n}^{2}{\pi }^{2}}}\right) \;\left( {\text{ où }\mathop{\prod }\limits_{{n = 1}}^{\infty } = \mathop{\lim }\limits_{{N \rightarrow   + \infty }}\mathop{\prod }\limits_{{n = 1}}^{N}}\right) .
\]

c) Montrer

> c) Show

\[
\forall t \in  \rbrack  - \pi ,\pi \lbrack , t \neq  0,\;\frac{1}{{\sin }^{2}t} = \mathop{\sum }\limits_{{-\infty }}^{{+\infty }}\frac{1}{{\left( t - n\pi \right) }^{2}}.
\]

Solution. a) L’application \( {f}_{\alpha } \) est paire donc \( {b}_{n}\left( {f}_{\alpha }\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Par ailleurs,

> Solution. a) The mapping \( {f}_{\alpha } \) is even, therefore \( {b}_{n}\left( {f}_{\alpha }\right) = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) . Furthermore,

\[
\forall n \in  \mathbb{N},\;{a}_{n}\left( {f}_{\alpha }\right)  = \frac{1}{\pi }{\int }_{-\pi }^{\pi }\cos {\alpha t}\cos {ntdt} = \frac{1}{\pi }{\int }_{0}^{\pi }\left\lbrack  {\cos \left( {\alpha  + n}\right) t + \cos \left( {\alpha  - n}\right) t}\right\rbrack  {dt}
\]

\[
= \frac{1}{\pi }\left\lbrack  {\frac{\sin \left( {\alpha  + n}\right) \pi }{\alpha  + n} + \frac{\sin \left( {\alpha  - n}\right) \pi }{\alpha  - n}}\right\rbrack   = {\left( -1\right) }^{n}\frac{{2\alpha }\sin {\alpha \pi }}{\pi \left( {{\alpha }^{2} - {n}^{2}}\right) }.
\]

La fonction \( {f}_{\alpha } \) est continue et de classe \( {\mathcal{C}}^{1} \) par morceaux, donc la série de Fourier de \( {f}_{\alpha } \) converge simplement (et même uniformément) vers \( {f}_{\alpha } \) sur \( \mathbb{R} \) , ce qui entraîne

> The function \( {f}_{\alpha } \) is continuous and piecewise \( {\mathcal{C}}^{1} \) , so the Fourier series of \( {f}_{\alpha } \) converges pointwise (and even uniformly) to \( {f}_{\alpha } \) on \( \mathbb{R} \) , which implies

\[
\forall t \in  \left\lbrack  {-\pi ,\pi }\right\rbrack  ,\;\cos {\alpha t} = \frac{\sin {\alpha t}}{\alpha \pi } + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\frac{{2\alpha }\sin {\alpha \pi }}{\pi \left( {{\alpha }^{2} - {n}^{2}}\right) }\cos {nt},
\]

ce qui en faisant \( t = \pi \) et en divisant par \( \sin {\alpha \pi } \) donne

> which, by setting \( t = \pi \) and dividing by \( \sin {\alpha \pi } \) , gives

\[
\operatorname{cotan}{\alpha \pi } = \frac{1}{\alpha \pi } + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{2\alpha }{\pi \left( {{\alpha }^{2} - {n}^{2}}\right) }.
\]

Ceci est vrai pour tout \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Z} \) , d’où le résultat en remplaçant \( \alpha \) par \( t/\pi \) .

> This is true for all \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Z} \) , hence the result by replacing \( \alpha \) with \( t/\pi \) .

b) Soit \( x \in \rbrack 0,\pi \left\lbrack \right. \) . On définit \( f : \left\lbrack {0, x}\right\rbrack \rightarrow \mathbb{R} \) par \( f\left( t\right) = \operatorname{cotan}t - 1/t \) si \( t \neq 0, f\left( 0\right) = 0 \) . La formule établie à la question précédente montre que

> b) Let \( x \in \rbrack 0,\pi \left\lbrack \right. \) . We define \( f : \left\lbrack {0, x}\right\rbrack \rightarrow \mathbb{R} \) by \( f\left( t\right) = \operatorname{cotan}t - 1/t \) if \( t \neq 0, f\left( 0\right) = 0 \) . The formula established in the previous question shows that

\[
\forall t \in  \left\lbrack  {0, x}\right\rbrack  ,\;f\left( t\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}.
\]

Comme cette série de fonctions converge normalement sur \( \left\lbrack {0, x}\right\rbrack \) , on peut écrire

> Since this series of functions converges normally on \( \left\lbrack {0, x}\right\rbrack \) , we can write

\[
{\int }_{0}^{x}f\left( t\right) {dt} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\int }_{0}^{x}\frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}\text{ autrement dit }\log \frac{\sin x}{x} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\log \left( {1 - \frac{{x}^{2}}{{n}^{2}{\pi }^{2}}}\right) .
\]

En prenant l'exponentielle de part et d'autre de cette dernière égalité, on voit que le produit infini existe bien et que

> By taking the exponential on both sides of this last equality, we see that the infinite product indeed exists and that

\[
\frac{\sin x}{x} = \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left( {1 - \frac{{x}^{2}}{{n}^{2}{\pi }^{2}}}\right) ,
\]

d’où le résultat pour \( 0 < x < \pi \) . Comme les fonctions en présence sont impaires et nulles en0, on en déduit le résultat pour tout \( x \in \rbrack - \pi ,\pi \lbrack \) .

> whence the result for \( 0 < x < \pi \) . As the functions involved are odd and zero at 0, we deduce the result for all \( x \in \rbrack - \pi ,\pi \lbrack \) .

c) L'égalité

> c) The equality

\[
\frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}} = \frac{1}{t - {n\pi }} + \frac{1}{t + {n\pi }}\;\text{ entraîne }\;\frac{d}{dt}\left( \frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}\right)  =  - \frac{1}{{\left( t - n\pi \right) }^{2}} - \frac{1}{{\left( t + n\pi \right) }^{2}}.
\]

Ainsi, si on fixe \( x \in \rbrack 0,\pi \lbrack \) , la série de fonctions \( \mathop{\sum }\limits_{{n \geq 1}}\frac{d}{dt}\left( \frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}\right) \) converge normalement sur \( \left\lbrack {0, x}\right\rbrack \) . En appliquant le théorème de dérivabilité des séries de fonctions, on en conclut que

> Thus, if we fix \( x \in \rbrack 0,\pi \lbrack \) , the series of functions \( \mathop{\sum }\limits_{{n \geq 1}}\frac{d}{dt}\left( \frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}\right) \) converges normally on \( \left\lbrack {0, x}\right\rbrack \) . By applying the theorem on the differentiability of series of functions, we conclude that

\[
t \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{2t}{{t}^{2} - {n}^{2}{\pi }^{2}}\;\text{ est dérivable sur }\left\lbrack  {0, x}\right\rbrack  \text{ , sa dérivée est }t \mapsto   - \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}\frac{1}{{\left( t - n\pi \right) }^{2}}.
\]

En dérivant l’identité obtenue dans la question a) au point \( x \) , on déduit

> By differentiating the identity obtained in question a) at point \( x \) , we deduce

\[
\frac{-1}{{\sin }^{2}x} + \frac{1}{{x}^{2}} =  - \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}\frac{1}{{\left( x - n\pi \right) }^{2}}.
\]

Ceci vaut pour tout \( x \in \rbrack 0,\pi \lbrack \) . Les fonctions en présence étant paires, cette relation vaut sur \( \rbrack - \pi ,\pi \lbrack \smallsetminus \{ 0\} \) d’où le résultat

> This holds for all \( x \in \rbrack 0,\pi \lbrack \) . As the functions involved are even, this relation holds on \( \rbrack - \pi ,\pi \lbrack \smallsetminus \{ 0\} \) , hence the result

EXERCICE 3. Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction \( {2\pi } \) -périodique de classe \( {\mathcal{C}}^{1} \) . On suppose que \( {\int }_{0}^{2\pi }f\left( t\right) {dt} = 0 \) . Montrer

> EXERCISE 3. Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \) -periodic function of class \( {\mathcal{C}}^{1} \) . Suppose that \( {\int }_{0}^{2\pi }f\left( t\right) {dt} = 0 \) . Show

\[
{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} \leq  {\int }_{0}^{2\pi }{\left| {f}^{\prime }\left( t\right) \right| }^{2}{dt}
\]

et caractériser l'égalité.

> and characterize the equality.

Solution. Le coefficient de Fourier \( {c}_{0}\left( f\right) \) est nul car \( {\int }_{0}^{2\pi }f\left( t\right) {dt} = 0 \) . En appliquant l’identité \( {c}_{n}\left( {f}^{\prime }\right) = \operatorname{in}{c}_{n}\left( f\right) \) , avec l’égalité de Parseval appliquée aux fonctions \( f \) et \( {f}^{\prime } \) , on trouve donc

> Solution. The Fourier coefficient \( {c}_{0}\left( f\right) \) is zero because \( {\int }_{0}^{2\pi }f\left( t\right) {dt} = 0 \) . By applying the identity \( {c}_{n}\left( {f}^{\prime }\right) = \operatorname{in}{c}_{n}\left( f\right) \) , with Parseval's equality applied to the functions \( f \) and \( {f}^{\prime } \) , we therefore find

\[
\frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} = \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}{\left| {c}_{n}\left( f\right) \right| }^{2} \leq  \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}{n}^{2}{\left| {c}_{n}\left( f\right) \right| }^{2} = \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{\left| {c}_{n}\left( {f}^{\prime }\right) \right| }^{2} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| {f}^{\prime }\left( t\right) \right| }^{2}{dt},
\]

(*)

> ce qui prouve l'inégalité voulue.

which proves the desired inequality.

> Il y aura égalité si et seulement si la seule inégalité de (*) est une égalité, c'est-à-dire si et seulement si \( {\left| {c}_{n}\left( f\right) \right| }^{2} = {n}^{2}{\left| {c}_{n}\left( f\right) \right| }^{2} \) pour tout \( n \in {\mathbb{Z}}^{ * } \) , ce qui équivaut à \( {c}_{n}\left( f\right) = 0 \) pour tout \( n \) tel que \( \left| n\right| \geq 2 \) . Or \( f \) est de classe \( {\mathcal{C}}^{1} \) , donc sa série de Fourier converge (uniformément) vers \( f \) . En résumé, l’égalité se produira si et seulement \( f \) est de la forme \( f\left( t\right) = a{e}^{it} + b{e}^{-{it}}, a, b \in \mathbb{C} \) .

Equality will hold if and only if the only inequality in (*) is an equality, that is, if and only if \( {\left| {c}_{n}\left( f\right) \right| }^{2} = {n}^{2}{\left| {c}_{n}\left( f\right) \right| }^{2} \) for all \( n \in {\mathbb{Z}}^{ * } \) , which is equivalent to \( {c}_{n}\left( f\right) = 0 \) for all \( n \) such that \( \left| n\right| \geq 2 \) . However, \( f \) is of class \( {\mathcal{C}}^{1} \) , so its Fourier series converges (uniformly) to \( f \) . In summary, equality will occur if and only if \( f \) is of the form \( f\left( t\right) = a{e}^{it} + b{e}^{-{it}}, a, b \in \mathbb{C} \) .

> EXERCICE 4 (UNE FONCTION CONTINUE 2π-PÉRIODIQUE DONT LA SÉRIE DE FOURIER DIVERGE EN 0). a) Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) la fonction paire, \( {2\pi } \) -périodique, telle que

EXERCISE 4 (A CONTINUOUS 2π-PERIODIC FUNCTION WHOSE FOURIER SERIES DIVERGES AT 0). a) Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be the even, \( {2\pi } \) -periodic function such that

\[
\forall x \in  \left\lbrack  {0,\pi }\right\rbrack  ,\;f\left( x\right)  = \mathop{\sum }\limits_{{p = 1}}^{{+\infty }}\frac{1}{{p}^{2}}\sin \left\lbrack  {\left( {{2}^{{p}^{3}} + 1}\right) \frac{x}{2}}\right\rbrack  .
\]

Vérifier l’existence et la continuité de \( f \) sur \( \mathbb{R} \) .

> Verify the existence and continuity of \( f \) on \( \mathbb{R} \) .

b) Pour tout \( \nu \in \mathbb{N} \) , on pose

> b) For all \( \nu \in \mathbb{N} \) , let

\[
\forall n \in  \mathbb{N},\;{a}_{n,\nu } = {\int }_{0}^{\pi }\cos {nt}\sin \frac{\left( {{2\nu } + 1}\right) t}{2}{dt},\;\forall q \in  \mathbb{N},\;{s}_{q,\nu } = \mathop{\sum }\limits_{{i = 0}}^{q}{a}_{i,\nu }.
\]

Calculer explicitement les \( {a}_{n,\nu } \) , montrer que \( {s}_{q,\nu } \geq 0 \) pour tout \( \left( {q,\nu }\right) \) , et montrer l’existence d’une constante \( B > 0 \) telle que \( {s}_{\nu ,\nu } > B\log \nu \) pour tout \( \nu \in {\mathbb{N}}^{ * } \) .

> Explicitly calculate the \( {a}_{n,\nu } \) , show that \( {s}_{q,\nu } \geq 0 \) for all \( \left( {q,\nu }\right) \) , and show the existence of a constant \( B > 0 \) such that \( {s}_{\nu ,\nu } > B\log \nu \) for all \( \nu \in {\mathbb{N}}^{ * } \) .

c) Montrer que la série de Fourier de \( f \) diverge en 0 .

> c) Show that the Fourier series of \( f \) diverges at 0 .

Solution. a) La série converge normalement sur \( \left\lbrack {0,\pi }\right\rbrack , f \) est donc bien définie et continue sur \( \left\lbrack {0,\pi }\right\rbrack \) . On la définit sur \( \lbrack - \pi ,0\lbrack \) , par \( f\left( x\right) = f\left( {-x}\right) \) . La fonction \( f \) est continue sur \( \left\lbrack {-\pi ,\pi }\right\rbrack \) . De plus \( f\left( {-\pi }\right) = f\left( \pi \right) \) , on en déduit que le prolongement de \( f \) en une fonction \( {2\pi } \) -périodique \( f \) sur \( \mathbb{R} \) est continu sur \( \mathbb{R} \) .

> Solution. a) The series converges normally on \( \left\lbrack {0,\pi }\right\rbrack , f \) and is therefore well-defined and continuous on \( \left\lbrack {0,\pi }\right\rbrack \) . We define it on \( \lbrack - \pi ,0\lbrack \) by \( f\left( x\right) = f\left( {-x}\right) \) . The function \( f \) is continuous on \( \left\lbrack {-\pi ,\pi }\right\rbrack \) . Furthermore, \( f\left( {-\pi }\right) = f\left( \pi \right) \) , from which we deduce that the extension of \( f \) into a \( {2\pi } \) -periodic function \( f \) on \( \mathbb{R} \) is continuous on \( \mathbb{R} \) .

b) Le calcul des \( {a}_{n,\nu } \) est facile, on a

> b) The calculation of the \( {a}_{n,\nu } \) is easy; we have

\[
{a}_{n,\nu } = \frac{1}{2}{\int }_{0}^{\pi }\left\lbrack  {\sin \left( {\frac{{2\nu } + 1}{2} + n}\right) t + \sin \left( {\frac{{2\nu } + 1}{2} - n}\right) t}\right\rbrack  {dt}
\]

\[
= \frac{1}{2}\left( {\frac{1}{\nu  + n + 1/2} + \frac{1}{\nu  - n + 1/2}}\right)  = \frac{\nu  + 1/2}{{\left( \nu  + 1/2\right) }^{2} - {n}^{2}}.
\]

Ainsi, on a \( {a}_{n,\nu } \geq 0 \) pour \( n \leq \nu \) , donc \( {s}_{q,\nu } \geq 0 \) pour \( q \leq \nu \) .

> Thus, we have \( {a}_{n,\nu } \geq 0 \) for \( n \leq \nu \) , so \( {s}_{q,\nu } \geq 0 \) for \( q \leq \nu \) .

Pour le cas \( q > \nu \) , on remarque que les \( {a}_{n,\nu } \) , sont, au facteur \( 2/\pi \) près, les coefficients de Fourier \( {a}_{n}\left( {g}_{\nu }\right) \) de la fonction paire \( {g}_{\nu }\left( t\right) = \left| {\sin \left( {\left( {\nu + 1/2}\right) t}\right) }\right| \) . Cette dernière est continue et \( {\mathcal{C}}^{1} \) par morceaux, sa série de Fourier converge donc vers \( {g}_{\nu } \) . En particulier, on a \( {a}_{0,\nu }/2 + \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n,\nu } = \; \frac{\pi }{2}{g}_{\nu }\left( 0\right) = 0 \) , donc la suite \( {\left( {s}_{q,\nu }\right) }_{q \in \mathbb{N}} \) converge vers \( {a}_{0,\nu }/2 \) . Or \( {a}_{n,\nu } \) est positif pour \( n \leq \nu \) , négatif pour \( n > \nu \) , donc \( {\left( {s}_{q,\nu }\right) }_{q} \) est décroissante à partir de l’indice \( q = \nu \) . Comme elle converge vers \( {a}_{0,\nu }/2 \) , on en déduit que \( {s}_{q,\nu } \geq {a}_{0,\nu }/2 \geq 0 \) pour tout \( q > \nu \) .

> For the case \( q > \nu \) , we note that the \( {a}_{n,\nu } \) are, up to a factor of \( 2/\pi \) , the Fourier coefficients \( {a}_{n}\left( {g}_{\nu }\right) \) of the even function \( {g}_{\nu }\left( t\right) = \left| {\sin \left( {\left( {\nu + 1/2}\right) t}\right) }\right| \) . The latter is continuous and piecewise \( {\mathcal{C}}^{1} \) , so its Fourier series converges to \( {g}_{\nu } \) . In particular, we have \( {a}_{0,\nu }/2 + \mathop{\sum }\limits_{{n = 1}}^{\infty }{a}_{n,\nu } = \; \frac{\pi }{2}{g}_{\nu }\left( 0\right) = 0 \) , so the sequence \( {\left( {s}_{q,\nu }\right) }_{q \in \mathbb{N}} \) converges to \( {a}_{0,\nu }/2 \) . However, \( {a}_{n,\nu } \) is positive for \( n \leq \nu \) and negative for \( n > \nu \) , so \( {\left( {s}_{q,\nu }\right) }_{q} \) is decreasing from the index \( q = \nu \) onwards. Since it converges to \( {a}_{0,\nu }/2 \) , we deduce that \( {s}_{q,\nu } \geq {a}_{0,\nu }/2 \geq 0 \) for all \( q > \nu \) .

Il nous reste à obtenir la minoration de \( {s}_{\nu ,\nu } \) . On écrit pour tout \( \nu \in {\mathbb{N}}^{ * } \) ,

> It remains for us to obtain the lower bound for \( {s}_{\nu ,\nu } \) . We write for all \( \nu \in {\mathbb{N}}^{ * } \) ,

\[
{s}_{\nu ,\nu } \geq  \mathop{\sum }\limits_{{n = 1}}^{\nu }\frac{\nu  + 1/2}{{\left( \nu  + 1/2\right) }^{2} - {n}^{2}} \geq  \mathop{\sum }\limits_{{n = 1}}^{\nu }{\int }_{n - 1}^{n}\frac{\left( {\nu  + 1/2}\right) {dt}}{{\left( \nu  + 1/2\right) }^{2} - {t}^{2}} = {\int }_{0}^{\nu }\frac{\left( {\nu  + 1/2}\right) {dt}}{{\left( \nu  + 1/2\right) }^{2} - {t}^{2}} = \frac{1}{2}\log \left( {{4\nu } + 3}\right) ,
\]

donc \( {s}_{\nu ,\nu } \geq \left( {\log \nu }\right) /2 \) pour tout \( \nu \in {\mathbb{N}}^{ * } \) .

> so \( {s}_{\nu ,\nu } \geq \left( {\log \nu }\right) /2 \) for all \( \nu \in {\mathbb{N}}^{ * } \) .

c) Comme \( f \) est paire, les coefficients de Fourier \( {b}_{n}\left( f\right) \) sont nuls. Par ailleurs, la parité de \( f \) entraîne

> c) Since \( f \) is even, the Fourier coefficients \( {b}_{n}\left( f\right) \) are zero. Furthermore, the parity of \( f \) implies

\[
\forall n \in  \mathbb{N},\;{a}_{n}\left( f\right)  = \frac{2}{\pi }{\int }_{0}^{\pi }f\left( t\right) \cos {ntdt} = \frac{2}{\pi }\mathop{\sum }\limits_{{p = 1}}^{{+\infty }}\frac{1}{{p}^{2}}{\int }_{0}^{\pi }\sin \left\lbrack  {\left( {{2}^{{p}^{3}} + 1}\right) \frac{t}{2}}\right\rbrack  \cos {ntdt},
\]

(on a le droit de changer les signes de sommation car la série converge normalement sur \( \lbrack 0,\pi \rbrack \) ), donc

> (we are allowed to change the summation signs because the series converges normally on \( \lbrack 0,\pi \rbrack \) ), so

\[
\forall n \in  \mathbb{N},\;{a}_{n}\left( f\right)  = \frac{2}{\pi }\mathop{\sum }\limits_{{p = 1}}^{{+\infty }}\frac{1}{{p}^{2}}{a}_{n,2{p}^{3} - 1},\;\text{ donc }\;{S}_{n} = \frac{\pi }{2}\mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\left( f\right)  = \mathop{\sum }\limits_{{p = 1}}^{{+\infty }}\frac{1}{{p}^{2}}{s}_{n,2{p}^{3} - 1}.
\]

Comme les \( {s}_{q,\nu } \) sont positifs, et que \( {s}_{\nu ,\nu } \geq \left( {\log \nu }\right) /2 \) , on en déduit

> Since the \( {s}_{q,\nu } \) are positive, and \( {s}_{\nu ,\nu } \geq \left( {\log \nu }\right) /2 \) , we deduce

\[
\forall p \in  \mathbb{N},\;{S}_{{2}^{{p}^{3} - 1}} \geq  \frac{1}{{p}^{2}}{s}_{{2}^{{p}^{3} - 1},{2}^{{p}^{3} - 1}} \geq  \frac{1}{2{p}^{2}}\log \left( {2}^{{p}^{3} - 1}\right)  = \frac{{p}^{3} - 1}{2{p}^{2}}\log 2.
\]

Ceci montre que \( {S}_{2{p}^{3} - 1} \rightarrow + \infty \) lorsque \( p \rightarrow + \infty \) , donc la série \( \sum {a}_{n}\left( f\right) \) diverge. Autrement dit, la série de Fourier de \( f \) en 0 diverge.

> This shows that \( {S}_{2{p}^{3} - 1} \rightarrow + \infty \) as \( p \rightarrow + \infty \) , so the series \( \sum {a}_{n}\left( f\right) \) diverges. In other words, the Fourier series of \( f \) at 0 diverges.

Remarque. Cet exemple d'une fonction continue \( {2\pi } \) -périodique dont la série de Fourier diverge en 0 est dû à Fejér. On peut montrer de manière non constructive que de telles fonctions existent à partir du théorème de Banach-Steinhaus (voir l'exercice 8 page 425).

> Remark. This example of a continuous \( {2\pi } \) -periodic function whose Fourier series diverges at 0 is due to Fejér. One can show non-constructively that such functions exist using the Banach-Steinhaus theorem (see exercise 8 on page 425).

EXERCICE 5. Montrer que la fonction

> EXERCISE 5. Show that the function

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\sin {nx}}{{n}^{2}}
\]

est bien définie, qu'elle est 2π-périodique et qu'elle est continue. Montrer que les coefficients de Fourier de \( f \) sont tels que \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{\left| n{b}_{n}\left( f\right) \right| }^{2} \) converge, mais que pourtant \( f \) n’est pas dérivable en 0 .

> is well-defined, that it is 2π-periodic, and that it is continuous. Show that the Fourier coefficients of \( f \) are such that \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{\left| n{b}_{n}\left( f\right) \right| }^{2} \) converges, but that \( f \) is nevertheless not differentiable at 0.

Solution. La série de fonctions \( \sum \left( {\sin {nx}}\right) /{n}^{2} \) converge normalement sur \( \mathbb{R} \) , donc \( f \) est définie et continue sur \( \mathbb{R} \) . Chaque somme partielle de la série est \( {2\pi } \) -périodique, donc \( f \) est \( {2\pi } \) -périodique.

> Solution. The series of functions \( \sum \left( {\sin {nx}}\right) /{n}^{2} \) converges normally on \( \mathbb{R} \), so \( f \) is defined and continuous on \( \mathbb{R} \). Each partial sum of the series is \( {2\pi } \)-periodic, so \( f \) is \( {2\pi } \)-periodic.

Comme la série trigonométrique définissant \( f \) converge normalement, \( f \) est égale à sa série de Fourier, donc \( {b}_{n}\left( f\right) = 1/{n}^{2} \) pour tout \( n \in {\mathbb{N}}^{ * } \) , et la série \( \sum {\left| n{b}_{n}\left( f\right) \right| }^{2} \) converge donc.

> Since the trigonometric series defining \( f \) converges normally, \( f \) is equal to its Fourier series, so \( {b}_{n}\left( f\right) = 1/{n}^{2} \) for all \( n \in {\mathbb{N}}^{ * } \), and the series \( \sum {\left| n{b}_{n}\left( f\right) \right| }^{2} \) therefore converges.

Montrons que \( f \) n’est pas dérivable en 0 . Soit \( N \) un entier naturel non nul. L’inégalité de concavité sin \( u \geq {2u}/\pi \) sur \( \left\lbrack {0,\pi /2}\right\rbrack \) entraîne

> Let us show that \( f \) is not differentiable at 0. Let \( N \) be a non-zero natural integer. The concavity inequality sin \( u \geq {2u}/\pi \) on \( \left\lbrack {0,\pi /2}\right\rbrack \) implies

\[
\left. {\forall x \in  }\right\rbrack  0,\frac{\pi }{2N}\rbrack ,\;\frac{f\left( x\right) }{x} = \mathop{\sum }\limits_{{n = 1}}^{N}\frac{\sin {nx}}{nx}\frac{1}{n} + \mathop{\sum }\limits_{{n > N}}\frac{\sin {nx}}{{n}^{2}x} \geq  \mathop{\sum }\limits_{{n = 1}}^{N}\frac{2}{\pi }\frac{1}{n} + \frac{1}{x}\mathop{\sum }\limits_{{n > N}}\frac{\sin {nx}}{{n}^{2}}.
\]

(*)

> Par ailleurs, une transformation d'Abel fournit

Furthermore, an Abel transformation provides

\[
\mathop{\sum }\limits_{{n > N}}\frac{\sin {nx}}{{n}^{2}} = \mathop{\sum }\limits_{{n > N}}{S}_{n}\left( x\right) \left( {\frac{1}{{n}^{2}} - \frac{1}{{\left( n + 1\right) }^{2}}}\right) \;\text{ avec }\;{S}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\sin {kx},
\]

ce qui grâce à la majoration (on utilise le fait que \( {S}_{n}\left( x\right) \) est la partie imaginaire de \( \mathop{\sum }\limits_{{k = 0}}^{n}{e}^{ikx} \) )

> which, thanks to the upper bound (using the fact that \( {S}_{n}\left( x\right) \) is the imaginary part of \( \mathop{\sum }\limits_{{k = 0}}^{n}{e}^{ikx} \))

\[
\left| {{S}_{n}\left( x\right) }\right|  \leq  \left| \frac{1 - {e}^{i\left( {n + 1}\right) x}}{1 - {e}^{ix}}\right|  = \left| \frac{\sin \left( {\left( {n + 1}\right) x/2}\right) }{\sin \left( {x/2}\right) }\right|  \leq  \frac{1}{\sin \left( {x/2}\right) } \leq  \frac{1}{\left( {2/\pi }\right) \left( {x/2}\right) } = \frac{\pi }{x},
\]

donne

> gives

\[
\left| {\mathop{\sum }\limits_{{n > N}}\frac{\sin {nx}}{{n}^{2}}}\right|  \leq  \frac{\pi }{x}\left( {\mathop{\sum }\limits_{{n > N}}\frac{1}{{n}^{2}} - \frac{1}{{\left( n + 1\right) }^{2}}}\right)  = \frac{\pi }{x}\frac{1}{{\left( N + 1\right) }^{2}} \leq  \frac{\pi }{x}\frac{1}{{N}^{2}}.
\]

Avec (*) on en déduit

> With (*) we deduce

\[
\forall x \in  \left\rbrack  {0,\frac{\pi }{2N}}\right\rbrack  ,\;\frac{f\left( x\right) }{x} \geq  \frac{2}{\pi }\left( {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n}}\right)  - \frac{\pi }{{N}^{2}{x}^{2}}.
\]

Ainsi, en posant \( {x}_{N} = \pi /\left( {2N}\right) \) , on a \( f\left( {x}_{N}\right) /{x}_{N} \geq \frac{2}{\pi }\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n} - \frac{4}{\pi } \) . La suite \( \left( {x}_{N}\right) \) tend vers 0 et comme \( \sum \frac{1}{n} \) diverge, \( \left( {f\left( {x}_{N}\right) - f\left( 0\right) }\right) /\left( {{x}_{N} - 0}\right) = f\left( {x}_{N}\right) /{x}_{N} \) diverge lorsque \( N \rightarrow + \infty \) . D’où la non-dérivabilité de \( f \) en 0 .

> Thus, by setting \( {x}_{N} = \pi /\left( {2N}\right) \), we have \( f\left( {x}_{N}\right) /{x}_{N} \geq \frac{2}{\pi }\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n} - \frac{4}{\pi } \). The sequence \( \left( {x}_{N}\right) \) tends to 0 and since \( \sum \frac{1}{n} \) diverges, \( \left( {f\left( {x}_{N}\right) - f\left( 0\right) }\right) /\left( {{x}_{N} - 0}\right) = f\left( {x}_{N}\right) /{x}_{N} \) diverges when \( N \rightarrow + \infty \). Hence the non-differentiability of \( f \) at 0.

EXERCICE 6 (PHÉNOMÉNE DE GIBBS). On considère le signal carré \( \varphi \) , qui est la fonc-tion \( {2\pi } \) -périodique,égale à1sur \( \rbrack 0,\pi \left\lbrack \text{ ,à 0 sur }\right\rbrack \pi ,{2\pi }\lbrack \) , et qui vaut \( 1/2 \) en ses points de discontinuité.

> EXERCISE 6 (GIBBS PHENOMENON). Consider the square signal \( \varphi \), which is the \( {2\pi } \)-periodic function equal to 1 on \( \rbrack 0,\pi \left\lbrack \text{ ,à 0 sur }\right\rbrack \pi ,{2\pi }\lbrack \), and which is equal to \( 1/2 \) at its points of discontinuity.

a) Calculer la série de Fourier de \( \varphi \) , montrer qu’elle converge simplement vers \( \varphi \) et même uniformément sur tout intervalle fermé ne contenant pas les discontinuités de \( \varphi \) .

> a) Calculate the Fourier series of \( \varphi \), show that it converges pointwise to \( \varphi \) and even uniformly on any closed interval not containing the discontinuities of \( \varphi \).

b) Montrer que les sommes partielles d’indice impair \( {s}_{{2n} - 1}\left( t\right) \) de la série de Fourier de \( \varphi \) admettent la représentation intégrale

> b) Show that the odd-indexed partial sums \( {s}_{{2n} - 1}\left( t\right) \) of the Fourier series of \( \varphi \) admit the integral representation

\[
{s}_{{2n} - 1}\left( t\right)  = \frac{1}{2} + \frac{1}{\pi }{\int }_{0}^{t}\frac{\sin {2ns}}{\sin s}{ds}.
\]

c) Calculer les points critiques de \( {s}_{{2n} - 1} \) sur \( \left\lbrack {0,\pi }\right\rbrack \) et la valeur de son maximum.

> c) Calculate the critical points of \( {s}_{{2n} - 1} \) on \( \left\lbrack {0,\pi }\right\rbrack \) and the value of its maximum.

d) Montrer que ce maximum converge lorsque \( n \) tend vers l’infini vers le nombre

> d) Show that this maximum converges as \( n \) tends to infinity to the number

\[
M = \frac{1}{2} + \frac{1}{\pi }{\int }_{0}^{\pi }\frac{\sin s}{s}{ds}
\]

puis conclure (on admet qu’une valeur approximative à \( {10}^{-3} \) près est \( M \approx 1,{089} \) ).

> then conclude (it is accepted that an approximate value to \( {10}^{-3} \) is \( M \approx 1,{089} \)).

Solution. a) Le signal carré \( \varphi \) est \( {\mathcal{C}}^{1} \) par morceaux, et comme \( \varphi \left( x\right) = \frac{1}{2}\left( {\varphi \left( {x - }\right) + \varphi \left( {x + }\right) }\right) \) en ses discontinuités, la série de Fourier de \( \varphi \) converge simplement vers \( \varphi \) . Elle se calcule facilement et on obtient

> Solution. a) The square signal \( \varphi \) is piecewise \( {\mathcal{C}}^{1} \), and since \( \varphi \left( x\right) = \frac{1}{2}\left( {\varphi \left( {x - }\right) + \varphi \left( {x + }\right) }\right) \) at its discontinuities, the Fourier series of \( \varphi \) converges pointwise to \( \varphi \). It is easily calculated, and we obtain

\[
\varphi \left( t\right)  = \frac{1}{2} + \frac{2}{\pi }\mathop{\sum }\limits_{{\nu  = 1}}^{{+\infty }}\frac{\sin \left( {{2\nu } - 1}\right) t}{{2\nu } - 1},\;t \in  \mathbb{R}.
\]

Les coefficients de Fourier formant une suite décroissante, la convergence est uniforme sur tout intervalle fermé ne contenant pas les discontinuités de \( \varphi \) d’après la proposition 2 page 268 .

> As the Fourier coefficients form a decreasing sequence, the convergence is uniform on any closed interval not containing the discontinuities of \( \varphi \) according to proposition 2 on page 268.

b) Partant de la représentation intégrale \( \frac{\sin \left( {{2\nu } - 1}\right) t}{{2\nu } - 1} = {\int }_{0}^{t}\cos \left( {{2\nu } - 1}\right) {sds} \) , on peut écrire

> b) Starting from the integral representation \( \frac{\sin \left( {{2\nu } - 1}\right) t}{{2\nu } - 1} = {\int }_{0}^{t}\cos \left( {{2\nu } - 1}\right) {sds} \), we can write

\[
{s}_{{2n} - 1}\left( t\right)  = \frac{1}{2} + \frac{2}{\pi }{\int }_{0}^{t}{C}_{n}\left( s\right) {ds},\;{C}_{n}\left( s\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\cos \left( {{2k} - 1}\right) s.
\]

(*)

> On calcule \( {C}_{n}\left( s\right) \) à partir de la partie réelle d’une somme d’exponentielles complexes,

We calculate \( {C}_{n}\left( s\right) \) from the real part of a sum of complex exponentials,

\[
{C}_{n}\left( s\right)  = \Re \left( {\mathop{\sum }\limits_{{k = 1}}^{n}{e}^{i\left( {{2k} - 1}\right) s}}\right)  = \Re \left( {{e}^{is}\frac{{e}^{i2ns} - 1}{{e}^{2is} - 1}}\right)  = \Re \left( {{e}^{ins}\frac{\sin {ns}}{\sin s}}\right)  = \frac{\cos {ns}\sin {ns}}{\sin s} = \frac{\sin {2ns}}{2\sin s}.
\]

On en déduit le résultat en remplaçant cette dernière expression dans (*).

> We deduce the result by substituting this last expression into (*).

c) La représentation intégrale précédente donne \( {s}_{{2n} - 1}^{\prime }\left( t\right) = \frac{1}{\pi }\sin \left( {2nt}\right) /\sin t \) (et \( {s}_{{2n} - 1}^{\prime }\left( 0\right) = {2n}/\pi \) par continuité), donc \( {s}_{{2n} - 1}^{\prime } \) s’annule sur \( \left\lbrack {0,\pi }\right\rbrack \) en \( t = {x}_{k} = {k\pi }/\left( {2n}\right) ,0 < k \leq {2n} \) . Montrons que son maximum est atteint en \( {x}_{1} \) . Pour \( 1 \leq k \leq n \) , on a

> c) The previous integral representation gives \( {s}_{{2n} - 1}^{\prime }\left( t\right) = \frac{1}{\pi }\sin \left( {2nt}\right) /\sin t \) (and \( {s}_{{2n} - 1}^{\prime }\left( 0\right) = {2n}/\pi \) by continuity), so \( {s}_{{2n} - 1}^{\prime } \) vanishes on \( \left\lbrack {0,\pi }\right\rbrack \) at \( t = {x}_{k} = {k\pi }/\left( {2n}\right) ,0 < k \leq {2n} \). Let us show that its maximum is reached at \( {x}_{1} \). For \( 1 \leq k \leq n \), we have

\[
{s}_{{2n} - 1}\left( {x}_{2k}\right)  - {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right)  = \frac{1}{\pi }{\int }_{{x}_{{2k} - 1}}^{{x}_{2k}}\frac{\sin {2ns}}{\sin s}{ds},
\]

et comme l’intégrande est négative sur \( \left\lbrack {{x}_{{2k} - 1},{x}_{2k}}\right\rbrack \) on en déduit \( {s}_{{2n} - 1}\left( {x}_{2k}\right) < {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \) . Le maximum est donc atteint sur l’un des \( {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \) pour \( 1 \leq k \leq n \) . Maintenant pour \( 1 \leq k < n \) , on a

> and since the integrand is negative on \( \left\lbrack {{x}_{{2k} - 1},{x}_{2k}}\right\rbrack \), we deduce \( {s}_{{2n} - 1}\left( {x}_{2k}\right) < {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \). The maximum is therefore reached on one of the \( {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \) for \( 1 \leq k \leq n \). Now for \( 1 \leq k < n \), we have

\[
{s}_{{2n} - 1}\left( {x}_{{2k} + 1}\right)  - {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right)  = \frac{1}{\pi }{\int }_{{x}_{{2k} - 1}}^{{x}_{2k}}\sin {2ns}\left( {\frac{1}{\sin s} - \frac{1}{\sin \left( {s + \frac{\pi }{2n}}\right) }}\right) {ds}
\]

expression que l’on obtient en découpant en deux l’intégrale \( {\int }_{{x}_{{2k} - 1}}^{{x}_{{2k} + 1}} = {\int }_{{x}_{{2k} - 1}}^{{x}_{2k}} + {\int }_{{x}_{2k}}^{{x}_{{2k} + 1}} \) et en effectuant le changement de variable \( s \mapsto s + \pi /\left( {2n}\right) \) dans la deuxième. La fonction sinus étant croissante sur \( \left\lbrack {0,\pi }\right\rbrack \) , et comme sin \( {2ns} \) est négatif sur \( \left\lbrack {{x}_{{2k} - 1},{x}_{2k}}\right\rbrack \) , la dernière intégrande est négative, donc \( {s}_{{2n} - 1}\left( {x}_{{2k} + 1}\right) < {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \) . Finalement, ceci montre que le maximum est atteint en \( t = {x}_{1} = \pi /\left( {2n}\right) \) et vaut

> an expression obtained by splitting the integral \( {\int }_{{x}_{{2k} - 1}}^{{x}_{{2k} + 1}} = {\int }_{{x}_{{2k} - 1}}^{{x}_{2k}} + {\int }_{{x}_{2k}}^{{x}_{{2k} + 1}} \) into two and performing the change of variable \( s \mapsto s + \pi /\left( {2n}\right) \) in the second. Since the sine function is increasing on \( \left\lbrack {0,\pi }\right\rbrack \), and as sin \( {2ns} \) is negative on \( \left\lbrack {{x}_{{2k} - 1},{x}_{2k}}\right\rbrack \), the last integrand is negative, so \( {s}_{{2n} - 1}\left( {x}_{{2k} + 1}\right) < {s}_{{2n} - 1}\left( {x}_{{2k} - 1}\right) \). Finally, this shows that the maximum is reached at \( t = {x}_{1} = \pi /\left( {2n}\right) \) and is equal to

\[
\mathop{\sup }\limits_{{0 \leq  t \leq  \pi }}{s}_{{2n} - 1}\left( t\right)  = {M}_{n} = \frac{1}{2} + \frac{1}{\pi }{\int }_{0}^{\pi /\left( {2n}\right) }\frac{\sin {2ns}}{\sin s}{ds}.
\]

d) Le changement de variable \( t = {2ns} \) dans l’intégrale précédente donne

> d) The change of variable \( t = {2ns} \) in the previous integral gives

\[
{M}_{n} = \frac{1}{2} + \frac{1}{\pi }{\int }_{0}^{\pi }\frac{\sin t}{{2n}\sin \left( {t/\left( {2n}\right) }\right) }{dt}.
\]

Lorsque \( x \rightarrow 0 \) , on a \( \sin x \sim x \) . Donc pour tout \( \varepsilon > 0 \) , il existe \( \alpha > 0 \) tel que \( x/\left( {1 + \varepsilon }\right) \leq \sin x \leq \; x/\left( {1 - \varepsilon }\right) \) pour \( x \in \left\lbrack {0,\alpha }\right\rbrack \) . Ainsi, si \( n > \pi /\left( {2\alpha }\right) \) on a \( t/\left( {1 - \varepsilon }\right) \leq {2n}\sin \left( {t/\left( {2n}\right) }\right) \leq t/\left( {1 + \varepsilon }\right) \) sur \( \left\lbrack {0,\pi }\right\rbrack \) , donc

> When \( x \rightarrow 0 \) , we have \( \sin x \sim x \) . Thus for any \( \varepsilon > 0 \) , there exists \( \alpha > 0 \) such that \( x/\left( {1 + \varepsilon }\right) \leq \sin x \leq \; x/\left( {1 - \varepsilon }\right) \) for \( x \in \left\lbrack {0,\alpha }\right\rbrack \) . Therefore, if \( n > \pi /\left( {2\alpha }\right) \) we have \( t/\left( {1 - \varepsilon }\right) \leq {2n}\sin \left( {t/\left( {2n}\right) }\right) \leq t/\left( {1 + \varepsilon }\right) \) on \( \left\lbrack {0,\pi }\right\rbrack \) , so

\[
\frac{1}{2} + \left( {1 - \varepsilon }\right) \frac{1}{\pi }{\int }_{0}^{\pi }\frac{\sin t}{t}{dt} \leq  {M}_{n} \leq  \frac{1}{2} + \left( {1 + \varepsilon }\right) \frac{1}{\pi }{\int }_{0}^{\pi }\frac{\sin t}{t}{dt}.
\]

On en déduit que \( \left( {M}_{n}\right) \) converge vers \( M \) lorsque \( n \rightarrow \infty \) .

> We deduce that \( \left( {M}_{n}\right) \) converges to \( M \) as \( n \rightarrow \infty \) .

Concluons. Nous venons de montrer que le maximum des sommes partielles \( {s}_{{2n} - 1} \) conver-geait vers un nombre \( M \approx 1,{089} \) qui est strictement plus grand que le maximum de \( \varphi \) . Ainsi, les sommes partielles convergent simplement vers le signal carré \( \varphi \) mais pas uniformément.

> In conclusion. We have just shown that the maximum of the partial sums \( {s}_{{2n} - 1} \) converges to a number \( M \approx 1,{089} \) which is strictly greater than the maximum of \( \varphi \) . Thus, the partial sums converge pointwise to the square wave \( \varphi \) but not uniformly.

![bo_d7fjkrs91nqc73ereoog_282_967_1245_427_281_0.jpg](images/gourdon_analysis_fr_en_011_bod7fjkrs91nqc73ereoog28296712454272810.jpg)

Remarque. Le graphe ci-contre illustre le phénomène de Gibbs (pour la somme partielle \( t \mapsto {s}_{{2n} - 1}\left( t\right) \) avec \( n = {40}) \) de la série de Fourier du signal carré.

> Remark. The graph opposite illustrates the Gibbs phenomenon (for the partial sum \( t \mapsto {s}_{{2n} - 1}\left( t\right) \) with \( n = {40}) \) of the Fourier series of the square wave.

- Le phénomène de Gibbs fut observé par Michelson en 1898 lorsqu'il développa un système mécanique capable de tracer la série de Fourier d'un signal. Alors que Michelson soupçonnait un défaut dans la fabrication de sa machine, Gibbs montra l'année suivante que le phénomène était d'origine mathématique.

> - The Gibbs phenomenon was observed by Michelson in 1898 when he developed a mechanical system capable of plotting the Fourier series of a signal. While Michelson suspected a manufacturing defect in his machine, Gibbs showed the following year that the phenomenon was mathematical in origin.

EXERCICE 7 (THÉORÉME DE S. BERNSTEIN SUR LES SÉRIES DE FOURIER). Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction \( {2\pi } \) -périodique. On suppose que

> EXERCISE 7 (S. BERNSTEIN'S THEOREM ON FOURIER SERIES). Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \) -periodic function. Suppose that

\[
\exists \alpha  \in  \rbrack 0,1\left\lbrack  {,\exists C > 0,\;\forall \left( {u, v}\right)  \in  {\mathbb{R}}^{2},\;\left| {f\left( u\right)  - f\left( v\right) }\right|  \leq  C{\left| u - v\right| }^{\alpha }}\right.
\]

(une telle fonction est dite \( \alpha \) -höldérienne).

> (such a function is said to be \( \alpha \) -Hölder continuous).

a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on pose \( {\rho }_{n} = {\left( {\left| {c}_{n}\left( f\right) \right| }^{2} + {\left| {c}_{-n}\left( f\right) \right| }^{2}\right) }^{1/2} \) . Montrer que

> a) For any \( n \in {\mathbb{N}}^{ * } \) , let \( {\rho }_{n} = {\left( {\left| {c}_{n}\left( f\right) \right| }^{2} + {\left| {c}_{-n}\left( f\right) \right| }^{2}\right) }^{1/2} \) . Show that

\[
\forall h \in  \mathbb{R},\;4\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\rho }_{n}^{2}{\sin }^{2}{nh} = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\left| f\left( x + h\right)  - f\left( x - h\right) \right| }^{2}{dx}.
\]

b) En déduire, pour tout \( \nu \in {\mathbb{N}}^{ * } \) , la majoration \( \mathop{\sum }\limits_{{{2}^{\nu - 1} < n \leq {2}^{\nu }}}{\rho }_{n} \leq \frac{C}{2}\frac{{\pi }^{\alpha }}{{2}^{\nu \left( {\alpha - 1/2}\right) }} \) .

> b) Deduce, for any \( \nu \in {\mathbb{N}}^{ * } \) , the bound \( \mathop{\sum }\limits_{{{2}^{\nu - 1} < n \leq {2}^{\nu }}}{\rho }_{n} \leq \frac{C}{2}\frac{{\pi }^{\alpha }}{{2}^{\nu \left( {\alpha - 1/2}\right) }} \) .

c) Si \( \alpha > 1/2 \) , montrer que la série de Fourier de \( f \) converge normalement vers \( f \) sur \( \mathbb{R} \) .

> c) If \( \alpha > 1/2 \) , show that the Fourier series of \( f \) converges normally to \( f \) on \( \mathbb{R} \) .

Solution. a) Remarquons déjà que \( f \) est continue. Ensuite, fixons \( h \in \mathbb{R} \) et considérons la fonction \( {f}_{h} : x \mapsto f\left( {x + h}\right) - f\left( {x - h}\right) \) . Les changements de variable \( u = x + h \) et \( u = x - h \) conjugués au caractère \( {2\pi } \) -périodique des intégrandes entraînent

> Solution. a) Let us first note that \( f \) is continuous. Then, fix \( h \in \mathbb{R} \) and consider the function \( {f}_{h} : x \mapsto f\left( {x + h}\right) - f\left( {x - h}\right) \) . The changes of variable \( u = x + h \) and \( u = x - h \) combined with the \( {2\pi } \) -periodic nature of the integrands lead to

\[
\forall n \in  \mathbb{Z},\;\frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( {x + h}\right) {e}^{-{inx}}{dx} = {e}^{inh}{c}_{n}\left( f\right) \;\text{ et }{\int }_{-\pi }^{\pi }f\left( {x - h}\right) {e}^{-{inx}}{dx} = {e}^{-{inh}}{c}_{n}\left( f\right)
\]

et comme \( {e}^{inh} - {e}^{-{inh}} = {2i}\left( {\sin {nh}}\right) \) , ceci montre que les coefficients de Fourier de \( {f}_{h} \) vérifient \( {c}_{n}\left( {f}_{h}\right) = {2i}\left( {\sin {nh}}\right) {c}_{n}\left( f\right) \) . On conclut en appliquant l’égalité de Parseval à \( {f}_{h} \) .

> and since \( {e}^{inh} - {e}^{-{inh}} = {2i}\left( {\sin {nh}}\right) \) , this shows that the Fourier coefficients of \( {f}_{h} \) satisfy \( {c}_{n}\left( {f}_{h}\right) = {2i}\left( {\sin {nh}}\right) {c}_{n}\left( f\right) \) . We conclude by applying Parseval's identity to \( {f}_{h} \) .

b) En appliquant l’égalité précédente à \( h = \pi /{2}^{\nu + 1} \) , on a

> b) By applying the previous equality to \( h = \pi /{2}^{\nu + 1} \) , we have

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\rho }_{n}^{2}{\sin }^{2}\frac{n\pi }{{2}^{\nu  + 1}} = \frac{1}{8\pi }{\int }_{-\pi }^{\pi }{\left| f\left( x + h\right)  - f\left( x - h\right) \right| }^{2}{dx} \leq  \frac{1}{8\pi }{\int }_{-\pi }^{\pi }{\left( C{\left( 2h\right) }^{\alpha }\right) }^{2}{dx} = \frac{{C}^{2}}{4}\frac{{\pi }^{2\alpha }}{{2}^{2\alpha \nu }}
\]

et comme

> and since

\[
\forall n,{2}^{\nu  - 1} < n \leq  {2}^{\nu },\;{\sin }^{2}\frac{n\pi }{{2}^{\nu  + 1}} \geq  {\sin }^{2}\frac{\pi }{4} = \frac{1}{2},\;\text{ on en déduit }\mathop{\sum }\limits_{{{2}^{\nu  - 1} < n \leq  {2}^{\nu }}}{\rho }_{n}^{2} \leq  2\frac{{C}^{2}}{4}\frac{{\pi }^{2\alpha }}{{2}^{2\alpha \nu }}.
\]

Il suffit ensuite d'appliquer l'inégalité de Schwarz, qui entraîne

> It then suffices to apply the Cauchy-Schwarz inequality, which implies

\[
\mathop{\sum }\limits_{{{2}^{\nu  - 1} < n \leq  {2}^{\nu }}}{\rho }_{n} \leq  {\left( \mathop{\sum }\limits_{{{2}^{\nu  - 1} < n \leq  {2}^{\nu }}}1\right) }^{1/2}{\left( \mathop{\sum }\limits_{{{2}^{\nu  - 1} < n \leq  {2}^{\nu }}}{\rho }_{n}^{2}\right) }^{1/2} \leq  {2}^{\left( {\nu  - 1}\right) /2}{\left( \frac{{C}^{2}}{2}\frac{{\pi }^{2\alpha }}{{2}^{2\alpha \nu }}\right) }^{1/2},
\]

d'où le résultat.

> hence the result.

c) Si \( \alpha > 1/2 \) , la majoration précédente montre que la série à termes positifs \( \sum {\rho }_{n} \) converge, et comme \( \left| {{c}_{n}\left( f\right) }\right| \leq {\rho }_{\left| n\right| } \) pour tout \( n \in \mathbb{Z} \) , on en déduit que \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{c}_{n}\left( f\right) }\right| \) converge. Ainsi, la série de Fourier de \( f \) converge normalement sur \( \mathbb{R} \) , et on sait alors qu’elle ne peut converger que vers \( f \) (voir le dernier alinéa de la remarque 6 page 271).

> c) If \( \alpha > 1/2 \) , the previous upper bound shows that the series with positive terms \( \sum {\rho }_{n} \) converges, and since \( \left| {{c}_{n}\left( f\right) }\right| \leq {\rho }_{\left| n\right| } \) for all \( n \in \mathbb{Z} \) , we deduce that \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{c}_{n}\left( f\right) }\right| \) converges. Thus, the Fourier series of \( f \) converges normally on \( \mathbb{R} \) , and we know that it can only converge to \( f \) (see the last paragraph of remark 6 on page 271).

EXERCICE 8. Soit \( \left( {\lambda }_{n}\right) \) une suite positive, décroissante et tendant vers 0.

> EXERCISE 8. Let \( \left( {\lambda }_{n}\right) \) be a positive, decreasing sequence tending to 0.

a) Montrer que la série de fonctions \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converge simplement vers une fonction \( f \) sur \( \mathbb{R} \) , et que \( f \) est continue sur \( \rbrack 0,{2\pi }\lbrack \) .

> a) Show that the series of functions \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converges pointwise to a function \( f \) on \( \mathbb{R} \), and that \( f \) is continuous on \( \rbrack 0,{2\pi }\lbrack \).

b) Si \( {\lambda }_{n} = o\left( {1/n}\right) \) lorsque \( n \rightarrow + \infty \) , montrer que \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converge uniformément vers \( f \) sur \( \mathbb{R} \) .

> b) If \( {\lambda }_{n} = o\left( {1/n}\right) \) as \( n \rightarrow + \infty \), show that \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converges uniformly to \( f \) on \( \mathbb{R} \).

c) Réciproquement, si \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converge uniformément vers \( f \) sur \( \mathbb{R} \) , montrer que \( {\lambda }_{n} = o\left( {1/n}\right) . \)

> c) Conversely, if \( \sum {\lambda }_{n}\sin \left( {nx}\right) \) converges uniformly to \( f \) on \( \mathbb{R} \), show that \( {\lambda }_{n} = o\left( {1/n}\right) . \)

d) Plus généralement, si \( f \) est continue sur \( \mathbb{R} \) montrer que \( {\lambda }_{n} = o\left( {1/n}\right) \) . (Indication. Considérer \( F\left( x\right) = {\int }_{0}^{x}f\left( t\right) {dt} \) .)

> d) More generally, if \( f \) is continuous on \( \mathbb{R} \), show that \( {\lambda }_{n} = o\left( {1/n}\right) \). (Hint: Consider \( F\left( x\right) = {\int }_{0}^{x}f\left( t\right) {dt} \).)

Solution. a) On sait d'après la proposition 2 page 268 qu'il y a convergence uniforme sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha \in \rbrack 0,\pi \left\lbrack \right. \) . On conclut qu’il y a convergence simple sur \( \rbrack 0,{2\pi }\lbrack \) , et que la fonction limite \( f \) est continue sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha > 0 \) , donc continue sur \( \rbrack 0,{2\pi }\lbrack \) .

> Solution. a) We know from proposition 2 on page 268 that there is uniform convergence on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for all \( \alpha \in \rbrack 0,\pi \left\lbrack \right. \). We conclude that there is pointwise convergence on \( \rbrack 0,{2\pi }\lbrack \), and that the limit function \( f \) is continuous on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for all \( \alpha > 0 \), and thus continuous on \( \rbrack 0,{2\pi }\lbrack \).

Il y a bien convergence simple en 0 (la série est nulle lorsque \( x = 0 \) ), il y a donc convergence simple sur \( \lbrack 0,{2\pi }\lbrack \) , donc sur \( \mathbb{R} \) car les fonctions en présence sont \( {2\pi } \) -périodiques.

> There is indeed pointwise convergence at 0 (the series is zero when \( x = 0 \)), so there is pointwise convergence on \( \lbrack 0,{2\pi }\lbrack \), and thus on \( \mathbb{R} \) because the functions involved are \( {2\pi } \)-periodic.

b) C'est un peu technique. Comme les fonctions en présence sont \( {2\pi } \) -périodiques et impaires, il suffit de prouver la convergence uniforme sur \( \left\lbrack {0,\pi }\right\rbrack \) . Le problème est en \( x = 0 \) car on a vu plus haut qu’il y avait convergence uniforme sur \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) pour tout \( \alpha > 0 \) .

> b) This is somewhat technical. Since the functions involved are \( {2\pi } \)-periodic and odd, it suffices to prove uniform convergence on \( \left\lbrack {0,\pi }\right\rbrack \). The problem is at \( x = 0 \) because we saw above that there was uniform convergence on \( \left\lbrack {\alpha ,{2\pi } - \alpha }\right\rbrack \) for all \( \alpha > 0 \).

Commençons par remarquer que

> Let us begin by noting that

\[
\forall x \in  \rbrack 0,\pi \rbrack ,\forall N \in  \mathbb{N},\;\left| {\mathop{\sum }\limits_{{n = N}}^{{+\infty }}{\lambda }_{n}{e}^{inx}}\right|  \leq  \frac{\pi {\lambda }_{N}}{x}.
\]

(*)

> En effet, une transformation d'Abel fournit

Indeed, an Abel transformation provides

\[
\forall M > N,\;\mathop{\sum }\limits_{{n = N}}^{M}{\lambda }_{n}{e}^{inx} = \mathop{\sum }\limits_{{n = N}}^{{M - 1}}\left( {{\lambda }_{n} - {\lambda }_{n + 1}}\right) {E}_{n}\left( x\right)  + {\lambda }_{M}{E}_{M}\left( x\right) \;\text{ avec }\;{E}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{e}^{ikx}
\]

et on a la majoration

> and we have the bound

\[
\forall x \in  \rbrack 0,\pi \rbrack ,\;\left| {{E}_{n}\left( x\right) }\right|  = \left| \frac{1 - {e}^{i\left( {n + 1}\right) x}}{1 - {e}^{ix}}\right|  = \left| \frac{\sin \left( {\frac{n + 1}{2}x}\right) }{\sin \left( {x/2}\right) }\right|  \leq  \frac{1}{\sin \left( {x/2}\right) } \leq  \frac{\pi }{x}
\]

(on a utilisé l’inégalité de concavité sin \( u \geq {2u}/\pi \) sur \( \left\lbrack {0,\pi /2}\right\rbrack \) ). En faisant tendre \( M \) vers l’infini on en déduit (*) car \( \left( {\lambda }_{n}\right) \) est décroissante et tend vers 0 .

> (we used the concavity inequality sin \( u \geq {2u}/\pi \) on \( \left\lbrack {0,\pi /2}\right\rbrack \)). By letting \( M \) tend to infinity, we deduce (*) because \( \left( {\lambda }_{n}\right) \) is decreasing and tends to 0.

Ceci étant, considérons \( \varepsilon > 0 \) et \( {N}_{0} \in {\mathbb{N}}^{ * } \) tel que \( {\lambda }_{n} \leq \varepsilon /n \) pour tout \( n \geq {N}_{0} \) . D’après (*)

> This being said, consider \( \varepsilon > 0 \) and \( {N}_{0} \in {\mathbb{N}}^{ * } \) such that \( {\lambda }_{n} \leq \varepsilon /n \) for all \( n \geq {N}_{0} \). According to (*)

\[
\forall x \in  \rbrack 0,\pi \rbrack ,\forall N \geq  {N}_{0},\;\left| {{r}_{N}\left( x\right) }\right|  \leq  \frac{\pi {\lambda }_{N}}{x} \leq  \frac{\pi \varepsilon }{Nx}\;\text{ où }\;{r}_{N}\left( x\right)  = \mathop{\sum }\limits_{{n = N}}^{{+\infty }}{\lambda }_{n}\sin \left( {nx}\right) .
\]

Ainsi, si \( N \geq {N}_{0} \) ,

> Thus, if \( N \geq {N}_{0} \),

\[
\forall x \in  \left\lbrack  {\frac{1}{N},\pi }\right\rbrack  ,\;\left| {{r}_{N}\left( x\right) }\right|  \leq  \frac{\pi \varepsilon N}{N} = {\pi \varepsilon },
\]

et si \( x \in \rbrack 0,1/N\lbrack \) , on a, en notant \( K = \left\lbrack {1/x}\right\rbrack \) la partie entière de \( 1/x \)

> and if \( x \in \rbrack 0,1/N\lbrack \), we have, by denoting \( K = \left\lbrack {1/x}\right\rbrack \) as the integer part of \( 1/x \)

\[
\left| {{r}_{N}\left( x\right) }\right|  \leq  \left| {\mathop{\sum }\limits_{{n = N}}^{K}{\lambda }_{n}\sin \left( {nx}\right) }\right|  + \left| {{r}_{K + 1}\left( x\right) }\right|  \leq  \mathop{\sum }\limits_{{n = N}}^{K}\frac{\varepsilon }{n}{nx} + \frac{\pi \varepsilon }{\left( {K + 1}\right) x} \leq  {\varepsilon Kx} + {\pi \varepsilon } \leq  \varepsilon  + {\pi \varepsilon }
\]

(on a utilisé la majoration \( \left| {\sin u}\right| \leq \left| u\right| \) que l’on montre facilement à partir de l’inégalité des accroissements finis). Ainsi, \( \left| {{r}_{N}\left( x\right) }\right| \leq \left( {1 + \pi }\right) \varepsilon \) pour tout \( x \in \left\lbrack {0,\pi }\right\rbrack \) (en \( x = 0 \) , c’est trivial), et ceci est vrai indépendamment de \( N \geq {N}_{0} \) . On a donc convergence uniforme sur \( \left\lbrack {0,\pi }\right\rbrack \) .

> (we used the bound \( \left| {\sin u}\right| \leq \left| u\right| \) which is easily shown from the mean value inequality). Thus, \( \left| {{r}_{N}\left( x\right) }\right| \leq \left( {1 + \pi }\right) \varepsilon \) for all \( x \in \left\lbrack {0,\pi }\right\rbrack \) (at \( x = 0 \) , it is trivial), and this is true independently of \( N \geq {N}_{0} \) . We therefore have uniform convergence on \( \left\lbrack {0,\pi }\right\rbrack \) .

c) Notons \( {s}_{n} \) les sommes partielles de notre série trigonométrique. \( \operatorname{Si}\left( {s}_{n}\right) \) converge uniformément sur \( \mathbb{R} \) vers \( f \) , alors \( f \) est continue, et la suite \( \left( {{s}_{n}\left( {1/n}\right) }\right) \) tend vers 0 (il suffit décrire \( \left| {{s}_{n}\left( {1/n}\right) }\right| \leq \; \left| {{s}_{n}\left( {1/n}\right) - f\left( {1/n}\right) }\right| + \left| {f\left( {1/n}\right) }\right| \) et de remarquer que les deux termes de droite tendent vers 0 lorsque \( n \rightarrow + \infty \) ). La suite \( \left( {\lambda }_{n}\right) \) étant décroissante, on a par ailleurs

> c) Let \( {s}_{n} \) denote the partial sums of our trigonometric series. If \( \operatorname{Si}\left( {s}_{n}\right) \) converges uniformly on \( \mathbb{R} \) to \( f \) , then \( f \) is continuous, and the sequence \( \left( {{s}_{n}\left( {1/n}\right) }\right) \) tends to 0 (it suffices to write \( \left| {{s}_{n}\left( {1/n}\right) }\right| \leq \; \left| {{s}_{n}\left( {1/n}\right) - f\left( {1/n}\right) }\right| + \left| {f\left( {1/n}\right) }\right| \) and note that both terms on the right tend to 0 as \( n \rightarrow + \infty \) ). Since the sequence \( \left( {\lambda }_{n}\right) \) is decreasing, we also have

\[
{s}_{n}\left( \frac{1}{n}\right)  \geq  {\lambda }_{n}\mathop{\sum }\limits_{{k = 1}}^{n}\sin \left( \frac{k}{n}\right)  \geq  {\lambda }_{n}\mathop{\sum }\limits_{{n/2 < k \leq  n}}\sin \left( \frac{1}{2}\right)  \geq  {\lambda }_{n}\frac{n}{2}\sin \left( \frac{1}{2}\right) ,
\]

donc \( 0 \leq {\lambda }_{n} \leq 2{s}_{n}\left( {1/n}\right) /\left( {n\sin \left( {1/2}\right) }\right) \) , et comme \( {s}_{n}\left( {1/n}\right) \rightarrow 0 \) , ceci montre \( {\lambda }_{n} = o\left( {1/n}\right) \) .

> therefore \( 0 \leq {\lambda }_{n} \leq 2{s}_{n}\left( {1/n}\right) /\left( {n\sin \left( {1/2}\right) }\right) \) , and since \( {s}_{n}\left( {1/n}\right) \rightarrow 0 \) , this shows \( {\lambda }_{n} = o\left( {1/n}\right) \) .

d) C’est difficile. Comme indiqué, nous considérons la fonction \( F : x \mapsto {\int }_{0}^{x}f\left( t\right) {dt} \) . Soit \( x \in \rbrack 0,\pi \rbrack \) et \( \alpha \in \rbrack 0, x\left\lbrack \right. \) . La série trigonométrique définissant \( f \) converge uniformément sur \( \left\lbrack {\alpha ,\pi }\right\rbrack \) comme on l'a vu plus haut, ce qui entraîne

> d) This is difficult. As indicated, we consider the function \( F : x \mapsto {\int }_{0}^{x}f\left( t\right) {dt} \) . Let \( x \in \rbrack 0,\pi \rbrack \) and \( \alpha \in \rbrack 0, x\left\lbrack \right. \) . The trigonometric series defining \( f \) converges uniformly on \( \left\lbrack {\alpha ,\pi }\right\rbrack \) as seen above, which implies

\[
{\int }_{\alpha }^{x}f\left( t\right) {dt} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\lambda }_{n}{\int }_{\alpha }^{x}\sin {ntdt} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\lambda }_{n}}{n}\left( {\cos {n\alpha } - \cos {nx}}\right) .
\]

\( \left( {* * }\right) \)

> Nous allons prouver que cette expression reste valable lorsque \( \alpha = 0 \) .

We will prove that this expression remains valid when \( \alpha = 0 \) .

> Pour tout \( t \in \rbrack 0,{2\pi }\lbrack \) , on note \( G\left( t\right) = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\lambda }_{n}\left( {\cos {nt}}\right) /n \) (la série converge simplement sur ] \( 0,{2\pi } \) [ car la suite \( \left( {{\lambda }_{n}/n}\right) \) est décroissante). Comme la suite \( \left( {{\lambda }_{n}/n}\right) \) est décroissante et tend vers 0 , on peut appliquer (*) qui entraîne

For all \( t \in \rbrack 0,{2\pi }\lbrack \) , we denote \( G\left( t\right) = \mathop{\sum }\limits_{{n = 1}}^{\infty }{\lambda }_{n}\left( {\cos {nt}}\right) /n \) (the series converges pointwise on ] \( 0,{2\pi } \) [ because the sequence \( \left( {{\lambda }_{n}/n}\right) \) is decreasing). Since the sequence \( \left( {{\lambda }_{n}/n}\right) \) is decreasing and tends to 0, we can apply (*) which implies

\[
\forall N \in  {\mathbb{N}}^{ * },\;\left| {\mathop{\sum }\limits_{{n \geq  N}}\frac{{\lambda }_{n}}{n}\cos \left( {n\frac{\pi }{3N}}\right) }\right|  \leq  \frac{{\lambda }_{N}}{N}\frac{3N\pi }{\pi } = 3{\lambda }_{N}
\]

Comme \( \cos \left( {{n\pi }/\left( {3N}\right) }\right) \geq \cos \left( {\pi /3}\right) = 1/2 \) pour \( 1 \leq n \leq N \) , on a donc

> Since \( \cos \left( {{n\pi }/\left( {3N}\right) }\right) \geq \cos \left( {\pi /3}\right) = 1/2 \) for \( 1 \leq n \leq N \) , we therefore have

\[
\forall N \in  {\mathbb{N}}^{ * },\;G\left( \frac{\pi }{3N}\right)  \geq  \frac{1}{2}\mathop{\sum }\limits_{{n = 1}}^{{N - 1}}\frac{{\lambda }_{n}}{n} - 3{\lambda }_{N}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 1}}^{{N - 1}}\frac{{\lambda }_{n}}{n} \leq  {2G}\left( \frac{\pi }{3N}\right)  + 6{\lambda }_{N}.
\]

(***)

> Comme \( f \) est continue en 0, l’égalité (**) montre que \( G\left( \alpha \right) \) converge lorsque \( \alpha \rightarrow {0}^{ + } \) , donc \( G \) est bornée au voisinage de \( {0}^{ + } \) , et (***) montre donc que la série \( \sum {\lambda }_{n}/n \) est majorée. Cette série converge donc (elle est à termes positifs), donc la série trigonométrique définissant \( G \) converge normalement sur \( \mathbb{R} \) . En particulier, ceci montre que \( G\left( \alpha \right) \) tend vers \( \sum {\lambda }_{n}/n \) lorsque \( \alpha \rightarrow 0 \) , et en faisant tendre \( \alpha \) vers 0 dans (*), on obtient

Since \( f \) is continuous at 0, equality (**) shows that \( G\left( \alpha \right) \) converges as \( \alpha \rightarrow {0}^{ + } \) , so \( G \) is bounded in the neighborhood of \( {0}^{ + } \) , and (***) therefore shows that the series \( \sum {\lambda }_{n}/n \) is bounded above. This series therefore converges (it has positive terms), so the trigonometric series defining \( G \) converges normally on \( \mathbb{R} \) . In particular, this shows that \( G\left( \alpha \right) \) tends to \( \sum {\lambda }_{n}/n \) as \( \alpha \rightarrow 0 \) , and by letting \( \alpha \) tend to 0 in (*), we obtain

\[
\forall x \in  \rbrack 0,\pi \rbrack ,\;F\left( x\right)  = {\int }_{0}^{x}f\left( t\right) {dt} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\lambda }_{n}}{n}\left( {1 - \cos {nx}}\right) .
\]

Les termes de la série de l'expression précédente sont positifs donc

> The terms of the series in the previous expression are positive, therefore

\[
\forall N \in  \mathbb{N},\;F\left( \frac{\pi }{N}\right)  \geq  \mathop{\sum }\limits_{{N/2 < n \leq  N}}\frac{{\lambda }_{n}}{n}\left( {1 - \cos \left( \frac{n\pi }{N}\right) }\right)  \geq  \mathop{\sum }\limits_{{N/2 < n \leq  N}}\frac{{\lambda }_{n}}{n} \geq  \frac{N}{2}\frac{{\lambda }_{N}}{N} = \frac{{\lambda }_{N}}{2},
\]

autrement dit \( 0 \leq {\lambda }_{N} \leq {2F}\left( {\pi /N}\right) \) . Comme \( f \) est continue et nulle en 0, on a \( F\left( x\right) = o\left( x\right) \) lorsque \( x \rightarrow 0 \) donc \( {\lambda }_{N} = o\left( {\pi /N}\right) = o\left( {1/N}\right) \) d’où le résultat.

> in other words \( 0 \leq {\lambda }_{N} \leq {2F}\left( {\pi /N}\right) \) . Since \( f \) is continuous and zero at 0, we have \( F\left( x\right) = o\left( x\right) \) as \( x \rightarrow 0 \) so \( {\lambda }_{N} = o\left( {\pi /N}\right) = o\left( {1/N}\right) \) hence the result.

Remarque. Si on suppose \( f \) bornée au voisinage de 0, on a \( {\lambda }_{n} = O\left( {1/n}\right) \) (immédiat à partir de l’inégalité \( 0 \leq {\lambda }_{N} \leq {2F}\left( {\pi /N}\right) \) obtenue à la fin de la solution de la question d), et le fait que \( F\left( x\right) = O\left( x\right) \) lorsque \( x \rightarrow 0 \) ).

> Remark. If we assume \( f \) is bounded in the neighborhood of 0, we have \( {\lambda }_{n} = O\left( {1/n}\right) \) (immediate from the inequality \( 0 \leq {\lambda }_{N} \leq {2F}\left( {\pi /N}\right) \) obtained at the end of the solution to question d), and the fact that \( F\left( x\right) = O\left( x\right) \) as \( x \rightarrow 0 \) ).
