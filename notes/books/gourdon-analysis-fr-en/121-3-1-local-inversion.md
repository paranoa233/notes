#### 3.1. Local inversion

*Français : 3.1. Inversion locale*

Pour une fonction \( f : \mathbb{R} \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{1} \) , on sait que si \( {f}^{\prime }\left( x\right) \neq 0 \) pour tout \( x \) , alors \( f \) admet un inverse global \( {f}^{-1} \) de classe \( {\mathcal{C}}^{1} \) qui vérifie \( {\left( {f}^{-1}\right) }^{\prime }\left\lbrack {f\left( x\right) }\right\rbrack = 1/{f}^{\prime }\left( x\right) \) pour tout \( x \) . Notre objectif est de généraliser ce résultat pour des fonctions de plusieurs variables, ou plus généralement pour des fonctions définies sur un espace de Banach. La condition " \( {f}^{\prime }\left( x\right) \neq 0 \) " devient ici " \( d{f}_{x} \) est inversible", et la fonction \( f \) est alors localement inversible autour de \( x \) (et non pas globalement comme dans le cas réel).

> For a function \( f : \mathbb{R} \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{1} \), we know that if \( {f}^{\prime }\left( x\right) \neq 0 \) for all \( x \), then \( f \) admits a global inverse \( {f}^{-1} \) of class \( {\mathcal{C}}^{1} \) which satisfies \( {\left( {f}^{-1}\right) }^{\prime }\left\lbrack {f\left( x\right) }\right\rbrack = 1/{f}^{\prime }\left( x\right) \) for all \( x \). Our goal is to generalize this result for functions of several variables, or more generally for functions defined on a Banach space. The condition "\( {f}^{\prime }\left( x\right) \neq 0 \)" here becomes "\( d{f}_{x} \) is invertible", and the function \( f \) is then locally invertible around \( x \) (and not globally as in the real case).

\( \rightarrow \) THÉORÉME 1 (INVERSION LOCALE). Soient \( E, F \) deux espaces de Banach, \( U \) un ouvert de \( E \) et \( f : U \rightarrow F \) une application de classe \( {\mathcal{C}}^{1} \) . On suppose qu’il existe \( a \in U \) tel que dfa soit un isomorphisme bicontinu de \( E \) sur \( F \) (i.e. \( d{f}_{a}^{-1} \) existe, \( d{f}_{a} \) et \( d{f}_{a}^{-1} \) sont continus). Alors il existe un voisinage ouvert \( V \) de a et un voisinage ouvert \( W \) de \( f\left( a\right) \) tels que

> \( \rightarrow \) THEOREM 1 (LOCAL INVERSION). Let \( E, F \) be two Banach spaces, \( U \) an open subset of \( E \), and \( f : U \rightarrow F \) a mapping of class \( {\mathcal{C}}^{1} \). Suppose there exists \( a \in U \) such that dfa is a bicontinuous isomorphism from \( E \) onto \( F \) (i.e., \( d{f}_{a}^{-1} \) exists, \( d{f}_{a} \) and \( d{f}_{a}^{-1} \) are continuous). Then there exists an open neighborhood \( V \) of a and an open neighborhood \( W \) of \( f\left( a\right) \) such that

(i) la restriction \( {f}_{\mid V} \) de \( f\dot{a}V \) est une bijection de \( V \) sur \( W \) ;

> (i) the restriction \( {f}_{\mid V} \) of \( f\dot{a}V \) is a bijection from \( V \) onto \( W \);

(ii) l’application inverse \( g : W \rightarrow V \) est continue ;

> (ii) the inverse mapping \( g : W \rightarrow V \) is continuous;

(iii) \( g \) est de classe \( {\mathcal{C}}^{1} \) et pour tout \( x \in V, d{g}_{f\left( x\right) } = d{f}_{x}^{-1} \) .

> (iii) \( g \) is of class \( {\mathcal{C}}^{1} \) and for all \( x \in V, d{g}_{f\left( x\right) } = d{f}_{x}^{-1} \).

Démonstration. Pour tout \( r > 0 \) , on note \( {B}_{r} \) la boule ouverte de centre 0 de rayon \( r \) , et \( {\bar{B}}_{r} \) la boule fermée correspondante. La norme utilisée sur \( {\mathcal{L}}_{c}\left( {E, F}\right) \) est \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \) .

> Proof. For all \( r > 0 \), we denote by \( {B}_{r} \) the open ball centered at 0 with radius \( r \), and by \( {\bar{B}}_{r} \) the corresponding closed ball. The norm used on \( {\mathcal{L}}_{c}\left( {E, F}\right) \) is \( \parallel u\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel u\left( x\right) \parallel \).

Quitte à considérer la fonction \( x \mapsto d{f}_{a}^{-1}\left\lbrack {f\left( {a + x}\right) - f\left( a\right) }\right\rbrack \) , on peut supposer \( a = 0, f\left( a\right) = 0 \) et \( d{f}_{0} = d{f}_{a} = {\operatorname{Id}}_{E} \) (et donc \( E = F \) ).

> By considering the function \( x \mapsto d{f}_{a}^{-1}\left\lbrack {f\left( {a + x}\right) - f\left( a\right) }\right\rbrack \), we can assume \( a = 0, f\left( a\right) = 0 \) and \( d{f}_{0} = d{f}_{a} = {\operatorname{Id}}_{E} \) (and thus \( E = F \)).

Comme \( f \) est de classe \( {\mathcal{C}}^{1} \) , il existe \( r > 0 \) tel que \( {\bar{B}}_{r} \subset U \) et \( \begin{Vmatrix}{d{f}_{x} - d{f}_{0}}\end{Vmatrix} = \begin{Vmatrix}{d{f}_{x} - {\operatorname{Id}}_{E}}\end{Vmatrix} \leq 1/2 \) pour tout \( x \in {B}_{r} \) . Considérons maintenant \( x \in {B}_{r} \) . On a \( d{f}_{x} = {\operatorname{Id}}_{E} - u \) avec \( \parallel u\parallel = \parallel i{d}_{E} - \; d{f}_{x}\parallel \leq 1/2 \) donc (voir la proposition 2 page 49) \( d{f}_{x} \) est un isomorphisme bicontinu qui vérifie \( d{f}_{x}^{-1} = {\operatorname{Id}}_{E} + u + \cdots + {u}^{n} + \cdots \) , et de plus

> Since \( f \) is of class \( {\mathcal{C}}^{1} \) , there exists \( r > 0 \) such that \( {\bar{B}}_{r} \subset U \) and \( \begin{Vmatrix}{d{f}_{x} - d{f}_{0}}\end{Vmatrix} = \begin{Vmatrix}{d{f}_{x} - {\operatorname{Id}}_{E}}\end{Vmatrix} \leq 1/2 \) for all \( x \in {B}_{r} \) . Now consider \( x \in {B}_{r} \) . We have \( d{f}_{x} = {\operatorname{Id}}_{E} - u \) with \( \parallel u\parallel = \parallel i{d}_{E} - \; d{f}_{x}\parallel \leq 1/2 \) so (see proposition 2 on page 49) \( d{f}_{x} \) is a bicontinuous isomorphism that satisfies \( d{f}_{x}^{-1} = {\operatorname{Id}}_{E} + u + \cdots + {u}^{n} + \cdots \) , and furthermore

\[
\begin{Vmatrix}{d{f}_{x}^{-1}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\parallel u{\parallel }^{n} \leq  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{{2}^{n}} = 2.
\]

(*)

> (i). Nous voulons montrer que \( f \) a un inverse local. Plus précisément, nous allons prouver que pour tout \( y \in {B}_{r/2} \) , il existe un unique \( x \in {B}_{r} \) vérifiant \( f\left( x\right) = y \) .

(i). We want to show that \( f \) has a local inverse. More precisely, we will prove that for all \( y \in {B}_{r/2} \) , there exists a unique \( x \in {B}_{r} \) satisfying \( f\left( x\right) = y \) .

> Fixons donc \( y \in {B}_{r/2} \) et considérons la fonction \( h : \;{B}_{r} \rightarrow E\;x \mapsto y + x - f\left( x\right) \) . Elle est de classe \( {\mathcal{C}}^{1} \) , et pour tout \( x \in {B}_{r},\begin{Vmatrix}{d{h}_{x}}\end{Vmatrix} = \begin{Vmatrix}{{\operatorname{Id}}_{E} - d{f}_{x}}\end{Vmatrix} \leq 1/2 \) , donc d’après l’inégalité des accroissements finis,

Let us fix \( y \in {B}_{r/2} \) and consider the function \( h : \;{B}_{r} \rightarrow E\;x \mapsto y + x - f\left( x\right) \) . It is of class \( {\mathcal{C}}^{1} \) , and for all \( x \in {B}_{r},\begin{Vmatrix}{d{h}_{x}}\end{Vmatrix} = \begin{Vmatrix}{{\operatorname{Id}}_{E} - d{f}_{x}}\end{Vmatrix} \leq 1/2 \) , so by the mean value inequality,

\[
\forall \left( {x,{x}^{\prime }}\right)  \in  {\bar{B}}_{r}^{2},\;\begin{Vmatrix}{h\left( x\right)  - h\left( {x}^{\prime }\right) }\end{Vmatrix} \leq  \frac{1}{2}\begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix}.
\]

\( \left( {* * }\right) \)

> En particulier, pour tout \( x \in {\bar{B}}_{r},\parallel x - f\left( x\right) \parallel = \parallel h\left( x\right) - h\left( 0\right) \parallel \leq \parallel x\parallel /2 \) donc

In particular, for all \( x \in {\bar{B}}_{r},\parallel x - f\left( x\right) \parallel = \parallel h\left( x\right) - h\left( 0\right) \parallel \leq \parallel x\parallel /2 \) so

\[
\forall x \in  {\bar{B}}_{r},\;\parallel h\left( x\right) \parallel  \leq  \parallel y\parallel  + \parallel x - f\left( x\right) \parallel  \leq  \parallel y\parallel  + \frac{1}{2}\parallel x\parallel  < \frac{r}{2} + \frac{r}{2} = r.
\]

Ainsi, \( h \) est une fonction de \( {\bar{B}}_{r} \) dans \( {B}_{r} \) , donc dans \( {\bar{B}}_{r} \) . Comme de plus \( h \) vérifie (**), on peut appliquer le théorème du point fixe qui entraîne l’existence et l’unicité de \( x \in {\bar{B}}_{r} \) tel que \( h\left( x\right) = x \) , et comme \( h \) est à valeurs dans \( {B}_{r}, x \in {B}_{r} \) . On a donc \( f\left( x\right) = y \) .

> Thus, \( h \) is a function from \( {\bar{B}}_{r} \) to \( {B}_{r} \) , so into \( {\bar{B}}_{r} \) . Since \( h \) also satisfies (**), we can apply the fixed-point theorem which implies the existence and uniqueness of \( x \in {\bar{B}}_{r} \) such that \( h\left( x\right) = x \) , and since \( h \) takes values in \( {B}_{r}, x \in {B}_{r} \) . We therefore have \( f\left( x\right) = y \) .

Résumons. Nous avons montré, pour tout \( y \in {B}_{r/2} \) , l’existence et l’unicité de \( x \in {B}_{r} \) tel que \( f\left( x\right) = y \) . En notant \( V = {f}^{-1}\left( {B}_{r/2}\right) \cap {B}_{r} \) (c’est un ouvert qui est un voisinage de0car \( f\left( 0\right) = 0 \) et \( f \) est continue en 0 ), ceci s’interprète en disant que \( {f}_{\mid V} : V \rightarrow W = {B}_{r/2} \) est une bijection.

> Let us summarize. We have shown, for all \( y \in {B}_{r/2} \) , the existence and uniqueness of \( x \in {B}_{r} \) such that \( f\left( x\right) = y \) . By denoting \( V = {f}^{-1}\left( {B}_{r/2}\right) \cap {B}_{r} \) (this is an open set which is a neighborhood of 0 because \( f\left( 0\right) = 0 \) and \( f \) is continuous at 0 ), this is interpreted by saying that \( {f}_{\mid V} : V \rightarrow W = {B}_{r/2} \) is a bijection.

(ii). Notons \( g : W \rightarrow V \) l’application inverse. Désignons par \( h \) l’application \( h : x \mapsto x - f\left( x\right) \) (c’est l’application \( h \) précédente avec \( y = 0 \) ), de sorte que \( x = h\left( x\right) + f\left( x\right) \) pour tout \( x \) . Pour montrer que \( g \) est continue, il suffit de remarquer que

> (ii). Let \( g : W \rightarrow V \) be the inverse mapping. Let \( h \) denote the mapping \( h : x \mapsto x - f\left( x\right) \) (this is the previous mapping \( h \) with \( y = 0 \) ), such that \( x = h\left( x\right) + f\left( x\right) \) for all \( x \) . To show that \( g \) is continuous, it suffices to note that

\[
\forall x,{x}^{\prime } \in  {B}_{r},\;\begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix} \leq  \begin{Vmatrix}{h\left( x\right)  - h\left( {x}^{\prime }\right) }\end{Vmatrix} + \begin{Vmatrix}{f\left( x\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix} \leq  \frac{1}{2}\begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix} + \begin{Vmatrix}{f\left( x\right)  - f\left( {x}^{\prime }\right) }\end{Vmatrix}
\]

donc \( \begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix} \leq 2\begin{Vmatrix}{f\left( x\right) - f\left( {x}^{\prime }\right) }\end{Vmatrix} \) . On en déduit

> thus \( \begin{Vmatrix}{x - {x}^{\prime }}\end{Vmatrix} \leq 2\begin{Vmatrix}{f\left( x\right) - f\left( {x}^{\prime }\right) }\end{Vmatrix} \) . We deduce from this

\[
\forall y,{y}^{\prime } \in  W,\;\begin{Vmatrix}{g\left( y\right)  - g\left( {y}^{\prime }\right) }\end{Vmatrix} \leq  2\begin{Vmatrix}{f\left( {g\left( y\right) }\right)  - f\left( {g\left( {y}^{\prime }\right) }\right) }\end{Vmatrix} = 2\begin{Vmatrix}{y - {y}^{\prime }}\end{Vmatrix},
\]

(***)

> autrement dit \( g \) est lipschitzienne, donc continue.

in other words \( g \) is Lipschitz, and therefore continuous.

> (iii). Fixons \( x \in V \) et posons \( y = f\left( x\right) \in W \) . Soit \( w \) tel que \( y + w \in W \) . On note \( v = \; g\left( {y + w}\right) - g\left( y\right) \) . On a \( \parallel v\parallel \leq 2\parallel w\parallel \) d’après (***), et

(iii). Let us fix \( x \in V \) and set \( y = f\left( x\right) \in W \) . Let \( w \) be such that \( y + w \in W \) . We denote \( v = \; g\left( {y + w}\right) - g\left( y\right) \) . We have \( \parallel v\parallel \leq 2\parallel w\parallel \) according to (***), and

\[
\Delta \left( w\right)  = g\left( {y + w}\right)  - g\left( y\right)  - d{f}_{x}^{-1}\left( w\right)
\]

\[
= \left( {x + v}\right)  - x - d{f}_{x}^{-1}\left\lbrack  {f\left( {x + v}\right)  - f\left( x\right) }\right\rbrack   =  - d{f}_{x}^{-1}\left\lbrack  {f\left( {x + v}\right)  - f\left( x\right)  - d{f}_{x}\left( v\right) }\right\rbrack  .
\]

Or \( \begin{Vmatrix}{d{f}_{x}^{-1}}\end{Vmatrix} \leq 2 \) d’après (*), donc

> However, \( \begin{Vmatrix}{d{f}_{x}^{-1}}\end{Vmatrix} \leq 2 \) according to (*), therefore

\[
\parallel \Delta \left( w\right) \parallel  \leq  2\parallel f\left( {x + v}\right)  - f\left( x\right)  - d{f}_{x}\left( v\right) \parallel  = 2\parallel v\parallel \varepsilon \left( v\right)
\]

avec \( \mathop{\lim }\limits_{{v \rightarrow 0}}\varepsilon \left( v\right) = 0 \) , donc

> with \( \mathop{\lim }\limits_{{v \rightarrow 0}}\varepsilon \left( v\right) = 0 \) , therefore

\[
\parallel \Delta \left( w\right) \parallel  \leq  4\parallel w\parallel \varepsilon \left\lbrack  {g\left( {y + w}\right)  - g\left( y\right) }\right\rbrack   = 4\parallel w\parallel {\varepsilon }^{\prime }\left( w\right) .
\]

La fonction \( g \) étant continue, on a \( \mathop{\lim }\limits_{{w \rightarrow 0}}{\varepsilon }^{\prime }\left( w\right) = 0 \) , donc \( \parallel \Delta \left( w\right) \parallel = o\left( {\parallel w\parallel }\right) \) . La fonction \( g \) est donc différentiable en \( y \) et \( d{g}_{y} = d{f}_{x}^{-1} \) .

> Since the function \( g \) is continuous, we have \( \mathop{\lim }\limits_{{w \rightarrow 0}}{\varepsilon }^{\prime }\left( w\right) = 0 \) , therefore \( \parallel \Delta \left( w\right) \parallel = o\left( {\parallel w\parallel }\right) \) . The function \( g \) is thus differentiable at \( y \) and \( d{g}_{y} = d{f}_{x}^{-1} \) .

Comme \( f \) est de classe \( {\mathcal{C}}^{1} \) , que la fonction \( g \) est continue et que Inv : \( u \mapsto {u}^{-1} \) est continue (Inv est même différentiable d’après l’exercice 5 page 331) l’application \( y \mapsto d{g}_{y} = d{f}_{g\left( y\right) }^{-1} \) est continue comme composée d’applications continues, donc \( g \) est de classe \( {\mathcal{C}}^{1} \) .

> Since \( f \) is of class \( {\mathcal{C}}^{1} \) , the function \( g \) is continuous, and Inv : \( u \mapsto {u}^{-1} \) is continuous (Inv is even differentiable according to exercise 5 on page 331), the mapping \( y \mapsto d{g}_{y} = d{f}_{g\left( y\right) }^{-1} \) is continuous as a composition of continuous mappings, therefore \( g \) is of class \( {\mathcal{C}}^{1} \) .

Remarque 1. Ce théorème est bien intuitif : sur un voisinage de \( a, f\left( x\right) \) et \( f\left( a\right) + d{f}_{a}\left( {x - a}\right) \) sont "proches", et \( d{f}_{a} \) étant inversible, il est donc naturel que \( f \) soit inversible sur un voisinage de \( a \) .

> Remark 1. This theorem is quite intuitive: on a neighborhood of \( a, f\left( x\right) \) , \( f\left( a\right) + d{f}_{a}\left( {x - a}\right) \) are "close", and since \( d{f}_{a} \) is invertible, it is natural that \( f \) is invertible on a neighborhood of \( a \) .

COROLLAIRE 1. Soient \( E \) et \( F \) deux espaces de Banach, et \( U \) un ouvert de \( E \) . Soit \( f : U \rightarrow F \) une application de classe \( {\mathcal{C}}^{1} \) telle que pour tout \( x \in U, d{f}_{x} \) soit inversible et bicontinu. Alors \( f \) est une application ouverte, \( c \) ’est-à-dire que pour tout ouvert \( \Omega \subset U \) , \( f\left( \Omega \right) \) est un ouvert de \( F \) .

> COROLLARY 1. Let \( E \) and \( F \) be two Banach spaces, and \( U \) an open set of \( E \). Let \( f : U \rightarrow F \) be a class \( {\mathcal{C}}^{1} \) application such that for every \( x \in U, d{f}_{x} \) it is invertible and bicontinuous. Then \( f \) is an open application, that is to say that for every open set \( \Omega \subset U \), \( f\left( \Omega \right) \) is an open set of \( F \).

Démonstration. Soit \( \Omega \) un ouvert de \( U \) et \( x \in \Omega \) . D’après le théorème d’inversion locale, on peut trouver un voisinage ouvert \( {V}_{x} \subset \Omega \) et un voisinage ouvert \( {W}_{x} \) de \( f\left( x\right) \) tels que \( {f}_{\mid {V}_{x}} \) soit une bijection de \( {V}_{x} \) sur \( {W}_{x} \) . En particulier, \( f\left( {V}_{x}\right) = {W}_{x} \) . On en déduit que

> Proof. Let \( \Omega \) be an open set of \( U \) and \( x \in \Omega \) . According to the local inversion theorem, we can find an open neighborhood \( {V}_{x} \subset \Omega \) and an open neighborhood \( {W}_{x} \) of \( f\left( x\right) \) such that \( {f}_{\mid {V}_{x}} \) is a bijection from \( {V}_{x} \) onto \( {W}_{x} \) . In particular, \( f\left( {V}_{x}\right) = {W}_{x} \) . We deduce that

\[
f\left( \Omega \right)  = f\left( {\mathop{\bigcup }\limits_{{x \in  \Omega }}{V}_{x}}\right)  = \mathop{\bigcup }\limits_{{x \in  \Omega }}f\left( {V}_{x}\right)  = \mathop{\bigcup }\limits_{{x \in  \Omega }}{W}_{x}
\]

est un ouvert de \( F \) .

> is an open set of \( F \) .

COROLLAIRE 2 (INVERSION GLOBALE). Soient \( E \) et \( F \) deux espaces de Banach, \( U \) un ouvert de \( E \) , et \( f : U \rightarrow F \) une fonction injective et de classe \( {\mathcal{C}}^{1} \) . Les assertions suivantes sont équivalentes :

> COROLLARY 2 (GLOBAL INVERSION). Let \( E \) and \( F \) be two Banach spaces, \( U \) an open set of \( E \) , and \( f : U \rightarrow F \) an injective function of class \( {\mathcal{C}}^{1} \) . The following assertions are equivalent:

(i) pour tout \( x \in U, d{f}_{x} \) est inversible et bicontinu ;

> (i) for all \( x \in U, d{f}_{x} \) is invertible and bicontinuous;

(ii) \( V = f\left( U\right) \) est un ouvert de \( F \) et \( {f}^{-1} : V \rightarrow U \) est de classe \( {\mathcal{C}}^{1} \) .

> (ii) \( V = f\left( U\right) \) is an open set of \( F \) and \( {f}^{-1} : V \rightarrow U \) is of class \( {\mathcal{C}}^{1} \) .

Démonstration. \( \left( i\right) \Rightarrow \left( {ii}\right) \) . D’après le corollaire précédent, que \( V = f\left( U\right) \) est ouvert. La fonc-tion \( f \) est donc une bijection de l’ouvert \( U \) sur l’ouvert \( V \) . Soit \( x \in U \) et \( y = f\left( x\right) \in V \) . D’après le théorème d’inversion locale, on peut trouver un voisinage ouvert \( A \) de \( x \) et un voisinage ouvert \( B \) de \( f\left( x\right) \) tels que \( {f}_{\mid A} : A \rightarrow B \) soit bijective et \( {f}_{\mid A}^{-1} \) soit de classe \( {\mathcal{C}}^{1} \) . Comme \( {\left( {f}^{-1}\right) }_{\mid B} = {\left( {f}_{\mid A}\right) }^{-1} \) , on en déduit que \( {f}^{-1} \) est de classe \( {\mathcal{C}}^{1} \) sur un voisinage de \( f\left( x\right) \) (ici \( B \) ), et ceci est vrai pour tout \( x \in V \) , donc \( {f}^{-1} \) est de classe \( {\mathcal{C}}^{1} \) sur \( V \) .

> Proof. \( \left( i\right) \Rightarrow \left( {ii}\right) \) . According to the previous corollary, \( V = f\left( U\right) \) is open. The function \( f \) is therefore a bijection from the open set \( U \) onto the open set \( V \) . Let \( x \in U \) and \( y = f\left( x\right) \in V \) . According to the local inversion theorem, we can find an open neighborhood \( A \) of \( x \) and an open neighborhood \( B \) of \( f\left( x\right) \) such that \( {f}_{\mid A} : A \rightarrow B \) is bijective and \( {f}_{\mid A}^{-1} \) is of class \( {\mathcal{C}}^{1} \) . Since \( {\left( {f}^{-1}\right) }_{\mid B} = {\left( {f}_{\mid A}\right) }^{-1} \) , we deduce that \( {f}^{-1} \) is of class \( {\mathcal{C}}^{1} \) on a neighborhood of \( f\left( x\right) \) (here \( B \) ), and this is true for all \( x \in V \) , so \( {f}^{-1} \) is of class \( {\mathcal{C}}^{1} \) on \( V \) .

(ii) \( \Rightarrow \) (i). Notons \( g = {f}^{-1} \) . On a \( g \circ f = {\operatorname{Id}}_{U} \) , donc \( f \) et \( g \) étant de classe \( {\mathcal{C}}^{1}, d{g}_{f\left( x\right) } \circ d{f}_{x} = \; {\operatorname{Id}}_{E} \) pour tout \( x \in U \) . De même, la relation \( f \circ g = {\operatorname{Id}}_{V} \) entraîne \( d{f}_{x} \circ d{g}_{f\left( x\right) } = {\operatorname{Id}}_{F} \) pour tout \( x \in U \) . On en déduit que pour tout \( x \in U, d{f}_{x} \) est inversible, d’inverse \( d{g}_{f\left( x\right) } \) donc continu.

> (ii) \( \Rightarrow \) (i). Let \( g = {f}^{-1} \) . We have \( g \circ f = {\operatorname{Id}}_{U} \) , so \( f \) and \( g \) are of class \( {\mathcal{C}}^{1}, d{g}_{f\left( x\right) } \circ d{f}_{x} = \; {\operatorname{Id}}_{E} \) for all \( x \in U \) . Similarly, the relation \( f \circ g = {\operatorname{Id}}_{V} \) implies \( d{f}_{x} \circ d{g}_{f\left( x\right) } = {\operatorname{Id}}_{F} \) for all \( x \in U \) . We deduce that for all \( x \in U, d{f}_{x} \) is invertible, with inverse \( d{g}_{f\left( x\right) } \) which is therefore continuous.

Remarque 2. D'après le théorème de Banach (voir exercice 6 page 423), une application linéaire continue bijective de \( E \) dans \( F \) a son inverse continu. Dans les résultats précédents, on peut donc remplacer l’hypothèse " \( d{f}_{x} \) est inversible et bicontinu" par " \( d{f}_{x} \) est inversible" ( \( d{f}_{x} \) est forcément continu par définition d’une différentielle).

> Remark 2. According to the Banach theorem (see exercise 6 page 423), a bijective continuous linear map from \( E \) to \( F \) has a continuous inverse. In the previous results, we can therefore replace the hypothesis "\( d{f}_{x} \) is invertible and bicontinuous" with "\( d{f}_{x} \) is invertible" (\( d{f}_{x} \) is necessarily continuous by the definition of a differential).

Cas des fonctions définies sur \( {\mathbb{R}}^{n} \) .

> Case of functions defined on \( {\mathbb{R}}^{n} \).

DéFINITION 1. Soient \( U \) et \( V \) deux ouverts de \( {\mathbb{R}}^{n} \) et une application \( f : U \rightarrow V \) . On dit que \( f \) est un \( {\mathcal{C}}^{k} \) -difféomorphisme \( \left( {k \geq 1}\right) \) , si \( f \) est bijective, de classe \( {\mathcal{C}}^{k} \) et si \( {f}^{-1} \) est de classe \( {\mathcal{C}}^{k} \) .

> DEFINITION 1. Let \( U \) and \( V \) be two open sets of \( {\mathbb{R}}^{n} \) and \( f : U \rightarrow V \) be a map. We say that \( f \) is a \( {\mathcal{C}}^{k} \)-diffeomorphism \( \left( {k \geq 1}\right) \) if \( f \) is bijective, of class \( {\mathcal{C}}^{k} \), and if \( {f}^{-1} \) is of class \( {\mathcal{C}}^{k} \).

Une autre conséquence du théorème d'inversion locale est la suivante.

> Another consequence of the local inversion theorem is the following.

COROLLAIRE 3. Soit \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) ) de classe \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . S’il existe \( a \in U \) tel que \( d{f}_{a} \) soit inversible (en termes équivalents, si le jacobien de \( f \) en a n’est pas nul), alors il existe un voisinage ouvert \( V \) de a et un voisinage ouvert \( W \) de \( f\left( a\right) \) tels que \( {f}_{\mid V} \) soit un \( {\mathcal{C}}^{k} \) -difféomorphisme de \( V \) sur \( W \) . On a alors \( d{\left( {f}_{\mid V}^{-1}\right) }_{f\left( x\right) } = d{f}_{x}^{-1} \) pour tout \( x \in V \) .

> COROLLARY 3. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( U \) is an open set of \( {\mathbb{R}}^{n} \)) be of class \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \). If there exists \( a \in U \) such that \( d{f}_{a} \) is invertible (in equivalent terms, if the Jacobian of \( f \) at a is non-zero), then there exists an open neighborhood \( V \) of a and an open neighborhood \( W \) of \( f\left( a\right) \) such that \( {f}_{\mid V} \) is a \( {\mathcal{C}}^{k} \)-diffeomorphism from \( V \) onto \( W \). We then have \( d{\left( {f}_{\mid V}^{-1}\right) }_{f\left( x\right) } = d{f}_{x}^{-1} \) for all \( x \in V \).

Démonstration. L’endomorphisme \( d{f}_{a} \) est inversible, donc bicontinu (on est en dimension finie). Le théorème d’inversion locale assure alors l’existence de deux voisinages ouverts \( V \) de \( a \) et \( W \) de \( f\left( a\right) \) tels que \( {f}_{\mid V} \) soit un \( {\mathcal{C}}^{1} \) difféomorphisme de \( V \) sur \( W \) , et donne \( d{\left( {f}_{\mid V}^{-1}\right) }_{f\left( x\right) } = d{f}_{x}^{-1} \) pour tout \( x \in V \) . Il nous reste à montrer que \( g = {f}_{\mid V}^{-1} \) est de classe \( {\mathcal{C}}^{k} \) .

> Proof. The endomorphism \( d{f}_{a} \) is invertible, therefore bicontinuous (we are in finite dimension). The local inversion theorem then ensures the existence of two open neighborhoods \( V \) of \( a \) and \( W \) of \( f\left( a\right) \) such that \( {f}_{\mid V} \) is a \( {\mathcal{C}}^{1} \) diffeomorphism from \( V \) onto \( W \), and gives \( d{\left( {f}_{\mid V}^{-1}\right) }_{f\left( x\right) } = d{f}_{x}^{-1} \) for all \( x \in V \). It remains for us to show that \( g = {f}_{\mid V}^{-1} \) is of class \( {\mathcal{C}}^{k} \).

En notant \( {J}_{f\left( x\right) }^{\prime } \) (resp. \( {J}_{x} \) ) la matrice jacobienne de \( g = {f}_{\mid V}^{-1} \) en \( f\left( x\right) \) (resp. de \( f \) en \( x \) ), l’égalité \( d{g}_{f\left( x\right) } = d{f}_{x}^{-1} \) s’écrit aussi \( {J}_{f\left( x\right) }^{\prime } = {J}_{x}^{-1} = {\left( \det {J}_{x}\right) }^{-1}{}^{t}{\widetilde{J}}_{x} \) , où \( {\widetilde{J}}_{x} \) désigne la comatrice de \( {J}_{x} \) . Les dérivées partielles du premier ordre de \( g \) au point \( f\left( x\right) \) s’expriment donc comme des fractions rationnelles en les dérivées partielles du premier ordre de \( f \) en \( x \) . Ainsi, les fonctions \( \frac{\partial g}{\partial {x}_{i}} \circ f \) sont de classe \( {\mathcal{C}}^{k - 1} \) . On conclut par récurrence sur \( k \) que les \( \frac{\partial g}{\partial {x}_{i}} \) sont de classe \( {\mathcal{C}}^{k - 1} \) , donc \( g \) est bien de classe \( {\mathcal{C}}^{k} \) .

> By denoting \( {J}_{f\left( x\right) }^{\prime } \) (resp. \( {J}_{x} \)) the Jacobian matrix of \( g = {f}_{\mid V}^{-1} \) at \( f\left( x\right) \) (resp. of \( f \) at \( x \)), the equality \( d{g}_{f\left( x\right) } = d{f}_{x}^{-1} \) can also be written as \( {J}_{f\left( x\right) }^{\prime } = {J}_{x}^{-1} = {\left( \det {J}_{x}\right) }^{-1}{}^{t}{\widetilde{J}}_{x} \), where \( {\widetilde{J}}_{x} \) denotes the comatrix of \( {J}_{x} \). The first-order partial derivatives of \( g \) at point \( f\left( x\right) \) are therefore expressed as rational fractions of the first-order partial derivatives of \( f \) at \( x \). Thus, the functions \( \frac{\partial g}{\partial {x}_{i}} \circ f \) are of class \( {\mathcal{C}}^{k - 1} \). We conclude by induction on \( k \) that the \( \frac{\partial g}{\partial {x}_{i}} \) are of class \( {\mathcal{C}}^{k - 1} \), so \( g \) is indeed of class \( {\mathcal{C}}^{k} \).

De la même manière que le corollaire 2, on peut montrer le corollaire suivant :

> In the same way as corollary 2, we can show the following corollary:

COROLLAIRE 4 (INVERSION GLOBALE). Soit \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) ) une application injective et de classe \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . Alors les assertions suivantes sont équivalentes :

> COROLLARY 4 (GLOBAL INVERSION). Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( U \) is an open set of \( {\mathbb{R}}^{n} \)) be an injective map of class \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \). Then the following assertions are equivalent:

(i) pour tout \( x \in U, d{f}_{x} \) est inversible ;

> (i) for all \( x \in U, d{f}_{x} \) is invertible;

(ii) \( V = f\left( U\right) \) est ouvert et \( f \) est un \( {\mathcal{C}}^{k} \) -difféomorphisme de \( U \) sur \( V \) .

> (ii) \( V = f\left( U\right) \) is open and \( f \) is a \( {\mathcal{C}}^{k} \)-diffeomorphism from \( U \) onto \( V \).

Remarque 3. Il se peut que \( d{f}_{x} \) soit inversible pour tout \( x \in U \) et que \( f \) ne soit pas injective (prendre par exemple \( f : {\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {{e}^{x}\cos y,{e}^{x}\sin y}\right) ) \) .

> Remark 3. It is possible for \( d{f}_{x} \) to be invertible for all \( x \in U \) while \( f \) is not injective (take, for example, \( f : {\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{2}\;\left( {x, y}\right) \mapsto \left( {{e}^{x}\cos y,{e}^{x}\sin y}\right) ) \)).
