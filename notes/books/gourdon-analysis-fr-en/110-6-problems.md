### 6. Problems

*Français : 6. Problèmes*

Problem 1. Donner un équivalent, lorsque \( n \rightarrow \infty \) , d’une suite réelle \( \left( {u}_{n}\right) \) vérifiant

> Problem 1. Give an equivalent, as \( n \rightarrow \infty \) , of a real sequence \( \left( {u}_{n}\right) \) satisfying

\[
{u}_{0} > 0,\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = {u}_{n} + \frac{1}{{u}_{n}^{\alpha }},\;\left( {\alpha  >  - 1}\right) .
\]

Solution. On remarque déjà que \( \left( {u}_{n}\right) \) diverge vers \( + \infty \) . En effet, \( \left( {u}_{n}\right) \) est croissante. Si elle était majorée, elle convergerait et sa limite \( \ell \) vérifierait \( \ell = \ell + a/{\ell }^{\alpha } \) , ce qui est absurde. La suite \( \left( {u}_{n}\right) \) est donc croissante et non majorée, donc diverge vers \( + \infty \) .

> Solution. We first note that \( \left( {u}_{n}\right) \) diverges to \( + \infty \) . Indeed, \( \left( {u}_{n}\right) \) is increasing. If it were bounded above, it would converge and its limit \( \ell \) would satisfy \( \ell = \ell + a/{\ell }^{\alpha } \) , which is absurd. The sequence \( \left( {u}_{n}\right) \) is therefore increasing and not bounded above, so it diverges to \( + \infty \) .

Pour rechercher un équivalent de \( \left( {u}_{n}\right) \) , on va appliquer une méthode classique (déjà utilisée dans l’exercice 7 page 207). On cherche s’il existe \( \beta > 0 \) tel que la suite \( \left( {{u}_{n + 1}^{\beta } - {u}_{n}^{\beta }}\right) \) converge. Comme \( \alpha + 1 > 0 \) et que \( \left( {u}_{n}\right) \) diverge vers \( + \infty \) , on peut écrire

> To find an equivalent of \( \left( {u}_{n}\right) \) , we will apply a classic method (already used in exercise 7 on page 207). We look for whether there exists \( \beta > 0 \) such that the sequence \( \left( {{u}_{n + 1}^{\beta } - {u}_{n}^{\beta }}\right) \) converges. Since \( \alpha + 1 > 0 \) and \( \left( {u}_{n}\right) \) diverges to \( + \infty \) , we can write

\[
{u}_{n + 1}^{\beta } = {\left\lbrack  {u}_{n}\left( 1 + \frac{1}{{u}_{n}^{\alpha  + 1}}\right) \right\rbrack  }^{\beta } = {u}_{n}^{\beta }\left( {1 + \frac{\beta }{{u}_{n}^{\alpha  + 1}} + o\left( \frac{1}{{u}_{n}^{\alpha  + 1}}\right) }\right) \;\text{ donc }\;{u}_{n + 1}^{\beta } - {u}_{n}^{\beta } \sim  \beta {u}_{n}^{\beta  - \left( {\alpha  + 1}\right) }.
\]

On choisit \( \beta = \alpha + 1 \) , de sorte que \( {u}_{n + 1}^{\alpha + 1} - {u}_{n}^{\alpha + 1} \sim \alpha + 1 \) . En sommant ces équivalents (on peut, voir le théorème 5 page 210), on obtient

> We choose \( \beta = \alpha + 1 \) , such that \( {u}_{n + 1}^{\alpha + 1} - {u}_{n}^{\alpha + 1} \sim \alpha + 1 \) . By summing these equivalents (we can, see theorem 5 on page 210), we obtain

\[
{u}_{n}^{\alpha  + 1} - {u}_{0}^{\alpha  + 1} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {{u}_{k + 1}^{\alpha  + 1} - {u}_{k}^{\alpha  + 1}}\right)  \sim  n\left( {\alpha  + 1}\right) ,
\]

donc finalement \( {u}_{n}^{\alpha + 1} \sim n\left( {\alpha + 1}\right) \) donc \( {u}_{n} \sim {\left\lbrack n\left( \alpha + 1\right) \right\rbrack }^{1/\left( {\alpha + 1}\right) } \) lorsque \( n \rightarrow + \infty \) .

> so finally \( {u}_{n}^{\alpha + 1} \sim n\left( {\alpha + 1}\right) \) so \( {u}_{n} \sim {\left\lbrack n\left( \alpha + 1\right) \right\rbrack }^{1/\left( {\alpha + 1}\right) } \) as \( n \rightarrow + \infty \) .

Problem 2 (NOMBRE MOYEN DE DIVISEURS D'UN ENTIER). Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( \tau \left( n\right) \) le nombre de diviseurs de \( n.\mathbf{1}/ \) Donner, lorsque \( x \rightarrow + \infty \) , un équivalent de

> Problem 2 (AVERAGE NUMBER OF DIVISORS OF AN INTEGER). For any \( n \in {\mathbb{N}}^{ * } \), let \( \tau \left( n\right) \) be the number of divisors of \( n.\mathbf{1}/ \). When \( x \rightarrow + \infty \), give an equivalent of

\[
F\left( x\right)  = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}\tau \left( n\right) .
\]

2/ On désigne par \( \gamma \) la constante d’Euler. Lorsque \( x \rightarrow + \infty \) , démontrer que

> 2/ Let \( \gamma \) denote the Euler-Mascheroni constant. When \( x \rightarrow + \infty \), prove that

\[
F\left( x\right)  = x\log x + \left( {{2\gamma } - 1}\right) x + O\left( \sqrt{x}\right)
\]

(on considérera les indices \( \leq \sqrt{x} \) dans l’expression de \( F\left( x\right) \) par une somme double).

> (consider the indices \( \leq \sqrt{x} \) in the expression of \( F\left( x\right) \) as a double sum).

Solution. 1/ En remarquant que \( \tau \left( n\right) = \mathop{\sum }\limits_{{m \mid n}}1 \) (on somme 1 sur les entiers \( m \) qui divisent \( n \) ), une inversion de sommation donne

> Solution. 1/ By noting that \( \tau \left( n\right) = \mathop{\sum }\limits_{{m \mid n}}1 \) (we sum 1 over the integers \( m \) that divide \( n \)), an inversion of summation gives

\[
F\left( x\right)  = \mathop{\sum }\limits_{{1 \leq  n \leq  x}}\mathop{\sum }\limits_{{m \mid  n}}1 = \mathop{\sum }\limits_{{1 \leq  m \leq  x}}\mathop{\sum }\limits_{\substack{{n \leq  x} \\  {m \mid  n} }}1.
\]

(*)

> Or \( \mathop{\sum }\limits_{{n \leq x, m \mid n}}1 \) est le nombre d’entiers naturels inférieurs à \( x \) divisibles par \( m \) . Ces éléments sont \( m,{2m},\ldots ,\left\lbrack {x/m}\right\rbrack m \) (où \( \left\lbrack y\right\rbrack \) désigne la partie entière de \( y \) ), donc au nombre de \( \left\lbrack {x/m}\right\rbrack \) . Donc finalement

Now \( \mathop{\sum }\limits_{{n \leq x, m \mid n}}1 \) is the number of natural integers less than \( x \) divisible by \( m \). These elements are \( m,{2m},\ldots ,\left\lbrack {x/m}\right\rbrack m \) (where \( \left\lbrack y\right\rbrack \) denotes the integer part of \( y \)), thus there are \( \left\lbrack {x/m}\right\rbrack \) of them. Therefore, finally

\[
F\left( x\right)  = \mathop{\sum }\limits_{{1 \leq  m \leq  x}}\left\lbrack  \frac{x}{m}\right\rbrack  .
\]

En utilisant l’encadrement \( x/m - 1 < \left\lbrack {x/m}\right\rbrack \leq x/m \) , en déduit

> Using the inequality \( x/m - 1 < \left\lbrack {x/m}\right\rbrack \leq x/m \), we deduce

\[
x\left( {\mathop{\sum }\limits_{{1 \leq  m \leq  x}}\frac{1}{m}}\right)  - x < F\left( x\right)  \leq  x\left( {\mathop{\sum }\limits_{{1 \leq  m \leq  x}}\frac{1}{m}}\right) ,
\]

et comme \( \mathop{\sum }\limits_{{1 \leq m \leq x}}1/m = \log x + O\left( 1\right) \) (c’est classique, voir la page 211), on en déduit \( F\left( x\right) = \; x\log x + O\left( x\right) \) , en particulier \( F\left( x\right) \sim x\log x \) .

> and since \( \mathop{\sum }\limits_{{1 \leq m \leq x}}1/m = \log x + O\left( 1\right) \) (this is standard, see page 211), we deduce \( F\left( x\right) = \; x\log x + O\left( x\right) \), in particular \( F\left( x\right) \sim x\log x \).

2 / Pousser l'asymptotique dans le raisonnement précédent ne permet pas d'obtenir le résultat. On effectue le changement de variable \( k = n/m \) dans la dernière somme de (*), qui donne

> 2/ Pushing the asymptotic in the previous reasoning does not allow obtaining the result. We perform the change of variable \( k = n/m \) in the last sum of (*), which gives

\[
F\left( x\right)  = \mathop{\sum }\limits_{{1 \leq  m \leq  x}}\mathop{\sum }\limits_{\substack{{1 \leq  k} \\  {1 \leq  {km} \leq  x} }}1 = \mathop{\sum }\limits_{{1 \leq  {km} \leq  x}}1.
\]

(**)

> Comme suggéré, découpons cette dernière somme en fonction de la position de \( k, m \) par rapport à \( \sqrt{x} \) . On peut écrire

As suggested, let us split this last sum based on the position of \( k, m \) relative to \( \sqrt{x} \). We can write

\[
F\left( x\right)  = \mathop{\sum }\limits_{\substack{{1 \leq  k \leq  \sqrt{x}} \\  {1 \leq  {km} \leq  x} }}1 + \mathop{\sum }\limits_{\substack{{1 \leq  m \leq  \sqrt{x}} \\  {1 \leq  {km} \leq  x} }}1 - \mathop{\sum }\limits_{\substack{{1 \leq  k, m \leq  \sqrt{x}} \\  {1 \leq  {km} \leq  x} }}1 = 2\mathop{\sum }\limits_{\substack{{1 \leq  m \leq  \sqrt{x}} \\  {1 \leq  {km} \leq  x} }}1 - {\left\lbrack  \sqrt{x}\right\rbrack  }^{2} = 2\mathop{\sum }\limits_{\substack{{1 \leq  m \leq  \sqrt{x}} }}\left\lbrack  \frac{x}{m}\right\rbrack   - {\left\lbrack  \sqrt{x}\right\rbrack  }^{2}.
\]

Ici aussi on utilise l’encadrement \( y - 1 < \left\lbrack y\right\rbrack \leq y \) , qui permet d’obtenir,à partir de la dernière expression

> Here too, we use the inequality \( y - 1 < \left\lbrack y\right\rbrack \leq y \), which allows us to obtain, from the last expression

\[
F\left( x\right)  = 2\mathop{\sum }\limits_{{1 \leq  m \leq  \sqrt{x}}}\frac{x}{m} + O\left( \sqrt{x}\right)  - {\left( \sqrt{x} + O\left( 1\right) \right) }^{2} = {2x}\mathop{\sum }\limits_{{1 \leq  m \leq  \sqrt{x}}}\frac{1}{m} - x + O\left( \sqrt{x}\right) .
\]

(***)

> L'asymptotique d'ordre 3 des nombres harmoniques (voir page 211) permet d'écrire

The 3rd-order asymptotic of harmonic numbers (see page 211) allows us to write

\[
\mathop{\sum }\limits_{{1 \leq  m \leq  \sqrt{x}}}\frac{1}{m} = \log \sqrt{x} + \gamma  + O\left( {1/\sqrt{x}}\right)  = \frac{1}{2}\log x + \gamma  + O\left( {1/\sqrt{x}}\right) .
\]

on en déduit le résultat en remplaçant ceci dans la dernière expression de (***).

> we deduce the result by replacing this in the last expression of (***).

Remarque. On peut interpréter ce résultat en disant qu’un entier \( n \) a en moyenne \( \log n + \; {2\gamma } - 1 \) diviseurs.

> Remark. One can interpret this result by saying that an integer \( n \) has on average \( \log n + \; {2\gamma } - 1 \) divisors.

La technique utilisée est classique dans ce type d'exercice : on fait apparaître une somme double puis on inverse les signes de sommation. On montre par exemple de la même façon que \( \mathop{\sum }\limits_{{n \leq x}}\sigma \left( n\right) \sim \left( {{\pi }^{2}/{12}}\right) {x}^{2} \) où \( \sigma \left( n\right) \) est la somme des diviseurs de \( n \) .

> The technique used is standard in this type of exercise: we introduce a double sum and then invert the summation signs. We show, for example, in the same way that \( \mathop{\sum }\limits_{{n \leq x}}\sigma \left( n\right) \sim \left( {{\pi }^{2}/{12}}\right) {x}^{2} \) where \( \sigma \left( n\right) \) is the sum of the divisors of \( n \).

L’approche consistant à découper la somme de (**) en considérant les cas où \( k, m \leq \; \sqrt{x} \) a été utilisée par Dirichlet et est appelée la méthode de l’hyperbole. Elle porte ce nom car géométriquement, elle consiste à regrouper les couples d'entiers naturels non nuls \( \left( {k, m}\right) \) situés sous l’hyperbole \( {km} \leq x \) en fonction de la position relative de \( k, m \) et \( \sqrt{x} \) . Le problème consistant à déterminer la plus petite constante \( \theta \) telle que \( F\left( x\right) = x\log x + \; \left( {{2\gamma } - 1}\right) x + O\left( {x}^{\theta + o\left( 1\right) }\right) \) est célèbre et s’appelle le problème des diviseurs de Dirichlet. Nous avons montré que \( \theta \leq 1/2 \) . En 1903, Voronoï a montré que \( \theta \leq 1/3 \) puis Hardy et Landau ont montré en 1915 que \( \theta \geq 1/4 \) . Il est conjecturé que \( \theta = 1/4 \) mais le meilleur résultat obtenu jusqu’à présent est dû à Huxley qui a prouvé en 2003 que \( \theta \leq {131}/{416} \simeq 0,{3149} \) .

> The approach of splitting the sum of (**) by considering the cases where \( k, m \leq \; \sqrt{x} \) was used by Dirichlet and is called the hyperbola method. It is so named because, geometrically, it consists of grouping pairs of non-zero natural numbers \( \left( {k, m}\right) \) located under the hyperbola \( {km} \leq x \) according to the relative position of \( k, m \) and \( \sqrt{x} \). The problem of determining the smallest constant \( \theta \) such that \( F\left( x\right) = x\log x + \; \left( {{2\gamma } - 1}\right) x + O\left( {x}^{\theta + o\left( 1\right) }\right) \) is famous and is called the Dirichlet divisor problem. We have shown that \( \theta \leq 1/2 \). In 1903, Voronoi showed that \( \theta \leq 1/3 \), then Hardy and Landau showed in 1915 that \( \theta \geq 1/4 \). It is conjectured that \( \theta = 1/4 \), but the best result obtained so far is due to Huxley, who proved in 2003 that \( \theta \leq {131}/{416} \simeq 0,{3149} \).

Problem 3 (Deux Techniques originales pour calculer \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \) ). 1 / Pour tout \( m \in {\mathbb{N}}^{ * } \) , on définit la fonction

> Problem 3 (Two original techniques for calculating \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \)). 1 / For all \( m \in {\mathbb{N}}^{ * } \), we define the function

\[
\left. {{f}_{m} : }\right\rbrack   - \pi ,\pi \lbrack  \smallsetminus  \{ 0\}  \rightarrow  \mathbb{R}\;\theta  \mapsto  \frac{\sin \left( {{2m} + 1}\right) \theta }{{\sin }^{{2m} + 1}\theta }.
\]

a) Écrire \( {f}_{m} \) sous la forme d’un polynôme \( {P}_{m} \) en cotan \( {}^{2}\theta \) .

> a) Write \( {f}_{m} \) in the form of a polynomial \( {P}_{m} \) in cotan \( {}^{2}\theta \).

b) En déduire les racines de \( {P}_{m} \) et calculer leur somme. Conclure.

> b) Deduce the roots of \( {P}_{m} \) and calculate their sum. Conclude.

2 / a) Montrer que la série de fonctions

> 2 / a) Show that the series of functions

\[
\sin t + \mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\frac{1}{{2n} + 1}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{\sin }^{{2n} + 1}t
\]

converge normalement vers \( t \mapsto t\operatorname{sur}\left\lbrack {-\pi /2,\pi /2}\right\rbrack \) .

> converges normally to \( t \mapsto t\operatorname{sur}\left\lbrack {-\pi /2,\pi /2}\right\rbrack \).

b) En déduire par intégration la valeur de \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}1/{\left( 2n + 1\right) }^{2} \) , puis celle de \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \) .

> b) Deduce by integration the value of \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}1/{\left( 2n + 1\right) }^{2} \), then that of \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \).

Solution. 1/ a) En écrivant que \( \sin \left( {{2m} + 1}\right) \theta \) est la partie imaginaire de \( {\left( \cos \theta + i\sin \theta \right) }^{{2m} + 1} \) , on trouve

> Solution. 1/ a) By writing that \( \sin \left( {{2m} + 1}\right) \theta \) is the imaginary part of \( {\left( \cos \theta + i\sin \theta \right) }^{{2m} + 1} \), we find

\[
\forall \theta  \in  \mathbb{R},\;\sin \left( {{2m} + 1}\right) \theta  = \mathop{\sum }\limits_{{k = 0}}^{m}{C}_{{2m} + 1}^{{2k} + 1}{\left( -1\right) }^{k}{\sin }^{{2k} + 1}\theta {\cos }^{2\left( {m - k}\right) }\theta ,
\]

donc \( {f}_{m}\left( \theta \right) = {P}_{m}\left( {{\operatorname{cotan}}^{2}\theta }\right) \) avec \( {P}_{m}\left( X\right) = \mathop{\sum }\limits_{{k = 0}}^{m}{C}_{{2m} + 1}^{{2k} + 1}{\left( -1\right) }^{k}{X}^{m - k} \) .

> therefore \( {f}_{m}\left( \theta \right) = {P}_{m}\left( {{\operatorname{cotan}}^{2}\theta }\right) \) with \( {P}_{m}\left( X\right) = \mathop{\sum }\limits_{{k = 0}}^{m}{C}_{{2m} + 1}^{{2k} + 1}{\left( -1\right) }^{k}{X}^{m - k} \).

b) L’expression \( {f}_{m}\left( \theta \right) = \sin \left( {\left( {{2m} + 1}\right) \theta }\right) /{\sin }^{{2m} + 1}\theta \) montre que

> b) The expression \( {f}_{m}\left( \theta \right) = \sin \left( {\left( {{2m} + 1}\right) \theta }\right) /{\sin }^{{2m} + 1}\theta \) shows that

\[
\forall k \in  \mathbb{N},1 \leq  k \leq  m,\;{f}_{m}\left( \frac{k\pi }{{2m} + 1}\right)  = 0\;\text{ donc }\;{P}_{m}\left( {{\operatorname{cotan}}^{2}\left( \frac{k\pi }{{2m} + 1}\right) }\right)  = 0.
\]

On a ainsi trouvé \( m \) racines distinctes du polynôme \( {P}_{m} \) , et comme \( \deg \left( {P}_{m}\right) = m \) , on a trouvé toutes les racines de \( {P}_{m} \) . La somme des racines de \( {P}_{m} \) est l’opposé du rapport du coefficient de \( {X}^{m - 1} \) par celui de \( {X}^{m} \) , donc

> We have thus found \( m \) distinct roots of the polynomial \( {P}_{m} \), and since \( \deg \left( {P}_{m}\right) = m \), we have found all the roots of \( {P}_{m} \). The sum of the roots of \( {P}_{m} \) is the opposite of the ratio of the coefficient of \( {X}^{m - 1} \) to that of \( {X}^{m} \), therefore

\[
\mathop{\sum }\limits_{{k = 1}}^{m}{\operatorname{cotan}}^{2}\left( \frac{k\pi }{{2m} + 1}\right)  = \frac{{C}_{{2m} + 1}^{3}}{{C}_{{2m} + 1}^{1}} = \frac{{2m}\left( {{2m} - 1}\right) }{6}.
\]

(*)

> Pour en déduire la valeur de \( \sum 1/{n}^{2} \) , nous allons comparer \( {\operatorname{cotan}}^{2}x \) et \( 1/{x}^{2} \) . Montrons

To deduce the value of \( \sum 1/{n}^{2} \), we will compare \( {\operatorname{cotan}}^{2}x \) and \( 1/{x}^{2} \). Let us show

\[
\forall x \in  \rbrack 0,\frac{\pi }{2}\left\lbrack  {,\;{\operatorname{cotan}}^{2}x \leq  \frac{1}{{x}^{2}} \leq  1 + {\operatorname{cotan}}^{2}x.}\right.
\]

\( \left( {* * }\right) \)

> L’inégalité des accroissements finis donne tan \( x \geq x \) sur \( \rbrack 0,\pi /2\lbrack \) , d’où la première inégalité de (**). Pour la seconde, on utilise la majoration \( \sin x \leq x \) sur ] \( 0,\pi /2\left\lbrack \right. \) (qui s’obtient aussi avec l’inégalité des accroissements finis) qui entraîne \( 1 + \operatorname{cotan}{}^{2}x = 1/{\sin }^{2}x \geq 1/{x}^{2} \) .

The mean value inequality gives tan \( x \geq x \) on \( \rbrack 0,\pi /2\lbrack \), hence the first inequality of (**). For the second, we use the bound \( \sin x \leq x \) on ] \( 0,\pi /2\left\lbrack \right. \) (which is also obtained with the mean value inequality) which leads to \( 1 + \operatorname{cotan}{}^{2}x = 1/{\sin }^{2}x \geq 1/{x}^{2} \).

> De (*) et (**), on tire

From (*) and (**), we derive

\[
\frac{{2m}\left( {{2m} - 1}\right) }{6} \leq  \mathop{\sum }\limits_{{k = 1}}^{m}\frac{{\left( 2m + 1\right) }^{2}}{{k}^{2}{\pi }^{2}} \leq  \frac{{2m}\left( {{2m} - 1}\right) }{6} + m
\]

donc

> therefore

\[
\frac{{2m}\left( {{2m} - 1}\right) }{{\left( 2m + 1\right) }^{2}}\frac{{\pi }^{2}}{6} \leq  \mathop{\sum }\limits_{{k = 1}}^{m}\frac{1}{{k}^{2}} \leq  \frac{{2m}\left( {{2m} - 1}\right) }{{\left( 2m + 1\right) }^{2}}\frac{{\pi }^{2}}{6} + \frac{m}{{\left( 2m + 1\right) }^{2}}{\pi }^{2}.
\]

Ceci est vrai pour tout \( m \in {\mathbb{N}}^{ * } \) . En faisant \( m \rightarrow + \infty \) , on en déduit \( \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}1/{k}^{2} = {\pi }^{2}/6 \) .

> This is true for all \( m \in {\mathbb{N}}^{ * } \). By letting \( m \rightarrow + \infty \), we deduce \( \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}1/{k}^{2} = {\pi }^{2}/6 \).

2 / a) On sait que la fonction arcsinus est développable en série entière sur ] -1,1 [, plus précisément

> 2 / a) We know that the arcsine function can be expanded as a power series on ] -1,1 [, more precisely

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;\arcsin x = x + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{u}_{n}{x}^{{2n} + 1}\;\text{ avec }\;{u}_{n} = \frac{1}{{2n} + 1}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }.}\right.
\]

(***)

> L’idée est ensuite de remplacer \( x \) par \( \sin t \) dans cette expression.

The idea is then to replace \( x \) with \( \sin t \) in this expression.

> On pourrait montrer la convergence normale de \( \sum {u}_{n}{x}^{{2n} + 1} \) sur \( \left\lbrack {-1,1}\right\rbrack \) en utilisant la règle de Raab-Duhamel pour estimer \( {u}_{n} \) , mais ici, on peut mieux faire. La positivité des \( {u}_{n} \) entraîne pour tout \( N \in {\mathbb{N}}^{ * } \) , d’après (***)

One could show the normal convergence of \( \sum {u}_{n}{x}^{{2n} + 1} \) on \( \left\lbrack {-1,1}\right\rbrack \) by using Raabe-Duhamel's rule to estimate \( {u}_{n} \), but here, we can do better. The positivity of \( {u}_{n} \) implies for all \( N \in {\mathbb{N}}^{ * } \), according to (***)

\[
\forall x \in  \rbrack  - 1,1\lbrack ,\;x + \mathop{\sum }\limits_{{n = 1}}^{N}{u}_{n}{x}^{{2n} + 1} \leq  \arcsin x \leq  \arcsin 1 = \frac{\pi }{2},
\]

et en faisant tendre \( x \) vers 1 on en déduit \( 1 + \mathop{\sum }\limits_{{n = 1}}^{N}{u}_{n} \leq \pi /2 \) . Ceci est vrai pour tout \( N \in {\mathbb{N}}^{ * } \) , donc \( \sum {u}_{n} \) est majorée, et comme les termes de cette série sont positifs, \( \sum {u}_{n} = \sum \left| {u}_{n}\right| \) converge. Ainsi, \( \sum {u}_{n}{x}^{{2n} + 1} \) converge normalement sur \( \left\lbrack {-1,1}\right\rbrack \) . Sa somme définit donc une fonction continue sur \( \left\lbrack {-1,1}\right\rbrack \) . L’égalité (***) vaut sur ] \( - 1,1\left\lbrack \text{ , elle vaut donc sur }\right\rbrack \left\lbrack {-1,1}\right\rbrack \) par continuité.

> and by letting \( x \) tend to 1 we deduce \( 1 + \mathop{\sum }\limits_{{n = 1}}^{N}{u}_{n} \leq \pi /2 \). This is true for all \( N \in {\mathbb{N}}^{ * } \), so \( \sum {u}_{n} \) is bounded, and since the terms of this series are positive, \( \sum {u}_{n} = \sum \left| {u}_{n}\right| \) converges. Thus, \( \sum {u}_{n}{x}^{{2n} + 1} \) converges normally on \( \left\lbrack {-1,1}\right\rbrack \). Its sum therefore defines a continuous function on \( \left\lbrack {-1,1}\right\rbrack \). The equality (***) holds on ] \( - 1,1\left\lbrack \text{ , elle vaut donc sur }\right\rbrack \left\lbrack {-1,1}\right\rbrack \) by continuity.

Finalement, nous avons montré que \( x + \sum {u}_{n}{x}^{{2n} + 1} \) converge normalement vers la fonction arcsinus sur \( \left\lbrack {-1,1}\right\rbrack \) . On en déduit le résultat demandé en remplaçant \( x \) par \( \sin t\left( {t \in \left\lbrack {-\pi /2,\pi /2}\right\rbrack }\right) \) . b) La convergence normale de la série de fonctions nous autorise à l'intégrer terme à terme, ce qui donne

> Finally, we have shown that \( x + \sum {u}_{n}{x}^{{2n} + 1} \) converges normally to the arcsine function on \( \left\lbrack {-1,1}\right\rbrack \). We deduce the requested result by replacing \( x \) with \( \sin t\left( {t \in \left\lbrack {-\pi /2,\pi /2}\right\rbrack }\right) \). b) The normal convergence of the series of functions allows us to integrate it term by term, which gives

\[
\frac{{\pi }^{2}}{8} = {\int }_{0}^{\pi /2}t\;{dt} = 1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{u}_{n}{\int }_{0}^{\pi /2}{\sin }^{{2n} + 1}{tdt} = 1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{u}_{n}\frac{2 \cdot  4\cdots \left( {2n}\right) }{3 \cdot  5\cdots \left( {{2n} + 1}\right) } = 1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{\left( 2n + 1\right) }^{2}}
\]

où nous avons utilisé la valeur de l’intégrale de Wallis \( {\int }_{0}^{\pi /2}{\sin }^{{2n} + 1}{tdt} \) (voir l’exercice 1 page 130). Pour en déduire \( S = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \) , il suffit de séparer les termes d’indices pairs et impairs

> where we used the value of the Wallis integral \( {\int }_{0}^{\pi /2}{\sin }^{{2n} + 1}{tdt} \) (see exercise 1 on page 130). To deduce \( S = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{2} \) from this, it suffices to separate the terms with even and odd indices

\[
S = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{{\left( 2n + 1\right) }^{2}} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{\left( 2n\right) }^{2}} = \frac{{\pi }^{2}}{8} + \frac{S}{4}\text{ d’où }S = \frac{{\pi }^{2}}{6}.
\]

Problems 4 (FORMULE SOMMATOIRE DE POISSON). a) Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction de classe \( {\mathcal{C}}^{1} \) vérifiant \( f\left( x\right) = O\left( {1/{x}^{2}}\right) \) et \( {f}^{\prime }\left( x\right) = O\left( {1/{x}^{2}}\right) \) lorsque \( \left| x\right| \rightarrow + \infty \) . Après avoir justifié l'existence des sommes infinies, montrer que

> Problem 4 (POISSON SUMMATION FORMULA). a) Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a function of class \( {\mathcal{C}}^{1} \) satisfying \( f\left( x\right) = O\left( {1/{x}^{2}}\right) \) and \( {f}^{\prime }\left( x\right) = O\left( {1/{x}^{2}}\right) \) as \( \left| x\right| \rightarrow + \infty \) . After justifying the existence of the infinite sums, show that

\[
\forall x \in  \mathbb{R},\;\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}f\left( {x + n}\right)  = \mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{f}^{ * }\left( n\right) {e}^{2i\pi nx}\text{ où }\;\forall n \in  \mathbb{Z},\;{f}^{ * }\left( n\right)  = {\int }_{-\infty }^{+\infty }f\left( t\right) {e}^{-{2i\pi nt}}{dt}.
\]

(formule sommatoire de Poisson).

> (Poisson summation formula).

b) (Application.) Montrer que

> b) (Application.) Show that

\[
\forall s > 0,\;\mathop{\sum }\limits_{{n =  - \infty }}^{{+\infty }}{e}^{-\pi {n}^{2}s} = {s}^{-1/2}\mathop{\sum }\limits_{{k =  - \infty }}^{{+\infty }}{e}^{-\pi {k}^{2}/s}
\]

(on pourra utiliser le résultat établi à la question 3/ de l'exercice 4 page 168).

> (one may use the result established in question 3/ of exercise 4 on page 168).

Solution. a) La série de fonctions \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}f\left( {x + n}\right) \) converge normalement (donc uniformément) sur tout segment de \( \mathbb{R} \) . En effet, si \( M > 0 \) est tel que \( \left| {f\left( x\right) }\right| \leq M/{x}^{2} \) pour \( \left| x\right| \geq 1 \) , il suffit d’écrire pour tout \( K > 0 \) la majoration

> Solution. a) The series of functions \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}f\left( {x + n}\right) \) converges normally (and thus uniformly) on any segment of \( \mathbb{R} \) . Indeed, if \( M > 0 \) is such that \( \left| {f\left( x\right) }\right| \leq M/{x}^{2} \) for \( \left| x\right| \geq 1 \) , it suffices to write the bound for any \( K > 0 \)

\[
\forall x \in  \left\lbrack  {-K, K}\right\rbrack  ,\forall n \in  \mathbb{Z},\left| n\right|  > K + 1,\;\left| {f\left( {x + n}\right) }\right|  \leq  \frac{M}{{\left( x + n\right) }^{2}} \leq  \frac{M}{{\left( \left| n\right|  - K\right) }^{2}}.
\]

En particulier, \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}f\left( {x + n}\right) \) converge simplement sur \( \mathbb{R} \) . On note \( F \) sa limite simple.

> In particular, \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}f\left( {x + n}\right) \) converges pointwise on \( \mathbb{R} \) . We denote its pointwise limit by \( F \) .

Pour les mêmes raisons, la série de fonctions \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{f}^{\prime }\left( {x + n}\right) \) converge uniformément sur tout segment de \( \mathbb{R} \) . On peut donc appliquer le théorème de dérivation sur les suites de fonctions qui entraîne que \( F \) est de classe \( {\mathcal{C}}^{1} \) sur tout segment de \( \mathbb{R} \) , donc sur \( \mathbb{R} \) .

> For the same reasons, the series of functions \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{f}^{\prime }\left( {x + n}\right) \) converges uniformly on any segment of \( \mathbb{R} \) . We can therefore apply the theorem on the differentiation of sequences of functions, which implies that \( F \) is of class \( {\mathcal{C}}^{1} \) on any segment of \( \mathbb{R} \) , and thus on \( \mathbb{R} \) .

Par ailleurs, \( F \) est 1-périodique car si on fixe \( x \in \mathbb{R} \) ,

> Furthermore, \( F \) is 1-periodic because if we fix \( x \in \mathbb{R} \) ,

\[
\forall N \in  \mathbb{N},\;\mathop{\sum }\limits_{{n =  - N}}^{N}f\left( {x + 1 + n}\right)  = \mathop{\sum }\limits_{{n =  - N + 1}}^{{N + 1}}f\left( {x + n}\right) ,
\]

et en faisant \( N \rightarrow + \infty \) , on en déduit \( F\left( {x + 1}\right) = F\left( x\right) \) .

> and by letting \( N \rightarrow + \infty \) , we deduce \( F\left( {x + 1}\right) = F\left( x\right) \) .

Les coefficients de Fourier de \( F \) sont donnés par

> The Fourier coefficients of \( F \) are given by

\[
\forall n \in  \mathbb{Z},\;{c}_{n}\left( F\right)  = {\int }_{0}^{1}F\left( t\right) {e}^{-{2i\pi nt}}{dt} = \mathop{\sum }\limits_{{n =  - \infty }}^{{+\infty }}{\int }_{0}^{1}f\left( {t + n}\right) {e}^{-{2i\pi nt}}{dt}
\]

\[
= \mathop{\sum }\limits_{{n =  - \infty }}^{{+\infty }}{\int }_{n}^{n + 1}f\left( t\right) {e}^{-{2i\pi nt}}{dt} = {\int }_{-\infty }^{+\infty }f\left( t\right) {e}^{-{2i\pi nt}}{dt} = {f}^{ * }\left( n\right)
\]

(on a bien le droit d'intervertir les signes de sommation car la série de fonctions définissant \( F \) converge uniformément sur \( \left\lbrack {0,1}\right\rbrack \) comme on l’a vu ; par ailleurs, la dernière intégrale converge absolument au vu des conditions de croissance satisfaites par \( f \) ). Comme de plus \( F \) est de classe \( {\mathcal{C}}^{1} \) , sa série de Fourier converge uniformément vers \( F \) , d’où la formule sommatoire de Poisson.

> (we are justified in interchanging the summation signs because the series of functions defining \( F \) converges uniformly on \( \left\lbrack {0,1}\right\rbrack \) as seen previously; furthermore, the last integral converges absolutely given the growth conditions satisfied by \( f \) ). Since \( F \) is also of class \( {\mathcal{C}}^{1} \) , its Fourier series converges uniformly to \( F \) , hence the Poisson summation formula.

b) Soit \( \alpha > 0 \) . Nous appliquons la formule sommatoire de Poisson à la fonction \( f : x \mapsto {e}^{-\alpha {x}^{2}} \) . Les coefficients \( {f}^{ * }\left( n\right) \) sont donnés par

> b) Let \( \alpha > 0 \) . We apply the Poisson summation formula to the function \( f : x \mapsto {e}^{-\alpha {x}^{2}} \) . The coefficients \( {f}^{ * }\left( n\right) \) are given by

\[
\forall n \in  \mathbb{Z},\;{f}^{ * }\left( n\right)  = {\int }_{-\infty }^{+\infty }{e}^{-\alpha {t}^{2}}{e}^{-{2i\pi nt}}{dt} = \frac{1}{\sqrt{\alpha }}{\int }_{-\infty }^{+\infty }{e}^{-{u}^{2}}{e}^{-{2i\pi nu}/\sqrt{\alpha }}{du} = \sqrt{\frac{\pi }{\alpha }}{e}^{-{\pi }^{2}{n}^{2}/\alpha }
\]

(où on a utilisé le résultat de la question 3/ de l'exercice 4 de la page 168). En appliquant la formule sommatoire de Poisson avec \( x = 0 \) , on déduit

> (where we used the result from question 3/ of exercise 4 on page 168). By applying the Poisson summation formula with \( x = 0 \) , we deduce

\[
\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{e}^{-\alpha {n}^{2}} = \sqrt{\frac{\pi }{\alpha }}\mathop{\sum }\limits_{{n \in  \mathbb{Z}}}{e}^{-{\pi }^{2}{n}^{2}/\alpha }
\]

Ceci est vrai pour tout \( \alpha > 0 \) , et en changeant \( \alpha \) en \( {\pi s} \) , on obtient le résultat désiré.

> This is true for all \( \alpha > 0 \), and by changing \( \alpha \) to \( {\pi s} \), we obtain the desired result.

Remarque. La dernière identité est non-triviale. En considérant la série entière \( \Theta \left( x\right) = \; \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{x}^{{n}^{2}} \) ,(fonction thêta de Jacobi) elle s’exprime en écrivant \( \sqrt{s}\Theta \left( {e}^{-{s\pi }}\right) = \Theta \left( {e}^{-\pi /s}\right) \) . Ainsi, le comportement de \( \Theta \left( x\right) \) en \( x = 1 \) est relié à son comportement en \( x = 0 \) .

> Remark. The last identity is non-trivial. By considering the power series \( \Theta \left( x\right) = \; \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{x}^{{n}^{2}} \) (Jacobi theta function), it is expressed by writing \( \sqrt{s}\Theta \left( {e}^{-{s\pi }}\right) = \Theta \left( {e}^{-\pi /s}\right) \). Thus, the behavior of \( \Theta \left( x\right) \) at \( x = 1 \) is related to its behavior at \( x = 0 \).

PROBLEME 5. Soit \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) une suite complexe vérifiant une récurrence linéaire d’ordre \( h \in {\mathbb{N}}^{ * } \) , c’est-à-dire

> PROBLEM 5. Let \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) be a complex sequence satisfying a linear recurrence of order \( h \in {\mathbb{N}}^{ * } \), that is to say

\[
\exists {a}_{1},\ldots ,{a}_{h} \in  \mathbb{C},\forall n \geq  h,\;{u}_{n} = {a}_{1}{u}_{n - 1} + \cdots  + {a}_{h}{u}_{n - h}.
\]

(*)

> En considérant la série entière \( \sum {u}_{n}{z}^{n} \) , démontrer la proposition 3 page 202.

By considering the power series \( \sum {u}_{n}{z}^{n} \), prove proposition 3 on page 202.

> Solution. Si la série entière \( \sum {u}_{n}{z}^{n} \) a un rayon de convergence non nul (on ne sait pas encore si c’est le cas), la récurrence (*) entraîne, après produit par \( {z}^{n} \) et sommation sur \( n \) (lorsque \( z \) est dans le disque de convergence) que sa somme \( f \) vérifie

Solution. If the power series \( \sum {u}_{n}{z}^{n} \) has a non-zero radius of convergence (we do not yet know if this is the case), the recurrence (*) implies, after multiplying by \( {z}^{n} \) and summing over \( n \) (when \( z \) is in the disk of convergence), that its sum \( f \) satisfies

\[
f\left( z\right)  - {P}_{h}\left( z\right)  = {a}_{1}z\left\lbrack  {f\left( z\right)  - {P}_{h - 1}\left( z\right) }\right\rbrack   + \cdots  + {a}_{h - 1}{z}^{h - 1}\left\lbrack  {f\left( z\right)  - {P}_{1}\left( z\right) }\right\rbrack   + {a}_{h}{z}^{h}f\left( z\right)
\]

\( \left( {* * }\right) \)

> où pour tout \( k,1 \leq k \leq h,{P}_{k}\left( z\right) = {u}_{0} + {u}_{1}z + \cdots + {u}_{k - 1}{z}^{k - 1} \) . Ceci s’écrit aussi \( f\left( z\right) Q\left( z\right) = P\left( z\right) \) où

where for all \( k,1 \leq k \leq h,{P}_{k}\left( z\right) = {u}_{0} + {u}_{1}z + \cdots + {u}_{k - 1}{z}^{k - 1} \). This is also written as \( f\left( z\right) Q\left( z\right) = P\left( z\right) \) where

\[
Q\left( z\right)  = 1 - {a}_{1}z - \cdots  - {a}_{h}{z}^{h}\;\text{ et }\;P\left( z\right)  = {P}_{h}\left( z\right)  - {a}_{1}z{P}_{h - 1}\left( z\right)  - \cdots  - {a}_{h - 1}{z}^{h - 1}{P}_{1}\left( z\right) .
\]

Ainsi, \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) est une fraction rationnelle. Par ailleurs,0 n’est pas un pôle de \( f\left( z\right) \) donc \( P\left( z\right) /Q\left( z\right) \) est développable en une série entière \( \sum {v}_{n}{z}^{n} \) dont le rayon de convergence est non nul (voir page 251). Sa somme \( g \) vérifie \( Q\left( z\right) g\left( z\right) = P\left( z\right) \) sur son disque de convergence, autrement dit \( g \) vérifie la même égalité que \( f \) dans (**), donc la suite \( \left( {v}_{n}\right) \) vérifie la récurrence (*). Par ailleurs, l’égalité (**) vérifiée par \( g \) montre que pour tout \( k,0 \leq k < h \) , le coefficient de \( {z}^{k} \) dans \( g\left( z\right) - {P}_{h}\left( z\right) \) est nul. Autrement dit, \( {v}_{k} = {u}_{k} \) lorsque \( 0 \leq k < h \) . Finalement, la suite \( \left( {v}_{n}\right) \) vérifie la même récurrence que \( \left( {u}_{n}\right) \) avec les mêmes conditions initiales. Ces suites sont donc égales, ce qui montre finalement que \( \sum {u}_{n}{z}^{n} \) a bien un rayon de convergence non nul et que sa somme \( f \) vérifie \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) sur son disque de convergence.

> Thus, \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) is a rational fraction. Furthermore, 0 is not a pole of \( f\left( z\right) \), so \( P\left( z\right) /Q\left( z\right) \) can be expanded into a power series \( \sum {v}_{n}{z}^{n} \) whose radius of convergence is non-zero (see page 251). Its sum \( g \) satisfies \( Q\left( z\right) g\left( z\right) = P\left( z\right) \) on its disk of convergence; in other words, \( g \) satisfies the same equality as \( f \) in (**), so the sequence \( \left( {v}_{n}\right) \) satisfies the recurrence (*). Furthermore, the equality (**) satisfied by \( g \) shows that for all \( k,0 \leq k < h \), the coefficient of \( {z}^{k} \) in \( g\left( z\right) - {P}_{h}\left( z\right) \) is zero. In other words, \( {v}_{k} = {u}_{k} \) when \( 0 \leq k < h \). Finally, the sequence \( \left( {v}_{n}\right) \) satisfies the same recurrence as \( \left( {u}_{n}\right) \) with the same initial conditions. These sequences are therefore equal, which finally shows that \( \sum {u}_{n}{z}^{n} \) indeed has a non-zero radius of convergence and that its sum \( f \) satisfies \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) on its disk of convergence.

On veut maintenant calculer explicitement \( {u}_{n} \) . Soient \( {x}_{1},\ldots ,{x}_{p} \) les racines de l’équation caractéristique de (*), d’ordre de multiplicité \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) , de sorte que

> We now wish to explicitly calculate \( {u}_{n} \) . Let \( {x}_{1},\ldots ,{x}_{p} \) be the roots of the characteristic equation of (*), with multiplicity \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) , such that

\[
R\left( X\right)  = {X}^{h} - {a}_{1}{X}^{h - 1} - \cdots  - {a}_{h} = \mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {x}_{i}\right) }^{{\alpha }_{i}}\;\text{ donc }\;Q\left( X\right)  = {X}^{h}R\left( \frac{1}{X}\right)  = \mathop{\prod }\limits_{{i = 1}}^{p}{\left( 1 - {x}_{i}X\right) }^{{\alpha }_{i}}.
\]

Le polynôme \( P \) vérifie \( \deg \left( P\right) < h = \deg \left( Q\right) \) par construction, on peut donc écrire la décomposition en éléments simples de \( P/Q \) sous la forme

> The polynomial \( P \) satisfies \( \deg \left( P\right) < h = \deg \left( Q\right) \) by construction, so we can write the partial fraction decomposition of \( P/Q \) in the form

\[
\frac{P\left( X\right) }{Q\left( X\right) } = \mathop{\sum }\limits_{{i = 1}}^{p}\left\lbrack  {\mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{c}_{i, j}}{{\left( X - 1/{x}_{i}\right) }^{j}}}\right\rbrack  \;\left( {{c}_{i, j} \in  \mathbb{C}}\right) .
\]

On en déduit (voir page 251) que le développement en série entière de \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) s’écrit

> We deduce from this (see page 251) that the power series expansion of \( f\left( z\right) = P\left( z\right) /Q\left( z\right) \) is written as

\[
f\left( z\right)  = \mathop{\sum }\limits_{{i = 1}}^{p}\left\lbrack  {\mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{\left( -1\right) }^{j}{c}_{i, j}{x}_{i}^{j}}{\left( {j - 1}\right) !}\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{\left( {n + j - 1}\right) !}{n!}{x}_{i}^{n}{z}^{n}}\right) }\right\rbrack  .
\]

On tire, en prenant le coefficient de \( {z}^{n} \) dans cette expression,

> By taking the coefficient of \( {z}^{n} \) in this expression, we obtain

\[
{u}_{n} = \mathop{\sum }\limits_{{i = 1}}^{p}\left\lbrack  {\mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{\left( -1\right) }^{j}{c}_{i, j}{x}_{i}^{j}}{\left( {j - 1}\right) !}\left( {n + j - 1}\right) \cdots \left( {n + 1}\right) }\right\rbrack  {x}_{i}^{n},
\]

donc \( {u}_{n} = \mathop{\sum }\limits_{{i = 1}}^{p}{T}_{i}\left( n\right) {x}_{i}^{n} \) où pour tout \( i,{T}_{i} \) est un polynôme de degré \( < {\alpha }_{i} \) .

> therefore \( {u}_{n} = \mathop{\sum }\limits_{{i = 1}}^{p}{T}_{i}\left( n\right) {x}_{i}^{n} \) where for all \( i,{T}_{i} \) is a polynomial of degree \( < {\alpha }_{i} \) .

En désignant par \( \Gamma \) l’e.v des suites vérifiant cette dernière condition, nous avons prouvé que l’e.v \( U \) des suites complexes vérifiant la récurrence linéaire (*) est tel que \( U \subset \Gamma \) . Nous voulons prouver la condition suffisante, c’est-à-dire \( \Gamma \subset U \) . Pour cela, on remarque que l’application

> By denoting by \( \Gamma \) the vector space of sequences satisfying this last condition, we have proven that the vector space \( U \) of complex sequences satisfying the linear recurrence (*) is such that \( U \subset \Gamma \) . We want to prove the sufficient condition, that is to say \( \Gamma \subset U \) . To do this, we note that the mapping

\[
U \rightarrow  {\mathbb{C}}^{h}\;{\left( {u}_{n}\right) }_{n \in  \mathbb{N}} \mapsto  \left( {{u}_{0},{u}_{1},\ldots ,{u}_{h - 1}}\right)
\]

est linéaire (c'est évident) et bijective (une suite vérifiant (*) est uniquement déterminée par ses premiers termes \( {u}_{0},\ldots ,{u}_{h - 1} \) ). Ainsi, \( U \) est de dimension \( h \) , et comme \( \Gamma \) est de dimension \( {\alpha }_{1} + \cdots + {\alpha }_{p} = h \) , l’inclusion \( U \subset \Gamma \) entraíne \( U = \Gamma \) .

> is linear (this is obvious) and bijective (a sequence satisfying (*) is uniquely determined by its first terms \( {u}_{0},\ldots ,{u}_{h - 1} \) ). Thus, \( U \) is of dimension \( h \) , and since \( \Gamma \) is of dimension \( {\alpha }_{1} + \cdots + {\alpha }_{p} = h \) , the inclusion \( U \subset \Gamma \) implies \( U = \Gamma \) .

Nous avons donc démontré la proposition 3 page 202.

> We have therefore proven proposition 3 on page 202.

Remarque. On démontre en général la proposition 3 page 202 en vérifiant directement que les expressions de la forme \( \mathop{\sum }\limits_{{i = 1}}^{p}{P}_{i}\left( n\right) {x}_{i}^{n} \) (avec \( {P}_{i} \) un polynôme de degré \( < {\alpha }_{i} \) ) sont bien solutions de la récurrence, puis en prouvant que la dimension de l'e.v correspondant est bien égal à celui des suites vérifiant la récurrence (comme dans la solution présentée ici). L'intérêt du problème proposé ici est qu'il permet de découvrir la forme générale de la solution sans la connaître a priori.

> Remark. Proposition 3 on page 202 is generally proven by directly verifying that expressions of the form \( \mathop{\sum }\limits_{{i = 1}}^{p}{P}_{i}\left( n\right) {x}_{i}^{n} \) (with \( {P}_{i} \) a polynomial of degree \( < {\alpha }_{i} \) ) are indeed solutions to the recurrence, then by proving that the dimension of the corresponding vector space is indeed equal to that of the sequences satisfying the recurrence (as in the solution presented here). The interest of the problem proposed here is that it allows one to discover the general form of the solution without knowing it a priori.

PROBLEME 6 (NOMBRES DE PISOT). a) Montrer que la série \( \sum \sin \left( {\pi {\left( 2 + \sqrt{3}\right) }^{n}}\right) \) converge. b) Plus généralement, on considère un polynôme \( P \) de degré d, unitaire,à coefficients entiers, et on suppose que ses racines \( {\xi }_{1},\ldots ,{\xi }_{d} \) vérifient \( \left| {\xi }_{1}\right| > 1 \) et \( \left| {\xi }_{k}\right| < 1 \) pour tout \( k \in \{ 2,\ldots , d\} \) (on dit que \( {\xi }_{1} \) est un nombre de Pisot). Montrer que la série \( \sum \sin \left( {\pi {\xi }_{1}^{n}}\right) \) converge.

> PROBLEM 6 (PISOT NUMBERS). a) Show that the series \( \sum \sin \left( {\pi {\left( 2 + \sqrt{3}\right) }^{n}}\right) \) converges. b) More generally, consider a monic polynomial \( P \) of degree d with integer coefficients, and assume its roots \( {\xi }_{1},\ldots ,{\xi }_{d} \) satisfy \( \left| {\xi }_{1}\right| > 1 \) and \( \left| {\xi }_{k}\right| < 1 \) for all \( k \in \{ 2,\ldots , d\} \) (we say that \( {\xi }_{1} \) is a Pisot number). Show that the series \( \sum \sin \left( {\pi {\xi }_{1}^{n}}\right) \) converges.

Solution. a) Il suffit de remarquer que pour tout \( n \in \mathbb{N},{\left( 2 + \sqrt{3}\right) }^{n} + {\left( 2 - \sqrt{3}\right) }^{n} \) est un entier (on s'en convainc en développant chacun des deux termes par la formule du binôme). Ceci entraîne \( \left| {\sin \left( {\pi {\left( 2 + \sqrt{3}\right) }^{n}}\right) }\right| = \left| {\sin \left( {\pi {\left( 2 - \sqrt{3}\right) }^{n}}\right) }\right| \) pour tout \( n \in \mathbb{N} \) . Comme \( \left| {\sin \left( {\pi {\left( 2 - \sqrt{3}\right) }^{n}}\right) }\right| \leq \pi {\left( 2 - \sqrt{3}\right) }^{n} \) et que \( \left| {2 - \sqrt{3}}\right| < 1 \) , on en déduit que notre série converge absolument, donc converge.

> Solution. a) It suffices to note that for all \( n \in \mathbb{N},{\left( 2 + \sqrt{3}\right) }^{n} + {\left( 2 - \sqrt{3}\right) }^{n} \) is an integer (one can be convinced of this by expanding each of the two terms using the binomial theorem). This implies \( \left| {\sin \left( {\pi {\left( 2 + \sqrt{3}\right) }^{n}}\right) }\right| = \left| {\sin \left( {\pi {\left( 2 - \sqrt{3}\right) }^{n}}\right) }\right| \) for all \( n \in \mathbb{N} \). Since \( \left| {\sin \left( {\pi {\left( 2 - \sqrt{3}\right) }^{n}}\right) }\right| \leq \pi {\left( 2 - \sqrt{3}\right) }^{n} \) and \( \left| {2 - \sqrt{3}}\right| < 1 \), we deduce that our series converges absolutely, and therefore converges.

b) Le polynôme \( P \) est unitaire à coefficients entiers, on en déduit que pour tout \( n \in \mathbb{N},{S}_{n} = \; {\xi }_{1}^{n} + \cdots + {\xi }_{d}^{n} \) est un entier \( \left( {S}_{n}\right. \) s’exprime comme un polynôme à coefficients entiers, symétrique en les \( {\xi }_{i} \) , donc s’exprime comme un polynôme à coefficients entiers en les fonctions symétriques des racines de \( P \) , et ces dernières sont entières donc \( {S}_{n} \in \mathbb{Z} \) . On peut aussi retrouver ce dernier résultat grâce aux formules de Newton - voir le tome Algèbre). Ceci entraîne

> b) The polynomial \( P \) is monic with integer coefficients, from which we deduce that for all \( n \in \mathbb{N},{S}_{n} = \; {\xi }_{1}^{n} + \cdots + {\xi }_{d}^{n} \) is an integer \( \left( {S}_{n}\right. \) expressed as a polynomial with integer coefficients, symmetric in the \( {\xi }_{i} \), and thus expressed as a polynomial with integer coefficients in the symmetric functions of the roots of \( P \), and the latter are integers, so \( {S}_{n} \in \mathbb{Z} \). One can also arrive at this latter result using Newton's sums - see the Algebra volume). This implies

\[
\left| {\sin \left( {\pi {\xi }_{1}^{n}}\right) }\right|  = \left| {\sin \left( {\pi \left( {{\xi }_{2}^{n} + \cdots  + {\xi }_{d}^{n}}\right) }\right) }\right|  \leq  \pi \left| {{\xi }_{2}^{n} + \cdots  + {\xi }_{d}^{n}}\right|  \leq  \pi \left( {{\left| {\xi }_{2}\right| }^{n} + \cdots  + {\left| {\xi }_{d}\right| }^{n}}\right)
\]

et comme \( \left| {\xi }_{k}\right| < 1 \) pour \( k \geq 2 \) , on en déduit la convergence de la série proposée.

> and since \( \left| {\xi }_{k}\right| < 1 \) for \( k \geq 2 \), we deduce the convergence of the proposed series.

Problem 7. a) Soit \( \alpha > 0 \) un nombre irrationnel. Pour tout \( N \in {\mathbb{N}}^{ * } \) , montrer

> Problem 7. a) Let \( \alpha > 0 \) be an irrational number. For all \( N \in {\mathbb{N}}^{ * } \), show

\[
\exists \left( {p, q}\right)  \in  {\mathbb{N}}^{2},\;1 \leq  q \leq  N,\;\left| {\alpha  - \frac{p}{q}}\right|  < \frac{1}{qN}.
\]

b) Donner la nature de la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\frac{1}{{n}^{2}{\sin }^{2}n} \) (on rappelle que \( \pi \) est un nombre irrationnel, voir le problème 15 page 187).

> b) Determine the nature of the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\frac{1}{{n}^{2}{\sin }^{2}n} \) (recall that \( \pi \) is an irrational number, see problem 15 page 187).

Solution. a) C'est classique. Nous allons utiliser une méthode connue sous le nom de principe des tiroirs. Pour tout \( x \in \mathbb{R} \) , notons \( \left\lbrack x\right\rbrack \) sa partie entière. On considère les nombres \( {u}_{k} = {k\alpha } - \left\lbrack {k\alpha }\right\rbrack \) pour \( k = 1,2,\ldots , N + 1 \) . Chacun des \( {u}_{k} \) est élément de \( \lbrack 0,1\lbrack \) , et pour tout \( k \) , il existe un unique \( i \in \{ 0,\ldots , N - 1\} \) tel que \( {u}_{k} \in \left\lbrack {\frac{i}{N},\frac{i + 1}{N}}\right. \) [. Autrement dit, nous rangeons les \( N + 1 \) nombres \( {u}_{k} \) dans les \( N \) "boites" \( \lbrack 0,\frac{1}{N}\lbrack ,\left\lbrack {\frac{1}{N},\frac{2}{N}\lbrack ,\ldots ,\left\lbrack {\frac{N - 1}{N},1\lbrack }\right. }\right. \) . Il existe donc une boite contenant au moins deux des nombres \( {u}_{k} \) , ce qui entraîne

> Solution. a) This is a classic. We will use a method known as the pigeonhole principle. For any \( x \in \mathbb{R} \), let \( \left\lbrack x\right\rbrack \) denote its integer part. Consider the numbers \( {u}_{k} = {k\alpha } - \left\lbrack {k\alpha }\right\rbrack \) for \( k = 1,2,\ldots , N + 1 \). Each \( {u}_{k} \) is an element of \( \lbrack 0,1\lbrack \), and for any \( k \), there exists a unique \( i \in \{ 0,\ldots , N - 1\} \) such that \( {u}_{k} \in \left\lbrack {\frac{i}{N},\frac{i + 1}{N}}\right. \) [. In other words, we place the \( N + 1 \) numbers \( {u}_{k} \) into the \( N \) "boxes" \( \lbrack 0,\frac{1}{N}\lbrack ,\left\lbrack {\frac{1}{N},\frac{2}{N}\lbrack ,\ldots ,\left\lbrack {\frac{N - 1}{N},1\lbrack }\right. }\right. \). There must therefore be a box containing at least two of the numbers \( {u}_{k} \), which implies

\[
\exists a, b \in  \{ 1,\ldots , N + 1\} , a < b,\;\left| {{u}_{b} - {u}_{a}}\right|  < \frac{1}{N},
\]

ce qui s’écrit encore \( \left| {\left( {b - a}\right) \alpha - \left( {\left\lbrack {b\alpha }\right\rbrack - \left\lbrack {a\alpha }\right\rbrack }\right) }\right| < 1/N \) . En posant \( p = \left\lbrack {b\alpha }\right\rbrack - \left\lbrack {a\alpha }\right\rbrack \) et \( q = b - a \) , on a donc \( \left( {p, q}\right) \in {\mathbb{N}}^{2},1 \leq q \leq N \) et \( \left| {{q\alpha } - p}\right| < 1/N \) , d’où le résultat.

> which can also be written as \( \left| {\left( {b - a}\right) \alpha - \left( {\left\lbrack {b\alpha }\right\rbrack - \left\lbrack {a\alpha }\right\rbrack }\right) }\right| < 1/N \). By setting \( p = \left\lbrack {b\alpha }\right\rbrack - \left\lbrack {a\alpha }\right\rbrack \) and \( q = b - a \), we have \( \left( {p, q}\right) \in {\mathbb{N}}^{2},1 \leq q \leq N \) and \( \left| {{q\alpha } - p}\right| < 1/N \), hence the result.

b) La question précédente entraîne l’existence, pour tout \( n \in {\mathbb{N}}^{ * } \) , d’un couple \( \left( {{p}_{n},{q}_{n}}\right) \in {\mathbb{N}}^{2} \) tel que \( 1 \leq {q}_{n} \leq n \) et \( \left| {\pi - {p}_{n}/{q}_{n}}\right| \leq 1/\left( {n{q}_{n}}\right) \leq 1/{q}_{n}^{2} \) . La suite de rationnels \( \left( {{p}_{n}/{q}_{n}}\right) \) tend vers le nombre irrationnel \( \pi \) , donc \( \left( {p}_{n}\right) \) et \( \left( {q}_{n}\right) \) tendent vers \( + \infty \) (voir l’exercice 4 page 205). Ensuite, pour tout \( n \in {\mathbb{N}}^{ * } \) , on a \( \left| {{p}_{n} - \pi {q}_{n}}\right| \leq 1/{q}_{n} \) donc

> b) The previous question implies the existence, for any \( n \in {\mathbb{N}}^{ * } \), of a pair \( \left( {{p}_{n},{q}_{n}}\right) \in {\mathbb{N}}^{2} \) such that \( 1 \leq {q}_{n} \leq n \) and \( \left| {\pi - {p}_{n}/{q}_{n}}\right| \leq 1/\left( {n{q}_{n}}\right) \leq 1/{q}_{n}^{2} \). The sequence of rationals \( \left( {{p}_{n}/{q}_{n}}\right) \) tends toward the irrational number \( \pi \), so \( \left( {p}_{n}\right) \) and \( \left( {q}_{n}\right) \) tend toward \( + \infty \) (see exercise 4 on page 205). Then, for any \( n \in {\mathbb{N}}^{ * } \), we have \( \left| {{p}_{n} - \pi {q}_{n}}\right| \leq 1/{q}_{n} \) therefore

\[
{\sin }^{2}{p}_{n} = {\sin }^{2}\left( {{p}_{n} - \pi {q}_{n}}\right)  \leq  {\left( {p}_{n} - \pi {q}_{n}\right) }^{2} \leq  1/{q}_{n}^{2},
\]

donc \( {p}_{n}^{2}{\sin }^{2}{p}_{n} \leq {p}_{n}^{2}/{q}_{n}^{2} \) , et comme \( \left( {{p}_{n}/{q}_{n}}\right) \) converge, la suite \( \left( {{p}_{n}^{2}{\sin }^{2}{p}_{n}}\right) \) est majorée. Donc la suite de terme général \( {\left( {p}_{n}^{2}{\sin }^{2}{p}_{n}\right) }^{-1} \) est minorée par une constante \( > 0 \) . On en déduit que le terme général de la série proposée ne tend pas vers 0, donc la série diverge.

> therefore \( {p}_{n}^{2}{\sin }^{2}{p}_{n} \leq {p}_{n}^{2}/{q}_{n}^{2} \) , and since \( \left( {{p}_{n}/{q}_{n}}\right) \) converges, the sequence \( \left( {{p}_{n}^{2}{\sin }^{2}{p}_{n}}\right) \) is bounded above. Thus the sequence with general term \( {\left( {p}_{n}^{2}{\sin }^{2}{p}_{n}\right) }^{-1} \) is bounded below by a constant \( > 0 \) . We deduce that the general term of the proposed series does not tend to 0, so the series diverges.

Problem 8. Soit \( g : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction continue, convexe, avec \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = 0 \) . a) Montrer que la fonction suivante est bien définie

> Problem 8. Let \( g : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a continuous, convex function, with \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = 0 \) . a) Show that the following function is well-defined

\[
S : \rbrack 0, + \infty \lbrack  \rightarrow  \mathbb{R}\;h \mapsto  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}g\left( {nh}\right) .
\]

b) Montrer que \( \mathop{\lim }\limits_{{h \rightarrow {0}^{ + }}}S\left( h\right) = \frac{g\left( 0\right) }{2} \) .

> b) Show that \( \mathop{\lim }\limits_{{h \rightarrow {0}^{ + }}}S\left( h\right) = \frac{g\left( 0\right) }{2} \) .

Solution. a) Si on montre que \( g \) est décroissante sur \( {\mathbb{R}}^{ + } \) , alors \( g \) sera positive (car \( g\left( x\right) \rightarrow 0 \) quand \( x \rightarrow + \infty ) \) et la série \( \sum {\left( -1\right) }^{n}g\left( {nh}\right) \) sera convergente pour tout \( h > 0 \) (série alternée dont la valeur absolue du terme général décroît et tend vers 0 ), ce qui prouvera le résultat.

> Solution. a) If we show that \( g \) is decreasing on \( {\mathbb{R}}^{ + } \) , then \( g \) will be positive (since \( g\left( x\right) \rightarrow 0 \) as \( x \rightarrow + \infty ) \) and the series \( \sum {\left( -1\right) }^{n}g\left( {nh}\right) \) will be convergent for all \( h > 0 \) (alternating series whose absolute value of the general term decreases and tends to 0 ), which will prove the result.

Soient \( a, b \in \mathbb{R},0 \leq a < b \) . Comme \( g \) est convexe, son graphe à droite de \( b \) est au dessus de la corde reliant \( \left( {a, g\left( a\right) }\right) \) à \( \left( {b, g\left( b\right) }\right) \) ce qui s’écrit

> Let \( a, b \in \mathbb{R},0 \leq a < b \) . Since \( g \) is convex, its graph to the right of \( b \) is above the chord connecting \( \left( {a, g\left( a\right) }\right) \) to \( \left( {b, g\left( b\right) }\right) \) which is written

\[
\forall t > b,\;g\left( t\right)  \geq  g\left( b\right)  + \left( {t - b}\right) \frac{g\left( b\right)  - g\left( a\right) }{b - a}.
\]

Comme \( g\left( t\right) \) tend vers 0 à l’infini, ceci n’est possible que si \( \left( {g\left( b\right) - g\left( a\right) }\right) /\left( {b - a}\right) \leq 0 \) , donc \( g\left( b\right) \leq g\left( a\right) \) . Donc \( g \) est bien décroissante.

> Since \( g\left( t\right) \) tends to 0 at infinity, this is only possible if \( \left( {g\left( b\right) - g\left( a\right) }\right) /\left( {b - a}\right) \leq 0 \) , so \( g\left( b\right) \leq g\left( a\right) \) . Thus \( g \) is indeed decreasing.

b) On remarque que \( R : h \mapsto S\left( h\right) - g\left( 0\right) /2 \) vérifie

> b) We note that \( R : h \mapsto S\left( h\right) - g\left( 0\right) /2 \) satisfies

\[
\forall h > 0,\;R\left( h\right)  = \frac{1}{2}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}{A}_{n}\left( h\right) \;\text{ avec }\;{A}_{n}\left( h\right)  = g\left( {nh}\right)  - g\left( {\left( {n + 1}\right) h}\right) .
\]

Comme \( g \) est décroissante, on a \( {A}_{n}\left( h\right) \geq 0 \) pour tout \( n \) et pour tout \( h > 0 \) . De plus la convexité de \( g \) entraîne

> Since \( g \) is decreasing, we have \( {A}_{n}\left( h\right) \geq 0 \) for all \( n \) and for all \( h > 0 \) . Furthermore, the convexity of \( g \) implies

\[
\forall h > 0,\forall n \in  {\mathbb{N}}^{ * },\;g\left( {nh}\right)  = g\left( \frac{\left( {n - 1}\right) h + \left( {n + 1}\right) h}{2}\right)  \leq  \frac{g\left( {\left( {n - 1}\right) h}\right) }{2} + \frac{g\left( {\left( {n + 1}\right) h}\right) }{2}
\]

c’est-à-dire \( g\left( {nh}\right) - g\left( {\left( {n + 1}\right) h}\right) \leq g\left( {\left( {n - 1}\right) h}\right) - g\left( {nh}\right) \) . Autrement dit, la suite \( \left( {{A}_{n}\left( h\right) }\right) \) décroît pour tout \( h > 0 \) .

> that is to say \( g\left( {nh}\right) - g\left( {\left( {n + 1}\right) h}\right) \leq g\left( {\left( {n - 1}\right) h}\right) - g\left( {nh}\right) \) . In other words, the sequence \( \left( {{A}_{n}\left( h\right) }\right) \) decreases for all \( h > 0 \) .

Finalement, \( \sum {\left( -1\right) }^{n}{A}_{n}\left( h\right) \) apparaît comme une série alternée dont la valeur absolue du terme général décroît et tend vers 0 . On peut donc écrire (voir le théorème 6 page 214)

> Finally, \( \sum {\left( -1\right) }^{n}{A}_{n}\left( h\right) \) appears as an alternating series whose absolute value of the general term decreases and tends to 0 . We can therefore write (see theorem 6 page 214)

\[
\forall h > 0,\;\left| {{2R}\left( h\right) }\right|  = \left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}{A}_{n}\left( h\right) }\right|  \leq  {A}_{0}\left( h\right)  = g\left( 0\right)  - g\left( h\right) .
\]

On en déduit que \( R\left( h\right) \) tend vers 0 lorsque \( h \rightarrow {0}^{ + } \) ( \( g \) est continue), donc \( S\left( h\right) \rightarrow g\left( 0\right) /2 \) lorsque \( h \rightarrow {0}^{ + } \) .

> We deduce that \( R\left( h\right) \) tends to 0 as \( h \rightarrow {0}^{ + } \) ( \( g \) is continuous), therefore \( S\left( h\right) \rightarrow g\left( 0\right) /2 \) as \( h \rightarrow {0}^{ + } \) .

Problem 9. Donner un équivalent, lorsque \( x \rightarrow {1}^{ - } \) , de la fonction

> Problem 9. Give an equivalent, as \( x \rightarrow {1}^{ - } \) , of the function

\[
f : \left\lbrack  {0,1\left\lbrack  { \rightarrow  \mathbb{R}\;x \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n}}{1 - {x}^{n}}.}\right. }\right.
\]

Solution. L’identité \( 1 - {x}^{n} = \left( {1 - x}\right) {P}_{n}\left( x\right) \) avec \( {P}_{n}\left( x\right) = 1 + x + \cdots + {x}^{n - 1} \) montre que

> Solution. The identity \( 1 - {x}^{n} = \left( {1 - x}\right) {P}_{n}\left( x\right) \) with \( {P}_{n}\left( x\right) = 1 + x + \cdots + {x}^{n - 1} \) shows that

\[
\forall x \in  \lbrack 0,1\lbrack ,\;g\left( x\right)  = \left( {1 - x}\right) f\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n}}{{P}_{n}\left( x\right) }.
\]

On se ramène ainsi à donner un équivalent de \( g \) . Pour \( n \) fixé, on a \( {P}_{n}\left( x\right) \rightarrow n \) lorsque \( x \rightarrow {1}^{ - } \) , ce qui amène à penser que \( g\left( x\right) \) est équivalent à \( h\left( x\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}/n = - \log \left( {1 - x}\right) \) . Montrons ce dernier résultat. Compte tenu du fait que, pour \( 0 \leq x < 1 \) ,

> We thus reduce the problem to finding an equivalent of \( g \) . For fixed \( n \) , we have \( {P}_{n}\left( x\right) \rightarrow n \) as \( x \rightarrow {1}^{ - } \) , which leads us to think that \( g\left( x\right) \) is equivalent to \( h\left( x\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}/n = - \log \left( {1 - x}\right) \) . Let us prove this latter result. Given that, for \( 0 \leq x < 1 \) ,

\[
0 \leq  n - {P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left( {1 - {x}^{k}}\right)  = \left( {1 - x}\right) \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{P}_{k}\left( x\right)  \leq  \left( {1 - x}\right) \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{P}_{n}\left( x\right)  \leq  n\left( {1 - x}\right) {P}_{n}\left( x\right) ,
\]

on en déduit, pour tout \( x \in \lbrack 0,1\lbrack \) ,

> we deduce, for all \( x \in \lbrack 0,1\lbrack \) ,

\[
0 \leq  g\left( x\right)  - h\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}\frac{n - {P}_{n}\left( x\right) }{n{P}_{n}\left( x\right) } \leq  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}\frac{n\left( {1 - x}\right) {P}_{n}\left( x\right) }{n{P}_{n}\left( x\right) } = \left( {1 - x}\right) \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n} = x \leq  1.
\]

Ainsi, lorsque \( x \rightarrow {1}^{ - }, g\left( x\right) = h\left( x\right) + O\left( 1\right) = - \log \left( {1 - x}\right) + O\left( 1\right) \sim - \log \left( {1 - x}\right) \) , donc \( f\left( x\right) \sim \log \left( {1 - x}\right) /\left( {x - 1}\right) . \)

> Thus, as \( x \rightarrow {1}^{ - }, g\left( x\right) = h\left( x\right) + O\left( 1\right) = - \log \left( {1 - x}\right) + O\left( 1\right) \sim - \log \left( {1 - x}\right) \) , therefore \( f\left( x\right) \sim \log \left( {1 - x}\right) /\left( {x - 1}\right) . \)

PROBLEME 10 (UNE SÉRIE ENTIÉRE SEMI-CONVERGENTE SUR TOUT SON CERCLE DE CONVERGENCE). 1/ Soient \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) et \( {\left( {b}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) deux suites complexes. On pose \( {\sigma }_{0} = 0 \) et pour tout \( n \in {\mathbb{N}}^{ * },{\sigma }_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k} \) . Montrer que \( \sum {a}_{n}{b}_{n} \) converge dans les cas suivants : a) (i) \( \left( {\sigma }_{n}\right) \) est bornée,(ii) \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) converge,(iii) \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{b}_{n} = 0 \) . b) (i) \( \left( {{\sigma }_{n}/\sqrt{n}}\right) \) est bornée,(ii) \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \sqrt{n} \) converge,(iii) \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{b}_{n}\sqrt{n} = 0 \) . 2/ (Application.) Montrer que la série entière

> PROBLEM 10 (A POWER SERIES SEMI-CONVERGENT ON ITS ENTIRE CIRCLE OF CONVERGENCE). 1/ Let \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) and \( {\left( {b}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be two complex sequences. Let \( {\sigma }_{0} = 0 \) and for all \( n \in {\mathbb{N}}^{ * },{\sigma }_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k} \) . Show that \( \sum {a}_{n}{b}_{n} \) converges in the following cases: a) (i) \( \left( {\sigma }_{n}\right) \) is bounded, (ii) \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) converges, (iii) \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{b}_{n} = 0 \) . b) (i) \( \left( {{\sigma }_{n}/\sqrt{n}}\right) \) is bounded, (ii) \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \sqrt{n} \) converges, (iii) \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{b}_{n}\sqrt{n} = 0 \) . 2/ (Application.) Show that the power series

\[
\mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\frac{{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  }}{n}{z}^{n}
\]

(où \( \left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) ) est convergente en tout point de son cercle de convergence \( \left| z\right| = 1 \) , mais n’est absolument convergente en aucun point de ce cercle (traiter séparément les cas \( z = 1 \) et \( z \neq 1 \) ).

> (where \( \left\lbrack x\right\rbrack \) denotes the integer part of \( x \) ) is convergent at every point of its circle of convergence \( \left| z\right| = 1 \) , but is not absolutely convergent at any point of this circle (treat the cases \( z = 1 \) and \( z \neq 1 \) separately).

Solution. 1 / Dans les deux cas, on utilisera la relation suivante, conséquence d'une transformation d'Abel :

> Solution. 1/ In both cases, we will use the following relation, which is a consequence of an Abel transformation:

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}{b}_{k} = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {{\sigma }_{k} - {\sigma }_{k - 1}}\right) {b}_{k} = \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{\sigma }_{k}\left( {{b}_{k} - {b}_{k + 1}}\right)  + {\sigma }_{n}{b}_{n}.
\]

(*)

> a) Si \( M \) désigne un majorant de la suite \( \left( \left| {\sigma }_{n}\right| \right) \) , on a \( \left| {{\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) }\right| \leq M\left| {{b}_{n} - {b}_{n + 1}}\right| \) , donc \( \sum {\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) \) converge absolument d’après (ii), et comme \( \left| {{\sigma }_{n}{b}_{n}}\right| \leq M\left| {b}_{n}\right| \) tend vers0d’après (iii), on en conclut avec (*) la convergence de \( \sum {a}_{k}{b}_{k} \) .

a) If \( M \) denotes an upper bound of the sequence \( \left( \left| {\sigma }_{n}\right| \right) \), we have \( \left| {{\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) }\right| \leq M\left| {{b}_{n} - {b}_{n + 1}}\right| \), so \( \sum {\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) \) converges absolutely according to (ii), and since \( \left| {{\sigma }_{n}{b}_{n}}\right| \leq M\left| {b}_{n}\right| \) tends to 0 according to (iii), we conclude with (*) the convergence of \( \sum {a}_{k}{b}_{k} \).

> b) Soit \( M \) un majorant de \( \left( \left| {{\sigma }_{n}/\sqrt{n}}\right| \right) \) , de sorte que \( \left| {\sigma }_{n}\right| \leq M\sqrt{n} \) pour tout \( n \) . On a \( \mid {\sigma }_{n}\left( {{b}_{n} - }\right. \; \left. {b}_{n + 1}\right) \left| { \leq M\left| {{b}_{n} - {b}_{n + 1}}\right| \sqrt{n}\text{ donc }\sum {\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) \text{ converge absolument d’après (ii). Or }\left| {{\sigma }_{n}{b}_{n}}\right| \leq }\right| \; M\left| {b}_{n}\right| \sqrt{n} \) tend vers 0 d’après (iii), d’où le résultat avec (*).

b) Let \( M \) be an upper bound of \( \left( \left| {{\sigma }_{n}/\sqrt{n}}\right| \right) \), such that \( \left| {\sigma }_{n}\right| \leq M\sqrt{n} \) for all \( n \). We have \( \mid {\sigma }_{n}\left( {{b}_{n} - }\right. \; \left. {b}_{n + 1}\right) \left| { \leq M\left| {{b}_{n} - {b}_{n + 1}}\right| \sqrt{n}\text{ donc }\sum {\sigma }_{n}\left( {{b}_{n} - {b}_{n + 1}}\right) \text{ converge absolument d’après (ii). Or }\left| {{\sigma }_{n}{b}_{n}}\right| \leq }\right| \; M\left| {b}_{n}\right| \sqrt{n} \) tending to 0 according to (iii), hence the result with (*).

> 2/ Commençons par le cas \( z = 1 \) . D’après la question 1/b) appliquée avec \( {a}_{n} = {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack } \) et \( {b}_{n} = 1/n \) , la convergence de \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }/n \) sera assurée si on montre que les sommes partielles \( {\sigma }_{n} \) de \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack } \) sont majorées en valeur absolue par un terme de la forme \( M\sqrt{n} \) . Montrons donc ce point.

2/ Let us begin with the case \( z = 1 \). According to question 1/b) applied with \( {a}_{n} = {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack } \) and \( {b}_{n} = 1/n \), the convergence of \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }/n \) will be ensured if we show that the partial sums \( {\sigma }_{n} \) of \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack } \) are bounded in absolute value by a term of the form \( M\sqrt{n} \). Let us therefore show this point.

> Pour tout entier naturel impair \( p \) on a

For any odd natural number \( p \), we have

\[
\mathop{\sum }\limits_{{n = {p}^{2}}}^{{{\left( p + 2\right) }^{2} - 1}}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  } = \mathop{\sum }\limits_{{n = {p}^{2}}}^{{{\left( p + 1\right) }^{2} - 1}}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  } + \mathop{\sum }\limits_{{n = {\left( p + 1\right) }^{2}}}^{{{\left( p + 2\right) }^{2} - 1}}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  } = {\left( -1\right) }^{p}\left( {{2p} + 1}\right)  + {\left( -1\right) }^{p + 1}\left( {{2p} + 3}\right)  = 2.
\]

Donnons nous maintenant \( N \in {\mathbb{N}}^{ * } \) et notons \( {N}_{0} \) le plus grand entier tel que \( {\left( 2{N}_{0} + 1\right) }^{2} \leq N \) . On a

> Now let us consider \( N \in {\mathbb{N}}^{ * } \) and denote by \( {N}_{0} \) the largest integer such that \( {\left( 2{N}_{0} + 1\right) }^{2} \leq N \). We have

\[
\mathop{\sum }\limits_{{n = 1}}^{{{\left( 2{N}_{0} + 1\right) }^{2} - 1}}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  } = \mathop{\sum }\limits_{{k = 0}}^{{{N}_{0} - 1}}\left( {\mathop{\sum }\limits_{{n = {\left( 2k + 1\right) }^{2}}}^{{{\left( 2k + 3\right) }^{2} - 1}}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  }}\right)  = \mathop{\sum }\limits_{{k = 0}}^{{{N}_{0} - 1}}2 = 2{N}_{0} \leq  \sqrt{N} - 1,
\]

et comme \( {\left( 2{N}_{0} + 1\right) }^{2} \leq N < {\left( 2{N}_{0} + 3\right) }^{2} \) ,

> and since \( {\left( 2{N}_{0} + 1\right) }^{2} \leq N < {\left( 2{N}_{0} + 3\right) }^{2} \),

\[
\left| {\mathop{\sum }\limits_{{n = {\left( 2{N}_{0} + 1\right) }^{2}}}^{N}{\left( -1\right) }^{\left\lbrack  \sqrt{n}\right\rbrack  }}\right|  \leq  N + 1 - {\left( 2{N}_{0} + 1\right) }^{2} \leq  {\left( 2{N}_{0} + 3\right) }^{2} - {\left( 2{N}_{0} + 1\right) }^{2} = 8\left( {{N}_{0} + 1}\right)  \leq  4\sqrt{N} + 4.
\]

Ceci montre que \( \left| {\sigma }_{N}\right| \leq \left( {\sqrt{N} - 1}\right) + \left( {4\sqrt{N} + 4}\right) = 5\sqrt{N} + 3 \leq 8\sqrt{N} \) pour tout \( N \in {\mathbb{N}}^{ * } \) , d’où le résultat.

> This shows that \( \left| {\sigma }_{N}\right| \leq \left( {\sqrt{N} - 1}\right) + \left( {4\sqrt{N} + 4}\right) = 5\sqrt{N} + 3 \leq 8\sqrt{N} \) for all \( N \in {\mathbb{N}}^{ * } \), hence the result.

Passons maintenant au cas où \( \left| z\right| = 1 \) et \( z \neq 1 \) . On écrit \( z = {e}^{i\theta } \) avec \( 0 < \theta < {2\pi } \) , et il s’agit de montrer la convergence de \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }{e}^{ni\theta }/n \) . Pour cela, on va appliquer 1/a) avec \( {a}_{n} = {e}^{ni\theta } \) et \( {b}_{n} = {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }/n. \)

> Let us now move on to the case where \( \left| z\right| = 1 \) and \( z \neq 1 \) . We write \( z = {e}^{i\theta } \) with \( 0 < \theta < {2\pi } \) , and the goal is to show the convergence of \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }{e}^{ni\theta }/n \) . To do this, we will apply 1/a) with \( {a}_{n} = {e}^{ni\theta } \) and \( {b}_{n} = {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }/n. \)

(i). La suite \( \left( {\sigma }_{n}\right) \) est bornée car

> (i). The sequence \( \left( {\sigma }_{n}\right) \) is bounded because

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\sigma }_{n} = \left| {\mathop{\sum }\limits_{{k = 1}}^{n}{e}^{ki\theta }}\right|  = \left| {{e}^{i\theta }\frac{1 - {e}^{ni\theta }}{1 - {e}^{i\theta }}}\right|  \leq  \frac{2}{\left| 1 - {e}^{i\theta }\right| }.
\]

(ii). Pour montrer que \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) converge, on remarque d’abord

> (ii). To show that \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) converges, we first note

si \( \;\exists p \geq 2\left( {p \in \mathbb{N}}\right) , n + 1 = {p}^{2}\; \) alors \( \;\left| {{b}_{n} - {b}_{n + 1}}\right| = \frac{1}{n} + \frac{1}{n + 1} = \frac{1}{{p}^{2} - 1} + \frac{1}{{p}^{2}} \) si \( \;\exists p \in {\mathbb{N}}^{ * },{p}^{2} \leq n < n + 1 < {\left( p + 1\right) }^{2} \) alors \( \left| {{b}_{n} - {b}_{n + 1}}\right| = \frac{1}{n} - \frac{1}{n + 1} = \frac{1}{n\left( {n + 1}\right) } \) .

> if \( \;\exists p \geq 2\left( {p \in \mathbb{N}}\right) , n + 1 = {p}^{2}\; \) then \( \;\left| {{b}_{n} - {b}_{n + 1}}\right| = \frac{1}{n} + \frac{1}{n + 1} = \frac{1}{{p}^{2} - 1} + \frac{1}{{p}^{2}} \) if \( \;\exists p \in {\mathbb{N}}^{ * },{p}^{2} \leq n < n + 1 < {\left( p + 1\right) }^{2} \) then \( \left| {{b}_{n} - {b}_{n + 1}}\right| = \frac{1}{n} - \frac{1}{n + 1} = \frac{1}{n\left( {n + 1}\right) } \) .

On en déduit

> We deduce from this

\[
\forall N \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{n = 1}}^{N}\left| {{b}_{n} - {b}_{n + 1}}\right|  \leq  \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{n\left( {n + 1}\right) } + \mathop{\sum }\limits_{{p = 2}}^{\left\lbrack  \sqrt{N + 1}\right\rbrack  }\left( {\frac{1}{{p}^{2} - 1} + \frac{1}{{p}^{2}}}\right) ,
\]

et comme les séries \( \sum 1/\left( {n\left( {n + 1}\right) }\right) ,\sum 1/\left( {{p}^{2} - 1}\right) \) et \( \sum 1/{p}^{2} \) convergent, on en déduit que \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) est bornée donc converge.

> and since the series \( \sum 1/\left( {n\left( {n + 1}\right) }\right) ,\sum 1/\left( {{p}^{2} - 1}\right) \) and \( \sum 1/{p}^{2} \) converge, we deduce that \( \sum \left| {{b}_{n} - {b}_{n + 1}}\right| \) is bounded and therefore converges.

(iii) est trivialement vérifiée.

> (iii) is trivially satisfied.

Ainsi, pour tout \( z \in \mathbb{C} \) tel que \( \left| z\right| = 1 \) , la série \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }{z}^{n}/n \) converge, mais ne converge pas absolument. En d'autres termes, notre série entière est semi-convergente en tout point de son cercle de convergence.

> Thus, for any \( z \in \mathbb{C} \) such that \( \left| z\right| = 1 \) , the series \( \sum {\left( -1\right) }^{\left\lbrack \sqrt{n}\right\rbrack }{z}^{n}/n \) converges, but does not converge absolutely. In other words, our power series is semi-convergent at every point on its circle of convergence.

PROBLEME 11. a) Montrer que la série entière \( \sum {z}^{n}/{\left( n!\right) }^{2} \) a un rayon de convergence infini. Soit \( f \) sa somme.

> PROBLEM 11. a) Show that the power series \( \sum {z}^{n}/{\left( n!\right) }^{2} \) has an infinite radius of convergence. Let \( f \) be its sum.

b) Pour tout \( x > 0 \) , comparer \( f\left( x\right) \) et

> b) For any \( x > 0 \) , compare \( f\left( x\right) \) and

\[
I\left( x\right)  = {\int }_{-\pi /2}^{\pi /2}\exp \left( {2\sqrt{x}\sin t}\right) {dt}.
\]

c) En déduire, lorsque \( x \rightarrow + \infty \) , un équivalent de \( f\left( x\right) \) .

> c) Deduce, when \( x \rightarrow + \infty \) , an equivalent for \( f\left( x\right) \) .

Solution.

> Solution.

a) C’est facile, car on a l’encadrement \( 0 \leq 1/{\left( n!\right) }^{2} \leq 1/n \) ! et la série \( \sum {z}^{n}/n \) ! a un rayon de convergence infini.

> a) This is easy, because we have the inequality \( 0 \leq 1/{\left( n!\right) }^{2} \leq 1/n \) ! and the series \( \sum {z}^{n}/n \) ! has an infinite radius of convergence.

b) Fixons \( x > 0 \) . La série de fonctions \( \sum {\left( 2\sqrt{x}\sin t\right) }^{n}/n \) ! de la variable \( t \) converge normalement sur \( \left\lbrack {-\pi /2,\pi /2}\right\rbrack \) (car \( 2\sqrt{x}\sin t \) y est bornée) vers la fonction \( t \mapsto \exp \left( {2\sqrt{x}\sin t}\right) \) , donc on est autorisé à intervertir les signes de sommation en écrivant

> b) Let \( x > 0 \) be fixed. The series of functions \( \sum {\left( 2\sqrt{x}\sin t\right) }^{n}/n \) of the variable \( t \) converges normally on \( \left\lbrack {-\pi /2,\pi /2}\right\rbrack \) (since \( 2\sqrt{x}\sin t \) is bounded there) to the function \( t \mapsto \exp \left( {2\sqrt{x}\sin t}\right) \) , so we are permitted to interchange the summation signs by writing

\[
I\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\int }_{-\pi /2}^{\pi /2}\frac{{2}^{n}{x}^{n/2}}{n!}{\sin }^{n}{tdt} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{2}^{n}{x}^{n/2}}{n!}{I}_{n},\;\text{ où }\;\forall n \in  \mathbb{N},\;{I}_{n} = {\int }_{-\pi /2}^{\pi /2}{\sin }^{n}{tdt}.
\]

(*)

> Lorsque \( n = {2k} + 1 \) est impair, l’intégrande de \( {I}_{{2k} + 1} \) est impaire donc \( {I}_{{2k} + 1} = 0 \) . Lorsque \( n = {2k} \) est pair, \( {I}_{2k} \) s’exprime au moyen des intégrales de Wallis (voir l’exercice 1 page 130)

When \( n = {2k} + 1 \) is odd, the integrand of \( {I}_{{2k} + 1} \) is odd, so \( {I}_{{2k} + 1} = 0 \) . When \( n = {2k} \) is even, \( {I}_{2k} \) is expressed using Wallis integrals (see exercise 1 on page 130)

\[
{I}_{2k} = 2{\int }_{0}^{\pi /2}{\sin }^{2k}{tdt} = \frac{\left( {{2k} - 1}\right) \left( {{2k} - 3}\right) \cdots 1}{{2k}\left( {{2k} - 2}\right) \cdots 2}\frac{\pi }{2} = \frac{\left( {2k}\right) !}{{2}^{2k}{\left( k!\right) }^{2}}\pi ,
\]

et donc (*) s'écrit

> and therefore (*) is written

\[
I\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{{2}^{2k}{x}^{k}}{\left( {2k}\right) !}{I}_{2k} = \frac{1}{\pi }\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{{x}^{k}}{{\left( k!\right) }^{2}} = \frac{f\left( x\right) }{\pi }.
\]

c) Il s’agit de donner un équivalent de l’intégrale \( I\left( x\right) \) lorsque \( x \rightarrow + \infty \) . On pourrait s’en tirer en appliquant directement la méthode de Laplace (voir le théorème 4 page 164). Comme cette dernière n'est pas au programme de mathématiques spéciales, nous allons nous mettre dans les conditions du concours et en faire abstraction.

> c) The goal is to provide an equivalent for the integral \( I\left( x\right) \) as \( x \rightarrow + \infty \) . One could manage by applying Laplace's method directly (see theorem 4 on page 164). Since the latter is not in the special mathematics curriculum, we will put ourselves in the conditions of the competitive exam and disregard it.

Pour simplifier l’intégrande, nous commençons par faire le changement de variable \( u = \; 2\sqrt{x}\sin t \) qui donne

> To simplify the integrand, we begin by making the change of variable \( u = \; 2\sqrt{x}\sin t \) which gives

\[
\forall x > 0,\;I\left( x\right)  = {\int }_{-2\sqrt{x}}^{2\sqrt{x}}\frac{{e}^{u}}{\sqrt{{4x} - {u}^{2}}}{du}.
\]

Lorsque \( x \) est grand, c’est la partie des \( u \) proche de \( 2\sqrt{x} \) qui contribue le plus à la valeur de l'intégrale. Pour ramener ce maximum à une abscisse fixe, on fait le changement de variable \( v = 2\sqrt{x} - u \) qui donne

> When \( x \) is large, it is the part of \( u \) close to \( 2\sqrt{x} \) that contributes most to the value of the integral. To bring this maximum to a fixed abscissa, we make the change of variable \( v = 2\sqrt{x} - u \) which gives

\[
\forall x > 0,\;I\left( x\right)  = {\int }_{0}^{4\sqrt{x}}\frac{{e}^{2\sqrt{x} - v}}{\sqrt{4\sqrt{x}v + {v}^{2}}}{dv} = \frac{{e}^{2\sqrt{x}}}{2{x}^{1/4}}J\left( x\right) ,\;J\left( x\right)  = {\int }_{0}^{4\sqrt{x}}\frac{{e}^{-v}}{\sqrt{v + {v}^{2}{x}^{-1/2}/4}}{dv}.
\]

Lorsque \( x \rightarrow + \infty \) , l’intégrande de \( J\left( x\right) \) tend vers \( {e}^{-v}/\sqrt{v} \) , et on s’attend à ce que \( J\left( x\right) \) converge vers l’intégrale correspondante. Pour prouver ce point, nous utilisons l’inégalité \( \mid {\left( v + a\right) }^{-1/2} - \; {v}^{-1/2} \mid \leq a/{v}^{3/2} \) pour \( a \geq 0 \) (conséquence de l’inégalité des accroissements finis) qui entraîne

> When \( x \rightarrow + \infty \) , the integrand of \( J\left( x\right) \) tends toward \( {e}^{-v}/\sqrt{v} \) , and we expect \( J\left( x\right) \) to converge to the corresponding integral. To prove this point, we use the inequality \( \mid {\left( v + a\right) }^{-1/2} - \; {v}^{-1/2} \mid \leq a/{v}^{3/2} \) for \( a \geq 0 \) (a consequence of the mean value inequality) which leads to

\[
\forall x > 0,\;\left| {J\left( x\right)  - {\int }_{0}^{4\sqrt{x}}\frac{{e}^{-v}}{\sqrt{v}}{dv}}\right|  \leq  {\int }_{0}^{4\sqrt{x}}\frac{{v}^{2}}{4\sqrt{x}}\frac{1}{{v}^{3/2}}{e}^{-v}{dv} = \frac{1}{4\sqrt{x}}{\int }_{0}^{4\sqrt{x}}{v}^{1/2}{e}^{-v}{dv},
\]

et comme \( {\int }_{0}^{+\infty }{v}^{1/2}{e}^{-v}{dv} \) converge, on en déduit \( J\left( x\right) = {\int }_{0}^{4\sqrt{x}}{e}^{-v}/\sqrt{v}{dv} + O\left( {1/\sqrt{x}}\right) \) donc \( J\left( x\right) \) converge vers \( K = {\int }_{0}^{+\infty }{e}^{-v}{v}^{-1/2}{dv} \) lorsque \( x \rightarrow + \infty \) . Or \( K = \Gamma \left( {1/2}\right) = \sqrt{\pi } \) (voir la question 2/d) du sujet d’étude 1 page 315), donc finalement, lorsque \( x \rightarrow + \infty \) ,

> and since \( {\int }_{0}^{+\infty }{v}^{1/2}{e}^{-v}{dv} \) converges, we deduce \( J\left( x\right) = {\int }_{0}^{4\sqrt{x}}{e}^{-v}/\sqrt{v}{dv} + O\left( {1/\sqrt{x}}\right) \) so \( J\left( x\right) \) converges to \( K = {\int }_{0}^{+\infty }{e}^{-v}{v}^{-1/2}{dv} \) as \( x \rightarrow + \infty \) . However, \( K = \Gamma \left( {1/2}\right) = \sqrt{\pi } \) (see question 2/d of study topic 1 on page 315), so finally, as \( x \rightarrow + \infty \) ,

\[
I\left( x\right)  = \frac{{e}^{2\sqrt{x}}}{2{x}^{1/4}}J\left( x\right)  \sim  \frac{{e}^{2\sqrt{x}}}{2{x}^{1/4}}\sqrt{\pi }\;\text{ d’où }\;f\left( x\right)  = \frac{I\left( x\right) }{\pi } \sim  \frac{1}{2\sqrt{\pi }}{x}^{-1/4}{e}^{2\sqrt{x}}.
\]

Problème 12. Soit \( \alpha > 0 \) . Donner un équivalent, lorsque \( n \rightarrow + \infty \) , de

> Problem 12. Let \( \alpha > 0 \) . Give an equivalent, as \( n \rightarrow + \infty \) , of

\[
{P}_{n}\left( \alpha \right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( \alpha n\right) }^{k}}{k!},\;\text{ et }\;{R}_{n}\left( \alpha \right)  = \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{{\left( \alpha n\right) }^{k}}{k!}.
\]

Solution. Remarquons que \( {P}_{n}\left( \alpha \right) + {R}_{n}\left( \alpha \right) = {e}^{\alpha n} \) .

> Solution. Note that \( {P}_{n}\left( \alpha \right) + {R}_{n}\left( \alpha \right) = {e}^{\alpha n} \) .

- Cas \( \alpha  > 1 \) . On écrit

> - Case \( \alpha  > 1 \) . We write

\[
{P}_{n}\left( \alpha \right)  = \frac{{\left( \alpha n\right) }^{n}}{n!}{A}_{n}\left( \alpha \right) ,\;\text{ avec }\;{A}_{n}\left( \alpha \right)  = 1 + \mathop{\sum }\limits_{{k = 1}}^{n}\frac{n\cdots \left( {n - k + 1}\right) }{{n}^{k}}\frac{1}{{\alpha }^{k}}.
\]

On écrit \( {A}_{n}\left( \alpha \right) \) sous la forme

> We write \( {A}_{n}\left( \alpha \right) \) in the form

\[
{A}_{n}\left( \alpha \right)  = 1 + \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k - 1}\left( n\right) \frac{1}{{\alpha }^{k}},\;\text{ où }\;{a}_{k}\left( n\right)  = \mathop{\prod }\limits_{{j = 1}}^{k}\left( {1 - j/n}\right) .
\]

Chaque \( {a}_{k}\left( n\right) \) converge vers1lorsque \( n \rightarrow + \infty \) , ce qui suggère que \( {A}_{n}\left( \alpha \right) \) converge vers \( \mathop{\sum }\limits_{{k \geq 0}}1/{\alpha }^{k} \) . Prouvons ce résultat. Soit \( \varepsilon > 0 \) . Fixons \( K \in \mathbb{N} \) tel que \( 1/{\alpha }^{K} < \varepsilon \) et \( N > K \) tel que \( {a}_{K}\left( N\right) > 1 - \varepsilon \) . Pour \( 0 \leq k \leq K \) et \( n \geq N \) , on a \( {a}_{k}\left( n\right) \geq {a}_{K}\left( N\right) > 1 - \varepsilon \) , donc

> Each \( {a}_{k}\left( n\right) \) converges to 1 as \( n \rightarrow + \infty \) , which suggests that \( {A}_{n}\left( \alpha \right) \) converges to \( \mathop{\sum }\limits_{{k \geq 0}}1/{\alpha }^{k} \) . Let us prove this result. Let \( \varepsilon > 0 \) . Fix \( K \in \mathbb{N} \) such that \( 1/{\alpha }^{K} < \varepsilon \) and \( N > K \) such that \( {a}_{K}\left( N\right) > 1 - \varepsilon \) . For \( 0 \leq k \leq K \) and \( n \geq N \) , we have \( {a}_{k}\left( n\right) \geq {a}_{K}\left( N\right) > 1 - \varepsilon \) , thus

\[
1 + \left( {1 - \varepsilon }\right) \frac{1 - 1/{\alpha }^{K + 1}}{1 - 1/\alpha } = 1 + \left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = 1}}^{K}\frac{1}{{\alpha }^{k}} < {A}_{n}\left( \alpha \right)  \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{{\alpha }^{k}}.
\]

On en déduit \( {\left( 1 - \varepsilon \right) }^{2}\frac{\alpha }{\alpha - 1} < {A}_{n}\left( \alpha \right) \leq \frac{\alpha }{\alpha - 1} \) , et ceci pour tout \( n \geq N \) . Donc \( {A}_{n}\left( \alpha \right) \) converge vers \( \alpha /\left( {\alpha - 1}\right) \) lorsque \( n \rightarrow \infty \) . Avec la formule de Stirling, on trouve

> We deduce \( {\left( 1 - \varepsilon \right) }^{2}\frac{\alpha }{\alpha - 1} < {A}_{n}\left( \alpha \right) \leq \frac{\alpha }{\alpha - 1} \) , and this for all \( n \geq N \) . Thus \( {A}_{n}\left( \alpha \right) \) converges to \( \alpha /\left( {\alpha - 1}\right) \) as \( n \rightarrow \infty \) . Using Stirling's formula, we find

\[
{P}_{n}\left( \alpha \right)  \sim  {\left( \alpha n\right) }^{n}{\left( \frac{e}{n}\right) }^{n}\frac{1}{\sqrt{2\pi n}}\frac{\alpha }{\alpha  - 1} = \frac{\alpha }{\alpha  - 1}\frac{{\left( \alpha e\right) }^{n}}{\sqrt{2\pi n}}\;\text{ et }\;{R}_{n}\left( \alpha \right)  = {e}^{\alpha n} - {P}_{n}\left( \alpha \right)  \sim  {e}^{\alpha n}.
\]

(on a utilisé l’inégalité \( {e}^{\alpha } \geq {\alpha e} \) , la fonction concave \( {e}^{x} \) étant au dessus de sa tangente en \( x = 1 \) ). - Cas \( \alpha < 1 \) . On écrit

> (we used the inequality \( {e}^{\alpha } \geq {\alpha e} \) , the concave function \( {e}^{x} \) being above its tangent at \( x = 1 \) ). - Case \( \alpha < 1 \) . We write

\[
{R}_{n}\left( \alpha \right)  = \frac{{\left( \alpha n\right) }^{n}}{n!}{B}_{n}\left( \alpha \right) ,\;\text{ avec }\;{B}_{n}\left( \alpha \right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{n}^{k}}{\left( {n + 1}\right) \cdots \left( {n + k}\right) }{\alpha }^{k}.
\]

On écrit \( {B}_{n}\left( \alpha \right) \) sous la forme

> We write \( {B}_{n}\left( \alpha \right) \) in the form

\[
{B}_{n}\left( \alpha \right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}{b}_{k}\left( n\right) {\alpha }^{k},\;\text{ où }\;{b}_{k}\left( n\right)  = \mathop{\prod }\limits_{{j = 1}}^{k}\frac{1}{1 + j/n}.
\]

On va montrer que \( {B}_{n}\left( \alpha \right) \) converge vers \( \mathop{\sum }\limits_{{k \geq 1}}{\alpha }^{k} \) . Soit \( \varepsilon > 0 \) . Fixons \( K \in \mathbb{N} \) tel que \( {\alpha }^{K} < \varepsilon \) , puis \( N \in \mathbb{N} \) tel que \( {b}_{K}\left( N\right) > 1 - \varepsilon \) . Pour \( 1 \leq \bar{k} \leq K \) et \( n \geq N \) , on a \( {b}_{k}\left( n\right) \geq {b}_{K}\left( N\right) > 1 - \varepsilon \) donc

> We will show that \( {B}_{n}\left( \alpha \right) \) converges to \( \mathop{\sum }\limits_{{k \geq 1}}{\alpha }^{k} \) . Let \( \varepsilon > 0 \) . Fix \( K \in \mathbb{N} \) such that \( {\alpha }^{K} < \varepsilon \) , then \( N \in \mathbb{N} \) such that \( {b}_{K}\left( N\right) > 1 - \varepsilon \) . For \( 1 \leq \bar{k} \leq K \) and \( n \geq N \) , we have \( {b}_{k}\left( n\right) \geq {b}_{K}\left( N\right) > 1 - \varepsilon \) thus

\[
{\left( 1 - \varepsilon \right) }^{2}\frac{\alpha }{1 - \alpha } \leq  \left( {1 - \varepsilon }\right) \frac{\alpha  - {\alpha }^{K + 1}}{1 - \alpha } = \left( {1 - \varepsilon }\right) \mathop{\sum }\limits_{{k = 1}}^{K}{\alpha }^{k} \leq  {B}_{n}\left( \alpha \right)  \leq  \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}{\alpha }^{k} = \frac{\alpha }{1 - \alpha }.
\]

Donc \( {B}_{n}\left( \alpha \right) \) converge vers \( \alpha /\left( {1 - \alpha }\right) \) . Avec la formule de Stirling, on en déduit

> Thus \( {B}_{n}\left( \alpha \right) \) converges to \( \alpha /\left( {1 - \alpha }\right) \) . Using Stirling's formula, we deduce

\[
{R}_{n}\left( \alpha \right)  \sim  {\left( \alpha n\right) }^{n}{\left( \frac{e}{n}\right) }^{n}\frac{1}{\sqrt{2\pi n}}\frac{\alpha }{1 - \alpha } = \frac{\alpha }{1 - \alpha }\frac{{\left( \alpha e\right) }^{n}}{\sqrt{2\pi n}}\text{ et }\;{P}_{n}\left( \alpha \right)  = {e}^{\alpha n} - {R}_{n}\left( \alpha \right)  \sim  {e}^{\alpha n}.
\]

- Cas \( \alpha  = 1 \) . C’est plus délicat. On va d’abord estimer \( {A}_{n}\left( 1\right)  - {B}_{n}\left( 1\right) \) ; pour cela, on coupe la somme sur \( k \) jusqu’a un entier \( m = \left\lbrack  {n}^{\lambda }\right\rbrack \) , où \( \lambda  \in  \rbrack 0,1\lbrack \) sera fixé plus tard \( (\left\lbrack  x\right\rbrack \) désigne la partie entière de \( x \) ). On écrit

> - Case \( \alpha  = 1 \) . This is more delicate. We will first estimate \( {A}_{n}\left( 1\right)  - {B}_{n}\left( 1\right) \) ; to do this, we split the sum over \( k \) up to an integer \( m = \left\lbrack  {n}^{\lambda }\right\rbrack \) , where \( \lambda  \in  \rbrack 0,1\lbrack \) will be fixed later \( (\left\lbrack  x\right\rbrack \) denotes the integer part of \( x \) ). We write

\[
{A}_{n}\left( 1\right)  - {B}_{n}\left( 1\right)  = 2 + {\alpha }_{n} + {\beta }_{n},\;\text{ avec }\;{\alpha }_{n} = \mathop{\sum }\limits_{{k = 1}}^{m}\left( {{a}_{k}\left( n\right)  - {b}_{k}\left( n\right) }\right) ,\;{\beta }_{n} = \mathop{\sum }\limits_{{k = m + 1}}^{{n - 1}}{a}_{k}\left( n\right)  - \mathop{\sum }\limits_{{k = m + 1}}^{{+\infty }}{b}_{k}\left( n\right) .
\]

On utilise maintenant la majoration \( \left| {\log \left( {1 + x}\right) - x}\right| \leq 2{x}^{2} \) sur \( \left\lbrack {-1/2,1/2}\right\rbrack \) (conséquence du developpement de Taylor-Young à l’ordre 2 appliqué à \( \log \left( {1 + x}\right) \) ). En notant \( {s}_{k}\left( n\right) = \mathop{\sum }\limits_{{j = 1}}^{k}j/n \) , elle entraîne, lorsque \( 0 \leq k \leq m \) (et \( n \) assez grand pour que \( m < n/2 \) , de sorte que \( k/n \leq 1/2 \) )

> We now use the upper bound \( \left| {\log \left( {1 + x}\right) - x}\right| \leq 2{x}^{2} \) on \( \left\lbrack {-1/2,1/2}\right\rbrack \) (a consequence of the Taylor-Young expansion to order 2 applied to \( \log \left( {1 + x}\right) \)). By denoting \( {s}_{k}\left( n\right) = \mathop{\sum }\limits_{{j = 1}}^{k}j/n \) , it implies, when \( 0 \leq k \leq m \) (and \( n \) is large enough so that \( m < n/2 \) , such that \( k/n \leq 1/2 \) )

\[
\log {a}_{k}\left( n\right)  = \mathop{\sum }\limits_{{j = 1}}^{k}\log \left( {1 - j/n}\right)  =  - {s}_{k}\left( n\right)  + {x}_{k}\left( n\right) ,\;\left| {{x}_{k}\left( n\right) }\right|  \leq  2\mathop{\sum }\limits_{{j = 1}}^{k}{\left( j/n\right) }^{2} \leq  2{m}^{3}/{n}^{2}
\]

\[
\log {b}_{k}\left( n\right)  =  - \mathop{\sum }\limits_{{j = 1}}^{k}\log \left( {1 + j/n}\right)  =  - {s}_{k}\left( n\right)  + {y}_{k}\left( n\right) ,\;\left| {{y}_{k}\left( n\right) }\right|  \leq  2\mathop{\sum }\limits_{{j = 1}}^{k}{\left( j/n\right) }^{2} \leq  2{m}^{3}/{n}^{2}.
\]

On a \( {m}^{3}/{n}^{2} \leq {n}^{{3\lambda } - 2} \) , on va donc choisir \( \lambda < 2/3 \) de sorte que \( {m}^{3}/{n}^{2} = o\left( 1\right) \) . Ceci assure l’existence d’une constante \( M > 0 \) telle que

> We have \( {m}^{3}/{n}^{2} \leq {n}^{{3\lambda } - 2} \) , so we will choose \( \lambda < 2/3 \) such that \( {m}^{3}/{n}^{2} = o\left( 1\right) \) . This ensures the existence of a constant \( M > 0 \) such that

\[
\left| {{a}_{k}\left( n\right)  - {b}_{k}\left( n\right) }\right|  = {a}_{k}\left( n\right) \left| {1 - \exp \left( {{y}_{k}\left( n\right)  - {x}_{k}\left( n\right) }\right) }\right|  \leq  M{a}_{k}\left( n\right) \left| {{y}_{k}\left( n\right)  - {x}_{k}\left( n\right) }\right|  \leq  {4M}{n}^{{3\lambda } - 2}{a}_{k}\left( n\right)
\]

donc

> therefore

\[
\left| {\alpha }_{n}\right|  \leq  {4M}{n}^{{3\lambda } - 2}{A}_{n}\left( 1\right) .
\]

Par ailleurs \( {a}_{k}\left( n\right) \leq {b}_{k}\left( n\right) \left( \right. \) car \( \left. {{a}_{k}\left( n\right) /{b}_{k}\left( n\right) = \mathop{\prod }\limits_{{1 \leq j \leq k}}\left( {1 - {j}^{2}/{n}^{2}}\right) \leq 1}\right) \) donc

> Furthermore \( {a}_{k}\left( n\right) \leq {b}_{k}\left( n\right) \left( \right. \) because \( \left. {{a}_{k}\left( n\right) /{b}_{k}\left( n\right) = \mathop{\prod }\limits_{{1 \leq j \leq k}}\left( {1 - {j}^{2}/{n}^{2}}\right) \leq 1}\right) \) therefore

\[
\left| {\beta }_{n}\right|  = \mathop{\sum }\limits_{{k = m + 1}}^{{n - 1}}\left( {{b}_{k}\left( n\right)  - {a}_{k}\left( n\right) }\right)  + \mathop{\sum }\limits_{{k = n}}^{{+\infty }}{b}_{k}\left( n\right)  \leq  \mathop{\sum }\limits_{{k = m + 1}}^{{+\infty }}{b}_{k}\left( n\right)  \leq  {b}_{m}\left( n\right) \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}{\left( \frac{1}{1 + m/n}\right) }^{k} \leq  {b}_{m}\left( n\right) \frac{n}{m}.
\]

Or

\[
{b}_{m}\left( n\right)  = {e}^{-{s}_{m}\left( n\right)  + {y}_{m}\left( n\right) } = O\left( {e}^{-{s}_{m}\left( n\right) }\right)  = O\left( {e}^{-m\left( {m + 1}\right) /\left( {2n}\right) }\right)  = O\left( {e}^{-{n}^{{2\lambda } - 1}/2}\right) .
\]

On choisit \( \lambda = \frac{1}{2}\left( {1/2 + 2/3}\right) = 7/{12} \) de sorte que \( {2\lambda } - 1 > 0 \) et \( \lambda < 2/3 \) . Avec ce choix de \( \lambda \) , les estimations précédentes deviennent

> We choose \( \lambda = \frac{1}{2}\left( {1/2 + 2/3}\right) = 7/{12} \) such that \( {2\lambda } - 1 > 0 \) and \( \lambda < 2/3 \) . With this choice of \( \lambda \) , the previous estimates become

\[
\left| {\alpha }_{n}\right|  \leq  {4M}{n}^{-1/4}{A}_{n}\left( 1\right) \;\text{ et }\left| {\beta }_{n}\right|  = O\left( {{e}^{-{n}^{1/6}/2}{n}^{5/{12}}}\right)  = o\left( 1\right) .
\]

Comme \( {A}_{n}\left( 1\right) \geq 1 \) on a \( {\beta }_{n} = o\left( {{A}_{n}\left( 1\right) }\right) \) , donc \( {A}_{n}\left( 1\right) - {B}_{n}\left( 1\right) = 2 + {\alpha }_{n} + {\beta }_{n} = 2 + o\left( {{A}_{n}\left( 1\right) }\right) \) . Ceci entraîne \( {P}_{n}\left( 1\right) - {R}_{n}\left( 1\right) = \left( {{n}^{n}/n!}\right) \left( {{A}_{n}\left( 1\right) - {B}_{n}\left( 1\right) }\right) = 2{n}^{n}/n! + o\left( {{P}_{n}\left( 1\right) }\right) = o\left( {e}^{n}\right) \) . Comme \( {P}_{n}\left( 1\right) + {R}_{n}\left( 1\right) = {e}^{n} \) on en déduit \( {P}_{n}\left( 1\right) \sim {R}_{n}\left( 1\right) \sim \frac{1}{2}{e}^{n} \) .

> Since \( {A}_{n}\left( 1\right) \geq 1 \) we have \( {\beta }_{n} = o\left( {{A}_{n}\left( 1\right) }\right) \) , therefore \( {A}_{n}\left( 1\right) - {B}_{n}\left( 1\right) = 2 + {\alpha }_{n} + {\beta }_{n} = 2 + o\left( {{A}_{n}\left( 1\right) }\right) \) . This implies \( {P}_{n}\left( 1\right) - {R}_{n}\left( 1\right) = \left( {{n}^{n}/n!}\right) \left( {{A}_{n}\left( 1\right) - {B}_{n}\left( 1\right) }\right) = 2{n}^{n}/n! + o\left( {{P}_{n}\left( 1\right) }\right) = o\left( {e}^{n}\right) \) . As \( {P}_{n}\left( 1\right) + {R}_{n}\left( 1\right) = {e}^{n} \) we deduce \( {P}_{n}\left( 1\right) \sim {R}_{n}\left( 1\right) \sim \frac{1}{2}{e}^{n} \) .

Problem 13. Soit \( \sum {a}_{n} \) une série complexe absolument convergence. On suppose que pour tout entier \( k \in {\mathbb{N}}^{ * },\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}^{k} = 0 \) . Montrer que la suite \( \left( {a}_{n}\right) \) est nulle.

> Problem 13. Let \( \sum {a}_{n} \) be an absolutely convergent complex series. Suppose that for every integer \( k \in {\mathbb{N}}^{ * },\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}^{k} = 0 \) . Show that the sequence \( \left( {a}_{n}\right) \) is zero.

Solution. On va raisonner par l’absurde en supposant que la suite \( \left( {a}_{n}\right) \) n’est pas nulle, de sorte que \( M = \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {a}_{n}\right| > 0 \) . Remarquons que \( \left( {a}_{n}\right) \) converge vers0(puisque \( \sum {a}_{n} \) converge) et donc si \( k \in {\mathbb{N}}^{ * } \) et pour \( n \) assez grand, \( {\left| {a}_{n}\right| }^{k} \leq \left| {a}_{n}\right| \) ce qui prouve que \( \sum {a}_{n}^{k} \) converge. Comme \( \left( {a}_{n}\right) \) tend vers 0, il existe \( {n}_{0} \in \mathbb{N} \) tel que \( \left| {a}_{n}\right| < M/2 \) pour \( n \geq {n}_{0} \) , donc il n’existe qu’un nombre fini de valeurs de \( {a}_{n} \) qui vérifient \( \left| {a}_{n}\right| \geq M/2 \) , on en déduit que \( I = \left\{ {n \in \mathbb{N}\left| \right| {a}_{n} \mid = M}\right\} \) est non vide. Quitte à diviser tous les termes de la suite \( \left( {a}_{n}\right) \) par \( M \) , on peut même supposer que \( M = 1 \) . On va mettre de coté les termes \( {a}_{n} \) pour \( n \notin I \) , en montrant que \( {S}_{k} = \mathop{\sum }\limits_{{n \notin I}}{a}_{n}^{k} \) tend vers 0. Soit \( \varepsilon > 0 \) ; on fixe \( {n}_{1} \geq {n}_{0} \) tel que \( \mathop{\sum }\limits_{{n > {n}_{1}}}\left| {a}_{n}\right| < \varepsilon \) . Soit \( q = \mathop{\sup }\limits_{{n \notin I, n \leq {n}_{1}}}\left| {a}_{n}\right| \) . Par définition de \( I \) , on a \( q < 1 \) . et on écrit

> Solution. We will reason by contradiction by assuming that the sequence \( \left( {a}_{n}\right) \) is not zero, such that \( M = \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {a}_{n}\right| > 0 \) . Note that \( \left( {a}_{n}\right) \) converges to 0 (since \( \sum {a}_{n} \) converges) and therefore if \( k \in {\mathbb{N}}^{ * } \) and for \( n \) large enough, \( {\left| {a}_{n}\right| }^{k} \leq \left| {a}_{n}\right| \) which proves that \( \sum {a}_{n}^{k} \) converges. As \( \left( {a}_{n}\right) \) tends to 0, there exists \( {n}_{0} \in \mathbb{N} \) such that \( \left| {a}_{n}\right| < M/2 \) for \( n \geq {n}_{0} \) , so there are only a finite number of values of \( {a}_{n} \) that satisfy \( \left| {a}_{n}\right| \geq M/2 \) , we deduce that \( I = \left\{ {n \in \mathbb{N}\left| \right| {a}_{n} \mid = M}\right\} \) is non-empty. By dividing all terms of the sequence \( \left( {a}_{n}\right) \) by \( M \) , we can even assume that \( M = 1 \) . We will set aside the terms \( {a}_{n} \) for \( n \notin I \) , by showing that \( {S}_{k} = \mathop{\sum }\limits_{{n \notin I}}{a}_{n}^{k} \) tends to 0. Let \( \varepsilon > 0 \) ; we fix \( {n}_{1} \geq {n}_{0} \) such that \( \mathop{\sum }\limits_{{n > {n}_{1}}}\left| {a}_{n}\right| < \varepsilon \) . Let \( q = \mathop{\sup }\limits_{{n \notin I, n \leq {n}_{1}}}\left| {a}_{n}\right| \) . By definition of \( I \) , we have \( q < 1 \) . and we write

\[
\left| {S}_{k}\right|  \leq  \mathop{\sum }\limits_{{n \notin  I, n \leq  {n}_{1}}}{\left| {a}_{n}\right| }^{k} + \mathop{\sum }\limits_{{n \geq  {n}_{1}}}\left| {a}_{n}\right|  \leq  {n}_{1}{q}^{k} + \varepsilon .
\]

Comme \( q < 1 \) on en déduit que \( \left| {S}_{k}\right| < {2\varepsilon } \) pour \( k \) suffisamment grand. On a donc bien montré que \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{S}_{k} = 0 \) . Comme \( {S}_{k} + \mathop{\sum }\limits_{{n \in I}}{a}_{n}^{k} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}^{k} = 0 \) , on en déduit que \( \mathop{\sum }\limits_{{n \in I}}{a}_{n}^{k} \) converge vers 0 lorsque \( k \) tend vers \( + \infty \) . En notant \( {z}_{1},\ldots ,{z}_{p} \) les valeurs distinctes de l’ensemble \( \left\{ {{a}_{n}, n \in I}\right\} \) (on a \( \left. {\left| {z}_{i}\right| = 1}\right) \) , et en notant \( {n}_{i} = \operatorname{Card}\left\{ {n \in I \mid {a}_{n} = {z}_{i}}\right\} \) , ceci s’écrit aussi \( \mathop{\lim }\limits_{{k \rightarrow + \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i}{z}_{i}^{k} = 0 \) . On utilise maintenant le résultat plus général suivant

> As \( q < 1 \) we deduce that \( \left| {S}_{k}\right| < {2\varepsilon } \) for \( k \) sufficiently large. We have thus clearly shown that \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{S}_{k} = 0 \) . As \( {S}_{k} + \mathop{\sum }\limits_{{n \in I}}{a}_{n}^{k} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}^{k} = 0 \) , we deduce that \( \mathop{\sum }\limits_{{n \in I}}{a}_{n}^{k} \) converges to 0 as \( k \) tends to \( + \infty \) . By denoting \( {z}_{1},\ldots ,{z}_{p} \) the distinct values of the set \( \left\{ {{a}_{n}, n \in I}\right\} \) (we have \( \left. {\left| {z}_{i}\right| = 1}\right) \) , and by denoting \( {n}_{i} = \operatorname{Card}\left\{ {n \in I \mid {a}_{n} = {z}_{i}}\right\} \) , this is also written \( \mathop{\lim }\limits_{{k \rightarrow + \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i}{z}_{i}^{k} = 0 \) . We now use the following more general result

LEMME 1. Soit \( {z}_{1},\ldots ,{z}_{p} \) des nombres complexes distincts tels que \( \left| {z}_{i}\right| = 1 \) pour tout i, et \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) des nombres complexes tels que \( \mathop{\lim }\limits_{{k \rightarrow \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{z}_{i}^{k} = 0 \) . Alors \( {\lambda }_{1} = \ldots = {\lambda }_{p} = 0 \) .

> LEMMA 1. Let \( {z}_{1},\ldots ,{z}_{p} \) be distinct complex numbers such that \( \left| {z}_{i}\right| = 1 \) for all i, and \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) be complex numbers such that \( \mathop{\lim }\limits_{{k \rightarrow \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{z}_{i}^{k} = 0 \) . Then \( {\lambda }_{1} = \ldots = {\lambda }_{p} = 0 \) .

Prouvons ce résultat intermédiaire par récurrence sur \( p \) . Pour \( p = 1 \) c’est immédiat car \( \left| {z}_{1}\right| = \) 1. Supposons le résultat vrai au rang \( p - 1 \) et montrons le au rang \( p \) . Notons \( {u}_{k} = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{z}_{i}^{k} \) . Comme \( \left( {u}_{k}\right) \) tend vers \( 0,{u}_{k + 1} - {z}_{p}{u}_{k} \) tend également vers 0 lorsque \( k \rightarrow \infty \) . Or \( {u}_{k + 1} - {z}_{p}{u}_{k} = \; \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}\left( {{\lambda }_{i}{z}_{i} - {\lambda }_{i}{z}_{p}}\right) {z}_{i}^{k} \) . D’après l’hypothèse de récurrence, on a donc \( 0 = {\lambda }_{i}{z}_{i} - {\lambda }_{i}{z}_{p} = {\lambda }_{i}\left( {{z}_{i} - {z}_{p}}\right) \) pour tout \( i < p \) , et comme les \( {z}_{i} \) sont distincts ceci entraîne \( {\lambda }_{i} = 0 \) pour \( i < p \) . On a donc \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{\lambda }_{p}{z}_{p}^{k} = 0 \) et comme \( \left| {z}_{p}\right| = 1 \) ceci entraîne également \( {\lambda }_{p} = 0 \) . On a donc prouvé le lemme.

> Let us prove this intermediate result by induction on \( p \) . For \( p = 1 \) it is immediate since \( \left| {z}_{1}\right| = \) 1. Assume the result is true at rank \( p - 1 \) and let us show it at rank \( p \) . Let \( {u}_{k} = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}{z}_{i}^{k} \) . As \( \left( {u}_{k}\right) \) tends to \( 0,{u}_{k + 1} - {z}_{p}{u}_{k} \) also tends to 0 as \( k \rightarrow \infty \) . Now \( {u}_{k + 1} - {z}_{p}{u}_{k} = \; \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}\left( {{\lambda }_{i}{z}_{i} - {\lambda }_{i}{z}_{p}}\right) {z}_{i}^{k} \) . According to the induction hypothesis, we therefore have \( 0 = {\lambda }_{i}{z}_{i} - {\lambda }_{i}{z}_{p} = {\lambda }_{i}\left( {{z}_{i} - {z}_{p}}\right) \) for all \( i < p \) , and since the \( {z}_{i} \) are distinct this implies \( {\lambda }_{i} = 0 \) for \( i < p \) . We therefore have \( \mathop{\lim }\limits_{{k \rightarrow \infty }}{\lambda }_{p}{z}_{p}^{k} = 0 \) and since \( \left| {z}_{p}\right| = 1 \) this also implies \( {\lambda }_{p} = 0 \) . We have thus proven the lemma.

Le résultat de l’exercice découle du lemme : comme \( \mathop{\lim }\limits_{{k \rightarrow + \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i}{z}_{i}^{k} = 0 \) , on a forcément les \( {n}_{i} \) nuls, ce qui est impossible puisque par construction, les \( {n}_{i} \) sont des entiers naturels non nuls. On a donc aboutit à une contraction, donc la suite \( \left( {a}_{n}\right) \) est nulle.

> The result of the exercise follows from the lemma: as \( \mathop{\lim }\limits_{{k \rightarrow + \infty }}\mathop{\sum }\limits_{{i = 1}}^{p}{n}_{i}{z}_{i}^{k} = 0 \) , we necessarily have the \( {n}_{i} \) equal to zero, which is impossible since by construction, the \( {n}_{i} \) are non-zero natural integers. We have therefore reached a contradiction, so the sequence \( \left( {a}_{n}\right) \) is zero.

Problem 14. a) Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue et \( {a}_{1},\ldots ,{a}_{n} \) des points distincts de \( \left\lbrack {0,1}\right\rbrack \) . Montrer qu’il existe une suite de polynômes \( \left( {P}_{k}\right) \) qui converge uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) et telle que pour tout \( k,{P}_{k} \) prend les mêmes valeurs que \( f \) aux points \( {a}_{1},\ldots ,{a}_{n} \) (on pourra utiliser le théorème de Weierstrass, voir page 235).

> Problem 14. a) Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a continuous function and \( {a}_{1},\ldots ,{a}_{n} \) be distinct points of \( \left\lbrack {0,1}\right\rbrack \) . Show that there exists a sequence of polynomials \( \left( {P}_{k}\right) \) that converges uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \) and such that for all \( k,{P}_{k} \) takes the same values as \( f \) at the points \( {a}_{1},\ldots ,{a}_{n} \) (one may use the Weierstrass theorem, see page 235).

b) Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une fonction continue qui ne s’annule qu’un nombre fini de fois sur \( \left\lbrack {0,1}\right\rbrack \) . Existe t-il une suite de polynômes \( \left( {P}_{k}\right) \) qui converge uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) et telle que pour tout \( k,{P}_{k} \) a les mêmes zéros que \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) ?

> b) Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a continuous function that vanishes only a finite number of times on \( \left\lbrack {0,1}\right\rbrack \). Does there exist a sequence of polynomials \( \left( {P}_{k}\right) \) that converges uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \) and such that for all \( k,{P}_{k} \) it has the same zeros as \( f \) on \( \left\lbrack {0,1}\right\rbrack \)?

Solution. a) D’après le théorème de Weierstrass, il existe une suite de polynômes \( \left( {Q}_{k}\right) \) qui converge uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) . L’idée est de perturber légèrement les \( {Q}_{k} \) pour que ceux ci prennent les mêmes valeurs que \( f \) sur les points \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) . Pour celà on considère les polynômes d'interpolation de Lagrange (voir le tome Algèbre) définis par

> Solution. a) According to the Weierstrass theorem, there exists a sequence of polynomials \( \left( {Q}_{k}\right) \) that converges uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \). The idea is to slightly perturb the \( {Q}_{k} \) so that they take the same values as \( f \) at the points \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \). To do this, we consider the Lagrange interpolation polynomials (see the Algebra volume) defined by

\[
{L}_{i}\left( x\right)  = \mathop{\prod }\limits_{{j \neq  i}}\frac{x - {a}_{j}}{{a}_{i} - {a}_{j}}.
\]

Ils vérifient \( {L}_{i}\left( {x}_{j}\right) = 0 \) si \( i \neq j,{L}_{i}\left( {x}_{i}\right) = 1 \) . Pour tout \( k \) , on définit maintenant \( {P}_{k}\left( x\right) = \; {Q}_{k}\left( x\right) + \mathop{\sum }\limits_{{i = 1}}^{n}\left( {f\left( {a}_{i}\right) - {Q}_{k}\left( {a}_{i}\right) }\right) {L}_{i}\left( x\right) \) . La fonction \( {P}_{k} \) est un polynôme qui prend les mêmes valeurs que \( f \) sur les points \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) , et en utilisant la notation de la norme de la convergence uniforme \( \parallel g{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {g\left( x\right) }\right| \) pour toute fonction réelle continue \( g \) sur \( \left\lbrack {0,1}\right\rbrack \) , on a

> They satisfy \( {L}_{i}\left( {x}_{j}\right) = 0 \) if \( i \neq j,{L}_{i}\left( {x}_{i}\right) = 1 \). For all \( k \), we now define \( {P}_{k}\left( x\right) = \; {Q}_{k}\left( x\right) + \mathop{\sum }\limits_{{i = 1}}^{n}\left( {f\left( {a}_{i}\right) - {Q}_{k}\left( {a}_{i}\right) }\right) {L}_{i}\left( x\right) \). The function \( {P}_{k} \) is a polynomial that takes the same values as \( f \) at the points \( {\left( {a}_{i}\right) }_{1 \leq i \leq n} \), and using the notation for the uniform convergence norm \( \parallel g{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {g\left( x\right) }\right| \) for any continuous real function \( g \) on \( \left\lbrack {0,1}\right\rbrack \), we have

\[
{\begin{Vmatrix}f - {P}_{k}\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}f - {Q}_{k}\end{Vmatrix}}_{\infty } + \mathop{\sum }\limits_{{i = 1}}^{n}\left| {f\left( {a}_{i}\right)  - {Q}_{k}\left( {a}_{i}\right) }\right|  \cdot  {\begin{Vmatrix}{L}_{i}\end{Vmatrix}}_{\infty } \leq  M{\begin{Vmatrix}f - {Q}_{k}\end{Vmatrix}}_{\infty },\;M = 1 + \mathop{\sum }\limits_{{i = 1}}^{n}{\begin{Vmatrix}{L}_{i}\end{Vmatrix}}_{\infty }.
\]

Comme \( {\begin{Vmatrix}f - {Q}_{k}\end{Vmatrix}}_{\infty } \) converge vers 0 on en déduit que \( {\begin{Vmatrix}f - {P}_{k}\end{Vmatrix}}_{\infty } \) également, d’où le résultat.

> Since \( {\begin{Vmatrix}f - {Q}_{k}\end{Vmatrix}}_{\infty } \) converges to 0, we deduce that \( {\begin{Vmatrix}f - {P}_{k}\end{Vmatrix}}_{\infty } \) does as well, hence the result.

b) La réponse est oui! Si \( f \) ne s’annule pas il suffit d’approcher \( f \) par une suite de polynômes \( \left( {P}_{k}\right) \) et de remarquer que les \( {P}_{k} \) ne s’annulent pas sur \( \left\lbrack {0,1}\right\rbrack \) à partir d’un certain rang (dès que \( {\begin{Vmatrix}{P}_{k} - f\end{Vmatrix}}_{\infty } < \mathop{\min }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {f\left( x\right) }\right| \) ). Si \( f \) s’annule on ne peut pas se contenter d’appliquer le résultat de la question précédentes aux zéros de \( f \) , car il faut s’assurer que les \( {P}_{k} \) n’ont pas d’autres zéros que ceux de \( f \) .

> b) The answer is yes! If \( f \) does not vanish, it suffices to approximate \( f \) by a sequence of polynomials \( \left( {P}_{k}\right) \) and note that the \( {P}_{k} \) do not vanish on \( \left\lbrack {0,1}\right\rbrack \) beyond a certain rank (as soon as \( {\begin{Vmatrix}{P}_{k} - f\end{Vmatrix}}_{\infty } < \mathop{\min }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {f\left( x\right) }\right| \)). If \( f \) vanishes, we cannot simply apply the result of the previous question to the zeros of \( f \), because we must ensure that the \( {P}_{k} \) have no other zeros than those of \( f \).

On va s’en sortir en approchant \( f \) par une suite de fonctions \( \left( {g}_{k}\right) \) qui s’écrivent sous la forme \( {g}_{k} = P{h}_{k} \) , avec \( P \) un polynôme fixé qui a les même zéros que \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) et les \( {h}_{k} \) continues ne s’annulant pas sur \( \left\lbrack {0,1}\right\rbrack \) , puis en approchant \( {h}_{k} \) par un polynôme ne s’annulant pas sur \( \left\lbrack {0,1}\right\rbrack \) .

> We will manage this by approximating \( f \) with a sequence of functions \( \left( {g}_{k}\right) \) written in the form \( {g}_{k} = P{h}_{k} \), where \( P \) is a fixed polynomial having the same zeros as \( f \) on \( \left\lbrack {0,1}\right\rbrack \) and the \( {h}_{k} \) are continuous and non-vanishing on \( \left\lbrack {0,1}\right\rbrack \), then by approximating \( {h}_{k} \) with a polynomial that does not vanish on \( \left\lbrack {0,1}\right\rbrack \).

Pour cela on va choisir \( {g}_{k} \) localement polynomiale au voisinage de chaque zéro de \( f \) . Plus précisément, notons \( {a}_{1},\ldots ,{a}_{n} \) les zéros de \( f \) . Pour tout \( i \) , notons \( {m}_{i} = 1 \) si \( f \) change de signe au voisinage de \( {a}_{i},{m}_{i} = 2 \) sinon. On choisit pour \( P \) le polynôme \( P = \mathop{\prod }\limits_{{i = 1}}^{n}{\left( x - {a}_{i}\right) }^{{m}_{i}} \) , de sorte que \( {fP} \) garde un signe constant sur \( \left\lbrack {0,1}\right\rbrack \) . Soit \( k \in {\mathbb{N}}^{ * } \) . Soit \( \delta > 0 \) suffisamment petit tel que les segments \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} + \delta }\right\rbrack \) soient deux à deux disjoints et tels que \( \left| f\right| < 1/k \) sur ces segments. On définit la fonction \( {g}_{k} \) par \( {g}_{k}\left( x\right) = f\left( x\right) \) lorsque \( x \) n’est pas dans l’un des segments \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} + \delta }\right\rbrack \) , et sur chacun de ces segments on définit \( {g}_{k} \) affine sur \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} - \delta /2}\right\rbrack \) et sur \( \left\lbrack {{a}_{i} + \delta /2,{a}_{i} + \delta }\right\rbrack \) de sorte que

> To do this, we will choose \( {g}_{k} \) to be locally polynomial in the neighborhood of each zero of \( f \). More precisely, let \( {a}_{1},\ldots ,{a}_{n} \) denote the zeros of \( f \). For any \( i \), let \( {m}_{i} = 1 \) if \( f \) changes sign in the neighborhood of \( {a}_{i},{m}_{i} = 2 \), otherwise. We choose for \( P \) the polynomial \( P = \mathop{\prod }\limits_{{i = 1}}^{n}{\left( x - {a}_{i}\right) }^{{m}_{i}} \), so that \( {fP} \) maintains a constant sign on \( \left\lbrack {0,1}\right\rbrack \). Let \( k \in {\mathbb{N}}^{ * } \). Let \( \delta > 0 \) be sufficiently small such that the segments \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} + \delta }\right\rbrack \) are pairwise disjoint and such that \( \left| f\right| < 1/k \) on these segments. We define the function \( {g}_{k} \) by \( {g}_{k}\left( x\right) = f\left( x\right) \) when \( x \) is not in one of the segments \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} + \delta }\right\rbrack \), and on each of these segments we define \( {g}_{k} \) to be affine on \( \left\lbrack {{a}_{i} - \delta ,{a}_{i} - \delta /2}\right\rbrack \) and on \( \left\lbrack {{a}_{i} + \delta /2,{a}_{i} + \delta }\right\rbrack \) such that

\[
\left\{  {\begin{array}{ll} {g}_{k}\left( {{a}_{i} - \delta }\right) &  = f\left( {{a}_{i} - \delta }\right) , \\  {g}_{k}\left( {{a}_{i} - \delta /2}\right) &  = {\varepsilon }_{i}/k \end{array}\;\text{ et }\left\{  \begin{array}{ll} {g}_{k}\left( {{a}_{i} + \delta /2}\right) &  = {\varepsilon }_{i}^{\prime }/k, \\  {g}_{k}\left( {{a}_{i} + \delta }\right) &  = f\left( {{a}_{i} + \delta }\right)  \end{array}\right. }\right.
\]

(où \( {\varepsilon }_{i} = f\left( {{a}_{i} - \delta }\right) /\left| {f\left( {{a}_{i} - \delta }\right) }\right| \in \{ - 1,1\} \) a le signe de \( f\left( {{a}_{i} - \delta }\right) \) et \( {\varepsilon }_{i}^{\prime } = f\left( {{a}_{i} + \delta }\right) /\left| {f\left( {{a}_{i} + \delta }\right) }\right| \in \{ - 1,1\} \) a le signe de \( f\left( {{a}_{i} + \delta }\right) \) ). On définit ensuite, pour tout \( i \)

> (where \( {\varepsilon }_{i} = f\left( {{a}_{i} - \delta }\right) /\left| {f\left( {{a}_{i} - \delta }\right) }\right| \in \{ - 1,1\} \) has the sign of \( f\left( {{a}_{i} - \delta }\right) \) and \( {\varepsilon }_{i}^{\prime } = f\left( {{a}_{i} + \delta }\right) /\left| {f\left( {{a}_{i} + \delta }\right) }\right| \in \{ - 1,1\} \) has the sign of \( f\left( {{a}_{i} + \delta }\right) \)). We then define, for all \( i \)

\[
\forall x \in  \rbrack {a}_{i} - \delta /2,{a}_{i} + \delta /2\left\lbrack  \right. ,\;{g}_{k}\left( x\right)  = \frac{{\left( x - {a}_{i}\right) }^{{m}_{i}}}{{\left( \delta /2\right) }^{{m}_{i}}}\frac{{\varepsilon }_{i}^{\prime }}{k}.
\]

Ainsi \( g \) est définie sur \( \left\lbrack {0,1}\right\rbrack \) , continue sur cet intervalle, a les mêmes zéros que \( f \) et de plus \( {\begin{Vmatrix}f - {g}_{k}\end{Vmatrix}}_{\infty } < 1/k \) . On définit maintenant \( {h}_{k}\left( x\right) = {g}_{k}\left( x\right) /P\left( x\right) \) si \( x \notin \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \) et \( {h}_{k}\left( {a}_{i}\right) = \; {\varepsilon }_{i}^{\prime }/\left( {k{\left( \delta /2\right) }^{{m}_{i}}}\right) \) . Ainsi définie, \( {h}_{k} \) est une fonction continue qui ne s’annule pas sur \( \left\lbrack {0,1}\right\rbrack \) et qui verifie \( {g}_{k} = P{h}_{k} \) . Comme on l’a vu au début de la solution de cette question, on peut donc trouver un polynôme \( {Q}_{k} \) ne s’annulant pas sur \( \left\lbrack {0,1}\right\rbrack \) tel que \( \begin{Vmatrix}{{h}_{k} - {Q}_{k}}\end{Vmatrix} \leq 1/k \) .

> Thus \( g \) is defined on \( \left\lbrack {0,1}\right\rbrack \), continuous on this interval, has the same zeros as \( f \), and furthermore \( {\begin{Vmatrix}f - {g}_{k}\end{Vmatrix}}_{\infty } < 1/k \). We now define \( {h}_{k}\left( x\right) = {g}_{k}\left( x\right) /P\left( x\right) \) if \( x \notin \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \) and \( {h}_{k}\left( {a}_{i}\right) = \; {\varepsilon }_{i}^{\prime }/\left( {k{\left( \delta /2\right) }^{{m}_{i}}}\right) \). As defined, \( {h}_{k} \) is a continuous function that does not vanish on \( \left\lbrack {0,1}\right\rbrack \) and satisfies \( {g}_{k} = P{h}_{k} \). As seen at the beginning of the solution to this question, we can therefore find a polynomial \( {Q}_{k} \) that does not vanish on \( \left\lbrack {0,1}\right\rbrack \) such that \( \begin{Vmatrix}{{h}_{k} - {Q}_{k}}\end{Vmatrix} \leq 1/k \).

\[
{\begin{Vmatrix}f - P{Q}_{k}\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}f - P{h}_{k}\end{Vmatrix}}_{\infty } + {\begin{Vmatrix}P{h}_{k} - P{Q}_{k}\end{Vmatrix}}_{\infty } \leq  {\begin{Vmatrix}f - {g}_{k}\end{Vmatrix}}_{\infty } + \parallel P{\parallel }_{\infty } \cdot  {\begin{Vmatrix}{Q}_{k} - {h}_{k}\end{Vmatrix}}_{\infty } \leq  \frac{1 + \parallel P{\parallel }_{\infty }}{k}.
\]

Ainsi, les \( {P}_{k} = P{Q}_{k} \) sont des polynômes qui convergent uniformément vers \( f \) sur \( \left\lbrack {0,1}\right\rbrack \) et qui ont les mêmes zéros que \( f \) .

> Thus, the \( {P}_{k} = P{Q}_{k} \) are polynomials that converge uniformly to \( f \) on \( \left\lbrack {0,1}\right\rbrack \) and have the same zeros as \( f \).

Problem 15. Pour tout entier naturel \( n \) , on note \( {\nu }_{2}\left( n\right) \) le nombre de "1" dans l'écriture binaire de \( n \) . Montrer que la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } \) converge et calculer sa somme.

> Problem 15. For any natural number \( n \), let \( {\nu }_{2}\left( n\right) \) be the number of "1"s in the binary representation of \( n \). Show that the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } \) converges and calculate its sum.

Solution. Soit \( n \in {\mathbb{N}}^{ * } \) et \( n = \mathop{\sum }\limits_{{k = 0}}^{p}{\varepsilon }_{k}{2}^{k} \) son écriture binaire \( \left( {{\varepsilon }_{k} \in \{ 0,1\} }\right. \) pour tout \( k \) et \( \left. {{\varepsilon }_{p} = 1}\right) \) . On a \( \nu \left( n\right) = \mathop{\sum }\limits_{{k = 0}}^{p}{\varepsilon }_{k} \leq p + 1 \) . Par ailleurs, \( {2}^{p} = {\varepsilon }_{p}{2}^{p} \leq n \) donc \( p \leq {\log }_{2}n \) , donc finalement \( {\nu }_{2}\left( n\right) \leq 1 + {\log }_{2}n \) . Comme \( 1 + {\log }_{2}n = O\left( \sqrt{n}\right) \) lorsque \( n \rightarrow + \infty \) , on en déduit \( {\nu }_{2}\left( n\right) = O\left( \sqrt{n}\right) \) , donc \( \frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } = O\left( {n}^{-3/2}\right) \) . La série à termes positifs \( \sum \frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } \) est donc convergente.

> Solution. Let \( n \in {\mathbb{N}}^{ * } \) and \( n = \mathop{\sum }\limits_{{k = 0}}^{p}{\varepsilon }_{k}{2}^{k} \) be its binary representation \( \left( {{\varepsilon }_{k} \in \{ 0,1\} }\right. \) for all \( k \) and \( \left. {{\varepsilon }_{p} = 1}\right) \). We have \( \nu \left( n\right) = \mathop{\sum }\limits_{{k = 0}}^{p}{\varepsilon }_{k} \leq p + 1 \). Furthermore, \( {2}^{p} = {\varepsilon }_{p}{2}^{p} \leq n \) so \( p \leq {\log }_{2}n \), and finally \( {\nu }_{2}\left( n\right) \leq 1 + {\log }_{2}n \). Since \( 1 + {\log }_{2}n = O\left( \sqrt{n}\right) \) as \( n \rightarrow + \infty \), we deduce \( {\nu }_{2}\left( n\right) = O\left( \sqrt{n}\right) \), so \( \frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } = O\left( {n}^{-3/2}\right) \). The series with positive terms \( \sum \frac{{\nu }_{2}\left( n\right) }{n\left( {n + 1}\right) } \) is therefore convergent.

Pour calculer sa somme \( S \) , on remarque que pour tout entier naturel \( n,{\nu }_{2}\left( {2n}\right) = {\nu }_{2}\left( n\right) \) et \( {\nu }_{2}\left( {{2n} + 1}\right) = {\nu }_{2}\left( n\right) + 1 \) . En séparant les termes pairs et impairs de la série, ceci entraîne

> To calculate its sum \( S \), we note that for any natural integer \( n,{\nu }_{2}\left( {2n}\right) = {\nu }_{2}\left( n\right) \) and \( {\nu }_{2}\left( {{2n} + 1}\right) = {\nu }_{2}\left( n\right) + 1 \). By separating the even and odd terms of the series, this leads to

\[
S = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\nu }_{2}\left( {2n}\right) }{{2n}\left( {{2n} + 1}\right) } + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\nu }_{2}\left( {{2n} + 1}\right) }{\left( {{2n} + 1}\right) \left( {{2n} + 2}\right) } = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\nu }_{2}\left( n\right) }{{2n}\left( {{2n} + 1}\right) } + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\nu }_{2}\left( n\right)  + 1}{\left( {{2n} + 1}\right) \left( {{2n} + 2}\right) }
\]

\[
= \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\nu }_{2}\left( n\right) \left( {\frac{1}{{2n}\left( {{2n} + 1}\right) } + \frac{1}{\left( {{2n} + 1}\right) \left( {{2n} + 2}\right) }}\right)  + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{\left( {{2n} + 1}\right) \left( {{2n} + 2}\right) }
\]

\[
= \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{2{\nu }_{2}\left( n\right) }{{2n}\left( {{2n} + 2}\right) } + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\frac{1}{{2n} + 1} - \frac{1}{{2n} + 2}}\right)  = \frac{S}{2} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n - 1}}{n}.
\]

Il est bien connu que \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n - 1}}{n} = \log 2 \) (voir par exemple la remarque de l’exercice 10 page 263), donc finalement, on a \( S = S/2 + \log 2 \) , donc \( S = 2\log 2 \) .

> It is well known that \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\left( -1\right) }^{n - 1}}{n} = \log 2 \) (see for example the remark in exercise 10 on page 263), so finally, we have \( S = S/2 + \log 2 \), thus \( S = 2\log 2 \).

Problem 16 (THÉORÉME DE RÉALISATION DE BOREL). Soit \( {\left( {a}_{n}\right) }_{n \in \mathbb{N}} \) une suite com-plexe quelconque.

> Problem 16 (BOREL'S REALIZATION THEOREM). Let \( {\left( {a}_{n}\right) }_{n \in \mathbb{N}} \) be any complex sequence.

Soit \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{\infty } \) telle que \( \varphi \left( x\right) = 1 \) pour \( x \in \left\lbrack {-1,1}\right\rbrack \) et \( \varphi \left( x\right) = 0 \) pour \( \left| x\right| \geq 2 \) (une fonction de ce type est construite dans l’exercice 3 page 79). On pose \( {\varphi }_{n}\left( x\right) = {x}^{n}\varphi \left( x\right) \) , on note \( {M}_{n} \) un majorant de \( \left| {\varphi }_{n}\right| ,\left| {\varphi }_{n}^{\prime }\right| ,\ldots ,\left| {\varphi }_{n}^{\left( n - 1\right) }\right| \) sur \( \mathbb{R} \) , et on choisit une suite réelle \( {\left( {\lambda }_{n}\right) }_{n \in \mathbb{N}} \) vérifiant \( {\lambda }_{n} \geq 1 \) pour \( n \in \mathbb{N} \) , tendant vers \( + \infty \) , et telle que \( \sum \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) converge.

> Let \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{\infty } \) class mapping such that \( \varphi \left( x\right) = 1 \) for \( x \in \left\lbrack {-1,1}\right\rbrack \) and \( \varphi \left( x\right) = 0 \) for \( \left| x\right| \geq 2 \) (a function of this type is constructed in exercise 3 on page 79). We set \( {\varphi }_{n}\left( x\right) = {x}^{n}\varphi \left( x\right) \), we denote by \( {M}_{n} \) an upper bound of \( \left| {\varphi }_{n}\right| ,\left| {\varphi }_{n}^{\prime }\right| ,\ldots ,\left| {\varphi }_{n}^{\left( n - 1\right) }\right| \) on \( \mathbb{R} \), and we choose a real sequence \( {\left( {\lambda }_{n}\right) }_{n \in \mathbb{N}} \) satisfying \( {\lambda }_{n} \geq 1 \) for \( n \in \mathbb{N} \), tending to \( + \infty \), and such that \( \sum \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) converges.

Montrer que la fonction \( f : x \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n}\varphi \left( {{\lambda }_{n}x}\right) \) est bien définie, de classe \( {\mathcal{C}}^{\infty } \) sur \( \mathbb{R} \) et vérifie \( {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) pour tout \( n \in \mathbb{N} \) .

> Show that the function \( f : x \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n}\varphi \left( {{\lambda }_{n}x}\right) \) is well-defined, of class \( {\mathcal{C}}^{\infty } \) on \( \mathbb{R} \) and satisfies \( {f}^{\left( n\right) }\left( 0\right) /n! = {a}_{n} \) for all \( n \in \mathbb{N} \) .

Solution. Notons d’abord que \( {M}_{n} \) existe bien car \( {\varphi }_{n} \) est à support compact, et qu’on peut choisir par exemple \( {\lambda }_{n} = 1 + {n}^{2}\left( {1 + \left| {a}_{n}\right| {M}_{n}}\right) \) . La fonction \( f \) est bien définie en \( x = 0 \) , et pour \( x \neq 0 \) également car les termes de la série sont nuls à partir d’un certain rang (dès que \( \left. {\left| {{\lambda }_{n}x}\right| > 2}\right) \) .

> Solution. First note that \( {M}_{n} \) exists because \( {\varphi }_{n} \) has compact support, and one can choose for example \( {\lambda }_{n} = 1 + {n}^{2}\left( {1 + \left| {a}_{n}\right| {M}_{n}}\right) \) . The function \( f \) is well-defined at \( x = 0 \) , and for \( x \neq 0 \) as well because the terms of the series are zero from a certain rank onwards (as soon as \( \left. {\left| {{\lambda }_{n}x}\right| > 2}\right) \) .

Montrons maintenant par récurrence sur \( p \in \mathbb{N} \) que \( f \) est de classe \( {\mathcal{C}}^{p} \) sur \( \mathbb{R} \) et que

> Let us now show by induction on \( p \in \mathbb{N} \) that \( f \) is of class \( {\mathcal{C}}^{p} \) on \( \mathbb{R} \) and that

\[
{f}^{\left( p\right) }\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{\lambda }_{n}^{p - n}{\varphi }_{n}^{\left( p\right) }\left( {{\lambda }_{n}x}\right) .
\]

(*)

> Pour \( p = 0 \) , l’écriture (*) découle de la définition de \( {\varphi }_{n} \) , et la série (*) converge normalement car pour \( n \geq 1,\left| {{a}_{n}{\lambda }_{n}^{-n}{\varphi }_{n}\left( {{\lambda }_{n}x}\right) }\right| \leq \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) , d’où la continuité de \( f \) sur \( \mathbb{R} \) . Supposons maintenant le résultat vrai au rang \( p \) et montrons le au rang \( p + 1 \) . La série des termes dérivés de (*) \( \sum {a}_{n}{\lambda }_{n}^{p + 1 - n}{\varphi }_{n}^{\left( p + 1\right) }\left( {{\lambda }_{n}x}\right) \) converge bien normalement car pour \( n \geq p + 2 \) , on a la majoration \( \left| {{a}_{n}{\lambda }_{n}^{p + 1 - n}{\varphi }_{n}^{\left( p + 1\right) }\left( {{\lambda }_{n}x}\right) }\right| \leq \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) . On en déduit que \( {f}^{\left( p\right) } \) est de classe \( {\mathcal{C}}^{1} \) (donc \( f \) de classe \( \left. {\mathcal{C}}^{p + 1}\right) \) et que la formule (*) est bien vraie au rang \( p + 1 \) .

For \( p = 0 \) , the expression (*) follows from the definition of \( {\varphi }_{n} \) , and the series (*) converges normally because for \( n \geq 1,\left| {{a}_{n}{\lambda }_{n}^{-n}{\varphi }_{n}\left( {{\lambda }_{n}x}\right) }\right| \leq \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) , hence the continuity of \( f \) on \( \mathbb{R} \) . Now assume the result is true at rank \( p \) and show it at rank \( p + 1 \) . The series of derived terms of (*) \( \sum {a}_{n}{\lambda }_{n}^{p + 1 - n}{\varphi }_{n}^{\left( p + 1\right) }\left( {{\lambda }_{n}x}\right) \) converges normally because for \( n \geq p + 2 \) , we have the bound \( \left| {{a}_{n}{\lambda }_{n}^{p + 1 - n}{\varphi }_{n}^{\left( p + 1\right) }\left( {{\lambda }_{n}x}\right) }\right| \leq \left| {a}_{n}\right| {M}_{n}/{\lambda }_{n} \) . We deduce that \( {f}^{\left( p\right) } \) is of class \( {\mathcal{C}}^{1} \) (thus \( f \) is of class \( \left. {\mathcal{C}}^{p + 1}\right) \) ) and that the formula (*) is indeed true at rank \( p + 1 \) .

> Il suffit maintenant de remarquer que \( {\varphi }_{n}\left( x\right) = {x}^{n} \) pour \( x \in \left\lbrack {-1,1}\right\rbrack \) donc \( {\varphi }_{p}^{\left( p\right) }\left( 0\right) = p \) ! et \( {\varphi }_{n}^{\left( p\right) }\left( 0\right) = 0 \) si \( n \neq p \) . Avec la formule (*), on en déduit que \( {f}^{\left( p\right) }\left( 0\right) = p!{a}_{p} \) .

It suffices now to note that \( {\varphi }_{n}\left( x\right) = {x}^{n} \) for \( x \in \left\lbrack {-1,1}\right\rbrack \) so \( {\varphi }_{p}^{\left( p\right) }\left( 0\right) = p \) ! and \( {\varphi }_{n}^{\left( p\right) }\left( 0\right) = 0 \) if \( n \neq p \) . With the formula (*), we deduce that \( {f}^{\left( p\right) }\left( 0\right) = p!{a}_{p} \) .

> Problem 17. Soit \( {\left( {a}_{n}\right) }_{n \in \mathbb{N}} \) une suite strictement croissante d’entiers, avec \( {a}_{0} > 0 \) . Pour tout \( n \in \mathbb{N} \) , on pose \( {b}_{n} = \operatorname{ppcm}\left( {{a}_{0},{a}_{1},\ldots ,{a}_{n}}\right) \) . Étudier la nature de la série \( \sum 1/{b}_{n} \) .

Problem 17. Let \( {\left( {a}_{n}\right) }_{n \in \mathbb{N}} \) be a strictly increasing sequence of integers, with \( {a}_{0} > 0 \) . For all \( n \in \mathbb{N} \) , let \( {b}_{n} = \operatorname{ppcm}\left( {{a}_{0},{a}_{1},\ldots ,{a}_{n}}\right) \) . Determine the nature of the series \( \sum 1/{b}_{n} \) .

> Solution. Nous allons montrer que la série converge. La suite \( \left( {b}_{n}\right) \) est croissante. Soit \( \varphi \) la fonction strictement croissante de \( \mathbb{N} \) dans \( \mathbb{N} \) telle que

Solution. We will show that the series converges. The sequence \( \left( {b}_{n}\right) \) is increasing. Let \( \varphi \) be the strictly increasing function from \( \mathbb{N} \) to \( \mathbb{N} \) such that

\[
\forall n \in  \mathbb{N},\;{b}_{\varphi \left( n\right) } = {b}_{\varphi \left( n\right)  + 1} = \cdots  = {b}_{\varphi \left( {n + 1}\right)  - 1} < {b}_{\varphi \left( {n + 1}\right) }.
\]

Comme \( {b}_{\varphi \left( n\right) } \) divise \( {b}_{\varphi \left( {n + 1}\right) } \) , on a \( {b}_{\varphi \left( {n + 1}\right) } \geq 2{b}_{\varphi \left( n\right) } \) , donc \( {b}_{\varphi \left( n\right) } \geq {2}^{n} \) pour tout \( n \in \mathbb{N} \) .

> Since \( {b}_{\varphi \left( n\right) } \) divides \( {b}_{\varphi \left( {n + 1}\right) } \) , we have \( {b}_{\varphi \left( {n + 1}\right) } \geq 2{b}_{\varphi \left( n\right) } \) , thus \( {b}_{\varphi \left( n\right) } \geq {2}^{n} \) for all \( n \in \mathbb{N} \) .

Par ailleurs,

> Furthermore,

\[
\forall n \in  \mathbb{N},\;{P}_{n} = \mathop{\sum }\limits_{{k = \varphi \left( n\right) }}^{{\varphi \left( {n + 1}\right)  - 1}}\frac{1}{{b}_{k}} = \frac{\varphi \left( {n + 1}\right)  - \varphi \left( n\right) }{{b}_{\varphi \left( n\right) }}.
\]

(*)

> Si \( {b}_{k} = {b}_{k + 1} \) , cela signifie que \( {a}_{k + 1} \mid {b}_{k} \) . En particulier, les entiers \( {a}_{\varphi \left( n\right) + 1},\ldots ,{a}_{\varphi \left( {n + 1}\right) - 1} \) divisent \( {b}_{\varphi \left( n\right) } \) pour tout \( n \) . Or tout entier \( N \) a au plus \( 2\sqrt{N} \) diviseurs, car l’application

If \( {b}_{k} = {b}_{k + 1} \) , this means that \( {a}_{k + 1} \mid {b}_{k} \) . In particular, the integers \( {a}_{\varphi \left( n\right) + 1},\ldots ,{a}_{\varphi \left( {n + 1}\right) - 1} \) divide \( {b}_{\varphi \left( n\right) } \) for all \( n \) . However, any integer \( N \) has at most \( 2\sqrt{N} \) divisors, because the mapping

\[
\left\{  {d \in  {\mathbb{N}}^{ * }\left| d\right| N}\right\}   \rightarrow  \{ 1,2,\ldots ,\sqrt{N}\} \;d \mapsto  \inf \left\{  {d,\frac{N}{d}}\right\}
\]

est telle que tout élément de l’image d’arrivée a au plus deux antécédents. Donc \( {b}_{\varphi \left( n\right) } \) a au plus \( 2\sqrt{{b}_{\varphi \left( n\right) }} \) diviseurs, donc \( \varphi \left( {n + 1}\right) - \varphi \left( n\right) \leq 2\sqrt{{b}_{\varphi \left( n\right) }} \) . On en déduit avec (*) que

> is such that every element in the codomain has at most two preimages. Thus \( {b}_{\varphi \left( n\right) } \) has at most \( 2\sqrt{{b}_{\varphi \left( n\right) }} \) divisors, so \( \varphi \left( {n + 1}\right) - \varphi \left( n\right) \leq 2\sqrt{{b}_{\varphi \left( n\right) }} \) . We deduce from (*) that

\[
{P}_{n} \leq  \frac{2}{\sqrt{{b}_{\varphi \left( n\right) }}} \leq  \frac{2}{{2}^{n/2}}
\]

donc \( \sum {P}_{n} \) converge, et comme les séries considérées sont à termes positifs, \( \sum 1/{b}_{n} \) converge.

> therefore \( \sum {P}_{n} \) converges, and since the series considered have positive terms, \( \sum 1/{b}_{n} \) converges.

Problem 18 (TRANSFORMATION D’EULER). 1/ Soit une suite réelle \( u = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) . On note \( {\Delta u} \) la suite de terme général \( {\left( \Delta u\right) }_{n} = {u}_{n + 1} - {u}_{n} \) . On note \( {\Delta }^{0}u = u \) et pour \( p \in {\mathbb{N}}^{ * } \) on note \( {\Delta }^{p}u \) la suite définie par \( {\Delta }^{p}u = \Delta \left( {{\Delta }^{p - 1}u}\right) \) .

> Problem 18 (EULER TRANSFORMATION). 1/ Let \( u = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) be a real sequence. Let \( {\Delta u} \) be the sequence with general term \( {\left( \Delta u\right) }_{n} = {u}_{n + 1} - {u}_{n} \) . Let \( {\Delta }^{0}u = u \) and for \( p \in {\mathbb{N}}^{ * } \) let \( {\Delta }^{p}u \) be the sequence defined by \( {\Delta }^{p}u = \Delta \left( {{\Delta }^{p - 1}u}\right) \) .

a) En désignant par \( {C}_{p}^{k} \) le coefficient binomial \( p!/\left( {k!\left( {p - k}\right) !}\right) \) , montrer que

> a) Denoting by \( {C}_{p}^{k} \) the binomial coefficient \( p!/\left( {k!\left( {p - k}\right) !}\right) \) , show that

\[
\forall p, n \in  \mathbb{N}\;{\left( {\Delta }^{p}u\right) }_{n} = \mathop{\sum }\limits_{{k = 0}}^{p}{\left( -1\right) }^{p - k}{C}_{p}^{k}{u}_{n + k}.
\]

b) On suppose que la série \( \sum {\left( -1\right) }^{n}{u}_{n} \) converge (on ne suppose rien de plus sur \( \left( {u}_{n}\right) \) ) et on note \( S \) sa somme. Montrer que pour tout \( n \in \mathbb{N} \) on a

> b) Assume that the series \( \sum {\left( -1\right) }^{n}{u}_{n} \) converges (no further assumptions are made about \( \left( {u}_{n}\right) \) ) and let \( S \) be its sum. Show that for all \( n \in \mathbb{N} \) we have

\[
S - \mathop{\sum }\limits_{{p = 0}}^{n}\frac{{\left( -1\right) }^{p}}{{2}^{p + 1}}{\left( {\Delta }^{p}u\right) }_{0} = \frac{1}{{2}^{n + 1}}\mathop{\sum }\limits_{{p = 0}}^{{n + 1}}{C}_{n + 1}^{p}{R}_{p},\;\text{ où }\;{R}_{p} = \mathop{\sum }\limits_{{k = p}}^{\infty }{\left( -1\right) }^{k}{u}_{k}.
\]

(*)

> c) En déduire que la transformée d’Euler, définie par la série \( \mathop{\sum }\limits_{p}{\left( -1\right) }^{p}{2}^{-p - 1}{\left( {\Delta }^{p}u\right) }_{0} \) , est convergente et que

c) Deduce that the Euler transform, defined by the series \( \mathop{\sum }\limits_{p}{\left( -1\right) }^{p}{2}^{-p - 1}{\left( {\Delta }^{p}u\right) }_{0} \), is convergent and that

\[
\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{p}}{{2}^{p + 1}}{\left( {\Delta }^{p}u\right) }_{0} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}{u}_{n}.
\]

2/ a) Appliquer ce résultat à la série \( \sum {\left( -1\right) }^{n}/\left( {n + 1}\right) \) en explicitant les termes de la transformée d'Euler correspondante.

> 2/ a) Apply this result to the series \( \sum {\left( -1\right) }^{n}/\left( {n + 1}\right) \) by explicitly stating the terms of the corresponding Euler transform.

b) Faire de même pour la série \( \sum {\left( -1\right) }^{n}/\left( {{2n} + 1}\right) \) . et d’appliquer l’hypothèse de récurrence à \( {\left( {\Delta }^{p}u\right) }_{n + 1} \) et \( {\left( {\Delta }^{p}u\right) }_{n} \) , ce qui donne

> b) Do the same for the series \( \sum {\left( -1\right) }^{n}/\left( {{2n} + 1}\right) \) and apply the induction hypothesis to \( {\left( {\Delta }^{p}u\right) }_{n + 1} \) and \( {\left( {\Delta }^{p}u\right) }_{n} \), which gives

\[
{\left( {\Delta }^{p + 1}u\right) }_{n} = \mathop{\sum }\limits_{{k = 0}}^{p}{\left( -1\right) }^{p - k}{C}_{p}^{k}{u}_{n + 1 + k} - \mathop{\sum }\limits_{{k = 0}}^{p}{\left( -1\right) }^{p - k}{C}_{p}^{k}{u}_{n + k}
\]

\[
= \mathop{\sum }\limits_{{k = 1}}^{{p + 1}}{\left( -1\right) }^{p + 1 - k}{C}_{p}^{k - 1}{u}_{n + k} - \mathop{\sum }\limits_{{k = 0}}^{p}{\left( -1\right) }^{p - k}{C}_{p}^{k}{u}_{n + k}
\]

\[
= \mathop{\sum }\limits_{{k = 1}}^{p}{\left( -1\right) }^{p + 1 - k}\left( {{C}_{p}^{k - 1} + {C}_{p}^{k}}\right) {u}_{n + k} - {\left( -1\right) }^{p - k}{u}_{n} + {u}_{n + 1 + p}
\]

\[
= \mathop{\sum }\limits_{{k = 0}}^{{p + 1}}{\left( -1\right) }^{p + 1 - k}{C}_{p + 1}^{k}{u}_{n + k},
\]

---

Solution. 1/a) On procède par récurrence sur \( p \) . Pour \( p = 0 \) c’est immédiat. Supposons le résultat vrai pour \( p \in \mathbb{N} \) et montrons le pour \( p + 1 \) . Il suffit d’écrire \( {\left( {\Delta }^{p + 1}u\right) }_{n} = {\left( {\Delta }^{p}u\right) }_{n + 1} - {\left( {\Delta }^{p}u\right) }_{n} \)

> Solution. 1/a) We proceed by induction on \( p \). For \( p = 0 \) it is immediate. Assume the result is true for \( p \in \mathbb{N} \) and show it for \( p + 1 \). It suffices to write \( {\left( {\Delta }^{p + 1}u\right) }_{n} = {\left( {\Delta }^{p}u\right) }_{n + 1} - {\left( {\Delta }^{p}u\right) }_{n} \)

---

où nous avons utilisé l’identité \( {C}_{p}^{k - 1} + {C}_{p}^{k} = {C}_{p + 1}^{k} \) pour \( 1 \leq k \leq p \) .

> where we used the identity \( {C}_{p}^{k - 1} + {C}_{p}^{k} = {C}_{p + 1}^{k} \) for \( 1 \leq k \leq p \).

b) Nous allons également procéder par récurrence sur \( n \) . Pour \( n = 0 \) , compte tenu du fait que \( {R}_{0} = S \) , on a bien

> b) We will also proceed by induction on \( n \). For \( n = 0 \), given that \( {R}_{0} = S \), we indeed have

\[
S - \frac{1}{2}{\left( {\Delta }^{0}u\right) }_{0} = S - \frac{{u}_{0}}{2} = \frac{1}{2}\left( {S + S - {u}_{0}}\right)  = \frac{1}{2}\left( {{R}_{0} + {R}_{1}}\right) .
\]

Supposons maintenant le résultat vrai pour \( n - 1 \) et montrons le pour \( n \) . L’identité \( {C}_{n + 1}^{p} = \; {C}_{n}^{p} + {C}_{n}^{p - 1} \) pour \( 1 \leq p \leq n \) permet d’écrire

> Now assume the result is true for \( n - 1 \) and show it for \( n \). The identity \( {C}_{n + 1}^{p} = \; {C}_{n}^{p} + {C}_{n}^{p - 1} \) for \( 1 \leq p \leq n \) allows us to write

\[
\mathop{\sum }\limits_{{p = 0}}^{{n + 1}}{C}_{n + 1}^{p}{R}_{p} = {R}_{0} + \mathop{\sum }\limits_{{p = 1}}^{n}{C}_{n}^{p}{R}_{p} + \mathop{\sum }\limits_{{p = 1}}^{n}{C}_{n}^{p - 1}{R}_{p} + {R}_{n + 1} = \mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}{R}_{p} + \mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}{R}_{p + 1}
\]

\[
= \mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}\left( {2{R}_{p} - {\left( -1\right) }^{p + 1}{u}_{p + 1}}\right)  = 2\mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}{R}_{p} - \mathop{\sum }\limits_{{p = 0}}^{n}{\left( -1\right) }^{p + 1}{C}_{n}^{p}{u}_{p + 1}.
\]

D’après le résultat de la question a), la dernière somme est égale à \( {\left( -1\right) }^{n + 1}{\left( {\Delta }^{n}u\right) }_{0} \) , on a donc

> According to the result of question a), the last sum is equal to \( {\left( -1\right) }^{n + 1}{\left( {\Delta }^{n}u\right) }_{0} \), so we have

\[
{\left( -1\right) }^{n}{\left( {\Delta }^{n}u\right) }_{0} = 2\mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}{R}_{p} - \mathop{\sum }\limits_{{p = 0}}^{{n + 1}}{C}_{n + 1}^{p}{R}_{p}.
\]

(**)

> Or d'après l'hypothèse de récurrence on peut écrire

However, according to the induction hypothesis, we can write

\[
S - \mathop{\sum }\limits_{{p = 0}}^{n}\frac{{\left( -1\right) }^{p}}{{2}^{p + 1}}{\left( {\Delta }^{p}u\right) }_{0} = S - \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}\frac{{\left( -1\right) }^{p}}{{2}^{p + 1}}{\left( {\Delta }^{p}u\right) }_{0} - \frac{{\left( -1\right) }^{n}}{{2}^{n + 1}}{\left( {\Delta }^{n}u\right) }_{0} = \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{p = 0}}^{n}{C}_{n}^{p}{R}_{p} - \frac{{\left( -1\right) }^{n}}{{2}^{n + 1}}{\left( {\Delta }^{n}u\right) }_{0}.
\]

En remplaçant \( {\left( -1\right) }^{n}{\left( {\Delta }^{n}u\right) }_{0} \) par l’expression à droite de (**), on en déduit l’identité (*), ce qui achève la preuve par récurrence.

> By replacing \( {\left( -1\right) }^{n}{\left( {\Delta }^{n}u\right) }_{0} \) with the expression on the right of (**), we deduce the identity (*), which completes the proof by induction.

c) Compte tenu du résultat de la question précédente, il suffit de prouver que \( {2}^{-n}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{R}_{k} \) tend vers 0 lorsque \( n \rightarrow + \infty \) . Soit \( \varepsilon > 0 \) . Comme la série \( \sum {\left( -1\right) }^{n}{u}_{n} \) converge, la suite de ses restes \( \left( {R}_{k}\right) \) converge vers 0 . Soit \( N \in {\mathbb{N}}^{ * } \) tel que pour tout \( k \geq N,\left| {R}_{k}\right| < \varepsilon \) . Comme la suite \( \left( {R}_{k}\right) \) converge vers 0, elle est bornée, donc \( \exists M > 0 \) tel que \( \left| {R}_{k}\right| \leq M \) pour tout \( k \) . Pour tout \( n \geq N \) on a

> c) Given the result of the previous question, it suffices to prove that \( {2}^{-n}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{R}_{k} \) tends to 0 as \( n \rightarrow + \infty \). Let \( \varepsilon > 0 \). Since the series \( \sum {\left( -1\right) }^{n}{u}_{n} \) converges, the sequence of its remainders \( \left( {R}_{k}\right) \) converges to 0. Let \( N \in {\mathbb{N}}^{ * } \) such that for all \( k \geq N,\left| {R}_{k}\right| < \varepsilon \). Since the sequence \( \left( {R}_{k}\right) \) converges to 0, it is bounded, so \( \exists M > 0 \) such that \( \left| {R}_{k}\right| \leq M \) for all \( k \). For all \( n \geq N \) we have

\[
\left| {\frac{1}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{R}_{k}}\right|  \leq  \frac{M}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{C}_{n}^{k} + \frac{\varepsilon }{{2}^{n}}\mathop{\sum }\limits_{{k = N}}^{n}{C}_{n}^{k} \leq  \frac{M}{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{{N - 1}}{n}^{k} + \frac{\varepsilon }{{2}^{n}}\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k} \leq  M\frac{N{n}^{N - 1}}{{2}^{n}} + \varepsilon .
\]

Comme \( N \) est un entier fixé, \( N{n}^{N - 1}/{2}^{n} \) tend vers 0 lorsque \( n \rightarrow + \infty \) donc lorsque \( n \) est suffisamment grand, tout ceci est majoré par \( {2\varepsilon } \) . On en déduit le résultat.

> As \( N \) is a fixed integer, \( N{n}^{N - 1}/{2}^{n} \) tends to 0 as \( n \rightarrow + \infty \), so when \( n \) is sufficiently large, all of this is bounded by \( {2\varepsilon } \). We deduce the result from this.

2 / a) Dans notre cas, on a \( {u}_{n} = 1/\left( {n + 1}\right) \) . La formule de la question 1/a) donne

> 2 / a) In our case, we have \( {u}_{n} = 1/\left( {n + 1}\right) \). The formula from question 1/a) gives

\[
{\left( {\Delta }^{n}u\right) }_{0} = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{n - k}\frac{{C}_{n}^{k}}{k + 1} = {\left( -1\right) }^{n}{\int }_{0}^{1}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{C}_{n}^{k}{x}^{k}}\right) {dx} = {\left( -1\right) }^{n}{\int }_{0}^{1}{\left( 1 - x\right) }^{n}{dx} = \frac{{\left( -1\right) }^{n}}{n + 1}.
\]

On en déduit, d'après l'identité de la transformée d'Euler obtenu à la question 1/c), que

> We deduce from this, according to the Euler transform identity obtained in question 1/c), that

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{n + 1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{\left( {n + 1}\right) {2}^{n + 1}}.
\]

Notons que la première série a pour somme log 2 (c'est classique, voir par exemple la remarque de l’exercice 10 page 263), et l’égalité ci dessus se retrouve en écrivant que \( \log 2 = - \log \left( {1 - 1/2}\right) \) à partir du développement en série entière de \( \log \left( {1 + x}\right) \) .

> Note that the first series has a sum of log 2 (this is standard, see for example the remark in exercise 10 on page 263), and the equality above is found by writing that \( \log 2 = - \log \left( {1 - 1/2}\right) \) from the power series expansion of \( \log \left( {1 + x}\right) \).

b) Ici \( {u}_{n} = 1/\left( {{2n} + 1}\right) \) et on a

> b) Here \( {u}_{n} = 1/\left( {{2n} + 1}\right) \) and we have

\[
{\left( {\Delta }^{n}u\right) }_{0} = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{n - k}\frac{{C}_{n}^{k}}{{2k} + 1} = {\left( -1\right) }^{n}{\int }_{0}^{1}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{C}_{n}^{k}{x}^{2k}}\right) {dx} = {\left( -1\right) }^{n}{\int }_{0}^{1}{\left( 1 - {x}^{2}\right) }^{n}{dx}.
\]

Notons \( {I}_{n} \) la dernière intégrale. Une intégration par partie donne, lorsque \( n \geq 1 \) ,

> Let \( {I}_{n} \) be the last integral. Integration by parts gives, as \( n \geq 1 \),

\[
{I}_{n} = {\left\lbrack  x{\left( 1 - {x}^{2}\right) }^{n}\right\rbrack  }_{0}^{1} + {\int }_{0}^{1}\left( {{2n}{x}^{2}}\right) {\left( 1 - {x}^{2}\right) }^{n - 1}{dx} = {2n}\left( {{I}_{n - 1} - {I}_{n}}\right) .
\]

On en déduit \( {I}_{n} = \left( {{2n}/\left( {{2n} + 1}\right) }\right) {I}_{n - 1} \) . Compte tenu de la valeur \( {I}_{0} = 1 \) , une récurrence facile donne \( {I}_{n} = \left( {2 \cdot 4\cdots \left( {2n}\right) }\right) /\left( {3 \cdot 5\cdots \left( {{2n} + 1}\right) }\right) \) . L’identité de la transformée d’Euler donne donc

> We deduce \( {I}_{n} = \left( {{2n}/\left( {{2n} + 1}\right) }\right) {I}_{n - 1} \). Given the value \( {I}_{0} = 1 \), an easy induction gives \( {I}_{n} = \left( {2 \cdot 4\cdots \left( {2n}\right) }\right) /\left( {3 \cdot 5\cdots \left( {{2n} + 1}\right) }\right) \). The Euler transform identity therefore gives

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{2n} + 1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{{2}^{n + 1}}\frac{2 \cdot  4\cdots \left( {2n}\right) }{3 \cdot  5\cdots \left( {{2n} + 1}\right) } = \frac{1}{2}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{n!}{1 \cdot  3\cdots \left( {{2n} + 1}\right) }.
\]

La somme de la série de gauche est égale à \( \pi /4 = \arctan \left( 1\right) \) (ici aussi, voir la remarque de l’exer-cice 10 page 263). La formule obtenue permet donc d'obtenir une série convergeant rapidement vers \( \pi /4 \) .

> The sum of the series on the left is equal to \( \pi /4 = \arctan \left( 1\right) \) (here too, see the remark in exercise 10 on page 263). The formula obtained therefore allows us to obtain a series that converges rapidly to \( \pi /4 \).

Remarque. La transformée d'Euler est en général utilisée pour accélérer la convergence des séries alternées. Sous certaines hypothèses, on peut démontrer que la convergence est \( O\left( {1/{2}^{n}}\right) \) , comme c’est le cas dans le problème suivant qui généralise la transformée d’Euler sous des conditions particulières de la suite \( \left( {u}_{n}\right) \) .

> Remark. The Euler transform is generally used to accelerate the convergence of alternating series. Under certain hypotheses, it can be shown that the convergence is \( O\left( {1/{2}^{n}}\right) \), as is the case in the following problem which generalizes the Euler transform under specific conditions on the sequence \( \left( {u}_{n}\right) \).

Problem 19 (ACCÉLÉRATION DE LA CONVERGENCE DES SÉRIES ALTERNÉES). Soit \( w \) une fonction réelle intégrable sur \( \rbrack 0,1\lbrack \) . On définit la suite \( \left( {u}_{n}\right) \) par

> Problem 19 (ACCELERATION OF THE CONVERGENCE OF ALTERNATING SERIES). Let \( w \) be a real function integrable on \( \rbrack 0,1\lbrack \). We define the sequence \( \left( {u}_{n}\right) \) by

\[
\forall n \in  \mathbb{N},\;{u}_{n} = {\int }_{0}^{1}{t}^{n}w\left( t\right) {dt}.
\]

On se donne une suite de polynômes \( \left( {P}_{n}\right) \) à coefficients réels telle que \( \forall n \in \mathbb{N} \) , \( \deg {P}_{n} = n \) et \( {P}_{n}\left( {-1}\right) \neq 0 \) .

> We are given a sequence of polynomials \( \left( {P}_{n}\right) \) with real coefficients such that \( \forall n \in \mathbb{N} \), \( \deg {P}_{n} = n \) and \( {P}_{n}\left( {-1}\right) \neq 0 \).

1/a) Montrer que

> 1/a) Show that

\[
{S}_{n} = \frac{1}{{P}_{n}\left( {-1}\right) }{\int }_{0}^{1}\frac{{P}_{n}\left( {-1}\right)  - {P}_{n}\left( x\right) }{1 + x}w\left( x\right) {dx}
\]

s’écrit comme une combinaison linéaire des termes \( {\left( {u}_{k}\right) }_{0 \leq k < n} \) et expliciter ses coefficients en fonction de ceux de \( {P}_{n} \) .

> can be written as a linear combination of the terms \( {\left( {u}_{k}\right) }_{0 \leq k < n} \) and express its coefficients in terms of those of \( {P}_{n} \).

b) Montrer que la série \( \sum {\left( -1\right) }^{n}{u}_{n} \) converge, et que sa somme \( S \) vérifie

> b) Show that the series \( \sum {\left( -1\right) }^{n}{u}_{n} \) converges, and that its sum \( S \) satisfies

\[
\left| {S - {S}_{n}}\right|  \leq  \frac{{M}_{n}}{\left| {P}_{n}\left( -1\right) \right| }I,\;\text{ avec }\;{M}_{n} = \mathop{\sup }\limits_{{x \in  \left\lbrack  {0,1}\right\rbrack  }}\left| {{P}_{n}\left( x\right) }\right| ,\;I = {\int }_{0}^{1}\frac{\left| w\left( t\right) \right| }{1 + t}{dt}.
\]

2/a) On choisit comme suite de polynômes \( {P}_{n}\left( x\right) = {\left( 1 - x\right) }^{n} \) . Expliciter \( {S}_{n} \) et donner une majoration de \( \left| {{S}_{n} - S}\right| \) en fonction de \( I \) et \( n \) .

> 2/a) We choose as a sequence of polynomials \( {P}_{n}\left( x\right) = {\left( 1 - x\right) }^{n} \). Express \( {S}_{n} \) and provide an upper bound for \( \left| {{S}_{n} - S}\right| \) in terms of \( I \) and \( n \).

b) Répondre à la même question avec la suite de polynômes \( {P}_{n}\left( x\right) = {\left( 1 - 2x\right) }^{n} \) .

> b) Answer the same question for the sequence of polynomials \( {P}_{n}\left( x\right) = {\left( 1 - 2x\right) }^{n} \) .

c) Montrer l’existence et l’unicité d’une suite de polynômes \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) vérifiant \( \deg {P}_{n} = n \) et \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) pour tout \( t \in \mathbb{R} \) . Avec ce choix de polynômes, majorer \( \left| {S - {S}_{n}}\right| \) .

> c) Show the existence and uniqueness of a sequence of polynomials \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) satisfying \( \deg {P}_{n} = n \) and \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) for all \( t \in \mathbb{R} \) . With this choice of polynomials, find an upper bound for \( \left| {S - {S}_{n}}\right| \) .

3/a) Montrer que l'on peut apliquer les processus d'accélération de convergence des questions précédentes aux séries \( \sum {\left( -1\right) }^{n}/{\left( n + 1\right) }^{s} \) , où \( s > 0 \) , et à la série \( \sum {\left( -1\right) }^{n}\left( {\log n}\right) /n \) .

> 3/a) Show that the convergence acceleration processes from the previous questions can be applied to the series \( \sum {\left( -1\right) }^{n}/{\left( n + 1\right) }^{s} \) , where \( s > 0 \) , and to the series \( \sum {\left( -1\right) }^{n}\left( {\log n}\right) /n \) .

b) En utilisant l'accélération fondée sur les polynômes de la question 2/c) de degré 4, calculer une approximation numérique de \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\left( {\log n}\right) /n \) et en déduire une approximation numérique de la constante d’Euler \( \gamma \) (on s’appuiera sur l’égalité \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\left( {\log n}\right) /n = \; \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) établie à l’exercice 11 page 226).

> b) Using the acceleration based on the polynomials from question 2/c) of degree 4, calculate a numerical approximation of \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\left( {\log n}\right) /n \) and deduce a numerical approximation of Euler's constant \( \gamma \) (rely on the equality \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\left( {\log n}\right) /n = \; \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) established in exercise 11 on page 226).

Solution. 1/ a) Ecrivons \( {P}_{n} \) sous la forme \( {P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{\left( -x\right) }^{k} \) . On a

> Solution. 1/ a) Let us write \( {P}_{n} \) in the form \( {P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{\left( -x\right) }^{k} \) . We have

\[
{P}_{n}\left( {-1}\right)  - {P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\left( {1 - {\left( -x\right) }^{k}}\right)  = \left( {1 + x}\right) \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}\mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{\left( -x\right) }^{j} = \left( {1 + x}\right) \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}\left( {\mathop{\sum }\limits_{{k = j + 1}}^{n}{a}_{k}}\right) {\left( -x\right) }^{j}.
\]

On en déduit l’expression de \( {S}_{n} \) comme combinaison linéaire des \( {\left( {u}_{k}\right) }_{0 \leq k < n} \) en écrivant

> We deduce the expression of \( {S}_{n} \) as a linear combination of \( {\left( {u}_{k}\right) }_{0 \leq k < n} \) by writing

\[
{S}_{n} = \frac{1}{{P}_{n}\left( {-1}\right) }{\int }_{0}^{1}\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}\left( {\mathop{\sum }\limits_{{k = j + 1}}^{n}{a}_{k}}\right) {\left( -x\right) }^{j}w\left( x\right) {dx} = \frac{1}{{P}_{n}\left( {-1}\right) }\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\left( -1\right) }^{j}\left( {\mathop{\sum }\limits_{{k = j + 1}}^{n}{a}_{k}}\right) {u}_{j}.
\]

(*)

> b) Compte tenu de la définition des \( {u}_{n} \) , on a

b) Given the definition of \( {u}_{n} \) , we have

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{u}_{k} = {\int }_{0}^{1}\frac{1 + {t}^{n + 1}}{1 + t}w\left( t\right) {dt}\;\text{ donc }\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{u}_{k} = {\int }_{0}^{1}\frac{w\left( t\right) }{1 + t}{dt},
\]

où nous avons utilisé le théorème de convergence dominée, la fonction intégrée dans l'intégrale de gauche étant majorée en valeur absolue par la fonction intégrable \( \left| w\right| \) indépendamment de \( n \) . Ainsi la somme de la série \( \sum {\left( -1\right) }^{n}{u}_{n} \) est égale à \( S = {\int }_{0}^{1}\frac{w\left( t\right) }{1 + t}{dt} \) . On a maintenant

> where we used the dominated convergence theorem, the integrand in the integral on the left being bounded in absolute value by the integrable function \( \left| w\right| \) independently of \( n \) . Thus the sum of the series \( \sum {\left( -1\right) }^{n}{u}_{n} \) is equal to \( S = {\int }_{0}^{1}\frac{w\left( t\right) }{1 + t}{dt} \) . We now have

\[
S - {S}_{n} = \frac{1}{{P}_{n}\left( {-1}\right) }{\int }_{0}^{1}\frac{{P}_{n}\left( x\right) }{1 + x}w\left( x\right) {dx}\;\text{ donc }\;\left| {S - {S}_{n}}\right|  \leq  \frac{{M}_{n}}{\left| {P}_{n}\left( -1\right) \right| }{\int }_{0}^{1}\frac{\left| w\left( x\right) \right| }{1 + x}{dx} = \frac{{M}_{n}}{\left| {P}_{n}\left( -1\right) \right| }I.
\]

Notons que si \( w \) est positive, on a \( I = S \) et la majoration devient \( \left| {S - {S}_{n}}\right| \leq \frac{{M}_{n}}{\left| {P}_{n}\left( -1\right) \right| }S \) .

> Note that if \( w \) is positive, we have \( I = S \) and the upper bound becomes \( \left| {S - {S}_{n}}\right| \leq \frac{{M}_{n}}{\left| {P}_{n}\left( -1\right) \right| }S \) .

2/a) En choisissant \( {P}_{n}\left( x\right) = {\left( 1 - x\right) }^{n} \) , on a \( {P}_{n}\left( {-1}\right) = {2}^{n},{P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{\left( -x\right) }^{k} \) et \( {M}_{n} = 1 \) . Avec la formule (*) on en déduit

> 2/a) By choosing \( {P}_{n}\left( x\right) = {\left( 1 - x\right) }^{n} \) , we have \( {P}_{n}\left( {-1}\right) = {2}^{n},{P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{\left( -x\right) }^{k} \) and \( {M}_{n} = 1 \) . With formula (*) we deduce

\[
{S}_{n} = \frac{1}{{2}^{n}}\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\left( -1\right) }^{j}\left( {\mathop{\sum }\limits_{{k = j + 1}}^{n}{C}_{n}^{k}}\right) {u}_{j},\;\text{ et }\;\left| {S - {S}_{n}}\right|  \leq  \frac{I}{{2}^{n}}.
\]

b) Avec \( {P}_{n}\left( x\right) = {\left( 1 - 2x\right) }^{n} \) , on a \( {P}_{n}\left( {-1}\right) = {3}^{n},{P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{2}^{k}{C}_{n}^{k}{\left( -x\right) }^{k} \) et \( {M}_{n} = 1 \) , d’où

> b) With \( {P}_{n}\left( x\right) = {\left( 1 - 2x\right) }^{n} \) , we have \( {P}_{n}\left( {-1}\right) = {3}^{n},{P}_{n}\left( x\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{2}^{k}{C}_{n}^{k}{\left( -x\right) }^{k} \) and \( {M}_{n} = 1 \) , hence

\[
{S}_{n} = \frac{1}{{3}^{n}}\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\left( -1\right) }^{j}\left( {\mathop{\sum }\limits_{{k = j + 1}}^{n}{2}^{k}{C}_{n}^{k}}\right) {u}_{j}\;\text{ et }\;\left| {S - {S}_{n}}\right|  \leq  \frac{I}{{3}^{n}}.
\]

c) L’existence et l’unicité de la suite de polynômes \( \left( {P}_{n}\right) \) découle de l’écriture

> c) The existence and uniqueness of the sequence of polynomials \( \left( {P}_{n}\right) \) follows from the expression

\[
\cos \left( {2nt}\right)  = \Re \left( {\left( \cos t + i\sin t\right) }^{2n}\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{2n}^{2k}{\left( -1\right) }^{n - k}{\cos }^{2k}t{\sin }^{2\left( {n - k}\right) }t = {P}_{n}\left( {{\sin }^{2}t}\right)
\]

avec

> with

\[
{P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{2n}^{2k}{\left( 1 - x\right) }^{k}{\left( -x\right) }^{n - k}.
\]

\( \left( {* * }\right) \) .

> Pour majorer \( \left| {S - {S}_{n}}\right| \) , on remarque déjà que l’égalité \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) entraîne \( {M}_{n} = 1 \) . Calculons maintenant \( {P}_{n}\left( {-1}\right) \) . L’égalité \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) , vraie pour \( t \in \mathbb{R} \) , l’est aussi pour \( t \in \mathbb{C} \) (en effet, on aurait pu démontrer l’identité \( \cos \left( {2nt}\right) = {P}_{n}\left( {{\sin }^{2}t}\right) \) en partant de \( 2\cos \left( {2nt}\right) = {\left( \cos t + i\sin t\right) }^{2n} + {\left( \cos t - i\sin t\right) }^{2n} \) qui est vraie pour tout \( t \in \mathbb{C} \) . On aurait pu aussi le démontrer en notant que \( {P}_{n}\left( {{\sin }^{2}t}\right) - \cos \left( {2nt}\right) \) est une série entière, nulle sur \( \mathbb{R} \) lonc sur \( \mathbb{C} \) d’après le principe des zéros isolés). En choisissant \( t = {t}_{0} \) tel que \( \sin {t}_{0} = i \) on va calculer

To find an upper bound for \( \left| {S - {S}_{n}}\right| \) , we first note that the equality \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) implies \( {M}_{n} = 1 \) . Let us now calculate \( {P}_{n}\left( {-1}\right) \) . The equality \( {P}_{n}\left( {{\sin }^{2}t}\right) = \cos \left( {2nt}\right) \) , true for \( t \in \mathbb{R} \) , is also true for \( t \in \mathbb{C} \) (indeed, we could have proven the identity \( \cos \left( {2nt}\right) = {P}_{n}\left( {{\sin }^{2}t}\right) \) starting from \( 2\cos \left( {2nt}\right) = {\left( \cos t + i\sin t\right) }^{2n} + {\left( \cos t - i\sin t\right) }^{2n} \) which is true for all \( t \in \mathbb{C} \) . We could also have proven it by noting that \( {P}_{n}\left( {{\sin }^{2}t}\right) - \cos \left( {2nt}\right) \) is a power series, zero on \( \mathbb{R} \) hence on \( \mathbb{C} \) according to the identity theorem). By choosing \( t = {t}_{0} \) such that \( \sin {t}_{0} = i \) we will calculate

> \( {P}_{n}\left( {-1}\right) \) . L’équation \( \sin {t}_{0} = i \) équivaut à \( \frac{{e}^{i{t}_{0}} - {e}^{-i{t}_{0}}}{2i} = i \) , ou encore \( {\left( {e}^{i{t}_{0}}\right) }^{2} + 2{e}^{i{t}_{0}} - 1 = 0 \) , vérifiée si on choisit \( {e}^{i{t}_{0}} = \sqrt{2} - 1 \) , ce qui est le cas avec \( {t}_{0} = - i\log \left( {\sqrt{2} - 1}\right) \) . On a alors

\( {P}_{n}\left( {-1}\right) \) . The equation \( \sin {t}_{0} = i \) is equivalent to \( \frac{{e}^{i{t}_{0}} - {e}^{-i{t}_{0}}}{2i} = i \) , or \( {\left( {e}^{i{t}_{0}}\right) }^{2} + 2{e}^{i{t}_{0}} - 1 = 0 \) , which is satisfied if we choose \( {e}^{i{t}_{0}} = \sqrt{2} - 1 \) , which is the case with \( {t}_{0} = - i\log \left( {\sqrt{2} - 1}\right) \) . We then have

\[
{P}_{n}\left( {-1}\right)  = \cos \left( {{2n}{t}_{0}}\right)  = \frac{{e}^{{2in}{t}_{0}} + {e}^{-{2in}{t}_{0}}}{2} = \frac{{\left( \sqrt{2} - 1\right) }^{2n} + {\left( \sqrt{2} + 1\right) }^{2n}}{2} = \frac{{\left( 3 + \sqrt{8}\right) }^{n} + {\left( 3 - \sqrt{8}\right) }^{n}}{2}.
\]

Finalement on obtient la majoration \( \left| {S - {S}_{n}}\right| \leq {2I}/{\left( 3 + \sqrt{8}\right) }^{n} \) .

> Finally, we obtain the upper bound \( \left| {S - {S}_{n}}\right| \leq {2I}/{\left( 3 + \sqrt{8}\right) }^{n} \) .

3/a) On part du résultat classique suivant, obtenu avec le changement de variable \( u = {nx} \)

> 3/a) We start from the following classic result, obtained with the change of variable \( u = {nx} \)

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\int }_{0}^{+\infty }{e}^{-{nx}}{x}^{s - 1}{dx} = \frac{1}{{n}^{s}}{\int }_{0}^{+\infty }{e}^{-u}{u}^{s - 1}{du} = \frac{\Gamma \left( s\right) }{{n}^{s}}
\]

où \( \Gamma \left( s\right) \) est la valeur de la dernière intégrale. Le changement de variable \( t = {e}^{-x} \) dans la première intégrale, entraîne

> where \( \Gamma \left( s\right) \) is the value of the last integral. The change of variable \( t = {e}^{-x} \) in the first integral leads to

\[
\frac{\Gamma \left( s\right) }{{n}^{s}} = {\int }_{0}^{1}{t}^{n - 1}{\log }^{s - 1}\left( {1/t}\right) {dt}\;\text{ donc }\;\frac{1}{{\left( n + 1\right) }^{s}} = {\int }_{0}^{1}{t}^{n}{w}_{s}\left( t\right) {dt},\;{w}_{s}\left( t\right)  = \frac{{\log }^{s - 1}\left( {1/t}\right) }{\Gamma \left( s\right) }.
\]

La fonction \( {w}_{s}\left( t\right) \) est intégrable sur \( \rbrack 0,1\rbrack \) , nous sommes bien dans le cadre des séries de l’exercice donc la convergence de \( \sum {\left( -1\right) }^{n}/{\left( n + 1\right) }^{s} \) peut être accélérée avec les méthodes précédentes.

> The function \( {w}_{s}\left( t\right) \) is integrable on \( \rbrack 0,1\rbrack \) , we are indeed within the framework of the series in the exercise, so the convergence of \( \sum {\left( -1\right) }^{n}/{\left( n + 1\right) }^{s} \) can be accelerated using the previous methods.

Passons maintenant à \( \sum {\left( -1\right) }^{n}\log n/n \) . En dérivant par rapport à \( s \) en \( s = 1 \) l’expression précédente de \( 1/{\left( n + 1\right) }^{s} \) (la dérivabilité est facile à partir du théorème de dérivation sous le signe intégral des fonctions intégrables), on obtient

> Let us now move on to \( \sum {\left( -1\right) }^{n}\log n/n \) . By differentiating the previous expression of \( 1/{\left( n + 1\right) }^{s} \) with respect to \( s \) at \( s = 1 \) (differentiability is easily established from the theorem of differentiation under the integral sign for integrable functions), we obtain

\[
- \frac{\log \left( {n + 1}\right) }{n + 1} =  - \frac{{\Gamma }^{\prime }\left( 1\right) }{\Gamma {\left( 1\right) }^{2}}{\int }_{0}^{1}{t}^{n}{dt} + \frac{1}{\Gamma \left( 1\right) }{\int }_{0}^{1}{t}^{n}\log \log \left( {1/t}\right) {dt} = {\int }_{0}^{1}{t}^{n}\left( {\log \log \left( {1/t}\right)  - {\Gamma }^{\prime }\left( 1\right) }\right) {dt}.
\]

Ainsi nous sommes bien dans le cadre des séries de l'exercice et la convergence de la série alternée \( \sum {\left( -1\right) }^{n}\log \left( {n + 1}\right) /\left( {n + 1}\right) \) peut être accélérée avec les méthodes précédentes.

> Thus, we are indeed within the framework of the series in the exercise, and the convergence of the alternating series \( \sum {\left( -1\right) }^{n}\log \left( {n + 1}\right) /\left( {n + 1}\right) \) can be accelerated using the previous methods.

b) En utilisant l’expression (**) du polynôme \( {P}_{4}\left( x\right) \) défini dans la question \( 2/\mathrm{c} \) ), on obtient \( {P}_{4}\left( x\right) = {x}^{4} - {28}\left( {1 - x}\right) {x}^{3} + {70}{\left( 1 - x\right) }^{2}{x}^{2} - {28}{\left( 1 - x\right) }^{3}x + {\left( 1 - x\right) }^{4} = 1 - {32x} + {160}{x}^{2} - {256}{x}^{3} + {128}{x}^{4} \) et \( {P}_{4}\left( {-1}\right) = {577} \) . Pour l’accélération de \( S = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}\log \left( {n + 1}\right) /\left( {n + 1}\right) \) , on en déduit, compte tenu de l'expression (*),

> b) Using expression (**) of the polynomial \( {P}_{4}\left( x\right) \) defined in question \( 2/\mathrm{c} \) ), we obtain \( {P}_{4}\left( x\right) = {x}^{4} - {28}\left( {1 - x}\right) {x}^{3} + {70}{\left( 1 - x\right) }^{2}{x}^{2} - {28}{\left( 1 - x\right) }^{3}x + {\left( 1 - x\right) }^{4} = 1 - {32x} + {160}{x}^{2} - {256}{x}^{3} + {128}{x}^{4} \) and \( {P}_{4}\left( {-1}\right) = {577} \) . For the acceleration of \( S = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}\log \left( {n + 1}\right) /\left( {n + 1}\right) \) , we deduce, taking into account expression (*),

\[
{S}_{4} = \frac{1}{577}\left( {-{544}\frac{\log 2}{2} + {384}\frac{\log 3}{3} - {128}\frac{\log 4}{4}}\right)  = \frac{1}{577}\left( {-{336}\log 2 + {128}\log 3}\right)  \approx   - 0,{159922}\ldots
\]

Pour majorer \( I = {\int }_{0}^{1}\left| {\log \log \left( {1/t}\right) - {\Gamma }^{\prime }\left( 1\right) }\right| /\left( {1 + t}\right) {dt} \) , on commence par majorer \( {\Gamma }^{\prime }\left( 1\right) \) . On a

> To bound \( I = {\int }_{0}^{1}\left| {\log \log \left( {1/t}\right) - {\Gamma }^{\prime }\left( 1\right) }\right| /\left( {1 + t}\right) {dt} \) , we begin by bounding \( {\Gamma }^{\prime }\left( 1\right) \) . We have

\[
{\Gamma }^{\prime }\left( 1\right)  = {\int }_{0}^{+\infty }{e}^{-t}\log {tdt}\;\text{ donc }\;\left| {{\Gamma }^{\prime }\left( 1\right) }\right|  \leq  {\int }_{0}^{1}\left| {\log t}\right| {dt} + {\int }_{0}^{+\infty }{e}^{-t}{tdt} = 2.
\]

Ensuite le changement de variable \( t = {e}^{-x} \) donne

> Then the change of variable \( t = {e}^{-x} \) gives

\[
{\int }_{0}^{1}\left| {\log \log \left( {1/t}\right) }\right| {dt} = {\int }_{0}^{+\infty }\left| {\log x}\right| {e}^{-x}{dx} \leq  {\int }_{0}^{1}\left| {\log t}\right| {dt} + {\int }_{0}^{+\infty }{e}^{-t}{tdt} = 2.
\]

On déduit de tout ceci la majoration \( I \leq 4 \) . Avec le résultat de la question \( 2/\mathrm{c} \) ), on a donc

> From all this, we deduce the bound \( I \leq 4 \) . With the result of question \( 2/\mathrm{c} \) ), we therefore have

\[
\left| {S - {S}_{4}}\right|  \leq  8/{\left( 3 + \sqrt{8}\right) }^{4} \leq  0,{007}
\]

Donc \( S \approx 0,{159\text{ Å }0},{007} \) près. Or \( - S = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\log n/n = \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) donc \( \gamma = \; - S/\log 2 + \frac{1}{2}\log 2 \approx 0,{577} \) à \( 0,{007}/\log 2 \approx 0,{01} \) près.

> Therefore \( S \approx 0,{159\text{ Å }0},{007} \) approximately. However, \( - S = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( -1\right) }^{n}\log n/n = \left( {\gamma - \frac{1}{2}\log 2}\right) \log 2 \) so \( \gamma = \; - S/\log 2 + \frac{1}{2}\log 2 \approx 0,{577} \) to within \( 0,{007}/\log 2 \approx 0,{01} \) .

Remarque. - L'accélération de convergence de séries alternées obtenue par le choix de polynômes de la question 2/a) correspond à la transformée d'Euler, rencontrée dans le problème précédent.

> Remark. - The acceleration of convergence of alternating series obtained by the choice of polynomials in question 2/a) corresponds to the Euler transform, encountered in the previous problem.

- La majoration de l'erreur obtenue en \( 3/\mathrm{b} \) ) est très grossière, car à partir de \( {S}_{4} \) on obtient l’approximation \( \gamma  \approx  0,{577292} \) ce qui est précis à \( 8 \times  {10}^{-5} \) près.

> - The error bound obtained in \( 3/\mathrm{b} \) ) is very rough, because from \( {S}_{4} \) we obtain the approximation \( \gamma  \approx  0,{577292} \) which is accurate to within \( 8 \times  {10}^{-5} \) .

- La fonction \( \Gamma \) introduite dans la solution de \( 3/a \) ) est étudiée dans le sujet d’étude 1 page 315. Dans la question \( 3/\mathrm{d}) \) de ce sujet d’étude on montre que \( {\Gamma }^{\prime }\left( 1\right)  =  - \gamma \) . - Les polynômes \( {P}_{n} \) définis dans la question \( 2/\mathrm{c} \) ) vérifient \( {P}_{n}\left( x\right)  = {T}_{n}\left( {1 - {2x}}\right) \) où les \( {T}_{n} \) sont les polynômes de Tchébycheff de première espèce (voir le tome Algèbre). On peut montrer qu’ils ont la forme explicite \( {P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{n}{n + k}{C}_{n + k}^{2k}{4}^{k}{\left( -x\right) }^{k} \) , ce qui permet d’expliciter l’expression de \( {S}_{n} \) avec ce choix de polynômes.

> - The function \( \Gamma \) introduced in the solution to \( 3/a \) ) is studied in study topic 1 on page 315. In question \( 3/\mathrm{d}) \) of this study topic, it is shown that \( {\Gamma }^{\prime }\left( 1\right)  =  - \gamma \) . - The polynomials \( {P}_{n} \) defined in question \( 2/\mathrm{c} \) ) satisfy \( {P}_{n}\left( x\right)  = {T}_{n}\left( {1 - {2x}}\right) \) where the \( {T}_{n} \) are the Chebyshev polynomials of the first kind (see the Algebra volume). It can be shown that they have the explicit form \( {P}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{n}{n + k}{C}_{n + k}^{2k}{4}^{k}{\left( -x\right) }^{k} \) , which allows for the explicit expression of \( {S}_{n} \) with this choice of polynomials.

Problems 20. Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( \geq 1 \) , telle que sa somme \( f \) se prolonge en une fonction continue (toujours notée \( f \) ) sur le disque unité fermé. On suppose que

> Problems 20. Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( \geq 1 \) , such that its sum \( f \) extends to a continuous function (still denoted \( f \) ) on the closed unit disk. Suppose that

\[
\exists \alpha  \in  \mathbb{R},\exists \theta  > 0,\forall t \in  \left\lbrack  {\alpha ,\alpha  + \theta }\right\rbrack  ,\;f\left( {e}^{it}\right)  = 0.
\]

(*)

> Montrer que \( f \) est la fonction nulle.

Show that \( f \) is the zero function.

> Solution. Soit \( N \in {\mathbb{N}}^{ * } \) tel que \( {N\theta } > {2\pi } \) . Considérons la fonction

Solution. Let \( N \in {\mathbb{N}}^{ * } \) be such that \( {N\theta } > {2\pi } \) . Consider the function

\[
g : D = \{ z \in  \mathbb{C},\left| z\right|  \leq  1\}  \rightarrow  \mathbb{C}\;z \mapsto  f\left( z\right) f\left( {z{e}^{i\theta }}\right) \cdots f\left( {z{e}^{i\left( {N - 1}\right) \theta }}\right) .
\]

D’après (*), \( g \) est nulle sur le cercle unité. Or \( f \) est la somme d’une série entière sur \( D \) , et par un produit de Cauchy on en déduit que \( g \) est la somme d’une série entière \( \sum {b}_{n}{z}^{n} \) sur le disque unité ouvert. Soit \( n \in \mathbb{N} \) . La formule de Cauchy (voir le théorème 4 page 250) donne

> According to (*), \( g \) is zero on the unit circle. However, \( f \) is the sum of a power series on \( D \) , and by a Cauchy product, we deduce that \( g \) is the sum of a power series \( \sum {b}_{n}{z}^{n} \) on the open unit disk. Let \( n \in \mathbb{N} \) . Cauchy's formula (see theorem 4 on page 250) gives

\[
\forall r \in  \rbrack 0,1\left\lbrack  {,\;{b}_{n}{r}^{n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }g\left( {r{e}^{it}}\right) {e}^{-{int}}{dt}.}\right.
\]

\( \left( {* * }\right) \)

> La fonction \( \left\lbrack {0,1}\right\rbrack \times \left\lbrack {0,{2\pi }}\right\rbrack \rightarrow \mathbb{C}\;\left( {r, t}\right) \rightarrow g\left( {r{e}^{it}}\right) \) est continue (car \( g \) est continue sur \( D \) ), et d’après le théorème de continuité sous le signe intégral, l’intégrale de (**) tend vers \( {\int }_{0}^{2\pi }g\left( {e}^{it}\right) {e}^{-{int}}{dt} = 0 \) lorsque \( r \rightarrow {1}^{ - } \) . On en déduit \( {b}_{n} = 0 \) d’après (**). Ceci est vrai pour tout \( n \in \mathbb{N} \) , donc \( g \) est nulle.

The function \( \left\lbrack {0,1}\right\rbrack \times \left\lbrack {0,{2\pi }}\right\rbrack \rightarrow \mathbb{C}\;\left( {r, t}\right) \rightarrow g\left( {r{e}^{it}}\right) \) is continuous (because \( g \) is continuous on \( D \) ), and according to the theorem of continuity under the integral sign, the integral of (**) tends to \( {\int }_{0}^{2\pi }g\left( {e}^{it}\right) {e}^{-{int}}{dt} = 0 \) as \( r \rightarrow {1}^{ - } \) . We deduce \( {b}_{n} = 0 \) from (**). This is true for all \( n \in \mathbb{N} \) , therefore \( g \) is zero.

> En particulier, \( g\left( {1/n}\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . La forme de \( g \) montre donc qu’il existe \( k \) et une infinité d’entiers \( n \) pour lesquels \( f\left( {{e}^{ki\theta }/n}\right) = 0 \) . Comme \( f \) , la fonction \( z \mapsto f\left( {{e}^{ik\theta }z}\right) \) est la somme d'une série entière sur le disque unité. D'après le principe de zéros isolés (voir le théorème 3 page 250) on en déduit que \( f\left( {{e}^{ik\theta }z}\right) = 0 \) pour tout \( z \in D \) . La fonction \( f \) est donc nulle.

In particular, \( g\left( {1/n}\right) = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) . The form of \( g \) therefore shows that there exists \( k \) and an infinite number of integers \( n \) for which \( f\left( {{e}^{ki\theta }/n}\right) = 0 \) . Since \( f \) , the function \( z \mapsto f\left( {{e}^{ik\theta }z}\right) \) is the sum of a power series on the unit disk. According to the isolated zeros principle (see theorem 3 on page 250), we deduce that \( f\left( {{e}^{ik\theta }z}\right) = 0 \) for all \( z \in D \) . The function \( f \) is therefore zero.

> Remarque. On aurait pu utiliser l'égalité de Parseval au lieu de la formule de Cauchy.

Remark. One could have used Parseval's identity instead of Cauchy's formula.

> Problem 21 (THÉORÉME DE BIEBERBACH, CAS RÉEL). Soit \( f\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) la somme d’une série entière de rayon de convergence 1,à coefficients réels, telle que \( {a}_{0} = 0 \) et \( {a}_{1} = 1 \) . On suppose que \( f \) est injective sur le domaine \( D = \{ z \in \mathbb{C} : \left| z\right| < 1\} \) . On veut montrer que \( \left| {a}_{n}\right| \leq n \) pour \( n \geq 1 \) .

Problem 21 (BIEBERBACH'S THEOREM, REAL CASE). Let \( f\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) be the sum of a power series with radius of convergence 1, with real coefficients, such that \( {a}_{0} = 0 \) and \( {a}_{1} = 1 \) . Suppose that \( f \) is injective on the domain \( D = \{ z \in \mathbb{C} : \left| z\right| < 1\} \) . We want to show that \( \left| {a}_{n}\right| \leq n \) for \( n \geq 1 \) .

> a) Montrer que pour tout \( r \) tel que \( 0 < r < 1 \) , on a

a) Show that for all \( r \) such that \( 0 < r < 1 \) , we have

\[
\frac{\pi {a}_{n}{r}^{n}}{2} = {\int }_{0}^{\pi }\Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) \sin {n\theta d\theta }.\;\left( {\Im \left( u\right) \text{ désigne la partie imaginaire de }u}\right)
\]

b) Lorsque \( \theta \in \left\lbrack {0,\pi }\right\rbrack \) ,étudier le signe de \( \Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) \) , puis montrer l’inégalité \( \left| {\sin \left( {n\theta }\right) }\right| \leq \; n\left| {\sin \theta }\right| \) . En déduire \( \left| {a}_{n}\right| \leq n \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> b) When \( \theta \in \left\lbrack {0,\pi }\right\rbrack \) , study the sign of \( \Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) \) , then show the inequality \( \left| {\sin \left( {n\theta }\right) }\right| \leq \; n\left| {\sin \theta }\right| \) . Deduce \( \left| {a}_{n}\right| \leq n \) for all \( n \in {\mathbb{N}}^{ * } \) .

c) Montrer que l'inégalité précédente est la meilleure possible.

> c) Show that the previous inequality is the best possible.

Solution. a) Soit \( r \in \rbrack 0,1\left\lbrack \right. \) . On a \( {a}_{k} \in \mathbb{R} \) pour tout \( k \in \mathbb{N} \) donc \( \Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{a}_{k}{r}^{k}\sin {k\theta } \) , et comme cette série est normalement convergente, on peut l'intégrer terme à terme ce qui donne

> Solution. a) Let \( r \in \rbrack 0,1\left\lbrack \right. \) . We have \( {a}_{k} \in \mathbb{R} \) for all \( k \in \mathbb{N} \) so \( \Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{a}_{k}{r}^{k}\sin {k\theta } \) , and since this series is normally convergent, we can integrate it term by term, which gives

\[
{\int }_{0}^{\pi }\Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) \sin {n\theta d\theta } = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{a}_{k}{r}^{k}{\int }_{0}^{\pi }\sin {k\theta }\sin {n\theta d\theta }.
\]

Il suffit ensuite de remarquer que \( \sin {k\theta }\sin {n\theta } = \frac{1}{2}\left( {\cos \left( {k - n}\right) \theta - \cos \left( {k + n}\right) \theta }\right) \) , et comme \( {\int }_{0}^{\pi }\cos {p\theta d\theta } = 0 \) si \( p \neq 0, = \pi \) sinon, on en déduit \( {\int }_{0}^{\pi }\sin {k\theta }\sin {n\theta d\theta } = 0 \) si \( k \neq n, = \pi /2 \) si \( k = n \) , d’où le résultat demandé.

> It then suffices to note that \( \sin {k\theta }\sin {n\theta } = \frac{1}{2}\left( {\cos \left( {k - n}\right) \theta - \cos \left( {k + n}\right) \theta }\right) \) , and since \( {\int }_{0}^{\pi }\cos {p\theta d\theta } = 0 \) if \( p \neq 0, = \pi \) otherwise, we deduce \( {\int }_{0}^{\pi }\sin {k\theta }\sin {n\theta d\theta } = 0 \) if \( k \neq n, = \pi /2 \) if \( k = n \) , hence the requested result.

b) On a \( f\left( z\right) \in \mathbb{R} \) si et seulement si \( f\left( z\right) = \overline{f\left( z\right) } = f\left( \bar{z}\right) \) , et comme \( f \) est injective, ceci n’est possible que si \( z = \bar{z} \) , c’est-à-dire \( z \in \mathbb{R} \) . Ainsi, \( \Im \left( {f\left( z\right) }\right) \) ne s’annule pas sur le connexe \( {D}^{ + } = \{ z \in D,\Re \left( z\right) > 0\} \) et comme l’image d’un connexe par une application continue est un connexe, \( \Im \left( {f\left( z\right) }\right) \) garde un signe constant sur \( {D}^{ + } \) . Comme \( f\left( z\right) = z + o\left( z\right) \) lorsque \( z \rightarrow 0 \) , on en déduit que \( \Im \left( {f\left( z\right) }\right) > 0 \) sur un voisinage de 0 dans \( {D}^{ + } \) , donc dans \( {D}^{ + } \) tout entier.

> b) We have \( f\left( z\right) \in \mathbb{R} \) if and only if \( f\left( z\right) = \overline{f\left( z\right) } = f\left( \bar{z}\right) \), and since \( f \) is injective, this is only possible if \( z = \bar{z} \), that is to say \( z \in \mathbb{R} \). Thus, \( \Im \left( {f\left( z\right) }\right) \) does not vanish on the connected set \( {D}^{ + } = \{ z \in D,\Re \left( z\right) > 0\} \) and since the image of a connected set under a continuous map is connected, \( \Im \left( {f\left( z\right) }\right) \) maintains a constant sign on \( {D}^{ + } \). As \( f\left( z\right) = z + o\left( z\right) \) when \( z \rightarrow 0 \), we deduce that \( \Im \left( {f\left( z\right) }\right) > 0 \) on a neighborhood of 0 in \( {D}^{ + } \), and therefore in \( {D}^{ + } \) entirely.

L’inégalité \( \left| {\sin \left( {n\theta }\right) }\right| \leq n\left| {\sin \theta }\right| \) pour \( \theta \in \mathbb{R} \) se montre facilement par récurrence sur \( n \) à partir de l’identité \( \sin \left( {n + 1}\right) \theta = \sin {n\theta }\cos \theta + \sin \theta \cos {n\theta } \) .

> The inequality \( \left| {\sin \left( {n\theta }\right) }\right| \leq n\left| {\sin \theta }\right| \) for \( \theta \in \mathbb{R} \) is easily shown by induction on \( n \) starting from the identity \( \sin \left( {n + 1}\right) \theta = \sin {n\theta }\cos \theta + \sin \theta \cos {n\theta } \).

On utilise maintenant l'identité démontrée dans la question précédente, qui implique

> We now use the identity proven in the previous question, which implies

\[
\left| {a}_{n}\right|  \leq  \frac{2}{\pi {r}^{n}}{\int }_{0}^{\pi }\left| {\Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) }\right|  \cdot  \left| {\sin {n\theta }}\right| {d\theta } \leq  \frac{2}{\pi {r}^{n}}{\int }_{0}^{\pi }\Im \left( {f\left( {r{e}^{i\theta }}\right) }\right) n\sin {\theta d\theta } = n{a}_{1} = n
\]

où nous avons une nouvelle fois utilisé l’identité de a) pour \( n = 1 \) .

> where we have once again used the identity from a) for \( n = 1 \).

c) L’inégalité est bien la meilleure possible, car on vérifie facilement que \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n{z}^{n} = z/{\left( 1 - z\right) }^{2} \) est injective sur \( D \) .

> c) The inequality is indeed the best possible, as one easily verifies that \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n{z}^{n} = z/{\left( 1 - z\right) }^{2} \) is injective on \( D \).

Remarque. Le théorème de Bieberbach dans le cas général s'exprime sans la condition que les coefficients \( {a}_{n} \) soient réels. Il a été annoncé comme une conjecture en 1916 par Ludwig Bieberbach, qui avait démontré uniquement \( \left| {a}_{2}\right| \leq 2 \) . Après de nombreux résultats partiels, le cas général n'a été démontré qu'en 1984 par Louis de Branges.

> Remark. The Bieberbach theorem in the general case is expressed without the condition that the coefficients \( {a}_{n} \) be real. It was announced as a conjecture in 1916 by Ludwig Bieberbach, who had only proven \( \left| {a}_{2}\right| \leq 2 \). After numerous partial results, the general case was only proven in 1984 by Louis de Branges.

Problem 22 (FONCTION ZÉTA DE RIEMANN). Pour tout \( s > 1 \) , on pose

> Problem 22 (RIEMANN ZETA FUNCTION). For all \( s > 1 \), we define

\[
\zeta \left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}}.
\]

a) Montrer que \( \zeta \) définit une fonction de classe \( {\mathcal{C}}^{\infty } \) sur ] \( 1, + \infty \) [ et exprimer ses dérivées successives.

> a) Show that \( \zeta \) defines a function of class \( {\mathcal{C}}^{\infty } \) on ] \( 1, + \infty \) [ and express its successive derivatives.

b) Montrer que \( \zeta \) converge en \( + \infty \) et que lorsque \( s \rightarrow {1}^{ + },\zeta \left( s\right) = 1/\left( {s - 1}\right) + \gamma + o\left( 1\right) \) (où \( \gamma \) désigne la constante d’Euler).

> b) Show that \( \zeta \) converges at \( + \infty \) and that as \( s \rightarrow {1}^{ + },\zeta \left( s\right) = 1/\left( {s - 1}\right) + \gamma + o\left( 1\right) \) (where \( \gamma \) denotes the Euler constant).

c) On note \( {\left( {p}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) la suite des nombres premiers rangés dans l’ordre croissant. Montrer la formule (identité due à Euler)

> c) Let \( {\left( {p}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be the sequence of prime numbers arranged in increasing order. Show the formula (identity due to Euler)

\[
\forall s > 1,\;\zeta \left( s\right)  = \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left( \frac{1}{1 - {p}_{n}^{-s}}\right) \;\left( {\mathop{\prod }\limits_{{n = 1}}^{{+\infty }} = \mathop{\lim }\limits_{{N \rightarrow   + \infty }}\mathop{\prod }\limits_{{n = 1}}^{N}}\right) .
\]

d) Montrer que la série \( \sum 1/{p}_{n} \) diverge.

> d) Show that the series \( \sum 1/{p}_{n} \) diverges.

Solution. a) Pour démontrer que \( \zeta \) est de classe \( {\mathcal{C}}^{\infty } \) sur ] \( 1, + \infty \left\lbrack \text{ , il suffit de montrer qu’elle est }\right\rbrack \) de classe \( {\mathcal{C}}^{\infty } \) sur \( \lbrack a, + \infty \lbrack \) pour tout \( a > 1 \) .

> Solution. a) To prove that \( \zeta \) is of class \( {\mathcal{C}}^{\infty } \) on ] \( 1, + \infty \left\lbrack \text{ , il suffit de montrer qu’elle est }\right\rbrack \) of class \( {\mathcal{C}}^{\infty } \) on \( \lbrack a, + \infty \lbrack \) for all \( a > 1 \) .

Fixons donc \( a > 1 \) . La fonction \( \zeta \) est limite simple de la série de fonctions \( \sum 1/{n}^{s} \) sur \( \rbrack 1, + \infty \left\lbrack \right. \) . Pour tout \( p \in {\mathbb{N}}^{ * } \) , montrons que la série des dérivées \( p \) -ièmes \( \sum {\left( -1\right) }^{p}{\log }^{p}n/{n}^{s} \) converge uniformément sur \( \lbrack a, + \infty \lbrack \) . Pour \( p \in {\mathbb{N}}^{ * } \) fixé, on a, en écrivant \( a = 1 + {2h}\left( {h > 0}\right) \)

> Let us fix \( a > 1 \) . The function \( \zeta \) is the pointwise limit of the series of functions \( \sum 1/{n}^{s} \) on \( \rbrack 1, + \infty \left\lbrack \right. \) . For all \( p \in {\mathbb{N}}^{ * } \) , let us show that the series of \( p \) -th derivatives \( \sum {\left( -1\right) }^{p}{\log }^{p}n/{n}^{s} \) converges uniformly on \( \lbrack a, + \infty \lbrack \) . For a fixed \( p \in {\mathbb{N}}^{ * } \) , we have, by writing \( a = 1 + {2h}\left( {h > 0}\right) \)

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{\log }^{p}n}{{n}^{h}} = 0\;\text{ donc }\;\frac{{\log }^{p}n}{{n}^{a}} = \frac{{\log }^{p}n}{{n}^{h}}\frac{1}{{n}^{1 + h}} = o\left( \frac{1}{{n}^{1 + h}}\right) ,
\]

donc la série \( \sum {\log }^{p}n/{n}^{a} \) converge. Comme \( {\log }^{p}n/{n}^{s} \leq {\log }^{p}n/{n}^{a} \) pour tout \( s \geq a \) , on en déduit que \( \sum {\left( -1\right) }^{p}{\log }^{p}n/{n}^{s} \) converge normalement donc uniformément sur \( \lbrack a, + \infty \lbrack \) . Ainsi (voir le premier alinéa de la remarque 5 page 234), la fonction \( \zeta \) est de classe \( {\mathcal{C}}^{\infty } \) sur \( \lbrack a, + \infty \lbrack \) et sur cet

> therefore the series \( \sum {\log }^{p}n/{n}^{a} \) converges. Since \( {\log }^{p}n/{n}^{s} \leq {\log }^{p}n/{n}^{a} \) for all \( s \geq a \), we deduce that \( \sum {\left( -1\right) }^{p}{\log }^{p}n/{n}^{s} \) converges normally and therefore uniformly on \( \lbrack a, + \infty \lbrack \). Thus (see the first paragraph of remark 5 on page 234), the function \( \zeta \) is of class \( {\mathcal{C}}^{\infty } \) on \( \lbrack a, + \infty \lbrack \) and on this

intervalle, on a

> interval, we have

\[
\forall p \in  {\mathbb{N}}^{ * },\;{\zeta }^{\left( p\right) }\left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{\log }^{p}n}{{n}^{s}}.
\]

b) On commence par une classique comparaison série-intégrale,

> b) We begin with a classic series-integral comparison,

\[
\forall s > 1,\forall n \in  {\mathbb{N}}^{ * },\;\frac{1}{{\left( n + 1\right) }^{s}} \leq  {\int }_{n}^{n + 1}\frac{dt}{{t}^{s}} \leq  \frac{1}{{n}^{s}}\;\text{ donc }\;\zeta \left( s\right)  - 1 \leq  {\int }_{1}^{+\infty }\frac{dt}{{t}^{s}} = \frac{1}{s - 1} \leq  \zeta \left( s\right)
\]

(par sommation sur \( n \geq 1 \) de la première inégalité). Ceci entraîne \( 1/\left( {s - 1}\right) \leq \zeta \left( s\right) \leq 1 + 1/\left( {s - 1}\right) \) pour tout \( s > 1 \) . On en déduit que \( \zeta \left( s\right) \sim 1/\left( {s - 1}\right) \) lorsque \( s \rightarrow {1}^{ + } \) , et comme \( 1 \leq \zeta \left( s\right) \leq \; 1 + 1/\left( {s - 1}\right) ,\zeta \) converge vers1en \( + \infty \) .

> (by summation over \( n \geq 1 \) of the first inequality). This implies \( 1/\left( {s - 1}\right) \leq \zeta \left( s\right) \leq 1 + 1/\left( {s - 1}\right) \) for all \( s > 1 \). We deduce that \( \zeta \left( s\right) \sim 1/\left( {s - 1}\right) \) as \( s \rightarrow {1}^{ + } \), and since \( 1 \leq \zeta \left( s\right) \leq \; 1 + 1/\left( {s - 1}\right) ,\zeta \) converges to 1 at \( + \infty \).

Pour obtenir le second terme du développement asymptotique de \( \zeta \) en \( s = {1}^{ + } \) , il faut raffiner la technique. Comme \( 1/\left( {s - 1}\right) = {\int }_{1}^{+\infty }{dt}/{t}^{s} \) , on a

> To obtain the second term of the asymptotic expansion of \( \zeta \) at \( s = {1}^{ + } \), the technique must be refined. Since \( 1/\left( {s - 1}\right) = {\int }_{1}^{+\infty }{dt}/{t}^{s} \), we have

\[
\forall s > 1,\;\zeta \left( s\right)  - \frac{1}{s - 1} = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{u}_{n}\left( s\right) \;\text{ où }\;{u}_{n}\left( s\right)  = \frac{1}{{n}^{s}} - {\int }_{n}^{n + 1}\frac{dt}{{t}^{s}}.
\]

(*)

> Or

\[
\forall s \in  \left\lbrack  {1,2}\right\rbrack  ,\;0 \leq  {u}_{n}\left( s\right)  \leq  \frac{1}{{n}^{s}} - \frac{1}{{\left( n + 1\right) }^{s}} = {\int }_{n}^{n + 1}\frac{sdt}{{t}^{s + 1}} \leq  2{\int }_{n}^{n + 1}\frac{dt}{{t}^{2}}.
\]

On en conclut que la série de fonctions \( \sum {u}_{n} \) converge normalement sur \( \left\lbrack {1,2}\right\rbrack \) , donc que sa somme est continue sur \( \left\lbrack {1,2}\right\rbrack \) , en particulier en \( {1}^{ + } \) . On en déduit

> We conclude that the series of functions \( \sum {u}_{n} \) converges normally on \( \left\lbrack {1,2}\right\rbrack \), and therefore its sum is continuous on \( \left\lbrack {1,2}\right\rbrack \), in particular at \( {1}^{ + } \). We deduce

\[
\mathop{\lim }\limits_{{s \rightarrow  {1}^{ + }}}\zeta \left( s\right)  - \frac{1}{s - 1} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k}\left( 1\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}1 + \frac{1}{2} + \cdots  + \frac{1}{n} - \log \left( {n + 1}\right)  = \gamma ,
\]

d'où le résultat.

> hence the result.

c) Si \( s > 1 \) , on a \( \log {\left( 1 - {p}_{n}^{-s}\right) }^{-1} \sim {p}_{n}^{-s} \leq 1/{n}^{-s} \) lorsque \( n \rightarrow + \infty \) , donc \( \mathop{\sum }\limits_{n}\log {\left( 1 - {p}_{n}^{-s}\right) }^{-1} \) converge, ce qui assure l’existence du produit infini pour tout \( s > 1 \) . L’idée dans ce qui suit repose sur le fait que pour tout \( k \) et pour tout \( s > 1 \) , on a \( {\left( 1 - {p}_{k}^{-s}\right) }^{-1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{p}_{k}^{-{ns}} \) .

> c) If \( s > 1 \), we have \( \log {\left( 1 - {p}_{n}^{-s}\right) }^{-1} \sim {p}_{n}^{-s} \leq 1/{n}^{-s} \) as \( n \rightarrow + \infty \), so \( \mathop{\sum }\limits_{n}\log {\left( 1 - {p}_{n}^{-s}\right) }^{-1} \) converges, which ensures the existence of the infinite product for all \( s > 1 \). The idea in what follows relies on the fact that for all \( k \) and for all \( s > 1 \), we have \( {\left( 1 - {p}_{k}^{-s}\right) }^{-1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{p}_{k}^{-{ns}} \).

Pour tous les entiers naturels non nuls \( m \) et \( M \) , pour tout \( s > 1 \) , on a

> For all non-zero natural integers \( m \) and \( M \), for all \( s > 1 \), we have

\[
\mathop{\prod }\limits_{{k = 1}}^{m}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{M}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right)  = \mathop{\sum }\limits_{{0 \leq  {i}_{1},\ldots ,{i}_{m} \leq  M}}\frac{1}{{\left( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}}\right) }^{s}}.
\]

\( \left( {* * }\right) \)

> Maintenant, donnons nous \( N \in {\mathbb{N}}^{ * } \) . Soit \( {p}_{{m}_{0}} \) le plus grand nombre premier \( {p}_{i} \) et \( {M}_{0} \) la plus grande des puissances \( {i}_{k} \) apparaissant dans toutes les décompositions en facteurs premiers des \( N \) premiers entiers \( 1,\ldots , N \) . Considérons \( m \geq {m}_{0} \) et \( M \geq {M}_{0} \) . Tous les entiers compris entre 1 et \( N \) se retrouvent dans les entiers \( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}}\left( {0 \leq {i}_{1},\ldots ,{i}_{m} \leq M}\right) \) , donc le dernier terme de (**) est supérieur à \( \mathop{\sum }\limits_{{n = 1}}^{N}1/{n}^{s} \) . Par ailleurs, les nombres \( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}} \) représentent des entiers distincts (unicité de la décomposition en facteurs premiers), et finalement, (**) montre

Now, let us define \( N \in {\mathbb{N}}^{ * } \) . Let \( {p}_{{m}_{0}} \) be the largest prime number \( {p}_{i} \) and \( {M}_{0} \) be the largest of the powers \( {i}_{k} \) appearing in all prime factorizations of the first \( N \) integers \( 1,\ldots , N \) . Let us consider \( m \geq {m}_{0} \) and \( M \geq {M}_{0} \) . All integers between 1 and \( N \) are found within the integers \( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}}\left( {0 \leq {i}_{1},\ldots ,{i}_{m} \leq M}\right) \) , so the last term of (**) is greater than \( \mathop{\sum }\limits_{{n = 1}}^{N}1/{n}^{s} \) . Furthermore, the numbers \( {p}_{1}^{{i}_{1}}\cdots {p}_{m}^{{i}_{m}} \) represent distinct integers (uniqueness of prime factorization), and finally, (**) shows

\[
\forall s > 1,\;\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{s}} \leq  \mathop{\prod }\limits_{{k = 1}}^{m}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{M}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right)  \leq  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}} = \zeta \left( s\right) .
\]

Cette expression est valable pour tout \( m \geq {m}_{0} \) et pour tout \( M \geq {M}_{0} \) . En faisant tendre \( M \) puis \( m \) vers \( + \infty \) , on en déduit

> This expression is valid for any \( m \geq {m}_{0} \) and for any \( M \geq {M}_{0} \) . By letting \( M \) and then \( m \) tend towards \( + \infty \) , we deduce

\[
\forall s > 1,\;\mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{s}} \leq  \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{{i}_{k} = 0}}^{{+\infty }}\frac{1}{{\left( {p}_{k}^{{i}_{k}}\right) }^{s}}}\right)  = \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}\left( \frac{1}{1 - {p}_{k}^{-s}}\right)  \leq  \zeta \left( s\right) .
\]

Cette expression est valable indépendamment de \( N \in {\mathbb{N}}^{ * } \) , on peut donc faire tendre \( N \) vers \( + \infty \) , ce qui fournit l'égalité voulue.

> This expression is valid independently of \( N \in {\mathbb{N}}^{ * } \) , so we can let \( N \) tend towards \( + \infty \) , which provides the desired equality.

d) Raisonnons par l’absurde. Si \( \sum 1/{p}_{n} \) converge, l’équivalent \( \log \left\lbrack {\left( 1 - 1/{p}_{n}\right) }^{-1}\right\rbrack \sim 1/{p}_{n} \) montre que \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}{\left( 1 - 1/{p}_{n}\right) }^{-1} \) converge. Notons \( \ell \) la valeur de ce produit infini. Pour tout \( s > 1 \) ,

> d) Let us reason by contradiction. If \( \sum 1/{p}_{n} \) converges, the equivalent \( \log \left\lbrack {\left( 1 - 1/{p}_{n}\right) }^{-1}\right\rbrack \sim 1/{p}_{n} \) shows that \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}{\left( 1 - 1/{p}_{n}\right) }^{-1} \) converges. Let \( \ell \) denote the value of this infinite product. For any \( s > 1 \) ,

\[
\zeta \left( s\right)  = \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left( \frac{1}{1 - {p}_{n}^{-s}}\right)  \leq  \mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left( \frac{1}{1 - 1/{p}_{n}}\right)  = \ell ,
\]

ce qui montre que \( \zeta \) est majorée sur \( \rbrack 1, + \infty \lbrack \) . Ceci est impossible puisque l’on a montré \( \zeta \left( s\right) \sim \; 1/\left( {s - 1}\right) \) lorsque \( s \rightarrow {1}^{ + } \) , d’où le résultat.

> which shows that \( \zeta \) is bounded on \( \rbrack 1, + \infty \lbrack \) . This is impossible since we have shown \( \zeta \left( s\right) \sim \; 1/\left( {s - 1}\right) \) when \( s \rightarrow {1}^{ + } \) , hence the result.

Remarque. Le résultat de c) est généralisé au domaine complexe dans l'annexe C, et constitue une des clés permettant de démontrer le théorème des nombres premiers.

> Remark. The result of c) is generalized to the complex domain in Appendix C, and constitutes one of the keys to proving the prime number theorem.

- On peut montrer que \( \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 - 1/{p}_{k}}\right)  \sim  {e}^{-\gamma }/\log n \) où \( \gamma \) est la constante d’Euler (formule de Mertens). On en déduit \( \mathop{\sum }\limits_{{k = 1}}^{n}1/{p}_{k} \sim  \log \left( {\log n}\right) \) lorsque \( n \rightarrow   + \infty \) . Cette dernière estimation est aussi une conséquence du théorème des nombres premiers (voir annex C) puisque ce dernier entraîne \( {p}_{n} \sim  n\log n \) .

> - We can show that \( \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 - 1/{p}_{k}}\right)  \sim  {e}^{-\gamma }/\log n \) where \( \gamma \) is the Euler constant (Mertens' formula). We deduce \( \mathop{\sum }\limits_{{k = 1}}^{n}1/{p}_{k} \sim  \log \left( {\log n}\right) \) when \( n \rightarrow   + \infty \) . This last estimate is also a consequence of the prime number theorem (see Appendix C) since the latter implies \( {p}_{n} \sim  n\log n \) .

- A partir du développement en série entière de la fonction \( x \mapsto  {u}_{n}\left( {1 + x}\right) \) et de l’expression (*) on peut montrer que pour tout \( x > 0 \) on a le développement en série entière

> - From the power series expansion of the function \( x \mapsto  {u}_{n}\left( {1 + x}\right) \) and the expression (*) we can show that for any \( x > 0 \) we have the power series expansion

\[
\zeta \left( {1 + x}\right)  - \frac{1}{x} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{p}{\gamma }_{p}}{p!}{x}^{p},\;{\gamma }_{p} = \mathop{\lim }\limits_{{k \rightarrow   + \infty }}\left( {\frac{{\log }^{p}\left( 1\right) }{1} + \cdots  + \frac{{\log }^{p}\left( k\right) }{k} - \frac{{\log }^{p + 1}k}{p + 1}}\right) .
\]

On a \( {\gamma }_{0} = \gamma \) et les termes \( {\gamma }_{p} \) pour \( p \geq 1 \) sont des généralisations de la constante d’Euler.

> We have \( {\gamma }_{0} = \gamma \) and the terms \( {\gamma }_{p} \) for \( p \geq 1 \) are generalizations of Euler's constant.

PROBLÉME 23 (PREUVE DU THÉORÉME DE WEIERSTRASS PAR LA CONVOLUTION). On note \( \mathcal{E} \) l’e.v des fonctions continues de \( \mathbb{R} \) dans \( \mathbb{C} \) et nulles en dehors d’un compact. On muni \( \mathcal{E} \) de la loi de convolution \( \star \) en définissant, pour tout \( \left( {f, g}\right) \in {\mathcal{E}}^{2} \) la convolée

> PROBLEM 23 (PROOF OF THE WEIERSTRASS THEOREM VIA CONVOLUTION). Let \( \mathcal{E} \) be the vector space of continuous functions from \( \mathbb{R} \) to \( \mathbb{C} \) that vanish outside a compact set. We equip \( \mathcal{E} \) with the convolution law \( \star \) by defining, for all \( \left( {f, g}\right) \in {\mathcal{E}}^{2} \), the convolution

\[
f \star  g : \mathbb{R} \rightarrow  \mathbb{C}\;x \mapsto  {\int }_{-\infty }^{+\infty }f\left( {x - t}\right) g\left( t\right) {dt}.
\]

1/ a) Montrer que la loi \( \star \) est commutative et distributive par rapport à l’addition. b) (Séquences de Dirac.) On appelle séquence de Dirac (on dit encore approximation de l’identité) toute suite \( \left( {\chi }_{n}\right) \) de fonctions positives de \( \mathcal{E} \) vérifiant

> 1/ a) Show that the law \( \star \) is commutative and distributive with respect to addition. b) (Dirac sequences.) A Dirac sequence (also called an approximation of the identity) is any sequence \( \left( {\chi }_{n}\right) \) of positive functions in \( \mathcal{E} \) satisfying

\[
\forall n \in  \mathbb{N},\;{\int }_{-\infty }^{+\infty }{\chi }_{n}\left( t\right) {dt} = 1,\;\text{ et }\;\forall \alpha  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{\left| t\right|  \geq  \alpha }{\chi }_{n}\left( t\right) {dt} = 0
\]

( \( {\int }_{\left| t\right| \geq \alpha } \) signifie \( {\int }_{-\infty }^{-\alpha } + {\int }_{\alpha }^{+\infty } \) ). Soit \( \left( {\chi }_{n}\right) \) une telle suite et soit \( f \in \mathcal{E} \) . Montrer que la suite de fonctions \( {\left( f \star {\chi }_{n}\right) }_{n \in \mathbb{N}} \) converge uniformément vers \( f \) sur \( \mathbb{R} \) .

> ( \( {\int }_{\left| t\right| \geq \alpha } \) means \( {\int }_{-\infty }^{-\alpha } + {\int }_{\alpha }^{+\infty } \) ). Let \( \left( {\chi }_{n}\right) \) be such a sequence and let \( f \in \mathcal{E} \) . Show that the sequence of functions \( {\left( f \star {\chi }_{n}\right) }_{n \in \mathbb{N}} \) converges uniformly to \( f \) on \( \mathbb{R} \) .

2 / Pour tout \( n \in \mathbb{N} \) , on pose

> 2 / For all \( n \in \mathbb{N} \) , we define

\[
{a}_{n} = {\int }_{-1}^{1}{\left( 1 - {t}^{2}\right) }^{n}{dt}\;\text{ et }\;{p}_{n} : \mathbb{R} \rightarrow  \mathbb{C}\;t \mapsto  \left\{  \begin{array}{ll} {\left( 1 - {t}^{2}\right) }^{n}/{a}_{n} & \text{ si }\;\left| t\right|  \leq  1 \\  0 & \text{ sinon. } \end{array}\right.
\]

a) Montrer que \( \left( {p}_{n}\right) \) est une séquence de Dirac.

> a) Show that \( \left( {p}_{n}\right) \) is a Dirac sequence.

b) Soit \( f \in \mathcal{E} \) , nulle en dehors de \( I = \left\lbrack {-1/2,1/2}\right\rbrack \) . Pour tout \( n \in \mathbb{N} \) , montrer que \( f \star {p}_{n} \) est une fonction polynôme. Conclure.

> b) Let \( f \in \mathcal{E} \) , vanishing outside \( I = \left\lbrack {-1/2,1/2}\right\rbrack \) . For all \( n \in \mathbb{N} \) , show that \( f \star {p}_{n} \) is a polynomial function. Conclude.

c) En déduire le théorème de Weierstrass : si \( J \) est un segment de \( \mathbb{R} \) et si \( f : J \rightarrow \mathbb{C} \) est continue, alors \( f \) est limite uniforme sur \( J \) d’une suite de fonctions polynôme.

> c) Deduce the Weierstrass theorem: if \( J \) is a segment of \( \mathbb{R} \) and if \( f : J \rightarrow \mathbb{C} \) is continuous, then \( f \) is the uniform limit on \( J \) of a sequence of polynomial functions.

Solution. 1/ a) La distributivité par rapport à l'addition de la loi \( \star \) est immédiate. Pour prouver qu’elle est commutative, il suffit d’effectuer le changement de variable \( u = x - t \) dans l’intégrale définissant \( f \star g \) .

> Solution. 1/ a) The distributivity of the law \( \star \) with respect to addition is immediate. To prove that it is commutative, it suffices to perform the change of variable \( u = x - t \) in the integral defining \( f \star g \) .

b) Fixons \( \varepsilon > 0 \) . La fonction \( f \) est continue et nulle en dehors d’un compact, elle est donc uniformément continue sur \( \mathbb{R} \) , donc

> b) Let us fix \( \varepsilon > 0 \) . The function \( f \) is continuous and vanishes outside a compact set, so it is uniformly continuous on \( \mathbb{R} \) , therefore

\[
\exists \eta  > 0,\forall \left( {x, y}\right)  \in  {\mathbb{R}}^{2},\left| {x - y}\right|  < \eta ,\;\left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  \varepsilon .
\]

Désignons par \( M \) un majorant de \( \left| f\right| \) sur \( \mathbb{R} \) . Choisissons \( N \in \mathbb{N} \) tel que \( {\int }_{\left| t\right| \geq \eta }{\chi }_{n}\left( t\right) {dt} < \varepsilon \) pour tout \( n \geq N \) . Comme \( {\int }_{-\infty }^{+\infty }{\chi }_{n}\left( t\right) {dt} = 1 \) , et que les fonctions \( {\chi }_{n} \) sont positives, on a pour tout \( n \geq N \)

> Let \( M \) denote an upper bound of \( \left| f\right| \) on \( \mathbb{R} \) . Choose \( N \in \mathbb{N} \) such that \( {\int }_{\left| t\right| \geq \eta }{\chi }_{n}\left( t\right) {dt} < \varepsilon \) for all \( n \geq N \) . Since \( {\int }_{-\infty }^{+\infty }{\chi }_{n}\left( t\right) {dt} = 1 \) , and the functions \( {\chi }_{n} \) are positive, we have for all \( n \geq N \)

\[
\forall x \in  \mathbb{R},\;\left| {f \star  {\chi }_{n}\left( x\right)  - f\left( x\right) }\right|  = \left| {{\int }_{-\infty }^{+\infty }\left\lbrack  {f\left( {x - t}\right)  - f\left( x\right) }\right\rbrack  {\chi }_{n}\left( t\right) {dt}}\right|
\]

\[
\leq  {\int }_{\left| t\right|  \geq  \eta }\left| {f\left( {x - t}\right)  - f\left( x\right) }\right| {\chi }_{n}\left( t\right) {dt} + {\int }_{-\eta }^{\eta }\left| {f\left( {x - t}\right)  - f\left( x\right) }\right| {\chi }_{n}\left( t\right) {dt}
\]

\[
\leq  {2M\varepsilon } + \varepsilon {\int }_{-\eta }^{\eta }{\chi }_{n}\left( t\right) {dt} \leq  {2M\varepsilon } + \varepsilon {\int }_{-\infty }^{+\infty }{\chi }_{n}\left( t\right) {dt} = \left( {{2M} + 1}\right) \varepsilon .
\]

Ceci suffit pour conclure.

> This is sufficient to conclude.

2 / a) On remarque que \( {\int }_{-\infty }^{+\infty }{p}_{n}\left( t\right) {dt} = {\int }_{-1}^{1}{p}_{n}\left( t\right) {dt} = 1 \) par définition de \( {a}_{n} \) . Par ailleurs,

> 2 / a) We note that \( {\int }_{-\infty }^{+\infty }{p}_{n}\left( t\right) {dt} = {\int }_{-1}^{1}{p}_{n}\left( t\right) {dt} = 1 \) by definition of \( {a}_{n} \) . Furthermore,

\[
\forall n \in  {\mathbb{N}}^{ * },\;{a}_{n} = 2{\int }_{0}^{1}{\left( 1 - {t}^{2}\right) }^{n}{dt} \geq  2{\int }_{0}^{1}t{\left( 1 - {t}^{2}\right) }^{n}{dt} = {\left\lbrack  \frac{-{\left( 1 - {t}^{2}\right) }^{n + 1}}{n + 1}\right\rbrack  }_{0}^{1} = \frac{1}{n + 1}
\]

donc si \( \alpha > 0\left( {\text{ et }\alpha < 1}\right) \) ,

> so if \( \alpha > 0\left( {\text{ et }\alpha < 1}\right) \) ,

\[
\forall n \in  {\mathbb{N}}^{ * },\;{\int }_{\left| t\right|  \geq  \alpha }{p}_{n}\left( t\right) {dt} = \frac{2}{{a}_{n}}{\int }_{\alpha }^{1}{\left( 1 - {t}^{2}\right) }^{n}{dt} \leq  \frac{2}{{a}_{n}}{\left( 1 - {\alpha }^{2}\right) }^{n} \leq  2\left( {n + 1}\right) {\left( 1 - {\alpha }^{2}\right) }^{n},
\]

et comme \( \left| {1 - {\alpha }^{2}}\right| < 1 \) , ceci suffit pour conclure que \( {\int }_{\left| t\right| \geq \alpha }{p}_{n}\left( t\right) {dt} \) tend vers 0 lorsque \( n \rightarrow + \infty \) . b) Pour montrer que \( f \star {p}_{n} \) est une fonction polynôme sur \( I \) , on commence par écrire

> and since \( \left| {1 - {\alpha }^{2}}\right| < 1 \) , this is sufficient to conclude that \( {\int }_{\left| t\right| \geq \alpha }{p}_{n}\left( t\right) {dt} \) tends to 0 as \( n \rightarrow + \infty \) . b) To show that \( f \star {p}_{n} \) is a polynomial function on \( I \) , we begin by writing

\[
\forall x \in  I,\;\left( {f \star  {p}_{n}}\right) \left( x\right)  = \left( {{p}_{n} \star  f}\right) \left( x\right)  = {\int }_{-1/2}^{1/2}{p}_{n}\left( {x - t}\right) f\left( t\right) {dt}.
\]

(*)

> Lorsque \( x \in I \) et \( t \in I \) , on a \( \left| {x - t}\right| \leq 1 \) donc \( {p}_{n}\left( {x - t}\right) = {\left( 1 - {\left( x - t\right) }^{2}\right) }^{n}/{a}_{n} \) , ce qui en développant s’écrit sous la forme \( \mathop{\sum }\limits_{{k = 0}}^{{2n}}{q}_{k}\left( t\right) {x}^{k} \) (où pour tout \( k,{q}_{k} \) est une fonction polynôme). En remplaçant dans (*), on en déduit

When \( x \in I \) and \( t \in I \) , we have \( \left| {x - t}\right| \leq 1 \) so \( {p}_{n}\left( {x - t}\right) = {\left( 1 - {\left( x - t\right) }^{2}\right) }^{n}/{a}_{n} \) , which, when expanded, is written in the form \( \mathop{\sum }\limits_{{k = 0}}^{{2n}}{q}_{k}\left( t\right) {x}^{k} \) (where for all \( k,{q}_{k} \) is a polynomial function). By substituting into (*), we deduce

\[
\forall x \in  I,\;\left( {f \star  {p}_{n}}\right) \left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{{2n}}\left( {{\int }_{-1/2}^{1/2}{q}_{k}\left( t\right) f\left( t\right) {dt}}\right) {x}^{k},
\]

qui est bien une fonction polynôme sur \( I \) .

> which is indeed a polynomial function on \( I \) .

Maintenant, on sait d’après \( 1/\mathrm{b} \) ) que \( \left( {f \star {p}_{n}}\right) \) converge uniformément vers \( f \) sur \( \mathbb{R} \) , en particulier sur \( I \) . En définitive, nous venons de montrer que \( f \) est limite uniforme sur \( I \) d’une suite de fonctions polynôme.

> Now, we know from \( 1/\mathrm{b} \) ) that \( \left( {f \star {p}_{n}}\right) \) converges uniformly to \( f \) on \( \mathbb{R} \) , in particular on \( I \) . Ultimately, we have just shown that \( f \) is the uniform limit on \( I \) of a sequence of polynomial functions.

c) Soit \( \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) une fonction continue. En considérant un intervalle plus grand \( \left\lbrack {c, d}\right\rbrack \) avec \( c < a, b < d \) , on prolonge \( f \) sur \( \left\lbrack {c, a}\right\rbrack \) (resp. sur \( \left\lbrack {b, d}\right\rbrack \) ) par une fonction affine prenant la valeur 0 en \( c \) et la valeur \( f\left( a\right) \) en \( a \) (resp. la valeur \( f\left( b\right) \) en \( b \) et la valeur 0 en \( d \) ). On prolonge ensuite \( f \) sur \( \mathbb{R} \) tout entier en prenant \( f\left( x\right) = 0 \) hors de \( \left\lbrack {c, d}\right\rbrack \) . Le prolongement ainsi construit de \( f \) est continu sur \( \mathbb{R} \) , nul en dehors d’un compact, donc \( f \in \mathcal{E} \) .

> c) Let \( \left\lbrack {a, b}\right\rbrack \) be a segment of \( \mathbb{R} \) and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{C} \) a continuous function. By considering a larger interval \( \left\lbrack {c, d}\right\rbrack \) with \( c < a, b < d \) , we extend \( f \) on \( \left\lbrack {c, a}\right\rbrack \) (resp. on \( \left\lbrack {b, d}\right\rbrack \) ) by an affine function taking the value 0 at \( c \) and the value \( f\left( a\right) \) at \( a \) (resp. the value \( f\left( b\right) \) at \( b \) and the value 0 at \( d \) ). We then extend \( f \) to the whole of \( \mathbb{R} \) by taking \( f\left( x\right) = 0 \) outside \( \left\lbrack {c, d}\right\rbrack \) . The extension of \( f \) thus constructed is continuous on \( \mathbb{R} \) , zero outside a compact set, therefore \( f \in \mathcal{E} \) .

On peut ensuite, en effectuant un changement de variable affine, se placer dans le cas où \( \left\lbrack {c, d}\right\rbrack = \left\lbrack {-1/2,1/2}\right\rbrack \) . La fonction \( f \) est alors limite uniforme de fonctions polynôme sur \( \left\lbrack {c, d}\right\rbrack \) d’après la question précédente, en particulier sur \( \left\lbrack {a, b}\right\rbrack \subset \left\lbrack {c, d}\right\rbrack \) .

> We can then, by performing an affine change of variable, place ourselves in the case where \( \left\lbrack {c, d}\right\rbrack = \left\lbrack {-1/2,1/2}\right\rbrack \) . The function \( f \) is then the uniform limit of polynomial functions on \( \left\lbrack {c, d}\right\rbrack \) according to the previous question, in particular on \( \left\lbrack {a, b}\right\rbrack \subset \left\lbrack {c, d}\right\rbrack \) .

Remarque. Une autre preuve de ce théorème fait l'objet de l'exercice 8 page 242.

> Remark. Another proof of this theorem is the subject of exercise 8 on page 242.

Problem 24. Dans ce problème, on pourra utiliser le théorème de Weierstrass (voir le problème précédent ou voir page 235).

> Problem 24. In this problem, one may use the Weierstrass theorem (see the previous problem or see page 235).

a) Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{C} \) une fonction continue, telle que pour tout \( n \in \mathbb{N},{\int }_{0}^{1}f\left( t\right) {t}^{n}{dt} = 0 \) . Montrer que \( f \) est la fonction nulle.

> a) Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{C} \) be a continuous function such that for all \( n \in \mathbb{N},{\int }_{0}^{1}f\left( t\right) {t}^{n}{dt} = 0 \) . Show that \( f \) is the zero function.

b) Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) une fonction continue telle que l’intégrale \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) existe. Montrer que pour tout \( n \in {\mathbb{N}}^{ * } \) , l’intégrale \( {I}_{n} = {\int }_{0}^{+\infty }f\left( t\right) {e}^{-{nt}}{dt} \) existe. Si \( {I}_{n} = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) , montrer que \( f \) est la fonction nulle.

> b) Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) be a continuous function such that the integral \( {\int }_{0}^{+\infty }f\left( t\right) {dt} \) exists. Show that for all \( n \in {\mathbb{N}}^{ * } \) , the integral \( {I}_{n} = {\int }_{0}^{+\infty }f\left( t\right) {e}^{-{nt}}{dt} \) exists. If \( {I}_{n} = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) , show that \( f \) is the zero function.

Solution. a) La propriété vérifiée par \( f \) entraîne par linéarité \( {\int }_{0}^{1}f\left( t\right) P\left( t\right) {dt} = 0 \) pour toute fonc-tion polynôme \( P \) . D'après le théorème de Weierstrass, il existe une suite de fonctions polynôme \( \left( {P}_{n}\right) \) qui converge uniformément vers \( \bar{f} \) sur \( \left\lbrack {0,1}\right\rbrack \) . De plus, \( f \) est bornée sur \( \left\lbrack {0,1}\right\rbrack \) (continue sur un compact) donc la suite de fonctions \( \left( {f{P}_{n}}\right) \) converge uniformément vers \( f\bar{f} = {\left| f\right| }^{2} \) sur \( \left\lbrack {0,1}\right\rbrack \) . Comme \( {\int }_{0}^{1}f\left( t\right) {P}_{n}\left( t\right) {dt} = 0 \) pour tout \( n \) , on en déduit

> Solution. a) The property satisfied by \( f \) implies by linearity \( {\int }_{0}^{1}f\left( t\right) P\left( t\right) {dt} = 0 \) for any polynomial function \( P \) . According to the Weierstrass theorem, there exists a sequence of polynomial functions \( \left( {P}_{n}\right) \) that converges uniformly to \( \bar{f} \) on \( \left\lbrack {0,1}\right\rbrack \) . Furthermore, \( f \) is bounded on \( \left\lbrack {0,1}\right\rbrack \) (continuous on a compact set), so the sequence of functions \( \left( {f{P}_{n}}\right) \) converges uniformly to \( f\bar{f} = {\left| f\right| }^{2} \) on \( \left\lbrack {0,1}\right\rbrack \) . Since \( {\int }_{0}^{1}f\left( t\right) {P}_{n}\left( t\right) {dt} = 0 \) for all \( n \) , we deduce

\[
{\int }_{0}^{1}{\left| f\left( t\right) \right| }^{2}{dt} = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\int }_{0}^{1}f\left( t\right) {P}_{n}\left( t\right) {dt} = 0.
\]

La fonction \( {\left| f\right| }^{2} \) est continue est positive, elle est donc nulle sur \( \left\lbrack {0,1}\right\rbrack \) d’où le résultat.

> The function \( {\left| f\right| }^{2} \) is continuous and positive, so it is zero on \( \left\lbrack {0,1}\right\rbrack \) , hence the result.

b) Considérons la primitive de \( f \) définie par \( F : x \mapsto {\int }_{0}^{x}f\left( t\right) {dt} \) . Si \( n \in {\mathbb{N}}^{ * } \) , une intégration par parties donne

> b) Consider the primitive of \( f \) defined by \( F : x \mapsto {\int }_{0}^{x}f\left( t\right) {dt} \) . If \( n \in {\mathbb{N}}^{ * } \) , integration by parts gives

\[
\forall X > 0,\;{\int }_{0}^{X}f\left( t\right) {e}^{-{nt}}{dt} = {\left\lbrack  F\left( t\right) {e}^{-{nt}}\right\rbrack  }_{0}^{X} + n{\int }_{0}^{X}F\left( t\right) {e}^{-{nt}}{dt} = F\left( X\right) {e}^{-{nX}} + n{\int }_{0}^{X}F\left( t\right) {e}^{-{nt}}{dt}.
\]

La fonction \( F \) est bornée car l’intégrale de \( f \) existe sur \( \mathbb{R} \) , ce qui en particulier entraîne l’existence de l’intégrale \( {J}_{n} = {\int }_{0}^{+\infty }F\left( t\right) {e}^{-{nt}}{dt} \) . Le membre de droite de la formule précédente converge donc lorsque \( X \rightarrow + \infty \) , ce qui assure l’existence de \( {I}_{n} \) et montre que \( {I}_{n} = n{J}_{n} \) .

> The function \( F \) is bounded because the integral of \( f \) exists on \( \mathbb{R} \) , which in particular implies the existence of the integral \( {J}_{n} = {\int }_{0}^{+\infty }F\left( t\right) {e}^{-{nt}}{dt} \) . The right-hand side of the previous formula therefore converges as \( X \rightarrow + \infty \) , which ensures the existence of \( {I}_{n} \) and shows that \( {I}_{n} = n{J}_{n} \) .

Si \( {I}_{n} = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) , on a donc \( {J}_{n} = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) , ce qui en effectuant le changement de variable \( u = {e}^{-t} \) entraîne

> If \( {I}_{n} = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) , we therefore have \( {J}_{n} = 0 \) for all \( n \in {\mathbb{N}}^{ * } \) , which, by performing the change of variable \( u = {e}^{-t} \) , leads to

\[
\forall n \in  {\mathbb{N}}^{ * },\;{J}_{n} = {\int }_{0}^{1}{u}^{n - 1}F\left( {-\log u}\right) {du} = 0.
\]

(*)

> La fonction continue \( \rbrack 0,1\rbrack \rightarrow \mathbb{C}\;u \mapsto F\left( {-\log u}\right) \) est prolongeable par continuité sur \( \left\lbrack {0,1}\right\rbrack \) car \( F \) converge vers \( + \infty \) (vers l’intégrale de \( f \) ). Ainsi, la formule (*) entraîne, d’après la question précédente, que \( F \) est la fonction nulle. Comme \( F \) est une primitive de la fonction continue \( f \) , on en déduit que \( f \) est la fonction nulle.

The continuous function \( \rbrack 0,1\rbrack \rightarrow \mathbb{C}\;u \mapsto F\left( {-\log u}\right) \) can be extended by continuity to \( \left\lbrack {0,1}\right\rbrack \) because \( F \) converges to \( + \infty \) (to the integral of \( f \)). Thus, formula (*) implies, according to the previous question, that \( F \) is the zero function. Since \( F \) is an antiderivative of the continuous function \( f \), we deduce that \( f \) is the zero function.

> Problem 25 (THÉORÉME DE FEJÉR). Soit \( f : \mathbb{R} \rightarrow \mathbb{C} \) une fonction continue et \( {2\pi } \) -périodique. Pour tout \( k \in \mathbb{Z} \) , on note \( {e}_{k} : \mathbb{R} \rightarrow \mathbb{C}\;x \mapsto {e}^{ikx} \) . Pour tout \( n \in \mathbb{N} \) , on définit les fonctions

Problem 25 (FEJÉR'S THEOREM). Let \( f : \mathbb{R} \rightarrow \mathbb{C} \) be a continuous and \( {2\pi } \)-periodic function. For all \( k \in \mathbb{Z} \), we denote \( {e}_{k} : \mathbb{R} \rightarrow \mathbb{C}\;x \mapsto {e}^{ikx} \). For all \( n \in \mathbb{N} \), we define the functions

\[
{S}_{n} = \mathop{\sum }\limits_{{k =  - n}}^{n}{c}_{k}\left( f\right) {e}_{k},\;{C}_{n} = \frac{{S}_{0} + {S}_{1} + \cdots  + {S}_{n}}{n + 1}
\]

(où les \( {c}_{k}\left( f\right) \) sont les coefficients de Fourier de \( f \) ) et

> (where the \( {c}_{k}\left( f\right) \) are the Fourier coefficients of \( f \)) and

\[
{\widetilde{S}}_{n} = \mathop{\sum }\limits_{{k =  - n}}^{n}{e}_{k},\;{\widetilde{C}}_{n} = \frac{{\widetilde{S}}_{0} + \cdots  + {\widetilde{S}}_{n}}{n + 1}.
\]

a) Vérifier que \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\widetilde{C}}_{n}\left( t\right) {dt} = 1 \) pour tout \( n \in \mathbb{N} \) , et montrer que pour tout \( \alpha \in \rbrack 0,\pi \lbrack \) la suite de fonction \( \left( {\widetilde{C}}_{n}\right) \) converge uniformément vers 0 sur \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \) .

> a) Verify that \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\widetilde{C}}_{n}\left( t\right) {dt} = 1 \) for all \( n \in \mathbb{N} \), and show that for all \( \alpha \in \rbrack 0,\pi \lbrack \) the sequence of functions \( \left( {\widetilde{C}}_{n}\right) \) converges uniformly to 0 on \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \).

b) En déduire le théorème de Fejér : la suite de fonctions \( \left( {C}_{n}\right) \) converge uniformément vers \( f \) sur \( \mathbb{R} \) .

> b) Deduce Fejér's theorem: the sequence of functions \( \left( {C}_{n}\right) \) converges uniformly to \( f \) on \( \mathbb{R} \).

Solution. a) On a \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{e}_{k}\left( t\right) {dt} = 0 \) pour tout \( k \in {\mathbb{Z}}^{ * } \) et \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{e}_{0}\left( t\right) {dt} = 1 \) . On en conclut

> Solution. a) We have \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{e}_{k}\left( t\right) {dt} = 0 \) for all \( k \in {\mathbb{Z}}^{ * } \) and \( \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{e}_{0}\left( t\right) {dt} = 1 \). We conclude

\[
\forall n \in  \mathbb{N},\;\frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\widetilde{S}}_{n}\left( t\right) {dt} = 1\;\text{ et }\;\frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\widetilde{C}}_{n}\left( t\right) {dt} = \frac{1}{n + 1}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\widetilde{S}}_{k}\left( t\right) {dt}}\right)  = 1.
\]

Pour montrer le résultat demandé sur la convergence uniforme de \( {\widetilde{C}}_{n} \) , on calcule d’abord \( {\widetilde{S}}_{n} \) . On reconnaît le noyau de Dirichlet, son calcul est classique et pour \( x \in \mathbb{R} \smallsetminus {2\pi }\mathbb{Z} \) on a

> To show the requested result on the uniform convergence of \( {\widetilde{C}}_{n} \), we first calculate \( {\widetilde{S}}_{n} \). We recognize the Dirichlet kernel; its calculation is standard and for \( x \in \mathbb{R} \smallsetminus {2\pi }\mathbb{Z} \) we have

\[
\forall n \in  \mathbb{N},\;{\widetilde{S}}_{n}\left( x\right)  = {e}^{-{inx}}\frac{{e}^{\left( {{2n} + 1}\right) {ix}} - 1}{{e}^{ix} - 1} = \frac{\sin \left( {\left( {n + 1/2}\right) x}\right) }{\sin \left( {x/2}\right) },
\]

et comme

> and since

\[
\forall n \in  \mathbb{N},\;\mathop{\sum }\limits_{{k = 0}}^{n}{e}^{\left( {k + 1/2}\right) {ix}} = {e}^{{ix}/2}\frac{{e}^{\left( {n + 1}\right) {ix}} - 1}{{e}^{ix} - 1} = {e}^{\left( {n + 1}\right) {ix}/2}\frac{\sin \left( {\left( {n + 1}\right) x/2}\right) }{\sin \left( {x/2}\right) },
\]

on en déduit, en prenant la partie imaginaire, que

> we deduce, by taking the imaginary part, that

\[
\forall n \in  \mathbb{N},\;{\widetilde{C}}_{n}\left( x\right)  = \frac{1}{n + 1}\mathop{\sum }\limits_{{k = 0}}^{n}{\widetilde{S}}_{k}\left( x\right)  = \frac{1}{n + 1}{\left( \frac{\sin \left( {\left( {n + 1}\right) x/2}\right) }{\sin \left( {x/2}\right) }\right) }^{2}.
\]

On en conclut que si \( 0 < \alpha < \pi \) ,

> We conclude that if \( 0 < \alpha < \pi \),

\[
\forall n \in  \mathbb{N},\forall x \in  \left\lbrack  {-\pi ,\pi }\right\rbrack  ,\left| x\right|  > \alpha ,\;\left| {{\widetilde{C}}_{n}\left( x\right) }\right|  \leq  \frac{1}{\left( {n + 1}\right) {\sin }^{2}\left( {\alpha /2}\right) }.
\]

Ceci suffit pour montrer que \( \left( {\widetilde{C}}_{n}\right) \) converge uniformément vers 0 sur \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \) . b) On remarque que pour tout \( n \in \mathbb{N} \) et pour tout \( x \in \mathbb{R} \) ,

> This is sufficient to show that \( \left( {\widetilde{C}}_{n}\right) \) converges uniformly to 0 on \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \). b) We note that for all \( n \in \mathbb{N} \) and for all \( x \in \mathbb{R} \),

\[
{S}_{n}\left( x\right)  = \frac{1}{2\pi }\mathop{\sum }\limits_{{k = 0}}^{n}\left( {{\int }_{-\pi }^{\pi }f\left( t\right) {e}^{-{ikt}}{dt}}\right) {e}^{ikx} = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( t\right) {\widetilde{S}}_{n}\left( {x - t}\right) {dt},
\]

donc \( {C}_{n}\left( x\right) = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( t\right) {\widetilde{C}}_{n}\left( {x - t}\right) {dt} \) . Ainsi \( {C}_{n} \) s’écrit comme un produit de convolution. Le changement de variable \( u = x - t \) , conjugué au caractère \( {2\pi } \) -périodique des intégrandes, entraîne

> thus \( {C}_{n}\left( x\right) = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( t\right) {\widetilde{C}}_{n}\left( {x - t}\right) {dt} \) . Thus \( {C}_{n} \) can be written as a convolution product. The change of variable \( u = x - t \) , combined with the \( {2\pi } \) -periodic nature of the integrands, leads to

\[
\forall x \in  \mathbb{R},\forall n \in  {\mathbb{N}}^{ * },\;{C}_{n}\left( x\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }f\left( {x - u}\right) {\widetilde{C}}_{n}\left( u\right) {du}.
\]

(*)

> Ceci étant, prouvons la convergence uniforme de \( \left( {C}_{n}\right) \) vers \( f \) . On procède comme dans la question 1/b) du problème 23. Soit \( \varepsilon > 0 \) . La fonction \( f \) est continue et \( {2\pi } \) -périodique, elle est donc uniformément continue sur \( \mathbb{R} \) ce qui entraîne

That being said, let us prove the uniform convergence of \( \left( {C}_{n}\right) \) to \( f \) . We proceed as in question 1/b) of problem 23. Let \( \varepsilon > 0 \) . The function \( f \) is continuous and \( {2\pi } \) -periodic, so it is uniformly continuous on \( \mathbb{R} \) which implies

\[
\exists \alpha  \in  \rbrack 0,\pi \lbrack ,\forall \left( {x, y}\right)  \in  {\mathbb{R}}^{2},\left| {x - y}\right|  < \alpha ,\;\left| {f\left( x\right)  - f\left( y\right) }\right|  < \varepsilon .
\]

En désignant par \( M \) un majorant de \( \left| f\right| \) sur \( \mathbb{R} \) , la formule (*) montre que pour tout \( x \in \mathbb{R} \) et pour tout \( n \in \mathbb{N} \) ,

> By denoting by \( M \) an upper bound of \( \left| f\right| \) on \( \mathbb{R} \) , formula (*) shows that for all \( x \in \mathbb{R} \) and for all \( n \in \mathbb{N} \) ,

\[
\left| {f\left( x\right)  - {C}_{n}\left( x\right) }\right|  = \left| {\frac{1}{2\pi }{\int }_{-\pi }^{\pi }\left( {f\left( {x - t}\right)  - f\left( x\right) }\right) {\widetilde{C}}_{n}\left( t\right) {dt}}\right|
\]

\[
\leq  \frac{1}{2\pi }{\int }_{\alpha  \leq  \left| t\right|  \leq  \pi }{2M}{\widetilde{C}}_{n}\left( t\right) {dt} + \frac{1}{2\pi }{\int }_{-\alpha }^{\alpha }\varepsilon {\widetilde{C}}_{n}\left( t\right) {dt} \leq  \frac{2M}{2\pi }{\int }_{\alpha  \leq  \left| t\right|  \leq  \pi }{\widetilde{C}}_{n}\left( t\right) {dt} + \varepsilon ,
\]

et comme \( \left( {\widetilde{C}}_{n}\right) \) converge uniformément vers 0 sur \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \) , il existe \( N \in \mathbb{N} \) tel que \( {\int }_{\alpha \leq \left| t\right| \leq \pi }{\widetilde{C}}_{n}\left( t\right) {dt} \leq \varepsilon \) pour tout \( n \geq N \) , de sorte que \( \left| {f\left( x\right) - {C}_{n}\left( x\right) }\right| \leq \left( {M/\pi }\right) \varepsilon + \varepsilon \) pour tout \( x \in \mathbb{R} \) et pour tout \( n \geq N \) . D’où le résultat

> and since \( \left( {\widetilde{C}}_{n}\right) \) converges uniformly to 0 on \( \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \left\lbrack {-\alpha ,\alpha }\right\rbrack \) , there exists \( N \in \mathbb{N} \) such that \( {\int }_{\alpha \leq \left| t\right| \leq \pi }{\widetilde{C}}_{n}\left( t\right) {dt} \leq \varepsilon \) for all \( n \geq N \) , so that \( \left| {f\left( x\right) - {C}_{n}\left( x\right) }\right| \leq \left( {M/\pi }\right) \varepsilon + \varepsilon \) for all \( x \in \mathbb{R} \) and for all \( n \geq N \) . Hence the result

Remarque. Le théorème de Fejér s'exprime en disant que la série de Fourier de toute fonction continue \( {2\pi } \) -périodique converge uniformément en moyenne de Césaro vers \( f \) . En particulier, toute fonction continue \( {2\pi } \) -périodique est limite uniforme de polynômes trigonométriques sur \( \mathbb{R} \) .

> Remark. Fejér's theorem states that the Fourier series of any continuous \( {2\pi } \) -periodic function converges uniformly in the Cesàro mean to \( f \) . In particular, any continuous \( {2\pi } \) -periodic function is a uniform limit of trigonometric polynomials on \( \mathbb{R} \) .

Problem 26. a) Soit \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) . Montrer que pour toute fonction \( f : \mathbb{R} \rightarrow \mathbb{C} \) continue et \( {2\pi } \) -périodique, on a

> Problem 26. a) Let \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) . Show that for any continuous and \( {2\pi } \) -periodic function \( f : \mathbb{R} \rightarrow \mathbb{C} \) , we have

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{S}_{n}\left( f\right)  = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( t\right) {dt}\text{ où }\;{S}_{n}\left( f\right)  = \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}f\left( {2\pi \alpha k}\right) .
\]

(*)

> (Indication. Utiliser le fait que \( f \) est limite uniforme de polynômes trigonométriques sur \( \mathbb{R} \) - voir le problème précédent.)

(Hint. Use the fact that \( f \) is a uniform limit of trigonometric polynomials on \( \mathbb{R} \) - see the previous problem.)

> b) En déduire que si \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) , l’ensemble \( \Gamma = \{ {n\alpha } - \left\lbrack {n\alpha }\right\rbrack , n \in \mathbb{N}\} \) (où \( \left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) pour tout \( x \in \mathbb{R} \) ) est dense dans \( \left\lbrack {0,1}\right\rbrack \) .

b) Deduce that if \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) , the set \( \Gamma = \{ {n\alpha } - \left\lbrack {n\alpha }\right\rbrack , n \in \mathbb{N}\} \) (where \( \left\lbrack x\right\rbrack \) denotes the integer part of \( x \) for all \( x \in \mathbb{R} \) ) is dense in \( \left\lbrack {0,1}\right\rbrack \) .

> Solution. a) Prouvons d’abord le résultat lorsque \( f \) est une fonction de la forme \( {e}_{p} : \mathbb{R} \rightarrow \; \mathbb{C}x \mapsto {e}^{ipx}\left( {p \in \mathbb{Z}}\right) \) . Si \( p \in {\mathbb{Z}}^{ * } \) , on a (compte tenu du fait que \( {e}^{2i\pi \alpha p} \neq 1 \) car \( \alpha \notin \mathbb{Q} \) )

Solution. a) Let us first prove the result when \( f \) is a function of the form \( {e}_{p} : \mathbb{R} \rightarrow \; \mathbb{C}x \mapsto {e}^{ipx}\left( {p \in \mathbb{Z}}\right) \) . If \( p \in {\mathbb{Z}}^{ * } \) , we have (given the fact that \( {e}^{2i\pi \alpha p} \neq 1 \) because \( \alpha \notin \mathbb{Q} \) )

\[
\forall n \in  {\mathbb{N}}^{ * },\;{S}_{n}\left( {e}_{p}\right)  = \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}{e}_{p}\left( {2\pi \alpha k}\right)  = \frac{1}{n}{e}^{2i\pi \alpha p}\frac{1 - {e}^{2i\pi \alpha pn}}{1 - {e}^{2i\pi \alpha p}}\;\text{ donc }\;\left| {{S}_{n}\left( {e}_{p}\right) }\right|  \leq  \frac{2}{n\left| {1 - {e}^{2i\pi \alpha p}}\right| },
\]

ce qui montre que \( {S}_{n}\left( {e}_{p}\right) \) tend vers \( 0 = \frac{1}{2\pi }{\int }_{0}^{2\pi }{e}_{p}\left( t\right) {dt} \) lorsque \( n \rightarrow + \infty \) . L’assertion (*) est donc vraie pour \( f = {e}_{p} \) lorsque \( p \in {\mathbb{Z}}^{ * } \) . Elle est trivialement vraie pour \( {e}_{0} \) .

> which shows that \( {S}_{n}\left( {e}_{p}\right) \) tends to \( 0 = \frac{1}{2\pi }{\int }_{0}^{2\pi }{e}_{p}\left( t\right) {dt} \) as \( n \rightarrow + \infty \) . The assertion (*) is therefore true for \( f = {e}_{p} \) when \( p \in {\mathbb{Z}}^{ * } \) . It is trivially true for \( {e}_{0} \) .

Finalement,(*) est vraie pour toute les fonctions \( {e}_{p} \) . Par linéarité, on en déduit qu’elle est vraie pour tout polynôme trigonométrique.

> Finally, (*) is true for all functions \( {e}_{p} \) . By linearity, we deduce that it is true for any trigonometric polynomial.

Considérons maintenant une fonction \( f : \mathbb{R} \rightarrow \mathbb{C} \) , continue et \( {2\pi } \) -périodique. Soit \( \varepsilon > \) 0 . On sait qu’il existe un polynôme trigonométrique \( P \) (voir le problème précédent) tel que \( \left| {f\left( x\right) - P\left( x\right) }\right| < \varepsilon \) pour tout \( x \in \mathbb{R} \) . Par ailleurs, nous avons montré que (*) était vrai pour \( P \) , donc il existe \( N \in \mathbb{N} \) tel que \( \left| {{S}_{n}\left( P\right) - \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( t\right) {dt}}\right| < \varepsilon \) pour tout \( n \geq N \) . On en déduit

> Now consider a function \( f : \mathbb{R} \rightarrow \mathbb{C} \) , continuous and \( {2\pi } \) -periodic. Let \( \varepsilon > \) 0 . We know that there exists a trigonometric polynomial \( P \) (see the previous problem) such that \( \left| {f\left( x\right) - P\left( x\right) }\right| < \varepsilon \) for all \( x \in \mathbb{R} \) . Furthermore, we have shown that (*) was true for \( P \) , so there exists \( N \in \mathbb{N} \) such that \( \left| {{S}_{n}\left( P\right) - \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( t\right) {dt}}\right| < \varepsilon \) for all \( n \geq N \) . We deduce from this

\[
\forall n \geq  N,\;\left| {{S}_{n}\left( f\right)  - \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( t\right) {dt}}\right|
\]

\[
\leq  \left| {{S}_{n}\left( f\right)  - {S}_{n}\left( P\right) }\right|  + \left| {{S}_{n}\left( P\right)  - \frac{1}{2\pi }{\int }_{0}^{2\pi }P\left( t\right) {dt}}\right|  + \frac{1}{2\pi }\left| {{\int }_{0}^{2\pi }\left\lbrack  {P\left( t\right)  - f\left( t\right) }\right\rbrack  {dt}}\right|  \leq  \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon }.
\]

D'où le résultat.

> Hence the result.

b) Raisonnons par l’absurde. Si \( \Gamma \) n’était pas dense dans \( \left\lbrack {0,1}\right\rbrack \) , il existerait \( a, b \in \mathbb{R},0 < a < \; b < 1 \) , tels que \( \Gamma \cap \left\lbrack {a, b}\right\rbrack = \varnothing \) . Il est facile de construire une fonction \( f \) positive, continue et \( {2\pi } \) -périodique sur \( \mathbb{R} \) telle que \( f\left( x\right) > 0 \) sur \( \rbrack {2\pi a},{2\pi b}\left\lbrack \right. \) et \( f\left( x\right) = 0 \) sur \( \left\lbrack {0,{2\pi a}}\right\rbrack \cup \left\lbrack {{2\pi b},{2\pi }}\right\rbrack \) . Comme pour tout \( n \in \mathbb{N} \) on a \( {n\alpha } - \left\lbrack {n\alpha }\right\rbrack \notin \left\lbrack {a, b}\right\rbrack \) , on a \( f\left( {2\pi \alpha k}\right) = 0 \) pour tout \( k \in \mathbb{N} \) donc \( {S}_{n}\left( f\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Ceci est en contradiction avec (*) car la fonction \( f \) vérifie \( {\int }_{0}^{2\pi }f\left( t\right) {dt} > 0 \) .

> b) Let us reason by contradiction. If \( \Gamma \) were not dense in \( \left\lbrack {0,1}\right\rbrack \) , there would exist \( a, b \in \mathbb{R},0 < a < \; b < 1 \) such that \( \Gamma \cap \left\lbrack {a, b}\right\rbrack = \varnothing \) . It is easy to construct a positive, continuous, and \( {2\pi } \) -periodic function \( f \) on \( \mathbb{R} \) such that \( f\left( x\right) > 0 \) on \( \rbrack {2\pi a},{2\pi b}\left\lbrack \right. \) and \( f\left( x\right) = 0 \) on \( \left\lbrack {0,{2\pi a}}\right\rbrack \cup \left\lbrack {{2\pi b},{2\pi }}\right\rbrack \) . As for every \( n \in \mathbb{N} \) we have \( {n\alpha } - \left\lbrack {n\alpha }\right\rbrack \notin \left\lbrack {a, b}\right\rbrack \) , we have \( f\left( {2\pi \alpha k}\right) = 0 \) for every \( k \in \mathbb{N} \) , hence \( {S}_{n}\left( f\right) = 0 \) for every \( n \in {\mathbb{N}}^{ * } \) . This contradicts (*) because the function \( f \) satisfies \( {\int }_{0}^{2\pi }f\left( t\right) {dt} > 0 \) .

Remarque. On retrouve facilement, avec la question b), que \( \alpha \mathbb{N} - \mathbb{N} \) est dense dans \( \mathbb{R} \) si \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) . C’est en substance le résultat démontré (par des moyens différents) dans la question c) de l'exercice 5 page 205.

> Remark. We easily find again, with question b), that \( \alpha \mathbb{N} - \mathbb{N} \) is dense in \( \mathbb{R} \) if \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) . This is essentially the result demonstrated (by different means) in question c) of exercise 5 on page 205.

Problem 27 (THÉORÉME TAUBÉRIEN FORT). Soit \( \left( {a}_{n}\right) \) une suite réelle telle que \( {a}_{n} = O\left( {1/n}\right) \) lorsque \( n \rightarrow + \infty \) . On suppose que la série entière \( \sum {a}_{n}{z}^{n} \) a un rayon de convergence \( \geq 1 \) et que sa somme \( F \) vérifie \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) = 0 \) . Notre propos est de montrer que la série \( \sum {a}_{n} \) converge et que sa somme est nulle.

> Problem 27 (STRONG TAUBERIAN THEOREM). Let \( \left( {a}_{n}\right) \) be a real sequence such that \( {a}_{n} = O\left( {1/n}\right) \) as \( n \rightarrow + \infty \) . Suppose that the power series \( \sum {a}_{n}{z}^{n} \) has a radius of convergence \( \geq 1 \) and that its sum \( F \) satisfies \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}F\left( x\right) = 0 \) . Our purpose is to show that the series \( \sum {a}_{n} \) converges and that its sum is zero.

On note \( \Phi \) l’ensemble des fonctions \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) telle que

> Let \( \Phi \) denote the set of functions \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) such that

1. pour tout \( x \in \left\lbrack {0,1\lbrack }\right. \) , la série \( \sum {a}_{n}\varphi \left( {x}^{n}\right) \) converge ;

> 1. for every \( x \in \left\lbrack {0,1\lbrack }\right. \) , the series \( \sum {a}_{n}\varphi \left( {x}^{n}\right) \) converges;

2. \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}\varphi \left( {x}^{n}\right) = 0 \) .

> 1/ a) Vérifier que toute fonction polynôme \( p \) nulle en 0 est élément de \( \Phi \) .

1/ a) Verify that any polynomial function \( p \) equal to zero at 0 is an element of \( \Phi \) .

> b) Soit \( q \) une fonction polynôme. Montrer l’existence et déterminer

b) Let \( q \) be a polynomial function. Show the existence of and determine

\[
\mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right) .
\]

2/ a) On considère la fonction \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto 0 \) si \( 0 \leq x < 1/2, x \mapsto 1 \) sinon. Pour tout \( \varepsilon > 0 \) , montrer qu’il existe deux polynômes \( {p}_{1} \) et \( {p}_{2} \) vérifiant

> 2/ a) Consider the function \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto 0 \) if \( 0 \leq x < 1/2, x \mapsto 1 \) otherwise. For every \( \varepsilon > 0 \) , show that there exist two polynomials \( {p}_{1} \) and \( {p}_{2} \) satisfying

(i) \( {p}_{1}\left( 0\right) = {p}_{2}\left( 0\right) = 0 \) et \( {p}_{1}\left( 1\right) = {p}_{2}\left( 1\right) = 1 \) ;

> (i) \( {p}_{1}\left( 0\right) = {p}_{2}\left( 0\right) = 0 \) and \( {p}_{1}\left( 1\right) = {p}_{2}\left( 1\right) = 1 \) ;

(ii) \( {p}_{1} \leq g \leq {p}_{2} \) sur \( \left\lbrack {0,1}\right\rbrack \) ;

> (ii) \( {p}_{1} \leq g \leq {p}_{2} \) over \( \left\lbrack {0,1}\right\rbrack \) ;

(iii) \( {\int }_{0}^{1}q\left( x\right) {dx} < \varepsilon \) avec \( q\left( x\right) = \frac{{p}_{2}\left( x\right) - {p}_{1}\left( x\right) }{x\left( {1 - x}\right) } \) .

> (iii) \( {\int }_{0}^{1}q\left( x\right) {dx} < \varepsilon \) with \( q\left( x\right) = \frac{{p}_{2}\left( x\right) - {p}_{1}\left( x\right) }{x\left( {1 - x}\right) } \) .

b) Montrer que \( g \in \Phi \) .

> b) Show that \( g \in \Phi \) .

3/ En déduire le théorème taubérien d’Hardy-Littlewood : Si \( \left( {b}_{n}\right) \) est une suite réelle vérifiant \( {b}_{n} = O\left( {1/n}\right) \) et si \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n} = \ell \) , alors la série \( \sum {b}_{n} \) converge et sa somme vaut \( \ell \) .

> 3/ Deduce the Hardy-Littlewood Tauberian theorem: If \( \left( {b}_{n}\right) \) is a real sequence satisfying \( {b}_{n} = O\left( {1/n}\right) \) and if \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n} = \ell \) , then the series \( \sum {b}_{n} \) converges and its sum is \( \ell \) .

Solution. \( 1/ \) a) Si \( p\left( x\right) = {x}^{k} \) avec \( k \in {\mathbb{N}}^{ * } \) , alors \( \sum {a}_{n}p\left( {x}^{n}\right) = \sum {a}_{n}{\left( {x}^{k}\right) }^{n} \) converge pour tout \( x \in \lbrack 0,1\lbrack \) , et de plus

> Solution. \( 1/ \) a) If \( p\left( x\right) = {x}^{k} \) with \( k \in {\mathbb{N}}^{ * } \) , then \( \sum {a}_{n}p\left( {x}^{n}\right) = \sum {a}_{n}{\left( {x}^{k}\right) }^{n} \) converges for all \( x \in \lbrack 0,1\lbrack \) , and furthermore

\[
\forall x \in  \lbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}p\left( {x}^{n}\right)  = F\left( {x}^{k}\right) \;\text{ donc }\;\mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}p\left( {x}^{n}\right)  = 0.
\]

Par linéarité, on en déduit que ce résultat est vrai pour toute fonction polynôme nulle en 0.

> By linearity, we deduce that this result holds for any polynomial function equal to 0 at 0.

b) Le polynôme \( q \) est borné sur \( \left\lbrack {0,1}\right\rbrack \) , donc pour tout \( x \in \left\lbrack {0,1\lbrack }\right. \) , la série \( \sum {x}^{n}q\left( {x}^{n}\right) \) converge absolument donc converge.

> b) The polynomial \( q \) is bounded on \( \left\lbrack {0,1}\right\rbrack \) , so for all \( x \in \left\lbrack {0,1\lbrack }\right. \) , the series \( \sum {x}^{n}q\left( {x}^{n}\right) \) converges absolutely and therefore converges.

Si \( q \) est le monôme \( x \mapsto {x}^{k}\left( {k \in \mathbb{N}}\right) \) , alors

> If \( q \) is the monomial \( x \mapsto {x}^{k}\left( {k \in \mathbb{N}}\right) \) , then

\[
\forall x \in  \lbrack 0,1\lbrack ,\;\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right)  = \left( {1 - x}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( {x}^{k + 1}\right) }^{n} = \frac{1 - x}{1 - {x}^{k + 1}} = \frac{1}{1 + x + \cdots  + {x}^{k}},
\]

donc

> therefore

\[
\mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right)  = \frac{1}{k + 1} = {\int }_{0}^{1}q\left( t\right) {dt}.
\]

On en déduit par linéarité que le résultat reste vrai pour tout polynôme \( q \) .

> We deduce by linearity that the result remains true for any polynomial \( q \) .

2 / a) On considère la fonction \( h : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) définie par

> 2 / a) Consider the function \( h : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) defined by

\[
h\left( x\right)  = \frac{g\left( x\right)  - x}{x\left( {1 - x}\right) }\;\text{ si }\;x \in  \rbrack 0,1\lbrack ,\;h\left( 0\right)  =  - 1,\;h\left( 1\right)  = 1.
\]

Compte tenu de la valeur de \( g \) la fonction \( h \) vérifie

> Given the value of \( g \) the function \( h \) satisfies

\[
\forall x \in  \left\lbrack  {0,\frac{1}{2}\left\lbrack  {,\;h\left( x\right)  =  - \frac{1}{1 - x},\;\forall x \in  \left\lbrack  {\frac{1}{2},1}\right\rbrack  ,\;h\left( x\right)  = \frac{1}{x}.}\right. }\right.
\]

Soit \( \varepsilon > 0 \) . On peut trouver deux fonctions continues \( {s}_{1} \) et \( {s}_{2} \) vérifiant \( {s}_{1} \leq h \leq {s}_{2},{\int }_{0}^{1}{s}_{2}\left( t\right) - \; {s}_{1}\left( t\right) {dt} < \varepsilon \) (on s’en convainc en faisant un dessin : prendre deux fonctions égales à \( h \) sur \( \left\lbrack {0,1}\right\rbrack \) sauf sur un petit voisinage de la discontinuité en \( x = 1/2 \) de \( h \) , et joindre les extrémités dans la partie manquante par une ligne continue qui reste toujours du même coté du graphe de \( h \) et qui reste bornée). Comme \( {s}_{1} \) et \( {s}_{2} \) sont continues, on peut trouver deux polynômes \( {t}_{1} \) et \( {t}_{2} \) tels que \( \left| {{t}_{1} - {s}_{1}}\right| < \varepsilon \) et \( \left| {{t}_{2} - {s}_{2}}\right| < \varepsilon \) sur \( \left\lbrack {0,1}\right\rbrack \) (conséquence du théorème de Weierstrass). Ainsi, les polynômes \( {u}_{1} = {t}_{1} - \varepsilon \) et \( {u}_{2} = {t}_{2} + \varepsilon \) vérifient \( {u}_{1} < {s}_{1} \leq h \leq {s}_{2} < {u}_{2} \) et \( {u}_{2} - {u}_{1} = {t}_{2} - {t}_{1} + {2\varepsilon } \leq \; {s}_{2} - {s}_{1} + {4\varepsilon } \) donc

> Let \( \varepsilon > 0 \). We can find two continuous functions \( {s}_{1} \) and \( {s}_{2} \) satisfying \( {s}_{1} \leq h \leq {s}_{2},{\int }_{0}^{1}{s}_{2}\left( t\right) - \; {s}_{1}\left( t\right) {dt} < \varepsilon \) (this can be visualized by drawing: take two functions equal to \( h \) on \( \left\lbrack {0,1}\right\rbrack \) except in a small neighborhood of the discontinuity at \( x = 1/2 \) of \( h \), and join the endpoints in the missing part with a continuous line that always stays on the same side of the graph of \( h \) and remains bounded). Since \( {s}_{1} \) and \( {s}_{2} \) are continuous, we can find two polynomials \( {t}_{1} \) and \( {t}_{2} \) such that \( \left| {{t}_{1} - {s}_{1}}\right| < \varepsilon \) and \( \left| {{t}_{2} - {s}_{2}}\right| < \varepsilon \) on \( \left\lbrack {0,1}\right\rbrack \) (a consequence of the Weierstrass theorem). Thus, the polynomials \( {u}_{1} = {t}_{1} - \varepsilon \) and \( {u}_{2} = {t}_{2} + \varepsilon \) satisfy \( {u}_{1} < {s}_{1} \leq h \leq {s}_{2} < {u}_{2} \) and \( {u}_{2} - {u}_{1} = {t}_{2} - {t}_{1} + {2\varepsilon } \leq \; {s}_{2} - {s}_{1} + {4\varepsilon } \) therefore

\[
{\int }_{0}^{1}\left( {{u}_{2}\left( x\right)  - {u}_{1}\left( x\right) }\right) {dx} \leq  {\int }_{0}^{1}\left( {{s}_{2}\left( x\right)  - {s}_{1}\left( x\right)  + {4\varepsilon }}\right) {dx} < {5\varepsilon }.
\]

Comme \( g\left( x\right) = x + x\left( {1 - x}\right) h\left( x\right) \) sur \( \left\lbrack {0,1}\right\rbrack \) , on en conclut que les polynômes \( {p}_{1} \) et \( {p}_{2} \) définis par \( {p}_{1}\left( x\right) = x + x\left( {1 - x}\right) {u}_{1}\left( x\right) ,{p}_{2}\left( x\right) = x + x\left( {1 - x}\right) {u}_{2}\left( x\right) \) vérifient \( {p}_{1}\left( 0\right) = {p}_{2}\left( 0\right) = 0,{p}_{1}\left( 1\right) = {p}_{2}\left( 1\right) = 1, \; {p}_{1} \leq g \leq {p}_{2} \) et

> Since \( g\left( x\right) = x + x\left( {1 - x}\right) h\left( x\right) \) on \( \left\lbrack {0,1}\right\rbrack \), we conclude that the polynomials \( {p}_{1} \) and \( {p}_{2} \) defined by \( {p}_{1}\left( x\right) = x + x\left( {1 - x}\right) {u}_{1}\left( x\right) ,{p}_{2}\left( x\right) = x + x\left( {1 - x}\right) {u}_{2}\left( x\right) \) satisfy \( {p}_{1}\left( 0\right) = {p}_{2}\left( 0\right) = 0,{p}_{1}\left( 1\right) = {p}_{2}\left( 1\right) = 1, \; {p}_{1} \leq g \leq {p}_{2} \) and

le polynôme \( q\left( x\right) = \frac{{p}_{2}\left( x\right) - {p}_{1}\left( x\right) }{x\left( {1 - x}\right) } = {u}_{2}\left( x\right) - {u}_{1}\left( x\right) \; \) vérifie \( \;{\int }_{0}^{1}q\left( x\right) {dx} < {5\varepsilon }. \)

> the polynomial \( q\left( x\right) = \frac{{p}_{2}\left( x\right) - {p}_{1}\left( x\right) }{x\left( {1 - x}\right) } = {u}_{2}\left( x\right) - {u}_{1}\left( x\right) \; \) satisfies \( \;{\int }_{0}^{1}q\left( x\right) {dx} < {5\varepsilon }. \)

D'où le résultat.

> Hence the result.

b) Soit \( \varepsilon > 0 \) et des polynômes \( {p}_{1},{p}_{2}, q \) vérifiant les conditions (i),(ii) et (iii) de la question précédente.

> b) Let \( \varepsilon > 0 \) and polynomials \( {p}_{1},{p}_{2}, q \) satisfying conditions (i), (ii), and (iii) from the previous question.

1. La convergence de \( \sum {a}_{n}g\left( {x}^{n}\right) \) pour tout \( x \in \lbrack 0,1\lbrack \) est immédiate car le terme d’indice \( n \) de cette série est nul dès que \( {x}^{n} < 1/2 \) .

> 1. The convergence of \( \sum {a}_{n}g\left( {x}^{n}\right) \) for any \( x \in \lbrack 0,1\lbrack \) is immediate because the term of index \( n \) of this series is zero as soon as \( {x}^{n} < 1/2 \) .

2. Soit \( M > 0 \) tel que \( \left| {a}_{n}\right| \leq M/n \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Comme \( {p}_{1} \leq g \leq {p}_{2} \) , on a par ailleurs

> 2. Let \( M > 0 \) be such that \( \left| {a}_{n}\right| \leq M/n \) for all \( n \in {\mathbb{N}}^{ * } \) . Since \( {p}_{1} \leq g \leq {p}_{2} \) , we also have

\[
\forall x \in  \left\lbrack  {0,1\lbrack ,\;\left| {\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}g\left( {x}^{n}\right)  - \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{p}_{1}\left( {x}^{n}\right) \left| {\; \leq  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left| {a}_{n}\right| \left( {{p}_{2} - {p}_{1}}\right) \left( {x}^{n}\right) }\right. }\right. }\right.
\]

\[
\leq  M\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n}\left( {1 - {x}^{n}}\right) }{n}q\left( {x}^{n}\right)  \leq  M\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right)
\]

(*)

> (on a utilisé la majoration \( \left. {\left( {1 - {x}^{n}}\right) = \left( {1 - x}\right) \left( {1 + x + \cdots + {x}^{n - 1}}\right) \leq \left( {1 - x}\right) n}\right) \) . Or \( {p}_{1} \in \Phi \) et \( \mathop{\lim }\limits_{{x \rightarrow 1 - }}\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right) = {\int }_{0}^{1}q\left( t\right) {dt} < \varepsilon \) , on en conclut

(we used the upper bound \( \left. {\left( {1 - {x}^{n}}\right) = \left( {1 - x}\right) \left( {1 + x + \cdots + {x}^{n - 1}}\right) \leq \left( {1 - x}\right) n}\right) \) . Now, \( {p}_{1} \in \Phi \) and \( \mathop{\lim }\limits_{{x \rightarrow 1 - }}\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right) = {\int }_{0}^{1}q\left( t\right) {dt} < \varepsilon \) , we conclude

\[
\exists \lambda  \in  \lbrack 0,1\lbrack ,\forall x \in  \lbrack \lambda ,1\lbrack ,\;\left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{p}_{1}\left( {x}^{n}\right) }\right|  < \varepsilon \;\text{ et }\;\left( {1 - x}\right) \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n}q\left( {x}^{n}\right)  < {2\varepsilon }.
\]

L'inégalité (*) entraîne donc

> The inequality (*) therefore implies

\[
\forall x \in  \left\lbrack  {\lambda ,1\left\lbrack  \right. }\right. \text{ , }\left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}g\left( {x}^{n}\right) }\right|  \leq  \left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{p}_{1}\left( {x}^{n}\right) }\right|  + \left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}\left( {g - {p}_{1}}\right) \left( {x}^{n}\right) }\right|  < \varepsilon  + {2M\varepsilon } = \left( {{2M} + 1}\right) \varepsilon \text{ . }
\]

Ceci est possible pour tout \( \varepsilon > 0 \) , donc \( g \) vérifie bien la condition 2 des éléments de \( \Phi \) . 3 / La forme de \( g \) montre que

> This is possible for any \( \varepsilon > 0 \) , so \( g \) indeed satisfies condition 2 of the elements of \( \Phi \) . 3 / The form of \( g \) shows that

\[
\forall x \in  \lbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}g\left( {x}^{n}\right)  = \mathop{\sum }\limits_{{n = 0}}^{\left\lbrack  -\log 2/\log x\right\rbrack  }{a}_{n},
\]

et comme \( g \in \Phi \) , on en conclut en faisant tendre \( x \) vers \( {1}^{ - } \) que la série \( \sum {a}_{n} \) converge et que sa somme est nulle.

> and since \( g \in \Phi \) , we conclude by letting \( x \) tend to \( {1}^{ - } \) that the series \( \sum {a}_{n} \) converges and its sum is zero.

Le théorème de Hardy-Littlewood s’en déduit facilement en considérant \( \left( {a}_{n}\right) \) définie par \( {a}_{0} = {b}_{0} - \ell \) et \( {a}_{n} = {b}_{n} \) pour tout \( n \in {\mathbb{N}}^{ * }. \)

> The Hardy-Littlewood theorem is easily deduced by considering \( \left( {a}_{n}\right) \) defined by \( {a}_{0} = {b}_{0} - \ell \) and \( {a}_{n} = {b}_{n} \) for all \( n \in {\mathbb{N}}^{ * }. \)

Remarque. Ce résultat est la version forte du théorème taubérien vu dans l'exercice 11 page 264. La preuve est intéressante car elle fait appel au théorème de Weierstrass là on ne s'y attendait pas a priori.

> Remark. This result is the strong version of the Tauberian theorem seen in exercise 11 on page 264. The proof is interesting because it uses the Weierstrass theorem where one would not have expected it a priori.

Si les \( {b}_{n} \) sont positifs, ce résultat est beaucoup plus facile à prouver.

> If the \( {b}_{n} \) are positive, this result is much easier to prove.

On peut montrer que le théorème Taubérien d'Hardy-Littlewood reste vrai si la suite \( \left( {n{b}_{n}}\right) \) est seulement minorée (et non pas bornée comme dans le cadre de l’exercice).

> It can be shown that the Hardy-Littlewood Tauberian theorem remains true if the sequence \( \left( {n{b}_{n}}\right) \) is only bounded below (and not bounded as in the context of the exercise).

PROBLEME 28 (THÉORÉME DE MÜNTZ). On note \( \mathcal{C} \) l’e.v des fonctions continues de \( \left\lbrack {0,1}\right\rbrack \) dans \( \mathbb{R} \) . On utilisera, sur \( \mathcal{C} \) , les deux normes suivantes :

> PROBLEM 28 (MÜNTZ'S THEOREM). Let \( \mathcal{C} \) be the vector space of continuous functions from \( \left\lbrack {0,1}\right\rbrack \) to \( \mathbb{R} \) . We will use the following two norms on \( \mathcal{C} \) :

\[
\forall f \in  \mathcal{C},\;\parallel f{\parallel }_{2} = {\left( {\int }_{0}^{1}{f}^{2}\left( t\right) dt\right) }^{1/2}\;\text{ et }\;\parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in  \left\lbrack  {0,1}\right\rbrack  }}\left| {f\left( t\right) }\right| .
\]

Le but de ce problème est de donner une condition nécessaire et suffisante sur une suite strictement croissante \( \left( {\alpha }_{n}\right) \) à valeurs positives, pour que \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) soit dense dans \( \mathcal{C} \) (par abus, \( {x}^{m} \) désigne la fonction de \( \mathcal{C} \) définie par \( x \mapsto {x}^{m} \) pour \( m \geq 0 \) ). On pourra utiliser le théorème de Weierstrass (voir le théorème 5 page 235).

> The goal of this problem is to provide a necessary and sufficient condition on a strictly increasing sequence \( \left( {\alpha }_{n}\right) \) with positive values for \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) to be dense in \( \mathcal{C} \) (by abuse of notation, \( {x}^{m} \) denotes the function of \( \mathcal{C} \) defined by \( x \mapsto {x}^{m} \) for \( m \geq 0 \) ). One may use the Weierstrass theorem (see theorem 5 on page 235).

1/ Soit \( {\left( {\alpha }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite à termes strictement positifs et strictement croissante.

> 1/ Let \( {\left( {\alpha }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a strictly increasing sequence of strictly positive terms.

a) Soient \( m \in {\mathbb{R}}^{+ * } \) et \( N \in {\mathbb{N}}^{ * } \) . On note \( {E}_{N} = {\operatorname{Vect}}_{1 \leq i \leq N}\left( {x}^{{\alpha }_{i}}\right) \) . Exprimer en fonction des \( {\alpha }_{i} \) et de \( m \) , la valeur \( {\Delta }_{N}\left( m\right) = \mathop{\inf }\limits_{{f \in {E}_{N}}}{\begin{Vmatrix}{x}^{m} - f\end{Vmatrix}}_{2} \) . (Indication. On pourra utiliser les déterminants de Gram - voir le tome Algèbre).

> a) Let \( m \in {\mathbb{R}}^{+ * } \) and \( N \in {\mathbb{N}}^{ * } \) be given. Let \( {E}_{N} = {\operatorname{Vect}}_{1 \leq i \leq N}\left( {x}^{{\alpha }_{i}}\right) \) be denoted as such. Express the value \( {\Delta }_{N}\left( m\right) = \mathop{\inf }\limits_{{f \in {E}_{N}}}{\begin{Vmatrix}{x}^{m} - f\end{Vmatrix}}_{2} \) in terms of \( {\alpha }_{i} \) and \( m \). (Hint: One may use Gram determinants - see the Algebra volume).

b) En déduire une condition nécessaire et suffisante sur la suite \( \left( {\alpha }_{n}\right) \) pour que \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) soit dense dans \( \mathcal{C} \) pour la norme \( \parallel .{\parallel }_{2} \) (théorème de Müntz).

> b) Deduce a necessary and sufficient condition on the sequence \( \left( {\alpha }_{n}\right) \) for \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) to be dense in \( \mathcal{C} \) for the norm \( \parallel .{\parallel }_{2} \) (Müntz's theorem).

2/ Soit \( {\left( {\alpha }_{n}\right) }_{n \in \mathbb{N}} \) une suite à termes positifs, strictement croissante, avec \( {\alpha }_{0} = 0 \) et vérifiant \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} > 1 \) . Donner une condition nécessaire et suffisante sur \( \left( {\alpha }_{n}\right) \) pour que \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) soit dense dans \( \mathcal{C} \) pour la norme \( \parallel .{\parallel }_{\infty } \) .

> 2/ Let \( {\left( {\alpha }_{n}\right) }_{n \in \mathbb{N}} \) be a strictly increasing sequence of positive terms, with \( {\alpha }_{0} = 0 \) and satisfying \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} > 1 \). Provide a necessary and sufficient condition on \( \left( {\alpha }_{n}\right) \) for \( {\operatorname{Vect}}_{n \in \mathbb{N}}\left( {x}^{{\alpha }_{n}}\right) \) to be dense in \( \mathcal{C} \) for the norm \( \parallel .{\parallel }_{\infty } \).

Solution. 1/ a) Munissons \( \mathcal{C} \) du produit scalaire \( \langle f, g\rangle = {\int }_{0}^{1}f\left( t\right) g\left( t\right) {dt} \) , dont \( \parallel .{\parallel }_{2} \) est la norme euclidienne associée. Le nombre réel \( {\Delta }_{N}\left( m\right) \) s’interprète comme la distance (au sens de \( \parallel .{\parallel }_{2} \) ) de \( {x}^{m} \) à \( {E}_{N} = {\operatorname{Vect}}_{1 \leq i \leq N}\left( {x}^{{\alpha }_{i}}\right) \) . On sait (voir le tome Algèbre) que ceci peut s’exprimer au moyen des déterminants de Gram. Plus précisément, en notant, pour tout \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathcal{C}}^{n} \) , \( G\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) le déterminant de la matrice \( {\left( \left\langle {x}_{i},{x}_{j}\right\rangle \right) }_{1 \leq i, j \leq n} \) , on a

> Solution. 1/ a) Let us equip \( \mathcal{C} \) with the inner product \( \langle f, g\rangle = {\int }_{0}^{1}f\left( t\right) g\left( t\right) {dt} \), for which \( \parallel .{\parallel }_{2} \) is the associated Euclidean norm. The real number \( {\Delta }_{N}\left( m\right) \) is interpreted as the distance (in the sense of \( \parallel .{\parallel }_{2} \)) from \( {x}^{m} \) to \( {E}_{N} = {\operatorname{Vect}}_{1 \leq i \leq N}\left( {x}^{{\alpha }_{i}}\right) \). We know (see the Algebra volume) that this can be expressed using Gram determinants. More precisely, by denoting, for any \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathcal{C}}^{n} \), \( G\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) as the determinant of the matrix \( {\left( \left\langle {x}_{i},{x}_{j}\right\rangle \right) }_{1 \leq i, j \leq n} \), we have

\[
{\Delta }_{N}{\left( m\right) }^{2} = \frac{G\left( {{x}^{{\alpha }_{1}},\ldots ,{x}^{{\alpha }_{N}},{x}^{m}}\right) }{G\left( {{x}^{{\alpha }_{1}},\ldots ,{x}^{{\alpha }_{N}}}\right) }.
\]

(*)

> Ici on a \( \left\langle {{x}^{a},{x}^{b}}\right\rangle = \frac{1}{a + b + 1} \) . On trouve dans le tome Algèbre que la valeur d’un déterminant de Cauchy \( \det {\left( \frac{1}{{a}_{i} + {b}_{j}}\right) }_{i, j} \) est donnée par

Here we have \( \left\langle {{x}^{a},{x}^{b}}\right\rangle = \frac{1}{a + b + 1} \). We find in the Algebra volume that the value of a Cauchy determinant \( \det {\left( \frac{1}{{a}_{i} + {b}_{j}}\right) }_{i, j} \) is given by

\[
\det {\left( \frac{1}{{a}_{i} + {b}_{j}}\right) }_{1 \leq  i, j \leq  n} = \frac{\left\lbrack  {\mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{a}_{i} - {a}_{j}}\right) }\right\rbrack   \cdot  \left\lbrack  {\mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}\left( {{b}_{i} - {b}_{j}}\right) }\right\rbrack  }{\mathop{\prod }\limits_{{1 \leq  i, j \leq  n}}\left( {{a}_{i} + {b}_{j}}\right) }.
\]

En particulier, pour toute famille \( {\left( {p}_{i}\right) }_{1 \leq i \leq n} \) de nombres réels, \( G\left( {{x}^{{p}_{1}},\ldots ,{x}^{{p}_{n}}}\right) \) est un déterminant de Gram car \( \left\langle {{x}^{{p}_{i}},{x}^{{p}_{j}}}\right\rangle = \frac{1}{{a}_{i} + {b}_{j}} \) avec \( {a}_{i} = {p}_{i} \) et \( {b}_{j} = {p}_{j} + 1 \) , et on a donc

> In particular, for any family \( {\left( {p}_{i}\right) }_{1 \leq i \leq n} \) of real numbers, \( G\left( {{x}^{{p}_{1}},\ldots ,{x}^{{p}_{n}}}\right) \) is a Gram determinant because \( \left\langle {{x}^{{p}_{i}},{x}^{{p}_{j}}}\right\rangle = \frac{1}{{a}_{i} + {b}_{j}} \) with \( {a}_{i} = {p}_{i} \) and \( {b}_{j} = {p}_{j} + 1 \) , and we therefore have

\[
G\left( {{x}^{{p}_{1}},\ldots ,{x}^{{p}_{n}}}\right)  = \frac{\mathop{\prod }\limits_{{1 \leq  i < j \leq  n}}{\left( {p}_{i} - {p}_{j}\right) }^{2}}{\mathop{\prod }\limits_{{1 \leq  i, j \leq  n}}\left( {{p}_{i} + {p}_{j} + 1}\right) }.
\]

En appliquant cette formule avec \( {p}_{1} = {\alpha }_{1},\ldots ,{p}_{N} = {\alpha }_{N},{p}_{N + 1} = m \) on obtient

> By applying this formula with \( {p}_{1} = {\alpha }_{1},\ldots ,{p}_{N} = {\alpha }_{N},{p}_{N + 1} = m \) we obtain

\[
G\left( {{x}^{{\alpha }_{1}},\ldots ,{x}^{{\alpha }_{N}},{x}^{m}}\right)  = \frac{\left\lbrack  {\mathop{\prod }\limits_{{i < j}}{\left( {\alpha }_{i} - {\alpha }_{j}\right) }^{2}}\right\rbrack   \cdot  \left\lbrack  {\mathop{\prod }\limits_{i}{\left( {\alpha }_{i} - m\right) }^{2}}\right\rbrack  }{\left( {{2m} + 1}\right) \left\lbrack  {\mathop{\prod }\limits_{{i, j}}\left( {{\alpha }_{i} + {\alpha }_{j} + 1}\right) }\right\rbrack   \cdot  \left\lbrack  {\mathop{\prod }\limits_{i}{\left( {\alpha }_{i} + m + 1\right) }^{2}}\right\rbrack  }
\]

(les indices \( i \) et \( j \) sont pris entre1et \( N \) ). De même, on trouve

> (the indices \( i \) and \( j \) are taken between 1 and \( N \) ). Similarly, we find

\[
G\left( {{x}^{{\alpha }_{1}},\ldots ,{x}^{{\alpha }_{N}}}\right)  = \frac{\mathop{\prod }\limits_{{i < j}}{\left( {\alpha }_{i} - {\alpha }_{j}\right) }^{2}}{\mathop{\prod }\limits_{{i, j}}\left( {{\alpha }_{i} + {\alpha }_{j} + 1}\right) }.
\]

On en conclut, avec (*), que

> We conclude, with (*), that

\[
{\Delta }_{N}\left( m\right)  = \frac{1}{\sqrt{{2m} + 1}}\mathop{\prod }\limits_{{i = 1}}^{N}\left| \frac{{\alpha }_{i} - m}{{\alpha }_{i} + m + 1}\right| .
\]

\( \left( {* * }\right) \)

> b) On note \( E = \operatorname{Vect}{\left( {x}^{{\alpha }_{i}}\right) }_{i \in {\mathbb{N}}^{ * }} \) . Nous allons montrer qu’une condition nécessaire et suffisante pour que \( \bar{E} = \mathcal{C} \) (où l’adhérence est prise au sens de la norme \( \parallel .{\parallel }_{2} \) ) est que la série \( \sum 1/{\alpha }_{n} \) diverge.

b) Let \( E = \operatorname{Vect}{\left( {x}^{{\alpha }_{i}}\right) }_{i \in {\mathbb{N}}^{ * }} \) . We will show that a necessary and sufficient condition for \( \bar{E} = \mathcal{C} \) (where the closure is taken in the sense of the norm \( \parallel .{\parallel }_{2} \) ) is that the series \( \sum 1/{\alpha }_{n} \) diverges.

> Condition nécessaire. Il existe bien sûr \( m > 0 \) tel que \( {\alpha }_{n} \neq m \) pour tout \( n \) . La fonction \( {x}^{m} \) appartient à \( \bar{E} = \mathcal{C} \) , donc la suite \( {\left( {\Delta }_{N}\left( m\right) \right) }_{N \in {\mathbb{N}}^{ * }} \) tend vers 0, ce qui entraîne, d’après (**)

Necessary condition. There certainly exists \( m > 0 \) such that \( {\alpha }_{n} \neq m \) for all \( n \) . The function \( {x}^{m} \) belongs to \( \bar{E} = \mathcal{C} \) , so the sequence \( {\left( {\Delta }_{N}\left( m\right) \right) }_{N \in {\mathbb{N}}^{ * }} \) tends to 0, which implies, according to (**)

\[
\mathop{\lim }\limits_{{N \rightarrow   + \infty }}\mathop{\prod }\limits_{{i = 1}}^{N}\left( \frac{{\alpha }_{i} - m}{{\alpha }_{i} + m + 1}\right)  = 0.
\]

(***)

> - Si la suite \( \left( {\alpha }_{n}\right) \) est majorée, la série \( \sum 1/{\alpha }_{n} \) diverge.

- If the sequence \( \left( {\alpha }_{n}\right) \) is bounded, the series \( \sum 1/{\alpha }_{n} \) diverges.

> - Sinon, \( \left( {\alpha }_{n}\right) \) tend vers \( + \infty \) . Soit \( {N}_{0} \in  \mathbb{N} \) tel que \( {\alpha }_{n} > m \) pour tout \( n \geq  {N}_{0} \) . Alors, dès que \( n \geq  {N}_{0} \) ,

- Otherwise, \( \left( {\alpha }_{n}\right) \) tends to \( + \infty \) . Let \( {N}_{0} \in  \mathbb{N} \) be such that \( {\alpha }_{n} > m \) for all \( n \geq  {N}_{0} \) . Then, as soon as \( n \geq  {N}_{0} \) ,

\[
{u}_{n} = \log \left( \frac{{\alpha }_{n} - m}{{\alpha }_{n} + m + 1}\right)  = \log \left( {1 - \frac{{2m} + 1}{{\alpha }_{n} + m + 1}}\right)  \sim   - \frac{{2m} + 1}{{\alpha }_{n}}\;\left( {n \rightarrow   + \infty }\right) ,
\]

(***)

> et comme d’après (***), \( \mathop{\sum }\limits_{{n \geq {N}_{0}}}{u}_{n} \) diverge, on en conclut que \( \sum 1/{\alpha }_{n} \) diverge.

and since according to (***), \( \mathop{\sum }\limits_{{n \geq {N}_{0}}}{u}_{n} \) diverges, we conclude that \( \sum 1/{\alpha }_{n} \) diverges.

> Condition suffisante. Réciproquement, si \( \sum 1/{\alpha }_{n} \) diverge, montrons \( \bar{E} = \mathcal{C} \) . Pour cela, en vertu du théorème de Weierstrass, il suffit de montrer que pour tout \( m \in \mathbb{N},{x}^{m} \in \bar{E} \) .

Sufficient condition. Conversely, if \( \sum 1/{\alpha }_{n} \) diverges, let us show \( \bar{E} = \mathcal{C} \) . For this, by virtue of the Weierstrass theorem, it suffices to show that for all \( m \in \mathbb{N},{x}^{m} \in \bar{E} \) .

> Soit \( m \in \mathbb{N} \) . Il s’agit de montrer que (***) est vérifié.

Let \( m \in \mathbb{N} \) . It is a matter of showing that (***) is satisfied.

> - Si \( \left( {\alpha }_{n}\right) \) est majorée, c’est évident.

- If \( \left( {\alpha }_{n}\right) \) is bounded, it is obvious.

> - Sinon, \( \left( {\alpha }_{n}\right) \) tend vers \( + \infty \) , et l’équivalent (****) montre que \( \sum {u}_{n} \) diverge vers \( - \infty \) , et on conclut que (***) est vérifié.

- Otherwise, \( \left( {\alpha }_{n}\right) \) tends to \( + \infty \) , and the equivalent (****) shows that \( \sum {u}_{n} \) diverges to \( - \infty \) , and we conclude that (***) is satisfied.

> 2/ \( \operatorname{Si}\bar{E} = \mathcal{C} \) au sens de la norme \( \parallel .{\parallel }_{\infty } \) , on vérifie facilement que \( \bar{E} = \mathcal{C} \) au sens de la norme \( \parallel .{\parallel }_{2} \) , donc d’après \( 1/\mathrm{b}),\mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) diverge.

2/ \( \operatorname{Si}\bar{E} = \mathcal{C} \) in the sense of the \( \parallel .{\parallel }_{\infty } \) norm, it is easy to verify that \( \bar{E} = \mathcal{C} \) in the sense of the \( \parallel .{\parallel }_{2} \) norm, therefore according to \( 1/\mathrm{b}),\mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) it diverges.

> Réciproquement, supposons que \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) diverge. Comme \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} > 1 \) , il existe \( N \in \mathbb{N} \) tel que \( {\alpha }_{N} > 1 \) . Quitte à retirer des termes à \( \left( {\alpha }_{n}\right) \) , on peut donc supposer \( {\alpha }_{1} > 1 \) . En vertu du théorème de Weierstrass, pour montrer \( \bar{E} = \mathcal{C} \) , il suffit de montrer que pour toute fonction polynôme \( P \) sur \( \left\lbrack {0,1}\right\rbrack , P \in \bar{E} \) . Soit \( P \) une fonction polynôme. Soit \( \varepsilon > 0 \) . La série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{\left( {\alpha }_{n} - 1\right) }^{-1} \) diverge, donc d’après \( 1/\mathrm{b}) \) , il existe \( g \in {\operatorname{Vect}}_{i \in {\mathbb{N}}^{ * }}\left( {x}^{{\alpha }_{i} - 1}\right) \) tel que \( {\begin{Vmatrix}{P}^{\prime } - g\end{Vmatrix}}_{2} < \varepsilon \) . Soit \( h \) la primitive de \( g \) sur \( \left\lbrack {0,1}\right\rbrack \) vérifiant \( h\left( 0\right) = P\left( 0\right) \) . On voit facilement que \( h \in E \) . En posant \( Q = h - P \) , on a \( Q\left( 0\right) = 0 \) , donc pour tout \( x \in \left\lbrack {0,1}\right\rbrack , Q\left( x\right) = {\int }_{0}^{x}{Q}^{\prime }\left( t\right) {dt} \) , donc d’après l’inégalité de Schwarz,

Conversely, suppose that \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) diverges. Since \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\alpha }_{n} > 1 \) , there exists \( N \in \mathbb{N} \) such that \( {\alpha }_{N} > 1 \) . By removing terms from \( \left( {\alpha }_{n}\right) \) , we can therefore assume \( {\alpha }_{1} > 1 \) . By virtue of the Weierstrass theorem, to show \( \bar{E} = \mathcal{C} \) , it suffices to show that for any polynomial function \( P \) on \( \left\lbrack {0,1}\right\rbrack , P \in \bar{E} \) . Let \( P \) be a polynomial function. Let \( \varepsilon > 0 \) . The series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{\left( {\alpha }_{n} - 1\right) }^{-1} \) diverges, therefore according to \( 1/\mathrm{b}) \) , there exists \( g \in {\operatorname{Vect}}_{i \in {\mathbb{N}}^{ * }}\left( {x}^{{\alpha }_{i} - 1}\right) \) such that \( {\begin{Vmatrix}{P}^{\prime } - g\end{Vmatrix}}_{2} < \varepsilon \) . Let \( h \) be the primitive of \( g \) on \( \left\lbrack {0,1}\right\rbrack \) satisfying \( h\left( 0\right) = P\left( 0\right) \) . It is easy to see that \( h \in E \) . By setting \( Q = h - P \) , we have \( Q\left( 0\right) = 0 \) , therefore for all \( x \in \left\lbrack {0,1}\right\rbrack , Q\left( x\right) = {\int }_{0}^{x}{Q}^{\prime }\left( t\right) {dt} \) , thus according to the Schwarz inequality,

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;\left| {Q\left( x\right) }\right|  \leq  {\left( {\int }_{0}^{x}{Q}^{\prime }{\left( t\right) }^{2}dt\right) }^{1/2}\sqrt{x} \leq  {\begin{Vmatrix}{Q}^{\prime }\end{Vmatrix}}_{2} = {\begin{Vmatrix}{P}^{\prime } - g\end{Vmatrix}}_{2} < \varepsilon ,
\]

donc \( \parallel h - P{\parallel }_{\infty } = \parallel Q{\parallel }_{\infty } < \varepsilon \) . Finalement, pour tout \( \varepsilon > 0 \) , nous avons trouvé \( h \in E \) tel que \( \parallel h - P{\parallel }_{\infty } < \varepsilon \) . On en conclut \( P \in \bar{E} \) , et finalement, \( \bar{E} = \mathcal{C} \) .

> therefore \( \parallel h - P{\parallel }_{\infty } = \parallel Q{\parallel }_{\infty } < \varepsilon \) . Finally, for all \( \varepsilon > 0 \) , we have found \( h \in E \) such that \( \parallel h - P{\parallel }_{\infty } < \varepsilon \) . We conclude \( P \in \bar{E} \) , and finally, \( \bar{E} = \mathcal{C} \) .

Finalement, on a \( \bar{E} = \mathcal{C} \) pour la norme \( \parallel .{\parallel }_{\infty } \) si et seulement si la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) diverge.

> Finally, we have \( \bar{E} = \mathcal{C} \) for the \( \parallel .{\parallel }_{\infty } \) norm if and only if the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}1/{\alpha }_{n} \) diverges.

Problem 29 (THÉORÉME DE CANTOR SUR LES SÉRIES TRIGONOMÉTRIQUES). 1/ Soit \( \sum {a}_{n} \) une série à termes complexes, convergente et de somme nulle. On pose

> Problem 29 (CANTOR'S THEOREM ON TRIGONOMETRIC SERIES). 1/ Let \( \sum {a}_{n} \) be a series with complex terms, convergent and with a sum of zero. We define

\[
{U}_{0} : {\mathbb{R}}^{ * } \rightarrow  \mathbb{C}\;t \mapsto  1\;\text{ et }\;\forall n \in  {\mathbb{N}}^{ * },\;{U}_{n} : {\mathbb{R}}^{ * } \rightarrow  \mathbb{C}\;t \mapsto  {\left( \frac{\sin {nt}}{nt}\right) }^{2}.
\]

Pour tout \( t \neq 0 \) , montrer que \( S\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{U}_{n}\left( t\right) \) existe, puis montrer \( \mathop{\lim }\limits_{\substack{{t \rightarrow 0} \\ {t \neq 0} }}S\left( t\right) = 0 \) . 2/ (Théorème de Cantor-Lebesgue.) Soit \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) une famille de nombres complexes. On suppose que pour tout \( t \in \mathbb{R},\mathop{\lim }\limits_{{n \rightarrow + \infty }}{c}_{n}{e}^{int} + {c}_{-n}{e}^{-{int}} = 0 \) . Montrer que \( \mathop{\lim }\limits_{{\left| n\right| \rightarrow + \infty }}{c}_{n} = \) 0. (Indication : on se ramènera à montrer que si pour tout \( t \in \mathbb{R},{\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) \rightarrow 0 \) , alors \( {\rho }_{n} \rightarrow 0 \) . Ensuite on construira, en supposant \( {\rho }_{n} \nrightarrow 0 \) , une suite décroissante \( \left( {I}_{k}\right) \) de segments non vides de \( \mathbb{R} \) vérifiant \( \cos \left( {{n}_{k}t - {\theta }_{{n}_{k}}}\right) \geq 1/2 \) pour tout \( t \in {I}_{k} \) et pour tout \( k \) , avec \( \left( {n}_{k}\right) \) bien choisie.) 3/ (Théorème de Cantor.) Soit \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) une famille de nombres complexes telle que

> For all \( t \neq 0 \), show that \( S\left( t\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{U}_{n}\left( t\right) \) exists, then show \( \mathop{\lim }\limits_{\substack{{t \rightarrow 0} \\ {t \neq 0} }}S\left( t\right) = 0 \). 2/ (Cantor-Lebesgue Theorem.) Let \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) be a family of complex numbers. Suppose that for all \( t \in \mathbb{R},\mathop{\lim }\limits_{{n \rightarrow + \infty }}{c}_{n}{e}^{int} + {c}_{-n}{e}^{-{int}} = 0 \). Show that \( \mathop{\lim }\limits_{{\left| n\right| \rightarrow + \infty }}{c}_{n} = \) 0. (Hint: reduce to showing that if for all \( t \in \mathbb{R},{\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) \rightarrow 0 \), then \( {\rho }_{n} \rightarrow 0 \). Then construct, assuming \( {\rho }_{n} \nrightarrow 0 \), a decreasing sequence \( \left( {I}_{k}\right) \) of non-empty segments of \( \mathbb{R} \) satisfying \( \cos \left( {{n}_{k}t - {\theta }_{{n}_{k}}}\right) \geq 1/2 \) for all \( t \in {I}_{k} \) and for all \( k \), with \( \left( {n}_{k}\right) \) well-chosen.) 3/ (Cantor's Theorem.) Let \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) be a family of complex numbers such that

\[
\forall x \in  \mathbb{R},\;\mathop{\lim }\limits_{{N \rightarrow   + \infty }}\mathop{\sum }\limits_{{n =  - N}}^{N}{c}_{n}{e}^{inx} = 0.
\]

a) Montrer que la fonction

> a) Show that the function

\[
F : x \mapsto  {c}_{0}\frac{{x}^{2}}{2} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{c}_{n}{e}^{inx} + {c}_{-n}{e}^{-{inx}}}{{\left( in\right) }^{2}}
\]

existe et est continue sur \( \mathbb{R} \) .

> exists and is continuous on \( \mathbb{R} \).

b) Pour tout fonction continue \( G : \mathbb{R} \rightarrow \mathbb{R} \) , on définit

> b) For any continuous function \( G : \mathbb{R} \rightarrow \mathbb{R} \), we define

\[
\forall x \in  \mathbb{R},\;\mathrm{D}G\left( x\right)  = \mathop{\lim }\limits_{\substack{{h \rightarrow  0} \\  {h \neq  0} }}\frac{G\left( {x + h}\right)  + G\left( {x - h}\right)  - {2G}\left( x\right) }{{h}^{2}}
\]

lorsque cette limite existe (on rappelle - voir la question c) de l'exercice 5 page 102 - que si pour tout \( x,\mathrm{D}G\left( x\right) \) existe et est nul, alors \( G \) est affine.) Montrer que pour tout \( x \in \mathbb{R},\mathrm{D}F\left( x\right) \) existe et est nul.

> when this limit exists (recall - see question c) of exercise 5 page 102 - that if for all \( x,\mathrm{D}G\left( x\right) \) exists and is zero, then \( G \) is affine.) Show that for all \( x \in \mathbb{R},\mathrm{D}F\left( x\right) \) exists and is zero.

c) En déduire \( {c}_{n} = 0 \) pour tout \( n \in \mathbb{Z} \) .

> c) Deduce \( {c}_{n} = 0 \) for all \( n \in \mathbb{Z} \).

Solution. 1 / La série \( \sum {a}_{n} \) converge, donc la suite \( \left( {a}_{n}\right) \) tend vers 0. Par ailleurs, \( \left| {{a}_{n}{U}_{n}\left( t\right) }\right| \leq \; \left( {\left| {a}_{n}\right| /{t}^{2}}\right) 1/{n}^{2} \) , donc \( S\left( t\right) \) existe pour tout \( t \neq 0 \) .

> Solution. 1/ The series \( \sum {a}_{n} \) converges, so the sequence \( \left( {a}_{n}\right) \) tends to 0. Furthermore, \( \left| {{a}_{n}{U}_{n}\left( t\right) }\right| \leq \; \left( {\left| {a}_{n}\right| /{t}^{2}}\right) 1/{n}^{2} \), so \( S\left( t\right) \) exists for all \( t \neq 0 \).

Pour tout \( n \in {\mathbb{N}}^{ * } \) , notons \( {s}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) . Une transformation d’Abel donne

> For all \( n \in {\mathbb{N}}^{ * } \), let \( {s}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \). An Abel transformation gives

\[
\forall t \neq  0,\;\mathop{\sum }\limits_{{n = 0}}^{N}{a}_{n}{U}_{n}\left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{N - 1}}{s}_{n}\left( {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right)  + {s}_{N}{U}_{N}\left( t\right) ,
\]

et comme \( \left( {{s}_{N}{U}_{N}\left( t\right) }\right) \) tend vers 0, on a finalement

> and since \( \left( {{s}_{N}{U}_{N}\left( t\right) }\right) \) tends to 0, we finally have

\[
\forall t \neq  0,\;S\left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{s}_{n}\left( {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right) .
\]

Soit \( \varepsilon > 0 \) et \( N \in {\mathbb{N}}^{ * } \) tel que \( \left| {s}_{n}\right| \leq \varepsilon \) pour \( n \geq N \) , et soit \( A \) un majorant de la suite \( \left( \left| {s}_{n}\right| \right) \) . La formule précédente entraîne la majoration

> Let \( \varepsilon > 0 \) and \( N \in {\mathbb{N}}^{ * } \) be such that \( \left| {s}_{n}\right| \leq \varepsilon \) for \( n \geq N \), and let \( A \) be an upper bound of the sequence \( \left( \left| {s}_{n}\right| \right) \). The previous formula leads to the upper bound

\[
\forall t \neq  0,\;\left| {S\left( t\right) }\right|  \leq  A\mathop{\sum }\limits_{{n = 0}}^{{N - 1}}\left| {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right|  + \varepsilon \mathop{\sum }\limits_{{n = N}}^{{+\infty }}\left| {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right| .
\]

(*)

> On remarque que

We note that

\[
\left| {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right|  = \left| {{\int }_{nt}^{\left( {n + 1}\right) t}f\left( x\right) {dx}}\right|  \leq  {\int }_{nt}^{\left( {n + 1}\right) t}\left| {f\left( x\right) }\right| {dx},\;f\left( x\right)  = \frac{d}{dx}\left\lbrack  {\left( \frac{\sin x}{x}\right) }^{2}\right\rbrack  .
\]

La fonction \( x \mapsto \left( {\sin x}\right) /x \) est égale à \( \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{\left( -1\right) }^{k}\frac{{x}^{2k}}{\left( {{2k} + 1}\right) !} \) , donc prolongeable en 0 en une fonction de classe \( {\mathcal{C}}^{\infty } \) , donc \( f \) est prolongeable en 0 en une fonction de classe \( {\mathcal{C}}^{\infty } \) . L’intégrale \( {\int }_{0}^{1}\left| {f\left( x\right) }\right| {dx} \) existe donc. Par ailleurs, un calcul rapide donne \( \left| {f\left( x\right) }\right| = O\left( {1/{x}^{2}}\right) \) en \( + \infty \) , donc l’intégrale \( {\int }_{0}^{+\infty }\left| {f\left( x\right) }\right| {dx} \) existe bien. Si on note \( M \) sa valeur,(*) entraîne

> The function \( x \mapsto \left( {\sin x}\right) /x \) is equal to \( \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{\left( -1\right) }^{k}\frac{{x}^{2k}}{\left( {{2k} + 1}\right) !} \), and thus can be extended at 0 into a function of class \( {\mathcal{C}}^{\infty } \), so \( f \) can be extended at 0 into a function of class \( {\mathcal{C}}^{\infty } \). The integral \( {\int }_{0}^{1}\left| {f\left( x\right) }\right| {dx} \) therefore exists. Furthermore, a quick calculation gives \( \left| {f\left( x\right) }\right| = O\left( {1/{x}^{2}}\right) \) at \( + \infty \), so the integral \( {\int }_{0}^{+\infty }\left| {f\left( x\right) }\right| {dx} \) does indeed exist. If we denote its value by \( M \), (*) leads to

\[
\forall t \neq  0,\;\left| {S\left( t\right) }\right|  \leq  A\mathop{\sum }\limits_{{n = 0}}^{{N - 1}}\left| {{U}_{n}\left( t\right)  - {U}_{n + 1}\left( t\right) }\right|  + {\varepsilon M}.
\]

Comme pour tout \( n,\mathop{\lim }\limits_{\substack{{t \rightarrow 0} \\ {t \neq 0} }}{U}_{n}\left( t\right) = 1 \) , la fonction \( t \mapsto A\mathop{\sum }\limits_{{n = 0}}^{{N - 1}}\left| {{U}_{n}\left( t\right) - {U}_{n + 1}\left( t\right) }\right| \) tend vers 0 lorsque \( t \rightarrow 0, t \neq 0 \) , ce qui entraîne l’existence de \( \alpha > 0 \) tel que \( \left| {S\left( t\right) }\right| < \varepsilon + \varepsilon = {2\varepsilon } \) pour tout \( t \) tel que \( 0 < \left| t\right| < \alpha \) , d’où le résultat.

> Since for all \( n,\mathop{\lim }\limits_{\substack{{t \rightarrow 0} \\ {t \neq 0} }}{U}_{n}\left( t\right) = 1 \), the function \( t \mapsto A\mathop{\sum }\limits_{{n = 0}}^{{N - 1}}\left| {{U}_{n}\left( t\right) - {U}_{n + 1}\left( t\right) }\right| \) tends to 0 as \( t \rightarrow 0, t \neq 0 \), which implies the existence of \( \alpha > 0 \) such that \( \left| {S\left( t\right) }\right| < \varepsilon + \varepsilon = {2\varepsilon } \) for all \( t \) such that \( 0 < \left| t\right| < \alpha \), hence the result.

2/ On peut écrire \( {c}_{n}{e}^{int} + {c}_{-n}{e}^{-{int}} \) sous la forme \( \left( {{a}_{n}\cos {nt} + {b}_{n}\sin {nt}}\right) + i\left( {{a}_{n}^{\prime }\cos {nt} + {b}_{n}^{\prime }\sin {nt}}\right) \) , où \( {a}_{n},{b}_{n},{a}_{n}^{\prime },{b}_{n}^{\prime } \in \mathbb{R} \) . Nous allons montrer que les suites \( \left( {a}_{n}\right) \) et \( \left( {b}_{n}\right) \) tendent vers 0 (on aura de même \( {a}_{n}^{\prime } \rightarrow 0 \) et \( {b}_{n}^{\prime } \rightarrow 0 \) , ce qui montrera que les suites \( \left( {c}_{n}\right) \) et \( \left( {c}_{-n}\right) \) tendent vers 0 \( ) \) . Pour tout \( t \in \mathbb{R} \) , on sait que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{a}_{n}\cos {nt} + {b}_{n}\sin {nt}}\right) = 0 \) . En posant \( {\rho }_{n} = \sqrt{{a}_{n}^{2} + {b}_{n}^{2}} \) , il existe pour tout \( n \) un nombre réel \( {\theta }_{n} \in \left\lbrack {0,{2\pi }}\right\rbrack \) tel que \( {a}_{n}\cos {nt} + {b}_{n}\sin {nt} = {\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) \) pour tout \( t \in \mathbb{R} \) . Ainsi, nous nous sommes ramené au problème suivant : si pour tout \( t \in \mathbb{R} \) , \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) = 0 \) , il faut montrer que la suite \( \left( {\rho }_{n}\right) \) tend vers 0 .

> 2/ We can write \( {c}_{n}{e}^{int} + {c}_{-n}{e}^{-{int}} \) in the form \( \left( {{a}_{n}\cos {nt} + {b}_{n}\sin {nt}}\right) + i\left( {{a}_{n}^{\prime }\cos {nt} + {b}_{n}^{\prime }\sin {nt}}\right) \) , where \( {a}_{n},{b}_{n},{a}_{n}^{\prime },{b}_{n}^{\prime } \in \mathbb{R} \) . We will show that the sequences \( \left( {a}_{n}\right) \) and \( \left( {b}_{n}\right) \) tend to 0 (we will similarly have \( {a}_{n}^{\prime } \rightarrow 0 \) and \( {b}_{n}^{\prime } \rightarrow 0 \) , which will show that the sequences \( \left( {c}_{n}\right) \) and \( \left( {c}_{-n}\right) \) tend to 0 \( ) \) . For all \( t \in \mathbb{R} \) , we know that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{a}_{n}\cos {nt} + {b}_{n}\sin {nt}}\right) = 0 \) . By setting \( {\rho }_{n} = \sqrt{{a}_{n}^{2} + {b}_{n}^{2}} \) , there exists for all \( n \) a real number \( {\theta }_{n} \in \left\lbrack {0,{2\pi }}\right\rbrack \) such that \( {a}_{n}\cos {nt} + {b}_{n}\sin {nt} = {\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) \) for all \( t \in \mathbb{R} \) . Thus, we have reduced the problem to the following: if for all \( t \in \mathbb{R} \) , \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\rho }_{n}\cos \left( {{nt} - {\theta }_{n}}\right) = 0 \) , we must show that the sequence \( \left( {\rho }_{n}\right) \) tends to 0 .

Supposons le contraire. Alors il existe \( \delta > 0 \) et une suite strictement croissante \( {\left( {n}_{k}\right) }_{k \in \mathbb{N}} \) d’entiers telle que \( {\rho }_{{n}_{k}} \geq \delta \) pour tout \( k \) . Quitte à restreindre la suite \( \left( {n}_{k}\right) \) , on peut même supposer \( {n}_{k + 1} \geq 6{n}_{k} \) pour tout \( k \) .

> Assume the contrary. Then there exists \( \delta > 0 \) and a strictly increasing sequence \( {\left( {n}_{k}\right) }_{k \in \mathbb{N}} \) of integers such that \( {\rho }_{{n}_{k}} \geq \delta \) for all \( k \) . By restricting the sequence \( \left( {n}_{k}\right) \) if necessary, we can even assume \( {n}_{k + 1} \geq 6{n}_{k} \) for all \( k \) .

Ensuite, on pose

> Next, we set

\[
{I}_{1} = \left\lbrack  {\frac{1}{{n}_{1}}\left( {{\theta }_{{n}_{1}} - \frac{\pi }{3}}\right) ,\frac{1}{{n}_{1}}\left( {{\theta }_{{n}_{1}} + \frac{\pi }{3}}\right) }\right\rbrack  ,
\]

de sorte que pour tout \( t \in {I}_{1},\cos \left( {{n}_{1}t - {\theta }_{{n}_{1}}}\right) \geq 1/2 \) . Lorsque \( t \) parcourt \( {I}_{1},{n}_{2}t - {\theta }_{{n}_{2}} \) parcourt un intervalle de longueur \( {n}_{2} \cdot {2\pi }/\left( {3{n}_{1}}\right) \geq {4\pi } \) . On peut donc trouver un segment \( {I}_{2} \subset {I}_{1} \) de longueur \( {2\pi }/\left( {3{n}_{2}}\right) \) tel que \( \cos \left( {{n}_{2}t - {\theta }_{{n}_{2}}}\right) \geq 1/2 \) pour tout \( t \in {I}_{2} \) . En itérant le procédé, on construit ainsi pour tout \( k \) un segment \( {I}_{k} \subset {I}_{k - 1} \) de longueur \( {2\pi }/\left( {3{n}_{k}}\right) \) tel que

> so that for all \( t \in {I}_{1},\cos \left( {{n}_{1}t - {\theta }_{{n}_{1}}}\right) \geq 1/2 \) . As \( t \) ranges over \( {I}_{1},{n}_{2}t - {\theta }_{{n}_{2}} \) , it covers an interval of length \( {n}_{2} \cdot {2\pi }/\left( {3{n}_{1}}\right) \geq {4\pi } \) . We can therefore find a segment \( {I}_{2} \subset {I}_{1} \) of length \( {2\pi }/\left( {3{n}_{2}}\right) \) such that \( \cos \left( {{n}_{2}t - {\theta }_{{n}_{2}}}\right) \geq 1/2 \) for all \( t \in {I}_{2} \) . By iterating the process, we thus construct for all \( k \) a segment \( {I}_{k} \subset {I}_{k - 1} \) of length \( {2\pi }/\left( {3{n}_{k}}\right) \) such that

\[
\forall t \in  {I}_{k},\;\cos \left( {{n}_{k}t - {\theta }_{{n}_{k}}}\right)  \geq  \frac{1}{2}.
\]

D’après la proposition 9 page 20, on sait qu’il existe \( \xi \in \mathbb{R} \) tel que \( { \cap }_{k \in \mathbb{N}}{I}_{k} = \{ \xi \} \) . Pour tout \( k \) , on a \( {\rho }_{{n}_{k}}\cos \left( {{n}_{k}\xi - {\theta }_{k}}\right) \geq \delta /2 \) , ce qui est absurde car \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\rho }_{n}\cos \left( {{n\xi } - {\theta }_{n}}\right) = 0 \) . La suite \( \left( {\rho }_{n}\right) \) converge donc vers 0 .

> According to proposition 9 on page 20, we know that there exists \( \xi \in \mathbb{R} \) such that \( { \cap }_{k \in \mathbb{N}}{I}_{k} = \{ \xi \} \) . For all \( k \) , we have \( {\rho }_{{n}_{k}}\cos \left( {{n}_{k}\xi - {\theta }_{k}}\right) \geq \delta /2 \) , which is absurd because \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\rho }_{n}\cos \left( {{n\xi } - {\theta }_{n}}\right) = 0 \) . The sequence \( \left( {\rho }_{n}\right) \) therefore converges to 0 .

3 / a) Pour tout \( x \) , on a \( \mathop{\lim }\limits_{{N \rightarrow + \infty }}\mathop{\sum }\limits_{{-N}}^{N}{c}_{n}{e}^{inx} = 0 \) , donc pour tout \( x,\mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{c}_{n}{e}^{inx} + }\right. \; \left. {{c}_{-n}{e}^{-{inx}}}\right) = 0 \) . D’après la question précédente, les suites \( \left( {c}_{n}\right) \) et \( \left( {c}_{-n}\right) \) convergent donc vers 0 . Elles sont donc bornées, et si \( M \) désigne un majorant du module de leur terme général, on a pour tout \( n \in {\mathbb{Z}}^{ * } \) la majoration \( \left| {{c}_{n}/{\left( in\right) }^{2}}\right| \leq M/{n}^{2} \) , ce qui assure l’existence et la continuité de \( F \) .

> 3 / a) For all \( x \) , we have \( \mathop{\lim }\limits_{{N \rightarrow + \infty }}\mathop{\sum }\limits_{{-N}}^{N}{c}_{n}{e}^{inx} = 0 \) , so for all \( x,\mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{c}_{n}{e}^{inx} + }\right. \; \left. {{c}_{-n}{e}^{-{inx}}}\right) = 0 \) . According to the previous question, the sequences \( \left( {c}_{n}\right) \) and \( \left( {c}_{-n}\right) \) therefore converge to 0 . They are thus bounded, and if \( M \) denotes an upper bound of the modulus of their general term, we have for all \( n \in {\mathbb{Z}}^{ * } \) the inequality \( \left| {{c}_{n}/{\left( in\right) }^{2}}\right| \leq M/{n}^{2} \) , which ensures the existence and continuity of \( F \) .

b) Un calcul donne immédiatement, pour tout \( x \in \mathbb{R} \) et pour tout \( h \neq 0 \)

> b) A calculation gives immediately, for all \( x \in \mathbb{R} \) and for all \( h \neq 0 \)

\[
\frac{F\left( {x + h}\right)  + F\left( {x - h}\right)  - {2F}\left( x\right) }{{h}^{2}} = {c}_{0} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {{c}_{n}{e}^{inx} + {c}_{-n}{e}^{-{inx}}}\right) {\left\lbrack  \frac{\sin \left( {{nh}/2}\right) }{\left( nh/2\right) }\right\rbrack  }^{2},
\]

donc d’après la question \( 1/,\mathrm{D}F\left( x\right) \) existe et \( \mathrm{D}F\left( x\right) = 0 \) pour tout \( x \in \mathbb{R} \) .

> so according to question \( 1/,\mathrm{D}F\left( x\right) \) exists and \( \mathrm{D}F\left( x\right) = 0 \) for all \( x \in \mathbb{R} \) .

c) On en déduit l’existence de \( \alpha ,\beta \in \mathbb{C} \) tels que

> c) We deduce the existence of \( \alpha ,\beta \in \mathbb{C} \) such that

\[
\forall x \in  \mathbb{R},\;F\left( x\right)  = {\alpha x} + \beta  = {c}_{0}\frac{{x}^{2}}{2} + \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}\frac{{c}_{n}}{{\left( in\right) }^{2}}{e}^{inx}.
\]

Ceci montre que la fonction \( x \mapsto {\alpha x} + \beta - \frac{{c}_{0}}{2}{x}^{2} \) est \( {2\pi } \) -périodique. Donc \( \alpha = {c}_{0} = 0 \) et

> This shows that the function \( x \mapsto {\alpha x} + \beta - \frac{{c}_{0}}{2}{x}^{2} \) is \( {2\pi } \) -periodic. Thus \( \alpha = {c}_{0} = 0 \) and

\[
\forall x \in  \mathbb{R},\;\beta  = \mathop{\sum }\limits_{{n \in  {\mathbb{Z}}^{ * }}}\frac{{c}_{n}}{{\left( in\right) }^{2}}{e}^{inx}.
\]

Nous avons vu plus haut que la famille \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) est bornée, la série trigonométrique de l’égalité précédente converge donc normalement sur \( \mathbb{R} \) . Elle est donc égale à sa série de Fourier, et comme c’est une constante, on en déduit \( {c}_{n}/{\left( in\right) }^{2} = 0 \) pour tout \( n \in {\mathbb{Z}}^{ * } \) . Finalement, on a \( {c}_{n} = 0 \) pour tout \( n \in \mathbb{Z} \) .

> We saw above that the family \( {\left( {c}_{n}\right) }_{n \in \mathbb{Z}} \) is bounded, so the trigonometric series of the previous equality converges normally on \( \mathbb{R} \) . It is therefore equal to its Fourier series, and since it is a constant, we deduce \( {c}_{n}/{\left( in\right) }^{2} = 0 \) for all \( n \in {\mathbb{Z}}^{ * } \) . Finally, we have \( {c}_{n} = 0 \) for all \( n \in \mathbb{Z} \) .

Remarque. Ce résultat a été démontré pour la première fois par Cantor en 1871. Cantor a ensuite affaibli les hypothèses, en recherchant des ensembles dit exceptionnels, tels que si une série trigonométrique converge vers 0 sauf peut être sur un tel ensemble, alors ses coefficients sont nuls. Ces considérations l'amenèrent peu à peu à construire la théorie des ensembles, en particulier la notion de puissance d'un ensemble (théorie de l'équipotence) que l'on connaît.

> Remark. This result was proven for the first time by Cantor in 1871. Cantor subsequently weakened the hypotheses by searching for so-called exceptional sets, such that if a trigonometric series converges to 0 except perhaps on such a set, then its coefficients are zero. These considerations gradually led him to construct set theory, in particular the notion of the cardinality of a set (theory of equipotence) that we know.
