#### 4.3. A priori bound principle

*Français : 4.3. Principe de majoration a priori*

Cette partie est consacrée à un résultat appelé principe de majoration a priori (ou théorème de sortie de tout compact), portant sur le comportement d'une solution maximale d'une équation différentielle aux extrémités de son intervalle de définition. Ce résultat est hors-programme ; il en existe une version faible (voir l'exercice 1 page 401) qui doit être connue et qui suffit à montrer de nombreux résultats portant sur les solutions maximales.

> This section is devoted to a result called the a priori bound principle (or theorem on exiting every compact set), concerning the behavior of a maximal solution of a differential equation at the endpoints of its interval of definition. This result is outside the curriculum; a weak version exists (see exercise 1 page 401) which must be known and which is sufficient to prove many results concerning maximal solutions.

Préliminaires. Soit \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( \Omega \) est un ouvert de \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) une application continue, localement lipschitzienne en la seconde variable. Le théorème de Cauchy-Lipschitz dit que pour tout \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , il existe un intervalle réel \( I \) centré en \( {t}_{0} \) et une solution \( \varphi \) de \( {y}^{\prime } = F\left( {t, y}\right) \) vérifiant \( \varphi \left( {t}_{0}\right) = {x}_{0} \) .

> Preliminaries. Let \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( \Omega \) is an open set of \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) be a continuous mapping, locally Lipschitz in the second variable. The Cauchy-Lipschitz theorem states that for all \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) , there exists a real interval \( I \) centered at \( {t}_{0} \) and a solution \( \varphi \) of \( {y}^{\prime } = F\left( {t, y}\right) \) satisfying \( \varphi \left( {t}_{0}\right) = {x}_{0} \) .

Autrement dit, le problème de Cauchy a toujours une solution, définie sur un intervalle centré en \( {t}_{0} \) . Nous allons voir qu’on peut trouver un voisinage de \( \left( {{t}_{0},{x}_{0}}\right) \) dans \( \Omega \) tel que toutes les solutions du problème de Cauchy pour \( \left( {t, x}\right) \) dans ce voisinage soient définies sur un méme intervalle \( I \) .

> In other words, the Cauchy problem always has a solution, defined on an interval centered at \( {t}_{0} \). We will see that we can find a neighborhood of \( \left( {{t}_{0},{x}_{0}}\right) \) in \( \Omega \) such that all solutions to the Cauchy problem for \( \left( {t, x}\right) \) in this neighborhood are defined on the same interval \( I \).

LEMME 1. Soit \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \) . Il existe un voisinage \( V \) de \( {x}_{0} \) dans \( \Omega \) et un intervalle ouvert I centré en \( {t}_{0} \) tel que pour tout \( \left( {{t}_{1}, x}\right) \in I \times V \) , il existe une solution \( \varphi \) de \( {y}^{\prime } = F\left( {t, y}\right) \) définie sur I et vérifiant \( \varphi \left( {t}_{1}\right) = x \) .

> LEMMA 1. Let \( \left( {{t}_{0},{x}_{0}}\right) \in \Omega \). There exists a neighborhood \( V \) of \( {x}_{0} \) in \( \Omega \) and an open interval I centered at \( {t}_{0} \) such that for all \( \left( {{t}_{1}, x}\right) \in I \times V \), there exists a solution \( \varphi \) of \( {y}^{\prime } = F\left( {t, y}\right) \) defined on I and satisfying \( \varphi \left( {t}_{1}\right) = x \).

Démonstration. Commençons par un rappel. Pour tout \( t \in \mathbb{R} \) et pour tout \( \alpha > 0 \) , on pose \( {I}_{\alpha }\left( t\right) = \; \rbrack t - \alpha , t + \alpha \left\lbrack \right. \) . Pour tout \( x \in {\mathbb{R}}^{n} \) et pour tout \( r > 0 \) , on pose \( {\mathrm{B}}_{r}\left( x\right) = \left\{ {y \in {\mathbb{R}}^{n} \mid \parallel x - y\parallel < r}\right\} \) . Nous avons vu, au cours de la démonstration du théorème de Cauchy-Lipschitz page 374 que si \( U = {I}_{\alpha }\left( t\right) \times {\mathrm{B}}_{r}\left( x\right) \) est un cylindre de sécurité pour \( F \) en \( \left( {t, x}\right) \) ,(i. e. \( F \) est lipschitzienne en la seconde variable sur \( U \) et il existe un majorant \( M > 0 \) de \( F \) sur \( U \) tel que \( {\alpha M} < r \) ), alors il existe une solution \( \varphi \) de \( {y}^{\prime } = F\left( {t, x}\right) \) définie sur \( {I}_{\alpha }\left( t\right) \) et vérifiant \( \varphi \left( t\right) = x \) .

> Proof. Let us begin with a reminder. For all \( t \in \mathbb{R} \) and for all \( \alpha > 0 \), we set \( {I}_{\alpha }\left( t\right) = \; \rbrack t - \alpha , t + \alpha \left\lbrack \right. \). For all \( x \in {\mathbb{R}}^{n} \) and for all \( r > 0 \), we set \( {\mathrm{B}}_{r}\left( x\right) = \left\{ {y \in {\mathbb{R}}^{n} \mid \parallel x - y\parallel < r}\right\} \). We saw, during the proof of the Cauchy-Lipschitz theorem on page 374, that if \( U = {I}_{\alpha }\left( t\right) \times {\mathrm{B}}_{r}\left( x\right) \) is a safety cylinder for \( F \) at \( \left( {t, x}\right) \) (i.e., \( F \) is Lipschitz in the second variable on \( U \) and there exists an upper bound \( M > 0 \) of \( F \) on \( U \) such that \( {\alpha M} < r \)), then there exists a solution \( \varphi \) of \( {y}^{\prime } = F\left( {t, x}\right) \) defined on \( {I}_{\alpha }\left( t\right) \) and satisfying \( \varphi \left( t\right) = x \).

Soit \( U \subset \Omega \) un voisinage compact de \( \left( {{t}_{0},{x}_{0}}\right) \) tel que \( F \) soit lipschitzienne en la seconde variable sur \( U \) . Notons \( M \) un majorant de \( F \) sur \( U \) , et choisissons \( \alpha > 0 \) et \( r > 0 \) tels que \( {I}_{\alpha }\left( {t}_{0}\right) \times {\mathrm{B}}_{r}\left( {x}_{0}\right) \subset U \) et \( {\alpha M} < r \) (ainsi \( {I}_{\alpha }\left( {t}_{0}\right) \times {\mathrm{B}}_{r}\left( {x}_{0}\right) \) est un cylindre de sécurité pour \( F \) en \( \left. \left( {{t}_{0},{x}_{0}}\right) \right) \) .

> Let \( U \subset \Omega \) be a compact neighborhood of \( \left( {{t}_{0},{x}_{0}}\right) \) such that \( F \) is Lipschitz in the second variable on \( U \). Let \( M \) denote an upper bound of \( F \) on \( U \), and choose \( \alpha > 0 \) and \( r > 0 \) such that \( {I}_{\alpha }\left( {t}_{0}\right) \times {\mathrm{B}}_{r}\left( {x}_{0}\right) \subset U \) and \( {\alpha M} < r \) (thus \( {I}_{\alpha }\left( {t}_{0}\right) \times {\mathrm{B}}_{r}\left( {x}_{0}\right) \) is a safety cylinder for \( F \) at \( \left. \left( {{t}_{0},{x}_{0}}\right) \right) \)).

Posons \( I = {I}_{\alpha /3}\left( {t}_{0}\right) \) et \( V = {\mathrm{B}}_{r/3}\left( {x}_{0}\right) \) . Soit \( \left( {{t}_{1}, x}\right) \in I \times V \) . Alors \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \times {\mathrm{B}}_{{2r}/3}\left( x\right) \) est un cylindre de sécurité pour \( F \) en \( \left( {{t}_{1}, x}\right) \) (en effet, \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \subset {I}_{\alpha }\left( {t}_{0}\right) ,{\mathrm{B}}_{{2r}/3}\left( x\right) \subset {\mathrm{B}}_{r}\left( {x}_{0}\right) \) , et \( \left( {{2\alpha }/3}\right) M < {2r}/3 < r) \) , donc il existe une solution \( \varphi \) de \( {y}^{\prime } = F\left( {t, y}\right) \) définie sur \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \) et vérifiant \( \varphi \left( {t}_{1}\right) = x \) . Comme \( I \subset {I}_{{2\alpha }/3}\left( {t}_{1}\right) \) , on en déduit le résultat.

> Let \( I = {I}_{\alpha /3}\left( {t}_{0}\right) \) and \( V = {\mathrm{B}}_{r/3}\left( {x}_{0}\right) \) . Let \( \left( {{t}_{1}, x}\right) \in I \times V \) . Then \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \times {\mathrm{B}}_{{2r}/3}\left( x\right) \) is a safety cylinder for \( F \) at \( \left( {{t}_{1}, x}\right) \) (indeed, \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \subset {I}_{\alpha }\left( {t}_{0}\right) ,{\mathrm{B}}_{{2r}/3}\left( x\right) \subset {\mathrm{B}}_{r}\left( {x}_{0}\right) \) , and \( \left( {{2\alpha }/3}\right) M < {2r}/3 < r) \) , so there exists a solution \( \varphi \) of \( {y}^{\prime } = F\left( {t, y}\right) \) defined on \( {I}_{{2\alpha }/3}\left( {t}_{1}\right) \) and satisfying \( \varphi \left( {t}_{1}\right) = x \) . Since \( I \subset {I}_{{2\alpha }/3}\left( {t}_{1}\right) \) , we deduce the result.)

Nous sommes maintenant en mesure de démontrer le théorème suivant.

> We are now in a position to prove the following theorem.

THÉORÉME 1 (PRINCIPE DE MAJORATION a priori). Soient ]a, b[ un intervalle ouvert de \( \mathbb{R}, O \) un ouvert de \( {\mathbb{R}}^{n} \) , et \( F : \rbrack a, b\lbrack \times O \rightarrow {\mathbb{R}}^{n} \) une fonction continue et localement lipschitzienne en la seconde variable. Soit \( \varphi : \;\rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}\text{ une solution maximale de }}\right\rbrack \; {y}^{\prime } = F\left( {t, y}\right) . \)

> THEOREM 1 (A PRIORI BOUND PRINCIPLE). Let ]a, b[ be an open interval of \( \mathbb{R}, O \) an open set of \( {\mathbb{R}}^{n} \) , and \( F : \rbrack a, b\lbrack \times O \rightarrow {\mathbb{R}}^{n} \) a continuous function that is locally Lipschitz in the second variable. Let \( \varphi : \;\rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}\text{ une solution maximale de }}\right\rbrack \; {y}^{\prime } = F\left( {t, y}\right) . \)

Alors si \( \beta < b \) (resp. si \( a < \alpha \) ), pour tout compact \( K \subset O \) , il existe un voisinage \( V \) de \( \beta \) (resp. de \( \alpha \) ) dans \( \rbrack \alpha ,\beta \left\lbrack \right. \) tel que \( \varphi \left( t\right) \notin K \) pour tout \( t \in V \) .

> Then if \( \beta < b \) (resp. if \( a < \alpha \) ), for any compact set \( K \subset O \) , there exists a neighborhood \( V \) of \( \beta \) (resp. of \( \alpha \) ) in \( \rbrack \alpha ,\beta \left\lbrack \right. \) such that \( \varphi \left( t\right) \notin K \) for all \( t \in V \) .

Démonstration. Montrons le résultat au voisinage de \( \beta \) (le problème au voisinage de \( \alpha \) de traite de la même manière). Raisonnons par l’absurde et supposons l’existence d’un compact \( K \subset O \) et d’une suite \( \left( {\beta }_{n}\right) \) de \( \rbrack \alpha ,\beta \left\lbrack \right. \) convergeant vers \( \beta \) tels que \( \varphi \left( {\beta }_{n}\right) \in K \) pour tout \( n \) .

> Proof. Let us show the result in the neighborhood of \( \beta \) (the problem in the neighborhood of \( \alpha \) is handled in the same way). Let us reason by contradiction and assume the existence of a compact set \( K \subset O \) and a sequence \( \left( {\beta }_{n}\right) \) of \( \rbrack \alpha ,\beta \left\lbrack \right. \) converging to \( \beta \) such that \( \varphi \left( {\beta }_{n}\right) \in K \) for all \( n \) .

Comme \( K \) est compact, on peut extraire de \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) une sous-suite convergente, encore notée \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) (par commodité). Soit \( {x}_{0} \) la limite de \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) . On a \( {x}_{0} \in O \) car \( {x}_{0} \in K \subset O \) .

> Since \( K \) is compact, we can extract from \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) a convergent subsequence, still denoted \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) (for convenience). Let \( {x}_{0} \) be the limit of \( \left( {\varphi \left( {\beta }_{n}\right) }\right) \) . We have \( {x}_{0} \in O \) because \( {x}_{0} \in K \subset O \) .

D’après le lemme précédent, comme \( \left. {\left( {\beta ,{x}_{0}}\right) \in }\right\rbrack a, b\left\lbrack {\times O}\right. \) , il existe un voisinage \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \times V \) de \( \left( {\beta ,{x}_{0}}\right) \) dans \( \rbrack a, b\left\lbrack {\times O}\right. \) vérifiant la propriété suivante : pour tout \( \left. {{t}_{1} \in }\right\rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \) , pour tout \( x \in V \) , il existe une solution \( \psi \) de \( {y}^{\prime } = F\left( {t, y}\right) \) définie sur \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \) et vérifiant \( \psi \left( {t}_{1}\right) = x \) .

> According to the previous lemma, since \( \left. {\left( {\beta ,{x}_{0}}\right) \in }\right\rbrack a, b\left\lbrack {\times O}\right. \), there exists a neighborhood \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \times V \) of \( \left( {\beta ,{x}_{0}}\right) \) in \( \rbrack a, b\left\lbrack {\times O}\right. \) satisfying the following property: for all \( \left. {{t}_{1} \in }\right\rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \), for all \( x \in V \), there exists a solution \( \psi \) of \( {y}^{\prime } = F\left( {t, y}\right) \) defined on \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \lbrack \) and satisfying \( \psi \left( {t}_{1}\right) = x \).

Choisissons \( n \in \mathbb{N} \) tel que \( {\beta }_{n} \in \rbrack \beta - \varepsilon ,\beta + \varepsilon \left\lbrack \right. \) et \( \varphi \left( {\beta }_{n}\right) \in V \) . Notons \( \psi \) la solution définie sur \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \left\lbrack \right. \) de \( {y}^{\prime } = F\left( {t, y}\right) \) telle que \( \psi \left( {\beta }_{n}\right) = \varphi \left( {\beta }_{n}\right) \) . L’unicité au problème de Cauchy donnée par le théorème de Cauchy Lipschitz montre que \( \psi = \varphi \) sur \( \rbrack \beta - \varepsilon ,\beta \lbrack \) . La fonction définie sur \( \rbrack \alpha ,\beta + \varepsilon \lbrack \) par

> Let us choose \( n \in \mathbb{N} \) such that \( {\beta }_{n} \in \rbrack \beta - \varepsilon ,\beta + \varepsilon \left\lbrack \right. \) and \( \varphi \left( {\beta }_{n}\right) \in V \). Let \( \psi \) be the solution defined on \( \rbrack \beta - \varepsilon ,\beta + \varepsilon \left\lbrack \right. \) of \( {y}^{\prime } = F\left( {t, y}\right) \) such that \( \psi \left( {\beta }_{n}\right) = \varphi \left( {\beta }_{n}\right) \). The uniqueness of the Cauchy problem given by the Cauchy-Lipschitz theorem shows that \( \psi = \varphi \) on \( \rbrack \beta - \varepsilon ,\beta \lbrack \). The function defined on \( \rbrack \alpha ,\beta + \varepsilon \lbrack \) by

\[
t \mapsto  \varphi \left( t\right) \;\text{ si }t \in  \rbrack \alpha ,\beta \lbrack ,\;t \mapsto  \psi \left( t\right) \;\text{ si }t \in  \lbrack \beta ,\beta  + \varepsilon \lbrack
\]

est donc solution de \( {y}^{\prime } = F\left( {t, y}\right) \) sur \( \rbrack \alpha ,\beta + \varepsilon \lbrack \) . Ceci est absurde, car \( \varphi \) est une solution maximale sur \( \rbrack \alpha ,\beta \left\lbrack \text{ . D’où le résultat. }\right. \)

> is therefore a solution of \( {y}^{\prime } = F\left( {t, y}\right) \) on \( \rbrack \alpha ,\beta + \varepsilon \lbrack \). This is absurd, because \( \varphi \) is a maximal solution on \( \rbrack \alpha ,\beta \left\lbrack \text{ . D’où le résultat. }\right. \)

Remarque 1. - Dans le cas \( O = {\mathbb{R}}^{n} \) , ce résultat s’écrit : si \( \beta < b \) , alors \( \mathop{\lim }\limits_{{t \rightarrow \beta }}\parallel \varphi \left( t\right) \parallel = \; + \infty \) .

> Remark 1. - In the case \( O = {\mathbb{R}}^{n} \), this result is written: if \( \beta < b \), then \( \mathop{\lim }\limits_{{t \rightarrow \beta }}\parallel \varphi \left( t\right) \parallel = \; + \infty \).

- Une fonction localement lipschitzienne \( F : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}\;y \mapsto  F\left( y\right) \) peut être vue comme une fonction de \( \mathbb{R} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) (en posant \( F\left( {t, y}\right)  = F\left( y\right) \) ). Le théorème précédent s’énonce alors comme suit : si \( \varphi  : \rbrack a, b\left\lbrack  { \rightarrow  {\mathbb{R}}^{n}}\right. \) est une solution maximale de \( {y}^{\prime } = F\left( y\right) \) , et si \( b <  + \infty \) , alors \( \mathop{\lim }\limits_{{t \rightarrow  b}}\parallel \varphi \left( t\right) \parallel  =  + \infty \) .

> - A locally Lipschitz function \( F : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}\;y \mapsto  F\left( y\right) \) can be seen as a function of \( \mathbb{R} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) (by setting \( F\left( {t, y}\right)  = F\left( y\right) \)). The previous theorem is then stated as follows: if \( \varphi  : \rbrack a, b\left\lbrack  { \rightarrow  {\mathbb{R}}^{n}}\right. \) is a maximal solution of \( {y}^{\prime } = F\left( y\right) \), and if \( b <  + \infty \), then \( \mathop{\lim }\limits_{{t \rightarrow  b}}\parallel \varphi \left( t\right) \parallel  =  + \infty \).

- Il existe une version faible du principe de majoration a priori dont la preuve est plus simple et ne repose pas sur le lemme précédent (voir l'exercice 1).

> - There exists a weak version of the a priori bound principle whose proof is simpler and does not rely on the previous lemma (see exercise 1).

Grâce au principe de majoration a priori, nous pouvons maintenant démontrer le théorème 1 page 378 (la version faible - exercice 1 - permet aussi de le démontrer).

> Thanks to the a priori bound principle, we can now prove theorem 1 on page 378 (the weak version - exercise 1 - also allows it to be proven).

COROLLAIRE 1. Soit \( \left( L\right) : {X}^{\prime } = A\left( t\right) X + B\left( t\right) \) une équation différentielle linéaire sur \( {\mathbb{R}}^{n} \) , où \( A : \rbrack a, b\left\lbrack { \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) }\right. \) et \( \left. {B : }\right\rbrack a, b\lbrack \rightarrow {\mathbb{R}}^{n} \) sont continues.

> COROLLARY 1. Let \( \left( L\right) : {X}^{\prime } = A\left( t\right) X + B\left( t\right) \) be a linear differential equation on \( {\mathbb{R}}^{n} \) , where \( A : \rbrack a, b\left\lbrack { \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) }\right. \) and \( \left. {B : }\right\rbrack a, b\lbrack \rightarrow {\mathbb{R}}^{n} \) are continuous.

Alors les solutions maximales de (L) sont définies sur \( \rbrack a, b\lbrack \) .

> Then the maximal solutions of (L) are defined on \( \rbrack a, b\lbrack \) .

Démonstration. On définit l’application \( F : \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;\left( {t, X}\right) \mapsto A\left( t\right) X + B\left( t\right) }\right. \) . Elle est continue sur \( \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n}}\right. \) et localement lipschitzienne en \( X \) , car \( F\left( {t, X}\right) - F\left( {t, Y}\right) = A\left( t\right) \left( {X - Y}\right) \) et \( A \) est continue.

> Proof. We define the mapping \( F : \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}\;\left( {t, X}\right) \mapsto A\left( t\right) X + B\left( t\right) }\right. \) . It is continuous on \( \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n}}\right. \) and locally Lipschitz in \( X \) , because \( F\left( {t, X}\right) - F\left( {t, Y}\right) = A\left( t\right) \left( {X - Y}\right) \) and \( A \) is continuous.

Soit \( X : \rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) une solution maximale de \( \left( L\right) \) . Supposons \( \beta < b \) , et \( {t}_{0} \in \rbrack a, b\lbrack \) étant fixé, notons \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {{t}_{0},\beta }\right\rbrack }}\parallel A\left( t\right) \parallel \) et \( N = \mathop{\sup }\limits_{{t \in \left\lbrack {{t}_{0},\beta }\right\rbrack }}\parallel B\left( t\right) \parallel \) (on a muni \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) de la norme d’algèbre \( \parallel A\parallel = \mathop{\sup }\limits_{{\parallel X\parallel = 1}}\parallel {AX}\parallel \) ). On a

> Let \( X : \rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) be a maximal solution of \( \left( L\right) \) . Suppose \( \beta < b \) , and \( {t}_{0} \in \rbrack a, b\lbrack \) being fixed, let us denote \( M = \mathop{\sup }\limits_{{t \in \left\lbrack {{t}_{0},\beta }\right\rbrack }}\parallel A\left( t\right) \parallel \) and \( N = \mathop{\sup }\limits_{{t \in \left\lbrack {{t}_{0},\beta }\right\rbrack }}\parallel B\left( t\right) \parallel \) (we have equipped \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) with the algebra norm \( \parallel A\parallel = \mathop{\sup }\limits_{{\parallel X\parallel = 1}}\parallel {AX}\parallel \) ). We have

\[
\forall t \in  \left\lbrack  {{t}_{0},\beta \left\lbrack  {,\;\begin{Vmatrix}{{X}^{\prime }\left( t\right) }\end{Vmatrix} \leq  M\parallel X\left( t\right) \parallel  + N,}\right. }\right.
\]

donc d'après le lemme de Gronwall (voir le corollaire 2 page 398), \( X \) est bornée au voisinage de \( {\beta }^{ - } \) . Ceci contredit le principe de majoration a priori, donc \( \beta = b \) . On montrerait de même \( \alpha = a \) .

> therefore, according to Gronwall's lemma (see corollary 2 on page 398), \( X \) is bounded in the neighborhood of \( {\beta }^{ - } \) . This contradicts the a priori bound principle, therefore \( \beta = b \) . We would show \( \alpha = a \) in the same way.

Exercices.

> Exercises.

\( \rightarrow \) EXERCICE 1 (UNE VERSION FAIBLE DU PRINCIPE DE MAJORATION a priori). On consi-dère \( F : \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}}\right. \) (avec \( - \infty \leq a < b \leq + \infty \) ) une fonction continue et localement lipschitzienne en la seconde variable.

> \( \rightarrow \) EXERCISE 1 (A WEAK VERSION OF THE A PRIORI BOUND PRINCIPLE). Consider \( F : \rbrack a, b\left\lbrack {\times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}}\right. \) (with \( - \infty \leq a < b \leq + \infty \) ) a function that is continuous and locally Lipschitz in the second variable.

Soit \( \varphi : \rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) une solution maximale de \( {y}^{\prime } = F\left( {t, y}\right) \) . Si \( \beta < b \) , montrer que \( \varphi \) n’est pas bornée au voisinage de \( \beta \) (sans utiliser, bien sûr, le principe de majoration \( a \) priori).

> Let \( \varphi : \rbrack \alpha ,\beta \left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) be a maximal solution of \( {y}^{\prime } = F\left( {t, y}\right) \) . If \( \beta < b \) , show that \( \varphi \) is not bounded in the neighborhood of \( \beta \) (without using, of course, the a priori \( a \) bound principle).

Solution. Raisonnons par l’absurde : supposons \( \beta < b \) et \( \varphi \) bornée au voisinage de \( \beta \) . Soit \( {t}_{0} \in \rbrack \alpha ,\beta \left\lbrack \right. \) et soit \( M > 0 \) tel que \( \parallel \varphi \left( t\right) \parallel \leq M \) pour tout \( t \in \left\lbrack {{t}_{0},\beta \lbrack }\right. \) .

> Solution. Let us reason by contradiction: assume \( \beta < b \) and \( \varphi \) are bounded in the neighborhood of \( \beta \) . Let \( {t}_{0} \in \rbrack \alpha ,\beta \left\lbrack \right. \) and let \( M > 0 \) be such that \( \parallel \varphi \left( t\right) \parallel \leq M \) for all \( t \in \left\lbrack {{t}_{0},\beta \lbrack }\right. \) .

Comme \( F \) est continue sur le compact \( \left\lbrack {{t}_{0},\beta }\right\rbrack \times {\mathrm{B}}_{\mathrm{f}}\left( {0, M}\right) \) , il existe \( K > 0 \) tel que \( \parallel F\left( {t, x}\right) \parallel \leq K \) pour tout \( \left( {t, x}\right) \in \left\lbrack {{t}_{0},\beta }\right\rbrack \times {\mathrm{B}}_{\mathrm{f}}\left( {0, M}\right) \) , et on a \( \begin{Vmatrix}{{\varphi }^{\prime }\left( t\right) }\end{Vmatrix} = \parallel F\left( {t,\varphi \left( t\right) }\right) \parallel \leq K \) pour tout \( t \in \left\lbrack {{t}_{0},\beta \lbrack }\right. \) . Comme de plus \( {\varphi }^{\prime } \) est continue, on en déduit que l’intégrale \( {\int }_{{t}_{0}}^{\beta }{\varphi }^{\prime }\left( t\right) {dt} \) converge absolument, donc converge, donc \( \varphi \) converge en \( \beta \) . Notons \( {x}_{0} = \mathop{\lim }\limits_{{t \rightarrow \beta }}\varphi \left( t\right) \) . Prolongeons \( \varphi \) par continuité en \( \beta \) en posant \( \varphi \left( \beta \right) = {x}_{0} \) . Comme \( {\varphi }^{\prime }\left( t\right) = F\left( {t,\varphi \left( t\right) }\right) \) , on voit que \( {\varphi }^{\prime } \) converge en \( \beta \) , donc le prolongement de \( \varphi \) est dérivable en \( \beta \) et \( {\varphi }^{\prime }\left( \beta \right) = F\left( {\beta ,\varphi \left( \beta \right) }\right) \) .

> Since \( F \) is continuous on the compact set \( \left\lbrack {{t}_{0},\beta }\right\rbrack \times {\mathrm{B}}_{\mathrm{f}}\left( {0, M}\right) \) , there exists \( K > 0 \) such that \( \parallel F\left( {t, x}\right) \parallel \leq K \) for all \( \left( {t, x}\right) \in \left\lbrack {{t}_{0},\beta }\right\rbrack \times {\mathrm{B}}_{\mathrm{f}}\left( {0, M}\right) \) , and we have \( \begin{Vmatrix}{{\varphi }^{\prime }\left( t\right) }\end{Vmatrix} = \parallel F\left( {t,\varphi \left( t\right) }\right) \parallel \leq K \) for all \( t \in \left\lbrack {{t}_{0},\beta \lbrack }\right. \) . Since, moreover, \( {\varphi }^{\prime } \) is continuous, we deduce that the integral \( {\int }_{{t}_{0}}^{\beta }{\varphi }^{\prime }\left( t\right) {dt} \) converges absolutely, therefore it converges, so \( \varphi \) converges at \( \beta \) . Let \( {x}_{0} = \mathop{\lim }\limits_{{t \rightarrow \beta }}\varphi \left( t\right) \) . Extend \( \varphi \) by continuity at \( \beta \) by setting \( \varphi \left( \beta \right) = {x}_{0} \) . Since \( {\varphi }^{\prime }\left( t\right) = F\left( {t,\varphi \left( t\right) }\right) \) , we see that \( {\varphi }^{\prime } \) converges at \( \beta \) , so the extension of \( \varphi \) is differentiable at \( \beta \) and \( {\varphi }^{\prime }\left( \beta \right) = F\left( {\beta ,\varphi \left( \beta \right) }\right) \) .

Ainsi prolongée, \( \varphi \) est solution de l’équation différentielle \( {y}^{\prime } = F\left( {t, y}\right) \) sur \( \rbrack \alpha ,\beta \rbrack \) . Or d’après le théorème de Cauchy-Lipschitz, il existe une fonction \( \psi \) définie sur un intervalle ouvert \( {I}_{\beta } \) centré en \( \beta \) , solution de \( {y}^{\prime } = F\left( {t, y}\right) \) , et vérifiant \( \psi \left( \beta \right) = {x}_{0} = \varphi \left( \beta \right) \) . Comme \( \varphi \) et \( \psi \) coincident en \( {x}_{0} \) , l’unicité au problème de Cauchy garantie par le théorème de Cauchy-Lipschitz entraîne que \( \left. {\left. {\left. {\left. {\left. {\varphi \left. { = \psi \operatorname{sur}}\right\rbrack }\right\rbrack \alpha ,\beta }\right\rbrack \cap {I}_{\beta }\text{ . Donc la fonction définie sur }}\right\rbrack \alpha ,\beta }\right\rbrack \cup {I}_{\beta }\text{ par }}\right\rbrack \)

> Thus extended, \( \varphi \) is a solution to the differential equation \( {y}^{\prime } = F\left( {t, y}\right) \) on \( \rbrack \alpha ,\beta \rbrack \) . However, according to the Cauchy-Lipschitz theorem, there exists a function \( \psi \) defined on an open interval \( {I}_{\beta } \) centered at \( \beta \) , which is a solution to \( {y}^{\prime } = F\left( {t, y}\right) \) and satisfies \( \psi \left( \beta \right) = {x}_{0} = \varphi \left( \beta \right) \) . Since \( \varphi \) and \( \psi \) coincide at \( {x}_{0} \) , the uniqueness of the Cauchy problem guaranteed by the Cauchy-Lipschitz theorem implies that \( \left. {\left. {\left. {\left. {\left. {\varphi \left. { = \psi \operatorname{sur}}\right\rbrack }\right\rbrack \alpha ,\beta }\right\rbrack \cap {I}_{\beta }\text{ . Donc la fonction définie sur }}\right\rbrack \alpha ,\beta }\right\rbrack \cup {I}_{\beta }\text{ par }}\right\rbrack \)

\[
\left. {\left. {t \mapsto  \varphi \left( t\right) \;\text{ si }t \in  }\right\rbrack  \alpha ,\beta }\right\rbrack  ,\;\left. {\left. {t \mapsto  \psi \left( t\right) \;\text{ si }t \in  {I}_{\beta } \smallsetminus  }\right\rbrack  \alpha ,\beta }\right\rbrack  ,
\]

est solution de \( {y}^{\prime } = F\left( {t, y}\right) \) sur un intervalle contenant strictement \( \rbrack \alpha ,\beta \lbrack \) . Ceci est absurde car \( \varphi \) est une solution maximale. D’où le résultat.

> is a solution to \( {y}^{\prime } = F\left( {t, y}\right) \) on an interval strictly containing \( \rbrack \alpha ,\beta \lbrack \) . This is absurd because \( \varphi \) is a maximal solution. Hence the result.

Remarque. Ce résultat est plus faible que le principe de majoration a priori énoncé à la page 400, car le fait que \( \varphi \) ne soit pas bornée n’entraîne pas forcément \( \parallel \varphi \left( t\right) \parallel \rightarrow + \infty \) .

> Remark. This result is weaker than the a priori bound principle stated on page 400, because the fact that \( \varphi \) is not bounded does not necessarily imply \( \parallel \varphi \left( t\right) \parallel \rightarrow + \infty \) .

Cette version faible permet aussi de montrer le corollaire 1. En fait, elle suffit à montrer beaucoup de conséquences du principe de majoration a priori.

> This weak version also allows for proving corollary 1. In fact, it is sufficient to show many consequences of the a priori bound principle.

EXERCICE 2. Soit \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une fonction de classe \( {\mathcal{C}}^{1} \) et bornée sur \( {\mathbb{R}}^{n} \) . Montrer que le champ de vecteurs \( F \) est complet, c’est-à-dire que toute solution maximale de l’équation différentielle \( {X}^{\prime } = F\left( X\right) \) est définie sur \( \mathbb{R} \) tout entier.

> EXERCISE 2. Let \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a function of class \( {\mathcal{C}}^{1} \) and bounded on \( {\mathbb{R}}^{n} \) . Show that the vector field \( F \) is complete, that is, every maximal solution of the differential equation \( {X}^{\prime } = F\left( X\right) \) is defined on the entire \( \mathbb{R} \) .

Solution. Soit \( \varphi : \rbrack a, b\left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) une solution maximale de \( {X}^{\prime } = f\left( X\right) \) . Supposons \( b < + \infty \) . Alors si \( {t}_{0} \in \rbrack a, b\left\lbrack \right. \) , en notant \( M \) un majorant de \( F \) sur \( {\mathbb{R}}^{n} \) , on a d’après l’inégalité des accroissements finis

> Solution. Let \( \varphi : \rbrack a, b\left\lbrack { \rightarrow {\mathbb{R}}^{n}}\right. \) be a maximal solution of \( {X}^{\prime } = f\left( X\right) \) . Suppose \( b < + \infty \) . Then if \( {t}_{0} \in \rbrack a, b\left\lbrack \right. \) , by denoting \( M \) as an upper bound of \( F \) on \( {\mathbb{R}}^{n} \) , we have by the mean value inequality

\[
\forall t \in  \left\lbrack  {{t}_{0}, b\left\lbrack  {,\;\begin{Vmatrix}{\varphi \left( t\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{\varphi \left( {t}_{0}\right) }\end{Vmatrix} + \begin{Vmatrix}{\varphi \left( t\right)  - \varphi \left( {t}_{0}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{\varphi \left( {t}_{0}\right) }\end{Vmatrix} + M\left( {t - {t}_{0}}\right)  \leq  M\left( {b - {t}_{0}}\right) .}\right. }\right.
\]

Ainsi, \( \varphi \) est bornée au voisinage de \( b \) . En appliquant le principe de majoration a priori (ou le résultat de l’exercice précédent), on conclut à une absurdité. Donc \( b = + \infty \) . On montrerait de même \( a = - \infty \) .

> Thus, \( \varphi \) is bounded in the neighborhood of \( b \) . By applying the a priori bound principle (or the result of the previous exercise), we conclude an absurdity. Therefore \( b = + \infty \) . We would show \( a = - \infty \) in the same way.

EXERCICE 3. Soit \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une application de classe \( {\mathcal{C}}^{1} \) . On considère le système différentied \( \left( E\right) : {X}^{\prime } = F\left( X\right) \) . En munissant \( {\mathbb{R}}^{n} \) de la métrique euclidienne standard, on suppose de plus que pour tout \( X \in {\mathbb{R}}^{n} \) tel que \( \parallel X\parallel = 1, F\left( X\right) \cdot X < 0 \) .

> EXERCISE 3. Let \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a \( {\mathcal{C}}^{1} \) class mapping. Consider the differential system \( \left( E\right) : {X}^{\prime } = F\left( X\right) \). By equipping \( {\mathbb{R}}^{n} \) with the standard Euclidean metric, we further assume that for all \( X \in {\mathbb{R}}^{n} \) such that \( \parallel X\parallel = 1, F\left( X\right) \cdot X < 0 \).

Soit \( {X}_{0} \in {\mathbb{R}}^{n} \) vérifiant \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} \leq 1 \) . Montrer qu’il existe une solution \( \varphi \) de \( \left( E\right) \) telle que \( \varphi \left( 0\right) = {X}_{0} \) et définie sur un intervalle de la forme \( \rbrack - \alpha , + \infty \left\lbrack \right. \) avec \( \alpha > 0 \) , vérifiant \( \parallel \varphi \left( t\right) \parallel < 1 \) pour tout \( t > 0. \)

> Let \( {X}_{0} \in {\mathbb{R}}^{n} \) satisfy \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} \leq 1 \). Show that there exists a solution \( \varphi \) to \( \left( E\right) \) such that \( \varphi \left( 0\right) = {X}_{0} \) and defined on an interval of the form \( \rbrack - \alpha , + \infty \left\lbrack \right. \) with \( \alpha > 0 \), satisfying \( \parallel \varphi \left( t\right) \parallel < 1 \) for all \( t > 0. \)

Solution. Le théorème de Cauchy-Lipschitz nous assure l'existence d'une solution maximale \( \varphi \) de \( \left( E\right) \) définie sur un intervalle de la forme \( \rbrack - \alpha ,\beta \lbrack \left( {\alpha ,\beta > 0}\right) \) et vérifiant \( \varphi \left( 0\right) = {X}_{0} \) .

> Solution. The Cauchy-Lipschitz theorem ensures the existence of a maximal solution \( \varphi \) to \( \left( E\right) \) defined on an interval of the form \( \rbrack - \alpha ,\beta \lbrack \left( {\alpha ,\beta > 0}\right) \) and satisfying \( \varphi \left( 0\right) = {X}_{0} \).

Montrons

> Let us show

\[
\exists \eta  \in  \rbrack 0,\beta \left\lbrack  {,\forall t \in  }\right\rbrack  0,\eta \lbrack ,\;\parallel \varphi \left( t\right) \parallel  < 1.
\]

\( \left( *\right) \)

> Si \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} < 1 \) c’est évident par continuité de \( \varphi \) en 0 . Sinon, \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} = 1 \) , donc \( \frac{d}{dt}{\left\lbrack \varphi \left( t\right) \cdot \varphi \left( t\right) \right\rbrack }_{t = 0} = \; 2{\varphi }^{\prime }\left( 0\right) \cdot \varphi \left( 0\right) = {2F}\left( {X}_{0}\right) \cdot {X}_{0} < 0 \) , c’est-à-dire \( \frac{d}{dt}{\left( \parallel \varphi \left( t\right) {\parallel }^{2}\right) }_{t = 0} < 0 \) , d’où \( \left( *\right) \) .

If \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} < 1 \) it is obvious by continuity of \( \varphi \) at 0. Otherwise, \( \begin{Vmatrix}{X}_{0}\end{Vmatrix} = 1 \), therefore \( \frac{d}{dt}{\left\lbrack \varphi \left( t\right) \cdot \varphi \left( t\right) \right\rbrack }_{t = 0} = \; 2{\varphi }^{\prime }\left( 0\right) \cdot \varphi \left( 0\right) = {2F}\left( {X}_{0}\right) \cdot {X}_{0} < 0 \), that is to say \( \frac{d}{dt}{\left( \parallel \varphi \left( t\right) {\parallel }^{2}\right) }_{t = 0} < 0 \), hence \( \left( *\right) \).

> Montrons maintenant que \( \parallel \varphi \left( t\right) \parallel < 1 \) pour tout \( t \in \left\rbrack {0,\beta }\right\lbrack \) . Notons \( \Gamma = \left\{ {{t}_{0} \in }\right\rbrack 0,\beta \lbrack \rbrack \mid \forall t \in \; \rbrack 0,{t}_{0}\left\lbrack {,\parallel \varphi \left( t\right) \parallel < 1\} }\right. \) . D’après (*), \( \Gamma \) est non vide, donc \( \gamma = \sup \Gamma \) existe. Supposons \( \gamma < \beta \) . Alors on a \( \parallel \varphi \left( \gamma \right) \parallel = 1 \) par continuité de \( \varphi \) , et \( \frac{d}{dt}{\left\lbrack \varphi \left( t\right) \cdot \varphi \left( t\right) \right\rbrack }_{t = \gamma } = 2{\varphi }^{\prime }\left( \gamma \right) \cdot \varphi \left( \gamma \right) = {2F}\left( {\varphi \left( \gamma \right) }\right) \cdot \varphi \left( \gamma \right) < 0 \) , c’est-à-dire \( \frac{d}{dt}{\left( \parallel \varphi \left( t\right) {\parallel }^{2}\right) }_{t = \gamma } < 0 \) . On en déduit qu’il existe \( \delta \in \rbrack 0,\gamma \left\lbrack \text{ tel que }\right\rbrack \parallel \varphi \left( \delta \right) \parallel > \parallel \varphi \left( \gamma \right) \parallel = 1 \) . Ceci est absurde par définition de \( \gamma \) . On a donc \( \gamma = \beta \) .

Let us now show that \( \parallel \varphi \left( t\right) \parallel < 1 \) for all \( t \in \left\rbrack {0,\beta }\right\lbrack \) . Let \( \Gamma = \left\{ {{t}_{0} \in }\right\rbrack 0,\beta \lbrack \rbrack \mid \forall t \in \; \rbrack 0,{t}_{0}\left\lbrack {,\parallel \varphi \left( t\right) \parallel < 1\} }\right. \) . According to (*), \( \Gamma \) is non-empty, so \( \gamma = \sup \Gamma \) exists. Suppose \( \gamma < \beta \) . Then we have \( \parallel \varphi \left( \gamma \right) \parallel = 1 \) by continuity of \( \varphi \) , and \( \frac{d}{dt}{\left\lbrack \varphi \left( t\right) \cdot \varphi \left( t\right) \right\rbrack }_{t = \gamma } = 2{\varphi }^{\prime }\left( \gamma \right) \cdot \varphi \left( \gamma \right) = {2F}\left( {\varphi \left( \gamma \right) }\right) \cdot \varphi \left( \gamma \right) < 0 \) , that is to say \( \frac{d}{dt}{\left( \parallel \varphi \left( t\right) {\parallel }^{2}\right) }_{t = \gamma } < 0 \) . We deduce that there exists \( \delta \in \rbrack 0,\gamma \left\lbrack \text{ tel que }\right\rbrack \parallel \varphi \left( \delta \right) \parallel > \parallel \varphi \left( \gamma \right) \parallel = 1 \) . This is absurd by the definition of \( \gamma \) . We therefore have \( \gamma = \beta \) .

> Terminons. La fonction \( \varphi \) est bornée au voisinage de \( \beta \) , donc d’après le principe de majoration a priori (ou le résultat de l’exercice 1), on a \( \beta = + \infty \) . D’où le résultat.

Let us finish. The function \( \varphi \) is bounded in the neighborhood of \( \beta \) , so according to the a priori bound principle (or the result of exercise 1), we have \( \beta = + \infty \) . Hence the result.
