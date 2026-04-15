#### 4.3. Orthogonality

*Français : 4.3. Orthogonalité*

DéFINITION 4. Des éléments \( x \in E \) et \( \varphi \in {E}^{ * } \) sont dit orthogonaux si \( \varphi \left( x\right) = \langle \varphi , x\rangle = 0 \) .

> DEFINITION 4. Elements \( x \in E \) and \( \varphi \in {E}^{ * } \) are said to be orthogonal if \( \varphi \left( x\right) = \langle \varphi , x\rangle = 0 \) .

- Si \( A \subset  E \) , on note \( {A}^{ \bot  } = \left\{  {\varphi  \in  {E}^{ * }\mid \forall x \in  A,\varphi \left( x\right)  = 0}\right\} \) . L’ensemble \( {A}^{ \bot  } \) est un s.e.v de \( {E}^{ * } \) appelé orthogonal de \( A \) .

> - If \( A \subset  E \) , we denote \( {A}^{ \bot  } = \left\{  {\varphi  \in  {E}^{ * }\mid \forall x \in  A,\varphi \left( x\right)  = 0}\right\} \) . The set \( {A}^{ \bot  } \) is a subspace of \( {E}^{ * } \) called the orthogonal of \( A \) .

- Si \( B \subset  {E}^{ * } \) , on note \( {B}^{ \circ  } = \{ x \in  E \mid  \forall \varphi  \in  B,\varphi \left( x\right)  = 0\} \) . L’ensemble \( {B}^{ \circ  } \) est un s.e.v de \( E \) appelé orthogonal de \( B \) .

> - If \( B \subset  {E}^{ * } \) , we denote \( {B}^{ \circ  } = \{ x \in  E \mid  \forall \varphi  \in  B,\varphi \left( x\right)  = 0\} \) . The set \( {B}^{ \circ  } \) is a subspace of \( E \) called the orthogonal of \( B \) .

Remarque 5. Si \( \varphi \in {E}^{ * } \) , alors \( \{ \varphi {\} }^{ \circ } \) est le noyau de \( \varphi \) .

> Remark 5. If \( \varphi \in {E}^{ * } \) , then \( \{ \varphi {\} }^{ \circ } \) is the kernel of \( \varphi \) .

La proposition qui suit se prouve facilement.

> The following proposition is easily proven.

Proposition 2. - Si \( {A}_{1} \subset {A}_{2} \subset E \) , alors \( {A}_{2}^{ \bot } \subset {A}_{1}^{ \bot } \) .

> Proposition 2. - If \( {A}_{1} \subset {A}_{2} \subset E \) , then \( {A}_{2}^{ \bot } \subset {A}_{1}^{ \bot } \) .

- Si \( {B}_{1} \subset  {B}_{2} \subset  {E}^{ * } \) , alors \( {B}_{2}^{ \circ  } \subset  {B}_{1}^{ \circ  } \) .

> - If \( {B}_{1} \subset  {B}_{2} \subset  {E}^{ * } \) , then \( {B}_{2}^{ \circ  } \subset  {B}_{1}^{ \circ  } \) .

- Si \( A \subset  E \) , alors \( {A}^{ \bot  } = {\left( \operatorname{Vect}A\right) }^{ \bot  } \) .

> - If \( A \subset  E \) , then \( {A}^{ \bot  } = {\left( \operatorname{Vect}A\right) }^{ \bot  } \) .

- Si \( B \subset  {E}^{ * } \) , alors \( {B}^{ \circ  } = {\left( \operatorname{Vect}B\right) }^{ \circ  } \) .

> - If \( B \subset  {E}^{ * } \) , then \( {B}^{ \circ  } = {\left( \operatorname{Vect}B\right) }^{ \circ  } \) .

Orthogonalité en dimension finie.

> Orthogonality in finite dimension.

THÉORÉME 3. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie. Alors :

> THEOREM 3. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space. Then:

(i) Si \( F \) est un s.e.v de \( E \) , \( \dim F + \dim {F}^{ \bot } = \dim E \) et \( {F}^{ \bot \circ } = F \) .

> (i) If \( F \) is a subspace of \( E \), \( \dim F + \dim {F}^{ \bot } = \dim E \) and \( {F}^{ \bot \circ } = F \).

(ii) Si \( G \) est un s.e.v de \( {E}^{ * },\dim G + \dim {G}^{ \circ } = \dim E \) et \( {G}^{\circ \bot } = G \) .

> (ii) If \( G \) is a subspace of \( {E}^{ * },\dim G + \dim {G}^{ \circ } = \dim E \) and \( {G}^{\circ \bot } = G \).

Démonstration. (i) Soit \( r = \dim F \) et \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) une base de \( F \) , que nous complétons en une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . On a \( F = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{r}}\right) \) donc d’après la proposition précédente, \( {F}^{ \bot } = \; {\left\{ {e}_{1},\ldots ,{e}_{r}\right\} }^{ \bot } \) . Soit \( \varphi \in {E}^{ * },\varphi = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i}^{ * } \) . Alors

> Proof. (i) Let \( r = \dim F \) and \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) be a basis of \( F \), which we extend to a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \). We have \( F = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{r}}\right) \) so, according to the previous proposition, \( {F}^{ \bot } = \; {\left\{ {e}_{1},\ldots ,{e}_{r}\right\} }^{ \bot } \). Let \( \varphi \in {E}^{ * },\varphi = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}{e}_{i}^{ * } \). Then

\[
\left( {\varphi  \in  {\left\{  {e}_{1},\ldots ,{e}_{r}\right\}  }^{ \bot  }}\right) \; \Leftrightarrow  \;\left( {\forall i \in  \{ 1,\ldots , r\} ,\;0 = \varphi \left( {e}_{i}\right)  = {\lambda }_{i}}\right) .
\]

Ainsi, \( \varphi \in {F}^{ \bot } \) si et seulement si \( \varphi \in \operatorname{Vect}\left( {{e}_{r + 1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) d’où la première égalité de (i).

> Thus, \( \varphi \in {F}^{ \bot } \) if and only if \( \varphi \in \operatorname{Vect}\left( {{e}_{r + 1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \), hence the first equality of (i).

Maintenant, toujours d’après la proposition précédente, on a \( {F}^{ \bot \circ } = {\left\{ {e}_{r + 1}^{ * },\ldots ,{e}_{n}^{ * }\right\} }^{ \circ } \) . Donc

> Now, still according to the previous proposition, we have \( {F}^{ \bot \circ } = {\left\{ {e}_{r + 1}^{ * },\ldots ,{e}_{n}^{ * }\right\} }^{ \circ } \). Therefore

\[
\left( {x = \mathop{\sum }\limits_{{i = 1}}^{n}{\alpha }_{i}{e}_{i} \in  {F}^{ \bot   \circ  }}\right)  \Leftrightarrow  \;\left( {\forall i \in  \{ r + 1,\ldots , n\} ,\;0 = {e}_{i}^{ * }\left( x\right)  = {\alpha }_{i}}\right) ,
\]

ce qui prouve \( {F}^{ \bot \circ } = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{r}}\right) = F \) .

> which proves \( {F}^{ \bot \circ } = \operatorname{Vect}\left( {{e}_{1},\ldots ,{e}_{r}}\right) = F \).

(ii) Soit \( r = \dim G,\left( {{f}_{1},\ldots ,{f}_{r}}\right) \) une base de \( G \) , complétée en une base \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) de \( {E}^{ * } \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base antéduale de cette dernière, de sorte que \( \forall i,{f}_{i} = {e}_{i}^{ * } \) . On a \( G = \; \operatorname{Vect}\left( {{e}_{1}^{ * },\ldots ,{e}_{r}^{ * }}\right) \) et en procédant comme plus haut, on trouve \( {G}^{ \circ } = \operatorname{Vect}\left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) et \( {G}^{\circ \bot } = \; \operatorname{Vect}\left( {{e}_{1}^{ * },\ldots ,{e}_{r}^{ * }}\right) = G. \)

> (ii) Let \( r = \dim G,\left( {{f}_{1},\ldots ,{f}_{r}}\right) \) be a basis of \( G \), extended to a basis \( \left( {{f}_{1},\ldots ,{f}_{n}}\right) \) of \( {E}^{ * } \). Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be an antidual basis of the latter, such that \( \forall i,{f}_{i} = {e}_{i}^{ * } \). We have \( G = \; \operatorname{Vect}\left( {{e}_{1}^{ * },\ldots ,{e}_{r}^{ * }}\right) \) and by proceeding as above, we find \( {G}^{ \circ } = \operatorname{Vect}\left( {{e}_{r + 1},\ldots ,{e}_{n}}\right) \) and \( {G}^{\circ \bot } = \; \operatorname{Vect}\left( {{e}_{1}^{ * },\ldots ,{e}_{r}^{ * }}\right) = G. \)

Consequence. En dimension finie, un sous-espace est égal à l'espace tout entier si et seule-ment si son orthogonal est nul.

> Corollary. In finite dimension, a subspace is equal to the entire space if and only if its orthogonal is zero.

Remarque 6. L’égalité \( {F}^{ \bot \circ } = F \) reste vraie en dimension infinie. Par contre l’égalité \( B = {B}^{\circ \bot } \) est fausse en dimension infinie. Prenons par exemple \( E = \mathbb{R}\left\lbrack X\right\rbrack \) et \( B \) le s.e.v de \( {E}^{ * } \) engendré par les formes linéaires \( {\varphi }_{n} : P \mapsto {P}^{\left( n\right) }\left( 0\right) \left( {n \in \mathbb{N}}\right) \) . Si \( P \in {B}^{ \circ } \) , alors pour tout \( n \in \mathbb{N},{P}^{\left( n\right) }\left( 0\right) = 0 \) donc d’après la formule de Taylor, \( P = 0 \) . Autrement dit, \( {B}^{ \circ } = \{ 0\} \) , donc \( {B}^{\circ \bot } = \{ 0{\} }^{ \bot } = {E}^{ * } \) . On a donc \( B \neq {B}^{\circ \bot } = {E}^{ * } \) (par exemple, \( \varphi : P \mapsto P\left( 1\right) \) est dans \( {E}^{ * } \) et on vérifie facilement que \( \varphi \notin B \) ). Cependant l’inclusion \( B \subset {B}^{\circ \bot } \) est vraie en dimension infinie.

> Remark 6. The equality \( {F}^{ \bot \circ } = F \) remains true in infinite dimension. However, the equality \( B = {B}^{\circ \bot } \) is false in infinite dimension. Let us take for example \( E = \mathbb{R}\left\lbrack X\right\rbrack \) and \( B \) the subspace of \( {E}^{ * } \) generated by the linear forms \( {\varphi }_{n} : P \mapsto {P}^{\left( n\right) }\left( 0\right) \left( {n \in \mathbb{N}}\right) \) . If \( P \in {B}^{ \circ } \) , then for all \( n \in \mathbb{N},{P}^{\left( n\right) }\left( 0\right) = 0 \) , therefore according to Taylor's formula, \( P = 0 \) . In other words, \( {B}^{ \circ } = \{ 0\} \) , so \( {B}^{\circ \bot } = \{ 0{\} }^{ \bot } = {E}^{ * } \) . We thus have \( B \neq {B}^{\circ \bot } = {E}^{ * } \) (for example, \( \varphi : P \mapsto P\left( 1\right) \) is in \( {E}^{ * } \) and it is easy to verify that \( \varphi \notin B \) ). However, the inclusion \( B \subset {B}^{\circ \bot } \) is true in infinite dimension.

En traduisant le théorème précédent en termes d'équations, on obtient le corollaire suivant.

> By translating the previous theorem into terms of equations, we obtain the following corollary.

COROLLAIRE 1 (ÉQUATIONS D'UN S.E.V EN DIMENSION FINIE). Soit E un K.e.v de dimension finie \( n \) .

> COROLLARY 1 (EQUATIONS OF A SUBSPACE IN FINITE DIMENSION). Let E be a K-vector space of finite dimension \( n \) .

- Soient \( p \) formes linéaires \( {\varphi }_{1},\ldots ,{\varphi }_{p} \) de \( {E}^{ * } \) telles que \( \operatorname{rg}\left( {{\varphi }_{1},\ldots ,{\varphi }_{p}}\right)  = r \) . Le s.e.v \( F = \left\{  {x \in  E\mid \forall i,{\varphi }_{i}\left( x\right)  = 0}\right\} \) est de dimension \( n - r \) .

> - Let \( p \) linear forms \( {\varphi }_{1},\ldots ,{\varphi }_{p} \) of \( {E}^{ * } \) such that \( \operatorname{rg}\left( {{\varphi }_{1},\ldots ,{\varphi }_{p}}\right)  = r \) . The subspace \( F = \left\{  {x \in  E\mid \forall i,{\varphi }_{i}\left( x\right)  = 0}\right\} \) has dimension \( n - r \) .

- Réciproquement, si \( F \) est un s.e.v de \( E \) de dimension \( q \) , il existe \( n - q \) formes linéaires linéairement indépendantes \( {\varphi }_{1},\ldots ,{\varphi }_{n - q} \) telles que \( F = \{ x \in  E \mid  \forall i,1 \leq \; i \leq  n - q,{\varphi }_{i}\left( x\right)  = 0\} . \)

> - Conversely, if \( F \) is a subspace of \( E \) of dimension \( q \) , there exist \( n - q \) linearly independent linear forms \( {\varphi }_{1},\ldots ,{\varphi }_{n - q} \) such that \( F = \{ x \in  E \mid  \forall i,1 \leq \; i \leq  n - q,{\varphi }_{i}\left( x\right)  = 0\} . \)

Proposition 3. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie et \( {A}_{1} \) et \( {A}_{2} \) deux s.e.v de E. Alors

> Proposition 3. Let \( E \) be a \( \mathbb{K} \) -vector space of finite dimension and \( {A}_{1} \) and \( {A}_{2} \) be two subspaces of E. Then

\[
\text{ (i) }{\left( {A}_{1} + {A}_{2}\right) }^{ \bot  } = {A}_{1}^{ \bot  } \cap  {A}_{2}^{ \bot  }
\]

(ii) \( {\left( {A}_{1} \cap {A}_{2}\right) }^{ \bot } = {A}_{1}^{ \bot } + {A}_{2}^{ \bot } \) .

> (ii) \( {\left( {A}_{1} \cap {A}_{2}\right) }^{ \bot } = {A}_{1}^{ \bot } + {A}_{2}^{ \bot } \) .

Soient \( {B}_{1} \) et \( {B}_{2} \) deux s.e.v de \( {E}^{ * } \) . Alors

> Let \( {B}_{1} \) and \( {B}_{2} \) be two subspaces of \( {E}^{ * } \) . Then

\[
\text{ (iii) }{\left( {B}_{1} + {B}_{2}\right) }^{ \circ  } = {B}_{1}^{ \circ  } \cap  {B}_{2}^{ \circ  }
\]

(iv) \( {\left( {B}_{1} \cap {B}_{2}\right) }^{ \circ } = {B}_{1}^{ \circ } + {B}_{2}^{ \circ } \) .

> (iv) \( {\left( {B}_{1} \cap {B}_{2}\right) }^{ \circ } = {B}_{1}^{ \circ } + {B}_{2}^{ \circ } \) .

La preuve est simple. Pour montrer chaque assertion, on montre une inclusion triviale puis l'égalité des dimensions grâce au théorème 3.

> The proof is simple. To show each assertion, we show a trivial inclusion and then the equality of dimensions using Theorem 3.

##### Orthogonality and hyperplanes.

*Français : Orthogonalité et hyperplans.*

PROPOSITION 4. Soit \( \varphi \in {E}^{ * } \) une forme linéaire non nulle. Alors \( \operatorname{Ker}\varphi \) est un hyperplan de E. Réciproquement, tout hyperplan de E est le noyau d'une forme linéaire non nulle.

> PROPOSITION 4. Let \( \varphi \in {E}^{ * } \) be a non-zero linear form. Then \( \operatorname{Ker}\varphi \) is a hyperplane of E. Conversely, every hyperplane of E is the kernel of a non-zero linear form.

Démonstration. Soit \( \varphi \in {E}^{ * },\varphi \neq 0 \) . On sait que \( E/\operatorname{Ker}\varphi \) est isomorphe à \( \operatorname{Im}\varphi = \mathbb{K} \) , donc de dimension 1, ce qui n’est autre que de dire que Ker \( \varphi \) est un hyperplan de \( E \) .

> Proof. Let \( \varphi \in {E}^{ * },\varphi \neq 0 \) . We know that \( E/\operatorname{Ker}\varphi \) is isomorphic to \( \operatorname{Im}\varphi = \mathbb{K} \) , thus of dimension 1, which is equivalent to saying that Ker \( \varphi \) is a hyperplane of \( E \) .

Réciproquement, soit \( H \) un hyperplan de \( E \) . D’après la proposition 2 page 120, il existe un s.e.v \( S = \mathbb{K}{x}_{0} \) de \( E \) de dimension 1 tel que \( H \oplus S = E \) . Si maintenant on définit \( \varphi \in {E}^{ * } \) par \( \varphi \left( x\right) = 0 \) si \( x \in H \) et \( \varphi \left( {\lambda {x}_{0}}\right) = \lambda \) sur \( S \) , on voit que \( \operatorname{Ker}\varphi = H \) .

> Conversely, let \( H \) be a hyperplane of \( E \) . According to proposition 2 on page 120, there exists a subspace \( S = \mathbb{K}{x}_{0} \) of \( E \) of dimension 1 such that \( H \oplus S = E \) . If we now define \( \varphi \in {E}^{ * } \) by \( \varphi \left( x\right) = 0 \) if \( x \in H \) and \( \varphi \left( {\lambda {x}_{0}}\right) = \lambda \) on \( S \) , we see that \( \operatorname{Ker}\varphi = H \) .

Proposition 5. Soit \( H \) un hyperplan de E. L’ensemble \( {H}^{ \bot } \) des formes linéaires sur \( E \) qui s’annulent sur \( H \) est une droite de \( {E}^{ * } \) .

> Proposition 5. Let \( H \) be a hyperplane of E. The set \( {H}^{ \bot } \) of linear forms on \( E \) that vanish on \( H \) is a line in \( {E}^{ * } \) .

Démonstration. D’après la proposition précédente, il existe \( {\varphi }_{0} \in {E}^{ * } \) tel que Ker \( {\varphi }_{0} = H \) . Mainte-nant, soit \( \varphi \in {E}^{ * } \) une forme linéaire qui s’annule sur \( H \) . Soit \( {x}_{0} \in E \) tel que \( H \oplus \mathbb{K}{x}_{0} = E \) . On a \( {\varphi }_{0}\left( {x}_{0}\right) \neq 0 \) (sinon \( {\varphi }_{0} \) s’annule sur \( H \) et sur \( \mathbb{K}{x}_{0} \) donc sur \( E \) , ce qui est absurde car \( \left. {\mathbb{K}\operatorname{er}{\varphi }_{0} = H}\right) \) . Posons \( \lambda = \varphi \left( {x}_{0}\right) /{\varphi }_{0}\left( {x}_{0}\right) \) et \( \psi = \varphi - \lambda {\varphi }_{0} \) . Comme \( \varphi \) et \( {\varphi }_{0} \) s’annulent sur \( H,\psi \) s’annule sur \( H \) . Or par construction de \( \lambda ,\psi \left( {x}_{0}\right) = 0 \) . L’application \( \psi \) s’annule donc aussi sur \( \mathbb{K}{x}_{0} \) , donc sur \( E \) tout entier, et donc \( \varphi = \lambda {\varphi }_{0} \in \operatorname{Vect}\left( {\varphi }_{0}\right) \) . Réciproquement, on vérifie facilement que si \( \varphi \in \operatorname{Vect}\left( {\varphi }_{0}\right) \) , alors \( \varphi \) s’annule sur \( H \) .

> Proof. According to the previous proposition, there exists \( {\varphi }_{0} \in {E}^{ * } \) such that Ker \( {\varphi }_{0} = H \) . Now, let \( \varphi \in {E}^{ * } \) be a linear form that vanishes on \( H \) . Let \( {x}_{0} \in E \) be such that \( H \oplus \mathbb{K}{x}_{0} = E \) . We have \( {\varphi }_{0}\left( {x}_{0}\right) \neq 0 \) (otherwise \( {\varphi }_{0} \) vanishes on \( H \) and on \( \mathbb{K}{x}_{0} \) , thus on \( E \) , which is absurd because \( \left. {\mathbb{K}\operatorname{er}{\varphi }_{0} = H}\right) \) ). Let \( \lambda = \varphi \left( {x}_{0}\right) /{\varphi }_{0}\left( {x}_{0}\right) \) and \( \psi = \varphi - \lambda {\varphi }_{0} \) . Since \( \varphi \) and \( {\varphi }_{0} \) vanish on \( H,\psi \) , \( \lambda ,\psi \left( {x}_{0}\right) = 0 \) vanishes on \( H \) . However, by construction of \( \lambda ,\psi \left( {x}_{0}\right) = 0 \) . The map \( \psi \) therefore also vanishes on \( \mathbb{K}{x}_{0} \) , thus on the whole of \( E \) , and so \( \varphi = \lambda {\varphi }_{0} \in \operatorname{Vect}\left( {\varphi }_{0}\right) \) . Conversely, it is easy to verify that if \( \varphi \in \operatorname{Vect}\left( {\varphi }_{0}\right) \) , then \( \varphi \) vanishes on \( H \) .

Remarque 7. On peut montrer de manière plus générale que si \( F \) est un s.e.v de \( E \) de codimension finie, alors \( {F}^{ \bot } \) est un s.e.v de \( {E}^{ * } \) de dimension \( {\operatorname{codim}}_{E}F \) .

> Remark 7. It can be shown more generally that if \( F \) is a subspace of \( E \) of finite codimension, then \( {F}^{ \bot } \) is a subspace of \( {E}^{ * } \) of dimension \( {\operatorname{codim}}_{E}F \) .
