#### 2.1. Generalities

*Français : 2.1. Généralités*

Notation. Soit \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{p}{X}^{p} \in \mathbb{K}\left\lbrack X\right\rbrack \) . Conformément à la définition d’une fonction polynôme sur une \( \mathbb{K} \) -algèbre (voir la partie 2.1 page 63), on définit les fonctions polynômes sur \( \mathcal{L}\left( E\right) \) ou \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) comme suit :

> Notation. Let \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{p}{X}^{p} \in \mathbb{K}\left\lbrack X\right\rbrack \) . In accordance with the definition of a polynomial function on a \( \mathbb{K} \) -algebra (see section 2.1 page 63), we define polynomial functions on \( \mathcal{L}\left( E\right) \) or \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) as follows:

- Pour tout \( f \in  \mathcal{L}\left( E\right) \) , on note \( P\left( f\right)  = {a}_{0}{\operatorname{Id}}_{E} + {a}_{1}f + \cdots  + {a}_{p}{f}^{p} \in  \mathcal{L}\left( E\right) \) .

> - For all \( f \in  \mathcal{L}\left( E\right) \), we denote \( P\left( f\right)  = {a}_{0}{\operatorname{Id}}_{E} + {a}_{1}f + \cdots  + {a}_{p}{f}^{p} \in  \mathcal{L}\left( E\right) \).

- Pour tout \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on note \( P\left( A\right)  = {a}_{0}{I}_{n} + {a}_{1}A + \cdots  + {a}_{p}{A}^{p} \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> - For all \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), we denote \( P\left( A\right)  = {a}_{0}{I}_{n} + {a}_{1}A + \cdots  + {a}_{p}{A}^{p} \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \).

Remarque 1. Si \( f \in \mathcal{L}\left( E\right) ,\forall P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) on a \( P\left( f\right) \circ Q\left( f\right) = \left( {PQ}\right) \left( f\right) \) . L’ensemble \( \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) est une sous-algèbre commutative de \( \mathcal{L}\left( E\right) \) .

> Remark 1. If \( f \in \mathcal{L}\left( E\right) ,\forall P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) we have \( P\left( f\right) \circ Q\left( f\right) = \left( {PQ}\right) \left( f\right) \). The set \( \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) is a commutative subalgebra of \( \mathcal{L}\left( E\right) \).

- Un polynôme d'une matrice triangulaire est une matrice triangulaire. Plus précisément, si \( P \in  \mathbb{K}\left\lbrack  X\right\rbrack \) on a

> - A polynomial of a triangular matrix is a triangular matrix. More precisely, if \( P \in  \mathbb{K}\left\lbrack  X\right\rbrack \) we have

\[
M = \left( \begin{matrix} {\alpha }_{1} &  \times  & \cdots &  \times  \\  0 & {\alpha }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\alpha }_{n} \end{matrix}\right)  \Rightarrow  P\left( M\right)  = \left( \begin{matrix} P\left( {\alpha }_{1}\right) &  \times  & \cdots &  \times  \\  0 & P\left( {\alpha }_{2}\right) &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & P\left( {\alpha }_{n}\right)  \end{matrix}\right) .
\]

Ainsi, si \( M \) est trigonalisable, \( P\left( M\right) \) également et les valeurs propres de \( P\left( M\right) \) sont les valeurs prises par le polynôme \( P \) sur les valeurs propres de \( M \) .

> Thus, if \( M \) is trigonalizable, \( P\left( M\right) \) is as well and the eigenvalues of \( P\left( M\right) \) are the values taken by the polynomial \( P \) on the eigenvalues of \( M \).

Proposition 1. Soit \( f \in \mathcal{L}\left( E\right) \) et \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( P\left( f\right) = 0 \) . Si \( \lambda \) est valeur propre de \( f \) , alors \( P\left( \lambda \right) = 0 \) .

> Proposition 1. Let \( f \in \mathcal{L}\left( E\right) \) and \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( P\left( f\right) = 0 \). If \( \lambda \) is an eigenvalue of \( f \), then \( P\left( \lambda \right) = 0 \).

Démonstration. Soit \( x \neq 0 \) un vecteur propre de \( f \) associé à la valeur propre \( \lambda \) . On a \( f\left( x\right) = {\lambda x} \) , donc \( 0 = P\left( f\right) \left( x\right) = P\left( \lambda \right) x \) , d’où le résultat.

> Proof. Let \( x \neq 0 \) be an eigenvector of \( f \) associated with the eigenvalue \( \lambda \). We have \( f\left( x\right) = {\lambda x} \), therefore \( 0 = P\left( f\right) \left( x\right) = P\left( \lambda \right) x \), hence the result.

Remarque 2. Attention, la réciproque est fausse. Par exemple, \( P = X\left( {X - 1}\right) \) annule \( {\operatorname{Id}}_{E} \) , et pourtant 0 qui est racine de \( P \) n’est pas valeur propre de \( {\operatorname{Id}}_{E} \) .

> Remark 2. Caution, the converse is false. For example, \( P = X\left( {X - 1}\right) \) annihilates \( {\operatorname{Id}}_{E} \), yet 0, which is a root of \( P \), is not an eigenvalue of \( {\operatorname{Id}}_{E} \).

\( \rightarrow \) THÉORÉME 1 (DÉCOMPOSITION DES NOYAUX). Soit \( f \in \mathcal{L}\left( E\right) \) et \( P = {P}_{1}\cdots {P}_{k} \in \mathbb{K}\left\lbrack X\right\rbrack \) , les polynômes \( {P}_{i} \) étant premiers entre eux deux à deux. Alors

> \( \rightarrow \) THEOREM 1 (DECOMPOSITION OF KERNELS). Let \( f \in \mathcal{L}\left( E\right) \) and \( P = {P}_{1}\cdots {P}_{k} \in \mathbb{K}\left\lbrack X\right\rbrack \), the polynomials \( {P}_{i} \) being pairwise coprime. Then

\[
\operatorname{Ker}P\left( f\right)  = \operatorname{Ker}{P}_{1}\left( f\right)  \oplus  \cdots  \oplus  \operatorname{Ker}{P}_{k}\left( f\right) .
\]

Démonstration. On procède par récurrence sur \( k \geq 2 \) .

> Proof. We proceed by induction on \( k \geq 2 \).

- Pour \( k = 2 : {P}_{1} \) et \( {P}_{2} \) étant premiers entre eux, il existe (théorème de Bezout) \( U \) et \( V \in  \mathbb{K}\left\lbrack  X\right\rbrack \) tels que \( U{P}_{1} + V{P}_{2} = 1 \) .

> - For \( k = 2 : {P}_{1} \) and \( {P}_{2} \) being coprime, there exist (Bézout's theorem) \( U \) and \( V \in  \mathbb{K}\left\lbrack  X\right\rbrack \) such that \( U{P}_{1} + V{P}_{2} = 1 \).

Soit \( x \in \operatorname{Ker}{P}_{1}\left( f\right) \cap \operatorname{Ker}{P}_{2}\left( f\right) \) . On a \( \left( {U{P}_{1} + V{P}_{2}}\right) \left( f\right) \left( x\right) = x \) , autrement dit \( x = U\left( f\right) \circ \; {P}_{1}\left( f\right) \left( x\right) + V\left( f\right) \circ {P}_{2}\left( f\right) \left( x\right) = 0 \) . Donc Ker \( {P}_{1}\left( f\right) \cap \operatorname{Ker}{P}_{2}\left( f\right) = \{ 0\} \;\left( *\right) \) .

> Let \( x \in \operatorname{Ker}{P}_{1}\left( f\right) \cap \operatorname{Ker}{P}_{2}\left( f\right) \) . We have \( \left( {U{P}_{1} + V{P}_{2}}\right) \left( f\right) \left( x\right) = x \) , in other words \( x = U\left( f\right) \circ \; {P}_{1}\left( f\right) \left( x\right) + V\left( f\right) \circ {P}_{2}\left( f\right) \left( x\right) = 0 \) . Thus Ker \( {P}_{1}\left( f\right) \cap \operatorname{Ker}{P}_{2}\left( f\right) = \{ 0\} \;\left( *\right) \) .

Soit \( x \in \operatorname{Ker}P\left( f\right) \) . On a \( x = U{P}_{1}\left( f\right) \left( x\right) + V{P}_{2}\left( f\right) \left( x\right) \;\left( {* * }\right) \) . Or

> Let \( x \in \operatorname{Ker}P\left( f\right) \) . We have \( x = U{P}_{1}\left( f\right) \left( x\right) + V{P}_{2}\left( f\right) \left( x\right) \;\left( {* * }\right) \) . However

\[
{P}_{2}\left( f\right) \left\lbrack  {U{P}_{1}\left( f\right) \left( x\right) }\right\rbrack   = U{P}_{1}{P}_{2}\left( f\right) \left( x\right)  = U\left( f\right)  \circ  P\left( f\right) \left( x\right)  = 0,
\]

donc \( U{P}_{1}\left( f\right) \left( x\right) \in \operatorname{Ker}{P}_{2}\left( f\right) \) . De même, \( V{P}_{2}\left( f\right) \left( x\right) \in \operatorname{Ker}{P}_{1}\left( f\right) \) . De \( \left( {* * }\right) \) , on tire \( \operatorname{Ker}P\left( f\right) = \; \operatorname{Ker}{P}_{1}\left( f\right) + \operatorname{Ker}{P}_{2}\left( f\right) \) , d’où le résultat pour \( k = 2 \) avec \( \left( *\right) \) .

> therefore \( U{P}_{1}\left( f\right) \left( x\right) \in \operatorname{Ker}{P}_{2}\left( f\right) \) . Similarly, \( V{P}_{2}\left( f\right) \left( x\right) \in \operatorname{Ker}{P}_{1}\left( f\right) \) . From \( \left( {* * }\right) \) , we derive \( \operatorname{Ker}P\left( f\right) = \; \operatorname{Ker}{P}_{1}\left( f\right) + \operatorname{Ker}{P}_{2}\left( f\right) \) , hence the result for \( k = 2 \) with \( \left( *\right) \) .

- Supposons le résultat vrai au rang \( k \) et montrons le au rang \( k + 1 \) . On a \( P = {Q}_{1}{Q}_{2} \) avec \( {Q}_{1} = {P}_{1}\cdots {P}_{k} \) et \( {Q}_{2} = {P}_{k + 1} \) . Les polynômes \( {Q}_{1} \) et \( {Q}_{2} \) sont premiers entre eux donc d’après le cas \( k = 2 \) , \( \operatorname{Ker}P\left( f\right)  = \operatorname{Ker}{Q}_{1}\left( f\right)  \oplus  \operatorname{Ker}{Q}_{2}\left( f\right) \) , et d’après l’hypothèse de récurrence, \( \operatorname{Ker}{Q}_{1}\left( f\right)  = \; { \oplus  }_{i = 1}^{k}\operatorname{Ker}{P}_{i}\left( f\right) \) . Finalement,

> - Assume the result holds for rank \( k \) and show it for rank \( k + 1 \) . We have \( P = {Q}_{1}{Q}_{2} \) with \( {Q}_{1} = {P}_{1}\cdots {P}_{k} \) and \( {Q}_{2} = {P}_{k + 1} \) . The polynomials \( {Q}_{1} \) and \( {Q}_{2} \) are coprime, so according to case \( k = 2 \) , \( \operatorname{Ker}P\left( f\right)  = \operatorname{Ker}{Q}_{1}\left( f\right)  \oplus  \operatorname{Ker}{Q}_{2}\left( f\right) \) , and by the induction hypothesis, \( \operatorname{Ker}{Q}_{1}\left( f\right)  = \; { \oplus  }_{i = 1}^{k}\operatorname{Ker}{P}_{i}\left( f\right) \) . Finally,

\[
\operatorname{Ker}P\left( f\right)  = \left\lbrack  {\operatorname{Ker}{P}_{1}\left( f\right)  \oplus  \cdots  \oplus  \operatorname{Ker}{P}_{k}\left( f\right) }\right\rbrack   \oplus  \operatorname{Ker}{P}_{k + 1}\left( f\right)  = \operatorname{Ker}{P}_{1}\left( f\right)  \oplus  \cdots  \oplus  \operatorname{Ker}{P}_{k + 1}\left( f\right) .
\]

Remarque 3. - Ce théorème est important. Il reste vrai en dimension infinie.

> Remark 3. - This theorem is important. It remains true in infinite dimension.

- Il existe beaucoup d’autres résultats du même type. Par exemple, soit \( f \in  \mathcal{L}\left( E\right) \) . Pour tout \( \varphi  \in  \mathbb{K}\left\lbrack  X\right\rbrack \) , on note \( {I}_{\varphi } = \operatorname{Im}\varphi \left( f\right) \) et \( {N}_{\varphi } = \operatorname{Ker}\varphi \left( f\right) \) . Soient \( P, Q \in  \mathbb{K}\left\lbrack  X\right\rbrack \) . Alors si \( D = \operatorname{pgcd}\left( {P, Q}\right) \) et \( M = \operatorname{ppcm}\left( {P, Q}\right) \) , on a

> - There are many other results of the same type. For example, let \( f \in  \mathcal{L}\left( E\right) \) . For all \( \varphi  \in  \mathbb{K}\left\lbrack  X\right\rbrack \) , we denote \( {I}_{\varphi } = \operatorname{Im}\varphi \left( f\right) \) and \( {N}_{\varphi } = \operatorname{Ker}\varphi \left( f\right) \) . Let \( P, Q \in  \mathbb{K}\left\lbrack  X\right\rbrack \) . Then if \( D = \operatorname{pgcd}\left( {P, Q}\right) \) and \( M = \operatorname{ppcm}\left( {P, Q}\right) \) , we have

\[
{N}_{P} \cap  {N}_{Q} = {N}_{D},\;{N}_{P} + {N}_{Q} = {N}_{M},\;{I}_{P} + {I}_{Q} = {I}_{D},\;{I}_{P} \cap  {I}_{Q} = {I}_{M}.
\]

Ces résultats se généralisent par récurrence à \( k \) polynômes.

> These results generalize by induction to \( k \) polynomials.

\( \rightarrow \) THÉORÉME 2. Soit \( f \in \mathcal{L}\left( E\right) \) . L’endomorphisme \( f \) est diagonalisable si et seulement s’il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) scindé sur \( \mathbb{K} \) ayant toutes ses racines simples tel que \( P\left( f\right) = 0 \) .

> \( \rightarrow \) THEOREM 2. Let \( f \in \mathcal{L}\left( E\right) \) . The endomorphism \( f \) is diagonalizable if and only if there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) split over \( \mathbb{K} \) having only simple roots such that \( P\left( f\right) = 0 \) .

Démonstration. Condition nécessaire. Notons \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) les valeurs propres (distinctes) de \( f \) et \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) les sous-espaces propres correspondants. Soit \( P = \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{r}}\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) . Le polynôme \( P \) est scindé dans \( \mathbb{K}\left\lbrack X\right\rbrack \) et a toutes ses racines simples. Par ailleurs, les polynômes \( \left( {X - {\lambda }_{i}}\right) \) sont premiers entre eux deux à deux, donc d’après le théorème de décomposition des noyaux,

> Proof. Necessary condition. Let \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) be the (distinct) eigenvalues of \( f \) and \( {E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) be the corresponding eigenspaces. Let \( P = \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{r}}\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) . The polynomial \( P \) is split in \( \mathbb{K}\left\lbrack X\right\rbrack \) and has only simple roots. Furthermore, the polynomials \( \left( {X - {\lambda }_{i}}\right) \) are pairwise coprime, so according to the primary decomposition theorem,

\[
\operatorname{Ker}P\left( f\right)  = {\bigoplus }_{i = 1}^{r}\operatorname{Ker}\left( {f - {\lambda }_{i}{\operatorname{Id}}_{E}}\right)  = {\bigoplus }_{i = 1}^{r}{E}_{{\lambda }_{i}}
\]

donc Ker \( P\left( f\right) = E \) car \( f \) est diagonalisable, c’est-à-dire \( P\left( f\right) = 0 \) .

> thus Ker \( P\left( f\right) = E \) because \( f \) is diagonalizable, that is to say \( P\left( f\right) = 0 \) .

Condition suffisante. Écrivons \( P = \alpha \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{r}}\right) \) avec les \( {\lambda }_{i} \in \mathbb{K} \) distincts et \( \alpha \neq 0 \) . Les \( {\lambda }_{i} \) étant distincts, les polynômes \( \left( {X - {\lambda }_{i}}\right) \) sont premiers entre eux deux à deux, donc d’après le théorème de décomposition des noyaux,

> Sufficient condition. Let us write \( P = \alpha \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{r}}\right) \) with the distinct \( {\lambda }_{i} \in \mathbb{K} \) and \( \alpha \neq 0 \) . Since the \( {\lambda }_{i} \) are distinct, the polynomials \( \left( {X - {\lambda }_{i}}\right) \) are pairwise coprime, so according to the primary decomposition theorem,

\[
E = \operatorname{Ker}P\left( f\right)  = \operatorname{Ker}\left( {f - {\lambda }_{1}{\operatorname{Id}}_{E}}\right)  \oplus  \cdots  \oplus  \operatorname{Ker}\left( {f - {\lambda }_{r}{\operatorname{Id}}_{E}}\right) .
\]

\( \left( *\right) \)

> Soit \( I = \left\{ {i \mid \operatorname{Ker}\left( {f - {\lambda }_{i}{\operatorname{Id}}_{E}}\right) \neq \{ 0\} }\right\} \) . Pour tout \( i \in I,{\lambda }_{i} \) est valeur propre de \( f \) et \( {E}_{{\lambda }_{i}} = \operatorname{Ker}(f - \; {\lambda }_{i}{\mathrm{{Id}}}_{E} \) ) n’est autre que le sous-espace propre correspondant. L’identité (*) s’écrit \( E = { \oplus }_{i \in I}{E}_{{\lambda }_{i}} \) , donc \( f \) est diagonalisable d’après le théorème 2 page 174.

Let \( I = \left\{ {i \mid \operatorname{Ker}\left( {f - {\lambda }_{i}{\operatorname{Id}}_{E}}\right) \neq \{ 0\} }\right\} \) . For all \( i \in I,{\lambda }_{i} \) is an eigenvalue of \( f \) and \( {E}_{{\lambda }_{i}} = \operatorname{Ker}(f - \; {\lambda }_{i}{\mathrm{{Id}}}_{E} \) ) is none other than the corresponding eigenspace. The identity (*) is written \( E = { \oplus }_{i \in I}{E}_{{\lambda }_{i}} \) , therefore \( f \) is diagonalizable according to theorem 2 on page 174.

> Conséquence . Il découle de ce dernier théorème la proposition 6 page 174. En effet, soit \( f \in \mathcal{L}\left( E\right) \) diagonalisable et \( F \) un s.e.v de \( E \) stable par \( f \) . Il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) scindé sur \( \mathbb{K} \) , à racines toutes simples, tel que \( P\left( f\right) = 0 \) . Alors \( P\left( {f}_{\mid F}\right) = 0 \) , donc \( {f}_{\mid F} \) est diagonalisable d'après le théorème 2.

Consequence. Proposition 6 on page 174 follows from this last theorem. Indeed, let \( f \in \mathcal{L}\left( E\right) \) be diagonalizable and \( F \) be a subspace of \( E \) stable by \( f \) . There exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) split over \( \mathbb{K} \) , with only simple roots, such that \( P\left( f\right) = 0 \) . Then \( P\left( {f}_{\mid F}\right) = 0 \) , therefore \( {f}_{\mid F} \) is diagonalizable according to theorem 2.
