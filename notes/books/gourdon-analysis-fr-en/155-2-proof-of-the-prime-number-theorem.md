### 2. Proof of the Prime Number Theorem

*Français : 2. Preuve du Théorème des nombres premiers*

Nous sommes maintenant armés pour démontrer le théorème des nombres premiers. Dans le problème ci-dessous, on utilisera les résultats établis dans les deux problèmes précédents.

> We are now equipped to prove the prime number theorem. In the problem below, we will use the results established in the two previous problems.

PROBLÉME 3 (THÉORÉME DES NOMBRES PREMIERS). 1/a) On considère la fonction \( F\left( s\right) = Z\left( s\right) - \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {\Lambda \left( n\right) - 1}\right) /{n}^{s} \) , que nous avons définie dans le problème 1 page 437. Nous avons vu que \( F \) , définie et continue sur \( D \) , est prolongeable en une fonction continue sur \( \bar{D} \) tout entier. Montrer l’identité

> PROBLEM 3 (PRIME NUMBER THEOREM). 1/a) Consider the function \( F\left( s\right) = Z\left( s\right) - \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {\Lambda \left( n\right) - 1}\right) /{n}^{s} \) , which we defined in problem 1 on page 437. We have seen that \( F \) , defined and continuous on \( D \) , can be extended to a continuous function on the entirety of \( \bar{D} \) . Show the identity

\[
\forall x > 1,\;{\int }_{0}^{x}\left( {\psi \left( y\right)  - \left\lbrack  y\right\rbrack  }\right) {dy} = \frac{{x}^{2}}{2\pi }{\int }_{-\infty }^{+\infty }\frac{F\left( {1 + {it}}\right) {x}^{it}}{\left( {1 + {it}}\right) \left( {2 + {it}}\right) }{dt},\;\text{ où }\;\psi \left( y\right)  = \mathop{\sum }\limits_{{1 \leq  n \leq  y}}\Lambda \left( n\right) .
\]

b) En déduire \( {\int }_{0}^{x}\psi \left( y\right) \sim {x}^{2}/2 \) lorsque \( x \rightarrow \infty \) .

> b) Deduce \( {\int }_{0}^{x}\psi \left( y\right) \sim {x}^{2}/2 \) when \( x \rightarrow \infty \) .

c) Montrer que \( \psi \left( x\right) \sim x \) lorsque \( x \rightarrow \infty \) .

> c) Show that \( \psi \left( x\right) \sim x \) when \( x \rightarrow \infty \) .

2/a) Pour alléger les notations, lorsque la lettre \( p \) apparaîtra dans un indice ceci signifiera forcément que \( p \) est un nombre premier. Montrer que

> 2/a) To simplify notation, whenever the letter \( p \) appears in an index, it will necessarily mean that \( p \) is a prime number. Show that

\[
\psi \left( x\right)  = \mathop{\sum }\limits_{{p \leq  x}}\left\lbrack  \frac{\log x}{\log p}\right\rbrack  \log p
\]

puis montrer que \( \pi \left( x\right) = \mathop{\sum }\limits_{{p \leq x}}1 \) (nombre de nombres premiers inférieurs à \( x \) ) vérifie \( \psi \left( x\right) \leq \pi \left( x\right) \log x \leq {2\psi }\left( x\right) . \)

> then show that \( \pi \left( x\right) = \mathop{\sum }\limits_{{p \leq x}}1 \) (number of prime numbers less than \( x \) ) satisfies \( \psi \left( x\right) \leq \pi \left( x\right) \log x \leq {2\psi }\left( x\right) . \)

b) Démontrer que \( \pi \left( x\right) = \psi \left( x\right) /\log x + O\left( {x/{\log }^{2}x}\right) \) . En déduire le théorème des nombres premiers : \( \pi \left( x\right) \sim x/\log x \) .

> b) Prove that \( \pi \left( x\right) = \psi \left( x\right) /\log x + O\left( {x/{\log }^{2}x}\right) \) . Deduce the prime number theorem: \( \pi \left( x\right) \sim x/\log x \) .

Solution. 1/a) Nous sommes dans les hypothèses de la formule de Perron établie au problème précédent, on en déduit que pour tout \( \sigma > 1 \) on a

> Solution. 1/a) We are under the hypotheses of Perron's formula established in the previous problem; we deduce that for all \( \sigma > 1 \) we have

\[
{\int }_{0}^{x}\left( {\psi \left( y\right)  - \left\lbrack  y\right\rbrack  }\right) {dy} = {\int }_{0}^{x}\mathop{\sum }\limits_{{1 \leq  n \leq  y}}\left( {\Lambda \left( n\right)  - 1}\right) {dy} = \frac{1}{2\pi }{\int }_{-\infty }^{+\infty }\frac{F\left( {\sigma  + {it}}\right) {x}^{1 + \sigma  + {it}}}{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }{dt}.
\]

(*)

> La borne sur \( \left| {F\left( {\sigma + {it}}\right) }\right| \) pour \( \left| t\right| \) suffisamment grand,établie à la fin du problème 1, entraîne qu’il existe \( M > 0 \) tel que \( \mid F\left( {\sigma + {it}}\right) \leq M{\log }^{9}\left( {2 + \left| t\right| }\right) \) pour \( 1 \leq \sigma \leq 2 \) et pour tout \( t \in \mathbb{R} \) . On en déduit que pour tout \( x > 1 \) on a

The bound on \( \left| {F\left( {\sigma + {it}}\right) }\right| \) for \( \left| t\right| \) sufficiently large, established at the end of problem 1, implies that there exists \( M > 0 \) such that \( \mid F\left( {\sigma + {it}}\right) \leq M{\log }^{9}\left( {2 + \left| t\right| }\right) \) for \( 1 \leq \sigma \leq 2 \) and for all \( t \in \mathbb{R} \) . We deduce that for all \( x > 1 \) we have

\[
\forall \sigma  \in  \left\lbrack  {1,2}\right\rbrack  ,\forall t \in  \mathbb{R},\;\left| \frac{F\left( {\sigma  + {it}}\right) {x}^{1 + \sigma  + {it}}}{\left( {\sigma  + {it}}\right) \left( {1 + \sigma  + {it}}\right) }\right|  \leq  \frac{M{\log }^{9}\left( {2 + \left| t\right| }\right) {x}^{3}}{1 + {t}^{2}}.
\]

La dernière fonction étant intégrable sur \( \mathbb{R} \) , l'hypothèse de domination est bien vérifiée donc l’intégrale de droite dans (*) est bien une fonction continue de \( \sigma \in \left\lbrack {1,2}\right\rbrack \) , en particulier en \( \sigma = 1 \) . L’égalité (*) a donc lieu également lorsque \( \sigma = 1 \) , d’où le résultat.

> Since the last function is integrable on \( \mathbb{R} \) , the domination hypothesis is indeed satisfied, so the integral on the right in (*) is indeed a continuous function of \( \sigma \in \left\lbrack {1,2}\right\rbrack \) , in particular at \( \sigma = 1 \) . The equality (*) therefore also holds when \( \sigma = 1 \) , hence the result.

b) Posons \( G\left( t\right) = F\left( {1 + {it}}\right) \times {\left( 1 + it\right) }^{-1} \times {\left( 2 + it\right) }^{-1} \) , fonction continue et intégrable sur \( \mathbb{R} \) . La formule établie à la question précédente s'écrit

> b) Let \( G\left( t\right) = F\left( {1 + {it}}\right) \times {\left( 1 + it\right) }^{-1} \times {\left( 2 + it\right) }^{-1} \) be a continuous and integrable function on \( \mathbb{R} \) . The formula established in the previous question is written

\[
{\int }_{0}^{x}\left( {\psi \left( y\right)  - \left\lbrack  y\right\rbrack  }\right) {dy} = {x}^{2}{\mathcal{F}}_{G}\left( {\log x}\right) ,\;{\mathcal{F}}_{G}\left( \alpha \right)  = \frac{1}{2\pi }{\int }_{-\infty }^{+\infty }G\left( t\right) {e}^{i\alpha t}{dt}.
\]

D’après le lemme de Riemann-Lebesgue (voir l’exercice 6 page 157), on a \( \mathop{\lim }\limits_{{\alpha \rightarrow + \infty }}{\mathcal{F}}_{G}\left( \alpha \right) = 0 \) , donc ceci entraîne \( {\int }_{0}^{x}\left( {\psi \left( y\right) - \left\lbrack y\right\rbrack }\right) {dy} = o\left( {x}^{2}\right) \) . Comme \( y - 1 < \left\lbrack y\right\rbrack \leq y \) on a \( {\int }_{0}^{x}\left( {y - 1}\right) {dy} \leq \; {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} \leq {\int }_{0}^{x}{ydy} \) d’où on déduit \( {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} = {x}^{2}/2 + o\left( {x}^{2}\right) \) , et finalement \( {\int }_{0}^{x}\psi \left( y\right) {dy} = {\int }_{0}^{x}(\psi \left( y\right) - \; \left. \left\lbrack y\right\rbrack \right) {dy} + {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} = {x}^{2}/2 + o\left( {x}^{2}\right) . \)

> According to the Riemann-Lebesgue lemma (see exercise 6 on page 157), we have \( \mathop{\lim }\limits_{{\alpha \rightarrow + \infty }}{\mathcal{F}}_{G}\left( \alpha \right) = 0 \), so this implies \( {\int }_{0}^{x}\left( {\psi \left( y\right) - \left\lbrack y\right\rbrack }\right) {dy} = o\left( {x}^{2}\right) \). Since \( y - 1 < \left\lbrack y\right\rbrack \leq y \) we have \( {\int }_{0}^{x}\left( {y - 1}\right) {dy} \leq \; {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} \leq {\int }_{0}^{x}{ydy} \) from which we deduce \( {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} = {x}^{2}/2 + o\left( {x}^{2}\right) \), and finally \( {\int }_{0}^{x}\psi \left( y\right) {dy} = {\int }_{0}^{x}(\psi \left( y\right) - \; \left. \left\lbrack y\right\rbrack \right) {dy} + {\int }_{0}^{x}\left\lbrack y\right\rbrack {dy} = {x}^{2}/2 + o\left( {x}^{2}\right) . \)

c) Soit \( \varepsilon > 0\left( {\varepsilon < 1/2}\right) \) . De ce qui précède, on déduit, la fonction \( \psi \) étant croissante

> c) Let \( \varepsilon > 0\left( {\varepsilon < 1/2}\right) \). From the above, we deduce, since the function \( \psi \) is increasing

\[
\frac{{x}^{2}}{2} - \frac{{x}^{2}{\left( 1 - \varepsilon \right) }^{2}}{2} + o\left( {x}^{2}\right)  \leq  {\int }_{x\left( {1 - \varepsilon }\right) }^{x}\psi \left( y\right) {dy} \leq  {\varepsilon x\psi }\left( x\right)  \leq  {\int }_{x}^{x\left( {1 + \varepsilon }\right) }\psi \left( y\right) {dy} \leq  \frac{{x}^{2}{\left( 1 + \varepsilon \right) }^{2}}{2} - \frac{{x}^{2}}{2} + o\left( {x}^{2}\right)
\]

d’où, en divisant par \( {\varepsilon x} \) on tire \( \left( {1 - \varepsilon /2}\right) x + o\left( x\right) \leq \psi \left( x\right) \leq \left( {1 + \varepsilon /2}\right) x + o\left( x\right) \) . Comme on peut avoir les petits \( o\left( x\right) \) plus petits que \( \frac{\varepsilon }{2}x \) en valeur absolue pour \( x \) suffisamment grand, ceci entraîne \( \left( {1 - \varepsilon }\right) x \leq \psi \left( x\right) \leq \left( {1 + \varepsilon }\right) x \) pour \( x \) assez grand.

> from which, by dividing by \( {\varepsilon x} \) we obtain \( \left( {1 - \varepsilon /2}\right) x + o\left( x\right) \leq \psi \left( x\right) \leq \left( {1 + \varepsilon /2}\right) x + o\left( x\right) \). Since we can have the small \( o\left( x\right) \) smaller than \( \frac{\varepsilon }{2}x \) in absolute value for \( x \) sufficiently large, this implies \( \left( {1 - \varepsilon }\right) x \leq \psi \left( x\right) \leq \left( {1 + \varepsilon }\right) x \) for \( x \) large enough.

2/a) On peut écrire

> 2/a) We can write

\[
\psi \left( x\right)  = \mathop{\sum }\limits_{{p \leq  x}}\left( {\mathop{\sum }\limits_{{k \geq  1,{p}^{k} \leq  x}}\log p}\right) ,
\]

et comme le nombre d’entiers \( k \geq 1 \) tels que \( {p}^{k} \leq x \) est égal à \( \left\lbrack {\log x/\log p}\right\rbrack \) , on en déduit la formule voulue pour \( \psi \left( x\right) \) .

> and since the number of integers \( k \geq 1 \) such that \( {p}^{k} \leq x \) is equal to \( \left\lbrack {\log x/\log p}\right\rbrack \), we deduce the desired formula for \( \psi \left( x\right) \).

Pour tout nombre réel \( u \geq 1 \) , l’inégalité \( \left\lbrack u\right\rbrack \leq u < \left\lbrack u\right\rbrack + 1 \leq 2\left\lbrack u\right\rbrack \) entraîne \( \left\lbrack {\log x/\log p}\right\rbrack \log p \leq \; \log x \leq 2\left\lbrack {\log x/\log p}\right\rbrack \) donc \( \psi \left( x\right) \leq \pi \left( x\right) \log x \leq {2\psi }\left( x\right) . \)

> For any real number \( u \geq 1 \), the inequality \( \left\lbrack u\right\rbrack \leq u < \left\lbrack u\right\rbrack + 1 \leq 2\left\lbrack u\right\rbrack \) implies \( \left\lbrack {\log x/\log p}\right\rbrack \log p \leq \; \log x \leq 2\left\lbrack {\log x/\log p}\right\rbrack \) therefore \( \psi \left( x\right) \leq \pi \left( x\right) \log x \leq {2\psi }\left( x\right) . \)

b) On a déjà montré \( 0 \leq \pi \left( x\right) \log x - \psi \left( x\right) \) , majorons maintenant cette quantité. On a

> b) We have already shown \( 0 \leq \pi \left( x\right) \log x - \psi \left( x\right) \), let us now bound this quantity. We have

\[
\pi \left( x\right) \log x - \psi \left( x\right)  = \mathop{\sum }\limits_{{p \leq  x}}\left( {\log x - \left\lbrack  \frac{\log x}{\log p}\right\rbrack  \log p}\right)  = \mathop{\sum }\limits_{{p \leq  \sqrt{x}}}\left( {\log x - \left\lbrack  \frac{\log x}{\log p}\right\rbrack  \log p}\right)  + \mathop{\sum }\limits_{{\sqrt{x} < p \leq  x}}\log \left( \frac{x}{p}\right)
\]

car lorsque \( \sqrt{x} < p \leq x \) on a \( 1 \leq \log x/\log p < 2 \) donc \( \left\lbrack {\log x/\log p}\right\rbrack = 1 \) . Maintenant l’inégalité \( \left\lbrack \frac{\log x}{\log p}\right\rbrack \geq \frac{\log x}{\log p} - 1 \) et le fait que \( \pi \left( n\right) - \pi \left( {n - 1}\right) = 1 \) si \( n \) est premier, \( = 0 \) sinon, entraîne

> for when \( \sqrt{x} < p \leq x \) we have \( 1 \leq \log x/\log p < 2 \) thus \( \left\lbrack {\log x/\log p}\right\rbrack = 1 \) . Now the inequality \( \left\lbrack \frac{\log x}{\log p}\right\rbrack \geq \frac{\log x}{\log p} - 1 \) and the fact that \( \pi \left( n\right) - \pi \left( {n - 1}\right) = 1 \) if \( n \) is prime, \( = 0 \) otherwise, implies

\[
\pi \left( x\right) \log x - \psi \left( x\right)  \leq  \mathop{\sum }\limits_{{p \leq  \sqrt{x}}}\log p + \mathop{\sum }\limits_{{\sqrt{x} < n \leq  x}}\left( {\pi \left( n\right)  - \pi \left( {n - 1}\right) }\right) \log \left( \frac{x}{n}\right) ,
\]

et grâce à une transformation d'Abel sur la dernière somme, on obtient

> and thanks to an Abel transformation on the last sum, we obtain

\[
\pi \left( x\right) \log x - \psi \left( x\right)  \leq  \sqrt{x}\log \sqrt{x} + \mathop{\sum }\limits_{{\sqrt{x} < n \leq  x - 1}}\pi \left( n\right) \left( {\log \frac{x}{n} - \log \frac{x}{n + 1}}\right)  + \pi \left( x\right) \log \frac{x}{\left\lbrack  x\right\rbrack  }.
\]

Pour \( x \geq 1 \) on a \( \log \left( {x/\left\lbrack x\right\rbrack }\right) < \log \left( 2\right) \) , et on sait que \( \pi \left( x\right) \leq {2\psi }\left( x\right) /\log \left( x\right) = O\left( {x/\log x}\right) \) . Par ailleurs \( \log \frac{x}{n} - \log \frac{x}{n + 1} = \log \frac{n + 1}{n} = {\int }_{n}^{n + 1}{dt}/t \) , donc tout ceci entraîne

> For \( x \geq 1 \) we have \( \log \left( {x/\left\lbrack x\right\rbrack }\right) < \log \left( 2\right) \) , and we know that \( \pi \left( x\right) \leq {2\psi }\left( x\right) /\log \left( x\right) = O\left( {x/\log x}\right) \) . Furthermore \( \log \frac{x}{n} - \log \frac{x}{n + 1} = \log \frac{n + 1}{n} = {\int }_{n}^{n + 1}{dt}/t \) , so all this implies

\[
\pi \left( x\right) \log x - \psi \left( x\right)  \leq  \mathop{\sum }\limits_{{\sqrt{x} < n \leq  x - 1}}\pi \left( n\right) {\int }_{n}^{n + 1}\frac{dt}{t} + O\left( \frac{x}{\log x}\right)  \leq  {\int }_{1}^{x}\frac{\pi \left( t\right) }{t}{dt} + O\left( \frac{x}{\log x}\right) .
\]

Comme \( \pi \left( x\right) = O\left( {x/\log x}\right) \) , on a \( {\int }_{1}^{x}\pi \left( t\right) /{tdt} = O\left( {{\int }_{1}^{x}{dt}/\log t}\right) = O\left( {x/\log x}\right) \) (voir le théorème 3 page 163), donc on a finalement démontré \( 0 \leq \pi \left( x\right) \log x - \psi \left( x\right) \leq O\left( {x/\log x}\right) \) . Ainsi, on a bien \( \pi \left( x\right) = \psi \left( x\right) /\log \left( x\right) + O\left( {x/{\log }^{2}x}\right) \) . On en déduit facilement le théorème des nombres premiers \( \operatorname{car}\psi \left( x\right) = x + o\left( x\right) \) donc \( \pi \left( x\right) = x/\log x + o\left( {x/\log x}\right) . \)

> Since \( \pi \left( x\right) = O\left( {x/\log x}\right) \) , we have \( {\int }_{1}^{x}\pi \left( t\right) /{tdt} = O\left( {{\int }_{1}^{x}{dt}/\log t}\right) = O\left( {x/\log x}\right) \) (see theorem 3 page 163), so we have finally proven \( 0 \leq \pi \left( x\right) \log x - \psi \left( x\right) \leq O\left( {x/\log x}\right) \) . Thus, we indeed have \( \pi \left( x\right) = \psi \left( x\right) /\log \left( x\right) + O\left( {x/{\log }^{2}x}\right) \) . We easily deduce the prime number theorem \( \operatorname{car}\psi \left( x\right) = x + o\left( x\right) \) therefore \( \pi \left( x\right) = x/\log x + o\left( {x/\log x}\right) . \)
