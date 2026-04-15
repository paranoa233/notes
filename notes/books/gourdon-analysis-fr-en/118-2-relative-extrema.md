### 2. Relative extrema

*Français : 2. Extremums relatifs*

Dans toute cette section, \( U \) désigne un ouvert de \( {\mathbb{R}}^{n} \) .

> Throughout this section, \( U \) denotes an open set of \( {\mathbb{R}}^{n} \) .

Proposition 1. Si \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) admet un extremum relatif en un point a de \( U \) et si \( f \) est différentiable en a, alors \( d{f}_{a} = 0 \) (en d’autres termes, \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) = 0 \) pour tout \( i \) ).

> Proposition 1. If \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) has a relative extremum at a point a of \( U \) and if \( f \) is differentiable at a, then \( d{f}_{a} = 0 \) (in other words, \( \frac{\partial f}{\partial {x}_{i}}\left( a\right) = 0 \) for all \( i \) ).

Un point \( a \) pour lequel \( d{f}_{a} = 0 \) est appelé point critique de \( f \) . Ce résultat nous dit qu'un extremum relatif est nécessairement un point critique (notez que \( U \) doit être ouvert : c'est comme dans \( \mathbb{R} \) , un extremum relatif est un point critique lorsque c'est un point intérieur à l'ensemble de définition). La réciproque est fausse dans le cas général. Cependant, moyennant un développement limité de \( f \) à l’ordre 2, il est possible d’obtenir une condition suffisante d'existence d'un extremum.

> A point \( a \) for which \( d{f}_{a} = 0 \) is called a critical point of \( f \) . This result tells us that a relative extremum is necessarily a critical point (note that \( U \) must be open: it is like in \( \mathbb{R} \) , a relative extremum is a critical point when it is an interior point of the domain). The converse is false in the general case. However, by means of a Taylor expansion of \( f \) to order 2, it is possible to obtain a sufficient condition for the existence of an extremum.

\( \rightarrow \) THÉORÉME 1. Soit \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{2} \) et supposons qu’il existe \( a \in U \) tel que \( d{f}_{a} = 0 \) , de sorte que d’après la formule de Taylor-Young, \( f\left( {a + h}\right) = \; f\left( a\right) + Q\left( h\right) /2 + o\left( {\parallel h{\parallel }^{2}}\right) , \) où \( Q \) est la forme quadratique

> \( \rightarrow \) THEOREM 1. Let \( f : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{2} \) and assume there exists \( a \in U \) such that \( d{f}_{a} = 0 \) , so that according to the Taylor-Young formula, \( f\left( {a + h}\right) = \; f\left( a\right) + Q\left( h\right) /2 + o\left( {\parallel h{\parallel }^{2}}\right) , \) where \( Q \) is the quadratic form

\[
Q\left( h\right)  = {\left\lbrack  \mathop{\sum }\limits_{{i = 1}}^{n}{h}_{i}\frac{\partial f}{\partial {x}_{i}}\left( a\right) \right\rbrack  }^{\left\lbrack  2\right\rbrack  } = \mathop{\sum }\limits_{i}{h}_{i}^{2}\frac{{\partial }^{2}f}{\partial {x}_{i}^{2}}\left( a\right)  + 2\mathop{\sum }\limits_{{i < j}}{h}_{i}{h}_{j}\frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( a\right) .
\]

Alors

> Then

(i) si \( f \) admet un minimum (resp. un maximum) relatif en a, \( Q \) est une forme qua-dratique positive (resp. négative) ;

> (i) if \( f \) has a relative minimum (resp. maximum) at a, \( Q \) is a positive (resp. negative) quadratic form;

(ii) si Q est une forme quadratique définie positive (resp. définie négative), f admet un minimum (resp. un maximum) relatif en a.

> (ii) if Q is a positive definite (resp. negative definite) quadratic form, f has a relative minimum (resp. maximum) at a.

Démonstration. Si \( f \) admet un minimum relatif en \( a \) , on a, sur un voisinage de 0 pour \( h \) ,

> Proof. If \( f \) has a relative minimum at \( a \) , we have, on a neighborhood of 0 for \( h \) ,

\[
f\left( {a + h}\right)  = f\left( a\right)  + \frac{1}{2}Q\left( h\right)  + o\left( {\parallel h{\parallel }^{2}}\right)  \geq  f\left( a\right) \;\text{ donc }\;Q\left( h\right)  + o\left( {\parallel h{\parallel }^{2}}\right)  \geq  0.
\]

Fixons \( h \in {\mathbb{R}}^{n} \) . Lorsque \( t \in \mathbb{R} \) tend vers 0, on peut donc écrire

> Let us fix \( h \in {\mathbb{R}}^{n} \) . As \( t \in \mathbb{R} \) tends to 0, we can therefore write

\[
Q\left( {th}\right)  + o\left( {\parallel {th}{\parallel }^{2}}\right)  = {t}^{2}\left( {Q\left( h\right)  + o\left( 1\right) }\right)  \geq  0\;\text{ donc }\;Q\left( h\right)  + o\left( 1\right)  \geq  0
\]

En faisant tendre \( t \) vers 0, on en déduit \( Q\left( h\right) \geq 0 \) . Ceci est vrai pour tout \( h \in {\mathbb{R}}^{n} \) , d’où (i).

> By letting \( t \) tend to 0, we deduce \( Q\left( h\right) \geq 0 \) . This is true for all \( h \in {\mathbb{R}}^{n} \) , hence (i).

Si \( Q \) est une forme quadratique définie positive, alors pour tout \( h \in {\mathbb{R}}^{n}, h \neq 0, Q\left( h\right) > 0 \) . Comme la sphère unité de \( {\mathbb{R}}^{n} \) est compacte, on en déduit \( \alpha = \mathop{\inf }\limits_{{\parallel h\parallel = 1}}Q\left( h\right) > 0 \) . Ainsi, lorsque \( h \) tend vers 0,

> If \( Q \) is a positive definite quadratic form, then for all \( h \in {\mathbb{R}}^{n}, h \neq 0, Q\left( h\right) > 0 \) . Since the unit sphere of \( {\mathbb{R}}^{n} \) is compact, we deduce \( \alpha = \mathop{\inf }\limits_{{\parallel h\parallel = 1}}Q\left( h\right) > 0 \) . Thus, when \( h \) tends to 0,

\[
f\left( {a + h}\right)  - f\left( a\right)  = \frac{1}{2}\left\lbrack  {Q\left( h\right)  + o\left( {\parallel h{\parallel }^{2}}\right) }\right\rbrack   = \frac{\parallel h{\parallel }^{2}}{2}\left\lbrack  {Q\left( \frac{h}{\parallel h\parallel }\right)  + o\left( 1\right) }\right\rbrack   \geq  \frac{\parallel h{\parallel }^{2}}{2}\left( {\alpha  + o\left( 1\right) }\right) .
\]

Comme \( \alpha + o\left( 1\right) \geq 0 \) sur un voisinage de \( h = 0 \) , on en déduit \( f\left( {a + h}\right) \geq f\left( a\right) \) sur ce voisinage, d'où (ii).

> Since \( \alpha + o\left( 1\right) \geq 0 \) on a neighborhood of \( h = 0 \) , we deduce \( f\left( {a + h}\right) \geq f\left( a\right) \) on this neighborhood, hence (ii).

Remarque 1. - Si la forme quadratique \( Q \) est seulement supposée positive (et non pas définie positive), on n'est pas assuré d'avoir un minimum relatif en \( a \) . Par exemple, pour la fonction \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {x}^{3} \) en \( a = 0, Q = 0 \) est positive (elle est nulle) et pourtant, \( f \) n’admet pas d’extremum en 0 .

> Remark 1. - If the quadratic form \( Q \) is only assumed to be positive (and not positive definite), we are not guaranteed to have a relative minimum at \( a \) . For example, for the function \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {x}^{3} \) at \( a = 0, Q = 0 \) is positive (it is zero) and yet, \( f \) does not admit an extremum at 0 .

- Dire que la forme quadratique \( Q \) est positive (resp. définie positive), c’est dire que la matrice symétrique \( A = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( a\right) \right) }_{i, j} \) est positive (resp. définie positive), ou encore que les valeurs propres de \( A \) sont \( \geq  0 \) (resp. \( > 0 \) ). La matrice \( A \) est appelée matrice hessienne de \( F \) au point critique \( a \) .

> - To say that the quadratic form \( Q \) is positive (resp. positive definite) is to say that the symmetric matrix \( A = {\left( \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\left( a\right) \right) }_{i, j} \) is positive (resp. positive definite), or also that the eigenvalues of \( A \) are \( \geq  0 \) (resp. \( > 0 \) ). The matrix \( A \) is called the Hessian matrix of \( F \) at the critical point \( a \) .

Exemple 1. (en dimension 2). Soit \( A = \left( \begin{array}{ll} r & s \\ s & t \end{array}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) et supposons \( \det A = {rt} - {s}^{2} > 0 \) . Alors les deux valeurs propres \( {\lambda }_{1} \) et \( {\lambda }_{2} \) de \( A \) (qui sont réelles car \( A \) est symétrique) ont même signe (car \( {\lambda }_{1}{\lambda }_{2} = \det A > 0 \) ). De plus, \( {\lambda }_{1} + {\lambda }_{2} = \operatorname{tr}A = r + t \) , et comme \( r \) et \( t \) ont même signe (car det \( A = {rt} - {s}^{2} > 0 \) donc \( {rt} > 0 \) ), on en déduit que \( {\lambda }_{1} + {\lambda }_{2} \) a le signe de \( r \) . Ainsi, les deux valeurs propres \( {\lambda }_{1} \) et \( {\lambda }_{2} \) ont le signe de \( r \) .

> Example 1. (in dimension 2). Let \( A = \left( \begin{array}{ll} r & s \\ s & t \end{array}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) and assume \( \det A = {rt} - {s}^{2} > 0 \) . Then the two eigenvalues \( {\lambda }_{1} \) and \( {\lambda }_{2} \) of \( A \) (which are real because \( A \) is symmetric) have the same sign (because \( {\lambda }_{1}{\lambda }_{2} = \det A > 0 \) ). Furthermore, \( {\lambda }_{1} + {\lambda }_{2} = \operatorname{tr}A = r + t \) , and since \( r \) and \( t \) have the same sign (because det \( A = {rt} - {s}^{2} > 0 \) therefore \( {rt} > 0 \) ), we deduce that \( {\lambda }_{1} + {\lambda }_{2} \) has the sign of \( r \) . Thus, the two eigenvalues \( {\lambda }_{1} \) and \( {\lambda }_{2} \) have the sign of \( r \) .

En résumé, si det \( A > 0 \) , alors \( A \) est définie positive (resp. définie négative) si et seulement si \( r > 0 \) (resp. \( r < 0 \) ). Si det \( A < 0 \) , on a \( {\lambda }_{1}{\lambda }_{2} < 0 \) donc \( A \) n’est ni positive, ni négative.

> In summary, if det \( A > 0 \) , then \( A \) is positive definite (resp. negative definite) if and only if \( r > 0 \) (resp. \( r < 0 \) ). If det \( A < 0 \) , we have \( {\lambda }_{1}{\lambda }_{2} < 0 \) therefore \( A \) is neither positive nor negative.

Maintenant, considérons une fonction \( f : U \subset {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{2} \) et telle que \( d{f}_{a} = 0 \) pour \( a \in U \) . Posons

> Now, let us consider a function \( f : U \subset {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{2} \) and such that \( d{f}_{a} = 0 \) for \( a \in U \) . Let us set

\[
r = \frac{{\partial }^{2}f}{\partial {x}^{2}}\left( a\right) ,\;s = \frac{{\partial }^{2}f}{\partial x\partial y}\left( a\right) ,\;t = \frac{{\partial }^{2}f}{\partial {y}^{2}}\left( a\right) .
\]

Alors d'après le théorème et ce que l'on vient de voir,

> Then, according to the theorem and what we have just seen,

- si \( {rt} - {s}^{2} > 0 \) et \( r > 0, f \) admet un minimum relatif en \( a \) ;

> - if \( {rt} - {s}^{2} > 0 \) and \( r > 0, f \) admits a relative minimum at \( a \) ;

- si \( {rt} - {s}^{2} > 0 \) et \( r < 0, f \) admet un maximum relatif en \( a \) ;

> - if \( {rt} - {s}^{2} > 0 \) and \( r < 0, f \) admits a relative maximum at \( a \) ;

- si \( {rt} - {s}^{2} < 0, f \) n’a pas un extremum en \( a \) ;

> - if \( {rt} - {s}^{2} < 0, f \) does not have an extremum at \( a \) ;

- si \( {rt} - {s}^{2} = 0 \) , on ne peut conclure.

> - if \( {rt} - {s}^{2} = 0 \) , we cannot conclude.

Extremums liés. On doit parfois maximiser (ou minimiser) une fonction \( f : U \subset {\mathbb{R}}^{n} \rightarrow \; \mathbb{R} \) sur un sous-ensemble de \( U \) de la forme \( \Gamma = \left\{ {x \in U \mid {g}_{1}\left( x\right) = \cdots = {g}_{r}\left( x\right) = 0}\right\} \) , où les \( {g}_{i} \) sont des fonctions de \( U \) dans \( \mathbb{R} \) . Pour ce faire, le théorème suivant, démontré à la page 347, rend de précieux services ; il est dû à Lagrange.

> Constrained extrema. One must sometimes maximize (or minimize) a function \( f : U \subset {\mathbb{R}}^{n} \rightarrow \; \mathbb{R} \) on a subset of \( U \) of the form \( \Gamma = \left\{ {x \in U \mid {g}_{1}\left( x\right) = \cdots = {g}_{r}\left( x\right) = 0}\right\} \) , where the \( {g}_{i} \) are functions from \( U \) to \( \mathbb{R} \) . To do this, the following theorem, proven on page 347, provides valuable assistance; it is due to Lagrange.

THÉORÉME 2. Soient \( f,{g}_{1},\ldots ,{g}_{r} : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) des fonctions de classe \( {\mathcal{C}}^{1} \) , où \( U \) est un ouvert de \( {\mathbb{R}}^{n} \) . On désigne par \( \Gamma \) l’ensemble \( \left\{ {x \in U \mid {g}_{1}\left( x\right) = \cdots = {g}_{r}\left( x\right) = 0}\right\} \) .

> THEOREM 2. Let \( f,{g}_{1},\ldots ,{g}_{r} : U \subset {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be functions of class \( {\mathcal{C}}^{1} \) , where \( U \) is an open set of \( {\mathbb{R}}^{n} \) . We denote by \( \Gamma \) the set \( \left\{ {x \in U \mid {g}_{1}\left( x\right) = \cdots = {g}_{r}\left( x\right) = 0}\right\} \) .

Si \( {f}_{\mid \Gamma } \) (restriction de \( f \) à \( \Gamma \) ) admet un extremum relatif en a \( \in \Gamma \) et si les formes linéaires \( d{g}_{1, a},\ldots , d{g}_{r, a} \) sont linéairement indépendantes, alors il existe des réels \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) (appelés multiplicateurs de Lagrange) tels que

> If \( {f}_{\mid \Gamma } \) (restriction of \( f \) to \( \Gamma \) ) admits a relative extremum at a \( \in \Gamma \) and if the linear forms \( d{g}_{1, a},\ldots , d{g}_{r, a} \) are linearly independent, then there exist real numbers \( {\lambda }_{1},\ldots ,{\lambda }_{r} \) (called Lagrange multipliers) such that

\[
d{f}_{a} = {\lambda }_{1}d{g}_{1, a} + \cdots  + {\lambda }_{r}d{g}_{r, a}.
\]

Remarque 2. - La famille \( \left( {d{g}_{i, a}}\right) \) étant libre, les multiplicateurs de Lagrange \( \left( {\lambda }_{i}\right) \) sont uniques.

> Remark 2. - The family \( \left( {d{g}_{i, a}}\right) \) being linearly independent, the Lagrange multipliers \( \left( {\lambda }_{i}\right) \) are unique.

- La condition " \( U \) ouvert" est essentielle dans le théorème des extremums liés.

> - The condition "\( U \) open" is essential in the theorem of constrained extrema.
