#### 3.3. Power series of endomorphisms

*Français : 3.3. Séries entières d'endomorphismes*

Ici, \( E \) désigne un \( \mathbb{K} \) -espace de Banach. Rappelons que dans ce cas, \( {\mathcal{L}}_{c}\left( E\right) \) , muni de la norme \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \) , est un \( \mathbb{K} \) -espace de Banach.

> Here, \( E \) denotes a \( \mathbb{K} \) -Banach space. Recall that in this case, \( {\mathcal{L}}_{c}\left( E\right) \) , equipped with the norm \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \) , is a \( \mathbb{K} \) -Banach space.

PROPOSITION 3. Soit \( z \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) la somme d’une série entière de rayon de convergence \( 0 < R \leq + \infty \) . Alors si \( f \in {\mathcal{L}}_{c}\left( E\right) ,\parallel f\parallel < R \) , la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{a}_{n}{f}^{n} \) converge et sa somme est élément de \( {\mathcal{L}}_{c}\left( E\right) \) . De plus, l’application

> PROPOSITION 3. Let \( z \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n} \) be the sum of a power series with radius of convergence \( 0 < R \leq + \infty \) . Then if \( f \in {\mathcal{L}}_{c}\left( E\right) ,\parallel f\parallel < R \) , the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{a}_{n}{f}^{n} \) converges and its sum is an element of \( {\mathcal{L}}_{c}\left( E\right) \) . Furthermore, the mapping

\[
\Gamma  = \left\{  {f \in  {\mathcal{L}}_{c}\left( E\right)  \mid  \parallel f\parallel  < R}\right\}   \rightarrow  {\mathcal{L}}_{c}\left( E\right) \;f \mapsto  \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{f}^{n}
\]

est continue.

> is continuous.

Démonstration. Comme \( {\mathcal{L}}_{c}\left( E\right) \) est un \( \mathbb{K} \) -espace de Banach, il suffit de montrer que si \( \parallel f\parallel < R \) , la série \( \sum {a}_{n}{f}^{n} \) converge absolument, ce qui est immédiat puisque \( \begin{Vmatrix}{{a}_{n}{f}^{n}}\end{Vmatrix} \leq \left| {a}_{n}\right| \cdot \parallel f{\parallel }^{n} \) et que \( \sum \left| {a}_{n}\right| \parallel f{\parallel }^{n} \) converge. La somme \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{f}^{n} \) existe donc et appartient à \( {\mathcal{L}}_{c}\left( E\right) \) .

> Proof. Since \( {\mathcal{L}}_{c}\left( E\right) \) is a \( \mathbb{K} \) -Banach space, it suffices to show that if \( \parallel f\parallel < R \) , the series \( \sum {a}_{n}{f}^{n} \) converges absolutely, which is immediate since \( \begin{Vmatrix}{{a}_{n}{f}^{n}}\end{Vmatrix} \leq \left| {a}_{n}\right| \cdot \parallel f{\parallel }^{n} \) and \( \sum \left| {a}_{n}\right| \parallel f{\parallel }^{n} \) converges. The sum \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{f}^{n} \) therefore exists and belongs to \( {\mathcal{L}}_{c}\left( E\right) \) .

Pour tout \( r \in \rbrack 0, R\left\lbrack \right. \) , on pose \( {\Gamma }_{r} = \left\{ {f \in {\mathcal{L}}_{c}\left( E\right) \mid \parallel f\parallel \leq r}\right\} \) . La série de fonctions \( f \mapsto \sum {a}_{n}{f}^{n} \) converge normalement sur \( {\Gamma }_{r} \) , puisque sur \( {\Gamma }_{r},\begin{Vmatrix}{{a}_{n}{f}^{n}}\end{Vmatrix} \leq \left| {a}_{n}\right| \cdot \parallel f{\parallel }^{n} \leq \left| {a}_{n}\right| {r}^{n} \) et \( \sum \left| {a}_{n}\right| {r}^{n} \) converge. Chacun des termes \( f \mapsto {a}_{n}{f}^{n} \) est continu sur \( {\Gamma }_{r} \) . On en déduit que \( f \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{f}^{n} \) est continue sur \( {\Gamma }_{r} \) , et ceci pour tout \( r \in \rbrack 0, R\lbrack \) , donc sur \( \Gamma \) .

> For any \( r \in \rbrack 0, R\left\lbrack \right. \), we set \( {\Gamma }_{r} = \left\{ {f \in {\mathcal{L}}_{c}\left( E\right) \mid \parallel f\parallel \leq r}\right\} \). The series of functions \( f \mapsto \sum {a}_{n}{f}^{n} \) converges normally on \( {\Gamma }_{r} \), since on \( {\Gamma }_{r},\begin{Vmatrix}{{a}_{n}{f}^{n}}\end{Vmatrix} \leq \left| {a}_{n}\right| \cdot \parallel f{\parallel }^{n} \leq \left| {a}_{n}\right| {r}^{n} \) and \( \sum \left| {a}_{n}\right| {r}^{n} \) converges. Each of the terms \( f \mapsto {a}_{n}{f}^{n} \) is continuous on \( {\Gamma }_{r} \). We deduce that \( f \mapsto \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{f}^{n} \) is continuous on \( {\Gamma }_{r} \), and this for any \( r \in \rbrack 0, R\lbrack \), therefore on \( \Gamma \).

Remarque 2. - Un résultat plus fin fait l'objet du problème 8 (page 221).

> Remark 2. - A more refined result is the subject of problem 8 (page 221).

- La proposition 3 reste vraie sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> - Proposition 3 remains true on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \).

Conséquence . Soit \( f \in {\mathcal{L}}_{c}\left( E\right) ,\parallel f\parallel < 1 \) . Alors \( {\operatorname{Id}}_{E} - f \) est inversible, et son inverse est \( g = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}^{n} \) . En effet, \( g \) existe d’après la proposition précédente et \( \left( {{\operatorname{Id}}_{E} - f}\right) g = g - {fg} = \; \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}^{n} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{f}^{n} = {\operatorname{Id}}_{E} \) ; de même, \( g\left( {{\operatorname{Id}}_{E} - f}\right) = {\operatorname{Id}}_{E} \) .

> Consequence. Let \( f \in {\mathcal{L}}_{c}\left( E\right) ,\parallel f\parallel < 1 \). Then \( {\operatorname{Id}}_{E} - f \) is invertible, and its inverse is \( g = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}^{n} \). Indeed, \( g \) exists according to the previous proposition and \( \left( {{\operatorname{Id}}_{E} - f}\right) g = g - {fg} = \; \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{f}^{n} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{f}^{n} = {\operatorname{Id}}_{E} \); likewise, \( g\left( {{\operatorname{Id}}_{E} - f}\right) = {\operatorname{Id}}_{E} \).

Exponentielles d'endomorphismes.

> Exponentials of endomorphisms.

Définition 1. Soit \( f \in {\mathcal{L}}_{c}\left( E\right) \) . D’après la proposition 3,

> Definition 1. Let \( f \in {\mathcal{L}}_{c}\left( E\right) \). According to proposition 3,

\[
g = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{n!}{f}^{n}
\]

existe et \( g \in {\mathcal{L}}_{c}\left( E\right) \) . L’endomorphisme \( g \) s’appelle l’exponentielle de \( f \) et on note \( g = \; \exp \left( f\right) = {e}^{f}. \)

> exists and \( g \in {\mathcal{L}}_{c}\left( E\right) \). The endomorphism \( g \) is called the exponential of \( f \) and is denoted \( g = \; \exp \left( f\right) = {e}^{f}. \)

Remarque 3. - On a \( \parallel \exp \left( f\right) \parallel \leq {e}^{\parallel f\parallel } \) . En effet, pour tout \( n \in \mathbb{N} \) ,

> Remark 3. - We have \( \parallel \exp \left( f\right) \parallel \leq {e}^{\parallel f\parallel } \). Indeed, for any \( n \in \mathbb{N} \),

\[
\begin{Vmatrix}{\mathop{\sum }\limits_{{k = 0}}^{n}\frac{1}{k!}{f}^{k}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = 0}}^{n}\frac{\parallel f{\parallel }^{k}}{k!}
\]

et le résultat se déduit en faisant tendre \( n \) vers \( + \infty \) .

> and the result is deduced by letting \( n \) tend towards \( + \infty \).

- D’après la proposition 3, l’application \( {\mathcal{L}}_{c}\left( E\right)  \rightarrow  {\mathcal{L}}_{c}\left( E\right) \;f \mapsto  \exp \left( f\right) \) est continue.

> - According to proposition 3, the mapping \( {\mathcal{L}}_{c}\left( E\right)  \rightarrow  {\mathcal{L}}_{c}\left( E\right) \;f \mapsto  \exp \left( f\right) \) is continuous.

Proposition 4. Soit \( u \in {\mathcal{L}}_{c}\left( E\right) \) . Soit \( v \in {\mathcal{L}}_{c}\left( E\right) \) inversible avec \( {v}^{-1} \in {\mathcal{L}}_{c}\left( E\right) \) . Alors \( \exp \left( {{v}^{-1}{uv}}\right) = {v}^{-1}\exp \left( u\right) v. \)

> Proposition 4. Let \( u \in {\mathcal{L}}_{c}\left( E\right) \) . Let \( v \in {\mathcal{L}}_{c}\left( E\right) \) be invertible with \( {v}^{-1} \in {\mathcal{L}}_{c}\left( E\right) \) . Then \( \exp \left( {{v}^{-1}{uv}}\right) = {v}^{-1}\exp \left( u\right) v. \)

Démonstration. Il suffit de remarquer que pour tout \( n \in \mathbb{N} \) on a \( {\left( {v}^{-1}uv\right) }^{n} = {v}^{-1}{u}^{n}v \) , ce qui entraîne

> Proof. It suffices to note that for all \( n \in \mathbb{N} \) we have \( {\left( {v}^{-1}uv\right) }^{n} = {v}^{-1}{u}^{n}v \) , which implies

\[
\exp \left( {{v}^{-1}{uv}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( {v}^{-1}uv\right) }^{n}}{n!} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{v}^{-1}{u}^{n}v}{n!} = {v}^{-1}\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{u}^{n}}{n!}}\right) v = {v}^{-1}\exp \left( u\right) v.
\]

La version matricielle de ce résultat est

> The matrix version of this result is

\[
\forall M \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\forall P \in  \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) ,\;\exp \left( {{P}^{-1}{MP}}\right)  = {P}^{-1}\exp \left( M\right) P.
\]

Deux matrices semblables ont donc des exponentielles semblables.

> Two similar matrices therefore have similar exponentials.

Proposition 5. Soient \( u, v \in {\mathcal{L}}_{c}\left( E\right) \) tels que \( {uv} = {vu} \) . Alors

> Proposition 5. Let \( u, v \in {\mathcal{L}}_{c}\left( E\right) \) be such that \( {uv} = {vu} \) . Then

\[
\exp \left( {u + v}\right)  = \exp \left( u\right) \exp \left( v\right)  = \exp \left( v\right) \exp \left( u\right) .
\]

Démonstration. La série \( \mathop{\sum }\limits_{n}{\left( u + v\right) }^{n}/n \) ! est en fait un produit de Cauchy des deux séries \( \mathop{\sum }\limits_{i}{u}^{i}/i \) ! et \( \mathop{\sum }\limits_{j}{v}^{j}/j \) !, dont nous redémontrons ici la convergence. On pose

> Proof. The series \( \mathop{\sum }\limits_{n}{\left( u + v\right) }^{n}/n \) ! is in fact a Cauchy product of the two series \( \mathop{\sum }\limits_{i}{u}^{i}/i \) ! and \( \mathop{\sum }\limits_{j}{v}^{j}/j \) !, for which we re-prove the convergence here. We set

\[
{\Delta }_{n} = \left( {\mathop{\sum }\limits_{{i = 0}}^{n}\frac{{u}^{i}}{i!}}\right) \left( {\mathop{\sum }\limits_{{j = 0}}^{n}\frac{{v}^{j}}{j!}}\right)  - \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( u + v\right) }^{k}}{k!}
\]

Il faut montrer que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{n} = 0 \) . Comme \( u \) et \( v \) commutent, on a

> We must show that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{n} = 0 \) . Since \( u \) and \( v \) commute, we have

\[
\forall k \in  {\mathbb{N}}^{ * },\;\frac{{\left( u + v\right) }^{k}}{k!} = \mathop{\sum }\limits_{{i + j = k}}\frac{1}{k!}\left( \begin{matrix} k \\  i \end{matrix}\right) {u}^{i}{v}^{j} = \mathop{\sum }\limits_{{i + j = k}}\frac{{u}^{i}}{i!} \cdot  \frac{{v}^{j}}{j!},
\]

donc

> therefore

\[
{\Delta }_{n} = \left( {\mathop{\sum }\limits_{{i = 0}}^{n}\frac{{u}^{i}}{i!}}\right) \left( {\mathop{\sum }\limits_{{j = 0}}^{n}\frac{{v}^{j}}{j!}}\right)  - \mathop{\sum }\limits_{{i + j \leq  n}}\frac{{u}^{i}}{i!} \cdot  \frac{{v}^{j}}{j!} = \mathop{\sum }\limits_{\substack{{n + 1 \leq  i + j \leq  {2n}} \\  {0 \leq  i, j \leq  n} }}\frac{{u}^{i}}{i!} \cdot  \frac{{v}^{j}}{j!}
\]

d'où on tire

> from which we derive

\[
\begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \leq  \mathop{\sum }\limits_{\substack{{n + 1 \leq  i + j \leq  {2n}} \\  {0 \leq  i, j \leq  n} }}\frac{\parallel u{\parallel }^{i}}{i!} \cdot  \frac{\parallel v{\parallel }^{j}}{j!} = \left( {\mathop{\sum }\limits_{{i = 0}}^{n}\frac{\parallel u{\parallel }^{i}}{i!}}\right) \left( {\mathop{\sum }\limits_{{j = 0}}^{n}\frac{\parallel v{\parallel }^{j}}{j!}}\right)  - \mathop{\sum }\limits_{{k = 0}}^{n}\frac{{\left( \parallel u\parallel  + \parallel v\parallel \right) }^{k}}{k!}.
\]

Lorsque \( n \) tend vers \( + \infty \) , ce dernier terme tend vers \( {e}^{\parallel u\parallel }{e}^{\parallel v\parallel } - {e}^{\parallel u\parallel + \parallel v\parallel } = 0 \) , donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{n} = \) 0, d’où \( \exp \left( {u + v}\right) = \exp \left( u\right) \exp \left( v\right) \) . On a de même \( \exp \left( v\right) \exp \left( u\right) = \exp \left( {v + u}\right) = \exp \left( {u + v}\right) \) . I

> When \( n \) tends to \( + \infty \) , this last term tends to \( {e}^{\parallel u\parallel }{e}^{\parallel v\parallel } - {e}^{\parallel u\parallel + \parallel v\parallel } = 0 \) , so \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{n} = \) 0, hence \( \exp \left( {u + v}\right) = \exp \left( u\right) \exp \left( v\right) \) . We similarly have \( \exp \left( v\right) \exp \left( u\right) = \exp \left( {v + u}\right) = \exp \left( {u + v}\right) \) . I

Conséquence . Pour tout \( u \in {\mathcal{L}}_{c}\left( E\right) ,{e}^{u}{e}^{-u} = {e}^{-u}{e}^{u} = {e}^{u - u} = {e}^{0} = {\mathrm{{Id}}}_{E} \) , donc \( {e}^{u} \) est inversible et \( {\left( {e}^{u}\right) }^{-1} = {e}^{-u} \) .

> Consequence. For all \( u \in {\mathcal{L}}_{c}\left( E\right) ,{e}^{u}{e}^{-u} = {e}^{-u}{e}^{u} = {e}^{u - u} = {e}^{0} = {\mathrm{{Id}}}_{E} \) , therefore \( {e}^{u} \) is invertible and \( {\left( {e}^{u}\right) }^{-1} = {e}^{-u} \) .

Remarque 4. - Si \( u \) et \( v \) ne commutent pas, la proposition précédente est fausse en général.

> Remark 4. - If \( u \) and \( v \) do not commute, the previous proposition is generally false.

- Si \( u \) et \( v \) commutent, alors \( u \) et \( \exp \left( v\right) \) commutent.

> - If \( u \) and \( v \) commute, then \( u \) and \( \exp \left( v\right) \) commute.

- On a souvent affaire aux exponentielles de matrices lors de l'étude des équations différentielles linéaires (voir le tome d'analyse). En effet, les exponentielles de matrices vérifient les propriétés suivantes :

> - We often deal with matrix exponentials when studying linear differential equations (see the analysis volume). Indeed, matrix exponentials satisfy the following properties:

- Soit \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . L’application \( \mathbb{R} \rightarrow  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \;t \mapsto  {e}^{tA} \) est dérivable, sa dérivée est \( A{e}^{tA} \) . Si \( X : \mathbb{R} \rightarrow  {\mathbb{K}}^{n} \) est dérivable et si \( \frac{dX}{dt} = {AX} \) , alors pour tout \( t \in  \mathbb{R} \) , \( X\left( t\right)  = {e}^{tA}X\left( 0\right) . \)

> - Let \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . The map \( \mathbb{R} \rightarrow  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \;t \mapsto  {e}^{tA} \) is differentiable, its derivative is \( A{e}^{tA} \) . If \( X : \mathbb{R} \rightarrow  {\mathbb{K}}^{n} \) is differentiable and if \( \frac{dX}{dt} = {AX} \) , then for all \( t \in  \mathbb{R} \) , \( X\left( t\right)  = {e}^{tA}X\left( 0\right) . \)

- Si \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est diagonalisable et a pour valeurs propres \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) , alors \( \exp \left( A\right) \) est diagonalisable et ses valeurs propres sont \( {e}^{{\alpha }_{1}},\ldots ,{e}^{{\alpha }_{n}} \) .

> - If \( A \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is diagonalizable and has eigenvalues \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) , then \( \exp \left( A\right) \) is diagonalizable and its eigenvalues are \( {e}^{{\alpha }_{1}},\ldots ,{e}^{{\alpha }_{n}} \) .

- Le calcul d'exponentielles de matrices est traité à la partie 3 page 206 du présent chapitre.

> - The calculation of matrix exponentials is covered in part 3 on page 206 of this chapter.
