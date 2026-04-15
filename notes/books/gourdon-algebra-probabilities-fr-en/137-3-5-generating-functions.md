#### 3.5. Generating functions

*Français : 3.5. Fonctions génératrices*

##### Generating series.

*Français : Séries génératrices.*

DÉFINITION 12. Soit \( X : \Omega \rightarrow \mathbb{N} \) une variable aléatoire. On appelle série génératrice de \( X \) la série entière notée \( {G}_{X}\left( z\right) \) et définie par \( {G}_{X}\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {X = n}\right) {z}^{n} \) , de rayon de convergence \( \geq 1 \) .

> DEFINITION 12. Let \( X : \Omega \rightarrow \mathbb{N} \) be a random variable. The generating series of \( X \) is the power series denoted by \( {G}_{X}\left( z\right) \) and defined by \( {G}_{X}\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {X = n}\right) {z}^{n} \) , with radius of convergence \( \geq 1 \) .

Proposition 18. Soit \( X : \Omega \rightarrow \mathbb{N} \) une variable aléatoire. La série génératrice de \( X \) converge normalement pour \( \left| z\right| \leq 1 \) , elle vérifie les propriétés suivantes :

> Proposition 18. Let \( X : \Omega \rightarrow \mathbb{N} \) be a random variable. The generating series of \( X \) converges normally for \( \left| z\right| \leq 1 \) , and satisfies the following properties:

(i) \( z \mapsto {G}_{X}\left( z\right) \) est définie et continue sur \( \left| z\right| \leq 1 \) , en particulier sur \( \left\lbrack {0,1}\right\rbrack \) .

> (i) \( z \mapsto {G}_{X}\left( z\right) \) is defined and continuous on \( \left| z\right| \leq 1 \) , in particular on \( \left\lbrack {0,1}\right\rbrack \) .

(ii) Lorsque \( t \in \left\lbrack {0,1}\right\rbrack \) , on a \( {G}_{X}\left( t\right) = E\left( {t}^{X}\right) \) . On a \( {G}_{X}\left( 1\right) = 1 \) .

> (ii) When \( t \in \left\lbrack {0,1}\right\rbrack \) , we have \( {G}_{X}\left( t\right) = E\left( {t}^{X}\right) \) . We have \( {G}_{X}\left( 1\right) = 1 \) .

(iii) \( X \) admet une espérance si et seulement si \( {G}_{X} \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) , et dans ce cas \( E\left( X\right) = {G}_{X}^{\prime }\left( 1\right) \) .

> (iii) \( X \) has an expectation if and only if \( {G}_{X} \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) , and in this case \( E\left( X\right) = {G}_{X}^{\prime }\left( 1\right) \) .

(iv) \( X \) admet une variance si et seulement si \( {G}_{X} \) est de classe \( {\mathcal{C}}^{2} \) sur \( \left\lbrack {0,1}\right\rbrack \) , et dans ce cas \( V\left( X\right) = {G}_{X}^{\prime \prime }\left( 1\right) + {G}_{X}^{\prime }\left( 1\right) - {G}_{X}^{\prime }{\left( 1\right) }^{2} \) .

> (iv) \( X \) has a variance if and only if \( {G}_{X} \) is of class \( {\mathcal{C}}^{2} \) on \( \left\lbrack {0,1}\right\rbrack \) , and in this case \( V\left( X\right) = {G}_{X}^{\prime \prime }\left( 1\right) + {G}_{X}^{\prime }\left( 1\right) - {G}_{X}^{\prime }{\left( 1\right) }^{2} \) .

(v) Soit \( Y : \Omega \rightarrow \mathbb{N} \) une variable aléatoire. Alors \( {G}_{X} = {G}_{Y} \) sur \( \left\lbrack {0,1}\right\rbrack \) si et seulement si \( X \) et \( Y \) ont même loi.

> (v) Let \( Y : \Omega \rightarrow \mathbb{N} \) be a random variable. Then \( {G}_{X} = {G}_{Y} \) on \( \left\lbrack {0,1}\right\rbrack \) if and only if \( X \) and \( Y \) have the same distribution.

(vi) Soit \( Y : \Omega \rightarrow \mathbb{N} \) une variable aléatoire indépendante de \( X \) . Alors \( {G}_{X + Y} = {G}_{X}{G}_{Y} \) .

> (vi) Let \( Y : \Omega \rightarrow \mathbb{N} \) be a random variable independent of \( X \) . Then \( {G}_{X + Y} = {G}_{X}{G}_{Y} \) .

Démonstration. (i) Pour \( \left| z\right| \leq 1 \) , on a \( \left| {P\left( {X = n}\right) {z}^{n}}\right| \leq P\left( {X = n}\right) \) donc la série converge normalement sur \( \left| z\right| \leq 1 \) , elle est donc définie et continue sur le disque fermé \( \left| z\right| \leq 1 \) .

> Proof. (i) For \( \left| z\right| \leq 1 \) , we have \( \left| {P\left( {X = n}\right) {z}^{n}}\right| \leq P\left( {X = n}\right) \) so the series converges normally on \( \left| z\right| \leq 1 \) , it is therefore defined and continuous on the closed disk \( \left| z\right| \leq 1 \) .

(ii) Lorsque \( t \in \left\lbrack {0,1}\right\rbrack \) , l’égalité \( E\left( {t}^{X}\right) = {G}_{X}\left( t\right) \) est une conséquence du théorème de transfert (voir la proposition 6 page 338). L’égalité \( {G}_{X}\left( 1\right) = 1 \) est immédiate.

> (ii) When \( t \in \left\lbrack {0,1}\right\rbrack \) , the equality \( E\left( {t}^{X}\right) = {G}_{X}\left( t\right) \) is a consequence of the transfer theorem (see proposition 6 page 338). The equality \( {G}_{X}\left( 1\right) = 1 \) is immediate.

(iii) Notons \( {p}_{n} = P\left( {X = n}\right) \) . Si \( X \) admet une espérance, alors \( \sum n{p}_{n} \) converge donc la série des termes dérivés \( \sum n{p}_{n}{t}^{n - 1} \) converge normalement sur \( t \in \left\lbrack {0,1}\right\rbrack \) , donc est bien \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) , et de plus \( {G}_{X}^{\prime }\left( t\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{p}_{n}{t}^{n - 1} \) sur \( \left\lbrack {0,1}\right\rbrack \) , en particulier pour \( t = 1 \) ce qui donne \( {G}_{X}^{\prime }\left( 1\right) = E\left( X\right) \) . Réciproquement supposons \( {G}_{X} \) de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) . La série des termes dérivés \( \sum n{p}_{n}{t}^{n - 1} \) converge normalement sur tout segment inclus dans \( \lbrack 0,1\lbrack \) , donc pour tout \( t \in \lbrack 0,1\lbrack \) on a \( {G}_{X}^{\prime }\left( t\right) = \; \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{p}_{n}{t}^{n - 1} \) . Ainsi \( {G}_{X}^{\prime } \) est croissante sur \( \lbrack 0,1\lbrack \) , et comme \( {G}_{X}^{\prime } \) est continue en 1 on en déduit

> (iii) Let \( {p}_{n} = P\left( {X = n}\right) \) . If \( X \) has an expectation, then \( \sum n{p}_{n} \) converges, so the series of derived terms \( \sum n{p}_{n}{t}^{n - 1} \) converges normally on \( t \in \left\lbrack {0,1}\right\rbrack \) , and is therefore \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) , and furthermore \( {G}_{X}^{\prime }\left( t\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{p}_{n}{t}^{n - 1} \) on \( \left\lbrack {0,1}\right\rbrack \) , in particular for \( t = 1 \) which gives \( {G}_{X}^{\prime }\left( 1\right) = E\left( X\right) \) . Conversely, suppose \( {G}_{X} \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) . The series of derived terms \( \sum n{p}_{n}{t}^{n - 1} \) converges normally on any segment included in \( \lbrack 0,1\lbrack \) , so for all \( t \in \lbrack 0,1\lbrack \) we have \( {G}_{X}^{\prime }\left( t\right) = \; \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{p}_{n}{t}^{n - 1} \) . Thus \( {G}_{X}^{\prime } \) is increasing on \( \lbrack 0,1\lbrack \) , and since \( {G}_{X}^{\prime } \) is continuous at 1, we deduce

\[
\forall N \in  {\mathbb{N}}^{ * },\;\mathop{\sum }\limits_{{n = 1}}^{N}n{p}_{n} = \mathop{\lim }\limits_{{t \rightarrow  {1}^{ - }}}\mathop{\sum }\limits_{{n = 1}}^{N}n{p}_{n}{t}^{n - 1} \leq  \mathop{\lim }\limits_{{t \rightarrow  {1}^{ - }}}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{p}_{n}{t}^{n - 1} = {G}_{X}^{\prime }\left( 1\right) .
\]

Donc la série à termes positifs \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}n{p}_{n} \) est majorée, donc elle converge.

> Therefore, the series with positive terms \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}n{p}_{n} \) is bounded, so it converges.

(iv) Le même raisonnement que pour (iii) montre que \( {G}_{X} \) est \( {\mathcal{C}}^{2} \) sur \( \left\lbrack {0,1}\right\rbrack \) si et seulement si \( \sum n\left( {n - 1}\right) {p}_{n} \) converge, et comme \( n\left( {n - 1}\right) {p}_{n} = {n}^{2}{p}_{n}\left( {1 + o\left( 1\right) }\right) \) ceci équivaut à dire que \( X \) admet une variance. On obtient facilement \( E\left( {X}^{2}\right) = \mathop{\sum }\limits_{{n > 1}}{n}^{2}{p}_{n} = \mathop{\sum }\limits_{{n > 1}}n\left( {n - 1}\right) {p}_{n} + \mathop{\sum }\limits_{{n > 1}}n{p}_{n} = \; {G}_{X}^{\prime \prime }\left( 1\right) + {G}_{X}^{\prime }\left( 1\right) \) , et on conclut avec la formule de Koénig-Huygens \( V\left( X\right) = E\left( {X}^{2}\right) - E{\left( X\right) }^{2} \) .

> (iv) The same reasoning as for (iii) shows that \( {G}_{X} \) is \( {\mathcal{C}}^{2} \) on \( \left\lbrack {0,1}\right\rbrack \) if and only if \( \sum n\left( {n - 1}\right) {p}_{n} \) converges, and since \( n\left( {n - 1}\right) {p}_{n} = {n}^{2}{p}_{n}\left( {1 + o\left( 1\right) }\right) \) this is equivalent to saying that \( X \) has a variance. We easily obtain \( E\left( {X}^{2}\right) = \mathop{\sum }\limits_{{n > 1}}{n}^{2}{p}_{n} = \mathop{\sum }\limits_{{n > 1}}n\left( {n - 1}\right) {p}_{n} + \mathop{\sum }\limits_{{n > 1}}n{p}_{n} = \; {G}_{X}^{\prime \prime }\left( 1\right) + {G}_{X}^{\prime }\left( 1\right) \) , and we conclude with the König-Huygens formula \( V\left( X\right) = E\left( {X}^{2}\right) - E{\left( X\right) }^{2} \) .

(v) est une conséquence du principe des zéros isolés, qui entraîne que les coefficients de \( {G}_{X} \) et \( {G}_{Y} \) sont identiques.

> (v) is a consequence of the principle of isolated zeros, which implies that the coefficients of \( {G}_{X} \) and \( {G}_{Y} \) are identical.

(vi) Si \( X \) et \( Y \) sont indépendants, alors \( {t}^{X} \) et \( {t}^{Y} \) aussi, donc \( {G}_{X}\left( t\right) {G}_{Y}\left( t\right) = E\left( {t}^{X}\right) E\left( {t}^{Y}\right) = \; E\left( {t}^{X + Y}\right) = {G}_{X + Y}\left( t\right) . \)

> (vi) If \( X \) and \( Y \) are independent, then \( {t}^{X} \) and \( {t}^{Y} \) are as well, so \( {G}_{X}\left( t\right) {G}_{Y}\left( t\right) = E\left( {t}^{X}\right) E\left( {t}^{Y}\right) = \; E\left( {t}^{X + Y}\right) = {G}_{X + Y}\left( t\right) . \)

SÉRIES GÉNÉRATRICES DES LOIS USUELLES. Les séries génératrices fournissent un moyen commode de calculer l'espérance et la variance d'une variable aléatoire à partir de leur forme close. Les séries génératrices des lois usuelles d'une variable aléatoire \( X \) sont les suivantes :

> GENERATING FUNCTIONS OF COMMON DISTRIBUTIONS. Generating functions provide a convenient way to calculate the expectation and variance of a random variable from their closed form. The generating functions of the common distributions of a random variable \( X \) are as follows:

- Loi de Bernoulli de paramètre \( p : {G}_{X}\left( t\right)  = 1 - p + {pt} \) .

> - Bernoulli distribution with parameter \( p : {G}_{X}\left( t\right)  = 1 - p + {pt} \) .

- Loi binomiale de paramètre \( \left( {n, p}\right)  : {G}_{X}\left( t\right)  = {\left( 1 - p + pt\right) }^{n} \) . Ce résultat est aussi une conséquence de de la propriété (vi) ci dessus, appliquée à une somme de \( n \) variables aléa-toires indépendantes suivant chacune une loi de Bernoulli de paramètre \( p \) . Cette formule permet de calculer \( E\left( X\right) \) et \( V\left( X\right) \) par les formules

> - Binomial distribution with parameter \( \left( {n, p}\right)  : {G}_{X}\left( t\right)  = {\left( 1 - p + pt\right) }^{n} \) . This result is also a consequence of property (vi) above, applied to a sum of \( n \) independent random variables each following a Bernoulli distribution with parameter \( p \) . This formula allows for the calculation of \( E\left( X\right) \) and \( V\left( X\right) \) using the formulas

\[
E\left( X\right)  = {G}_{X}^{\prime }\left( 1\right)  = {np}
\]

\[
V\left( X\right)  = {G}_{X}^{\prime \prime }\left( 1\right)  + {G}_{X}^{\prime }\left( 1\right)  - {G}_{X}^{\prime }{\left( 1\right) }^{2} = n\left( {n - 1}\right) {p}^{2} + {np} - {\left( np\right) }^{2} = {np}\left( {1 - p}\right) .
\]

Remarquons également que les propriétés (vi) et (v) ci dessus permettent de montrer que si \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) et \( Y \hookrightarrow \mathcal{B}\left( {m, p}\right) \) sont indépendantes, alors \( X + Y \hookrightarrow \mathcal{B}\left( {n + m, p}\right) \) . - Loi géométrique de paramètre \( p \) :

> Note also that properties (vi) and (v) above allow us to show that if \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) and \( Y \hookrightarrow \mathcal{B}\left( {m, p}\right) \) are independent, then \( X + Y \hookrightarrow \mathcal{B}\left( {n + m, p}\right) \) . - Geometric distribution with parameter \( p \) :

\[
{G}_{X}\left( t\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( 1 - p\right) }^{n - 1}p{t}^{n} = \frac{pt}{1 - \left( {1 - p}\right) t} = \frac{p}{1 - p}\left( {-1 + \frac{1}{1 - \left( {1 - p}\right) t}}\right) ,
\]

d'où on déduit

> from which we deduce

\[
E\left( X\right)  = {G}_{X}^{\prime }\left( 1\right)  = \frac{p}{1 - p}\frac{1 - p}{{p}^{2}} = \frac{1}{p}
\]

\[
V\left( X\right)  = {G}_{X}^{\prime \prime }\left( 1\right)  + {G}_{X}^{\prime }\left( 1\right)  - {G}_{X}^{\prime }{\left( 1\right) }^{2} = \frac{{2p}\left( {1 - p}\right) }{{p}^{3}} + \frac{1}{p} - \frac{1}{{p}^{2}} = \frac{1 - p}{{p}^{2}}.
\]

- Loi de Poisson de paramètre \( p : {G}_{X}\left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{e}^{-\lambda }\frac{{\lambda }^{n}}{n!} \cdot  {t}^{n} = {e}^{\lambda \left( {t - 1}\right) } \) , donc

> - Poisson distribution with parameter \( p : {G}_{X}\left( t\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{e}^{-\lambda }\frac{{\lambda }^{n}}{n!} \cdot  {t}^{n} = {e}^{\lambda \left( {t - 1}\right) } \) , so

\[
E\left( X\right)  = {G}_{X}^{\prime }\left( 1\right)  = \lambda
\]

\[
V\left( X\right)  = {G}_{X}^{\prime \prime }\left( 1\right)  + {G}_{X}^{\prime }\left( 1\right)  - {G}_{X}^{\prime }{\left( 1\right) }^{2} = {\lambda }^{2} + \lambda  - {\lambda }^{2} = \lambda .
\]

Nous terminons par un résultat sur les séries génératrices qui n'est pas au programme des classes préparatoires mais qui est facile à retenir et à redémontrer.

> We conclude with a result on generating functions that is not in the preparatory classes curriculum but is easy to remember and re-derive.

Proposition 19 (FORMULE DE WALD). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires et indépendantes de \( \Omega \) sur \( \mathbb{N} \) , identiquement distribuées, et \( N : \Omega \rightarrow {\mathbb{N}}^{ * } \) une variable aléatoire indépendante des \( {X}_{n} \) . On note \( {S}_{N} \) la variable aléatoire définie sur \( \Omega \) par \( {S}_{N}\left( \omega \right) = \; \mathop{\sum }\limits_{{n = 1}}^{{N\left( \omega \right) }}{X}_{n}\left( \omega \right) \) . Alors la série génératrice de \( {S}_{N} \) s’exprime en fonction de celle de \( N \) et \( {X}_{1} \) sous la forme \( {G}_{{S}_{N}} = {G}_{N} \circ {G}_{{X}_{1}} \) . Si \( N \) et les \( {X}_{n} \) admettent une espérance, \( {S}_{N} \) également et on a \( E\left( {S}_{N}\right) = E\left( N\right) E\left( {X}_{1}\right) \) .

> Proposition 19 (WALD'S IDENTITY). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent random variables of \( \Omega \) on \( \mathbb{N} \) , identically distributed, and \( N : \Omega \rightarrow {\mathbb{N}}^{ * } \) a random variable independent of the \( {X}_{n} \) . Let \( {S}_{N} \) be the random variable defined on \( \Omega \) by \( {S}_{N}\left( \omega \right) = \; \mathop{\sum }\limits_{{n = 1}}^{{N\left( \omega \right) }}{X}_{n}\left( \omega \right) \) . Then the generating function of \( {S}_{N} \) is expressed in terms of those of \( N \) and \( {X}_{1} \) in the form \( {G}_{{S}_{N}} = {G}_{N} \circ {G}_{{X}_{1}} \) . If \( N \) and the \( {X}_{n} \) have an expectation, \( {S}_{N} \) does as well and we have \( E\left( {S}_{N}\right) = E\left( N\right) E\left( {X}_{1}\right) \) .

Démonstration. Comme \( N \) et les \( {X}_{n} \) sont indépendants on peut écrire

> Proof. Since \( N \) and the \( {X}_{n} \) are independent, we can write

\[
P\left( {{S}_{N} = n}\right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}P\left( {N = k,{X}_{1} + \cdots  + {X}_{k} = n}\right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}P\left( {N = k}\right) P\left( {{X}_{1} + \cdots  + {X}_{k} = n}\right) .
\]

On peut donc écrire, pour \( \left| z\right| \leq 1 \) ,

> We can therefore write, for \( \left| z\right| \leq 1 \) ,

\[
{G}_{{S}_{N}}\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{S}_{N} = n}\right) {z}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 1}}^{{+\infty }}P\left( {N = k}\right) P\left( {{X}_{1} + \cdots  + {X}_{k} = n}\right) {z}^{n}}\right)
\]

\[
= \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}P\left( {N = k}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{X}_{1} + \cdots  + {X}_{k} = n}\right) {z}^{n}}\right) .
\]

(par définition d'une série génératrice d'une variable aléatoire, les séries en présence sont à termes positifs et sommables, on peut donc bien intervertir les signes de sommation). Remarquons que \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{X}_{1} + \cdots + {X}_{k} = n}\right) {z}^{n} = {G}_{{X}_{1} + \cdots + {X}_{k}}\left( z\right) \) , et que les \( {X}_{k} \) étant indépendants, ceci est égal à \( {G}_{{X}_{1}}\left( z\right) \cdots {G}_{{X}_{k}}\left( z\right) = {G}_{{X}_{1}}{\left( z\right) }^{k} \) . On a donc

> (by definition of a probability generating function of a random variable, the series involved have positive, summable terms, so we may indeed interchange the summation signs). Note that \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{X}_{1} + \cdots + {X}_{k} = n}\right) {z}^{n} = {G}_{{X}_{1} + \cdots + {X}_{k}}\left( z\right) \) , and since the \( {X}_{k} \) are independent, this is equal to \( {G}_{{X}_{1}}\left( z\right) \cdots {G}_{{X}_{k}}\left( z\right) = {G}_{{X}_{1}}{\left( z\right) }^{k} \) . We thus have

\[
{G}_{{S}_{N}}\left( z\right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}P\left( {N = k}\right) {G}_{{X}_{1}}{\left( z\right) }^{k} = {G}_{N}\left( {{G}_{{X}_{1}}\left( z\right) }\right) .
\]

Si \( N \) et \( {X}_{1} \) admettent une espérance, alors \( {G}_{N} \) et \( {G}_{{X}_{1}} \) sont de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) , et comme \( {G}_{{X}_{1}}\left( \left\lbrack {0,1}\right\rbrack \right) \subset \left\lbrack {0,1}\right\rbrack \) , on en déduit que \( {G}_{{S}_{N}} = {G}_{N} \circ {G}_{{X}_{1}} \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) . Donc \( {S}_{N} \) admet une espérance (voir la proposition 18, assertion (iii)), et on a \( E\left( {S}_{N}\right) = {G}_{{S}_{N}}^{\prime }\left( 1\right) = \; {G}_{N}^{\prime }\left( {{G}_{{X}_{1}}\left( 1\right) }\right) {G}_{{X}_{1}}^{\prime }\left( 1\right) = {G}_{N}^{\prime }\left( 1\right) {G}_{{X}_{1}}^{\prime }\left( 1\right) = E\left( N\right) E\left( {X}_{1}\right) . \)

> If \( N \) and \( {X}_{1} \) have an expected value, then \( {G}_{N} \) and \( {G}_{{X}_{1}} \) are of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) , and since \( {G}_{{X}_{1}}\left( \left\lbrack {0,1}\right\rbrack \right) \subset \left\lbrack {0,1}\right\rbrack \) , we deduce that \( {G}_{{S}_{N}} = {G}_{N} \circ {G}_{{X}_{1}} \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) . Therefore, \( {S}_{N} \) has an expected value (see proposition 18, assertion (iii)), and we have \( E\left( {S}_{N}\right) = {G}_{{S}_{N}}^{\prime }\left( 1\right) = \; {G}_{N}^{\prime }\left( {{G}_{{X}_{1}}\left( 1\right) }\right) {G}_{{X}_{1}}^{\prime }\left( 1\right) = {G}_{N}^{\prime }\left( 1\right) {G}_{{X}_{1}}^{\prime }\left( 1\right) = E\left( N\right) E\left( {X}_{1}\right) . \)

Fonctions caractéristiques. Les fonctions caractéristiques ne sont pas au programme des classes préparatoires mais outre le fait qu'elles fournissent un outil très utilisé en probabilité, on tombe parfois sur des exercices qui s'appuie sur ces dernières. Elles sont la transformée de Fourier de la loi d'une variable aléatoire. La notion d'espérance, définie sur les variables aléatoires réelles, se généralise facilement au cas complexe, permettant l’usage de \( E\left( {e}^{iuX}\right) \) .

> Characteristic functions. Characteristic functions are not in the preparatory class curriculum, but besides being a widely used tool in probability, one sometimes encounters exercises that rely on them. They are the Fourier transform of the distribution of a random variable. The notion of expected value, defined for real random variables, generalizes easily to the complex case, allowing the use of \( E\left( {e}^{iuX}\right) \) .

DéFINITION 13 (FONCTION CARACTÉRISTIQUE). Soit \( X \) une variable aléatoire discrète réelle sur \( \Omega \) . On appelle fonction caractéristique de \( X \) la fonction notée \( {\varphi }_{X} \) et définie par

> DEFINITION 13 (CHARACTERISTIC FUNCTION). Let \( X \) be a real discrete random variable on \( \Omega \) . The characteristic function of \( X \) is the function denoted by \( {\varphi }_{X} \) and defined by

\[
{\varphi }_{X} : \mathbb{R} \rightarrow  \mathbb{C}\;u \mapsto  E\left( {e}^{iuX}\right)  = \mathop{\sum }\limits_{{x \in  X\left( \Omega \right) }}P\left( {X = x}\right) {e}^{iux}.
\]

Remarque 17. Un cas courant est celui où \( X \) prend ses valeurs dans \( \mathbb{Z} \) , et dans ce cas \( {\varphi }_{X}\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}P\left( {X = n}\right) {e}^{inu} \) est \( {2\pi } \) -périodique. Lorsque \( X \) prend ses valeurs dans \( \mathbb{N} \) , on a \( {\varphi }_{X}\left( u\right) = {G}_{X}\left( {e}^{iu}\right) \) où \( {G}_{X} \) est la série génératrice de \( X \) .

> Remark 17. A common case is when \( X \) takes its values in \( \mathbb{Z} \), and in this case \( {\varphi }_{X}\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}P\left( {X = n}\right) {e}^{inu} \) is \( {2\pi } \)-periodic. When \( X \) takes its values in \( \mathbb{N} \), we have \( {\varphi }_{X}\left( u\right) = {G}_{X}\left( {e}^{iu}\right) \) where \( {G}_{X} \) is the generating function of \( X \).

Dans la suite on suppose que \( X \) est à valeur dans \( \mathbb{Z} \) , mais les résultats restent vrais pour toute variable aléatoire discrète réelle \( X \) . Comme pour les séries de Fourier, on utilisera la convention suivante pour les séries dont les termes sont indexés sur \( \mathbb{Z} \) : la série \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{a}_{n}{e}^{inu} \) désigne la série \( {a}_{0} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}{e}^{inu} + {a}_{-n}{e}^{-{inu}}}\right) \) (ici nous serons dans le cas où \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {a}_{n}\right| \) est sommable, donc l’ordre des indices n’importe pas, néanmoins cette convention sera une commodité pour nous permettre d'utiliser les théorèmes sur les séries de fonction).

> In the following, we assume that \( X \) takes values in \( \mathbb{Z} \), but the results remain true for any real discrete random variable \( X \). As with Fourier series, we will use the following convention for series whose terms are indexed over \( \mathbb{Z} \): the series \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{a}_{n}{e}^{inu} \) denotes the series \( {a}_{0} + \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{a}_{n}{e}^{inu} + {a}_{-n}{e}^{-{inu}}}\right) \) (here we will be in the case where \( \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {a}_{n}\right| \) is summable, so the order of the indices does not matter; nevertheless, this convention will be a convenience to allow us to use theorems on series of functions).

Proposition 20. La fonction caractéristique \( {\varphi }_{X} \) d’une variable aléatoire discrète \( X \) à valeurs dans \( \mathbb{Z} \) vérifie les propriétés suivantes :

> Proposition 20. The characteristic function \( {\varphi }_{X} \) of a discrete random variable \( X \) taking values in \( \mathbb{Z} \) satisfies the following properties:

(i) \( {\varphi }_{X} \) est définie, continue et \( {2\pi } \) -périodique sur \( \mathbb{R} \) , et vérifie \( \left| {{\varphi }_{X}\left( u\right) }\right| \leq 1 \) sur \( \mathbb{R} \) .

> (i) \( {\varphi }_{X} \) is defined, continuous, and \( {2\pi } \)-periodic on \( \mathbb{R} \), and satisfies \( \left| {{\varphi }_{X}\left( u\right) }\right| \leq 1 \) on \( \mathbb{R} \).

(ii) Si \( X \) admet une espérance, \( {\varphi }_{X} \) est de classe \( {\mathcal{C}}^{1} \) sur \( \mathbb{R} \) et on a \( {\varphi }_{X}^{\prime }\left( 0\right) = {iE}\left( X\right) \) .

> (ii) If \( X \) has an expectation, \( {\varphi }_{X} \) is of class \( {\mathcal{C}}^{1} \) on \( \mathbb{R} \) and we have \( {\varphi }_{X}^{\prime }\left( 0\right) = {iE}\left( X\right) \).

(iii) Si \( X \) admet un moment d’ordre \( p,{\varphi }_{X} \) est de classe \( {\mathcal{C}}^{p} \) et \( {\varphi }_{X}^{\left( p\right) }\left( 0\right) = {i}^{p}E\left( {X}^{p}\right) \) .

> (iii) If \( X \) has a moment of order \( p,{\varphi }_{X} \), it is of class \( {\mathcal{C}}^{p} \) and \( {\varphi }_{X}^{\left( p\right) }\left( 0\right) = {i}^{p}E\left( {X}^{p}\right) \).

(iv) Soit \( Y \) une variable aléatoire sur \( \Omega \) . Alors \( {\varphi }_{X} = {\varphi }_{Y} \) si et seulement si \( X \) et \( Y \) ont même loi.

> (iv) Let \( Y \) be a random variable on \( \Omega \). Then \( {\varphi }_{X} = {\varphi }_{Y} \) if and only if \( X \) and \( Y \) have the same distribution.

(v) Soit \( Y \) une variable aléatoire sur \( \Omega \) indépendante de \( X \) . Alors \( {\varphi }_{X + Y} = {\varphi }_{X}{\varphi }_{Y} \) .

> (v) Let \( Y \) be a random variable on \( \Omega \) independent of \( X \). Then \( {\varphi }_{X + Y} = {\varphi }_{X}{\varphi }_{Y} \).

Démonstration. (i) Pour simplifier nous notons \( {p}_{n} = P\left( {X = n}\right) \) . L’inégalité \( \left| {{p}_{n}{e}^{inu}}\right| \leq {p}_{n} \) entraîne la convergence normale de la série de fonctions \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{p}_{n}{e}^{inu} + {p}_{-n}{e}^{-{inu}}}\right) \) sur \( \mathbb{R} \) , donc \( {\varphi }_{X} \) est bien définie et continue sur \( \mathbb{R} \) . De plus \( \left| {{\varphi }_{X}\left( u\right) }\right| \leq \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{p}_{n}{e}^{inu}}\right| = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{p}_{n} = 1 \) .

> Proof. (i) For simplicity, we denote \( {p}_{n} = P\left( {X = n}\right) \). The inequality \( \left| {{p}_{n}{e}^{inu}}\right| \leq {p}_{n} \) implies the normal convergence of the series of functions \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{p}_{n}{e}^{inu} + {p}_{-n}{e}^{-{inu}}}\right) \) on \( \mathbb{R} \), so \( {\varphi }_{X} \) is well-defined and continuous on \( \mathbb{R} \). Furthermore, \( \left| {{\varphi }_{X}\left( u\right) }\right| \leq \mathop{\sum }\limits_{{n \in \mathbb{Z}}}\left| {{p}_{n}{e}^{inu}}\right| = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{p}_{n} = 1 \).

(ii) Si \( X \) admet une espérance alors \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {n{p}_{n} + n{p}_{-n}}\right) \) converge, donc la série des termes dérivés \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{in}{p}_{n}{e}^{inu} - {in}{p}_{-n}{e}^{-{inu}}}\right) \) converge normalement sur \( \mathbb{R} \) , donc \( {\varphi }_{X} \) est bien de classe \( {\mathcal{C}}^{1} \) sur \( \mathbb{R} \) et \( {\varphi }_{X}^{\prime }\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{in}{p}_{n}{e}^{inu} \) , en particulier \( {\varphi }_{X}^{\prime }\left( 0\right) = {iE}\left( X\right) \) .

> (ii) If \( X \) has an expectation, then \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {n{p}_{n} + n{p}_{-n}}\right) \) converges, so the series of derived terms \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}\left( {{in}{p}_{n}{e}^{inu} - {in}{p}_{-n}{e}^{-{inu}}}\right) \) converges normally on \( \mathbb{R} \), so \( {\varphi }_{X} \) is indeed of class \( {\mathcal{C}}^{1} \) on \( \mathbb{R} \) and \( {\varphi }_{X}^{\prime }\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{in}{p}_{n}{e}^{inu} \), in particular \( {\varphi }_{X}^{\prime }\left( 0\right) = {iE}\left( X\right) \).

(iii) La dérivée \( p \) -ième de \( {p}_{n}{e}^{inu} \) est \( {i}^{p}{n}^{p}{p}_{n}{e}^{inu} \) , donc la série des dérivées \( p \) -ièmes converge normalement, donc \( {\varphi }_{X} \) est de classe \( {\mathcal{C}}^{p} \) et \( {\varphi }_{X}^{\left( p\right) }\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{i}^{p}{n}^{p}{p}_{n}{e}^{inu} \) , d’où le résultat.

> (iii) The \( p \)-th derivative of \( {p}_{n}{e}^{inu} \) is \( {i}^{p}{n}^{p}{p}_{n}{e}^{inu} \), so the series of \( p \)-th derivatives converges normally, so \( {\varphi }_{X} \) is of class \( {\mathcal{C}}^{p} \) and \( {\varphi }_{X}^{\left( p\right) }\left( u\right) = \mathop{\sum }\limits_{{n \in \mathbb{Z}}}{i}^{p}{n}^{p}{p}_{n}{e}^{inu} \), hence the result.

(iv) Si \( X \) et \( Y \) ont même loi il est immédiat que \( {\varphi }_{X} = {\varphi }_{Y} \) . La réciproque est une conséquence du fait qu'une série de Fourier convergeant normalement est égale à sa série de Fourier, donc \( P\left( {X = n}\right) = P\left( {Y = n}\right) \) pour tout \( n \in \mathbb{Z} \) (cette égalité est aussi une conséquence de la formule (*) de la remarque 18 plus bas).

> (iv) If \( X \) and \( Y \) have the same distribution, it is immediate that \( {\varphi }_{X} = {\varphi }_{Y} \). The converse is a consequence of the fact that a normally converging Fourier series is equal to its Fourier series, so \( P\left( {X = n}\right) = P\left( {Y = n}\right) \) for all \( n \in \mathbb{Z} \) (this equality is also a consequence of formula (*) in remark 18 below).

(v) Si \( X \) et \( Y \) sont indépendants, \( {e}^{iuX} \) et \( {e}^{iuY} \) également donc \( {\varphi }_{X}\left( u\right) {\varphi }_{Y}\left( u\right) = E\left( {e}^{iuX}\right) E\left( {e}^{iuY}\right) = \; E\left( {e}^{{iu}\left( {X + Y}\right) }\right) = {\varphi }_{X + Y}\left( u\right) . \)

> (v) If \( X \) and \( Y \) are independent, \( {e}^{iuX} \) and \( {e}^{iuY} \) are as well, therefore \( {\varphi }_{X}\left( u\right) {\varphi }_{Y}\left( u\right) = E\left( {e}^{iuX}\right) E\left( {e}^{iuY}\right) = \; E\left( {e}^{{iu}\left( {X + Y}\right) }\right) = {\varphi }_{X + Y}\left( u\right) . \)

\( \rightarrow \) Remarque 18. Pour toute variable aléatoire \( X \) à valeurs dans \( \mathbb{Z} \) on a l’égalité

> \( \rightarrow \) Remark 18. For any random variable \( X \) taking values in \( \mathbb{Z} \), we have the equality

\[
\forall n \in  \mathbb{Z},\;P\left( {X = n}\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{e}^{-{int}}{\varphi }_{X}\left( {e}^{it}\right) {dt}.
\]

(*)

> Cette identité est très utile, elle permet de connaître la loi de \( X \) à partir de \( {\varphi }_{X} \) . En parti-culier, elle entraîne le résultat suivant : si \( \left( {X}_{n}\right) \) est une suite de variables aléatoires sur \( \Omega \) à valeurs dans \( \mathbb{Z} \) , et \( X : \Omega \rightarrow \mathbb{Z} \) une variable aléatoire, telle que \( \left( {\varphi }_{{X}_{n}}\right) \) converge simplement vers \( {\varphi }_{X} \) sur \( \mathbb{R} \) , alors pour tout \( p \in \mathbb{Z} \) , on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{n} = p}\right) = P\left( {X = p}\right) \) (on dit alors que \( \left( {X}_{n}\right) \) converge en loi vers \( X \) ). Cette propriété est une conséquence du théorème de convergence dominée appliqué à l'intégrale de (*). Dans sa forme plus générale, ce ré- sultat est appelé théorème de convergence de Lévy, il permet notamment de démontrer le théorème central limite (qui n'est pas au programme des classes préparatoires, une preuve est néanmoins proposée dans le cas des variables aléatoires entières dans le problème 9 page 386) par critère de convergence simple des fonctions caractéristiques.

This identity is very useful; it allows one to determine the distribution of \( X \) from \( {\varphi }_{X} \). In particular, it leads to the following result: if \( \left( {X}_{n}\right) \) is a sequence of random variables on \( \Omega \) taking values in \( \mathbb{Z} \), and \( X : \Omega \rightarrow \mathbb{Z} \) is a random variable such that \( \left( {\varphi }_{{X}_{n}}\right) \) converges pointwise to \( {\varphi }_{X} \) on \( \mathbb{R} \), then for all \( p \in \mathbb{Z} \), we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{n} = p}\right) = P\left( {X = p}\right) \) (we then say that \( \left( {X}_{n}\right) \) converges in distribution to \( X \)). This property is a consequence of the dominated convergence theorem applied to the integral of (*). In its more general form, this result is called Lévy's continuity theorem; it allows, in particular, the proof of the central limit theorem (which is not in the preparatory classes curriculum, though a proof is provided for integer-valued random variables in problem 9 on page 386) via the criterion of pointwise convergence of characteristic functions.
