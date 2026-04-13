# Chapter 22 Whole Manifolds of Minimal Geodesics

Based on lecture notes by

M. Spivak and R. Wells

So far we have used a path space \( \Omega \left( {M;p, q}\right) \) based on two points \( p, q \in  M \) which are in "general position." However, Bott has pointed out that very useful results can be obtained by considering pairs \( p, q \) in some special position. As an example let \( M \) be the unit sphere \( {\mathbb{S}}^{n + 1} \) , and let \( p, q \) be antipodal points. Then there are infinitely many minimal geodesics from \( p \) to \( q \) . In fact the space \( {\Omega }^{{\pi }^{2}} \) of minimal geodesics forms a smooth manifold of dimension \( n \) which can be identified with the equator \( {\mathbb{S}}^{n} \subseteq  {\mathbb{S}}^{n + 1} \) . We will see that this space of minimal geodesics provides a fairly good approximation to the entire loop space \( \Omega \left( {\mathbb{S}}^{n + 1}\right) \) .

![bo_d7du90alb0pc73deir8g_110_603_1167_434_465_0.jpg](images/bo_d7du90alb0pc73deir8g_110_603_1167_434_465_0.jpg)

Let \( M \) be a complete Riemannian manifold, and let \( p, q \in  M \) be two points with distance \( \rho \left( {p, q}\right)  = \sqrt{d} \) .

Theorem 22.1. If the space \( {\Omega }^{d} \) of minimal geodesics from \( p \) to \( q \) is a topological manifold, and if every non-minimal geodesic from \( p \) to \( q \) has index \( \geq  {\lambda }_{0} \) , then the relative homotopy group \( {\pi }_{i}\left( {\Omega ,{\Omega }^{d}}\right) \) is zero for \( 0 \leq  i < {\lambda }_{0} \) .

It follows that the inclusion homomorphism

\[
{\pi }_{i}\left( {\Omega }^{d}\right)  \rightarrow  {\pi }_{i}\left( \Omega \right)
\]

is an isomorphism for \( i \geq  {\lambda }_{0} - 2 \) . But it is well known that the homotopy group \( {\pi }_{i}\left( \Omega \right) \) is isomorphic to \( {\pi }_{i + 1}\left( M\right) \) for all values of \( i \) . (Compare S. T. Hu [Hu59,

p. 111]; together with Theorem 17.1.)

Thus we obtain:

Corollary 22.2. With the same hypotheses, \( {\pi }_{i}\left( {\Omega }^{d}\right) \) is isomorphic to \( {\pi }_{i + 1}\left( M\right) \) for \( 0 \leq  i \leq  {\lambda }_{0} - 2. \)

Let us apply this corollary to the case of two antipodal points on the \( \left( {n + 1}\right) \) - sphere. Evidently the hypotheses are satisfied with \( {\lambda }_{0} = {2n} \) . For any non-minimal geodesic must wind one and a half times around \( {\mathbb{S}}^{n + 1} \) ; and contain two conjugate points, each of multiplicity \( n \) , in its interior. This proves the following.

Corollary 22.3 (The Freudenthal suspension theorem). The homotopy group \( {\pi }_{i}\left( {\mathbb{S}}^{n}\right) \) is isomorphic to \( {\pi }_{i + 1}\left( {\mathbb{S}}^{n + 1}\right) \) for \( i \leq  {2n} - 2 \) .

Theorem 22.1 also implies that the homology groups of the loop space \( \Omega \) are isomorphic to those of \( {\Omega }^{d} \) in dimensions \( \leq  {\lambda }_{0} - 2 \) . This fact follows from Theorem 22.1 together with the relative Hurewicz theorem. (See for example Hu, [Hu59, p. 306]. Compare also [Whi49a, Theorem 2].)

The rest of chapter 22 will be devoted to the proof of Theorem 22.1. The proof will be based on the following lemma, which asserts that the condition "all critical points have index \( \geq  \lambda \) " remains true when a function is jiggled slightly.

Let \( K \) be a compact subset of the Euclidean space \( {\mathbf{R}}^{n} \) ; let \( U \) be a neighborhood of \( K \) ; and let

\[
f : U \rightarrow  \mathbf{R}
\]

be a smooth function such that all critical points of \( f \) in \( K \) have index \( \geq  \lambda \) .

Lemma 22.4. If \( g : U \rightarrow  \mathbf{R} \) is any smooth function which is "close" to \( f \) , in the sense that

\[
\left| {\frac{\partial g}{\partial {x}_{i}} - \frac{\partial f}{\partial {x}_{i}}}\right|  < \varepsilon ,\;\left| {\frac{{\partial }^{2}g}{\partial {x}_{i}\partial {x}_{j}} - \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}}\right|  < \varepsilon ,\;\left( {i, j = 1,\ldots , n}\right)
\]

uniformly throughout \( K \) , for some sufficiently small constant \( \varepsilon \) , then all critical points of \( g \) in \( K \) have index \( \geq  \lambda \) .

(Note that \( f \) is allowed to have degenerate critical points. In the application, \( g \) will be a nearby function without degenerate critical points.)

Proof of Lemma 22.4. The first derivatives of \( g \) are roughly described by the single real valued function

\[
{k}_{g}\left( x\right)  = \mathop{\sum }\limits_{i}\left| \frac{\partial g}{\partial {x}_{i}}\right|  \geq  0
\]

on \( U \) ; which vanishes precisely at the critical points of \( g \) . The second derivatives of \( g \) can be roughly described by \( n \) continuous functions

\[
{e}_{g}^{1},\ldots ,{e}_{g}^{n} : U \rightarrow  \mathbf{R},
\]

as follows. Let

\[
{e}_{g}^{1}\left( x\right)  \leq  {e}_{g}^{2}\left( x\right)  \leq  \cdots  \leq  {e}_{g}^{n}\left( x\right)
\]

denote the \( n \) eigenvalues of the matrix \( \left( \frac{{\partial }^{2}g}{\partial {x}_{i}\partial {x}_{j}}\right) \) . Thus a critical point \( x \) of \( g \) has index \( \geq  \lambda \) if and only if the number \( {e}_{g}^{\lambda }\left( x\right) \) is negative.

The continuity of the functions \( {e}_{g}^{\lambda } \) follows from the fact that the \( \lambda \) -th eigenvalue of a symmetric matrix depends continuously on the matrix \( {}^{1} \) . This can be proved, for example, using the fact that the roots of a complex polynomial of degree \( n \) vary continuously with the coefficient of the polynomial. (Rouche's theorem.)

Let \( {m}_{g}\left( x\right) \) denote the larger of the two numbers \( {k}_{g}\left( x\right) \) and \( - {e}_{g}^{{\lambda }_{0}}\left( x\right) \) . Similarly let \( {m}_{f}\left( x\right) \) denote the larger of the corresponding numbers \( {k}_{f}\left( x\right) \) and \( - {e}_{f}^{{\lambda }_{0}}\left( x\right) \) . The hypothesis that all critical points of \( f \) in \( K \) have index \( \geq  {\lambda }_{0} \) implies that \( - {e}_{f}^{{\lambda }_{0}}\left( x\right)  > 0 \) whenever \( {k}_{f}\left( x\right)  = 0 \) . In other words \( {m}_{f}\left( x\right)  > 0 \) for all \( x \in  K \) .

Let \( \delta  > 0 \) denote the minimum of \( {m}_{f} \) on \( K \) . Now suppose that \( g \) is so close to \( f \) that

\[
\left| {{k}_{g}\left( x\right)  - {k}_{f}\left( x\right) }\right|  < \delta ,\;\left| {{e}_{g}^{{\lambda }_{0}}\left( x\right)  - {e}_{f}^{{\lambda }_{0}}\left( x\right) }\right|  < \delta \tag{22.1}
\]

for all \( x \in  K \) . Then \( {m}_{g}\left( x\right) \) will be positive for \( x \in  K \) ; hence every critical point of \( g \) in \( K \) will have index \( \geq  {\lambda }_{0} \) .

To complete the proof of Lemma 22.4, it is only necessary to show that the inequalities (22.1) will be satisfied providing that

\[
\left| {\frac{\partial g}{\partial {x}_{i}} - \frac{\partial f}{\partial {x}_{i}}}\right|  < \varepsilon ,\;\text{ and }\;\left| {\frac{{\partial }^{2}g}{\partial {x}_{i}\partial {x}_{j}} - \frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}}\right|  < \varepsilon
\]

for sufficiently small \( \varepsilon \) . This follows by a uniform continuity argument which will be left to the reader (or by the footnote above).

We will next prove an analogue of Theorem 22.1 for real valued functions on a manifold.

Let \( f : M \rightarrow  \mathbf{R} \) be a smooth real valued function with minimum 0, such that each \( {M}^{c} = {f}^{-1}\left\lbrack  {0, c}\right\rbrack \) is compact.

Lemma 22.5. If the set \( {M}^{0} \) of minimal points is a manifold, and if every critical point in \( M - {M}^{0} \) has index \( \geq  {\lambda }_{0} \) , then \( {\pi }_{r}\left( {M,{M}^{0}}\right)  = 0 \) for \( 0 \leq  r < {\lambda }_{0} \) .

Proof. First observe that \( {M}^{0} \) is a retract of some neighborhood \( U \subseteq  M \) . In fact Hanner has proved that any manifold \( {M}^{0} \) is an absolute neighborhood retract. (See Theorem 3.3 of O. Hanner, Some theorems on absolute neighborhood retracts, Arkiv för Matematik, Vol. 1 (1950), pp. 389-408.) Replacing \( U \) by a smaller neighborhood if necessary, we may assume that each point of \( U \) is joined to the corresponding point of \( {M}^{0} \) by a unique minimal geodesic. Thus \( U \) can be deformed into \( {M}^{0} \) within \( M \) .

Let \( {\mathrm{I}}^{r} \) denote the unit cube of dimension \( r < {\lambda }_{0} \) , and let

\[
h : \left( {{\mathrm{I}}^{r},{\dot{\mathrm{I}}}^{r}}\right)  \rightarrow  \left( {M,{M}^{0}}\right)
\]

be any map. We must show that \( h \) is homotopic to a map \( {h}^{\prime } \) with \( {h}^{\prime }\left( {\mathrm{I}}^{r}\right)  \subseteq  {M}^{0} \) .

---

\( {}^{1} \) This statement can be sharpened as follows. Consider two \( n \times  n \) symmetric matrices. If corresponding entries of the two matrices differ by at most \( \varepsilon \) , then corresponding eigenvalues differ by at most \( {n\varepsilon } \) . This can be proved using Courant’s minimax definition of the \( \lambda \) -th eigenvalue. (See [Cou19, § 1])

---

Let \( c \) be the maximum of \( f \) on \( h\left( {\mathrm{I}}^{r}\right) \) . Let \( {3\delta } > 0 \) be the minimum of \( f \) on the set \( M - U \) . (The function \( f \) has a minimum on \( M - U \) since each subset \( {M}^{\bar{c}} - U \) is compact.)

Now choose a smooth function

\[
g : {M}^{c + {2\delta }} \rightarrow  \mathbf{R}
\]

which approximates \( f \) closely, but has no degenerate critical points. This is possible by Corollary 6.8. To be more precise the approximation should be so close that:

(1) \( \left| {f\left( x\right)  - g\left( x\right) }\right|  < \delta \) for all \( x \in  {M}^{c + {2\delta }} \) ; and

(2) The index of \( g \) at each critical point which lies in the compact set \( {f}^{-1}\lbrack \delta , c + \; {2\delta }\rbrack \) is \( \geq  {\lambda }_{0} \) .

It follows from Lemma 22.4 that any \( g \) which approximates \( f \) sufficiently closely, the first and second derivatives also being approximated, will satisfy (2). In fact the compact set \( {f}^{-1}\left\lbrack  {\delta , c + {2\delta }}\right\rbrack \) can be covered by finitely many compact set \( {K}_{i} \) , each of which lies in a coordinate neighborhood. Lemma 22.4 can then be applied to each \( {K}_{i} \) .

The proof of Lemma 22.5 now proceeds as follows. The function \( g \) is smooth on the compact region \( {g}^{-1}\left\lbrack  {{2\delta }, c + \delta }\right\rbrack   \subseteq  {f}^{-1}\left\lbrack  {\delta , c + {2\delta }}\right\rbrack \) , and all critical points are nondegenerate, with index \( \geq  {\lambda }_{0} \) . Hence the manifold \( {g}^{-1}( - \infty , c + \delta \rbrack \) has the homotopy type of \( {g}^{-1}( - \infty ,{2\delta }\rbrack \) with cells of dimension \( \geq  {\lambda }_{0} \) attached.

Now consider the map

\[
h : {\mathrm{I}}^{r},{\dot{\mathrm{I}}}^{r} \rightarrow  {M}^{c},{M}^{0} \subseteq  {g}^{-1}( - \infty , c + \delta \rbrack ,{M}^{0}.
\]

Since \( r < {\lambda }_{0} \) it follows that \( h \) is homotopic within \( {g}^{-1}( - \infty , c + \delta \rbrack ,{M}^{0} \) to a map

\[
{h}^{\prime } : {\mathrm{I}}^{r},{\dot{\mathrm{I}}}^{r} \rightarrow  {g}^{-1}( - \infty ,{2\delta }\rbrack ,{M}^{0}.
\]

But this last pair is contained in \( \left( {U,{M}^{0}}\right) \) ; and \( U \) can be deformed into \( {M}^{0} \) within \( M \) . It follows that \( {h}^{\prime } \) is homotopic within \( \left( {M,{M}^{0}}\right) \) to a map \( {h}^{\prime \prime } : {\mathrm{I}}^{r},{\mathrm{I}}^{r} \rightarrow  {M}^{0},{M}^{0} \) . This completes the proof of Lemma 22.5.

The original theorem, 22.1, now can be proved as follows. Clearly it is sufficient to prove that

\[
{\pi }_{i}\left( {\operatorname{Int}{\Omega }^{c},{\Omega }^{d}}\right)  = 0
\]

for arbitrarily large values of \( c \) . As in chapter 16 the space Int \( {\Omega }^{c} \) contains a smooth manifold Int \( {\Omega }^{c}\left( {{t}_{1},\ldots ,{t}_{k}}\right) \) as deformation retract. The space \( {\Omega }^{d} \) of minimal geodesics is contained in this smooth manifold.

The energy function \( E : \Omega  \rightarrow  \mathbf{R} \) , when restricted to Int \( {\Omega }^{c}\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) , almost satisfies the hypothesis of Lemma 22.5. The only difficulty is that \( E\left( m\right) \) ranges over the interval \( d \leq  E < c \) , instead of the required interval \( \lbrack 0,\infty ) \) . To correct this, let

\[
F : \lbrack d, c) \rightarrow  \lbrack 0,\infty )
\]

be any diffeomorphism. Then

\[
F \circ  E : \text{ Int }{\Omega }^{c}\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right)  \rightarrow  \mathbf{R}
\]

satisfies the hypothesis of Lemma 22.5. Hence

\[
{\pi }_{i}\left( {\operatorname{Int}{\Omega }^{c}\left( {{t}_{0},\ldots ,{t}_{k}}\right) ,{\Omega }^{d}}\right)  \cong  {\pi }_{i}\left( {\operatorname{Int}{\Omega }^{c},{\Omega }^{d}}\right)
\]

is zero for \( i < {\lambda }_{0} \) . This completes the proof.
