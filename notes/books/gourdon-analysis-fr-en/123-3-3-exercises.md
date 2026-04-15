#### 3.3. Exercises

*Français : 3.3. Exercices*

EXERCICE 1. Soit \( f : {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {{x}^{2} - {y}^{2},{2xy}}\right) \)

> EXERCISE 1. Let \( f : {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {{x}^{2} - {y}^{2},{2xy}}\right) \)

a) Montrer qu’en tout point de \( {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} , f \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme local.

> a) Show that at every point of \( {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} , f \) is a local \( {\mathcal{C}}^{\infty } \) diffeomorphism.

b) L’application \( f \) est-elle un \( {\mathcal{C}}^{\infty } \) difféomorphisme global ?

> b) Is the map \( f \) a global \( {\mathcal{C}}^{\infty } \) diffeomorphism?

Solution. a) La fonction \( f \) est clairement de classe \( {\mathcal{C}}^{\infty } \) . Soit \( \left( {a, b}\right) \in {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} \) . Le jacobien de \( f \) en \( \left( {a, b}\right) \) est égal à

> Solution. a) The function \( f \) is clearly of class \( {\mathcal{C}}^{\infty } \) . Let \( \left( {a, b}\right) \in {\mathbb{R}}^{2} \smallsetminus \{ \left( {0,0}\right) \} \) . The Jacobian of \( f \) at \( \left( {a, b}\right) \) is equal to

\[
\left| \begin{array}{rr} {2a} & {2b} \\   - {2b} & {2a} \end{array}\right|  = 4\left( {{a}^{2} + {b}^{2}}\right)  \neq  0.
\]

Donc, d’après le théorème d’inversion locale (corollaire 3), il existe un ouvert \( U \) contenant \( \left( {a, b}\right) \) , un ouvert \( V \) contenant \( f\left( {a, b}\right) \) , tel que la restriction de \( f \) à \( U \) soit un \( {\mathcal{C}}^{\infty } \) -difféomorphisme de \( U \) sur \( V \) . Autrement dit, \( f \) est un \( {\mathcal{C}}^{\infty } \) -difféomorphisme local en \( \left( {a, b}\right) \) .

> Thus, according to the local inversion theorem (corollary 3), there exists an open set \( U \) containing \( \left( {a, b}\right) \) , an open set \( V \) containing \( f\left( {a, b}\right) \) , such that the restriction of \( f \) to \( U \) is a \( {\mathcal{C}}^{\infty } \) -diffeomorphism from \( U \) onto \( V \) . In other words, \( f \) is a local \( {\mathcal{C}}^{\infty } \) -diffeomorphism at \( \left( {a, b}\right) \) .

b) On remarque que \( f\left( {-x, - y}\right) = f\left( {x, y}\right) \) , la fonction \( f \) n’est donc pas injective, et donc ce n’est pas un \( {\mathcal{C}}^{\infty } \) difféomorphisme global.

> b) We note that \( f\left( {-x, - y}\right) = f\left( {x, y}\right) \) , the function \( f \) is therefore not injective, and thus it is not a global \( {\mathcal{C}}^{\infty } \) diffeomorphism.

En fait, en identifiant \( {\mathbb{R}}^{2} \) et \( \mathbb{C}, f \) s’écrit \( f\left( z\right) = {z}^{2} \) pour tout \( z \in {\mathbb{C}}^{ * } \) . On en conclut que les ensembles \( {U}_{\alpha } = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid x\cos \alpha + y\sin \alpha > 0}\right\} \) sont des ouverts maximaux sur lesquels \( f \) est injective. Avec le corollaire 4, on en conclut que \( f \) un \( {\mathcal{C}}^{\infty } \) -difféomorphisme de \( {U}_{\alpha } \) sur \( f\left( {U}_{\alpha }\right) = {\mathbb{R}}^{2} \smallsetminus \left\{ {-r\left( {\cos {2\alpha },\sin {2\alpha }}\right) , r \geq 0}\right\} \) (avec \( \alpha \in \mathbb{R} \) quelconque).

> In fact, by identifying \( {\mathbb{R}}^{2} \) and \( \mathbb{C}, f \) is written as \( f\left( z\right) = {z}^{2} \) for all \( z \in {\mathbb{C}}^{ * } \) . We conclude that the sets \( {U}_{\alpha } = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid x\cos \alpha + y\sin \alpha > 0}\right\} \) are maximal open sets on which \( f \) is injective. With corollary 4, we conclude that \( f \) is a \( {\mathcal{C}}^{\infty } \) -diffeomorphism from \( {U}_{\alpha } \) onto \( f\left( {U}_{\alpha }\right) = {\mathbb{R}}^{2} \smallsetminus \left\{ {-r\left( {\cos {2\alpha },\sin {2\alpha }}\right) , r \geq 0}\right\} \) (with \( \alpha \in \mathbb{R} \) arbitrary).

EXERCICE 2. Soit l’application \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto \sin y + x{y}^{4} + {x}^{2} \) .

> EXERCISE 2. Let the map \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto \sin y + x{y}^{4} + {x}^{2} \) .

a) Montrer qu’il existe deux voisinages ouverts \( U \) et \( V \) de 0 dans \( \mathbb{R} \) et une fonction \( \varphi : U \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{\infty } \) tels que pour tout \( x \in U,\varphi \left( x\right) \) est l’unique solution \( y \in V \) de l’équation \( f\left( {x, y}\right) = 0 \) .

> a) Show that there exist two open neighborhoods \( U \) and \( V \) of 0 in \( \mathbb{R} \) and a function \( \varphi : U \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{\infty } \) such that for all \( x \in U,\varphi \left( x\right) \) is the unique solution \( y \in V \) to the equation \( f\left( {x, y}\right) = 0 \) .

b) Donner un développement limité à l’ordre 10 de \( \varphi \) au voisinage de 0 .

> b) Provide a Taylor expansion to the order of 10 for \( \varphi \) in the neighborhood of 0.

Solution. a) La fonction \( f \) est de classe \( {\mathcal{C}}^{\infty } \) , elle vérifie \( f\left( {0,0}\right) = 0 \) et \( \frac{\partial f}{\partial y}\left( {0,0}\right) = 1 \neq 0 \) . On en déduit le résultat en appliquant le théorème des fonctions implicites.

> Solution. a) The function \( f \) is of class \( {\mathcal{C}}^{\infty } \), it satisfies \( f\left( {0,0}\right) = 0 \) and \( \frac{\partial f}{\partial y}\left( {0,0}\right) = 1 \neq 0 \). We deduce the result by applying the implicit function theorem.

b) On a bien sûr \( \varphi \left( 0\right) = 0 \) puisque \( f\left( {0,0}\right) = 0 \) . On pourrait calculer le développement limité de \( \varphi \) en utilisant la relation exprimant \( {\varphi }^{\prime } \) , puis en la dérivant successivement. Cette technique est cependant fastidieuse puisque l'on veut aller jusqu'à l'ordre 10 !

> b) We obviously have \( \varphi \left( 0\right) = 0 \) since \( f\left( {0,0}\right) = 0 \). One could calculate the Taylor expansion of \( \varphi \) by using the relation expressing \( {\varphi }^{\prime } \), then by differentiating it successively. This technique is however tedious since we want to go up to the order 10!

Nous utilisons une autre technique, classique (et à retenir). On a vu \( \varphi \left( 0\right) = 0 \) , donc \( \varphi \left( x\right) = O\left( x\right) \) lorsque \( x \rightarrow 0 \) (puisque \( \varphi \) est dérivable en 0 ). Maintenant,à partir de la relation \( f\left( {x,\varphi \left( x\right) }\right) = 0 \) , l’idée est d’exprimer \( \varphi \left( x\right) \) en fonction de termes ne faisant intervenir \( \varphi \left( x\right) \) qu'avec un ordre supérieur. Ici, on a

> We use another technique, which is classic (and worth remembering). We have seen \( \varphi \left( 0\right) = 0 \), therefore \( \varphi \left( x\right) = O\left( x\right) \) when \( x \rightarrow 0 \) (since \( \varphi \) is differentiable at 0). Now, starting from the relation \( f\left( {x,\varphi \left( x\right) }\right) = 0 \), the idea is to express \( \varphi \left( x\right) \) as a function of terms involving \( \varphi \left( x\right) \) only with a higher order. Here, we have

\[
\varphi \left( x\right)  = \left( {\varphi \left( x\right)  - \sin \varphi \left( x\right) }\right)  - {x\varphi }{\left( x\right) }^{4} - {x}^{2} = O\left( {\varphi {\left( x\right) }^{3}}\right)  - {x}^{2} =  - {x}^{2} + O\left( {x}^{3}\right) ,
\]

ce qui nous donne déjà le développement limité à l'ordre 2. Partant maintenant de l'information \( \varphi \left( x\right) = - {x}^{2} + O\left( {x}^{3}\right) \) , on itère le procédé, ce qui donne

> which already gives us the Taylor expansion to the order 2. Starting now from the information \( \varphi \left( x\right) = - {x}^{2} + O\left( {x}^{3}\right) \), we iterate the process, which gives

\[
\varphi \left( x\right)  = \left( {\varphi \left( x\right)  - \sin \varphi \left( x\right) }\right)  - {x\varphi }{\left( x\right) }^{4} - {x}^{2} = \frac{\varphi {\left( x\right) }^{3}}{6} + O\left( {\varphi {\left( x\right) }^{4}}\right)  - {x}^{2}
\]

\[
= \frac{{\left( -{x}^{2} + O\left( {x}^{3}\right) \right) }^{3}}{6} + O\left( {x}^{8}\right)  - {x}^{2} =  - {x}^{2} - \frac{{x}^{6}}{6} + O\left( {x}^{7}\right) .
\]

On obtient le résultat demandé en réinjectant encore une fois,

> We obtain the requested result by re-injecting once more,

\[
\varphi \left( x\right)  = \left( {\varphi \left( x\right)  - \sin \varphi \left( x\right) }\right)  - {x\varphi }{\left( x\right) }^{4} - {x}^{2}
\]

\[
= \frac{\varphi {\left( x\right) }^{3}}{6} - \frac{\varphi {\left( x\right) }^{5}}{120} + O\left( {\varphi {\left( x\right) }^{7}}\right)  - {x\varphi }{\left( x\right) }^{4} - {x}^{2}
\]

\[
=  - \frac{{x}^{6}}{6}{\left( 1 + \frac{{x}^{4}}{6} + O\left( {x}^{5}\right) \right) }^{3} + \frac{{x}^{10}}{120}{\left( 1 + O\left( {x}^{4}\right) \right) }^{5} + O\left( {x}^{14}\right)  - {x}^{9}{\left( 1 + O\left( {x}^{4}\right) \right) }^{4} - {x}^{2}
\]

\[
=  - {x}^{2} - \frac{{x}^{6}}{6} - {x}^{9} - \frac{3{x}^{10}}{40} + O\left( {x}^{11}\right) .
\]

EXERCICE 3. Soit \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que l’application \( \varphi = \; f - {\operatorname{Id}}_{{\mathbb{R}}^{n}} \) est \( k \) -contractante (avec \( 0 < k < 1 \) ). Montrer que \( f \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme global de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) .

> EXERCISE 3. Let \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a function of class \( {\mathcal{C}}^{1} \) such that the mapping \( \varphi = \; f - {\operatorname{Id}}_{{\mathbb{R}}^{n}} \) is \( k \)-contracting (with \( 0 < k < 1 \)). Show that \( f \) is a \( {\mathcal{C}}^{1} \)-global diffeomorphism from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \).

Solution. En vertu du corollaire 4 du théorème d'inversion locale, il suffit de montrer que

> Solution. By virtue of corollary 4 of the local inversion theorem, it suffices to show that

(i) pour tout \( x \in {\mathbb{R}}^{n}, d{f}_{x} \) est inversible ;

> (i) for all \( x \in {\mathbb{R}}^{n}, d{f}_{x} \) is invertible;

(ii) \( f \) est une bijection de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) .

> (ii) \( f \) is a bijection from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \).

(i). Soit \( x \in {\mathbb{R}}^{n} \) . Pour tout \( h \in {\mathbb{R}}^{n} \) , on a \( \parallel \varphi \left( {x + h}\right) - \varphi \left( x\right) \parallel \leq k\parallel h\parallel \) , et on en déduit facilement \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} \leq k\parallel h\parallel \) pour tout \( h \in {\mathbb{R}}^{n} \) . En d’autres termes, \( \begin{Vmatrix}{d{\varphi }_{x}}\end{Vmatrix} \leq k < 1 \) , et donc \( d{f}_{x} = \operatorname{Id} + d{\varphi }_{x} \) est inversible d’après la proposition 2 page 49. On peut retrouver ce résultat sans invoquer cette dernière proposition en remarquant que si \( d{f}_{x}\left( h\right) = 0 \) , alors \( h + d{\varphi }_{x}\left( h\right) = 0 \) donc \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} = \parallel h\parallel \) et comme \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} \leq k\parallel h\parallel \) avec \( k < 1 \) ceci entraîne forcément \( h = 0 \) . Ainsi \( d{f}_{x} \) est un endomorphisme injectif et comme on est en dimension finie, \( d{f}_{x} \) est donc inversible.

> (i). Let \( x \in {\mathbb{R}}^{n} \). For all \( h \in {\mathbb{R}}^{n} \), we have \( \parallel \varphi \left( {x + h}\right) - \varphi \left( x\right) \parallel \leq k\parallel h\parallel \), and we easily deduce \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} \leq k\parallel h\parallel \) for all \( h \in {\mathbb{R}}^{n} \). In other words, \( \begin{Vmatrix}{d{\varphi }_{x}}\end{Vmatrix} \leq k < 1 \), and therefore \( d{f}_{x} = \operatorname{Id} + d{\varphi }_{x} \) is invertible according to proposition 2 on page 49. We can recover this result without invoking the latter proposition by noting that if \( d{f}_{x}\left( h\right) = 0 \), then \( h + d{\varphi }_{x}\left( h\right) = 0 \) so \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} = \parallel h\parallel \) and since \( \begin{Vmatrix}{d{\varphi }_{x}\left( h\right) }\end{Vmatrix} \leq k\parallel h\parallel \) with \( k < 1 \) this necessarily implies \( h = 0 \). Thus \( d{f}_{x} \) is an injective endomorphism and since we are in finite dimension, \( d{f}_{x} \) is therefore invertible.

(ii). Il nous reste à montrer que \( f \) est une bijection. Fixons \( y \in {\mathbb{R}}^{n} \) . On a \( f\left( x\right) = y \) si et seulement si \( x \) est point fixe de l’application \( {\psi }_{y} : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;x \mapsto x - f\left( x\right) + y = y - \varphi \left( x\right) \) . Or

> (ii). It remains for us to show that \( f \) is a bijection. Let us fix \( y \in {\mathbb{R}}^{n} \). We have \( f\left( x\right) = y \) if and only if \( x \) is a fixed point of the mapping \( {\psi }_{y} : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;x \mapsto x - f\left( x\right) + y = y - \varphi \left( x\right) \). Now

\[
\forall x,{x}^{\prime } \in  {\mathbb{R}}^{n},\;\begin{Vmatrix}{{\psi }_{y}\left( x\right)  - {\psi }_{y}\left( {x}^{\prime }\right) }\end{Vmatrix} = \begin{Vmatrix}{\varphi \left( x\right)  - \varphi \left( {x}^{\prime }\right) }\end{Vmatrix} \leq  k\begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix},
\]

donc \( {\psi }_{y} \) est \( k \) -contractante. D’après le théorème du point fixe, on en déduit qu’il existe un unique point \( x \) de \( {\mathbb{R}}^{n} \) tel que \( {\psi }_{y}\left( x\right) = x \) , autrement dit il existe un unique point \( x \in {\mathbb{R}}^{n} \) tel que \( f\left( x\right) = y \) . Ceci étant vrai pour tout \( y \in {\mathbb{R}}^{n} \) , on en déduit que \( f \) est une bijection de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) .

> therefore \( {\psi }_{y} \) is \( k \)-contracting. According to the fixed-point theorem, we deduce that there exists a unique point \( x \) of \( {\mathbb{R}}^{n} \) such that \( {\psi }_{y}\left( x\right) = x \), in other words there exists a unique point \( x \in {\mathbb{R}}^{n} \) such that \( f\left( x\right) = y \). Since this is true for all \( y \in {\mathbb{R}}^{n} \), we deduce that \( f \) is a bijection from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \).

EXERCICE 4. Soit \( E \) un espace euclidien (de dimension finie). On note \( \langle \) , \( \rangle {leproduit} \) scalaire sur \( E \) et \( \parallel .\parallel \) la norme euclidienne associée. Soit \( f : E \rightarrow E \) une application de classe \( {\mathcal{C}}^{1} \) telle que pour tout \( x \in E, d{f}_{x} \) est une isométrie de \( E \) (i. e. \( \begin{Vmatrix}{d{f}_{x}\left( h\right) }\end{Vmatrix} = \parallel h\parallel \) pour tout \( h \in E \) ).

> EXERCISE 4. Let \( E \) be a Euclidean space (of finite dimension). We denote by \( \langle \), \( \rangle {leproduit} \) the scalar product on \( E \) and by \( \parallel .\parallel \) the associated Euclidean norm. Let \( f : E \rightarrow E \) be a \( {\mathcal{C}}^{1} \) class mapping such that for all \( x \in E, d{f}_{x} \) is an isometry of \( E \) (i.e., \( \begin{Vmatrix}{d{f}_{x}\left( h\right) }\end{Vmatrix} = \parallel h\parallel \) for all \( h \in E \)).

a) Pour tout \( a \in E \) , montrer l’existence d’un ouvert \( {U}_{a} \) contenant \( a \) tel que \( \parallel f\left( x\right) - f\left( y\right) \parallel = \; \parallel x - y\parallel \) pour tout \( \left( {x, y}\right) \in {U}_{a}^{2}. \)

> a) For all \( a \in E \), show the existence of an open set \( {U}_{a} \) containing \( a \) such that \( \parallel f\left( x\right) - f\left( y\right) \parallel = \; \parallel x - y\parallel \) for all \( \left( {x, y}\right) \in {U}_{a}^{2}. \)

b) Montrer que

> b) Show that

\[
\forall \left( {x, y}\right)  \in  {U}_{a}^{2},\forall \left( {h,\ell }\right)  \in  {E}^{2},\;\left\langle  {d{f}_{x}\left( h\right) , d{f}_{y}\left( \ell \right) }\right\rangle   = \langle h,\ell \rangle .
\]

En déduire \( d{f}_{x} = d{f}_{y} \) pour tout \( \left( {x, y}\right) \in {U}_{a}^{2} \) .

> Deduce \( d{f}_{x} = d{f}_{y} \) for all \( \left( {x, y}\right) \in {U}_{a}^{2} \).

c) Montrer que \( f \) est une isométrie affine de \( E \) sur \( E \) .

> c) Show that \( f \) is an affine isometry from \( E \) onto \( E \).

Solution. a) Normons \( \mathcal{L}\left( E\right) \) avec la norme \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) pour tout \( u \in \mathcal{L}\left( E\right) \) . On a \( \begin{Vmatrix}{d{f}_{x}}\end{Vmatrix} = 1 \) pour tout \( x \in E \) , donc d’après l’inégalité des accroissements finis,

> Solution. a) Let us equip \( \mathcal{L}\left( E\right) \) with the norm \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) for all \( u \in \mathcal{L}\left( E\right) \). We have \( \begin{Vmatrix}{d{f}_{x}}\end{Vmatrix} = 1 \) for all \( x \in E \), so by the mean value inequality,

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\parallel f\left( x\right)  - f\left( y\right) \parallel  \leq  \parallel x - y\parallel .
\]

(*)

> Ceci étant, soit \( a \in E \) . Comme \( d{f}_{a} \) est une isométrie, \( d{f}_{a} \) est inversible. D’après le théorème d’inversion locale, il existe un ouvert \( {V}_{a} \) contenant \( a \) tel que \( {f}_{\mid {V}_{a}} \) soit un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( {V}_{a} \) sur \( {W}_{a} = f\left( {V}_{a}\right) \) . Notons \( g : {W}_{a} \rightarrow {V}_{a} \) le difféomorphisme inverse. Pour tout \( y = f\left( x\right) \in {W}_{a} \) , \( d{g}_{y} = {\left( d{f}_{x}\right) }^{-1} \) est une isométrie, donc \( \begin{Vmatrix}{d{g}_{y}}\end{Vmatrix} = 1 \) . Quitte à restreindre \( {V}_{a} \) en un ouvert plus petit \( {U}_{a} \) , on peut supposer que \( {W}_{a} = f\left( {U}_{a}\right) \) est convexe (prendre par exemple \( {U}_{a} = g\left( B\right) \) où \( B \) est une boule ouverte centrée en \( f\left( a\right) \) incluse dans \( f\left( {V}_{a}\right) \) , de sorte que \( {W}_{a} = f\left( {g\left( B\right) }\right) = B \) ). On peut donc appliquer l’inégalité des accroissements finis à \( g \) sur \( {W}_{a} \) , ce qui entraîne \( \parallel g\left( x\right) - g\left( y\right) \parallel \leq \parallel x - y\parallel \) pour tout \( \left( {x, y}\right) \in {W}_{a}^{2} \) . On en conclut

Given this, let \( a \in E \). Since \( d{f}_{a} \) is an isometry, \( d{f}_{a} \) is invertible. By the local inversion theorem, there exists an open set \( {V}_{a} \) containing \( a \) such that \( {f}_{\mid {V}_{a}} \) is a \( {\mathcal{C}}^{1} \)-diffeomorphism from \( {V}_{a} \) onto \( {W}_{a} = f\left( {V}_{a}\right) \). Let \( g : {W}_{a} \rightarrow {V}_{a} \) denote the inverse diffeomorphism. For all \( y = f\left( x\right) \in {W}_{a} \), \( d{g}_{y} = {\left( d{f}_{x}\right) }^{-1} \) is an isometry, so \( \begin{Vmatrix}{d{g}_{y}}\end{Vmatrix} = 1 \). By restricting \( {V}_{a} \) to a smaller open set \( {U}_{a} \), we can assume that \( {W}_{a} = f\left( {U}_{a}\right) \) is convex (take, for example, \( {U}_{a} = g\left( B\right) \) where \( B \) is an open ball centered at \( f\left( a\right) \) included in \( f\left( {V}_{a}\right) \), such that \( {W}_{a} = f\left( {g\left( B\right) }\right) = B \)). We can therefore apply the mean value inequality to \( g \) on \( {W}_{a} \), which implies \( \parallel g\left( x\right) - g\left( y\right) \parallel \leq \parallel x - y\parallel \) for all \( \left( {x, y}\right) \in {W}_{a}^{2} \). We conclude

\[
\forall \left( {x, y}\right)  \in  {U}_{a}^{2},\;\parallel x - y\parallel  = \parallel g\left( {f\left( x\right) }\right)  - g\left( {f\left( y\right) }\right) \parallel  \leq  \parallel f\left( x\right)  - f\left( y\right) \parallel .
\]

Avec (*), on en déduit \( \parallel f\left( x\right) - f\left( y\right) \parallel = \parallel x - y\parallel \) pour tout \( \left( {x, y}\right) \in {U}_{a}^{2} \) .

> With (*), we deduce \( \parallel f\left( x\right) - f\left( y\right) \parallel = \parallel x - y\parallel \) for all \( \left( {x, y}\right) \in {U}_{a}^{2} \).

b) Le résultat de la question précédente s'écrit aussi

> b) The result of the previous question can also be written as

\[
\forall \left( {x, y}\right)  \in  {U}_{a}^{2},\;\langle f\left( x\right)  - f\left( y\right) , f\left( x\right)  - f\left( y\right) \rangle  = \langle x - y, x - y\rangle .
\]

En différentiant cette égalité par rapport à \( x \) selon le vecteur \( h \in E \) , on obtient

> By differentiating this equality with respect to \( x \) along the vector \( h \in E \), we obtain

\[
\left\langle  {d{f}_{x}\left( h\right) , f\left( x\right)  - f\left( y\right) }\right\rangle   + \left\langle  {f\left( x\right)  - f\left( y\right) , d{f}_{x}\left( h\right) }\right\rangle   = \langle h, x - y\rangle  + \langle x - y, h\rangle ,
\]

et par symétrie du produit scalaire, ceci s’écrit aussi \( \left\langle {d{f}_{x}\left( h\right) , f\left( x\right) - f\left( y\right) }\right\rangle = \langle h, x - y\rangle \) . Par différentiation de cette dernière égalité par rapport à \( y \) selon un vecteur \( \ell \in E \) , on en déduit \( - \left\langle {d{f}_{x}\left( h\right) , d{f}_{y}\left( \ell \right) }\right\rangle = - \langle h,\ell \rangle \) . Autrement dit nous venons de montrer le premier résultat voulu.

> and by symmetry of the scalar product, this can also be written as \( \left\langle {d{f}_{x}\left( h\right) , f\left( x\right) - f\left( y\right) }\right\rangle = \langle h, x - y\rangle \) . By differentiating this last equality with respect to \( y \) along a vector \( \ell \in E \) , we deduce \( - \left\langle {d{f}_{x}\left( h\right) , d{f}_{y}\left( \ell \right) }\right\rangle = - \langle h,\ell \rangle \) . In other words, we have just shown the first desired result.

Donnons nous maintenant \( x, y \in {U}_{a} \) et \( h \in E \) . On a

> Let us now consider \( x, y \in {U}_{a} \) and \( h \in E \) . We have

\[
{\begin{Vmatrix}d{f}_{x}\left( h\right)  - d{f}_{y}\left( h\right) \end{Vmatrix}}^{2} = {\begin{Vmatrix}d{f}_{x}\left( h\right) \end{Vmatrix}}^{2} - 2\left\langle  {d{f}_{x}\left( h\right) , d{f}_{y}\left( h\right) }\right\rangle   + {\begin{Vmatrix}d{f}_{y}\left( h\right) \end{Vmatrix}}^{2} = \parallel h{\parallel }^{2} - 2\langle h, h\rangle  + \parallel h{\parallel }^{2} = 0,
\]

donc \( d{f}_{x}\left( h\right) = d{f}_{y}\left( h\right) \) . Ceci étant vrai pour tout \( h \in E \) , on a donc \( d{f}_{x} = d{f}_{y} \) .

> therefore \( d{f}_{x}\left( h\right) = d{f}_{y}\left( h\right) \) . Since this is true for all \( h \in E \) , we therefore have \( d{f}_{x} = d{f}_{y} \) .

c) D’après le résultat de la question précédente, l’ensemble \( \Gamma = \left\{ {x \in E \mid d{f}_{x} = d{f}_{0}}\right\} \) est un ouvert de \( {\mathbb{R}}^{n} \) . De plus, \( f \) est de classe \( {\mathcal{C}}^{1} \) donc \( \Gamma \) est aussi un fermé de \( {\mathbb{R}}^{n} \) . En résumé, \( \Gamma \) est un ouvert et un fermé de \( E \) . Or \( E \) est connexe (car convexe), donc \( \Gamma = E \) . En posant \( u = d{f}_{0} \) , on a donc \( d{f}_{x} = u \) pour tout \( x \in E \) . Ainsi la fonction \( x \mapsto f\left( x\right) - u\left( x\right) \) a sa différentielle nulle sur \( E \) tout entier, donc c’est une fonction constante. Si on note \( \alpha \in E \) sa valeur, on a \( f\left( x\right) = u\left( x\right) + \alpha \) pour tout \( x \in {\mathbb{R}}^{n} \) . Comme \( u = d{f}_{0} \) est une isométrie, on en déduit que \( f \) est une isométrie affine.

> c) According to the result of the previous question, the set \( \Gamma = \left\{ {x \in E \mid d{f}_{x} = d{f}_{0}}\right\} \) is an open subset of \( {\mathbb{R}}^{n} \) . Furthermore, \( f \) is of class \( {\mathcal{C}}^{1} \) , so \( \Gamma \) is also a closed subset of \( {\mathbb{R}}^{n} \) . In summary, \( \Gamma \) is an open and closed subset of \( E \) . However, \( E \) is connected (because it is convex), so \( \Gamma = E \) . By setting \( u = d{f}_{0} \) , we therefore have \( d{f}_{x} = u \) for all \( x \in E \) . Thus, the function \( x \mapsto f\left( x\right) - u\left( x\right) \) has a zero differential on the entirety of \( E \) , so it is a constant function. If we denote its value by \( \alpha \in E \) , we have \( f\left( x\right) = u\left( x\right) + \alpha \) for all \( x \in {\mathbb{R}}^{n} \) . Since \( u = d{f}_{0} \) is an isometry, we deduce that \( f \) is an affine isometry.

EXERCICE 5 (FONCTIONS STRICTEMENT MONOTONES). Soit \( E \) un espace euclidien (de dimension finie). On note \( \langle \) , \( \rangle {leproduitscalairesurEet}\parallel .\parallel {lanormeeuclidienneassoci}. \)

> EXERCISE 5 (STRICTLY MONOTONE FUNCTIONS). Let \( E \) be a Euclidean space (of finite dimension). We denote \( \langle \) , \( \rangle {leproduitscalairesurEet}\parallel .\parallel {lanormeeuclidienneassoci}. \)

Une application \( f : E \rightarrow E \) est dite strictement monotone s’il existe \( k > 0 \) tel que

> A mapping \( f : E \rightarrow E \) is said to be strictly monotone if there exists \( k > 0 \) such that

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\langle f\left( x\right)  - f\left( y\right) , x - y\rangle  \geq  k\parallel x - y{\parallel }^{2}.
\]

(*)

> a) Soit \( f : E \rightarrow E \) une fonction de classe \( {\mathcal{C}}^{1} \) . Montrer que \( f \) vérifie (*) si et seulement si

a) Let \( f : E \rightarrow E \) be a function of class \( {\mathcal{C}}^{1} \) . Show that \( f \) satisfies (*) if and only if

\[
\forall x \in  E,\forall h \in  E,\;\left\langle  {d{f}_{x}\left( h\right) , h}\right\rangle   \geq  k\parallel h{\parallel }^{2}.
\]

b) Si \( f : E \rightarrow E \) est de classe \( {\mathcal{C}}^{1} \) et si elle est strictement monotone, montrer que \( f \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( E \) sur \( E \) .

> b) If \( f : E \rightarrow E \) is of class \( {\mathcal{C}}^{1} \) and is strictly monotone, show that \( f \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism from \( E \) onto \( E \) .

Solution. a) Condition nécessaire. Supposons que \( f \) vérifie (*). Alors pour tout \( x \in E \) , pour tout \( h \in E \) et pour tout \( t \in {\mathbb{R}}^{ * } \) ,

> Solution. a) Necessary condition. Suppose that \( f \) satisfies (*). Then for all \( x \in E \) , for all \( h \in E \) , and for all \( t \in {\mathbb{R}}^{ * } \) ,

\[
\langle f\left( {x + {th}}\right)  - f\left( x\right) ,{th}\rangle  \geq  k{t}^{2}\parallel h{\parallel }^{2}\;\text{ ou encore }\;\left\langle  {\frac{f\left( {x + {th}}\right)  - f\left( x\right) }{t}, h}\right\rangle   \geq  k\parallel h{\parallel }^{2},
\]

et en faisant tendre \( t \) vers 0 on en déduit \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) .

> and by letting \( t \) tend to 0, we deduce \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) .

Condition suffisante. Supposons \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) pour tout \( x, h \in E \) . Soient \( x, h \in E \) . Consi-dérons l’application \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto \langle f\left( {x + {th}}\right) , h\rangle \) . On a

> Sufficient condition. Assume \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) for all \( x, h \in E \) . Let \( x, h \in E \) . Consider the mapping \( \varphi : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;t \mapsto \langle f\left( {x + {th}}\right) , h\rangle \) . We have

\[
\forall t \in  \mathbb{R},\;{\varphi }^{\prime }\left( t\right)  = \left\langle  {d{f}_{x + {th}}\left( h\right) , h}\right\rangle   \geq  k\parallel h{\parallel }^{2}
\]

donc \( \varphi \left( 1\right) - \varphi \left( 0\right) \geq k\parallel h{\parallel }^{2} \) , c’est-à-dire \( \langle f\left( {x + h}\right) - f\left( x\right) , h\rangle \geq k\parallel h{\parallel }^{2} \) , d’où (*).

> thus \( \varphi \left( 1\right) - \varphi \left( 0\right) \geq k\parallel h{\parallel }^{2} \) , that is to say \( \langle f\left( {x + h}\right) - f\left( x\right) , h\rangle \geq k\parallel h{\parallel }^{2} \) , whence (*).

b) En vertu du corollaire 4 du théorème d'inversion locale, il suffit de montrer

> b) By virtue of corollary 4 of the local inversion theorem, it suffices to show

(i) pour tout \( x \in E, d{f}_{x} \) est inversible ;

> (i) for all \( x \in E, d{f}_{x} \) is invertible ;

(ii) \( f \) est une bijection de \( E \) sur \( E \) .

> (ii) \( f \) is a bijection from \( E \) onto \( E \) .

(i). Soit \( x \in E \) . On a \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) pour tout \( h \in E \) , donc \( d{f}_{x}\left( h\right) \neq 0 \) pour tout \( h \neq 0 \) . Ainsi, \( d{f}_{x} \) est injective donc bijective (c'est un endomorphisme en dimension finie), d’où (i).

> (i). Let \( x \in E \) . We have \( \left\langle {d{f}_{x}\left( h\right) , h}\right\rangle \geq k\parallel h{\parallel }^{2} \) for all \( h \in E \) , thus \( d{f}_{x}\left( h\right) \neq 0 \) for all \( h \neq 0 \) . Thus, \( d{f}_{x} \) is injective and therefore bijective (it is an endomorphism in finite dimension), whence (i).

(ii). La relation (*) entraîne l’injectivité de \( f \) . Montrons maintenant que \( f \) est surjective. Comme \( E \) est connexe, on aura prouvé \( f\left( E\right) = E \) si on montre que \( f\left( E\right) \) est ouvert et fermé dans \( E \) . On sait déjà que \( f\left( E\right) \) est ouvert d’après (i) (voir le corollaire 1). Pour montrer que \( f\left( E\right) \) est fermé, nous allons montrer que \( f\left( E\right) \) est complet. Commençons par remarquer que d'après (*) et d'après l'inégalité de Schwarz,

> (ii). The relation (*) implies the injectivity of \( f \) . Let us now show that \( f \) is surjective. Since \( E \) is connected, we will have proven \( f\left( E\right) = E \) if we show that \( f\left( E\right) \) is open and closed in \( E \) . We already know that \( f\left( E\right) \) is open according to (i) (see corollary 1). To show that \( f\left( E\right) \) is closed, we will show that \( f\left( E\right) \) is complete. Let us begin by noting that according to (*) and according to the Schwarz inequality,

\[
\forall x, y \in  E,\;k\parallel x - y{\parallel }^{2} \leq  \parallel x - y\parallel \parallel f\left( x\right)  - f\left( y\right) \parallel \;\text{ donc }\;\parallel x - y\parallel  \leq  \frac{1}{k}\parallel f\left( x\right)  - f\left( y\right) \parallel .
\]

\( \left( {* * }\right) \)

> Considérons maintenant une suite de Cauchy \( \left( {f\left( {x}_{n}\right) }\right) \) de \( f\left( E\right) \) . D’après (**), on a \( \begin{Vmatrix}{{x}_{p} - {x}_{q}}\end{Vmatrix} \leq \; \begin{Vmatrix}{f\left( {x}_{p}\right) - f\left( {x}_{q}\right) }\end{Vmatrix}/k \) pour tout \( p, q \in \mathbb{N} \) , donc \( \left( {x}_{n}\right) \) est une suite de Cauchy dans \( E \) , donc converge. Si on note \( x \) sa limite, on a alors \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {x}_{n}\right) \) . Ainsi, la suite \( \left( {f\left( {x}_{n}\right) }\right) \) converge vers \( f\left( x\right) \in f\left( E\right) \) , donc \( f\left( E\right) \) est complet, d’où le résultat.

Consider now a Cauchy sequence \( \left( {f\left( {x}_{n}\right) }\right) \) of \( f\left( E\right) \) . According to (**), we have \( \begin{Vmatrix}{{x}_{p} - {x}_{q}}\end{Vmatrix} \leq \; \begin{Vmatrix}{f\left( {x}_{p}\right) - f\left( {x}_{q}\right) }\end{Vmatrix}/k \) for all \( p, q \in \mathbb{N} \) , thus \( \left( {x}_{n}\right) \) is a Cauchy sequence in \( E \) , and therefore converges. If we denote its limit by \( x \) , we then have \( f\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {x}_{n}\right) \) . Thus, the sequence \( \left( {f\left( {x}_{n}\right) }\right) \) converges to \( f\left( x\right) \in f\left( E\right) \) , therefore \( f\left( E\right) \) is complete, whence the result.

> EXERCICE 6. Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {U}_{n} = \left\{ {\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {\mathbb{R}}^{n} \mid {\lambda }_{1} < \cdots < {\lambda }_{n}}\right\} \) , et on note \( {\mathbb{R}}_{n - 1}\left\lbrack X\right\rbrack \) l’e.v des polynômes de \( \mathbb{R}\left\lbrack X\right\rbrack \) de degré \( \leq n - 1 \) . Montrer que l’application

EXERCISE 6. Let \( n \in {\mathbb{N}}^{ * } \) . Let \( {U}_{n} = \left\{ {\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {\mathbb{R}}^{n} \mid {\lambda }_{1} < \cdots < {\lambda }_{n}}\right\} \) be denoted, and let \( {\mathbb{R}}_{n - 1}\left\lbrack X\right\rbrack \) be the vector space of polynomials of \( \mathbb{R}\left\lbrack X\right\rbrack \) of degree \( \leq n - 1 \) . Show that the mapping

\[
\varphi  : {U}_{n} \rightarrow  {\mathbb{R}}_{n - 1}\left\lbrack  X\right\rbrack  \;\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \mapsto  \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right)  - {X}^{n}
\]

est un \( {\mathcal{C}}^{\infty } \) -difféomorphisme global de l’ouvert \( {U}_{n} \) sur \( \varphi \left( {U}_{n}\right) \) .

> is a global \( {\mathcal{C}}^{\infty } \) -diffeomorphism from the open set \( {U}_{n} \) onto \( \varphi \left( {U}_{n}\right) \) .

Solution. Il est clair que \( \varphi \) est injective, c’est donc une bijection de \( {U}_{n} \) sur \( \varphi \left( {U}_{n}\right) \) .

> Solution. It is clear that \( \varphi \) is injective, so it is a bijection from \( {U}_{n} \) onto \( \varphi \left( {U}_{n}\right) \) .

En vertu du corollaire 4 du théorème d'inversion locale, il suffit maintenant de prouver que la différentielle de \( \varphi \) est inversible en tout point \( \lambda \) de \( {U}_{n} \) , ce qui équivaut à montrer que les vecteurs \( \frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = d{\varphi }_{\lambda }\left( {e}_{i}\right) \) sont linéairement indépendants.

> By virtue of corollary 4 of the local inversion theorem, it now suffices to prove that the differential of \( \varphi \) is invertible at every point \( \lambda \) of \( {U}_{n} \) , which is equivalent to showing that the vectors \( \frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = d{\varphi }_{\lambda }\left( {e}_{i}\right) \) are linearly independent.

Soit \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {U}_{n} \) . Pour tout \( i \in \{ 1,\ldots , n\} ,\frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = - \mathop{\prod }\limits_{{j \neq i}}\left( {X - {\lambda }_{j}}\right) \) . Si maintenant on suppose \( \mathop{\sum }\limits_{i}{\mu }_{i}\frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = 0 \) , alors

> Let \( \lambda = \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {U}_{n} \) . For all \( i \in \{ 1,\ldots , n\} ,\frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = - \mathop{\prod }\limits_{{j \neq i}}\left( {X - {\lambda }_{j}}\right) \) . If we now assume \( \mathop{\sum }\limits_{i}{\mu }_{i}\frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) = 0 \) , then

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}\mathop{\prod }\limits_{{j \neq  i}}\left( {X - {\lambda }_{j}}\right)  = 0.
\]

(*)

> Soit \( k \in \{ 1,\ldots , n\} \) . En donnant à l’indéterminée \( X \) la valeur \( {\lambda }_{k} \) dans (*), on obtient \( {\mu }_{k}\mathop{\prod }\limits_{{j \neq k}}\left( {{\lambda }_{k} - }\right. \; {\lambda }_{j}) = 0 \) , donc \( {\mu }_{k} = 0 \) car les \( {\lambda }_{i} \) sont distincts. Ceci étant vrai pour tout \( k \) , on en déduit que les vecteurs \( \frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) \) sont linéairement indépendants, et ceci pour tout \( \lambda \in {U}_{n} \) , d’où le résultat.

Let \( k \in \{ 1,\ldots , n\} \) . By assigning the value \( {\lambda }_{k} \) to the indeterminate \( X \) in (*), we obtain \( {\mu }_{k}\mathop{\prod }\limits_{{j \neq k}}\left( {{\lambda }_{k} - }\right. \; {\lambda }_{j}) = 0 \) , therefore \( {\mu }_{k} = 0 \) because the \( {\lambda }_{i} \) are distinct. Since this is true for all \( k \) , we deduce that the vectors \( \frac{\partial \varphi }{\partial {\lambda }_{i}}\left( \lambda \right) \) are linearly independent, and this for all \( \lambda \in {U}_{n} \) , hence the result.
