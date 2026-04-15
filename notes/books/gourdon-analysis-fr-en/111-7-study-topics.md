### 7. Study topics

*Français : 7. Sujets d'étude*

SUJET D'ÉTUDE 1 (INTÉGRALES EULÉRIENNES : FONCTION GAMMA, FONCTION BÉTA).

> STUDY TOPIC 1 (EULERIAN INTEGRALS: GAMMA FUNCTION, BETA FUNCTION).

Le but de ce sujet d'étude est d'étudier et de donner quelques propriétés des fonctions gamma et bêta définies respectivement par

> The purpose of this study topic is to examine and provide some properties of the gamma and beta functions, defined respectively by

\[
\Gamma \left( x\right)  = {\int }_{0}^{+\infty }{e}^{-t}{t}^{x - 1}{dt}\;\left( {x > 0}\right) ,\;\mathrm{B}\left( {x, y}\right)  = {\int }_{0}^{1}{t}^{x - 1}{\left( 1 - t\right) }^{y - 1}{dt}\;\left( {x, y > 0}\right) .
\]

1/ (Fonction gamma.) a) Montrer que \( \Gamma \) est de classe \( {\mathcal{C}}^{\infty } \) et convexe sur \( {\mathbb{R}}^{+ * } \) .

> 1/ (Gamma function.) a) Show that \( \Gamma \) is of class \( {\mathcal{C}}^{\infty } \) and convex on \( {\mathbb{R}}^{+ * } \) .

b) Montrer que \( \Gamma \) est logarithmiquement convexe (i. e. que log \( \Gamma \) est convexe).

> b) Show that \( \Gamma \) is logarithmically convex (i.e., that log \( \Gamma \) is convex).

c) Montrer

> c) Show

\[
\forall x > 0,\;\Gamma \left( {x + 1}\right)  = {x\Gamma }\left( x\right) \;\text{ et }\;\forall n \in  \mathbb{N},\;\Gamma \left( {n + 1}\right)  = n!.
\]

d) Donner un équivalent de \( \Gamma \) en \( {0}^{ + } \) et tracer l’allure de son graphe.

> d) Provide an equivalent for \( \Gamma \) at \( {0}^{ + } \) and sketch its graph.

2 / (Fonction bêta.) a) Montrer que B vérifie les équations fonctionnelles

> 2/ (Beta function.) a) Show that B satisfies the functional equations

\[
\forall x, y > 0,\;\mathrm{B}\left( {x, y}\right)  = \mathrm{B}\left( {y, x}\right) \;\text{ et }\;\mathrm{B}\left( {x + 1, y}\right)  = \frac{x}{x + y}\mathrm{\;B}\left( {x, y}\right) .
\]

b) Pour \( n \in {\mathbb{N}}^{ * } \) , on pose \( {I}_{n}\left( x\right) = {\int }_{0}^{n}{\left( 1 - \frac{t}{n}\right) }^{n}{t}^{x - 1}{dt} \) . Montrer que pour tout \( x > 0 \) , on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{I}_{n}\left( x\right) = \Gamma \left( x\right) \) . En exprimant \( {I}_{n}\left( x\right) \) en fonction de la fonction B, en déduire

> b) For \( n \in {\mathbb{N}}^{ * } \) , let \( {I}_{n}\left( x\right) = {\int }_{0}^{n}{\left( 1 - \frac{t}{n}\right) }^{n}{t}^{x - 1}{dt} \) . Show that for all \( x > 0 \) , we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{I}_{n}\left( x\right) = \Gamma \left( x\right) \) . By expressing \( {I}_{n}\left( x\right) \) in terms of the B function, deduce

\[
\Gamma \left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{n}^{x}n!}{x\left( {x + 1}\right) \cdots \left( {x + n}\right) }.
\]

c) Montrer que pour \( x, y > 0 \) fixés, \( \mathrm{B}\left( {x + n + 1, y}\right) \sim \Gamma \left( y\right) /{n}^{y} \) lorsque \( n \rightarrow + \infty \) . En déduire la formule

> c) Show that for fixed \( x, y > 0 \) , \( \mathrm{B}\left( {x + n + 1, y}\right) \sim \Gamma \left( y\right) /{n}^{y} \) as \( n \rightarrow + \infty \) . Deduce the formula

\[
\forall x, y > 0,\;\mathrm{B}\left( {x, y}\right)  = \frac{\Gamma \left( x\right) \Gamma \left( y\right) }{\Gamma \left( {x + y}\right) }.
\]

d) Calculer \( \Gamma \left( {1/2}\right) \) .

> d) Calculate \( \Gamma \left( {1/2}\right) \) .

3/ a) Démontrer la formule de Weierstrass :

> 3/ a) Prove the Weierstrass formula:

\[
\forall x > 0,\;\frac{1}{\Gamma \left( x\right) } = x{e}^{\gamma x}\mathop{\prod }\limits_{{n = 1}}^{{+\infty }}\left\lbrack  {\left( {1 + \frac{x}{n}}\right) {e}^{-x/n}}\right\rbrack  ,
\]

où \( \gamma \) est la constante d’Euler (le produit infini \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }} \) signifie \( \left. {\mathop{\lim }\limits_{{N \rightarrow + \infty }}\mathop{\prod }\limits_{{n = 1}}^{N}}\right) \) . b) Montrer la formule de duplication

> where \( \gamma \) is the Euler constant (the infinite product \( \mathop{\prod }\limits_{{n = 1}}^{{+\infty }} \) means \( \left. {\mathop{\lim }\limits_{{N \rightarrow + \infty }}\mathop{\prod }\limits_{{n = 1}}^{N}}\right) \) . b) Show the duplication formula

\[
\forall x > 0,\;{2}^{{2x} - 1}\Gamma \left( x\right) \Gamma \left( {x + \frac{1}{2}}\right)  = \sqrt{\pi }\Gamma \left( {2x}\right) .
\]

c) En utilisant le développement en produit infini de la fonction sinus (voir la question b) de l'exercice 2 page 273) montrer la formule des compléments

> c) Using the infinite product expansion of the sine function (see question b) of exercise 2 on page 273), show the reflection formula

\[
\forall x \in  \rbrack 0,1\lbrack ,\;\frac{1}{\Gamma \left( x\right) \Gamma \left( {1 - x}\right) } = \frac{\sin {\pi x}}{\pi }.
\]

d) Montrer la relation

> d) Show the relation

\[
\forall x > 0,\;\frac{{\Gamma }^{\prime }\left( x\right) }{\Gamma \left( x\right) } =  - \gamma  - \frac{1}{x} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{x}{n\left( {x + n}\right) }.
\]

En déduire \( {\int }_{0}^{+\infty }\left( {\log t}\right) {e}^{-t}{dt} = - \gamma \) .

> Deduce \( {\int }_{0}^{+\infty }\left( {\log t}\right) {e}^{-t}{dt} = - \gamma \) .

Solution. 1/ a) Remarquons tout d’abord que l’intégrale qui définit \( \Gamma \) est bien convergente lorsque \( x > 0 \) . Nous allons démontrer que la fonction \( \Gamma \) est de classe \( {\mathcal{C}}^{\infty } \) et que

> Solution. 1/ a) First, note that the integral defining \( \Gamma \) is indeed convergent when \( x > 0 \) . We will demonstrate that the function \( \Gamma \) is of class \( {\mathcal{C}}^{\infty } \) and that

\[
\forall p \in  \mathbb{N},\forall x > 0,\;{\Gamma }^{\left( p\right) }\left( x\right)  = {\int }_{0}^{+\infty }{\left( \log t\right) }^{p}{e}^{-t}{t}^{x - 1}{dt}.
\]

(*)

> On remarque que lorsque \( x \) est dans un segment \( \left\lbrack {a, b}\right\rbrack \subset \rbrack 0, + \infty \lbrack \) , l’intégrande de (*) vérifie

We note that when \( x \) is in a segment \( \left\lbrack {a, b}\right\rbrack \subset \rbrack 0, + \infty \lbrack \) , the integrand of (*) satisfies

\[
\left| {{\left( \log t\right) }^{p}{e}^{-t}{t}^{x - 1}}\right|  \leq  {\varphi }_{p}\left( t\right) ,\;{\varphi }_{p}\left( t\right)  = \left\{  \begin{array}{ll} {\left| \log t\right| }^{p}{t}^{a - 1} & \text{ si }t \in  \rbrack 0,1\rbrack \\  {\left( \log t\right) }^{p}{e}^{-t}{t}^{b - 1} & \text{ si }t > 1 \end{array}\right.
\]

et que la fonction \( {\varphi }_{p} \) est intégrable sur \( \rbrack 0, + \infty \left\lbrack \right. \) puisque lorsque \( t \rightarrow {0}^{ + } \) , on a \( {\varphi }_{p}\left( t\right) = o\left( {t}^{a/2 - 1}\right) \; \left( {\operatorname{car}{\left| \log t\right| }^{p}{t}^{a/2} = o\left( 1\right) }\right) \) et \( {\varphi }_{p}\left( t\right) = O\left( {e}^{-t/2}\right) \) lorsque \( t \rightarrow \infty \) .

> and that the function \( {\varphi }_{p} \) is integrable on \( \rbrack 0, + \infty \left\lbrack \right. \) since when \( t \rightarrow {0}^{ + } \) , we have \( {\varphi }_{p}\left( t\right) = o\left( {t}^{a/2 - 1}\right) \; \left( {\operatorname{car}{\left| \log t\right| }^{p}{t}^{a/2} = o\left( 1\right) }\right) \) and \( {\varphi }_{p}\left( t\right) = O\left( {e}^{-t/2}\right) \) when \( t \rightarrow \infty \) .

Soit \( \left\lbrack {a, b}\right\rbrack \) un segment inclus dans ] \( 0, + \infty \) [. Nous allons prouver par récurrence sur \( p \in \mathbb{N} \) que \( \Gamma \) est de classe \( {\mathcal{C}}^{p} \) sur \( \left\lbrack {a, b}\right\rbrack \) et que \( {\Gamma }^{\left( p\right) } \) vérifie la relation (*) sur cet intervalle. Comme ceci sera vrai pour tout segment inclus dans ] \( 0, + \infty \left\lbrack \right. \) , on aura prouvé le résultat sur \( \rbrack 0, + \infty \lbrack \) tout entier.

> Let \( \left\lbrack {a, b}\right\rbrack \) be a segment included in ] \( 0, + \infty \) [. We will prove by induction on \( p \in \mathbb{N} \) that \( \Gamma \) is of class \( {\mathcal{C}}^{p} \) on \( \left\lbrack {a, b}\right\rbrack \) and that \( {\Gamma }^{\left( p\right) } \) satisfies the relation (*) on this interval. As this will be true for any segment included in ] \( 0, + \infty \left\lbrack \right. \) , we will have proven the result on the whole of \( \rbrack 0, + \infty \lbrack \) .

Pour \( p = 0 \) , il s’agit de montrer que \( \Gamma \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) . La majoration \( \left| {{t}^{x - 1}{e}^{-t}}\right| \leq {\varphi }_{0}\left( t\right) \) avec \( {\varphi }_{0} \) intégrable sur \( \rbrack 0, + \infty \lbrack \) assure que l’hypothèse de domination du théorème de continuité sous le signe intégral est bien vérifiée. Comme par ailleurs l'intégrande de \( \Gamma \) est continue, ceci assure la continuité de \( \Gamma \) sur \( \left\lbrack {a, b}\right\rbrack \) .

> For \( p = 0 \) , it is a matter of showing that \( \Gamma \) is continuous on \( \left\lbrack {a, b}\right\rbrack \) . The bound \( \left| {{t}^{x - 1}{e}^{-t}}\right| \leq {\varphi }_{0}\left( t\right) \) with \( {\varphi }_{0} \) integrable on \( \rbrack 0, + \infty \lbrack \) ensures that the domination hypothesis of the continuity theorem under the integral sign is indeed satisfied. As the integrand of \( \Gamma \) is also continuous, this ensures the continuity of \( \Gamma \) on \( \left\lbrack {a, b}\right\rbrack \) .

Supposons maintenant l’hypothèse de récurrence vraie au rang \( p \) et montrons là au rang \( p + 1 \) . L’intégrande de (*) est bien continûment dérivable par rapport à \( x \) et sa dérivée est égale à \( {f}_{x}\left( t\right) = {\left( \log t\right) }^{p + 1}{t}^{x - 1}{e}^{-t} \) . Grâce à la majoration \( \left| {{f}_{x}\left( t\right) }\right| \leq {\varphi }_{p + 1}\left( t\right) \) lorsque \( x \in \left\lbrack {a, b}\right\rbrack \) , avec \( {\varphi }_{p + 1} \) intégrable, on peut appliquer le théorème de dérivation sous le signe intégral qui nous assure que \( {\Gamma }^{\left( p\right) } \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {a, b}\right\rbrack \) et que sa dérivée est égale à \( {\int }_{{\mathbb{R}}^{+ * }}{f}_{x} \) . Ainsi, l’hypothèse de récurrence est vraie au rang \( p + 1 \) . Ceci termine la preuve que \( \Gamma \) est bien de classe \( {\mathcal{C}}^{\infty } \) .

> Let us now assume the induction hypothesis is true at rank \( p \) and show it at rank \( p + 1 \) . The integrand of (*) is indeed continuously differentiable with respect to \( x \) and its derivative is equal to \( {f}_{x}\left( t\right) = {\left( \log t\right) }^{p + 1}{t}^{x - 1}{e}^{-t} \) . Thanks to the bound \( \left| {{f}_{x}\left( t\right) }\right| \leq {\varphi }_{p + 1}\left( t\right) \) when \( x \in \left\lbrack {a, b}\right\rbrack \) , with \( {\varphi }_{p + 1} \) integrable, we can apply the theorem of differentiation under the integral sign which ensures that \( {\Gamma }^{\left( p\right) } \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {a, b}\right\rbrack \) and that its derivative is equal to \( {\int }_{{\mathbb{R}}^{+ * }}{f}_{x} \) . Thus, the induction hypothesis is true at rank \( p + 1 \) . This completes the proof that \( \Gamma \) is indeed of class \( {\mathcal{C}}^{\infty } \) .

Pour montrer la convexité de \( \Gamma \) , il suffit de montrer que \( {\Gamma }^{\prime \prime } \) est positive, ce qui est immédiat car la relation (*) montre que \( {\Gamma }^{\prime \prime } \) a son intégrande positive.

> To show the convexity of \( \Gamma \) , it suffices to show that \( {\Gamma }^{\prime \prime } \) is positive, which is immediate because the relation (*) shows that \( {\Gamma }^{\prime \prime } \) has a positive integrand.

b) Posons \( g : x \mapsto \log \Gamma \left( x\right) \) . On a \( {g}^{\prime \prime } = \left( {\Gamma {\Gamma }^{\prime \prime } - {\Gamma }^{\prime 2}}\right) /{\Gamma }^{2} \) , il s’agit donc de montrer que \( {\Gamma }^{\prime 2} \leq \Gamma {\Gamma }^{\prime \prime } \) . Pour tout \( x > 0 \) , l’inégalité de Schwarz donne

> b) Let \( g : x \mapsto \log \Gamma \left( x\right) \) . We have \( {g}^{\prime \prime } = \left( {\Gamma {\Gamma }^{\prime \prime } - {\Gamma }^{\prime 2}}\right) /{\Gamma }^{2} \) , so it is a matter of showing that \( {\Gamma }^{\prime 2} \leq \Gamma {\Gamma }^{\prime \prime } \) . For all \( x > 0 \) , the Schwarz inequality gives

\[
{\left( {\int }_{0}^{+\infty }\left( {t}^{\left( {x - 1}\right) /2}{e}^{-t/2}\right) \left( {t}^{\left( {x - 1}\right) /2}\log t{e}^{-t/2}\right) dt\right) }^{2} \leq  {\int }_{0}^{+\infty }{t}^{x - 1}{e}^{-t}{dt} \cdot  {\int }_{0}^{+\infty }{\left( \log t\right) }^{2}{t}^{x - 1}{e}^{-t}{dt},
\]

ce qui est précisément l’inégalité \( {\Gamma }^{\prime }{\left( x\right) }^{2} \leq \Gamma \left( x\right) {\Gamma }^{\prime \prime }\left( x\right) \) .

> which is precisely the inequality \( {\Gamma }^{\prime }{\left( x\right) }^{2} \leq \Gamma \left( x\right) {\Gamma }^{\prime \prime }\left( x\right) \) .

c) Une intégration par parties donne

> c) Integration by parts gives

\[
\forall x > 0,\;\Gamma \left( {x + 1}\right)  = {\int }_{0}^{+\infty }{t}^{x}{e}^{-t}{dt} = {\left\lbrack  -{t}^{x}{e}^{-t}\right\rbrack  }_{0}^{+\infty } + {\int }_{0}^{+\infty }x{t}^{x - 1}{e}^{-t}{dt} = {x\Gamma }\left( x\right) .
\]

La seconde formule s’en déduit facilement par récurrence sur \( n \in \mathbb{N} \) , compte tenu du fait que \( \Gamma \left( 1\right) = {\int }_{0}^{+\infty }{e}^{-t}{dt} = 1. \)

> The second formula is easily deduced by induction on \( n \in \mathbb{N} \) , given the fact that \( \Gamma \left( 1\right) = {\int }_{0}^{+\infty }{e}^{-t}{dt} = 1. \)

d) Lorsque \( x \rightarrow {0}^{ + },{x\Gamma }\left( x\right) = \Gamma \left( {x + 1}\right) \sim \Gamma \left( 1\right) = 1 \) , autrement dit \( \Gamma \left( x\right) \sim 1/x \) lorsque \( x \rightarrow {0}^{ + } \) .

> d) When \( x \rightarrow {0}^{ + },{x\Gamma }\left( x\right) = \Gamma \left( {x + 1}\right) \sim \Gamma \left( 1\right) = 1 \) , in other words \( \Gamma \left( x\right) \sim 1/x \) when \( x \rightarrow {0}^{ + } \) .

Le comportement de \( \Gamma \) au voisinage de \( {0}^{ + } \) nous donne un premier renseignement sur l’allure de son graphe. Notons que \( \Gamma \left( 1\right) = \Gamma \left( 2\right) = 1 \) , ce qui entraîne l’existence d’un point \( c \) de \( \rbrack 1,2\lbrack \) où \( {\Gamma }^{\prime } \) s’annule d’après le théorème de Rolle. Comme \( \Gamma \) est convexe, la fonction \( \Gamma \) croît sur \( \lbrack c, + \infty \lbrack \) , et comme \( \Gamma \left( {n + 1}\right) = n! \rightarrow + \infty \) , on en déduit que \( \Gamma \) tend vers \( + \infty \) en \( + \infty \) . De plus, \( \Gamma \left( {x + 1}\right) /x = \Gamma \left( x\right) \) , donc \( \Gamma \left( x\right) /x \) tend vers \( + \infty \) lorsque \( x \rightarrow + \infty \) , donc \( \Gamma \) admet une branche parabolique dans la direction verticale en \( + \infty \) . On en déduit l’allure du graphe de \( \Gamma \) (voir la figure ci-dessous).

> The behavior of \( \Gamma \) in the neighborhood of \( {0}^{ + } \) gives us initial information about the shape of its graph. Note that \( \Gamma \left( 1\right) = \Gamma \left( 2\right) = 1 \) , which implies the existence of a point \( c \) in \( \rbrack 1,2\lbrack \) where \( {\Gamma }^{\prime } \) vanishes according to Rolle's theorem. Since \( \Gamma \) is convex, the function \( \Gamma \) increases on \( \lbrack c, + \infty \lbrack \) , and since \( \Gamma \left( {n + 1}\right) = n! \rightarrow + \infty \) , we deduce that \( \Gamma \) tends to \( + \infty \) at \( + \infty \) . Furthermore, \( \Gamma \left( {x + 1}\right) /x = \Gamma \left( x\right) \) , so \( \Gamma \left( x\right) /x \) tends to \( + \infty \) when \( x \rightarrow + \infty \) , so \( \Gamma \) admits a parabolic branch in the vertical direction at \( + \infty \) . We deduce the shape of the graph of \( \Gamma \) (see the figure below).

2/ a) L’égalité \( \mathrm{B}\left( {x, y}\right) = \mathrm{B}\left( {y, x}\right) \) s’obtient en effectuant le changement de variable \( u = 1 - t \) dans l'intégrale définissant \( \mathrm{B}\left( {x, y}\right) \) .

> 2/ a) The equality \( \mathrm{B}\left( {x, y}\right) = \mathrm{B}\left( {y, x}\right) \) is obtained by performing the change of variable \( u = 1 - t \) in the integral defining \( \mathrm{B}\left( {x, y}\right) \) .

![bo_d7fjkrs91nqc73ereoog_321_506_195_527_507_0.jpg](images/gourdon_analysis_fr_en_012_bod7fjkrs91nqc73ereoog3215061955275070.jpg)

Figure 2. Le graphe de la fonction \( \Gamma \) .

> Figure 2. The graph of the function \( \Gamma \) .

Pour la seconde identité, on intègre par parties, en écrivant

> For the second identity, we integrate by parts, by writing

\[
\mathrm{B}\left( {x + 1, y}\right)  = {\int }_{0}^{1}{\left( \frac{t}{1 - t}\right) }^{x}{\left( 1 - t\right) }^{x + y - 1}{dt} = {\left\lbrack  -\frac{{\left( 1 - t\right) }^{x + y}}{x + y}{\left( \frac{t}{1 - t}\right) }^{x}\right\rbrack  }_{0}^{1}
\]

\[
+ \frac{x}{x + y}{\int }_{0}^{1}{\left( 1 - t\right) }^{x + y}{\left( \frac{t}{1 - t}\right) }^{x - 1}\frac{dt}{{\left( 1 - t\right) }^{2}} = \frac{x}{x + y}\mathrm{\;B}\left( {x, y}\right) ,
\]

ce qui prouve le résultat.

> which proves the result.

b) Fixons \( x > 0 \) . La suite de fonctions \( {\left( {g}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) définie sur \( {\mathbb{R}}^{+ * } \) par

> b) Let us fix \( x > 0 \) . The sequence of functions \( {\left( {g}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) defined on \( {\mathbb{R}}^{+ * } \) by

\[
{g}_{n}\left( t\right)  = {\left( 1 - \frac{t}{n}\right) }^{n}{t}^{x - 1}\;\text{ si }0 < t \leq  n,\;{g}_{n}\left( t\right)  = 0\;\text{ si }t > n
\]

converge simplement vers \( t \mapsto {e}^{-t}{t}^{x - 1} \) . De plus on a la majoration \( \left| {{g}_{n}\left( t\right) }\right| \leq {e}^{-t}{t}^{x - 1} \) (car \( {\left( 1 - t/n\right) }^{n} \leq {e}^{-t} \) sur \( \left\lbrack {0, n}\right\rbrack \) , conséquence de l’inégalité \( \log \left( {1 - u}\right) \leq - u \) qui s’obtient par l’égalité des accroissements finis), et comme \( t \mapsto {e}^{-t}{t}^{x - 1} \) est intégrable sur \( {\mathbb{R}}^{ + } \) , le théorème de convergence dominée nous assure de la convergence de \( {I}_{n}\left( x\right) = {\int }_{{\mathbb{R}}^{ + }}{g}_{n} \) vers \( \Gamma \left( x\right) \) .

> converges simply to \( t \mapsto {e}^{-t}{t}^{x - 1} \) . Furthermore, we have the bound \( \left| {{g}_{n}\left( t\right) }\right| \leq {e}^{-t}{t}^{x - 1} \) (since \( {\left( 1 - t/n\right) }^{n} \leq {e}^{-t} \) on \( \left\lbrack {0, n}\right\rbrack \) , a consequence of the inequality \( \log \left( {1 - u}\right) \leq - u \) which is obtained by the mean value theorem), and since \( t \mapsto {e}^{-t}{t}^{x - 1} \) is integrable on \( {\mathbb{R}}^{ + } \) , the dominated convergence theorem ensures the convergence of \( {I}_{n}\left( x\right) = {\int }_{{\mathbb{R}}^{ + }}{g}_{n} \) to \( \Gamma \left( x\right) \) .

Le changement de variable \( u = t/n \) dans l’intégrale \( {I}_{n}\left( x\right) \) donne \( {I}_{n}\left( x\right) = {n}^{x}\mathrm{\;B}\left( {x, n + 1}\right) \) . Compte tenu de la seconde identité de la question précédente, on a

> The change of variable \( u = t/n \) in the integral \( {I}_{n}\left( x\right) \) gives \( {I}_{n}\left( x\right) = {n}^{x}\mathrm{\;B}\left( {x, n + 1}\right) \) . Given the second identity from the previous question, we have

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathrm{B}\left( {x, n + 1}\right)  = \mathrm{B}\left( {n + 1, x}\right)  = \frac{n!}{\left( {x + 1}\right) \cdots \left( {x + n}\right) }\mathrm{B}\left( {1, x}\right)  = \frac{n!}{x\left( {x + 1}\right) \cdots \left( {x + n}\right) }
\]

\( \operatorname{car}\mathrm{B}\left( {1, x}\right) = {\int }_{0}^{1}{\left( 1 - t\right) }^{x - 1}{dt} = 1/x \) . On en déduit le résultat car on a montré que \( {I}_{n}\left( x\right) = \; {n}^{x}\mathrm{\;B}\left( {x, n + 1}\right) \) converge vers \( \Gamma \left( x\right) \) lorsque \( n \rightarrow + \infty \) .

> \( \operatorname{car}\mathrm{B}\left( {1, x}\right) = {\int }_{0}^{1}{\left( 1 - t\right) }^{x - 1}{dt} = 1/x \) . We deduce the result because we have shown that \( {I}_{n}\left( x\right) = \; {n}^{x}\mathrm{\;B}\left( {x, n + 1}\right) \) converges to \( \Gamma \left( x\right) \) as \( n \rightarrow + \infty \) .

c) On a \( \mathrm{B}\left( {x + n + 1, y}\right) = \mathrm{B}\left( {y, x + n + 1}\right) = {\int }_{0}^{1}{t}^{y - 1}{\left( 1 - t\right) }^{x + n}{dt} \) , et en effectuant le changement de variable \( t = u/n \) dans cette dernière intégrale, on s’aperçoit que

> c) We have \( \mathrm{B}\left( {x + n + 1, y}\right) = \mathrm{B}\left( {y, x + n + 1}\right) = {\int }_{0}^{1}{t}^{y - 1}{\left( 1 - t\right) }^{x + n}{dt} \) , and by performing the change of variable \( t = u/n \) in this last integral, we notice that

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathrm{\;B}\left( {x + n + 1, y}\right)  = \frac{1}{{n}^{y}}{\int }_{0}^{n}{u}^{y - 1}{\left( 1 - \frac{u}{n}\right) }^{x + n}{du}.
\]

Fixons \( x, y > 0 \) . Pour \( u \) fixé, \( {\left( 1 - u/n\right) }^{x} \) converge vers 1 lorsque \( n \rightarrow + \infty \) . Ainsi, la suite de fonctions \( {\left( {h}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) définie par \( {h}_{n}\left( u\right) = {u}^{y - 1}{\left( 1 - u/n\right) }^{x + n} \) si \( 0 < u \leq n,{h}_{n}\left( u\right) = 0 \) si \( u > n \) , converge simplement vers \( u \mapsto {u}^{y - 1}{e}^{-u} \) . La majoration par une fonction intégrable \( \left| {{h}_{n}\left( u\right) }\right| \leq {u}^{y - 1}{e}^{-u} \) permet d’appliquer le théorème de convergence dominée, ce qui assure que la dernière intégrale converge vers \( \Gamma \left( y\right) \) lorsque \( n \rightarrow + \infty \) . On a donc \( \mathrm{B}\left( {x + n + 1, y}\right) \sim \Gamma \left( y\right) /{n}^{y} \) lorsque \( n \rightarrow + \infty \) .

> Let us fix \( x, y > 0 \) . For fixed \( u \) , \( {\left( 1 - u/n\right) }^{x} \) converges to 1 as \( n \rightarrow + \infty \) . Thus, the sequence of functions \( {\left( {h}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) defined by \( {h}_{n}\left( u\right) = {u}^{y - 1}{\left( 1 - u/n\right) }^{x + n} \) if \( 0 < u \leq n,{h}_{n}\left( u\right) = 0 \) if \( u > n \) , converges pointwise to \( u \mapsto {u}^{y - 1}{e}^{-u} \) . The bound by an integrable function \( \left| {{h}_{n}\left( u\right) }\right| \leq {u}^{y - 1}{e}^{-u} \) allows the application of the dominated convergence theorem, which ensures that the last integral converges to \( \Gamma \left( y\right) \) as \( n \rightarrow + \infty \) . We therefore have \( \mathrm{B}\left( {x + n + 1, y}\right) \sim \Gamma \left( y\right) /{n}^{y} \) as \( n \rightarrow + \infty \) .

Maintenant, compte tenu de la seconde identité prouvée à la question \( 2/\mathrm{a} \) ), on a

> Now, given the second identity proven in question \( 2/\mathrm{a} \) ), we have

\[
\forall n \in  {\mathbb{N}}^{ * },\;\mathrm{B}\left( {x, y}\right)  = \frac{\left( {x + y}\right) \left( {x + y + 1}\right) \cdots \left( {x + y + n}\right) }{x\left( {x + 1}\right) \cdots \left( {x + n}\right) }\mathrm{B}\left( {x + n + 1, y}\right) ,
\]

et compte tenu de l’équivalent \( z\left( {z + 1}\right) \cdots \left( {z + n}\right) \sim {n}^{z}n!/\Gamma \left( z\right) \) valable pour tout \( z > 0 \) fixé (conséquence de la question précédente), on en déduit, lorsque \( n \rightarrow + \infty \)

> and given the equivalent \( z\left( {z + 1}\right) \cdots \left( {z + n}\right) \sim {n}^{z}n!/\Gamma \left( z\right) \) valid for any fixed \( z > 0 \) (a consequence of the previous question), we deduce, as \( n \rightarrow + \infty \)

\[
\mathrm{B}\left( {x, y}\right)  \sim  \frac{{n}^{x + y}n!/\Gamma \left( {x + y}\right) }{{n}^{x}n!/\Gamma \left( x\right) }\frac{\Gamma \left( y\right) }{{n}^{y}} = \frac{\Gamma \left( x\right) \Gamma \left( y\right) }{\Gamma \left( {x + y}\right) },
\]

d'où le résultat.

> hence the result.

d) La formule précédente donne \( \mathrm{B}\left( {1/2,1/2}\right) = \Gamma {\left( 1/2\right) }^{2}/\Gamma \left( 1\right) = \Gamma {\left( 1/2\right) }^{2} \) . Le changement de variable \( t = {\sin }^{2}u \) dans l’intégrale définissant \( \mathrm{B}\left( {1/2,1/2}\right) \) montre que \( \mathrm{B}\left( {1/2,1/2}\right) = \pi \) . Comme \( \Gamma \) est positive sur \( {\mathbb{R}}^{+ * } \) (c’est l’intégrale d’une fonction positive), on en déduit \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) .

> d) The previous formula gives \( \mathrm{B}\left( {1/2,1/2}\right) = \Gamma {\left( 1/2\right) }^{2}/\Gamma \left( 1\right) = \Gamma {\left( 1/2\right) }^{2} \) . The change of variable \( t = {\sin }^{2}u \) in the integral defining \( \mathrm{B}\left( {1/2,1/2}\right) \) shows that \( \mathrm{B}\left( {1/2,1/2}\right) = \pi \) . Since \( \Gamma \) is positive on \( {\mathbb{R}}^{+ * } \) (it is the integral of a positive function), we deduce \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) .

3/ a) Compte tenu de la relation \( \log n = 1 + \frac{1}{2} + \cdots + \frac{1}{n} - \gamma + o\left( 1\right) \) (voir page 211), on a

> 3/ a) Given the relation \( \log n = 1 + \frac{1}{2} + \cdots + \frac{1}{n} - \gamma + o\left( 1\right) \) (see page 211), we have

\[
\frac{x\left( {x + 1}\right) \cdots \left( {x + n}\right) }{{n}^{x}n!} = x{e}^{-x\log n}\mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + \frac{x}{k}}\right)  = x{e}^{\gamma x}{e}^{o\left( 1\right) }\mathop{\prod }\limits_{{k = 1}}^{n}{e}^{-x/k}\mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + \frac{x}{k}}\right) ,
\]

et ceci converge vers \( 1/\Gamma \left( x\right) \) d’après \( 2/\mathrm{b}) \) , d’où le résultat (remarquez que du même coup on a la convergence du produit infini).

> and this converges to \( 1/\Gamma \left( x\right) \) according to \( 2/\mathrm{b}) \) , hence the result (note that at the same time we have the convergence of the infinite product).

b) Fixons \( x > 0 \) . D’après la question \( 2/\mathrm{b} \) ), on a, lorsque \( n \rightarrow + \infty \) ,

> b) Let us fix \( x > 0 \) . According to question \( 2/\mathrm{b} \) ), we have, as \( n \rightarrow + \infty \) ,

\[
\Gamma \left( x\right) \Gamma \left( {x + \frac{1}{2}}\right)  \sim  \frac{{n}^{{2x} + 1/2}{\left( n!\right) }^{2}}{x\left( {x + 1/2}\right) \cdots \left( {x + n}\right) \left( {x + n + 1/2}\right) } = \frac{{2}^{{2n} + 2}{n}^{{2x} + 1/2}{\left( n!\right) }^{2}}{\left( {2x}\right) \left( {{2x} + 1}\right) \cdots \left( {{2x} + {2n} + 1}\right) }
\]

\[
\sim  \frac{\Gamma \left( {2x}\right) }{{\left( 2n + 1\right) }^{2x}\left( {{2n} + 1}\right) !}{2}^{{2n} + 2}{n}^{{2x} + 1/2}{\left( n!\right) }^{2} \sim  \frac{\Gamma \left( {2x}\right) {2}^{{2n} + 2}{n}^{1/2}{\left( n!\right) }^{2}}{{2}^{2x}\left( {2n}\right) !\left( {2n}\right) } = \frac{\Gamma \left( {2x}\right) {2}^{{2n} + 1 - {2x}}}{{n}^{1/2}}\frac{{\left( n!\right) }^{2}}{\left( {2n}\right) !}.
\]

Or d'après la formule de Stirling,

> However, according to Stirling's formula,

\[
\frac{{\left( n!\right) }^{2}}{\left( {2n}\right) !} \sim  \frac{{n}^{2n}{e}^{-{2n}}\left( {2\pi n}\right) }{{\left( 2n\right) }^{2n}{e}^{-{2n}}{\left( 4\pi n\right) }^{1/2}} = \frac{{\left( \pi n\right) }^{1/2}}{{2}^{2n}}
\]

(on peut aussi montrer ce résultat avec la formule de Wallis), et on en déduit finalement \( \Gamma \left( x\right) \Gamma \left( {x + 1/2}\right) \sim \Gamma \left( {2x}\right) {2}^{1 - {2x}}\sqrt{\pi } \) , d’où le résultat.

> (one can also show this result with Wallis's formula), and we finally deduce \( \Gamma \left( x\right) \Gamma \left( {x + 1/2}\right) \sim \Gamma \left( {2x}\right) {2}^{1 - {2x}}\sqrt{\pi } \) , hence the result.

c) Toujours en utilisant \( 2/\mathrm{b} \) ) on a, pour \( x \in \rbrack 0,1\lbrack \) fixé et lorsque \( n \rightarrow + \infty \) ,

> c) Still using \( 2/\mathrm{b} \) ) we have, for fixed \( x \in \rbrack 0,1\lbrack \) and as \( n \rightarrow + \infty \) ,

\[
\frac{1}{\Gamma \left( x\right) \Gamma \left( {1 - x}\right) } \sim  \frac{x\left( {1 + x}\right) \left( {1 + x/2}\right) \cdots \left( {1 + x/n}\right) }{{n}^{x}} \cdot  \frac{\left( {1 - x}\right) \left( {1 - x/2}\right) \cdots \left( {1 - x/n}\right) \left( {1 - x + n}\right) }{{n}^{1 - x}}
\]

\[
= \frac{x\left( {1 - x + n}\right) }{n}\left( {1 - {x}^{2}}\right) \left( {1 - \frac{{x}^{2}}{{2}^{2}}}\right) \cdots \left( {1 - \frac{{x}^{n}}{{n}^{2}}}\right)  \sim  x\mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 - \frac{{x}^{2}}{{k}^{2}}}\right)
\]

On conclut facilement avec le développement de la fonction sinus en produit infini.

> We conclude easily with the expansion of the sine function into an infinite product.

d) La formule de Weierstrass s'écrit aussi

> d) Weierstrass's formula is also written as

\[
\forall x > 0,\;\log \Gamma \left( x\right)  =  - \log x - {\gamma x} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left\lbrack  {\frac{x}{n} - \log \left( {1 + \frac{x}{n}}\right) }\right\rbrack  .
\]

\( \left( {* * }\right) \)

> En posant \( {f}_{n}\left( x\right) = x/n - \log \left( {1 + x/n}\right) \) pour tout \( n \in {\mathbb{N}}^{ * } \) et pour tout \( x \geq 0 \) , on a

By setting \( {f}_{n}\left( x\right) = x/n - \log \left( {1 + x/n}\right) \) for all \( n \in {\mathbb{N}}^{ * } \) and for all \( x \geq 0 \) , we have

\[
\forall x \geq  0,\forall n \in  {\mathbb{N}}^{ * },\;{f}_{n}^{\prime }\left( x\right)  = \frac{1}{n} - \frac{1}{n}\frac{1}{1 + x/n} = \frac{1}{n} - \frac{1}{n + x} = \frac{x}{n\left( {n + x}\right) }.
\]

Ainsi, pour tout \( A > 0 \) , on a \( \left| {{f}_{n}^{\prime }\left( x\right) }\right| \leq \frac{A}{{n}^{2}} \) pour tout \( x \in \left\lbrack {0, A}\right\rbrack \) , donc la série de fonctions \( \sum {f}_{n}^{\prime }\left( x\right) \) converge normalement sur \( \left\lbrack {0, A}\right\rbrack \) . Comme \( \sum {f}_{n} \) converge simplement sur \( {\mathbb{R}}^{+ * } \) (conséquence de l’existence de la formule (**)), on en déduit que la somme de cette série est dérivable sur \( \left\lbrack {0, A}\right\rbrack \) , et que sa dérivée est donnée par la somme de \( \sum {f}_{n}^{\prime } \) . Ainsi sur \( \rbrack 0, A\rbrack \) , la dérivée de \( \log \Gamma \) vérifie, d'après la formule (**),

> Thus, for all \( A > 0 \) , we have \( \left| {{f}_{n}^{\prime }\left( x\right) }\right| \leq \frac{A}{{n}^{2}} \) for all \( x \in \left\lbrack {0, A}\right\rbrack \) , so the series of functions \( \sum {f}_{n}^{\prime }\left( x\right) \) converges normally on \( \left\lbrack {0, A}\right\rbrack \) . Since \( \sum {f}_{n} \) converges pointwise on \( {\mathbb{R}}^{+ * } \) (a consequence of the existence of formula (**)), we deduce that the sum of this series is differentiable on \( \left\lbrack {0, A}\right\rbrack \) , and that its derivative is given by the sum of \( \sum {f}_{n}^{\prime } \) . Thus on \( \rbrack 0, A\rbrack \) , the derivative of \( \log \Gamma \) satisfies, according to formula (**),

\[
\frac{{\Gamma }^{\prime }\left( x\right) }{\Gamma \left( x\right) } =  - \frac{1}{x} - \gamma  + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{x}{n\left( {n + x}\right) }.
\]

Ceci est vrai sur \( \rbrack 0, A\rbrack \) pour tout \( A > 0 \) , donc sur \( {\mathbb{R}}^{+ * } \) . C’est en particulier vrai pour \( x = 1 \) , ce qui fournit, compte tenu du fait que \( \Gamma \left( 1\right) = 1 \) ,

> This is true on \( \rbrack 0, A\rbrack \) for all \( A > 0 \) , and therefore on \( {\mathbb{R}}^{+ * } \) . This is in particular true for \( x = 1 \) , which provides, given the fact that \( \Gamma \left( 1\right) = 1 \) ,

\[
{\Gamma }^{\prime }\left( 1\right)  =  - 1 - \gamma  + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{n\left( {n + 1}\right) } =  - \gamma  - 1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {\frac{1}{n} - \frac{1}{n + 1}}\right)  =  - \gamma  - 1 + 1 =  - \gamma .
\]

Comme \( {\Gamma }^{\prime }\left( 1\right) = {\int }_{0}^{+\infty }\left( {\log t}\right) {e}^{-t}{dt} \) (voir 1/a)), on en déduit le résultat.

> As \( {\Gamma }^{\prime }\left( 1\right) = {\int }_{0}^{+\infty }\left( {\log t}\right) {e}^{-t}{dt} \) (see 1/a)), we deduce the result.

SUJET D'ÉTUDE 2 (NOMBRES ET POLYNÔMES DE BERNOULLI). On définit la fonction

> STUDY TOPIC 2 (BERNOULLI NUMBERS AND POLYNOMIALS). We define the function

\[
f : \mathbb{C} \rightarrow  \mathbb{C}\;z \mapsto  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{n}}{\left( {n + 1}\right) !}\;\text{ qui vérifie }\;\forall z \in  {\mathbb{C}}^{ * },\;f\left( z\right)  = \frac{{e}^{z} - 1}{z}.
\]

Comme \( f\left( 0\right) = 1 \neq 0 \) , on sait (voir l’exercice 9 page 262) que \( 1/f \) est développable en série entière dans un disque \( \{ z \in \mathbb{C},\left| z\right| < r\} \) . Il existe donc une suite \( \left( {b}_{n}\right) \) telle que

> As \( f\left( 0\right) = 1 \neq 0 \), we know (see exercise 9 on page 262) that \( 1/f \) can be expanded as a power series in a disk \( \{ z \in \mathbb{C},\left| z\right| < r\} \). There therefore exists a sequence \( \left( {b}_{n}\right) \) such that

\[
\forall z \in  {\mathbb{C}}^{ * },\left| z\right|  < r,\;\frac{z}{{e}^{z} - 1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{b}_{n}}{n!}{z}^{n}.
\]

Les nombres \( {b}_{n} \) s’appellent les nombres de Bernoulli. On constate, par un produit de Cauchy, qu’il existe également une suite de polynômes \( \left( {B}_{n}\right) \) telle que

> The numbers \( {b}_{n} \) are called Bernoulli numbers. We observe, via a Cauchy product, that there also exists a sequence of polynomials \( \left( {B}_{n}\right) \) such that

\[
\forall x \in  \mathbb{C},\forall z \in  {\mathbb{C}}^{ * },\left| z\right|  < r,\;\frac{z{e}^{zx}}{{e}^{z} - 1} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( x\right) }{n!}{z}^{n}.
\]

Les polynômes \( {B}_{n} \) s’appellent les polynômes de Bernoulli.

> The polynomials \( {B}_{n} \) are called Bernoulli polynomials.

1/ a) En utilisant les propriétés de la fonction \( \left( {z, x}\right) \mapsto z{e}^{zx}/\left( {{e}^{z} - 1}\right) \) , montrer

> 1/ a) Using the properties of the function \( \left( {z, x}\right) \mapsto z{e}^{zx}/\left( {{e}^{z} - 1}\right) \), show

(i) \( \forall n \in \mathbb{N},\;{B}_{n}\left( {1 - x}\right) = {\left( -1\right) }^{n}{B}_{n}\left( x\right) \) (ii) \( \forall n \in {\mathbb{N}}^{ * },\;{B}_{n}^{\prime } = n{B}_{n - 1} \)

> (i) \( \forall n \in \mathbb{N},\;{B}_{n}\left( {1 - x}\right) = {\left( -1\right) }^{n}{B}_{n}\left( x\right) \) (ii) \( \forall n \in {\mathbb{N}}^{ * },\;{B}_{n}^{\prime } = n{B}_{n - 1} \)

(iii) \( \;\forall n \in {\mathbb{N}}^{ * },\;{B}_{n}\left( {x + 1}\right) - {B}_{n}\left( x\right) = n{x}^{n - 1} \) (iv) \( \forall n \geq 2,\;{B}_{n}\left( 0\right) = {B}_{n}\left( 1\right) \)

> (iii) \( \;\forall n \in {\mathbb{N}}^{ * },\;{B}_{n}\left( {x + 1}\right) - {B}_{n}\left( x\right) = n{x}^{n - 1} \) (iv) \( \forall n \geq 2,\;{B}_{n}\left( 0\right) = {B}_{n}\left( 1\right) \)

(v) \( \forall n \in {\mathbb{N}}^{ * },\;{\int }_{0}^{1}{B}_{n}\left( x\right) {dx} = 0 \) (vi) \( \forall n \in {\mathbb{N}}^{ * },\;{b}_{{2n} + 1} = 0 \) .

> (v) \( \forall n \in {\mathbb{N}}^{ * },\;{\int }_{0}^{1}{B}_{n}\left( x\right) {dx} = 0 \) (vi) \( \forall n \in {\mathbb{N}}^{ * },\;{b}_{{2n} + 1} = 0 \) .

b) Exprimer les polynômes de Bernoulli en fonction des nombres de Bernoulli. Montrer que \( {b}_{n} \in \mathbb{Q} \) pour tout \( n \in \mathbb{N} \) , et calculer \( {b}_{0},{b}_{1},{b}_{2},{b}_{4},{b}_{6} \) .

> b) Express the Bernoulli polynomials in terms of the Bernoulli numbers. Show that \( {b}_{n} \in \mathbb{Q} \) for all \( n \in \mathbb{N} \), and calculate \( {b}_{0},{b}_{1},{b}_{2},{b}_{4},{b}_{6} \) .

2 / Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {\widetilde{B}}_{n} \) l’application de \( \mathbb{R} \) dans \( \mathbb{R} \) ,1-périodique, qui coïncide avec \( {B}_{n} \) sur ] \( 0,1\left\lbrack \right. \) et telle que \( {\widetilde{B}}_{n}\left( 0\right) = \frac{1}{2}\left\lbrack {{B}_{n}\left( 0\right) + {B}_{n}\left( 1\right) }\right\rbrack \) .

> 2 / For all \( n \in {\mathbb{N}}^{ * } \), we denote by \( {\widetilde{B}}_{n} \) the mapping from \( \mathbb{R} \) to \( \mathbb{R} \), 1-periodic, which coincides with \( {B}_{n} \) on ] \( 0,1\left\lbrack \right. \) and such that \( {\widetilde{B}}_{n}\left( 0\right) = \frac{1}{2}\left\lbrack {{B}_{n}\left( 0\right) + {B}_{n}\left( 1\right) }\right\rbrack \) .

a) En procédant par récurrence, montrer que pour tout \( k \in {\mathbb{N}}^{ * } \) et pour tout \( x \in \mathbb{R} \)

> a) By proceeding by induction, show that for all \( k \in {\mathbb{N}}^{ * } \) and for all \( x \in \mathbb{R} \)

\[
\frac{{\widetilde{B}}_{2k}\left( x\right) }{\left( {2k}\right) !} = 2 \cdot  {\left( -1\right) }^{k + 1}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\cos \left( {2\pi nx}\right) }{{\left( 2n\pi \right) }^{2k}},\;\frac{{\widetilde{B}}_{{2k} - 1}\left( x\right) }{\left( {{2k} - 1}\right) !} = 2 \cdot  {\left( -1\right) }^{k}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\sin \left( {2\pi nx}\right) }{{\left( 2n\pi \right) }^{{2k} - 1}}.
\]

b) En déduire, pour tout \( k \in {\mathbb{N}}^{ * } \) , la valeur de \( \zeta \left( {2k}\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{n}^{-{2k}} \) en fonction de \( {b}_{2k} \) . c) Donner un équivalent de \( {b}_{2k} \) lorsque \( k \rightarrow + \infty \) .

> b) Deduce, for all \( k \in {\mathbb{N}}^{ * } \), the value of \( \zeta \left( {2k}\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{n}^{-{2k}} \) as a function of \( {b}_{2k} \). c) Give an equivalent of \( {b}_{2k} \) as \( k \rightarrow + \infty \).

Solution. 1/ a) (i). Soit \( x \in \mathbb{C} \) . Pour tout \( z \in \mathbb{C},0 < \left| z\right| < r \) , on a

> Solution. 1/ a) (i). Let \( x \in \mathbb{C} \). For all \( z \in \mathbb{C},0 < \left| z\right| < r \), we have

\[
\frac{z{e}^{z\left( {1 - x}\right) }}{{e}^{z} - 1} = \frac{\left( {-z}\right) {e}^{\left( {-z}\right) x}}{{e}^{-z} - 1}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( {1 - x}\right) }{n!}{z}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( x\right) }{n!}{\left( -z\right) }^{n}.
\]

Deux séries entières dont les sommes coïncident dans un voisinage de 0 ont les mêmes coefficients, on en déduit (i).

> Two power series whose sums coincide in a neighborhood of 0 have the same coefficients; we deduce (i) from this.

(ii). L'idée est de dériver terme à terme l'expression qui définit les polynômes de Bernoulli. Pour montrer que l’on a bien le droit de procéder ainsi, on fixe \( \rho \in \rbrack 0, r\lbrack \) et on utilise la formule de Cauchy (voir le théorème 4 page 250) qui donne

> (ii). The idea is to differentiate term by term the expression defining the Bernoulli polynomials. To show that we are justified in doing so, we fix \( \rho \in \rbrack 0, r\lbrack \) and use Cauchy's formula (see theorem 4 on page 250), which gives

\[
\forall x \in  \mathbb{R},\;{2\pi }{\rho }^{n}\frac{{B}_{n}\left( x\right) }{n!} = {\int }_{0}^{2\pi }f\left( {\rho {e}^{i\theta }, x}\right) {e}^{-{ni\theta }}{d\theta }\;\text{ où }\;f\left( {z, x}\right)  = \frac{z{e}^{zx}}{{e}^{z} - 1}.
\]

L’intégrande est continûment dérivable par rapport à \( x \) sur \( \mathbb{R} \) , on peut donc dériver sous le signe intégral ce qui donne, pour tout \( x \in \mathbb{R} \) ,

> The integrand is continuously differentiable with respect to \( x \) on \( \mathbb{R} \), so we can differentiate under the integral sign, which gives, for all \( x \in \mathbb{R} \),

\[
{2\pi }{\rho }^{n}\frac{{B}_{n}^{\prime }\left( x\right) }{n!} = {\int }_{0}^{2\pi }\frac{\partial f}{\partial x}\left( {\rho {e}^{i\theta }, x}\right) {e}^{-{ni\theta }}{d\theta } = {\int }_{0}^{2\pi }\rho {e}^{i\theta }f\left( {\rho {e}^{i\theta }, x}\right) {e}^{-{ni\theta }}{d\theta } = {2\pi }{\rho }^{n}\frac{{B}_{n - 1}\left( x\right) }{\left( {n - 1}\right) !},
\]

d’où on déduit \( {B}_{n}^{\prime } = n{B}_{n - 1} \) .

> from which we deduce \( {B}_{n}^{\prime } = n{B}_{n - 1} \).

(iii). On procède de manière analogue à (i). Soit \( x \in \mathbb{C} \) . Pour tout \( z \in \mathbb{C},0 < \left| z\right| < r \) , on a

> (iii). We proceed analogously to (i). Let \( x \in \mathbb{C} \). For all \( z \in \mathbb{C},0 < \left| z\right| < r \), we have

\[
\frac{z{e}^{z\left( {x + 1}\right) }}{{e}^{z} - 1} = z{e}^{zx} + \frac{z{e}^{zx}}{{e}^{z} - 1}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( {x + 1}\right) }{n!}{z}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{n}}{n!}{z}^{n} + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( x\right) }{n!}{z}^{n}
\]

et on conclut en identifiant les coefficients de \( {z}^{n} \) de part et d’autre de cette expression.

> and we conclude by identifying the coefficients of \( {z}^{n} \) on both sides of this expression.

(iv). C'est une conséquence immédiate de (iii) appliqué à \( x = 0 \) .

> (iv). This is an immediate consequence of (iii) applied to \( x = 0 \).

(v). C'est une conséquence de (ii) et (iv).

> (v). This is a consequence of (ii) and (iv).

(vi). L’assertion (i) entraîne \( {B}_{{2n} + 1}\left( 0\right) = - {B}_{{2n} + 1}\left( 1\right) \) , donc d’après (iv), \( {B}_{{2n} + 1}\left( 0\right) = 0 \) . Il suffit ensuite de remarquer que \( {B}_{k}\left( 0\right) = {b}_{k} \) pour tout \( k \) par définition des \( {b}_{k} \) et des \( {B}_{k}\left( x\right) \) .

> (vi). Assertion (i) implies \( {B}_{{2n} + 1}\left( 0\right) = - {B}_{{2n} + 1}\left( 1\right) \), so according to (iv), \( {B}_{{2n} + 1}\left( 0\right) = 0 \). It then suffices to note that \( {B}_{k}\left( 0\right) = {b}_{k} \) for all \( k \) by the definition of \( {b}_{k} \) and \( {B}_{k}\left( x\right) \).

b) Un produit de Cauchy donne, pour tout \( x \in \mathbb{C} \) et pour tout \( z \in {\mathbb{C}}^{ * },\left| z\right| < r \) ,

> b) A Cauchy product gives, for all \( x \in \mathbb{C} \) and for all \( z \in {\mathbb{C}}^{ * },\left| z\right| < r \),

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}\left( x\right) }{n!}{z}^{n} = \frac{z}{{e}^{z} - 1}{e}^{zx} = \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{b}_{n}}{n!}{z}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{n}}{n!}{z}^{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{b}_{n - k}}{\left( {n - k}\right) !}\frac{{x}^{k}}{k!}}\right) {z}^{n}
\]

donc en identifiant les coefficients de \( {z}^{n} \) de part et d’autre

> so by identifying the coefficients of \( {z}^{n} \) on both sides

\[
\forall n \in  \mathbb{N},\forall x \in  \mathbb{C},\;{B}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{b}_{n - k}{x}^{k}.
\]

Comme \( {B}_{n}\left( 1\right) = {B}_{n}\left( 0\right) = {b}_{n} \) pour tout \( n \geq 2 \) , cette dernière relation entraîne

> Since \( {B}_{n}\left( 1\right) = {B}_{n}\left( 0\right) = {b}_{n} \) for all \( n \geq 2 \), this last relation implies

\[
\forall n \geq  2,\;\mathop{\sum }\limits_{{k = 1}}^{n}{C}_{n}^{k}{b}_{n - k} = 0\;\text{ donc }\;{b}_{n - 1} =  - \frac{1}{n}\mathop{\sum }\limits_{{k = 2}}^{n}{C}_{n}^{k}{b}_{n - k} =  - \frac{1}{n}\mathop{\sum }\limits_{{k = 0}}^{{n - 2}}{C}_{n}^{k}{b}_{k}.
\]

En procédant par récurrence (sachant que \( {b}_{0} = 1/f\left( 0\right) = 1 \) ) ceci permet d’affirmer que \( {b}_{n} \in \mathbb{Q} \) pour tout \( n \in \mathbb{N} \) . De plus, cette relation de récurrence permet de calculer les \( {b}_{k} \) . On trouve \( {b}_{0} = 1,{b}_{1} = - 1/2,{b}_{2} = 1/6,{b}_{4} = - 1/{30},{b}_{6} = 1/{42} \) .

> By proceeding by induction (knowing that \( {b}_{0} = 1/f\left( 0\right) = 1 \)), this allows us to state that \( {b}_{n} \in \mathbb{Q} \) for all \( n \in \mathbb{N} \). Furthermore, this recurrence relation allows us to calculate the \( {b}_{k} \). We find \( {b}_{0} = 1,{b}_{1} = - 1/2,{b}_{2} = 1/6,{b}_{4} = - 1/{30},{b}_{6} = 1/{42} \).

2 / a) Les \( {\widetilde{B}}_{p} \) sont des fonctions 1-périodiques, continues par morceaux, et égales à la demi-somme de leur limite à gauche et à droite en leurs discontinuités, elles sont donc égales à leurs séries de Fourier. Par commodité, nous calculons les coefficients de Fourier \( {c}_{n}\left( {\widetilde{B}}_{p}\right) \) . Montrons que

> 2 / a) The \( {\widetilde{B}}_{p} \) are 1-periodic, piecewise continuous functions, equal to the average of their left and right limits at their points of discontinuity; they are therefore equal to their Fourier series. For convenience, we calculate the Fourier coefficients \( {c}_{n}\left( {\widetilde{B}}_{p}\right) \) . Let us show that

\[
\forall p \in  {\mathbb{N}}^{ * },\;{c}_{0}\left( {\widetilde{B}}_{p}\right)  = 0\;\text{ et }\;\forall n \in  {\mathbb{Z}}^{ * },\;{c}_{n}\left( {\widetilde{B}}_{p}\right)  = \frac{p!}{{\left( 2\pi ni\right) }^{p}}.
\]

(*)

> La première égalité de (*) est une conséquence de l'assertion (v) établie à la question 1/a).

The first equality of (*) is a consequence of assertion (v) established in question 1/a).

> Pour la seconde, nous procédons par récurrence sur \( p \in {\mathbb{N}}^{ * } \) . Pour \( p = 1 \) , on a \( {B}_{1}\left( x\right) = x - 1/2 \) d’après la question 1/b), donc une intégration par parties fournit, pour tout \( n \in {\mathbb{Z}}^{ * } \) ,

For the second, we proceed by induction on \( p \in {\mathbb{N}}^{ * } \) . For \( p = 1 \) , we have \( {B}_{1}\left( x\right) = x - 1/2 \) according to question 1/b), so integration by parts provides, for all \( n \in {\mathbb{Z}}^{ * } \) ,

\[
{c}_{n}\left( {\widetilde{B}}_{1}\right)  = {\int }_{0}^{1}\left( {x - \frac{1}{2}}\right) {e}^{-{2\pi nix}}{dx} = {\left\lbrack  \left( x - \frac{1}{2}\right) \frac{{e}^{-{2\pi nix}}}{-{2\pi ni}}\right\rbrack  }_{0}^{1} + \frac{1}{2\pi ni}{\int }_{0}^{1}{e}^{-{2\pi nix}}{dx} = \frac{1}{2\pi ni}.
\]

Supposons maintenant le résultat vrai au rang \( p - 1 \geq 1 \) et montrons le au rang \( p \) . On a \( p \geq 2 \) , donc \( {B}_{p}\left( 0\right) = {B}_{p}\left( 1\right) \) et comme de plus \( {B}_{p}^{\prime } = p{B}_{p - 1} \) , une intégration par parties entraîne

> Now assume the result is true at rank \( p - 1 \geq 1 \) and show it at rank \( p \) . We have \( p \geq 2 \) , so \( {B}_{p}\left( 0\right) = {B}_{p}\left( 1\right) \) and since, moreover, \( {B}_{p}^{\prime } = p{B}_{p - 1} \) , integration by parts leads to

\[
{c}_{n}\left( {\widetilde{B}}_{p}\right)  = {\int }_{0}^{1}{B}_{p}\left( x\right) {e}^{-{2\pi nix}}{dx} = \frac{1}{2\pi ni}{\int }_{0}^{1}p{B}_{p - 1}\left( x\right) {e}^{-{2\pi nix}}{dx} = \frac{p}{2\pi ni}{c}_{n}\left( {\widetilde{B}}_{p - 1}\right)  = \frac{p!}{{\left( 2\pi ni\right) }^{p}}.
\]

Ainsi, nous avons prouvé (*). Avec les relations liant les coefficients de Fourier \( {a}_{n}\left( {\widetilde{B}}_{p}\right) ,{b}_{n}\left( {\widetilde{B}}_{p}\right) \) aux \( {c}_{n}\left( {\widetilde{B}}_{p}\right) \) , on en déduit \( {a}_{0}\left( {\widetilde{B}}_{p}\right) = 0 \) pour tout \( p \in {\mathbb{N}}^{ * } \) , et pour tout \( k, n \in {\mathbb{N}}^{ * } \) ,

> Thus, we have proven (*). With the relations linking the Fourier coefficients \( {a}_{n}\left( {\widetilde{B}}_{p}\right) ,{b}_{n}\left( {\widetilde{B}}_{p}\right) \) to the \( {c}_{n}\left( {\widetilde{B}}_{p}\right) \) , we deduce \( {a}_{0}\left( {\widetilde{B}}_{p}\right) = 0 \) for all \( p \in {\mathbb{N}}^{ * } \) , and for all \( k, n \in {\mathbb{N}}^{ * } \) ,

\[
{a}_{n}\left( {\widetilde{B}}_{2k}\right)  = \frac{{\left( -1\right) }^{k + 1}2\left( {2k}\right) !}{{\left( 2n\pi \right) }^{2k}},\;{b}_{n}\left( {\widetilde{B}}_{2k}\right)  = 0,\;{a}_{n}\left( {\widetilde{B}}_{{2k} - 1}\right)  = 0,\;{b}_{n}\left( {\widetilde{B}}_{{2k} - 1}\right)  = \frac{{\left( -1\right) }^{k}2\left( {{2k} - 1}\right) !}{{\left( 2n\pi \right) }^{{2k} - 1}}.
\]

On en déduit le résultat car nous avons vu plus haut que les fonctions \( {\widetilde{B}}_{p} \) sont égales à leur série de Fourier.

> We deduce the result because we saw above that the functions \( {\widetilde{B}}_{p} \) are equal to their Fourier series.

b) En faisant \( x = 0 \) dans la première relation établie à la question précédente, on a

> b) By setting \( x = 0 \) in the first relation established in the previous question, we have

\[
\forall k \in  {\mathbb{N}}^{ * },\;\frac{{b}_{2k}}{\left( {2k}\right) !} = 2 \cdot  {\left( -1\right) }^{k + 1}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{\left( 2n\pi \right) }^{2k}}\;\text{ donc }\;\zeta \left( {2k}\right)  = \frac{{\left( -1\right) }^{k + 1}{b}_{2k}}{2\left( {2k}\right) !}{\left( 2\pi \right) }^{2k}.
\]

\( \left( {* * }\right) \)

> En particulier, on trouve \( \zeta \left( 2\right) = {\pi }^{2}/6,\zeta \left( 4\right) = {\pi }^{4}/{90},\zeta \left( 6\right) = {\pi }^{6}/{945} \) .

In particular, we find \( \zeta \left( 2\right) = {\pi }^{2}/6,\zeta \left( 4\right) = {\pi }^{4}/{90},\zeta \left( 6\right) = {\pi }^{6}/{945} \) .

> c) pour tout \( k \in {\mathbb{N}}^{ * } \) , on a

c) for all \( k \in {\mathbb{N}}^{ * } \) , we have

\[
\forall n \geq  2,\;\frac{1}{{n}^{2k}} \leq  {\int }_{n - 1}^{n}\frac{dt}{{t}^{2k}}\;\text{ donc }\;\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}\frac{1}{{n}^{2k}} \leq  {\int }_{1}^{+\infty }\frac{dt}{{t}^{2k}} = \frac{1}{{2k} - 1}.
\]

On en déduit \( 1 \leq \zeta \left( {2k}\right) \leq 1 + 1/\left( {{2k} - 1}\right) \) , donc \( \zeta \left( {2k}\right) \rightarrow 1 \) lorsque \( k \rightarrow + \infty \) . Grâce à la relation (**), on en déduit

> We deduce \( 1 \leq \zeta \left( {2k}\right) \leq 1 + 1/\left( {{2k} - 1}\right) \) , therefore \( \zeta \left( {2k}\right) \rightarrow 1 \) when \( k \rightarrow + \infty \) . Thanks to relation (**), we deduce

\[
{b}_{2k} \sim  {\left( -1\right) }^{k + 1}\frac{2\left( {2k}\right) !}{{\left( 2\pi \right) }^{2k}}\;\left( { \sim  {\left( -1\right) }^{k + 1}\frac{4\sqrt{\pi }{k}^{{2k} + 1/2}}{{\left( e\pi \right) }^{2k}}\;\text{ en utilisant la formule de Stirling }}\right) .
\]

Remarque. On ne connaît presque rien sur la somme de la série \( \sum 1/{n}^{p} \) lorsque \( p \) est impair (le seul résultat connu à ce jour sur le sujet est que \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{3} \) est irrationnel - démontré par Apéry en 1978).

> Remark. Almost nothing is known about the sum of the series \( \sum 1/{n}^{p} \) when \( p \) is odd (the only result known to date on the subject is that \( \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{3} \) is irrational - proven by Apéry in 1978).

- Les nombres de Bernoulli jouent un rôle important et assez mystérieux dans des parties aussi diverses des mathématiques que l'analyse, la théorie des nombres et la topologie différentielle. Citons par exemple l’étonnant théorème de Von Staudt : si pour tout \( n \in \; {\mathbb{N}}^{ * },{s}_{n} \) désigne la somme des inverses des nombres premiers \( p \) tels que \( p - 1 \) divise \( {2n} \) , alors \( {s}_{n} + {b}_{2n} \) est un entier. Le sujet d’étude qui suit propose également une intéressante application des nombres et des polynômes de Bernoulli.

> - Bernoulli numbers play an important and rather mysterious role in areas of mathematics as diverse as analysis, number theory, and differential topology. Let us cite, for example, the astonishing Von Staudt theorem: if for all \( n \in \; {\mathbb{N}}^{ * },{s}_{n} \) denotes the sum of the inverses of the prime numbers \( p \) such that \( p - 1 \) divides \( {2n} \) , then \( {s}_{n} + {b}_{2n} \) is an integer. The study topic that follows also proposes an interesting application of Bernoulli numbers and polynomials.

SUJET D'ÉTUDE 3 (FORMULE D'EULER-MACLAURIN). Ce sujet d'étude fait suite au précédent, dont on reprend les notations.

> STUDY TOPIC 3 (EULER-MACLAURIN FORMULA). This study topic follows the previous one, whose notation is used here.

a) Soient \( \left( {m, n}\right) \in {\mathbb{Z}}^{2}, m < n, r \in {\mathbb{N}}^{ * } \) , et \( f : \left\lbrack {m, n}\right\rbrack \rightarrow \mathbb{C} \) de classe \( {\mathcal{C}}^{r} \) . Montrer

> a) Let \( \left( {m, n}\right) \in {\mathbb{Z}}^{2}, m < n, r \in {\mathbb{N}}^{ * } \) and \( f : \left\lbrack {m, n}\right\rbrack \rightarrow \mathbb{C} \) be of class \( {\mathcal{C}}^{r} \) . Show

\[
f\left( m\right)  + f\left( {m + 1}\right)  + \cdots  + f\left( n\right)  = {\int }_{m}^{n}f\left( t\right) {dt} + \frac{1}{2}\left\lbrack  {f\left( m\right)  + f\left( n\right) }\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{h = 2}}^{r}\frac{{b}_{h}}{h!}\left\lbrack  {{f}^{\left( h - 1\right) }\left( n\right)  - {f}^{\left( h - 1\right) }\left( m\right) }\right\rbrack   + {R}_{r}\;\text{ avec }\;{R}_{r} = \frac{{\left( -1\right) }^{r + 1}}{r!}{\int }_{m}^{n}{\widetilde{B}}_{r}\left( t\right) {f}^{\left( r\right) }\left( t\right) {dt}.
\]

b) (Application.) Donner, lorsque \( n \rightarrow + \infty \) , un développement asymptotique à un nombre fixé quelconque de termes de \( {H}_{n} = 1 + \frac{1}{2} + \cdots + \frac{1}{n} \) .

> b) (Application.) Provide, when \( n \rightarrow + \infty \) , an asymptotic expansion to any fixed number of terms of \( {H}_{n} = 1 + \frac{1}{2} + \cdots + \frac{1}{n} \) .

Solution. a) On va procéder par récurrence sur \( r \in {\mathbb{N}}^{ * } \) . Pour \( r = 1 \) , compte tenu du fait que \( {B}_{1}\left( x\right) = x - 1/2 \) sur \( \rbrack 0,1\lbrack \) , une intégration par parties donne pour tout entier \( k, m \leq k \leq n - 1 \) ,

> Solution. a) We will proceed by induction on \( r \in {\mathbb{N}}^{ * } \) . For \( r = 1 \) , given the fact that \( {B}_{1}\left( x\right) = x - 1/2 \) on \( \rbrack 0,1\lbrack \) , integration by parts gives for any integer \( k, m \leq k \leq n - 1 \) ,

\[
{\int }_{k}^{k + 1}{\widetilde{B}}_{1}\left( t\right) {f}^{\prime }\left( t\right) {dt} = {\left\lbrack  {\widetilde{B}}_{1}\left( t\right) f\left( t\right) \right\rbrack  }_{k}^{k + 1} - {\int }_{k}^{k + 1}f\left( t\right) {dt} = \frac{f\left( {k + 1}\right)  + f\left( k\right) }{2} - {\int }_{k}^{k + 1}f\left( t\right) {dt},
\]

puis en sommant cette relation pour \( k \) allant de \( m \) à \( n - 1 \) , on obtient

> then by summing this relation for \( k \) ranging from \( m \) to \( n - 1 \) , we obtain

\[
{\int }_{m}^{n}{\widetilde{B}}_{1}\left( t\right) {f}^{\prime }\left( t\right) {dt} = f\left( m\right)  + f\left( {m + 1}\right)  + \cdots  + f\left( n\right)  - \frac{f\left( m\right)  + f\left( n\right) }{2} - {\int }_{m}^{n}f\left( t\right) {dt},
\]

d’où le résultat pour \( r = 1 \) .

> whence the result for \( r = 1 \) .

Supposons le résultat vrai au rang \( r - 1 \in {\mathbb{N}}^{ * } \) et montrons le au rang \( r \) . Soit \( k \in \mathbb{Z} \) , \( m \leq k \leq n - 1 \) . Sur \( \rbrack k, k + 1\left\lbrack \right. \) , on a \( {\widetilde{B}}_{r}^{\prime } = r{\widetilde{B}}_{r - 1} \) ; par ailleurs, pour \( r \geq 2 \) , on a \( {B}_{r}\left( 0\right) = {B}_{r}\left( 1\right) = {b}_{r} \) , donc par définition de \( {\widetilde{B}}_{r},{\widetilde{B}}_{r} \) est continue sur \( \left\lbrack {k, k + 1}\right\rbrack \) . En intégrant par parties, on obtient

> Assume the result is true at rank \( r - 1 \in {\mathbb{N}}^{ * } \) and show it at rank \( r \) . Let \( k \in \mathbb{Z} \) , \( m \leq k \leq n - 1 \) . On \( \rbrack k, k + 1\left\lbrack \right. \) , we have \( {\widetilde{B}}_{r}^{\prime } = r{\widetilde{B}}_{r - 1} \) ; furthermore, for \( r \geq 2 \) , we have \( {B}_{r}\left( 0\right) = {B}_{r}\left( 1\right) = {b}_{r} \) , so by definition of \( {\widetilde{B}}_{r},{\widetilde{B}}_{r} \) is continuous on \( \left\lbrack {k, k + 1}\right\rbrack \) . By integrating by parts, we obtain

\[
\frac{1}{\left( {r - 1}\right) !}{\int }_{k}^{k + 1}{\widetilde{B}}_{r - 1}\left( t\right) {f}^{\left( r - 1\right) }\left( t\right) {dt} = \frac{1}{r!}{\left\lbrack  {\widetilde{B}}_{r}\left( t\right) {f}^{\left( r - 1\right) }\left( t\right) \right\rbrack  }_{k}^{k + 1} - \frac{1}{r!}{\int }_{k}^{k + 1}{\widetilde{B}}_{r}\left( t\right) {f}^{\left( r\right) }\left( t\right) {dt}
\]

\[
= \frac{{b}_{r}}{r!}\left\lbrack  {{f}^{\left( r - 1\right) }\left( {k + 1}\right)  - {f}^{\left( r - 1\right) }\left( k\right) }\right\rbrack   - \frac{1}{r!}{\int }_{k}^{k + 1}{\widetilde{B}}_{r}\left( t\right) {f}^{\left( r\right) }\left( t\right) {dt},
\]

donc après sommation de ces relations pour \( k \) allant de \( m \) à \( n - 1 \) , puis multiplication par \( {\left( -1\right) }^{r} \) ,

> thus after summing these relations for \( k \) ranging from \( m \) to \( n - 1 \) , then multiplying by \( {\left( -1\right) }^{r} \) ,

\[
{R}_{r - 1} = \frac{{\left( -1\right) }^{r}{b}_{r}}{r!}\left\lbrack  {{f}^{\left( r - 1\right) }\left( n\right)  - {f}^{\left( r - 1\right) }\left( m\right) }\right\rbrack   + {R}_{r}.
\]

On a toujours \( {\left( -1\right) }^{r}{b}_{r} = {b}_{r} \) (si \( r \geq 2 \) est impair on a \( {b}_{r} = 0 \) ). On en déduit le résultat au rang \( r \) . b) Soit \( r \in {\mathbb{N}}^{ * } \) . On applique la formule précédente à la fonction \( f\left( t\right) = 1/t \) entre 1 et \( n \) . Comme \( {f}^{\left( h\right) }\left( t\right) = {\left( -1\right) }^{h}h!/{t}^{h + 1} \) , on a

> We always have \( {\left( -1\right) }^{r}{b}_{r} = {b}_{r} \) (if \( r \geq 2 \) is odd we have \( {b}_{r} = 0 \) ). We deduce the result at rank \( r \) . b) Let \( r \in {\mathbb{N}}^{ * } \) . We apply the previous formula to the function \( f\left( t\right) = 1/t \) between 1 and \( n \) . Since \( {f}^{\left( h\right) }\left( t\right) = {\left( -1\right) }^{h}h!/{t}^{h + 1} \) , we have

\[
{H}_{n} = {\int }_{1}^{n}\frac{dt}{t} + \frac{1}{2}\left( {1 + \frac{1}{n}}\right)  + \mathop{\sum }\limits_{{h = 2}}^{r}\frac{{b}_{h}}{h}\left\lbrack  {\frac{{\left( -1\right) }^{h - 1}}{{n}^{h}} - {\left( -1\right) }^{h - 1}}\right\rbrack   + \frac{{\left( -1\right) }^{r + 1}}{r!}{\int }_{1}^{n}{\widetilde{B}}_{r}\left( t\right) \frac{{\left( -1\right) }^{r}r!}{{t}^{r + 1}}{dt}
\]

\[
= \log n + \underset{ = {\gamma }_{r}}{\underbrace{\left\lbrack  \frac{1}{2} + \mathop{\sum }\limits_{{h = 2}}^{r}\frac{{\left( -1\right) }^{h}{b}_{h}}{h} - {\int }_{1}^{+\infty }{\widetilde{B}}_{r}\left( t\right) \frac{dt}{{t}^{r + 1}}\right\rbrack  }} + \frac{1}{2n} + \mathop{\sum }\limits_{{h = 2}}^{r}{\left( -1\right) }^{h - 1}\frac{{b}_{h}}{h}\frac{1}{{n}^{h}} + {\varepsilon }_{r}\left( n\right)
\]

avec

> with

\[
{\varepsilon }_{r}\left( n\right)  = {\int }_{n}^{+\infty }{\widetilde{B}}_{r}\left( t\right) \frac{dt}{{t}^{r + 1}}\;\text{ qui vérifie }\;\left| {{\varepsilon }_{r}\left( n\right) }\right|  \leq  M{\int }_{n}^{+\infty }\frac{dt}{{t}^{r + 1}} = \frac{M}{r{n}^{r}} = O\left( \frac{1}{{n}^{r}}\right)
\]

(où \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {{B}_{r}\left( t\right) }\right| = \mathop{\sup }\limits_{{x \in \mathbb{R}}}\left| {{\widetilde{B}}_{r}\left( t\right) }\right| \) ). On a donc

> (where \( M = \mathop{\sup }\limits_{{x \in \left\lbrack {0,1}\right\rbrack }}\left| {{B}_{r}\left( t\right) }\right| = \mathop{\sup }\limits_{{x \in \mathbb{R}}}\left| {{\widetilde{B}}_{r}\left( t\right) }\right| \) ). We therefore have

\[
{H}_{n} = \log n + {\gamma }_{r} + \frac{1}{2n} + \mathop{\sum }\limits_{{h = 2}}^{{r - 1}}\frac{{\left( -1\right) }^{h - 1}{b}_{h}}{h}\frac{1}{{n}^{h}} + O\left( \frac{1}{{n}^{r}}\right) ,
\]

et la constante \( {\gamma }_{r} \) est indépendante de \( r \) car la formule précédente donne

> and the constant \( {\gamma }_{r} \) is independent of \( r \) because the previous formula gives

\[
{\gamma }_{r} = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{H}_{n} - \log n = \gamma .
\]
