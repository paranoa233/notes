# 9 Oriented Bundles and the Euler Class

Up to this point we have always used the coefficient group \( \mathbb{Z}/2 \) for our cohomology. This of necessity means that we have overlooked much interesting structure. Now we will take a closer look, using the integers \( \mathbb{Z} \) as coefficient group. But in order to do this it will be necessary to impose the additional structure of an orientation on our vector bundles. In particular we will need an orientation in order to construct the fundamental cohomology class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) with integer coefficients.

First consider the case of a single vector space.

Definition. An orientation of a real vector space \( V \) of dimension \( n > 0 \) is an equivalence class of bases, where two (ordered) bases \( {v}_{1},\ldots ,{v}_{n} \) and \( {v}_{1}^{\prime },\ldots ,{v}_{n}^{\prime } \) are said to be equivalent if and only if the matrix \( \left\lbrack  {a}_{ij}\right\rbrack \) defined by the equation \( {v}_{i}^{\prime } = \sum {a}_{ij}{v}_{j} \) has positive determinant. Evidently every such vector space \( V \) has precisely two distinct orientations. Note that the coordinate space \( {\mathbb{R}}^{n} \) has a canonical orientation, corresponding to its canonical ordered basis.

In algebraic topology, it is customary to specify the orientation of a simplex by choosing some ordering of its vertices. Our concept of orientation is related as follows. Let \( {\sum }^{n} \) be an \( n \) -simplex, linearly embedded in the \( n \) -dimensional vector space \( V \) , with ordered vertices \( {A}_{0},{A}_{1},\ldots ,{A}_{n} \) . Then taking the vector from \( {A}_{0} \) to \( {A}_{1} \) as first basis vector, the vector from \( {A}_{1} \) to \( {A}_{2} \) as second, and so on, we obtain a corresponding orientation for the vector space \( V \) .

Note that a choice of orientation for \( V \) corresponds to a choice of one of the two possible generators for the singular homology group \( {\mathrm{H}}_{n}\left( {V,{V}_{0};\mathbb{Z}}\right) \) . In fact let \( {\Delta }^{n} \) denote the standard \( n \) -simplex, with canonically ordered vertices. Choose some orientation preserving linear embedding

\[
\sigma  : {\Delta }^{n} \rightarrow  V
\]

which maps the barycenter of \( {\Delta }^{n} \) to the zero vector (and hence maps the bouncary of \( {\Delta }^{n} \) into \( {V}_{0} \) ). Then \( \sigma \) is a singular \( n \) -simplex representing an element in the group of relative \( n \) -cycles \( {Z}_{n}\left( {V,{V}_{0};\mathbb{Z}}\right) \) . The homology class of this \( n \) -cycle \( \sigma \) is now the preferred generator \( {\mu }_{V} \) for the homology group \( {\mathrm{H}}_{n}\left( {V,{V}_{0};\mathbb{Z}}\right) \) .

Similarly the cohomology group \( {\mathrm{H}}^{n}\left( {V,{V}_{0};\mathbb{Z}}\right) \) associated with an oriented vector space \( V \) has a preferred generator which we denote by the symbol \( {u}_{V} \) , determined by the equation \( \left\langle  {{u}_{V},{\mu }_{V}}\right\rangle   =  + 1 \) .

Now consider a vector bundle \( \xi \) of fiber dimension \( n > 0 \) .

Definition. An orientation for \( \xi \) is a function which assigns an orientation to each fiber \( F \) of \( \xi \) , subject to the following local compatibility condition. For every point \( {b}_{0} \) in the base space there should exist a local coordinate system \( \left( {N, h}\right) \) , with \( {b}_{0} \in  n \) and \( h : N \times  {\mathbb{R}}^{n} \rightarrow  {\pi }^{-1}\left( N\right) \) , so that for each fiber \( F = {\pi }^{-1}\left( b\right) \) over \( N \) the homomorphism \( x \mapsto  h\left( {b, x}\right) \) from \( {\mathbb{R}}^{n} \) to \( F \) is orientation preserving. (Or equivalently there should exist sections \( {s}_{1},\ldots ,{s}_{n} : N \rightarrow  {\pi }^{-1}\left( N\right) \) so that the basis \( {s}_{1}\left( b\right) ,\ldots ,{s}_{n}\left( b\right) \) determines the required orientation of \( {\pi }^{-1}\left( b\right) \) for each \( b \) in n.)

In terms of cohomology, this means that to each fiber \( F \) there is assigned a preferred generator

\[
{u}_{F} \in  {\mathrm{H}}^{n}\left( {F,{F}_{0};\mathbb{Z}}\right) \text{ . }
\]

The local compatibility condition implies that for every point in the base space there exists a neighborhood \( N \) and a cohomology class

\[
u \in  {\mathrm{H}}^{n}\left( {{\pi }^{-1}\left( N\right) ,{\pi }^{-1}{\left( N\right) }_{0};\mathbb{Z}}\right)
\]

so that for every fiber \( F \) over \( N \) the restriction

\[
{\left. u\right| }_{\left( F,{F}_{0}\right) } \in  {\mathrm{H}}^{n}\left( {F,{F}_{0};\mathbb{Z}}\right)
\]

is equal to \( {u}_{F} \) . The proof is straightforward.

The following important result will be proved in \( \text{ § }{10} \) (Compare Theorem 8.1)

Theorem 9.1. Let \( \xi \) be an oriented \( n \) -plane bundle with total space \( E \) . Then the cohomology group \( {\mathrm{H}}^{i}\left( {E,{E}_{0};\mathbb{Z}}\right) \) is zero for \( i < n \) , and \( {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) contains one and only one cohomology class \( u \) whose restriction

\[
{\left. u\right| }_{\left( F,{F}_{0}\right) } \in  {\mathrm{H}}^{n}\left( {F,{F}_{0};\mathbb{Z}}\right)
\]

is equal to the preferred generator \( {u}_{F} \) for every fiber \( F \) of \( \xi \) . Furthermore the correspondence \( \mathrm{y} \mapsto  y \smile  u \) maps \( {\mathrm{H}}^{k}\left( {E;\mathbb{Z}}\right) \) isomorphically onto \( {\mathrm{H}}^{k + n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) for every integer \( k \) .

In more technical language, this theorem can be summarized by saying that \( {\mathrm{H}}^{ * }\left( {E,{E}_{0};\mathbb{Z}}\right) \) is a free \( {\mathrm{H}}^{ * }\left( {E;\mathbb{Z}}\right) \) -module on one generator \( u \) of degree \( n \) . (More generally, any ring with unit could be used as coefficient group.)

It follows of course that \( {\mathrm{H}}^{k + n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) is isomorphic to the cohomology group \( {\mathrm{H}}^{k}\left( {B;\mathbb{Z}}\right) \) of the base space. In fact the Thom isomorphism

\[
\phi  : {\mathrm{H}}^{k}\left( {B;\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}^{k + n}\left( {E,{E}_{0};\mathbb{Z}}\right)
\]

can be defined by the formula

\[
\phi \left( x\right)  = \left( {{\pi }^{ * }x}\right)  \smile  u,
\]

just as in \( \text{ § }8 \) .

We are now ready to define an important new characteristic class. Given an oriented \( n \) -plane bundle \( \xi \) , the inclusion \( \left( {E\text{ , empty set }}\right)  \subset  \left( {E,{E}_{0}}\right) \) gives rise to a restriction homomorphism

\[
{\mathrm{H}}^{ * }\left( {E,{E}_{0};\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {E;\mathbb{Z}}\right)
\]

which we denote by \( y \mapsto  {\left. y\right| }_{E} \) . In particular, applying this homomorphism to the fundamental class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) , we obtain a new cohomology class

\[
{\left. u\right| }_{E} \in  {\mathrm{H}}^{n}\left( {E;\mathbb{Z}}\right) .
\]

But \( {\mathrm{H}}^{n}\left( {E;\mathbb{Z}}\right) \) is canonically isomorphic to the cohomology group \( {\mathrm{H}}^{n}\left( {B;\mathbb{Z}}\right) \) of the base space.

Definition. The Euler class of an oriented \( n \) -plane bundle \( \xi \) is the cohomology class

\[
\mathrm{e}\left( \xi \right)  \in  {\mathrm{H}}^{n}\left( {B;\mathbb{Z}}\right)
\]

which corresponds to \( {\left. u\right| }_{E} \) under the canonical isomorphism \( {\pi }^{ * } : {H}^{n}\left( {B;\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}^{n}\left( {E;\mathbb{Z}}\right) . \)

For the motivation for the name "Euler class," we refer the reader to Section 11.5. Here are some fundamental properties of the Euler class:

Property 9.2. (Naturality). If \( f : B \rightarrow  {B}^{\prime } \) is covered by an orientation preserving bundle map \( \xi  \rightarrow  {\xi }^{\prime } \) , then \( \mathrm{e}\left( \xi \right)  = {f}^{ * }\mathrm{e}\left( {\xi }^{\prime }\right) \) .

In particular, if \( \xi \) is a trivial \( n \) -plane bundle, \( n > 0 \) , then \( \mathrm{e}\left( \xi \right)  = 0 \) . For in this case we can take \( {\xi }^{\prime } \) to be a bundle over a point.

Property 9.3. If the orientation of \( \xi \) is reversed, then the Euler class \( \mathrm{e}\left( \xi \right) \) changes sign.

The proofs are immediate.

Property 9.4. If the fiber dimension \( n \) is odd, then \( \mathrm{e}\left( \xi \right)  + \mathrm{e}\left( \xi \right)  = 0 \) .

Because of this, we will usually assume that the fiber dimension is even when making use of Euler classes.

First proof. Any odd dimensional vector bundle possesses an orientation reversing automorphism \( \left( {b, v}\right)  \mapsto  \left( {b, - v}\right) \) . The required equation \( \mathrm{e}\left( \xi \right)  =  - \mathrm{e}\left( \xi \right) \) now follows from 9.3.

Alternate proof. The Thom isomorphism \( \phi \left( x\right)  = {\pi }^{ * }\left( x\right)  \smile  u \) evidently maps \( \mathrm{e}\left( \xi \right) \) to the cohomology class

\[
{\pi }^{ * }\mathrm{e}\left( \xi \right)  \smile  u = \left( {\left. u\right| }_{E}\right)  \smile  u = u \smile  u.
\]

In other words

\[
\mathrm{e}\left( \xi \right)  = {\phi }^{-1}\left( {u \smile  u}\right) .
\]

But using the identity

\[
a \smile  b = {\left( -1\right) }^{\left( {\dim a}\right) \left( {\dim b}\right) }b \smile  a
\]

we see that \( u \smile  u \) is an element of order 2 whenever the dimension \( n \) is odd.

Property 9.5. The natural homomorphism \( {\mathrm{H}}^{n}\left( {B;\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}^{n}\left( {B;\mathbb{Z}/2}\right) \) carries the Euler class \( \mathrm{e}\left( \xi \right) \) to the top Stiefel-Whitney class \( {\mathrm{w}}_{n}\left( \xi \right) \) .

Proof. If we apply this homomorphism (induced by the coefficient surjection \( \mathbb{Z} \rightarrow  \mathbb{Z}/2) \) to both sides of the equation \( \mathrm{e}\left( \xi \right)  = {\phi }^{-1}\left( {u \smile  u}\right) \) , then evidently the integer cohomology class \( u \) maps to the mod 2 cohomology class \( u \) of \( \text{ § }8 \) , and \( u \smile  u \) maps to \( {\mathrm{{Sq}}}^{n}\left( u\right) \) . Hence \( {\phi }^{-1}\left( {u \smile  u}\right) \) maps to \( {\phi }^{-1}{\mathrm{{Sq}}}^{n}\left( u\right)  = {\mathrm{w}}_{n}\left( \xi \right) \)

Several important properties of the characteristic class \( {\mathrm{w}}_{n}\left( \xi \right) \) apply equally well to \( \mathrm{e}\left( \xi \right) \) .

Property 9.6. The Euler class of a Whitney sum is given by \( \mathrm{e}\left( {\xi  \oplus  {\xi }^{\prime }}\right)  = \mathrm{e}\left( \xi \right)  \smile  \mathrm{e}\left( {\xi }^{\prime }\right) \) . Similarly the Euler class of a cartesian product is given by \( \mathrm{e}\left( {\xi  \times  {\xi }^{\prime }}\right)  = \mathrm{e}\left( \xi \right)  \times  \mathrm{e}\left( {\xi }^{\prime }\right) \) .

Here we must specify that the direct sum \( F \oplus  {F}^{\prime } \) of two oriented vector spaces is to be oriented by taking an oriented basis for \( F \) followed by an oriented basis for \( {F}^{\prime } \) .

proof of 9.6. Let the fiber dimensions be \( m \) and \( n \) respectively. Taking account of our sign conventions as specified in Appendix A, it is not difficult to check that the fundamental cohomology class of the Cartesian product is given by

\[
u\left( {\xi  \times  {\xi }^{\prime }}\right)  = {\left( -1\right) }^{mn}u\left( \xi \right)  \times  u\left( {\xi }^{\prime }\right) .
\]

(Compare the verification of Axiom 3 in \( \text{ § }8 \) . If we used the classical system of sign conventions, as in [Spa81], then there would be no sign here.) Now apply the restriction homomorphism

\[
{\mathrm{H}}^{m + n}\left( {E \times  {E}^{\prime },{\left( E \times  {E}^{\prime }\right) }_{0}}\right)  \rightarrow  {\mathrm{H}}^{m + n}\left( {E \times  {E}^{\prime }}\right)  \approx  {\mathrm{H}}^{m + n}\left( {B \times  {B}^{\prime }}\right)
\]

to both sides. It follows easily that

\[
\mathrm{e}\left( {\xi  \times  {\xi }^{\prime }}\right)  = {\left( -1\right) }^{mn}\mathrm{e}\left( \xi \right)  \times  \mathrm{e}\left( {\xi }^{\prime }\right) ;
\]

where the sign can be ignored since the right side of this equation is an element of order two whenever \( m \) or \( n \) is odd.

Now suppose that \( B = {B}^{\prime } \) . Pulling both sides of this equation back to \( {\mathrm{H}}^{m + n}\left( {B;\mathbb{Z}}\right) \) by means of the diagonal embedding \( B \rightarrow  B \times  B \) , we obtain the formula \( \mathrm{e}\left( {\xi  \oplus  {\xi }^{\prime }}\right)  = \mathrm{e}\left( {\xi }^{\prime }\right)  \smile  \mathrm{e}\left( {\xi }^{\prime }\right) \) for the Euler class of a Whitney sum.

Remark. Although this formula looks very much like the corresponding formula \( \mathrm{w}\left( {\xi  \oplus  {\xi }^{\prime }}\right)  = \mathrm{w}\left( \xi \right)  \smile  \mathrm{w}\left( {\xi }^{\prime }\right) \) for Stiefel-Whitney classes, there is one essential difference. The total Stiefel-Whitney class \( \mathrm{w}\left( \xi \right) \) is a unit in the ring \( {H}^{\Pi }\left( {B;\mathbb{Z}/2}\right) \) , hence it is easy to solve for \( \mathrm{w}\left( {\xi }^{\prime }\right) \) as a function of \( \mathrm{w}\left( \xi \right) \) and \( \mathrm{w}\left( {\xi  \oplus  {\xi }^{\prime }}\right) \) . (Compare 4.1.) However the Euler class \( \mathrm{e}\left( \xi \right) \) is certainly not a unit in the integral cohomology ring of \( B \) , and in fact it may well be zero or a zero-divisor. So the equation \( \mathrm{e}\left( {\xi  \oplus  {\xi }^{\prime }}\right)  = \mathrm{e}\left( \xi \right)  \smile  \mathrm{e}\left( {\xi }^{\prime }\right) \) cannot usually be solved for \( \mathrm{e}\left( {\xi }^{\prime }\right) \) as a function of \( \mathrm{e}\left( \xi \right) \) and \( \mathrm{e}\left( {\xi  \oplus  {\xi }^{\prime }}\right) \)

Here is an application of 9.6. Let \( \eta \) be a vector bundle for which \( 2\mathrm{e}\left( \eta \right)  \neq  0 \) . Then it follows that \( \eta \) cannot split as the Whitney sum of two oriented odd dimensional vector bundles. As an example, let \( M \) be a smooth compact manifold. Suppose that the tangent bundle \( \tau \) of \( M \) is oriented, and that \( \mathrm{e}\left( \tau \right)  \neq  0 \) . Then \( \tau \) cannot admit any odd dimensional sub vector bundle. For if this sub-bundle \( \xi \) were orientable, then the Euler class \( \mathrm{e}\left( \tau \right)  = \mathrm{e}\left( \xi \right)  \smile  \mathrm{e}\left( {\xi }^{ \bot  }\right) \) would have to be an element of order two in the free abelian group \( {\mathrm{H}}^{n}\left( {M;\mathbb{Z}}\right) \) . (Compare Appendix A.) The case where \( \xi \) is not orientable can be handled by passing to a suitable 2-fold covering manifold of \( M \) . Details will be left to the reader.

Property 9.7. If the oriented vector bundle \( \xi \) possesses a nowhere zero cross-section, then the Euler class \( \mathrm{e}\left( \xi \right) \) must be zero.

Proof. Let \( s : B \rightarrow  {E}_{0} \) be a cross-section, so that the composition

\[
B\overset{s}{ \rightarrow  }{E}_{0} \subset  E\overset{\pi }{ \rightarrow  }B
\]

is the identity map of \( B \) . Then the corresponding composition

\[
{\mathrm{H}}^{n}\left( B\right) \overset{{\pi }^{ * }}{ \rightarrow  }{\mathrm{H}}^{n}\left( E\right)  \rightarrow  {\mathrm{H}}^{n}\left( {E}_{0}\right) \overset{{s}^{ * }}{ \rightarrow  }{\mathrm{H}}^{n}\left( B\right)
\]

is the identity map of \( {\mathrm{H}}^{n}\left( B\right) \) . By definition the first homomorphism \( {\pi }^{ * } \) maps \( \mathrm{e}\left( \xi \right) \) to the restriction \( {\left. u\right| }_{E} \) . Hence the first two homomorphisms in this composition map \( \mathrm{e}\left( \xi \right) \) to the restriction \( {\left. \left( {\left. u\right| }_{E}\right) \right| }_{{E}_{0}} \) which is zero since the composition

\[
{\mathrm{H}}^{n}\left( {E,{E}_{0}}\right)  \rightarrow  {\mathrm{H}}^{n}\left( E\right)  \rightarrow  {\mathrm{H}}^{n}\left( {E}_{0}\right)
\]

is zero. Applying \( {s}^{ * } \) , it follows that \( \mathrm{e}\left( \xi \right)  = {s}^{ * }\left( 0\right)  = 0 \) .

[If the bundle \( \xi \) possesses a Euclidean metric, then an alternative proof can be given as follows: Let \( \varepsilon \) be the trivial line bundle spanned by the cross-section \( s \) of \( \xi \) . Then

\[
\mathrm{e}\left( \xi \right)  = \mathrm{e}\left( \varepsilon \right)  \smile  \mathrm{e}\left( {\varepsilon }^{ \bot  }\right)
\]

by 9.6, where the class \( \mathrm{e}\left( \varepsilon \right) \) is zero by 9.2]

To conclude this section we will describe some examples of bundles with nonzero Euler class. (See also \( \text{ § }{11} \) and \( \text{ § }{15} \) .)

Problem 9-A. Recall that \( {\gamma }^{n} \) denotes the canonical \( n \) -plane bundle over the infinite Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) . Show that \( {\gamma }^{n} \oplus  {\gamma }^{n} \) is an orientable vector bundle with \( {\mathrm{w}}_{2n}\left( {{\gamma }^{n} \oplus  {\gamma }^{n}}\right)  \neq  0 \) , and hence \( \mathrm{e}\left( {{\gamma }^{n} \oplus  {\gamma }^{n}}\right)  \neq  0 \) . If \( n \) is odd, show that \( 2\mathrm{e}\left( {{\gamma }^{n} \oplus  {\gamma }^{n}}\right)  = 0. \)

Problem 9-B. Now consider the complex Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{C}}^{\infty }\right) \) , consisting of all complex sub vector spaces of complex dimension \( n \) in infinite complex coordinate space. (Compare §14.) Since every complex \( n \) -plane can be thought of as a real oriented \( {2n} \) -plane, it follows that there is a canonical oriented \( {2n} \) - plane bundle \( {\xi }^{2n} \) over \( {\operatorname{Gr}}_{n}\left( {\mathbb{C}}^{\infty }\right) \) . Show that the restriction of \( {\xi }^{2n} \) to the real sub-space \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) is isomorphic to \( {\gamma }^{n} \oplus  {\gamma }^{n} \) , and hence that \( \mathrm{e}\left( {\xi }^{2n}\right)  \neq  0 \) . (Remark: The group \( {\mathrm{H}}^{2n}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) is actually free abelian, with \( \mathrm{e}\left( {\xi }^{2n}\right) \) as one of its generators. See Lemma 14.3.

Problem 9-C. Let \( \tau \) be the tangent bundle of the n-sphere, and let \( A \subset  {S}^{n} \times  {S}^{n} \) be the anti-diagonal, consisting of all pairs of antipodal unit vectors. Using stereographic projection, show that the total space \( E = E\left( \tau \right) \) is canonically homeomorphic to \( {S}^{n} \times  {S}^{n} - A \) . Hence, using excision and homotopy, show that

\[
{\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right)  \approx  {\mathrm{H}}^{ * }\left( {{S}^{n} \times  {S}^{n},{S}^{n} \times  {S}^{n} - \text{ diagonal }}\right)  \approx  {\mathrm{H}}^{ * }\left( {{S}^{n} \times  {S}^{n}, A}\right)  \subset  {\mathrm{H}}^{ * }\left( {{S}^{n} \times  {S}^{n}}\right)
\]

(Compare \( \text{ § }{11} \) .) Now suppose that \( n \) is even. Show that the Euler class \( \mathrm{e}\left( \tau \right)  = {\phi }^{-1}\left( {u \smile  u}\right) \) is twice a generator of \( {\mathrm{H}}^{n}\left( {{S}^{n};\mathbb{Z}}\right) \) . As a corollary, show that \( \tau \) possesses no non-trivial sub vector bundles.
