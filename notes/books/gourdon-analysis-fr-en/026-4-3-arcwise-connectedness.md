#### 4.3. Arcwise connectedness

*Français : 4.3. Connexité par arcs*

DéFINITION 2. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. On appelle chemin de \( E \) toute application \( \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow \left( {E,\mathrm{\;d}}\right) \) , continue. L’image \( \gamma \left( \left\lbrack {0,1}\right\rbrack \right) \) du chemin s’appelle un arc, \( \gamma \left( 0\right) \) l’origine de l’arc, \( \gamma \left( 1\right) \) son extrémité.

> DEFINITION 2. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. A path in \( E \) is any continuous map \( \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow \left( {E,\mathrm{\;d}}\right) \). The image \( \gamma \left( \left\lbrack {0,1}\right\rbrack \right) \) of the path is called an arc, \( \gamma \left( 0\right) \) is the origin of the arc, and \( \gamma \left( 1\right) \) is its endpoint.

DéFINITION 3. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. On dit que \( E \) est connexe par arcs si pour tout \( \left( {a, b}\right) \in {E}^{2} \) , il existe un arc inclus dans \( E \) d’origine \( a \) et d’extrémité \( b \) .

> DEFINITION 3. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. We say that \( E \) is arcwise connected if for any \( \left( {a, b}\right) \in {E}^{2} \), there exists an arc included in \( E \) with origin \( a \) and endpoint \( b \).

\( \rightarrow \) THÉORÉME 4. Un espace connexe par arcs est connexe.

> \( \rightarrow \) THEOREM 4. An arcwise connected space is connected.

Démonstration. Soient \( E \) un espace connexe par arcs et \( f : E \rightarrow D = \{ 0,1\} \) une application continue. Soit \( \left( {a, b}\right) \in {E}^{2} \) . Il existe une application continue \( \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow E \) telle que \( \gamma \left( 0\right) = a \) et \( \gamma \left( 1\right) = b \) . L’application \( f \circ \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow D \) est continue, donc constante car \( \left\lbrack {0,1}\right\rbrack \) est connexe. Donc \( \left( {f \circ \gamma }\right) \left( 0\right) = \left( {f \circ \gamma }\right) \left( 1\right) \) , c’est-à-dire \( f\left( a\right) = f\left( b\right) \) . L’application \( f \) est donc constante, donc \( E \) est connexe d’après la proposition 3

> Proof. Let \( E \) be an arcwise connected space and \( f : E \rightarrow D = \{ 0,1\} \) a continuous map. Let \( \left( {a, b}\right) \in {E}^{2} \). There exists a continuous map \( \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow E \) such that \( \gamma \left( 0\right) = a \) and \( \gamma \left( 1\right) = b \). The map \( f \circ \gamma : \left\lbrack {0,1}\right\rbrack \rightarrow D \) is continuous, hence constant because \( \left\lbrack {0,1}\right\rbrack \) is connected. Thus \( \left( {f \circ \gamma }\right) \left( 0\right) = \left( {f \circ \gamma }\right) \left( 1\right) \), that is to say \( f\left( a\right) = f\left( b\right) \). The map \( f \) is therefore constant, so \( E \) is connected according to proposition 3.

Remarque 4. - La connexité par arcs est surtout une notion pratique pour montrer qu'un espace est connexe. En termes intuitifs, un espace est connexe par arcs si on peut toujours relier deux de ses points par une courbe continue, ce qui fait du concept de connexité par arcs une notion moins abstraite que la notion de connexité.

> Remark 4. - Arcwise connectedness is primarily a practical notion for showing that a space is connected. Intuitively, a space is arcwise connected if one can always connect any two of its points with a continuous curve, which makes the concept of arcwise connectedness less abstract than the notion of connectedness.

- La réciproque du théorème 4 est fausse (voir l'exercice 5 page 44). Elle est cependant vraie dans un ouvert d'un \( \mathbb{R} \) -e.v.n (voir le théorème 5).

> - The converse of theorem 4 is false (see exercise 5 on page 44). It is, however, true in an open set of a \( \mathbb{R} \) -n.v.s. (see theorem 5).

- La connexité par arcs est, comme la connexité, une notion topologique.

> - Arcwise connectedness is, like connectedness, a topological notion.

Connexité par lignes brisées dans un espace vectoriel normé. Dans tout ce paragraphe, \( E \) désigne un \( \mathbb{R} \) -espace vectoriel normé.

> Connectedness by polygonal paths in a normed vector space. Throughout this section, \( E \) denotes a \( \mathbb{R} \) -normed vector space.

DéFINITION 4. Soient \( \left( {a, b}\right) \in {E}^{2} \) . On appelle segment d’extrémité \( a \) et \( b \) l’ensemble \( \left\{ {{\lambda a} + \left( {1 - \lambda }\right) b,\lambda \in \left\lbrack {0,1}\right\rbrack }\right\} \) , et on le note \( \left\lbrack {a, b}\right\rbrack \) .

> DEFINITION 4. Let \( \left( {a, b}\right) \in {E}^{2} \) . The segment with endpoints \( a \) and \( b \) is the set \( \left\{ {{\lambda a} + \left( {1 - \lambda }\right) b,\lambda \in \left\lbrack {0,1}\right\rbrack }\right\} \) , and it is denoted by \( \left\lbrack {a, b}\right\rbrack \) .

DÉFINITION 5. On appelle ligne brisée (ou ligne polygonale) de \( E \) joignant deux points a et \( b \) de \( E \) tout ensemble de la forme \( { \cup }_{1 \leq i \leq n}\left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) où \( n \in {\mathbb{N}}^{ * },{x}_{0} = a \) et \( {x}_{n} = b \) et pour tout \( i,{x}_{i} \in E \) .

> DEFINITION 5. A polygonal path (or broken line) of \( E \) joining two points a and \( b \) in \( E \) is any set of the form \( { \cup }_{1 \leq i \leq n}\left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) where \( n \in {\mathbb{N}}^{ * },{x}_{0} = a \) and \( {x}_{n} = b \) and for all \( i,{x}_{i} \in E \) .

DÉFINITION 6. Une partie \( A \) de \( E \) est dite connexe par lignes brisées si pour tout \( \left( {a, b}\right) \in \; {A}^{2} \) , il existe une ligne brisée incluse dans \( A \) joignant \( a \) et \( b \) .

> DEFINITION 6. A subset \( A \) of \( E \) is said to be connected by polygonal paths if for any \( \left( {a, b}\right) \in \; {A}^{2} \) , there exists a polygonal path included in \( A \) joining \( a \) and \( b \) .

Remarque 5. Il est clair qu'une ligne brisée est un arc. Une partie de \( E \) connexe par lignes brisées est donc connexe par arcs.

> Remark 5. It is clear that a polygonal path is an arc. A subset of \( E \) connected by polygonal paths is therefore arcwise connected.

Exemple 2. Un R-e.v.n \( E \) est connexe par lignes brisées (donc connexe par arcs et connexe) car pour tout \( \left( {a, b}\right) \in {E}^{2},\left\lbrack {a, b}\right\rbrack \subset E \) .

> Example 2. An R-n.v.s. \( E \) is connected by polygonal paths (and therefore arcwise connected and connected) because for any \( \left( {a, b}\right) \in {E}^{2},\left\lbrack {a, b}\right\rbrack \subset E \) .

THÉORÉME 5. Soit \( E \) un \( \mathbb{R} \) -e.v.n. Une partie ouverte \( \Omega \) de \( E \) est connexe si et seulement si elle est connexe par lignes brisées.

> THEOREM 5. Let \( E \) be a \( \mathbb{R} \) -n.v.s. An open subset \( \Omega \) of \( E \) is connected if and only if it is connected by polygonal paths.

Démonstration. La condition suffisante découle du théorème 4, une partie connexe par ligne brisée étant connexe par arcs.

> Proof. The sufficient condition follows from theorem 4, as a set connected by polygonal paths is arcwise connected.

Montrons la condition nécessaire. Soit \( \Omega \) un ouvert connexe non vide de \( E \) . Soit \( {x}_{0} \in \Omega \) et notons \( {T}_{{x}_{0}} \) l’ensemble des points de \( \Omega \) que l’on peut joindre à \( {x}_{0} \) par une ligne brisée contenue dans \( \Omega \) .

> Let us show the necessary condition. Let \( \Omega \) be a non-empty connected open set of \( E \) . Let \( {x}_{0} \in \Omega \) and denote by \( {T}_{{x}_{0}} \) the set of points in \( \Omega \) that can be joined to \( {x}_{0} \) by a polygonal path contained in \( \Omega \) .

- On a \( {T}_{{x}_{0}} \neq  \varnothing \) car \( {x}_{0} \in  {T}_{{x}_{0}} \) .

> - We have \( {T}_{{x}_{0}} \neq  \varnothing \) because \( {x}_{0} \in  {T}_{{x}_{0}} \) .

- L’ensemble \( {T}_{{x}_{0}} \) est ouvert. En effet, si \( x \in  {T}_{{x}_{0}} \) , on a \( x \in  \Omega \) donc il existe \( \rho  > 0 \) tel que la boule \( \mathrm{B}\left( {x,\rho }\right) \) soit incluse dans \( \Omega \) . Ainsi, pour tout \( y \in  \mathrm{B}\left( {x,\rho }\right) ,\left\lbrack  {x, y}\right\rbrack   \subset  \Omega \) et comme \( x \in  {T}_{{x}_{0}} \) , on en déduit \( y \in  {T}_{{x}_{0}} \) .

> - The set \( {T}_{{x}_{0}} \) is open. Indeed, if \( x \in  {T}_{{x}_{0}} \) , we have \( x \in  \Omega \) , so there exists \( \rho  > 0 \) such that the ball \( \mathrm{B}\left( {x,\rho }\right) \) is included in \( \Omega \) . Thus, for any \( y \in  \mathrm{B}\left( {x,\rho }\right) ,\left\lbrack  {x, y}\right\rbrack   \subset  \Omega \) and since \( x \in  {T}_{{x}_{0}} \) , we deduce \( y \in  {T}_{{x}_{0}} \) .

- L’ensemble \( {T}_{{x}_{0}} \) est fermé dans \( \Omega \) . En effet, si \( x \in  \overline{{T}_{{x}_{0}}} \cap  \Omega \) , il existe une boule \( \mathrm{B}\left( {x,\rho }\right) \) incluse dans \( \Omega \) telle que \( \mathrm{B}\left( {x,\rho }\right)  \cap  {T}_{{x}_{0}} \neq  \varnothing \) . Si on choisit \( y \in  \mathrm{B}\left( {x,\rho }\right)  \cap  {T}_{{x}_{0}} \) , on a alors \( \left\lbrack  {y, x}\right\rbrack   \subset  \Omega \) , donc \( x \in  {T}_{{x}_{0}} \) .

> - The set \( {T}_{{x}_{0}} \) is closed in \( \Omega \) . Indeed, if \( x \in  \overline{{T}_{{x}_{0}}} \cap  \Omega \) , there exists a ball \( \mathrm{B}\left( {x,\rho }\right) \) included in \( \Omega \) such that \( \mathrm{B}\left( {x,\rho }\right)  \cap  {T}_{{x}_{0}} \neq  \varnothing \) . If we choose \( y \in  \mathrm{B}\left( {x,\rho }\right)  \cap  {T}_{{x}_{0}} \) , we then have \( \left\lbrack  {y, x}\right\rbrack   \subset  \Omega \) , therefore \( x \in  {T}_{{x}_{0}} \) .

Finalement, \( {T}_{{x}_{0}} \neq \varnothing \) est ouvert et fermé dans le connexe \( \Omega \) , donc \( {T}_{{x}_{0}} = \Omega \) , d’où le résultat.

> Finally, \( {T}_{{x}_{0}} \neq \varnothing \) is open and closed in the connected space \( \Omega \) , therefore \( {T}_{{x}_{0}} = \Omega \) , hence the result.

Remarque 6. On en déduit avec la remarque 5 que tout ouvert connexe d'un e.v.n est connexe par arcs. Attention, ce dernier résultat n’est plus vrai si on remplace \( E \) par un espace métrique quelconque.

> Remark 6. We deduce from Remark 5 that every connected open set of a n.v.s. is path-connected. Note that this last result is no longer true if we replace \( E \) with an arbitrary metric space.
