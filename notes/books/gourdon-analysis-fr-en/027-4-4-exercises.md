#### 4.4. Exercises

*Français : 4.4. Exercices*

EXERCICE 1. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique, \( B \) une partie connexe de \( E \) et \( A \) une partie de \( E \) telle que \( B \cap \overset{ \circ }{A} \neq \varnothing \) et \( B \cap \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) \neq \varnothing \) . Montrer que \( B \cap \operatorname{Fr}\left( A\right) \neq \varnothing \) (où \( \operatorname{Fr}\left( A\right) \) désigne la frontière de \( A) \) .

> EXERCISE 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space, \( B \) a connected subset of \( E \) , and \( A \) a subset of \( E \) such that \( B \cap \overset{ \circ }{A} \neq \varnothing \) and \( B \cap \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) \neq \varnothing \) . Show that \( B \cap \operatorname{Fr}\left( A\right) \neq \varnothing \) (where \( \operatorname{Fr}\left( A\right) \) denotes the boundary of \( A) \) ).

Solution. On note \( \complement X = E \smallsetminus X \) le complémentaire de \( X \) dans \( E \) . Remarquons déjà que

> Solution. Let \( \complement X = E \smallsetminus X \) denote the complement of \( X \) in \( E \) . Note first that

\[
E \smallsetminus  \operatorname{Fr}\left( A\right)  = \complement \left( {\bar{A} \smallsetminus  \overset{ \circ  }{A}}\right)  = \complement \left( {\bar{A} \cap  \complement \overset{ \circ  }{A}}\right)  = \left( {\complement \bar{A}}\right)  \cup  \overset{ \circ  }{A} = \overset{ \circ  }{A} \cup  \left( {E \smallsetminus  \bar{A}}\right)  = \overset{ \circ  }{A} \cup  \left( \overset{\text{ ⏜ }}{E \smallsetminus  A}\right) .
\]

Ceci étant, supposons \( B \cap \operatorname{Fr}\left( A\right) = \varnothing \) . Alors \( B \subset E \smallsetminus \operatorname{Fr}\left( A\right) = \overset{ \circ }{A} \cup \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) \) . Les ensembles \( \overset{ \circ }{A} \) et \( \overset{\text{ ⏜ }}{E \smallsetminus A} \) étant deux ouverts disjoints de \( E \) , on en déduit, \( B \) étant connexe, que \( B \cap \overset{ \circ }{A} = \varnothing \) ou \( B \cap \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) = \varnothing \) , ce qui absurde par hypothèse. Donc \( B \cap \operatorname{Fr}\left( A\right) \neq \varnothing \) .

> Given this, suppose \( B \cap \operatorname{Fr}\left( A\right) = \varnothing \) . Then \( B \subset E \smallsetminus \operatorname{Fr}\left( A\right) = \overset{ \circ }{A} \cup \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) \) . Since the sets \( \overset{ \circ }{A} \) and \( \overset{\text{ ⏜ }}{E \smallsetminus A} \) are two disjoint open sets in \( E \) , we deduce, as \( B \) is connected, that \( B \cap \overset{ \circ }{A} = \varnothing \) or \( B \cap \left( \overset{\text{ ⏜ }}{E \smallsetminus A}\right) = \varnothing \) , which is absurd by hypothesis. Therefore \( B \cap \operatorname{Fr}\left( A\right) \neq \varnothing \) .

EXERCICE 2. Soient \( A \) et \( B \) deux espaces métriques connexes. Soit \( X \subset A, X \neq A \) et \( Y \subset B, Y \neq B \) . Montrer que \( C = \left( {A \times B}\right) \smallsetminus \left( {X \times Y}\right) \) est un connexe de \( A \times B \) .

> EXERCISE 2. Let \( A \) and \( B \) be two connected metric spaces. Let \( X \subset A, X \neq A \) and \( Y \subset B, Y \neq B \) . Show that \( C = \left( {A \times B}\right) \smallsetminus \left( {X \times Y}\right) \) is a connected subset of \( A \times B \) .

Solution. D’après les hypothèses, il existe \( {a}_{0} \in A \) tel que \( {a}_{0} \notin X \) et \( {b}_{0} \in B \) tel que \( {b}_{0} \notin Y \) .

> Solution. According to the hypotheses, there exists \( {a}_{0} \in A \) such that \( {a}_{0} \notin X \) and \( {b}_{0} \in B \) such that \( {b}_{0} \notin Y \) .

Soit \( f : C \rightarrow \{ 0,1\} \) une application continue. Il s’agit de montrer que \( f \) est constante. Soit \( \left( {a, b}\right) \) un point de \( C \) . Comme \( \left( {a, b}\right) \notin X \times Y \) , on a \( a \notin X \) ou \( b \notin Y \) , par exemple \( a \notin X \) . Ainsi, pour tout \( y \in B,\left( {a, y}\right) \in C \) . La restriction de \( f \) à \( \{ a\} \times B \) est continue. Comme \( \{ a\} \) et \( B \) sont connexes, la restriction de \( f \) à \( \{ a\} \times B \) est constante. En particulier, \( f\left( {a, b}\right) = f\left( {a,{b}_{0}}\right) \) . Comme \( {b}_{0} \notin Y \) , on montrerait de même \( f\left( {a,{b}_{0}}\right) = f\left( {{a}_{0},{b}_{0}}\right) \) . Donc \( f\left( {a, b}\right) = f\left( {{a}_{0},{b}_{0}}\right) \) , et ceci pour tout \( \left( {a, b}\right) \in C \) , donc \( f \) est constante. D’après la proposition 3 page \( {39}, C \) est donc connexe.

> Let \( f : C \rightarrow \{ 0,1\} \) be a continuous map. We must show that \( f \) is constant. Let \( \left( {a, b}\right) \) be a point in \( C \) . Since \( \left( {a, b}\right) \notin X \times Y \) , we have \( a \notin X \) or \( b \notin Y \) , for example \( a \notin X \) . Thus, for all \( y \in B,\left( {a, y}\right) \in C \) . The restriction of \( f \) to \( \{ a\} \times B \) is continuous. Since \( \{ a\} \) and \( B \) are connected, the restriction of \( f \) to \( \{ a\} \times B \) is constant. In particular, \( f\left( {a, b}\right) = f\left( {a,{b}_{0}}\right) \) . Since \( {b}_{0} \notin Y \) , we would similarly show \( f\left( {a,{b}_{0}}\right) = f\left( {{a}_{0},{b}_{0}}\right) \) . Thus \( f\left( {a, b}\right) = f\left( {{a}_{0},{b}_{0}}\right) \) , and this for all \( \left( {a, b}\right) \in C \) , so \( f \) is constant. According to proposition 3 on page \( {39}, C \) , it is therefore connected.

EXERCICE 3. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique connexe et \( F \) un fermé de \( E \) . On suppose que \( \operatorname{Fr}\left( F\right) \) est connexe. Montrer que \( F \) est connexe. Le résultat subsiste-t-il si \( F \) n’est pas supposé fermé ?

> EXERCISE 3. Let \( \left( {E,\mathrm{\;d}}\right) \) be a connected metric space and \( F \) a closed subset of \( E \) . Suppose that \( \operatorname{Fr}\left( F\right) \) is connected. Show that \( F \) is connected. Does the result hold if \( F \) is not assumed to be closed?

Solution. En vertu de la proposition 3 page 39, il suffit de montrer que toute application continue \( f : F \rightarrow D = \{ 0,1\} \) est constante. Soit \( f \) une telle application. La restriction \( {f}_{\mid \operatorname{Fr}\left( F\right) } \) de \( f \) à \( \operatorname{Fr}\left( F\right) \subset F \) est continue, et comme \( \operatorname{Fr}\left( F\right) \) est connexe par hypothèse, \( {f}_{\mid \operatorname{Fr}\left( F\right) } \) est constante. Supposons par exemple que \( f\left( x\right) = 0 \) pour tout \( x \in \operatorname{Fr}\left( F\right) \) . On définit une extension \( g \) de \( f \) sur \( E \) par

> Solution. By virtue of proposition 3 on page 39, it suffices to show that any continuous map \( f : F \rightarrow D = \{ 0,1\} \) is constant. Let \( f \) be such a map. The restriction \( {f}_{\mid \operatorname{Fr}\left( F\right) } \) of \( f \) to \( \operatorname{Fr}\left( F\right) \subset F \) is continuous, and since \( \operatorname{Fr}\left( F\right) \) is connected by hypothesis, \( {f}_{\mid \operatorname{Fr}\left( F\right) } \) is constant. Suppose for example that \( f\left( x\right) = 0 \) for all \( x \in \operatorname{Fr}\left( F\right) \) . We define an extension \( g \) of \( f \) to \( E \) by

\[
g\left( x\right)  = f\left( x\right) \;\text{ si }\;x \in  F,\;g\left( x\right)  = 0\;\text{ si }\;x \in  E \smallsetminus  F.
\]

On va montrer que \( g \) est continue, il suffit donc de montrer que l’image réciproque de tout fermé de \( D \) est fermée dans \( E \) . Les fermés de \( D \) sont \( \varnothing , D,\{ 0\} \) et \{1\}. On a

> We will show that \( g \) is continuous; it therefore suffices to show that the preimage of any closed set in \( D \) is closed in \( E \) . The closed sets of \( D \) are \( \varnothing , D,\{ 0\} \) and \{1\}. We have

\[
{g}^{-1}\left( \varnothing \right)  = \varnothing ,\;{g}^{-1}\left( D\right)  = E,\;{g}^{-1}\left( {\{ 1\} }\right)  = {f}^{-1}\left( {\{ 1\} }\right)
\]

donc ces images réciproques sont fermées \( \left( {{f}^{-1}\left( {\{ 1\} }\right) }\right. \) est fermé dans \( F \) car \( f \) est continue, donc dans \( E \) car \( F \) est fermé dans \( E \) ). Il reste à monter que \( {g}^{-1}\left( {\{ 0\} }\right) \) est fermé dans \( E \) . Partant de

> so these inverse images are closed \( \left( {{f}^{-1}\left( {\{ 1\} }\right) }\right. \) is closed in \( F \) because \( f \) is continuous, therefore in \( E \) because \( F \) is closed in \( E \) ). It remains to show that \( {g}^{-1}\left( {\{ 0\} }\right) \) is closed in \( E \) . Starting from

\[
{g}^{-1}\left( {\{ 0\} }\right)  = \left( {E \smallsetminus  F}\right)  \cup  {f}^{-1}\left( {\{ 0\} }\right)  = \left( {E \smallsetminus  \overset{ \circ  }{F}}\right)  \cup  {f}^{-1}\left( {\{ 0\} }\right) ,
\]

(cette dernière égalité est vraie car \( E \smallsetminus F = \left( {E \smallsetminus F}\right) \cup \operatorname{Fr}\left( F\right) \) et \( \operatorname{Fr}\left( F\right) \subset {f}^{-1}\left( {\{ 0\} }\right) \) ), on voit que \( {g}^{-1}\left( {\{ 0\} }\right) \) , union de deux fermés dans \( E \) , est fermé dans \( E \) .

> (this last equality is true because \( E \smallsetminus F = \left( {E \smallsetminus F}\right) \cup \operatorname{Fr}\left( F\right) \) and \( \operatorname{Fr}\left( F\right) \subset {f}^{-1}\left( {\{ 0\} }\right) \) ), we see that \( {g}^{-1}\left( {\{ 0\} }\right) \) , the union of two closed sets in \( E \) , is closed in \( E \) .

Finalement on a démontré que \( g : E \rightarrow D \) est continue. Or \( E \) est connexe, donc \( g \) est constante, donc \( f = {g}_{\mid F} \) est constante. Ceci conclut à la connexité de \( F \) .

> Finally, we have shown that \( g : E \rightarrow D \) is continuous. However, \( E \) is connected, so \( g \) is constant, therefore \( f = {g}_{\mid F} \) is constant. This concludes the connectedness of \( F \) .

Le résultat est faux si \( F \) n’est pas supposé fermé. Par exemple, si \( E = \mathbb{R} \) et \( F = {\mathbb{R}}^{ * } \) , \( \operatorname{Fr}\left( F\right) = \{ 0\} \) est connexe et pourtant \( F = \rbrack - \infty ,0\left\lbrack \cup \right\rbrack 0, + \infty \lbrack \) n’est pas connexe.

> The result is false if \( F \) is not assumed to be closed. For example, if \( E = \mathbb{R} \) and \( F = {\mathbb{R}}^{ * } \) , \( \operatorname{Fr}\left( F\right) = \{ 0\} \) is connected and yet \( F = \rbrack - \infty ,0\left\lbrack \cup \right\rbrack 0, + \infty \lbrack \) is not connected.

EXERCICE 4. On note \( \mathbb{U} = \{ z \in \mathbb{C},\left| z\right| = 1\} \) et on considère \( f : \mathbb{U} \rightarrow \mathbb{R} \) une application continue. Montrer qu'il existe deux points diamétralement opposés du cercle unité \( \mathbb{U} \) ayant même image par \( f \) .

> EXERCISE 4. Let \( \mathbb{U} = \{ z \in \mathbb{C},\left| z\right| = 1\} \) be denoted and consider \( f : \mathbb{U} \rightarrow \mathbb{R} \) a continuous map. Show that there exist two diametrically opposite points on the unit circle \( \mathbb{U} \) having the same image under \( f \) .

Solution. Il s’agit de prouver l’existence de \( z \in \mathbb{U} \) tel que \( f\left( z\right) = f\left( {-z}\right) \) . Considérons l’application

> Solution. It is a matter of proving the existence of \( z \in \mathbb{U} \) such that \( f\left( z\right) = f\left( {-z}\right) \) . Consider the map

\[
g : \mathbb{U} \rightarrow  \mathbb{R}\;z \mapsto  f\left( z\right)  - f\left( {-z}\right)
\]

La continuité de \( g \) et le caractère connexe de \( \mathbb{U}\left( \mathbb{U}\right. \) est connexe comme image du connexe \( \left\lbrack {0,{2\pi }}\right\rbrack \) par l’application continue \( \theta \mapsto {e}^{i\theta } \) ) entraîne que \( g\left( \mathbb{U}\right) \) est connexe dans \( \mathbb{R} \) , c’est donc un intervalle de \( \mathbb{R} \) . Or \( g\left( 1\right) = f\left( 1\right) - f\left( {-1}\right) = - g\left( {-1}\right) \) . L’intervalle \( g\left( \mathbb{U}\right) \) contient donc deux valeurs opposées, donc \( 0 \in g\left( \mathbb{U}\right) \) . En d’autres termes, il existe \( z \in \mathbb{U} \) tel que \( g\left( z\right) = 0 = f\left( z\right) - f\left( {-z}\right) \) , d’où le résultat.

> The continuity of \( g \) and the connected nature of \( \mathbb{U}\left( \mathbb{U}\right. \) is connected as the image of the connected set \( \left\lbrack {0,{2\pi }}\right\rbrack \) under the continuous map \( \theta \mapsto {e}^{i\theta } \) ) implies that \( g\left( \mathbb{U}\right) \) is connected in \( \mathbb{R} \) , it is therefore an interval of \( \mathbb{R} \) . However, \( g\left( 1\right) = f\left( 1\right) - f\left( {-1}\right) = - g\left( {-1}\right) \) . The interval \( g\left( \mathbb{U}\right) \) therefore contains two opposite values, so \( 0 \in g\left( \mathbb{U}\right) \) . In other words, there exists \( z \in \mathbb{U} \) such that \( g\left( z\right) = 0 = f\left( z\right) - f\left( {-z}\right) \) , hence the result.

EXERCICE 5. Soit \( \Gamma \) le sous-ensemble de \( {\mathbb{R}}^{2} \) défini par

> EXERCISE 5. Let \( \Gamma \) be the subset of \( {\mathbb{R}}^{2} \) defined by

\[
\Gamma  = \left\lbrack  {\mathop{\bigcup }\limits_{{x \in  \mathbb{Q}}}\left( {\{ x\}  \times  {\mathbb{R}}^{ + }}\right) }\right\rbrack   \cup  \left\lbrack  {\mathop{\bigcup }\limits_{{x \in  \mathbb{R} \smallsetminus  \mathbb{Q}}}\left( {\{ x\}  \times  \rbrack  - \infty ,0\lbrack }\right) }\right\rbrack  .
\]

a) Montrer que \( \Gamma \) est un connexe de \( {\mathbb{R}}^{2} \) .

> a) Show that \( \Gamma \) is a connected set of \( {\mathbb{R}}^{2} \) .

b) Montrer que \( \Gamma \) n’est pas connexe par arcs.

> b) Show that \( \Gamma \) is not path-connected.

Solution. a) Pour prouver la connexité de \( \Gamma \) , il suffit de montrer que toute fonction continue \( f : \Gamma \rightarrow \{ 0,1\} \) est constante.

> Solution. a) To prove the connectedness of \( \Gamma \), it suffices to show that any continuous function \( f : \Gamma \rightarrow \{ 0,1\} \) is constant.

Pour tout \( x \in \mathbb{Q} \) , l’ensemble \( \{ x\} \times {\mathbb{R}}^{ + } \) est une demi droite, donc connexe par arc, donc connexe, donc :

> For any \( x \in \mathbb{Q} \), the set \( \{ x\} \times {\mathbb{R}}^{ + } \) is a half-line, therefore path-connected, therefore connected, so:

\[
\left\{  \begin{array}{ll} \forall x \in  \mathbb{Q}, & f\text{ est constante sur }\{ x\}  \times  {\mathbb{R}}^{ + }, \\  \forall x \in  \mathbb{R} \smallsetminus  \mathbb{Q}, & f\text{ est constante sur }\{ x\}  \times  \rbrack  - \infty ,0\lbrack  \end{array}\right.
\]

de même

> likewise(*)

On peut donc définir une application \( g : \mathbb{R} \rightarrow \{ 0,1\} \) comme suit :

> We can therefore define a map \( g : \mathbb{R} \rightarrow \{ 0,1\} \) as follows:

- Si \( x \in  \mathbb{Q}, g\left( x\right) \) est la valeur prise par \( f \) sur \( \{ x\}  \times  {\mathbb{R}}^{ + } \) ,

> - If \( x \in  \mathbb{Q}, g\left( x\right) \) is the value taken by \( f \) on \( \{ x\}  \times  {\mathbb{R}}^{ + } \),

- si \( x \in  \mathbb{R} \smallsetminus  \mathbb{Q}, g\left( x\right) \) est la valeur prise par \( f \) sur \( \{ x\}  \times  \rbrack  - \infty ,0\lbrack \) .

> - if \( x \in  \mathbb{R} \smallsetminus  \mathbb{Q}, g\left( x\right) \) is the value taken by \( f \) on \( \{ x\}  \times  \rbrack  - \infty ,0\lbrack \).

Si on montre que \( g \) est constante. on aura prouvé, en vertu de (*), que \( f \) est constante et donc que \( \Gamma \) est connexe.

> If we show that \( g \) is constant, we will have proven, by virtue of (*), that \( f \) is constant and therefore that \( \Gamma \) is connected.

L’application \( g \) est localement constante. En effet.

> The map \( g \) is locally constant. Indeed.

- Soit \( {x}_{0} \in  \mathbb{Q} \) . On a \( \left( {{x}_{0},0}\right)  \in  \Gamma \) et comme \( f \) est continue en ce point et que \( \left\{  {f\left( {{x}_{0},0}\right) }\right\} \) est un ouvert de \( \{ 0,1\} ,{f}^{-1}\left( \left\{  {f\left( {{x}_{0},0}\right) }\right\}  \right) \) est un ouvert de \( \Gamma \) , de sorte que

> - Let \( {x}_{0} \in  \mathbb{Q} \). We have \( \left( {{x}_{0},0}\right)  \in  \Gamma \) and since \( f \) is continuous at this point and \( \left\{  {f\left( {{x}_{0},0}\right) }\right\} \) is an open set of \( \{ 0,1\} ,{f}^{-1}\left( \left\{  {f\left( {{x}_{0},0}\right) }\right\}  \right) \) is an open set of \( \Gamma \), so that

\[
\exists \alpha  > 0,\forall \left( {x, y}\right)  \in  \left( {\rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \left\lbrack  \times \right\rbrack   - \alpha ,\alpha \lbrack }\right)  \cap  \Gamma ,\;f\left( {x, y}\right)  = f\left( {{x}_{0},0}\right) .
\]

Donc si \( x \in \rbrack {x}_{0} - \alpha ,{x}_{0},{x}_{0} + \alpha \left\lbrack {, g\left( x\right) = g\left( {x}_{0}\right) }\right. \) (en effet, si \( x \) est rationnel, \( g\left( x\right) = f\left( {x,0}\right) = \; f\left( {{x}_{0},0}\right) = g\left( {x}_{0}\right) \) et si \( x \) est irrationnel, \( g\left( x\right) = f\left( {x, - \alpha /2}\right) = f\left( {{x}_{0},0}\right) = g\left( {x}_{0}\right) ). \) - Soit \( {x}_{0} \in \mathbb{R} \smallsetminus \mathbb{Q} \) . Fixons \( {y}_{0} < 0 \) . L’application \( f \) étant continue en \( \left( {{x}_{0},{y}_{0}}\right) \in \Gamma \) , on en déduit comme précédemment que

> So if \( x \in \rbrack {x}_{0} - \alpha ,{x}_{0},{x}_{0} + \alpha \left\lbrack {, g\left( x\right) = g\left( {x}_{0}\right) }\right. \) (indeed, if \( x \) is rational, \( g\left( x\right) = f\left( {x,0}\right) = \; f\left( {{x}_{0},0}\right) = g\left( {x}_{0}\right) \) and if \( x \) is irrational, \( g\left( x\right) = f\left( {x, - \alpha /2}\right) = f\left( {{x}_{0},0}\right) = g\left( {x}_{0}\right) ). \) - Let \( {x}_{0} \in \mathbb{R} \smallsetminus \mathbb{Q} \). Let us fix \( {y}_{0} < 0 \). The map \( f \) being continuous at \( \left( {{x}_{0},{y}_{0}}\right) \in \Gamma \), we deduce as before that

\[
\exists \alpha  > 0,\forall x \in  \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack  \cap  \left( {\mathbb{R} \smallsetminus  \mathbb{Q}}\right) ,\;f\left( {x,{y}_{0}}\right)  = f\left( {{x}_{0},{y}_{0}}\right)  = g\left( {x}_{0}\right) .
\]

Grâce à (*), on en déduit

> Thanks to (*), we deduce

\[
\forall x \in  \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack  \cap  \left( {\mathbb{R} \smallsetminus  \mathbb{Q}}\right) ,\;{f}_{\mid \{ x\}  \times  \rbrack  - \infty ,0\lbrack } = g\left( {x}_{0}\right) .
\]

On en tire \( g\left( x\right) = g\left( {x}_{0}\right) \) pour tout \( x \in \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \) . (En effet, si \( x \) est irrationnel, \( g\left( x\right) = \; {f}_{\left| {\{ x\} \times }\right| - \infty ,0\lbrack } = g\left( {x}_{0}\right) \) . Si \( x \) est rationnel, la densité de \( \mathbb{R} \smallsetminus \mathbb{Q} \) dans \( \mathbb{Q} \) permet d’affirmer l’existence d’une suite \( \left( {x}_{n}\right) \) de \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \cap \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \) qui converge vers \( x \) , et

> From this, we derive \( g\left( x\right) = g\left( {x}_{0}\right) \) for all \( x \in \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \) . (Indeed, if \( x \) is irrational, \( g\left( x\right) = \; {f}_{\left| {\{ x\} \times }\right| - \infty ,0\lbrack } = g\left( {x}_{0}\right) \) . If \( x \) is rational, the density of \( \mathbb{R} \smallsetminus \mathbb{Q} \) in \( \mathbb{Q} \) allows us to assert the existence of a sequence \( \left( {x}_{n}\right) \) of \( \rbrack {x}_{0} - \alpha ,{x}_{0} + \alpha \lbrack \cap \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \) that converges to \( x \) , and

\[
g\left( x\right)  = f\left( {x,0}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {{x}_{n}, - 1/n}\right)  = g\left( {x}_{0}\right) .)
\]

- Ainsi, \( g \) est localement constante autour des rationnels et des irrationnels, donc sur \( \mathbb{R} \) , donc continue sur \( \mathbb{R} \) . Comme \( g \) est à valeurs dans \( \{ 0,1\} \) et que \( \mathbb{R} \) est connexe, on en déduit que \( g \) est constante sur \( \mathbb{R} \) et le résultat.

> - Thus, \( g \) is locally constant around rationals and irrationals, therefore on \( \mathbb{R} \) , and thus continuous on \( \mathbb{R} \) . Since \( g \) takes values in \( \{ 0,1\} \) and \( \mathbb{R} \) is connected, we deduce that \( g \) is constant on \( \mathbb{R} \) and the result.

b) Raisonnons par l'absurde et supposons \( \Gamma \) connexe par arcs. En particulier, il existe un arc contenu dans \( \Gamma \) qui relie \( \left( {0,0}\right) \) et un point \( \left. {\left( {{x}_{0},{y}_{0}}\right) \in \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \times }\right\rbrack - \infty ,0\lbrack \) . En d’autres termes, il existe une application continue

> b) Let us reason by contradiction and assume \( \Gamma \) is path-connected. In particular, there exists a path contained in \( \Gamma \) that connects \( \left( {0,0}\right) \) and a point \( \left. {\left( {{x}_{0},{y}_{0}}\right) \in \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \times }\right\rbrack - \infty ,0\lbrack \) . In other words, there exists a continuous map

\[
\gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathbb{R}}^{2}\;t \mapsto  \left( {{\gamma }_{1}\left( t\right) ,{\gamma }_{2}\left( t\right) }\right)
\]

telle que \( \gamma \left( 0\right) = \left( {{x}_{0},{y}_{0}}\right) \in \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \times \rbrack - \infty ,0\left\lbrack {,\gamma \left( 1\right) = \left( {0,0}\right) }\right. \) et \( \forall t \in \left\lbrack {0,1}\right\rbrack ,\gamma \left( t\right) \in \Gamma \) .

> such that \( \gamma \left( 0\right) = \left( {{x}_{0},{y}_{0}}\right) \in \left( {\mathbb{R} \smallsetminus \mathbb{Q}}\right) \times \rbrack - \infty ,0\left\lbrack {,\gamma \left( 1\right) = \left( {0,0}\right) }\right. \) and \( \forall t \in \left\lbrack {0,1}\right\rbrack ,\gamma \left( t\right) \in \Gamma \) .

L’application \( {\gamma }_{1} \) étant continue, l’ensemble \( {\gamma }_{1}^{-1}\left( \left\{ {x}_{0}\right\} \right) \) est un fermé, non vide car il contient \( {x}_{0} \) . Donc \( \alpha = \sup {\gamma }_{1}^{-1}\left( \left\{ {x}_{0}\right\} \right) \) existe et \( {\gamma }_{1}\left( \alpha \right) = {x}_{0} \) . On a \( \alpha < 1 \) car \( {\gamma }_{1}\left( 1\right) = 0 \) . En résumé,

> Since the map \( {\gamma }_{1} \) is continuous, the set \( {\gamma }_{1}^{-1}\left( \left\{ {x}_{0}\right\} \right) \) is closed and non-empty because it contains \( {x}_{0} \) . Thus \( \alpha = \sup {\gamma }_{1}^{-1}\left( \left\{ {x}_{0}\right\} \right) \) exists and \( {\gamma }_{1}\left( \alpha \right) = {x}_{0} \) . We have \( \alpha < 1 \) because \( {\gamma }_{1}\left( 1\right) = 0 \) . In summary,

\[
{\gamma }_{1}\left( \alpha \right)  = {x}_{0}\;\text{ et }\;\forall t \in  \rbrack \alpha ,1\rbrack ,\;{\gamma }_{1}\left( t\right)  \neq  {x}_{0}.
\]

\( \left( {* * }\right) \)

> Comme \( {\gamma }_{1}\left( \alpha \right) = {x}_{0} \) et que \( \gamma \left( \alpha \right) \in \Gamma \) , on a \( {\gamma }_{2}\left( \alpha \right) < 0 \) . La continuité de \( {\gamma }_{2} \) assure l’existence d’un \( \varepsilon > 0 \) tel que \( {\gamma }_{2}\left( t\right) < 0 \) pour tout \( t \in \left\lbrack {\alpha ,\alpha + \varepsilon }\right\rbrack \) , et comme \( \gamma \left( t\right) \in \Gamma \) , on en déduit

Since \( {\gamma }_{1}\left( \alpha \right) = {x}_{0} \) and \( \gamma \left( \alpha \right) \in \Gamma \) , we have \( {\gamma }_{2}\left( \alpha \right) < 0 \) . The continuity of \( {\gamma }_{2} \) ensures the existence of a \( \varepsilon > 0 \) such that \( {\gamma }_{2}\left( t\right) < 0 \) for all \( t \in \left\lbrack {\alpha ,\alpha + \varepsilon }\right\rbrack \) , and since \( \gamma \left( t\right) \in \Gamma \) , we deduce

\[
\forall t \in  \left\lbrack  {\alpha ,\alpha  + \varepsilon }\right\rbrack  ,\;{\gamma }_{1}\left( t\right)  \notin  \mathbb{Q}.
\]

(***)

> D’après le théorème des valeurs intermédiaires, \( {\gamma }_{1}\left( \left\lbrack {\alpha ,\alpha + \varepsilon }\right\rbrack \right) \) est un intervalle, non réduit à un singleton d'après (**). Ceci est absurde d'après (***), d'où le résultat.

According to the intermediate value theorem, \( {\gamma }_{1}\left( \left\lbrack {\alpha ,\alpha + \varepsilon }\right\rbrack \right) \) is an interval, not reduced to a singleton according to (**). This is absurd according to (***), hence the result.

> EXERCICE 6 (ESPACES BIEN ENCHAÍNÉS). Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Soit \( \varepsilon > 0 \) . On dit que \( E \) est \( \varepsilon \) -enchaîné si pour tout \( \left( {a, b}\right) \in {E}^{2} \) , il existe \( n \in {\mathbb{N}}^{ * } \) et des points \( {x}_{0},\ldots ,{x}_{n} \) de \( E \) tels que \( {x}_{0} = a,{x}_{n} = b \) et \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) pour tout \( i \in \{ 1,\ldots , n\} \) . On dit que \( E \) est bien enchaîné si il est \( \varepsilon \) -enchaîné pour tout \( \varepsilon > 0 \) .

EXERCISE 6 (CHAIN-CONNECTED SPACES). Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. Let \( \varepsilon > 0 \) . We say that \( E \) is \( \varepsilon \) -chained if for all \( \left( {a, b}\right) \in {E}^{2} \) , there exist \( n \in {\mathbb{N}}^{ * } \) and points \( {x}_{0},\ldots ,{x}_{n} \) in \( E \) such that \( {x}_{0} = a,{x}_{n} = b \) and \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) for all \( i \in \{ 1,\ldots , n\} \) . We say that \( E \) is chain-connected if it is \( \varepsilon \) -chained for all \( \varepsilon > 0 \) .

> a) Si \( E \) est connexe, montrer que \( E \) est bien enchaîné.

a) If \( E \) is connected, show that \( E \) is chain-connected.

> b) Si \( E \) est compact et si \( E \) est bien enchaîné, montrer que \( E \) est connexe. Ce résultat reste-t-il vrai si \( E \) n’est pas supposé compact ?

b) If \( E \) is compact and if \( E \) is chain-connected, show that \( E \) is connected. Does this result remain true if \( E \) is not assumed to be compact?

> Solution. a) Soit \( \varepsilon > 0 \) . On définit la relation d’équivalence \( {\mathcal{R}}_{\varepsilon } \) sur \( E \) par : \( x{\mathcal{R}}_{\varepsilon }y \) si et seulement s’il existe \( n \in {\mathbb{N}}^{ * } \) et \( {x}_{0},\ldots ,{x}_{n} \in E \) tels que \( {x}_{0} = x,{x}_{n} = y \) et \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) pour tout \( i \in \{ 1,\ldots , n\} \) (on vérifie facilement que l’on a bien affaire à une relation d’équivalence). Soit \( x \in E \) . Nous montrons que la classe \( \dot{x} \) de \( x \) est ouverte et fermée.

Solution. a) Let \( \varepsilon > 0 \) . We define the equivalence relation \( {\mathcal{R}}_{\varepsilon } \) on \( E \) by: \( x{\mathcal{R}}_{\varepsilon }y \) if and only if there exist \( n \in {\mathbb{N}}^{ * } \) and \( {x}_{0},\ldots ,{x}_{n} \in E \) such that \( {x}_{0} = x,{x}_{n} = y \) and \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) for all \( i \in \{ 1,\ldots , n\} \) (it is easy to verify that this is indeed an equivalence relation). Let \( x \in E \) . We show that the class \( \dot{x} \) of \( x \) is open and closed.

> La classe \( \dot{x} \) est ouverte. En effet, soit \( y \in \dot{x} \) . Pour tout \( z \in \mathrm{B}\left( {y,\varepsilon }\right) \) , on a \( y{\mathcal{R}}_{\varepsilon }z \) donc \( z \in \dot{y} = \dot{x} \) . Ainsi, \( \mathrm{B}\left( {y,\varepsilon }\right) \subset \dot{x} \) , et ceci pour tout \( y \in \dot{x} \) , donc \( \dot{x} \) est ouvert.

The class \( \dot{x} \) is open. Indeed, let \( y \in \dot{x} \) . For all \( z \in \mathrm{B}\left( {y,\varepsilon }\right) \) , we have \( y{\mathcal{R}}_{\varepsilon }z \) so \( z \in \dot{y} = \dot{x} \) . Thus, \( \mathrm{B}\left( {y,\varepsilon }\right) \subset \dot{x} \) , and this for all \( y \in \dot{x} \) , so \( \dot{x} \) is open.

> La classe \( \dot{x} \) est également fermée car c’est le complémentaire de l’ouvert \( { \cup }_{y \notin \dot{x}}\dot{y} \) .

The class \( \dot{x} \) is also closed because it is the complement of the open set \( { \cup }_{y \notin \dot{x}}\dot{y} \) .

> Ainsi, \( \dot{x} \) , ouverte et fermée dans le connexe \( E \) , est égale à \( E \) . Ceci montre que \( E \) est \( \varepsilon \) -enchaîné pour tout \( \varepsilon > 0 \) , d’où le résultat.

Thus, \( \dot{x} \) , open and closed in the connected set \( E \) , is equal to \( E \) . This shows that \( E \) is \( \varepsilon \) -chained for all \( \varepsilon > 0 \) , hence the result.

> b) Raisonnons par l’absurde en supposant \( E \) non connexe. On peut écrire \( E = {F}_{1} \cup {F}_{2} \) où \( {F}_{1} \) et \( {F}_{2} \) sont deux fermés non vides disjoints. Un fermé dans un compact est compact, donc \( {F}_{1} \) et \( {F}_{2} \) sont compacts. Il existe donc \( {a}_{1} \in {F}_{1} \) et \( {a}_{2} \in {F}_{2} \) tels que \( \mathrm{d}\left( {{a}_{1},{a}_{2}}\right) = \mathrm{d}\left( {{F}_{1},{F}_{2}}\right) \) (voir

b) Let us reason by contradiction by assuming \( E \) is not connected. We can write \( E = {F}_{1} \cup {F}_{2} \) where \( {F}_{1} \) and \( {F}_{2} \) are two non-empty disjoint closed sets. A closed set in a compact set is compact, so \( {F}_{1} \) and \( {F}_{2} \) are compact. There exist \( {a}_{1} \in {F}_{1} \) and \( {a}_{2} \in {F}_{2} \) such that \( \mathrm{d}\left( {{a}_{1},{a}_{2}}\right) = \mathrm{d}\left( {{F}_{1},{F}_{2}}\right) \) (see

> l’exercice 3 page 33). Comme \( {F}_{1} \cap {F}_{2} = \varnothing ,{a}_{1} \neq {a}_{2} \) donc \( \varepsilon = \mathrm{d}\left( {{a}_{1},{a}_{2}}\right) > 0 \) , de sorte que \( \mathrm{d}\left( {x, y}\right) \geq \varepsilon \) pour tout \( \left( {x, y}\right) \in {F}_{1} \times {F}_{2} \) . Comme \( E \) est bien enchaîné, on peut trouver une chaîne \( \left( {{x}_{0},\ldots ,{x}_{n}}\right) \in {E}^{n + 1} \) telle que \( {x}_{0} \in {F}_{1},{x}_{n} = {y}_{0} \in {F}_{2} \) , et \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) pour tout \( i \in \{ 1,\ldots , n\} \) . Il existe un indice \( i \in \{ 1,\ldots , n\} \) tel que \( {x}_{i - 1} \in {F}_{1} \) et \( {x}_{i} \in {F}_{2} \) (ceci car \( {x}_{0} \in {F}_{1} \) et \( {x}_{n} \in {F}_{2} \) ), et alors \( \mathrm{d}\left( {{x}_{i - 1},{x}_{i}}\right) \geq \mathrm{d}\left( {{F}_{1},{F}_{2}}\right) = \varepsilon \) , ce qui est absurde. L’espace métrique \( E \) est donc connexe.

exercise 3 on page 33). Since \( {F}_{1} \cap {F}_{2} = \varnothing ,{a}_{1} \neq {a}_{2} \) then \( \varepsilon = \mathrm{d}\left( {{a}_{1},{a}_{2}}\right) > 0 \) , so that \( \mathrm{d}\left( {x, y}\right) \geq \varepsilon \) for all \( \left( {x, y}\right) \in {F}_{1} \times {F}_{2} \) . As \( E \) is well-chained, we can find a chain \( \left( {{x}_{0},\ldots ,{x}_{n}}\right) \in {E}^{n + 1} \) such that \( {x}_{0} \in {F}_{1},{x}_{n} = {y}_{0} \in {F}_{2} \) , and \( \mathrm{d}\left( {{x}_{i},{x}_{i - 1}}\right) < \varepsilon \) for all \( i \in \{ 1,\ldots , n\} \) . There exists an index \( i \in \{ 1,\ldots , n\} \) such that \( {x}_{i - 1} \in {F}_{1} \) and \( {x}_{i} \in {F}_{2} \) (this is because \( {x}_{0} \in {F}_{1} \) and \( {x}_{n} \in {F}_{2} \) ), and then \( \mathrm{d}\left( {{x}_{i - 1},{x}_{i}}\right) \geq \mathrm{d}\left( {{F}_{1},{F}_{2}}\right) = \varepsilon \) , which is absurd. The metric space \( E \) is therefore connected.

> Si \( E \) n’est pas supposé compact, le résultat est faux. Par exemple \( \mathbb{Q} \) (muni de la métrique \( \mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| ) \) est bien enchaîné (car dense dans \( \mathbb{R} \) ) mais non connexe.

If \( E \) is not assumed to be compact, the result is false. For example \( \mathbb{Q} \) (equipped with the metric \( \mathrm{d}\left( {x, y}\right) = \left| {x - y}\right| ) \) is well-chained (because it is dense in \( \mathbb{R} \) ) but not connected.

> EXERCICE 7. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique compact et \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( E \) telle que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{u}_{n},{u}_{n + 1}}\right) = 0 \) . Montrer que l’ensemble des valeurs d’adhérence de \( \left( {u}_{n}\right) \) est connexe.

EXERCISE 7. Let \( \left( {E,\mathrm{\;d}}\right) \) be a compact metric space and \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) a sequence of \( E \) such that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{u}_{n},{u}_{n + 1}}\right) = 0 \) . Show that the set of limit points of \( \left( {u}_{n}\right) \) is connected.

> Solution. Pour tout \( p \in \mathbb{N} \) , on note \( {A}_{p} = \left\{ {{u}_{n}, n \geq p}\right\} \) . On sait que l’ensemble \( \Gamma \) des valeurs d’adhérence de \( \left( {u}_{n}\right) \) est égal à \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \) . C’est donc un fermé, et comme \( E \) est compact, \( \Gamma \) est compact.

Solution. For any \( p \in \mathbb{N} \), we denote \( {A}_{p} = \left\{ {{u}_{n}, n \geq p}\right\} \). We know that the set \( \Gamma \) of limit points of \( \left( {u}_{n}\right) \) is equal to \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \). It is therefore a closed set, and since \( E \) is compact, \( \Gamma \) is compact.

> Supposons \( \Gamma \) non connexe, de sorte que l’on peut écrire \( \Gamma = A \cup B \) où \( A \) et \( B \) sont deux fermés non vides disjoints de \( \Gamma \) . Comme \( \Gamma \) et compact, \( A \) et \( B \) sont même compacts et donc (voir l’exercice 3 page 33) \( \alpha = \mathrm{d}\left( {A, B}\right) > 0 \) puisque \( A \) et \( B \) sont disjoints. Notons

Suppose \( \Gamma \) is not connected, such that we can write \( \Gamma = A \cup B \) where \( A \) and \( B \) are two non-empty disjoint closed sets of \( \Gamma \). Since \( \Gamma \) is compact, \( A \) and \( B \) are also compact and therefore (see exercise 3 page 33) \( \alpha = \mathrm{d}\left( {A, B}\right) > 0 \) since \( A \) and \( B \) are disjoint. Let us denote

\[
{A}^{\prime } = \left\{  {x \in  E \mid  \mathrm{d}\left( {x, A}\right)  < \frac{\alpha }{3}}\right\}   = \mathop{\bigcup }\limits_{{x \in  A}}\mathrm{\;B}\left( {x,\frac{\alpha }{3}}\right) \;\text{ et }\;{B}^{\prime } = \left\{  {x \in  E \mid  \mathrm{d}\left( {x, B}\right)  < \frac{\alpha }{3}}\right\}  .
\]

Les ensembles \( {A}^{\prime } \) et \( {B}^{\prime } \) sont ouverts donc \( K = E \smallsetminus \left( {{A}^{\prime } \cup {B}^{\prime }}\right) \) est fermé dans le compact \( E \) , donc compact. Nous allons montrer que \( \left( {u}_{n}\right) \) admet au moins une valeur d’adhérence dans \( K \) , ce qui sera une absurdité car \( \Gamma \cap K = \varnothing \) .

> The sets \( {A}^{\prime } \) and \( {B}^{\prime } \) are open, so \( K = E \smallsetminus \left( {{A}^{\prime } \cup {B}^{\prime }}\right) \) is closed in the compact \( E \), and therefore compact. We will show that \( \left( {u}_{n}\right) \) admits at least one limit point in \( K \), which would be an absurdity because \( \Gamma \cap K = \varnothing \).

Par hypothèse, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{u}_{n},{u}_{n + 1}}\right) = 0 \) donc

> By hypothesis, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {{u}_{n},{u}_{n + 1}}\right) = 0 \) therefore

\[
\exists {N}_{0} \in  \mathbb{N},\forall n \geq  {N}_{0},\;\mathrm{\;d}\left( {{u}_{n},{u}_{n + 1}}\right)  < \frac{\alpha }{3}.
\]

(*)

![bo_d7fjkrs91nqc73ereoog_50_368_1276_902_421_0.jpg](images/gourdon_analysis_fr_en_025_bod7fjkrs91nqc73ereoog5036812769024210.jpg)

Figure 2. Les compacts \( A, B, E \) et \( K = E \smallsetminus \left( {{A}^{\prime } \cup {B}^{\prime }}\right) \)

> Figure 2. The compact sets \( A, B, E \) and \( K = E \smallsetminus \left( {{A}^{\prime } \cup {B}^{\prime }}\right) \)

Soit \( N \) un entier quelconque supérieur à \( {N}_{0} \) . Donnons nous \( {x}_{0} \in A \) . Le point \( {x}_{0} \) est valeur d’adhérence de \( \left( {u}_{n}\right) \) donc il existe \( {n}_{1} > N \) tel que \( \mathrm{d}\left( {{x}_{0},{u}_{{n}_{1}}}\right) < \alpha /3 \) , donc \( {u}_{{n}_{1}} \in {A}^{\prime } \) . Si \( {y}_{0} \in B \) , \( {y}_{0} \) est aussi valeur d’adhérence de \( \left( {u}_{n}\right) \) donc il existe \( {n}_{2} > {n}_{1} \) tel que \( \mathrm{d}\left( {{y}_{0},{u}_{{n}_{2}}}\right) < \alpha /3 \) , de sorte que \( {u}_{{n}_{2}} \in {B}^{\prime } \) . Notons maintenant \( {n}_{0} \) le premier entier supérieur à \( {n}_{1} \) tel que \( {u}_{{n}_{0}} \notin {A}^{\prime } \) (un tel entier existe car \( {u}_{{n}_{2}} \notin {A}^{\prime } \) ). On a \( {u}_{{n}_{0} - 1} \in {A}^{\prime } \) , donc d’après (*)

> Let \( N \) be any integer greater than \( {N}_{0} \). Let us choose \( {x}_{0} \in A \). The point \( {x}_{0} \) is a limit point of \( \left( {u}_{n}\right) \), so there exists \( {n}_{1} > N \) such that \( \mathrm{d}\left( {{x}_{0},{u}_{{n}_{1}}}\right) < \alpha /3 \), and thus \( {u}_{{n}_{1}} \in {A}^{\prime } \). If \( {y}_{0} \in B \), \( {y}_{0} \) is also a limit point of \( \left( {u}_{n}\right) \), so there exists \( {n}_{2} > {n}_{1} \) such that \( \mathrm{d}\left( {{y}_{0},{u}_{{n}_{2}}}\right) < \alpha /3 \), such that \( {u}_{{n}_{2}} \in {B}^{\prime } \). Let us now denote \( {n}_{0} \) as the first integer greater than \( {n}_{1} \) such that \( {u}_{{n}_{0}} \notin {A}^{\prime } \) (such an integer exists because \( {u}_{{n}_{2}} \notin {A}^{\prime } \)). We have \( {u}_{{n}_{0} - 1} \in {A}^{\prime } \), therefore according to (*)

\[
\mathrm{d}\left( {{u}_{{n}_{0}}, B}\right)  \geq  \mathrm{d}\left( {{u}_{{n}_{0} - 1}, B}\right)  - \mathrm{d}\left( {{u}_{{n}_{0} - 1},{u}_{{n}_{0}}}\right)  \geq  \mathrm{d}\left( {A, B}\right)  - \mathrm{d}\left( {{u}_{{n}_{0} - 1}, A}\right)  - \mathrm{d}\left( {{u}_{{n}_{0} - 1},{u}_{{n}_{0}}}\right)  > \frac{\alpha }{3},
\]

ce qui prouve que \( {u}_{{n}_{0}} \notin {B}^{\prime } \) . Comme de plus \( {u}_{{n}_{0}} \notin {A}^{\prime } \) , on a \( {u}_{{n}_{0}} \in K \) .

> which proves that \( {u}_{{n}_{0}} \notin {B}^{\prime } \). Since, moreover, \( {u}_{{n}_{0}} \notin {A}^{\prime } \), we have \( {u}_{{n}_{0}} \in K \).

Résumons. Nous venons de montrer que pour tout \( N \geq {N}_{0} \) , il existe \( {n}_{0} \geq N \) tel que \( {u}_{{n}_{0}} \in K \) . On peut donc construire une sous-suite \( \left( {u}_{\varphi \left( n\right) }\right) \) de \( \left( {u}_{n}\right) \) qui prend ses valeurs dans \( K \) . Comme

> Let us summarize. We have just shown that for any \( N \geq {N}_{0} \) , there exists \( {n}_{0} \geq N \) such that \( {u}_{{n}_{0}} \in K \) . We can therefore construct a subsequence \( \left( {u}_{\varphi \left( n\right) }\right) \) of \( \left( {u}_{n}\right) \) which takes its values in \( K \) . Since

\( K \) est compact, \( \left( {u}_{\varphi \left( n\right) }\right) \) admet au moins une valeur d’adhérence dans \( K \) , donc \( \left( {u}_{n}\right) \) admet au moins une valeur d’adhérence dans \( K \) . Ceci est impossible car \( \Gamma \cap K = \varnothing \) . L’ensemble \( \Gamma \) est donc connexe.

> \( K \) is compact, \( \left( {u}_{\varphi \left( n\right) }\right) \) admits at least one cluster point in \( K \) , so \( \left( {u}_{n}\right) \) admits at least one cluster point in \( K \) . This is impossible because \( \Gamma \cap K = \varnothing \) . The set \( \Gamma \) is therefore connected.

EXERCICE 8 ( \( \mathbb{R} \) ET \( {\mathbb{R}}^{2} \) NE SONT PAS HOMÉOMORPHES). Il est bien connu que \( \mathbb{R} \) et \( {\mathbb{R}}^{2} \) sont deux ensembles équipotents, autrement dit il existe une bijection \( f \) de \( \mathbb{R} \) dans \( {\mathbb{R}}^{2} \) . Montrer qu'une telle bijection ne peut pas être un homéomorphisme.

> EXERCISE 8 ( \( \mathbb{R} \) AND \( {\mathbb{R}}^{2} \) ARE NOT HOMEOMORPHIC). It is well known that \( \mathbb{R} \) and \( {\mathbb{R}}^{2} \) are two equipotent sets, in other words there exists a bijection \( f \) from \( \mathbb{R} \) to \( {\mathbb{R}}^{2} \) . Show that such a bijection cannot be a homeomorphism.

Solution. Supposons l’existence d’un homéomorphisme \( f \) de \( \mathbb{R} \) sur \( {\mathbb{R}}^{2} \) . L’ensemble \( {\mathbb{R}}^{2} \smallsetminus \{ 0\} \) est connexe (car trivialement connexe par arcs), et \( {f}^{-1} \) étant continue, \( {f}^{-1}\left( {{\mathbb{R}}^{2}\smallsetminus \{ 0\} }\right) \) est un connexe de \( \mathbb{R} \) . Or \( f \) étant une bijection,

> Solution. Suppose there exists a homeomorphism \( f \) from \( \mathbb{R} \) onto \( {\mathbb{R}}^{2} \) . The set \( {\mathbb{R}}^{2} \smallsetminus \{ 0\} \) is connected (as it is trivially path-connected), and since \( {f}^{-1} \) is continuous, \( {f}^{-1}\left( {{\mathbb{R}}^{2}\smallsetminus \{ 0\} }\right) \) is a connected subset of \( \mathbb{R} \) . However, since \( f \) is a bijection,

\[
\left. {{f}^{-1}\left( {{\mathbb{R}}^{2}\smallsetminus \{ 0\} }\right)  = \mathbb{R} \smallsetminus  \left\{  {{f}^{-1}\left( 0\right) }\right\}   = }\right\rbrack   - \infty ,{f}^{-1}\left( 0\right) \left\lbrack  \cup \right\rbrack  {f}^{-1}\left( 0\right) , + \infty \lbrack
\]

n'est pas connexe. Ceci est absurde, d'où le résultat.

> is not connected. This is absurd, hence the result.

EXERCICE 9 (THÉORÉME DE DARBOUX, PREUVE TOPOLOGIQUE). Soit \( f : \mathbb{R} \rightarrow \mathbb{R} \) une application dérivable sur \( \mathbb{R} \) (mais pas forcément de classe \( {\mathcal{C}}^{1} \) ). Soit \( I \) un intervalle ouvert non vide de \( \mathbb{R} \) . En considérant l’ensemble

> EXERCISE 9 (DARBOUX'S THEOREM, TOPOLOGICAL PROOF). Let \( f : \mathbb{R} \rightarrow \mathbb{R} \) be a differentiable function on \( \mathbb{R} \) (but not necessarily of class \( {\mathcal{C}}^{1} \) ). Let \( I \) be a non-empty open interval of \( \mathbb{R} \) . By considering the set

\[
\Gamma  = \left\{  {\frac{f\left( x\right)  - f\left( y\right) }{x - y},\left( {x, y}\right)  \in  {I}^{2}\text{ et }x < y}\right\}  ,
\]

montrer que \( {f}^{\prime }\left( I\right) \) est un intervalle de \( \mathbb{R} \) .

> show that \( {f}^{\prime }\left( I\right) \) is an interval of \( \mathbb{R} \) .

Solution. Notons \( A \) l’ensemble \( \left\{ {\left( {x, y}\right) \in {I}^{2}, x < y}\right\} \) . Cet ensemble est connexe (il est même convexe). L'application

> Solution. Let \( A \) denote the set \( \left\{ {\left( {x, y}\right) \in {I}^{2}, x < y}\right\} \) . This set is connected (it is even convex). The mapping

\[
F : A \rightarrow  \mathbb{R}\;\left( {x, y}\right)  \mapsto  \frac{f\left( x\right)  - f\left( y\right) }{x - y}
\]

est continue, donc \( f\left( A\right) = \Gamma \) , image continue d’un connexe, est connexe.

> is continuous, so \( f\left( A\right) = \Gamma \) , the continuous image of a connected set, is connected.

On a \( {f}^{\prime }\left( I\right) \subset \overline{\Gamma } \) . En effet, si \( x \in I \) et si \( \left( {x}_{n}\right) \) est une suite de \( I \) qui tend vers \( x \) telle que \( {x}_{n} > x \) pour tout \( n \) , on a \( {f}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}F\left( {x,{x}_{n}}\right) \) .

> We have \( {f}^{\prime }\left( I\right) \subset \overline{\Gamma } \) . Indeed, if \( x \in I \) and if \( \left( {x}_{n}\right) \) is a sequence in \( I \) that converges to \( x \) such that \( {x}_{n} > x \) for all \( n \) , we have \( {f}^{\prime }\left( x\right) = \mathop{\lim }\limits_{{n \rightarrow \infty }}F\left( {x,{x}_{n}}\right) \) .

D’après le théorème des accroissements finis, on a \( \Gamma \subset {f}^{\prime }\left( I\right) \) . Finalement, \( \Gamma \subset {f}^{\prime }\left( I\right) \subset \overline{\Gamma } \) , donc \( {f}^{\prime }\left( I\right) \) est connexe d’après la proposition 4. Les connexes de \( \mathbb{R} \) étant les intervalles, on en déduit le résultat.

> According to the mean value theorem, we have \( \Gamma \subset {f}^{\prime }\left( I\right) \). Finally, \( \Gamma \subset {f}^{\prime }\left( I\right) \subset \overline{\Gamma } \), therefore \( {f}^{\prime }\left( I\right) \) is connected according to proposition 4. Since the connected sets of \( \mathbb{R} \) are intervals, we deduce the result.

Remarque. Ce résultat est prouvé avec des moyens différents à l'exercice 4 page 80.

> Remark. This result is proven using different methods in exercise 4 on page 80.
