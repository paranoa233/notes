# Chapter 7 The Lefschetz Theorem on Hyperplane Sections

Based on lecture notes by

M. Spivak and R. Wells

As an application of the ideas which have been developed, we will prove some results concerning the topology of algebraic varieties. These were originally proved by Lefschetz, using quite different arguments. The present version is due to Andreotti and Frankel \( {}^{1} \) .

Theorem 7.1. If \( M \subset  {\mathbb{C}}^{n} \) is a non-singular affine algebraic variety in complex \( n \) -space with real dimension \( {2k} \) , then

\[
{\mathrm{H}}_{i}\left( {M;\mathbb{Z}}\right)  = 0\;\text{ for }i > k.
\]

This is a consequence of the stronger:

Theorem 7.2. A complex analytic manifold \( M \) of complex dimension \( k \) , bianalyt-ically embedded as a closed subset of \( {\mathbb{C}}^{n} \) has the homotopy type of a k-dimensional CW-complex.

The proof will be broken up into several steps. First consider a quadratic form in \( k \) complex variables

\[
\mathrm{Q}\left( {{z}^{1},\ldots ,{z}^{k}}\right)  = \sum {b}_{hj}{z}^{h}{z}^{j}
\]

If we substitute \( {x}^{h} + i{y}^{h} \) for \( {z}^{h} \) , and then take the real part of \( Q \) we obtain a real quadratic form in \( {2k} \) real variables:

\[
{\mathrm{Q}}^{\prime }\left( {{x}^{1},\ldots ,{x}^{k},{y}^{1},\ldots ,{y}^{k}}\right)  = \text{ real part of }\sum {b}_{hj}\left( {{x}^{h} + i{y}^{h}}\right) \left( {{x}^{j} + i{y}^{j}}\right) \text{ . }
\]

Assertion 7.1. If \( \mathrm{e} \) is an eigenvalue of \( {\mathrm{Q}}^{\prime } \) with multiplicity \( \mu \) , then -e is also an eigenvalue with the same multiplicity \( \mu \) .

Proof. The identity \( \mathrm{Q}\left( {i{z}^{1},\ldots , i{z}^{k}}\right)  =  - \mathrm{Q}\left( {{z}^{1},\ldots ,{z}^{k}}\right) \) shows that the quadratic form \( {Q}^{\prime } \) can be transformed into \( - {Q}^{\prime } \) by an orthogonal change of variables. Assertion 7.1 clearly follows.

Now consider a complex manifold \( M \) which is bianalytically imbedded as a subset of \( {\mathbb{C}}^{n} \) . Let \( q \) be a point of \( M \) .

---

\( {}^{1} \) See [Lef24]; and [AF59].

---

Assertion 7.2. The focal points of \( \left( {M, q}\right) \) along any normal line 2 occur in pairs which are situated symmetrically about \( q \) .

In other words if \( q + {tv} \) is a focal point, then \( q - {tv} \) is a focal point with the same multiplicity.

Proof. Choose complex coordinates \( {z}^{1},\ldots ,{z}^{k} \) for \( M \) in a neighborhood of \( q \) so that \( {z}^{1}\left( q\right)  = \cdots  = {z}^{k}\left( q\right)  = 0 \) . The inclusion map \( M \rightarrow  {\mathbb{C}}^{n} \) determines \( n \) complex analytic functions

\[
{w}_{\alpha } = {w}_{\alpha }\left( {{z}^{1},\ldots ,{z}^{k}}\right) ,\;\alpha  = 1,\ldots , n.
\]

Let \( v \) be a fixed unit vector which is orthogonal to \( M \) at \( q \) . Consider the Hermitian inner product

\[
\sum {w}_{\alpha }{\bar{v}}_{\alpha } = \sum {w}_{\alpha }\left( {{z}^{1},\ldots ,{z}^{k}}\right) {\bar{v}}_{\alpha }
\]

of \( w \) and \( v \) . This can be expanded as a complex power series

\[
\sum {w}_{\alpha }\left( {{z}^{1},\ldots ,{z}^{k}}\right) {\bar{v}}_{\alpha } = \text{ constant } + \mathrm{Q}\left( {{z}^{1},\ldots ,{z}^{k}}\right)  + \text{ higher terms, }
\]

where Q denotes a homogeneous quadratic function. (The linear terms vanish since \( v \) is orthogonal to \( M \) .)

Now substitute \( {x}^{h} + i{y}^{h} \) for \( {z}^{h} \) so as to obtain a real coordinate system for \( M \) ; and consider the real inner product

\[
w \cdot  v = \text{ real part of }\sum {w}_{\alpha }{\bar{v}}_{\alpha }.
\]

This function has the real power series expansion

\[
w \cdot  v = \text{ constant } + {\mathrm{Q}}^{\prime }\left( {{x}^{1},\ldots ,{x}^{k},{y}^{1},\ldots ,{y}^{k}}\right)  + \text{ higher terms. }
\]

Clearly the quadratic terms \( {Q}^{\prime } \) determine the second fundamental form of \( M \) at \( q \) in the normal direction \( v \) . By Assertion 7.1 the eigenvalues of \( {\mathrm{Q}}^{\prime } \) occur in equal and opposite pairs. Hence the focal points of \( \left( {M, q}\right) \) along the line through \( q \) and \( q + v \) also occur in symmetric pairs. This proves Assertion 7.2.

Proof of Theorem 7.2. We are now ready to prove Theorem 7.2. Choose a point \( p \in  {\mathbb{C}}^{n} \) so that the squared-distance function

\[
{L}_{p} : M \rightarrow  \mathbf{R}
\]

has no degenerate critical points. Since \( M \) is a closed subset of \( {\mathbb{C}}^{n} \) , it is clear that each set

\[
{M}^{a} = {L}_{p}^{-1}\left\lbrack  {0, a}\right\rbrack
\]

is compact. Now consider the index of \( {L}_{p} \) at a critical point \( q \) . According to Lemma 6.9, this index is equal to the number of focal points of \( \left( {M, q}\right) \) which lie on the line segment from \( p \) to \( q \) . But there are at most \( {2k} \) focal points along the full line through \( p \) and \( q \) ; and these are distributed symmetrically about \( q \) . Hence at most \( k \) of them can lie between \( p \) and \( q \) .

Thus the index of \( {L}_{p} \) at \( q \) is \( \leq  k \) . It follows that \( M \) has the homotopy type of a CW-complex of dimension \( \leq  k \) ; which completes the proof of Theorem 7.2.

Corollary 7.3 (Lefschetz). Let \( V \) be an algebraic variety of complex dimension \( k \) which lies in the complex projective space \( {\mathbb{{CP}}}_{n} \) . Let \( P \) be a hyperplane in \( {\mathbb{{CP}}}_{n} \) which contains the singular points (if any) of \( V \) . Then the inclusion map

\[
V \cap  P \rightarrow  V
\]

induces isomorphisms of homology groups in dimensions less than \( k - 1 \) . Furthermore, the induced homomorphism

\[
{\mathrm{H}}_{k - 1}\left( {V \cap  P;\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}_{k - 1}\left( {V;\mathbb{Z}}\right)
\]

is onto.

Proof. Using the exact sequence of the pair \( \left( {V, V \cap  P}\right) \) it is clearly sufficient to show that \( {\mathrm{H}}_{r}\left( {V, V \cap  P;\mathbb{Z}}\right)  = 0 \) for \( r \leq  k - 1 \) . But the Lefschetz duality theorem asserts that

\[
{\mathrm{H}}_{r}\left( {V, V \cap  P;\mathbb{Z}}\right)  \cong  {\mathrm{H}}^{{2k} - r}\left( {V \smallsetminus  \left( {V \cap  P}\right) ;\mathbb{Z}}\right) .
\]

But \( V \smallsetminus  \left( {V \cap  P}\right) \) is a non-singular algebraic variety in the affine space \( \mathbb{C}{\mathbf{P}}_{n} - P \) . Hence it follows from Theorem 7.2 that the last group is zero for \( r \leq  k - 1 \) .

This result can be sharpened as follows:

Theorem 7.4 (Lefschetz). Under the hypothesis of the preceding corollary, the relative homotopy group \( {\pi }_{r}\left( {V, V \cap  P}\right) \) is zero for \( r < k \) .

Proof. The proof will be based on the hypothesis that some neighborhood \( U \) of \( V \cap  P \) can be deformed into \( V \cap  P \) within \( V \) . This can be proved, for example, using the theorem that algebraic varieties can be triangulated.

In place of the function \( {L}_{p} : V \smallsetminus  \left( {V \cap  P}\right)  \rightarrow  \mathbf{R} \) we will use \( f : V \rightarrow  \mathbf{R} \) where

\[
f\left( x\right)  = \left\{  \begin{array}{ll} 0 & \text{ for }x \in  V \cap  P \\  \frac{1}{{L}_{p}\left( x\right) } & \text{ for }x \notin  P. \end{array}\right.
\]

Since the critical points of \( {}_{L}p \) have index \( \leq  k \) it follows that the critical points of \( f \) have index \( \geq  {2k} - k = k \) . The function \( f \) has no degenerate critical points with \( \varepsilon  \leq  f < \infty \) . Therefore \( V \) has the homotopy type of \( {V}^{\varepsilon } = {f}^{-1}\left\lbrack  {0,\varepsilon }\right\rbrack \) with finitely many cells of dimension \( \geq  k \) attached.

Choose \( \varepsilon \) small enough so that \( {V}^{\varepsilon } \subset  U \) . Let \( {\mathrm{I}}^{r} \) denote the unit \( r \) -cube. Then every map of the pair \( \left( {{\mathrm{I}}^{r},{\dot{\mathrm{I}}}^{r}}\right) \) into \( \left( {V, V \cap  P}\right) \) can be deformed into a map

\[
\left( {{\mathrm{I}}^{r},{\dot{\mathrm{I}}}^{r}}\right)  \rightarrow  \left( {{V}^{\varepsilon }, V \cap  P}\right)  \subset  \left( {U, V \cap  P}\right) ,
\]

since \( r < k \) , and hence can be deformed into \( V \cap  P \) . This completes the proof.

## Part II A Rapid Course in Riemannian Geometry
