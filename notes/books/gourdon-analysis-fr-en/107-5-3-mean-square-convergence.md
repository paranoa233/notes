#### 5.3. Mean square convergence

*Français : 5.3. Convergence en moyenne quadratique*

Structure préhilbertienne de D. Sur l'e.v D, l'application

> Prehilbertian structure of D. On the vector space D, the mapping

\[
\left( {f, g}\right)  \mapsto  \langle f, g\rangle  = \frac{1}{2\pi }{\int }_{0}^{2\pi }\overline{f\left( t\right) }g\left( t\right) {dt}
\]

définit un produit scalaire et fait de \( D \) un espace préhilbertien complexe, muni de la norme hermitienne \( \parallel f{\parallel }_{2} = \sqrt{\langle f, f\rangle } \) .

> defines an inner product and makes \( D \) a complex prehilbertian space, equipped with the Hermitian norm \( \parallel f{\parallel }_{2} = \sqrt{\langle f, f\rangle } \) .

En notant, pour tout \( n \in \mathbb{Z},{e}_{n} \) l’application \( x \mapsto {e}^{inx},{\left( {e}_{n}\right) }_{n \in \mathbb{Z}} \) constitue une famille libre orthonormale de \( D \) vis-à-vis du produit scalaire défini précédemment.

> By denoting, for all \( n \in \mathbb{Z},{e}_{n} \) , the mapping \( x \mapsto {e}^{inx},{\left( {e}_{n}\right) }_{n \in \mathbb{Z}} \) constitutes an orthonormal free family of \( D \) with respect to the previously defined inner product.

Proposition 3. Soient \( n \in \mathbb{N} \) et \( f \in D \) . Le sous-espace vectoriel \( {\mathcal{P}}_{n} = \operatorname{Vect}{\left( {e}_{k}\right) }_{-n \leq k \leq n} \) vérifie \( {\mathcal{P}}_{n} \oplus {\mathcal{P}}_{n}^{ \bot } = D \) . La projection orthogonale \( {p}_{n} \) sur \( {\mathcal{P}}_{n} \) vérifie

> Proposition 3. Let \( n \in \mathbb{N} \) and \( f \in D \) . The vector subspace \( {\mathcal{P}}_{n} = \operatorname{Vect}{\left( {e}_{k}\right) }_{-n \leq k \leq n} \) satisfies \( {\mathcal{P}}_{n} \oplus {\mathcal{P}}_{n}^{ \bot } = D \) . The orthogonal projection \( {p}_{n} \) onto \( {\mathcal{P}}_{n} \) satisfies

\[
{s}_{n} = \mathop{\sum }\limits_{{k =  - n}}^{n}{c}_{k}\left( f\right) {e}_{k} = {p}_{n}\left( f\right)
\]

et de plus

> and furthermore

\[
\mathop{\inf }\limits_{{g \in  {\mathcal{P}}_{n}}}\parallel f - g{\parallel }_{2}^{2} = {\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2}^{2} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} - \mathop{\sum }\limits_{{k =  - n}}^{n}{\left| {c}_{k}\left( f\right) \right| }^{2}.
\]

(*)

> Démonstration. Cette proposition est en fait une conséquence directe des résultats généraux sur les espaces préhilbertiens (voir tome Algèbre) appliqués à \( D \) . Nous le redémontrons dans notre cas.

Proof. This proposition is in fact a direct consequence of the general results on prehilbertian spaces (see Algebra volume) applied to \( D \) . We re-prove it for our case.

> On remarque que \( {c}_{k}\left( f\right) = \left\langle {{e}_{k}, f}\right\rangle = \left\langle {{e}_{k},{s}_{n}}\right\rangle \) si \( - n \leq k \leq n \) , donc \( \left\langle {{e}_{k}, f - {s}_{n}}\right\rangle = 0 \) pour \( - n \leq k \leq n \) . Autrement dit, \( f - {s}_{n} \in {\mathcal{P}}_{n}^{ \bot } \) . Comme \( f = {s}_{n} + \left( {f - {s}_{n}}\right) \) avec \( {s}_{n} \in {\mathcal{P}}_{n} \) (et que ceci est vrai pour tout \( f \in D \) ), on en déduit \( D = {\mathcal{P}}_{n} + {\mathcal{P}}_{n}^{ \bot } \) . Par ailleurs \( {\mathcal{P}}_{n} \cap {\mathcal{P}}_{n}^{ \bot } = \{ 0\} \) car si \( g = \mathop{\sum }\limits_{{-n < k < n}}{\lambda }_{k}{e}_{k} \in {\mathcal{P}}_{n}^{ \bot } \) , alors \( {\lambda }_{k} = \left\langle {g,{e}_{k}}\right\rangle = 0 \) . Finalement on a bien \( D = {\mathcal{P}}_{n} \oplus {\mathcal{P}}_{n}^{ \bot } \) .

We note that \( {c}_{k}\left( f\right) = \left\langle {{e}_{k}, f}\right\rangle = \left\langle {{e}_{k},{s}_{n}}\right\rangle \) if \( - n \leq k \leq n \) , so \( \left\langle {{e}_{k}, f - {s}_{n}}\right\rangle = 0 \) for \( - n \leq k \leq n \) . In other words, \( f - {s}_{n} \in {\mathcal{P}}_{n}^{ \bot } \) . Since \( f = {s}_{n} + \left( {f - {s}_{n}}\right) \) with \( {s}_{n} \in {\mathcal{P}}_{n} \) (and this is true for any \( f \in D \) ), we deduce \( D = {\mathcal{P}}_{n} + {\mathcal{P}}_{n}^{ \bot } \) . Furthermore \( {\mathcal{P}}_{n} \cap {\mathcal{P}}_{n}^{ \bot } = \{ 0\} \) because if \( g = \mathop{\sum }\limits_{{-n < k < n}}{\lambda }_{k}{e}_{k} \in {\mathcal{P}}_{n}^{ \bot } \) , then \( {\lambda }_{k} = \left\langle {g,{e}_{k}}\right\rangle = 0 \) . Finally, we indeed have \( D = {\mathcal{P}}_{n} \oplus {\mathcal{P}}_{n}^{ \bot } \) .

> On a montré que \( f = {s}_{n} + \left( {f - {s}_{n}}\right) \) avec \( f - {s}_{n} \in {\mathcal{P}}_{n}^{ \bot } \) , donc \( {s}_{n} = {p}_{n}\left( f\right) \) . Les éléments \( {s}_{n} \) et \( f - {s}_{n} \) sont orthogonaux, donc \( {\begin{Vmatrix}{s}_{n}\end{Vmatrix}}_{2}^{2} + {\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2}^{2} = \parallel f{\parallel }_{2}^{2} \) , ce qui fournit la dernière égalité de (*). Par ailleurs, pour tout \( g \in {\mathcal{P}}_{n} \) , on a

We have shown that \( f = {s}_{n} + \left( {f - {s}_{n}}\right) \) with \( f - {s}_{n} \in {\mathcal{P}}_{n}^{ \bot } \) , so \( {s}_{n} = {p}_{n}\left( f\right) \) . The elements \( {s}_{n} \) and \( f - {s}_{n} \) are orthogonal, so \( {\begin{Vmatrix}{s}_{n}\end{Vmatrix}}_{2}^{2} + {\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2}^{2} = \parallel f{\parallel }_{2}^{2} \) , which provides the last equality of (*). Furthermore, for any \( g \in {\mathcal{P}}_{n} \) , we have

\[
\parallel f - g{\parallel }_{2}^{2} = {\begin{Vmatrix}\left( f - {s}_{n}\right)  + \left( {s}_{n} - g\right) \end{Vmatrix}}_{2}^{2} = {\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2}^{2} + {\begin{Vmatrix}{s}_{n} - g\end{Vmatrix}}_{2}^{2} \geq  {\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2}^{2},
\]

et ceci fournit la première égalité de (*).

> and this provides the first equality of (*).

Remarque 5. - On interprète (*) en disant que parmi les polynômes trigonométriques de degré \( \leq n,{s}_{n} \) est celui qui se rapproche le plus de \( f \) en moyenne quadratique.

> Remark 5. - We interpret (*) by saying that among the trigonometric polynomials of degree \( \leq n,{s}_{n} \) is the one that is closest to \( f \) in the mean square sense.

- La formule (*) montre que \( \mathop{\sum }\limits_{{-n}}^{n}{\left| {c}_{k}\left( f\right) \right| }^{2} \leq  \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} \) pour tout \( n > 0 \) . Ainsi, la série \( \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \) converge et la somme de cette série vérifie

> - The formula (*) shows that \( \mathop{\sum }\limits_{{-n}}^{n}{\left| {c}_{k}\left( f\right) \right| }^{2} \leq  \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} \) for any \( n > 0 \) . Thus, the series \( \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \) converges and the sum of this series satisfies

\[
\mathop{\sum }\limits_{{-\infty }}^{{+\infty }}{\left| {c}_{n}\left( f\right) \right| }^{2} \leq  \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt}\;\text{ (inégalité de Bessel). }
\]

En fait, cette inégalité est une égalité (dans ce cas on parle d'égalité de Parseval), comme il est énoncé dans le théorème qui suit.

> In fact, this inequality is an equality (in this case we speak of Parseval's identity), as stated in the theorem that follows.

##### Parseval's identity.

*Français : Égalité de Parseval.*

\( \rightarrow \) THÉORÉME 1 (ÉGALITÉ DE PARSEVAL). Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction \( {2\pi } \) -périodique et continue par morceaux. Alors les séries \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2},\sum {\left| {a}_{n}\left( f\right) \right| }^{2},\sum {\left| {b}_{n}\left( f\right) \right| }^{2} \) convergent et on a

> \( \rightarrow \) THEOREM 1 (PARSEVAL'S IDENTITY). Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a \( {2\pi } \)-periodic piecewise continuous function. Then the series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2},\sum {\left| {a}_{n}\left( f\right) \right| }^{2},\sum {\left| {b}_{n}\left( f\right) \right| }^{2} \) converge and we have

\[
\mathop{\sum }\limits_{{-\infty }}^{{+\infty }}{\left| {c}_{n}\left( f\right) \right| }^{2} = \frac{{\left| {a}_{0}\left( f\right) \right| }^{2}}{4} + \frac{1}{2}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left| {a}_{n}\left( f\right) \right| }^{2} + \frac{1}{2}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left| {b}_{n}\left( f\right) \right| }^{2} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt}.
\]

Démonstration. Quitte à changer la valeur de \( f \) en ses discontinuités, on peut supposer \( f \in D \) (la valeurs des intégrales faisant intervenir \( f \) ne change pas). Il suffit de prouver le résultat sur la série \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \) car les relations liant les \( {a}_{n}\left( f\right) ,{b}_{n}\left( f\right) \) aux \( {c}_{n}\left( f\right) \) entraînent \( {\left| {c}_{n}\left( f\right) \right| }^{2} + {\left| {c}_{-n}\left( f\right) \right| }^{2} = \; \left( {{\left| {a}_{n}\left( f\right) \right| }^{2} + {\left| {b}_{n}\left( f\right) \right| }^{2}}\right) /2 \) pour tout \( n \in {\mathbb{N}}^{ * } \) et \( {\left| {c}_{0}\left( f\right) \right| }^{2} = {\left| {a}_{0}\left( f\right) \right| }^{2}/4 \) .

> Proof. By modifying the value of \( f \) at its discontinuities, we can assume \( f \in D \) (the values of the integrals involving \( f \) do not change). It suffices to prove the result for the series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \) because the relations linking the \( {a}_{n}\left( f\right) ,{b}_{n}\left( f\right) \) to the \( {c}_{n}\left( f\right) \) imply \( {\left| {c}_{n}\left( f\right) \right| }^{2} + {\left| {c}_{-n}\left( f\right) \right| }^{2} = \; \left( {{\left| {a}_{n}\left( f\right) \right| }^{2} + {\left| {b}_{n}\left( f\right) \right| }^{2}}\right) /2 \) for all \( n \in {\mathbb{N}}^{ * } \) and \( {\left| {c}_{0}\left( f\right) \right| }^{2} = {\left| {a}_{0}\left( f\right) \right| }^{2}/4 \) .

La proposition précédente donne

> The previous proposition gives

\[
\frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( t\right) \right| }^{2}{dt} - \mathop{\sum }\limits_{{-\infty }}^{{+\infty }}{\left| {c}_{n}\left( f\right) \right| }^{2} = \mathop{\inf }\limits_{{g \in  \mathcal{P}}}\parallel f - g{\parallel }_{2}^{2},
\]

\( \left( {* * }\right) \)

> où \( \mathcal{P} \) désigne l’e.v des polynômes trigonométriques.

where \( \mathcal{P} \) denotes the vector space of trigonometric polynomials.

> Si \( f \) est continue, on sait (conséquence du théorème de Fejér, voir le problème 25 page 306) qu’il existe une suite de polynômes trigonométriques \( \left( {g}_{n}\right) \) qui converge uniformément vers \( f \) sur \( \mathbb{R} \) , et donc \( {\begin{Vmatrix}f - {g}_{n}\end{Vmatrix}}_{2}^{2} \) tend vers 0, ce qui montre \( \mathop{\inf }\limits_{{g \in \mathcal{P}}}\parallel f - g{\parallel }_{2}^{2} = 0 \) , d’où l’égalité de Parseval d'après (**).

If \( f \) is continuous, we know (as a consequence of Fejér's theorem, see problem 25 on page 306) that there exists a sequence of trigonometric polynomials \( \left( {g}_{n}\right) \) that converges uniformly to \( f \) on \( \mathbb{R} \) , and thus \( {\begin{Vmatrix}f - {g}_{n}\end{Vmatrix}}_{2}^{2} \) tends to 0, which shows \( \mathop{\inf }\limits_{{g \in \mathcal{P}}}\parallel f - g{\parallel }_{2}^{2} = 0 \) , hence Parseval's identity according to (**).

> Si \( f \in D \) n’est pas continue, on peut montrer (c’est facile et peu intéressant) que pour tout \( \varepsilon > 0 \) , il existe une fonction \( \widetilde{f} \in D \) continue telle que \( \parallel f - \widetilde{f}{\parallel }_{2} < \varepsilon \) . Comme on l’a vu précédemment, il existe \( g \in \mathcal{P} \) tel que \( \parallel \widetilde{f} - g{\parallel }_{2} < \varepsilon \) , donc finalement \( \parallel f - g\parallel < {2\varepsilon } \) . Ceci est possible pour tout \( \varepsilon > 0 \) , donc \( \mathop{\inf }\limits_{{g \in \mathcal{P}}}\parallel f - g{\parallel }_{2}^{2} = 0 \) , d’où le résultat d’après (**).

If \( f \in D \) is not continuous, one can show (it is easy and of little interest) that for any \( \varepsilon > 0 \) , there exists a continuous function \( \widetilde{f} \in D \) such that \( \parallel f - \widetilde{f}{\parallel }_{2} < \varepsilon \) . As seen previously, there exists \( g \in \mathcal{P} \) such that \( \parallel \widetilde{f} - g{\parallel }_{2} < \varepsilon \) , so finally \( \parallel f - g\parallel < {2\varepsilon } \) . This is possible for any \( \varepsilon > 0 \) , therefore \( \mathop{\inf }\limits_{{g \in \mathcal{P}}}\parallel f - g{\parallel }_{2}^{2} = 0 \) , hence the result according to (**).

> Remarque 6. - On peut montrer que l'égalité de Parseval reste vraie pour toute fonction \( {f2\pi } \) -périodique, continue par morceaux et intégrable sur \( \rbrack 0,{2\pi }\lbrack \) .

Remark 6. - It can be shown that Parseval's identity remains true for any \( {f2\pi } \)-periodic function that is piecewise continuous and integrable on \( \rbrack 0,{2\pi }\lbrack \) .

> - Si \( f \) est une fonction \( {2\pi } \) -périodique et continue par morceaux, on a \( \mathop{\lim }\limits_{{\left| n\right|  \rightarrow   + \infty }}{c}_{n}\left( f\right)  = \) 0 (conséquence de la convergence de \( \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \) ). On retrouve ainsi le lemme de Lebesgue dans ce cas particulier (voir l'exercice 6 page 157).

- If \( f \) is a \( {2\pi } \)-periodic and piecewise continuous function, we have \( \mathop{\lim }\limits_{{\left| n\right|  \rightarrow   + \infty }}{c}_{n}\left( f\right)  = \) 0 (a consequence of the convergence of \( \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{\left| {c}_{n}\left( f\right) \right| }^{2} \)). We thus recover the Lebesgue lemma in this particular case (see exercise 6 on page 157).

> - L'égalité de Parseval entraîne qu'une fonction continue \( {2\pi } \) -périodique qui a tout ses coefficients de Fourier nuls est nulle.

- Parseval's identity implies that a continuous \( {2\pi } \)-periodic function whose Fourier coefficients are all zero is zero.

> - Soit \( f : \mathbb{R} \rightarrow  \mathbb{C} \) une fonction continue et \( {2\pi } \) -périodique. D’après l’égalité de Parseval et la proposition 3, on a \( \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2} = 0 \) où \( {s}_{n} = \mathop{\sum }\limits_{{-n}}^{n}{c}_{k}\left( f\right) {e}_{k} \) . On en déduit que si la série de Fourier de \( f \) converge uniformément sur \( \mathbb{R} \) , alors \( f \) est égale à sa série de Fourier (sa fonction limite \( g \) vérifie \( \parallel f - g{\parallel }_{2} = 0 \) et \( g \) est continue - limite uniforme de fonctions continues - donc \( f = g \) ).

- Let \( f : \mathbb{R} \rightarrow  \mathbb{C} \) be a continuous and \( {2\pi } \)-periodic function. According to Parseval's identity and proposition 3, we have \( \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\begin{Vmatrix}f - {s}_{n}\end{Vmatrix}}_{2} = 0 \) where \( {s}_{n} = \mathop{\sum }\limits_{{-n}}^{n}{c}_{k}\left( f\right) {e}_{k} \). We deduce that if the Fourier series of \( f \) converges uniformly on \( \mathbb{R} \), then \( f \) is equal to its Fourier series (its limit function \( g \) satisfies \( \parallel f - g{\parallel }_{2} = 0 \) and \( g \) is continuous - uniform limit of continuous functions - therefore \( f = g \)).
