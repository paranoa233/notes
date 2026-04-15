#### 2.4. Exercises

*Français : 2.4. Exercices*

EXERCICE 1. Le gène de l'hémophilie est porté par le chromosome X, les hommes le révèlent systématiquement s'ils le portent, et les femmes ne le révèlent pas (nous considé- rons ici qu'il n'y a pas d'exception à cette règle). Ce gène est transmis aux enfants avec une probabilité \( 1/2 \) par la mère. Une femme a un cousin germain hémophile (le fils de la soeur de sa mère), ni son grand-père, ni son père ni son beau-frère ne sont hémophiles. De plus elle a deux fils non hémophiles.

> EXERCISE 1. The hemophilia gene is carried by the X chromosome; men reveal it systematically if they carry it, and women do not reveal it (we assume here that there are no exceptions to this rule). This gene is transmitted to children with a probability \( 1/2 \) by the mother. A woman has a first cousin who is a hemophiliac (the son of her mother's sister); neither her grandfather, nor her father, nor her brother-in-law are hemophiliacs. Furthermore, she has two non-hemophiliac sons.

1/ Quelle est sa probabilité de porter le gène de l'hémophilie?

> 1/ What is her probability of carrying the hemophilia gene?

2/ Quelle est cette probabilité, si on sait de plus qu'elle a un frère non-hémophile?

> 2/ What is this probability, if we also know that she has a non-hemophiliac brother?

Solution.

> Solution.

1 / La soeur de sa mère porte le gène de l’hémophilie, donc sa grand-mère est porteuse (aucun homme de la famille ne porte le gène). Donc sa mère a une probabilité \( 1/2 \) de porter le gène, donc elle même a une probabilité \( 1/4 \) de le porter.

> 1 / Her mother's sister carries the hemophilia gene, so her grandmother is a carrier (no man in the family carries the gene). Thus, her mother has a probability \( 1/2 \) of carrying the gene, so she herself has a probability \( 1/4 \) of carrying it.

Ainsi l’événement \( A \) "la femme porte le gène de l’hémophilie" vérifie \( P\left( A\right) = 1/4 \) . En notant \( B \) l’événement "aucun de ses deux fils n’est hémophile", il s’agit de calculer \( P\left( {A \mid B}\right) \) . La formule de Bayes appliqué à la partition \( A,{A}^{C} \) de l’ensemble des cas possibles, donne

> Thus, the event \( A \) "the woman carries the hemophilia gene" satisfies \( P\left( A\right) = 1/4 \) . Denoting by \( B \) the event "none of her two sons is hemophiliac", we need to calculate \( P\left( {A \mid B}\right) \) . Bayes' formula applied to the partition \( A,{A}^{C} \) of the set of possible cases gives

\[
P\left( {A \mid  B}\right)  = \frac{P\left( {A \cap  B}\right) }{P\left( B\right) } = \frac{P\left( {B \mid  A}\right) P\left( A\right) }{P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) } = \frac{\left( {1/4}\right) \left( {1/4}\right) }{\left( {1/4}\right) \left( {1/4}\right)  + 1 \cdot  \left( {3/4}\right) } = \frac{1}{13}.
\]

2/ La probabilité que sa mère soit porteuse est modifiée, ce qui modifie \( P\left( A\right) \) . Notons \( M \) l’évé- nement "sa mère est porteuse" et \( F \) l’événement "son frère est non-hémophile", de sorte que \( P\left( A\right) = \frac{1}{2}P\left( {M \mid F}\right) \) . Comme précédemment on applique la formule de Bayes qui donne

> 2/ The probability that her mother is a carrier is modified, which changes \( P\left( A\right) \) . Let \( M \) be the event "her mother is a carrier" and \( F \) be the event "her brother is non-hemophiliac", such that \( P\left( A\right) = \frac{1}{2}P\left( {M \mid F}\right) \) . As before, we apply Bayes' formula, which gives

\[
P\left( {M \mid  F}\right)  = \frac{P\left( {M \cap  F}\right) }{P\left( F\right) } = \frac{P\left( {F \mid  M}\right) P\left( M\right) }{P\left( {F \mid  M}\right) P\left( M\right)  + P\left( {F \mid  {M}^{C}}\right) P\left( {M}^{C}\right) } = \frac{\left( {1/2}\right) \left( {1/2}\right) }{\left( {1/2}\right) \left( {1/2}\right)  + 1 \cdot  \left( {1/2}\right) } = \frac{1}{3}.
\]

Donc \( P\left( A\right) = 1/6 \) . La même formule que celle utilisée dans \( 1/ \) avec cette nouvelle valeur de \( P\left( A\right) \) donne

> Therefore \( P\left( A\right) = 1/6 \) . The same formula as the one used in \( 1/ \) with this new value of \( P\left( A\right) \) gives

\[
P\left( {A \mid  B}\right)  = \frac{P\left( {B \mid  A}\right) P\left( A\right) }{P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) } = \frac{\left( {1/4}\right) \left( {1/6}\right) }{\left( {1/4}\right) \left( {1/6}\right)  + 1 \cdot  \left( {5/6}\right) } = \frac{1}{21}.
\]

EXERCICE 2. Une chaine de fabrication produit des pièces dont le nombre suit une loi de Poisson : la probabilité d’avoir \( n \) pièces fabriquées en une journée est \( {p}_{n} = {e}^{-\lambda }{\lambda }^{n}/n \) ! avec \( \lambda = {1000} \) . Une pièce a une probabilité \( p = 1/{250} \) d’avoir un défault.

> EXERCISE 2. A production line manufactures parts whose number follows a Poisson distribution: the probability of having \( n \) parts manufactured in one day is \( {p}_{n} = {e}^{-\lambda }{\lambda }^{n}/n \) ! with \( \lambda = {1000} \) . A part has a probability \( p = 1/{250} \) of having a defect.

1 / Quelle est la plus grande valeur de \( k \in \mathbb{N} \) pour laquelle la probabilité \( {d}_{k} \) d’avoir moins de \( k \) pièces avec défaut la même journée, vérifie \( {d}_{k} < 1/2 \) ?

> 1 / What is the largest value of \( k \in \mathbb{N} \) for which the probability \( {d}_{k} \) of having fewer than \( k \) defective parts on the same day satisfies \( {d}_{k} < 1/2 \) ?

2 / Un automate effectue un test de contrôle automatique de chaque pièce en sortie de la chaîne et rejette les pièces lorsque celui ci est positif.

> 2 / An automated machine performs an automatic control test on each part leaving the line and rejects the parts when it is positive.

- Si la pièce a un défaut, le test de contrôle est positif avec une probabilité \( q = 0,{98} \) .

> - If the part has a defect, the control test is positive with a probability \( q = 0,{98} \) .

- Si la pièce n’a pas de défaut, l’automate la rejette avec une probabilité \( r = {10}^{-4} \) . a) Quelle est la probabilité d'avoir 5 pièces rejetées en une seule journée ?

> - If the part has no defect, the machine rejects it with a probability \( r = {10}^{-4} \) . a) What is the probability of having 5 rejected parts in a single day?

b) Quelle est la probabilité qu'en une journée, aucune pièce sans défaut n'ait été rejetée, sachant que 5 pièces ont été rejetées?

> b) What is the probability that in one day, no non-defective part was rejected, given that 5 parts were rejected?

Solution. 1/ Notons \( {A}_{n} \) l’événement "il y a \( n \) pièces fabriquées en une journée" et \( {B}_{k} \) l’événement "il y a \( k \) pieces avec défaut en une journée". Lorsqu’on a \( n \geq k \) pièces produites en une journée, il y a parmi celles-ci \( \left( \begin{array}{l} n \\ k \end{array}\right) \) combinaisons possibles de \( k \) pièces avec défaut et \( n - k \) sans défaut, chacune ayant une probabilité \( {p}^{k}{\left( 1 - p\right) }^{n - k} \) de se produire, donc \( P\left( {{B}_{k} \mid {A}_{n}}\right) = \left( \begin{array}{l} n \\ k \end{array}\right) {p}^{k}{\left( 1 - p\right) }^{n - k} \) . La formule des probabilités totale donne

> Solution. 1/ Let \( {A}_{n} \) be the event "there are \( n \) parts manufactured in one day" and \( {B}_{k} \) be the event "there are \( k \) defective parts in one day". When there are \( n \geq k \) parts produced in a day, there are among these \( \left( \begin{array}{l} n \\ k \end{array}\right) \) possible combinations of \( k \) defective parts and \( n - k \) non-defective ones, each having a probability \( {p}^{k}{\left( 1 - p\right) }^{n - k} \) of occurring, so \( P\left( {{B}_{k} \mid {A}_{n}}\right) = \left( \begin{array}{l} n \\ k \end{array}\right) {p}^{k}{\left( 1 - p\right) }^{n - k} \) . The law of total probability gives

\[
P\left( {B}_{k}\right)  = \mathop{\sum }\limits_{{n = k}}^{{+\infty }}P\left( {{B}_{k} \mid  {A}_{n}}\right) P\left( {A}_{n}\right)  = \mathop{\sum }\limits_{{n = k}}^{{+\infty }}\left( \begin{array}{l} n \\  k \end{array}\right) {p}^{k}{\left( 1 - p\right) }^{n - k}{e}^{-\lambda }\frac{{\lambda }^{n}}{n!}
\]

\[
= \mathop{\sum }\limits_{{n = k}}^{{+\infty }}{e}^{-\lambda }\frac{{\left( p\lambda \right) }^{k}}{k!}\frac{{\left( \left( 1 - p\right) \lambda \right) }^{n - k}}{\left( {n - k}\right) !} = \frac{{\left( p\lambda \right) }^{k}}{k!}{e}^{-{p\lambda }}.
\]

Donc la probabilité d’avoir moins de \( k \) pièces avec défaut dans la même journée est

> Therefore, the probability of having fewer than \( k \) defective parts in the same day is

\[
{d}_{k} = \mathop{\sum }\limits_{{j = 0}}^{k}P\left( {B}_{j}\right)  = {e}^{-{p\lambda }}\mathop{\sum }\limits_{{j = 0}}^{k}\frac{{\left( p\lambda \right) }^{j}}{j!}.
\]

On trouve \( {d}_{3} \simeq 0,{43},{d}_{4} \simeq 0,{63} \) et \( \left( {d}_{k}\right) \) est croisssante, donc la valeur recherchée est \( k = 3 \) .

> We find \( {d}_{3} \simeq 0,{43},{d}_{4} \simeq 0,{63} \) and \( \left( {d}_{k}\right) \) is increasing, so the sought value is \( k = 3 \) .

2/a) Commençons par calculer la probabilité de l’événement \( R = \) "une pièce produite est re-jetée". Soit \( D \) l’événement "une pièce produite a un défaut". On a \( P\left( R\right) = P\left( {R \mid D}\right) P\left( D\right) + \; P\left( {R \mid {D}^{C}}\right) P\left( {D}^{C}\right) = s \) avec \( s = {qp} + r\left( {1 - p}\right) \) . Soit \( B \) l’événement "il y a 5 pièces rejetées en une seule journée". La même approche que précédemment donne

> 2/a) Let us start by calculating the probability of the event \( R = \) "a produced part is rejected". Let \( D \) be the event "a produced part has a defect". We have \( P\left( R\right) = P\left( {R \mid D}\right) P\left( D\right) + \; P\left( {R \mid {D}^{C}}\right) P\left( {D}^{C}\right) = s \) with \( s = {qp} + r\left( {1 - p}\right) \) . Let \( B \) be the event "there are 5 rejected parts in a single day". The same approach as before gives

\[
P\left( B\right)  = \mathop{\sum }\limits_{{n \geq  5}}P\left( {B \mid  {A}_{n}}\right) P\left( {A}_{n}\right)  = \mathop{\sum }\limits_{{n \geq  5}}\left( \begin{array}{l} n \\  5 \end{array}\right) {s}^{5} \times  {\left( 1 - s\right) }^{n - 5}{e}^{-\lambda }\frac{{\lambda }^{n}}{n!} = \frac{{\left( s\lambda \right) }^{5}}{5!}{e}^{-{s\lambda }}.
\]

Un calcul numérique donne \( P\left( B\right) \simeq 0,{16} \) .

> A numerical calculation gives \( P\left( B\right) \simeq 0,{16} \) .

b) On utilise la formule de Bayes pour calculer la probabilité qu'une pièce ait un défaut sachant qu'elle est rejetée :

> b) We use Bayes' formula to calculate the probability that a part has a defect given that it is rejected:

\[
P\left( {D \mid  R}\right)  = \frac{P\left( {D \cap  R}\right) }{P\left( R\right) } = \frac{P\left( {R \mid  D}\right) P\left( D\right) }{P\left( {R \mid  D}\right) P\left( D\right)  + P\left( {R \mid  {D}^{C}}\right) P\left( {D}^{C}\right) } = \frac{qp}{{qp} + r\left( {1 - p}\right) }
\]

La probabilité recherchée est celle que les 5 pièces rejetées aient toutes un défaut, donc égale à \( {\left( \frac{qp}{{qp} + r\left( {1 - p}\right) }\right) }^{5} \simeq 0,{88}. \)

> The sought probability is that all 5 rejected parts have a defect, therefore equal to \( {\left( \frac{qp}{{qp} + r\left( {1 - p}\right) }\right) }^{5} \simeq 0,{88}. \)

EXERCICE 3. Soit \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé. 1/ Si \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite d’événe-ments deux à deux disjoints. Montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) .

> EXERCISE 3. Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space. 1/ If \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) is a sequence of pairwise disjoint events. Show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) .

2/ Soit \( n \in {\mathbb{N}}^{ * } \) . Soient \( {A}_{1},\ldots ,{A}_{n} \) des événements tels que \( P\left( {A}_{k}\right) > 1 - 1/n \) pour \( 1 \leq k \leq n \) . Montrer qu’il existe un résultat \( \omega \in \Omega \) qui appartient à tous les \( {A}_{k} \) .

> 2/ Let \( n \in {\mathbb{N}}^{ * } \) . Let \( {A}_{1},\ldots ,{A}_{n} \) be events such that \( P\left( {A}_{k}\right) > 1 - 1/n \) for \( 1 \leq k \leq n \) . Show that there exists an outcome \( \omega \in \Omega \) that belongs to all \( {A}_{k} \) .

3/ Soient \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) est une suite d’événements tels que \( P\left( {A}_{n}\right) \) ne converge pas vers 0 . Montrer qu’il existe un résultat \( \omega \in \Omega \) qui appartient à une infinité de \( {A}_{k} \) .

> 3/ Let \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of events such that \( P\left( {A}_{n}\right) \) does not converge to 0 . Show that there exists an outcome \( \omega \in \Omega \) that belongs to infinitely many \( {A}_{k} \) .

Solution. 1 / La définition d’une probabilité nous assure que \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{n}\right) = P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) \) , en particulier la série \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{n}\right) \) converge, ce qui entraîne \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) .

> Solution. 1 / The definition of a probability ensures that \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{n}\right) = P\left( {{ \cup }_{n \in \mathbb{N}}{A}_{n}}\right) \) , in particular the series \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}P\left( {A}_{n}\right) \) converges, which implies \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( {A}_{n}\right) = 0 \) .

2 / Le cas \( n = 1 \) est évident car dans ce cas, \( P\left( {A}_{1}\right) > 0 \) donc \( {A}_{1} \neq \varnothing \) . Pour traiter le cas \( n = 2 \) , on écrit \( P\left( {{A}_{1} \cap {A}_{2}}\right) = P\left( {A}_{1}\right) + P\left( {A}_{2}\right) - P\left( {{A}_{1} \cup {A}_{2}}\right) > \left( {1 - 1/2}\right) + \left( {1 - 1/2}\right) - 1 = 0 \) , donc \( {A}_{1} \cap {A}_{2} \neq \varnothing \) .

> 2 / The case \( n = 1 \) is obvious because in this case, \( P\left( {A}_{1}\right) > 0 \) so \( {A}_{1} \neq \varnothing \) . To handle the case \( n = 2 \) , we write \( P\left( {{A}_{1} \cap {A}_{2}}\right) = P\left( {A}_{1}\right) + P\left( {A}_{2}\right) - P\left( {{A}_{1} \cup {A}_{2}}\right) > \left( {1 - 1/2}\right) + \left( {1 - 1/2}\right) - 1 = 0 \) , so \( {A}_{1} \cap {A}_{2} \neq \varnothing \) .

Le cas \( n = 2 \) nous invite à traiter le cas général en prouvant par récurrence sur \( k \) la propriété :

> The case \( n = 2 \) invites us to treat the general case by proving the following property by induction on \( k \) :

\[
\forall k \in  \{ 1,\ldots , n\} ,\;P\left( {{A}_{1} \cap  \ldots  \cap  {A}_{k}}\right)  > 1 - \frac{k}{n}.
\]

(*)

> C’est vrai pour \( k = 1 \) . Supposons le résultat vérifié pour \( k < n \) . Par commodité on note \( B = \; {A}_{1} \cap \ldots \cap {A}_{k} \) . On a \( P\left( B\right) > 1 - k/n \) d’après l’hypothèse de récurrence, donc

It is true for \( k = 1 \) . Assume the result holds for \( k < n \) . For convenience, we denote \( B = \; {A}_{1} \cap \ldots \cap {A}_{k} \) . We have \( P\left( B\right) > 1 - k/n \) by the induction hypothesis, so

\[
P\left( {{A}_{1} \cap  \ldots  \cap  {A}_{k} \cap  {A}_{k + 1}}\right)  = P\left( {B \cap  {A}_{k + 1}}\right)  = P\left( B\right)  + P\left( {A}_{k + 1}\right)  - P\left( {B \cup  {A}_{k + 1}}\right)
\]

\[
> \left( {1 - \frac{k}{n}}\right)  + \left( {1 - \frac{1}{n}}\right)  - 1 = 1 - \frac{k + 1}{n}\text{ . }
\]

Ainsi la propriété (*) est vraie pour tout \( k \leq n \) , en particulier pour \( k = n \) , ce qui entraîne \( P\left( {{A}_{1} \cap \ldots \cap {A}_{n}}\right) > 1 - n/n = 0 \) , donc \( {A}_{1} \cap \ldots \cap {A}_{n} \neq \varnothing \) .

> Thus the property (*) is true for all \( k \leq n \) , in particular for \( k = n \) , which implies \( P\left( {{A}_{1} \cap \ldots \cap {A}_{n}}\right) > 1 - n/n = 0 \) , so \( {A}_{1} \cap \ldots \cap {A}_{n} \neq \varnothing \) .

3/ Si les \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) sont mutuellement indépendants, le résultat est une conséquence du lemme de Borel-Cantelli (voir (ii) du théorème 1 page 326). Ici on n'a pas l'indépendance donc on procède autrement. Comme la suite \( {\left( P\left( {A}_{n}\right) \right) }_{n \in \mathbb{N}} \) ne converge pas vers 0, il existe \( \varepsilon > 0 \) tel que

> 3/ If the \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) are mutually independent, the result is a consequence of the Borel-Cantelli lemma (see (ii) of theorem 1 on page 326). Here we do not have independence, so we proceed differently. Since the sequence \( {\left( P\left( {A}_{n}\right) \right) }_{n \in \mathbb{N}} \) does not converge to 0, there exists \( \varepsilon > 0 \) such that

\[
\forall p \in  \mathbb{N},\exists n \geq  p,\;P\left( {A}_{n}\right)  \geq  \varepsilon .
\]

\( \left( {* * }\right) \)

> Ainsi, en notant \( {B}_{p} = { \cup }_{n \geq p}{A}_{n} \) , on a \( P\left( {B}_{p}\right) \geq \varepsilon \) pour tout \( p \in \mathbb{N} \) (pour tout \( p,\left( {* * }\right) \) nous assure l’existence d’un \( n \geq p \) tel que \( P\left( {A}_{n}\right) \geq \varepsilon \) , et comme \( {A}_{n} \subset {B}_{p} \) on a bien \( P\left( {B}_{p}\right) \geq P\left( {A}_{n}\right) \geq \varepsilon \) ). Comme \( {\left( {B}_{p}\right) }_{p \in \mathbb{N}} \) est une suite décroissante d’événements, on a \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}P\left( {B}_{p}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) \) , on en déduit \( P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) \geq \varepsilon \) . En particulier \( { \cap }_{p \in \mathbb{N}}{B}_{p} \) n’est pas vide. En choisissant un \( \omega \in { \cap }_{p \in \mathbb{N}}{B}_{p} \) , la définition des \( {B}_{p} \) entraîne que \( \omega \) se trouve dans une infinité de \( {A}_{n} \) , on a donc prouvé le résultat.

Thus, by denoting \( {B}_{p} = { \cup }_{n \geq p}{A}_{n} \), we have \( P\left( {B}_{p}\right) \geq \varepsilon \) for all \( p \in \mathbb{N} \) (for all \( p,\left( {* * }\right) \) ensures the existence of an \( n \geq p \) such that \( P\left( {A}_{n}\right) \geq \varepsilon \), and since \( {A}_{n} \subset {B}_{p} \) we indeed have \( P\left( {B}_{p}\right) \geq P\left( {A}_{n}\right) \geq \varepsilon \)). As \( {\left( {B}_{p}\right) }_{p \in \mathbb{N}} \) is a decreasing sequence of events, we have \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}P\left( {B}_{p}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) \), from which we deduce \( P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) \geq \varepsilon \). In particular, \( { \cap }_{p \in \mathbb{N}}{B}_{p} \) is not empty. By choosing an \( \omega \in { \cap }_{p \in \mathbb{N}}{B}_{p} \), the definition of \( {B}_{p} \) implies that \( \omega \) is in an infinite number of \( {A}_{n} \), so we have proven the result.

> EXERCICE 4. Soient \( A \) et \( B \) deux événements quelconques d’un espace probabilisé. Dé- montrer que \( \left| {P\left( {A \cap B}\right) - P\left( A\right) P\left( B\right) }\right| \leq 1/4 \) et caractériser le cas d’égalité.

EXERCISE 4. Let \( A \) and \( B \) be any two events in a probability space. Prove that \( \left| {P\left( {A \cap B}\right) - P\left( A\right) P\left( B\right) }\right| \leq 1/4 \) and characterize the equality case.

> Solution. Notons \( C = A \cap B,{A}^{\prime } = A \smallsetminus C \) et \( {B}^{\prime } = B \smallsetminus C \) . Notons \( a = P\left( {A}^{\prime }\right) , b = P\left( {B}^{\prime }\right) \) et \( c = P\left( C\right) \) . On a \( P\left( A\right) = a + c \) et \( P\left( B\right) = b + c \) , donc \( \left| {P\left( {A \cap B}\right) - P\left( A\right) P\left( B\right) }\right| = \left| {c - \left( {c + a}\right) \left( {c + b}\right) }\right| \) . Traitons deux cas :

Solution. Let us denote \( C = A \cap B,{A}^{\prime } = A \smallsetminus C \) and \( {B}^{\prime } = B \smallsetminus C \). Let us denote \( a = P\left( {A}^{\prime }\right) , b = P\left( {B}^{\prime }\right) \) and \( c = P\left( C\right) \). We have \( P\left( A\right) = a + c \) and \( P\left( B\right) = b + c \), so \( \left| {P\left( {A \cap B}\right) - P\left( A\right) P\left( B\right) }\right| = \left| {c - \left( {c + a}\right) \left( {c + b}\right) }\right| \). Let us consider two cases:

> - Cas 1. \( \operatorname{Si}\left( {c + a}\right) \left( {c + b}\right)  \geq  c \) , alors comme \( {A}^{\prime },{B}^{\prime } \) et \( C \) sont disjoints on a \( a + b + c \leq  1 \) , donc \( c + b \leq  1 - a \) , donc

- Case 1. \( \operatorname{Si}\left( {c + a}\right) \left( {c + b}\right)  \geq  c \), then since \( {A}^{\prime },{B}^{\prime } \) and \( C \) are disjoint we have \( a + b + c \leq  1 \), therefore \( c + b \leq  1 - a \), so

\[
\left| {c - \left( {c + a}\right) \left( {c + b}\right) }\right|  = \left( {c + a}\right) \left( {c + b}\right)  - c \leq  \left( {c + a}\right) \left( {1 - a}\right)  - c = a - {a}^{2} - {ac} \leq  a - {a}^{2}.
\]

(*)

> On a \( a - {a}^{2} = 1/4 - {\left( a - 1/2\right) }^{2} \leq 1/4 \) , l’inégalité est donc prouvée dans ce premier cas. Dans le cas 1, l’égalité a lieu si et seulement si \( a = 1/2 \) , et compte tenu de (*), \( {ac} = 0 \) et \( c + b = 1 - a \) , ce qui revient à avoir \( c = 0 \) et \( b = 1/2 \) . Autrement dit, l’égalité a lieu lorsque \( A \cap B \) est négligeable et \( P\left( A\right) = P\left( B\right) = 1/2 \) (notons que dans le cas d’égalité, \( P\left( {A \cup B}\right) = P\left( A\right) + P\left( B\right) - P\left( {A \cap B}\right) = 1 \) , i.e. \( A \cup B \) est presque sûr).

We have \( a - {a}^{2} = 1/4 - {\left( a - 1/2\right) }^{2} \leq 1/4 \), so the inequality is proven in this first case. In case 1, equality holds if and only if \( a = 1/2 \), and given (*), \( {ac} = 0 \) and \( c + b = 1 - a \), which amounts to having \( c = 0 \) and \( b = 1/2 \). In other words, equality holds when \( A \cap B \) is negligible and \( P\left( A\right) = P\left( B\right) = 1/2 \) (note that in the case of equality, \( P\left( {A \cup B}\right) = P\left( A\right) + P\left( B\right) - P\left( {A \cap B}\right) = 1 \), i.e., \( A \cup B \) is almost sure).

> - Cas 2. Si \( c > \left( {c + a}\right) \left( {c + b}\right) \) , alors l’inégalité souhaitée est bien vraie car

- Case 2. If \( c > \left( {c + a}\right) \left( {c + b}\right) \), then the desired inequality is indeed true because

\[
\left| {c - \left( {c + a}\right) \left( {c + b}\right) }\right|  = c - \left( {c + a}\right) \left( {c + b}\right)  \leq  c - {c}^{2}.
\]

\( \left( {* * }\right) \)

> Le cas d’égalité se produit lorsque \( c = 1/2 \) et \( \left( {c + a}\right) \left( {c + b}\right) = {c}^{2} \) , donc \( a = b = 0 \) . Autrement dit, l’égalité se produit lorsque \( P\left( A\right) = P\left( B\right) = 1/2 \) et lorsque \( {A}^{\prime } \) et \( {B}^{\prime } \) sont négligeables (c’est-à-dire lorsque \( A = B \) à un ensemble négligeable près).

The equality case occurs when \( c = 1/2 \) and \( \left( {c + a}\right) \left( {c + b}\right) = {c}^{2} \), therefore \( a = b = 0 \). In other words, equality occurs when \( P\left( A\right) = P\left( B\right) = 1/2 \) and when \( {A}^{\prime } \) and \( {B}^{\prime } \) are negligible (that is, when \( A = B \) up to a negligible set).

> EXERCICE 5. Alice et Zoé jouent à pile ou face en lançant indéfiniment une pièce non équilibrée, dont la probabilité de tomber sur pile est \( p \in \rbrack 0,1\lbrack \) . Alice gagne dès que la séquence "FFP" (face-face-pile) est apparue, alors que la séquence "FPP" n'est pas encore apparue. Bernard gagne dès que la séquence "FPP" est apparue, alors que la séquence "FFP" n'est pas encore apparue. Déterminer la probabilité de gain de Alice, et de Bernard. Peut-on trouver une valeur de \( p \) telle qu’Alice et Bernard aient la même probabilité de gain? (indication : on pourra considérer la série génératrice \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) où \( {a}_{n} \) est la probabilité de gain au \( n \) -ième lancer.)

EXERCISE 5. Alice and Zoé play heads or tails by tossing an unfair coin indefinitely, where the probability of landing on heads is \( p \in \rbrack 0,1\lbrack \). Alice wins as soon as the sequence "TTH" (tails-tails-heads) has appeared, while the sequence "THH" has not yet appeared. Bernard wins as soon as the sequence "THH" has appeared, while the sequence "TTH" has not yet appeared. Determine the probability of Alice winning, and of Bernard winning. Can we find a value of \( p \) such that Alice and Bernard have the same probability of winning? (hint: one may consider the generating series \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) where \( {a}_{n} \) is the probability of winning at the \( n \)-th toss.)

> Solution. Supposons que Alice ou Zoé gagne au \( n \) -ième lancer. Soit \( w = \left( {{w}_{1},\ldots ,{w}_{n}}\right) \) la \( n \) -liste de \( \{ \mathrm{P},\mathrm{F}\} \) (pile ou face) correspondante. On a \( n \geq 3 \) . Notons \( {w}^{\prime } \) la \( \left( {n - 3}\right) \) -liste des \( n - 3 \) premières lettres de \( w \) . En étudiant les enchaînements possibles de "P" et de "F", on s’aperçoit que \( {w}^{\prime } \) a la forme d'une séquence de "P", suivi d'une séquence de "FP", suivi d'une séquence de "F" (ces séquences pouvant chacune être vide), ce qu’on note sous la forme \( {w}^{\prime } = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \) . Pour prouver ce résultat on traite plusieurs cas :

Solution. Suppose that Alice or Zoé wins at the \( n \)-th toss. Let \( w = \left( {{w}_{1},\ldots ,{w}_{n}}\right) \) be the corresponding \( n \)-list of \( \{ \mathrm{P},\mathrm{F}\} \) (heads or tails). We have \( n \geq 3 \). Let \( {w}^{\prime } \) be the \( \left( {n - 3}\right) \)-list of the first \( n - 3 \) letters of \( w \). By studying the possible sequences of "H" and "T", we notice that \( {w}^{\prime } \) has the form of a sequence of "H", followed by a sequence of "TH", followed by a sequence of "T" (these sequences each possibly being empty), which we denote in the form \( {w}^{\prime } = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \). To prove this result, we treat several cases:

> - \( {w}^{\prime } \) ne contient pas la lettre "F". Alors \( {w}^{\prime } \) ne contient que la lettre "P" : \( {w}^{\prime } = {\mathrm{P}}^{n - 3} \) .

- \( {w}^{\prime } \) does not contain the letter "F". Then \( {w}^{\prime } \) only contains the letter "P": \( {w}^{\prime } = {\mathrm{P}}^{n - 3} \) .

> - Sinon il existe un plus petit entier \( q \in  \mathbb{N} \) tel que \( {w}_{q + 1} = \mathrm{F} \) . On a deux cas :

- Otherwise, there exists a smallest integer \( q \in  \mathbb{N} \) such that \( {w}_{q + 1} = \mathrm{F} \) . We have two cases:

> - soit il n’y a que des "F" dans \( {w}^{\prime } \) après la position \( q \) . Alors \( {w}^{\prime } = {\mathrm{P}}^{q}{\mathrm{\;F}}^{s} \) avec \( p + s = n - 3 \) .

- either there are only "F"s in \( {w}^{\prime } \) after position \( q \). Then \( {w}^{\prime } = {\mathrm{P}}^{q}{\mathrm{\;F}}^{s} \) with \( p + s = n - 3 \).

> - sinon le premier "F" est immédiatement suivi d'un "P" (sinon, comme on a un "P" entre ce "F" et la fin de \( {w}^{\prime } \) , la séquence "FFP" arriverait avant la position \( n \) ). On note \( r \) le nombre de "FP" consécutifs (à partir de la position \( q + 1 \) ). Si \( q + {2r} < n - 3 \) , après le "FP" se terminant à la position \( q + {2r} \) , on a forcément un " \( F \) " (sinon la séquence "FPP" arriverait avant la position \( n \) ). Si \( q + {2r} + 1 < n - 3 \) on doit encore avoir un "F" (par définition de \( r \) ce ne peut pas être un "P"), puis uniquement des "F" (sinon "FFP" arriverait avant la position \( n \) ). En résumé, on ne peut avoir qu’une séquence de "F" commençant à la position \( q + {2r} + 1 \) , jusque la fin de \( {w}^{\prime } \) , et donc \( {w}^{\prime } = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \) .

- otherwise the first "F" is immediately followed by a "P" (otherwise, since there is a "P" between this "F" and the end of \( {w}^{\prime } \), the sequence "FFP" would occur before position \( n \)). Let \( r \) be the number of consecutive "FP"s (starting from position \( q + 1 \)). If \( q + {2r} < n - 3 \), after the "FP" ending at position \( q + {2r} \), there must be an " \( F \) " (otherwise the sequence "FPP" would occur before position \( n \)). If \( q + {2r} + 1 < n - 3 \) we must still have an "F" (by definition of \( r \) it cannot be a "P"), then only "F"s (otherwise "FFP" would occur before position \( n \)). In summary, we can only have a sequence of "F"s starting at position \( q + {2r} + 1 \), until the end of \( {w}^{\prime } \), and therefore \( {w}^{\prime } = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \).

> En résumé, nous venons de montrer que \( {w}^{\prime } \) est forcément de la forme \( {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \) où \( \left( {q, r, s}\right) \in {\mathbb{N}}^{3} \) sont tels que \( q + {2r} + s = n - 3 \) . On en déduit que les séquences de gain \( w \) ont la forme suivante :

In summary, we have just shown that \( {w}^{\prime } \) is necessarily of the form \( {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s} \) where \( \left( {q, r, s}\right) \in {\mathbb{N}}^{3} \) are such that \( q + {2r} + s = n - 3 \). We deduce that the winning sequences \( w \) have the following form:

> (i) Si Alice gagne, \( w = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s}\mathrm{{FFP}} \) , avec \( q, r, s \in \mathbb{N}, q + {2r} + s = n - 3 \) .

(i) If Alice wins, \( w = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}{\mathrm{\;F}}^{s}\mathrm{{FFP}} \), with \( q, r, s \in \mathbb{N}, q + {2r} + s = n - 3 \).

> (ii) Si Zoé gagne, \( w = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}\mathrm{{FP}} \) , avec \( q, r \in \mathbb{N}, q + {2r} = n - 3 \) .

(ii) If Zoé wins, \( w = {\mathrm{P}}^{q}{\left( \mathrm{{FP}}\right) }^{r}\mathrm{{FP}} \), with \( q, r \in \mathbb{N}, q + {2r} = n - 3 \).

> Réciproquement il est clair que ces séquences sont bien associées à celles où Alice ou Zoé gagnent au \( n \) -ième lancer.

Conversely, it is clear that these sequences are indeed associated with those where Alice or Zoé wins at the \( n \)-th toss.

> Calculons maintenant \( {a}_{n} \) la probabilité de gain d’Alice au \( n \) -ième lancer. D’après (i) et sa réciproque, on a

Let us now calculate \( {a}_{n} \), the probability of Alice winning at the \( n \)-th toss. According to (i) and its converse, we have

\[
{a}_{n} = \left( {\mathop{\sum }\limits_{\substack{{q, r, s \in  \mathbb{N}} \\  {q + {2r} + s = n - 3} }}{p}^{q}{\left( p\left( 1 - p\right) \right) }^{r}{\left( 1 - p\right) }^{s}}\right) {\left( 1 - p\right) }^{2}p.
\]

En considérant les trois séries entières

> By considering the three power series

\[
Q\left( z\right)  = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{p}^{q}{z}^{q},\;R\left( z\right)  = \mathop{\sum }\limits_{{r = 0}}^{{+\infty }}{p}^{r}{\left( 1 - p\right) }^{r}{z}^{2r},\;S\left( z\right)  = \mathop{\sum }\limits_{{s = 0}}^{{+\infty }}{\left( 1 - p\right) }^{s}{z}^{s},
\]

dont le rayon de convergence est \( \geq 1 \) , un produit de Cauchy nous assure que la série génératrice \( A\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) (de rayon de convergence \( \geq 1 \) ) vérifie, pour \( \left| z\right| < 1 \)

> whose radius of convergence is \( \geq 1 \), a Cauchy product ensures that the generating series \( A\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) (with radius of convergence \( \geq 1 \)) satisfies, for \( \left| z\right| < 1 \)

\[
{z}^{3}A\left( z\right)  = Q\left( z\right) R\left( z\right) S\left( z\right) {\left( 1 - p\right) }^{2}p = \frac{1}{1 - {pz}} \cdot  \frac{1}{1 - p\left( {1 - p}\right) {z}^{2}} \cdot  \frac{1}{1 - \left( {1 - p}\right) z}{\left( 1 - p\right) }^{2}p.
\]

Les séries de fonctions en jeu convergent absolument pour \( z \in \left\lbrack {-1,1}\right\rbrack \) , donc sont définies et continues sur ce domaine et on en déduit que la probabilité de gain de Alice est

> The series of functions involved converge absolutely for \( z \in \left\lbrack {-1,1}\right\rbrack \), so they are defined and continuous on this domain, and we deduce that Alice's probability of winning is

\[
a = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n} = A\left( 1\right)  = Q\left( 1\right) R\left( 1\right) S\left( 1\right) {\left( 1 - p\right) }^{2}p = \frac{{\left( 1 - p\right) }^{2}p}{\left( {1 - p}\right) \left( {1 - p\left( {1 - p}\right) }\right) p} = \frac{1 - p}{1 - p\left( {1 - p}\right) }.
\]

En notant \( {b}_{n} \) la probabilité de gain de Zoé au \( n \) -ième lancer, la même approche permet de montrer, d’après (ii) et sa réciproque, que la série entière \( B\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{z}^{n} \) vérifie \( {z}^{3}B\left( z\right) = \; Q\left( z\right) R\left( z\right) \left( {1 - p}\right) {p}^{2} \) puis que la probabilité de gain de Zoé est

> By denoting \( {b}_{n} \) as the probability of Zoé winning on the \( n \) -th toss, the same approach allows us to show, according to (ii) and its converse, that the power series \( B\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{z}^{n} \) satisfies \( {z}^{3}B\left( z\right) = \; Q\left( z\right) R\left( z\right) \left( {1 - p}\right) {p}^{2} \) and then that the probability of Zoé winning is

\[
b = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n} = B\left( 1\right)  = Q\left( 1\right) R\left( 1\right) \left( {1 - p}\right) {p}^{2} = \frac{\left( {1 - p}\right) {p}^{2}}{\left( {1 - p}\right) \left( {1 - p\left( {1 - p}\right) }\right) } = \frac{{p}^{2}}{1 - p\left( {1 - p}\right) }.
\]

On remarque que \( a + b = 1 \) , donc presque surement, Alice ou Zoé gagne.

> We note that \( a + b = 1 \) , therefore almost surely, Alice or Zoé wins.

Pour avoir \( a = b \) , compte tenu des valeurs obtenues plus haut, il suffit de choisir \( p \) tel que \( 1 - p = {p}^{2} \) , dont il existe une unique solution dans \( \left\lbrack {0,1}\right\rbrack \) qui est \( p = \left( {\sqrt{5} - 1}\right) /2 \simeq 0,{618} \) .

> To have \( a = b \) , given the values obtained above, it suffices to choose \( p \) such that \( 1 - p = {p}^{2} \) , for which there exists a unique solution in \( \left\lbrack {0,1}\right\rbrack \) which is \( p = \left( {\sqrt{5} - 1}\right) /2 \simeq 0,{618} \) .

EXERCICE 6. On lance indéfiniment une pièce de monnaie non équilibrée, dont la probabi-lité de tomber sur pile est \( p \in \rbrack 0,1\left\lbrack \right. \) . On note \( \Omega = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \) l’ensemble des suites possibles de "pile" ou "face" correspondantes.

> EXERCISE 6. We toss a biased coin indefinitely, where the probability of landing on heads is \( p \in \rbrack 0,1\left\lbrack \right. \) . Let \( \Omega = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \) be the set of possible sequences of "heads" or "tails" corresponding to this.

1/ a) Soit \( N \in {\mathbb{N}}^{ * } \) et \( a = \left( {{a}_{1},\ldots ,{a}_{N}}\right) \) une \( N \) -liste de \( \{ \mathrm{P},\mathrm{F}\} \) . Montrer que l’ensemble

> 1/ a) Let \( N \in {\mathbb{N}}^{ * } \) and \( a = \left( {{a}_{1},\ldots ,{a}_{N}}\right) \) be a \( N \) -list of \( \{ \mathrm{P},\mathrm{F}\} \) . Show that the set

\[
A = \left\{  {w = {\left( {w}_{i}\right) }_{i \in  {\mathbb{N}}^{ * }} \in  \Omega \mid \exists n \in  {\mathbb{N}}^{ * },{w}_{n + 1} = {a}_{1},\ldots ,{w}_{n + N} = {a}_{N}}\right\}
\]

est presque sûr.

> is almost sure.

b) Montrer l'existence d'événement négligeable et infini non dénombrable.

> b) Show the existence of a negligible and uncountable infinite event.

2/ Soit \( \alpha > 0 \) . Pour tout \( n \) on note \( {A}_{n} \) l’événement "la suite a au moins \( \alpha \log n \) piles consécutifs à partir de la position \( n \) ", c'est-à-dire

> 2/ Let \( \alpha > 0 \) . For any \( n \) , we denote by \( {A}_{n} \) the event "the sequence has at least \( \alpha \log n \) consecutive heads starting from position \( n \) ", that is to say

\[
{A}_{n} = \left\{  {w = {\left( {w}_{i}\right) }_{i \in  {\mathbb{N}}^{ * }} \in  \Omega  \mid  {w}_{n + 1} = \ldots  = {w}_{n + \ell \left( n\right) } = \mathrm{P}}\right\}  ,\;\ell \left( n\right)  = \lceil \alpha \log n\rceil ,
\]

(où \( \lceil x\rceil \) désigne le plus petit entier \( \geq x \) ).

> (where \( \lceil x\rceil \) denotes the smallest integer \( \geq x \) ).

a) Lorsque \( \alpha > 1/\log \left( {1/p}\right) \) , montrer que presque surement, les suites de \( \Omega \) ont au plus un nombre fini de \( n \) tels qu’il y a au moins \( \alpha \log n \) piles consécutifs à partir de la position \( n \) . b) Lorsque \( \alpha \leq 1/\log \left( {1/p}\right) \) , montrer que presque surement, les suites de \( \Omega \) ont un nombre infini de \( n \) tels qu’il y a au moins \( \alpha \log n \) piles consécutifs à partir de la position \( n \) .

> a) When \( \alpha > 1/\log \left( {1/p}\right) \) , show that almost surely, the sequences of \( \Omega \) have at most a finite number of \( n \) such that there are at least \( \alpha \log n \) consecutive heads starting from position \( n \) . b) When \( \alpha \leq 1/\log \left( {1/p}\right) \) , show that almost surely, the sequences of \( \Omega \) have an infinite number of \( n \) such that there are at least \( \alpha \log n \) consecutive heads starting from position \( n \) .

Solution. 1/a) On va construire un événement plus petit, presque sûr, ce qui montrera que \( A \) est presque sûr. Pour tout \( p \in \mathbb{N} \) , notons \( {A}_{p} = \left\{ {w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \mid {w}_{{pN} + 1} = {a}_{1},\ldots ,{w}_{{pN} + N} = {a}_{N}}\right\} \) . Les événements \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \) sont mutuellement indépendants, la probabilité de chacun est \( P\left( {A}_{p}\right) = \; P\left( {A}_{0}\right) > 0 \) , donc la série \( \mathop{\sum }\limits_{p}P\left( {A}_{p}\right) \) diverge. On peut donc appliquer le lemme de Borel-Cantelli (assertion (ii), voir le théorème 1 page 326), qui entraîne que \( B = { \cap }_{n \in \mathbb{N}}{ \cup }_{p \geq n}{A}_{p} \) est presque sûr. Toute suite \( w \) dans \( B \) appartient à une infinité de \( {A}_{p} \) , donc vérifie en particulier \( {w}_{n + 1} = \; {a}_{1},\ldots ,{w}_{n + N} = {a}_{N} \) pour une infinité de valeurs de \( n \) . Donc \( B \subset A \) , donc \( P\left( A\right) \geq P\left( B\right) = 1 \) ce qui prouve que \( A \) est presque sûr.

> Solution. 1/a) We will construct a smaller, almost sure event, which will show that \( A \) is almost sure. For any \( p \in \mathbb{N} \) , let us denote \( {A}_{p} = \left\{ {w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \mid {w}_{{pN} + 1} = {a}_{1},\ldots ,{w}_{{pN} + N} = {a}_{N}}\right\} \) . The events \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \) are mutually independent, the probability of each is \( P\left( {A}_{p}\right) = \; P\left( {A}_{0}\right) > 0 \) , so the series \( \mathop{\sum }\limits_{p}P\left( {A}_{p}\right) \) diverges. We can therefore apply the Borel-Cantelli lemma (assertion (ii), see theorem 1 page 326), which implies that \( B = { \cap }_{n \in \mathbb{N}}{ \cup }_{p \geq n}{A}_{p} \) is almost sure. Any sequence \( w \) in \( B \) belongs to an infinite number of \( {A}_{p} \) , and therefore satisfies \( {w}_{n + 1} = \; {a}_{1},\ldots ,{w}_{n + N} = {a}_{N} \) for an infinite number of values of \( n \) . Thus \( B \subset A \) , therefore \( P\left( A\right) \geq P\left( B\right) = 1 \) which proves that \( A \) is almost sure.

b) On choisit un cas particulier de la question précédente : \( N = 2 \) et \( a = \left( {\mathrm{P},\mathrm{P}}\right) \) . D’après la question précédente, l’événement \( A = \left\{ {w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \mid \exists n \in {\mathbb{N}}^{ * },{w}_{n + 1} = {w}_{n + 2} = \mathrm{P}}\right\} \) est presque sûr. Donc son complémentaire \( C \) , qui est l’ensemble des suites n’ayant jamais deux "pile" consécutifs, est négligeable. On va montrer que \( C \) est infini non dénombrable. Pour cela on considère l'ensemble des suites

> b) We choose a special case of the previous question: \( N = 2 \) and \( a = \left( {\mathrm{P},\mathrm{P}}\right) \) . According to the previous question, the event \( A = \left\{ {w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \mid \exists n \in {\mathbb{N}}^{ * },{w}_{n + 1} = {w}_{n + 2} = \mathrm{P}}\right\} \) is almost sure. Therefore its complement \( C \) , which is the set of sequences never having two consecutive "heads", is negligible. We will show that \( C \) is uncountable. To do this, we consider the set of sequences

\[
D = \left\{  {w = {\left( {w}_{i}\right) }_{i \in  {\mathbb{N}}^{ * }} \in  \Omega \mid \forall n \in  \mathbb{N},\left( {{w}_{{2n} + 1},{w}_{{2n} + 2}}\right)  \in  \{ \left( {\mathrm{F},\mathrm{F}}\right) ,\left( {\mathrm{F},\mathrm{P}}\right) \} }\right\}  .
\]

On a \( D \subset C \) . On va montrer que \( D \) est infini non dénombrable, en utilisanr un procédé diagonal, similaire à celui utilisé pour la preuve de la non-dénombrabilité de \( \mathbb{R} \) . Raisonnons par l'absurde et supposons \( D \) dénombrable, de sorte qu’il existe une bijection \( \varphi : \mathbb{N} \rightarrow D \) . On note \( {x}_{n, i} \in \{ \mathrm{P},\mathrm{F}\} \) le \( i \) -ième terme de la suite \( \varphi \left( n\right) \) . On construit la suite \( w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \) comme suit : pour tout \( i \in \mathbb{N} \) , on choisit \( \left( {{w}_{{2i} + 1},{w}_{{2i} + 2}}\right) \in \{ \left( {\mathrm{F},\mathrm{F}}\right) ,\left( {\mathrm{F},\mathrm{P}}\right) \} \smallsetminus \left\{ \left( {{x}_{i,{2i} + 1},{x}_{i,{2i} + 2}}\right) \right\} \) (il n’y a qu’un seul élément possible). Comme \( w \in D \) , il existe \( n \in \mathbb{N} \) tel que \( w = \varphi \left( n\right) \) , ce qui entraîne \( \left( {{w}_{{2n} + 1},{w}_{{2n} + 2}}\right) = \; \left( {{x}_{n,{2n} + 1},{x}_{n,{2n} + 2}}\right) \) , et ceci est absurde étant donnée la définition de \( w \) . Donc \( D \) est infini non dénombrable, donc c’est aussi le cas pour \( C \) car \( D \subset C \) .

> We have \( D \subset C \) . We will show that \( D \) is uncountably infinite, using a diagonal argument similar to the one used for the proof of the uncountability of \( \mathbb{R} \) . Let us reason by contradiction and assume \( D \) is countable, such that there exists a bijection \( \varphi : \mathbb{N} \rightarrow D \) . We denote \( {x}_{n, i} \in \{ \mathrm{P},\mathrm{F}\} \) as the \( i \) -th term of the sequence \( \varphi \left( n\right) \) . We construct the sequence \( w = {\left( {w}_{i}\right) }_{i \in {\mathbb{N}}^{ * }} \in \Omega \) as follows: for all \( i \in \mathbb{N} \) , we choose \( \left( {{w}_{{2i} + 1},{w}_{{2i} + 2}}\right) \in \{ \left( {\mathrm{F},\mathrm{F}}\right) ,\left( {\mathrm{F},\mathrm{P}}\right) \} \smallsetminus \left\{ \left( {{x}_{i,{2i} + 1},{x}_{i,{2i} + 2}}\right) \right\} \) (there is only one possible element). Since \( w \in D \) , there exists \( n \in \mathbb{N} \) such that \( w = \varphi \left( n\right) \) , which implies \( \left( {{w}_{{2n} + 1},{w}_{{2n} + 2}}\right) = \; \left( {{x}_{n,{2n} + 1},{x}_{n,{2n} + 2}}\right) \) , and this is absurd given the definition of \( w \) . Therefore, \( D \) is uncountably infinite, and thus the same is true for \( C \) because \( D \subset C \) .

2/a) La probabilité de \( {A}_{n} \) est \( {p}^{\ell \left( n\right) } \leq {p}^{\alpha \log n} = {n}^{\alpha \log p} \) . Ainsi on a \( P\left( {A}_{n}\right) \leq {n}^{-\beta } \) avec \( \beta = \; \alpha \log \left( {1/p}\right) > 1 \) . Donc la série \( \mathop{\sum }\limits_{n}P\left( {A}_{n}\right) \) converge, et d’après le lemme de Borel-Cantelli (assertion

> 2/a) The probability of \( {A}_{n} \) is \( {p}^{\ell \left( n\right) } \leq {p}^{\alpha \log n} = {n}^{\alpha \log p} \) . Thus we have \( P\left( {A}_{n}\right) \leq {n}^{-\beta } \) with \( \beta = \; \alpha \log \left( {1/p}\right) > 1 \) . Therefore, the series \( \mathop{\sum }\limits_{n}P\left( {A}_{n}\right) \) converges, and according to the Borel-Cantelli lemma (assertion

(i)), on en déduit que \( { \cap }_{n \in {\mathbb{N}}^{ * }}{ \cup }_{p \geq n}{A}_{p} \) est négligeable. Donc, presque surement toute suite \( w \) n’appartient qu’à un nombre fini de \( {A}_{n} \) , ce qu’il fallait démontrer.

> (i)), we deduce that \( { \cap }_{n \in {\mathbb{N}}^{ * }}{ \cup }_{p \geq n}{A}_{p} \) is negligible. Thus, almost surely, any sequence \( w \) belongs to only a finite number of \( {A}_{n} \) , which was to be demonstrated.

b) Ici on ne peut pas appliquer directement l'assertion (ii) du lemme de Borel-Cantelli car les \( \left( {A}_{n}\right) \) ne sont pas mutuellement indépendants. On s’en sort en se restreignant à une sous-suite de \( \left( {A}_{n}\right) \) tels que les indices des suites impliqués dans la définition des \( {A}_{n} \) ne se chevauchent pas. On choisit \( {B}_{n} = {A}_{{m}_{n}} \) avec \( {m}_{n} = {2n}\ell \left( n\right) \) . Il existe \( N \in \mathbb{N} \) tel que pour tout \( n \geq N \) ,

> b) Here we cannot directly apply assertion (ii) of the Borel-Cantelli lemma because the \( \left( {A}_{n}\right) \) are not mutually independent. We get around this by restricting ourselves to a subsequence of \( \left( {A}_{n}\right) \) such that the indices of the sequences involved in the definition of the \( {A}_{n} \) do not overlap. We choose \( {B}_{n} = {A}_{{m}_{n}} \) with \( {m}_{n} = {2n}\ell \left( n\right) \) . There exists \( N \in \mathbb{N} \) such that for all \( n \geq N \) ,

\[
\ell \left( {m}_{n}\right)  \leq  1 + \alpha \log \left( {{2n}\ell \left( n\right) }\right)  = 1 + \alpha \log n + \alpha \log \left( {2\ell \left( n\right) }\right)  < {2\alpha }\log n \leq  2\ell \left( n\right) .
\]

Lorsque \( n \geq N \) , on a donc \( {m}_{n + 1} = 2\left( {n + 1}\right) \ell \left( {n + 1}\right) \geq 2\left( {n + 1}\right) \ell \left( n\right) = {m}_{n} + 2\ell \left( n\right) > {m}_{n} + \ell \left( {m}_{n}\right) \) . Ainsi les ensembles d’indices \( \left\{ {{m}_{n} + 1,\ldots ,{m}_{n} + \ell \left( {m}_{n}\right) }\right\} \) impliqués dans la définition de \( {B}_{n} \) sont disjoints lorsque \( n \geq N \) , ce qui entraîne que les \( {\left( {B}_{n}\right) }_{n \geq N} \) sont mutuellement indépendants. La probabilité de \( {B}_{n} \) vérifie

> When \( n \geq N \) , we have \( {m}_{n + 1} = 2\left( {n + 1}\right) \ell \left( {n + 1}\right) \geq 2\left( {n + 1}\right) \ell \left( n\right) = {m}_{n} + 2\ell \left( n\right) > {m}_{n} + \ell \left( {m}_{n}\right) \) . Thus, the index sets \( \left\{ {{m}_{n} + 1,\ldots ,{m}_{n} + \ell \left( {m}_{n}\right) }\right\} \) involved in the definition of \( {B}_{n} \) are disjoint when \( n \geq N \) , which implies that the \( {\left( {B}_{n}\right) }_{n \geq N} \) are mutually independent. The probability of \( {B}_{n} \) satisfies

\[
P\left( {B}_{n}\right)  = {p}^{\ell \left( {m}_{n}\right) } \geq  {p}^{\alpha \log {m}_{n} + 1} = p{m}_{n}^{\alpha \log p} = \frac{p}{{\left( 2n\ell \left( n\right) \right) }^{\alpha \log \left( {1/p}\right) }} \geq  \frac{p}{{2n}\ell \left( n\right) }.
\]

Comme \( \frac{p}{{2n}\ell \left( n\right) } \sim \frac{p/\left( {2\alpha }\right) }{n\log n} \) , on en déduit que la série \( \mathop{\sum }\limits_{{n \geq N}}P\left( {B}_{n}\right) \) diverge. On peut appliquer l’assertion (ii) du lemme de Borel-Cantelli, qui entraîne que \( { \cap }_{n \geq N}{ \cup }_{p \geq n}{B}_{n} \) est presque sûr. Donc presque surement, toute suite de \( \Omega \) appartient à une infinité de \( {B}_{n} \) , donc à une infinité de \( {A}_{m} \) , ce qu'il fallait démontrer.

> Since \( \frac{p}{{2n}\ell \left( n\right) } \sim \frac{p/\left( {2\alpha }\right) }{n\log n} \) , we deduce that the series \( \mathop{\sum }\limits_{{n \geq N}}P\left( {B}_{n}\right) \) diverges. We can apply assertion (ii) of the Borel-Cantelli lemma, which implies that \( { \cap }_{n \geq N}{ \cup }_{p \geq n}{B}_{n} \) is almost sure. Therefore, almost surely, any sequence of \( \Omega \) belongs to infinitely many \( {B}_{n} \) , and thus to infinitely many \( {A}_{m} \) , which was to be demonstrated.

EXERCICE 7. On note \( \mathcal{P} \) l’ensemble des nombres premiers.

> EXERCISE 7. Let \( \mathcal{P} \) be the set of prime numbers.

1/ Soit \( s > 1 \) . On note \( \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}} \) (fonction zêta de Riemann), et on définit une probabilité \( P \) sur \( {\mathbb{N}}^{ * } \) par

> 1/ Let \( s > 1 \) . We denote \( \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}} \) (Riemann zeta function), and we define a probability \( P \) on \( {\mathbb{N}}^{ * } \) by

\[
\forall n \in  {\mathbb{N}}^{ * },\;P\left( {\{ n\} }\right)  = \frac{1}{\zeta \left( s\right) }\frac{1}{{n}^{s}}.
\]

a) Pour tout \( q \in {\mathbb{N}}^{ * } \) , on note \( {A}_{q} = q{\mathbb{N}}^{ * } \) . Montrer que les événements \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) sont mutuellement indépendants.

> a) For all \( q \in {\mathbb{N}}^{ * } \) , we denote \( {A}_{q} = q{\mathbb{N}}^{ * } \) . Show that the events \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) are mutually independent.

b) En notant \( {p}_{1} < {p}_{2} < \ldots \) les nombres premiers dans l’ordre croissant, en déduire que

> b) By denoting \( {p}_{1} < {p}_{2} < \ldots \) the prime numbers in increasing order, deduce that

\[
\frac{1}{\zeta \left( s\right) } = \mathop{\prod }\limits_{{k = 1}}^{{+\infty }}\left( {1 - \frac{1}{{p}_{k}^{s}}}\right) .
\]

c) Déterminer la nature de la série \( \mathop{\sum }\limits_{{k \geq 1}}1/{p}_{k} \) .

> c) Determine the nature of the series \( \mathop{\sum }\limits_{{k \geq 1}}1/{p}_{k} \) .

2/a) Montrer qu’il n’existe pas de probabilité \( P \) sur \( {\mathbb{N}}^{ * } \) telle que \( P\left( {A}_{q}\right) = 1/q \) pour tout \( q \in {\mathbb{N}}^{ * } \) .

> 2/a) Show that there is no probability \( P \) on \( {\mathbb{N}}^{ * } \) such that \( P\left( {A}_{q}\right) = 1/q \) for all \( q \in {\mathbb{N}}^{ * } \) .

b) Soit \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}u\left( n\right) \) une série à termes positifs et convergente. Montrer qu’il n’existe pas de probabilité \( P \) sur \( {\mathbb{N}}^{ * } \) telle que \( \left| {P\left( {A}_{q}\right) - 1/q}\right| < u\left( q\right) \) pour tout \( q \in {\mathbb{N}}^{ * } \) .

> b) Let \( \mathop{\sum }\limits_{{n \in {\mathbb{N}}^{ * }}}u\left( n\right) \) be a convergent series with positive terms. Show that there is no probability \( P \) on \( {\mathbb{N}}^{ * } \) such that \( \left| {P\left( {A}_{q}\right) - 1/q}\right| < u\left( q\right) \) for all \( q \in {\mathbb{N}}^{ * } \) .

Solution. \( \mathbf{1}/\mathbf{a} \) ) On commence par remarquer que pour tout \( q \in {\mathbb{N}}^{ * } \) , on a

> Solution. \( \mathbf{1}/\mathbf{a} \) ) We begin by noting that for all \( q \in {\mathbb{N}}^{ * } \) , we have

\[
P\left( {A}_{q}\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{\zeta \left( s\right) }\frac{1}{{\left( qn\right) }^{s}} = \frac{1}{{q}^{s}}.
\]

Par ailleurs, lorsque \( q, r \) sont premiers entre eux, \( {A}_{qr} \) est l’ensemble des nombres entiers divisibles par \( q \) et par \( r \) , donc \( {A}_{qr} = {A}_{q} \cap {A}_{r} \) . Considérons maintenant \( k \) nombres premiers distincts \( {p}_{1},\ldots ,{p}_{k} \) . L’observation précédente entraîne \( {A}_{{p}_{1}\cdots {p}_{k}} = {A}_{{p}_{1}} \cap \ldots \cap {A}_{{p}_{k}} \) donc on a

> Furthermore, when \( q, r \) are coprime, \( {A}_{qr} \) is the set of integers divisible by \( q \) and by \( r \) , therefore \( {A}_{qr} = {A}_{q} \cap {A}_{r} \) . Now consider \( k \) distinct prime numbers \( {p}_{1},\ldots ,{p}_{k} \) . The previous observation implies \( {A}_{{p}_{1}\cdots {p}_{k}} = {A}_{{p}_{1}} \cap \ldots \cap {A}_{{p}_{k}} \) so we have

\[
P\left( {{A}_{{p}_{1}} \cap  \ldots  \cap  {A}_{{p}_{k}}}\right)  = P\left( {A}_{{p}_{1}\cdots {p}_{k}}\right)  = \frac{1}{{\left( {p}_{1}\cdots {p}_{k}\right) }^{s}} = \frac{1}{{p}_{1}^{s}}\cdots \frac{1}{{p}_{k}^{s}} = P\left( {A}_{1}\right) \cdots P\left( {A}_{k}\right) ,
\]

ce qui prouve bien l’indépendance des \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) .

> which clearly proves the independence of \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) .

b) Comme les \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) sont indépendants, les \( {\left( \overline{{A}_{p}}\right) }_{p \in \mathcal{P}} \) également (où \( \bar{A} \) désigne le complémen-taire de \( A \) ). Ainsi pour tout \( K \in {\mathbb{N}}^{ * } \) , l’événement \( {B}_{K} = { \cap }_{k = 1}^{K}\overline{{A}_{{p}_{k}}} \) , qui est l’ensemble des entiers divisibles par aucun des \( {\left( {p}_{k}\right) }_{1 \leq k \leq K} \) , vérifie

> b) Since the \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) are independent, the \( {\left( \overline{{A}_{p}}\right) }_{p \in \mathcal{P}} \) are as well (where \( \bar{A} \) denotes the complement of \( A \) ). Thus for any \( K \in {\mathbb{N}}^{ * } \) , the event \( {B}_{K} = { \cap }_{k = 1}^{K}\overline{{A}_{{p}_{k}}} \) , which is the set of integers divisible by none of the \( {\left( {p}_{k}\right) }_{1 \leq k \leq K} \) , satisfies

\[
P\left( {B}_{K}\right)  = \mathop{\prod }\limits_{{k = 1}}^{K}P\left( \overline{{A}_{{p}_{k}}}\right)  = \mathop{\prod }\limits_{{k = 1}}^{K}\left( {1 - P\left( {A}_{{p}_{k}}\right) }\right)  = \mathop{\prod }\limits_{{k = 1}}^{K}\left( {1 - \frac{1}{{p}_{k}^{s}}}\right) .
\]

(*)

> Or \( \{ 1\} \subset {B}_{K} \subset \{ 1\} \cup \left\{ {n \in {\mathbb{N}}^{ * }, n > {p}_{K}}\right\} \) donc

However \( \{ 1\} \subset {B}_{K} \subset \{ 1\} \cup \left\{ {n \in {\mathbb{N}}^{ * }, n > {p}_{K}}\right\} \) so

\[
P\left( {\{ 1\} }\right)  \leq  P\left( {B}_{K}\right)  \leq  P\left( {\{ 1\} }\right)  + \mathop{\sum }\limits_{{n > {p}_{K}}}P\left( {\{ n\} }\right)
\]

donc

> therefore

\[
\frac{1}{\zeta \left( s\right) } \leq  P\left( {B}_{K}\right)  \leq  \frac{1}{\zeta \left( s\right) } + \mathop{\sum }\limits_{{n > {p}_{K}}}\frac{1}{\zeta \left( s\right) }\frac{1}{{n}^{s}} \leq  \frac{1}{\zeta \left( s\right) }\left( {1 + {\int }_{{p}_{K}}^{+\infty }\frac{dt}{{t}^{s}}}\right) .
\]

Il y a une infinité de nombres premiers donc \( {p}_{K} \) tend vers \( + \infty \) et comme l’intégrale \( {\int }_{1}^{+\infty }{dt}/{t}^{s} \) converge, on en déduit \( \mathop{\lim }\limits_{{K \rightarrow + \infty }}P\left( {B}_{K}\right) = 1/\zeta \left( s\right) \) , d’où le résultat en faisant tendre \( K \) vers \( + \infty \) dans (*).

> There are infinitely many prime numbers so \( {p}_{K} \) tends to \( + \infty \) and since the integral \( {\int }_{1}^{+\infty }{dt}/{t}^{s} \) converges, we deduce \( \mathop{\lim }\limits_{{K \rightarrow + \infty }}P\left( {B}_{K}\right) = 1/\zeta \left( s\right) \) , hence the result by letting \( K \) tend to \( + \infty \) in (*).

c) Nous allons montrer que la série diverge. Raisonnons par l'absurde et supposons qu'elle converge. Alors comme \( \left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \sim 1/{p}_{k} \) , la série \( \mathop{\sum }\limits_{{k > 1}}\left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \) converge. Soit \( M \) sa somme. Lorsque \( s > 1 \) , on a \( \left| {\log \left( {1 - 1/{p}_{k}^{s}}\right) }\right| \leq \left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \) et avec le résultat de la question précédente, on en déduit

> c) We will show that the series diverges. Let us reason by contradiction and assume that it converges. Then since \( \left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \sim 1/{p}_{k} \) , the series \( \mathop{\sum }\limits_{{k > 1}}\left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \) converges. Let \( M \) be its sum. When \( s > 1 \) , we have \( \left| {\log \left( {1 - 1/{p}_{k}^{s}}\right) }\right| \leq \left| {\log \left( {1 - 1/{p}_{k}}\right) }\right| \) and with the result of the previous question, we deduce

\[
\forall s > 1,\;\left| {\log \zeta \left( s\right) }\right|  = \left| {\mathop{\sum }\limits_{{k = 1}}^{{+\infty }}\log \left( {1 - \frac{1}{{p}_{k}^{s}}}\right) }\right|  \leq  M.
\]

(**)

> Or on a la minoration

However, we have the lower bound

\[
\forall s > 1,\;\zeta \left( s\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1}{{n}^{s}} \geq  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\int }_{n}^{n + 1}\frac{dt}{{t}^{s}} = {\int }_{1}^{+\infty }\frac{dt}{{t}^{s}} = \frac{1}{s - 1}.
\]

ce qui est incompatible avec (**). La série \( \mathop{\sum }\limits_{{k \geq 1}}1/{p}_{k} \) diverge donc.

> which is incompatible with (**). The series \( \mathop{\sum }\limits_{{k \geq 1}}1/{p}_{k} \) therefore diverges.

2/a) Supposons qu'une telle probabilité existe. Le même raisonnement que dans 1/a), montre que les \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) sont mutuellement indépendants. D’après 1/c), la série \( \mathop{\sum }\limits_{{k \geq 1}}P\left( {A}_{{p}_{k}}\right) \) diverge, on peut donc appliquer le lemme du Borel-Cantelli (assertion (ii)) qui nous assure que presque surement, tout entier est dans une infinité de \( {A}_{{p}_{k}} \) , autrement dit que presque surement, tout entier est divisible par une infinité de nombres premiers, ce qui est absurde. On en déduit qu'une telle probabilité n'existe pas.

> 2/a) Suppose such a probability exists. The same reasoning as in 1/a) shows that the \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) are mutually independent. According to 1/c), the series \( \mathop{\sum }\limits_{{k \geq 1}}P\left( {A}_{{p}_{k}}\right) \) diverges, so we can apply the Borel-Cantelli lemma (assertion (ii)), which ensures that almost surely, every integer is in an infinite number of \( {A}_{{p}_{k}} \), in other words, that almost surely, every integer is divisible by an infinite number of prime numbers, which is absurd. We deduce that such a probability does not exist.

b) On va également raisonner par l'absurde en supposant qu'une telle probabilité existe. Ici l’utilisation du lemme de Borel-Cantelli n’est pas possible car les \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) ne sont pas indépendants. On s'en sort en s'inspirant de la preuve de l'assertion (ii) du lemme de Borel-Cantelli, en commençant par déterminer une minoration de \( P\left( {{ \cup }_{m \leq k \leq n}{A}_{{p}_{k}}}\right) \) . En l’absence d’indépendance des événements en présence, on utilise la formule du crible, qui s'écrit

> b) We will also reason by contradiction by assuming that such a probability exists. Here, the use of the Borel-Cantelli lemma is not possible because the \( {\left( {A}_{p}\right) }_{p \in \mathcal{P}} \) are not independent. We get around this by drawing inspiration from the proof of assertion (ii) of the Borel-Cantelli lemma, starting by determining a lower bound for \( P\left( {{ \cup }_{m \leq k \leq n}{A}_{{p}_{k}}}\right) \). In the absence of independence of the events involved, we use the inclusion-exclusion principle, which is written

\[
P\left( {{ \cup  }_{m \leq  k \leq  n}{A}_{{p}_{k}}}\right)  = \mathop{\sum }\limits_{{J \subset  \{ m,\ldots , n\} ,\left| J\right|  \geq  1}}{\left( -1\right) }^{\left| J\right|  - 1}P\left( {{ \cap  }_{j \in  J}{A}_{{p}_{j}}}\right) .
\]

Or \( { \cap }_{j \in J}{A}_{{p}_{j}} = {A}_{q} \) avec \( q = \mathop{\prod }\limits_{{j \in J}}{p}_{j} \) donc

> However, \( { \cap }_{j \in J}{A}_{{p}_{j}} = {A}_{q} \) with \( q = \mathop{\prod }\limits_{{j \in J}}{p}_{j} \), therefore

\[
\left| {P\left( {{ \cap  }_{j \in  J}{A}_{{p}_{j}}}\right)  - \frac{1}{\mathop{\prod }\limits_{{j \in  J}}{p}_{j}}}\right|  \leq  u\left( {\mathop{\prod }\limits_{{j \in  J}}{p}_{j}}\right) .
\]

On a donc

> We therefore have

\[
\left| {P\left( {{ \cup  }_{m \leq  k \leq  n}{A}_{{p}_{k}}}\right)  - \mathop{\sum }\limits_{{J \subset  \{ m,\ldots , n\} ,\left| J\right|  \geq  1}}\frac{{\left( -1\right) }^{\left| J\right|  - 1}}{\mathop{\prod }\limits_{{j \in  J}}{p}_{j}}}\right|  \leq  \mathop{\sum }\limits_{{J \subset  \{ m,\ldots , n\} ,\left| J\right|  \geq  1}}u\left( {\mathop{\prod }\limits_{{j \in  J}}{p}_{j}}\right)  \leq  \mathop{\sum }\limits_{{k = {p}_{m}}}^{{+\infty }}u\left( k\right) .\;\left( {* *  * }\right)
\]

\( \left( {* * * }\right) \)

> La dernière majoration est une conséquence du fait que, lorsque \( J \) parcourt les parties non vides de \( \{ m,\ldots , n\} \) , les entiers \( \mathop{\prod }\limits_{{j \in J}}{p}_{j} \) sont tous distincts (d’après l’unicité de la décomposition en facteurs premiers) et supérieurs à \( {p}_{m} \) . On minore maintenant le terme de droite dans la valeur absolue :

The last upper bound is a consequence of the fact that, when \( J \) ranges over the non-empty subsets of \( \{ m,\ldots , n\} \), the integers \( \mathop{\prod }\limits_{{j \in J}}{p}_{j} \) are all distinct (due to the uniqueness of prime factorization) and greater than \( {p}_{m} \). We now provide a lower bound for the term on the right inside the absolute value:

\[
\mathop{\sum }\limits_{{J \subset  \{ m,\ldots , n\} ,\left| J\right|  \geq  1}}\frac{{\left( -1\right) }^{\left| J\right|  - 1}}{\mathop{\prod }\limits_{{j \in  J}}{p}_{j}} = 1 - \mathop{\prod }\limits_{{k = m}}^{n}\left( {1 - \frac{1}{{p}_{k}}}\right)  \geq  1 - \mathop{\prod }\limits_{{k = m}}^{n}\exp \left( {-1/{p}_{k}}\right)  = 1 - \exp \left( {-\mathop{\sum }\limits_{{k = m}}^{n}\frac{1}{{p}_{k}}}\right) .
\]

Avec \( \left( {* * * }\right) \) on en déduit

> With \( \left( {* * * }\right) \), we deduce

\[
P\left( {{ \cup  }_{m \leq  k \leq  n}{A}_{{p}_{k}}}\right)  \geq  1 - \exp \left( {-\mathop{\sum }\limits_{{k = m}}^{n}\frac{1}{{p}_{k}}}\right)  - \mathop{\sum }\limits_{{k = {p}_{m}}}^{{+\infty }}u\left( k\right) .
\]

En faisant tendre \( n \) vers \( + \infty \) , on obtient, compte tenu du fait que \( \sum 1/{p}_{k} \) diverge

> By letting \( n \) tend to \( + \infty \), we obtain, given the fact that \( \sum 1/{p}_{k} \) diverges

\[
P\left( {{ \cup  }_{k \geq  m}{A}_{{p}_{k}}}\right)  \geq  1 - \mathop{\sum }\limits_{{k = {p}_{m}}}^{{+\infty }}u\left( k\right) .
\]

Comme \( \mathop{\sum }\limits_{k}u\left( k\right) \) converge, ceci entraîne

> Since \( \mathop{\sum }\limits_{k}u\left( k\right) \) converges, this implies

\[
P\left( {{ \cap  }_{m \in  {\mathbb{N}}^{ * }}{ \cup  }_{k \geq  m}{A}_{{p}_{k}}}\right)  \geq  1,
\]

donc \( { \cap }_{m \in {\mathbb{N}}^{ * }}{ \cup }_{k \geq m}{A}_{{p}_{k}} \) est presque sûr. Comme précédemment, on en déduit que presque surement, tout entier est dans une infinité de \( {A}_{{p}_{k}} \) , donc divisible par une infinité de \( {p}_{k} \) , ce qui est absurde.

> therefore \( { \cap }_{m \in {\mathbb{N}}^{ * }}{ \cup }_{k \geq m}{A}_{{p}_{k}} \) is almost certain. As before, we deduce that almost surely, every integer is in an infinite number of \( {A}_{{p}_{k}} \), and therefore divisible by an infinite number of \( {p}_{k} \), which is absurd.

Remarque. Nous avons ainsi démontré par des moyens probabilistes l’expression de \( \zeta \left( s\right) \) comme produit eulérien (question 1/b)). Cette formidable identité est également dé- montrée par des moyens analytiques dans le tome Analyse, c'est notamment l'un des résultats utilisés pour la preuve du théorème des nombres premiers (qui affirme que \( \pi \left( x\right) = \left| {\{ p \in \mathcal{P}, p \leq x\} }\right| \sim x/\log x). \)

> Remark. We have thus demonstrated the expression of \( \zeta \left( s\right) \) as an Euler product using probabilistic means (question 1/b)). This formidable identity is also demonstrated using analytical means in the Analysis volume; it is notably one of the results used for the proof of the prime number theorem (which states that \( \pi \left( x\right) = \left| {\{ p \in \mathcal{P}, p \leq x\} }\right| \sim x/\log x). \)

- On peut montrer que \( \mathop{\sum }\limits_{{p \in  \mathcal{P}, p \leq  n}}1/p = \log \log n + O\left( 1\right) \) . La divergence de la série est donc très lente.

> - One can show that \( \mathop{\sum }\limits_{{p \in  \mathcal{P}, p \leq  n}}1/p = \log \log n + O\left( 1\right) \). The divergence of the series is therefore very slow.
