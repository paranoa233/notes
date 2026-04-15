#### 5.5. Exercises

*Français : 5.5. Exercices*

EXERCICE 1. Soient \( E \) un \( \mathbb{R} \) -e.v.n et \( A, B \) deux parties de \( A \) . On note \( A + B = \{ a + \; b,\left( {a, b}\right) \in A \times B\} \) .

> EXERCISE 1. Let \( E \) be a \( \mathbb{R} \) -n.v.s. and \( A, B \) be two subsets of \( A \) . We denote \( A + B = \{ a + \; b,\left( {a, b}\right) \in A \times B\} \) .

a) Si \( A \) est ouvert (et \( B \) quelconque), montrer que \( A + B \) est ouvert.

> a) If \( A \) is open (and \( B \) is arbitrary), show that \( A + B \) is open.

b) Si \( A \) est compact et \( B \) fermé, montrer que \( A + B \) est fermé. Ce résultat subsiste-t-il si \( A \) est seulement supposé fermé?

> b) If \( A \) is compact and \( B \) is closed, show that \( A + B \) is closed. Does this result still hold if \( A \) is only assumed to be closed?

Solution. a) On a \( A + B = { \cup }_{b \in B}\left( {A+\{ b\} }\right) \) . Pour tout \( b \in B \) , il est clair que \( A + \{ b\} \) est un ouvert de \( E \) (si \( \mathrm{B}\left( {x,\rho }\right) \subset A,\mathrm{\;B}\left( {x + b,\rho }\right) \subset A + \{ b\} \) ). Donc \( A + B \) , réunion d’ouverts, est un ouvert.

> Solution. a) We have \( A + B = { \cup }_{b \in B}\left( {A+\{ b\} }\right) \) . For all \( b \in B \) , it is clear that \( A + \{ b\} \) is an open set of \( E \) (if \( \mathrm{B}\left( {x,\rho }\right) \subset A,\mathrm{\;B}\left( {x + b,\rho }\right) \subset A + \{ b\} \) ). Thus \( A + B \) , as a union of open sets, is open.

b) Soit \( \left( {z}_{n}\right) = {\left( {x}_{n} + {y}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( A + B \) , convergente dans \( E \) vers \( z \) , où \( \left( {x}_{n}\right) \) est une suite de \( A \) et \( \left( {y}_{n}\right) \) une suite de \( B \) . La compacité de \( A \) entraîne l’existence d’une sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) qui converge dans \( A \) . Notons \( x \in A \) sa limite. Comme \( \left( {z}_{\varphi \left( n\right) }\right) \) converge vers \( z,\left( {y}_{\varphi \left( n\right) }\right) = \left( {{z}_{\varphi \left( n\right) } - {x}_{\varphi \left( n\right) }}\right) \) converge vers \( z - x \) . Comme \( B \) est fermé, \( y = z - x \in B \) . Ainsi, \( z = x + y \in A + B \) , d’où le résultat.

> b) Let \( \left( {z}_{n}\right) = {\left( {x}_{n} + {y}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of \( A + B \) converging in \( E \) to \( z \) , where \( \left( {x}_{n}\right) \) is a sequence of \( A \) and \( \left( {y}_{n}\right) \) is a sequence of \( B \) . The compactness of \( A \) implies the existence of a subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) that converges in \( A \) . Let \( x \in A \) denote its limit. Since \( \left( {z}_{\varphi \left( n\right) }\right) \) converges to \( z,\left( {y}_{\varphi \left( n\right) }\right) = \left( {{z}_{\varphi \left( n\right) } - {x}_{\varphi \left( n\right) }}\right) \) converges to \( z - x \) . Since \( B \) is closed, \( y = z - x \in B \) . Thus, \( z = x + y \in A + B \) , hence the result.

Si \( A \) est seulement supposé fermé, le résultat est faux. Par exemple, dans le plan, les ensembles \( A = \left\{ {\left( {x,{e}^{x}}\right) , x \in \mathbb{R}}\right\} \) et \( B = \mathbb{R} \times \{ 0\} \) sont fermés et pourtant \( A + B = \mathbb{R} \times \rbrack 0, + \infty \lbrack \) n’est pas fermé. On peut donner un autre contre exemple dans \( \mathbb{R} \) , en considérant les ensembles \( \mathbb{Z} \) et \( x\mathbb{Z} \) (avec \( x \in \mathbb{R} \smallsetminus \mathbb{Q} \) ). Ces ensembles sont fermés, et \( \mathbb{Z} + x\mathbb{Z} \) est dense dans \( \mathbb{R} \) (voir l’exercice 5 page 205). Si ce dernier était fermé, il serait égal à \( \mathbb{R} \) tout entier, ce qui est impossible puisque \( \mathbb{Z} + x\mathbb{Z} \) est dénombrable et que \( \mathbb{R} \) ne l’est pas.

> If \( A \) is only assumed to be closed, the result is false. For example, in the plane, the sets \( A = \left\{ {\left( {x,{e}^{x}}\right) , x \in \mathbb{R}}\right\} \) and \( B = \mathbb{R} \times \{ 0\} \) are closed, yet \( A + B = \mathbb{R} \times \rbrack 0, + \infty \lbrack \) is not closed. Another counterexample can be given in \( \mathbb{R} \) by considering the sets \( \mathbb{Z} \) and \( x\mathbb{Z} \) (with \( x \in \mathbb{R} \smallsetminus \mathbb{Q} \) ). These sets are closed, and \( \mathbb{Z} + x\mathbb{Z} \) is dense in \( \mathbb{R} \) (see exercise 5 on page 205). If the latter were closed, it would be equal to the entire space \( \mathbb{R} \) , which is impossible since \( \mathbb{Z} + x\mathbb{Z} \) is countable and \( \mathbb{R} \) is not.

EXERCICE 2. Soit \( K \) un compact convexe d’un e.v.n et \( f : K \rightarrow K \) une application continue telle que

> EXERCISE 2. Let \( K \) be a compact convex subset of a n.v.s. and \( f : K \rightarrow K \) a continuous map such that

\[
\forall \left( {x, y}\right)  \in  {K}^{2},\;\parallel f\left( x\right)  - f\left( y\right) \parallel  \leq  \parallel x - y\parallel .
\]

Montrer que \( f \) admet au moins un point fixe.

> Show that \( f \) admits at least one fixed point.

Solution. Si \( f \) était \( k \) -contractante (avec \( k < 1 \) ), le résultat serait vrai (théorème du point fixe, page 21). Fixons \( a \in K \) . La convexité de \( K \) nous invite à poser, pour tout entier naturel non nul \( n \)

> Solution. If \( f \) were \( k \) -contracting (with \( k < 1 \) ), the result would be true (fixed-point theorem, page 21). Let us fix \( a \in K \) . The convexity of \( K \) invites us to define, for every non-zero natural number \( n \)

\[
{f}_{n} : K \rightarrow  K\;x \mapsto  \frac{1}{n}a + \left( {1 - \frac{1}{n}}\right) f\left( x\right) .
\]

L’application \( {f}_{n} \) est bien à valeurs dans \( K \) car \( K \) est convexe. D’autre part,

> The map \( {f}_{n} \) indeed takes values in \( K \) because \( K \) is convex. On the other hand,

\[
\forall n \in  {\mathbb{N}}^{ * },\forall \left( {x, y}\right)  \in  {K}^{2},\;\begin{Vmatrix}{{f}_{n}\left( x\right)  - {f}_{n}\left( y\right) }\end{Vmatrix} = \left( {1 - \frac{1}{n}}\right) \begin{Vmatrix}{f\left( x\right)  - f\left( y\right) }\end{Vmatrix} \leq  \left( {1 - \frac{1}{n}}\right) \parallel x - y\parallel ,
\]

donc \( {f}_{n} \) est \( \left( {1 - 1/n}\right) \) -contractante. Comme \( K \) est compact, \( K \) est complet, et le théorème du point fixe nous assure l’existence de \( {x}_{n} \in K \) tel que \( {f}_{n}\left( {x}_{n}\right) = {x}_{n} \) . La suite \( \left( {x}_{n}\right) \) prend ses valeurs dans le compact \( K \) , on peut donc en extraire une sous-suite convergente \( \left( {x}_{\varphi \left( n\right) }\right) \) , dont la limite \( x \) appartient à \( K \) . Grâce à l’inégalité

> therefore \( {f}_{n} \) is \( \left( {1 - 1/n}\right) \) -contracting. Since \( K \) is compact, \( K \) is complete, and the fixed-point theorem ensures the existence of \( {x}_{n} \in K \) such that \( {f}_{n}\left( {x}_{n}\right) = {x}_{n} \) . The sequence \( \left( {x}_{n}\right) \) takes its values in the compact set \( K \) , so we can extract a convergent subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) , whose limit \( x \) belongs to \( K \) . Thanks to the inequality

\[
\begin{Vmatrix}{f\left( x\right)  - {f}_{n}\left( {x}_{n}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{f\left( x\right)  - {f}_{n}\left( x\right) }\end{Vmatrix} + \begin{Vmatrix}{{f}_{n}\left( x\right)  - {f}_{n}\left( {x}_{n}\right) }\end{Vmatrix} \leq  \frac{1}{n}\left( {\parallel a\parallel  + \parallel f\left( x\right) \parallel }\right)  + \begin{Vmatrix}{x - {x}_{n}}\end{Vmatrix}
\]

on voit que \( \left( {{f}_{\varphi \left( n\right) }\left( {x}_{\varphi \left( n\right) }\right) }\right) \) converge vers \( f\left( x\right) \) . En passant à la limite dans l’égalité \( {f}_{\varphi \left( n\right) }\left( {x}_{\varphi \left( n\right) }\right) = \; {x}_{\varphi \left( n\right) } \) , on en déduit \( f\left( x\right) = x \) , d’où le résultat.

> we see that \( \left( {{f}_{\varphi \left( n\right) }\left( {x}_{\varphi \left( n\right) }\right) }\right) \) converges to \( f\left( x\right) \) . By passing to the limit in the equality \( {f}_{\varphi \left( n\right) }\left( {x}_{\varphi \left( n\right) }\right) = \; {x}_{\varphi \left( n\right) } \) , we deduce \( f\left( x\right) = x \) , hence the result.

Remarque. Plus généralement, on peut montrer que toute application continue d'un convexe compact dans lui même admet au moins un point fixe (théorème de Brouwer).

> Remark. More generally, it can be shown that any continuous map from a compact convex set into itself admits at least one fixed point (Brouwer's theorem).

EXERCICE 3. Montrer qu’un e.v.n \( E \) est complet si et seulement si toute série \( \sum {u}_{n} \) absolument convergente (i. e. telle que \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converge) est convergente.

> EXERCISE 3. Show that a normed vector space \( E \) is complete if and only if every absolutely convergent series \( \sum {u}_{n} \) (i.e., such that \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converges) is convergent.

Solution. Condition nécessaire. Si \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converge, alors la suite \( \left( {S}_{n}\right) \) associée à la série \( \sum {u}_{n} \) définie par \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) est de Cauchy car

> Solution. Necessary condition. If \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converges, then the sequence \( \left( {S}_{n}\right) \) associated with the series \( \sum {u}_{n} \) defined by \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} \) is Cauchy because

\[
\forall p < q,\;\begin{Vmatrix}{{S}_{p} - {S}_{q}}\end{Vmatrix} = \begin{Vmatrix}{\mathop{\sum }\limits_{{k = p + 1}}^{q}{u}_{k}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = p + 1}}^{q}\begin{Vmatrix}{u}_{k}\end{Vmatrix}.
\]

Comme \( E \) est complet, \( \left( {S}_{n}\right) \) converge donc, c’est-à-dire \( \sum {u}_{n} \) converge.

> Since \( E \) is complete, \( \left( {S}_{n}\right) \) converges, that is to say \( \sum {u}_{n} \) converges.

Condition suffisante. Soit \( \left( {S}_{n}\right) \) une suite de Cauchy de \( E \) . D’après le critère de Cauchy,

> Sufficient condition. Let \( \left( {S}_{n}\right) \) be a Cauchy sequence in \( E \) . According to the Cauchy criterion,

\( - \exists \varphi \left( 0\right) \in \mathbb{N},\forall n \geq \varphi \left( 0\right) ,\;\begin{Vmatrix}{{S}_{n} - {S}_{\varphi \left( 0\right) }}\end{Vmatrix} \leq 1 \) , de même

> \( - \exists \varphi \left( 0\right) \in \mathbb{N},\forall n \geq \varphi \left( 0\right) ,\;\begin{Vmatrix}{{S}_{n} - {S}_{\varphi \left( 0\right) }}\end{Vmatrix} \leq 1 \) , likewise

\( - \exists \varphi \left( 1\right) > \varphi \left( 0\right) ,\forall n \geq \varphi \left( 1\right) ,\;\begin{Vmatrix}{{S}_{n} - {S}_{\varphi \left( 1\right) }}\end{Vmatrix} \leq \frac{1}{2}, \)

> - on construit ainsi par récurrence \( \varphi \left( k\right)  > \varphi \left( {k - 1}\right) \) tel que \( \forall n \geq  \varphi \left( k\right) ,\;\begin{Vmatrix}{{S}_{n} - {S}_{\varphi \left( k\right) }}\end{Vmatrix} \leq  \frac{1}{{2}^{k}} \) . Pour tout \( k \in  \mathbb{N} \) , on pose \( {u}_{k} = {S}_{\varphi \left( {k + 1}\right) } - {S}_{\varphi \left( k\right) } \) . Par construction, \( \begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq  {2}^{-k} \) donc \( \sum {u}_{k} \) est absolument convergente, donc convergente. Or \( \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} = {S}_{\varphi \left( {n + 1}\right) } - {S}_{\varphi \left( 0\right) } \) , donc \( \left( {S}_{\varphi \left( n\right) }\right) \) converge. Une suite de Cauchy admettant une sous-suite convergente converge, d'où le résultat.

- we thus construct by induction \( \varphi \left( k\right)  > \varphi \left( {k - 1}\right) \) such that \( \forall n \geq  \varphi \left( k\right) ,\;\begin{Vmatrix}{{S}_{n} - {S}_{\varphi \left( k\right) }}\end{Vmatrix} \leq  \frac{1}{{2}^{k}} \) . For all \( k \in  \mathbb{N} \) , we set \( {u}_{k} = {S}_{\varphi \left( {k + 1}\right) } - {S}_{\varphi \left( k\right) } \) . By construction, \( \begin{Vmatrix}{u}_{k}\end{Vmatrix} \leq  {2}^{-k} \) therefore \( \sum {u}_{k} \) is absolutely convergent, and thus convergent. However \( \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} = {S}_{\varphi \left( {n + 1}\right) } - {S}_{\varphi \left( 0\right) } \) , so \( \left( {S}_{\varphi \left( n\right) }\right) \) converges. A Cauchy sequence admitting a convergent subsequence converges, hence the result.

> EXERCICE 4. 1 / Soit \( A \) une \( \mathbb{R} \) -algèbre normée (i. e. une algèbre munie d’une norme \( \parallel \) . \( \parallel \) vérifiant \( \parallel {xy}\parallel \leq \parallel x\parallel \cdot \parallel y\parallel \) pour tout \( \left( {x, y}\right) \in {A}^{2} \) ) unitaire et complète.

EXERCISE 4. 1 / Let \( A \) be a unital and complete normed \( \mathbb{R} \) -algebra (i.e., an algebra equipped with a norm \( \parallel \) satisfying \( \parallel {xy}\parallel \leq \parallel x\parallel \cdot \parallel y\parallel \) for all \( \left( {x, y}\right) \in {A}^{2} \) ).

> a) Si \( x \in A \) et si \( \parallel x\parallel < 1 \) , si 1 désigne l’élément unité de \( A \) , montrer que \( 1 - x \) est inversible dans \( A \) .

a) If \( x \in A \) and if \( \parallel x\parallel < 1 \), if 1 denotes the identity element of \( A \), show that \( 1 - x \) is invertible in \( A \).

> b) Montrer que l’ensemble des inversibles de \( A \) est un ouvert de \( A \) .

b) Show that the set of invertible elements of \( A \) is an open subset of \( A \).

> c) Soit \( \varphi : A \rightarrow \mathbb{R} \) un morphisme d’algèbre. Montrer que \( \varphi \) est continue.

c) Let \( \varphi : A \rightarrow \mathbb{R} \) be an algebra morphism. Show that \( \varphi \) is continuous.

> 2 / Soit \( E \) un \( \mathbb{R} \) -espace de Banach et \( u \in {\mathcal{L}}_{c}\left( E\right) \) . On appelle spectre de \( u \) l’ensemble des réels \( \lambda \) tels que \( u - \lambda \operatorname{Id} \notin \mathcal{G}{\ell }_{c}\left( E\right) \) , où \( \mathcal{G}{\ell }_{c}\left( E\right) \) désigne l’ensemble des \( v \in {\mathcal{L}}_{c}\left( E\right) \) tels que \( v \) est inversible et \( {v}^{-1} \) est continu. Montrer que le spectre de \( u \) est compact.

2 / Let \( E \) be a \( \mathbb{R} \)-Banach space and \( u \in {\mathcal{L}}_{c}\left( E\right) \). The spectrum of \( u \) is defined as the set of real numbers \( \lambda \) such that \( u - \lambda \operatorname{Id} \notin \mathcal{G}{\ell }_{c}\left( E\right) \), where \( \mathcal{G}{\ell }_{c}\left( E\right) \) denotes the set of \( v \in {\mathcal{L}}_{c}\left( E\right) \) such that \( v \) is invertible and \( {v}^{-1} \) is continuous. Show that the spectrum of \( u \) is compact.

> Solution. 1/ a) On ne fait que réécrire la démonstration de la proposition 2 dans le cas plus général d’une algèbre normée. La série \( \sum {x}^{n} \) converge absolument car \( \begin{Vmatrix}{x}^{n}\end{Vmatrix} \leq \parallel x{\parallel }^{n} \) et \( \parallel x\parallel < 1 \) , et comme \( A \) est complet, elle converge. Notons \( y \) sa somme. Alors

Solution. 1/ a) We simply rewrite the proof of proposition 2 in the more general case of a normed algebra. The series \( \sum {x}^{n} \) converges absolutely because \( \begin{Vmatrix}{x}^{n}\end{Vmatrix} \leq \parallel x{\parallel }^{n} \) and \( \parallel x\parallel < 1 \), and since \( A \) is complete, it converges. Let \( y \) denote its sum. Then

\[
\left( {1 - x}\right) y = y - {xy} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{x}^{n} = 1,
\]

de même \( y\left( {1 - x}\right) = 1 \) . Donc \( \left( {1 - x}\right) \) est inversible, son inverse est \( y = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n} \) .

> similarly \( y\left( {1 - x}\right) = 1 \). Thus \( \left( {1 - x}\right) \) is invertible, its inverse is \( y = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n} \).

b) Soit \( {x}_{0} \in A \) un élément inversible. Si \( h \in A,\parallel h\parallel < {\begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix}}^{-1} \) , on a \( \begin{Vmatrix}{{x}_{0}^{-1}h}\end{Vmatrix} \leq \begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix} \cdot \parallel h\parallel < 1 \) . D’après la question précédente, \( 1 + {x}_{0}^{-1}h = 1 - \left( {-{x}_{0}^{-1}h}\right) \) est inversible. On en déduit que \( {x}_{0} + h = {x}_{0}\left( {1 + {x}_{0}^{-1}h}\right) \) est inversible (son inverse est \( {\left( 1 + {x}_{0}^{-1}h\right) }^{-1}{x}_{0}^{-1} \) ). La boule de centre \( {x}_{0} \) de rayon \( 1/\begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix} \) est donc incluse dans l’ensemble des inversibles, d’où le résultat.

> b) Let \( {x}_{0} \in A \) be an invertible element. If \( h \in A,\parallel h\parallel < {\begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix}}^{-1} \), we have \( \begin{Vmatrix}{{x}_{0}^{-1}h}\end{Vmatrix} \leq \begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix} \cdot \parallel h\parallel < 1 \). According to the previous question, \( 1 + {x}_{0}^{-1}h = 1 - \left( {-{x}_{0}^{-1}h}\right) \) is invertible. We deduce that \( {x}_{0} + h = {x}_{0}\left( {1 + {x}_{0}^{-1}h}\right) \) is invertible (its inverse is \( {\left( 1 + {x}_{0}^{-1}h\right) }^{-1}{x}_{0}^{-1} \)). The ball centered at \( {x}_{0} \) with radius \( 1/\begin{Vmatrix}{x}_{0}^{-1}\end{Vmatrix} \) is therefore included in the set of invertible elements, hence the result.

c) Si \( \varphi \) est nulle, c’est terminé. Sinon, il existe \( x \in A \) tel que \( \varphi \left( x\right) \neq 0 \) . On a alors \( \varphi \left( x\right) = \; \varphi \left( {1 \cdot x}\right) = \varphi \left( 1\right) \varphi \left( x\right) \) , donc \( \varphi \left( 1\right) = 1 \) . Montrons maintenant que si \( \parallel x\parallel = 1 \) , alors \( \left| {\varphi \left( x\right) }\right| \leq 1 \) , ce qui montrera la continuité de \( \varphi \) (un morphisme d’algèbre est linéaire). Raisonnons par l’absurde et supposons l’existence de \( x \in A,\parallel x\parallel = 1 \) , tel que \( \lambda = \varphi \left( x\right) \) vérifie \( \left| \lambda \right| > 1 \) . Alors \( \begin{Vmatrix}{\frac{1}{\lambda }x}\end{Vmatrix} < 1 \) , donc \( 1 - \frac{1}{\lambda }x \) est inversible, donc \( \lambda \cdot 1 - x \) est inversible. Désignons par \( y \) son inverse. On a

> c) If \( \varphi \) is zero, we are done. Otherwise, there exists \( x \in A \) such that \( \varphi \left( x\right) \neq 0 \) . We then have \( \varphi \left( x\right) = \; \varphi \left( {1 \cdot x}\right) = \varphi \left( 1\right) \varphi \left( x\right) \) , so \( \varphi \left( 1\right) = 1 \) . Let us now show that if \( \parallel x\parallel = 1 \) , then \( \left| {\varphi \left( x\right) }\right| \leq 1 \) , which will show the continuity of \( \varphi \) (an algebra morphism is linear). Let us reason by contradiction and assume the existence of \( x \in A,\parallel x\parallel = 1 \) such that \( \lambda = \varphi \left( x\right) \) satisfies \( \left| \lambda \right| > 1 \) . Then \( \begin{Vmatrix}{\frac{1}{\lambda }x}\end{Vmatrix} < 1 \) , so \( 1 - \frac{1}{\lambda }x \) is invertible, so \( \lambda \cdot 1 - x \) is invertible. Let us denote its inverse by \( y \) . We have

\[
\varphi \left( {\left( {\lambda  \cdot  1 - x}\right) y}\right)  = \varphi \left( 1\right)  = 1 = \varphi \left( {\lambda  \cdot  1 - x}\right) \varphi \left( y\right) ,
\]

ce qui est absurde car \( \varphi \left( {\lambda \cdot 1 - x}\right) = {\lambda \varphi }\left( 1\right) - \varphi \left( x\right) = 0 \) .

> which is absurd because \( \varphi \left( {\lambda \cdot 1 - x}\right) = {\lambda \varphi }\left( 1\right) - \varphi \left( x\right) = 0 \) .

\( \mathbf{2}/ \) Si \( A = {\mathcal{L}}_{c}\left( E\right) , A \) est une algèbre normée complète. D’après \( 1/ \) b), l’ensemble \( \mathcal{G}{\ell }_{c}\left( E\right) \) des inversibles de \( A \) est un ouvert, et l’application \( \varphi : \lambda \mapsto u - \lambda \operatorname{Id} \) étant continue, on en déduit que le spectre \( S \) de \( u \) est fermé car \( S = {\varphi }^{-1}\left( {A \smallsetminus \mathcal{G}{\ell }_{c}\left( E\right) }\right) \) .

> \( \mathbf{2}/ \) If \( A = {\mathcal{L}}_{c}\left( E\right) , A \) is a complete normed algebra. According to \( 1/ \) b), the set \( \mathcal{G}{\ell }_{c}\left( E\right) \) of invertible elements of \( A \) is an open set, and since the map \( \varphi : \lambda \mapsto u - \lambda \operatorname{Id} \) is continuous, we deduce that the spectrum \( S \) of \( u \) is closed because \( S = {\varphi }^{-1}\left( {A \smallsetminus \mathcal{G}{\ell }_{c}\left( E\right) }\right) \) .

Le spectre \( S \) est également borné. En effet, \( S \subset \left\lbrack {-\parallel u\parallel ,\parallel u\parallel }\right\rbrack \) car si \( \lambda > \parallel u\parallel \) , on a \( \begin{Vmatrix}{\frac{1}{\lambda }u}\end{Vmatrix} < 1 \) donc Id \( - \frac{1}{\lambda }u \) est dans \( \mathcal{G}{\ell }_{c}\left( E\right) \) , donc \( u - \lambda \) Id est dans \( \mathcal{G}{\ell }_{c}\left( E\right) \) .

> The spectrum \( S \) is also bounded. Indeed, \( S \subset \left\lbrack {-\parallel u\parallel ,\parallel u\parallel }\right\rbrack \) because if \( \lambda > \parallel u\parallel \) , we have \( \begin{Vmatrix}{\frac{1}{\lambda }u}\end{Vmatrix} < 1 \) so Id \( - \frac{1}{\lambda }u \) is in \( \mathcal{G}{\ell }_{c}\left( E\right) \) , therefore \( u - \lambda \) Id is in \( \mathcal{G}{\ell }_{c}\left( E\right) \) .

Finalement, \( S \) , fermé borné de \( \mathbb{R} \) , est compact.

> Finally, \( S \) , a closed bounded set of \( \mathbb{R} \) , is compact.

Remarque. - Si \( E \) est un espace de Banach et si \( u \in {\mathcal{L}}_{c}\left( E\right) \) est inversible, alors \( {u}^{-1} \) est forcément continu. Ce résultat est appelé théorème de Banach, il est démontré à l'annexe A, exercice 6 page 423.

> Remark. - If \( E \) is a Banach space and if \( u \in {\mathcal{L}}_{c}\left( E\right) \) is invertible, then \( {u}^{-1} \) is necessarily continuous. This result is called the Banach theorem; it is proven in Appendix A, exercise 6 on page 423.

- La notion de spectre de \( u \in  {\mathcal{L}}_{c}\left( E\right) \) généralise celle des valeurs propres d’un endomor-phisme en dimension finie.

> - The notion of the spectrum of \( u \in  {\mathcal{L}}_{c}\left( E\right) \) generalizes that of the eigenvalues of an endomorphism in finite dimension.

EXERCICE 5. On note \( {\ell }^{1} \) le \( \mathbb{R} \) -e.v des suites réelles \( \left( {u}_{n}\right) \) telles que \( \sum \left| {u}_{n}\right| \) converge, muni de la norme \( {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{1} = \mathop{\sum }\limits_{{n = 0}}^{\infty }\left| {u}_{n}\right| \) . On note \( {\ell }^{\infty } \) le \( \mathbb{R} \) -e.v des suites réelles \( \left( {u}_{n}\right) \) bornées, muni de la norme \( {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{n}\left| {u}_{n}\right| \) .

> EXERCISE 5. Let \( {\ell }^{1} \) be the \( \mathbb{R} \) -vector space of real sequences \( \left( {u}_{n}\right) \) such that \( \sum \left| {u}_{n}\right| \) converges, equipped with the norm \( {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{1} = \mathop{\sum }\limits_{{n = 0}}^{\infty }\left| {u}_{n}\right| \) . Let \( {\ell }^{\infty } \) be the \( \mathbb{R} \) -vector space of bounded real sequences \( \left( {u}_{n}\right) \) , equipped with the norm \( {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{\infty } = \mathop{\sup }\limits_{n}\left| {u}_{n}\right| \) .

Montrer que le dual topologique \( {\left( {\ell }^{1}\right) }^{\prime } \) de \( {\ell }^{1} \) (i. e. l’e.v des formes linéaires continues sur \( {\ell }^{1} \) ) s’identifie à \( {\ell }^{\infty } \) à une isométrie bijective près.

> Show that the topological dual \( {\left( {\ell }^{1}\right) }^{\prime } \) of \( {\ell }^{1} \) (i.e., the vector space of continuous linear forms on \( {\ell }^{1} \) ) is identified with \( {\ell }^{\infty } \) via a bijective isometry.

Solution. Pour toute suite \( k = \left( {k}_{n}\right) \) de \( {\ell }^{\infty } \) , on définit l’application

> Solution. For any sequence \( k = \left( {k}_{n}\right) \) in \( {\ell }^{\infty } \) , we define the map

\[
{\Phi }_{k} : {\ell }^{1} \rightarrow  \mathbb{R}\;\left( {u}_{n}\right)  \mapsto  \mathop{\sum }\limits_{{n = 0}}^{\infty }{k}_{n}{u}_{n}
\]

(la série \( \sum {k}_{n}{u}_{n} \) converge absolument car \( \left( {k}_{n}\right) \) est bornée et \( \sum {u}_{n} \) converge absolument). Il est clair que \( {\Phi }_{k} \) est une forme linéaire de \( {\ell }^{1} \) . Elle est même continue car

> (the series \( \sum {k}_{n}{u}_{n} \) converges absolutely because \( \left( {k}_{n}\right) \) is bounded and \( \sum {u}_{n} \) converges absolutely). It is clear that \( {\Phi }_{k} \) is a linear form on \( {\ell }^{1} \) . It is also continuous because

\[
\left| {{\Phi }_{k}\left\lbrack  \left( {u}_{n}\right) \right\rbrack  }\right|  \leq  \mathop{\sum }\limits_{{n = 0}}^{\infty }\left| {k}_{n}\right| \left| {u}_{n}\right|  \leq  {\begin{Vmatrix}\left( {k}_{n}\right) \end{Vmatrix}}_{\infty } \cdot  {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{1},
\]

et de plus cette inégalité montre que \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \leq \parallel k{\parallel }_{\infty } \) .

> and furthermore, this inequality shows that \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \leq \parallel k{\parallel }_{\infty } \) .

On a même \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} = \parallel k{\parallel }_{\infty } \) . En effet, pour \( n \in \mathbb{N} \) , désignons par \( {e}_{n} \) la suite dont tous les éléments sont nuls sauf le \( n \) -ième qui vaut 1 . On a \( \left| {{\Phi }_{k}\left( {e}_{n}\right) }\right| = \left| {k}_{n}\right| \) et \( {\begin{Vmatrix}{e}_{n}\end{Vmatrix}}_{1} = 1 \) , donc \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \geq \left| {k}_{n}\right| \) pour tout entier naturel \( n \) , d’où on tire \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \geq \parallel k{\parallel }_{\infty } \) , et donc \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} = \parallel k{\parallel }_{\infty } \) .

> We even have \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} = \parallel k{\parallel }_{\infty } \) . Indeed, for \( n \in \mathbb{N} \) , let \( {e}_{n} \) denote the sequence whose elements are all zero except for the \( n \) -th, which is 1. We have \( \left| {{\Phi }_{k}\left( {e}_{n}\right) }\right| = \left| {k}_{n}\right| \) and \( {\begin{Vmatrix}{e}_{n}\end{Vmatrix}}_{1} = 1 \) , so \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \geq \left| {k}_{n}\right| \) for every natural number \( n \) , from which we derive \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} \geq \parallel k{\parallel }_{\infty } \) , and thus \( \begin{Vmatrix}{\Phi }_{k}\end{Vmatrix} = \parallel k{\parallel }_{\infty } \) .

L’application linéaire \( \Phi : {\ell }^{\infty } \rightarrow {\left( {\ell }^{1}\right) }^{\prime }\;k = \left( {k}_{n}\right) \mapsto {\Phi }_{k} \) est donc une isométrie, en particulier injective.

> The linear map \( \Phi : {\ell }^{\infty } \rightarrow {\left( {\ell }^{1}\right) }^{\prime }\;k = \left( {k}_{n}\right) \mapsto {\Phi }_{k} \) is therefore an isometry, and in particular, injective.

Il nous reste à montrer que \( \Phi \) est surjective. Soit \( \varphi \in {\left( {\ell }^{1}\right) }^{\prime } \) . Comme \( \varphi \) est continue,

> It remains to show that \( \Phi \) is surjective. Let \( \varphi \in {\left( {\ell }^{1}\right) }^{\prime } \) . Since \( \varphi \) is continuous,

\[
\exists M > 0,\forall \left( {u}_{n}\right)  \in  {\ell }^{1},\;\left| {\varphi \left\lbrack  \left( {u}_{n}\right) \right\rbrack  }\right|  \leq  M \cdot  {\begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix}}_{1}.
\]

La suite \( k = \left( {k}_{n}\right) \) définie par \( {k}_{n} = \varphi \left( {e}_{n}\right) \) est donc une suite de \( {\ell }^{\infty } \) et

> The sequence \( k = \left( {k}_{n}\right) \) defined by \( {k}_{n} = \varphi \left( {e}_{n}\right) \) is therefore a sequence in \( {\ell }^{\infty } \) and

\[
\forall N \in  \mathbb{N},\;\varphi \left( {\mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}{e}_{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}\varphi \left( {e}_{n}\right)  = \mathop{\sum }\limits_{{n = 0}}^{N}{k}_{n}{u}_{n} = {\Phi }_{k}\left( {\mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}{e}_{n}}\right) .
\]

Or la suite \( {\left( \mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}{e}_{n}\right) }_{N \in \mathbb{N}} \) de \( {\ell }^{1} \) converge vers \( \left( {u}_{n}\right) \) dans \( {\ell }^{1} \) , et \( \varphi \) et \( {\Phi }_{k} \) étant continues, on en déduit \( \varphi \left\lbrack \left( {u}_{n}\right) \right\rbrack = {\Phi }_{k}\left\lbrack \left( {u}_{n}\right) \right\rbrack \) . Ceci est vrai pour tout \( \left( {u}_{n}\right) \in {\ell }^{1} \) , donc \( \varphi = {\Phi }_{k} \) , d’où le résultat.

> Now, the sequence \( {\left( \mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}{e}_{n}\right) }_{N \in \mathbb{N}} \) of \( {\ell }^{1} \) converges to \( \left( {u}_{n}\right) \) in \( {\ell }^{1} \), and since \( \varphi \) and \( {\Phi }_{k} \) are continuous, we deduce \( \varphi \left\lbrack \left( {u}_{n}\right) \right\rbrack = {\Phi }_{k}\left\lbrack \left( {u}_{n}\right) \right\rbrack \). This is true for all \( \left( {u}_{n}\right) \in {\ell }^{1} \), therefore \( \varphi = {\Phi }_{k} \), hence the result.

EXERCICE 6 (CONVEXES, THÉORÉME DE CARATHÉODORY ET APPLICATION). 1/ Soit \( E \) un e.v.n et \( C \) un convexe de \( E \) . Montrer que \( \bar{C} \) et \( \overset{ \circ }{C} \) sont convexes.

> EXERCISE 6 (CONVEX SETS, CARATHÉODORY'S THEOREM AND APPLICATION). 1/ Let \( E \) be a n.v.s. and \( C \) a convex subset of \( E \). Show that \( \bar{C} \) and \( \overset{ \circ }{C} \) are convex.

2/a) (Théorème de Carathéodory.) Soit \( E \) un \( \mathbb{R} \) -e.v de dimension \( n \in {\mathbb{N}}^{ * } \) , et soit \( x \in E \) le barycentre de \( p \) vecteurs \( {x}_{1},\ldots ,{x}_{p} \in E \) affectés de coefficients positifs (i. e. \( \exists {\lambda }_{1},\ldots ,{\lambda }_{p} \in \; {\mathbb{R}}^{ + },\mathop{\sum }\limits_{i}{\lambda }_{i} = 1 \) avec \( x = \mathop{\sum }\limits_{i}{\lambda }_{i}{x}_{i} \) ). Montrer qu’il existe \( I \subset \{ 1,\ldots , p\} \) tel que Card \( I \leq \; n + 1 \) et tel que \( x \) soit barycentre des \( {\left( {x}_{i}\right) }_{i \in I} \) affectés de coefficients positifs.

> 2/a) (Carathéodory's Theorem.) Let \( E \) be a \( \mathbb{R} \)-v.s. of dimension \( n \in {\mathbb{N}}^{ * } \), and let \( x \in E \) be the barycenter of \( p \) vectors \( {x}_{1},\ldots ,{x}_{p} \in E \) assigned positive coefficients (i.e., \( \exists {\lambda }_{1},\ldots ,{\lambda }_{p} \in \; {\mathbb{R}}^{ + },\mathop{\sum }\limits_{i}{\lambda }_{i} = 1 \) with \( x = \mathop{\sum }\limits_{i}{\lambda }_{i}{x}_{i} \)). Show that there exists \( I \subset \{ 1,\ldots , p\} \) such that Card \( I \leq \; n + 1 \) and such that \( x \) is the barycenter of \( {\left( {x}_{i}\right) }_{i \in I} \) assigned positive coefficients.

b) (Application.) Soit \( E \) un \( \mathbb{R} \) -e.v.n de dimension finie et \( A \) une partie compacte de \( E \) . Montrer que Conv \( \left( A\right) \) , l’enveloppe convexe de \( A \) , est compacte.

> b) (Application.) Let \( E \) be a \( \mathbb{R} \)-n.v.s. of finite dimension and \( A \) a compact subset of \( E \). Show that Conv \( \left( A\right) \), the convex hull of \( A \), is compact.

Solution. 1 / L’adhérence \( \bar{C} \) de \( C \) est convexe. En effet. Donnons nous deux points \( x \) et \( y \) de \( \bar{C} \) et un réel \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . Il existe deux suites \( \left( {x}_{n}\right) \) et \( \left( {y}_{n}\right) \) de \( C \) qui convergent respectivement vers \( x \) et \( y \) . Pour tout \( n \in \mathbb{N} \) , on a \( \lambda {x}_{n} + \left( {1 - \lambda }\right) {y}_{n} \in C \) , et en passant à la limite lorsque \( n \) tend vers l’infini, on en déduit que \( {\lambda x} + \left( {1 - \lambda }\right) y \) , limite de points de \( C \) , appartient à \( \bar{C} \) .

> Solution. 1/ The closure \( \bar{C} \) of \( C \) is convex. Indeed, let us take two points \( x \) and \( y \) in \( \bar{C} \) and a real number \( \lambda \in \left\lbrack {0,1}\right\rbrack \). There exist two sequences \( \left( {x}_{n}\right) \) and \( \left( {y}_{n}\right) \) in \( C \) that converge respectively to \( x \) and \( y \). For all \( n \in \mathbb{N} \), we have \( \lambda {x}_{n} + \left( {1 - \lambda }\right) {y}_{n} \in C \), and by passing to the limit as \( n \) tends to infinity, we deduce that \( {\lambda x} + \left( {1 - \lambda }\right) y \), as a limit of points in \( C \), belongs to \( \bar{C} \).

Montrons que l’intérieur \( \overset{ \circ }{C} \) de \( C \) est convexe. Soient \( x \) et \( y \in \overset{ \circ }{C} \) . Il existe \( \rho > 0 \) tel que \( \mathrm{B}\left( {x,\rho }\right) \subset C \) et \( \mathrm{B}\left( {y,\rho }\right) \subset C \) . Soit \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . Pour tout \( h \in E \) tel que \( \parallel h\parallel < \rho \) , on a \( \lbrack {\lambda x} + (1 - \; \lambda )y\rbrack + h = \lambda \left( {x + h}\right) + \left( {1 - \lambda }\right) \left( {y + h}\right) \in C \) , donc \( \mathrm{B}\left( {{\lambda x} + \left( {1 - \lambda }\right) y,\rho }\right) \subset C \) . Ceci prouve que \( {\lambda x} + \left( {1 - \lambda }\right) y \in \overset{ \circ }{C} \) , d’où le résultat.

> Let us show that the interior \( \overset{ \circ }{C} \) of \( C \) is convex. Let \( x \) and \( y \in \overset{ \circ }{C} \) . There exists \( \rho > 0 \) such that \( \mathrm{B}\left( {x,\rho }\right) \subset C \) and \( \mathrm{B}\left( {y,\rho }\right) \subset C \) . Let \( \lambda \in \left\lbrack {0,1}\right\rbrack \) . For any \( h \in E \) such that \( \parallel h\parallel < \rho \) , we have \( \lbrack {\lambda x} + (1 - \; \lambda )y\rbrack + h = \lambda \left( {x + h}\right) + \left( {1 - \lambda }\right) \left( {y + h}\right) \in C \) , therefore \( \mathrm{B}\left( {{\lambda x} + \left( {1 - \lambda }\right) y,\rho }\right) \subset C \) . This proves that \( {\lambda x} + \left( {1 - \lambda }\right) y \in \overset{ \circ }{C} \) , hence the result.

2/ a) Soit \( \Gamma \) l’ensemble des parties \( J \) de \( \{ 1,\ldots , p\} \) telles que \( x \) est barycentre des \( {\left( {x}_{i}\right) }_{i \in J} \) affectés de coefficients positifs. Notons \( q = \inf \{ \operatorname{Card}J, J \in \Gamma \} \) . Il s’agit de montrer \( q \leq n + 1 \) .

> 2/ a) Let \( \Gamma \) be the set of subsets \( J \) of \( \{ 1,\ldots , p\} \) such that \( x \) is a barycenter of the \( {\left( {x}_{i}\right) }_{i \in J} \) assigned positive coefficients. Let \( q = \inf \{ \operatorname{Card}J, J \in \Gamma \} \) . We must show \( q \leq n + 1 \) .

Supposons \( q \geq n + 2 \) . Par construction de \( q \) , il existe une partie \( J \) de \( \{ 1,\ldots , p\} \) de cardinal \( q \) telle que \( x \) soit barycentre des \( {\left( {x}_{i}\right) }_{i \in J} \) affectés de coefficients positifs :

> Suppose \( q \geq n + 2 \) . By the construction of \( q \) , there exists a subset \( J \) of \( \{ 1,\ldots , p\} \) with cardinality \( q \) such that \( x \) is a barycenter of the \( {\left( {x}_{i}\right) }_{i \in J} \) assigned positive coefficients:

\[
x = \mathop{\sum }\limits_{{i \in  J}}{\lambda }_{i}{x}_{i}\;\text{ avec }\;\mathop{\sum }\limits_{{i \in  J}}{\lambda }_{i} = 1\;\text{ et }\;\forall i \in  J,{\lambda }_{i} \geq  0.
\]

Comme \( E \) est de dimension \( n \) , les \( q \geq n + 2 \) éléments \( {\left( {x}_{i}\right) }_{i \in J} \) sont affinements liés, c’est-à-dire qu’il existe une famille \( {\left( {\mu }_{i}\right) }_{i \in J} \) d’éléments non tous nuls tels que

> Since \( E \) is of dimension \( n \) , the \( q \geq n + 2 \) elements \( {\left( {x}_{i}\right) }_{i \in J} \) are affinely dependent, meaning there exists a family \( {\left( {\mu }_{i}\right) }_{i \in J} \) of elements not all zero such that

\[
\mathop{\sum }\limits_{{i \in  J}}{\mu }_{i}{x}_{i} = 0\;\text{ et }\;\mathop{\sum }\limits_{{i \in  J}}{\mu }_{i} = 0
\]

(si \( {i}_{0} \in J \) ,écrire par exemple que les \( q - 1 \geq n + 1 \) vecteurs \( {\left( {x}_{i} - {x}_{{i}_{0}}\right) }_{i \in J \smallsetminus \left\{ {i}_{0}\right\} } \) sont liés). Soit \( \alpha = \mathop{\inf }\limits_{{{\mu }_{i} > 0}}{\lambda }_{i}/{\mu }_{i} \) , de sorte que \( {\lambda }_{i} - \alpha {\mu }_{i} \geq 0 \) pour tout \( i \in J \) (remarquons qu’il existe bien \( i \in J \) tel que \( {\mu }_{i} > 0 \) car les \( {\mu }_{i} \) sont non tous nuls et leur somme est nulle). On a

> (if \( {i}_{0} \in J \) , write for example that the \( q - 1 \geq n + 1 \) vectors \( {\left( {x}_{i} - {x}_{{i}_{0}}\right) }_{i \in J \smallsetminus \left\{ {i}_{0}\right\} } \) are linearly dependent). Let \( \alpha = \mathop{\inf }\limits_{{{\mu }_{i} > 0}}{\lambda }_{i}/{\mu }_{i} \) , such that \( {\lambda }_{i} - \alpha {\mu }_{i} \geq 0 \) for all \( i \in J \) (note that there indeed exists \( i \in J \) such that \( {\mu }_{i} > 0 \) because the \( {\mu }_{i} \) are not all zero and their sum is zero). We have

\[
x = \mathop{\sum }\limits_{{i \in  J}}\left( {{\lambda }_{i} - \alpha {\mu }_{i}}\right) {x}_{i},\;\text{ avec }\;\forall i \in  J,{\lambda }_{i} - \alpha {\mu }_{i} \geq  0\;\text{ et }\;\mathop{\sum }\limits_{{i \in  J}}\left( {{\lambda }_{i} - \alpha {\mu }_{i}}\right)  = \mathop{\sum }\limits_{{i \in  J}}{\lambda }_{i} = 1,
\]

et par définition de \( \alpha \) , il existe \( {i}_{0} \in J \) tel que \( {\lambda }_{{i}_{0}} - \alpha {\mu }_{{i}_{0}} = 0 \) . Ainsi, \( x \) est barycentre des points \( {\left( {x}_{i}\right) }_{i \in J\smallsetminus \left\{ {i}_{0}\right\} } \) affectés de coefficients positifs. Ceci est absurde par définition de \( q \) , d’où le résultat.

> and by the definition of \( \alpha \) , there exists \( {i}_{0} \in J \) such that \( {\lambda }_{{i}_{0}} - \alpha {\mu }_{{i}_{0}} = 0 \) . Thus, \( x \) is a barycenter of the points \( {\left( {x}_{i}\right) }_{i \in J\smallsetminus \left\{ {i}_{0}\right\} } \) assigned positive coefficients. This is absurd by the definition of \( q \) , hence the result.

b) Notons \( \Delta = \left\{ {\left( {{\lambda }_{1},\ldots ,{\lambda }_{n + 1}}\right) \in {\mathbb{R}}^{n + 1} \mid \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\lambda }_{i} = 1\text{ et }\forall i,{\lambda }_{i} \geq 0}\right\} \) . Cet ensemble, fermé du compact \( {\left\lbrack 0,1\right\rbrack }^{n + 1} \) est compact. On considère l’application

> b) Let \( \Delta = \left\{ {\left( {{\lambda }_{1},\ldots ,{\lambda }_{n + 1}}\right) \in {\mathbb{R}}^{n + 1} \mid \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\lambda }_{i} = 1\text{ et }\forall i,{\lambda }_{i} \geq 0}\right\} \) be denoted. This set, a closed subset of the compact set \( {\left\lbrack 0,1\right\rbrack }^{n + 1} \), is compact. We consider the map

\[
\varphi  : \Delta  \times  {A}^{n + 1} \rightarrow  E\;\left( {\left( {{\lambda }_{1},\ldots ,{\lambda }_{n + 1}}\right) ,{x}_{1},\ldots ,{x}_{n + 1}}\right)  \mapsto  \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\lambda }_{i}{x}_{i}.
\]

Comme Conv \( \left( A\right) \) est l’ensemble des barycentres des points de \( A \) affectés de coefficients positifs, on a d’après le théorème de Carathéodory \( \operatorname{Conv}\left( A\right) = \varphi \left( {\Delta \times {A}^{n + 1}}\right) \) . Or \( \Delta \times {A}^{n + 1} \) est compact (produit de compacts) et \( \varphi \) est continue, donc \( \operatorname{Conv}\left( A\right) \) est compact.

> Since Conv \( \left( A\right) \) is the set of barycenters of points in \( A \) with positive coefficients, by Carathéodory's theorem \( \operatorname{Conv}\left( A\right) = \varphi \left( {\Delta \times {A}^{n + 1}}\right) \) holds. Now, \( \Delta \times {A}^{n + 1} \) is compact (a product of compact sets) and \( \varphi \) is continuous, so \( \operatorname{Conv}\left( A\right) \) is compact.

EXERCICE 7. Soit \( E \) un \( \mathbb{R} \) -e.v.n et \( \varphi : E \rightarrow \mathbb{R} \) une forme linéaire.

> EXERCISE 7. Let \( E \) be a \( \mathbb{R} \) -n.v.s. and \( \varphi : E \rightarrow \mathbb{R} \) a linear form.

1/ Montrer que \( \varphi \) est continue si et seulement si Ker \( \varphi \) est un fermé de \( E \) .

> 1/ Show that \( \varphi \) is continuous if and only if Ker \( \varphi \) is a closed subset of \( E \) .

2 / a) Soit \( F \) un s.e.v de \( E \) . Montrer que l’application

> 2 / a) Let \( F \) be a subspace of \( E \) . Show that the map

\[
N : E/F \rightarrow  \mathbb{R}\;\dot{x} \mapsto  \mathop{\inf }\limits_{{y \in  \dot{x}}}\parallel y\parallel
\]

est une semi-norme sur l’espace quotient \( E/F \) . Que dire si \( F \) est fermé ? b) En utilisant la question précédente, retrouver le résultat de la question 1/.

> is a seminorm on the quotient space \( E/F \) . What can be said if \( F \) is closed? b) Using the previous question, recover the result of question 1/.

Solution. 1/ Si \( \varphi \) est continue, \( \operatorname{Ker}\varphi \) est l’image réciproque par \( \varphi \) du fermé \{0\} donc fermé.

> Solution. 1/ If \( \varphi \) is continuous, \( \operatorname{Ker}\varphi \) is the preimage of the closed set \{0\} under \( \varphi \) and is therefore closed.

Réciproquement, supposons Ker \( \varphi \) fermé. Si \( \varphi \) n’est pas continue, \( \varphi \) n’est pas bornée sur la sphère unité. Il existe donc une suite \( \left( {x}_{n}\right) \) de \( E \) telle que

> Conversely, suppose Ker \( \varphi \) is closed. If \( \varphi \) is not continuous, \( \varphi \) is not bounded on the unit sphere. There exists a sequence \( \left( {x}_{n}\right) \) in \( E \) such that

\[
\text{ (i) }\;\forall n \in  \mathbb{N},\begin{Vmatrix}{x}_{n}\end{Vmatrix} = 1
\]

\[
\text{ (ii) }\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left| {\varphi \left( {x}_{n}\right) }\right|  =  + \infty \text{ . }
\]

Fixons \( u \in E \) tel que \( \varphi \left( u\right) = 1 \) . Pour tout \( n \) , posons \( {u}_{n} = u - \frac{{x}_{n}}{\varphi \left( {x}_{n}\right) } \) . On a \( \varphi \left( {u}_{n}\right) = \varphi \left( u\right) - \; \frac{1}{\varphi \left( {x}_{n}\right) }\varphi \left( {x}_{n}\right) = 0 \) , donc \( {u}_{n} \in \operatorname{Ker}\varphi \) . D’après (i) et (ii), \( \left( {u}_{n}\right) \) converge vers \( u \) , et Ker \( \varphi \) étant fermé, \( u \in \operatorname{Ker}\varphi \) . Ceci est absurde car \( \varphi \left( u\right) = 1 \) . Ainsi, \( \varphi \) est continue.

> Let us fix \( u \in E \) such that \( \varphi \left( u\right) = 1 \) . For all \( n \) , let \( {u}_{n} = u - \frac{{x}_{n}}{\varphi \left( {x}_{n}\right) } \) . We have \( \varphi \left( {u}_{n}\right) = \varphi \left( u\right) - \; \frac{1}{\varphi \left( {x}_{n}\right) }\varphi \left( {x}_{n}\right) = 0 \) , so \( {u}_{n} \in \operatorname{Ker}\varphi \) . According to (i) and (ii), \( \left( {u}_{n}\right) \) converges to \( u \) , and since Ker \( \varphi \) is closed, \( u \in \operatorname{Ker}\varphi \) . This is absurd because \( \varphi \left( u\right) = 1 \) . Thus, \( \varphi \) is continuous.

2 / a) Soit \( x \in E \) et \( \lambda \in \mathbb{R} \) . Rappelons que la classe \( \dot{x} \) de \( x \) est \( \dot{x} = x + F \) . De l’égalité \( \overbrace{\lambda x} = \lambda \dot{x} \) , on tire \( N\left( {\lambda \dot{x}}\right) = \left| \lambda \right| N\left( \dot{x}\right) \) .

> 2 / a) Let \( x \in E \) and \( \lambda \in \mathbb{R} \) . Recall that the class \( \dot{x} \) of \( x \) is \( \dot{x} = x + F \) . From the equality \( \overbrace{\lambda x} = \lambda \dot{x} \) , we derive \( N\left( {\lambda \dot{x}}\right) = \left| \lambda \right| N\left( \dot{x}\right) \) .

Il nous reste à montrer que \( N \) vérifie l’inégalité triangulaire. Soient \( x, y \in E \) . On a

> It remains to show that \( N \) satisfies the triangle inequality. Let \( x, y \in E \) . We have

\[
\forall u, v \in  F,\;N\left( \overset{\text{ ⏜ }}{x + y}\right)  \leq  \parallel \left( {x + y}\right)  + \left( {u + v}\right) \parallel  \leq  \parallel x + u\parallel  + \parallel y + v\parallel ,
\]

ce qui en passant aux inf à droite donne \( N\left( \widehat{x + y}\right) \leq N\left( \dot{x}\right) + N\left( \dot{y}\right) \) .

> which, by taking the infimum on the right, gives \( N\left( \widehat{x + y}\right) \leq N\left( \dot{x}\right) + N\left( \dot{y}\right) \) .

Ainsi, \( N \) est une semi-norme. Comme \( \dot{x} = x + F \) pour tout \( x, N\left( \dot{x}\right) = \mathop{\inf }\limits_{{y \in F}}\parallel x - y\parallel \) est la distance de \( x \) à \( F \) . Si \( F \) est fermé, on a donc \( N\left( \dot{x}\right) = 0 \) si et seulement si \( x \in F \) , c’est-à-dire \( \dot{x} = 0 \) . Finalement, si \( F \) est fermé, \( N \) est une norme sur \( E \smallsetminus F \) .

> Thus, \( N \) is a seminorm. Since \( \dot{x} = x + F \) for all \( x, N\left( \dot{x}\right) = \mathop{\inf }\limits_{{y \in F}}\parallel x - y\parallel \) is the distance from \( x \) to \( F \) . If \( F \) is closed, we have \( N\left( \dot{x}\right) = 0 \) if and only if \( x \in F \) , that is to say \( \dot{x} = 0 \) . Finally, if \( F \) is closed, \( N \) is a norm on \( E \smallsetminus F \) .

b) Soit \( \varphi : E \rightarrow \mathbb{R} \) une forme linéaire telle que Ker \( \varphi \) est fermé. Si \( \varphi \) est nulle, il est clair que \( \varphi \) est continue. Sinon \( \varphi \left( E\right) = \mathbb{R} \) . Considérons la factorisation canonique de \( \varphi \) suivante

> b) Let \( \varphi : E \rightarrow \mathbb{R} \) be a linear form such that Ker \( \varphi \) is closed. If \( \varphi \) is zero, it is clear that \( \varphi \) is continuous. Otherwise \( \varphi \left( E\right) = \mathbb{R} \) . Consider the following canonical factorization of \( \varphi \)

![bo_d7fjkrs91nqc73ereoog_60_651_230_269_149_0.jpg](images/gourdon_analysis_fr_en_026_bod7fjkrs91nqc73ereoog606512302691490.jpg)

On a \( \varphi = \psi \circ s \) où \( s \) est la surjection canonique de \( E \) sur \( E/\operatorname{Ker}\varphi \) et \( \psi : E/\operatorname{Ker}\varphi \rightarrow \mathbb{R} \) est linéaire.

> We have \( \varphi = \psi \circ s \) where \( s \) is the canonical surjection from \( E \) onto \( E/\operatorname{Ker}\varphi \) and \( \psi : E/\operatorname{Ker}\varphi \rightarrow \mathbb{R} \) is linear.

- L'application \( \psi \) est continue (c'est une application linéaire sur des espaces de dimension finie).

> - The map \( \psi \) is continuous (it is a linear map on finite-dimensional spaces).

- La surjection \( s \) de \( \left( {E,\parallel .\parallel }\right) \) dans \( \left( {E/\operatorname{Ker}\varphi , N}\right) \) est continue (où \( N \) est la norme définie plus haut avec \( F = \operatorname{Ker}\varphi \) , fermé), car \( N\left( {\dot{x} - \dot{y}}\right)  = N\left( \overbrace{x - y}\right)  \leq  \parallel x - y\parallel \) .

> - The surjection \( s \) from \( \left( {E,\parallel .\parallel }\right) \) to \( \left( {E/\operatorname{Ker}\varphi , N}\right) \) is continuous (where \( N \) is the norm defined above with \( F = \operatorname{Ker}\varphi \) closed), because \( N\left( {\dot{x} - \dot{y}}\right)  = N\left( \overbrace{x - y}\right)  \leq  \parallel x - y\parallel \) .

On en déduit que \( \varphi = \psi \circ s \) est continue.

> We deduce that \( \varphi = \psi \circ s \) is continuous.

Remarque. La méthode utilisée au 2/ b) se généralise aisément pour montrer qu'une application linéaire de rang fini est continue si et seulement si son noyau est fermé.

> Remark. The method used in 2/ b) generalizes easily to show that a linear map of finite rank is continuous if and only if its kernel is closed.

EXERCICE 8. Démontrer qu’un espace vectoriel normé \( E \) qui admet une base dénombrable n'est jamais complet.

> EXERCISE 8. Prove that a normed vector space \( E \) that admits a countable basis is never complete.

Solution. Soit \( {\left( {e}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une base de \( E \) . Quitte à normaliser les \( {e}_{n} \) , on peut supposer \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} = 1 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Nous allons construire une série \( \sum {\lambda }_{n}{e}_{n} \) absolument convergente à partir d’une suite \( \left( {\lambda }_{n}\right) \) particulière, et nous allons prouver que \( \sum {\lambda }_{n}{e}_{n} \) ne converge pas (intuitivement, si une telle série convergeait, sa somme serait combinaison linéaire infinie de \( \left( {e}_{n}\right) \) , ce qui est impossible dans un espace vectoriel par définition d'une base).

> Solution. Let \( {\left( {e}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a basis of \( E \) . By normalizing the \( {e}_{n} \) , we can assume \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} = 1 \) for all \( n \in {\mathbb{N}}^{ * } \) . We will construct an absolutely convergent series \( \sum {\lambda }_{n}{e}_{n} \) from a particular sequence \( \left( {\lambda }_{n}\right) \) , and we will prove that \( \sum {\lambda }_{n}{e}_{n} \) does not converge (intuitively, if such a series converged, its sum would be an infinite linear combination of \( \left( {e}_{n}\right) \) , which is impossible in a vector space by the definition of a basis).

Notons \( {F}_{0} = \{ 0\} \) et \( {F}_{n} = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) pour tout \( n \in {\mathbb{N}}^{ * } \) . A partir de \( {\lambda }_{1} = 1/3 \) , on définit \( \left( {\lambda }_{n}\right) \) par

> Let \( {F}_{0} = \{ 0\} \) and \( {F}_{n} = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{n}}\right) \) for all \( n \in {\mathbb{N}}^{ * } \) . From \( {\lambda }_{1} = 1/3 \) , we define \( \left( {\lambda }_{n}\right) \) by

\[
{\lambda }_{n + 1} = \frac{1}{3}\mathrm{\;d}\left( {{\lambda }_{n}{e}_{n},{F}_{n - 1}}\right)  = \frac{1}{3}\mathop{\inf }\limits_{{x \in  {F}_{n - 1}}}\begin{Vmatrix}{{\lambda }_{n}{e}_{n} - x}\end{Vmatrix}.
\]

Comme \( {F}_{n} \) est fermé (s.e.v de dimension finie), on sait que \( \mathrm{d}\left( {x,{F}_{n}}\right) = 0 \) si et seulement si \( x \in {F}_{n} \) . Par récurrence, on en déduit \( {\lambda }_{n} > 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Enfin, l’inégalité

> Since \( {F}_{n} \) is closed (finite-dimensional subspace), we know that \( \mathrm{d}\left( {x,{F}_{n}}\right) = 0 \) if and only if \( x \in {F}_{n} \) . By induction, we deduce \( {\lambda }_{n} > 0 \) for all \( n \in {\mathbb{N}}^{ * } \) . Finally, the inequality

\[
{\lambda }_{n + 1} = \frac{1}{3}\mathrm{\;d}\left( {{\lambda }_{n}{e}_{n},{F}_{n - 1}}\right)  \leq  \frac{1}{3}\begin{Vmatrix}{{\lambda }_{n}{e}_{n}}\end{Vmatrix} = \frac{{\lambda }_{n}}{3},
\]

assure la majoration \( {\lambda }_{n} \leq 1/{3}^{n} \) pour tout \( n \) .

> ensures the bound \( {\lambda }_{n} \leq 1/{3}^{n} \) for all \( n \) .

La série \( \sum {\lambda }_{n}{e}_{n} \) converge donc absolument. Si \( E \) est supposé complet, elle converge donc. Notons \( x \) sa limite. Comme \( {\left( {e}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) est une base de \( E \) , il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( x \in {F}_{n} \) . Ainsi, \( y = \mathop{\sum }\limits_{{k = n + 1}}^{\infty }{\lambda }_{k}{e}_{k} = x - \mathop{\sum }\limits_{{k = 1}}^{n}{\lambda }_{k}{e}_{k} \in {F}_{n} \) , donc

> The series \( \sum {\lambda }_{n}{e}_{n} \) therefore converges absolutely. If \( E \) is assumed to be complete, it therefore converges. Let \( x \) denote its limit. Since \( {\left( {e}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) is a basis for \( E \), there exists \( n \in {\mathbb{N}}^{ * } \) such that \( x \in {F}_{n} \). Thus, \( y = \mathop{\sum }\limits_{{k = n + 1}}^{\infty }{\lambda }_{k}{e}_{k} = x - \mathop{\sum }\limits_{{k = 1}}^{n}{\lambda }_{k}{e}_{k} \in {F}_{n} \), therefore

\[
3{\lambda }_{n + 2} = \mathrm{d}\left( {{\lambda }_{n + 1}{e}_{n + 1},{F}_{n}}\right)  \leq  \begin{Vmatrix}{{\lambda }_{n + 1}{e}_{n + 1} - y}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = n + 2}}^{\infty }{\lambda }_{k} \leq  {\lambda }_{n + 2}\mathop{\sum }\limits_{{k = 0}}^{\infty }\frac{1}{{3}^{k}} = \frac{3}{2}{\lambda }_{n + 2},
\]

ce qui est absurde car \( {\lambda }_{n + 2} \neq 0 \) . L’espace métrique \( E \) n’est donc pas complet.

> which is absurd because \( {\lambda }_{n + 2} \neq 0 \). The metric space \( E \) is therefore not complete.

Remarque. Ce résultat est aussi une conséquence immédiate du théorème de Baire (voir l'annexe A, exercice 1).

> Remark. This result is also an immediate consequence of the Baire category theorem (see Appendix A, exercise 1).

EXERCICE 9 (THÉORÉME DE RIESZ). Soit \( E \) un \( \mathbb{R} \) -e.v.n de dimension infinie. Montrer que la boule unité fermée de \( E \) ne peut pas être incluse dans une réunion finie de boules ouvertes de rayon 1. Qu'en conclure ?

> EXERCISE 9 (RIESZ'S THEOREM). Let \( E \) be an infinite-dimensional \( \mathbb{R} \)-n.v.s. Show that the closed unit ball of \( E \) cannot be contained in a finite union of open balls of radius 1. What can be concluded from this?

Solution. Raisonnons par l’absurde en supposant l’existence de \( n \in {\mathbb{N}}^{ * } \) et de \( {x}_{1},\ldots ,{x}_{n} \in E \) tels que \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},1}\right) \) . Notons \( F = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) . Comme \( E \) est de dimension infinie,

> Solution. Let us reason by contradiction by assuming the existence of \( n \in {\mathbb{N}}^{ * } \) and \( {x}_{1},\ldots ,{x}_{n} \in E \) such that \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},1}\right) \). Let \( F = \operatorname{Vect}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \). Since \( E \) is infinite-dimensional,

il existe \( x \in E \) tel que \( x \notin F \) . Comme \( F \) est un s.e.v de dimension finie, il existe \( y \in F \) tel que \( \parallel x - y\parallel = \mathrm{d}\left( {x, F}\right) \) (voir l’exercice 3 page 33). Soit \( {x}_{0} = \frac{x - y}{\parallel x - y\parallel } \) . On a \( \mathrm{d}\left( {{x}_{0}, F}\right) \leq \begin{Vmatrix}{x}_{0}\end{Vmatrix} = 1 \) et

> there exists \( x \in E \) such that \( x \notin F \). Since \( F \) is a finite-dimensional subspace, there exists \( y \in F \) such that \( \parallel x - y\parallel = \mathrm{d}\left( {x, F}\right) \) (see exercise 3 on page 33). Let \( {x}_{0} = \frac{x - y}{\parallel x - y\parallel } \). We have \( \mathrm{d}\left( {{x}_{0}, F}\right) \leq \begin{Vmatrix}{x}_{0}\end{Vmatrix} = 1 \) and

\[
\forall z \in  F,\;\begin{Vmatrix}{{x}_{0} - z}\end{Vmatrix} = \frac{1}{\parallel x - y\parallel }\parallel x - \left( {y + \parallel x - y\parallel z}\right) \parallel  \geq  \frac{\mathrm{d}\left( {x, F}\right) }{\parallel x - y\parallel } = 1,
\]

donc \( \mathrm{d}\left( {{x}_{0}, F}\right) = 1 \) .

> therefore \( \mathrm{d}\left( {{x}_{0}, F}\right) = 1 \).

Or \( {x}_{0} \in {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) , donc il existe \( i \) tel que \( {x}_{0} \in \mathrm{B}\left( {{x}_{i},1}\right) \) , de sorte que \( \mathrm{d}\left( {{x}_{0},{x}_{i}}\right) < 1 \) , ce qui est absurde car \( 1 = \mathrm{d}\left( {{x}_{0}, F}\right) \leq \mathrm{d}\left( {{x}_{0},{x}_{i}}\right) \) .

> However, \( {x}_{0} \in {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \), so there exists \( i \) such that \( {x}_{0} \in \mathrm{B}\left( {{x}_{i},1}\right) \), such that \( \mathrm{d}\left( {{x}_{0},{x}_{i}}\right) < 1 \), which is absurd because \( 1 = \mathrm{d}\left( {{x}_{0}, F}\right) \leq \mathrm{d}\left( {{x}_{0},{x}_{i}}\right) \).

Finalement, nous avons démontré que \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) n’est pas précompact, en particulier non compact.

> Finally, we have shown that \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) is not precompact, and in particular not compact.
