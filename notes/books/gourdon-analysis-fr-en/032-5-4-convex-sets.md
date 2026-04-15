#### 5.4. Convex sets

*Français : 5.4. Convexes*

Les parties convexes jouent un rôle important dans les e.v.n, en particulier dans les espaces de Hilbert (voir l’annexe B, problème 1). Dans toute cette sous-partie, \( E \) désigne un \( \mathbb{K} \) -e.v (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ).

> Convex sets play an important role in n.v.s., particularly in Hilbert spaces (see Appendix B, problem 1). Throughout this subsection, \( E \) denotes a \( \mathbb{K} \) -v.s. (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) ).

DéFINITION 2. Soient \( A, B \in E \) . On appelle segment d’extrémités \( A \) et \( B \) et on note \( \left\lbrack {A, B}\right\rbrack \) l’ensemble \( \{ {\lambda A} + \left( {1 - \lambda }\right) B,\lambda \in \left\lbrack {0,1}\right\rbrack \} \) . Dans un e.v.n, un segment est fermé.

> DEFINITION 2. Let \( A, B \in E \) . The segment with endpoints \( A \) and \( B \) , denoted by \( \left\lbrack {A, B}\right\rbrack \) , is the set \( \{ {\lambda A} + \left( {1 - \lambda }\right) B,\lambda \in \left\lbrack {0,1}\right\rbrack \} \) . In a n.v.s., a segment is closed.

DéFINITION 3. Soit \( C \) une partie de \( E \) . On dit que \( C \) est convexe si pour tout \( \left( {A, B}\right) \in {C}^{2} \) , \( \left\lbrack {A, B}\right\rbrack \subset C. \)

> DEFINITION 3. Let \( C \) be a subset of \( E \) . We say that \( C \) is convex if for all \( \left( {A, B}\right) \in {C}^{2} \) , \( \left\lbrack {A, B}\right\rbrack \subset C. \)

Remarque 6. - Un s.e.v est convexe.

> Remark 6. - A subspace is convex.

- Une partie convexe est connexe par lignes brisées donc connexe. La même remarque vaut pour les parties étoilées définies plus bas.

> - A convex set is path-connected by broken lines, and therefore connected. The same remark applies to star-shaped sets defined below.

- Plus généralement, un convexe peut être défini dans un espace affine.

> - More generally, a convex set can be defined in an affine space.

DÉFINITION 4. Une partie \( A \) de \( E \) est dite étoilée s’il existe \( P \in A \) tel que \( \left\lbrack {P, M}\right\rbrack \subset A \) pour tout \( M \in A \) (on dit alors que \( A \) est étoilée par rapport à \( P \) ). Un tel point \( P \) s’appelle un centre de \( A \) .

> DEFINITION 4. A subset \( A \) of \( E \) is said to be star-shaped if there exists \( P \in A \) such that \( \left\lbrack {P, M}\right\rbrack \subset A \) for all \( M \in A \) (we then say that \( A \) is star-shaped with respect to \( P \) ). Such a point \( P \) is called a center of \( A \) .

Enveloppe convexe.

> Convex hull.

DéFINITION 5. Soit \( A \) une partie de \( E \) . Il existe une plus petite partie convexe de \( E \) contenant \( A \) . On l’appelle enveloppe convexe de \( A \) et on la note Conv \( \left( A\right) \) . L’ensemble \( \operatorname{Conv}\left( A\right) \) est aussi l’ensemble des barycentres des points de \( A \) affectés de coefficients positifs, i. e. \( \operatorname{Conv}\left( A\right) \) est l’ensemble des \( x \) tels que

> DEFINITION 5. Let \( A \) be a subset of \( E \) . There exists a smallest convex subset of \( E \) containing \( A \) . It is called the convex hull of \( A \) and is denoted by Conv \( \left( A\right) \) . The set \( \operatorname{Conv}\left( A\right) \) is also the set of barycenters of points of \( A \) with positive coefficients, i.e., \( \operatorname{Conv}\left( A\right) \) is the set of \( x \) such that

\[
\exists {x}_{1},\ldots ,{x}_{n} \in  A,\exists {\lambda }_{1},\ldots ,{\lambda }_{n} \in  {\mathbb{R}}^{ + },\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i} = 1,\;x = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{x}_{i}.
\]
