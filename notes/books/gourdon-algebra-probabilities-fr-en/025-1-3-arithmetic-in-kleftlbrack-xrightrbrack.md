#### 1.3. Arithmetic in \( \mathbb{K}\left\lbrack X\right\rbrack \)

*Français : 1.3. Arithmétique dans \( \mathbb{K}\left\lbrack X\right\rbrack \)*

Dans toute cette section, \( \mathbb{K} \) désigne un corps commutatif.

> Throughout this section, \( \mathbb{K} \) denotes a commutative field.

Le caractère euclidien (donc principal) de l’anneau des polynômes \( \mathbb{K}\left\lbrack X\right\rbrack \) lui confère une structure arithmétique tout-à-fait analogue à celle sur les entiers. Pour cette raison, nous ne passerons en revue que les propriétés arithmétiques de \( \mathbb{K}\left\lbrack X\right\rbrack \) les plus importantes.

> The Euclidean (and therefore principal) nature of the polynomial ring \( \mathbb{K}\left\lbrack X\right\rbrack \) gives it an arithmetic structure quite analogous to that of the integers. For this reason, we will only review the most important arithmetic properties of \( \mathbb{K}\left\lbrack X\right\rbrack \) .

Théorème 1 (Division EUCLIDIENNE). Soient \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack , B \neq 0 \) . Alors

> Theorem 1 (EUCLIDEAN division). Let \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack , B \neq 0 \) . Then

\[
\exists !\left( {Q, R}\right)  \in  \mathbb{K}{\left\lbrack  X\right\rbrack  }^{2}\;\text{ tel que }\;A = {BQ} + R\;\text{ avec }\;\deg \left( R\right)  < \deg \left( B\right) \text{ . }
\]

Remarque 3. Dans le cas de \( \mathcal{A}\left\lbrack X\right\rbrack \) où \( \mathcal{A} \) est un anneau commutatif unitaire, si le coefficient dominant de \( B \) est inversible, alors

> Remark 3. In the case of \( \mathcal{A}\left\lbrack X\right\rbrack \) where \( \mathcal{A} \) is a commutative unitary ring, if the leading coefficient of \( B \) is invertible, then

\[
\left( {\exists \left( {Q, R}\right)  \in  \mathcal{A}{\left\lbrack  X\right\rbrack  }^{2}}\right) ,\;A = {BQ} + R\;\text{ avec }\;\deg \left( R\right)  < \deg \left( B\right) .
\]

Si de plus \( \mathcal{A} \) est intègre, il y a unicité du couple \( \left( {Q, R}\right) \) . Ceci est en particulier vrai sur \( \mathbb{Z}\left\lbrack X\right\rbrack \) si \( B \) est unitaire.

> If, in addition, \( \mathcal{A} \) is an integral domain, the pair \( \left( {Q, R}\right) \) is unique. This is particularly true over \( \mathbb{Z}\left\lbrack X\right\rbrack \) if \( B \) is monic.

Remarque 4. Ceci est faux sur \( \mathcal{A}\left\lbrack X\right\rbrack \) lorsque \( \mathcal{A} \) n’est pas un corps (voir l’exercice 1).

> Remark 4. This is false over \( \mathcal{A}\left\lbrack X\right\rbrack \) when \( \mathcal{A} \) is not a field (see exercise 1).

DéFINITION 7. Soient \( {P}_{1},\ldots ,{P}_{n} \) des polynômes de \( \mathbb{K}\left\lbrack X\right\rbrack \) . L’unique polynôme unitaire \( P \) engendrant l’idéal \( \left( {P}_{1}\right) + \cdots + \left( {P}_{n}\right) \) s’appelle le pgcd des polynômes \( {P}_{1},\ldots ,{P}_{n} \) . Il est noté pgcd \( \left( {{P}_{1},\ldots ,{P}_{n}}\right) \) . C’est aussi le diviseur unitaire de plus haut degré divisant tous les \( {P}_{i} \) .

> DEFINITION 7. Let \( {P}_{1},\ldots ,{P}_{n} \) be polynomials in \( \mathbb{K}\left\lbrack X\right\rbrack \). The unique monic polynomial \( P \) generating the ideal \( \left( {P}_{1}\right) + \cdots + \left( {P}_{n}\right) \) is called the gcd of the polynomials \( {P}_{1},\ldots ,{P}_{n} \). It is denoted by gcd \( \left( {{P}_{1},\ldots ,{P}_{n}}\right) \). It is also the monic divisor of highest degree dividing all \( {P}_{i} \).

DéFINITION 8. Des polynômes \( {P}_{1},\ldots ,{P}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) sont dits premiers entre eux dans leur ensemble si on a pgcd \( \left( {{P}_{1},\ldots ,{P}_{n}}\right) = 1 \) . Ils sont dits premiers entre eux deux à deux si \( \forall i \neq j,\operatorname{pgcd}\left( {{P}_{i},{P}_{j}}\right) = 1. \)

> DEFINITION 8. Polynomials \( {P}_{1},\ldots ,{P}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) are said to be coprime as a set if we have gcd \( \left( {{P}_{1},\ldots ,{P}_{n}}\right) = 1 \). They are said to be pairwise coprime if \( \forall i \neq j,\operatorname{pgcd}\left( {{P}_{i},{P}_{j}}\right) = 1. \)

On définit également, comme dans \( \mathbb{Z} \) , la notion de ppcm de \( n \) polynômes.

> We also define, as in \( \mathbb{Z} \), the notion of lcm of \( n \) polynomials.

THÉORÉME 3 (BEZOUT). Des polynômes \( {P}_{1},\ldots ,{P}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) sont premiers entre eux dans leur ensemble si et seulement s’il existe \( {U}_{1},\ldots ,{U}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( {U}_{1}{P}_{1} + \cdots + {U}_{n}{P}_{n} = 1 \) .

> THEOREM 3 (BÉZOUT). Polynomials \( {P}_{1},\ldots ,{P}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) are coprime as a set if and only if there exist \( {U}_{1},\ldots ,{U}_{n} \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {U}_{1}{P}_{1} + \cdots + {U}_{n}{P}_{n} = 1 \).

Remarque 5. - Lorsque \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) sont premiers entre eux, on peut même avoir \( {UP} + {VQ} = 1 \) avec \( \deg \left( U\right) < \deg \left( Q\right) \) et \( \deg \left( V\right) < \deg \left( P\right) \) (voir la remarque de l'exercice 3, page 60).

> Remark 5. - When \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) are coprime, we can even have \( {UP} + {VQ} = 1 \) with \( \deg \left( U\right) < \deg \left( Q\right) \) and \( \deg \left( V\right) < \deg \left( P\right) \) (see the remark in exercise 3, page 60).

- Comme dans \( \mathbb{Z} \) , il découle du théorème de Bezout le théorème de Gauss : Si \( P \mid  {QR} \) et si pgcd \( \left( {P, Q}\right)  = 1 \) , alors \( P \mid  R \) .

> - As in \( \mathbb{Z} \), Gauss's theorem follows from Bézout's theorem: If \( P \mid  {QR} \) and if gcd \( \left( {P, Q}\right)  = 1 \), then \( P \mid  R \).

Ce qui dans \( \mathbb{Z} \) joue le rôle des nombres premiers est ici appelé polynôme irréductible. Plus précisément :

> What plays the role of prime numbers in \( \mathbb{Z} \) is called an irreducible polynomial here. More precisely:

DéFINITION 9. Un polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) est dit irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) si \( P \) n’est pas constant (i.e. \( \deg \left( P\right) \geq 1 \) ) et si ses seuls diviseurs dans \( \mathbb{K}\left\lbrack X\right\rbrack \) sont les constantes non nulles et les polynômes associés à \( P \) .

> DEFINITION 9. A polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) is said to be irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) if \( P \) is not constant (i.e., \( \deg \left( P\right) \geq 1 \)) and if its only divisors in \( \mathbb{K}\left\lbrack X\right\rbrack \) are the non-zero constants and the polynomials associated with \( P \).

Remarque 6. Attention. Un polynôme irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) ne l’est pas forcément dans \( \mathbb{L}\left\lbrack X\right\rbrack \) où \( \mathbb{L} \) est un surcorps de \( \mathbb{K} \) . Par exemple, \( P = {X}^{2} + 1 \) est irréductible dans \( \mathbb{R}\left\lbrack X\right\rbrack \) , mais pas dans \( \mathbb{C}\left\lbrack X\right\rbrack \) puisque \( P = \left( {X - i}\right) \left( {X + i}\right) \) .

> Remark 6. Caution. A polynomial that is irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) is not necessarily so in \( \mathbb{L}\left\lbrack X\right\rbrack \) where \( \mathbb{L} \) is an extension field of \( \mathbb{K} \). For example, \( P = {X}^{2} + 1 \) is irreducible in \( \mathbb{R}\left\lbrack X\right\rbrack \), but not in \( \mathbb{C}\left\lbrack X\right\rbrack \) since \( P = \left( {X - i}\right) \left( {X + i}\right) \).

Comme dans \( \mathbb{Z} \) , on a le résultat suivant.

> As in \( \mathbb{Z} \), we have the following result.

- THÉORÉME 4. Soit \( P \in  \mathbb{K}\left\lbrack  X\right\rbrack \) un polynôme non nul. Alors \( P \) se décompose de manière unique à l'ordre prés sous la forme

> - THEOREM 4. Let \( P \in  \mathbb{K}\left\lbrack  X\right\rbrack \) be a non-zero polynomial. Then \( P \) decomposes uniquely up to order in the form

\[
P = \lambda {P}_{1}^{{\alpha }_{1}}\cdots {P}_{k}^{{\alpha }_{k}}
\]

où \( \lambda \in {\mathbb{K}}^{ * },{\alpha }_{i} \in {\mathbb{N}}^{ * } \) et les \( {P}_{i} \) des polynômes distincts, unitaires et irréductibles dans \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> where \( \lambda \in {\mathbb{K}}^{ * },{\alpha }_{i} \in {\mathbb{N}}^{ * } \) and the \( {P}_{i} \) are distinct, monic, and irreducible polynomials in \( \mathbb{K}\left\lbrack X\right\rbrack \).

Rappelons enfin le théorème de division selon les puissances croissantes (l'algorithme associé peut être utilisé sur une fraction rationnelle, pour calculer son développement limité, ou pour calculer la partie principale relative à un pôle multiple dans sa décomposition en éléments simples, dont un exemple est donné page 76).

> Finally, let us recall the division theorem according to increasing powers (the associated algorithm can be used on a rational fraction to calculate its Taylor expansion, or to calculate the principal part relative to a multiple pole in its partial fraction decomposition, an example of which is given on page 76).

THÉORÈME 5 (DIVISION SELON LES PUISSANCES CROISSANTES). Soient \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack \) , le coefficient du terme constant de \( B \) étant non nul. Soit \( k \in {\mathbb{N}}^{ * } \) . Alors

> THEOREM 5 (DIVISION ACCORDING TO INCREASING POWERS). Let \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack \), the coefficient of the constant term of \( B \) being non-zero. Let \( k \in {\mathbb{N}}^{ * } \). Then

\[
\left( {\exists !\left( {{Q}_{k},{R}_{k}}\right)  \in  \mathbb{K}{\left\lbrack  X\right\rbrack  }^{2}}\right) ,\;A = B{Q}_{k} + {X}^{k + 1}{R}_{k}\;\text{ avec }\;\deg \left( {Q}_{k}\right)  \leq  k.
\]
