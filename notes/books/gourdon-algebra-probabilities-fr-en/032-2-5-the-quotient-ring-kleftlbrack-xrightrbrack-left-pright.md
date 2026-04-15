#### 2.5. The quotient ring \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \)

*Français : 2.5. L'anneau quotient \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \)*

Notation. - Si \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , on note \( \left( P\right) \) l’idéal \( \left( P\right) = \{ {PQ} \mid Q \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . - Si \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack \) , on note \( A \equiv B\left( {\;\operatorname{mod}\;P}\right) \) lorsque \( A - B \in \left( P\right) \) .

> Notation. - If \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , we denote by \( \left( P\right) \) the ideal \( \left( P\right) = \{ {PQ} \mid Q \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . - If \( A, B \in \mathbb{K}\left\lbrack X\right\rbrack \) , we denote \( A \equiv B\left( {\;\operatorname{mod}\;P}\right) \) when \( A - B \in \left( P\right) \) .

Soit \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) . Comme \( \left( P\right) \) est un idéal de \( \mathbb{K}\left\lbrack X\right\rbrack \) , le quotient \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) définit une structure d’anneau (voir la partie 3.2 du chapitre I). Si \( A \in \mathbb{K}\left\lbrack X\right\rbrack \) , la classe de \( A \) dans \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est \( \dot{A} = A + \left( P\right) = \{ A + {PQ} \mid Q \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . On a par ailleurs

> Let \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) . Since \( \left( P\right) \) is an ideal of \( \mathbb{K}\left\lbrack X\right\rbrack \) , the quotient \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) defines a ring structure (see part 3.2 of chapter I). If \( A \in \mathbb{K}\left\lbrack X\right\rbrack \) , the class of \( A \) in \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is \( \dot{A} = A + \left( P\right) = \{ A + {PQ} \mid Q \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . We also have

\[
\dot{A} = \dot{B} \Leftrightarrow  A \equiv  B\;\left( {\;\operatorname{mod}\;P}\right)  \Leftrightarrow  P \mid  \left( {B - A}\right) .
\]

THÉORÉME 4. Soit \( P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \) . Alors \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est une \( \mathbb{K} \) -algèbre de dimension finie \( n = \deg \left( P\right) \) . Si on note \( x = \dot{X} \) , la famille \( \left( {1, x,\ldots ,{x}^{n - 1}}\right) \) en est une base.

> THEOREM 4. Let \( P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \). Then \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is a finite-dimensional \( \mathbb{K} \)-algebra \( n = \deg \left( P\right) \). If we denote \( x = \dot{X} \), the family \( \left( {1, x,\ldots ,{x}^{n - 1}}\right) \) is a basis for it.

Démonstration. L’anneau quotient \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est évidemment une \( \mathbb{K} \) -algèbre. Montrons que la famille \( \left( {1, x,\ldots ,{x}^{n - 1}}\right) \) en est une base.

> Proof. The quotient ring \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is obviously a \( \mathbb{K} \)-algebra. Let us show that the family \( \left( {1, x,\ldots ,{x}^{n - 1}}\right) \) is a basis for it.

- C’est une famille génératrice. En effet. Soit \( A \in  \mathbb{K}\left\lbrack  X\right\rbrack \) . Il existe \( Q, R \in  \mathbb{K}\left\lbrack  X\right\rbrack \) tels que \( A = {PQ} + R \) avec \( \deg \left( R\right)  < n = \deg \left( P\right) \) . Donc \( \dot{A} = \dot{R} \in  \operatorname{Vect}\left( {1, x,\ldots ,{x}^{n - 1}}\right) . \)

> - It is a generating family. Indeed. Let \( A \in  \mathbb{K}\left\lbrack  X\right\rbrack \). There exist \( Q, R \in  \mathbb{K}\left\lbrack  X\right\rbrack \) such that \( A = {PQ} + R \) with \( \deg \left( R\right)  < n = \deg \left( P\right) \). Thus \( \dot{A} = \dot{R} \in  \operatorname{Vect}\left( {1, x,\ldots ,{x}^{n - 1}}\right) . \)

- C’est une famille libre. Si \( {a}_{0} + {a}_{1}x + \cdots  + {a}_{n - 1}{x}^{n - 1} = 0 \) , alors le polynôme \( A = {a}_{0} + \; {a}_{1}X + \cdots  + {a}_{n - 1}{X}^{n - 1} \) vérifie \( \dot{A} = 0 \) . Donc \( P \mid  A \) , et comme \( \deg \left( A\right)  < \deg \left( P\right) \) , on a \( A = 0 \) , donc \( {a}_{0} = {a}_{1} = \ldots  = {a}_{n - 1} = 0. \)

> - It is a linearly independent family. If \( {a}_{0} + {a}_{1}x + \cdots  + {a}_{n - 1}{x}^{n - 1} = 0 \), then the polynomial \( A = {a}_{0} + \; {a}_{1}X + \cdots  + {a}_{n - 1}{X}^{n - 1} \) satisfies \( \dot{A} = 0 \). Thus \( P \mid  A \), and since \( \deg \left( A\right)  < \deg \left( P\right) \), we have \( A = 0 \), therefore \( {a}_{0} = {a}_{1} = \ldots  = {a}_{n - 1} = 0. \)

Proposition 4. Soit \( P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \) . L’anneau \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est un corps si et seulement si \( P \) est irréductible.

> Proposition 4. Let \( P \in \mathbb{K}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \). The ring \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is a field if and only if \( P \) is irreducible.

Démonstration. Condition nécessaire. Si \( P \) est réductible, alors il existe \( Q \) et \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( P = {QR} \) , avec \( 1 \leq \deg \left( Q\right) < \deg \left( P\right) \) et \( 1 \leq \deg \left( R\right) < \deg \left( P\right) \) . Donc \( \dot{0} = \dot{Q}\dot{R} \) avec \( \dot{Q} \neq \dot{0} \) et \( \dot{R} \neq \dot{0} \) , ce qui est absurde puisque \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est un corps par hypothèse. Donc \( P \) est irréductible. Condition suffisante. Supposons \( P \) irréductible. Soit \( A \in \mathbb{K}\left\lbrack X\right\rbrack ,\dot{A} \neq \dot{0} \) . Le polynôme \( P \) ne divise pas \( A \) et \( P \) étant irréductible, \( P \) et \( A \) sont premiers entre eux. D’après le théorème de Bezout, il existe \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( {UP} + {VA} = 1 \) , d’où \( \dot{V}\dot{A} = 1 \) . Donc \( \dot{A} \) est inversible, et ceci dès que \( \dot{A} \neq \dot{0} \) . Finalement, \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) est un corps.

> Proof. Necessary condition. If \( P \) is reducible, then there exist \( Q \) and \( R \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( P = {QR} \) , with \( 1 \leq \deg \left( Q\right) < \deg \left( P\right) \) and \( 1 \leq \deg \left( R\right) < \deg \left( P\right) \) . Thus \( \dot{0} = \dot{Q}\dot{R} \) with \( \dot{Q} \neq \dot{0} \) and \( \dot{R} \neq \dot{0} \) , which is absurd since \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is a field by hypothesis. Therefore \( P \) is irreducible. Sufficient condition. Suppose \( P \) is irreducible. Let \( A \in \mathbb{K}\left\lbrack X\right\rbrack ,\dot{A} \neq \dot{0} \) . The polynomial \( P \) does not divide \( A \) and since \( P \) is irreducible, \( P \) and \( A \) are coprime. According to Bezout's theorem, there exist \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {UP} + {VA} = 1 \) , hence \( \dot{V}\dot{A} = 1 \) . Thus \( \dot{A} \) is invertible, and this holds as soon as \( \dot{A} \neq \dot{0} \) . Finally, \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) is a field.

Remarque 9. Ce résultat est analogue à la proposition 10 page 11 (ici aussi, on voit que les propriétés arithmétiques de \( \mathbb{Z} \) et de \( \mathbb{K}\left\lbrack X\right\rbrack \) sont semblables.)

> Remark 9. This result is analogous to proposition 10 on page 11 (here too, we see that the arithmetic properties of \( \mathbb{Z} \) and \( \mathbb{K}\left\lbrack X\right\rbrack \) are similar.)
