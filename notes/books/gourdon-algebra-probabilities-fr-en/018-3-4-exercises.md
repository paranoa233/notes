#### 3.4. Exercises

*Français : 3.4. Exercices*

EXERCICE 1. Soit \( A \) un anneau unitaire dont l’élément neutre pour la loi ⋅ est noté 1. a) Soit \( x \in A \) nilpotent. Montrer que \( 1 - x \) est inversible.

> EXERCISE 1. Let \( A \) be a unital ring whose identity element for the operation ⋅ is denoted by 1. a) Let \( x \in A \) be nilpotent. Show that \( 1 - x \) is invertible.

b) Si \( n \in {\mathbb{N}}^{ * } \) (et \( x \) toujours nilpotent), simplifier l’expression

> b) If \( n \in {\mathbb{N}}^{ * } \) (and \( x \) is still nilpotent), simplify the expression

\[
{U}_{n} = \left( {1 + x}\right) \left( {1 + {x}^{2}}\right) \cdots \left( {1 + {x}^{{2}^{n}}}\right)  = \mathop{\prod }\limits_{{k = 0}}^{n}\left( {1 + {x}^{{2}^{k}}}\right) .
\]

Solution. a) Soit \( p \) l’indice de nilpotence de \( x \) , de sorte que \( {x}^{p} = 0 \) . On a

> Solution. a) Let \( p \) be the index of nilpotence of \( x \) , such that \( {x}^{p} = 0 \) . We have

\[
\left( {1 - x}\right) \left( {1 + x + \cdots  + {x}^{p - 1}}\right)  = \left( {1 + x + \cdots  + {x}^{p - 1}}\right) \left( {1 - x}\right)  = 1 - {x}^{p} = 1,
\]

d’où le résultat car on a prouvê que \( {xy} = {yx} = 1 \) avec \( y = 1 + x + \cdots + {x}^{p - 1} \) .

> hence the result, as we have proven that \( {xy} = {yx} = 1 \) with \( y = 1 + x + \cdots + {x}^{p - 1} \) .

b) On va montrer par récurrence sur \( n \in \mathbb{N} \) que \( {U}_{n} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n + 1}}}\right) \) .

> b) We will show by induction on \( n \in \mathbb{N} \) that \( {U}_{n} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n + 1}}}\right) \) .

- Pour \( n = 0 \) c’est vrai car \( \left( {1 - x}\right) {U}_{0} = \left( {1 - x}\right) \left( {1 + x}\right)  = 1 - {x}^{2} \) , d’où \( {U}_{0} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{2}}\right) \) .

> - For \( n = 0 \) it is true because \( \left( {1 - x}\right) {U}_{0} = \left( {1 - x}\right) \left( {1 + x}\right)  = 1 - {x}^{2} \) , hence \( {U}_{0} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{2}}\right) \) .

- Supposons \( {U}_{n - 1} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n}}}\right) \) . Alors \( {U}_{n} = {U}_{n - 1}\left( {1 + {x}^{{2}^{n}}}\right)  = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n + 1}}}\right) \) .

> - Suppose \( {U}_{n - 1} = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n}}}\right) \) . Then \( {U}_{n} = {U}_{n - 1}\left( {1 + {x}^{{2}^{n}}}\right)  = {\left( 1 - x\right) }^{-1}\left( {1 - {x}^{{2}^{n + 1}}}\right) \) .

Remarque. Le résultat a) appliqué aux matrices carrées entraîne que si \( N \) est une matrice nilpotente, alors \( I - N \) est inversible (ceci reste vrai dès que \( \parallel N\parallel < 1 - \) où \( \parallel \cdot \parallel \) est une norme d'algèbre sur les matrices, voir le tome analyse sur les espaces vectoriels normés).

> Remark. Result a) applied to square matrices implies that if \( N \) is a nilpotent matrix, then \( I - N \) is invertible (this remains true as soon as \( \parallel N\parallel < 1 - \) where \( \parallel \cdot \parallel \) is an algebra norm on matrices, see the analysis volume on normed vector spaces).

EXERCICE 2 (ANNEAU DE BOOLE). Soit \( A \) un anneau tel que tout élément de \( A \) soit idempotent (i. e. \( \forall x \in A,{x}^{2} = x \) ).

> EXERCISE 2 (BOOLEAN RING). Let \( A \) be a ring such that every element of \( A \) is idempotent (i.e., \( \forall x \in A,{x}^{2} = x \) ).

a) Si \( x \in A \) , montrer que \( {2x} = 0 \) . Montrer que \( A \) est commutatif.

> a) If \( x \in A \) , show that \( {2x} = 0 \) . Show that \( A \) is commutative.

b) Montrer que si \( x, y \in A \) alors \( {xy}\left( {x + y}\right) = 0 \) . Que dire si \( A \) est intègre ?

> b) Show that if \( x, y \in A \) then \( {xy}\left( {x + y}\right) = 0 \) . What can be said if \( A \) is an integral domain?

Solution. a) Si \( x \in A \) , alors \( {\left( 2x\right) }^{2} = {2x} \) donc \( 4{x}^{2} = {2x} \) , ce qui entraîne \( {4x} = {2x} \) puis \( {2x} = 0 \) . Ceci s’écrit encore \( x = - x \) .

> Solution. a) If \( x \in A \) , then \( {\left( 2x\right) }^{2} = {2x} \) so \( 4{x}^{2} = {2x} \) , which implies \( {4x} = {2x} \) then \( {2x} = 0 \) . This can also be written as \( x = - x \) .

Si \( x, y \in A,{\left( x + y\right) }^{2} = x + y \) donc \( {x}^{2} + {xy} + {yx} + {y}^{2} = x + y = {x}^{2} + {y}^{2} \) , d’où on tire \( {xy} + {yx} = 0 \) , donc \( {xy} = - {yx} = {yx} \) .

> If \( x, y \in A,{\left( x + y\right) }^{2} = x + y \) then \( {x}^{2} + {xy} + {yx} + {y}^{2} = x + y = {x}^{2} + {y}^{2} \) , from which we derive \( {xy} + {yx} = 0 \) , so \( {xy} = - {yx} = {yx} \) .

b) Si \( x, y \in A \) , alors \( {xy}\left( {x + y}\right) = {xyx} + x{y}^{2} = {x}^{2}y + x{y}^{2} = {2xy} = 0 \) .

> b) If \( x, y \in A \) , then \( {xy}\left( {x + y}\right) = {xyx} + x{y}^{2} = {x}^{2}y + x{y}^{2} = {2xy} = 0 \) .

- Si \( A \) est intègre, alors \( A \) a au plus deux éléments. En effet, sinon il existe \( x, y \in  A \) distincts et différents de 0 . Donc \( \left( {x + y}\right)  \neq  0 \) (sinon \( x =  - y = y \) ) et A étant intègre \( {xy}\left( {x + y}\right)  \neq  0 \) , absurde.

> - If \( A \) is an integral domain, then \( A \) has at most two elements. Indeed, otherwise there exist \( x, y \in  A \) distinct and different from 0. Thus \( \left( {x + y}\right)  \neq  0 \) (otherwise \( x =  - y = y \) ) and since A is an integral domain \( {xy}\left( {x + y}\right)  \neq  0 \) , which is absurd.

EXERCICE 3 (RADICAL D'UN IDÉAL). Soit \( A \) un anneau commutatif unitaire et \( I \) un idéal de \( A \) . On appelle radical de \( I \) l’ensemble noté \( \sqrt{I} = \left\{ {x \in A\mid \exists n \in {\mathbb{N}}^{ * },{x}^{n} \in I}\right\} \) . a) Montrer que \( \sqrt{I} \) est un idéal de \( A \) .

> EXERCISE 3 (RADICAL OF AN IDEAL). Let \( A \) be a commutative unital ring and \( I \) an ideal of \( A \) . The radical of \( I \) is the set denoted by \( \sqrt{I} = \left\{ {x \in A\mid \exists n \in {\mathbb{N}}^{ * },{x}^{n} \in I}\right\} \) . a) Show that \( \sqrt{I} \) is an ideal of \( A \) .

b) Déterminer le radical d'un idéal de \( \mathbb{Z} \) .

> b) Determine the radical of an ideal of \( \mathbb{Z} \) .

Solution. a) - Montrons tout d’abord que \( \left( {\sqrt{I}, + }\right) \) est un sous-groupe de \( \left( {A, + }\right) \) . Il est clair que \( 0 \in \sqrt{I} \) puisque \( I \subset \sqrt{I} \) . Par ailleurs, si \( x \in \sqrt{I} \) alors \( - x \in \sqrt{I} \) puisque le fait que \( {x}^{n} \in I \) entraîne \( {\left( -1\right) }^{n}{x}^{n} = {\left( -x\right) }^{n} \in I \) . Prenons maintenant \( x, y \in \sqrt{I} \) . Il existe \( m \) et \( n \in {\mathbb{N}}^{ * } \) tels que \( {x}^{m} \in I \) et \( {y}^{n} \in I \) . L’anneau \( A \) étant commutatif, la formule du binôme entraîne

> Solution. a) - Let us first show that \( \left( {\sqrt{I}, + }\right) \) is a subgroup of \( \left( {A, + }\right) \) . It is clear that \( 0 \in \sqrt{I} \) since \( I \subset \sqrt{I} \) . Furthermore, if \( x \in \sqrt{I} \) then \( - x \in \sqrt{I} \) since the fact that \( {x}^{n} \in I \) implies \( {\left( -1\right) }^{n}{x}^{n} = {\left( -x\right) }^{n} \in I \) . Now let \( x, y \in \sqrt{I} \) . There exist \( m \) and \( n \in {\mathbb{N}}^{ * } \) such that \( {x}^{m} \in I \) and \( {y}^{n} \in I \) . Since the ring \( A \) is commutative, the binomial formula implies

\[
{\left( x + y\right) }^{m + n - 1} = {y}^{n} \cdot  \mathop{\sum }\limits_{{k = 0}}^{{m - 1}}\left( \begin{matrix} m + n - 1 \\  k \end{matrix}\right) {x}^{k}{y}^{m - 1 - k} + {x}^{m} \cdot  \mathop{\sum }\limits_{{k = m}}^{{m + n - 1}}\left( \begin{matrix} m + n - 1 \\  k \end{matrix}\right) {x}^{k - m}{y}^{m + n - 1 - k}
\]

et puisque \( I \) est un idéal, ce terme appartient à \( I \) . Donc \( x + y \in \sqrt{I} \) .

> and since \( I \) is an ideal, this term belongs to \( I \) . Thus \( x + y \in \sqrt{I} \) .

- Enfin, si \( a \in  A \) et si \( x \in  \sqrt{I} \) , il existe \( n \in  {\mathbb{N}}^{ * } \) tel que \( {x}^{n} \in  I \) et donc \( A \) étant commutatif, \( {\left( ax\right) }^{n} = {a}^{n}{x}^{n} \in  I \) . Donc \( {ax} \in  \sqrt{I} \) . Finalement, \( \sqrt{I} \) est un idéal de \( A \) .

> - Finally, if \( a \in  A \) and if \( x \in  \sqrt{I} \) , there exists \( n \in  {\mathbb{N}}^{ * } \) such that \( {x}^{n} \in  I \) and therefore, since \( A \) is commutative, \( {\left( ax\right) }^{n} = {a}^{n}{x}^{n} \in  I \) . Thus \( {ax} \in  \sqrt{I} \) . Finally, \( \sqrt{I} \) is an ideal of \( A \) .

b) Soit \( I \) un idéal de \( \mathbb{Z} \) . L’anneau des entiers étant principal, il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( I = n\mathbb{Z} \) . Si \( n = 0 \) , on a bien sûr \( \sqrt{I} = 0 \) et si \( n = 1,\sqrt{I} = \mathbb{Z} \) . Sinon \( n \geq 2 \) , et on écrit la décomposition de \( n \) en produit de facteurs premiers \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) . Montrons que \( \sqrt{I} = {p}_{1}\cdots {p}_{k}\mathbb{Z} \) .

> b) Let \( I \) be an ideal of \( \mathbb{Z} \) . Since the ring of integers is a principal ideal domain, there exists \( n \in {\mathbb{N}}^{ * } \) such that \( I = n\mathbb{Z} \) . If \( n = 0 \) , we obviously have \( \sqrt{I} = 0 \) and if \( n = 1,\sqrt{I} = \mathbb{Z} \) . Otherwise \( n \geq 2 \) , and we write the prime factorization of \( n \) as \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \) . Let us show that \( \sqrt{I} = {p}_{1}\cdots {p}_{k}\mathbb{Z} \) .

- On a \( \sqrt{I} \subset  {p}_{1}\cdots {p}_{k}\mathbb{Z} \) . En effet. Si \( x \in  \sqrt{I} \) alors il existe \( m \in  {\mathbb{N}}^{ * } \) tel que \( {x}^{m} \in  n\mathbb{Z} \) , donc \( n \mid  {x}^{m} \) , donc \( \forall i,1 \leq  i \leq  k,{p}_{i} \mid  {x}^{m} \) , donc \( \forall i,1 \leq  i \leq  k,{p}_{i} \mid  x \) d’où \( {p}_{1}\cdots {p}_{k} \mid  x \) puisque les \( {p}_{i} \) sont premiers entre eux deux à deux (ils sont premiers et distincts).

> - We have \( \sqrt{I} \subset  {p}_{1}\cdots {p}_{k}\mathbb{Z} \) . Indeed. If \( x \in  \sqrt{I} \) then there exists \( m \in  {\mathbb{N}}^{ * } \) such that \( {x}^{m} \in  n\mathbb{Z} \) , therefore \( n \mid  {x}^{m} \) , therefore \( \forall i,1 \leq  i \leq  k,{p}_{i} \mid  {x}^{m} \) , therefore \( \forall i,1 \leq  i \leq  k,{p}_{i} \mid  x \) , from which \( {p}_{1}\cdots {p}_{k} \mid  x \) follows since the \( {p}_{i} \) are pairwise coprime (they are prime and distinct).

- On a \( {p}_{1}\cdots {p}_{k}\mathbb{Z} \subset  \sqrt{I} \) . En effet. Soit \( x \in  {p}_{1}\cdots {p}_{k}\mathbb{Z} \) . Il existe \( r \in  \mathbb{Z} \) tel que \( x = {p}_{1}\cdots {p}_{k}r \) . Si \( m = \mathop{\max }\limits_{{1 \leq  i \leq  k}}{\alpha }_{i} \) , on a \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \mid  {x}^{m} = {p}_{1}^{m}\cdots {p}_{k}^{m}{r}^{m} \) donc \( {x}^{m} \in  I \) , ou encore \( x \in  \sqrt{I} \) .

> - We have \( {p}_{1}\cdots {p}_{k}\mathbb{Z} \subset  \sqrt{I} \) . Indeed. Let \( x \in  {p}_{1}\cdots {p}_{k}\mathbb{Z} \) . There exists \( r \in  \mathbb{Z} \) such that \( x = {p}_{1}\cdots {p}_{k}r \) . If \( m = \mathop{\max }\limits_{{1 \leq  i \leq  k}}{\alpha }_{i} \) , we have \( n = {p}_{1}^{{\alpha }_{1}}\cdots {p}_{k}^{{\alpha }_{k}} \mid  {x}^{m} = {p}_{1}^{m}\cdots {p}_{k}^{m}{r}^{m} \) thus \( {x}^{m} \in  I \) , or also \( x \in  \sqrt{I} \) .

EXERCICE 4 (IDÉAL PREMIER, IDÉAL MAXIMAL). Soit \( A \) un anneau commutatif unitaire. a) Un idéal \( \mathcal{P} \neq A \) de \( A \) est dit premier si pour \( x, y \in A \) le fait que \( {xy} \in \mathcal{P} \) entraîne \( x \in \mathcal{P} \) ou \( y \in \mathcal{P} \) . Montrer que \( \mathcal{P} \) est un idéal premier si et seulement si l’anneau quotient \( A/\mathcal{P} \) est intègre.

> EXERCISE 4 (PRIME IDEAL, MAXIMAL IDEAL). Let \( A \) be a commutative unital ring. a) An ideal \( \mathcal{P} \neq A \) of \( A \) is called prime if for \( x, y \in A \) the fact that \( {xy} \in \mathcal{P} \) implies \( x \in \mathcal{P} \) or \( y \in \mathcal{P} \) . Show that \( \mathcal{P} \) is a prime ideal if and only if the quotient ring \( A/\mathcal{P} \) is an integral domain.

b) Un idéal \( \mathcal{M} \neq A \) de \( A \) est dit maximal si les seuls idéaux contenant \( \mathcal{M} \) sont \( \mathcal{M} \) et \( A \) . Montrer que \( \mathcal{M} \) est un idéal maximal si et seulement si \( A/\mathcal{M} \) est un corps.

> b) An ideal \( \mathcal{M} \neq A \) of \( A \) is called maximal if the only ideals containing \( \mathcal{M} \) are \( \mathcal{M} \) and \( A \) . Show that \( \mathcal{M} \) is a maximal ideal if and only if \( A/\mathcal{M} \) is a field.

c) Montrer que tout idéal maximal est premier.

> c) Show that every maximal ideal is prime.

d) Si l’anneau \( A \) est principal, montrer qu’un idéal premier \( \mathcal{P} \neq \{ 0\} \) est maximal.

> d) If the ring \( A \) is a principal ideal ring, show that a prime ideal \( \mathcal{P} \neq \{ 0\} \) is maximal.

Solution. a) Si \( x \in A \) , notons \( \dot{x} \) sa classe dans \( A/\mathcal{P} \) . Alors

> Solution. a) If \( x \in A \) , let \( \dot{x} \) denote its class in \( A/\mathcal{P} \) . Then

\[
\left( {\mathcal{P}\text{ est premier }}\right)  \Leftrightarrow  \left( {{xy} \in  \mathcal{P} \Rightarrow  x\text{ ou }y \in  \mathcal{P}}\right)
\]

\[
\Leftrightarrow  (\dot{x} \cdot  \dot{y} = \dot{0} \Rightarrow  \dot{x} = \dot{0}\text{ ou }\dot{y} = \dot{0}) \Leftrightarrow  \left( {A/\mathcal{P}\text{ est intègre }}\right) \text{ . }
\]

b) Condition nécessaire. Soit \( \mathcal{M} \) un idéal maximal. Soit \( x \in A \) tel que \( \dot{x} \) (classe de \( x \) dans \( A/\mathcal{M} \) ) vérifie \( \dot{x} \neq 0 \) . Alors \( x \notin \mathcal{M} \) de sorte que \( \mathcal{M} + \left( x\right) = A \) (en effet, \( I = \mathcal{M} + \left( x\right) \) est un idéal contenant \( \mathcal{M} \) , différent de \( \mathcal{M} \) puisque \( x \notin \mathcal{M} \) , donc \( I = A \) ). Donc il existe \( a \in A \) et \( m \in \mathcal{M} \) tels que \( 1 = m + {ax} \) , ce qui s’écrit \( 1 = \dot{a}\dot{x} \) . L’anneau \( A/\mathcal{M} \) est donc un corps.

> b) Necessary condition. Let \( \mathcal{M} \) be a maximal ideal. Let \( x \in A \) such that \( \dot{x} \) (class of \( x \) in \( A/\mathcal{M} \) ) satisfies \( \dot{x} \neq 0 \) . Then \( x \notin \mathcal{M} \) such that \( \mathcal{M} + \left( x\right) = A \) (indeed, \( I = \mathcal{M} + \left( x\right) \) is an ideal containing \( \mathcal{M} \) , different from \( \mathcal{M} \) since \( x \notin \mathcal{M} \) , thus \( I = A \) ). So there exist \( a \in A \) and \( m \in \mathcal{M} \) such that \( 1 = m + {ax} \) , which is written \( 1 = \dot{a}\dot{x} \) . The ring \( A/\mathcal{M} \) is therefore a field.

Condition suffisante. Soit \( I \) un idéal de \( A \) tel que \( \mathcal{M} \subset I \) et \( \mathcal{M} \neq I \) . Soit \( a \in I, a \notin \mathcal{M} \) . On a \( \dot{a} \neq \dot{0} \) de sorte que \( A/\mathcal{M} \) étant un corps, il existe \( b \in A,\dot{a}\dot{b} = \dot{1} \) . Donc il existe \( m \in \mathcal{M} \) , \( {ab} = 1 + m \) , d’où \( 1 = {ab} - m \in I \) . Donc \( I = A \) et \( \mathcal{M} \) est maximal.

> Sufficient condition. Let \( I \) be an ideal of \( A \) such that \( \mathcal{M} \subset I \) and \( \mathcal{M} \neq I \) . Let \( a \in I, a \notin \mathcal{M} \) . We have \( \dot{a} \neq \dot{0} \) so that \( A/\mathcal{M} \) being a field, there exists \( b \in A,\dot{a}\dot{b} = \dot{1} \) . Thus there exists \( m \in \mathcal{M} \) , \( {ab} = 1 + m \) , whence \( 1 = {ab} - m \in I \) . Therefore \( I = A \) and \( \mathcal{M} \) is maximal.

c) Soit \( \mathcal{M} \) un idéal de \( A \) maximal. L’anneau quotient \( A/\mathcal{M} \) est un corps donc un anneau intègre, donc \( \mathcal{M} \) est premier.

> c) Let \( \mathcal{M} \) be a maximal ideal of \( A \) . The quotient ring \( A/\mathcal{M} \) is a field, hence an integral domain, so \( \mathcal{M} \) is prime.

d) Soit \( I \) un idéal de \( A \) tel que \( \mathcal{P} \subset I \) et \( \mathcal{P} \neq I \) . Comme \( A \) est principal, il existe \( m \in \mathcal{P} \) tel que \( \mathcal{P} = \left( m\right) \) et il existe \( a \in I, I = \left( a\right) \) . Comme \( m \in I \) , il existe \( q \in A \) tel que \( m = {aq} \) . L’idéal \( \mathcal{P} \) étant premier, on a \( a \in \mathcal{P} \) ou \( q \in \mathcal{P} \) . Or \( a \notin \mathcal{P} \) sinon \( \mathcal{P} = I \) . Donc \( q \in \mathcal{P} \) , de sorte qu’il existe \( p \in A \) tel que \( q = {mp} \) . Donc \( m = {aq} = {amp} \) d’où \( m\left( {1 - {ap}}\right) = 0 \) d’où \( {ap} = 1 \) (car \( A \) est principal donc intègre et \( m \neq 0 \) sinon \( \mathcal{P} = 0 \) ). Or \( {ap} \in I \) , donc \( 1 \in I \) , donc \( I = A \) , d’où le résultat.

> d) Let \( I \) be an ideal of \( A \) such that \( \mathcal{P} \subset I \) and \( \mathcal{P} \neq I \) . Since \( A \) is a principal ideal domain, there exists \( m \in \mathcal{P} \) such that \( \mathcal{P} = \left( m\right) \) and there exists \( a \in I, I = \left( a\right) \) . As \( m \in I \) , there exists \( q \in A \) such that \( m = {aq} \) . The ideal \( \mathcal{P} \) being prime, we have \( a \in \mathcal{P} \) or \( q \in \mathcal{P} \) . However, \( a \notin \mathcal{P} \) otherwise \( \mathcal{P} = I \) . Thus \( q \in \mathcal{P} \) , so there exists \( p \in A \) such that \( q = {mp} \) . Therefore \( m = {aq} = {amp} \) whence \( m\left( {1 - {ap}}\right) = 0 \) whence \( {ap} = 1 \) (since \( A \) is a principal ideal domain, hence an integral domain, and \( m \neq 0 \) otherwise \( \mathcal{P} = 0 \) ). However, \( {ap} \in I \) , so \( 1 \in I \) , so \( I = A \) , whence the result.

EXERCICE 5. Soit \( n \geq 2 \) un entier. Si \( a \) est un entier premier avec \( n \) montrer

> EXERCISE 5. Let \( n \geq 2 \) be an integer. If \( a \) is an integer coprime to \( n \) show that

\[
{a}^{n!} \equiv  1\;\left( {\;\operatorname{mod}\;n}\right)
\]

Solution. D’après le théorème d’Euler, on sait que \( {a}^{\varphi \left( n\right) } \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) où \( \varphi \) désigne l’indicateur d’Euler. Le résultat sera donc démontré si on prouve \( \varphi \left( n\right) \mid n! \) , ce qui est immédiat car \( \varphi \left( n\right) \leq n \) .

> Solution. According to Euler's theorem, we know that \( {a}^{\varphi \left( n\right) } \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) where \( \varphi \) denotes Euler's totient function. The result will thus be proven if we show \( \varphi \left( n\right) \mid n! \) , which is immediate since \( \varphi \left( n\right) \leq n \) .

EXERCICE 6 (ANNEAUX NOETHÉRIENS). On dit qu'un anneau commutatif unitaire \( A \) est noethérien si tout idéal \( I \) de \( A \) est engendré par un nombre fini d’éléments (i. e. il existe \( \left. {{x}_{1},\ldots ,{x}_{k} \in I\text{ tels que }\left( {x}_{1}\right) + \cdots + \left( {x}_{k}\right) = I}\right) \) . Montrer que \( A \) est noethérien si et seulement s’il n’existe pas de suite d’idéaux de \( A \) strictement croissante au sens de l'inclusion.

> EXERCISE 6 (NOETHERIAN RINGS). A commutative unital ring \( A \) is said to be Noetherian if every ideal \( I \) of \( A \) is generated by a finite number of elements (i.e., there exists \( \left. {{x}_{1},\ldots ,{x}_{k} \in I\text{ tels que }\left( {x}_{1}\right) + \cdots + \left( {x}_{k}\right) = I}\right) \) . Show that \( A \) is Noetherian if and only if there is no strictly increasing sequence of ideals of \( A \) with respect to inclusion.

Solution. Condition nécessaire. Soit \( {\left( {I}_{n}\right) }_{n \in \mathbb{N}} \) une suite croissante d’idéaux de \( A \) . On vérifie fa-cilement que \( I = { \cup }_{n \in \mathbb{N}}{I}_{n} \) est un idéal de \( A \) . Il est donc engendré par un nombre fini d’éléments \( {x}_{1},\ldots ,{x}_{p} \in I \) . Or chaque \( {x}_{i} \) appartient à \( I = { \cup }_{n \in \mathbb{N}}{I}_{n} \) et donc il existe \( {n}_{i} \) tel que \( {x}_{i} \in {I}_{{n}_{i}} \) . Si \( N = \mathop{\sup }\limits_{{1 < i < p}}{n}_{i} \) , la suite \( \left( {I}_{n}\right) \) étant croissante, tous les \( {x}_{i}\left( {1 \leq i \leq p}\right) \) appartiennent à \( {I}_{N} \) , et donc \( I = \left( {x}_{1}\right) + \cdots + \left( {x}_{p}\right) \subset {I}_{N} \) . Par ailleurs \( {I}_{N} \subset I \) puisque \( I = { \cup }_{i \in \mathbb{N}}{I}_{n} \) . Donc \( {I}_{N} = I \) , ce qui entraîne que la suite \( \left( {I}_{n}\right) \) est stationnaire pour \( n \geq N \) .

> Solution. Necessary condition. Let \( {\left( {I}_{n}\right) }_{n \in \mathbb{N}} \) be an increasing sequence of ideals of \( A \) . It is easily verified that \( I = { \cup }_{n \in \mathbb{N}}{I}_{n} \) is an ideal of \( A \) . It is therefore generated by a finite number of elements \( {x}_{1},\ldots ,{x}_{p} \in I \) . However, each \( {x}_{i} \) belongs to \( I = { \cup }_{n \in \mathbb{N}}{I}_{n} \) and thus there exists \( {n}_{i} \) such that \( {x}_{i} \in {I}_{{n}_{i}} \) . If \( N = \mathop{\sup }\limits_{{1 < i < p}}{n}_{i} \) , since the sequence \( \left( {I}_{n}\right) \) is increasing, all \( {x}_{i}\left( {1 \leq i \leq p}\right) \) belong to \( {I}_{N} \) , and thus \( I = \left( {x}_{1}\right) + \cdots + \left( {x}_{p}\right) \subset {I}_{N} \) . Furthermore, \( {I}_{N} \subset I \) since \( I = { \cup }_{i \in \mathbb{N}}{I}_{n} \) . Thus \( {I}_{N} = I \) , which implies that the sequence \( \left( {I}_{n}\right) \) is stationary for \( n \geq N \) .

Condition suffisante. Soit \( I \) un idéal de \( A \) . Supposons que \( I \) ne puisse pas être engendré par un nombre fini d’éléments. Sous cette hypothèse, nous allons construire une suite \( \left( {x}_{n}\right) \) d’éléments de \( I \) tels que \( {x}_{n + 1} \notin \left( {x}_{1}\right) + \cdots + \left( {x}_{n}\right) \) .

> Sufficient condition. Let \( I \) be an ideal of \( A \) . Suppose that \( I \) cannot be generated by a finite number of elements. Under this hypothesis, we will construct a sequence \( \left( {x}_{n}\right) \) of elements of \( I \) such that \( {x}_{n + 1} \notin \left( {x}_{1}\right) + \cdots + \left( {x}_{n}\right) \) .

- On choisit un élément \( {x}_{1} \in  I \) .

> - We choose an element \( {x}_{1} \in  I \) .

- \( {x}_{1},\ldots ,{x}_{n} \in  I \) étant supposés construits, on sait que \( \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right)  \neq  I \) car \( I \) ne peut pas être engendré par un nombre fini d’éléments. On choisit alors \( {x}_{n + 1} \in  I,{x}_{n + 1} \notin  \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right) \) . Ainsi, si on pose \( {I}_{n} = \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right) \) , la suite \( \left( {I}_{n}\right) \) est une suite d’idéaux de \( A \) strictement croissante au sens de l'inclusion, ce qui est contraire aux hypothèses. Donc \( I \) peut être engendré par un nombre fini d'éléments, d'où le résultat.

> - With \( {x}_{1},\ldots ,{x}_{n} \in  I \) assumed to be constructed, we know that \( \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right)  \neq  I \) because \( I \) cannot be generated by a finite number of elements. We then choose \( {x}_{n + 1} \in  I,{x}_{n + 1} \notin  \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right) \) . Thus, if we set \( {I}_{n} = \left( {x}_{1}\right)  + \cdots  + \left( {x}_{n}\right) \) , the sequence \( \left( {I}_{n}\right) \) is a strictly increasing sequence of ideals of \( A \) in the sense of inclusion, which contradicts the hypotheses. Therefore, \( I \) can be generated by a finite number of elements, hence the result.

Remarque. Tout anneau principal est noethérien.

> Remark. Every principal ideal ring is Noetherian.
