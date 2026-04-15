#### 1.2. Topology of a metric space

*Français : 1.2. Topologie d'un espace métrique*

Sauf mention contraire, dans toute cette sous-partie, \( \left( {E,\mathrm{\;d}}\right) \) désigne un espace métrique.

> Unless otherwise stated, throughout this subsection, \( \left( {E,\mathrm{\;d}}\right) \) denotes a metric space.

Ouverts.

> Open sets.

DéFINITION 6. Une partie \( \Omega \) de \( E \) est dite ouverte (ou \( \Omega \) un ouvert) si \( \Omega = \varnothing \) ou si

> DEFINITION 6. A subset \( \Omega \) of \( E \) is said to be open (or \( \Omega \) an open set) if \( \Omega = \varnothing \) or if

\[
\forall x \in  \Omega ,\exists \rho  > 0\;\text{ tel que }\;\mathrm{B}\left( {x,\rho }\right)  \subset  \Omega .
\]

L’ensemble des parties ouvertes de \( E \) s’appelle topologie de \( E \) .

> The set of open subsets of \( E \) is called the topology of \( E \).

Exemple 3. Une boule ouverte est un ouvert. En particulier, dans \( \mathbb{R} \) (muni de la distance usuelle \( \mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| \) ), les intervalles ouverts \( \rbrack \alpha ,\beta \lbrack \) sont des ouverts.

> Example 3. An open ball is an open set. In particular, in \( \mathbb{R} \) (equipped with the usual distance \( \mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| \)), the open intervals \( \rbrack \alpha ,\beta \lbrack \) are open sets.

Proposition 2. (i) Les parties \( \varnothing \) et \( E \) sont des ouverts.

> Proposition 2. (i) The sets \( \varnothing \) and \( E \) are open sets.

(ii) Une réunion d'ouverts est un ouvert.

> (ii) A union of open sets is an open set.

(iii) Une intersection finie d'ouverts est un ouvert.

> (iii) A finite intersection of open sets is an open set.

Remarque 3. Attention, une intersection infinie d'ouverts peut ne pas être ouverte. Par exemple, dans \( \mathbb{R},{ \cap }_{n \in {\mathbb{N}}^{ * }}\rbrack - 1/n,1/n\lbrack = \{ 0\} \) n’est pas ouvert.

> Remark 3. Caution, an infinite intersection of open sets may not be open. For example, in \( \mathbb{R},{ \cap }_{n \in {\mathbb{N}}^{ * }}\rbrack - 1/n,1/n\lbrack = \{ 0\} \) is not open.

Fermés.

> Closed sets.

DéFINITION 7. Une partie \( F \) de \( E \) est dite fermée (ou \( F \) un fermé) si \( E \smallsetminus F \) est ouvert.

> DEFINITION 7. A subset \( F \) of \( E \) is said to be closed (or \( F \) a closed set) if \( E \smallsetminus F \) is open.

Exemple 4. Une boule fermée est un fermé. En particulier, un singleton \( \{ x\} = {\mathrm{B}}_{\mathrm{f}}\left( {x,0}\right) \) est un fermé. Dans \( \mathbb{R} \) , les intervalles fermés \( \left\lbrack {\alpha ,\beta }\right\rbrack \) sont des fermés.

> Example 4. A closed ball is a closed set. In particular, a singleton \( \{ x\} = {\mathrm{B}}_{\mathrm{f}}\left( {x,0}\right) \) is a closed set. In \( \mathbb{R} \), the closed intervals \( \left\lbrack {\alpha ,\beta }\right\rbrack \) are closed sets.

Proposition 3. (i) Les parties \( \varnothing \) et \( E \) sont des fermés.

> Proposition 3. (i) The subsets \( \varnothing \) and \( E \) are closed sets.

(ii) Une intersection de fermés est un fermé.

> (ii) An intersection of closed sets is a closed set.

(iii) Une réunion finie de fermés est un fermé.

> (iii) A finite union of closed sets is a closed set.

Remarque 4. Attention, une réunion infinie de fermés peut ne pas être fermée. Par exemple, dans \( \mathbb{R},{ \cup }_{n \in {\mathbb{N}}^{ * }}\left\lbrack {1/n,1 - 1/n}\right\rbrack = \rbrack 0,1\lbrack \) n’est pas un fermé.

> Remark 4. Caution, an infinite union of closed sets may not be closed. For example, in \( \mathbb{R},{ \cup }_{n \in {\mathbb{N}}^{ * }}\left\lbrack {1/n,1 - 1/n}\right\rbrack = \rbrack 0,1\lbrack \) is not a closed set.

Voisinages.

> Neighborhoods.

DéFINITION 8. On appelle voisinage d’un élément \( x \) de \( E \) toute partie \( V \) de \( E \) contenant un ouvert contenant \( x \) . L’ensemble des voisinages de \( x \) est noté \( \mathcal{V}\left( x\right) \) .

> DEFINITION 8. A neighborhood of an element \( x \) of \( E \) is any subset \( V \) of \( E \) containing an open set that contains \( x \). The set of neighborhoods of \( x \) is denoted by \( \mathcal{V}\left( x\right) \).

Exemple 5. Un ouvert contenant \( x \) est un voisinage de \( x \) , une boule fermée de centre \( x \) de rayon \( \rho > 0 \) est un voisinage de \( x \) .

> Example 5. An open set containing \( x \) is a neighborhood of \( x \); a closed ball centered at \( x \) with radius \( \rho > 0 \) is a neighborhood of \( x \).

Remarque 5. Une réunion (resp. une intersection finie) de voisinages de \( x \) est un voisinage de \( x \) .

> Remark 5. A union (resp. a finite intersection) of neighborhoods of \( x \) is a neighborhood of \( x \).

Commentaire sur les espaces topologiques généraux.

> Commentary on general topological spaces.

Un espace topologique général \( E \) est défini comme étant un ensemble muni d’une partie de \( \mathcal{P}\left( E\right) \) dont les éléments sont appelés des ouverts et vérifient les axiomes (i),(ii) et (iii) de la proposition 2. On définit alors les fermés comme à la définition 7 et les voisinages comme à la définition 8.

> A general topological space \( E \) is defined as a set equipped with a subset of \( \mathcal{P}\left( E\right) \) whose elements are called open sets and satisfy axioms (i), (ii), and (iii) of Proposition 2. Closed sets are then defined as in Definition 7 and neighborhoods as in Definition 8.

Toutes les notions de cette partie 1.2 peuvent être étendues aux espaces topologiques.

> All concepts in this part 1.2 can be extended to topological spaces.

Il existe pour les espaces topologiques généraux une notion importante appelée la séparation. Un espace topologique \( E \) est dit séparé si pour tous éléments \( x, y \in E, x \neq y \) , il existe \( V \in \mathcal{V}\left( x\right) \) et \( W \in \mathcal{V}\left( y\right) \) tels que \( V \cap W = \varnothing \) . On voit facilement que tout espace métrique est séparé.

> There exists an important notion for general topological spaces called separation. A topological space \( E \) is said to be separated (Hausdorff) if for any elements \( x, y \in E, x \neq y \), there exist \( V \in \mathcal{V}\left( x\right) \) and \( W \in \mathcal{V}\left( y\right) \) such that \( V \cap W = \varnothing \). It is easy to see that every metric space is separated.

Adhérence.

> Closure.

DÉFINITION 9. L’adhérence d’une partie \( A \) de \( E \) , notée \( \bar{A} \) , est le plus petit ensemble fermé contenant \( A \) .

> DEFINITION 9. The closure of a subset \( A \) of \( E \), denoted by \( \bar{A} \), is the smallest closed set containing \( A \).

Remarque 6. - L’ensemble \( \bar{A} \) existe, c’est l’intersection des fermés contenant \( A \) .

> Remark 6. - The set \( \bar{A} \) exists; it is the intersection of all closed sets containing \( A \).

- Une partie \( A \) est fermée si et seulement si \( A = \bar{A} \) .

> - A subset \( A \) is closed if and only if \( A = \bar{A} \).

Proposition 4. Soit A une partie de E. Un élément \( x \) de \( E \) est dans \( \bar{A} \) si et seulement si l'une des assertions suivantes est vérifiée :

> Proposition 4. Let A be a subset of E. An element \( x \) of \( E \) is in \( \bar{A} \) if and only if one of the following assertions is satisfied:

(i) \( \forall \varepsilon > 0,\exists a \in A,\;\mathrm{\;d}\left( {a, x}\right) < \varepsilon \) .

> (ii) Pour tout voisinage \( V \) de \( x, V \cap A \neq \varnothing \) .

(ii) For every neighborhood \( V \) of \( x, V \cap A \neq \varnothing \).

> (iii) \( \mathrm{d}\left( {x, A}\right) = 0 \) .

(iii) \( \mathrm{d}\left( {x, A}\right) = 0 \).

> Exemple 6. — Dans ℝ, l’adhérence de tout intervalle ouvert borné ] \( \alpha ,\beta \) [ est \( \left\lbrack {\alpha ,\beta }\right\rbrack \) .

Example 6. — In ℝ, the closure of any bounded open interval ] \( \alpha ,\beta \) [ is \( \left\lbrack {\alpha ,\beta }\right\rbrack \).

> - Dans un e.v.n, on a \( \overline{\mathrm{B}\left( {0,1}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) , propriété fausse dans un espace métrique général (voir l'exercice 1).

- In a n.v.s., we have \( \overline{\mathrm{B}\left( {0,1}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \), a property that is false in a general metric space (see exercise 1).

> — Si \( A \) est fermé, on a

— If \( A \) is closed, we have

\[
x \in  A \Leftrightarrow  x \in  \bar{A} \Leftrightarrow  \mathrm{d}\left( {x, A}\right)  = 0.
\]

DÉFINITION 10. Une partie \( A \) de \( E \) est dite dense dans \( E \) si \( \bar{A} = E \) .

> DEFINITION 10. A subset \( A \) of \( E \) is said to be dense in \( E \) if \( \bar{A} = E \).

Exemple 7. En utilisant la proposition précédente, on voit facilement qu'une partie \( A \) de \( \mathbb{R} \) est dense dans \( \mathbb{R} \) ( \( \mathbb{R} \) étant muni de la distance usuelle) si et seulement si

> Example 7. Using the previous proposition, it is easy to see that a subset \( A \) of \( \mathbb{R} \) is dense in \( \mathbb{R} \) (\( \mathbb{R} \) being equipped with the usual distance) if and only if

\[
\left( {\forall \left( {a, b}\right)  \in  {\mathbb{R}}^{2}, a < b}\right) ,\;\rbrack a, b\lbrack  \cap  A \neq  \varnothing .
\]

Par exemple, \( \mathbb{Q} \) et \( \mathbb{R} \smallsetminus \mathbb{Q} \) sont denses dans \( \mathbb{R} \) .

> For example, \( \mathbb{Q} \) and \( \mathbb{R} \smallsetminus \mathbb{Q} \) are dense in \( \mathbb{R} \).

Intérieur.

> Interior.

DéFINITION 11. L’intérieur d’une partie \( A \) de \( E \) , noté \( A \) , est le plus grand ouvert contenu dans \( A \) .

> DEFINITION 11. The interior of a subset \( A \) of \( E \), denoted by \( A \), is the largest open set contained in \( A \).

Remarque 7. - L’intérieur de \( A \) existe : c’est la réunion des ouverts contenus dans A.

> Remark 7. - The interior of \( A \) exists: it is the union of all open sets contained in A.

- Une partie \( A \) de \( E \) est ouverte si et seulement si \( A = A \) .

> - A subset \( A \) of \( E \) is open if and only if \( A = A \) .

- Pour toute partie \( A \) de \( E,\overset{ \circ  }{A} = E \smallsetminus  \overline{\left( E \smallsetminus  A\right) } \) et \( \bar{A} = E \smallsetminus  \overset{\text{ ⏜ }}{\left( E \smallsetminus  A\right) } \) .

> - For any subset \( A \) of \( E,\overset{ \circ  }{A} = E \smallsetminus  \overline{\left( E \smallsetminus  A\right) } \) and \( \bar{A} = E \smallsetminus  \overset{\text{ ⏜ }}{\left( E \smallsetminus  A\right) } \) .

Proposition 5. Soit A une partie de E et x un élément de A. On a \( x \in \overset{ \circ }{A} \) si et seulement si l'une des assertions suivantes est vérifiée.

> Proposition 5. Let A be a subset of E and x an element of A. We have \( x \in \overset{ \circ }{A} \) if and only if one of the following assertions is satisfied.

(i) A est un voisinage de \( x \) .

> (i) A is a neighborhood of \( x \) .

(ii) Il existe \( \varepsilon > 0 \) tel que \( \mathrm{B}\left( {x,\varepsilon }\right) \subset A \) .

> (ii) There exists \( \varepsilon > 0 \) such that \( \mathrm{B}\left( {x,\varepsilon }\right) \subset A \) .

Exemple 8. Dans \( \mathbb{R} \) , l’intérieur de \( \left\lbrack {\alpha ,\beta }\right\rbrack \) est \( \rbrack \alpha ,\beta \lbrack \) ; l’intérieur de \( \mathbb{Q} \) , de \( \mathbb{R} \smallsetminus \mathbb{Q} \) , est \( \varnothing \) .

> Example 8. In \( \mathbb{R} \) , the interior of \( \left\lbrack {\alpha ,\beta }\right\rbrack \) is \( \rbrack \alpha ,\beta \lbrack \) ; the interior of \( \mathbb{Q} \) , of \( \mathbb{R} \smallsetminus \mathbb{Q} \) , is \( \varnothing \) .

##### Boundary.

*Français : Frontière.*

DéFINITION 12. La frontière d’une partie \( A \) de \( E \) est l’ensemble \( \bar{A} \smallsetminus \overset{ \circ }{A} \) . On la note \( \operatorname{Fr}\left( A\right) \) (ou encore \( \partial A \) ).

> DEFINITION 12. The boundary of a subset \( A \) of \( E \) is the set \( \bar{A} \smallsetminus \overset{ \circ }{A} \) . It is denoted by \( \operatorname{Fr}\left( A\right) \) (or also \( \partial A \) ).

##### Accumulation point, isolated point.

*Français : Point d'accumulation, point isolé.*

DéFINITION 13. Soit \( A \) une partie de \( E \) .

> DEFINITION 13. Let \( A \) be a subset of \( E \) .

- On dit que \( a \in  E \) est un point d’accumulation de \( A \) si pour tout voisinage \( V \) de \( a \) , \( V \cap  A \neq  \varnothing \) et \( V \cap  A \neq  \{ a\} \) , ce qui s’écrit encore

> - We say that \( a \in  E \) is an accumulation point of \( A \) if for every neighborhood \( V \) of \( a \) , \( V \cap  A \neq  \varnothing \) and \( V \cap  A \neq  \{ a\} \) , which is also written

\[
\left( {\forall \varepsilon  > 0}\right) ,\;\mathrm{B}\left( {a,\varepsilon }\right)  \cap  A \neq  \varnothing \text{ et } \neq  \{ a\} .
\]

- On dit que \( a \in  A \) est un point isolé de \( A \) s’il existe un voisinage \( V \) de \( a \) tel que \( V \cap  A = \{ a\} \) , ce qui s’écrit encore

> - We say that \( a \in  A \) is an isolated point of \( A \) if there exists a neighborhood \( V \) of \( a \) such that \( V \cap  A = \{ a\} \) , which is also written

\[
\left( {\exists \varepsilon  > 0}\right) ,\;\mathrm{B}\left( {a,\varepsilon }\right)  \cap  A = \{ a\} .
\]

Remarque 8. Si a est un point d’accumulation de \( A \) , alors \( a \in \bar{A} \) et de plus pour tout \( \varepsilon > 0,\mathrm{\;B}\left( {a,\varepsilon }\right) \) contient une infinité de points de \( A \) .

> Remark 8. If a is an accumulation point of \( A \) , then \( a \in \bar{A} \) and furthermore for every \( \varepsilon > 0,\mathrm{\;B}\left( {a,\varepsilon }\right) \) contains an infinite number of points of \( A \) .

Exemple 9. Dans \( \mathbb{R},0 \) est point d’accumulation de l’ensemble \( \left\{ {1/n, n \in {\mathbb{N}}^{ * }}\right\} \) .

> Example 9. In \( \mathbb{R},0 \) is an accumulation point of the set \( \left\{ {1/n, n \in {\mathbb{N}}^{ * }}\right\} \) .

Topologie induite dans un espace métrique. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( A \subset E \) . Une manière bien naturelle de faire de \( A \) un espace métrique est de le munir de la restriction de la distance \( d \) de \( E \) à \( A \times A \) . Ainsi, \( \left( {A,\mathrm{\;d}}\right) \) est un espace métrique dont la topologie est appelée topologie induite par \( \left( {E,\mathrm{\;d}}\right) \) . La proposition suivante permet de caractériser les ouverts, fermés et voisinages de \( A \) par rapport à ceux de \( E \) .

> Induced topology in a metric space. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( A \subset E \) . A very natural way to make \( A \) a metric space is to equip it with the restriction of the distance \( d \) of \( E \) to \( A \times A \) . Thus, \( \left( {A,\mathrm{\;d}}\right) \) is a metric space whose topology is called the topology induced by \( \left( {E,\mathrm{\;d}}\right) \) . The following proposition allows us to characterize the open sets, closed sets, and neighborhoods of \( A \) with respect to those of \( E \) .

Proposition 6. Soit A une partie de \( E \) .

> Proposition 6. Let A be a subset of \( E \) .

- Les ouverts de A sont les ensembles de la forme \( \Omega  \cap  A,\Omega \) étant un ouvert de E.

> - The open sets of A are the sets of the form \( \Omega  \cap  A,\Omega \) where \( \Omega  \cap  A,\Omega \) is an open set of E.

- Les fermés de A sont les ensembles de la forme \( F \cap  A \) , où \( F \) est un fermé de \( E \) .

> - The closed sets of A are the sets of the form \( F \cap  A \) , where \( F \) is a closed set of \( E \) .

- Si a \( \in  A \) , les voisinages de a dans A sont les ensembles de la forme \( V \cap  A, V \) étant un voisinage de a dans \( E \) .

> - If a \( \in  A \) , the neighborhoods of a in A are the sets of the form \( V \cap  A, V \) where \( V \cap  A, V \) is a neighborhood of a in \( E \) .

Exemple 10. L’ensemble \( \lbrack 0,1\lbrack \) est un ouvert de \( A = \left\lbrack {0,2}\right\rbrack \) (on peut écrire par exemple \( \left\lbrack {0,1\left\lbrack = \right\rbrack - 1,1\lbrack \cap A}\right\rbrack \) .

> Example 10. The set \( \lbrack 0,1\lbrack \) is an open set of \( A = \left\lbrack {0,2}\right\rbrack \) (we can write for example \( \left\lbrack {0,1\left\lbrack = \right\rbrack - 1,1\lbrack \cap A}\right\rbrack \) .
