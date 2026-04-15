### 6. Problems

*Français : 6. Problèmes*

Problem 1. Soient \( E \) et \( F \) deux espaces métriques, \( K \) un espace métrique compact. Soit \( f : E \times K \rightarrow F\;\left( {\lambda , x}\right) \mapsto f\left( {\lambda , x}\right) \) une application continue. Pour tout \( y \in F \) , on note \( {E}_{y} = \{ \lambda \in E \mid \exists x \in K, f\left( {\lambda , x}\right) = y\} \) .

> Problem 1. Let \( E \) and \( F \) be two metric spaces, \( K \) a compact metric space. Let \( f : E \times K \rightarrow F\;\left( {\lambda , x}\right) \mapsto f\left( {\lambda , x}\right) \) be a continuous map. For any \( y \in F \) , we denote \( {E}_{y} = \{ \lambda \in E \mid \exists x \in K, f\left( {\lambda , x}\right) = y\} \) .

a) Montrer que \( {E}_{y} \) est un fermé de \( E \) .

> a) Show that \( {E}_{y} \) is a closed subset of \( E \) .

b) Fixons \( y \in E \) . On suppose que

> b) Let us fix \( y \in E \) . We assume that

\[
\forall \lambda  \in  {E}_{y},\exists !x \in  K,\;f\left( {\lambda , x}\right)  = y,
\]

et on note \( x = \varphi \left( \lambda \right) \) . Montrer que l’application \( \varphi : {E}_{y} \rightarrow K \) ainsi définie est continue.

> and we denote \( x = \varphi \left( \lambda \right) \) . Show that the map \( \varphi : {E}_{y} \rightarrow K \) thus defined is continuous.

Solution. a) L’ensemble \( {F}_{y} = {f}^{-1}\left( {\{ y\} }\right) \) est fermé par continuité de \( f \) , et on remarque que \( {E}_{y} = \left\{ {\lambda \in E\mid \exists x \in K,\left( {\lambda , x}\right) \in {F}_{y}}\right\} \) . Considérons une suite \( \left( {\lambda }_{n}\right) \) de \( {E}_{y} \) qui converge vers \( \lambda \in E \) . Il s’agit de montrer que \( \lambda \in {E}_{y} \) . Pour tout \( n \) , il existe \( {x}_{n} \in K \) tel que \( \left( {{\lambda }_{n},{x}_{n}}\right) \in {F}_{y} \) . Comme \( K \) est compact, on peut extraire de \( \left( {x}_{n}\right) \) une sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) qui converge vers un point \( x \in K \) . La suite \( \left( {{\lambda }_{\varphi \left( n\right) },{x}_{\varphi \left( n\right) }}\right) \) converge vers \( \left( {\lambda , x}\right) \) et comme \( {F}_{y} \) est fermé on en déduit \( \left( {\lambda , x}\right) \in {F}_{y} \) , donc \( \lambda \in {E}_{y} \) .

> Solution. a) The set \( {F}_{y} = {f}^{-1}\left( {\{ y\} }\right) \) is closed by continuity of \( f \) , and we note that \( {E}_{y} = \left\{ {\lambda \in E\mid \exists x \in K,\left( {\lambda , x}\right) \in {F}_{y}}\right\} \) . Consider a sequence \( \left( {\lambda }_{n}\right) \) in \( {E}_{y} \) that converges to \( \lambda \in E \) . We must show that \( \lambda \in {E}_{y} \) . For any \( n \) , there exists \( {x}_{n} \in K \) such that \( \left( {{\lambda }_{n},{x}_{n}}\right) \in {F}_{y} \) . Since \( K \) is compact, we can extract from \( \left( {x}_{n}\right) \) a subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) that converges to a point \( x \in K \) . The sequence \( \left( {{\lambda }_{\varphi \left( n\right) },{x}_{\varphi \left( n\right) }}\right) \) converges to \( \left( {\lambda , x}\right) \) and since \( {F}_{y} \) is closed we deduce \( \left( {\lambda , x}\right) \in {F}_{y} \) , thus \( \lambda \in {E}_{y} \) .

b) Soit \( \left( {\lambda }_{n}\right) \) une suite de \( {E}_{y} \) qui tend vers \( \lambda \in {E}_{y} \) . Il s’agit de montrer que la suite \( \left( {\varphi \left( {\lambda }_{n}\right) }\right) \) converge vers \( \varphi \left( \lambda \right) \) .

> b) Let \( \left( {\lambda }_{n}\right) \) be a sequence in \( {E}_{y} \) that tends to \( \lambda \in {E}_{y} \) . We must show that the sequence \( \left( {\varphi \left( {\lambda }_{n}\right) }\right) \) converges to \( \varphi \left( \lambda \right) \) .

Notons \( {x}_{n} = \varphi \left( {\lambda }_{n}\right) \) , et considérons une valeur d’adhérence \( a \in K \) de \( \left( {x}_{n}\right) \) , limite d’une sous-suite \( \left( {x}_{\psi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) . Par continuité de \( f, f\left( {\lambda , a}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {{\lambda }_{\psi \left( n\right) },{x}_{\psi \left( n\right) }}\right) = y \) donc \( a = \varphi \left( \lambda \right) \) . Ceci prouve que la seule valeur d’adhérence de \( \left( {x}_{n}\right) \) est \( \varphi \left( \lambda \right) \) . Comme \( \left( {x}_{n}\right) \) prend ses valeurs dans un compact, on en déduit que \( \left( {x}_{n}\right) \) converge vers \( \varphi \left( \lambda \right) \) (voir la proposition 9 page 30), c’est-à-dire \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\varphi \left( {\lambda }_{n}\right) = \varphi \left( \lambda \right) \) .

> Let \( {x}_{n} = \varphi \left( {\lambda }_{n}\right) \) be, and consider an accumulation point \( a \in K \) of \( \left( {x}_{n}\right) \) , the limit of a subsequence \( \left( {x}_{\psi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) . By continuity of \( f, f\left( {\lambda , a}\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {{\lambda }_{\psi \left( n\right) },{x}_{\psi \left( n\right) }}\right) = y \) , therefore \( a = \varphi \left( \lambda \right) \) . This proves that the only accumulation point of \( \left( {x}_{n}\right) \) is \( \varphi \left( \lambda \right) \) . Since \( \left( {x}_{n}\right) \) takes its values in a compact set, we deduce that \( \left( {x}_{n}\right) \) converges to \( \varphi \left( \lambda \right) \) (see proposition 9 on page 30), that is to say \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\varphi \left( {\lambda }_{n}\right) = \varphi \left( \lambda \right) \) .

Problem 2. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( f : E \rightarrow \mathbb{R} \) une application continue. On suppose qu’il existe un compact \( K \) de \( E \) tel que la restriction de \( f \) à \( K,{f}_{\mid K} \) , soit injective et tel que

> Problem 2. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( f : E \rightarrow \mathbb{R} \) a continuous map. Suppose there exists a compact set \( K \) of \( E \) such that the restriction of \( f \) to \( K,{f}_{\mid K} \) is injective and such that

\[
\forall x \in  K,\exists \varepsilon  > 0,\;{f}_{\mid \mathrm{B}\left( {x,\varepsilon }\right) }\;\text{ est injective. }
\]

Montrer qu’il existe un ouvert \( \Omega \) contenant \( K \) tel que \( {f}_{\mid \Omega } \) est injective.

> Show that there exists an open set \( \Omega \) containing \( K \) such that \( {f}_{\mid \Omega } \) is injective.

Solution. Raisonnons par l’absurde en supposant qu’un tel ouvert n’existe pas. Pour tout \( n \in {\mathbb{N}}^{ * } \) ,

> Solution. Let us reason by contradiction by assuming that such an open set does not exist. For every \( n \in {\mathbb{N}}^{ * } \) ,

\[
{O}_{n} = \left\{  {x \in  E \mid  \mathrm{d}\left( {x, K}\right)  < \frac{1}{n}}\right\}   = \mathop{\bigcup }\limits_{{x \in  K}}\mathrm{\;B}\left( {x,\frac{1}{n}}\right)
\]

est un ouvert contenant \( K \) , donc

> is an open set containing \( K \) , therefore

\[
\exists \left( {{x}_{n},{y}_{n}}\right)  \in  {O}_{n}^{2},\;\left( {{x}_{n} \neq  {y}_{n}\;\text{ et }\;f\left( {x}_{n}\right)  = f\left( {y}_{n}\right) }\right) .
\]

Pour tout \( n,{x}_{n} \in {O}_{n} \) donc il existe \( {x}_{n}^{\prime } \in K \) tel que \( \mathrm{d}\left( {{x}_{n},{x}_{n}^{\prime }}\right) < 1/n \) . De même, il existe pour tout \( n \) un point \( {y}_{n}^{\prime } \) de \( K \) tel que \( \mathrm{d}\left( {{y}_{n},{y}_{n}^{\prime }}\right) < 1/n \) .

> For every \( n,{x}_{n} \in {O}_{n} \) , there exists \( {x}_{n}^{\prime } \in K \) such that \( \mathrm{d}\left( {{x}_{n},{x}_{n}^{\prime }}\right) < 1/n \) . Similarly, for every \( n \) , there exists a point \( {y}_{n}^{\prime } \) in \( K \) such that \( \mathrm{d}\left( {{y}_{n},{y}_{n}^{\prime }}\right) < 1/n \) .

La suite \( {\left\lbrack \left( {x}_{n}^{\prime },{y}_{n}^{\prime }\right) \right\rbrack }_{n \in {\mathbb{N}}^{ * }} \) prend ses valeurs dans le compact \( {K}^{2} \) . On peut donc en extraire une sous-suite convergente \( \left\lbrack \left( {{x}_{\varphi \left( n\right) }^{\prime },{y}_{\varphi \left( n\right) }^{\prime }}\right) \right\rbrack \) dont nous noterons \( \left( {x, y}\right) \in {K}^{2} \) la limite. Les inégalités

> The sequence \( {\left\lbrack \left( {x}_{n}^{\prime },{y}_{n}^{\prime }\right) \right\rbrack }_{n \in {\mathbb{N}}^{ * }} \) takes its values in the compact set \( {K}^{2} \) . We can therefore extract a convergent subsequence \( \left\lbrack \left( {{x}_{\varphi \left( n\right) }^{\prime },{y}_{\varphi \left( n\right) }^{\prime }}\right) \right\rbrack \) whose limit we shall denote by \( \left( {x, y}\right) \in {K}^{2} \) . The inequalities

\[
\mathrm{d}\left( {{x}_{n}, x}\right)  \leq  \mathrm{d}\left( {{x}_{n},{x}_{n}^{\prime }}\right)  + \mathrm{d}\left( {{x}_{n}^{\prime }, x}\right)  < \frac{1}{n} + \mathrm{d}\left( {{x}_{n}^{\prime }, x}\right) \;\text{ et }\;\mathrm{d}\left( {{y}_{n}, y}\right)  < \frac{1}{n} + \mathrm{d}\left( {{y}_{n}^{\prime }, y}\right)
\]

montrent que les suites \( \left( {x}_{\varphi \left( n\right) }\right) \) et \( \left( {y}_{\varphi \left( n\right) }\right) \) tendent respectivement vers \( x \) et \( y \) . Comme \( f \) est continue et que pour tout \( n, f\left( {x}_{\varphi \left( n\right) }\right) = f\left( {y}_{\varphi \left( n\right) }\right) \) , on a \( f\left( x\right) = f\left( y\right) \) et comme \( {f}_{\mid K} \) est injective, \( x = y \) . De plus, il existe par hypothèse un \( \varepsilon > 0 \) tel que \( {f}_{\mid \mathrm{B}\left( {x,\varepsilon }\right) } \) soit injective. Ceci est contradictoire car il existe \( N \in {\mathbb{N}}^{ * } \) tel que \( {x}_{\varphi \left( N\right) } \) et \( {y}_{\varphi \left( N\right) } \) appartiennent à \( \mathrm{B}\left( {x,\varepsilon }\right) \) , et de plus \( f\left( {x}_{\varphi \left( N\right) }\right) = f\left( {y}_{\varphi \left( N\right) }\right) \) avec \( {x}_{\varphi \left( N\right) } \neq {y}_{\varphi \left( n\right) } \) par construction.

> show that the sequences \( \left( {x}_{\varphi \left( n\right) }\right) \) and \( \left( {y}_{\varphi \left( n\right) }\right) \) converge respectively to \( x \) and \( y \) . Since \( f \) is continuous and for all \( n, f\left( {x}_{\varphi \left( n\right) }\right) = f\left( {y}_{\varphi \left( n\right) }\right) \) , we have \( f\left( x\right) = f\left( y\right) \) and since \( {f}_{\mid K} \) is injective, \( x = y \) . Furthermore, there exists by hypothesis a \( \varepsilon > 0 \) such that \( {f}_{\mid \mathrm{B}\left( {x,\varepsilon }\right) } \) is injective. This is contradictory because there exists \( N \in {\mathbb{N}}^{ * } \) such that \( {x}_{\varphi \left( N\right) } \) and \( {y}_{\varphi \left( N\right) } \) belong to \( \mathrm{B}\left( {x,\varepsilon }\right) \) , and moreover \( f\left( {x}_{\varphi \left( N\right) }\right) = f\left( {y}_{\varphi \left( N\right) }\right) \) with \( {x}_{\varphi \left( N\right) } \neq {y}_{\varphi \left( n\right) } \) by construction.

Il existe donc un ouvert \( \Omega \) contenant \( K \) tel que \( {f}_{\mid \Omega } \) soit injective.

> There therefore exists an open set \( \Omega \) containing \( K \) such that \( {f}_{\mid \Omega } \) is injective.

Problem 3. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique.

> Problem 3. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space.

a) On suppose que toute application continue de \( E \) dans \( E \) admet un point fixe. Montrer que \( E \) est connexe.

> a) Suppose that every continuous map from \( E \) to \( E \) has a fixed point. Show that \( E \) is connected.

b) On suppose \( E \) connexe et compact. Peut-on affirmer que toute application continue de \( E \) dans \( E \) admet un point fixe ?

> b) Suppose \( E \) is connected and compact. Can we assert that every continuous map from \( E \) to \( E \) has a fixed point?

Solution. a) Raisonnons par l'absurde en supposant \( E \) non connexe. On peut trouver deux ouverts disjoints non vides \( A \) et \( B \) tels que \( E = A \cup B \) . Fixons \( a \in A \) et \( b \in B \) . Définissons \( f : E \rightarrow E \) par

> Solution. a) Let us reason by contradiction by assuming \( E \) is not connected. We can find two non-empty disjoint open sets \( A \) and \( B \) such that \( E = A \cup B \) . Let us fix \( a \in A \) and \( b \in B \) . Define \( f : E \rightarrow E \) by

\[
f\left( x\right)  = b\;\text{ si }\;x \in  A,\;f\left( x\right)  = a\;\text{ si }\;x \in  B.
\]

L’application \( f \) est continue puisque l’image réciproque de tout ouvert est un ouvert (si \( X \subset E \) , \( {f}^{-1}\left( X\right) \) est égal soit à \( \varnothing , E, A \) ou \( B \) ), sans point fixe par construction. Ceci est contraire aux hypothèses, donc \( E \) est nécessairement connexe.

> The map \( f \) is continuous since the preimage of any open set is an open set (if \( X \subset E \) , \( {f}^{-1}\left( X\right) \) is equal to either \( \varnothing , E, A \) or \( B \) ), with no fixed point by construction. This contradicts the hypotheses, therefore \( E \) is necessarily connected.

b) Non ! Par exemple, la partie du plan \( E = \{ z \in \mathbb{C}\left| \right| z \mid = 1\} \) est compacte, connexe (car connexe par arcs), et l’application \( f : E \rightarrow E\;x \mapsto - x \) est continue et sans point fixe.

> b) No! For example, the subset of the plane \( E = \{ z \in \mathbb{C}\left| \right| z \mid = 1\} \) is compact, connected (since it is path-connected), and the map \( f : E \rightarrow E\;x \mapsto - x \) is continuous and has no fixed point.

Problem 4. Soit \( K \) un fermé de \( {\left\lbrack 0,1\right\rbrack }^{2} \) . On suppose que

> Problem 4. Let \( K \) be a closed subset of \( {\left\lbrack 0,1\right\rbrack }^{2} \) . Suppose that

\( \forall x \in \left\lbrack {0,1}\right\rbrack ,\;{K}_{x} = \{ y \in \left\lbrack {0,1}\right\rbrack \mid \left( {x, y}\right) \in K\} \; \) est un intervalle non vide.

> \( \forall x \in \left\lbrack {0,1}\right\rbrack ,\;{K}_{x} = \{ y \in \left\lbrack {0,1}\right\rbrack \mid \left( {x, y}\right) \in K\} \; \) is a non-empty interval.

a) Montrer que \( K \) est connexe.

> a) Show that \( K \) is connected.

b) Montrer qu’il existe \( x \in \left\lbrack {0,1}\right\rbrack \) tel que \( x \in {K}_{x} \) .

> b) Show that there exists \( x \in \left\lbrack {0,1}\right\rbrack \) such that \( x \in {K}_{x} \) .

Solution. a) En vertu de la proposition 3 de la page 39, il suffit de montrer que toute application continue de \( K \) dans \( \{ 0,1\} \) est constante. Soit \( f \) une telle application.

> Solution. a) By virtue of proposition 3 on page 39, it suffices to show that any continuous map from \( K \) to \( \{ 0,1\} \) is constant. Let \( f \) be such a map.

Pour tout \( x \in \left\lbrack {0,1}\right\rbrack \) , l’application \( f\left( {x, \cdot }\right) : {K}_{x} \rightarrow \{ 0,1\} \;y \mapsto f\left( {x, y}\right) \) est continue, et \( {K}_{x} \) étant connexe (c’est un intervalle), on en déduit que \( f\left( {x, \cdot }\right) \) est constante. Notons \( g\left( x\right) \) cette constante. Si on montre que l’application ainsi définie \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \{ 0,1\} \) est constante, on aura prouvé que \( f \) est constante.

> For any \( x \in \left\lbrack {0,1}\right\rbrack \), the map \( f\left( {x, \cdot }\right) : {K}_{x} \rightarrow \{ 0,1\} \;y \mapsto f\left( {x, y}\right) \) is continuous, and since \( {K}_{x} \) is connected (it is an interval), we deduce that \( f\left( {x, \cdot }\right) \) is constant. Let us denote this constant by \( g\left( x\right) \). If we show that the map thus defined \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \{ 0,1\} \) is constant, we will have proven that \( f \) is constant.

Comme \( \left\lbrack {0,1}\right\rbrack \) est connexe, il suffit de prouver que \( g \) est localement constante pour montrer qu’elle est constante. Supposons que ce ne soit pas le cas, de sorte qu’il existe \( x \in \left\lbrack {0,1}\right\rbrack \) et une suite \( \left( {x}_{n}\right) \) de \( \left\lbrack {0,1}\right\rbrack \) qui tend vers \( x \) telle que \( g\left( {x}_{n}\right) \neq g\left( x\right) \) pour tout \( n \in \mathbb{N} \) . Supposons par exemple \( g\left( x\right) = 0 \) et \( g\left( {x}_{n}\right) = 1 \) pour tout \( n \) . Pour tout \( n,{K}_{{x}_{n}} \) est non vide donc il existe \( {y}_{n} \in {K}_{{x}_{n}} \) . L’ensemble \( K \) , fermé du compact \( {\left\lbrack 0,1\right\rbrack }^{2} \) est compact. On peut donc extraire de la suite \( {\left\lbrack \left( {x}_{n},{y}_{n}\right) \right\rbrack }_{n \in \mathbb{N}} \) de \( K \) une sous-suite convergente \( \left\lbrack \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \right\rbrack \) . On a \( x = \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{\varphi \left( n\right) } \) , et notons \( y \) la limite de \( \left( {y}_{\varphi \left( n\right) }\right) \) . Comme \( f \) est continue sur \( K \) ,

> Since \( \left\lbrack {0,1}\right\rbrack \) is connected, it suffices to prove that \( g \) is locally constant to show that it is constant. Suppose this is not the case, such that there exists \( x \in \left\lbrack {0,1}\right\rbrack \) and a sequence \( \left( {x}_{n}\right) \) in \( \left\lbrack {0,1}\right\rbrack \) that tends to \( x \) such that \( g\left( {x}_{n}\right) \neq g\left( x\right) \) for all \( n \in \mathbb{N} \). Suppose for example \( g\left( x\right) = 0 \) and \( g\left( {x}_{n}\right) = 1 \) for all \( n \). For all \( n,{K}_{{x}_{n}} \) is non-empty, so there exists \( {y}_{n} \in {K}_{{x}_{n}} \). The set \( K \), a closed subset of the compact set \( {\left\lbrack 0,1\right\rbrack }^{2} \), is compact. We can therefore extract from the sequence \( {\left\lbrack \left( {x}_{n},{y}_{n}\right) \right\rbrack }_{n \in \mathbb{N}} \) in \( K \) a convergent subsequence \( \left\lbrack \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \right\rbrack \). We have \( x = \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{\varphi \left( n\right) } \), and let us denote by \( y \) the limit of \( \left( {y}_{\varphi \left( n\right) }\right) \). Since \( f \) is continuous on \( K \),

\[
g\left( x\right)  = f\left( {x, y}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}g\left( {x}_{\varphi \left( n\right) }\right) .
\]

Ceci est impossible puisque \( g\left( x\right) = 0 \) et \( g\left( {x}_{\varphi \left( n\right) }\right) = 1 \) pour tout \( n \) .

> This is impossible since \( g\left( x\right) = 0 \) and \( g\left( {x}_{\varphi \left( n\right) }\right) = 1 \) for all \( n \).

L’application est donc localement constante sur \( \left\lbrack {0,1}\right\rbrack \) , donc continue sur \( \left\lbrack {0,1}\right\rbrack \) . Comme \( \left\lbrack {0,1}\right\rbrack \) est connexe, \( g \) est constante, donc \( f \) est constante et le résultat est prouvé.

> The map is therefore locally constant on \( \left\lbrack {0,1}\right\rbrack \), and thus continuous on \( \left\lbrack {0,1}\right\rbrack \). Since \( \left\lbrack {0,1}\right\rbrack \) is connected, \( g \) is constant, therefore \( f \) is constant and the result is proven.

b) Soit \( \varphi : K \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto x - y \) . Comme \( K \) est connexe et que \( \varphi \) est continue, \( \varphi \left( K\right) \) est un connexe de \( \mathbb{R} \) , donc un intervalle. L’ensemble \( {K}_{0} \) est non vide, il existe donc \( y \in \left\lbrack {0,1}\right\rbrack \) tel que \( \left( {0, y}\right) \in K \) , donc \( \varphi \left( {0, y}\right) = - y \leq 0 \) . De même, il existe \( y \in \left\lbrack {0,1}\right\rbrack \) tel que \( \left( {1, y}\right) \in K \) , donc \( \varphi \left( {1, y}\right) = y \geq 0 \) . Comme \( \varphi \left( K\right) \) est un intervalle, on en déduit l’existence de \( \left( {x, y}\right) \in K \) tel que \( \varphi \left( {x, y}\right) = 0 \) , c’est-à-dire \( x = y \) , ou encore \( x \in {K}_{x} \) .

> b) Let \( \varphi : K \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto x - y \) . Since \( K \) is connected and \( \varphi \) is continuous, \( \varphi \left( K\right) \) is a connected subset of \( \mathbb{R} \) , and thus an interval. The set \( {K}_{0} \) is non-empty, so there exists \( y \in \left\lbrack {0,1}\right\rbrack \) such that \( \left( {0, y}\right) \in K \) , and thus \( \varphi \left( {0, y}\right) = - y \leq 0 \) . Similarly, there exists \( y \in \left\lbrack {0,1}\right\rbrack \) such that \( \left( {1, y}\right) \in K \) , and thus \( \varphi \left( {1, y}\right) = y \geq 0 \) . Since \( \varphi \left( K\right) \) is an interval, we deduce the existence of \( \left( {x, y}\right) \in K \) such that \( \varphi \left( {x, y}\right) = 0 \) , that is \( x = y \) , or equivalently \( x \in {K}_{x} \) .

Problem 5. Soit \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une application continue. Un point \( {x}_{0} \) de \( {\mathbb{R}}^{n} \) étant donné, on définit la suite \( \left( {x}_{n}\right) \) par \( {x}_{n + 1} = f\left( {x}_{n}\right) \) . On suppose que \( \left( {x}_{n}\right) \) admet une et une seule valeur d’adhérence. Montrer que la suite \( \left( {x}_{n}\right) \) converge.

> Problem 5. Let \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a continuous map. Given a point \( {x}_{0} \) in \( {\mathbb{R}}^{n} \) , we define the sequence \( \left( {x}_{n}\right) \) by \( {x}_{n + 1} = f\left( {x}_{n}\right) \) . Suppose that \( \left( {x}_{n}\right) \) has one and only one cluster point. Show that the sequence \( \left( {x}_{n}\right) \) converges.

Solution. Il suffit de montrer que la suite \( \left( {x}_{n}\right) \) est bornée, car elle prendra alors ses valeurs dans un compact (les compacts de \( {\mathbb{R}}^{n} \) sont les fermés bornés) et on conclura grâce à la proposition 9 de la page 30.

> Solution. It suffices to show that the sequence \( \left( {x}_{n}\right) \) is bounded, as it will then take its values in a compact set (the compact sets of \( {\mathbb{R}}^{n} \) are the closed bounded sets) and we will conclude using proposition 9 on page 30.

Raisonnons par l’absurde et supposons \( \left( {x}_{n}\right) \) non bornée. Notons a l’unique valeur d’adhérence de \( \left( {x}_{n}\right) \) , et notons \( K \) le compact \( {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) \) . Soit \( N \in \mathbb{N} \) . Comme \( a \) est valeur d’adhérence il existe \( {n}_{0} \geq N \) tel que \( {x}_{{n}_{0}} \in K \) . De plus, \( \left( {x}_{n}\right) \) n’est pas bornée donc il existe \( n > {n}_{0} \) tel que \( {x}_{n} \notin K \) . Ceci prouve qu’il existe un entier \( m \geq {n}_{0} \) tel que \( {x}_{m} \in K \) et \( {x}_{m + 1} \notin K \) . On a aussi \( {x}_{m + 1} = f\left( {x}_{m}\right) \in f\left( K\right) \) , donc \( {x}_{m + 1} \in f\left( K\right) \smallsetminus K \) . En résumé, nous venons de montrer

> Let us reason by contradiction and assume \( \left( {x}_{n}\right) \) is unbounded. Let a be the unique cluster point of \( \left( {x}_{n}\right) \) , and let \( K \) be the compact set \( {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) \) . Let \( N \in \mathbb{N} \) . Since \( a \) is a cluster point, there exists \( {n}_{0} \geq N \) such that \( {x}_{{n}_{0}} \in K \) . Furthermore, \( \left( {x}_{n}\right) \) is not bounded, so there exists \( n > {n}_{0} \) such that \( {x}_{n} \notin K \) . This proves that there exists an integer \( m \geq {n}_{0} \) such that \( {x}_{m} \in K \) and \( {x}_{m + 1} \notin K \) . We also have \( {x}_{m + 1} = f\left( {x}_{m}\right) \in f\left( K\right) \) , so \( {x}_{m + 1} \in f\left( K\right) \smallsetminus K \) . In summary, we have just shown

\[
\forall N \in  \mathbb{N},\exists m \geq  N,\;{x}_{m} \in  f\left( K\right)  \smallsetminus  K.
\]

Ceci montre qu’il existe une sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) prenant ses valeurs dans \( f\left( K\right) \smallsetminus K \) , en particulier dans \( f\left( K\right) \) . L’ensemble \( f\left( K\right) \) est compact (image d’un compact par une application continue), on peut donc extraire de \( \left( {x}_{\varphi \left( n\right) }\right) \) une sous-suite \( \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \) qui converge. Notons \( b \) sa limite. Pour tout \( n,{x}_{\varphi \left( n\right) } \notin K \) donc \( \mathrm{d}\left( {{x}_{\varphi \left( n\right) }, a}\right) \geq 1 \) , on a donc \( \mathrm{d}\left( {b, a}\right) \geq 1 \) . Ceci est contraire aux hypothèses car \( b \) est une valeur d’adhérence de \( \left( {x}_{n}\right) \) différente de \( a \) . La suite \( \left( {x}_{n}\right) \) converge donc vers \( a \) .

> This shows that there exists a subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) taking its values in \( f\left( K\right) \smallsetminus K \), in particular in \( f\left( K\right) \). The set \( f\left( K\right) \) is compact (image of a compact set by a continuous map), so we can extract from \( \left( {x}_{\varphi \left( n\right) }\right) \) a subsequence \( \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \) that converges. Let \( b \) denote its limit. For all \( n,{x}_{\varphi \left( n\right) } \notin K \) therefore \( \mathrm{d}\left( {{x}_{\varphi \left( n\right) }, a}\right) \geq 1 \), we have \( \mathrm{d}\left( {b, a}\right) \geq 1 \). This contradicts the hypotheses because \( b \) is a cluster point of \( \left( {x}_{n}\right) \) different from \( a \). The sequence \( \left( {x}_{n}\right) \) therefore converges to \( a \).

PROBLEME 6. Soit \( G \) un groupe. On suppose que \( G \) est muni d’une distance, et que l’application \( \varphi : G \times G \rightarrow G\;\left( {x, y}\right) \mapsto x{y}^{-1} \) est continue (on parle de groupe topologique). a) On désigne par \( e \) l’élément neutre de \( G \) et par \( C \) la composante connexe de \( G \) contenant \( \{ e\} \) . Montrer que \( C \) est un sous-groupe de \( G \) .

> PROBLEM 6. Let \( G \) be a group. Suppose that \( G \) is equipped with a distance, and that the map \( \varphi : G \times G \rightarrow G\;\left( {x, y}\right) \mapsto x{y}^{-1} \) is continuous (we speak of a topological group). a) Let \( e \) denote the neutral element of \( G \) and \( C \) the connected component of \( G \) containing \( \{ e\} \). Show that \( C \) is a subgroup of \( G \).

b) On suppose \( G \) connexe. Soit \( H \) un sous-groupe ouvert de \( G \) . Montrer que \( H = G \) .

> b) Suppose \( G \) is connected. Let \( H \) be an open subgroup of \( G \). Show that \( H = G \).

Solution. a) En vertu d'un résultat classique d'algèbre, il suffit de montrer que \( \varphi \left( {C \times C}\right) \) est inclus dans \( C \) . Comme \( C \) est connexe, \( C \times C \) est connexe. De plus, \( \varphi \) est continue, donc \( \varphi \left( {C \times C}\right) \) est connexe. Or \( e \in \varphi \left( {C \times C}\right) \) (par exemple \( e = \varphi \left( {e, e}\right) \) ). L’ensemble \( \varphi \left( {C \times C}\right) \) est donc un connexe contenant \( e \) . Par définition de \( C \) , on a donc \( \varphi \left( {C \times C}\right) \subset C \) , d’où le résultat.

> Solution. a) By virtue of a classic result in algebra, it suffices to show that \( \varphi \left( {C \times C}\right) \) is included in \( C \). Since \( C \) is connected, \( C \times C \) is connected. Moreover, \( \varphi \) is continuous, so \( \varphi \left( {C \times C}\right) \) is connected. However, \( e \in \varphi \left( {C \times C}\right) \) (for example \( e = \varphi \left( {e, e}\right) \)). The set \( \varphi \left( {C \times C}\right) \) is therefore a connected set containing \( e \). By the definition of \( C \), we therefore have \( \varphi \left( {C \times C}\right) \subset C \), hence the result.

b) Considérons la relation d’équivalence \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \) . Les classes d’équivalence sont de la forme \( {Hx} \) avec \( x \in G \) . Pour \( y \in G \) , l’application \( \psi : G \rightarrow G\;x \mapsto x{y}^{-1} \) étant continue, \( {Hy} = {\psi }^{-1}\left( H\right) \) est ouvert. Ainsi, \( G \smallsetminus H = { \cup }_{y \notin H}{Hy} \) , réunion d’ouverts est ouvert, et donc \( H \) est fermé. Ainsi, \( H \) est ouvert et fermé dans le connexe \( G \) , donc \( H = G \) .

> b) Consider the equivalence relation \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \). The equivalence classes are of the form \( {Hx} \) with \( x \in G \). For \( y \in G \), the map \( \psi : G \rightarrow G\;x \mapsto x{y}^{-1} \) being continuous, \( {Hy} = {\psi }^{-1}\left( H\right) \) is open. Thus, \( G \smallsetminus H = { \cup }_{y \notin H}{Hy} \), a union of open sets, is open, and therefore \( H \) is closed. Thus, \( H \) is open and closed in the connected set \( G \), therefore \( H = G \).

PROBLÉME 7 (POINTS FIXES DE FONCTIONS RÉELLES À VARIABLE RÉELLE).

> PROBLEM 7 (FIXED POINTS OF REAL FUNCTIONS OF A REAL VARIABLE).

a) Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) une application croissante. Montrer que \( f \) a au moins un point fixe.

> a) Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) be an increasing map. Show that \( f \) has at least one fixed point.

b) Montrer qu’une application continue \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) a au moins un point fixe.

> b) Show that a continuous map \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) has at least one fixed point.

c) Soit \( f \) et \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) deux applications continues, telles que \( f \circ g = g \circ f \) . Montrer qu’il existe \( a \in \left\lbrack {0,1}\right\rbrack \) tel que \( f\left( a\right) = g\left( a\right) \) .

> c) Let \( f \) and \( g : \left\lbrack {0,1}\right\rbrack \rightarrow \left\lbrack {0,1}\right\rbrack \) be two continuous maps such that \( f \circ g = g \circ f \). Show that there exists \( a \in \left\lbrack {0,1}\right\rbrack \) such that \( f\left( a\right) = g\left( a\right) \).

d) Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application continue telle que \( f \circ f \) admette un point fixe. Montrer que \( f \) admet un point fixe. Généraliser.

> d) Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a continuous map such that \( f \circ f \) admits a fixed point. Show that \( f \) admits a fixed point. Generalize.

Solution. a) Soit \( A = \{ x \in \left\lbrack {0,1}\right\rbrack , x \leq f\left( x\right) \} \) . L’ensemble \( A \) est non vide car \( 0 \in A \) . Soit \( a = \sup A \) . Pour tout \( x \in A \) on a \( x \leq f\left( x\right) \leq f\left( a\right) \) car \( f \) est croissante, donc \( f\left( a\right) \) est un majorant de \( A \) donc \( a \leq f\left( a\right) \) . Comme \( f \) est croissante, ceci entraîne \( f\left( a\right) \leq f\left( {f\left( a\right) }\right) \) donc \( f\left( a\right) \in A \) par définition de \( A \) , donc \( f\left( a\right) \leq a \) par définition de \( a \) . Donc \( f\left( a\right) = a \) .

> Solution. a) Let \( A = \{ x \in \left\lbrack {0,1}\right\rbrack , x \leq f\left( x\right) \} \). The set \( A \) is non-empty because \( 0 \in A \). Let \( a = \sup A \). For all \( x \in A \) we have \( x \leq f\left( x\right) \leq f\left( a\right) \) because \( f \) is increasing, so \( f\left( a\right) \) is an upper bound of \( A \) so \( a \leq f\left( a\right) \). As \( f \) is increasing, this implies \( f\left( a\right) \leq f\left( {f\left( a\right) }\right) \) so \( f\left( a\right) \in A \) by definition of \( A \), so \( f\left( a\right) \leq a \) by definition of \( a \). Thus \( f\left( a\right) = a \).

b) Il suffit de considérer l’application \( g : x \mapsto f\left( x\right) - x \) . On a \( g\left( 0\right) = f\left( 0\right) \geq 0 \) et \( g\left( 1\right) = \; f\left( 1\right) - 1 \leq 0 \) , donc \( g \) change de signe, et comme \( g \) est continue elle s’annule au moins en un point \( a \) . On a alors \( f\left( a\right) = a \) .

> b) It suffices to consider the map \( g : x \mapsto f\left( x\right) - x \). We have \( g\left( 0\right) = f\left( 0\right) \geq 0 \) and \( g\left( 1\right) = \; f\left( 1\right) - 1 \leq 0 \), so \( g \) changes sign, and since \( g \) is continuous it vanishes at at least one point \( a \). We then have \( f\left( a\right) = a \).

c) L’ensemble \( E \) des points fixes de \( f \) est non vide d’après la question précédente. Si \( x \in E \) alors \( f\left( {g\left( x\right) }\right) = g\left( {f\left( x\right) }\right) = g\left( x\right) \) donc \( g\left( x\right) \in E \) . Autrement dit, \( g\left( E\right) \subset E \) . Donc si \( m = \inf E \) et \( M = \sup E \) , on a \( g\left( m\right) \geq m = f\left( m\right) \) et \( g\left( M\right) \leq M = f\left( M\right) \) , donc la fonction continue \( g - f \) change de signe sur \( \left\lbrack {0,1}\right\rbrack \) donc elle s’annule en un moins un point \( a \) , qui vérifie \( f\left( a\right) = g\left( a\right) \) .

> c) The set \( E \) of fixed points of \( f \) is non-empty according to the previous question. If \( x \in E \) then \( f\left( {g\left( x\right) }\right) = g\left( {f\left( x\right) }\right) = g\left( x\right) \) so \( g\left( x\right) \in E \) . In other words, \( g\left( E\right) \subset E \) . Thus if \( m = \inf E \) and \( M = \sup E \) , we have \( g\left( m\right) \geq m = f\left( m\right) \) and \( g\left( M\right) \leq M = f\left( M\right) \) , so the continuous function \( g - f \) changes sign on \( \left\lbrack {0,1}\right\rbrack \) and therefore vanishes at at least one point \( a \) , which satisfies \( f\left( a\right) = g\left( a\right) \) .

d) Si \( f \) n’admet pas de point fixe, alors la fonction continue \( x \mapsto f\left( x\right) - x \) ne s’annule jamais, elle garde donc un signe constant, par exemple \( f\left( x\right) - x > 0 \) sur \( \mathbb{R} \) . Ainsi pour tout réel \( x \) on a \( f\left( x\right) > x \) donc \( f\left( {f\left( x\right) }\right) > f\left( x\right) > x \) , ce qui n’est pas compatible avec l’hypothèse de point fixe de \( f \circ f \) . On généralise aisément : si la composée \( n \) fois de \( f \) avec elle même admet un point fixe, alors \( f \) admet un point fixe.

> d) If \( f \) does not admit a fixed point, then the continuous function \( x \mapsto f\left( x\right) - x \) never vanishes, so it maintains a constant sign, for example \( f\left( x\right) - x > 0 \) on \( \mathbb{R} \) . Thus for any real number \( x \) we have \( f\left( x\right) > x \) so \( f\left( {f\left( x\right) }\right) > f\left( x\right) > x \) , which is not compatible with the fixed point hypothesis of \( f \circ f \) . This generalizes easily: if the \( n \) -fold composition of \( f \) with itself admits a fixed point, then \( f \) admits a fixed point.

Problem 8. Soit \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) une application continue vérifiant \( f\left( 0\right) = f\left( 1\right) \) .

> Problem 8. Let \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) be a continuous map satisfying \( f\left( 0\right) = f\left( 1\right) \) .

a) Montrer qu’il existe \( x \in \left\lbrack {0,1/2}\right\rbrack \) tel que \( f\left( x\right) = f\left( {x + 1/2}\right) \) .

> a) Show that there exists \( x \in \left\lbrack {0,1/2}\right\rbrack \) such that \( f\left( x\right) = f\left( {x + 1/2}\right) \) .

b) Pour tout \( n \in \mathbb{N}, n \geq 2 \) , montrer qu’il existe \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) tel que \( f\left( x\right) = f\left( {x + 1/n}\right) \) . c) Montrer qu’il existe \( \alpha > 0 \) tel que \( \forall \beta \in \rbrack 0,\alpha \rbrack ,\exists x \in \left\lbrack {0,1 - \alpha }\right\rbrack , f\left( x\right) = f\left( {x + \beta }\right) \) .

> b) For all \( n \in \mathbb{N}, n \geq 2 \) , show that there exists \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) such that \( f\left( x\right) = f\left( {x + 1/n}\right) \) . c) Show that there exists \( \alpha > 0 \) such that \( \forall \beta \in \rbrack 0,\alpha \rbrack ,\exists x \in \left\lbrack {0,1 - \alpha }\right\rbrack , f\left( x\right) = f\left( {x + \beta }\right) \) .

d) Montrer qu’il existe une fonction continue \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) telle que \( f\left( 0\right) = f\left( 1\right) \) et vérifiant \( f\left( x\right) \neq f\left( {x + 2/5}\right) \) pour tout \( x \in \left\lbrack {0,3/5}\right\rbrack \) .

> d) Show that there exists a continuous function \( f : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R} \) such that \( f\left( 0\right) = f\left( 1\right) \) and satisfying \( f\left( x\right) \neq f\left( {x + 2/5}\right) \) for all \( x \in \left\lbrack {0,3/5}\right\rbrack \) .

Solution. a) Il suffit de considérer l’application \( g : \left\lbrack {0,1/2}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) - f\left( {x + 1/2}\right) \) . On a \( g\left( 0\right) = - g\left( {1/2}\right) \) donc \( g \) change de signe, et comme elle est continue, le théorème des valeurs intermédiaires nous assure de l’existence de \( x \in \left\lbrack {0,1/2}\right\rbrack \) tel que \( g\left( x\right) = 0 \) , ce qui entraîne \( f\left( x\right) = f\left( {x + 1/2}\right) . \)

> Solution. a) It suffices to consider the map \( g : \left\lbrack {0,1/2}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto f\left( x\right) - f\left( {x + 1/2}\right) \) . We have \( g\left( 0\right) = - g\left( {1/2}\right) \) so \( g \) changes sign, and since it is continuous, the intermediate value theorem ensures the existence of \( x \in \left\lbrack {0,1/2}\right\rbrack \) such that \( g\left( x\right) = 0 \) , which implies \( f\left( x\right) = f\left( {x + 1/2}\right) . \)

b) Raisonnons par l’absurde et supposons \( f\left( x\right) \neq f\left( {x + 1/n}\right) \) pour tout \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) . Ceci signifie que l’application continue \( g\left( x\right) = f\left( x\right) - f\left( {x + 1/n}\right) \) ne s’annule jamais, donc \( g \) garde un signe constant non nul, par exemple \( g > 0 \) . On en déduit \( f\left( x\right) > f\left( {x + 1/n}\right) \) pour tout \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) donc \( f\left( 0\right) > f\left( {1/n}\right) > f\left( {2/n}\right) > \cdots > f\left( {n/n}\right) = f\left( 1\right) \) , ce qui est absurde.

> b) Let us reason by contradiction and assume \( f\left( x\right) \neq f\left( {x + 1/n}\right) \) for all \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) . This means that the continuous map \( g\left( x\right) = f\left( x\right) - f\left( {x + 1/n}\right) \) never vanishes, so \( g \) maintains a non-zero constant sign, for example \( g > 0 \) . We deduce \( f\left( x\right) > f\left( {x + 1/n}\right) \) for all \( x \in \left\lbrack {0,1 - 1/n}\right\rbrack \) so \( f\left( 0\right) > f\left( {1/n}\right) > f\left( {2/n}\right) > \cdots > f\left( {n/n}\right) = f\left( 1\right) \) , which is absurd.

c) Si \( f \) est constante, le résultat est évident, sinon l’intuition nous suggère de nous placer autour d’un extremum de \( f \) . Comme \( f \) n’est pas constante, il existe \( x \) tel que \( f\left( x\right) \neq f\left( 0\right) \) , par exemple \( f\left( x\right) > f\left( 0\right) \) . Comme \( f \) est continue sur le compact \( \left\lbrack {0,1}\right\rbrack \) elle atteint son maximum donc il existe \( c \in \rbrack 0,1\left\lbrack \right. \) tel que \( f\left( c\right) = \mathop{\max }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}f\left( t\right) \) . Choisissons \( \alpha = \min \left( {c,1 - c}\right) \) . Considérons \( \beta \in \rbrack 0,\alpha \rbrack \) et construisons la fonction \( g\left( x\right) = f\left( x\right) - f\left( {x + \beta }\right) \) , définie sur \( \left\lbrack {0,1 - \beta }\right\rbrack \) . Si \( \alpha = c \) , on a \( g\left( {\alpha - \beta }\right) = f\left( {c - \beta }\right) - f\left( c\right) \leq 0 \) et \( g\left( \alpha \right) = f\left( c\right) - f\left( {c + \beta }\right) \geq 0 \) , donc \( g \) change de signe et comme elle est continue, elle s'annule au moins en un point, ce qui entraîne bien l'existence de \( x \in \left\lbrack {0,1 - \beta }\right\rbrack \) tel que \( f\left( x\right) = f\left( {x + \beta }\right) \) . Le raisonnement est similaire si \( \alpha = 1 - c \) à partir des inégalités \( g\left( {1 - \alpha - \beta }\right) = f\left( {c - \beta }\right) - f\left( c\right) \leq 0 \) et \( g\left( {1 - \alpha }\right) = f\left( c\right) - f\left( {c + \beta }\right) \geq 0 \) .

> c) If \( f \) is constant, the result is obvious; otherwise, intuition suggests we focus on an extremum of \( f \). Since \( f \) is not constant, there exists \( x \) such that \( f\left( x\right) \neq f\left( 0\right) \), for example \( f\left( x\right) > f\left( 0\right) \). As \( f \) is continuous on the compact set \( \left\lbrack {0,1}\right\rbrack \), it reaches its maximum, so there exists \( c \in \rbrack 0,1\left\lbrack \right. \) such that \( f\left( c\right) = \mathop{\max }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}f\left( t\right) \). Let us choose \( \alpha = \min \left( {c,1 - c}\right) \). Consider \( \beta \in \rbrack 0,\alpha \rbrack \) and construct the function \( g\left( x\right) = f\left( x\right) - f\left( {x + \beta }\right) \), defined on \( \left\lbrack {0,1 - \beta }\right\rbrack \). If \( \alpha = c \), we have \( g\left( {\alpha - \beta }\right) = f\left( {c - \beta }\right) - f\left( c\right) \leq 0 \) and \( g\left( \alpha \right) = f\left( c\right) - f\left( {c + \beta }\right) \geq 0 \), so \( g \) changes sign and, since it is continuous, it vanishes at at least one point, which indeed implies the existence of \( x \in \left\lbrack {0,1 - \beta }\right\rbrack \) such that \( f\left( x\right) = f\left( {x + \beta }\right) \). The reasoning is similar if \( \alpha = 1 - c \) starting from the inequalities \( g\left( {1 - \alpha - \beta }\right) = f\left( {c - \beta }\right) - f\left( c\right) \leq 0 \) and \( g\left( {1 - \alpha }\right) = f\left( c\right) - f\left( {c + \beta }\right) \geq 0 \).

d). Soit \( f \) une telle fonction. La fonction continue \( f\left( x\right) - f\left( {x + 2/5}\right) \) ne s’annule pas donc garde un signe constant non nul, par exemple positif. Donc on a toujours \( f\left( x\right) > f\left( {x + 2/5}\right) \) . La fonction \( f \) doit donc nécessairement vérifier \( f\left( 0\right) > f\left( {2/5}\right) > f\left( {4/5}\right) \) et \( f\left( {1/5}\right) > f\left( {3/5}\right) > f\left( 1\right) \) .

> d). Let \( f \) be such a function. The continuous function \( f\left( x\right) - f\left( {x + 2/5}\right) \) does not vanish, so it maintains a constant non-zero sign, for example positive. Thus, we always have \( f\left( x\right) > f\left( {x + 2/5}\right) \). The function \( f \) must therefore necessarily satisfy \( f\left( 0\right) > f\left( {2/5}\right) > f\left( {4/5}\right) \) and \( f\left( {1/5}\right) > f\left( {3/5}\right) > f\left( 1\right) \).

Ceci suggère de construire \( f \) telle que \( f\left( 0\right) = 0, f\left( {2/5}\right) = - 1, f\left( {4/5}\right) = - 2 \) et \( f\left( {1/5}\right) = 2 \) ,

> This suggests constructing \( f \) such that \( f\left( 0\right) = 0, f\left( {2/5}\right) = - 1, f\left( {4/5}\right) = - 2 \) and \( f\left( {1/5}\right) = 2 \),

![bo_d7fjkrs91nqc73ereoog_65_458_220_645_381_0.jpg](images/gourdon_analysis_fr_en_027_bod7fjkrs91nqc73ereoog654582206453810.jpg)

Figure 3. Le graphe de l’application \( f \) telle que \( f\left( {x + 2/5}\right) \neq f\left( x\right) \) , et en pointillé, le graphe de l’application \( x \mapsto f\left( {x + 2/5}\right) \)

> Figure 3. The graph of the map \( f \) such that \( f\left( {x + 2/5}\right) \neq f\left( x\right) \), and in dashed lines, the graph of the map \( x \mapsto f\left( {x + 2/5}\right) \)

\( f\left( {3/5}\right) = 1 \) et \( f\left( 1\right) = 0 \) , puis on interpole linéairement \( f \) sur chaque intervalle \( \left\lbrack {i/5,\left( {i + 1}\right) /5}\right\rbrack \) . Ainsi construite, on vérifie facilement que \( f\left( x\right) > f\left( {x + 2/5}\right) \) pour tout \( x \in \left\lbrack {0,3/5}\right\rbrack \) (voir la figure ci-contre).

> \( f\left( {3/5}\right) = 1 \) and \( f\left( 1\right) = 0 \), then we linearly interpolate \( f \) on each interval \( \left\lbrack {i/5,\left( {i + 1}\right) /5}\right\rbrack \). Constructed this way, it is easy to verify that \( f\left( x\right) > f\left( {x + 2/5}\right) \) for all \( x \in \left\lbrack {0,3/5}\right\rbrack \) (see the figure opposite).

Problem 9 (DISTANCE DE HAUSDORFF). Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. On note \( \mathcal{F} \) l’ensemble des parties fermées bornées non vides de \( E \) . Pour \( A, B \in \mathcal{F} \) , on pose

> Problem 9 (HAUSDORFF DISTANCE). Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. We denote by \( \mathcal{F} \) the set of non-empty bounded closed subsets of \( E \). For \( A, B \in \mathcal{F} \), we define

\[
\lambda \left( {A, B}\right)  = \mathop{\sup }\limits_{{x \in  A}}\mathrm{\;d}\left( {x, B}\right) \;\text{ et }\;\Delta \left( {A, B}\right)  = \sup \{ \lambda \left( {A, B}\right) ,\lambda \left( {B, A}\right) \} .
\]

a) Montrer que \( \Delta \) est une distance sur \( \mathcal{F} \) .

> a) Show that \( \Delta \) is a distance on \( \mathcal{F} \).

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {\mathcal{F}}_{n} \) l’ensemble des éléments de \( \mathcal{F} \) qui contiennent au moins \( n \) éléments de \( E \) . Pour tout \( n \in {\mathbb{N}}^{ * } \) , montrer que \( {\mathcal{F}}_{n} \) est un ouvert de \( \mathcal{F} \) .

> b) For any \( n \in {\mathbb{N}}^{ * } \), we denote by \( {\mathcal{F}}_{n} \) the set of elements of \( \mathcal{F} \) that contain at least \( n \) elements of \( E \). For any \( n \in {\mathbb{N}}^{ * } \), show that \( {\mathcal{F}}_{n} \) is an open set of \( \mathcal{F} \).

c) On suppose \( E \) compact. Montrer qu’une suite de Cauchy \( {\left( {Y}_{n}\right) }_{n \in \mathbb{N}} \) de \( \left( {\mathcal{F},\Delta }\right) \) telle que \( {Y}_{n + 1} \subset {Y}_{n} \) pour tout \( n \) converge vers \( Y = { \cap }_{n \in \mathbb{N}}{Y}_{n} \) . En déduire que \( \left( {\mathcal{F},\Delta }\right) \) est complet.

> c) Assume \( E \) is compact. Show that a Cauchy sequence \( {\left( {Y}_{n}\right) }_{n \in \mathbb{N}} \) of \( \left( {\mathcal{F},\Delta }\right) \) such that \( {Y}_{n + 1} \subset {Y}_{n} \) for all \( n \) converges to \( Y = { \cap }_{n \in \mathbb{N}}{Y}_{n} \). Deduce that \( \left( {\mathcal{F},\Delta }\right) \) is complete.

d) Si \( E \) est compact, montrer que \( \mathcal{F} \) est compact (on pourra utiliser le résultat de l’exer-cice 2 de la page 32).

> d) If \( E \) is compact, show that \( \mathcal{F} \) is compact (one may use the result of exercise 2 on page 32).

Solution. a) Il est clair que \( \Delta \) est symétrique.

> Solution. a) It is clear that \( \Delta \) is symmetric.

Si \( \lambda \left( {A, B}\right) = 0 \) avec \( A, B \in \mathcal{F} \) , alors pour tout \( x \in A,\mathrm{\;d}\left( {x, B}\right) = 0 \) et \( B \) étant fermé, \( x \in B \) . On en déduit \( A \subset B \) . Maintenant, si \( \Delta \left( {A, B}\right) = 0 \) , alors \( \lambda \left( {A, B}\right) = \lambda \left( {B, A}\right) = 0 \) donc \( A \subset B \) et \( B \subset A \) donc \( A = B \) . Réciproquement si \( A = B \) on a bien sûr \( \Delta \left( {A, B}\right) = 0 \) .

> If \( \lambda \left( {A, B}\right) = 0 \) with \( A, B \in \mathcal{F} \), then for all \( x \in A,\mathrm{\;d}\left( {x, B}\right) = 0 \) and \( B \) being closed, \( x \in B \). We deduce \( A \subset B \). Now, if \( \Delta \left( {A, B}\right) = 0 \), then \( \lambda \left( {A, B}\right) = \lambda \left( {B, A}\right) = 0 \) so \( A \subset B \) and \( B \subset A \) so \( A = B \). Conversely, if \( A = B \), we clearly have \( \Delta \left( {A, B}\right) = 0 \).

Il nous reste à montrer que \( \Delta \) vérifie l’inégalité triangulaire. Donnons nous \( A, B \) et \( C \in \mathcal{F} \) . - On a \( \forall \left( {x, y, z}\right) \in A \times B \times C,\;\mathrm{\;d}\left( {x, C}\right) \leq \mathrm{d}\left( {x, z}\right) \leq \mathrm{d}\left( {x, y}\right) + \mathrm{d}\left( {y, z}\right) \) .

> It remains for us to show that \( \Delta \) satisfies the triangle inequality. Let us take \( A, B \) and \( C \in \mathcal{F} \). - We have \( \forall \left( {x, y, z}\right) \in A \times B \times C,\;\mathrm{\;d}\left( {x, C}\right) \leq \mathrm{d}\left( {x, z}\right) \leq \mathrm{d}\left( {x, y}\right) + \mathrm{d}\left( {y, z}\right) \).

- En ne retenant que le premier et le dernier terme dans les inégalités précédentes, on obtient, en passant à la borne inférieure sur les \( z \in  C\mathrm{\;d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, y}\right)  + \mathrm{d}\left( {y, C}\right) \) .

> - By keeping only the first and last terms in the previous inequalities, we obtain, by taking the infimum over \( z \in  C\mathrm{\;d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, y}\right)  + \mathrm{d}\left( {y, C}\right) \).

- Comme \( \mathrm{d}\left( {y, C}\right)  \leq  \lambda \left( {B, C}\right) \) , on a \( \mathrm{d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, y}\right)  + \lambda \left( {B, C}\right) \) .

> - Since \( \mathrm{d}\left( {y, C}\right)  \leq  \lambda \left( {B, C}\right) \), we have \( \mathrm{d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, y}\right)  + \lambda \left( {B, C}\right) \).

- En prenant la borne inférieure sur les \( y \in  B \) , on obtient \( \mathrm{d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, B}\right)  + \lambda \left( {B, C}\right) \) .

> - By taking the infimum over \( y \in  B \), we obtain \( \mathrm{d}\left( {x, C}\right)  \leq  \mathrm{d}\left( {x, B}\right)  + \lambda \left( {B, C}\right) \).

- Comme \( \mathrm{d}\left( {x, B}\right)  \leq  \lambda \left( {A, B}\right) ,\mathrm{d}\left( {x, C}\right)  \leq  \lambda \left( {A, B}\right)  + \lambda \left( {B, C}\right) \) .

> - Since \( \mathrm{d}\left( {x, B}\right)  \leq  \lambda \left( {A, B}\right) ,\mathrm{d}\left( {x, C}\right)  \leq  \lambda \left( {A, B}\right)  + \lambda \left( {B, C}\right) \).

- Il ne reste plus qu’à prendre la borne supérieure sur les \( x \in  A \) , ce qui donne \( \lambda \left( {A, C}\right)  \leq \; \lambda \left( {A, B}\right)  + \lambda \left( {B, C}\right) . \)

> - It only remains to take the supremum over \( x \in  A \), which gives \( \lambda \left( {A, C}\right)  \leq \; \lambda \left( {A, B}\right)  + \lambda \left( {B, C}\right) . \)

- On a de même \( \lambda \left( {C, A}\right)  \leq  \lambda \left( {C, B}\right)  + \lambda \left( {B, A}\right) \) .

> - We similarly have \( \lambda \left( {C, A}\right)  \leq  \lambda \left( {C, B}\right)  + \lambda \left( {B, A}\right) \).

- Ceci suffit pour conclure \( \Delta \left( {A, C}\right)  \leq  \Delta \left( {A, B}\right)  + \Delta \left( {B, C}\right) \) .

> - This is sufficient to conclude \( \Delta \left( {A, C}\right)  \leq  \Delta \left( {A, B}\right)  + \Delta \left( {B, C}\right) \).

b) Soit \( F \in {\mathcal{F}}_{n} \) . Il existe \( n \) éléments distincts \( {x}_{1},\ldots ,{x}_{n} \) dans \( F \) . Soit \( \varepsilon = \mathop{\inf }\limits_{{i \neq j}}\mathrm{\;d}\left( {{x}_{i},{x}_{j}}\right) > 0 \) . Soit \( G \in \mathcal{F} \) tel que \( \Delta \left( {F, G}\right) < \varepsilon /2 \) . Alors \( \lambda \left( {F, G}\right) < \varepsilon /2 \) , donc pour tout \( i,1 \leq i \leq n,\mathrm{\;d}\left( {{x}_{i}, G}\right) < \varepsilon /2 \) , de sorte qu’il existe \( {y}_{i} \in G \) tel que \( \mathrm{d}\left( {{x}_{i},{y}_{i}}\right) < \varepsilon /2 \) . Les points \( {y}_{1},\ldots ,{y}_{n} \) sont distincts (si \( {y}_{i} = {y}_{j} \) , alors \( \mathrm{d}\left( {{x}_{i},{x}_{j}}\right) \leq \mathrm{d}\left( {{x}_{i},{y}_{i}}\right) + \mathrm{d}\left( {{y}_{j},{x}_{j}}\right) < \varepsilon \) , donc \( i = j \) par définition de \( \varepsilon \) ), donc \( G \in {\mathcal{F}}_{n} \) . La boule ouverte de centre \( F \) de rayon \( \varepsilon /2 \) est donc incluse dans \( {\mathcal{F}}_{n} \) , donc \( {\mathcal{F}}_{n} \) est ouvert. c) Les \( {Y}_{n} \) sont fermés dans le compact \( E \) donc compact, et l’intersection d’une suite décroissante de compacts non vides étant non vide, on en déduit \( Y = { \cap }_{n}{Y}_{n} \in \mathcal{F} \) .

> b) Let \( F \in {\mathcal{F}}_{n} \) . There exist \( n \) distinct elements \( {x}_{1},\ldots ,{x}_{n} \) in \( F \) . Let \( \varepsilon = \mathop{\inf }\limits_{{i \neq j}}\mathrm{\;d}\left( {{x}_{i},{x}_{j}}\right) > 0 \) . Let \( G \in \mathcal{F} \) such that \( \Delta \left( {F, G}\right) < \varepsilon /2 \) . Then \( \lambda \left( {F, G}\right) < \varepsilon /2 \) , so for all \( i,1 \leq i \leq n,\mathrm{\;d}\left( {{x}_{i}, G}\right) < \varepsilon /2 \) , such that there exists \( {y}_{i} \in G \) such that \( \mathrm{d}\left( {{x}_{i},{y}_{i}}\right) < \varepsilon /2 \) . The points \( {y}_{1},\ldots ,{y}_{n} \) are distinct (if \( {y}_{i} = {y}_{j} \) , then \( \mathrm{d}\left( {{x}_{i},{x}_{j}}\right) \leq \mathrm{d}\left( {{x}_{i},{y}_{i}}\right) + \mathrm{d}\left( {{y}_{j},{x}_{j}}\right) < \varepsilon \) , so \( i = j \) by definition of \( \varepsilon \) ), so \( G \in {\mathcal{F}}_{n} \) . The open ball centered at \( F \) with radius \( \varepsilon /2 \) is therefore included in \( {\mathcal{F}}_{n} \) , so \( {\mathcal{F}}_{n} \) is open. c) The \( {Y}_{n} \) are closed in the compact \( E \) and thus compact, and since the intersection of a decreasing sequence of non-empty compact sets is non-empty, we deduce \( Y = { \cap }_{n}{Y}_{n} \in \mathcal{F} \) .

Donnons nous maintenant \( \varepsilon > 0 \) . Par hypothèse, la suite \( \left( {Y}_{n}\right) \) est de Cauchy dans \( \left( {\mathcal{F},\Delta }\right) \) donc il existe \( N \in \mathbb{N} \) tel que pour tout \( p, q \geq N,\Delta \left( {{Y}_{p},{Y}_{q}}\right) < \varepsilon \) . Nous allons montrer que \( \Delta \left( {Y,{Y}_{n}}\right) \leq \varepsilon \) pour tout \( n \geq N. \)

> Now let us consider \( \varepsilon > 0 \) . By hypothesis, the sequence \( \left( {Y}_{n}\right) \) is Cauchy in \( \left( {\mathcal{F},\Delta }\right) \) so there exists \( N \in \mathbb{N} \) such that for all \( p, q \geq N,\Delta \left( {{Y}_{p},{Y}_{q}}\right) < \varepsilon \) . We will show that \( \Delta \left( {Y,{Y}_{n}}\right) \leq \varepsilon \) for all \( n \geq N. \)

Fixons \( n \geq N \) . Pour tout \( p \geq n,\lambda \left( {{Y}_{n},{Y}_{p}}\right) \leq \Delta \left( {{Y}_{n},{Y}_{p}}\right) < \varepsilon \) . Donnons nous \( x \in {Y}_{n} \) . On a \( \mathrm{d}\left( {x,{Y}_{p}}\right) < \varepsilon \) , donc

> Let us fix \( n \geq N \) . For all \( p \geq n,\lambda \left( {{Y}_{n},{Y}_{p}}\right) \leq \Delta \left( {{Y}_{n},{Y}_{p}}\right) < \varepsilon \) . Let us consider \( x \in {Y}_{n} \) . We have \( \mathrm{d}\left( {x,{Y}_{p}}\right) < \varepsilon \) , so

\[
\forall p \geq  n,\exists {x}_{p} \in  {Y}_{p},\;\mathrm{\;d}\left( {x,{x}_{p}}\right)  < \varepsilon .
\]

La suite \( \left( {x}_{p}\right) \) prend ses valeurs dans le compact \( E \) , on peut donc en extraire une sous-suite convergente \( \left( {x}_{\varphi \left( p\right) }\right) \) , dont nous noterons \( \ell \) la limite. Pour tout \( p \geq n,\ell \in {Y}_{p} \) car pour tout \( m \geq p,{x}_{m} \in {Y}_{p} \) et \( {Y}_{p} \) est fermé. Ainsi, \( \ell \in { \cap }_{p \geq n}{Y}_{p} = Y \) . Par ailleurs, pour tout \( p,\mathrm{\;d}\left( {x,{x}_{\varphi \left( p\right) }}\right) < \varepsilon \) donc \( \mathrm{d}\left( {x,\ell }\right) \leq \varepsilon \) . Comme \( \ell \in Y \) , on en déduit \( \mathrm{d}\left( {x, Y}\right) \leq \varepsilon \) . Ceci étant vrai pour tout \( x \in {Y}_{n} \) , on en déduit \( \lambda \left( {{Y}_{n}, Y}\right) \leq \varepsilon \) . Or \( Y \subset {Y}_{n} \) , donc \( \lambda \left( {Y,{Y}_{n}}\right) = 0 \) , donc \( \Delta \left( {{Y}_{n}, Y}\right) \leq \varepsilon \) . Ceci étant vrai pour tout \( n \geq N \) , on en déduit que \( \left( {Y}_{n}\right) \) converge vers \( Y \) .

> The sequence \( \left( {x}_{p}\right) \) takes its values in the compact set \( E \) , so we can extract a convergent subsequence \( \left( {x}_{\varphi \left( p\right) }\right) \) , whose limit we will denote by \( \ell \) . For all \( p \geq n,\ell \in {Y}_{p} \) because for all \( m \geq p,{x}_{m} \in {Y}_{p} \) and \( {Y}_{p} \) is closed. Thus, \( \ell \in { \cap }_{p \geq n}{Y}_{p} = Y \) . Furthermore, for all \( p,\mathrm{\;d}\left( {x,{x}_{\varphi \left( p\right) }}\right) < \varepsilon \) so \( \mathrm{d}\left( {x,\ell }\right) \leq \varepsilon \) . As \( \ell \in Y \) , we deduce \( \mathrm{d}\left( {x, Y}\right) \leq \varepsilon \) . Since this is true for all \( x \in {Y}_{n} \) , we deduce \( \lambda \left( {{Y}_{n}, Y}\right) \leq \varepsilon \) . However \( Y \subset {Y}_{n} \) , so \( \lambda \left( {Y,{Y}_{n}}\right) = 0 \) , so \( \Delta \left( {{Y}_{n}, Y}\right) \leq \varepsilon \) . Since this is true for all \( n \geq N \) , we deduce that \( \left( {Y}_{n}\right) \) converges to \( Y \) .

Montrons maintenant que l’espace métrique \( \left( {\mathcal{F},\Delta }\right) \) est complet. Soit \( \left( {Y}_{n}\right) \) une suite de Cauchy de cet espace. Pour tout \( n \in \mathbb{N} \) , on pose \( {X}_{n} = \overline{{ \cup }_{p \geq n}{Y}_{p}} \) . La suite \( \left( {X}_{n}\right) \) ainsi définie est une suite décroissante de \( \left( {\mathcal{F},\Delta }\right) \) .

> Let us now show that the metric space \( \left( {\mathcal{F},\Delta }\right) \) is complete. Let \( \left( {Y}_{n}\right) \) be a Cauchy sequence in this space. For all \( n \in \mathbb{N} \) , we set \( {X}_{n} = \overline{{ \cup }_{p \geq n}{Y}_{p}} \) . The sequence \( \left( {X}_{n}\right) \) thus defined is a decreasing sequence of \( \left( {\mathcal{F},\Delta }\right) \) .

Soit \( \varepsilon > 0 \) et \( N \in \mathbb{N} \) tel que pour tous \( p, q \geq N,\Delta \left( {{Y}_{p},{Y}_{q}}\right) < \varepsilon \) . Soit \( n \geq N \) . Si \( x \in { \cup }_{p \geq n}{Y}_{p} \) , il existe \( p \geq n \) tel que \( x \in {Y}_{p} \) , donc \( \mathrm{d}\left( {x,{Y}_{n}}\right) \leq \lambda \left( {{Y}_{p},{Y}_{n}}\right) < \varepsilon \) . On en déduit que pour tout \( x \in \; \overline{{ \cup }_{p \geq n}{Y}_{p}},\mathrm{\;d}\left( {x,{Y}_{n}}\right) \leq \varepsilon \) , donc \( \lambda \left( {{X}_{n},{Y}_{n}}\right) \leq \varepsilon \) . Comme \( {X}_{n} \subset {Y}_{n} \) , on a \( \lambda \left( {{Y}_{n},{X}_{n}}\right) = 0 \) . Finalement, nous venons de montrer que

> Let \( \varepsilon > 0 \) and \( N \in \mathbb{N} \) such that for all \( p, q \geq N,\Delta \left( {{Y}_{p},{Y}_{q}}\right) < \varepsilon \) . Let \( n \geq N \) . If \( x \in { \cup }_{p \geq n}{Y}_{p} \) , there exists \( p \geq n \) such that \( x \in {Y}_{p} \) , so \( \mathrm{d}\left( {x,{Y}_{n}}\right) \leq \lambda \left( {{Y}_{p},{Y}_{n}}\right) < \varepsilon \) . We deduce that for all \( x \in \; \overline{{ \cup }_{p \geq n}{Y}_{p}},\mathrm{\;d}\left( {x,{Y}_{n}}\right) \leq \varepsilon \) , so \( \lambda \left( {{X}_{n},{Y}_{n}}\right) \leq \varepsilon \) . As \( {X}_{n} \subset {Y}_{n} \) , we have \( \lambda \left( {{Y}_{n},{X}_{n}}\right) = 0 \) . Finally, we have just shown that

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall n \geq  N,\;\Delta \left( {{X}_{n},{Y}_{n}}\right)  < \varepsilon .
\]

(*)

> On en déduit maintenant aisément que la suite \( \left( {X}_{n}\right) \) vérifie le critère de Cauchy. C’est de plus une suite décroissante de fermés non vides, donc d’après ce que l’on a vu précédemment, \( \left( {X}_{n}\right) \) converge vers \( X = { \cap }_{n \in \mathbb{N}}{X}_{n} \) . La relation (*) montre alors que \( \left( {Y}_{n}\right) \) converge vers \( X \) .

We now easily deduce that the sequence \( \left( {X}_{n}\right) \) satisfies the Cauchy criterion. Moreover, it is a decreasing sequence of non-empty closed sets, so according to what we saw previously, \( \left( {X}_{n}\right) \) converges to \( X = { \cap }_{n \in \mathbb{N}}{X}_{n} \) . The relation (*) then shows that \( \left( {Y}_{n}\right) \) converges to \( X \) .

> d) Nous venons de voir que \( \left( {\mathcal{F},\Delta }\right) \) est complet. En vertu du résultat de l’exercice 2 de la page 32, il suffit, pour prouver la compacité de cet espace métrique, de montrer qu'il est précompact (i. e. pour tout \( \varepsilon > 0 \) , il existe un nombre fini de boules de rayon \( \varepsilon \) qui recouvrent \( \mathcal{F} \) ).

d) We have just seen that \( \left( {\mathcal{F},\Delta }\right) \) is complete. By virtue of the result of exercise 2 on page 32, it suffices, to prove the compactness of this metric space, to show that it is precompact (i.e., for any \( \varepsilon > 0 \) , there exists a finite number of balls of radius \( \varepsilon \) that cover \( \mathcal{F} \) ).

> Soit \( \varepsilon > 0 \) . L’ensemble \( E \) est compact donc précompact, donc il existe une famille finie de boules \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) qui recouvre \( \mathcal{F} \) . Notons \( \Gamma \) l’ensemble des parties non vides de \( \left\{ {{x}_{1},\ldots ,{x}_{n}}\right\} \) . Nous allons montrer que \( \mathcal{F} \subset { \cup }_{F \in \Gamma }{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) , où pour tout \( F \in \Gamma ,{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) désigne la boule fermée de centre \( F \) de rayon \( \varepsilon \) dans \( \left( {\mathcal{F},\Delta }\right) \) .

Let \( \varepsilon > 0 \) . The set \( E \) is compact and therefore precompact, so there exists a finite family of balls \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) that covers \( \mathcal{F} \) . Let \( \Gamma \) denote the set of non-empty subsets of \( \left\{ {{x}_{1},\ldots ,{x}_{n}}\right\} \) . We will show that \( \mathcal{F} \subset { \cup }_{F \in \Gamma }{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) , where for all \( F \in \Gamma ,{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) denotes the closed ball with center \( F \) and radius \( \varepsilon \) in \( \left( {\mathcal{F},\Delta }\right) \) .

> Soit \( A \in \mathcal{F} \) . Notons \( F = \left\{ {{x}_{i} \mid 1 \leq i \leq n,\mathrm{\;d}\left( {{x}_{i}, A}\right) < \varepsilon }\right\} \) . Comme la famille \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) recouvre \( E, F \) est non vide donc \( F \in \Gamma \) . Pour tout \( x \in F,\mathrm{\;d}\left( {x, A}\right) < \varepsilon \) donc \( \lambda \left( {F, A}\right) < \varepsilon \) .

Let \( A \in \mathcal{F} \) . Let \( F = \left\{ {{x}_{i} \mid 1 \leq i \leq n,\mathrm{\;d}\left( {{x}_{i}, A}\right) < \varepsilon }\right\} \) . Since the family \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) covers \( E, F \) and is non-empty, \( F \in \Gamma \) . For all \( x \in F,\mathrm{\;d}\left( {x, A}\right) < \varepsilon \) , therefore \( \lambda \left( {F, A}\right) < \varepsilon \) .

> Soit \( x \in A \) . La famille \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) recouvrant \( E \) , il existe \( {x}_{i}\left( {1 \leq i \leq n}\right) \) tel que \( \mathrm{d}\left( {x,{x}_{i}}\right) < \; \varepsilon \) . On a donc \( {x}_{i} \in F \) et \( \mathrm{d}\left( {x, F}\right) \leq \mathrm{d}\left( {x,{x}_{i}}\right) < \varepsilon \) , et ecci pour tout \( x \in A \) , donc \( \lambda \left( {A, F}\right) \leq \varepsilon \) . On en déduit \( \Delta \left( {A, F}\right) \leq \varepsilon \) , donc \( A \in {\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) .

Let \( x \in A \) . Since the family \( {\left( \mathrm{B}\left( {x}_{i},\varepsilon \right) \right) }_{1 \leq i \leq n} \) covers \( E \) , there exists \( {x}_{i}\left( {1 \leq i \leq n}\right) \) such that \( \mathrm{d}\left( {x,{x}_{i}}\right) < \; \varepsilon \) . We therefore have \( {x}_{i} \in F \) and \( \mathrm{d}\left( {x, F}\right) \leq \mathrm{d}\left( {x,{x}_{i}}\right) < \varepsilon \) , and this for all \( x \in A \) , so \( \lambda \left( {A, F}\right) \leq \varepsilon \) . We deduce \( \Delta \left( {A, F}\right) \leq \varepsilon \) , therefore \( A \in {\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) .

> Nous venons de montrer que \( \mathcal{F} \subset { \cup }_{F \in \Gamma }{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) , et comme \( \Gamma \) est fini, on en déduit le résultat.

We have just shown that \( \mathcal{F} \subset { \cup }_{F \in \Gamma }{\mathrm{B}}_{\Delta }\left( {F,\varepsilon }\right) \) , and since \( \Gamma \) is finite, we deduce the result.

> Problem 10 (Oscillation D’UNE FONCTION). Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques et une application \( f : E \rightarrow F \) . Pour tout \( {x}_{0} \in E \) , on note

Problem 10 (OSCILLATION OF A FUNCTION). Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces and a map \( f : E \rightarrow F \) . For any \( {x}_{0} \in E \) , we denote

\[
\omega \left( {f,{x}_{0}}\right)  = \mathop{\inf }\limits_{{\rho  > 0}}\left\lbrack  {\mathop{\sup }\limits_{{x, y \in  \mathrm{B}\left( {{x}_{0},\rho }\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right) }\right\rbrack   \in  {\mathbb{R}}^{ + } \cup  \{  + \infty \}
\]

(oscillation de \( f \) en \( {x}_{0} \) ), où \( \mathrm{B}\left( {{x}_{0},\rho }\right) \) désigne la boule ouverte dans \( \left( {E,\mathrm{\;d}}\right) \) de centre \( {x}_{0} \) de rayon \( \rho \) .

> (oscillation of \( f \) at \( {x}_{0} \) ), where \( \mathrm{B}\left( {{x}_{0},\rho }\right) \) denotes the open ball in \( \left( {E,\mathrm{\;d}}\right) \) centered at \( {x}_{0} \) with radius \( \rho \) .

a) Montrer que \( f \) est continue en \( {x}_{0} \in E \) si et seulement si \( \omega \left( {f,{x}_{0}}\right) = 0 \) .

> a) Show that \( f \) is continuous at \( {x}_{0} \in E \) if and only if \( \omega \left( {f,{x}_{0}}\right) = 0 \) .

b) Pour tout \( \varepsilon \geq 0 \) , montrer que l’ensemble

> b) For any \( \varepsilon \geq 0 \) , show that the set

\[
{A}_{\varepsilon } = \{ x \in  E \mid  \omega \left( {f, x}\right)  \geq  \varepsilon \}
\]

est un fermé de \( E \) . L’application \( x \mapsto \omega \left( {f, x}\right) \) est elle continue ?

> is a closed subset of \( E \) . Is the map \( x \mapsto \omega \left( {f, x}\right) \) continuous?

c) Montrer que l’ensemble des points où \( f \) est continue est le complémentaire de l’ensemble \( { \cup }_{n \in {\mathbb{N}}^{ * }}{A}_{1/n} \) .

> c) Show that the set of points where \( f \) is continuous is the complement of the set \( { \cup }_{n \in {\mathbb{N}}^{ * }}{A}_{1/n} \) .

d) On suppose ici \( E \) compact et qu’il existe \( \varepsilon > 0 \) tel que \( \omega \left( {f, x}\right) < \varepsilon \) pour tout \( x \in E \) . Montrer

> d) Assume here that \( E \) is compact and that there exists \( \varepsilon > 0 \) such that \( \omega \left( {f, x}\right) < \varepsilon \) for all \( x \in E \) . Show

\[
\exists \alpha  > 0,\forall \left( {x, y}\right)  \in  {E}^{2},\mathrm{\;d}\left( {x, y}\right)  < \alpha ,\;\delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

Solution. a) Supposons \( f \) continue en \( {x}_{0} \in E \) . Soit \( \varepsilon > 0 \) . Alors

> Solution. a) Suppose \( f \) is continuous at \( {x}_{0} \in E \) . Let \( \varepsilon > 0 \) . Then

\[
\exists \rho  > 0,\forall y \in  \mathrm{B}\left( {{x}_{0},\rho }\right) ,\;\delta \left( {f\left( {x}_{0}\right) , f\left( y\right) }\right)  < \varepsilon ,
\]

donc

> therefore

\[
\forall \left( {x, y}\right)  \in  \mathrm{B}{\left( {x}_{0},\rho \right) }^{2},\;\delta \left( {f\left( x\right) , f\left( y\right) }\right)  \leq  \delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  + \delta \left( {f\left( {x}_{0}\right)  + f\left( y\right) }\right)  < {2\varepsilon },
\]

d’où

> whence

\[
\omega \left( {f,{x}_{0}}\right)  \leq  \mathop{\sup }\limits_{{x, y \in  \mathrm{B}\left( {{x}_{0},\rho }\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right)  \leq  {2\varepsilon }.
\]

Ceci étant vrai pour tout \( \varepsilon > 0 \) , on en déduit \( \omega \left( {f,{x}_{0}}\right) = 0 \) .

> Since this is true for any \( \varepsilon > 0 \) , we deduce \( \omega \left( {f,{x}_{0}}\right) = 0 \) .

Réciproquement, si \( \omega \left( {f,{x}_{0}}\right) = 0 \) , alors

> Conversely, if \( \omega \left( {f,{x}_{0}}\right) = 0 \) , then

\[
\forall \varepsilon  > 0,\exists \rho  > 0,\;\mathop{\sup }\limits_{{x, y \in  \mathrm{B}\left( {{x}_{0},\rho }\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon ,
\]

en particulier

> in particular

\[
\forall x \in  E,\mathrm{\;d}\left( {{x}_{0}, x}\right)  < \rho ,\;\delta \left( {f\left( x\right) , f\left( {x}_{0}\right) }\right)  < \varepsilon ,
\]

ce qui montre la continuité de \( f \) en \( {x}_{0} \) .

> which shows the continuity of \( f \) at \( {x}_{0} \) .

b) Montrons que \( {B}_{\varepsilon } = E \smallsetminus {A}_{\varepsilon } = \left\{ {x \in E \mid \omega \left( {f, x}\right) < \varepsilon }\right\} \) est ouvert. Soit \( {x}_{0} \in {B}_{\varepsilon } \) . On a \( \omega \left( {f,{x}_{0}}\right) < \varepsilon \) donc il existe \( \rho > 0 \) tel que \( \mathop{\sup }\limits_{{x, y \in \mathrm{B}\left( {{x}_{0},\rho }\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \) . Considérons maintenant \( {x}_{1} \in \mathrm{B}\left( {{x}_{0},\rho }\right) \) , et \( r = \rho - \mathrm{d}\left( {{x}_{0},{x}_{1}}\right) \) . On a \( \mathrm{B}\left( {{x}_{1}, r}\right) \subset \mathrm{B}\left( {{x}_{0},\rho }\right) \) donc \( \omega \left( {f,{x}_{1}}\right) \leq \; \mathop{\sup }\limits_{{x, y \in \mathrm{B}\left( {{x}_{1}, r}\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \) , donc \( {x}_{1} \in {B}_{\varepsilon } \) . Ainsi, \( {B}_{\varepsilon } \) est ouvert.

> b) Let us show that \( {B}_{\varepsilon } = E \smallsetminus {A}_{\varepsilon } = \left\{ {x \in E \mid \omega \left( {f, x}\right) < \varepsilon }\right\} \) is open. Let \( {x}_{0} \in {B}_{\varepsilon } \) . We have \( \omega \left( {f,{x}_{0}}\right) < \varepsilon \) so there exists \( \rho > 0 \) such that \( \mathop{\sup }\limits_{{x, y \in \mathrm{B}\left( {{x}_{0},\rho }\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \) . Now consider \( {x}_{1} \in \mathrm{B}\left( {{x}_{0},\rho }\right) \) , and \( r = \rho - \mathrm{d}\left( {{x}_{0},{x}_{1}}\right) \) . We have \( \mathrm{B}\left( {{x}_{1}, r}\right) \subset \mathrm{B}\left( {{x}_{0},\rho }\right) \) so \( \omega \left( {f,{x}_{1}}\right) \leq \; \mathop{\sup }\limits_{{x, y \in \mathrm{B}\left( {{x}_{1}, r}\right) }}\delta \left( {f\left( x\right) , f\left( y\right) }\right) < \varepsilon \) , thus \( {x}_{1} \in {B}_{\varepsilon } \) . Therefore, \( {B}_{\varepsilon } \) is open.

L’application \( {x}_{0} \mapsto \omega \left( {f,{x}_{0}}\right) \) n’est pas forcément continue. Par exemple, la fonction \( f \) de \( \mathbb{R} \) dans \( \mathbb{R} \) nulle partout sauf en 0 où elle vaut 1, vérifie \( \omega \left( {f, x}\right) = f\left( x\right) \) .

> The map \( {x}_{0} \mapsto \omega \left( {f,{x}_{0}}\right) \) is not necessarily continuous. For example, the function \( f \) from \( \mathbb{R} \) to \( \mathbb{R} \) that is zero everywhere except at 0 where it equals 1, satisfies \( \omega \left( {f, x}\right) = f\left( x\right) \) .

c) C'est immédiat car

> c) This is immediate because

\[
\left( {f\text{ est continue en }{x}_{0}}\right)  \Leftrightarrow  \left( {\omega \left( {f,{x}_{0}}\right)  = 0}\right)  \Leftrightarrow  \left( {\forall n \in  {\mathbb{N}}^{ * },\omega \left( {f,{x}_{0}}\right)  < \frac{1}{n}}\right)
\]

\[
\Leftrightarrow  \left( {\forall n \in  {\mathbb{N}}^{ * },{x}_{0} \notin  {A}_{1/n}}\right)  \Leftrightarrow  \left( {{x}_{0} \notin  { \cup  }_{n \in  {\mathbb{N}}^{ * }}{A}_{1/n}}\right) .
\]

d) Supposons le contraire. Alors

> d) Suppose the contrary. Then

\[
\forall n \in  {\mathbb{N}}^{ * },\exists \left( {{x}_{n},{y}_{n}}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {{x}_{n},{y}_{n}}\right)  < \frac{1}{n}\;\text{ et }\;\delta \left( {f\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right)  \geq  \varepsilon .
\]

La suite \( \left( {{x}_{n},{y}_{n}}\right) \) prend ses valeurs dans le compact \( {E}^{2} \) , on peut donc en extraire une sous-suite convergente \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \) dont nous noterons \( \left( {x, y}\right) \) la limite. On a \( x = y \) car pour tout \( n \) , \( \mathrm{d}\left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) < 1/\varphi \left( n\right) \) . Or \( \omega \left( {f, x}\right) < \varepsilon \) donc

> The sequence \( \left( {{x}_{n},{y}_{n}}\right) \) takes its values in the compact set \( {E}^{2} \) , so we can extract a convergent subsequence \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \) whose limit we denote by \( \left( {x, y}\right) \) . We have \( x = y \) because for all \( n \) , \( \mathrm{d}\left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) < 1/\varphi \left( n\right) \) . However, \( \omega \left( {f, x}\right) < \varepsilon \) so

\[
\exists \rho  > 0,\forall \left( {z,{z}^{\prime }}\right)  \in  \mathrm{B}{\left( x,\rho \right) }^{2},\;\delta \left( {f\left( z\right) , f\left( {z}^{\prime }\right) }\right)  < \varepsilon .
\]

(*)

> Comme \( \left( {x}_{\varphi \left( n\right) }\right) \) et \( \left( {y}_{\varphi \left( n\right) }\right) \) convergent vers \( x \) , il existe \( n \in {\mathbb{N}}^{ * } \) tel que \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \in \mathrm{B}{\left( x,\rho \right) }^{2} \) . Ceci est absurde d’après (*) car par hypothèse, \( \delta \left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq \varepsilon \) .

Since \( \left( {x}_{\varphi \left( n\right) }\right) \) and \( \left( {y}_{\varphi \left( n\right) }\right) \) converge to \( x \) , there exists \( n \in {\mathbb{N}}^{ * } \) such that \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \in \mathrm{B}{\left( x,\rho \right) }^{2} \) . This is absurd according to (*) because by hypothesis, \( \delta \left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq \varepsilon \) .

> Remarque. Le résultat de la partie d) généralise le théorème de Heine, et est de nature proche du résultat de la question d) de l'exercice 7 page 36.

Remark. The result of part d) generalizes the Heine theorem, and is similar in nature to the result of question d) of exercise 7 on page 36.

> Problem 11 (PARTIES NÉGLIGEABLES DE R, ENSEMBLE TRIADIQUE DE CANTOR). \( 1/ \) Pour tout intervalle de \( \mathbb{R} \) ouvert borné \( I = \rbrack a, b\lbrack \) , on note \( \ell \left( I\right) = b - a \) . Une partie

Problem 11 (NEGLIGIBLE SUBSETS OF R, CANTOR TERNARY SET). \( 1/ \) For any bounded open interval \( \mathbb{R} \) \( I = \rbrack a, b\lbrack \) , we denote \( \ell \left( I\right) = b - a \) . A subset

> \( A \) de \( \mathbb{R} \) est dite négligeable si pour tout \( \varepsilon > 0 \) , il existe une famille au plus dénombrable \( {\left( {I}_{n}\right) }_{n \in J} \) d’intervalles ouverts bornés de \( \mathbb{R} \) telle que

\( A \) of \( \mathbb{R} \) is said to be negligible if for every \( \varepsilon > 0 \) , there exists an at most countable family \( {\left( {I}_{n}\right) }_{n \in J} \) of bounded open intervals of \( \mathbb{R} \) such that

\[
\text{ (ii) }\sum \ell \left( {I}_{n}\right) \text{ converge et }\mathop{\sum }\limits_{{n \in  J}}\ell \left( {I}_{n}\right)  \leq  \varepsilon \text{ . }
\]

a) Montrer qu'une réunion au plus dénombrable de parties négligeables est négligeable.

> a) Show that an at most countable union of negligible sets is negligible.

b) Montrer que \( \mathbb{Q} \) est une partie négligeable de \( \mathbb{R} \) .

> b) Show that \( \mathbb{Q} \) is a negligible subset of \( \mathbb{R} \) .

c) Si \( A \) est une partie négligeable de \( \mathbb{R} \) , montrer que \( A \) est d’intérieur vide.

> c) If \( A \) is a negligible subset of \( \mathbb{R} \) , show that \( A \) has an empty interior.

d) L’ensemble \( \mathbb{R} \smallsetminus \mathbb{Q} \) est-il négligeable ?

> d) Is the set \( \mathbb{R} \smallsetminus \mathbb{Q} \) negligible?

2/ (Ensemble triadique de Cantor.) Soit \( I = \left\lbrack {0,1}\right\rbrack \) . On construit une suite de parties \( {\left( {K}_{n}\right) }_{n \in \mathbb{N}} \) de \( I \) par récurrence, comme suit.

> 2/ (Cantor ternary set.) Let \( I = \left\lbrack {0,1}\right\rbrack \) . We construct a sequence of subsets \( {\left( {K}_{n}\right) }_{n \in \mathbb{N}} \) of \( I \) by induction, as follows.

- On prend \( {K}_{0} = I \) .

> - We take \( {K}_{0} = I \) .

- \( {K}_{n} \) étant une réunion finie de segments disjoints : \( {K}_{n} = { \cup  }_{k}\left\lbrack  {{a}_{k},{b}_{k}}\right\rbrack \) , on construit

> - Given \( {K}_{n} \) as a finite union of disjoint closed intervals: \( {K}_{n} = { \cup  }_{k}\left\lbrack  {{a}_{k},{b}_{k}}\right\rbrack \) , we construct

\[
{K}_{n + 1} = \mathop{\bigcup }\limits_{k}\left( {\left\lbrack  {{a}_{k},{a}_{k} + \frac{{b}_{k} - {a}_{k}}{3}}\right\rbrack   \cup  \left\lbrack  {{a}_{k} + 2\frac{{b}_{k} - {a}_{k}}{3},{b}_{k}}\right\rbrack  }\right) .
\]

On pose alors \( K = { \cap }_{n \in \mathbb{N}}{K}_{n} \) (ensemble triadique de Cantor).

> We then define \( K = { \cap }_{n \in \mathbb{N}}{K}_{n} \) (Cantor ternary set).

a) Montrer que \( K \) est négligeable.

> a) Show that \( K \) is negligible.

b) Soit \( x \in \lbrack 0,1\lbrack \) . Donner une condition nécessaire et suffisante sur le développement en base 3 de \( x \) pour que \( x \in K \) .

> b) Let \( x \in \lbrack 0,1\lbrack \) . Give a necessary and sufficient condition on the base-3 expansion of \( x \) for \( x \in K \) .

c) Montrer que \( K \) est un fermé, d’intérieur vide, sans point isolé, et qu’il a la puissance du continu.

> c) Show that \( K \) is a closed set, with an empty interior, no isolated points, and that it has the cardinality of the continuum.

Solution. 1/ Remarquons tout d'abord que la convergence et la somme d'une série à termes positifs ne dépend pas de l'ordre de sommation (voir le théorème 8 page 216), ce qui donne un sens à \( \mathop{\sum }\limits_{{n \in J}}\ell \left( {I}_{n}\right) \) .

> Solution. 1/ Let us first note that the convergence and sum of a series with positive terms do not depend on the order of summation (see theorem 8 page 216), which gives meaning to \( \mathop{\sum }\limits_{{n \in J}}\ell \left( {I}_{n}\right) \) .

a) Soit \( {\left( {A}_{j}\right) }_{j \in J} \) une famille au plus dénombrable de parties négligeables (avec \( J \subset \mathbb{N} \) ). Soit \( \varepsilon > 0 \) . Pour tout \( j \in J \) , on peut écrire \( {A}_{j} \subset { \cup }_{n \in {K}_{j}}{I}_{n, j} \) où les \( {I}_{n, j} \) sont des intervalles de \( \mathbb{R} \) ouverts bornés, \( {K}_{j} \) est au plus dénombrable et où

> a) Let \( {\left( {A}_{j}\right) }_{j \in J} \) be an at most countable family of negligible sets (with \( J \subset \mathbb{N} \) ). Let \( \varepsilon > 0 \) . For every \( j \in J \) , we can write \( {A}_{j} \subset { \cup }_{n \in {K}_{j}}{I}_{n, j} \) where the \( {I}_{n, j} \) are bounded open intervals of \( \mathbb{R} \) , \( {K}_{j} \) is at most countable and where

\[
\mathop{\sum }\limits_{{n \in  {K}_{j}}}\ell \left( {I}_{n, j}\right)  < \varepsilon /{2}^{j + 1}
\]

Notons \( \Gamma = { \cup }_{j \in J}\{ j\} \times {K}_{j} \) . L’ensemble \( \Gamma \) est au plus dénombrable (réunion au plus dénombrable d’ensembles au plus dénombrables), et on a \( \mathop{\bigcup }\limits_{{j \in J}}{A}_{j} \subset \mathop{\bigcup }\limits_{{\left( {j, n}\right) \in \Gamma }}{I}_{n, j} \) avec

> Let us denote \( \Gamma = { \cup }_{j \in J}\{ j\} \times {K}_{j} \) . The set \( \Gamma \) is at most countable (at most countable union of at most countable sets), and we have \( \mathop{\bigcup }\limits_{{j \in J}}{A}_{j} \subset \mathop{\bigcup }\limits_{{\left( {j, n}\right) \in \Gamma }}{I}_{n, j} \) with

\[
\mathop{\sum }\limits_{{\left( {j, n}\right)  \in  \Gamma }}\ell \left( {I}_{n, j}\right)  = \mathop{\sum }\limits_{{j \in  J}}\left\lbrack  {\mathop{\sum }\limits_{{n \in  {K}_{j}}}\ell \left( {I}_{n, j}\right) }\right\rbrack   \leq  \mathop{\sum }\limits_{{j \in  J}}\frac{\varepsilon }{{2}^{j + 1}} \leq  \mathop{\sum }\limits_{{j = 0}}^{{+\infty }}\frac{\varepsilon }{{2}^{j + 1}} = \varepsilon .
\]

Ainsi, \( A = { \cup }_{j \in J}{A}_{j} \) est négligeable.

> Thus, \( A = { \cup }_{j \in J}{A}_{j} \) is negligible.

b) Un singleton \( \left\{ {x}_{0}\right\} \) est négligeable car pour tout \( \varepsilon > 0,\left\{ {x}_{0}\right\} \subset \rbrack {x}_{0} - \varepsilon /2,{x}_{0} + \varepsilon /2\lbrack \) . Donc \( \mathbb{Q} \) , réunion dénombrable de singletons, est négligeable d'après a).

> b) A singleton \( \left\{ {x}_{0}\right\} \) is negligible because for all \( \varepsilon > 0,\left\{ {x}_{0}\right\} \subset \rbrack {x}_{0} - \varepsilon /2,{x}_{0} + \varepsilon /2\lbrack \) . Therefore \( \mathbb{Q} \) , a countable union of singletons, is negligible according to a).

c) Soit \( A \) une partie négligeable de \( \mathbb{R} \) . Raisonnons par l’absurde en supposant que \( A \) n’est pas d’intérieur vide. Alors il existe un segment \( I = \left\lbrack {a, b}\right\rbrack \) inclus dans \( A \) tel que \( a < b \) . Comme \( A \) est négligeable, il existe une famille au plus dénombrable \( {\left( {I}_{n}\right) }_{n \in J} \) d’intervalles ouverts bornés qui recouvre \( A \) , tel que \( \mathop{\sum }\limits_{{n \in J}}\ell \left( {I}_{n}\right) < b - a \) . Cette famille recouvre aussi le compact \( \left\lbrack {a, b}\right\rbrack \) , dont on peut extraire un sous-recouvrement fini \( {\left( {I}_{{n}_{i}}\right) }_{1 \leq i \leq p} \) qui vérifie

> c) Let \( A \) be a negligible subset of \( \mathbb{R} \) . Let us reason by contradiction by assuming that \( A \) does not have an empty interior. Then there exists a segment \( I = \left\lbrack {a, b}\right\rbrack \) included in \( A \) such that \( a < b \) . Since \( A \) is negligible, there exists an at most countable family \( {\left( {I}_{n}\right) }_{n \in J} \) of bounded open intervals that covers \( A \) , such that \( \mathop{\sum }\limits_{{n \in J}}\ell \left( {I}_{n}\right) < b - a \) . This family also covers the compact set \( \left\lbrack {a, b}\right\rbrack \) , from which we can extract a finite sub-covering \( {\left( {I}_{{n}_{i}}\right) }_{1 \leq i \leq p} \) that satisfies

\[
\mathop{\sum }\limits_{{i = 1}}^{p}\ell \left( {I}_{{n}_{i}}\right)  \leq  \mathop{\sum }\limits_{{n \in  J}}\ell \left( {I}_{n}\right)  < b - a.
\]

Ceci est impossible, car comme \( \left\lbrack {a, b}\right\rbrack \subset { \cup }_{1 \leq i \leq n}{I}_{{n}_{i}} \) , on a \( {\chi }_{\left\lbrack a, b\right\rbrack } \leq \mathop{\sum }\limits_{{i = 1}}^{p}{\chi }_{{I}_{{n}_{i}}} \) (où \( {\chi }_{P} \) désigne la fonction caractéristique de \( P \) ), donc

> This is impossible, because as \( \left\lbrack {a, b}\right\rbrack \subset { \cup }_{1 \leq i \leq n}{I}_{{n}_{i}} \) , we have \( {\chi }_{\left\lbrack a, b\right\rbrack } \leq \mathop{\sum }\limits_{{i = 1}}^{p}{\chi }_{{I}_{{n}_{i}}} \) (where \( {\chi }_{P} \) denotes the characteristic function of \( P \) ), therefore

\[
{\int }_{\mathbb{R}}{\chi }_{\left\lbrack  a, b\right\rbrack  } = b - a \leq  {\int }_{\mathbb{R}}\mathop{\sum }\limits_{{i = 1}}^{p}{\chi }_{{I}_{{n}_{i}}} = \mathop{\sum }\limits_{{i = 1}}^{p}\ell \left( {I}_{{n}_{i}}\right) .
\]

d) Non ! S'il était négligeable, alors \( \mathbb{R} = \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \cup \mathbb{Q} \) serait négligeable (d'après a) et b)), ce qui est absurde d’après c) car l’intérieur de \( \mathbb{R} \) est non vide.

> d) No! If it were negligible, then \( \mathbb{R} = \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \cup \mathbb{Q} \) would be negligible (according to a) and b)), which is absurd according to c) because the interior of \( \mathbb{R} \) is non-empty.

2 / a) On voit facilement (par récurrence sur \( n \) ) que \( {K}_{n} \) est la réunion de \( {2}^{n} \) intervalles fermés de longueur \( {3}^{-n} \) .

> 2 / a) It is easy to see (by induction on \( n \) ) that \( {K}_{n} \) is the union of \( {2}^{n} \) closed intervals of length \( {3}^{-n} \) .

Soit \( \varepsilon > 0 \) et soit \( N \in {\mathbb{N}}^{ * } \) tel que \( {\left( 2/3\right) }^{N} < \varepsilon /2 \) . Comme on l’a vu, on peut écrire \( {K}_{N} = \; { \cup }_{1 \leq n \leq {2}^{N}}\left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) avec \( {b}_{n} - {a}_{n} = {3}^{-N} \) pour tout \( n \) . En posant \( {I}_{n} = \left\rbrack {{a}_{n} - \frac{\varepsilon }{4 \cdot {2}^{N}},{b}_{n} + \frac{\varepsilon }{4 \cdot {2}^{N}}}\right\lbrack \) , on a \( K \subset {K}_{N} \subset { \cup }_{1 \leq n \leq {2}^{N}}{I}_{n} \) , et

> Let \( \varepsilon > 0 \) and let \( N \in {\mathbb{N}}^{ * } \) be such that \( {\left( 2/3\right) }^{N} < \varepsilon /2 \) . As we have seen, we can write \( {K}_{N} = \; { \cup }_{1 \leq n \leq {2}^{N}}\left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) with \( {b}_{n} - {a}_{n} = {3}^{-N} \) for all \( n \) . By setting \( {I}_{n} = \left\rbrack {{a}_{n} - \frac{\varepsilon }{4 \cdot {2}^{N}},{b}_{n} + \frac{\varepsilon }{4 \cdot {2}^{N}}}\right\lbrack \) , we have \( K \subset {K}_{N} \subset { \cup }_{1 \leq n \leq {2}^{N}}{I}_{n} \) , and

\[
\mathop{\sum }\limits_{{n = 1}}^{{2}^{N}}\ell \left( {I}_{n}\right)  = \mathop{\sum }\limits_{{n = 1}}^{{2}^{N}}\left\lbrack  {\left( {{b}_{n} - {a}_{n}}\right)  + \frac{\varepsilon }{2 \cdot  {2}^{N}}}\right\rbrack   = {\left( \frac{2}{3}\right) }^{N} + \frac{\varepsilon }{2} < \varepsilon ,
\]

d'où le résultat.

> hence the result.

b) Une récurrence facile donne

> b) An easy induction gives

\[
\forall n \in  \mathbb{N},{K}_{n} = \mathop{\bigcup }\limits_{{{\varepsilon }_{1} \in  \{ 0,2\} ,\cdots ,{\varepsilon }_{n} \in  \{ 0,2\} }}\left\lbrack  {\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{\varepsilon }_{k}}{{3}^{k}},\frac{1}{{3}^{n}} + \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{\varepsilon }_{k}}{{3}^{k}}}\right\rbrack  .
\]

(*)

> Ceci étant, soit \( x \in \lbrack 0,1\lbrack \) . Considérons son développement en base \( 3 : x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) , avec \( {\alpha }_{k} \in \{ 0,1,2\} \) , la suite \( \left( {\alpha }_{k}\right) \) n’étant pas stationnaire à 2 à partir d’un certain rang (propriété des développements tri-adiques). Si les \( {\varepsilon }_{k} \) sont dans \( \{ 0,2\} \) , on a l’équivalence

Given this, let \( x \in \lbrack 0,1\lbrack \) . Consider its expansion in base \( 3 : x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) , with \( {\alpha }_{k} \in \{ 0,1,2\} \) , the sequence \( \left( {\alpha }_{k}\right) \) not being stationary at 2 from a certain rank (property of triadic expansions). If the \( {\varepsilon }_{k} \) are in \( \{ 0,2\} \) , we have the equivalence

\[
\mathop{\sum }\limits_{{k = 1}}^{n}\frac{{\varepsilon }_{k}}{{3}^{k}} \leq  x < \frac{1}{{3}^{n}} + \mathop{\sum }\limits_{{k = 1}}^{n}\frac{{\varepsilon }_{k}}{{3}^{k}}\; \Leftrightarrow  \;\forall k \in  \{ 1,\ldots , n\} ,\;{\alpha }_{k} = {\varepsilon }_{k},
\]

et compte tenu du fait que les réels de \( \lbrack 0,1\lbrack \) de la forme \( 1/{3}^{n} + \mathop{\sum }\limits_{{k = 1}}^{n}{\varepsilon }_{k}/{3}^{k} \) (avec \( {\varepsilon }_{k} \in \{ 0,2\} \) ) sont aussi ceux de la forme

> and taking into account the fact that the reals of \( \lbrack 0,1\lbrack \) of the form \( 1/{3}^{n} + \mathop{\sum }\limits_{{k = 1}}^{n}{\varepsilon }_{k}/{3}^{k} \) (with \( {\varepsilon }_{k} \in \{ 0,2\} \) ) are also those of the form

\[
\mathop{\sum }\limits_{{k = 1}}^{p}\frac{{\beta }_{k}}{{3}^{k}}\;\text{ avec }\;p \leq  n,\;{\beta }_{k} \in  \{ 0,2\} \;\text{ pour }\;1 \leq  k \leq  p - 1,\;\text{ et }\;{\beta }_{p} = 1,
\]

on en déduit grâce à (*) que

> we deduce from (*) that

\[
\left( {x \in  K}\right)  \Leftrightarrow  \left( {\forall n, x \in  {K}_{n}}\right)  \Leftrightarrow  \left( {\forall k,{\alpha }_{k} \in  \{ 0,2\} \text{ ou }\exists p \in  \mathbb{N}, x = \mathop{\sum }\limits_{{k = 1}}^{p}\frac{{\varepsilon }_{k}}{{3}^{k}} + \frac{1}{{3}^{p + 1}},{\varepsilon }_{k} \in  \{ 0,2\} }\right) .
\]

En d’autres termes, \( x \in K \) si et seulement si tous les termes \( \left( {\alpha }_{k}\right) \) du développement de \( x \) en base 3 sont dans \( \{ 0,2\} \) ou s’il existe un entier naturel \( p \) tel que \( {\alpha }_{k} \in \{ 0,2\} \) pour \( k \leq p,{\alpha }_{p + 1} = 1 \) et \( {\alpha }_{k} = 0 \) pour \( k > p + 1 \) .

> In other words, \( x \in K \) if and only if all terms \( \left( {\alpha }_{k}\right) \) of the expansion of \( x \) in base 3 are in \( \{ 0,2\} \) or if there exists a natural integer \( p \) such that \( {\alpha }_{k} \in \{ 0,2\} \) for \( k \leq p,{\alpha }_{p + 1} = 1 \) and \( {\alpha }_{k} = 0 \) for \( k > p + 1 \) .

c) L’ensemble \( K \) est une intersection de fermés, c’est donc un fermé.

> c) The set \( K \) is an intersection of closed sets, it is therefore a closed set.

Il est d'intérieur vide car négligeable. On pouvait aussi remarquer, grâce à la question précédente, que pour tout \( x \in K \) , pour tout \( N \in \mathbb{N} \) , il existe \( n \geq N \) tel que \( x + 1/{3}^{n} \notin K \) .

> It has an empty interior because it is negligible. One could also note, thanks to the previous question, that for all \( x \in K \) , for all \( N \in \mathbb{N} \) , there exists \( n \geq N \) such that \( x + 1/{3}^{n} \notin K \) .

Aucun point de \( K \) n’est isolé dans \( K \) . En effet, deux cas se présentent.

> No point of \( K \) is isolated in \( K \) . Indeed, two cases arise.

- Si le développement en base 3 de \( x \in  K \) est de la forme \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) avec \( {\alpha }_{k} \in  \{ 0,2\} \) pour tout \( k \) , alors la suite \( \left( {\alpha }_{k}\right) \) n’étant jamais stationnaire à 2 à partir d’un certain rang, on s'aperçoit que

> - If the base 3 expansion of \( x \in  K \) is of the form \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) with \( {\alpha }_{k} \in  \{ 0,2\} \) for all \( k \) , then the sequence \( \left( {\alpha }_{k}\right) \) never being stationary at 2 from a certain rank, we notice that

\[
\forall N \in  \mathbb{N},\exists n \geq  N,\;x + \frac{2}{{3}^{n}} \in  K.
\]

- Si \( x \) est de la forme \( \mathop{\sum }\limits_{{k = 1}}^{p}{\varepsilon }_{k}/{3}^{k} + 1/{3}^{p + 1} \) avec \( {\varepsilon }_{k} \in  \{ 0,2\} \) , alors pour tout \( n \geq  p + 1 \) ,

> - If \( x \) is of the form \( \mathop{\sum }\limits_{{k = 1}}^{p}{\varepsilon }_{k}/{3}^{k} + 1/{3}^{p + 1} \) with \( {\varepsilon }_{k} \in  \{ 0,2\} \) , then for all \( n \geq  p + 1 \) ,

\[
x - \frac{1}{{3}^{n}} = \mathop{\sum }\limits_{{k = 1}}^{p}\frac{{\varepsilon }_{k}}{{3}^{k}} + \mathop{\sum }\limits_{{k = p + 1}}^{{n - 1}}\frac{2}{{3}^{k}} \in  K.
\]

L’ensemble \( K \) a la puissance du continu. En effet, l’application \( \varphi \) de \( \lbrack 0,1\lbrack \) dans \( K \) qui à tout \( x \) dont le développement \( {di} \) -adique est \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\varepsilon }_{k}/{2}^{k} \) associe \( \varphi \left( x\right) = 2\mathop{\sum }\limits_{{k = 1}}^{\infty }{\varepsilon }_{k}/{3}^{k} \) est injective.

> The set \( K \) has the cardinality of the continuum. Indeed, the map \( \varphi \) from \( \lbrack 0,1\lbrack \) to \( K \) which associates \( \varphi \left( x\right) = 2\mathop{\sum }\limits_{{k = 1}}^{\infty }{\varepsilon }_{k}/{3}^{k} \) to any \( x \) whose \( {di} \) -adic expansion is \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\varepsilon }_{k}/{2}^{k} \) is injective.

Remarque. A la question \( 2/\mathrm{b} \) ), on aurait pu montrer que \( x \in K \) si et seulement s’il existe une suite \( \left( {\alpha }_{k}\right) \in \{ 0,2{\} }^{{\mathbb{N}}^{ * }} \) telle que \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) . Mais les écritures de cette forme ne sont pas forcément un développement en base 3, car dans un tel développement, la suite des termes du développement ne peut pas être stationnaire à 2 à partir d'un certain rang (cette contrainte permet d'avoir l'unicité de l'écriture triadique).

> Remark. In question \( 2/\mathrm{b} \) ), one could have shown that \( x \in K \) if and only if there exists a sequence \( \left( {\alpha }_{k}\right) \in \{ 0,2{\} }^{{\mathbb{N}}^{ * }} \) such that \( x = \mathop{\sum }\limits_{{k = 1}}^{\infty }{\alpha }_{k}/{3}^{k} \) . However, expressions of this form are not necessarily a base-3 expansion, because in such an expansion, the sequence of terms cannot be stationary at 2 from a certain rank onwards (this constraint ensures the uniqueness of the triadic representation).

- L'ensemble de Cantor possède des propriétés intéressantes qui sont des contre-exemples à beaucoup de fausses intuitions.

> - The Cantor set possesses interesting properties that serve as counterexamples to many false intuitions.

- Dans la théorie de la mesure de Lebesgue, les ensembles négligeables sont les ensembles de mesure nulle.

> - In Lebesgue measure theory, negligible sets are sets of measure zero.

- Dans la même veine, signalons l'escalier de Cantor-Lebesgue, introduite par Lebesgue, qui est le graphe d’une fonction continue \( \psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \left\lbrack  {0,1}\right\rbrack \) , vérifiant \( \psi \left( 0\right)  = 0 \) et \( \psi \left( 1\right)  = 1 \) , dérivable presque partout (c'est-à-dire sur le complémentaire d'une partie négligeable) et de dérivée presque partout nulle. On l'appelle aussi parfois escalier du diable car il est continu, a presque partout une tangente horizontale, et pourtant il monte. Cette fonction peut être définie sur l’ensemble triadique de Cantor \( K \) par \( \psi \left( {\mathop{\sum }\limits_{k}2{\beta }_{k}/{3}^{k}}\right)  = \mathop{\sum }\limits_{k}{\beta }_{k}/{2}^{k} \) (avec \( {\beta }_{k} \in  \{ 0,1\} \) ), et elle est localement constante sur le complémentaire de \( K \) .

> - In the same vein, let us note the Cantor-Lebesgue function, introduced by Lebesgue, which is the graph of a continuous function \( \psi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \left\lbrack  {0,1}\right\rbrack \) , satisfying \( \psi \left( 0\right)  = 0 \) and \( \psi \left( 1\right)  = 1 \) , differentiable almost everywhere (that is, on the complement of a negligible set) and with a derivative equal to zero almost everywhere. It is also sometimes called the devil's staircase because it is continuous, has a horizontal tangent almost everywhere, and yet it rises. This function can be defined on the Cantor triadic set \( K \) by \( \psi \left( {\mathop{\sum }\limits_{k}2{\beta }_{k}/{3}^{k}}\right)  = \mathop{\sum }\limits_{k}{\beta }_{k}/{2}^{k} \) (with \( {\beta }_{k} \in  \{ 0,1\} \) ), and it is locally constant on the complement of \( K \) .

Problem 12 (THÉORÉME DE PROLONGEMENT DE TIETZE-URYSOHN). Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique, \( A \) un fermé de \( E \) , et \( f : A \rightarrow \mathbb{R} \) une application continue et bornée. Montrer l’existence d’une fonction \( g : E \rightarrow \mathbb{R} \) , continue, telle que \( {g}_{\mid A} = f \) et

> Problem 12 (TIETZE-URYSOHN EXTENSION THEOREM). Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space, \( A \) a closed subset of \( E \) , and \( f : A \rightarrow \mathbb{R} \) a continuous and bounded map. Show the existence of a continuous function \( g : E \rightarrow \mathbb{R} \) such that \( {g}_{\mid A} = f \) and

\[
\mathop{\sup }\limits_{{x \in  E}}g\left( x\right)  = \mathop{\sup }\limits_{{y \in  A}}f\left( y\right) \;\text{ et }\;\mathop{\inf }\limits_{{x \in  E}}g\left( x\right)  = \mathop{\inf }\limits_{{y \in  A}}f\left( y\right) .
\]

(Indication. Se ramener au cas où \( \mathop{\inf }\limits_{{y \in A}}f\left( y\right) = 1,\mathop{\sup }\limits_{{y \in A}}f\left( y\right) = 2 \) , et prendre \( g = f \) sur \( A \) et \( g\left( x\right) = \frac{1}{\mathrm{\;d}\left( {x, A}\right) }\mathop{\inf }\limits_{{y \in A}}\left\lbrack {f\left( y\right) \mathrm{d}\left( {x, y}\right) }\right\rbrack \) si \( x \notin A.) \)

> (Hint. Reduce to the case where \( \mathop{\inf }\limits_{{y \in A}}f\left( y\right) = 1,\mathop{\sup }\limits_{{y \in A}}f\left( y\right) = 2 \) , and take \( g = f \) on \( A \) and \( g\left( x\right) = \frac{1}{\mathrm{\;d}\left( {x, A}\right) }\mathop{\inf }\limits_{{y \in A}}\left\lbrack {f\left( y\right) \mathrm{d}\left( {x, y}\right) }\right\rbrack \) if \( x \notin A.) \)

Solution. Si \( f \) est constante, le résultat est évident, sinon en remplaçant \( f \) par \( {\alpha f} + \beta \) avec \( \alpha \neq 0 \) et \( \beta \) des réels bien choisis, on peut supposer \( \mathop{\inf }\limits_{{y \in A}}f\left( y\right) = 1 \) et \( \mathop{\sup }\limits_{{y \in A}}f\left( y\right) = 2 \) . Suivons l’indication et construisons la fonction \( g : E \rightarrow \mathbb{R} \) définie par \( g\left( x\right) = f\left( x\right) \) si \( x \in A \) et

> Solution. If \( f \) is constant, the result is obvious; otherwise, by replacing \( f \) with \( {\alpha f} + \beta \) where \( \alpha \neq 0 \) and \( \beta \) are well-chosen real numbers, we can assume \( \mathop{\inf }\limits_{{y \in A}}f\left( y\right) = 1 \) and \( \mathop{\sup }\limits_{{y \in A}}f\left( y\right) = 2 \) . Let us follow the hint and construct the function \( g : E \rightarrow \mathbb{R} \) defined by \( g\left( x\right) = f\left( x\right) \) if \( x \in A \) and

\[
\forall x \in  E \smallsetminus  A,\;g\left( x\right)  = \frac{h\left( x\right) }{\mathrm{d}\left( {x, A}\right) },\;\text{ avec }\;h\left( x\right)  = \mathop{\inf }\limits_{{y \in  A}}\left( {f\left( y\right) \mathrm{d}\left( {x, y}\right) }\right)
\]

(*)

> (cette dernière expression est bien définie, car \( A \) étant fermé, on a \( \mathrm{d}\left( {x, A}\right) = 0 \) si et seulement si \( x \in A) \) .

(this last expression is well-defined, because since \( A \) is closed, we have \( \mathrm{d}\left( {x, A}\right) = 0 \) if and only if \( x \in A) \) .

> Les inégalités \( 1 \leq f\left( x\right) \leq 2 \) pour tout \( x \in A \) montrent que \( 1 \leq g\left( x\right) \leq 2 \) pour tout \( x \in E \) . Comme \( {g}_{\mid A} = f \) , on a même inf \( {}_{x \in E}g\left( x\right) = 1 \) et \( \mathop{\sup }\limits_{{x \in E}}g\left( x\right) = 2 \) .

The inequalities \( 1 \leq f\left( x\right) \leq 2 \) for all \( x \in A \) show that \( 1 \leq g\left( x\right) \leq 2 \) for all \( x \in E \) . Since \( {g}_{\mid A} = f \) , we even have inf \( {}_{x \in E}g\left( x\right) = 1 \) and \( \mathop{\sup }\limits_{{x \in E}}g\left( x\right) = 2 \) .

> Il nous reste à montrer la continuité de \( g \) en tout point \( {x}_{0} \) de \( E \) . Nous allons traiter les cas \( {x}_{0} \in \overset{ \circ }{A} \) , puis \( {x}_{0} \in E \smallsetminus A \) , puis \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) .

It remains for us to show the continuity of \( g \) at every point \( {x}_{0} \) of \( E \) . We will treat the cases \( {x}_{0} \in \overset{ \circ }{A} \) , then \( {x}_{0} \in E \smallsetminus A \) , then \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) .

> (i) Si \( {x}_{0} \in \overset{ \circ }{A} \) , comme \( {g}_{\mid A} = f \) et que \( f \) est continue sur \( A, g \) est continue en \( {x}_{0} \) .

(i) If \( {x}_{0} \in \overset{ \circ }{A} \) , since \( {g}_{\mid A} = f \) and \( f \) is continuous on \( A, g \) is continuous at \( {x}_{0} \) .

> (ii) Supposons \( {x}_{0} \in E \smallsetminus A \) . Sur l’ouvert \( E \smallsetminus A \) , l’application \( g \) prend la forme (*), et comme \( x \mapsto \mathrm{d}\left( {x, A}\right) \) est continue (voir l’exercice 3, page 33), il nous suffit de montrer que \( h \) est continue en \( {x}_{0} \) . Soit \( r > 0 \) tel que \( \mathrm{B}\left( {{x}_{0}, r}\right) \subset E \smallsetminus A \) . Pour tout \( x \in \mathrm{B}\left( {{x}_{0}, r}\right) \) , pour tout \( y \in A \) ,

(ii) Suppose \( {x}_{0} \in E \smallsetminus A \) . On the open set \( E \smallsetminus A \) , the map \( g \) takes the form (*), and since \( x \mapsto \mathrm{d}\left( {x, A}\right) \) is continuous (see exercise 3, page 33), it suffices to show that \( h \) is continuous at \( {x}_{0} \) . Let \( r > 0 \) be such that \( \mathrm{B}\left( {{x}_{0}, r}\right) \subset E \smallsetminus A \) . For all \( x \in \mathrm{B}\left( {{x}_{0}, r}\right) \) , for all \( y \in A \) ,

\[
h\left( {x}_{0}\right)  \leq  f\left( y\right) \mathrm{d}\left( {{x}_{0}, y}\right)  \leq  f\left( y\right) \left( {\mathrm{d}\left( {{x}_{0}, x}\right)  + \mathrm{d}\left( {x, y}\right) }\right)  \leq  2\mathrm{\;d}\left( {{x}_{0}, x}\right)  + f\left( y\right) \mathrm{d}\left( {x, y}\right) ,
\]

et ceci étant vrai pour tout \( y \in A \) , on en déduit, en ne considérant que les termes des extrémités et en prenant la borne inférieure sur les \( y \in A \) , que \( h\left( {x}_{0}\right) \leq h\left( x\right) + 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \) . De même, \( h\left( x\right) \leq h\left( {x}_{0}\right) + 2\mathrm{\;d}\left( {x,{x}_{0}}\right) \) , donc finalement, \( \left| {h\left( {x}_{0}\right) - h\left( x\right) }\right| \leq 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \) , ce qui prouve la continuité de \( h \) en \( {x}_{0} \in E \smallsetminus A \) .

> and since this is true for all \( y \in A \) , we deduce, by considering only the terms at the ends and taking the infimum over \( y \in A \) , that \( h\left( {x}_{0}\right) \leq h\left( x\right) + 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \) . Similarly, \( h\left( x\right) \leq h\left( {x}_{0}\right) + 2\mathrm{\;d}\left( {x,{x}_{0}}\right) \) , so finally, \( \left| {h\left( {x}_{0}\right) - h\left( x\right) }\right| \leq 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \) , which proves the continuity of \( h \) at \( {x}_{0} \in E \smallsetminus A \) .

(iii) Il reste le cas où \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) . Soit \( \varepsilon > 0 \) . Comme \( f \) est continue en \( {x}_{0} \in A \) ,

> (iii) The case where \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) remains. Let \( \varepsilon > 0 \) . Since \( f \) is continuous at \( {x}_{0} \in A \) ,

\[
\exists r > 0,\forall y \in  A \cap  \mathrm{B}\left( {{x}_{0}, r}\right) ,\;\left| {f\left( y\right)  - f\left( {x}_{0}\right) }\right|  \leq  \varepsilon .
\]

Si \( x \in E \smallsetminus A \) et \( \mathrm{d}\left( {{x}_{0}, x}\right) \leq r/4 \) , on a, en notant \( C = A \cap \mathrm{B}\left( {{x}_{0}, r}\right) \) :

> If \( x \in E \smallsetminus A \) and \( \mathrm{d}\left( {{x}_{0}, x}\right) \leq r/4 \) , we have, by denoting \( C = A \cap \mathrm{B}\left( {{x}_{0}, r}\right) \) :

\[
\forall y \in  A \smallsetminus  C,\;\mathrm{\;d}\left( {x, y}\right)  \geq  \mathrm{d}\left( {{x}_{0}, y}\right)  - \mathrm{d}\left( {{x}_{0}, x}\right)  \geq  \frac{3r}{4},
\]

donc \( \mathop{\inf }\limits_{{y \in A \smallsetminus C}}f\left( y\right) \mathrm{d}\left( {x, y}\right) \geq {3r}/4 \) . D’autre part, \( f\left( {x}_{0}\right) \mathrm{d}\left( {{x}_{0}, x}\right) \leq 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \leq r/2 \) , donc

> therefore \( \mathop{\inf }\limits_{{y \in A \smallsetminus C}}f\left( y\right) \mathrm{d}\left( {x, y}\right) \geq {3r}/4 \) . On the other hand, \( f\left( {x}_{0}\right) \mathrm{d}\left( {{x}_{0}, x}\right) \leq 2\mathrm{\;d}\left( {{x}_{0}, x}\right) \leq r/2 \) , so

\[
\mathop{\inf }\limits_{{y \in  A}}f\left( y\right) \mathrm{d}\left( {x, y}\right)  = \mathop{\inf }\limits_{{y \in  C}}f\left( y\right) \mathrm{d}\left( {x, y}\right) ,
\]

et comme \( f\left( {x}_{0}\right) - \varepsilon \leq f\left( y\right) \leq f\left( {x}_{0}\right) + \varepsilon \) pour tout \( y \in C \) , on en déduit

> and since \( f\left( {x}_{0}\right) - \varepsilon \leq f\left( y\right) \leq f\left( {x}_{0}\right) + \varepsilon \) for all \( y \in C \) , we deduce

\[
\left( {f\left( {x}_{0}\right)  - \varepsilon }\right) \mathrm{d}\left( {x, A}\right)  \leq  \mathop{\inf }\limits_{{y \in  A}}\left( {f\left( y\right) \mathrm{d}\left( {x, y}\right) }\right)  \leq  \left( {f\left( {x}_{0}\right)  + \varepsilon }\right) \mathrm{d}\left( {x, A}\right) ,
\]

donc \( g\left( {x}_{0}\right) - \varepsilon \leq g\left( x\right) \leq g\left( {x}_{0}\right) + \varepsilon \) pour tout \( x \in E \smallsetminus A \) tel que \( \mathrm{d}\left( {{x}_{0}, x}\right) \leq r/4 \) . Ceci reste vrai si \( x \in A \) et \( \mathrm{d}\left( {x,{x}_{0}}\right) \leq r/4 \) car c’est vrai pour \( f \) . Ainsi, \( g \) est continue en \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) , d’où le résultat.

> therefore \( g\left( {x}_{0}\right) - \varepsilon \leq g\left( x\right) \leq g\left( {x}_{0}\right) + \varepsilon \) for all \( x \in E \smallsetminus A \) such that \( \mathrm{d}\left( {{x}_{0}, x}\right) \leq r/4 \) . This remains true if \( x \in A \) and \( \mathrm{d}\left( {x,{x}_{0}}\right) \leq r/4 \) because it is true for \( f \) . Thus, \( g \) is continuous at \( {x}_{0} \in \operatorname{Fr}\left( A\right) \) , hence the result.

Problem 13 (Continuité DES RACINES DE POLYNÔMES). On norme \( \mathbb{C}\left\lbrack X\right\rbrack \) en posant \( \begin{Vmatrix}{{a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n}}\end{Vmatrix} = \mathop{\sum }\limits_{{i = 0}}^{n}\left| {a}_{i}\right| . \)

> Problem 13 (CONTINUITY OF POLYNOMIAL ROOTS). We norm \( \mathbb{C}\left\lbrack X\right\rbrack \) by setting \( \begin{Vmatrix}{{a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n}}\end{Vmatrix} = \mathop{\sum }\limits_{{i = 0}}^{n}\left| {a}_{i}\right| . \)

1/ Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) un polynôme unitaire et \( \lambda \in \mathbb{C} \) une racine de \( P \) . Montrer que \( \left| \lambda \right| \leq \parallel P\parallel \) .

> 1/ Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) be a monic polynomial and \( \lambda \in \mathbb{C} \) a root of \( P \) . Show that \( \left| \lambda \right| \leq \parallel P\parallel \) .

2/ Soit \( n \in {\mathbb{N}}^{ * } \) et \( P = \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{n}}\right) \in \mathbb{C}\left\lbrack X\right\rbrack \) . Soit \( {\left( {P}_{m}\right) }_{m \in \mathbb{N}} \) une suite de polynômes unitaires de degré \( n \) qui tend vers \( P \) .

> 2/ Let \( n \in {\mathbb{N}}^{ * } \) and \( P = \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{n}}\right) \in \mathbb{C}\left\lbrack X\right\rbrack \) . Let \( {\left( {P}_{m}\right) }_{m \in \mathbb{N}} \) be a sequence of monic polynomials of degree \( n \) that converges to \( P \) .

a) Montrer que pour toute racine \( \lambda \) de \( P \) , il existe une suite de nombres complexes \( \left( {\alpha }_{m}\right) \) telle que pour tout \( m,{\alpha }_{m} \) est racine de \( {P}_{m} \) et telle que \( \mathop{\lim }\limits_{{m \rightarrow \infty }}{\alpha }_{m} = \lambda \) .

> a) Show that for any root \( \lambda \) of \( P \) , there exists a sequence of complex numbers \( \left( {\alpha }_{m}\right) \) such that for all \( m,{\alpha }_{m} \) is a root of \( {P}_{m} \) and such that \( \mathop{\lim }\limits_{{m \rightarrow \infty }}{\alpha }_{m} = \lambda \) .

b) Montrer que l'on peut écrire

> b) Show that one can write

\[
\forall m \in  \mathbb{N},\;{P}_{m} = \left( {X - {\lambda }_{1, m}}\right) \cdots \left( {X - {\lambda }_{n, m}}\right)
\]

avec pour tout \( i \in \{ 1,\ldots , n\} ,\mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i, m} = {\lambda }_{i} \) .

> with for all \( i \in \{ 1,\ldots , n\} ,\mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i, m} = {\lambda }_{i} \) .

Solution. 1/ Écrivons \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{n - 1}{X}^{n - 1} + {X}^{n} \) , où \( n = \deg \left( P\right) \) . On a \( \parallel P\parallel = \; \left| {a}_{0}\right| + \cdots + \left| {a}_{n - 1}\right| + 1 \geq 1 \) , donc si \( \left| \lambda \right| \leq 1 \) , c’est terminé. Sinon \( \left| \lambda \right| > 1 \) , et l’égalité \( P\left( \lambda \right) = 0 \) entraîne

> Solution. 1/ Let us write \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{n - 1}{X}^{n - 1} + {X}^{n} \) , where \( n = \deg \left( P\right) \) . We have \( \parallel P\parallel = \; \left| {a}_{0}\right| + \cdots + \left| {a}_{n - 1}\right| + 1 \geq 1 \) , so if \( \left| \lambda \right| \leq 1 \) , we are done. Otherwise \( \left| \lambda \right| > 1 \) , and the equality \( P\left( \lambda \right) = 0 \) implies

\[
\lambda  =  - {a}_{n - 1} - \frac{{a}_{n - 2}}{\lambda } - \cdots  - \frac{{a}_{1}}{{\lambda }^{n - 2}} - \frac{{a}_{0}}{{\lambda }^{n - 1}}
\]

de sorte que \( \left| \lambda \right| \leq \left| {a}_{n - 1}\right| + \cdots + \left| {a}_{1}\right| + \left| {a}_{0}\right| < \parallel P\parallel \) , d’où le résultat.

> so that \( \left| \lambda \right| \leq \left| {a}_{n - 1}\right| + \cdots + \left| {a}_{1}\right| + \left| {a}_{0}\right| < \parallel P\parallel \) , hence the result.

2/ a) Pour tout \( m \in \mathbb{N} \) , notons \( {\left( {\alpha }_{i, m}\right) }_{1 \leq i \leq n} \) les racines de \( {P}_{m} \) (sans tenir compte pour l’instant de la numérotation). Il s’agit de montrer que \( \mathop{\min }\limits_{{1 \leq i \leq n}}\left| {{\alpha }_{i, m} - \lambda }\right| \) tend vers 0, c’est-à-dire

> 2/ a) For all \( m \in \mathbb{N} \) , let \( {\left( {\alpha }_{i, m}\right) }_{1 \leq i \leq n} \) denote the roots of \( {P}_{m} \) (without considering the numbering for now). We must show that \( \mathop{\min }\limits_{{1 \leq i \leq n}}\left| {{\alpha }_{i, m} - \lambda }\right| \) tends to 0, that is

\[
\forall \varepsilon  > 0,\exists N,\forall m \geq  N,\exists i \in  \{ 1,\ldots , n\} ,\;\left| {{\alpha }_{i, m} - \lambda }\right|  < \varepsilon .
\]

Supposons le résultat faux, de sorte que

> Assume the result is false, such that

\[
\exists \varepsilon  > 0,\forall N,\exists m \geq  N,\forall i \in  \{ 1,\ldots , n\} ,\;\left| {{\alpha }_{i, m} - \lambda }\right|  \geq  \varepsilon .
\]

On peut alors extraire de la suite \( {\left( {\alpha }_{m}\right) }_{m \in \mathbb{N}} = {\left( {\alpha }_{1, m},\ldots ,{\alpha }_{n, m}\right) }_{m \in \mathbb{N}} \) une sous-suite \( \left( {\alpha }_{\varphi \left( m\right) }\right) \) telle que

> We can then extract from the sequence \( {\left( {\alpha }_{m}\right) }_{m \in \mathbb{N}} = {\left( {\alpha }_{1, m},\ldots ,{\alpha }_{n, m}\right) }_{m \in \mathbb{N}} \) a subsequence \( \left( {\alpha }_{\varphi \left( m\right) }\right) \) such that

\[
\forall m \in  \mathbb{N},\forall i,\;\left| {{\alpha }_{i,\varphi \left( m\right) } - \lambda }\right|  \geq  \varepsilon .
\]

\( \left( {* * }\right) \)

> Comme la suite \( \left( {P}_{m}\right) \) converge, elle est bornée. Notons \( M \) un majorant de \( \left( \begin{Vmatrix}{P}_{m}\end{Vmatrix}\right) \) . La suite \( {\left( {\alpha }_{\varphi \left( m\right) }\right) }_{m \in \mathbb{N}} \) est à valeur dans le compact \( {K}^{n} \) , où \( K = \{ z \in \mathbb{C}\left| \right| z \mid \leq M\} \) (d’après \( 1/) \) . On peut donc en extraire une sous-suite convergente \( \left( {\alpha }_{\varphi \circ \psi \left( m\right) }\right) \) dont nous noterons \( \alpha = \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) la limite. Alors

Since the sequence \( \left( {P}_{m}\right) \) converges, it is bounded. Let \( M \) be an upper bound of \( \left( \begin{Vmatrix}{P}_{m}\end{Vmatrix}\right) \). The sequence \( {\left( {\alpha }_{\varphi \left( m\right) }\right) }_{m \in \mathbb{N}} \) takes values in the compact set \( {K}^{n} \), where \( K = \{ z \in \mathbb{C}\left| \right| z \mid \leq M\} \) (according to \( 1/) \)). We can therefore extract a convergent subsequence \( \left( {\alpha }_{\varphi \circ \psi \left( m\right) }\right) \) whose limit we will denote by \( \alpha = \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \). Then

\[
P = \mathop{\lim }\limits_{{m \rightarrow  \infty }}{P}_{\varphi  \circ  \psi \left( m\right) } = \mathop{\lim }\limits_{{m \rightarrow  \infty }}\left\lbrack  {\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\alpha }_{i,\varphi  \circ  \psi \left( m\right) }}\right) }\right\rbrack   = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\alpha }_{i}}\right) ,
\]

donc les \( {\alpha }_{i} \) sont les racines de \( P \) , donc il existe \( k \) tel que \( {\alpha }_{k} = \lambda \) . Or d’après (**), pour tout \( m \) , \( \left| {{\alpha }_{k} - {\alpha }_{k,\varphi \circ \psi \left( m\right) }}\right| \geq \varepsilon \) . Ceci est contradictoire car \( \left( {\alpha }_{k,\varphi \circ \psi \left( m\right) }\right) \) tend vers \( {\alpha }_{k} \) . D’où le résultat.

> therefore the \( {\alpha }_{i} \) are the roots of \( P \), so there exists \( k \) such that \( {\alpha }_{k} = \lambda \). However, according to (**), for all \( m \), \( \left| {{\alpha }_{k} - {\alpha }_{k,\varphi \circ \psi \left( m\right) }}\right| \geq \varepsilon \). This is contradictory because \( \left( {\alpha }_{k,\varphi \circ \psi \left( m\right) }\right) \) tends to \( {\alpha }_{k} \). Hence the result.

b) Nous allons procéder par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Considérons la racine \( {\lambda }_{n} \) de \( P \) . D’après la question précédente, on peut écrire \( {P}_{m} = \left( {X - {\alpha }_{m}}\right) {Q}_{m} \) pour tout \( m \) , où \( \left( {\alpha }_{m}\right) \) converge vers \( {\lambda }_{n} \) . Notons \( Q \) le polynôme de degré \( n - 1 \) tel que \( P = \left( {X - {\lambda }_{n}}\right) Q \) . En écrivant chacun des polynômes \( {Q}_{m} \) comme le quotient de la division euclidienne de \( {P}_{m} \) par \( \left( {X - {\alpha }_{m}}\right) \) , on s’aperçoit que les coefficients de \( {Q}_{m} \) s’expriment comme un polynôme en les coefficients de \( {P}_{m} \) et en \( {\alpha }_{m} \) . Comme \( \left( {\alpha }_{m}\right) \) tend vers \( \lambda \) et que \( \left( {P}_{m}\right) \) tend vers \( P \) , on en déduit que \( \left( {Q}_{m}\right) \) tend vers \( Q \) . D’après l’hypothèse de récurrence, on peut donc écrire \( {Q}_{m} = \left( {X - {\lambda }_{1, m}}\right) \cdots \left( {X - {\lambda }_{n - 1, m}}\right) \) pour tout \( m \) , avec pour tout \( i\mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i, m} = {\lambda }_{i} \) . Finalement, on a \( {P}_{m} = \left( {X - {\lambda }_{1, m}}\right) \cdots \left( {X - {\lambda }_{n - 1, m}}\right) \left( {X - {\alpha }_{m}}\right) \) pour tout \( m \) et

> b) We will proceed by induction on \( n \in {\mathbb{N}}^{ * } \). For \( n = 1 \), it is obvious. Suppose the result is true at rank \( n - 1 \) and let us show it at rank \( n \). Consider the root \( {\lambda }_{n} \) of \( P \). According to the previous question, we can write \( {P}_{m} = \left( {X - {\alpha }_{m}}\right) {Q}_{m} \) for all \( m \), where \( \left( {\alpha }_{m}\right) \) converges to \( {\lambda }_{n} \). Let \( Q \) be the polynomial of degree \( n - 1 \) such that \( P = \left( {X - {\lambda }_{n}}\right) Q \). By writing each of the polynomials \( {Q}_{m} \) as the quotient of the Euclidean division of \( {P}_{m} \) by \( \left( {X - {\alpha }_{m}}\right) \), we notice that the coefficients of \( {Q}_{m} \) are expressed as a polynomial in the coefficients of \( {P}_{m} \) and in \( {\alpha }_{m} \). Since \( \left( {\alpha }_{m}\right) \) tends to \( \lambda \) and \( \left( {P}_{m}\right) \) tends to \( P \), we deduce that \( \left( {Q}_{m}\right) \) tends to \( Q \). According to the induction hypothesis, we can therefore write \( {Q}_{m} = \left( {X - {\lambda }_{1, m}}\right) \cdots \left( {X - {\lambda }_{n - 1, m}}\right) \) for all \( m \), with for all \( i\mathop{\lim }\limits_{{m \rightarrow \infty }}{\lambda }_{i, m} = {\lambda }_{i} \). Finally, we have \( {P}_{m} = \left( {X - {\lambda }_{1, m}}\right) \cdots \left( {X - {\lambda }_{n - 1, m}}\right) \left( {X - {\alpha }_{m}}\right) \) for all \( m \) and

\[
\forall i \in  \{ 1,\ldots , n - 1\} ,\;\mathop{\lim }\limits_{{m \rightarrow  \infty }}{\lambda }_{i, m} = {\lambda }_{i}\;\text{ et }\;\mathop{\lim }\limits_{{m \rightarrow  \infty }}{\alpha }_{m} = {\lambda }_{n},
\]

ce qui est précisément ce que l'on voulait montrer.

> which is precisely what we wanted to show.

Remarque. On aurait pu répondre à la question 2/ a) sans utiliser la question 1/, en utilisant le résultat suivant.

> Remark. One could have answered question 2/ a) without using question 1/, by using the following result.

LEMME 1. Soit \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) un polynôme unitaire de degré \( n \) et \( \gamma \in \mathbb{C} \) .

> LEMMA 1. Let \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) be a monic polynomial of degree \( n \) and \( \gamma \in \mathbb{C} \) .

Alors il existe une racine \( \alpha \) de \( F \) telle que \( \left| {\alpha - \gamma }\right| \leq {\left| F\left( \gamma \right) \right| }^{1/n} \) .

> Then there exists a root \( \alpha \) of \( F \) such that \( \left| {\alpha - \gamma }\right| \leq {\left| F\left( \gamma \right) \right| }^{1/n} \) .

Le lemme se démontre en notant \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) les racines de \( F \) et en les supposant ordonnées de sorte que \( \left| {\gamma - {\alpha }_{1}}\right| \leq \left| {\gamma - {\alpha }_{i}}\right| \) pour tout \( i \) . Alors on a \( {\left| \gamma - {\alpha }_{1}\right| }^{n} \leq \mathop{\prod }\limits_{{i = 1}}^{n}\left| {\gamma - {\alpha }_{i}}\right| = \left| {F\left( \gamma \right) }\right| \) d'où le résultat.

> The lemma is proven by denoting \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) as the roots of \( F \) and assuming they are ordered such that \( \left| {\gamma - {\alpha }_{1}}\right| \leq \left| {\gamma - {\alpha }_{i}}\right| \) for all \( i \) . Then we have \( {\left| \gamma - {\alpha }_{1}\right| }^{n} \leq \mathop{\prod }\limits_{{i = 1}}^{n}\left| {\gamma - {\alpha }_{i}}\right| = \left| {F\left( \gamma \right) }\right| \) which gives the result.

Le fait que \( \left( {P}_{m}\right) \) tende vers \( P \) entraîne que \( {P}_{m}\left( \lambda \right) \) tend vers \( P\left( \lambda \right) = 0 \) . Le lemme nous assure pour tout \( m \) l’existence d’une racine \( {\alpha }_{m} \) de \( {P}_{m} \) telle que \( \left| {\lambda - {\alpha }_{m}}\right| \leq {\left| {P}_{m}\left( \lambda \right) \right| }^{1/n} \) . Comme \( \left( {{P}_{m}\left( \lambda \right) }\right) \) tend vers 0, on en déduit que \( \left( {\alpha }_{m}\right) \) tend vers \( \lambda \) , ce qui répond à la question \( 2/ \) a).

> The fact that \( \left( {P}_{m}\right) \) tends to \( P \) implies that \( {P}_{m}\left( \lambda \right) \) tends to \( P\left( \lambda \right) = 0 \) . The lemma ensures for all \( m \) the existence of a root \( {\alpha }_{m} \) of \( {P}_{m} \) such that \( \left| {\lambda - {\alpha }_{m}}\right| \leq {\left| {P}_{m}\left( \lambda \right) \right| }^{1/n} \) . As \( \left( {{P}_{m}\left( \lambda \right) }\right) \) tends to 0, we deduce that \( \left( {\alpha }_{m}\right) \) tends to \( \lambda \) , which answers question \( 2/ \) a).

Problems 14 (THÉORÉME D’ASCOLI). Soit \( \left( {X, d}\right) \) et \( \left( {Y,\delta }\right) \) deux espaces métriques compacts. On note \( \mathcal{C}\left( {X, Y}\right) \) l’ensemble des fonctions continues de \( X \) dans \( Y \) . Muni de la distance de la convergence uniforme \( \Delta \left( {f, g}\right) = \mathop{\sup }\limits_{{x \in X}}\delta \left( {f\left( x\right) , g\left( x\right) }\right) \) , l’ensemble \( \mathcal{C}\left( {X, Y}\right) \) est un espace métrique.

> Problems 14 (ASCOLI'S THEOREM). Let \( \left( {X, d}\right) \) and \( \left( {Y,\delta }\right) \) be two compact metric spaces. Let \( \mathcal{C}\left( {X, Y}\right) \) denote the set of continuous functions from \( X \) to \( Y \) . Equipped with the uniform convergence distance \( \Delta \left( {f, g}\right) = \mathop{\sup }\limits_{{x \in X}}\delta \left( {f\left( x\right) , g\left( x\right) }\right) \) , the set \( \mathcal{C}\left( {X, Y}\right) \) is a metric space.

Soit \( A \) une partie de \( \mathcal{C}\left( {X, Y}\right) \) . On dit que \( A \) est équicontinue si

> Let \( A \) be a subset of \( \mathcal{C}\left( {X, Y}\right) \) . We say that \( A \) is equicontinuous if

\[
\forall x \in  X,\forall \varepsilon  > 0,\exists \eta  > 0;\forall f \in  F,\forall y \in  X,\;d\left( {x, y}\right)  < \eta  \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

1/ Montrer que si \( A \) est équicontinue, alors \( A \) est uniformément équicontinue, c’est-à-dire

> 1/ Show that if \( A \) is equicontinuous, then \( A \) is uniformly equicontinuous, that is to say

\[
\forall \varepsilon  > 0,\exists \eta  > 0;\forall f \in  A,\forall x, y \in  X,\;d\left( {x, y}\right)  < \eta  \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

2/ (Théorème d'Ascoli) Démontrer que les deux propositions suivantes sont équivalentes : (i) A est relativement compacte (i.e son adhérence est compacte) dans \( \mathcal{C}\left( {X, Y}\right) \) .

> 2/ (Ascoli's Theorem) Prove that the following two propositions are equivalent: (i) A is relatively compact (i.e., its closure is compact) in \( \mathcal{C}\left( {X, Y}\right) \) .

(ii) A est équicontinue.

> (ii) A is equicontinuous.

(Pour montrer (ii) ⇒ (i), on pourra utiliser le résultat de l'exercice 2 page 32 qui dit que tout précompact complet est compact).

> (To show (ii) ⇒ (i), one may use the result of exercise 2 on page 32 which states that every complete precompact set is compact).

Solution. 1/ Soit \( \varepsilon > 0 \) . Comme \( A \) est équicontinue, pour tout \( x \in X \) il existe \( {\eta }_{x} > 0 \) tel que

> Solution. 1/ Let \( \varepsilon > 0 \) . Since \( A \) is equicontinuous, for all \( x \in X \) there exists \( {\eta }_{x} > 0 \) such that

\[
\forall f \in  F,\forall y \in  X;\;d\left( {x, y}\right)  < 2{\eta }_{x} \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

On peut extraire du recouvrement d’ouverts \( { \cup }_{x \in X}\mathrm{\;B}\left( {x,{\eta }_{x}}\right) \) du compact \( \mathrm{X} \) , un recouvrement fini. Autrement dit, il existe \( n \in {\mathbb{N}}^{ * } \) et des éléments \( {x}_{1},\ldots ,{x}_{n} \in X \) tels que \( X \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \) . Soit \( \eta = \mathop{\min }\limits_{{1 \leq i \leq n}}{\eta }_{{x}_{i}} \) . On a \( \eta > 0 \) . Soit \( x, y \in X \) tels que \( d\left( {x, y}\right) < \eta \) . Soit \( i \) tel que \( d\left( {x,{x}_{i}}\right) < {\eta }_{{x}_{i}} \) . On a

> We can extract a finite subcover from the open cover \( { \cup }_{x \in X}\mathrm{\;B}\left( {x,{\eta }_{x}}\right) \) of the compact set \( \mathrm{X} \). In other words, there exists \( n \in {\mathbb{N}}^{ * } \) and elements \( {x}_{1},\ldots ,{x}_{n} \in X \) such that \( X \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \). Let \( \eta = \mathop{\min }\limits_{{1 \leq i \leq n}}{\eta }_{{x}_{i}} \). We have \( \eta > 0 \). Let \( x, y \in X \) be such that \( d\left( {x, y}\right) < \eta \). Let \( i \) be such that \( d\left( {x,{x}_{i}}\right) < {\eta }_{{x}_{i}} \). We have

\[
d\left( {x,{x}_{i}}\right)  < {\eta }_{{x}_{i}} < 2{\eta }_{{x}_{i}}\;\text{ donc }\;\delta \left( {f\left( x\right) , f\left( {x}_{i}\right) }\right)  < \varepsilon
\]

\[
d\left( {y,{x}_{i}}\right)  \leq  d\left( {y, x}\right)  + d\left( {x,{x}_{i}}\right)  < \eta  + {\eta }_{{x}_{i}} \leq  2{\eta }_{{x}_{i}}\;\text{ donc }\;\delta \left( {f\left( y\right) , f\left( {x}_{i}\right) }\right)  < \varepsilon .
\]

On en déduit \( \delta \left( {f\left( x\right) , f\left( y\right) }\right) \leq \delta \left( {f\left( x\right) , f\left( {x}_{i}\right) }\right) + \delta \left( {f\left( {x}_{i}\right) , f\left( y\right) }\right) < {2\varepsilon } \) . Ceci est vrai pour tout \( x, y \in X \) tels que \( d\left( {x, y}\right) < \eta \) , donc \( A \) est bien uniformément équicontinue.

> We deduce \( \delta \left( {f\left( x\right) , f\left( y\right) }\right) \leq \delta \left( {f\left( x\right) , f\left( {x}_{i}\right) }\right) + \delta \left( {f\left( {x}_{i}\right) , f\left( y\right) }\right) < {2\varepsilon } \). This is true for all \( x, y \in X \) such that \( d\left( {x, y}\right) < \eta \), therefore \( A \) is indeed uniformly equicontinuous.

2 / Montrons (i) \( \Rightarrow \) (ii). Soit \( x \in X \) et \( \varepsilon > 0 \) . Comme \( A \) est relativement compact, on peut le recouvrir par un nombre fini de boules centrées dans \( A \) de rayon \( \varepsilon \) , c’est-à-dire

> 2 / Let us show (i) \( \Rightarrow \) (ii). Let \( x \in X \) and \( \varepsilon > 0 \). Since \( A \) is relatively compact, it can be covered by a finite number of balls centered in \( A \) with radius \( \varepsilon \), that is to say

\[
\exists n \in  {\mathbb{N}}^{ * },\exists {f}_{1},\ldots ,{f}_{n} \in  A,\;A \subset  { \cup  }_{1 \leq  i \leq  n}\mathrm{\;B}\left( {{f}_{i},\varepsilon }\right) .
\]

(*)

> Chaque fonction \( {f}_{i} \) est continue en \( x \) donc

Each function \( {f}_{i} \) is continuous at \( x \) therefore

\[
\forall i,\exists {\eta }_{i} > 0;\;\forall y \in  K,\;d\left( {x, y}\right)  < {\eta }_{i} \Rightarrow  \delta \left( {{f}_{i}\left( x\right) ,{f}_{i}\left( y\right) }\right)  < \varepsilon .
\]

Choisissons \( \eta = \mathop{\inf }\limits_{{1 \leq i \leq n}}{\eta }_{i} \) . Soit \( f \in A \) . D’après (*), il existe \( i \) tel que \( f \in \mathrm{B}\left( {{f}_{i},\varepsilon }\right) \) . Avec ce choix de \( \eta > 0 \) , on a démontré (ii) car pour tous \( y \in K \) tel que \( d\left( {x, y}\right) < \eta \) , on a l’inégalité

> Let us choose \( \eta = \mathop{\inf }\limits_{{1 \leq i \leq n}}{\eta }_{i} \). Let \( f \in A \). According to (*), there exists \( i \) such that \( f \in \mathrm{B}\left( {{f}_{i},\varepsilon }\right) \). With this choice of \( \eta > 0 \), we have proven (ii) because for all \( y \in K \) such that \( d\left( {x, y}\right) < \eta \), we have the inequality

\[
\delta \left( {f\left( x\right) , f\left( y\right) }\right)  \leq  \delta \left( {f\left( x\right) ,{f}_{i}\left( x\right) }\right)  + \delta \left( {{f}_{i}\left( x\right) ,{f}_{i}\left( y\right) }\right)  + \delta \left( {{f}_{i}\left( y\right) , f\left( y\right) }\right)  < \varepsilon  + \varepsilon  + \varepsilon  = {3\varepsilon }.
\]

- Montrons maintenant (ii) \( \Rightarrow \) (i). Suivons l’indication et démontrons que \( \bar{A} \) est précompact et complet. Montrons d’abord que \( \bar{A} \) est précompact. Pour cela il suffit de montrer que \( A \) est précompact. Soit \( \varepsilon  > 0 \) . On va montrer qu’on peut recouvrir \( A \) par un recouvrement fini de boules de rayon \( {4\varepsilon } \) . Pour tout \( x \in  X \) , il existe \( {\eta }_{x} > 0 \) tel que

> - Let us now show (ii) \( \Rightarrow \) (i). Let us follow the hint and prove that \( \bar{A} \) is precompact and complete. Let us first show that \( \bar{A} \) is precompact. To do this, it suffices to show that \( A \) is precompact. Let \( \varepsilon  > 0 \). We will show that we can cover \( A \) with a finite cover of balls of radius \( {4\varepsilon } \). For all \( x \in  X \), there exists \( {\eta }_{x} > 0 \) such that

\[
\forall f \in  F,\forall y \in  X,\;d\left( {x, y}\right)  < {\eta }_{x} \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]

Du recouvrement d’ouverts \( { \cup }_{x \in X}\mathrm{B}\left( {x,{\eta }_{x}}\right) \) de \( X \) on peut en extraire un sous-recouvrement fini \( { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \) , avec les \( {x}_{i} \in X \) . Comme \( Y \) est compact on peut le recouvrir par un nombre fini de boules de rayon \( \varepsilon > 0 \) , autrement dit il existe \( m \in {\mathbb{N}}^{ * } \) et \( {z}_{1},\ldots ,{z}_{m} \in Y \) tels que \( Y \subset { \cup }_{1 \leq j \leq m}\mathrm{\;B}\left( {{z}_{j},\varepsilon }\right) \) . Pour tout \( n \) -uplet \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) \) de \( \{ 1,\ldots , m{\} }^{n} \) , on note

> From the open cover \( { \cup }_{x \in X}\mathrm{B}\left( {x,{\eta }_{x}}\right) \) of \( X \) we can extract a finite subcover \( { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \) , with the \( {x}_{i} \in X \) . Since \( Y \) is compact it can be covered by a finite number of balls of radius \( \varepsilon > 0 \) , in other words there exist \( m \in {\mathbb{N}}^{ * } \) and \( {z}_{1},\ldots ,{z}_{m} \in Y \) such that \( Y \subset { \cup }_{1 \leq j \leq m}\mathrm{\;B}\left( {{z}_{j},\varepsilon }\right) \) . For any \( n \) -tuple \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) \) of \( \{ 1,\ldots , m{\} }^{n} \) , we denote

\[
{B}_{J} = \left\{  {f \in  \mathcal{C}\left( {X, Y}\right) \mid \forall i = 1,\ldots , n,\forall x \in  B\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) ,\delta \left( {f\left( x\right) ,{z}_{{j}_{i}}}\right)  < {2\varepsilon }}\right\}  .
\]

Pour tout \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) ,{B}_{J} \) est inclus dans une boule de rayon \( {4\varepsilon } \) . En effet, choisissons arbitrairement \( {f}_{J} \in {B}_{J} \) . Soit \( f \in {B}_{J} \) . Pour tout \( x \in X \) , il existe \( i \) tel que \( x \in \mathrm{B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \) donc \( \delta \left( {f\left( x\right) ,{z}_{{j}_{i}}}\right) < {2\varepsilon } \) et \( \delta \left( {{f}_{J}\left( x\right) ,{z}_{{j}_{i}}}\right) < {2\varepsilon } \) . Donc \( \delta \left( {f\left( x\right) ,{f}_{J}\left( x\right) }\right) \leq \delta \left( {f\left( z\right) ,{z}_{{j}_{i}}}\right) + \delta \left( {{z}_{{j}_{i}},{f}_{J}\left( z\right) }\right) < {4\varepsilon } \) . Ainsi, \( \Delta \left( {f,{f}_{J}}\right) < {4\varepsilon } \) (le sup d’une fonction continue est atteint sur un compact donc l’inégalité reste stricte) donc \( {B}_{J} \subset \mathrm{B}\left( {{f}_{J},{4\varepsilon }}\right) \) . Par ailleurs, les \( {B}_{J} \) recouvrent bien \( A \) . En effet, soit \( f \in A \) . Pour tout \( i \) , soit \( {j}_{i} \) tel que \( f\left( {x}_{i}\right) \in \mathrm{B}\left( {{z}_{{j}_{i}},\varepsilon }\right) \) . On a

> For any \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) ,{B}_{J} \) is included in a ball of radius \( {4\varepsilon } \) . Indeed, let us choose arbitrarily \( {f}_{J} \in {B}_{J} \) . Let \( f \in {B}_{J} \) . For any \( x \in X \) , there exists \( i \) such that \( x \in \mathrm{B}\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) \) therefore \( \delta \left( {f\left( x\right) ,{z}_{{j}_{i}}}\right) < {2\varepsilon } \) and \( \delta \left( {{f}_{J}\left( x\right) ,{z}_{{j}_{i}}}\right) < {2\varepsilon } \) . Thus \( \delta \left( {f\left( x\right) ,{f}_{J}\left( x\right) }\right) \leq \delta \left( {f\left( z\right) ,{z}_{{j}_{i}}}\right) + \delta \left( {{z}_{{j}_{i}},{f}_{J}\left( z\right) }\right) < {4\varepsilon } \) . Thus, \( \Delta \left( {f,{f}_{J}}\right) < {4\varepsilon } \) (the sup of a continuous function is attained on a compact set so the inequality remains strict) therefore \( {B}_{J} \subset \mathrm{B}\left( {{f}_{J},{4\varepsilon }}\right) \) . Furthermore, the \( {B}_{J} \) indeed cover \( A \) . Indeed, let \( f \in A \) . For any \( i \) , let \( {j}_{i} \) such that \( f\left( {x}_{i}\right) \in \mathrm{B}\left( {{z}_{{j}_{i}},\varepsilon }\right) \) . We have

\[
\forall x \in  B\left( {{x}_{i},{\eta }_{{x}_{i}}}\right) ,\;\delta \left( {f\left( x\right) ,{z}_{{j}_{i}}}\right)  \leq  \delta \left( {f\left( x\right) , f\left( {x}_{i}\right) }\right)  + \delta \left( {f\left( {x}_{i}\right) ,{z}_{{j}_{i}}}\right)  < {2\varepsilon }.
\]

En notant \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) \) , on en déduit que \( f \in {B}_{J} \) .

> By denoting \( J = \left( {{j}_{1},\ldots ,{j}_{n}}\right) \) , we deduce that \( f \in {B}_{J} \) .

Il nous reste à montrer que \( \bar{A} \) est complet. Tout fermé dans un complet est complet, il nous suffit donc de prouver que \( \mathcal{C}\left( {X, Y}\right) \) est complet. Pour cela, on considère une suite de Cauchy \( {\left( {f}_{n}\right) }_{n \in N} \) de \( \mathcal{C}\left( {X, Y}\right) \) . Pour tout \( p, q \in \mathbb{N} \) et pour tout \( x \in X \) on a \( \delta \left( {{f}_{p}\left( x\right) ,{f}_{q}\left( x\right) }\right) \leq \Delta \left( {{f}_{p},{f}_{q}}\right) \) , donc la suite \( \left( {{f}_{n}\left( x\right) }\right) \) est de Cauchy. Cette suite est à valeur dans le compact \( Y \) , donc complet, donc elle converge. En désignant par \( f\left( x\right) \) sa limite, on défini une fonction \( f \) de \( X \) dans \( Y \) . Comme \( f \) est la limite uniforme des fonctions continues \( {f}_{n} \) , elle est donc continue. Ainsi \( \left( {f}_{n}\right) \) converge vers \( f \in \mathcal{C}\left( {X, Y}\right) \) .

> It remains for us to show that \( \bar{A} \) is complete. Any closed set in a complete space is complete, so it suffices to prove that \( \mathcal{C}\left( {X, Y}\right) \) is complete. To do this, we consider a Cauchy sequence \( {\left( {f}_{n}\right) }_{n \in N} \) in \( \mathcal{C}\left( {X, Y}\right) \). For all \( p, q \in \mathbb{N} \) and for all \( x \in X \) we have \( \delta \left( {{f}_{p}\left( x\right) ,{f}_{q}\left( x\right) }\right) \leq \Delta \left( {{f}_{p},{f}_{q}}\right) \) , so the sequence \( \left( {{f}_{n}\left( x\right) }\right) \) is Cauchy. This sequence takes values in the compact set \( Y \) , which is therefore complete, so it converges. By denoting its limit as \( f\left( x\right) \) , we define a function \( f \) from \( X \) to \( Y \) . Since \( f \) is the uniform limit of the continuous functions \( {f}_{n} \) , it is therefore continuous. Thus \( \left( {f}_{n}\right) \) converges to \( f \in \mathcal{C}\left( {X, Y}\right) \) .

Remarque. - Le résultat de la question 1/ peut être vu comme une généralisation du théorème de Heine. Nous ne l'avons pas utilisé pour la solution de la question \( 2/ \) .

> Remark. - The result of question 1/ can be seen as a generalization of the Heine theorem. We did not use it for the solution to question \( 2/ \) .

- Le résultat de la question 2/ est une version faible du théorème d'Ascoli. Dans sa version plus générale, le compact \( Y \) est remplacé par un espace métrique quelconque et la condition d'équicontinuité est complétée par une autre condition (dite de ponctuelle relative compacité).

> - The result of question 2/ is a weak version of the Ascoli theorem. In its more general version, the compact set \( Y \) is replaced by an arbitrary metric space and the equicontinuity condition is supplemented by another condition (known as pointwise relative compactness).

- On peut aussi prouver le résultat de la question sans faire appel à la propriété "tout précompact complet est compact", en démontrant que de toute suite \( \left( {f}_{n}\right) \) de \( A \) , on peut en extraire une sous-suite convergente, en construisant cette sous-suite par un procédé diagonal (comme pour l'exercice 2 page 32).

> - One can also prove the result of the question without invoking the property "every complete precompact set is compact," by demonstrating that from any sequence \( \left( {f}_{n}\right) \) in \( A \) , one can extract a convergent subsequence by constructing this subsequence using a diagonal process (as for exercise 2 on page 32).

- Le théorème d'Ascoli a de multiple conséquences, comme la compacité de certains opérateurs ou l'existence de solutions dans certaines équations différentielles.

> - The Ascoli theorem has multiple consequences, such as the compactness of certain operators or the existence of solutions in certain differential equations.
