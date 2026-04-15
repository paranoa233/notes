#### 5.2. Continuity of linear maps

*Français : 5.2. Continuité des applications linéaires*

Dans toute cette sous-partie, \( E \) et \( F \) désignent deux \( \mathbb{K} \) -e.v.n (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ).

> Throughout this subsection, \( E \) and \( F \) denote two \( \mathbb{K} \)-n.v.s (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \)).

THÉORÉME 1. Soit \( f \in \mathcal{L}\left( {E, F}\right) \) une application linéaire de \( E \) dans \( F \) . Les assertions qui suivent sont équivalentes.

> THEOREM 1. Let \( f \in \mathcal{L}\left( {E, F}\right) \) be a linear map from \( E \) to \( F \). The following assertions are equivalent.

(i) \( f \) est continue sur \( E \) ;

> (i) \( f \) is continuous on \( E \);

(ii) \( f \) est continue en0;

> (ii) \( f \) is continuous at 0;

(iii) \( f \) est bornée sur la boule unité fermée \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) de \( E \) ;

> (iii) \( f \) is bounded on the closed unit ball \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) of \( E \) ;

(iv) \( f \) est bornée sur la sphère unité \( \mathrm{S}\left( {0,1}\right) \) de \( E \) ;

> (iv) \( f \) is bounded on the unit sphere \( \mathrm{S}\left( {0,1}\right) \) of \( E \) ;

(v) il existe \( M > 0 \) tel que \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) pour tout \( x \in E \) ;

> (v) there exists \( M > 0 \) such that \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) for all \( x \in E \) ;

(vi) \( f \) est lipschitzienne ;

> (vi) \( f \) is Lipschitz continuous ;

(vii) \( f \) est uniformément continue sur \( E \) .

> (vii) \( f \) is uniformly continuous on \( E \) .

Remarque 1. - Dans la pratique, on utilise souvent les assertions (iv) et (v).

> Remark 1. - In practice, assertions (iv) and (v) are often used.

- De même, on montre qu’une application multilinéaire de \( {E}_{1} \times  \cdots  \times  {E}_{n} \) dans \( F \) est continue si et seulement si

> - Similarly, it can be shown that a multilinear map from \( {E}_{1} \times  \cdots  \times  {E}_{n} \) to \( F \) is continuous if and only if

\[
\exists M > 0,\forall x = \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {E}_{1} \times  \cdots  \times  {E}_{n},\;\parallel f\left( x\right) \parallel  \leq  M\begin{Vmatrix}{x}_{1}\end{Vmatrix}\cdots \begin{Vmatrix}{x}_{n}\end{Vmatrix}.
\]

DÉFINITION 1. L’ensemble des applications linéaires continues de \( E \) dans \( F \) est noté \( {\mathcal{L}}_{c}\left( {E, F}\right) \) . On norme \( {\mathcal{L}}_{c}\left( {E, F}\right) \) en posant

> DEFINITION 1. The set of continuous linear maps from \( E \) to \( F \) is denoted by \( {\mathcal{L}}_{c}\left( {E, F}\right) \) . We define a norm on \( {\mathcal{L}}_{c}\left( {E, F}\right) \) by setting

\[
\forall f \in  {\mathcal{L}}_{c}\left( {E, F}\right) ,\;\parallel f\parallel  = \mathop{\sup }\limits_{{\parallel x\parallel  = 1}}\parallel f\left( x\right) \parallel  = \mathop{\sup }\limits_{{\parallel x\parallel  \leq  1}}\parallel f\left( x\right) \parallel ,
\]

ce qui fait de \( {\mathcal{L}}_{c}\left( {E, F}\right) \) un e.v normé.

> which makes \( {\mathcal{L}}_{c}\left( {E, F}\right) \) a normed vector space.

Remarque 2. Le réel \( \parallel f\parallel \) est le plus petit réel positif \( M \) tel que \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) pour tout \( x \in E \) . En particulier, pour tout \( x \in E,\parallel f\left( x\right) \parallel \leq \parallel f\parallel \cdot \parallel x\parallel \) . Sauf mention contraire, c’est la norme \( x \mapsto \parallel f\parallel \) qui est choisie sur \( {\mathcal{L}}_{c}\left( {E, F}\right) \) .

> Remark 2. The real number \( \parallel f\parallel \) is the smallest positive real number \( M \) such that \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) for all \( x \in E \) . In particular, for all \( x \in E,\parallel f\left( x\right) \parallel \leq \parallel f\parallel \cdot \parallel x\parallel \) . Unless otherwise stated, the norm \( x \mapsto \parallel f\parallel \) is the one chosen on \( {\mathcal{L}}_{c}\left( {E, F}\right) \) .

Proposition 1. Soient \( E, F \) et \( G \) trois e.v.n, soient \( f \in {\mathcal{L}}_{c}\left( {E, F}\right) \) et \( g \in {\mathcal{L}}_{c}\left( {F, G}\right) \) . Alors \( g \circ f \in {\mathcal{L}}_{c}\left( {E, G}\right) \) et \( \parallel g \circ f\parallel \leq \parallel g\parallel \cdot \parallel f\parallel . \)

> Proposition 1. Let \( E, F \) and \( G \) be three normed vector spaces, let \( f \in {\mathcal{L}}_{c}\left( {E, F}\right) \) and \( g \in {\mathcal{L}}_{c}\left( {F, G}\right) \) . Then \( g \circ f \in {\mathcal{L}}_{c}\left( {E, G}\right) \) and \( \parallel g \circ f\parallel \leq \parallel g\parallel \cdot \parallel f\parallel . \)

En particulier, la norme \( \parallel .\parallel \) sur \( {\mathcal{L}}_{c}\left( E\right) = {\mathcal{L}}_{c}\left( {E, E}\right) \) en fait une algèbre normée (voir plus bas).

> In particular, the norm \( \parallel .\parallel \) on \( {\mathcal{L}}_{c}\left( E\right) = {\mathcal{L}}_{c}\left( {E, E}\right) \) makes it a normed algebra (see below).

- THÉORÉME 2. Si \( F \) est un espace de Banach, l’e.v.n \( {\mathcal{L}}_{c}\left( {E, F}\right) \) est un espace de Banach. Démonstration. Soit \( \left( {f}_{n}\right) \) une suite de Cauchy de \( {\mathcal{L}}_{c}\left( {E, F}\right) \) .

> - THEOREM 2. If \( F \) is a Banach space, the normed vector space \( {\mathcal{L}}_{c}\left( {E, F}\right) \) is a Banach space. Proof. Let \( \left( {f}_{n}\right) \) be a Cauchy sequence in \( {\mathcal{L}}_{c}\left( {E, F}\right) \) .

On construit la limite éventuelle de \( \left( {f}_{n}\right) \) . Fixons un élément quelconque \( x \) de \( E \) . On a

> We construct the potential limit of \( \left( {f}_{n}\right) \) . Let us fix an arbitrary element \( x \) of \( E \) . We have

\[
\forall \left( {p, q}\right)  \in  {\mathbb{N}}^{2},\;\begin{Vmatrix}{{f}_{p}\left( x\right)  - {f}_{q}\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \cdot  \parallel x\parallel ,
\]

donc la suite \( \left( {{f}_{n}\left( x\right) }\right) \) est de Cauchy dans \( F \) , et comme \( F \) est complet, elle converge. On note \( f\left( x\right) \) sa limite. On définit ainsi une application \( f \) de \( E \) dans \( F \) .

> therefore the sequence \( \left( {{f}_{n}\left( x\right) }\right) \) is Cauchy in \( F \) , and since \( F \) is complete, it converges. We denote its limit by \( f\left( x\right) \) . We thus define a map \( f \) from \( E \) to \( F \) .

On vérifie que \( f \in {\mathcal{L}}_{c}\left( {E, F}\right) \) . L’application \( f \) est linéaire car si \( x, y \in E \) et \( \lambda ,\mu \in \mathbb{K} \) ,

> We verify that \( f \in {\mathcal{L}}_{c}\left( {E, F}\right) \) . The map \( f \) is linear because if \( x, y \in E \) and \( \lambda ,\mu \in \mathbb{K} \) ,

\[
f\left( {{\lambda x} + {\mu y}}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{f}_{n}\left( {{\lambda x} + {\mu y}}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left\lbrack  {\lambda {f}_{n}\left( x\right)  + \mu {f}_{n}\left( y\right) }\right\rbrack   = {\lambda f}\left( x\right)  + {\mu f}\left( y\right) .
\]

Elle est continue. En effet, \( \left( {f}_{n}\right) \) étant de Cauchy, elle est bornée donc il existe \( M > 0 \) tel que \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) pour tout \( n \) . Si \( x \in E \) est fixé, on a donc \( \begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq M\parallel x\parallel \) pour tout \( n \) , donc à la limite lorsque \( n \rightarrow \infty \) , on obtient \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) . Ainsi, \( f \) est bien continue.

> It is continuous. Indeed, since \( \left( {f}_{n}\right) \) is Cauchy, it is bounded, so there exists \( M > 0 \) such that \( \begin{Vmatrix}{f}_{n}\end{Vmatrix} \leq M \) for all \( n \) . If \( x \in E \) is fixed, we therefore have \( \begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq M\parallel x\parallel \) for all \( n \) , so in the limit as \( n \rightarrow \infty \) , we obtain \( \parallel f\left( x\right) \parallel \leq M\parallel x\parallel \) . Thus, \( f \) is indeed continuous.

Il nous reste à prouver que \( \left( {f}_{n}\right) \) converge vers \( f \) au sens de la norme \( \parallel \) . Most \( \varepsilon > 0 \) . Il existe \( N \in \mathbb{N} \) tel que pour tout \( p, q \geq N,\begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \leq \varepsilon \) . En fixant \( x \in E \) , on a donc

> It remains for us to prove that \( \left( {f}_{n}\right) \) converges to \( f \) in the sense of the norm \( \parallel \) . Most \( \varepsilon > 0 \) . There exists \( N \in \mathbb{N} \) such that for all \( p, q \geq N,\begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \leq \varepsilon \) . By fixing \( x \in E \) , we therefore have

\[
\forall p, q \geq  N,\;\begin{Vmatrix}{{f}_{p}\left( x\right)  - {f}_{q}\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{f}_{p} - {f}_{q}}\end{Vmatrix} \cdot  \parallel x\parallel  \leq  \varepsilon \parallel x\parallel .
\]

En fixant \( p \geq N \) et en faisant tendre \( q \) vers l’infini, on obtient \( \begin{Vmatrix}{{f}_{p}\left( x\right) - f\left( x\right) }\end{Vmatrix} \leq \varepsilon \parallel x\parallel \) . Ceci est vrai pour tout \( x \in E \) , on a donc \( \begin{Vmatrix}{{f}_{p} - f}\end{Vmatrix} \leq \varepsilon \) , et ceci pour tout \( p \geq N \) , d’où le résultat.

> By fixing \( p \geq N \) and letting \( q \) tend to infinity, we obtain \( \begin{Vmatrix}{{f}_{p}\left( x\right) - f\left( x\right) }\end{Vmatrix} \leq \varepsilon \parallel x\parallel \) . This is true for all \( x \in E \) , so we have \( \begin{Vmatrix}{{f}_{p} - f}\end{Vmatrix} \leq \varepsilon \) , and this for all \( p \geq N \) , hence the result.

Remarque 3. Il faut savoir refaire cette démonstration. Retenez en particulier les trois étapes principales (faites l'exercice 1 page 21 qui est du même type).

> Remark 3. You must know how to reproduce this proof. Remember in particular the three main steps (do exercise 1 on page 21 which is of the same type).

Formes linéaires continues. Si \( E \) est un \( \mathbb{K} \) -e.v.n (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ), l’e.v.n \( {\mathcal{L}}_{c}\left( {E,\mathbb{K}}\right) \) (ensemble des formes linéaires continues sur \( E \) ) est un s.e.v du dual \( {E}^{ * } \) de \( E \) . On le note souvent \( {E}^{\prime } \) et on l’appelle dual topologique de \( E \) . Comme \( \mathbb{K} \) est complet, \( {E}^{\prime } \) est un espace de Banach d’après le théorème 2. Dans un espace de Hilbert, \( {E}^{\prime } \) et \( E \) sont isomorphes (voir l'annexe B, question 3/ a) du problème 1 page 427).

> Continuous linear forms. If \( E \) is a \( \mathbb{K} \) -n.v.s. (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) ), the n.v.s. \( {\mathcal{L}}_{c}\left( {E,\mathbb{K}}\right) \) (set of continuous linear forms on \( E \) ) is a subspace of the dual \( {E}^{ * } \) of \( E \) . It is often denoted \( {E}^{\prime } \) and is called the topological dual of \( E \) . Since \( \mathbb{K} \) is complete, \( {E}^{\prime } \) is a Banach space according to theorem 2. In a Hilbert space, \( {E}^{\prime } \) and \( E \) are isomorphic (see appendix B, question 3/ a) of problem 1 on page 427).

Une forme linéaire \( f \) sur \( E \) est continue si et seulement si son noyau Ker \( f \) est un fermé de \( E \) (voir l’exercice 7 page 55).

> A linear form \( f \) on \( E \) is continuous if and only if its kernel Ker \( f \) is a closed subset of \( E \) (see exercise 7 on page 55).

L’algèbre normée \( {\mathcal{L}}_{c}\left( E\right) \) . On rappelle qu’une algèbre normée \( A \) est une algèbre (i. e. un e.v muni d'une loi de produit interne, distributive par rapport à l'addition, vérifiant \( \left( {\lambda u}\right) v = \lambda \left( {uv}\right) = u\left( {\lambda v}\right) \) pour tout \( u, v \in A \) et \( \lambda \in \mathbb{K}) \) munie d’une norme \( \parallel .\parallel \) vérifiant \( \parallel {uv}\parallel \leq \parallel u\parallel \cdot \parallel v\parallel \) pour tout \( u, v \in A \) . Ceci assure la continuité de l’application \( \left( {u, v}\right) \mapsto {uv} \) .

> The normed algebra \( {\mathcal{L}}_{c}\left( E\right) \) . Recall that a normed algebra \( A \) is an algebra (i.e., a v.s. equipped with an internal product law, distributive with respect to addition, satisfying \( \left( {\lambda u}\right) v = \lambda \left( {uv}\right) = u\left( {\lambda v}\right) \) for all \( u, v \in A \) and \( \lambda \in \mathbb{K}) \) ) equipped with a norm \( \parallel .\parallel \) satisfying \( \parallel {uv}\parallel \leq \parallel u\parallel \cdot \parallel v\parallel \) for all \( u, v \in A \) . This ensures the continuity of the map \( \left( {u, v}\right) \mapsto {uv} \) .

D’après la proposition 1, l’algèbre \( {\mathcal{L}}_{c}\left( E\right) = {\mathcal{L}}_{c}\left( {E, E}\right) \) , munie de la norme \( \parallel .\parallel \) , est une algèbre normée. Si de plus \( E \) est un espace de Banach, \( {\mathcal{L}}_{c}\left( E\right) \) est un espace de Banach d’après le théorème 2. Une conséquence importante est la suivante. Toute série \( \sum {u}_{n} \) de \( {\mathcal{L}}_{c}\left( E\right) \) absolument convergente (i. e. telle que \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converge) est convergente (en effet, la suite associée est de Cauchy).

> According to proposition 1, the algebra \( {\mathcal{L}}_{c}\left( E\right) = {\mathcal{L}}_{c}\left( {E, E}\right) \), equipped with the norm \( \parallel .\parallel \), is a normed algebra. If, in addition, \( E \) is a Banach space, \( {\mathcal{L}}_{c}\left( E\right) \) is a Banach space according to theorem 2. An important consequence is the following. Any series \( \sum {u}_{n} \) of \( {\mathcal{L}}_{c}\left( E\right) \) that is absolutely convergent (i.e., such that \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converges) is convergent (indeed, the associated sequence is Cauchy).

##### An important application.

*Français : Une application importante.*

Proposition 2. Soient \( E \) un espace de Banach et \( u \in {\mathcal{L}}_{c}\left( E\right) \) tel que \( \parallel u\parallel < 1 \) . Alors Id \( - u \) est inversible, son inverse est \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n} \in {\mathcal{L}}_{c}\left( E\right) \) .

> Proposition 2. Let \( E \) be a Banach space and \( u \in {\mathcal{L}}_{c}\left( E\right) \) such that \( \parallel u\parallel < 1 \). Then Id \( - u \) is invertible, its inverse is \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n} \in {\mathcal{L}}_{c}\left( E\right) \).

Démonstration. La série \( \sum {u}^{n} \) converge absolument car \( \begin{Vmatrix}{u}^{n}\end{Vmatrix} \leq \parallel u{\parallel }^{n} \) et \( \parallel u\parallel < 1 \) . Or

> Proof. The series \( \sum {u}^{n} \) converges absolutely because \( \begin{Vmatrix}{u}^{n}\end{Vmatrix} \leq \parallel u{\parallel }^{n} \) and \( \parallel u\parallel < 1 \). Now

\[
\left( {\operatorname{Id} - u}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{u}^{n} = \operatorname{Id}
\]

de même \( \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n}}\right) \left( {\operatorname{Id} - u}\right) = \operatorname{Id} \) , d’où le résultat.

> similarly \( \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}^{n}}\right) \left( {\operatorname{Id} - u}\right) = \operatorname{Id} \), hence the result.

Remarque 4. - On note \( \mathcal{G}{\ell }_{c}\left( E\right) \) l’ensemble des endomorphismes inversibles \( u \) continus et tels que \( {u}^{-1} \) est continu (en fait, si \( E \) est un espace de Banach et si \( u \) est inversible et continu, \( {u}^{-1} \) est toujours continu - c'est le théorème de Banach, voir l’annexe A, exercice 6 page 423). Si \( E \) est un espace de Banach, la proposition précédente permet de montrer que \( \mathcal{G}{\ell }_{c}\left( E\right) \) est un ouvert de \( {\mathcal{L}}_{c}\left( E\right) \) (voir l’exercice 4 page 52).

> Remark 4. - We denote by \( \mathcal{G}{\ell }_{c}\left( E\right) \) the set of invertible continuous endomorphisms \( u \) such that \( {u}^{-1} \) is continuous (in fact, if \( E \) is a Banach space and if \( u \) is invertible and continuous, \( {u}^{-1} \) is always continuous - this is the Banach theorem, see appendix A, exercise 6 page 423). If \( E \) is a Banach space, the previous proposition allows us to show that \( \mathcal{G}{\ell }_{c}\left( E\right) \) is an open subset of \( {\mathcal{L}}_{c}\left( E\right) \) (see exercise 4 page 52).

- De manière générale, pour toute série entière \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) (avec \( {a}_{n} \in  \mathbb{R} \) ou \( {a}_{n} \in  \mathbb{C} \) ) de rayon de convergence \( R > 0 \) , on peut définir la série entière d’endomorphisme \( \mathop{\sum }\limits_{n}{a}_{n}{u}^{n} \) dès que \( \parallel u\parallel  < R \) pour \( u \in  {\mathcal{L}}_{c}\left( E\right) \) avec \( E \) un espace de Banach. Par exemple, l’exponentielle d’un endomorphisme continu \( u \in  {\mathcal{L}}_{c}\left( E\right) \) , est défini par la série \( \exp \left( u\right)  = \mathop{\sum }\limits_{{n = 0}}^{\infty }{u}^{n}/n \) ! (voir le tome Algèbre, partie 4.3). On peut aussi utiliser les séries entières d'endomorphisme pour démontrer des résultats intéressant. Par exemple, on prouve l’existence, dès que \( \parallel u\parallel  < 1 \) , d’un endomorphisme continu \( v \in  {\mathcal{L}}_{c}\left( E\right) \) tel que \( {v}^{2} = 1 + u \) ; il suffit de choisir \( v = \mathop{\sum }\limits_{n}{a}_{n}{u}^{n} \) où les \( \left( {a}_{n}\right) \) sont les coefficients de la série entière \( \sqrt{1 + z} = \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) .

> - In general, for any power series \( \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) (with \( {a}_{n} \in  \mathbb{R} \) or \( {a}_{n} \in  \mathbb{C} \) ) with radius of convergence \( R > 0 \) , one can define the power series of an endomorphism \( \mathop{\sum }\limits_{n}{a}_{n}{u}^{n} \) as soon as \( \parallel u\parallel  < R \) for \( u \in  {\mathcal{L}}_{c}\left( E\right) \) with \( E \) a Banach space. For example, the exponential of a continuous endomorphism \( u \in  {\mathcal{L}}_{c}\left( E\right) \) is defined by the series \( \exp \left( u\right)  = \mathop{\sum }\limits_{{n = 0}}^{\infty }{u}^{n}/n \) ! (see the Algebra volume, part 4.3). One can also use power series of endomorphisms to prove interesting results. For example, we prove the existence, as soon as \( \parallel u\parallel  < 1 \) , of a continuous endomorphism \( v \in  {\mathcal{L}}_{c}\left( E\right) \) such that \( {v}^{2} = 1 + u \) ; it suffices to choose \( v = \mathop{\sum }\limits_{n}{a}_{n}{u}^{n} \) where the \( \left( {a}_{n}\right) \) are the coefficients of the power series \( \sqrt{1 + z} = \mathop{\sum }\limits_{n}{a}_{n}{z}^{n} \) .
