#### 3.4. Compact sets and continuous maps

*Français : 3.4. Compacts et applications continues*

Proposition 13. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique compact, \( \left( {F,\delta }\right) \) un espace métrique et une application continue \( f : E \rightarrow F \) . Alors \( f\left( E\right) \) est compact.

> Proposition 13. Let \( \left( {E,\mathrm{\;d}}\right) \) be a compact metric space, \( \left( {F,\delta }\right) \) a metric space, and \( f : E \rightarrow F \) a continuous map. Then \( f\left( E\right) \) is compact.

Remarque 6. Cette proposition entraîne que l’image par \( f \) de tout fermé de \( E \) (où \( E \) est compact) est un fermé (une application vérifiant cette propriété est dite fermée). Ceci est faux en général. En corollaire (et grâce à la proposition 9), on a le résultat qui suit.

> Remark 6. This proposition implies that the image under \( f \) of any closed set of \( E \) (where \( E \) is compact) is a closed set (a map satisfying this property is called a closed map). This is false in general. As a corollary (and thanks to proposition 9), we have the following result.

Proposition 14. Soit \( f : \;\left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) une application continue et bijective. Si \( \left( {E,\mathrm{\;d}}\right) \) est compact, alors \( {f}^{-1} : \;F \rightarrow E \) est continue (en d’autres termes, \( f \) est un homéomorphisme).

> Proposition 14. Let \( f : \;\left( {E,\mathrm{\;d}}\right) \rightarrow \left( {F,\delta }\right) \) be a continuous and bijective map. If \( \left( {E,\mathrm{\;d}}\right) \) is compact, then \( {f}^{-1} : \;F \rightarrow E \) is continuous (in other words, \( f \) is a homeomorphism).

Remarque 7. Pour toute fonction continue et bijective \( f : I \rightarrow J \) , où \( I \) et \( J \) sont des intervalles de \( \mathbb{R} \) , l’application réciproque \( {f}^{-1} \) est continue. Il suffit en effet d’appliquer la proposition précédente à la restriction de \( f \) à tout segment (donc compact) de \( I \) .

> Remark 7. For any continuous and bijective function \( f : I \rightarrow J \) , where \( I \) and \( J \) are intervals of \( \mathbb{R} \) , the inverse map \( {f}^{-1} \) is continuous. It suffices indeed to apply the previous proposition to the restriction of \( f \) to any segment (and thus compact) of \( I \) .

- Proposition 15. Soit \( f : \left( {E,\mathrm{\;d}}\right)  \rightarrow  \mathbb{R} \) une application continue, où \( \left( {E,\mathrm{\;d}}\right) \) est compact. Alors \( f \) est bornée et atteint ses bornes. En d’autres termes, il existe \( c, d \in  E \) tels que

> - Proposition 15. Let \( f : \left( {E,\mathrm{\;d}}\right)  \rightarrow  \mathbb{R} \) be a continuous map, where \( \left( {E,\mathrm{\;d}}\right) \) is compact. Then \( f \) is bounded and attains its bounds. In other words, there exist \( c, d \in  E \) such that

\[
f\left( c\right)  = \mathop{\inf }\limits_{{x \in  E}}f\left( x\right) \;\text{ et }\;f\left( d\right)  = \mathop{\sup }\limits_{{x \in  E}}f\left( x\right) .
\]

Remarque 8. On verra (voir le théorème 3 page 41) que si \( f : \mathbb{R} \rightarrow \mathbb{R} \) est une application continue, l’image par \( f \) d’un intervalle est un intervalle (c’est le théorème des valeurs intermédiaires). Avec cette dernière proposition, on en déduit que l’image par \( f \) d’un intervalle fermé borné est un intervalle fermé borné.

> Remark 8. We will see (see theorem 3 on page 41) that if \( f : \mathbb{R} \rightarrow \mathbb{R} \) is a continuous map, the image under \( f \) of an interval is an interval (this is the intermediate value theorem). With this last proposition, we deduce that the image under \( f \) of a closed bounded interval is a closed bounded interval.

- THÉORÉME 2 (DE HEINE). Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques, \( E \) étant compact, et \( f : E \rightarrow  F \) une application continue. Alors \( f \) est une application uniformément continue.

> - THEOREM 2 (HEINE). Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces, \( E \) being compact, and \( f : E \rightarrow  F \) a continuous map. Then \( f \) is a uniformly continuous map.
