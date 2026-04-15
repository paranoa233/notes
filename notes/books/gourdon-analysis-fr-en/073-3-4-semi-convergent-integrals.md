#### 3.4. Semi-convergent integrals

*Français : 3.4. Intégrales semi-convergentes*

On appelle ainsi les intégrales qui convergent mais ne convergent pas absolument. Le résultat qui suit permet souvent de montrer la convergence de telles intégrales.

> This term refers to integrals that converge but do not converge absolutely. The following result is often used to show the convergence of such integrals.

THÉORÉME 5 (RÉGLE D’ABEL). Soient \( f : \left\lbrack {a, b\lbrack \rightarrow \mathbb{R}}\right. \) de classe \( {\mathcal{C}}^{1} \) et \( g : \lbrack a, b\lbrack \rightarrow \mathbb{R} \) continue sur \( \lbrack a, b\lbrack \) vérifiant

> THEOREM 5 (ABEL'S RULE). Let \( f : \left\lbrack {a, b\lbrack \rightarrow \mathbb{R}}\right. \) be of class \( {\mathcal{C}}^{1} \) and \( g : \lbrack a, b\lbrack \rightarrow \mathbb{R} \) be continuous on \( \lbrack a, b\lbrack \) satisfying

(i) \( f \) est décroissante et \( \mathop{\lim }\limits_{{x \rightarrow b}}f\left( x\right) = 0 \) (en particulier, \( f \) est positive),

> (i) \( f \) is decreasing and \( \mathop{\lim }\limits_{{x \rightarrow b}}f\left( x\right) = 0 \) (in particular, \( f \) is positive),

(ii) il existe \( M > 0 \) tel que pour tout \( x \in \left\lbrack {a, b\lbrack ,\left| {{\int }_{a}^{x}g\left( t\right) {dt}}\right| \leq M}\right. \) .

> (ii) there exists \( M > 0 \) such that for all \( x \in \left\lbrack {a, b\lbrack ,\left| {{\int }_{a}^{x}g\left( t\right) {dt}}\right| \leq M}\right. \) .

Alors \( {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \) est convergente.

> Then \( {\int }_{a}^{b}f\left( t\right) g\left( t\right) {dt} \) is convergent.

Démonstration. Soit \( \varepsilon > 0 \) . L’hypothèse (i) assure l’existence de \( A > 0 \) tel que \( f\left( A\right) \leq \varepsilon \) . En utilisant la deuxième formule de la moyenne (voir page 128), on a

> Proof. Let \( \varepsilon > 0 \) . Hypothesis (i) ensures the existence of \( A > 0 \) such that \( f\left( A\right) \leq \varepsilon \) . Using the second mean value theorem (see page 128), we have

\[
\forall x, y \in  \mathbb{R}, a \leq  x < y < b,\exists c \in  \left\lbrack  {x, y}\right\rbrack  ,\;{\int }_{x}^{y}f\left( t\right) g\left( t\right) {dt} = f\left( x\right) {\int }_{x}^{c}g\left( t\right) {dt},
\]

ce qui entraîne,

> which implies,

\[
\forall x, y \in  \mathbb{R}, A \leq  x < y,\;\left| {{\int }_{x}^{y}f\left( t\right) g\left( t\right) {dt}}\right|  \leq  f\left( x\right)  \cdot  {2M} \leq  f\left( A\right)  \cdot  {2M} \leq  {2M\varepsilon },
\]

d'où le résultat en vertu du critère de Cauchy.

> from which the result follows by the Cauchy criterion.

Remarque 5. - Ce résultat est une version continue du théorème 7 page 215 sur les séries. Il repose essentiellement sur la deuxième formule de la moyenne (page 128). Cette dernière n'est pas au programme (la règle d'Abel pour les intégrales ne l'est pas non plus), mais nous avions vu que lorsque \( f \) est \( {\mathcal{C}}^{1} \) et \( g \) continue, sa preuve s’obtient facilement. La remarque 6 donne un exemple typique de preuve directe.

> Remark 5. - This result is a continuous version of theorem 7 on page 215 regarding series. It relies essentially on the second mean value theorem (page 128). The latter is not in the curriculum (neither is Abel's rule for integrals), but we have seen that when \( f \) is \( {\mathcal{C}}^{1} \) and \( g \) is continuous, its proof is easily obtained. Remark 6 provides a typical example of a direct proof.

- En utilisant la proposition 1 page 125, il est clair que ce théorème reste vrai si \( g \) est à valeurs dans un \( \mathbb{R} \) -e.v de dimension finie, en particulier sur \( \mathbb{C} \) .

> - Using proposition 1 on page 125, it is clear that this theorem remains true if \( g \) takes values in a finite-dimensional \( \mathbb{R} \) -vector space, in particular on \( \mathbb{C} \) .

Conséquence : On considère la fonction \( g : \left\lbrack {a, + \infty \left\lbrack { \rightarrow \mathbb{C}\;t \mapsto {e}^{i\lambda t}\left( \right. }\right. }\right. \) ou \( a,\lambda \in \mathbb{R}) \) . On a

> Consequence: Consider the function \( g : \left\lbrack {a, + \infty \left\lbrack { \rightarrow \mathbb{C}\;t \mapsto {e}^{i\lambda t}\left( \right. }\right. }\right. \) or \( a,\lambda \in \mathbb{R}) \) . We have

\[
\forall x > a,\;\left| {{\int }_{a}^{x}g\left( t\right) {dt}}\right|  = \left| \frac{{e}^{i\lambda x} - {e}^{i\lambda a}}{\lambda }\right|  \leq  \frac{2}{\left| \lambda \right| }.
\]

En appliquant la règle d’Abel, on en déduit que pour toute fonction \( f : \left\lbrack {a, + \infty \lbrack \rightarrow \mathbb{R}}\right. \) décroissante et tendant vers 0 à l'infini, l'intégrale

> By applying Abel's rule, we deduce that for any function \( f : \left\lbrack {a, + \infty \lbrack \rightarrow \mathbb{R}}\right. \) that is decreasing and tends to 0 at infinity, the integral

\[
{\int }_{a}^{+\infty }f\left( t\right) {e}^{i\lambda t}{dt}
\]

converge. En particulier, pour tout \( \alpha > 0 \) , l’intégrale \( {\int }_{1}^{+\infty }{e}^{it}/{t}^{\alpha }{dt} \) converge.

> converges. In particular, for any \( \alpha > 0 \) , the integral \( {\int }_{1}^{+\infty }{e}^{it}/{t}^{\alpha }{dt} \) converges.

Remarque 6. - On peut prouver facilement la convergence de l'intégrale

> Remark 6. - One can easily prove the convergence of the integral

\[
{\int }_{1}^{+\infty }\frac{{e}^{it}}{{t}^{\alpha }}{dt}
\]

(*)

> pour \( \alpha > 0 \) sans utiliser la règle d’Abel (qui rappelons le, n’est pas au programme). Il suffit d'intégrer par parties, en écrivant

for \( \alpha > 0 \) without using Abel's rule (which, let us recall, is not in the syllabus). It suffices to integrate by parts, by writing

\[
\forall X > 1,\;{\int }_{1}^{X}\frac{{e}^{it}}{{t}^{\alpha }}{dt} = {\left\lbrack  \frac{{e}^{it}}{i{t}^{\alpha }}\right\rbrack  }_{1}^{X} + \frac{\alpha }{i}{\int }_{1}^{X}\frac{{e}^{it}}{{t}^{\alpha  + 1}}{dt}.
\]

On remarque ensuite que le terme de gauche dans le membre de droite de cette dernière égalité converge lorsque \( X \rightarrow + \infty \) ; quant à son terme de droite, il converge également quand \( X \rightarrow + \infty \) car l’intégrale \( {\int }_{1}^{+\infty }{e}^{it}/{t}^{\alpha + 1}{dt} \) converge absolument. De tout ceci, on en déduit la convergence de l'intégrale (*). En particulier, les parties réelles et imaginaires de cette intégrale convergent, c’est-à-dire que pour tout \( \alpha > 0 \) , on a la convergence des intégrales

> We then note that the term on the left in the right-hand side of this last equality converges as \( X \rightarrow + \infty \) ; as for its term on the right, it also converges when \( X \rightarrow + \infty \) because the integral \( {\int }_{1}^{+\infty }{e}^{it}/{t}^{\alpha + 1}{dt} \) converges absolutely. From all this, we deduce the convergence of the integral (*). In particular, the real and imaginary parts of this integral converge, that is to say that for all \( \alpha > 0 \) , we have the convergence of the integrals

\[
{\int }_{1}^{+\infty }\frac{\sin t}{{t}^{\alpha }}{dt}\;\text{ et }\;{\int }_{1}^{+\infty }\frac{\cos t}{{t}^{\alpha }}{dt}.
\]

- Lorsque \( 0 < \alpha  \leq  1 \) , l’intégrale (*) est semi-convergente (elle est convergente mais non absolument convergente). Lorsque \( \alpha  \leq  0 \) , elle est divergente.

> - When \( 0 < \alpha  \leq  1 \) , the integral (*) is semi-convergent (it is convergent but not absolutely convergent). When \( \alpha  \leq  0 \) , it is divergent.

- Grâce au changement de variable \( u = {t}^{2} \) , on montre que l’intégrale \( {\int }_{1}^{+\infty }\sin \left( {t}^{2}\right) {dt} \) a la même nature que \( {\int }_{1}^{+\infty }\left( {\sin u}\right) /\sqrt{u}{du} \) , donc convergente d’après ce que l’on vient de voir. Ceci est un exemple d'intégrale convergente dont la fonction intégrée ne tend pas vers 0 à l'infini.

> - Thanks to the change of variable \( u = {t}^{2} \) , we show that the integral \( {\int }_{1}^{+\infty }\sin \left( {t}^{2}\right) {dt} \) has the same nature as \( {\int }_{1}^{+\infty }\left( {\sin u}\right) /\sqrt{u}{du} \) , therefore convergent according to what we have just seen. This is an example of a convergent integral whose integrand does not tend to 0 at infinity.

- Profitons en ici pour rappeler que si deux fonctions sont équivalentes en l'infini et si elles ne sont pas de signe constant, leurs intégrales ne sont pas forcément de même nature. Par exemple, les fonctions

> - Let us take this opportunity to recall that if two functions are equivalent at infinity and if they are not of constant sign, their integrals are not necessarily of the same nature. For example, the functions

\[
f : \left\lbrack  {1, + \infty \left\lbrack  { \rightarrow  \mathbb{C}\;t \mapsto  \frac{{e}^{it}}{\sqrt{t}}\;\text{ et }\;g : \left\lbrack  {1, + \infty \left\lbrack  { \rightarrow  \mathbb{C}\;t \mapsto  \frac{{e}^{it}}{\sqrt{t}} + \frac{1}{t}}\right. }\right. }\right. }\right.
\]

sont équivalentes en l'infini ; pourtant \( {\int }_{1}^{+\infty }f\left( x\right) {dx} \) converge (on vient de le voir) et \( {\int }_{1}^{+\infty }g\left( x\right) {dx} \) diverge (si elle convergeait, \( {\int }_{1}^{+\infty }\left( {g\left( t\right) - f\left( t\right) }\right) {dt} = {\int }_{1}^{+\infty }{dt}/t \) conver-gerait, ce qui est faux).

> are equivalent at infinity; yet \( {\int }_{1}^{+\infty }f\left( x\right) {dx} \) converges (we have just seen it) and \( {\int }_{1}^{+\infty }g\left( x\right) {dx} \) diverges (if it converged, \( {\int }_{1}^{+\infty }\left( {g\left( t\right) - f\left( t\right) }\right) {dt} = {\int }_{1}^{+\infty }{dt}/t \) would converge, which is false).
