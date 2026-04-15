#### 1.3. Exercises

*Français : 1.3. Exercices*

EXERCICE 1. Déterminer les triplets \( \left( {a, b, c}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{3} \) tels que

> EXERCISE 1. Determine the triplets \( \left( {a, b, c}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{3} \) such that

(i) \( \operatorname{ppcm}\left( {a, b}\right) = {42}\; \) (ii) \( \operatorname{pgcd}\left( {a, c}\right) = 3\; \) (iii) \( a + b + c = {29} \) .

> (i) \( \operatorname{ppcm}\left( {a, b}\right) = {42}\; \) (ii) \( \operatorname{pgcd}\left( {a, c}\right) = 3\; \) (iii) \( a + b + c = {29} \) .

---

Solution. D’après (ii), \( 3\left| {a\text{ et }3}\right| c \) , donc 3 \( \mid \left( {a + c}\right) \) . Comme \( b = {29} - \left( {a + c}\right) \) , \( b \) n’est pas un multiple de 3, et 3 étant premier, \( 3 \land b = 1 \) . En utilisant (i) on a \( b \mid {42} = 3 \times {14} \) et d’après le théorème de Gauss, \( b \mid {14} \) . Donc \( b \in \{ 1,2,7,{14}\} \) . Mais \( {29} - b = a + c \) est divisible par 3, ce qui restreint les valeurs possibles de \( b \) à 2 et 14 .

> Solution. According to (ii), \( 3\left| {a\text{ et }3}\right| c \), so 3 \( \mid \left( {a + c}\right) \). Since \( b = {29} - \left( {a + c}\right) \), \( b \) is not a multiple of 3, and 3 being prime, \( 3 \land b = 1 \). Using (i) we have \( b \mid {42} = 3 \times {14} \) and according to Gauss's theorem, \( b \mid {14} \). Therefore \( b \in \{ 1,2,7,{14}\} \). But \( {29} - b = a + c \) is divisible by 3, which restricts the possible values of \( b \) to 2 and 14.

- Si \( b = 2, a \in  \{ {21},{42}\} \) d’après (i). Mais \( a \leq  {29} \) d’après (iii), donc \( a = {21} \) et \( c = 6 \) avec (iii).

> - If \( b = 2, a \in  \{ {21},{42}\} \) according to (i). But \( a \leq  {29} \) according to (iii), so \( a = {21} \) and \( c = 6 \) with (iii).

- Si \( b = {14}, a \in  \{ 3,6,{21},{42}\} \) d’après (i). La relation (iii) entraîne \( a \leq  {29} - b = {15} \) , d’où \( a \in  \{ 3,6\} \) . Si \( a = 3, c = {12} \) par (iii); si \( a = 6, c = 9 \) .

> - If \( b = {14}, a \in  \{ 3,6,{21},{42}\} \) according to (i). The relation (iii) implies \( a \leq  {29} - b = {15} \), hence \( a \in  \{ 3,6\} \). If \( a = 3, c = {12} \) by (iii); if \( a = 6, c = 9 \).

---

Nécessairement, on a donc \( \left( {a, b, c}\right) = \left( {{21},2,6}\right) ,\left( {3,{14},{12}}\right) \) ou \( \left( {6,{14},9}\right) \) . Réciproquement, on vérifie facilement que ces triplets sont solution.

> Necessarily, we therefore have \( \left( {a, b, c}\right) = \left( {{21},2,6}\right) ,\left( {3,{14},{12}}\right) \) or \( \left( {6,{14},9}\right) \). Conversely, it is easy to verify that these triplets are solutions.

\( \rightarrow \) EXERCICE 2. 1/ Soient \( a \) et \( b \geq 2 \) deux entiers naturels non nuls premiers entre eux. Montrer que

> \( \rightarrow \) EXERCISE 2. 1/ Let \( a \) and \( b \geq 2 \) be two non-zero natural integers that are coprime. Show that

\[
\exists !\left( {{u}_{0},{v}_{0}}\right)  \in  {\mathbb{N}}^{2},\;{u}_{0}a - {v}_{0}b = 1,\;\text{ avec }\;{u}_{0} < b\text{ et }{v}_{0} < a
\]

\( \left( *\right) \)

> et exprimer en fonction de \( {u}_{0},{v}_{0}, a \) et \( b \) tous les couples \( \left( {u, v}\right) \in {\mathbb{Z}}^{2} \) solutions de \( {ua} - {vb} = 1 \) . 2/ Déterminer deux entiers \( u \) et \( v \) vérifiant \( {47u} + {111v} = 1 \) .

and express all pairs \( \left( {u, v}\right) \in {\mathbb{Z}}^{2} \) that are solutions to \( {ua} - {vb} = 1 \) in terms of \( {u}_{0},{v}_{0}, a \) and \( b \). 2/ Determine two integers \( u \) and \( v \) satisfying \( {47u} + {111v} = 1 \).

> Solution. 1 / Le théorème de Bezout assure l’existence de deux entiers \( {u}_{1} \) et \( {v}_{1} \) vérifiant \( {u}_{1}a - \; {v}_{1}b = 1 \) . On effectue ensuite la division euclidienne de \( {u}_{1} \) par \( b : {u}_{1} = {bq} + {u}_{0} \) , avec \( 0 \leq {u}_{0} < b \) . On obtient \( \left( {{bq} + {u}_{0}}\right) a - {v}_{1}b = 1 = {u}_{0}a - {v}_{0}b \) , avec \( {v}_{0} = {v}_{1} - {aq} \) . Donc \( - 1 \leq {v}_{0}b = {u}_{0}a - 1 < {u}_{0}a < {ba} \) , et en divisant par \( b \geq 2 \) , on tire \( 0 \leq {v}_{0} < a \) . Ainsi, notre couple \( \left( {{u}_{0},{v}_{0}}\right) \) vérifie l’assertion \( \left( *\right) \) .

Solution. 1/ Bezout's theorem ensures the existence of two integers \( {u}_{1} \) and \( {v}_{1} \) satisfying \( {u}_{1}a - \; {v}_{1}b = 1 \). We then perform the Euclidean division of \( {u}_{1} \) by \( b : {u}_{1} = {bq} + {u}_{0} \), with \( 0 \leq {u}_{0} < b \). We obtain \( \left( {{bq} + {u}_{0}}\right) a - {v}_{1}b = 1 = {u}_{0}a - {v}_{0}b \), with \( {v}_{0} = {v}_{1} - {aq} \). Thus \( - 1 \leq {v}_{0}b = {u}_{0}a - 1 < {u}_{0}a < {ba} \), and by dividing by \( b \geq 2 \), we derive \( 0 \leq {v}_{0} < a \). Thus, our pair \( \left( {{u}_{0},{v}_{0}}\right) \) satisfies the assertion \( \left( *\right) \).

> Ceci étant, considérons un couple \( \left( {u, v}\right) \) vérifiant \( {ua} - {vb} = 1 \) . En retranchant à \( \left( *\right) \) , on obtient

This being so, let us consider a pair \( \left( {u, v}\right) \) satisfying \( {ua} - {vb} = 1 \). By subtracting from \( \left( *\right) \), we obtain

\[
\left( {u - {u}_{0}}\right) a = \left( {v - {v}_{0}}\right) b.
\]

\( \left( {* * }\right) \)

> Ceci montre que \( a \mid \left( {v - {v}_{0}}\right) b \) et comme \( a \) et \( b \) sont premiers entre eux, le théorème de Gauss entraîne \( a \mid \left( {v - {v}_{0}}\right) \) . Soit \( k \in \mathbb{Z} \) tel que \( v = {v}_{0} + {ka} \) . En remplaçant dans \( \left( {* * }\right) \) , on obtient \( \left( {u, v}\right) = \left( {{u}_{0} + {kb},{v}_{0} + {ka}}\right) \) . Ceci prouve que le couple \( \left( {{u}_{0},{v}_{0}}\right) \) est bien l’unique couple vérifiant la propriété (*), et réciproquement, on vérifie facilement que les couples de cette forme sont solutions de \( {ua} - {vb} = 1 \) .

This shows that \( a \mid \left( {v - {v}_{0}}\right) b \) and since \( a \) and \( b \) are coprime, Gauss's theorem implies \( a \mid \left( {v - {v}_{0}}\right) \). Let \( k \in \mathbb{Z} \) be such that \( v = {v}_{0} + {ka} \). By substituting into \( \left( {* * }\right) \), we obtain \( \left( {u, v}\right) = \left( {{u}_{0} + {kb},{v}_{0} + {ka}}\right) \). This proves that the pair \( \left( {{u}_{0},{v}_{0}}\right) \) is indeed the unique pair satisfying property (*), and conversely, it is easy to verify that pairs of this form are solutions to \( {ua} - {vb} = 1 \).

> 2 / Les nombres 47 et 111 sont premiers entre eux, \( u \) et \( v \) existent donc. Nous allons les déterminer grâce à l'algorithme d'Euclide. On effectue d'abord la division euclidienne de 111 par 47

2/ The numbers 47 and 111 are coprime, so \( u \) and \( v \) exist. We will determine them using the Euclidean algorithm. We first perform the Euclidean division of 111 by 47

\[
{111} = {47} \times  2 + {17}
\]

puis on itère en divisant toujours le dividende par le reste, jusqu'à ce que le reste égale 1 :

> then we iterate by always dividing the dividend by the remainder, until the remainder equals 1:

\[
{47} = {17} \times  2 + {13},\;{17} = {13} \times  1 + 4,\;{13} = 4 \times  3 + 1.
\]

On part maintenant de \( 1 = {13} - 4 \times 3 \) et on remonte :

> We now start from \( 1 = {13} - 4 \times 3 \) and work backwards:

\( 1 = {13} - 4 \times 3 = {13} - \left( {{17} - {13} \times 1}\right) \times 3 = 4 \times {13} - 3 \times {17} = 4 \times \left( {{47} - {17} \times 2}\right) - 3 \times {17} = \; 4 \times {47} - {11} \times {17} = 4 \times {47} - {11} \times \left( {{111} - {47} \times 2}\right) = {26} \times {47} - {11} \times {111} \) , d’où le résultat avec \( u = {26} \) et \( v = - {11} \) .

> \( 1 = {13} - 4 \times 3 = {13} - \left( {{17} - {13} \times 1}\right) \times 3 = 4 \times {13} - 3 \times {17} = 4 \times \left( {{47} - {17} \times 2}\right) - 3 \times {17} = \; 4 \times {47} - {11} \times {17} = 4 \times {47} - {11} \times \left( {{111} - {47} \times 2}\right) = {26} \times {47} - {11} \times {111} \) , whence the result with \( u = {26} \) and \( v = - {11} \) .

Remarque. Il existe des résultats analogues sur les polynômes (voir l'exercice 3 page 60).

> Remark. There are analogous results for polynomials (see exercise 3 on page 60).

EXERCICE 3. a) Montrer que pour tout entier naturel \( n,5 \mid \left( {{2}^{{3n} + 5} + {3}^{n + 1}}\right) \) .

> EXERCISE 3. a) Show that for any natural integer \( n,5 \mid \left( {{2}^{{3n} + 5} + {3}^{n + 1}}\right) \) .

b) Montrer que pour tout entier \( n,{30} \mid \left( {{n}^{5} - n}\right) \) .

> b) Show that for any integer \( n,{30} \mid \left( {{n}^{5} - n}\right) \) .

c) Quel est le reste de la division euclidienne de \( {16}^{\left( {2}^{1000}\right) } \) par 7?

> c) What is the remainder of the Euclidean division of \( {16}^{\left( {2}^{1000}\right) } \) by 7?

Solution. a) On a \( {2}^{5} \equiv 2\left( {\;\operatorname{mod}\;5}\right) \) et \( {2}^{3n} \equiv {8}^{n} \equiv {3}^{n}\left( {\;\operatorname{mod}\;5}\right) \) donc \( {2}^{{3n} + 5} \equiv 2 \cdot {3}^{n}\left( {\;\operatorname{mod}\;5}\right) \) et \( {2}^{{3n} + 5} + {3}^{n + 1} \equiv 2 \cdot {3}^{n} + 3 \cdot {3}^{n} \equiv 0\left( {\;\operatorname{mod}\;5}\right) . \)

> Solution. a) We have \( {2}^{5} \equiv 2\left( {\;\operatorname{mod}\;5}\right) \) and \( {2}^{3n} \equiv {8}^{n} \equiv {3}^{n}\left( {\;\operatorname{mod}\;5}\right) \) therefore \( {2}^{{3n} + 5} \equiv 2 \cdot {3}^{n}\left( {\;\operatorname{mod}\;5}\right) \) and \( {2}^{{3n} + 5} + {3}^{n + 1} \equiv 2 \cdot {3}^{n} + 3 \cdot {3}^{n} \equiv 0\left( {\;\operatorname{mod}\;5}\right) . \)

b) D’après le théorème de Fermat, \( {n}^{5} \equiv n\left( {\;\operatorname{mod}\;5}\right) \) , c’est-à-dire \( 5 \mid \left( {{n}^{5} - n}\right) \) .

> b) According to Fermat's theorem, \( {n}^{5} \equiv n\left( {\;\operatorname{mod}\;5}\right) \) , that is to say \( 5 \mid \left( {{n}^{5} - n}\right) \) .

De même, \( {n}^{3} \equiv n\left( {\;\operatorname{mod}\;3}\right) \) donc \( {n}^{5} \equiv {n}^{3} \cdot {n}^{2} \equiv n \cdot {n}^{2} \equiv {n}^{3} \equiv n\left( {\;\operatorname{mod}\;3}\right) \) , i. e. \( 3 \mid \left( {{n}^{5} - n}\right) \) .

> Similarly, \( {n}^{3} \equiv n\left( {\;\operatorname{mod}\;3}\right) \) therefore \( {n}^{5} \equiv {n}^{3} \cdot {n}^{2} \equiv n \cdot {n}^{2} \equiv {n}^{3} \equiv n\left( {\;\operatorname{mod}\;3}\right) \) , i. e. \( 3 \mid \left( {{n}^{5} - n}\right) \) .

Les entiers \( n \) et \( {n}^{5} \) ayant même parité, on a aussi \( 2 \mid \left( {{n}^{5} - n}\right) \) .

> Since the integers \( n \) and \( {n}^{5} \) have the same parity, we also have \( 2 \mid \left( {{n}^{5} - n}\right) \) .

De plus 2,3 et 5 sont premiers entre eux deux à deux, et finalement 30 = 2 3 .5 divise \( \left( {{n}^{5} - n}\right) \) . c) Posons \( N = {16}^{\left( {2}^{1000}\right) } \) . Il s’agit de déterminer la classe de congruence de \( N \) modulo 7 . Comme \( {16} \equiv 2\left( {\;\operatorname{mod}\;7}\right) \) , on a déjà \( N \equiv {2}^{{2}^{1000}}\left( {\;\operatorname{mod}\;7}\right) \) . En vue d’utiliser la relation \( {2}^{6} \equiv 1\left( {\;\operatorname{mod}\;7}\right) \) (théorème de Fermat), recherchons le reste de la division de \( {2}^{1000} \) par 6 . La relation \( {4}^{2} \equiv 4 \) (mod 6) permet d’obtenir, par récurrence sur \( n \) , la relation \( {4}^{n} \equiv 4 \) (mod 6), vraie pour tout \( n \) . En particulier, \( {2}^{1000} \equiv {4}^{500} \equiv 4 \) (mod 6), donc il existe un entier naturel \( q \) tel que \( {2}^{1000} = {6q} + 4 \) .

> Furthermore, 2, 3, and 5 are pairwise coprime, and finally 30 = 2 3 .5 divides \( \left( {{n}^{5} - n}\right) \) . c) Let \( N = {16}^{\left( {2}^{1000}\right) } \) . We must determine the congruence class of \( N \) modulo 7 . Since \( {16} \equiv 2\left( {\;\operatorname{mod}\;7}\right) \) , we already have \( N \equiv {2}^{{2}^{1000}}\left( {\;\operatorname{mod}\;7}\right) \) . In order to use the relation \( {2}^{6} \equiv 1\left( {\;\operatorname{mod}\;7}\right) \) (Fermat's Little Theorem), let us find the remainder of the division of \( {2}^{1000} \) by 6 . The relation \( {4}^{2} \equiv 4 \) (mod 6) allows us to obtain, by induction on \( n \) , the relation \( {4}^{n} \equiv 4 \) (mod 6), true for all \( n \) . In particular, \( {2}^{1000} \equiv {4}^{500} \equiv 4 \) (mod 6), so there exists a natural number \( q \) such that \( {2}^{1000} = {6q} + 4 \) .

Il ne reste qu'à écrire

> It only remains to write

\[
N \equiv  {2}^{{6q} + 4} \equiv  {\left( {2}^{6}\right) }^{q} \cdot  {2}^{4} \equiv  {1}^{q}{2}^{4} \equiv  {2}^{4} \equiv  2\;\left( {\;\operatorname{mod}\;7}\right) ,
\]

et le reste recherché est 2.

> and the sought remainder is 2.

EXERCICE 4 (NOMBRES DE MERSENNE, NOMBRES DE FERMAT). a) Nombres de Mer-senne. Soient \( a \geq 2 \) et \( n \geq 2 \) deux entiers. Si \( {a}^{n} - 1 \) est un nombre premier, montrer que \( a = 2 \) et que \( n \) est un nombre premier (un nombre de la forme \( {2}^{p} - 1 \) où \( p \) est un nombre premier, est appelé nombre de Mersenne).

> EXERCISE 4 (MERSENNE NUMBERS, FERMAT NUMBERS). a) Mersenne numbers. Let \( a \geq 2 \) and \( n \geq 2 \) be two integers. If \( {a}^{n} - 1 \) is a prime number, show that \( a = 2 \) and that \( n \) is a prime number (a number of the form \( {2}^{p} - 1 \) where \( p \) is a prime number is called a Mersenne number).

b) Nombres de Fermat. Soit \( n \in {\mathbb{N}}^{ * } \) . Si \( {2}^{n} + 1 \) est un nombre premier, montrer que \( n \) est une puissance de 2.

> b) Fermat numbers. Let \( n \in {\mathbb{N}}^{ * } \) . If \( {2}^{n} + 1 \) is a prime number, show that \( n \) is a power of 2.

Solution. a) L’identité \( {x}^{n} - 1 = \left( {x - 1}\right) \left( {{x}^{n - 1} + \cdots + x + 1}\right) \) montre que

> Solution. a) The identity \( {x}^{n} - 1 = \left( {x - 1}\right) \left( {{x}^{n - 1} + \cdots + x + 1}\right) \) shows that

\[
\forall x \in  \mathbb{N}, x \geq  2,\;\left( {x - 1}\right) \text{ divise }\left( {{x}^{n} - 1}\right) .
\]

(*)

> L’entier \( {a}^{n} - 1 \) étant premier, on en déduit \( a - 1 = 1 \) , c’est-à-dire \( a = 2 \) .

Since the integer \( {a}^{n} - 1 \) is prime, we deduce \( a - 1 = 1 \) , that is to say \( a = 2 \) .

> Écrivons \( n = {pq} \) où \( p \) et \( q \) sont deux entiers naturels. On a \( {a}^{n} - 1 = {2}^{n} - 1 = {\left( {2}^{q}\right) }^{p} - 1 \) de sorte que \( \left( {{2}^{q} - 1}\right) \) divise \( {a}^{n} - 1 \) d’après \( \left( *\right) \) , ce qui entraîne \( q = 1 \) ou \( q = n \) puisque \( {a}^{n} - 1 \) est premier. L’entier \( n \) est donc premier.

Let us write \( n = {pq} \) where \( p \) and \( q \) are two natural numbers. We have \( {a}^{n} - 1 = {2}^{n} - 1 = {\left( {2}^{q}\right) }^{p} - 1 \) so that \( \left( {{2}^{q} - 1}\right) \) divides \( {a}^{n} - 1 \) according to \( \left( *\right) \) , which implies \( q = 1 \) or \( q = n \) since \( {a}^{n} - 1 \) is prime. The integer \( n \) is therefore prime.

> b) Lorsque \( n \) est impair, l’identité \( {x}^{n} + 1 = \left( {x + 1}\right) \left( {{x}^{n - 1} - \cdots + {x}^{2} - x + 1}\right) \) entraîne

b) When \( n \) is odd, the identity \( {x}^{n} + 1 = \left( {x + 1}\right) \left( {{x}^{n - 1} - \cdots + {x}^{2} - x + 1}\right) \) implies

\[
\forall x \in  \mathbb{N},\forall n \in  \mathbb{N}, n\text{ impair },\;\left( {x + 1}\right) \text{ divise }\left( {{x}^{n} + 1}\right) .
\]

\( \left( {* * }\right) \)

> Si \( n \) n’est pas une puissance de \( 2, n \) a au moins un facteur impair \( p > 1 \) . Écrivons \( n = {pq} \) avec \( q \in {\mathbb{N}}^{ * } \) . L’entier \( {2}^{n} + 1 = {\left( {2}^{q}\right) }^{p} + 1 \) est divisible par \( \left( {{2}^{q} + 1}\right) \) d’après \( \left( {* * }\right) \) , donc non premier. Ainsi, \( n \) doit être une puissance de 2.

If \( n \) is not a power of \( 2, n \), it has at least one odd factor \( p > 1 \). Let us write \( n = {pq} \) with \( q \in {\mathbb{N}}^{ * } \). The integer \( {2}^{n} + 1 = {\left( {2}^{q}\right) }^{p} + 1 \) is divisible by \( \left( {{2}^{q} + 1}\right) \) according to \( \left( {* * }\right) \), and is therefore not prime. Thus, \( n \) must be a power of 2.

> Remarque. La réciproque du résultat de la question a) est fausse. Par exemple, \( {2}^{11} - 1 = \; {23} \times {49}\mathrm{n} \) ’est pas premier. Cependant, on peut tester facilement la primalité des nombres de Mersenne grâce au test suivant (test de Lucas).

Remark. The converse of the result in question a) is false. For example, \( {2}^{11} - 1 = \; {23} \times {49}\mathrm{n} \) is not prime. However, one can easily test the primality of Mersenne numbers using the following test (Lucas test).

> Soit \( \left( {Y}_{n}\right) \) la suite définie par \( {Y}_{0} = 2 \) et \( {Y}_{n + 1} = 2{Y}_{n}^{2} - 1 \) . Si \( n \geq 3,{2}^{n} - 1 \)

Let \( \left( {Y}_{n}\right) \) be the sequence defined by \( {Y}_{0} = 2 \) and \( {Y}_{n + 1} = 2{Y}_{n}^{2} - 1 \). If \( n \geq 3,{2}^{n} - 1 \)

> est premier si et seulement si \( \left( {{2}^{n} - 1}\right) \mid {Y}_{n - 2} \) .

is prime if and only if \( \left( {{2}^{n} - 1}\right) \mid {Y}_{n - 2} \).

> Ce test a permis de trouver le plus grand nombre premier connu en \( {2020} : {2}^{82589933} - 1 \) , nombre d'un peu moins de 25 millions de chiffres, établi en 2018 avec le test de Lucas. On ignore s'il y a une infinité de nombres de Mersenne premiers ou pas. Notons que les nombres de Mersenne apparaissent dans les nombres parfaits (voir l'exercice 10 page 16).

This test allowed for the discovery of the largest known prime number in \( {2020} : {2}^{82589933} - 1 \), a number with just under 25 million digits, established in 2018 using the Lucas test. It is unknown whether there are infinitely many Mersenne primes or not. Note that Mersenne numbers appear in perfect numbers (see exercise 10 on page 16).

> - Nombres de Fermat. Fermat avait vérifié que \( {2}^{{2}^{n}} + 1 \) était premier pour \( 0 \leq  n \leq  4 \) et pensait que \( {2}^{{2}^{n}} + 1 \) était premier pour tout \( n \) . Mais Euler montra que \( {2}^{{2}^{5}} + 1 = \) 641 × 6700417, et on a jusqu'ici trouvé aucun autre nombre de Fermat premier. On ne sait même pas s'il y en a ! Le sujet d'étude 2 page 49 donne un test de primalité simple des nombres de Fermat.

- Fermat numbers. Fermat had verified that \( {2}^{{2}^{n}} + 1 \) was prime for \( 0 \leq  n \leq  4 \) and thought that \( {2}^{{2}^{n}} + 1 \) was prime for all \( n \). But Euler showed that \( {2}^{{2}^{5}} + 1 = \) 641 × 6700417, and so far no other prime Fermat number has been found. We do not even know if there are any! Study topic 2 on page 49 provides a simple primality test for Fermat numbers.

> EXERCICE 5. Soit \( A \) la somme des chiffres de \( {4444}^{4444} \) (écrit dans le système décimal) et \( B \) la somme des chiffres de \( A \) . Que vaut \( C \) , la somme des chiffres de \( B \) ?

EXERCISE 5. Let \( A \) be the sum of the digits of \( {4444}^{4444} \) (written in the decimal system) and \( B \) be the sum of the digits of \( A \). What is the value of \( C \), the sum of the digits of \( B \)?

> Solution. L'exercice repose essentiellement sur la remarque suivante.

Solution. The exercise relies essentially on the following remark.

> Tout entier naturel \( N \) est congru à la somme de ses chiffres (en base 10) modulo 9.

Every natural number \( N \) is congruent to the sum of its digits (in base 10) modulo 9.

> En effet. On peut écrire \( N = {a}_{0} + {a}_{1} \cdot {10} + \cdots + {a}_{p} \cdot {10}^{p} \) , où les \( {a}_{i} \) sont des entiers compris entre 0 et 9 . La congruence 10 \( \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) entraîne \( {10}^{i} \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) pour tout \( i \) donc

Indeed. We can write \( N = {a}_{0} + {a}_{1} \cdot {10} + \cdots + {a}_{p} \cdot {10}^{p} \), where the \( {a}_{i} \) are integers between 0 and 9. The congruence 10 \( \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) implies \( {10}^{i} \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) for all \( i \), therefore

\[
N = \mathop{\sum }\limits_{{i = 0}}^{p}{a}_{i}{10}^{i} \equiv  \mathop{\sum }\limits_{{i = 0}}^{p}{a}_{i}\;\left( {\;\operatorname{mod}\;9}\right) .
\]

On applique maintenant ce résultat. On a \( C \equiv B \equiv A \equiv {4444}^{4444} \) (mod 9). D’après (*), \( {4444} \equiv {16} \equiv - 2\left( {\;\operatorname{mod}\;9}\right) \) donc \( {4444}^{3} \equiv {\left( -2\right) }^{3} \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) , et comme \( {4444} = 3 \cdot {1481} + 1 \) , on a \( {4444}^{4444} = {\left( {4444}^{3}\right) }^{1481} \cdot {4444} \equiv 1 \cdot \left( {-2}\right) \equiv 7\left( {\;\operatorname{mod}\;9}\right) \) . Finalement,

> We now apply this result. We have \( C \equiv B \equiv A \equiv {4444}^{4444} \) (mod 9). According to (*), \( {4444} \equiv {16} \equiv - 2\left( {\;\operatorname{mod}\;9}\right) \) therefore \( {4444}^{3} \equiv {\left( -2\right) }^{3} \equiv 1\left( {\;\operatorname{mod}\;9}\right) \) , and since \( {4444} = 3 \cdot {1481} + 1 \) , we have \( {4444}^{4444} = {\left( {4444}^{3}\right) }^{1481} \cdot {4444} \equiv 1 \cdot \left( {-2}\right) \equiv 7\left( {\;\operatorname{mod}\;9}\right) \) . Finally,

\[
C \equiv  7\left( {\;\operatorname{mod}\;9}\right) .
\]

\( \left( {* * }\right) \)

> Majorons maintenant \( C \) de manière à montrer \( C = 7 \) . Le nombre \( {4444}^{4444} \) étant inférieur à \( {10000}^{5000} = {10}^{20000} \) , il a au plus 20000 chiffres. Donc \( A \) vaut au plus \( 9 \times {20000} = {180000} \) , donc a au plus 6 chiffres, donc \( B \) vaut au plus \( 6 \times 9 = {54} \) , donc \( C \leq 5 + 9 = {14} \) . De (**), on tire \( C = 7 \) .

Let us now bound \( C \) so as to show \( C = 7 \) . Since the number \( {4444}^{4444} \) is less than \( {10000}^{5000} = {10}^{20000} \) , it has at most 20,000 digits. Thus \( A \) is at most \( 9 \times {20000} = {180000} \) , so it has at most 6 digits, thus \( B \) is at most \( 6 \times 9 = {54} \) , so \( C \leq 5 + 9 = {14} \) . From (**), we derive \( C = 7 \) .

> Remarque. C'est la propriété (*) qui explique le principe de la preuve par 9 que l'on effectue dans les classes de l'école primaire.

Remark. It is property (*) that explains the principle of casting out nines used in primary school classrooms.

> EXERCICE 6. Soit \( P = {X}^{n} + {c}_{1}{X}^{n - 1} + \cdots + {c}_{n - 1}X + {c}_{n} \) un polynôme à coefficients entiers. Montrer qu’une racine rationnelle de \( P \) est nécessairement entière.

EXERCISE 6. Let \( P = {X}^{n} + {c}_{1}{X}^{n - 1} + \cdots + {c}_{n - 1}X + {c}_{n} \) be a polynomial with integer coefficients. Show that a rational root of \( P \) is necessarily an integer.

> Solution. Soit \( x = a/b \) une racine rationnelle de \( P\left( {a \in \mathbb{Z}, b \in {\mathbb{N}}^{ * }, a \land b = 1}\right) \) . On a

Solution. Let \( x = a/b \) be a rational root of \( P\left( {a \in \mathbb{Z}, b \in {\mathbb{N}}^{ * }, a \land b = 1}\right) \) . We have

\[
0 = {b}^{n}P\left( \frac{a}{b}\right)  = {a}^{n} + {c}_{1}{a}^{n - 1}b + \cdots  + {c}_{n - 1}a{b}^{n - 1} + {c}_{n}{b}^{n}
\]

done

> therefore

\[
{a}^{n} =  - b\left( {{c}_{1}{a}^{n - 1} + \cdots  + {c}_{n - 1}a{b}^{n - 2} + {c}_{n}{b}^{n - 1}}\right) ,
\]

ce qui montre que \( b \) divise \( {a}^{n} \) . Les entiers \( a \) et \( b \) étant premiers entre eux, ceci n’est possible que si \( b = 1 \) , d’où le résultat.

> which shows that \( b \) divides \( {a}^{n} \) . Since the integers \( a \) and \( b \) are coprime, this is only possible if \( b = 1 \) , hence the result.

Remarque. On en déduit en particulier que la racine \( n \) -ième de tout entier \( N \) est soit entière, soit irrationnelle (considérer le polynôme \( {X}^{n} - N \) ).

> Remark. We deduce in particular that the \( n \) -th root of any integer \( N \) is either an integer or irrational (consider the polynomial \( {X}^{n} - N \) ).

EXERCICE 7. Montrer qu’il y a une infinité de nombres premiers de la forme \( {6k} - 1 \) , \( k \in {\mathbb{N}}^{ * } \) .

> EXERCISE 7. Show that there are infinitely many prime numbers of the form \( {6k} - 1 \) , \( k \in {\mathbb{N}}^{ * } \) .

Solution. Raisonnons par l'absurde en supposant qu'il n'y en ait qu'un nombre fini. Désignons par \( N \) le plus grand d’entre eux. L’entier \( M = - 1 + 6\left( {N!}\right) \) est impair donc \( 2 \nmid M \) . De même, \( M \equiv - 1\left( {\;\operatorname{mod}\;3}\right) \) donc \( 3 \nmid M \) .

> Solution. Let us reason by contradiction by assuming that there is only a finite number of them. Let \( N \) denote the largest among them. The integer \( M = - 1 + 6\left( {N!}\right) \) is odd, so \( 2 \nmid M \) . Similarly, \( M \equiv - 1\left( {\;\operatorname{mod}\;3}\right) \) so \( 3 \nmid M \) .

Soit \( p \) un facteur premier de \( M \) . Si \( p \) est de la forme \( {6k} - 1 \) , alors \( p \leq N \) donc \( p \mid \left( {6 \cdot N!}\right) \) , d’où \( p \mid \left( {{6N}! - M}\right) = 1 \) , ce qui est impossible. Le nombre \( p \) n’est donc pas de la forme \( {6k} - 1 \) . De plus \( p \notin \{ 2,3\} \) comme on l’a vu plus haut, donc \( p \) est de la forme \( {6k} + 1, k \in {\mathbb{N}}^{ * } \) . Dans la décomposition \( M = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{n}^{{\alpha }_{n}} \) de \( M \) en facteurs premiers, on a donc \( {p}_{i} \equiv 1\left( {\;\operatorname{mod}\;6}\right) \) pour tout \( i \) , d’où \( M \equiv 1\left( {\;\operatorname{mod}\;6}\right) \) , ce qui est absurde car \( M \equiv - 1\left( {\;\operatorname{mod}\;6}\right) \) par construction.

> Let \( p \) be a prime factor of \( M \) . If \( p \) is of the form \( {6k} - 1 \) , then \( p \leq N \) so \( p \mid \left( {6 \cdot N!}\right) \) , hence \( p \mid \left( {{6N}! - M}\right) = 1 \) , which is impossible. The number \( p \) is therefore not of the form \( {6k} - 1 \) . Furthermore \( p \notin \{ 2,3\} \) as seen above, so \( p \) is of the form \( {6k} + 1, k \in {\mathbb{N}}^{ * } \) . In the prime factorization \( M = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{n}^{{\alpha }_{n}} \) of \( M \) , we therefore have \( {p}_{i} \equiv 1\left( {\;\operatorname{mod}\;6}\right) \) for all \( i \) , hence \( M \equiv 1\left( {\;\operatorname{mod}\;6}\right) \) , which is absurd because \( M \equiv - 1\left( {\;\operatorname{mod}\;6}\right) \) by construction.

Remarque. On peut démontrer de la même manière qu'il y a une infinité de nombres premiers de la forme \( {4k} - 1 \) . Il existe un théorème plus général (théorème de Dirichlet, 1837) qui dit :

> Remark. One can demonstrate in the same way that there are infinitely many prime numbers of the form \( {4k} - 1 \) . There exists a more general theorem (Dirichlet's theorem, 1837) which states:

\( \forall \left( {a, b}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}, a \land b = 1 \) , il existe une infinité de nombres premiers de la forme ak + b, \( k \in \mathbb{N} \) .

> \( \forall \left( {a, b}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{2}, a \land b = 1 \) , there exist infinitely many prime numbers of the form ak + b, \( k \in \mathbb{N} \) .

Malheureusement, ce résultat n'a encore jamais pu être obtenu par des moyens élémen-taires et simples. On peut cependant le démontrer dans certains cas particuliers (voir le problème 5 page 40, la partie 6 / du sujet d'étude 2 page 49 ou le problème 11 page 99).

> Unfortunately, this result has never yet been obtained by elementary and simple means. It can, however, be proven in certain special cases (see problem 5 page 40, part 6 / of study topic 2 page 49 or problem 11 page 99).

En notant \( {\pi }_{a, b}\left( x\right) \) le nombre de nombres premiers \( \leq x \) de la forme \( {ak} + b \) , le théorème de Dirichlet assure également que lorsque \( a \land b = 1 \) , on a \( {\pi }_{a, b}\left( x\right) { \sim }_{x \rightarrow + \infty }\pi \left( x\right) /\varphi \left( a\right) \) (où \( \pi \left( x\right) \) désigne le nombre de nombres premiers \( \leq x \) et \( \varphi \left( a\right) \) l’indicateur d’Euler de \( a) \) .

> By denoting \( {\pi }_{a, b}\left( x\right) \) as the number of prime numbers \( \leq x \) of the form \( {ak} + b \) , Dirichlet's theorem also ensures that when \( a \land b = 1 \) , we have \( {\pi }_{a, b}\left( x\right) { \sim }_{x \rightarrow + \infty }\pi \left( x\right) /\varphi \left( a\right) \) (where \( \pi \left( x\right) \) denotes the number of prime numbers \( \leq x \) and \( \varphi \left( a\right) \) the Euler totient function of \( a) \) .

EXERCICE 8. a) Montrer qu'il n'existe pas de polynôme \( P \) non constant à coefficients entiers, tel que \( P\left( n\right) \) soit premier pour tout entier \( n \) supérieur à un certain rang \( N \) .

> EXERCISE 8. a) Show that there is no non-constant polynomial \( P \) with integer coefficients such that \( P\left( n\right) \) is prime for every integer \( n \) greater than a certain rank \( N \) .

b) On considère un polynôme \( P \) à \( k \) variables et à coefficients entiers. On pose \( f\left( n\right) = \; P\left( {n,{2}^{n},{3}^{n},\ldots ,{k}^{n}}\right) \) , et on suppose \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( n\right) = + \infty \) (ceci pour éviter des fonctions comme \( f\left( n\right) = {2}^{n}{5}^{n} - {10}^{n} + 7 \) ). Montrer que \( f\left( n\right) \) ne peut pas être un nombre premier pour tout entier \( n \) supérieur à un certain rang \( N \) .

> b) Consider a polynomial \( P \) in \( k \) variables with integer coefficients. Let \( f\left( n\right) = \; P\left( {n,{2}^{n},{3}^{n},\ldots ,{k}^{n}}\right) \) , and assume \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( n\right) = + \infty \) (this is to avoid functions like \( f\left( n\right) = {2}^{n}{5}^{n} - {10}^{n} + 7 \) ). Show that \( f\left( n\right) \) cannot be a prime number for every integer \( n \) greater than a certain rank \( N \) .

Solution. a) Supposons qu’un tel polynôme existe. Écrivons \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) . L’entier \( p = \; P\left( N\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{N}^{k} \) est premier. Or tout entier naturel \( r \) vérifie

> Solution. a) Suppose such a polynomial exists. Let us write \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) . The integer \( p = \; P\left( N\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{N}^{k} \) is prime. However, any natural number \( r \) satisfies

\[
P\left( {N + {rp}}\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{\left( N + rp\right) }^{k} \equiv  \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{N}^{k} \equiv  0\;\left( {\;\operatorname{mod}\;p}\right) ,
\]

autrement dit \( P\left( {N + {rp}}\right) \) est divisible par \( p \) pour tout entier naturel \( r \) . Comme \( P\left( {N + {rp}}\right) \) est premier, on a \( P\left( {N + {rp}}\right) = p \) pour tout entier naturel \( r \) . Ainsi, le polynôme \( P\left( X\right) - p \) a une infinité de racines, il est donc nul, ce qui est contraire aux hypothèses.

> in other words \( P\left( {N + {rp}}\right) \) is divisible by \( p \) for any natural number \( r \) . Since \( P\left( {N + {rp}}\right) \) is prime, we have \( P\left( {N + {rp}}\right) = p \) for any natural number \( r \) . Thus, the polynomial \( P\left( X\right) - p \) has infinitely many roots, so it is zero, which contradicts the hypotheses.

b) Supposons l'existence d'une telle fonction. Un peu d'attention montre que \( f \) peut se mettre sous la forme

> b) Suppose such a function exists. A little attention shows that \( f \) can be written in the form

\[
f\left( n\right)  = \mathop{\sum }\limits_{{r = 1}}^{m}\left( {\mathop{\sum }\limits_{{s = 0}}^{{q}_{r}}{c}_{r, s}{n}^{s}}\right) {a}_{r}^{n},
\]

où les \( {a}_{r} \) et \( {c}_{r, s} \) sont entiers, avec \( 1 \leq {a}_{1} < {a}_{2} < \cdots < {a}_{m} \) . Comme \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( n\right) = + \infty \) , on peut supposer \( f\left( N\right) > {a}_{m} > \cdots > {a}_{1} \geq 1 \) (quitte à augmenter \( N \) ). Notons \( p \) le nombre premier \( p = f\left( N\right) \) . On a

> where \( {a}_{r} \) and \( {c}_{r, s} \) are integers, with \( 1 \leq {a}_{1} < {a}_{2} < \cdots < {a}_{m} \) . Since \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( n\right) = + \infty \) , we can assume \( f\left( N\right) > {a}_{m} > \cdots > {a}_{1} \geq 1 \) (by increasing \( N \) if necessary). Let \( p \) be the prime number \( p = f\left( N\right) \) . We have

\[
\forall \ell  \in  \mathbb{N},\forall s \in  \mathbb{N},\;{\left\lbrack  N + \ell p\left( p - 1\right) \right\rbrack  }^{s} \equiv  {N}^{s}\;\left( {\;\operatorname{mod}\;p}\right) ,
\]

et d’après le théorème de Fermat, lorsque \( 1 \leq r \leq m \) on a

> and according to Fermat's theorem, when \( 1 \leq r \leq m \) we have

\[
{a}_{r}^{p - 1} \equiv  1\;\left( {\;\operatorname{mod}\;p}\right) \;\text{ donc }\;\forall \ell  \in  \mathbb{N},\;{a}_{r}^{N + \ell p\left( {p - 1}\right) } \equiv  {a}_{r}^{N}\;\left( {\;\operatorname{mod}\;p}\right) .
\]

Finalement,

> Finally,

\[
\forall \ell  \in  \mathbb{N},\;{\left\lbrack  N + \ell p\left( p - 1\right) \right\rbrack  }^{s}{a}_{r}^{N + \ell p\left( {p - 1}\right) } \equiv  {N}^{s}{a}_{r}^{N}\;\left( {\;\operatorname{mod}\;p}\right) ,
\]

et ceci pour tous les entiers \( r, s \) donc \( f\left\lbrack {N + \ell p\left( {p - 1}\right) }\right\rbrack \equiv f\left( N\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) . Ceci étant vrai pour tout entier naturel \( \ell \) , on aboutit à une absurdité.

> and this for all integers \( r, s \) so \( f\left\lbrack {N + \ell p\left( {p - 1}\right) }\right\rbrack \equiv f\left( N\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) . Since this is true for any natural number \( \ell \) , we arrive at an absurdity.

EXERCICE 9. Pour tout entier naturel \( n \) , on pose \( {F}_{n} = {2}^{{2}^{n}} + 1 \) (nombres de Fermat). a) Montrer que les nombres \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) sont premiers entre eux deux à deux. b) En déduire une autre démonstration du fait qu'il y a une infinité de nombres premiers.

> EXERCISE 9. For any natural number \( n \) , let \( {F}_{n} = {2}^{{2}^{n}} + 1 \) (Fermat numbers). a) Show that the numbers \( {\left( {F}_{n}\right) }_{n \in \mathbb{N}} \) are pairwise coprime. b) Deduce another proof of the fact that there are infinitely many prime numbers.

Solution. a) Si \( n \in \mathbb{N}, k \in {\mathbb{N}}^{ * } \) , il s’agit de montrer que \( {F}_{n} \) et \( {F}_{n + k} \) sont premiers entre eux. La relation

> Solution. a) If \( n \in \mathbb{N}, k \in {\mathbb{N}}^{ * } \) , it is a matter of showing that \( {F}_{n} \) and \( {F}_{n + k} \) are coprime. The relation

\[
{F}_{n + k} - 1 = {2}^{{2}^{n + k}} = {\left( {2}^{{2}^{n}}\right) }^{{2}^{k}} = {\left( {F}_{n} - 1\right) }^{{2}^{k}}
\]

entraîne

> implies

\[
{F}_{n + k} - 1 \equiv  {\left( {F}_{n} - 1\right) }^{{2}^{k}} \equiv  {\left( -1\right) }^{{2}^{k}} \equiv  1\;\left( {\;\operatorname{mod}\;{F}_{n}}\right)
\]

donc \( {F}_{n} \mid \left( {{F}_{n + k} - 2}\right) \) . Ainsi, le pgcd \( d \) de \( {F}_{n} \) et \( {F}_{n + k} \) divise \( {F}_{n + k} - 2 \) . Comme de plus \( d \mid {F}_{n + k} \) , \( d \) divise 2, et \( {F}_{n} \) étant impair, on a nécessairement \( d = 1 \) .

> therefore \( {F}_{n} \mid \left( {{F}_{n + k} - 2}\right) \) . Thus, the gcd \( d \) of \( {F}_{n} \) and \( {F}_{n + k} \) divides \( {F}_{n + k} - 2 \) . Since, in addition, \( d \mid {F}_{n + k} \) , \( d \) divides 2, and since \( {F}_{n} \) is odd, we necessarily have \( d = 1 \) .

b) Pour tout \( n \in \mathbb{N} \) , notons \( {p}_{n} \) un facteur premier de \( {F}_{n} \) . Les \( {F}_{n} \) étant premiers entre eux deux à deux, les \( {\left( {p}_{n}\right) }_{n \in \mathbb{N}} \) sont distincts deux à deux. On a donc trouvé une infinité de nombres premiers.

> b) For any \( n \in \mathbb{N} \) , let \( {p}_{n} \) denote a prime factor of \( {F}_{n} \) . Since the \( {F}_{n} \) are pairwise coprime, the \( {\left( {p}_{n}\right) }_{n \in \mathbb{N}} \) are pairwise distinct. We have therefore found an infinite number of primes.

Remarque. Profitons en ici pour rappeler quelques résultats dans l'histoire des nombres premiers. Les grecs savaient déjà qu'il y en avait une infinité. Le gros résultat suivant fut le théorème des nombres premiers.

> Remark. Let us take this opportunity to recall some results in the history of prime numbers. The Greeks already knew that there were infinitely many. The next major result was the prime number theorem.

Si \( \forall x > 0,\pi \left( x\right) \) désigne le nombre de nombres premiers inférieurs à \( x \) ,

> If \( \forall x > 0,\pi \left( x\right) \) denotes the number of prime numbers less than \( x \) ,

on a \( \pi \left( x\right) \sim x/\log \left( x\right) \) lorsque \( x \) tend vers l’infini.

> we have \( \pi \left( x\right) \sim x/\log \left( x\right) \) as \( x \) tends to infinity.

Il fut démontré pour la première fois et presque simultanément par J. Hadamard et C. De la Vallée Poussin en 1896. Les démonstrations les plus classiques de ce résultat font appel à la fonction \( \zeta \) de Riemann. Une preuve en est proposée en annexe du tome d’Analyse (à partir de la deuxième édition).

> It was proven for the first time and almost simultaneously by J. Hadamard and C. De la Vallée Poussin in 1896. The most classical proofs of this result use the Riemann \( \zeta \) function. A proof is provided in the appendix of the Analysis volume (starting from the second edition).

EXERCICE 10 (NOMBRES PARFAITS). 1/a) Pour tout entier naturel non nul \( n \) , on note \( \sigma \left( n\right) \) la somme des diviseurs de \( n \) . Exprimer \( \sigma \left( n\right) \) en fonction des termes intervenant dans la décomposition de \( n \) en facteurs premiers. Montrer que

> EXERCISE 10 (PERFECT NUMBERS). 1/a) For any non-zero natural number \( n \) , let \( \sigma \left( n\right) \) denote the sum of the divisors of \( n \) . Express \( \sigma \left( n\right) \) in terms of the factors in the prime factorization of \( n \) . Show that

\[
n \land  m = 1 \Rightarrow  \sigma \left( {nm}\right)  = \sigma \left( n\right) \sigma \left( m\right) .
\]

(*)

> b) On dit qu'un entier naturel non nul \( n \) est parfait s’il est égal à la somme de ses diviseurs autres que lui même (i.e. si \( \sigma \left( n\right) = {2n} \) ). Si \( {2}^{p} - 1 \) est un nombre premier, montrer que \( n = {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) est un nombre parfait.

b) A non-zero natural number \( n \) is said to be perfect if it is equal to the sum of its divisors other than itself (i.e., if \( \sigma \left( n\right) = {2n} \) ). If \( {2}^{p} - 1 \) is a prime number, show that \( n = {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) is a perfect number.

> c) Réciproquement, démontrer qu’un nombre parfait pair \( n \) est de la forme \( {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) , où \( {2}^{p} - 1 \) est nécessairement un nombre premier.

c) Conversely, prove that an even perfect number \( n \) is of the form \( {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) , where \( {2}^{p} - 1 \) is necessarily a prime number.

> 2/ (Nombres parfaits impairs). a) (Théorème d'Euler). Montrer que s'il existe un nombre parfait impair \( n \) , alors il est nécessairement de la forme

2/ (Odd perfect numbers). a) (Euler's Theorem). Show that if an odd perfect number \( n \) exists, then it is necessarily of the form

\[
n = {p}^{1 + {4\alpha }}{Q}^{2}\text{ avec }\;p\text{ premier, }p \equiv  1\;\left( {\;\operatorname{mod}\;4}\right) ,\alpha  \in  \mathbb{N}\text{ , et }Q \in  {\mathbb{N}}^{ * }\text{ avec }p \land  Q = 1.
\]

(Indication : à partir de la décomposition en facteurs premiers \( n = \prod {p}_{i}^{{\alpha }_{i}} \) ,étudier la valeur de \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \) modulo 4.)

> (Hint: starting from the prime factorization \( n = \prod {p}_{i}^{{\alpha }_{i}} \) , study the value of \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \) modulo 4.)

b) Montrer qu'un nombre parfait impair a au moins 3 facteurs premiers distincts.

> b) Show that an odd perfect number has at least 3 distinct prime factors.

Solution. 1/a) Si \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) est la décomposition de \( n \) en facteurs premiers, on a

> Solution. 1/a) If \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) is the prime factorization of \( n \) , we have

\[
\sigma \left( n\right)  = \mathop{\sum }\limits_{\substack{{0 \leq  {\beta }_{1} \leq  {\alpha }_{1}} \\  {0 \leq  {\beta }_{k} \leq  {\alpha }_{k}} }}{p}_{1}^{{\beta }_{1}}{p}_{2}^{{\beta }_{2}}\cdots {p}_{k}^{{\beta }_{k}} = \mathop{\prod }\limits_{{i = 1}}^{k}\left( {1 + {p}_{i} + \cdots  + {p}_{i}^{{\alpha }_{i}}}\right)  = \mathop{\prod }\limits_{{i = 1}}^{k}\left( \frac{{p}_{i}^{{\alpha }_{i} + 1} - 1}{{p}_{i} - 1}\right) .
\]

La propriété (*) en découle immédiatement.

> Property (*) follows immediately.

b) On applique les résultats de la question précédente pour écrire

> b) We apply the results from the previous question to write

\[
\sigma \left( n\right)  = \sigma \left\lbrack  {{2}^{p - 1}\left( {{2}^{p} - 1}\right) }\right\rbrack   = \sigma \left( {2}^{p - 1}\right) \sigma \left( {{2}^{p} - 1}\right)  = \left( {{2}^{p} - 1}\right) {2}^{p} = {2n}.
\]

c) La réciproque est plus délicate. Comme \( n \) est pair, il existe un entier \( p \geq 2 \) tel que \( n = \; {2}^{p - 1}m \) avec \( m \) impair. Le fait que \( {2}^{p - 1} \land m = 1 \) nous autorise à utiliser (*), de sorte que \( \sigma \left( n\right) = \sigma \left( {2}^{p - 1}\right) \sigma \left( m\right) = \left( {{2}^{p} - 1}\right) \sigma \left( m\right) \) . Or \( \sigma \left( n\right) = {2n} = {2}^{p}m \) donc \( \left( {{2}^{p} - 1}\right) \mid {2}^{p}m \) , et comme \( \left( {{2}^{p} - 1}\right) \land {2}^{p} = 1 \) , d’après le théorème de Gauss on a \( \left( {{2}^{p} - 1}\right) \mid m \) . Autrement dit, il existe \( \ell \in {\mathbb{N}}^{ * } \) tel que \( m = \left( {{2}^{p} - 1}\right) \ell \) . La relation \( {2}^{p}m = {2n} = \sigma \left( n\right) = \left( {{2}^{p} - 1}\right) \sigma \left( m\right) \) entraîne \( \sigma \left( m\right) = {2}^{p}\ell = m + \ell \) .

> c) The converse is more delicate. Since \( n \) is even, there exists an integer \( p \geq 2 \) such that \( n = \; {2}^{p - 1}m \) with \( m \) odd. The fact that \( {2}^{p - 1} \land m = 1 \) allows us to use (*), so that \( \sigma \left( n\right) = \sigma \left( {2}^{p - 1}\right) \sigma \left( m\right) = \left( {{2}^{p} - 1}\right) \sigma \left( m\right) \) . However, \( \sigma \left( n\right) = {2n} = {2}^{p}m \) so \( \left( {{2}^{p} - 1}\right) \mid {2}^{p}m \) , and since \( \left( {{2}^{p} - 1}\right) \land {2}^{p} = 1 \) , by Gauss's theorem we have \( \left( {{2}^{p} - 1}\right) \mid m \) . In other words, there exists \( \ell \in {\mathbb{N}}^{ * } \) such that \( m = \left( {{2}^{p} - 1}\right) \ell \) . The relation \( {2}^{p}m = {2n} = \sigma \left( n\right) = \left( {{2}^{p} - 1}\right) \sigma \left( m\right) \) leads to \( \sigma \left( m\right) = {2}^{p}\ell = m + \ell \) .

Si \( \ell > 1, m \) a au moins trois diviseurs distincts qui sont \( 1,\ell \) et \( m \) , d’où \( \sigma \left( m\right) \geq m + \ell + 1 \) , ce qui est absurde. Donc \( \ell = 1, m = {2}^{p} - 1 \) et \( \sigma \left( m\right) = m + \ell = m + 1 \) ; on en déduit que les seuls diviseurs de \( m \) sont 1 et \( m \) , donc \( m \) est un nombre premier. En résumé, on doit avoir \( n = {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) où \( {2}^{p} - 1 \) est un nombre premier.

> If \( \ell > 1, m \) has at least three distinct divisors which are \( 1,\ell \) and \( m \) , hence \( \sigma \left( m\right) \geq m + \ell + 1 \) , which is absurd. Therefore \( \ell = 1, m = {2}^{p} - 1 \) and \( \sigma \left( m\right) = m + \ell = m + 1 \) ; we deduce that the only divisors of \( m \) are 1 and \( m \) , so \( m \) is a prime number. In summary, we must have \( n = {2}^{p - 1}\left( {{2}^{p} - 1}\right) \) where \( {2}^{p} - 1 \) is a prime number.

2/a) Considérons la décomposition de \( n \) en facteurs premiers \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) . D’après 1/a), on a \( \sigma \left( n\right) = \sigma \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \sigma \left( {p}_{k}^{{\alpha }_{k}}\right) \) . Comme \( n \) est un nombre impair, on a \( {2n} \equiv 2\left( {\;\operatorname{mod}\;4}\right) \) . Si \( n \) est parfait, alors \( \sigma \left( n\right) = {2n} \) donc \( \sigma \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \sigma \left( {p}_{k}^{{\alpha }_{k}}\right) \equiv 2\left( {\;\operatorname{mod}\;4}\right) \) . Ceci implique forcément qu’il existe un et un seul indice \( i \) pour lequel \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \equiv 2\left( {\;\operatorname{mod}\;4}\right) \) et que les autres vérifient \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \equiv \pm 1\left( {\;\operatorname{mod}\;4}\right) \) . Quitte à renuméroter les \( {p}_{i} \) , on peut donc supposer que

> 2/a) Consider the prime factorization of \( n \) as \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \). According to 1/a), we have \( \sigma \left( n\right) = \sigma \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \sigma \left( {p}_{k}^{{\alpha }_{k}}\right) \). Since \( n \) is an odd number, we have \( {2n} \equiv 2\left( {\;\operatorname{mod}\;4}\right) \). If \( n \) is perfect, then \( \sigma \left( n\right) = {2n} \) so \( \sigma \left( {p}_{1}^{{\alpha }_{1}}\right) \cdots \sigma \left( {p}_{k}^{{\alpha }_{k}}\right) \equiv 2\left( {\;\operatorname{mod}\;4}\right) \). This necessarily implies that there exists one and only one index \( i \) for which \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \equiv 2\left( {\;\operatorname{mod}\;4}\right) \) and that the others satisfy \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) \equiv \pm 1\left( {\;\operatorname{mod}\;4}\right) \). By renumbering the \( {p}_{i} \), we can therefore assume that

\[
\sigma \left( {p}_{1}^{{\alpha }_{1}}\right)  \equiv  2\;\left( {\;\operatorname{mod}\;4}\right) \;\text{ et }\;\forall i \geq  2,\sigma \left( {p}_{i}^{{\alpha }_{i}}\right)  \equiv   \pm  1\;\left( {\;\operatorname{mod}\;4}\right) .
\]

\( \left( {* * }\right) \)

> Les \( {p}_{i} \) sont des nombres premiers impairs car \( n \) est impair. Nous traitons deux cas selon que \( {p}_{i} \equiv - 1 \) ou 1 (mod 4).

The \( {p}_{i} \) are odd prime numbers because \( n \) is odd. We treat two cases depending on whether \( {p}_{i} \equiv - 1 \) or 1 (mod 4).

> (i) Si \( {p}_{i} \equiv - 1\left( {\;\operatorname{mod}\;4}\right) \) , alors l’égalité \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) = 1 + {p}_{i} + \cdots + {p}_{i}^{{\alpha }_{i}} \) entraîne

(i) If \( {p}_{i} \equiv - 1\left( {\;\operatorname{mod}\;4}\right) \), then the equality \( \sigma \left( {p}_{i}^{{\alpha }_{i}}\right) = 1 + {p}_{i} + \cdots + {p}_{i}^{{\alpha }_{i}} \) leads to

\[
\sigma \left( {p}_{i}^{{\alpha }_{i}}\right)  \equiv  1 + \left( {-1}\right)  + \cdots  + {\left( -1\right) }^{{\alpha }_{i}} \equiv  \left\{  \begin{array}{lll} 0 & \left( {\;\operatorname{mod}\;4}\right) & \text{ si }{\alpha }_{i}\text{ est impair, } \\  1 & \left( {\;\operatorname{mod}\;4}\right) & \text{ si }{\alpha }_{i}\text{ est pair. } \end{array}\right.
\]

D’après \( \left( {* * }\right) \) on en déduit \( i \geq 2 \) et \( {\alpha }_{i} \) est forcément un nombre pair.

> According to \( \left( {* * }\right) \), we deduce \( i \geq 2 \) and \( {\alpha }_{i} \) is necessarily an even number.

(ii) Lorsque \( {p}_{i} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) , on a

> (ii) When \( {p}_{i} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \), we have

\[
\sigma \left( {p}_{i}^{{\alpha }_{i}}\right)  = 1 + {p}_{i} + \cdots  + {p}_{i}^{{\alpha }_{i}} \equiv  {\alpha }_{i} + 1\;\left( {\;\operatorname{mod}\;4}\right) .
\]

Avec (**), on en déduit que \( {\alpha }_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) et que \( {\alpha }_{i} \) est pair pour \( i \geq 2 \) .

> With (**), we deduce that \( {\alpha }_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) and that \( {\alpha }_{i} \) is even for \( i \geq 2 \).

En résumé, on a forcément \( {p}_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) ,{\alpha }_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) et dans tous les cas, \( {\alpha }_{i} \) est pair lorsque \( i \geq 2 \) . Le résultat en découle avec \( p = {p}_{1},\alpha = \left( {{\alpha }_{1} - 1}\right) /4 \) et \( Q = {p}_{2}^{{\alpha }_{2}/2}\cdots {p}_{k}^{{\alpha }_{k}/2} \) .

> In summary, we necessarily have \( {p}_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) ,{\alpha }_{1} \equiv 1\left( {\;\operatorname{mod}\;4}\right) \) and in all cases, \( {\alpha }_{i} \) is even when \( i \geq 2 \). The result follows with \( p = {p}_{1},\alpha = \left( {{\alpha }_{1} - 1}\right) /4 \) and \( Q = {p}_{2}^{{\alpha }_{2}/2}\cdots {p}_{k}^{{\alpha }_{k}/2} \).

b) Soit \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) la décomposition en facteurs premiers de \( n \) , avec \( {p}_{1} < {p}_{2} < \ldots < {p}_{k} \) . Si \( n \) est parfait, l’égalité \( \sigma \left( n\right) = {2n} \) entraîne

> b) Let \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) be the prime factorization of \( n \), with \( {p}_{1} < {p}_{2} < \ldots < {p}_{k} \). If \( n \) is perfect, the equality \( \sigma \left( n\right) = {2n} \) leads to

\[
2 = \frac{\sigma \left( n\right) }{n} = \mathop{\prod }\limits_{{i = 1}}^{k}\frac{\sigma \left( {p}_{i}^{{\alpha }_{i}}\right) }{{p}_{i}^{{\alpha }_{i}}} = \mathop{\prod }\limits_{{i = 1}}^{k}\left( {1 + \frac{1}{{p}_{i}} + \cdots  + \frac{1}{{p}_{i}^{{\alpha }_{i}}}}\right)  \leq  \mathop{\prod }\limits_{{i = 1}}^{k}\frac{1}{1 - 1/{p}_{i}}.
\]

\( \left( {* * * }\right) \)

> Si \( k = 1 \) , on a \( {p}_{1} \geq 3 \) et \( \left( {* * * }\right) \) entraîne \( 2 \leq {\left( 1 - 1/{p}_{1}\right) }^{-1} \leq 3/2 \) ce qui est absurde. Si \( k = 2 \) , alors \( {p}_{1} \geq 3 \) et \( {p}_{2} \geq 5 \) , donc d’après \( \left( {* * * }\right) \) on a \( 2 \leq {\left( 1 - 1/{p}_{1}\right) }^{-1}{\left( 1 - 1/{p}_{2}\right) }^{-1} \leq \left( {3/2}\right) \cdot \left( {5/4}\right) = {15}/8 \) ce qui est absurde. Donc \( k \geq 3 \) .

If \( k = 1 \) , we have \( {p}_{1} \geq 3 \) and \( \left( {* * * }\right) \) implies \( 2 \leq {\left( 1 - 1/{p}_{1}\right) }^{-1} \leq 3/2 \) which is absurd. If \( k = 2 \) , then \( {p}_{1} \geq 3 \) and \( {p}_{2} \geq 5 \) , so according to \( \left( {* * * }\right) \) we have \( 2 \leq {\left( 1 - 1/{p}_{1}\right) }^{-1}{\left( 1 - 1/{p}_{2}\right) }^{-1} \leq \left( {3/2}\right) \cdot \left( {5/4}\right) = {15}/8 \) which is absurd. Therefore \( k \geq 3 \) .

> Remarque. On ne connaît aucun nombre parfait impair, on ne sait même pas s'il y en a. Outre le résultat 2/a), on sait que s'il en existe un alors il a au moins 1500 chiffres décimaux et il a au moins 10 facteurs premiers distincts dont le plus grand est supérieur à \( {10}^{8} \) .

Remark. No odd perfect number is known; it is not even known if any exist. Besides the result in 2/a), it is known that if one exists, it has at least 1500 decimal digits and at least 10 distinct prime factors, the largest of which is greater than \( {10}^{8} \) .

> EXERCICE 11 (THÉORÉME DE LIOUVILLE). Soit \( p > 5 \) un entier. Montrer que l’équation en \( m \in {\mathbb{N}}^{ * } \)

EXERCISE 11 (LIOUVILLE'S THEOREM). Let \( p > 5 \) be an integer. Show that the equation in \( m \in {\mathbb{N}}^{ * } \)

\[
\left( {p - 1}\right) ! + 1 = {p}^{m}
\]

n'a pas de solution.

> has no solution.

Solution. Comme \( p > 5,\left( {p - 1}\right) ! + 1 \) est impair donc \( {p}^{m} \) est impair, donc \( p \) est impair. Or \( p > 5 \) donc \( 2 < \frac{p - 1}{2} < p - 1 \) , d’où

> Solution. Since \( p > 5,\left( {p - 1}\right) ! + 1 \) is odd, \( {p}^{m} \) is odd, so \( p \) is odd. However, \( p > 5 \) so \( 2 < \frac{p - 1}{2} < p - 1 \) , hence

\[
{\left( p - 1\right) }^{2} = 2 \cdot  \left( \frac{p - 1}{2}\right)  \cdot  \left( {p - 1}\right) \;\text{ divise }\;\left( {p - 1}\right) !.
\]

Ceci étant, supposons \( \left( {p - 1}\right) ! + 1 = {p}^{m} \) . Comme \( \left( {p - 1}\right) ! = {p}^{m} - 1,{\left( p - 1\right) }^{2} \) divise \( {p}^{m} - 1 = \; \left( {p - 1}\right) \left( {1 + p + \cdots + {p}^{m - 1}}\right) \) , donc \( \left( {p - 1}\right) \) divise \( 1 + p + \cdots + {p}^{m - 1} \) . Or \( p \equiv 1\left( {{\;\operatorname{mod}\;p} - 1}\right) \) donc \( 1 + p + \cdots + {p}^{m - 1} \equiv m\left( {{\;\operatorname{mod}\;p} - 1}\right) \) , ce qui prouve \( \left( {p - 1}\right) \mid m \) . Ceci montre \( m \geq p - 1 \) donc \( {p}^{m} \geq {p}^{p - 1} > {\left( p - 1\right) }^{p - 1} > \left( {p - 1}\right) ! \) , et finalement \( \left( {p - 1}\right) ! + 1 < {p}^{m} \) et l’équation proposée n’a pas de solution.

> That being said, suppose \( \left( {p - 1}\right) ! + 1 = {p}^{m} \) . Since \( \left( {p - 1}\right) ! = {p}^{m} - 1,{\left( p - 1\right) }^{2} \) divides \( {p}^{m} - 1 = \; \left( {p - 1}\right) \left( {1 + p + \cdots + {p}^{m - 1}}\right) \) , then \( \left( {p - 1}\right) \) divides \( 1 + p + \cdots + {p}^{m - 1} \) . However, \( p \equiv 1\left( {{\;\operatorname{mod}\;p} - 1}\right) \) so \( 1 + p + \cdots + {p}^{m - 1} \equiv m\left( {{\;\operatorname{mod}\;p} - 1}\right) \) , which proves \( \left( {p - 1}\right) \mid m \) . This shows \( m \geq p - 1 \) so \( {p}^{m} \geq {p}^{p - 1} > {\left( p - 1\right) }^{p - 1} > \left( {p - 1}\right) ! \) , and finally \( \left( {p - 1}\right) ! + 1 < {p}^{m} \) and the proposed equation has no solution.

EXERCICE 12 (CRITERE DE FACTORISABILITÉ DES NOMBRES DE MERSENNE). a) Soit \( p \) un nombre premier de la forme \( {4k} + 3 \) avec \( k \in {\mathbb{N}}^{ * } \) . Montrer que \( {2}^{\left( {p - 1}\right) /2} \equiv {\left( -1\right) }^{k + 1} \; \left( {\;\operatorname{mod}\;p}\right) \) .

> EXERCISE 12 (FACTORIZABILITY CRITERION FOR MERSENNE NUMBERS). a) Let \( p \) be a prime number of the form \( {4k} + 3 \) with \( k \in {\mathbb{N}}^{ * } \) . Show that \( {2}^{\left( {p - 1}\right) /2} \equiv {\left( -1\right) }^{k + 1} \; \left( {\;\operatorname{mod}\;p}\right) \) .

b) On rappelle que les nombres de Mersenne sont les nombres de la forme \( {M}_{p} = {2}^{p} - 1 \) où \( p \) est un nombre premier (voir l’exercice 4). Si \( p \) est un nombre premier de la forme \( {4k} + 3\left( {k \in {\mathbb{N}}^{ * }}\right) \) et si \( {2p} + 1 \) est premier, montrer que \( {M}_{p} \) n’est pas premier.

> b) Recall that Mersenne numbers are numbers of the form \( {M}_{p} = {2}^{p} - 1 \) where \( p \) is a prime number (see exercise 4). If \( p \) is a prime number of the form \( {4k} + 3\left( {k \in {\mathbb{N}}^{ * }}\right) \) and if \( {2p} + 1 \) is prime, show that \( {M}_{p} \) is not prime.

Solution. a) Posons

> Solution. a) Let

\[
N = {2}^{\left( {p - 1}\right) /2}\left( \frac{p - 1}{2}\right) ! = {2}^{\left( {p - 1}\right) /2}\left( {{2k} + 1}\right) !.
\]

L’astuce est de donner une autre expression de \( N \) modulo \( p \) . On écrit

> The trick is to provide another expression for \( N \) modulo \( p \). We write

\[
N \equiv  {2}^{\left( {p - 1}\right) /2}\left( {1 \cdot  2\cdots \frac{p - 1}{2}}\right)  \equiv  2 \cdot  4\cdots \left( {p - 1}\right) \;\left( {\;\operatorname{mod}\;p}\right) ,
\]

ou encore

> or

\[
N \equiv  \left( {2 \cdot  4\cdots \left( {2k}\right) }\right)  \cdot  \left( {\left( {{2k} + 2}\right) \cdots \left( {4k}\right)  \cdot  \left( {{4k} + 2}\right) }\right) \;\left( {\;\operatorname{mod}\;p}\right) .
\]

Les congruences

> The congruences

![bo_d7fjffs91nqc73erehlg_18_518_788_515_168_0.jpg](images/gourdon_algebra_probabilities_fr_en_006_bod7fjffs91nqc73erehlg185187885151680.jpg)

entraînent

> imply

\[
\left( {{2k} + 2}\right)  \cdot  \left( {{2k} + 4}\right) \cdots \left( {4k}\right)  \cdot  \left( {{4k} + 2}\right)  \equiv  {\left( -1\right) }^{k + 1}\left( {{2k} + 1}\right)  \cdot  \left( {{2k} - 1}\right) \cdots 3 \cdot  1\;\left( {\;\operatorname{mod}\;p}\right)
\]

donc

> therefore

\[
N \equiv  \left( {2 \cdot  4\cdots \left( {2k}\right) }\right)  \cdot  {\left( -1\right) }^{k + 1}\left( {\left( {{2k} + 1}\right) \cdots 3 \cdot  1}\right) \;\left( {\;\operatorname{mod}\;p}\right) ,
\]

d’où

> whence

\[
{2}^{\left( {p - 1}\right) /2}\left( {{2k} + 1}\right) ! \equiv  N \equiv  {\left( -1\right) }^{k + 1}\left( {{2k} + 1}\right) !\;\left( {\;\operatorname{mod}\;p}\right) ,
\]

d’où le résultat car comme \( p \) est premier et \( {2k} + 1 < p \) , on a \( \left( {{2k} + 1}\right) ! \text{ ≢ } 0\left( {\;\operatorname{mod}\;p}\right) \) .

> hence the result, because as \( p \) is prime and \( {2k} + 1 < p \), we have \( \left( {{2k} + 1}\right) ! \text{ ≢ } 0\left( {\;\operatorname{mod}\;p}\right) \).

b) Supposons \( p = {4k} + 3 \) premier, ainsi que \( q = {2p} + 1 = {8k} + 7 \) . Le résultat précédent appliqué à \( q = 4\left( {{2k} + 1}\right) + 3 \) donne

> b) Suppose \( p = {4k} + 3 \) is prime, as well as \( q = {2p} + 1 = {8k} + 7 \). The previous result applied to \( q = 4\left( {{2k} + 1}\right) + 3 \) gives

\[
{2}^{\left( {q - 1}\right) /2} \equiv  {2}^{p} \equiv  {\left( -1\right) }^{{2k} + 2} \equiv  1\;\left( {\;\operatorname{mod}\;q}\right)
\]

donc \( {2}^{p} - 1 \equiv 0\left( {{\;\operatorname{mod}\;2}p + 1}\right) \) . Autrement dit, \( {2p} + 1 \) divise \( {M}_{p} > {2p} + 1 \) et \( {M}_{p} \) n’est pas premier.

> therefore \( {2}^{p} - 1 \equiv 0\left( {{\;\operatorname{mod}\;2}p + 1}\right) \). In other words, \( {2p} + 1 \) divides \( {M}_{p} > {2p} + 1 \) and \( {M}_{p} \) is not prime.

Remarque. En appliquant b) aux petits nombres premiers, on montre que \( {M}_{p} \) n’est pas un nombre premier pour \( p = {11},{23},{83},{131},{179},{191},{239},{251} \) .

> Remark. By applying b) to small prime numbers, we show that \( {M}_{p} \) is not a prime number for \( p = {11},{23},{83},{131},{179},{191},{239},{251} \).

EXERCICE 13. Résoudre \( {x}^{2} + {y}^{2} = {z}^{2} \) , avec \( \left( {x, y, z}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{3} \) . (Indication : se ramener au cas où \( x, y \) et \( z \) sont premiers entre eux, puis étudier leur parité.)

> EXERCISE 13. Solve \( {x}^{2} + {y}^{2} = {z}^{2} \), with \( \left( {x, y, z}\right) \in {\left( {\mathbb{N}}^{ * }\right) }^{3} \). (Hint: reduce to the case where \( x, y \) and \( z \) are coprime, then study their parity.)

Solution. Quitte à tout diviser par \( \operatorname{pgcd}{\left( x, y, z\right) }^{2} \) , on peut supposer \( x, y \) et \( z \) premiers entre eux dans leur ensemble. On vérifie alors facilement que \( x, y \) et \( z \) sont premiers entre eux deux à deux.

> Solution. By dividing everything by \( \operatorname{pgcd}{\left( x, y, z\right) }^{2} \), we can assume \( x, y \) and \( z \) are coprime as a set. It is then easy to verify that \( x, y \) and \( z \) are pairwise coprime.

- Étudions la parité de \( x, y \) et \( z \) . Tout nombre impair \( N = {2n} + 1 \) vérifie \( {N}^{2} = 4{n}^{2} + {4n} + 1 \equiv  1 \) (mod 4). Donc si \( x \) et \( y \) sont impairs, \( {x}^{2} + {y}^{2} \equiv  2\left( {\;\operatorname{mod}\;4}\right) \) , donc \( z \) est pair et on aboutit à une absurdité car \( {z}^{2} \equiv  0\left( {\;\operatorname{mod}\;4}\right) \) . L’un des entiers \( x \) ou \( y \) est donc pair, par exemple \( x \) . Comme \( x \) , \( y \) et \( z \) sont premiers entre eux deux à deux, \( y \) et \( z \) sont impairs.

> - Let us study the parity of \( x, y \) and \( z \). Any odd number \( N = {2n} + 1 \) satisfies \( {N}^{2} = 4{n}^{2} + {4n} + 1 \equiv  1 \) (mod 4). Thus, if \( x \) and \( y \) are odd, \( {x}^{2} + {y}^{2} \equiv  2\left( {\;\operatorname{mod}\;4}\right) \), so \( z \) is even and we reach an absurdity because \( {z}^{2} \equiv  0\left( {\;\operatorname{mod}\;4}\right) \). One of the integers \( x \) or \( y \) is therefore even, for example \( x \). Since \( x \), \( y \), and \( z \) are pairwise coprime, \( y \) and \( z \) are odd.

- On écrit

> - We write

\[
{\left( \frac{x}{2}\right) }^{2} = \left( \frac{z - y}{2}\right) \left( \frac{z + y}{2}\right)
\]

( \( z \) et \( y \) étant impairs, \( \frac{z - y}{2} \) et \( \frac{z + y}{2} \) sont entiers). Ceci montre que \( \frac{z - y}{2} \) et \( \frac{z + y}{2} \) sont des carrés d’entiers. Si tel n’était pas le cas, la décomposition de \( {\left( \frac{x}{2}\right) }^{2} \) en facteurs premiers entraînerait

> (Since \( z \) and \( y \) are odd, \( \frac{z - y}{2} \) and \( \frac{z + y}{2} \) are integers). This shows that \( \frac{z - y}{2} \) and \( \frac{z + y}{2} \) are squares of integers. If this were not the case, the prime factorization of \( {\left( \frac{x}{2}\right) }^{2} \) would imply

l’existence d’un nombre premier \( p \) divisant \( \left( \frac{z - y}{2}\right) \) et \( \left( \frac{z + y}{2}\right) \) . L’entier \( p \) diviserait \( \left( {\frac{z - y}{2} + \frac{z + y}{2}}\right) = z \) et \( \left( {\frac{z + y}{2} - \frac{z - y}{2}}\right) = y \) ce qui est impossible car \( y \land z = 1 \) .

> the existence of a prime number \( p \) dividing \( \left( \frac{z - y}{2}\right) \) and \( \left( \frac{z + y}{2}\right) \). The integer \( p \) would divide \( \left( {\frac{z - y}{2} + \frac{z + y}{2}}\right) = z \) and \( \left( {\frac{z + y}{2} - \frac{z - y}{2}}\right) = y \), which is impossible because \( y \land z = 1 \).

- Finalement, il existe \( \left( {n, m}\right)  \in  {\mathbb{N}}^{2} \) , tel que \( \frac{z - y}{2} = {n}^{2} \) et \( \frac{z + y}{2} = {m}^{2} \) . On en déduit \( x = {2mn} \) , \( y = {m}^{2} - {n}^{2} \) et \( z = {m}^{2} + {n}^{2} \) . Réciproquement, ce triplet est solution. La solution du problème général est donc

> - Finally, there exists \( \left( {n, m}\right)  \in  {\mathbb{N}}^{2} \) such that \( \frac{z - y}{2} = {n}^{2} \) and \( \frac{z + y}{2} = {m}^{2} \). We deduce \( x = {2mn} \), \( y = {m}^{2} - {n}^{2} \), and \( z = {m}^{2} + {n}^{2} \). Conversely, this triplet is a solution. The solution to the general problem is therefore

\[
\left( {x, y}\right) \text{ ou }\left( {y, x}\right)  = \left( {{2kmn}, k\left( {{m}^{2} - {n}^{2}}\right) }\right) ;\;z = k\left( {{m}^{2} + {n}^{2}}\right) \;k \in  {\mathbb{N}}^{ * },\left( {m, n}\right)  \in  {\mathbb{N}}^{2}, m > n.
\]

Remarque. Cet exercice est un cas particulier de l’équation \( {x}^{n} + {y}^{n} = {z}^{n} \) . Fermat énonça en 1637 que pour tout entier \( n \geq 3 \) , cette équation n’a pas de solution \( \left( {x, y, z}\right) \in {\left( {\mathbb{Z}}^{ * }\right) }^{3} \) , et affirmait qu'il en possédait une démonstration. La prétendue preuve n'a jamais été retrouvée et les mathématiciens, après de très nombreuses recherches aux cours des siècles suivants, ont sérieusement douté de l'existence de la preuve de Fermat. Une démonstration complète du théorème de Fermat a finalement été trouvée en 1993 par le mathématicien anglais Andrew Wiles, résolvant ainsi le problème le plus célèbre des mathématiques. Inutile de dire que le niveau de la preuve dépasse largement celui des classes préparatoires.

> Remark. This exercise is a special case of the equation \( {x}^{n} + {y}^{n} = {z}^{n} \). Fermat stated in 1637 that for any integer \( n \geq 3 \), this equation has no solution \( \left( {x, y, z}\right) \in {\left( {\mathbb{Z}}^{ * }\right) }^{3} \), and claimed to possess a proof. The alleged proof was never found, and mathematicians, after extensive research over the following centuries, seriously doubted the existence of Fermat's proof. A complete proof of Fermat's Theorem was finally found in 1993 by the English mathematician Andrew Wiles, thus solving the most famous problem in mathematics. Needless to say, the level of the proof far exceeds that of preparatory classes.

- Pour ceux que la théorie des nombres intéresse, on ne peut que conseiller l'excellent ouvrage de Hardy et Wright : An Introduction to the Theory of Numbers.

> - For those interested in number theory, we highly recommend the excellent work by Hardy and Wright: An Introduction to the Theory of Numbers.
