#### 3.1. Definitions

Il existe principalement deux types de convergence pour une suite de fonctions : la convergence "point par point" (convergence simple) et la convergence "globale" (convergence uniforme). La seconde est la plus importante car elle entraîne comme on le verra plus tard des propriétés intéressantes sur la fonction limite.

> There are mainly two types of convergence for a sequence of functions: "pointwise" convergence (simple convergence) and "global" convergence (uniform convergence). The latter is the most important because, as we will see later, it leads to interesting properties regarding the limit function.

DéFINITION 1. Soient \( X \) un ensemble, \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique, et \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) une suite de fonctions de \( X \) dans \( E \) .

> DEFINITION 1. Let \( X \) be a set, \( \left( {E,\mathrm{\;d}}\right) \) a metric space, and \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) a sequence of functions from \( X \) to \( E \) .

- On dit que \( \left( {f}_{n}\right) \) converge simplement (sur \( X \) ) vers \( f : X \rightarrow  E \) si pour tout \( x \in  X \) , la suite \( {\left( {f}_{n}\left( x\right) \right) }_{n \in  \mathbb{N}} \) converge vers \( f\left( x\right) \) , en d’autres termes si

> - We say that \( \left( {f}_{n}\right) \) converges pointwise (on \( X \) ) to \( f : X \rightarrow  E \) if for all \( x \in  X \) , the sequence \( {\left( {f}_{n}\left( x\right) \right) }_{n \in  \mathbb{N}} \) converges to \( f\left( x\right) \) , in other words if

\[
\forall \varepsilon  > 0,\forall x \in  X,\exists N \in  \mathbb{N},\forall n \geq  N,\;\mathrm{\;d}\left( {{f}_{n}\left( x\right) , f\left( x\right) }\right)  < \varepsilon ;
\]

- on dit que \( \left( {f}_{n}\right) \) converge uniformément (sur \( X \) ) vers \( f : X \rightarrow  E \) si

> - we say that \( \left( {f}_{n}\right) \) converges uniformly (on \( X \) ) to \( f : X \rightarrow  E \) if

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall n \geq  N,\forall x \in  X,\;\mathrm{\;d}\left( {{f}_{n}\left( x\right) , f\left( x\right) }\right)  < \varepsilon .
\]

Remarque 1. - Il est important de saisir complètement la différence entre ces deux notions. Étant donné \( \varepsilon > 0 \) , la valeur de \( N \) pour laquelle \( \mathrm{d}\left( {{f}_{n}\left( x\right) , f\left( x\right) }\right) < \varepsilon \) pour tout \( n \geq N \) dépend de \( x \) pour la convergence simple, et ne dépend pas de \( x \) pour la convergence uniforme.

> Remark 1. - It is important to fully grasp the difference between these two notions. Given \( \varepsilon > 0 \) , the value of \( N \) for which \( \mathrm{d}\left( {{f}_{n}\left( x\right) , f\left( x\right) }\right) < \varepsilon \) for all \( n \geq N \) depends on \( x \) for pointwise convergence, and does not depend on \( x \) for uniform convergence.

- La convergence uniforme entraîne la convergence simple.

> - Uniform convergence implies pointwise convergence.

- Lorsque les fonctions \( \left( {f}_{n}\right) \) sont à variable et valeurs réelles, la convergence uniforme de \( \left( {f}_{n}\right) \) vers \( f \) équivaut à dire que pour tout \( \varepsilon  > 0 \) , il existe un rang à partir duquel le graphe de \( {f}_{n} \) est "coincé" entre le graphe de \( f - \varepsilon \) et \( f + \varepsilon \) .

> - When the functions \( \left( {f}_{n}\right) \) are real-valued with real variables, the uniform convergence of \( \left( {f}_{n}\right) \) to \( f \) is equivalent to saying that for all \( \varepsilon  > 0 \) , there exists a rank beyond which the graph of \( {f}_{n} \) is "trapped" between the graph of \( f - \varepsilon \) and \( f + \varepsilon \) .

Exemple 1. La suite de fonctions \( {f}_{n} : \;\left\lbrack {0,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n}}\right. \) converge simplement vers 0 sur \( \lbrack 0,1\lbrack \) , mais pas uniformément car pour tout \( n \in \mathbb{N} \) , il existe \( x \in \lbrack 0,1\lbrack \) tel que \( \left| {{f}_{n}\left( x\right) - 0}\right| \geq 1/2 \) (la définition n’est plus vérifiée dès que \( \varepsilon < 1/2 \) ).

> Example 1. The sequence of functions \( {f}_{n} : \;\left\lbrack {0,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n}}\right. \) converges pointwise to 0 on \( \lbrack 0,1\lbrack \) , but not uniformly because for all \( n \in \mathbb{N} \) , there exists \( x \in \lbrack 0,1\lbrack \) such that \( \left| {{f}_{n}\left( x\right) - 0}\right| \geq 1/2 \) (the definition is no longer satisfied as soon as \( \varepsilon < 1/2 \) ).

Par contre, elle converge uniformément vers 0 sur \( \left\lbrack {0,1/2}\right\rbrack \) car pour tout \( n \) et pour tout \( x \in \left\lbrack {0,1/2}\right\rbrack ,\left| {{f}_{n}\left( x\right) - 0}\right| \leq {2}^{-n} \) . Plus généralement, elle converge uniformément vers 0 sur \( \left\lbrack {0, a}\right\rbrack \) pour tout \( a < 1 \) .

> However, it converges uniformly to 0 on \( \left\lbrack {0,1/2}\right\rbrack \) because for all \( n \) and for all \( x \in \left\lbrack {0,1/2}\right\rbrack ,\left| {{f}_{n}\left( x\right) - 0}\right| \leq {2}^{-n} \) . More generally, it converges uniformly to 0 on \( \left\lbrack {0, a}\right\rbrack \) for all \( a < 1 \) .

Ce phénomène est courant. Les intervalles où il y a convergence uniforme sont souvent différents de ceux où il y a convergence simple.

> This phenomenon is common. The intervals where there is uniform convergence are often different from those where there is pointwise convergence.

##### Uniform Cauchy criterion.

*Français : Critère de Cauchy uniforme.*

Proposition 1. Une suite de fonctions d'un ensemble \( X \) vers un espace métrique complet (E, d) converge uniformément (sur \( X \) ) si et seulement si

> Proposition 1. A sequence of functions from a set \( X \) to a complete metric space (E, d) converges uniformly (on \( X \) ) if and only if

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall p \geq  N,\forall q \geq  N,\forall x \in  X,\;\mathrm{\;d}\left( {{f}_{p}\left( x\right) ,{f}_{q}\left( x\right) }\right)  < \varepsilon .
\]

Démonstration. La condition nécessaire est immédiate.

> Proof. The necessary condition is immediate.

Voyons la condition suffisante. Pour tout \( x \in X \) , la suite \( \left( {{f}_{n}\left( x\right) }\right) \) est de Cauchy dans l’espace complet \( E \) donc elle converge, vers une limite que nous notons \( f\left( x\right) \) . On définit ainsi une fonction \( f : X \rightarrow E \) .

> Let us look at the sufficient condition. For all \( x \in X \) , the sequence \( \left( {{f}_{n}\left( x\right) }\right) \) is Cauchy in the complete space \( E \) , therefore it converges to a limit that we denote \( f\left( x\right) \) . We thus define a function \( f : X \rightarrow E \) .

Soit \( \varepsilon > 0 \) , et soit \( N \in \mathbb{N} \) tel que

> Let \( \varepsilon > 0 \) , and let \( N \in \mathbb{N} \) such that

\[
\forall p \geq  N,\forall q \geq  N,\forall x \in  X\;\mathrm{\;d}\left( {{f}_{p}\left( x\right) ,{f}_{q}\left( x\right) }\right)  < \varepsilon .
\]

(*)

> Fixons un entier quelconque \( p \geq N \) et un \( x \in X \) quelconque. En faisant \( q \rightarrow + \infty \) dans (*), on obtient \( \mathrm{d}\left( {{f}_{p}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \) , et comme \( p \geq N \) et \( x \in X \) étaient arbitraires, on obtient finalement \( \mathrm{d}\left( {{f}_{p}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \) pour tout \( p \geq N \) et pour tout \( x \in X \) . Il y a donc convergence uniforme.

Let us fix an arbitrary integer \( p \geq N \) and an arbitrary \( x \in X \). By setting \( q \rightarrow + \infty \) in (*), we obtain \( \mathrm{d}\left( {{f}_{p}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \), and since \( p \geq N \) and \( x \in X \) were arbitrary, we finally obtain \( \mathrm{d}\left( {{f}_{p}\left( x\right) , f\left( x\right) }\right) \leq \varepsilon \) for all \( p \geq N \) and for all \( x \in X \). There is therefore uniform convergence.

> Caractérisation de la convergence uniforme sur l'espace des fonctions. On peut obtenir une caractérisation agréable de la convergence uniforme si on regarde une suite de fonctions comme une suite de points d'un espace de fonctions.

Characterization of uniform convergence on the space of functions. We can obtain a convenient characterization of uniform convergence if we view a sequence of functions as a sequence of points in a function space.

> DéFINITION 2 (Norme de la convergence uniforme). Soit \( X \) un ensemble et \( E \) un e.v normé. On note \( \mathcal{B}\left( {X, E}\right) \) l’e.v des applications bornées de \( X \) dans \( E \) , et pour tout \( f \in \; \mathcal{B}\left( {X, E}\right) \) , la norme

DEFINITION 2 (Uniform convergence norm). Let \( X \) be a set and \( E \) a normed vector space. We denote by \( \mathcal{B}\left( {X, E}\right) \) the vector space of bounded mappings from \( X \) to \( E \), and for all \( f \in \; \mathcal{B}\left( {X, E}\right) \), the norm

\[
\parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in  E}}\parallel f\left( x\right) \parallel
\]

fait de \( \mathcal{B}\left( {X, E}\right) \) un e.v.n. Cette norme est appelée norme de la convergence uniforme. Une suite \( \left( {f}_{n}\right) \) de \( \mathcal{B}\left( {X, E}\right) \) , regardée comme une suite de fonctions de \( X \) dans \( E \) , converge uniformément (sur \( X \) ) vers \( f \in \mathcal{B}\left( {X, E}\right) \) si et seulement si \( {\begin{Vmatrix}{f}_{n} - f\end{Vmatrix}}_{\infty } \rightarrow 0 \) (i. e. si \( {f}_{n} \rightarrow f \) dans l’e.v.n \( \mathcal{B}\left( {X, E}\right) ) \) .

> makes \( \mathcal{B}\left( {X, E}\right) \) a normed vector space. This norm is called the uniform convergence norm. A sequence \( \left( {f}_{n}\right) \) of \( \mathcal{B}\left( {X, E}\right) \), viewed as a sequence of functions from \( X \) to \( E \), converges uniformly (on \( X \)) to \( f \in \mathcal{B}\left( {X, E}\right) \) if and only if \( {\begin{Vmatrix}{f}_{n} - f\end{Vmatrix}}_{\infty } \rightarrow 0 \) (i.e., if \( {f}_{n} \rightarrow f \) in the normed vector space \( \mathcal{B}\left( {X, E}\right) ) \).

Remarque 2. \( \operatorname{Si}\left( {f}_{n}\right) \) est une suite de fonction de \( \mathcal{B}\left( {X, E}\right) \) et si \( E \) est un espace de Banach (i. e. un e.v.n complet), la condition suffisante de la proposition 1 s'énonce comme suit : si \( \left( {f}_{n}\right) \) est une suite de Cauchy de \( \mathcal{B}\left( {X, E}\right) \) , alors \( \left( {f}_{n}\right) \) converge vers une fonction \( f : X \rightarrow E \) . Cette fonction \( f \) est bornée car la suite \( \left( {f}_{n}\right) \) est bornée dans \( \mathcal{B}\left( {X, E}\right) \) (c’est une suite de Cauchy), donc il existe \( M > 0 \) tel que \( {\begin{Vmatrix}{f}_{n}\end{Vmatrix}}_{\infty } \leq M \) pour tout \( n \) , donc

> Remark 2. \( \operatorname{Si}\left( {f}_{n}\right) \) is a sequence of functions from \( \mathcal{B}\left( {X, E}\right) \) and if \( E \) is a Banach space (i.e., a complete normed vector space), the sufficient condition of Proposition 1 is stated as follows: if \( \left( {f}_{n}\right) \) is a Cauchy sequence in \( \mathcal{B}\left( {X, E}\right) \), then \( \left( {f}_{n}\right) \) converges to a function \( f : X \rightarrow E \). This function \( f \) is bounded because the sequence \( \left( {f}_{n}\right) \) is bounded in \( \mathcal{B}\left( {X, E}\right) \) (it is a Cauchy sequence), so there exists \( M > 0 \) such that \( {\begin{Vmatrix}{f}_{n}\end{Vmatrix}}_{\infty } \leq M \) for all \( n \), therefore

\[
\forall x \in  X,\forall n \in  \mathbb{N},\;\begin{Vmatrix}{{f}_{n}\left( x\right) }\end{Vmatrix} \leq  M.
\]

En fixant \( x \in X \) (quelconque) et en faisant \( n \rightarrow + \infty \) , on en déduit que \( \parallel f\left( x\right) \parallel \leq M \) , et ceci est vrai pour tout \( x \in X \) donc \( f \) est bien bornée. Finalement, nous avons \( f \in \mathcal{B}\left( {X, E}\right) \) . Autrement dit nous venons de montrer que si \( E \) est un espace de Banach, alors \( \mathcal{B}\left( {X, E}\right) \) est aussi un espace de Banach.

> By fixing \( x \in X \) (arbitrary) and setting \( n \rightarrow + \infty \), we deduce that \( \parallel f\left( x\right) \parallel \leq M \), and this is true for all \( x \in X \), so \( f \) is indeed bounded. Finally, we have \( f \in \mathcal{B}\left( {X, E}\right) \). In other words, we have just shown that if \( E \) is a Banach space, then \( \mathcal{B}\left( {X, E}\right) \) is also a Banach space.

Séries de fonctions, convergence normale. Comme pour les séries numériques, une série de fonctions \( \sum {g}_{n} \) est définie comme étant la suite de fonctions \( \left( {f}_{n}\right) \) avec \( {f}_{n} = \; {g}_{0} + \cdots + {g}_{n} \) . On en rencontre beaucoup dans la pratique, et on dispose pour ces dernières d'un nouveau type de convergence (convergence normale) qui n'est en fait qu'une condition suffisante commode pour montrer la convergence uniforme.

> Series of functions, normal convergence. As with numerical series, a series of functions \( \sum {g}_{n} \) is defined as the sequence of functions \( \left( {f}_{n}\right) \) with \( {f}_{n} = \; {g}_{0} + \cdots + {g}_{n} \) . These are frequently encountered in practice, and for the latter, we have a new type of convergence (normal convergence) which is actually a convenient sufficient condition to show uniform convergence.

DéFINITION 3. Soient \( X \) un ensemble et \( E \) un espace de Banach (i. e. un e.v.n complet). On dit qu’une série de fonctions \( \sum {g}_{n} \) à termes dans \( \mathcal{B}\left( {X, E}\right) \) converge normalement si la série \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converge.

> DEFINITION 3. Let \( X \) be a set and \( E \) be a Banach space (i.e., a complete n.v.s.). A series of functions \( \sum {g}_{n} \) with terms in \( \mathcal{B}\left( {X, E}\right) \) is said to converge normally if the series \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converges.

Remarque 3. Il est équivalent de dire que la série de fonctions \( \sum {g}_{n} \) converge normalement s’il existe une série à termes positifs \( \sum {a}_{n} \) convergente telle que

> Remark 3. It is equivalent to say that the series of functions \( \sum {g}_{n} \) converges normally if there exists a convergent series with positive terms \( \sum {a}_{n} \) such that

\[
\forall n \in  \mathbb{N},\forall x \in  X,\;\begin{Vmatrix}{{g}_{n}\left( x\right) }\end{Vmatrix} \leq  {a}_{n}.
\]

Exemple 2. La série de fonctions \( \sum {g}_{n} \) définie par \( {g}_{n} : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n}/{n}^{2} \) converge normalement sur \( \left\lbrack {0,1}\right\rbrack \) car \( {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } = 1/{n}^{2} \) donc \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converge.

> Example 2. The series of functions \( \sum {g}_{n} \) defined by \( {g}_{n} : \left\lbrack {0,1}\right\rbrack \rightarrow \mathbb{R}\;x \mapsto {x}^{n}/{n}^{2} \) converges normally on \( \left\lbrack {0,1}\right\rbrack \) because \( {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } = 1/{n}^{2} \) therefore \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converges.

\( \rightarrow \) THÉORÉME 1. Une série de fonctions \( \sum {g}_{n} \) à valeurs dans un espace de Banach qui converge normalement sur un ensemble \( X \) converge uniformément sur \( X \) .

> \( \rightarrow \) THEOREM 1. A series of functions \( \sum {g}_{n} \) with values in a Banach space that converges normally on a set \( X \) converges uniformly on \( X \) .

Démonstration. Il suffit de vérifier le critère de Cauchy uniforme (voir la proposition 1), ce qui est immédiat car pour tout \( n, p \in \mathbb{N} \) et pour tout \( x \in X \) ,

> Proof. It suffices to verify the uniform Cauchy criterion (see proposition 1), which is immediate because for all \( n, p \in \mathbb{N} \) and for all \( x \in X \) ,

\[
\begin{Vmatrix}{{g}_{n}\left( x\right)  + \cdots  + {g}_{n + p}\left( x\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{g}_{n}\left( x\right) }\end{Vmatrix} + \cdots  + \begin{Vmatrix}{{g}_{n + p}\left( x\right) }\end{Vmatrix} \leq  {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } + \cdots  + {\begin{Vmatrix}{g}_{n + p}\end{Vmatrix}}_{\infty }
\]

et \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converge.

> and \( \sum {\begin{Vmatrix}{g}_{n}\end{Vmatrix}}_{\infty } \) converges.

Une autre solution est de dire que \( \sum {g}_{n} \) est une série absolument convergente dans \( \mathcal{B}\left( {X, E}\right) \) qui est un espace de Banach (voir la remarque 2), donc elle converge dans \( \mathcal{B}\left( {X, E}\right) \) , donc elle converge uniformément.

> Another solution is to say that \( \sum {g}_{n} \) is an absolutely convergent series in \( \mathcal{B}\left( {X, E}\right) \) which is a Banach space (see remark 2), therefore it converges in \( \mathcal{B}\left( {X, E}\right) \) , therefore it converges uniformly.

Remarque 4. De même qu'il existe des séries convergentes mais non absolument conver-gentes, il existe des séries de fonctions uniformément convergentes qui ne sont pas nor-malement convergentes (voir par exemple la question b) de l'exercice 2 page 236).

> Remark 4. Just as there exist convergent series that are not absolutely convergent, there exist uniformly convergent series of functions that are not normally convergent (see for example question b) of exercise 2 on page 236).
