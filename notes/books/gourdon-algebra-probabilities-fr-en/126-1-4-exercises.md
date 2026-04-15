#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1. On dispose d'un jeu de 32 cartes. On rappelle que la couleur désigne carreau, coeur, pique ou trèfle, et que la hauteur désigne (dans l'ordre) : as, roi, dame, valet, 10, 9, 8, 7. On tire 5 cartes dans le paquet de 32 cartes.

> EXERCISE 1. We have a 32-card deck. Recall that the suit refers to diamonds, hearts, spades, or clubs, and the rank refers to (in order): ace, king, queen, jack, 10, 9, 8, 7. We draw 5 cards from the 32-card deck.

1/ Combien y a t-il de mains possibles?

> 1/ How many possible hands are there?

2/ Combien de mains contiennent :

> 2/ How many hands contain:

a) un carré (4 cartes de même hauteur et une autre carte)?

> a) a four-of-a-kind (4 cards of the same rank and one other card)?

b) un full (3 cartes de même hauteur et 2 autres de même hauteur)?

> b) a full house (3 cards of the same rank and 2 others of the same rank)?

c) une quinte flush (5 cartes de hauteurs consécutives dans une même couleur) ?

> c) a straight flush (5 cards of consecutive ranks in the same suit)?

d) une quinte (5 cartes de hauteurs consécutives pas toutes de même couleur)?

> d) a straight (5 cards of consecutive ranks not all of the same suit)?

Solution. 1 / Une main correspond à un sous-ensemble de 5 cartes parmi les 32 cartes, donc il y en a \( \left( \begin{matrix} {32} \\ 5 \end{matrix}\right) = \frac{{32} \times {31} \times {30} \times {29} \times {28}}{1 \times 2 \times 3 \times 4 \times 5} = {201376} \) .

> Solution. 1 / A hand corresponds to a subset of 5 cards from the 32 cards, so there are \( \left( \begin{matrix} {32} \\ 5 \end{matrix}\right) = \frac{{32} \times {31} \times {30} \times {29} \times {28}}{1 \times 2 \times 3 \times 4 \times 5} = {201376} \) .

2/a) Il y a 8 possibilités d'avoir 4 cartes de même hauteur (autant que de hauteurs), et la cinquième carte doit être choisie parmi les 28 cartes restantes. On en déduit qu'il y a \( 8 \times {28} = {224} \) carrés possibles.

> 2/a) There are 8 possibilities to have 4 cards of the same rank (as many as there are ranks), and the fifth card must be chosen from the 28 remaining cards. We deduce that there are \( 8 \times {28} = {224} \) possible four-of-a-kinds.

b) Pour chacune des 8 hauteurs, il y a \( \left( \begin{array}{l} 4 \\ 3 \end{array}\right) = 4 \) possibilités d’avoir trois cartes de cette hauteur, ce qui donne \( 8 \times 4 = {32} \) possibilités pour les trois premiers cartes. Les deux autres cartes doivent être de même hauteur parmi les 7 hauteurs restantes, donc au nombre de \( 7 \times \left( \begin{array}{l} 4 \\ 2 \end{array}\right) = 7 \times 6 = {42} \) . En tout on a donc \( {32} \times {42} = {1344} \) fulls possibles.

> b) For each of the 8 ranks, there are \( \left( \begin{array}{l} 4 \\ 3 \end{array}\right) = 4 \) possibilities to have three cards of that rank, which gives \( 8 \times 4 = {32} \) possibilities for the first three cards. The other two cards must be of the same rank among the 7 remaining ranks, so there are \( 7 \times \left( \begin{array}{l} 4 \\ 2 \end{array}\right) = 7 \times 6 = {42} \) . In total, there are \( {32} \times {42} = {1344} \) possible full houses.

c) Pour chaque couleur, il y a 4 possibilités d'avoir 5 cartes de hauteurs consécutives, donc \( 4 \times 4 = {16} \) quintes flush en tout.

> c) For each suit, there are 4 possibilities to have 5 cards of consecutive ranks, so \( 4 \times 4 = {16} \) straight flushes in total.

d) Si on ne tient pas compte de la couleur, il y a 4 possibilités d'avoir 5 cartes de hauteurs consé- cutives. Chacune peut prendre l'une quelconque des 4 couleurs donc cela fait \( 4 \times {4}^{5} \) possibilités d'avoir 5 cartes de hauteurs consécutives. En retirant les cas où les 5 cartes ont la même couleur (les quintes flush) cela donne \( 4 \times {4}^{5} - {16} = {4080} \) suites au total.

> d) If we do not take the suit into account, there are 4 possibilities to have 5 cards of consecutive ranks. Each can take any of the 4 suits, so that makes \( 4 \times {4}^{5} \) possibilities to have 5 cards of consecutive ranks. By removing the cases where the 5 cards have the same suit (the straight flushes), this gives \( 4 \times {4}^{5} - {16} = {4080} \) straights in total.

EXERCICE 2. Soit \( n \in {\mathbb{N}}^{ * } \) . a) Combien y a t-il de parties de \( \{ 1,2,\ldots ,{2n}\} \) qui contiennent autant de nombres pairs que impairs?

> EXERCISE 2. Let \( n \in {\mathbb{N}}^{ * } \) . a) How many subsets of \( \{ 1,2,\ldots ,{2n}\} \) contain as many even numbers as odd numbers?

b) Combien y a t-il de parties de \( \{ 1,2,\ldots ,{3n}\} \) qui contiennent autant de nombres divi-sibles par trois, que non-divisibles par trois ?

> b) How many subsets of \( \{ 1,2,\ldots ,{3n}\} \) contain as many numbers divisible by three as numbers not divisible by three?

Solution. a) Notons \( \mathcal{A} \) l’ensemble des parties concernées. Une partie \( P \) dans \( \mathcal{A} \) est constituée de \( k \) nombres pairs, choisis parmi les \( n \) nombres \( \{ 2,4,\ldots ,{2n}\} \) , et \( k \) nombres impairs, choisis parmi les \( n \) autres, pour un entier \( k \) vérifiant \( 0 \leq k \leq n \) . On en déduit

> Solution. a) Let \( \mathcal{A} \) be the set of subsets concerned. A subset \( P \) in \( \mathcal{A} \) consists of \( k \) even numbers, chosen from the \( n \) numbers \( \{ 2,4,\ldots ,{2n}\} \) , and \( k \) odd numbers, chosen from the \( n \) others, for an integer \( k \) satisfying \( 0 \leq k \leq n \) . We deduce

\[
\left| \mathcal{A}\right|  = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( \begin{array}{l} n \\  k \end{array}\right) }^{2} = \left( \begin{matrix} {2n} \\  n \end{matrix}\right)
\]

où on a utilisé la formule de Vandermonde pour la dernière égalité (voir la remarque qui suit la proposition 14 page 304, dans le cas où \( n = m = p \) ). On peut retrouver ce résultat sans passer par la formule de Vandermonde, en remarquant que \( \mathcal{A} \) est en bijection avec l’ensemble \( \mathcal{B} \) des parties de \( \{ 1,2,\ldots ,{2n}\} \) à \( n \) éléments : pour tout \( P \in \mathcal{A} \) , on associe \( Q \in \mathcal{B} \) défini par \( Q = {Q}_{0} \cup {Q}_{1} \) , où \( {Q}_{0} \) est l’ensemble des entiers pairs de \( P \) , et \( {Q}_{1} \) l’ensemble des entiers impairs de \( \{ 1,\ldots ,{2n}\} \) qui ne sont pas dans \( P \) . On a bien \( Q \in \mathcal{B} \) car \( \left| Q\right| = \left| {Q}_{1}\right| + \left| {Q}_{2}\right| = \left| {Q}_{1}\right| + \left( {n - \left| {Q}_{1}\right| }\right) = n \) .

> where we used Vandermonde's identity for the last equality (see the remark following proposition 14 on page 304, in the case where \( n = m = p \) ). This result can also be obtained without using Vandermonde's identity by noting that \( \mathcal{A} \) is in bijection with the set \( \mathcal{B} \) of subsets of \( \{ 1,2,\ldots ,{2n}\} \) with \( n \) elements: for any \( P \in \mathcal{A} \) , we associate \( Q \in \mathcal{B} \) defined by \( Q = {Q}_{0} \cup {Q}_{1} \) , where \( {Q}_{0} \) is the set of even integers in \( P \) , and \( {Q}_{1} \) is the set of odd integers in \( \{ 1,\ldots ,{2n}\} \) that are not in \( P \) . We indeed have \( Q \in \mathcal{B} \) because \( \left| Q\right| = \left| {Q}_{1}\right| + \left| {Q}_{2}\right| = \left| {Q}_{1}\right| + \left( {n - \left| {Q}_{1}\right| }\right) = n \) .

b) Le même raisonnement implique que le nombre de de parties recherchées est

> b) The same reasoning implies that the number of subsets sought is

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{matrix} {2n} \\  k \end{matrix}\right)  = \left( \begin{matrix} {3n} \\  n \end{matrix}\right)
\]

où on a également utilisé la formule de Vandermonde, dans le cas \( m = p = {2n} \) . Un raisonnement combinatoire similaire au précédent permet aussi de retrouver directement ce résultat.

> where we also used Vandermonde's identity, in the case \( m = p = {2n} \) . A combinatorial argument similar to the previous one also allows for this result to be obtained directly.

EXERCICE 3. Soit \( n \in {\mathbb{N}}^{ * } \) . 1/ Supposons \( n \geq 2 \) . Soit \( \left( {{a}_{1},{a}_{2},\ldots ,{a}_{2n}}\right) \) une suite de \( {2n} \) entiers naturels non nuls, telle que leur somme est \( \leq {3n} \) . Montrer qu’il existe \( i \) et \( j \) vérifiant \( 1 \leq i < j \leq {2n} \) , tels que \( {a}_{i + 1} + {a}_{i + 2} + \cdots + {a}_{j} = n - 1 \) .

> EXERCISE 3. Let \( n \in {\mathbb{N}}^{ * } \) . 1/ Suppose \( n \geq 2 \) . Let \( \left( {{a}_{1},{a}_{2},\ldots ,{a}_{2n}}\right) \) be a sequence of \( {2n} \) non-zero natural numbers such that their sum is \( \leq {3n} \) . Show that there exist \( i \) and \( j \) satisfying \( 1 \leq i < j \leq {2n} \) , such that \( {a}_{i + 1} + {a}_{i + 2} + \cdots + {a}_{j} = n - 1 \) .

2 / Soit \( A \) une partie de \( \{ 1,\ldots ,{2n}\} \) d’au moins \( n + 1 \) éléments. Montrer qu’il existe deux éléments distincts \( a \) et \( b \) dans \( A \) tels que \( a \) divise \( b \) .

> 2 / Let \( A \) be a subset of \( \{ 1,\ldots ,{2n}\} \) with at least \( n + 1 \) elements. Show that there exist two distinct elements \( a \) and \( b \) in \( A \) such that \( a \) divides \( b \) .

Solution. L’exercice repose sur le principe des tiroirs. \( 1/ \) Pour tout \( k,1 \leq k \leq {2n} \) on note \( {s}_{k} = {a}_{1} + \cdots + {a}_{k} \) et \( {t}_{k} = {s}_{k} + n - 1 \) . On a \( 1 \leq {s}_{1} < {s}_{2} < \ldots < {s}_{2n} \leq {3n} \) , et \( n \leq {t}_{1} < \ldots < {t}_{2n} \leq \; {4n} - 1 \) . Ainsi les \( {4n} \) valeurs \( {s}_{i} \) et \( {t}_{j} \) sont toutes dans \( \{ 1,\ldots ,{4n} - 1\} \) de cardinal \( {4n} - 1 \) . D’après le principes des tiroirs, il doit donc y avoir au moins deux valeurs égales parmi les \( {s}_{j} \) et les \( {t}_{i} \) , et comme les \( {s}_{j} \) sont différents deux à deux, et les \( {t}_{i} \) également, ceci signifie qu’il existe un des \( {s}_{j} \) égal à un des \( {t}_{i} \) . Ceci s’écrit \( {s}_{j} = {s}_{i} + n - 1 \) ou encore \( {s}_{j} - {s}_{i} = n - 1 \) , ce qu’il fallait démontrer. 2/ Tout élément \( m \) de \( A \) s’écrit de manière unique sous la forme \( m = {2}^{e}f\left( m\right) \) où \( e \in \mathbb{N} \) et \( f\left( m\right) \) est un entier impair. L’application \( f \) ainsi construite sur \( A \) est à valeurs dans \( B = \{ 1,3,\ldots ,{2n} - 1\} \) . Comme \( \left| B\right| = n < \left| A\right| \) , le principe des tiroirs affirme qu’il existe deux valeurs distinctes \( a < b \) de \( A \) pour lesquelles \( f\left( a\right) = f\left( b\right) \) . En notant \( q = f\left( a\right) \) ceci s’écrit \( a = {2}^{{e}_{1}}q \) et \( b = {2}^{{e}_{2}}q \) avec \( {e}_{1},{e}_{2} \in \mathbb{N} \) . Comme \( a < b \) on a \( {e}_{1} < {e}_{2} \) , donc \( a \) divise \( b \) .

> Solution. The exercise is based on the pigeonhole principle. \( 1/ \) For any \( k,1 \leq k \leq {2n} \) we denote \( {s}_{k} = {a}_{1} + \cdots + {a}_{k} \) and \( {t}_{k} = {s}_{k} + n - 1 \) . We have \( 1 \leq {s}_{1} < {s}_{2} < \ldots < {s}_{2n} \leq {3n} \) , and \( n \leq {t}_{1} < \ldots < {t}_{2n} \leq \; {4n} - 1 \) . Thus the \( {4n} \) values \( {s}_{i} \) and \( {t}_{j} \) are all in \( \{ 1,\ldots ,{4n} - 1\} \) with cardinality \( {4n} - 1 \) . According to the pigeonhole principle, there must therefore be at least two equal values among the \( {s}_{j} \) and the \( {t}_{i} \) , and since the \( {s}_{j} \) are distinct from each other, and the \( {t}_{i} \) as well, this means that there exists one of the \( {s}_{j} \) equal to one of the \( {t}_{i} \) . This is written \( {s}_{j} = {s}_{i} + n - 1 \) or \( {s}_{j} - {s}_{i} = n - 1 \) , which was to be demonstrated. 2/ Every element \( m \) of \( A \) can be written uniquely in the form \( m = {2}^{e}f\left( m\right) \) where \( e \in \mathbb{N} \) and \( f\left( m\right) \) is an odd integer. The mapping \( f \) thus constructed on \( A \) takes values in \( B = \{ 1,3,\ldots ,{2n} - 1\} \) . Since \( \left| B\right| = n < \left| A\right| \) , the pigeonhole principle asserts that there exist two distinct values \( a < b \) of \( A \) for which \( f\left( a\right) = f\left( b\right) \) . By denoting \( q = f\left( a\right) \) this is written \( a = {2}^{{e}_{1}}q \) and \( b = {2}^{{e}_{2}}q \) with \( {e}_{1},{e}_{2} \in \mathbb{N} \) . Since \( a < b \) we have \( {e}_{1} < {e}_{2} \) , therefore \( a \) divides \( b \) .

\( \rightarrow \) EXERCICE 4 (COMBINAISONS AVEC RÉPÉTITION). Soit \( E \) un ensemble fini, de cardinal \( n \in {\mathbb{N}}^{ * } \) . On appelle p-combinaison avec répétition de \( E \) toute \( p \) -liste de \( E \) dans laquelle on autorise les répétitions, mais dans laquelle l’ordre ne compte pas. On note \( \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \) le nombre de \( p \) -combinaisons avec répétitions de \( E \) .

> \( \rightarrow \) EXERCISE 4 (COMBINATIONS WITH REPETITION). Let \( E \) be a finite set, with cardinality \( n \in {\mathbb{N}}^{ * } \) . A p-combination with repetition of \( E \) is any \( p \) -list of \( E \) in which repetitions are allowed, but in which order does not count. We denote by \( \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \) the number of \( p \) -combinations with repetitions of \( E \) .

1/a) Montrer que \( \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \) est égal au nombre de \( n \) -listes \( \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) de \( \mathbb{N} \) qui vérifient \( {i}_{1} + \cdots + {i}_{n} = p \) (de telles \( n \) -listes sont appelées compositions de \( p \) en \( n \) sommants).

> 1/a) Show that \( \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \) is equal to the number of \( n \) -lists \( \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) of \( \mathbb{N} \) that satisfy \( {i}_{1} + \cdots + {i}_{n} = p \) (such \( n \) -lists are called compositions of \( p \) into \( n \) summands).

b) On note \( {\mathcal{F}}_{c}\left( {p, n}\right) \) l’ensemble des fonctions croissantes (au sens large) de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) . Montrer que \( \left| {{\mathcal{F}}_{c}\left( {p, n}\right) }\right| = \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \) .

> b) Let \( {\mathcal{F}}_{c}\left( {p, n}\right) \) be the set of non-decreasing functions from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \). Show that \( \left| {{\mathcal{F}}_{c}\left( {p, n}\right) }\right| = \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle \).

2/ Nous proposons trois méthodes différentes pour obtenir l'identité

> 2/ We propose three different methods to obtain the identity

\[
\left\langle  \begin{array}{l} n \\  p \end{array}\right\rangle   = \left( \begin{matrix} n + p - 1 \\  p \end{matrix}\right)
\]

(*)

> a) Prouver l'égalité (*) en montrant d'abord la relation

a) Prove the equality (*) by first showing the relation

\[
\forall n \geq  2,\forall p \geq  1,\;\left\langle  \begin{array}{l} n \\  p \end{array}\right\rangle   = \left\langle  \begin{matrix} n - 1 \\  p \end{matrix}\right\rangle   + \left\langle  \begin{matrix} n \\  p - 1 \end{matrix}\right\rangle  .
\]

\( \left( {* * }\right) \)

> b) Prouver (*) directement, en construisant une bijection de \( {\mathcal{F}}_{c}\left( {p, n}\right) \) vers l’ensemble des parties à \( p \) éléments de \( \{ 1,\ldots , n + p - 1\} \) .

b) Prove (*) directly by constructing a bijection from \( {\mathcal{F}}_{c}\left( {p, n}\right) \) to the set of subsets with \( p \) elements of \( \{ 1,\ldots , n + p - 1\} \).

> c) Prouver (*) en considérant le coefficient de \( {x}^{p} \) dans la série entière \( 1/{\left( 1 - x\right) }^{n} \) .

c) Prove (*) by considering the coefficient of \( {x}^{p} \) in the power series \( 1/{\left( 1 - x\right) }^{n} \).

> Solution. Notons que ceci revient à dire que les \( p \) -combinaisons avec répétition de \( E \) sont les classes d’équivalence des \( p \) -listes de \( E \) , pour la relation d’équivalence

Solution. Note that this amounts to saying that the \( p \)-combinations with repetition of \( E \) are the equivalence classes of \( p \)-lists of \( E \), for the equivalence relation

\[
\left( {{a}_{1},\ldots ,{a}_{p}}\right) \mathcal{R}\left( {{b}_{1},\ldots ,{b}_{p}}\right)  \Leftrightarrow  \exists \sigma  \in  {\mathcal{S}}_{p},\left( {{a}_{1},\ldots ,{a}_{p}}\right)  = \left( {{b}_{\sigma \left( 1\right) },\ldots ,{b}_{\sigma \left( p\right) }}\right) .
\]

1/ Notons \( {x}_{1},\ldots ,{x}_{n} \) les éléments de \( E \) . A toute \( p \) -combinaison avec répétition \( P \) , on associe la composition \( c = \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) de \( p \) en \( n \) sommants, où \( {i}_{k} \) est le nombre de fois que \( {x}_{k} \) apparait dans \( P \) . Ainsi construite, \( \varphi \) est une bijection de l’ensemble des \( p \) -combinaisons avec répétition de \( E \) , vers l’ensemble des compositions de \( p \) en \( n \) sommants, d’où le résultat.

> 1/ Let \( {x}_{1},\ldots ,{x}_{n} \) be the elements of \( E \). To any \( p \)-combination with repetition \( P \), we associate the composition \( c = \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) of \( p \) into \( n \) summands, where \( {i}_{k} \) is the number of times \( {x}_{k} \) appears in \( P \). Constructed this way, \( \varphi \) is a bijection from the set of \( p \)-combinations with repetition of \( E \) to the set of compositions of \( p \) into \( n \) summands, hence the result.

b) Soit \( a \) une \( p \) -combinaison avec répétition de \( E \) . Parmi les représentants \( \left( {{x}_{{i}_{1}},{x}_{{i}_{2}},\ldots ,{x}_{{i}_{p}}}\right) \) de \( a \) , il en existe un unique pour lequel \( {i}_{1} \leq {i}_{2} \leq \ldots \leq {i}_{p} \) . On note \( {f}_{a}\left( 1\right) \leq \ldots \leq {f}_{a}\left( p\right) \) les indices correspondants. La fonction \( {f}_{a} \) est bien dans \( {\mathcal{F}}_{c}\left( {p, n}\right) \) . La fonction \( a \mapsto {f}_{a} \) est une bijection des \( p \) -combinaisons avec répétition de \( E \) , vers \( {\mathcal{F}}_{c}\left( {p, n}\right) \) . D’où le résultat.

> b) Let \( a \) be a \( p \)-combination with repetition of \( E \). Among the representatives \( \left( {{x}_{{i}_{1}},{x}_{{i}_{2}},\ldots ,{x}_{{i}_{p}}}\right) \) of \( a \), there exists a unique one for which \( {i}_{1} \leq {i}_{2} \leq \ldots \leq {i}_{p} \). Let \( {f}_{a}\left( 1\right) \leq \ldots \leq {f}_{a}\left( p\right) \) be the corresponding indices. The function \( {f}_{a} \) is indeed in \( {\mathcal{F}}_{c}\left( {p, n}\right) \). The function \( a \mapsto {f}_{a} \) is a bijection from the \( p \)-combinations with repetition of \( E \) to \( {\mathcal{F}}_{c}\left( {p, n}\right) \). Hence the result.

2/a) Supposons \( n \geq 2 \) et \( p \geq 1 \) . On partitionne les compositions \( \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) de \( p \) en \( n \) sommants, en deux parties. D’abord celles pour laquelle \( {i}_{1} = 0 \) . Il y en a \( \left\langle \begin{matrix} n - 1 \\ p \end{matrix}\right\rangle \) . Ensuite celles pour lesquelles \( {i}_{1} \geq 1 \) . On notant \( {i}_{1}^{\prime } = {i}_{1} - 1 \geq 0 \) , on voit que ces dernières sont en bijection avec les \( n \) -listes \( \left( {{i}_{1}^{\prime },{i}_{2},\ldots ,{i}_{n}}\right) \) de \( \mathbb{N} \) , telles que \( {i}_{1}^{\prime } + {i}_{2} + \ldots + {i}_{n} = p - 1 \) , donc au nombre de \( \left\langle \begin{matrix} n \\ p - 1 \end{matrix}\right\rangle \) . On a donc bien démontré la relation (**).

> 2/a) Suppose \( n \geq 2 \) and \( p \geq 1 \) . We partition the compositions \( \left( {{i}_{1},\ldots ,{i}_{n}}\right) \) of \( p \) into \( n \) summands into two parts. First, those for which \( {i}_{1} = 0 \) . There are \( \left\langle \begin{matrix} n - 1 \\ p \end{matrix}\right\rangle \) of them. Then, those for which \( {i}_{1} \geq 1 \) . By noting \( {i}_{1}^{\prime } = {i}_{1} - 1 \geq 0 \) , we see that the latter are in bijection with the \( n \) -lists \( \left( {{i}_{1}^{\prime },{i}_{2},\ldots ,{i}_{n}}\right) \) of \( \mathbb{N} \) such that \( {i}_{1}^{\prime } + {i}_{2} + \ldots + {i}_{n} = p - 1 \) , and thus there are \( \left\langle \begin{matrix} n \\ p - 1 \end{matrix}\right\rangle \) of them. We have therefore successfully proven the relation (**).

Pour obtenir (*), on va montrer que \( A\left( {n, p}\right) = \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle - \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \) est nul, ce qui prouvera le résultat demandé. La formule de Pascal entraîne que \( A\left( {n, p}\right) = A\left( {n - 1, p}\right) + A\left( {n, p - 1}\right) \) . Pour prouver que \( A\left( {n, p}\right) = 0 \) pour tout \( p \in \mathbb{N} \) , on procède ensuite par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) cette propriété est vraie car \( \left\langle \begin{array}{l} 1 \\ p \end{array}\right\rangle = 1 \) , donc \( A\left( {1, p}\right) = 0 \) . Supposons la propriété vraie pour \( n - 1 \) . Comme \( A\left( {n - 1, p}\right) = 0 \) , la relation obtenue plus haut entraîne \( A\left( {n, p}\right) = A\left( {n, p - 1}\right) \) pour tout \( p \geq 1 \) . En particulier \( A\left( {n, p}\right) = A\left( {n,0}\right) \) . Comme \( \left\langle \begin{array}{l} n \\ 0 \end{array}\right\rangle = 1 \) , on a bien \( A\left( {n,0}\right) = 0 \) , donc la propriété est prouvée au rang \( n \) .

> To obtain (*), we will show that \( A\left( {n, p}\right) = \left\langle \begin{array}{l} n \\ p \end{array}\right\rangle - \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \) is zero, which will prove the requested result. Pascal's formula implies that \( A\left( {n, p}\right) = A\left( {n - 1, p}\right) + A\left( {n, p - 1}\right) \) . To prove that \( A\left( {n, p}\right) = 0 \) for all \( p \in \mathbb{N} \) , we then proceed by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , this property is true because \( \left\langle \begin{array}{l} 1 \\ p \end{array}\right\rangle = 1 \) , so \( A\left( {1, p}\right) = 0 \) . Assume the property is true for \( n - 1 \) . Since \( A\left( {n - 1, p}\right) = 0 \) , the relation obtained above implies \( A\left( {n, p}\right) = A\left( {n, p - 1}\right) \) for all \( p \geq 1 \) . In particular, \( A\left( {n, p}\right) = A\left( {n,0}\right) \) . Since \( \left\langle \begin{array}{l} n \\ 0 \end{array}\right\rangle = 1 \) , we indeed have \( A\left( {n,0}\right) = 0 \) , so the property is proven at rank \( n \) .

b) Considérons une fonction \( f \) croissante de \( \{ 1,\ldots , p\} \) vers \( \{ 1,\ldots , n\} \) . On construit une partie de \( \{ 1,\ldots , n + p - 1\} \) par \( \varphi \left( f\right) = \{ f\left( 1\right) , f\left( 2\right) + 1,\ldots , f\left( p\right) + p - 1\} \) . Comme \( f \) est croissante, les \( f\left( k\right) + k - 1 \) sont distincts et donc \( \varphi \left( f\right) \) est bien une partie à \( p \) éléments. \( \varphi \) est injective. Réciproquement, considérons une partie \( P \) de \( \{ 1,\ldots , n + p - 1\} \) à \( p \) éléments. On peut écrire \( P = \left\{ {{a}_{1},\ldots ,{a}_{p}}\right\} \) avec \( {a}_{1} < \ldots < {a}_{p} \) . La fonction \( f\left( k\right) = {a}_{k} - \left( {k - 1}\right) \) est bien une fonction croissante de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) . Ainsi, on a montré que \( \varphi \) est bijective. On en déduit l'égalité (*) d'après le résultat de la question 1/b).

> b) Let us consider an increasing function \( f \) from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \). We construct a subset of \( \{ 1,\ldots , n + p - 1\} \) by \( \varphi \left( f\right) = \{ f\left( 1\right) , f\left( 2\right) + 1,\ldots , f\left( p\right) + p - 1\} \). Since \( f \) is increasing, the \( f\left( k\right) + k - 1 \) are distinct and therefore \( \varphi \left( f\right) \) is indeed a subset with \( p \) elements. \( \varphi \) is injective. Conversely, let us consider a subset \( P \) of \( \{ 1,\ldots , n + p - 1\} \) with \( p \) elements. We can write \( P = \left\{ {{a}_{1},\ldots ,{a}_{p}}\right\} \) with \( {a}_{1} < \ldots < {a}_{p} \). The function \( f\left( k\right) = {a}_{k} - \left( {k - 1}\right) \) is indeed an increasing function from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \). Thus, we have shown that \( \varphi \) is bijective. We deduce the equality (*) from the result of question 1/b).

c) Rappelons qu’on a le développement en série entière \( 1/\left( {1 - x}\right) = \mathop{\sum }\limits_{{n > 0}}{x}^{n} \) , valable lorsque \( \left| x\right| < 1 \) . Par produit de Cauchy, on a lorsque \( \left| x\right| < 1 \)

> c) Recall that we have the power series expansion \( 1/\left( {1 - x}\right) = \mathop{\sum }\limits_{{n > 0}}{x}^{n} \), valid when \( \left| x\right| < 1 \). By Cauchy product, we have when \( \left| x\right| < 1 \)

\[
\frac{1}{{\left( 1 - x\right) }^{n}} = \left( {\mathop{\sum }\limits_{{{i}_{1} \geq  0}}{x}^{{i}_{1}}}\right) \cdots \left( {\mathop{\sum }\limits_{{{i}_{n} \geq  0}}{x}^{{i}_{n}}}\right)  = \mathop{\sum }\limits_{{{i}_{1},\ldots {i}_{n} \geq  0}}{x}^{{i}_{1} + \cdots  + {i}_{n}} = \mathop{\sum }\limits_{{p \geq  0}}{a}_{p}{x}^{p},\;{a}_{p} = \mathop{\sum }\limits_{{{i}_{1} + \cdots  + {i}_{n} = p}}1.
\]

On remarque que le coefficient \( {a}_{p} \) est le nombre de compositions de \( p \) en \( n \) sommants. Donc d’après \( 1/\mathrm{a}) \) , il suffit de montrer \( {a}_{p} = \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \) . Pour cela, on dérive \( n - 1 \) fois la série entière \( f\left( x\right) = 1/\left( {1 - x}\right) \) . On obtient, pour tout \( x \) tel que \( \left| x\right| < 1 \)

> We note that the coefficient \( {a}_{p} \) is the number of compositions of \( p \) into \( n \) summands. Therefore, according to \( 1/\mathrm{a}) \), it suffices to show \( {a}_{p} = \left( \begin{matrix} n + p - 1 \\ p \end{matrix}\right) \). To do this, we differentiate the power series \( f\left( x\right) = 1/\left( {1 - x}\right) \) \( n - 1 \) times. We obtain, for all \( x \) such that \( \left| x\right| < 1 \)

\[
{f}^{\left( n - 1\right) }\left( x\right)  = \frac{\left( {n - 1}\right) !}{{\left( 1 - x\right) }^{n}} = \mathop{\sum }\limits_{{k \geq  n - 1}}k\left( {k - 1}\right) \cdots \left( {k - n + 2}\right) {x}^{k - \left( {n - 1}\right) }.
\]

Par identification avec la valeur du coefficient de \( {x}^{p} \) , on en déduit

> By identification with the value of the coefficient of \( {x}^{p} \), we deduce

\[
\left( {n - 1}\right) !{a}_{p} = \left( {n - 1 + p}\right) \cdots \left( {p + 1}\right)  = \frac{\left( {n + p - 1}\right) !}{p!},\;\text{ d’où }\;{a}_{p} = \left( \begin{matrix} n + p - 1 \\  p \end{matrix}\right) .
\]

EXERCICE 5. Soit \( n \) et \( p \in {\mathbb{N}}^{ * } \) avec \( p \leq n \) . 1/On note \( {\mathcal{F}}_{s}\left( {p, n}\right) \) l’ensemble des fonctions strictement croissantes de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) . Calculer \( \left| {{\mathcal{F}}_{s}\left( {p, n}\right) }\right| \) .

> EXERCISE 5. Let \( n \) and \( p \in {\mathbb{N}}^{ * } \) with \( p \leq n \) . 1/Let \( {\mathcal{F}}_{s}\left( {p, n}\right) \) be the set of strictly increasing functions from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \) . Calculate \( \left| {{\mathcal{F}}_{s}\left( {p, n}\right) }\right| \) .

2/a) Soit \( \ell \in {\mathbb{N}}^{ * } \) tel que \( n - p \geq \left( {p - 1}\right) \ell \) . Compter le nombre de fonctions \( f \) de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) telles que \( f\left( {k + 1}\right) > f\left( k\right) + \ell \) , pour \( 1 \leq k \leq p - 1 \) .

> 2/a) Let \( \ell \in {\mathbb{N}}^{ * } \) be such that \( n - p \geq \left( {p - 1}\right) \ell \) . Count the number of functions \( f \) from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \) such that \( f\left( {k + 1}\right) > f\left( k\right) + \ell \) , for \( 1 \leq k \leq p - 1 \) .

b) Un ensemble de \( n \) personnes se répartit entre \( p \) adultes et \( n - p \) enfants. Compter combien il y a de façon de placer les \( n \) personnes sur un banc, de sorte qu’entre deux adultes on ait toujours au moins \( \ell \) enfants (quelle que soit la paire d’adulte).

> b) A group of \( n \) people is divided into \( p \) adults and \( n - p \) children. Count how many ways there are to seat the \( n \) people on a bench, such that between any two adults there is always at least \( \ell \) children (regardless of the pair of adults).

c) On suppose ici \( n \geq p\left( {\ell + 1}\right) \) . Combien y a t-il de façons de placer les \( p \) adultes et \( n - p \) enfants autour d'une table ronde, de sorte qu'entre deux adultes (de part et d'autre de la table) il y ait toujours au moins \( \ell \) enfants ? (on précise ici que seul compte le placement relatif des personnes autour de la table). à considérer les ensembles suivant :

> c) Assume here \( n \geq p\left( {\ell + 1}\right) \) . How many ways are there to seat the \( p \) adults and \( n - p \) children around a round table, such that between any two adults (on either side of the table) there is always at least \( \ell \) children? (note that only the relative placement of people around the table matters). Consider the following sets:

\[
{\mathcal{A}}_{k} = \{ P \in  \mathcal{A} \mid  P \cap  \{ 1,\ldots ,\ell \}  = \{ k\} \} ,\;\left( {1 \leq  k \leq  \ell }\right) ,
\]

\[
{\mathcal{A}}^{ * } = \{ P \in  \mathcal{A} \mid  P \cap  \{ 1,\ldots ,\ell \}  = \varnothing \} .
\]

---

Solution. 1/ On va montrer que \( {\mathcal{F}}_{s}\left( {p, n}\right) \) en est bijection avec les parties de \( \{ 1,\ldots , n\} \) à \( p \) éléments. Considérons une fonction \( f \) strictement croissante de \( \{ 1,\ldots , p\} \) vers \( \{ 1,\ldots , n\} \) . On construit une partie de \( \{ 1,\ldots , n\} \) par \( \varphi \left( f\right) = \{ f\left( 1\right) , f\left( 2\right) ,\ldots , f\left( p\right) \} \) . Comme \( f \) est stricte-ment croissante, les \( f\left( k\right) \) sont distincts et donc \( \varphi \left( f\right) \) est bien une partie à \( p \) éléments. \( \varphi \) est injective. Réciproquement, considérons une partie \( P \) de \( \{ 1,\ldots , n\} \) à \( p \) éléments. On peut écrire \( P = \left\{ {{a}_{1},\ldots ,{a}_{p}}\right\} \) avec \( {a}_{1} < \ldots < {a}_{p} \) . La fonction \( f\left( k\right) = {a}_{k} \) est bien une fonction strictement croissante de \( \{ 1,\ldots , p\} \) dans \( \{ 1,\ldots , n\} \) . Ainsi, on a montré que \( \varphi \) est bijective. On en déduit \( \left| {{\mathcal{F}}_{s}\left( {p, n}\right) }\right| = \left( \begin{array}{l} n \\ p \end{array}\right) . \)

> Solution. 1/ We will show that \( {\mathcal{F}}_{s}\left( {p, n}\right) \) is in bijection with the subsets of \( \{ 1,\ldots , n\} \) with \( p \) elements. Consider a strictly increasing function \( f \) from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \) . We construct a subset of \( \{ 1,\ldots , n\} \) by \( \varphi \left( f\right) = \{ f\left( 1\right) , f\left( 2\right) ,\ldots , f\left( p\right) \} \) . Since \( f \) is strictly increasing, the \( f\left( k\right) \) are distinct and therefore \( \varphi \left( f\right) \) is indeed a subset with \( p \) elements. \( \varphi \) is injective. Conversely, consider a subset \( P \) of \( \{ 1,\ldots , n\} \) with \( p \) elements. We can write \( P = \left\{ {{a}_{1},\ldots ,{a}_{p}}\right\} \) with \( {a}_{1} < \ldots < {a}_{p} \) . The function \( f\left( k\right) = {a}_{k} \) is indeed a strictly increasing function from \( \{ 1,\ldots , p\} \) to \( \{ 1,\ldots , n\} \) . Thus, we have shown that \( \varphi \) is bijective. We deduce \( \left| {{\mathcal{F}}_{s}\left( {p, n}\right) }\right| = \left( \begin{array}{l} n \\ p \end{array}\right) . \)

2/a) Notons \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \) l’ensemble des fonctions en question. Pour toute fonction \( f \) de \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \) , on construit la fonction \( g = \varphi \left( f\right) \) de \( {\mathcal{F}}_{s}\left( {p, n - \left( {p - 1}\right) \ell }\right) \) par : \( g\left( k\right) = f\left( k\right) - \left( {k - 1}\right) \ell \) . Il est clair que les conditions sur \( f \) sont équivalentes à dire que \( g \) est strictement croissante. Donc \( \varphi \) est bijective, et \( \left| {{\mathcal{F}}_{\ell }\left( {p, n}\right) }\right| = \left| {{\mathcal{F}}_{s}(p, n - \left( {p - 1}\right) \ell }\right| = \left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \) .

> 2/a) Let \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \) be the set of functions in question. For any function \( f \) in \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \), we construct the function \( g = \varphi \left( f\right) \) from \( {\mathcal{F}}_{s}\left( {p, n - \left( {p - 1}\right) \ell }\right) \) by: \( g\left( k\right) = f\left( k\right) - \left( {k - 1}\right) \ell \). It is clear that the conditions on \( f \) are equivalent to saying that \( g \) is strictly increasing. Thus \( \varphi \) is bijective, and \( \left| {{\mathcal{F}}_{\ell }\left( {p, n}\right) }\right| = \left| {{\mathcal{F}}_{s}(p, n - \left( {p - 1}\right) \ell }\right| = \left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \).

b) On compte d’abord les façons de placer les adultes. Notons \( {i}_{1} < \ldots < {i}_{p} \) leur emplacement sur le banc. Avoir au moins \( \ell \) enfants entre chaque adulte, revient à avoir \( {i}_{k + 1} - {i}_{k} > \ell \) pour \( 1 \leq k \leq p - 1 \) . Ainsi il y a autant de façons d’avoir des emplacements d’adultes que de fonctions dans \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \) , donc \( \left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \) façons. Pour chacun, il y a \( p \) ! placements d’adultes, et il y a ensuite \( \left( {n - p}\right) \) ! façons de placer les \( n - p \) enfants sur les \( n - p \) places restantes. Le nombre de façons de placer les \( n \) personnes sur le banc pour avoir toujours au moins \( \ell \) enfants entre deux adultes est donc égal à \( p!\left( {n - p}\right) !\left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \) .

> b) We first count the ways to place the adults. Let \( {i}_{1} < \ldots < {i}_{p} \) be their positions on the bench. Having at least \( \ell \) children between each adult is equivalent to having \( {i}_{k + 1} - {i}_{k} > \ell \) for \( 1 \leq k \leq p - 1 \). Thus, there are as many ways to have adult positions as there are functions in \( {\mathcal{F}}_{\ell }\left( {p, n}\right) \), so \( \left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \) ways. For each, there are \( p \)! adult placements, and there are then \( \left( {n - p}\right) \)! ways to place the \( n - p \) children in the \( n - p \) remaining spots. The number of ways to place the \( n \) people on the bench such that there is always at least \( \ell \) children between two adults is therefore equal to \( p!\left( {n - p}\right) !\left( \begin{matrix} n - \left( {p - 1}\right) \ell \\ p \end{matrix}\right) \).

c) On numérote les emplacements de la table de 1 à \( n \) . Les places prises par les adultes autour de la table correspondent à une partie \( P \) de \( \{ 1,\ldots , n\} \) à \( p \) éléments (pour le moment on ne considère que les placements absolus autour de la table, i.e. on différencie les placements relatifs, et on ne prend en compte que les places prises par les adultes). Les placements possibles sont plus restreints que sur un banc car entre l'adulte d'emplacement de plus petit indice et celui du plus grand indice, on doit avoir au moins \( \ell \) enfants (du coté où on passe de l’emplacement \( n \) à l’emplacement 1). Désignons par \( \mathcal{A} \) l’ensemble des façons d’avoir des places d’adultes autour de la table. On a \( P \in \mathcal{A} \) si et seulement si les éléments \( {i}_{1},\ldots ,{i}_{p} \) de \( P \) , rangés en ordre croissants, vérifient \( {i}_{k + 1} - {i}_{k} > \ell \) pour \( 1 \leq k \leq p - 1 \) , et \( {i}_{1} + n - {i}_{p} > \ell \) . On partitionne les placements de \( \mathcal{A} \) en fonction du fait que le plus petit élément \( {i}_{1} \) de \( P \) vérifie \( 1 \leq {i}_{1} \leq \ell \) ou \( {i}_{1} > \ell \) . Ceci revient

> c) The table positions are numbered from 1 to \( n \). The seats taken by the adults around the table correspond to a subset \( P \) of \( \{ 1,\ldots , n\} \) with \( p \) elements (for now, we only consider absolute positions around the table, i.e., we differentiate relative positions, and we only take into account the seats taken by the adults). The possible placements are more restricted than on a bench because between the adult at the position with the smallest index and the one at the position with the largest index, there must be at least \( \ell \) children (on the side where one goes from position \( n \) to position 1). Let \( \mathcal{A} \) denote the set of ways to have adult seats around the table. We have \( P \in \mathcal{A} \) if and only if the elements \( {i}_{1},\ldots ,{i}_{p} \) of \( P \), arranged in increasing order, satisfy \( {i}_{k + 1} - {i}_{k} > \ell \) for \( 1 \leq k \leq p - 1 \), and \( {i}_{1} + n - {i}_{p} > \ell \). We partition the placements of \( \mathcal{A} \) based on whether the smallest element \( {i}_{1} \) of \( P \) satisfies \( 1 \leq {i}_{1} \leq \ell \) or \( {i}_{1} > \ell \). This amounts to

---

- Choisir \( P \in  {\mathcal{A}}_{k} \) revient à placer les \( p - 1 \) autres adultes, sur le banc constitué des emplacements \( k + \ell  + 1, k + \ell  + 2,\ldots , k + n - \ell  - 1 \) , de sorte qu’entre deux adultes il y a toujours au moins \( \ell \) enfants. Il y a \( n - 2\ell  - 1 \) places sur ce banc, d’après ce qui a été vu dans la solution de la question précédente, on déduit \( \left| {\mathcal{A}}_{k}\right|  = \left( \begin{matrix} n - 2\ell  - 1 - \left( {p - 2}\right) \ell \\  p - 1 \end{matrix}\right) \) .

> - Choosing \( P \in  {\mathcal{A}}_{k} \) amounts to placing the \( p - 1 \) other adults on the bench consisting of positions \( k + \ell  + 1, k + \ell  + 2,\ldots , k + n - \ell  - 1 \), such that between two adults there are always at least \( \ell \) children. There are \( n - 2\ell  - 1 \) seats on this bench; based on what was seen in the solution to the previous question, we deduce \( \left| {\mathcal{A}}_{k}\right|  = \left( \begin{matrix} n - 2\ell  - 1 - \left( {p - 2}\right) \ell \\  p - 1 \end{matrix}\right) \).

- Choisir \( P \in  {\mathcal{A}}^{ * } \) revient à placer sur le banc constitué des emplacements \( \ell  + 1,\ldots , n \) les \( p \) adultes, de sorte qu’entre deux adultes il y ait toujours au moins \( \ell \) enfants. Comme vu précédemment, on a donc \( \left| {\mathcal{A}}^{ * }\right|  = \left( \begin{matrix} n - \ell  - \left( {p - 1}\right) \ell \\  p \end{matrix}\right) \) .

> - Choosing \( P \in  {\mathcal{A}}^{ * } \) amounts to placing the \( p \) adults on the bench consisting of positions \( \ell  + 1,\ldots , n \), such that between two adults there are always at least \( \ell \) children. As seen previously, we therefore have \( \left| {\mathcal{A}}^{ * }\right|  = \left( \begin{matrix} n - \ell  - \left( {p - 1}\right) \ell \\  p \end{matrix}\right) \).

Comme les \( {\left( {\mathcal{A}}_{k}\right) }_{1 \leq k \leq \ell } \) et \( {\mathcal{A}}^{ * } \) forment une partition de \( \mathcal{A} \) , on en déduit

> Since \( {\left( {\mathcal{A}}_{k}\right) }_{1 \leq k \leq \ell } \) and \( {\mathcal{A}}^{ * } \) form a partition of \( \mathcal{A} \), we deduce

\[
\left| \mathcal{A}\right|  = \mathop{\sum }\limits_{{k = 1}}^{\ell }\left| {\mathcal{A}}_{k}\right|  + \left| {\mathcal{A}}^{ * }\right|  = \ell \left( \begin{matrix} n - p\ell  - 1 \\  p - 1 \end{matrix}\right)  + \left( \begin{matrix} n - p\ell \\  p \end{matrix}\right)  = \frac{n}{n - p\ell }\left( \begin{matrix} n - p\ell \\  p \end{matrix}\right) .
\]

Pour chaque possibilité d’emplacements d’adultes dans \( \mathcal{A} \) , on a \( p \) ! placements possibles d’adultes, et \( \left( {n - p}\right) \) ! placements possibles pour les enfants sur les \( n - p \) places restantes. Ainsi il y a en tout \( p!\left( {n - p}\right) !\frac{n}{n - p\ell }\left( \begin{matrix} n - p\ell \\ p \end{matrix}\right) \) placements possibles des \( n \) personnes. Rappelons nous qu’on ne tient compte que des placements relatifs autour de la table, il faut diviser ce nombre par \( n \) (à chaque placement relatif des \( n \) personnes autour de la table correspond \( n \) placements absolus possibles, en les faisant tourner autour de la table), donc le résultat demandé est \( \frac{p!\left( {n - p}\right) !}{n - p\ell }\left( \begin{matrix} n - p\ell \\ p \end{matrix}\right) \) .

> For each possible arrangement of adults in \( \mathcal{A} \), there are \( p \)! possible placements for adults, and \( \left( {n - p}\right) \)! possible placements for children in the \( n - p \) remaining seats. Thus, there are a total of \( p!\left( {n - p}\right) !\frac{n}{n - p\ell }\left( \begin{matrix} n - p\ell \\ p \end{matrix}\right) \) possible placements for the \( n \) people. Recalling that we only consider relative placements around the table, we must divide this number by \( n \) (each relative placement of the \( n \) people around the table corresponds to \( n \) possible absolute placements by rotating them around the table), so the requested result is \( \frac{p!\left( {n - p}\right) !}{n - p\ell }\left( \begin{matrix} n - p\ell \\ p \end{matrix}\right) \).

Remarque. La formule obtenue dans \( 2/\mathrm{a} \) ) lorsque \( \ell = - 1 \) est compatible avec le résultat de la question 2/b) de l'exercice 4 page 306 sur les combinaisons avec répétition.

> Note. The formula obtained in \( 2/\mathrm{a} \) when \( \ell = - 1 \) is consistent with the result of question 2/b) of exercise 4 on page 306 regarding combinations with repetition.

EXERCICE 6. \( \mathbf{1}/ \) Soit \( n \in {\mathbb{N}}^{ * } \) . Donner une forme close des expressions suivantes :

> EXERCISE 6. \( \mathbf{1}/ \) Let \( n \in {\mathbb{N}}^{ * } \). Provide a closed form for the following expressions:

\[
\mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }\left( \begin{matrix} n \\  {2k} \end{matrix}\right) ,\;\mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/3\right\rbrack  }\left( \begin{matrix} n \\  {3k} \end{matrix}\right) ,\;\mathop{\sum }\limits_{{k = 0}}^{n}\frac{1}{k + 1}\left( \begin{array}{l} n \\  k \end{array}\right) ,\;\mathop{\sum }\limits_{{k = 0}}^{n}{k}^{2}\left( \begin{array}{l} n \\  k \end{array}\right) ,\;\mathop{\sum }\limits_{{k = 0}}^{n}k{\left( \begin{array}{l} n \\  k \end{array}\right) }^{2}.
\]

2/ Prouver les identités suivantes, pour \( n \in {\mathbb{N}}^{ * } \) :

> 2/ Prove the following identities, for \( n \in {\mathbb{N}}^{ * } \):

\[
\text{ a) }\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{matrix} {2n} - k \\  n \end{matrix}\right)  = 1,\;\text{ b) }\;\mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}{\left( \begin{array}{l} n \\  k \end{array}\right) }^{2}{\left( \begin{array}{l} {2n} \\  k \end{array}\right) }^{-1} = {\left( \begin{matrix} {2n} \\  n \end{matrix}\right) }^{-1}\text{ . }
\]

Solution. 1/ Notons \( {E}_{k} \) la \( k \) -ième expression.

> Solution. 1/ Let \( {E}_{k} \) be the \( k \)-th expression.

(1) Pour déterminer \( {E}_{1} \) , on utilise la formule du binôme qui permet d’écrire

> (1) To determine \( {E}_{1} \), we use the binomial theorem, which allows us to write

\[
{2}^{n} = {\left( 1 + 1\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \;\text{ et }\;0 = {\left( 1 - 1\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {\left( -1\right) }^{k}.
\]

Par sommation de ces deux sommes, on déduit \( {2}^{n} = 2{E}_{1} \) , donc \( {E}_{1} = {2}^{n - 1} \) .

> By summing these two sums, we deduce \( {2}^{n} = 2{E}_{1} \), therefore \( {E}_{1} = {2}^{n - 1} \).

(2) On procède de manière similaire pour la deuxième expression \( {E}_{2} \) ,à partir de la formule du binôme. Ici on écrit, en notant \( j = \exp \left( {{2i\pi }/3}\right) \) :

> (2) We proceed similarly for the second expression \( {E}_{2} \), starting from the binomial theorem. Here we write, by denoting \( j = \exp \left( {{2i\pi }/3}\right) \):

\[
\forall m \in  \{ 0,1,2\} ,\;{B}_{m} = {\left( 1 + {j}^{m}\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( {j}^{m}\right) }^{n}\left( \begin{array}{l} n \\  k \end{array}\right) .
\]

Par sommation on obtient

> By summation, we obtain

\[
{B}_{0} + {B}_{1} + {B}_{2} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( {1 + {j}^{n} + {j}^{2n}}\right) \left( \begin{array}{l} n \\  k \end{array}\right) .
\]

(*)

> Or \( 1 + {j}^{n} + {j}^{2n} = 1 + {j}^{r} + {j}^{2r} \) où \( r \) est le reste de la division par 3 de \( n \) , donc \( 1 + {j}^{n} + {j}^{2n} = 3 \) si 3 divise \( n \) , et \( 1 + {j}^{n} + {j}^{2n} = 0 \) sinon. L’expression (*) entraîne donc

However, \( 1 + {j}^{n} + {j}^{2n} = 1 + {j}^{r} + {j}^{2r} \) where \( r \) is the remainder of the division of \( n \) by 3, so \( 1 + {j}^{n} + {j}^{2n} = 3 \) if 3 divides \( n \), and \( 1 + {j}^{n} + {j}^{2n} = 0 \) otherwise. The expression (*) therefore leads to

\[
{B}_{0} + {B}_{1} + {B}_{2} = 3{E}_{2},\;\text{ donc }\;{E}_{2} = \frac{1}{3}\left( {{\left( 1 + 1\right) }^{n} + {\left( 1 + j\right) }^{n} + {\left( 1 + {j}^{2}\right) }^{n}}\right) .
\]

Comme \( 1 + j = - {j}^{2} \) et \( 1 + {j}^{2} = - j \) , on a \( {\left( 1 + j\right) }^{n} + {\left( 1 + {j}^{2}\right) }^{n} = 2\cos \left( {{n\pi }/3}\right) \) . Finalement on a \( {E}_{2} = \left( {{2}^{n} + 2\cos \left( {{n\pi }/3}\right) }\right) /3. \)

> Since \( 1 + j = - {j}^{2} \) and \( 1 + {j}^{2} = - j \), we have \( {\left( 1 + j\right) }^{n} + {\left( 1 + {j}^{2}\right) }^{n} = 2\cos \left( {{n\pi }/3}\right) \). Finally, we have \( {E}_{2} = \left( {{2}^{n} + 2\cos \left( {{n\pi }/3}\right) }\right) /3. \)

(3) On reconnait que \( \frac{1}{k + 1}\left( \begin{array}{l} n \\ k \end{array}\right) \) est le coefficient de \( {x}^{k + 1} \) dans la primitive de \( \left( \begin{array}{l} n \\ k \end{array}\right) {x}^{k} \) . Ceci nous invite à intégrer la formule du binôme, appliquée à \( {\left( 1 + x\right) }^{n} \) . On écrit

> (3) We recognize that \( \frac{1}{k + 1}\left( \begin{array}{l} n \\ k \end{array}\right) \) is the coefficient of \( {x}^{k + 1} \) in the primitive of \( \left( \begin{array}{l} n \\ k \end{array}\right) {x}^{k} \). This invites us to integrate the binomial theorem applied to \( {\left( 1 + x\right) }^{n} \). We write

\[
{\int }_{0}^{1}{\left( 1 + x\right) }^{n}{dx} = {\int }_{0}^{1}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {x}^{k}}\right) {dx} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {\int }_{0}^{1}{x}^{k}{dx} = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{1}{k + 1}\left( \begin{array}{l} n \\  k \end{array}\right) .
\]

En calculant la valeur de la première intégrale, on en déduit \( {E}_{3} = \left( {{2}^{n + 1} - 1}\right) /\left( {n + 1}\right) \) .

> By calculating the value of the first integral, we deduce \( {E}_{3} = \left( {{2}^{n + 1} - 1}\right) /\left( {n + 1}\right) \) .

(4) Au lieu d'intégrer, comme dans l'expression précédente, on va dériver plusieurs fois l'expression \( f\left( x\right) = {\left( 1 + x\right) }^{n} \) appliquée à la formule du binôme, sur la base de l’observation que pour \( {f}_{k}\left( x\right) = {x}^{k} \) , on a \( x{f}_{k}^{\prime }\left( x\right) + {x}^{2}{f}_{k}^{\prime \prime }\left( x\right) = {k}^{2}{x}^{k} \) . On écrit

> (4) Instead of integrating, as in the previous expression, we will differentiate the expression \( f\left( x\right) = {\left( 1 + x\right) }^{n} \) applied to the binomial formula several times, based on the observation that for \( {f}_{k}\left( x\right) = {x}^{k} \) , we have \( x{f}_{k}^{\prime }\left( x\right) + {x}^{2}{f}_{k}^{\prime \prime }\left( x\right) = {k}^{2}{x}^{k} \) . We write

\[
x{f}^{\prime }\left( x\right)  + {x}^{2}{f}^{\prime \prime }\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) k{x}^{k} + \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) k\left( {k - 1}\right) {x}^{k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {k}^{2}{x}^{k}.
\]

En donnant à \( x \) la valeur 1 dans la dernière expression on trouve l’expression \( {E}_{4} \) . En faisant \( x = 1 \) dans le membre de gauche on en déduit \( {E}_{4} = {f}^{\prime }\left( 1\right) + {f}^{\prime \prime }\left( 1\right) = n{2}^{n - 1} + n\left( {n - 1}\right) {2}^{n - 2} = n\left( {n + 1}\right) {2}^{n - 2} \) . (5) L'idée est de repartir du principe de la preuve de la formule de Vandermonde, mais en considérant la dérivée de \( f\left( x\right) = {\left( 1 + x\right) }^{n} \) pour le premier terme du produit. L’expression \( {E}_{5} \) s’écrit \( {E}_{5} = \mathop{\sum }\limits_{{k = 0}}^{n}k\left( \begin{array}{l} n \\ k \end{array}\right) \times \left( \begin{matrix} n \\ n - k \end{matrix}\right) \) , c’est donc le coefficient de \( {x}^{n} \) dans le produit \( A\left( x\right) B\left( x\right) \) , où

> By setting \( x \) to the value 1 in the last expression, we find the expression \( {E}_{4} \) . By setting \( x = 1 \) in the left-hand side, we deduce \( {E}_{4} = {f}^{\prime }\left( 1\right) + {f}^{\prime \prime }\left( 1\right) = n{2}^{n - 1} + n\left( {n - 1}\right) {2}^{n - 2} = n\left( {n + 1}\right) {2}^{n - 2} \) . (5) The idea is to start again from the principle of the proof of Vandermonde's identity, but by considering the derivative of \( f\left( x\right) = {\left( 1 + x\right) }^{n} \) for the first term of the product. The expression \( {E}_{5} \) is written as \( {E}_{5} = \mathop{\sum }\limits_{{k = 0}}^{n}k\left( \begin{array}{l} n \\ k \end{array}\right) \times \left( \begin{matrix} n \\ n - k \end{matrix}\right) \) , it is therefore the coefficient of \( {x}^{n} \) in the product \( A\left( x\right) B\left( x\right) \) , where

\[
A\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}k\left( \begin{array}{l} n \\  k \end{array}\right) {x}^{k},\;B\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {x}^{k}.
\]

La formule du binôme donne \( B\left( x\right) = {\left( 1 + x\right) }^{n} \) , et \( A\left( x\right) = x{B}^{\prime }\left( x\right) = {nx}{\left( 1 + x\right) }^{n - 1} \) , on a donc \( A\left( x\right) B\left( x\right) = {nx}{\left( 1 + x\right) }^{{2n} - 1} \) . La formule du binôme appliquée à \( {\left( 1 + x\right) }^{{2n} - 1} \) montre que le coefficient de \( {x}^{n} \) dans \( A\left( x\right) B\left( x\right) \) est \( n\left( \begin{matrix} {2n} - 1 \\ n - 1 \end{matrix}\right) \) . On en déduit donc \( {E}_{5} = n\left( \begin{matrix} {2n} - 1 \\ n - 1 \end{matrix}\right) \) .

> The binomial formula gives \( B\left( x\right) = {\left( 1 + x\right) }^{n} \) , and \( A\left( x\right) = x{B}^{\prime }\left( x\right) = {nx}{\left( 1 + x\right) }^{n - 1} \) , we therefore have \( A\left( x\right) B\left( x\right) = {nx}{\left( 1 + x\right) }^{{2n} - 1} \) . The binomial formula applied to \( {\left( 1 + x\right) }^{{2n} - 1} \) shows that the coefficient of \( {x}^{n} \) in \( A\left( x\right) B\left( x\right) \) is \( n\left( \begin{matrix} {2n} - 1 \\ n - 1 \end{matrix}\right) \) . We therefore deduce \( {E}_{5} = n\left( \begin{matrix} {2n} - 1 \\ n - 1 \end{matrix}\right) \) .

2/a) L’idée est de calculer le coefficient de \( {x}^{n} \) dans \( p\left( x\right) = {\left( 1 + x\right) }^{n}{\left( -1 + \left( 1 + x\right) \right) }^{n} \) de deux manières différentes. Comme \( p\left( x\right) = {\left( 1 + x\right) }^{n}{x}^{n} \) , le coefficient de \( {x}^{n} \) dans \( p\left( x\right) \) est égal à 1. Par ailleurs, l’application de la formule du binôme à \( {\left( -1 + \left( 1 + x\right) \right) }^{n} \) , donne

> 2/a) The idea is to calculate the coefficient of \( {x}^{n} \) in \( p\left( x\right) = {\left( 1 + x\right) }^{n}{\left( -1 + \left( 1 + x\right) \right) }^{n} \) in two different ways. Since \( p\left( x\right) = {\left( 1 + x\right) }^{n}{x}^{n} \) , the coefficient of \( {x}^{n} \) in \( p\left( x\right) \) is equal to 1. Furthermore, applying the binomial theorem to \( {\left( -1 + \left( 1 + x\right) \right) }^{n} \) , gives

\[
{\left( -1 + \left( 1 + x\right) \right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {\left( -1\right) }^{k}{\left( 1 + x\right) }^{n - k}\;\text{ donc }\;p\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {\left( -1\right) }^{k}{\left( 1 + x\right) }^{{2n} - k}.
\]

\( \left( {* * }\right) \)

> La formule du binôme montre que le coefficient de \( {x}^{n} \) dans \( {\left( 1 + x\right) }^{{2n} - k} \) est égal à \( \left( \begin{matrix} {2n} - k \\ n \end{matrix}\right) \) . Par linéarité à partir de la dernière égalité de (**), on en déduit que le coefficient de \( {x}^{n} \) dans \( p\left( x\right) \) est égal à \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\ k \end{array}\right) \left( \begin{matrix} {2n} - k \\ n \end{matrix}\right) \) . Nous avons montré plus haut que le coefficient de \( {x}^{n} \) dans \( p\left( x\right) \) est aussi égal à 1, on en déduit le résultat.

The binomial theorem shows that the coefficient of \( {x}^{n} \) in \( {\left( 1 + x\right) }^{{2n} - k} \) is equal to \( \left( \begin{matrix} {2n} - k \\ n \end{matrix}\right) \) . By linearity from the last equality of (**), we deduce that the coefficient of \( {x}^{n} \) in \( p\left( x\right) \) is equal to \( \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\ k \end{array}\right) \left( \begin{matrix} {2n} - k \\ n \end{matrix}\right) \) . We showed above that the coefficient of \( {x}^{n} \) in \( p\left( x\right) \) is also equal to 1, from which we deduce the result.

> b) Notons \( E \) la somme à gauche dans l’identité de la question 2/b). On va montrer \( \left( \begin{matrix} {2n} \\ n \end{matrix}\right) E = 1 \) . Pour cela, on remarque que pour tout \( k \) on a

b) Let \( E \) be the sum on the left in the identity of question 2/b). We will show \( \left( \begin{matrix} {2n} \\ n \end{matrix}\right) E = 1 \) . To do this, we note that for all \( k \) we have

\[
\left( \begin{array}{l} n \\  k \end{array}\right) {\left( \begin{matrix} {2n} \\  k \end{matrix}\right) }^{-1}\left( \begin{matrix} {2n} \\  n \end{matrix}\right)  = \frac{n!}{k!\left( {n - k}\right) !}\frac{k!\left( {{2n} - k}\right) !}{\left( {2n}\right) !}\frac{\left( {2n}\right) !}{{\left( n!\right) }^{2}} = \frac{\left( {{2n} - k}\right) !}{\left( {n - k}\right) !n!} = \left( \begin{matrix} {2n} - k \\  n \end{matrix}\right) .
\]

On a donc

> We therefore have

\[
\left( \begin{matrix} {2n} \\  n \end{matrix}\right) E = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\  k \end{array}\right)  \times  \left( \begin{array}{l} n \\  k \end{array}\right) {\left( \begin{matrix} {2n} \\  k \end{matrix}\right) }^{-1}\left( \begin{matrix} {2n} \\  n \end{matrix}\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{\left( -1\right) }^{k}\left( \begin{array}{l} n \\  k \end{array}\right) \left( \begin{matrix} {2n} - k \\  n \end{matrix}\right)  = 1,
\]

où la dernière égalité provient de l'identité de la question précédente.

> where the last equality comes from the identity of the previous question.

EXERCICE 7 (COMBINATOIRE ET NOMBRES DE FIBONACCI). 1/ Donner une forme explicite des termes de la suite de Fibonacci \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) définie par

> EXERCISE 7 (COMBINATORICS AND FIBONACCI NUMBERS). 1/ Give an explicit form for the terms of the Fibonacci sequence \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) defined by

\[
{F}_{0} = {F}_{1} = 1;\;\forall n \geq  2,\;{F}_{n} = {F}_{n - 1} + {F}_{n - 2}.
\]

2/ Soit \( n \in {\mathbb{N}}^{ * } \) . a) On note \( {\mathcal{A}}_{n} \) l’ensemble des listes de \( \{ 1,2\} \) dont la somme des termes vaut \( n \) (de manière équivalente, c’est l’ensemble des manières d’écrire \( n \) comme la somme de 1 et de 2). Montrer que \( \left| {\mathcal{A}}_{n}\right| = {F}_{n} \) .

> 2/ Let \( n \in {\mathbb{N}}^{ * } \) . a) Let \( {\mathcal{A}}_{n} \) be the set of lists of \( \{ 1,2\} \) whose terms sum to \( n \) (equivalently, this is the set of ways to write \( n \) as a sum of 1s and 2s). Show that \( \left| {\mathcal{A}}_{n}\right| = {F}_{n} \) .

b) On note \( {\mathcal{B}}_{n} \) l’ensemble des parties de \( \{ 1,\ldots , n\} \) sans entiers consécutifs. Montrer \( \left| {\mathcal{B}}_{n}\right| = {F}_{n + 1} \) , en établissant une bijection entre \( {\mathcal{B}}_{n} \) et \( {\mathcal{A}}_{n + 1} \) .

> b) Let \( {\mathcal{B}}_{n} \) be the set of subsets of \( \{ 1,\ldots , n\} \) with no consecutive integers. Show \( \left| {\mathcal{B}}_{n}\right| = {F}_{n + 1} \) , by establishing a bijection between \( {\mathcal{B}}_{n} \) and \( {\mathcal{A}}_{n + 1} \) .

c) Montrer que

> c) Show that

\[
\mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }\left( \begin{matrix} n - k \\  k \end{matrix}\right)  = {F}_{n}
\]

(*)

> Solution. 1/ C'est hyper classique. On a affaire à une récurrence linéaire d'ordre 2 (voir le tome analyse, dans la section sur les suites), dont l’équation caractéristique est \( {x}^{2} - x - 1 \) . Elle a deux racines, \( \varphi = \left( {1 + \sqrt{5}}\right) /2 \) et \( \psi = \left( {1 - \sqrt{5}}\right) /2 \) (notons que \( \psi = - 1/\varphi \) ). Ainsi on sait qu’il existe deux coefficients \( a \) et \( b \) tels que \( {F}_{n} = a{\varphi }^{n} + b{\psi }^{n} \) . Les cas \( n = 0 \) et \( n = 1 \) donnent \( 1 = a + b \) et \( 1 = {a\varphi } + {b\psi } \) d’où on déduit \( a = \varphi /\sqrt{5} \) et \( b = - \psi /\sqrt{5} \) . On a donc

Solution. 1/ This is a classic. We are dealing with a second-order linear recurrence (see the analysis volume, in the section on sequences), whose characteristic equation is \( {x}^{2} - x - 1 \). It has two roots, \( \varphi = \left( {1 + \sqrt{5}}\right) /2 \) and \( \psi = \left( {1 - \sqrt{5}}\right) /2 \) (note that \( \psi = - 1/\varphi \)). Thus, we know there exist two coefficients \( a \) and \( b \) such that \( {F}_{n} = a{\varphi }^{n} + b{\psi }^{n} \). The cases \( n = 0 \) and \( n = 1 \) give \( 1 = a + b \) and \( 1 = {a\varphi } + {b\psi } \), from which we deduce \( a = \varphi /\sqrt{5} \) and \( b = - \psi /\sqrt{5} \). We therefore have

\[
\forall n \in  \mathbb{N},\;{F}_{n} = \frac{{\varphi }^{n + 1} - {\psi }^{n + 1}}{\sqrt{5}} = \frac{1}{\sqrt{5}}\left( {{\left( \frac{1 + \sqrt{5}}{2}\right) }^{n + 1} - {\left( \frac{1 - \sqrt{5}}{2}\right) }^{n + 1}}\right)
\]

2/ a) On vérifie facilement \( \left| {\mathcal{A}}_{1}\right| = 1 \) et \( \left| {\mathcal{A}}_{2}\right| = 2 \) , donc la propriété est vraie pour \( n \leq 2 \) . Supposons maintenant \( n \geq 3 \) . L’ensemble \( {\mathcal{A}}_{n} \) se partitionne en deux ensemble \( {E}_{1} \) et \( {E}_{2} \) , où \( {E}_{k} \) est l’ensemble des listes de \( {\mathcal{A}}_{n} \) dont le dernier terme est \( k \) (pour \( k = 1,2 \) ). Les éléments de \( {E}_{k} \) sont de la forme \( x = \left( {y, k}\right) \) où \( y \) est une liste dans \( {\mathcal{A}}_{n - k} \) . Donc \( \left| {E}_{k}\right| = \left| {\mathcal{A}}_{n - k}\right| \) . On en déduit

> 2/ a) We easily verify \( \left| {\mathcal{A}}_{1}\right| = 1 \) and \( \left| {\mathcal{A}}_{2}\right| = 2 \), so the property is true for \( n \leq 2 \). Now assume \( n \geq 3 \). The set \( {\mathcal{A}}_{n} \) is partitioned into two sets \( {E}_{1} \) and \( {E}_{2} \), where \( {E}_{k} \) is the set of lists of \( {\mathcal{A}}_{n} \) whose last term is \( k \) (for \( k = 1,2 \)). The elements of \( {E}_{k} \) are of the form \( x = \left( {y, k}\right) \) where \( y \) is a list in \( {\mathcal{A}}_{n - k} \). Thus \( \left| {E}_{k}\right| = \left| {\mathcal{A}}_{n - k}\right| \). We deduce from this

\[
\left| {\mathcal{A}}_{n}\right|  = \left| {E}_{1}\right|  + \left| {E}_{2}\right|  = \left| {\mathcal{A}}_{n - 1}\right|  + \left| {\mathcal{A}}_{n - 2}\right| .
\]

Ainsi \( \left| {\mathcal{A}}_{n}\right| \) vérifie la même récurrence que la suite de Fibonacci. En procédant par récurrence sur \( n \) , on va montrer que \( \left| {\mathcal{A}}_{n}\right| = {F}_{n} \) . Comme on l’a vu plus haut c’est déjà vrai pour \( n = 1 \) et \( n = 2 \) . Si \( n \geq 3 \) , l’hypothèse de récurrence entraîne \( \left| {\mathcal{A}}_{n}\right| = \left| {\mathcal{A}}_{n - 1}\right| + \left| {\mathcal{A}}_{n - 2}\right| = {F}_{n - 1} + {F}_{n - 2} = {F}_{n} \) .

> Thus \( \left| {\mathcal{A}}_{n}\right| \) satisfies the same recurrence as the Fibonacci sequence. By proceeding by induction on \( n \), we will show that \( \left| {\mathcal{A}}_{n}\right| = {F}_{n} \). As seen above, this is already true for \( n = 1 \) and \( n = 2 \). If \( n \geq 3 \), the induction hypothesis implies \( \left| {\mathcal{A}}_{n}\right| = \left| {\mathcal{A}}_{n - 1}\right| + \left| {\mathcal{A}}_{n - 2}\right| = {F}_{n - 1} + {F}_{n - 2} = {F}_{n} \).

b) Å toute liste \( x = \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) de \( {\mathcal{A}}_{n + 1} \) , on associe la partie \( \varphi \left( x\right) = \left\{ {{s}_{k} - 1 \mid {x}_{k} = 2}\right\} \) de \( \{ 1,\ldots , n\} \) , où \( {s}_{k} = {x}_{1} + \cdots + {x}_{k} \) . Autrement dit, en regardant la liste \( x \) comme un pavage du rectangle \( \left( {n + 1}\right) \times 1 \) par des rectangles \( 1 \times 1 \) ou \( 2 \times 1,\varphi \left( x\right) \) est constitué des entiers qui correspondent aux premières cases des rectangles \( 2 \times 1 \) (voir la figure ci-dessous). Il est clair que \( \varphi \left( x\right) \) est une partie de \( \{ 1,\ldots , n\} \) , elle ne contient pas d’entiers consécutifs car pour deux entiers distincts \( a = {s}_{k} - 1 \) et \( b = {s}_{\ell } - 1 \) (avec \( k < \ell \) ), on a \( b - a \geq {x}_{\ell } \geq 2 \) . L’application \( \varphi \) est bien injective. Elle est surjective. En effet, considérons une partie \( y = \left\{ {{y}_{1},\ldots ,{y}_{p}}\right\} \) dans \( {\mathcal{B}}_{n} \) avec \( {y}_{1} < \ldots < {y}_{p} \) . Comme \( y \in {\mathcal{B}}_{n} \) on a \( {\delta }_{k} = {y}_{k + 1} - {y}_{k} \geq 2 \) pour \( k = 1,\ldots , p - 1 \) . On crée un pavage

> b) To every list \( x = \left( {{x}_{1},\ldots ,{x}_{p}}\right) \) of \( {\mathcal{A}}_{n + 1} \), we associate the subset \( \varphi \left( x\right) = \left\{ {{s}_{k} - 1 \mid {x}_{k} = 2}\right\} \) of \( \{ 1,\ldots , n\} \), where \( {s}_{k} = {x}_{1} + \cdots + {x}_{k} \). In other words, by viewing the list \( x \) as a tiling of the rectangle \( \left( {n + 1}\right) \times 1 \) by rectangles \( 1 \times 1 \) or \( 2 \times 1,\varphi \left( x\right) \) consisting of the integers corresponding to the first cells of the rectangles \( 2 \times 1 \) (see the figure below). It is clear that \( \varphi \left( x\right) \) is a subset of \( \{ 1,\ldots , n\} \); it contains no consecutive integers because for two distinct integers \( a = {s}_{k} - 1 \) and \( b = {s}_{\ell } - 1 \) (with \( k < \ell \)), we have \( b - a \geq {x}_{\ell } \geq 2 \). The mapping \( \varphi \) is indeed injective. It is surjective. Indeed, let us consider a subset \( y = \left\{ {{y}_{1},\ldots ,{y}_{p}}\right\} \) in \( {\mathcal{B}}_{n} \) with \( {y}_{1} < \ldots < {y}_{p} \). As \( y \in {\mathcal{B}}_{n} \), we have \( {\delta }_{k} = {y}_{k + 1} - {y}_{k} \geq 2 \) for \( k = 1,\ldots , p - 1 \). We create a tiling

![bo_d7fjffs91nqc73erehlg_312_455_206_623_117_0.jpg](images/gourdon_algebra_probabilities_fr_en_012_bod7fjffs91nqc73erehlg3124552066231170.jpg)

Figure 1. Illustration dans le cas \( n = {10} \) , d’un pavage du rectangle \( {11} \times 1 \) par des rectangles \( 1 \times 1 \) et \( 2 \times 1 \) . Les premières cases des rectangles \( 2 \times 1 \) forment une partie de \( \{ 1,\ldots ,{10}\} \) sans entiers consécutifs.

> Figure 1. Illustration in the case \( n = {10} \) of a tiling of the rectangle \( {11} \times 1 \) by rectangles \( 1 \times 1 \) and \( 2 \times 1 \). The first cells of the rectangles \( 2 \times 1 \) form a subset of \( \{ 1,\ldots ,{10}\} \) with no consecutive integers.

du rectangle \( \left( {n + 1}\right) \times 1 \) du type de celui discuté plus haut, en mettant un rectangle \( 2 \times 1 \) sur chaque couple de cases \( \left( {{y}_{k},{y}_{k} + 1}\right) \) , puis des carrés \( 1 \times 1 \) sur les cases restantes. Autrement dit, on considère la liste \( x = \left( {{1}^{{y}_{1} - 1},2,{1}^{{\delta }_{1} - 2},2,\ldots ,2,{1}^{{\delta }_{p - 1} - 2},2,{1}^{n - {y}_{p}}}\right) \) où la notation \( {1}^{k} \) désigne une suite de \( k \) " 1 " consécutifs (vide si \( k = 0 \) ). On a bien \( x \in {\mathcal{A}}_{n + 1} \) car la somme de ses termes est

> of the rectangle \( \left( {n + 1}\right) \times 1 \) of the type discussed above, by placing a rectangle \( 2 \times 1 \) on each pair of cells \( \left( {{y}_{k},{y}_{k} + 1}\right) \), then squares \( 1 \times 1 \) on the remaining cells. In other words, we consider the list \( x = \left( {{1}^{{y}_{1} - 1},2,{1}^{{\delta }_{1} - 2},2,\ldots ,2,{1}^{{\delta }_{p - 1} - 2},2,{1}^{n - {y}_{p}}}\right) \) where the notation \( {1}^{k} \) denotes a sequence of \( k \) consecutive "1"s (empty if \( k = 0 \)). We indeed have \( x \in {\mathcal{A}}_{n + 1} \) because the sum of its terms is

\( \left( {{y}_{1} - 1}\right) + 2 + \left( {{\delta }_{1} - 2}\right) + 2 + \cdots + \left( {{\delta }_{p - 1} - 2}\right) + 2 + n - {y}_{p} = {y}_{1} + 1 + {\delta }_{1} + \cdots + {\delta }_{p - 1} + n - {y}_{p} = n + 1 \) . On a bien \( \varphi \left( x\right) = y \) car lorsque \( {x}_{k} = 2 \) , la valeur \( {s}_{k} - 1 \) vaut \( \left( {{y}_{1} - 1}\right) + 2 + \left( {{\delta }_{1} - 2}\right) + 2 + \cdots + \; \left( {{\delta }_{k - 1} - 2}\right) + 2 = {y}_{k} \) . Ainsi \( \varphi \) est bien une bijection de \( {\mathcal{A}}_{n + 1} \) vers \( {\mathcal{B}}_{n} \) , donc \( \left| {\mathcal{B}}_{n}\right| = {F}_{n + 1} \) .

> \( \left( {{y}_{1} - 1}\right) + 2 + \left( {{\delta }_{1} - 2}\right) + 2 + \cdots + \left( {{\delta }_{p - 1} - 2}\right) + 2 + n - {y}_{p} = {y}_{1} + 1 + {\delta }_{1} + \cdots + {\delta }_{p - 1} + n - {y}_{p} = n + 1 \) . We have \( \varphi \left( x\right) = y \) because when \( {x}_{k} = 2 \) , the value \( {s}_{k} - 1 \) is \( \left( {{y}_{1} - 1}\right) + 2 + \left( {{\delta }_{1} - 2}\right) + 2 + \cdots + \; \left( {{\delta }_{k - 1} - 2}\right) + 2 = {y}_{k} \) . Thus \( \varphi \) is indeed a bijection from \( {\mathcal{A}}_{n + 1} \) to \( {\mathcal{B}}_{n} \) , so \( \left| {\mathcal{B}}_{n}\right| = {F}_{n + 1} \) .

c) On peut montrer directement que la somme des binomiaux de (*) vérifie la relation de récur-rence de \( {F}_{n} \) (à partir de la formule de Pascal), mais on va proposer ici une preuve combinatoire. Fixons \( n \in {\mathbb{N}}^{ * } \) . Pour tout \( k \in \mathbb{N} \) , on note \( {E}_{k} \) l’ensemble des listes de \( {\mathcal{A}}_{n} \) dont le nombre de 2 est égal à \( k \) . Comme la somme des termes des listes dans \( {E}_{k} \) est égal à \( n \) , on a \( {2k} \leq n \) . Ainsi, les \( {\left( {E}_{k}\right) }_{0 < k < \left\lbrack {n/2}\right\rbrack } \) forment une partition de \( {\mathcal{A}}_{n} \) . Dans chaque liste de \( {E}_{k} \) , le 2 est utilisé \( k \) fois et le 1 est utilisé \( n - {2k} \) fois. Ainsi les listes dans \( {E}_{k} \) ont \( n - k \) termes. Il y a autant de listes dans \( {E}_{k} \) que de manière de placer les 2 parmi les \( n - k \) termes, donc \( \left| {E}_{k}\right| = \left( \begin{matrix} n - k \\ k \end{matrix}\right) \) . On en déduit l’identité (*) car les \( {\left( {E}_{k}\right) }_{0 \leq k \leq \left\lbrack {n/2}\right\rbrack } \) forment une partition de \( {\mathcal{A}}_{n} \)

> c) We can show directly that the sum of the binomial coefficients in (*) satisfies the recurrence relation of \( {F}_{n} \) (using Pascal's formula), but we will propose a combinatorial proof here. Let us fix \( n \in {\mathbb{N}}^{ * } \) . For any \( k \in \mathbb{N} \) , let \( {E}_{k} \) be the set of lists of \( {\mathcal{A}}_{n} \) where the number of 2s is equal to \( k \) . Since the sum of the terms of the lists in \( {E}_{k} \) is equal to \( n \) , we have \( {2k} \leq n \) . Thus, the \( {\left( {E}_{k}\right) }_{0 < k < \left\lbrack {n/2}\right\rbrack } \) form a partition of \( {\mathcal{A}}_{n} \) . In each list of \( {E}_{k} \) , the 2 is used \( k \) times and the 1 is used \( n - {2k} \) times. Thus the lists in \( {E}_{k} \) have \( n - k \) terms. There are as many lists in \( {E}_{k} \) as there are ways to place the 2s among the \( n - k \) terms, so \( \left| {E}_{k}\right| = \left( \begin{matrix} n - k \\ k \end{matrix}\right) \) . We deduce the identity (*) because the \( {\left( {E}_{k}\right) }_{0 \leq k \leq \left\lbrack {n/2}\right\rbrack } \) form a partition of \( {\mathcal{A}}_{n} \)

Remarque. Les entiers \( {F}_{n} \) s’appellent les nombres de Fibonacci. Ils possèdent de nom-breuses propriétés. Lorsque \( n \rightarrow \infty \) , le ratio \( {F}_{n + 1}/{F}_{n} \) converge vers \( \varphi = \frac{1 + \sqrt{5}}{2} \) , qu’on appelle nombre d'or.

> Remark. The integers \( {F}_{n} \) are called Fibonacci numbers. They possess many properties. As \( n \rightarrow \infty \) , the ratio \( {F}_{n + 1}/{F}_{n} \) converges to \( \varphi = \frac{1 + \sqrt{5}}{2} \) , which is called the golden ratio.

- Les termes de la somme dans (*) forment une diagonale dans le triangle de Pascal.

> - The terms of the sum in (*) form a diagonal in Pascal's triangle.

EXERCICE 8 (DÉRANGEMENTS). Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {\mathcal{D}}_{n} \) l’ensemble des permutations de \( \{ 1,\ldots , n\} \) sans point fixe (une permutation sans point fixe s’appelle un dérangement). 1 / Calculer directement \( {d}_{n} = \left| {\mathcal{D}}_{n}\right| \) .

> EXERCISE 8 (DERANGEMENTS). Let \( n \in {\mathbb{N}}^{ * } \) . Let \( {\mathcal{D}}_{n} \) be the set of permutations of \( \{ 1,\ldots , n\} \) with no fixed points (a permutation with no fixed points is called a derangement). 1 / Calculate \( {d}_{n} = \left| {\mathcal{D}}_{n}\right| \) directly.

2 / On propose un autre moyen de calculer \( {d}_{n} \) . Etablir l’égalité

> 2 / Another way to calculate \( {d}_{n} \) is proposed. Establish the equality

\[
\forall n \in  {\mathbb{N}}^{ * },\;n! = \mathop{\sum }\limits_{{p = 0}}^{n}\left( \begin{array}{l} n \\  p \end{array}\right) {d}_{p}
\]

et en déduire \( {d}_{n} \) , en utilisant la série génératrice exponentielle \( D\left( z\right) = \mathop{\sum }\limits_{{n \geq 1}}\frac{{d}_{n}}{n!}{z}^{n} \) .

> and deduce \( {d}_{n} \) from it, using the exponential generating function \( D\left( z\right) = \mathop{\sum }\limits_{{n \geq 1}}\frac{{d}_{n}}{n!}{z}^{n} \) .

3/ Montrer que \( {d}_{n} = \left\lbrack {n!/e + 1/2}\right\rbrack \) (où \( \left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) ).

> 3/ Show that \( {d}_{n} = \left\lbrack {n!/e + 1/2}\right\rbrack \) (where \( \left\lbrack x\right\rbrack \) denotes the integer part of \( x \) ).

Solution. 1/ Fixons \( n \in {\mathbb{N}}^{ * } \) et désignons par \( {A}_{k} \) l’ensemble des permutations de \( \{ 1,\ldots , n\} \) qui laisse \( k \) invariant. L’ensemble des dérangements est le complémentaire de \( { \cup }_{1 \leq i \leq n}{A}_{i} \) . Pour calculer le cardinal de ce dernier ensemble, on utilise la formule du crible de Poincaré, qui donne

> Solution. 1/ Let us fix \( n \in {\mathbb{N}}^{ * } \) and denote by \( {A}_{k} \) the set of permutations of \( \{ 1,\ldots , n\} \) that leave \( k \) invariant. The set of derangements is the complement of \( { \cup }_{1 \leq i \leq n}{A}_{i} \) . To calculate the cardinality of the latter set, we use the Poincaré inclusion-exclusion principle, which gives

\[
\left| {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right|  = \mathop{\sum }\limits_{{k = 1}}^{n}{\left( -1\right) }^{k - 1}{S}_{k},\;{S}_{k} = \mathop{\sum }\limits_{{1 \leq  {i}_{1} < \ldots  < {i}_{k} \leq  n}}\left| {{A}_{{i}_{1}} \cap  \ldots  \cap  {A}_{{i}_{k}}}\right| .
\]

Or pour \( 1 \leq {i}_{1} < \ldots < {i}_{k} \leq n,{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}} \) est l’ensemble des permutations qui laissent \( {i}_{1},\ldots ,{i}_{k} \) invariants, il y a donc \( \left( {n - k}\right) \) ! permutations de ce type. Donc \( \left| {{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}}}\right| = \left( {n - k}\right) \) !. Par ailleurs, il y a \( \left( \begin{array}{l} n \\ k \end{array}\right) \) façons d’avoir des indices \( {i}_{1},\ldots ,{i}_{k} \) tels que \( 1 \leq {i}_{1} < \ldots < {i}_{k} \leq n \) . Donc \( {S}_{k} = \left( \begin{array}{l} n \\ k \end{array}\right) \left( {n - k}\right) ! = \frac{n!}{k!} \) . D’après la formule précédente on en déduit

> However, for \( 1 \leq {i}_{1} < \ldots < {i}_{k} \leq n,{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}} \) is the set of permutations that leave \( {i}_{1},\ldots ,{i}_{k} \) invariant, there are therefore \( \left( {n - k}\right) \) ! permutations of this type. Thus \( \left| {{A}_{{i}_{1}} \cap \ldots \cap {A}_{{i}_{k}}}\right| = \left( {n - k}\right) \) !. Furthermore, there are \( \left( \begin{array}{l} n \\ k \end{array}\right) \) ways to have indices \( {i}_{1},\ldots ,{i}_{k} \) such that \( 1 \leq {i}_{1} < \ldots < {i}_{k} \leq n \) . Thus \( {S}_{k} = \left( \begin{array}{l} n \\ k \end{array}\right) \left( {n - k}\right) ! = \frac{n!}{k!} \) . From the previous formula, we deduce

\[
{d}_{n} = \left| {\mathcal{D}}_{n}\right|  = n! - \left| {\mathop{\bigcup }\limits_{{i = 1}}^{n}{A}_{i}}\right|  = n!\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( -1\right) }^{k}}{k!}.
\]

(*)

> 2 / Fixons \( n \in {\mathbb{N}}^{ * } \) et désignons par \( {\mathcal{F}}_{k} \) l’ensemble des permutations de \( \{ 1,\ldots , n\} \) qui ont \( k \) points fixes. Les \( {\left( {\mathcal{F}}_{k}\right) }_{0 \leq k \leq n} \) forment une partition de l’ensemble des permutations de \( \{ 1,\ldots , n\} \) . Choisir une permutation dans \( {\mathcal{F}}_{k} \) revient à choisir une partie \( P \) de \( n - k \) entiers parmi \( \{ 1,\ldots , n\} \) puis à choisir une permutation sans point fixe de \( P \) (et laisser les \( k \) autres points fixes). On en déduit \( \left| {\mathcal{F}}_{k}\right| = \left( \begin{matrix} n \\ n - k \end{matrix}\right) {d}_{n - k} \) . On a donc

2 / Let us fix \( n \in {\mathbb{N}}^{ * } \) and denote by \( {\mathcal{F}}_{k} \) the set of permutations of \( \{ 1,\ldots , n\} \) that have \( k \) fixed points. The \( {\left( {\mathcal{F}}_{k}\right) }_{0 \leq k \leq n} \) form a partition of the set of permutations of \( \{ 1,\ldots , n\} \) . Choosing a permutation in \( {\mathcal{F}}_{k} \) amounts to choosing a subset \( P \) of \( n - k \) integers from \( \{ 1,\ldots , n\} \) and then choosing a permutation without fixed points of \( P \) (and leaving the \( k \) other points fixed). We deduce \( \left| {\mathcal{F}}_{k}\right| = \left( \begin{matrix} n \\ n - k \end{matrix}\right) {d}_{n - k} \) . We therefore have

\[
n! = \left| {\mathcal{S}}_{n}\right|  = \mathop{\sum }\limits_{{k = 0}}^{n}\left| {\mathcal{F}}_{k}\right|  = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{matrix} n \\  n - k \end{matrix}\right) {d}_{n - k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {d}_{k}.
\]

Ceci s'écrit aussi

> This can also be written as

\[
1 = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{d}_{k}}{k!}\frac{1}{\left( {n - k}\right) !}
\]

La série génératrice exponentielle \( D\left( z\right) = \mathop{\sum }\limits_{{n > 1}}\frac{{d}_{n}}{n!}{z}^{n} \) a un rayon de convergence \( \geq 1 \) puisque \( \left| {{d}_{n}/n!}\right| < 1 \) . L’égalité précédente entraîne, par produit de Cauchy, pour \( \left| z\right| < 1 \)

> The exponential generating function \( D\left( z\right) = \mathop{\sum }\limits_{{n > 1}}\frac{{d}_{n}}{n!}{z}^{n} \) has a radius of convergence \( \geq 1 \) since \( \left| {{d}_{n}/n!}\right| < 1 \) . The previous equality implies, by Cauchy product, for \( \left| z\right| < 1 \)

\[
D\left( z\right) \exp \left( z\right)  = \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{d}_{n}}{n!}{z}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{n!}{z}^{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{d}_{k}}{k!}\frac{1}{\left( {n - k}\right) !}}\right) {z}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{z}^{n}.
\]

Donc

> Therefore

\[
D\left( z\right)  = \exp \left( {-z}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{z}^{n}}\right)  = \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{n!}{z}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{z}^{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( -1\right) }^{k}}{k!}}\right) {z}^{n}.
\]

Par identification des coefficients de \( D\left( z\right) \) , on retrouve l’expression (*) de \( {d}_{n} \) .

> By identifying the coefficients of \( D\left( z\right) \), we recover the expression (*) of \( {d}_{n} \).

3/ L'expression (*) permet d'écrire

> 3/ The expression (*) allows us to write

\[
\frac{{d}_{n}}{n!} = \exp \left( {-1}\right)  - \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{{\left( -1\right) }^{k}}{k!}
\]

donc

> therefore

\[
\left| {{d}_{n} - \frac{n!}{e}}\right|  \leq  \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{n!}{k!} = \frac{1}{n + 1} + \frac{1}{\left( {n + 1}\right) \left( {n + 2}\right) } + \cdots  < \mathop{\sum }\limits_{{p = 1}}^{{+\infty }}\frac{1}{{\left( n + 1\right) }^{p}} = \frac{1}{n}.
\]

Lorsque \( n \geq 2 \) on en déduit \( {d}_{n} \leq {d}_{n} + 1/2 - 1/n < n!/e + 1/2 < {d}_{n} + 1/2 + 1/n \leq {d}_{n} + 1 \) donc \( {d}_{n} < n!/e + 1/2 < {d}_{n} + 1 \) et on a bien \( {d}_{n} = \left\lbrack {n!/e + 1/2}\right\rbrack \) . Cette formule est également vraie lorsque \( n = 1 \) , d’où le résultat.

> When \( n \geq 2 \), we deduce \( {d}_{n} \leq {d}_{n} + 1/2 - 1/n < n!/e + 1/2 < {d}_{n} + 1/2 + 1/n \leq {d}_{n} + 1 \), therefore \( {d}_{n} < n!/e + 1/2 < {d}_{n} + 1 \), and we indeed have \( {d}_{n} = \left\lbrack {n!/e + 1/2}\right\rbrack \). This formula is also true when \( n = 1 \), hence the result.

Remarque. On a ici répondu au célébre problème des chapeaux : \( n \) personnes laissent leur chapeau à un vestiaire. En repartant, chaque personne reprend un chapeau au hasard. Quelle est la probabilité qu'aucune personne ne reprenne son propre chapeau? Cette probabilité est égale à \( 1/e \) (à une erreur \( < 1/n \) ! près).

> Remark. We have here answered the famous hat-check problem: \( n \) people leave their hats at a cloakroom. Upon leaving, each person takes a hat at random. What is the probability that no person takes their own hat? This probability is equal to \( 1/e \) (up to an error of \( < 1/n \)!).

- Les dérangements sont un cas particulier des permutations dont les cycles sont tous de longueur \( > k \) ,étudiés dans le problème 3 page 369.

> - Derangements are a special case of permutations whose cycles are all of length \( > k \), studied in problem 3 on page 369.

EXERCICE 9 (NOMBRES DE BELL). Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {B}_{n} \) le nombre de partitions de l’ensemble \( \{ 1,\ldots , n\} \) . Par convention on pose \( {B}_{0} = 1 \) .

> EXERCISE 9 (BELL NUMBERS). For all \( n \in {\mathbb{N}}^{ * } \), we denote by \( {B}_{n} \) the number of partitions of the set \( \{ 1,\ldots , n\} \). By convention, we set \( {B}_{0} = 1 \).

1/ Déterminer \( {B}_{1} \) , puis une relation de récurrence sur les \( {B}_{n} \) .

> 1/ Determine \( {B}_{1} \), then a recurrence relation for the \( {B}_{n} \).

2/ On définit la série génératrice exponentielle des \( {B}_{n} \) par \( B\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}}{n!}{z}^{n} \) . Montrer que le rayon de convergence de \( B\left( z\right) \) n’est pas nul, puis calculer \( B\left( z\right) \) . 3/ En déduire une expression de \( {B}_{n} \) comme la somme d’une série.

> 2/ We define the exponential generating series of \( {B}_{n} \) by \( B\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}}{n!}{z}^{n} \). Show that the radius of convergence of \( B\left( z\right) \) is non-zero, then calculate \( B\left( z\right) \). 3/ Deduce an expression for \( {B}_{n} \) as the sum of a series.

Solution. 1/ On a \( {B}_{1} = 1 \) . Supposons \( n \in {\mathbb{N}}^{ * } \) et exprimons \( {B}_{n + 1} \) en fonction des \( {\left( {B}_{k}\right) }_{0 < k < n} \) . Pour tout \( k \leq n \) , on note \( {E}_{k} \) l’ensemble des partitions \( P \) de \( \{ 1,\ldots , n + 1\} \) tel que la partie de \( P \) qui contient \( n + 1 \) est de taille \( k + 1 \) . Choisir \( P \in {E}_{k} \) , c’est choisir \( k \) entiers de \( \{ 1,\ldots , n\} \) (ceux de la partition de \( P \) qui contient \( n + 1 \) ) puis construire une partition des \( n - k \) éléments restants. Donc \( \left| {E}_{k}\right| = \left( \begin{array}{l} n \\ k \end{array}\right) {B}_{n - k} \) . Comme les \( {\left( {E}_{k}\right) }_{0 \leq k \leq n} \) forment une partition de l’ensemble des partitions de \( \{ 1,\ldots , n + 1\} \) , on en déduit

> Solution. 1/ We have \( {B}_{1} = 1 \). Suppose \( n \in {\mathbb{N}}^{ * } \) and express \( {B}_{n + 1} \) in terms of \( {\left( {B}_{k}\right) }_{0 < k < n} \). For all \( k \leq n \), we denote by \( {E}_{k} \) the set of partitions \( P \) of \( \{ 1,\ldots , n + 1\} \) such that the part of \( P \) containing \( n + 1 \) is of size \( k + 1 \). Choosing \( P \in {E}_{k} \) means choosing \( k \) integers from \( \{ 1,\ldots , n\} \) (those of the partition of \( P \) containing \( n + 1 \)) then constructing a partition of the \( n - k \) remaining elements. Therefore \( \left| {E}_{k}\right| = \left( \begin{array}{l} n \\ k \end{array}\right) {B}_{n - k} \). As the \( {\left( {E}_{k}\right) }_{0 \leq k \leq n} \) form a partition of the set of partitions of \( \{ 1,\ldots , n + 1\} \), we deduce

\[
{B}_{n + 1} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {B}_{n - k} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {B}_{k}.
\]

2/ A toute partition \( P \) de \( \{ 1,\ldots , n\} \) , on peut associer une permutation \( \varphi \left( P\right) \) de \( \{ 1,\ldots , n\} \) qui est le produit des cycles de chaque partition de \( P \) . Ainsi construite, \( \varphi \) est une application injective vers le groupe symétrique \( {\mathcal{S}}_{n} \) , donc \( {B}_{n} \leq n \) ! (on peut aussi retrouver ce résultat par récurrence sur \( n \) avec la formule de récurrence précédente). On en déduit que le rayon de convergence de \( B\left( z\right) \) est \( \geq 1 \) . La relation de récurrence établie précédemment s’interprète en produit de Cauchy, en remarquant que

> 2/ To any partition \( P \) of \( \{ 1,\ldots , n\} \), we can associate a permutation \( \varphi \left( P\right) \) of \( \{ 1,\ldots , n\} \) which is the product of the cycles of each partition of \( P \). Constructed this way, \( \varphi \) is an injective mapping to the symmetric group \( {\mathcal{S}}_{n} \), thus \( {B}_{n} \leq n \)! (this result can also be found by induction on \( n \) using the previous recurrence formula). We deduce that the radius of convergence of \( B\left( z\right) \) is \( \geq 1 \). The recurrence relation established previously can be interpreted as a Cauchy product, by noting that

\[
\frac{{B}_{n + 1}}{n!} = \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{B}_{k}}{k!}\frac{1}{\left( {n - k}\right) !}
\]

qui entraîne, lorsque \( \left| x\right| < 1 \)

> which implies, when \( \left| x\right| < 1 \)

\[
{B}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n + 1}}{n!}{x}^{n} = \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{B}_{n}}{n!}{x}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{n}}{n!}}\right)  = B\left( x\right) \exp \left( x\right) .
\]

Ainsi, la fonction \( B \) vérifie l’équation différentielle \( {B}^{\prime }\left( x\right) = B\left( x\right) {e}^{x} \) sur \( \rbrack 0,1\lbrack \) . On en déduit l’existence de \( \lambda \in \mathbb{R} \) tel que \( B\left( x\right) = \lambda \exp \left( {\exp \left( x\right) }\right) \) . En faisant \( x = 0 \) on a \( 1 = {B}_{0} = B\left( 0\right) = \; \lambda \exp \left( 1\right) \) donc \( \lambda = 1/e \) . Donc finalement \( B\left( x\right) = \exp \left( {\exp \left( x\right) }\right) /e \) .

> Thus, the function \( B \) satisfies the differential equation \( {B}^{\prime }\left( x\right) = B\left( x\right) {e}^{x} \) on \( \rbrack 0,1\lbrack \). We deduce the existence of \( \lambda \in \mathbb{R} \) such that \( B\left( x\right) = \lambda \exp \left( {\exp \left( x\right) }\right) \). By setting \( x = 0 \) we have \( 1 = {B}_{0} = B\left( 0\right) = \; \lambda \exp \left( 1\right) \) therefore \( \lambda = 1/e \). So finally \( B\left( x\right) = \exp \left( {\exp \left( x\right) }\right) /e \).

3 / La série entière définissant l'exponentielle a un rayon de convergence infini. On peut donc écrire, pour tout \( z \in \mathbb{C} \)

> 3/ The power series defining the exponential has an infinite radius of convergence. We can therefore write, for any \( z \in \mathbb{C} \)

\[
\exp \left( {\exp \left( z\right) }\right)  = \mathop{\sum }\limits_{{m = 0}}^{{+\infty }}\frac{{e}^{mz}}{m!} = \mathop{\sum }\limits_{{m = 0}}^{{+\infty }}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( mz\right) }^{n}}{m!n!}.
\]

La série double \( \mathop{\sum }\limits_{{m, n}}{u}_{m, n} \) définie par \( {u}_{m, n} = {\left( mz\right) }^{n}/\left( {m!n!}\right) \) est sommable, car

> The double series \( \mathop{\sum }\limits_{{m, n}}{u}_{m, n} \) defined by \( {u}_{m, n} = {\left( mz\right) }^{n}/\left( {m!n!}\right) \) is summable, because

\[
\forall \left( {M, N}\right)  \in  {\mathbb{N}}^{2},\;\mathop{\sum }\limits_{{m = 0}}^{M}\mathop{\sum }\limits_{{n = 0}}^{N}\left| {u}_{m, n}\right|  \leq  \mathop{\sum }\limits_{{m = 0}}^{M}\mathop{\sum }\limits_{{n = 0}}^{N}\frac{{\left( m\left| z\right| \right) }^{n}}{m!n!} \leq  \mathop{\sum }\limits_{{m = 0}}^{M}\frac{\exp \left( {m\left| z\right| }\right) }{m!} \leq  \exp \left( {\exp \left( \left| z\right| \right) }\right) .
\]

On peut donc intervertir les signes de sommations, ce qui donne

> We can therefore interchange the summation signs, which gives

\[
B\left( z\right)  = \frac{1}{e}\exp \left( {\exp \left( z\right) }\right)  = \frac{1}{e}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{m = 0}}^{{+\infty }}\frac{{m}^{n}}{m!}}\right) \frac{{z}^{n}}{n!}.
\]

Par identification, avec le coefficient \( {B}_{n}/n \) ! de \( {z}^{n} \) dans \( B\left( z\right) \) , on en déduit

> By identification, with the coefficient \( {B}_{n}/n \)! of \( {z}^{n} \) in \( B\left( z\right) \), we deduce

\[
{B}_{n} = \frac{1}{e}\mathop{\sum }\limits_{{m = 0}}^{{+\infty }}\frac{{m}^{n}}{m!}
\]

Remarque. On a \( {B}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}S\left( {n, k}\right) \) , où \( S\left( {n, k}\right) \) est le nombre de Stirling de seconde espèce, qui compte le nombre de partitions de \( \{ 1,\ldots , n\} \) de \( k \) sous-ensembles (voir la remarque du problème 7 page 379).

> Remark. We have \( {B}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}S\left( {n, k}\right) \), where \( S\left( {n, k}\right) \) is the Stirling number of the second kind, which counts the number of partitions of \( \{ 1,\ldots , n\} \) into \( k \) subsets (see the remark in problem 7 on page 379).

EXERCICE 10 (NOMBRES DE CATALAN). On appelle mot binaire une liste de \( \{ 0,1\} \) . Le mot \( w = \left( {{a}_{1},{a}_{2},\ldots ,{a}_{p}}\right) \) est noté \( w = {a}_{1}{a}_{2}\ldots {a}_{p} \) , la longueur de \( w \) est \( p \) . La concaténation de deux mots \( u \) et \( v \) est le mot noté \( {uv} \) , obtenu en mettant bout à bout \( u \) et \( v \) . Un préfixe d’un mot \( w = {a}_{1}\ldots {a}_{p} \) est tout mot de la forme \( {w}^{\prime } = {a}_{1}\ldots {a}_{q} \) avec \( 1 \leq q \leq p \) . Une représentation graphique d’un mot binaire \( w = {a}_{1}\ldots {a}_{p} \) , est obtenue à partir la fonction

> EXERCISE 10 (CATALAN NUMBERS). A binary word is a list of \( \{ 0,1\} \). The word \( w = \left( {{a}_{1},{a}_{2},\ldots ,{a}_{p}}\right) \) is denoted \( w = {a}_{1}{a}_{2}\ldots {a}_{p} \), the length of \( w \) is \( p \). The concatenation of two words \( u \) and \( v \) is the word denoted \( {uv} \), obtained by placing \( u \) and \( v \) end to end. A prefix of a word \( w = {a}_{1}\ldots {a}_{p} \) is any word of the form \( {w}^{\prime } = {a}_{1}\ldots {a}_{q} \) with \( 1 \leq q \leq p \). A graphical representation of a binary word \( w = {a}_{1}\ldots {a}_{p} \) is obtained from the function

\[
{f}_{w} : \{ 0,1,\ldots , p\}  \rightarrow  \mathbb{Z}\;{f}_{w}\left( 0\right)  = 0,\;{f}_{w}\left( k\right)  - {f}_{w}\left( {k - 1}\right)  = \begin{cases} 1 & \text{ si }{a}_{k} = 1 \\   - 1 & \text{ si }{a}_{k} = 0 \end{cases}
\]

puis en construisant la ligne brisée qui relie les points \( \left( {k,{f}_{w}\left( k\right) }\right) \) (voir la figure ci dessous). Un mot binaire \( w \) est un mot de Dyck s’il contient autant de " 0 " que de " 1 ", et si dans tous

> then by constructing the polygonal chain connecting the points \( \left( {k,{f}_{w}\left( k\right) }\right) \) (see the figure below). A binary word \( w \) is a Dyck word if it contains as many "0"s as "1"s, and if in all

![bo_d7fjffs91nqc73erehlg_315_441_802_622_342_0.jpg](images/gourdon_algebra_probabilities_fr_en_014_bod7fjffs91nqc73erehlg3154418026223420.jpg)

FIGURE 2. Exemple de représentation graphique du mot binaire \( w = {1001110111} \) .

> FIGURE 2. Example of a graphical representation of the binary word \( w = {1001110111} \) .

les préfixes de \( w \) il y a toujours moins de " 0 " que de " 1 ". On note \( {\mathcal{D}}_{n} \) l’ensemble des mots de Dyck de longueur \( {2n} \) . Par convention, le mot vide est un mot de Dyck (cas \( n = 0 \) ).

> the prefixes of \( w \) there are always fewer "0"s than "1"s. Let \( {\mathcal{D}}_{n} \) denote the set of Dyck words of length \( {2n} \) . By convention, the empty word is a Dyck word (case \( n = 0 \) ).

1/ Interpréter les mots de Dyck à partir de leur représentation graphique. Déterminer une relation de récurrence sur \( {C}_{n} = \left| {\mathcal{D}}_{n}\right| \) , puis calculer explicitement \( {C}_{n} \) .

> 1/ Interpret Dyck words based on their graphical representation. Determine a recurrence relation for \( {C}_{n} = \left| {\mathcal{D}}_{n}\right| \) , then calculate \( {C}_{n} \) explicitly.

2/ Pour tout mot \( w = {a}_{1}\ldots {a}_{p} \) et pour \( k \in \mathbb{N}\left( {k < p}\right) \) , on note \( {c}^{k}\left( w\right) \) la permutation circulaire \( {c}^{k}\left( w\right) = {a}_{k + 1}\ldots {a}_{p}{a}_{1}\ldots {a}_{k} \) (de même longueur \( p \) que \( w \) ). Montrer que parmi les permutations circulaires de tout mot binaire \( w \) constitué de \( n + 1 \) "1" et \( n \) "0 ", il y en a une et une seule qui s’écrit sous la forme \( w = 1{w}^{\prime } \) , où \( {w}^{\prime } \) est un mot de Dyck. Retrouver ensuite directement l’expression de \( {C}_{n} \) .

> 2/ For any word \( w = {a}_{1}\ldots {a}_{p} \) and for \( k \in \mathbb{N}\left( {k < p}\right) \) , let \( {c}^{k}\left( w\right) \) denote the circular permutation \( {c}^{k}\left( w\right) = {a}_{k + 1}\ldots {a}_{p}{a}_{1}\ldots {a}_{k} \) (of the same length \( p \) as \( w \) ). Show that among the circular permutations of any binary word \( w \) consisting of \( n + 1 \) "1"s and \( n \) "0"s, there is one and only one that can be written in the form \( w = 1{w}^{\prime } \) , where \( {w}^{\prime } \) is a Dyck word. Then directly recover the expression for \( {C}_{n} \) .

Solution. 1 / Avoir autant de " 0 " que de " 1 " dans un mot binaire équivaut à ce que la ligne brisée de sa représentation graphique revient sur l'axe des abscisses. Avoir tout préfixe de ce mot avec plus de "1" que de "0" revient à avoir cette ligne brisée toujours au dessus de l'axe des abscisses. Ainsi les mots de Dyck sont ceux dont la représentation graphique est une ligne brisée toujours au dessus de l'axe des abscisses, qui termine sur l'axe des abscisses (voir la figure ci-dessous). Soit \( n \in {\mathbb{N}}^{ * } \) . Pour obtenir une récurrence sur les \( {C}_{n} \) , on remarque que tout mot \( w \in {\mathcal{D}}_{n} \) s’écrit

> Solution. 1/ Having as many "0"s as "1"s in a binary word is equivalent to the polygonal chain of its graphical representation returning to the x-axis. Having every prefix of this word contain more "1"s than "0"s is equivalent to having this polygonal chain always above the x-axis. Thus, Dyck words are those whose graphical representation is a polygonal chain always above the x-axis, ending on the x-axis (see the figure below). Let \( n \in {\mathbb{N}}^{ * } \) . To obtain a recurrence for the \( {C}_{n} \) , we note that any word \( w \in {\mathcal{D}}_{n} \) can be written

![bo_d7fjffs91nqc73erehlg_315_441_1841_623_199_0.jpg](images/gourdon_algebra_probabilities_fr_en_013_bod7fjffs91nqc73erehlg31544118416231990.jpg)

FIGURE 3. Représentation graphique du mot de Dyck \( w = {1100110100} \) .

> FIGURE 3. Graphical representation of the Dyck word \( w = {1100110100} \) .

de manière unique sous la forme \( w = {1u0v} \) , où \( u \in {\mathcal{D}}_{k} \) et \( v \in {\mathcal{D}}_{n - 1 - k} \) , avec \( k \in \{ 0,\ldots , n - 1\} \) .

> uniquely in the form \( w = {1u0v} \) , where \( u \in {\mathcal{D}}_{k} \) and \( v \in {\mathcal{D}}_{n - 1 - k} \) , with \( k \in \{ 0,\ldots , n - 1\} \) .

On en déduit

> We deduce

\[
{C}_{n} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{C}_{k}{C}_{n - 1 - k}.
\]

On reconnait l'expression de coefficients d'un produit de Cauchy. Ceci nous invite à considérer la série génératrice ordinaire des \( \left( {C}_{n}\right) \) , définie par \( C\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{C}_{n}{z}^{n} \) . Il y a moins de mots dans \( {\mathcal{D}}_{n} \) que de mots binaires de longueur \( {2n} \) , donc \( {C}_{n} \leq {2}^{2n} \) , donc \( C\left( z\right) \) est une série entière de rayon de convergence \( \geq 1/4 \) . Lorsque \( x \in \mathbb{R} \) , avec \( \left| x\right| < 1/4 \) et \( x \neq 0 \) , la relation de récurrence obtenue plus haut permet d'écrire

> We recognize the expression for the coefficients of a Cauchy product. This invites us to consider the ordinary generating function of \( \left( {C}_{n}\right) \), defined by \( C\left( z\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{C}_{n}{z}^{n} \). There are fewer words in \( {\mathcal{D}}_{n} \) than binary words of length \( {2n} \), so \( {C}_{n} \leq {2}^{2n} \), therefore \( C\left( z\right) \) is a power series with radius of convergence \( \geq 1/4 \). When \( x \in \mathbb{R} \), with \( \left| x\right| < 1/4 \) and \( x \neq 0 \), the recurrence relation obtained above allows us to write

\[
{C}^{2}\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{k}{C}_{n - k}}\right) {x}^{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{C}_{n + 1}{x}^{n} = \frac{C\left( x\right)  - 1}{x}.
\]

Ainsi \( C\left( x\right) \) est solution de l’équation du second degré \( x{C}^{2}\left( x\right) - C\left( x\right) + 1 = 0 \) , dont les solutions sont \( {f}_{\varepsilon }\left( x\right) = \frac{1 + \varepsilon \sqrt{1 - {4x}}}{2x} \) avec \( \varepsilon \in \{ - 1,1\} \) . On note que \( \mathop{\lim }\limits_{\substack{{x \rightarrow 0} \\ {x > 0} }}{f}_{1}\left( x\right) = + \infty \) alors que \( C\left( x\right) \) est continue en0, donc \( C\left( x\right) \neq {f}_{1}\left( x\right) \) . On en déduit \( C\left( x\right) = {f}_{-1}\left( x\right) = \frac{1 - \sqrt{1 - {4x}}}{2x} \) . Le developpement en série entière de \( \sqrt{1 + u} = {\left( 1 + u\right) }^{1/2} \) entraîne

> Thus \( C\left( x\right) \) is a solution to the quadratic equation \( x{C}^{2}\left( x\right) - C\left( x\right) + 1 = 0 \), whose solutions are \( {f}_{\varepsilon }\left( x\right) = \frac{1 + \varepsilon \sqrt{1 - {4x}}}{2x} \) with \( \varepsilon \in \{ - 1,1\} \). We note that \( \mathop{\lim }\limits_{\substack{{x \rightarrow 0} \\ {x > 0} }}{f}_{1}\left( x\right) = + \infty \) while \( C\left( x\right) \) is continuous at 0, so \( C\left( x\right) \neq {f}_{1}\left( x\right) \). We deduce \( C\left( x\right) = {f}_{-1}\left( x\right) = \frac{1 - \sqrt{1 - {4x}}}{2x} \). The power series expansion of \( \sqrt{1 + u} = {\left( 1 + u\right) }^{1/2} \) leads to

\[
\sqrt{1 - {4x}} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{\left( -4x\right) }^{n},\;\text{ avec }\;{a}_{n} = \frac{1}{n!}\mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {\frac{1}{2} - k}\right)  = \frac{{\left( -1\right) }^{n - 1}}{2 \cdot  n!}\mathop{\prod }\limits_{{k = 1}}^{{n - 1}}\left( \frac{{2k} - 1}{2}\right) .
\]

On a

> We have

\[
{a}_{n} = \frac{{\left( -1\right) }^{n - 1}}{{2}^{n}n!}\frac{\left( {{2n} - 2}\right) !}{2 \times  4 \times  \cdots  \times  \left( {{2n} - 2}\right) } = \frac{{\left( -1\right) }^{n - 1}}{{2}^{n}n!}\frac{\left( {{2n} - 2}\right) !}{{2}^{n - 1}\left( {n - 1}\right) !} = \frac{{\left( -1\right) }^{n - 1}}{{2}^{{2n} - 1}}\frac{1}{n}\left( \begin{matrix} {2n} - 2 \\  n - 1 \end{matrix}\right) .
\]

On en déduit que le coefficient de \( {x}^{n} \) dans \( \sqrt{1 - {4x}} \) est \( - \frac{2}{n}\left( \begin{matrix} {2n} - 2 \\ n - 1 \end{matrix}\right) \) . Compte tenu de l’expression \( C\left( z\right) = {f}_{-1}\left( x\right) \) , l’identification de coefficients fournit \( {C}_{n} = \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \) .

> We deduce that the coefficient of \( {x}^{n} \) in \( \sqrt{1 - {4x}} \) is \( - \frac{2}{n}\left( \begin{matrix} {2n} - 2 \\ n - 1 \end{matrix}\right) \). Given the expression \( C\left( z\right) = {f}_{-1}\left( x\right) \), identifying the coefficients provides \( {C}_{n} = \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \).

2 / Considérons un mot \( w \) formé de \( n + 1 \) "1 " et \( n \) "0 . On s’aide de la représentation graphique de \( w \) . On obtient les permutations cycliques de \( w \) à partir d’une fenêtre glissante de longueur \( {2n} + 1 \) dans le mot \( w \) concaténé avec lui-même (sans la derniere lettre). Trouver un sous-mot de Dyck de longueur \( {2n} \) , juste après un "1", revient à pouvoir placer sous le graphe une règle horizontale de longueur \( {2n} \) , au dessus de laquelle est posée la représentation de ce sous-mot de Dyck. Comme le suggère la figure ci-dessous, on trouve un mot de Dyck un pas après le dernier minimum atteint par la courbe.

> 2 / Consider a word \( w \) formed of \( n + 1 \) "1"s and \( n \) "0"s. We use the graphical representation of \( w \). We obtain the cyclic permutations of \( w \) from a sliding window of length \( {2n} + 1 \) in the word \( w \) concatenated with itself (without the last letter). Finding a Dyck subword of length \( {2n} \), just after a "1", amounts to being able to place a horizontal ruler of length \( {2n} \) under the graph, above which the representation of this Dyck subword is placed. As the figure below suggests, we find a Dyck word one step after the last minimum reached by the curve.

![bo_d7fjffs91nqc73erehlg_316_442_1593_752_224_0.jpg](images/gourdon_algebra_probabilities_fr_en_015_bod7fjffs91nqc73erehlg31644215937522240.jpg)

FIGURE 4. Représentation de \( w = {1010110} \) , concaténé avec lui-même (en poin-tillé) sans la dernière lettre. Un sous-mot de Dyck de longueur 6 (souligné) précédé d'un pas croissant, se trouve un pas après le dernier moment où la courbe atteint son minimum.

> FIGURE 4. Representation of \( w = {1010110} \), concatenated with itself (dotted) without the last letter. A Dyck subword of length 6 (underlined) preceded by an increasing step, is found one step after the last moment the curve reaches its minimum.

Cette constatation graphique nous invite à considérer l'indice

> This graphical observation invites us to consider the index

\[
\ell  = \max \left\{  {k \leq  {2n} \mid  {f}_{w}\left( k\right)  = m}\right\}  ,\;\text{ où }\;m = \min \left\{  {{f}_{w}\left( 0\right) ,{f}_{w}\left( 1\right) ,\ldots ,{f}_{w}\left( {2n}\right) }\right\}  .
\]

Nous allons montrer que \( {c}^{\ell }\left( w\right) = {1y} \) , où \( y \) est un mot de Dyck, et que \( \ell \in \mathbb{N} \) est le seul indice \( \leq {2n} \) vérifiant cette propriété. Notons \( w = {a}_{1}\ldots {a}_{{2n} + 1} \) .

> We will show that \( {c}^{\ell }\left( w\right) = {1y} \) , where \( y \) is a Dyck word, and that \( \ell \in \mathbb{N} \) is the only index \( \leq {2n} \) satisfying this property. Let us denote \( w = {a}_{1}\ldots {a}_{{2n} + 1} \) .

- La première lettre de \( {c}^{\ell }\left( w\right) \) est " 1 ". En effet, par définition \( \ell \) , on a \( {f}_{w}\left( k\right)  > m = {f}_{w}\left( \ell \right) \) pour \( k > \ell \) , en particulier \( {a}_{\ell  + 1} = {f}_{w}\left( {\ell  + 1}\right)  - {f}_{w}\left( \ell \right)  > 0 \) donc \( {a}_{\ell  + 1} = 1 \) . Le mot \( x = {c}^{\ell }\left( w\right) \) s’écrit donc sous la forme \( x = {1y} \) où \( y \) est un mot qui a forcément \( n \) " 1 " et \( n \) "0 . Il reste à montrer que dans tous les préfixes de \( y \) , il y a moins de " 0 " que de " 1 ". On remarque que la fonction \( {f}_{x} \) vérifie

> - The first letter of \( {c}^{\ell }\left( w\right) \) is " 1 ". Indeed, by definition of \( \ell \) , we have \( {f}_{w}\left( k\right)  > m = {f}_{w}\left( \ell \right) \) for \( k > \ell \) , in particular \( {a}_{\ell  + 1} = {f}_{w}\left( {\ell  + 1}\right)  - {f}_{w}\left( \ell \right)  > 0 \) so \( {a}_{\ell  + 1} = 1 \) . The word \( x = {c}^{\ell }\left( w\right) \) can therefore be written in the form \( x = {1y} \) where \( y \) is a word that necessarily has \( n \) " 1 "s and \( n \) " 0 "s. It remains to show that in all prefixes of \( y \) , there are fewer " 0 "s than " 1 "s. We note that the function \( {f}_{x} \) satisfies

\[
{f}_{x}\left( k\right)  = \left\{  \begin{array}{l} {f}_{w}\left( {k + \ell }\right)  - {f}_{w}\left( \ell \right) \;\text{ pour }0 \leq  k \leq  {2n} + 1 - \ell \\  {f}_{w}\left( {k + \ell  - \left( {{2n} + 1}\right) }\right)  + 1 - {f}_{w}\left( \ell \right) \;\text{ pour }{2n} + 1 - \ell  < k \leq  {2n} + 1 \end{array}\right.
\]

Par définition de \( \ell \) , si \( 1 \leq k \leq {2n} + 1 - \ell \) on a \( {f}_{x}\left( k\right) > 0 \) . Lorsque \( {2n} + 1 - \ell < k \leq {2n} + 1 \) , on a \( {f}_{x}\left( k\right) \geq 1 \) car \( {f}_{w}\left( {k + \ell - \left( {{2n} + 1}\right) }\right) \geq {f}_{w}\left( \ell \right) \) . Ainsi \( {f}_{x}\left( k\right) \geq 1 \) pour \( 1 \leq k \leq {2n} + 1 \) , donc \( {f}_{x}\left( k\right) - {f}_{x}\left( 1\right) \geq 0 \) pour \( 1 \leq k \leq {2n} + 1 \) , ce qui signifie que dans tous les préfixes de \( y \) , il y a moins de " 0 " que de " 1 ". Donc \( y \) est un mot de Dyck.

> By definition of \( \ell \) , if \( 1 \leq k \leq {2n} + 1 - \ell \) we have \( {f}_{x}\left( k\right) > 0 \) . When \( {2n} + 1 - \ell < k \leq {2n} + 1 \) , we have \( {f}_{x}\left( k\right) \geq 1 \) because \( {f}_{w}\left( {k + \ell - \left( {{2n} + 1}\right) }\right) \geq {f}_{w}\left( \ell \right) \) . Thus \( {f}_{x}\left( k\right) \geq 1 \) for \( 1 \leq k \leq {2n} + 1 \) , so \( {f}_{x}\left( k\right) - {f}_{x}\left( 1\right) \geq 0 \) for \( 1 \leq k \leq {2n} + 1 \) , which means that in all prefixes of \( y \) , there are fewer " 0 "s than " 1 "s. Therefore \( y \) is a Dyck word.

- Il reste à montrer que \( \ell \) est le seul indice \( \leq  {2n} \) ayant cette propriété. Raisonnons par l’absurde et supposons l’existence de deux indices \( \ell \) et \( m\left( {\ell  < m}\right) \) ayant cette propriété. Soit \( u \) le mot \( u = {c}^{\ell }\left( w\right) \) et notons \( p = m - \ell \) . Compte tenu des propriétés de \( \ell \) et \( m \) , on a \( {f}_{u}\left( k\right)  \geq  1 \) pour \( 1 \leq  k \leq  {2n} \) et \( {f}_{u}\left( k\right)  \geq  1 + {f}_{u}\left( p\right) \) pour \( p < k \leq  {2n} + 1 \) . En particulier \( {f}_{u}\left( {{2n} + 1}\right)  \geq  1 + {f}_{u}\left( p\right)  \geq  2 \) , ce qui est impossible puisque \( {f}_{u}\left( {{2n} + 1}\right)  = 1 \) . On a donc démontré l'unicité recherchée.

> - It remains to show that \( \ell \) is the only index \( \leq  {2n} \) having this property. Let us reason by contradiction and assume the existence of two indices \( \ell \) and \( m\left( {\ell  < m}\right) \) having this property. Let \( u \) be the word \( u = {c}^{\ell }\left( w\right) \) and let us denote \( p = m - \ell \) . Given the properties of \( \ell \) and \( m \) , we have \( {f}_{u}\left( k\right)  \geq  1 \) for \( 1 \leq  k \leq  {2n} \) and \( {f}_{u}\left( k\right)  \geq  1 + {f}_{u}\left( p\right) \) for \( p < k \leq  {2n} + 1 \) . In particular \( {f}_{u}\left( {{2n} + 1}\right)  \geq  1 + {f}_{u}\left( p\right)  \geq  2 \) , which is impossible since \( {f}_{u}\left( {{2n} + 1}\right)  = 1 \) . We have thus demonstrated the sought uniqueness.

Notons \( {\mathcal{A}}_{n} \) les mots formés de \( n + 1 \) "1 et \( n \) "0 ", et \( {\mathcal{B}}_{n} \) les classes d’équivalence des mots de \( {\mathcal{A}}_{n} \) égaux à une permutation circulaire près. Le résultat montré précédemment montre que l’application \( \varphi : {\mathcal{D}}_{n} \rightarrow {\mathcal{B}}_{n}w \mapsto \overline{1w} \) (où \( \bar{x} \) désigne la classe d’équivalence dans \( {\mathcal{B}}_{n} \) d’un mot \( x \) de \( {\mathcal{A}}_{n} \) ) est bijective. On en déduit \( \left| {\mathcal{D}}_{n}\right| = \left| {\mathcal{B}}_{n}\right| \) . Or les \( {2n} + 1 \) permutations circulaires \( {c}^{k}\left( w\right) \) de n’importe quel mot \( w \in {\mathcal{A}}_{n} \) sont distinctes : en effet, soit \( \ell \) l’unique entier de \( \{ 0,1,\ldots ,{2n}\} \) vérifiant \( {c}^{\ell }\left( w\right) = {1y} \) avec \( y \in {\mathcal{D}}_{n} \) . Si \( {c}^{p}\left( w\right) = {c}^{q}\left( w\right) \) alors \( w = {c}^{q - p}\left( w\right) \) , donc \( {c}^{\ell }\left( w\right) = {c}^{\ell + q - p}\left( w\right) = \; {1y} \) , et par unicité de \( \ell \) on en déduit \( \ell + p - q \equiv \ell \left( {{\;\operatorname{mod}\;2}n + 1}\right) \) donc \( p = q\left( {{\;\operatorname{mod}\;2}n + 1}\right) \) . Donc \( \left| {\mathcal{B}}_{n}\right| = \left| {\mathcal{A}}_{n}\right| /\left( {{2n} + 1}\right) \) . Il y a autant de mots \( w \) dans \( {\mathcal{A}}_{n} \) que de façon de répartir les \( n \) " 0 "parmi les \( {2n} + 1 \) lettres de \( w \) , donc \( \left| {\mathcal{A}}_{n}\right| = \left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) \) . On en déduit \( \left| {\mathcal{D}}_{n}\right| = \frac{1}{{2n} + 1}\left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) \) . On vérifie facilement que \( \frac{1}{{2n} + 1}\left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) = \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \) , retrouvant ainsi le résultat obtenu à la question précédente.

> Let \( {\mathcal{A}}_{n} \) be the words formed of \( n + 1 \) "1"s and \( n \) "0"s, and \( {\mathcal{B}}_{n} \) be the equivalence classes of words in \( {\mathcal{A}}_{n} \) equal up to a circular permutation. The result shown previously demonstrates that the mapping \( \varphi : {\mathcal{D}}_{n} \rightarrow {\mathcal{B}}_{n}w \mapsto \overline{1w} \) (where \( \bar{x} \) denotes the equivalence class in \( {\mathcal{B}}_{n} \) of a word \( x \) in \( {\mathcal{A}}_{n} \)) is bijective. We deduce \( \left| {\mathcal{D}}_{n}\right| = \left| {\mathcal{B}}_{n}\right| \). However, the \( {2n} + 1 \) circular permutations \( {c}^{k}\left( w\right) \) of any word \( w \in {\mathcal{A}}_{n} \) are distinct: indeed, let \( \ell \) be the unique integer in \( \{ 0,1,\ldots ,{2n}\} \) satisfying \( {c}^{\ell }\left( w\right) = {1y} \) with \( y \in {\mathcal{D}}_{n} \). If \( {c}^{p}\left( w\right) = {c}^{q}\left( w\right) \), then \( w = {c}^{q - p}\left( w\right) \), so \( {c}^{\ell }\left( w\right) = {c}^{\ell + q - p}\left( w\right) = \; {1y} \), and by the uniqueness of \( \ell \) we deduce \( \ell + p - q \equiv \ell \left( {{\;\operatorname{mod}\;2}n + 1}\right) \), thus \( p = q\left( {{\;\operatorname{mod}\;2}n + 1}\right) \). Therefore \( \left| {\mathcal{B}}_{n}\right| = \left| {\mathcal{A}}_{n}\right| /\left( {{2n} + 1}\right) \). There are as many words \( w \) in \( {\mathcal{A}}_{n} \) as there are ways to distribute the \( n \) "0"s among the \( {2n} + 1 \) letters of \( w \), so \( \left| {\mathcal{A}}_{n}\right| = \left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) \). We deduce \( \left| {\mathcal{D}}_{n}\right| = \frac{1}{{2n} + 1}\left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) \). We easily verify that \( \frac{1}{{2n} + 1}\left( \begin{matrix} {2n} + 1 \\ n \end{matrix}\right) = \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \), thus recovering the result obtained in the previous question.

Remarque. Ainsi \( \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \) est un nombre entier, résultat non évident a priori. - Les nombres de Catalan sont des nombres classiques qu'on retrouve dans le comptage de nombreuses structures. Par exemple le nombre \( {C}_{n} \) est :

> Remark. Thus \( \frac{1}{n + 1}\left( \begin{matrix} {2n} \\ n \end{matrix}\right) \) is an integer, a result not obvious a priori. - Catalan numbers are classic numbers found in the counting of many structures. For example, the number \( {C}_{n} \) is:

- le nombre de façons de calculer le produit de \( n + 1 \) facteurs (avec parenthésages com-plets). Par exemple pour \( n = 4 : \left( {a\left( {bc}\right) }\right) d, a\left( {\left( {bc}\right) d}\right) ,\left( {ab}\right) \left( {cd}\right) , a\left( {b\left( {cd}\right) }\right) \) et \( \left( {\left( {ab}\right) c}\right) d \) ,

> - the number of ways to calculate the product of \( n + 1 \) factors (with complete parenthesization). For example for \( n = 4 : \left( {a\left( {bc}\right) }\right) d, a\left( {\left( {bc}\right) d}\right) ,\left( {ab}\right) \left( {cd}\right) , a\left( {b\left( {cd}\right) }\right) \) and \( \left( {\left( {ab}\right) c}\right) d \),

- le nombre d’arbres binaires avec \( n + 1 \) feuilles,

> - the number of binary trees with \( n + 1 \) leaves,

- le nombre de façons de tracer des diagonales entre les sommets d’un polygône convexe de \( n + 2 \) cotés, sans qu’elles ne se coupent.

> - the number of ways to draw diagonals between the vertices of a convex polygon with \( n + 2 \) sides, without them intersecting.

EXERCICE 11. Soit \( m \geq 2 \) un entier. On suppose qu’il existe \( a \in \mathbb{N} \) et \( n \in {\mathbb{N}}^{ * } \) parties non vides et distinctes deux a deux \( {A}_{1},\ldots ,{A}_{n} \) de \( \{ 1,2,\ldots , m\} \) telles que \( \left| {{A}_{i} \cap {A}_{j}}\right| = a \) pour \( i \neq j \) . Montrer que \( n \leq m \) (indication : considérer la matrice \( A = {\left( {a}_{i, j}\right) }_{i, j} \) définie par \( \left. {{a}_{i, j} = 1\text{ si }i \in {A}_{j},{a}_{i, j} = 0\text{ si }i \notin {A}_{j}\text{ , et montrer que son rang est } \geq n}\right) \) . \( {c}_{i} = \left| {A}_{i}\right| \) , la matrice \( B \) a la forme

> EXERCISE 11. Let \( m \geq 2 \) be an integer. Suppose there exist \( a \in \mathbb{N} \) and \( n \in {\mathbb{N}}^{ * } \) non-empty and pairwise distinct subsets \( {A}_{1},\ldots ,{A}_{n} \) of \( \{ 1,2,\ldots , m\} \) such that \( \left| {{A}_{i} \cap {A}_{j}}\right| = a \) for \( i \neq j \). Show that \( n \leq m \) (hint: consider the matrix \( A = {\left( {a}_{i, j}\right) }_{i, j} \) defined by \( \left. {{a}_{i, j} = 1\text{ si }i \in {A}_{j},{a}_{i, j} = 0\text{ si }i \notin {A}_{j}\text{ , et montrer que son rang est } \geq n}\right) \). \( {c}_{i} = \left| {A}_{i}\right| \), the matrix \( B \) has the form

\[
B = \left( \begin{matrix} {c}_{1} & a & \ldots & a \\  a & {c}_{2} & \ldots & a \\  \vdots & &  \ddots  & \vdots \\  a & \ldots & a & {c}_{n} \end{matrix}\right) .
\]

---

Solution. Considérons la matrice \( A \in {\mathcal{M}}_{m, n}\left( \mathbb{R}\right) \) de l’indication. On remarque que les coefficients \( \left( {b}_{i, j}\right) \) de la matrice \( B = {}^{\mathrm{t}}{AA} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) vérifient \( {b}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{m}{a}_{k, j}{a}_{k, i} = \left| {{A}_{i} \cap {A}_{j}}\right| \) . Ainsi, en notant

> Solution. Consider the matrix \( A \in {\mathcal{M}}_{m, n}\left( \mathbb{R}\right) \) from the hint. We note that the coefficients \( \left( {b}_{i, j}\right) \) of the matrix \( B = {}^{\mathrm{t}}{AA} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) satisfy \( {b}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{m}{a}_{k, j}{a}_{k, i} = \left| {{A}_{i} \cap {A}_{j}}\right| \). Thus, by denoting

---

On va montrer qu’elle est inversible. C’est évident si \( a = 0 \) car les \( {A}_{i} \) sont non vides. Supposons maintenant \( a > 0 \) . On va montrer que les vecteurs colonnes \( {V}_{i} \) de la matrice \( B \) forment une famille libre. Notons \( W \) le vecteur dont toutes coordonnées sont égales à \( a \) . On a

> We will show that it is invertible. This is obvious if \( a = 0 \) because the \( {A}_{i} \) are non-empty. Now suppose \( a > 0 \). We will show that the column vectors \( {V}_{i} \) of the matrix \( B \) form a linearly independent family. Let \( W \) be the vector whose coordinates are all equal to \( a \). We have

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{V}_{i} = 0 \Rightarrow  \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( {{V}_{i} - W}\right)  =  - {\mu W},\;\mu  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}.
\]

Comme le vecteur \( {V}_{i} - W \) a toutes ses coordonnées nulles, sauf la \( i \) -ième qui vaut \( {c}_{i} - a \) on en déduit

> Since the vector \( {V}_{i} - W \) has all its coordinates equal to zero, except the \( i \)-th which is equal to \( {c}_{i} - a \), we deduce

\[
{\lambda }_{1}\left( {{c}_{1} - a}\right)  =  - {\mu a},\;\ldots ,\;{\lambda }_{n}\left( {{c}_{n} - a}\right)  =  - {\mu a}.
\]

(*)

> Pour tout \( i \) , on a \( {c}_{i} = \left| {A}_{i}\right| \geq \left| {{A}_{i} \cap {A}_{j}}\right| = a \) (en choisissant un \( j \neq i \) ). Au plus l’un des \( {c}_{i} \) est égal à \( a \) (si \( {c}_{i} = {c}_{j} = a \) on a \( \left| {{A}_{i} \cap {A}_{j}}\right| = \left| {A}_{i}\right| \) donc \( {A}_{i} \cap {A}_{j} = {A}_{i} \) , de même \( {A}_{i} \cap {A}_{j} = {A}_{j} \) donc \( {A}_{i} = {A}_{j} \) , ce qui entraîne \( i = j \) d’après les hypothèses). Maintenant on traite deux cas.

For any \( i \), we have \( {c}_{i} = \left| {A}_{i}\right| \geq \left| {{A}_{i} \cap {A}_{j}}\right| = a \) (by choosing a \( j \neq i \)). At most one of the \( {c}_{i} \) is equal to \( a \) (if \( {c}_{i} = {c}_{j} = a \) we have \( \left| {{A}_{i} \cap {A}_{j}}\right| = \left| {A}_{i}\right| \) thus \( {A}_{i} \cap {A}_{j} = {A}_{i} \), likewise \( {A}_{i} \cap {A}_{j} = {A}_{j} \) thus \( {A}_{i} = {A}_{j} \), which leads to \( i = j \) according to the hypotheses). Now we consider two cases.

> - Premier cas : \( {c}_{i} > a \) pour tout \( i \) . Alors d’après (*) tous les \( {\lambda }_{i} \) ont le même signe, donc du signe de \( \mu  = {\lambda }_{1} + \cdots  + {\lambda }_{n} \) , et comme \( {\lambda }_{i}\left( {{c}_{i} - a}\right)  =  - {\mu a} \) la seule possibilité est \( {\lambda }_{i} = \mu  = 0 \) .

- First case: \( {c}_{i} > a \) for all \( i \). Then according to (*) all the \( {\lambda }_{i} \) have the same sign, therefore the sign of \( \mu  = {\lambda }_{1} + \cdots  + {\lambda }_{n} \), and since \( {\lambda }_{i}\left( {{c}_{i} - a}\right)  =  - {\mu a} \) the only possibility is \( {\lambda }_{i} = \mu  = 0 \).

> - Deuxième cas : l’un des \( {c}_{i} \) est égal à \( a \) , par exemple \( {c}_{n} = a \) , et \( {c}_{i} > a \) pour \( i < n \) . Dans ce cas \( {\mu a} = 0 \) (d’après la dernière égalité de (*)) donc \( \mu  = 0 \) . Donc les \( n - 1 \) premières égalités de (*) entraînent \( {\lambda }_{i} = 0 \) pour \( i < n \) , puis \( {\lambda }_{n} = \mu  - \mathop{\sum }\limits_{{i < n}}{\lambda }_{i} = 0 \) .

- Second case: one of the \( {c}_{i} \) is equal to \( a \), for example \( {c}_{n} = a \), and \( {c}_{i} > a \) for \( i < n \). In this case \( {\mu a} = 0 \) (according to the last equality of (*)) thus \( \mu  = 0 \). Therefore the first \( n - 1 \) equalities of (*) lead to \( {\lambda }_{i} = 0 \) for \( i < n \), then \( {\lambda }_{n} = \mu  - \mathop{\sum }\limits_{{i < n}}{\lambda }_{i} = 0 \).

> Ainsi la famille \( {\left( {V}_{i}\right) }_{1 \leq i \leq n} \) est libre, donc \( B \) est inversible. On en déduit rg t \( {AA} = n \) , donc rg \( A \geq n \) , et comme \( A \) a \( m \) lignes ceci n’est possible que si \( m \geq n \) , ce qu’il fallait démontrer.

Thus the family \( {\left( {V}_{i}\right) }_{1 \leq i \leq n} \) is linearly independent, so \( B \) is invertible. We deduce rg t \( {AA} = n \), therefore rg \( A \geq n \), and since \( A \) has \( m \) rows this is only possible if \( m \geq n \), which was to be demonstrated.

> Remarque. On aurait pu également montrer l’inversibilité de \( B \) à partir du calcul de son déterminant qui est classique (voir la question c) de l'exercice 2 page 145).

Remark. We could also have shown the invertibility of \( B \) from the calculation of its determinant, which is classic (see question c) of exercise 2 page 145).
