#### 2.5. Commutatively convergent series, Cauchy product, double series

*Français : 2.5. Séries commutativement convergentes, produit de Cauchy, séries doubles*

Séries commutativement convergentes. On appelle ainsi les séries \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) telles que pour toute bijection \( \varphi \) de \( \mathbb{N} \) dans \( \mathbb{N} \) , la série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{\varphi \left( n\right) } \) converge. En particulier, une série commutativement convergente est convergente.

> Commutatively convergent series. This is the name given to series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) such that for any bijection \( \varphi \) from \( \mathbb{N} \) to \( \mathbb{N} \) , the series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{\varphi \left( n\right) } \) converges. In particular, a commutatively convergent series is convergent.

THÉORÉME 8. Une série \( \sum {u}_{n} \) à valeurs dans un espace de Banach et absolument conver-gente est commutativement convergente. De plus, pour toute bijection \( \varphi : \mathbb{N} \rightarrow \mathbb{N} \) , on a

> THEOREM 8. A series \( \sum {u}_{n} \) with values in a Banach space that is absolutely convergent is commutatively convergent. Furthermore, for any bijection \( \varphi : \mathbb{N} \rightarrow \mathbb{N} \) , we have

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{\varphi \left( n\right) }
\]

Démonstration. Soit \( \varphi \) une bijection de \( \mathbb{N} \) dans \( \mathbb{N} \) . Pour tout \( n \in \mathbb{N} \) , on a

> Proof. Let \( \varphi \) be a bijection from \( \mathbb{N} \) to \( \mathbb{N} \) . For any \( n \in \mathbb{N} \) , we have

\[
\mathop{\sum }\limits_{{k = 0}}^{n}\begin{Vmatrix}{u}_{\varphi \left( k\right) }\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\begin{Vmatrix}{u}_{k}\end{Vmatrix}
\]

donc \( \sum {u}_{\varphi \left( n\right) } \) converge absolument, donc converge. Montrons l’égalité des sommes des deux séries. Soit \( \varepsilon > 0 \) et soit \( N \in \mathbb{N} \) tel que \( \mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{n}\end{Vmatrix} < \varepsilon \) . Comme \( \varphi : \mathbb{N} \rightarrow \mathbb{N} \) est une bijection, il existe \( {N}^{\prime } \in \mathbb{N} \) tel que \( \{ 0,1,\ldots , N\} \subset \left\{ {\varphi \left( 0\right) ,\varphi \left( 1\right) ,\ldots ,\varphi \left( {N}^{\prime }\right) }\right\} \) . On en déduit

> so \( \sum {u}_{\varphi \left( n\right) } \) converges absolutely, therefore it converges. Let us show the equality of the sums of the two series. Let \( \varepsilon > 0 \) and let \( N \in \mathbb{N} \) be such that \( \mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{n}\end{Vmatrix} < \varepsilon \) . Since \( \varphi : \mathbb{N} \rightarrow \mathbb{N} \) is a bijection, there exists \( {N}^{\prime } \in \mathbb{N} \) such that \( \{ 0,1,\ldots , N\} \subset \left\{ {\varphi \left( 0\right) ,\varphi \left( 1\right) ,\ldots ,\varphi \left( {N}^{\prime }\right) }\right\} \) . We deduce from this

\[
\begin{Vmatrix}{\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} - \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{\varphi \left( n\right) }}\end{Vmatrix} \leq  \begin{Vmatrix}{\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} - \mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n}}\end{Vmatrix} + \begin{Vmatrix}{\mathop{\sum }\limits_{{n = 0}}^{N}{u}_{n} - \mathop{\sum }\limits_{{n = 0}}^{{N}^{\prime }}{u}_{\varphi \left( n\right) }}\end{Vmatrix} + \begin{Vmatrix}{\mathop{\sum }\limits_{{n = 0}}^{{N}^{\prime }}{u}_{\varphi \left( n\right) } - \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{\varphi \left( n\right) }}\end{Vmatrix}
\]

\[
\leq  \mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{n}\end{Vmatrix} + \mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{n}\end{Vmatrix} + \mathop{\sum }\limits_{{n = {N}^{\prime } + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{\varphi \left( n\right) }\end{Vmatrix} \leq  3\mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}\begin{Vmatrix}{u}_{n}\end{Vmatrix} < {3\varepsilon }.
\]

Cette inégalité est vraie pour tout \( \varepsilon > 0 \) , on en conclut \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{\varphi \left( n\right) } \) .

> This inequality is true for all \( \varepsilon > 0 \) , we conclude \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{\varphi \left( n\right) } \) .

Produit de Cauchy.

> Cauchy product.

THÉORÉME 9 (PRODUIT DE CAUCHY). Soient \( \mathop{\sum }\limits_{{p \in \mathbb{N}}}{a}_{p} \) et \( \mathop{\sum }\limits_{{q \in \mathbb{N}}}{b}_{q} \) deux séries absolu-ment convergentes à valeurs dans une algèbre normée complète. Alors la série

> THEOREM 9 (CAUCHY PRODUCT). Let \( \mathop{\sum }\limits_{{p \in \mathbb{N}}}{a}_{p} \) and \( \mathop{\sum }\limits_{{q \in \mathbb{N}}}{b}_{q} \) be two absolutely convergent series with values in a complete normed algebra. Then the series

\[
\mathop{\sum }\limits_{{n \in  \mathbb{N}}}{c}_{n}\;\text{ avec }\;{c}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{b}_{n - k}
\]

est appelée produit de Cauchy de \( \sum {a}_{p} \) et \( \sum {b}_{q} \) , elle est absolument convergente et on a

> is called the Cauchy product of \( \sum {a}_{p} \) and \( \sum {b}_{q} \) , it is absolutely convergent and we have

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{c}_{n} = \left( {\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{a}_{p}}\right) \left( {\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{b}_{q}}\right) .
\]

(*)

> Démonstration. La série \( \sum {c}_{n} \) est absolument convergente d’après la majoration

Proof. The series \( \sum {c}_{n} \) is absolutely convergent according to the bound

\[
\mathop{\sum }\limits_{{n = 0}}^{N}\begin{Vmatrix}{c}_{n}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{n = 0}}^{N}\left( {\mathop{\sum }\limits_{{p + q = n}}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \cdot  \begin{Vmatrix}{b}_{q}\end{Vmatrix}}\right)  \leq  \mathop{\sum }\limits_{{0 \leq  p, q \leq  N}}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \cdot  \begin{Vmatrix}{b}_{q}\end{Vmatrix} = \left( {\mathop{\sum }\limits_{{p = 0}}^{N}\begin{Vmatrix}{a}_{p}\end{Vmatrix}}\right) \left( {\mathop{\sum }\limits_{{q = 0}}^{N}\begin{Vmatrix}{b}_{q}\end{Vmatrix}}\right)  \leq  {AB}
\]

avec \( A = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \) et \( B = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}\begin{Vmatrix}{b}_{q}\end{Vmatrix} \) . Pour montrer (*), remarquons maintenant que

> with \( A = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \) and \( B = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}\begin{Vmatrix}{b}_{q}\end{Vmatrix} \) . To show (*), let us now note that

\[
{\Delta }_{n} = \mathop{\sum }\limits_{{k = 0}}^{{2n}}{c}_{k} - \left( {\mathop{\sum }\limits_{{p = 0}}^{n}{a}_{p}}\right) \left( {\mathop{\sum }\limits_{{q = 0}}^{n}{b}_{q}}\right)  = \mathop{\sum }\limits_{{0 \leq  p + q \leq  {2n}}}{a}_{p}{b}_{q} - \mathop{\sum }\limits_{{0 \leq  p, q \leq  n}}{a}_{p}{b}_{q} = \mathop{\sum }\limits_{\substack{{p > n} \\  {p + q \leq  {2n}} }}{a}_{p}{b}_{q} + \mathop{\sum }\limits_{\substack{{q > n} \\  {p + q \leq  {2n}} }}{a}_{p}{b}_{q}
\]

ce qui entraîne

> which implies

\[
\begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \leq  \mathop{\sum }\limits_{\substack{{n \leq  p \leq  {2n}} \\  {q < n} }}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \cdot  \begin{Vmatrix}{b}_{q}\end{Vmatrix} + \mathop{\sum }\limits_{\substack{{n < q \leq  {2n}} \\  {p < n} }}\begin{Vmatrix}{a}_{p}\end{Vmatrix} \cdot  \begin{Vmatrix}{b}_{q}\end{Vmatrix} = \mathop{\sum }\limits_{{p = n + 1}}^{{2n}}\begin{Vmatrix}{a}_{p}\end{Vmatrix}\mathop{\sum }\limits_{{q = 0}}^{{n - 1}}\begin{Vmatrix}{b}_{q}\end{Vmatrix} + \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}\begin{Vmatrix}{a}_{p}\end{Vmatrix}\mathop{\sum }\limits_{{q = n + 1}}^{{2n}}\begin{Vmatrix}{b}_{q}\end{Vmatrix},
\]

donc \( \begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \leq B\mathop{\sum }\limits_{{p = n + 1}}^{{2n}}\begin{Vmatrix}{a}_{p}\end{Vmatrix} + A\mathop{\sum }\limits_{{q = n + 1}}^{{2n}}\begin{Vmatrix}{b}_{q}\end{Vmatrix} \) . Ainsi \( \begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \) converge vers 0, d’où \( \left( *\right) \) .

> so \( \begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \leq B\mathop{\sum }\limits_{{p = n + 1}}^{{2n}}\begin{Vmatrix}{a}_{p}\end{Vmatrix} + A\mathop{\sum }\limits_{{q = n + 1}}^{{2n}}\begin{Vmatrix}{b}_{q}\end{Vmatrix} \) . Thus \( \begin{Vmatrix}{\Delta }_{n}\end{Vmatrix} \) converges to 0, hence \( \left( *\right) \) .

Séries doubles. On désigne ainsi les séries de la forme \( \mathop{\sum }\limits_{{\left( {p, q}\right) \in {\mathbb{N}}^{2}}}{u}_{p, q} \) .

> Double series. This term refers to series of the form \( \mathop{\sum }\limits_{{\left( {p, q}\right) \in {\mathbb{N}}^{2}}}{u}_{p, q} \) .

THÉORÉME 10. Soit \( {\left( {u}_{p, q}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) une suite à double entrée,à valeurs dans un espace de Banach. Alors les deux assertions suivantes sont équivalentes

> THEOREM 10. Let \( {\left( {u}_{p, q}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) be a double sequence with values in a Banach space. Then the following two assertions are equivalent

(i) Pour tout \( q \in \mathbb{N},\mathop{\sum }\limits_{p}{u}_{p, q} \) est absolument convergente, et \( \mathop{\sum }\limits_{q}\left( {\mathop{\sum }\limits_{{p = 0}}^{\infty }\begin{Vmatrix}{u}_{p, q}\end{Vmatrix}}\right) \) converge.

> (i) For all \( q \in \mathbb{N},\mathop{\sum }\limits_{p}{u}_{p, q} \) is absolutely convergent, and \( \mathop{\sum }\limits_{q}\left( {\mathop{\sum }\limits_{{p = 0}}^{\infty }\begin{Vmatrix}{u}_{p, q}\end{Vmatrix}}\right) \) converges.

(ii) Pour tout \( p \in \mathbb{N},\mathop{\sum }\limits_{q}{u}_{p, q} \) est absolument convergente, et \( \mathop{\sum }\limits_{p}\left( {\mathop{\sum }\limits_{{q = 0}}^{\infty }\begin{Vmatrix}{u}_{p, q}\end{Vmatrix}}\right) \) converge. Dans ces hypothèses, on a de plus

> (ii) For all \( p \in \mathbb{N},\mathop{\sum }\limits_{q}{u}_{p, q} \) is absolutely convergent, and \( \mathop{\sum }\limits_{p}\left( {\mathop{\sum }\limits_{{q = 0}}^{\infty }\begin{Vmatrix}{u}_{p, q}\end{Vmatrix}}\right) \) converges. Under these hypotheses, we further have

\[
\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{u}_{p, q}}\right)  = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{u}_{p, q}}\right) .
\]

(*)

> Démonstration. Montrons (i) \( \Rightarrow \) (ii). Notons \( {A}_{q} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \) . Pour \( p \) fixé, \( \begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \leq {A}_{q} \) et d’après (i), \( \sum {A}_{q} \) converge, donc \( \mathop{\sum }\limits_{q}\begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \) converge. Notons \( {B}_{p} \) la somme de cette série. On a

Proof. Let us show (i) \( \Rightarrow \) (ii). Let \( {A}_{q} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \) . For fixed \( p \) , \( \begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \leq {A}_{q} \) and according to (i), \( \sum {A}_{q} \) converges, therefore \( \mathop{\sum }\limits_{q}\begin{Vmatrix}{u}_{p, q}\end{Vmatrix} \) converges. Let \( {B}_{p} \) be the sum of this series. We have

\[
\forall P \in  \mathbb{N},\;\mathop{\sum }\limits_{{p = 0}}^{P}{B}_{p} = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}\left( {\mathop{\sum }\limits_{{p = 0}}^{P}\begin{Vmatrix}{u}_{p, q}\end{Vmatrix}}\right)  \leq  \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{A}_{q}.
\]

Cette majoration étant indépendante de \( P \) , on en conclut que \( \mathop{\sum }\limits_{p}{B}_{p} \) converge, d’où (ii). On montre de la même manière que (ii) : (i).

> Since this upper bound is independent of \( P \) , we conclude that \( \mathop{\sum }\limits_{p}{B}_{p} \) converges, hence (ii). We show in the same way that (ii) : (i).

Montrons maintenant (*). Notons \( {a}_{n, q} = \mathop{\sum }\limits_{{p = 0}}^{n}{u}_{p, q} \) et \( {a}_{q} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{u}_{p, q} \) . La série \( \sum {a}_{q} \) converge absolument car \( \begin{Vmatrix}{a}_{q}\end{Vmatrix} \leq {A}_{q} \) , donc elle converge. Soit \( \varepsilon > 0 \) et soit \( Q \in \mathbb{N} \) tel que \( \mathop{\sum }\limits_{{q > Q}}{A}_{q} < \varepsilon \) . Notons \( {C}_{n} = \mathop{\sum }\limits_{{0 \leq p, q \leq n}}{u}_{p, q} \) . Lorsque \( n > Q \) on a

> Let us now show (*). Let \( {a}_{n, q} = \mathop{\sum }\limits_{{p = 0}}^{n}{u}_{p, q} \) and \( {a}_{q} = \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{u}_{p, q} \) . The series \( \sum {a}_{q} \) converges absolutely because \( \begin{Vmatrix}{a}_{q}\end{Vmatrix} \leq {A}_{q} \) , therefore it converges. Let \( \varepsilon > 0 \) and let \( Q \in \mathbb{N} \) such that \( \mathop{\sum }\limits_{{q > Q}}{A}_{q} < \varepsilon \) . Let \( {C}_{n} = \mathop{\sum }\limits_{{0 \leq p, q \leq n}}{u}_{p, q} \) . When \( n > Q \) we have

\[
\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} - {C}_{n} = \mathop{\sum }\limits_{{q = 0}}^{Q}\left( {{a}_{q} - {a}_{n, q}}\right)  + \mathop{\sum }\limits_{{q = Q + 1}}^{n}\left( {{a}_{q} - {a}_{n, q}}\right)  + \mathop{\sum }\limits_{{q = n + 1}}^{{+\infty }}{a}_{q}.
\]

\( \left( {* * }\right) \)

> Pour \( q > Q \) , on a \( \begin{Vmatrix}{{a}_{q} - {a}_{n, q}}\end{Vmatrix} = \begin{Vmatrix}{\mathop{\sum }\limits_{{p > n}}{u}_{p, q}}\end{Vmatrix} \leq {A}_{q} \) et comme \( \begin{Vmatrix}{a}_{q}\end{Vmatrix} \leq {A}_{q} \) ,(**) entraîne

For \( q > Q \) , we have \( \begin{Vmatrix}{{a}_{q} - {a}_{n, q}}\end{Vmatrix} = \begin{Vmatrix}{\mathop{\sum }\limits_{{p > n}}{u}_{p, q}}\end{Vmatrix} \leq {A}_{q} \) and since \( \begin{Vmatrix}{a}_{q}\end{Vmatrix} \leq {A}_{q} \) , (**) implies

\[
\begin{Vmatrix}{\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} - {C}_{n}}\end{Vmatrix} \leq  \begin{Vmatrix}{\mathop{\sum }\limits_{{q = 0}}^{Q}\left( {{a}_{q} - {a}_{n, q}}\right) }\end{Vmatrix} + \mathop{\sum }\limits_{{q = Q + 1}}^{\infty }{A}_{q} \leq  \begin{Vmatrix}{\mathop{\sum }\limits_{{q = 0}}^{Q}\left( {{a}_{q} - {a}_{n, q}}\right) }\end{Vmatrix} + \varepsilon .
\]

Les suites \( {\left( {a}_{n, q}\right) }_{n} \) pour \( 0 \leq q \leq Q \) convergent vers \( {a}_{q} \) donc il existe \( {N}_{0} \geq Q \) tel que \( \parallel \mathop{\sum }\limits_{{q = 0}}^{Q}\left( {{a}_{q} - }\right. \; \left. {a}_{n, q}\right) \parallel < \varepsilon \) dès que \( n \geq {N}_{0} \) . Ainsi, pour \( n \geq {N}_{0} \) on a \( \begin{Vmatrix}{\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} - {C}_{n}}\end{Vmatrix} < {2\varepsilon } \) , donc la suite \( \left( {C}_{n}\right) \) converge vers \( \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} \) . On montrerait de même que \( \sum {b}_{p} \) converge et que \( \left( {C}_{n}\right) \) converge vers \( \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{b}_{p} \) (avec \( {b}_{p} = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{u}_{p, q} \) ). Ainsi, on peut bien intervertir les signes de sommation.

> The sequences \( {\left( {a}_{n, q}\right) }_{n} \) for \( 0 \leq q \leq Q \) converge to \( {a}_{q} \), so there exists \( {N}_{0} \geq Q \) such that \( \parallel \mathop{\sum }\limits_{{q = 0}}^{Q}\left( {{a}_{q} - }\right. \; \left. {a}_{n, q}\right) \parallel < \varepsilon \) as soon as \( n \geq {N}_{0} \). Thus, for \( n \geq {N}_{0} \) we have \( \begin{Vmatrix}{\mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} - {C}_{n}}\end{Vmatrix} < {2\varepsilon } \), so the sequence \( \left( {C}_{n}\right) \) converges to \( \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{a}_{q} \). We could show similarly that \( \sum {b}_{p} \) converges and that \( \left( {C}_{n}\right) \) converges to \( \mathop{\sum }\limits_{{p = 0}}^{{+\infty }}{b}_{p} \) (with \( {b}_{p} = \mathop{\sum }\limits_{{q = 0}}^{{+\infty }}{u}_{p, q} \)). Thus, we can indeed interchange the summation signs.

Remarque 8. Les résultats précédents s'inscrivent naturellement dans le cadre de la théorie des familles sommables, que nous présentons brièvement. Soit \( E \) un espace de Banach, \( I \) un ensemble non vide. On note \( {\mathcal{P}}_{f}\left( I\right) \) l’ensemble des parties finies de \( I \) . On considère une famille \( {\left( {u}_{i}\right) }_{i \in I} \) d’éléments de \( E \) .

> Remark 8. The previous results fit naturally into the framework of the theory of summable families, which we present briefly. Let \( E \) be a Banach space, \( I \) a non-empty set. We denote by \( {\mathcal{P}}_{f}\left( I\right) \) the set of finite subsets of \( I \). We consider a family \( {\left( {u}_{i}\right) }_{i \in I} \) of elements of \( E \).

(1) La famille \( {\left( {u}_{i}\right) }_{i \in I} \) est dite sommable s’il existe \( S \in E \) tel que

> (1) The family \( {\left( {u}_{i}\right) }_{i \in I} \) is said to be summable if there exists \( S \in E \) such that

\[
\forall \varepsilon  > 0,\exists {J}_{0} \in  {\mathcal{P}}_{f}\left( I\right) ,\forall J \in  {\mathcal{P}}_{f}\left( I\right) ,{J}_{0} \subset  J,\;\begin{Vmatrix}{\mathop{\sum }\limits_{{i \in  J}}{u}_{i} - S}\end{Vmatrix} < \varepsilon .
\]

La grandeur \( S \) est alors appelée somme de \( {\left( {u}_{i}\right) }_{i \in I} \) et notée \( \mathop{\sum }\limits_{{i \in I}}{u}_{i} \) .

> The quantity \( S \) is then called the sum of \( {\left( {u}_{i}\right) }_{i \in I} \) and denoted by \( \mathop{\sum }\limits_{{i \in I}}{u}_{i} \).

(2) Elle est dite absolument sommable si la famille \( {\left( \begin{Vmatrix}{u}_{i}\end{Vmatrix}\right) }_{i \in I} \) est sommable. Ceci est équivalent à dire que l’ensemble \( \left\{ {\mathop{\sum }\limits_{{i \in J}}\begin{Vmatrix}{u}_{i}\end{Vmatrix}, J \in {\mathcal{P}}_{f}\left( I\right) }\right\} \) est borné.

> (2) It is said to be absolutely summable if the family \( {\left( \begin{Vmatrix}{u}_{i}\end{Vmatrix}\right) }_{i \in I} \) is summable. This is equivalent to saying that the set \( \left\{ {\mathop{\sum }\limits_{{i \in J}}\begin{Vmatrix}{u}_{i}\end{Vmatrix}, J \in {\mathcal{P}}_{f}\left( I\right) }\right\} \) is bounded.

Les familles sommables vérifient les propriétés suivantes :

> Summable families satisfy the following properties:

(i) Si \( {\left( {u}_{i}\right) }_{i \in I} \) est sommable, alors l’ensemble \( \left\{ {i \in I,{u}_{i} \neq 0}\right\} \) est au plus dénombrable.

> (i) If \( {\left( {u}_{i}\right) }_{i \in I} \) is summable, then the set \( \left\{ {i \in I,{u}_{i} \neq 0}\right\} \) is at most countable.

(ii) Une série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) est absolument convergente si et seulement si la famille \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) est absolument sommable.

> (ii) A series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) is absolutely convergent if and only if the family \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) is absolutely summable.

(iii) Une famille absolument sommable est sommable. La réciproque est vraie si \( E \) est de dimension finie mais fausse si \( E \) est de dimension infinie.

> (iii) An absolutely summable family is summable. The converse is true if \( E \) is of finite dimension but false if \( E \) is of infinite dimension.

(iv) Une série \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) est commutativement convergente si et seulement si la famille \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) est sommable.

> (iv) A series \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{u}_{n} \) is commutatively convergent if and only if the family \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) is summable.

(v) (Associativité) Si \( {\left( {I}_{t}\right) }_{t \in T} \) est une partition de \( I \) , alors \( {\left( {u}_{i}\right) }_{i \in I} \) est sommable si et seulement si pour tout \( t \in T,{\left( {u}_{i}\right) }_{i \in {I}_{t}} \) est sommable, de somme \( {s}_{t} \) , et la famille \( {\left( {s}_{t}\right) }_{t \in T} \) est sommable.

> (v) (Associativity) If \( {\left( {I}_{t}\right) }_{t \in T} \) is a partition of \( I \), then \( {\left( {u}_{i}\right) }_{i \in I} \) is summable if and only if for every \( t \in T,{\left( {u}_{i}\right) }_{i \in {I}_{t}} \) is summable, with sum \( {s}_{t} \), and the family \( {\left( {s}_{t}\right) }_{t \in T} \) is summable.

Les résultats précédents découlent naturellement des propriétés des familles sommables : le théorème 8 est la conséquence de (ii), (iii) et (iv). Pour le théorème sur les produits de Cauchy, la convergence absolue de \( \sum {c}_{n} \) découle de (v) appliqué à la famille \( {\left( \begin{Vmatrix}{u}_{p}{v}_{q}\end{Vmatrix}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) avec la partition \( {\left( \{ \left( p, q\right) , p + q = n\} \right) }_{n \in \mathbb{N}} \) de \( {\mathbb{N}}^{2} \) , et l’égalité des limites provient de (v) appliqué à la famille \( {\left( {u}_{p}{v}_{q}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) et à la même partition. L’équivalence des assertions (i) et (ii) du théorème d'interversion des limites est la conséquence de la propriété d'associativité appliquée à la famille \( {\left( \begin{Vmatrix}{u}_{p, q}\end{Vmatrix}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) , et la formule (*) est la conséquence de (iii) et de (v) appliqué aux partitions \( {\left( \mathbb{N}\times \{ n\} \right) }_{n \in \mathbb{N}} \) et \( {\left( \{ n\} \times \mathbb{N}\right) }_{n \in \mathbb{N}} \) de \( {\mathbb{N}}^{2} \) .

> The preceding results follow naturally from the properties of summable families: Theorem 8 is a consequence of (ii), (iii), and (iv). For the theorem on Cauchy products, the absolute convergence of \( \sum {c}_{n} \) follows from (v) applied to the family \( {\left( \begin{Vmatrix}{u}_{p}{v}_{q}\end{Vmatrix}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) with the partition \( {\left( \{ \left( p, q\right) , p + q = n\} \right) }_{n \in \mathbb{N}} \) of \( {\mathbb{N}}^{2} \), and the equality of the limits comes from (v) applied to the family \( {\left( {u}_{p}{v}_{q}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \) and the same partition. The equivalence of assertions (i) and (ii) of the theorem on the interversion of limits is a consequence of the associativity property applied to the family \( {\left( \begin{Vmatrix}{u}_{p, q}\end{Vmatrix}\right) }_{\left( {p, q}\right) \in {\mathbb{N}}^{2}} \), and formula (*) is a consequence of (iii) and (v) applied to the partitions \( {\left( \mathbb{N}\times \{ n\} \right) }_{n \in \mathbb{N}} \) and \( {\left( \{ n\} \times \mathbb{N}\right) }_{n \in \mathbb{N}} \) of \( {\mathbb{N}}^{2} \).
