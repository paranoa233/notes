#### 1.6. Exercises

*Français : 1.6. Exercices*

EXERCICE 1. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique.

> EXERCISE 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space.

a) Soit \( a \in E \) et \( r > 0 \) . Montrer que \( \overline{\mathrm{B}\left( {a, r}\right) } \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) . Peut-on affirmer, dans le cas général, que \( \overline{\mathrm{B}\left( {a, r}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) ?

> a) Let \( a \in E \) and \( r > 0 \). Show that \( \overline{\mathrm{B}\left( {a, r}\right) } \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \). Can we assert, in the general case, that \( \overline{\mathrm{B}\left( {a, r}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \)?

b) Si \( E \) est un \( \mathbb{R} \) -e.v.n, montrer que \( \overline{\mathrm{B}\left( {0,1}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) .

> b) If \( E \) is a \( \mathbb{R} \)-n.v.s., show that \( \overline{\mathrm{B}\left( {0,1}\right) } = {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \).

Solution. a) On a \( \mathrm{B}\left( {a, r}\right) \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) . Comme \( {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) est fermé et que \( \overline{\mathrm{B}\left( {a, r}\right) } \) est le plus petit fermé contenant \( \mathrm{B}\left( {a, r}\right) \) , on en déduit \( \overline{\mathrm{B}\left( {a, r}\right) } \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) .

> Solution. a) We have \( \mathrm{B}\left( {a, r}\right) \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \). Since \( {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \) is closed and \( \overline{\mathrm{B}\left( {a, r}\right) } \) is the smallest closed set containing \( \mathrm{B}\left( {a, r}\right) \), we deduce \( \overline{\mathrm{B}\left( {a, r}\right) } \subset {\mathrm{B}}_{\mathrm{f}}\left( {a, r}\right) \).

L'égalité n'a pas lieu dans le cas général, comme nous allons le vérifier sur un contre-exemple. Si \( E \) est muni de sa distance discrète d (définie par \( \mathrm{d}\left( {x, y}\right) = 0 \) si \( x = y, = 1 \) si \( x \neq y \) ), on a \( \mathrm{B}\left( {a,1}\right) = \{ a\} \) , fermé, et \( {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) = E \) . Ainsi, dès que \( E \) possède plus d’un élément, \( \overline{\mathrm{B}\left( {a,1}\right) } = \; \{ a\} \neq E = {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) . \)

> The equality does not hold in the general case, as we will verify with a counterexample. If \( E \) is equipped with its discrete distance d (defined by \( \mathrm{d}\left( {x, y}\right) = 0 \) if \( x = y, = 1 \) if \( x \neq y \)), we have \( \mathrm{B}\left( {a,1}\right) = \{ a\} \), closed, and \( {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) = E \). Thus, as soon as \( E \) has more than one element, \( \overline{\mathrm{B}\left( {a,1}\right) } = \; \{ a\} \neq E = {\mathrm{B}}_{\mathrm{f}}\left( {a,1}\right) . \)

b) D’après la question précédente, il suffit de montrer l’inclusion \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \subset \overline{\mathrm{B}\left( {0,1}\right) } \) . Soit \( x \in \; {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \) . Si \( \parallel x\parallel < 1 \) , alors \( x \in \mathrm{B}\left( {0,1}\right) \subset \overline{\mathrm{B}\left( {0,1}\right) } \) et c’est terminé. Sinon \( \parallel x\parallel = 1 \) , et alors pour tout \( \varepsilon > 0 \) , il existe \( y \in \mathrm{B}\left( {0,1}\right) \) tel que \( \parallel x - y\parallel < \varepsilon \) (prendre par exemple \( y = \left( {1 - \varepsilon /2}\right) x \) ). En d’autres termes, \( x \in \overline{\mathrm{B}\left( {0,1}\right) } \) d’après la proposition 4, d’où le résultat.

> b) According to the previous question, it suffices to show the inclusion \( {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \subset \overline{\mathrm{B}\left( {0,1}\right) } \). Let \( x \in \; {\mathrm{B}}_{\mathrm{f}}\left( {0,1}\right) \). If \( \parallel x\parallel < 1 \), then \( x \in \mathrm{B}\left( {0,1}\right) \subset \overline{\mathrm{B}\left( {0,1}\right) } \) and we are done. Otherwise \( \parallel x\parallel = 1 \), and then for all \( \varepsilon > 0 \), there exists \( y \in \mathrm{B}\left( {0,1}\right) \) such that \( \parallel x - y\parallel < \varepsilon \) (take for example \( y = \left( {1 - \varepsilon /2}\right) x \)). In other words, \( x \in \overline{\mathrm{B}\left( {0,1}\right) } \) according to proposition 4, hence the result.

EXERCICE 2. Soit \( A \subset \mathbb{R} \) tel que tout point de \( A \) est isolé dans \( A \) . Montrer que \( A \) est au plus dénombrable.

> EXERCISE 2. Let \( A \subset \mathbb{R} \) be such that every point of \( A \) is isolated in \( A \). Show that \( A \) is at most countable.

Solution. Nous allons associer à chaque élément de \( A \) un rationnel de manière injective. Tout élément \( a \in A \) est isolé dans \( A \) , donc

> Solution. We will associate with each element of \( A \) a rational number in an injective manner. Every element \( a \in A \) is isolated in \( A \), therefore

\[
\exists {r}_{a} > 0,\;\rbrack a - {r}_{a}, a + {r}_{a}\lbrack  \cap  A = \{ a\} .
\]

(*)

> Comme \( \mathbb{Q} \) est dense dans \( \mathbb{R} \) , il existe \( {q}_{a} \in \mathbb{Q} \) tel que \( {q}_{a} \in \rbrack a - {r}_{a}/2, a + {r}_{a}/2\lbrack \) .

Since \( \mathbb{Q} \) is dense in \( \mathbb{R} \), there exists \( {q}_{a} \in \mathbb{Q} \) such that \( {q}_{a} \in \rbrack a - {r}_{a}/2, a + {r}_{a}/2\lbrack \).

> Montrons maintenant que l’application \( \varphi : A \rightarrow \mathbb{Q}\;a \mapsto {q}_{a} \) est injective. Si \( {q}_{a} = {q}_{b} = q \) , avec \( a, b \in A \) , alors \( \left| {q - a}\right| < {r}_{a}/2 \) (car \( q = {q}_{a} \) est choisi dans \( \rbrack a - {r}_{a}/2, a + {r}_{a}/2\lbrack ) \) , de même, \( \left| {q - b}\right| < {r}_{b}/2 \) , donc

Let us now show that the mapping \( \varphi : A \rightarrow \mathbb{Q}\;a \mapsto {q}_{a} \) is injective. If \( {q}_{a} = {q}_{b} = q \), with \( a, b \in A \), then \( \left| {q - a}\right| < {r}_{a}/2 \) (because \( q = {q}_{a} \) is chosen in \( \rbrack a - {r}_{a}/2, a + {r}_{a}/2\lbrack ) \), likewise, \( \left| {q - b}\right| < {r}_{b}/2 \), therefore

\[
\left| {a - b}\right|  = \left| {\left( {q - b}\right)  - \left( {q - a}\right) }\right|  \leq  \left| {q - b}\right|  + \left| {q - a}\right|  < \frac{{r}_{a} + {r}_{b}}{2}.
\]

\( \left( {* * }\right) \)

> L’un des réels \( {r}_{a},{r}_{b} \) est plus grand que l’autre, par exemple \( {r}_{a} \geq {r}_{b} \) . L’inégalité (**) entraîne \( \left| {a - b}\right| < {r}_{a} \) , ce qui d’après (*) implique \( b = a \) car \( b \in A \) .

One of the real numbers \( {r}_{a},{r}_{b} \) is greater than the other, for example \( {r}_{a} \geq {r}_{b} \). Inequality (**) leads to \( \left| {a - b}\right| < {r}_{a} \), which according to (*) implies \( b = a \) because \( b \in A \).

> Finalement, nous avons construit une application injective \( \varphi : \;A \rightarrow \mathbb{Q} \) , et comme \( \mathbb{Q} \) est dénombrable, on en déduit que \( A \) est au plus dénombrable.

Finally, we have constructed an injective mapping \( \varphi : \;A \rightarrow \mathbb{Q} \), and since \( \mathbb{Q} \) is countable, we deduce that \( A \) is at most countable.

> Remarque. Le raisonnement effectué dans la démonstration reste valable pour \( A \subset {\mathbb{R}}^{n} \) , en utilisant le fait que \( {\mathbb{Q}}^{n} \) est dénombrable.

Remark. The reasoning used in the proof remains valid for \( A \subset {\mathbb{R}}^{n} \), by using the fact that \( {\mathbb{Q}}^{n} \) is countable.

> EXERCICE 3. Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) une fonction uniformément continue sur \( {\mathbb{R}}^{ + } \) . Montrer

EXERCISE 3. Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) be a uniformly continuous function on \( {\mathbb{R}}^{ + } \). Show

\[
\exists \alpha ,\beta  > 0,\forall x \in  {\mathbb{R}}^{ + },\;\left| {f\left( x\right) }\right|  \leq  {\alpha x} + \beta .
\]

Solution. L’application \( f \) étant uniformément continue, on a l’existence de \( \eta > 0 \) tel que

> Solution. Since the mapping \( f \) is uniformly continuous, there exists \( \eta > 0 \) such that

\[
\forall \left( {x, y}\right)  \in  {\left( {\mathbb{R}}^{ + }\right) }^{2},\left| {x - y}\right|  \leq  \eta ,\;\left| {f\left( x\right)  - f\left( y\right) }\right|  \leq  1.
\]

(*)

> Maintenant, fixons \( x \in {\mathbb{R}}^{ + } \) et notons \( n = \left\lbrack {x/\eta }\right\rbrack \) (partie entière de \( x/\eta \) ). On a \( {n\eta } \leq x < \left( {n + 1}\right) \eta \) , donc

Now, let us fix \( x \in {\mathbb{R}}^{ + } \) and denote \( n = \left\lbrack {x/\eta }\right\rbrack \) (the integer part of \( x/\eta \) ). We have \( {n\eta } \leq x < \left( {n + 1}\right) \eta \) , therefore

\[
\left| {f\left( x\right)  - f\left( 0\right) }\right|  = \left| {f\left( x\right)  - f\left( {n\eta }\right)  + \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left\lbrack  {f\left( {\left( {k + 1}\right) \eta }\right)  - f\left( {k\eta }\right) }\right\rbrack  }\right|
\]

\[
\leq  \left| {f\left( x\right)  - f\left( {n\eta }\right) }\right|  + \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left| {f\left( {\left( {k + 1}\right) \eta }\right)  - f\left( {k\eta }\right) }\right|  \leq  1 + \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}1 = 1 + n
\]

ce qui entraîne

> which implies

\[
\left| {f\left( x\right) }\right|  \leq  \left| {f\left( 0\right) }\right|  + 1 + n \leq  \left| {f\left( 0\right) }\right|  + 1 + \frac{x}{\eta } = \beta  + {\alpha x}
\]

avec \( \beta = \left| {f\left( 0\right) }\right| + 1 \) et \( \alpha = 1/\eta \) . Les réels \( \alpha \) et \( \beta \) sont indépendants du choix de \( x \) , donc ceci est vrai pour tout \( x \in {\mathbb{R}}^{ + } \) , d’où le résultat.

> with \( \beta = \left| {f\left( 0\right) }\right| + 1 \) and \( \alpha = 1/\eta \) . The real numbers \( \alpha \) and \( \beta \) are independent of the choice of \( x \) , so this is true for all \( x \in {\mathbb{R}}^{ + } \) , hence the result.

EXERCICE 4. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique.

> EXERCISE 4. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space.

1 / Soit \( A \subset E \) . Montrer que l’application \( E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {x, A}\right) \) est continue sur \( E \) (on rappelle que \( \mathrm{d}\left( {x, A}\right) = \mathop{\inf }\limits_{{y \in A}}\mathrm{\;d}\left( {x, y}\right) ) \) .

> 1 / Let \( A \subset E \) . Show that the map \( E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {x, A}\right) \) is continuous on \( E \) (recall that \( \mathrm{d}\left( {x, A}\right) = \mathop{\inf }\limits_{{y \in A}}\mathrm{\;d}\left( {x, y}\right) ) \) ).

2/ Soient \( A \) et \( B \) deux fermés disjoints de \( E \) .

> 2/ Let \( A \) and \( B \) be two disjoint closed sets of \( E \) .

a) Montrer qu’il existe \( f : E \rightarrow \mathbb{R} \) continue, \( 0 \leq f \leq 1 \) , telle que \( A = {f}^{-1}\left( {\{ 0\} }\right) \) et \( B = {f}^{-1}\left( {\{ 1\} }\right) . \)

> a) Show that there exists a continuous function \( f : E \rightarrow \mathbb{R} \) , \( 0 \leq f \leq 1 \) , such that \( A = {f}^{-1}\left( {\{ 0\} }\right) \) and \( B = {f}^{-1}\left( {\{ 1\} }\right) . \)

b) En déduire l’existence de deux ouverts \( U \) et \( V \) de \( E \) , disjoints, tels que \( A \subset U \) et \( B \subset V \) .

> b) Deduce the existence of two disjoint open sets \( U \) and \( V \) of \( E \) , such that \( A \subset U \) and \( B \subset V \) .

Solution. 1 / On va montrer que l’application \( x \mapsto \mathrm{d}\left( {x, A}\right) \) est 1-lipschitzienne. Fixons \( \left( {{x}_{1},{x}_{2}}\right) \in \; {E}^{2} \) . D’après l’inégalité triangulaire,

> Solution. 1 / We will show that the map \( x \mapsto \mathrm{d}\left( {x, A}\right) \) is 1-Lipschitz. Let us fix \( \left( {{x}_{1},{x}_{2}}\right) \in \; {E}^{2} \) . According to the triangle inequality,

\[
\forall y \in  A,\;\mathrm{\;d}\left( {{x}_{1}, A}\right)  \leq  \mathrm{d}\left( {{x}_{1}, y}\right)  \leq  \mathrm{d}\left( {{x}_{1},{x}_{2}}\right)  + \mathrm{d}\left( {{x}_{2}, y}\right) .
\]

L’inégalité \( \mathrm{d}\left( {{x}_{1}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) + \mathrm{d}\left( {{x}_{2}, y}\right) \) étant vrai pour tout \( y \in A \) , on en déduit \( \mathrm{d}\left( {{x}_{1}, A}\right) \leq \; \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) + \mathrm{d}\left( {{x}_{2}, A}\right) \) . Autrement dit, \( \mathrm{d}\left( {{x}_{1}, A}\right) - \mathrm{d}\left( {{x}_{2}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) . On montrerait de même \( \mathrm{d}\left( {{x}_{2}, A}\right) - \mathrm{d}\left( {{x}_{1}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) , ce qui prouve \( \left| {\mathrm{d}\left( {{x}_{1}, A}\right) - \mathrm{d}\left( {{x}_{2}, A}\right) }\right| \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) .

> Since the inequality \( \mathrm{d}\left( {{x}_{1}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) + \mathrm{d}\left( {{x}_{2}, y}\right) \) is true for all \( y \in A \) , we deduce \( \mathrm{d}\left( {{x}_{1}, A}\right) \leq \; \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) + \mathrm{d}\left( {{x}_{2}, A}\right) \) . In other words, \( \mathrm{d}\left( {{x}_{1}, A}\right) - \mathrm{d}\left( {{x}_{2}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) . We would show \( \mathrm{d}\left( {{x}_{2}, A}\right) - \mathrm{d}\left( {{x}_{1}, A}\right) \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) in the same way, which proves \( \left| {\mathrm{d}\left( {{x}_{1}, A}\right) - \mathrm{d}\left( {{x}_{2}, A}\right) }\right| \leq \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) \) .

L’application \( x \mapsto \mathrm{d}\left( {x, A}\right) \) étant lipschitzienne, elle est uniformément continue sur \( E \) (voir l’exemple 11), donc continue sur \( E \) .

> Since the map \( x \mapsto \mathrm{d}\left( {x, A}\right) \) is Lipschitz, it is uniformly continuous on \( E \) (see example 11), and therefore continuous on \( E \) .

2/a) Rappelons que lorsque \( F \) est fermé, on a \( \mathrm{d}\left( {x, F}\right) = 0 \) si et seulement si \( x \in F \) .

> 2/a) Recall that when \( F \) is closed, we have \( \mathrm{d}\left( {x, F}\right) = 0 \) if and only if \( x \in F \) .

Ceci étant, définissons \( f : E \rightarrow \mathbb{R} \) par \( f\left( x\right) = \frac{\mathrm{d}\left( {x, A}\right) }{\mathrm{d}\left( {x, A}\right) + \mathrm{d}\left( {x, B}\right) } \) .

> Given this, let us define \( f : E \rightarrow \mathbb{R} \) by \( f\left( x\right) = \frac{\mathrm{d}\left( {x, A}\right) }{\mathrm{d}\left( {x, A}\right) + \mathrm{d}\left( {x, B}\right) } \) .

- L’application \( f \) est bien définie, car si \( \mathrm{d}\left( {x, A}\right)  + \mathrm{d}\left( {x, B}\right)  = 0 \) , alors \( \mathrm{d}\left( {x, A}\right)  = \mathrm{d}\left( {x, B}\right)  = 0 \) , donc \( x \in  A \) et \( x \in  B \) ( \( A \) et \( B \) sont fermés), ce qui est impossible à réaliser puisque \( A \cap  B = \varnothing \) .

> - The mapping \( f \) is well-defined, because if \( \mathrm{d}\left( {x, A}\right)  + \mathrm{d}\left( {x, B}\right)  = 0 \) , then \( \mathrm{d}\left( {x, A}\right)  = \mathrm{d}\left( {x, B}\right)  = 0 \) , so \( x \in  A \) and \( x \in  B \) ( \( A \) and \( B \) are closed), which is impossible to achieve since \( A \cap  B = \varnothing \) .

- On a \( f\left( x\right)  = 0 \) si et seulement si \( \mathrm{d}\left( {x, A}\right)  = 0, i.e.x \in  A \) .

> - We have \( f\left( x\right)  = 0 \) if and only if \( \mathrm{d}\left( {x, A}\right)  = 0, i.e.x \in  A \) .

- On a \( f\left( x\right)  = 1 \) si et seulement si \( \mathrm{d}\left( {x, A}\right)  = \mathrm{d}\left( {x, A}\right)  + \mathrm{d}\left( {x, B}\right) \) , i. e. \( \mathrm{d}\left( {x, B}\right)  = 0 \) ou encore \( x \in  B \) .

> - We have \( f\left( x\right)  = 1 \) if and only if \( \mathrm{d}\left( {x, A}\right)  = \mathrm{d}\left( {x, A}\right)  + \mathrm{d}\left( {x, B}\right) \) , i.e. \( \mathrm{d}\left( {x, B}\right)  = 0 \) or also \( x \in  B \) .

- L'application \( f \) est continue d’après a) et comme composée d’applications continues.

> - The mapping \( f \) is continuous according to a) and as a composition of continuous mappings.

- Enfin, il est clair que \( 0 \leq  f\left( x\right)  \leq  1 \) pour tout \( x \in  E \) .

> - Finally, it is clear that \( 0 \leq  f\left( x\right)  \leq  1 \) for all \( x \in  E \) .

b) Si \( f \) est la fonction exhibée à la question précédente, on a

> b) If \( f \) is the function exhibited in the previous question, we have

\[
A \subset  U = {f}^{-1}\left( {\rbrack  - \infty ,1/2\lbrack }\right) \;\text{ et }\;B \subset  V = {f}^{-1}\left( {\rbrack 1/2, + \infty \lbrack }\right) ,
\]

et \( U \) et \( V \) sont ouverts par continuité de \( f \) (voir la proposition 9), disjoints par construction.

> and \( U \) and \( V \) are open by continuity of \( f \) (see proposition 9), disjoint by construction.

Remarque. Il est possible de répondre à la question 2/b) sans utiliser le résultat de la question 2/a).

> Remark. It is possible to answer question 2/b) without using the result of question 2/a).

EXERCICE 5. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique.

> EXERCISE 5. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space.

a) Soit \( A \) un ouvert de \( E \) et \( B \subset E \) . Montrer que \( A \cap \bar{B} \subset \overline{A \cap B} \) . A-t-on l’égalité dans le cas général ?

> a) Let \( A \) be an open set of \( E \) and \( B \subset E \) . Show that \( A \cap \bar{B} \subset \overline{A \cap B} \) . Do we have equality in the general case?

b) Soit \( A \in E \) . On dit que \( A \) est localement fermé si

> b) Let \( A \in E \) . We say that \( A \) is locally closed if

\[
\forall x \in  A,\exists V\text{ voisinage de }x\text{ tel que }V \cap  A\text{ est un fermé de }V\text{ . }
\]

Montrer que \( A \) est localement fermé si et seulement si \( A \) est l’intersection d’un ouvert de \( E \) et d’un fermé de \( E \) .

> Show that \( A \) is locally closed if and only if \( A \) is the intersection of an open set of \( E \) and a closed set of \( E \) .

Solution. a) Soit \( x \in A \cap \bar{B} \) . On a \( x \in A \) . Comme est ouvert, \( A \) est un voisinage de \( x \) . On en déduit que pour tout voisinage \( V \) de \( x, V \cap A \) est un voisinage de \( x \) . De plus \( x \in \bar{B} \) , donc \( \left( {V \cap A}\right) \cap B = V \cap \left( {A \cap B}\right) \neq 0 \) , et ceci pour tout voisinage \( V \) de \( x \) . On en déduit \( x \in \overline{A \cap B} \) , donc \( A \cap \bar{B} \subset \overline{A \cap B} \) .

> Solution. a) Let \( x \in A \cap \bar{B} \) . We have \( x \in A \) . Since is open, \( A \) is a neighborhood of \( x \) . We deduce that for any neighborhood \( V \) of \( x, V \cap A \) is a neighborhood of \( x \) . Moreover \( x \in \bar{B} \) , so \( \left( {V \cap A}\right) \cap B = V \cap \left( {A \cap B}\right) \neq 0 \) , and this for any neighborhood \( V \) of \( x \) . We deduce \( x \in \overline{A \cap B} \) , so \( A \cap \bar{B} \subset \overline{A \cap B} \) .

On n’a pas toujours l’égalité. Par exemple, dans \( \mathbb{R} \) , si \( A \) est l’ouvert ] \( 0,2\left\lbrack {\text{ et si }B = \left\lbrack {1,3}\right\rbrack \text{ , on }}\right\rbrack \) a \( A \cap \bar{B} = \lbrack 1,2\lbrack \) et \( \overline{A \cap B} = \left\lbrack {1,2}\right\rbrack \) .

> Equality does not always hold. For example, in \( \mathbb{R} \), if \( A \) is the open set ] \( 0,2\left\lbrack {\text{ et si }B = \left\lbrack {1,3}\right\rbrack \text{ , on }}\right\rbrack \) a \( A \cap \bar{B} = \lbrack 1,2\lbrack \) and \( \overline{A \cap B} = \left\lbrack {1,2}\right\rbrack \) .

b) La condition suffisante parait plus simple. Commençons donc par cela.

> b) The sufficient condition seems simpler. Let us start with that.

Condition suffisante. Supposons \( A = \Omega \cap F \) , où \( \Omega \) est un ouvert de \( E \) et \( F \) un fermé de \( E \) . Soit \( x \in A \) . On a \( x \in \Omega \) , ouvert, donc \( \Omega \) est un voisinage de \( x \) . Il vérifie \( \Omega \cap A = \Omega \cap \left( {\Omega \cap F}\right) = \Omega \cap F \) , c’est donc un fermé de \( \Omega \) . Finalement, \( A \) est localement fermé.

> Sufficient condition. Suppose \( A = \Omega \cap F \), where \( \Omega \) is an open set of \( E \) and \( F \) is a closed set of \( E \). Let \( x \in A \). We have \( x \in \Omega \), open, so \( \Omega \) is a neighborhood of \( x \). It satisfies \( \Omega \cap A = \Omega \cap \left( {\Omega \cap F}\right) = \Omega \cap F \), so it is a closed set of \( \Omega \). Finally, \( A \) is locally closed.

Condition nécessaire. Soit \( A \) localement fermé. Pour tout \( x \in A \) , nous allons montrer qu’il existe un voisinage ouvert \( {V}_{x} \) de \( x \) tel que \( {V}_{x} \cap A \) est un fermé de \( {V}_{x} \) . Par hypothèse sur \( A \) , il existe un voisinage \( {U}_{x} \) de \( x \) tel que \( {U}_{x} \cap A \) est un fermé de \( {U}_{x} \) . On peut donc écrire \( {U}_{x} \cap A = {U}_{x} \cap F \) où \( F \) est un fermé de \( E \) . Soit \( {V}_{x} = {U}_{x} \) . C’est un ouvert contenant \( x \) et on a \( {V}_{x} \cap A = {V}_{x} \cap {U}_{x} \cap A = {V}_{x} \cap F \) , donc \( {V}_{x} \cap A \) est un fermé de \( {V}_{x} \) .

> Necessary condition. Let \( A \) be locally closed. For any \( x \in A \), we will show that there exists an open neighborhood \( {V}_{x} \) of \( x \) such that \( {V}_{x} \cap A \) is a closed set of \( {V}_{x} \). By the hypothesis on \( A \), there exists a neighborhood \( {U}_{x} \) of \( x \) such that \( {U}_{x} \cap A \) is a closed set of \( {U}_{x} \). We can therefore write \( {U}_{x} \cap A = {U}_{x} \cap F \) where \( F \) is a closed set of \( E \). Let \( {V}_{x} = {U}_{x} \). This is an open set containing \( x \) and we have \( {V}_{x} \cap A = {V}_{x} \cap {U}_{x} \cap A = {V}_{x} \cap F \), so \( {V}_{x} \cap A \) is a closed set of \( {V}_{x} \).

Posons maintenant \( \Omega = { \cup }_{x \in A}{V}_{x} \) , ouvert de \( E \) (réunion d’ouverts). Nous allons prouver que \( A = \Omega \cap \bar{A} \) , ce qui montrera le résultat.

> Now let us set \( \Omega = { \cup }_{x \in A}{V}_{x} \), an open set of \( E \) (union of open sets). We will prove that \( A = \Omega \cap \bar{A} \), which will show the result.

- On a \( A \subset  \Omega \) et \( A \subset  \bar{A} \) , donc \( A \subset  \Omega  \cap  \bar{A} \) . - Il reste à montrer l’inclusion réciproque. Soit \( x \in  \Omega  \cap  \bar{A} \) . Comme \( x \in  \Omega \) , il existe \( y \in  A \) tel que \( x \in  {V}_{y} \) . On a aussi \( x \in  \bar{A} \) , donc

> - We have \( A \subset  \Omega \) and \( A \subset  \bar{A} \), so \( A \subset  \Omega  \cap  \bar{A} \). - It remains to show the reverse inclusion. Let \( x \in  \Omega  \cap  \bar{A} \). Since \( x \in  \Omega \), there exists \( y \in  A \) such that \( x \in  {V}_{y} \). We also have \( x \in  \bar{A} \), therefore

\[
x \in  {V}_{y} \cap  \bar{A} \subset  \overline{{V}_{y} \cap  A}\text{ di’après a). }
\]

(*)

> Supposons \( x \notin A \) . Alors \( x \in W = {V}_{y} \smallsetminus \left( {{V}_{y} \cap A}\right) \) , ouvert de \( {V}_{y} \) (car \( {V}_{y} \cap A \) est un fermé de \( {V}_{y} \) ). Comme \( {V}_{y} \) est ouvert, \( W \) est même un ouvert de \( E \) . Or \( \left( {{V}_{y} \cap A}\right) \cap W = \varnothing \) , c’est-à-dire \( {V}_{y} \cap A \subset E \smallsetminus W \) , et comme \( E \smallsetminus W \) est un fermé de \( E,\overline{{V}_{y} \cap A} \subset E \smallsetminus W \) . Autrement dit, \( \overline{{V}_{y} \cap A} \cap W = \varnothing \) , donc \( x \notin \overline{{V}_{y} \cap A} \) , ce qui est contradictoire avec (*). Finalement, \( x \in A \) et le résultat.

Suppose \( x \notin A \) . Then \( x \in W = {V}_{y} \smallsetminus \left( {{V}_{y} \cap A}\right) \) , an open set of \( {V}_{y} \) (since \( {V}_{y} \cap A \) is a closed set of \( {V}_{y} \) ). As \( {V}_{y} \) is open, \( W \) is also an open set of \( E \) . However \( \left( {{V}_{y} \cap A}\right) \cap W = \varnothing \) , that is \( {V}_{y} \cap A \subset E \smallsetminus W \) , and since \( E \smallsetminus W \) is a closed set of \( E,\overline{{V}_{y} \cap A} \subset E \smallsetminus W \) . In other words, \( \overline{{V}_{y} \cap A} \cap W = \varnothing \) , therefore \( x \notin \overline{{V}_{y} \cap A} \) , which contradicts (*). Finally, \( x \in A \) and the result.

> Remarque. Nous n’avons pas utilisé la métrique de \( E \) ; ce résultat reste donc vrai, avec la même démonstration, pour un espace topologique \( E \) .

Remark. We did not use the metric of \( E \) ; this result therefore remains true, with the same proof, for a topological space \( E \) .
