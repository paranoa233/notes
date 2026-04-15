#### 2.1. Generalities

*Français : 2.1. Généralités*

Définition 1. Soit \( p \in {\mathbb{N}}^{ * } \) . Toute équation différentielle sur \( {\mathbb{K}}^{n} \) d’ordre \( p \) du type

> Definition 1. Let \( p \in {\mathbb{N}}^{ * } \). Any differential equation on \( {\mathbb{K}}^{n} \) of order \( p \) of the type

\[
{Y}^{\left( p\right) } = {A}_{p - 1}\left( t\right) {Y}^{\left( p - 1\right) } + \cdots  + {A}_{0}\left( t\right) Y + B\left( t\right) , \tag{L}
\]

où \( {A}_{p - 1},\ldots ,{A}_{0} \) sont des fonctions continues de \( I \) dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) et \( B : I \rightarrow {\mathbb{K}}^{n} \) une fonction continue quelconque, est appelée équation différentielle linéaire d'ordre p.

> where \( {A}_{p - 1},\ldots ,{A}_{0} \) are continuous functions from \( I \) to \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) and \( B : I \rightarrow {\mathbb{K}}^{n} \) is any continuous function, is called a linear differential equation of order p.

Lorsque la fonction \( B \) est identiquement nulle sur \( I \) , l’équation différentielle linéaire (L) est dite homogène.

> When the function \( B \) is identically zero on \( I \), the linear differential equation (L) is said to be homogeneous.

Comme on l'a vu dans la partie précédente, on peut ramener toute équation différen-tielle d’ordre \( p \) à une équation différentielle d’ordre 1. Ici, l’équation différentielle linéaire (L) peut aussi s'écrire

> As seen in the previous section, any differential equation of order \( p \) can be reduced to a first-order differential equation. Here, the linear differential equation (L) can also be written

\[
\frac{d}{dt}\left( \begin{matrix} Y \\  {Y}^{\prime } \\  \vdots \\  {Y}^{\left( p - 1\right) } \end{matrix}\right)  = \left( \begin{matrix} 0 & {I}_{n} & & 0 \\  \vdots &  \ddots  &  \ddots  & \\  0 & \cdots & 0 & {I}_{n} \\  {A}_{0}\left( t\right) & \cdots & \cdots & {A}_{p - 1}\left( t\right)  \end{matrix}\right) \left( \begin{matrix} Y \\  {Y}^{\prime } \\  \vdots \\  {Y}^{\left( p - 1\right) } \end{matrix}\right)  + \left( \begin{matrix} 0 \\  \vdots \\  0 \\  B\left( t\right)  \end{matrix}\right)
\]

(écriture en matrices par blocs). Ainsi, nous avons ramené l'équation différentielle linéaire (L) d'ordre \( p \) à une équation différentielle linéaire d'ordre 1 (l'espace des vecteurs de base passe de \( {\mathbb{K}}^{n} \) à \( {\mathbb{K}}^{np} \) ). Pour cette raison, nous nous limiterons à l’étude des équations différentielles linéaires d'ordre 1.

> (block matrix notation). Thus, we have reduced the linear differential equation (L) of order \( p \) to a first-order linear differential equation (the base vector space goes from \( {\mathbb{K}}^{n} \) to \( {\mathbb{K}}^{np} \)). For this reason, we will limit ourselves to the study of first-order linear differential equations.

Remarque 1. Lorsque l'équation différentielle linéaire porte sur des fonctions à valeurs dans \( {\mathbb{K}}^{n} \) (avec \( n \geq 2 \) ), on parle aussi de système différentiel linéaire. Si \( n = 1 \) , on parle d'équation différentielle linéaire scalaire.

> Remark 1. When the linear differential equation involves functions with values in \( {\mathbb{K}}^{n} \) (with \( n \geq 2 \) ), it is also called a linear differential system. If \( n = 1 \) , it is called a scalar linear differential equation.

Solutions des équations différentielles linéaires. Les solutions maximales des équations différentielles linéaires ont la propriété d'être définies sur tout l'intervalle \( I \) où les fonctions de l'équation sont définies. Plus précisément, on a le résultat suivant, dont une preuve est donnée au corollaire 1 page 400.

> Solutions to linear differential equations. The maximal solutions of linear differential equations have the property of being defined on the entire interval \( I \) where the functions of the equation are defined. More precisely, we have the following result, a proof of which is given in corollary 1 on page 400.

THÉORÉME 1. Soit une équation différentielle linéaire

> THEOREM 1. Let a linear differential equation be

\[
{Y}^{\prime } = A\left( t\right) Y + B\left( t\right)
\]

\( \left( {L}_{1}\right) \)

> où \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) et \( B : I \rightarrow {\mathbb{K}}^{n} \) sont des fonctions continues. Alors pour tout \( {t}_{0} \in I \) et pour tout \( {X}_{0} \in {\mathbb{K}}^{n} \) , il existe une unique solution \( V \) de \( \left( {L}_{1}\right) \) définie sur \( I \) tout entier, telle que \( V\left( {t}_{0}\right) = {X}_{0} \) .

where \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) and \( B : I \rightarrow {\mathbb{K}}^{n} \) are continuous functions. Then for any \( {t}_{0} \in I \) and for any \( {X}_{0} \in {\mathbb{K}}^{n} \) , there exists a unique solution \( V \) to \( \left( {L}_{1}\right) \) defined on the entire \( I \) , such that \( V\left( {t}_{0}\right) = {X}_{0} \) .

> Remarque 2. La version de ce théorème pour les équations différentielles linéaires d'ordre \( p \) est la suivante : pour tout \( {t}_{0} \in I \) , pour tout \( {X}_{0},\ldots ,{X}_{p - 1} \in {\mathbb{K}}^{n} \) , il existe une unique solution \( \varphi \) de \( \left( L\right) \) définie sur \( I \) tout entier, telle que \( \varphi \left( {t}_{0}\right) = {X}_{0},\ldots ,{\varphi }^{\left( p - 1\right) }\left( {t}_{0}\right) = {X}_{p - 1} \) .

Remark 2. The version of this theorem for linear differential equations of order \( p \) is as follows: for any \( {t}_{0} \in I \) , for any \( {X}_{0},\ldots ,{X}_{p - 1} \in {\mathbb{K}}^{n} \) , there exists a unique solution \( \varphi \) to \( \left( L\right) \) defined on the entire \( I \) , such that \( \varphi \left( {t}_{0}\right) = {X}_{0},\ldots ,{\varphi }^{\left( p - 1\right) }\left( {t}_{0}\right) = {X}_{p - 1} \) .

> \( \rightarrow \) THÉORÉME 2. Soit \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) une fonction continue. L’ensemble \( {\mathcal{S}}_{H} \) des solutions maximales de l'équation différentielle linéaire homogène

\( \rightarrow \) THEOREM 2. Let \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be a continuous function. The set \( {\mathcal{S}}_{H} \) of maximal solutions to the homogeneous linear differential equation

\[
\frac{dY}{dt} = A\left( t\right) Y \tag{H}
\]

est un s.e.v de dimension \( n \) du \( \mathbb{K} \) -espace vectoriel \( {\mathcal{C}}^{1}\left( {I,{\mathbb{K}}^{n}}\right) \) (fonctions \( {\mathcal{C}}^{1} \) de \( I \) dans \( {\mathbb{K}}^{n} \) ). Démonstration. La forme de \( \left( H\right) \) montre que \( {\mathcal{S}}_{H} \) est un s.e.v de \( {\mathcal{C}}^{1}\left( {I,{\mathbb{K}}^{n}}\right) \) . Par ailleurs, pour \( {t}_{0} \in I \) fixé, l’application \( \Phi : {\mathcal{S}}_{H} \rightarrow {\mathbb{K}}^{n}\;V \mapsto V\left( {t}_{0}\right) \) est linéaire. C’est même un isomorphisme d'après le théorème précédent, d'où le résultat.

> is a subspace of dimension \( n \) of the \( \mathbb{K} \) -vector space \( {\mathcal{C}}^{1}\left( {I,{\mathbb{K}}^{n}}\right) \) (functions \( {\mathcal{C}}^{1} \) from \( I \) to \( {\mathbb{K}}^{n} \) ). Proof. The form of \( \left( H\right) \) shows that \( {\mathcal{S}}_{H} \) is a subspace of \( {\mathcal{C}}^{1}\left( {I,{\mathbb{K}}^{n}}\right) \) . Furthermore, for a fixed \( {t}_{0} \in I \) , the mapping \( \Phi : {\mathcal{S}}_{H} \rightarrow {\mathbb{K}}^{n}\;V \mapsto V\left( {t}_{0}\right) \) is linear. It is even an isomorphism according to the previous theorem, hence the result.

Remarque 3. - De ce théorème, on déduit que l'ensemble des solutions de l'équation différentielle \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y + B\left( t\right) \) est un espace affine de dimension \( n \) . En effet, si \( {V}_{0} \) est une solution particulière de \( \left( L\right) \) , les solutions de \( L \) s’écrivent \( V + {V}_{0} \) , où \( V \) décrit les solutions de \( \left( H\right) \) .

> Remark 3. - From this theorem, we deduce that the set of solutions to the differential equation \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y + B\left( t\right) \) is an affine space of dimension \( n \) . Indeed, if \( {V}_{0} \) is a particular solution of \( \left( L\right) \) , the solutions of \( L \) are written as \( V + {V}_{0} \) , where \( V \) describes the solutions of \( \left( H\right) \) .

- La construction effectuée plus haut pour transformer une équation différentielle linéaire d’ordre \( p \) en une équation différentielle linéaire d’ordre 1 montre, avec ce dernier théorème, que les solutions d'une équation différentielle linéaire homogène sur \( {\mathbb{K}}^{n} \) , d’ordre \( p \) , forment un \( \mathbb{K} \) -e.v de dimension \( {np} \) .

> - The construction carried out above to transform a linear differential equation of order \( p \) into a linear differential equation of order 1 shows, with this last theorem, that the solutions of a homogeneous linear differential equation on \( {\mathbb{K}}^{n} \) , of order \( p \) , form a \( \mathbb{K} \) -vector space of dimension \( {np} \) .

Wronskien. On se donne \( \left( H\right) : {Y}^{\prime } = A\left( t\right) Y \) une équation différentielle linéaire ho-mogène d’ordre1sur \( {\mathbb{K}}^{n} \) , où \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est continue.

> Wronskian. Let \( \left( H\right) : {Y}^{\prime } = A\left( t\right) Y \) be a homogeneous linear differential equation of order 1 on \( {\mathbb{K}}^{n} \) , where \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is continuous.

DéFINITION 2. Soient \( {V}_{1},\ldots ,{V}_{n}n \) solutions de \( \left( H\right) \) . On appelle wronskien de \( {V}_{1},\ldots ,{V}_{n} \) l’application wronskien : \( I \rightarrow \mathbb{K}\;t \mapsto \det \left( {{V}_{1}\left( t\right) ,\ldots ,{V}_{n}\left( t\right) }\right) \) .

> DEFINITION 2. Let \( {V}_{1},\ldots ,{V}_{n}n \) be solutions of \( \left( H\right) \) . We call the Wronskian of \( {V}_{1},\ldots ,{V}_{n} \) the Wronskian mapping: \( I \rightarrow \mathbb{K}\;t \mapsto \det \left( {{V}_{1}\left( t\right) ,\ldots ,{V}_{n}\left( t\right) }\right) \) .

Remarque 4. Considérons une équation différentielle linéaire homogène scalaire d'ordre \( p \)

> Remark 4. Consider a scalar homogeneous linear differential equation of order \( p \)

\[
{y}^{\left( p\right) } = {a}_{p - 1}\left( t\right) {y}^{\left( p - 1\right) } + \cdots  + {a}_{0}\left( t\right) y
\]

\( \left( {H}_{p}\right) \)

> (où les \( {a}_{i} \) sont des fonctions de \( I \) dans \( \mathbb{K} \) ). Nous avons vu plus haut comment transformer \( \left( {H}_{p}\right) \) en une équation différentielle \( \left( {H}_{1}\right) \) d’ordre 1 sur \( {\mathbb{K}}^{p} \) , et il résulte de la construction que \( v \) est une solution de \( \left( {H}_{p}\right) \) si et seulement si \( \left( \begin{matrix} v \\ \vdots \\ {v}^{\left( p - 1\right) } \end{matrix}\right) \) est solution de \( \left( {H}_{1}\right) \) . On appelle

(where the \( {a}_{i} \) are functions from \( I \) to \( \mathbb{K} \) ). We have seen above how to transform \( \left( {H}_{p}\right) \) into a differential equation \( \left( {H}_{1}\right) \) of order 1 on \( {\mathbb{K}}^{p} \) , and it follows from the construction that \( v \) is a solution of \( \left( {H}_{p}\right) \) if and only if \( \left( \begin{matrix} v \\ \vdots \\ {v}^{\left( p - 1\right) } \end{matrix}\right) \) is a solution of \( \left( {H}_{1}\right) \) . We call

> wronskien de \( p \) solutions \( {v}_{1},\ldots ,{v}_{p} \) de \( \left( {H}_{p}\right) \) le wronskien de l’équation différentielle \( \left( {H}_{1}\right) \) des solutions \( \left( \begin{matrix} {v}_{i} \\ \vdots \\ {v}_{i}^{\left( p - 1\right) } \end{matrix}\right) \left( {1 \leq i \leq p}\right) \) de \( \left( {H}_{1}\right) \) , en d’autres termes

Wronskian of \( p \) solutions \( {v}_{1},\ldots ,{v}_{p} \) of \( \left( {H}_{p}\right) \) the Wronskian of the differential equation \( \left( {H}_{1}\right) \) of the solutions \( \left( \begin{matrix} {v}_{i} \\ \vdots \\ {v}_{i}^{\left( p - 1\right) } \end{matrix}\right) \left( {1 \leq i \leq p}\right) \) of \( \left( {H}_{1}\right) \) , in other words

\[
\operatorname{wronskien}\left( {{v}_{1},\ldots ,{v}_{p}}\right) \left( t\right)  = \left| \begin{matrix} {v}_{1}\left( t\right) & {v}_{2}\left( t\right) & \cdots & {v}_{p}\left( t\right) \\  \vdots & \vdots & & \vdots \\  {v}_{1}^{\left( p - 1\right) }\left( t\right) & {v}_{2}^{\left( p - 1\right) }\left( t\right) & \cdots & {v}_{p}^{\left( p - 1\right) }\left( t\right)  \end{matrix}\right| .
\]

Par exemple, le wronskien de deux solutions \( u \) et \( v \) d’une équation différentielle linéaire homogène d’ordre \( 2 : {y}^{\prime \prime } = p\left( t\right) {y}^{\prime } + q\left( t\right) y \) est \( \left| \begin{matrix} u & v \\ {u}^{\prime } & {v}^{\prime } \end{matrix}\right| = u{v}^{\prime } - {u}^{\prime }v \) .

> For example, the Wronskian of two solutions \( u \) and \( v \) of a homogeneous linear differential equation of order \( 2 : {y}^{\prime \prime } = p\left( t\right) {y}^{\prime } + q\left( t\right) y \) is \( \left| \begin{matrix} u & v \\ {u}^{\prime } & {v}^{\prime } \end{matrix}\right| = u{v}^{\prime } - {u}^{\prime }v \) .

Nous verrons dans l'exercice 7 page 388 un moyen pratique de calculer le wronskien.

> We will see in exercise 7 on page 388 a practical way to calculate the Wronskian.

Proposition 1. Soient \( {V}_{1},\ldots ,{V}_{n} \) des solutions de \( \left( H\right) \) . Le rang des vecteurs \( {V}_{1}\left( t\right) ,\ldots \) , \( {V}_{n}\left( t\right) \) est indépendant de \( t \in I \) .

> Proposition 1. Let \( {V}_{1},\ldots ,{V}_{n} \) be solutions of \( \left( H\right) \) . The rank of the vectors \( {V}_{1}\left( t\right) ,\ldots \) , \( {V}_{n}\left( t\right) \) is independent of \( t \in I \) .

Démonstration. C’est une conséquence immédiate de l’isomorphisme \( \Phi : {\mathcal{S}}_{H} \rightarrow {\mathbb{K}}^{n}\;V \mapsto V\left( {t}_{0}\right) \) (où \( {t}_{0} \in I \) est fixé) - voir la preuve du théorème 2.

> Proof. This is an immediate consequence of the isomorphism \( \Phi : {\mathcal{S}}_{H} \rightarrow {\mathbb{K}}^{n}\;V \mapsto V\left( {t}_{0}\right) \) (where \( {t}_{0} \in I \) is fixed) - see the proof of theorem 2.

COROLLAIRE 1. Des solutions \( {V}_{1},\ldots ,{V}_{n} \) de \( \left( H\right) \) forment une base des solutions de \( \left( H\right) \) si et seulement s’il existe \( {t}_{0} \in I \) tel que wronskien \( \left( {{V}_{1},\ldots ,{V}_{n}}\right) \left( {t}_{0}\right) \neq 0 \) , et dans ce cas on a wronskien \( \left( {{V}_{1},\ldots ,{V}_{n}}\right) \left( t\right) \neq 0 \) pour tout \( t \in I \) .

> COROLLARY 1. Solutions \( {V}_{1},\ldots ,{V}_{n} \) of \( \left( H\right) \) form a basis of the solutions of \( \left( H\right) \) if and only if there exists \( {t}_{0} \in I \) such that Wronskian \( \left( {{V}_{1},\ldots ,{V}_{n}}\right) \left( {t}_{0}\right) \neq 0 \) , and in this case we have Wronskian \( \left( {{V}_{1},\ldots ,{V}_{n}}\right) \left( t\right) \neq 0 \) for all \( t \in I \) .

Résolution de l'équation différentielle linéaire d'ordre 1 sur \( \mathbb{K} \) . Il est facile de résoudre l’équation différentielle linéaire homogène \( \left( H\right) : {y}^{\prime } = a\left( t\right) y \) , où \( a : I \rightarrow \mathbb{K} \) est continue. Les solutions (dont on sait d'après le théorème 2 qu'elles forment un \( \mathbb{K} \) -e.v de dimension 1) sont toutes proportionnelles à \( t \mapsto {e}^{\psi \left( t\right) } \) , où \( \psi \) est une primitive de \( a \) sur l’intervalle \( I \) .

> Solving the first-order linear differential equation on \( \mathbb{K} \) . It is easy to solve the homogeneous linear differential equation \( \left( H\right) : {y}^{\prime } = a\left( t\right) y \) , where \( a : I \rightarrow \mathbb{K} \) is continuous. The solutions (which we know from theorem 2 form a \( \mathbb{K} \) -vector space of dimension 1) are all proportional to \( t \mapsto {e}^{\psi \left( t\right) } \) , where \( \psi \) is an antiderivative of \( a \) on the interval \( I \) .

Pour résoudre ensuite l’équation différentielle linéaire inhomogène \( \left( L\right) : {y}^{\prime } = a\left( t\right) y + \; b\left( t\right) \) , où \( b : I \rightarrow \mathbb{K} \) est continue, on applique la méthode de variation de la constante. On recherche les solutions sous la forme \( t \mapsto \lambda \left( t\right) {e}^{\psi \left( t\right) } \) où \( \lambda : I \rightarrow \mathbb{K} \) est une fonction de classe \( {\mathcal{C}}^{1} \) encore inconnue. Par dérivation, on voit que notre fonction est solution si et seulement si \( {\lambda }^{\prime }\left( t\right) {e}^{\psi \left( t\right) } = b\left( t\right) \) pour tout \( t \in \mathbb{R} \) , ce qui équivaut à dire que \( \lambda \) est une primitive de \( {e}^{-\psi \left( t\right) }b\left( t\right) \) sur \( I \) (voir des calculs pratiques dans l’exercice 1). Rappelons que la solution générale de \( \left( L\right) \) est la somme de la solution générale de \( \left( H\right) \) et d’une solution particulière de \( \left( L\right) \) .

> To then solve the inhomogeneous linear differential equation \( \left( L\right) : {y}^{\prime } = a\left( t\right) y + \; b\left( t\right) \), where \( b : I \rightarrow \mathbb{K} \) is continuous, we apply the method of variation of constants. We look for solutions in the form \( t \mapsto \lambda \left( t\right) {e}^{\psi \left( t\right) } \) where \( \lambda : I \rightarrow \mathbb{K} \) is a function of class \( {\mathcal{C}}^{1} \) that is still unknown. By differentiation, we see that our function is a solution if and only if \( {\lambda }^{\prime }\left( t\right) {e}^{\psi \left( t\right) } = b\left( t\right) \) for all \( t \in \mathbb{R} \), which is equivalent to saying that \( \lambda \) is an antiderivative of \( {e}^{-\psi \left( t\right) }b\left( t\right) \) on \( I \) (see practical calculations in exercise 1). Recall that the general solution of \( \left( L\right) \) is the sum of the general solution of \( \left( H\right) \) and a particular solution of \( \left( L\right) \).

Résolution d'un système linéaire d'ordre 1. Dans le cas général, il n'existe pas de méthode pratique pour résoudre un système différentiel homogène \( \left( H\right) : {Y}^{\prime } = A\left( t\right) Y \) lorsqu’on est en dimension \( n \geq 2 \) . Cependant, si on connaît \( n \) solutions \( {V}_{1},\ldots ,{V}_{n} \) de \( \left( H\right) \) , linéairement indépendantes, on sait que la solution générale de \( \left( H\right) \) est \( \mathop{\sum }\limits_{i}{\lambda }_{i}{V}_{i} \) où les \( {\lambda }_{i} \in \; \mathbb{K} \) (voir le théorème 2). Connaissant ces solutions, on peut résoudre le système différentiel inhomogène \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y + B\left( t\right) \) par la méthode de variation des constantes.

> Solving a first-order linear system. In the general case, there is no practical method to solve a homogeneous differential system \( \left( H\right) : {Y}^{\prime } = A\left( t\right) Y \) when in dimension \( n \geq 2 \). However, if we know \( n \) solutions \( {V}_{1},\ldots ,{V}_{n} \) of \( \left( H\right) \) that are linearly independent, we know that the general solution of \( \left( H\right) \) is \( \mathop{\sum }\limits_{i}{\lambda }_{i}{V}_{i} \) where the \( {\lambda }_{i} \in \; \mathbb{K} \) (see theorem 2). Knowing these solutions, we can solve the inhomogeneous differential system \( \left( L\right) : {Y}^{\prime } = A\left( t\right) Y + B\left( t\right) \) using the method of variation of constants.

On recherche les solutions de \( \left( L\right) \) sous la forme \( V : t \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( t\right) {V}_{i}\left( t\right) \) où les \( {\lambda }_{i} : I \rightarrow \mathbb{K} \) sont des fonctions \( {\mathcal{C}}^{1} \) . Par dérivation, on obtient que \( V \) est solution de \( \left( L\right) \) si et seulement si

> We look for solutions of \( \left( L\right) \) in the form \( V : t \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( t\right) {V}_{i}\left( t\right) \) where the \( {\lambda }_{i} : I \rightarrow \mathbb{K} \) are \( {\mathcal{C}}^{1} \) functions. By differentiation, we obtain that \( V \) is a solution of \( \left( L\right) \) if and only if

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{\prime }\left( t\right) {V}_{i}\left( t\right)  + \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( t\right) {V}_{i}^{\prime }\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}\left( t\right) A\left( t\right) {V}_{i}\left( t\right)  + B\left( t\right) ,
\]

et comme \( {V}_{i}^{\prime } = A\left( t\right) {V}_{i} \) , ceci s’écrit aussi

> and since \( {V}_{i}^{\prime } = A\left( t\right) {V}_{i} \), this can also be written as

\[
\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}^{\prime }\left( t\right) {V}_{i}\left( t\right)  = B\left( t\right)
\]

Les \( {V}_{i} \) étant indépendants, ceci apparaît comme un système de Cramer dont les inconnues sont les \( {\lambda }_{i}^{\prime }\left( t\right) \) . Par résolution puis intégration, on trouve les \( {\lambda }_{i} \) (voir l’exercice 1 pour des calculs pratiques).

> The \( {V}_{i} \) being independent, this appears as a Cramer system whose unknowns are the \( {\lambda }_{i}^{\prime }\left( t\right) \). By solving and then integrating, we find the \( {\lambda }_{i} \) (see exercise 1 for practical calculations).

Regardons en particulier comment mettre en œuvre cette méthode pour les équations différentielles linéaires d'ordre 2 sur K.

> Let us look in particular at how to implement this method for second-order linear differential equations over K.

Supposons connues deux solutions linéairement indépendantes \( u \) et \( v \) de \( \left( H\right) : {y}^{\prime \prime } = \; a\left( t\right) {y}^{\prime } + b\left( t\right) y \) , et recherchons la solution générale de \( \left( L\right) : {y}^{\prime \prime } = a\left( t\right) {y}^{\prime } + b\left( t\right) y + c\left( t\right) \) . On se ramène d’abord à un système différentiel d’ordre1: en posant \( Y = \left( \begin{matrix} y \\ {y}^{\prime } \end{matrix}\right) \) , les équations différentielles \( \left( H\right) \) et \( \left( L\right) \) deviennent respectivement \( \left( {H}_{1}\right) : {Y}^{\prime } = A\left( t\right) Y \) et \( \left( {L}_{1}\right) : {Y}^{\prime } = A\left( t\right) Y + C\left( t\right) \) où

> Suppose two linearly independent solutions \( u \) and \( v \) of \( \left( H\right) : {y}^{\prime \prime } = \; a\left( t\right) {y}^{\prime } + b\left( t\right) y \) are known, and let us seek the general solution of \( \left( L\right) : {y}^{\prime \prime } = a\left( t\right) {y}^{\prime } + b\left( t\right) y + c\left( t\right) \) . We first reduce this to a first-order differential system: by setting \( Y = \left( \begin{matrix} y \\ {y}^{\prime } \end{matrix}\right) \) , the differential equations \( \left( H\right) \) and \( \left( L\right) \) become respectively \( \left( {H}_{1}\right) : {Y}^{\prime } = A\left( t\right) Y \) and \( \left( {L}_{1}\right) : {Y}^{\prime } = A\left( t\right) Y + C\left( t\right) \) where

\[
A\left( t\right)  = \left( \begin{matrix} 0 & 1 \\  b\left( t\right) & a\left( t\right)  \end{matrix}\right) \;\text{ et }\;C\left( t\right)  = \left( \begin{matrix} 0 \\  c\left( t\right)  \end{matrix}\right) .
\]

Il s’agit donc de trouver les solutions de \( \left( {L}_{1}\right) \) . On pose \( W\left( t\right) = \lambda \left( t\right) U\left( t\right) + \mu \left( t\right) V\left( t\right) \) , où \( U\left( t\right) = \left( \begin{matrix} u\left( t\right) \\ {u}^{\prime }\left( t\right) \end{matrix}\right) \) et \( V\left( t\right) = \left( \begin{matrix} v\left( t\right) \\ {v}^{\prime }\left( t\right) \end{matrix}\right) \) . Comme on l’a vu plus haut, \( W \) est solution de \( \left( {L}_{1}\right) \) si et seulement si \( {\lambda }^{\prime }\left( t\right) U\left( t\right) + {\mu }^{\prime }\left( t\right) V\left( t\right) = C\left( t\right) \) pour tout \( t \in I \) , donc \( t \mapsto \lambda \left( t\right) u\left( t\right) + \mu \left( t\right) v\left( t\right) \) est solution de \( \left( L\right) \) si et seulement si

> The goal is therefore to find the solutions of \( \left( {L}_{1}\right) \) . We set \( W\left( t\right) = \lambda \left( t\right) U\left( t\right) + \mu \left( t\right) V\left( t\right) \) , where \( U\left( t\right) = \left( \begin{matrix} u\left( t\right) \\ {u}^{\prime }\left( t\right) \end{matrix}\right) \) and \( V\left( t\right) = \left( \begin{matrix} v\left( t\right) \\ {v}^{\prime }\left( t\right) \end{matrix}\right) \) . As seen above, \( W \) is a solution of \( \left( {L}_{1}\right) \) if and only if \( {\lambda }^{\prime }\left( t\right) U\left( t\right) + {\mu }^{\prime }\left( t\right) V\left( t\right) = C\left( t\right) \) for all \( t \in I \) , therefore \( t \mapsto \lambda \left( t\right) u\left( t\right) + \mu \left( t\right) v\left( t\right) \) is a solution of \( \left( L\right) \) if and only if

\[
\left\{  \begin{matrix} {\lambda }^{\prime }u + {\mu }^{\prime }v = 0 \\  {\lambda }^{\prime }{u}^{\prime } + {\mu }^{\prime }{v}^{\prime } = c\left( t\right)  \end{matrix}\right.
\]

relations utiles dans les exercices (voir l'exercice 1).

> useful relations in the exercises (see exercise 1).

Abaissement de l'ordre dans une équation différentielle linéaire sur \( \mathbb{K} \) . On considère une équation différentielle de la forme \( \left( L\right) : {y}^{\left( n\right) } = {a}_{n - 1}\left( t\right) {y}^{\left( n - 1\right) } + \cdots + {a}_{1}\left( t\right) {y}^{\prime } + \; {a}_{0}\left( t\right) y \) , où les \( {a}_{i} \) sont des fonctions continues de \( I \) dans \( \mathbb{K} \) . Si l’on connaît une solution \( \varphi \) de \( \left( L\right) \) , il est possible d’abaisser l’ordre de \( \left( L\right) \) en procédant comme suit : on recherche les solutions de \( \left( L\right) \) sous la forme \( f = {g\varphi } \) , où \( g \) est une fonction de classe \( {\mathcal{C}}^{n} \) encore inconnue. En remplaçant dans \( \left( L\right) \) , on voit que \( f \) est solution si et seulement si

> Reduction of order for a linear differential equation over \( \mathbb{K} \) . Consider a differential equation of the form \( \left( L\right) : {y}^{\left( n\right) } = {a}_{n - 1}\left( t\right) {y}^{\left( n - 1\right) } + \cdots + {a}_{1}\left( t\right) {y}^{\prime } + \; {a}_{0}\left( t\right) y \) , where the \( {a}_{i} \) are continuous functions from \( I \) to \( \mathbb{K} \) . If a solution \( \varphi \) of \( \left( L\right) \) is known, it is possible to reduce the order of \( \left( L\right) \) by proceeding as follows: we seek solutions of \( \left( L\right) \) in the form \( f = {g\varphi } \) , where \( g \) is a function of class \( {\mathcal{C}}^{n} \) yet to be determined. Substituting into \( \left( L\right) \) , we see that \( f \) is a solution if and only if

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{C}_{n}^{k}{g}^{\left( k\right) }{\varphi }^{\left( n - k\right) } = {a}_{n - 1}\left( t\right) \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{C}_{n - 1}^{k}{g}^{\left( k\right) }{\varphi }^{\left( n - 1 - k\right) } + \cdots  + {a}_{1}\left( t\right) \left( {g{\varphi }^{\prime } + {g}^{\prime }\varphi }\right)  + {a}_{0}\left( t\right) {g\varphi },
\]

et comme \( \varphi \) est solution de \( \left( L\right) \) , tous les termes contenant \( g \) s’éliminent, ce qui entraîne

> and since \( \varphi \) is a solution of \( \left( L\right) \) , all terms containing \( g \) cancel out, which leads to

\[
\mathop{\sum }\limits_{{k = 1}}^{n}{C}_{n}^{k}{g}^{\left( k\right) }{\varphi }^{\left( n - k\right) } = {a}_{n - 1}\left( t\right) \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}{C}_{n - 1}^{k}{g}^{\left( k\right) }{\varphi }^{\left( n - 1 - k\right) } + \cdots  + {a}_{1}\left( t\right) \left( {{g}^{\prime }\varphi }\right) .
\]

Autrement dit, \( {g}^{\prime } \) est solution d’une équation différentielle d’ordre \( n - 1 \) : nous venons d'abaisser l'ordre de l'équation.

> In other words, \( {g}^{\prime } \) is a solution to a differential equation of order \( n - 1 \): we have just reduced the order of the equation.

Cette technique est particulièrement sympathique dans le cas des équations du second ordre \( \left( {L}_{2}\right) : {y}^{\prime \prime } = a\left( t\right) {y}^{\prime } + b\left( t\right) y \) . Si on connaît une solution \( \varphi , f = {g\varphi } \) sera solution de \( \left( {L}_{2}\right) \) si et seulement si \( \left( {2{g}^{\prime }{\varphi }^{\prime } + {g}^{\prime \prime }\varphi }\right) = a\left( t\right) {g}^{\prime }\varphi \) ,équation linéaire d’ordre 1 en \( {g}^{\prime } \) que l’on sait intégrer, ce qui permet de connaître toutes les solutions de \( \left( {L}_{2}\right) \) .

> This technique is particularly appealing in the case of second-order equations \( \left( {L}_{2}\right) : {y}^{\prime \prime } = a\left( t\right) {y}^{\prime } + b\left( t\right) y \). If we know one solution, \( \varphi , f = {g\varphi } \) will be a solution to \( \left( {L}_{2}\right) \) if and only if \( \left( {2{g}^{\prime }{\varphi }^{\prime } + {g}^{\prime \prime }\varphi }\right) = a\left( t\right) {g}^{\prime }\varphi \), a first-order linear equation in \( {g}^{\prime } \) that we know how to integrate, which allows us to find all solutions to \( \left( {L}_{2}\right) \).
