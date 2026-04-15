#### 3.2. Implicit functions

*Français : 3.2. Fonctions implicites*

Nous commençons par énoncer le théorème des fonctions implicites pour une fonction à variable dans un espace de Banach, avant de passer à la dimension finie. Nous aurons besoin pour cela de la définition qui suit (qui généralise la notion de dérivée partielle).

> We begin by stating the implicit function theorem for a function with a variable in a Banach space, before moving on to the finite-dimensional case. For this, we will need the following definition (which generalizes the notion of partial derivative).

DéFINITION 2. Soient \( {E}_{1},\ldots ,{E}_{n}, F \) des e.v.n et une application \( f : \Omega \subset E = {E}_{1} \times \cdots \times \; {E}_{n} \rightarrow F \) , où \( \Omega \) est un ouvert de \( E \) . Soit \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in \Omega \) . Pour \( 1 \leq i \leq n \) , la fonction \( {f}_{i} : x \mapsto f\left( {{a}_{1},\ldots ,{a}_{i - 1}, x,{a}_{i + 1},\ldots ,{a}_{n}}\right) \) est définie sur un voisinage de \( {a}_{i} \) dans \( {E}_{i} \) . Si elle est différentiable en \( {a}_{i} \) , on dit que \( f \) admet une différentielle partielle d’indice \( i \) , et on appelle différentielle partielle d’indice \( i \) la différentielle \( d{f}_{i,{a}_{i}} \) , notée \( {\partial }_{i}{f}_{\left( {a}_{1},\ldots ,{a}_{n}\right) } \) .

> DEFINITION 2. Let \( {E}_{1},\ldots ,{E}_{n}, F \) be normed vector spaces and \( f : \Omega \subset E = {E}_{1} \times \cdots \times \; {E}_{n} \rightarrow F \) a mapping, where \( \Omega \) is an open subset of \( E \) . Let \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \in \Omega \) . For \( 1 \leq i \leq n \) , the function \( {f}_{i} : x \mapsto f\left( {{a}_{1},\ldots ,{a}_{i - 1}, x,{a}_{i + 1},\ldots ,{a}_{n}}\right) \) is defined on a neighborhood of \( {a}_{i} \) in \( {E}_{i} \) . If it is differentiable at \( {a}_{i} \) , we say that \( f \) admits a partial differential of index \( i \) , and the partial differential of index \( i \) is the differential \( d{f}_{i,{a}_{i}} \) , denoted by \( {\partial }_{i}{f}_{\left( {a}_{1},\ldots ,{a}_{n}\right) } \) .

Remarque 4. - Lorsque \( {E}_{i} = \mathbb{R} \) pour tout \( i, E = {\mathbb{R}}^{n} \) , les différentielles partielles s’expriment en fonction des dérivées partielles par la relation \( {\partial }_{i}{f}_{a}\left( h\right) = h\frac{\partial f}{\partial {x}_{i}}\left( a\right) \) .

> Remark 4. - When \( {E}_{i} = \mathbb{R} \) for all \( i, E = {\mathbb{R}}^{n} \) , the partial differentials are expressed in terms of partial derivatives by the relation \( {\partial }_{i}{f}_{a}\left( h\right) = h\frac{\partial f}{\partial {x}_{i}}\left( a\right) \) .

- Il résulte de la définition de la différentielle que si \( f \) est différentiable en \( a = \; \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , alors \( {\partial }_{i}{f}_{\left( {a}_{1},\ldots ,{a}_{n}\right) } \) existe pour tout \( i \) et de plus

> - It follows from the definition of the differential that if \( f \) is differentiable at \( a = \; \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , then \( {\partial }_{i}{f}_{\left( {a}_{1},\ldots ,{a}_{n}\right) } \) exists for all \( i \) and furthermore

\[
\forall h \in  {E}_{i},\;{\partial }_{i}{f}_{\left( {a}_{1},\ldots ,{a}_{n}\right) }\left( h\right)  = d{f}_{a}\left( {0,\ldots ,0, h,0,\ldots ,0}\right) ,
\]

ce qui entraîne

> which implies

\[
\forall \left( {{h}_{1},\ldots ,{h}_{n}}\right)  \in  {E}_{1} \times  \cdots  \times  {E}_{n},\;d{f}_{a}\left( {{h}_{1},\ldots ,{h}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\partial }_{i}{f}_{a}\left( {h}_{i}\right) .
\]

THÉORÉME 2 (FONCTIONS IMPLICITES). Soient \( E, F, G \) trois espaces de Banach, \( U \) un ouvert de \( E \) et \( V \) un ouvert de \( F \) . Soit \( f : U \times V \rightarrow G\;\left( {x, y}\right) \mapsto f\left( {x, y}\right) \) une application de classe \( {\mathcal{C}}^{1} \) . Supposons que pour \( \left( {a, b}\right) \in U \times V,{\partial }_{2}{f}_{\left( a, b\right) } \) est un isomorphisme bicontinu de \( F \) sur \( G \) . Alors il existe

> THEOREM 2 (IMPLICIT FUNCTIONS). Let \( E, F, G \) be three Banach spaces, \( U \) an open subset of \( E \) and \( V \) an open subset of \( F \) . Let \( f : U \times V \rightarrow G\;\left( {x, y}\right) \mapsto f\left( {x, y}\right) \) be a mapping of class \( {\mathcal{C}}^{1} \) . Suppose that for \( \left( {a, b}\right) \in U \times V,{\partial }_{2}{f}_{\left( a, b\right) } \) is a bicontinuous isomorphism from \( F \) onto \( G \) . Then there exists

- un voisinage ouvert \( {U}^{\prime } \) de a (avec \( {U}^{\prime } \subset  U \) ),

> - an open neighborhood \( {U}^{\prime } \) of a (with \( {U}^{\prime } \subset  U \) ),

- un voisinage ouvert \( W \) de \( f\left( {a, b}\right) \) ,

> - an open neighborhood \( W \) of \( f\left( {a, b}\right) \) ,

- un voisinage ouvert \( \Omega \) de \( \left( {a, b}\right) \) (avec \( \Omega  \subset  U \times  V \) ),

> - an open neighborhood \( \Omega \) of \( \left( {a, b}\right) \) (with \( \Omega  \subset  U \times  V \) ),

- une fonction \( \varphi  : {U}^{\prime } \times  W \rightarrow  V \) de classe \( {\mathcal{C}}^{1} \) ,

> - a function \( \varphi  : {U}^{\prime } \times  W \rightarrow  V \) of class \( {\mathcal{C}}^{1} \) ,

vérifiant

> satisfying

- pour tout \( x \in  {U}^{\prime } \) , pour tout \( z \in  W \) , il existe une unique solution \( y \) de \( f\left( {x, y}\right)  = z \) avec \( \left( {x, y}\right)  \in  \Omega \) , et on a \( y = \varphi \left( {x, z}\right) \) .

> - for all \( x \in  {U}^{\prime } \) , for all \( z \in  W \) , there exists a unique solution \( y \) to \( f\left( {x, y}\right)  = z \) with \( \left( {x, y}\right)  \in  \Omega \) , and we have \( y = \varphi \left( {x, z}\right) \) .

En particulier, \( f\left( {x,\varphi \left( {x, z}\right) }\right) = z \) pour tout \( \left( {x, z}\right) \in {U}^{\prime } \times W \) . Démonstration. Introduisons la fonction

> In particular, \( f\left( {x,\varphi \left( {x, z}\right) }\right) = z \) for all \( \left( {x, z}\right) \in {U}^{\prime } \times W \) . Proof. Let us introduce the function

\[
F : U \times  V \rightarrow  E \times  G\;\left( {x, y}\right)  \mapsto  \left( {x, f\left( {x, y}\right) }\right) .
\]

D’après la règle de composition, \( F \) est de classe \( {\mathcal{C}}^{1} \) et

> According to the chain rule, \( F \) is of class \( {\mathcal{C}}^{1} \) and

\[
d{F}_{\left( a, b\right) }\left( {{h}_{1},{h}_{2}}\right)  = \left( {{h}_{1}, d{f}_{\left( a, b\right) }\left( {{h}_{1},{h}_{2}}\right) }\right)  = \left( {{h}_{1},{\partial }_{1}{f}_{\left( a, b\right) }\left( {h}_{1}\right)  + {\partial }_{2}{f}_{\left( a, b\right) }\left( {h}_{2}\right) }\right) .
\]

Ainsi, \( d{F}_{\left( a, b\right) } \) est un isomorphisme bicontinu de \( E \times F \) sur \( E \times G \) - son isomorphisme inverse est donné par \( \left( {{\ell }_{1},{\ell }_{2}}\right) \mapsto \left( {{\ell }_{1},{\left( {\partial }_{2}{f}_{\left( a, b\right) }\right) }^{-1}\left( {{\ell }_{1} - {\partial }_{1}{f}_{\left( a, b\right) }\left( {\ell }_{2}\right) }\right) }\right) \) . On peut donc appliquer le théorème d’inversion locale, qui entraîne l’existence d’un voisinage ouvert \( \Omega \) de \( \left( {a, b}\right) \) , d’un voisinage ouvert \( \Gamma \) de \( \left( {a, f\left( {a, b}\right) }\right) \) tels que \( F \) soit un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( \Omega \) sur \( \Gamma \) . Quitte à restreindre \( \Gamma \) , on peut même écrire \( \Gamma = {U}^{\prime } \times W \) où \( {U}^{\prime } \) est un voisinage ouvert de \( a \) et \( W \) un voisinage ouvert de \( f\left( {a, b}\right) \) .

> Thus, \( d{F}_{\left( a, b\right) } \) is a bicontinuous isomorphism from \( E \times F \) onto \( E \times G \) - its inverse isomorphism is given by \( \left( {{\ell }_{1},{\ell }_{2}}\right) \mapsto \left( {{\ell }_{1},{\left( {\partial }_{2}{f}_{\left( a, b\right) }\right) }^{-1}\left( {{\ell }_{1} - {\partial }_{1}{f}_{\left( a, b\right) }\left( {\ell }_{2}\right) }\right) }\right) \) . We can therefore apply the local inversion theorem, which implies the existence of an open neighborhood \( \Omega \) of \( \left( {a, b}\right) \) , and an open neighborhood \( \Gamma \) of \( \left( {a, f\left( {a, b}\right) }\right) \) such that \( F \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism from \( \Omega \) onto \( \Gamma \) . By restricting \( \Gamma \) if necessary, we can even write \( \Gamma = {U}^{\prime } \times W \) where \( {U}^{\prime } \) is an open neighborhood of \( a \) and \( W \) is an open neighborhood of \( f\left( {a, b}\right) \) .

Comme \( F\left( {x, y}\right) = \left( {x, f\left( {x, y}\right) }\right) \) , le difféomorphisme inverse \( {F}^{-1} : \Gamma = {U}^{\prime } \times W \rightarrow \Omega \) s’écrit sous la forme \( {F}^{-1}\left( {x, z}\right) = \left( {x,\varphi \left( {x, z}\right) }\right) \) où \( \varphi \) est de classe \( {\mathcal{C}}^{1} \) . On en déduit que pour tout \( \left( {x, z}\right) \in \; {U}^{\prime } \times W = \Gamma \) , il existe un unique \( y \) tel que \( \left( {x, y}\right) \in \Omega \) et \( f\left( {x, y}\right) = z \) , et de plus \( y = \varphi \left( {x, z}\right) \) . D’où le théorème.

> Since \( F\left( {x, y}\right) = \left( {x, f\left( {x, y}\right) }\right) \) , the inverse diffeomorphism \( {F}^{-1} : \Gamma = {U}^{\prime } \times W \rightarrow \Omega \) is written in the form \( {F}^{-1}\left( {x, z}\right) = \left( {x,\varphi \left( {x, z}\right) }\right) \) where \( \varphi \) is of class \( {\mathcal{C}}^{1} \) . We deduce that for all \( \left( {x, z}\right) \in \; {U}^{\prime } \times W = \Gamma \) , there exists a unique \( y \) such that \( \left( {x, y}\right) \in \Omega \) and \( f\left( {x, y}\right) = z \) , and furthermore \( y = \varphi \left( {x, z}\right) \) . Hence the theorem.

Remarque 5. - Le théorème que nous venons d'énoncer peut sembler obscur. Es-sayons de l’éclaircir : deux points \( x \) et \( z \) étant donnés, on recherche \( y \) tel que \( f\left( {x, y}\right) = z \) . A condition de prendre \( y \) proche de \( b \) (exprimé par la condition \( \left( {x, y}\right) \in \Omega ), y \) existe et est unique, et on peut écrire \( y = \varphi \left( {x, z}\right) \) où \( \varphi \) est de classe \( {\mathcal{C}}^{1} \) .

> Remark 5. - The theorem we have just stated may seem obscure. Let us try to clarify it: given two points \( x \) and \( z \) , we look for \( y \) such that \( f\left( {x, y}\right) = z \) . Provided we take \( y \) close to \( b \) (expressed by the condition \( \left( {x, y}\right) \in \Omega ), y \) exists and is unique, and we can write \( y = \varphi \left( {x, z}\right) \) where \( \varphi \) is of class \( {\mathcal{C}}^{1} \) .

- On peut calculer la différentielle de \( \varphi \) en différentiant la relation \( f\left( {x,\varphi \left( {x, z}\right) }\right)  = z \) . Après calculs, on trouve

> - We can calculate the differential of \( \varphi \) by differentiating the relation \( f\left( {x,\varphi \left( {x, z}\right) }\right)  = z \) . After calculation, we find

\[
d{\varphi }_{\left( x, z\right) }\left( {{h}_{1},{h}_{2}}\right)  = {\partial }_{2}{f}_{\left( x,\varphi \left( x, z\right) \right) }{)}^{-1}\left( {{h}_{1} - {\partial }_{1}{f}_{\left( x,\varphi \left( x, z\right) \right) }\left( {h}_{2}\right) }\right) .
\]

Remarque 6. On utilise souvent le théorème des fonctions implicites lorsque \( z \) est fixé, menant ainsi au corollaire suivant :

> Remark 6. The implicit function theorem is often used when \( z \) is fixed, leading to the following corollary:

Sous les hypothèses du théorème, si \( c = f\left( {a, b}\right) \) , alors il existe un voisinage ouvert \( {U}^{\prime } \) de \( a \) , un voisinage ouvert \( \Omega \) de \( \left( {a, b}\right) \) et une fonction \( \psi : {U}^{\prime } \rightarrow V \) de classe \( {\mathcal{C}}^{1} \) vérifiant

> Under the hypotheses of the theorem, if \( c = f\left( {a, b}\right) \) , then there exists an open neighborhood \( {U}^{\prime } \) of \( a \) , an open neighborhood \( \Omega \) of \( \left( {a, b}\right) \) and a function \( \psi : {U}^{\prime } \rightarrow V \) of class \( {\mathcal{C}}^{1} \) satisfying

- pour tout \( x \in  {U}^{\prime }, y = \psi \left( x\right) \) est l’unique solution de \( f\left( {x, y}\right)  = c \) telle que \( \left( {x, y}\right)  \in  \Omega \) (avec les notations du théorème, on a \( \psi \left( x\right)  = \varphi \left( {x, c}\right) \) ). On obtient la différentielle de \( \psi \) en calculant la différentielle des deux membres de l’égalité \( f\left( {x,\psi \left( x\right) }\right)  = c \) , ce qui donne

> - for all \( x \in  {U}^{\prime }, y = \psi \left( x\right) \) is the unique solution of \( f\left( {x, y}\right)  = c \) such that \( \left( {x, y}\right)  \in  \Omega \) (using the theorem's notation, we have \( \psi \left( x\right)  = \varphi \left( {x, c}\right) \) ). We obtain the differential of \( \psi \) by calculating the differential of both sides of the equality \( f\left( {x,\psi \left( x\right) }\right)  = c \) , which gives

\[
0 = d{f}_{\left( x,\psi \left( x\right) \right) } \circ  \left( {{\operatorname{Id}}_{E}, d{\psi }_{x}}\right)  = {\partial }_{1}{f}_{\left( x,\psi \left( x\right) \right) } + {\partial }_{2}{f}_{\left( x,\psi \left( x\right) \right) } \circ  d{\psi }_{x},
\]

donc \( d{\psi }_{x} = - {\partial }_{2}{f}_{\left( x,\psi \left( x\right) \right) }^{-1} \circ {\partial }_{1}{f}_{\left( x,\psi \left( x\right) \right) } \) .

> therefore \( d{\psi }_{x} = - {\partial }_{2}{f}_{\left( x,\psi \left( x\right) \right) }^{-1} \circ {\partial }_{1}{f}_{\left( x,\psi \left( x\right) \right) } \) .

Cas des fonctions définies sur \( {\mathbb{R}}^{n} \) .

> Case of functions defined on \( {\mathbb{R}}^{n} \) .

COROLLAIRE 5. Soient \( p, q \in {\mathbb{N}}^{ * } \) , \( A \) un ouvert de \( {\mathbb{R}}^{p} \times {\mathbb{R}}^{q} \) et une fonction

> COROLLARY 5. Let \( p, q \in {\mathbb{N}}^{ * } \) , \( A \) be an open set of \( {\mathbb{R}}^{p} \times {\mathbb{R}}^{q} \) and a function

\[
f = \left( {{f}_{1},\ldots ,{f}_{q}}\right)  : A \subset  {\mathbb{R}}^{p} \times  {\mathbb{R}}^{q} \rightarrow  {\mathbb{R}}^{q}\;\left( {x, y}\right)  = \left( {{x}_{1},\ldots ,{x}_{q};{y}_{1},\ldots ,{y}_{q}}\right)  \mapsto  f\left( {x, y}\right)
\]

de classe \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . Soit \( \left( {a, b}\right) \in A \) . On appelle jacobien partiel de \( f \) en \( \left( {a, b}\right) \) le réel

> of class \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . Let \( \left( {a, b}\right) \in A \) . The partial Jacobian of \( f \) at \( \left( {a, b}\right) \) is the real number

\[
\frac{D\left( {{f}_{1},\ldots ,{f}_{q}}\right) }{D\left( {{y}_{1},\ldots ,{y}_{q}}\right) }\left( {a, b}\right)  = \det {\left\lbrack  \frac{\partial {f}_{i}}{\partial {y}_{j}}\left( a, b\right) \right\rbrack  }_{\begin{matrix} {1 \leq  i \leq  q} \\  {1 \leq  j \leq  q} \end{matrix}}.
\]

S’il est non nul en \( \left( {a, b}\right) \) , alors il existe

> If it is non-zero at \( \left( {a, b}\right) \) , then there exists

- un voisinage ouvert \( {U}^{\prime } \) de a, un voisinage ouvert \( W \) de \( f\left( {a, b}\right) \) , un voisinage ouvert \( \Omega \) de \( \left( {a, b}\right) \) ,

> - an open neighborhood \( {U}^{\prime } \) of a, an open neighborhood \( W \) of \( f\left( {a, b}\right) \) , an open neighborhood \( \Omega \) of \( \left( {a, b}\right) \) ,

- une application \( \varphi  : {U}^{\prime } \times  W \rightarrow  {\mathbb{R}}^{q} \) de classe \( {\mathcal{C}}^{k} \) ,

> - a mapping \( \varphi  : {U}^{\prime } \times  W \rightarrow  {\mathbb{R}}^{q} \) of class \( {\mathcal{C}}^{k} \) ,

vérifiant

> satisfying

- pour tout \( x \in  {U}^{\prime } \) , pour tout \( z \in  W,\varphi \left( {x, z}\right) \) est l’unique solution \( y \) de \( f\left( {x, y}\right)  = z \) telle que \( \left( {x, y}\right)  \in  \Omega \) .

> - for all \( x \in  {U}^{\prime } \) , for all \( z \in  W,\varphi \left( {x, z}\right) \) is the unique solution \( y \) of \( f\left( {x, y}\right)  = z \) such that \( \left( {x, y}\right)  \in  \Omega \) .

En particulier, on a \( f\left( {x,\varphi \left( {x, z}\right) }\right) = z \) pour tout \( x \in {U}^{\prime } \) et pour tout \( z \in W \) .

> In particular, we have \( f\left( {x,\varphi \left( {x, z}\right) }\right) = z \) for all \( x \in {U}^{\prime } \) and for all \( z \in W \) .

Démonstration. Quitte à restreindre \( A \) , on peut supposer \( A = U \times V \) , où \( U \) est un ouvert de \( {\mathbb{R}}^{p}, V \) un ouvert de \( {\mathbb{R}}^{q} \) et \( \left( {a, b}\right) \in U \times V \) . Ici, \( {\partial }_{2}{f}_{\left( a, b\right) } \) a pour matrice \( {\left\lbrack \frac{\partial {f}_{i}}{\partial {y}_{j}}\left( a, b\right) \right\rbrack }_{1 \leq i, j \leq q} \) , et d’après les hypothèses, le déterminant de cette matrice est non nul, autrement dit, \( {\partial }_{2}{f}_{\left( a, b\right) } \) est un isomorphisme de \( {\mathbb{R}}^{q} \) (bien sûr bicontinu puisque l’on est en dimension finie). On peut donc appliquer le théorème précédent. Il reste à démontrer que \( \varphi \) est de classe \( {\mathcal{C}}^{k}\ldots \) mais on peut reprendre mot pour mot la démonstration du théorème 2 en remplaçant \( {\mathcal{C}}^{1} \) par \( {\mathcal{C}}^{k} \) , d’où le résultat.

> Proof. By restricting \( A \) , we can assume \( A = U \times V \) , where \( U \) is an open set of \( {\mathbb{R}}^{p}, V \) , \( {\mathbb{R}}^{q} \) is an open set of \( {\mathbb{R}}^{q} \) , and \( \left( {a, b}\right) \in U \times V \) . Here, \( {\partial }_{2}{f}_{\left( a, b\right) } \) has the matrix \( {\left\lbrack \frac{\partial {f}_{i}}{\partial {y}_{j}}\left( a, b\right) \right\rbrack }_{1 \leq i, j \leq q} \) , and according to the hypotheses, the determinant of this matrix is non-zero; in other words, \( {\partial }_{2}{f}_{\left( a, b\right) } \) is an isomorphism of \( {\mathbb{R}}^{q} \) (which is, of course, bicontinuous since we are in finite dimension). We can therefore apply the previous theorem. It remains to prove that \( \varphi \) is of class \( {\mathcal{C}}^{k}\ldots \) , but we can repeat the proof of theorem 2 word for word, replacing \( {\mathcal{C}}^{1} \) with \( {\mathcal{C}}^{k} \) , hence the result.

Remarque 7. Là encore, on utilise souvent ce résultat lorsque \( z \) est fixé, ce qui mène au corollaire suivant :

> Remark 7. Here again, we often use this result when \( z \) is fixed, which leads to the following corollary:

sous les même hypothèses, on peut trouver un voisinage ouvert \( {U}^{\prime } \) de \( a \) , un voisinage ouvert \( \Omega \) de \( c = f\left( {a, b}\right) \) , et une fonction \( \psi : {U}^{\prime } \rightarrow {\mathbb{R}}^{q} \) de classe \( {\mathcal{C}}^{k} \) telle que pour tout \( x \in {U}^{\prime }, y = \psi \left( x\right) \) est l’unique solution de \( f\left( {x, y}\right) = c \) vérifiant \( \left( {x, y}\right) \in \Omega \) .

> under the same hypotheses, we can find an open neighborhood \( {U}^{\prime } \) of \( a \) , an open neighborhood \( \Omega \) of \( c = f\left( {a, b}\right) \) , and a function \( \psi : {U}^{\prime } \rightarrow {\mathbb{R}}^{q} \) of class \( {\mathcal{C}}^{k} \) such that for all \( x \in {U}^{\prime }, y = \psi \left( x\right) \) is the unique solution of \( f\left( {x, y}\right) = c \) satisfying \( \left( {x, y}\right) \in \Omega \) .

En termes intuitifs, ceci s’énonce en disant que \( q \) contraintes (de classe \( {\mathcal{C}}^{k} \) ) sur \( q \) variables mènent localement à une solution de classe \( {\mathcal{C}}^{k} \) en les autres variables. Ceci permet, sous de bonnes hypothèses, de voir les sous-ensembles de \( {\mathbb{R}}^{n} \) définis implicitement par \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) comme des nappes paramétrées.

> Intuitively, this can be stated by saying that \( q \) constraints (of class \( {\mathcal{C}}^{k} \) ) on \( q \) variables lead locally to a solution of class \( {\mathcal{C}}^{k} \) in the other variables. This allows, under good hypotheses, viewing the subsets of \( {\mathbb{R}}^{n} \) implicitly defined by \( f\left( {{x}_{1},\ldots ,{x}_{n}}\right) = 0 \) as parameterized surfaces.

On peut obtenir la matrice jacobienne (resp. les dérivées partielles) de \( \psi \) en écrivant que la matrice jacobienne (resp. les dérivées partielles) de \( f\left( {x,\psi \left( x\right) }\right) \) est nulle (resp. sont nulles).

> We can obtain the Jacobian matrix (resp. the partial derivatives) of \( \psi \) by writing that the Jacobian matrix (resp. the partial derivatives) of \( f\left( {x,\psi \left( x\right) }\right) \) is zero (resp. are zero).

On utilise beaucoup le corollaire énoncé dans la remarque précédente lorsque \( p = q = 1 \) ou lorsque \( p = 2, q = 1 \) . Dans ces cas particuliers, ceci s’énonce comme suit.

> We make frequent use of the corollary stated in the previous remark when \( p = q = 1 \) or when \( p = 2, q = 1 \) . In these special cases, this is stated as follows.

COROLLAIRE 6. Soit \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) (où \( A \) est un ouvert de \( {\mathbb{R}}^{2} \) ) une fonction de classe \( {\mathcal{C}}^{k} \) , \( \left( {k \geq 1}\right) \) . Soit \( \left( {a, b}\right) \in A \) et supposons

> COROLLARY 6. Let \( f : {\mathbb{R}}^{2} \rightarrow \mathbb{R} \) (where \( A \) is an open set of \( {\mathbb{R}}^{2} \) ) be a function of class \( {\mathcal{C}}^{k} \) , \( \left( {k \geq 1}\right) \) . Let \( \left( {a, b}\right) \in A \) and assume

\[
f\left( {a, b}\right)  = 0\;\text{ et }\;\frac{\partial f}{\partial y}\left( {a, b}\right)  \neq  0.
\]

Alors il existe \( \alpha ,\beta > 0 \) tel que pour tout \( x \in \rbrack a - \alpha , a + \alpha \lbrack \) , l’équation \( f\left( {x, y}\right) = 0 \) possède une et une seule solution \( y = \varphi \left( x\right) \) dans l’intervalle \( \rbrack b - \beta , b + \beta \lbrack \) . La fonction \( \varphi \) est de classe \( {\mathcal{C}}^{k} \) sur \( \rbrack a - \alpha , a + \alpha \lbrack \) , et on a

> Then there exists \( \alpha ,\beta > 0 \) such that for all \( x \in \rbrack a - \alpha , a + \alpha \lbrack \) , the equation \( f\left( {x, y}\right) = 0 \) has one and only one solution \( y = \varphi \left( x\right) \) in the interval \( \rbrack b - \beta , b + \beta \lbrack \) . The function \( \varphi \) is of class \( {\mathcal{C}}^{k} \) on \( \rbrack a - \alpha , a + \alpha \lbrack \) , and we have

\[
\forall x \in  \rbrack a - \alpha , a + \alpha \left\lbrack  {,\;{\varphi }^{\prime }\left( x\right)  =  - \frac{\frac{\partial f}{\partial x}\left( {x,\varphi \left( x\right) }\right) }{\frac{\partial f}{\partial y}\left( {x,\varphi \left( x\right) }\right) }.}\right.
\]

Démonstration. L’existence de \( \alpha ,\beta > 0 \) et de \( \varphi \) sont assurés par le corollaire énoncé dans la remarque précédente. Pour calculer \( {\varphi }^{\prime } \) , on dérive la relation \( f\left( {x,\varphi \left( x\right) }\right) = 0 \) qui entraîne

> Proof. The existence of \( \alpha ,\beta > 0 \) and \( \varphi \) is ensured by the corollary stated in the previous remark. To calculate \( {\varphi }^{\prime } \) , we differentiate the relation \( f\left( {x,\varphi \left( x\right) }\right) = 0 \) which leads to

\[
\frac{\partial f}{\partial x}\left( {x,\varphi \left( x\right) }\right)  + {\varphi }^{\prime }\left( x\right) \frac{\partial f}{\partial y}\left( {x,\varphi \left( x\right) }\right)  = 0,
\]

d’où la valeur de \( {\varphi }^{\prime }\left( x\right) \) .

> whence the value of \( {\varphi }^{\prime }\left( x\right) \) .

On démontrerait de même le corollaire suivant

> We would prove the following corollary in the same way

COROLLAIRE 7. Soit \( f : A \subset {\mathbb{R}}^{2} \times \mathbb{R} \rightarrow \mathbb{R} \) (où \( A \) est un ouvert de \( {\mathbb{R}}^{3} \) ) une fonction de classe \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . Soit \( \left( {a, b, c}\right) \in A \) et supposons

> COROLLARY 7. Let \( f : A \subset {\mathbb{R}}^{2} \times \mathbb{R} \rightarrow \mathbb{R} \) (where \( A \) is an open set of \( {\mathbb{R}}^{3} \) ) be a function of class \( {\mathcal{C}}^{k}\left( {k \geq 1}\right) \) . Let \( \left( {a, b, c}\right) \in A \) and assume

\[
f\left( {a, b, c}\right)  = 0\;\text{ et }\;\frac{\partial f}{\partial z}\left( {a, b, c}\right)  \neq  0.
\]

Alors il existe \( \alpha ,\beta ,\gamma > 0 \) tels que pour tout \( \left( {x, y}\right) \in \rbrack a - \alpha , a + \alpha \left\lbrack \times \right\rbrack b - \beta , b + \beta \lbrack \) , l’équation en \( z : f\left( {x, y, z}\right) = 0 \) admette une unique solution \( z = \varphi \left( {x, y}\right) \) dans \( \rbrack c - \gamma , c + \gamma \lbrack \) . La fonction \( \varphi \) est de classe \( {\mathcal{C}}^{k} \) et

> Then there exist \( \alpha ,\beta ,\gamma > 0 \) such that for all \( \left( {x, y}\right) \in \rbrack a - \alpha , a + \alpha \left\lbrack \times \right\rbrack b - \beta , b + \beta \lbrack \) , the equation in \( z : f\left( {x, y, z}\right) = 0 \) admits a unique solution \( z = \varphi \left( {x, y}\right) \) in \( \rbrack c - \gamma , c + \gamma \lbrack \) . The function \( \varphi \) is of class \( {\mathcal{C}}^{k} \) and

\[
\frac{\partial \varphi }{\partial x}\left( {x, y}\right)  =  - \frac{\frac{\partial f}{\partial x}\left( {x, y,\varphi \left( {x, y}\right) }\right) }{\frac{\partial f}{\partial z}\left( {x, y,\varphi \left( {x, y}\right) }\right) },\;\frac{\partial \varphi }{\partial y}\left( {x, y}\right)  =  - \frac{\frac{\partial f}{\partial y}\left( {x, y,\varphi \left( {x, y}\right) }\right) }{\frac{\partial f}{\partial z}\left( {x, y,\varphi \left( {x, y}\right) }\right) }.
\]

Preuve du théorème des extremums liés. Munis du théorème des fonctions impli-cites, nous sommes maintenant en mesure de démontrer le théorème des extremums liés énoncé à la page 337. On utilise les mêmes notations que celles de l'énoncé.

> Proof of the theorem on constrained extrema. Equipped with the implicit function theorem, we are now able to prove the theorem on constrained extrema stated on page 337. We use the same notation as in the statement.

Soit \( s = n - r \) . Identifions \( {\mathbb{R}}^{n} \) à \( {\mathbb{R}}^{s} \times {\mathbb{R}}^{r} \) . On écrit les éléments de \( {\mathbb{R}}^{n} \) sous la forme \( \left( {x, y}\right) = \; \left( {{x}_{1},\ldots ,{x}_{s};{y}_{1},\ldots ,{y}_{r}}\right) \) . Écrivons \( a = \left( {\alpha ,\beta }\right) ,\alpha \in {\mathbb{R}}^{s} \) et \( \beta \in {\mathbb{R}}^{r} \) .

> Let \( s = n - r \) . Identify \( {\mathbb{R}}^{n} \) with \( {\mathbb{R}}^{s} \times {\mathbb{R}}^{r} \) . We write the elements of \( {\mathbb{R}}^{n} \) in the form \( \left( {x, y}\right) = \; \left( {{x}_{1},\ldots ,{x}_{s};{y}_{1},\ldots ,{y}_{r}}\right) \) . Let us write \( a = \left( {\alpha ,\beta }\right) ,\alpha \in {\mathbb{R}}^{s} \) and \( \beta \in {\mathbb{R}}^{r} \) .

Commençons par faire la remarque suivante. On a nécessairement \( r \leq n \) car les formes linéaires \( d{g}_{i, a} \) forment une famille libre et la dimension du dual de \( {\mathbb{R}}^{n} \) est \( n \) . Par ailleurs, si \( r = n \) , le théorème est évident car les \( d{g}_{i, a} \) forment une base de \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) . On peut donc supposer \( r \leq n - 1 \) , c’est-à-dire \( s \geq 1 \) .

> Let us begin by making the following remark. We necessarily have \( r \leq n \) because the linear forms \( d{g}_{i, a} \) form a free family and the dimension of the dual of \( {\mathbb{R}}^{n} \) is \( n \) . Furthermore, if \( r = n \) , the theorem is obvious because the \( d{g}_{i, a} \) form a basis of \( {\left( {\mathbb{R}}^{n}\right) }^{ * } \) . We can therefore assume \( r \leq n - 1 \) , that is to say \( s \geq 1 \) .

Les formes linéaires \( {\left( d{g}_{i, a}\right) }_{1 \leq i \leq r} \) forment une famille libre, la matrice

> The linear forms \( {\left( d{g}_{i, a}\right) }_{1 \leq i \leq r} \) form a linearly independent family, the matrix

\[
\left( \begin{matrix} \frac{\partial {g}_{1}}{\partial {x}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{1}}{\partial {x}_{s}}\left( a\right) & \frac{\partial {g}_{1}}{\partial {y}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{1}}{\partial {y}_{r}}\left( a\right) \\  \vdots & & \vdots & \vdots & & \vdots \\  \frac{\partial {g}_{r}}{\partial {x}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{r}}{\partial {x}_{s}}\left( a\right) & \frac{\partial {g}_{r}}{\partial {y}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{r}}{\partial {y}_{r}}\left( a\right)  \end{matrix}\right)
\]

est donc de rang \( r \) . On peut donc en extraire une sous-matrice \( r \times r \) inversible. Quitte à changer le nom des variables, on peut supposer que

> is therefore of rank \( r \) . We can thus extract an invertible submatrix \( r \times r \) from it. By relabeling the variables, we can assume that

\[
\det {\left( \frac{\partial {g}_{i}}{\partial {y}_{j}}\left( a\right) \right) }_{1 \leq  i, j \leq  r} = \frac{D\left( {{g}_{1},\ldots ,{g}_{r}}\right) }{D\left( {{y}_{1},\ldots ,{y}_{r}}\right) }\left( a\right)  \neq  0.
\]

D'après le théorème des fonctions implicites (plus précisément la remarque 7), on peut donc trouver un voisinage ouvert \( {U}^{\prime } \) de \( \alpha \) dans \( {\mathbb{R}}^{s} \) , un voisinage ouvert \( \Omega \) de \( a = \left( {\alpha ,\beta }\right) \) dans \( {\mathbb{R}}^{n} \) et une fonction \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{r}}\right) : {U}^{\prime } \rightarrow {\mathbb{R}}^{r} \) de classe \( {\mathcal{C}}^{1} \) tels que (en notant \( g = \left( {{g}_{1},\ldots ,{g}_{r}}\right) \) )

> According to the implicit function theorem (more precisely, Remark 7), we can therefore find an open neighborhood \( {U}^{\prime } \) of \( \alpha \) in \( {\mathbb{R}}^{s} \) , an open neighborhood \( \Omega \) of \( a = \left( {\alpha ,\beta }\right) \) in \( {\mathbb{R}}^{n} \) , and a function \( \varphi = \left( {{\varphi }_{1},\ldots ,{\varphi }_{r}}\right) : {U}^{\prime } \rightarrow {\mathbb{R}}^{r} \) of class \( {\mathcal{C}}^{1} \) such that (denoting \( g = \left( {{g}_{1},\ldots ,{g}_{r}}\right) \) )

\[
\left( {g\left( {x, y}\right)  = 0\;\text{ avec }x \in  {U}^{\prime }\text{ et }\left( {x, y}\right)  \in  \Omega }\right)  \Leftrightarrow  \left( {y = \varphi \left( x\right) }\right) .
\]

En d’autres termes, sur un voisinage de \( a \) , les éléments de \( \Gamma = \{ z \mid g\left( z\right) = 0\} \) s’écrivent \( \left( {x,\varphi \left( x\right) }\right) \) . Posons \( h\left( x\right) = f\left( {x,\varphi \left( x\right) }\right) \) . La fonction \( h \) admet donc un extremum local en \( x = \alpha \) (car \( \left( {\alpha ,\varphi \left( \alpha \right) }\right) = a \) et \( \left( {x,\varphi \left( x\right) }\right) \in \Gamma ) \) , ce qui entraîne

> In other words, on a neighborhood of \( a \) , the elements of \( \Gamma = \{ z \mid g\left( z\right) = 0\} \) are written as \( \left( {x,\varphi \left( x\right) }\right) \) . Let \( h\left( x\right) = f\left( {x,\varphi \left( x\right) }\right) \) . The function \( h \) therefore admits a local extremum at \( x = \alpha \) (since \( \left( {\alpha ,\varphi \left( \alpha \right) }\right) = a \) and \( \left( {x,\varphi \left( x\right) }\right) \in \Gamma ) \) , which implies

\[
\forall i,1 \leq  i \leq  s,\;0 = \frac{\partial h}{\partial {x}_{i}}\left( \alpha \right)  = \frac{\partial f}{\partial {x}_{i}}\left( a\right)  + \mathop{\sum }\limits_{{j = 1}}^{r}\frac{\partial {\varphi }_{j}}{\partial {x}_{i}}\left( \alpha \right) \frac{\partial f}{\partial {y}_{j}}\left( a\right) .
\]

\( \left( *\right) \) .

> Par ailleurs, en écrivant les dérivées partielles par rapport aux \( {x}_{i} \) de \( g\left( {x,\varphi \left( x\right) }\right) = 0 \) , on tire

Furthermore, by writing the partial derivatives with respect to the \( {x}_{i} \) of \( g\left( {x,\varphi \left( x\right) }\right) = 0 \) , we obtain

\[
\forall k,1 \leq  k \leq  r,\forall i,1 \leq  i \leq  s,\;0 = \frac{\partial {g}_{k}}{\partial {x}_{i}}\left( a\right)  + \mathop{\sum }\limits_{{j = 1}}^{r}\frac{\partial {\varphi }_{j}}{\partial {x}_{i}}\left( \alpha \right) \frac{\partial {g}_{k}}{\partial {y}_{j}}\left( a\right) .
\]

(**)

> Autrement dit, les \( s \) premiers vecteurs colonnes de la matrice

In other words, the first \( s \) column vectors of the matrix

\[
M = \left( \begin{matrix} \frac{\partial f}{\partial {x}_{1}}\left( a\right) & \cdots & \frac{\partial f}{\partial {x}_{s}}\left( a\right) & \frac{\partial f}{\partial {y}_{1}}\left( a\right) & \cdots & \frac{\partial f}{\partial {y}_{r}}\left( a\right) \\  \frac{\partial {g}_{1}}{\partial {x}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{1}}{\partial {x}_{s}}\left( a\right) & \frac{\partial {g}_{1}}{\partial {y}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{1}}{\partial {y}_{r}}\left( a\right) \\  \vdots & & \vdots & \vdots & & \vdots \\  \frac{\partial {g}_{r}}{\partial {x}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{r}}{\partial {x}_{s}}\left( a\right) & \frac{\partial {g}_{r}}{\partial {y}_{1}}\left( a\right) & \cdots & \frac{\partial {g}_{r}}{\partial {y}_{r}}\left( a\right)  \end{matrix}\right)
\]

s’expriment, d’après (*) et (**), linéairement en fonction de ses \( r \) derniers vecteurs colonnes. Donc rg \( M \leq r \) . Or le rang des vecteurs lignes est égal au rang des vecteurs colonnes de \( M \) (car \( \left. {{\operatorname{rg}}^{t}M = \operatorname{rg}M}\right) \) , donce les \( r + 1 \) vecteurs lignes de \( M \) forment une famille liée, ce qui entraîne l’existence de réels \( {\mu }_{0},\ldots ,{\mu }_{r} \) non tous nuls tels que \( {\mu }_{0}d{f}_{a} + {\mu }_{1}d{g}_{1, a} + \cdots + {\mu }_{r}d{g}_{r, a} = 0 \) . Comme la famille \( {\left( d{g}_{i, a}\right) }_{1 \leq i \leq r} \) est libre, on a \( {\mu }_{0} \neq 0 \) , et en posant \( {\lambda }_{i} = - {\mu }_{i}/{\mu }_{0} \) pour \( 1 \leq i \leq r \) , on en déduit \( d{f}_{a} = \mathop{\sum }\limits_{{i = 1}}^{r}{\lambda }_{i}d{g}_{i, a} \) . D’où le théorème.

> are expressed, according to (*) and (**), linearly in terms of its last \( r \) column vectors. Thus rg \( M \leq r \) . However, the rank of the row vectors is equal to the rank of the column vectors of \( M \) (since \( \left. {{\operatorname{rg}}^{t}M = \operatorname{rg}M}\right) \) , so the \( r + 1 \) row vectors of \( M \) form a linearly dependent family, which implies the existence of real numbers \( {\mu }_{0},\ldots ,{\mu }_{r} \) not all zero such that \( {\mu }_{0}d{f}_{a} + {\mu }_{1}d{g}_{1, a} + \cdots + {\mu }_{r}d{g}_{r, a} = 0 \) . Since the family \( {\left( d{g}_{i, a}\right) }_{1 \leq i \leq r} \) is linearly independent, we have \( {\mu }_{0} \neq 0 \) , and by setting \( {\lambda }_{i} = - {\mu }_{i}/{\mu }_{0} \) for \( 1 \leq i \leq r \) , we deduce \( d{f}_{a} = \mathop{\sum }\limits_{{i = 1}}^{r}{\lambda }_{i}d{g}_{i, a} \) . Hence the theorem.
