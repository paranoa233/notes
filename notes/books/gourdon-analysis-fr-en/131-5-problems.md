### 5. Problems

*Français : 5. Problèmes*

ProblEME 1. Déterminer les fonctions \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto f\left( {x, y}\right) \) , de classe \( {\mathcal{C}}^{2} \) , telles que

> PROBLEM 1. Determine the functions \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto f\left( {x, y}\right) \), of class \( {\mathcal{C}}^{2} \), such that

\[
\frac{{\partial }^{2}f}{\partial {x}^{2}} + 2\frac{{\partial }^{2}f}{\partial x\partial y} - 3\frac{{\partial }^{2}f}{\partial {y}^{2}} = 0. \tag{E}
\]

(Indication : on pourra effectuer le changement de variable \( u = x + y, v = {\alpha x} - y \) , où \( \alpha \) est un réel à déterminer).

> (Hint: one may perform the change of variable \( u = x + y, v = {\alpha x} - y \), where \( \alpha \) is a real number to be determined).

Solution. Fixons \( \alpha \) quelconque et notons \( \varphi : {\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {u, v}\right) = \left( {x + y,{\alpha x} - y}\right) \) . Si \( \alpha \neq - 1,\varphi \) est bijective. Plaçons nous dans ce cas. Notons \( F = f \circ {\varphi }^{-1} \) (la fonction \( F \) est la fonction \( f \) dans les coordonnées \( u \) et \( v \) ). On a donc \( f\left( {x, y}\right) = F \circ \varphi \left( {x, y}\right) = F\left( {x + y,{\alpha x} - y}\right) \) et \( F = f \circ {\varphi }^{-1} \) est de classe \( {\mathcal{C}}^{2} \) . On a

> Solution. Let us fix an arbitrary \( \alpha \) and denote \( \varphi : {\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {u, v}\right) = \left( {x + y,{\alpha x} - y}\right) \). If \( \alpha \neq - 1,\varphi \) is bijective. Let us assume this case. Let us denote \( F = f \circ {\varphi }^{-1} \) (the function \( F \) is the function \( f \) in the coordinates \( u \) and \( v \)). We therefore have \( f\left( {x, y}\right) = F \circ \varphi \left( {x, y}\right) = F\left( {x + y,{\alpha x} - y}\right) \) and \( F = f \circ {\varphi }^{-1} \) is of class \( {\mathcal{C}}^{2} \). We have

\[
\frac{\partial f}{\partial x} = \frac{\partial F}{\partial u} + \alpha \frac{\partial F}{\partial v}\;\text{ et }\;\frac{\partial f}{\partial y} = \frac{\partial F}{\partial u} - \frac{\partial F}{\partial v}
\]

donc

> therefore

\[
\frac{{\partial }^{2}f}{\partial {x}^{2}} = \frac{\partial }{\partial u}\left( {\frac{\partial F}{\partial u} + \alpha \frac{\partial F}{\partial v}}\right)  + \alpha \frac{\partial }{\partial v}\left( {\frac{\partial F}{\partial u} + \alpha \frac{\partial F}{\partial v}}\right)  = \frac{{\partial }^{2}F}{\partial {u}^{2}} + {2\alpha }\frac{{\partial }^{2}F}{\partial u\partial v} + {\alpha }^{2}\frac{{\partial }^{2}F}{\partial {v}^{2}}
\]

\[
\frac{{\partial }^{2}f}{\partial x\partial y} = \frac{\partial }{\partial u}\left( \frac{\partial f}{\partial y}\right)  + \alpha \frac{\partial }{\partial v}\left( \frac{\partial f}{\partial y}\right)  = \frac{{\partial }^{2}F}{\partial {u}^{2}} + \left( {\alpha  - 1}\right) \frac{{\partial }^{2}F}{\partial u\partial v} - \alpha \frac{{\partial }^{2}F}{\partial {v}^{2}}
\]

\[
\frac{{\partial }^{2}f}{\partial {y}^{2}} = \frac{{\partial }^{2}F}{\partial {u}^{2}} - 2\frac{{\partial }^{2}F}{\partial u\partial v} + \frac{{\partial }^{2}F}{\partial {v}^{2}}
\]

et on en déduit

> and we deduce

\[
\frac{{\partial }^{2}f}{\partial {x}^{2}} + 2\frac{{\partial }^{2}f}{\partial x\partial y} - 3\frac{{\partial }^{2}f}{\partial {y}^{2}} = \left\lbrack  {{2\alpha } + 2\left( {\alpha  - 1}\right)  + 6}\right\rbrack  \frac{{\partial }^{2}F}{\partial u\partial v} + \left( {{\alpha }^{2} - {2\alpha } - 3}\right) \frac{{\partial }^{2}F}{\partial {v}^{2}}.
\]

L’idée est de faire disparaître le terme en \( \frac{{\partial }^{2}F}{\partial {v}^{2}} \) , pour se ramener à résoudre d \( \frac{{\partial }^{2}F}{\partial u\partial v} = 0 \) (ce qui s’intègre facilement). On va donc choisir \( \alpha \) tel que \( {\alpha }^{2} - {2\alpha } - 3 = 0 \) , c’est-à-dire \( \alpha = 3 \) ou \( \alpha = - 1 \) . Comme on doit avoir \( \alpha \neq - 1 \) (pour que la transformation soit bijective), on choisit \( \alpha = 3 \) .

> The idea is to eliminate the term in \( \frac{{\partial }^{2}F}{\partial {v}^{2}} \) to reduce it to solving d \( \frac{{\partial }^{2}F}{\partial u\partial v} = 0 \) (which integrates easily). We therefore choose \( \alpha \) such that \( {\alpha }^{2} - {2\alpha } - 3 = 0 \) , that is to say \( \alpha = 3 \) or \( \alpha = - 1 \) . Since we must have \( \alpha \neq - 1 \) (for the transformation to be bijective), we choose \( \alpha = 3 \) .

L’équation \( \left( E\right) \) est donc équivalente à \( \frac{{\partial }^{2}F}{\partial u\partial v} = 0 \) , où \( f\left( {x, y}\right) = F\left( {x + y,{3x} - y}\right) \) . Ceci s’écrit aussi \( \frac{\partial }{\partial u}\left\lbrack \frac{\partial F}{\partial v}\right\rbrack = 0 \) , donc la fonction \( {\mathcal{C}}^{1}\frac{\partial F}{\partial v} \) est indépendante de \( u \) . Il existe donc une fonction \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{1} \) telle que \( \frac{\partial F}{\partial v}\left( {u, v}\right) = \varphi \left( v\right) \) pour tout \( \left( {u, v}\right) \in {\mathbb{R}}^{2} \) . Notons \( \psi \) une primitive de \( \varphi \) . On a \( \frac{\partial \left( {F - \psi }\right) }{\partial v} = 0 \) , donc la fonction \( {\mathcal{C}}^{2}F - \psi \) est indépendante de \( v \) , de sorte qu’il existe \( \theta : \mathbb{R} \rightarrow \mathbb{R} \) telle que \( F\left( {u, v}\right) = \psi \left( v\right) + \theta \left( u\right) \) pour tout \( \left( {u, v}\right) \in {\mathbb{R}}^{2} \) . Finalement, nous avons montré que si \( f \) vérifie \( \left( E\right) \) , alors il existe deux fonctions \( \psi ,\theta : \mathbb{R} \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{2} \) telles que

> The equation \( \left( E\right) \) is therefore equivalent to \( \frac{{\partial }^{2}F}{\partial u\partial v} = 0 \) , where \( f\left( {x, y}\right) = F\left( {x + y,{3x} - y}\right) \) . This can also be written as \( \frac{\partial }{\partial u}\left\lbrack \frac{\partial F}{\partial v}\right\rbrack = 0 \) , so the function \( {\mathcal{C}}^{1}\frac{\partial F}{\partial v} \) is independent of \( u \) . There therefore exists a function \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{1} \) such that \( \frac{\partial F}{\partial v}\left( {u, v}\right) = \varphi \left( v\right) \) for all \( \left( {u, v}\right) \in {\mathbb{R}}^{2} \) . Let \( \psi \) be an antiderivative of \( \varphi \) . We have \( \frac{\partial \left( {F - \psi }\right) }{\partial v} = 0 \) , so the function \( {\mathcal{C}}^{2}F - \psi \) is independent of \( v \) , such that there exists \( \theta : \mathbb{R} \rightarrow \mathbb{R} \) such that \( F\left( {u, v}\right) = \psi \left( v\right) + \theta \left( u\right) \) for all \( \left( {u, v}\right) \in {\mathbb{R}}^{2} \) . Finally, we have shown that if \( f \) satisfies \( \left( E\right) \) , then there exist two functions \( \psi ,\theta : \mathbb{R} \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{2} \) such that

\[
\forall \left( {x, y}\right)  \in  {\mathbb{R}}^{2},\;f\left( {x, y}\right)  = F\left( {u, v}\right)  = F\left( {x + y,{3x} - y}\right)  = \theta \left( {x + y}\right)  + \psi \left( {{3x} - y}\right) .
\]

Réciproquement, si \( f \) a cette forme, on vérifie facilement qu’elle satisfait l’équation \( \left( E\right) \) .

> Conversely, if \( f \) has this form, we easily verify that it satisfies the equation \( \left( E\right) \) .

Problem 2 (DéRIVATIONS). Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {G}_{0}^{\infty } \) l’e.v des fonctions à valeurs réelles, définies sur un voisinage de 0 et de classe \( {\mathcal{C}}^{\infty } \) . Soit \( L \) une application de \( {G}_{0}^{\infty } \) dans \( \mathbb{R} \) vérifiant les propriétés suivantes :

> Problem 2 (DERIVATIONS). Let \( n \in {\mathbb{N}}^{ * } \) . Let \( {G}_{0}^{\infty } \) be the vector space of real-valued functions defined on a neighborhood of 0 and of class \( {\mathcal{C}}^{\infty } \) . Let \( L \) be a mapping from \( {G}_{0}^{\infty } \) to \( \mathbb{R} \) satisfying the following properties:

(i) \( L \) est linéaire ;

> (i) \( L \) is linear;

(ii) pour tout \( f, g \in {G}_{0}^{\infty }, L\left( {fg}\right) = f\left( 0\right) L\left( g\right) + L\left( f\right) g\left( 0\right) \) ;

> (ii) for all \( f, g \in {G}_{0}^{\infty }, L\left( {fg}\right) = f\left( 0\right) L\left( g\right) + L\left( f\right) g\left( 0\right) \) ;

(iii) \( L\left( 1\right) = 0 \) ;

> (iii) \( L\left( 1\right) = 0 \) ;

(on dit que \( L \) est une dérivation). Montrer qu’il existe \( \xi \in {\mathbb{R}}^{n} \) tel que \( L\left( f\right) = {f}_{\xi }^{\prime }\left( 0\right) = \; d{f}_{0}\left( \xi \right) \) pour tout \( f \in {G}_{0}^{\infty } \) . (Indication : on pourra utiliser le lemme d’Hadamard - voir l'exercice 4 page 331).

> (we say that \( L \) is a derivation). Show that there exists \( \xi \in {\mathbb{R}}^{n} \) such that \( L\left( f\right) = {f}_{\xi }^{\prime }\left( 0\right) = \; d{f}_{0}\left( \xi \right) \) for all \( f \in {G}_{0}^{\infty } \) . (Hint: one may use Hadamard's lemma - see exercise 4 on page 331).

Solution. Soit \( f \in {G}_{0}^{\infty } \) . Comme \( f - f\left( 0\right) \) s’annule en 0, on peut écrire, d’après le lemme d'Hadamard

> Solution. Let \( f \in {G}_{0}^{\infty } \) . Since \( f - f\left( 0\right) \) vanishes at 0, we can write, according to Hadamard's lemma

\[
\forall x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) ,\;f\left( x\right)  = f\left( 0\right)  + \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{\varphi }_{i}\left( x\right) ,
\]

où pour tout \( i,{\varphi }_{i} \) est définie et de classe \( {\mathcal{C}}^{\infty } \) sur un voisinage de 0, c’est-à-dire \( {\varphi }_{i} \in {G}_{0}^{\infty } \) . En notant par abus \( {x}_{i} \) la fonction \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{i} \) , la linéarité et la propriété (iii) de \( L \) entraînent

> where for all \( i,{\varphi }_{i} \) is defined and of class \( {\mathcal{C}}^{\infty } \) on a neighborhood of 0, that is to say \( {\varphi }_{i} \in {G}_{0}^{\infty } \) . By denoting by abuse \( {x}_{i} \) the function \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \mapsto {x}_{i} \) , the linearity and property (iii) of \( L \) imply

\[
L\left( f\right)  = f\left( 0\right) L\left( 1\right)  + \mathop{\sum }\limits_{{i = 1}}^{n}L\left( {{x}_{i}{\varphi }_{i}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}L\left( {{x}_{i}{\varphi }_{i}}\right) .
\]

Or, d’après (ii), \( L\left( {{x}_{i}{\varphi }_{i}}\right) = {0L}\left( {\varphi }_{i}\right) + L\left( {x}_{i}\right) {\varphi }_{i}\left( 0\right) = L\left( {x}_{i}\right) {\varphi }_{i}\left( 0\right) \) , et comme \( {\varphi }_{i}\left( 0\right) = \frac{\partial f}{\partial {x}_{i}}\left( 0\right) \) , on en déduit

> Now, according to (ii), \( L\left( {{x}_{i}{\varphi }_{i}}\right) = {0L}\left( {\varphi }_{i}\right) + L\left( {x}_{i}\right) {\varphi }_{i}\left( 0\right) = L\left( {x}_{i}\right) {\varphi }_{i}\left( 0\right) \) , and since \( {\varphi }_{i}\left( 0\right) = \frac{\partial f}{\partial {x}_{i}}\left( 0\right) \) , we deduce

\[
L\left( f\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}L\left( {x}_{i}\right) \frac{\partial f}{\partial {x}_{i}}\left( 0\right) .
\]

En notant \( \xi = \left( {L\left( {x}_{1}\right) ,\ldots , L\left( {x}_{n}\right) }\right) \) , ceci s’écrit aussi \( L\left( f\right) = {f}_{\xi }^{\prime }\left( 0\right) = d{f}_{0}\left( \xi \right) \) , et ceci pour tout \( f \in {G}_{0}^{\infty } \) , d’où le résultat.

> By denoting \( \xi = \left( {L\left( {x}_{1}\right) ,\ldots , L\left( {x}_{n}\right) }\right) \) , this is also written \( L\left( f\right) = {f}_{\xi }^{\prime }\left( 0\right) = d{f}_{0}\left( \xi \right) \) , and this for all \( f \in {G}_{0}^{\infty } \) , hence the result.

Problem 3. Soit \( n \in {\mathbb{N}}^{ * } \) et \( f : \mathbb{R} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{\infty } \) . Donner une condition nécéssaire et suffisante sur \( f \) pour que la fonction \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}X \mapsto f\left( {\parallel X{\parallel }^{2}}\right) X \) , où \( \parallel X\parallel \) désigne la norme euclidienne canonique de \( X \) sur \( {\mathbb{R}}^{n} \) , soit un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( {\mathbb{R}}^{n} \) sur lui même.

> Problem 3. Let \( n \in {\mathbb{N}}^{ * } \) and \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{\infty } \) . Give a necessary and sufficient condition on \( f \) for the function \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}X \mapsto f\left( {\parallel X{\parallel }^{2}}\right) X \) , where \( \parallel X\parallel \) denotes the canonical Euclidean norm of \( X \) on \( {\mathbb{R}}^{n} \) , to be a \( {\mathcal{C}}^{\infty } \) diffeomorphism of \( {\mathbb{R}}^{n} \) onto itself.

Solution. Considérons la fonction \( g : \mathbb{R} \rightarrow \mathbb{R},\;x \mapsto {xf}\left( {x}^{2}\right) \) , de classe \( {\mathcal{C}}^{\infty } \) .

> Solution. Consider the function \( g : \mathbb{R} \rightarrow \mathbb{R},\;x \mapsto {xf}\left( {x}^{2}\right) \) , of class \( {\mathcal{C}}^{\infty } \) .

Supposons que \( F \) soit un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) . En notant \( {e}_{1} = \left( {1,0,\ldots ,0}\right) \in \; {\mathbb{R}}^{n} \) , on a \( F\left( {x{e}_{1}}\right) = g\left( x\right) {e}_{1} \) pour tout réel \( x \) . En dérivant par rapport à \( x \) on obtient \( \partial F/\partial {x}_{1}\left( {x{e}_{1}}\right) = \; {g}^{\prime }\left( x\right) {e}_{1} \) , donc \( {g}^{\prime }\left( x\right) \neq 0 \) . Par ailleurs, \( F\left( {\mathbb{R}}^{n}\right) = {\mathbb{R}}^{n} \) donc pour tout \( y \in \mathbb{R} \) il existe \( X \in {\mathbb{R}}^{n} \) tel que \( F\left( X\right) = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) X = y{e}_{1} \) . On en déduit que seule la première coordonnée \( {x}_{1} \) de \( X \) n’est pas nulle, donc \( X = {x}_{1}{e}_{1} \) d’où \( f\left( {x}_{1}^{2}\right) {x}_{1}{e}_{1} = y{e}_{1} \) , ce qui entraîne \( y = g\left( {x}_{1}\right) \) . Ainsi \( g \) est une surjection de \( \mathbb{R} \) sur \( \mathbb{R} \) . De plus \( {g}^{\prime } \neq 0 \) sur \( \mathbb{R} \) , on en déduit que \( g \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( \mathbb{R} \) sur \( \mathbb{R} \) .

> Suppose that \( F \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \). Denoting \( {e}_{1} = \left( {1,0,\ldots ,0}\right) \in \; {\mathbb{R}}^{n} \), we have \( F\left( {x{e}_{1}}\right) = g\left( x\right) {e}_{1} \) for any real number \( x \). Differentiating with respect to \( x \) yields \( \partial F/\partial {x}_{1}\left( {x{e}_{1}}\right) = \; {g}^{\prime }\left( x\right) {e}_{1} \), thus \( {g}^{\prime }\left( x\right) \neq 0 \). Furthermore, \( F\left( {\mathbb{R}}^{n}\right) = {\mathbb{R}}^{n} \) so for any \( y \in \mathbb{R} \) there exists \( X \in {\mathbb{R}}^{n} \) such that \( F\left( X\right) = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) X = y{e}_{1} \). We deduce that only the first coordinate \( {x}_{1} \) of \( X \) is non-zero, thus \( X = {x}_{1}{e}_{1} \) whence \( f\left( {x}_{1}^{2}\right) {x}_{1}{e}_{1} = y{e}_{1} \), which implies \( y = g\left( {x}_{1}\right) \). Thus \( g \) is a surjection from \( \mathbb{R} \) onto \( \mathbb{R} \). Moreover \( {g}^{\prime } \neq 0 \) on \( \mathbb{R} \), we deduce that \( g \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism from \( \mathbb{R} \) onto \( \mathbb{R} \).

Supposons maintenant que \( g \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( \mathbb{R} \) sur \( \mathbb{R} \) et montrons que \( F \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) . Remarquons déjà que \( f \) ne s’annule pas sur \( {\mathbb{R}}^{ + } \) , car \( f\left( 0\right) = {g}^{\prime }\left( 0\right) \neq 0 \) , et pour \( x > 0, g\left( x\right) \neq g\left( {-x}\right) \) donc \( {xf}\left( {x}^{2}\right) \neq - {xf}\left( {x}^{2}\right) \) ce qui entraîne \( f\left( {x}^{2}\right) \neq 0 \) . Quitte à changer \( f \) par \( - f \) , on peut même supposer \( f > 0 \) sur \( {\mathbb{R}}^{ + } \) .

> Now suppose that \( g \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism from \( \mathbb{R} \) onto \( \mathbb{R} \) and let us show that \( F \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \). Note first that \( f \) does not vanish on \( {\mathbb{R}}^{ + } \), because \( f\left( 0\right) = {g}^{\prime }\left( 0\right) \neq 0 \), and for \( x > 0, g\left( x\right) \neq g\left( {-x}\right) \) thus \( {xf}\left( {x}^{2}\right) \neq - {xf}\left( {x}^{2}\right) \) which implies \( f\left( {x}^{2}\right) \neq 0 \). Up to replacing \( f \) by \( - f \), we can even assume \( f > 0 \) on \( {\mathbb{R}}^{ + } \).

Montrons que \( F \) est injective. Supposons \( F\left( X\right) = F\left( Y\right) \) pour deux vecteurs \( X, Y \in {\mathbb{R}}^{n} \) . Si \( X = Y = 0 \) on a bien \( X = Y \) , sinon l’un des deux est non nul, par exemple \( X \neq 0 \) . On a \( f\left( {\parallel {X}^{2}\parallel }\right) X = f\left( \begin{Vmatrix}{Y}^{2}\end{Vmatrix}\right) Y \) , et comme \( f \) ne s’annule pas on a \( Y = {\lambda X} \) avec \( \lambda = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) /f\left( \begin{Vmatrix}{Y}^{2}\end{Vmatrix}\right) \) . On en déduit \( f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) X = f\left( {{\lambda }^{2}\begin{Vmatrix}{X}^{2}\end{Vmatrix}}\right) {\lambda X} \) . Ceci entraîne \( g\left( {\parallel X\parallel }\right) = g\left( {\lambda \parallel X\parallel }\right) \) , d’où \( \parallel X\parallel = \lambda \parallel X\parallel \) par injectivité de \( g \) , donc \( \lambda = 1 \) car \( \parallel X\parallel \neq 0 \) , donc \( Y = X \) .

> Let us show that \( F \) is injective. Suppose \( F\left( X\right) = F\left( Y\right) \) for two vectors \( X, Y \in {\mathbb{R}}^{n} \) . If \( X = Y = 0 \) we indeed have \( X = Y \) , otherwise one of the two is non-zero, for example \( X \neq 0 \) . We have \( f\left( {\parallel {X}^{2}\parallel }\right) X = f\left( \begin{Vmatrix}{Y}^{2}\end{Vmatrix}\right) Y \) , and since \( f \) does not vanish we have \( Y = {\lambda X} \) with \( \lambda = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) /f\left( \begin{Vmatrix}{Y}^{2}\end{Vmatrix}\right) \) . We deduce \( f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) X = f\left( {{\lambda }^{2}\begin{Vmatrix}{X}^{2}\end{Vmatrix}}\right) {\lambda X} \) . This implies \( g\left( {\parallel X\parallel }\right) = g\left( {\lambda \parallel X\parallel }\right) \) , hence \( \parallel X\parallel = \lambda \parallel X\parallel \) by injectivity of \( g \) , therefore \( \lambda = 1 \) because \( \parallel X\parallel \neq 0 \) , so \( Y = X \) .

La fonction \( F \) est surjective. En effet, si \( Y \in {\mathbb{R}}^{n} \) , on peut trouver \( x \in \mathbb{R} \) tel que \( g\left( x\right) = \parallel Y\parallel \) . En notant \( \lambda = x/\parallel Y\parallel \) on en déduit \( F\left( {\lambda Y}\right) = f\left( {x}^{2}\right) \left( {x/\parallel Y\parallel }\right) Y = \left( {g\left( x\right) /\parallel Y\parallel }\right) Y = Y \) .

> The function \( F \) is surjective. Indeed, if \( Y \in {\mathbb{R}}^{n} \) , we can find \( x \in \mathbb{R} \) such that \( g\left( x\right) = \parallel Y\parallel \) . By noting \( \lambda = x/\parallel Y\parallel \) we deduce \( F\left( {\lambda Y}\right) = f\left( {x}^{2}\right) \left( {x/\parallel Y\parallel }\right) Y = \left( {g\left( x\right) /\parallel Y\parallel }\right) Y = Y \) .

La fonction \( F \) est clairement de classe \( {\mathcal{C}}^{\infty } \) et il reste à montrer que la différentielle de \( F \) est inversible en tout point \( X \) . La matrice jacobienne \( {J}_{X} \) de \( F \) en \( X = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) vérifie \( {J}_{X} = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) avec \( {m}_{i, j} = 2{x}_{i}{x}_{j}{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \) si \( i \neq j \) et \( {m}_{i, i} = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) + 2{x}_{i}^{2}{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \) . Autrement dit, \( {J}_{X} = f\left( {\parallel X{\parallel }^{2}}\right) {I}_{n} + 2{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) {X}^{t}X \) . La matrice jacobienne \( {J}_{X} \) est symétrique et on va montrer qu’elle est définie positive. Pour tout vecteur \( V \in {\mathbb{R}}^{n} \) non nul, on a

> The function \( F \) is clearly of class \( {\mathcal{C}}^{\infty } \) and it remains to show that the differential of \( F \) is invertible at every point \( X \) . The Jacobian matrix \( {J}_{X} \) of \( F \) at \( X = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) satisfies \( {J}_{X} = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \) with \( {m}_{i, j} = 2{x}_{i}{x}_{j}{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \) if \( i \neq j \) and \( {m}_{i, i} = f\left( \begin{Vmatrix}{X}^{2}\end{Vmatrix}\right) + 2{x}_{i}^{2}{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \) . In other words, \( {J}_{X} = f\left( {\parallel X{\parallel }^{2}}\right) {I}_{n} + 2{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) {X}^{t}X \) . The Jacobian matrix \( {J}_{X} \) is symmetric and we will show that it is positive definite. For any non-zero vector \( V \in {\mathbb{R}}^{n} \) , we have

\[
{}^{t}V{J}_{X}V = f{\left( \parallel X{\parallel }^{2}\right) }^{t}{VV} + 2{f}^{\prime }{\left( \parallel X{\parallel }^{2}\right) }^{t}{\left( {}^{t}XV\right) }^{\prime }\left( {{}^{t}{XV}}\right)  = f\left( {\parallel X{\parallel }^{2}}\right) \parallel V{\parallel }^{2} + 2{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) {\left( {}^{t}XV\right) }^{2}.
\]

(*)

> Si \( {f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \geq 0 \) , alors cette expression est \( > 0 \) . Sinon \( {f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) < 0 \) . Comme \( {g}^{\prime } \) ne s’annule pas, elle garde le signe de \( {g}^{\prime }\left( 0\right) = f\left( 0\right) > 0 \) , donc \( {g}^{\prime }\left( x\right) = f\left( {x}^{2}\right) + 2{x}^{2}{f}^{\prime }\left( {x}^{2}\right) > 0 \) . Or d’après l’inégalité de Schwarz on a \( {\left( {}^{t}XV\right) }^{2} \leq \parallel X{\parallel }^{2} \cdot \parallel V{\parallel }^{2} \) , donc d’après (*)

If \( {f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) \geq 0 \) , then this expression is \( > 0 \) . Otherwise \( {f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) < 0 \) . Since \( {g}^{\prime } \) does not vanish, it maintains the sign of \( {g}^{\prime }\left( 0\right) = f\left( 0\right) > 0 \) , therefore \( {g}^{\prime }\left( x\right) = f\left( {x}^{2}\right) + 2{x}^{2}{f}^{\prime }\left( {x}^{2}\right) > 0 \) . However, according to the Schwarz inequality we have \( {\left( {}^{t}XV\right) }^{2} \leq \parallel X{\parallel }^{2} \cdot \parallel V{\parallel }^{2} \) , so according to (*)

\[
{}^{t}V{J}_{X}V \geq  f\left( {\parallel X{\parallel }^{2}}\right) \parallel V{\parallel }^{2} - 2\left| {{f}^{\prime }\left( {\parallel X{\parallel }^{2}}\right) }\right| \parallel X{\parallel }^{2} \cdot  \parallel V{\parallel }^{2} = {g}^{\prime }\left( {\parallel X\parallel }\right) \begin{Vmatrix}{V}^{2}\end{Vmatrix} > 0.
\]

Ainsi \( {J}_{X} \) est définie positive, donc inversible. On a donc prouvé que \( F \) est un \( {\mathcal{C}}^{\infty } \) difféomorphisme de \( {\mathbb{R}}^{n} \) sur lui même.

> Thus \( {J}_{X} \) is positive definite, and therefore invertible. We have thus proven that \( F \) is a \( {\mathcal{C}}^{\infty } \) diffeomorphism of \( {\mathbb{R}}^{n} \) onto itself.

Problem 4 (FONCTIONS CONVEXES SUR \( {\mathbb{R}}^{n} \) ). On munit \( {\mathbb{R}}^{n} \) de son produit scalaire \( \langle \) , \( \rangle \) standard et de la norme euclidienne associée. Soit \( C \) un ouvert convexe de \( {\mathbb{R}}^{n} \) . Une application \( J : C \rightarrow \mathbb{R} \) est dite \( \alpha \) -convexe (avec \( \alpha \geq 0 \) ) si

> Problem 4 (CONVEX FUNCTIONS ON \( {\mathbb{R}}^{n} \) ). We equip \( {\mathbb{R}}^{n} \) with its standard \( \langle \) , \( \rangle \) scalar product and the associated Euclidean norm. Let \( C \) be a convex open set of \( {\mathbb{R}}^{n} \) . A mapping \( J : C \rightarrow \mathbb{R} \) is said to be \( \alpha \) -convex (with \( \alpha \geq 0 \) ) if

\[
\forall x, y \in  C,\forall \delta  \in  \left\lbrack  {0,1}\right\rbrack  ,\;J\left\lbrack  {\left( {1 - \delta }\right) x + {\delta y}}\right\rbrack   \leq  \left( {1 - \delta }\right) J\left( x\right)  + {\delta J}\left( y\right)  - \frac{\alpha }{2}\delta \left( {1 - \delta }\right) \parallel x - y{\parallel }^{2}.
\]

(*)

> Si \( J \) est 0-convexe, on dit que \( J \) est convexe.

If \( J \) is 0-convex, we say that \( J \) is convex.

> 1 / Montrer que toute fonction convexe \( J : \;C \rightarrow \mathbb{R} \) est continue, et dérivable en tout point de \( C \) par rapport à tout vecteur.

1 / Show that any convex function \( J : \;C \rightarrow \mathbb{R} \) is continuous, and differentiable at every point of \( C \) with respect to any vector.

> 2 / Soit \( J : C \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{2} \) . Pour tout \( x \in C \) , on note \( {J}^{\prime }\left( x\right) \) le gradient de \( J \) en \( x \) et \( {J}^{\prime \prime }\left( x\right) \) la matrice hessienne de \( J \) en \( x \) , définie par \( {J}^{\prime \prime }\left( x\right) = {\left( \frac{{\partial }^{2}J}{\partial {x}_{i}\partial {x}_{j}}\left( x\right) \right) }_{1 \leq i, j \leq n} \) . Montrer que \( J \) est \( \alpha \) -convexe si et seulement si l’une des conditions suivantes est réalisée :

2 / Let \( J : C \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{2} \) class mapping. For any \( x \in C \) , we denote by \( {J}^{\prime }\left( x\right) \) the gradient of \( J \) at \( x \) and by \( {J}^{\prime \prime }\left( x\right) \) the Hessian matrix of \( J \) at \( x \) , defined by \( {J}^{\prime \prime }\left( x\right) = {\left( \frac{{\partial }^{2}J}{\partial {x}_{i}\partial {x}_{j}}\left( x\right) \right) }_{1 \leq i, j \leq n} \) . Show that \( J \) is \( \alpha \) -convex if and only if one of the following conditions is met:

> (i) pour tout \( \left( {x, y}\right) \in {C}^{2}, J\left( y\right) \geq J\left( x\right) + \left\langle {{J}^{\prime }\left( x\right) , y - x}\right\rangle + \frac{\alpha }{2}\parallel y - x{\parallel }^{2} \) ;

(i) for all \( \left( {x, y}\right) \in {C}^{2}, J\left( y\right) \geq J\left( x\right) + \left\langle {{J}^{\prime }\left( x\right) , y - x}\right\rangle + \frac{\alpha }{2}\parallel y - x{\parallel }^{2} \) ;

> (ii) pour tout \( \left( {x, y}\right) \in {C}^{2},\left\langle {{J}^{\prime }\left( y\right) - {J}^{\prime }\left( x\right) , y - x}\right\rangle \geq \alpha \parallel y - x{\parallel }^{2} \) ;

(ii) for all \( \left( {x, y}\right) \in {C}^{2},\left\langle {{J}^{\prime }\left( y\right) - {J}^{\prime }\left( x\right) , y - x}\right\rangle \geq \alpha \parallel y - x{\parallel }^{2} \) ;

> (iii) pour tout \( x \in C \) , pour tout \( w \in {\mathbb{R}}^{n},\left\langle {{J}^{\prime \prime }\left( x\right) w, w}\right\rangle \geq \alpha \parallel w{\parallel }^{2} \) .

(iii) for all \( x \in C \) , for all \( w \in {\mathbb{R}}^{n},\left\langle {{J}^{\prime \prime }\left( x\right) w, w}\right\rangle \geq \alpha \parallel w{\parallel }^{2} \) .

> 3/ (Optimisation dans \( {\mathbb{R}}^{n} \) ) Soit \( J : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction \( \alpha \) -convexe (avec \( \alpha > 0 \) ).

3/ (Optimization in \( {\mathbb{R}}^{n} \) ) Let \( J : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a \( \alpha \) -convex function (with \( \alpha > 0 \) ).

> a) Montrer qu’il existe \( {x}_{0} \in {\mathbb{R}}^{n} \) tel que \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in {\mathbb{R}}^{n}}}J\left( x\right) \) .

a) Show that there exists \( {x}_{0} \in {\mathbb{R}}^{n} \) such that \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in {\mathbb{R}}^{n}}}J\left( x\right) \) .

> b) \( \mathrm{{Si}}\left( {u}_{n}\right) \) est une suite minimisante (i.e. si \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}J\left( {u}_{n}\right) = J\left( {x}_{0}\right) \) ), montrer que \( \left( {u}_{n}\right) \) converge vers \( {x}_{0} \) .

b) \( \mathrm{{Si}}\left( {u}_{n}\right) \) is a minimizing sequence (i.e. if \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}J\left( {u}_{n}\right) = J\left( {x}_{0}\right) \) ), show that \( \left( {u}_{n}\right) \) converges to \( {x}_{0} \) .

> Solution. 1/ Soit \( {x}_{0} \in C \) . Commençons par montrer que \( J \) est dérivable selon tout vecteur en \( {x}_{0} \) . Soit un vecteur \( \xi \in {\mathbb{R}}^{n} \) , et l’application de la variable réelle \( \varphi : t \mapsto J\left( {{x}_{0} + {t\xi }}\right) \) . Cette application est définie sur un voisinage de 0 dans \( \mathbb{R} \) , et elle de plus convexe car \( J \) est convexe. On sait donc, d'après la théorie des fonctions convexes de la variable réelle, que \( \varphi \) est dérivable à droite en0, c’est-à-dire que \( J \) est dérivable selon le vecteur \( \xi \) en \( {x}_{0} \) .

Solution. 1/ Let \( {x}_{0} \in C \) . Let us begin by showing that \( J \) is differentiable along any vector at \( {x}_{0} \) . Let \( \xi \in {\mathbb{R}}^{n} \) be a vector, and consider the mapping of the real variable \( \varphi : t \mapsto J\left( {{x}_{0} + {t\xi }}\right) \) . This mapping is defined on a neighborhood of 0 in \( \mathbb{R} \) , and it is furthermore convex because \( J \) is convex. We therefore know, from the theory of convex functions of a real variable, that \( \varphi \) is differentiable from the right at 0, which means that \( J \) is differentiable along the vector \( \xi \) at \( {x}_{0} \) .

> Prouvons maintenant la continuité de \( J \) en \( {x}_{0} \) (attention, ce n’est pas parce que \( J \) est dérivable selon tout vecteur en \( {x}_{0} \) qu’elle y est continue - voir un contre exemple à l’exercice 1 page 329). Quitte à considérer la fonction \( J\left( {x + {x}_{0}}\right) - J\left( {x}_{0}\right) \) , on peut supposer \( {x}_{0} = 0 \) et \( J\left( 0\right) = 0 \) .

Let us now prove the continuity of \( J \) at \( {x}_{0} \) (note: \( J \) being differentiable along every vector at \( {x}_{0} \) does not imply it is continuous there - see a counterexample in exercise 1 on page 329). By considering the function \( J\left( {x + {x}_{0}}\right) - J\left( {x}_{0}\right) \) instead, we can assume \( {x}_{0} = 0 \) and \( J\left( 0\right) = 0 \) .

> La norme sur \( {\mathbb{R}}^{n} \) utilisée dans la suite de cette question sera \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{1} = \mathop{\sum }\limits_{i}\left| {x}_{i}\right| \) . L’ensemble \( C \) est ouvert, donc il existe \( \rho > 0 \) tel que la boule \( \mathrm{B}\left( {0,\rho }\right) \) soit incluse dans \( C \) . Quitte à considérer la fonction \( J\left( {{\rho x}/2}\right) \) , on peut même supposer \( \rho = 2 \) , de sorte que la boule unité fermée est incluse dans \( C \) .

The norm on \( {\mathbb{R}}^{n} \) used in the remainder of this question will be \( {\begin{Vmatrix}\left( {x}_{1},\ldots ,{x}_{n}\right) \end{Vmatrix}}_{1} = \mathop{\sum }\limits_{i}\left| {x}_{i}\right| \) . The set \( C \) is open, so there exists \( \rho > 0 \) such that the ball \( \mathrm{B}\left( {0,\rho }\right) \) is included in \( C \) . By considering the function \( J\left( {{\rho x}/2}\right) \) instead, we can even assume \( \rho = 2 \) , so that the closed unit ball is included in \( C \) .

> Commençons par montrer que \( J \) est majorée sur la sphère unité. Notons \( \left( {e}_{i}\right) \) la base cano-nique de \( {\mathbb{R}}^{n} \) et considérons \( u = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) tel que \( \parallel u\parallel = 1 \) . Pour tout \( i \) , il existe \( {\varepsilon }_{i} \in \{ - 1,1\} \) tel que \( {x}_{i} = \left| {x}_{i}\right| {\varepsilon }_{i} \) . Comme \( \parallel u\parallel = \mathop{\sum }\limits_{i}\left| {x}_{i}\right| = 1 \) , on a facilement (comme pour les fonctions convexes à variables réelles)

Let us begin by showing that \( J \) is bounded on the unit sphere. Let \( \left( {e}_{i}\right) \) denote the canonical basis of \( {\mathbb{R}}^{n} \) and consider \( u = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) such that \( \parallel u\parallel = 1 \) . For any \( i \) , there exists \( {\varepsilon }_{i} \in \{ - 1,1\} \) such that \( {x}_{i} = \left| {x}_{i}\right| {\varepsilon }_{i} \) . Since \( \parallel u\parallel = \mathop{\sum }\limits_{i}\left| {x}_{i}\right| = 1 \) , we easily have (as for convex functions of real variables)

\[
J\left( u\right)  = J\left( {\mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right| {\varepsilon }_{i}{e}_{i}}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right| J\left( {{\varepsilon }_{i}{e}_{i}}\right)  \leq  M\mathop{\sum }\limits_{{i = 1}}^{n}\left| {x}_{i}\right|  = M,\;\text{ avec }\;M = \mathop{\sup }\limits_{\substack{{1 \leq  i \leq  n} \\  {\varepsilon  \in  \{  - 1,1\} } }}J\left( {\varepsilon {e}_{i}}\right) .
\]

Achevons la démonstration. Soit \( x \in C,0 < \parallel x\parallel \leq 1 \) , et soit \( u = x/\parallel x\parallel \) . La fonction \( \psi : \left\lbrack {-1,1}\right\rbrack \rightarrow \mathbb{R}\;\lambda \mapsto J\left( {\lambda u}\right) \) est une fonction de la variable réelle convexes ur \( \left\lbrack {-1,1}\right\rbrack \) , donc

> Let us complete the proof. Let \( x \in C,0 < \parallel x\parallel \leq 1 \) , and let \( u = x/\parallel x\parallel \) . The function \( \psi : \left\lbrack {-1,1}\right\rbrack \rightarrow \mathbb{R}\;\lambda \mapsto J\left( {\lambda u}\right) \) is a convex function of the real variable on \( \left\lbrack {-1,1}\right\rbrack \) , therefore

\[
\forall \lambda  \in  \left\lbrack  {-1,1}\right\rbrack  ,\lambda  \neq  0,\;\psi \left( 0\right)  - \psi \left( {-1}\right)  \leq  \frac{\psi \left( \lambda \right)  - \psi \left( 0\right) }{\lambda } \leq  \psi \left( 1\right)  - \psi \left( 0\right) ,
\]

ce qui s'écrit aussi

> which can also be written as

\[
\forall \lambda  \in  \left\lbrack  {-1,1}\right\rbrack  ,\lambda  \neq  0,\; - J\left( {-u}\right)  \leq  \frac{J\left( {\lambda u}\right) }{\lambda } \leq  J\left( u\right) \;\text{ donc }\; - M \leq  \frac{J\left( {\lambda u}\right) }{\lambda } \leq  M.
\]

Ainsi, \( \left| {J\left( x\right) }\right| = \left| {J\left( {\parallel x\parallel u}\right) }\right| \leq M\parallel x\parallel \) . Comme \( J\left( 0\right) = 0 \) , on en déduit la continuité de \( J \) en 0 . 2/ \( \left( {J\text{ est }\alpha \text{ -convexe }}\right) \Leftrightarrow \left( i\right) \) :

> Thus, \( \left| {J\left( x\right) }\right| = \left| {J\left( {\parallel x\parallel u}\right) }\right| \leq M\parallel x\parallel \) . Since \( J\left( 0\right) = 0 \) , we deduce the continuity of \( J \) at 0 . 2/ \( \left( {J\text{ est }\alpha \text{ -convexe }}\right) \Leftrightarrow \left( i\right) \) :

- Supposons \( {J\alpha } \) -convexe. Soient \( \left. {\left. {\left( {x, y}\right)  \in  {\mathbb{C}}^{2}\text{ et }\delta  \in  }\right\rbrack  0,1}\right\rbrack \) . L’inégalité (*) s’écrit encore

> - Suppose \( {J\alpha } \) -convex. Let \( \left. {\left. {\left( {x, y}\right)  \in  {\mathbb{C}}^{2}\text{ et }\delta  \in  }\right\rbrack  0,1}\right\rbrack \) . The inequality (*) can also be written as

\[
\frac{J\left( {x + \delta \left( {y - x}\right) }\right)  - J\left( x\right) }{\delta } \leq  J\left( y\right)  - J\left( x\right)  - \frac{\alpha }{2}\left( {1 - \delta }\right) \parallel y - x{\parallel }^{2},
\]

d’où (i) en faisant tendre \( \delta \) vers 0 .

> whence (i) by letting \( \delta \) tend to 0 .

- Inversement, supposons (i) vérifié. Écrivons (i) pour le couple \( \left( {y, x + \delta \left( {y - x}\right) }\right) \) puis pour le couple \( \left( {x, x + \delta \left( {y - x}\right) }\right) \) , avec \( \delta  \in  \left\lbrack  {0,1}\right\rbrack \)

> - Conversely, suppose (i) is satisfied. Let us write (i) for the pair \( \left( {y, x + \delta \left( {y - x}\right) }\right) \) then for the pair \( \left( {x, x + \delta \left( {y - x}\right) }\right) \) , with \( \delta  \in  \left\lbrack  {0,1}\right\rbrack \)

\[
J\left( y\right)  \geq  J\left( {x + \delta \left( {y - x}\right) }\right)  + \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) ,\left( {1 - \delta }\right) \left( {y - x}\right) }\right\rangle   + \frac{\alpha }{2}{\left( 1 - \delta \right) }^{2}\parallel y - x{\parallel }^{2},
\]

\[
J\left( x\right)  \geq  J\left( {x + \delta \left( {y - x}\right) }\right)  + \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) , - \delta \left( {y - x}\right) }\right\rangle   + \frac{\alpha }{2}{\delta }^{2}\parallel y - x{\parallel }^{2}.
\]

En multipliant la première inégalité par \( \delta \) , la seconde par \( 1 - \delta \) , puis en additionnant, il vient

> By multiplying the first inequality by \( \delta \) , the second by \( 1 - \delta \) , then adding them, we get

\[
{\delta J}\left( y\right)  + \left( {1 - \delta }\right) J\left( x\right)  \geq  J\left( {x + \delta \left( {y - x}\right) }\right)  + \frac{\alpha }{2}\delta \left( {1 - \delta }\right) \parallel y - x{\parallel }^{2},
\]

donc \( J \) est \( \alpha \) -convexe.

> therefore \( J \) is \( \alpha \) -convex.

\( \left( i\right) \Leftrightarrow \left( {ii}\right) \) .

> — Supposons (i) vraie. En écrivant l’inégalité (i) pour le couple \( \left( {x, y}\right) \) , pour le couple \( \left( {y, x}\right) \) , puis en additionnant, on obtient (ii).

— Suppose (i) is true. By writing inequality (i) for the pair \( \left( {x, y}\right) \) , for the pair \( \left( {y, x}\right) \) , then adding them, we obtain (ii).

> - Supposons (ii) vérifiée. Si on fixe \( \left( {x, y}\right)  \in  {C}^{2} \) , la fonction \( \varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;\delta  \mapsto  J(x + \; \delta \left( {y - x}\right) ) \) a pour dérivée \( {\varphi }^{\prime }\left( \delta \right)  = \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) , y - x}\right\rangle \) et vérifie donc

- Suppose (ii) is satisfied. If we fix \( \left( {x, y}\right)  \in  {C}^{2} \) , the function \( \varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;\delta  \mapsto  J(x + \; \delta \left( {y - x}\right) ) \) has derivative \( {\varphi }^{\prime }\left( \delta \right)  = \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) , y - x}\right\rangle \) and therefore satisfies

\[
\forall \delta  \in  \rbrack 0,1\rbrack ,\;{\varphi }^{\prime }\left( \delta \right)  - {\varphi }^{\prime }\left( 0\right)  = \frac{1}{\delta }\left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right)  - {J}^{\prime }\left( x\right) ,\delta \left( {y - x}\right) }\right\rangle   \geq  \alpha \parallel y - x{\parallel }^{2}\delta ,
\]

(inégalité qui reste évidemment vraie pour \( \delta = 0 \) ) d’où (i) car par intégration, on obtient

> (an inequality that obviously remains true for \( \delta = 0 \) ) hence (i) because by integration, we obtain

\[
\varphi \left( 1\right)  \geq  {\int }_{0}^{1}\left( {{\varphi }^{\prime }\left( 0\right)  + \alpha \parallel y - x{\parallel }^{2}\delta }\right) {d\delta } = \varphi \left( 0\right)  + {\varphi }^{\prime }\left( 0\right)  + \frac{\alpha }{2}\parallel y - x{\parallel }^{2}.
\]

(ii) \( \Leftrightarrow \) (iii).

> (ii) \( \Leftrightarrow \) (iii).

— Supposons (ii) vérifiée. Soit \( w \in {\mathbb{R}}^{n} \) . Lorsque \( \rho \) est un nombre réel non nul suffisamment proche de 0, on a d'après (ii)

> — Suppose (ii) is satisfied. Let \( w \in {\mathbb{R}}^{n} \) . When \( \rho \) is a non-zero real number sufficiently close to 0, we have according to (ii)

\[
\left\langle  {{J}^{\prime }\left( {x + {\rho w}}\right)  - {J}^{\prime }\left( x\right) ,{\rho w}}\right\rangle   \geq  \alpha {\rho }^{2}\parallel w{\parallel }^{2}\text{ ou encore }\left\langle  {\frac{{J}^{\prime }\left( {x + {\rho w}}\right)  - {J}^{\prime }\left( x\right) }{\rho }, w}\right\rangle   \geq  \alpha \parallel w{\parallel }^{2},
\]

d’où (iii) en faisant tendre \( \rho \) vers 0 (remarquer que \( {J}^{\prime \prime }\left( x\right) \) est la matrice jacobienne de \( x \mapsto {J}^{\prime }\left( x\right) ) \) .

> hence (iii) by letting \( \rho \) tend to 0 (note that \( {J}^{\prime \prime }\left( x\right) \) is the Jacobian matrix of \( x \mapsto {J}^{\prime }\left( x\right) ) \) .

- Supposons (iii) vérifiée. Fixons \( \left( {x, y}\right)  \in  {C}^{2} \) , et considérons la fonction \( \psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R} \) définie par \( \psi \left( x\right)  = \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) , y - x}\right\rangle  \rangle \) . On a

> - Suppose (iii) is satisfied. Let us fix \( \left( {x, y}\right)  \in  {C}^{2} \) , and consider the function \( \psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R} \) defined by \( \psi \left( x\right)  = \left\langle  {{J}^{\prime }\left( {x + \delta \left( {y - x}\right) }\right) , y - x}\right\rangle  \rangle \) . We have

\[
\forall \delta  \in  \left\lbrack  {0,1}\right\rbrack  ,\;{\psi }^{\prime }\left( \delta \right)  = \left\langle  {{J}^{\prime \prime }\left( {x + \delta \left( {y - x}\right) }\right) \left( {y - x}\right) , y - x}\right\rangle   \geq  \alpha \parallel y - x{\parallel }^{2},
\]

donc par intégration \( \psi \left( 1\right) - \psi \left( 0\right) \geq \alpha \parallel y - x{\parallel }^{2} \) , d’où (ii).

> therefore by integration \( \psi \left( 1\right) - \psi \left( 0\right) \geq \alpha \parallel y - x{\parallel }^{2} \) , hence (ii).

3 / a) L’inégalité d’ \( \alpha \) -convexité, appliquée avec \( x = 0 \) donne

> 3 / a) The \( \alpha \) -convexity inequality, applied with \( x = 0 \) gives

\[
\forall y \in  {\mathbb{R}}^{n},\forall \delta  \in  \left\lbrack  {0,1}\right\rbrack  ,\;J\left( {\delta y}\right)  \leq  \left( {1 - \delta }\right) J\left( 0\right)  + {\delta J}\left( y\right)  - \frac{\alpha }{2}\delta \left( {1 - \delta }\right) \parallel y{\parallel }^{2}
\]

ce qui s'écrit encore

> which can also be written

\[
\left. {\forall y \in  {\mathbb{R}}^{n},\forall \delta  \in  \rbrack 0,1\rbrack ,\;J\left( y\right)  \geq  J\left( 0\right)  + \frac{J\left( {\delta y}\right)  - J\left( 0\right) }{\delta } + \frac{\alpha }{2}\left( {1 - \delta }\right) \parallel y{\parallel }^{2}.}\right\rbrack
\]

En appliquant cette dernière inégalité aux \( y \) tels que \( \parallel y\parallel \geq 2 \) avec \( \delta = 1/\parallel y\parallel \) , on a

> By applying this last inequality to the \( y \) such that \( \parallel y\parallel \geq 2 \) with \( \delta = 1/\parallel y\parallel \) , we have

\[
J\left( y\right)  \geq  J\left( 0\right)  + \left\lbrack  {J\left( \frac{y}{\parallel y\parallel }\right)  - J\left( 0\right) }\right\rbrack  \parallel y\parallel  + \frac{\alpha }{2}\left( {1 - \frac{1}{\parallel y\parallel }}\right) \parallel y{\parallel }^{2} \geq  J\left( 0\right)  + K\parallel y\parallel  + \frac{\alpha }{4}\parallel y{\parallel }^{2},
\]

où \( K \) est un minorant de \( J\left( u\right) - J\left( 0\right) \) sur la sphère unité \( (K \) existe car \( J \) est continue et la sphère unité est compacte). On en déduit \( \mathop{\lim }\limits_{{\parallel y\parallel \rightarrow + \infty }}J\left( y\right) = + \infty \) .

> where \( K \) is a lower bound of \( J\left( u\right) - J\left( 0\right) \) on the unit sphere \( (K \) exists because \( J \) is continuous and the unit sphere is compact). We deduce \( \mathop{\lim }\limits_{{\parallel y\parallel \rightarrow + \infty }}J\left( y\right) = + \infty \) .

Ainsi, l’ensemble \( \Gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid J\left( x\right) \leq J\left( 0\right) }\right\} \) est borné. Or \( \Gamma \) est fermé ( \( J \) est continue), donc \( \Gamma \subset {\mathbb{R}}^{n} \) est compact. Il existe donc \( {x}_{0} \in \Gamma \) tel que \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in \Gamma }}J\left( x\right) \) (ceci car \( J \) est continue). Par construction de \( \Gamma \) , on a \( J\left( x\right) \geq J\left( {x}_{0}\right) \) pour tout \( x \in {\mathbb{R}}^{n} \) , donc \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in {\mathbb{R}}^{n}}}J\left( x\right) \) .

> Thus, the set \( \Gamma = \left\{ {x \in {\mathbb{R}}^{n} \mid J\left( x\right) \leq J\left( 0\right) }\right\} \) is bounded. Now \( \Gamma \) is closed (\( J \) is continuous), so \( \Gamma \subset {\mathbb{R}}^{n} \) is compact. There therefore exists \( {x}_{0} \in \Gamma \) such that \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in \Gamma }}J\left( x\right) \) (this is because \( J \) is continuous). By construction of \( \Gamma \), we have \( J\left( x\right) \geq J\left( {x}_{0}\right) \) for all \( x \in {\mathbb{R}}^{n} \), so \( J\left( {x}_{0}\right) = \mathop{\inf }\limits_{{x \in {\mathbb{R}}^{n}}}J\left( x\right) \).

b) L’inégalité d’ \( \alpha \) -convexité donne, pour tout \( m, n \in \mathbb{N} \) ,

> b) The \( \alpha \)-convexity inequality gives, for all \( m, n \in \mathbb{N} \),

\[
\frac{\alpha }{8}{\begin{Vmatrix}{u}_{n} - {u}_{m}\end{Vmatrix}}^{2} \leq  \frac{J\left( {u}_{n}\right)  + J\left( {u}_{m}\right) }{2} - J\left( \frac{{u}_{n} + {u}_{m}}{2}\right)  \leq  \frac{J\left( {u}_{n}\right)  + J\left( {u}_{m}\right) }{2} - J\left( {x}_{0}\right) ,
\]

et on en conclut que \( \mathop{\lim }\limits_{{m, n \rightarrow + \infty }}\frac{\alpha }{8}{\begin{Vmatrix}{u}_{n} - {u}_{m}\end{Vmatrix}}^{2} = 0 \) . Donc \( \left( {u}_{n}\right) \) est une suite de Cauchy. Comme \( {\mathbb{R}}^{n} \) est complet, elle converge. Soit \( u \) sa limite. Par continuité de \( J \) on a \( J\left( u\right) = J\left( {x}_{0}\right) \) , et d’après l’inégalité d’ \( \alpha \) -convexité

> and we conclude that \( \mathop{\lim }\limits_{{m, n \rightarrow + \infty }}\frac{\alpha }{8}{\begin{Vmatrix}{u}_{n} - {u}_{m}\end{Vmatrix}}^{2} = 0 \). Thus \( \left( {u}_{n}\right) \) is a Cauchy sequence. Since \( {\mathbb{R}}^{n} \) is complete, it converges. Let \( u \) be its limit. By continuity of \( J \) we have \( J\left( u\right) = J\left( {x}_{0}\right) \), and according to the \( \alpha \)-convexity inequality

\[
\frac{\alpha }{8}{\begin{Vmatrix}u - {x}_{0}\end{Vmatrix}}^{2} \leq  \frac{J\left( u\right)  + J\left( {x}_{0}\right) }{2} - J\left( \frac{u + {x}_{0}}{2}\right)  \leq  0,
\]

donc \( u = {x}_{0} \) . D’où le résultat.

> so \( u = {x}_{0} \). Hence the result.

Remarque. Les résultats des questions 2/ et 3/ restent vrais dans un espace de Hilbert. Par contre, le résultat de 1/ est faux en dimension infinie.

> Remark. The results of questions 2/ and 3/ remain true in a Hilbert space. However, the result of 1/ is false in infinite dimension.

Problem 5 (Lemme De Morse). 1/ (Préliminaires.) Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( \mathcal{S} \) l’e.v des matrices symétriques de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . On fixe \( A \in \mathcal{S} \) inversible, et on note \( \mathcal{F} \) l’e.v \( \mathcal{F} = \{ U \in \; {\left. {\mathcal{M}}_{n}\left( \mathbb{R}\right) \right| }^{t}{UA} = {AU}\} \)

> Problem 5 (Morse Lemma). 1/ (Preliminaries.) Let \( n \in {\mathbb{N}}^{ * } \). We denote by \( \mathcal{S} \) the vector space of symmetric matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). We fix \( A \in \mathcal{S} \) invertible, and we denote by \( \mathcal{F} \) the vector space \( \mathcal{F} = \{ U \in \; {\left. {\mathcal{M}}_{n}\left( \mathbb{R}\right) \right| }^{t}{UA} = {AU}\} \)

a) Montrer que \( \Omega = \mathcal{F} \cap \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) est un ouvert de \( \mathcal{F} \) et que l’application \( \varphi : \Omega \rightarrow \mathcal{S}\;U \mapsto \; {}^{t}{UAU} \) est un \( {\mathcal{C}}^{\infty } \) -difféomorphisme local en \( U = {I}_{n} \) .

> a) Show that \( \Omega = \mathcal{F} \cap \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) is an open subset of \( \mathcal{F} \) and that the map \( \varphi : \Omega \rightarrow \mathcal{S}\;U \mapsto \; {}^{t}{UAU} \) is a \( {\mathcal{C}}^{\infty } \)-local diffeomorphism at \( U = {I}_{n} \).

b) Montrer l’existence d’un voisinage ouvert \( V \) de \( A \) dans \( \mathcal{S} \) et d’une application \( h : V \rightarrow \; \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) de classe \( {\mathcal{C}}^{\infty } \) telle que \( h\left( A\right) = {I}_{n} \) et telle que \( {}^{t}h\left( B\right) {Ah}\left( B\right) = B \) pour tout \( B \in V \) . c) Montrer qu’il existe une application \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) de classe \( {\mathcal{C}}^{\infty } \) telle que pour tout \( B \in V,{}^{t}g\left( B\right) {Dg}\left( B\right) = B \) , où \( D \) est une matrice diagonale dont les coefficients diagonaux sont égaux à 1 ou à -1 .

> b) Show the existence of an open neighborhood \( V \) of \( A \) in \( \mathcal{S} \) and a \( {\mathcal{C}}^{\infty } \) class map \( h : V \rightarrow \; \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that \( h\left( A\right) = {I}_{n} \) and such that \( {}^{t}h\left( B\right) {Ah}\left( B\right) = B \) for all \( B \in V \) . c) Show that there exists a \( {\mathcal{C}}^{\infty } \) class map \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that for all \( B \in V,{}^{t}g\left( B\right) {Dg}\left( B\right) = B \) , where \( D \) is a diagonal matrix whose diagonal coefficients are equal to 1 or -1 .

2/ (Lemme de Morse.) Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{\infty } \) , nulle en 0, telle que \( d{f}_{0} = 0 \) . On suppose que la matrice hessienne de \( f \) en 0 définie par \( H = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( 0\right) \right) }_{1 \leq i, j \leq n} \) est inversible. Montrer qu’il existe un \( {\mathcal{C}}^{\infty } \) -difféomorphisme \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) défini sur un voisinage \( W \) de 0, et un entier \( r \) tels que

> 2/ (Morse Lemma.) Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{\infty } \) class function, vanishing at 0, such that \( d{f}_{0} = 0 \) . Suppose the Hessian matrix of \( f \) at 0 defined by \( H = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( 0\right) \right) }_{1 \leq i, j \leq n} \) is invertible. Show that there exists a \( {\mathcal{C}}^{\infty } \) -diffeomorphism \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) defined on a neighborhood \( W \) of 0, and an integer \( r \) such that

\[
\forall x \in  W,\;f\left( x\right)  = {\left\lbrack  {\varphi }_{1}\left( x\right) \right\rbrack  }^{2} + \cdots  + {\left\lbrack  {\varphi }_{r}\left( x\right) \right\rbrack  }^{2} - {\left\lbrack  {\varphi }_{r + 1}\left( x\right) \right\rbrack  }^{2} - \cdots  - {\left\lbrack  {\varphi }_{n}\left( x\right) \right\rbrack  }^{2}
\]

(on utilisera le résultat de la question b) de l'exercice 4 de la page 331).

> (use the result from question b) of exercise 4 on page 331).

Solution. 1/ a) On sait que \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) est un ouvert de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (image réciproque de la fonction déterminant, qui est continue, de l’ouvert \( {\mathbb{R}}^{ * } \) ), donc \( \Omega = \mathcal{F} \cap \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) est un ouvert de \( \mathcal{F} \) .

> Solution. 1/ a) We know that \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) is an open subset of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (inverse image of the determinant function, which is continuous, of the open set \( {\mathbb{R}}^{ * } \) ), therefore \( \Omega = \mathcal{F} \cap \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) is an open subset of \( \mathcal{F} \) .

La fonction \( \varphi \) est de classe \( {\mathcal{C}}^{\infty } \) car les coefficients de \( \varphi \left( U\right) \) s’expriment comme des polynômes en les coefficients de \( U \) .

> The function \( \varphi \) is of class \( {\mathcal{C}}^{\infty } \) because the coefficients of \( \varphi \left( U\right) \) are expressed as polynomials in the coefficients of \( U \) .

On a bien sûr \( {I}_{n} \in \Omega \) . Calculons \( d{\varphi }_{{I}_{n}} \) , la différentielle de \( \varphi \) en \( {I}_{n} \) . Si \( {I}_{n} + H \in \Omega \) , on a

> We have, of course, \( {I}_{n} \in \Omega \) . Let us calculate \( d{\varphi }_{{I}_{n}} \) , the differential of \( \varphi \) at \( {I}_{n} \) . If \( {I}_{n} + H \in \Omega \) , we have

\[
\varphi \left( {{I}_{n} + H}\right)  - \varphi \left( {I}_{n}\right)  = {}^{t}{HA} + {AH} + {}^{t}{HAH} = {}^{t}{HA} + {AH} + o\left( {\parallel H\parallel }\right) ,
\]

donc \( d{\varphi }_{{I}_{n}}\left( H\right) = {}^{t}{HA} + {AH} \) pour tout \( H \in \mathcal{F} \) .

> therefore \( d{\varphi }_{{I}_{n}}\left( H\right) = {}^{t}{HA} + {AH} \) for all \( H \in \mathcal{F} \) .

Montrons que \( d{\varphi }_{{I}_{n}} : \mathcal{F} \rightarrow \mathcal{S} \) est un isomorphisme de \( \mathcal{F} \) sur \( \mathcal{S} \) , ce qui permettra de conclure que \( \varphi \) est un \( {\mathcal{C}}^{\infty } \) -difféomorphisme local en \( {I}_{n} \) d’après le théorème d’inversion locale.

> Let us show that \( d{\varphi }_{{I}_{n}} : \mathcal{F} \rightarrow \mathcal{S} \) is an isomorphism from \( \mathcal{F} \) onto \( \mathcal{S} \) , which will allow us to conclude that \( \varphi \) is a local \( {\mathcal{C}}^{\infty } \) -diffeomorphism at \( {I}_{n} \) according to the inverse function theorem.

- La différentielle \( d{\varphi }_{{I}_{n}} : \mathcal{F} \rightarrow  \mathcal{S} \) est injective. En effet, si \( d{\varphi }_{{I}_{n}}\left( H\right)  = {}^{t}{HA} + {AH} = 0 \) , alors comme \( {}^{t}{HA} = {AH} \) (puisque \( H \in  \mathcal{F} \) ), on a \( {AH} = 0 \) , donc \( H = 0 \) car \( A \) est inversible.

> - The differential \( d{\varphi }_{{I}_{n}} : \mathcal{F} \rightarrow  \mathcal{S} \) is injective. Indeed, if \( d{\varphi }_{{I}_{n}}\left( H\right)  = {}^{t}{HA} + {AH} = 0 \), then since \( {}^{t}{HA} = {AH} \) (because \( H \in  \mathcal{F} \)), we have \( {AH} = 0 \), thus \( H = 0 \) because \( A \) is invertible.

- La différentielle \( d{\varphi }_{{I}_{n}} \) est surjective. En effet, pour tout \( S \in  \mathcal{S} \) la matrice \( H = \frac{1}{2}{A}^{-1}S \) est bien dans \( \mathcal{F} \) (car comme \( A \in  \mathcal{S} \) , on a \( {}^{t}{HA} = \frac{1}{2}{}^{t}{S}^{t}{A}^{-1}A = \frac{1}{2}S = {AH} \) ) et \( d{\varphi }_{{I}_{n}}\left( H\right)  = \; {}^{t}{HA} + {AH} = {2AH} = S. \)

> - The differential \( d{\varphi }_{{I}_{n}} \) is surjective. Indeed, for any \( S \in  \mathcal{S} \), the matrix \( H = \frac{1}{2}{A}^{-1}S \) is indeed in \( \mathcal{F} \) (because as \( A \in  \mathcal{S} \), we have \( {}^{t}{HA} = \frac{1}{2}{}^{t}{S}^{t}{A}^{-1}A = \frac{1}{2}S = {AH} \)) and \( d{\varphi }_{{I}_{n}}\left( H\right)  = \; {}^{t}{HA} + {AH} = {2AH} = S. \)

b) Il existe donc un voisinage ouvert \( W \) de \( {I}_{n} \) dans \( \Omega \) , un voisinage ouvert \( V \) de \( \varphi \left( {I}_{n}\right) = A \) dans \( \mathcal{S} \) tel que \( {\varphi }_{\mid W} \) soit un \( {\mathcal{C}}^{\infty } \) -difféomorphisme de \( W \) sur \( V \) . Si on note \( h : V \rightarrow W \) son difféomorphisme inverse, \( h \) est de classe \( {\mathcal{C}}^{\infty } \) ,à valeurs dans \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) (car \( W \subset \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) ) et pour tout \( B \in V,\varphi \left( {h\left( B\right) }\right) = B = {}^{t}h\left( B\right) {Ah}\left( B\right) \) .

> b) There exists therefore an open neighborhood \( W \) of \( {I}_{n} \) in \( \Omega \), an open neighborhood \( V \) of \( \varphi \left( {I}_{n}\right) = A \) in \( \mathcal{S} \) such that \( {\varphi }_{\mid W} \) is a \( {\mathcal{C}}^{\infty } \)-diffeomorphism from \( W \) onto \( V \). If we denote \( h : V \rightarrow W \) as its inverse diffeomorphism, \( h \) is of class \( {\mathcal{C}}^{\infty } \), with values in \( \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) (because \( W \subset \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \)) and for all \( B \in V,\varphi \left( {h\left( B\right) }\right) = B = {}^{t}h\left( B\right) {Ah}\left( B\right) \).

c) Notons \( \left( {p, q}\right) \) la signature de la forme quadratique \( X \mapsto {}^{t}{XAX}\left( {X \in {\mathbb{R}}^{n}}\right) \) . On sait que \( p + q = n \) (car \( A \) est inversible) et que \( A \) est congrue à la matrice diagonale \( D \) dont les \( p \) premiers termes diagonaux sont égaux à 1, les \( q = n - p \) derniers égaux à-1, autrement dit, il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) tel que \( A = {}^{t}{PDP} \) . On définit maintenant l’application \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) par \( g\left( B\right) = {Ph}\left( B\right) \) . Elle est de classe \( {\mathcal{C}}^{\infty } \) et elle vérifie

> c) Let \( \left( {p, q}\right) \) be the signature of the quadratic form \( X \mapsto {}^{t}{XAX}\left( {X \in {\mathbb{R}}^{n}}\right) \). We know that \( p + q = n \) (because \( A \) is invertible) and that \( A \) is congruent to the diagonal matrix \( D \) whose first \( p \) diagonal terms are equal to 1, the last \( q = n - p \) equal to -1, in other words, there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) such that \( A = {}^{t}{PDP} \). We now define the map \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) by \( g\left( B\right) = {Ph}\left( B\right) \). It is of class \( {\mathcal{C}}^{\infty } \) and it satisfies

\[
\forall B \in  V,\;{}^{t}g\left( B\right) {Dg}\left( B\right)  = {}^{t}h\left( B\right) \left\lbrack  {{}^{t}{PDP}}\right\rbrack  h\left( B\right)  = {}^{t}h\left( B\right) {Ah}\left( B\right)  = B.
\]

2/ D’après la question b) de l’exercice 4 de la page 331, on peut trouver \( {n}^{2} \) fonctions \( {h}_{i, j} : {\mathbb{R}}^{n} \rightarrow \; \mathbb{R} \) , de classe \( {\mathcal{C}}^{\infty } \) , telles que

> 2/ According to question b) of exercise 4 on page 331, we can find \( {n}^{2} \) functions \( {h}_{i, j} : {\mathbb{R}}^{n} \rightarrow \; \mathbb{R} \), of class \( {\mathcal{C}}^{\infty } \), such that

\[
\forall x = \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n},\;f\left( x\right)  = \mathop{\sum }\limits_{{i, j}}{x}_{i}{x}_{j}{h}_{i, j}\left( x\right) .
\]

Si on pose \( {a}_{i, j}\left( x\right) = \frac{1}{2}\left\lbrack {{h}_{i, j}\left( x\right) + {h}_{j, i}\left( x\right) }\right\rbrack \) pour tout \( \left( {i, j}\right) \) , les fonctions \( {a}_{i, j} \) sont de classe \( {\mathcal{C}}^{\infty } \) sur \( {\mathbb{R}}^{n} \) , on a \( f\left( x\right) = \mathop{\sum }\limits_{{i, j}}{x}_{i}{x}_{j}{a}_{i, j}\left( x\right) \) , et pour tout \( x \) , la matrice \( A\left( x\right) = {\left( {a}_{i, j}\left( x\right) \right) }_{1 < i, j < n} \) est symétrique.

> If we set \( {a}_{i, j}\left( x\right) = \frac{1}{2}\left\lbrack {{h}_{i, j}\left( x\right) + {h}_{j, i}\left( x\right) }\right\rbrack \) for all \( \left( {i, j}\right) \) , the functions \( {a}_{i, j} \) are of class \( {\mathcal{C}}^{\infty } \) on \( {\mathbb{R}}^{n} \) , we have \( f\left( x\right) = \mathop{\sum }\limits_{{i, j}}{x}_{i}{x}_{j}{a}_{i, j}\left( x\right) \) , and for all \( x \) , the matrix \( A\left( x\right) = {\left( {a}_{i, j}\left( x\right) \right) }_{1 < i, j < n} \) is symmetric.

Résumons. Il existe une application \( A : {\mathbb{R}}^{n} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , de classe \( {\mathcal{C}}^{\infty } \) , telle que

> Let us summarize. There exists a mapping \( A : {\mathbb{R}}^{n} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , of class \( {\mathcal{C}}^{\infty } \) , such that

- pour tout \( X \in  {\mathbb{R}}^{n}, A\left( X\right) \) est symétrique et \( f\left( X\right)  = {}^{t}{XA}\left( X\right) X \) ;

> - for all \( X \in  {\mathbb{R}}^{n}, A\left( X\right) \) is symmetric and \( f\left( X\right)  = {}^{t}{XA}\left( X\right) X \) ;

- \( A\left( 0\right)  = H = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( 0\right) \right) }_{i, j} \) est inversible.

> - \( A\left( 0\right)  = H = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( 0\right) \right) }_{i, j} \) is invertible.

Soit \( \left( {r, n - r}\right) \) la signature de la forme quadratique \( X \mapsto {}^{t}{XHX} \) . D’après 1/c), il existe un voisinage \( V \) de \( H = A\left( 0\right) \) dans \( \mathcal{S} \) et une fonction \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , de classe \( {\mathcal{C}}^{\infty } \) , telle que \( {}^{t}g\left( B\right) {Dg}\left( B\right) = B \) pour tout \( B \in V \) , où \( D \) est la matrice diagonale dont les \( r \) premiers éléments diagonaux sont égaux à 1 et les \( n - r \) derniers égaux à-1.

> Let \( \left( {r, n - r}\right) \) be the signature of the quadratic form \( X \mapsto {}^{t}{XHX} \) . According to 1/c), there exists a neighborhood \( V \) of \( H = A\left( 0\right) \) in \( \mathcal{S} \) and a function \( g : V \rightarrow \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , of class \( {\mathcal{C}}^{\infty } \) , such that \( {}^{t}g\left( B\right) {Dg}\left( B\right) = B \) for all \( B \in V \) , where \( D \) is the diagonal matrix whose first \( r \) diagonal elements are equal to 1 and the last \( n - r \) are equal to -1.

Comme \( X \mapsto A\left( X\right) \) est continue, il existe un voisinage \( W \) de 0 dans \( {\mathbb{R}}^{n} \) tel que \( A\left( X\right) \in V \) pour tout \( X \in W \) . On a donc \( A\left( X\right) = {}^{t}g\left\lbrack {A\left( X\right) }\right\rbrack {Dg}\left\lbrack {A\left( X\right) }\right\rbrack \) pour tout \( X \in W \) , et on en déduit

> Since \( X \mapsto A\left( X\right) \) is continuous, there exists a neighborhood \( W \) of 0 in \( {\mathbb{R}}^{n} \) such that \( A\left( X\right) \in V \) for all \( X \in W \) . We therefore have \( A\left( X\right) = {}^{t}g\left\lbrack {A\left( X\right) }\right\rbrack {Dg}\left\lbrack {A\left( X\right) }\right\rbrack \) for all \( X \in W \) , and we deduce from this

\[
\forall X \in  W,\;f\left( X\right)  = {}^{t}{XA}\left( X\right) X = {}^{t}\varphi \left( X\right) {D\varphi }\left( X\right) \;\text{ où }\;\varphi \left( X\right)  = g\left\lbrack  {A\left( X\right) }\right\rbrack  X.
\]

En notant \( {\varphi }_{1}\left( X\right) ,\ldots ,{\varphi }_{n}\left( X\right) \) les coordonnées de \( \varphi \left( X\right) \) , ceci s’écrit aussi

> By denoting \( {\varphi }_{1}\left( X\right) ,\ldots ,{\varphi }_{n}\left( X\right) \) as the coordinates of \( \varphi \left( X\right) \) , this can also be written as

\[
\forall X \in  W,\;f\left( X\right)  = {\varphi }_{1}{\left( X\right) }^{2} + \cdots  + {\varphi }_{r}{\left( X\right) }^{2} - {\varphi }_{r + 1}{\left( X\right) }^{2} - \cdots  - {\varphi }_{n}{\left( X\right) }^{2}.
\]

Ce n’est pas tout-à-fait fini. On a \( d{\varphi }_{0} = g\left\lbrack {A\left( 0\right) }\right\rbrack \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , donc quitte à restreindre \( W \) , on peut supposer (d’après le théorème d’inversion locale) que \( \varphi \) est un \( {\mathcal{C}}^{\infty } \) -difféomorphisme de \( W \; \operatorname{sur}\varphi \left( W\right) \) . On a bien sûr \( \varphi \left( 0\right) = g\left\lbrack {A\left( 0\right) }\right\rbrack 0 = 0 \) .

> It is not quite finished. We have \( d{\varphi }_{0} = g\left\lbrack {A\left( 0\right) }\right\rbrack \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) , so by restricting \( W \) , we can assume (by the local inversion theorem) that \( \varphi \) is a \( {\mathcal{C}}^{\infty } \) -diffeomorphism of \( W \; \operatorname{sur}\varphi \left( W\right) \) . We have, of course, \( \varphi \left( 0\right) = g\left\lbrack {A\left( 0\right) }\right\rbrack 0 = 0 \) .

Problem 6 (Équation de la chualeur).

> Problem 6 (Heat equation).

![bo_d7fjkrs91nqc73ereoog_373_1185_949_214_230_0.jpg](images/gourdon_analysis_fr_en_023_bod7fjkrs91nqc73ereoog37311859492142300.jpg)

On se place dans le plan \( {\mathbb{R}}^{2} \) dont les éléments sont notés \( \left( {x, t}\right) \) . Pour tout \( T > 0 \) , on note

> We consider the plane \( {\mathbb{R}}^{2} \) whose elements are denoted by \( \left( {x, t}\right) \) . For all \( T > 0 \) , we denote

\[
\text{ - }{R}_{T} = \rbrack 0,\pi \left\lbrack  \times \right\rbrack  0, T\lbrack \text{ , }
\]

\[
\text{ - }{C}_{T} = \left( {\{ 0\}  \times  \left\lbrack  {0, T}\right\rbrack  }\right)  \cup  \left( {\left\lbrack  {0,\pi }\right\rbrack  \times \{ 0\} }\right)  \cup  \left( {\{ \pi \}  \times  \left\lbrack  {0, T}\right\rbrack  }\right) \text{ , }
\]

\[
\text{ — }{\Lambda }_{T} = \rbrack 0,\pi \lbrack  \times  \{ T\} \text{ . }
\]

de sorte que \( {R}_{T},{C}_{T} \) et \( {\Lambda }_{T} \) soient disjoints et que leur réunion soit le rectangle fermé \( \overline{{R}_{T}} \) .

> such that \( {R}_{T},{C}_{T} \) and \( {\Lambda }_{T} \) are disjoint and their union is the closed rectangle \( \overline{{R}_{T}} \) .

1 / Soit \( \varphi : \left\lbrack {0,\pi }\right\rbrack \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) , telle que \( \varphi \left( 0\right) = \varphi \left( \pi \right) = 0 \) .

> 1 / Let \( \varphi : \left\lbrack {0,\pi }\right\rbrack \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{1} \) , such that \( \varphi \left( 0\right) = \varphi \left( \pi \right) = 0 \) .

a) Montrer l’existence d’une suite réelle \( \left( {b}_{n}\right) \) telle que \( \sum \left| {b}_{n}\right| \) converge et telle que

> a) Show the existence of a real sequence \( \left( {b}_{n}\right) \) such that \( \sum \left| {b}_{n}\right| \) converges and such that

\[
\forall x \in  \left\lbrack  {0,\pi }\right\rbrack  ,\;\varphi \left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{b}_{n}\sin \left( {nx}\right) .
\]

b) Soit \( {T}_{0} > 0 \) . Construire une fonction \( \Phi \) continue sur \( \overline{{R}_{{T}_{0}}} \) telle que

> b) Let \( {T}_{0} > 0 \) . Construct a function \( \Phi \) continuous on \( \overline{{R}_{{T}_{0}}} \) such that

(i) \( \Phi \) est de classe \( {\mathcal{C}}^{2} \) sur \( {R}_{{T}_{0}} \) et \( \frac{{\partial }^{2}\Phi }{\partial {x}^{2}} - \frac{\partial \Phi }{\partial t} = 0 \) sur \( {R}_{{T}_{0}} \) ;

> (i) \( \Phi \) is of class \( {\mathcal{C}}^{2} \) on \( {R}_{{T}_{0}} \) and \( \frac{{\partial }^{2}\Phi }{\partial {x}^{2}} - \frac{\partial \Phi }{\partial t} = 0 \) on \( {R}_{{T}_{0}} \) ;

(ii) pour tout \( t \in \left\lbrack {0,{T}_{0}}\right\rbrack ,\Phi \left( {0, t}\right) = \Phi \left( {\pi , t}\right) = 0 \) ;

> (ii) for all \( t \in \left\lbrack {0,{T}_{0}}\right\rbrack ,\Phi \left( {0, t}\right) = \Phi \left( {\pi , t}\right) = 0 \) ;

(iii) pour tout \( x \in \left\lbrack {0,\pi }\right\rbrack ,\Phi \left( {x,0}\right) = \varphi \left( x\right) \) .

> (iii) for all \( x \in \left\lbrack {0,\pi }\right\rbrack ,\Phi \left( {x,0}\right) = \varphi \left( x\right) \) .

2 / On veut montrer qu’il n’existe qu’une seule fonction \( \Phi \) vérifiant (i),(ii) et (iii). Soit \( f \) une fonction à valeurs réelles, continue sur \( \overline{{R}_{{T}_{0}}} \) et de classe \( {\mathcal{C}}^{2} \) sur \( {R}_{{T}_{0}} \) .

> 2 / We want to show that there exists only one function \( \Phi \) satisfying (i),(ii) and (iii). Let \( f \) be a real-valued function, continuous on \( \overline{{R}_{{T}_{0}}} \) and of class \( {\mathcal{C}}^{2} \) on \( {R}_{{T}_{0}} \) .

a) Si \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} > 0 \) sur \( {R}_{{T}_{0}} \) , montrer que \( f \) atteint son maximum sur \( {C}_{{T}_{0}} \) (on po commencer par prouver le résultat sur \( {R}_{T} \) et \( {C}_{T} \) pour tout \( T \in \left. {\rbrack 0,{T}_{0}\lbrack }\right) \) .

> a) If \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} > 0 \) on \( {R}_{{T}_{0}} \) , show that \( f \) reaches its maximum on \( {C}_{{T}_{0}} \) (one can start by proving the result on \( {R}_{T} \) and \( {C}_{T} \) for all \( T \in \left. {\rbrack 0,{T}_{0}\lbrack }\right) \) .

b) Si \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} \geq 0 \) sur \( {R}_{{T}_{0}} \) , montrer que \( f \) atteint son maximum sur \( {C}_{{T}_{0}} \) .

> b) If \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} \geq 0 \) on \( {R}_{{T}_{0}} \) , show that \( f \) reaches its maximum on \( {C}_{{T}_{0}} \) .

c) Si \( f \) est nulle sur \( {C}_{{T}_{0}} \) et si \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} = 0 \) sur \( {R}_{{T}_{0}} \) , montrer que \( f \) est nulle.

> c) If \( f \) is zero on \( {C}_{{T}_{0}} \) and if \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} = 0 \) on \( {R}_{{T}_{0}} \) , show that \( f \) is zero.

d) En déduire que la fonction \( \Phi \) construite à la question 1/b) est la seule fonction vérifiant (i), (ii) et (iii). pour tout \( x \in \rbrack - \pi ,\pi \rbrack \) . Ainsi construite, la fonction \( \widehat{\varphi } \) est \( {2\pi } \) -périodique sur \( \mathbb{R} \) , impaire, de classe \( {\mathcal{C}}^{1} \) par morceaux et continue sur \( \mathbb{R} \) car \( \varphi \left( 0\right) = \varphi \left( \pi \right) = 0 \) . On en déduit que ses coefficients de Fourier \( {a}_{n}\left( f\right) \) sont nuls, que ses coefficients de Fourier \( {b}_{n} = {b}_{n}\left( f\right) \) sont tels que \( \sum \left| {b}_{n}\right| \) converge (voir le théorème 3 page 272), et que de plus

> d) Deduce that the function \( \Phi \) constructed in question 1/b) is the only function satisfying (i), (ii) and (iii) for all \( x \in \rbrack - \pi ,\pi \rbrack \) . Thus constructed, the function \( \widehat{\varphi } \) is \( {2\pi } \) -periodic on \( \mathbb{R} \) , odd, piecewise \( {\mathcal{C}}^{1} \) and continuous on \( \mathbb{R} \) because \( \varphi \left( 0\right) = \varphi \left( \pi \right) = 0 \) . We deduce that its Fourier coefficients \( {a}_{n}\left( f\right) \) are zero, that its Fourier coefficients \( {b}_{n} = {b}_{n}\left( f\right) \) are such that \( \sum \left| {b}_{n}\right| \) converges (see theorem 3 page 272), and that furthermore

\[
\forall x \in  \mathbb{R},\;\widehat{\varphi }\left( x\right)  = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{b}_{n}\sin {nx}.
\]

---

Solution. 1/ a) On pense évidemment au développement en série de Fourier. Pour cela, on prolonge \( \varphi \) sur \( \mathbb{R} \) de la manière suivante : sur ] \( - \pi ,0\left\lbrack {\text{ on pose }\widetilde{\varphi }\left( x\right) = - \varphi \left( {-x}\right) \text{ , sur }\lbrack 0,\pi }\right\rbrack \) , \( \widetilde{\varphi }\left( x\right) = \varphi \left( x\right) \) . On définit ensuite une fonction \( \widehat{\varphi } \) sur \( \mathbb{R} \) par \( \widehat{\varphi }\left( {x + {2k\pi }}\right) = \widetilde{\varphi }\left( x\right) \) pour tout \( k \in \mathbb{Z} \) et

> Solution. 1/ a) One naturally thinks of the Fourier series expansion. To do this, we extend \( \varphi \) to \( \mathbb{R} \) in the following way: on ] \( - \pi ,0\left\lbrack {\text{ on pose }\widetilde{\varphi }\left( x\right) = - \varphi \left( {-x}\right) \text{ , sur }\lbrack 0,\pi }\right\rbrack \) , \( \widetilde{\varphi }\left( x\right) = \varphi \left( x\right) \) . We then define a function \( \widehat{\varphi } \) on \( \mathbb{R} \) by \( \widehat{\varphi }\left( {x + {2k\pi }}\right) = \widetilde{\varphi }\left( x\right) \) for all \( k \in \mathbb{Z} \) and

---

On en déduit le résultat car \( \varphi \left( x\right) = \widehat{\varphi }\left( x\right) \) pour tout \( x \in \left\lbrack {0,\pi }\right\rbrack \) .

> We deduce the result because \( \varphi \left( x\right) = \widehat{\varphi }\left( x\right) \) for all \( x \in \left\lbrack {0,\pi }\right\rbrack \) .

b) Remarquons que la fonction \( f : \left( {x, t}\right) \mapsto \left( {\sin {nx}}\right) {e}^{-{n}^{2}t} \) vérifie \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} = 0 \) . On pose donc

> b) Note that the function \( f : \left( {x, t}\right) \mapsto \left( {\sin {nx}}\right) {e}^{-{n}^{2}t} \) satisfies \( \frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t} = 0 \) . We therefore set

\[
\Phi  : \overline{{R}_{{T}_{0}}} \rightarrow  \mathbb{R}\;\left( {x, t}\right)  \mapsto  \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{b}_{n}\left( {\sin {nx}}\right) {e}^{-{n}^{2}t}.
\]

La série est normalement convergente sur \( \overline{{R}_{{T}_{0}}} \) , donc \( \Phi \) est bien définie et continue sur \( \overline{{R}_{{T}_{0}}} \) . Par ailleurs, les conditions (ii) et (iii) sont vérifiées.

> The series converges normally on \( \overline{{R}_{{T}_{0}}} \) , so \( \Phi \) is well-defined and continuous on \( \overline{{R}_{{T}_{0}}} \) . Furthermore, conditions (ii) and (iii) are satisfied.

Il nous reste à vérifier (i). Soit \( p \in \mathbb{N} \) . Pour tout \( a > 0 \) , on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{e}^{-{n}^{2}a}{n}^{p} = 0 \) , donc les séries de fonctions \( \sum {n}^{p}{b}_{n}\left( {\sin {nx}}\right) {e}^{-{n}^{2}t} \) et \( \sum {n}^{p}{b}_{n}\left( {\cos {nx}}\right) {e}^{-{n}^{2}t} \) convergent normalement pour \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {a,{T}_{0}}\right\rbrack \) . On en déduit facilement, grâce au théorème de dérivation des séries de fonctions que \( \Phi \) est de classe \( {\mathcal{C}}^{p} \) sur \( \rbrack 0,\pi \left\lbrack \times \right\rbrack a,{T}_{0}\lbrack \) , et ceci pour tout \( a > 0 \) , donc de classe \( {\mathcal{C}}^{p} \) sur \( {R}_{{T}_{0}} \) , et que les dérivées partielles de \( \Phi \) s’obtiennent en dérivant formellement chacun de ses termes. Comme ceci est vrai pour tout \( p \in \mathbb{N},\Phi \) est de classe \( {\mathcal{C}}^{\infty } \) . En particulier, \( \Phi \) est de classe \( {\mathcal{C}}^{2} \) et

> It remains for us to verify (i). Let \( p \in \mathbb{N} \) . For all \( a > 0 \) , we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{e}^{-{n}^{2}a}{n}^{p} = 0 \) , so the series of functions \( \sum {n}^{p}{b}_{n}\left( {\sin {nx}}\right) {e}^{-{n}^{2}t} \) and \( \sum {n}^{p}{b}_{n}\left( {\cos {nx}}\right) {e}^{-{n}^{2}t} \) converge normally for \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {a,{T}_{0}}\right\rbrack \) . We easily deduce, thanks to the theorem on the differentiation of series of functions, that \( \Phi \) is of class \( {\mathcal{C}}^{p} \) on \( \rbrack 0,\pi \left\lbrack \times \right\rbrack a,{T}_{0}\lbrack \) , and this for all \( a > 0 \) , therefore of class \( {\mathcal{C}}^{p} \) on \( {R}_{{T}_{0}} \) , and that the partial derivatives of \( \Phi \) are obtained by formally differentiating each of its terms. As this is true for all \( p \in \mathbb{N},\Phi \) is of class \( {\mathcal{C}}^{\infty } \) . In particular, \( \Phi \) is of class \( {\mathcal{C}}^{2} \) and

\[
\forall \left( {x, t}\right)  \in  {R}_{{T}_{0}},\;\frac{{\partial }^{2}\Phi }{\partial {x}^{2}} =  - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{n}^{2}\left( {\sin {nx}}\right) {e}^{-{n}^{2}t},\;\frac{\partial \Phi }{\partial t} =  - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{n}^{2}\left( {\sin {nx}}\right) {e}^{-{n}^{2}t}.
\]

Ainsi, \( \frac{{\partial }^{2}\Phi }{\partial {x}^{2}} - \frac{\partial \Phi }{\partial t} = 0 \) sur \( {R}_{{T}_{0}} \) , d’où (i) et le résultat.

> Thus, \( \frac{{\partial }^{2}\Phi }{\partial {x}^{2}} - \frac{\partial \Phi }{\partial t} = 0 \) on \( {R}_{{T}_{0}} \) , whence (i) and the result.

\( \mathbf{2}/ \) a) Montrons d’abord que pour tout \( T \in \rbrack 0,{T}_{0}\lbrack \) , la restriction de \( f \) à \( \overline{{R}_{T}} \) atteint son maximum en un point de \( {C}_{T} \) (on sait déjà que \( f \) atteint son maximum sur \( \overline{{R}_{T}} \) car \( \overline{{R}_{T}} \) est compact et \( f \) est continue). Raisonnons par l'absurde : si ceci n'est pas vrai, le maximum est atteint en un point \( \left( {{x}_{0},{t}_{0}}\right) \) de \( {R}_{T} \) ou de \( {\Lambda }_{T} \) .

> \( \mathbf{2}/ \) a) Let us first show that for all \( T \in \rbrack 0,{T}_{0}\lbrack \) , the restriction of \( f \) to \( \overline{{R}_{T}} \) reaches its maximum at a point in \( {C}_{T} \) (we already know that \( f \) reaches its maximum on \( \overline{{R}_{T}} \) because \( \overline{{R}_{T}} \) is compact and \( f \) is continuous). Let us reason by contradiction: if this is not true, the maximum is reached at a point \( \left( {{x}_{0},{t}_{0}}\right) \) of \( {R}_{T} \) or of \( {\Lambda }_{T} \) .

- Si \( \left( {{x}_{0},{t}_{0}}\right)  \in  {R}_{T} \) , alors comme \( \left( {{x}_{0},{t}_{0}}\right) \) est un point intérieur à \( \overline{{R}_{T}} \) , on a

> - If \( \left( {{x}_{0},{t}_{0}}\right)  \in  {R}_{T} \) , then as \( \left( {{x}_{0},{t}_{0}}\right) \) is an interior point of \( \overline{{R}_{T}} \) , we have

\[
\frac{\partial f}{\partial t}\left( {{x}_{0},{t}_{0}}\right)  = \frac{\partial f}{\partial x}\left( {{x}_{0},{t}_{0}}\right)  = 0
\]

et la forme quadratique

> and the quadratic form

\[
{x}^{2}\frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{x}_{0},{t}_{0}}\right)  + {2xt}\frac{{\partial }^{2}f}{\partial x\partial t}\left( {{x}_{0},{t}_{0}}\right)  + {t}^{2}\frac{{\partial }^{2}f}{\partial {t}^{2}}\left( {{x}_{0},{t}_{0}}\right)
\]

est négative, en particulier \( \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{x}_{0},{t}_{0}}\right) \leq 0 \) . On a donc \( \left( {\frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t}}\right) \left( {{x}_{0},{t}_{0}}\right) \leq 0 \) , ce qui est contraire aux hypothèses.

> is negative, in particular \( \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{x}_{0},{t}_{0}}\right) \leq 0 \) . We therefore have \( \left( {\frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t}}\right) \left( {{x}_{0},{t}_{0}}\right) \leq 0 \) , which is contrary to the hypotheses.

- \( \operatorname{Si}\left( {{x}_{0},{t}_{0}}\right)  = \left( {{x}_{0}, T}\right)  \in  {\Lambda }_{T} \) , alors

> - \( \operatorname{Si}\left( {{x}_{0},{t}_{0}}\right)  = \left( {{x}_{0}, T}\right)  \in  {\Lambda }_{T} \) , then

- \( \frac{\partial f}{\partial t}\left( {{x}_{0}, T}\right)  \geq  0 \) puisque \( t \mapsto  f\left( {{x}_{0}, t}\right) \) atteint son maximum en \( t = T \) ;

> - \( \frac{\partial f}{\partial t}\left( {{x}_{0}, T}\right)  \geq  0 \) since \( t \mapsto  f\left( {{x}_{0}, t}\right) \) reaches its maximum at \( t = T \) ;

- \( \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{x}_{0}, T}\right)  \leq  0 \) puisque \( x \mapsto  f\left( {x, T}\right) \) atteint son maximum en \( x = {x}_{0} \) , point intérieur à \( \left\lbrack  {0,\pi }\right\rbrack \) .

> - \( \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {{x}_{0}, T}\right)  \leq  0 \) since \( x \mapsto  f\left( {x, T}\right) \) reaches its maximum at \( x = {x}_{0} \) , an interior point of \( \left\lbrack  {0,\pi }\right\rbrack \) .

On a donc \( \left( {\frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t}}\right) \left( {{x}_{0},{t}_{0}}\right) \leq 0 \) , ce qui est contraire aux hypothèses.

> We therefore have \( \left( {\frac{{\partial }^{2}f}{\partial {x}^{2}} - \frac{\partial f}{\partial t}}\right) \left( {{x}_{0},{t}_{0}}\right) \leq 0 \) , which contradicts the hypotheses.

Nous avons donc montré le premier résultat annoncé (on ne pouvait pas procéder directement avec \( T = {T}_{0} \) car \( f \) n’est pas supposée \( {\mathcal{C}}^{2} \) sur un voisinage de \( {\Lambda }_{{T}_{0}} \) ).

> We have thus shown the first announced result (we could not proceed directly with \( T = {T}_{0} \) because \( f \) is not assumed to be \( {\mathcal{C}}^{2} \) on a neighborhood of \( {\Lambda }_{{T}_{0}} \) ).

Achevons notre raisonnement. Soit \( \left( {T}_{n}\right) \) une suite croissante de points de \( \rbrack 0, T\left\lbrack \right. \) qui converge vers \( T \) . Comme nous venons de le montrer, il existe pour tout \( n \) un point \( \left( {{x}_{n},{t}_{n}}\right) \) de \( {C}_{{T}_{n}} \subset {C}_{T} \) tel que \( f\left( {{x}_{n},{t}_{n}}\right) = \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{n}}}}}f\left( {x, t}\right) \) . Comme \( {C}_{T} \) est compact, on peut extraire de la suite \( \left( {{x}_{n},{t}_{n}}\right) \) une sous-suite qui converge vers un point \( \left( {{x}^{ * },{t}^{ * }}\right) \) de \( {C}_{T} \) . Quitte à retirer des termes de la suite et à la réindicer, on peut même supposer que \( \left( {{x}_{n},{t}_{n}}\right) \) converge vers \( \left( {{x}^{ * },{t}^{ * }}\right) \) . Par continuité de

> Let us complete our reasoning. Let \( \left( {T}_{n}\right) \) be an increasing sequence of points in \( \rbrack 0, T\left\lbrack \right. \) that converges to \( T \) . As we have just shown, for every \( n \) there exists a point \( \left( {{x}_{n},{t}_{n}}\right) \) in \( {C}_{{T}_{n}} \subset {C}_{T} \) such that \( f\left( {{x}_{n},{t}_{n}}\right) = \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{n}}}}}f\left( {x, t}\right) \) . Since \( {C}_{T} \) is compact, we can extract from the sequence \( \left( {{x}_{n},{t}_{n}}\right) \) a subsequence that converges to a point \( \left( {{x}^{ * },{t}^{ * }}\right) \) in \( {C}_{T} \) . By removing terms from the sequence and reindexing it, we can even assume that \( \left( {{x}_{n},{t}_{n}}\right) \) converges to \( \left( {{x}^{ * },{t}^{ * }}\right) \) . By continuity of

\( f \) , on a \( f\left( {{x}^{ * },{t}^{ * }}\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {{x}_{n},{t}_{n}}\right) \) . Maintenant soit \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \lbrack 0, T\lbrack \) . Comme \( t < T \) , il existe \( N \) tel que \( t < {T}_{N} \) , donc

> \( f \) , we have \( f\left( {{x}^{ * },{t}^{ * }}\right) = \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {{x}_{n},{t}_{n}}\right) \) . Now let \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \lbrack 0, T\lbrack \) . Since \( t < T \) , there exists \( N \) such that \( t < {T}_{N} \) , therefore

\[
\forall n \geq  N,\;f\left( {{x}_{n},{t}_{n}}\right)  \geq  f\left( {x, t}\right) .
\]

En faisant \( n \rightarrow \infty \) , on en déduit \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq f\left( {x, t}\right) \) . Ceci est vrai pour tout \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \lbrack 0, T\lbrack \) . Par continuité de \( f \) , on a donc \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq f\left( {x, t}\right) \) pour tout \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {0, T}\right\rbrack \) , d’où le résultat.

> By letting \( n \rightarrow \infty \) , we deduce \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq f\left( {x, t}\right) \) . This is true for all \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \lbrack 0, T\lbrack \) . By continuity of \( f \) , we therefore have \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq f\left( {x, t}\right) \) for all \( \left( {x, t}\right) \in \left\lbrack {0,\pi }\right\rbrack \times \left\lbrack {0, T}\right\rbrack \) , hence the result.

b) La fonction \( f \) est continue sur le compact \( {C}_{{T}_{0}} \) donc il existe \( \left( {{x}^{ * },{t}^{ * }}\right) \in {C}_{{T}_{0}} \) tel que \( f\left( {{x}^{ * },{t}^{ * }}\right) = \; \mathop{\sup }\limits_{{\left( {x, t}\right) \in {C}_{{T}_{0}}}}f\left( {x, t}\right) \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , considérons la fonction \( {f}_{n} \) définie sur \( \overline{{R}_{{T}_{0}}} \) par \( {f}_{n}\left( {x, t}\right) = \; f\left( {x, t}\right) + {x}^{2}/n \) . La fonction \( {f}_{n} \) est de classe \( {\mathcal{C}}^{2} \) sur \( {R}_{{T}_{0}} \) et

> b) The function \( f \) is continuous on the compact set \( {C}_{{T}_{0}} \) therefore there exists \( \left( {{x}^{ * },{t}^{ * }}\right) \in {C}_{{T}_{0}} \) such that \( f\left( {{x}^{ * },{t}^{ * }}\right) = \; \mathop{\sup }\limits_{{\left( {x, t}\right) \in {C}_{{T}_{0}}}}f\left( {x, t}\right) \) . For any \( n \in {\mathbb{N}}^{ * } \) , consider the function \( {f}_{n} \) defined on \( \overline{{R}_{{T}_{0}}} \) by \( {f}_{n}\left( {x, t}\right) = \; f\left( {x, t}\right) + {x}^{2}/n \) . The function \( {f}_{n} \) is of class \( {\mathcal{C}}^{2} \) on \( {R}_{{T}_{0}} \) and

\[
\forall \left( {x, t}\right)  \in  {R}_{{T}_{0}},\;\frac{{\partial }^{2}{f}_{n}}{\partial {x}^{2}}\left( {x, t}\right)  - \frac{\partial {f}_{n}}{\partial t}\left( {x, t}\right)  = \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( {x, t}\right)  - \frac{\partial f}{\partial t}\left( {x, t}\right)  + \frac{2}{n} \geq  \frac{2}{n} > 0.
\]

On peut donc appliquer le résultat de la question précédente à \( {f}_{n} \) qui entraîne l’existence d’un point \( \left( {{x}_{n},{t}_{n}}\right) \) de \( {C}_{{T}_{0}} \) tel que \( {f}_{n}\left( {{x}_{n},{t}_{n}}\right) = \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{0}}}}}{f}_{n}\left( {x, t}\right) \) . On a donc

> We can therefore apply the result of the previous question to \( {f}_{n} \) which implies the existence of a point \( \left( {{x}_{n},{t}_{n}}\right) \) in \( {C}_{{T}_{0}} \) such that \( {f}_{n}\left( {{x}_{n},{t}_{n}}\right) = \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{0}}}}}{f}_{n}\left( {x, t}\right) \) . We therefore have

\[
f\left( {{x}^{ * },{t}^{ * }}\right)  \geq  f\left( {{x}_{n},{t}_{n}}\right)  = {f}_{n}\left( {{x}_{n},{t}_{n}}\right)  - \frac{{x}_{n}{}^{2}}{n} = \mathop{\sup }\limits_{{\left( {x, t}\right)  \in  {R}_{{T}_{0}}}}{f}_{n}\left( {x, t}\right)  - \frac{{x}_{n}^{2}}{n} \geq  \mathop{\sup }\limits_{{\left( {x, t}\right)  \in  {R}_{{T}_{0}}}}f\left( {x, t}\right)  - \frac{{\pi }^{2}}{n}.
\]

Ceci étant vrai pour tout \( n \in {\mathbb{N}}^{ * } \) , on en déduit, en prenant en compte les deux termes extrêmes des inégalités, que \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{0}}}}}f\left( {x, t}\right) \) . Ainsi, \( f \) atteint son maximum en \( \left( {{x}^{ * },{t}^{ * }}\right) \in \; {C}_{{T}_{0}} \) .

> Since this is true for any \( n \in {\mathbb{N}}^{ * } \) , we deduce, by taking into account the two extreme terms of the inequalities, that \( f\left( {{x}^{ * },{t}^{ * }}\right) \geq \mathop{\sup }\limits_{{\left( {x, t}\right) \in \overline{{R}_{{T}_{0}}}}}f\left( {x, t}\right) \) . Thus, \( f \) reaches its maximum at \( \left( {{x}^{ * },{t}^{ * }}\right) \in \; {C}_{{T}_{0}} \) .

c) La fonction \( f \) vérifie les hypothèses de la question précédente, donc son maximum est atteint sur \( {C}_{{T}_{0}} \) . Comme \( f \) est nulle sur \( {C}_{{T}_{0}} \) , on en déduit \( f \leq 0 \) . Le même raisonnement s’applique à \( - f \) , donc \( f \geq 0 \) . On en déduit que \( f \) est la fonction nulle.

> c) The function \( f \) satisfies the hypotheses of the previous question, so its maximum is reached on \( {C}_{{T}_{0}} \) . As \( f \) is zero on \( {C}_{{T}_{0}} \) , we deduce \( f \leq 0 \) . The same reasoning applies to \( - f \) , so \( f \geq 0 \) . We deduce that \( f \) is the zero function.

d) Supposons trouvée une fonction \( {\Phi }_{1} \) vérifiant les assertions (i),(ii) et (iii). Alors \( f = \Phi - {\Phi }_{1} \) satisfait les hypothèses de la question précédente, donc \( f = 0 \) , donc \( \Phi = {\Phi }_{1} \) .

> d) Suppose we have found a function \( {\Phi }_{1} \) satisfying assertions (i), (ii), and (iii). Then \( f = \Phi - {\Phi }_{1} \) satisfies the hypotheses of the previous question, therefore \( f = 0 \) , therefore \( \Phi = {\Phi }_{1} \) .

Problem 7. Soit \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que pour tout \( x \in {\mathbb{R}}^{n} \) , \( d{f}_{x} \) (différentielle de \( f \) en \( x \) ) est inversible, et telle que \( \mathop{\lim }\limits_{{\parallel x\parallel \rightarrow + \infty }}\parallel f\left( x\right) \parallel = + \infty \) .

> Problem 7. Let \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a \( {\mathcal{C}}^{1} \) class function such that for all \( x \in {\mathbb{R}}^{n} \) , \( d{f}_{x} \) (differential of \( f \) at \( x \) ) is invertible, and such that \( \mathop{\lim }\limits_{{\parallel x\parallel \rightarrow + \infty }}\parallel f\left( x\right) \parallel = + \infty \) .

a) Pour tout compact \( K \) de \( {\mathbb{R}}^{n} \) , montrer que \( {f}^{-1}\left( K\right) \) est un compact de \( {\mathbb{R}}^{n} \) .

> a) For any compact set \( K \) of \( {\mathbb{R}}^{n} \) , show that \( {f}^{-1}\left( K\right) \) is a compact set of \( {\mathbb{R}}^{n} \) .

b) Montrer que \( f \) est surjective (on utilisera un argument de connexité).

> b) Show that \( f \) is surjective (use a connectedness argument).

c) Soit \( y \) un élément de \( {\mathbb{R}}^{n} \) . Montrer que \( {f}^{-1}\left( {\{ y\} }\right) \) est un ensemble fini. On note \( m = \; \operatorname{Card}\left\lbrack {{f}^{-1}\left( {\{ y\} }\right) }\right\rbrack \) et on note \( {x}_{1},\ldots ,{x}_{m} \) les éléments de \( {f}^{-1}\left( {\{ y\} }\right) \) .

> c) Let \( y \) be an element of \( {\mathbb{R}}^{n} \) . Show that \( {f}^{-1}\left( {\{ y\} }\right) \) is a finite set. Let \( m = \; \operatorname{Card}\left\lbrack {{f}^{-1}\left( {\{ y\} }\right) }\right\rbrack \) be denoted by \( {x}_{1},\ldots ,{x}_{m} \) , the elements of \( {f}^{-1}\left( {\{ y\} }\right) \) .

d) Pour tout \( \varepsilon > 0 \) , montrer qu’il existe un voisinage ouvert \( V \) de \( y \) tel que \( {f}^{-1}\left( V\right) \subset \; { \cup }_{1 \leq i \leq m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) (où \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) désigne la boule ouverte de centre \( {x}_{i} \) de rayon \( \varepsilon \) ).

> d) For all \( \varepsilon > 0 \) , show that there exists an open neighborhood \( V \) of \( y \) such that \( {f}^{-1}\left( V\right) \subset \; { \cup }_{1 \leq i \leq m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) (where \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) denotes the open ball centered at \( {x}_{i} \) with radius \( \varepsilon \) ).

e) Montrer qu’il existe un voisinage ouvert \( W \) de \( y \) tel que

> e) Show that there exists an open neighborhood \( W \) of \( y \) such that

\[
\forall z \in  W,\;\operatorname{Card}\left\lbrack  {{f}^{-1}\left( {\{ z\} }\right) }\right\rbrack   = m.
\]

f) En déduire que l’application \( {\mathbb{R}}^{n} \rightarrow \mathbb{N}\;z \mapsto \operatorname{Card}\left\lbrack {{f}^{-1}\left( z\right) }\right\rbrack \) est constante.

> f) Deduce that the mapping \( {\mathbb{R}}^{n} \rightarrow \mathbb{N}\;z \mapsto \operatorname{Card}\left\lbrack {{f}^{-1}\left( z\right) }\right\rbrack \) is constant.

g) Si \( f\left( 0\right) = 0 \) et \( f\left( z\right) \neq 0 \) pour tout \( z \neq 0 \) , montrer que \( f \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( {\mathbb{R}}^{n} \) sur \( {\mathbb{R}}^{n} \) .

> g) If \( f\left( 0\right) = 0 \) and \( f\left( z\right) \neq 0 \) for all \( z \neq 0 \) , show that \( f \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism from \( {\mathbb{R}}^{n} \) onto \( {\mathbb{R}}^{n} \) .

Solution. a) Soit \( K \subset {\mathbb{R}}^{n} \) un compact. Comme \( K \) est fermé et que \( f \) est continue (car \( {\mathcal{C}}^{1} \) ), \( {f}^{-1}\left( K\right) \) est fermé. Il reste à montrer que \( {f}^{-1}\left( K\right) \) est borné pour montrer sa compacité.

> Solution. a) Let \( K \subset {\mathbb{R}}^{n} \) be a compact set. Since \( K \) is closed and \( f \) is continuous (because \( {\mathcal{C}}^{1} \) ), \( {f}^{-1}\left( K\right) \) is closed. It remains to show that \( {f}^{-1}\left( K\right) \) is bounded to prove its compactness.

Comme \( K \) est compact donc borné, il existe \( M > 0 \) tel que \( \parallel x\parallel \leq M \) pour tout \( x \in K \) . Or

> Since \( K \) is compact and therefore bounded, there exists \( M > 0 \) such that \( \parallel x\parallel \leq M \) for all \( x \in K \) . However

\[
\mathop{\lim }\limits_{{\parallel x\parallel  \rightarrow   + \infty }}\parallel f\left( x\right) \parallel  =  + \infty \;\text{ donc }\;\exists A > 0,\forall x \in  {\mathbb{R}}^{n},\parallel x\parallel  > A,\;\parallel f\left( x\right) \parallel  > M.
\]

Ainsi, si \( x \in {f}^{-1}\left( K\right) \) , on a \( \parallel x\parallel \leq A \) , d’où le résultat.

> Thus, if \( x \in {f}^{-1}\left( K\right) \) , we have \( \parallel x\parallel \leq A \) , hence the result.

b) On va montrer que \( f\left( {\mathbb{R}}^{n}\right) \) est à la fois ouvert et fermé. Comme \( {\mathbb{R}}^{n} \) est connexe, on en déduira \( f\left( {\mathbb{R}}^{n}\right) = {\mathbb{R}}^{n} \) , c’est-à-dire la surjectivité de \( f \) .

> b) We will show that \( f\left( {\mathbb{R}}^{n}\right) \) is both open and closed. Since \( {\mathbb{R}}^{n} \) is connected, we will deduce \( f\left( {\mathbb{R}}^{n}\right) = {\mathbb{R}}^{n} \), that is, the surjectivity of \( f \).

Pour tout \( x \in {\mathbb{R}}^{n}, d{f}_{x} \) est inversible, donc \( f \) est une application ouverte (voir le corollaire 1 page 343). En particulier, \( f\left( {\mathbb{R}}^{n}\right) \) est un ouvert de \( {\mathbb{R}}^{n} \) .

> For all \( x \in {\mathbb{R}}^{n}, d{f}_{x} \) is invertible, so \( f \) is an open mapping (see corollary 1 on page 343). In particular, \( f\left( {\mathbb{R}}^{n}\right) \) is an open subset of \( {\mathbb{R}}^{n} \).

Enfin, nous avons vu que pour tout compact \( K \) de \( {\mathbb{R}}^{n},{f}^{-1}\left( K\right) \) est compact. On sait alors (ou alors on le retrouve, voir l’exercice 1 page 31) que \( f \) est une application fermée. En particulier, \( f\left( {\mathbb{R}}^{n}\right) \) est fermé.

> Finally, we have seen that for any compact \( K \) of \( {\mathbb{R}}^{n},{f}^{-1}\left( K\right) \) is compact. We know then (or we can derive it, see exercise 1 on page 31) that \( f \) is a closed mapping. In particular, \( f\left( {\mathbb{R}}^{n}\right) \) is closed.

c) Commençons par montrer que les points de \( {f}^{-1}\left( {\{ y\} }\right) \) sont isolés. Soit \( {x}_{0} \in {f}^{-1}\left( {\{ y\} }\right) \) , de sorte que \( f\left( {x}_{0}\right) = y \) . Comme \( d{f}_{{x}_{0}} \) est inversible, on peut appliquer le théorème d’inversion locale qui nous dit que \( f \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme local autour de \( {x}_{0} \) . En d’autres termes, il existe un ouvert \( V \) contenant \( {x}_{0} \) tel que \( {f}_{\mid V} \) soit une bijection de \( V \) sur \( f\left( V\right) \) . En particulier, \( f \) est injective sur \( V \) , donc pour tout \( x \neq {x}_{0} \) et \( x \in V, f\left( x\right) \neq f\left( {x}_{0}\right) = y \) , c’est-à-dire \( V \cap {f}^{-1}\left( {\{ y\} }\right) = \left\{ {x}_{0}\right\} \) .

> c) Let us begin by showing that the points of \( {f}^{-1}\left( {\{ y\} }\right) \) are isolated. Let \( {x}_{0} \in {f}^{-1}\left( {\{ y\} }\right) \), such that \( f\left( {x}_{0}\right) = y \). Since \( d{f}_{{x}_{0}} \) is invertible, we can apply the local inversion theorem which tells us that \( f \) is a local \( {\mathcal{C}}^{1} \)-diffeomorphism around \( {x}_{0} \). In other words, there exists an open set \( V \) containing \( {x}_{0} \) such that \( {f}_{\mid V} \) is a bijection from \( V \) onto \( f\left( V\right) \). In particular, \( f \) is injective on \( V \), so for all \( x \neq {x}_{0} \) and \( x \in V, f\left( x\right) \neq f\left( {x}_{0}\right) = y \), that is \( V \cap {f}^{-1}\left( {\{ y\} }\right) = \left\{ {x}_{0}\right\} \).

Or d’après a), \( {f}^{-1}\left( {\{ y\} }\right) \) est compact. Un compact dont tous les éléments sont des points isolés est un ensemble fini (s'il était infini, il contiendrait un point d'accumulation, qui n'est pas isolé), donc \( {f}^{-1}\left( {\{ y\} }\right) \) est fini.

> However, according to a), \( {f}^{-1}\left( {\{ y\} }\right) \) is compact. A compact set whose elements are all isolated points is a finite set (if it were infinite, it would contain an accumulation point, which is not isolated), so \( {f}^{-1}\left( {\{ y\} }\right) \) is finite.

d) Raisonnons par l'absurde. Si le résultat était faux, alors

> d) Let us reason by contradiction. If the result were false, then

\[
\forall p \in  \mathbb{N},\;{f}^{-1}\left( {\mathrm{\;B}\left( {y,\frac{1}{{2}^{p}}}\right) }\right)  \text{ ⊄ } \mathop{\bigcup }\limits_{{1 \leq  i \leq  m}}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) .
\]

En d’autre termes, il existe pour tout \( p \in \mathbb{N} \) un élément \( {z}_{p} \) vérifiant \( \begin{Vmatrix}{f\left( {z}_{p}\right) - y}\end{Vmatrix} \leq 1/{2}^{p} \) tel que \( {z}_{p} \notin \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) pour tout \( i \) . La suite \( \left( {z}_{p}\right) \) est à valeurs dans le compact \( {f}^{-1}\left( {{\mathrm{\;B}}_{\mathrm{f}}\left( {y,1}\right) }\right) \) , on peut donc en extraire une sous-suite convergente \( \left( {z}_{\varphi \left( p\right) }\right) \) , de limite \( z \) . Comme \( f \) est continue, et que \( \begin{Vmatrix}{f\left( {z}_{p}\right) - y}\end{Vmatrix} \leq 1/{2}^{p} \) pour tout \( p \) , on a \( f\left( z\right) = y \) . Il existe donc \( i,1 \leq i \leq m \) , tel que \( z = {x}_{i} \) , et comme \( \left( {z}_{\varphi \left( p\right) }\right) \) converge vers \( z = {x}_{i} \) , il existe \( P \in \mathbb{N} \) tel que \( {z}_{\varphi \left( p\right) } \in \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) pour tout \( p \geq P \) . Ceci est impossible par construction des \( {z}_{p} \) , d’où le résultat.

> In other words, for every \( p \in \mathbb{N} \) there exists an element \( {z}_{p} \) satisfying \( \begin{Vmatrix}{f\left( {z}_{p}\right) - y}\end{Vmatrix} \leq 1/{2}^{p} \) such that \( {z}_{p} \notin \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) for all \( i \) . The sequence \( \left( {z}_{p}\right) \) takes values in the compact set \( {f}^{-1}\left( {{\mathrm{\;B}}_{\mathrm{f}}\left( {y,1}\right) }\right) \) , so we can extract a convergent subsequence \( \left( {z}_{\varphi \left( p\right) }\right) \) , with limit \( z \) . Since \( f \) is continuous, and \( \begin{Vmatrix}{f\left( {z}_{p}\right) - y}\end{Vmatrix} \leq 1/{2}^{p} \) for all \( p \) , we have \( f\left( z\right) = y \) . There therefore exists \( i,1 \leq i \leq m \) such that \( z = {x}_{i} \) , and since \( \left( {z}_{\varphi \left( p\right) }\right) \) converges to \( z = {x}_{i} \) , there exists \( P \in \mathbb{N} \) such that \( {z}_{\varphi \left( p\right) } \in \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) for all \( p \geq P \) . This is impossible by the construction of \( {z}_{p} \) , hence the result.

e) Nous allons nous servir du résultat de la question précédente. Pour cela, il faut choisir correctement \( \varepsilon > 0 \) .

> e) We will use the result from the previous question. To do this, we must choose \( \varepsilon > 0 \) correctly.

Pour tout \( i, d{f}_{{x}_{i}} \) est inversible, donc d’après le théorème d’inversion locale, il existe \( {\varepsilon }_{i} > 0 \) tel que \( f \) soit injective sur \( \mathrm{B}\left( {{x}_{i},{\varepsilon }_{i}}\right) \) . Si \( \varepsilon = \mathop{\inf }\limits_{{1 \leq i \leq m}}{\varepsilon }_{i} \) , on a donc \( \varepsilon > 0 \) et \( f \) est injective sur chaque \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) . Quitte à diminuer \( \varepsilon > 0 \) , on peut supposer que les boules \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) sont disjointes.

> For all \( i, d{f}_{{x}_{i}} \) is invertible, so by the local inversion theorem, there exists \( {\varepsilon }_{i} > 0 \) such that \( f \) is injective on \( \mathrm{B}\left( {{x}_{i},{\varepsilon }_{i}}\right) \) . If \( \varepsilon = \mathop{\inf }\limits_{{1 \leq i \leq m}}{\varepsilon }_{i} \) , we therefore have \( \varepsilon > 0 \) and \( f \) is injective on each \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) . By potentially shrinking \( \varepsilon > 0 \) , we can assume that the balls \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) are disjoint.

D’après la question précédente, on peut trouver un voisinage ouvert \( V \) de \( y \) tel que \( {f}^{-1}\left( V\right) \subset \; { \cup }_{1 \leq i \leq m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) . Posons alors \( W = V \cap \Gamma \) , où \( \Gamma = { \cap }_{1 \leq i \leq m}f\left( {\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) }\right) \) . L’ensemble \( W \) est un voisinage ouvert de \( y \) (car nous avons montré à la question b) que \( f \) est une application ouverte). Par ailleurs,

> According to the previous question, we can find an open neighborhood \( V \) of \( y \) such that \( {f}^{-1}\left( V\right) \subset \; { \cup }_{1 \leq i \leq m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) . Let us then set \( W = V \cap \Gamma \) , where \( \Gamma = { \cap }_{1 \leq i \leq m}f\left( {\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) }\right) \) . The set \( W \) is an open neighborhood of \( y \) (because we showed in question b) that \( f \) is an open mapping). Furthermore,

- pour tout \( z \in  W \) , on a \( z \in  \Gamma \) donc pour tout \( i,1 \leq  i \leq  m \) , il existe \( {x}_{i}^{\prime } \in  \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) tel que \( z = f\left( {x}_{i}^{\prime }\right) \) . Comme les \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) sont disjoints, on en déduit Card \( \left\lbrack  {{f}^{-1}\left( z\right) }\right\rbrack   \geq  m \) .

> - for all \( z \in  W \) , we have \( z \in  \Gamma \) so for all \( i,1 \leq  i \leq  m \) , there exists \( {x}_{i}^{\prime } \in  \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) such that \( z = f\left( {x}_{i}^{\prime }\right) \) . Since the \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) are disjoint, we deduce Card \( \left\lbrack  {{f}^{-1}\left( z\right) }\right\rbrack   \geq  m \) .

- Pour tout \( z \in  W \) , on a \( z \in  V \) donc \( {f}^{-1}\left( {\{ z\} }\right)  \subset  {f}^{-1}\left( V\right)  \subset  { \cup  }_{1 \leq  i \leq  m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) , et comme \( f \) est injective sur chaque \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) , on a \( \operatorname{Card}\left\lbrack  {{f}^{-1}\left( {\{ z\} }\right) }\right\rbrack   \leq  m \) .

> - For all \( z \in  W \) , we have \( z \in  V \) so \( {f}^{-1}\left( {\{ z\} }\right)  \subset  {f}^{-1}\left( V\right)  \subset  { \cup  }_{1 \leq  i \leq  m}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) , and since \( f \) is injective on each \( \mathrm{B}\left( {{x}_{i},\varepsilon }\right) \) , we have \( \operatorname{Card}\left\lbrack  {{f}^{-1}\left( {\{ z\} }\right) }\right\rbrack   \leq  m \) .

On en déduit Card \( \left\lbrack {{f}^{-1}\left( {\{ z\} }\right) }\right\rbrack = m \) pour tout \( z \in W \) .

> We deduce Card \( \left\lbrack {{f}^{-1}\left( {\{ z\} }\right) }\right\rbrack = m \) for all \( z \in W \) .

f) D’après la question précédente, l’ensemble \( {\Gamma }_{m} = \left\{ {z \in {\mathbb{R}}^{n} \mid \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = m}\right\} \) est un ouvert. Or \( f \) est surjective et \( {f}^{-1}\left( {\{ z\} }\right) \) est fini pour tout \( z \in {\mathbb{R}}^{n} \) , donc

> f) According to the previous question, the set \( {\Gamma }_{m} = \left\{ {z \in {\mathbb{R}}^{n} \mid \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = m}\right\} \) is an open set. However \( f \) is surjective and \( {f}^{-1}\left( {\{ z\} }\right) \) is finite for all \( z \in {\mathbb{R}}^{n} \) , therefore

\[
{\mathbb{R}}^{n} = \mathop{\bigcup }\limits_{{m \in  {\mathbb{N}}^{ * }}}{\Gamma }_{m} = {\Gamma }_{{m}_{0}}\bigcup \left\lbrack  {\mathop{\bigcup }\limits_{\substack{{m \neq  {m}_{o}} \\  {m > 0} }}{\Gamma }_{m}}\right\rbrack  ,\;\text{ où }\;{m}_{0} = \operatorname{Card}{f}^{-1}\left( {\{ 0\} }\right) .
\]

Ainsi, \( {\mathbb{R}}^{n} \) est la réunion des deux ouverts \( {\Gamma }_{{m}_{0}} \) et \( { \cup }_{m \neq {m}_{0}}{\Gamma }_{m} \) . Comme \( {\mathbb{R}}^{n} \) est connexe, que ces ouverts sont disjoints et que \( {\Gamma }_{{m}_{0}} \neq \varnothing \) (car \( 0 \in {\Gamma }_{{m}_{0}} \) ) on en tire \( {\Gamma }_{{m}_{0}} = {\mathbb{R}}^{n} \) . En d’autres termes, \( \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = {m}_{0} \) pour tout \( z \in {\mathbb{R}}^{n} \) .

> Thus, \( {\mathbb{R}}^{n} \) is the union of the two open sets \( {\Gamma }_{{m}_{0}} \) and \( { \cup }_{m \neq {m}_{0}}{\Gamma }_{m} \) . Since \( {\mathbb{R}}^{n} \) is connected, that these open sets are disjoint and that \( {\Gamma }_{{m}_{0}} \neq \varnothing \) (because \( 0 \in {\Gamma }_{{m}_{0}} \) ) we derive \( {\Gamma }_{{m}_{0}} = {\mathbb{R}}^{n} \) . In other words, \( \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = {m}_{0} \) for all \( z \in {\mathbb{R}}^{n} \) .

g) Les hypothèses s’écrivent aussi \( {f}^{-1}\left( {\{ 0\} }\right) = \{ 0\} \) . Donc \( {m}_{0} = 1 \) , donc d’après la question précédente, \( \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = 1 \) pour tout \( z \in {\mathbb{R}}^{n} \) . Autrement dit, \( f \) est bijective. On conclut avec le corollaire 4 page 344 (inversion globale) que \( f \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme global.

> g) The hypotheses can also be written \( {f}^{-1}\left( {\{ 0\} }\right) = \{ 0\} \) . So \( {m}_{0} = 1 \) , therefore according to the previous question, \( \operatorname{Card}{f}^{-1}\left( {\{ z\} }\right) = 1 \) for all \( z \in {\mathbb{R}}^{n} \) . In other words, \( f \) is bijective. We conclude with corollary 4 on page 344 (global inversion) that \( f \) is a global \( {\mathcal{C}}^{1} \) -diffeomorphism.
