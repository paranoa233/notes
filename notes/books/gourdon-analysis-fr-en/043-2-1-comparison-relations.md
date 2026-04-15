#### 2.1. Comparison relations

*Français : 2.1. Relations de comparaison*

Soit \( X \) un espace métrique. On considère deux applications \( f, g \) de \( D \subset X \) dans \( E \) et \( {x}_{0} \) un point d’accumulation de \( D \) .

> Let \( X \) be a metric space. Consider two mappings \( f, g \) from \( D \subset X \) to \( E \) and \( {x}_{0} \) an accumulation point of \( D \) .

- On dit que \( f \) est dominée par \( g \) au voisinage de \( {x}_{0} \) si

> - We say that \( f \) is dominated by \( g \) in the neighborhood of \( {x}_{0} \) if

\[
\exists C > 0,\exists V \in  \mathcal{V}\left( {x}_{0}\right) ,\forall x \in  V \cap  D,\;\parallel f\left( x\right) \parallel  \leq  C\parallel g\left( x\right) \parallel
\]

(où \( \mathcal{V}\left( {x}_{0}\right) \) désigne l’ensemble des voisinages de \( {x}_{0} \) ). On note alors \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }O\left( {g\left( x\right) }\right) \)

> (where \( \mathcal{V}\left( {x}_{0}\right) \) denotes the set of neighborhoods of \( {x}_{0} \) ). We then write \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }O\left( {g\left( x\right) }\right) \)

(lire "grand o", notation de Landau) ou encore \( f\left( x\right) \preccurlyeq g\left( x\right) \) (notation de Hardy).

> (read "big O", Landau notation) or \( f\left( x\right) \preccurlyeq g\left( x\right) \) (Hardy notation).

- On dit que \( f \) est négligeable devant \( g \) au voisinage de \( {x}_{0} \) si

> - We say that \( f \) is negligible compared to \( g \) in the neighborhood of \( {x}_{0} \) if

\[
\forall \varepsilon  > 0,\exists V \in  \mathcal{V}\left( {x}_{0}\right) ,\forall x \in  V \cap  D,\;\parallel f\left( x\right) \parallel  \leq  \varepsilon \parallel g\left( x\right) \parallel .
\]

On note alors \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }o\left( {g\left( x\right) }\right) \) (lire "petit o", notation de Landau) ou encore \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ \prec }g\left( x\right) \) (notation de Hardy).

> We then write \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ = }o\left( {g\left( x\right) }\right) \) (read "little o", Landau notation) or \( f\left( x\right) \underset{x \rightarrow {x}_{0}}{ \prec }g\left( x\right) \) (Hardy notation).

- On dit que \( f \) et \( g \) sont équivalentes au voisinage de \( {x}_{0} \) si \( f\left( x\right)  - g\left( x\right) \underset{x \rightarrow  {x}_{0}}{ = }o\left( {g\left( x\right) }\right) \) , et on écrit alors \( f\left( x\right) \underset{x \rightarrow  {x}_{0}}{ \sim  }g\left( x\right) \) .

> - We say that \( f \) and \( g \) are equivalent in the neighborhood of \( {x}_{0} \) if \( f\left( x\right)  - g\left( x\right) \underset{x \rightarrow  {x}_{0}}{ = }o\left( {g\left( x\right) }\right) \) , and we then write \( f\left( x\right) \underset{x \rightarrow  {x}_{0}}{ \sim  }g\left( x\right) \) .

Remarque 8. - Il faut prendre garde au fait que les notations de Landau sont des abus. Lorsqu’on écrit \( f\left( x\right) = O\left( {g\left( x\right) }\right) \) par exemple, il n’y a pas à proprement parler d’égalité (si \( {f}_{1}\left( x\right) = O\left( {g\left( x\right) }\right) \) et \( {f}_{2}\left( x\right) = O\left( {g\left( x\right) }\right) \) , on ne peut pas dire \( {f}_{1}\left( x\right) = {f}_{2}\left( x\right) \) ) - une notation correcte serait \( f\left( x\right) \in O\left( {g\left( x\right) }\right) \) . Cependant, l’usage est bien établi et cette notation est très commode, c'est pourquoi on l'utilise beaucoup.

> Remark 8. - One must be careful with the fact that Landau notations are abuses of language. When writing \( f\left( x\right) = O\left( {g\left( x\right) }\right) \) for example, there is not, strictly speaking, an equality (if \( {f}_{1}\left( x\right) = O\left( {g\left( x\right) }\right) \) and \( {f}_{2}\left( x\right) = O\left( {g\left( x\right) }\right) \) , one cannot say \( {f}_{1}\left( x\right) = {f}_{2}\left( x\right) \) ) - a correct notation would be \( f\left( x\right) \in O\left( {g\left( x\right) }\right) \) . However, the usage is well-established and this notation is very convenient, which is why it is widely used.

- Dans la pratique, on utilisera souvent cette notation pour des fonctions \( \mathbb{R} \rightarrow  \mathbb{C} \) , au voisinage d'un point de \( \mathbb{R} \) ou de l'infini, ou pour des suites réelles ou complexes \( \left( {u}_{n}\right) \) lorsque \( n \rightarrow   + \infty \) .

> - In practice, this notation is often used for functions \( \mathbb{R} \rightarrow  \mathbb{C} \) , in the neighborhood of a point of \( \mathbb{R} \) or infinity, or for real or complex sequences \( \left( {u}_{n}\right) \) when \( n \rightarrow   + \infty \) .

- Attention ! La relation \( \sim \) se manie avec précaution. En particulier, elle n’est pas compatible avec l'addition, par exemple

> - Warning! The relation \( \sim \) must be handled with caution. In particular, it is not compatible with addition, for example

---

\[
x + 2\underset{x \rightarrow   + \infty }{ \sim  }x + 1,\; - x\underset{x \rightarrow   + \infty }{ \sim  } - x\;\text{ et pourtant }2\underset{x \rightarrow   + \infty }{ \sim  }1.
\]

---

Par contre, l’équivalence est compatible avec le produit et la puissance (si \( {f}_{1} \sim {f}_{2} \) et \( {g}_{1} \sim {g}_{2},{f}_{1}{g}_{1} \sim {g}_{1}{g}_{2} \) ; si \( f \sim g,{f}^{\alpha } \sim {g}^{\alpha } \) pour tout \( \alpha \in \mathbb{R} \) ).

> On the other hand, equivalence is compatible with products and powers (if \( {f}_{1} \sim {f}_{2} \) and \( {g}_{1} \sim {g}_{2},{f}_{1}{g}_{1} \sim {g}_{1}{g}_{2} \) ; if \( f \sim g,{f}^{\alpha } \sim {g}^{\alpha } \) for all \( \alpha \in \mathbb{R} \) ).
