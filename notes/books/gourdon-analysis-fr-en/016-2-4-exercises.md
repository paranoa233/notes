#### 2.4. Exercises

*Français : 2.4. Exercices*

\( \rightarrow \) EXERCICE 1. Soit \( X \) un ensemble. On note \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) le \( \mathbb{R} \) -e.v des fonctions bornées de \( X \) dans \( \mathbb{R} \) . On norme \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) en posant

> \( \rightarrow \) EXERCISE 1. Let \( X \) be a set. Let \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) denote the \( \mathbb{R} \) -v.s. of bounded functions from \( X \) to \( \mathbb{R} \) . We norm \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) by setting

\[
\forall f \in  \mathcal{B}\left( {X,\mathbb{R}}\right) ,\;\parallel f\parallel  = \mathop{\sup }\limits_{{x \in  X}}\left| {f\left( x\right) }\right| .
\]

Muni de cette norme, montrer que \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) est un espace de Banach.

> Equipped with this norm, show that \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) is a Banach space.

Solution. Rappelons qu'un espace de Banach est un e.v.n complet. La preuve de la complétude d'un espace métrique est hyper-classique. On procède comme suit :

> Solution. Recall that a Banach space is a complete n.v.s. The proof of the completeness of a metric space is highly classic. We proceed as follows:

(i) On considère une suite de Cauchy, et on construit sa limite éventuelle,

> (i) We consider a Cauchy sequence and construct its potential limit,

(ii) on vérifie qu'elle appartient à l'ensemble de départ,

> (ii) we verify that it belongs to the original set,

(iii) on montre que la suite de Cauchy converge bien vers cette limite éventuelle.

> (iii) we show that the Cauchy sequence indeed converges to this potential limit.

(i) Soit \( \left( {f}_{n}\right) \) une suite de Cauchy de \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) . Fixons \( x \in X \) . Pour tous \( p, q \in \mathbb{N} \) , l’inégalité \( \left| {{f}_{p}\left( x\right) - {f}_{q}\left( x\right) }\right| \leq \begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \) implique que la suite \( \left( {{f}_{n}\left( x\right) }\right) \) est de Cauchy dans \( \mathbb{R} \) . Comme \( \mathbb{R} \) est complet, \( \left( {{f}_{p}\left( x\right) }\right) \) converge. Notons \( f\left( x\right) \) sa limite.

> (i) Let \( \left( {f}_{n}\right) \) be a Cauchy sequence in \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) . Let us fix \( x \in X \) . For all \( p, q \in \mathbb{N} \) , the inequality \( \left| {{f}_{p}\left( x\right) - {f}_{q}\left( x\right) }\right| \leq \begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \) implies that the sequence \( \left( {{f}_{n}\left( x\right) }\right) \) is Cauchy in \( \mathbb{R} \) . Since \( \mathbb{R} \) is complete, \( \left( {{f}_{p}\left( x\right) }\right) \) converges. Let us denote its limit by \( f\left( x\right) \) .

(ii) L’application \( f : X \rightarrow \mathbb{R} \) ainsi construite vérifie \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n}\left( x\right) \) pour tout \( x \in X \) . Montrons que \( f \) est bornée. La suite \( \left( {f}_{n}\right) \) étant de Cauchy, elle est bornée. Ainsi, il existe \( M > 0 \) tel que \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) pour tout \( n \) . Si \( x \in X \) , on a donc \( \left| {{f}_{n}\left( x\right) }\right| \leq M \) pour tout \( n \) , donc en passant à la limite \( \left| {f\left( x\right) }\right| \leq M \) . Ceci étant vrai pour tout \( x, f \) est bien bornée, i. \( e.f \in \mathcal{B}\left( {X,\mathbb{R}}\right) \) .

> (ii) The mapping \( f : X \rightarrow \mathbb{R} \) thus constructed satisfies \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n}\left( x\right) \) for all \( x \in X \) . Let us show that \( f \) is bounded. Since the sequence \( \left( {f}_{n}\right) \) is Cauchy, it is bounded. Thus, there exists \( M > 0 \) such that \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) for all \( n \) . If \( x \in X \) , we therefore have \( \left| {{f}_{n}\left( x\right) }\right| \leq M \) for all \( n \) , so by passing to the limit \( \left| {f\left( x\right) }\right| \leq M \) . Since this is true for all \( x, f \) is indeed bounded, i.e., \( e.f \in \mathcal{B}\left( {X,\mathbb{R}}\right) \) .

(iii) Montrons maintenant que \( \left( {f}_{n}\right) \) tend vers \( f \) dans \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) . Soit \( \varepsilon > 0 \) . Il existe \( N > 0 \) tel que pour tout \( p, q \geq N,\begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \leq \varepsilon \) . Ainsi, si on fixe un élément \( x \) quelconque de \( X \) , on a

> (iii) Let us now show that \( \left( {f}_{n}\right) \) tends to \( f \) in \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) . Let \( \varepsilon > 0 \) . There exists \( N > 0 \) such that for all \( p, q \geq N,\begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \leq \varepsilon \) . Thus, if we fix any element \( x \) of \( X \) , we have

\[
\forall p \geq  N,\forall q \geq  N,\;\left| {{f}_{p}\left( x\right)  - {f}_{q}\left( x\right) }\right|  \leq  \begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} < \varepsilon .
\]

En fixant \( p \) dans l’assertion précédente et en faisant tendre \( q \) vers l’infini, on en déduit l’inégalité \( \left| {{f}_{p}\left( x\right) - f\left( x\right) }\right| \leq \varepsilon \) . Ceci étant vrai pour tout \( x \in X \) , on a \( \begin{Vmatrix}{{f}_{p} - f}\end{Vmatrix} \leq \varepsilon \) . Ceci est vrai pour tout \( p \geq N \) , donc \( \left( {f}_{p}\right) \) converge vers \( f \) .

> By fixing \( p \) in the previous assertion and letting \( q \) tend to infinity, we deduce the inequality \( \left| {{f}_{p}\left( x\right) - f\left( x\right) }\right| \leq \varepsilon \) . Since this is true for all \( x \in X \) , we have \( \begin{Vmatrix}{{f}_{p} - f}\end{Vmatrix} \leq \varepsilon \) . This is true for all \( p \geq N \) , therefore \( \left( {f}_{p}\right) \) converges to \( f \) .

Finalement, toute suite de Cauchy \( \left( {f}_{n}\right) \) de \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) converge, donc \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) est complet.

> Finally, every Cauchy sequence \( \left( {f}_{n}\right) \) in \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) converges, therefore \( \mathcal{B}\left( {X,\mathbb{R}}\right) \) is complete.

EXERCICE 2. On munit l’espace \( \rbrack 0, + \infty \left\lbrack \right. \) de la distance \( \delta \left( {x, y}\right) = \left| {\frac{1}{x} - \frac{1}{y}}\right| \) .

> EXERCISE 2. We equip the space \( \rbrack 0, + \infty \left\lbrack \right. \) with the distance \( \delta \left( {x, y}\right) = \left| {\frac{1}{x} - \frac{1}{y}}\right| \) .

a) Montrer que \( \delta \) est bien une distance sur \( \rbrack 0, + \infty \lbrack \) .

> a) Show that \( \delta \) is indeed a distance on \( \rbrack 0, + \infty \lbrack \) .

b) Montrer que cette distance définit sur \( \rbrack 0, + \infty \lbrack \) la même topologie que la topologie usuelle.

> b) Show that this distance defines the same topology on \( \rbrack 0, + \infty \lbrack \) as the usual topology.

c) Montrer que l’espace métrique ( ]0,+∞[ \( ,\delta \) ) n’est pas complet.

> c) Show that the metric space ( ]0,+∞[ \( ,\delta \) ) is not complete.

d) On restreint la distance \( \delta \) à l’espace \( \rbrack 0,1\rbrack \) . Montrer que ( \( \rbrack 0,1\rbrack ,\delta \) ) est complet.

> d) We restrict the distance \( \delta \) to the space \( \rbrack 0,1\rbrack \) . Show that ( \( \rbrack 0,1\rbrack ,\delta \) ) is complete.

Solution. a) C'est bien une distance car :

> Solution. a) It is indeed a distance because:

(i) \( \delta \left( {x, y}\right) = 0 \) si et seulement si \( 1/x = 1/y \) , i.e. \( x = y \) .

> (i) \( \delta \left( {x, y}\right) = 0 \) if and only if \( 1/x = 1/y \) , i.e. \( x = y \) .

(ii) \( \forall \left( {x, y}\right) \in \rbrack 0, + \infty \left\lbrack {{}^{2},\delta \left( {x, y}\right) = \delta \left( {y, x}\right) }\right. \) .

> (ii) \( \forall \left( {x, y}\right) \in \rbrack 0, + \infty \left\lbrack {{}^{2},\delta \left( {x, y}\right) = \delta \left( {y, x}\right) }\right. \) .

(iii) \( \forall \left( {x, y, z}\right) \in \rbrack 0, + \infty {\lbrack }^{3} \) ,

> (iii) \( \forall \left( {x, y, z}\right) \in \rbrack 0, + \infty {\lbrack }^{3} \) ,

\[
\delta \left( {x, z}\right)  = \left| {\frac{1}{x} - \frac{1}{z}}\right|  \leq  \left| {\frac{1}{x} - \frac{1}{y}}\right|  + \left| {\frac{1}{y} - \frac{1}{z}}\right|  = \delta \left( {x, y}\right)  + \delta \left( {y, z}\right) .
\]

b) Notons d la distance usuelle sur les nombres réels \( \left( {\mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| }\right) \) . Rappelons le fait suivant : dire que les deux espaces métriques ( ]0,+∞ [, \( \delta \) ) et ( ]0,+∞ [, d) définissent la même topologie, c'est dire qu'ils ont les mêmes ouverts. La proposition 10 de la page 12 affirme que ceci équivaut au fait que l’application identité \( {\operatorname{Id}}_{\rbrack 0, + \infty \lbrack } : \left( {\rbrack 0, + \infty \lbrack ,\mathrm{d}}\right) \rightarrow \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) est un homéomorphisme. Pour prouver ce dernier point, nous allons utiliser le fait que cette application est la composée de

> b) Let d denote the usual distance on the real numbers \( \left( {\mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| }\right) \) . Recall the following fact: saying that the two metric spaces ( ]0,+∞ [, \( \delta \) ) and ( ]0,+∞ [, d) define the same topology means they have the same open sets. Proposition 10 on page 12 states that this is equivalent to the fact that the identity map \( {\operatorname{Id}}_{\rbrack 0, + \infty \lbrack } : \left( {\rbrack 0, + \infty \lbrack ,\mathrm{d}}\right) \rightarrow \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) is a homeomorphism. To prove this last point, we will use the fact that this map is the composition of

\[
\varphi  : \left( {\rbrack 0, + \infty \lbrack ,\mathrm{d}}\right)  \rightarrow  \left( {\rbrack 0, + \infty \lbrack ,\mathrm{d}}\right) \;x \mapsto  \frac{1}{x}\;\text{ et }\;\psi  : \left( {\rbrack 0, + \infty \lbrack ,\mathrm{d}}\right)  \rightarrow  \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \;x \mapsto  \frac{1}{x},
\]

et que \( \varphi \) et \( \psi \) sont des homéomorphismes.

> and that \( \varphi \) and \( \psi \) are homeomorphisms.

L'application \( \varphi \) est continue (c’est classique puisque d est la distance usuelle), elle est bijective, et \( {\varphi }^{-1} = \varphi \) est aussi continue. On a donc bien affaire à un homéomorphisme.

> The map \( \varphi \) is continuous (this is standard since d is the usual distance), it is bijective, and \( {\varphi }^{-1} = \varphi \) is also continuous. We are therefore dealing with a homeomorphism.

L’application \( \psi \) vérifie

> The map \( \psi \) satisfies

\[
\forall \left( {x, y}\right)  \in  \rbrack 0, + \infty {\lbrack }^{2},\;\delta \left( {\psi \left( x\right) ,\psi \left( y\right) }\right)  = \left| {\frac{1}{\psi \left( x\right) } - \frac{1}{\psi \left( y\right) }}\right|  = \left| {x - y}\right|  = \mathrm{d}\left( {x, y}\right) ,
\]

c'est donc une isométrie, donc un homéomorphisme. D'où le résultat.

> it is therefore an isometry, and thus a homeomorphism. Hence the result.

Remarque. On aurait pu également prouver le résultat "à la main", en montrant qu'un ouvert de \( \left( {\rbrack 0, + \infty \lbrack \text{ , d }}\right) \) est un ouvert de \( \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) et réciproquement.

> Remark. We could also have proven the result "by hand," by showing that an open set of \( \left( {\rbrack 0, + \infty \lbrack \text{ , d }}\right) \) is an open set of \( \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) and vice versa.

c) Dans ( \( \rbrack 0, + \infty \lbrack ,\delta ) \) , la suite \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) définie par \( {u}_{n} = n \) est de Cauchy car \( \delta \left( {{u}_{p},{u}_{q}}\right) = \mid 1/p - \; 1/q \mid \) tend vers 0 lorsque \( p \) et \( q \) tendent vers \( + \infty \) . Il est clair que cette suite ne converge pas dans ( \( \rbrack 0, + \infty \lbrack \) , d) (elle n’est pas bornée), donc elle ne converge pas dans ( \( \rbrack 0, + \infty \lbrack ,\delta ) \) puisque ces deux espaces métriques définissent la même topologie (la notion de convergence est topologique). Ainsi, \( \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) n’est pas complet.

> c) In ( \( \rbrack 0, + \infty \lbrack ,\delta ) \) , the sequence \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) defined by \( {u}_{n} = n \) is Cauchy because \( \delta \left( {{u}_{p},{u}_{q}}\right) = \mid 1/p - \; 1/q \mid \) tends to 0 as \( p \) and \( q \) tend to \( + \infty \) . It is clear that this sequence does not converge in ( \( \rbrack 0, + \infty \lbrack \) , d) (it is not bounded), so it does not converge in ( \( \rbrack 0, + \infty \lbrack ,\delta ) \) since these two metric spaces define the same topology (the notion of convergence is topological). Thus, \( \left( {\rbrack 0, + \infty \lbrack ,\delta }\right) \) is not complete.

d) On applique la méthode utilisée dans la solution de l'exercice précédent pour prouver la complétude souhaitée. Considérons une suite \( \left. {\left( {u}_{n}\right) \text{ de Cauchy dans }(\rbrack 0,1\rbrack ,\delta }\right) \) . Pour tout \( p, q \) , on

> d) We apply the method used in the solution of the previous exercise to prove the desired completeness. Consider a sequence \( \left. {\left( {u}_{n}\right) \text{ de Cauchy dans }(\rbrack 0,1\rbrack ,\delta }\right) \) . For all \( p, q \) , we

a

\[
\delta \left( {{u}_{p},{u}_{q}}\right)  = \left| {\frac{1}{{u}_{p}} - \frac{1}{{u}_{q}}}\right|  = \left| \frac{{u}_{p} - {u}_{q}}{{u}_{p}{u}_{q}}\right|  \geq  \left| {{u}_{p} - {u}_{q}}\right| ,
\]

ce qui montre que \( \left( {u}_{n}\right) \) est de Cauchy dans \( \left( {\mathbb{R},\mathrm{d}}\right) \) . Ce dernier étant complet, \( \left( {u}_{n}\right) \) converge dans \( \left( {\mathbb{R},\mathrm{d}}\right) \) . Soit \( u \) sa limite dans cet espace métrique.

> which shows that \( \left( {u}_{n}\right) \) is Cauchy in \( \left( {\mathbb{R},\mathrm{d}}\right) \) . The latter being complete, \( \left( {u}_{n}\right) \) converges in \( \left( {\mathbb{R},\mathrm{d}}\right) \) . Let \( u \) be its limit in this metric space.

La limite \( u \) est forcément dans l’adhérence de \( \rbrack 0,1\rbrack \) dans \( \left( {\mathbb{R},\mathrm{d}}\right) \) , qui est \( \left\lbrack {0,1}\right\rbrack \) . Si \( u = 0 \) , alors \( \left. {\delta \left( {1,{u}_{n}}\right) = \left| {1 - 1/{u}_{n}}\right| \text{ tend vers } + \infty \text{ , donc la suite }\left( {u}_{n}\right) \text{ n’est pas bornée dans }(\rbrack 0,1\rbrack ,\delta }\right) \) , ce qui est impossible car c’est une suite de Cauchy de cet espace. Ainsi, \( u \neq 0 \) , donc \( u \in \rbrack 0,1\rbrack \) . Comme \( \left( {\rbrack 0,1\rbrack ,\mathrm{d}}\right) \) et \( \left( {\rbrack 0,1\rbrack ,\delta }\right) \) possèdent la même topologie (c’est la topologie induite par \( (\rbrack 0, + \infty \lbrack ,\mathrm{d}) \) ou (]0,+∞[, \( \delta \) ) — qui possèdent la même topologie — sur ]0,1]), on en déduit que \( \left( {u}_{n}\right) \) converge vers \( u \) dans \( \left( {\rbrack 0,1\rbrack ,\delta }\right) \) .

> The limit \( u \) is necessarily in the closure of \( \rbrack 0,1\rbrack \) in \( \left( {\mathbb{R},\mathrm{d}}\right) \) , which is \( \left\lbrack {0,1}\right\rbrack \) . If \( u = 0 \) , then \( \left. {\delta \left( {1,{u}_{n}}\right) = \left| {1 - 1/{u}_{n}}\right| \text{ tend vers } + \infty \text{ , donc la suite }\left( {u}_{n}\right) \text{ n’est pas bornée dans }(\rbrack 0,1\rbrack ,\delta }\right) \) , which is impossible as it is a Cauchy sequence of this space. Thus, \( u \neq 0 \) , so \( u \in \rbrack 0,1\rbrack \) . Since \( \left( {\rbrack 0,1\rbrack ,\mathrm{d}}\right) \) and \( \left( {\rbrack 0,1\rbrack ,\delta }\right) \) possess the same topology (it is the topology induced by \( (\rbrack 0, + \infty \lbrack ,\mathrm{d}) \) or (]0,+∞[, \( \delta \) ) — which possess the same topology — on ]0,1]), we deduce that \( \left( {u}_{n}\right) \) converges to \( u \) in \( \left( {\rbrack 0,1\rbrack ,\delta }\right) \) .

On a prouvé que toute suite de Cauchy de ( ]0,1 ], \( \delta \) ) converge, donc ( ]0,1 ], \( \delta \) ) est complet.

> We have proven that every Cauchy sequence in ( ]0,1 ], \( \delta \) ) converges, therefore ( ]0,1 ], \( \delta \) ) is complete.

EXERCICE 3 (DEUX RÉSULTATS DE POINT FIXE). 1 / Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique complet et une application \( f : E \rightarrow E \) . On suppose l’existence d’un entier naturel non nul \( r \) tel que l’application \( {f}^{r} \) (composée \( r \) fois de \( f \) ) est \( k \) -contractante \( \left( {0 < k < 1}\right) \) . Montrer que \( f \) admet un unique point fixe.

> EXERCISE 3 (TWO FIXED-POINT RESULTS). 1 / Let \( \left( {E,\mathrm{\;d}}\right) \) be a complete metric space and \( f : E \rightarrow E \) a mapping. Suppose there exists a non-zero natural number \( r \) such that the mapping \( {f}^{r} \) (the composition of \( f \) \( r \) times) is \( k \) -contractive \( \left( {0 < k < 1}\right) \) . Show that \( f \) has a unique fixed point.

2/ (Point fixe à paramètre). Soient \( \left( {X,\delta }\right) \) et \( \left( {E,\mathrm{\;d}}\right) \) deux espaces métriques, \( \left( {E,\mathrm{\;d}}\right) \) étant complet. On considère une application

> 2/ (Fixed point with parameter). Let \( \left( {X,\delta }\right) \) and \( \left( {E,\mathrm{\;d}}\right) \) be two metric spaces, with \( \left( {E,\mathrm{\;d}}\right) \) being complete. Consider a mapping

\[
F : X \times  E \rightarrow  E\;\left( {\lambda , x}\right)  \mapsto  F\left( {\lambda , x}\right) ,
\]

continue, et \( k \) -contractante en la seconde variable, i. \( e \) .

> continuous, and \( k \) -contractive in the second variable, i.e., \( e \) .

\[
\exists k \in  \rbrack 0,1\lbrack ,\forall \lambda  \in  X,\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {F\left( {\lambda , x}\right) , F\left( {\lambda , y}\right) }\right)  \leq  k\mathrm{\;d}\left( {x, y}\right) .
\]

Montrer que pour tout \( \lambda \in X \) , l’application \( F\left( {\lambda , \cdot }\right) : x \mapsto F\left( {\lambda , x}\right) \) admet un unique point fixe, que l’on note \( {x}_{\lambda } \) . Montrer ensuite que l’application \( X \rightarrow E\;\lambda \mapsto {x}_{\lambda } \) est continue.

> Show that for all \( \lambda \in X \) , the mapping \( F\left( {\lambda , \cdot }\right) : x \mapsto F\left( {\lambda , x}\right) \) has a unique fixed point, denoted by \( {x}_{\lambda } \) . Then show that the mapping \( X \rightarrow E\;\lambda \mapsto {x}_{\lambda } \) is continuous.

Solution. 1 / Comme \( E \) est complet et que \( {f}^{r} : E \rightarrow E \) est \( k \) -contractante, \( {f}^{r} \) a un unique point fixe \( x \in E \) (voir le théorème du point fixe). De l’égalité \( {f}^{r}\left( x\right) = x \) on tire \( f\left( {{f}^{r}\left( x\right) }\right) = f\left( x\right) = \; {f}^{r}\left( {f\left( x\right) }\right) \) , ce qui montre que \( f\left( x\right) \) est un point fixe de \( {f}^{r} \) . Comme \( x \) est l’unique point fixe de \( {f}^{r} \) , on a forcément \( f\left( x\right) = x \) .

> Solution. 1 / Since \( E \) is complete and \( {f}^{r} : E \rightarrow E \) is \( k \) -contractive, \( {f}^{r} \) has a unique fixed point \( x \in E \) (see the fixed-point theorem). From the equality \( {f}^{r}\left( x\right) = x \) we derive \( f\left( {{f}^{r}\left( x\right) }\right) = f\left( x\right) = \; {f}^{r}\left( {f\left( x\right) }\right) \) , which shows that \( f\left( x\right) \) is a fixed point of \( {f}^{r} \) . Since \( x \) is the unique fixed point of \( {f}^{r} \) , we necessarily have \( f\left( x\right) = x \) .

Maintenant, \( x \) est le seul point fixe de \( f \) car l’égalité \( f\left( y\right) = y \) entraîne \( {f}^{r}\left( y\right) = y \) donc \( y = x \) car \( x \) est le seul point fixe de \( {f}^{r} \) .

> Now, \( x \) is the only fixed point of \( f \) because the equality \( f\left( y\right) = y \) implies \( {f}^{r}\left( y\right) = y \) , therefore \( y = x \) because \( x \) is the only fixed point of \( {f}^{r} \) .

2/ Pour tout \( \lambda \in X \) , l’application \( F\left( {\lambda , \cdot }\right) : E \rightarrow E \) est \( k \) -contractante, donc admet un unique point fixe \( {x}_{\lambda } \) car \( E \) est complet.

> 2/ For all \( \lambda \in X \) , the mapping \( F\left( {\lambda , \cdot }\right) : E \rightarrow E \) is \( k \) -contractive, and therefore has a unique fixed point \( {x}_{\lambda } \) because \( E \) is complete.

Montrons que l’application \( \lambda \mapsto {x}_{\lambda } \) est continue. Si \( \lambda ,{\lambda }^{\prime } \in X \) , on a

> Let us show that the mapping \( \lambda \mapsto {x}_{\lambda } \) is continuous. If \( \lambda ,{\lambda }^{\prime } \in X \) , we have

\[
\mathrm{d}\left( {{x}_{\lambda },{x}_{{\lambda }^{\prime }}}\right)  = \mathrm{d}\left( {F\left( {\lambda ,{x}_{\lambda }}\right) , F\left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) }\right)  \leq  \mathrm{d}\left( {F\left( {\lambda ,{x}_{\lambda }}\right) , F\left( {\lambda ,{x}_{{\lambda }^{\prime }}}\right) }\right)  + \mathrm{d}\left( {F\left( {\lambda ,{x}_{{\lambda }^{\prime }}}\right) , F\left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) }\right)
\]

\[
\leq  k\mathrm{\;d}\left( {{x}_{\lambda },{x}_{{\lambda }^{\prime }}}\right)  + \mathrm{d}\left( {F\left( {\lambda ,{x}_{{\lambda }^{\prime }}}\right) , F\left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) }\right)
\]

donc

> therefore

\[
\mathrm{d}\left( {{x}_{\lambda },{x}_{{\lambda }^{\prime }}}\right)  \leq  \frac{1}{1 - k}\mathrm{\;d}\left( {F\left( {\lambda ,{x}_{{\lambda }^{\prime }}}\right) , F\left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) }\right) .
\]

La continuité de \( F \) au point \( \left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) \) permet maintenant d’affirmer \( \mathop{\lim }\limits_{{\lambda \rightarrow {\lambda }^{\prime }}}{x}_{\lambda } = {x}_{{\lambda }^{\prime }} \) , d’où le résultat.

> The continuity of \( F \) at point \( \left( {{\lambda }^{\prime },{x}_{{\lambda }^{\prime }}}\right) \) now allows us to assert \( \mathop{\lim }\limits_{{\lambda \rightarrow {\lambda }^{\prime }}}{x}_{\lambda } = {x}_{{\lambda }^{\prime }} \) , hence the result.

EXERCICE 4 (DEUX RÉSULTATS DE PROLONGEMENT). Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux es-paces métriques, \( A \) une partie de \( E \) dense dans \( E \) . a) Si une application \( f : \left( {A,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) est continue et si

> EXERCISE 4 (TWO EXTENSION RESULTS). Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces, \( A \) a subset of \( E \) dense in \( E \) . a) If a mapping \( f : \left( {A,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) is continuous and if

\[
\forall x \in  E \smallsetminus  A,\;\mathop{\lim }\limits_{\substack{{y \rightarrow  x} \\  {y \in  A} }}f\left( y\right) \;\text{ existe, }
\]

montrer qu’il existe une unique fonction \( g : E \rightarrow F \) , continue, telle que la restriction \( {g}_{\mid A} \) de \( g \) à \( A \) soit égale à \( f \) .

> show that there exists a unique continuous function \( g : E \rightarrow F \) such that the restriction \( {g}_{\mid A} \) of \( g \) to \( A \) is equal to \( f \) .

b) On suppose cette fois ci que \( \left( {F,\delta }\right) \) est complet. Soit \( f : \left( {A,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) une application uniformément continue. Montrer l’existence d’une unique fonction \( g : E \rightarrow F \) uniformément continue, telle que \( {g}_{\mid A} = f \) .

> b) Suppose this time that \( \left( {F,\delta }\right) \) is complete. Let \( f : \left( {A,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) be a uniformly continuous mapping. Show the existence of a unique uniformly continuous function \( g : E \rightarrow F \) such that \( {g}_{\mid A} = f \) .

Solution. a) Définissons \( g : E \rightarrow F \) de la manière suivante :

> Solution. a) Let us define \( g : E \rightarrow F \) as follows:

\[
\forall x \in  A,\;g\left( x\right)  = f\left( x\right) \;\text{ et }\;\forall x \in  E \smallsetminus  A,\;g\left( x\right)  = \mathop{\lim }\limits_{\substack{{y \rightarrow  x} \\  {y \in  A} }}f\left( y\right) .
\]

Montrons que \( g \) est continue sur \( E \) . Soit \( x \in E \) et \( {\left( {x}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) une suite de points de \( E \) tendant vers \( x \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , on a \( \mathop{\lim }\limits_{\substack{{y \rightarrow {x}_{n}} \\ {y \in A} }}f\left( y\right) = g\left( {x}_{n}\right) \) . On en déduit facilement

> Let us show that \( g \) is continuous on \( E \) . Let \( x \in E \) and \( {\left( {x}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be a sequence of points in \( E \) converging to \( x \) . For all \( n \in {\mathbb{N}}^{ * } \) , we have \( \mathop{\lim }\limits_{\substack{{y \rightarrow {x}_{n}} \\ {y \in A} }}f\left( y\right) = g\left( {x}_{n}\right) \) . We easily deduce

\[
\left( {\forall n \in  {\mathbb{N}}^{ * },\exists {y}_{n} \in  A}\right) ,\;\mathrm{d}\left( {{x}_{n},{y}_{n}}\right)  \leq  \frac{1}{n}\;\text{ et }\;\delta \left( {g\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right)  < \frac{1}{n}.
\]

La relation \( \mathrm{d}\left( {x,{y}_{n}}\right) \leq \mathrm{d}\left( {x,{x}_{n}}\right) + \mathrm{d}\left( {{x}_{n},{y}_{n}}\right) \leq \frac{1}{n} + \mathrm{d}\left( {x,{x}_{n}}\right) \) montre que

> The relation \( \mathrm{d}\left( {x,{y}_{n}}\right) \leq \mathrm{d}\left( {x,{x}_{n}}\right) + \mathrm{d}\left( {{x}_{n},{y}_{n}}\right) \leq \frac{1}{n} + \mathrm{d}\left( {x,{x}_{n}}\right) \) shows that

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{y}_{n} = x,\;\text{ et donc }\;\mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {y}_{n}\right)  = g\left( x\right) .
\]

(*)

> Maintenant, les inégalités

Now, the inequalities

\[
\delta \left( {g\left( {x}_{n}\right) , g\left( x\right) }\right)  \leq  \delta \left( {g\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right)  + \delta \left( {f\left( {y}_{n}\right) , g\left( x\right) }\right)  \leq  \frac{1}{n} + \delta \left( {f\left( {y}_{n}\right) , g\left( x\right) }\right)
\]

montrent avec (*) que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}g\left( {x}_{n}\right) = g\left( x\right) \) . Ceci étant vrai pour tout suite \( \left( {x}_{n}\right) \) de \( E \) tendant vers \( x \) , on en conclut que \( g \) est continue en \( x \) , et ceci pour tout \( x \in E \) .

> show with (*) that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}g\left( {x}_{n}\right) = g\left( x\right) \) . Since this is true for any sequence \( \left( {x}_{n}\right) \) of \( E \) converging to \( x \) , we conclude that \( g \) is continuous at \( x \) , and this for all \( x \in E \) .

Unicité. Soient \( g \) et \( h : E \rightarrow F \) deux applications continues telles que \( {g}_{\mid A} = {h}_{\mid A} \) .

> Uniqueness. Let \( g \) and \( h : E \rightarrow F \) be two continuous mappings such that \( {g}_{\mid A} = {h}_{\mid A} \) .

- Par hypothèse, \( g\left( x\right)  = h\left( x\right) \) pour tout \( x \in  A \) .

> - By hypothesis, \( g\left( x\right)  = h\left( x\right) \) for all \( x \in  A \) .

- Soit \( x \in  E \smallsetminus  A \) . Comme \( A \) est dense dans \( E \) , il existe une suite \( \left( {x}_{n}\right) \) de points de \( A \) tendant vers \( x \) . Comme \( g \) et \( h \) sont continues, on a

> - Let \( x \in  E \smallsetminus  A \) . Since \( A \) is dense in \( E \) , there exists a sequence \( \left( {x}_{n}\right) \) of points in \( A \) converging to \( x \) . Since \( g \) and \( h \) are continuous, we have

\[
g\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}g\left( {x}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {x}_{n}\right) ,\;\text{ de même }\;h\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {x}_{n}\right) ,
\]

ce qui suffit pour conclure \( g\left( x\right) = h\left( x\right) \) .

> which is sufficient to conclude \( g\left( x\right) = h\left( x\right) \) .

b) L'idée est de se ramener au cas précédent puis de prouver que la fonction \( g \) obtenue est bien uniformément continue.

> b) The idea is to reduce it to the previous case and then prove that the resulting function \( g \) is indeed uniformly continuous.

Soit \( {x}_{0} \in E \smallsetminus A \) . Montrons que \( \mathop{\lim }\limits_{\substack{{y \rightarrow {x}_{0}} \\ {y \in A} }}f\left( y\right) \) existe. Soit \( \varepsilon > 0 \) . Comme \( f \) est uniformément continue sur \( A \) ,

> Let \( {x}_{0} \in E \smallsetminus A \) . Let us show that \( \mathop{\lim }\limits_{\substack{{y \rightarrow {x}_{0}} \\ {y \in A} }}f\left( y\right) \) exists. Let \( \varepsilon > 0 \) . Since \( f \) is uniformly continuous on \( A \) ,

\[
\left( {\exists \alpha  > 0,\forall \left( {x, y}\right)  \in  {A}^{2}}\right) ,\;\mathrm{\;d}\left( {x, y}\right)  < \alpha  \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

En particulier, si \( x, y \in A \) vérifient \( \mathrm{d}\left( {x,{x}_{0}}\right) < \alpha /2 \) et \( \mathrm{d}\left( {y,{x}_{0}}\right) < \alpha /2 \) , on a \( \mathrm{d}\left( {x, y}\right) < \alpha \) donc \( \delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \) . Comme \( \left( {F,\delta }\right) \) est complet, d’après le critère de Cauchy pour les fonctions (voir la proposition 10), on en déduit que lim \( \mathop{\max }\limits_{\substack{{y \rightarrow {x}_{0}} \\ {u \in A} }}f\left( y\right) \) existe.

> In particular, if \( x, y \in A \) satisfy \( \mathrm{d}\left( {x,{x}_{0}}\right) < \alpha /2 \) and \( \mathrm{d}\left( {y,{x}_{0}}\right) < \alpha /2 \), we have \( \mathrm{d}\left( {x, y}\right) < \alpha \) and therefore \( \delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \). Since \( \left( {F,\delta }\right) \) is complete, according to the Cauchy criterion for functions (see proposition 10), we deduce that lim \( \mathop{\max }\limits_{\substack{{y \rightarrow {x}_{0}} \\ {u \in A} }}f\left( y\right) \) exists.

D’après le résultat de la question précédente, la fonction \( g \) définie sur \( E \) par

> Based on the result of the previous question, the function \( g \) defined on \( E \) by

\[
\forall x \in  A,\;g\left( x\right)  = f\left( x\right) \;\text{ et }\;\forall x \in  E \smallsetminus  A,\;g\left( x\right)  = \mathop{\lim }\limits_{\substack{{y \rightarrow  x} \\  {y \in  A} }}f\left( y\right)
\]

est continue sur \( E \) . Nous allons prouver qu’elle est uniformément continue sur \( E \) . Fixons \( \varepsilon > 0 \) . Par hypothèse, \( f \) est uniformément continue sur \( A \) , donc

> is continuous on \( E \). We will prove that it is uniformly continuous on \( E \). Let us fix \( \varepsilon > 0 \). By hypothesis, \( f \) is uniformly continuous on \( A \), so

\[
\left( {\exists \alpha  > 0,\forall \left( {x, y}\right)  \in  {A}^{2}}\right) ,\;\mathrm{\;d}\left( {x, y}\right)  < \alpha  \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

Donnons nous \( \left( {x, y}\right) \in {E}^{2} \) avec \( \mathrm{d}\left( {x, y}\right) < \alpha \) . Comme \( A \) est dense dans \( E \) , il existe deux suites \( \left( {x}_{n}\right) \) et \( \left( {y}_{n}\right) \) de points de \( A \) tendant respectivement vers \( x \) et \( y \) . La distance étant continue, on a \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{x}_{n},{y}_{n}}\right) = \mathrm{d}\left( {x, y}\right) < \alpha \) , ce qui montre l’existence de \( N \in \mathbb{N} \) tel que \( \mathrm{d}\left( {{x}_{n},{y}_{n}}\right) < \alpha \) pour tout \( n \geq N \) . Ainsi, pour tout \( n \geq N,\delta \left( {f\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right) < \varepsilon \) et en faisant tendre \( n \) vers l’infini, on obtient \( \delta \left( {g\left( x\right) , g\left( y\right) }\right) \leq \varepsilon \) . Ceci est vrai pour tout couple \( \left( {x, y}\right) \in {E}^{2} \) tel que \( \mathrm{d}\left( {x, y}\right) < \alpha \) , la fonction \( g \) est donc uniformément continue sur \( E \) .

> Let us take \( \left( {x, y}\right) \in {E}^{2} \) with \( \mathrm{d}\left( {x, y}\right) < \alpha \). Since \( A \) is dense in \( E \), there exist two sequences \( \left( {x}_{n}\right) \) and \( \left( {y}_{n}\right) \) of points in \( A \) tending respectively to \( x \) and \( y \). Since the distance is continuous, we have \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{x}_{n},{y}_{n}}\right) = \mathrm{d}\left( {x, y}\right) < \alpha \), which shows the existence of \( N \in \mathbb{N} \) such that \( \mathrm{d}\left( {{x}_{n},{y}_{n}}\right) < \alpha \) for all \( n \geq N \). Thus, for all \( n \geq N,\delta \left( {f\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right) < \varepsilon \) and by letting \( n \) tend to infinity, we obtain \( \delta \left( {g\left( x\right) , g\left( y\right) }\right) \leq \varepsilon \). This is true for any pair \( \left( {x, y}\right) \in {E}^{2} \) such that \( \mathrm{d}\left( {x, y}\right) < \alpha \), the function \( g \) is therefore uniformly continuous on \( E \).

L'unicité découle de l'unicité de la question précédente car une fonction uniformément continue est continue.

> Uniqueness follows from the uniqueness in the previous question because a uniformly continuous function is continuous.

EXERCICE 5. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) deux espaces métriques. On suppose que \( \left( {E,\mathrm{\;d}}\right) \) est complet. Soient \( f : E \rightarrow F \) continue et \( {\left( {E}_{n}\right) }_{n \in \mathbb{N}} \) une suite décroissante de fermés non vides dont le diamètre \( \delta \left( {E}_{n}\right) \) tend vers 0 . Montrer que

> EXERCISE 5. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,{\mathrm{\;d}}^{\prime }}\right) \) be two metric spaces. Suppose that \( \left( {E,\mathrm{\;d}}\right) \) is complete. Let \( f : E \rightarrow F \) be continuous and \( {\left( {E}_{n}\right) }_{n \in \mathbb{N}} \) be a decreasing sequence of non-empty closed sets whose diameter \( \delta \left( {E}_{n}\right) \) tends to 0. Show that

\[
f\left( {\mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}{E}_{n}}\right)  = \mathop{\bigcap }\limits_{{n \in  \mathbb{N}}}f\left( {E}_{n}\right) .
\]

Solution. Comme \( E \) est complet, il existe \( {x}_{0} \in E \) tel que \( { \cap }_{n \in \mathbb{N}}{E}_{n} = \left\{ {x}_{0}\right\} \) (voir la proposition 9). On en déduit \( f\left( {{ \cap }_{n \in \mathbb{N}}{E}_{n}}\right) = \left\{ {f\left( {x}_{0}\right) }\right\} \) . Il nous faut donc prouver \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) = \left\{ {f\left( {x}_{0}\right) }\right\} \) .

> Solution. Since \( E \) is complete, there exists \( {x}_{0} \in E \) such that \( { \cap }_{n \in \mathbb{N}}{E}_{n} = \left\{ {x}_{0}\right\} \) (see Proposition 9). We deduce \( f\left( {{ \cap }_{n \in \mathbb{N}}{E}_{n}}\right) = \left\{ {f\left( {x}_{0}\right) }\right\} \) from this. We must therefore prove \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) = \left\{ {f\left( {x}_{0}\right) }\right\} \) .

Pour tout \( n \in \mathbb{N},{x}_{0} \in {E}_{n} \) donc \( \left\{ {f\left( {x}_{0}\right) }\right\} \subset { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \) .

> For all \( n \in \mathbb{N},{x}_{0} \in {E}_{n} \) , therefore \( \left\{ {f\left( {x}_{0}\right) }\right\} \subset { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \) .

Montrons l’inclusion réciproque. L’application \( f \) est continue en \( {x}_{0} \) , donc pour tout voisinage \( V \) de \( f\left( {x}_{0}\right) \) , il existe un voisinage \( U \) de \( {x}_{0} \) tel que \( f\left( U\right) \subset V \) . Or pour tout \( n,{E}_{n} \subset {\mathrm{B}}_{\mathrm{f}}\left( {{x}_{0},\delta \left( {E}_{n}\right) }\right) \; \left( {\operatorname{car}{x}_{0} \in {E}_{n}}\right) \) , et comme \( \delta \left( {E}_{n}\right) \) tend vers 0,

> Let us show the reverse inclusion. The mapping \( f \) is continuous at \( {x}_{0} \) , so for every neighborhood \( V \) of \( f\left( {x}_{0}\right) \) , there exists a neighborhood \( U \) of \( {x}_{0} \) such that \( f\left( U\right) \subset V \) . However, for all \( n,{E}_{n} \subset {\mathrm{B}}_{\mathrm{f}}\left( {{x}_{0},\delta \left( {E}_{n}\right) }\right) \; \left( {\operatorname{car}{x}_{0} \in {E}_{n}}\right) \) , and since \( \delta \left( {E}_{n}\right) \) tends to 0,

\[
\exists n \in  \mathbb{N},\;{E}_{n} \subset  {\mathrm{B}}_{\mathrm{f}}\left( {{x}_{0},\delta \left( {E}_{n}\right) }\right)  \subset  U,\;\text{ donc }\;f\left( {E}_{n}\right)  \subset  f\left( U\right)  \subset  V.
\]

Ainsi, \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \subset V \) , et ceci pour tout voisinage \( V \) de \( f\left( {x}_{0}\right) \) . Ceci suffit pour conclure à l’inclusion \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \subset \left\{ {f\left( {x}_{0}\right) }\right\} \) , d’où le résultat.

> Thus, \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \subset V \) , and this for every neighborhood \( V \) of \( f\left( {x}_{0}\right) \) . This is sufficient to conclude the inclusion \( { \cap }_{n \in \mathbb{N}}f\left( {E}_{n}\right) \subset \left\{ {f\left( {x}_{0}\right) }\right\} \) , hence the result.

Remarque. Rappelons qu’en général l’égalité \( f\left( {{ \cap }_{i \in I}{X}_{i}}\right) = { \cap }_{i \in I}f\left( {X}_{i}\right) \) est fausse. Par contre, l’inclusion \( f\left( {{ \cap }_{i \in I}{X}_{i}}\right) \subset { \cap }_{i \in I}f\left( {X}_{i}\right) \) a toujours lieu.

> Remark. Recall that in general the equality \( f\left( {{ \cap }_{i \in I}{X}_{i}}\right) = { \cap }_{i \in I}f\left( {X}_{i}\right) \) is false. On the other hand, the inclusion \( f\left( {{ \cap }_{i \in I}{X}_{i}}\right) \subset { \cap }_{i \in I}f\left( {X}_{i}\right) \) always holds.

EXERCICE 6 (COMPLÉTÉ D'UN ESPACE MÉTRIQUE). Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. On note \( \mathcal{C} \) l’ensemble des suites de Cauchy \( U = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) de \( E \) . Le but de l’exercice est de plonger \( \left( {E,\mathrm{\;d}}\right) \) dans un espace complet dont la distance prolonge celle de \( E \) .

> EXERCISE 6 (COMPLETION OF A METRIC SPACE). Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. Let \( \mathcal{C} \) denote the set of Cauchy sequences \( U = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) of \( E \) . The goal of the exercise is to embed \( \left( {E,\mathrm{\;d}}\right) \) into a complete space whose distance extends that of \( E \) .

1 / a) Soient \( U = \left( {u}_{n}\right) \) et \( V = \left( {v}_{n}\right) \in \mathcal{C} \) . Montrer que la suite \( \left( {\mathrm{d}\left( {{u}_{n},{v}_{n}}\right) }\right) \) converge. On note \( \delta \left( {U, V}\right) \) sa limite.

> 1 / a) Let \( U = \left( {u}_{n}\right) \) and \( V = \left( {v}_{n}\right) \in \mathcal{C} \) . Show that the sequence \( \left( {\mathrm{d}\left( {{u}_{n},{v}_{n}}\right) }\right) \) converges. Let \( \delta \left( {U, V}\right) \) denote its limit.

b) Montrer que \( \delta \) est symétrique et vérifie l’inégalité triangulaire.

> b) Show that \( \delta \) is symmetric and satisfies the triangle inequality.

2 / On considère la relation d’équivalence sur \( \mathcal{C} \) définie par \( \left( {U \sim V}\right) \Leftrightarrow \left( {\delta \left( {U, V}\right) = 0}\right) \) . On note \( \widehat{E} \) l’espace quotient \( \mathcal{C}/ \sim \) et \( \widehat{U} \) la classe d’équivalence dans \( \widehat{E} \) de \( U \in \mathcal{C} \) .

> 2 / Consider the equivalence relation on \( \mathcal{C} \) defined by \( \left( {U \sim V}\right) \Leftrightarrow \left( {\delta \left( {U, V}\right) = 0}\right) \) . Let \( \widehat{E} \) denote the quotient space \( \mathcal{C}/ \sim \) and \( \widehat{U} \) the equivalence class in \( \widehat{E} \) of \( U \in \mathcal{C} \) .

a) Quelle est la classe d'une suite convergente dans \( E \) ?

> a) What is the class of a convergent sequence in \( E \) ?

b) Montrer que si \( U \sim {U}^{\prime } \) et \( V \sim {V}^{\prime } \) , alors \( \delta \left( {U, V}\right) = \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \) . Lorsque \( \widehat{U},\widehat{V} \in \widehat{E} \) , le réel \( \delta \left( {U, V}\right) \) est donc indépendant du choix des représentants \( U \) et \( V \) de \( \widehat{U} \) et \( \widehat{V} \) . On le note \( \delta \left( {\widehat{U},\widehat{V}}\right) \) .

> b) Show that if \( U \sim {U}^{\prime } \) and \( V \sim {V}^{\prime } \) , then \( \delta \left( {U, V}\right) = \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \) . When \( \widehat{U},\widehat{V} \in \widehat{E} \) , the real number \( \delta \left( {U, V}\right) \) is therefore independent of the choice of representatives \( U \) and \( V \) of \( \widehat{U} \) and \( \widehat{V} \) . We denote it by \( \delta \left( {\widehat{U},\widehat{V}}\right) \) .

c) Ainsi définie, montrer que \( \delta \) est une distance sur \( \widehat{E} \) .

> c) Thus defined, show that \( \delta \) is a distance on \( \widehat{E} \) .

d) Montrer qu’il existe une injection naturelle \( i : E \rightarrow \widehat{E} \) , isométrique, et que \( i\left( E\right) \) est dense dans \( \widehat{E} \) .

> d) Show that there exists a natural isometric injection \( i : E \rightarrow \widehat{E} \) , and that \( i\left( E\right) \) is dense in \( \widehat{E} \) .

3/ Montrer que \( \widehat{E} \) est complet.

> 3/ Show that \( \widehat{E} \) is complete.

4/ Soient \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\left( {{E}_{2},{\mathrm{\;d}}_{2}}\right) \) deux espaces métriques complets tels qu’il existe une isométrie \( {i}_{1} \) (resp. \( {i}_{2} \) ) de \( E \) dans \( {E}_{1} \) (resp. dans \( {E}_{2} \) ), avec \( {i}_{1}\left( E\right) \) (resp. \( {i}_{2}\left( E\right) \) ) dense dans \( {E}_{1} \) (resp. dans \( {E}_{2} \) ). Montrer l’existence d’une unique isométrie \( \varphi \) de \( {E}_{1} \) dans \( {E}_{2} \) , bijective, et vérifiant \( \varphi \left( {{i}_{1}\left( x\right) }\right) = {i}_{2}\left( x\right) \) pour tout \( x \in E \) .

> 4/ Let \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\left( {{E}_{2},{\mathrm{\;d}}_{2}}\right) \) be two complete metric spaces such that there exists an isometry \( {i}_{1} \) (resp. \( {i}_{2} \) ) from \( E \) into \( {E}_{1} \) (resp. into \( {E}_{2} \) ), with \( {i}_{1}\left( E\right) \) (resp. \( {i}_{2}\left( E\right) \) ) dense in \( {E}_{1} \) (resp. in \( {E}_{2} \) ). Show the existence of a unique bijective isometry \( \varphi \) from \( {E}_{1} \) onto \( {E}_{2} \) , satisfying \( \varphi \left( {{i}_{1}\left( x\right) }\right) = {i}_{2}\left( x\right) \) for all \( x \in E \) .

Solution. 1/ a) Comme \( \mathbb{R} \) est complet, il suffit de montrer que la suite \( {\left( \mathrm{d}\left( {u}_{n},{v}_{n}\right) \right) }_{n \in \mathbb{N}} \) est de Cauchy. Pour tous \( p, q \in \mathbb{N} \) ,

> Solution. 1/ a) Since \( \mathbb{R} \) is complete, it suffices to show that the sequence \( {\left( \mathrm{d}\left( {u}_{n},{v}_{n}\right) \right) }_{n \in \mathbb{N}} \) is Cauchy. For all \( p, q \in \mathbb{N} \) ,

\[
\mathrm{d}\left( {{u}_{p},{v}_{p}}\right)  \leq  \mathrm{d}\left( {{u}_{p},{u}_{q}}\right)  + \mathrm{d}\left( {{u}_{q},{v}_{q}}\right)  + \mathrm{d}\left( {{v}_{q},{v}_{p}}\right)
\]

donc

> therefore

\[
\mathrm{d}\left( {{u}_{p},{v}_{p}}\right)  - \mathrm{d}\left( {{u}_{q},{v}_{q}}\right)  \leq  \mathrm{d}\left( {{u}_{p},{u}_{q}}\right)  + \mathrm{d}\left( {{v}_{p},{v}_{q}}\right) .
\]

On obtient de même \( \mathrm{d}\left( {{u}_{q},{v}_{q}}\right) - \mathrm{d}\left( {{u}_{p},{v}_{p}}\right) \leq \mathrm{d}\left( {{u}_{p},{u}_{q}}\right) + \mathrm{d}\left( {{v}_{p},{v}_{q}}\right) \) , d’où

> We similarly obtain \( \mathrm{d}\left( {{u}_{q},{v}_{q}}\right) - \mathrm{d}\left( {{u}_{p},{v}_{p}}\right) \leq \mathrm{d}\left( {{u}_{p},{u}_{q}}\right) + \mathrm{d}\left( {{v}_{p},{v}_{q}}\right) \) , hence

\[
\left| {\mathrm{d}\left( {{u}_{q},{v}_{q}}\right)  - \mathrm{d}\left( {{u}_{p},{v}_{p}}\right) }\right|  \leq  \mathrm{d}\left( {{u}_{p},{u}_{q}}\right)  + \mathrm{d}\left( {{v}_{p},{v}_{q}}\right) .
\]

Les suites \( U \) et \( V \) étant de Cauchy, on en déduit que la suite \( \left( {\mathrm{d}\left( {{u}_{n},{v}_{n}}\right) }\right) \) est de Cauchy.

> Since the sequences \( U \) and \( V \) are Cauchy, we deduce that the sequence \( \left( {\mathrm{d}\left( {{u}_{n},{v}_{n}}\right) }\right) \) is Cauchy.

b) C'est immédiat par passage à la limite, les propriétés de symétrie et d'inégalité triangulaires étant vraies pour d.

> b) This is immediate by passing to the limit, as the properties of symmetry and the triangle inequality hold for d.

2 / a) Soit \( U = \left( {u}_{n}\right) \) une suite de \( E \) convergeant vers \( \alpha \in E \) . Toute suite convergente est de Cauchy, donc \( U \in \mathcal{C} \) . Soit \( V = \left( {v}_{n}\right) \in \mathcal{C} \) . On a

> 2 / a) Let \( U = \left( {u}_{n}\right) \) be a sequence of \( E \) converging to \( \alpha \in E \) . Every convergent sequence is Cauchy, so \( U \in \mathcal{C} \) . Let \( V = \left( {v}_{n}\right) \in \mathcal{C} \) . We have

\[
U \sim  V \Leftrightarrow  \delta \left( {U, V}\right)  = 0 \Leftrightarrow  \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathrm{d}\left( {{u}_{n},{v}_{n}}\right)  = 0.
\]

Les inégalités

> The inequalities

\[
\mathrm{d}\left( {\alpha ,{v}_{n}}\right)  \leq  \mathrm{d}\left( {\alpha ,{u}_{n}}\right)  + \mathrm{d}\left( {{u}_{n},{v}_{n}}\right) \;\text{ et }\;\mathrm{d}\left( {{u}_{n},{v}_{n}}\right)  \leq  \mathrm{d}\left( {{u}_{n},\alpha }\right)  + \mathrm{d}\left( {\alpha ,{v}_{n}}\right)
\]

montrent que \( U \sim V \) si et seulement si \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {\alpha ,{v}_{n}}\right) = 0 \) . Finalement, la classe de \( U \) est l’ensemble des suites qui convergent vers \( \alpha \) .

> show that \( U \sim V \) if and only if \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {\alpha ,{v}_{n}}\right) = 0 \) . Finally, the class of \( U \) is the set of sequences that converge to \( \alpha \) .

b) Si \( U \sim {U}^{\prime } \) et \( V \sim {V}^{\prime } \) , comme \( \delta \) satisfait l’inégalité triangulaire, on a

> b) If \( U \sim {U}^{\prime } \) and \( V \sim {V}^{\prime } \) , as \( \delta \) satisfies the triangle inequality, we have

\[
\delta \left( {U, V}\right)  \leq  \delta \left( {U,{U}^{\prime }}\right)  + \delta \left( {{U}^{\prime },{V}^{\prime }}\right)  + \delta \left( {{V}^{\prime }, V}\right)  = \delta \left( {{U}^{\prime },{V}^{\prime }}\right) ,
\]

de même \( \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \leq \delta \left( {U, V}\right) \) . Donc \( \delta \left( {U, V}\right) = \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \) .

> similarly \( \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \leq \delta \left( {U, V}\right) \) . Thus \( \delta \left( {U, V}\right) = \delta \left( {{U}^{\prime },{V}^{\prime }}\right) \) .

c) Après le résultat de la question \( 1/\mathrm{b} \) ), il reste à prouver \( \delta \left( {\widehat{U},\widehat{V}}\right) = 0 \) si et seulement si \( \widehat{U} = \widehat{V} \) . Ceci est vrai par construction de la relation d'équivalence \( \sim \) .

> c) After the result of question \( 1/\mathrm{b} \) ), it remains to prove \( \delta \left( {\widehat{U},\widehat{V}}\right) = 0 \) if and only if \( \widehat{U} = \widehat{V} \) . This is true by construction of the equivalence relation \( \sim \) .

d) Pour tout \( \alpha \in E \) , on note \( \left( \alpha \right) \in \mathcal{C} \) la suite constante égale à \( \alpha \) . Soit \( i : E \rightarrow \widehat{E}\;\alpha \mapsto \widehat{\left( \alpha \right) } \) . On a

> d) For any \( \alpha \in E \) , we denote by \( \left( \alpha \right) \in \mathcal{C} \) the constant sequence equal to \( \alpha \) . Let \( i : E \rightarrow \widehat{E}\;\alpha \mapsto \widehat{\left( \alpha \right) } \) . We have

\[
\delta \left( {i\left( \alpha \right) , i\left( \beta \right) }\right)  = \delta \left( {\left( \alpha \right) ,\left( \beta \right) }\right)  = \mathrm{d}\left( {\alpha ,\beta }\right) ,
\]

c’est-à-dire \( i \) est isométrique, et c’est donc une injection.

> that is to say \( i \) is isometric, and it is therefore an injection.

Montrons que \( i\left( E\right) \) est dense dans \( \widehat{E} \) . Soit \( \widehat{U} \in \widehat{E} \) , avec \( U = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \in \mathcal{C} \) . Nous allons prouver que \( \widehat{U} \) est la limite de la suite \( {\left( i\left( {u}_{n}\right) \right) }_{n \in \mathbb{N}} \) . Soit \( \varepsilon > 0 \) . La suite \( \left( {u}_{n}\right) \) est de Cauchy, de sorte qu’il existe \( N \in \mathbb{N} \) tel que pour tous \( p, q \geq N,\mathrm{\;d}\left( {{u}_{p},{u}_{q}}\right) < \varepsilon \) . En fixant \( p \geq N \) , on en déduit

> Let us show that \( i\left( E\right) \) is dense in \( \widehat{E} \) . Let \( \widehat{U} \in \widehat{E} \) , with \( U = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \in \mathcal{C} \) . We will prove that \( \widehat{U} \) is the limit of the sequence \( {\left( i\left( {u}_{n}\right) \right) }_{n \in \mathbb{N}} \) . Let \( \varepsilon > 0 \) . The sequence \( \left( {u}_{n}\right) \) is Cauchy, so there exists \( N \in \mathbb{N} \) such that for all \( p, q \geq N,\mathrm{\;d}\left( {{u}_{p},{u}_{q}}\right) < \varepsilon \) . By fixing \( p \geq N \) , we deduce

\[
\delta \left( {\widehat{U}, i\left( {u}_{p}\right) }\right)  = \delta \left( {U,\left( {u}_{p}\right) }\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathrm{d}\left( {{u}_{n},{u}_{p}}\right)  \leq  \varepsilon .
\]

Ceci étant vrai pour tout \( p \geq N \) , on en déduit lim \( {}_{p \rightarrow \infty }i\left( {u}_{p}\right) = \widehat{U} \) . Ainsi, on a montré que tout élément \( \widehat{U} \) de \( \widehat{E} \) est limite de points de \( i\left( E\right) \) , d’où le résultat.

> Since this is true for all \( p \geq N \) , we deduce lim \( {}_{p \rightarrow \infty }i\left( {u}_{p}\right) = \widehat{U} \) . Thus, we have shown that every element \( \widehat{U} \) of \( \widehat{E} \) is a limit of points of \( i\left( E\right) \) , hence the result.

3/ Soit \( {\left( {\alpha }_{n}\right) }_{n \in \mathbb{N}} \) une suite de Cauchy de \( \widehat{E} \) . Comme \( i\left( E\right) \) est dense dans \( \widehat{E} \) , il existe pour tout \( n \in {\mathbb{N}}^{ * } \) un point \( {x}_{n} \) de \( E \) tel que \( \delta \left( {{\alpha }_{n}, i\left( {x}_{n}\right) }\right) < 1/n \) . L’inégalité

> 3/ Let \( {\left( {\alpha }_{n}\right) }_{n \in \mathbb{N}} \) be a Cauchy sequence in \( \widehat{E} \) . Since \( i\left( E\right) \) is dense in \( \widehat{E} \) , for every \( n \in {\mathbb{N}}^{ * } \) there exists a point \( {x}_{n} \) in \( E \) such that \( \delta \left( {{\alpha }_{n}, i\left( {x}_{n}\right) }\right) < 1/n \) . The inequality

\[
\mathrm{d}\left( {{x}_{p},{x}_{q}}\right)  = \delta \left( {i\left( {x}_{p}\right) , i\left( {x}_{q}\right) }\right)  \leq  \delta \left( {i\left( {x}_{p}\right) ,{\alpha }_{p}}\right)  + \delta \left( {{\alpha }_{p},{\alpha }_{q}}\right)  + \delta \left( {{\alpha }_{q}, i\left( {x}_{q}\right) }\right)  \leq  \delta \left( {{\alpha }_{p},{\alpha }_{q}}\right)  + \frac{1}{p} + \frac{1}{q}
\]

montre que la suite \( \left( {x}_{n}\right) \) est de Cauchy dans \( E \) . Notons \( \alpha \) la suite \( {\left( \widehat{{x}_{n}}\right) }_{n \in \mathbb{N}} \) de \( \widehat{E} \) .

> shows that the sequence \( \left( {x}_{n}\right) \) is Cauchy in \( E \) . Let \( \alpha \) denote the sequence \( {\left( \widehat{{x}_{n}}\right) }_{n \in \mathbb{N}} \) in \( \widehat{E} \) .

Montrons que \( \left( {\alpha }_{n}\right) \) converge vers \( \alpha \) . Comme \( \delta \left( {{\alpha }_{n},\alpha }\right) \leq \delta \left( {{\alpha }_{n}, i\left( {x}_{n}\right) }\right) + \delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) \leq \frac{1}{n} + \; \delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) \) , il suffit de prouver que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) = 0 \) . Soit \( \varepsilon > 0 \) . La suite \( \left( {x}_{n}\right) \) étant de Cauchy dans \( E \) ,

> Let us show that \( \left( {\alpha }_{n}\right) \) converges to \( \alpha \) . Since \( \delta \left( {{\alpha }_{n},\alpha }\right) \leq \delta \left( {{\alpha }_{n}, i\left( {x}_{n}\right) }\right) + \delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) \leq \frac{1}{n} + \; \delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) \) , it suffices to prove that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {i\left( {x}_{n}\right) ,\alpha }\right) = 0 \) . Let \( \varepsilon > 0 \) . Since the sequence \( \left( {x}_{n}\right) \) is Cauchy in \( E \) ,

\[
\exists N \in  \mathbb{N},\forall p \geq  N,\forall q \geq  N,\;\mathrm{\;d}\left( {{x}_{p},{x}_{q}}\right)  < \varepsilon ,
\]

donc si on fixe \( n \geq N \) ,

> so if we fix \( n \geq N \) ,

\[
\delta \left( {i\left( {x}_{n}\right) ,\alpha }\right)  = \mathop{\lim }\limits_{{p \rightarrow  \infty }}\mathrm{d}\left( {{x}_{n},{x}_{p}}\right)  \leq  \varepsilon ,
\]

et ceci pour tout \( n \geq N \) , d’où le résultat. 4 / Définissons \( \varphi \operatorname{sur}{i}_{1}\left( E\right) \) en posant \( \varphi \left( {{i}_{1}\left( x\right) }\right) = {i}_{2}\left( x\right) \) pour tout \( x \in E \) . L’application \( \varphi \) restreinte à \( {i}_{1}\left( E\right) \) est isométrique car

> and this for all \( n \geq N \) , hence the result. 4/ Let us define \( \varphi \operatorname{sur}{i}_{1}\left( E\right) \) by setting \( \varphi \left( {{i}_{1}\left( x\right) }\right) = {i}_{2}\left( x\right) \) for all \( x \in E \) . The map \( \varphi \) restricted to \( {i}_{1}\left( E\right) \) is an isometry because

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;{\mathrm{\;d}}_{2}\left( {\varphi \left( {{i}_{1}\left( x\right) }\right) ,\varphi \left( {{i}_{1}\left( y\right) }\right) }\right)  = {\mathrm{d}}_{2}\left( {{i}_{2}\left( x\right) ,{i}_{2}\left( y\right) }\right)  = \mathrm{d}\left( {x, y}\right)  = {\mathrm{d}}_{1}\left( {{i}_{1}\left( x\right) ,{i}_{1}\left( y\right) }\right) .
\]

Ainsi, \( \varphi \) est uniformément continue sur \( {i}_{1}\left( E\right) \) . Comme \( {i}_{1}\left( E\right) \) est dense dans \( {E}_{1} \) et que \( {E}_{2} \) est complet, il existe (voir l’exercice 4) un prolongement de \( \varphi \) sur \( {E}_{1} \) , encore noté \( \varphi \) , qui est uniformément continu sur \( {E}_{1} \) . De plus \( \varphi \) est isométrique sur \( {i}_{1}\left( E\right) \) , et comme \( {i}_{1}\left( E\right) \) est dense dans \( {E}_{1} \) et que \( \varphi \) est continue, \( \varphi \) est isométrique sur \( {E}_{1} \) tout entier. En particulier, \( \varphi \) est injective.

> Thus, \( \varphi \) is uniformly continuous on \( {i}_{1}\left( E\right) \) . Since \( {i}_{1}\left( E\right) \) is dense in \( {E}_{1} \) and \( {E}_{2} \) is complete, there exists (see exercise 4) an extension of \( \varphi \) to \( {E}_{1} \) , still denoted by \( \varphi \) , which is uniformly continuous on \( {E}_{1} \) . Furthermore, \( \varphi \) is an isometry on \( {i}_{1}\left( E\right) \) , and since \( {i}_{1}\left( E\right) \) is dense in \( {E}_{1} \) and \( \varphi \) is continuous, \( \varphi \) is an isometry on the whole of \( {E}_{1} \) . In particular, \( \varphi \) is injective.

Il nous reste à montrer que \( \varphi \) est surjective. Soit \( \beta \in {E}_{2} \) . Comme \( {i}_{2}\left( E\right) \) est dense dans \( {E}_{2} \) , il existe une suite \( \left( {\beta }_{n}\right) = \left( {{i}_{2}\left( {x}_{n}\right) }\right) \) de \( {i}_{2}\left( E\right) \) qui converge vers \( \beta \) . De plus pour tous \( p, q \in \mathbb{N} \) ,

> It remains for us to show that \( \varphi \) is surjective. Let \( \beta \in {E}_{2} \) . Since \( {i}_{2}\left( E\right) \) is dense in \( {E}_{2} \) , there exists a sequence \( \left( {\beta }_{n}\right) = \left( {{i}_{2}\left( {x}_{n}\right) }\right) \) in \( {i}_{2}\left( E\right) \) that converges to \( \beta \) . Moreover, for all \( p, q \in \mathbb{N} \) ,

\[
{\mathrm{d}}_{1}\left( {{i}_{1}\left( {x}_{p}\right) ,{i}_{1}\left( {x}_{q}\right) }\right)  = \mathrm{d}\left( {{x}_{p},{x}_{q}}\right)  = {\mathrm{d}}_{2}\left( {{i}_{2}\left( {x}_{p}\right) ,{i}_{2}\left( {x}_{q}\right) }\right)  = {\mathrm{d}}_{2}\left( {{\beta }_{p},{\beta }_{q}}\right)
\]

la suite \( \left( {{i}_{1}\left( {x}_{n}\right) }\right) \) est donc de Cauchy dans \( {E}_{1} \) . Comme \( {E}_{1} \) est complet, elle converge. Soit \( \alpha \) sa limite. Comme \( \varphi \) est continue,

> the sequence \( \left( {{i}_{1}\left( {x}_{n}\right) }\right) \) is therefore Cauchy in \( {E}_{1} \) . Since \( {E}_{1} \) is complete, it converges. Let \( \alpha \) be its limit. Since \( \varphi \) is continuous,

\[
\varphi \left( \alpha \right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\varphi \left( {{i}_{1}\left( {x}_{n}\right) }\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{i}_{2}\left( {x}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\beta }_{n} = \beta ,
\]

d'où la surjectivité.

> hence the surjectivity.

L’application \( \varphi \) est unique d’après l’unicité du prolongement continue sur \( {E}_{1} \) (voir l’exer-cice 4).

> The map \( \varphi \) is unique according to the uniqueness of the continuous extension on \( {E}_{1} \) (see exercise 4).

Remarque. Par abus, on identifie souvent \( E \) et \( i\left( E\right) \) dans \( \widehat{E} \) . Ainsi, \( \widehat{E} \) est un espace complet dans lequel \( E \) est plongé, et sa métrique prolonge celle de \( E \) .

> Remark. By abuse of notation, \( E \) and \( i\left( E\right) \) are often identified in \( \widehat{E} \) . Thus, \( \widehat{E} \) is a complete space in which \( E \) is embedded, and its metric extends that of \( E \) .

- La partie 4/ montre que \( \widehat{E} \) est unique à une isométrie bijective près. On l’appelle le complété de \( E \) .

> - Part 4/ shows that \( \widehat{E} \) is unique up to a bijective isometry. It is called the completion of \( E \) .

- On procède de manière similaire pour définir \( \mathbb{R} \) à partir de \( \mathbb{Q} \) ( \( \mathbb{R} \) est le complété de \( \mathbb{Q} \) ). La différence est que, \( \mathbb{R} \) "n’existant pas encore", on ne peut pas définir \( \delta \left( {U, V}\right) \) pour \( U, V \in  \mathcal{C} \) . On peut par contre définir la classe d’équivalence \( U \sim  V \Leftrightarrow  \mathop{\lim }\limits_{{n \rightarrow  \infty }}{u}_{n} - {v}_{n} = 0 \) . La notion de limite peut en effet être définie si l’on reste uniquement sur \( \mathbb{Q} \) (il suffit de prendre les \( \varepsilon \) et les \( \alpha \) dans \( \mathbb{Q} \) ).

> - We proceed similarly to define \( \mathbb{R} \) from \( \mathbb{Q} \) ( \( \mathbb{R} \) is the completion of \( \mathbb{Q} \) ). The difference is that, since \( \mathbb{R} \) "does not yet exist", we cannot define \( \delta \left( {U, V}\right) \) for \( U, V \in  \mathcal{C} \) . However, we can define the equivalence class \( U \sim  V \Leftrightarrow  \mathop{\lim }\limits_{{n \rightarrow  \infty }}{u}_{n} - {v}_{n} = 0 \) . The notion of limit can indeed be defined if we remain solely on \( \mathbb{Q} \) (it suffices to take the \( \varepsilon \) and the \( \alpha \) in \( \mathbb{Q} \) ).
