#### 1.1. Cardinality of finite sets

*Français : 1.1. Cardinal des ensemble finis*

DéFINITION 1 (ENSEMBLE FINI ET CARDINAL). On dit qu'un ensemble \( E \) est fini s’il est vide ou s’il existe \( n \in {\mathbb{N}}^{ * } \) tel qu’il existe une bijection de \( \{ 1,2,\cdots , n\} \) dans \( E \) . Dans ce cas, l’entier \( n \) ne dépend pas de la bijection, on l’appelle cardinal de \( E \) . Il est noté \( \left| E\right| \) (ou \( \operatorname{Card}\left( E\right) \) , ou encore \( \# E) \) . Si \( E \) est vide son cardinal est égal à 0 .

> DEFINITION 1 (FINITE SET AND CARDINALITY). A set \( E \) is said to be finite if it is empty or if there exists \( n \in {\mathbb{N}}^{ * } \) such that there exists a bijection from \( \{ 1,2,\cdots , n\} \) to \( E \). In this case, the integer \( n \) does not depend on the bijection; it is called the cardinality of \( E \). It is denoted by \( \left| E\right| \) (or \( \operatorname{Card}\left( E\right) \), or \( \# E) \)). If \( E \) is empty, its cardinality is equal to 0.

Remarque 1. Un ensemble qui n'est pas fini, est dit infini. Les ensembles infinis n'ont pas tous la même "sorte" d'infini. Les ensembles infinis dénombrables sont ceux en bijection avec N. L'ensemble des nombres réels n'est pas dénombrable.

> Remark 1. A set that is not finite is said to be infinite. Infinite sets do not all have the same "kind" of infinity. Countably infinite sets are those in bijection with N. The set of real numbers is not countable.

PROPOSITION 1. Soient \( E \) et \( F \) deux ensembles.

> PROPOSITION 1. Let \( E \) and \( F \) be two sets.

- Si E est fini et s’il existe une bijection de E vers \( F \) , alors \( F \) est fini et \( \left| F\right|  = \left| E\right| \) .

> - If E is finite and there exists a bijection from E to \( F \), then \( F \) is finite and \( \left| F\right|  = \left| E\right| \).

- Si \( F \) est fini et s’il existe un injection de \( E \) vers \( F \) , alors \( E \) est fini et \( \left| E\right|  \leq  \left| F\right| \) , avec égalité si et seulement si f est bijective.

> - If \( F \) is finite and there exists an injection from \( E \) to \( F \), then \( E \) is finite and \( \left| E\right|  \leq  \left| F\right| \), with equality if and only if f is bijective.

- Si E est fini et s’il existe une surjection de E vers \( F \) , alors \( F \) est fini et \( \left| F\right|  \leq  \left| E\right| \) , avec égalité si et seulement si f est bijective.

> - If E is finite and there exists a surjection from E to \( F \), then \( F \) is finite and \( \left| F\right|  \leq  \left| E\right| \), with equality if and only if f is bijective.

Remarque 2. - On détermine parfois le cardinal d'un ensemble en construisant une bijection avec un autre ensemble plus simple dont on connait le cardinal (c'est une approche combinatoire). Les constructions de telles bijections sont parfois as-sez astucieuses (voir par exemple la preuve combinatoire de la détermination des nombres de Catalan, question 2/ de l'exercice 10 page 315).

> Remark 2. - We sometimes determine the cardinality of a set by constructing a bijection with another simpler set whose cardinality is known (this is a combinatorial approach). The constructions of such bijections are sometimes quite clever (see for example the combinatorial proof of the determination of Catalan numbers, question 2/ of exercise 10 on page 315).

- De manière générale, pour deux ensembles \( E \) et \( F \) (pas forcément finis), s’il existe une bijection de \( E \) vers \( F \) on dit que \( E \) et \( F \) sont équipotents. Lorsqu’il existe une injection de \( E \) vers \( F \) on dit que \( E \) est subpotent à \( F \) . En quelque sorte, ceci permet de généraliser au cas infini la comparaison de taille entre les ensembles. Par exemple un ensemble fini est subpotent à \( \mathbb{N} \) , lui même subpotent à \( \mathbb{R} \) . Un résultat classique (théorème de Cantor-Bernstein) affirme que si deux ensembles sont subpotents l'un à l'autre, alors ils sont équipotents.

> - In general, for two sets \( E \) and \( F \) (not necessarily finite), if there exists a bijection from \( E \) to \( F \), we say that \( E \) and \( F \) are equipotent. When there exists an injection from \( E \) to \( F \), we say that \( E \) is subpotent to \( F \). In a way, this allows for generalizing the comparison of set sizes to the infinite case. For example, a finite set is subpotent to \( \mathbb{N} \), which is itself subpotent to \( \mathbb{R} \). A classic result (Cantor-Bernstein theorem) states that if two sets are subpotent to each other, then they are equipotent.

COROLLAIRE 1 (PRINCIPE DES TIROIRS). Soient \( E \) et \( F \) deux ensembles finis avec \( \left| E\right| > \; \left| F\right| \) . Si \( \varphi \) est une application de \( E \) vers \( F \) , alors il existe \( y \in F \) ayant au moins deux antécédents par \( \varphi \) dans \( E \) .

> COROLLARY 1 (PIGEONHOLE PRINCIPLE). Let \( E \) and \( F \) be two finite sets with \( \left| E\right| > \; \left| F\right| \). If \( \varphi \) is a mapping from \( E \) to \( F \), then there exists \( y \in F \) having at least two antecedents by \( \varphi \) in \( E \).

Remarque 3. - Ainsi, si on doit ranger \( n + 1 \) chaussettes dans \( n \) tiroirs, alors un des tiroirs (au moins) contiendra deux chaussettes ou plus. En anglais on parle de pigeonhole principle (qui fait référence à la répartition des pigeons dans les trous d'un pigeonnier).

> Remark 3. - Thus, if one must put \( n + 1 \) socks into \( n \) drawers, then one of the drawers (at least) will contain two or more socks. In English, this is called the pigeonhole principle (which refers to the distribution of pigeons into the holes of a pigeon loft).

- Le principe des tiroirs peut entrainer des résultats assez puissants. Par exemple, il permet de montrer que pour tout \( x \in  \mathbb{R} \) et pour tout \( n \in  {\mathbb{N}}^{ * } \) , il existe \( p/q \in  \mathbb{Q} \) avec \( 1 \leq  q \leq  n \) tel que \( \left| {x - p/q}\right|  < 1/\left( {qn}\right) \) . On se ramène au principe des tiroirs en considérant les \( n + 1 \) valeurs \( \{ {mx}\} \) pour \( m = 1,\ldots , n + 1 \) ( \( \{ y\}  = y - \left\lbrack  y\right\rbrack \) est la partie fractionnaire de \( y \) ), toutes dans \( \lbrack 0,1\lbrack \) , et les \( n \) tiroirs \( \lbrack r/n,\left( {r + 1}\right) /n\lbrack \) pour \( r = 0,1,\ldots , n - 1 \) . Au moins deux réels \( \{ {ax}\} \) et \( \{ {bx}\} \) avec \( a < b \) se retrouvent dans le même tiroir, ce qui implique \( \left| {\{ {bx}\} -\{ {ax}\} }\right|  < 1/n \) et donc \( \left| {\left( {b - a}\right) x - \left\lbrack  {bx}\right\rbrack   + \left\lbrack  {ax}\right\rbrack  }\right|  < \; 1/n \) . En notant \( p = \left\lbrack  {bx}\right\rbrack   - \left\lbrack  {ax}\right\rbrack   \in  \mathbb{Z} \) et \( q = b - a \in  {\mathbb{N}}^{ * } \) on en déduit \( \left| {{qx} - p}\right|  < 1/n \) avec \( 1 \leq  q \leq  n \) (note : ce résultat fait parti d’un exercice du tome d’analyse).

> - The pigeonhole principle can lead to quite powerful results. For example, it allows one to show that for any \( x \in  \mathbb{R} \) and any \( n \in  {\mathbb{N}}^{ * } \), there exists \( p/q \in  \mathbb{Q} \) with \( 1 \leq  q \leq  n \) such that \( \left| {x - p/q}\right|  < 1/\left( {qn}\right) \). We reduce this to the pigeonhole principle by considering the \( n + 1 \) values \( \{ {mx}\} \) for \( m = 1,\ldots , n + 1 \) (\( \{ y\}  = y - \left\lbrack  y\right\rbrack \) is the fractional part of \( y \)), all in \( \lbrack 0,1\lbrack \), and the \( n \) drawers \( \lbrack r/n,\left( {r + 1}\right) /n\lbrack \) for \( r = 0,1,\ldots , n - 1 \). At least two real numbers \( \{ {ax}\} \) and \( \{ {bx}\} \) with \( a < b \) end up in the same drawer, which implies \( \left| {\{ {bx}\} -\{ {ax}\} }\right|  < 1/n \) and therefore \( \left| {\left( {b - a}\right) x - \left\lbrack  {bx}\right\rbrack   + \left\lbrack  {ax}\right\rbrack  }\right|  < \; 1/n \). By noting \( p = \left\lbrack  {bx}\right\rbrack   - \left\lbrack  {ax}\right\rbrack   \in  \mathbb{Z} \) and \( q = b - a \in  {\mathbb{N}}^{ * } \), we deduce \( \left| {{qx} - p}\right|  < 1/n \) with \( 1 \leq  q \leq  n \) (note: this result is part of an exercise in the analysis volume).

- Une autre conséquence amusante est la suivante : si on choisit 6 nombres distincts dans \( \{ 1,2,3,4,5,6,7,8,9,{10}\} \) , il en existe deux dont la somme vaut 11. En effet, chacun des 6 nombres est dans l'un des 5 sous-ensembles \( \{ 1,{10}\} ,\{ 2,9\} ,\{ 3,8\} \) , \( \{ 4,7\} ,\{ 5,6\} \) , donc il y en a deux parmi les 6 qui sont dans le même sous-ensemble, et leur somme vaut donc 11.

> - Another amusing consequence is the following: if we choose 6 distinct numbers from \( \{ 1,2,3,4,5,6,7,8,9,{10}\} \), there exist two whose sum is 11. Indeed, each of the 6 numbers is in one of the 5 subsets \( \{ 1,{10}\} ,\{ 2,9\} ,\{ 3,8\} \), \( \{ 4,7\} ,\{ 5,6\} \), so there are two among the 6 that are in the same subset, and their sum is therefore 11.

— D'autres applications du principe des tiroirs font l'objet de l'exercice 3 page 306.

> — Other applications of the pigeonhole principle are the subject of exercise 3 on page 306.

Proposition 2. Soit \( B \) un ensemble fini et A une partie de B. Alors A est fini et \( \left| A\right| \leq \left| B\right| \) . Si \( \left| A\right| = \left| B\right| \) alors \( A = B \) .

> Proposition 2. Let \( B \) be a finite set and A a subset of B. Then A is finite and \( \left| A\right| \leq \left| B\right| \). If \( \left| A\right| = \left| B\right| \) then \( A = B \).

Proposition 3. Soient \( A \) et \( B \) deux ensembles finis.

> Proposition 3. Let \( A \) and \( B \) be two finite sets.

- On a \( \left| {A \cup  B}\right|  = \left| A\right|  + \left| B\right|  - \left| {A \cap  B}\right| \) .

> - We have \( \left| {A \cup  B}\right|  = \left| A\right|  + \left| B\right|  - \left| {A \cap  B}\right| \).

- En particulier si A et B sont disjoints, alors \( \left| {A \cup  B}\right|  = \left| A\right|  + \left| B\right| \) .

> - In particular, if A and B are disjoint, then \( \left| {A \cup  B}\right|  = \left| A\right|  + \left| B\right| \) .

- On a \( \left| {A \smallsetminus  B}\right|  = \left| A\right|  - \left| {A \cap  B}\right| \) . En particulier si \( B \subset  A \) on a \( \left| {A \smallsetminus  B}\right|  = \left| A\right|  - \left| B\right| \) .

> - We have \( \left| {A \smallsetminus  B}\right|  = \left| A\right|  - \left| {A \cap  B}\right| \) . In particular, if \( B \subset  A \) we have \( \left| {A \smallsetminus  B}\right|  = \left| A\right|  - \left| B\right| \) .

Proposition 4. Soient \( {A}_{1},\ldots ,{A}_{n} \) des ensembles finis deux à deux disjoints, c’est-à-dire que pour tout \( \left( {i, j}\right) \) tels que \( 1 \leq i < j \leq n \) , on a \( {A}_{i} \cap {A}_{j} = \varnothing \) . Alors

> Proposition 4. Let \( {A}_{1},\ldots ,{A}_{n} \) be pairwise disjoint finite sets, that is to say that for all \( \left( {i, j}\right) \) such that \( 1 \leq i < j \leq n \) , we have \( {A}_{i} \cap {A}_{j} = \varnothing \) . Then

\[
\left| {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right|  = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {A}_{i}\right|
\]

Remarque 4. Un cas particulier de ce dernier résultat est le suivant : si \( {A}_{1},\ldots ,{A}_{n} \) forment une partition d’un ensemble fini \( E \) ,(c’est-à-dire si les \( {A}_{i} \) sont deux à deux disjoints et si \( \left. {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i} = E}\right) \) , alors \( \left| E\right| = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {A}_{i}\right| \) . Lorsque tous les \( {A}_{i} \) on le même cardinal \( k \) , alors \( \left| E\right| = {nk} \) . Ce dernier résultat est connu sous le nom de lemme des bergers et est souvent utilisé (implicitement) dans les problèmes combinatoires. Cette dénomination provient du fait qu'un berger peut compter ses moutons s'il ne voit que leurs pattes, en divisant le nombre de pattes par quatre.

> Remark 4. A special case of this last result is as follows: if \( {A}_{1},\ldots ,{A}_{n} \) form a partition of a finite set \( E \) (that is to say, if the \( {A}_{i} \) are pairwise disjoint and if \( \left. {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i} = E}\right) \) ), then \( \left| E\right| = \mathop{\sum }\limits_{{i = 1}}^{n}\left| {A}_{i}\right| \) . When all the \( {A}_{i} \) have the same cardinality \( k \) , then \( \left| E\right| = {nk} \) . This last result is known as the shepherd's lemma and is often used (implicitly) in combinatorial problems. This name comes from the fact that a shepherd can count his sheep if he only sees their legs, by dividing the number of legs by four.

Le théorème suivant généralise le premier résultat de la proposition 3. Il n'est pas au programme des classes préparatoires, néanmoins il est utile et la preuve proposée ci-dessous est à retenir.

> The following theorem generalizes the first result of Proposition 3. It is not in the preparatory classes curriculum; nevertheless, it is useful and the proof proposed below is worth remembering.

Proposition 5 (FORMULE DU CRIBLE DE POINCARÉ). Soient \( {A}_{1},\ldots ,{A}_{n} \) des ensembles finis. Alors on a

> Proposition 5 (POINCARÉ'S PRINCIPLE OF INCLUSION-EXCLUSION). Let \( {A}_{1},\ldots ,{A}_{n} \) be finite sets. Then we have

\[
\left| {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right|  = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}\left| {{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}\right| .
\]

Démonstration. Il est possible de procéder par récurrence sur \( n \) mais cette approche est peu commode. Une preuve plus naturelle s’obtient en considérant les fonctions indicatrices \( {\mathbf{1}}_{{A}_{i}} \) dé- finies sur \( E = { \cup }_{i = 1}^{n}{A}_{i} \) par : \( {\mathbf{1}}_{{A}_{i}}\left( x\right) = 1 \) si \( x \in {A}_{i} \) , \( = 0 \) sinon. L’indicatrice d’une intersection est le produit des indicatrices, et l’indicatrice du complémentaire \( \bar{A} \) d’une partie \( A \) de \( E \) est \( {\mathbf{1}}_{\bar{A}} = 1 - {\mathbf{1}}_{A} \) . Ainsi on peut écrire

> Proof. It is possible to proceed by induction on \( n \) , but this approach is inconvenient. A more natural proof is obtained by considering the indicator functions \( {\mathbf{1}}_{{A}_{i}} \) defined on \( E = { \cup }_{i = 1}^{n}{A}_{i} \) by: \( {\mathbf{1}}_{{A}_{i}}\left( x\right) = 1 \) if \( x \in {A}_{i} \) , \( = 0 \) otherwise. The indicator of an intersection is the product of the indicators, and the indicator of the complement \( \bar{A} \) of a subset \( A \) of \( E \) is \( {\mathbf{1}}_{\bar{A}} = 1 - {\mathbf{1}}_{A} \) . Thus, we can write

\[
{\mathbf{1}}_{{A}_{1} \cup  \ldots  \cup  {A}_{n}} = 1 - {\mathbf{1}}_{\overline{{A}_{1} \cup  \ldots  \cup  {A}_{n}}} = 1 - {\mathbf{1}}_{\overline{{A}_{1}} \cap  \ldots  \cap  \overline{{A}_{n}}} = 1 - {\mathbf{1}}_{\overline{{A}_{1}}}\cdots {\mathbf{1}}_{\overline{{A}_{n}}} = 1 - \mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 - {\mathbf{1}}_{{A}_{i}}}\right) .
\]

On en déduit

> We deduce from this

\[
{\mathbf{1}}_{{A}_{1} \cup  \ldots  \cup  {A}_{n}} = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}{\mathbf{1}}_{{A}_{{i}_{1}}}\cdots {\mathbf{1}}_{{A}_{{i}_{k}}} = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}{\mathbf{1}}_{{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}.
\]

et donc

> and therefore

\[
\left| {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right|  = \mathop{\sum }\limits_{{x \in  E}}{\mathbf{1}}_{{A}_{1} \cup  \ldots  \cup  {A}_{n}}\left( x\right)  = \mathop{\sum }\limits_{{x \in  E}}\mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}{\mathbf{1}}_{{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}\left( x\right)
\]

\[
= \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}\mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}\mathop{\sum }\limits_{{x \in  E}}{\mathbf{1}}_{{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}\left( x\right) .
\]

On conclut en observant que \( \mathop{\sum }\limits_{{x \in E}}{\mathbf{1}}_{{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}}}\left( x\right) = \left| {{A}_{{i}_{1}} \cap \ldots {A}_{{i}_{k}}}\right| \) .

> We conclude by observing that \( \mathop{\sum }\limits_{{x \in E}}{\mathbf{1}}_{{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}}}\left( x\right) = \left| {{A}_{{i}_{1}} \cap \ldots {A}_{{i}_{k}}}\right| \) .
