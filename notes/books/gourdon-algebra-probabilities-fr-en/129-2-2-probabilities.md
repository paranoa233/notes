#### 2.2. Probabilities

*Français : 2.2. Probabilités*

Intuitivement, la probabilité d'un événement est la vraisemblance qu'il se produise. C'est un nombre réel dans \( \left\lbrack {0,1}\right\rbrack \) . Pour définir les probabilités sur l'ensemble des événements \( \mathcal{A} \) , il faut (pour des raisons techniques) que \( \mathcal{A} \) vérifie certaines propriétés. Lorsque \( \Omega \) est fini ou dénombrable, on verra qu’on peut choisir \( \mathcal{A} = \mathcal{P}\left( \Omega \right) \) , mais dans le cas général (par exemple si \( \Omega = \mathbb{R} \) ), on ne sait pas toujours définir une probabilité sur n’importe quelle partie de \( \Omega \) . La notion de tribu, définie plus bas, permet de se limiter à des parties de \( \Omega \) dont on sait définir leur probabilité de réalisation.

> Intuitively, the probability of an event is the likelihood of it occurring. It is a real number in \( \left\lbrack {0,1}\right\rbrack \). To define probabilities on the set of events \( \mathcal{A} \), it is necessary (for technical reasons) that \( \mathcal{A} \) satisfies certain properties. When \( \Omega \) is finite or countable, we will see that we can choose \( \mathcal{A} = \mathcal{P}\left( \Omega \right) \), but in the general case (for example if \( \Omega = \mathbb{R} \)), we do not always know how to define a probability on any subset of \( \Omega \). The notion of a sigma-algebra, defined below, allows us to restrict ourselves to subsets of \( \Omega \) for which we know how to define their probability of occurrence.

##### Sigma-algebras.

*Français : Tribus.*

DéFINITION 1. Soit \( \Omega \) un ensemble. On appelle tribu sur \( \Omega \) une famille \( \mathcal{T} \) de parties de \( \Omega \) , vérifiant les propriétés

> DEFINITION 1. Let \( \Omega \) be a set. A sigma-algebra on \( \Omega \) is a family \( \mathcal{T} \) of subsets of \( \Omega \) satisfying the properties

(i) \( \varnothing \in \mathcal{T} \) et \( \Omega \in \mathcal{T} \) .

> (i) \( \varnothing \in \mathcal{T} \) and \( \Omega \in \mathcal{T} \).

(ii) Pour tout \( A \in \mathcal{T} \) , on a \( {A}^{C} \in \mathcal{T}\left( {A}^{C}\right. \) désigne le complémentaire \( \Omega \smallsetminus A \) de \( A \) ).

> (ii) For all \( A \in \mathcal{T} \), we have \( {A}^{C} \in \mathcal{T}\left( {A}^{C}\right. \) denotes the complement \( \Omega \smallsetminus A \) of \( A \)).

(iii) Si \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite d’éléments de \( \mathcal{T} \) , alors \( { \cup }_{n \in \mathbb{N}}{A}_{n} \in \mathcal{T} \) .

> (iii) If \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) is a sequence of elements of \( \mathcal{T} \), then \( { \cup }_{n \in \mathbb{N}}{A}_{n} \in \mathcal{T} \).

Le couple \( \left( {\Omega ,\mathcal{T}}\right) \) est alors appelé espace probabilisable, l’ensemble \( \Omega \) l’univers, et les élé- ments de \( \mathcal{T} \) s’appellent des événements.

> The pair \( \left( {\Omega ,\mathcal{T}}\right) \) is then called a measurable space, the set \( \Omega \) the sample space, and the elements of \( \mathcal{T} \) are called events.

Remarque 1. - (iii) et (ii) entraînent que l’intersection dénombrable d’éléments de \( \mathcal{T} \) est dans \( \mathcal{T} \) .

> Remark 1. - (iii) and (ii) imply that the countable intersection of elements of \( \mathcal{T} \) is in \( \mathcal{T} \).

- La réunion (ou l’intersection) finie d’éléments de \( \mathcal{T} \) est dans \( \mathcal{T} \) (prendre \( {A}_{k} = \varnothing \) à partir d'un certain rang dans la propriété (iii)).

> - The finite union (or intersection) of elements of \( \mathcal{T} \) is in \( \mathcal{T} \) (take \( {A}_{k} = \varnothing \) from a certain rank in property (iii)).

— Notons que (iii) n’entraîne pas que \( \mathcal{T} \) soit stable par réunion (ou intersection) infinie non dénombrable.

> — Note that (iii) does not imply that \( \mathcal{T} \) is stable under uncountable infinite union (or intersection).

Exemple 1. \( \; - \mathcal{T} = \{ \varnothing ,\Omega \} \) est une tribu, appelée tribu grossière (ou triviale) sur \( \Omega \) .

> Example 1. \( \; - \mathcal{T} = \{ \varnothing ,\Omega \} \) is a sigma-algebra, called the coarse (or trivial) sigma-algebra on \( \Omega \).

- L’ensemble \( \mathcal{T} = \mathcal{P}\left( \Omega \right) \) est une tribu sur \( \Omega \) . C’est cette tribu que l’on choisira pour l’ensemble \( \mathcal{A} \) des événements dont on mesure la probabilité, chaque fois que \( \Omega \) est fini ou dénombrable. Dans le cas général, pour des raisons fondamentales discutées rapidement plus bas, cette tribu sera trop grande dès que \( \Omega \) est infini non dénombrable, pour que l'on puisse définir la probabilité de tous ses éléments.

> - The set \( \mathcal{T} = \mathcal{P}\left( \Omega \right) \) is a sigma-algebra on \( \Omega \). This is the sigma-algebra that we will choose for the set \( \mathcal{A} \) of events whose probability we measure, whenever \( \Omega \) is finite or countable. In the general case, for fundamental reasons discussed briefly below, this sigma-algebra will be too large as soon as \( \Omega \) is uncountable, for us to be able to define the probability of all its elements.

Proposition 1. Soit \( {\left( {\mathcal{T}}_{\lambda }\right) }_{\lambda \in \Lambda } \) une famille de tribu sur \( \Omega \) . Alors \( { \cap }_{\lambda \in \Lambda }{\mathcal{T}}_{\lambda } \) est une tribu sur \( \Omega \) . Ainsi, si \( X \) est une partie de \( \mathcal{P}\left( \Omega \right) \) , l’intersection des tribus contenant \( X \) est la plus petite tribu contenant \( X \) , on l’appelle tribu engendrée par \( X \) .

> Proposition 1. Let \( {\left( {\mathcal{T}}_{\lambda }\right) }_{\lambda \in \Lambda } \) be a family of sigma-algebras on \( \Omega \) . Then \( { \cap }_{\lambda \in \Lambda }{\mathcal{T}}_{\lambda } \) is a sigma-algebra on \( \Omega \) . Thus, if \( X \) is a subset of \( \mathcal{P}\left( \Omega \right) \) , the intersection of the sigma-algebras containing \( X \) is the smallest sigma-algebra containing \( X \) , called the sigma-algebra generated by \( X \) .

Exemple 2. - Si \( A \subset \Omega \) , la tribu engendré par \( \{ A\} \) est \( \mathcal{T} = \left\{ {\varnothing , A,{A}^{C},\Omega }\right\} \) .

> Example 2. - If \( A \subset \Omega \) , the sigma-algebra generated by \( \{ A\} \) is \( \mathcal{T} = \left\{ {\varnothing , A,{A}^{C},\Omega }\right\} \) .

- Si \( {\left( {A}_{i}\right) }_{i \in  I} \) est une partition finie ou dénombrable de \( \Omega \) , la tribu engendrée par \( \left\{  {{A}_{i}, i \in  I}\right\} \) est l’ensemble des réunions \( {B}_{J} = \mathop{\sum }\limits_{{j \in  J}}{A}_{j} \) où \( J \) parcourt l’ensemble des parties de \( I \) .

> - If \( {\left( {A}_{i}\right) }_{i \in  I} \) is a finite or countable partition of \( \Omega \) , the sigma-algebra generated by \( \left\{  {{A}_{i}, i \in  I}\right\} \) is the set of unions \( {B}_{J} = \mathop{\sum }\limits_{{j \in  J}}{A}_{j} \) where \( J \) ranges over the set of subsets of \( I \) .

DéFINITION 2. Lorsque \( \Omega = \mathbb{R} \) , la tribu \( \mathcal{B} \) engendrée par les intervalles ouverts de \( \mathbb{R} \) s'appelle la tribu borélienne de \( \mathbb{R} \) .

> DEFINITION 2. When \( \Omega = \mathbb{R} \) , the sigma-algebra \( \mathcal{B} \) generated by the open intervals of \( \mathbb{R} \) is called the Borel sigma-algebra of \( \mathbb{R} \) .

Remarque 2. La tribu borélienne est aussi la tribu engendrée par la classe des intervalles \( \left. {\left. {{I}_{a} = }\right\rbrack - \infty , a}\right\rbrack \) avec \( a \in \mathbb{R} \) . C’est également la tribu engendrée par \( \left\{ {{I}_{a}, a \in \mathbb{Q}}\right\} \) .

> Remark 2. The Borel sigma-algebra is also the sigma-algebra generated by the class of intervals \( \left. {\left. {{I}_{a} = }\right\rbrack - \infty , a}\right\rbrack \) with \( a \in \mathbb{R} \) . It is also the sigma-algebra generated by \( \left\{ {{I}_{a}, a \in \mathbb{Q}}\right\} \) .

Probabilités.

> Probabilities.

DÉFINITION 3. Soit \( \Omega \) un ensemble et \( \mathcal{A} \) une tribu sur \( \Omega \) . On appelle probabilité sur l’espace \( \left( {\Omega ,\mathcal{A}}\right) \) une application \( P : \mathcal{A} \rightarrow \left\lbrack {0,1}\right\rbrack \) vérifiant

> DEFINITION 3. Let \( \Omega \) be a set and \( \mathcal{A} \) a sigma-algebra on \( \Omega \) . A probability on the space \( \left( {\Omega ,\mathcal{A}}\right) \) is a mapping \( P : \mathcal{A} \rightarrow \left\lbrack {0,1}\right\rbrack \) satisfying

(i) \( P\left( \Omega \right) = 1 \) ,

> (ii) Pour toute suite (dénombrable) \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) d’éléments de \( \mathcal{A} \) , disjoints deux à deux,

(ii) For any (countable) sequence \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) of elements of \( \mathcal{A} \) , disjoint two by two,

\[
P\left( {{ \cup  }_{n \in  \mathbb{N}}{A}_{n}}\right)  = \mathop{\sum }\limits_{{n \in  \mathbb{N}}}P\left( {A}_{n}\right) .
\]

On dit alors que \( \left( {\Omega ,\mathcal{A}, P}\right) \) est un espace probabilisé, et \( P \) sa mesure de probabilité (ou loi de probabilité).

> We then say that \( \left( {\Omega ,\mathcal{A}, P}\right) \) is a probability space, and \( P \) is its probability measure (or probability distribution).

Proposition 2. Soit \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé. On a les propriétés suivantes :

> Proposition 2. Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space. We have the following properties:

(i) Pour tout événement \( A \) dans \( \mathcal{A} \) , on a \( P\left( {A}^{C}\right) = 1 - P\left( A\right) \) .

> (i) For any event \( A \) in \( \mathcal{A} \) , we have \( P\left( {A}^{C}\right) = 1 - P\left( A\right) \) .

(ii) Pour tout \( n \in {\mathbb{N}}^{ * } \) et \( {A}_{0},\ldots ,{A}_{n} \) des événements dans \( \mathcal{A} \) ,

> (ii) For any \( n \in {\mathbb{N}}^{ * } \) and \( {A}_{0},\ldots ,{A}_{n} \) events in \( \mathcal{A} \) ,

(a) si les \( {\left( {A}_{k}\right) }_{0 \leq k \leq n} \) sont deux à deux disjoints alors \( P\left( {{ \cup }_{k = 0}^{n}{A}_{k}}\right) = \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) ,

> (a) if the \( {\left( {A}_{k}\right) }_{0 \leq k \leq n} \) are pairwise disjoint then \( P\left( {{ \cup }_{k = 0}^{n}{A}_{k}}\right) = \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) ,

(b) dans tous les cas \( P\left( {{ \cup }_{k = 0}^{n}{A}_{k}}\right) \leq \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) .

> (b) in all cases \( P\left( {{ \cup }_{k = 0}^{n}{A}_{k}}\right) \leq \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) .

(iii) Si A et B sont deux événements dans \( \mathcal{A} \) et si \( A \subset B \) , alors \( P\left( A\right) \leq P\left( B\right) \) .

> (iii) If A and B are two events in \( \mathcal{A} \) and if \( A \subset B \) , then \( P\left( A\right) \leq P\left( B\right) \) .

(iv) Si A et B sont deux événements dans \( \mathcal{A} \) alors \( P\left( {A \cup B}\right) = P\left( A\right) + P\left( B\right) - P\left( {A \cap B}\right) \) .

> (iv) If A and B are two events in \( \mathcal{A} \) then \( P\left( {A \cup B}\right) = P\left( A\right) + P\left( B\right) - P\left( {A \cap B}\right) \) .

(v) Si \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite croissante (au sens de l’inclusion, i.e pour tout \( n \in \mathbb{N} \) , \( {A}_{n} \subset {A}_{n + 1}) \) de \( \mathcal{A} \) , alors \( P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}P\left( {A}_{n}\right) \) .

> (v) If \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) is an increasing sequence (in the sense of inclusion, i.e. for all \( n \in \mathbb{N} \) , \( {A}_{n} \subset {A}_{n + 1}) \) of \( \mathcal{A} \) , then \( P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}P\left( {A}_{n}\right) \) .

(vi) Si \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite décroissante (au sens de l’inclusion, i.e pour tout \( n \in \mathbb{N} \) , \( \left. {{A}_{n + 1} \subset {A}_{n}}\right) \) de \( \mathcal{A} \) , alors \( P\left( {{ \cap }_{n \in \mathbb{N}}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}P\left( {A}_{n}\right) \) .

> (vi) If \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) is a decreasing sequence (in the sense of inclusion, i.e. for all \( n \in \mathbb{N} \) , \( \left. {{A}_{n + 1} \subset {A}_{n}}\right) \) of \( \mathcal{A} \) , then \( P\left( {{ \cap }_{n \in \mathbb{N}}{A}_{n}}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}P\left( {A}_{n}\right) \) .

(vii) Si \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite d’événéments de \( \mathcal{A} \) , alors \( P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) \leq \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{k}\right) \) (la dernière somme étant éventuellement infinie).

> (vii) If \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) is a sequence of events of \( \mathcal{A} \) , then \( P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) \leq \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{k}\right) \) (the last sum being possibly infinite).

Démonstration.

> Proof.

- Le résultat (ii) (a) est une conséquence de l'assertion (ii) de la définition précédente en choi-sissant \( {A}_{k} = \varnothing \) pour \( k > n \) .

> - The result (ii) (a) is a consequence of assertion (ii) of the previous definition by choosing \( {A}_{k} = \varnothing \) for \( k > n \) .

- La résultat (i) est une conséquence de (ii)(a) appliqué à la partition de \( \Omega \) formée de \( A \) et \( {A}^{C} \) . - On montre (iii) en considérant l’ensemble \( C = B \smallsetminus  A \) , de sorte que \( A \) et \( C \) forment une partition de \( B \) , donc d’après (ii)(a) on a \( P\left( A\right)  + P\left( C\right)  = P\left( B\right) \) , d’où le résultat car \( P\left( C\right)  \geq  0 \) .

> - The result (i) is a consequence of (ii)(a) applied to the partition of \( \Omega \) formed by \( A \) and \( {A}^{C} \) . - We show (iii) by considering the set \( C = B \smallsetminus  A \) , so that \( A \) and \( C \) form a partition of \( B \) , therefore according to (ii)(a) we have \( P\left( A\right)  + P\left( C\right)  = P\left( B\right) \) , hence the result because \( P\left( C\right)  \geq  0 \) .

- Pour montrer (iv) on note \( C = A \cap  B \) de sorte que les trois ensembles \( A \smallsetminus  C, B \smallsetminus  C \) et \( C \) forment une partition de \( A \cup  B \) . Ainsi, d’après la propriété (ii)(a), on a \( P\left( {A \smallsetminus  C}\right)  + P\left( {B \smallsetminus  C}\right)  + P\left( C\right)  = \; P\left( {A \cup  B}\right) \) . Comme \( A \smallsetminus  C \) et \( C \) forment une partition de \( A \) , on a \( P\left( {A \smallsetminus  C}\right)  + P\left( C\right)  = P\left( A\right) \) . De même \( P\left( {B \smallsetminus  C}\right)  + P\left( C\right)  = P\left( B\right) \) . On en déduit \( \left( {P\left( A\right)  - P\left( C\right) }\right)  + \left( {P\left( A\right)  - P\left( C\right) }\right)  + P\left( C\right)  = P\left( {A \cup  B}\right) \) , ce qui prouve (iv) vu que \( C = A \cap  B \) .

> - To show (iv), we denote \( C = A \cap  B \) such that the three sets \( A \smallsetminus  C, B \smallsetminus  C \) and \( C \) form a partition of \( A \cup  B \) . Thus, according to property (ii)(a), we have \( P\left( {A \smallsetminus  C}\right)  + P\left( {B \smallsetminus  C}\right)  + P\left( C\right)  = \; P\left( {A \cup  B}\right) \) . Since \( A \smallsetminus  C \) and \( C \) form a partition of \( A \) , we have \( P\left( {A \smallsetminus  C}\right)  + P\left( C\right)  = P\left( A\right) \) . Similarly, \( P\left( {B \smallsetminus  C}\right)  + P\left( C\right)  = P\left( B\right) \) . We deduce \( \left( {P\left( A\right)  - P\left( C\right) }\right)  + \left( {P\left( A\right)  - P\left( C\right) }\right)  + P\left( C\right)  = P\left( {A \cup  B}\right) \) , which proves (iv) given that \( C = A \cap  B \) .

- La propriété (ii)(b) découle directement de (iv) qui entraîne \( P\left( {A \cup  B}\right)  \leq  P\left( A\right)  + P\left( B\right) \) , puis en procédant par récurrence sur \( n \) .

> - Property (ii)(b) follows directly from (iv), which implies \( P\left( {A \cup  B}\right)  \leq  P\left( A\right)  + P\left( B\right) \) , and then by proceeding by induction on \( n \) .

- Pour montrer (v), on considère la suite d’événements \( {\left( {B}_{n}\right) }_{n \in  \mathbb{N}} \) définie par \( {B}_{0} = {A}_{0} \) et \( {B}_{n} = \; {A}_{n} \smallsetminus  {A}_{n - 1} \) pour \( n \in  {\mathbb{N}}^{ * } \) . On a \( P\left( {B}_{n}\right)  = P\left( {A}_{n}\right)  - P\left( {A}_{n - 1}\right) \) pour \( n \in  {\mathbb{N}}^{ * } \) et les \( {B}_{n} \) sont deux à deux disjoints. On peut donc appliquer l’assertion (ii) de la définition précédente à \( {\left( {B}_{n}\right) }_{n \in  \mathbb{N}} \) :

> - To show (v), we consider the sequence of events \( {\left( {B}_{n}\right) }_{n \in  \mathbb{N}} \) defined by \( {B}_{0} = {A}_{0} \) and \( {B}_{n} = \; {A}_{n} \smallsetminus  {A}_{n - 1} \) for \( n \in  {\mathbb{N}}^{ * } \) . We have \( P\left( {B}_{n}\right)  = P\left( {A}_{n}\right)  - P\left( {A}_{n - 1}\right) \) for \( n \in  {\mathbb{N}}^{ * } \) and the \( {B}_{n} \) are pairwise disjoint. We can therefore apply assertion (ii) of the previous definition to \( {\left( {B}_{n}\right) }_{n \in  \mathbb{N}} \) :

\[
P\left( {{ \cup  }_{n \in  \mathbb{N}}{B}_{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {B}_{n}\right)  = P\left( {A}_{0}\right)  + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {P\left( {A}_{n}\right)  - P\left( {A}_{n - 1}\right) }\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {A}_{n}\right) .
\]

On en déduit (iv) car \( { \cup }_{n \in \mathbb{N}}{B}_{n} = { \cup }_{n \in \mathbb{N}}{A}_{n} \) .

> We deduce (iv) from this because \( { \cup }_{n \in \mathbb{N}}{B}_{n} = { \cup }_{n \in \mathbb{N}}{A}_{n} \) .

- On prouve (vi) en appliquant (v) à la suite croissante \( \left( {B}_{n}\right) \) définie par \( {B}_{n} = {A}_{n}^{C} \) , de sorte que

> - We prove (vi) by applying (v) to the increasing sequence \( \left( {B}_{n}\right) \) defined by \( {B}_{n} = {A}_{n}^{C} \) , such that

\[
P\left( {{ \cap  }_{n \in  \mathbb{N}}{A}_{n}}\right)  = 1 - P\left( {\left( { \cap  }_{n \in  \mathbb{N}}{A}_{n}\right) }^{C}\right)  = 1 - P\left( {{ \cup  }_{n \in  \mathbb{N}}{B}_{n}}\right)  = 1 - \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {B}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {A}_{n}\right) .
\]

- Pour démontrer (vii), on pose \( {B}_{n} = { \cup  }_{k = 0}^{n}{A}_{k} \) . D’après (ii)(b) on a \( P\left( {B}_{n}\right)  \leq  \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) donc \( P\left( {B}_{n}\right)  \leq  \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}P\left( {A}_{k}\right) \) . La suite \( \left( {B}_{n}\right) \) est croissante donc on peut lui appliquer (v), qui donne \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {B}_{n}\right)  = P\left( {{ \cup  }_{n \in  \mathbb{N}}{B}_{n}}\right) \) . On en déduit le résultat car \( { \cup  }_{n \in  \mathbb{N}}{B}_{n} = { \cup  }_{n \in  \mathbb{N}}{A}_{n} \) .

> - To prove (vii), let \( {B}_{n} = { \cup  }_{k = 0}^{n}{A}_{k} \) . According to (ii)(b) we have \( P\left( {B}_{n}\right)  \leq  \mathop{\sum }\limits_{{k = 0}}^{n}P\left( {A}_{k}\right) \) so \( P\left( {B}_{n}\right)  \leq  \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}P\left( {A}_{k}\right) \) . The sequence \( \left( {B}_{n}\right) \) is increasing, so we can apply (v) to it, which gives \( \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {B}_{n}\right)  = P\left( {{ \cup  }_{n \in  \mathbb{N}}{B}_{n}}\right) \) . We deduce the result because \( { \cup  }_{n \in  \mathbb{N}}{B}_{n} = { \cup  }_{n \in  \mathbb{N}}{A}_{n} \) .

Remarque 3. Les propriétés (v) et (vi) sont parfois appelées théorème de la limite monotone. En corollaire, elles entraînent, pour une suite quelconque \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) d"événements,

> Remark 3. Properties (v) and (vi) are sometimes called the monotone convergence theorem. As a corollary, they imply, for any sequence \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) of events,

\[
P\left( {{ \cup  }_{n \in  \mathbb{N}}{A}_{n}}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {{ \cup  }_{k = 0}^{n}{A}_{k}}\right) ,\;P\left( {{ \cap  }_{n \in  \mathbb{N}}{A}_{n}}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}P\left( {{ \cap  }_{k = 0}^{n}{A}_{k}}\right)
\]

(il suffit d’appliquer (v) à \( {B}_{n} = { \cup }_{k = 0}^{n}{A}_{k} \) et (vi) à \( {B}_{n} = { \cap }_{k = 0}^{n}{A}_{k} \) ).

> (it suffices to apply (v) to \( {B}_{n} = { \cup }_{k = 0}^{n}{A}_{k} \) and (vi) to \( {B}_{n} = { \cap }_{k = 0}^{n}{A}_{k} \) ).

Le résultat suivant généralise la propriété (iv) de la proposition précédente, il n'est pas au programme des classes préparatoires, mais il est utile de le connaitre et de savoir le démontrer. Il s'agit de la version probabiliste de la formule du crible portant sur le cardinal de l'union de \( n \) ensembles finis (voir la proposition 5 page 301).

> The following result generalizes property (iv) of the previous proposition; it is not in the preparatory classes curriculum, but it is useful to know it and how to prove it. It is the probabilistic version of the inclusion-exclusion principle concerning the cardinality of the union of \( n \) finite sets (see proposition 5 on page 301).

Proposition 2 (FORMULE DU CRIBLE DE POINCARÉ). Soient \( {A}_{1},\ldots ,{A}_{n} \) n événements d’un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Alors on a

> Proposition 2 (POINCARÉ'S INCLUSION-EXCLUSION PRINCIPLE). Let \( {A}_{1},\ldots ,{A}_{n} \) be n events of a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Then we have

\[
P\left( {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}P\left( {{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}\right) .
\]

Démonstration. On procéde par récurrence (une approche du type de la démonstration de la proposition 5 page 301 est possible en utilisant les espérances des fonctions indicatrices des \( {A}_{i} \) lorsqu'elles peuvent être définies, en particulier dans le cas discret, mais nous ne disposons pas de ces outils à ce stade du cours). Remarquons déjà que la formule du crible de Poincaré s'écrit de manière équivalente sous la forme

> Proof. We proceed by induction (an approach similar to the proof of proposition 5 on page 301 is possible using the expectations of the indicator functions of \( {A}_{i} \) when they can be defined, particularly in the discrete case, but we do not have these tools at this stage of the course). Let us first note that Poincaré's inclusion-exclusion formula can be written equivalently as

\[
P\left( {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n\} } \\  {J \neq  \varnothing } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right) .
\]

(*)

> L'usage de cette forme sera plus commode pour la démonstration. Prouvons donc (*) par ré- currence sur \( n \) . Pour \( n = 1 \) le résultat est immédiat, pour \( n = 2 \) il s’agit du résultat (iv) de la proposition précédente. Supposons (*) vrai pour \( n - 1 \) et montrons le pour \( n \) . On note \( B = {A}_{1} \cup \ldots \cup {A}_{n - 1} \) . Nous utiliserons l’égalité \( P\left( {B \cup {A}_{n}}\right) = P\left( B\right) + P\left( {A}_{n}\right) - P\left( {B \cap {A}_{n}}\right) \) , pour ce faire on calcule \( P\left( B\right) \) et \( P\left( {B \cap {A}_{n}}\right) \) . L’hypothèse de récurrence appliquée à \( B \) s’écrit

Using this form will be more convenient for the proof. Let us therefore prove (*) by induction on \( n \) . For \( n = 1 \) the result is immediate; for \( n = 2 \) it is the result (iv) of the previous proposition. Assume (*) is true for \( n - 1 \) and let us show it for \( n \) . Let \( B = {A}_{1} \cup \ldots \cup {A}_{n - 1} \) . We will use the equality \( P\left( {B \cup {A}_{n}}\right) = P\left( B\right) + P\left( {A}_{n}\right) - P\left( {B \cap {A}_{n}}\right) \) ; to do this, we calculate \( P\left( B\right) \) and \( P\left( {B \cap {A}_{n}}\right) \) . The induction hypothesis applied to \( B \) is written

\[
P\left( B\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n - 1\} } \\  {J \neq  \varnothing } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right) .
\]

On a \( B \cap {A}_{n} = { \cup }_{i = 1}^{n - 1}{B}_{i} \) où \( {B}_{i} = {A}_{i} \cap {A}_{n} \) donc l’hypothèse de récurrence appliquée à \( B \cap {A}_{n} \) entraîne

> We have \( B \cap {A}_{n} = { \cup }_{i = 1}^{n - 1}{B}_{i} \) where \( {B}_{i} = {A}_{i} \cap {A}_{n} \) so the induction hypothesis applied to \( B \cap {A}_{n} \) implies

\[
P\left( {B \cap  {A}_{n}}\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n - 1\} } \\  {J \neq  \varnothing } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{B}_{j}}\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n\} } \\  {n \in  J, J \neq  \{ n\} } }}{\left( -1\right) }^{\left| J\right| }P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right)
\]

où la dernière égalité provient de l’identité \( { \cap }_{j \in J}{B}_{j} = \left( {{ \cap }_{j \in J}{A}_{j}}\right) \cap {A}_{n} = { \cap }_{j \in J\cup \{ n\} }{A}_{j} \) lorsque \( J \subset \{ 1,\ldots , n - 1\} \) . En écrivant \( P\left( {B \cup {A}_{n}}\right) = P\left( B\right) - P\left( {B \cap {A}_{n}}\right) + P\left( {A}_{n}\right) \) on en déduit

> where the last equality comes from the identity \( { \cap }_{j \in J}{B}_{j} = \left( {{ \cap }_{j \in J}{A}_{j}}\right) \cap {A}_{n} = { \cap }_{j \in J\cup \{ n\} }{A}_{j} \) when \( J \subset \{ 1,\ldots , n - 1\} \) . By writing \( P\left( {B \cup {A}_{n}}\right) = P\left( B\right) - P\left( {B \cap {A}_{n}}\right) + P\left( {A}_{n}\right) \) we deduce

\[
P\left( {B \cup  {A}_{n}}\right)  = \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n - 1\} } \\  {J \neq  \varnothing } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right)  + \mathop{\sum }\limits_{\substack{{J \subset  \{ 1,\ldots , n\} } \\  {n \in  J, J \neq  \{ n\} } }}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right)  + P\left( {A}_{n}\right) ,
\]

ce qui entraîne (*), achèvant ainsi la preuve par récurrence.

> which implies (*), thus completing the proof by induction.

Remarque 4. Il est intéressant de retenir la forme équivalente (*) (dans la démonstration), car elle fournit parfois un moyen commode d'utilisation de la formule du crible.

> Remark 4. It is interesting to remember the equivalent form (*) (in the proof), as it sometimes provides a convenient way to use the inclusion-exclusion principle.

Evénements négligeables, presques sûrs.

> Negligible events, almost sure events.

DéFINITION 4. Soit \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé. Un événement \( A \in \mathcal{A} \) est dit négli-geable si \( P\left( A\right) = 0 \) , il est dit presque sûr si \( P\left( A\right) = 1 \) . Une propriété vraie sur tous les éléments d'un événement presque sûr est dite presque sure.

> DEFINITION 4. Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space. An event \( A \in \mathcal{A} \) is said to be negligible if \( P\left( A\right) = 0 \) , it is said to be almost sure if \( P\left( A\right) = 1 \) . A property true for all elements of an almost sure event is said to be almost sure.

Remarque 5. - Une union dénombrable d'événements négligeable est négligeable, une intersection dénombrable d'événements presque sûrs est presque sure.

> Remark 5. - A countable union of negligible events is negligible, a countable intersection of almost sure events is almost sure.

- Lorsque \( \Omega \) est fini ou dénombrable (avec \( \forall x \in  \Omega , P\left( {\{ x\} }\right)  > 0 \) , ce qu’on rencontre en pratique), un événement négligeable est forcément impossible. Un exemple d'événement négligeable non vide, dans le cas des suites infinies de pile ou face, \( \left( {\Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{\mathbb{N}}}\right) \) est l’événement \( \left\{  {\mathrm{P}}_{\mathbb{N}}\right\} \) où \( {\mathrm{P}}_{\mathbb{N}} \) désigne la suite ne contenant que des piles. Cet exemple n'est qu'intuitif car nous n'avons pas probabilisé l'espace \( \Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{\mathbb{N}} \) (ceci est abordé dans l’exemple 4 page 326). Un événement négligeable peut même être infini non dénombrable (voir l'exercice 6 page 331).

> - When \( \Omega \) is finite or countable (with \( \forall x \in  \Omega , P\left( {\{ x\} }\right)  > 0 \) , which is encountered in practice), a negligible event is necessarily impossible. An example of a non-empty negligible event, in the case of infinite sequences of heads or tails, \( \left( {\Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{\mathbb{N}}}\right) \) is the event \( \left\{  {\mathrm{P}}_{\mathbb{N}}\right\} \) where \( {\mathrm{P}}_{\mathbb{N}} \) denotes the sequence containing only tails. This example is only intuitive because we have not probabilized the space \( \Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{\mathbb{N}} \) (this is addressed in example 4 on page 326). A negligible event can even be uncountable (see exercise 6 on page 331).

Probabilités sur les espaces finis ou dénombrables. On considère ici que \( \Omega \) est fini ou dénombrable. On peut numéroter ses élements de sorte que \( \Omega = \left\{ {{w}_{k}, k \in I}\right\} \) avec \( I = \{ 0,\ldots , n - 1\} \) si \( \Omega \) est fini de cardinal \( n \) , ou \( I = \mathbb{N} \) si \( \Omega \) est dénombrable. La tribu considérée est ici l’ensemble \( \mathcal{P}\left( \Omega \right) \) des parties de \( \Omega \) .

> Probabilities on finite or countable spaces. We consider here that \( \Omega \) is finite or countable. We can number its elements such that \( \Omega = \left\{ {{w}_{k}, k \in I}\right\} \) with \( I = \{ 0,\ldots , n - 1\} \) if \( \Omega \) is finite with cardinality \( n \) , or \( I = \mathbb{N} \) if \( \Omega \) is countable. The sigma-algebra considered here is the set \( \mathcal{P}\left( \Omega \right) \) of all subsets of \( \Omega \) .

Proposition 3. Une probabilité sur un univers \( \Omega = \left\{ {{w}_{k}, k \in I}\right\} \) fini ou dénombrable est entièrement caractérisée par ses valeurs sur les singletons \( P\left( \left\{ {w}_{k}\right\} \right) \) pour \( {w}_{k} \in \Omega \) . Étant donnée une suite de nombres réels positifs \( {\left( {p}_{k}\right) }_{k \in I} \) telle que \( \mathop{\sum }\limits_{{k \in I}}{p}_{k} = 1 \) , il lui correspond une unique probabilité \( P \) telle que

> Proposition 3. A probability on a finite or countable universe \( \Omega = \left\{ {{w}_{k}, k \in I}\right\} \) is entirely characterized by its values on the singletons \( P\left( \left\{ {w}_{k}\right\} \right) \) for \( {w}_{k} \in \Omega \) . Given a sequence of positive real numbers \( {\left( {p}_{k}\right) }_{k \in I} \) such that \( \mathop{\sum }\limits_{{k \in I}}{p}_{k} = 1 \) , there corresponds a unique probability \( P \) such that

\[
\forall A \in  \mathcal{P}\left( \Omega \right) ,\;P\left( A\right)  = \mathop{\sum }\limits_{{{\omega }_{k} \in  A}}P\left( \left\{  {\omega }_{k}\right\}  \right)  = \mathop{\sum }\limits_{{{\omega }_{k} \in  A}}{p}_{k}.
\]

Ainsi, la connaissance des \( P\left( \left\{ {\omega }_{k}\right\} \right) \) suffit pour connaitre celle de tout événement. Exemples. Espaces probabilisés finis ou dénombrables classiques.

> Thus, knowledge of the \( P\left( \left\{ {\omega }_{k}\right\} \right) \) is sufficient to know that of any event. Examples. Classic finite or countable probability spaces.

- Espaces finis

> - Finite spaces

- LoI UNIFORME. La loi définie par \( P\left( A\right)  = \frac{\left| A\right| }{\left| \Omega \right| } \) pour tout \( A \in  \mathcal{P}\left( \Omega \right) \) est la loi uniforme. Dans ce cas le calcul des probabilités se ramène à des problèmes combinatoires.

> - UNIFORM DISTRIBUTION. The distribution defined by \( P\left( A\right)  = \frac{\left| A\right| }{\left| \Omega \right| } \) for all \( A \in  \mathcal{P}\left( \Omega \right) \) is the uniform distribution. In this case, the calculation of probabilities reduces to combinatorial problems.

- LoI DE BERNOULLI. Sur \( \Omega  = \{ 0,1\} \) , la loi de Bernoulli de paramètre \( p \in  \rbrack 0,1\lbrack \) est définie par \( P\left( {\{ 1\} }\right)  = p \) et \( P\left( {\{ 0\} }\right)  = 1 - p \) . On peut aussi définir cette loi pour un jeu de pile ou face \( \left( {\Omega  = \{ \mathrm{P},\mathrm{F}\} }\right) \) , elle modélise alors la chance que la pièce tombe sur pile ou sur face. Lorsque la pièce est équilibrée on a \( p = 1/2 \) , dans le cas général la pièce est dite biaisée.

> - BERNOULLI DISTRIBUTION. On \( \Omega  = \{ 0,1\} \) , the Bernoulli distribution with parameter \( p \in  \rbrack 0,1\lbrack \) is defined by \( P\left( {\{ 1\} }\right)  = p \) and \( P\left( {\{ 0\} }\right)  = 1 - p \) . This distribution can also be defined for a coin toss \( \left( {\Omega  = \{ \mathrm{P},\mathrm{F}\} }\right) \) , where it models the chance of the coin landing on heads or tails. When the coin is fair, we have \( p = 1/2 \) ; in the general case, the coin is said to be biased.

##### Countable spaces

*Français : Espaces dénombrables*

- LoI GÉOMÉTRIQUE. Sur \( \Omega  = \mathbb{N} \) , la loi géométrique de paramètre \( p \in  \rbrack 0,1\lbrack \) est définie par \( P\left( {\{ n\} }\right)  = p{\left( 1 - p\right) }^{n} \) .

> - GEOMETRIC DISTRIBUTION. On \( \Omega  = \mathbb{N} \) , the geometric distribution with parameter \( p \in  \rbrack 0,1\lbrack \) is defined by \( P\left( {\{ n\} }\right)  = p{\left( 1 - p\right) }^{n} \) .

- LoI DE POISSON. Sur \( \Omega  = \mathbb{N} \) , la loi de Poisson de paramètre \( \lambda  > 0 \) est définie par \( P\left( {\{ n\} }\right)  = \frac{{\lambda }^{n}}{n!}{e}^{-\lambda } \) . Elle modélise le nombre d’événements qui se produisent dans un intervalle de temps fixé.

> - POISSON DISTRIBUTION. On \( \Omega  = \mathbb{N} \) , the Poisson distribution with parameter \( \lambda  > 0 \) is defined by \( P\left( {\{ n\} }\right)  = \frac{{\lambda }^{n}}{n!}{e}^{-\lambda } \) . It models the number of events occurring in a fixed time interval.

- LOI ZÉTA. Sur \( \Omega  = {\mathbb{N}}^{ * } \) la loi zéta de paramètre \( s > 1 \) est définie par \( P\left( {\{ n\} }\right)  = \)

> - ZETA DISTRIBUTION. On \( \Omega  = {\mathbb{N}}^{ * } \) , the zeta distribution with parameter \( s > 1 \) is defined by \( P\left( {\{ n\} }\right)  = \)

\[
\frac{1}{{n}^{s}}\frac{1}{\zeta \left( s\right) }\text{ , où }\zeta \left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}}\text{ . }
\]
