#### 2.1. The language of probability

*Français : 2.1.Le langage des probabilités*

La théorie des probabilités modélise les phénomènes dans lesquels le hasard intervient. Elle a des applications dans de nombreux domaines (physique, médecine, météorologie, marchés boursiers, etc) et dans ce contexte, a son vocabulaire propre.

> Probability theory models phenomena in which chance plays a role. It has applications in many fields (physics, medicine, meteorology, stock markets, etc.) and in this context, has its own vocabulary.

Les expériences aléatoires sont les expériences \( \mathcal{E} \) dont le résultat est soumis au hasard. L'espace des résultats possibles associés à l'expérience s'appelle l'univers, il est souvent noté \( \Omega \) (on l’appelle parfois espace d’états). Voici quelques exemples d’expériences aléa-toires avec l'univers associé :

> Random experiments are experiments \( \mathcal{E} \) whose result is subject to chance. The space of possible outcomes associated with the experiment is called the sample space, it is often denoted by \( \Omega \) (it is sometimes called the state space). Here are some examples of random experiments with the associated sample space:

- Lancement de dé : l'expérience aléatoire est celle du résultat d'un lancement de dé à 6 faces, et l’univers est \( \Omega  = \{ 1,2,3,4,5,6\} \) .

> - Die roll: the random experiment is that of the result of a 6-sided die roll, and the sample space is \( \Omega  = \{ 1,2,3,4,5,6\} \).

- On tire successivement deux boules dans une urne contenant \( n \) boules noires et blanches, puis on observe leurs couleurs. Ici \( \Omega  = \{ \left( {B, B}\right) ,\left( {B, N}\right) ,\left( {N, B}\right) ,\left( {N, N}\right) \} \) .

> - Two balls are drawn successively from an urn containing \( n \) black and white balls, then their colors are observed. Here \( \Omega  = \{ \left( {B, B}\right) ,\left( {B, N}\right) ,\left( {N, B}\right) ,\left( {N, N}\right) \} \) .

— Un colis doit arriver entre 15h et 18h, on observe le temps d’attente. On a \( \Omega = \left\lbrack {0,3}\right\rbrack \) .

> — A package is to arrive between 3 PM and 6 PM; the waiting time is observed. We have \( \Omega = \left\lbrack {0,3}\right\rbrack \) .

- On observe le prix d’une action en bourse, sur tout l’intervalle de temps \( \left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack \) . Ici \( \Omega  = \mathcal{C}\left( {\left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack  ,{\mathbb{R}}^{ + }}\right) \) , l’ensemble des fonctions continues de \( \left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack \) dans \( {\mathbb{R}}^{ + } \) .

> - The price of a stock on the stock market is observed over the entire time interval \( \left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack \) . Here \( \Omega  = \mathcal{C}\left( {\left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack  ,{\mathbb{R}}^{ + }}\right) \) , the set of continuous functions from \( \left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack \) to \( {\mathbb{R}}^{ + } \) .

Les événements (la définition rigoureuse sera donnée plus bas) associés à l'expérience aléatoire \( \mathcal{E} \) , d’univers \( \Omega \) , sont les sous-ensembles de \( \Omega \) dont on peut dire s’ils sont réalisés ou non. Des exemples d'événements sont les suivants :

> Events (the rigorous definition will be given below) associated with the random experiment \( \mathcal{E} \) , with sample space \( \Omega \) , are the subsets of \( \Omega \) for which we can determine whether they have occurred or not. Examples of events are as follows:

- Dans l'expérience de lancement de dé, l'événement "le dé montre une valeur paire" est le sous-ensemble \( A = \{ 2,4,6\} \) de \( \Omega \) .

> - In the die-rolling experiment, the event "the die shows an even value" is the subset \( A = \{ 2,4,6\} \) of \( \Omega \) .

- Dans l’attente du colis entre 15h et 18h, \( A = \rbrack 2,3\rbrack \) est l’événement "l’attente a duré plus de 2 heures".

> - In the case of waiting for the package between 3 PM and 6 PM, \( A = \rbrack 2,3\rbrack \) is the event "the wait lasted more than 2 hours".

- L'événement "le prix d'une action en bourse ne varie pas plus de \( {10}\% \) entre \( {t}_{0} \) et \( {t}_{1} \) " est \( A = \left\{  {f \in  \mathcal{C}\left( {\left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack  ,{\mathbb{R}}^{ + }}\right)  \mid  \mathop{\sup }\limits_{{{t}_{0} \leq  t \leq  {t}_{1}}}\left| {f\left( t\right)  - f\left( {t}_{0}\right) }\right|  \leq  f\left( {t}_{0}\right) /{10}}\right\} \) .

> - The event "the price of a stock on the stock market does not vary by more than \( {10}\% \) between \( {t}_{0} \) and \( {t}_{1} \) " is \( A = \left\{  {f \in  \mathcal{C}\left( {\left\lbrack  {{t}_{0},{t}_{1}}\right\rbrack  ,{\mathbb{R}}^{ + }}\right)  \mid  \mathop{\sup }\limits_{{{t}_{0} \leq  t \leq  {t}_{1}}}\left| {f\left( t\right)  - f\left( {t}_{0}\right) }\right|  \leq  f\left( {t}_{0}\right) /{10}}\right\} \) .

Ici aussi, plutôt que d'utiliser des termes ensemblistes, le langage utilisé sur les événements est propre aux probabilités :

> Here too, rather than using set-theoretic terms, the language used for events is specific to probability:

- L’ensemble \( \varnothing \) est l’événement impossible.

> - The set \( \varnothing \) is the impossible event.

- L’ensemble \( \Omega \) est l’événement certain.

> - The set \( \Omega \) is the certain event.

- Deux événements \( A \) et \( B \) tels que \( A \cap  B = \varnothing \) sont dit incompatibles.

> - Two events \( A \) and \( B \) such that \( A \cap  B = \varnothing \) are said to be mutually exclusive.

- Si \( A \subset  B \) on dit que \( A \) implique \( B \) .

> - If \( A \subset  B \) we say that \( A \) implies \( B \) .
