# Chapter 16 A Finite Dimensional Approximation to Omega^c

A Finite Dimensional Approximation to \( {\Omega }^{c} \)

Based on lecture notes by

M. Spivak and R. Wells

Let \( M \) be a connected Riemannian manifold and let \( p \) and \( q \) be two (not necessarily distinct) points of \( M \) . The set \( \Omega  = 0\left( {M;p, q}\right) \) of piecewise \( {C}^{\infty } \) paths from \( p \) to \( q \) can be topologized as follows. Let \( p \) denote the topological metric on \( M \) coming from its Riemann metric. Given \( \omega ,{\omega }^{\prime } \in  \Omega \) with arc-lengths \( s\left( t\right) ,{s}^{\prime }\left( t\right) \) respectively, define the distance \( \mathrm{d}\left( {\omega ,{\omega }^{\prime }}\right) \) to be

\[
\mathop{\max }\limits_{{0 \leq  t \leq  1}}\rho \left( {\omega \left( t\right) ,{\omega }^{\prime }\left( t\right) }\right)  + {\left( {\int }_{0}^{1}{\left( \frac{\mathrm{d}s}{\mathrm{\;d}t} - \frac{\mathrm{d}{s}^{\prime }}{\mathrm{d}t}\right) }^{2}\mathrm{\;d}t\right) }^{\frac{1}{2}}.
\]

(The last term is added on so that the energy function

\[
{E}_{a}^{b}\left( \omega \right)  = {\int }_{a}^{b}{\left( \frac{\mathrm{d}s}{\mathrm{\;d}t}\right) }^{2}\mathrm{\;d}t
\]

will be a continuous function from a to the real numbers.) This metric induces the required topology on \( \Omega \) .

Given \( c > 0 \) let \( {\Omega }^{c} \) denote the closed subset \( {E}^{-1}\left( \left\lbrack  {0, c}\right\rbrack  \right)  \subset  \Omega \) and let Int \( {\Omega }^{c} \) denote the open subset \( {E}^{-1}\left( {\lbrack 0, c}\right) ) \) (where \( E = {E}_{0}^{1} : \Omega  \rightarrow  \mathbf{R} \) is the energy function). We will study the topology of \( {\Omega }^{c} \) by constructing a finite dimensional approximation to it.

Choose some subdivision \( 0 = {t}_{0} < {t}_{1} < \ldots  < {t}_{k} = 1 \) of the unit interval. Let \( \Omega \left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) be the subspace of a consisting of paths \( \omega  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) such that

(a) \( \omega \left( 0\right)  = p \) and \( \omega \left( 1\right)  = q \) ,

(b) \( {\left. \omega \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is a geodesic for each \( i = 1,\ldots , k \) .

Finally we define the subspaces

\[
\Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c} = {\Omega }^{c} \cap  \Omega \left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right)
\]

\[
\operatorname{Int}\Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c} = \left( {\operatorname{Int}{\Omega }^{c}}\right)  \cap  \Omega \left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) .
\]

Lemma 16.1. Let \( M \) be a complete Riemannian manifold; and let \( c \) be a fixed positive number such that \( {\Omega }^{c} \neq  \varnothing \) . Then for all sufficiently fine subdivisions \( \left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) of \( \left\lbrack  {0,1}\right\rbrack \) the set \( \operatorname{Int}\Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c} \) can be given the structure of a smooth finite dimensional manifold in a natural way.

Proof. Let \( S \) denote the ball

\[
\{ x \in  M : \rho \left( {x, p}\right)  \leq  \sqrt{c}\} .
\]

Note that every path \( \omega  \in  {\Omega }^{c} \) lies within this subset \( S \subset  M \) . This follows from the inequality \( {L}^{2} \leq  E \leq  c \) .

Since \( M \) is complete, \( S \) is a compact set. Hence by Corollary 10.11 there exists \( \varepsilon  > 0 \) so that whenever \( x, y \in  S \) and \( \rho \left( {x, y}\right)  < \varepsilon \) there is a unique geodesic from \( x \) to \( y \) of length \( < \varepsilon \) ; and so that this geodesic depends differentiably on \( x \) and \( y \) .

Choose the subdivision \( \left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) of \( \left\lbrack  {0,1}\right\rbrack \) so that each difference \( {t}_{i} - {t}_{i - 1} \) is less than \( {\varepsilon }^{2}/c \) . Then for each broken geodesic

\[
\omega  \in  \Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c}
\]

we have

\[
{\left( {L}_{{t}_{i - 1}}^{{t}_{i}}\omega \right) }^{2} = \left( {{t}_{i} - {t}_{i - 1}}\right) \left( {{E}_{{t}_{i - 1}}^{{t}_{i}}\omega }\right)  \leq  \left( {{t}_{i} - {t}_{i - 1}}\right) \left( {E\omega }\right)
\]

\[
\leq  \left( {{t}_{i} - {t}_{i - 1}}\right) c < {\varepsilon }^{2}
\]

Thus the geodesic \( {\left. \omega \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is uniquely an differentiably determined by the two end points.

The broken geodesic \( \omega \) is uniquely determined by the \( \left( {k - 1}\right) \) -tuple

\[
\omega \left( {t}_{1}\right) ,\omega \left( {t}_{2}\right) ,\ldots ,\omega \left( {t}_{k - 1}\right)  \in  M \times  M \times  \cdots  \times  M.
\]

Evidently this correspondence

\[
\omega  \mapsto  \left( {\omega \left( {t}_{1}\right) ,\ldots ,\omega \left( {t}_{k - 1}\right) }\right)
\]

defines a homeomorphism between Int \( \Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c} \) and a certain open subset of the \( \left( {k - 1}\right) \) -fold product \( M \times  \cdots  \times  M \) . Taking over the differentiable structure from this product, this completes the proof of Lemma 16.1.

To shorten the notation, let us denote this manifold Int \( \Omega {\left( {t}_{0},{t}_{1},\ldots ,{t}_{k}\right) }^{c} \) of broken geodesics by \( B \) . Let

\[
{E}^{\prime } : B \rightarrow  \mathbf{R}
\]

denote the restriction to \( B \) of the energy function \( E : \Omega  \rightarrow  \mathbf{R} \) .

Theorem 16.2. This function \( {E}^{\prime } : B \rightarrow  \mathbf{R} \) is smooth. Furthermore, for each \( a < c \) the set \( {B}^{a} = {\left( {E}^{\prime }\right) }^{-1}\left\lbrack  {0, a}\right\rbrack \) is compact, and is a deformation retract \( {}^{1} \) of the corresponding set \( {\Omega }^{a} \) . The critical points of \( {E}^{\prime } \) are precisely the same as the critical points of \( E \) in \( \operatorname{Int}{\Omega }^{c} \) : namely the unbroken geodesics from \( p \) to \( q \) of length less than \( \sqrt{c} \) . The index (or the nullity) of the Hessian \( {E}_{* * }^{\prime } \) at each such critical point \( \gamma \) is equal to the index (or the nullity) of \( {E}_{* * } \) at \( \gamma \) .

Thus the finite dimensional manifold \( B \) provides a faithful model for the infinite dimensional path space Int \( {\Omega }^{c} \) . As an immediate consequence we have the following basic result.

---

\( {}^{1} \) Similarly \( B \) itself is a deformation retract of \( \operatorname{Int}{\Omega }^{c} \) .

---

Theorem 16.3. Let \( M \) be a complete Riemannian manifold and let \( p, q \in  M \) be two points which are not conjugate along any geodesic of length \( \leq  \sqrt{a} \) . Then as has the homotopy type of a finite CW-complex, with one cell of dimension \( \lambda \) for each geodesic in \( {\Omega }^{a} \) at which \( {E}_{* * } \) has index \( \lambda \) .

(In particular it is asserted that \( {\Omega }^{a} \) contains only finitely many geodesics.)

Proof. This follows from Theorem 16.2 together with Theorem 3.3.

Proof of Theorem 16.2. Since the broken geodesic \( \omega  \in  B \) depends smoothly on the \( \left( {k - 1}\right) \) -tuple

\[
\omega \left( {t}_{1}\right) ,\omega \left( {t}_{2}\right) ,\ldots ,\omega \left( {t}_{k - 1}\right)  \in  M \times  M \times  \cdots  \times  M
\]

it is clear that the energy \( {E}^{\prime }\left( \omega \right) \) also depends smoothly on this \( \left( {k - 1}\right) \) -tuple. In fact we have the explicit formula

\[
{E}^{\prime }\left( \omega \right)  = \mathop{\sum }\limits_{{i = 1}}^{k}\frac{\rho {\left( \omega \left( {t}_{i - 1}\right) ,\omega \left( {t}_{i}\right) \right) }^{2}}{{t}_{i} - {t}_{i - 1}}.
\]

For \( a < c \) the set \( {B}^{a} \) is homeomorphic to the set of all \( \left( {k - 1}\right) \) -tuples \( \left( {{p}_{1},\ldots ,{p}_{k - 1}}\right)  \in \; S \times  S \times  \cdots  \times  S \) such that

\[
\mathop{\sum }\limits_{{i = 1}}^{k}\frac{\rho {\left( {p}_{i - 1},{p}_{i}\right) }^{2}}{{t}_{i} - {t}_{i - 1}} \leq  a.
\]

(Here it is to be understood that \( {p}_{0} = p,{p}_{k} = q \) .) As a closed subset of a compact set, this is certainly compact.

A retraction \( r \) : Int \( {\Omega }^{c} \rightarrow  B \) is defined as follows. Let \( r\left( \omega \right) \) denote the unique broken geodesic in \( B \) such that each \( {\left. r\left( \omega \right) \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is a geodesic of length \( < \varepsilon \) from \( \omega \left( {t}_{i - 1}\right) \) to \( \omega \left( {t}_{i}\right) \) . The inequality

\[
\rho {\left( p,\omega \left( t\right) \right) }^{2} \leq  {\left( L\omega \right) }^{2} \leq  {E\omega } < c
\]

implies that \( \omega \left\lbrack  {o,1}\right\rbrack   \subset  S \) . Hence the inequality

\[
\rho {\left( \omega \left( {t}_{i - 1}\right) ,\omega \left( {t}_{i}\right) \right) }^{2} \leq  \left( {{t}_{i} - {t}_{i - 1}}\right) \left( {{E}_{{t}_{i - 1}}^{{t}_{i}}\omega }\right)  < \frac{{\varepsilon }^{2}}{c} \cdot  c = {\varepsilon }^{2}
\]

implies that \( r\left( \omega \right) \) can be so defined.

Clearly \( E\left( {r\left( \omega \right) }\right)  \leq  E\left( \omega \right)  < c \) . This retraction \( r \) fits into a 1-parameter family of maps

\[
{r}_{u} : \operatorname{Int}{\Omega }^{c} \rightarrow  \operatorname{Int}{\Omega }^{c}
\]

as follows. For \( {t}_{i - 1} \leq  u \leq  {t}_{i} \) let

\[
\left\{  \begin{array}{l} {\left. {r}_{u}\left( \omega \right) \right| }_{\left\lbrack  0,{t}_{i - 1}\right\rbrack  } = {\left. r\left( \omega \right) \right| }_{\left\lbrack  0,{t}_{i - 1}\right\rbrack  }, \\  {\left. {r}_{u}\left( \omega \right) \right| }_{\left\lbrack  {t}_{i - 1}, u\right\rbrack  } = \text{ minimal geodesic from }\omega \left( {t}_{i - 1}\right) \text{ to }\omega \left( u\right) , \\  {\left. {r}_{u}\left( \omega \right) \right| }_{\left\lbrack  u,1\right\rbrack  } = {\left. \omega \right| }_{\left\lbrack  u,1\right\rbrack  }. \end{array}\right.
\]

Then \( {r}_{0} \) is the identity map of Int \( {\Omega }^{c} \) , and \( {r}_{1} = r \) . It is easily verified that \( {r}_{u}\left( \omega \right) \) is continuous as a function of both variables. This proves that \( B \) is a deformation retract of Int \( {\Omega }^{c} \) .

Since \( E\left( {{r}_{u}\left( \omega \right) }\right)  \leq  E\left( \omega \right) \) it is clear that each \( {B}^{a} \) is also a deformation retract of \( {\Omega }^{a} \) .

Every geodesic is also a broken geodesic, so it is clear that every "critical point" of \( E \) in Int \( {\Omega }^{c} \) automatically lies in the submanifold \( B \) . Using the first variation formula (Theorem 12.2) it is clear that the critical points of \( {E}^{\prime } \) are precisely the unbroken geodesics.

Consider the tangent space \( T{B}_{\gamma } \) to the manifold \( B \) at a geodesic \( \gamma \) . This will be identified with the space \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) of broken Jacobi fields along \( \gamma \) , as described in chapter 15. This identification can be justified as follows. Let

\[
\overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  B
\]

be any variation of \( \gamma \) through broken geodesics. Then the corresponding variation vector field \( \frac{\partial \alpha }{\partial u}\left( {0, t}\right) \) along \( \gamma \) is clearly a broken Jacobi field. (Compare Lemma 14.5)

Now the statement that the index (or the nullity) of \( {E}_{* * } \) at \( \gamma \) is equal to the index (or nullity) of \( {E}_{* * }^{\prime } \) at \( \gamma \) is an immediate consequence of Lemma 15.4. This completes the proof of Theorem 16.2.

Remark. As one consequence of this theorem we obtain an alternative proof of the existence of a minimal geodesic joining two given points p, q of a complete manifold. For if \( {\Omega }^{a}\left( {p, q}\right) \) is non-vacuous, then the corresponding set \( {B}^{a} \) will be compact and non-vacuous. Hence the continuous function \( {E}^{\prime } : {B}^{a} \rightarrow  \mathbf{R} \) will take on its minimum at some point \( \gamma  \in  {B}^{a} \) . This \( \gamma \) will be the required minimal geodesic.
