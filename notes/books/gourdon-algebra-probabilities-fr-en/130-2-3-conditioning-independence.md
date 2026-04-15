#### 2.3. Conditioning, independence

*Français : 2.3. Conditionnement, indépendance*

Conditionnement. La notion de conditionnement est particulièrement fructueuse en probabilité. A partir de la probabilité d'un événement connaissant des informations supplémentaires, elle permet d'en déduire la probabilité de l'événement.

> Conditioning. The notion of conditioning is particularly fruitful in probability. Based on the probability of an event given additional information, it allows one to deduce the probability of the event.

Définition 5 (Probabilité condition (which and the data) Soit A un événement d'un espace pro-babilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) , avec \( P\left( A\right) > 0 \) . Soit \( B \in \mathcal{A} \) un événement. La probabilité conditionnelle de \( B \) sachant \( A \) est définie par

> Definition 5 (Conditional probability). Let A be an event in a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \), with \( P\left( A\right) > 0 \). Let \( B \in \mathcal{A} \) be an event. The conditional probability of \( B \) given \( A \) is defined by

\[
P\left( {B \mid  A}\right)  = \frac{P\left( {A \cap  B}\right) }{P\left( A\right) }.
\]

L’application \( {P}_{A} : \mathcal{A} \rightarrow \left\lbrack {0,1}\right\rbrack \;B \mapsto P\left( {A \cap B}\right) /P\left( A\right) \) définit une nouvelle probabilité sur \( \Omega \) , appelée probabilité conditionnelle sachant \( A \) .

> The mapping \( {P}_{A} : \mathcal{A} \rightarrow \left\lbrack {0,1}\right\rbrack \;B \mapsto P\left( {A \cap B}\right) /P\left( A\right) \) defines a new probability on \( \Omega \), called the conditional probability given \( A \).

Proposition 4. Soient \( {A}_{1},\ldots ,{A}_{n} \) un nombre fini d’événements d’un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) tel que \( P\left( {{A}_{1} \cap \ldots \cap {A}_{n - 1}}\right) > 0 \) . Alors

> Proposition 4. Let \( {A}_{1},\ldots ,{A}_{n} \) be a finite number of events in a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) such that \( P\left( {{A}_{1} \cap \ldots \cap {A}_{n - 1}}\right) > 0 \). Then

\[
P\left( {{A}_{1} \cap  \ldots  \cap  {A}_{n}}\right)  = P\left( {A}_{1}\right) P\left( {{A}_{2} \mid  {A}_{1}}\right) P\left( {{A}_{3} \mid  {A}_{1} \cap  {A}_{2}}\right) \cdots P\left( {{A}_{n} \mid  {A}_{1} \cap  \ldots  \cap  {A}_{n - 1}}\right) .
\]

PROPOSITION 5 (FORMULE DES PROBABILITÉS TOTALES). Soit un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) et \( {\left( {A}_{i}\right) }_{i \in I} \) une famille finie ou dénombrable d’événements, qui forment une partition de \( \Omega \) , et telle que \( P\left( {A}_{i}\right) > 0 \) pour tout \( i \in I \) . Alors pour tout \( B \in \mathcal{A} \)

> PROPOSITION 5 (LAW OF TOTAL PROBABILITY). Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space and \( {\left( {A}_{i}\right) }_{i \in I} \) be a finite or countable family of events that form a partition of \( \Omega \), and such that \( P\left( {A}_{i}\right) > 0 \) for all \( i \in I \). Then for any \( B \in \mathcal{A} \)

\[
P\left( B\right)  = \mathop{\sum }\limits_{{i \in  I}}P\left( {B \mid  {A}_{i}}\right) P\left( {A}_{i}\right) .
\]

PROPOSITION 6 (FORMULE DE BAYES). Sous les hypothèses de la propriété précédente, on a, si \( P\left( B\right) > 0 \)

> PROPOSITION 6 (BAYES' THEOREM). Under the hypotheses of the previous property, we have, if \( P\left( B\right) > 0 \)

\[
\forall i \in  I,\;P\left( {{A}_{i} \mid  B}\right)  = \frac{P\left( {B \mid  {A}_{i}}\right) P\left( {A}_{i}\right) }{\mathop{\sum }\limits_{{i \in  I}}P\left( {B \mid  {A}_{i}}\right) P\left( {A}_{i}\right) }.
\]

Démonstration. On a \( P\left( {{A}_{i} \cap B}\right) = P\left( {{A}_{i} \mid B}\right) P\left( B\right) = P\left( {B \mid {A}_{i}}\right) P\left( {A}_{i}\right) \) , donc

> Proof. We have \( P\left( {{A}_{i} \cap B}\right) = P\left( {{A}_{i} \mid B}\right) P\left( B\right) = P\left( {B \mid {A}_{i}}\right) P\left( {A}_{i}\right) \), therefore

\[
P\left( {{A}_{i} \mid  B}\right)  = \frac{P\left( {B \mid  {A}_{i}}\right) P\left( {A}_{i}\right) }{P\left( B\right) }
\]

et on conclut avec la formule des probabilités totales.

> and we conclude with the law of total probability.

Remarque 6. - Il n'est pas nécéssaire de retenir par cœur la formule de Bayes, on la redémontre facilement.

> Remark 6. - It is not necessary to memorize Bayes' theorem; it can be easily re-derived.

- Un cas particulier souvent rencontré est celui où on considère la partition \( A,{A}^{C} \) de \( \Omega \) . Dans ce cas on a \( P\left( B\right)  = P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) \) , et la formule de Bayes devient

> - A frequently encountered special case is when we consider the partition \( A,{A}^{C} \) of \( \Omega \). In this case, we have \( P\left( B\right)  = P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) \), and Bayes' theorem becomes

\[
P\left( {A \mid  B}\right)  = \frac{P\left( {B \mid  A}\right) P\left( A\right) }{P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) }.
\]

Exemple 3. Un test de détection d'une maladie rare est positif à 99% lorsqu'un individu est atteint de cette maladie, et il est positif à 0,1% lorsqu'il n'est pas atteint. Supposons que 0,01% de la population soit atteint de cette maladie. On considère un individu pris au hasard dans la population. Sachant qu'il est positif au test de detection, calculons la probabilité qu'il soit atteint par la maladie. On considère l'événement \( A \) des individus atteints de la maladie, et \( {A}^{C} \) ceux qui ne le sont pas. Soit B l’événement "le test est positif". Il s’agit de calculer \( P\left( {A \mid B}\right) \) . La formule de Bayes donne

> Example 3. A detection test for a rare disease is positive 99% of the time when an individual has the disease, and it is positive 0.1% of the time when they do not. Suppose that 0.01% of the population has this disease. We consider an individual chosen at random from the population. Given that they test positive, let us calculate the probability that they have the disease. Let \( A \) be the event that individuals have the disease, and \( {A}^{C} \) those who do not. Let B be the event "the test is positive". We need to calculate \( P\left( {A \mid B}\right) \). Bayes' theorem gives

\[
P\left( {A \mid  B}\right)  = \frac{P\left( {B \mid  A}\right) P\left( A\right) }{P\left( {B \mid  A}\right) P\left( A\right)  + P\left( {B \mid  {A}^{C}}\right) P\left( {A}^{C}\right) } = \frac{0,{99} \times  0,{0001}}{0,{99} \times  0,{0001} + 0,{001} \times  {0.9999}},
\]

et un calcul donne \( P\left( {A \mid B}\right) \simeq 0,{09} \) . La probabilité est petite, ce qui peut sembler contraire à l'intuition.

> and a calculation gives \( P\left( {A \mid B}\right) \simeq 0,{09} \) . The probability is small, which may seem counterintuitive.

Indépendance. Étant donnés deux événéments \( A \) et \( B \) avec \( P\left( A\right) > 0 \) , si le fait de savoir \( A \) ne donne aucune information sur \( B \) , on a \( P\left( {B \mid A}\right) = P\left( B\right) \) , donc \( P\left( {A \cap B}\right) /P\left( A\right) = \; P\left( B\right) \) ce qui entraîne \( P\left( {A \cap B}\right) = P\left( A\right) P\left( B\right) \) . Ceci introduit la notion d’événements indépendants, dont la définition ci-dessous reste valide lorque \( P\left( A\right) = 0 \) .

> Independence. Given two events \( A \) and \( B \) with \( P\left( A\right) > 0 \) , if knowing \( A \) provides no information about \( B \) , we have \( P\left( {B \mid A}\right) = P\left( B\right) \) , thus \( P\left( {A \cap B}\right) /P\left( A\right) = \; P\left( B\right) \) which leads to \( P\left( {A \cap B}\right) = P\left( A\right) P\left( B\right) \) . This introduces the notion of independent events, the definition of which below remains valid when \( P\left( A\right) = 0 \) .

DéFINITION 6. Deux événements \( A \) et \( B \) d’un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) sont dit indé- pendants si

> DEFINITION 6. Two events \( A \) and \( B \) of a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) are said to be independent if

\[
P\left( {A \cap  B}\right)  = P\left( A\right) P\left( B\right) .
\]

Remarque 7. - Lorsque \( P\left( A\right) > 0 \) , les événements \( A \) et \( B \) sont indépendants si et seulement si \( P\left( {B \mid A}\right) = P\left( B\right) \) .

> Remark 7. - When \( P\left( A\right) > 0 \) , the events \( A \) and \( B \) are independent if and only if \( P\left( {B \mid A}\right) = P\left( B\right) \) .

- Un événement presque sûr est indépendant de tout autre.

> - An almost sure event is independent of any other.

- Un événement négligeable est indépendant de tout autre.

> - A negligible event is independent of any other.

Proposition 7. Soir A et B deux événements indépendants d'un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Alors il en est de même de \( {A}^{C} \) et \( B \) , de \( A \) et \( {B}^{C} \) , de \( {A}^{C} \) et \( {B}^{C} \) .

> Proposition 7. Let A and B be two independent events of a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Then the same is true for \( {A}^{C} \) and \( B \) , for \( A \) and \( {B}^{C} \) , and for \( {A}^{C} \) and \( {B}^{C} \) .

On étend la définition de l'indépendance à une famille quelconque d'événements.

> We extend the definition of independence to any family of events.

DéFINITION 7. Soit \( {\left( {A}_{i}\right) }_{i \in I} \) une famille (éventuellement infinie) d’événements d’un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) . On dit que les \( {\left( {A}_{i}\right) }_{i \in I} \) sont mutuellement indépendants si pour toute partie finie \( J \subset I \) , on a

> DEFINITION 7. Let \( {\left( {A}_{i}\right) }_{i \in I} \) be a family (possibly infinite) of events of a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) . We say that the \( {\left( {A}_{i}\right) }_{i \in I} \) are mutually independent if for any finite subset \( J \subset I \) , we have

\[
P\left( {{ \cap  }_{j \in  J}{A}_{j}}\right)  = \mathop{\prod }\limits_{{j \in  J}}P\left( {A}_{j}\right) .
\]

Remarque 8. On se contente parfois de dire que les \( {\left( {A}_{i}\right) }_{i \in I} \) sont indépendants. Si les \( {\left( {A}_{i}\right) }_{i \in I} \) sont indépendants alors ils sont indépendants deux à deux mais la réciproque est fausse. Par exemple, on tire deux fois à pile ou face et on considère les événements A = "pile au premier lancer", \( B = \) "pile au deuxième lancer", \( C = \) "même résultat aux deux lancers". Ils sont indépendants deux à deux mais pas mutuellement indépendants.

> Remark 8. We sometimes simply say that the \( {\left( {A}_{i}\right) }_{i \in I} \) are independent. If the \( {\left( {A}_{i}\right) }_{i \in I} \) are independent, then they are pairwise independent, but the converse is false. For example, we flip a coin twice and consider the events A = "heads on the first flip", \( B = \) "heads on the second flip", \( C = \) "same result on both flips". They are pairwise independent but not mutually independent.

Proposition 8. Soit \( {\left( {A}_{i}\right) }_{i \in I} \) une famille d’événements indépendants d’un espace proba-bilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Pour toute famille \( {\left( {\varepsilon }_{i}\right) }_{i \in I}d \) ’éléments de \( \{ - 1,1\} ,{\left( {A}_{i}^{{\varepsilon }_{i}}\right) }_{i \in I} \) est une famille d’événements indépendants (où pour tout événement \( B \) on a noté \( {B}^{1} = B \) et \( {B}^{-1} = {B}^{C} \) ).

> Proposition 8. Let \( {\left( {A}_{i}\right) }_{i \in I} \) be a family of independent events in a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \). For any family \( {\left( {\varepsilon }_{i}\right) }_{i \in I}d \) of elements of \( \{ - 1,1\} ,{\left( {A}_{i}^{{\varepsilon }_{i}}\right) }_{i \in I} \) is a family of independent events (where for any event \( B \) we have denoted \( {B}^{1} = B \) and \( {B}^{-1} = {B}^{C} \)).

Espaces de probabilité produit. Nous étudions ici comment construire un espace pro-babilisé rendant compte de plusieurs expériences indépendantes les unes des autres.

> Product probability spaces. We study here how to construct a probability space accounting for several experiments independent of one another.

CAS FINI. Considérons \( n \geq 2 \) espaces probabilisés \( \left( {{\Omega }_{k},{\mathcal{A}}_{k},{P}_{k}}\right) \) avec \( 1 \leq k \leq n \) et \( \Omega = \; {\Omega }_{1} \times \ldots \times {\Omega }_{n} \) . On muni \( \Omega \) de la tribu \( \mathcal{A} \) engendrée par les pavés \( {A}_{1} \times \ldots \times {A}_{n} \) avec \( {A}_{k} \in {\mathcal{A}}_{k} \) . Un résultat de la théorie des probabilités que nous admettrons, affirme qu'il existe une unique probabilité \( P \) (appelée probabilité produit) sur l’espace probabilisable \( \left( {\Omega ,\mathcal{A}}\right) \) tel que sur les pavés de \( \mathcal{A} \) on ait \( P\left( {{A}_{1} \times \ldots \times {A}_{n}}\right) = {P}_{1}\left( {A}_{1}\right) \cdots {P}_{n}\left( {A}_{n}\right) \) . La probabilité

> FINITE CASE. Consider \( n \geq 2 \) probability spaces \( \left( {{\Omega }_{k},{\mathcal{A}}_{k},{P}_{k}}\right) \) with \( 1 \leq k \leq n \) and \( \Omega = \; {\Omega }_{1} \times \ldots \times {\Omega }_{n} \). We equip \( \Omega \) with the sigma-algebra \( \mathcal{A} \) generated by the rectangles \( {A}_{1} \times \ldots \times {A}_{n} \) with \( {A}_{k} \in {\mathcal{A}}_{k} \). A result from probability theory that we shall assume states that there exists a unique probability \( P \) (called the product probability) on the measurable space \( \left( {\Omega ,\mathcal{A}}\right) \) such that on the rectangles of \( \mathcal{A} \) we have \( P\left( {{A}_{1} \times \ldots \times {A}_{n}}\right) = {P}_{1}\left( {A}_{1}\right) \cdots {P}_{n}\left( {A}_{n}\right) \). The probability

\( P \) rend ainsi indépendantes les expériences aléatoires correspondantes à chaque espace \( \left( {{\Omega }_{k},{\mathcal{A}}_{k},{P}_{k}}\right) \) . Nous énonçons et prouvons ce résultat dans le cas où les \( {\Omega }_{k} \) sont finis ou dénombrables, lorsque \( {\mathcal{A}}_{k} = \mathcal{P}\left( {\Omega }_{k}\right) \) . Dans ce cas, \( \Omega \) est fini ou dénombrable et il suffit de définir \( P \) sur ses singletons d’après la proposition 3.

> \( P \) thus makes the random experiments corresponding to each space \( \left( {{\Omega }_{k},{\mathcal{A}}_{k},{P}_{k}}\right) \) independent. We state and prove this result in the case where the \( {\Omega }_{k} \) are finite or countable, when \( {\mathcal{A}}_{k} = \mathcal{P}\left( {\Omega }_{k}\right) \). In this case, \( \Omega \) is finite or countable and it suffices to define \( P \) on its singletons according to Proposition 3.

PROPOSITION 9. Considérons \( n \) espaces probabilisés \( {\left( {\Omega }_{k},\mathcal{P}\left( {\Omega }_{k}\right) ,{P}_{k}\right) }_{1 \leq k \leq n} \) , chacun étant fini ou dénombrable. Alors \( \Omega = {\Omega }_{1} \times \ldots \times {\Omega }_{n} \) est fini ou dénombrable, et la probabilité \( P \) définie sur les singletons de \( \Omega \) par

> PROPOSITION 9. Consider \( n \) probability spaces \( {\left( {\Omega }_{k},\mathcal{P}\left( {\Omega }_{k}\right) ,{P}_{k}\right) }_{1 \leq k \leq n} \), each being finite or countable. Then \( \Omega = {\Omega }_{1} \times \ldots \times {\Omega }_{n} \) is finite or countable, and the probability \( P \) defined on the singletons of \( \Omega \) by

\[
P\left( \left\{  \left( {{x}_{1},\ldots ,{x}_{n}}\right) \right\}  \right)  = {P}_{1}\left( \left\{  {x}_{1}\right\}  \right) \cdots {P}_{n}\left( \left\{  {x}_{n}\right\}  \right)
\]

(*)

> est l’unique probabilité sur \( \left( {\Omega ,\mathcal{P}\left( \Omega \right) }\right) \) telle que pour tout \( {A}_{1} \in \mathcal{P}\left( {\Omega }_{1}\right) ,\ldots ,{A}_{n} \in \mathcal{P}\left( {\Omega }_{n}\right) \) ,

is the unique probability on \( \left( {\Omega ,\mathcal{P}\left( \Omega \right) }\right) \) such that for all \( {A}_{1} \in \mathcal{P}\left( {\Omega }_{1}\right) ,\ldots ,{A}_{n} \in \mathcal{P}\left( {\Omega }_{n}\right) \),

\[
P\left( {{A}_{1} \times  \ldots  \times  {A}_{n}}\right)  = {P}_{1}\left( {A}_{1}\right)  \times  \cdots  \times  {P}_{n}\left( {A}_{n}\right) .
\]

(**)

> Démonstration. Le fait que \( \Omega \) est fini ou dénombrable est un résultat classique sur les ensembles au plus dénombrables.

Proof. The fact that \( \Omega \) is finite or countable is a classic result on at most countable sets.

> - Montrons d’abord que \( P \) défini par (*) est bien une probabilité sur \( \Omega \) . Par commodité notons \( {p}_{k}\left( {x}_{k}\right)  = {P}_{k}\left( \left\{  {x}_{k}\right\}  \right) \) . Lorsque \( {A}_{1},\ldots ,{A}_{n} \) sont des parties finies de \( {\Omega }_{1},\ldots ,{\Omega }_{n} \) on a

- Let us first show that \( P \) defined by (*) is indeed a probability on \( \Omega \) . For convenience, let us denote \( {p}_{k}\left( {x}_{k}\right)  = {P}_{k}\left( \left\{  {x}_{k}\right\}  \right) \) . When \( {A}_{1},\ldots ,{A}_{n} \) are finite subsets of \( {\Omega }_{1},\ldots ,{\Omega }_{n} \) , we have

\[
\mathop{\sum }\limits_{{{x}_{1} \in  {A}_{1},\ldots ,{x}_{n} \in  {A}_{n}}}{p}_{1}\left( {x}_{1}\right) \cdots {p}_{n}\left( {x}_{n}\right)  = \left( {\mathop{\sum }\limits_{{{x}_{1} \in  {A}_{1}}}{p}_{1}\left( {x}_{1}\right) }\right) \cdots \left( {\mathop{\sum }\limits_{{{x}_{n} \in  {A}_{n}}}{p}_{n}\left( {x}_{n}\right) }\right)  = {P}_{1}\left( {A}_{1}\right) \cdots {P}_{n}\left( {A}_{n}\right)
\]

(***)

> donc la première somme est majorée par 1. Ainsi la famille de réels positifs \( {p}_{1}\left( {x}_{1}\right) \cdots {p}_{n}\left( {x}_{n}\right) \) avec \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in \Omega \) est sommable. On peut donc écrire

therefore the first sum is bounded by 1. Thus, the family of positive real numbers \( {p}_{1}\left( {x}_{1}\right) \cdots {p}_{n}\left( {x}_{n}\right) \) with \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in \Omega \) is summable. We can therefore write

\[
\mathop{\sum }\limits_{{{x}_{1} \in  {\Omega }_{1},\ldots ,{x}_{n} \in  {\Omega }_{n}}}{p}_{1}\left( {x}_{1}\right) \cdots {p}_{n}\left( {x}_{n}\right)  = \left( {\mathop{\sum }\limits_{{{x}_{1} \in  {\Omega }_{1}}}{p}_{1}\left( {x}_{1}\right) }\right) \cdots \left( {\mathop{\sum }\limits_{{{x}_{n} \in  {\Omega }_{n}}}{p}_{n}\left( {x}_{n}\right) }\right)  = 1,
\]

donc les hypothèses de la proposition 3 sont vérifiées, et (*) définit bien une probabilité \( P \) sur \( \Omega \) . Pour prouver la propriété (**) on part de l’égalité

> therefore the hypotheses of proposition 3 are satisfied, and (*) indeed defines a probability \( P \) on \( \Omega \) . To prove property (**), we start from the equality

\[
P\left( {{A}_{1} \times  \cdots  \times  {A}_{n}}\right)  = \mathop{\sum }\limits_{{{x}_{1} \in  {A}_{1},\ldots ,{x}_{n} \in  {A}_{n}}}{p}_{1}\left( {x}_{1}\right) \cdots {p}_{n}\left( {x}_{n}\right)
\]

puis on remarque que l'égalité (***) reste vraie même lorsque les \( {A}_{k} \) ne sont pas forcément finis, étant en présence d'une famille sommable.

> then we note that equality (***) remains true even when the \( {A}_{k} \) are not necessarily finite, as we are dealing with a summable family.

- L'unicité de \( P \) vérifiant (**) est une conséquence de la même égalité (**) lorsqu’on l’applique à tous les singletons \( \left\{  {x}_{1}\right\}   \times  \ldots  \times  \left\{  {x}_{n}\right\}   = \left\{  \left( {{x}_{1},\ldots ,{x}_{n}}\right) \right\} \) .

> - The uniqueness of \( P \) satisfying (**) is a consequence of the same equality (**) when applied to all singletons \( \left\{  {x}_{1}\right\}   \times  \ldots  \times  \left\{  {x}_{n}\right\}   = \left\{  \left( {{x}_{1},\ldots ,{x}_{n}}\right) \right\} \) .

Remarque 9. Un cas particulier courant est celui de \( n \) expériences aléatoires indépendantes modélisées par le même espace \( \left( {E,\mathcal{T}, P}\right) \) . Dans ce cas \( \Omega = {E}^{n} \) , muni de la probabilité produit \( {P}^{ * } \) , et comme on s’y attend, la probabilité que la \( k \) -ième expérience ait ses résultats dans l’événement \( {A}_{k} \in \mathcal{A} \) , est égal à \( {P}^{ * }\left( {{E}^{k - 1} \times {A}_{k} \times {E}^{n - k}}\right) = P\left( {A}_{k}\right) \) . Lorsque \( E = \{ 0,1\} \) avec \( P\left( {\{ 1\} }\right) = p \in \rbrack 0,1\lbrack \) , la probabilité du singleton \( \left\{ \left( {{w}_{1},\ldots ,{w}_{n}}\right) \right\} \) avec \( {w}_{j} \in \{ 0,1\} \) est \( {p}^{k}{\left( 1 - p\right) }^{n - k} \) , où \( k \) est le nombre de \( {w}_{j} \) égaux à 1 .

> Remark 9. A common special case is that of \( n \) independent random experiments modeled by the same space \( \left( {E,\mathcal{T}, P}\right) \) . In this case \( \Omega = {E}^{n} \) , equipped with the product probability \( {P}^{ * } \) , and as expected, the probability that the \( k \) -th experiment has its results in the event \( {A}_{k} \in \mathcal{A} \) is equal to \( {P}^{ * }\left( {{E}^{k - 1} \times {A}_{k} \times {E}^{n - k}}\right) = P\left( {A}_{k}\right) \) . When \( E = \{ 0,1\} \) with \( P\left( {\{ 1\} }\right) = p \in \rbrack 0,1\lbrack \) , the probability of the singleton \( \left\{ \left( {{w}_{1},\ldots ,{w}_{n}}\right) \right\} \) with \( {w}_{j} \in \{ 0,1\} \) is \( {p}^{k}{\left( 1 - p\right) }^{n - k} \) , where \( k \) is the number of \( {w}_{j} \) equal to 1 .

CAS DÉNOMBRABLE. Ici nous nous placons dans le cas où on souhaite probabiliser un espace \( \Omega = {E}^{{\mathbb{N}}^{ * }} \) , modélisant une infinité (dénombrable) de fois la même expérience aléa-toire. Partant d’un espace probabilisé \( \left( {E,\mathcal{T}, P}\right) \) , on définit pour tout \( n \in {\mathbb{N}}^{ * } \) et pour tout \( \left( {{A}_{1},\ldots ,{A}_{n}}\right) \in {\mathcal{T}}^{n} \) le cylindre

> COUNTABLE CASE. Here we consider the case where we wish to assign a probability to a space \( \Omega = {E}^{{\mathbb{N}}^{ * }} \) , modeling an infinite (countable) number of times the same random experiment. Starting from a probability space \( \left( {E,\mathcal{T}, P}\right) \) , we define for all \( n \in {\mathbb{N}}^{ * } \) and for all \( \left( {{A}_{1},\ldots ,{A}_{n}}\right) \in {\mathcal{T}}^{n} \) the cylinder

\[
{A}_{1} \times  \ldots  \times  {A}_{n} \times  E \times  E \times  \ldots  = \left\{  {w = {\left( {w}_{i}\right) }_{i \in  {\mathbb{N}}^{ * }} \in  {E}^{{\mathbb{N}}^{ * }}\mid \forall k \in  \{ 1,\ldots , n\} ,{w}_{k} \in  {A}_{k}}\right\}
\]

et on définit la tribu \( \mathcal{A} \) engendrée par tous les cylindres de cette forme. Ici aussi, nous ad-mettrons un résultat dû à Kolmogorov, qui affirme l'existence et l'unicité d'une probabilité \( {P}^{ * } \) sur \( \left( {\Omega ,\mathcal{A}}\right) \) tel que pour tout cylindre, on ait

> and we define the sigma-algebra \( \mathcal{A} \) generated by all cylinders of this form. Here too, we will accept a result due to Kolmogorov, which asserts the existence and uniqueness of a probability \( {P}^{ * } \) on \( \left( {\Omega ,\mathcal{A}}\right) \) such that for every cylinder, we have

\[
{P}^{ * }\left( {{A}_{1} \times  \ldots  \times  {A}_{n} \times  E \times  E \times  \ldots }\right)  = P\left( {A}_{1}\right) \cdots P\left( {A}_{n}\right) .
\]

C'est l'existence et l'unicité de cette probabilité qui permet par exemple de considérer des probabilités sur des suites infinies de tirage à pile ou face (voir par exemple l'exemple ci-dessous, ou les exercices 5 et 6 pages 330 et 331), et c'est indispensable pour avoir le droit de définir une probabilité sur ces espaces. Dans la même veine, la proposition 17 page 344, assure l'existence d'une suite de variables aléatoires indépendantes qui suivent une suite de lois donnée.

> It is the existence and uniqueness of this probability that allows, for example, the consideration of probabilities on infinite sequences of coin tosses (see for example the example below, or exercises 5 and 6 on pages 330 and 331), and it is essential to be allowed to define a probability on these spaces. In the same vein, proposition 17 on page 344 ensures the existence of a sequence of independent random variables that follow a given sequence of distributions.

Exemple 4. On lance successivement et de manière indépendante une pièce, dont la pro-babilité de tomber sur pile est \( p \in \rbrack 0,1\lbrack \) . On calcule la probabilité pour que pile appa-raisse pour la première fois au \( n \) -ième lancer. Ici la probabilité \( P \) est celle sur les suites \( {\left( {w}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \in \Omega = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \) , dont l’existence et l’unicité est garantie par le résultat que nous avons présenté plus haut. Notons \( {A}_{n} \) l’événement "Pile apparait pour la première fois au lancer numéro \( n \) ", qui correspond au cylindre \( \{ \mathrm{F}\} \times \ldots \times \{ \mathrm{F}\} \times \{ \mathrm{P}\} \times E \times \ldots \) , où il y a \( n - 1 \) fois \( \{ \mathrm{F}\} \) . La probabilité \( P \) de \( {A}_{n} \) est donc \( P\left( {A}_{n}\right) = {\left( 1 - p\right) }^{n - 1}p \) . Les événements \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) forment une partition de \( \Omega \smallsetminus \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \) , od \( {\mathrm{P}}_{{\mathbb{N}}^{ * }} \) désigne la suite dont tous les éléments sont des "piles". On en déduit

> Example 4. We toss a coin successively and independently, where the probability of landing on heads is \( p \in \rbrack 0,1\lbrack \). We calculate the probability that heads appears for the first time on the \( n \)-th toss. Here the probability \( P \) is that on the sequences \( {\left( {w}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \in \Omega = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \), whose existence and uniqueness is guaranteed by the result we presented above. Let \( {A}_{n} \) be the event "Heads appears for the first time on toss number \( n \)", which corresponds to the cylinder \( \{ \mathrm{F}\} \times \ldots \times \{ \mathrm{F}\} \times \{ \mathrm{P}\} \times E \times \ldots \), where there are \( n - 1 \) instances of \( \{ \mathrm{F}\} \). The probability \( P \) of \( {A}_{n} \) is therefore \( P\left( {A}_{n}\right) = {\left( 1 - p\right) }^{n - 1}p \). The events \( {\left( {A}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) form a partition of \( \Omega \smallsetminus \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \), where \( {\mathrm{P}}_{{\mathbb{N}}^{ * }} \) denotes the sequence where all elements are "heads". We deduce from this

\[
P\left( {\Omega  \smallsetminus  \left\{  {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\}  }\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}P\left( {A}_{n}\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{\left( 1 - p\right) }^{n - 1}p = 1.
\]

Donc \( P\left( \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \right) = 0 \) , c’est-à-dire que le singleton \( \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \) est un événement négligeable, comme déjà discuté dans la remarque 5 page 322.

> Therefore \( P\left( \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \right) = 0 \), meaning that the singleton \( \left\{ {\mathrm{P}}_{{\mathbb{N}}^{ * }}\right\} \) is a negligible event, as already discussed in remark 5 on page 322.

Lemme de Borel-Cantelli. Considérons une suite \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) d’événements. On définit

> Borel-Cantelli Lemma. Consider a sequence \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) of events. We define

\[
\mathop{\limsup }\limits_{n}{A}_{n} = { \cap  }_{p \in  \mathbb{N}}\left( {{ \cup  }_{n \geq  p}{A}_{n}}\right)
\]

Il n'est pas difficile de voir que

> It is not difficult to see that

\[
w \in  \mathop{\limsup }\limits_{n}{A}_{n} \Leftrightarrow  w\text{ appartient à une infinité de }{A}_{n}.
\]

Notons également que

> Note also that

\( w \notin \mathop{\limsup }\limits_{n}{A}_{n} \Leftrightarrow w \) appartient à au plus un nombre fini de \( {A}_{n}. \)

> \( w \notin \mathop{\limsup }\limits_{n}{A}_{n} \Leftrightarrow w \) belongs to at most a finite number of \( {A}_{n}. \)

Mentionnons également la notation \( \mathop{\liminf }\limits_{n}{A}_{n} = { \cup }_{p \in \mathbb{N}}\left( {{ \cap }_{n \geq p}{A}_{n}}\right) \) , qui désigne l’ensemble des \( w \in \Omega \) qui appartiennent à tous les \( {A}_{n} \) sauf éventuellement un nombre fini.

> Let us also mention the notation \( \mathop{\liminf }\limits_{n}{A}_{n} = { \cup }_{p \in \mathbb{N}}\left( {{ \cap }_{n \geq p}{A}_{n}}\right) \), which denotes the set of \( w \in \Omega \) that belong to all \( {A}_{n} \) except possibly a finite number.

Muni de cette définition, nous pouvons maintenant énoncer le lemme de Borel-Cantelli, qui n'est pas au programme des classes préparatoires mais qu'il est très utile de connaitre et de savoir démontrer (la preuve est assez simple). Il est presque systématiquement utilisé chaque fois qu'on veut prouver qu'une propriété est vraie presque partout.

> With this definition, we can now state the Borel-Cantelli lemma, which is not in the preparatory classes curriculum but is very useful to know and be able to prove (the proof is quite simple). It is almost systematically used whenever one wants to prove that a property is true almost everywhere.

\( \rightarrow \) THÉORÉME 1 (LEMME DE BOREL-CANTELLI). Soit \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) une suite d’événements d’un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Alors

> \( \rightarrow \) THEOREM 1 (BOREL-CANTELLI LEMMA). Let \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of events in a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \) . Then

(i) Si \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) converge, on a \( P\left( {\lim \mathop{\sup }\limits_{n}{A}_{n}}\right) = 0 \) .

> (i) If \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) converges, we have \( P\left( {\lim \mathop{\sup }\limits_{n}{A}_{n}}\right) = 0 \) .

(ii) Si les \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) sont mutuellements indépendants, et si \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) diverge, alors \( P\left( {\lim \mathop{\sup }\limits_{n}{A}_{n}}\right) = 1. \)

> (ii) If the \( {\left( {A}_{n}\right) }_{n \in \mathbb{N}} \) are mutually independent, and if \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) diverges, then \( P\left( {\lim \mathop{\sup }\limits_{n}{A}_{n}}\right) = 1. \)

Démonstration. (i) Notons \( {B}_{p} = { \cup }_{n \geq p}{A}_{n} \) . On a \( P\left( {B}_{p}\right) \leq \mathop{\sum }\limits_{{n \geq p}}P\left( {A}_{n}\right) \) donc \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}P\left( {B}_{p}\right) = 0 \) . Comme \( {\left( {B}_{p}\right) }_{p \in \mathbb{N}} \) est une suite décroissante (au sens de l’inclusion), on en déduit d’après (vi) de la proposition 2 page 320, que \( P\left( {\mathop{\limsup }\limits_{n}{A}_{n}}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}P\left( {B}_{p}\right) = 0 \) .

> Proof. (i) Let \( {B}_{p} = { \cup }_{n \geq p}{A}_{n} \) . We have \( P\left( {B}_{p}\right) \leq \mathop{\sum }\limits_{{n \geq p}}P\left( {A}_{n}\right) \) so \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}P\left( {B}_{p}\right) = 0 \) . Since \( {\left( {B}_{p}\right) }_{p \in \mathbb{N}} \) is a decreasing sequence (in the sense of inclusion), we deduce from (vi) of proposition 2 on page 320 that \( P\left( {\mathop{\limsup }\limits_{n}{A}_{n}}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}P\left( {B}_{p}\right) = 0 \) .

(ii) Soit \( p \in \mathbb{N} \) . Les \( \left( {A}_{n}\right) \) sont indépendants, donc les \( \left( {A}_{n}^{C}\right) \) également, donc pour tout \( m > p \) ,

> (ii) Let \( p \in \mathbb{N} \) . The \( \left( {A}_{n}\right) \) are independent, so the \( \left( {A}_{n}^{C}\right) \) are as well, therefore for all \( m > p \) ,

\[
P\left( {\mathop{\bigcup }\limits_{{i = p}}^{m}{A}_{i}}\right)  = 1 - P\left( {\mathop{\bigcap }\limits_{{i = p}}^{m}{A}_{i}^{C}}\right)  = 1 - \mathop{\prod }\limits_{{i = p}}^{m}P\left( {A}_{i}^{C}\right)  = 1 - \mathop{\prod }\limits_{{i = p}}^{m}\left( {1 - P\left( {A}_{i}\right) }\right) .
\]

Lorsque \( x > 0 \) , on a \( 1 - x < \exp \left( {-x}\right) \) , on en déduit \( \mathop{\prod }\limits_{{i = p}}^{m}\left( {1 - P\left( {A}_{i}\right) }\right) \leq \exp \left( {-\mathop{\sum }\limits_{{i = p}}^{m}P\left( {A}_{i}\right) }\right) \) , donc \( \mathop{\lim }\limits_{{m \rightarrow \infty }}\mathop{\prod }\limits_{{i = p}}^{m}\left( {1 - P\left( {A}_{i}\right) }\right) = 0 \) , donc \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}P\left( {{ \cup }_{i = p}^{m}{A}_{i}}\right) = 1 \) . On en déduit \( P\left( {B}_{p}\right) = \; P\left( {{ \cup }_{m \geq p}{A}_{i}}\right) = 1 \) . Donc \( P\left( {\mathop{\limsup }\limits_{n}{A}_{n}}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}P\left( {B}_{p}\right) = 1 \) .

> When \( x > 0 \) , we have \( 1 - x < \exp \left( {-x}\right) \) , from which we deduce \( \mathop{\prod }\limits_{{i = p}}^{m}\left( {1 - P\left( {A}_{i}\right) }\right) \leq \exp \left( {-\mathop{\sum }\limits_{{i = p}}^{m}P\left( {A}_{i}\right) }\right) \) , thus \( \mathop{\lim }\limits_{{m \rightarrow \infty }}\mathop{\prod }\limits_{{i = p}}^{m}\left( {1 - P\left( {A}_{i}\right) }\right) = 0 \) , therefore \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}P\left( {{ \cup }_{i = p}^{m}{A}_{i}}\right) = 1 \) . We deduce \( P\left( {B}_{p}\right) = \; P\left( {{ \cup }_{m \geq p}{A}_{i}}\right) = 1 \) . Thus \( P\left( {\mathop{\limsup }\limits_{n}{A}_{n}}\right) = P\left( {{ \cap }_{p \in \mathbb{N}}{B}_{p}}\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}P\left( {B}_{p}\right) = 1 \) .

Remarque 10. Une autre façon d’exprimer l’assertion (i) est d’affirmer que si \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) converge, alors presque surement, si \( \omega \in \Omega \) , il n’y a qu’un nombre fini de \( n \) pour lequel \( \omega \in {A}_{n} \) .

> Remark 10. Another way to express assertion (i) is to state that if \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}P\left( {A}_{n}\right) \) converges, then almost surely, if \( \omega \in \Omega \) , there are only a finite number of \( n \) for which \( \omega \in {A}_{n} \) .

- Voyons une conséquence typique de ce lemme. On considère l’espace \( \Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \) des suites infinies de tirages à pile ou face d’une pièce équilibrée. Pour tout \( n \in  {\mathbb{N}}^{ * } \) , considérons l’événement "la suite contient \( n \) piles consécutifs à partir de la position \( n \) ", c’est-à-dire

> - Let us look at a typical consequence of this lemma. Consider the space \( \Omega  = \{ \mathrm{P},\mathrm{F}{\} }^{{\mathbb{N}}^{ * }} \) of infinite sequences of coin tosses of a fair coin. For any \( n \in  {\mathbb{N}}^{ * } \) , consider the event "the sequence contains \( n \) consecutive heads starting from position \( n \) ", that is to say

\[
{A}_{n} = \left\{  {w = {\left( {w}_{i}\right) }_{i \in  {\mathbb{N}}^{ * }} \in  \Omega  \mid  {w}_{n} = {w}_{n + 1} = \ldots  = {w}_{{2n} - 1} = \mathrm{P}}\right\}  .
\]

On a \( P\left( {A}_{n}\right) = 1/{2}^{n} \) , donc \( \mathop{\sum }\limits_{n}P\left( {A}_{n}\right) \) converge et d’après le lemme de Borel-Cantelli, on en déduit que l'ensemble des suites qui contiennent pour une infinité de valeurs de \( n \) , une série de \( n \) "piles" consécutifs à partir de la position \( n \) , est négligeable. De manière équivalente, une suite dans \( \Omega \) ne contient presque surement qu’un nombre fini (éventuellement vide) de valeurs de \( n \) , pour lesquels il y a \( n \) "piles" consécutifs à partir de la position \( n \) .

> We have \( P\left( {A}_{n}\right) = 1/{2}^{n} \) , so \( \mathop{\sum }\limits_{n}P\left( {A}_{n}\right) \) converges and according to the Borel-Cantelli lemma, we deduce that the set of sequences that contain, for an infinite number of values of \( n \) , a series of \( n \) consecutive "heads" starting from position \( n \) , is negligible. Equivalently, a sequence in \( \Omega \) almost surely contains only a finite number (possibly zero) of values of \( n \) for which there are \( n \) consecutive "heads" starting from position \( n \) .
