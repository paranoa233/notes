#### 1.2. Study in finite dimension

*Français : 1.2. Étude en dimension finie*

La lettre \( E \) désigne désormais un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) .

> The letter \( E \) henceforth denotes a \( \mathbb{K} \)-vector space of finite dimension \( n \in {\mathbb{N}}^{ * } \).

##### Characteristic polynomial.

*Français : Polynôme caractéristique.*

DÉFINITION 3. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On appelle polynôme caractéristique de \( A \) le polynôme \( \operatorname{de}\mathbb{K}\left\lbrack X\right\rbrack \) défini par \( {P}_{A}\left( X\right) = \det \left( {A - X{I}_{n}}\right) \) .

> DEFINITION 3. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). The characteristic polynomial of \( A \) is the polynomial \( \operatorname{de}\mathbb{K}\left\lbrack X\right\rbrack \) defined by \( {P}_{A}\left( X\right) = \det \left( {A - X{I}_{n}}\right) \).

Remarque 2. - Une matrice a même polynôme caractéristique que sa transposée.

> Remark 2. - A matrix has the same characteristic polynomial as its transpose.

- Deux matrices semblables ont même polynôme caractéristique.

> - Two similar matrices have the same characteristic polynomial.

- On a \( {P}_{A}\left( 0\right)  = \det A \) (i.e. le coefficient constant de \( {P}_{A} \) est égal à \( \det A \) ).

> - We have \( {P}_{A}\left( 0\right)  = \det A \) (i.e., the constant coefficient of \( {P}_{A} \) is equal to \( \det A \)).

DÉFINITION 4. Soit \( f \in \mathcal{L}\left( E\right) \) . Le polynôme caractéristique de la matrice de \( f \) dans une base \( B \) de \( E \) ne dépend pas de la base \( B \) choisie. On l’appelle polynôme caractéristique de \( f \) et on le note \( {P}_{f} \) .

> DEFINITION 4. Let \( f \in \mathcal{L}\left( E\right) \). The characteristic polynomial of the matrix of \( f \) in a basis \( B \) of \( E \) does not depend on the chosen basis \( B \). It is called the characteristic polynomial of \( f \) and is denoted by \( {P}_{f} \).

Remarque 3. Un endomorphisme \( f \in \mathcal{L}\left( E\right) \) a même polynôme caractéristique que son application transposée \( {}^{\mathrm{t}}f\left( {\operatorname{car}{\left\lbrack {}^{\mathrm{t}}f\right\rbrack }_{B} = {}^{\mathrm{t}}{\left\lbrack f\right\rbrack }_{B}}\right) \) .

> Remark 3. An endomorphism \( f \in \mathcal{L}\left( E\right) \) has the same characteristic polynomial as its transpose map \( {}^{\mathrm{t}}f\left( {\operatorname{car}{\left\lbrack {}^{\mathrm{t}}f\right\rbrack }_{B} = {}^{\mathrm{t}}{\left\lbrack f\right\rbrack }_{B}}\right) \).

Proposition 1. \( \lambda \) est valeur propre de \( f \in \mathcal{L}\left( E\right) \) si et seulement si \( {P}_{f}\left( \lambda \right) = 0 \) .

> Proposition 1. \( \lambda \) is an eigenvalue of \( f \in \mathcal{L}\left( E\right) \) if and only if \( {P}_{f}\left( \lambda \right) = 0 \).

Remarque 4. Bien sûr, ce résultat reste vrai pour les matrices. En fait, en dimension finie, tout ce qui est vrai pour les endomorphismes est vrai pour les matrices et réciproquement (en effet, toute matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) peut s’associer à l’endomorphisme de \( {\mathbb{K}}^{n} : X \mapsto {AX} \) , c’est-à-dire l’endomorphisme de \( {\mathbb{K}}^{n} \) dont \( A \) est la matrice dans la base canonique de \( {\mathbb{K}}^{n} \) ).

> Remark 4. Of course, this result remains true for matrices. In fact, in finite dimension, everything true for endomorphisms is true for matrices and vice versa (indeed, any matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) can be associated with the endomorphism of \( {\mathbb{K}}^{n} : X \mapsto {AX} \), that is to say the endomorphism of \( {\mathbb{K}}^{n} \) whose \( A \) is the matrix in the canonical basis of \( {\mathbb{K}}^{n} \)).

Remarque 5. - Si \( \mathbb{K} \) est algébriquement clos (par exemple \( \mathbb{K} = \mathbb{C} \) ), tout élément \( f \in \mathcal{L}\left( E\right) \) a au moins une valeur propre \( \lambda \in \mathbb{K} \) .

> Remark 5. - If \( \mathbb{K} \) is algebraically closed (for example \( \mathbb{K} = \mathbb{C} \)), every element \( f \in \mathcal{L}\left( E\right) \) has at least one eigenvalue \( \lambda \in \mathbb{K} \).

- Pour montrer que \( \lambda \) est valeur propre d’une matrice \( A \) , on peut montrer que \( \operatorname{rg}(A - \; \left. {\lambda {I}_{n}}\right)  < n \) (ce qui est parfois plus simple que de montrer \( {P}_{A}\left( \lambda \right)  = 0 \) ). Par exemple si \( n \geq  2 \) et

> - To show that \( \lambda \) is an eigenvalue of a matrix \( A \), one can show that \( \operatorname{rg}(A - \; \left. {\lambda {I}_{n}}\right)  < n \) (which is sometimes simpler than showing \( {P}_{A}\left( \lambda \right)  = 0 \)). For example, if \( n \geq  2 \) and

\[
A = \left( \begin{matrix} a & 1 & \cdots & 1 \\  1 &  \ddots  &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & 1 \\  1 & \cdots & 1 & a \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) ,
\]

on voit que \( \operatorname{rg}\left( {A - \left( {a - 1}\right) {I}_{n}}\right) = 1 < n \) donc \( a - 1 \) est valeur propre de \( A \) et \( \dim {E}_{a - 1} = n - 1 \) .

> we see that \( \operatorname{rg}\left( {A - \left( {a - 1}\right) {I}_{n}}\right) = 1 < n \) therefore \( a - 1 \) is an eigenvalue of \( A \) and \( \dim {E}_{a - 1} = n - 1 \) .

- Dans la pratique, pour déterminer \( {E}_{\lambda } \) lorsque \( \lambda \) est valeur propre d’une matrice \( A = {\left( {a}_{i, j}\right) }_{1 \leq  i, j \leq  n} \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on résout le système \( {AX} = {\lambda X} \) qui s’écrit

> - In practice, to determine \( {E}_{\lambda } \) when \( \lambda \) is an eigenvalue of a matrix \( A = {\left( {a}_{i, j}\right) }_{1 \leq  i, j \leq  n} \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , we solve the system \( {AX} = {\lambda X} \) which is written

\[
\left\{  \begin{matrix} \left( {{a}_{1,1} - \lambda }\right) & {x}_{1} + & {a}_{1,2} & {x}_{2} + \cdots  + & {a}_{1, n} & {x}_{n} = 0 \\  {a}_{2,1} & {x}_{1} + & \left( {{a}_{2,2} - \lambda }\right) & {x}_{2} + \cdots  + & {a}_{2, n} & {x}_{n} = 0 \\  \cdots & \cdots & & \cdots & \cdots & \cdots \\  {a}_{n,1} & {x}_{1} + & {a}_{n,2} & {x}_{2} + \cdots  + & \cdots & \cdots  \end{matrix}\right.
\]

(voir l'exercice 1 page 177).

> (see exercise 1 on page 177).

Coefficients du polynôme caractéristique d’une matrice. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On peut écrire

> Coefficients of the characteristic polynomial of a matrix. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . We can write

\[
{P}_{A}\left( X\right)  = {\left( -1\right) }^{n}\left\lbrack  {{X}^{n} - {\beta }_{1}{X}^{n - 1} + {\beta }_{2}{X}^{n - 2} + \cdots  + {\left( -1\right) }^{n - 1}{\beta }_{n - 1}X + {\left( -1\right) }^{n}{\beta }_{n}}\right\rbrack  ,
\]

où \( {\beta }_{1} = \operatorname{tr}A,{\beta }_{n} = \det A \) , et pour tout \( k,{\beta }_{k} \) est la somme des mineurs principaux de \( A \) d’ordre \( k \) (rappelons qu’un mineur principal d’ordre \( k \) est un mineur obtenu comme intersection de \( k \) lignes et de \( k \) colonnes de même numéros). En particulier, si \( \widetilde{A} \) désigne la comatrice de \( A,{\beta }_{n - 1} = \operatorname{tr}\widetilde{A} \) .

> where \( {\beta }_{1} = \operatorname{tr}A,{\beta }_{n} = \det A \) , and for all \( k,{\beta }_{k} \) is the sum of the principal minors of \( A \) of order \( k \) (recall that a principal minor of order \( k \) is a minor obtained as the intersection of \( k \) rows and \( k \) columns with the same indices). In particular, if \( \widetilde{A} \) denotes the comatrix of \( A,{\beta }_{n - 1} = \operatorname{tr}\widetilde{A} \) .

Proposition 2. Soit \( f \in \mathcal{L}\left( E\right) \) , \( F \) un s.e.v strict de \( E \) (i.e. \( F \neq E \) et \( F \neq \{ 0\} \) ) stable par \( f \) . Soit \( g = {f}_{\mid F} \) la restriction de \( f \) à \( F \) . Alors \( g \in \mathcal{L}\left( F\right) \) et \( {P}_{g} \) divise \( {P}_{f} \) .

> Proposition 2. Let \( f \in \mathcal{L}\left( E\right) \) , \( F \) be a proper subspace of \( E \) (i.e. \( F \neq E \) and \( F \neq \{ 0\} \) ) stable under \( f \) . Let \( g = {f}_{\mid F} \) be the restriction of \( f \) to \( F \) . Then \( g \in \mathcal{L}\left( F\right) \) and \( {P}_{g} \) divides \( {P}_{f} \) .

Démonstration. \( F \) étant stable par \( f, g = {f}_{\mid F} \) est bien un endomorphisme de \( F \) . Ceci étant, soit \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) une base de \( F \) complétée en une base \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . La matrice de \( f \) dans \( \mathcal{B} \) a la forme

> Proof. Since \( F \) is stable under \( f, g = {f}_{\mid F} \) , it is indeed an endomorphism of \( F \) . That being said, let \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) be a basis of \( F \) extended to a basis \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . The matrix of \( f \) in \( \mathcal{B} \) has the form

\[
{\left\lbrack  f\right\rbrack  }_{\mathcal{B}} = \left( \begin{matrix} A & C \\  0 & B \end{matrix}\right) \;\text{ où }\;A = {\left\lbrack  g\right\rbrack  }_{\left( {e}_{1},\ldots ,{e}_{r}\right) },
\]

et donc

> and therefore

\[
{P}_{f} = \det \left( {{\left\lbrack  f\right\rbrack  }_{\mathcal{B}} - X{I}_{n}}\right)  = \left| \frac{A - X{I}_{r}}{0}\right| \frac{C}{B - X{I}_{n - r}}
\]

\[
= \det \left( {A - X{I}_{r}}\right)  \cdot  \det \left( {B - X{I}_{n - r}}\right)  = {P}_{g} \cdot  \det \left( {B - X{I}_{n - r}}\right) .
\]

Proposition 3. Soit \( f \in \mathcal{L}\left( E\right) \) un endomorphisme nilpotent. Alors \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n}(o\dot{u} \; n = \dim E) \) .

> Proposition 3. Let \( f \in \mathcal{L}\left( E\right) \) be a nilpotent endomorphism. Then \( {P}_{f} = {\left( -1\right) }^{n}{X}^{n}(o\dot{u} \; n = \dim E) \) .

Démonstration. Nous donnons deux méthodes de démonstration de ce résultat. Soit \( q \in {\mathbb{N}}^{ * } \) tel que \( {f}^{q} = 0 \) .

> Proof. We provide two methods for proving this result. Let \( q \in {\mathbb{N}}^{ * } \) be such that \( {f}^{q} = 0 \) .

Première méthode. Soit \( A \) la matrice de \( f \) dans une base de \( E,{\mathbb{K}}^{\prime } \) le corps des racines de \( {P}_{A}\left( X\right) \) . Dans \( {\mathbb{K}}^{\prime } \) , on peut écrire \( {P}_{A} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{i}\left( {X - {\lambda }_{i}}\right) \) . On peut bien sûr regarder \( A \) comme une matrice de \( {\mathcal{M}}_{n}\left( {\mathbb{K}}^{\prime }\right) \) . Pour tout \( i,{\lambda }_{i} \) est valeur propre de \( A \) , associé à un vecteur propre \( X \neq 0 \) . Un calcul rapide donne \( {A}^{q}X = {\lambda }_{i}^{q}X \) , et comme \( {A}^{q} = 0 \) , on en tire \( {\lambda }_{i} = 0 \) . Donc \( {P}_{A} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{i}\left( {X - {\lambda }_{i}}\right) = {\left( -1\right) }^{n}{X}^{n}. \)

> First method. Let \( A \) be the matrix of \( f \) in a basis of \( E,{\mathbb{K}}^{\prime } \), the splitting field of \( {P}_{A}\left( X\right) \). In \( {\mathbb{K}}^{\prime } \), we can write \( {P}_{A} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{i}\left( {X - {\lambda }_{i}}\right) \). We can of course view \( A \) as a matrix of \( {\mathcal{M}}_{n}\left( {\mathbb{K}}^{\prime }\right) \). For any \( i,{\lambda }_{i} \) is an eigenvalue of \( A \), associated with an eigenvector \( X \neq 0 \). A quick calculation gives \( {A}^{q}X = {\lambda }_{i}^{q}X \), and since \( {A}^{q} = 0 \), we derive \( {\lambda }_{i} = 0 \). Thus \( {P}_{A} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{i}\left( {X - {\lambda }_{i}}\right) = {\left( -1\right) }^{n}{X}^{n}. \)

Seconde méthode. Nous allons montrer ce résultat sans faire appel au corps des racines de \( {P}_{f} \) , en procédant par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) , montrons le au rang \( n \) . On a (det \( f{)}^{q} = \det \left( {f}^{q}\right) = 0 \) , donc det \( f = 0 \) et donc Ker \( f \neq \{ 0\} \) . Soit \( {e}_{1} \in \operatorname{Ker}f,{e}_{1} \neq 0 \) , de sorte que \( f\left( {e}_{1}\right) = 0 \) . Complétons \( {e}_{1} \) en une base \( B \) de E. Alors

> Second method. We will show this result without invoking the splitting field of \( {P}_{f} \), by proceeding by induction on \( n \in {\mathbb{N}}^{ * } \). For \( n = 1 \), it is obvious. Assume the result is true at rank \( n - 1 \), let us show it at rank \( n \). We have (det \( f{)}^{q} = \det \left( {f}^{q}\right) = 0 \), so det \( f = 0 \) and thus Ker \( f \neq \{ 0\} \). Let \( {e}_{1} \in \operatorname{Ker}f,{e}_{1} \neq 0 \), such that \( f\left( {e}_{1}\right) = 0 \). Complete \( {e}_{1} \) into a basis \( B \) of E. Then

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} 0 &  \times  \cdots  \times  \\  0 & M \end{matrix}\right) \;\text{ et }\;0 = {\left\lbrack  {f}^{q}\right\rbrack  }_{B} = {\left( {\left\lbrack  f\right\rbrack  }_{B}\right) }^{q} = \left( \begin{matrix} 0 &  \times  \cdots  \times  \\  0 & {M}^{q} \end{matrix}\right) ,
\]

donc \( {M}^{q} = 0 \) , et d’après l’hypothèse de récurrence \( {P}_{M} = {\left( -1\right) }^{n - 1}{X}^{n - 1} \) , donc

> therefore \( {M}^{q} = 0 \), and according to the induction hypothesis \( {P}_{M} = {\left( -1\right) }^{n - 1}{X}^{n - 1} \), thus

\[
{P}_{f}\left( X\right)  = \left| \begin{matrix}  - X &  \times  \cdots  \times  \\  0 & M - X{I}_{n - 1} \end{matrix}\right|  = \left( {-X}\right) {P}_{M} = {\left( -1\right) }^{n}{X}^{n}.
\]

Remarque 6. Un résultat plus fort sera donné à la remarque 6 page 187.

> Remark 6. A stronger result will be given in remark 6 on page 187.
