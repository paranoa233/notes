#### 5.4. The Jordan-Dirichlet theorem

*Français : 5.4.Le théorème de Jordan-Dirichlet*

Le résultat qui suit est le résultat principal sur les séries de Fourier.

> The following result is the main result on Fourier series.

THÉORÉME 2 (JORDAN-DIRICHLET). Soient \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction \( {2\pi } \) -périodique, continue par morceaux sur \( \mathbb{R} \) et \( {t}_{0} \in \mathbb{R} \) tels que la fonction

> THEOREM 2 (JORDAN-DIRICHLET). Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \)-periodic function, piecewise continuous on \( \mathbb{R} \) and \( {t}_{0} \in \mathbb{R} \) such that the function

\[
h \mapsto  \frac{f\left( {{t}_{0} + h}\right)  + f\left( {{t}_{0} - h}\right)  - f\left( {{t}_{0} + }\right)  - f\left( {{t}_{0} - }\right) }{h}
\]

est bornée au voisinage de 0 . Alors \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}\left( f\right) {e}^{{in}{t}_{0}} \) converge et on a

> is bounded in the neighborhood of 0. Then \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{c}_{n}\left( f\right) {e}^{{in}{t}_{0}} \) converges and we have

\[
\mathop{\sum }\limits_{{-\infty }}^{{+\infty }}{c}_{n}\left( f\right) {e}^{{in}{t}_{0}} = \frac{f\left( {{t}_{0} + }\right)  + f\left( {{t}_{0} - }\right) }{2}.
\]

Démonstration. Quitte à effectuer une translation \( t \mapsto t + {t}_{0} \) , on peut supposer \( {t}_{0} = 0 \) . Pour tout \( n \in \mathbb{N} \) , on note \( {s}_{n} = \mathop{\sum }\limits_{{-n}}^{n}{c}_{k}\left( f\right) \) . Il s’agit de montrer que la suite \( \left( {u}_{n}\right) \) définie par \( {u}_{n} = \; {s}_{n} - \left( {f\left( {0 + }\right) + f\left( {0 - }\right) }\right) /2 \) tend vers 0 .

> Proof. By performing a translation \( t \mapsto t + {t}_{0} \), we can assume \( {t}_{0} = 0 \). For all \( n \in \mathbb{N} \), we denote \( {s}_{n} = \mathop{\sum }\limits_{{-n}}^{n}{c}_{k}\left( f\right) \). It is a matter of showing that the sequence \( \left( {u}_{n}\right) \) defined by \( {u}_{n} = \; {s}_{n} - \left( {f\left( {0 + }\right) + f\left( {0 - }\right) }\right) /2 \) tends to 0.

On a

> We have

\[
{2\pi }{s}_{n} = \mathop{\sum }\limits_{{k =  - n}}^{n}{\int }_{-\pi }^{\pi }f\left( t\right) {e}^{-{ipt}}{dt} = {\int }_{-\pi }^{\pi }f\left( t\right) {D}_{n}\left( t\right) {dt},\;\text{ où }\;\forall t \in  \mathbb{R},\;{D}_{n}\left( t\right)  = \mathop{\sum }\limits_{{k =  - n}}^{n}{e}^{ikt}.
\]

(*)

> Le polynôme trigonométrique \( {D}_{n}\left( t\right) \) s’appelle noyau de Dirichlet, on le rencontre souvent lors de l'étude de séries de Fourier. Il peut être calculé explicitement :

The trigonometric polynomial \( {D}_{n}\left( t\right) \) is called the Dirichlet kernel; it is often encountered when studying Fourier series. It can be calculated explicitly:

\[
\forall t \in  \mathbb{R} \smallsetminus  {2\pi }\mathbb{Z},\;{D}_{n}\left( t\right)  = {e}^{-{int}}\frac{{e}^{i\left( {{2n} + 1}\right) t} - 1}{{e}^{it} - 1} = \frac{\sin \left( {\left( {{2n} + 1}\right) t/2}\right) }{\sin \left( {t/2}\right) }.
\]

Par ailleurs, \( {D}_{n} \) est une fonction paire, donc

> Furthermore, \( {D}_{n} \) is an even function, so

\[
{\int }_{-\pi }^{0}f\left( t\right) {D}_{n}\left( t\right) {dt} = {\int }_{0}^{\pi }f\left( {-t}\right) {D}_{n}\left( t\right) {dt}\text{ d’où }{2\pi }{s}_{n} = {\int }_{0}^{\pi }\left( {f\left( t\right)  + f\left( {-t}\right) }\right) {D}_{n}\left( t\right) {dt}.
\]

On en déduit finalement

> We finally deduce

\[
{2\pi }{u}_{n} = {\int }_{0}^{\pi }\left( {f\left( t\right)  + f\left( {-t}\right)  - f\left( {0 + }\right)  - f\left( {0 - }\right) }\right) {D}_{n}\left( t\right) {dt} = {\int }_{0}^{\pi }g\left( t\right) \sin \left( \frac{\left( {{2n} + 1}\right) t}{2}\right) {dt},
\]

où \( g\left( t\right) = \left( {f\left( t\right) + f\left( {-t}\right) - f\left( {0 + }\right) - f\left( {0 - }\right) }\right) /\sin \left( {t/2}\right) \) est continue par morceaux sur \( \rbrack 0,\pi \rbrack \) et bornée sur un voisinage de 0 d’après les hypothèses. La fonction \( g \) est donc intégrable sur \( \rbrack 0,\pi \rbrack \) et le lemme de Riemann-Lebesgue (voir l’exercice 6 page 157) entraîne \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{2\pi }{u}_{n} = 0 \) , d’où le résultat.

> where \( g\left( t\right) = \left( {f\left( t\right) + f\left( {-t}\right) - f\left( {0 + }\right) - f\left( {0 - }\right) }\right) /\sin \left( {t/2}\right) \) is piecewise continuous on \( \rbrack 0,\pi \rbrack \) and bounded in a neighborhood of 0 according to the hypotheses. The function \( g \) is therefore integrable on \( \rbrack 0,\pi \rbrack \) and the Riemann-Lebesgue lemma (see exercise 6 page 157) implies \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{2\pi }{u}_{n} = 0 \) , hence the result.

\( \rightarrow \) COROLLAIRE 1. Si \( f \) est \( {2\pi } \) -périodique et de classe \( {\mathcal{C}}^{1} \) par morceaux, alors pour tout \( x \in \mathbb{R} \) , la série de Fourier de \( f \) converge en ce point \( x \) vers \( \frac{f\left( {x + }\right) + f\left( {x - }\right) }{2} \) . En particulier, si \( f \) est continue en \( x \) , la série de Fourier de \( f \) en \( x \) converge vers \( f\left( x\right) \) .

> \( \rightarrow \) COROLLARY 1. If \( f \) is \( {2\pi } \) -periodic and piecewise \( {\mathcal{C}}^{1} \) , then for any \( x \in \mathbb{R} \) , the Fourier series of \( f \) converges at this point \( x \) to \( \frac{f\left( {x + }\right) + f\left( {x - }\right) }{2} \) . In particular, if \( f \) is continuous at \( x \) , the Fourier series of \( f \) at \( x \) converges to \( f\left( x\right) \) .

Remarque 7. L’hypothèse \( {\mathcal{C}}^{1} \) par morceaux est importante. Il existe en effet des fonctions continues dont la série de Fourier diverge (voir l'exercice 4 page 275).

> Remark 7. The hypothesis of being piecewise \( {\mathcal{C}}^{1} \) is important. Indeed, there exist continuous functions whose Fourier series diverges (see exercise 4 page 275).

##### Uniform convergence of the Fourier series.

*Français : Convergence uniforme de la série de Fourier.*

LEMME 1. Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction \( {2\pi } \) -périodique, continue et \( {\mathcal{C}}^{1} \) par morceaux. On définit \( \varphi : \mathbb{R} \rightarrow \mathbb{C} \) par \( \varphi \left( t\right) = {f}^{\prime }\left( t\right) \) si \( f \) est dérivable en \( t \) et \( \varphi \left( t\right) = \left( {{f}^{\prime }\left( {t + }\right) + {f}^{\prime }\left( {t - }\right) }\right) /2 \) sinon. Les coefficients de Fourier de \( \varphi \) vérifient \( {c}_{n}\left( \varphi \right) = {in}{c}_{n}\left( f\right) \) pour tout \( n \in \mathbb{Z} \) .

> LEMMA 1. Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \) -periodic, continuous, and piecewise \( {\mathcal{C}}^{1} \) function. We define \( \varphi : \mathbb{R} \rightarrow \mathbb{C} \) by \( \varphi \left( t\right) = {f}^{\prime }\left( t\right) \) if \( f \) is differentiable at \( t \) and \( \varphi \left( t\right) = \left( {{f}^{\prime }\left( {t + }\right) + {f}^{\prime }\left( {t - }\right) }\right) /2 \) otherwise. The Fourier coefficients of \( \varphi \) satisfy \( {c}_{n}\left( \varphi \right) = {in}{c}_{n}\left( f\right) \) for all \( n \in \mathbb{Z} \) .

Démonstration. Soit \( 0 = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = {2\pi } \) une subdivision de \( \left\lbrack {0,{2\pi }}\right\rbrack \) telle que \( f \) soit \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {{x}_{k - 1},{x}_{k}}\right\rbrack \) pour tout \( k \) . En intégrant par parties, on a pour tout \( k \)

> Proof. Let \( 0 = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = {2\pi } \) be a subdivision of \( \left\lbrack {0,{2\pi }}\right\rbrack \) such that \( f \) is \( {\mathcal{C}}^{1} \) on \( \left\lbrack {{x}_{k - 1},{x}_{k}}\right\rbrack \) for all \( k \) . By integrating by parts, we have for all \( k \)

\[
{\int }_{{x}_{k - 1}}^{{x}_{k}}\varphi \left( t\right) {e}^{-{int}}{dt} = {\left\lbrack  f\left( t\right) {e}^{-{int}}\right\rbrack  }_{{x}_{k - 1}}^{{x}_{k}} + {in}{\int }_{{x}_{k - 1}}^{{x}_{k}}f\left( t\right) {e}^{-{int}}{dt},
\]

puis la fonction \( f \) étant continue, on obtient en sommant cette relation sur \( k \) ,

> then, since the function \( f \) is continuous, we obtain by summing this relation over \( k \) ,

\[
{c}_{n}\left( \varphi \right)  = {\int }_{0}^{2\pi }\varphi \left( t\right) {e}^{-{int}}{dt} = {\left\lbrack  f\left( t\right) {e}^{-{int}}\right\rbrack  }_{0}^{2\pi } + {in}{\int }_{0}^{2\pi }f\left( t\right) {e}^{-{int}}{dt} = {in}{\int }_{0}^{2\pi }f\left( t\right) {e}^{-{int}}{dt} = {in}{c}_{n}\left( f\right) .
\]

\( \rightarrow \) THÉORÉME 3. Si \( f : \mathbb{R} \rightarrow \mathbb{C} \) est une fonction \( {2\pi } \) -périodique, continue et \( {\mathcal{C}}^{1} \) par morceaux, alors la série de Fourier de \( f \) converge normalement vers \( f \) sur \( \mathbb{R} \) .

> \( \rightarrow \) THEOREM 3. If \( f : \mathbb{R} \rightarrow \mathbb{C} \) is a \( {2\pi } \) -periodic, continuous, and piecewise \( {\mathcal{C}}^{1} \) function, then the Fourier series of \( f \) converges normally to \( f \) on \( \mathbb{R} \) .

Démonstration. En reprenant les notations du lemme précédent, on a \( {c}_{n}\left( \varphi \right) = {in}{c}_{n}\left( f\right) \) . Ainsi,

> Proof. Using the notation from the previous lemma, we have \( {c}_{n}\left( \varphi \right) = {in}{c}_{n}\left( f\right) \) . Thus,

\[
\forall n \in  {\mathbb{Z}}^{ * },\;\left| {{c}_{n}\left( f\right) }\right|  = \left| \frac{{c}_{n}\left( \varphi \right) }{n}\right|  \leq  \frac{1}{2}\left( {{\left| {c}_{n}\left( \varphi \right) \right| }^{2} + \frac{1}{{n}^{2}}}\right) ,
\]

et comme \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( \varphi \right) \right| }^{2} \) converge (voir l’égalité de Parseval), on en déduit que \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{c}_{n}\left( f\right) }\right| \) converge, d'où le résultat avec le corollaire 1.

> and since \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( \varphi \right) \right| }^{2} \) converges (see Parseval's identity), we deduce that \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{c}_{n}\left( f\right) }\right| \) converges, hence the result with corollary 1.
