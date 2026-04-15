#### 2.4. Exercises

*Français : 2.4. Exercices*

EXERCICE 1. Soit \( E \) un \( \mathbb{K} \) -e.v et \( f \in \mathcal{L}\left( E\right) \) admettant un polynôme minimal. Si \( f \) est inversible, montrer que \( {f}^{-1} \) est un polynôme en \( f \) .

> EXERCISE 1. Let \( E \) be a \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( E\right) \) admitting a minimal polynomial. If \( f \) is invertible, show that \( {f}^{-1} \) is a polynomial in \( f \) .

Solution. Montrons déjà que \( X \) ne divise pas le polynôme minimal \( {\Pi }_{f} \) de \( f \) . En effet, s’il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {\Pi }_{f} = {XP} \) , alors \( 0 = {\Pi }_{f}\left( f\right) = f \circ P\left( f\right) \) , et comme \( f \) est inversible, \( P\left( f\right) = 0 \) . Comme deg \( P < \deg {\Pi }_{f} \) , ceci contredit le fait que \( {\Pi }_{f} \) est le polynôme minimal de \( f \) .

> Solution. Let us first show that \( X \) does not divide the minimal polynomial \( {\Pi }_{f} \) of \( f \) . Indeed, if there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {\Pi }_{f} = {XP} \) , then \( 0 = {\Pi }_{f}\left( f\right) = f \circ P\left( f\right) \) , and since \( f \) is invertible, \( P\left( f\right) = 0 \) . As deg \( P < \deg {\Pi }_{f} \) , this contradicts the fact that \( {\Pi }_{f} \) is the minimal polynomial of \( f \) .

Donc \( X \nmid {\Pi }_{f} \) . Comme \( X \) est irréductible, \( X \) et \( {\Pi }_{f} \) sont premiers entre eux, donc il existe \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( {UX} + V{\Pi }_{f} = 1 \) , d’où on tire \( U\left( f\right) \circ f + V\left( f\right) \circ {\Pi }_{f}\left( f\right) = {\operatorname{Id}}_{E} \) , c’est-à-dire \( U\left( f\right) \circ f = {\operatorname{Id}}_{E} \) . Donc \( {f}^{-1} = U\left( f\right) \) , d’où le résultat.

> Thus \( X \nmid {\Pi }_{f} \) . Since \( X \) is irreducible, \( X \) and \( {\Pi }_{f} \) are coprime, so there exist \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {UX} + V{\Pi }_{f} = 1 \) , from which we derive \( U\left( f\right) \circ f + V\left( f\right) \circ {\Pi }_{f}\left( f\right) = {\operatorname{Id}}_{E} \) , that is to say \( U\left( f\right) \circ f = {\operatorname{Id}}_{E} \) . Therefore \( {f}^{-1} = U\left( f\right) \) , hence the result.

Remarque. En dimension finie, on aurait pu raisonner avec le polynôme caractéristique \( {P}_{f} \) de \( f : \) comme \( {P}_{f}\left( 0\right) = \det f \neq 0 \) , on a \( X \nmid {P}_{f} \) et on procède ensuite comme plus haut. - On peut également donner une forme explicite d’un polynôme \( U \) tel que \( {f}^{-1} = U\left( f\right) \) en fonction du polynôme minimal : il suffit de prendre \( U = \left( {{\Pi }_{f}\left( 0\right) - {\Pi }_{f}\left( X\right) }\right) /\left( {{\Pi }_{f}\left( 0\right) X}\right) \) .

> Remark. In finite dimension, we could have reasoned with the characteristic polynomial \( {P}_{f} \) of \( f : \) as \( {P}_{f}\left( 0\right) = \det f \neq 0 \) , we have \( X \nmid {P}_{f} \) and then proceed as above. - One can also provide an explicit form of a polynomial \( U \) such that \( {f}^{-1} = U\left( f\right) \) in terms of the minimal polynomial: it suffices to take \( U = \left( {{\Pi }_{f}\left( 0\right) - {\Pi }_{f}\left( X\right) }\right) /\left( {{\Pi }_{f}\left( 0\right) X}\right) \) .

EXERCICE 2. Soit \( \mathbb{K} \) un corps commutatif fini à \( q \) éléments, \( E \) un \( \mathbb{K} \) -e.v de dimension finie et \( f \in \mathcal{L}\left( E\right) \) . Montrer que \( f \) est diagonalisable dans \( E \) si et seulement si \( {f}^{q} = f \) .

> EXERCISE 2. Let \( \mathbb{K} \) be a finite commutative field with \( q \) elements, \( E \) a finite-dimensional \( \mathbb{K} \) -v.s. and \( f \in \mathcal{L}\left( E\right) \) . Show that \( f \) is diagonalizable in \( E \) if and only if \( {f}^{q} = f \) .

Solution. Commençons par montrer

> Solution. Let us begin by showing

\[
{X}^{q} - X = \mathop{\prod }\limits_{{\alpha  \in  \mathbb{K}}}\left( {X - \alpha }\right)
\]

(*)

> Muni de la loi produit, \( {\mathbb{K}}^{ * } \) est un groupe multiplicatif à \( q - 1 \) éléments, donc pour tout \( x \in {\mathbb{K}}^{ * } \) , \( {x}^{q - 1} = 1 \) , d’où pour tout \( x \in \mathbb{K},{x}^{q} = x \) . On a ainsi déterminé \( q \) racines distinctes du polynôme \( {X}^{q} - X \) qui est de degré q, d’où \( \left( *\right) \) .

Equipped with the product law, \( {\mathbb{K}}^{ * } \) is a multiplicative group with \( q - 1 \) elements, so for all \( x \in {\mathbb{K}}^{ * } \) , \( {x}^{q - 1} = 1 \) , hence for all \( x \in \mathbb{K},{x}^{q} = x \) . We have thus determined \( q \) distinct roots of the polynomial \( {X}^{q} - X \) which is of degree q, hence \( \left( *\right) \) .

> Concluons. D'après le théorème 2, on peut affirmer que \( f \) est diagonalisable si et seulement s’il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , scindé sur \( \mathbb{K} \) ,à racines toutes simples, tel que \( P\left( f\right) = 0 \) , autrement dit si et seulement s’il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \mid \mathop{\prod }\limits_{{\alpha \in \mathbb{K}}}\left( {X - \alpha }\right) = {X}^{q} - X \) tel que \( P\left( f\right) = 0 \) . En d’autres termes, \( f \) est diagonalisable si et seulement si \( {f}^{q} - f = 0 \) .

Let us conclude. According to Theorem 2, we can state that \( f \) is diagonalizable if and only if there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , split over \( \mathbb{K} \) , with all simple roots, such that \( P\left( f\right) = 0 \) , in other words if and only if there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \mid \mathop{\prod }\limits_{{\alpha \in \mathbb{K}}}\left( {X - \alpha }\right) = {X}^{q} - X \) such that \( P\left( f\right) = 0 \) . In other words, \( f \) is diagonalizable if and only if \( {f}^{q} - f = 0 \) .

> EXERCICE 3. Soient \( E \) un \( \mathbb{K} \) -espace vectoriel et \( f \in \mathcal{L}\left( E\right) \) admettant un polynôme minimal \( {\Pi }_{f} \) . Pour tout \( x \in E \) , on note \( {P}_{x} \) le polynôme unitaire de \( \mathbb{K}\left\lbrack X\right\rbrack \) de plus bas degré tel que \( {P}_{x}\left( f\right) \left( x\right) = 0\left( {P}_{x}\right. \) s’appelle le polynôme minimal de \( x \) relatif à \( \left. f\right) \) .

EXERCISE 3. Let \( E \) be a \( \mathbb{K} \) -vector space and \( f \in \mathcal{L}\left( E\right) \) admitting a minimal polynomial \( {\Pi }_{f} \) . For any \( x \in E \) , we denote by \( {P}_{x} \) the monic polynomial of \( \mathbb{K}\left\lbrack X\right\rbrack \) of lowest degree such that \( {P}_{x}\left( f\right) \left( x\right) = 0\left( {P}_{x}\right. \) is called the minimal polynomial of \( x \) relative to \( \left. f\right) \) .

> 1/a) Montrer l’existence et l’unicité de \( {P}_{x} \) . Si \( P\left( f\right) \left( x\right) = 0 \) avec \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , montrer que \( {P}_{x} \mid P \) .

1/a) Show the existence and uniqueness of \( {P}_{x} \) . If \( P\left( f\right) \left( x\right) = 0 \) with \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , show that \( {P}_{x} \mid P \) .

> b) Montrer que \( {E}_{x} = \{ P\left( f\right) \left( x\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) est un s.e.v de dimension \( \deg \left( {P}_{x}\right) \) .

b) Show that \( {E}_{x} = \{ P\left( f\right) \left( x\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) is a subspace of dimension \( \deg \left( {P}_{x}\right) \) .

> 2/a) Si \( {E}_{x} \cap {E}_{y} = \{ 0\} \) , montrer que \( {P}_{x + y} = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) . Généraliser à \( p \) vecteurs \( {x}_{1},\ldots ,{x}_{p}. \)

2/a) If \( {E}_{x} \cap {E}_{y} = \{ 0\} \) , show that \( {P}_{x + y} = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) . Generalize to \( p \) vectors \( {x}_{1},\ldots ,{x}_{p}. \)

> b) Si \( {P}_{x} \) et \( {P}_{y} \) sont premiers entre eux, montrer \( {E}_{x + y} = {E}_{x} \oplus {E}_{y} \) . Généraliser à \( p \) vecteurs \( {x}_{1},\ldots ,{x}_{p}. \)

b) If \( {P}_{x} \) and \( {P}_{y} \) are coprime, show \( {E}_{x + y} = {E}_{x} \oplus {E}_{y} \) . Generalize to \( p \) vectors \( {x}_{1},\ldots ,{x}_{p}. \)

> 3/a) Soit \( M \in \mathbb{K}\left\lbrack X\right\rbrack \) un facteur irréductible de \( {\Pi }_{f},\alpha \) sa multiplicité dans la décomposition de \( {\Pi }_{f} \) en facteurs irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) . Montrer qu’il existe \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) tel que \( {P}_{x} = {M}^{\alpha }. \)

3/a) Let \( M \in \mathbb{K}\left\lbrack X\right\rbrack \) be an irreducible factor of \( {\Pi }_{f},\alpha \) its multiplicity in the decomposition of \( {\Pi }_{f} \) into irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \) . Show that there exists \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) such that \( {P}_{x} = {M}^{\alpha }. \)

> b) Montrer qu’il existe \( x \in E \) tel que \( {P}_{x} = {\Pi }_{f} \) .

b) Show that there exists \( x \in E \) such that \( {P}_{x} = {\Pi }_{f} \) .

> Solution. 1/a) Soit \( {I}_{x} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) \left( x\right) = 0\} \) . C’est un idéal de \( \mathbb{K}\left\lbrack X\right\rbrack \) , non réduit à \( \{ 0\} \) car \( {\Pi }_{f} \in {I}_{x} \) . Il existe donc un unique polynôme unitaire \( {P}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {I}_{x} = \left( {P}_{x}\right) \) . Ainsi, \( {P}_{x} \) est le polynôme unitaire de plus bas degré tel que \( {P}_{x}\left( f\right) \left( x\right) = 0 \) . Si maintenant \( P\left( f\right) \left( x\right) = 0 \) , alors on a \( P \in {I}_{x} = \left( {P}_{x}\right) \) , donc \( {P}_{x} \mid P \) .

Solution. 1/a) Let \( {I}_{x} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) \left( x\right) = 0\} \) . This is an ideal of \( \mathbb{K}\left\lbrack X\right\rbrack \) , not reduced to \( \{ 0\} \) because \( {\Pi }_{f} \in {I}_{x} \) . There exists, therefore, a unique monic polynomial \( {P}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {I}_{x} = \left( {P}_{x}\right) \) . Thus, \( {P}_{x} \) is the monic polynomial of lowest degree such that \( {P}_{x}\left( f\right) \left( x\right) = 0 \) . If now \( P\left( f\right) \left( x\right) = 0 \) , then we have \( P \in {I}_{x} = \left( {P}_{x}\right) \) , so \( {P}_{x} \mid P \) .

> b) L'application linéaire

b) The linear map

\[
\varphi  : \mathbb{K}\left\lbrack  X\right\rbrack   \rightarrow  {E}_{x}\;P \mapsto  P\left( f\right) \left( x\right)
\]

est surjective. On en déduit que le s.e.v \( {E}_{x} \) est isomorphe à \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {P}_{x}\right) \) , donc de dimension \( \deg \left( {P}_{x}\right) \) .

> is surjective. We deduce that the subspace \( {E}_{x} \) is isomorphic to \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {P}_{x}\right) \) , and thus of dimension \( \deg \left( {P}_{x}\right) \) .

2/a) Notons \( Q = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) . Comme \( {P}_{x + y}\left( f\right) \left( {x + y}\right) = 0 \) , on a \( {P}_{x + y}\left( f\right) \left( x\right) = - {P}_{x + y}\left( f\right) \left( y\right) \) . Ces deux vecteurs sont donc éléments de \( {E}_{x} \cap {E}_{y} = \{ 0\} \) , donc nuls. Donc d’après 1/ a), \( {P}_{x} \mid {P}_{x + y} \) et \( {P}_{y} \mid {P}_{x + y} \) , d’où \( Q \mid {P}_{x + y} \) .

> 2/a) Let us denote \( Q = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) . Since \( {P}_{x + y}\left( f\right) \left( {x + y}\right) = 0 \) , we have \( {P}_{x + y}\left( f\right) \left( x\right) = - {P}_{x + y}\left( f\right) \left( y\right) \) . These two vectors are therefore elements of \( {E}_{x} \cap {E}_{y} = \{ 0\} \) , and thus zero. So, according to 1/ a), \( {P}_{x} \mid {P}_{x + y} \) and \( {P}_{y} \mid {P}_{x + y} \) , hence \( Q \mid {P}_{x + y} \) .

Or \( {P}_{x} \mid Q \) donc \( Q\left( f\right) \left( x\right) = 0 \) . De même, \( Q\left( f\right) \left( y\right) = 0 \) , donc \( Q\left( f\right) \left( {x + y}\right) = 0 \) . Donc \( {P}_{x + y} \mid Q \) , ce comme on a vu que \( Q \mid {P}_{x + y} \) , on en déduit \( {P}_{x + y} = Q = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) , ces deux polynômes étant unitaires.

> However, \( {P}_{x} \mid Q \) so \( Q\left( f\right) \left( x\right) = 0 \) . Similarly, \( Q\left( f\right) \left( y\right) = 0 \) , so \( Q\left( f\right) \left( {x + y}\right) = 0 \) . Thus \( {P}_{x + y} \mid Q \) , and as we have seen that \( Q \mid {P}_{x + y} \) , we deduce \( {P}_{x + y} = Q = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right) \) , these two polynomials being monic.

- Par récurrence sur \( p \) , on montre maintenant facilement que si \( {E}_{{x}_{1}},\ldots ,{E}_{{x}_{p}} \) sont en somme directe, alors \( {P}_{{x}_{1} + \cdots  + {x}_{p}} = \operatorname{ppcm}\left( {{P}_{{x}_{1}},\ldots ,{P}_{{x}_{p}}}\right) \) .

> - By induction on \( p \) , we now easily show that if \( {E}_{{x}_{1}},\ldots ,{E}_{{x}_{p}} \) are in direct sum, then \( {P}_{{x}_{1} + \cdots  + {x}_{p}} = \operatorname{ppcm}\left( {{P}_{{x}_{1}},\ldots ,{P}_{{x}_{p}}}\right) \) .

b) Montrons tout d’abord que \( {E}_{x} \cap {E}_{y} = \{ 0\} \) . Soit \( z \in {E}_{x} \cap {E}_{y} \) . Il existe \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( z = P\left( f\right) \left( x\right) = Q\left( f\right) \left( y\right) \) . Or

> b) Let us first show that \( {E}_{x} \cap {E}_{y} = \{ 0\} \) . Let \( z \in {E}_{x} \cap {E}_{y} \) . There exist \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( z = P\left( f\right) \left( x\right) = Q\left( f\right) \left( y\right) \) . However

\[
0 = P\left( f\right)  \circ  {P}_{x}\left( f\right) \left( x\right)  = \left( {P{P}_{x}}\right) \left( f\right) \left( x\right)  = {P}_{x}\left( f\right)  \circ  P\left( f\right) \left( x\right)  = {P}_{x}\left( f\right) \left( z\right)  = \left( {{P}_{x}Q}\right) \left( f\right) \left( y\right) ,
\]

donc d’après \( 1/ \) a), \( {P}_{y} \mid {P}_{x}Q \) . Or \( {P}_{x} \) et \( {P}_{y} \) sont premiers entre eux, donc d’après le théorème de Gauss, \( {P}_{y} \mid Q \) , et donc \( z = Q\left( f\right) \left( y\right) = 0 \) . Ainsi, on a bien \( {E}_{x} \cap {E}_{y} = \{ 0\} \) .

> therefore, according to \( 1/ \) a), \( {P}_{y} \mid {P}_{x}Q \) . Now \( {P}_{x} \) and \( {P}_{y} \) are coprime, so by Gauss's theorem, \( {P}_{y} \mid Q \) , and thus \( z = Q\left( f\right) \left( y\right) = 0 \) . Thus, we indeed have \( {E}_{x} \cap {E}_{y} = \{ 0\} \) .

- D’après 2/ a), on a donc \( {P}_{x + y} = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right)  = {P}_{x}{P}_{y} \) , d’où

> - According to 2/ a), we therefore have \( {P}_{x + y} = \operatorname{ppcm}\left( {{P}_{x},{P}_{y}}\right)  = {P}_{x}{P}_{y} \) , whence

\[
\dim {E}_{x + y} = \deg \left( {P}_{x + y}\right)  = \deg \left( {P}_{x}\right)  + \deg \left( {P}_{y}\right)  = \dim {E}_{x} + \dim {E}_{y}.
\]

(*)

> Par ailleurs lorsque \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , l’égalité \( P\left( f\right) \left( {x + y}\right) = P\left( f\right) \left( x\right) + P\left( f\right) \left( y\right) \) entraîne l’inclusion \( {E}_{x + y} \subset {E}_{x} + {E}_{y} = {E}_{x} \oplus {E}_{y} \) , donc d’après \( \left( *\right) ,{E}_{x + y} = {E}_{x} \oplus {E}_{y} \) .

Furthermore, when \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , the equality \( P\left( f\right) \left( {x + y}\right) = P\left( f\right) \left( x\right) + P\left( f\right) \left( y\right) \) implies the inclusion \( {E}_{x + y} \subset {E}_{x} + {E}_{y} = {E}_{x} \oplus {E}_{y} \) , so according to \( \left( *\right) ,{E}_{x + y} = {E}_{x} \oplus {E}_{y} \) .

> Par récurrence sur \( p \) , on montre maintenant facilement que si \( {P}_{{x}_{1}},\ldots ,{P}_{{x}_{p}} \) sont premiers entre eux deux à deux, alors \( {E}_{{x}_{1} + \cdots + {x}_{p}} = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{p}} \) .

By induction on \( p \) , we now easily show that if \( {P}_{{x}_{1}},\ldots ,{P}_{{x}_{p}} \) are pairwise coprime, then \( {E}_{{x}_{1} + \cdots + {x}_{p}} = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{p}} \) .

> 3/a) On peut écrire \( {\Pi }_{f} = {M}^{\alpha }N \) où \( N \in \mathbb{K}\left\lbrack X\right\rbrack \) est premier avec \( M \) (donc avec \( {M}^{\alpha } \) ). D’après le théorème de décomposition des noyaux, on a

3/a) We can write \( {\Pi }_{f} = {M}^{\alpha }N \) where \( N \in \mathbb{K}\left\lbrack X\right\rbrack \) is coprime to \( M \) (and thus to \( {M}^{\alpha } \) ). According to the primary decomposition theorem, we have

\[
E = \operatorname{Ker}{M}^{\alpha }\left( f\right)  \oplus  \operatorname{Ker}N\left( f\right) .
\]

\( \left( {* * }\right) \)

> Pour tout \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) , on a \( {M}^{\alpha }\left( f\right) \left( x\right) = 0 \) , donc d’après \( 1/ \) a), \( {P}_{x} \mid {M}^{\alpha } \) et comme \( M \) est irréductible, il existe \( {\beta }_{x} \leq \alpha \) tel que \( {P}_{x} = {M}^{{\beta }_{x}} \) . Il s’agit de montrer qu’il existe \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) tel que \( {\beta }_{x} = \alpha \) . Raisonnons par l’absurde et supposons le contraire, de sorte que pour tout \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) ,{P}_{x} \mid {M}^{\alpha - 1}, \) i. e. \( {M}^{\alpha - 1}\left( f\right) \left( x\right) = 0 \) , autrement dit \( \operatorname{Ker}{M}^{\alpha }\left( f\right) = \operatorname{Ker}{M}^{\alpha - 1}\left( f\right) \) . D’après \( \left( {* * }\right) , E = \operatorname{Ker}{M}^{\alpha - 1}\left( f\right) \oplus \operatorname{Ker}N\left( f\right) \) ce qui d’après le théorème de décomposition des noyaux entraîne \( \operatorname{Ker}\left( {{M}^{\alpha - 1}N\left( f\right) }\right) = E \) , ou encore \( {M}^{\alpha - 1}N\left( f\right) = Q\left( f\right) = 0 \) , ce qui contredit la minimalité du degré du polynôme minimal \( {\Pi }_{f} \) de \( f \) car \( \deg Q < \deg {\Pi }_{f} \) . Donc il existe \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) tel que \( {P}_{x} = {M}^{\alpha } \) .

For all \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) , we have \( {M}^{\alpha }\left( f\right) \left( x\right) = 0 \) , so according to \( 1/ \) a), \( {P}_{x} \mid {M}^{\alpha } \) and since \( M \) is irreducible, there exists \( {\beta }_{x} \leq \alpha \) such that \( {P}_{x} = {M}^{{\beta }_{x}} \) . We must show that there exists \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) such that \( {\beta }_{x} = \alpha \) . Let us reason by contradiction and assume the opposite, such that for all \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) ,{P}_{x} \mid {M}^{\alpha - 1}, \) i.e. \( {M}^{\alpha - 1}\left( f\right) \left( x\right) = 0 \) , in other words \( \operatorname{Ker}{M}^{\alpha }\left( f\right) = \operatorname{Ker}{M}^{\alpha - 1}\left( f\right) \) . According to \( \left( {* * }\right) , E = \operatorname{Ker}{M}^{\alpha - 1}\left( f\right) \oplus \operatorname{Ker}N\left( f\right) \) which, by the primary decomposition theorem, implies \( \operatorname{Ker}\left( {{M}^{\alpha - 1}N\left( f\right) }\right) = E \) , or \( {M}^{\alpha - 1}N\left( f\right) = Q\left( f\right) = 0 \) , which contradicts the minimality of the degree of the minimal polynomial \( {\Pi }_{f} \) of \( f \) because \( \deg Q < \deg {\Pi }_{f} \) . Thus there exists \( x \in \operatorname{Ker}{M}^{\alpha }\left( f\right) \) such that \( {P}_{x} = {M}^{\alpha } \) .

> b) Soit \( {\Pi }_{f} = \mathop{\prod }\limits_{{i = 1}}^{k}{M}_{i}^{{\alpha }_{i}} \) la décomposition de \( {\Pi }_{f} \) en facteurs irréductibles de \( \mathbb{K}\left\lbrack X\right\rbrack \) . D’après la question précédente, pour tout \( i \) , il existe \( {x}_{i} \in \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \) tel que \( {P}_{{x}_{i}} = {M}_{i}^{{\alpha }_{i}} \) . D’après la question \( 2/\mathrm{b}) \) , on a donc \( {E}_{{x}_{1} + \cdots + {x}_{k}} = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) , et donc d’après la question \( 2/\mathrm{a}) \) , on a

b) Let \( {\Pi }_{f} = \mathop{\prod }\limits_{{i = 1}}^{k}{M}_{i}^{{\alpha }_{i}} \) be the decomposition of \( {\Pi }_{f} \) into irreducible factors of \( \mathbb{K}\left\lbrack X\right\rbrack \) . According to the previous question, for all \( i \) , there exists \( {x}_{i} \in \operatorname{Ker}{M}_{i}^{{\alpha }_{i}}\left( f\right) \) such that \( {P}_{{x}_{i}} = {M}_{i}^{{\alpha }_{i}} \) . According to question \( 2/\mathrm{b}) \) , we therefore have \( {E}_{{x}_{1} + \cdots + {x}_{k}} = {E}_{{x}_{1}} \oplus \cdots \oplus {E}_{{x}_{k}} \) , and thus according to question \( 2/\mathrm{a}) \) , we have

\[
{P}_{{x}_{1} + \cdots  + {x}_{k}} = \mathop{\prod }\limits_{{i = 1}}^{k}{P}_{{x}_{i}} = \mathop{\prod }\limits_{{i = 1}}^{k}{M}_{i}^{{\alpha }_{i}} = {\Pi }_{f},
\]

d'où le résultat.

> whence the result.

EXERCICE 4 (DIAGONALISATION D'UN DÉTERMINANT CIRCULANT). On considère la matrice circulante

> EXERCISE 4 (DIAGONALIZATION OF A CIRCULANT DETERMINANT). Consider the circulant matrix

\[
A = \left( \begin{matrix} {a}_{1} & {a}_{2} & \cdots & {a}_{n} \\  {a}_{n} & {a}_{1} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & {a}_{2} \\  {a}_{2} & \cdots & {a}_{n} & {a}_{1} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) .
\]

En exprimant \( A \) comme un polynôme en la matrice

> By expressing \( A \) as a polynomial in the matrix

\[
J = \left( \begin{matrix} 0 & 1 & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  0 & &  \ddots  & 1 \\  1 & 0 & \cdots & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right)
\]

diagonaliser \( A \) .

> diagonalize \( A \) .

Solution. Si \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) désigne la base canonique de \( {\mathbb{C}}^{n}, J \) est la matrice de l’endomor-phisme qui à \( {e}_{i} \) associe \( {e}_{i - 1} \) si \( i \geq 2 \) , et à \( {e}_{1} \) associe \( {e}_{n} \) . Pour tout \( p,1 \leq p \leq n - 1,{J}^{p} \) est donc la matrice qui à \( {e}_{i} \) associe \( {e}_{i - p} \) si \( i > p \) ,à \( {e}_{i} \) associe \( {e}_{i + n - p} \) si \( i \leq p \) , autrement dit

> Solution. If \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) denotes the canonical basis of \( {\mathbb{C}}^{n}, J \) is the matrix of the endomorphism that maps \( {e}_{i} \) to \( {e}_{i - 1} \) if \( i \geq 2 \) , and maps \( {e}_{1} \) to \( {e}_{n} \) . For any \( p,1 \leq p \leq n - 1,{J}^{p} \) is therefore the matrix that maps \( {e}_{i} \) to \( {e}_{i - p} \) if \( i > p \) , maps \( {e}_{i} \) to \( {e}_{i + n - p} \) if \( i \leq p \) , in other words

\[
\forall p,1 \leq  p \leq  n - 1,\;{J}^{p} = \left( \begin{matrix} 0 & {I}_{n - p} \\  {I}_{p} & 0 \end{matrix}\right) .
\]

On en déduit que pour tout \( {\alpha }_{1},\ldots ,{\alpha }_{n} \in \mathbb{C} \) ,

> We deduce that for any \( {\alpha }_{1},\ldots ,{\alpha }_{n} \in \mathbb{C} \) ,

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\alpha }_{i}{J}^{i - 1} = \left( \begin{matrix} {\alpha }_{1} & {\alpha }_{2} & \cdots & {\alpha }_{n} \\  {\alpha }_{n} & {\alpha }_{1} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & {\alpha }_{2} \\  {\alpha }_{2} & \cdots & {\alpha }_{n} & {\alpha }_{1} \end{matrix}\right)
\]

Ceci montre en particulier que \( A = P\left( J\right) \) où \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{i - 1} \) . Ceci montre également que si \( Q \in \mathbb{K}\left\lbrack X\right\rbrack , Q \neq 0 \) et \( \deg Q < n \) , alors \( Q\left( J\right) \neq 0 \) . Le polynôme minimal de \( J \) vérifie donc \( \deg {\Pi }_{J} \geq n \) . Or \( {J}^{n} - I = 0 \) , on a donc \( {\Pi }_{J} = {X}^{n} - 1 \) . Or \( {\Pi }_{J} \) divise le polynôme caractéristique \( {P}_{J} \) de \( J \) et deg \( {P}_{J} = n \) , donc \( {P}_{J} = {\left( -1\right) }^{n}{\Pi }_{J} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) , où \( \omega = {e}^{{2i\pi }/n} \) . D’après le théorème 2, \( J \) est donc diagonalisable, et il existe \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que

> This shows in particular that \( A = P\left( J\right) \) where \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{i - 1} \) . This also shows that if \( Q \in \mathbb{K}\left\lbrack X\right\rbrack , Q \neq 0 \) and \( \deg Q < n \) , then \( Q\left( J\right) \neq 0 \) . The minimal polynomial of \( J \) therefore satisfies \( \deg {\Pi }_{J} \geq n \) . However \( {J}^{n} - I = 0 \) , we thus have \( {\Pi }_{J} = {X}^{n} - 1 \) . Now \( {\Pi }_{J} \) divides the characteristic polynomial \( {P}_{J} \) of \( J \) and deg \( {P}_{J} = n \) , so \( {P}_{J} = {\left( -1\right) }^{n}{\Pi }_{J} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) , where \( \omega = {e}^{{2i\pi }/n} \) . According to theorem 2, \( J \) is therefore diagonalizable, and there exists \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that

\[
{Q}^{-1}{JQ} = \left( \begin{matrix} 1 & & & 0 \\   & \omega & & \\   & 0 &  \ddots  & \\   & & & {\omega }^{n - 1} \end{matrix}\right) .
\]

On en déduit

> We deduce

\[
{Q}^{-1}{AQ} = {Q}^{-1}P\left( J\right) Q = P\left( {{Q}^{-1}{JQ}}\right)  = \left( \begin{matrix} P\left( 1\right) & & & 0 \\   & P\left( \omega \right) & & 0 \\   & &  \ddots  & \\  0 & & & P\left( {\omega }^{n - 1}\right)  \end{matrix}\right) .
\]

Remarque. On retrouve ainsi le résultat de l'exercice 12 page 153.

> Remark. We thus recover the result of exercise 12 on page 153.

EXERCICE 5. Donner une condition nécessaire et suffisante sur \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) pour que la matrice par blocs \( B = \left( \begin{matrix} A & A \\ 0 & A \end{matrix}\right) \in {\mathcal{M}}_{2n}\left( \mathbb{K}\right) \) soit diagonalisable.

> EXERCISE 5. Give a necessary and sufficient condition on \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) for the block matrix \( B = \left( \begin{matrix} A & A \\ 0 & A \end{matrix}\right) \in {\mathcal{M}}_{2n}\left( \mathbb{K}\right) \) to be diagonalizable.

Solution. Notons \( F \) le s.e.v de \( {\mathbb{K}}^{2n} \) engendré par les \( n \) premiers vecteurs de la base canonique de \( {\mathbb{K}}^{2n} \) . Le s.e.v \( F \) est stable par \( B \) . Si \( B \) est diagonalisable, sa restriction à \( F \) , qui n’est autre que \( A \) , est diagonalisable.

> Solution. Let \( F \) be the subspace of \( {\mathbb{K}}^{2n} \) spanned by the first \( n \) vectors of the canonical basis of \( {\mathbb{K}}^{2n} \) . The subspace \( F \) is stable under \( B \) . If \( B \) is diagonalizable, its restriction to \( F \) , which is none other than \( A \) , is diagonalizable.

Allons plus loin. Si \( B \) est diagonalisable, il existe un polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) , scindé sur \( \mathbb{K} \) , dont toutes les racines sont simples, tel que \( P\left( B\right) = 0 \) . Par récurrence sur \( k \) , on a facilement \( {B}^{k} = \left( \begin{matrix} {A}^{p} & p{A}^{p} \\ 0 & {A}^{p} \end{matrix}\right) \) pour tout \( k \in \mathbb{N} \) . De ceci, on déduit

> Let's go further. If \( B \) is diagonalizable, there exists a polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \), split over \( \mathbb{K} \), whose roots are all simple, such that \( P\left( B\right) = 0 \). By induction on \( k \), we easily have \( {B}^{k} = \left( \begin{matrix} {A}^{p} & p{A}^{p} \\ 0 & {A}^{p} \end{matrix}\right) \) for all \( k \in \mathbb{N} \). From this, we deduce

\[
0 = P\left( B\right)  = \left( \begin{matrix} P\left( A\right) & A{P}^{\prime }\left( A\right) \\  0 & P\left( A\right)  \end{matrix}\right)
\]

donc \( P\left( A\right) = A{P}^{\prime }\left( A\right) = 0 \) . Comme \( P\left( A\right) = 0 \) , on retrouve le fait que \( A \) est diagonalisable. Soit \( \lambda \) une valeur propre de \( A \) . Comme \( A{P}^{\prime }\left( A\right) = 0 \) , on a \( \lambda {P}^{\prime }\left( \lambda \right) = 0 \) . Or \( \lambda \) étant racine simple de \( P \) , on a \( {P}^{\prime }\left( \lambda \right) \neq 0 \) , donc \( \lambda = 0 \) . En résumé, \( A \) est diagonalisable et \( \lambda = 0 \) est la seule valeur propre de \( A \) , autrement dit, \( A = 0 \) .

> therefore \( P\left( A\right) = A{P}^{\prime }\left( A\right) = 0 \). As \( P\left( A\right) = 0 \), we recover the fact that \( A \) is diagonalizable. Let \( \lambda \) be an eigenvalue of \( A \). As \( A{P}^{\prime }\left( A\right) = 0 \), we have \( \lambda {P}^{\prime }\left( \lambda \right) = 0 \). However, since \( \lambda \) is a simple root of \( P \), we have \( {P}^{\prime }\left( \lambda \right) \neq 0 \), therefore \( \lambda = 0 \). In summary, \( A \) is diagonalizable and \( \lambda = 0 \) is the only eigenvalue of \( A \), in other words, \( A = 0 \).

Réciproquement, si \( A = 0, B \) est diagonalisable. Finalement, \( B \) est diagonalisable si et seulement si \( A = 0 \) .

> Conversely, if \( A = 0, B \) is diagonalizable. Finally, \( B \) is diagonalizable if and only if \( A = 0 \).

EXERCICE 6 (COMMUTANT D'UN ENDOMORPHISME). Soit \( E \) un \( \mathbb{K} \) -espace vectoriel de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Soit \( f \in \mathcal{L}\left( E\right) \) . On note \( {\Gamma }_{f} \) le s.e.v de \( \mathcal{L}\left( E\right) \) défini par

> EXERCISE 6 (COMMUTANT OF AN ENDOMORPHISM). Let \( E \) be a finite-dimensional \( \mathbb{K} \)-vector space \( n \in {\mathbb{N}}^{ * } \). Let \( f \in \mathcal{L}\left( E\right) \). We denote by \( {\Gamma }_{f} \) the subspace of \( \mathcal{L}\left( E\right) \) defined by

\[
{\Gamma }_{f} = \{ g \in  \mathcal{L}\left( E\right)  \mid  f \circ  g = g \circ  f\} .
\]

1/a) Si \( f \) est diagonalisable, déterminer dim \( {\Gamma }_{f} \) .

> 1/a) If \( f \) is diagonalizable, determine dim \( {\Gamma }_{f} \).

b) Si de plus les valeurs propres de \( f \) sont toutes distinctes, montrer que \( {\Gamma }_{f} = \{ P\left( f\right) \mid P \in \; \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> b) If, in addition, the eigenvalues of \( f \) are all distinct, show that \( {\Gamma }_{f} = \{ P\left( f\right) \mid P \in \; \mathbb{K}\left\lbrack X\right\rbrack \} \).

2/ On suppose que le polynôme minimal \( {\Pi }_{f} \) de \( f \) est de degré \( n \) . En utilisant le résultat établi à l’exercice 3 (il existe \( x \in E,{P}_{x} = {\Pi }_{f} \) ), montrer que \( {\Gamma }_{f} = \{ P\left( f\right) , P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> 2/ We assume that the minimal polynomial \( {\Pi }_{f} \) of \( f \) is of degree \( n \). Using the result established in exercise 3 (there exists \( x \in E,{P}_{x} = {\Pi }_{f} \)), show that \( {\Gamma }_{f} = \{ P\left( f\right) , P \in \mathbb{K}\left\lbrack X\right\rbrack \} \).

---

Solution. 1/a) Soient \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) les valeurs propres de \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) les sous-espaces propres correspondants.

> Solution. 1/a) Let \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) be the eigenvalues of \( f,{E}_{{\lambda }_{1}},\ldots ,{E}_{{\lambda }_{r}} \) and the corresponding eigenspaces.

Si \( g \in {\Gamma }_{f} \) , alors pour tout \( i,{E}_{{\lambda }_{i}} \) est stable par \( g \) .

> If \( g \in {\Gamma }_{f} \), then for all \( i,{E}_{{\lambda }_{i}} \) is stable by \( g \).

Réciproquement, si \( {E}_{{\lambda }_{i}} \) est stable par \( g \) pour tout \( i \) , alors :

> Conversely, if \( {E}_{{\lambda }_{i}} \) is stable by \( g \) for all \( i \), then:

\[
\forall x \in  {E}_{{\lambda }_{i}},\;f \circ  g\left( x\right)  = {\lambda }_{i}g\left( x\right)  = g \circ  f\left( x\right) ,
\]

donc comme \( E = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{r}} \) , on a \( g \in {\Gamma }_{f} \) .

> therefore, as \( E = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{r}} \), we have \( g \in {\Gamma }_{f} \).

Donc \( {\Gamma }_{f} = \{ g \in \mathcal{L}\left( E\right) \mid \forall i,{E}_{{\lambda }_{i}} \) est stable par \( g\} \) . Pour tout \( i \) , soit \( {B}_{i} \) une base de \( {E}_{{\lambda }_{i}} \) , de sorte que \( B = {B}_{1} \cup \cdots \cup {B}_{r} \) est une base de \( E \) . Les matrices des endomorphismes de \( {\Gamma }_{f} \) dans la base \( B \) sont celles de la forme

> Thus \( {\Gamma }_{f} = \{ g \in \mathcal{L}\left( E\right) \mid \forall i,{E}_{{\lambda }_{i}} \) is stable under \( g\} \) . For any \( i \) , let \( {B}_{i} \) be a basis of \( {E}_{{\lambda }_{i}} \) , such that \( B = {B}_{1} \cup \cdots \cup {B}_{r} \) is a basis of \( E \) . The matrices of the endomorphisms of \( {\Gamma }_{f} \) in the basis \( B \) are those of the form

\[
\left( \begin{matrix} {M}_{1} & & 0 \\   &  \ddots  & \\  0 & & {M}_{r} \end{matrix}\right) \;\text{ avec }\;\forall i,{M}_{i} \in  {\mathcal{M}}_{\dim {E}_{{\lambda }_{i}}}\left( \mathbb{K}\right) .
\]

On voit donc que \( \dim {\Gamma }_{f} = \mathop{\sum }\limits_{{i = 1}}^{r}{\left( \dim {E}_{{\lambda }_{i}}\right) }^{2} \) .

> We therefore see that \( \dim {\Gamma }_{f} = \mathop{\sum }\limits_{{i = 1}}^{r}{\left( \dim {E}_{{\lambda }_{i}}\right) }^{2} \) .

b) Nous donnons deux méthodes de résolution.

> b) We provide two methods of resolution.

Première méthode. Ici, pour tout \( i \) , on a \( \dim {E}_{{\lambda }_{i}} = 1 \) , donc dim \( {\Gamma }_{f} = \mathop{\sum }\limits_{{i = 1}}^{n}{1}^{2} = n \) . Pour tout \( i \) , \( {\Pi }_{f}\left( {\lambda }_{i}\right) = 0 \) donc \( \left( {X - {\lambda }_{i}}\right) \mid {\Pi }_{f} \) , et comme les \( {\lambda }_{i} \) sont distincts deux à deux, \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) divise \( {\Pi }_{f} \) , donc \( \deg \left( {\Pi }_{f}\right) \geq n \) . Or \( {\Pi }_{f} \) divise le polynôme caractéristique de \( f \) , donc \( \deg \left( {\Pi }_{f}\right) \leq n \) . On en déduit deg \( {\Pi }_{f} = n \) .

> First method. Here, for any \( i \) , we have \( \dim {E}_{{\lambda }_{i}} = 1 \) , so dim \( {\Gamma }_{f} = \mathop{\sum }\limits_{{i = 1}}^{n}{1}^{2} = n \) . For any \( i \) , \( {\Pi }_{f}\left( {\lambda }_{i}\right) = 0 \) so \( \left( {X - {\lambda }_{i}}\right) \mid {\Pi }_{f} \) , and since the \( {\lambda }_{i} \) are pairwise distinct, \( \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) divides \( {\Pi }_{f} \) , so \( \deg \left( {\Pi }_{f}\right) \geq n \) . However, \( {\Pi }_{f} \) divides the characteristic polynomial of \( f \) , so \( \deg \left( {\Pi }_{f}\right) \leq n \) . We deduce deg \( {\Pi }_{f} = n \) .

Soit \( C = \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . L’application

> Let \( C = \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . The map

\[
\varphi  : \mathbb{K}\left\lbrack  X\right\rbrack   \rightarrow  C\;P \mapsto  P\left( f\right)
\]

est linéaire surjective, donc \( C \) est isomorphe comme \( \mathbb{K} \) -e.v à \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {\Pi }_{f}\right) \) , donc \( \dim C = \deg \left( {\Pi }_{f}\right) = n \) . Or \( C \subset {\Gamma }_{f} \) et \( \dim {\Gamma }_{f} = n \) , donc \( C = {\Gamma }_{f} \) .

> is a surjective linear map, so \( C \) is isomorphic as a \( \mathbb{K} \) -v.s. to \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {\Pi }_{f}\right) \) , so \( \dim C = \deg \left( {\Pi }_{f}\right) = n \) . However, \( C \subset {\Gamma }_{f} \) and \( \dim {\Gamma }_{f} = n \) , so \( C = {\Gamma }_{f} \) .

---

Seconde méthode. Pour tout \( i \) , \( \dim {E}_{{\lambda }_{i}} = 1 \) donc il existe \( {x}_{i} \in E \) tel que \( {E}_{{\lambda }_{i}} = \operatorname{Vect}\left( {x}_{i}\right) \) . Soit \( g \in {\Gamma }_{f} \) . Pour tout \( i,{E}_{{\lambda }_{i}} \) est stable par \( g \in {\Gamma }_{f} \) , donc il existe \( {\mu }_{i} \in \mathbb{K} \) tel que \( g\left( {x}_{i}\right) = {\mu }_{i}{x}_{i} \) (au passage, on remarque que, \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) étant une base de \( E, g \) est diagonalisable). La théorie des polynômes d'interpolation de Lagrange (voir le chapitre II page 65) nous assure l'existence d'un polynôme \( P \) tel que \( P\left( {\lambda }_{i}\right) = {\mu }_{i} \) pour tout \( i \) . Ainsi,

> Second method. For all \( i \) , \( \dim {E}_{{\lambda }_{i}} = 1 \) so there exists \( {x}_{i} \in E \) such that \( {E}_{{\lambda }_{i}} = \operatorname{Vect}\left( {x}_{i}\right) \) . Let \( g \in {\Gamma }_{f} \) . For all \( i,{E}_{{\lambda }_{i}} \) is stable by \( g \in {\Gamma }_{f} \) , so there exists \( {\mu }_{i} \in \mathbb{K} \) such that \( g\left( {x}_{i}\right) = {\mu }_{i}{x}_{i} \) (incidentally, we note that, \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) being a basis of \( E, g \) is diagonalizable). The theory of Lagrange interpolation polynomials (see chapter II page 65) ensures the existence of a polynomial \( P \) such that \( P\left( {\lambda }_{i}\right) = {\mu }_{i} \) for all \( i \) . Thus,

\[
\forall i \in  \{ 1,\ldots , n\} ,\;P\left( f\right) \left( {x}_{i}\right)  = P\left( {\lambda }_{i}\right) {x}_{i} = {\mu }_{i}{x}_{i} = g\left( {x}_{i}\right)
\]

et comme \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est une base de \( E, P\left( f\right) = g \) . Donc \( {\Gamma }_{f} \subset \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . L’inclusion réciproque étant immédiate, on en déduit le résultat demandé.

> and since \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is a basis of \( E, P\left( f\right) = g \) . Therefore \( {\Gamma }_{f} \subset \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . The reverse inclusion being immediate, we deduce the requested result.

2/ On utilise les notations de l'exercice 3. D'après la question 3/b) de l'exercice 3, il existe \( x \in E \) tel que \( {P}_{x} = {\Pi }_{f} \) , donc \( \deg \left( {P}_{x}\right) = n \) et d’après la question 1/b) du même exercice, \( \dim {E}_{x} = \deg \left( {P}_{x}\right) = n \) donc \( {E}_{x} = E. \)

> 2/ We use the notation from exercise 3. According to question 3/b) of exercise 3, there exists \( x \in E \) such that \( {P}_{x} = {\Pi }_{f} \) , so \( \deg \left( {P}_{x}\right) = n \) and according to question 1/b) of the same exercise, \( \dim {E}_{x} = \deg \left( {P}_{x}\right) = n \) so \( {E}_{x} = E. \)

Soit \( g \in {\Gamma }_{f} \) . Comme \( {E}_{x} = E \) , il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( g\left( x\right) = P\left( f\right) \left( x\right) \) . Or pour tout \( y = Q\left( f\right) \left( x\right) \in {E}_{x}, \)

> Let \( g \in {\Gamma }_{f} \) . Since \( {E}_{x} = E \) , there exist \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( g\left( x\right) = P\left( f\right) \left( x\right) \) . Now for all \( y = Q\left( f\right) \left( x\right) \in {E}_{x}, \)

\[
g\left( y\right)  = g \circ  Q\left( f\right) \left( x\right)  = Q\left( f\right)  \circ  g\left( x\right)  = Q\left( f\right)  \circ  P\left( f\right) \left( x\right)  = P\left( f\right)  \circ  Q\left( f\right) \left( x\right)  = P\left( f\right) \left( y\right) .
\]

Les endomorphismes \( g \) et \( P\left( f\right) \) prennent donc la même valeur sur \( {E}_{x} \) . Or \( {E}_{x} = E \) , donc \( g = P\left( f\right) \) . On a donc montré que \( {\Gamma }_{f} \subset \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . L’inclusion réciproque est évidente, d’où l'égalité.

> The endomorphisms \( g \) and \( P\left( f\right) \) therefore take the same value on \( {E}_{x} \) . Now \( {E}_{x} = E \) , so \( g = P\left( f\right) \) . We have thus shown that \( {\Gamma }_{f} \subset \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) . The reverse inclusion is obvious, hence the equality.

Remarque. On aurait pu montrer 1/b), en utilisant \( 2/ \) car on avait montré que \( \deg \left( {\Pi }_{f}\right) = \; n \) dans la première méthode.

> Remark. We could have shown 1/b), using \( 2/ \) because we had shown that \( \deg \left( {\Pi }_{f}\right) = \; n \) in the first method.

- La réciproque de la question \( 2/ \) est vraie : si \( {\Gamma }_{f} = \{ P\left( f\right)  \mid  P \in  \mathbb{K}\left\lbrack  X\right\rbrack  \} \) , alors \( \deg \left( {\Pi }_{f}\right)  = n \) , mais la démonstration est plus difficile (voir la dernière application de la théorie des invariants de similitude dans l'annexe B page 400).

> - The converse of question \( 2/ \) is true: if \( {\Gamma }_{f} = \{ P\left( f\right)  \mid  P \in  \mathbb{K}\left\lbrack  X\right\rbrack  \} \) , then \( \deg \left( {\Pi }_{f}\right)  = n \) , but the proof is more difficult (see the last application of the theory of similarity invariants in appendix B page 400).
