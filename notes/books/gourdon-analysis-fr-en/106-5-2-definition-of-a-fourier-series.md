#### 5.2. Definition of a Fourier series

*Français : 5.2. Définition d'une série de Fourier*

DÉFINITION 3. Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une application \( {2\pi } \) -périodique et continue par morceaux sur \( \mathbb{R} \) . On appelle coefficients de Fourier de \( f \) les nombres complexes définis par

> DEFINITION 3. Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \)-periodic mapping that is piecewise continuous on \( \mathbb{R} \). The complex numbers defined by are called the Fourier coefficients of \( f \)

\[
\forall n \in  \mathbb{Z},\;{c}_{n}\left( f\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( t\right) {e}^{-{int}}{dt}
\]

\[
\forall n \in  \mathbb{N},\;{a}_{n}\left( f\right)  = \frac{1}{\pi }{\int }_{0}^{2\pi }f\left( t\right) \cos {ntdt},\;\forall n \in  {\mathbb{N}}^{ * },\;{b}_{n}\left( f\right)  = \frac{1}{\pi }{\int }_{0}^{2\pi }f\left( t\right) \sin {ntdt}.
\]

On appelle série de Fourier associée à \( f \) la série trigonométrique

> The trigonometric series is called the Fourier series associated with \( f \)

\[
\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{c}_{n}\left( f\right) {e}^{inx}\;\text{ ou encore }\;\frac{{a}_{0}\left( f\right) }{2} + \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\left( {{a}_{n}\left( f\right) \cos {nx} + {b}_{n}\left( f\right) \sin {nx}}\right) .
\]

Notez que les coefficients de Fourier vérifient les relations

> Note that the Fourier coefficients satisfy the relations

\[
\forall n \in  \mathbb{N},\;{a}_{n}\left( f\right)  = {c}_{n}\left( f\right)  + {c}_{-n}\left( f\right) ,\;\forall n \in  {\mathbb{N}}^{ * },\;{b}_{n}\left( f\right)  = i\left( {{c}_{n}\left( f\right)  - {c}_{-n}\left( f\right) }\right)
\]

et que les deux dernières séries trigonométriques sont égales, car

> and that the last two trigonometric series are equal, because

\[
{c}_{n}\left( f\right) {e}^{inx} + {c}_{-n}\left( f\right) {e}^{-{inx}} = {a}_{n}\left( f\right) \cos {nx} + {b}_{n}\left( f\right) \sin {nx}.
\]

Remarque 4. - Les intégrandes étant \( {2\pi } \) -périodiques, on peut remplacer l’intervalle d’intégration \( \left\lbrack {0,{2\pi }}\right\rbrack \) par n’importe quel intervalle de longueur \( {2\pi } \) .

> Remark 4. - Since the integrands are \( {2\pi } \)-periodic, the interval of integration \( \left\lbrack {0,{2\pi }}\right\rbrack \) can be replaced by any interval of length \( {2\pi } \).

- On utilise en général les coefficients \( {a}_{n}\left( f\right) ,{b}_{n}\left( f\right) \) lorsque \( f \) est à valeurs réelles.

> - We generally use the coefficients \( {a}_{n}\left( f\right) ,{b}_{n}\left( f\right) \) when \( f \) is real-valued.

- Si \( f \) est paire (resp. impaire), les coefficients \( {b}_{n}\left( f\right) \) (resp. \( {a}_{n}\left( f\right) \) ) sont nuls.

> - If \( f \) is even (resp. odd), the coefficients \( {b}_{n}\left( f\right) \) (resp. \( {a}_{n}\left( f\right) \)) are zero.

— Une série trigonométrique qui converge uniformément sur \( \mathbb{R} \) est égale à sa série de Fourier.

> — A trigonometric series that converges uniformly on \( \mathbb{R} \) is equal to its Fourier series.

- Si \( f \) est \( T \) -périodique, on peut également définir les coefficients de Fourier de \( f \) par

> - If \( f \) is \( T \)-periodic, one can also define the Fourier coefficients of \( f \) by

\[
{c}_{n}\left( f\right)  = \frac{1}{T}{\int }_{0}^{T}f\left( t\right) \exp \left( {-i\frac{2\pi }{T}{nt}}\right) {dt}
\]

\[
{a}_{n}\left( f\right)  = \frac{2}{T}{\int }_{0}^{T}f\left( t\right) \cos \left( {\frac{2\pi }{T}{nt}}\right) {dt},\;{b}_{n}\left( f\right)  = \frac{2}{T}{\int }_{0}^{T}f\left( t\right) \sin \left( {\frac{2\pi }{T}{nt}}\right) {dt}.
\]

et avec \( \omega = {2\pi }/T \) , la série de Fourier associée à \( f \) est

> and with \( \omega = {2\pi }/T \), the Fourier series associated with \( f \) is

\[
\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{c}_{n}\left( f\right) {e}^{i\omega nx}\;\text{ ou encore }\;\frac{{a}_{0}\left( f\right) }{2} + \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\left( {{a}_{n}\left( f\right) \cos {\omega nx} + {b}_{n}\left( f\right) \sin {\omega nx}}\right) .
\]

Dans la suite de cette partie, la période sera toujours \( T = {2\pi } \) mais les résultats se généralisent aisément par normalisation pour toute période \( T > 0 \) .

> In the remainder of this part, the period will always be \( T = {2\pi } \), but the results are easily generalized by normalization for any period \( T > 0 \).

L'espace D. Nous aurons besoin de la définition suivante.

> The space D. We will need the following definition.

DéFINITION 4. Une application \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) (où \( \left\lbrack {a, b}\right\rbrack \) est un segment de \( \mathbb{R} \) ) est dite de classe \( {\mathcal{C}}^{n} \) par morceaux sur \( \left\lbrack {a, b}\right\rbrack \) s’il existe une subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que pour tout \( i \in \{ 0,\ldots , p - 1\} \) , la restriction de \( f \) à l’intervalle \( \rbrack {x}_{i},{x}_{i + 1}\lbrack \) est prolongeable par continuité sur \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) en une fonction de classe \( {\mathcal{C}}^{n} \) sur \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) .

> DEFINITION 4. A mapping \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) (where \( \left\lbrack {a, b}\right\rbrack \) is a segment of \( \mathbb{R} \) ) is said to be piecewise \( {\mathcal{C}}^{n} \) on \( \left\lbrack {a, b}\right\rbrack \) if there exists a subdivision \( a = {x}_{0} < {x}_{1} < \cdots < {x}_{p} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that for all \( i \in \{ 0,\ldots , p - 1\} \) , the restriction of \( f \) to the interval \( \rbrack {x}_{i},{x}_{i + 1}\lbrack \) can be extended by continuity to \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) as a function of class \( {\mathcal{C}}^{n} \) on \( \left\lbrack {{x}_{i},{x}_{i + 1}}\right\rbrack \) .

Une application \( f : \mathbb{R} \rightarrow \mathbb{C} \) est dite de classe \( {\mathcal{C}}^{n} \) par morceaux si la restriction de \( f \) a tout segment de \( \mathbb{R} \) est de classe \( {\mathcal{C}}^{n} \) par morceaux.

> A mapping \( f : \mathbb{R} \rightarrow \mathbb{C} \) is said to be piecewise \( {\mathcal{C}}^{n} \) if the restriction of \( f \) to any segment of \( \mathbb{R} \) is piecewise \( {\mathcal{C}}^{n} \) .

Une fonction \( f \) de classe \( {\mathcal{C}}^{n} \) par morceaux admet donc en tout point \( x \) une limite à gauche et à droite, que nous notons respectivement \( f\left( {x - }\right) \) et \( f\left( {x + }\right) \) .

> A function \( f \) that is piecewise \( {\mathcal{C}}^{n} \) therefore admits a left-hand and right-hand limit at every point \( x \) , which we denote respectively as \( f\left( {x - }\right) \) and \( f\left( {x + }\right) \) .

Notation. On note \( D \) l’e.v des fonctions de \( \mathbb{R} \) dans \( \mathbb{C},{2\pi } \) -périodiques, continues par morceaux, et telles que

> Notation. We denote by \( D \) the vector space of \( \mathbb{R} \) -periodic functions from \( \mathbb{C},{2\pi } \) that are piecewise continuous and such that

\[
\forall x \in  \mathbb{R},\;f\left( x\right)  = \frac{f\left( {x - }\right)  + f\left( {x + }\right) }{2}.
\]
