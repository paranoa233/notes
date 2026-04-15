#### 3.4. Estimation and convergence

*Français : 3.4. Estimations et convergence*

PROPOSITION 14 (INÉGALITÉ DE MARKOV). Soit \( X \) une variable aléatoire discrète réelle, admettant une espérance. Alors

> PROPOSITION 14 (MARKOV'S INEQUALITY). Let \( X \) be a real discrete random variable admitting an expectation. Then

\[
\forall a > 0,\;P\left( {\left| X\right|  \geq  a}\right)  \leq  \frac{E\left( \left| X\right| \right) }{a}.
\]

Si \( X \) admet une variance, on a

> If \( X \) admits a variance, we have

\[
\forall a > 0,\;P\left( {\left| X\right|  \geq  a}\right)  \leq  \frac{E\left( {X}^{2}\right) }{{a}^{2}}.
\]

En appliquant cette proposition à \( \varphi \left( X\right) \) où \( \varphi \) est une fonction croissante positive, on obtient le corollaire suivant :

> By applying this proposition to \( \varphi \left( X\right) \) where \( \varphi \) is a positive increasing function, we obtain the following corollary:

COROLLAIRE 1. Soit \( \varphi \) une fonction positive croissante sur un intervalle réel I. Soit \( X \) une variable aléatoire discrète à valeurs dans I. Si \( \varphi \left( X\right) \) admet une espérance, on a

> COROLLARY 1. Let \( \varphi \) be a positive increasing function on a real interval I. Let \( X \) be a discrete random variable with values in I. If \( \varphi \left( X\right) \) admits an expectation, we have

\[
\forall a > 0,\;P\left( {X \geq  a}\right)  \leq  \frac{E\left( {\varphi \left( X\right) }\right) }{\varphi \left( a\right) }.
\]

Démonstration. La preuve est immédiate (à refaire à chaque fois) : la croissance de \( \varphi \) implique \( \{ X \geq a\} \subset \{ \varphi \left( X\right) \geq \varphi \left( a\right) \} \) , donc l’inégalité de Markov appliquée à \( \varphi \left( X\right) \) permet d’écrire

> Proof. The proof is immediate (to be redone each time): the growth of \( \varphi \) implies \( \{ X \geq a\} \subset \{ \varphi \left( X\right) \geq \varphi \left( a\right) \} \), so Markov's inequality applied to \( \varphi \left( X\right) \) allows us to write

\[
P\left( {X \geq  a}\right)  \leq  P\left( {\varphi \left( X\right)  \geq  \varphi \left( a\right) }\right)  \leq  \frac{E\left( {\varphi \left( X\right) }\right) }{\varphi \left( a\right) }.
\]

Remarque 13. - La deuxième inégalité de la proposition 15 est la conséquence de ce corollaire, appliqué à la variable aléatoire \( \left| X\right| \) et à \( \varphi \left( x\right) = {x}^{2} \) .

> Remark 13. - The second inequality of proposition 15 is a consequence of this corollary, applied to the random variable \( \left| X\right| \) and to \( \varphi \left( x\right) = {x}^{2} \).

- En appliquant ce corollaire à \( \varphi \left( x\right)  = {e}^{\lambda x} \) avec \( \lambda  > 0 \) , on aboutit à l’inégalité

> - By applying this corollary to \( \varphi \left( x\right)  = {e}^{\lambda x} \) with \( \lambda  > 0 \), we arrive at the inequality

\[
P\left( {X \leq  a}\right)  = P\left( {{e}^{\lambda X} \geq  {e}^{\lambda a}}\right)  \leq  \frac{E\left( {e}^{\lambda X}\right) }{{e}^{\lambda a}},
\]

valide si \( {e}^{\lambda X} \) admet une espérance. Cette inégalité est la première étape de la preuve de l'inégalité de Hoeffding (voir l'exercice 7 page 352).

> valid if \( {e}^{\lambda X} \) admits an expectation. This inequality is the first step in the proof of Hoeffding's inequality (see exercise 7 on page 352).

- En appliquant ce corollaire à la fonction \( \varphi \left( X\right)  = {\left( X - E\left( X\right) \right) }^{2} \) on obtient l’inégalité de Bienaymé-Tchébycheff ci-dessous.

> - By applying this corollary to the function \( \varphi \left( X\right)  = {\left( X - E\left( X\right) \right) }^{2} \), we obtain the Bienaymé-Chebyshev inequality below.

Proposition 15 (Inégalité de Bienaymé-Tchébycheff). Soit X une variable aléatoire discrète réelle, admettant une variance. Alors \( X \) admet une espérance et on a

> Proposition 15 (Bienaymé-Chebyshev inequality). Let X be a real discrete random variable admitting a variance. Then \( X \) admits an expectation and we have

\[
\forall a > 0,\;P\left( {\left| {X - E\left( X\right) }\right|  \geq  a}\right)  \leq  \frac{V\left( X\right) }{{a}^{2}}.
\]

PROPOSITION 16 (INEGALITÉ DE JENSEN). Soit \( X \) une variable aléatoire discrète, pre-nant ses valeurs dans un intervalle réel I et \( \varphi : I \rightarrow \mathbb{R} \) une fonction convexe. Alors si \( X \) et \( \varphi \left( X\right) \) admettent une espérance, on a

> PROPOSITION 16 (JENSEN'S INEQUALITY). Let \( X \) be a discrete random variable taking its values in a real interval I and \( \varphi : I \rightarrow \mathbb{R} \) be a convex function. Then if \( X \) and \( \varphi \left( X\right) \) admit an expectation, we have

\[
E\left( {\varphi \left( X\right) }\right)  \geq  \varphi \left( {E\left( X\right) }\right) .
\]

Démonstration. Comme \( \varphi \) est une fonction convexe, on peut écrire

> Proof. Since \( \varphi \) is a convex function, we can write

\[
\forall a \in  \mathbb{R},\exists {\lambda }_{a} \in  \mathbb{R};\;\forall x \in  I,\varphi \left( x\right)  \geq  \varphi \left( a\right)  + {\lambda }_{a}\left( {x - \varphi \left( a\right) }\right) .
\]

( \( \varphi \) étant convexe elle admet une dérivée à gauche \( {\varphi }_{\mathrm{g}}^{\prime }\left( a\right) \) et à droite \( {\varphi }_{\mathrm{d}}^{\prime }\left( a\right) \) pour tout \( a \in I \) . On choisit \( {\lambda }_{a} = {\varphi }_{\mathrm{g}}^{\prime }\left( a\right) \) , ou \( {\lambda }_{a} = {\varphi }_{\mathrm{d}}^{\prime }\left( a\right) \) dans le cas où \( I \) est fermé à gauche d’extrémité \( a \) ). L’inégalité précédente appliquée à \( a = E\left( X\right) \) entraîne \( \varphi \left( x\right) \geq \varphi \left( {E\left( X\right) }\right) + {\lambda }_{a}\left( {x - E\left( X\right) }\right) \) , donc en prenant les espérances de chaque membre on obtient

> (Since \( \varphi \) is convex, it admits a left derivative \( {\varphi }_{\mathrm{g}}^{\prime }\left( a\right) \) and a right derivative \( {\varphi }_{\mathrm{d}}^{\prime }\left( a\right) \) for all \( a \in I \). We choose \( {\lambda }_{a} = {\varphi }_{\mathrm{g}}^{\prime }\left( a\right) \), or \( {\lambda }_{a} = {\varphi }_{\mathrm{d}}^{\prime }\left( a\right) \) in the case where \( I \) is closed on the left with endpoint \( a \)). The previous inequality applied to \( a = E\left( X\right) \) leads to \( \varphi \left( x\right) \geq \varphi \left( {E\left( X\right) }\right) + {\lambda }_{a}\left( {x - E\left( X\right) }\right) \), so by taking the expectations of each member we obtain

\[
E\left( {\varphi \left( X\right) }\right)  \geq  \varphi \left( {E\left( X\right) }\right)  + {\lambda }_{a}E\left( {X - E\left( X\right) }\right)  = \varphi \left( {E\left( X\right) }\right) .
\]

Remarque 14. L'inégalité de Jensen n'est pas au programme des classes préparatoires mais se prouve facilement en reprenant la démonstration proposée ci-dessus. En l'appliquant à la fonction convexe \( \varphi \left( x\right) = {x}^{2} \) , on obtient l’inégalité \( E\left( {X}^{2}\right) \geq E{\left( X\right) }^{2} \) (qu’on obtient aussi à partir du théorème de Koënig-Huygens, car \( E\left( {X}^{2}\right) - E{\left( X\right) }^{2} = V\left( {X}^{2}\right) \geq 0 \) ). Plus généralement, pour tout \( p > q > 1 \) , l’inégalité de Jensen appliquée à \( \varphi \left( x\right) = {x}^{p/q} \) entraîne \( E\left( {X}^{p}\right) \geq E{\left( {X}^{q}\right) }^{p/q} \) , en particulier \( E\left( {X}^{p}\right) \geq E{\left( X\right) }^{p} \) .

> Remark 14. Jensen's inequality is not in the preparatory classes curriculum but is easily proven by following the proof proposed above. By applying it to the convex function \( \varphi \left( x\right) = {x}^{2} \), we obtain the inequality \( E\left( {X}^{2}\right) \geq E{\left( X\right) }^{2} \) (which is also obtained from the Koënig-Huygens theorem, because \( E\left( {X}^{2}\right) - E{\left( X\right) }^{2} = V\left( {X}^{2}\right) \geq 0 \)). More generally, for any \( p > q > 1 \), Jensen's inequality applied to \( \varphi \left( x\right) = {x}^{p/q} \) leads to \( E\left( {X}^{p}\right) \geq E{\left( {X}^{q}\right) }^{p/q} \), in particular \( E\left( {X}^{p}\right) \geq E{\left( X\right) }^{p} \).

Suites de variables aléatoires. Avant de présenter la loi faible des grands nombres, il convient de s'intéresser aux suites de variables aléatoires indépendantes. L'existence de telles suites indépendantes n'est pas évident a priori (de fait, l'espace Ω doit être assez grand et en général infini non dénombrable, voir l'exercice 5 page 351). Elle est garantie par le résultat suivant que nous admettrons (ceci est à rapprocher du résultat sur l’existence d’une probabilité sur \( {E}^{{\mathbb{N}}^{ * }} \) discutée page 326 dans le cas dénombrable des espaces de probabilités produits).

> Sequences of random variables. Before presenting the weak law of large numbers, it is appropriate to look at sequences of independent random variables. The existence of such independent sequences is not obvious a priori (in fact, the space Ω must be large enough and generally uncountably infinite, see exercise 5 on page 351). It is guaranteed by the following result which we will admit (this is to be compared with the result on the existence of a probability on \( {E}^{{\mathbb{N}}^{ * }} \) discussed on page 326 in the countable case of product probability spaces).

Proposition 17. Soit \( \left( {P}_{n}\right) \) une suite de probabilités sur \( \mathbb{R} \) , telles que pour tout \( n \) , il existe \( {S}_{n} \subset \mathbb{R} \) , au plus dénombrable, tel que \( {P}_{n}\left( {S}_{n}\right) = 1 \) . Alors il existe un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) et une suite de variables aléatoires discrètes \( \left( {X}_{n}\right) \) définies sur \( \Omega \) et mutuellement indépendantes, tels que chaque variable aléatoire \( {X}_{n} \) suit la loi \( {P}_{n} \) .

> Proposition 17. Let \( \left( {P}_{n}\right) \) be a sequence of probabilities on \( \mathbb{R} \), such that for all \( n \), there exists \( {S}_{n} \subset \mathbb{R} \), at most countable, such that \( {P}_{n}\left( {S}_{n}\right) = 1 \). Then there exists a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) and a sequence of discrete random variables \( \left( {X}_{n}\right) \) defined on \( \Omega \) and mutually independent, such that each random variable \( {X}_{n} \) follows the distribution \( {P}_{n} \).

Remarque 15. Un exemple classique est celui de l'existence d'une suite de variables aléa-toires indépendantes \( \left( {X}_{n}\right) \) suivant chacune une loi de Bernoulli de paramètre \( p \) . Dans ce cas, on peut prendre pour \( \Omega \) l’espace des suites \( \omega = {\left( {\omega }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \in \{ 0,1{\} }^{{\mathbb{N}}^{ * }} \) , et \( {X}_{n} \) définie par \( {X}_{n}\left( \omega \right) = {\omega }_{n} \in \{ 0,1\} \) (correspondant à l’expérience aléatoire du résultat du \( n \) -ième tirage à pile ou face).

> Remark 15. A classic example is that of the existence of a sequence of independent random variables \( \left( {X}_{n}\right) \) each following a Bernoulli distribution with parameter \( p \). In this case, we can take for \( \Omega \) the space of sequences \( \omega = {\left( {\omega }_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \in \{ 0,1{\} }^{{\mathbb{N}}^{ * }} \), and \( {X}_{n} \) defined by \( {X}_{n}\left( \omega \right) = {\omega }_{n} \in \{ 0,1\} \) (corresponding to the random experiment of the result of the \( n \)-th coin toss).

Loi faible des grands nombres. Nous nous limitons ici à la loi faible des grands nombres dans le cas des variables aléatoires admettant une variance, conformément au programme des classes préparatoires. Diverses généralisations, incluant la loi forte des grands nombres, sont discutées dans la remarque 16 plus bas.

> Weak law of large numbers. We limit ourselves here to the weak law of large numbers in the case of random variables admitting a variance, in accordance with the preparatory classes curriculum. Various generalizations, including the strong law of large numbers, are discussed in remark 16 below.

DéFINITION 11 (CONVERGENCE EN PROBABILITÉ). On dit qu'une suite \( \left( {X}_{n}\right) \) de variables aléatoires discrètes réelles sur \( \Omega \) converge en probabilité vers une variable aléatoire discrète réelle \( X \) si

> DEFINITION 11 (CONVERGENCE IN PROBABILITY). A sequence \( \left( {X}_{n}\right) \) of real discrete random variables on \( \Omega \) is said to converge in probability to a real discrete random variable \( X \) if

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {\left| {{X}_{n} - X}\right|  \geq  \varepsilon }\right)  = 0.
\]

\( \rightarrow \) THÉORÉME 1 (LOI FAIBLE DES GRANDS NOMBRES). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, mutuellement indépendantes, suivant une même loi (on dit alors que les \( {X}_{n} \) sont identiquement distribuées) admettant une espérance \( m \) et une variance \( {\sigma }^{2} \) . Alors la variable aléatoire \( {S}_{n}/n \) , où \( {S}_{n} = {X}_{1} + \ldots + {X}_{n} \) , converge en probabilité vers \( m \) , et plus précisément

> \( \rightarrow \) THEOREM 1 (WEAK LAW OF LARGE NUMBERS). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of real discrete random variables, mutually independent, following the same distribution (we then say that the \( {X}_{n} \) are identically distributed) admitting an expectation \( m \) and a variance \( {\sigma }^{2} \) . Then the random variable \( {S}_{n}/n \) , where \( {S}_{n} = {X}_{1} + \ldots + {X}_{n} \) , converges in probability to \( m \) , and more precisely

\[
\forall \varepsilon  > 0,\forall n \in  {\mathbb{N}}^{ * },\;P\left( {\left| {\frac{{S}_{n}}{n} - m}\right|  \geq  \varepsilon }\right)  \leq  \frac{{\sigma }^{2}}{n{\varepsilon }^{2}}.
\]

(*)

> Démonstration. L’inégalité (*) entraîne la convergence en probabilité de \( {S}_{n}/n \) vers \( m \) . En appli-quant l’inégalité de Bienaymé-Tchébycheff à \( {S}_{n} \) on a \( P\left( {\left| {{S}_{n}/n - E\left( {{S}_{n}/n}\right) }\right| \geq \varepsilon }\right) \leq \left( {V\left( {S}_{n}\right) /{n}^{2}}\right) /{\varepsilon }^{2} \) , d’où (*) car \( E\left( {{S}_{n}/n}\right) = m \) et l’indépendance de \( {X}_{1},\ldots ,{X}_{n} \) entraîne \( V\left( {S}_{n}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}V\left( {X}_{i}\right) = \; n{\sigma }^{2} \) .

Proof. Inequality (*) implies the convergence in probability of \( {S}_{n}/n \) to \( m \) . By applying Bienaymé-Chebyshev's inequality to \( {S}_{n} \) we have \( P\left( {\left| {{S}_{n}/n - E\left( {{S}_{n}/n}\right) }\right| \geq \varepsilon }\right) \leq \left( {V\left( {S}_{n}\right) /{n}^{2}}\right) /{\varepsilon }^{2} \) , hence (*) because \( E\left( {{S}_{n}/n}\right) = m \) and the independence of \( {X}_{1},\ldots ,{X}_{n} \) implies \( V\left( {S}_{n}\right) = \mathop{\sum }\limits_{{k = 1}}^{n}V\left( {X}_{i}\right) = \; n{\sigma }^{2} \) .

> Remarque 16. - Ce résultat exprime que l’erreur entre \( {S}_{n}/n \) et \( m \) a l’ordre de grandeur de \( 1/\sqrt{n} \) . L’estimation plus précise de la distribution de \( \sqrt{n}\left( {{S}_{n}/n - m}\right) \) fait l'objet du théorème central limite, qui exprime que cette distribution se rapproche d'une Gaussienne. Le théorème central limite n'est pas au programme des classes préparatoires, il fait l'objet du problème 9 page 386 dans le cas des variables aléa-toires entières.

Remark 16. - This result expresses that the error between \( {S}_{n}/n \) and \( m \) is of the order of magnitude of \( 1/\sqrt{n} \) . The more precise estimation of the distribution of \( \sqrt{n}\left( {{S}_{n}/n - m}\right) \) is the subject of the central limit theorem, which states that this distribution approaches a Gaussian. The central limit theorem is not in the preparatory classes curriculum; it is the subject of problem 9 on page 386 in the case of integer-valued random variables.

> - L’estimation (*) est en général très grossière lorsque \( \varepsilon \) est beaucoup plus grand que \( {n}^{-1/2} \) . L’inégalité de Hoeffding donne sous certaines conditions une estimation beaucoup plus fine des queues de probabilité (voir l'exercice 7 page 352).

- The estimation (*) is generally very coarse when \( \varepsilon \) is much larger than \( {n}^{-1/2} \) . Hoeffding's inequality provides, under certain conditions, a much finer estimation of probability tails (see exercise 7 on page 352).

> - La loi faible des grands nombres reste vraie même sans supposer que la loi commune des \( \left( {X}_{n}\right) \) admet un moment d’ordre 2 (voir l’exercice 12 page 362).

- The weak law of large numbers remains true even without assuming that the common distribution of the \( \left( {X}_{n}\right) \) admits a second-order moment (see exercise 12 on page 362).

> - La loi forte des grands nombres exprime que \( {S}_{n}/n \) converge vers \( m \) presque surement. Elle n'est pas au programme des classes préparatoires. Une démonstration dans des cas particuliers fait l'objet de l'exercice 7 page 352 (voir la remarque), ou de l'exercice 13 page 363. Une preuve dans le cas général est donnée dans le problème 10 page 389.

- The strong law of large numbers states that \( {S}_{n}/n \) converges to \( m \) almost surely. It is not in the preparatory classes curriculum. A proof in specific cases is the subject of exercise 7 on page 352 (see the remark), or exercise 13 on page 363. A proof in the general case is given in problem 10 on page 389.

> - Il existe plusieurs modes de convergence des suites de variables aléatoires (en pro-babilité, convergence presque sure, en loi, \( {\mathcal{L}}^{1},\ldots \) ). Ceci fait l’objet du problème 5 page 375.

- There are several modes of convergence for sequences of random variables (in probability, almost sure convergence, in distribution, \( {\mathcal{L}}^{1},\ldots \) ). This is the subject of problem 5 on page 375.
