#### 4.5. Line integrals

*Français : 4.5. Intégrales curvilignes*

##### Recalls on parameterized arcs.

*Français : Rappels sur les arcs paramétrés.*

DÉFINITION 8. On appelle arc paramétré de \( {\mathbb{R}}^{n} \) de classe \( {\mathcal{C}}^{k} \) tout couple \( \left( {I, f}\right) \) où \( I \) est un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow {\mathbb{R}}^{n} \) une application de classe \( {\mathcal{C}}^{k} \) . L’ensemble \( f\left( I\right) \subset {\mathbb{R}}^{n} \) est appelé support de l'arc. Un arc paramétré continu est aussi appelé chemin.

> DEFINITION 8. A parameterized arc of \( {\mathbb{R}}^{n} \) of class \( {\mathcal{C}}^{k} \) is any pair \( \left( {I, f}\right) \) where \( I \) is an interval of \( \mathbb{R} \) and \( f : I \rightarrow {\mathbb{R}}^{n} \) is a mapping of class \( {\mathcal{C}}^{k} \). The set \( f\left( I\right) \subset {\mathbb{R}}^{n} \) is called the support of the arc. A continuous parameterized arc is also called a path.

DéFINITION 9. On dit que deux arcs paramétrés \( \left( {I, f}\right) \) et \( \left( {J, g}\right) \) de classe \( {\mathcal{C}}^{k} \) sont \( {\mathcal{C}}^{k} \) -équi-valents s’il existe un \( {\mathcal{C}}^{k} \) -difféomorphisme \( \theta \) de \( J \) sur \( I \) tel que \( g = f \circ \theta \) .

> DEFINITION 9. Two parameterized arcs \( \left( {I, f}\right) \) and \( \left( {J, g}\right) \) of class \( {\mathcal{C}}^{k} \) are said to be \( {\mathcal{C}}^{k} \)-equivalent if there exists a \( {\mathcal{C}}^{k} \)-diffeomorphism \( \theta \) from \( J \) onto \( I \) such that \( g = f \circ \theta \).

On définit ainsi une relation d'équivalence sur les arcs paramétrés. Chaque classe est appelée arc géométrique de classe \( {\mathcal{C}}^{k} \) , tout représentant de classe un paramétrage admissible de l'arc géométrique. Deux paramétrages admissibles d'un même arc géométriques ont même support, on parle donc de support d'un arc géométrique.

> This defines an equivalence relation on parameterized arcs. Each class is called a geometric arc of class \( {\mathcal{C}}^{k} \), and any representative of the class is called an admissible parameterization of the geometric arc. Two admissible parameterizations of the same geometric arc have the same support; we therefore speak of the support of a geometric arc.

Remarque 8. L'application \( \theta \) est soit strictement croissante, soit strictement décroissante.

> Remark 8. The map \( \theta \) is either strictly increasing or strictly decreasing.

DÉFINITION 10. Deux paramétrages admissibles \( \left( {I, f}\right) \) et \( \left( {J, g}\right) \) d’un arc géométrique de classe \( {\mathcal{C}}^{k} \) sont dit de même sens s’il existe un \( {\mathcal{C}}^{k} \) -difféomorphisme croissant de \( J \) sur \( I \) tel que \( g = f \circ \theta \) .

> DEFINITION 10. Two admissible parameterizations \( \left( {I, f}\right) \) and \( \left( {J, g}\right) \) of a geometric arc of class \( {\mathcal{C}}^{k} \) are said to have the same orientation if there exists an increasing \( {\mathcal{C}}^{k} \)-diffeomorphism from \( J \) onto \( I \) such that \( g = f \circ \theta \).

On définit ainsi une relation d'équivalence sur un arc géométrique (dont il y a au plus deux classes d'après la remarque précédente) ; les classes sont appelées arcs géométriques orientés de \( {\mathbb{R}}^{n} \) de classe \( {\mathcal{C}}^{k} \) .

> This defines an equivalence relation on a geometric arc (which has at most two classes according to the previous remark); the classes are called oriented geometric arcs of \( {\mathbb{R}}^{n} \) of class \( {\mathcal{C}}^{k} \).

##### Differential forms of degree 1.

*Français : Formes différentielles de degré 1.*

DéFINITION 11. Soit \( \Omega \) un ouvert de \( {\mathbb{R}}^{n} \) . On appelle forme différentielle de degré 1 sur \( \Omega \) toute application \( \alpha \) de \( \Omega \) sur le dual \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) de \( {\mathbb{R}}^{n} \) .

> DEFINITION 11. Let \( \Omega \) be an open set of \( {\mathbb{R}}^{n} \). A differential form of degree 1 on \( \Omega \) is any map \( \alpha \) from \( \Omega \) to the dual \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) of \( {\mathbb{R}}^{n} \).

On peut écrire la forme différentielle \( \alpha \) sous la forme \( \alpha \left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}\left( x\right) d{x}_{i} \) pour \( x \in \Omega \) (où les \( {a}_{i} \) sont à valeurs réelles et \( \left( {d{x}_{i}}\right) \) est la base duale de la base canonique de \( {\mathbb{R}}^{n} \) ).

> The differential form \( \alpha \) can be written in the form \( \alpha \left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}\left( x\right) d{x}_{i} \) for \( x \in \Omega \) (where the \( {a}_{i} \) are real-valued and \( \left( {d{x}_{i}}\right) \) is the dual basis of the canonical basis of \( {\mathbb{R}}^{n} \)).

S’il existe une fonction \( \varphi : \Omega \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{1} \) telle que \( \alpha = {d\varphi } \) , la forme différentielle \( \alpha \) de degré 1 est dite exacte.

> If there exists a function \( \varphi : \Omega \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{1} \) such that \( \alpha = {d\varphi } \), the differential form \( \alpha \) of degree 1 is said to be exact.

Si \( \alpha \) est de classe \( {\mathcal{C}}^{1} \) (i.e. si les \( {a}_{i} \) sont \( {\mathcal{C}}^{1} \) ), \( \alpha \) est dite fermée si pour tout \( \left( {i, j}\right) \) , \( \frac{\partial {a}_{i}}{\partial {x}_{j}} = \frac{\partial {a}_{j}}{\partial {x}_{i}} \)

> If \( \alpha \) is of class \( {\mathcal{C}}^{1} \) (i.e., if the \( {a}_{i} \) are \( {\mathcal{C}}^{1} \)), \( \alpha \) is said to be closed if for all \( \left( {i, j}\right) \), \( \frac{\partial {a}_{i}}{\partial {x}_{j}} = \frac{\partial {a}_{j}}{\partial {x}_{i}} \)

Remarque 9. Si une forme différentielle de classe \( {\mathcal{C}}^{1} \) est exacte, elle est fermée (conséquence du théorème de Schwarz). La réciproque est vraie lorsque \( \Omega \) est un ouvert étoilé mais est fausse dans le cas général (voir un contre exemple à l'exemple 3).

> Remark 9. If a differential form of class \( {\mathcal{C}}^{1} \) is exact, it is closed (a consequence of Schwarz's theorem). The converse is true when \( \Omega \) is a star-shaped open set but is false in the general case (see a counterexample in Example 3).

Définition d'une intégrale curviligne. On se donne une forme différentielle \( \alpha = \; \mathop{\sum }\limits_{i}{a}_{i}\left( x\right) d{x}_{i} \) de degré 1, définie et continue sur un ouvert \( \Omega \) de \( {\mathbb{R}}^{n} \) .

> Definition of a line integral. Let \( \alpha = \; \mathop{\sum }\limits_{i}{a}_{i}\left( x\right) d{x}_{i} \) be a differential 1-form defined and continuous on an open set \( \Omega \) of \( {\mathbb{R}}^{n} \).

DéFINITION 12. Soit \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) (avec \( f = \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) ) un arc paramétré de \( {\mathbb{R}}^{n} \) de classe \( {\mathcal{C}}^{1} \) dont le support est contenu dans \( \Omega \) . On appelle intégrale curviligne de \( \alpha \) le long de \( \gamma \) le réel

> DEFINITION 12. Let \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) (with \( f = \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) ) be a parameterized arc of \( {\mathbb{R}}^{n} \) of class \( {\mathcal{C}}^{1} \) whose support is contained in \( \Omega \) . The line integral of \( \alpha \) along \( \gamma \) is the real number

\[
{\int }_{\gamma }\alpha  = {\int }_{a}^{b}\alpha \left\lbrack  {f\left( t\right) }\right\rbrack  {f}^{\prime }\left( t\right) {dt} = {\int }_{a}^{b}\left\lbrack  {\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}\left( {f\left( t\right) }\right) {f}_{i}^{\prime }\left( t\right) }\right\rbrack  {dt}.
\]

Remarque 10. Si \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) est un chemin continu de classe \( {\mathcal{C}}^{1} \) par morceaux, c’est-à- dire s’il existe une subdivision \( a = {t}_{0} < {t}_{1} < \cdots < {t}_{p} = b \) de \( \left\lbrack {a, b}\right\rbrack \) telle que \( {f}_{\left| \left\lbrack {t}_{i - 1},{t}_{i}\right\rbrack \right| } \) soit de classe \( {\mathcal{C}}^{1} \) pour tout \( i \in \{ 1,\ldots , p\} \) , on définit de même l’intégrale curvilligne de \( \alpha \) le long de \( \gamma \) par l’expression

> Remark 10. If \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) is a continuous path of class \( {\mathcal{C}}^{1} \) by pieces, that is, if there exists a subdivision \( a = {t}_{0} < {t}_{1} < \cdots < {t}_{p} = b \) of \( \left\lbrack {a, b}\right\rbrack \) such that \( {f}_{\left| \left\lbrack {t}_{i - 1},{t}_{i}\right\rbrack \right| } \) is of class \( {\mathcal{C}}^{1} \) for all \( i \in \{ 1,\ldots , p\} \) , the line integral of \( \alpha \) along \( \gamma \) is defined in the same way by the expression

\[
{\int }_{\gamma }\alpha  = \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}{\int }_{\left( \left\lbrack  {t}_{i},{t}_{i + 1}\right\rbrack  , f\right) }\alpha .
\]

DÉFINITION 13. Soit \( {\Gamma }^{ + } \) un arc géométrique de classe \( {\mathcal{C}}^{1} \) , orienté,à support dans \( \Omega \) . Les intégrales curvilignes de \( \alpha \) le long des paramétrages admissibles de \( {\Gamma }^{ + } \) sont identiques, et leur valeur commune est appelé intégrale curviligne de \( \alpha \) le long de \( {\Gamma }^{ + } \) , et notée \( {\int }_{{\Gamma }^{ + }}\alpha \) .

> DEFINITION 13. Let \( {\Gamma }^{ + } \) be a geometric arc of class \( {\mathcal{C}}^{1} \) , oriented, with support in \( \Omega \) . The line integrals of \( \alpha \) along the admissible parameterizations of \( {\Gamma }^{ + } \) are identical, and their common value is called the line integral of \( \alpha \) along \( {\Gamma }^{ + } \) , and denoted \( {\int }_{{\Gamma }^{ + }}\alpha \) .

Proposition 1. Soit \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) un arc paramétré de \( {\mathbb{R}}^{n} \) de classe \( {\mathcal{C}}^{1} \) à support contenu dans \( \Omega \) . Si \( \alpha \) est une forme exacte, c’est-à-dire \( \alpha = {d\varphi } \) avec \( \varphi : \Omega \rightarrow \mathbb{R} \) de classe \( {\mathcal{C}}^{1} \) , alors

> Proposition 1. Let \( \gamma = \left( {\left\lbrack {a, b}\right\rbrack , f}\right) \) be a parameterized arc of \( {\mathbb{R}}^{n} \) of class \( {\mathcal{C}}^{1} \) with support contained in \( \Omega \) . If \( \alpha \) is an exact form, that is \( \alpha = {d\varphi } \) with \( \varphi : \Omega \rightarrow \mathbb{R} \) of class \( {\mathcal{C}}^{1} \) , then

\[
{\int }_{\gamma }\alpha  = \varphi \left\lbrack  {f\left( b\right) }\right\rbrack   - \varphi \left\lbrack  {f\left( a\right) }\right\rbrack
\]

En particulier, si \( \gamma \) est un lacet (i.e. si \( f\left( a\right) = f\left( b\right) \) ), \( {\int }_{\gamma }\alpha = 0 \) .

> In particular, if \( \gamma \) is a loop (i.e., if \( f\left( a\right) = f\left( b\right) \) ), \( {\int }_{\gamma }\alpha = 0 \) .

Exemple 3. Soit la forme différentielle de degré 1

> Example 3. Let the differential form of degree 1 be

\[
\alpha  : {\mathbb{R}}^{2} \smallsetminus  \{ \left( {0,0}\right) \}  \rightarrow  {\left( {\mathbb{R}}^{2}\right) }^{ * }\;\left( {x, y}\right)  \mapsto  \frac{{xdy} - {ydx}}{{x}^{2} + {y}^{2}}.
\]

On vérifie facilement que l'on a affaire à une forme fermée. Elle n'est cependant pas exacte, car si \( \gamma \) est le lacet \( \left( {\left\lbrack {0,{2\pi }}\right\rbrack , f}\right) \) où \( f\left( \theta \right) = \left( {\cos \theta ,\sin \theta }\right) \) , on trouve \( {\int }_{\gamma }\alpha = {2\pi } \neq 0 \) , et on conclut avec la proposition précédente.

> It is easily verified that we are dealing with a closed form. However, it is not exact, because if \( \gamma \) is the loop \( \left( {\left\lbrack {0,{2\pi }}\right\rbrack , f}\right) \) where \( f\left( \theta \right) = \left( {\cos \theta ,\sin \theta }\right) \) , we find \( {\int }_{\gamma }\alpha = {2\pi } \neq 0 \) , and we conclude with the previous proposition.

Théorème de Green-Riemann. Ce théorème permet de calculer certaines intégrales sur un compact \( K \) en fonction d’une intégrale curviligne le long de sa frontière \( \partial K \) . Intuitivement, le compact \( K \) doit avoir sa frontière qui est une courbe orientable et \( {\mathcal{C}}^{1} \) par morceaux. Nous rendons cette définition plus rigoureuse avec la notion de compact \( \dot{a} \) bord.

> Green-Riemann Theorem. This theorem allows for the calculation of certain integrals over a compact set \( K \) as a function of a line integral along its boundary \( \partial K \) . Intuitively, the compact set \( K \) must have a boundary that is an orientable and piecewise \( {\mathcal{C}}^{1} \) curve. We make this definition more rigorous with the notion of a compact set \( \dot{a} \) with boundary.

DéFINITION 14. Un compact \( K \subset {\mathbb{R}}^{2} \) est dit compact à bord si

> DEFINITION 14. A compact set \( K \subset {\mathbb{R}}^{2} \) is said to be a compact set with boundary if

(i) il existe une famille finie \( \left( {\gamma }_{i}\right) = {\left( {I}_{i},{f}_{i}\right) }_{1 \leq i \leq p} \) de chemins fermés, simples (i. e. injectifs) et \( {\mathcal{C}}^{1} \) par morceaux, dont les supports \( {\mathcal{C}}_{i} \) sont disjoints, et telle que la frontière \( \partial K \) de \( K \) soit la réunion des \( {\mathcal{C}}_{i} \) ;

> (i) there exists a finite family \( \left( {\gamma }_{i}\right) = {\left( {I}_{i},{f}_{i}\right) }_{1 \leq i \leq p} \) of closed, simple (i.e., injective) and piecewise \( {\mathcal{C}}^{1} \) paths, whose supports \( {\mathcal{C}}_{i} \) are disjoint, and such that the boundary \( \partial K \) of \( K \) is the union of the \( {\mathcal{C}}_{i} \) ;

(ii) en tout point \( a = {f}_{i}\left( t\right) \) régulier d’un chemin \( {\gamma }_{i} \) , il existe un pavé \( P \) centré en \( a \) tel que

> (ii) at every regular point \( a = {f}_{i}\left( t\right) \) of a path \( {\gamma }_{i} \) , there exists a rectangle \( P \) centered at \( a \) such that

- \( P \smallsetminus  \partial K \) a deux composantes connexes, l’une notée \( {P}_{1} \) constituée de points de \( K \) , l’autre de points de \( {\mathbb{R}}^{2} \smallsetminus  K \) ;

> - \( P \smallsetminus  \partial K \) has two connected components, one denoted \( {P}_{1} \) consisting of points in \( K \) , the other of points in \( {\mathbb{R}}^{2} \smallsetminus  K \) ;

- pour tout \( b \in  P \) tel que le vecteur \( \overrightarrow{ab} \) fasse un angle \( + \pi /2 \) avec \( {f}_{i}^{\prime }\left( t\right) \) , on a \( b \in  {P}_{1} \) . Pour toute forme différentielle \( \alpha \) de degré 1 définie sur un ouvert contenant \( K \) , la valeur \( \mathop{\sum }\limits_{{i = 1}}^{p}{\int }_{{\gamma }_{i}}\alpha \) est alors indépendante des paramétrages admissibles des arcs géométriques orientés \( {\gamma }_{i} \) . On la note \( {\int }_{\partial {K}^{ + }}\alpha \) .

> - for any \( b \in  P \) such that the vector \( \overrightarrow{ab} \) makes an angle \( + \pi /2 \) with \( {f}_{i}^{\prime }\left( t\right) \) , we have \( b \in  {P}_{1} \) . For any differential form \( \alpha \) of degree 1 defined on an open set containing \( K \) , the value \( \mathop{\sum }\limits_{{i = 1}}^{p}{\int }_{{\gamma }_{i}}\alpha \) is then independent of the admissible parameterizations of the oriented geometric arcs \( {\gamma }_{i} \) . It is denoted by \( {\int }_{\partial {K}^{ + }}\alpha \) .

![bo_d7fjkrs91nqc73ereoog_362_361_1231_790_279_0.jpg](images/gourdon_analysis_fr_en_014_bod7fjkrs91nqc73ereoog36236112317902790.jpg)

Figure 2. Un compact à bord \( K \)

> Figure 2. A compact set with boundary \( K \)

Remarque 11. Dans la pratique, on se contente en général de la notion intuitive suivante : la frontière du compact à bord \( K \) est réunion finie, disjointe de supports d'arcs géométriques orientés, fermés, simples, \( {\mathcal{C}}^{1} \) par morceaux, tels qu’en parcourant cette frontière dans le sens de l’orientation, on ait \( K \) constamment à sa gauche.

> Remark 11. In practice, we generally settle for the following intuitive notion: the boundary of the compact set with boundary \( K \) is a finite, disjoint union of supports of oriented, closed, simple, piecewise \( {\mathcal{C}}^{1} \) geometric arcs, such that by traversing this boundary in the direction of the orientation, one has \( K \) constantly to one's left.

THÉORÉME 6 (GREEN-RIEMANN). Soit \( K \subset {\mathbb{R}}^{2} \) un compact à bord et \( \alpha = {Pdx} + {Qdy} \) une forme différentielle de degré 1, de classe \( {\mathcal{C}}^{1} \) sur un ouvert contenant \( K \) . Alors \( K \) est mesurable et

> THEOREM 6 (GREEN-RIEMANN). Let \( K \subset {\mathbb{R}}^{2} \) be a compact set with boundary and \( \alpha = {Pdx} + {Qdy} \) a differential form of degree 1, of class \( {\mathcal{C}}^{1} \) on an open set containing \( K \) . Then \( K \) is measurable and

\[
{\int }_{\partial {K}^{ + }}\left( {{Pdx} + {Qdy}}\right)  = {\iint }_{K}\left\lbrack  {\frac{\partial Q}{\partial x}\left( {x, y}\right)  - \frac{\partial P}{\partial y}\left( {x, y}\right) }\right\rbrack  {dxdy}.
\]

Application. Si \( K \) est un compact à bord, son aire \( \mathcal{A} = {\iint }_{K}{dxdy} \) peut s’expri-mer, d’après le théorème de Green-Riemann, comme \( \mathcal{A} = {\int }_{\partial {K}^{ + }}{xdy} = - {\int }_{\partial {K}^{ + }}{ydx} = \; \frac{1}{2}{\int }_{\partial {K}^{ + }}\left( {{xdy} - {ydx}}\right) \) . En désignant par \( \left( {r,\theta }\right) \) les coordonnées polaires, on a facilement \( {xdy} - {ydx} = {r}^{2}{d\theta } \) donc \( \mathcal{A} = \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta }. \)

> Application. If \( K \) is a compact set with a boundary, its area \( \mathcal{A} = {\iint }_{K}{dxdy} \) can be expressed, according to the Green-Riemann theorem, as \( \mathcal{A} = {\int }_{\partial {K}^{ + }}{xdy} = - {\int }_{\partial {K}^{ + }}{ydx} = \; \frac{1}{2}{\int }_{\partial {K}^{ + }}\left( {{xdy} - {ydx}}\right) \) . By denoting \( \left( {r,\theta }\right) \) as polar coordinates, we easily have \( {xdy} - {ydx} = {r}^{2}{d\theta } \) therefore \( \mathcal{A} = \frac{1}{2}{\int }_{\partial {K}^{ + }}{r}^{2}{d\theta }. \)
