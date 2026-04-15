#### 4.4. Transpose maps

*Français : 4.4. Applications transposées*

DéFINITION 5. Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v de dimension quelconque. Soit \( u \in \mathcal{L}\left( {E, F}\right) \) . Pour tout \( f \in {F}^{ * } \) , on a \( f \circ u \in {E}^{ * } \) . L’application linéaire \( {F}^{ * } \rightarrow {E}^{ * }\;f \mapsto f \circ u \) est appelée application transposée de \( u \) et notée \( {}^{\mathrm{t}}u \) .

> DEFINITION 5. Let \( E \) and \( F \) be two \( \mathbb{K} \) -vector spaces of any dimension. Let \( u \in \mathcal{L}\left( {E, F}\right) \) . For all \( f \in {F}^{ * } \) , we have \( f \circ u \in {E}^{ * } \) . The linear map \( {F}^{ * } \rightarrow {E}^{ * }\;f \mapsto f \circ u \) is called the transpose map of \( u \) and is denoted by \( {}^{\mathrm{t}}u \) .

Proposition 6. Soient \( E \) et \( F \) deux \( \mathbb{K} \) -e.v. Si \( E \) et \( F \) sont de dimension finie, on a

> Proposition 6. Let \( E \) and \( F \) be two \( \mathbb{K} \) -vector spaces. If \( E \) and \( F \) are finite-dimensional, we have

\[
\text{ (i) }\operatorname{rg}u = \operatorname{rg}\left( {{}^{\mathrm{t}}u}\right) \;\text{ (ii) }\;\operatorname{Im}\left( {{}^{\mathrm{t}}u}\right)  = {\left( \operatorname{Ker}u\right) }^{ \bot  }\text{ , }
\]

et en dimension quelconque

> and in any dimension

\[
\text{ (iii) }\operatorname{Ker}\left( {{}^{\mathrm{t}}u}\right)  = {\left( \operatorname{Im}u\right) }^{ \bot  }\text{ . }
\]

Démonstration. (i) est démontré dans l'étude des problèmes matriciels (voir partie 4.5 page 136).

> Proof. (i) is proven in the study of matrix problems (see section 4.5 page 136).

(ii) Soit \( g \in \operatorname{Im}\left( {{}^{\mathrm{t}}u}\right) \) . Il existe \( f \in {F}^{ * } \) tel que \( g = f \circ u \) , donc pour tout \( x \in \operatorname{Ker}u, g\left( x\right) = 0 \) , et donc \( g \in {\left( \operatorname{Ker}u\right) }^{ \bot } \) . On vient donc de montrer que \( \operatorname{Im}\left( {{}^{\mathrm{t}}u}\right) \subset {\left( \operatorname{Ker}u\right) }^{ \bot } \) . Or \( \dim \left( {{\operatorname{Im}}^{\mathrm{t}}u}\right) = {\operatorname{rg}}^{\mathrm{t}}u = \; \operatorname{rg}u = \dim E - \dim \left( {\operatorname{Ker}u}\right) = \dim {\left( \operatorname{Ker}u\right) }^{ \bot } \) , d’où (ii).

> (ii) Let \( g \in \operatorname{Im}\left( {{}^{\mathrm{t}}u}\right) \) . There exists \( f \in {F}^{ * } \) such that \( g = f \circ u \) , so for all \( x \in \operatorname{Ker}u, g\left( x\right) = 0 \) , and thus \( g \in {\left( \operatorname{Ker}u\right) }^{ \bot } \) . We have just shown that \( \operatorname{Im}\left( {{}^{\mathrm{t}}u}\right) \subset {\left( \operatorname{Ker}u\right) }^{ \bot } \) . However \( \dim \left( {{\operatorname{Im}}^{\mathrm{t}}u}\right) = {\operatorname{rg}}^{\mathrm{t}}u = \; \operatorname{rg}u = \dim E - \dim \left( {\operatorname{Ker}u}\right) = \dim {\left( \operatorname{Ker}u\right) }^{ \bot } \) , hence (ii).

(iii) Il suffit de remarquer que

> (iii) It suffices to note that

\[
\varphi  \in  {\operatorname{Ker}}^{\mathrm{t}}u \Leftrightarrow  \varphi  \circ  u = 0 \Leftrightarrow  \operatorname{Im}u \subset  \operatorname{Ker}\varphi  \Leftrightarrow  \varphi  \in  {\left( \operatorname{Im}u\right) }^{ \bot  }.
\]

Proposition 7. Soient \( E, F, G \) trois \( \mathbb{K} \) -e.v, \( u \in \mathcal{L}\left( {E, F}\right) \) et \( v \in \mathcal{L}\left( {F, G}\right) \) . Alors \( {}^{\mathrm{t}}\left( {v \circ u}\right) = \; {}^{\mathrm{t}}u \circ {}^{\mathrm{t}}v \) .

> Proposition 7. Let \( E, F, G \) be three \( \mathbb{K} \) -vector spaces, \( u \in \mathcal{L}\left( {E, F}\right) \) and \( v \in \mathcal{L}\left( {F, G}\right) \) . Then \( {}^{\mathrm{t}}\left( {v \circ u}\right) = \; {}^{\mathrm{t}}u \circ {}^{\mathrm{t}}v \) .

Démonstration. Il suffit d’écrire que si \( g \in {G}^{ * }, g \circ \left( {v \circ u}\right) = \left( {g \circ v}\right) \circ u = {}^{\mathrm{t}}u\left( {g \circ v}\right) = {}^{\mathrm{t}}u \circ \left\lbrack {{}^{\mathrm{t}}v\left( g\right) }\right\rbrack \) .

> Proof. It suffices to write that if \( g \in {G}^{ * }, g \circ \left( {v \circ u}\right) = \left( {g \circ v}\right) \circ u = {}^{\mathrm{t}}u\left( {g \circ v}\right) = {}^{\mathrm{t}}u \circ \left\lbrack {{}^{\mathrm{t}}v\left( g\right) }\right\rbrack \) .

Proposition 8. Supposons \( E \) de dimension finie. Soit \( u \in \mathcal{L}\left( E\right) \) . Un s.e.v \( F \) de \( E \) est stable par \( u \) si et seulement si \( {F}^{ \bot } \) est stable par \( {}^{t}u \) .

> Proposition 8. Suppose \( E \) is finite-dimensional. Let \( u \in \mathcal{L}\left( E\right) \) . A subspace \( F \) of \( E \) is invariant under \( u \) if and only if \( {F}^{ \bot } \) is invariant under \( {}^{t}u \) .

Démonstration. Condition nécessaire. On a \( u\left( F\right) \subset F \) donc pour tout \( \varphi \in {F}^{ \bot } \) , comme \( \varphi \left( F\right) = \; \{ 0\} \) on a \( \varphi \circ u\left( F\right) = \{ 0\} \) . Autrement dit, si \( \varphi \in {F}^{ \bot } \) on a \( {}^{t}u\left( \varphi \right) \in {F}^{ \bot } \) . Finalement, \( {F}^{ \bot } \) est stable par \( {}^{t}u \) .

> Proof. Necessary condition. We have \( u\left( F\right) \subset F \) so for all \( \varphi \in {F}^{ \bot } \) , since \( \varphi \left( F\right) = \; \{ 0\} \) we have \( \varphi \circ u\left( F\right) = \{ 0\} \) . In other words, if \( \varphi \in {F}^{ \bot } \) we have \( {}^{t}u\left( \varphi \right) \in {F}^{ \bot } \) . Finally, \( {F}^{ \bot } \) is stable under \( {}^{t}u \) .

Condition suffisante. D’après le corollaire 1, il existe \( r \) formes linéaires \( {\varphi }_{1},\ldots ,{\varphi }_{r} \) telles que \( F = \; { \cap }_{i = 1}^{r}\operatorname{Ker}{\varphi }_{i} \) . En particulier, pour tout \( i, F \subset \operatorname{Ker}{\varphi }_{i} \) c’est-à-dire que \( {\varphi }_{i} \in {F}^{ \bot } \) . Maintenant, comme \( {F}^{ \bot } \) est stable par \( {}^{t}u \) , on a \( {}^{t}u\left( {\varphi }_{i}\right) = {\varphi }_{i} \circ u \in {F}^{ \bot } \) pour tout \( i \) , donc \( {\varphi }_{i} \circ u\left( F\right) = {\varphi }_{i}\left\lbrack {u\left( F\right) }\right\rbrack = \{ 0\} \) . Autrement dit, pour tout \( i, u\left( F\right) \subset \operatorname{Ker}{\varphi }_{i} \) et donc \( u\left( F\right) \subset { \cap }_{i = 1}^{r}\operatorname{Ker}{\varphi }_{i} = F \) , d’où la condition suffisante.

> Sufficient condition. According to corollary 1, there exist \( r \) linear forms \( {\varphi }_{1},\ldots ,{\varphi }_{r} \) such that \( F = \; { \cap }_{i = 1}^{r}\operatorname{Ker}{\varphi }_{i} \) . In particular, for all \( i, F \subset \operatorname{Ker}{\varphi }_{i} \) that is to say \( {\varphi }_{i} \in {F}^{ \bot } \) . Now, since \( {F}^{ \bot } \) is stable under \( {}^{t}u \) , we have \( {}^{t}u\left( {\varphi }_{i}\right) = {\varphi }_{i} \circ u \in {F}^{ \bot } \) for all \( i \) , therefore \( {\varphi }_{i} \circ u\left( F\right) = {\varphi }_{i}\left\lbrack {u\left( F\right) }\right\rbrack = \{ 0\} \) . In other words, for all \( i, u\left( F\right) \subset \operatorname{Ker}{\varphi }_{i} \) and thus \( u\left( F\right) \subset { \cap }_{i = 1}^{r}\operatorname{Ker}{\varphi }_{i} = F \) , hence the sufficient condition.

\( \rightarrow \) Remarque 8.

> \( \rightarrow \) Remark 8.

- Ce résultat reste vrai en dimension infinie mais sa démonstration fait appel à l'axiome du choix.

> - This result remains true in infinite dimension but its proof requires the axiom of choice.

- Cette proposition peut être très utile dans certains raisonnements par récurrence en dimension finie \( n \) relatifs aux réductions d’endomorphismes. En effet, si \( x \in  {E}^{ * } \) est un vecteur propre de \( {}^{t}u \) , alors \( \mathbb{K}x \) est stable par \( {}^{t}u \) et donc \( {\left( \mathbb{K}x\right) }^{ \circ  } \) , hyperplan de \( E \) , est stable par \( u \) (appliquer la proposition à \( F = {\left( \mathbb{K}x\right) }^{ \circ  } \) ). Le tour est joué, on est ramené en dimension \( n - 1 \) (on trouve des raisonnements de ce type dans la démonstration du théorème de trigonalisation par exemple).

> - This proposition can be very useful in certain reasoning by induction in finite dimension \( n \) related to endomorphism reductions. Indeed, if \( x \in  {E}^{ * } \) is an eigenvector of \( {}^{t}u \) , then \( \mathbb{K}x \) is stable under \( {}^{t}u \) and thus \( {\left( \mathbb{K}x\right) }^{ \circ  } \) , a hyperplane of \( E \) , is stable under \( u \) (apply the proposition to \( F = {\left( \mathbb{K}x\right) }^{ \circ  } \) ). The trick is done, we are brought back to dimension \( n - 1 \) (we find reasoning of this type in the proof of the triangularization theorem for example).
