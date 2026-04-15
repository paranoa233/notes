### 2. Some properties of Hilbert spaces

*Français : 2. Quelques propriétés des espaces de Hilbert*

Les deux exercices qui suivent ont pour but de présenter des propriétés intéressantes des espaces de Hilbert. Ils sont indépendants. Il est nécessaire, pour les traiter, d'avoir pris connaissance des résultats du problème précédent.

> The following two exercises aim to present interesting properties of Hilbert spaces. They are independent. To work through them, it is necessary to have read the results of the previous problem.

EXERCICE 1 (TOPOLOGIE FAIBLE DANS UN ESPACE DE HILBERT). Soit \( H \) un espace de Hilbert dont le produit scalaire est noté ⟨, ⟩. Soit \( \left( {x}_{n}\right) \) une suite de points de \( H \) ,

> EXERCISE 1 (WEAK TOPOLOGY IN A HILBERT SPACE). Let \( H \) be a Hilbert space whose inner product is denoted by ⟨, ⟩. Let \( \left( {x}_{n}\right) \) be a sequence of points in \( H \) ,

- on dit que \( \left( {x}_{n}\right) \) converge fortement vers \( x \in  H \) si \( \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\begin{Vmatrix}{x - {x}_{n}}\end{Vmatrix} = 0 \) (c’est la convergence usuelle);

> - we say that \( \left( {x}_{n}\right) \) converges strongly to \( x \in  H \) if \( \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\begin{Vmatrix}{x - {x}_{n}}\end{Vmatrix} = 0 \) (this is the usual convergence);

- on dit que \( \left( {x}_{n}\right) \) converge faiblement vers \( x \in  H \) si pour tout \( y \in  H,\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {{x}_{n}, y}\right\rangle   = \; \langle x, y\rangle \) .

> - we say that \( \left( {x}_{n}\right) \) converges weakly to \( x \in  H \) if for all \( y \in  H,\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {{x}_{n}, y}\right\rangle   = \; \langle x, y\rangle \) .

1/ a) Si \( \left( {x}_{n}\right) \) converge faiblement vers \( x \) , montrer que \( x \) est la seule limite faible possible de \( \left( {x}_{n}\right) \) . Si de plus il existe \( M > 0 \) tel que \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) pour tout \( n \in \mathbb{N} \) , montrer que \( \parallel x\parallel \leq M. \)

> 1/ a) If \( \left( {x}_{n}\right) \) converges weakly to \( x \) , show that \( x \) is the only possible weak limit of \( \left( {x}_{n}\right) \) . If, in addition, there exists \( M > 0 \) such that \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) for all \( n \in \mathbb{N} \) , show that \( \parallel x\parallel \leq M. \)

b) \( \mathrm{{Si}}\left( {x}_{n}\right) \) converge fortement vers \( x \) , montrer que \( \left( {x}_{n}\right) \) converge faiblement vers \( x \) . La réciproque est-elle vraie ?

> b) \( \mathrm{{Si}}\left( {x}_{n}\right) \) converges strongly to \( x \) , show that \( \left( {x}_{n}\right) \) converges weakly to \( x \) . Is the converse true?

c) \( \operatorname{Si}\left( {x}_{n}\right) \) converge faiblement vers \( x \) et si \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x}_{n}\end{Vmatrix} = \parallel x\parallel \) , montrer que \( \left( {x}_{n}\right) \) converge fortement vers \( x \) .

> c) \( \operatorname{Si}\left( {x}_{n}\right) \) converges weakly to \( x \) and if \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{x}_{n}\end{Vmatrix} = \parallel x\parallel \) , show that \( \left( {x}_{n}\right) \) converges strongly to \( x \) .

2/ Compacité faible de la boule unité fermée. Soit \( \left( {x}_{n}\right) \) une suite bornée de \( H \) . On veut montrer qu’il existe une sous-suite de \( \left( {x}_{n}\right) \) qui converge faiblement.

> 2/ Weak compactness of the closed unit ball. Let \( \left( {x}_{n}\right) \) be a bounded sequence in \( H \) . We want to show that there exists a subsequence of \( \left( {x}_{n}\right) \) that converges weakly.

a) Montrer qu’il existe une sous-suite \( \left( {y}_{n}\right) = \left( {x}_{\varphi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) telle que pour tout \( k \in \mathbb{N} \) , la suite \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in \mathbb{N}} \) soit convergente.

> a) Show that there exists a subsequence \( \left( {y}_{n}\right) = \left( {x}_{\varphi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) such that for all \( k \in \mathbb{N} \) , the sequence \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in \mathbb{N}} \) is convergent.

b) Si \( E \) est l’adhérence du s.e.v \( \operatorname{Vect}{\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) , montrer

> b) If \( E \) is the closure of the subspace \( \operatorname{Vect}{\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) , show

\[
\exists !u \in  E,\forall v \in  E,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {{y}_{n}, v}\right\rangle   = \langle u, v\rangle .
\]

c) En déduire que \( \left( {y}_{n}\right) \) converge faiblement vers \( u \) .

> c) Deduce that \( \left( {y}_{n}\right) \) converges weakly to \( u \) .

Solution. \( \mathbf{1}/\mathbf{a} \) ) Soit \( {x}^{\prime } \in H \) tel que pour tout \( y \in H,\mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{x}_{n}, y}\right\rangle = \left\langle {{x}^{\prime }, y}\right\rangle \) . Alors pour tout \( y \in H,\langle x, y\rangle = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{x}_{n}, y}\right\rangle = \left\langle {{x}^{\prime }, y}\right\rangle \) , donc \( \left\langle {x - {x}^{\prime }, y}\right\rangle = 0 \) pour tout \( y \in H \) . En particulier \( \left\langle {x - {x}^{\prime }, x - {x}^{\prime }}\right\rangle = {\begin{Vmatrix}x - {x}^{\prime }\end{Vmatrix}}^{2} = 0 \) , donc \( x = {x}^{\prime }. \)

> Solution. \( \mathbf{1}/\mathbf{a} \) ) Let \( {x}^{\prime } \in H \) be such that for all \( y \in H,\mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{x}_{n}, y}\right\rangle = \left\langle {{x}^{\prime }, y}\right\rangle \) . Then for all \( y \in H,\langle x, y\rangle = \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{x}_{n}, y}\right\rangle = \left\langle {{x}^{\prime }, y}\right\rangle \) , so \( \left\langle {x - {x}^{\prime }, y}\right\rangle = 0 \) for all \( y \in H \) . In particular \( \left\langle {x - {x}^{\prime }, x - {x}^{\prime }}\right\rangle = {\begin{Vmatrix}x - {x}^{\prime }\end{Vmatrix}}^{2} = 0 \) , so \( x = {x}^{\prime }. \)

Si \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) pour tout \( n \) , alors pour tout \( n,\left| \left\langle {{x}_{n}, x}\right\rangle \right| \leq \begin{Vmatrix}{x}_{n}\end{Vmatrix} \cdot \parallel x\parallel \leq M\parallel x\parallel \) . Comme \( \left( \left\langle {{x}_{n}, x}\right\rangle \right) \) converge vers \( \langle x, x\rangle = \parallel x{\parallel }^{2} \) , on en déduit \( \parallel x{\parallel }^{2} \leq M\parallel x\parallel \) donc \( \parallel x\parallel \leq M \) .

> If \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) for all \( n \) , then for all \( n,\left| \left\langle {{x}_{n}, x}\right\rangle \right| \leq \begin{Vmatrix}{x}_{n}\end{Vmatrix} \cdot \parallel x\parallel \leq M\parallel x\parallel \) . Since \( \left( \left\langle {{x}_{n}, x}\right\rangle \right) \) converges to \( \langle x, x\rangle = \parallel x{\parallel }^{2} \) , we deduce \( \parallel x{\parallel }^{2} \leq M\parallel x\parallel \) so \( \parallel x\parallel \leq M \) .

b) C’est évident car pour tout \( y \in H,\left| {\left\langle {{x}_{n}, y}\right\rangle - \langle x, y\rangle }\right| = \left| \left\langle {{x}_{n} - x, y}\right\rangle \right| \leq \begin{Vmatrix}{{x}_{n} - x}\end{Vmatrix} \cdot \parallel y\parallel \) .

> b) This is obvious because for all \( y \in H,\left| {\left\langle {{x}_{n}, y}\right\rangle - \langle x, y\rangle }\right| = \left| \left\langle {{x}_{n} - x, y}\right\rangle \right| \leq \begin{Vmatrix}{{x}_{n} - x}\end{Vmatrix} \cdot \parallel y\parallel \) .

Par contre, la réciproque est fausse. Par exemple, dans un espace de Hilbert séparable dont \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) est une base hilbertienne (par exemple \( H = {\ell }^{2} \) , espace des suites réelles \( \left( {x}_{n}\right) \) telles que \( \sum {x}_{n}^{2} < + \infty ) \) , la suite \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) converge faiblement vers 0 car si \( y \in H \) , on a \( y = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left\langle {y,{e}_{n}}\right\rangle {e}_{n} \) et \( \sum {\left\langle y,{e}_{n}\right\rangle }^{2} \) converge, donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {y,{e}_{n}}\right\rangle = 0 \) , Bien sûr, il est clair que \( \left( {e}_{n}\right) \) ne converge pas fortement (si c'était le cas, sa limite forte serait sa limite faible donc 0, ce qui est impossible puisque \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} = 1 \) pour tout \( n \) ).

> However, the converse is false. For example, in a separable Hilbert space where \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) is a Hilbert basis (for example \( H = {\ell }^{2} \) , the space of real sequences \( \left( {x}_{n}\right) \) such that \( \sum {x}_{n}^{2} < + \infty ) \) , the sequence \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) converges weakly to 0 because if \( y \in H \) , we have \( y = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left\langle {y,{e}_{n}}\right\rangle {e}_{n} \) and \( \sum {\left\langle y,{e}_{n}\right\rangle }^{2} \) converges, so \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {y,{e}_{n}}\right\rangle = 0 \) , Of course, it is clear that \( \left( {e}_{n}\right) \) does not converge strongly (if it did, its strong limit would be its weak limit, i.e., 0, which is impossible since \( \begin{Vmatrix}{e}_{n}\end{Vmatrix} = 1 \) for all \( n \) ).

c) Il suffit d’écrire \( {\begin{Vmatrix}{x}_{n} - x\end{Vmatrix}}^{2} = \parallel x{\parallel }^{2} + {\begin{Vmatrix}{x}_{n}\end{Vmatrix}}^{2} - 2\left\langle {x,{x}_{n}}\right\rangle \) .

> c) It suffices to write \( {\begin{Vmatrix}{x}_{n} - x\end{Vmatrix}}^{2} = \parallel x{\parallel }^{2} + {\begin{Vmatrix}{x}_{n}\end{Vmatrix}}^{2} - 2\left\langle {x,{x}_{n}}\right\rangle \) .

2 / a) Comme \( \left( {x}_{n}\right) \) est bornée, la suite réelle \( {\left( \left\langle {x}_{n},{x}_{1}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) est bornée. On peut donc extraire une sous-suite \( \left( {x}_{{\varphi }_{1}\left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) telle que la suite \( {\left( \left\langle {x}_{{\varphi }_{1}\left( n\right) },{x}_{1}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge.

> 2 / a) Since \( \left( {x}_{n}\right) \) is bounded, the real sequence \( {\left( \left\langle {x}_{n},{x}_{1}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) is bounded. We can therefore extract a subsequence \( \left( {x}_{{\varphi }_{1}\left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) such that the sequence \( {\left( \left\langle {x}_{{\varphi }_{1}\left( n\right) },{x}_{1}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges.

De même, la suite réelle ( \( {\left\langle {x}_{{\varphi }_{1}\left( n\right) },{x}_{2}\rangle \right\rangle }_{n \in {\mathbb{N}}^{ * }} \) est bornée, on peut donc extraire une sous-suite \( {\left( {x}_{{\varphi }_{1} \circ {\varphi }_{2}\left( n\right) }\left( n\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) de \( \left( {x}_{{\varphi }_{1}\left( n\right) }\right) \) telle que la suite \( {\left( \left\langle {x}_{{\varphi }_{1} \circ {\varphi }_{2}\left( n\right) },{x}_{2}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge.

> Similarly, the real sequence ( \( {\left\langle {x}_{{\varphi }_{1}\left( n\right) },{x}_{2}\rangle \right\rangle }_{n \in {\mathbb{N}}^{ * }} \) is bounded, so we can extract a subsequence \( {\left( {x}_{{\varphi }_{1} \circ {\varphi }_{2}\left( n\right) }\left( n\right) \right) }_{n \in {\mathbb{N}}^{ * }} \) of \( \left( {x}_{{\varphi }_{1}\left( n\right) }\right) \) such that the sequence \( {\left( \left\langle {x}_{{\varphi }_{1} \circ {\varphi }_{2}\left( n\right) },{x}_{2}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges.

En procédant par récurrence, on construit ainsi pour tout \( k \) une sous-suite \( {\left( {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) }\right) }_{n \in {\mathbb{N}}^{ * }} \) telle que la suite \( {\left( \left\langle {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) },{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge.

> By proceeding by induction, we thus construct for every \( k \) a subsequence \( {\left( {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) }\right) }_{n \in {\mathbb{N}}^{ * }} \) such that the sequence \( {\left( \left\langle {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) },{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges.

On définit alors la suite \( \left( {y}_{n}\right) \) par \( {y}_{n} = {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{n}\left( n\right) } \) pour tout \( n \) (procédé d’extraction diagonal). Pour \( n \geq k \) , la suite \( \left( {y}_{n}\right) \) est une sous-suite de \( {\left( {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) }\right) }_{n \in {\mathbb{N}}^{ * }} \) , donc la suite \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge, et ceci pour tout \( k \in {\mathbb{N}}^{ * } \) .

> We then define the sequence \( \left( {y}_{n}\right) \) by \( {y}_{n} = {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{n}\left( n\right) } \) for every \( n \) (diagonal extraction process). For \( n \geq k \) , the sequence \( \left( {y}_{n}\right) \) is a subsequence of \( {\left( {x}_{{\varphi }_{1} \circ \cdots \circ {\varphi }_{k}\left( n\right) }\right) }_{n \in {\mathbb{N}}^{ * }} \) , so the sequence \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges, and this for every \( k \in {\mathbb{N}}^{ * } \) .

b) Pour tout \( k \) , la suite \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge. Il est donc clair que pour tout \( v \in F = \; \operatorname{Vect}{\left( {x}_{k}\right) }_{k \in {\mathbb{N}}^{ * }} \) , la suite \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge.

> b) For all \( k \), the sequence \( {\left( \left\langle {y}_{n},{x}_{k}\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges. It is therefore clear that for all \( v \in F = \; \operatorname{Vect}{\left( {x}_{k}\right) }_{k \in {\mathbb{N}}^{ * }} \), the sequence \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges.

Montrons que cette propriété reste vraie si \( v \in E = \bar{F} \) . Soit \( v \in E \) . Soit \( \varepsilon > 0 \) et \( w \in F \) tel que \( \parallel v - w\parallel < \varepsilon \) . La suite \( {\left( \left\langle {y}_{n}, w\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converge. Elle est donc de Cauchy, ce qui entraîne

> Let us show that this property remains true if \( v \in E = \bar{F} \). Let \( v \in E \). Let \( \varepsilon > 0 \) and \( w \in F \) such that \( \parallel v - w\parallel < \varepsilon \). The sequence \( {\left( \left\langle {y}_{n}, w\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) converges. It is therefore Cauchy, which implies

\[
\exists N \in  \mathbb{N},\forall p, q \geq  N,\;\left| {\left\langle  {{y}_{p}, w}\right\rangle   - \left\langle  {{y}_{q}, w}\right\rangle  }\right|  < \varepsilon .
\]

On en déduit

> We deduce from this

\[
\forall p, q \geq  N,\;\left| {\left\langle  {{y}_{p}, v}\right\rangle   - \left\langle  {{y}_{q}, v}\right\rangle  }\right|  \leq  \left| \left\langle  {{y}_{p}, v - w}\right\rangle  \right|  + \left| {\left\langle  {{y}_{p}, w}\right\rangle   - \left\langle  {{y}_{q}, w}\right\rangle  }\right|  + \left| \left\langle  {{y}_{q}, v - w}\right\rangle  \right|  \leq  {M\varepsilon } + \varepsilon  + {M\varepsilon },
\]

où \( M \) est un majorant de \( \left( \begin{Vmatrix}{x}_{n}\end{Vmatrix}\right) \) (donc de \( \left( \begin{Vmatrix}{y}_{n}\end{Vmatrix}\right) \) ). Donc \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) est une suite de Cauchy, donc elle converge car \( H \) est complet.

> where \( M \) is an upper bound of \( \left( \begin{Vmatrix}{x}_{n}\end{Vmatrix}\right) \) (and thus of \( \left( \begin{Vmatrix}{y}_{n}\end{Vmatrix}\right) \)). Therefore \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) is a Cauchy sequence, so it converges because \( H \) is complete.

Pour tout \( v \in E \) , on note \( \ell \left( v\right) \) la limite de la suite \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \) . Il est clair que l’application \( \ell : E \rightarrow \mathbb{R} \) ainsi définie est linéaire. Elle est continue car \( \left( {y}_{n}\right) \) est bornée. Le s.e.v \( E \) , fermé dans un complet, est complet. Muni du produit scalaire sur \( H \) , c’est donc un espace de Hilbert, donc d’après le théorème de représentation de Riesz, il existe un unique vecteur \( u \) de \( E \) tel que \( \ell \left( v\right) = \langle u, v\rangle \) pour tout \( v \in E \) . Ceci s’écrit aussi

> For all \( v \in E \), we denote by \( \ell \left( v\right) \) the limit of the sequence \( {\left( \left\langle {y}_{n}, v\right\rangle \right) }_{n \in {\mathbb{N}}^{ * }} \). It is clear that the mapping \( \ell : E \rightarrow \mathbb{R} \) thus defined is linear. It is continuous because \( \left( {y}_{n}\right) \) is bounded. The subspace \( E \), closed in a complete space, is complete. Equipped with the inner product on \( H \), it is therefore a Hilbert space, so according to the Riesz representation theorem, there exists a unique vector \( u \) of \( E \) such that \( \ell \left( v\right) = \langle u, v\rangle \) for all \( v \in E \). This can also be written as

\[
\exists !u \in  E,\forall v \in  E,\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {{y}_{n}, v}\right\rangle   = \langle u, v\rangle .
\]

c) Comme \( E \) est un s.e.v fermé de \( H \) , on sait que \( E \oplus {E}^{ \bot } = H \) . Soit \( v \in H \) , et soit \( \left( {{v}_{1},{v}_{2}}\right) \in E \times \; {E}^{ \bot } \) tel que \( v = {v}_{1} + {v}_{2} \) . Pour tout \( n \) , on a \( {y}_{n} \in E \) , donc \( \left\langle {{y}_{n}, v}\right\rangle = \left\langle {{y}_{n},{v}_{1}}\right\rangle \) . Or \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{y}_{n},{v}_{1}}\right\rangle = \; \left\langle {u,{v}_{1}}\right\rangle \) car \( {v}_{1} \in E \) , et comme \( u \in E \) , on a \( \left\langle {u,{v}_{1}}\right\rangle = \langle u, v\rangle \) . On en déduit lim \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{y}_{n}, v}\right\rangle = \langle u, v\rangle \) , et ceci pour tout \( v \in H \) , d’où le résultat.

> c) Since \( E \) is a closed subspace of \( H \), we know that \( E \oplus {E}^{ \bot } = H \). Let \( v \in H \), and let \( \left( {{v}_{1},{v}_{2}}\right) \in E \times \; {E}^{ \bot } \) such that \( v = {v}_{1} + {v}_{2} \). For all \( n \), we have \( {y}_{n} \in E \), so \( \left\langle {{y}_{n}, v}\right\rangle = \left\langle {{y}_{n},{v}_{1}}\right\rangle \). However, \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{y}_{n},{v}_{1}}\right\rangle = \; \left\langle {u,{v}_{1}}\right\rangle \) because \( {v}_{1} \in E \), and since \( u \in E \), we have \( \left\langle {u,{v}_{1}}\right\rangle = \langle u, v\rangle \). We deduce lim \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {{y}_{n}, v}\right\rangle = \langle u, v\rangle \), and this for all \( v \in H \), hence the result.

Remarque. A l'aide du théorème de Banach-Steinhaus (voir l'exercice 7 page 424 dans l’annexe A), on montre facilement que si \( \left( {x}_{n}\right) \) converge faiblement, alors \( \left( {x}_{n}\right) \) est bornée (considérer les formes linéaires \( {f}_{n} : H \rightarrow \mathbb{R}\;x \mapsto \left\langle {{x}_{n}, x}\right\rangle ) \) .

> Remark. Using the Banach-Steinhaus theorem (see exercise 7 page 424 in appendix A), it is easy to show that if \( \left( {x}_{n}\right) \) converges weakly, then \( \left( {x}_{n}\right) \) is bounded (consider the linear forms \( {f}_{n} : H \rightarrow \mathbb{R}\;x \mapsto \left\langle {{x}_{n}, x}\right\rangle ) \).

La convergence faible permet de définir la topologie faible sur \( H \) (un ensemble est faiblement fermé si toute limite faible de points de cet ensemble reste dans cet ensemble). Si \( H \) est séparable, la topologie faible sur la boule unité de \( H \) est métrisable (i. e. il existe une distance d sur \( H \) telle que la topologie induite par d est la topologie faible - prendre pour \( \mathrm{d} \) la fonction \( \mathrm{d}\left( {u, v}\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{{2}^{n}}\left| \left\langle {{e}_{n}, u - v}\right\rangle \right| \) , où \( \left( {e}_{n}\right) \) est une base hilbertienne). On comprend alors mieux le terme de compacité faible, car dans un espace métrique, la propriété de Bolzano Weierstrass est équivalente à la propriété de Borel-Lebesgue.

> Weak convergence allows for the definition of the weak topology on \( H \) (a set is weakly closed if every weak limit of points in this set remains in this set). If \( H \) is separable, the weak topology on the unit ball of \( H \) is metrizable (i.e., there exists a distance d on \( H \) such that the topology induced by d is the weak topology - take for \( \mathrm{d} \) the function \( \mathrm{d}\left( {u, v}\right) = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{1}{{2}^{n}}\left| \left\langle {{e}_{n}, u - v}\right\rangle \right| \), where \( \left( {e}_{n}\right) \) is a Hilbertian basis). The term weak compactness is then better understood, because in a metric space, the Bolzano-Weierstrass property is equivalent to the Borel-Lebesgue property.

EXERCICE 2 (OPÉRATEURS COMPACTS DANS UN ESPACE DE HILBERT).

> EXERCISE 2 (COMPACT OPERATORS IN A HILBERT SPACE).

Soit \( E \) un \( \mathbb{R} \) -espace de Banach. On note \( {\mathcal{L}}_{c}\left( E\right) \) l’e.v des endomorphismes continus de \( E \) , muni de la norme \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \) .

> Let \( E \) be a \( \mathbb{R} \) -Banach space. We denote by \( {\mathcal{L}}_{c}\left( E\right) \) the vector space of continuous endomorphisms of \( E \), equipped with the norm \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\parallel f\left( x\right) \parallel \).

Un endomorphisme (on dit aussi opérateur) \( f \) sur \( E \) est dit compact si \( \overline{f\left( B\right) } \) est compact (où \( B \) désigne la boule unité fermée de \( E \) ). On note \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) l’ensemble des opérateurs compacts de \( E \) .

> An endomorphism (also called an operator) \( f \) on \( E \) is said to be compact if \( \overline{f\left( B\right) } \) is compact (where \( B \) denotes the closed unit ball of \( E \)). We denote by \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) the set of compact operators on \( E \).

##### I. Generalities.

*Français : I. Généralités.*

1 / a) Montrer \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \subset {\mathcal{L}}_{c}\left( E\right) \) .

> 1 / a) Show \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \subset {\mathcal{L}}_{c}\left( E\right) \) .

b) Soit \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Montrer que les trois assertions suivantes sont équivalentes :

> b) Let \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Show that the following three assertions are equivalent:

(i) \( f \) est un opérateur compact ;

> (i) \( f \) is a compact operator;

(ii) pour tout \( \varepsilon > 0 \) , on peut recouvrir \( f\left( B\right) \) par un nombre fini de boules ouvertes de rayon \( \varepsilon \) ;

> (ii) for any \( \varepsilon > 0 \) , one can cover \( f\left( B\right) \) with a finite number of open balls of radius \( \varepsilon \) ;

(iii) pour toute suite \( \left( {x}_{n}\right) \) bornée de \( E \) , on peut extraire de la suite \( \left\lbrack {f\left( {x}_{n}\right) }\right\rbrack \) une sous-suite convergente.

> (iii) for any bounded sequence \( \left( {x}_{n}\right) \) in \( E \) , one can extract a convergent subsequence from the sequence \( \left\lbrack {f\left( {x}_{n}\right) }\right\rbrack \) .

(pour (ii), on pourra utiliser le résultat de l'exercice 2 page 32).

> (for (ii), one may use the result of exercise 2 page 32).

2/ a) Montrer que \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) est un s.e.v fermé de \( {\mathcal{L}}_{c}\left( E\right) \) .

> 2/ a) Show that \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) is a closed subspace of \( {\mathcal{L}}_{c}\left( E\right) \) .

b) Si \( f \in {\mathcal{L}}_{c}\left( E\right) \) est de rang fini (i.e. si \( f\left( E\right) \) est de dimension finie), montrer que \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) .

> b) If \( f \in {\mathcal{L}}_{c}\left( E\right) \) is of finite rank (i.e., if \( f\left( E\right) \) is finite-dimensional), show that \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) .

II. Opérateurs compacts dans un espace de Hilbert. Dorénavant, \( E \) désigne un \( \mathbb{R} \) -espace de Hilbert.

> II. Compact operators in a Hilbert space. Henceforth, \( E \) denotes a \( \mathbb{R} \) -Hilbert space.

1/ a) Si \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , montrer que \( f \) est limite d’opérateurs continus de rang fini. b) Si \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , montrer que son adjoint \( {f}^{ * } \) est un opérateur compact.

> 1/ a) If \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , show that \( f \) is the limit of continuous finite-rank operators. b) If \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , show that its adjoint \( {f}^{ * } \) is a compact operator.

c) Si \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) est une suite de vecteurs de norme 1, deux-à-deux orthogonaux, et si \( f \in \; {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , montrer \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {e}_{n}\right) = 0 \) .

> c) If \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) is a sequence of unit vectors, pairwise orthogonal, and if \( f \in \; {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , show \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {e}_{n}\right) = 0 \) .

2 / Valuers propres d’un opérateur compact dans un Hilbert. Soit \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . On note

> 2 / Eigenvalues of a compact operator in a Hilbert space. Let \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . We denote

\[
\Lambda \left( f\right)  = \{ \lambda  \in  \mathbb{R} \mid  \exists x \neq  0,\;f\left( x\right)  = {\lambda x}\}
\]

(ensemble des valeurs propres de \( f \) ).

> (set of eigenvalues of \( f \) ).

a) Si \( \lambda \in \Lambda \left( f\right) \) et \( \lambda \neq 0 \) , montrer que le sous-espace propre Ker \( \left( {f - \lambda \text{ Id }}\right) \) correspondant est de dimension finie.

> a) If \( \lambda \in \Lambda \left( f\right) \) and \( \lambda \neq 0 \) , show that the corresponding eigenspace Ker \( \left( {f - \lambda \text{ Id }}\right) \) is finite-dimensional.

b) Montrer que 0 est le seul point d’accumulation possible de \( \Lambda \left( f\right) \) . En déduire que \( \Lambda \left( f\right) \) est au plus dénombrable.

> b) Show that 0 is the only possible accumulation point of \( \Lambda \left( f\right) \) . Deduce that \( \Lambda \left( f\right) \) is at most countable.

III. Opérateurs compacts autoadjoints. Soit \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) autoadjoint (i.e \( \forall x, y \in \; E,\langle f\left( x\right) , y\rangle = \langle x, f\left( y\right) \rangle ). \)

> III. Self-adjoint compact operators. Let \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) be self-adjoint (i.e., \( \forall x, y \in \; E,\langle f\left( x\right) , y\rangle = \langle x, f\left( y\right) \rangle ). \)

1/ a) Montrer qu’il existe une suite \( \left( {x}_{n}\right) \) de vecteurs de \( E \) , tous de norme 1, telle que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| \left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle \right| = \parallel f\parallel . \)

> 1/ a) Show that there exists a sequence \( \left( {x}_{n}\right) \) of vectors in \( E \) , all of norm 1, such that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| \left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle \right| = \parallel f\parallel . \)

b) Si \( f \neq 0 \) , en déduire que \( f \) a au moins une valeur propre non nulle.

> b) If \( f \neq 0 \) , deduce that \( f \) has at least one non-zero eigenvalue.

2/ a) Montrer que deux sous-espaces propres de \( f \) pour des valeurs propres distinctes sont orthogonaux.

> 2/ a) Show that two eigenspaces of \( f \) corresponding to distinct eigenvalues are orthogonal.

b) Soit \( G \) le s.e.v engendré (algébriquement) par les vecteurs propres de \( f \) associés à des valeurs propres non nulles. En notant \( F = \bar{G} \) , montrer que \( {F}^{ \bot } = \operatorname{Ker}f \) .

> b) Let \( G \) be the subspace (algebraically) spanned by the eigenvectors of \( f \) associated with non-zero eigenvalues. Denoting \( F = \bar{G} \) , show that \( {F}^{ \bot } = \operatorname{Ker}f \) .

c) On suppose que \( \Lambda \left( f\right) \) n’est pas fini. Montrer qu’il existe une famille orthonormale dénombrable \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) de vecteurs propres, associés à des valeurs propres non nulles, telle que

> c) Suppose \( \Lambda \left( f\right) \) is not finite. Show that there exists a countable orthonormal family \( {\left( {e}_{n}\right) }_{n \in \mathbb{N}} \) of eigenvectors, associated with non-zero eigenvalues, such that

\[
\forall x \in  E,\exists y \in  \operatorname{Ker}f,\;x = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left\langle  {x,{e}_{n}}\right\rangle  {e}_{n} + y.
\]

Que dire si \( \Lambda \left( f\right) \) est fini ?

> What can be said if \( \Lambda \left( f\right) \) is finite?

Solution. I. \( 1/ \) a) Soit \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . L’ensemble \( \overline{f\left( B\right) } \) est compact, donc borné, donc \( f\left( B\right) \) est borné, donc \( f \) est continue, d’où le résultat.

> Solution. I. \( 1/ \) a) Let \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . The set \( \overline{f\left( B\right) } \) is compact, therefore bounded, therefore \( f\left( B\right) \) is bounded, therefore \( f \) is continuous, hence the result.

b) Montrons d'abord que les assertions (i) et (ii) sont équivalentes.

> b) Let us first show that assertions (i) and (ii) are equivalent.

— \( \left( i\right) \Rightarrow \left( {ii}\right) \) est clair car \( \overline{f\left( B\right) } \) étant compact, on peut toujours, pour tout \( \varepsilon > 0 \) , recouvrir \( \overline{f\left( B\right) } \) (donc \( f\left( B\right) \) ) par un nombre fini de boules ouvertes de rayon \( \varepsilon \) .

> — \( \left( i\right) \Rightarrow \left( {ii}\right) \) is clear because since \( \overline{f\left( B\right) } \) is compact, one can always, for any \( \varepsilon > 0 \) , cover \( \overline{f\left( B\right) } \) (and thus \( f\left( B\right) \) ) with a finite number of open balls of radius \( \varepsilon \) .

- \( \left( {ii}\right)  \Rightarrow  \left( i\right) \) . Soit \( \varepsilon  > 0 \) . On peut recouvrir \( f\left( B\right) \) par un nombre fini de boules de rayon \( \varepsilon /2 : f\left( B\right)  \subset  { \cup  }_{1 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon /2}\right) \) . Ainsi, \( \overline{f\left( B\right) } \subset  { \cup  }_{1 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) , et comme ceci est possible pour tout \( \varepsilon  > 0,\overline{f\left( B\right) } \) est précompact (voir l’exercice 2 page 32). De plus \( \overline{f\left( B\right) } \) , fermé dans le complet \( E \) , est complet. On en déduit que \( \overline{f\left( B\right) } \) est compact.

> - \( \left( {ii}\right)  \Rightarrow  \left( i\right) \) . Let \( \varepsilon  > 0 \) . One can cover \( f\left( B\right) \) with a finite number of balls of radius \( \varepsilon /2 : f\left( B\right)  \subset  { \cup  }_{1 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon /2}\right) \) . Thus, \( \overline{f\left( B\right) } \subset  { \cup  }_{1 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right) \) , and as this is possible for any \( \varepsilon  > 0,\overline{f\left( B\right) } \) , it is precompact (see exercise 2 on page 32). Furthermore, \( \overline{f\left( B\right) } \) , closed in the complete space \( E \) , is complete. We deduce that \( \overline{f\left( B\right) } \) is compact.

Montrons maintenant l'équivalence entre les assertions (i) et (iii).

> Let us now show the equivalence between assertions (i) and (iii).

— (i) \( \Rightarrow \) (iii). Soit \( \left( {x}_{n}\right) \) une suite de \( E \) , bornée. Soit \( M > 0 \) tel que \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) pour tout \( n \) . Pour tout \( n,{x}_{n}/M \in B \) , donc la suite \( \left( {f\left( {{x}_{n}/M}\right) }\right) \) est à valeurs dans le compact \( \overline{f\left( B\right) } \) . On peut donc en extraire une sous-suite convergente \( {\left( f\left( {x}_{\varphi \left( n\right) }/M\right) \right) }_{n \in \mathbb{N}} \) , donc la suite \( {\left( f\left( {x}_{\varphi \left( n\right) }\right) \right) }_{n \in \mathbb{N}} \) est une sous-suite convergente de \( \left( {f\left( {x}_{n}\right) }\right) \) .

> — (i) \( \Rightarrow \) (iii). Let \( \left( {x}_{n}\right) \) be a bounded sequence in \( E \) . Let \( M > 0 \) be such that \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} \leq M \) for all \( n \) . For all \( n,{x}_{n}/M \in B \) , thus the sequence \( \left( {f\left( {{x}_{n}/M}\right) }\right) \) takes values in the compact set \( \overline{f\left( B\right) } \) . We can therefore extract a convergent subsequence \( {\left( f\left( {x}_{\varphi \left( n\right) }/M\right) \right) }_{n \in \mathbb{N}} \) , thus the sequence \( {\left( f\left( {x}_{\varphi \left( n\right) }\right) \right) }_{n \in \mathbb{N}} \) is a convergent subsequence of \( \left( {f\left( {x}_{n}\right) }\right) \) .

- (iii) \( \Rightarrow  \left( i\right) \) . Soit \( \left( {y}_{n}\right) \) une suite de \( \overline{f\left( B\right) } \) . Il s’agit de montrer que l’on peut en extraire une sous-suite convergente. Pour tout \( n \in  {\mathbb{N}}^{ * } \) , il existe \( {x}_{n} \in  B \) tel que \( \begin{Vmatrix}{f\left( {x}_{n}\right)  - {y}_{n}}\end{Vmatrix} < 1/n \) . D’après (iii), on peut extraire de \( \left( {f\left( {x}_{n}\right) }\right) \) une sous-suite convergente \( {\left\lbrack  f\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack  }_{n \in  \mathbb{N}} \) , et il est alors clair que la sous-suite \( \left( {y}_{\varphi \left( n\right) }\right) \) est convergente.

> - (iii) \( \Rightarrow  \left( i\right) \) . Let \( \left( {y}_{n}\right) \) be a sequence of \( \overline{f\left( B\right) } \) . We must show that a convergent subsequence can be extracted from it. For every \( n \in  {\mathbb{N}}^{ * } \) , there exists \( {x}_{n} \in  B \) such that \( \begin{Vmatrix}{f\left( {x}_{n}\right)  - {y}_{n}}\end{Vmatrix} < 1/n \) . According to (iii), we can extract a convergent subsequence \( {\left\lbrack  f\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack  }_{n \in  \mathbb{N}} \) from \( \left( {f\left( {x}_{n}\right) }\right) \) , and it is then clear that the subsequence \( \left( {y}_{\varphi \left( n\right) }\right) \) is convergent.

2/ a) Montrons que \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) est un s.e.v de \( {\mathcal{L}}_{c}\left( E\right) \) .

> 2/ a) Let us show that \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) is a subspace of \( {\mathcal{L}}_{c}\left( E\right) \) .

Si \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , et si \( \lambda \in \mathbb{R} \) , on a \( \overline{\left( {\lambda f}\right) \left( B\right) } = \lambda \overline{f\left( B\right) } \) , donc \( {\lambda f} \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) .

> If \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) , and if \( \lambda \in \mathbb{R} \) , we have \( \overline{\left( {\lambda f}\right) \left( B\right) } = \lambda \overline{f\left( B\right) } \) , therefore \( {\lambda f} \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) .

Soient \( f, g \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . Soit \( \left( {x}_{n}\right) \) une suite bornée de \( E \) . On peut extraire de \( {\left\lbrack f\left( {x}_{n}\right) \right\rbrack }_{n \in \mathbb{N}} \) une sous-suite convergente \( {\left\lbrack f\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) . De même, comme \( \left( {x}_{\varphi \left( n\right) }\right) \) est bornée, on peut extraire de \( {\left\lbrack g\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) une sous-suite convergente \( {\left\lbrack g\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) . Les deux suites \( {\left\lbrack f\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) et \( {\left\lbrack g\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) sont donc convergentes, donc la suite \( {\left\lbrack \left( f + g\right) \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) est convergente. D’après l’équivalence (iii) \( \Leftrightarrow \left( i\right) \) de la question précédente, on en déduit que \( f + g \) est un opérateur compact.

> Let \( f, g \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . Let \( \left( {x}_{n}\right) \) be a bounded sequence of \( E \) . We can extract a convergent subsequence \( {\left\lbrack f\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) from \( {\left\lbrack f\left( {x}_{n}\right) \right\rbrack }_{n \in \mathbb{N}} \) . Similarly, since \( \left( {x}_{\varphi \left( n\right) }\right) \) is bounded, we can extract a convergent subsequence \( {\left\lbrack g\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) from \( {\left\lbrack g\left( {x}_{\varphi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) . Both sequences \( {\left\lbrack f\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) and \( {\left\lbrack g\left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) are therefore convergent, so the sequence \( {\left\lbrack \left( f + g\right) \left( {x}_{\varphi \circ \psi \left( n\right) }\right) \right\rbrack }_{n \in \mathbb{N}} \) is convergent. According to the equivalence (iii) \( \Leftrightarrow \left( i\right) \) from the previous question, we deduce that \( f + g \) is a compact operator.

Montrons maintenant que \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) est un fermé de \( {\mathcal{L}}_{c}\left( E\right) \) . Soit \( \left( {f}_{n}\right) \) une suite de \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) qui converge vers \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Soit \( \varepsilon > 0 \) . Choisissons \( n \in \mathbb{N} \) tel que \( \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} < \varepsilon /2 \) . Comme \( {f}_{n} \) est un opérateur compact, d’après \( 1/\mathrm{b} \) ) (ii), on peut recouvrir \( {f}_{n}\left( B\right) \) par un nombre fini de boules ouvertes de rayon \( \varepsilon /2 \) . Alors \( f\left( B\right) \) est recouvert par les boules de même centre et de rayon \( \varepsilon \) , donc \( f \) est compact d’après \( 1/\mathrm{b} \) )(ii).

> Let us now show that \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) is a closed subset of \( {\mathcal{L}}_{c}\left( E\right) \) . Let \( \left( {f}_{n}\right) \) be a sequence in \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) that converges to \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Let \( \varepsilon > 0 \) . Choose \( n \in \mathbb{N} \) such that \( \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} < \varepsilon /2 \) . Since \( {f}_{n} \) is a compact operator, according to \( 1/\mathrm{b} \) (ii), we can cover \( {f}_{n}\left( B\right) \) with a finite number of open balls of radius \( \varepsilon /2 \) . Then \( f\left( B\right) \) is covered by balls with the same centers and radius \( \varepsilon \) , so \( f \) is compact according to \( 1/\mathrm{b} \) (ii).

b) Soit \( f \in {\mathcal{L}}_{c}\left( E\right) \) de rang fini. Comme \( f \) est continue, \( f\left( B\right) \) est bornée. Par ailleurs, \( f\left( E\right) \) est fermé (c’est un sous-espace de dimension finie), donc \( \overline{f\left( B\right) } \subset f\left( E\right) \) . Finalement, \( \overline{f\left( B\right) } \) est un fermé borné de \( f\left( E\right) \) . Comme \( f\left( E\right) \) est de dimension finie, \( \overline{f\left( B\right) } \) est donc un compact de \( f\left( E\right) \) , donc de \( E \) puisque \( f\left( E\right) \) est fermé.

> b) Let \( f \in {\mathcal{L}}_{c}\left( E\right) \) be of finite rank. Since \( f \) is continuous, \( f\left( B\right) \) is bounded. Furthermore, \( f\left( E\right) \) is closed (it is a finite-dimensional subspace), so \( \overline{f\left( B\right) } \subset f\left( E\right) \) . Finally, \( \overline{f\left( B\right) } \) is a closed bounded subset of \( f\left( E\right) \) . Since \( f\left( E\right) \) is finite-dimensional, \( \overline{f\left( B\right) } \) is therefore a compact subset of \( f\left( E\right) \) , and thus of \( E \) since \( f\left( E\right) \) is closed.

II. 1/ a) Soit \( \varepsilon > 0 \) . D’après I.1/b)(ii), il existe un nombre fini de boules de rayon \( \varepsilon \) recouvrant \( f\left( B\right) : f\left( B\right) \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{y}_{i},\varepsilon }\right) \) . Soit \( F = \operatorname{Vect}\left( {{y}_{1},\ldots ,{y}_{n}}\right) \) et \( {p}_{F} \) le projecteur orthogonal sur \( F \) .

> II. 1/ a) Let \( \varepsilon > 0 \) . According to I.1/b)(ii), there exists a finite number of balls of radius \( \varepsilon \) covering \( f\left( B\right) : f\left( B\right) \subset { \cup }_{1 \leq i \leq n}\mathrm{\;B}\left( {{y}_{i},\varepsilon }\right) \) . Let \( F = \operatorname{Vect}\left( {{y}_{1},\ldots ,{y}_{n}}\right) \) and \( {p}_{F} \) be the orthogonal projection onto \( F \) .

On a \( \begin{Vmatrix}{f - {p}_{F} \circ F}\end{Vmatrix} < \varepsilon \) . En effet, si \( x \in B \) , on sait qu’il existe \( i \) tel que \( \begin{Vmatrix}{f\left( x\right) - {y}_{i}}\end{Vmatrix} < \varepsilon \) . De plus, on sait que \( \parallel f\left( x\right) - {p}_{F} \circ f\left( x\right) \parallel = \mathop{\inf }\limits_{{y \in F}}\parallel f\left( x\right) - y\parallel \) , et comme \( {y}_{i} \in F \) , on en déduit \( \begin{Vmatrix}{f\left( x\right) - {p}_{F} \circ f\left( x\right) }\end{Vmatrix} \leq \begin{Vmatrix}{f\left( x\right) - {y}_{i}}\end{Vmatrix} < \varepsilon . \)

> We have \( \begin{Vmatrix}{f - {p}_{F} \circ F}\end{Vmatrix} < \varepsilon \) . Indeed, if \( x \in B \) , we know there exists \( i \) such that \( \begin{Vmatrix}{f\left( x\right) - {y}_{i}}\end{Vmatrix} < \varepsilon \) . Moreover, we know that \( \parallel f\left( x\right) - {p}_{F} \circ f\left( x\right) \parallel = \mathop{\inf }\limits_{{y \in F}}\parallel f\left( x\right) - y\parallel \) , and since \( {y}_{i} \in F \) , we deduce \( \begin{Vmatrix}{f\left( x\right) - {p}_{F} \circ f\left( x\right) }\end{Vmatrix} \leq \begin{Vmatrix}{f\left( x\right) - {y}_{i}}\end{Vmatrix} < \varepsilon . \)

En résumé, pour tout \( \varepsilon > 0 \) , nous avons trouvé un opérateur \( g \) continu de rang fini (ici \( g = {p}_{F} \circ f \) qui est bien de rang fini car \( F \) est de dimension finie), tel que \( \parallel g - f\parallel < \varepsilon \) . D’où le résultat.

> In summary, for any \( \varepsilon > 0 \), we have found a continuous finite-rank operator \( g \) (here \( g = {p}_{F} \circ f \), which is indeed of finite rank because \( F \) is finite-dimensional) such that \( \parallel g - f\parallel < \varepsilon \). Hence the result.

b) Remarquons déjà que si \( f \in {\mathcal{L}}_{c}\left( E\right) \) est de rang fini, alors \( {f}^{ * } \) aussi. En effet. La relation \( \left\langle {x,{f}^{ * }\left( y\right) }\right\rangle = \langle f\left( x\right) , y\rangle \) pour tout \( x, y \in E \) entraîne \( {f}^{ * }\left( E\right) \subset {\left( \operatorname{Ker}f\right) }^{ \bot } \) . Par ailleurs, la restriction de \( f \) à \( {\left( \operatorname{Ker}f\right) }^{ \bot } \) est un isomorphisme de \( {\left( \operatorname{Ker}f\right) }^{ \bot } \) sur \( f\left( E\right) \) , donc ( \( \operatorname{Ker}f{)}^{ \bot } \) est de dimension finie. Donc \( {f}^{ * }\left( E\right) \) est de dimension finie.

> b) Let us first note that if \( f \in {\mathcal{L}}_{c}\left( E\right) \) is of finite rank, then \( {f}^{ * } \) is as well. Indeed, the relation \( \left\langle {x,{f}^{ * }\left( y\right) }\right\rangle = \langle f\left( x\right) , y\rangle \) for all \( x, y \in E \) implies \( {f}^{ * }\left( E\right) \subset {\left( \operatorname{Ker}f\right) }^{ \bot } \). Furthermore, the restriction of \( f \) to \( {\left( \operatorname{Ker}f\right) }^{ \bot } \) is an isomorphism from \( {\left( \operatorname{Ker}f\right) }^{ \bot } \) onto \( f\left( E\right) \), so \( \operatorname{Ker}f{)}^{ \bot } \) is finite-dimensional. Thus \( {f}^{ * }\left( E\right) \) is finite-dimensional.

Ceci étant, soit \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) . D’après la question précédente, il existe une suite \( \left( {f}_{n}\right) \) d’opéra-teurs continus de rang fini qui converge vers \( f \) . Or popur tout \( n,\begin{Vmatrix}{{f}_{n}^{ * } - {f}^{ * }}\end{Vmatrix} = \begin{Vmatrix}{\left( {f}_{n} - f\right) }^{ * }\end{Vmatrix} = \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} \) , donc \( \left( {f}_{n}^{ * }\right) \) converge vers \( {f}^{ * } \) . Or tous les \( {f}_{n}^{ * } \) sont continus et de rang fini, donc compacts (voir I.2/b)), et comme \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) est fermé, on en déduit \( {f}^{ * } \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \) .

> Given this, let \( f \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \). According to the previous question, there exists a sequence \( \left( {f}_{n}\right) \) of continuous finite-rank operators that converges to \( f \). However, for any \( n,\begin{Vmatrix}{{f}_{n}^{ * } - {f}^{ * }}\end{Vmatrix} = \begin{Vmatrix}{\left( {f}_{n} - f\right) }^{ * }\end{Vmatrix} = \begin{Vmatrix}{{f}_{n} - f}\end{Vmatrix} \), \( \left( {f}_{n}^{ * }\right) \) converges to \( {f}^{ * } \). Since all \( {f}_{n}^{ * } \) are continuous and of finite rank, they are compact (see I.2/b)), and as \( {\mathcal{L}}_{\text{ comp }}\left( E\right) \) is closed, we deduce \( {f}^{ * } \in {\mathcal{L}}_{\text{ comp }}\left( E\right) \).

c) Supposons le contraire. Alors il existe \( \alpha > 0 \) et une sous-suite de \( \left( {e}_{n}\right) \) , encore notée \( \left( {e}_{n}\right) \) , telle que \( \begin{Vmatrix}{f\left( {e}_{n}\right) }\end{Vmatrix} \geq \alpha \) pour tout \( n \) . Comme \( f \) est compact, il existe une sous-suite \( \left( {e}_{\varphi \left( n\right) }\right) \) de \( \left( {e}_{n}\right) \) telle que \( \left( {f\left( {e}_{\varphi \left( n\right) }\right) }\right) \) converge. Notons \( x \) sa limite. On a \( \parallel x\parallel \geq \alpha \) , et

> c) Suppose the contrary. Then there exists \( \alpha > 0 \) and a subsequence of \( \left( {e}_{n}\right) \), still denoted by \( \left( {e}_{n}\right) \), such that \( \begin{Vmatrix}{f\left( {e}_{n}\right) }\end{Vmatrix} \geq \alpha \) for all \( n \). Since \( f \) is compact, there exists a subsequence \( \left( {e}_{\varphi \left( n\right) }\right) \) of \( \left( {e}_{n}\right) \) such that \( \left( {f\left( {e}_{\varphi \left( n\right) }\right) }\right) \) converges. Let \( x \) denote its limit. We have \( \parallel x\parallel \geq \alpha \), and

\[
\forall y \in  E,\;\langle x, y\rangle  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {f\left( {e}_{\varphi \left( n\right) }\right) , y}\right\rangle   = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left\langle  {{e}_{\varphi \left( n\right) },{f}^{ * }\left( y\right) }\right\rangle  ,
\]

et le dernier membre est nul en vertu de l'inégalité de Bessel (voir le problème 1, question 4/a)). On en déduit \( \langle x, y\rangle = 0 \) pour tout \( y \in E \) , donc \( x = 0 \) . Ceci est absurde car \( \parallel x\parallel \geq \alpha > 0 \) .

> and the last term is zero by virtue of Bessel's inequality (see problem 1, question 4/a)). We deduce \( \langle x, y\rangle = 0 \) for all \( y \in E \), so \( x = 0 \). This is absurd because \( \parallel x\parallel \geq \alpha > 0 \).

2/ a) Supposons que \( \operatorname{Ker}\left( {f - \lambda \text{ Id }}\right) \) soit de dimension infinie. Alors on peut trouver une suite orthonormale \( \left( {e}_{n}\right) \) de vecteurs de \( \operatorname{Ker}\left( {f - \lambda \text{ Id }}\right) \) (en partant d’un vecteur \( {e}_{0} \) de norme 1, construire les \( {e}_{n} \) par récurrence). Pour tout \( n \in \mathbb{N} \) , on a \( f\left( {e}_{n}\right) = \lambda {e}_{n} \) , donc \( \begin{Vmatrix}{f\left( {e}_{n}\right) }\end{Vmatrix} = \lambda \neq 0 \) . Ceci est absurde d'après le résultat de la question précédente.

> 2/ a) Suppose that \( \operatorname{Ker}\left( {f - \lambda \text{ Id }}\right) \) is infinite-dimensional. Then we can find an orthonormal sequence \( \left( {e}_{n}\right) \) of vectors in \( \operatorname{Ker}\left( {f - \lambda \text{ Id }}\right) \) (starting from a vector \( {e}_{0} \) of norm 1, construct the \( {e}_{n} \) by induction). For any \( n \in \mathbb{N} \) , we have \( f\left( {e}_{n}\right) = \lambda {e}_{n} \) , therefore \( \begin{Vmatrix}{f\left( {e}_{n}\right) }\end{Vmatrix} = \lambda \neq 0 \) . This is absurd according to the result of the previous question.

b) Soit \( \left( {\lambda }_{n}\right) \) une suite de valeurs propres distinctes de \( f \) , convergeant vers une valeur \( \lambda \) . Il s’agit de montrer que \( \lambda = 0 \) . Pour tout \( n \in \mathbb{N} \) , on note \( {x}_{n} \) un vecteur propre associé à la valeur propre \( {\lambda }_{n} \) . Le procédé d’orthonormalisation de Schmidt permet de construire une suite orthonor-male \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) qui vérifie \( \operatorname{Vect}\left( {{y}_{0},\ldots ,{y}_{n}}\right) = \operatorname{Vect}\left( {{x}_{0},\ldots ,{x}_{n}}\right) \) pour tout \( n \) . D’après II.1/c), on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {y}_{n}\right) = 0 \) . Pour tout \( n \) , on a \( \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \in \operatorname{Vect}\left( {{x}_{0},\ldots ,{x}_{n - 1}}\right) = \operatorname{Vect}\left( {{y}_{0},\ldots ,{y}_{n - 1}}\right) \) . Donc \( {\lambda }_{n}{y}_{n} \) et \( \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \) sont orthogonaux, et comme \( f\left( {y}_{n}\right) = {\lambda }_{n}{y}_{n} + \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \) , on en déduit \( \begin{Vmatrix}{f\left( {y}_{n}\right) }\end{Vmatrix} \geq \left| {\lambda }_{n}\right| \begin{Vmatrix}{y}_{n}\end{Vmatrix} = \left| {\lambda }_{n}\right| \) . Comme \( \left( {f\left( {y}_{n}\right) }\right) \) tend vers 0, on en déduit que \( \left( {\lambda }_{n}\right) \) tend vers 0 . Ainsi,0 est le seul point d’accumulation possible de \( \Lambda \left( f\right) \) . D’après le théorème de Weierstrass, on en déduit que pour tout \( n,\Lambda \left( f\right) \cap \left\lbrack {1/n, n}\right\rbrack \) est fini, donc

> b) Let \( \left( {\lambda }_{n}\right) \) be a sequence of distinct eigenvalues of \( f \) , converging to a value \( \lambda \) . We must show that \( \lambda = 0 \) . For any \( n \in \mathbb{N} \) , let \( {x}_{n} \) be an eigenvector associated with the eigenvalue \( {\lambda }_{n} \) . The Gram-Schmidt orthonormalization process allows us to construct an orthonormal sequence \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) which satisfies \( \operatorname{Vect}\left( {{y}_{0},\ldots ,{y}_{n}}\right) = \operatorname{Vect}\left( {{x}_{0},\ldots ,{x}_{n}}\right) \) for all \( n \) . According to II.1/c), we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {y}_{n}\right) = 0 \) . For all \( n \) , we have \( \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \in \operatorname{Vect}\left( {{x}_{0},\ldots ,{x}_{n - 1}}\right) = \operatorname{Vect}\left( {{y}_{0},\ldots ,{y}_{n - 1}}\right) \) . Thus \( {\lambda }_{n}{y}_{n} \) and \( \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \) are orthogonal, and since \( f\left( {y}_{n}\right) = {\lambda }_{n}{y}_{n} + \left( {f - {\lambda }_{n}\operatorname{Id}}\right) \left( {y}_{n}\right) \) , we deduce \( \begin{Vmatrix}{f\left( {y}_{n}\right) }\end{Vmatrix} \geq \left| {\lambda }_{n}\right| \begin{Vmatrix}{y}_{n}\end{Vmatrix} = \left| {\lambda }_{n}\right| \) . As \( \left( {f\left( {y}_{n}\right) }\right) \) tends to 0, we deduce that \( \left( {\lambda }_{n}\right) \) tends to 0. Thus, 0 is the only possible accumulation point of \( \Lambda \left( f\right) \) . According to the Weierstrass theorem, we deduce that for any \( n,\Lambda \left( f\right) \cap \left\lbrack {1/n, n}\right\rbrack \) is finite, therefore

\[
\Lambda \left( f\right)  \cap  {\mathbb{R}}^{+ * } = \mathop{\bigcup }\limits_{{n \in  {\mathbb{N}}^{ * }}}\left( {\Lambda \left( f\right)  \cap  \left\lbrack  {\frac{1}{n}, n}\right\rbrack  }\right)
\]

est au plus dénombrable. On montrerait de même que \( {\mathbb{R}}^{- * } \cap \Lambda \left( f\right) \) est au plus dénombrable. Donc \( \Lambda \left( f\right) \) est au plus dénombrable.

> is at most countable. We would show similarly that \( {\mathbb{R}}^{- * } \cap \Lambda \left( f\right) \) is at most countable. Therefore \( \Lambda \left( f\right) \) is at most countable.

III. 1/ a) Montrons déjà

> III. 1/ a) Let us first show

\[
\mathop{\sup }\limits_{{\parallel x\parallel  = \parallel y\parallel  = 1}}\left| {\langle f\left( x\right) , y\rangle }\right|  = \parallel f\parallel .
\]

(*)

> Si \( \parallel x\parallel = \parallel y\parallel = 1 \) , on a \( \left| {\langle f\left( x\right) , y\rangle }\right| \leq \parallel f\left( x\right) \parallel \parallel y\parallel \leq \parallel f\parallel \) .

If \( \parallel x\parallel = \parallel y\parallel = 1 \) , we have \( \left| {\langle f\left( x\right) , y\rangle }\right| \leq \parallel f\left( x\right) \parallel \parallel y\parallel \leq \parallel f\parallel \) .

> Par définition de la norme intrinsèque \( \parallel f\parallel \) , il existe une suite \( \left( {x}_{n}\right) \) de vecteurs de norme 1 qui vérifie \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} = \parallel f\parallel \) . En posant \( {y}_{n} = f\left( {x}_{n}\right) /\begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} \) pour tout \( n \) , on a \( \begin{Vmatrix}{y}_{n}\end{Vmatrix} = 1 \) et \( \left\langle {f\left( {x}_{n}\right) ,{y}_{n}}\right\rangle = \begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} \) , donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {f\left( {x}_{n}\right) ,{y}_{n}}\right\rangle = \parallel f\parallel \) , d’où (*).

By definition of the intrinsic norm \( \parallel f\parallel \) , there exists a sequence \( \left( {x}_{n}\right) \) of vectors of norm 1 satisfying \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} = \parallel f\parallel \) . By setting \( {y}_{n} = f\left( {x}_{n}\right) /\begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} \) for all \( n \) , we have \( \begin{Vmatrix}{y}_{n}\end{Vmatrix} = 1 \) and \( \left\langle {f\left( {x}_{n}\right) ,{y}_{n}}\right\rangle = \begin{Vmatrix}{f\left( {x}_{n}\right) }\end{Vmatrix} \) , so \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {f\left( {x}_{n}\right) ,{y}_{n}}\right\rangle = \parallel f\parallel \) , whence (*).

> Ceci étant, posons \( M = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\left| {\langle f\left( x\right) , x\rangle }\right| \) et montrons \( M = \parallel f\parallel \) . Tout d’abord, il est clair que pour tout vecteur \( x \) de norme \( 1,\left| {\langle f\left( x\right) , x\rangle }\right| \leq \parallel f\left( x\right) \parallel \parallel x\parallel = \parallel f\left( x\right) \parallel \leq \parallel f\parallel \) , donc \( M \leq \parallel f\parallel \) .

This being said, let us set \( M = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\left| {\langle f\left( x\right) , x\rangle }\right| \) and show \( M = \parallel f\parallel \) . First of all, it is clear that for any vector \( x \) of norm \( 1,\left| {\langle f\left( x\right) , x\rangle }\right| \leq \parallel f\left( x\right) \parallel \parallel x\parallel = \parallel f\left( x\right) \parallel \leq \parallel f\parallel \) , so \( M \leq \parallel f\parallel \) .

> Montrons l’inégalité réciproque. Si \( \parallel x\parallel = \parallel y\parallel = 1 \) , le caractère autoadjoint de \( f \) permet d’écrire, pour \( \varepsilon \in \{ - 1,1\} ,\langle f\left( {x + {\varepsilon y}}\right) , x + {\varepsilon y}\rangle = \langle f\left( x\right) , x\rangle + \langle f\left( y\right) , y\rangle + {2\varepsilon }\langle f\left( x\right) , y\rangle \) donc

Let us show the reverse inequality. If \( \parallel x\parallel = \parallel y\parallel = 1 \) , the self-adjoint nature of \( f \) allows us to write, for \( \varepsilon \in \{ - 1,1\} ,\langle f\left( {x + {\varepsilon y}}\right) , x + {\varepsilon y}\rangle = \langle f\left( x\right) , x\rangle + \langle f\left( y\right) , y\rangle + {2\varepsilon }\langle f\left( x\right) , y\rangle \) so

\[
4\langle f\left( x\right) , y\rangle  = \langle f\left( {x + y}\right) , x + y\rangle  - \langle f\left( {x - y}\right) , x - y\rangle
\]

ce qui entraîne

> which implies

\[
4\left| {\langle f\left( x\right) , y\rangle }\right|  \leq  \left| {\langle f\left( {x + y}\right) , x + y\rangle }\right|  + \left| {\langle f\left( {x - y}\right) , x - y\rangle }\right| .
\]

Or, par normalisation on a \( \left| {\langle f\left( {x + y}\right) , x + y\rangle }\right| \leq M\parallel x + y{\parallel }^{2} \) et \( \left| {\langle f\left( {x - y}\right) , x - y\rangle }\right| \leq M\parallel x - y{\parallel }^{2} \) , donc finalement

> However, by normalization we have \( \left| {\langle f\left( {x + y}\right) , x + y\rangle }\right| \leq M\parallel x + y{\parallel }^{2} \) and \( \left| {\langle f\left( {x - y}\right) , x - y\rangle }\right| \leq M\parallel x - y{\parallel }^{2} \) , so finally

\[
4\left| {\langle f\left( x\right) , y\rangle }\right|  \leq  M\left( {\parallel x + y{\parallel }^{2} + \parallel x - y{\parallel }^{2}}\right)  = {2M}\left( {\parallel x{\parallel }^{2} + \parallel y{\parallel }^{2}}\right)  = {4M}.
\]

Finalement, nous avons montré \( \left| {\langle f\left( x\right) , y\rangle }\right| \leq M \) dès que \( \parallel x\parallel = \parallel y\parallel = 1 \) . Avec (*), on en déduit \( \parallel f\parallel \leq M \) .

> Finally, we have shown \( \left| {\langle f\left( x\right) , y\rangle }\right| \leq M \) as soon as \( \parallel x\parallel = \parallel y\parallel = 1 \) . With (*), we deduce \( \parallel f\parallel \leq M \) .

Nous venons de montrer \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\left| {\langle f\left( x\right) , x\rangle }\right| \) , on conclut facilement qu’il existe une suite \( \left( {x}_{n}\right) \) de vecteurs normés telle que \( \left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle \) converge vers \( \parallel f\parallel \) .

> We have just shown \( \parallel f\parallel = \mathop{\sup }\limits_{{\parallel x\parallel = 1}}\left| {\langle f\left( x\right) , x\rangle }\right| \), we easily conclude that there exists a sequence \( \left( {x}_{n}\right) \) of normalized vectors such that \( \left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle \) converges to \( \parallel f\parallel \).

b) Il est clair que l’on peut trouver une sous-suite de la suite \( \left( {x}_{n}\right) \) construite précédemment, encore notée \( \left( {x}_{n}\right) \) , et \( \alpha \in \{ - 1,1\} \) tels que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle = \alpha \parallel f\parallel \) .

> b) It is clear that we can find a subsequence of the sequence \( \left( {x}_{n}\right) \) constructed previously, still denoted \( \left( {x}_{n}\right) \), and \( \alpha \in \{ - 1,1\} \) such that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left\langle {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle = \alpha \parallel f\parallel \).

Comme \( f \) est compact, on peut en extraire de \( \left( {x}_{n}\right) \) une sous-suite, encore notée \( \left( {x}_{n}\right) \) , telle que \( \left( {f\left( {x}_{n}\right) }\right) \) converge. Soit \( y \) sa limite. Posons \( \lambda = \alpha \parallel f\parallel \) . Pour tout \( n \) , on a

> Since \( f \) is compact, we can extract from \( \left( {x}_{n}\right) \) a subsequence, still denoted \( \left( {x}_{n}\right) \), such that \( \left( {f\left( {x}_{n}\right) }\right) \) converges. Let \( y \) be its limit. Let us set \( \lambda = \alpha \parallel f\parallel \). For all \( n \), we have

\[
{\begin{Vmatrix}f\left( {x}_{n}\right)  - \lambda {x}_{n}\end{Vmatrix}}^{2} = {\begin{Vmatrix}f\left( {x}_{n}\right) \end{Vmatrix}}^{2} + {\lambda }^{2}{\begin{Vmatrix}{x}_{n}\end{Vmatrix}}^{2} - {2\lambda }\left\langle  {{x}_{n}, f\left( {x}_{n}\right) }\right\rangle   \leq  2{\lambda }^{2} - {2\lambda }\left\langle  {f\left( {x}_{n}\right) ,{x}_{n}}\right\rangle  ,
\]

donc \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{f\left( {x}_{n}\right) - \lambda {x}_{n}}\end{Vmatrix} = 0 \) . Comme \( y - \lambda {x}_{n} = \left( {y - f\left( {x}_{n}\right) }\right) + \left( {f\left( {x}_{n}\right) - \lambda {x}_{n}}\right) \) , on en déduit que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}y - \lambda {x}_{n} = 0 \) . De plus \( \lambda = \alpha \parallel f\parallel \neq 0 \) , on a donc li \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{x}_{n} = y/\lambda \) , et comme \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} = 1 \) pour tout \( n \) , on a \( y \neq 0 \) .

> therefore \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\begin{Vmatrix}{f\left( {x}_{n}\right) - \lambda {x}_{n}}\end{Vmatrix} = 0 \). As \( y - \lambda {x}_{n} = \left( {y - f\left( {x}_{n}\right) }\right) + \left( {f\left( {x}_{n}\right) - \lambda {x}_{n}}\right) \), we deduce that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}y - \lambda {x}_{n} = 0 \). Furthermore \( \lambda = \alpha \parallel f\parallel \neq 0 \), we therefore have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{x}_{n} = y/\lambda \), and since \( \begin{Vmatrix}{x}_{n}\end{Vmatrix} = 1 \) for all \( n \), we have \( y \neq 0 \).

Le fait que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {x}_{n}\right) - \lambda {x}_{n} = 0 \) permet alors d’affirmer \( f\left( y\right) = {\lambda y} \) , donc \( \lambda \) est valeur propre non nulle de \( f \) .

> The fact that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}f\left( {x}_{n}\right) - \lambda {x}_{n} = 0 \) then allows us to assert \( f\left( y\right) = {\lambda y} \), therefore \( \lambda \) is a non-zero eigenvalue of \( f \).

2 / a) C’est comme en dimension finie. Si \( f\left( x\right) = {\lambda x} \) et \( f\left( y\right) = {\mu y} \) avec \( \lambda \neq \mu \) , alors

> 2 / a) It is as in finite dimension. If \( f\left( x\right) = {\lambda x} \) and \( f\left( y\right) = {\mu y} \) with \( \lambda \neq \mu \), then

\[
\lambda \langle x, y\rangle  = \langle f\left( x\right) , y\rangle  = \langle x, f\left( y\right) \rangle  = \mu \langle x, y\rangle ,
\]

donc \( \langle x, y\rangle = 0 \) .

> therefore \( \langle x, y\rangle = 0 \).

b) Montrons que \( {G}^{ \bot } \subset \operatorname{Ker}f \) . L’ensemble \( {G}^{ \bot } \) est stable par \( f \) . En effet, considérons \( x \in {G}^{ \bot } \) . Pour tout vecteur propre \( y \) de \( f \) associé à une valeur propre \( \lambda \neq 0 \) , on a \( \langle f\left( x\right) , y\rangle = \langle x, f\left( y\right) \rangle = \; \lambda \langle x, y\rangle = 0 \) , donc par linéarité \( \langle f\left( x\right) , y\rangle \) pour tout \( y \in G \) , c’est-à-dire \( x \in {G}^{ \bot } \) .

> b) Let us show that \( {G}^{ \bot } \subset \operatorname{Ker}f \). The set \( {G}^{ \bot } \) is stable by \( f \). Indeed, let us consider \( x \in {G}^{ \bot } \). For any eigenvector \( y \) of \( f \) associated with an eigenvalue \( \lambda \neq 0 \), we have \( \langle f\left( x\right) , y\rangle = \langle x, f\left( y\right) \rangle = \; \lambda \langle x, y\rangle = 0 \), therefore by linearity \( \langle f\left( x\right) , y\rangle \) for all \( y \in G \), that is to say \( x \in {G}^{ \bot } \).

La restriction \( g \) de \( f \) à \( {G}^{ \bot } \) est donc un endomorphisme (qui reste bien sûr compact et autoadjoint) de \( {G}^{ \bot } \) , qui est un espace de Hilbert (car fermé dans \( E \) ). Comme \( G \cap {G}^{ \bot } = \{ 0\} , g \) n’a aucune valeur propre non nulle. Donc d’après III.1/b), \( g = 0 \) , autrement dit, \( f\left( x\right) = 0 \) pour tout \( x \in {G}^{ \bot } \) . Donc \( {G}^{ \bot } \subset \operatorname{Ker}f \) .

> The restriction \( g \) of \( f \) to \( {G}^{ \bot } \) is therefore an endomorphism (which remains, of course, compact and self-adjoint) of \( {G}^{ \bot } \), which is a Hilbert space (as it is closed in \( E \)). Since \( G \cap {G}^{ \bot } = \{ 0\} , g \) has no non-zero eigenvalues. Thus, according to III.1/b), \( g = 0 \), in other words, \( f\left( x\right) = 0 \) for all \( x \in {G}^{ \bot } \). Therefore \( {G}^{ \bot } \subset \operatorname{Ker}f \).

Montrons maintenant l’inclusion réciproque. Soit \( x \in \operatorname{Ker}f \) , soit \( y \) un vecteur propre de \( f \) associé à une valeur propre \( \lambda \neq 0 \) . Alors

> Let us now show the reverse inclusion. Let \( x \in \operatorname{Ker}f \), let \( y \) be an eigenvector of \( f \) associated with an eigenvalue \( \lambda \neq 0 \). Then

\[
0 = \langle f\left( x\right) , y\rangle  = \langle x, f\left( y\right) \rangle  = \lambda \langle x, y\rangle ,
\]

donc \( \langle x, y\rangle = 0 \) , et par linéarité, \( x \in {G}^{ \bot } \) .

> therefore \( \langle x, y\rangle = 0 \), and by linearity, \( x \in {G}^{ \bot } \).

Donc Ker \( f = {G}^{ \bot } \) . Or \( {G}^{ \bot } = {\left( \bar{G}\right) }^{ \bot } = {F}^{ \bot } \) , d’où le résultat. c) Si \( \Lambda \left( f\right) \) n’est pas fini, d’après II.2/b), \( \Lambda \left( f\right) \) est dénombrable. Notons \( {\left( {\lambda }_{n}\right) }_{n \in \mathbb{N}} \) les éléments non nuls de \( \Lambda \left( f\right) \) . Pour tout \( n \) , le sous-espace propre \( {E}_{{\lambda }_{n}} = \operatorname{Ker}\left( {f - {\lambda }_{n}\text{ Id }}\right) \) est de dimension finie, et on note \( \left( {{e}_{n,1},\ldots ,{e}_{n,{p}_{n}}}\right) \) une base orthonormale de \( {E}_{{\lambda }_{n}} \) . Alors \( \left( {e}_{n}\right) = {\left( {e}_{n, i}\right) }_{\begin{matrix} {n \in \mathbb{N}} \\ {1 \leq i \leq {p}_{n}} \end{matrix}} \) est une base orthonormale de \( G \) (d’après III.2/a)). Tout élément de \( F = \bar{G} \) s’écrit donc sous la forme \( x = \mathop{\sum }\limits_{0}^{{+\infty }}\left\langle {x,{e}_{n}}\right\rangle {e}_{n} \) et comme \( F \oplus {F}^{ \bot } = E \) , on en déduit le résultat d’après III.2/b).

> Thus Ker \( f = {G}^{ \bot } \). However \( {G}^{ \bot } = {\left( \bar{G}\right) }^{ \bot } = {F}^{ \bot } \), hence the result. c) If \( \Lambda \left( f\right) \) is not finite, according to II.2/b), \( \Lambda \left( f\right) \) is countable. Let \( {\left( {\lambda }_{n}\right) }_{n \in \mathbb{N}} \) denote the non-zero elements of \( \Lambda \left( f\right) \). For all \( n \), the eigenspace \( {E}_{{\lambda }_{n}} = \operatorname{Ker}\left( {f - {\lambda }_{n}\text{ Id }}\right) \) is of finite dimension, and we denote by \( \left( {{e}_{n,1},\ldots ,{e}_{n,{p}_{n}}}\right) \) an orthonormal basis of \( {E}_{{\lambda }_{n}} \). Then \( \left( {e}_{n}\right) = {\left( {e}_{n, i}\right) }_{\begin{matrix} {n \in \mathbb{N}} \\ {1 \leq i \leq {p}_{n}} \end{matrix}} \) is an orthonormal basis of \( G \) (according to III.2/a)). Any element of \( F = \bar{G} \) can therefore be written in the form \( x = \mathop{\sum }\limits_{0}^{{+\infty }}\left\langle {x,{e}_{n}}\right\rangle {e}_{n} \) and since \( F \oplus {F}^{ \bot } = E \), we deduce the result according to III.2/b).

Si \( \Lambda \left( f\right) \) est fini, en notant \( \Lambda \left( f\right) \smallsetminus \{ 0\} = \left\{ {{\lambda }_{1},\ldots ,{\lambda }_{p}}\right\} , G = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{p}} \) est de dimension finie, donc \( F = G \) , donc

> If \( \Lambda \left( f\right) \) is finite, by noting \( \Lambda \left( f\right) \smallsetminus \{ 0\} = \left\{ {{\lambda }_{1},\ldots ,{\lambda }_{p}}\right\} , G = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{p}} \) is of finite dimension, therefore \( F = G \), thus

\[
{E}_{{\lambda }_{1}} \oplus  \cdots  \oplus  {E}_{{\lambda }_{p}} \oplus  \operatorname{Ker}f = F \oplus  {F}^{ \bot  } = E,
\]

la somme directe étant orthogonale.

> the direct sum being orthogonal.

Remarque. Rappelons que la boule unité d'un e.v.n n'est compacte qu'en dimension finie (théorème de Riesz, voir l’exercice 9 page 56). L’opérateur \( {\mathrm{{Id}}}_{E} \) n’est donc compact qu’en dimension finie.

> Remark. Recall that the unit ball of a normed vector space is compact only in finite dimension (Riesz's theorem, see exercise 9 page 56). The operator \( {\mathrm{{Id}}}_{E} \) is therefore compact only in finite dimension.

ANNEXE C

> APPENDIX C

##### Prime Number Theorem

*Français : Théorème des nombres premiers*

Cette annexe propose une preuve du théorème des nombres premiers, qui exprime que \( \pi \left( x\right) \) , le nombre de nombres premiers inférieurs à \( x \) , vérifie

> This appendix offers a proof of the prime number theorem, which states that \( \pi \left( x\right) \), the number of prime numbers less than \( x \), satisfies

\[
\pi \left( x\right)  \sim  \frac{x}{\log x},\;x \rightarrow   + \infty \;\pi \left( x\right)  = \operatorname{Card}\{ p\text{ premier, }p \leq  x\} .
\]

Ce célèbre résultat, conjecturé à la fin du dix-huitième siècle, résista aux mathématiciens jusqu'à la fin du dix-neuvième siècle.

> This famous result, conjectured at the end of the eighteenth century, resisted mathematicians until the end of the nineteenth century.

La preuve que nous proposons est classique et utilise la fonction \( \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{s} \) dans le domaine complexe. Nous utilisons une démonstration qui n'emploie pas la théorie des fonctions analytiques (qui est le cadre standard de cette preuve) et qui nous est donc accessible à partir du programme des classes préparatoires.

> The proof we propose is classical and uses the function \( \zeta \left( s\right) = \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}1/{n}^{s} \) in the complex domain. We use a demonstration that does not employ the theory of analytic functions (which is the standard framework for this proof) and is therefore accessible to us based on the preparatory classes curriculum.

La preuve fait l'objet du problème 3. Elle est précédée de deux problèmes qui four-nissent les ingrédients nécessaires à la démonstration : on démontre d'abord l'absence de zéro de \( \zeta \left( s\right) \) sur la ligne \( \Re \left( s\right) = 1 \) , puis on montre la formule de Perron, qui nous permet d’exploiter l’expression de \( \zeta \left( s\right) \) en fonction des nombres premiers.

> The proof is the subject of problem 3. It is preceded by two problems that provide the necessary ingredients for the demonstration: we first prove the absence of zeros of \( \zeta \left( s\right) \) on the line \( \Re \left( s\right) = 1 \), then we show Perron's formula, which allows us to exploit the expression of \( \zeta \left( s\right) \) as a function of prime numbers.

La dernière partie de cette annexe présente une histoire de la preuve du théorème des nombres premiers.

> The final part of this appendix presents a history of the proof of the prime number theorem.
