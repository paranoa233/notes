#### 3.3. Common discrete distributions

*Français : 3.3. Lois discrètes usuelles*

Dans cette partie, \( X \) désigne une variable aléatoire discrète réelle sur \( \Omega \) .

> In this section, \( X \) denotes a real discrete random variable on \( \Omega \) .

Loi uniforme. On dit que \( X \) suit une loi uniforme lorsque \( X\left( \Omega \right) \) est fini, de cardinal \( n \in {\mathbb{N}}^{ * } \) , et lorsque pour tout \( x \in X\left( \Omega \right) \) on a \( P\left( {X = x}\right) = 1/n \) . Cette loi correspond à la probabilité de tirer une boule donnée dans une urne de \( n \) boules différenciées, lors d'un tirage équiprobable.

> Uniform distribution. We say that \( X \) follows a uniform distribution when \( X\left( \Omega \right) \) is finite, with cardinality \( n \in {\mathbb{N}}^{ * } \) , and when for all \( x \in X\left( \Omega \right) \) we have \( P\left( {X = x}\right) = 1/n \) . This distribution corresponds to the probability of drawing a specific ball from an urn of \( n \) distinct balls, in an equiprobable draw.

Loi de Bernoulli. Soit \( p \in \rbrack 0,1\lbrack \) . On dit que \( X \) suit une loi de Bernoulli de paramètre \( p \) ,(et on note \( X \hookrightarrow \mathcal{B}\left( p\right) \) ), si

> Bernoulli distribution. Let \( p \in \rbrack 0,1\lbrack \) . We say that \( X \) follows a Bernoulli distribution with parameter \( p \) , (denoted \( X \hookrightarrow \mathcal{B}\left( p\right) \) ), if

\[
X\left( \Omega \right)  = \{ 0,1\} \;\text{ et }\;P\left( {X = 0}\right)  = 1 - p,\;P\left( {X = 1}\right)  = p.
\]

On a \( E\left( X\right) = p \) et \( V\left( X\right) = p\left( {1 - p}\right) \) .

> We have \( E\left( X\right) = p \) and \( V\left( X\right) = p\left( {1 - p}\right) \) .

Il s'agit de la loi qui modélise un tirage à pile ou face avec une pièce déséquilibrée, associé à la valeur aléatoire \( X \) définie par \( X = 1 \) si on tombe sur pile (succés), \( X = 0 \) si on tombe sur face (une telle expérience s'appelle expérience de Bernoulli).

> This is the distribution that models a coin toss with a biased coin, associated with the random variable \( X \) defined by \( X = 1 \) if the result is heads (success), \( X = 0 \) if the result is tails (such an experiment is called a Bernoulli trial).

Remarque 12. Une loi qui ressemble à celle de Bernoulli dans le cas \( p = 1/2 \) est la loi de Rademacher. La variable \( X \) suit une loi de Rademacher si \( X\left( \Omega \right) = \{ - 1,1\} \) et si \( P\left( {X = - 1}\right) = P\left( {X = 1}\right) = 1/2. \)

> Remark 12. A distribution similar to the Bernoulli distribution in the case \( p = 1/2 \) is the Rademacher distribution. The variable \( X \) follows a Rademacher distribution if \( X\left( \Omega \right) = \{ - 1,1\} \) and if \( P\left( {X = - 1}\right) = P\left( {X = 1}\right) = 1/2. \)

Loi binomiale. Soit \( p \in \rbrack 0,1\left\lbrack \right. \) et \( n \in {\mathbb{N}}^{ * } \) . On dit que \( X \) suit une loi binomiale de paramètre \( \left( {n, p}\right) \) (et on note \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) ) si

> Binomial distribution. Let \( p \in \rbrack 0,1\left\lbrack \right. \) and \( n \in {\mathbb{N}}^{ * } \) . We say that \( X \) follows a binomial distribution with parameter \( \left( {n, p}\right) \) (denoted \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) ) if

\[
X\left( \Omega \right)  = \{ 0,\ldots , n\} ,\;\text{ et }\;\forall k \in  \{ 0,\ldots , n\} ,\;P\left( {X = k}\right)  = \left( \begin{array}{l} n \\  k \end{array}\right) {p}^{k}{\left( 1 - p\right) }^{n - k}.
\]

On a \( E\left( X\right) = {np} \) et \( V\left( X\right) = {np}\left( {1 - p}\right) \) .

> We have \( E\left( X\right) = {np} \) and \( V\left( X\right) = {np}\left( {1 - p}\right) \) .

La loi binomiale est celle d’une variable aléatoire \( X \) qui est la somme de \( n \) variables indépendantes \( {X}_{1},\ldots ,{X}_{n} \) qui suivent chacune une loi de Bernoulli de paramètre \( p \) , on l'appelle parfois loi du nombre du succés.

> The binomial distribution is that of a random variable \( X \) which is the sum of \( n \) independent variables \( {X}_{1},\ldots ,{X}_{n} \) each following a Bernoulli distribution with parameter \( p \) ; it is sometimes called the distribution of the number of successes.

Si \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) et \( Y \hookrightarrow \mathcal{B}\left( {m, p}\right) \) sont indépendantes, alors \( X + Y \hookrightarrow \mathcal{B}\left( {n + m, p}\right) \) .

> If \( X \hookrightarrow \mathcal{B}\left( {n, p}\right) \) and \( Y \hookrightarrow \mathcal{B}\left( {m, p}\right) \) are independent, then \( X + Y \hookrightarrow \mathcal{B}\left( {n + m, p}\right) \) .

Loi géométrique. Soit \( p \in \rbrack 0,1\left\lbrack \right. \) et \( n \in {\mathbb{N}}^{ * } \) . On dit que \( X \) suit une loi géométrique de paramètre \( p \) (et on note \( X \hookrightarrow \mathcal{G}\left( p\right) \) ) si

> Geometric distribution. Let \( p \in \rbrack 0,1\left\lbrack \right. \) and \( n \in {\mathbb{N}}^{ * } \) . We say that \( X \) follows a geometric distribution with parameter \( p \) (and we denote it \( X \hookrightarrow \mathcal{G}\left( p\right) \) ) if

\[
X\left( \Omega \right)  = {\mathbb{N}}^{ * },\;\text{ et }\;\forall n \in  {\mathbb{N}}^{ * },\;P\left( {X = n}\right)  = p{\left( 1 - p\right) }^{n - 1}.
\]

On a \( E\left( X\right) = 1/p \) et \( V\left( X\right) = \left( {1 - p}\right) /{p}^{2} \) .

> We have \( E\left( X\right) = 1/p \) and \( V\left( X\right) = \left( {1 - p}\right) /{p}^{2} \) .

Lors d'une succession infinie d'expériences de Bernoulli, cette loi est celle de la variable \( X \) définie par le rang du premier succés rencontré. Les lois géométriques sont caractérisées par des lois dans mémoire, comme l'exprime la proposition suivante.

> In an infinite sequence of Bernoulli trials, this distribution is that of the variable \( X \) defined by the rank of the first success encountered. Geometric distributions are characterized by memoryless properties, as expressed by the following proposition.

Proposition 13. Soit \( X \) une variable aléatoire à valeurs dans \( {\mathbb{N}}^{ * } \) . Alors \( X \) suit une loi géométrique si et seulement si \( P\left( {X = 1}\right) \in \rbrack 0,1\lbrack \) et \( X \) est sans mémoire, c’est-à-dire

> Proposition 13. Let \( X \) be a random variable taking values in \( {\mathbb{N}}^{ * } \) . Then \( X \) follows a geometric distribution if and only if \( P\left( {X = 1}\right) \in \rbrack 0,1\lbrack \) and \( X \) is memoryless, that is to say

\[
\forall \left( {n, k}\right)  \in  {\left( {\mathbb{N}}^{ * }\right) }^{2},\;P\left( {X > n + k \mid  X > n}\right)  = P\left( {X > k}\right) .
\]

(*)

> Démonstration. Si \( X \) suit une loi géométrique de paramètre \( p \in \rbrack 0,1\lbrack \) , on a pour tout \( \ell \in \mathbb{N} \)

Proof. If \( X \) follows a geometric distribution with parameter \( p \in \rbrack 0,1\lbrack \) , we have for all \( \ell \in \mathbb{N} \)

\[
P\left( {X > \ell }\right)  = \mathop{\sum }\limits_{{k = \ell  + 1}}^{{+\infty }}P\left( {X = k}\right)  = \mathop{\sum }\limits_{{k = \ell  + 1}}^{{+\infty }}p{\left( 1 - p\right) }^{k - 1} = {\left( 1 - p\right) }^{\ell }.
\]

Done

> Therefore

\[
P\left( {X > n + k \mid  X > n}\right)  = \frac{P\left( {X > n + k, X > n}\right) }{P\left( {X > n}\right) } = \frac{P\left( {X > n + k}\right) }{P\left( {X > n}\right) } = {\left( 1 - p\right) }^{k} = P\left( {X > k}\right) .
\]

Réciproquement supposons \( X \) sans mémoire, et notons \( p = P\left( {X = 1}\right) \in \rbrack 0,1\lbrack \) . Comme \( X \) est à valeurs dans \( {\mathbb{N}}^{ * } \) , on a \( P\left( {X > 1}\right) = 1 - P\left( {X = 1}\right) = 1 - p \) . En appliquant (*) avec \( k = 1 \) on obtient

> Conversely, suppose \( X \) is memoryless, and let \( p = P\left( {X = 1}\right) \in \rbrack 0,1\lbrack \) . Since \( X \) takes values in \( {\mathbb{N}}^{ * } \) , we have \( P\left( {X > 1}\right) = 1 - P\left( {X = 1}\right) = 1 - p \) . By applying (*) with \( k = 1 \) we obtain

\[
1 - p = P\left( {X > 1}\right)  = P\left( {X > n + 1 \mid  X > n}\right)  = \frac{P\left( {X > n + 1, X > n}\right) }{P\left( {X > n}\right) } = \frac{P\left( {X > n + 1}\right) }{P\left( {X > n}\right) }
\]

donc \( P\left( {X > n + 1}\right) = \left( {1 - p}\right) P\left( {X > n}\right) \) , ce qui par récurrence sur \( n \) entraîne \( P\left( {X > n}\right) = {\left( 1 - p\right) }^{n} \) . La variable aléatoire \( X \) suit donc bien une loi géométrique, de paramètre \( p \in \rbrack 0,1\lbrack \) puisque \( P\left( {X = 1}\right) = p \) et si \( n > 1, P\left( {X = n}\right) = P\left( {X > n - 1}\right) - P\left( {X > n}\right) = {\left( 1 - p\right) }^{n - 1}p. \)

> thus \( P\left( {X > n + 1}\right) = \left( {1 - p}\right) P\left( {X > n}\right) \) , which by induction on \( n \) leads to \( P\left( {X > n}\right) = {\left( 1 - p\right) }^{n} \) . The random variable \( X \) therefore follows a geometric distribution with parameter \( p \in \rbrack 0,1\lbrack \) since \( P\left( {X = 1}\right) = p \) and if \( n > 1, P\left( {X = n}\right) = P\left( {X > n - 1}\right) - P\left( {X > n}\right) = {\left( 1 - p\right) }^{n - 1}p. \)

Loi de Poisson. Soit \( \lambda > 0 \) . On dit que \( X \) suit une loi de Poisson de paramètre \( \lambda \) (et on note \( X \hookrightarrow \mathcal{P}\left( \lambda \right) \) ) si

> Poisson distribution. Let \( \lambda > 0 \) . We say that \( X \) follows a Poisson distribution with parameter \( \lambda \) (and we denote it \( X \hookrightarrow \mathcal{P}\left( \lambda \right) \) ) if

\[
X\left( \Omega \right)  = \mathbb{N},\;\text{ et }\;\forall n \in  \mathbb{N},\;P\left( {X = n}\right)  = {e}^{-\lambda }\frac{{\lambda }^{n}}{n!}.
\]

On a \( E\left( X\right) = \lambda \) et \( V\left( X\right) = \lambda \) .

> We have \( E\left( X\right) = \lambda \) and \( V\left( X\right) = \lambda \) .

La loi de Poisson est celle d'une variable aléatoire \( X \) qui compte le nombre d'événé- ments indépendants qui se produisent dans un intervalle de temps donné (par exemple : le nombre de clients rentrant dans un magasin, dans un intervalle de temps donné). Elle est la limite de la loi binomiale de paramètre \( \left( {n,\lambda /n}\right) \) lorsque \( n \rightarrow + \infty \) . En effet, si \( \left( {X}_{n}\right) \) est une suite de variables aléatoires discrètes suivant chacune un loi binomiale de paramètre \( \left( {n,\lambda /n}\right) \) , on a, pour tout \( k \) fixé, lorsque \( n \rightarrow + \infty \) ,

> The Poisson distribution is that of a discrete random variable \( X \) that counts the number of independent events occurring within a given time interval (for example: the number of customers entering a store in a given time interval). It is the limit of the binomial distribution with parameter \( \left( {n,\lambda /n}\right) \) as \( n \rightarrow + \infty \) . Indeed, if \( \left( {X}_{n}\right) \) is a sequence of discrete random variables each following a binomial distribution with parameter \( \left( {n,\lambda /n}\right) \) , then for any fixed \( k \) , as \( n \rightarrow + \infty \) ,

\[
P\left( {{X}_{n} = k}\right)  = \left( \begin{array}{l} n \\  k \end{array}\right) {\left( \frac{\lambda }{n}\right) }^{k}{\left( 1 - \frac{\lambda }{n}\right) }^{n - k} \sim  \frac{{n}^{k}}{k!}{\left( \frac{\lambda }{n}\right) }^{k}{\left( 1 - \frac{\lambda }{n}\right) }^{n} \sim  \frac{{\lambda }^{k}}{k!}{e}^{-\lambda },
\]

où on a utilisé l’équivalent \( \left( \begin{array}{l} n \\ k \end{array}\right) = \frac{n\left( {n - 1}\right) \cdots \left( {n - k + 1}\right) }{k!} \sim \frac{{n}^{k}}{k!} \) . Par exemple, si chaque seconde, il y a une probabilité \( p = 1/{600} \) qu’un client entre dans un magasin, le nombre de clients qui entrent sur un intervalle d'une heure suit approximativement une loi de poisson de paramètre \( \lambda = {3600p} = 6 \) . Pour cette raison, on appelle parfois cette loi la loi des événements rares.

> where we used the equivalent \( \left( \begin{array}{l} n \\ k \end{array}\right) = \frac{n\left( {n - 1}\right) \cdots \left( {n - k + 1}\right) }{k!} \sim \frac{{n}^{k}}{k!} \) . For example, if every second there is a probability \( p = 1/{600} \) that a customer enters a store, the number of customers entering over a one-hour interval approximately follows a Poisson distribution with parameter \( \lambda = {3600p} = 6 \) . For this reason, this distribution is sometimes called the law of rare events.

Si \( X \hookrightarrow \mathcal{P}\left( \lambda \right) \) et \( Y \hookrightarrow \mathcal{P}\left( \mu \right) \) sont indépendantes, alors \( X + Y \hookrightarrow \mathcal{P}\left( {\lambda + \mu }\right) \) .

> If \( X \hookrightarrow \mathcal{P}\left( \lambda \right) \) and \( Y \hookrightarrow \mathcal{P}\left( \mu \right) \) are independent, then \( X + Y \hookrightarrow \mathcal{P}\left( {\lambda + \mu }\right) \) .

Si à chaque événement comptabilisé par une loi de Poisson de paramètre \( \lambda \) , on associe une expérience de Bernoulli de paramètre \( p \) , le nombre d'événements à succés suit une loi de Poisson de paramètre \( {p\lambda } \) . Par exemple, si le nombre de clients \( X \) entrant dans un magasin suit une loi de Poisson de paramètre \( \lambda \) et si chaque client a une probabilité \( p \) d’être un enfant, le nombre d’enfants \( Y \) qui entrent dans le magasin suit une loi de Poisson de paramètre \( {p\lambda } \) . En effet, on a, pour tout \( k \in \mathbb{N} \)

> If each event counted by a Poisson distribution with parameter \( \lambda \) is associated with a Bernoulli trial with parameter \( p \) , the number of successful events follows a Poisson distribution with parameter \( {p\lambda } \) . For example, if the number of customers \( X \) entering a store follows a Poisson distribution with parameter \( \lambda \) and if each customer has a probability \( p \) of being a child, the number of children \( Y \) entering the store follows a Poisson distribution with parameter \( {p\lambda } \) . Indeed, for any \( k \in \mathbb{N} \)

\[
P\left( {Y = k}\right)  = \mathop{\sum }\limits_{{n = k}}^{{+\infty }}P\left( {Y = k \mid  X = n}\right) P\left( {X = n}\right)
\]

\[
= \mathop{\sum }\limits_{{n = k}}^{{+\infty }}\left( \begin{array}{l} n \\  k \end{array}\right) {p}^{k}{\left( 1 - p\right) }^{n - k}{e}^{-\lambda }\frac{{\lambda }^{n}}{n!} = \frac{{\lambda }^{k}{p}^{k}}{k!}\mathop{\sum }\limits_{{n = k}}^{{+\infty }}\frac{{\left( 1 - p\right) }^{n - k}}{\left( {n - k}\right) !}{e}^{-\lambda }{\lambda }^{n - k} = \frac{{\left( \lambda p\right) }^{k}}{k!}{e}^{-{\lambda p}}.
\]
