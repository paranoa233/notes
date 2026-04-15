#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1. Soit \( A \) un anneau commutatif unitaire intègre. Montrer que \( A \) est un corps si et seulement si \( A\left\lbrack X\right\rbrack \) est un anneau principal.

> EXERCISE 1. Let \( A \) be a commutative unitary integral domain. Show that \( A \) is a field if and only if \( A\left\lbrack X\right\rbrack \) is a principal ideal domain.

Solution. La condition nécessaire est une question de cours. Montrons la condition suffisante. Soit \( a \in A, a \neq 0 \) . Il s’agit de montrer que \( a \) est inversible. Comme \( A\left\lbrack X\right\rbrack \) est principal, il existe \( P \in A\left\lbrack X\right\rbrack \) tel que \( \left( a\right) + \left( X\right) = \left( P\right) \) . Comme \( a \in \left( P\right) \) , il existe \( Q \in A\left\lbrack X\right\rbrack \) tel que \( a = {PQ} \) . On en déduit, \( A\left\lbrack X\right\rbrack \) étant intègre, que \( P \in A \) .

> Solution. The necessary condition is a standard course question. Let us show the sufficient condition. Let \( a \in A, a \neq 0 \). We must show that \( a \) is invertible. Since \( A\left\lbrack X\right\rbrack \) is a principal ideal domain, there exists \( P \in A\left\lbrack X\right\rbrack \) such that \( \left( a\right) + \left( X\right) = \left( P\right) \). Since \( a \in \left( P\right) \), there exists \( Q \in A\left\lbrack X\right\rbrack \) such that \( a = {PQ} \). We deduce, since \( A\left\lbrack X\right\rbrack \) is an integral domain, that \( P \in A \).

Comme \( P \in \left( a\right) + \left( X\right) \) , il existe \( U \) et \( V \in A\left\lbrack X\right\rbrack \) tels que \( {aU} + {XV} = P \) . Si \( b \in A \) désigne le coefficient du terme constant de \( U \) , on en déduit \( {ab} = P \) puisque \( P \) est constant.

> As \( P \in \left( a\right) + \left( X\right) \), there exist \( U \) and \( V \in A\left\lbrack X\right\rbrack \) such that \( {aU} + {XV} = P \). If \( b \in A \) denotes the coefficient of the constant term of \( U \), we deduce \( {ab} = P \) since \( P \) is constant.

Comme \( X \in \left( P\right) \) , il existe \( Q \in A\left\lbrack X\right\rbrack \) tel que \( {PQ} = X \) . Si \( c \in A \) désigne le coefficient du terme en \( X \) de \( Q \) , on a donc \( {Pc} = 1 \) . Finalement, on a \( {abc} = {Pc} = 1 \) , et \( A \) étant commutatif, \( a\left( {bc}\right) = \left( {bc}\right) a = 1 \) donc \( a \) est inversible. D’où le résultat.

> As \( X \in \left( P\right) \) , there exists \( Q \in A\left\lbrack X\right\rbrack \) such that \( {PQ} = X \) . If \( c \in A \) denotes the coefficient of the \( X \) term of \( Q \) , we therefore have \( {Pc} = 1 \) . Finally, we have \( {abc} = {Pc} = 1 \) , and since \( A \) is commutative, \( a\left( {bc}\right) = \left( {bc}\right) a = 1 \) thus \( a \) is invertible. Hence the result.

EXERCICE 2. Soient \( A = {X}^{a} - 1 \) et \( B = {X}^{b} - 1 \in \mathbb{K}\left\lbrack X\right\rbrack \) , avec \( a, b \in {\mathbb{N}}^{ * } \) . Quel est le pgcd de \( A \) et de \( B \) ?

> EXERCISE 2. Let \( A = {X}^{a} - 1 \) and \( B = {X}^{b} - 1 \in \mathbb{K}\left\lbrack X\right\rbrack \) , with \( a, b \in {\mathbb{N}}^{ * } \) . What is the gcd of \( A \) and \( B \) ?

Solution. Nous allons déterminer pgcd \( \left( {A, B}\right) \) grâce à l'algorithme d'Euclide. Rappelons en le principe. On effectue à partir de \( A \) et \( B \) des divisions euclidiennes successives. On écrit

> Solution. We will determine gcd \( \left( {A, B}\right) \) using the Euclidean algorithm. Let us recall its principle. Starting from \( A \) and \( B \) , we perform successive Euclidean divisions. We write

\[
A = B{Q}_{0} + {R}_{0}\;\text{ avec }\;{Q}_{0},{R}_{0} \in  \mathbb{K}\left\lbrack  X\right\rbrack  \;\text{ et }\;\deg \left( {R}_{0}\right)  < \deg \left( B\right) ,
\]

et on recommence, en divisant toujours le dividende par le reste :

> and we repeat, always dividing the dividend by the remainder:

\[
B = {R}_{0}{Q}_{1} + {R}_{1}\;\text{ avec }\;{Q}_{1},{R}_{1} \in  \mathbb{K}\left\lbrack  X\right\rbrack  \;\text{ et }\;\deg \left( {R}_{1}\right)  < \deg \left( {R}_{0}\right) .
\]

Au rang \( k \) , on fait

> At rank \( k \) , we perform

\[
{R}_{k - 1} = {R}_{k}{Q}_{k + 1} + {R}_{k + 1}\;\text{ avec }\;{Q}_{k + 1},{R}_{k + 1} \in  \mathbb{K}\left\lbrack  X\right\rbrack  \;\text{ et }\;\deg \left( {R}_{k + 1}\right)  < \deg \left( {R}_{k}\right) .
\]

La suite \( {\left( \deg \left( {R}_{k}\right) \right) }_{k \in \mathbb{N}} \) décroît strictement et donc il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( {R}_{n} = 0 \) et \( {R}_{n - 1} \neq 0 \) . On remarque alors que pgcd \( \left( {A, B}\right) = \operatorname{pgcd}\left( {B,{R}_{0}}\right) = \cdots = \operatorname{pgcd}\left( {{R}_{n - 1},{R}_{n}}\right) \) , de sorte qu’a une constante multiplicative près, \( \operatorname{pgcd}\left( {A, B}\right) = {R}_{n - 1} \) (cet algorithme reste valable dans \( \mathbb{Z} \) ).

> The sequence \( {\left( \deg \left( {R}_{k}\right) \right) }_{k \in \mathbb{N}} \) is strictly decreasing and therefore there exists \( n \in {\mathbb{N}}^{ * } \) such that \( {R}_{n} = 0 \) and \( {R}_{n - 1} \neq 0 \) . We then note that gcd \( \left( {A, B}\right) = \operatorname{pgcd}\left( {B,{R}_{0}}\right) = \cdots = \operatorname{pgcd}\left( {{R}_{n - 1},{R}_{n}}\right) \) , so that up to a multiplicative constant, \( \operatorname{pgcd}\left( {A, B}\right) = {R}_{n - 1} \) (this algorithm remains valid in \( \mathbb{Z} \) ).

Avant d’appliquer l’algorithme, remarquons d’abord que si \( m \geq n \in {\mathbb{N}}^{ * } \) et si \( m = {nq} + r \) est la division euclidienne dans \( \mathbb{Z} \) de \( m \) par \( n \) , on a

> Before applying the algorithm, let us first note that if \( m \geq n \in {\mathbb{N}}^{ * } \) and if \( m = {nq} + r \) is the Euclidean division in \( \mathbb{Z} \) of \( m \) by \( n \) , we have

\[
{X}^{m} - 1 = \left( {{X}^{n} - 1}\right) \left( {{X}^{m - n} + {X}^{m - {2n}} + \cdots  + {X}^{m - {qn}}}\right)  + \left( {{X}^{m - {qn}} - 1}\right) .
\]

Comme \( m - {qn} = r < m \) , cette égalité constitue la division euclidienne de \( {X}^{m} - 1 \) par \( {X}^{n} - 1 \) . Nous venons donc de montrer que

> Since \( m - {qn} = r < m \) , this equality constitutes the Euclidean division of \( {X}^{m} - 1 \) by \( {X}^{n} - 1 \) . We have thus just shown that

le reste de la division euclidienne de \( {X}^{m} - 1 \) par \( {X}^{n} - 1 \) est \( {X}^{r} - 1 \) où \( r \) est le reste de la division euclidienne de \( m \) par \( n \) .

> the remainder of the Euclidean division of \( {X}^{m} - 1 \) by \( {X}^{n} - 1 \) is \( {X}^{r} - 1 \) where \( r \) is the remainder of the Euclidean division of \( m \) by \( n \) .(*)

Appliquons l’algorithme d’Euclide (dans \( \mathbb{Z} \) ) à \( a \) et \( b \) :

> Let us apply the Euclidean algorithm (in \( \mathbb{Z} \) ) to \( a \) and \( b \) :

\[
a = b{q}_{0} + {r}_{0},\;0 \leq  {r}_{0} < b,
\]

\[
b = {r}_{0}{q}_{1} + {r}_{1},\;0 \leq  {r}_{1} < {r}_{0},
\]

...

\[
{r}_{k - 1} = {r}_{k}{q}_{k + 1} + {r}_{k + 1},\;0 \leq  {r}_{k + 1} < {r}_{k}.
\]

On s’arrête au rang \( n \) lorsque \( {r}_{n} = 0 \neq {r}_{n - 1} \) . Comme pour les polynômes, on a

> We stop at rank \( n \) when \( {r}_{n} = 0 \neq {r}_{n - 1} \) . As with polynomials, we have

\[
\operatorname{pgcd}\left( {a, b}\right)  = \operatorname{pgcd}\left( {b,{r}_{0}}\right)  = \cdots  = \operatorname{pgcd}\left( {{r}_{n - 1},{r}_{n}}\right)  = {r}_{n - 1}.
\]

D’après le principe \( \left( *\right) \) , si les \( {R}_{k} \) désignent les polynômes introduits plus haut, on a \( {R}_{0} = \; {X}^{{r}_{0}} - 1,{R}_{1} = {X}^{{r}_{1}} - 1,\cdots ,{R}_{n - 1} = {X}^{{r}_{n - 1}} - 1,{R}_{n} = 0 \) . Donc pgcd \( \left( {A, B}\right) = {R}_{n - 1} = {X}^{{r}_{n - 1}} - 1 = \; {X}^{\operatorname{pgcd}\left( {a, b}\right) } - 1 \) .

> According to the principle \( \left( *\right) \), if \( {R}_{k} \) denote the polynomials introduced above, we have \( {R}_{0} = \; {X}^{{r}_{0}} - 1,{R}_{1} = {X}^{{r}_{1}} - 1,\cdots ,{R}_{n - 1} = {X}^{{r}_{n - 1}} - 1,{R}_{n} = 0 \). Thus gcd \( \left( {A, B}\right) = {R}_{n - 1} = {X}^{{r}_{n - 1}} - 1 = \; {X}^{\operatorname{pgcd}\left( {a, b}\right) } - 1 \).

EXERCICE 3. Déterminer l’ensemble des polynômes \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) tels que

> EXERCISE 3. Determine the set of polynomials \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) such that

\[
P \equiv  1\;\left( {\;\operatorname{mod}\;{\left( X - 1\right) }^{3}}\right) \;\text{ et }\;P \equiv   - 1\;\left( {\;\operatorname{mod}\;{\left( X + 1\right) }^{3}}\right) .
\]

Solution. Notons \( \Gamma \) l’ensemble des polynômes \( P \) vérifiant la condition requise. Un polynôme \( P \) appartient à \( \Gamma \) si et seulement s’il existe \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) tels que

> Solution. Let \( \Gamma \) be the set of polynomials \( P \) satisfying the required condition. A polynomial \( P \) belongs to \( \Gamma \) if and only if there exist \( U, V \in \mathbb{R}\left\lbrack X\right\rbrack \) such that

\[
\left\{  {\begin{array}{l} P = 1 + U{\left( X - 1\right) }^{3} \\  P =  - 1 + V{\left( X + 1\right) }^{3} \end{array}\text{ ou encore }\left\{  {\begin{array}{ll} P &  = 1 + U{\left( X - 1\right) }^{3} \\  1 + U{\left( X - 1\right) }^{3} &  =  - 1 + V{\left( X + 1\right) }^{3} \end{array}.}\right. }\right.
\]

En d’autres termes, \( \Gamma \) représente l’ensemble des polynômes de la forme \( 1 + U{\left( X - 1\right) }^{3} \) où \( U \) appartient à l'ensemble

> In other words, \( \Gamma \) represents the set of polynomials of the form \( 1 + U{\left( X - 1\right) }^{3} \) where \( U \) belongs to the set

\[
\Delta  = \left\{  {U \in  \mathbb{R}\left\lbrack  X\right\rbrack  \mid \exists V \in  \mathbb{R}\left\lbrack  X\right\rbrack  , U{\left( X - 1\right) }^{3} + V{\left( X + 1\right) }^{3} = 2}\right\}  .
\]

(*)

> Au facteur 2 près, on est ramené au problème de trouver les couples \( \left( {U, V}\right) \) tels que \( U{\left( X - 1\right) }^{3} + \; V{\left( X + 1\right) }^{3} = 1 \) . C’est un problème classique qui rentre dans le cadre du résultat suivant.

Up to a factor of 2, we are reduced to the problem of finding the pairs \( \left( {U, V}\right) \) such that \( U{\left( X - 1\right) }^{3} + \; V{\left( X + 1\right) }^{3} = 1 \). This is a classic problem that falls within the scope of the following result.

> Lemme. Soient \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) , premiers entre eux. Alors il existe \( \left( {{U}_{0},{V}_{0}}\right) \in \mathbb{K}{\left\lbrack X\right\rbrack }^{2} \) tel que \( {U}_{0}P + {V}_{0}Q = 1 \) , et les couples \( \left( {U, V}\right) \) solution de \( {UP} + {VQ} = 1 \) vérifient :

Lemma. Let \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) be coprime. Then there exists \( \left( {{U}_{0},{V}_{0}}\right) \in \mathbb{K}{\left\lbrack X\right\rbrack }^{2} \) such that \( {U}_{0}P + {V}_{0}Q = 1 \), and the pairs \( \left( {U, V}\right) \) that are solutions to \( {UP} + {VQ} = 1 \) satisfy:

\[
{UP} + {VQ} = 1\;\left( {U, V \in  \mathbb{K}\left\lbrack  X\right\rbrack  }\right)  \Leftrightarrow  \exists R \in  \mathbb{K}\left\lbrack  X\right\rbrack  ,\;U = {U}_{0} + {RQ}, V = {V}_{0} - {RP}.
\]

Preuve. L’existence de \( \left( {{U}_{0},{V}_{0}}\right) \) est assurée par le théorème de Bezout. Si \( {UP} + {VQ} = 1 \) on a \( \left( {U - {U}_{0}}\right) P + \left( {V - {V}_{0}}\right) Q = 0 \) donc \( \left( {U - {U}_{0}}\right) P = - \left( {V - {V}_{0}}\right) Q \) . Donc \( P \mid \left( {V - {V}_{0}}\right) Q \) et comme \( P \) et \( Q \) sont premiers entre eux, d’après le théorème de Gauss, \( P \mid V - {V}_{0} \) . Donc il existe \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( V = {V}_{0} - {RP} \) , et en remplaçant dans l’équation \( \left( {U - {U}_{0}}\right) P = - \left( {V - {V}_{0}}\right) Q \) , on tire \( U = {U}_{0} + {RQ} \) . Réciproquement, on vérifie facilement que ce couple est solution. D’où le lemme.

> Proof. The existence of \( \left( {{U}_{0},{V}_{0}}\right) \) is guaranteed by Bezout's theorem. If \( {UP} + {VQ} = 1 \) we have \( \left( {U - {U}_{0}}\right) P + \left( {V - {V}_{0}}\right) Q = 0 \) so \( \left( {U - {U}_{0}}\right) P = - \left( {V - {V}_{0}}\right) Q \). Thus \( P \mid \left( {V - {V}_{0}}\right) Q \) and since \( P \) and \( Q \) are coprime, by Gauss's theorem, \( P \mid V - {V}_{0} \). Thus there exists \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( V = {V}_{0} - {RP} \), and by substituting into equation \( \left( {U - {U}_{0}}\right) P = - \left( {V - {V}_{0}}\right) Q \), we obtain \( U = {U}_{0} + {RQ} \). Conversely, it is easy to verify that this pair is a solution. Hence the lemma.

Les polynômes \( X - 1 \) et \( X + 1 \) étant premiers entre eux, il en est de même des polynômes \( P = {\left( X - 1\right) }^{3} \) et \( Q = {\left( X + 1\right) }^{3} \) , et le lemme s’applique donc. On détermine \( {U}_{0} \) et \( {V}_{0} \) en utilisant l'algorithme d'Euclide (déjà rencontré dans l'exercice précédent, et de manière similaire à l’exercice 2 page 12 dans \( \mathbb{Z} \) ), ce qui donne : .

> Since the polynomials \( X - 1 \) and \( X + 1 \) are coprime, the same holds for the polynomials \( P = {\left( X - 1\right) }^{3} \) and \( Q = {\left( X + 1\right) }^{3} \), and the lemma therefore applies. We determine \( {U}_{0} \) and \( {V}_{0} \) using the Euclidean algorithm (already encountered in the previous exercise, and similarly to exercise 2 on page 12 in \( \mathbb{Z} \)), which gives: .

\[
{\left( X + 1\right) }^{3} = {\left( X - 1\right) }^{3} + 6{X}^{2} + 2
\]

\[
{\left( X - 1\right) }^{3} = \left( {6{X}^{2} + 2}\right) \left( {\frac{X}{6} - \frac{1}{2}}\right)  + \frac{8}{3}X
\]

\[
6{X}^{2} + 2 = \left( {\frac{8}{3}X}\right) \left( {\frac{9}{4}X}\right)  + 2
\]

Maintenant, on remonte les calculs (la méthode s'appelle algorithme d'Euclide étendu) :

> Now, we backtrack through the calculations (the method is called the extended Euclidean algorithm):

\[
2 = \left( {6{X}^{2} + 2}\right)  - \left\lbrack  {{\left( X - 1\right) }^{3} - \left( {6{X}^{2} + 2}\right) \left( {\frac{X}{6} - \frac{1}{2}}\right) }\right\rbrack  \left( {\frac{9}{4}X}\right)
\]

\[
= \left( {-\frac{9}{4}X}\right) {\left( X - 1\right) }^{3} + \left( {6{X}^{2} + 2}\right) \left\lbrack  {\left( {\frac{X}{6} - \frac{1}{2}}\right) \frac{9}{4}X + 1}\right\rbrack
\]

\[
= \left( {-\frac{9}{4}X}\right) {\left( X - 1\right) }^{3} + \left\lbrack  {{\left( X + 1\right) }^{3} - {\left( X - 1\right) }^{3}}\right\rbrack  \left( {\frac{3}{8}{X}^{2} - \frac{9}{8}X + 1}\right)
\]

\[
= \left( {-\frac{3}{8}{X}^{2} - \frac{9}{8}X - 1}\right) {\left( X - 1\right) }^{3} + \left( {\frac{3}{8}{X}^{2} - \frac{9}{8}X + 1}\right) {\left( X + 1\right) }^{3}.
\]

Ainsi, les polynômes

> Thus, the polynomials

\[
{U}_{0} =  - \frac{3}{16}{X}^{2} - \frac{9}{16}X - \frac{1}{2}\;\text{ et }\;{V}_{0} = \frac{3}{16}{X}^{2} - \frac{9}{16}X + \frac{1}{2}
\]

vérifient \( {U}_{0}{\left( X - 1\right) }^{3} + {V}_{0}{\left( X + 1\right) }^{3} = 1 \) . Le lemme entraîne que l’ensemble défini dans \( \left( *\right) \) est égal à \( \Delta = \left\{ {{U}_{0} + R{\left( X + 1\right) }^{3}, R \in \mathbb{R}\left\lbrack X\right\rbrack }\right\} \) , on a donc

> satisfy \( {U}_{0}{\left( X - 1\right) }^{3} + {V}_{0}{\left( X + 1\right) }^{3} = 1 \). The lemma implies that the set defined in \( \left( *\right) \) is equal to \( \Delta = \left\{ {{U}_{0} + R{\left( X + 1\right) }^{3}, R \in \mathbb{R}\left\lbrack X\right\rbrack }\right\} \), so we have

\[
\Gamma  = \left\{  {1 + \left( {2{U}_{0} + R{\left( X + 1\right) }^{3}}\right) {\left( X - 1\right) }^{3} \mid  R \in  \mathbb{R}\left\lbrack  X\right\rbrack  }\right\}  ,\;\text{ avec }\;{U}_{0} =  - \frac{3}{16}{X}^{2} - \frac{9}{16}X - \frac{1}{2}.
\]

Remarque. On peut tirer du lemme un résultat analogue à celui de la question a) de l'exercice 2 page 12, qui ici s'exprime sous la forme suivante.

> Remark. One can derive from the lemma a result analogous to that of question a) of exercise 2 on page 12, which here is expressed in the following form.

\( {SiP} \) et \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) sont premiers entre eux, alors il existe un unique couple \( \left( {{U}_{0},{V}_{0}}\right) \in {\left( \mathbb{K}\left\lbrack X\right\rbrack \right) }^{2} \) tel que \( {U}_{0}P + {V}_{0}Q = 1 \) avec \( \deg \left( {U}_{0}\right) < \deg \left( Q\right) \) et \( \deg \left( {V}_{0}\right) < \deg \left( P\right) \) .

> \( {SiP} \) and \( Q \in \mathbb{K}\left\lbrack X\right\rbrack \) are coprime, then there exists a unique pair \( \left( {{U}_{0},{V}_{0}}\right) \in {\left( \mathbb{K}\left\lbrack X\right\rbrack \right) }^{2} \) such that \( {U}_{0}P + {V}_{0}Q = 1 \) with \( \deg \left( {U}_{0}\right) < \deg \left( Q\right) \) and \( \deg \left( {V}_{0}\right) < \deg \left( P\right) \).

(Pour montrer ce résultat, partir d’une solution \( {UP} + {VQ} = 1 \) puis effectuer la division euclidienne de \( U \) par \( Q \) .)

> (To show this result, start with a solution \( {UP} + {VQ} = 1 \) then perform the Euclidean division of \( U \) by \( Q \).)

EXERCICE 4 (LEMME DE GAUSS ET CRITÉRE D’EISENSTEIN). 1/ a) Soient \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) et \( p \) un nombre premier. On suppose que \( p \) divise tous les coefficients du produit \( {PQ} \) . Montrer que \( p \) divise tous les coefficients de \( P \) ou tous les coefficients de \( Q \) .

> EXERCISE 4 (GAUSS'S LEMMA AND EISENSTEIN'S CRITERION). 1/ a) Let \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) and \( p \) be a prime number. Suppose that \( p \) divides all the coefficients of the product \( {PQ} \). Show that \( p \) divides all the coefficients of \( P \) or all the coefficients of \( Q \).

b) (Lemme de Gauss). Si \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) , on note \( c\left( P\right) \) le pgcd des coefficients de \( P \) (et \( c\left( P\right) = 1 \) si \( P = 0) \) . Montrer que si \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) , alors \( c\left( {PQ}\right) = c\left( P\right) c\left( Q\right) \) .

> b) (Gauss's Lemma). If \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \), we denote by \( c\left( P\right) \) the gcd of the coefficients of \( P \) (and \( c\left( P\right) = 1 \) if \( P = 0) \). Show that if \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \), then \( c\left( {PQ}\right) = c\left( P\right) c\left( Q\right) \).

2 / Montrer que si \( \Phi \in \mathbb{Z}\left\lbrack X\right\rbrack \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , il est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> 2 / Show that if \( \Phi \in \mathbb{Z}\left\lbrack X\right\rbrack \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \), it is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \).

3 / a) (Critère d’Eisenstein). Soit \( n \in {\mathbb{N}}^{ * } \) et \( P = {a}_{n}{X}^{n} + \cdots + {a}_{1}X + {a}_{0} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . On suppose qu’il existe un nombre premier \( p \) tel que

> 3 / a) (Eisenstein's criterion). Let \( n \in {\mathbb{N}}^{ * } \) and \( P = {a}_{n}{X}^{n} + \cdots + {a}_{1}X + {a}_{0} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Suppose there exists a prime number \( p \) such that

(iii) \( {p}^{2} \nmid {a}_{0} \) .

> (iii) \( {p}^{2} \nmid {a}_{0} \) .

Montrer que \( P \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> Show that \( P \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

b) Application. Soit \( p \) un nombre premier et \( \Phi \left( X\right) = {X}^{p - 1} + \cdots + X + 1 \) . Montrer que \( \Phi \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> b) Application. Let \( p \) be a prime number and \( \Phi \left( X\right) = {X}^{p - 1} + \cdots + X + 1 \) . Show that \( \Phi \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

Solution. \( 1/ \) a) Si \( a \in \mathbb{Z} \) , on note \( \bar{a} \) sa classe dans \( \mathbb{Z}/p\mathbb{Z} \) . Si \( P = {a}_{n}{X}^{n} + \cdots + {a}_{1}X + {a}_{0} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , on note \( \bar{P} = {\bar{a}}_{n}{X}^{n} + \cdots + {\bar{a}}_{1}X + {\bar{a}}_{0} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . Si \( p \) divise tous les coefficients de \( {PQ} \) , on a, avec ces notations : \( \overline{PQ} = \bar{P} \cdot \bar{Q} = \overline{0} \) . Comme \( \mathbb{Z}/p\mathbb{Z} \) est intègre, \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) est intègre. Donc \( \bar{P} = \overline{0} \) ou \( \bar{Q} = \overline{0} \) , d’où le résultat.

> Solution. \( 1/ \) a) If \( a \in \mathbb{Z} \) , we denote by \( \bar{a} \) its class in \( \mathbb{Z}/p\mathbb{Z} \) . If \( P = {a}_{n}{X}^{n} + \cdots + {a}_{1}X + {a}_{0} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , we denote by \( \bar{P} = {\bar{a}}_{n}{X}^{n} + \cdots + {\bar{a}}_{1}X + {\bar{a}}_{0} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . If \( p \) divides all the coefficients of \( {PQ} \) , we have, with these notations: \( \overline{PQ} = \bar{P} \cdot \bar{Q} = \overline{0} \) . Since \( \mathbb{Z}/p\mathbb{Z} \) is an integral domain, \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) is an integral domain. Thus \( \bar{P} = \overline{0} \) or \( \bar{Q} = \overline{0} \) , hence the result.

Remarque : on peut également résoudre cette question "à la main", sans passer par \( \mathbb{Z}/p\mathbb{Z} \) .

> Remark: one can also solve this question "by hand", without using \( \mathbb{Z}/p\mathbb{Z} \) .

b) Soient \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Il est clair que \( {P}_{1} = \frac{1}{c\left( P\right) }P \) et \( {Q}_{1} = \frac{1}{c\left( Q\right) }Q \) sont dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , et on a \( c\left( {P}_{1}\right) = c\left( {Q}_{1}\right) = 1 \) . Si \( c\left( {{P}_{1}{Q}_{1}}\right) > 1 \) , alors il existe un nombre premier \( p \) divisant \( c\left( {{P}_{1}{Q}_{1}}\right) \) . D’après \( 1/\mathrm{a}) \) , on a donc \( p \mid c\left( {P}_{1}\right) \) ou \( p \mid c\left( {Q}_{1}\right) \) , ce qui est absurde. Donc \( c\left( {{P}_{1}{Q}_{1}}\right) = 1 \) , ce qui entraîne \( c\left( {PQ}\right) = c\left( P\right) c\left( Q\right) c\left( {{P}_{1}{Q}_{1}}\right) = c\left( P\right) c\left( Q\right) \) .

> b) Let \( P, Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) . It is clear that \( {P}_{1} = \frac{1}{c\left( P\right) }P \) and \( {Q}_{1} = \frac{1}{c\left( Q\right) }Q \) are in \( \mathbb{Z}\left\lbrack X\right\rbrack \) , and we have \( c\left( {P}_{1}\right) = c\left( {Q}_{1}\right) = 1 \) . If \( c\left( {{P}_{1}{Q}_{1}}\right) > 1 \) , then there exists a prime number \( p \) dividing \( c\left( {{P}_{1}{Q}_{1}}\right) \) . According to \( 1/\mathrm{a}) \) , we therefore have \( p \mid c\left( {P}_{1}\right) \) or \( p \mid c\left( {Q}_{1}\right) \) , which is absurd. Thus \( c\left( {{P}_{1}{Q}_{1}}\right) = 1 \) , which implies \( c\left( {PQ}\right) = c\left( P\right) c\left( Q\right) c\left( {{P}_{1}{Q}_{1}}\right) = c\left( P\right) c\left( Q\right) \) .

2 / Soient \( P, Q \in \mathbb{Q}\left\lbrack X\right\rbrack \) tels que \( \Phi = {PQ} \) . Soient \( \alpha ,\beta \in {\mathbb{N}}^{ * } \) tels que \( {P}_{1} = {\alpha P} \) et \( {Q}_{1} = {\beta Q} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . On a \( {\alpha \beta \Phi } = {P}_{1}{Q}_{1} \) donc d’après le lemme de Gauss

> 2 / Let \( P, Q \in \mathbb{Q}\left\lbrack X\right\rbrack \) be such that \( \Phi = {PQ} \) . Let \( \alpha ,\beta \in {\mathbb{N}}^{ * } \) be such that \( {P}_{1} = {\alpha P} \) and \( {Q}_{1} = {\beta Q} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . We have \( {\alpha \beta \Phi } = {P}_{1}{Q}_{1} \) so, according to Gauss's lemma

\[
{\alpha \beta } \cdot  c\left( \Phi \right)  = c\left( {P}_{1}\right) c\left( {Q}_{1}\right) .
\]

Posons \( {P}_{2} = \frac{1}{c\left( {P}_{1}\right) }{P}_{1} \) et \( {Q}_{2} = \frac{1}{c\left( {Q}_{1}\right) }{Q}_{1} \) . Ces polynômes sont à coefficients entiers. Par ailleurs,

> Let us set \( {P}_{2} = \frac{1}{c\left( {P}_{1}\right) }{P}_{1} \) and \( {Q}_{2} = \frac{1}{c\left( {Q}_{1}\right) }{Q}_{1} \) . These polynomials have integer coefficients. Furthermore,

\[
{\alpha \beta \Phi } = c\left( {P}_{1}\right) c\left( {Q}_{1}\right) {P}_{2}{Q}_{2} = {\alpha \beta } \cdot  c\left( \Phi \right) {P}_{2}{Q}_{2}.
\]

Si \( {P}_{3} = c\left( \Phi \right) {P}_{2} \) , on a donc \( \Phi = {P}_{3}{Q}_{2} \) avec \( {P}_{3},{Q}_{2} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Comme \( \Phi \) est irréductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , on a nécessairement \( \deg \left( {P}_{3}\right) = 0 \) ou \( \deg \left( {Q}_{2}\right) = 0 \) , donc \( \deg \left( P\right) = 0 \) ou \( \deg \left( Q\right) = 0 \) , ce qui prouve que \( \Phi \) est bien irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> If \( {P}_{3} = c\left( \Phi \right) {P}_{2} \) , we then have \( \Phi = {P}_{3}{Q}_{2} \) with \( {P}_{3},{Q}_{2} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Since \( \Phi \) is irreducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) , we necessarily have \( \deg \left( {P}_{3}\right) = 0 \) or \( \deg \left( {Q}_{2}\right) = 0 \) , therefore \( \deg \left( P\right) = 0 \) or \( \deg \left( Q\right) = 0 \) , which proves that \( \Phi \) is indeed irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

3 / a) Supposons \( P \) réductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . D’après la question précédente, \( \Phi \) est réductible dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) et donc il existe \( Q, R \in \mathbb{Z}\left\lbrack X\right\rbrack \) tels que \( P = {QR} \) , avec \( a = \deg \left( Q\right) \geq 1 \) et \( b = \deg \left( R\right) \geq 1 \) . Dans \( \mathbb{Z}/p\mathbb{Z} \) , on a, d’après les hypothèses, \( \bar{P} = {\bar{a}}_{n}{X}^{n} \) . Écrivons \( Q = \mathop{\sum }\limits_{{i = 0}}^{a}{q}_{i}{X}^{i} \) et \( R = \mathop{\sum }\limits_{{i = 0}}^{b}{r}_{i}{X}^{i} \) . Dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , on a \( \bar{P} = \overline{QR} \) donc \( {\bar{a}}_{n}{X}^{n} = \overline{QR} \) , donc \( \bar{Q} = {\bar{q}}_{a}{X}^{a} \) et \( \bar{R} = {\bar{r}}_{b}{X}^{b} \) . Ceci entraîne \( {\bar{q}}_{0} = {\bar{r}}_{0} = 0 \) , donc \( p\left| {{q}_{0}\text{ et }p}\right| {r}_{0} \) , donc \( {p}^{2} \mid {q}_{0}{r}_{0} = {a}_{0} \) , ce qui est contraire aux hypothèses. Finalement, \( P \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> 3 / a) Suppose \( P \) is reducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) . According to the previous question, \( \Phi \) is reducible in \( \mathbb{Z}\left\lbrack X\right\rbrack \) and therefore there exist \( Q, R \in \mathbb{Z}\left\lbrack X\right\rbrack \) such that \( P = {QR} \) , with \( a = \deg \left( Q\right) \geq 1 \) and \( b = \deg \left( R\right) \geq 1 \) . In \( \mathbb{Z}/p\mathbb{Z} \) , we have, according to the hypotheses, \( \bar{P} = {\bar{a}}_{n}{X}^{n} \) . Let us write \( Q = \mathop{\sum }\limits_{{i = 0}}^{a}{q}_{i}{X}^{i} \) and \( R = \mathop{\sum }\limits_{{i = 0}}^{b}{r}_{i}{X}^{i} \) . In \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) , we have \( \bar{P} = \overline{QR} \) so \( {\bar{a}}_{n}{X}^{n} = \overline{QR} \) , therefore \( \bar{Q} = {\bar{q}}_{a}{X}^{a} \) and \( \bar{R} = {\bar{r}}_{b}{X}^{b} \) . This implies \( {\bar{q}}_{0} = {\bar{r}}_{0} = 0 \) , so \( p\left| {{q}_{0}\text{ et }p}\right| {r}_{0} \) , therefore \( {p}^{2} \mid {q}_{0}{r}_{0} = {a}_{0} \) , which contradicts the hypotheses. Finally, \( P \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

b) L’astuce est d’utiliser le critère d’Eisenstein en considérant \( \Phi \left( {X + 1}\right) \) . L’identité \( \left( {X - 1}\right) \Phi \left( X\right) = \; {X}^{p} - 1 \) entraîne \( {X\Phi }\left( {X + 1}\right) = {\left( X + 1\right) }^{p} - 1 \) , d’où on tire

> b) The trick is to use Eisenstein's criterion by considering \( \Phi \left( {X + 1}\right) \) . The identity \( \left( {X - 1}\right) \Phi \left( X\right) = \; {X}^{p} - 1 \) leads to \( {X\Phi }\left( {X + 1}\right) = {\left( X + 1\right) }^{p} - 1 \) , from which we derive

\[
\Phi \left( {X + 1}\right)  = \mathop{\sum }\limits_{{k = 1}}^{p}\left( \begin{array}{l} p \\  k \end{array}\right) {X}^{k - 1}
\]

Il est maintenant facile de vérifier que \( \Phi \left( {X + 1}\right) \) satisfait les hypothèses du critère d’Eisenstein avec le nombre premier \( p \) (rappelons que si \( p \) est premier et si \( 1 \leq k \leq p - 1 \) , alors \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) ), donc \( \Phi \left( {X + 1}\right) \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Donc \( \Phi \left( X\right) \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> It is now easy to verify that \( \Phi \left( {X + 1}\right) \) satisfies the hypotheses of Eisenstein's criterion with the prime number \( p \) (recall that if \( p \) is prime and if \( 1 \leq k \leq p - 1 \) , then \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) ), so \( \Phi \left( {X + 1}\right) \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Thus \( \Phi \left( X\right) \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

Remarque. Le résultat 3/ b) est un cas particulier d'un résultat général concernant les polynômes cyclotomiques (voir le problème 10, page 97).

> Remark. The result 3/ b) is a special case of a general result concerning cyclotomic polynomials (see problem 10, page 97).
