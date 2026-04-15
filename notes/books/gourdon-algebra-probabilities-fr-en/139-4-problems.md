### 4. Problems

*Français : 4. Problèmes*

Problem 1. 1 / Soit \( n \in \mathbb{N}, n \geq 2 \) . On place \( n \) boules de manière aléatoire,équiprobable, et indépendante, dans \( n \) urnes. Pour tout \( i \) on note \( {N}_{i} \) la variable aléatoire qui compte le nombre de boules dans l’urne numéro \( i \) , et \( {M}_{n} = \mathop{\max }\limits_{{1 \leq i \leq n}}{N}_{i} \) .

> Problem 1. 1 / Let \( n \in \mathbb{N}, n \geq 2 \) . We place \( n \) balls randomly, equiprobably, and independently, into \( n \) urns. For any \( i \) we denote by \( {N}_{i} \) the random variable that counts the number of balls in urn number \( i \) , and \( {M}_{n} = \mathop{\max }\limits_{{1 \leq i \leq n}}{N}_{i} \) .

a) Quelle est la proportion moyenne d’urnes vides, et sa limite lorsque \( n \rightarrow + \infty \) ?

> a) What is the average proportion of empty urns, and its limit as \( n \rightarrow + \infty \) ?

b) Calculer les lois de \( {N}_{i} \) , puis montrer que pour tout \( k \in {\mathbb{N}}^{ * }, P\left( {{M}_{n} = k}\right) \leq n/k \) !. Les \( {N}_{i} \) sont elles indépendantes?

> b) Calculate the distributions of \( {N}_{i} \) , then show that for any \( k \in {\mathbb{N}}^{ * }, P\left( {{M}_{n} = k}\right) \leq n/k \) !. Are the \( {N}_{i} \) independent?

c) Montrer que pour tout \( \varepsilon > 0 \) , on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) = 0 \) .

> c) Show that for any \( \varepsilon > 0 \) , we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) = 0 \) .

2 / Dans 1 /, la non-indépendance des \( {N}_{i} \) rend difficile l’obtention d’une borne minimum en probabilité pour \( {M}_{n} \) . Pour ce faire, on modifie l’expérience aléatoire, en se plaçant dans le cas où le nombre de boules placées aléatoirement dans les \( n \) urnes est une variable aléatoire \( K \) qui suit une loi de Poisson de paramètre \( {n\alpha } \) , où \( \alpha > 0 \) est fixé. Par simplicité, on note toujours \( {N}_{i} \) le nombre de boules dans l’urne numéro \( i \) et \( {M}_{n,\alpha } = \mathop{\max }\limits_{{1 \leq i \leq n}}{N}_{i} \) .

> 2 / In 1 /, the non-independence of the \( {N}_{i} \) makes it difficult to obtain a minimum bound in probability for \( {M}_{n} \) . To do this, we modify the random experiment by placing ourselves in the case where the number of balls placed randomly into the \( n \) urns is a random variable \( K \) which follows a Poisson distribution with parameter \( {n\alpha } \) , where \( \alpha > 0 \) is fixed. For simplicity, we still denote by \( {N}_{i} \) the number of balls in urn number \( i \) and \( {M}_{n,\alpha } = \mathop{\max }\limits_{{1 \leq i \leq n}}{N}_{i} \) .

a) Montrer que les \( {N}_{i} \) sont indépendantes et suivent une loi de Poisson de paramètre \( \alpha \) . b) Montrer que \( {M}_{n,\alpha }\log \log n/\log n \) converge vers 1 en probabilité, c’est-à-dire

> a) Show that the \( {N}_{i} \) are independent and follow a Poisson distribution with parameter \( \alpha \) . b) Show that \( {M}_{n,\alpha }\log \log n/\log n \) converges to 1 in probability, that is to say

\[
\forall \varepsilon  > 0,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {\left| {\frac{{M}_{n,\alpha }}{\log n/\log \log n} - 1}\right|  > \varepsilon }\right)  = 0.
\]

c) En déduire que \( {M}_{n}\log \log n/\log n \) converge vers 1 en probabilité (où \( {M}_{n} \) est la variable aléatoire définie dans la question 1/).

> c) Deduce that \( {M}_{n}\log \log n/\log n \) converges to 1 in probability (where \( {M}_{n} \) is the random variable defined in question 1/).

Solution. 1/a) Une urne donnée est vide si chacun des \( n \) placements se fait dans les \( n - 1 \) autres urnes, elle a donc une probabilité \( {p}_{n} = {\left( 1 - 1/n\right) }^{n} \) d’être vide. Notons \( {X}_{i} \) la variable aléatoire qui vaut 1 sur l’urne numéro \( i \) est vide,0 sinon. Elle suit une loi de Bernoulli de paramètre \( {p}_{n} \) , et le nombre d’urnes vides est \( \mathop{\sum }\limits_{{i = 1}}^{n}{X}_{i} \) , et le nombre moyen égal à \( \mathop{\sum }\limits_{{i = 1}}^{n}E\left( {X}_{i}\right) = n{p}_{n} \) . La proportion moyenne d’urnes vides est donc \( {p}_{n} = {\left( 1 - 1/n\right) }^{n} \) , et sa limite est \( 1/e \) lorsque \( n \rightarrow + \infty \) .

> Solution. 1/a) A given urn is empty if each of the \( n \) placements is made into the \( n - 1 \) other urns, so it has a probability \( {p}_{n} = {\left( 1 - 1/n\right) }^{n} \) of being empty. Let \( {X}_{i} \) be the random variable that equals 1 if urn number \( i \) is empty, 0 otherwise. It follows a Bernoulli distribution with parameter \( {p}_{n} \) , and the number of empty urns is \( \mathop{\sum }\limits_{{i = 1}}^{n}{X}_{i} \) , with an average number equal to \( \mathop{\sum }\limits_{{i = 1}}^{n}E\left( {X}_{i}\right) = n{p}_{n} \) . The average proportion of empty urns is therefore \( {p}_{n} = {\left( 1 - 1/n\right) }^{n} \) , and its limit is \( 1/e \) as \( n \rightarrow + \infty \) .

b) Soit \( k \in \{ 0,\ldots , n\} \) . On a \( {N}_{i} = k \) si et seulement si on choisit \( k \) boules parmi les \( n \) , chacune de ces \( k \) boules se trouvant dans l’urne numéro \( i \) (avec probabilité \( 1/n \) ), et les \( n - k \) autres se trouvant dans les autres urnes (avec probabilité \( 1 - 1/n \) ). Donc

> b) Let \( k \in \{ 0,\ldots , n\} \) . We have \( {N}_{i} = k \) if and only if we choose \( k \) balls out of the \( n \) , each of these \( k \) balls being in urn number \( i \) (with probability \( 1/n \) ), and the \( n - k \) others being in the other urns (with probability \( 1 - 1/n \) ). Therefore

\[
P\left( {{N}_{i} = k}\right)  = \left( \begin{array}{l} n \\  k \end{array}\right) {\left( \frac{1}{n}\right) }^{k}{\left( \frac{n - 1}{n}\right) }^{n - k}.
\]

On en déduit l'inégalité

> We deduce the inequality

\[
P\left( {{N}_{i} = k}\right)  = \frac{n\left( {n - 1}\right) \cdots \left( {n - k + 1}\right) }{{n}^{k}}\frac{1}{k!}{\left( \frac{n - 1}{n}\right) }^{n - k} \leq  \frac{1}{k!}.
\]

Or \( \left\{ {{M}_{n} = k}\right\} \subset { \cup }_{i = 1}^{n}\left\{ {{N}_{i} = k}\right\} \) donc

> However \( \left\{ {{M}_{n} = k}\right\} \subset { \cup }_{i = 1}^{n}\left\{ {{N}_{i} = k}\right\} \) therefore

\[
P\left( {{M}_{n} = k}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}P\left( {{N}_{i} = k}\right)  \leq  \frac{n}{k!}.
\]

Les \( {N}_{i} \) ne sont pas indépendantes car \( P\left( {{N}_{1} = n,{N}_{2} = 1}\right) = 0 \) et \( P\left( {{N}_{1} = n}\right) P\left( {{N}_{2} = 1}\right) \neq 0 \) . c) D'après la question précédente on a

> The \( {N}_{i} \) are not independent because \( P\left( {{N}_{1} = n,{N}_{2} = 1}\right) = 0 \) and \( P\left( {{N}_{1} = n}\right) P\left( {{N}_{2} = 1}\right) \neq 0 \) . c) According to the previous question, we have

\[
\forall m \in  {\mathbb{N}}^{ * },\;P\left( {{M}_{n} > m}\right)  \leq  \mathop{\sum }\limits_{{k = m + 1}}^{n}\frac{n}{k!} = \frac{n}{m!}\left( {\frac{1}{m + 1} + \frac{1}{\left( {m + 1}\right) \left( {m + 2}\right) } + \cdots }\right)  \leq  \frac{n}{m!}.
\]

Notons \( {m}_{n} \) est le plus petit entier \( m > 0 \) vérifiant \( n \leq m \) !, de sorte que \( \left( {{m}_{n} - 1}\right) ! < n \leq {m}_{n}! \) . On a \( \log \left( {\left( {{m}_{n} - 1}\right) !}\right) \leq \log n < \log \left( {{m}_{n}!}\right) \) . La formule de Stirling entraîne \( \log m! \sim m\log m \) , donc on a \( {m}_{n}\log {m}_{n} \sim \log n \) . En considérant le logarithme des deux membres, ceci entraîne \( \log {m}_{n} \sim \log \log n \) , et en reinjectant, on obtient \( {m}_{n} \sim \log n/\log {m}_{n} \sim \log n/\log \log n \) . Notons que \( P\left( {{M}_{n} > {m}_{n} + 1}\right) \leq 1/\left( {{m}_{n} + 1}\right) \rightarrow 0 \) . Soit \( \varepsilon > 0 \) . Il existe \( {n}_{0} \in \mathbb{N} \) tel que pour tout \( n \geq {n}_{0} \) , \( {m}_{n} + 1 < \left( {1 + \varepsilon }\right) \log n/\log \log n \) , donc pour tout \( n \geq {n}_{0} \) on a \( P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) \leq \; P\left( {{M}_{n} > {m}_{n} + 1}\right) \leq 1/\left( {{m}_{n} + 1}\right) \) , d’où le résultat.

> Let \( {m}_{n} \) be the smallest integer \( m > 0 \) satisfying \( n \leq m \) !, so that \( \left( {{m}_{n} - 1}\right) ! < n \leq {m}_{n}! \) . We have \( \log \left( {\left( {{m}_{n} - 1}\right) !}\right) \leq \log n < \log \left( {{m}_{n}!}\right) \) . Stirling's formula implies \( \log m! \sim m\log m \) , so we have \( {m}_{n}\log {m}_{n} \sim \log n \) . Considering the logarithm of both sides, this implies \( \log {m}_{n} \sim \log \log n \) , and by substituting back, we obtain \( {m}_{n} \sim \log n/\log {m}_{n} \sim \log n/\log \log n \) . Note that \( P\left( {{M}_{n} > {m}_{n} + 1}\right) \leq 1/\left( {{m}_{n} + 1}\right) \rightarrow 0 \) . Let \( \varepsilon > 0 \) . There exists \( {n}_{0} \in \mathbb{N} \) such that for all \( n \geq {n}_{0} \) , \( {m}_{n} + 1 < \left( {1 + \varepsilon }\right) \log n/\log \log n \) , so for all \( n \geq {n}_{0} \) we have \( P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) \leq \; P\left( {{M}_{n} > {m}_{n} + 1}\right) \leq 1/\left( {{m}_{n} + 1}\right) \) , hence the result.

2/a) Nous sommes dans le cas équiprobable. Ainsi, la probabilité d’avoir \( {i}_{k} \) boules dans l’urne \( k \) pour \( 1 \leq k \leq n \) , lorsque \( {i}_{1} + \cdots + {i}_{n} = m \) , est égale à

> 2/a) We are in the equiprobable case. Thus, the probability of having \( {i}_{k} \) balls in urn \( k \) for \( 1 \leq k \leq n \) , when \( {i}_{1} + \cdots + {i}_{n} = m \) , is equal to

\[
P\left( {{N}_{1} = {i}_{1},,\ldots ,{N}_{n} = {i}_{n} \mid  K = m}\right)  = \left( \begin{matrix} m \\  {i}_{1},\ldots ,{i}_{n} \end{matrix}\right) \frac{1}{{n}^{m}} = \frac{m!}{{i}_{1}!\cdots {i}_{n}!}\frac{1}{{n}^{m}},
\]

donc

> therefore

\[
P\left( {{N}_{1} = {i}_{1},\ldots ,{N}_{n} = {i}_{n}}\right)  = P\left( {{N}_{1} = {i}_{1},\ldots ,{N}_{n} = {i}_{n} \mid  K = {i}_{1} + \cdots  + {i}_{n}}\right) P\left( {K = {i}_{1} + \cdots  + {i}_{n}}\right)
\]

\[
= \frac{\left( {{i}_{1} + \cdots  + {i}_{n}}\right) !}{{i}_{1}!\cdots {i}_{n}!}\frac{1}{{n}^{{i}_{1} + \cdots  + {i}_{n}}}{e}^{-{n\alpha }}\frac{{\left( n\alpha \right) }^{{i}_{1} + \cdots  + {i}_{n}}}{\left( {{i}_{1} + \cdots  + {i}_{n}}\right) !} = \mathop{\prod }\limits_{{k = 1}}^{n}{e}^{-\alpha }\frac{{\alpha }^{{i}_{k}}}{{i}_{k}!}
\]

qui s’exprime comme le produit de \( n \) lois de Poisson de paramètre \( \alpha \) . Ceci démontre le résultat souhaité.

> which is expressed as the product of \( n \) Poisson distributions with parameter \( \alpha \) . This proves the desired result.

b) Notons \( {M}_{n,\alpha }^{ * } = {M}_{n,\alpha }\log \log n/\log n \) . Pour démontrer la convergence en probabilité de \( {M}_{n,\alpha }^{ * } \) vers 1, il suffit de montrer que la fonction de répartition \( {F}_{n}\left( x\right) = P\left( {{M}_{n,\alpha }^{ * } \leq x}\right) \) vérifie : \( \forall \varepsilon > 0 \) , \( {F}_{n}\left( {1 - \varepsilon }\right) \rightarrow 0 \) et \( {F}_{n}\left( {1 + \varepsilon }\right) \rightarrow 1 \) . Pour tout \( x > 0 \) on a

> b) Let \( {M}_{n,\alpha }^{ * } = {M}_{n,\alpha }\log \log n/\log n \) . To prove the convergence in probability of \( {M}_{n,\alpha }^{ * } \) to 1, it suffices to show that the cumulative distribution function \( {F}_{n}\left( x\right) = P\left( {{M}_{n,\alpha }^{ * } \leq x}\right) \) satisfies: \( \forall \varepsilon > 0 \) , \( {F}_{n}\left( {1 - \varepsilon }\right) \rightarrow 0 \) and \( {F}_{n}\left( {1 + \varepsilon }\right) \rightarrow 1 \) . For all \( x > 0 \) we have

\[
{F}_{n}\left( x\right)  = P\left( {{N}_{1} \leq  x\frac{\log n}{\log \log n},\ldots ,{N}_{n} \leq  x\frac{\log n}{\log \log n}}\right)  = P{\left( {N}_{1} \leq  x\frac{\log n}{\log \log n}\right) }^{n}.
\]

Soit \( x > 0 \) et notons \( {u}_{n} = 1 + \left\lbrack {x\log n/\log \log n}\right\rbrack \) . On a

> Let \( x > 0 \) and let \( {u}_{n} = 1 + \left\lbrack {x\log n/\log \log n}\right\rbrack \) . We have

\[
P\left( {{N}_{1} \leq  x\frac{\log n}{\log \log n}}\right)  = 1 - P\left( {{N}_{1} \geq  {u}_{n}}\right) ,\;P\left( {{N}_{1} \geq  {u}_{n}}\right)  = \mathop{\sum }\limits_{{k = {u}_{n}}}^{{+\infty }}{e}^{-\alpha }\frac{{\alpha }^{k}}{k!}.
\]

Or

\[
P\left( {{N}_{1} \geq  {u}_{n}}\right)  = {e}^{-\alpha }\frac{{\alpha }^{{u}_{n}}}{{u}_{n}!}\left( {1 + \frac{1}{{u}_{n} + 1} + \frac{1}{\left( {{u}_{n} + 1}\right) \left( {{u}_{n} + 2}\right) } + \cdots }\right)  = {e}^{-\alpha }\frac{{\alpha }^{{u}_{n}}}{{u}_{n}!}\left( {1 + o\left( 1\right) }\right) .
\]

Comme \( {u}_{n} \rightarrow + \infty \) , on en déduit \( P\left( {{N}_{1} \geq {u}_{n}}\right) \rightarrow 0 \) et de plus

> Since \( {u}_{n} \rightarrow + \infty \) , we deduce \( P\left( {{N}_{1} \geq {u}_{n}}\right) \rightarrow 0 \) and furthermore

\[
\log P\left( {{N}_{1} \leq  x\frac{\log n}{\log \log n}}\right)  \sim   - P\left( {{N}_{1} \geq  {u}_{n}}\right)  \sim   - {e}^{-\alpha }\frac{{\alpha }^{{u}_{n}}}{{u}_{n}!}.
\]

Or

\[
{e}^{-\alpha }\frac{{\alpha }^{{u}_{n}}}{{u}_{n}!} = \exp \left( {-\alpha  + {u}_{n}\log \alpha  - \log \left( {{u}_{n}!}\right) }\right)  = \exp \left( {-{u}_{n}\log \left( {u}_{n}\right) \left( {1 + o\left( 1\right) }\right) }\right) ,
\]

ou nous avons encore une fois utilisé l’équivalent log \( {u}_{n}! \sim {u}_{n}\log {u}_{n} \) . La définition de \( {u}_{n} \) entraîne \( {u}_{n}\log {u}_{n} \sim x\log n \) , donc \( {e}^{-\alpha }{\alpha }^{{u}_{n}}/{u}_{n}! = \exp \left( {-x\log n\left( {1 + o\left( 1\right) }\right) }\right) = {n}^{-x + o\left( 1\right) } \) . On en déduit

> where we once again used the equivalent log \( {u}_{n}! \sim {u}_{n}\log {u}_{n} \) . The definition of \( {u}_{n} \) implies \( {u}_{n}\log {u}_{n} \sim x\log n \) , so \( {e}^{-\alpha }{\alpha }^{{u}_{n}}/{u}_{n}! = \exp \left( {-x\log n\left( {1 + o\left( 1\right) }\right) }\right) = {n}^{-x + o\left( 1\right) } \) . We deduce from this

\[
{F}_{n}\left( x\right)  = \exp \left( {n\log P\left( {{N}_{1} \leq  x\frac{\log n}{\log \log n}}\right) }\right)  = \exp \left( {-n{n}^{-x + o\left( 1\right) }\left( {1 + o\left( 1\right) }\right) }\right)  = \exp \left( {-{n}^{1 - x + o\left( 1\right) }}\right)
\]

donc si \( x < 1,{F}_{n}\left( x\right) \rightarrow 0 \) et si \( x > 1,{F}_{n}\left( x\right) \rightarrow 1 \) , ce qu’il fallait démontrer.

> therefore if \( x < 1,{F}_{n}\left( x\right) \rightarrow 0 \) and if \( x > 1,{F}_{n}\left( x\right) \rightarrow 1 \) , which was to be demonstrated.

c) L’idée est de comparer \( K \) à \( n \) , et comparer \( {M}_{n} \) à \( {M}_{n,\alpha } \) . Pour ce faire, on commence par fixer un nombre \( \alpha \in \rbrack 0,1\left\lbrack \right. \) quelconque (par exemple \( \alpha = 1/2) \) et noter \( {K}_{n,\alpha } \) la variable aléatoire \( K \) (elle dépend de \( n \) et \( \alpha \) ). La variable \( {K}_{n,\alpha } \) suit une loi de Poisson de paramètre \( {\alpha n} \) , sa moyenne et sa variance est \( {\alpha n} \) , donc l’inégalité de Bienaymé-Tchébycheff fournit

> c) The idea is to compare \( K \) to \( n \) , and compare \( {M}_{n} \) to \( {M}_{n,\alpha } \) . To do this, we start by fixing an arbitrary number \( \alpha \in \rbrack 0,1\left\lbrack \right. \) (for example \( \alpha = 1/2) \) and denote by \( {K}_{n,\alpha } \) the random variable \( K \) (it depends on \( n \) and \( \alpha \) ). The variable \( {K}_{n,\alpha } \) follows a Poisson distribution with parameter \( {\alpha n} \) , its mean and variance is \( {\alpha n} \) , so Bienaymé-Chebyshev's inequality provides

\[
P\left( {\left| {{K}_{n,\alpha } - {n\alpha }}\right|  > \left( {1 - \alpha }\right) n}\right)  \leq  \frac{V\left( {K}_{n,\alpha }\right) }{{\left( 1 - \alpha \right) }^{2}{n}^{2}} = \frac{\alpha }{{\left( 1 - \alpha \right) }^{2}n}.
\]

(*)

> Pour pouvoir comparer \( {M}_{n} \) et \( {M}_{n,\alpha } \) , il faut que ces variables aléatoires soient associées à une même expérience aléatoire. Pour ce faire, on considère une suite de variables aléatoires indépendantes \( \left( {X}_{k}\right) \) et suivant toutes la loi uniforme sur \( \{ 1,\ldots , n\} \) , et une variable aléatoire \( {K}_{n,\alpha } \) indépendante des \( \left( {X}_{k}\right) \) et suivant une loi de Poisson de paramètre \( {n\alpha } \) . On définit alors les variables aléatoires

To be able to compare \( {M}_{n} \) and \( {M}_{n,\alpha } \) , these random variables must be associated with the same random experiment. To do this, we consider a sequence of independent random variables \( \left( {X}_{k}\right) \) all following the uniform distribution on \( \{ 1,\ldots , n\} \) , and a random variable \( {K}_{n,\alpha } \) independent of the \( \left( {X}_{k}\right) \) and following a Poisson distribution with parameter \( {n\alpha } \) . We then define the random variables

\[
{N}_{k}\left( {n,\alpha }\right)  = \mathop{\sum }\limits_{{i = 1}}^{{K}_{n,\alpha }}{\mathbf{1}}_{\left\{  {X}_{i} = k\right\}  }\;\text{ et }\;{N}_{k} = \mathop{\sum }\limits_{{i = 1}}^{n}{\mathbf{1}}_{\left\{  {X}_{i} = k\right\}  }
\]

puis

> then

\[
{M}_{n,\alpha } = \max \left\{  {{N}_{1}\left( {n,\alpha }\right) ,\ldots ,{N}_{n}\left( {n,\alpha }\right) }\right\}  \;\text{ et }\;{M}_{n} = \max \left\{  {{N}_{1},\ldots ,{N}_{n}}\right\}  .
\]

Ainsi définie, \( {M}_{n} \) (respectivement \( {M}_{n,\alpha } \) ) est bien le nombre maximum de boules dans une même urne, lorsqu’on place \( n \) boules (respectivement \( {K}_{n,\alpha } \) boules). On peut maintenant comparer ces variables aléatoires, de sorte que lorsque \( K\left( {n,\alpha }\right) \leq n \) , on a \( {M}_{n,\alpha } \leq {M}_{n} \) . Ainsi pour tout \( m > 0 \) on peut écrire

> Defined in this way, \( {M}_{n} \) (respectively \( {M}_{n,\alpha } \) ) is indeed the maximum number of balls in a single urn, when placing \( n \) balls (respectively \( {K}_{n,\alpha } \) balls). We can now compare these random variables, so that when \( K\left( {n,\alpha }\right) \leq n \) , we have \( {M}_{n,\alpha } \leq {M}_{n} \) . Thus for any \( m > 0 \) we can write

\[
\left\{  {{M}_{n} < m}\right\}   = \left\{  {{M}_{n} < m,{K}_{n,\alpha } \leq  n}\right\}   \cup  \left\{  {{M}_{n} < m,{K}_{n,\alpha } > n}\right\}   \subset  \left\{  {{M}_{n,\alpha } < m}\right\}   \cup  \left\{  {{K}_{n,\alpha } > n}\right\}
\]

donc en l’appliquant avec \( m = \left( {1 - \varepsilon }\right) \log n/\log \log n \) on obtient

> so by applying it with \( m = \left( {1 - \varepsilon }\right) \log n/\log \log n \) we obtain

\[
P\left( {{M}_{n} < \left( {1 - \varepsilon }\right) \frac{\log n}{\log \log n}}\right)  \leq  P\left( {{M}_{n,\alpha } < \left( {1 - \varepsilon }\right) \frac{\log n}{\log \log n}}\right)  + P\left( {{K}_{n,\alpha } > n}\right) .
\]

D'après la question précédente et d'après (*), le terme de droite tend vers 0, donc le terme de gauche tend vers 0 . Avec le résultat établi en 1/c), on en déduit que \( {M}_{n}\log \log n/\log n \) converge vers 1 en probabilité (nous aurions pu prouver que \( P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) \rightarrow 0 \) sans \( 1/\mathrm{c}) \) , en utilisant une approche similaire à utilisée ici mais en choisissant \( \alpha > 1 \) ).

> According to the previous question and according to (*), the term on the right tends to 0, so the term on the left tends to 0 . With the result established in 1/c), we deduce that \( {M}_{n}\log \log n/\log n \) converges to 1 in probability (we could have proven that \( P\left( {{M}_{n} > \left( {1 + \varepsilon }\right) \log n/\log \log n}\right) \rightarrow 0 \) without \( 1/\mathrm{c}) \) , by using an approach similar to the one used here but by choosing \( \alpha > 1 \) ).

Problem 2. Soit \( p, n \in {\mathbb{N}}^{ * } \) avec \( p < n \) . On veut déterminer le nombre \( T\left( {n, p}\right) \) de façons de placer \( p \) chaises blanches et \( q = n - p \) chaises noires autour d’une table ronde de \( n \) places (on ne compte que le placement relatif des chaises).

> Problem 2. Let \( p, n \in {\mathbb{N}}^{ * } \) with \( p < n \) . We want to determine the number \( T\left( {n, p}\right) \) of ways to place \( p \) white chairs and \( q = n - p \) black chairs around a round table with \( n \) seats (only the relative placement of the chairs is counted).

1 / Calculer \( T\left( {n, p}\right) \) dans le cas où \( p \) et \( q \) sont premiers entre eux.

> 1 / Calculate \( T\left( {n, p}\right) \) in the case where \( p \) and \( q \) are coprime.

2/ (Cas général) a) Soit \( m \in {\mathbb{N}}^{ * } \) et \( f, g \) deux fonctions réelles définies (au moins) sur l’ensemble \( {D}_{m} \) des diviseurs de \( m \) . On définit la convolution de Dirichlet de \( f \) et \( g \) , et on note \( f * g \) , la fonction définie sur \( {D}_{m} \) par

> 2/ (General case) a) Let \( m \in {\mathbb{N}}^{ * } \) and \( f, g \) be two real functions defined (at least) on the set \( {D}_{m} \) of divisors of \( m \) . We define the Dirichlet convolution of \( f \) and \( g \) , and denote it by \( f * g \) , as the function defined on \( {D}_{m} \) by

\[
\forall k \in  {D}_{m},\;\left( {f * g}\right) \left( k\right)  = \mathop{\sum }\limits_{{d \mid  k}}f\left( d\right) g\left( {k/d}\right) .
\]

(*)

> Montrer que la loi * ainsi définie sur les fonctions de \( {D}_{m} \) vers \( \mathbb{R} \) , est commutative et associative.

Show that the law * thus defined on the functions from \( {D}_{m} \) to \( \mathbb{R} \) , is commutative and associative.

> b) On considère la fonction de Möbius \( \mu \) définie sur \( {\mathbb{N}}^{ * } \) par \( \mu \left( 1\right) = 1 \) et

b) Consider the Möbius function \( \mu \) defined on \( {\mathbb{N}}^{ * } \) by \( \mu \left( 1\right) = 1 \) and

> \( \mu \left( m\right) = \left\{ \begin{array}{ll} {\left( -1\right) }^{k} & \text{ si }m\text{ est le produit de }k\text{ nombres premiers distincts, } \\ 0 & \text{ si }m\text{ est divisible par un carré d’un nombre premier. } \end{array}\right. \)

Montrer que \( \mathop{\sum }\limits_{{d \mid m}}\mu \left( d\right) = 0 \) si \( m > 1, = 1 \) si \( m = 1 \) .

> Show that \( \mathop{\sum }\limits_{{d \mid m}}\mu \left( d\right) = 0 \) if \( m > 1, = 1 \) if \( m = 1 \) .

c) (formule d’inversion de Möbius) : Soit \( m \in {\mathbb{N}}^{ * } \) . Si \( f \) et \( g \) sont deux fonctions définies sur \( {D}_{m} \) et si pour tout diviseur \( \ell \) de \( m \) on a \( g\left( \ell \right) = \mathop{\sum }\limits_{{d \mid \ell }}f\left( d\right) \) , alors montrer que

> c) (Möbius inversion formula): Let \( m \in {\mathbb{N}}^{ * } \) . If \( f \) and \( g \) are two functions defined on \( {D}_{m} \) and if for every divisor \( \ell \) of \( m \) we have \( g\left( \ell \right) = \mathop{\sum }\limits_{{d \mid \ell }}f\left( d\right) \) , then show that

\[
\forall k \in  {\mathbb{N}}^{ * }, k \mid  m,\;f\left( k\right)  = \mathop{\sum }\limits_{{d \mid  k}}\mu \left( d\right) g\left( {k/d}\right) .
\]

d) En notant \( \varphi \left( k\right) \) l’indicateur d’Euler de l’entier \( k \) , montrer que

> d) By denoting \( \varphi \left( k\right) \) as the Euler totient function of the integer \( k \) , show that

\[
\forall k \in  {\mathbb{N}}^{ * },\;\varphi \left( k\right)  = \mathop{\sum }\limits_{{d \mid  k}}d \cdot  \mu \left( {k/d}\right) .
\]

e) En notant \( \alpha = \operatorname{pgcd}\left( {p, q}\right) \) , montrer que

> e) By denoting \( \alpha = \operatorname{pgcd}\left( {p, q}\right) \) , show that

\[
T\left( {n, p}\right)  = \frac{1}{n}\mathop{\sum }\limits_{{d \mid  \alpha }}\varphi \left( d\right) \left( \begin{array}{l} n/d \\  p/d \end{array}\right)
\]

(pour tout entier \( r \) , on utilisera l’inversion de Möbius pour calculer le nombre \( {C}_{r}\left( {n, p}\right) \) de placements relatifs \( x \) de \( p \) chaises blanches et \( q = n - p \) noires, tels que \( r\left( x\right) = r \) , où \( r\left( x\right) \) désigne le plus petit entier \( k > 0 \) tel que \( x \) est invariant à une rotation de \( k \) chaises).

> (for any integer \( r \) , we will use the Möbius inversion to calculate the number \( {C}_{r}\left( {n, p}\right) \) of relative placements \( x \) of \( p \) white chairs and \( q = n - p \) black ones, such that \( r\left( x\right) = r \) , where \( r\left( x\right) \) denotes the smallest integer \( k > 0 \) such that \( x \) is invariant under a rotation of \( k \) chairs).

Solution. 1/ On note \( E = \{ \mathrm{\;B},\mathrm{\;N}\} \) l’ensemble des couleurs de chaises possibles (blanche ou noire). Chaque placement absolu (ici on ne compte pas les placements relatifs) de \( p \) chaises blanches et \( q \) chaises noires autour de la table est représenté par l’ensemble \( {P}_{p} \) des \( n \) -listes \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) de \( E \) , contenant \( p \) fois l’élément B (et forcément \( q = n - p \) fois l’élément \( \mathrm{N} \) ). On a donc \( \left( \begin{array}{l} n \\ p \end{array}\right) \) placements absolus possibles.

> Solution. 1/ Let \( E = \{ \mathrm{\;B},\mathrm{\;N}\} \) be the set of possible chair colors (white or black). Each absolute placement (here we do not count relative placements) of \( p \) white chairs and \( q \) black chairs around the table is represented by the set \( {P}_{p} \) of \( n \) -lists \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) of \( E \) , containing the element B \( p \) times (and necessarily the element \( \mathrm{N} \) \( q = n - p \) times). We therefore have \( \left( \begin{array}{l} n \\ p \end{array}\right) \) possible absolute placements.

On regroupe ensuite les emplacements égaux à une permutation prés. Pour cela, on considère les permutations circulaires \( G = \left\{ {{\gamma }^{k},0 \leq k < n}\right\} \) de \( \{ 1,\ldots , n\} \) , où \( \gamma \) est le cycle \( \left( {1,2,\ldots , n}\right) \) . On fait opérer \( G \) (sous-groupe de \( {\mathcal{S}}_{n} \) ) sur \( {P}_{p} \) , en définissant, pour tout \( k \in \mathbb{N}, k < n \)

> We then group the placements that are equal up to a permutation. To do this, we consider the circular permutations \( G = \left\{ {{\gamma }^{k},0 \leq k < n}\right\} \) of \( \{ 1,\ldots , n\} \) , where \( \gamma \) is the cycle \( \left( {1,2,\ldots , n}\right) \) . We let \( G \) (subgroup of \( {\mathcal{S}}_{n} \) ) act on \( {P}_{p} \) , by defining, for any \( k \in \mathbb{N}, k < n \)

\[
\forall x = \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {P}_{p},\;{\gamma }^{k}\left( x\right)  = \left( {{x}_{{\gamma }^{k}\left( 1\right) },\ldots ,{x}_{{\gamma }^{k}\left( n\right) }}\right)  = \left( {{x}_{k + 1},\ldots ,{x}_{n},{x}_{1},\ldots ,{x}_{k}}\right) ,
\]

le placement \( x \) après une rotation de \( k \) chaises. On considère la relation d’intransitivité sur \( {P}_{p} \) , définie par : \( x\mathcal{R}y \) si et seulement s’il existe \( k \in \{ 0,\ldots , n - 1\} \) tel que \( y = {\gamma }^{k}\left( x\right) \) (voir la définition 17 page 23). La classe d’équivalence de \( x \) est l’orbite \( {G}_{x} = \left\{ {{\gamma }^{k}\left( x\right) , k \in \mathbb{N}}\right\} \) .

> the placement \( x \) after a rotation of \( k \) chairs. We consider the intransitivity relation on \( {P}_{p} \) , defined by: \( x\mathcal{R}y \) if and only if there exists \( k \in \{ 0,\ldots , n - 1\} \) such that \( y = {\gamma }^{k}\left( x\right) \) (see definition 17 page 23). The equivalence class of \( x \) is the orbit \( {G}_{x} = \left\{ {{\gamma }^{k}\left( x\right) , k \in \mathbb{N}}\right\} \) .

Soit \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {P}_{p} \) . Prouvons que \( \left| {G}_{x}\right| = n \) . Notons \( m \) le plus petit entier \( > 0 \) tel que \( {\gamma }^{m}\left( x\right) = x \) . On a \( {G}_{x} = \left\{ {x,\gamma \left( x\right) ,\ldots ,{\gamma }^{m - 1}\left( x\right) }\right\} \) et \( \left| {G}_{x}\right| = m \) (si \( 0 \leq i < j < m \) alors \( {\gamma }^{i}\left( x\right) \neq {\gamma }^{j}\left( x\right) \) , sinon on aurait \( {\gamma }^{j - i}\left( x\right) = x \) , ce qui contredit la définition de \( m \) ). Comme \( {\gamma }^{n}\left( x\right) = x \) , on a forcément \( m \mid n \) (il suffit d’écrire \( n = {am} + b \) , avec \( a, b \in \mathbb{N} \) et \( 0 \leq b < m \) , qui entraine \( {\gamma }^{b}\left( x\right) = x \) donc \( b = 0 \) par minimalité de \( m \) ). Soit \( c \in {\mathbb{N}}^{ * } \) tel que \( n = {mc} \) . Pour tout \( k \in \{ 1,\ldots , m\} \) , l’ensemble des indices \( {I}_{k} = \{ k, k + m,\ldots , k + \left( {c - 1}\right) m\} \) vérifie \( {x}_{\ell } = {x}_{k} \) pour tout \( \ell \in {I}_{k} \) . En notant \( {R}_{\mathrm{B}} = \left\{ {k \in \{ 1,\ldots , m\} \mid {x}_{k} = \mathrm{B}}\right\} \) et \( {R}_{\mathrm{N}} = \left\{ {k \in \{ 1,\ldots , m\} \mid {x}_{k} = \mathrm{N}}\right\} \) , on en déduit que les \( {\left( {I}_{k}\right) }_{k \in {R}_{\mathrm{B}}} \) (resp. les \( {\left( {I}_{k}\right) }_{k \in {R}_{\mathrm{N}}} \) ) forment une partition des indices correspondants aux chaises blanches (resp. noires). Comme les \( {I}_{k} \) ont tous cardinal \( c \) , on en déduit \( p = c\left| {R}_{\mathrm{B}}\right| \) et \( q = c\left| {R}_{\mathrm{N}}\right| \) . Donc \( c \mid p \) et \( c \mid q \) . On vient donc de prouver le résultat suivant :

> Let \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {P}_{p} \) . Let us prove that \( \left| {G}_{x}\right| = n \) . Let \( m \) be the smallest integer \( > 0 \) such that \( {\gamma }^{m}\left( x\right) = x \) . We have \( {G}_{x} = \left\{ {x,\gamma \left( x\right) ,\ldots ,{\gamma }^{m - 1}\left( x\right) }\right\} \) and \( \left| {G}_{x}\right| = m \) (if \( 0 \leq i < j < m \) then \( {\gamma }^{i}\left( x\right) \neq {\gamma }^{j}\left( x\right) \) , otherwise we would have \( {\gamma }^{j - i}\left( x\right) = x \) , which contradicts the definition of \( m \) ). Since \( {\gamma }^{n}\left( x\right) = x \) , we necessarily have \( m \mid n \) (it suffices to write \( n = {am} + b \) , with \( a, b \in \mathbb{N} \) and \( 0 \leq b < m \) , which implies \( {\gamma }^{b}\left( x\right) = x \) hence \( b = 0 \) by the minimality of \( m \) ). Let \( c \in {\mathbb{N}}^{ * } \) be such that \( n = {mc} \) . For any \( k \in \{ 1,\ldots , m\} \) , the set of indices \( {I}_{k} = \{ k, k + m,\ldots , k + \left( {c - 1}\right) m\} \) satisfies \( {x}_{\ell } = {x}_{k} \) for all \( \ell \in {I}_{k} \) . By denoting \( {R}_{\mathrm{B}} = \left\{ {k \in \{ 1,\ldots , m\} \mid {x}_{k} = \mathrm{B}}\right\} \) and \( {R}_{\mathrm{N}} = \left\{ {k \in \{ 1,\ldots , m\} \mid {x}_{k} = \mathrm{N}}\right\} \) , we deduce that the \( {\left( {I}_{k}\right) }_{k \in {R}_{\mathrm{B}}} \) (resp. the \( {\left( {I}_{k}\right) }_{k \in {R}_{\mathrm{N}}} \) ) form a partition of the indices corresponding to the white (resp. black) chairs. Since the \( {I}_{k} \) all have cardinality \( c \) , we deduce \( p = c\left| {R}_{\mathrm{B}}\right| \) and \( q = c\left| {R}_{\mathrm{N}}\right| \) . Thus \( c \mid p \) and \( c \mid q \) . We have therefore just proven the following result:

\[
\forall x \in  {P}_{p},\;\left| {G}_{x}\right|  \mid  n\text{ et }c = n/\left| {G}_{x}\right| \text{ vérifie }c \mid  p\text{ et }c \mid  q.
\]

\( \left( {* * }\right) \)

> Ici \( p \) et \( q \) sont supposés premiers entre eux, on a donc \( c = 1 \) et \( \left| {G}_{x}\right| = n \) . Ainsi,à chaque placement relatif des chaises, correspond \( n \) placements absolus distincts, on a donc \( T\left( {n, p}\right) = \frac{1}{n}\left( \begin{array}{l} n \\ p \end{array}\right) \) .

Here \( p \) and \( q \) are assumed to be coprime, so we have \( c = 1 \) and \( \left| {G}_{x}\right| = n \) . Thus, to each relative placement of the chairs, corresponds \( n \) distinct absolute placements, so we have \( T\left( {n, p}\right) = \frac{1}{n}\left( \begin{array}{l} n \\ p \end{array}\right) \) .

> 2/a) La commutativité de la loi est immédiate en remarquant que

2/a) The commutativity of the law is immediate by noting that

\[
\left( {f * g}\right) \left( k\right)  = \mathop{\sum }\limits_{{\left( {a, b}\right)  \in  {\mathbb{N}}^{2},{ab} = k}}f\left( a\right) g\left( b\right) .
\]

Démontrons l’associativité. Soient \( f, g, h \) trois fonctions réelles définies sur \( {D}_{m} \) . Si \( k \in {D}_{m} \) on a

> Let us prove associativity. Let \( f, g, h \) be three real functions defined on \( {D}_{m} \) . If \( k \in {D}_{m} \) we have

\[
\left( {\left( {f * g}\right)  * h}\right) \left( k\right)  = \mathop{\sum }\limits_{\substack{{\left( {a, b}\right)  \in  {\mathbb{N}}^{2}} \\  {{ab} = k} }}\left( {f * g}\right) \left( a\right) h\left( b\right)  = \mathop{\sum }\limits_{\substack{{\left( {a, b}\right)  \in  {\mathbb{N}}^{2}} \\  {{ab} = k} }}\mathop{\sum }\limits_{\substack{{\left( {c, d}\right)  \in  {\mathbb{N}}^{2}} \\  {{cd} = a} }}f\left( c\right) g\left( d\right) h\left( b\right)  = \mathop{\sum }\limits_{\substack{{\left( {b, c, d}\right)  \in  {\mathbb{N}}^{3}} \\  {{bcd} = k} }}f\left( c\right) g\left( d\right) h\left( b\right) ,
\]

et

\[
\left( {f * \left( {g * h}\right) }\right) \left( k\right)  = \mathop{\sum }\limits_{\substack{{\left( {a, b}\right)  \in  {\mathbb{N}}^{2}} \\  {{ab} = k} }}f\left( a\right) \left( {g * h}\right) \left( b\right)  = \mathop{\sum }\limits_{\substack{{\left( {a, b}\right)  \in  {\mathbb{N}}^{2}} \\  {{ab} = k} }}\mathop{\sum }\limits_{\substack{{\left( {c, d}\right)  \in  {\mathbb{N}}^{2}} \\  {{cd} = b} }}f\left( a\right) g\left( c\right) h\left( d\right)  = \mathop{\sum }\limits_{\substack{{\left( {a, c, d}\right)  \in  {\mathbb{N}}^{3}} \\  {{acd} = k} }}f\left( a\right) g\left( c\right) h\left( d\right) .
\]

On en déduit \( \left( {\left( {f * g}\right) * h}\right) \left( k\right) = \left( {f * \left( {g * h}\right) }\right) \left( k\right) \) , donc la loi \( * \) est bien associative.

> We deduce \( \left( {\left( {f * g}\right) * h}\right) \left( k\right) = \left( {f * \left( {g * h}\right) }\right) \left( k\right) \) , so the law \( * \) is indeed associative.

b) Pour \( m = 1 \) le résultat est évident. Supposons \( m > 1 \) et considérons sa décomposition en facteurs premiers \( m = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) . Notons \( \mathcal{P} = \left\{ {{p}_{1},\ldots ,{p}_{k}}\right\} \) . Il suffit d’écrire

> b) For \( m = 1 \) the result is obvious. Assume \( m > 1 \) and consider its prime factorization \( m = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) . Let \( \mathcal{P} = \left\{ {{p}_{1},\ldots ,{p}_{k}}\right\} \) . It suffices to write

\[
\mathop{\sum }\limits_{{d \mid  m}}\mu \left( d\right)  = \mathop{\sum }\limits_{{Q \subset  \mathcal{P}}}\mu \left( {\mathop{\prod }\limits_{{p \in  Q}}p}\right)  = \mathop{\sum }\limits_{{Q \subset  \mathcal{P}}}{\left( -1\right) }^{\left| Q\right| } = \mathop{\sum }\limits_{{j = 0}}^{k}\left( \begin{array}{l} k \\  j \end{array}\right) {\left( -1\right) }^{j} = {\left( 1 - 1\right) }^{k} = 0.
\]

c) En notant 1 la fonction égale à 1 sur \( {D}_{m} \) , et \( \delta \) celle définie par \( \delta \left( k\right) = 1 \) si \( k = 1, = 0 \) sinon, le résultat de la question précédente s’écrit \( \mathbf{1} * \mu = \delta \) . Or ici, par hypothèse, on a \( g = \mathbf{1} * f \) , donc \( \mu * g = \mu * \left( {\mathbf{1} * f}\right) = \left( {\mu * \mathbf{1}}\right) * f = \delta * f = f \) , ce qui montre le résultat.

> c) By denoting 1 as the function equal to 1 on \( {D}_{m} \) , and \( \delta \) as the one defined by \( \delta \left( k\right) = 1 \) if \( k = 1, = 0 \) otherwise, the result of the previous question is written \( \mathbf{1} * \mu = \delta \) . However, here, by hypothesis, we have \( g = \mathbf{1} * f \) , so \( \mu * g = \mu * \left( {\mathbf{1} * f}\right) = \left( {\mu * \mathbf{1}}\right) * f = \delta * f = f \) , which shows the result.

d) L’indicateur d’Euler vérifie la relation classique \( \mathop{\sum }\limits_{{d \mid k}}\varphi \left( d\right) = k \) (voir la proposition 6 page 34). Autrement dit \( \varphi * \mathbf{1} = \mathrm{{Id}} \) , où Id est la fonction identité. Donc \( \varphi * \mathbf{1} * \mu = \mathrm{{Id}} * \mu \) , et comme \( \mathbf{1} * \mu = \delta \) on en déduit \( \varphi = \operatorname{Id} * \mu \) , d’où le résultat.

> d) Euler's totient function satisfies the classical relation \( \mathop{\sum }\limits_{{d \mid k}}\varphi \left( d\right) = k \) (see proposition 6 on page 34). In other words \( \varphi * \mathbf{1} = \mathrm{{Id}} \) , where Id is the identity function. Thus \( \varphi * \mathbf{1} * \mu = \mathrm{{Id}} * \mu \) , and since \( \mathbf{1} * \mu = \delta \) we deduce \( \varphi = \operatorname{Id} * \mu \) , hence the result.

e) On utilise les notations introduites à la solution de la question 1/. On suit l'indication, et on remarque que \( r\left( x\right) = \left| {G}_{x}\right| \) . D’après le résultat (**), on a forcément \( n = r\left( x\right) c \) où \( c \) est un entier vérifiant \( c \mid p \) et \( c \mid q \) , donc \( c \mid \operatorname{pgcd}\left( {p, q}\right) = \alpha \) . Notons \( {p}^{\prime } = p/\alpha ,{q}^{\prime } = q/\alpha \) et \( {n}^{\prime } = n/\alpha \) . On a donc \( r\left( x\right) = d{n}^{\prime } \) avec \( d \mid \alpha \) . Notons \( \Theta \) une partie de \( {P}_{p} \) contenant exactement un représentant de chaque classe \( {G}_{x} \) , et \( {\Theta }_{r} = \{ x \in \Theta \mid r\left( x\right) = r\} \) . On a

> e) We use the notations introduced in the solution to question 1/. We follow the hint, and note that \( r\left( x\right) = \left| {G}_{x}\right| \) . According to result (**), we necessarily have \( n = r\left( x\right) c \) where \( c \) is an integer satisfying \( c \mid p \) and \( c \mid q \) , so \( c \mid \operatorname{pgcd}\left( {p, q}\right) = \alpha \) . Let \( {p}^{\prime } = p/\alpha ,{q}^{\prime } = q/\alpha \) and \( {n}^{\prime } = n/\alpha \) . We thus have \( r\left( x\right) = d{n}^{\prime } \) with \( d \mid \alpha \) . Let \( \Theta \) be a subset of \( {P}_{p} \) containing exactly one representative of each class \( {G}_{x} \) , and \( {\Theta }_{r} = \{ x \in \Theta \mid r\left( x\right) = r\} \) . We have

\[
\left( \begin{array}{l} n \\  p \end{array}\right)  = \left| {P}_{p}\right|  = \mathop{\sum }\limits_{{x \in  \Theta }}\left| {G}_{x}\right|  = \mathop{\sum }\limits_{{d \mid  \alpha }}\mathop{\sum }\limits_{{x \in  {\Theta }_{d{n}^{\prime }}}}\left| {G}_{x}\right|  = \mathop{\sum }\limits_{{d \mid  \alpha }}\left( {d{n}^{\prime }}\right) {C}_{d{n}^{\prime }}\left( {n, p}\right)
\]

\( \left( {* * * }\right) \)

> où on a noté \( {C}_{r}\left( {n, p}\right) = \left| {\Theta }_{r}\right| \) . On rapproche ceci de la question \( 2/\mathrm{b} \) ), en remarquant que cette expression s'écrit aussi

where we have denoted \( {C}_{r}\left( {n, p}\right) = \left| {\Theta }_{r}\right| \) . We compare this to question \( 2/\mathrm{b} \) ), by noting that this expression can also be written

\[
g\left( \alpha \right)  = \mathop{\sum }\limits_{{d \mid  \alpha }}f\left( d\right) ,\;\text{ avec }\;g\left( \ell \right)  = \left( \begin{matrix} \ell {n}^{\prime } \\  \ell {p}^{\prime } \end{matrix}\right) \text{ et }f\left( k\right)  = k{n}^{\prime }{C}_{k{n}^{\prime }}\left( {n, p}\right) .
\]

Lorsque \( \beta \mid \alpha \) , la formule (***) appliquée en remplaçant \( n \) par \( \beta {n}^{\prime } \) et \( p \) par \( \beta {p}^{\prime } \) fournit

> When \( \beta \mid \alpha \) , formula (***) applied by replacing \( n \) with \( \beta {n}^{\prime } \) and \( p \) with \( \beta {p}^{\prime } \) provides

\[
g\left( \beta \right)  = \mathop{\sum }\limits_{{d \mid  \beta }}\left( {d{n}^{\prime }}\right) {C}_{d{n}^{\prime }}\left( {\beta {n}^{\prime },\beta {p}^{\prime }}\right) .
\]

Or lorsque \( \beta \mid \alpha \) et \( d \mid \beta \) , on a \( {C}_{d{n}^{\prime }}\left( {\beta {n}^{\prime },\beta {p}^{\prime }}\right) = {C}_{d{n}^{\prime }}\left( {n, p}\right) \) puisque les placements \( x \) invariants à une rotation de \( r = d{n}^{\prime } \) chaises sont uniquement déterminés par les \( r \) premières valeurs \( \left( {{x}_{1},\ldots ,{x}_{r}}\right) \) , qui doivent contenir \( d{p}^{\prime } \) fois B et \( d{q}^{\prime } \) fois \( \mathrm{N} \) , et ne dépendent donc pas du nombre total de chaises de la table (qui est un multiple de \( r \) ). Ainsi on peut écrire \( g\left( \beta \right) = \mathop{\sum }\limits_{{d \mid \beta }}f\left( d\right) \) pour tout diviseur \( \beta \) de \( \alpha \) . Nous sommes donc dans les conditions d’application de la question \( 2/\mathrm{c} \) ) avec \( m = \alpha \) , ce qui entraîne \( f = \mu * g \) . Or on a

> Now, when \( \beta \mid \alpha \) and \( d \mid \beta \), we have \( {C}_{d{n}^{\prime }}\left( {\beta {n}^{\prime },\beta {p}^{\prime }}\right) = {C}_{d{n}^{\prime }}\left( {n, p}\right) \) since the arrangements \( x \) invariant under a rotation of \( r = d{n}^{\prime } \) chairs are uniquely determined by the \( r \) first values \( \left( {{x}_{1},\ldots ,{x}_{r}}\right) \), which must contain \( d{p}^{\prime } \) times B and \( d{q}^{\prime } \) times \( \mathrm{N} \), and therefore do not depend on the total number of chairs at the table (which is a multiple of \( r \)). Thus, we can write \( g\left( \beta \right) = \mathop{\sum }\limits_{{d \mid \beta }}f\left( d\right) \) for any divisor \( \beta \) of \( \alpha \). We are therefore in the conditions to apply question \( 2/\mathrm{c} \)) with \( m = \alpha \), which leads to \( f = \mu * g \). Now we have

\[
T\left( {n, p}\right)  = \left| \Theta \right|  = \mathop{\sum }\limits_{{\beta  \mid  \alpha }}\left| {\Theta }_{\beta {n}^{\prime }}\right|  = \mathop{\sum }\limits_{{\beta  \mid  \alpha }}{C}_{\beta {n}^{\prime }}\left( {n, p}\right)  = \mathop{\sum }\limits_{{\beta  \mid  \alpha }}\frac{1}{\beta {n}^{\prime }}f\left( \beta \right) ,
\]

on en déduit

> we deduce from this

\[
{nT}\left( {n, p}\right)  = \mathop{\sum }\limits_{{\beta  \mid  \alpha }}\left( {\alpha /\beta }\right) f\left( \beta \right)  = \left( {\operatorname{Id} * f}\right) \left( \alpha \right) .
\]

Or \( \operatorname{Id} * f = \operatorname{Id} * \left( {\mu * g}\right) = \left( {\operatorname{Id} * \mu }\right) * g = \varphi * g \) , et on conclut en écrivant

> Now \( \operatorname{Id} * f = \operatorname{Id} * \left( {\mu * g}\right) = \left( {\operatorname{Id} * \mu }\right) * g = \varphi * g \), and we conclude by writing

\[
{nT}\left( {n, p}\right)  = \left( {\varphi  * g}\right) \left( \alpha \right)  = \mathop{\sum }\limits_{{d \mid  \alpha }}\varphi \left( d\right) g\left( {\alpha /d}\right)  = \mathop{\sum }\limits_{{d \mid  \alpha }}\varphi \left( d\right) \left( \begin{array}{l} n/d \\  p/d \end{array}\right) .
\]

Problems 3. 1/ Pour toute famille d’ensembles de permutations \( \mathcal{P} = {\left( {\mathcal{P}}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) , avec \( {\mathcal{P}}_{n} \subset {\mathcal{S}}_{n} \) (où \( {\mathcal{S}}_{n} \) désigne le groupe symétrique d’indice \( n \) ), on note \( {\Phi }_{\mathcal{P}}\left( z\right) \) la série généra-trice exponentielle de \( \mathcal{P} \) définie par

> Problems 3. 1/ For any family of sets of permutations \( \mathcal{P} = {\left( {\mathcal{P}}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \), with \( {\mathcal{P}}_{n} \subset {\mathcal{S}}_{n} \) (where \( {\mathcal{S}}_{n} \) denotes the symmetric group of index \( n \)), we denote by \( {\Phi }_{\mathcal{P}}\left( z\right) \) the exponential generating series of \( \mathcal{P} \) defined by

\[
{\Phi }_{\mathcal{P}}\left( z\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\left| {\mathcal{P}}_{n}\right| }{n!}{z}^{n}
\]

a) Montrer que \( {\Phi }_{\mathcal{P}} \) a toujours un rayon de convergence \( \geq 1 \) .

> a) Show that \( {\Phi }_{\mathcal{P}} \) always has a radius of convergence \( \geq 1 \).

b) Soit \( N \) une partie de \( {\mathbb{N}}^{ * } \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {\mathcal{P}}_{n}\left( N\right) \) les permutations \( s \) de \( {\mathcal{S}}_{n} \) dont la longueur des cycles (dans la décomposition de \( s \) en produit de cycles) est dans l’ensemble \( N \) , et pour \( k \in {\mathbb{N}}^{ * } \) on note \( {\mathcal{P}}_{n}\left( {N, k}\right) \) l’ensemble des permutations de \( {\mathcal{P}}_{n}\left( N\right) \) qui s’écrivent comme le produit de \( k \) cycles. Montrer que la série génératrice exponentielle de \( \mathcal{P}\left( {N, k}\right) = {\left( {\mathcal{P}}_{n}\left( N, k\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) est égale à \( {C}_{N}{\left( z\right) }^{k}/k \) !, où \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{n \in N}}{z}^{n}/n \) .

> b) Let \( N \) be a subset of \( {\mathbb{N}}^{ * } \). For any \( n \in {\mathbb{N}}^{ * } \), we denote by \( {\mathcal{P}}_{n}\left( N\right) \) the permutations \( s \) of \( {\mathcal{S}}_{n} \) whose cycle lengths (in the decomposition of \( s \) into a product of cycles) are in the set \( N \), and for \( k \in {\mathbb{N}}^{ * } \) we denote by \( {\mathcal{P}}_{n}\left( {N, k}\right) \) the set of permutations of \( {\mathcal{P}}_{n}\left( N\right) \) that can be written as the product of \( k \) cycles. Show that the exponential generating series of \( \mathcal{P}\left( {N, k}\right) = {\left( {\mathcal{P}}_{n}\left( N, k\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) is equal to \( {C}_{N}{\left( z\right) }^{k}/k \)!, where \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{n \in N}}{z}^{n}/n \).

c) En déduire que la série génératrice exponentielle de \( \mathcal{P}\left( N\right) = {\left( {\mathcal{P}}_{n}\left( N\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) est égale à \( {\Phi }_{\mathcal{P}\left( N\right) }\left( z\right) = \exp \left( {{C}_{N}\left( z\right) }\right) - 1. \)

> c) Deduce that the exponential generating function of \( \mathcal{P}\left( N\right) = {\left( {\mathcal{P}}_{n}\left( N\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) is equal to \( {\Phi }_{\mathcal{P}\left( N\right) }\left( z\right) = \exp \left( {{C}_{N}\left( z\right) }\right) - 1. \)

2/a) Expliciter la série génératrice exponentielle des familles d'ensembles de permutations sans point fixe, et montrer que la probabilité qu'une permutation de \( \{ 1,\ldots , n\} \) n'ait aucun point fixe converge vers \( 1/e \) lorsque \( n \rightarrow + \infty \) .

> 2/a) Explicitly state the exponential generating function for families of sets of fixed-point-free permutations, and show that the probability that a permutation of \( \{ 1,\ldots , n\} \) has no fixed points converges to \( 1/e \) as \( n \rightarrow + \infty \) .

b) Donner l’expression puis un comportement asymptotique, lorsque \( n \rightarrow + \infty \) , de la probabilité qu'une permutation de \( \{ 1,\ldots , n\} \) n’ait que des cycles de longueur paire.

> b) Give the expression and an asymptotic behavior, as \( n \rightarrow + \infty \) , of the probability that a permutation of \( \{ 1,\ldots , n\} \) has only cycles of even length.

3/ Soit \( m \in {\mathbb{N}}^{ * } \) , désormais fixé. On note \( {H}_{m} = 1 + 1/2 + \cdots + 1/m \) .

> 3/ Let \( m \in {\mathbb{N}}^{ * } \) be fixed from now on. Let \( {H}_{m} = 1 + 1/2 + \cdots + 1/m \) .

a) Montrer que la fonction

> a) Show that the function

\[
{\varphi }_{m} : {D}^{ * } = \{ z \mid  \left| z\right|  \leq  1, z \neq  1\} , z \mapsto  \frac{{e}^{-z - {z}^{2}/2 - \cdots  - {z}^{m}/m}}{1 - z} - \frac{{e}^{-{H}_{m}}}{1 - z}
\]

est continue, et prolongeable par continuité sur \( D = \{ z \mid \left| z\right| \leq 1\} = {D}^{ * } \cup \{ 1\} \) .

> is continuous, and can be extended by continuity to \( D = \{ z \mid \left| z\right| \leq 1\} = {D}^{ * } \cup \{ 1\} \) .

b) Montrer que pour tout \( n \in {\mathbb{N}}^{ * } \) , la probabilité \( {p}_{n}\left( m\right) \) qu’une permutation de \( \{ 1,\ldots , n\} \) ait tout ses cycles de longueur \( > m \) vérifie

> b) Show that for all \( n \in {\mathbb{N}}^{ * } \) , the probability \( {p}_{n}\left( m\right) \) that a permutation of \( \{ 1,\ldots , n\} \) has all its cycles of length \( > m \) satisfies

\[
{p}_{n}\left( m\right)  = {e}^{-{H}_{m}} + \frac{1}{2\pi }{\int }_{0}^{2\pi }{\varphi }_{m}\left( {e}^{it}\right) {e}^{-{int}}{dt}.
\]

c) En déduire que lorsque \( n \rightarrow + \infty \) , la probabilité qu’une permutation de \( \{ 1,\ldots , n\} \) ait tout ses cycles de longueur \( > m \) , converge vers \( {e}^{-{H}_{m}} \) .

> c) Deduce that as \( n \rightarrow + \infty \) , the probability that a permutation of \( \{ 1,\ldots , n\} \) has all its cycles of length \( > m \) converges to \( {e}^{-{H}_{m}} \) .

Solution. 1/a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on a \( 0 \leq \left| {\mathcal{P}}_{n}\right| \leq \left| {\mathcal{S}}_{n}\right| = n \) !, donc \( 0 \leq \left| {\mathcal{P}}_{n}\right| /n! \leq 1 \) . On en déduit que la série entière \( \sum \left| {\mathcal{P}}_{n}\right| /n!{z}^{n} \) a un rayon de convergence \( \geq 1 \) .

> Solution. 1/a) For all \( n \in {\mathbb{N}}^{ * } \) , we have \( 0 \leq \left| {\mathcal{P}}_{n}\right| \leq \left| {\mathcal{S}}_{n}\right| = n \) !, so \( 0 \leq \left| {\mathcal{P}}_{n}\right| /n! \leq 1 \) . We deduce that the power series \( \sum \left| {\mathcal{P}}_{n}\right| /n!{z}^{n} \) has a radius of convergence \( \geq 1 \) .

b) On prouve le résultat par récurrence sur \( k \in {\mathbb{N}}^{ * } \) . Pour \( k = 1 \) c’est immédiat, car on a \( \left( {n - 1}\right) \) ! cycles de longueur \( n \) dans \( {\mathcal{S}}_{n} \) (pour construire un cycle \( c \) de longueur \( n \) dans \( {\mathcal{S}}_{n} \) , il y a \( n - 1 \) valeurs possibles pour \( c\left( 1\right) \) , puis \( n - 2 \) pour \( {c}^{2}\left( 1\right) ,\ldots ,1 \) valeur possible pour \( {c}^{n - 1}\left( 1\right) \) , donc un total de \( \left( {n - 1}\right) \) ! cycles possibles en tout), donc \( \left| {{\mathcal{P}}_{n}\left( {N,1}\right) }\right| /n! = 1/n \) si \( n \in N \) , \( = 0 \) sinon. Supposons le résultat vérifié pour \( k - 1 \) et montrons le pour \( k \) . Une permutation \( s \) de \( {\mathcal{P}}_{n}\left( {N, k}\right) \) s’écrit comme le produit d’un cycle \( {c}_{1} \) de longueur \( m \in N \) , portant sur \( m \) entiers choisis parmi \( \{ 1,\ldots , n\} \) , et d’une permutation des \( n - m \) autres entiers, qui s’écrit comme le produit de \( k - 1 \) cycles de longueur dans \( N \) . Il y a \( k \) manières différentes d’écrire \( s \) sous cette forme, car \( {c}_{1} \) peut être l’un des \( k \) cycles de \( s \) . On a donc

> b) We prove the result by induction on \( k \in {\mathbb{N}}^{ * } \) . For \( k = 1 \) it is immediate, because there are \( \left( {n - 1}\right) \) ! cycles of length \( n \) in \( {\mathcal{S}}_{n} \) (to construct a cycle \( c \) of length \( n \) in \( {\mathcal{S}}_{n} \) , there are \( n - 1 \) possible values for \( c\left( 1\right) \) , then \( n - 2 \) for \( {c}^{2}\left( 1\right) ,\ldots ,1 \) possible value for \( {c}^{n - 1}\left( 1\right) \) , thus a total of \( \left( {n - 1}\right) \) ! possible cycles in all), so \( \left| {{\mathcal{P}}_{n}\left( {N,1}\right) }\right| /n! = 1/n \) if \( n \in N \) , \( = 0 \) otherwise. Assume the result holds for \( k - 1 \) and let us show it for \( k \) . A permutation \( s \) of \( {\mathcal{P}}_{n}\left( {N, k}\right) \) can be written as the product of a cycle \( {c}_{1} \) of length \( m \in N \) , acting on \( m \) integers chosen from \( \{ 1,\ldots , n\} \) , and a permutation of the \( n - m \) other integers, which can be written as the product of \( k - 1 \) cycles of length in \( N \) . There are \( k \) different ways to write \( s \) in this form, because \( {c}_{1} \) can be one of the \( k \) cycles of \( s \) . We therefore have

\[
k\left| {{\mathcal{P}}_{n}\left( {N, k}\right) }\right|  = \mathop{\sum }\limits_{{m \in  N}}\left( \begin{matrix} n \\  m \end{matrix}\right) \left( {m - 1}\right) !\left| {{\mathcal{P}}_{n - m}\left( {N, k - 1}\right) }\right| ,
\]

ce qui s'écrit aussi

> which can also be written

\[
k\frac{\left| {\mathcal{P}}_{n}\left( N, k\right) \right| }{n!} = \mathop{\sum }\limits_{{m \in  N}}\frac{1}{m}\frac{\left| {\mathcal{P}}_{n - m}\left( N, k - 1\right) \right| }{\left( {n - m}\right) !}.
\]

On reconnait dans cette expression un produit de Cauchy ; on en déduit, pour \( \left| z\right| < 1 \) ,

> We recognize in this expression a Cauchy product; we deduce, for \( \left| z\right| < 1 \) ,

\[
k\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{\left| {\mathcal{P}}_{n}\left( N, k\right) \right| }{n!}{z}^{n} = \left( {\mathop{\sum }\limits_{{m \in  N}}\frac{{z}^{m}}{m}}\right) \left( {\mathop{\sum }\limits_{{\ell  = 1}}^{{+\infty }}\frac{\left| {\mathcal{P}}_{\ell }\left( N, k - 1\right) \right| }{\ell !}{z}^{\ell }}\right) .
\]

On a donc \( k{\Phi }_{\mathcal{P}\left( {N, k}\right) }\left( z\right) = {C}_{N}\left( z\right) {\Phi }_{\mathcal{P}\left( {N, k - 1}\right) }\left( z\right) = {C}_{N}{\left( z\right) }^{k}/\left( {k - 1}\right) \) !. Ceci démontre le résultat souhaité.

> We therefore have \( k{\Phi }_{\mathcal{P}\left( {N, k}\right) }\left( z\right) = {C}_{N}\left( z\right) {\Phi }_{\mathcal{P}\left( {N, k - 1}\right) }\left( z\right) = {C}_{N}{\left( z\right) }^{k}/\left( {k - 1}\right) \) !. This proves the desired result.

c) Soit \( n \in {\mathbb{N}}^{ * } \) . Chaque permutation dans \( {\mathcal{P}}_{n}\left( N\right) \) a au plus \( n \) cycles, donc \( \left| {{\mathcal{P}}_{n}\left( N\right) }\right| /n! = \; \mathop{\sum }\limits_{{k = 1}}^{n}\left| {{\mathcal{P}}_{n}\left( {N, k}\right) }\right| /n \) ! est le coefficient de \( {z}^{n} \) dans \( \mathop{\sum }\limits_{{k = 1}}^{n}{\Phi }_{\mathcal{P}\left( {N, k}\right) }\left( z\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{C}_{N}{\left( z\right) }^{k}/k \) !. Or pour \( k > n \) , le coefficient de \( {z}^{n} \) dans \( {C}_{N}{\left( z\right) }^{k} \) est nul (car le coefficient constant de \( {C}_{N}\left( z\right) \) est nul). On en déduit que \( \left| {{\mathcal{P}}_{n}\left( N\right) }\right| /n! \) est le coefficient de \( {z}^{n} \) dans \( \mathop{\sum }\limits_{{k = 1}}^{n}{C}_{N}{\left( z\right) }^{k}/k! + \mathop{\sum }\limits_{{k > n}}{C}_{N}{\left( z\right) }^{k}/k! = \; \exp \left( {{C}_{N}\left( z\right) }\right) - 1 \) .

> c) Let \( n \in {\mathbb{N}}^{ * } \) . Each permutation in \( {\mathcal{P}}_{n}\left( N\right) \) has at most \( n \) cycles, so \( \left| {{\mathcal{P}}_{n}\left( N\right) }\right| /n! = \; \mathop{\sum }\limits_{{k = 1}}^{n}\left| {{\mathcal{P}}_{n}\left( {N, k}\right) }\right| /n \) ! is the coefficient of \( {z}^{n} \) in \( \mathop{\sum }\limits_{{k = 1}}^{n}{\Phi }_{\mathcal{P}\left( {N, k}\right) }\left( z\right) = \mathop{\sum }\limits_{{k = 1}}^{n}{C}_{N}{\left( z\right) }^{k}/k \) !. However, for \( k > n \) , the coefficient of \( {z}^{n} \) in \( {C}_{N}{\left( z\right) }^{k} \) is zero (since the constant coefficient of \( {C}_{N}\left( z\right) \) is zero). We deduce that \( \left| {{\mathcal{P}}_{n}\left( N\right) }\right| /n! \) is the coefficient of \( {z}^{n} \) in \( \mathop{\sum }\limits_{{k = 1}}^{n}{C}_{N}{\left( z\right) }^{k}/k! + \mathop{\sum }\limits_{{k > n}}{C}_{N}{\left( z\right) }^{k}/k! = \; \exp \left( {{C}_{N}\left( z\right) }\right) - 1 \) .

2/a) Une permutation \( s \in {\mathcal{S}}_{n} \) est sans point fixe si et seulement si aucun de ses cycles a une longueur de 1 dans sa décomposition en produits de cycles, ce qui revient à écrire \( s \in {\mathcal{P}}_{n}\left( N\right) \) avec \( N = \{ k \in \mathbb{N}, k \geq 2\} \) . D’après la question précédente, la série génératrice exponentielle des permutations sans point fixe est donc \( \Phi \left( z\right) = \exp \left( {{C}_{N}\left( z\right) }\right) - 1 \) avec \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}{z}^{k}/k \) . Or lorsque \( z \in \rbrack - 1,1\lbrack \) , la forme du développement en série entière de \( \log \left( {1 - z}\right) \) entraîne \( {C}_{N}\left( z\right) = - z - \log \left( {1 - z}\right) \) donc

> 2/a) A permutation \( s \in {\mathcal{S}}_{n} \) is fixed-point-free if and only if none of its cycles have a length of 1 in its cycle decomposition, which amounts to writing \( s \in {\mathcal{P}}_{n}\left( N\right) \) with \( N = \{ k \in \mathbb{N}, k \geq 2\} \) . According to the previous question, the exponential generating function for fixed-point-free permutations is therefore \( \Phi \left( z\right) = \exp \left( {{C}_{N}\left( z\right) }\right) - 1 \) with \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{k = 2}}^{{+\infty }}{z}^{k}/k \) . However, when \( z \in \rbrack - 1,1\lbrack \) , the form of the power series expansion of \( \log \left( {1 - z}\right) \) implies \( {C}_{N}\left( z\right) = - z - \log \left( {1 - z}\right) \) so

\[
\forall z \in  \rbrack  - 1,1\lbrack \;\Phi \left( z\right)  = \frac{\exp \left( {-z}\right) }{1 - z} - 1 = \left( {\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{k}}{k!}{z}^{k}}\right) \left( {\mathop{\sum }\limits_{{\ell  = 0}}^{{+\infty }}{z}^{\ell }}\right)  - 1 = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( -1\right) }^{k}}{k!}}\right) {z}^{n}.
\]

Le nombre \( {D}_{n} \) de permutations sans point fixes dans \( {\mathcal{S}}_{n} \) vérifie donc \( {D}_{n}/n! = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}/k! \) . Comme \( 1/e = \exp \left( {-1}\right) = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{\left( -1\right) }^{k}/k! \) , on a bien \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{D}_{n}/n! = 1/e \) , ce qu’il fallait démontrer.

> The number \( {D}_{n} \) of fixed-point-free permutations in \( {\mathcal{S}}_{n} \) therefore satisfies \( {D}_{n}/n! = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}/k! \) . Since \( 1/e = \exp \left( {-1}\right) = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{\left( -1\right) }^{k}/k! \) , we indeed have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{D}_{n}/n! = 1/e \) , which was to be demonstrated.

b) Le cas des permutations n'ayant que des cycles de longueur paire correspond au cas où \( N = \{ {2k} \mid k \in \mathbb{N}\} \) , donc

> b) The case of permutations having only cycles of even length corresponds to the case where \( N = \{ {2k} \mid k \in \mathbb{N}\} \) , so

\[
\forall z \in  \rbrack  - 1,1\left\lbrack  {\;{C}_{N}\left( z\right)  = \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\frac{{z}^{2k}}{2k} = \frac{1}{2}\log \left( \frac{1}{1 - {z}^{2}}\right) .}\right.
\]

On en déduit que la série génératrice expoentielle des permutations correspondantes vérifie, pour tout \( z \in \rbrack - 1,1\lbrack \) ,

> We deduce that the exponential generating function for the corresponding permutations satisfies, for all \( z \in \rbrack - 1,1\lbrack \) ,

\[
\Phi \left( z\right)  = {\left( \frac{1}{1 - {z}^{2}}\right) }^{1/2} - 1 = \mathop{\sum }\limits_{{m = 1}}^{{+\infty }}{a}_{m}{z}^{2m},\;\text{ avec }\;{a}_{m} = \frac{1}{m!} \cdot  \frac{1}{2} \cdot  \frac{3}{2}\cdots \frac{{2m} - 1}{2} = \frac{\left( {2m}\right) !}{{2}^{2m}{\left( m!\right) }^{2}}.
\]

Ainsi, lorsque \( n \) est impair, il n’y a pas de permutation dans \( {\mathcal{S}}_{n} \) qui s’écrit comme produit de cycles de longueur paire, et lorsque \( n = {2m} \) est pair, il y en a \( n!{a}_{m} = {2}^{-{2m}}{\left( \left( 2m\right) !\right) }^{2}/{\left( m!\right) }^{2} \) . La probabilité qu’une permutation dans \( {\mathcal{S}}_{2m} \) ait tout ses cycles de longueur paire est égal à \( {a}_{m} \) , dont on calcule le comportement asymptotique avec la formule de Stirling

> Thus, when \( n \) is odd, there is no permutation in \( {\mathcal{S}}_{n} \) that can be written as a product of cycles of even length, and when \( n = {2m} \) is even, there are \( n!{a}_{m} = {2}^{-{2m}}{\left( \left( 2m\right) !\right) }^{2}/{\left( m!\right) }^{2} \) . The probability that a permutation in \( {\mathcal{S}}_{2m} \) has all its cycles of even length is equal to \( {a}_{m} \) , the asymptotic behavior of which is calculated using Stirling's formula.

\[
{a}_{m} \sim  \frac{1}{{2}^{2m}}\frac{\sqrt{4\pi m}{\left( 2m/e\right) }^{2m}}{{\left( \sqrt{2\pi m}{\left( m/e\right) }^{m}\right) }^{2}} = \frac{1}{\sqrt{\pi m}}.
\]

3/a) La continuité de \( {\varphi }_{m} \) par rapport à la variable complexe \( z \) sur \( {D}^{ * } \) est immédiate d’après la forme de \( {\varphi }_{m}\left( z\right) \) . Lorsque \( z \in {D}^{ * } \) , on peut écrire

> 3/a) The continuity of \( {\varphi }_{m} \) with respect to the complex variable \( z \) on \( {D}^{ * } \) is immediate from the form of \( {\varphi }_{m}\left( z\right) \) . When \( z \in {D}^{ * } \) , we can write

\[
{\varphi }_{m}\left( z\right)  = \frac{{e}^{-{H}_{m}}}{1 - z}\left( {{e}^{{\psi }_{m}\left( z\right) } - 1}\right) ,\;\text{ avec }\;{\psi }_{m}\left( z\right)  = {H}_{m} - \mathop{\sum }\limits_{{k = 1}}^{m}\frac{{z}^{k}}{k} = \mathop{\sum }\limits_{{k = 1}}^{m}\frac{1 - {z}^{k}}{k} = \left( {1 - z}\right) {\theta }_{m}\left( z\right)
\]

où

> where

\[
{\theta }_{m}\left( z\right)  = \mathop{\sum }\limits_{{k = 1}}^{m}\frac{1 + z + \cdots  + {z}^{k - 1}}{k}.
\]

La fonction \( {\theta }_{m}\left( z\right) \) est polynomiale, donc continue sur \( \mathbb{C} \) , en particulier, lorsque \( z \in {D}^{ * } \) tend vers 1 on a \( {\theta }_{m}\left( z\right) = {\theta }_{m}\left( 1\right) + o\left( 1\right) = m + o\left( 1\right) \) . Lorsque \( z \in {D}^{ * } \) converge vers 1 on peut donc écrire

> The function \( {\theta }_{m}\left( z\right) \) is polynomial, therefore continuous on \( \mathbb{C} \) ; in particular, when \( z \in {D}^{ * } \) tends to 1, we have \( {\theta }_{m}\left( z\right) = {\theta }_{m}\left( 1\right) + o\left( 1\right) = m + o\left( 1\right) \) . When \( z \in {D}^{ * } \) converges to 1, we can therefore write

\[
{\varphi }_{m}\left( z\right)  = \frac{{e}^{-{H}_{m}}}{1 - z}\left( {{e}^{\left( {1 - z}\right) \left( {m + o\left( 1\right) }\right) } - 1}\right)  = \frac{{e}^{-{H}_{m}}}{1 - z}\left( {\left( {1 - z}\right) \left( {m + o\left( 1\right) }\right)  + o\left( {1 - z}\right) }\right)  = {e}^{-{H}_{m}}m + o\left( 1\right) .
\]

En posant \( {\varphi }_{m}\left( 1\right) = {e}^{-{H}_{m}}m \) , on a donc prolongé par continuité \( {\varphi }_{m} \) sur \( D \) tout entier.

> By setting \( {\varphi }_{m}\left( 1\right) = {e}^{-{H}_{m}}m \) , we have thus extended \( {\varphi }_{m} \) by continuity to the entirety of \( D \) .

b) Les permutations avec cycles de longueur \( > m \) correspond au cas où \( N = \{ k \in \mathbb{N} \mid k > m\} \) , pour lequel \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{k > m}}{z}^{k}/k = - \log \left( {1 - z}\right) - \mathop{\sum }\limits_{{k = 1}}^{m}{z}^{k}/k \) pour \( z \in \rbrack - 1,1\lbrack \) . Donc la série génératrice exponentielle correspondante \( {\Phi }_{m}\left( z\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{p}_{n}\left( m\right) {z}^{n} \) vérifie

> b) Permutations with cycles of length \( > m \) correspond to the case where \( N = \{ k \in \mathbb{N} \mid k > m\} \) , for which \( {C}_{N}\left( z\right) = \mathop{\sum }\limits_{{k > m}}{z}^{k}/k = - \log \left( {1 - z}\right) - \mathop{\sum }\limits_{{k = 1}}^{m}{z}^{k}/k \) for \( z \in \rbrack - 1,1\lbrack \) . Thus, the corresponding exponential generating function \( {\Phi }_{m}\left( z\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{p}_{n}\left( m\right) {z}^{n} \) satisfies

\[
\forall z \in  \rbrack  - 1,1\left\lbrack  {\;{\Phi }_{m}\left( z\right)  = \exp \left( {{C}_{N}\left( z\right) }\right)  - 1 = \frac{{e}^{-z - {z}^{2}/2 - \cdots  - {z}^{m}/m}}{1 - z} - 1.}\right.
\]

(*)

> La fonction \( z \mapsto {e}^{-z - {z}^{2}/2 - \cdots - {z}^{m}/m}/\left( {1 - z}\right) \) est la somme d’une série entière de rayon de convergence \( \geq 1 \) , car c’est le produit des fonctions \( {e}^{-{z}^{k}/k} \) pour \( 1 \leq k \leq m \) et \( 1/\left( {1 - z}\right) \) qui sont toutes des sommes de séries entières de rayon de convergence \( \geq 1 \) . Ainsi l’identité (*), vraie sur \( \rbrack - 1,1\lbrack \) l’est aussi sur \( \{ z \in \mathbb{C}\left| \right| z \mid < 1\} \) d’après le principe des zéros isolés. Or pour toute série entière \( f\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) de rayon de convergence \( \geq 1 \) , on a l’identité classique

The function \( z \mapsto {e}^{-z - {z}^{2}/2 - \cdots - {z}^{m}/m}/\left( {1 - z}\right) \) is the sum of a power series with radius of convergence \( \geq 1 \) , because it is the product of the functions \( {e}^{-{z}^{k}/k} \) for \( 1 \leq k \leq m \) and \( 1/\left( {1 - z}\right) \) , which are all sums of power series with radius of convergence \( \geq 1 \) . Thus, the identity (*), true on \( \rbrack - 1,1\lbrack \) , is also true on \( \{ z \in \mathbb{C}\left| \right| z \mid < 1\} \) according to the identity theorem for holomorphic functions. However, for any power series \( f\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) with radius of convergence \( \geq 1 \) , we have the classical identity

\[
\forall \rho  \in  \rbrack 0,1\lbrack ,\forall n \in  \mathbb{N},\;{a}_{n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( {\rho {e}^{it}}\right) \frac{{e}^{-{int}}}{{\rho }^{n}}{dt}
\]

(**)

> que l'on démontre en écrivant

which is proven by writing

\[
\frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( {\rho {e}^{it}}\right) \frac{{e}^{-{int}}}{{\rho }^{n}}{dt} = \frac{1}{2\pi }{\int }_{0}^{2\pi }\left( {\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{a}_{k}{\rho }^{k - n}{e}^{i\left( {k - n}\right) t}}\right) {dt} = \frac{1}{2\pi }\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{\int }_{0}^{2\pi }{a}_{k}{\rho }^{k - n}{e}^{i\left( {k - n}\right) t}{dt}
\]

où l'intervertion des signes de sommation est possible car la série de fonction intégrée converge normalement, et en remarquant que \( {\int }_{0}^{2\pi }{e}^{i\left( {k - n}\right) t}{dt} = 0 \) si \( k \neq n, = {2\pi } \) si \( k = n \) . Or

> where the interchange of summation signs is possible because the integrated series of functions converges normally, and noting that \( {\int }_{0}^{2\pi }{e}^{i\left( {k - n}\right) t}{dt} = 0 \) if \( k \neq n, = {2\pi } \) if \( k = n \) . Now

\[
1 - {e}^{-{H}_{m}} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {{p}_{n}\left( m\right)  - {e}^{-{H}_{m}}}\right) {z}^{n} = 1 + {\Phi }_{m}\left( z\right)  - \frac{{e}^{-{H}_{m}}}{1 - z} = {\varphi }_{m}\left( z\right) ,
\]

les séries entières en présence ayant rayon de convergence \( \geq 1 \) , on a donc, compte tenu de l'identité (**) appliquée à cette série entière

> the power series in question having radius of convergence \( \geq 1 \) , we therefore have, taking into account identity (**) applied to this power series

\[
\forall \rho  \in  \rbrack 0,1\left\lbrack  {,\forall n \in  {\mathbb{N}}^{ * },\;{p}_{n}\left( m\right)  - {e}^{-{H}_{m}} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\varphi }_{m}\left( {\rho {e}^{it}}\right) \frac{{e}^{-{int}}}{{\rho }^{n}}{dt}.}\right.
\]

Notons \( I\left( \rho \right) \) cette dernière intégrale. La question précédente entraîne la continuité de la fonction intégrée sur \( \left( {\rho , t}\right) \in \rbrack 0,1\rbrack \times \left\lbrack {0,{2\pi }}\right\rbrack \) . Ainsi, \( I\left( 1\right) \) existe et le théorème de continuité sous le signe intégral entraîne que \( I \) est continue sur \( \rbrack 0,1\rbrack \) , en particulier en \( \rho = 1 \) . Comme \( I\left( \rho \right) /\left( {2\pi }\right) = \; {p}_{n}\left( m\right) - {e}^{-{H}_{m}} \) pour tout \( \rho \in \rbrack 0,1\lbrack \) , on en déduit le résultat demandé car

> Let us denote this last integral by \( I\left( \rho \right) \) . The previous question implies the continuity of the integrated function on \( \left( {\rho , t}\right) \in \rbrack 0,1\rbrack \times \left\lbrack {0,{2\pi }}\right\rbrack \) . Thus, \( I\left( 1\right) \) exists and the theorem of continuity under the integral sign implies that \( I \) is continuous on \( \rbrack 0,1\rbrack \) , in particular at \( \rho = 1 \) . Since \( I\left( \rho \right) /\left( {2\pi }\right) = \; {p}_{n}\left( m\right) - {e}^{-{H}_{m}} \) for all \( \rho \in \rbrack 0,1\lbrack \) , we deduce the requested result because

\[
{p}_{n}\left( m\right)  - {e}^{-{H}_{m}} = \mathop{\lim }\limits_{{\rho  \rightarrow  1,\rho  < 1}}\frac{I\left( \rho \right) }{2\pi } = \frac{I\left( 1\right) }{2\pi }.
\]

c) Lorsque \( n \rightarrow + \infty \) , il est classique que l’intégrale de la question précédente converge vers 0 (c'est le lemme de Lebesgue, voir le tome Analyse). La preuve du lemme de Lebesgue est facile lorsque la fonction intégré est de classe \( {\mathcal{C}}^{1} \) , en procédant par intégration par parties. Lorsque l'intégrande est uniquement supposée continue, on le démontre en approchant la fonction continue \( t \mapsto {\varphi }_{m}\left( {e}^{it}\right) \) par une fonction en escalier, sur \( \left\lbrack {0,{2\pi }}\right\rbrack \) (cette approche est décrite dans le tome Analyse). Ici, pour faciliter la preuve, on va procéder de manière hybride. Soit \( \varepsilon > 0 \) (et \( \varepsilon < \pi \) ). La forme de \( {\varphi }_{m} \) montre que \( f\left( t\right) = {\varphi }_{m}\left( {e}^{it}\right) \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {\varepsilon ,{2\pi } - \varepsilon }\right\rbrack \) , on pourra donc intégrer par parties sur cet intervalle. On écrit \( {p}_{n}\left( m\right) - {e}^{-{H}_{m}} = \left( {{A}_{n} + {B}_{n}}\right) /\left( {2\pi }\right) \) avec

> c) When \( n \rightarrow + \infty \) , it is standard that the integral from the previous question converges to 0 (this is the Lebesgue lemma, see the Analysis volume). The proof of the Lebesgue lemma is easy when the integrated function is of class \( {\mathcal{C}}^{1} \) , by proceeding via integration by parts. When the integrand is only assumed to be continuous, it is demonstrated by approximating the continuous function \( t \mapsto {\varphi }_{m}\left( {e}^{it}\right) \) with a step function on \( \left\lbrack {0,{2\pi }}\right\rbrack \) (this approach is described in the Analysis volume). Here, to facilitate the proof, we will proceed in a hybrid manner. Let \( \varepsilon > 0 \) (and \( \varepsilon < \pi \) ). The form of \( {\varphi }_{m} \) shows that \( f\left( t\right) = {\varphi }_{m}\left( {e}^{it}\right) \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {\varepsilon ,{2\pi } - \varepsilon }\right\rbrack \) , so we can integrate by parts on this interval. We write \( {p}_{n}\left( m\right) - {e}^{-{H}_{m}} = \left( {{A}_{n} + {B}_{n}}\right) /\left( {2\pi }\right) \) with

\[
{A}_{n} = {\int }_{0}^{\varepsilon }f\left( t\right) {e}^{-{int}}{dt} + {\int }_{{2\pi } - \varepsilon }^{2\pi }f\left( t\right) {e}^{-{int}}{dt}\;\text{ et }\;{B}_{n} = {\int }_{\varepsilon }^{{2\pi } - \varepsilon }f\left( t\right) {e}^{-{int}}{dt}.
\]

Une intégration par partie permet d'écrire

> An integration by parts allows us to write

\[
{B}_{n} = {\left\lbrack  -f\left( t\right) \frac{{e}^{-{int}}}{in}\right\rbrack  }_{\varepsilon }^{{2\pi } - \varepsilon } + \frac{1}{in}{\int }_{\varepsilon }^{{2\pi } - \varepsilon }{f}^{\prime }\left( t\right) {e}^{-{int}}{dt}.
\]

On a donc

> We therefore have

\[
\left| {A}_{n}\right|  \leq  {2\varepsilon }\mathop{\sup }\limits_{{t \in  \left\lbrack  {0,{2\pi }}\right\rbrack  }}\left| {f\left( t\right) }\right| \;\text{ et }\;\left| {B}_{n}\right|  \leq  \frac{2}{n}\mathop{\sup }\limits_{{t \in  \left\lbrack  {0,{2\pi }}\right\rbrack  }}\left| {f\left( t\right) }\right|  + \frac{2\pi }{n}\mathop{\sup }\limits_{{t \in  \left\lbrack  {\varepsilon ,{2\pi } - \varepsilon }\right\rbrack  }}\left| {{f}^{\prime }\left( t\right) }\right| .
\]

On en déduit qu’il existe \( {N}_{0} \in \mathbb{N} \) tel que pour tout \( n > {N}_{0} \) , on ait \( \left| {B}_{n}\right| < \varepsilon \) . Donc lorsque \( n > {N}_{0} \) , on a \( \left| {{p}_{n}\left( m\right) - {e}^{-{H}_{m}}}\right| < {2\varepsilon }\mathop{\sup }\limits_{{t \in \left\lbrack {0,{2\pi }}\right\rbrack }}\left| {f\left( t\right) }\right| /\left( {2\pi }\right) + \varepsilon /\left( {2\pi }\right) \) , d’où le résultat.

> We deduce that there exists \( {N}_{0} \in \mathbb{N} \) such that for all \( n > {N}_{0} \) , we have \( \left| {B}_{n}\right| < \varepsilon \) . Thus when \( n > {N}_{0} \) , we have \( \left| {{p}_{n}\left( m\right) - {e}^{-{H}_{m}}}\right| < {2\varepsilon }\mathop{\sup }\limits_{{t \in \left\lbrack {0,{2\pi }}\right\rbrack }}\left| {f\left( t\right) }\right| /\left( {2\pi }\right) + \varepsilon /\left( {2\pi }\right) \) , hence the result.

Remarque. On a ainsi retrouvé dans la question 2/a) le résultat de l'exercice 8 page 312. - Le résultat de la question 3/c) est un cas particulier d'un théorème plus général, qui exprime que sous certaines conditions (dont la formulation dépasse le cadre du programme des classes préparatoires) le comportement asymptotique du \( n \) -ième coefficient d’une série entière est dicté par le comportement de cette dernière en ses singularités les plus proches de 0 (ici en \( z = 1 \) ). Dans notre cas, l’équivalent \( {\Phi }_{m}\left( z\right) \sim {e}^{-{H}_{m}}/\left( {1 - z}\right) \) entraîne que le \( n \) -ième coefficient de \( {\Phi }_{m}\left( z\right) \) est équivalent à celui de \( {e}^{-{H}_{m}}/\left( {1 - z}\right) \) .

> Remark. We have thus recovered in question 2/a) the result of exercise 8 on page 312. - The result of question 3/c) is a special case of a more general theorem, which states that under certain conditions (the formulation of which is beyond the scope of the preparatory classes curriculum) the asymptotic behavior of the \( n \)-th coefficient of a power series is dictated by the behavior of the latter at its singularities closest to 0 (here at \( z = 1 \)). In our case, the equivalent \( {\Phi }_{m}\left( z\right) \sim {e}^{-{H}_{m}}/\left( {1 - z}\right) \) implies that the \( n \)-th coefficient of \( {\Phi }_{m}\left( z\right) \) is equivalent to that of \( {e}^{-{H}_{m}}/\left( {1 - z}\right) \).

- La fonction \( f\left( t\right)  = {\varphi }_{m}\left( {e}^{it}\right) \) de la partie \( 3/ \) est aussi de classe \( {\mathcal{C}}^{1} \) (elle est même \( {\mathcal{C}}^{\infty } \) ) et nous aurions pu procéder plus rapidement pour démontrer la convergence vers 0 de l'intégrale de 3/b) si nous avions utilisé cette propriété (en intégrant par parties), mais la preuve de la regularité \( {\mathcal{C}}^{1} \) de \( f \) est assez pénible avec les outils dont nous disposons.

> - The function \( f\left( t\right)  = {\varphi }_{m}\left( {e}^{it}\right) \) of part \( 3/ \) is also of class \( {\mathcal{C}}^{1} \) (it is even \( {\mathcal{C}}^{\infty } \)) and we could have proceeded more quickly to demonstrate the convergence to 0 of the integral in 3/b) if we had used this property (by integrating by parts), but the proof of the \( {\mathcal{C}}^{1} \) regularity of \( f \) is quite tedious with the tools at our disposal.

Problem 4 (Problem 2 M CNOLEME DU SCRUTIN). Pour \( \left( {m, n}\right) \in {\mathbb{N}}^{2} \) tels que \( m \leq n \) et \( \left( {a, b}\right) \in {\mathbb{Z}}^{2} \) , on appelle chemin de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) toute suite de la forme \( {\left( k,{c}_{k}\right) }_{m \leq k \leq n} \) , telle que \( {c}_{m} = a \) , \( {c}_{n} = b \) , et \( {c}_{k + 1} - {c}_{k} \in \{ - 1,1\} \) pour \( m \leq k < n \) . On dit que le chemin passe par 0 s’il existe \( k \) tel que \( {c}_{k} = 0 \) . On représente graphiquement un chemin par une ligne brisée qui relie les points \( \left( {k,{c}_{k}}\right) \) pour les valeurs consécutives de \( k \) .

> Problem 4 (Ballot Problem). For \( \left( {m, n}\right) \in {\mathbb{N}}^{2} \) such that \( m \leq n \) and \( \left( {a, b}\right) \in {\mathbb{Z}}^{2} \), a path from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) is defined as any sequence of the form \( {\left( k,{c}_{k}\right) }_{m \leq k \leq n} \), such that \( {c}_{m} = a \), \( {c}_{n} = b \), and \( {c}_{k + 1} - {c}_{k} \in \{ - 1,1\} \) for \( m \leq k < n \). A path is said to pass through 0 if there exists \( k \) such that \( {c}_{k} = 0 \). A path is represented graphically by a broken line connecting the points \( \left( {k,{c}_{k}}\right) \) for consecutive values of \( k \).

1/a) Soit \( \left( {m, n}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}, m < n \) , et \( \left( {a, b}\right) \in {\mathbb{Z}}^{2} \) . Montrer que le nombre de chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) ne dépend que de \( \Delta = n - m \) et \( \delta = b - a \) , et calculer le nombre \( N\left( {\Delta ,\delta }\right) \) correspondant.

> 1/a) Let \( \left( {m, n}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}, m < n \) and \( \left( {a, b}\right) \in {\mathbb{Z}}^{2} \). Show that the number of paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) depends only on \( \Delta = n - m \) and \( \delta = b - a \), and calculate the corresponding number \( N\left( {\Delta ,\delta }\right) \).

b) (Principe de reflexion). On suppose \( \left( {a, b}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) . En s’appuyant sur une réprésenta-tion graphique, montrer que le nombre de chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) passant par 0, est égal au nombre total de chemins de \( \left( {m, - a}\right) \) à \( \left( {n, b}\right) \) . En déduire le nombre de chemins correspondants.

> b) (Reflection principle). Assume \( \left( {a, b}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \). Using a graphical representation, show that the number of paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) passing through 0 is equal to the total number of paths from \( \left( {m, - a}\right) \) to \( \left( {n, b}\right) \). Deduce the corresponding number of paths.

2/ Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une liste de variable aléatoires indépendantes, suivant toutes une loi de Rademacher \( P\left( {{X}_{n} = 1}\right) = 1/2, P\left( {{X}_{n} = - 1}\right) = 1/2 \) . On définit la suite \( {\left( {S}_{n}\right) }_{n \in \mathbb{N}} \) par \( {S}_{0} = 0 \) et \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) pour \( n \in {\mathbb{N}}^{ * } \) . On peut associer la suite \( {\left( {S}_{k}\right) }_{0 \leq k \leq n} \) au chemin \( {\left( k,{S}_{k}\right) }_{0 \leq k \leq n}. \)

> 2/ Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a list of independent random variables, all following a Rademacher distribution \( P\left( {{X}_{n} = 1}\right) = 1/2, P\left( {{X}_{n} = - 1}\right) = 1/2 \). We define the sequence \( {\left( {S}_{n}\right) }_{n \in \mathbb{N}} \) by \( {S}_{0} = 0 \) and \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) for \( n \in {\mathbb{N}}^{ * } \). We can associate the sequence \( {\left( {S}_{k}\right) }_{0 \leq k \leq n} \) with the path \( {\left( k,{S}_{k}\right) }_{0 \leq k \leq n}. \)

a) (Problème du scrutin). Soit \( \left( {b, n}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \) . Montrer que la probabilité que \( {S}_{n} = b \) , sachant que \( {S}_{k} \) reste toujours \( > 0 \) pour \( k < n \) vérifie

> a) (Ballot problem). Let \( \left( {b, n}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2} \). Show that the probability that \( {S}_{n} = b \), given that \( {S}_{k} \) always remains \( > 0 \) for \( k < n \), satisfies

\[
P\left( {{S}_{1} > 0,\ldots ,{S}_{n - 1} > 0,{S}_{n} = b}\right)  = \frac{b}{n}P\left( {{S}_{n} = b}\right) .
\]

b) Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer que

> b) Let \( n \in {\mathbb{N}}^{ * } \). Show that

\[
P\left( {{S}_{1} \neq  0,{S}_{2} \neq  0,\ldots ,{S}_{2n} \neq  0}\right)  = P\left( {{S}_{2n} = 0}\right) .
\]

c) Montrer que presque surement, il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( {S}_{2n} = 0 \) .

> c) Show that almost surely, there exists \( n \in {\mathbb{N}}^{ * } \) such that \( {S}_{2n} = 0 \).

d) On définit \( T = \min \left\{ {{2n}, n \in {\mathbb{N}}^{ * } \mid {S}_{2n} = 0}\right\} \) . Montrer que \( T \) n’admet pas d’espérance.

> d) We define \( T = \min \left\{ {{2n}, n \in {\mathbb{N}}^{ * } \mid {S}_{2n} = 0}\right\} \). Show that \( T \) does not have an expectation.

Solution. 1/a Soit \( c = \left( {k,{c}_{k}}\right) \) un chemin de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) . Une récurrence immédiate sur \( k \) montre que pour tout \( k \in \{ m,\ldots , n\} ,{c}_{k} - a \) et \( k - m \) ont même parité. En particulier \( \Delta = n - m \) et \( \delta = b - a \) ont même parité. Réciproquement, si ces conditions sont vérifiées, on peut construire autant de chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) , que de choix de \( \alpha \) indices \( k \) parmi \( \{ m,\ldots , n - 1\} \) tels que \( {c}_{k + 1} - {c}_{k} = 1 \) , et \( \beta \) indices tels que \( {c}_{k + 1} - {c}_{k} = - 1 \) , avec \( \alpha - \beta = \delta \) et \( \alpha + \beta = \Delta \) , c’est-à-dire \( \alpha = \left( {\Delta + \delta }\right) /2,\beta = \left( {\Delta - \delta }\right) /2 \) , donc un total de \( \left( \begin{matrix} \Delta \\ \left( {\Delta + \delta }\right) /2 \end{matrix}\right) \) chemins (avec \( \left( \begin{matrix} \Delta \\ \gamma \end{matrix}\right) = 0 \) si \( \gamma < 0 \) ou \( \gamma > \Delta \) ). En résumé, le nombre de chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) est égal à \( N\left( {n - m, b - a}\right) \) , où

> Solution. 1/a Let \( c = \left( {k,{c}_{k}}\right) \) be a path from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \). An immediate induction on \( k \) shows that for all \( k \in \{ m,\ldots , n\} ,{c}_{k} - a \) and \( k - m \) have the same parity. In particular, \( \Delta = n - m \) and \( \delta = b - a \) have the same parity. Conversely, if these conditions are met, we can construct as many paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) as there are choices of \( \alpha \) indices \( k \) among \( \{ m,\ldots , n - 1\} \) such that \( {c}_{k + 1} - {c}_{k} = 1 \), and \( \beta \) indices such that \( {c}_{k + 1} - {c}_{k} = - 1 \), with \( \alpha - \beta = \delta \) and \( \alpha + \beta = \Delta \), that is to say \( \alpha = \left( {\Delta + \delta }\right) /2,\beta = \left( {\Delta - \delta }\right) /2 \), thus a total of \( \left( \begin{matrix} \Delta \\ \left( {\Delta + \delta }\right) /2 \end{matrix}\right) \) paths (with \( \left( \begin{matrix} \Delta \\ \gamma \end{matrix}\right) = 0 \) if \( \gamma < 0 \) or \( \gamma > \Delta \)). In summary, the number of paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) is equal to \( N\left( {n - m, b - a}\right) \), where

\[
N\left( {\Delta ,\delta }\right)  = \left( \begin{matrix} \Delta \\  \left( {\Delta  + \delta }\right) /2 \end{matrix}\right) \text{ si }\Delta  - \delta \text{ est pair, }\;N\left( {\Delta ,\delta }\right)  = 0\;\text{ sinon. }
\]

b) Pour tout chemin \( c \) de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) passant par zéro, on considère le plus petit entier \( k > m \) tel que \( {c}_{k} = 0 \) , et on construit le chemin \( {c}^{\prime } \) dont la représentation jusqu’à l’abscisse \( k \) est la symétrique de celle de \( c \) par rapport à l’axes des abscisses, puis égal à \( c \) après cette abscisse. Comme on le voit sur la figure ci-contre, il est facile de vérifier qu'on obtient ainsi une bjiection de l’ensemble des chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) passant par zéro, vers celui des chemins de \( \left( {m, - a}\right) \) vers \( \left( {n, b}\right) \) . On en déduit que le nombre de chemins de \( \left( {m, a}\right) \) à \( \left( {n, b}\right) \) passant par zéro est égal à \( N\left( {n - m, b + a}\right) \) .

> b) For any path \( c \) from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) passing through zero, we consider the smallest integer \( k > m \) such that \( {c}_{k} = 0 \), and we construct the path \( {c}^{\prime } \) whose representation up to the abscissa \( k \) is the reflection of that of \( c \) with respect to the x-axis, and then equal to \( c \) after this abscissa. As seen in the figure opposite, it is easy to verify that we thus obtain a bijection from the set of paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) passing through zero to that of paths from \( \left( {m, - a}\right) \) to \( \left( {n, b}\right) \). We deduce that the number of paths from \( \left( {m, a}\right) \) to \( \left( {n, b}\right) \) passing through zero is equal to \( N\left( {n - m, b + a}\right) \).

2/a) Si \( n - b \) est impair, toute les probabilités sont nulles donc la relation est vraie. Supposons maintenant \( n \) et \( b \) de même parité. Il y a autant de valeurs de \( {\left( {X}_{k}\right) }_{1 \leq k \leq n} \) vérifiant \( {S}_{n} = b \) que de chemins de \( \left( {0,0}\right) \) à \( \left( {n, b}\right) \) , donc comme nous sommes ici dans le cas équiprobable, on a \( P\left( {{S}_{n} = b}\right) = {2}^{-n}N\left( {n, b}\right) \) . Comme \( {S}_{1} = {X}_{1} \) , pour avoir \( {S}_{1} > 0 \) on doit avoir \( {S}_{1} = 1 \) . Ainsi, on a \( \left( {{S}_{1} > 0,\ldots ,{S}_{n - 1} > 0,{S}_{n} = b}\right) \) si et seulement si le chemin \( {\left( k,{S}_{k}\right) }_{1 \leq k \leq n} \) va de \( \left( {1,1}\right) \) à \( \left( {n, b}\right) \) , sans jamais passer par 0 . D'après la question 1/b), il y a \( {C}^{ * } = N\left( {n - 1, b - 1}\right) - N\left( {n - 1, b + 1}\right) \) chemins de cette forme. En notant \( \gamma = \left( {n + b}\right) /2 \) on trouve

> 2/a) If \( n - b \) is odd, all probabilities are zero, so the relation is true. Now assume \( n \) and \( b \) have the same parity. There are as many values of \( {\left( {X}_{k}\right) }_{1 \leq k \leq n} \) satisfying \( {S}_{n} = b \) as there are paths from \( \left( {0,0}\right) \) to \( \left( {n, b}\right) \), so since we are in the equiprobable case here, we have \( P\left( {{S}_{n} = b}\right) = {2}^{-n}N\left( {n, b}\right) \). Since \( {S}_{1} = {X}_{1} \), to have \( {S}_{1} > 0 \) we must have \( {S}_{1} = 1 \). Thus, we have \( \left( {{S}_{1} > 0,\ldots ,{S}_{n - 1} > 0,{S}_{n} = b}\right) \) if and only if the path \( {\left( k,{S}_{k}\right) }_{1 \leq k \leq n} \) goes from \( \left( {1,1}\right) \) to \( \left( {n, b}\right) \) without ever passing through 0. According to question 1/b), there are \( {C}^{ * } = N\left( {n - 1, b - 1}\right) - N\left( {n - 1, b + 1}\right) \) paths of this form. By noting \( \gamma = \left( {n + b}\right) /2 \) we find

\[
{C}^{ * } = \left( \begin{matrix} n - 1 \\  \gamma  - 1 \end{matrix}\right)  - \left( \begin{matrix} n - 1 \\  \gamma  \end{matrix}\right)  = \frac{\gamma }{n}\left( \begin{array}{l} n \\  \gamma  \end{array}\right)  - \frac{n - \gamma }{n}\left( \begin{array}{l} n \\  \gamma  \end{array}\right)  = \frac{{2\gamma } - n}{n}\left( \begin{array}{l} n \\  \gamma  \end{array}\right)  = \frac{b}{n}N\left( {n, b}\right) .
\]

(*)

![bo_d7fjffs91nqc73erehlg_374_410_193_650_347_0.jpg](images/gourdon_algebra_probabilities_fr_en_016_bod7fjffs91nqc73erehlg3744101936503470.jpg)

FIGURE 5. Représentation graphique d’un chemin \( c \) de \( \left( {2,1}\right) \) à \( \left( {{10},3}\right) \) passant par 0, et du chemin \( {c}^{\prime } \) de \( \left( {2, - 1}\right) \) à \( \left( {{10},3}\right) \) obtenu par reflexion de la première partie de \( c \) (en trait fin).

> FIGURE 5. Graphical representation of a path \( c \) from \( \left( {2,1}\right) \) to \( \left( {{10},3}\right) \) passing through 0, and of the path \( {c}^{\prime } \) from \( \left( {2, - 1}\right) \) to \( \left( {{10},3}\right) \) obtained by reflection of the first part of \( c \) (in thin line).

On en déduit \( P\left( {{S}_{1} > 0,\ldots ,{S}_{n - 1} > 0,{S}_{n} = b}\right) = {2}^{-n}\left( {b/n}\right) N\left( {n, b}\right) = \left( {b/n}\right) P\left( {{S}_{n} = b}\right) \) .

> We deduce \( P\left( {{S}_{1} > 0,\ldots ,{S}_{n - 1} > 0,{S}_{n} = b}\right) = {2}^{-n}\left( {b/n}\right) N\left( {n, b}\right) = \left( {b/n}\right) P\left( {{S}_{n} = b}\right) \).

b) On a \( \left\{ {{S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0}\right\} = \left\{ {{S}_{1} > 0,\ldots ,{S}_{2n} > 0}\right\} \cup \left\{ {{S}_{1} < 0,\ldots ,{S}_{2n} < 0}\right\} \) , ces deux ensembles étant disjoints, donc par symétrie on a

> b) We have \( \left\{ {{S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0}\right\} = \left\{ {{S}_{1} > 0,\ldots ,{S}_{2n} > 0}\right\} \cup \left\{ {{S}_{1} < 0,\ldots ,{S}_{2n} < 0}\right\} \) , these two sets being disjoint, so by symmetry we have

\[
P\left( {{S}_{1} \neq  0,\ldots ,{S}_{2n} \neq  0}\right)  = {2P}\left( {{S}_{1} > 0,\ldots ,{S}_{2n} > 0}\right) .
\]

\( \left( {* * }\right) \) .

> Or, d'après la question précédente, on a

However, according to the previous question, we have

\[
P\left( {{S}_{1} > 0,\ldots ,{S}_{2n} > 0}\right)  = \mathop{\sum }\limits_{{b > 0}}P\left( {{S}_{1} > 0,\ldots ,{S}_{{2n} - 1} > 0,{S}_{2n} = {2b}}\right)  = \mathop{\sum }\limits_{{b > 0}}{2}^{-{2n}}\frac{2b}{2n}N\left( {{2n},{2b}}\right) .
\]

Les égalités de (*) montrent que \( \frac{2b}{2n}N\left( {{2n},{2b}}\right) = \left( \begin{matrix} {2n} - 1 \\ n + b - 1 \end{matrix}\right) - \left( \begin{matrix} {2n} - 1 \\ n + b \end{matrix}\right) \) . Donc

> The equalities in (*) show that \( \frac{2b}{2n}N\left( {{2n},{2b}}\right) = \left( \begin{matrix} {2n} - 1 \\ n + b - 1 \end{matrix}\right) - \left( \begin{matrix} {2n} - 1 \\ n + b \end{matrix}\right) \) . Therefore

\[
P\left( {{S}_{1} > 0,\ldots ,{S}_{2n} > 0}\right)  = {2}^{-{2n}}\mathop{\sum }\limits_{{b > 0}}\left\lbrack  {\left( \begin{matrix} {2n} - 1 \\  n + b - 1 \end{matrix}\right)  - \left( \begin{matrix} {2n} - 1 \\  n + b \end{matrix}\right) }\right\rbrack   = {2}^{-{2n}}\left( \begin{matrix} {2n} - 1 \\  n \end{matrix}\right) .
\]

Il y a autant de valeurs de \( {\left( {X}_{k}\right) }_{1 \leq k \leq {2n}} \) vérifiant \( {S}_{2n} = 0 \) que de chemins allant de \( \left( {0,0}\right) \) à \( \left( {{2n},0}\right) \) , donc

> There are as many values of \( {\left( {X}_{k}\right) }_{1 \leq k \leq {2n}} \) satisfying \( {S}_{2n} = 0 \) as there are paths from \( \left( {0,0}\right) \) to \( \left( {{2n},0}\right) \) , so

\[
P\left( {{S}_{2n} = 0}\right)  = {2}^{-{2n}}N\left( {{2n},0}\right)  = {2}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right)  = {2}^{-{2n}}\frac{2n}{n}\left( \begin{matrix} {2n} - 1 \\  n - 1 \end{matrix}\right)  = {2}^{1 - {2n}}\left( \begin{matrix} {2n} - 1 \\  n \end{matrix}\right) .
\]

On en déduit le résultat avec (**).

> We deduce the result from (**).

c) Notons \( {A}_{n} = \left\{ {{S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0}\right\} \) . La formule de Stirling appliquée à la question précédente entraîne

> c) Let us denote \( {A}_{n} = \left\{ {{S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0}\right\} \) . Stirling's formula applied to the previous question implies

\[
P\left( {A}_{n}\right)  = {2}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right)  = {2}^{-{2n}}\frac{\left( {2n}\right) !}{{\left( n!\right) }^{2}} \sim  {2}^{-{2n}}\frac{\sqrt{4\pi n}{\left( 2n/e\right) }^{2n}}{{\left( \sqrt{2\pi n}{\left( n/e\right) }^{n}\right) }^{2}} = \frac{1}{\sqrt{\pi n}}.
\]

La suite \( \left( {A}_{n}\right) \) est décroissante, donc \( P\left( {{ \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) . Donc \( A = { \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n} \) est négligeable, et comme \( A \) est l’événement \( {S}_{2n} \neq 0 \) pour tout \( n \in \mathbb{N} \) , on en déduit que presque surement, il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( {S}_{2n} = 0 \) .

> The sequence \( \left( {A}_{n}\right) \) is decreasing, so \( P\left( {{ \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) . Thus \( A = { \cap }_{n \in {\mathbb{N}}^{ * }}{A}_{n} \) is negligible, and since \( A \) is the event \( {S}_{2n} \neq 0 \) for all \( n \in \mathbb{N} \) , we deduce that almost surely, there exists \( n \in {\mathbb{N}}^{ * } \) such that \( {S}_{2n} = 0 \) .

d) On a \( T > {2n} \) si et seulement si \( {S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0 \) . Donc d’après 2/b), on a \( P\left( {T > {2n}}\right) = \; P\left( {{S}_{2n} = 0}\right) \sim {\left( \pi n\right) }^{-1/2} \) . Donc la série \( \mathop{\sum }\limits_{n}P\left( {T > n}\right) \) diverge, donc \( T \) n’admet pas d’espèrance d'après la proposition 7 page 338.

> d) We have \( T > {2n} \) if and only if \( {S}_{1} \neq 0,\ldots ,{S}_{2n} \neq 0 \) . Thus, according to 2/b), we have \( P\left( {T > {2n}}\right) = \; P\left( {{S}_{2n} = 0}\right) \sim {\left( \pi n\right) }^{-1/2} \) . Therefore the series \( \mathop{\sum }\limits_{n}P\left( {T > n}\right) \) diverges, so \( T \) does not have an expectation according to proposition 7 on page 338.

Remarque. Une conséquence du résultat de la question 2/a), est que si un scrutin entre deux candidats \( A \) et \( B \) se termine avec \( a \) voix pour le candidat \( A \) , et \( b \) voix pour le candidat \( B \) , avec \( a > b \) , alors la probabilité que le nombre de voix pour \( A \) soit toujours strictement supérieur au nombre de voix pour \( B \) pendant le dépouillement du scrutin, est égale à \( \left( {a - b}\right) /\left( {a + b}\right) \) (d’où la dénomination problème du scrutin).

> Remark. A consequence of the result in question 2/a) is that if a ballot between two candidates \( A \) and \( B \) ends with \( a \) votes for candidate \( A \) and \( b \) votes for candidate \( B \) , with \( a > b \) , then the probability that the number of votes for \( A \) is always strictly greater than the number of votes for \( B \) during the counting of the ballot is equal to \( \left( {a - b}\right) /\left( {a + b}\right) \) (hence the name ballot problem).

Problems 5 (MODES DE CONVERGENCE). Soit \( \left( {X}_{n}\right) \) une suite de variables aléatoires discrètes réelles sur \( \Omega \) , et \( X : \Omega \rightarrow \mathbb{R} \) une variable aléatoire discrète.

> Problems 5 (MODES OF CONVERGENCE). Let \( \left( {X}_{n}\right) \) be a sequence of real discrete random variables on \( \Omega \), and \( X : \Omega \rightarrow \mathbb{R} \) be a discrete random variable.

(Convergence en probabilité). On dit que \( \left( {X}_{n}\right) \) converge en probabilité vers \( X \) si pour tout \( \varepsilon > 0,\mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {{X}_{n} - X}\right| \geq \varepsilon }\right) = 0. \)

> (Convergence in probability). We say that \( \left( {X}_{n}\right) \) converges in probability to \( X \) if for all \( \varepsilon > 0,\mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {\left| {{X}_{n} - X}\right| \geq \varepsilon }\right) = 0. \)

1/ (Convergence presque sure). On dit que \( \left( {X}_{n}\right) \) converge presque surement vers \( X \) s’il existe un événement \( A \) presque sûr tel que \( \left( {X}_{n}\right) \) converge simplement vers \( X \) sur \( A \) .

> 1/ (Almost sure convergence). We say that \( \left( {X}_{n}\right) \) converges almost surely to \( X \) if there exists an almost sure event \( A \) such that \( \left( {X}_{n}\right) \) converges pointwise to \( X \) on \( A \).

a) Si \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) converge presque surement vers \( X \) , montrer que \( \left( {X}_{n}\right) \) converge en proba-bilité vers \( X \)

> a) If \( {\left( {X}_{n}\right) }_{n \in \mathbb{N}} \) converges almost surely to \( X \), show that \( \left( {X}_{n}\right) \) converges in probability to \( X \).

b) Si pour tout \( \varepsilon > 0 \) , la série \( \mathop{\sum }\limits_{n}P\left( {\left| {{X}_{n} - X}\right| > \varepsilon }\right) \) converge, montrer que \( \left( {X}_{n}\right) \) converge presque surement vers \( X \) .

> b) If for all \( \varepsilon > 0 \), the series \( \mathop{\sum }\limits_{n}P\left( {\left| {{X}_{n} - X}\right| > \varepsilon }\right) \) converges, show that \( \left( {X}_{n}\right) \) converges almost surely to \( X \).

c) \( \mathrm{{Si}}\left( {X}_{n}\right) \) converge en probabilité vers \( X \) , montrer qu’il existe une sous-suite de \( \left( {X}_{n}\right) \) qui converge presque surement vers \( X \) .

> c) \( \mathrm{{Si}}\left( {X}_{n}\right) \) converges in probability to \( X \), show that there exists a subsequence of \( \left( {X}_{n}\right) \) that converges almost surely to \( X \).

d) Montrer que la réciproque de a) est fausse (Indication : choisir les \( {X}_{n} \) indépendants et suivant une loi de Bernoulli de paramètre \( {p}_{n} \) , avec \( {p}_{n} \rightarrow 0 \) et \( \mathop{\sum }\limits_{n}{p}_{n} = + \infty \) ).

> d) Show that the converse of a) is false (Hint: choose \( {X}_{n} \) independent and following a Bernoulli distribution with parameter \( {p}_{n} \), with \( {p}_{n} \rightarrow 0 \) and \( \mathop{\sum }\limits_{n}{p}_{n} = + \infty \)).

2/ (Convergence \( {\mathcal{L}}^{1} \) ). Si les \( {X}_{n} \) et \( X \) admettent une espérance, on dit que \( \left( {X}_{n}\right) \) converge dans \( {\mathcal{L}}^{1} \) vers \( X \) si la suite \( {\left( E\left( \left| {X}_{n} - X\right| \right) \right) }_{n} \) converge vers 0 . Montrer que la convergence dans \( {\mathcal{L}}^{1} \) entraîne la convergence en probabilité, mais que la réciproque est fausse.

> 2/ (Convergence \( {\mathcal{L}}^{1} \)). If \( {X}_{n} \) and \( X \) have an expectation, we say that \( \left( {X}_{n}\right) \) converges in \( {\mathcal{L}}^{1} \) to \( X \) if the sequence \( {\left( E\left( \left| {X}_{n} - X\right| \right) \right) }_{n} \) converges to 0. Show that convergence in \( {\mathcal{L}}^{1} \) implies convergence in probability, but that the converse is false.

3/ (Convergence en loi). On suppose ici que les \( {X}_{n} \) et \( X \) sont à valeurs dans \( \mathbb{Z} \) . On dit que \( \left( {X}_{n}\right) \) converge en loi vers \( X \) si pour tout \( k \in \mathbb{Z},\mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{n} = k}\right) = P\left( {X = k}\right) \) . Montrer que si \( \left( {X}_{n}\right) \) converge en probabilité vers \( X \) , alors \( \left( {X}_{n}\right) \) converge en loi vers \( X \) , mais que la réciproque est fausse.

> 3/ (Convergence in distribution). We assume here that \( {X}_{n} \) and \( X \) take values in \( \mathbb{Z} \). We say that \( \left( {X}_{n}\right) \) converges in distribution to \( X \) if for all \( k \in \mathbb{Z},\mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{X}_{n} = k}\right) = P\left( {X = k}\right) \). Show that if \( \left( {X}_{n}\right) \) converges in probability to \( X \), then \( \left( {X}_{n}\right) \) converges in distribution to \( X \), but that the converse is false.

Solution. 1/ a) Par hypothèse, il existe un événement presque sûr \( A \) tel que \( \left( {X}_{n}\right) \) converge simplement vers \( X \) sur \( A \) . Soit \( \varepsilon > 0 \) . Pour tout \( n \in \mathbb{N} \) , on note \( {A}_{n}\left( \varepsilon \right) = { \cap }_{m \geq n}\left\{ {\left| {{X}_{m} - X}\right| < \varepsilon }\right\} \) . La convergence simple de \( \left( {X}_{n}\right) \) vers \( X \) sur \( A \) entraîne \( A \subset B = { \cup }_{n \in \mathbb{N}}{A}_{n}\left( \varepsilon \right) \) . Comme \( {\left( {A}_{n}\left( \varepsilon \right) \right) }_{n} \) est une suite croissante, on en déduit li \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{A}_{n}\left( \varepsilon \right) }\right) = P\left( B\right) = 1 \) . Donc pour tout \( \delta > 0 \) , il existe \( N \in \mathbb{N} \) tel que \( P\left( {{A}_{n}\left( \varepsilon \right) }\right) \geq 1 - \delta \) pour \( n \geq N \) . On en déduit

> Solution. 1/ a) By hypothesis, there exists an almost sure event \( A \) such that \( \left( {X}_{n}\right) \) converges pointwise to \( X \) on \( A \). Let \( \varepsilon > 0 \). For any \( n \in \mathbb{N} \), we denote \( {A}_{n}\left( \varepsilon \right) = { \cap }_{m \geq n}\left\{ {\left| {{X}_{m} - X}\right| < \varepsilon }\right\} \). The pointwise convergence of \( \left( {X}_{n}\right) \) to \( X \) on \( A \) implies \( A \subset B = { \cup }_{n \in \mathbb{N}}{A}_{n}\left( \varepsilon \right) \). Since \( {\left( {A}_{n}\left( \varepsilon \right) \right) }_{n} \) is an increasing sequence, we deduce \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {{A}_{n}\left( \varepsilon \right) }\right) = P\left( B\right) = 1 \). Thus, for any \( \delta > 0 \), there exists \( N \in \mathbb{N} \) such that \( P\left( {{A}_{n}\left( \varepsilon \right) }\right) \geq 1 - \delta \) for \( n \geq N \). We deduce

\[
\forall n \geq  N,\;P\left( {\left| {{X}_{n} - X}\right|  > \varepsilon }\right)  = 1 - P\left( {\left| {{X}_{n} - X}\right|  \leq  \varepsilon }\right)  \leq  1 - P\left( {{A}_{n}\left( \varepsilon \right) }\right)  \leq  \delta .
\]

On a donc démontré que la suite \( {\left( P\left( \left| {X}_{n} - X\right| > \varepsilon \right) \right) }_{n} \) tend vers 0, d’où le résultat.

> We have thus shown that the sequence \( {\left( P\left( \left| {X}_{n} - X\right| > \varepsilon \right) \right) }_{n} \) tends to 0, hence the result.

b) C'est un classique, rencontré par exemple dans la dernière question de l'exercice 13 page 363. Soit \( p \in {\mathbb{N}}^{ * } \) . D’après le lemme de Borel-Cantelli (voir le théorème 1, page 326, assertion (i)), la convergence de la série \( \mathop{\sum }\limits_{n}P\left( {\left| {{X}_{n} - X}\right| > 1/p}\right) \) entraîne l’existence d’un événement presque sûr \( {B}_{p} \) tel que sur \( {B}_{p} \) , au plus un nombre fini de valeurs de \( n \in \mathbb{N} \) vérifient \( \left| {{X}_{n} - X}\right| > 1/p \) . L’événement \( B = { \cap }_{p \in {\mathbb{N}}^{ * }}{B}_{p} \) , intersection dénombrable d’ensembles presques sûrs, est presque sûr. La suite \( \left( {X}_{n}\right) \) converge simplement vers \( X \) sur \( B \) . En effet, soit \( \omega \in B \) , soit \( \varepsilon > 0 \) . On choisit \( p \in {\mathbb{N}}^{ * } \) tel que \( 1/p < \varepsilon \) . Alors \( \omega \in {B}_{p} \) donc il y a au plus un nombre fini de valeurs de \( n \) telles que \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| > 1/p \) . Donc il existe \( N \in \mathbb{N} \) tel que \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| \leq 1/p \) pour tout \( n \geq N \) , et donc lorsque \( n \geq N \) on a \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| < \varepsilon \) .

> b) This is a classic, encountered for example in the last question of exercise 13 on page 363. Let \( p \in {\mathbb{N}}^{ * } \). According to the Borel-Cantelli lemma (see theorem 1, page 326, assertion (i)), the convergence of the series \( \mathop{\sum }\limits_{n}P\left( {\left| {{X}_{n} - X}\right| > 1/p}\right) \) implies the existence of an almost sure event \( {B}_{p} \) such that on \( {B}_{p} \), at most a finite number of values of \( n \in \mathbb{N} \) satisfy \( \left| {{X}_{n} - X}\right| > 1/p \). The event \( B = { \cap }_{p \in {\mathbb{N}}^{ * }}{B}_{p} \), a countable intersection of almost sure sets, is almost sure. The sequence \( \left( {X}_{n}\right) \) converges pointwise to \( X \) on \( B \). Indeed, let \( \omega \in B \), let \( \varepsilon > 0 \). We choose \( p \in {\mathbb{N}}^{ * } \) such that \( 1/p < \varepsilon \). Then \( \omega \in {B}_{p} \) so there are at most a finite number of values of \( n \) such that \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| > 1/p \). Thus there exists \( N \in \mathbb{N} \) such that \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| \leq 1/p \) for all \( n \geq N \), and therefore when \( n \geq N \) we have \( \left| {{X}_{n}\left( \omega \right) - X\left( \omega \right) }\right| < \varepsilon \).

c) On construit une suite strictement croissante d’entiers \( {\left( {n}_{p}\right) }_{p \in \mathbb{N}} \) par récurrence, comme suit. On pose \( {n}_{0} = 0 \) , et pour \( p \in {\mathbb{N}}^{ * },{n}_{0},\ldots ,{n}_{p - 1} \) étant construits, on choisit \( {n}_{p} > {n}_{p - 1} \) tel que \( P\left( {\left| {{X}_{{n}_{p}} - X}\right| \geq 1/p}\right) < {2}^{-p} \) (c’est possible car la suite \( {\left( P\left( \left| {X}_{n} - X\right| \geq 1/p\right) \right) }_{n} \) converge vers 0 ). Montrons maintenant que pour tout \( \varepsilon > 0 \) , la série \( \mathop{\sum }\limits_{k}P\left( {\left| {{X}_{{n}_{k}} - X}\right| > \varepsilon }\right) \) converge. Le résultat de la question précédente nous assurera alors que la sous-suite \( {\left( {X}_{{n}_{k}}\right) }_{k \in \mathbb{N}} \) converge presque surement vers \( X \) . Fixons donc \( \varepsilon > 0 \) . Soit \( p \in {\mathbb{N}}^{ * } \) tel que \( 1/p < \varepsilon \) . Lorsque \( k > p \) , on a \( 1/k < \varepsilon \) donc

> c) We construct a strictly increasing sequence of integers \( {\left( {n}_{p}\right) }_{p \in \mathbb{N}} \) by induction as follows. We set \( {n}_{0} = 0 \) , and for \( p \in {\mathbb{N}}^{ * },{n}_{0},\ldots ,{n}_{p - 1} \) already constructed, we choose \( {n}_{p} > {n}_{p - 1} \) such that \( P\left( {\left| {{X}_{{n}_{p}} - X}\right| \geq 1/p}\right) < {2}^{-p} \) (this is possible because the sequence \( {\left( P\left( \left| {X}_{n} - X\right| \geq 1/p\right) \right) }_{n} \) converges to 0 ). Let us now show that for any \( \varepsilon > 0 \) , the series \( \mathop{\sum }\limits_{k}P\left( {\left| {{X}_{{n}_{k}} - X}\right| > \varepsilon }\right) \) converges. The result of the previous question will then ensure that the subsequence \( {\left( {X}_{{n}_{k}}\right) }_{k \in \mathbb{N}} \) converges almost surely to \( X \) . Let us fix \( \varepsilon > 0 \) . Let \( p \in {\mathbb{N}}^{ * } \) be such that \( 1/p < \varepsilon \) . When \( k > p \) , we have \( 1/k < \varepsilon \) therefore

\[
\forall k > p,\;P\left( {\left| {{X}_{{n}_{k}} - X}\right|  > \varepsilon }\right)  \leq  P\left( {\left| {{X}_{{n}_{k}} - X}\right|  > 1/k}\right)  < {2}^{-k}.
\]

et donc \( \mathop{\sum }\limits_{k}P\left( {\left| {{X}_{{n}_{k}} - X}\right| > \varepsilon }\right) \) converge. On a bien prouvé le résultat souhaité.

> and thus \( \mathop{\sum }\limits_{k}P\left( {\left| {{X}_{{n}_{k}} - X}\right| > \varepsilon }\right) \) converges. We have indeed proven the desired result.

d) On suit l’indication. Soit \( {\left( {p}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite à valeurs dans ]0,1 [convergeant vers 0, telle que \( \sum {p}_{n} \) diverge (par exemple \( {p}_{n} = 1/\left( {n + 1}\right) \) ). D’après la proposition 17 page 344, il existe un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) et une suite de variables aléatoires \( \left( {X}_{n}\right) \) discrètes indépendantes, telles que \( {X}_{n} \) suive une loi de Bernoulli de paramètre \( {p}_{n} \) , c’est-à-dire \( P\left( {{X}_{n} = 1}\right) = {p}_{n} \) et \( P\left( {{X}_{n} = 0}\right) = 1 - {p}_{n} \) . La suite \( \left( {X}_{n}\right) \) converge en probabilité vers 0 car pour tout \( \varepsilon \in \rbrack 0,1\lbrack \) , on a \( P\left( {\left| {X}_{n}\right| > \varepsilon }\right) = P\left( {{X}_{n} = 1}\right) = {p}_{n} \) . En revanche, d’après le lemme de Borel-Cantelli (assertion (ii)), \( A = \lim \mathop{\sup }\limits_{n}\left\{ {{X}_{n} = 1}\right\} \) est presque sûr, et pour tout \( \omega \in A \) , il existe une infinité d’entiers \( n \) tels que \( {X}_{n}\left( w\right) = 1 \) , donc \( {\left( {X}_{n}\left( \omega \right) \right) }_{n \in \mathbb{N}} \) ne converge pas simplement vers0sur \( A \) .

> d) We follow the hint. Let \( {\left( {p}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence with values in ]0,1 [converging to 0, such that \( \sum {p}_{n} \) diverges (for example \( {p}_{n} = 1/\left( {n + 1}\right) \) ). According to proposition 17 on page 344, there exists a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) and a sequence of independent discrete random variables \( \left( {X}_{n}\right) \) , such that \( {X}_{n} \) follows a Bernoulli distribution with parameter \( {p}_{n} \) , that is to say \( P\left( {{X}_{n} = 1}\right) = {p}_{n} \) and \( P\left( {{X}_{n} = 0}\right) = 1 - {p}_{n} \) . The sequence \( \left( {X}_{n}\right) \) converges in probability to 0 because for any \( \varepsilon \in \rbrack 0,1\lbrack \) , we have \( P\left( {\left| {X}_{n}\right| > \varepsilon }\right) = P\left( {{X}_{n} = 1}\right) = {p}_{n} \) . On the other hand, according to the Borel-Cantelli lemma (assertion (ii)), \( A = \lim \mathop{\sup }\limits_{n}\left\{ {{X}_{n} = 1}\right\} \) is almost sure, and for any \( \omega \in A \) , there exist infinitely many integers \( n \) such that \( {X}_{n}\left( w\right) = 1 \) , therefore \( {\left( {X}_{n}\left( \omega \right) \right) }_{n \in \mathbb{N}} \) does not converge pointwise to 0 on \( A \) .

2/ Supposons que \( \left( {X}_{n}\right) \) converge dans \( {\mathcal{L}}^{1} \) vers \( X \) . Soit \( \varepsilon > 0 \) . L’inégalité de Markov entraîne

> 2/ Suppose that \( \left( {X}_{n}\right) \) converges in \( {\mathcal{L}}^{1} \) to \( X \) . Let \( \varepsilon > 0 \) . Markov's inequality implies

\[
P\left( {\left| {{X}_{n} - X}\right|  \geq  \varepsilon }\right)  \leq  \frac{E\left( \left| {X - {X}_{n}}\right| \right) }{\varepsilon },
\]

et comme \( {\left( E\left( \left| X - {X}_{n}\right| \right) \right) }_{n} \rightarrow 0 \) , on en déduit que \( {\left( P\left( \left| {X}_{n} - X\right| \geq \varepsilon \right) \right) }_{n} \) converge vers 0 .

> and since \( {\left( E\left( \left| X - {X}_{n}\right| \right) \right) }_{n} \rightarrow 0 \) , we deduce that \( {\left( P\left( \left| {X}_{n} - X\right| \geq \varepsilon \right) \right) }_{n} \) converges to 0 .

La réciproque est fausse, comme le montre le contre-exemple suivant : pour tout \( n \in {\mathbb{N}}^{ * } \) , on choisit \( {X}_{n} \) vérifiant \( P\left( {{X}_{n} = 0}\right) = 1 - 1/n \) et \( P\left( {{X}_{n} = n}\right) = 1/n \) . Pour tout \( \varepsilon \in \rbrack 0,1\lbrack \) , on a \( P\left( {\left| {X}_{n}\right| > \varepsilon }\right) = P\left( {{X}_{n} = n}\right) = 1/n \) , donc \( \left( {P\left( {\left| {X}_{n}\right| > \varepsilon }\right) }\right) \) converge vers0, c’est-à-dire que \( {X}_{n} \) converge en probabilité vers 0, alors que \( E\left( \left| {X}_{n}\right| \right) = 1 \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> The converse is false, as shown by the following counterexample: for any \( n \in {\mathbb{N}}^{ * } \), we choose \( {X}_{n} \) satisfying \( P\left( {{X}_{n} = 0}\right) = 1 - 1/n \) and \( P\left( {{X}_{n} = n}\right) = 1/n \). For any \( \varepsilon \in \rbrack 0,1\lbrack \), we have \( P\left( {\left| {X}_{n}\right| > \varepsilon }\right) = P\left( {{X}_{n} = n}\right) = 1/n \), so \( \left( {P\left( {\left| {X}_{n}\right| > \varepsilon }\right) }\right) \) converges to 0, meaning \( {X}_{n} \) converges in probability to 0, whereas \( E\left( \left| {X}_{n}\right| \right) = 1 \) for any \( n \in {\mathbb{N}}^{ * } \).

3/ Supposons que \( \left( {X}_{n}\right) \) converge en probabilité vers \( X \) . Alors \( \left( {P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) }\right) \) converge vers 0 . Fixons \( k \in \mathbb{Z} \) . Comme les variables aléatoires sont à valeurs dans \( \mathbb{Z} \) , on a

> 3/ Suppose that \( \left( {X}_{n}\right) \) converges in probability to \( X \). Then \( \left( {P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) }\right) \) converges to 0. Let us fix \( k \in \mathbb{Z} \). Since the random variables take values in \( \mathbb{Z} \), we have

\[
\left\{  {{X}_{n} = k}\right\}   \subset  \{ X = k\}  \cup  \left\{  {\left| {X - {X}_{n}}\right|  > 1/2}\right\}  \;\text{ et }\;\{ X = k\}  \subset  \left\{  {{X}_{n} = k}\right\}   \cup  \left\{  {\left| {X - {X}_{n}}\right|  > 1/2}\right\}  .
\]

On en déduit \( P\left( {{X}_{n} = k}\right) \leq P\left( {X = k}\right) + P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \) et \( P\left( {X = k}\right) \leq P\left( {{X}_{n} = }\right. \; k) + P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \) , donc \( \left| {P\left( {{X}_{n} = k}\right) - P\left( {X = k}\right) }\right| \leq P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \) , ce qui montre que \( \left| {P\left( {{X}_{n} = k}\right) - P\left( {X = k}\right) }\right| \) tend vers 0 lorsque \( n \rightarrow + \infty \) .

> We deduce \( P\left( {{X}_{n} = k}\right) \leq P\left( {X = k}\right) + P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \) and \( P\left( {X = k}\right) \leq P\left( {{X}_{n} = }\right. \; k) + P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \), so \( \left| {P\left( {{X}_{n} = k}\right) - P\left( {X = k}\right) }\right| \leq P\left( {\left| {{X}_{n} - X}\right| > 1/2}\right) \), which shows that \( \left| {P\left( {{X}_{n} = k}\right) - P\left( {X = k}\right) }\right| \) tends to 0 as \( n \rightarrow + \infty \).

La réciproque est fausse. Considérons par exemple une variable aléatoire \( B \) qui suit une loi de Bernoulli de paramètre \( 1/2 \) , et \( {X}_{n} = B \) pour tout \( n \) . Alors \( \left( {X}_{n}\right) \) converge en loi vers \( X = 1 - B \) ( \( X \) suit aussi une loi de Bernoulli de paramètre \( 1/2 \) , donc elle suit la même loi que chaque \( {X}_{n} \) ), alors qu’on a toujours \( X - {X}_{n} = 1 \) .

> The converse is false. Consider for example a random variable \( B \) that follows a Bernoulli distribution with parameter \( 1/2 \), and \( {X}_{n} = B \) for all \( n \). Then \( \left( {X}_{n}\right) \) converges in distribution to \( X = 1 - B \) (\( X \) also follows a Bernoulli distribution with parameter \( 1/2 \), so it follows the same distribution as each \( {X}_{n} \)), whereas we always have \( X - {X}_{n} = 1 \).

Problem 6 (PROCESSUS DE GALTON-WATSON). Soit \( X \) une variable aléatoire à valeurs dans \( \mathbb{N} \) , admettant une espérance, notée \( m \) . On note, pour tout \( k \in \mathbb{N},{p}_{k} = P\left( {X = k}\right) \) et on suppose \( {p}_{0} \in \rbrack 0,1\left\lbrack \right. \) . Soit \( {\left( {X}_{n, i}\right) }_{\left( {n, i}\right) \in \mathbb{N} \times {\mathbb{N}}^{ * }} \) une famille de variables aléatoires indépen-dantes, suivant toutes la loi de \( X \) . On définit la suite \( \left( {Z}_{n}\right) \) de la manière suivante :

> Problem 6 (GALTON-WATSON PROCESS). Let \( X \) be a random variable taking values in \( \mathbb{N} \), admitting an expectation, denoted by \( m \). We denote, for all \( k \in \mathbb{N},{p}_{k} = P\left( {X = k}\right) \) and we assume \( {p}_{0} \in \rbrack 0,1\left\lbrack \right. \). Let \( {\left( {X}_{n, i}\right) }_{\left( {n, i}\right) \in \mathbb{N} \times {\mathbb{N}}^{ * }} \) be a family of independent random variables, all following the distribution of \( X \). We define the sequence \( \left( {Z}_{n}\right) \) as follows:

\[
{Z}_{0} = 1\;\text{ et }\;\forall n \in  \mathbb{N},{Z}_{n + 1} = \mathop{\sum }\limits_{{i = 1}}^{{Z}_{n}}{X}_{n, i}\;\left( {{Z}_{n + 1} = 0\text{ si }{Z}_{n} = 0}\right) .
\]

La variable aléatoire \( {Z}_{n} \) représente le nombre d’individus à la génération \( n \) . On note \( {\pi }_{n} = P\left( {{Z}_{n} = 0}\right) \) la probabilité d’extinction à la génération \( n \) , et \( {P}_{\text{ ext }} = P\left( {\exists n \in \mathbb{N},{Z}_{n} = 0}\right) \) la probabilité d’extinction de la population. On suppose \( {p}_{0} \in \rbrack 0,1\lbrack \) .

> The random variable \( {Z}_{n} \) represents the number of individuals at generation \( n \). We denote by \( {\pi }_{n} = P\left( {{Z}_{n} = 0}\right) \) the probability of extinction at generation \( n \), and by \( {P}_{\text{ ext }} = P\left( {\exists n \in \mathbb{N},{Z}_{n} = 0}\right) \) the probability of extinction of the population. We assume \( {p}_{0} \in \rbrack 0,1\lbrack \).

1/a) Montrer que la série génératrice \( {G}_{n} \) de \( {Z}_{n} \) vérifie : \( {G}_{n + 1} = G \circ {G}_{n} \) , où \( G \) est la série génératrice de \( X \) .

> 1/a) Show that the generating function \( {G}_{n} \) of \( {Z}_{n} \) satisfies: \( {G}_{n + 1} = G \circ {G}_{n} \), where \( G \) is the generating function of \( X \).

b) En déduire que pour tout \( n \in \mathbb{N},{\pi }_{n + 1} = G\left( {\pi }_{n}\right) \) .

> b) Deduce that for all \( n \in \mathbb{N},{\pi }_{n + 1} = G\left( {\pi }_{n}\right) \).

c) Pour tout \( n \in \mathbb{N} \) , montrer que \( {Z}_{n} \) admet une espérance et calculer \( E\left( {Z}_{n}\right) \) .

> c) For all \( n \in \mathbb{N} \), show that \( {Z}_{n} \) admits an expectation and calculate \( E\left( {Z}_{n}\right) \).

2/a) Montrer que \( G \) n’a aucun point fixe sur \( \lbrack 0,1\lbrack \) si \( m \leq 1 \) , et un seul point fixe sur [0,1[ si \( m > 1 \) .

> 2/a) Show that \( G \) has no fixed point on \( \lbrack 0,1\lbrack \) if \( m \leq 1 \), and a single fixed point on [0,1[ if \( m > 1 \).

b) Montrer que si \( m \leq 1,{P}_{\text{ ext }} = 1 \) , et si \( m > 1,{P}_{\text{ ext }} \) est l’unique point fixe de \( G \) sur [0,1[. Le cas \( m < 1 \) est dit sous-critique, le cas \( m = 1 \) est dit critique et le cas \( m > 1 \) est dit super-critique.

> b) Show that if \( m \leq 1,{P}_{\text{ ext }} = 1 \), and if \( m > 1,{P}_{\text{ ext }} \) is the unique fixed point of \( G \) on [0,1[. The case \( m < 1 \) is called subcritical, the case \( m = 1 \) is called critical, and the case \( m > 1 \) is called supercritical.

3) Soient \( a, b \in \rbrack 0,1\left\lbrack \right. \) . On se place ici dans le cas linéaire-fractionnaire où \( X \) suit la loi

> 3) Let \( a, b \in \rbrack 0,1\left\lbrack \right. \). We consider here the linear-fractional case where \( X \) follows the distribution

\[
P\left( {X = 0}\right)  = a,\;\text{ et }\;\forall k \geq  1, P\left( {X = k}\right)  = \left( {1 - a}\right) b{\left( 1 - b\right) }^{k - 1}
\]

a) Calculer explicitement \( G\left( x\right) \) et vérifier

> a) Calculate \( G\left( x\right) \) explicitly and verify

\[
\sin m \neq  1\;\frac{G\left( x\right)  - \alpha }{G\left( x\right)  - 1} = \frac{1}{m} \cdot  \frac{x - \alpha }{x - 1}\;\text{ avec }\;\alpha  = \frac{a}{1 - b},
\]

\[
\operatorname{si}m = 1\;\frac{1}{G\left( x\right)  - 1} = \frac{1}{x - 1} + \beta \;\text{ avec }\;\beta  = \frac{b - 1}{b}.
\]

b) En déduire les probabilités d’extinction \( {\pi }_{n} \) et \( {P}_{\text{ ext }} \) dans le cas linéaire-fractionnaire.

> b) Deduce the extinction probabilities \( {\pi }_{n} \) and \( {P}_{\text{ ext }} \) in the linear-fractional case.

Solution. 1/a) La formule de Wald (voir la proposition 19 page 347), appliquée avec \( N = {Z}_{n} \) , fournit l’identité \( {G}_{n + 1} = {G}_{n} \circ G \) . La loi de composition est associative on donc bien \( {G}_{n + 1} = \; G \circ {G}_{n} \) .

> Solution. 1/a) Wald's identity (see proposition 19 page 347), applied with \( N = {Z}_{n} \), provides the identity \( {G}_{n + 1} = {G}_{n} \circ G \). The composition law is associative, so we indeed have \( {G}_{n + 1} = \; G \circ {G}_{n} \).

b) C’est une conséquence du fait que pour tout \( n \in \mathbb{N} \) on a \( {\pi }_{n} = {G}_{n}\left( 0\right) \) , donc \( {\pi }_{n + 1} = {G}_{n + 1}\left( 0\right) = \; G \circ {G}_{n}\left( 0\right) = G\left( {{G}_{n}\left( 0\right) }\right) = G\left( {\pi }_{n}\right) . \)

> b) This is a consequence of the fact that for all \( n \in \mathbb{N} \) we have \( {\pi }_{n} = {G}_{n}\left( 0\right) \) , therefore \( {\pi }_{n + 1} = {G}_{n + 1}\left( 0\right) = \; G \circ {G}_{n}\left( 0\right) = G\left( {{G}_{n}\left( 0\right) }\right) = G\left( {\pi }_{n}\right) . \)

c) Pour tout \( n \in \mathbb{N},{Z}_{n} \) admet une espérance si et seulement si sa série génératrice \( {G}_{n} \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) , et on a alors \( E\left( {Z}_{n}\right) = {G}_{n}^{\prime }\left( 1\right) \) . On a \( {G}_{0}\left( x\right) = x \) , donc \( {Z}_{0} \) admet une espérance et \( E\left( {Z}_{0}\right) = 1 \) . La relation \( {G}_{n + 1} = G \circ {G}_{n} \) entraîne avec une récurrence immédiate que les \( {G}_{n} \) sont de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) et que \( {G}_{n + 1}^{\prime }\left( 1\right) = {G}_{n}^{\prime }\left( 1\right) \cdot {G}^{\prime }\left( {{G}_{n}\left( 1\right) }\right) = {G}_{n}^{\prime }\left( 1\right) \cdot {G}^{\prime }\left( 1\right) = m{G}_{n}^{\prime }\left( 1\right) \) . On en déduit que pour tout \( n \in \mathbb{N},{Z}_{n} \) admet une espérance, et que \( E\left( {Z}_{n}\right) = {G}_{n}^{\prime }\left( 1\right) = {m}^{n} \) .

> c) For all \( n \in \mathbb{N},{Z}_{n} \) admits an expectation if and only if its generating series \( {G}_{n} \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) , and we then have \( E\left( {Z}_{n}\right) = {G}_{n}^{\prime }\left( 1\right) \) . We have \( {G}_{0}\left( x\right) = x \) , therefore \( {Z}_{0} \) admits an expectation and \( E\left( {Z}_{0}\right) = 1 \) . The relation \( {G}_{n + 1} = G \circ {G}_{n} \) implies by immediate induction that the \( {G}_{n} \) are of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) and that \( {G}_{n + 1}^{\prime }\left( 1\right) = {G}_{n}^{\prime }\left( 1\right) \cdot {G}^{\prime }\left( {{G}_{n}\left( 1\right) }\right) = {G}_{n}^{\prime }\left( 1\right) \cdot {G}^{\prime }\left( 1\right) = m{G}_{n}^{\prime }\left( 1\right) \) . We deduce that for all \( n \in \mathbb{N},{Z}_{n} \) admits an expectation, and that \( E\left( {Z}_{n}\right) = {G}_{n}^{\prime }\left( 1\right) = {m}^{n} \) .

2/a) Commençons par le cas \( m \leq 1 \) . Si \( {p}_{n} = 0 \) pour tout \( n > 1 \) , alors \( {p}_{0} + {p}_{1} = 1 \) et \( G\left( x\right) = \; {p}_{0} + {p}_{1}x \) . On a donc \( G\left( x\right) - x = {p}_{0} + \left( {{p}_{1} - 1}\right) x = {p}_{0}\left( {1 - x}\right) \) , donc si \( 0 \leq x < 1 \) , on a \( G\left( x\right) - x > 0 \) et donc \( G \) n’admet pas de point fixe sur \( \lbrack 0,1\lbrack \) . Supposons maintenant qu’il existe \( n > 1 \) avec \( {p}_{n} > 0 \) . Comme \( X \) admet une espérance, \( G \) est de classe \( {\mathcal{C}}^{1} \) sur \( \left\lbrack {0,1}\right\rbrack \) . Sa dérivée \( {G}^{\prime }\left( x\right) = \mathop{\sum }\limits_{{n > 1}}n{p}_{n}{x}^{n - 1} \) est strictement croissante sur \( \left\lbrack {0,1}\right\rbrack \) . Pour tout \( x \in \lbrack 0,1\lbrack \) , l’égalité des accroissements finis assure l’existence de \( {c}_{x} \in \rbrack x,1\left\lbrack \right. \) tel que \( G\left( 1\right) - G\left( x\right) = \left( {1 - x}\right) {G}^{\prime }\left( {c}_{x}\right) \) , et on en déduit \( G\left( 1\right) - G\left( x\right) < \; \left( {1 - x}\right) {G}^{\prime }\left( 1\right) = m\left( {1 - x}\right) \leq \left( {1 - x}\right) \) (on vient de redémontrer que la fonction strictement convexe \( G \) est strictement au dessus de sa tangente en1sur \( \left\lbrack {0,1}\right\rbrack \) Donc \( G\left( x\right) > G\left( 1\right) - \left( {1 - x}\right) = x \) , donc \( G \) n’a pas de points fixe sur \( \lbrack 0,1\lbrack \) .

> 2/a) Let us start with the case \( m \leq 1 \) . If \( {p}_{n} = 0 \) for all \( n > 1 \) , then \( {p}_{0} + {p}_{1} = 1 \) and \( G\left( x\right) = \; {p}_{0} + {p}_{1}x \) . We thus have \( G\left( x\right) - x = {p}_{0} + \left( {{p}_{1} - 1}\right) x = {p}_{0}\left( {1 - x}\right) \) , so if \( 0 \leq x < 1 \) , we have \( G\left( x\right) - x > 0 \) and therefore \( G \) has no fixed point on \( \lbrack 0,1\lbrack \) . Now suppose there exists \( n > 1 \) with \( {p}_{n} > 0 \) . Since \( X \) has an expectation, \( G \) is of class \( {\mathcal{C}}^{1} \) on \( \left\lbrack {0,1}\right\rbrack \) . Its derivative \( {G}^{\prime }\left( x\right) = \mathop{\sum }\limits_{{n > 1}}n{p}_{n}{x}^{n - 1} \) is strictly increasing on \( \left\lbrack {0,1}\right\rbrack \) . For all \( x \in \lbrack 0,1\lbrack \) , the mean value theorem ensures the existence of \( {c}_{x} \in \rbrack x,1\left\lbrack \right. \) such that \( G\left( 1\right) - G\left( x\right) = \left( {1 - x}\right) {G}^{\prime }\left( {c}_{x}\right) \) , and we deduce \( G\left( 1\right) - G\left( x\right) < \; \left( {1 - x}\right) {G}^{\prime }\left( 1\right) = m\left( {1 - x}\right) \leq \left( {1 - x}\right) \) (we have just re-proven that the strictly convex function \( G \) lies strictly above its tangent at 1 on \( \left\lbrack {0,1}\right\rbrack \) ). Thus \( G\left( x\right) > G\left( 1\right) - \left( {1 - x}\right) = x \) , so \( G \) has no fixed points on \( \lbrack 0,1\lbrack \) .

![bo_d7fjffs91nqc73erehlg_377_216_1397_1145_336_0.jpg](images/gourdon_algebra_probabilities_fr_en_017_bod7fjffs91nqc73erehlg377216139711453360.jpg)

FIGURE 6. Représentation graphique de la série génératrice \( G \) de \( X \) , dans le cas sous-critique \( \left( {m < 1}\right) \) , puis critique \( \left( {m = 1}\right) \) et super-critique \( \left( {m > 1}\right) \) .

> FIGURE 6. Graphical representation of the generating function \( G \) of \( X \) , in the subcritical \( \left( {m < 1}\right) \) , then critical \( \left( {m = 1}\right) \) and supercritical \( \left( {m > 1}\right) \) cases.

Traîtons maintenant le cas \( m > 1 \) . Il existe forcément \( n > 1 \) tel que \( {p}_{n} > 0 \) (sinon \( G\left( x\right) = \; {p}_{0} + {p}_{1}x \) donc \( m = {G}^{\prime }\left( 1\right) = {p}_{1} < 1 \) , ce qui est impossible). Donc \( {G}^{\prime } - 1 \) est strictement croissante sur \( \left\lbrack {0,1}\right\rbrack \) . Or \( {G}^{\prime }\left( 1\right) - 1 = m - 1 > 0 \) et \( {G}^{\prime }\left( 0\right) - 1 = {p}_{1} - 1 < 0 \) , donc la fonction continue \( {G}^{\prime } - 1 \) s’annule en un point \( \beta \in \rbrack 0,1\left\lbrack \right. \) . Comme \( {G}^{\prime } - 1 \) est strictement croissante, on en déduit \( {G}^{\prime }\left( x\right) - 1 < 0 \) sur \( \left\lbrack {0,\beta \left\lbrack {\text{ et }{G}^{\prime }\left( x\right) - 1 > 0\text{ sur }}\right\rbrack \beta ,1}\right\rbrack \) . Donc \( H\left( x\right) = G\left( x\right) - x \) est strictement décroissante sur \( \left\lbrack {0,\beta }\right\rbrack \) et strictement croissante sur \( \left\lbrack {\beta ,1}\right\rbrack \) . On a donc \( H\left( \beta \right) = G\left( \beta \right) - \beta < G\left( 1\right) - 1 = 0 \) et comme \( H\left( 0\right) = G\left( 0\right) = {p}_{0} > 0 \) on en déduit que \( H\left( x\right) \) s’annule une et une seule fois sur \( \left\lbrack {0,\beta }\right\rbrack \) , et ne s’annule pas sur \( \lbrack \beta ,1\lbrack \) , ce qui démontre le résultat souhaité.

> Let us now consider the case \( m > 1 \) . There necessarily exists \( n > 1 \) such that \( {p}_{n} > 0 \) (otherwise \( G\left( x\right) = \; {p}_{0} + {p}_{1}x \) and thus \( m = {G}^{\prime }\left( 1\right) = {p}_{1} < 1 \) , which is impossible). Therefore \( {G}^{\prime } - 1 \) is strictly increasing on \( \left\lbrack {0,1}\right\rbrack \) . However, \( {G}^{\prime }\left( 1\right) - 1 = m - 1 > 0 \) and \( {G}^{\prime }\left( 0\right) - 1 = {p}_{1} - 1 < 0 \) , so the continuous function \( {G}^{\prime } - 1 \) vanishes at a point \( \beta \in \rbrack 0,1\left\lbrack \right. \) . Since \( {G}^{\prime } - 1 \) is strictly increasing, we deduce \( {G}^{\prime }\left( x\right) - 1 < 0 \) on \( \left\lbrack {0,\beta \left\lbrack {\text{ et }{G}^{\prime }\left( x\right) - 1 > 0\text{ sur }}\right\rbrack \beta ,1}\right\rbrack \) . Thus \( H\left( x\right) = G\left( x\right) - x \) is strictly decreasing on \( \left\lbrack {0,\beta }\right\rbrack \) and strictly increasing on \( \left\lbrack {\beta ,1}\right\rbrack \) . We therefore have \( H\left( \beta \right) = G\left( \beta \right) - \beta < G\left( 1\right) - 1 = 0 \) and since \( H\left( 0\right) = G\left( 0\right) = {p}_{0} > 0 \) we deduce that \( H\left( x\right) \) vanishes exactly once on \( \left\lbrack {0,\beta }\right\rbrack \) , and does not vanish on \( \lbrack \beta ,1\lbrack \) , which proves the desired result.

b) Remarquons que \( {Z}_{n} = 0 \) entraîne \( {Z}_{n + 1} = 0 \) , donc la suite des événements \( {\left\{ {Z}_{n} = 0\right\} }_{n \in \mathbb{N}} \) est croissante. Donc la suite \( {\left( {\pi }_{n}\right) }_{n \in \mathbb{N}} \) est croissante et elle converge. En notant \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\pi }_{n} \) on a

> b) Note that \( {Z}_{n} = 0 \) implies \( {Z}_{n + 1} = 0 \) , so the sequence of events \( {\left\{ {Z}_{n} = 0\right\} }_{n \in \mathbb{N}} \) is increasing. Thus the sequence \( {\left( {\pi }_{n}\right) }_{n \in \mathbb{N}} \) is increasing and it converges. By denoting \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\pi }_{n} \) we have

\[
{P}_{\text{ ext }} = P\left( \left\{  {\exists n \in  \mathbb{N},{Z}_{n} = 0}\right\}  \right)  = P\left( {{ \cup  }_{n \in  \mathbb{N}}\left\{  {{Z}_{n} = 0}\right\}  }\right) ) = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {{Z}_{n} = 0}\right)  = \ell .
\]

(*)

> Comme \( {\pi }_{n + 1} = G\left( {\pi }_{n}\right) \) , par continuité de \( G \) on a \( \ell = G\left( \ell \right) \) . Si \( m \leq 1 \) , la question précédente assure qu’on a forcément \( \ell = 1 \) , donc d’après (*) \( {P}_{\text{ ext }} = 1 \) . Si \( m > 1 \) , l’unique point fixe \( \alpha \) de \( G \) sur \( \lbrack 0,1\lbrack \) vérifie \( {\pi }_{n} \leq \alpha \) (c’est immédiat par récurrence sur \( n : \) vrai pour \( n = 0 \) car \( {\pi }_{0} = 0 \) , et si le résultat est vrai pour \( n \) , alors \( 0 \leq {\pi }_{n} \leq \alpha \) et la croissance de \( G \) sur \( \left\lbrack {0,1}\right\rbrack \) entraîne \( {\pi }_{n + 1} = G\left( {\pi }_{n}\right) \leq G\left( \alpha \right) = \alpha \) donc le résultat est vrai pour \( n + 1) \) . Donc \( \ell \leq \alpha \) , et l’unicité du point fixe de \( G \) sur \( \lbrack 0,1\lbrack \) permet d’en déduire \( \ell = \alpha \) . Donc d’après (*), \( {P}_{\text{ ext }} = \alpha \) .

As \( {\pi }_{n + 1} = G\left( {\pi }_{n}\right) \), by continuity of \( G \) we have \( \ell = G\left( \ell \right) \). If \( m \leq 1 \), the previous question ensures that we necessarily have \( \ell = 1 \), so according to (*) \( {P}_{\text{ ext }} = 1 \). If \( m > 1 \), the unique fixed point \( \alpha \) of \( G \) on \( \lbrack 0,1\lbrack \) satisfies \( {\pi }_{n} \leq \alpha \) (this is immediate by induction on \( n : \) true for \( n = 0 \) because \( {\pi }_{0} = 0 \), and if the result is true for \( n \), then \( 0 \leq {\pi }_{n} \leq \alpha \) and the growth of \( G \) on \( \left\lbrack {0,1}\right\rbrack \) implies \( {\pi }_{n + 1} = G\left( {\pi }_{n}\right) \leq G\left( \alpha \right) = \alpha \) so the result is true for \( n + 1) \)). Thus \( \ell \leq \alpha \), and the uniqueness of the fixed point of \( G \) on \( \lbrack 0,1\lbrack \) allows us to deduce \( \ell = \alpha \). Therefore, according to (*), \( {P}_{\text{ ext }} = \alpha \).

> 3/a) On calcule d’abord la série génératrice \( G\left( x\right) \) de \( X \)

3/a) We first calculate the generating series \( G\left( x\right) \) of \( X \)

\[
\forall x \in  \left\lbrack  {0,1}\right\rbrack  ,\;G\left( x\right)  = a + \mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\left( {1 - a}\right) b{\left( 1 - b\right) }^{k - 1}{x}^{k} = a + \left( {1 - a}\right) {bx}\frac{1}{1 - \left( {1 - b}\right) x}.
\]

En particulier on trouve \( m = {G}^{\prime }\left( 1\right) = \left( {1 - a}\right) + \left( {1 - a}\right) \left( {1 - b}\right) /b = \left( {1 - a}\right) /b \) . L’égalité \( {G}_{n + 1}\left( x\right) = G\left( {{G}_{n}\left( x\right) }\right) \) est celle d’une récurrence homographique (voir le tome analyse), et les identités demandées sont un cas particulier de la résolution explicite de ces récurrences. Dans le cas \( m \neq 1 \) , les solutions de \( G\left( x\right) = x \) sont \( x = 1 \) et \( x = \alpha = a/\left( {1 - b}\right) \) . En posant \( c = 1 - b \) on a

> In particular, we find \( m = {G}^{\prime }\left( 1\right) = \left( {1 - a}\right) + \left( {1 - a}\right) \left( {1 - b}\right) /b = \left( {1 - a}\right) /b \). The equality \( {G}_{n + 1}\left( x\right) = G\left( {{G}_{n}\left( x\right) }\right) \) is that of a homographic recurrence (see the analysis volume), and the requested identities are a special case of the explicit resolution of these recurrences. In the case \( m \neq 1 \), the solutions of \( G\left( x\right) = x \) are \( x = 1 \) and \( x = \alpha = a/\left( {1 - b}\right) \). By setting \( c = 1 - b \) we have

\[
G\left( x\right)  - G\left( y\right)  = \left( {1 - a}\right) b\left( {\frac{x}{1 - {cx}} - \frac{y}{1 - {cy}}}\right)  = \left( {1 - a}\right) b\frac{x - y}{\left( {1 - {cx}}\right) \left( {1 - {cy}}\right) },
\]

\( \left( {* * }\right) \)

> égalité qui reste vraie pour tout \( x, y \in D = \mathbb{R} \smallsetminus \{ 1/c\} \) lorsqu’on étend la définition de \( G\left( x\right) \) à \( D \) tout entier. Comme \( G\left( \alpha \right) = \alpha \) et \( G\left( 1\right) = 1 \) on en déduit

equality which remains true for all \( x, y \in D = \mathbb{R} \smallsetminus \{ 1/c\} \) when extending the definition of \( G\left( x\right) \) to the whole \( D \). Since \( G\left( \alpha \right) = \alpha \) and \( G\left( 1\right) = 1 \) we deduce

\[
\frac{G\left( x\right)  - \alpha }{G\left( x\right)  - 1} = \frac{G\left( x\right)  - G\left( \alpha \right) }{G\left( x\right)  - G\left( 1\right) } = \frac{x - \alpha }{\left( {1 - {cx}}\right) \left( {1 - a}\right) }\frac{\left( {1 - {cx}}\right) b}{x - 1} = \frac{1}{m}\frac{x - \alpha }{x - 1}.
\]

Lorsque \( m = 1 \) , on a \( 1 - a = b \) et \( c = 1 - b = a \) . En utilisant (**) avec \( y = 1 \) pour calculer \( G\left( x\right) - 1 = G\left( x\right) - G\left( 1\right) \) on obtient

> When \( m = 1 \), we have \( 1 - a = b \) and \( c = 1 - b = a \). Using (**) with \( y = 1 \) to calculate \( G\left( x\right) - 1 = G\left( x\right) - G\left( 1\right) \) we obtain

\[
\frac{1}{G\left( x\right)  - 1} - \frac{1}{x - 1} = \frac{\left( {1 - {ax}}\right) b}{{b}^{2}\left( {x - 1}\right) } - \frac{1}{x - 1} = \frac{1 - {ax} - b}{b\left( {x - 1}\right) } =  - \frac{a}{b} = \frac{b - 1}{b}.
\]

b) Les identités obtenues précédemment permettent facilement de déduire, pour tout \( n \in {\mathbb{N}}^{ * } \)

> b) The identities obtained previously allow us to easily deduce, for all \( n \in {\mathbb{N}}^{ * } \)

\[
\text{ si }m \neq  1\;\frac{{G}_{n}\left( x\right)  - \alpha }{{G}_{n}\left( x\right)  - 1} = \frac{1}{{m}^{n}}\frac{x - \alpha }{x - 1},\;\text{ et si }m = 1\;\frac{1}{{G}_{n}\left( x\right)  - 1} = \frac{1}{x - 1} + {n\beta }.
\]

Ceci permet d'obtenir une forme explicite pour \( {G}_{n}\left( x\right) \) , mais nous n’en n’aurons pas besoin directement. En remplaçant \( x \) par 0 dans les relations précédentes on obtient, pour tout \( n \in {\mathbb{N}}^{ * } \)

> This allows us to obtain an explicit form for \( {G}_{n}\left( x\right) \), but we will not need it directly. By replacing \( x \) with 0 in the previous relations we obtain, for all \( n \in {\mathbb{N}}^{ * } \)

\[
\text{ si }m \neq  1\;\frac{{\pi }_{n} - \alpha }{{\pi }_{n} - 1} = \frac{\alpha }{{m}^{n}}\;\text{ donc }\;{\pi }_{n} = \alpha \frac{{m}^{n} - 1}{{m}^{n} - \alpha }
\]

\[
\text{ si }m = 1\;\frac{1}{{\pi }_{n} - 1} = {n\beta } - 1\;\text{ donc }\;{\pi }_{n} = 1 + \frac{1}{{n\beta } - 1} = \frac{n\left( {1 - b}\right) }{n\left( {1 - b}\right)  + b}.
\]

En faisant \( n \rightarrow + \infty \) , on obtient \( {P}_{\text{ ext }} = 1 \) si \( m \leq 1,{P}_{\text{ ext }} = \alpha = a/\left( {1 - b}\right) \) si \( m > 1 \) . On retrouve en particulier le résultat de la question 2/b).

> By doing \( n \rightarrow + \infty \), we obtain \( {P}_{\text{ ext }} = 1 \) if \( m \leq 1,{P}_{\text{ ext }} = \alpha = a/\left( {1 - b}\right) \) if \( m > 1 \). In particular, we recover the result of question 2/b).

Remarque. Ce modèle a été introduit par Watson en 1874 pour étudier la survivance des patronymes dans l'Angleterre victorienne, en réponse à un problème posé par Galton. On l'appelle aussi processus de branchement. Il peut aussi modéliser la reproduction de population de bactéries, de neutrons, d'individus porteurs d'une maladie, etc.

> Remark. This model was introduced by Watson in 1874 to study the survival of surnames in Victorian England, in response to a problem posed by Galton. It is also called a branching process. It can also model the reproduction of populations of bacteria, neutrons, individuals carrying a disease, etc.

Problems 7 (NOMBRES DE STIRLING). Pour tout \( x \in \mathbb{R} \) , on définit la factorielle dé- croissante et la factorielle croissante par \( {x}^{\underline{0}} = {x}^{\overline{0}} = 1 \) , et pour \( n \in {\mathbb{N}}^{ * } \)

> Problems 7 (STIRLING NUMBERS). For any \( x \in \mathbb{R} \), we define the falling factorial and the rising factorial by \( {x}^{\underline{0}} = {x}^{\overline{0}} = 1 \), and for \( n \in {\mathbb{N}}^{ * } \)

\[
{x}^{\underline{n}} = x\left( {x - 1}\right) \cdots \left( {x - n + 1}\right) \;\text{ et }\;{x}^{\bar{n}} = x\left( {x + 1}\right) \cdots \left( {x + n - 1}\right) .
\]

1/ (Nombres de Stirling de première espèce). Pour tout \( n \in \mathbb{N} \) , on note \( {\left( s\left( n, k\right) \right) }_{0 \leq k \leq n} \) et on appelle nombres de Stirling de première espèce les nombres réels définis par

> 1/ (Stirling numbers of the first kind). For any \( n \in \mathbb{N} \), we denote \( {\left( s\left( n, k\right) \right) }_{0 \leq k \leq n} \) and call the real numbers defined by the Stirling numbers of the first kind

\[
\forall x \in  \mathbb{R},\;{x}^{\underline{n}} = \mathop{\sum }\limits_{{k = 0}}^{n}s\left( {n, k}\right) {x}^{k}.
\]

a) Montrer que \( s\left( {n, k}\right) \) a le signe de \( {\left( -1\right) }^{n - k} \) et que les nombres de Stirling de première espèce non signés \( \left| {s\left( {n, k}\right) }\right| \) vérifient

> a) Show that \( s\left( {n, k}\right) \) has the sign of \( {\left( -1\right) }^{n - k} \) and that the unsigned Stirling numbers of the first kind \( \left| {s\left( {n, k}\right) }\right| \) satisfy

\[
\forall x \in  \mathbb{R},\;{x}^{\bar{n}} = \mathop{\sum }\limits_{{k = 0}}^{n}\left| {s\left( {n, k}\right) }\right| {x}^{k}.
\]

b) Montrer que les nombres de Stirling de première espèce vérifient

> b) Show that the Stirling numbers of the first kind satisfy

\[
s\left( {0,0}\right)  = 1\text{ et }\forall n \in  {\mathbb{N}}^{ * }\left\{  \begin{array}{l} s\left( {n,0}\right)  = 0,\;s\left( {n, n}\right)  = 1, \\  \forall k \in  \{ 1,\ldots , n\} ,\;s\left( {n + 1, k}\right)  = s\left( {n, k - 1}\right)  - {ns}\left( {n, k}\right) . \end{array}\right.
\]

c) Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer que \( \left| {s\left( {n, k}\right) }\right| \) est le nombre de permutations de \( \{ 1,\ldots , n\} \) qui s’écrivent comme le produit de \( k \) cycles à supports disjoints.

> c) Let \( n \in {\mathbb{N}}^{ * } \). Show that \( \left| {s\left( {n, k}\right) }\right| \) is the number of permutations of \( \{ 1,\ldots , n\} \) that can be written as the product of \( k \) disjoint cycles.

d) Calculer le nombre moyen de cycles dans une permutation de \( \{ 1,\ldots , n\} \) .

> d) Calculate the average number of cycles in a permutation of \( \{ 1,\ldots , n\} \).

2/ (Nombres de Stirling de seconde espèce). Pour tout \( n \in \mathbb{N} \) , on note \( {\left( S\left( n, k\right) \right) }_{0 \leq k \leq n} \) et on appelle nombres de Stirling de seconde espèce les nombres réels définis par

> 2/ (Stirling numbers of the second kind). For any \( n \in \mathbb{N} \), we denote \( {\left( S\left( n, k\right) \right) }_{0 \leq k \leq n} \) and call the real numbers defined by the Stirling numbers of the second kind

\[
\forall x \in  \mathbb{R},\;{x}^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}S\left( {n, k}\right) {x}^{\underline{k}}.
\]

(*)

> a) Montrer que les \( S\left( {n, k}\right) \) sont bien définis.

a) Show that the \( S\left( {n, k}\right) \) are well-defined.

> b) Montrer que les nombres de Stirling de seconde espèce vérifient

b) Show that the Stirling numbers of the second kind satisfy

\[
S\left( {0,0}\right)  = 1\text{ et }\forall n \in  {\mathbb{N}}^{ * }\left\{  \begin{array}{l} S\left( {n,0}\right)  = 0,\;S\left( {n, n}\right)  = 1, \\  \forall k \in  \{ 1,\ldots , n\} ,\;S\left( {n + 1, k}\right)  = S\left( {n, k - 1}\right)  + {kS}\left( {n, k}\right) . \end{array}\right.
\]

c) Soit \( n \in {\mathbb{N}}^{ * } \) et \( k \in \{ 1,\ldots , n\} \) . Montrer que \( S\left( {n, k}\right) \) est le nombre de façon de par-titionner \( \{ 1,\ldots , n\} \) en \( k \) sous-ensembles. Exprimer en fonction de \( S\left( {n, k}\right) \) le nombre de surjections possibles entre \( \{ 1,\ldots , n\} \) et \( \{ 1,\ldots , k\} \) .

> c) Let \( n \in {\mathbb{N}}^{ * } \) and \( k \in \{ 1,\ldots , n\} \). Show that \( S\left( {n, k}\right) \) is the number of ways to partition \( \{ 1,\ldots , n\} \) into \( k \) subsets. Express the number of possible surjections between \( \{ 1,\ldots , n\} \) and \( \{ 1,\ldots , k\} \) in terms of \( S\left( {n, k}\right) \).

d) En procédant par récurrence sur \( k \in \mathbb{N} \) , montrer que la série génératrice exponentielle \( \operatorname{des}{\left( S\left( n, k\right) \right) }_{n \in \mathbb{N}} \) , définie par \( {\Phi }_{k}\left( x\right) = \mathop{\sum }\limits_{{n = k}}^{{+\infty }}\frac{S\left( {n, k}\right) }{n!}{x}^{n} \) , est bien définie sur \( \mathbb{R} \) et qu’elle vérifie

> d) By proceeding by induction on \( k \in \mathbb{N} \), show that the exponential generating series \( \operatorname{des}{\left( S\left( n, k\right) \right) }_{n \in \mathbb{N}} \), defined by \( {\Phi }_{k}\left( x\right) = \mathop{\sum }\limits_{{n = k}}^{{+\infty }}\frac{S\left( {n, k}\right) }{n!}{x}^{n} \), is well-defined on \( \mathbb{R} \) and that it satisfies

\[
\forall x \in  \mathbb{R}\;{\Phi }_{k}\left( x\right)  = \frac{1}{k!}{\left( {e}^{x} - 1\right) }^{k}.
\]

(**)

> e) Montrer que

e) Show that

\[
\forall n \in  {\mathbb{N}}^{ * },\;\forall k \in  \{ 1,\ldots , n\} ,\;S\left( {n, k}\right)  = \frac{1}{k!}\mathop{\sum }\limits_{{j = 0}}^{k}{\left( -1\right) }^{k - j}\left( \begin{array}{l} k \\  j \end{array}\right) {j}^{n}.
\]

f) Lorsque \( k \) est fixé, donner un équivalent lorsque \( n \rightarrow + \infty \) de \( S\left( {n, k}\right) \) .

> f) When \( k \) is fixed, give an equivalent as \( n \rightarrow + \infty \) of \( S\left( {n, k}\right) \) .

Solution. 1/a) L’identité \( {\left( -1\right) }^{n}{\left( -x\right) }^{\underline{n}} = {x}^{\bar{n}} \) entraîne

> Solution. 1/a) The identity \( {\left( -1\right) }^{n}{\left( -x\right) }^{\underline{n}} = {x}^{\bar{n}} \) implies

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{n - k}s\left( {n, k}\right) {x}^{k} = {\left( -1\right) }^{n}{\left( -x\right) }^{\underline{n}} = {x}^{\bar{n}}
\]

et compte tenu du fait que les coefficients de \( {x}^{\bar{n}} \) sont positifs, ceci entraîne que \( {\left( -1\right) }^{n - k}s\left( {n, k}\right) \) est positif, donc égal à \( \left| {s\left( {n, k}\right) }\right| \) , ce qui montre le résultat demandé.

> and given that the coefficients of \( {x}^{\bar{n}} \) are positive, this implies that \( {\left( -1\right) }^{n - k}s\left( {n, k}\right) \) is positive, hence equal to \( \left| {s\left( {n, k}\right) }\right| \) , which shows the requested result.

b) Comme \( {x}^{\underline{0}} = 1 \) , on a bien \( s\left( {0,0}\right) = 1 \) . Lorsque \( n \geq 1 \) , le coefficient dominant de \( {x}^{\underline{n}} \) est 1, donc \( s\left( {n, n}\right) = 1 \) ; le coefficient constant est 0 donc \( s\left( {n,0}\right) = 0 \) . Maintenant si \( k \in \{ 1,\ldots , n\} \) on a \( {x}^{\underline{n + 1}} = \left( {x - n}\right) {x}^{\underline{n}} \) , donc

> b) As \( {x}^{\underline{0}} = 1 \) , we indeed have \( s\left( {0,0}\right) = 1 \) . When \( n \geq 1 \) , the leading coefficient of \( {x}^{\underline{n}} \) is 1, so \( s\left( {n, n}\right) = 1 \) ; the constant coefficient is 0 so \( s\left( {n,0}\right) = 0 \) . Now if \( k \in \{ 1,\ldots , n\} \) we have \( {x}^{\underline{n + 1}} = \left( {x - n}\right) {x}^{\underline{n}} \) , therefore

\[
\mathop{\sum }\limits_{{k = 0}}^{{n + 1}}s\left( {n + 1, k}\right) {x}^{k} =  - {ns}\left( {n,0}\right)  + \mathop{\sum }\limits_{{k = 1}}^{n}\left( {s\left( {n, k - 1}\right)  - {ns}\left( {n, k}\right) }\right) {x}^{k} + s\left( {n, n}\right) {x}^{n + 1}
\]

et par identification des coefficients de \( {x}^{k} \) pour \( 1 \leq k \leq n \) , on en déduit \( s\left( {n + 1, k}\right) = s(n, k - \) 1) \( - {ns}\left( {n, k}\right) \) pour \( k \in \{ 1,\ldots , n\} \) .

> and by identifying the coefficients of \( {x}^{k} \) for \( 1 \leq k \leq n \) , we deduce \( s\left( {n + 1, k}\right) = s(n, k - \) 1) \( - {ns}\left( {n, k}\right) \) for \( k \in \{ 1,\ldots , n\} \) .

c) On note \( {\mathcal{S}}_{n, k} \) l’ensemble des permutations de \( \{ 1,\ldots , n\} \) qui s’écrivent comme le produit de \( k \) cycles à supports disjoints, et \( C\left( {n, k}\right) = \left| {\mathcal{S}}_{n, k}\right| \) . On va montrer que \( C\left( {n, k}\right) \) suit la même récurrence et les mêmes conditions initiales que \( \left| {s\left( {n, k}\right) }\right| \) . Lorsque \( n \in {\mathbb{N}}^{ * } \) , on a \( C\left( {n,0}\right) = 0 \) (il y a au moins un cycle dans l'écriture de toute permutation comme produits de cycles), et \( C\left( {n, n}\right) = 1 \) car l’identité est la seule permutation qui s’écrit comme le produit de \( n \) cycles de supports disjoints (les \( n \) cycles de supports disjoints ont forcément longueur 1). On a la partition

> c) Let \( {\mathcal{S}}_{n, k} \) be the set of permutations of \( \{ 1,\ldots , n\} \) that can be written as the product of \( k \) disjoint cycles, and \( C\left( {n, k}\right) = \left| {\mathcal{S}}_{n, k}\right| \) . We will show that \( C\left( {n, k}\right) \) follows the same recurrence and the same initial conditions as \( \left| {s\left( {n, k}\right) }\right| \) . When \( n \in {\mathbb{N}}^{ * } \) , we have \( C\left( {n,0}\right) = 0 \) (there is at least one cycle in the writing of any permutation as a product of cycles), and \( C\left( {n, n}\right) = 1 \) because the identity is the only permutation that can be written as the product of \( n \) disjoint cycles (the \( n \) disjoint cycles must have length 1). We have the partition

\[
{\mathcal{S}}_{n + 1, k} = \mathop{\bigcup }\limits_{{1 \leq  m \leq  n + 1}}{\mathcal{S}}_{n + 1, k}\left( m\right) ,\;\text{ où }\;{\mathcal{S}}_{n + 1, k}\left( m\right)  = \left\{  {s \in  {\mathcal{S}}_{n + 1, k} \mid  s\left( {n + 1}\right)  = m}\right\}  .
\]

(***)

> - (Cas \( m = n + 1 \) ). Soit \( s \in  {\mathcal{S}}_{n + 1, k}\left( {n + 1}\right) \) . On a \( s\left( {n + 1}\right)  = n + 1 \) , donc \( \left( {n + 1}\right) \) est un cycle de longueur 1 qui est un des cycles de la décomposition de \( s \) en \( k \) cycles disjoints, donc sa restriction \( {s}_{\mid \{ 1,\ldots , n\} } \) à \( \{ 1,\ldots , n\} \) est une permutation de \( {\mathcal{S}}_{n, k - 1} \) . On vérifie facilement que l’application ainsi construite \( {\mathcal{S}}_{n + 1, k}\left( {n + 1}\right)  \rightarrow  {\mathcal{S}}_{n, k - 1}\;s \mapsto  {s}_{\mid \{ 1,\ldots , n\} } \) est une bijection. Donc \( \left| {{\mathcal{S}}_{n + 1, k}\left( {n + 1}\right) }\right|  = \left| {\mathcal{S}}_{n, k - 1}\right|  = C\left( {n, k - 1}\right) \) .

- (Case \( m = n + 1 \) ). Let \( s \in  {\mathcal{S}}_{n + 1, k}\left( {n + 1}\right) \) . We have \( s\left( {n + 1}\right)  = n + 1 \) , so \( \left( {n + 1}\right) \) is a cycle of length 1 which is one of the cycles in the decomposition of \( s \) into \( k \) disjoint cycles, so its restriction \( {s}_{\mid \{ 1,\ldots , n\} } \) to \( \{ 1,\ldots , n\} \) is a permutation of \( {\mathcal{S}}_{n, k - 1} \) . It is easy to verify that the map thus constructed \( {\mathcal{S}}_{n + 1, k}\left( {n + 1}\right)  \rightarrow  {\mathcal{S}}_{n, k - 1}\;s \mapsto  {s}_{\mid \{ 1,\ldots , n\} } \) is a bijection. Thus \( \left| {{\mathcal{S}}_{n + 1, k}\left( {n + 1}\right) }\right|  = \left| {\mathcal{S}}_{n, k - 1}\right|  = C\left( {n, k - 1}\right) \) .

> - (Cas \( m \leq  n \) ). Soit \( s \in  {\mathcal{S}}_{n + 1, k}\left( m\right) \) . On a \( s\left( {n + 1}\right)  = m \) , donc la permutation \( {s}^{\prime } = \; \left( {n + 1, m}\right)  \cdot  s \) , obtenue en multipliant \( s \) à gauche par la transposition \( \left( {n + 1, m}\right) \) , vérifie \( {s}^{\prime }\left( {n + 1}\right)  = n + 1 \) , et sa restriction à \( \{ 1,\ldots , n\} \) définit donc une permutation de \( \{ 1,\ldots , n\} \) que nous notons \( f\left( s\right) \) . Soit \( c = \left( {n + 1, m,{n}_{3},\ldots ,{n}_{r}}\right) \) le cycle dans la décomposition de \( s \) en produits de cycles, qui contient \( n + 1 \) . On a \( {c}^{\prime } = \left( {n + 1, m}\right)  \cdot  c = \left( {m,{n}_{3},\ldots ,{n}_{r}}\right) \) , donc \( f\left( s\right) \) a les même cycles que \( s \) sauf le cycle \( c \) qui devient \( {c}^{\prime } \) . En particulier \( f\left( s\right) \) contient \( k \) cycles, et \( f \) est une bijection de \( {\mathcal{S}}_{n + 1, k}\left( m\right) \) vers \( {\mathcal{S}}_{n, k} \) . Donc \( \left| {{\mathcal{S}}_{n + 1, k}\left( m\right) }\right|  = \left| {\mathcal{S}}_{n, k}\right|  = C\left( {n, k}\right) \) .

- (Case \( m \leq  n \) ). Let \( s \in  {\mathcal{S}}_{n + 1, k}\left( m\right) \) . We have \( s\left( {n + 1}\right)  = m \) , so the permutation \( {s}^{\prime } = \; \left( {n + 1, m}\right)  \cdot  s \) , obtained by multiplying \( s \) on the left by the transposition \( \left( {n + 1, m}\right) \) , satisfies \( {s}^{\prime }\left( {n + 1}\right)  = n + 1 \) , and its restriction to \( \{ 1,\ldots , n\} \) therefore defines a permutation of \( \{ 1,\ldots , n\} \) which we denote by \( f\left( s\right) \) . Let \( c = \left( {n + 1, m,{n}_{3},\ldots ,{n}_{r}}\right) \) be the cycle in the decomposition of \( s \) into products of cycles, which contains \( n + 1 \) . We have \( {c}^{\prime } = \left( {n + 1, m}\right)  \cdot  c = \left( {m,{n}_{3},\ldots ,{n}_{r}}\right) \) , so \( f\left( s\right) \) has the same cycles as \( s \) except for the cycle \( c \) which becomes \( {c}^{\prime } \) . In particular \( f\left( s\right) \) contains \( k \) cycles, and \( f \) is a bijection from \( {\mathcal{S}}_{n + 1, k}\left( m\right) \) to \( {\mathcal{S}}_{n, k} \) . Thus \( \left| {{\mathcal{S}}_{n + 1, k}\left( m\right) }\right|  = \left| {\mathcal{S}}_{n, k}\right|  = C\left( {n, k}\right) \) .

> De la partition (***), on en déduit

From the partition (***), we deduce

\[
C\left( {n + 1, k}\right)  = \left| {{\mathcal{S}}_{n + 1, k}\left( {n + 1}\right) }\right|  + \mathop{\sum }\limits_{{k = 1}}^{n}\left| {{\mathcal{S}}_{n + 1, k}\left( m\right) }\right|  = C\left( {n, k - 1}\right)  + {nC}\left( {n, k}\right) .
\]

Or \( \left| {s\left( {n, k}\right) }\right| \) vérifie la même récurrence, car d’après la question précédente,

> However \( \left| {s\left( {n, k}\right) }\right| \) satisfies the same recurrence, because according to the previous question,

\[
\left| {s\left( {n + 1, k}\right) }\right|  = {\left( -1\right) }^{n + 1 - k}s\left( {n + 1, k}\right)  = {\left( -1\right) }^{n + 1 - k}\left( {s\left( {n, k - 1}\right)  - {ns}\left( {n, k}\right) }\right)  = \left| {s\left( {n, k - 1}\right) }\right|  + n\left| {s\left( {n, k}\right) }\right| .
\]

On en déduit que \( D\left( {n, k}\right) = \left| {s}_{n, k}\right| - C\left( {n, k}\right) \) vérifie \( D\left( {n,0}\right) = D\left( {n, n}\right) = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) , et \( D\left( {n + 1, k}\right) = D\left( {n, k - 1}\right) + {nD}\left( {n, k}\right) \) pour \( 1 \leq k \leq n \) . En procédant par récurrence sur \( n \in {\mathbb{N}}^{ * } \) , on en déduit que \( D\left( {n, k}\right) = 0 \) pour tout \( k \in \{ 0,\ldots , n\} \) . On a donc bien \( C\left( {n, k}\right) = \left| {s\left( {n, k}\right) }\right| \) pour tout \( n \in {\mathbb{N}}^{ * } \) et \( 0 \leq k \leq n \) .

> We deduce that \( D\left( {n, k}\right) = \left| {s}_{n, k}\right| - C\left( {n, k}\right) \) satisfies \( D\left( {n,0}\right) = D\left( {n, n}\right) = 0 \) for all \( n \in {\mathbb{N}}^{ * } \), and \( D\left( {n + 1, k}\right) = D\left( {n, k - 1}\right) + {nD}\left( {n, k}\right) \) for \( 1 \leq k \leq n \). By proceeding by induction on \( n \in {\mathbb{N}}^{ * } \), we deduce that \( D\left( {n, k}\right) = 0 \) for all \( k \in \{ 0,\ldots , n\} \). We therefore have \( C\left( {n, k}\right) = \left| {s\left( {n, k}\right) }\right| \) for all \( n \in {\mathbb{N}}^{ * } \) and \( 0 \leq k \leq n \).

d) Soit \( {M}_{n} \) le nombre moyen de cycles dans les permutations de \( {\mathcal{S}}_{n} \) . D’après la question précé- dente, on a

> d) Let \( {M}_{n} \) be the average number of cycles in permutations of \( {\mathcal{S}}_{n} \). According to the previous question, we have

\[
{M}_{n} = \frac{1}{n!}\mathop{\sum }\limits_{{k = 1}}^{n}k\left| {s\left( {n, k}\right) }\right|  = \frac{{F}_{n}^{\prime }\left( 1\right) }{n!},\;\text{ où }\;{F}_{n}\left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\left| {s\left( {n, k}\right) }\right| {x}^{k} = {x}^{\bar{n}} = x\left( {x + 1}\right) \cdots \left( {x + n - 1}\right) .
\]

Or

\[
\frac{{F}_{n}^{\prime }\left( x\right) }{{F}_{n}\left( x\right) } = \frac{1}{x} + \frac{1}{x + 1} + \cdots  + \frac{1}{x + n - 1}\;\text{ donc }\;{M}_{n} = \frac{{F}_{n}^{\prime }\left( 1\right) }{{F}_{n}\left( 1\right) } = {H}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n}.
\]

2/a) La matrice carrée \( M \) de taille \( n + 1 \) , dans laquelle on exprime les coefficients des \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \) , en fonction des \( {\left( {x}^{k}\right) }_{0 \leq k \leq n} \) , est une matrice triangulaire dans laquelle les coefficients diagonaux, qui correspondent au coefficient dominant de chaque \( {x}^{\underline{k}} \) , sont tous égaux à 1. Donc cette matrice est inversible, donc les \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \) forment une base des polynômes de degré \( \leq n \) , en particulier on peut exprimer \( {x}^{n} \) comme combinaison linéaire des \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \) , d’où le résultat.

> 2/a) The square matrix \( M \) of size \( n + 1 \), in which we express the coefficients of \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \) in terms of \( {\left( {x}^{k}\right) }_{0 \leq k \leq n} \), is a triangular matrix in which the diagonal coefficients, which correspond to the leading coefficient of each \( {x}^{\underline{k}} \), are all equal to 1. Thus, this matrix is invertible, so the \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \) form a basis for polynomials of degree \( \leq n \); in particular, we can express \( {x}^{n} \) as a linear combination of \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n} \), hence the result.

b) En faisant \( n = 0 \) dans (*) on trouve \( 1 = S\left( {0,0}\right) {x}^{0} = S\left( {0,0}\right) \) . Si \( n \in {\mathbb{N}}^{ * } \) , en faisant \( x = 0 \) dans (*), on trouve \( 0 = S\left( {n,0}\right) \) , et lorsque \( x \rightarrow + \infty \) le terme de droite a pour équivalent \( S\left( {n, n}\right) {x}^{n} \) donc \( S\left( {n, n}\right) = 1 \) . Comme \( x \cdot {x}^{\underline{k}} = \left( {x - k}\right) {x}^{\underline{k}} + k{x}^{\underline{k}} = {x}^{\underline{k + 1}} + k{x}^{\underline{k}} \) , on a

> b) By setting \( n = 0 \) in (*) we find \( 1 = S\left( {0,0}\right) {x}^{0} = S\left( {0,0}\right) \). If \( n \in {\mathbb{N}}^{ * } \), by setting \( x = 0 \) in (*), we find \( 0 = S\left( {n,0}\right) \), and as \( x \rightarrow + \infty \) the term on the right is equivalent to \( S\left( {n, n}\right) {x}^{n} \) so \( S\left( {n, n}\right) = 1 \). Since \( x \cdot {x}^{\underline{k}} = \left( {x - k}\right) {x}^{\underline{k}} + k{x}^{\underline{k}} = {x}^{\underline{k + 1}} + k{x}^{\underline{k}} \), we have

\[
{x}^{n + 1} = x \cdot  {x}^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}S\left( {n, k}\right) \left( {{x}^{\underline{k + 1}} + k{x}^{\underline{k}}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}\left( {S\left( {n, k - 1}\right)  + {kS}\left( {n, k}\right) }\right) {x}^{\underline{k}} + S\left( {n, n}\right) {x}^{\underline{n + 1}}.
\]

Ceci est égal à \( {x}^{n + 1} = \mathop{\sum }\limits_{{k = 0}}^{{n + 1}}S\left( {n + 1, k}\right) {x}^{\underline{k}} \) . Or nous avons vu précédemment que les \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n + 1} \) forment une base des polynômes de degré \( \leq n + 1 \) , on peut donc procéder par identification ce qui donne \( S\left( {n + 1, k}\right) = S\left( {n, k - 1}\right) + {kS}\left( {n, k}\right) \) pour \( 1 \leq k \leq n \) .

> This is equal to \( {x}^{n + 1} = \mathop{\sum }\limits_{{k = 0}}^{{n + 1}}S\left( {n + 1, k}\right) {x}^{\underline{k}} \) . However, we have seen previously that the \( {\left( {x}^{\underline{k}}\right) }_{0 \leq k \leq n + 1} \) form a basis for polynomials of degree \( \leq n + 1 \) , so we can proceed by identification, which gives \( S\left( {n + 1, k}\right) = S\left( {n, k - 1}\right) + {kS}\left( {n, k}\right) \) for \( 1 \leq k \leq n \) .

c) Notons \( {\mathcal{P}}_{n, k} \) l’ensemble des partitions de \( \{ 1,\ldots , n\} \) en \( k \) parties. Soit \( P \in {\mathcal{P}}_{n + 1, k} \) une partition. On numérote les sous-ensembles \( {p}_{1},\ldots ,{p}_{k} \) de \( P \) dans l’ordre de leur plus petit élément, de sorte que \( \min {p}_{1} < \ldots < \min {p}_{k} \) , on note \( m\left( P\right) \) l’indice \( m \) tel que \( n + 1 \in {p}_{m} \) , et on note \( {p}^{\prime }\left( P\right) = {p}_{m\left( P\right) } \smallsetminus \{ n + 1\} \) . On a donc la partition

> c) Let \( {\mathcal{P}}_{n, k} \) be the set of partitions of \( \{ 1,\ldots , n\} \) into \( k \) parts. Let \( P \in {\mathcal{P}}_{n + 1, k} \) be a partition. We number the subsets \( {p}_{1},\ldots ,{p}_{k} \) of \( P \) in order of their smallest element, such that \( \min {p}_{1} < \ldots < \min {p}_{k} \) , we denote \( m\left( P\right) \) as the index \( m \) such that \( n + 1 \in {p}_{m} \) , and we denote \( {p}^{\prime }\left( P\right) = {p}_{m\left( P\right) } \smallsetminus \{ n + 1\} \) . We thus have the partition

\[
{\mathcal{P}}_{n + 1, k} = {\mathcal{P}}_{n + 1, k}^{ * } \cup  \mathop{\bigcup }\limits_{{m = 1}}^{k}{\mathcal{P}}_{n + 1, k}\left( m\right) ,\;\left\{  \begin{array}{l} {\mathcal{P}}_{n + 1, k}^{ * } = \left\{  {P \in  {\mathcal{P}}_{n + 1, k} \mid  {p}^{\prime }\left( P\right)  = \varnothing }\right\}  , \\  {\mathcal{P}}_{n + 1, k}\left( m\right)  = \left\{  {P \in  {\mathcal{P}}_{n + 1, k} \mid  m\left( P\right)  = m,{p}^{\prime }\left( P\right)  \neq  \varnothing }\right\}   \end{array}\right.
\]

L’application \( {\mathcal{P}}_{n + 1, k}^{ * } \rightarrow {\mathcal{P}}_{n, k - 1}\;P \mapsto \left\{ {{p}_{\ell },\ell \neq m\left( p\right) }\right\} \) est une bijection, donc \( \left| {\mathcal{P}}_{n + 1, k}^{ * }\right| = \left| {\mathcal{P}}_{n, k - 1}\right| \) , et pour \( 1 \leq m \leq k \) l’application \( {\mathcal{P}}_{n + 1, k}\left( m\right) \rightarrow {\mathcal{P}}_{n, k}\;P \mapsto \left\{ {{p}_{k}, k \neq m}\right\} \cup \left\{ {{p}^{\prime }\left( P\right) }\right\} \) est aussi une bijection, donc \( \left| {{\mathcal{P}}_{n + 1, k}\left( m\right) }\right| = \left| {\mathcal{P}}_{n, k}\right| \) . On en déduit \( \left| {\mathcal{P}}_{n + 1, k}\right| = \left| {\mathcal{P}}_{n, k - 1}\right| + k\left| {\mathcal{P}}_{n, k}\right| \) , autrement dit \( P\left( {n, k}\right) = \left| {\mathcal{P}}_{n, k}\right| \) satisfait la même récurrence que \( S\left( {n, k}\right) \) . Par ailleurs, il est immédiat que \( P\left( {n,0}\right) = 0 \) et \( P\left( {n, n}\right) = 1 \) , donc \( P\left( {n, k}\right) \) satisfait les même conditions initiales que \( S\left( {n, k}\right) \) . On procéde ensuite comme dans \( 1/\mathrm{c} \) ), en montrant par récurrence sur \( n \in {\mathbb{N}}^{ * } \) que \( P\left( {n, k}\right) - S\left( {n, k}\right) = \) 0 pour \( 0 \leq k \leq n \) . On en déduit que \( P\left( {n, k}\right) = S\left( {n, k}\right) \) .

> The map \( {\mathcal{P}}_{n + 1, k}^{ * } \rightarrow {\mathcal{P}}_{n, k - 1}\;P \mapsto \left\{ {{p}_{\ell },\ell \neq m\left( p\right) }\right\} \) is a bijection, so \( \left| {\mathcal{P}}_{n + 1, k}^{ * }\right| = \left| {\mathcal{P}}_{n, k - 1}\right| \) , and for \( 1 \leq m \leq k \) the map \( {\mathcal{P}}_{n + 1, k}\left( m\right) \rightarrow {\mathcal{P}}_{n, k}\;P \mapsto \left\{ {{p}_{k}, k \neq m}\right\} \cup \left\{ {{p}^{\prime }\left( P\right) }\right\} \) is also a bijection, so \( \left| {{\mathcal{P}}_{n + 1, k}\left( m\right) }\right| = \left| {\mathcal{P}}_{n, k}\right| \) . We deduce \( \left| {\mathcal{P}}_{n + 1, k}\right| = \left| {\mathcal{P}}_{n, k - 1}\right| + k\left| {\mathcal{P}}_{n, k}\right| \) , in other words \( P\left( {n, k}\right) = \left| {\mathcal{P}}_{n, k}\right| \) satisfies the same recurrence as \( S\left( {n, k}\right) \) . Furthermore, it is immediate that \( P\left( {n,0}\right) = 0 \) and \( P\left( {n, n}\right) = 1 \) , so \( P\left( {n, k}\right) \) satisfies the same initial conditions as \( S\left( {n, k}\right) \) . We then proceed as in \( 1/\mathrm{c} \) ), by showing by induction on \( n \in {\mathbb{N}}^{ * } \) that \( P\left( {n, k}\right) - S\left( {n, k}\right) = \) 0 for \( 0 \leq k \leq n \) . We deduce that \( P\left( {n, k}\right) = S\left( {n, k}\right) \) .

A toute partition \( {p}_{1} \cup \ldots \cup {p}_{k} \) de \( \{ 1,\ldots ,, n\} \) et pour toute permutation \( \sigma \) de \( \{ 1,\ldots , k\} \) on peut associer une et une seule surjection \( f \) de \( \{ 1,\ldots , n\} \rightarrow \{ 1,\ldots , k\} \) par \( f\left( i\right) = \sigma \circ g\left( i\right) \) , où \( g\left( i\right) \) est l’indice tel que \( i \in {p}_{g\left( i\right) } \) . On a donc \( S\left( {n, k}\right) \cdot k \) ! surjections possibles de \( \{ 1,\ldots , n\} \rightarrow \{ 1,\ldots , k\} \) . d) Si \( k,\ell \in \mathbb{N} \) vérifient \( k > \ell \) on a \( {\ell }^{\underline{k}} = 0 \) , et si \( k \leq \ell \) on a \( {\ell }^{\underline{k}} \geq 0 \) . La définition (*), appliquée avec \( x = \ell \leq n \) et \( \ell \in \mathbb{N} \) , implique donc \( {\ell }^{n} = \mathop{\sum }\limits_{{k = 0}}^{\ell }S\left( {n, k}\right) {\ell }^{\underline{k}} \geq S\left( {n,\ell }\right) {\ell }^{\underline{\ell }} = S\left( {n,\ell }\right) \ell \) ! (la question précédente assure que les \( S\left( {n, k}\right) \) sont positifs). Donc \( 0 \leq S\left( {n, k}\right) \leq {k}^{n}/k \) !, ce qui implique \( \left| {S\left( {n, k}\right) /n!}\right| \leq \left( {1/k!}\right) {k}^{n}/n! \) , donc la série définissant \( {\Phi }_{k}\left( x\right) \) converge bien pour tout \( x \in \mathbb{R} \) .

> To any partition \( {p}_{1} \cup \ldots \cup {p}_{k} \) of \( \{ 1,\ldots ,, n\} \) and for any permutation \( \sigma \) of \( \{ 1,\ldots , k\} \) one can associate one and only one surjection \( f \) from \( \{ 1,\ldots , n\} \rightarrow \{ 1,\ldots , k\} \) by \( f\left( i\right) = \sigma \circ g\left( i\right) \) , where \( g\left( i\right) \) is the index such that \( i \in {p}_{g\left( i\right) } \) . We therefore have \( S\left( {n, k}\right) \cdot k \) ! possible surjections from \( \{ 1,\ldots , n\} \rightarrow \{ 1,\ldots , k\} \) . d) If \( k,\ell \in \mathbb{N} \) satisfy \( k > \ell \) we have \( {\ell }^{\underline{k}} = 0 \) , and if \( k \leq \ell \) we have \( {\ell }^{\underline{k}} \geq 0 \) . The definition (*), applied with \( x = \ell \leq n \) and \( \ell \in \mathbb{N} \) , therefore implies \( {\ell }^{n} = \mathop{\sum }\limits_{{k = 0}}^{\ell }S\left( {n, k}\right) {\ell }^{\underline{k}} \geq S\left( {n,\ell }\right) {\ell }^{\underline{\ell }} = S\left( {n,\ell }\right) \ell \) ! (the previous question ensures that the \( S\left( {n, k}\right) \) are positive). Thus \( 0 \leq S\left( {n, k}\right) \leq {k}^{n}/k \) !, which implies \( \left| {S\left( {n, k}\right) /n!}\right| \leq \left( {1/k!}\right) {k}^{n}/n! \) , so the series defining \( {\Phi }_{k}\left( x\right) \) indeed converges for all \( x \in \mathbb{R} \) .

Montrons maintenant l’identité (**) par récurrence sur \( k \in \mathbb{N} \) . Pour \( k = 0 \) c’est immédiat. Soit \( k \in {\mathbb{N}}^{ * } \) et supposons la propriété vraie pour \( k - 1 \) . Les relations de récurrence vérifiée par \( S\left( {n, k}\right) \) entraînent

> Let us now show the identity (**) by induction on \( k \in \mathbb{N} \) . For \( k = 0 \) it is immediate. Let \( k \in {\mathbb{N}}^{ * } \) and assume the property is true for \( k - 1 \) . The recurrence relations satisfied by \( S\left( {n, k}\right) \) entail

\[
{\Phi }_{k}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = k - 1}}^{{+\infty }}\frac{S\left( {n + 1, k}\right) }{n!}{x}^{n} = \frac{{x}^{k - 1}}{\left( {k - 1}\right) !} + \mathop{\sum }\limits_{{n = k}}^{{+\infty }}\frac{S\left( {n, k - 1}\right)  + {kS}\left( {n, k}\right) }{n!}{x}^{n} = {\Phi }_{k - 1}\left( x\right)  + k{\Phi }_{k}\left( x\right) .
\]

D’après l’hypothèse de récurrence, \( {\Phi }_{k - 1}\left( x\right) = {\left( {e}^{x} - 1\right) }^{k - 1}/\left( {k - 1}\right) \) !. On a donc \( {\Phi }_{k}^{\prime }\left( x\right) - k{\Phi }_{k}\left( x\right) = \; {\left( {e}^{x} - 1\right) }^{k - 1}/\left( {k - 1}\right) \) !. En notant \( {\Delta }_{k}\left( x\right) = {\Phi }_{k}\left( x\right) - {\left( {e}^{x} - 1\right) }^{k}/k \) !, ceci entraîne \( {\Delta }_{k}^{\prime } = k{\Delta }_{k} \) sur \( \mathbb{R} \) . Donc il existe \( \lambda \in \mathbb{R} \) tel que \( {\Delta }_{k}\left( x\right) = \lambda {e}^{kx} \) . Lorsque \( x = 0 \) , on a \( {\Delta }_{k}\left( 0\right) = {\Phi }_{k}\left( 0\right) = 0 \) , donc \( \lambda = 0 \) , donc \( {\Phi }_{k}\left( x\right) = {\left( {e}^{x} - 1\right) }^{k}/k \) ! pour tout \( x \in \mathbb{R} \) .

> According to the induction hypothesis, \( {\Phi }_{k - 1}\left( x\right) = {\left( {e}^{x} - 1\right) }^{k - 1}/\left( {k - 1}\right) \) !. We therefore have \( {\Phi }_{k}^{\prime }\left( x\right) - k{\Phi }_{k}\left( x\right) = \; {\left( {e}^{x} - 1\right) }^{k - 1}/\left( {k - 1}\right) \) !. By noting \( {\Delta }_{k}\left( x\right) = {\Phi }_{k}\left( x\right) - {\left( {e}^{x} - 1\right) }^{k}/k \) !, this leads to \( {\Delta }_{k}^{\prime } = k{\Delta }_{k} \) on \( \mathbb{R} \) . Thus there exists \( \lambda \in \mathbb{R} \) such that \( {\Delta }_{k}\left( x\right) = \lambda {e}^{kx} \) . When \( x = 0 \) , we have \( {\Delta }_{k}\left( 0\right) = {\Phi }_{k}\left( 0\right) = 0 \) , therefore \( \lambda = 0 \) , so \( {\Phi }_{k}\left( x\right) = {\left( {e}^{x} - 1\right) }^{k}/k \) ! for all \( x \in \mathbb{R} \) .

e) En développant la formule (**), on trouve pour tout \( k \in \mathbb{N} \)

> e) By expanding the formula (**), we find for all \( k \in \mathbb{N} \)

\[
\mathop{\sum }\limits_{{n = k}}^{{+\infty }}\frac{S\left( {n, k}\right) }{n!}{x}^{n} = \frac{1}{k!}\mathop{\sum }\limits_{{j = 0}}^{k}{\left( -1\right) }^{k - j}\left( \begin{array}{l} k \\  j \end{array}\right) {e}^{jx} = \frac{1}{k!}\mathop{\sum }\limits_{{j = 0}}^{k}{\left( -1\right) }^{k - j}\left( \begin{array}{l} k \\  j \end{array}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{j}^{n}}{n!}{x}^{n}}\right) .
\]

En identifiant les coefficients de \( {x}^{n} \) on en déduit

> By identifying the coefficients of \( {x}^{n} \) we deduce

\[
\forall n \geq  k,\;\frac{S\left( {n, k}\right) }{n!} = \frac{1}{k!}\mathop{\sum }\limits_{{j = 0}}^{k}{\left( -1\right) }^{k - j}\left( \begin{array}{l} k \\  j \end{array}\right) \frac{{j}^{n}}{n!},
\]

et en multipliant cette égalité par \( n \) ! on obtient le résultat souhaité.

> and by multiplying this equality by \( n \) ! we obtain the desired result.

f) La formule précédente entraîne, lorsque \( n \rightarrow + \infty \) , l’équivalent \( S\left( {n, k}\right) \sim {k}^{n}/k \) !.

> f) The previous formula leads, when \( n \rightarrow + \infty \) , to the equivalent \( S\left( {n, k}\right) \sim {k}^{n}/k \) !.

Remarque. On a \( \mathop{\sum }\limits_{{k = 0}}^{n}S\left( {n, k}\right) = {B}_{n} \) où \( {B}_{n} \) est le nombre de Bell, rencontré dans l’exer-cice 8 page 314. En sommant sur \( k \) les séries génératrices exponentielles des \( {\left( S\left( n, k\right) \right) }_{n} \) on retrouve l’expression de la série génératrice exponentielle de \( {B}_{n} \) .

> Remark. We have \( \mathop{\sum }\limits_{{k = 0}}^{n}S\left( {n, k}\right) = {B}_{n} \) where \( {B}_{n} \) is the Bell number, encountered in exercise 8 on page 314. By summing over \( k \) the exponential generating series of \( {\left( S\left( n, k\right) \right) }_{n} \) we recover the expression of the exponential generating series of \( {B}_{n} \) .

PROBLÉME 8 (THÉORÉME DE PÓLYA). Soit \( d \in {\mathbb{N}}^{ * } \) et \( \left( {{e}_{1},\ldots ,{e}_{d}}\right) \) la base canonique de \( {\mathbb{R}}^{d} \) . Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires indépendantes et identiquement distribuées,à valeurs dans \( \left\{ {-{e}_{1},{e}_{1}, - {e}_{2},{e}_{2},\ldots , - {e}_{d},{e}_{d}}\right\} \) . On considère la marche aléatoire sur \( {\mathbb{Z}}^{d} \) définie par \( {S}_{0} = 0 \) et \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) pour \( n \in {\mathbb{N}}^{ * } \) . On dit que \( \left( {S}_{n}\right) \) est récurrente, si presque surement, il existe une infinité d’entiers \( n \in {\mathbb{N}}^{ * } \) tels que \( {S}_{n} = 0 \) ; on dit que \( \left( {S}_{n}\right) \) est transitoire si presque surement, il n’existe qu’un nombre fini d’entiers \( n \in {\mathbb{N}}^{ * } \) tels que \( {S}_{n} = 0 \) .

> PROBLEM 8 (PÓLYA'S THEOREM). Let \( d \in {\mathbb{N}}^{ * } \) and \( \left( {{e}_{1},\ldots ,{e}_{d}}\right) \) be the canonical basis of \( {\mathbb{R}}^{d} \). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent and identically distributed random variables taking values in \( \left\{ {-{e}_{1},{e}_{1}, - {e}_{2},{e}_{2},\ldots , - {e}_{d},{e}_{d}}\right\} \). Consider the random walk on \( {\mathbb{Z}}^{d} \) defined by \( {S}_{0} = 0 \) and \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) for \( n \in {\mathbb{N}}^{ * } \). We say that \( \left( {S}_{n}\right) \) is recurrent if, almost surely, there exist infinitely many integers \( n \in {\mathbb{N}}^{ * } \) such that \( {S}_{n} = 0 \); we say that \( \left( {S}_{n}\right) \) is transient if, almost surely, there exist only a finite number of integers \( n \in {\mathbb{N}}^{ * } \) such that \( {S}_{n} = 0 \).

1/ Montrer que si la série \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}P\left( {{S}_{n} = 0}\right) \) diverge, alors \( \left( {S}_{n}\right) \) est récurrente, et que si \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}P\left( {{S}_{n} = 0}\right) \) converge, alors \( \left( {S}_{n}\right) \) est transitoire.

> 1/ Show that if the series \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}P\left( {{S}_{n} = 0}\right) \) diverges, then \( \left( {S}_{n}\right) \) is recurrent, and if \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}P\left( {{S}_{n} = 0}\right) \) converges, then \( \left( {S}_{n}\right) \) is transient.

2/ On se place désormais dans le cas isotrope, où les \( \left( {X}_{n}\right) \) suivent toutes la loi

> 2/ We now consider the isotropic case, where the \( \left( {X}_{n}\right) \) all follow the distribution

\[
\forall i \in  \{ 1,\ldots , d\} ,\;P\left( {{X}_{n} = {e}_{i}}\right)  = P\left( {{X}_{n} =  - {e}_{i}}\right)  = \frac{1}{2d}.
\]

a) Calculer explicitement \( P\left( {{S}_{n} = 0}\right) \) lorsque \( d = 1 \) ou \( d = 2 \) , et en déduire que lorsque \( d \in \{ 1,2\} \) , alors la marche aléatoire \( \left( {S}_{n}\right) \) est récurrente.

> a) Explicitly calculate \( P\left( {{S}_{n} = 0}\right) \) when \( d = 1 \) or \( d = 2 \), and deduce that when \( d \in \{ 1,2\} \), the random walk \( \left( {S}_{n}\right) \) is recurrent.

b) Dans le cas \( d = 3 \) , exprimer sous forme de somme multiple la valeur de \( P\left( {{S}_{n} = 0}\right) \) , et montrer que la marche aléatoire \( \left( {S}_{n}\right) \) est transitoire.

> b) In the case \( d = 3 \), express the value of \( P\left( {{S}_{n} = 0}\right) \) as a multiple sum, and show that the random walk \( \left( {S}_{n}\right) \) is transient.

3 / On appelle chemin de \( {\mathbb{Z}}^{d} \) de longueur \( n \in \mathbb{N} \) , toute famille \( {\left( {C}_{k}\right) }_{0 < k < n} \) de \( {\mathbb{Z}}^{d} \) vérifiant \( {C}_{0} = 0 \) et \( \forall k \in \{ 0,\ldots , n - 1\} ,{C}_{k + 1} - {C}_{k} \in \left\{ {-{e}_{1},{e}_{1},\ldots , - {e}_{d},{e}_{d}}\right\} \) ; si \( {C}_{n} = 0 \) on dit que le chemin \( \left( {C}_{k}\right) \) est une boucle. On note \( {c}_{n}^{\left( d\right) } \) le nombre de boucles de \( {\mathbb{Z}}^{d} \) de longueur \( n \) .

> 3/ A path of \( {\mathbb{Z}}^{d} \) of length \( n \in \mathbb{N} \) is any family \( {\left( {C}_{k}\right) }_{0 < k < n} \) of \( {\mathbb{Z}}^{d} \) satisfying \( {C}_{0} = 0 \) and \( \forall k \in \{ 0,\ldots , n - 1\} ,{C}_{k + 1} - {C}_{k} \in \left\{ {-{e}_{1},{e}_{1},\ldots , - {e}_{d},{e}_{d}}\right\} \); if \( {C}_{n} = 0 \), the path \( \left( {C}_{k}\right) \) is called a loop. Let \( {c}_{n}^{\left( d\right) } \) denote the number of loops of \( {\mathbb{Z}}^{d} \) of length \( n \).

a) Montrer que la série génératrice exponentielle \( {\Phi }_{d}\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{c}_{n}^{\left( d\right) }}{n!}{z}^{n} \) a un rayon de convergence infini, puis montrer

> a) Show that the exponential generating function \( {\Phi }_{d}\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{c}_{n}^{\left( d\right) }}{n!}{z}^{n} \) has an infinite radius of convergence, then show

\[
\forall z \in  \mathbb{C},\;{\Phi }_{1}\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{2n}}{{\left( n!\right) }^{2}},\;\text{ et }\;\forall d \in  {\mathbb{N}}^{ * },\;{\Phi }_{d}\left( z\right)  = {\Phi }_{1}{\left( z\right) }^{d}.
\]

b) Montrer que \( {\Phi }_{1}\left( z\right) \) vérifie l’identité

> b) Show that \( {\Phi }_{1}\left( z\right) \) satisfies the identity

\[
\forall t \in  \mathbb{R},\;{\Phi }_{1}\left( t\right)  = {I}_{0}\left( {2t}\right) ,\;\text{ où }\;{I}_{0}\left( t\right)  = \frac{1}{\pi }{\int }_{0}^{\pi }{e}^{t\cos \theta }{d\theta },
\]

puis déterminer un équivalent de \( {I}_{0}\left( t\right) \) lorsque \( t \rightarrow + \infty \) .

> then determine an equivalent for \( {I}_{0}\left( t\right) \) as \( t \rightarrow + \infty \) .

c) Montrer que la série génératrice \( \varphi \left( x\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{S}_{n} = 0}\right) {x}^{n} \) vérifie

> c) Show that the generating function \( \varphi \left( x\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {{S}_{n} = 0}\right) {x}^{n} \) satisfies

\[
\forall x \in  \rbrack  - 1,1\lbrack ,\;\varphi \left( x\right)  = {\int }_{0}^{+\infty }{I}_{0}{\left( \frac{tx}{d}\right) }^{d}{e}^{-t}{dt}.
\]

En déduire le théorème de Pólya : \( \left( {S}_{n}\right) \) est récurrente si \( d \in \{ 1,2\} \) , transitoire si \( d \geq 3 \) .

> Deduce Pólya's theorem: \( \left( {S}_{n}\right) \) is recurrent if \( d \in \{ 1,2\} \) , transient if \( d \geq 3 \) .

---

Solution. \( 1/ \) Si \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) converge, le lemme de Borel-Cantelli nous assure que presque surement, il n’y a qu’un nombre fini d’entiers \( n \) tel que \( {S}_{n} = 0 \) , i.e. que \( \left( {S}_{n}\right) \) est transitoire.

> Solution. \( 1/ \) If \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) converges, the Borel-Cantelli lemma ensures that almost surely, there are only finitely many integers \( n \) such that \( {S}_{n} = 0 \) , i.e., that \( \left( {S}_{n}\right) \) is transient.

Supposons maintenant que \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverge. Ici on ne peut pas appliquer le lemme de Borel-Cantelli car les événements \( \left\{ {{S}_{2n} = 0}\right\} \) ne sont pas indépendants. Pour prouver que presque surement, la marche aléatoire passe une infinité de fois par 0, il est équivalent de prouver que

> Now suppose that \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverges. Here we cannot apply the Borel-Cantelli lemma because the events \( \left\{ {{S}_{2n} = 0}\right\} \) are not independent. To prove that almost surely, the random walk visits 0 infinitely often, it is equivalent to prove that

---

l'événement \( B \) "la marche aléatoire ne passe qu'un nombre fini de fois par 0" est négligeable. On partitionne \( B \) sous la forme \( B = { \cup }_{n \in \mathbb{N}}{B}_{n} \) , où \( {B}_{n} \) désigne l’événement des marches aléatoires qui passe en 0 la dernière fois à l’indice \( n \) . On a donc \( P\left( B\right) = \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {B}_{n}\right) \) . Par ailleurs, on a

> the event \( B \) "the random walk visits 0 only finitely many times" is negligible. We partition \( B \) as \( B = { \cup }_{n \in \mathbb{N}}{B}_{n} \) , where \( {B}_{n} \) denotes the event of random walks that visit 0 for the last time at index \( n \) . We thus have \( P\left( B\right) = \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {B}_{n}\right) \) . Furthermore, we have

\[
{B}_{n} = \left\{  {{S}_{n} = 0}\right\}   \cap  \left\{  {\forall k > n,{S}_{k} \neq  0}\right\}   = \left\{  {{S}_{n} = 0}\right\}   \cap  \left\{  {\forall j > 0,{X}_{n + 1} + \cdots  + {X}_{n + j} \neq  0}\right\}  .
\]

car si \( {S}_{n} = 0 \) et \( k > n \) , avoir \( {S}_{k} = 0 \) équivaut à avoir \( 0 = {S}_{k} - {S}_{n} = {X}_{n + 1} + \cdots + {X}_{k} \) . Or les \( \left( {X}_{k}\right) \) sont indépendants, donc \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) est indépendant de \( {X}_{n + 1} + \cdots + {X}_{n + j} \) . On peut donc écrire

> because if \( {S}_{n} = 0 \) and \( k > n \) , having \( {S}_{k} = 0 \) is equivalent to having \( 0 = {S}_{k} - {S}_{n} = {X}_{n + 1} + \cdots + {X}_{k} \) . Now, the \( \left( {X}_{k}\right) \) are independent, so \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) is independent of \( {X}_{n + 1} + \cdots + {X}_{n + j} \) . We can therefore write

\[
P\left( {B}_{n}\right)  = P\left( {{S}_{n} = 0}\right) P\left( {\forall j > 0,{X}_{n + 1} + \cdots  + {X}_{n + j} \neq  0}\right) .
\]

Les \( \left( {X}_{k}\right) \) étant indépendants et identiquement distribuées, \( P\left( {\forall j > 0,{X}_{n + 1} + \cdots + {X}_{n + j} \neq 0}\right) \) ne dépend pas de \( n \) . Notons \( q \) cette probabilité. On a donc \( P\left( {B}_{n}\right) = {qP}\left( {{S}_{n} = 0}\right) \) . Or la série \( \sum P\left( {B}_{n}\right) \) converge (vers \( P\left( B\right) \) ), et comme \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverge, la seule possibilité est d’avoir \( q = 0 \) . Donc \( P\left( {B}_{n}\right) = 0 \) pour tout \( n \in \mathbb{N} \) , donc \( P\left( B\right) = 0 \) .

> Since the \( \left( {X}_{k}\right) \) are independent and identically distributed, \( P\left( {\forall j > 0,{X}_{n + 1} + \cdots + {X}_{n + j} \neq 0}\right) \) does not depend on \( n \) . Let us denote this probability by \( q \) . We therefore have \( P\left( {B}_{n}\right) = {qP}\left( {{S}_{n} = 0}\right) \) . However, the series \( \sum P\left( {B}_{n}\right) \) converges (to \( P\left( B\right) \) ), and since \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverges, the only possibility is to have \( q = 0 \) . Thus \( P\left( {B}_{n}\right) = 0 \) for all \( n \in \mathbb{N} \) , and therefore \( P\left( B\right) = 0 \) .

2/a) Remarquons déja que, quelque soit la valeur de \( d \) , la somme des coordonnées de \( {S}_{n} \) a la même parité que \( n \) . Donc on ne peut avoir \( {S}_{n} = 0 \) que si \( n \) est pair. Ainsi, \( P\left( {{S}_{{2n} + 1} = 0}\right) \) pour tout \( n \in \mathbb{N} \) , et on se bornera dans la suite à estimer \( P\left( {{S}_{2n} = 0}\right) \) .

> 2/a) Let us first note that, whatever the value of \( d \) , the sum of the coordinates of \( {S}_{n} \) has the same parity as \( n \) . Therefore, we can only have \( {S}_{n} = 0 \) if \( n \) is even. Thus, \( P\left( {{S}_{{2n} + 1} = 0}\right) \) for all \( n \in \mathbb{N} \) , and we will limit ourselves in the following to estimating \( P\left( {{S}_{2n} = 0}\right) \) .

Traitons maintenant le cas \( d = 1 \) . Pour avoir \( {S}_{2n} = 0 \) , il faut et il suffit d’avoir exactement \( n \) indices \( k \) parmi \( \{ 1,\ldots ,{2n}\} \) tels que \( {X}_{k} = 1 \) , et chaque \( {2n} \) -liste possible \( \left( {X}_{k}\right) \) correspondante a une probabilité \( {2}^{-{2n}} \) de se produire. On en déduit, en utilisant la formule de Stirling, que

> Let us now treat the case \( d = 1 \) . To have \( {S}_{2n} = 0 \) , it is necessary and sufficient to have exactly \( n \) indices \( k \) among \( \{ 1,\ldots ,{2n}\} \) such that \( {X}_{k} = 1 \) , and each corresponding \( {2n} \) -list \( \left( {X}_{k}\right) \) has a probability \( {2}^{-{2n}} \) of occurring. We deduce from this, using Stirling's formula, that

\[
P\left( {{S}_{2n} = 0}\right)  = {2}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right)  = {2}^{-{2n}}\frac{\left( {2n}\right) !}{{\left( n!\right) }^{2}} \sim  {2}^{-{2n}}\frac{\sqrt{4\pi n}{\left( 2n/e\right) }^{2n}}{{\left( \sqrt{2\pi n}{\left( n/e\right) }^{n}\right) }^{2}} = \frac{1}{\sqrt{\pi n}}.
\]

Donc \( \mathop{\sum }\limits_{n}P\left( {{S}_{2n} = 0}\right) \) diverge, donc d’après la question \( 1/,\left( {S}_{n}\right) \) est récurrente.

> Therefore \( \mathop{\sum }\limits_{n}P\left( {{S}_{2n} = 0}\right) \) diverges, so according to question \( 1/,\left( {S}_{n}\right) \) is recurrent.

Lorsque \( d = 2 \) , pour avoir \( {S}_{2n} = 0 \) il faut et il suffit que la partition ordonnée de \( \{ 1,\ldots ,{2n}\} \) formée des 4 sous-ensembles d’indices \( \left( {{A}_{1},{A}_{1}^{\prime },{A}_{2},{A}_{2}^{\prime }}\right) \) définis pour \( \ell \in \{ 1,2\} \) par

> When \( d = 2 \) , to have \( {S}_{2n} = 0 \) it is necessary and sufficient that the ordered partition of \( \{ 1,\ldots ,{2n}\} \) formed by the 4 subsets of indices \( \left( {{A}_{1},{A}_{1}^{\prime },{A}_{2},{A}_{2}^{\prime }}\right) \) defined for \( \ell \in \{ 1,2\} \) by

\[
{A}_{\ell } = \left\{  {m \in  \{ 1,\ldots ,{2n}\}  \mid  {X}_{m} = {e}_{\ell }}\right\}  \;\text{ et }\;{A}_{\ell }^{\prime } = \left\{  {m \in  \{ 1,\ldots ,{2n}\}  \mid  {X}_{m} =  - {e}_{\ell }}\right\}  ,
\]

(*)

> vérifie \( \left| {A}_{1}\right| = \left| {A}_{1}^{\prime }\right| = i \) et \( \left| {A}_{2}\right| = \left| {A}_{2}^{\prime }\right| = j \) avec \( i + j = n \) . Lorsque \( i + j = n \) , la proposition 15 page 304 nous assure que le nombre de \( {2n} \) -listes \( \left( {X}_{m}\right) \) de cette forme est \( \left( \begin{matrix} {2n} \\ i, i, j, j \end{matrix}\right) \) . Chacune a une probabilité \( {4}^{-{2n}} \) de se produire, on en déduit

satisfies \( \left| {A}_{1}\right| = \left| {A}_{1}^{\prime }\right| = i \) and \( \left| {A}_{2}\right| = \left| {A}_{2}^{\prime }\right| = j \) with \( i + j = n \) . When \( i + j = n \) , proposition 15 on page 304 ensures that the number of \( {2n} \) -lists \( \left( {X}_{m}\right) \) of this form is \( \left( \begin{matrix} {2n} \\ i, i, j, j \end{matrix}\right) \) . Each has a probability \( {4}^{-{2n}} \) of occurring, from which we deduce

\[
P\left( {{S}_{2n} = 0}\right)  = {4}^{-{2n}}\mathop{\sum }\limits_{{i + j = n}}\left( \begin{matrix} {2n} \\  i, i, j, j \end{matrix}\right)  = {4}^{-{2n}}\mathop{\sum }\limits_{{i = 0}}^{n}\frac{\left( {2n}\right) !}{i!i!\left( {n - i}\right) !\left( {n - i}\right) !} = {4}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \mathop{\sum }\limits_{{i = 0}}^{n}{\left( \begin{array}{l} n \\  i \end{array}\right) }^{2}.
\]

En utilisant la formule de Vandermonde puis à nouveau la formule de Stirling, on en déduit

> Using Vandermonde's identity and then Stirling's formula again, we deduce

\[
P\left( {{S}_{2n} = 0}\right)  = {4}^{-{2n}}{\left( \begin{matrix} {2n} \\  n \end{matrix}\right) }^{2} = {\left( {2}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \right) }^{2} \sim  {\left( \frac{1}{\sqrt{\pi n}}\right) }^{2} = \frac{1}{\pi n}.
\]

Donc \( \mathop{\sum }\limits_{n}P\left( {{S}_{2n} = 0}\right) \) diverge, donc \( \left( {S}_{n}\right) \) est récurrente.

> Therefore \( \mathop{\sum }\limits_{n}P\left( {{S}_{2n} = 0}\right) \) diverges, so \( \left( {S}_{n}\right) \) is recurrent.

b) Pour le cas \( d = 3 \) , on procéde en généralisant l’approche utilisée dans le cas \( d = 2 \) . Ici il s’agit de compter le nombre de partitions ordonnées de \( \{ 1,\ldots ,{2n}\} \) formée des 6 sous-ensembles \( \left( {{A}_{1},{A}_{1}^{\prime },{A}_{2},{A}_{2}^{\prime },{A}_{3},{A}_{3}^{\prime }}\right) \) définis par (*), tels que \( \left| {A}_{\ell }\right| = \left| {A}_{\ell }^{\prime }\right| = {i}_{\ell } \) , avec \( {i}_{1} + {i}_{2} + {i}_{3} = n \) . A chacune de ces partitions il y a un chemin possible avec une probabilité \( {6}^{-{2n}} \) de se réaliser, donc

> b) For the case \( d = 3 \), we proceed by generalizing the approach used in the case \( d = 2 \). Here, it is a matter of counting the number of ordered partitions of \( \{ 1,\ldots ,{2n}\} \) formed by the 6 subsets \( \left( {{A}_{1},{A}_{1}^{\prime },{A}_{2},{A}_{2}^{\prime },{A}_{3},{A}_{3}^{\prime }}\right) \) defined by (*), such that \( \left| {A}_{\ell }\right| = \left| {A}_{\ell }^{\prime }\right| = {i}_{\ell } \), with \( {i}_{1} + {i}_{2} + {i}_{3} = n \). For each of these partitions, there is a possible path with a probability \( {6}^{-{2n}} \) of occurring, therefore

\[
P\left( {{S}_{2n} = 0}\right)  = {6}^{-{2n}}\mathop{\sum }\limits_{{i + j + k = n}}\left( \begin{matrix} {2n} \\  i, i, j, j, k, k \end{matrix}\right)  = {6}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \mathop{\sum }\limits_{{i + j + k = n}}{\left( \begin{matrix} n \\  i, j, k \end{matrix}\right) }^{2}.
\]

Or on a

> However, we have

\[
\mathop{\sum }\limits_{{i + j + k = n}}{\left( \begin{matrix} n \\  i, j, k \end{matrix}\right) }^{2} \leq  {M}_{n}\mathop{\sum }\limits_{{i + j + k = n}}\left( \begin{matrix} n \\  i, j, k \end{matrix}\right)  = {3}^{n}{M}_{n},\;\text{ où }\;{M}_{n} = \mathop{\max }\limits_{{i + j + k = n}}\left( \begin{matrix} n \\  i, j, k \end{matrix}\right) .
\]

On va estimer \( {M}_{n} \) . Supposons d’abord que \( n \) soit divisible par 3, de sorte que \( n = {3q} \) avec \( q \in {\mathbb{N}}^{ * } \) . Si \( i + j + k = n = {3q} \) et \( \left( {i, j, k}\right) \neq \left( {q, q, q}\right) \) , l’un des indices \( i, j, k \) est \( < q \) et un autre est \( > q \) , par exemple \( i < q < j \) (notons que \( i, j \) et \( k \) jouent un role symétrique), donc

> We will estimate \( {M}_{n} \). First, assume that \( n \) is divisible by 3, so that \( n = {3q} \) with \( q \in {\mathbb{N}}^{ * } \). If \( i + j + k = n = {3q} \) and \( \left( {i, j, k}\right) \neq \left( {q, q, q}\right) \), one of the indices \( i, j, k \) is \( < q \) and another is \( > q \), for example \( i < q < j \) (note that \( i, j \) and \( k \) play a symmetric role), therefore

\[
\left( \begin{matrix} n \\  i, j, k \end{matrix}\right)  = \frac{i + 1}{j}\left( \begin{matrix} n \\  i + 1, j - 1, k \end{matrix}\right)  < \left( \begin{matrix} n \\  i + 1, j - 1, k \end{matrix}\right)  \leq  {M}_{n}.
\]

Ainsi le maximum recherché est atteint lorsque \( \left( {i, j, k}\right) = \left( {q, q, q}\right) \) . Donc on a, en utilisant la formule de Stirling

> Thus, the sought maximum is reached when \( \left( {i, j, k}\right) = \left( {q, q, q}\right) \). So we have, using Stirling's formula

\[
{M}_{n} = \left( \begin{matrix} {3q} \\  q, q, q \end{matrix}\right)  = \frac{\left( {3q}\right) !}{{\left( q!\right) }^{3}} \sim  \sqrt{6q\pi }{\left( \frac{3q}{e}\right) }^{3q}{\left\lbrack  {\left( \frac{1}{\sqrt{2q\pi }}\frac{e}{q}\right) }^{q}\right\rbrack  }^{3} = \frac{{3}^{n + 3/2}}{2n\pi } = O\left( \frac{{3}^{n}}{n}\right) .
\]

Pour traiter le cas où \( n > 3 \) n’est pas divisible par 3, on écrit \( n = {3q} + r \) avec \( r \in \{ 1,2\} \) . Lorsque \( i \leq j \leq k \) , on a \( k \geq q + 1 \) et l’inégalité

> To handle the case where \( n > 3 \) is not divisible by 3, we write \( n = {3q} + r \) with \( r \in \{ 1,2\} \). When \( i \leq j \leq k \), we have \( k \geq q + 1 \) and the inequality

\[
\left( \begin{matrix} {3q} + r \\  i, j, k \end{matrix}\right)  = \left( {\mathop{\prod }\limits_{{i = 1}}^{r}\frac{{3q} + i}{k - i + 1}}\right) \left( \begin{matrix} {3q} \\  i, j, k - r \end{matrix}\right)  \leq  \left( {\mathop{\prod }\limits_{{i = 1}}^{r}\frac{{3q} + i}{q}}\right) {M}_{3q} \leq  {20}{M}_{3q}
\]

montre que \( {M}_{n} = O\left( {{3}^{n}/n}\right) \) dans tous les cas. On en déduit

> shows that \( {M}_{n} = O\left( {{3}^{n}/n}\right) \) in all cases. We deduce from this

\[
P\left( {{S}_{2n} = 0}\right)  \leq  {6}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) {3}^{n}{M}_{n} = O\left( {{6}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \frac{{3}^{2n}}{n}}\right)  = O\left( {{2}^{-{2n}}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \frac{1}{n}}\right)  = O\left( \frac{1}{{n}^{3/2}}\right) .
\]

Donc \( \sum P\left( {{S}_{2n} = 0}\right) \) converge, et d’après la question précédente, \( \left( {S}_{n}\right) \) est transitoire.

> Therefore \( \sum P\left( {{S}_{2n} = 0}\right) \) converges, and according to the previous question, \( \left( {S}_{n}\right) \) is transient.

3/a) Le nombre total de chemins de longueur \( n \) est \( {\left( 2d\right) }^{n} \) , donc \( 0 \leq {c}_{n}^{\left( d\right) }/n! \leq {\left( 2d\right) }^{n}/n! \) , donc \( {\Phi }_{d}\left( z\right) \) a un rayon de convergence infini. Lorsque \( d = 1 \) , on a vu plus haut que le nombre de boucles de longueur \( n \) est égal à \( \left( \begin{matrix} {2m} \\ m \end{matrix}\right) \) si \( n = {2m} \) est pair,égal à0si \( n \) est impair. Donc

> 3/a) The total number of paths of length \( n \) is \( {\left( 2d\right) }^{n} \) , so \( 0 \leq {c}_{n}^{\left( d\right) }/n! \leq {\left( 2d\right) }^{n}/n! \) , therefore \( {\Phi }_{d}\left( z\right) \) has an infinite radius of convergence. When \( d = 1 \) , we saw above that the number of loops of length \( n \) is equal to \( \left( \begin{matrix} {2m} \\ m \end{matrix}\right) \) if \( n = {2m} \) is even, equal to 0 if \( n \) is odd. Therefore

\[
{\Phi }_{1}\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( \begin{matrix} {2n} \\  n \end{matrix}\right) \frac{{z}^{2n}}{\left( {2n}\right) !} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{2n}}{{\left( n!\right) }^{2}}.
\]

Prouvons maintenant \( {\Phi }_{d} = {\Phi }_{1}^{d} \) . Pour cela il suffit de prouver \( {\Phi }_{d} = {\Phi }_{1}{\Phi }_{d - 1} \) pour tout \( d \geq 2 \) . Notons \( {\mathcal{B}}_{n}^{\left( d\right) } \) l’ensemble des boucles de longueur \( n \) dans \( {\mathbb{Z}}^{d} \) . Soit \( C = \left( {C}_{k}\right) \in {\mathcal{B}}_{n}^{\left( d\right) } \) . Soit \( A = \{ k \in \; \left. {\left\{ {1,\ldots , n}\right\} \mid {C}_{k} - {C}_{k - 1} \in \left\{ {-{e}_{d},{e}_{d}}\right\} }\right\} \) et \( m = \left| A\right| \) . Notons \( \{ 1,\ldots , n\} \smallsetminus A = \left\{ {{k}_{1},\ldots ,{k}_{n - m}}\right\} \) avec \( {k}_{1} < \ldots < {k}_{n - m} \) et \( A = \left\{ {{\ell }_{1},\ldots ,{\ell }_{m}}\right\} \) avec \( {\ell }_{1} < \ldots < {\ell }_{m} \) . Pour tout \( k \) notons \( {C}_{k} = \left( {{C}_{k}^{\prime },{C}_{k}^{\prime \prime }}\right) \) avec \( {C}_{k}^{\prime } \in {\mathbb{Z}}^{d - 1} \) les \( d - 1 \) premières coordonnées de \( {C}_{k} \) , et \( {C}_{k}^{\prime \prime } \in \mathbb{Z} \) la dernière coordonnée de \( {C}_{k} \) . Les chemins \( {C}^{\prime } = {\left( {C}_{{k}_{i}}^{\prime }\right) }_{1 \leq i \leq n - m} \) et \( {C}^{\prime \prime } = {\left( {C}_{{\ell }_{j}}^{\prime \prime }\right) }_{1 \leq j \leq m} \) vérifient \( {C}^{\prime } \in {\mathcal{B}}_{n - m}^{\left( d - 1\right) } \) et \( {C}^{\prime \prime } \in {\mathcal{B}}_{m}^{\left( 1\right) } \) . L’application \( C \mapsto \left( {A,{C}^{\prime },{C}^{\prime \prime }}\right) \) définit ainsi une bijection de \( {\mathcal{B}}_{n}^{\left( d\right) } \) vers \( { \cup }_{A \subset \{ 1,\ldots , n\} }\{ A\} \times {\mathcal{B}}_{n - \left| A\right| }^{\left( d - 1\right) } \times {\mathcal{B}}_{\left| A\right| }^{\left( 1\right) } \) . Donc

> Let us now prove \( {\Phi }_{d} = {\Phi }_{1}^{d} \). To do this, it suffices to prove \( {\Phi }_{d} = {\Phi }_{1}{\Phi }_{d - 1} \) for all \( d \geq 2 \). Let \( {\mathcal{B}}_{n}^{\left( d\right) } \) denote the set of loops of length \( n \) in \( {\mathbb{Z}}^{d} \). Let \( C = \left( {C}_{k}\right) \in {\mathcal{B}}_{n}^{\left( d\right) } \). Let \( A = \{ k \in \; \left. {\left\{ {1,\ldots , n}\right\} \mid {C}_{k} - {C}_{k - 1} \in \left\{ {-{e}_{d},{e}_{d}}\right\} }\right\} \) and \( m = \left| A\right| \). Let \( \{ 1,\ldots , n\} \smallsetminus A = \left\{ {{k}_{1},\ldots ,{k}_{n - m}}\right\} \) with \( {k}_{1} < \ldots < {k}_{n - m} \) and \( A = \left\{ {{\ell }_{1},\ldots ,{\ell }_{m}}\right\} \) with \( {\ell }_{1} < \ldots < {\ell }_{m} \). For all \( k \), let \( {C}_{k} = \left( {{C}_{k}^{\prime },{C}_{k}^{\prime \prime }}\right) \) with \( {C}_{k}^{\prime } \in {\mathbb{Z}}^{d - 1} \) be the first \( d - 1 \) coordinates of \( {C}_{k} \), and \( {C}_{k}^{\prime \prime } \in \mathbb{Z} \) be the last coordinate of \( {C}_{k} \). The paths \( {C}^{\prime } = {\left( {C}_{{k}_{i}}^{\prime }\right) }_{1 \leq i \leq n - m} \) and \( {C}^{\prime \prime } = {\left( {C}_{{\ell }_{j}}^{\prime \prime }\right) }_{1 \leq j \leq m} \) satisfy \( {C}^{\prime } \in {\mathcal{B}}_{n - m}^{\left( d - 1\right) } \) and \( {C}^{\prime \prime } \in {\mathcal{B}}_{m}^{\left( 1\right) } \). The map \( C \mapsto \left( {A,{C}^{\prime },{C}^{\prime \prime }}\right) \) thus defines a bijection from \( {\mathcal{B}}_{n}^{\left( d\right) } \) to \( { \cup }_{A \subset \{ 1,\ldots , n\} }\{ A\} \times {\mathcal{B}}_{n - \left| A\right| }^{\left( d - 1\right) } \times {\mathcal{B}}_{\left| A\right| }^{\left( 1\right) } \). Therefore

\[
{c}_{n}^{\left( d\right) } = \mathop{\sum }\limits_{{m = 0}}^{n}\mathop{\sum }\limits_{{A \subset  \{ 1,\ldots , n\} ,\left| A\right|  = m}}{c}_{n - m}^{\left( d - 1\right) }{c}_{m}^{\left( 1\right) } = \mathop{\sum }\limits_{{m = 0}}^{n}\left( \begin{matrix} n \\  m \end{matrix}\right) {c}_{n - m}^{\left( d - 1\right) }{c}_{m}^{\left( 1\right) }.
\]

On récrit cette identité sous la forme \( \frac{{c}_{n}^{\left( d\right) }}{n!} = \mathop{\sum }\limits_{{m = 0}}^{n}\frac{{c}_{m}^{\left( 1\right) }}{m!}\frac{{c}_{n - m}^{\left( d - 1\right) }}{\left( {n - m}\right) !} \) . On reconnaît un produit de Cauchy, qui montre que \( {\Phi }_{d}\left( z\right) = {\Phi }_{1}\left( z\right) {\Phi }_{d - 1}\left( z\right) \) , et le résultat est prouvé.

> We rewrite this identity in the form \( \frac{{c}_{n}^{\left( d\right) }}{n!} = \mathop{\sum }\limits_{{m = 0}}^{n}\frac{{c}_{m}^{\left( 1\right) }}{m!}\frac{{c}_{n - m}^{\left( d - 1\right) }}{\left( {n - m}\right) !} \). We recognize a Cauchy product, which shows that \( {\Phi }_{d}\left( z\right) = {\Phi }_{1}\left( z\right) {\Phi }_{d - 1}\left( z\right) \), and the result is proven.

b) La convergence normale du développement en série de \( {e}^{t\cos \theta } \) sur \( \theta \in \left\lbrack {0,\pi }\right\rbrack \) , entraîne

> b) The normal convergence of the series expansion of \( {e}^{t\cos \theta } \) on \( \theta \in \left\lbrack {0,\pi }\right\rbrack \) implies

\[
{I}_{0}\left( t\right)  = \frac{1}{\pi }{\int }_{0}^{\pi }\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{t}^{n}{\cos }^{n}\theta }{n!}}\right) {d\theta } = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{J}_{n}}{n!}{t}^{n},\;{J}_{n} = \frac{1}{\pi }{\int }_{0}^{\pi }{\cos }^{n}{\theta d\theta }.
\]

(**)

> Le changement de variable \( u = \pi - \theta \) donne

The change of variable \( u = \pi - \theta \) gives

\[
{\int }_{\pi /2}^{\pi }{\cos }^{n}{\theta d\theta } = {\left( -1\right) }^{n}{\int }_{0}^{\pi /2}{\cos }^{n}{udu}\;\text{ donc }\;{J}_{n} = \frac{1 + {\left( -1\right) }^{n}}{\pi }{\int }_{0}^{\pi /2}{\cos }^{n}{\theta d\theta }.
\]

Donc \( {J}_{n} = 0 \) si \( n \) est impair. Si \( n \) est pair, on reconnait,à un facteur de normalisation près, une intégrale de Wallis (c’est classique, voir le tome Analyse). Supposons \( n \) pair et \( n \geq 2 \) . En écrivant \( {\cos }^{n}\theta = {\cos }^{n - 2}\theta \left( {1 - {\sin }^{2}\theta }\right) \) puis en intégrant par parties, on trouve

> Thus \( {J}_{n} = 0 \) if \( n \) is odd. If \( n \) is even, we recognize, up to a normalization factor, a Wallis integral (this is standard, see the Analysis volume). Assume \( n \) is even and \( n \geq 2 \) . By writing \( {\cos }^{n}\theta = {\cos }^{n - 2}\theta \left( {1 - {\sin }^{2}\theta }\right) \) and then integrating by parts, we find

\[
{J}_{n} = {J}_{n - 2} - \frac{2}{\pi }{\int }_{0}^{\pi /2}{\cos }^{n - 2}\theta {\sin }^{2}{\theta d\theta } = {J}_{n - 2} + \frac{2}{\pi }{\left\lbrack  \frac{{\cos }^{n - 1}\theta }{n - 1}\sin \theta \right\rbrack  }_{0}^{\pi /2} - \frac{2}{\pi }{\int }_{0}^{\pi /2}\frac{{\cos }^{n}\theta }{n - 1}{d\theta }.
\]

Ainsi, on a \( {J}_{n} = {J}_{n - 2} - {J}_{n}/\left( {n - 1}\right) \) , donc \( {J}_{n} = \left( {\left( {n - 1}\right) /n}\right) {J}_{n - 2} \) . Comme \( {J}_{0} = 1 \) , on en déduit

> Thus, we have \( {J}_{n} = {J}_{n - 2} - {J}_{n}/\left( {n - 1}\right) \) , so \( {J}_{n} = \left( {\left( {n - 1}\right) /n}\right) {J}_{n - 2} \) . Since \( {J}_{0} = 1 \) , we deduce

\[
\forall n \in  \mathbb{N},\;{J}_{2n} = \frac{\left( {{2n} - 1}\right) \left( {{2n} - 3}\right) \cdots 1}{\left( {2n}\right) \left( {{2n} - 2}\right) \cdots 2} = \frac{\left( {2n}\right) !}{{\left( 2n\right) }^{2}{\left( 2n - 2\right) }^{2}\cdots {2}^{2}} = \frac{\left( {2n}\right) !}{{2}^{2n}{\left( n!\right) }^{2}}.
\]

On en déduit l’identité \( {I}_{0}\left( t\right) = {\Phi }_{1}\left( {t/2}\right) \) grâce à (**). Pour trouver un équivalent de \( {I}_{0}\left( t\right) \) lorsque \( t \rightarrow + \infty \) , on utilise la méthode de Laplace (voir le tome analyse), que nous instancions ici dans notre cas particulier. Soit \( \varepsilon > 0 \) (suffisamment petit pour que \( \varepsilon < 1 \) ), et \( \delta \in \rbrack 0,\pi /2\lbrack \) tel que \( 1 - {\theta }^{2}{\left( 1 + \varepsilon \right) }^{2}/2 \leq \cos \theta \leq 1 - {\theta }^{2}{\left( 1 - \varepsilon \right) }^{2}/2 \) sur \( \left\lbrack {0,\delta }\right\rbrack \) , de sorte que

> We deduce the identity \( {I}_{0}\left( t\right) = {\Phi }_{1}\left( {t/2}\right) \) thanks to (**). To find an equivalent of \( {I}_{0}\left( t\right) \) as \( t \rightarrow + \infty \) , we use Laplace's method (see the Analysis volume), which we instantiate here for our particular case. Let \( \varepsilon > 0 \) (sufficiently small so that \( \varepsilon < 1 \) ), and \( \delta \in \rbrack 0,\pi /2\lbrack \) such that \( 1 - {\theta }^{2}{\left( 1 + \varepsilon \right) }^{2}/2 \leq \cos \theta \leq 1 - {\theta }^{2}{\left( 1 - \varepsilon \right) }^{2}/2 \) on \( \left\lbrack {0,\delta }\right\rbrack \) , so that

\[
{\int }_{0}^{\delta }{e}^{t - t{\theta }^{2}{\left( 1 + \varepsilon \right) }^{2}/2}{d\theta } \leq  {\int }_{0}^{\delta }{e}^{t\cos \theta }{d\theta } \leq  {\int }_{0}^{\delta }{e}^{t - t{\theta }^{2}{\left( 1 - \varepsilon \right) }^{2}/2}{d\theta }.
\]

(***)

> Le changement de variable \( u = \sqrt{t}\theta \left( {1 + \varepsilon }\right) \) donne, pour la première intégrale

The change of variable \( u = \sqrt{t}\theta \left( {1 + \varepsilon }\right) \) gives, for the first integral

\[
{\int }_{0}^{\delta }{e}^{t - t{\theta }^{2}{\left( 1 + \varepsilon \right) }^{2}/2}{d\theta } = \frac{{e}^{t}}{\sqrt{t}\left( {1 + \varepsilon }\right) }{\int }_{0}^{\delta \sqrt{t}\left( {1 + \varepsilon }\right) }{e}^{-{u}^{2}/2}{du} \sim  \frac{I{e}^{t}}{\sqrt{t}\left( {1 + \varepsilon }\right) },\;I = {\int }_{0}^{+\infty }{e}^{-{u}^{2}/2}{du}.
\]

De même, la dernière intégrale de (***) est équivalente à \( I{e}^{t}/\left( {\sqrt{t}\left( {1 - \varepsilon }\right) }\right) \) lorsque \( t \rightarrow + \infty \) . Donc

> Similarly, the last integral of (***) is equivalent to \( I{e}^{t}/\left( {\sqrt{t}\left( {1 - \varepsilon }\right) }\right) \) as \( t \rightarrow + \infty \) . Therefore

\[
\exists {T}_{0} > 0,\forall t > {T}_{0},\;\frac{I{e}^{t}}{\sqrt{t}}\frac{1}{{\left( 1 + \varepsilon \right) }^{2}} \leq  {\int }_{0}^{\delta }{e}^{t\cos \theta }{d\theta } \leq  \frac{I{e}^{t}}{\sqrt{t}}\frac{1}{{\left( 1 - \varepsilon \right) }^{2}}.
\]

Comme \( \left| {{\int }_{\delta }^{\pi }{e}^{t\cos \theta }{d\theta }}\right| \leq \pi {e}^{\alpha t} \) avec \( \alpha = \cos \delta < 1 \) , on en déduit l’existence de \( {T}_{1} > {T}_{0} \) tel que \( \left| {{\int }_{\delta }^{\pi }{e}^{t\cos \theta }{d\theta }}\right| \leq \varepsilon {e}^{t}/\sqrt{t} \) pour \( t > {T}_{1} \) . On a donc

> Since \( \left| {{\int }_{\delta }^{\pi }{e}^{t\cos \theta }{d\theta }}\right| \leq \pi {e}^{\alpha t} \) with \( \alpha = \cos \delta < 1 \) , we deduce the existence of \( {T}_{1} > {T}_{0} \) such that \( \left| {{\int }_{\delta }^{\pi }{e}^{t\cos \theta }{d\theta }}\right| \leq \varepsilon {e}^{t}/\sqrt{t} \) for \( t > {T}_{1} \) . We therefore have

\[
\forall t > {T}_{1},\;\frac{1}{\pi }\frac{{e}^{t}}{\sqrt{t}}\frac{I - \varepsilon }{{\left( 1 + \varepsilon \right) }^{2}} \leq  {I}_{0}\left( t\right)  \leq  \frac{1}{\pi }\frac{{e}^{t}}{\sqrt{t}}\frac{I + \varepsilon }{{\left( 1 - \varepsilon \right) }^{2}}.
\]

Comme ceci est possible pour tout \( \varepsilon > 0 \) , on en déduit \( {I}_{0}\left( t\right) \sim \left( {I/\pi }\right) {e}^{t}/\sqrt{t} \) .

> As this is possible for any \( \varepsilon > 0 \) , we deduce \( {I}_{0}\left( t\right) \sim \left( {I/\pi }\right) {e}^{t}/\sqrt{t} \) .

c) Le comportement de \( {I}_{0}\left( t\right) \) obtenu précédemment entraîne \( {I}_{0}{\left( tx/d\right) }^{d} = O\left( {e}^{tx}\right) \) , donc donc si \( \left| x\right| < 1 \) l’intégrale \( {\int }_{0}^{+\infty }{I}_{0}{\left( tx/d\right) }^{d}{e}^{-t}{dt} \) converge bien. Par ailleurs, si \( \left| x\right| < 1 \) , on a

> c) The behavior of \( {I}_{0}\left( t\right) \) obtained previously leads to \( {I}_{0}{\left( tx/d\right) }^{d} = O\left( {e}^{tx}\right) \) , so if \( \left| x\right| < 1 \) the integral \( {\int }_{0}^{+\infty }{I}_{0}{\left( tx/d\right) }^{d}{e}^{-t}{dt} \) indeed converges. Furthermore, if \( \left| x\right| < 1 \) , we have

\[
{\int }_{0}^{+\infty }{I}_{0}{\left( \frac{tx}{d}\right) }^{d}{e}^{-t}{dt} = {\int }_{0}^{+\infty }{\Phi }_{d}\left( \frac{tx}{2d}\right) {e}^{-t}{dt} = {\int }_{0}^{+\infty }\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{c}_{n}^{\left( d\right) }}{{\left( 2d\right) }^{n}n!}{t}^{n}{x}^{n}}\right) {e}^{-t}{dt}.
\]

Comme \( \left| x\right| < 1 \) , et que \( 0 \leq {c}_{n}^{\left( d\right) } \leq {\left( 2d\right) }^{n} \) , on a

> Since \( \left| x\right| < 1 \) , and that \( 0 \leq {c}_{n}^{\left( d\right) } \leq {\left( 2d\right) }^{n} \) , we have

\[
\forall N \in  \mathbb{N},\forall t \in  {\mathbb{R}}^{ + },\;\left| {\mathop{\sum }\limits_{{n = 0}}^{N}\frac{{c}_{n}^{\left( d\right) }}{{\left( 2d\right) }^{n}n!}{t}^{n}{x}^{n}}\right| {e}^{-t} \leq  \left| {\mathop{\sum }\limits_{{n = 0}}^{N}\frac{{x}^{n}}{n!}{t}^{n}}\right| {e}^{-t} \leq  {e}^{\left| x\right| t}{e}^{-t} = {e}^{\left( {\left| x\right|  - 1}\right) t},
\]

on peut donc appliquer le théorème de convergence dominée qui nous autorise à intervertir les signes de sommations, ce qui fournit

> we can therefore apply the dominated convergence theorem which allows us to interchange the summation signs, which provides

\[
{\int }_{0}^{+\infty }{I}_{0}{\left( \frac{tx}{d}\right) }^{d}{e}^{-t}{dt} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{c}_{n}^{\left( d\right) }}{{\left( 2d\right) }^{n}n!}{x}^{n}{K}_{n},\;{K}_{n} = {\int }_{0}^{+\infty }{t}^{n}{e}^{-t}{dt}.
\]

Une intégration par partie fournit facilement \( {K}_{n}/n = {K}_{n - 1} \) lorsque \( n \in {\mathbb{N}}^{ * } \) , donc \( {K}_{n} = n \) !. Par ailleurs, comme nous sommes dans le cas isotrope, on a \( P\left( {{S}_{n} = 0}\right) = {c}_{n}^{\left( d\right) }/{\left( 2d\right) }^{n} \) . On en déduit bien \( {\int }_{0}^{+\infty }{I}_{0}{\left( tx/d\right) }^{d}{e}^{-t}{dt} = \varphi \left( x\right) \) .

> Integration by parts easily provides \( {K}_{n}/n = {K}_{n - 1} \) when \( n \in {\mathbb{N}}^{ * } \) , so \( {K}_{n} = n \) !. Furthermore, as we are in the isotropic case, we have \( P\left( {{S}_{n} = 0}\right) = {c}_{n}^{\left( d\right) }/{\left( 2d\right) }^{n} \) . We thus deduce \( {\int }_{0}^{+\infty }{I}_{0}{\left( tx/d\right) }^{d}{e}^{-t}{dt} = \varphi \left( x\right) \) .

Supposons maintenant \( d \geq 3 \) . D’après la question précédente, il existe \( C > 0 \) tel que \( {I}_{0}\left( u\right) \leq \; C{e}^{u}/{u}^{1/2} \) pour tout \( u > 0 \) . Donc pour tout \( x \in \left\lbrack {1/2,1\lbrack }\right. \) on a \( {I}_{0}{\left( tx/d\right) }^{d}{e}^{-t} \leq D{e}^{t\left( {x - 1}\right) }{t}^{-d/2} \leq \; D{t}^{-d/2} \) avec \( D = {C}^{d}{\left( 2d\right) }^{d/2} \) . Comme \( d \geq 3, M = {\int }_{0}^{+\infty }D{t}^{-d/2}{dt} \) existe bien et on a \( \varphi \left( x\right) \leq M \) sur \( \lbrack 1/2,1\lbrack \) . Pour tout \( N \in {\mathbb{N}}^{ * } \) , on a donc \( \mathop{\sum }\limits_{{n = 0}}^{N}P\left( {{S}_{n} = 0}\right) {x}^{n} \leq \varphi \left( x\right) \leq M \) donc en faisant \( x \rightarrow 1 \) on en déduit \( \mathop{\sum }\limits_{{n = 0}}^{N}P\left( {{S}_{n} = 0}\right) \leq M \) . Ceci est vrai pour tout \( N \) , donc \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) converge. Ainsi, lorsque \( d \geq 3,\left( {S}_{n}\right) \) est transitoire d’après la question \( 1/ \) .

> Now suppose \( d \geq 3 \) . According to the previous question, there exists \( C > 0 \) such that \( {I}_{0}\left( u\right) \leq \; C{e}^{u}/{u}^{1/2} \) for all \( u > 0 \) . So for all \( x \in \left\lbrack {1/2,1\lbrack }\right. \) we have \( {I}_{0}{\left( tx/d\right) }^{d}{e}^{-t} \leq D{e}^{t\left( {x - 1}\right) }{t}^{-d/2} \leq \; D{t}^{-d/2} \) with \( D = {C}^{d}{\left( 2d\right) }^{d/2} \) . Since \( d \geq 3, M = {\int }_{0}^{+\infty }D{t}^{-d/2}{dt} \) exists and we have \( \varphi \left( x\right) \leq M \) on \( \lbrack 1/2,1\lbrack \) . For all \( N \in {\mathbb{N}}^{ * } \) , we therefore have \( \mathop{\sum }\limits_{{n = 0}}^{N}P\left( {{S}_{n} = 0}\right) {x}^{n} \leq \varphi \left( x\right) \leq M \) so by letting \( x \rightarrow 1 \) we deduce \( \mathop{\sum }\limits_{{n = 0}}^{N}P\left( {{S}_{n} = 0}\right) \leq M \) . This is true for all \( N \) , so \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) converges. Thus, when \( d \geq 3,\left( {S}_{n}\right) \) is transient according to question \( 1/ \) .

Lorsque \( d \leq 2 \) , montrons que \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverge. On raisonne par l’absurde en supposant que \( M = \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{S}_{n} = 0}\right) \) existe. L’intégrande étant positive, on en déduit, pour tout \( T > 0 \)

> When \( d \leq 2 \) , let us show that \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverges. We reason by contradiction by assuming that \( M = \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {{S}_{n} = 0}\right) \) exists. Since the integrand is positive, we deduce that, for all \( T > 0 \)

\[
\forall x \in  \left\lbrack  {0,1\left\lbrack  {\;{\int }_{0}^{T}{I}_{0}{\left( \frac{tx}{d}\right) }^{d}{e}^{-t}{dt} \leq  \varphi \left( x\right)  \leq  M.}\right. }\right.
\]

En faisant \( x \rightarrow 1 \) , on en déduit \( {\int }_{0}^{T}{I}_{0}{\left( \frac{t}{d}\right) }^{d}{e}^{-t}{dt} \leq M \) . Ainsi \( {\int }_{0}^{+\infty }{I}_{0}{\left( \frac{t}{d}\right) }^{d}{e}^{-t}{dt} \) converge, ce qui est impossible puisque \( {I}_{0}{\left( t/d\right) }^{d}{e}^{-t} \sim \alpha {t}^{-d/2} \) (avec \( \left. {\alpha = {\left( I{d}^{1/2}/\pi \right) }^{d}}\right) \) et \( d \leq 2 \) . Donc \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverge et \( \left( {S}_{n}\right) \) est récurrente.

> By letting \( x \rightarrow 1 \) , we deduce \( {\int }_{0}^{T}{I}_{0}{\left( \frac{t}{d}\right) }^{d}{e}^{-t}{dt} \leq M \) . Thus \( {\int }_{0}^{+\infty }{I}_{0}{\left( \frac{t}{d}\right) }^{d}{e}^{-t}{dt} \) converges, which is impossible since \( {I}_{0}{\left( t/d\right) }^{d}{e}^{-t} \sim \alpha {t}^{-d/2} \) (with \( \left. {\alpha = {\left( I{d}^{1/2}/\pi \right) }^{d}}\right) \) and \( d \leq 2 \) . Therefore \( \mathop{\sum }\limits_{n}P\left( {{S}_{n} = 0}\right) \) diverges and \( \left( {S}_{n}\right) \) is recurrent.

Remarque. Ainsi, une personne ivre revient une infinité de fois en son lieu d'origine, mais un oiseau ivre n'y revient au plus qu'un nombre fini de fois.

> Remark. Thus, a drunk person returns an infinite number of times to their point of origin, but a drunk bird returns there at most a finite number of times.

- On peut démontrer le théorème de Pólya en généralisant l'approche (dite combinatoire) du 2/b) au cas \( d > 3 \) , mais la technique est fastidieuse. Une approche plus élégante (dite analytique) consiste à estimer \( P\left( {{S}_{2n} = 0}\right) \) à partir de l’expression intégrale (*) de la remarque 18 page 348, et en utilisant des transformations d'intégrales multiples.

> - One can prove Pólya's theorem by generalizing the approach (called combinatorial) from 2/b) to the case \( d > 3 \) , but the technique is tedious. A more elegant approach (called analytical) consists of estimating \( P\left( {{S}_{2n} = 0}\right) \) from the integral expression (*) in remark 18 on page 348, and by using multiple integral transformations.

- La fonction \( {I}_{0}\left( x\right) \) définie dans \( 3/\mathrm{b}) \) est un cas particulier des fonctions de Bessel modifiées de première espèce \( {I}_{\alpha } \) , définies par \( {I}_{\alpha }\left( t\right)  = \mathop{\sum }\limits_{{n \in  \mathbb{N}}}\frac{1}{n!\left( {n + \alpha }\right) !}{\left( \frac{x}{2}\right) }^{{2n} + \alpha } \) .

> - The function \( {I}_{0}\left( x\right) \) defined in \( 3/\mathrm{b}) \) is a special case of the modified Bessel functions of the first kind \( {I}_{\alpha } \) , defined by \( {I}_{\alpha }\left( t\right)  = \mathop{\sum }\limits_{{n \in  \mathbb{N}}}\frac{1}{n!\left( {n + \alpha }\right) !}{\left( \frac{x}{2}\right) }^{{2n} + \alpha } \) .

- La formule de 3/c), permet de passer d'une série génératrice exponentielle à une série génératrice ordinaire. On l'appelle transformation de Borel.

> - The formula from 3/c) allows one to move from an exponential generating series to an ordinary generating series. It is called the Borel transform.

PROBLÉME 9 (THÉORÉME LOCAL LIMITE ET CENTRAL LIMITE). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires à valeurs dans \( \mathbb{Z} \) , indépendantes, identiquement distribuées, admettant un moment d’ordre 2. On note \( {S}_{n} = {X}_{1} + \cdots + {X}_{n}, E\left( {X}_{1}\right) = \mu \) et \( V\left( {X}_{1}\right) = {\sigma }^{2} \) (avec \( \sigma > 0 \) ). On suppose que la fonction caractéristique \( {\varphi }_{{X}_{1}} : t \mapsto E\left( {e}^{{it}{X}_{1}}\right) \) de \( {X}_{1} \) vérifie

> PROBLEM 9 (LOCAL LIMIT AND CENTRAL LIMIT THEOREM). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of independent, identically distributed random variables taking values in \( \mathbb{Z} \) , admitting a second-order moment. We denote \( {S}_{n} = {X}_{1} + \cdots + {X}_{n}, E\left( {X}_{1}\right) = \mu \) and \( V\left( {X}_{1}\right) = {\sigma }^{2} \) (with \( \sigma > 0 \) ). We assume that the characteristic function \( {\varphi }_{{X}_{1}} : t \mapsto E\left( {e}^{{it}{X}_{1}}\right) \) of \( {X}_{1} \) satisfies

\[
\forall t \in  \left\lbrack  {-\pi ,\pi }\right\rbrack   \smallsetminus  \{ 0\} ,\;\left| {{\varphi }_{{X}_{1}}\left( t\right) }\right|  < 1.
\]

(*)

> 1/ Montrer que \( {X}_{1} \) ne satisfait pas l’hypothèse (*) si et seulement si il existe \( a \in \mathbb{Z} \) et \( b \in \mathbb{N}, b \geq 2 \) , tels que presque surement, \( {X}_{1} \) prend ses valeurs dans \( a + b\mathbb{Z} \) .

1/ Show that \( {X}_{1} \) does not satisfy hypothesis (*) if and only if there exist \( a \in \mathbb{Z} \) and \( b \in \mathbb{N}, b \geq 2 \) such that, almost surely, \( {X}_{1} \) takes its values in \( a + b\mathbb{Z} \) .

> 2 / a) Montrer que pour \( a \in \mathbb{R} \) , l’intégrale \( I\left( a\right) = {\int }_{-\infty }^{+\infty }{e}^{-{\left( t + ia\right) }^{2}/2}{dt} \) existe et ne dépend pas de \( a \) , puis calculer \( J\left( a\right) = {\int }_{-\infty }^{+\infty }{e}^{{iat} - {t}^{2}/2}{dt} \) (on rappelle la valeur classique \( I\left( 0\right) = \sqrt{2\pi } \) ). b) Montrer que

2 / a) Show that for \( a \in \mathbb{R} \) , the integral \( I\left( a\right) = {\int }_{-\infty }^{+\infty }{e}^{-{\left( t + ia\right) }^{2}/2}{dt} \) exists and does not depend on \( a \) , then calculate \( J\left( a\right) = {\int }_{-\infty }^{+\infty }{e}^{{iat} - {t}^{2}/2}{dt} \) (recall the classical value \( I\left( 0\right) = \sqrt{2\pi } \) ). b) Show that

\[
\forall x \in  \mathbb{Z},\;P\left( {{S}_{n} = x}\right)  = \frac{1}{2\pi }{\int }_{-\pi }^{\pi }{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt}.
\]

(**)

> c) Montrer qu’il existe une fonction \( \delta \left( t\right) \) vérifiant \( \mathop{\lim }\limits_{{t \rightarrow 0}}\delta \left( t\right) = 0 \) , et telle que

c) Show that there exists a function \( \delta \left( t\right) \) satisfying \( \mathop{\lim }\limits_{{t \rightarrow 0}}\delta \left( t\right) = 0 \) , and such that

\[
\forall t \in  \mathbb{R},\forall n \in  {\mathbb{N}}^{ * },\;\left| {{\varphi }_{{X}_{1}}{\left( t\right) }^{n} - {e}^{in\mu t}{e}^{-n{\sigma }^{2}{t}^{2}/2}}\right|  \leq  {e}^{-n{\sigma }^{2}{t}^{2}/2}\left( {{e}^{n{t}^{2}\delta \left( t\right) } - 1}\right) .
\]

d) (Théorème local limite). Montrer que lorsque \( n \rightarrow + \infty \) , on a pour tout \( x \in \mathbb{Z} \)

> d) (Local limit theorem). Show that as \( n \rightarrow + \infty \) , we have for all \( x \in \mathbb{Z} \)

\[
P\left( {{S}_{n} = x}\right)  = \frac{1}{\sqrt{{2\pi }{\sigma }^{2}n}}\exp \left( {-\frac{{\left( x - n\mu \right) }^{2}}{2{\sigma }^{2}n}}\right)  + o\left( \frac{1}{\sqrt{n}}\right) ,
\]

où le \( o\left( {1/\sqrt{n}}\right) \) ne dépend que de \( n \) (indication : remarquer que l’intégrale de \( 2/\mathrm{b} \) ) est dictée par son comportement en \( t = 0 \) , sur un intervalle de la forme \( \left\lbrack {-A/\sqrt{n}, A/\sqrt{n}}\right\rbrack ) \) . 3/ (Théorème central limite). Soit \( a, b \in \mathbb{R}, a < b \) . Montrer que

> where \( o\left( {1/\sqrt{n}}\right) \) depends only on \( n \) (hint: note that the integral of \( 2/\mathrm{b} \) ) is dictated by its behavior at \( t = 0 \) , on an interval of the form \( \left\lbrack {-A/\sqrt{n}, A/\sqrt{n}}\right\rbrack ) \) . 3/ (Central limit theorem). Let \( a, b \in \mathbb{R}, a < b \) . Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {a \leq  \frac{{S}_{n} - {n\mu }}{\sigma \sqrt{n}} \leq  b}\right)  = \frac{1}{\sqrt{2\pi }}{\int }_{a}^{b}{e}^{-{t}^{2}/2}{dt}.
\]

Solution. 1/ S’il existe \( a \in \mathbb{Z} \) et \( b \in \mathbb{N}, b \geq 2 \) , tels que presque surement \( {X}_{1} \) prend ses valeurs dans \( a + b\mathbb{Z} \) , ceci signifie que \( P\left( {X = k}\right) = 0 \) si \( k \notin a + b\mathbb{Z} \) . Donc on peut écrire

> Solution. 1/ If there exist \( a \in \mathbb{Z} \) and \( b \in \mathbb{N}, b \geq 2 \) such that almost surely \( {X}_{1} \) takes its values in \( a + b\mathbb{Z} \) , this means that \( P\left( {X = k}\right) = 0 \) if \( k \notin a + b\mathbb{Z} \) . Thus we can write

\[
{\varphi }_{{X}_{1}}\left( {{2\pi }/b}\right)  = \mathop{\sum }\limits_{{k \in  \mathbb{Z}}}P\left( {X = a + {bk}}\right) {e}^{i\left( {{2\pi }/b}\right) \left( {a + {bk}}\right) } = {e}^{{2i\pi a}/b}\mathop{\sum }\limits_{{k \in  \mathbb{Z}}}P\left( {X = a + {bk}}\right)  = {e}^{{2i\pi a}/b}{\varphi }_{{X}_{1}}\left( 0\right)
\]

donc \( \left| {{\varphi }_{{X}_{1}}\left( {{2\pi }/b}\right) }\right| = \left| {{\varphi }_{{X}_{1}}\left( 0\right) }\right| = 1 \) , et comme \( b \geq 2 \) on a démontré la condition suffisante.

> therefore \( \left| {{\varphi }_{{X}_{1}}\left( {{2\pi }/b}\right) }\right| = \left| {{\varphi }_{{X}_{1}}\left( 0\right) }\right| = 1 \) , and since \( b \geq 2 \) we have proven the sufficient condition.

Réciproquement supposons qu’il existe \( \beta \in \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \{ 0\} \) tel que \( \left| {{\varphi }_{{X}_{1}}\left( \beta \right) }\right| = 1 \) . On peut supposer \( \beta > 0 \) car \( {\varphi }_{{X}_{1}}\left( \beta \right) \) et \( {\varphi }_{{X}_{1}}\left( {-\beta }\right) \) sont conjugués. Soit \( \alpha \in \mathbb{R} \) tel que \( {\varphi }_{{X}_{1}}\left( \beta \right) = {e}^{i\alpha } \) . On a

> Conversely, assume there exists \( \beta \in \left\lbrack {-\pi ,\pi }\right\rbrack \smallsetminus \{ 0\} \) such that \( \left| {{\varphi }_{{X}_{1}}\left( \beta \right) }\right| = 1 \) . We can assume \( \beta > 0 \) because \( {\varphi }_{{X}_{1}}\left( \beta \right) \) and \( {\varphi }_{{X}_{1}}\left( {-\beta }\right) \) are conjugates. Let \( \alpha \in \mathbb{R} \) such that \( {\varphi }_{{X}_{1}}\left( \beta \right) = {e}^{i\alpha } \) . We have

\[
1 = {e}^{-{i\alpha }}{\varphi }_{{X}_{1}}\left( \beta \right)  = \mathop{\sum }\limits_{{k \in  \mathbb{Z}}}P\left( {{X}_{1} = k}\right) {e}^{i\left( {{k\beta } - \alpha }\right) } = \mathop{\sum }\limits_{{k \in  \mathbb{Z}}}P\left( {{X}_{1} = k}\right) \cos \left( {{\beta k} - \alpha }\right) .
\]

Comme \( \mathop{\sum }\limits_{{k \in \mathbb{Z}}}P\left( {{X}_{1} = k}\right) = 1 \) , on doit forcément avoir \( \cos \left( {{\beta k} - \alpha }\right) = 1 \) pour tout \( k \) tel que \( P\left( {{X}_{1} = k}\right) > 0 \) . Pour ces valeurs de \( k \) on a donc \( {\beta k} - \alpha \in {2\pi }\mathbb{Z} \) , ou encore \( k \in c + d\mathbb{Z} \) avec \( c = \alpha /\beta \) et \( d = {2\pi }/\beta \) . Fixons \( {k}_{0} \in \mathbb{Z} \) tel que \( P\left( {{X}_{1} = {k}_{0}}\right) > 0 \) . Pour \( k \in \mathbb{Z}, k \neq {k}_{0} \) tel que \( P\left( {{X}_{1} = k}\right) > 0 \) on a \( k - {k}_{0} \in d\mathbb{Z} \) donc \( d = p/q \in \mathbb{Q} \) , avec \( p, q \in {\mathbb{N}}^{ * } \) et \( p \land q = 1 \) . Comme \( k - {k}_{0} \in d\mathbb{Z} \) , il existe \( \ell \in \mathbb{Z} \) tel que \( k - {k}_{0} = \left( {p/q}\right) \ell \) , donc \( q\left( {k - {k}_{0}}\right) = p\ell \) , et comme \( p \land q = 1 \) ceci implique \( q \mid \ell \) . Finalement on a donc \( k - {k}_{0} = p\left( {\ell /q}\right) \in p\mathbb{Z} \) . Donc \( k \in {k}_{0} + p\mathbb{Z} \) . On en déduit le résultat avec \( a = {k}_{0} \) et \( b = p \) . On a bien \( b \geq 2 \) car \( p \geq d = {2\pi }/\beta \geq 2 \) .

> As \( \mathop{\sum }\limits_{{k \in \mathbb{Z}}}P\left( {{X}_{1} = k}\right) = 1 \), we must necessarily have \( \cos \left( {{\beta k} - \alpha }\right) = 1 \) for all \( k \) such that \( P\left( {{X}_{1} = k}\right) > 0 \). For these values of \( k \), we therefore have \( {\beta k} - \alpha \in {2\pi }\mathbb{Z} \), or \( k \in c + d\mathbb{Z} \) with \( c = \alpha /\beta \) and \( d = {2\pi }/\beta \). Let us fix \( {k}_{0} \in \mathbb{Z} \) such that \( P\left( {{X}_{1} = {k}_{0}}\right) > 0 \). For \( k \in \mathbb{Z}, k \neq {k}_{0} \) such that \( P\left( {{X}_{1} = k}\right) > 0 \), we have \( k - {k}_{0} \in d\mathbb{Z} \), thus \( d = p/q \in \mathbb{Q} \), with \( p, q \in {\mathbb{N}}^{ * } \) and \( p \land q = 1 \). Since \( k - {k}_{0} \in d\mathbb{Z} \), there exists \( \ell \in \mathbb{Z} \) such that \( k - {k}_{0} = \left( {p/q}\right) \ell \), thus \( q\left( {k - {k}_{0}}\right) = p\ell \), and since \( p \land q = 1 \), this implies \( q \mid \ell \). Finally, we have \( k - {k}_{0} = p\left( {\ell /q}\right) \in p\mathbb{Z} \). Thus \( k \in {k}_{0} + p\mathbb{Z} \). We deduce the result with \( a = {k}_{0} \) and \( b = p \). We indeed have \( b \geq 2 \) because \( p \geq d = {2\pi }/\beta \geq 2 \).

2/a) Pour tout \( a \in \mathbb{R} \) , l’intégrale \( I\left( a\right) \) est bien définie car \( \left| {e}^{-{\left( t + ia\right) }^{2}/2}\right| = {e}^{{a}^{2}/2}{e}^{-{t}^{2}/2} \) . La suite de fonctions \( {I}_{n} : a \mapsto {\int }_{-n}^{n}{e}^{-{\left( t + ia\right) }^{2}/2}{dt} \) converge simplement vers \( I \) , et la théorème de dérivation sous le signe intégral nous permet d’assurer la dérivabilité de \( {I}_{n} \) et la formule

> 2/a) For all \( a \in \mathbb{R} \), the integral \( I\left( a\right) \) is well-defined because \( \left| {e}^{-{\left( t + ia\right) }^{2}/2}\right| = {e}^{{a}^{2}/2}{e}^{-{t}^{2}/2} \). The sequence of functions \( {I}_{n} : a \mapsto {\int }_{-n}^{n}{e}^{-{\left( t + ia\right) }^{2}/2}{dt} \) converges pointwise to \( I \), and the theorem of differentiation under the integral sign allows us to ensure the differentiability of \( {I}_{n} \) and the formula

\[
{I}_{n}^{\prime }\left( a\right)  =  - i{\int }_{-n}^{n}\left( {t + {ia}}\right) {e}^{-{\left( t + ia\right) }^{2}/2}{dt} = i{\left\lbrack  {e}^{-{\left( t + ia\right) }^{2}/2}\right\rbrack  }_{-n}^{n} = i{e}^{{a}^{2}/2}{e}^{-{n}^{2}/2}\cos \left( {na}\right) .
\]

Sur tout segment \( \left\lbrack {-K, K}\right\rbrack \) de \( \mathbb{R} \) ceci entraîne \( \left| {{I}_{n}^{\prime }\left( a\right) }\right| \leq 2{e}^{{K}^{2}/2}{e}^{-{n}^{2}/2} \) , donc la suite de fonctions \( \left( {{I}_{n}^{\prime }\left( a\right) }\right) \) converge uniformément vers0sur ce segment. Donc \( I\left( a\right) \) est dérivable sur tout segment \( \left\lbrack {-K, K}\right\rbrack \) de \( \mathbb{R} \) , donc sur \( \mathbb{R} \) tout entier, et \( {I}^{\prime }\left( a\right) = 0 \) . Ainsi \( I\left( a\right) = I\left( 0\right) \) ce qui entraîne

> On any segment \( \left\lbrack {-K, K}\right\rbrack \) of \( \mathbb{R} \) this implies \( \left| {{I}_{n}^{\prime }\left( a\right) }\right| \leq 2{e}^{{K}^{2}/2}{e}^{-{n}^{2}/2} \) , therefore the sequence of functions \( \left( {{I}_{n}^{\prime }\left( a\right) }\right) \) converges uniformly to 0 on this segment. Thus \( I\left( a\right) \) is differentiable on any segment \( \left\lbrack {-K, K}\right\rbrack \) of \( \mathbb{R} \) , and therefore on \( \mathbb{R} \) in its entirety, and \( {I}^{\prime }\left( a\right) = 0 \) . Thus \( I\left( a\right) = I\left( 0\right) \) which implies

\[
J\left( a\right)  = {\int }_{-\infty }^{+\infty }{e}^{-{t}^{2}/2 + {iat}}{dt} = {e}^{-{a}^{2}/2}{\int }_{-\infty }^{+\infty }{e}^{-{\left( t + ia\right) }^{2}/2}{dt} = {e}^{-{a}^{2}/2}I\left( a\right)  = \sqrt{2\pi }{e}^{-{a}^{2}/2}.
\]

b) Compte tenu de l’indépendance des \( {X}_{k} \) , la fonction caractéristique de \( {S}_{n} \) vérifie \( {\varphi }_{{S}_{n}}\left( t\right) = \; {\varphi }_{{X}_{1}}\left( t\right) \cdots {\varphi }_{{X}_{n}}\left( t\right) = {\left( {\varphi }_{{X}_{1}}\left( t\right) \right) }^{n} \) . On conclut avec la formule de la remarque 18 page 348.

> b) Given the independence of the \( {X}_{k} \) , the characteristic function of \( {S}_{n} \) satisfies \( {\varphi }_{{S}_{n}}\left( t\right) = \; {\varphi }_{{X}_{1}}\left( t\right) \cdots {\varphi }_{{X}_{n}}\left( t\right) = {\left( {\varphi }_{{X}_{1}}\left( t\right) \right) }^{n} \) . We conclude with the formula from remark 18 on page 348.

c) Comme \( {X}_{1} \) admet un moment d’ordre \( 2,{\varphi }_{{X}_{1}} \) est de classe \( {\mathcal{C}}^{2} \) et on a, lorsque \( t \rightarrow 0 \)

> c) As \( {X}_{1} \) admits a moment of order \( 2,{\varphi }_{{X}_{1}} \) is of class \( {\mathcal{C}}^{2} \) and we have, when \( t \rightarrow 0 \)

\[
{\varphi }_{{X}_{1}}\left( t\right)  = {\varphi }_{{X}_{1}}\left( 0\right)  + {\varphi }_{{X}_{1}}^{\prime }\left( 0\right) t + \frac{{\varphi }_{{X}_{1}}^{\prime \prime }\left( 0\right) }{2}{t}^{2} + o\left( {t}^{2}\right)  = 1 + {i\mu t} - \frac{{\sigma }^{2} + {\mu }^{2}}{2}{t}^{2} + o\left( {t}^{2}\right) .
\]

On a donc

> We therefore have

\[
{e}^{-{i\mu t} + {\sigma }^{2}{t}^{2}/2}{\varphi }_{{X}_{1}}\left( t\right)  = \left( {1 - {i\mu t} + \frac{{\sigma }^{2} - {\mu }^{2}}{2}{t}^{2} + o\left( {t}^{2}\right) }\right) {\varphi }_{{X}_{1}}\left( t\right)  = 1 + o\left( {t}^{2}\right)  = 1 + {t}^{2}f\left( t\right) ,
\]

avec \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) , et on a alors

> with \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) , and we then have

\[
{\varphi }_{{X}_{1}}{\left( t\right) }^{n} = {e}^{in\mu t}{e}^{-n{\sigma }^{2}{t}^{2}/2}{\left( 1 + {t}^{2}f\left( t\right) \right) }^{n},
\]

ce qui entraîne, en posant \( \delta \left( t\right) = \left| {f\left( t\right) }\right| \) ,

> which implies, by setting \( \delta \left( t\right) = \left| {f\left( t\right) }\right| \) ,

\[
\left| {{\varphi }_{{X}_{1}}{\left( t\right) }^{n} - {e}^{in\mu t}{e}^{-n{\sigma }^{2}{t}^{2}/2}}\right|  = {e}^{-n{\sigma }^{2}{t}^{2}/2}\left| {{\left( 1 + {t}^{2}f\left( t\right) \right) }^{n} - 1}\right|  \leq  {e}^{-n{\sigma }^{2}{t}^{2}/2}\left( {{e}^{n{t}^{2}\delta \left( t\right) } - 1}\right) .
\]

d) Considérons maintenant \( \varepsilon > 0 \) . Soit \( \alpha \in \rbrack 0,\pi \left\lbrack {\text{ tel que pour }t \in \left\lbrack {-\alpha ,\alpha }\right\rbrack \text{ , on ait }\delta \left( t\right) < {\sigma }^{2}/4\text{ . }}\right\rbrack \) Soit \( A > 0 \) (on verra plus tard comment choisir \( A \) ), et \( n \) suffisamment grand pour que \( A/\sqrt{n} < \alpha \) . Nous allons découper l'intégrale de 2/b) sur les domaines d'intégration

> d) Let us now consider \( \varepsilon > 0 \) . Let \( \alpha \in \rbrack 0,\pi \left\lbrack {\text{ tel que pour }t \in \left\lbrack {-\alpha ,\alpha }\right\rbrack \text{ , on ait }\delta \left( t\right) < {\sigma }^{2}/4\text{ . }}\right\rbrack \) Let \( A > 0 \) (we will see later how to choose \( A \) ), and \( n \) large enough so that \( A/\sqrt{n} < \alpha \) . We will split the integral from 2/b) over the integration domains

\[
{D}_{n} = \left\lbrack  {-\frac{A}{\sqrt{n}},\frac{A}{\sqrt{n}}}\right\rbrack  ,\;{E}_{n,\alpha } = \left\lbrack  {-\alpha , - \frac{A}{\sqrt{n}}}\right\rbrack   \cup  \left\lbrack  {\frac{A}{\sqrt{n}},\alpha }\right\rbrack  ,\;{F}_{\alpha } = \left\lbrack  {-\pi , - \alpha }\right\rbrack   \cup  \left\lbrack  {\alpha ,\pi }\right\rbrack  .
\]

L'inégalité précédente implique

> The previous inequality implies

\[
\left| {{\int }_{{D}_{n}}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt} - {\int }_{{D}_{n}}{e}^{i\left( {{n\mu } - x}\right) t}{e}^{-n{\sigma }^{2}{t}^{2}/2}{dt}}\right|  \leq  {\int }_{{D}_{n}}{e}^{-n{\sigma }^{2}{t}^{2}/2}\left( {{e}^{{A}^{2}\delta \left( t\right) } - 1}\right) {dt}.
\]

Comme \( \mathop{\lim }\limits_{{t \rightarrow 0}}\delta \left( t\right) = 0 \) , il existe \( {N}_{0} \in \mathbb{N} \) , tel que pour \( n \geq {N}_{0},\mathop{\sup }\limits_{{t \in {D}_{n}}}{e}^{{A}^{2}\delta \left( t\right) } - 1 < \varepsilon \) , donc pour \( n \geq {N}_{0} \) , on en déduit, après avoir fait le changement de variable \( t = u/\left( {\sigma \sqrt{n}}\right) \) dans ces deux dernières intégrales,

> As \( \mathop{\lim }\limits_{{t \rightarrow 0}}\delta \left( t\right) = 0 \) , there exists \( {N}_{0} \in \mathbb{N} \) , such that for \( n \geq {N}_{0},\mathop{\sup }\limits_{{t \in {D}_{n}}}{e}^{{A}^{2}\delta \left( t\right) } - 1 < \varepsilon \) , therefore for \( n \geq {N}_{0} \) , we deduce from this, after having performed the change of variable \( t = u/\left( {\sigma \sqrt{n}}\right) \) in these last two integrals,

\[
\left| {{\int }_{{D}_{n}}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt} - \frac{1}{\sigma \sqrt{n}}{\int }_{-{A\sigma }}^{A\sigma }{e}^{i\left( {{n\mu } - x}\right) u/\left( {\sigma \sqrt{n}}\right) }{e}^{-{u}^{2}/2}{du}}\right|  \leq  \frac{\varepsilon }{\sigma \sqrt{n}}{\int }_{-{A\sigma }}^{A\sigma }{e}^{-{u}^{2}/2}{du}
\]

ce qui entraîne

> which implies

\[
\left| {{\int }_{{D}_{n}}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt} - \frac{1}{\sigma \sqrt{n}}J\left( \frac{{n\mu } - x}{\sigma \sqrt{n}}\right) }\right|  \leq  \frac{\varepsilon }{\sigma \sqrt{n}}{\int }_{-{A\sigma }}^{A\sigma }{e}^{-{u}^{2}/2}{du} + \frac{1}{\sigma \sqrt{n}}{\int }_{\left| u\right|  \geq  {A\sigma }}{e}^{-{u}^{2}/2}{du}.
\]

La dernière intégrale est majorée par \( 2{\int }_{u \geq {A\sigma }}\left( {u/\left( {A\sigma }\right) }\right) {e}^{-{u}^{2}/2}{du} = 2{e}^{-{A}^{2}{\sigma }^{2}/2}/\left( {A\sigma }\right) \) , on en déduit

> The last integral is bounded by \( 2{\int }_{u \geq {A\sigma }}\left( {u/\left( {A\sigma }\right) }\right) {e}^{-{u}^{2}/2}{du} = 2{e}^{-{A}^{2}{\sigma }^{2}/2}/\left( {A\sigma }\right) \) , we deduce from this

\[
\left| {{\int }_{{D}_{n}}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt} - \frac{1}{\sigma \sqrt{n}}J\left( \frac{{n\mu } - x}{\sigma \sqrt{n}}\right) }\right|  \leq  \frac{\varepsilon \sqrt{2\pi }}{\sigma \sqrt{n}} + 2\frac{{e}^{-{A}^{2}{\sigma }^{2}/2}}{A{\sigma }^{2}\sqrt{n}}. \tag{I}
\]

Sur le domaine \( {E}_{n,\alpha } \) , il suffit d’utiliser encore une fois la majoration obtenue à la question précédente, qui entraîne \( \left| {{\varphi }_{{X}_{1}}{\left( t\right) }^{n}}\right| \leq {e}^{-n{\sigma }^{2}{t}^{2}/2}{e}^{n{t}^{2}{\sigma }^{2}/4} = {e}^{-n{\sigma }^{2}{t}^{2}/4} \) sur ce domaine, donc

> On the domain \( {E}_{n,\alpha } \), it suffices to use the upper bound obtained in the previous question once again, which leads to \( \left| {{\varphi }_{{X}_{1}}{\left( t\right) }^{n}}\right| \leq {e}^{-n{\sigma }^{2}{t}^{2}/2}{e}^{n{t}^{2}{\sigma }^{2}/4} = {e}^{-n{\sigma }^{2}{t}^{2}/4} \) on this domain, therefore

\[
\left| {{\int }_{{E}_{n,\alpha }}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt}}\right|  \leq  {\int }_{{E}_{n,\alpha }}{e}^{-n{\sigma }^{2}{t}^{2}/4}{dt} = \frac{1}{\sigma \sqrt{n}}{\int }_{{A\sigma } \leq  \left| u\right|  \leq  {\alpha \sigma }\sqrt{n}}{e}^{-{u}^{2}/4}{du} \leq  4\frac{{e}^{-{A}^{2}{\sigma }^{2}/4}}{A{\sigma }^{2}\sqrt{n}}. \tag{II}
\]

Enfin, les hypothèses vérifiées par \( {\varphi }_{{X}_{1}} \) entraînent que \( q = \mathop{\sup }\limits_{{t \in {F}_{\alpha }}}\left| {{\varphi }_{{X}_{1}}\left( t\right) }\right| < 1 \) , et on a

> Finally, the hypotheses satisfied by \( {\varphi }_{{X}_{1}} \) imply that \( q = \mathop{\sup }\limits_{{t \in {F}_{\alpha }}}\left| {{\varphi }_{{X}_{1}}\left( t\right) }\right| < 1 \), and we have

\[
\left| {{\int }_{{F}_{\alpha }}{\varphi }_{{X}_{1}}{\left( t\right) }^{n}{e}^{-{ixt}}{dt}}\right|  \leq  {2\pi }{q}^{n}. \tag{III}
\]

Résumons. Pour tout \( \varepsilon > 0 \) , pour tout \( A > 0 \) , il existe \( {N}_{0} \in \mathbb{N} \) et \( q \in \rbrack 0,1\left\lbrack \right. \) tels que pour \( n \geq {N}_{0} \) ,(I),(II) et (III) sont vérifiées. En choisissant \( A \) tel que \( 4{e}^{-{A}^{2}{\sigma }^{2}/4}/\left( {A{\sigma }^{2}}\right) < \varepsilon \) , on en déduit l’existence de \( {N}_{0} \in \mathbb{N} \) tel que les termes de droites de (I) et (II) sont respectivement \( < \varepsilon \left( {\sqrt{2\pi } + 1}\right) /\left( {\sigma \sqrt{n}}\right) \) et \( < \varepsilon /\left( {\sigma \sqrt{n}}\right) \) , et si on choisit \( {N}_{1} \geq {N}_{0} \) tel que \( {2\pi }{q}^{n} \leq \varepsilon /\left( {\sigma \sqrt{n}}\right) \) pour \( n \geq {N}_{1} \) . On en déduit, compte tenu de la formule établie en \( 2/\mathrm{b} \) ),

> Let us summarize. For all \( \varepsilon > 0 \), for all \( A > 0 \), there exist \( {N}_{0} \in \mathbb{N} \) and \( q \in \rbrack 0,1\left\lbrack \right. \) such that for \( n \geq {N}_{0} \), (I), (II) and (III) are satisfied. By choosing \( A \) such that \( 4{e}^{-{A}^{2}{\sigma }^{2}/4}/\left( {A{\sigma }^{2}}\right) < \varepsilon \), we deduce the existence of \( {N}_{0} \in \mathbb{N} \) such that the right-hand terms of (I) and (II) are respectively \( < \varepsilon \left( {\sqrt{2\pi } + 1}\right) /\left( {\sigma \sqrt{n}}\right) \) and \( < \varepsilon /\left( {\sigma \sqrt{n}}\right) \), and if we choose \( {N}_{1} \geq {N}_{0} \) such that \( {2\pi }{q}^{n} \leq \varepsilon /\left( {\sigma \sqrt{n}}\right) \) for \( n \geq {N}_{1} \). We deduce from this, taking into account the formula established in \( 2/\mathrm{b} \)),

\[
\forall n \geq  {N}_{1},\forall x \in  \mathbb{Z},\;\left| {P\left( {{S}_{n} = x}\right)  - \frac{1}{2\pi }\frac{1}{\sigma \sqrt{n}}J\left( \frac{{n\mu } - x}{\sigma \sqrt{n}}\right) }\right|  \leq  \left( {\sqrt{2\pi } + 3}\right) \frac{\varepsilon }{\sigma \sqrt{n}}.
\]

On en déduit le résultat compte tenu de l’expression de \( J\left( a\right) \) obtenue en \( 2/\mathrm{a}) \) .

> We deduce the result from this, taking into account the expression of \( J\left( a\right) \) obtained in \( 2/\mathrm{a}) \).

3/ Notons \( {Z}_{n} = \{ x \in \mathbb{Z} \mid {a\sigma }\sqrt{n} + {n\mu } \leq x \leq {b\sigma }\sqrt{n} + {n\mu }\} \) . D’après le résultat de la question précédente, on a

> 3/ Let us denote \( {Z}_{n} = \{ x \in \mathbb{Z} \mid {a\sigma }\sqrt{n} + {n\mu } \leq x \leq {b\sigma }\sqrt{n} + {n\mu }\} \). According to the result of the previous question, we have

\[
P\left( {a \leq  \frac{{S}_{n} - {n\mu }}{\sigma \sqrt{n}} \leq  b}\right)  = \mathop{\sum }\limits_{{x \in  {Z}_{n}}}P\left( {{S}_{n} = x}\right)  = \frac{1}{\sqrt{{2\pi }{\sigma }^{2}n}}\mathop{\sum }\limits_{{x \in  {Z}_{n}}}g\left( \frac{x - {n\mu }}{\sigma \sqrt{n}}\right)  + \mathop{\sum }\limits_{{x \in  {Z}_{n}}}o\left( \frac{1}{\sqrt{n}}\right) \;\left( {* *  * }\right)
\]

\( \left( {* * * }\right) \)

> avec \( g\left( u\right) = {e}^{-{u}^{2}/2} \) , et où les \( o\left( {1/\sqrt{n}}\right) \) ne dépendent que de \( n \) . Comme \( \left| {Z}_{n}\right| \leq \left( {b - a}\right) \sqrt{n} + 1 = \; O\left( \sqrt{n}\right) \) , la dernière somme est un \( o\left( 1\right) \) . Soit \( {x}_{0} = \min {Z}_{n} \) , et \( K = \left| {Z}_{n}\right| \) . On a \( \left| {K - \left( {b - a}\right) \sigma \sqrt{n}}\right| < 1 \) . On note \( {a}_{0} = \left( {{x}_{0} - {n\mu }}\right) /\left( {\sigma \sqrt{n}}\right) \) , et \( h = 1/\left( {\sigma \sqrt{n}}\right) \) , de sorte que \( a \leq {a}_{0} < a + h \) , et on a

with \( g\left( u\right) = {e}^{-{u}^{2}/2} \), and where the \( o\left( {1/\sqrt{n}}\right) \) depend only on \( n \). Since \( \left| {Z}_{n}\right| \leq \left( {b - a}\right) \sqrt{n} + 1 = \; O\left( \sqrt{n}\right) \), the last sum is a \( o\left( 1\right) \). Let \( {x}_{0} = \min {Z}_{n} \), and \( K = \left| {Z}_{n}\right| \). We have \( \left| {K - \left( {b - a}\right) \sigma \sqrt{n}}\right| < 1 \). We denote \( {a}_{0} = \left( {{x}_{0} - {n\mu }}\right) /\left( {\sigma \sqrt{n}}\right) \), and \( h = 1/\left( {\sigma \sqrt{n}}\right) \), so that \( a \leq {a}_{0} < a + h \), and we have

\[
\frac{1}{\sigma \sqrt{n}}\mathop{\sum }\limits_{{x \in  {Z}_{n}}}g\left( \frac{x - {n\mu }}{\sigma \sqrt{n}}\right)  = h\mathop{\sum }\limits_{{k = 0}}^{{K - 1}}g\left( {{a}_{0} + {kh}}\right) .
\]

\( \left( {* * * * }\right) \)

> Or la dernière somme est,à un terme \( \left( {b - a - \left( {K - 1}\right) h}\right) g\left( {b}_{0}\right) \) près (avec \( {a}_{0} + \left( {K - 1}\right) h \leq {b}_{0} \leq b \) ), une somme de Riemann de \( g \) sur l’intervalle \( \left\lbrack {a, b}\right\rbrack \) , pour la subdivision \( \sigma : a < a + h < \ldots < \; a + \left( {K - 1}\right) h < b \) dont le pas est \( h \) . Comme \( h \) tend vers 0 et \( \left( {b - a - \left( {K - 1}\right) h}\right) g\left( {b}_{0}\right) \) aussi, on en déduit, lorsque \( n \rightarrow + \infty \) , que la somme de (****) converge vers \( {\int }_{a}^{b}g\left( u\right) {du} \) lorsque \( n \rightarrow + \infty \) . L'estimation (***) permet donc d'écrire

However, the last sum is, up to a term \( \left( {b - a - \left( {K - 1}\right) h}\right) g\left( {b}_{0}\right) \) (with \( {a}_{0} + \left( {K - 1}\right) h \leq {b}_{0} \leq b \) ), a Riemann sum of \( g \) on the interval \( \left\lbrack {a, b}\right\rbrack \) , for the subdivision \( \sigma : a < a + h < \ldots < \; a + \left( {K - 1}\right) h < b \) whose mesh size is \( h \) . As \( h \) tends to 0 and \( \left( {b - a - \left( {K - 1}\right) h}\right) g\left( {b}_{0}\right) \) as well, we deduce, when \( n \rightarrow + \infty \) , that the sum of (****) converges to \( {\int }_{a}^{b}g\left( u\right) {du} \) when \( n \rightarrow + \infty \) . The estimate (***) therefore allows us to write

\[
P\left( {a \leq  \frac{{S}_{n} - {n\mu }}{\sigma \sqrt{n}} \leq  b}\right)  = \frac{1}{\sqrt{2\pi }}\frac{1}{\sigma \sqrt{n}}\mathop{\sum }\limits_{{x \in  {Z}_{n}}}g\left( \frac{x - {n\mu }}{\sigma \sqrt{n}}\right)  + o\left( 1\right)  = \frac{1}{\sqrt{2\pi }}{\int }_{a}^{b}{e}^{-{u}^{2}/2}{du} + o\left( 1\right) .
\]

Remarque. La condition (*) permet d’éviter les cas comme celui où les \( {X}_{k} \) suivent une loi de Rademacher, pour lequel \( {S}_{2n} \) prend ses valeurs dans \( 2\mathbb{Z} \) et la forme \( 2/\mathrm{d}) \) du théo-rème local limite serait fausse. Néanmoins on peut facilement démontrer, compte tenu du résultat 1/, que le théorème central limite reste vrai sans la condition (*).

> Remark. Condition (*) allows us to avoid cases such as the one where the \( {X}_{k} \) follow a Rademacher distribution, for which \( {S}_{2n} \) takes its values in \( 2\mathbb{Z} \) and the form \( 2/\mathrm{d}) \) of the local limit theorem would be false. Nevertheless, one can easily demonstrate, given result 1/, that the central limit theorem remains true without condition (*).

- Le théorème central limite reste vrai pour toute suite de variables aléatoires discrètes, sous les conditions décrites au début du problème, sans la condition (*). Mais il ne permet pas de conclure lorsque \( a \) et \( b \) dans \( 3/ \) , varient en fonction de \( n \) . Pour ces cas, on peut utiliser des versions du théorème local limite qui précisent le comportement de \( P\left( {{S}_{n} = x}\right) \) lorsque \( \left( {x - {n\mu }}\right) /\sqrt{n} \) est grand (on parle de grandes déviations). Par exemple, si \( {X}_{1} \) admet un moment d’ordre 3, on peut remplacer le \( o\left( \frac{1}{\sqrt{n}}\right) \) dans \( 2/\mathrm{d}) \) par \( O\left( \frac{1}{n{\left( 1 + \left| x\right| \right) }^{3}}\right) \) .

> - The central limit theorem remains true for any sequence of discrete random variables, under the conditions described at the beginning of the problem, without condition (*). But it does not allow us to conclude when \( a \) and \( b \) in \( 3/ \) vary as a function of \( n \) . For these cases, one can use versions of the local limit theorem that specify the behavior of \( P\left( {{S}_{n} = x}\right) \) when \( \left( {x - {n\mu }}\right) /\sqrt{n} \) is large (this is referred to as large deviations). For example, if \( {X}_{1} \) admits a moment of order 3, one can replace the \( o\left( \frac{1}{\sqrt{n}}\right) \) in \( 2/\mathrm{d}) \) with \( O\left( \frac{1}{n{\left( 1 + \left| x\right| \right) }^{3}}\right) \) .

- Nous avons prouvé, sous certaines conditions, la convergence en loi de \( \left( {{S}_{n} - {n\mu }}\right) /\left( {\sigma \sqrt{n}}\right) \) vers la loi normale centrée réduite (parfois appelée loi gaussienne), définie par \( x \mapsto \; \left( {1/\sqrt{2\pi }}\right) {\int }_{-\infty }^{x}{e}^{-{t}^{2}/2}{dt} \) . Le domaine d’application de ce résultat est assez large et explique pourquoi on rencontre souvent la gaussienne dans les modélisations statistiques.

> - We have proven, under certain conditions, the convergence in distribution of \( \left( {{S}_{n} - {n\mu }}\right) /\left( {\sigma \sqrt{n}}\right) \) to the standard normal distribution (sometimes called the Gaussian distribution), defined by \( x \mapsto \; \left( {1/\sqrt{2\pi }}\right) {\int }_{-\infty }^{x}{e}^{-{t}^{2}/2}{dt} \) . The field of application of this result is quite broad and explains why the Gaussian distribution is often encountered in statistical modeling.

Problem 10 (LOI FORTE DES GRANDS NOMBRES). 1/a) Soit \( n \in {\mathbb{N}}^{ * } \) et \( {X}_{1},\ldots ,{X}_{n} \) des variables aléatoires discrètes réelles, centrées, indépendantes, et admettant une variance. Pour \( 1 \leq k \leq n \) , on note \( {S}_{k} = {X}_{1} + \cdots + {X}_{k} \) . Montrer l’inégalité de Kolmogorov :

> Problem 10 (STRONG LAW OF LARGE NUMBERS). 1/a) Let \( n \in {\mathbb{N}}^{ * } \) and \( {X}_{1},\ldots ,{X}_{n} \) be real, centered, independent discrete random variables that admit a variance. For \( 1 \leq k \leq n \) , we denote \( {S}_{k} = {X}_{1} + \cdots + {X}_{k} \) . Show Kolmogorov's inequality:

\[
\forall x > 0,\;P\left( {\mathop{\max }\limits_{{1 \leq  k \leq  n}}\left| {S}_{k}\right|  > x}\right)  \leq  \frac{V\left( {S}_{n}\right) }{{x}^{2}}.
\]

(indication : considérer les événements \( {A}_{k} = \left\{ {{\left( {S}_{j} \leq x\right) }_{j < k},{S}_{k} > x}\right\} \) du plus petit indice \( k \) tel que \( {S}_{k} > x \) , et minorer \( E\left( {{S}_{n}^{2}{\mathbf{1}}_{{A}_{k}}}\right) \) , où \( {\mathbf{1}}_{{A}_{k}} \) désigne la fonction indicatrice de \( {A}_{k} \) ).

> (hint: consider the events \( {A}_{k} = \left\{ {{\left( {S}_{j} \leq x\right) }_{j < k},{S}_{k} > x}\right\} \) with the smallest index \( k \) such that \( {S}_{k} > x \) , and provide a lower bound for \( E\left( {{S}_{n}^{2}{\mathbf{1}}_{{A}_{k}}}\right) \) , where \( {\mathbf{1}}_{{A}_{k}} \) denotes the indicator function of \( {A}_{k} \) ).

b) Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, centrées, indépendantes, admettant une variance, et telles que \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}V\left( {X}_{n}\right) \) converge. Montrer que \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{X}_{n} \) converge presque surement.

> b) Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of real, centered, independent discrete random variables, admitting a variance, and such that \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}V\left( {X}_{n}\right) \) converges. Show that \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{X}_{n} \) converges almost surely.

\( 2/\left( \right. \) Loi forte des grands nombres, cas \( \left. {\mathcal{L}}^{2}\right) \) .

> \( 2/\left( \right. \) Strong law of large numbers, \( \left. {\mathcal{L}}^{2}\right) \) case.

a) Soit \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite croissante de \( {\mathbb{R}}^{+ * } \) tendant vers \( + \infty \) et \( {\left( {x}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite réelle. Si \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{x}_{n}/{a}_{n} \) converge, montrer le lemme de Kronecker :

> a) Let \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be an increasing sequence of \( {\mathbb{R}}^{+ * } \) tending to \( + \infty \) and \( {\left( {x}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a real sequence. If \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}{x}_{n}/{a}_{n} \) converges, show Kronecker's lemma:

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{1}{{a}_{n}}\mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k} = 0.
\]

b) Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, centrées, indépendantes, admettant une variance, et \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite croissante de \( {\mathbb{R}}^{+ * } \) tendant vers \( + \infty \) . Si \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}V\left( {X}_{n}\right) /{a}_{n}^{2} \) converge, montrer que presque surement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{{a}_{n}}\left( {{X}_{1} + \cdots + {X}_{n}}\right) = 0 \) . 3/ (Loi forte des grands nombres). Soit \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de variables aléatoires discrètes réelles, indépendantes, admettant une espérance, centrées et identiquement distribuées. a) On considère les variables aléatoires tronquées \( {Y}_{n} = {X}_{n}{\mathbf{1}}_{{\left| {X}_{n}\right| }_{ \leq }n} \) et \( {Z}_{n} = {Y}_{n} - E\left( {Y}_{n}\right) \) .

> b) Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of real, centered, independent discrete random variables, admitting a variance, and \( {\left( {a}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be an increasing sequence of \( {\mathbb{R}}^{+ * } \) tending to \( + \infty \) . If \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}V\left( {X}_{n}\right) /{a}_{n}^{2} \) converges, show that almost surely, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{{a}_{n}}\left( {{X}_{1} + \cdots + {X}_{n}}\right) = 0 \) . 3/ (Strong law of large numbers). Let \( {\left( {X}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of real, independent, centered, identically distributed discrete random variables admitting an expectation. a) Consider the truncated random variables \( {Y}_{n} = {X}_{n}{\mathbf{1}}_{{\left| {X}_{n}\right| }_{ \leq }n} \) and \( {Z}_{n} = {Y}_{n} - E\left( {Y}_{n}\right) \) .

Montrer que presque surement, \( \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n \) converge vers 0 .

> Show that almost surely, \( \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n \) converges to 0 .

b) Montrer que presque surement, \( \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n \) converge vers 0 .

> b) Show that almost surely, \( \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n \) converges to 0 .

c) Montrer que presque surement \( \left( {{X}_{n} - {Y}_{n}}\right) \) converge vers 0, puis que presque surement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{n}\left( {{X}_{1} + \cdots + {X}_{n}}\right) = 0, \)

> c) Show that \( \left( {{X}_{n} - {Y}_{n}}\right) \) converges to 0 almost surely, then that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{n}\left( {{X}_{1} + \cdots + {X}_{n}}\right) = 0, \) almost surely

Solution. 1/a) Remarquons que l’inégalité de Markov appliquée à \( {S}_{n}^{2} \) fournit \( P\left( {\left| {S}_{n}\right| > x}\right) \leq \; V\left( {S}_{n}\right) /{x}^{2} \) , mais ceci est moins fort que l’inégalité demandée. On suit l’indication, en considérant les événéments

> Solution. 1/a) Note that Markov's inequality applied to \( {S}_{n}^{2} \) yields \( P\left( {\left| {S}_{n}\right| > x}\right) \leq \; V\left( {S}_{n}\right) /{x}^{2} \), but this is weaker than the requested inequality. We follow the hint by considering the events

\[
A = \left\{  {\mathop{\max }\limits_{{1 \leq  k \leq  n}}\left| {S}_{k}\right|  > x}\right\}  \;\text{ et }\;\forall k \in  \{ 1,\ldots , n\} \;{A}_{k} = \left\{  {{S}_{1} \leq  x,\ldots ,{S}_{k - 1} \leq  x,{S}_{k} > x}\right\}  .
\]

Les événements \( {A}_{1},\ldots ,{A}_{n} \) forment une partition de \( A \) . Pour tout \( k \) , l’événement \( {A}_{k} \) est déterminé par \( {X}_{1},\ldots ,{X}_{k} \) , indépendants de \( {X}_{k + 1},\ldots ,{X}_{n} \) , donc la fonction indicatrice \( {\mathbf{1}}_{{A}_{k}} \) (définie par \( {\mathbf{1}}_{{A}_{k}}\left( \omega \right) = 1 \) si \( \omega \in {A}_{k}, = 0 \) sinon) est indépendante de \( {X}_{k + 1},\ldots ,{X}_{n} \) , donc \( {S}_{n} - {S}_{k} \) est indépendante de \( {S}_{k}{\mathbf{1}}_{{A}_{k}} \) . On en déduit

> The events \( {A}_{1},\ldots ,{A}_{n} \) form a partition of \( A \). For any \( k \), the event \( {A}_{k} \) is determined by \( {X}_{1},\ldots ,{X}_{k} \), which are independent of \( {X}_{k + 1},\ldots ,{X}_{n} \), so the indicator function \( {\mathbf{1}}_{{A}_{k}} \) (defined by \( {\mathbf{1}}_{{A}_{k}}\left( \omega \right) = 1 \) if \( \omega \in {A}_{k}, = 0 \) otherwise) is independent of \( {X}_{k + 1},\ldots ,{X}_{n} \), thus \( {S}_{n} - {S}_{k} \) is independent of \( {S}_{k}{\mathbf{1}}_{{A}_{k}} \). We deduce

\[
E\left( {{S}_{n}^{2}{\mathbf{1}}_{{A}_{k}}}\right)  = E\left( {{\left( {S}_{n} - {S}_{k}\right) }^{2}{\mathbf{1}}_{{A}_{k}}}\right)  + {2E}\left( {\left( {{S}_{n} - {S}_{k}}\right) {S}_{k}{\mathbf{1}}_{{A}_{k}}}\right)  + E\left( {{S}_{k}^{2}{\mathbf{1}}_{{A}_{k}}}\right)  \geq  {x}^{2}P\left( {A}_{k}\right)
\]

(nous avons utilisé l’indépendance de \( {S}_{n} - {S}_{k} \) et \( {S}_{k}{\mathbf{1}}_{{A}_{k}} \) , qui entraîne \( E\left( {\left( {{S}_{n} - {S}_{k}}\right) {S}_{k}{\mathbf{1}}_{{A}_{k}}}\right) = \; \left. {E\left( {{S}_{n} - {S}_{k}}\right) E\left( {{S}_{k}{\mathbf{1}}_{{A}_{k}}}\right) = 0}\right) \) . Comme les \( {\left( {A}_{k}\right) }_{1 \leq k \leq n} \) forment une partition de \( A \) , on en déduit le résultat car

> (we used the independence of \( {S}_{n} - {S}_{k} \) and \( {S}_{k}{\mathbf{1}}_{{A}_{k}} \), which implies \( E\left( {\left( {{S}_{n} - {S}_{k}}\right) {S}_{k}{\mathbf{1}}_{{A}_{k}}}\right) = \; \left. {E\left( {{S}_{n} - {S}_{k}}\right) E\left( {{S}_{k}{\mathbf{1}}_{{A}_{k}}}\right) = 0}\right) \). Since the \( {\left( {A}_{k}\right) }_{1 \leq k \leq n} \) form a partition of \( A \), we deduce the result because

\[
V\left( {S}_{n}\right)  = E\left( {S}_{n}^{2}\right)  \geq  E\left( {{S}_{n}^{2}\mathop{\sum }\limits_{{k = 1}}^{n}{\mathbf{1}}_{{A}_{k}}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}E\left( {{S}_{n}^{2}{\mathbf{1}}_{{A}_{k}}}\right)  \geq  {x}^{2}\mathop{\sum }\limits_{{k = 1}}^{n}P\left( {A}_{k}\right)  = {x}^{2}P\left( A\right) .
\]

b) L’idée est d’utiliser le critère de Cauchy,à partir de l’inégalité précédente. Soit \( \varepsilon > 0 \) et \( M \in {\mathbb{N}}^{ * } \) . Pour tout \( m > M \) , l’inégalité précédente appliquée à \( {X}_{M + 1},\ldots ,{X}_{m} \) permet d’écrire

> b) The idea is to use the Cauchy criterion, starting from the previous inequality. Let \( \varepsilon > 0 \) and \( M \in {\mathbb{N}}^{ * } \). For any \( m > M \), the previous inequality applied to \( {X}_{M + 1},\ldots ,{X}_{m} \) allows us to write

\[
P\left( {\mathop{\max }\limits_{{M < k \leq  m}}\left| {{X}_{M + 1} + \cdots  + {X}_{k}}\right|  > \varepsilon }\right)  < \frac{\mathop{\sum }\limits_{{k = M + 1}}^{m}V\left( {X}_{k}\right) }{{\varepsilon }^{2}}.
\]

En notant \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \) , on en déduit

> By denoting \( {S}_{n} = {X}_{1} + \cdots + {X}_{n} \), we deduce

\[
\forall m > M,\;P\left( {\mathop{\max }\limits_{{M < k \leq  m}}\left| {{S}_{k} - {S}_{M}}\right|  > \varepsilon }\right)  < \frac{\mathop{\sum }\limits_{{k = N + 1}}^{{+\infty }}V\left( {X}_{k}\right) }{{\varepsilon }^{2}}.
\]

La suite des ensembles \( {\left( \left\{ \mathop{\max }\limits_{{M < k \leq m}}\left| {S}_{k} - {S}_{M}\right| > \varepsilon \right\} \right) }_{m} \) est croissante avec \( m \) , on en déduit

> The sequence of sets \( {\left( \left\{ \mathop{\max }\limits_{{M < k \leq m}}\left| {S}_{k} - {S}_{M}\right| > \varepsilon \right\} \right) }_{m} \) is increasing with \( m \), we deduce

\[
P\left( {B}_{M}\right)  \leq  \frac{\mathop{\sum }\limits_{{k = N + 1}}^{{+\infty }}V\left( {X}_{k}\right) }{{\varepsilon }^{2}},\;\text{ où }\;{B}_{M} = \left\{  {\mathop{\max }\limits_{{k > M}}\left| {{S}_{k} - {S}_{M}}\right|  > \varepsilon }\right\}  .
\]

Notons \( {C}_{M} = \left\{ {\mathop{\max }\limits_{{k,\ell \geq M}}\left| {{S}_{k} - {S}_{\ell }}\right| > {2\varepsilon }}\right\} \) . L’inégalité \( \left| {{S}_{k} - {S}_{\ell }}\right| \left( \omega \right) \leq \left| {{S}_{k} - {S}_{M}}\right| \left( \omega \right) + \mid {S}_{\ell } - \; {S}_{M} \mid \left( \omega \right) \) entraîne \( {B}_{M}^{C} \subset {C}_{M}^{C} \) , donc par passage au complémentaire \( {C}_{M} \subset {B}_{M} \) , donc \( P\left( {C}_{M}\right) \leq \; \mathop{\sum }\limits_{{k = N + 1}}^{{+\infty }}V\left( {X}_{k}\right) /{\varepsilon }^{2} \) . Donc \( \mathop{\lim }\limits_{{M \rightarrow + \infty }}P\left( {C}_{M}\right) = 0 \) . Comme \( \left( {C}_{M}\right) \) est décroissante, on en déduit \( P\left( {{ \cap }_{M \in {\mathbb{N}}^{ * }}{C}_{M}}\right) = 0 \) . Ainsi, le complémentaire \( D\left( \varepsilon \right) \) de \( { \cap }_{M \in {\mathbb{N}}^{ * }}{C}_{M} \) est presque sûr. Remarquons que

> Let \( {C}_{M} = \left\{ {\mathop{\max }\limits_{{k,\ell \geq M}}\left| {{S}_{k} - {S}_{\ell }}\right| > {2\varepsilon }}\right\} \) . The inequality \( \left| {{S}_{k} - {S}_{\ell }}\right| \left( \omega \right) \leq \left| {{S}_{k} - {S}_{M}}\right| \left( \omega \right) + \mid {S}_{\ell } - \; {S}_{M} \mid \left( \omega \right) \) implies \( {B}_{M}^{C} \subset {C}_{M}^{C} \) , so by taking the complement \( {C}_{M} \subset {B}_{M} \) , thus \( P\left( {C}_{M}\right) \leq \; \mathop{\sum }\limits_{{k = N + 1}}^{{+\infty }}V\left( {X}_{k}\right) /{\varepsilon }^{2} \) . Therefore \( \mathop{\lim }\limits_{{M \rightarrow + \infty }}P\left( {C}_{M}\right) = 0 \) . Since \( \left( {C}_{M}\right) \) is decreasing, we deduce \( P\left( {{ \cap }_{M \in {\mathbb{N}}^{ * }}{C}_{M}}\right) = 0 \) . Thus, the complement \( D\left( \varepsilon \right) \) of \( { \cap }_{M \in {\mathbb{N}}^{ * }}{C}_{M} \) is almost sure. Note that

\[
D\left( \varepsilon \right)  = \left\{  {\omega \mid \exists M \in  {\mathbb{N}}^{ * },\forall k,\ell  \geq  M,\left| {{S}_{k} - {S}_{\ell }}\right| \left( \omega \right)  \leq  {2\varepsilon }}\right\}  .
\]

L’ensemble \( D = { \cap }_{n \in {\mathbb{N}}^{ * }}D\left( {1/n}\right) \) , intersection dénombrable d’ensembles presque sûrs, est presque sûr, et pour tout \( \omega \in D \) , la suite réelle \( {\left( {S}_{n}\left( \omega \right) \right) }_{n \in {\mathbb{N}}^{ * }} \) est de Cauchy, donc converge.

> The set \( D = { \cap }_{n \in {\mathbb{N}}^{ * }}D\left( {1/n}\right) \) , a countable intersection of almost sure sets, is almost sure, and for all \( \omega \in D \) , the real sequence \( {\left( {S}_{n}\left( \omega \right) \right) }_{n \in {\mathbb{N}}^{ * }} \) is Cauchy, therefore it converges.

2/a) On note \( {b}_{n} = {a}_{n} - {a}_{n - 1} \) (pour \( n \geq 2 \) ), \( {b}_{1} = {a}_{1} \) , et \( {s}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k}/{a}_{k} \) (pour \( n \in {\mathbb{N}}^{ * } \) ), \( {s}_{0} = 0 \) . Une transformation d'Abel fournit

> 2/a) Let \( {b}_{n} = {a}_{n} - {a}_{n - 1} \) (for \( n \geq 2 \) ), \( {b}_{1} = {a}_{1} \) , and \( {s}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k}/{a}_{k} \) (for \( n \in {\mathbb{N}}^{ * } \) ), \( {s}_{0} = 0 \) . An Abel transformation provides

\[
\mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k} = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}\frac{{x}_{k}}{{a}_{k}} = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}\left( {{s}_{k} - {s}_{k - 1}}\right)  = {a}_{n}{s}_{n} - \mathop{\sum }\limits_{{k = 1}}^{n}{b}_{k}{s}_{k - 1} = \mathop{\sum }\limits_{{k = 1}}^{n}{b}_{k}\left( {{s}_{n} - {s}_{k - 1}}\right) .
\]

Soit \( \varepsilon > 0 \) . Comme la suite \( \left( {s}_{n}\right) \) converge, elle est de Cauchy, donc : \( \exists N \in {\mathbb{N}}^{ * },\forall k, n \geq N\left( {k < n}\right) \) , \( \left| {{s}_{n} - {s}_{k - 1}}\right| < \varepsilon \) . On en déduit que pour tout \( n > N \)

> Let \( \varepsilon > 0 \) . Since the sequence \( \left( {s}_{n}\right) \) converges, it is Cauchy, therefore: \( \exists N \in {\mathbb{N}}^{ * },\forall k, n \geq N\left( {k < n}\right) \) , \( \left| {{s}_{n} - {s}_{k - 1}}\right| < \varepsilon \) . We deduce that for all \( n > N \)

\[
\left| {\mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k}}\right|  \leq  \left| {\mathop{\sum }\limits_{{k = 1}}^{N}{b}_{k}\left( {{s}_{n} - {s}_{k - 1}}\right) }\right|  + \mathop{\sum }\limits_{{k = N + 1}}^{n}{b}_{k}\varepsilon  \leq  \mathop{\sum }\limits_{{k = 1}}^{N}{b}_{k}\left| {s}_{n}\right|  + \left| {\mathop{\sum }\limits_{{k = 1}}^{N}{b}_{k}{s}_{k - 1}}\right|  + {a}_{n}\varepsilon  = A\left| {s}_{n}\right|  + B + {a}_{n}\varepsilon
\]

avec \( A = {a}_{N} \) et \( B = \left| {\mathop{\sum }\limits_{{k = 1}}^{N}{b}_{k}{s}_{k - 1}}\right| \) . Comme \( \left( {s}_{n}\right) \) converge et que \( {a}_{n} \) tend vers \( + \infty \) , il existe \( {N}_{1} \geq N \) tel que pour tout \( n \geq {N}_{1}, A\left| {s}_{n}\right| + B \leq {a}_{n}\varepsilon \) . On en déduit que pour tout \( n \geq {N}_{1} \) , \( \left| {\mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k}}\right| \leq 2{a}_{n}\varepsilon \) , d’où le résultat.

> with \( A = {a}_{N} \) and \( B = \left| {\mathop{\sum }\limits_{{k = 1}}^{N}{b}_{k}{s}_{k - 1}}\right| \) . Since \( \left( {s}_{n}\right) \) converges and \( {a}_{n} \) tends to \( + \infty \) , there exists \( {N}_{1} \geq N \) such that for all \( n \geq {N}_{1}, A\left| {s}_{n}\right| + B \leq {a}_{n}\varepsilon \) . We deduce that for all \( n \geq {N}_{1} \) , \( \left| {\mathop{\sum }\limits_{{k = 1}}^{n}{x}_{k}}\right| \leq 2{a}_{n}\varepsilon \) , hence the result.

b) Il suffit d’appliquer le résultat de 1/b) à la suite de variables aléatoires \( \left( {{X}_{n}/{a}_{n}}\right) \) , qui entraîne presque surement la convergence de \( \sum {X}_{n}/{a}_{n} \) , et d’après le lemme de Kronecker, ceci entraîne presque surement \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /{a}_{n} = 0 \) .

> b) It suffices to apply the result of 1/b) to the sequence of random variables \( \left( {{X}_{n}/{a}_{n}}\right) \) , which leads to the almost sure convergence of \( \sum {X}_{n}/{a}_{n} \) , and according to Kronecker's lemma, this leads almost surely to \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /{a}_{n} = 0 \) .

3/a) Quitte à considérer les variables aléatoires \( {X}_{n} - E\left( {X}_{1}\right) \) , on peut supposer \( m = 0 \) . Les variables aléatoires \( {Y}_{n} \) et \( {Z}_{n} \) sont bornées, donc admettent un moment d’ordre 2. On a \( V\left( {Z}_{n}\right) = \; V\left( {Y}_{n}\right) \leq E\left( {Y}_{n}^{2}\right) \) donc pour tout \( N \in {\mathbb{N}}^{ * } \)

> 3/a) By considering the random variables \( {X}_{n} - E\left( {X}_{1}\right) \) , we can assume \( m = 0 \) . The random variables \( {Y}_{n} \) and \( {Z}_{n} \) are bounded, therefore they admit a second-order moment. We have \( V\left( {Z}_{n}\right) = \; V\left( {Y}_{n}\right) \leq E\left( {Y}_{n}^{2}\right) \) so for all \( N \in {\mathbb{N}}^{ * } \)

\[
\mathop{\sum }\limits_{{n = 1}}^{N}\frac{V\left( {Z}_{n}\right) }{{n}^{2}} \leq  \mathop{\sum }\limits_{{n = 1}}^{N}\frac{E\left( {Y}_{n}^{2}\right) }{{n}^{2}} = \mathop{\sum }\limits_{{n = 1}}^{N}\frac{1}{{n}^{2}}\mathop{\sum }\limits_{\substack{{x \in  {X}_{1}\left( \Omega \right) } \\  {\left| x\right|  \leq  n} }}{x}^{2}P\left( {{X}_{1} = x}\right)  = \mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) }}{x}^{2}P\left( {{X}_{1} = x}\right) \mathop{\sum }\limits_{\substack{{1 \leq  n \leq  N} \\  {n \geq  \left| x\right| } }}\frac{1}{{n}^{2}}
\]

\[
\leq  \mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) , x \neq  0}}{x}^{2}P\left( {{X}_{1} = x}\right) \left( {\frac{1}{{x}^{2}} + \frac{1}{\left| x\right| }}\right)  \leq  1 + \mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) }}\left| x\right| P\left( {{X}_{1} = x}\right) ,
\]

où nous avons utilisé la majoration, pour \( x \neq 0 \) ,

> where we used the upper bound, for \( x \neq 0 \) ,

\[
\mathop{\sum }\limits_{{1 \leq  n \leq  N, n \geq  \left| x\right| }}\frac{1}{{n}^{2}} \leq  \frac{1}{{x}^{2}} + \mathop{\sum }\limits_{{n \geq  \left| x\right|  + 1}}\frac{1}{{n}^{2}} \leq  \frac{1}{{x}^{2}} + {\int }_{\left| x\right| }^{+\infty }\frac{dt}{{t}^{2}} = \frac{1}{{x}^{2}} + \frac{1}{\left| x\right| }.
\]

Comme \( {X}_{1} \) admet une espérance, on en déduit que la série \( \sum V\left( {Z}_{n}\right) /{n}^{2} \) converge. D’après le résultat de la question précédente (appliqué avec \( {a}_{n} = n \) ), on en déduit que presque surement, \( \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n \) converge vers 0 .

> Since \( {X}_{1} \) admits an expectation, we deduce that the series \( \sum V\left( {Z}_{n}\right) /{n}^{2} \) converges. According to the result of the previous question (applied with \( {a}_{n} = n \) ), we deduce that almost surely, \( \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n \) converges to 0 .

b) On a

> b) We have

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}E\left( {Y}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathop{\sum }\limits_{{x \in  X\left( \Omega \right) ,\left| x\right|  \leq  n}}{xP}\left( {{X}_{1} = x}\right)  = E\left( {X}_{1}\right)  = 0.
\]

Il est classique que ceci implique la convergence de \( \left( {E\left( {Y}_{1}\right) + \cdots + E\left( {Y}_{n}\right) }\right) /n \) vers 0 . En effet c’est la conséquence du résultat suivant, appliqué à \( {u}_{n} = E\left( {Y}_{n}\right) \) (voir aussi le tome Analyse sur la moyenne de Césaro)

> It is standard that this implies the convergence of \( \left( {E\left( {Y}_{1}\right) + \cdots + E\left( {Y}_{n}\right) }\right) /n \) to 0 . Indeed, this is a consequence of the following result, applied to \( {u}_{n} = E\left( {Y}_{n}\right) \) (see also the Analysis volume on the Cesàro mean)

Soit \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite réelle convergeant vers 0 . Alors \( \left( {{u}_{1} + \cdots + {u}_{n}}\right) /n \) converge vers 0 . \( \left( *\right) \) La preuve de \( \left( *\right) \) est facile : pour tout \( \varepsilon > 0 \) , soit \( N \in \mathbb{N} \) tel que \( \left| {u}_{n}\right| < \varepsilon \) pour \( n \geq N \) . Alors pour \( n > N \) on a \( \left| {{u}_{1} + \cdots + {u}_{n}}\right| < A + \mathop{\sum }\limits_{{k = N + 1}}^{n}\left| {u}_{k}\right| < A + \left( {n - N}\right) \varepsilon \) avec \( A = \left| {{u}_{1} + \cdots + {u}_{n}}\right| \) , donc \( \left| {{u}_{1} + \cdots + {u}_{n}}\right| < {2n\varepsilon } \) pour \( n \) assez grand.

> Let \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a real sequence converging to 0. Then \( \left( {{u}_{1} + \cdots + {u}_{n}}\right) /n \) converges to 0. \( \left( *\right) \) The proof of \( \left( *\right) \) is easy: for any \( \varepsilon > 0 \), let \( N \in \mathbb{N} \) be such that \( \left| {u}_{n}\right| < \varepsilon \) for \( n \geq N \). Then for \( n > N \) we have \( \left| {{u}_{1} + \cdots + {u}_{n}}\right| < A + \mathop{\sum }\limits_{{k = N + 1}}^{n}\left| {u}_{k}\right| < A + \left( {n - N}\right) \varepsilon \) with \( A = \left| {{u}_{1} + \cdots + {u}_{n}}\right| \), so \( \left| {{u}_{1} + \cdots + {u}_{n}}\right| < {2n\varepsilon } \) for \( n \) sufficiently large.

On en déduit que \( \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n = \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n + \left( {E\left( {Y}_{1}\right) + \cdots + E\left( {Y}_{n}\right) }\right) /n \) converge presque surement vers 0 .

> We deduce that \( \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n = \left( {{Z}_{1} + \cdots + {Z}_{n}}\right) /n + \left( {E\left( {Y}_{1}\right) + \cdots + E\left( {Y}_{n}\right) }\right) /n \) converges almost surely to 0.

c) On remarque pour tout \( N \in {\mathbb{N}}^{ * } \) ,

> c) We note that for any \( N \in {\mathbb{N}}^{ * } \),

\[
\mathop{\sum }\limits_{{n = 1}}^{N}P\left( {{X}_{n} \neq  {Y}_{n}}\right)  = \mathop{\sum }\limits_{{n = 1}}^{N}P\left( {\left| {X}_{n}\right|  > n}\right)  = \mathop{\sum }\limits_{{n = 1}}^{N}P\left( {\left| {X}_{1}\right|  > n}\right)  = \mathop{\sum }\limits_{{n = 1}}^{N}\mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) ,\left| x\right|  > n}}P\left( {{X}_{1} = x}\right)
\]

\[
= \mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) }}\mathop{\sum }\limits_{{1 \leq  n \leq  N, n < \left| x\right| }}P\left( {{X}_{1} = x}\right)  \leq  \mathop{\sum }\limits_{{x \in  {X}_{1}\left( \Omega \right) }}\left| x\right| P\left( {{X}_{1} = x}\right)
\]

et comme \( {X}_{1} \) admet une espérance, on en déduit que \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} \neq {Y}_{n}}\right) \) converge, donc d’après le lemme de Borel-Cantelli, \( P\left( {\mathop{\limsup }\limits_{n}\left\{ {{X}_{n} \neq {Y}_{n}}\right\} }\right) = 0 \) . Donc presque surement, on a \( {X}_{n} = {Y}_{n} \) sauf pour un nombre fini de valeurs de \( n \) , donc presque surement, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{X}_{n} - {Y}_{n} = 0 \) .

> and since \( {X}_{1} \) has an expectation, we deduce that \( \mathop{\sum }\limits_{n}P\left( {{X}_{n} \neq {Y}_{n}}\right) \) converges, so by the Borel-Cantelli lemma, \( P\left( {\mathop{\limsup }\limits_{n}\left\{ {{X}_{n} \neq {Y}_{n}}\right\} }\right) = 0 \). Thus, almost surely, we have \( {X}_{n} = {Y}_{n} \) except for a finite number of values of \( n \), so almost surely, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{X}_{n} - {Y}_{n} = 0 \).

On en déduit, en appliquant une fois encore le résultat \( \left( *\right) \) , que la moyenne de Césaro \( {M}_{n} = \; \left( {\left( {{X}_{1} - {Y}_{1}}\right) + \cdots + \left( {{X}_{n} - {Y}_{n}}\right) }\right) /n \) converge presque surement vers \( 0,\operatorname{donc}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n = \; \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n + {M}_{n} \) converge presque surement vers 0 .

> We deduce, by applying result \( \left( *\right) \) once again, that the Cesàro mean \( {M}_{n} = \; \left( {\left( {{X}_{1} - {Y}_{1}}\right) + \cdots + \left( {{X}_{n} - {Y}_{n}}\right) }\right) /n \) converges almost surely to \( 0,\operatorname{donc}\left( {{X}_{1} + \cdots + {X}_{n}}\right) /n = \; \left( {{Y}_{1} + \cdots + {Y}_{n}}\right) /n + {M}_{n} \) converges almost surely to 0.

Remarque. - Sous les hypothèses de la question 3/, mais sans supposer les \( {X}_{n} \) centrées, on obtient que \( \left( {{X}_{1} + \cdots + {X}_{n}}\right) /n \) converge presque surement vers \( E\left( {X}_{1}\right) \) (il suffit d’appliquer

> Remark. - Under the hypotheses of question 3/, but without assuming the \( {X}_{n} \) are centered, we obtain that \( \left( {{X}_{1} + \cdots + {X}_{n}}\right) /n \) converges almost surely to \( E\left( {X}_{1}\right) \) (it suffices to apply

3/c) à \( {X}_{n}^{ * } = {X}_{n} - E\left( {X}_{1}\right) \) ), ce qui est la formulation générale de la loi forte des grands nombres.

> 3/c) to \( {X}_{n}^{ * } = {X}_{n} - E\left( {X}_{1}\right) \)), which is the general formulation of the strong law of large numbers.

- Soit \( \alpha  > 1/2 \) . Sous les hypothèses de la question 3/ et si \( {X}_{1} \) est centré et admet une variance, le résultat 2/b) affirme que presque surement, on a

> - Let \( \alpha  > 1/2 \) . Under the assumptions of question 3/ and if \( {X}_{1} \) is centered and admits a variance, result 2/b) states that almost surely, we have

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{X}_{1} + \cdots  + {X}_{n}}{\sqrt{n}{\left( \log n\right) }^{\alpha }} = 0.
\]

Ainsi, presque surement, \( {X}_{1} + \cdots + {X}_{n} = o\left( {\sqrt{n}{\left( \log n\right) }^{\alpha }}\right) \) . Ce résultat est moins fort que celui obtenu à l'exercice 7 page 352 dans le cas particulier de la loi de Rademacher, ou il est montré que presque surement, \( \left| {{X}_{1} + \cdots + {X}_{n}}\right| \leq \sqrt{{2n}\log n}\left( {1 + o\left( 1\right) }\right) \) . Un résultat optimal de ce type, appelé loi du logarithme itéré a été obtenu par Kolmogorov en 1929, qui a montré que si les \( \left( {X}_{n}\right) \) sont identiquement distribuées, centrées, admettant un moment d’ordre 2, alors presque surement, \( \left| {{X}_{1} + \cdots + {X}_{n}}\right| \leq \left( {\sigma \sqrt{2} + o\left( 1\right) }\right) \sqrt{n\log \log n} \) , où \( \sigma \) est l’écart type de \( {X}_{1} \) , et que la constante \( \sigma \sqrt{2} \) est optimale (ce résultat a été raffiné en 1941 par Hattman et Wintner qui ont montré que presque surement, l'ensemble des valeurs d’adhérence de \( \left( {{X}_{1} + \cdots + {X}_{n}}\right) /\sqrt{n\log \log n} \) est égal à tout l’intervalle \( \left\lbrack {-\sigma \sqrt{2},\sigma \sqrt{2}}\right\rbrack ) \) .

> Thus, almost surely, \( {X}_{1} + \cdots + {X}_{n} = o\left( {\sqrt{n}{\left( \log n\right) }^{\alpha }}\right) \) . This result is weaker than the one obtained in exercise 7 on page 352 in the special case of the Rademacher distribution, where it is shown that almost surely, \( \left| {{X}_{1} + \cdots + {X}_{n}}\right| \leq \sqrt{{2n}\log n}\left( {1 + o\left( 1\right) }\right) \) . An optimal result of this type, called the law of the iterated logarithm, was obtained by Kolmogorov in 1929, who showed that if the \( \left( {X}_{n}\right) \) are identically distributed, centered, and admit a second-order moment, then almost surely, \( \left| {{X}_{1} + \cdots + {X}_{n}}\right| \leq \left( {\sigma \sqrt{2} + o\left( 1\right) }\right) \sqrt{n\log \log n} \) , where \( \sigma \) is the standard deviation of \( {X}_{1} \) , and the constant \( \sigma \sqrt{2} \) is optimal (this result was refined in 1941 by Hartman and Wintner, who showed that almost surely, the set of limit points of \( \left( {{X}_{1} + \cdots + {X}_{n}}\right) /\sqrt{n\log \log n} \) is equal to the entire interval \( \left\lbrack {-\sigma \sqrt{2},\sigma \sqrt{2}}\right\rbrack ) \) .
