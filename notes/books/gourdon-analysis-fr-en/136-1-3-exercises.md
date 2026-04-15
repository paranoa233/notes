#### 1.3. Exercises

*Français : 1.3. Exercices*

EXERCICE 1. Montrer que pour l'équation différentielle définie sur \( \mathbb{R} \) par

> EXERCISE 1. Show that for the differential equation defined on \( \mathbb{R} \) by

\[
{y}^{\prime } = \left\{  \begin{array}{ll} 0 & \text{ si }y < 0 \\  \sqrt{y} & \text{ si }y \geq  0 \end{array}\right.
\]

il n'y a pas unicité au problème de Cauchy.

> there is no uniqueness for the Cauchy problem.

Solution. Faisons une première remarque : cette équation différentielle ne faisant pas intervenir la variable \( t \) , si une fonction \( f : \mathbb{R} \rightarrow \mathbb{R} \) est solution, il en est de même pour toutes les fonctions \( {f}_{c} : \mathbb{R} \rightarrow \mathbb{R}\;t \mapsto f\left( {t - c}\right) \left( {c \in \mathbb{R}}\right) . \)

> Solution. Let us make a first observation: since this differential equation does not involve the variable \( t \), if a function \( f : \mathbb{R} \rightarrow \mathbb{R} \) is a solution, then the same is true for all functions \( {f}_{c} : \mathbb{R} \rightarrow \mathbb{R}\;t \mapsto f\left( {t - c}\right) \left( {c \in \mathbb{R}}\right) . \)

La fonction \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) définie par \( \varphi \left( x\right) = 0 \) pour \( x \leq 0 \) , et \( \varphi \left( x\right) = {x}^{2}/4 \) pour \( x \geq 0 \) , est solution comme on le vérifie facilement. Notre remarque précédente montre alors que pour tout \( c \in \mathbb{R} \) , la fonction

> The function \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) defined by \( \varphi \left( x\right) = 0 \) for \( x \leq 0 \), and \( \varphi \left( x\right) = {x}^{2}/4 \) for \( x \geq 0 \), is a solution as can be easily verified. Our previous observation then shows that for any \( c \in \mathbb{R} \), the function

\[
{\varphi }_{c} : \mathbb{R} \rightarrow  \mathbb{R}\;t \mapsto  \left\{  \begin{array}{ll} 0 & \text{ si }t \leq  c \\  {\left( t - c\right) }^{2}/4 & \text{ si }t > c \end{array}\right.
\]

est solution. Mais pour \( c > 0 \) , ces fonctions coincident sur \( {\mathbb{R}}^{ - } \) , et pourtant elles ne sont pas identiques. Il n'y a donc pas unicité au problème de Cauchy (le théorème de Cauchy-Lipschitz ne s'applique pas car il n'y a pas de caractère lipschitzien).

> is a solution. But for \( c > 0 \), these functions coincide on \( {\mathbb{R}}^{ - } \), and yet they are not identical. There is therefore no uniqueness for the Cauchy problem (the Cauchy-Lipschitz theorem does not apply because there is no Lipschitz property).

EXERCICE 2. Soit \( F : {\mathbb{R}}^{3} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{1} \) . On s’intéresse à l’équation différentielle \( {y}^{\prime \prime } = F\left( {t, y,{y}^{\prime }}\right) \) . On suppose que pour tout \( t \in \mathbb{R}, F\left( {t,0,0}\right) = 0 \) (en d’autres termes, la fonction nulle est solution). Montrer que toute solution non identiquement nulle a ses zéros isolés.

> EXERCISE 2. Let \( F : {\mathbb{R}}^{3} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) class mapping. We are interested in the differential equation \( {y}^{\prime \prime } = F\left( {t, y,{y}^{\prime }}\right) \). Suppose that for all \( t \in \mathbb{R}, F\left( {t,0,0}\right) = 0 \) (in other words, the zero function is a solution). Show that any non-identically zero solution has isolated zeros.

Solution. C'est classique ! Soit \( \varphi \) une solution non identiquement nulle, et soit \( {t}_{0} \) un zéro éventuel de \( \varphi \) .

> Solution. This is a classic! Let \( \varphi \) be a non-identically zero solution, and let \( {t}_{0} \) be a potential zero of \( \varphi \) .

On a \( {\varphi }^{\prime }\left( {t}_{0}\right) \neq 0 \) . En effet, si \( {\varphi }^{\prime }\left( {t}_{0}\right) = 0 \) , d’après le théorème de Cauchy-Lipschitz (qui s’applique car \( F \) est de classe \( {\mathcal{C}}^{1} \) ), \( \varphi \) ayant même valeur et même dérivée que la fonction nulle en \( {t}_{0},\varphi \) est la fonction nulle (unicité au problème de Cauchy pour les équations différentielles du second ordre), ce qui est absurde.

> We have \( {\varphi }^{\prime }\left( {t}_{0}\right) \neq 0 \) . Indeed, if \( {\varphi }^{\prime }\left( {t}_{0}\right) = 0 \) , according to the Cauchy-Lipschitz theorem (which applies because \( F \) is of class \( {\mathcal{C}}^{1} \) ), \( \varphi \) having the same value and the same derivative as the zero function at \( {t}_{0},\varphi \) is the zero function (uniqueness of the Cauchy problem for second-order differential equations), which is absurd.

On peut écrire, lorsque \( t \) tend vers \( {t}_{0} \) ,

> We can write, as \( t \) tends to \( {t}_{0} \) ,

\[
\varphi \left( t\right)  = \varphi \left( {t}_{0}\right)  + \left( {t - {t}_{0}}\right) {\varphi }^{\prime }\left( {t}_{0}\right)  + o\left( {t - {t}_{0}}\right)  = \left( {t - {t}_{0}}\right) \left\lbrack  {{\varphi }^{\prime }\left( {t}_{0}\right)  + o\left( 1\right) }\right\rbrack  ,
\]

et comme \( {\varphi }^{\prime }\left( {t}_{0}\right) \neq 0 \) , le terme \( {\varphi }^{\prime }\left( {t}_{0}\right) + o\left( 1\right) \) est non nul sur un voisinage de \( {t}_{0} \) , donc sur un voisinage de \( {t}_{0},\varphi \) ne s’annule qu’en \( {t}_{0} \) .

> and since \( {\varphi }^{\prime }\left( {t}_{0}\right) \neq 0 \) , the term \( {\varphi }^{\prime }\left( {t}_{0}\right) + o\left( 1\right) \) is non-zero on a neighborhood of \( {t}_{0} \) , therefore on a neighborhood of \( {t}_{0},\varphi \) it only vanishes at \( {t}_{0} \) .

Les zéros de \( \varphi \) sont donc isolés.

> The zeros of \( \varphi \) are therefore isolated.

EXERCICE 3. Soit \( F : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) et \( f, g : \mathbb{R} \rightarrow \mathbb{R} \) deux solutions de l’équation différentielle \( {y}^{\prime } = F\left( {t, y}\right) \) . On suppose qu’il existe \( {t}_{0} \in \mathbb{R} \) tel que \( f\left( {t}_{0}\right) < g\left( {t}_{0}\right) \) . Montrer que pour tout \( t \in \mathbb{R}, f\left( t\right) < g\left( t\right) \) .

> EXERCISE 3. Let \( F : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{1} \) and \( f, g : \mathbb{R} \rightarrow \mathbb{R} \) be two solutions of the differential equation \( {y}^{\prime } = F\left( {t, y}\right) \) . Suppose there exists \( {t}_{0} \in \mathbb{R} \) such that \( f\left( {t}_{0}\right) < g\left( {t}_{0}\right) \) . Show that for all \( t \in \mathbb{R}, f\left( t\right) < g\left( t\right) \) .

Solution. Raisonnons par l’absurde. S’il existe \( {t}_{1} \in \mathbb{R} \) tel que \( f\left( {t}_{1}\right) \geq g\left( {t}_{1}\right) \) , alors comme \( f \) et \( g \) sont continues (elles sont même de classe \( {\mathcal{C}}^{1} \) ), d’après le théorème des valeurs intermédiaires,

> Solution. Let us reason by contradiction. If there exists \( {t}_{1} \in \mathbb{R} \) such that \( f\left( {t}_{1}\right) \geq g\left( {t}_{1}\right) \) , then since \( f \) and \( g \) are continuous (they are even of class \( {\mathcal{C}}^{1} \) ), according to the intermediate value theorem,

il existe \( u \in \mathbb{R} \) tel que \( f\left( u\right) = g\left( u\right) \) . Mais alors, d’après le théorème de Cauchy-Lipschitz (qui s’applique car \( F \) est de classe \( {\mathcal{C}}^{1} \) ) il y a unicité au problème de Cauchy au point \( u \) , donc \( f = g \) . Ceci est absurde car \( f\left( {t}_{0}\right) \neq g\left( {t}_{0}\right) \) , d’où le résultat.

> there exists \( u \in \mathbb{R} \) such that \( f\left( u\right) = g\left( u\right) \) . But then, according to the Cauchy-Lipschitz theorem (which applies because \( F \) is of class \( {\mathcal{C}}^{1} \) ), there is uniqueness for the Cauchy problem at point \( u \) , so \( f = g \) . This is absurd because \( f\left( {t}_{0}\right) \neq g\left( {t}_{0}\right) \) , hence the result.

EXERCICE 4. Soit \( F : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{1} \) vérifiant

> EXERCISE 4. Let \( F : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) be a mapping of class \( {\mathcal{C}}^{1} \) satisfying

\[
\exists T > 0,\forall t \in  \mathbb{R},\;F\left( {t + T,.}\right)  = F\left( {t,.}\right) .
\]

(*)

> Soit \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) une solution de l’équation différentielle \( {y}^{\prime } = F\left( {t, y}\right) \) . Montrer que la suite \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) est strictement monotone ou est constante. Dans ce dernier cas, montrer que \( \varphi \) est une solution \( T \) -périodique.

Let \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) be a solution of the differential equation \( {y}^{\prime } = F\left( {t, y}\right) \) . Show that the sequence \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) is strictly monotonic or constant. In the latter case, show that \( \varphi \) is an \( T \) -periodic solution.

> Solution. Comme \( \varphi \) est solution, la relation (*) montre que la fonction \( {\varphi }_{T} : t \mapsto \varphi \left( {t + T}\right) \) est aussi une solution. Trois cas se présentent.

Solution. Since \( \varphi \) is a solution, the relation (*) shows that the function \( {\varphi }_{T} : t \mapsto \varphi \left( {t + T}\right) \) is also a solution. Three cases arise.

> (i) Si \( \varphi \left( 0\right) < \varphi \left( T\right) = {\varphi }_{T}\left( 0\right) \) , alors d’après l’exercice précédent, on a \( \varphi \left( t\right) < {\varphi }_{T}\left( t\right) \) pour tout \( t \in \mathbb{R} \) . On en conclut \( \varphi \left( {kT}\right) < {\varphi }_{T}\left( {kT}\right) = \varphi \left( {\left( {k + 1}\right) T}\right) \) pour tout \( k \in \mathbb{N} \) , autrement dit, la suite \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) est strictement croissante.

(i) If \( \varphi \left( 0\right) < \varphi \left( T\right) = {\varphi }_{T}\left( 0\right) \), then according to the previous exercise, we have \( \varphi \left( t\right) < {\varphi }_{T}\left( t\right) \) for all \( t \in \mathbb{R} \). We conclude \( \varphi \left( {kT}\right) < {\varphi }_{T}\left( {kT}\right) = \varphi \left( {\left( {k + 1}\right) T}\right) \) for all \( k \in \mathbb{N} \), in other words, the sequence \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) is strictly increasing.

> (ii) Si \( \varphi \left( 0\right) > \varphi \left( T\right) \) , on montrerait en procédant de la même manière que la suite \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) est strictement décroissante.

(ii) If \( \varphi \left( 0\right) > \varphi \left( T\right) \), we would show by proceeding in the same way that the sequence \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) is strictly decreasing.

> (iii) Si \( \varphi \left( 0\right) = \varphi \left( T\right) = {\varphi }_{T}\left( 0\right) \) , alors d’après le théorème de Cauchy-Lipschitz (qui donne l’unicité au problème de Cauchy), \( \varphi = {\varphi }_{T} \) , c’est-à-dire que \( \varphi \) est \( T \) -périodique, et en particulier, la suite \( \left( {\varphi \left( {kT}\right) }\right) \) est constante.

(iii) If \( \varphi \left( 0\right) = \varphi \left( T\right) = {\varphi }_{T}\left( 0\right) \), then according to the Cauchy-Lipschitz theorem (which provides uniqueness for the Cauchy problem), \( \varphi = {\varphi }_{T} \), that is to say that \( \varphi \) is \( T \)-periodic, and in particular, the sequence \( \left( {\varphi \left( {kT}\right) }\right) \) is constant.
