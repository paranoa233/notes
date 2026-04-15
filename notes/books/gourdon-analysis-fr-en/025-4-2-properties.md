#### 4.2. Properties

*Français : 4.2. Propriétés*

THÉORÉME 1. Soit \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) une application continue. Si E est connexe, alors \( f\left( E\right) \) est connexe.

> THEOREM 1. Let \( f : \left( {E,\mathrm{\;d}}\right) \rightarrow \left( {{E}^{\prime },{\mathrm{d}}^{\prime }}\right) \) be a continuous map. If E is connected, then \( f\left( E\right) \) is connected.

Démonstration. Soit \( B \) une partie ouverte et fermée de \( f\left( E\right) \) . Il existe un ouvert \( O \) et un fermé \( F \) de \( {E}^{\prime } \) tels que \( B = O \cap f\left( E\right) = F \cap f\left( E\right) \) . On a alors \( {f}^{-1}\left( B\right) = {f}^{-1}\left( O\right) = {f}^{-1}\left( F\right) \) , donc \( {f}^{-1}\left( B\right) \) est fermé et ouvert dans \( E \) , et \( E \) étant connexe, \( {f}^{-1}\left( B\right) = \varnothing \) ou \( {f}^{-1}\left( B\right) = E \) , c’est-à-dire \( B = \varnothing \) ou \( B = f\left( E\right) \) .

> Proof. Let \( B \) be an open and closed subset of \( f\left( E\right) \) . There exists an open set \( O \) and a closed set \( F \) of \( {E}^{\prime } \) such that \( B = O \cap f\left( E\right) = F \cap f\left( E\right) \) . We then have \( {f}^{-1}\left( B\right) = {f}^{-1}\left( O\right) = {f}^{-1}\left( F\right) \) , so \( {f}^{-1}\left( B\right) \) is closed and open in \( E \) , and since \( E \) is connected, \( {f}^{-1}\left( B\right) = \varnothing \) or \( {f}^{-1}\left( B\right) = E \) , that is to say \( B = \varnothing \) or \( B = f\left( E\right) \) .

Caractérisation des connexes. On note \( D = \{ 0,1\} \) muni de la distance discrète \( \delta \; \left( {\delta \left( {0,0}\right) = \delta \left( {1,1}\right) = 0\text{ et }\delta \left( {0,1}\right) = \delta \left( {1,0}\right) = 1}\right) \) . L’espace métrique \( \left( {D,\delta }\right) \) n’est pas connexe puisque \( D = \{ 0\} \cup \{ 1\} \) est réunion de deux fermés disjoints. Grâce à cet espace métrique, nous allons donner une caractérisation commode des connexes.

> Characterization of connected sets. Let \( D = \{ 0,1\} \) be equipped with the discrete metric \( \delta \; \left( {\delta \left( {0,0}\right) = \delta \left( {1,1}\right) = 0\text{ et }\delta \left( {0,1}\right) = \delta \left( {1,0}\right) = 1}\right) \) . The metric space \( \left( {D,\delta }\right) \) is not connected since \( D = \{ 0\} \cup \{ 1\} \) is the union of two disjoint closed sets. Using this metric space, we will provide a convenient characterization of connected sets.

\( \rightarrow \) PROPOSITION 3. Un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est connexe si et seulement si toute application continue \( f : E \rightarrow D \) est constante.

> \( \rightarrow \) PROPOSITION 3. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is connected if and only if every continuous map \( f : E \rightarrow D \) is constant.

Démonstration. Condition nécessaire. Si E est connexe, alors \( f\left( E\right) \) est connexe, donc constante car \( D \) n’est pas connexe et a deux éléments.

> Proof. Necessary condition. If E is connected, then \( f\left( E\right) \) is connected, and therefore constant because \( D \) is not connected and has two elements.

Condition suffisante. Si \( E \) n’est pas connexe, on peut écrire \( E = {O}_{1} \cup {O}_{2} \) où \( {O}_{1} \) et \( {O}_{2} \) sont deux ouverts non vides disjoints de \( E \) . Soit \( f : E \rightarrow D \) une application définie par \( f\left( x\right) = 0 \) si \( x \in {O}_{1} \) , \( f\left( x\right) = 1 \) si \( x \in {O}_{2} \) . Elle est continue (l’image réciproque de tout ouvert est un ouvert), ce qui est contraire aux hypothèses puisqu'elle est non constante. Finalement, \( E \) est connexe.

> Sufficient condition. If \( E \) is not connected, we can write \( E = {O}_{1} \cup {O}_{2} \) where \( {O}_{1} \) and \( {O}_{2} \) are two non-empty disjoint open sets of \( E \) . Let \( f : E \rightarrow D \) be a map defined by \( f\left( x\right) = 0 \) if \( x \in {O}_{1} \) , \( f\left( x\right) = 1 \) if \( x \in {O}_{2} \) . It is continuous (the preimage of any open set is an open set), which contradicts the hypotheses since it is non-constant. Finally, \( E \) is connected.

Proposition 4. Soit A une partie connexe d'un espace métrique (E, d). Si une partie B de \( E \) vérifie \( A \subset B \subset \bar{A} \) , alors \( B \) est connexe.

> Proposition 4. Let A be a connected subset of a metric space (E, d). If a subset B of \( E \) satisfies \( A \subset B \subset \bar{A} \) , then \( B \) is connected.

Démonstration. Soit \( f : B \rightarrow D = \{ 0,1\} \) une application continue. Comme \( A \) est connexe, \( {f}_{\mid A} \) est constante, par exemple \( {f}_{\mid A} = 0 \) . Soit \( {x}_{0} \in B \) . Il existe un voisinage \( V \) de \( {x}_{0} \) dans \( B \) tel que

> Proof. Let \( f : B \rightarrow D = \{ 0,1\} \) be a continuous map. Since \( A \) is connected, \( {f}_{\mid A} \) is constant, for example \( {f}_{\mid A} = 0 \) . Let \( {x}_{0} \in B \) . There exists a neighborhood \( V \) of \( {x}_{0} \) in \( B \) such that

\[
\forall x \in  V,\;\delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  < \frac{1}{2},
\]

ce qui montre que pour tout \( x \in V, f\left( x\right) = f\left( {x}_{0}\right) \) . Or \( B \subset \bar{A} \) , donc \( V \cap A \neq \varnothing \) . Si on choisit \( {x}_{1} \in V \cap A \) , on a \( f\left( {x}_{0}\right) = f\left( {x}_{1}\right) = 0 \) . Ainsi, \( f = 0 \) , d’où le résultat d’après la proposition 3 .

> which shows that for all \( x \in V, f\left( x\right) = f\left( {x}_{0}\right) \) . However \( B \subset \bar{A} \) , so \( V \cap A \neq \varnothing \) . If we choose \( {x}_{1} \in V \cap A \) , we have \( f\left( {x}_{0}\right) = f\left( {x}_{1}\right) = 0 \) . Thus, \( f = 0 \) , hence the result according to proposition 3 .

Dans le cas général, une réunion de connexes n'est pas connexe (par exemple, \{0\} et \{1\} sont connexes dans \( \mathbb{R} \) , mais \( \{ 0,1\} = \{ 0\} \cup \{ 1\} \) n’est pas connexe). On a cependant le résultat qui suit.

> In the general case, a union of connected sets is not connected (for example, \{0\} and \{1\} are connected in \( \mathbb{R} \) , but \( \{ 0,1\} = \{ 0\} \cup \{ 1\} \) is not connected). We do, however, have the following result.

Proposition 5. Soit \( {\left( {C}_{i}\right) }_{i \in I} \) une famille de connexes d’un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) telle que

> Proposition 5. Let \( {\left( {C}_{i}\right) }_{i \in I} \) be a family of connected sets of a metric space \( \left( {E,\mathrm{\;d}}\right) \) such that

\[
\exists {i}_{0} \in  I,\forall i \in  I,\;{C}_{i} \cap  {C}_{{i}_{0}} \neq  \varnothing .
\]

Alors \( { \cup }_{i \in I}{C}_{i} \) est connexe.

> Then \( { \cup }_{i \in I}{C}_{i} \) is connected.

Démonstration. Soit \( f : { \cup }_{i \in I}{C}_{i} \rightarrow D = \{ 0,1\} \) une application continue. Pour tout \( i,{C}_{i} \) est connexe donc \( {f}_{\mid {C}_{i}} \) est constante. En particulier, \( {f}_{\mid {C}_{{i}_{0}}} \) est connexe, par exemple \( {f}_{\mid {C}_{{i}_{0}}} = 0 \) . Soit \( x \in { \cup }_{i \in I}{C}_{i} \) et soit \( i \in I \) tel que \( x \in {C}_{i} \) . Comme \( {C}_{i} \cap {C}_{{i}_{0}} \neq \varnothing \) , on peut trouver \( {x}_{0} \in {C}_{i} \cap {C}_{{i}_{0}} \) . On a alors \( f\left( x\right) = f\left( {x}_{0}\right) = 0 \) car \( {f}_{\mid {C}_{i}} \) est constante. Ainsi, \( f \) est constante sur \( { \cup }_{i \in I}{C}_{i} \) , d’où le résultat d'après la proposition 3.

> Proof. Let \( f : { \cup }_{i \in I}{C}_{i} \rightarrow D = \{ 0,1\} \) be a continuous map. For any \( i,{C}_{i} \) is connected, therefore \( {f}_{\mid {C}_{i}} \) is constant. In particular, \( {f}_{\mid {C}_{{i}_{0}}} \) is connected, for example \( {f}_{\mid {C}_{{i}_{0}}} = 0 \) . Let \( x \in { \cup }_{i \in I}{C}_{i} \) and let \( i \in I \) such that \( x \in {C}_{i} \) . Since \( {C}_{i} \cap {C}_{{i}_{0}} \neq \varnothing \) , we can find \( {x}_{0} \in {C}_{i} \cap {C}_{{i}_{0}} \) . We then have \( f\left( x\right) = f\left( {x}_{0}\right) = 0 \) because \( {f}_{\mid {C}_{i}} \) is constant. Thus, \( f \) is constant on \( { \cup }_{i \in I}{C}_{i} \) , hence the result according to proposition 3.

Remarque 2. Si \( {\left( {C}_{i}\right) }_{i \in I} \) est une famille de connexes telle que \( { \cap }_{i \in I}{C}_{i} \neq \varnothing \) , alors \( { \cup }_{i \in I}{C}_{i} \) est connexe (si \( x \in { \cap }_{i \in I}{C}_{i} \) , tous ces connexes ont une intersection non vide avec le connexe \( \{ x\} ) \) .

> Remark 2. If \( {\left( {C}_{i}\right) }_{i \in I} \) is a family of connected sets such that \( { \cap }_{i \in I}{C}_{i} \neq \varnothing \) , then \( { \cup }_{i \in I}{C}_{i} \) is connected (if \( x \in { \cap }_{i \in I}{C}_{i} \) , all these connected sets have a non-empty intersection with the connected set \( \{ x\} ) \) .

Dans le cas dénombrable, on a également le résultat qui suit.

> In the countable case, we also have the following result.

Proposition 6. Soit \( {\left( {C}_{i}\right) }_{i \in I} \) une famille au plus dénombrable de connexes (avec \( I = \; \{ 0,1,\ldots , p\} \) ou \( I = \mathbb{N}) \) telle que pour tout \( i \in I, i \neq 0,{C}_{i - 1} \cap {C}_{i} \neq \varnothing \) . Alors \( { \cup }_{i \in I}{C}_{i} \) est connexe.

> Proposition 6. Let \( {\left( {C}_{i}\right) }_{i \in I} \) be an at most countable family of connected sets (with \( I = \; \{ 0,1,\ldots , p\} \) or \( I = \mathbb{N}) \) such that for all \( i \in I, i \neq 0,{C}_{i - 1} \cap {C}_{i} \neq \varnothing \) . Then \( { \cup }_{i \in I}{C}_{i} \) is connected.

Démonstration. Soit \( f : { \cup }_{i \in I}{C}_{i} \rightarrow D = \{ 0,1\} \) une application continue. Pour tout \( i,{f}_{\mid {C}_{i}} \) est constante, et comme \( {C}_{i - 1} \cap {C}_{i} \neq \varnothing \) pour \( i \neq 0 \) , on a \( {f}_{\mid {C}_{i - 1}} = {f}_{\mid {C}_{i}} \) pour tout \( i \neq 0 \) . En procédant par récurrence sur \( i \) , on en déduit que \( {f}_{\mid {C}_{i}} = {f}_{\mid {C}_{0}} \) pour tout \( i \) . Ainsi, \( f \) est constante, d’où le résultat.

> Proof. Let \( f : { \cup }_{i \in I}{C}_{i} \rightarrow D = \{ 0,1\} \) be a continuous map. For all \( i,{f}_{\mid {C}_{i}} \) is constant, and since \( {C}_{i - 1} \cap {C}_{i} \neq \varnothing \) for \( i \neq 0 \) , we have \( {f}_{\mid {C}_{i - 1}} = {f}_{\mid {C}_{i}} \) for all \( i \neq 0 \) . By proceeding by induction on \( i \) , we deduce that \( {f}_{\mid {C}_{i}} = {f}_{\mid {C}_{0}} \) for all \( i \) . Thus, \( f \) is constant, hence the result.

Proposition 7. Soient \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) des espaces métriques (en nombre fini). L’espace produit \( E = {E}_{1} \times \cdots \times {E}_{n} \) est connexe si et seulement si \( {E}_{i} \) est connexe pour tout \( i \) .

> Proposition 7. Let \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) be metric spaces (in finite number). The product space \( E = {E}_{1} \times \cdots \times {E}_{n} \) is connected if and only if \( {E}_{i} \) is connected for all \( i \) .

Démonstration. Condition nécessaire. Soit \( i \in \{ 1,\ldots , n\} \) et soit \( f : {E}_{i} \rightarrow D = \{ 0,1\} \) une application continue. La projection \( {p}_{i} \) de \( E \) sur \( {E}_{i} \) étant continue,1’application \( f \circ {p}_{i} : E \rightarrow D \) est continue, et comme \( E \) est connexe, \( f \circ {p}_{i} \) est constante. Donc \( f \) est constante et \( {E}_{i} \) est connexe.

> Proof. Necessary condition. Let \( i \in \{ 1,\ldots , n\} \) and let \( f : {E}_{i} \rightarrow D = \{ 0,1\} \) be a continuous map. Since the projection \( {p}_{i} \) of \( E \) onto \( {E}_{i} \) is continuous, the map \( f \circ {p}_{i} : E \rightarrow D \) is continuous, and since \( E \) is connected, \( f \circ {p}_{i} \) is constant. Thus \( f \) is constant and \( {E}_{i} \) is connected.

Condition suffisante. Soient \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) et \( \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in E \) et une application continue \( f : E \rightarrow \; D \) . L’application \( {f}_{1} : {E}_{1} \rightarrow D\;x \mapsto f\left( {x,{x}_{2},\ldots ,{x}_{n}}\right) \) est continue, donc constante car \( {E}_{1} \) est connexe. En particulier, \( f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{n}}\right) = f\left( {{y}_{1},{x}_{2},\ldots ,{x}_{n}}\right) \) . En itérant le procédé sur chacun des connexes \( {E}_{2},\ldots ,{E}_{n} \) , on obtient \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = f\left( {{y}_{1},\ldots ,{y}_{n}}\right) \) . L’application \( f \) est donc constante, donc \( E \) est connexe d’après la proposition 3.

> Sufficient condition. Let \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) and \( \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in E \) and a continuous map \( f : E \rightarrow \; D \). The map \( {f}_{1} : {E}_{1} \rightarrow D\;x \mapsto f\left( {x,{x}_{2},\ldots ,{x}_{n}}\right) \) is continuous, hence constant because \( {E}_{1} \) is connected. In particular, \( f\left( {{x}_{1},{x}_{2},\ldots ,{x}_{n}}\right) = f\left( {{y}_{1},{x}_{2},\ldots ,{x}_{n}}\right) \). By iterating the process on each connected component \( {E}_{2},\ldots ,{E}_{n} \), we obtain \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = f\left( {{y}_{1},\ldots ,{y}_{n}}\right) \). The map \( f \) is therefore constant, so \( E \) is connected according to proposition 3.

Composantes connexes. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. On considère sur \( \left( {E,\mathrm{\;d}}\right) \) la relation

> Connected components. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. We consider on \( \left( {E,\mathrm{\;d}}\right) \) the relation

\[
\left( {x\mathcal{R}y}\right)  \Leftrightarrow  \left( {\exists C\text{ connexe de }E\text{ tel que }x \in  C\text{ et }y \in  C}\right) .
\]

On a affaire à une relation d'équivalence car

> This is an equivalence relation because

- Si \( x\mathcal{R}y, y\mathcal{R}x \) (immédiat).

> - If \( x\mathcal{R}y, y\mathcal{R}x \) (immediate).

- Pour tout \( x, x\mathcal{R}x\operatorname{car}\{ x\} \) est un connexe.

> - For any \( x, x\mathcal{R}x\operatorname{car}\{ x\} \) is a connected set.

- Si \( x\mathcal{R}y \) et \( y\mathcal{R}z \) , il existe deux connexes \( C \) et \( {C}^{\prime } \) tels que \( x \in  C, y \in  C \) et \( y \in  {C}^{\prime } \) , \( z \in  {C}^{\prime } \) . On a \( C \cap  {C}^{\prime } \neq  \varnothing \) donc d’après la remarque \( 2, C \cup  {C}^{\prime } \) est connexe, et comme \( x \in  C \cup  {C}^{\prime } \) et \( z \in  C \cup  {C}^{\prime }, x\mathcal{R}z \) .

> - If \( x\mathcal{R}y \) and \( y\mathcal{R}z \), there exist two connected sets \( C \) and \( {C}^{\prime } \) such that \( x \in  C, y \in  C \) and \( y \in  {C}^{\prime } \), \( z \in  {C}^{\prime } \). We have \( C \cap  {C}^{\prime } \neq  \varnothing \) so according to remark \( 2, C \cup  {C}^{\prime } \) is connected, and since \( x \in  C \cup  {C}^{\prime } \) and \( z \in  C \cup  {C}^{\prime }, x\mathcal{R}z \).

Si \( x \in E \) , sa classe d’équivalence, notée \( \dot{x} \) , est la réunion des connexes contenant \( x \) . C’est donc un connexe d’après la proposition 5 (en effet, tous les connexes contenant \( x \) ont tous une intersection non vide avec le connexe \( \{ x\} \) ). L’ensemble \( \dot{x} \) s’appelle une composante connexe de \( E \) .

> If \( x \in E \), its equivalence class, denoted \( \dot{x} \), is the union of the connected sets containing \( x \). It is therefore a connected set according to proposition 5 (indeed, all connected sets containing \( x \) all have a non-empty intersection with the connected set \( \{ x\} \)). The set \( \dot{x} \) is called a connected component of \( E \).

Les composantes connexes de \( E \) forment donc une partition de \( E \) . L’espace métrique \( E \) est connexe si et seulement s’il n’a qu’une seule composante connexe.

> The connected components of \( E \) therefore form a partition of \( E \). The metric space \( E \) is connected if and only if it has only one connected component.

Les composantes connexes de \( E \) sont des fermés de \( E \) . Considérons en effet une com-posante connexe \( \dot{x} \) de \( E \) . La proposition 4 entraîne le fait que \( \overline{\dot{x}} \) est connexe, c’est donc un connexe contenant \( x \) , donc \( \dot{x} \subset \overline{\dot{x}} \) et \( \dot{x} = \overline{\dot{x}} \) .

> The connected components of \( E \) are closed sets in \( E \) . Indeed, consider a connected component \( \dot{x} \) of \( E \) . Proposition 4 implies that \( \overline{\dot{x}} \) is connected, so it is a connected set containing \( x \) , thus \( \dot{x} \subset \overline{\dot{x}} \) and \( \dot{x} = \overline{\dot{x}} \) .

Si les composantes connexes de \( E \) sont en nombre fini, elles sont ouvertes comme complémentaires d’une réunion finie de fermés de \( E \) .

> If the connected components of \( E \) are finite in number, they are open as the complement of a finite union of closed sets in \( E \) .

##### Connected subsets of \( \mathbb{R} \) .

*Français : Connexes de \( \mathbb{R} \) .*

\( \rightarrow \) THÉORÈME 2. Les parties connexes de \( \mathbb{R} \) sont les intervalles de \( \mathbb{R} \) .

> \( \rightarrow \) THEOREM 2. The connected subsets of \( \mathbb{R} \) are the intervals of \( \mathbb{R} \) .

Démonstration. Un connexe de \( \mathbb{R} \) est un intervalle. En effet, si \( C \subset \mathbb{R} \) n’est pas un intervalle, il existe \( \left( {a, b}\right) \in {C}^{2} \) et \( x \in \mathbb{R} \) tels que \( a < x < b \) et \( x \notin C \) . Mais alors \( C \subset \rbrack - \infty , x\left\lbrack \cup \right\rbrack x, + \infty \lbrack \) , donc \( C \) n’est pas connexe.

> Proof. A connected subset of \( \mathbb{R} \) is an interval. Indeed, if \( C \subset \mathbb{R} \) is not an interval, there exist \( \left( {a, b}\right) \in {C}^{2} \) and \( x \in \mathbb{R} \) such that \( a < x < b \) and \( x \notin C \) . But then \( C \subset \rbrack - \infty , x\left\lbrack \cup \right\rbrack x, + \infty \lbrack \) , so \( C \) is not connected.

Réciproquement, montrons qu’un intervalle \( I \) de \( \mathbb{R} \) est connexe. C’est un peu plus délicat.

> Conversely, let us show that an interval \( I \) of \( \mathbb{R} \) is connected. This is slightly more delicate.

Si \( I \) est un singleton, c’est immédiat.

> If \( I \) is a singleton, it is immediate.

Si \( I = \rbrack a, b\left\lbrack \right. \) avec \( - \infty \leq a < b \leq + \infty \) , considérons une application continue \( f : I \rightarrow D = \; \{ 0,1\} \) . Si \( f \) n’est pas constante, il existe \( x, y \in I \) vérifiant \( a < x < y < b \) tels que \( f\left( x\right) \neq f\left( y\right) \) , par exemple \( f\left( x\right) = 0 \) et \( f\left( y\right) = 1 \) . Considérons l’ensemble

> If \( I = \rbrack a, b\left\lbrack \right. \) with \( - \infty \leq a < b \leq + \infty \) , consider a continuous map \( f : I \rightarrow D = \; \{ 0,1\} \) . If \( f \) is not constant, there exist \( x, y \in I \) satisfying \( a < x < y < b \) such that \( f\left( x\right) \neq f\left( y\right) \) , for example \( f\left( x\right) = 0 \) and \( f\left( y\right) = 1 \) . Consider the set

\[
\Gamma  = \{ z \in  I \mid  z \geq  x\text{ et }\forall t \in  \left\lbrack  {x, z}\right\rbrack  , f\left( t\right)  = 0\} .
\]

L’ensemble \( \Gamma \) est non vide car \( x \in \Gamma \) . De plus, \( \Gamma \) est majoré car pour tout \( z \in \Gamma , z \leq y \) . Soit \( c = \sup \Gamma \) . Comme \( f \) est continue, \( f\left( c\right) = 0 \) . De même, \( f \) étant continue en \( c \) ,

> The set \( \Gamma \) is non-empty because \( x \in \Gamma \) . Moreover, \( \Gamma \) is bounded above because for all \( z \in \Gamma , z \leq y \) . Let \( c = \sup \Gamma \) . Since \( f \) is continuous, \( f\left( c\right) = 0 \) . Similarly, since \( f \) is continuous at \( c \) ,

\[
\exists \varepsilon  > 0,\forall t \in  \left\lbrack  {c, c + \varepsilon }\right\rbrack  ,\;\delta \left( {f\left( t\right) , f\left( c\right) }\right)  < \frac{1}{2},
\]

donc pour tout \( t \in \left\lbrack {c, c + \varepsilon }\right\rbrack , f\left( t\right) = 0 \) , ce qui montre que \( c + \varepsilon \in \Gamma \) . Ceci contredit le fait que \( c = \sup \Gamma \) . Finalement, l’application \( f \) est constante et \( I \) est connexe d’après la proposition 3 .

> therefore for all \( t \in \left\lbrack {c, c + \varepsilon }\right\rbrack , f\left( t\right) = 0 \) , which shows that \( c + \varepsilon \in \Gamma \) . This contradicts the fact that \( c = \sup \Gamma \) . Finally, the map \( f \) is constant and \( I \) is connected according to proposition 3 .

Tout intervalle \( I \) de \( \mathbb{R} \) non réduit à un singleton étant compris entre un intervalle ouvert et son adhérence, on en conclut avec la proposition 4 que tout intervalle de \( \mathbb{R} \) est connexe.

> Since any interval \( I \) of \( \mathbb{R} \) not reduced to a singleton is contained between an open interval and its closure, we conclude with proposition 4 that every interval of \( \mathbb{R} \) is connected.

\( \rightarrow \) THéORÉME 3 (DES VALEURS INTERMÉDIAIRES). Soit I un intervalle de \( \mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application continue. Alors \( f\left( I\right) \) est un intervalle.

> \( \rightarrow \) THEOREM 3 (INTERMEDIATE VALUE THEOREM). Let I be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a continuous map. Then \( f\left( I\right) \) is an interval.

Démonstration. Le théorème précédent assure la connexité de \( I \) , donc \( f\left( I\right) \) est connexe d’après le théorème 1, c'est donc un intervalle.

> Proof. The previous theorem ensures the connectedness of \( I \), so \( f\left( I\right) \) is connected according to theorem 1, and is therefore an interval.

Remarque 3. - Une autre manière d'écrire le résultat est la suivante. Si \( f\left( a\right) \leq f\left( b\right) \) (resp. \( f\left( b\right) \geq f\left( a\right) \) ) avec \( a < b \) , alors pour tout \( \gamma \) tel que \( f\left( a\right) \leq \gamma \leq f\left( b\right) \) (resp. \( f\left( b\right) \leq \gamma \leq f\left( a\right) ) \) , il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( f\left( c\right) = \gamma \) .

> Remark 3. - Another way to write the result is as follows. If \( f\left( a\right) \leq f\left( b\right) \) (resp. \( f\left( b\right) \geq f\left( a\right) \)) with \( a < b \), then for any \( \gamma \) such that \( f\left( a\right) \leq \gamma \leq f\left( b\right) \) (resp. \( f\left( b\right) \leq \gamma \leq f\left( a\right) ) \), there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( f\left( c\right) = \gamma \).

- Avec la proposition 15, on en conclut que l’image d’un segment de \( \mathbb{R} \) par \( f \) est un segment de \( \mathbb{R} \) .

> - With proposition 15, we conclude that the image of a segment of \( \mathbb{R} \) by \( f \) is a segment of \( \mathbb{R} \).
