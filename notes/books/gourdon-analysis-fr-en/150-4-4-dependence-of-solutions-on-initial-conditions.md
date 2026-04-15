#### 4.4. Dependence of solutions on initial conditions

*Français : 4.4. Dépendance des solutions vis-à-vis des conditions initiales*

Soit \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (où \( \Omega \) est un ouvert de \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) une application continue et localement lipschitzienne en la seconde variable. Le théorème de Cauchy-Lipschitz dit que pour tout \( \left( {{t}_{0},{X}_{0}}\right) \in \Omega \) , il existe une solution maximale \( {\varphi }_{{t}_{0},{X}_{0}} \) de \( {X}^{\prime } = F\left( {t, X}\right) \) définie sur un intervalle ouvert \( {I}_{{t}_{0},{X}_{0}} \) contenant \( {t}_{0} \) et telle que \( {\varphi }_{{t}_{0},{X}_{0}}\left( {t}_{0}\right) = {X}_{0} \) . En notant

> Let \( F : \Omega \subset \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) (where \( \Omega \) is an open set of \( \mathbb{R} \times {\mathbb{R}}^{n} \) ) be a continuous mapping that is locally Lipschitz in the second variable. The Cauchy-Lipschitz theorem states that for all \( \left( {{t}_{0},{X}_{0}}\right) \in \Omega \) , there exists a maximal solution \( {\varphi }_{{t}_{0},{X}_{0}} \) to \( {X}^{\prime } = F\left( {t, X}\right) \) defined on an open interval \( {I}_{{t}_{0},{X}_{0}} \) containing \( {t}_{0} \) and such that \( {\varphi }_{{t}_{0},{X}_{0}}\left( {t}_{0}\right) = {X}_{0} \) . By denoting

\[
W = \mathop{\bigcup }\limits_{{\left( {{t}_{0},{X}_{0}}\right)  \in  \Omega }}\left\{  \left( {{t}_{0},{X}_{0}}\right) \right\}   \times  {I}_{{t}_{0},{X}_{0}} \subset  \Omega  \times  \mathbb{R},
\]

on peut ainsi définir une application \( \Phi \) de \( W \) dans \( {\mathbb{R}}^{n} \) par \( \Phi \left( {{t}_{0},{X}_{0};t}\right) = {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) . Ainsi, \( \Phi \left( {{t}_{0},{X}_{0};\text{ . }}\right) {est}\operatorname{la}{solution} \) maximale \( \operatorname{de}{X}^{\prime } = F\left( {t, X}\right) \) passant \( = {X}_{0} \) au \( = 0 \)

> we can thus define a mapping \( \Phi \) from \( W \) to \( {\mathbb{R}}^{n} \) by \( \Phi \left( {{t}_{0},{X}_{0};t}\right) = {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) . Thus, \( \Phi \left( {{t}_{0},{X}_{0};\text{ . }}\right) {est}\operatorname{la}{solution} \) maximal \( \operatorname{de}{X}^{\prime } = F\left( {t, X}\right) \) passing \( = {X}_{0} \) through \( = 0 \)

Un problème nouveau (et intéressant) se pose alors : celui de l'étude de la dépendance de \( \Phi \) par rapport à ses paramètres. Ce changement de point de vue s’avère d’ailleurs très fécond dans la théorie des équations différentielles.

> A new (and interesting) problem then arises: that of studying the dependence of \( \Phi \) on its parameters. This change of perspective proves to be very fruitful in the theory of differential equations.

Dans le cas général, on peut montrer que \( W \) est ouvert (cela découle essentiellement du lemme 1 page 399) et que \( \Phi \) est continue sur \( W \) . La démonstration est assez technique. Nous allons démontrer ces résultats dans certains cas particuliers.

> In the general case, we can show that \( W \) is open (this essentially follows from lemma 1 on page 399) and that \( \Phi \) is continuous on \( W \) . The proof is quite technical. We will demonstrate these results in certain specific cases.

Systèmes différentiels linéaires. On considère le système différentiel homogène sur \( {\mathbb{R}}^{n}\left( H\right) : {X}^{\prime } = A\left( t\right) X \) où \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est continue (et \( I \) un intervalle ouvert de \( \mathbb{R} \) ).

> Linear differential systems. We consider the homogeneous differential system on \( {\mathbb{R}}^{n}\left( H\right) : {X}^{\prime } = A\left( t\right) X \) where \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is continuous (and \( I \) an open interval of \( \mathbb{R} \) ).

Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) la base canonique de \( {\mathbb{R}}^{n} \) . Fixons \( {t}_{0} \in I \) . On sait que pour tout \( i \) , il existe une unique solution \( {X}_{i} \) de \( \left( H\right) \) définie sur \( I \) et telle que \( {X}_{i}\left( {t}_{0}\right) = {e}_{i} \) . Pour tout \( t \in I \) , on note \( {M}_{{t}_{0}}\left( t\right) \) la matrice dont les vecteurs colonnes sont les \( {X}_{i}\left( t\right) \) , de sorte que

> Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be the canonical basis of \( {\mathbb{R}}^{n} \) . Let us fix \( {t}_{0} \in I \) . We know that for all \( i \) , there exists a unique solution \( {X}_{i} \) of \( \left( H\right) \) defined on \( I \) and such that \( {X}_{i}\left( {t}_{0}\right) = {e}_{i} \) . For all \( t \in I \) , we denote by \( {M}_{{t}_{0}}\left( t\right) \) the matrix whose column vectors are the \( {X}_{i}\left( t\right) \) , so that

\[
\frac{d}{dt}{M}_{{t}_{0}} = A\left( t\right) {M}_{{t}_{0}}\;\text{ et }\;{M}_{{t}_{0}}\left( {t}_{0}\right)  = {I}_{n}.
\]

Soit \( {X}_{0} \in {\mathbb{R}}^{n} \) . La fonction \( \varphi : t \mapsto {M}_{{t}_{0}}\left( t\right) {X}_{0} \) est donc solution de \( \left( H\right) \) et vérifie \( \varphi \left( {t}_{0}\right) = \; {X}_{0} \) . Avec les notations précédentes, on a donc, pour tout \( t \in I \) , l’égalité \( {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) = \; \Phi \left( {{t}_{0},{X}_{0};t}\right) = {M}_{{t}_{0}}\left( t\right) {X}_{0} \) . La matrice \( {M}_{{t}_{0}}\left( t\right) \) est souvent notée \( R\left( {t,{t}_{0}}\right) \) .

> Let \( {X}_{0} \in {\mathbb{R}}^{n} \) . The function \( \varphi : t \mapsto {M}_{{t}_{0}}\left( t\right) {X}_{0} \) is therefore a solution of \( \left( H\right) \) and satisfies \( \varphi \left( {t}_{0}\right) = \; {X}_{0} \) . With the preceding notations, we therefore have, for all \( t \in I \) , the equality \( {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) = \; \Phi \left( {{t}_{0},{X}_{0};t}\right) = {M}_{{t}_{0}}\left( t\right) {X}_{0} \) . The matrix \( {M}_{{t}_{0}}\left( t\right) \) is often denoted by \( R\left( {t,{t}_{0}}\right) \) .

DÉFINITION 1. L’application \( {I}^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {t,{t}^{\prime }}\right) \mapsto R\left( {t,{t}^{\prime }}\right) \) est appelée la résolvante de \( \left( H\right) \) . Elle vérifie les propriétés suivantes.

> DEFINITION 1. The mapping \( {I}^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {t,{t}^{\prime }}\right) \mapsto R\left( {t,{t}^{\prime }}\right) \) is called the resolvent of \( \left( H\right) \) . It satisfies the following properties.

- Pour tout \( \left( {{t}_{0},{X}_{0}}\right)  \in  I \times  {\mathbb{R}}^{n} \) , la solution \( {\varphi }_{{t}_{0},{X}_{0}} \) de \( \left( H\right) \) vérifiant \( {\varphi }_{{t}_{0},{X}_{0}}\left( {t}_{0}\right)  = {X}_{0} \) s’écrit \( {\varphi }_{{t}_{0},{X}_{0}}\left( t\right)  = R\left( {t,{t}_{0}}\right) {X}_{0} = \Phi \left( {{t}_{0},{X}_{0};t}\right) \) ;

> - For all \( \left( {{t}_{0},{X}_{0}}\right)  \in  I \times  {\mathbb{R}}^{n} \), the solution \( {\varphi }_{{t}_{0},{X}_{0}} \) of \( \left( H\right) \) satisfying \( {\varphi }_{{t}_{0},{X}_{0}}\left( {t}_{0}\right)  = {X}_{0} \) is written as \( {\varphi }_{{t}_{0},{X}_{0}}\left( t\right)  = R\left( {t,{t}_{0}}\right) {X}_{0} = \Phi \left( {{t}_{0},{X}_{0};t}\right) \);

- par construction, on a

> - by construction, we have

\[
\forall \left( {t,{t}^{\prime },{t}^{\prime \prime }}\right)  \in  {I}^{3},\;R\left( {t,{t}^{\prime }}\right)  \circ  R\left( {{t}^{\prime },{t}^{\prime \prime }}\right)  = R\left( {t,{t}^{\prime \prime }}\right) \;\text{ et }\;\forall t \in  I,\;R\left( {t, t}\right)  = {I}_{n}.
\]

- pour tout \( {t}_{0} \in  I \) fixé, on a \( \frac{d}{dt}R\left( {t,{t}_{0}}\right)  = A\left( t\right)  \circ  R\left( {t,{t}_{0}}\right) \) .

> - for any fixed \( {t}_{0} \in  I \), we have \( \frac{d}{dt}R\left( {t,{t}_{0}}\right)  = A\left( t\right)  \circ  R\left( {t,{t}_{0}}\right) \).

Proposition 1. Pour tout \( \left( {t,{t}^{\prime }}\right) \in {I}^{2} \) , on a \( R\left( {t,{t}^{\prime }}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) et \( R{\left( t,{t}^{\prime }\right) }^{-1} = R\left( {{t}^{\prime }, t}\right) \) .

> Proposition 1. For all \( \left( {t,{t}^{\prime }}\right) \in {I}^{2} \), we have \( R\left( {t,{t}^{\prime }}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) and \( R{\left( t,{t}^{\prime }\right) }^{-1} = R\left( {{t}^{\prime }, t}\right) \).

Démonstration. Il suffit de remarquer que \( R\left( {t,{t}^{\prime }}\right) \circ R\left( {{t}^{\prime }, t}\right) = R\left( {t, t}\right) = {I}_{n} \) .

> Proof. It suffices to note that \( R\left( {t,{t}^{\prime }}\right) \circ R\left( {{t}^{\prime }, t}\right) = R\left( {t, t}\right) = {I}_{n} \).

Proposition 2. La résolvante \( R \) est de classe \( {\mathcal{C}}^{1} \) sur \( {I}^{2} \) .

> Proposition 2. The resolvent \( R \) is of class \( {\mathcal{C}}^{1} \) on \( {I}^{2} \).

Démonstration. Fixons \( {t}_{0} \in I \) . Par construction, l’application \( t \mapsto R\left( {t,{t}_{0}}\right) \) est de classe \( {\mathcal{C}}^{1} \) sur I. Maintenant, comme \( R\left( {t,{t}^{\prime }}\right) = R\left( {t,{t}_{0}}\right) \circ R\left( {{t}_{0},{t}^{\prime }}\right) = R\left( {t,{t}_{0}}\right) \circ R{\left( {t}^{\prime },{t}_{0}\right) }^{-1} \) , on en conclut que \( R \) est de classe \( {\mathcal{C}}^{1} \) sur \( {I}^{2} \) .

> Proof. Let us fix \( {t}_{0} \in I \). By construction, the mapping \( t \mapsto R\left( {t,{t}_{0}}\right) \) is of class \( {\mathcal{C}}^{1} \) on I. Now, since \( R\left( {t,{t}^{\prime }}\right) = R\left( {t,{t}_{0}}\right) \circ R\left( {{t}_{0},{t}^{\prime }}\right) = R\left( {t,{t}_{0}}\right) \circ R{\left( {t}^{\prime },{t}_{0}\right) }^{-1} \), we conclude that \( R \) is of class \( {\mathcal{C}}^{1} \) on \( {I}^{2} \).

Proposition 3. L’application \( \Phi : \left( {{t}_{0},{X}_{0};t}\right) \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) = {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) est continue sur \( I \times {\mathbb{R}}^{n} \times I. \)

> Proposition 3. The mapping \( \Phi : \left( {{t}_{0},{X}_{0};t}\right) \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) = {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) is continuous on \( I \times {\mathbb{R}}^{n} \times I. \)

Démonstration. Il suffit d’écrire \( \Phi \left( {{t}_{0},{X}_{0};t}\right) = R\left( {t,{t}_{0}}\right) {X}_{0} \) et d’utiliser la proposition précédente.

> Proof. It suffices to write \( \Phi \left( {{t}_{0},{X}_{0};t}\right) = R\left( {t,{t}_{0}}\right) {X}_{0} \) and use the previous proposition.

Remarque 1. - Les colonnes de la matrice \( R\left( {t,{t}_{0}}\right) \) sont des solutions de \( \left( H\right) \) , donc det \( R\left( {t,{t}_{0}}\right) \) est un wronskien. En particulier, d’après le résultat de la question b) de l'exercice 7 page 388, on a

> Remark 1. - The columns of the matrix \( R\left( {t,{t}_{0}}\right) \) are solutions of \( \left( H\right) \), so det \( R\left( {t,{t}_{0}}\right) \) is a Wronskian. In particular, according to the result of question b) of exercise 7 on page 388, we have

\[
\det R\left( {t,{t}_{0}}\right)  = \left\lbrack  {\det R\left( {{t}_{0},{t}_{0}}\right) }\right\rbrack  \exp \left( {{\int }_{{t}_{0}}^{t}\operatorname{tr}A\left( s\right) {ds}}\right)  = \exp \left( {{\int }_{{t}_{0}}^{t}\operatorname{tr}A\left( s\right) {ds}}\right) .
\]

- Connaissant \( R\left( {t,{t}_{0}}\right) \) , la méthode de variation des constantes pour résoudre le système différentiel \( \left( L\right)  : {X}^{\prime } = A\left( t\right) X + b\left( t\right) \) en terme de résolvante s’exprime comme suit : on cherche les solutions \( \varphi \) de \( \left( L\right) \) sous la forme \( \varphi \left( t\right)  = R\left( {t,{t}_{0}}\right) \psi \left( t\right) \) , où \( \psi  : I \rightarrow  {\mathbb{R}}^{n} \) est une fonction \( {\mathcal{C}}^{1} \) encore inconnue. La fonction \( \varphi \) est solution de (L) si et seulement si

> - Knowing \( R\left( {t,{t}_{0}}\right) \), the method of variation of constants to solve the differential system \( \left( L\right)  : {X}^{\prime } = A\left( t\right) X + b\left( t\right) \) in terms of the resolvent is expressed as follows: we look for solutions \( \varphi \) of \( \left( L\right) \) in the form \( \varphi \left( t\right)  = R\left( {t,{t}_{0}}\right) \psi \left( t\right) \), where \( \psi  : I \rightarrow  {\mathbb{R}}^{n} \) is a function \( {\mathcal{C}}^{1} \) yet to be determined. The function \( \varphi \) is a solution of (L) if and only if

\[
\forall t \in  I,\;\frac{d\varphi }{dt}\left( t\right)  = A\left( t\right)  \circ  R\left( {t,{t}_{0}}\right) \psi \left( t\right)  + R\left( {t,{t}_{0}}\right) \left( {\frac{d\psi }{dt}\left( t\right) }\right)  = A\left( t\right)  \circ  R\left( {t,{t}_{0}}\right) \psi \left( t\right)  + b\left( t\right) ,
\]

ce qui équivaut à \( \frac{d\psi }{dt}\left( t\right) = R{\left( t,{t}_{0}\right) }^{-1}b\left( t\right) = R\left( {{t}_{0}, t}\right) b\left( t\right) \) . La solution \( \varphi \) de \( \left( L\right) \) vérifiant \( \varphi \left( {t}_{0}\right) = {X}_{0} \) , notée \( {\varphi }_{{t}_{0},{X}_{0}} \) , est donc donnée par

> which is equivalent to \( \frac{d\psi }{dt}\left( t\right) = R{\left( t,{t}_{0}\right) }^{-1}b\left( t\right) = R\left( {{t}_{0}, t}\right) b\left( t\right) \). The solution \( \varphi \) of \( \left( L\right) \) satisfying \( \varphi \left( {t}_{0}\right) = {X}_{0} \), denoted \( {\varphi }_{{t}_{0},{X}_{0}} \), is therefore given by

\[
{\varphi }_{{t}_{0},{X}_{0}}\left( t\right)  = R\left( {t,{t}_{0}}\right) \left\lbrack  {{X}_{0} + {\int }_{{t}_{0}}^{t}R\left( {{t}_{0}, s}\right) b\left( s\right) {ds}}\right\rbrack  .
\]

On en déduit la proposition qui suit.

> We deduce the following proposition.

Proposition 4. Soit le système différentiel \( \left( L\right) : {X}^{\prime } = A\left( t\right) X + b\left( t\right) \) , où \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et \( b : I \rightarrow {\mathbb{R}}^{n} \) sont continues. Avec les notations précédentes, la fonction \( \Phi : \left( {{t}_{0},{X}_{0};t}\right) \mapsto \; {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) est continue sur \( I \times {\mathbb{R}}^{n} \times I \) .

> Proposition 4. Let the differential system \( \left( L\right) : {X}^{\prime } = A\left( t\right) X + b\left( t\right) \), where \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and \( b : I \rightarrow {\mathbb{R}}^{n} \) are continuous. With the preceding notations, the function \( \Phi : \left( {{t}_{0},{X}_{0};t}\right) \mapsto \; {\varphi }_{{t}_{0},{X}_{0}}\left( t\right) \) is continuous on \( I \times {\mathbb{R}}^{n} \times I \).

##### Case of differential equations of the form \( {X}^{\prime } = F\left( X\right) \).

*Français : Cas des équations différentielles de la forme \( {X}^{\prime } = F\left( X\right) \) .*

Proposition 5. Soit \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une fonction localement lipschitzienne. Conformé- ment aux notations précédentes, on note \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \) la solution maximale \( \varphi \) de \( {X}^{\prime } = F\left( X\right) \) telle que \( \varphi \left( {t}_{0}\right) = {X}_{0} \) .

> Proposition 5. Let \( F : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a locally Lipschitz function. In accordance with the preceding notations, we denote by \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \) the maximal solution \( \varphi \) of \( {X}^{\prime } = F\left( X\right) \) such that \( \varphi \left( {t}_{0}\right) = {X}_{0} \).

Soit \( \left( {{t}_{0},{X}_{0}}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \) , et notons \( \rbrack a, b\lbrack \) l’intervalle de définition de la solution maximale \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \) . Alors pour tout \( \alpha \in \mathbb{R} \) , la solution maximale \( t \mapsto \Phi \left( {{t}_{0} + \alpha ,{X}_{0}, t}\right) \) est définie sur \( \rbrack a + \alpha , b + \alpha \lbrack \) et on a

> Let \( \left( {{t}_{0},{X}_{0}}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \), and let us denote by \( \rbrack a, b\lbrack \) the interval of definition of the maximal solution \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \). Then for all \( \alpha \in \mathbb{R} \), the maximal solution \( t \mapsto \Phi \left( {{t}_{0} + \alpha ,{X}_{0}, t}\right) \) is defined on \( \rbrack a + \alpha , b + \alpha \lbrack \) and we have

\[
\forall t \in  \rbrack a + \alpha , b + \alpha \lbrack ,\;\Phi \left( {{t}_{0} + \alpha ,{X}_{0};t}\right)  = \Phi \left( {{t}_{0},{X}_{0};t - \alpha }\right) .
\]

Démonstration. Posons \( \varphi : \rbrack a, b\left\lbrack { \rightarrow {\mathbb{R}}^{n}\;t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \text{ et }\psi : }\right\rbrack a + \alpha , b + \alpha \lbrack \rightarrow {\mathbb{R}}^{n}\;t \mapsto \varphi \left( {t - \alpha }\right) \) . On vérifie facilement que \( {\psi }^{\prime } = F\left( \psi \right) \) , et comme \( \psi \left( {{t}_{0} + \alpha }\right) = \varphi \left( {t}_{0}\right) = {X}_{0} \) , on a \( \psi \left( t\right) = \Phi \left( {{t}_{0} + }\right. \; \left. {\alpha ,{X}_{0};t}\right) \) pour tout \( t \in \rbrack a + \alpha , b + \alpha \lbrack \) .

> Proof. Let \( \varphi : \rbrack a, b\left\lbrack { \rightarrow {\mathbb{R}}^{n}\;t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \text{ et }\psi : }\right\rbrack a + \alpha , b + \alpha \lbrack \rightarrow {\mathbb{R}}^{n}\;t \mapsto \varphi \left( {t - \alpha }\right) \). We easily verify that \( {\psi }^{\prime } = F\left( \psi \right) \), and since \( \psi \left( {{t}_{0} + \alpha }\right) = \varphi \left( {t}_{0}\right) = {X}_{0} \), we have \( \psi \left( t\right) = \Phi \left( {{t}_{0} + }\right. \; \left. {\alpha ,{X}_{0};t}\right) \) for all \( t \in \rbrack a + \alpha , b + \alpha \lbrack \).

Or \( \psi \) est une solution maximale (sinon \( \varphi \) ne serait pas une solution maximale), donc \( t \mapsto \; \Phi \left( {{t}_{0} + \alpha ,{X}_{0};t}\right) \) est définie sur \( \rbrack a + \alpha , b + \alpha \lbrack \) et

> However, \( \psi \) is a maximal solution (otherwise \( \varphi \) would not be a maximal solution), so \( t \mapsto \; \Phi \left( {{t}_{0} + \alpha ,{X}_{0};t}\right) \) is defined on \( \rbrack a + \alpha , b + \alpha \lbrack \) and

\[
\forall t \in  \rbrack a + \alpha , b + \alpha \lbrack ,\;\Phi \left( {{t}_{0} + \alpha ,{X}_{0};t}\right)  = \psi \left( t\right)  = \varphi \left( {t - \alpha }\right)  = \Phi \left( {{t}_{0},{X}_{0};t - \alpha }\right) .
\]

Dans l’exercice qui suit, on montre la continuité de \( \Phi \) dans un autre cas particulier.

> In the following exercise, we show the continuity of \( \Phi \) in another special case.

Exercices.

> Exercises.

EXERCICE 1. Soit \( F : \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) une application de classe \( {\mathcal{C}}^{1} \) et globalement lipschit-zienne en la seconde variable, i. e.

> EXERCISE 1. Let \( F : \mathbb{R} \times {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n} \) be a mapping of class \( {\mathcal{C}}^{1} \) and globally Lipschitz in the second variable, i.e.

\[
\exists L > 0,\forall X, Y \in  {\mathbb{R}}^{n},\forall t \in  \mathbb{R},\;\parallel F\left( {t, X}\right)  - F\left( {t, Y}\right) \parallel  \leq  L\parallel X - Y\parallel .
\]

a) Montrer que les solutions maximales de \( {X}^{\prime } = F\left( {t, X}\right) \) sont définies sur \( \mathbb{R} \) .

> a) Show that the maximal solutions of \( {X}^{\prime } = F\left( {t, X}\right) \) are defined on \( \mathbb{R} \).

b) Pour tout \( {t}_{0} \in \mathbb{R} \) , pour tout \( {X}_{0} \in {\mathbb{R}}^{n} \) , on note \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \) la solution sur \( \mathbb{R} \) de \( {X}^{\prime } = F\left( {t, X}\right) \) qui prend la valeur \( {X}_{0} \) au point \( {t}_{0} \) . Montrer que l’application \( \Phi \) ainsi définie est continue sur \( \mathbb{R} \times {\mathbb{R}}^{n} \times \mathbb{R} \) .

> b) For all \( {t}_{0} \in \mathbb{R} \), for all \( {X}_{0} \in {\mathbb{R}}^{n} \), let \( t \mapsto \Phi \left( {{t}_{0},{X}_{0};t}\right) \) denote the solution on \( \mathbb{R} \) of \( {X}^{\prime } = F\left( {t, X}\right) \) that takes the value \( {X}_{0} \) at point \( {t}_{0} \). Show that the mapping \( \Phi \) thus defined is continuous on \( \mathbb{R} \times {\mathbb{R}}^{n} \times \mathbb{R} \).

Solution. a) Soit \( \varphi \) une solution maximale de \( {X}^{\prime } = F\left( {t, X}\right) \) définie sur \( \rbrack a, b\lbrack \) . Supposons par exemple \( b < + \infty \) . Soit \( c \in \rbrack a, b\lbrack \) . Alors pour tout \( t \in \lbrack c, b\lbrack \) ,

> Solution. a) Let \( \varphi \) be a maximal solution of \( {X}^{\prime } = F\left( {t, X}\right) \) defined on \( \rbrack a, b\lbrack \). Suppose, for example, \( b < + \infty \). Let \( c \in \rbrack a, b\lbrack \). Then for all \( t \in \lbrack c, b\lbrack \),

\[
\begin{Vmatrix}{{\varphi }^{\prime }\left( t\right) }\end{Vmatrix} = \parallel F\left( {t,\varphi \left( t\right) }\right) \parallel  \leq  \parallel F\left( {t,\varphi \left( t\right) }\right)  - F\left( {t,0}\right) \parallel  + \parallel F\left( {t,0}\right) \parallel  \leq  L\parallel \varphi \left( t\right) \parallel  + M,
\]

où \( M \) est un majorant de \( t \mapsto F\left( {t,0}\right) \) sur le compact \( \left\lbrack {c, b}\right\rbrack \) . On en conclut, avec le corollaire 2 du lemme de Gronwall (page 398), que \( \varphi \) est bornée au voisinage de \( b \) . Ceci est absurde d’après le principe de majoration a priori (ou le résultat de l’exercice 1 page 401). On a donc \( b = + \infty \) . On montrerait de même \( a = - \infty \) .

> where \( M \) is an upper bound of \( t \mapsto F\left( {t,0}\right) \) on the compact set \( \left\lbrack {c, b}\right\rbrack \). We conclude, with corollary 2 of Gronwall's lemma (page 398), that \( \varphi \) is bounded in the neighborhood of \( b \). This is absurd according to the a priori estimate principle (or the result of exercise 1, page 401). We therefore have \( b = + \infty \). We would show \( a = - \infty \) similarly.

b) On procède en plusieurs étapes.

> b) We proceed in several steps.

(i) Fixons d’abord \( {t}_{0} \in {\mathbb{R}}^{n} \) . Pour tout \( X \in {\mathbb{R}}^{n} \) , on note \( {\varphi }_{X} : \mathbb{R} \rightarrow \mathbb{R}\;t \mapsto \varphi \left( {{t}_{0}, X;t}\right) \) . On a \( \forall t, \in \mathbb{R},\forall X, Y \in {\mathbb{R}}^{n},\;\begin{Vmatrix}{{\varphi }_{X}^{\prime }\left( t\right) - {\varphi }_{Y}^{\prime }\left( t\right) }\end{Vmatrix} = \begin{Vmatrix}{F\left( {t,{\varphi }_{X}\left( t\right) }\right) - F\left( {t,{\varphi }_{Y}\left( t\right) }\right) }\end{Vmatrix} \leq L\begin{Vmatrix}{{\varphi }_{X}\left( t\right) - {\varphi }_{Y}\left( t\right) }\end{Vmatrix}, \) donc d'après le corollaire 2 du lemme de Gronwall,

> (i) Let us first fix \( {t}_{0} \in {\mathbb{R}}^{n} \) . For any \( X \in {\mathbb{R}}^{n} \) , we denote \( {\varphi }_{X} : \mathbb{R} \rightarrow \mathbb{R}\;t \mapsto \varphi \left( {{t}_{0}, X;t}\right) \) . We have \( \forall t, \in \mathbb{R},\forall X, Y \in {\mathbb{R}}^{n},\;\begin{Vmatrix}{{\varphi }_{X}^{\prime }\left( t\right) - {\varphi }_{Y}^{\prime }\left( t\right) }\end{Vmatrix} = \begin{Vmatrix}{F\left( {t,{\varphi }_{X}\left( t\right) }\right) - F\left( {t,{\varphi }_{Y}\left( t\right) }\right) }\end{Vmatrix} \leq L\begin{Vmatrix}{{\varphi }_{X}\left( t\right) - {\varphi }_{Y}\left( t\right) }\end{Vmatrix}, \) , so according to corollary 2 of Gronwall's lemma,

\[
\forall t \in  \mathbb{R},\;\begin{Vmatrix}{{\varphi }_{X}\left( t\right)  - {\varphi }_{Y}\left( t\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{{\varphi }_{X}\left( {t}_{0}\right)  - {\varphi }_{Y}\left( {t}_{0}\right) }\end{Vmatrix}{e}^{L\left| {t - {t}_{0}}\right| },
\]

ce qui s'écrit aussi

> which can also be written as

\[
\forall t \in  \mathbb{R},\forall X, Y \in  {\mathbb{R}}^{n},\;\begin{Vmatrix}{\Phi \left( {{t}_{0}, X;t}\right)  - \Phi \left( {{t}_{0}, Y;t}\right) }\end{Vmatrix} \leq  \parallel X - Y\parallel {e}^{L\left| {t - {t}_{0}}\right| }.
\]

(*)

> En écrivant maintenant

By now writing

\[
\begin{Vmatrix}{\Phi \left( {{t}_{0}, X;t}\right)  - \Phi \left( {{t}_{0}, Y;{t}^{\prime }}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{\Phi \left( {{t}_{0}, X;t}\right)  - \Phi \left( {{t}_{0}, X;{t}^{\prime }}\right) }\end{Vmatrix} + \begin{Vmatrix}{\Phi \left( {{t}_{0}, X;{t}^{\prime }}\right)  - \Phi \left( {{t}_{0}, Y,{t}^{\prime }}\right) }\end{Vmatrix}
\]

\[
\leq  \begin{Vmatrix}{\Phi \left( {{t}_{0}, X;t}\right)  - \Phi \left( {{t}_{0}, X;{t}^{\prime }}\right) }\end{Vmatrix} + \parallel X - Y\parallel {e}^{L\left| {{t}^{\prime } - {t}_{0}}\right| },
\]

on en conclut que pour tout \( {t}_{0} \in \mathbb{R} \) fixé, l’application \( \left( {X, t}\right) \mapsto \Phi \left( {{t}_{0}, X;t}\right) \) est continue.

> we conclude that for any fixed \( {t}_{0} \in \mathbb{R} \) , the mapping \( \left( {X, t}\right) \mapsto \Phi \left( {{t}_{0}, X;t}\right) \) is continuous.

(ii) Montrons maintenant, pour \( {t}_{1} \in \mathbb{R} \) fixé, la continuité de \( \left( {t, X}\right) \mapsto \Phi \left( {t, X;{t}_{1}}\right) \) . Soit \( \left( {{t}_{0},{X}_{0}}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \) . Pour tout \( \left( {t, X}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \) , on a

> (ii) Let us now show, for fixed \( {t}_{1} \in \mathbb{R} \), the continuity of \( \left( {t, X}\right) \mapsto \Phi \left( {t, X;{t}_{1}}\right) \). Let \( \left( {{t}_{0},{X}_{0}}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \). For any \( \left( {t, X}\right) \in \mathbb{R} \times {\mathbb{R}}^{n} \), we have

\[
\Phi \left( {t, X;{t}_{1}}\right)  = \Phi \left( {{t}_{0},\Phi \left( {t, X;{t}_{0}}\right) ,{t}_{1}}\right)
\]

(en effet, pour \( t, X,{t}_{0} \) fixés, ces deux fonctions de \( {t}_{1} \) sont des solutions de \( {X}^{\prime } = F\left( {t, X}\right) \) qui coïncident en \( {t}_{1} = {t}_{0} \) , elles sont donc égales d’après le théorème de Cauchy-Lipschitz). On en conclut avec (*) que

> (indeed, for fixed \( t, X,{t}_{0} \), these two functions of \( {t}_{1} \) are solutions to \( {X}^{\prime } = F\left( {t, X}\right) \) that coincide at \( {t}_{1} = {t}_{0} \), so they are equal according to the Cauchy-Lipschitz theorem). We conclude from (*) that

\[
\begin{Vmatrix}{\Phi \left( {t, X;{t}_{1}}\right)  - \Phi \left( {{t}_{0},{X}_{0};{t}_{1}}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{\Phi \left( {t, X;{t}_{0}}\right)  - {X}_{0}}\end{Vmatrix}{e}^{L\left| {{t}_{1} - {t}_{0}}\right| }.
\]

Or \( {X}_{0} = \Phi \left( {{t}_{0},{X}_{0};{t}_{0}}\right) = \Phi \left( {t,\Phi \left( {{t}_{0},{X}_{0};t}\right) ;{t}_{0}}\right) \) , donc toujours d’après (*)

> However \( {X}_{0} = \Phi \left( {{t}_{0},{X}_{0};{t}_{0}}\right) = \Phi \left( {t,\Phi \left( {{t}_{0},{X}_{0};t}\right) ;{t}_{0}}\right) \), so still according to (*)

\[
\begin{Vmatrix}{\Phi \left( {t, X;{t}_{0}}\right)  - {X}_{0}}\end{Vmatrix} \leq  \begin{Vmatrix}{X - \Phi \left( {{t}_{0},{X}_{0};t}\right) }\end{Vmatrix}{e}^{L\left| {t - {t}_{0}}\right| }.
\]

On en déduit

> We deduce from this

\[
\begin{Vmatrix}{\Phi \left( {t, X;{t}_{1}}\right)  - \Phi \left( {{t}_{0},{X}_{0};{t}_{1}}\right) }\end{Vmatrix} \leq  \begin{Vmatrix}{X - \Phi \left( {{t}_{0},{X}_{0};t}\right) }\end{Vmatrix}{e}^{L\left( {\left| {t - {t}_{0}}\right|  + \left| {{t}_{1} - {t}_{0}}\right| }\right) }.
\]

Ceci entraîne que lorsque \( \left( {t, X}\right) \rightarrow \left( {{t}_{0},{X}_{0}}\right) \) , on a \( \Phi \left( {t, X;{t}_{1}}\right) \rightarrow \Phi \left( {{t}_{0},{X}_{0};{t}_{1}}\right) \) , d’où la continuité voulue.

> This implies that when \( \left( {t, X}\right) \rightarrow \left( {{t}_{0},{X}_{0}}\right) \), we have \( \Phi \left( {t, X;{t}_{1}}\right) \rightarrow \Phi \left( {{t}_{0},{X}_{0};{t}_{1}}\right) \), hence the desired continuity.

(iii) Il suffit maintenant d’écrire \( \Phi \left( {s, X;t}\right) = \Phi \left( {{t}_{0},\Phi \left( {s, X;{t}_{0}}\right) ;t}\right) \) (pour \( {t}_{0} \) fixé), pour conclure que \( \Phi : \left( {s, X;t}\right) \mapsto \Phi \left( {s, X;t}\right) \) est continue.

> (iii) It now suffices to write \( \Phi \left( {s, X;t}\right) = \Phi \left( {{t}_{0},\Phi \left( {s, X;{t}_{0}}\right) ;t}\right) \) (for fixed \( {t}_{0} \)) to conclude that \( \Phi : \left( {s, X;t}\right) \mapsto \Phi \left( {s, X;t}\right) \) is continuous.

EXERCICE 2. Soit \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) , globalement lipschitzienne en la seconde variable, telle que

> EXERCISE 2. Let \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{1} \), globally Lipschitz in the second variable, such that

\[
\forall t \in  {\mathbb{R}}^{ + },\;f\left( {t,1}\right)  > 0,\;f\left( {t, - 1}\right)  < 0.
\]

Montrer qu’il existe une fonction \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) solution de \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \) vérifiant \( \left| {\varphi \left( t\right) }\right| < 1 \) pour tout \( t \geq 0 \) (on pourra utiliser le résultat de l’exercice précédent).

> Show that there exists a function \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) that is a solution to \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \) satisfying \( \left| {\varphi \left( t\right) }\right| < 1 \) for all \( t \geq 0 \) (one may use the result of the previous exercise).

Solution. D'après l'exercice précédent, les solutions maximales de \( \left( E\right) \) sont définies sur \( \mathbb{R} \) . De plus, en notant \( t \mapsto \Phi \left( {a, t}\right) \) la solution maximale de \( \left( E\right) \) prenant la valeur \( a \) en \( t = 0 \) , la fonction \( \Phi : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) ansi définie est continue.

> Solution. According to the previous exercise, the maximal solutions of \( \left( E\right) \) are defined on \( \mathbb{R} \). Furthermore, by denoting \( t \mapsto \Phi \left( {a, t}\right) \) as the maximal solution of \( \left( E\right) \) taking the value \( a \) at \( t = 0 \), the function \( \Phi : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) thus defined is continuous.

Remarquons maintenant le fait suivant. Si \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) est solution de \( \left( E\right) \) et s’il existe \( {t}_{0} \geq 0 \) tel que \( \varphi \left( {t}_{0}\right) > 1 \) , alors \( \varphi \left( t\right) > 1 \) pour tout \( t \geq {t}_{0} \) . En effet, supposons qu’il existe \( {t}_{1} > {t}_{0} \) tel que \( \varphi \left( {t}_{1}\right) \leq 1 \) . Alors il existe \( u \in \rbrack {t}_{0},{t}_{1}\rbrack \) tel que \( \varphi \left( u\right) = 1 \) d’après le théorème des valeurs intermédiaires. Autrement dit, le fermé \( {\varphi }^{-1}\left( {\{ 1\} }\right) \) a une intersection non vide avec \( \rbrack {t}_{0},{t}_{1}\rbrack \) . Notons \( {t}_{2} = \inf {\varphi }^{-1}\left( {\{ 1\} }\right) \cap \left\lbrack {{t}_{0},{t}_{1}}\right\rbrack \) . On a \( \varphi \left( {t}_{2}\right) = 1 \) et \( {t}_{2} \neq {t}_{0}\left( {\operatorname{car}\varphi \left( {t}_{0}\right) > 1}\right) \) , et \( \varphi \left( t\right) > 1 \) pour tout \( t \in \rbrack {t}_{0},{t}_{2}\left\lbrack {\text{ , donc }{\varphi }^{\prime }\left( {t}_{2}\right) \leq 0,}\right. \) ce qui est absurde puisque \( {\varphi }^{\prime }\left( {t}_{2}\right) = f\left( {{t}_{2},\varphi \left( {t}_{2}\right) }\right) = f\left( {{t}_{2},1}\right) > 0 \) . On montrerait de même que s’il existe \( {t}_{0} \geq 0 \) tel que \( \varphi \left( {t}_{0}\right) < - 1 \) , alors \( \varphi \left( t\right) < - 1 \) pour tout \( t \geq {t}_{0} \) .

> Let us now note the following fact. If \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) is a solution to \( \left( E\right) \) and there exists \( {t}_{0} \geq 0 \) such that \( \varphi \left( {t}_{0}\right) > 1 \), then \( \varphi \left( t\right) > 1 \) for all \( t \geq {t}_{0} \). Indeed, suppose there exists \( {t}_{1} > {t}_{0} \) such that \( \varphi \left( {t}_{1}\right) \leq 1 \). Then there exists \( u \in \rbrack {t}_{0},{t}_{1}\rbrack \) such that \( \varphi \left( u\right) = 1 \) according to the intermediate value theorem. In other words, the closed set \( {\varphi }^{-1}\left( {\{ 1\} }\right) \) has a non-empty intersection with \( \rbrack {t}_{0},{t}_{1}\rbrack \). Let us denote \( {t}_{2} = \inf {\varphi }^{-1}\left( {\{ 1\} }\right) \cap \left\lbrack {{t}_{0},{t}_{1}}\right\rbrack \). We have \( \varphi \left( {t}_{2}\right) = 1 \) and \( {t}_{2} \neq {t}_{0}\left( {\operatorname{car}\varphi \left( {t}_{0}\right) > 1}\right) \), and \( \varphi \left( t\right) > 1 \) for all \( t \in \rbrack {t}_{0},{t}_{2}\left\lbrack {\text{ , donc }{\varphi }^{\prime }\left( {t}_{2}\right) \leq 0,}\right. \), which is absurd since \( {\varphi }^{\prime }\left( {t}_{2}\right) = f\left( {{t}_{2},\varphi \left( {t}_{2}\right) }\right) = f\left( {{t}_{2},1}\right) > 0 \). We would show similarly that if there exists \( {t}_{0} \geq 0 \) such that \( \varphi \left( {t}_{0}\right) < - 1 \), then \( \varphi \left( t\right) < - 1 \) for all \( t \geq {t}_{0} \).

Ceci étant, notons

> This being said, let us denote

\[
{A}^{ + } = \left\{  {y \in  \left\lbrack  {-1,1}\right\rbrack  \mid \exists t \in  {\mathbb{R}}^{ + },\Phi \left( {y, t}\right)  > 1}\right\}  \;\text{ et }\;{A}^{ - } = \left\{  {y \in  \left\lbrack  {-1,1}\right\rbrack  \mid \exists t \in  {\mathbb{R}}^{ + },\Phi \left( {y, t}\right)  <  - 1}\right\}  .
\]

Comme \( \Phi \) est continue, on voit facilement que \( {A}^{ + } \) et \( {A}^{ - } \) sont des ouverts de \( \left\lbrack {-1,1}\right\rbrack \) . Par ailleurs, \( {A}^{ + } \neq \varnothing \) . En effet, si \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) est la solution de \( \left( E\right) \) vérifiant \( \varphi \left( 1\right) = 1 \) , on ne peut pas avoir \( \varphi \left( 0\right) > 1 \) (sinon \( \varphi \left( t\right) > 1 \) sur \( {\mathbb{R}}^{ + } \) d’après le principe énoncé plus haut), et de même, on ne peut pas avoir \( \varphi \left( 0\right) < - 1 \) . Donc \( \varphi \left( 0\right) \in \left\lbrack {-1,1}\right\rbrack \) , et comme \( \varphi \left( 1\right) = 1 \) et \( {\varphi }^{\prime }\left( 1\right) = f\left( {1,1}\right) > 0 \) , on a \( \varphi \left( t\right) > 1 \) sur un voisinage à droite de 1, d’où \( y = \varphi \left( 0\right) \in {A}^{ + } \) . De même, \( {A}^{ - } \) est non vide.

> Since \( \Phi \) is continuous, it is easy to see that \( {A}^{ + } \) and \( {A}^{ - } \) are open sets of \( \left\lbrack {-1,1}\right\rbrack \) . Furthermore, \( {A}^{ + } \neq \varnothing \) . Indeed, if \( \varphi : \mathbb{R} \rightarrow \mathbb{R} \) is the solution to \( \left( E\right) \) satisfying \( \varphi \left( 1\right) = 1 \) , we cannot have \( \varphi \left( 0\right) > 1 \) (otherwise \( \varphi \left( t\right) > 1 \) on \( {\mathbb{R}}^{ + } \) according to the principle stated above), and likewise, we cannot have \( \varphi \left( 0\right) < - 1 \) . Thus \( \varphi \left( 0\right) \in \left\lbrack {-1,1}\right\rbrack \) , and since \( \varphi \left( 1\right) = 1 \) and \( {\varphi }^{\prime }\left( 1\right) = f\left( {1,1}\right) > 0 \) , we have \( \varphi \left( t\right) > 1 \) on a neighborhood to the right of 1, hence \( y = \varphi \left( 0\right) \in {A}^{ + } \) . Similarly, \( {A}^{ - } \) is non-empty.

On a \( {A}^{ + } \cap {A}^{ - } = \varnothing \) . En effet, raisonnons par l’absurde en supposant que \( {A}^{ + } \cap {A}^{ - } \) contienne un élément \( y \) . Notons \( \varphi : t \mapsto \Phi \left( {y, t}\right) \) , et soient \( {t}_{1},{t}_{2} > 0 \) tels que \( \varphi \left( {t}_{1}\right) > 1 \) et \( \varphi \left( {t}_{2}\right) < - 1 \) . On a \( \varphi \left( {t}_{1}\right) > 1 \) donc \( \varphi \left( t\right) > 1 \) pour tout \( t > {t}_{1} \) d’après le principé énoncé plus haut, d’où \( {t}_{2} < {t}_{1} \) . On montrerait de même \( {t}_{1} < {t}_{2} \) , ce qui est absurde. Donc \( {A}^{ + } \cap {A}^{ - } = \varnothing \) .

> We have \( {A}^{ + } \cap {A}^{ - } = \varnothing \) . Indeed, let us reason by contradiction by assuming that \( {A}^{ + } \cap {A}^{ - } \) contains an element \( y \) . Let \( \varphi : t \mapsto \Phi \left( {y, t}\right) \) , and let \( {t}_{1},{t}_{2} > 0 \) be such that \( \varphi \left( {t}_{1}\right) > 1 \) and \( \varphi \left( {t}_{2}\right) < - 1 \) . We have \( \varphi \left( {t}_{1}\right) > 1 \) so \( \varphi \left( t\right) > 1 \) for all \( t > {t}_{1} \) according to the principle stated above, hence \( {t}_{2} < {t}_{1} \) . We would show \( {t}_{1} < {t}_{2} \) in the same way, which is absurd. Therefore \( {A}^{ + } \cap {A}^{ - } = \varnothing \) .

Comme \( \left\lbrack {-1,1}\right\rbrack \) est connexe et que \( {A}^{ + } \) et \( {A}^{ - } \) sont deux ouverts disjoints et non vides de \( \left\lbrack {-1,1}\right\rbrack \) , on ne peut pas avoir \( {A}^{ + } \cup {A}^{ - } = \left\lbrack {-1,1}\right\rbrack \) . Il existe donc \( {y}_{0} \in \left\lbrack {-1,1}\right\rbrack \) tel que \( {y}_{0} \notin {A}^{ + } \cup {A}^{ - } \) . On voit alors que la fonction \( \varphi = \Phi \left( {{y}_{0},\text{ . }}\right) \) vérifie \( \left| {\varphi \left( t\right) }\right| \leq 1 \) pour tout \( t \in {\mathbb{R}}^{ + } \) . Si \( \left| {\varphi \left( {t}_{0}\right) }\right| = 1 \) pour un \( {t}_{0} \geq 0 \) , par exemple \( \varphi \left( {t}_{0}\right) = 1 \) , le fait que \( {\varphi }^{\prime }\left( {t}_{0}\right) = f\left( {{t}_{0},1}\right) > 0 \) montre que sur un voisinage à droite de \( {t}_{0},\varphi \left( t\right) > 1 \) , donc \( {y}_{0} \in {A}^{ + } \) ce qui est absurde. Finalement, \( \varphi \) est une solution de \( \left( E\right) \) sur \( \mathbb{R} \) qui vérifie \( \left| {\varphi \left( t\right) }\right| < 1 \) pour tout \( t \in {\mathbb{R}}^{ + } \) .

> Since \( \left\lbrack {-1,1}\right\rbrack \) is connected and \( {A}^{ + } \) and \( {A}^{ - } \) are two disjoint, non-empty open sets of \( \left\lbrack {-1,1}\right\rbrack \), we cannot have \( {A}^{ + } \cup {A}^{ - } = \left\lbrack {-1,1}\right\rbrack \). There therefore exists \( {y}_{0} \in \left\lbrack {-1,1}\right\rbrack \) such that \( {y}_{0} \notin {A}^{ + } \cup {A}^{ - } \). We then see that the function \( \varphi = \Phi \left( {{y}_{0},\text{ . }}\right) \) satisfies \( \left| {\varphi \left( t\right) }\right| \leq 1 \) for all \( t \in {\mathbb{R}}^{ + } \). If \( \left| {\varphi \left( {t}_{0}\right) }\right| = 1 \) for some \( {t}_{0} \geq 0 \), for example \( \varphi \left( {t}_{0}\right) = 1 \), the fact that \( {\varphi }^{\prime }\left( {t}_{0}\right) = f\left( {{t}_{0},1}\right) > 0 \) shows that on a neighborhood to the right of \( {t}_{0},\varphi \left( t\right) > 1 \), then \( {y}_{0} \in {A}^{ + } \), which is absurd. Finally, \( \varphi \) is a solution of \( \left( E\right) \) on \( \mathbb{R} \) which satisfies \( \left| {\varphi \left( t\right) }\right| < 1 \) for all \( t \in {\mathbb{R}}^{ + } \).

EXERCICE 3. Soit \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{1} \) et globalement lipschitzienne en la seconde variable. On suppose

> EXERCISE 3. Let \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) be a \( {\mathcal{C}}^{1} \) class function that is globally Lipschitz in the second variable. We assume

\[
\exists T > 0,\forall \left( {t, y}\right)  \in  {\mathbb{R}}^{2},\;f\left( {t + T, y}\right)  = f\left( {t, y}\right) .
\]

On suppose également que \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \) admet une solution définie sur \( \mathbb{R} \) et bornée sur \( \mathbb{R} \) . Montrer que \( \left( E\right) \) admet une solution définie sur \( \mathbb{R} \) et \( T \) -périodique (on pourra utiliser le résultat de l'exercice 1).

> We also assume that \( \left( E\right) : {y}^{\prime } = f\left( {t, y}\right) \) admits a solution defined on \( \mathbb{R} \) and bounded on \( \mathbb{R} \). Show that \( \left( E\right) \) admits a solution defined on \( \mathbb{R} \) and \( T \)-periodic (one may use the result of exercise 1).

Solution. Les hypothèses de l'énoncé de l'exercice 1 sont satisfaites, donc les solutions maximales de \( \left( E\right) \) sont définies sur \( \mathbb{R} \) . De plus, si on note \( t \mapsto \Phi \left( {y, t}\right) \) la solution maximale de \( \left( E\right) \) prenant la valeur \( y \) en \( t = 0 \) , la fonction \( \Phi : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) ainsi définie est continue sur \( {\mathbb{R}}^{2} \) .

> Solution. The hypotheses of the statement of exercise 1 are satisfied, so the maximal solutions of \( \left( E\right) \) are defined on \( \mathbb{R} \). Furthermore, if we denote by \( t \mapsto \Phi \left( {y, t}\right) \) the maximal solution of \( \left( E\right) \) taking the value \( y \) at \( t = 0 \), the function \( \Phi : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) thus defined is continuous on \( {\mathbb{R}}^{2} \).

On sait qu’il existe une solution \( \varphi \) de \( \left( E\right) \) bornée sur \( \mathbb{R} \) . Par ailleurs, l’exercice 4 page 377 montre que la suite \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) est monotone. De plus \( \varphi \) est bornée, donc cette suite est bornée, donc elle converge. Notons \( \ell \) sa limite.

> We know that there exists a solution \( \varphi \) of \( \left( E\right) \) bounded on \( \mathbb{R} \). Furthermore, exercise 4 on page 377 shows that the sequence \( {\left( \varphi \left( kT\right) \right) }_{k \in \mathbb{N}} \) is monotonic. Moreover, \( \varphi \) is bounded, so this sequence is bounded, and therefore it converges. Let \( \ell \) be its limit.

Remarquons maintenant que pour tout \( k \in \mathbb{N} \) , on a \( \Phi \left( {\varphi \left( {kT}\right) , t}\right) = \varphi \left( {{kT} + t}\right) \) pour tout \( t \in \mathbb{R} \) (en effet, ces fonctions de \( t \) sont solutions de \( \left( E\right) \) et prennent la même valeur en 0 ). Fixons alors \( t \in \mathbb{R} \) . Pour tout \( k \in \mathbb{N} \) , on a

> Let us now note that for all \( k \in \mathbb{N} \), we have \( \Phi \left( {\varphi \left( {kT}\right) , t}\right) = \varphi \left( {{kT} + t}\right) \) for all \( t \in \mathbb{R} \) (indeed, these functions of \( t \) are solutions to \( \left( E\right) \) and take the same value at 0). Let us then fix \( t \in \mathbb{R} \). For all \( k \in \mathbb{N} \), we have

\[
\Phi \left( {\varphi \left( {kT}\right) , t + T}\right)  = \varphi \left\lbrack  {\left( {k + 1}\right) T + t}\right\rbrack   = \Phi \left( {\varphi \left\lbrack  {\left( {k + 1}\right) T}\right\rbrack  , t}\right) ,
\]

donc en faisant tendre \( k \) vers \( + \infty \) , on obtient, \( \Phi \) étant continue \( \Phi \left( {\ell , t + T}\right) = \Phi \left( {\ell , t}\right) \) . Ceci est vrai indépendamment de \( t \in \mathbb{R} \) . Finalement, la fonction \( \psi = \Phi \left( {\ell ,\text{ . }}\right) {estunesolutionT} \) -périodique de \( \left( E\right) \) sur \( \mathbb{R} \) .

> therefore, by letting \( k \) tend towards \( + \infty \), we obtain, \( \Phi \) being continuous \( \Phi \left( {\ell , t + T}\right) = \Phi \left( {\ell , t}\right) \). This is true independently of \( t \in \mathbb{R} \). Finally, the function \( \psi = \Phi \left( {\ell ,\text{ . }}\right) {estunesolutionT} \)-periodic of \( \left( E\right) \) on \( \mathbb{R} \).

EXERCICE 4. Si \( M = \left( {m}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , on note \( M \geq 0 \) si pour tout \( \left( {i, j}\right) ,{m}_{i, j} \geq 0 \) . Si \( Y = \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in {\mathbb{R}}^{n} \) , on note \( Y \geq 0 \) si \( {y}_{i} \geq 0 \) pour tout \( i \) , et on note \( Y > 0 \) si \( {y}_{i} > 0 \) pour tout \( i \) .

> EXERCISE 4. If \( M = \left( {m}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), we denote \( M \geq 0 \) if for all \( \left( {i, j}\right) ,{m}_{i, j} \geq 0 \). If \( Y = \left( {{y}_{1},\ldots ,{y}_{n}}\right) \in {\mathbb{R}}^{n} \), we denote \( Y \geq 0 \) if \( {y}_{i} \geq 0 \) for all \( i \), and we denote \( Y > 0 \) if \( {y}_{i} > 0 \) for all \( i \).

Soit \( A : {\mathbb{R}}^{ + } \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une fonction continue vérifiant \( A\left( t\right) \geq 0 \) pour tout \( t \in {\mathbb{R}}^{ + } \) .

> Let \( A : {\mathbb{R}}^{ + } \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a continuous function satisfying \( A\left( t\right) \geq 0 \) for all \( t \in {\mathbb{R}}^{ + } \).

a) Soit \( Y : {\mathbb{R}}^{ + } \rightarrow {\mathbb{R}}^{n} \) une solution de \( {Y}^{\prime } = A\left( t\right) Y \) vérifiant \( Y\left( 0\right) > 0 \) . Montrer que pour tout \( t \in {\mathbb{R}}^{ + }, Y\left( t\right) > 0 \) .

> a) Let \( Y : {\mathbb{R}}^{ + } \rightarrow {\mathbb{R}}^{n} \) be a solution to \( {Y}^{\prime } = A\left( t\right) Y \) satisfying \( Y\left( 0\right) > 0 \). Show that for all \( t \in {\mathbb{R}}^{ + }, Y\left( t\right) > 0 \).

b) Montrer qu’il existe une solution \( Y \) de \( \left( L\right) : {Y}^{\prime } = - A\left( t\right) Y \) , non nulle, telle que \( Y\left( t\right) \geq 0 \) pour tout \( t \in {\mathbb{R}}^{ + } \) .

> b) Show that there exists a non-zero solution \( Y \) to \( \left( L\right) : {Y}^{\prime } = - A\left( t\right) Y \) such that \( Y\left( t\right) \geq 0 \) for all \( t \in {\mathbb{R}}^{ + } \).

Solution. a) Notons \( \left( {y}_{i}\right) \) les composantes de \( Y \) et \( \left( {a}_{i, j}\right) \) celles de \( A \) et supposons le résultat faux. Alors \( c = \inf \left\{ {t \in {\mathbb{R}}^{ + }\mid \exists i,{y}_{i}\left( t\right) = 0}\right\} \) existe. Comme \( Y \) est continue, il existe \( i \) tel que \( {y}_{i}\left( c\right) = 0 \) , et par ailleurs, \( Y\left( t\right) \geq 0 \) pour tout \( t \in \left\lbrack {0, c}\right\rbrack \) . On a donc \( {y}_{i}^{\prime }\left( t\right) = \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}\left( t\right) {y}_{j}\left( t\right) \geq 0 \) pour tout \( t \in \left\lbrack {0, c}\right\rbrack \) , donc \( {y}_{i} \) est croissante sur \( \left\lbrack {0, c}\right\rbrack \) , donc \( {y}_{i}\left( c\right) \geq {y}_{i}\left( 0\right) > 0 \) , ce qui est absurde.

> Solution. a) Let \( \left( {y}_{i}\right) \) be the components of \( Y \) and \( \left( {a}_{i, j}\right) \) those of \( A \) and assume the result is false. Then \( c = \inf \left\{ {t \in {\mathbb{R}}^{ + }\mid \exists i,{y}_{i}\left( t\right) = 0}\right\} \) exists. Since \( Y \) is continuous, there exists \( i \) such that \( {y}_{i}\left( c\right) = 0 \) , and furthermore, \( Y\left( t\right) \geq 0 \) for all \( t \in \left\lbrack {0, c}\right\rbrack \) . We therefore have \( {y}_{i}^{\prime }\left( t\right) = \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{i, j}\left( t\right) {y}_{j}\left( t\right) \geq 0 \) for all \( t \in \left\lbrack {0, c}\right\rbrack \) , so \( {y}_{i} \) is increasing on \( \left\lbrack {0, c}\right\rbrack \) , thus \( {y}_{i}\left( c\right) \geq {y}_{i}\left( 0\right) > 0 \) , which is absurd.

b) Donnons l’idée. Lorsque \( p \) est grand, et si \( X \) vérifie \( {X}^{\prime } = A\left( t\right) X \) avec \( X\left( 0\right) \geq 0 \) , alors \( Y : t \mapsto X\left( {p - t}\right) \) est solution de \( \left( L\right) \) . Comme \( X\left( t\right) \geq 0 \) sur \( \left\lbrack {0, p}\right\rbrack \) , on a \( Y\left( t\right) \geq 0 \) sur \( \left\lbrack {0, p}\right\rbrack \) . Ensuite, notre but sera de faire tendre \( p \) vers \( + \infty \) et d’en tirer parti.

> b) Let us provide the idea. When \( p \) is large, and if \( X \) satisfies \( {X}^{\prime } = A\left( t\right) X \) with \( X\left( 0\right) \geq 0 \) , then \( Y : t \mapsto X\left( {p - t}\right) \) is a solution to \( \left( L\right) \) . Since \( X\left( t\right) \geq 0 \) on \( \left\lbrack {0, p}\right\rbrack \) , we have \( Y\left( t\right) \geq 0 \) on \( \left\lbrack {0, p}\right\rbrack \) . Then, our goal will be to let \( p \) tend towards \( + \infty \) and take advantage of it.

Soit \( R\left( {t, s}\right) \) la résolvante de \( \left( L\right) \) (voir la définition 1 page 403), de sorte que pour tout \( s \in {\mathbb{R}}^{ + } \) fixé, \( \frac{dR}{dt}\left( {t, s}\right) = - A\left( t\right) R\left( {t, s}\right) \) et \( R\left( {s, s}\right) = {I}_{n} \) .

> Let \( R\left( {t, s}\right) \) be the resolvent of \( \left( L\right) \) (see definition 1 on page 403), such that for any fixed \( s \in {\mathbb{R}}^{ + } \) , \( \frac{dR}{dt}\left( {t, s}\right) = - A\left( t\right) R\left( {t, s}\right) \) and \( R\left( {s, s}\right) = {I}_{n} \) .

Notons \( E \) le vecteur de \( {\mathbb{R}}^{n} \) dont toutes les composantes sont égales à1, et pour tout \( p \in \mathbb{N} \) , notons \( {C}_{p} = R\left( {0, p}\right) E \) . Pour tout \( p \in \mathbb{N} \) , nous notons \( {Y}_{p}\left( t\right) = R\left( {t,0}\right) {C}_{p} = R\left( {t, p}\right) E \) . On a \( {Y}_{p}\left( t\right) \geq 0 \) pour tout \( t \in \left\lbrack {0, p}\right\rbrack \) . En effet. Considérons l’application \( \varphi : \left\lbrack {0, p}\right\rbrack \rightarrow {\mathbb{R}}^{n}\;t \mapsto \; R\left( {p - t, t}\right) E = {Y}_{p}\left( {p - t}\right) \) . On a

> Let \( E \) be the vector of \( {\mathbb{R}}^{n} \) whose components are all equal to 1, and for any \( p \in \mathbb{N} \) , let us denote \( {C}_{p} = R\left( {0, p}\right) E \) . For any \( p \in \mathbb{N} \) , we denote \( {Y}_{p}\left( t\right) = R\left( {t,0}\right) {C}_{p} = R\left( {t, p}\right) E \) . We have \( {Y}_{p}\left( t\right) \geq 0 \) for all \( t \in \left\lbrack {0, p}\right\rbrack \) . Indeed. Consider the mapping \( \varphi : \left\lbrack {0, p}\right\rbrack \rightarrow {\mathbb{R}}^{n}\;t \mapsto \; R\left( {p - t, t}\right) E = {Y}_{p}\left( {p - t}\right) \) . We have

\[
\forall t \in  \left\lbrack  {0, p}\right\rbrack  ,\;\frac{d\varphi }{dt}\left( t\right)  =  - \frac{dR}{dt}\left( {p - t, p}\right) E = A\left( {p - t}\right) R\left( {p - t, p}\right) E = A\left( {p - t}\right) \varphi \left( t\right) ,
\]

et comme \( \varphi \left( 0\right) = E > 0 \) , on en déduit d’après la question précédente que \( \varphi \left( t\right) \geq 0 \) pour tout \( t \in \left\lbrack {0, p}\right\rbrack \) , c’est-à-dire \( {Y}_{p}\left( t\right) \geq 0 \) pour tout \( t \in \left\lbrack {0, p}\right\rbrack \) .

> and since \( \varphi \left( 0\right) = E > 0 \) , we deduce from the previous question that \( \varphi \left( t\right) \geq 0 \) for all \( t \in \left\lbrack {0, p}\right\rbrack \) , that is to say \( {Y}_{p}\left( t\right) \geq 0 \) for all \( t \in \left\lbrack {0, p}\right\rbrack \) .

Pour tout \( p \in \mathbb{N} \) , on note ensuite \( {A}_{p} = {C}_{p}/\begin{Vmatrix}{C}_{p}\end{Vmatrix} \) . La suite \( \left( {A}_{p}\right) \) est à valeurs dans la sphère unité de \( {\mathbb{R}}^{n} \) qui est compacte, on peut donc en extraire une sous-suite convergente \( \left( {A}_{\varphi \left( p\right) }\right) \) . Notons \( A \) sa limite. Posons \( Y\left( t\right) = R\left( {t,0}\right) A = \mathop{\lim }\limits_{{p \rightarrow + \infty }}R\left( {t,0}\right) {A}_{\varphi \left( p\right) } \) . Alors \( Y \) est solution de (L) et on a

> For all \( p \in \mathbb{N} \) , we then denote \( {A}_{p} = {C}_{p}/\begin{Vmatrix}{C}_{p}\end{Vmatrix} \) . The sequence \( \left( {A}_{p}\right) \) takes values in the unit sphere of \( {\mathbb{R}}^{n} \) which is compact, so we can extract a convergent subsequence \( \left( {A}_{\varphi \left( p\right) }\right) \) . Let \( A \) be its limit. Let \( Y\left( t\right) = R\left( {t,0}\right) A = \mathop{\lim }\limits_{{p \rightarrow + \infty }}R\left( {t,0}\right) {A}_{\varphi \left( p\right) } \) . Then \( Y \) is a solution to (L) and we have

\[
\forall p \in  \mathbb{N},\;R\left( {t,0}\right) {A}_{\varphi \left( p\right) } = \frac{1}{\begin{Vmatrix}{C}_{\varphi \left( p\right) }\end{Vmatrix}}{Y}_{\varphi \left( p\right) }\left( t\right) ,
\]

donc \( R\left( {t,0}\right) {A}_{\varphi \left( p\right) } \geq 0 \) pour \( \varphi \left( p\right) > t \) . En passant à la limite lorsque \( p \rightarrow + \infty \) (avec \( t \) fixé), on en déduit \( Y\left( t\right) \geq 0 \) , et ceci pour tout \( t \in {\mathbb{R}}^{ + } \) , d’où le résultat.

> therefore \( R\left( {t,0}\right) {A}_{\varphi \left( p\right) } \geq 0 \) for \( \varphi \left( p\right) > t \) . By passing to the limit as \( p \rightarrow + \infty \) (with \( t \) fixed), we deduce \( Y\left( t\right) \geq 0 \) , and this for all \( t \in {\mathbb{R}}^{ + } \) , hence the result.
