# 2.1 Euclidean Vector Bundles

For many purposes it is important to study vector bundles in which each fiber has the structure of a Euclidean vector space.

Recall that a real valued function \( \mu \) on a finite dimensional vector space \( V \) is quadratic if \( \mu \) can be expressed in the form

\[
\mu \left( v\right)  = \mathop{\sum }\limits_{i}{\ell }_{i}\left( v\right) {\ell }_{i}^{\prime }\left( v\right) ,
\]

where each \( {\ell }_{i} \) and each \( {\ell }_{i}^{\prime } \) is linear. Each quadratic function determines a symmetric and bilinear pairing \( v, w \mapsto  v \cdot  w \) from \( V \times  V \) to \( \mathbb{R} \) , where

\[
v \cdot  w = \frac{1}{2}\left( {\mu \left( {v + w}\right)  - \mu \left( v\right)  - \mu \left( w\right) }\right) .
\]

Note that \( v \cdot  v = \mu \left( v\right) \) . The quadratic function \( \mu \) is called positive definite if \( \mu \left( v\right)  > 0 \) for \( v \neq  0 \) .

Definition. A Euclidean vector space is a real vector space \( V \) together with a positive definite quadratic function

\[
\mu  : V \rightarrow  \mathbb{R}.
\]

The real number \( v \cdot  w \) will be called the inner product of the vectors \( v \) and \( w \) . The number \( v \cdot  v = \mu \left( v\right) \) may also be denoted by \( {\left| v\right| }^{2} \) .

Definition. A Euclidean vector bundle is a real vector bundle \( \mu \) together with a continuous function

\[
\mu  : E\left( \xi \right)  \rightarrow  \mathbb{R},
\]

such that the restriction of \( \mu \) to each fiber of \( \xi \) is positive definite and quadratic. The function \( \mu \) itself will be called a Euclidean metric on the vector bundle \( \xi \) .

In the case of the tangent bundle \( {\tau }_{M} \) of a smooth manifold, a Euclidean metric

\[
\mu  : \mathbf{T}M \rightarrow  \mathbb{R},
\]

is called a Riemannian metric, and \( M \) together with \( \mu \) is called a Riemannian manifold. (In practice one usually requires that \( \mu \) be a smooth function. The notation \( \mu  = \mathrm{d}{s}^{2} \) is often used for a Riemannian metric.)

Note. In Steenrod's terminology, a Euclidean metric on \( \xi \) gives rise to a reduction of the structural group of \( \xi \) from the full linear group to the orthogonal group. Compare [Ste51, §12.9].

Example 5. The trivial bundle \( {\varepsilon }_{B}^{n} \) can be given the Euclidean metric

\[
\mu \left( {b, x}\right)  = {x}_{1}^{2} + \cdots  + {x}_{n}^{2}.
\]

Since the tangent bundle of \( {\mathbb{R}}^{n} \) is trivial it follows that the smooth manifold \( {\mathbb{R}}^{n} \) possesses a standard Riemannian metric. For any smooth manifold \( M \subset  {\mathbb{R}}^{n} \) the composition

\[
\mathbf{{TM}} \subset  {\mathbf{T}}^{n}\overset{\mu }{ \rightarrow  }\mathbb{R}
\]

now makes \( M \) into a Riemannian manifold.

A priori there appear to be two different concepts of triviality for Euclidean vector bundles; however the next lemma shows that these coincide.

Lemma 2.4. Let \( \xi \) be a trivial vector bundle of dimension \( n \) over \( B \) , and let \( \mu \) be any Euclidean metric on \( \xi \) . Then there exist \( n \) cross-sections \( {s}_{1},\ldots ,{s}_{n} \) of \( \xi \) which are normal and orthogonal in the sense that

\[
{s}_{i}\left( b\right)  \cdot  {s}_{j}\left( b\right)  = {\delta }_{ij}\;\text{ (= Kronecker delta) }
\]

for each \( b \in  B \) .

Thus \( \xi \) is trivial also as a Euclidean vector bundle. (Compare 2-E below.)

Proof. Let \( {s}_{1}^{\prime },\ldots ,{s}_{n}^{\prime } \) be any \( n \) cross-sections which are nowhere linearly dependent. Applying the Gram-Schmidt \( {}^{3} \) process to \( {s}_{1}^{\prime }\left( b\right) ,\ldots ,{s}_{n}^{\prime }\left( b\right) \) we obtain a normal orthogonal basis \( {s}_{1}\left( b\right) ,\ldots ,{s}_{n}^{\prime }\left( b\right) \) for \( {F}_{b}\left( \xi \right) \) . Since the resulting functions \( {s}_{1},\ldots ,{s}_{n} \) are clearly continuous, this completes the proof.

Here are six problems for the reader.

Problem 2-A. Show that the unit sphere \( {S}^{n} \) admits a vector field which is nowhere zero, provided that \( n \) is odd. Show that the normal bundle of \( {S}^{n} \subset  {\mathbb{R}}^{n + 1} \) is trivial for all \( n \) .

Problem 2-B. If \( {S}^{n} \) admits a vector field which is nowhere zero, show that the identity map of \( {S}^{n} \) is homotopic to the antipodal map. For \( n \) even show that the antipodal map of \( {S}^{n} \) is homotopic to the reflection

\[
r\left( {{x}_{1},\ldots ,{x}_{n + 1}}\right)  = \left( {-{x}_{1},{x}_{2},\ldots ,{x}_{n + 1}}\right) ;
\]

and therefore has degree -1. (Compare [ES52, p.304].) Combining these facts, show that \( {S}^{n} \) is not parallelizable for \( n \) even, \( n \geq  2 \) .

---

\( {}^{3} \) See any text book on linear algebra.

---

Problem 2-C (Existence theorem for Euclidean metrics.). Using a partition of unity, show that any vector bundle over a paracompact base space can be given a Euclidean metric. (See 5.3; or see [Kel55, pp. 156 and 171].)

Problem 2-D. The Alexandroff line \( L \) (sometimes called the "long line") is a smooth, connected, 1-dimensional manifold which is not paracompact. (Reference: [Kne58].) Show that \( L \) cannot be given a Riemannian metric.

Problem 2-E (Isometry theorem.). Let \( \mu \) and \( {\mu }^{\prime } \) be two different Euclidean metrics on the same vector bundle \( \xi \) . Prove that there exists a homeomorphism \( f : E\left( \xi \right)  \rightarrow  E\left( \xi \right) \) which carries each fiber isomorphically onto itself, so that the composition \( \mu  \circ  f : E\left( \xi \right)  \rightarrow  \mathbb{R} \) is equal to \( {\mu }^{\prime } \) . [Hint: Use the fact that every positive definite matrix \( A \) can be expressed uniquely as the square of a positive definite matrix \( \sqrt{A} \) . The power series expansion

\[
\sqrt{{tI} + X} = \sqrt{t}\left( {I + \frac{1}{2t}X - \frac{1}{8{t}^{2}}{X}^{2} + \cdots }\right) ,
\]

is valid providing that the characteristic roots of \( {tI} + X = A \) lie between 0 and \( {2t} \) . This shows that the function \( A \mapsto  \sqrt{A} \) is smooth.]

Problem 2-F. As in 1-C, let \( F \) denote the algebra of smooth real valued functions on \( M \) . For each \( x \in  M \) let \( {I}_{X}^{r + 1} \) be the ideal consisting of all functions in \( F \) whose derivatives of order \( \leq  r \) vanish at \( x \) . An element of the quotient algebra \( F/{I}_{X}^{r + 1} \) is called an \( r \) -jet of a real valued function at \( x \) . (Compare [Ehr53].) Construct a locally trivial "bundle of algebras" \( {\mathcal{A}}_{M}^{\left( r\right) } \) over \( M \) with typical fiber \( F/{I}_{X}^{r + 1} \) .
