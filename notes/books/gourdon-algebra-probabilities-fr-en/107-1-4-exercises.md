#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1. Décomposer sous forme de somme de carrés les formes quadratiques ou hermitiennes suivantes ; en déduire leur signature et leur rang.

> EXERCISE 1. Decompose the following quadratic or Hermitian forms into a sum of squares; deduce their signature and rank.

a) \( \Phi \left( {x, y, z, t}\right) = {xy} + {yz} + {zt} + {tx},\left( {x, y, z, t}\right) \in {\mathbb{R}}^{4} \) .

> b) \( \Phi \left( {x, y, z}\right) = {x}^{2} - 2{y}^{2} + {xz} + {yz},\left( {x, y, z}\right) \in {\mathbb{R}}^{3} \) .

c) \( \Phi \left( {x, y, z}\right) = \bar{x}x + \bar{y}y + \bar{z}z + \bar{x}y + x\bar{y} - \bar{y}z - y\bar{z},\left( {x, y, z}\right) \in {\mathbb{C}}^{3} \) .

> Solution. On va appliquer la méthode de Gauss, garantissant ainsi l'indépendance linéaire des formes linéaires obtenues, ce qui nous permettra de calculer la signature de la forme correspon-dante.

Solution. We will apply Gauss's method, thereby guaranteeing the linear independence of the linear forms obtained, which will allow us to calculate the signature of the corresponding form.

> a) Il suffit d'écrire

a) It suffices to write

\[
\Phi \left( {x, y, z, t}\right)  = \left( {x + z}\right) \left( {y + t}\right)  = \frac{1}{4}\left\lbrack  {{\left( x + z + y + t\right) }^{2} - {\left( x + z - y - t\right) }^{2}}\right\rbrack  .
\]

La signature de \( \Phi \) est donc \( \left( {1,1}\right) \) , son rang \( 1 + 1 = 2 \) .

> The signature of \( \Phi \) is therefore \( \left( {1,1}\right) \) , its rank \( 1 + 1 = 2 \) .

b) On a

> b) We have

\[
\Phi \left( {x, y, z}\right)  = {\left( x + \frac{z}{2}\right) }^{2} - \frac{{z}^{2}}{4} - 2{y}^{2} + {yz} = {\left( x + \frac{z}{2}\right) }^{2} - 2{\left( y - \frac{z}{4}\right) }^{2} + \frac{{z}^{2}}{8} - \frac{{z}^{2}}{4}
\]

\[
= {\left( x + \frac{z}{2}\right) }^{2} - 2{\left( y - \frac{z}{4}\right) }^{2} - \frac{{z}^{2}}{8}.
\]

La signature de \( \Phi \) est donc \( \left( {1,2}\right) \) , son rang est 3 .

> The signature of \( \Phi \) is therefore \( \left( {1,2}\right) \) , its rank is 3 .

c) On a

> c) We have

\[
\Phi \left( {x, y, z}\right)  = \left( {x + y}\right) \left( {\bar{x} + \bar{y}}\right)  + z\bar{z} - \bar{y}z - y\bar{z}
\]

\[
= \left( {x + y}\right) \left( {\bar{x} + \bar{y}}\right)  + \left( {z - y}\right) \left( {\bar{z} - \bar{y}}\right)  - y\bar{y} = {\left| x + y\right| }^{2} + {\left| z - y\right| }^{2} - {\left| y\right| }^{2}.
\]

La signature de \( \Phi \) est donc \( \left( {2,1}\right) \) et son rang est 3 .

> The signature of \( \Phi \) is therefore \( \left( {2,1}\right) \) and its rank is 3 .

EXERCICE 2. Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {\mathbb{C}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{C}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Démontrer que l'application

> EXERCISE 2. Let \( n \in {\mathbb{N}}^{ * } \) . We denote \( {\mathbb{C}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{C}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Prove that the mapping

\[
\Phi  : {\mathbb{C}}_{n}\left\lbrack  X\right\rbrack   \rightarrow  \mathbb{C}\;P \mapsto  {\int }_{-1}^{1}\overline{P\left( x\right) }P\left( {-x}\right) {dx}
\]

est une forme hermitienne et calculer sa signature. Solution. La forme sesquilinéaire

> is a Hermitian form and calculate its signature. Solution. The sesquilinear form

\[
\varphi  : {\mathbb{C}}_{n}{\left\lbrack  X\right\rbrack  }^{2} \rightarrow  \mathbb{C}\;\left( {P, Q}\right)  \mapsto  {\int }_{-1}^{1}\overline{P\left( x\right) }Q\left( {-x}\right) {dx}
\]

est à symétrie hermitienne (on le vérifie facilement en effectuant le changement de variable \( x \rightarrow - x \) dans l’intégrale), et \( \Phi \) est sa forme hermitienne associée.

> is Hermitian symmetric (this is easily verified by performing the change of variable \( x \rightarrow - x \) in the integral), and \( \Phi \) is its associated Hermitian form.

Notons \( \mathcal{P} \) (resp. \( \mathcal{I} \) ) le s.e.v des fonctions paires (resp. impaires) de \( {\mathbb{C}}_{n}\left\lbrack X\right\rbrack \) . On a \( \mathcal{P} \oplus \mathcal{I} = {\mathbb{C}}_{n}\left\lbrack X\right\rbrack \) puisque

> Let \( \mathcal{P} \) (resp. \( \mathcal{I} \) ) be the subspace of even (resp. odd) functions of \( {\mathbb{C}}_{n}\left\lbrack X\right\rbrack \) . We have \( \mathcal{P} \oplus \mathcal{I} = {\mathbb{C}}_{n}\left\lbrack X\right\rbrack \) since

si \( \;P \in \mathcal{P} \cap \mathcal{I}, P\left( {-X}\right) = P\left( X\right) = - P\left( X\right) \; \) donc \( \;P = 0,\; \) ainsi \( \;\mathcal{P} \cap \mathcal{I} = \{ 0\} \)

> if \( \;P \in \mathcal{P} \cap \mathcal{I}, P\left( {-X}\right) = P\left( X\right) = - P\left( X\right) \; \) then \( \;P = 0,\; \) thus \( \;\mathcal{P} \cap \mathcal{I} = \{ 0\} \)

et

\[
\forall P \in  {\mathbb{C}}_{n}\left\lbrack  X\right\rbrack  ,\;P\left( X\right)  = \underset{ \in  \mathcal{P}}{\underbrace{\frac{P\left( X\right)  + P\left( {-X}\right) }{2}}} + \underset{ \in  \mathcal{I}}{\underbrace{\frac{P\left( X\right)  - P\left( {-X}\right) }{2}}},\;\text{ donc }\mathcal{P} + \mathcal{I} = {\mathbb{C}}_{n}\left\lbrack  X\right\rbrack  .
\]

Si \( P \in \mathcal{P}, P \neq 0 \) , est une fonction paire, alors

> If \( P \in \mathcal{P}, P \neq 0 \) is an even function, then

\[
\Phi \left( P\right)  = {\int }_{-1}^{1}\overline{P\left( x\right) }P\left( x\right) {dx} = {\int }_{-1}^{1}{\left| P\left( x\right) \right| }^{2}{dx} > 0,
\]

et si \( P \in \mathcal{I}, P \neq 0 \) , est impaire,

> and if \( P \in \mathcal{I}, P \neq 0 \) is odd,

\[
\Phi \left( P\right)  = {\int }_{-1}^{1}\overline{P\left( x\right) }\left( {-P\left( x\right) }\right) {dx} =  - {\int }_{-1}^{1}{\left| P\left( x\right) \right| }^{2}{dx} < 0.
\]

De plus, \( \mathcal{P} \) et \( \mathcal{I} \) sont \( \Phi \) -orthogonaux car

> Furthermore, \( \mathcal{P} \) and \( \mathcal{I} \) are \( \Phi \) -orthogonal because

\[
\forall \left( {P, Q}\right)  \in  \mathcal{P} \times  \mathcal{I},\;{\int }_{-1}^{1}\overline{P\left( x\right) }Q\left( {-x}\right) {dx} = {\int }_{-1}^{1}\overline{P\left( {-x}\right) }\left( {-Q\left( x\right) }\right) {dx} =  - {\int }_{-1}^{1}\overline{P\left( x\right) }Q\left( {-x}\right) {dx},
\]

donc \( \varphi \left( {P, Q}\right) = 0 \) . Avec la remarque 9 page 246, on en conclue que la signature de \( \Phi \) est \( \left( {\dim \mathcal{P},\dim \mathcal{I}}\right) = \left( {\left\lbrack {n/2}\right\rbrack + 1,\left\lbrack {\left( {n + 1}\right) /2}\right\rbrack }\right) \) (où la notation \( \left\lbrack x\right\rbrack \) désigne la partie entière de \( x \) ).

> therefore \( \varphi \left( {P, Q}\right) = 0 \) . With remark 9 on page 246, we conclude that the signature of \( \Phi \) is \( \left( {\dim \mathcal{P},\dim \mathcal{I}}\right) = \left( {\left\lbrack {n/2}\right\rbrack + 1,\left\lbrack {\left( {n + 1}\right) /2}\right\rbrack }\right) \) (where the notation \( \left\lbrack x\right\rbrack \) denotes the integer part of \( x \) ).

EXERCICE 3 (QUELQUES FORMES QUADRATIQUES SUR \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ). Montrer que les applications suivantes sont des formes quadratiques et calculer leur signature.

> EXERCISE 3 (SOME QUADRATIC FORMS ON \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ). Show that the following mappings are quadratic forms and calculate their signature.

a) \( {q}_{1} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;A \mapsto {\left( \operatorname{tr}A\right) }^{2} \) .

> b) \( {q}_{2} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;A \mapsto \operatorname{tr}\left( {{}^{\mathrm{t}}{AA}}\right) \) .

c) \( {q}_{3} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;A \mapsto \operatorname{tr}\left( {A}^{2}\right) \) .

> d) \( {q}_{4} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;A \mapsto \operatorname{tr}\left( {S{A}^{\mathrm{t}}A}\right) \) , où \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est une matrice symétrique fixée.

d) \( {q}_{4} : {\mathcal{M}}_{n}\left( \mathbb{R}\right) \rightarrow \mathbb{R}\;A \mapsto \operatorname{tr}\left( {S{A}^{\mathrm{t}}A}\right) \) , where \( S \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is a fixed symmetric matrix.

> Solution. Tout au long de l'exercice, nous aurons besoin du résultat suivant :

Solution. Throughout the exercise, we will need the following result:

\[
\text{ Si }P = {\left( {p}_{i, j}\right) }_{1 \leq  i, j \leq  n}\text{ et }Q = {\left( {q}_{i, j}\right) }_{1 \leq  i, j \leq  n} \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \text{ , on a }\operatorname{tr}\left( {PQ}\right)  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}{p}_{i, j}{q}_{j, i}\text{ . }
\]

(*)

> La preuve est simple, il suffit de remarquer que l’élément d’indice \( \left( {i, i}\right) \) dans la produit \( {PQ} \) est égal à \( \mathop{\sum }\limits_{{j = 1}}^{n}{p}_{i, j}{q}_{j, i} \) .

The proof is simple; it suffices to note that the element with index \( \left( {i, i}\right) \) in the product \( {PQ} \) is equal to \( \mathop{\sum }\limits_{{j = 1}}^{n}{p}_{i, j}{q}_{j, i} \) .

> a) L’application \( {q}_{1} \) est bien une forme quadratique, sa forme polaire étant \( {\varphi }_{1} : \left( {A, B}\right) \mapsto \; \operatorname{tr}\left( A\right) \operatorname{tr}\left( B\right) \) .

a) The mapping \( {q}_{1} \) is indeed a quadratic form, its polar form being \( {\varphi }_{1} : \left( {A, B}\right) \mapsto \; \operatorname{tr}\left( A\right) \operatorname{tr}\left( B\right) \) .

> L’application trace est une forme linéaire sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Son noyau \( H \) est donc un hyperplan de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Soit \( S \) un supplémentaire de \( H \) dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , de sorte que \( \dim S = 1 \) et \( \forall A \in S \smallsetminus \{ 0\} \) , \( \operatorname{tr}A \neq 0 \) . Ainsi,

The trace mapping is a linear form on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Its kernel \( H \) is therefore a hyperplane of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Let \( S \) be a complement of \( H \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , such that \( \dim S = 1 \) and \( \forall A \in S \smallsetminus \{ 0\} \) , \( \operatorname{tr}A \neq 0 \) . Thus,

\[
\forall A \in  H,\;{q}_{1}\left( A\right)  = 0\;\text{ et }\;\forall B \in  S \smallsetminus  \{ 0\} ,\;{q}_{1}\left( B\right)  > 0.
\]

\( \left( {* * }\right) \)

> De plus, pour tout couple \( \left( {A, B}\right) \in H \times S,{\varphi }_{1}\left( {A, B}\right) = \operatorname{tr}\left( A\right) \operatorname{tr}\left( B\right) = 0 \) , donc \( H \) et \( S \) sont \( {q}_{1} \) -orthogonaux. Avec (**) et d’après la remarque 9 page 246, ceci suffit pour conclure que la signature de \( {q}_{1} \) est \( \left( {1,0}\right) \) .

Furthermore, for any pair \( \left( {A, B}\right) \in H \times S,{\varphi }_{1}\left( {A, B}\right) = \operatorname{tr}\left( A\right) \operatorname{tr}\left( B\right) = 0 \) , therefore \( H \) and \( S \) are \( {q}_{1} \) -orthogonal. With (**) and according to remark 9 on page 246, this is sufficient to conclude that the signature of \( {q}_{1} \) is \( \left( {1,0}\right) \) .

> b) On a bien affaire à une forme quadratique, la forme polaire associée étant \( {\varphi }_{2} : \left( {A, B}\right) \mapsto \; \operatorname{tr}\left( {{}^{\mathrm{t}}{AB}}\right) \) . Maintenant, en appliquant le principe \( \left( *\right) \) , on voit que toute matrice \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) vérifie \( {q}_{2}\left( A\right) = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) , ce qui suffit à prouver que \( {q}_{2} \) est une forme définie positive, donc de signature \( \left( {{n}^{2},0}\right) \) (en d’autres termes, c’est un produit scalaire sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ).

b) We are indeed dealing with a quadratic form, the associated polar form being \( {\varphi }_{2} : \left( {A, B}\right) \mapsto \; \operatorname{tr}\left( {{}^{\mathrm{t}}{AB}}\right) \) . Now, by applying the principle \( \left( *\right) \) , we see that any matrix \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) satisfies \( {q}_{2}\left( A\right) = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) , which is sufficient to prove that \( {q}_{2} \) is a positive definite form, and therefore has signature \( \left( {{n}^{2},0}\right) \) (in other words, it is a scalar product on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ).

> c) La forme polaire associée à \( {q}_{3} \) est \( {\varphi }_{3} : \left( {A, B}\right) \mapsto \operatorname{tr}\left( {AB}\right) \) .

c) The polar form associated with \( {q}_{3} \) is \( {\varphi }_{3} : \left( {A, B}\right) \mapsto \operatorname{tr}\left( {AB}\right) \) .

> La relation \( \left( *\right) \) prouve que si \( A \in \mathcal{S} \) (s.e.v des matrices symétriques de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) ),{q}_{3}\left( A\right) = \; \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) donc la restriction \( {q}_{3 \mid \mathcal{S}} \) de \( {q}_{3} \) à \( \mathcal{S} \) est définie positive. Si \( A \in \mathcal{A} \) (s.e.v des matrices antisymétriques), \( \left( *\right) \) montre que \( {q}_{3}\left( A\right) = - \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) , ce qui prouve que \( {q}_{3 \mid \mathcal{A}} \) est définie négative. De plus, \( \mathcal{S} \oplus \mathcal{A} = {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (voir la remarque 2) et \( \mathcal{S} \) et \( \mathcal{A} \) sont \( {\varphi }_{3} \) -orthogonaux puisque si \( S \in \mathcal{S} \) et \( A \in \mathcal{A} \) ,

The relation \( \left( *\right) \) proves that if \( A \in \mathcal{S} \) (subspace of symmetric matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) ),{q}_{3}\left( A\right) = \; \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) ), then the restriction \( {q}_{3 \mid \mathcal{S}} \) of \( {q}_{3} \) to \( \mathcal{S} \) is positive definite. If \( A \in \mathcal{A} \) (subspace of antisymmetric matrices), \( \left( *\right) \) shows that \( {q}_{3}\left( A\right) = - \mathop{\sum }\limits_{{i, j}}{a}_{i, j}^{2} \) , which proves that \( {q}_{3 \mid \mathcal{A}} \) is negative definite. Furthermore, \( \mathcal{S} \oplus \mathcal{A} = {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (see remark 2) and \( \mathcal{S} \) and \( \mathcal{A} \) are \( {\varphi }_{3} \) -orthogonal since if \( S \in \mathcal{S} \) and \( A \in \mathcal{A} \) ,

\[
{\varphi }_{3}\left( {S, A}\right)  = \operatorname{tr}\left( {SA}\right)  = \operatorname{tr}\left( {{}^{\mathrm{t}}\left( {SA}\right) }\right)  = \operatorname{tr}\left( {{}^{\mathrm{t}}A{}^{\mathrm{t}}S}\right)  = \operatorname{tr}\left( {-{AS}}\right)  =  - \operatorname{tr}\left( {SA}\right)  =  - {\varphi }_{3}\left( {S, A}\right) ,
\]

donc \( {\varphi }_{3}\left( {S, A}\right) = 0 \) . D’après la remarque 9, ceci suffit pour conclure que la signature de \( {q}_{3} \) est \( \left( {\dim \mathcal{S},\dim \mathcal{A}}\right) = \left( {n\left( {n + 1}\right) /2, n\left( {n - 1}\right) /2}\right) . \)

> therefore \( {\varphi }_{3}\left( {S, A}\right) = 0 \) . According to remark 9, this is sufficient to conclude that the signature of \( {q}_{3} \) is \( \left( {\dim \mathcal{S},\dim \mathcal{A}}\right) = \left( {n\left( {n + 1}\right) /2, n\left( {n - 1}\right) /2}\right) . \)

d) Remarquons tout d’abord que \( {q}_{4}\left( A\right) = \operatorname{tr}\left( {S{A}^{\mathrm{t}}A}\right) = \operatorname{tr}\left( {{}^{\mathrm{t}}{ASA}}\right) \) . La forme polaire de \( {q}_{4} \) est \( {\varphi }_{4} : \left( {A, B}\right) \mapsto \operatorname{tr}\left( {{}^{\mathrm{t}}{ASB}}\right) . \)

> d) First, let us note that \( {q}_{4}\left( A\right) = \operatorname{tr}\left( {S{A}^{\mathrm{t}}A}\right) = \operatorname{tr}\left( {{}^{\mathrm{t}}{ASA}}\right) \) . The polar form of \( {q}_{4} \) is \( {\varphi }_{4} : \left( {A, B}\right) \mapsto \operatorname{tr}\left( {{}^{\mathrm{t}}{ASB}}\right) . \)

La matrice \( S \) est symétrique. L’application \( {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;X \mapsto {}^{\mathrm{t}}{XSX} \) est une forme quadratique. Si on note \( \left( {p, q}\right) \) sa signature, on s’aperçoit que \( S \) est congrue à la matrice \( J = \left( \begin{matrix} {I}_{p} & 0 & 0 \\ 0 & - {I}_{q} & 0 \\ 0 & 0 & 0 \end{matrix}\right) \) , autrement dit

> The matrix \( S \) is symmetric. The map \( {\mathbb{R}}^{n} \rightarrow \mathbb{R}\;X \mapsto {}^{\mathrm{t}}{XSX} \) is a quadratic form. If we denote its signature by \( \left( {p, q}\right) \) , we see that \( S \) is congruent to the matrix \( J = \left( \begin{matrix} {I}_{p} & 0 & 0 \\ 0 & - {I}_{q} & 0 \\ 0 & 0 & 0 \end{matrix}\right) \) , in other words

\[
\exists P \in  \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) ,\;{}^{\mathrm{t}}{PSP} = J = \left( \begin{matrix} {I}_{p} & 0 & 0 \\  0 &  - {I}_{q} & 0 \\  0 & 0 & 0 \end{matrix}\right) .
\]

Maintenant, on se donne \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et on écrit \( B = {PA} \) avec \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j, \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Un peu d'attention montre que

> Now, let us take \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and write \( B = {PA} \) with \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j, \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . A little attention shows that

\[
{q}_{4}\left( B\right)  = {q}_{4}\left( {PA}\right)  = \operatorname{tr}\left( {{}^{\mathrm{t}}{A}^{\mathrm{t}}{PSPA}}\right)  = \operatorname{tr}\left( {{}^{\mathrm{t}}{AJA}}\right)  = \mathop{\sum }\limits_{{j = 1}}^{p}\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, j}^{2} - \mathop{\sum }\limits_{{j = p + 1}}^{{p + q}}\mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i, j}^{2}.
\]

\( \left( {* * * }\right) \)

> Les applications \( {f}_{i, j} : B \mapsto {a}_{i, j} \) où \( {a}_{i, j} \) est le coefficient d’indice \( \left( {i, j}\right) \) dans \( A = {P}^{-1}B \) formant une famille libre de formes linéaires de \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{ * } \) , l’expression (***) montre que la signature de \( {q}_{4} \) est \( \left( {{np},{nq}}\right) \) .

The maps \( {f}_{i, j} : B \mapsto {a}_{i, j} \) where \( {a}_{i, j} \) is the coefficient with index \( \left( {i, j}\right) \) in \( A = {P}^{-1}B \) forming a linearly independent family of linear forms of \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{ * } \) , expression (***) shows that the signature of \( {q}_{4} \) is \( \left( {{np},{nq}}\right) \) .

> EXERCICE 4. Soit \( E \) un \( \mathbb{R} \) -e.v de dimension finie et \( \Phi \) une forme quadratique sur \( E \) . Si \( \Phi \) est définie, montrer que \( \Phi \) est soit positive soit négative.

EXERCISE 4. Let \( E \) be a finite-dimensional \( \mathbb{R} \) -v.s. and \( \Phi \) a quadratic form on \( E \) . If \( \Phi \) is definite, show that \( \Phi \) is either positive or negative.

> Solution. Soit \( \left( {p, q}\right) \) la signature de \( \Phi \) (au passage, on a \( p + q = \dim E \) car \( \Phi \) étant définie, \( \Phi \) est non dégénérée, c’est à dire rg \( \Phi = p + q = \dim E \) ). Il s’agit de montrer que \( p = 0 \) ou \( q = 0 \) . Nous allons raisonner par l’absurde en supposant \( p \neq 0 \) et \( q \neq 0 \) . On peut écrire

Solution. Let \( \left( {p, q}\right) \) be the signature of \( \Phi \) (incidentally, we have \( p + q = \dim E \) because since \( \Phi \) is definite, \( \Phi \) is non-degenerate, i.e., rg \( \Phi = p + q = \dim E \) ). We must show that \( p = 0 \) or \( q = 0 \) . We will reason by contradiction by assuming \( p \neq 0 \) and \( q \neq 0 \) . We can write

\[
\Phi \left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{p}{\varphi }_{i}{\left( x\right) }^{2} - \mathop{\sum }\limits_{{i = 1}}^{q}{\psi }_{i}{\left( x\right) }^{2},
\]

où \( {\varphi }_{1},\ldots ,{\varphi }_{p},{\psi }_{1},\ldots ,{\psi }_{q} \) sont des formes linéaires (on peut même les supposer linéairement in-dépendantes, mais nous n'en aurons pas besoin).

> where \( {\varphi }_{1},\ldots ,{\varphi }_{p},{\psi }_{1},\ldots ,{\psi }_{q} \) are linear forms (we can even assume they are linearly independent, but we will not need that).

Les formes linéaires \( {\varphi }_{1} - {\psi }_{1},{\varphi }_{2},\ldots ,{\varphi }_{p},{\psi }_{2},\ldots ,{\psi }_{q} \) sont au nombre de \( p + q - 1 < \dim E \) , donc si \( F \) désigne le sous-espace de \( {E}^{ * } \) (dual de \( E \) ) engendré par ces formes linéaires, on a dim \( F < n \) , et donc l’orthogonal \( {F}^{ \circ } \) de \( F \) (au sens dual) est différent de \( \{ 0\} \) . En particulier, il existe \( x \in E \) , \( x \neq 0 \) , tel que

> There are \( p + q - 1 < \dim E \) linear forms \( {\varphi }_{1} - {\psi }_{1},{\varphi }_{2},\ldots ,{\varphi }_{p},{\psi }_{2},\ldots ,{\psi }_{q} \), so if \( F \) denotes the subspace of \( {E}^{ * } \) (dual of \( E \)) spanned by these linear forms, we have dim \( F < n \), and thus the orthogonal \( {F}^{ \circ } \) of \( F \) (in the dual sense) is different from \( \{ 0\} \). In particular, there exists \( x \in E \), \( x \neq 0 \), such that

\[
{\varphi }_{1}\left( x\right)  - {\psi }_{1}\left( x\right)  = {\varphi }_{2}\left( x\right)  = \cdots  = {\varphi }_{p}\left( x\right)  = {\psi }_{2}\left( x\right)  = \cdots  = {\psi }_{q}\left( x\right)  = 0,
\]

ce qui entraîne \( {\varphi }_{1}\left( x\right) = {\psi }_{1}\left( x\right) \) et

> which implies \( {\varphi }_{1}\left( x\right) = {\psi }_{1}\left( x\right) \) and

\[
\Phi \left( x\right)  = {\varphi }_{1}{\left( x\right) }^{2} - {\psi }_{1}{\left( x\right) }^{2} = 0,
\]

ce qui est contraire aux hypothèses puisque \( \Phi \) est définie.

> which contradicts the hypotheses since \( \Phi \) is definite.

Remarque. Une autre approche consiste à passer par un argument topologique de conti-nuité. Si \( \Phi \) n’est ni positive ni négative, il existe \( x \neq 0 \) et \( y \neq 0 \) tels que \( \Phi \left( x\right) > 0 \) et \( \Phi \left( y\right) < 0 \) . On considère alors l’application

> Remark. Another approach consists of using a topological continuity argument. If \( \Phi \) is neither positive nor negative, there exist \( x \neq 0 \) and \( y \neq 0 \) such that \( \Phi \left( x\right) > 0 \) and \( \Phi \left( y\right) < 0 \). We then consider the map

\[
f : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R}\;\lambda  \mapsto  \Phi \left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right) .
\]

Comme \( \Phi \) est quadratique, \( f \) est une fonction polynôme de degré \( \leq 2 \) donc est continue. Or \( f\left( 0\right) = \Phi \left( y\right) < 0, f\left( 1\right) = \Phi \left( x\right) > 0 \) donc d’après le théorème des valeurs intermédiaires, il existe \( \lambda \in \rbrack 0,1\left\lbrack \right. \) tel que \( f\left( \lambda \right) = 0 = \Phi \left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right) \) , et \( \Phi \) étant définie, on a \( {\lambda x} + \left( {1 - \lambda }\right) y = \) 0, donc \( y = {\beta x} \) avec \( \beta = - \lambda /\left( {1 - \lambda }\right) \) . Ceci entraîne \( \Phi \left( y\right) = \Phi \left( {\beta x}\right) = {\beta }^{2}\Phi \left( x\right) > 0 \) , ce qui est absurde, donc notre résultat est prouvé. Cette dernière démonstration montre que le résultat de l'exercice est vrai en dimension infinie.

> Since \( \Phi \) is quadratic, \( f \) is a polynomial function of degree \( \leq 2 \) and is therefore continuous. However, \( f\left( 0\right) = \Phi \left( y\right) < 0, f\left( 1\right) = \Phi \left( x\right) > 0 \), so by the intermediate value theorem, there exists \( \lambda \in \rbrack 0,1\left\lbrack \right. \) such that \( f\left( \lambda \right) = 0 = \Phi \left( {{\lambda x} + \left( {1 - \lambda }\right) y}\right) \), and since \( \Phi \) is definite, we have \( {\lambda x} + \left( {1 - \lambda }\right) y = \) 0, thus \( y = {\beta x} \) with \( \beta = - \lambda /\left( {1 - \lambda }\right) \). This implies \( \Phi \left( y\right) = \Phi \left( {\beta x}\right) = {\beta }^{2}\Phi \left( x\right) > 0 \), which is absurd, so our result is proven. This last proof shows that the result of the exercise is true in infinite dimension.

- Le même type de résultats vaut pour les formes hermitiennes.

> - The same type of results holds for Hermitian forms.

EXERCICE 5 (SOUS-ESPACES TOTALEMENT ISOTROPES). Soit \( \Phi \) une forme quadratique sur un \( \mathbb{K} \) -e.v \( E \) de dimension finie \( n \in {\mathbb{N}}^{ * } \) . On appelle sous-espace totalement isotrope (en abrégé SETI) un s.e.v \( F \) de \( E \) tel que pour tout \( x \in F,\Phi \left( x\right) = 0 \) , ce qui équivaut à \( F \subset {F}^{ \bot } \) . On appelle SETI maximal (en abrégé SETIM) un SETI \( F \) tel que pour tout SETI \( G \) vérifiant \( F \subset G \) , on a \( G = F \) .

> EXERCISE 5 (TOTALLY ISOTROPIC SUBSPACES). Let \( \Phi \) be a quadratic form on a finite-dimensional \( \mathbb{K} \)-vector space \( E \) of dimension \( n \in {\mathbb{N}}^{ * } \). A totally isotropic subspace (abbreviated TIS) is a subspace \( F \) of \( E \) such that for all \( x \in F,\Phi \left( x\right) = 0 \), which is equivalent to \( F \subset {F}^{ \bot } \). A maximal TIS (abbreviated MTIS) is a TIS \( F \) such that for any TIS \( G \) satisfying \( F \subset G \), we have \( G = F \).

1/ a) Soit \( F \) un SETI. Montrer que \( \dim F \leq n - r/2 \) , où \( r \) est le rang de \( \Phi \) .

> 1/ a) Let \( F \) be a TIS. Show that \( \dim F \leq n - r/2 \), where \( r \) is the rank of \( \Phi \).

b) Montrer que tout SETI est inclus dans un SETIM.

> b) Show that every TIS is contained in an MTIS.

2/ On suppose dorénavant que \( \Phi \) est non dégénérée.

> 2/ We assume from now on that \( \Phi \) is non-degenerate.

a) Soient \( {F}_{1} \) et \( {F}_{2} \) deux SETIM. On pose \( F = {F}_{1} \cap {F}_{2},{S}_{1} \) un supplémentaire de \( F \) dans \( {F}_{1},{S}_{2} \) un supplémentaire de \( F \) dans \( {F}_{2} \) , de sorte que \( F \oplus {S}_{1} = {F}_{1} \) et \( F \oplus {S}_{2} = {F}_{2} \) . Montrer que \( {S}_{1} \cap {S}_{2}^{ \bot } = {S}_{1}^{ \bot } \cap {S}_{2} = \{ 0\} \) . En déduire \( \dim {F}_{1} = \dim {F}_{2} \) .

> a) Let \( {F}_{1} \) and \( {F}_{2} \) be two maximal isotropic subspaces. Let \( F = {F}_{1} \cap {F}_{2},{S}_{1} \) be a complement of \( F \) in \( {F}_{1},{S}_{2} \) and a complement of \( F \) in \( {F}_{2} \), such that \( F \oplus {S}_{1} = {F}_{1} \) and \( F \oplus {S}_{2} = {F}_{2} \). Show that \( {S}_{1} \cap {S}_{2}^{ \bot } = {S}_{1}^{ \bot } \cap {S}_{2} = \{ 0\} \). Deduce \( \dim {F}_{1} = \dim {F}_{2} \).

Les SETIM ont donc tous même dimension ; cette dimension est appelée indice de \( \Phi \) . b) On suppose ici \( \mathbb{K} = \mathbb{R} \) et \( \Phi \) de signature \( \left( {p, q}\right) \) . Quel est l’indice de \( \Phi \) ?

> Maximal isotropic subspaces therefore all have the same dimension; this dimension is called the index of \( \Phi \). b) Assume here \( \mathbb{K} = \mathbb{R} \) and \( \Phi \) have signature \( \left( {p, q}\right) \). What is the index of \( \Phi \)?

Solution. 1/ a) On a \( F \subset {F}^{ \bot } \) , donc dim \( F \leq \dim {F}^{ \bot } \) , et avec la proposition 6 page 245,

> Solution. 1/ a) We have \( F \subset {F}^{ \bot } \), so dim \( F \leq \dim {F}^{ \bot } \), and with proposition 6 on page 245,

\( 2\dim F \leq \dim F + \dim {F}^{ \bot } = n + \dim \left( {F \cap \operatorname{Ker}\Phi }\right) \leq n + \dim \left( {\operatorname{Ker}\Phi }\right) = {2n} - r, \)

> d'où le résultat.

hence the result.

> b) Soit \( F \) un SETI et \( \Gamma \) l’ensemble des SETI contenant \( F \) . On pose \( m = \sup \{ \dim G, G \in \Gamma \} \) . Par construction, il existe un SETI \( G \) tel que \( F \subset G \) et \( \dim G = m \) . Le s.e.v \( G \) est alors un SETIM (si \( H \) est un SETI et si \( G \subset H \) , alors \( F \subset H \) de sorte que \( H \in \Gamma \) et donc dim \( H \leq m \) , ce qui entraîne dim \( H = m = \dim G \) et \( G = H \) ).

b) Let \( F \) be an isotropic subspace and \( \Gamma \) the set of isotropic subspaces containing \( F \). Let \( m = \sup \{ \dim G, G \in \Gamma \} \). By construction, there exists an isotropic subspace \( G \) such that \( F \subset G \) and \( \dim G = m \). The subspace \( G \) is then a maximal isotropic subspace (if \( H \) is an isotropic subspace and if \( G \subset H \), then \( F \subset H \) such that \( H \in \Gamma \) and thus dim \( H \leq m \), which implies dim \( H = m = \dim G \) and \( G = H \)).

> 2/a) Soit \( x \in {S}_{1} \cap {S}_{2}^{ \bot } \) .

2/a) Let \( x \in {S}_{1} \cap {S}_{2}^{ \bot } \).

> On a déjà \( x \in {F}_{2}^{ \bot } \) . En effet, comme \( {F}_{2} = F \oplus {S}_{2} \) , on a \( {F}_{2}^{ \bot } = {F}^{ \bot } \cap {S}_{2}^{ \bot } \) , et il suffit de montrer que \( x \in {F}^{ \bot } \) . Ceci est vrai car \( x \in {F}_{1} \subset {F}_{1}^{ \bot } \subset {F}^{ \bot } \) (la première inclusion provient du fait que \( {F}_{1} \) est un SETI et la seconde est une conséquence de ce que \( F \subset {F}_{1} \) ).

We already have \( x \in {F}_{2}^{ \bot } \). Indeed, since \( {F}_{2} = F \oplus {S}_{2} \), we have \( {F}_{2}^{ \bot } = {F}^{ \bot } \cap {S}_{2}^{ \bot } \), and it suffices to show that \( x \in {F}^{ \bot } \). This is true because \( x \in {F}_{1} \subset {F}_{1}^{ \bot } \subset {F}^{ \bot } \) (the first inclusion comes from the fact that \( {F}_{1} \) is an isotropic subspace and the second is a consequence of the fact that \( F \subset {F}_{1} \)).

> Poursuivons. On a \( x \in {S}_{1} \subset {F}_{1} \) donc \( x \) est isotrope. Considérons le s.e.v \( G = {F}_{2} + \mathbb{K}x \) . Soit \( z = y + {kx} \in G\left( {y \in {F}_{2}, k \in \mathbb{K}}\right) \) . En notant \( \varphi \) la forme polaire de \( \Phi \) , on a

Let us continue. We have \( x \in {S}_{1} \subset {F}_{1} \) so \( x \) is isotropic. Consider the subspace \( G = {F}_{2} + \mathbb{K}x \). Let \( z = y + {kx} \in G\left( {y \in {F}_{2}, k \in \mathbb{K}}\right) \). Denoting \( \varphi \) as the polar form of \( \Phi \), we have

\[
\Phi \left( z\right)  = \Phi \left( y\right)  + {k}^{2}\Phi \left( x\right)  + {2k\varphi }\left( {x, y}\right) .
\]

(*)

> On a \( y \in {F}_{2} \) donc \( \Phi \left( y\right) = 0 \) ; on a vu que \( \Phi \left( x\right) = 0 \) , et on a montré plus haut que \( x \in {F}_{2}^{ \bot } \) , de sorte que \( \varphi \left( {x, y}\right) = 0 \) , et donc \( \left( *\right) \) entraîne \( \Phi \left( z\right) = 0 \) . Ceci étant vrai pour tout \( z \in G \) , on en déduit que \( G \) est un SETI. Comme \( {F}_{2} \subset G \) et que \( {F}_{2} \) est un SETIM, ceci entraîne \( G = {F}_{2} \) et donc \( x \in {F}_{2} \) . Or \( x \in {S}_{1} \subset {F}_{1} \) , donc \( x \in {F}_{1} \cap {F}_{2} = F \) , donc \( x \in {S}_{1} \cap F = \{ 0\} \) , ce qui entraîne \( x = 0. \) - Nous venons de montrer \( {S}_{1} \cap {S}_{2}^{ \bot } = \{ 0\} \) , c’est à dire que \( {S}_{1} \) et \( {S}_{2}^{ \bot } \) sont en somme directe, ce qui entraîne dim \( {S}_{1} + \dim {S}_{2}^{ \bot } \leq \dim E = n \) . La forme quadratique \( \Phi \) étant non dégénérée, la proposition 6 entraîne dim \( {S}_{2}^{ \bot } = n - \dim {S}_{2} \) , donc finalement \( \dim {S}_{1} + n - \dim {S}_{2} \leq n \) , i.e \( \dim {S}_{1} \leq \dim {S}_{2} \) . Par symétrie, on a également \( \dim {S}_{2} \leq \dim {S}_{1} \) , d’où \( \dim {S}_{1} = \dim {S}_{2} \) et

We have \( y \in {F}_{2} \) so \( \Phi \left( y\right) = 0 \) ; we have seen that \( \Phi \left( x\right) = 0 \) , and we showed above that \( x \in {F}_{2}^{ \bot } \) , so that \( \varphi \left( {x, y}\right) = 0 \) , and thus \( \left( *\right) \) implies \( \Phi \left( z\right) = 0 \) . Since this is true for all \( z \in G \) , we deduce that \( G \) is an OIS. As \( {F}_{2} \subset G \) and \( {F}_{2} \) is an OISM, this implies \( G = {F}_{2} \) and thus \( x \in {F}_{2} \) . However \( x \in {S}_{1} \subset {F}_{1} \) , so \( x \in {F}_{1} \cap {F}_{2} = F \) , so \( x \in {S}_{1} \cap F = \{ 0\} \) , which implies \( x = 0. \) - We have just shown \( {S}_{1} \cap {S}_{2}^{ \bot } = \{ 0\} \) , that is to say that \( {S}_{1} \) and \( {S}_{2}^{ \bot } \) are in direct sum, which implies dim \( {S}_{1} + \dim {S}_{2}^{ \bot } \leq \dim E = n \) . The quadratic form \( \Phi \) being non-degenerate, proposition 6 implies dim \( {S}_{2}^{ \bot } = n - \dim {S}_{2} \) , so finally \( \dim {S}_{1} + n - \dim {S}_{2} \leq n \) , i.e \( \dim {S}_{1} \leq \dim {S}_{2} \) . By symmetry, we also have \( \dim {S}_{2} \leq \dim {S}_{1} \) , whence \( \dim {S}_{1} = \dim {S}_{2} \) and

\[
\dim {F}_{1} = \dim \left( {F \oplus  {S}_{1}}\right)  = \dim F + \dim {S}_{1} = \dim F + \dim {S}_{2} = \dim \left( {F \oplus  {S}_{2}}\right)  = \dim {F}_{2}.
\]

b) La non dégénérescence de \( \Phi \) entraîne \( p + q = n \) . Notons \( k = \inf \{ p, q\} \) . Il existe une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) dans laquelle la matrice de \( \Phi \) a la forme \( \left( \begin{matrix} {I}_{p} & 0 \\ 0 & - {I}_{q} \end{matrix}\right) \) . Posons \( F = \operatorname{Vect}\left( {{e}_{1} + }\right. \; \left. {{e}_{p + 1},\ldots ,{e}_{k} + {e}_{p + k}}\right) \) . Pour tout \( i,1 \leq i \leq k,\Phi \left( {{e}_{i} + {e}_{p + i}}\right) = \Phi \left( {e}_{i}\right) + \Phi \left( {e}_{p + i}\right) = 1 - 1 = 0 \) . Les vecteurs \( {e}_{i} \) étant de plus deux à deux orthogonaux, on en déduit que \( F \) est un SETI.

> b) The non-degeneracy of \( \Phi \) implies \( p + q = n \) . Let \( k = \inf \{ p, q\} \) . There exists a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) in which the matrix of \( \Phi \) has the form \( \left( \begin{matrix} {I}_{p} & 0 \\ 0 & - {I}_{q} \end{matrix}\right) \) . Let \( F = \operatorname{Vect}\left( {{e}_{1} + }\right. \; \left. {{e}_{p + 1},\ldots ,{e}_{k} + {e}_{p + k}}\right) \) . For all \( i,1 \leq i \leq k,\Phi \left( {{e}_{i} + {e}_{p + i}}\right) = \Phi \left( {e}_{i}\right) + \Phi \left( {e}_{p + i}\right) = 1 - 1 = 0 \) . The vectors \( {e}_{i} \) being furthermore pairwise orthogonal, we deduce that \( F \) is an OIS.

Soit \( G \) un SETI tel que \( F \subset G \) . Donnons nous \( x \in G \) , et écrivons \( x = \mathop{\sum }\limits_{i}{\lambda }_{i}{e}_{i} \) . On a

> Let \( G \) be an OIS such that \( F \subset G \) . Let us take \( x \in G \) , and write \( x = \mathop{\sum }\limits_{i}{\lambda }_{i}{e}_{i} \) . We have

\[
\Phi \left( x\right)  = 0 = \mathop{\sum }\limits_{{i = 1}}^{p}{\lambda }_{i}^{2} - \mathop{\sum }\limits_{{i = p + 1}}^{n}{\lambda }_{i}^{2}.
\]

\( \left( {* * }\right) \)

> En désignant toujours par \( \varphi \) la forme polaire de \( \Phi \) , on a

Still denoting by \( \varphi \) the polar form of \( \Phi \) , we have

\[
\forall i,1 \leq  i \leq  k,\;\varphi \left( {x,{e}_{i} + {e}_{p + i}}\right)  = \frac{1}{2}\left\lbrack  {\Phi \left( {x + {e}_{i} + {e}_{p + i}}\right)  - \Phi \left( x\right)  - \Phi \left( {{e}_{i} + {e}_{i + p}}\right) }\right\rbrack   = 0 = {\lambda }_{i} - {\lambda }_{i + p},
\]

ce qui entraîne \( {\lambda }_{i} = {\lambda }_{p + i} \) pour \( 1 \leq i \leq k \) . Avec \( \left( {* * }\right) \) on a donc \( x = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( {{e}_{i} + {e}_{p + i}}\right) \in F \) , et ceci pour tout SETI \( G \) contenant \( F \) . Le s.e.v \( F \) est donc un SETIM et l’indice de \( \Phi \) est \( \dim F = k = \inf \{ p, q\} . \)

> which implies \( {\lambda }_{i} = {\lambda }_{p + i} \) for \( 1 \leq i \leq k \) . With \( \left( {* * }\right) \) we therefore have \( x = \mathop{\sum }\limits_{{i = 1}}^{k}{\lambda }_{i}\left( {{e}_{i} + {e}_{p + i}}\right) \in F \) , and this for any SETI \( G \) containing \( F \) . The subspace \( F \) is therefore a SETIM and the index of \( \Phi \) is \( \dim F = k = \inf \{ p, q\} . \)

EXERCICE 6. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, soit \( \varphi : E \times E \rightarrow \mathbb{K} \) une forme bilinéaire vérifiant la propriété suivante : \( \forall \left( {x, y}\right) \in {E}^{2} \) tel que \( \varphi \left( {x, y}\right) = 0 \) , on a \( \varphi \left( {y, x}\right) = 0 \) . Montrer que \( \varphi \) est symétrique ou antisymétrique.

> EXERCISE 6. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space, let \( \varphi : E \times E \rightarrow \mathbb{K} \) be a bilinear form satisfying the following property: \( \forall \left( {x, y}\right) \in {E}^{2} \) such that \( \varphi \left( {x, y}\right) = 0 \) , we have \( \varphi \left( {y, x}\right) = 0 \) . Show that \( \varphi \) is symmetric or antisymmetric.

Solution. Supposons dans un premier temps \( \varphi \) non dégénérée (i.e pour tout \( x \neq 0,\varphi \left( {x, \cdot }\right) \neq 0 \) ). L’hypothèse sur \( \varphi \) entraîne que pour tout \( x \in E \) , les formes linéaires

> Solution. Let us first assume \( \varphi \) is non-degenerate (i.e. for all \( x \neq 0,\varphi \left( {x, \cdot }\right) \neq 0 \) ). The hypothesis on \( \varphi \) implies that for all \( x \in E \) , the linear forms

\[
\varphi \left( {x, \cdot  }\right)  : y \mapsto  \varphi \left( {x, y}\right) \;\text{ et }\;\varphi \left( {\cdot , x}\right)  : y \mapsto  \varphi \left( {y, x}\right)
\]

ont même noyau. Comme elles sont non nulles, il existe \( {\lambda }_{x} \in \mathbb{K} \) tel que \( \varphi \left( {x, \cdot }\right) = {\lambda }_{x}\varphi \left( {\cdot , x}\right) \) (voir la proposition 5 page 135).

> have the same kernel. Since they are non-zero, there exists \( {\lambda }_{x} \in \mathbb{K} \) such that \( \varphi \left( {x, \cdot }\right) = {\lambda }_{x}\varphi \left( {\cdot , x}\right) \) (see proposition 5 on page 135).

On considère maintenant les applications

> We now consider the mappings

\[
f : E \rightarrow  {E}^{ * }\;x \mapsto  \varphi \left( {x, \cdot  }\right) \;\text{ et }\;g : E \rightarrow  {E}^{ * }\;x \mapsto  \varphi \left( {\cdot , x}\right) .
\]

Ces applications sont linéaires, injectives (car \( \varphi \) est non dégénérée), donc bijectives (car dim \( E = \; \dim {E}^{ * } \) ). Or, comme on a vu plus haut, pour tout \( x \in E, f\left( x\right) = {\lambda }_{x}g\left( x\right) \) , ou encore \( f \circ {g}^{-1}\left( x\right) = \; {\lambda }_{x}x \) avec \( {\lambda }_{x} \in \mathbb{K} \) . D’après la proposition 3 page 121, \( f \circ {g}^{-1} \) est donc une homothétie, autrement dit il existe \( \lambda \in \mathbb{K} \) tel que \( f \circ {g}^{-1} = \lambda \) Id ou encore \( f = {\lambda g} \) . Ceci s’écrit aussi

> These mappings are linear, injective (because \( \varphi \) is non-degenerate), and therefore bijective (because dim \( E = \; \dim {E}^{ * } \) ). However, as seen above, for all \( x \in E, f\left( x\right) = {\lambda }_{x}g\left( x\right) \) , or equivalently \( f \circ {g}^{-1}\left( x\right) = \; {\lambda }_{x}x \) with \( {\lambda }_{x} \in \mathbb{K} \) . According to proposition 3 on page 121, \( f \circ {g}^{-1} \) is therefore a homothety, in other words there exists \( \lambda \in \mathbb{K} \) such that \( f \circ {g}^{-1} = \lambda \) Id or equivalently \( f = {\lambda g} \) . This can also be written as

\[
\forall x \in  E,\;\varphi \left( {x, \cdot  }\right)  = {\lambda \varphi }\left( {\cdot , x}\right)
\]

et donc

> and therefore

\[
\forall x, y \in  E,\;\varphi \left( {x, y}\right)  = {\lambda \varphi }\left( {y, x}\right)  = {\lambda }^{2}\varphi \left( {x, y}\right) .
\]

On en déduit que \( {\lambda }^{2} = 1 \) , donc que \( \lambda \in \{ - 1,1\} \) . La forme bilinéaire \( \varphi \) est donc symétrique ou antisymétrique.

> We deduce that \( {\lambda }^{2} = 1 \) , and therefore that \( \lambda \in \{ - 1,1\} \) . The bilinear form \( \varphi \) is therefore symmetric or antisymmetric.

- Traitons maintenant le cas général. On considère \( \operatorname{Ker}\varphi  = \{ x \in  E \mid  \varphi \left( {x, \cdot  }\right)  = 0\} \) . Soit \( F \) un s.e.v de \( E \) tel que \( \operatorname{Ker}\varphi  \oplus  F = E \) . Comme \( F \cap  \operatorname{Ker}\varphi  = \{ 0\} \) , la restriction de \( \varphi \) à \( F \) est non dégénérée, de sorte que l'on peut appliquer ce que l'on vient de montrer :

> - Let us now treat the general case. We consider \( \operatorname{Ker}\varphi  = \{ x \in  E \mid  \varphi \left( {x, \cdot  }\right)  = 0\} \) . Let \( F \) be a subspace of \( E \) such that \( \operatorname{Ker}\varphi  \oplus  F = E \) . Since \( F \cap  \operatorname{Ker}\varphi  = \{ 0\} \) , the restriction of \( \varphi \) to \( F \) is non-degenerate, so we can apply what we have just shown:

\[
\left( {\exists \varepsilon  \in  \{  - 1,1\} }\right) ,\;\forall \left( {x, y}\right)  \in  {F}^{2},\varphi \left( {x, y}\right)  = {\varepsilon \varphi }\left( {y, x}\right) .
\]

Ceci étant, on se donne \( \left( {x, y}\right) \in {E}^{2} \) et on écrit \( x = {x}_{1} + {x}_{2}, y = {y}_{1} + {y}_{2}\left( {{x}_{1},{y}_{1} \in \operatorname{Ker}\varphi }\right. \) , \( \left. {{x}_{2},{y}_{2} \in F}\right) \) . On a

> Given this, we consider \( \left( {x, y}\right) \in {E}^{2} \) and write \( x = {x}_{1} + {x}_{2}, y = {y}_{1} + {y}_{2}\left( {{x}_{1},{y}_{1} \in \operatorname{Ker}\varphi }\right. \) , \( \left. {{x}_{2},{y}_{2} \in F}\right) \) . We have

\[
\varphi \left( {x, y}\right)  = \varphi \left( {{x}_{1},{y}_{1} + {y}_{2}}\right)  + \varphi \left( {{x}_{2},{y}_{1} + {y}_{2}}\right)  = \varphi \left( {{x}_{2},{y}_{1} + {y}_{2}}\right)  = \varphi \left( {{x}_{2},{y}_{2}}\right)  = {\varepsilon \varphi }\left( {{y}_{2},{x}_{2}}\right)  = {\varepsilon \varphi }\left( {y, x}\right) ,
\]

d'où le résultat.

> hence the result.
