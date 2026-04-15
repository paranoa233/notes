#### 2.3. Cayley-Hamilton Theorem

*Français : 2.3. Théorème de Cayley-Hamilton*

\( \rightarrow \) THÉORÉME 3 (CAYLEY-HAMILTON). Soit \( f \in \mathcal{L}\left( E\right) ,{P}_{f} \) son polynôme caractéristique. Alors \( {P}_{f}\left( f\right) = 0 \) .

> \( \rightarrow \) THEOREM 3 (CAYLEY-HAMILTON). Let \( f \in \mathcal{L}\left( E\right) ,{P}_{f} \) be its characteristic polynomial. Then \( {P}_{f}\left( f\right) = 0 \) .

Démonstration. Nous proposons deux démonstrations de ce théorème.

> Proof. We propose two proofs for this theorem.

Première démonstration. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) la matrice de \( f \) dans la base canonique de \( {\mathbb{K}}^{n} \) . Soit \( \mathbb{L} \) le corps des racines de \( {P}_{A} = {P}_{f} \) . On regarde \( A \) comme une matrice de \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) . D’après le théorème de trigonalisation, il existe une matrice \( T = \left( {t}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) triangulaire supérieure et semblable à \( A \) :

> First proof. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be the matrix of \( f \) in the canonical basis of \( {\mathbb{K}}^{n} \) . Let \( \mathbb{L} \) be the splitting field of \( {P}_{A} = {P}_{f} \) . We view \( A \) as a matrix in \( {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) . According to the triangularization theorem, there exists an upper triangular matrix \( T = \left( {t}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{L}\right) \) similar to \( A \) :

\[
T = \left( \begin{matrix} {t}_{1,1} & & & \left( {t}_{i, j}\right) \\   & {t}_{2,2} & & \backprime \\  0 & &  \ddots  & \\   & & & {t}_{n, n} \end{matrix}\right) .
\]

On a \( {P}_{f} = {P}_{T} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {t}_{i, i}}\right) \) . Soit \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) la base canonique de \( {\mathbb{L}}^{n}\left( {E}_{k}\right. \) est le vecteur colonne dont tous les éléments sont nuls sauf le \( k \) -ième qui vaut 1). Pour tout \( k \) , on pose \( {P}_{k} = \mathop{\prod }\limits_{{i = 1}}^{k}\left( {X - {t}_{i, i}}\right) \) . Nous allons montrer par récurrence sur \( k \in \{ 1,\ldots , n\} \) que

> We have \( {P}_{f} = {P}_{T} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {t}_{i, i}}\right) \) . Let \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be the canonical basis of \( {\mathbb{L}}^{n}\left( {E}_{k}\right. \) (is the column vector whose elements are all zero except the \( k \) -th which is 1). For all \( k \) , we set \( {P}_{k} = \mathop{\prod }\limits_{{i = 1}}^{k}\left( {X - {t}_{i, i}}\right) \) . We will show by induction on \( k \in \{ 1,\ldots , n\} \) that

\[
\forall i \in  \{ 1,\ldots , k\} ,\;\left\lbrack  {{P}_{k}\left( T\right) }\right\rbrack  {E}_{i} = 0.
\]

(*)

> Pour \( k = 1 \) , c’est vrai car \( T{E}_{1} = {t}_{1,1}{E}_{1} \) , donc \( \left( {T - {t}_{1,1}{I}_{n}}\right) {E}_{1} = 0 = {P}_{1}\left( T\right) {E}_{1} \) . Supposons le résultat vrai au rang \( k - 1 \) et montrons le au rang \( k \) . On a

For \( k = 1 \) , it is true because \( T{E}_{1} = {t}_{1,1}{E}_{1} \) , therefore \( \left( {T - {t}_{1,1}{I}_{n}}\right) {E}_{1} = 0 = {P}_{1}\left( T\right) {E}_{1} \) . Assume the result is true at rank \( k - 1 \) and show it at rank \( k \) . We have

\[
\forall i \in  \{ 1,\ldots , k - 1\} ,\;{P}_{k}\left( T\right) {E}_{i} = \left( {T - {t}_{k, k}{I}_{n}}\right) {P}_{k - 1}\left( T\right) {E}_{i} = 0,
\]

\[
{P}_{k}\left( T\right) {E}_{k} = {P}_{k - 1}\left( T\right)  \cdot  \left( {T - {t}_{k, k}{I}_{n}}\right) {E}_{k} = {P}_{k - 1}\left( T\right) \left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{{k - 1}}{t}_{i, k}{E}_{i}}\right\rbrack   = \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}{t}_{i, k}{P}_{k - 1}\left( T\right) {E}_{i} = 0.
\]

La propriété (*) est donc démontrée pour tout \( k \in \{ 1,\ldots , n\} \) . Elle est vraie en particulier pour \( k = n \) , donc \( {P}_{n}\left( T\right) = 0 \) . Or \( {P}_{T} = {P}_{n} \) donc ceci s’écrit \( {P}_{T}\left( T\right) = 0 \) , donc \( {P}_{f}\left( f\right) = 0 \) .

> The property (*) is therefore proven for all \( k \in \{ 1,\ldots , n\} \) . It is true in particular for \( k = n \) , so \( {P}_{n}\left( T\right) = 0 \) . However \( {P}_{T} = {P}_{n} \) so this is written \( {P}_{T}\left( T\right) = 0 \) , so \( {P}_{f}\left( f\right) = 0 \) .

Seconde démonstration (elle ne fait pas appel au corps des racines d'un polynôme).

> Second proof (it does not rely on the splitting field of a polynomial).

PRÉLIMINAIRES. Nous montrons d'abord que le polynôme caractéristique de la matrice

> PRELIMINARIES. We first show that the characteristic polynomial of the matrix

\[
A = \left( \begin{matrix} 0 & \cdots & 0 &  - {a}_{0} \\  1 &  \ddots  & \vdots & \vdots \\   &  \ddots  & 0 &  - {a}_{p - 2} \\   & & & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{p}\left( \mathbb{K}\right) .
\]

est \( {P}_{A}\left( X\right) = {\left( -1\right) }^{p}\left( {{X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0}}\right) \) (pour cette raison, la matrice \( A \) est appelée matrice compagnon du polynôme \( {X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0} \) ). Pour montrer ce préliminaire, nous procédons par récurrence sur \( p \) . Pour \( p = 1 \) , c’est évident. Supposons le résultat vrai au rang \( p \) , montrons le au rang \( p + 1 \) . En développant par rapport à la première ligne, on a

> is \( {P}_{A}\left( X\right) = {\left( -1\right) }^{p}\left( {{X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0}}\right) \) (for this reason, the matrix \( A \) is called the companion matrix of the polynomial \( {X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0} \) ). To show this preliminary result, we proceed by induction on \( p \) . For \( p = 1 \) , it is obvious. Assume the result is true at rank \( p \) , let us show it at rank \( p + 1 \) . By expanding with respect to the first row, we have

![bo_d7fjffs91nqc73erehlg_187_170_955_540_193_0.jpg](images/gourdon_algebra_probabilities_fr_en_004_bod7fjffs91nqc73erehlg1871709555401930.jpg)

![bo_d7fjffs91nqc73erehlg_187_425_1150_966_188_0.jpg](images/gourdon_algebra_probabilities_fr_en_005_bod7fjffs91nqc73erehlg18742511509661880.jpg)

et donc d'après l'hypothèse de récurrence

> and therefore according to the induction hypothesis

\[
{P}_{A}\left( X\right)  = {\left( -1\right) }^{p + 1}X\left( {{X}^{p} + {a}_{p}{X}^{p - 1} + \cdots  + {a}_{1}}\right)  + {\left( -1\right) }^{p + 1}{a}_{0} = {\left( -1\right) }^{p + 1}\left( {{X}^{p + 1} + {a}_{p}{X}^{p} + \cdots  + {a}_{1}X + {a}_{0}}\right) .
\]

Démontrons maintenant le théorème. Soit \( x \in E, x \neq 0 \) . Il existe un plus petit entier \( p > 0 \) tel que la famille \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p}\left( x\right) }\right) \) soit liée. La famille \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p - 1}\left( x\right) }\right) \) est donc libre et

> Let us now prove the theorem. Let \( x \in E, x \neq 0 \) . There exists a smallest integer \( p > 0 \) such that the family \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p}\left( x\right) }\right) \) is linearly dependent. The family \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p - 1}\left( x\right) }\right) \) is therefore linearly independent and

\[
\left( {\exists {a}_{0},\ldots ,{a}_{p - 1} \in  \mathbb{K}}\right) ,\;{f}^{p}\left( x\right)  + {a}_{p - 1}{f}^{p - 1}\left( x\right)  + \cdots  + {a}_{0}x = 0.
\]

\( \left( {* * }\right) \)

> Complétons \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p - 1}\left( x\right) }\right) \) en une base \( \mathcal{B} \) de \( E \) . Alors on a la forme par blocs

Let us extend \( \left( {x, f\left( x\right) ,\ldots ,{f}^{p - 1}\left( x\right) }\right) \) into a basis \( \mathcal{B} \) of \( E \) . Then we have the block form

\[
{\left\lbrack  f\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} A & B \\  0 & C \end{matrix}\right) \;\text{ avec }\;A = \left( \begin{matrix} 0 & \cdots & 0 &  - {a}_{0} \\  1 &  \ddots  & \vdots & \vdots \\   &  \ddots  & 0 &  - {a}_{p - 2} \\   & & 0 & 1 - {a}_{p - 1} \end{matrix}\right) .
\]

Or \( {P}_{f} = {P}_{A}{P}_{C} \) , donc \( {P}_{f}\left( f\right) \left( x\right) = {P}_{C}\left( f\right) \circ {P}_{A}\left( f\right) \left( x\right) \) , et d’après le préliminaire et d’après (**),

> However \( {P}_{f} = {P}_{A}{P}_{C} \) , so \( {P}_{f}\left( f\right) \left( x\right) = {P}_{C}\left( f\right) \circ {P}_{A}\left( f\right) \left( x\right) \) , and according to the preliminary result and (**),

\[
{P}_{A}\left( f\right) \left( x\right)  = {\left( -1\right) }^{p}\left( {{f}^{p}\left( x\right)  + {a}_{p - 1}{f}^{p - 1}\left( x\right)  + \cdots  + {a}_{0}x}\right)  = 0,
\]

donc \( {P}_{f}\left( f\right) \left( x\right) = 0 \) . Ceci est vrai pour tout \( x \) donc \( {P}_{f}\left( f\right) = 0 \) .

> so \( {P}_{f}\left( f\right) \left( x\right) = 0 \) . This is true for all \( x \) so \( {P}_{f}\left( f\right) = 0 \) .

Remarque 6. - En d'autres termes, le théorème dit que le polynôme minimal de \( f \) divise son polynôme caractéristique. Avec la proposition 2, on en déduit que

> Remark 6. - In other words, the theorem states that the minimal polynomial of \( f \) divides its characteristic polynomial. With proposition 2, we deduce that

\[
\text{ si }{P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{r}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}}\text{ , alors }{\Pi }_{f} = \mathop{\prod }\limits_{{i = 1}}^{r}{\left( X - {\lambda }_{i}\right) }^{{q}_{i}},\;1 \leq  {q}_{i} \leq  {r}_{i}\text{ . }
\]

- Ce théorème permet d'affirmer, compte tenu de la proposition 3 page 173, que \( f \in  \mathcal{L}\left( E\right) \) est nilpotent si et seulement si \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n} \) .

> - This theorem allows us to state, given proposition 3 on page 173, that \( f \in  \mathcal{L}\left( E\right) \) is nilpotent if and only if \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n} \) .
