#### 1.3. Continuity

*Français : 1.3. Continuité*

##### Continuous maps.

*Français : Applications continues.*

DéFINITION 14. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) deux espaces métriques, et \( f : E \rightarrow {E}^{\prime } \) une application. On dit que \( f \) est continue en \( a \in E \) si pour tout voisinage \( W \) de \( f\left( a\right) \) , il existe un voisinage \( V \) de \( a \) tel que \( f\left( V\right) \subset W \) . Lorsque \( f \) est continue en tout point de \( E \) , on dit que \( f \) est continue sur \( E \) .

> DEFINITION 14. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) be two metric spaces, and \( f : E \rightarrow {E}^{\prime } \) be a map. We say that \( f \) is continuous at \( a \in E \) if for every neighborhood \( W \) of \( f\left( a\right) \) , there exists a neighborhood \( V \) of \( a \) such that \( f\left( V\right) \subset W \) . When \( f \) is continuous at every point of \( E \) , we say that \( f \) is continuous on \( E \) .

Proposition 7. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) deux espaces métriques, et soit \( f : E \rightarrow {E}^{\prime } \) une application. Alors \( f \) est continue en \( a \in E \) si et seulement si

> Proposition 7. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) be two metric spaces, and let \( f : E \rightarrow {E}^{\prime } \) be a map. Then \( f \) is continuous at \( a \in E \) if and only if

\[
\left( {\forall \varepsilon  > 0,\exists \alpha  > 0,\forall x \in  E}\right) ,\;\left( {\mathrm{d}\left( {a, x}\right)  < \alpha  \Rightarrow  {\mathrm{d}}^{\prime }\left( {f\left( a\right) , f\left( x\right) }\right)  < \varepsilon }\right) .
\]

Proposition 8. Soient \( \left( {E,\mathrm{\;d}}\right) ,\left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) ,\left( {{E}^{\prime \prime },{\mathrm{d}}^{\prime \prime }}\right) \) trois espaces métriques, et deux applications \( f : E \rightarrow {E}^{\prime } \) et \( g : {E}^{\prime } \rightarrow {E}^{\prime \prime } \) . Si \( f \) est continue en \( a \in E \) et \( g \) continue en \( f\left( a\right) \) , alors l’application \( g \circ f : E \rightarrow {E}^{\prime \prime } \) est continue en a.

> Proposition 8. Let \( \left( {E,\mathrm{\;d}}\right) ,\left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) ,\left( {{E}^{\prime \prime },{\mathrm{d}}^{\prime \prime }}\right) \) be three metric spaces, and two maps \( f : E \rightarrow {E}^{\prime } \) and \( g : {E}^{\prime } \rightarrow {E}^{\prime \prime } \) . If \( f \) is continuous at \( a \in E \) and \( g \) is continuous at \( f\left( a\right) \) , then the map \( g \circ f : E \rightarrow {E}^{\prime \prime } \) is continuous at a.

Proposition 9. Soit \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) une application. Les trois assertions suivantes sont équivalentes.

> Proposition 9. Let \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) be a map. The following three assertions are equivalent.

(i) \( f \) est continue sur \( E \) .

> (i) \( f \) is continuous on \( E \) .

(ii) L'image réciproque par \( f \) de tout ouvert de \( {E}^{\prime } \) est un ouvert de \( E \) .

> (ii) The preimage under \( f \) of every open set of \( {E}^{\prime } \) is an open set of \( E \) .

(iii) L’image réciproque par \( f \) de tout fermé de \( {E}^{\prime } \) est un fermé de \( E \) .

> (iii) The preimage under \( f \) of every closed set of \( {E}^{\prime } \) is a closed set of \( E \) .

Remarque 9. Lorsque l’image de tout ouvert par \( f \) est un ouvert, on dit que \( f \) est une application ouverte. Une application continue n'est pas forcément ouverte (considérer par exemple une fonction constante sur \( \mathbb{R} \) ). De même, l’image d’un fermé par une application continue n'est pas forcément fermée. Par exemple,

> Remark 9. When the image of every open set under \( f \) is an open set, we say that \( f \) is an open map. A continuous map is not necessarily open (consider for example a constant function on \( \mathbb{R} \) ). Similarly, the image of a closed set under a continuous map is not necessarily closed. For example,

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  \frac{x}{1 + \left| x\right| }
\]

est continue et \( f\left( \mathbb{R}\right) = \rbrack - 1,1\lbrack \) n’est pas fermé.

> is continuous and \( f\left( \mathbb{R}\right) = \rbrack - 1,1\lbrack \) is not closed.

Homéomorphismes.

> Homeomorphisms.

DÉFINITION 15. Soit une application \( F : \;\left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) . On dit que \( f \) est un homéomorphisme si \( f \) est bijective, continue, et si \( {f}^{-1} \) est continue.

> DEFINITION 15. Let \( F : \;\left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) be a map. We say that \( f \) is a homeomorphism if \( f \) is bijective, continuous, and if \( {f}^{-1} \) is continuous.

Remarque 10. Une application peut être continue et bijective sans que l'application réciproque ne soit continue. Par exemple, l’application identité \( f \) de \( \left( {\mathbb{R},{\mathrm{d}}_{\text{ dis }}}\right) \) dans \( \left( {\mathbb{R},\mathrm{d}}\right) \) ( \( {\mathrm{d}}_{\text{ dis }} \) désignant la distance discrète sur \( \mathbb{R} \) , \( \mathrm{d} \) la distance usuelle) est continue mais \( {f}^{-1} \) n’est pas continue. (Cependant, on sait que si \( f : \left( {\mathbb{R},\mathrm{d}}\right) \rightarrow \left( {\mathbb{R},\mathrm{d}}\right) \) est continue et bijective, alors \( {f}^{-1} \) est continue. Sous certaines hypothèses de compacité, il est également possible de conclure à la continuité de l'application réciproque - voir la proposition 14 page 31.)

> Remark 10. A map can be continuous and bijective without its inverse map being continuous. For example, the identity map \( f \) from \( \left( {\mathbb{R},{\mathrm{d}}_{\text{ dis }}}\right) \) to \( \left( {\mathbb{R},\mathrm{d}}\right) \) (where \( {\mathrm{d}}_{\text{ dis }} \) denotes the discrete distance on \( \mathbb{R} \) and \( \mathrm{d} \) the usual distance) is continuous, but \( {f}^{-1} \) is not continuous. (However, we know that if \( f : \left( {\mathbb{R},\mathrm{d}}\right) \rightarrow \left( {\mathbb{R},\mathrm{d}}\right) \) is continuous and bijective, then \( {f}^{-1} \) is continuous. Under certain compactness hypotheses, it is also possible to conclude that the inverse map is continuous - see Proposition 14 on page 31.)

DéFINITION 16. Deux distances \( \mathrm{d} \) et \( {\mathrm{d}}^{\prime } \) sur \( E \) sont dites topologiquement équivalentes si elles définissent la même topologie (i. e. si les ouverts de \( \left( {E,\mathrm{\;d}}\right) \) sont des ouverts de \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) et réciproquement).

> DEFINITION 16. Two distances \( \mathrm{d} \) and \( {\mathrm{d}}^{\prime } \) on \( E \) are said to be topologically equivalent if they define the same topology (i.e., if the open sets of \( \left( {E,\mathrm{\;d}}\right) \) are open sets of \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) and vice versa).

Proposition 10. Deux distances \( d \) et \( {d}^{\prime } \) sur \( E \) sont topologiquement équivalentes si et seulement si l'application identité de \( \left( {E,\mathrm{\;d}}\right) \) sur \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) est un homéomorphisme.

> Proposition 10. Two distances \( d \) and \( {d}^{\prime } \) on \( E \) are topologically equivalent if and only if the identity map from \( \left( {E,\mathrm{\;d}}\right) \) to \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) is a homeomorphism.

Remarque 11. Si d et d' sont topologiquement équivalentes, les espaces métriques \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) possèdent les mêmes propriétés topologiques (en effet, les ouverts de ces deux espaces métriques coïncident, et il en est donc de même pour les fermés et les voisinages).

> Remark 11. If d and d' are topologically equivalent, the metric spaces \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) possess the same topological properties (indeed, the open sets of these two metric spaces coincide, and the same is therefore true for closed sets and neighborhoods).

Normes et distances équivalentes.

> Equivalent norms and distances.

DéFINITION 17. - Deux normes \( {N}_{1} \) et \( {N}_{2} \) sur un même e.v \( E \) sont dites équivalentes s’il existe \( a > 0 \) et \( b > 0 \) tels que pour tout \( x \in E, a{N}_{1}\left( x\right) \leq {N}_{2}\left( x\right) \leq b{N}_{1}\left( x\right) \) .

> DEFINITION 17. - Two norms \( {N}_{1} \) and \( {N}_{2} \) on the same v.s. \( E \) are said to be equivalent if there exist \( a > 0 \) and \( b > 0 \) such that for all \( x \in E, a{N}_{1}\left( x\right) \leq {N}_{2}\left( x\right) \leq b{N}_{1}\left( x\right) \) .

- Deux distances \( {\mathrm{d}}_{1} \) et \( {\mathrm{d}}_{2} \) sur \( E \) sont dites équivalentes s’il existe \( a > 0 \) et \( b > 0 \) tels que pour tout \( x, y \in  E, a{\mathrm{\;d}}_{1}\left( {x, y}\right)  \leq  {\mathrm{d}}_{2}\left( {x, y}\right)  \leq  b{\mathrm{\;d}}_{1}\left( {x, y}\right) \) .

> - Two distances \( {\mathrm{d}}_{1} \) and \( {\mathrm{d}}_{2} \) on \( E \) are said to be equivalent if there exist \( a > 0 \) and \( b > 0 \) such that for all \( x, y \in  E, a{\mathrm{\;d}}_{1}\left( {x, y}\right)  \leq  {\mathrm{d}}_{2}\left( {x, y}\right)  \leq  b{\mathrm{\;d}}_{1}\left( {x, y}\right) \) .

Remarque 12. - Deux normes équivalentes induisent deux distances équivalentes.

> Remark 12. - Two equivalent norms induce two equivalent distances.

- Deux distances équivalentes sont topologiquement équivalentes. Ainsi, les résultats de nature topologiques sont indépendant du choix de l'une ou l'autre des distances.

> - Two equivalent distances are topologically equivalent. Thus, results of a topological nature are independent of the choice of one distance or the other.

- On verra plus loin (voir le théorème 3 page 50) que sur un e.v de dimension finie, toutes les normes sont équivalentes.

> - We will see later (see Theorem 3 on page 50) that on a finite-dimensional v.s., all norms are equivalent.

##### Uniformly continuous maps.

*Français : Applications uniformément continues.*

DÉFINITION 18. Une application \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) est dite uniformément continue sur \( E \) si

> DEFINITION 18. A map \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) is said to be uniformly continuous on \( E \) if

\[
\left( {\forall \varepsilon  > 0,\exists \alpha  > 0,\forall x, y \in  E}\right) ,\;\left( {\mathrm{d}\left( {x, y}\right)  < \alpha  \Rightarrow  {\mathrm{d}}^{\prime }\left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon }\right) .
\]

Remarque 13. - Une fonction uniformément continue est continue; la nuance entre ces deux notions est qu’une fonction uniformément continue vérifie \( {\mathrm{d}}^{\prime }\left( {f\left( x\right) , f\left( y\right) }\right) < \; \varepsilon \) pour tous les couples \( \left( {x, y}\right) \) tels que \( \mathrm{d}\left( {x, y}\right) < \alpha ,\alpha \) étant indépendant de \( x \) , alors que pour une fonction continue, \( \alpha \) dépend de \( x \) . L’uniformité de cet \( \alpha > 0 \) pour une fonction uniformément continue \( f \) en fait une fonction souple d’emploi. Du coup, certains théorèmes sont vrais pour les fonctions uniformément continues mais pas pour les fonctions continues. Nous verrons cependant que toute fonction continue sur un compact y est uniformément continue (voir le théorème 2 page 31).

> Remark 13. - A uniformly continuous function is continuous; the nuance between these two notions is that a uniformly continuous function satisfies \( {\mathrm{d}}^{\prime }\left( {f\left( x\right) , f\left( y\right) }\right) < \; \varepsilon \) for all pairs \( \left( {x, y}\right) \) such that \( \mathrm{d}\left( {x, y}\right) < \alpha ,\alpha \) is independent of \( x \), whereas for a continuous function, \( \alpha \) depends on \( x \). The uniformity of this \( \alpha > 0 \) for a uniformly continuous function \( f \) makes it a flexible function to use. Consequently, some theorems are true for uniformly continuous functions but not for continuous functions. We will see, however, that any continuous function on a compact set is uniformly continuous there (see Theorem 2 on page 31).

— Attention ! L'uniforme continuité n'est pas une notion topologique. Autrement dit, la seule définition de la topologie de \( E \) et \( {E}^{\prime } \) ne suffit pas à définir l’uniforme conti-nuité. En particulier, une fonction uniformément continue vis-à-vis d'une certaine distance ne l'est pas forcément vis-à-vis d'une distance topologiquement équivalente. Par contre, une fonction uniformément continue de \( \left( {E,{\mathrm{d}}_{1}}\right) \) dans \( \left( {{E}^{\prime },{\mathrm{d}}_{1}^{\prime }}\right) \) , lorsqu’elle est regardée comme une fonction de \( \left( {E,{\mathrm{d}}_{2}}\right) \) dans \( \left( {{E}^{\prime },{\mathrm{d}}_{2}^{\prime }}\right) \) , reste uniformément continue lorsque les distances \( {\mathrm{d}}_{1},{\mathrm{\;d}}_{2} \) et \( {\mathrm{d}}_{1}^{\prime },{\mathrm{d}}_{2}^{\prime } \) sont équivalentes, ou lorsqu’elles sont uniformément équivalentes (voir la définition qui suit).

> — Warning! Uniform continuity is not a topological notion. In other words, the mere definition of the topology of \( E \) and \( {E}^{\prime } \) is not sufficient to define uniform continuity. In particular, a function that is uniformly continuous with respect to a certain distance is not necessarily so with respect to a topologically equivalent distance. However, a function that is uniformly continuous from \( \left( {E,{\mathrm{d}}_{1}}\right) \) to \( \left( {{E}^{\prime },{\mathrm{d}}_{1}^{\prime }}\right) \), when viewed as a function from \( \left( {E,{\mathrm{d}}_{2}}\right) \) to \( \left( {{E}^{\prime },{\mathrm{d}}_{2}^{\prime }}\right) \), remains uniformly continuous when the distances \( {\mathrm{d}}_{1},{\mathrm{\;d}}_{2} \) and \( {\mathrm{d}}_{1}^{\prime },{\mathrm{d}}_{2}^{\prime } \) are equivalent, or when they are uniformly equivalent (see the following definition).

Exemple 11. - Une fonction \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) lipschitzienne, c’est-à-dire vérifiant

> Example 11. - A Lipschitz function \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \), that is to say satisfying

\[
\left( {\exists k > 0,\forall x, y \in  E}\right) ,\;{\mathrm{d}}^{\prime }\left( {f\left( x\right) , f\left( y\right) }\right)  \leq  k\mathrm{\;d}\left( {x, y}\right) ,
\]

est uniformément continue.

> is uniformly continuous.

- La fonction \( f : \rbrack 0,1\rbrack  \rightarrow  \mathbb{R}\;x \mapsto  1/x \) est continue mais n’est pas uniformément continue.

> - The function \( f : \rbrack 0,1\rbrack  \rightarrow  \mathbb{R}\;x \mapsto  1/x \) is continuous but is not uniformly continuous.

La fin de la remarque précédente motive la définition suivante.

> The end of the previous remark motivates the following definition.

DÉFINITION 19. Deux distances \( \mathrm{d} \) et \( {\mathrm{d}}^{\prime } \) sur \( E \) sont dites uniformément équivalentes si l’application identité est uniformément continue de \( \left( {E,\mathrm{\;d}}\right) \) dans \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) et de \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) dans \( \left( {E,\mathrm{\;d}}\right) \) .

> DEFINITION 19. Two distances \( \mathrm{d} \) and \( {\mathrm{d}}^{\prime } \) on \( E \) are said to be uniformly equivalent if the identity map is uniformly continuous from \( \left( {E,\mathrm{\;d}}\right) \) to \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) and from \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) to \( \left( {E,\mathrm{\;d}}\right) \).

Remarque 14. Deux distances équivalentes sont uniformément équivalentes. Deux distances uniformément équivalentes sont topologiquement équivalentes.

> Remark 14. Two equivalent distances are uniformly equivalent. Two uniformly equivalent distances are topologically equivalent.
