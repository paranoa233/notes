## §6 The Thom Isomorphism

So far we have encountered two kinds of \( {C}^{\infty } \) invariants of a manifold, de Rham cohomology and compactly supported cohomology. For vector bundles there is another invariant, namely, cohomology with compact support in the vertical direction. The Thom isomorphism is a statement about this last-named cohomology. In this section we use the Mayer-Vietoris argument to prove the Thom isomorphism for an orientable vector bundle. We then explain why the Poincaré dual and the Thom class are in fact one and the same thing. Using the interpretation of the Poincaré dual of a sub-manifold as the Thom class of the normal bundle, it is easy to write down explicitly the Poincaré dual, at least when the normal bundle is trivial. Next we give an explicit construction of the Thom class for an oriented rank 2 bundle, introducing along the way the global angular form and the Euler class. The higher-rank analogues will be taken up in Sections 11 and 12. We conclude this section with a brief discussion of the relative de Rham theory, citing the Thom class as an example of a relative class.

## Vector Bundles and the Reduction of Structure Groups

Let \( \pi  : E \rightarrow  M \) be a surjective map of manifolds whose fiber \( {\pi }^{-1}\left( x\right) \) is a vector space for every \( x \) in \( M \) . The map \( \pi \) is a \( {C}^{\infty } \) real vector bundle of rank \( n \) if there is an open cover \( \left\{  {U}_{\alpha }\right\} \) of \( M \) and fiber-preserving diffeomorphisms

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} = {\pi }^{-1}\left( {U}_{\alpha }\right)  \supset  {U}_{\alpha } \times  {\mathbb{R}}^{n}
\]

which are linear isomorphisms on each fiber. The maps

\[
{\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1} : \left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \times  {\mathbb{R}}^{n} \rightarrow  \left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \times  {\mathbb{R}}^{n}
\]

are vector-space automorphisms of \( {\mathbb{R}}^{n} \) in each fiber and hence give rise to maps

\[
{g}_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  {GL}\left( {n,\mathbb{R}}\right)
\]

\[
{g}_{\alpha \beta }\left( x\right)  = {\left. {\phi }_{\alpha }{\phi }_{\beta  - 1}\right| }_{\{ x\}  \times  {\mathbb{R}}^{n}}.
\]

In the terminology of Section 5 a vector bundle of rank \( n \) is a fiber bundle with fiber \( {\mathbb{R}}^{n} \) and structure group \( {GL}\left( {n,\mathbb{R}}\right) \) . If the fiber is \( {\mathbb{C}}^{n} \) and the structure group is \( {GL}\left( {n,\mathbb{C}}\right) \) , the vector bundle is a complex vector bundle. Unless otherwise stated, by a vector bundle we mean a \( {C}^{\infty } \) real vector bundle.

Let \( U \) be an open set in \( M \) . A map \( s : U \rightarrow  E \) is a section of the vector bundle \( E \) over \( U \) if \( \pi  \circ  s \) is the identity on \( U \) . The space of all sections over \( U \) is written \( \Gamma \left( {U, E}\right) \) . Note that every vector bundle has a well-defined global zero section. A collection of sections \( {s}_{1},\ldots ,{s}_{n} \) over an open set \( U \) in \( M \) is a frame on \( U \) if for every point \( x \) in \( U,{s}_{1}\left( x\right) ,\ldots ,{s}_{n}\left( x\right) \) form a basis of the vector space \( {E}_{x} = {\pi }^{-1}\left( x\right) \) .

The transition functions \( \left\{  {g}_{\alpha \beta }\right\} \) of a vector bundle satisfy the cocycle condition

\[
{g}_{\alpha \beta } \circ  {g}_{\beta \gamma } = {g}_{\alpha \gamma }\text{ on }{U}_{\alpha } \cap  {U}_{\beta } \cap  {U}_{\gamma }.
\]

The cocycle \( \left\{  {g}_{\alpha \beta }\right\} \) depends on the choice of the trivialization.

Lemma 6.1. If the cocycle \( \left\{  {g}_{\alpha \beta }^{\prime }\right\} \) comes from another trivialization \( \left\{  {\phi }_{\alpha }^{\prime }\right\} \) , then there exist maps \( {\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  {GL}\left( {n,\mathbb{R}}\right) \) such that

\[
{g}_{\alpha \beta } = {\lambda }_{\alpha }{g}_{\alpha \beta }^{\prime }{\lambda }_{\beta }^{-1}\;\text{ on }\;{U}_{\alpha } \cap  {U}_{\beta }.
\]

Proof. The two trivializations differ by a nonsingular transformation of \( {\mathbb{R}}^{n} \) at each point:

\[
{\phi }_{\alpha } = {\lambda }_{\alpha }{\phi }_{\alpha }^{\prime }\;,\;{\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  {GL}\left( {n,\mathbb{R}}\right) .
\]

Therefore,

\[
{g}_{\alpha \beta } = {\phi }_{\alpha }{\phi }_{\beta }^{-1} = {\lambda }_{\alpha }{\phi }_{\alpha }^{\prime }{\phi }_{\beta }^{\prime  - 1}{\lambda }_{\beta }^{-1} = {\lambda }_{\alpha }{g}_{\alpha \beta }^{\prime }{\lambda }_{\beta }^{-1}.
\]

Two cocycles related in this way are said to be equivalent.

Given a cocycle \( \left\{  {g}_{\alpha \beta }\right\} \) with values in \( {GL}\left( {n,\mathbb{R}}\right) \) we can construct a vector bundle \( E \) having \( \left\{  {g}_{\alpha \beta }\right\} \) as its cocycle as in (5.10). A homomorphism between two vector bundles, called a bundle map, is a fiber-preserving smooth map \( f : E \rightarrow  {E}^{\prime } \) which is linear on corresponding fibers.

Exercise 6.2. Show that two vector bundles on \( M \) are isomorphic if and only if their cocycles relative to some open cover are equivalent.

Given a vector bundle with cocycle \( \left\{  {g}_{\alpha \beta }\right\} \) , if it is possible to find an equivalent cocycle with values in a subgroup \( H \) of \( {GL}\left( {n,\mathbb{R}}\right) \) , we say that the structure group of \( E \) may be reduced to \( H \) . A vector bundle is orientable if its structure group may be reduced to \( G{L}^{ + }\left( {n,\mathbb{R}}\right) \) , the linear transformations of \( {\mathbb{R}}^{n} \) with positive determinant. A trivialization \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) on \( E \) is said to be oriented if for every \( \alpha \) and \( \beta \) in \( I \) , the transition function \( {g}_{\alpha \beta } \) has positive determinant. Two oriented trivializations \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\}  ,\left\{  \left( {{V}_{\beta },{\psi }_{\beta }}\right) \right\} \) are equivalent if for every \( x \) in \( {U}_{\alpha } \cap  {V}_{\beta },{\phi }_{\alpha } \circ  {\left( {\psi }_{\beta }\right) }^{-1}\left( x\right)  : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) has positive determinant. It is easily checked that this is an equivalence relation and that on a connected manifold \( M \) it partitions all the oriented trivializations of the vector bundle \( E \) into two equivalence classes. Either equivalence class is called an orientation on the vector bundle \( E \) .

Example 6.3 (The tangent bundle). By attaching to each point \( x \) in a manifold \( M \) , the tangent space to \( M \) at \( x \) , we obtain the tangent bundle of \( M \) :

\[
{T}_{M} = \mathop{\bigcup }\limits_{{x \in  M}}{T}_{x}M
\]

Let \( \left\{  \left( {{U}_{a},{\psi }_{a}}\right) \right\} \) be an atlas for \( M \) . The diffeomorphism

\[
{\psi }_{\alpha } : {U}_{\alpha } \rightrightarrows  {\mathbb{R}}^{n}
\]

induces a map

\[
{\left( {\psi }_{a}\right) }_{ * } : {T}_{{U}_{a}} \simeq  {T}_{{\mathbf{R}}^{n}}
\]

which gives a local trivialization of the tangent bundle \( {T}_{M} \) . From this we see that the transition functions of \( {T}_{M} \) are the Jacobians of the transition functions of \( M \) . Therefore \( M \) is orientable as a manifold if and only if its tangent bundle is orientable as a bundle. (However, the total space of the tangent bundle is always orientable as a manifold.) If \( {\psi }_{\alpha } = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) , then \( \partial /\partial {x}_{1},\ldots ,\partial /\partial {x}_{n} \) is a frame for \( {T}_{M} \) over \( {U}_{\alpha } \) . In the language of bundles a smooth vector field on \( {U}_{\alpha } \) is a smooth section of the tangent bundle over \( {U}_{\alpha } \) .

We now show that the structure group of every real vector bundle \( E \) may be reduced to the orthogonal group. First, we can endow \( E \) with a Riemannian structure-a smoothly varying positive definite symmetric bilinear form on each fiber-as follows. Let \( \left\{  {U}_{\alpha }\right\} \) be an open cover of \( M \) which trivializes \( E \) . On each \( {U}_{\alpha } \) , choose a frame for \( {\left. E\right| }_{{U}_{\alpha }} \) and declare it to be orthonormal. This defines a Riemannian structure on \( {\left. E\right| }_{{U}_{\alpha }} \) . Let \( \langle  \cdot  ,{\rangle }_{\alpha } \) denote this inner product on \( {\left. E\right| }_{{U}_{\alpha }} \) . Now use a partition of unity \( \left\{  {\rho }_{\alpha }\right\} \) to splice them together, i.e., form

\[
\langle \;,\;\rangle  = \sum {\rho }_{\alpha }\langle \;,\;{\rangle }_{\alpha }.
\]

This will be an inner product over all of \( M \) .

As trivializations of \( E \) , we take only those maps \( {\phi }_{\alpha } \) that send orthonormal frames of \( E \) (relative to the global metric \( \langle \) , \( \rangle ){toorthonormal} \) frames of \( {\mathbb{R}}^{n} \) -such maps exist by the Gram-Schmidt process. Then the transition functions \( {g}_{\alpha \beta } \) will preserve orthonormal frames and hence take values in the orthogonal group \( O\left( n\right) \) . If the determinant of \( {g}_{\alpha \beta } \) is positive, \( {g}_{\alpha \beta } \) will actually be in the special orthogonal group \( {SO}\left( n\right) \) . Thus

Proposition 6.4. The structure group of a real vector bundle of rank \( n \) can always be reduced to \( O\left( n\right) \) ; it can be reduced to \( {SO}\left( n\right) \) if and only if the vector bundle is orientable.

Exercise 6.5. (a) Show that there is a direct product decomposition

\[
{GL}\left( {n,\mathbb{R}}\right)  = O\left( n\right)  \times  \{ \text{ positive definite symmetric matrices }\} \text{ . }
\]

(b) Use (a) to show that the structure group of any real vector bundle may be reduced to \( O\left( n\right) \) by finding the \( {\lambda }_{\alpha } \) ’s of Lemma 6.1.

## Operations on Vector Bundles

Apart from introducing the functorial operations on vector bundles, our main purpose here is to establish the triviality of a vector bundle over a contractible manifold, a fact needed in the proof of the Thom isomorphism.

Functorial operations on vector spaces carry over to vector bundles. For instance, if \( E \) and \( {E}^{\prime } \) are vector bundles over \( M \) of rank \( n \) and \( m \) respectively, their direct sum \( E \oplus  {E}^{\prime } \) is the vector bundle over \( M \) whose fiber at the point \( x \) in \( M \) is \( {E}_{x} \oplus  {E}_{x}^{\prime } \) . The local trivializations \( \left\{  {\phi }_{\alpha }\right\} \) and \( \left\{  {\phi }_{\alpha }^{\prime }\right\} \) for \( E \) and \( {E}^{\prime } \) induce a local trivialization for \( E \oplus  {E}^{\prime } \) :

\[
{\phi }_{\alpha } \oplus  {\phi }_{\alpha } : {\left. E \oplus  {E}^{\prime }\right| }_{{U}_{\alpha }} \supset  {U}_{\alpha } \times  \left( {{\mathbb{R}}^{n} \oplus  {\mathbb{R}}^{m}}\right) .
\]

Hence the transition matrices for \( E \oplus  {E}^{\prime } \) are

\[
\left( \begin{matrix} {g}_{\alpha \beta } & 0 \\  0 & {g}_{\alpha \beta }^{\prime } \end{matrix}\right) .
\]

Similarly we can define the tensor product \( E \otimes  {E}^{\prime } \) , the dual \( {E}^{ * } \) , and \( \operatorname{Hom}\left( {E,{E}^{\prime }}\right) \) . Note that \( \operatorname{Hom}\left( {E,{E}^{\prime }}\right) \) is isomorphic to \( {E}^{ * } \otimes  {E}^{\prime } \) . The tensor product \( E \otimes  {E}^{\prime } \) clearly has transition matrices \( \left\{  {{g}_{\alpha \beta } \otimes  {g}_{\alpha \beta }^{\prime }}\right\} \) , but the transition matrices for the dual \( {E}^{ * } \) are not so immediate. Recall that the dual \( {V}^{ * } \) of a real vector space \( V \) is the space of all linear functionals on \( V \) , i.e., \( {V}^{ * } \simeq  \operatorname{Hom}\left( {V,\mathbb{R}}\right) \) , and that a linear map \( f : V \rightarrow  W \) induces a map \( {f}^{t} \) : \( {W}^{ * } \rightarrow  {V}^{ * } \) represented by the transpose of the matrix of \( f \) . If

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n}
\]

is a trivialization for \( E \) , then

\[
{\left( {\phi }_{\alpha }^{t}\right) }^{-1} : {\left. {E}^{ * }\right| }_{{U}_{\alpha }} \supset  {U}_{\alpha } \times  {\left( {\mathbb{R}}^{n}\right) }^{ * }
\]

is a trivialization for \( {E}^{ * } \) . Therefore the transition functions of \( {E}^{ * } \) are

(6.6)

\[
{\left( {\phi }_{\alpha }^{t}\right) }^{-1}{\phi }_{\beta }^{t} = {\left( {\left( {\phi }_{\alpha }{\phi }_{\beta }^{-1}\right) }^{t}\right) }^{-1} = {\left( {g}_{\alpha \beta }^{t}\right) }^{-1}.
\]

Let \( M \) and \( N \) be manifolds and \( \pi  : E \rightarrow  M \) a vector bundle over \( M \) . Any map \( f : N \rightarrow  M \) induces a vector bundle \( {f}^{-1}E \) on \( N \) , called the pullback of \( E \) by \( f \) . This bundle \( {f}^{-1}E \) is defined to be the subset of \( N \times  E \) given by

\[
\{ \left( {n, e}\right)  \mid  f\left( n\right)  = \pi \left( e\right) \} .
\]

It is the unique maximal subset of \( N \times  E \) which makes the following diagram commutative

![bo_d7b6f8alb0pc73dd9avg_67_639_427_315_284_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_67_639_427_315_284_0.jpg)

The fiber of \( {f}^{-1}E \) over a point \( y \) in \( N \) is isomorphic to \( {E}_{f\left( y\right) } \) . Since a product bundle pulls back to a product bundle we see that \( {f}^{-1}E \) is locally trivial, and is therefore a vector bundle. Furthermore, if we have a composition

\[
{M}^{\prime \prime }\overset{g}{ \rightarrow  }{M}^{\prime }\overset{f}{ \rightarrow  }M
\]

then

\[
{\left( f \circ  g\right) }^{-1}E = {g}^{-1}\left( {{f}^{-1}E}\right) .
\]

Let \( {\operatorname{Vect}}_{k}\left( M\right) \) be the isomorphism classes of rank \( k \) real vector bundles over \( M \) . It is a pointed set with base point the isomorphism class of the product bundle over \( M \) . If \( f : M \rightarrow  N \) is a map between two manifolds, let \( {\operatorname{Vect}}_{k}\left( f\right)  = {f}^{-1} \) be the pullback map on bundles. In this way, for each integer \( k,{\operatorname{Vect}}_{k}\left( \right) \) becomes a functor from the category of manifolds and smooth maps to the category of pointed sets and base point preserving maps.

REMARK 6.7 Let \( \left\{  {U}_{\alpha }\right\} \) be a trivializing open cover for \( E \) and \( {g}_{\alpha \beta } \) the transition functions. Then \( \left\{  {{f}^{-1}{U}_{\alpha }}\right\} \) is a trivializing open cover for \( {f}^{-1}E \) over \( N \) and \( {\left. \left( {f}^{-1}E\right) \right| }_{{f}^{-1}{U}_{\alpha }} \simeq  {f}^{-1}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) . Therefore the transition functions for \( {f}^{-1}E \) are the pullback functions \( {f}^{ * }{g}_{\alpha \beta } \) .

A basic property of the pullback is the following.

Theorem 6.8 (Homotopy Property of Vector Bundles). Assume \( Y \) to be a compact manifold. If \( {f}_{0} \) and \( {f}_{1} \) are homotopic maps from \( Y \) to a manifold \( X \) and \( E \) is a vector bundle on \( X \) , then \( {f}_{0}^{-1}E \) is isomorphic to \( {f}_{1}^{-1}E \) , i.e., homotopic maps induce isomorphic bundles.

Proof. The problem of constructing an isomorphism between two vector bundles \( V \) and \( W \) of rank \( k \) over a space \( B \) may be turned into a problem in cross-sectioning a fiber bundle over \( B \) , as follows. Recall that \( \operatorname{Hom}\left( {V, W}\right)  = {V}^{ * } \otimes  W \) is a vector bundle over \( B \) whose fiber at each point \( p \) consists of all the linear maps from \( {V}_{p} \) to \( {W}_{p} \) . Define \( \operatorname{Iso}\left( {V, W}\right) \) to be the subset of \( \operatorname{Hom}\left( {V, W}\right) \) whose fiber at each point consists of all the isomorphisms from \( {V}_{p} \) to \( {W}_{p} \) . (This is like looking at the complement of the zero section of a line bundle.) Iso \( \left( {V, W}\right) \) inherits a topology from \( \operatorname{Hom}\left( {V, W}\right) \) , and is a fiber bundle with fiber \( {GL}\left( {n,\mathbb{R}}\right) \) . An isomorphism between \( V \) and \( W \) is simply a section of \( \operatorname{Iso}\left( {V, W}\right) \) .

Let \( f : Y \times  I \rightarrow  X \) be a homotopy between \( {f}_{0} \) and \( {f}_{1} \) , and let \( \pi  : Y \times  I \rightarrow  Y \) be the projection. Suppose for some \( {t}_{0} \) in \( I,{f}_{{t}_{0}}^{-1}E \) is isomorphic to some vector bundle \( F \) on \( Y \) . We will show that for all \( t \) near \( {t}_{0} \) , \( {f}_{t}^{-1}E \simeq  F \) . By the compactness and connectedness of the unit interval \( I \) it will then follow that \( {f}_{t}^{-1}E \simeq  F \) for all \( t \) in \( I \) .

Over \( Y \times  I \) there are two pullback bundles, \( {f}^{-1}E \) and \( {\pi }^{-1}F \) . Since \( {f}_{{t}_{0}}^{-1}E \simeq  F \) , \( \operatorname{Iso}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) has a section over \( Y \times  {t}_{0} \) , which a priori is also a section of \( \operatorname{Hom}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) . Since \( Y \) is compact, \( Y \times  {t}_{0} \) may be covered with a finite number of trivializing open sets for \( \operatorname{Hom}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) (see Figure 6.1). As the fibers of \( \operatorname{Hom}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) are Euclidean spaces, the section over \( Y \times  {t}_{0} \) may be extended to a section of \( \operatorname{Hom}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) over the union of these open sets. Now any linear map near an isomorphism remains an isomorphism; thus we can extend the given section of Iso \( \left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) to a strip containing \( Y \times  {t}_{0} \) . This proves that \( {f}_{t}^{-1}E \simeq  F \) for \( t \) near \( {t}_{0} \) . We now cover \( Y \times  I \) with a finite number of such strips. Hence \( {f}_{0}^{-1}E \simeq  F \simeq  {f}_{1}^{-1}E \) .

![bo_d7b6f8alb0pc73dd9avg_68_469_1211_730_363_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_68_469_1211_730_363_0.jpg)

Figure 6.1

REMARK. If \( Y \) is not compact, we may not be able to find a strip of constant width over which \( \operatorname{Iso}\left( {{f}^{-1}E,{\pi }^{-1}F}\right) \) has a section; for example the strip may look like Figure 6.2.

But the same argument can be refined to give the theorem for \( Y \) a paracompact space. See, for instance, Husemoller [1, Theorem 4.7, p. 29]. Recall that \( Y \) is said to be paracompact if every open cover \( \mathfrak{U} \) of \( Y \) has a locally finite open refinement \( {\mathfrak{U}}^{\prime } \) , that is, every point in \( Y \) has a neighborhood which meets only finitely many open sets in \( {\mathfrak{U}}^{\prime } \) . A compact space or a discrete space are clearly paracompact. By a theorem of A. H. Stone, so is every metric space (Dugundji [1, p. 186]). More importantly for us, every manifold is paracompact (Spivak [1, Ch. 2, Th. 13, p. 66]). Thus the homotopy

![bo_d7b6f8alb0pc73dd9avg_69_511_303_591_422_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_69_511_303_591_422_0.jpg)

Figure 6.2

property of vector bundles (Theorem 6.8) actually holds over any manifold \( Y \) , compact or not.

Corollary 6.9. A vector bundle over a contractible manifold is trivial.

Proof. Let \( E \) be a vector bundle over \( M \) and let \( f \) and \( g \) be maps

\[
M\underset{g}{\overset{f}{ \rightleftarrows  }}\text{ point }
\]

such that \( g \circ  f \) is homotopic to the identity \( {1}_{M} \) . By the homotopy property of vector bundles

\[
E \simeq  {\left( g \circ  f\right) }^{-1}E \simeq  {f}^{-1}\left( {{g}^{-1}E}\right) .
\]

Since \( {g}^{-1}E \) is a vector bundle on a point, it is trivial, hence so is \( {f}^{-1}\left( {{g}^{-1}E}\right) \) .

So for a contractible manifold \( M,{\operatorname{Vect}}_{k}\left( M\right) \) is a single point.

REMARK. Although all the results in this subsection are stated in the differentiable category of manifolds and smooth maps, the corresponding statements with "manifold" replaced by "space" also hold in the continuous category of topological spaces and continuous maps, the only exception being Corollary 6.9, in which the space should be assumed paracompact.

Exercise 6.10. Compute \( {\operatorname{Vect}}_{k}\left( {S}^{1}\right) \) .

Compact Cohomology of a Vector Bundle

The Poincaré lemmas

\[
{H}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  = {H}^{ * }\left( M\right)
\]

\[
{H}_{c}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  = {H}_{c}^{* - n}\left( M\right)
\]

may be viewed as results on the cohomology of the trivial bundle \( M \times  {\mathbb{R}}^{n} \) over \( M \) . More generally let \( E \) be a vector bundle of rank \( n \) over \( M \) . The zero section of \( E, s : x \mapsto  \left( {x,0}\right) \) , embeds \( M \) diffeomorphically in \( E \) . Since \( M \times  \{ 0\} \) is a deformation retract of \( E \) , it follows from the homotopy axiom for de Rham cohomology (Corollary 4.1.2.2) that

\[
{H}^{ * }\left( E\right)  \simeq  {H}^{ * }\left( M\right)
\]

For cohomology with compact support one may suspect that

(6.11)

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

This is in general not true; the open Möbius strip, considered as a vector bundle over \( {S}^{1} \) , provides a counterexample, since the compact cohomology of the Möbius strip is identically zero (Exercise 4.8). However, if \( E \) and \( M \) are orientable manifolds of finite type, then formula (6.11) holds. The proof is based on Poincaré duality, as follows. Let \( m \) be the dimension of \( M \) . Then

\( {H}_{c}^{ * }\left( E\right)  \simeq  {\left( {H}^{m + n -  * }\left( E\right) \right) }^{ * } \) by Poincaré duality on \( E \; \simeq  {\left( {H}^{m + n -  * }\left( M\right) \right) }^{ * } \) by the homotopy axiom for de Rham cohomology \( \simeq  {H}_{c}^{* - n}\left( M\right) \; \) by Poincaré duality on \( M \) .

Lemma 6.12. An orientable vector bundle \( E \) over an orientable manifold \( M \) is an orientable manifold.

Proof. This follows from the fact that if \( \left\{  \left( {{U}_{\alpha },{\psi }_{\alpha }}\right) \right\} \) is an oriented atlas for \( M \) with transition functions \( {h}_{\alpha \beta } = {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1} \) and

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n}
\]

is a local trivialization for \( E \) with transition functions \( {g}_{\alpha \beta } \) , then the composition

\[
{\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{R}}^{n} \simeq  {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}
\]

gives an atlas for \( E \) . The typical transition function of this atlas,

\[
\left( {{\psi }_{\alpha } \times  1}\right)  \circ  {\phi }_{\alpha }{\phi }_{\beta }^{-1} \circ  \left( {{\psi }_{\beta }^{-1} \times  1}\right)  : {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}
\]

sends \( \left( {x, y}\right) \) to \( \left( {{h}_{\alpha \beta }\left( x\right) ,{g}_{\alpha \beta }\left( {{\psi }_{\alpha }^{-1}\left( x\right) }\right) y}\right) \) and has Jacobian matrix

(6.12.1)

\[
\left( \begin{matrix} D\left( {h}_{\alpha \beta }\right) &  * \\  0 & {g}_{\alpha \beta }\left( {{\psi }_{\alpha }^{-1}\left( x\right) }\right)  \end{matrix}\right) ,
\]

where \( D\left( {h}_{\alpha \beta }\right) \) is the Jacobian matrix of \( {h}_{\alpha \beta } \) . The determinant of the matrix (6.12.1) is clearly positive.

Thus,

Proposition 6.13. If \( \pi  : E \rightarrow  M \) is an orientable vector bundle and \( M \) is orientable of finite type, then \( {H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right) \) .

REMARK 6.13.1. Actually the orientability assumption on \( M \) is superfluous. See Exercise 6.20.

REMARK 6.13.2. Let \( M \) be an oriented manifold with oriented atlas \( \left\{  \left( {U}_{\alpha }\right. \right. \) , \( \left. {\psi }_{\alpha }\right\} \) and \( \pi  : E \rightarrow  M \) an oriented vector bundle over \( M \) with an oriented trivialization \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) determining the orientation on the vector bundle (terminology on pp. 54-55). Then \( E \) can be made into an oriented manifold with orientation given by the oriented atlas

\[
\left\{  {{\pi }^{-1}\left( {U}_{\alpha }\right) ,\left( {{\psi }_{\alpha } \times  1}\right)  \circ  {\phi }_{\alpha } : {\pi }^{-1}\left( {U}_{\alpha }\right)  \rightarrow  {U}_{\alpha } \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}}\right\}  .
\]

This is called the local product orientation on \( E \) .

## Compact Vertical Cohomology and Integration along the Fiber

As mentioned earlier, for vector bundles there is a third kind of cohomology. Instead of \( {\Omega }_{c}^{ * }\left( E\right) \) , the complex of forms with compact support, we consider \( {\Omega }_{cv}^{ * }\left( E\right) \) , the complex of forms with compact support in the vertical direction, defined as follows: a smooth \( n \) -form \( \omega \) on \( E \) is in \( {\Omega }_{cv}^{n}\left( E\right) \) if and only if for every compact set \( K \) in \( M,{\pi }^{-1}\left( K\right)  \cap  \operatorname{Supp}\omega \) is compact. If \( \omega  \in  {\Omega }_{cv}^{n}\left( E\right) \) , then since \( \operatorname{Supp}\left( {\left. \omega \right| }_{{\pi }^{-1}\left( x\right) }\right)  \subset  {\pi }^{-1}\left( x\right)  \cap  \operatorname{Supp}\omega \) is a closed subset of a compact set, \( \operatorname{Supp}\left( {\left. \omega \right| }_{{\pi }^{-1}\left( x\right) }\right) \) is compact. Thus, although a form in \( {\Omega }_{cv}^{ * }\left( E\right) \) need not have compact support in \( E \) , its restriction to each fiber has compact support. The cohomology of this complex, denoted \( {H}_{cv}^{ * }\left( E\right) \) , is called the cohomology of \( E \) with compact support in the vertical direction, or compact vertical cohomology.

Let \( E \) be oriented as a rank \( n \) vector bundle. The formulas in (4.4) extend to this situation to give integration along the fiber, \( {\pi }_{ * } : {\Omega }_{cv}^{ * }\left( E\right)  \rightarrow  {\Omega }^{* - n}\left( M\right) \) , as follows. First consider the case of a trivial bundle \( E = M \times  {\mathbb{R}}^{n} \) . Let \( {t}_{1},\ldots ,{t}_{n} \) be the coordinates on the fiber \( {\mathbb{R}}^{n} \) . A form on \( E \) is a real linear combination of two types of forms: the type (I) forms are those which do not contain as a factor the \( n \) -form \( d{t}_{1}\ldots d{t}_{n} \) and the type (II) forms are those which do. The map \( {\pi }_{ * } \) is defined by

(I) \( \left( {\pi  * \phi }\right) f\left( {x,{t}_{1},\ldots ,{t}_{n}}\right) d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} \mapsto  0,\;r < n \) (II) \( \left( {{\pi }^{ * }\phi }\right) f\left( {x,{t}_{1},\ldots ,{t}_{n}}\right) d{t}_{1}\ldots d{t}_{n} \mapsto  \phi {\int }_{{\mathbb{R}}^{n}}f\left( {x,{t}_{1},\ldots ,{t}_{n}}\right) d{t}_{1}\ldots d{t}_{n} \) ,

where \( f \) has compact support for each fixed \( x \) in \( M \) and \( \phi \) is a form on \( M \) . Next suppose \( E \) is an arbitrary oriented vector bundle, with oriented trivialization \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  1} \) . Let \( {x}_{1},\ldots ,{x}_{m} \) and \( {y}_{1},\ldots ,{y}_{m} \) be the coordinate functions on \( {U}_{\alpha } \) and \( {U}_{\beta } \) , and \( {t}_{1},\ldots ,{t}_{n},{u}_{1},\ldots ,{u}_{n} \) the fiber coordinates on \( {\left. E\right| }_{{U}_{\alpha }} \) and \( {\left. E\right| }_{{U}_{\beta }} \) given by \( {\phi }_{\alpha } \) and \( {\phi }_{\beta } \) respectively. Because \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) is an oriented trivialization for \( E \) , the two sets of fiber coordinates \( {t}_{1},\ldots ,{t}_{n} \) and \( {u}_{1}\ldots ,{u}_{n} \) are related by an element of \( G{L}^{ + }\left( {n,\mathbb{R}}\right) \) at each point of \( {U}_{\alpha } \cap  {U}_{\beta } \) . Again a form \( \omega \) in \( {\Omega }_{cv}^{ * }\left( E\right) \) is locally of type (I) or (II). The map \( {\pi }_{ * } \) is defined to be zero on type (I) forms. To define \( {\pi }_{ * } \) on type (II) forms, write \( {\omega }_{\alpha } \) for \( \omega {|}_{\pi  - 1\left( {U}_{\alpha }\right) } \) . Then

\[
{\omega }_{\alpha } = \left( {{\pi }^{ * }\phi }\right) f\left( {{x}_{1},\ldots ,{x}_{m},{t}_{1},\ldots ,{t}_{n}}\right) d{t}_{1}\ldots d{t}_{n}
\]

and

\[
{\omega }_{\beta } = \left( {{\pi }^{ * }\tau }\right) g\left( {{y}_{1},\ldots ,{y}_{m},{u}_{1},\ldots ,{u}_{n}}\right) d{u}_{1}\ldots d{u}_{n}.
\]

Define

\[
{\pi }_{ * }{\omega }_{\alpha } = \phi {\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n}.
\]

Exercise 6.14. Show that if \( E \) is an oriented vector bundle, then \( {\pi }_{ * }{\omega }_{\alpha } = \; {\pi }_{ * }{\omega }_{\beta } \) . Hence \( {\left\{  {\pi }_{ * }{\omega }_{\alpha }\right\}  }_{\alpha  \in  I} \) piece together to give a global form \( {\pi }_{ * }\omega \) on \( M \) . Furthermore, this definition is independent of the choice of the oriented trivialization for \( E \) .

Proposition 6.14.1. Integration along the fiber \( {\pi }_{ * } \) commutes with exterior differentiation d.

Proof. Let \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) be a trivialization for \( E,\left\{  {\rho }_{\alpha }\right\} \) a partition of unity subordinate to \( \left\{  {U}_{\alpha }\right\} \) , and \( \omega \) a form in \( {\Omega }_{cv}^{ * }\left( E\right) \) . Since \( \omega  = \sum {\rho }_{\alpha }\omega \) , and both \( {\pi }_{ * } \) and \( d \) are linear, it suffices to prove the proposition for \( {\rho }_{\alpha }\omega \) , that is, \( {\pi }_{ * }d\left( {{\rho }_{\alpha }\omega }\right)  = d{\pi }_{ * }\left( {{\rho }_{\alpha }\omega }\right) \) . Thus from the outset we may assume \( E \) to be the product bundle \( M \times  {\mathbb{R}}^{n} \) . If \( \omega  = \left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} \) is a type (II) form,

\[
d{\pi }_{ * }\omega  = d\left( {\phi \int f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n}}\right)
\]

\[
= \left( {d\phi }\right) \int f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} + {\left( -1\right) }^{\deg \phi }\phi \mathop{\sum }\limits_{i}d{x}_{i}\int \frac{\partial f}{\partial {x}_{i}}\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n}
\]

and

\[
{\pi }_{ * }{d\omega } = {\pi }_{ * }\left( {\left( {{\pi }^{ * }{d\phi }}\right) {fd}{t}_{1}\ldots d{t}_{n} + {\left( -1\right) }^{\deg \phi }{\pi }^{ * }\phi \sum \frac{\partial f}{\partial {x}_{i}}d{x}_{i}d{t}_{1}\ldots d{t}_{n}}\right)
\]

\[
= \left( {d\phi }\right) \int {fd}{t}_{1}\ldots d{t}_{n} + {\left( -1\right) }^{\deg \phi }\mathop{\sum }\limits_{i}{\phi d}{x}_{i}\int \frac{\partial f}{\partial {x}_{i}}d{t}_{1}\ldots d{t}_{n}.
\]

So \( d{\pi }_{ * }\omega  = {\pi }_{ * }{d\omega } \) for a type (II) form. Next let \( \omega  = \left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right) d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} \) , \( r < n \) , be a type (I) form. Then

\[
d{\pi }_{ * }\omega  = 0
\]

and

\[
{\pi }_{ * }{d\omega } = {\left( -1\right) }^{\deg \phi }\mathop{\sum }\limits_{i}{\pi }_{ * }\left( {\left( {{\pi }^{ * }\phi }\right) \frac{\partial f}{\partial {t}_{i}}\left( {x, t}\right) d{t}_{i}d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}}}\right)
\]

\[
= 0\text{ if }d{t}_{i}d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} \neq   \pm  d{t}_{1}\ldots d{t}_{n}.
\]

If \( d{t}_{i}d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} =  \pm  d{t}_{1}\ldots d{t}_{n} \) , then \( \int \partial f/\partial {t}_{i}\left( {x, t}\right) d{t}_{i}d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} \) is again 0 : because \( f \) has compact support,

\[
{\int }_{-\infty }^{\infty }\frac{\partial f}{\partial {t}_{i}}\left( {x, t}\right) d{t}_{i} = f\left( {\ldots ,\infty ,\ldots }\right)  - f\left( {\ldots , - \infty ,\ldots }\right)  = 0.
\]

Note that integration along the fiber, \( {\pi }_{ * } : {\Omega }_{cv}^{ * }\left( E\right)  \rightarrow  {\Omega }^{* - n}\left( M\right) \) lowers the degree of a form by the fiber dimension.

Proposition 6.15 (Projection Formula). (a) Let \( \pi  : E \rightarrow  M \) be an oriented rank \( n \) vector bundle, \( \tau \) a form on \( M \) and \( \omega \) a form on \( E \) with compact support along the fiber. Then

\[
{\pi }_{ * }\left( {\left( {{\pi }^{ * }\tau }\right)  \cdot  \omega }\right)  = \tau  \cdot  {\pi }_{ * }\omega .
\]

(b) Suppose in addition that \( M \) is oriented of dimension \( m,\omega  \in  {\Omega }_{cv}^{q}\left( E\right) \) , and \( \tau  \in  {\Omega }_{c}^{m + n - q}\left( M\right) \) . Then with the local product orientation on \( E \)

\[
{\int }_{E}\left( {{\pi }^{ * }\tau }\right)  \land  \omega  = {\int }_{M}\tau  \land  {\pi }_{ * }\omega .
\]

PROOF. (a) Since two forms are the same if and only if they are the same locally, we may assume that \( E \) is the product bundle \( M \times  {\mathbb{R}}^{n} \) . If \( \omega \) is a form of type (I), say \( \omega  = {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}} \) , where \( r < n \) , then

\[
{\pi }_{ * }\left( {\left( {{\pi }^{ * }\tau }\right)  \cdot  \omega }\right)  = {\pi }_{ * }\left( {{\pi }^{ * }\left( {\tau \phi }\right)  \cdot  f\left( {x, t}\right) d{t}_{{i}_{1}}\ldots d{t}_{{i}_{r}}}\right) ) = 0 = \tau  \cdot  {\pi }_{ * }\omega .
\]

If \( \omega \) is a form of type (II), say \( \omega  = {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} \) , then

\[
{\pi }_{ * }\left( {\left( {{\pi }^{ * }\tau }\right)  \cdot  \omega }\right)  = {\tau \phi }{\int }_{{\mathbb{R}}^{n}}f\left( {x, t}\right) d{t}_{1}\ldots d{t}_{n} = \tau  \cdot  {\pi }_{ * }\omega .
\]

(b) Let \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  J} \) be an oriented trivialization for \( E \) and \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  J} \) a partition of unity subordinate to \( \left\{  {U}_{\alpha }\right\} \) . Writing \( \omega  = \sum {\rho }_{\alpha }\omega \) , where \( {\rho }_{\alpha }\omega \) has support in \( {U}_{\alpha } \) , we have

and

\[
{\int }_{E}\left( {{\pi }^{ * }\tau }\right)  \land  \omega  = \mathop{\sum }\limits_{\alpha }{\int }_{E{ \mid  }_{{U}_{\alpha }}}\left( {{\pi }^{ * }\tau }\right)  \land  \left( {{\rho }_{\alpha }\omega }\right)
\]

\[
{\int }_{M}\tau  \land  {\pi }_{ * }\omega  = \mathop{\sum }\limits_{\alpha }{\int }_{{U}_{\alpha }}\tau  \land  {\pi }_{ * }\left( {{\rho }_{\alpha }\omega }\right)
\]

Here \( \tau  \land  {\pi }_{ * }\left( {{\rho }_{\alpha }\omega }\right) \) has compact support because its support is a closed subset of the compact set \( \operatorname{Supp}\tau \) ; similarly, \( \left( {{\pi }^{ * }\tau }\right)  \land  \left( {{\rho }_{\alpha }\omega }\right) \) also has compact support. Therefore, it is enough to prove the proposition for \( M = {U}_{\alpha } \) and \( E \) trivial. The rest of the proof proceeds as in (a).

The proof of the Poincaré lemma for compact supports (4.7) carries over verbatim to give

Proposition 6.16 (Poincaré Lemma for Compact Vertical Supports). Integration along the fiber defines an isomorphism

\[
{\pi }_{ * } : {H}_{cv}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  \rightarrow  {H}^{* - n}\left( M\right)
\]

This is a special case of

Theorem 6.17 (Thom Isomorphism). If the vector bundle \( \pi  : E \rightarrow  M \) over a manifold \( M \) of finite type is orientable, then

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( M\right)
\]

where \( n \) is the rank of \( E \) .

Proof. Let \( U \) and \( V \) be open subsets of \( M \) . Using a partition of unity from the base \( M \) we see that

\[
0 \rightarrow  {\Omega }_{cv}^{ * }\left( {\left. E\right| }_{U \cup  V}\right)  \rightarrow  {\Omega }_{cv}^{ * }\left( {\left. E\right| }_{U}\right)  \oplus  {\Omega }_{cv}^{ * }\left( {\left. E\right| }_{V}\right)  \rightarrow  {\Omega }_{cv}^{ * }\left( {\left. E\right| }_{U \cap  V}\right)  \rightarrow  0
\]

is exact, as in (2.3). So we have the diagram of Mayer-Vietoris sequences

\( \begin{matrix} {H}_{cv}\left( {E{ \mid  }_{U \cup  V}}\right)  \rightarrow  {H}_{cv}^{ * }\left( {E{ \mid  }_{U}}\right)  \oplus  {H}_{cv}^{ * }\left( {E{ \mid  }_{V}}\right)  \rightarrow  {H}_{cv}^{ * }\left( {E{ \mid  }_{U \cap  V}}\right)  \rightarrow  {H}_{cv}^{ * }\left( {E{ \mid  }_{U \cup  V}}\right)  \rightarrow  \cdots \\  {\pi }_{ * }\;{\pi }_{ * } \end{matrix} \)

\( \overset{\cdots  \rightarrow  {H}^{ * } - n\left( {U \cup  V}\right) }{ \rightarrow  }{H}^{ * } - n\left( U\right)  \oplus  {H}^{ * } - n\left( V\right)  \rightarrow  {H}^{ * } - n\left( {U \cap  V}\right)  \rightarrow  {H}^{ * } + 1 - n\left( {U \cup  V}\right)  \rightarrow  \cdots \)

The commutativity of this diagram is trivial for the first two squares; we will check that of the third. Recalling from (2.5) the explicit formula for the coboundary operator \( {d}^{ * } \) , we have by the projection formula (6.15)

\[
{\pi }_{ * }{d}^{ * }\omega  = {\pi }_{ * }\left( {\left( {{\pi }^{ * }d{\rho }_{U}}\right)  \cdot  \omega }\right)  = \left( {d{\rho }_{U}}\right)  \cdot  {\pi }_{ * }\omega  = {d}^{ * }{\pi }_{ * }\omega .
\]

So the diagram in question is commutative.

By (6.9) if \( U \) is diffeomorphic to \( {\mathbb{R}}^{n} \) , then \( {\left. E\right| }_{U} \) is trivial, so that in this case the Thom isomorphism reduces to the Poincaré lemma for compact vertical supports (6.16). Hence in the diagram above, \( {\pi }_{ * } \) is an isomorphism for contractible open sets. By the Five Lemma if the Thom isomorphism holds for \( U, V \) , and \( U \cap  V \) , then it holds for \( U \cup  V \) . The proof now proceeds by induction on the cardinality of a good cover for the base, as in the proof of Poincaré duality. This gives the Thom isomorphism for any manifold \( M \) having a finite good cover.

REMARK 6.17.1. Although the proof above works only for a manifold of finite type, the theorem is actually true for any base space. We will reprove the theorem for an arbitrary manifold in (12.2.2).

Under the Thom isomorphism \( \mathcal{T} : {H}^{ * }\left( M\right)  \simeq  {H}_{cv}^{* + n}\left( E\right) \) , the image of 1 in \( {H}^{0}\left( M\right) \) determines a cohomology class \( \Phi \) in \( {H}_{cv}^{n}\left( E\right) \) , called the Thom class of the oriented vector bundle \( E \) . Because \( {\pi }_{ * }\Phi  = 1 \) , by the projection formula (6.15)

\[
{\pi }_{ * }\left( {{\pi }^{ * }\omega  \land  \Phi }\right)  = \omega  \land  {\pi }_{ * }\Phi  = \omega .
\]

So the Thom isomorphism, which is inverse to \( {\pi }_{ * } \) , is given by

\[
\mathcal{T}\left( \;\right)  = {\pi }^{ * }\left( \;\right)  \land  \Phi .
\]

Proposition 6.18. The Thom class \( \Phi \) on a rank \( n \) oriented vector bundle \( E \) can be uniquely characterized as the cohomology class in \( {H}_{cv}^{n}\left( E\right) \) which restricts to the generator of \( {H}_{c}^{n}\left( F\right) \) on each fiber \( F \) .

Proof. Since \( {\pi }_{ * }\Phi  = 1,{\left. \Phi \right| }_{\text{ fiber }} \) is a bump form on the fiber with total integral 1. Conversely if \( {\Phi }^{\prime } \) in \( {H}_{cv}^{n}\left( E\right) \) restricts to a generator on each fiber, then

\[
{\pi }_{ * }\left( {\left( {{\pi }^{ * }\omega }\right)  \land  {\Phi }^{\prime }}\right)  = \omega  \land  {\pi }_{ * }{\Phi }^{\prime } = \omega .
\]

Hence \( {\pi }^{ * }\left( \;\right)  \land  {\Phi }^{\prime } \) must be the Thom isomorphism \( \mathcal{T} \) and \( {\Phi }^{\prime } = \mathcal{T}\left( 1\right) \) is the Thom class.

Proposition 6.19. If \( E \) and \( F \) are two oriented vector bundles over a manifold \( M \) , and \( {\pi }_{1} \) and \( {\pi }_{2} \) are the projections

![bo_d7b6f8alb0pc73dd9avg_75_670_524_287_131_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_75_670_524_287_131_0.jpg)

then the Thom class of \( E \oplus  F \) is \( \Phi \left( {E \oplus  F}\right)  = {\pi }_{1}^{ * }\Phi \left( E\right)  \land  {\pi }_{2}^{ * }\Phi \left( F\right) \) .

Proof. Let \( m = \operatorname{rank}E \) and \( n = \operatorname{rank}F \) . Then \( {\pi }_{1}^{ * }\Phi \left( E\right)  \land  {\pi }_{2}^{ * }\Phi \left( F\right) \) is a class in \( {H}_{cv}^{m + n}\left( {E \oplus  F}\right) \) whose restriction to each fiber is a generator of the compact cohomology of the fiber, since the isomorphism

\[
{H}_{c}^{m + n}\left( {{\mathbb{R}}^{m} \times  {\mathbb{R}}^{n}}\right)  \simeq  {H}_{c}^{m}\left( {\mathbb{R}}^{m}\right)  \otimes  {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right)
\]

is given by the wedge product of the generators.

Exercise 6.20. Using a Mayer-Vietoris argument as in the proof of the Thom isomorphism (Theorem 6.17), show that if \( \pi  : E \rightarrow  M \) is an orient-able rank \( n \) bundle over a manifold \( M \) of finite type, then

\[
{H}_{c}^{ * }\left( E\right)  \simeq  {H}_{c}^{* - n}\left( M\right)
\]

Note that this is Proposition 6.13 with the orientability assumption on \( M \) removed.

## Poincaré Duality and the Thom Class

Let \( S \) be a closed oriented submanifold of dimension \( k \) in an oriented manifold \( M \) of dimension \( n \) . Recall from (5.13) that the Poincaré dual of \( S \) is the cohomology class of the closed \( \left( {n - k}\right) \) -form \( {\eta }_{S} \) characterized by the property

(6.21)

\[
{\int }_{S}\omega  = {\int }_{M}\omega  \land  {\eta }_{S}
\]

for any closed \( k \) -form with compact support on \( M \) . In this section we will explain how the Poincaré dual of a submanifold relates to the Thom class of a bundle (Proposition 6.24). To this end we first introduce the notion of a tubular neighborhood of \( S \) in \( M \) ; this is by definition an open neighborhood of \( S \) in \( M \) diffeomorphic to a vector bundle of rank \( n - k \) over \( S \) such that \( S \) is diffeomorphic to the zero section. Now a sequence of vector bundles over \( M \) ,

\[
0 \rightarrow  E \rightarrow  {E}^{\prime } \rightarrow  {E}^{\prime \prime } \rightarrow  0
\]

is said to be exact if at each point \( p \) in \( M \) , the sequence of vector spaces

\[
0 \rightarrow  {E}_{p} \rightarrow  {E}_{p}^{\prime } \rightarrow  {E}_{p}^{\prime \prime } \rightarrow  0
\]

is exact, where \( {E}_{p} \) is the fiber of \( E \) at \( p \) . If \( S \) is a submanifold in \( M \) , the normal bundle \( N = {N}_{S/M} \) of \( S \) in \( M \) is the vector bundle on \( S \) defined by the exact sequence

(6.22)

\[
0 \rightarrow  {T}_{S} \rightarrow  {T}_{M}{ \mid  }_{S} \rightarrow  N \rightarrow  0
\]

where \( {\left. {T}_{M}\right| }_{s} \) is the restriction of the tangent bundle of \( M \) to \( S \) . The tubular neighborhood theorem states that every submanifold \( S \) in \( M \) has a tubular neighborhood \( T \) , and that in fact \( T \) is diffeomorphic to the normal bundle of \( S \) in \( M \) (see Spivak [1, p. 465] or Guillemin and Pollack [1, p. 76]). For example, if \( S \) is a curve in \( {\mathbb{R}}^{3} \) , then a tubular neighborhood of \( S \) may be constructed using the metric in \( {\mathbb{R}}^{3} \) by attaching to each point of \( S \) an open disc of sufficiently small radius \( \varepsilon  > 0 \) perpendicular to \( S \) at the center. The union of all these discs is a tubular neighborhood of \( S \) (Figure 6.3(a)).

![bo_d7b6f8alb0pc73dd9avg_76_270_888_1113_471_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_76_270_888_1113_471_0.jpg)

Figure 6.3

In general if \( A \) and \( B \) are two oriented vector bundles with oriented trivializations \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( \left\{  \left( {{U}_{\alpha },{\psi }_{\alpha }}\right) \right\} \) , respectively, then the direct sum orientation on \( A \oplus  B \) is given by the oriented trivialization \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha } \oplus  {\psi }_{\alpha }}\right) \right\} \) . Returning to our submanifold \( S \) in \( M \) , we let \( j : T \hookrightarrow  M \) be the inclusion of a tubular neighborhood \( T \) of \( S \) in \( M \) (see Figure 6.3(b)). Since \( S \) and \( M \) are orientable, the normal bundle \( {N}_{S} \) , being the quotient of \( {\left. {T}_{M}\right| }_{s} \) by \( {T}_{S} \) , is also orientable. By convention it is oriented in such a way that

\[
{N}_{S} \oplus  {T}_{S} = {T}_{M} \mid  s
\]

has the direct sum orientation. So the Thom isomorphism theorem applies to the normal bundle \( T = {N}_{S} \) over \( S \) and we have the sequence of maps

![bo_d7b6f8alb0pc73dd9avg_76_532_1937_596_73_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_76_532_1937_596_73_0.jpg)

where \( \Phi \) is the Thom class of the tube \( T \) and \( {j}_{ * } \) is extension by 0 ; here \( {j}_{ * } \) is defined because we are only concerned with forms on the tubular neighborhood \( T \) which vanish near the boundary of \( T \) . We claim that the Poincaré dual of \( S \) is the Thom class of the normal bundle of \( S \) ; more precisely

(6.23)

\[
{\eta }_{S} = {j}_{ * }\left( {\Phi  \land  1}\right)  = {j}_{ * }\Phi \;\text{ in }\;{H}^{n - k}\left( M\right) .
\]

To prove this we merely have to show that \( {j}_{ * }\Phi \) satisfies the defining property (5.13) of the Poincaré dual \( {\eta }_{S} \) . Let \( \omega \) be any closed \( k \) -form with compact support on \( M \) , and \( i : S \rightarrow  T \) the inclusion, regarded as the zero section of the bundle \( \pi  : T \rightarrow  S \) . Since \( \pi \) is a deformation retraction of \( T \) onto \( S,{\pi }^{ * } \) and \( {i}^{ * } \) are inverse isomorphisms in cohomology. Therefore on the level of forms, \( \omega \) and \( {\pi }^{ * }{i}^{ * }\omega \) differ by an exact form: \( \omega  = {\pi }^{ * }{i}^{ * }\omega  + {d\tau } \) .

\[
{\int }_{M}\omega  \land  {j}_{ * }\Phi
\]

\[
= {\int }_{T}\omega  \land  \Phi
\]

\[
= {\int }_{T}\left( {{\pi }^{ * }{i}^{ * }\omega  + {d\tau }}\right)  \land  \Phi
\]

\[
= {\int }_{T}\left( {{\pi }^{ * }{i}^{ * }\omega }\right)  \land  \Phi
\]

theorem

\[
= {\int }_{S}{i}^{ * }\omega  \land  {\pi }_{ * }\Phi \;\text{ by the projection formula (6.15) }
\]

\[
= {\int }_{S}{i}^{ * }\omega \;\text{ because }{\pi }_{ * }\Phi  = 1\text{ . }
\]

This concludes the proof of the claim. Note that if \( S \) is compact, then its Poincaré dual \( {\eta }_{s} = {j}_{ * }\Phi \) has compact support.

Conversely, suppose \( E \) is an oriented vector bundle over an oriented manifold \( M \) . Then \( M \) is diffeomorphically embedded as the zero section in \( E \) and there is an exact sequence

\[
{\left. 0 \rightarrow  {T}_{M} \rightarrow  \left( {T}_{E}\right) \right| }_{M} \rightarrow  E \rightarrow  0
\]

i.e., the normal bundle of \( M \) in \( E \) is \( E \) itself. By (6.23), the Poincaré dual of \( M \) in \( E \) is the Thom class of \( E \) . In summary,

Proposition 6.24. (a) The Poincaré dual of a closed oriented submanifold \( S \) in an oriented manifold \( M \) and the Thom class of the normal bundle of \( S \) can be represented by the same forms.

(b) The Thom class of an oriented vector bundle \( \pi  : E \rightarrow  M \) over an oriented manifold \( M \) and the Poincaré dual of the zero section of \( E \) can be represented by the same form.

Because the normal bundle of the submanifold \( S \) in \( M \) is diffeomorphic to any tubular neighborhood of \( S \) , we have the following proposition.

Proposition 6.25 (Localization Principle). The support of the Poincaré dual of a submanifold S can be shrunk into any given tubular neighborhood of S.

![bo_d7b6f8alb0pc73dd9avg_78_535_299_590_376_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_78_535_299_590_376_0.jpg)

Figure 6.4

Example 6.26.

(a) The Poincaré dual of a point \( p \) in \( M \) .

A tubular neighborhood \( T \) of \( p \) is simply an open ball around \( p \) (Figure 6.4). A generator of \( {H}_{cv}^{n}\left( T\right) \) is a bump \( n \) -form with total integral 1 . So the Poincaré dual of a point is a bump \( n \) -form on \( M \) . The form need not have support at \( p \) since all bump \( n \) -forms on a connected manifold are cohomologous. Here the dual of \( p \) is taken in \( {H}_{c}^{n}\left( M\right) \) , and not in \( {H}^{n}\left( M\right) \) .

(b) The Poincaré dual of \( M \) .

Here the tubular neighborhood \( T \) is \( M \) itself, and \( {H}_{cv}^{ * }\left( T\right)  = {H}^{ * }\left( M\right) \) . So the Poincaré dual of \( M \) is the constant function 1.

(c) The Poincaré dual of a circle on a torus.

![bo_d7b6f8alb0pc73dd9avg_78_642_1274_383_259_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_78_642_1274_383_259_0.jpg)

Figure 6.5

The Poincaré dual is a bump 1-form with support in a tubular neighborhood of the circle and with total integral 1 on each fiber of the tubular neighborhood (Figure 6.5). In the usual representation of the torus as a square, if the circle is a vertical segment, then its Poincaré dual is \( \rho \left( x\right) {dx} \) where \( \rho \) is a bump function with total integral 1 (Figure 6.6).

Using the explicit construction of the Poincaré dual \( {\eta }_{s} = {j}_{ * }\Phi \) as the Thom class of the normal bundle, we now prove two basic properties of Poincaré duality. Two submanifolds \( R \) and \( S \) in \( M \) are said to intersect transversally if and only if

(6.27)

\[
{T}_{x}R + {T}_{x}S = {T}_{x}M
\]

at all points \( x \) in the intersection \( R \cap  S \) (Guillemin and Pollack [1, pp.

![bo_d7b6f8alb0pc73dd9avg_79_632_300_330_327_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_79_632_300_330_327_0.jpg)

Figure 6.6

27-32]). For such a transversal intersection the codimension in \( M \) is additive:

(6.28)

\[
\operatorname{codim}R \cap  S = \operatorname{codim}R + \operatorname{codim}S.
\]

This implies that the normal bundle of \( R \cap  S \) in \( M \) is

(6.29)

\[
{N}_{R \cap  S} = {N}_{R} \oplus  {N}_{S}
\]

Assume \( M \) to be an oriented manifold, and \( R \) and \( S \) to be closed oriented submanifolds. Denoting the Thom class of an oriented vector bundle \( E \) by \( \Phi \left( E\right) \) , we have by (6.19)

(6.30)

\[
\Phi \left( {N}_{R \cap  S}\right)  = \Phi \left( {{N}_{R} \oplus  {N}_{S}}\right)  = \Phi \left( {N}_{R}\right)  \land  \Phi \left( {N}_{S}\right) .
\]

Therefore,

(6.31)

\[
{\eta }_{\mathbf{R} \cap  \mathbf{S}} = {\eta }_{\mathbf{R}} \land  {\eta }_{\mathbf{S}}
\]

i.e., under Poincaré duality the transversal intersection of closed oriented submanifolds corresponds to the wedge product of forms.

More generally, a smooth map \( f : {M}^{\prime } \rightarrow  M \) is said to be transversal to a submanifold \( S \subset  M \) if for every \( x \in  {f}^{-1}\left( S\right) ,{f}_{ * }\left( {{T}_{x}{M}^{\prime }}\right)  + {T}_{f\left( x\right) }S = {T}_{f\left( x\right) }M \) . If \( f : {M}^{\prime } \rightarrow  M \) is an orientation-preserving map of oriented manifolds, \( T \) is a sufficiently small tubular neighborhood of the closed oriented submanifold \( S \) in \( M \) , and \( f \) is transversal to \( S \) and \( T \) , then \( {f}^{-1}T \) is a tubular neighborhood of \( {f}^{-1}S \) in \( {M}^{\prime } \) . From the commutative diagram

![bo_d7b6f8alb0pc73dd9avg_79_395_1672_792_236_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_79_395_1672_792_236_0.jpg)

we see that if \( \omega \) is the cohomology class on \( M \) representing the submanifold \( S \) in \( M \) , then \( {f}^{ * }\omega \) is the cohomology class on \( {M}^{\prime } \) representing \( {f}^{-1}\left( S\right) \) , i.e., under Poincaré duality the induced map on cohomology corresponds to the pre-image in geometry, i.e., \( {\eta }_{{f}^{-1}\left( S\right) } = {f}^{ * }{\eta }_{S} \) . By the Transversality Homotopy Theorem, the transversality hypothesis on \( f \) is in fact not necessary (Guillemin and Pollack [1, p. 70]).

The Global Angular Form, the Euler Class, and the Thom Class

In this subsection we will construct explicitly the Thom class of an oriented rank 2 vector bundle \( \pi  : E \rightarrow  M \) , using such data as a partition of unity on \( M \) and the transition functions of \( E \) . The higher-rank case is similar but more involved, and will be taken up in (11.11) and (12.3). The construction is best understood as the vector-bundle analogue of the procedure for going from a generator of \( {H}^{n - 1}\left( {S}^{n - 1}\right)  = {H}^{n - 1}\left( {{\mathbb{R}}^{n}-\{ 0\} }\right) \) to a generator of \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) . So let us first try to understand the situation in \( {\mathbb{R}}^{n} \) .

We will call a top form on an oriented manifold \( M \) positive if it is in the orientation class of \( M \) . The standard orientation on the unit sphere \( {S}^{n - 1} \) in \( {\mathbb{R}}^{n} \) is by convention the following one: if \( \sigma \) is a generator of \( {H}^{n - 1}\left( {S}^{n - 1}\right) \) and \( \pi  : {\mathbb{R}}^{n} - \{ 0\}  \rightarrow  {S}^{n - 1} \) is a deformation retraction, then \( \sigma \) is positive on \( {S}^{n - 1} \) if and only if \( {dr} \cdot  {\pi }^{ * }\sigma \) is positive on \( {\mathbb{R}}^{n} - \{ 0\} \) .

Exercise 6.32. (a) Show that if \( \theta \) is the standard angle function on \( {\mathbb{R}}^{2} \) , measured in the counterclockwise direction, then \( {d\theta } \) is positive on the circle \( {S}^{1} \) .

(b) Show that if \( \phi \) and \( \theta \) are the spherical coordinates on \( {\mathbb{R}}^{3} \) as in Figure 6.7, then \( {d\phi } \land  {d\theta } \) is positive on the 2-sphere \( {S}^{2} \) .

![bo_d7b6f8alb0pc73dd9avg_80_617_1192_421_423_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_80_617_1192_421_423_0.jpg)

Figure 6.7

Let \( \sigma \) be the positive generator of \( {H}^{n - 1}\left( {S}^{n - 1}\right) \) and \( \psi  = {\pi }^{ * }\sigma \) the corresponding generator of \( {H}^{n - 1}\left( {{\mathbb{R}}^{n}-\{ 0\} }\right) ;\psi \) is called the angular form on \( {\mathbb{R}}^{n} - \{ 0\} \) . If \( \rho \left( r\right) \) is the function of the radius shown in Figure 6.8, then \( {d\rho } = {\rho }^{\prime }\left( r\right) {dr} \) is a bump form on \( {\mathbb{R}}^{1} \) with total integral 1 (Figure 6.9). Therefore \( \left( {d\rho }\right)  \cdot  \psi \) is a compactly supported form on \( {\mathbb{R}}^{n} \) with total integral 1, i.e., \( \left( {d\rho }\right)  \cdot  \psi \) is the generator of \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) . Note that because \( \psi \) is closed, we can write

(6.33)

\[
\left( {d\rho }\right)  \cdot  \psi  = d\left( {\rho  \cdot  \psi }\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_81_429_298_777_520_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_81_429_298_777_520_0.jpg)

Figure 6.8

Now let \( E \) be an oriented rank \( n \) vector bundle over \( M \) , and \( {E}^{0} \) the complement of the zero section in \( E \) . Endow \( E \) with a Riemannian structure as in (6.4) so that the radius function \( r \) makes sense on \( E \) . We begin our construction of the Thom class by finding a global form \( \psi \) on \( {E}^{0} \) whose restriction to each fiber is the angular form on \( {\mathbb{R}}^{n} - \{ 0\} .\psi \) is called the global angular form. Once we have the angular form \( \psi \) , it is then easy to check that \( \Phi  = d\left( {\rho  \cdot  \psi }\right) \) is the Thom class.

Now suppose the rank of \( E \) is 2, and \( \left\{  {U}_{\alpha }\right\} \) is a coordinate open cover of \( M \) that trivializes \( E \) . Since \( E \) has a Riemannian structure, over each \( {U}_{\alpha } \) we can choose an orthonormal frame. This defines on \( {\left. {E}^{0}\right| }_{{U}_{\alpha }} \) polar coordinates \( {r}_{\alpha } \) and \( {\theta }_{\alpha } \) ; if \( {x}_{1},\ldots ,{x}_{n} \) are coordinates on \( {U}_{\alpha } \) , then \( {\pi }^{ * }{x}_{1},\ldots ,{\pi }^{ * }{x}_{n},{r}_{\alpha },{\theta }_{\alpha } \) are coordinates on \( {E}^{0} \mid  {U}_{\alpha } \) . On the overlap \( {U}_{\alpha } \cap  {U}_{\beta } \) , the radii \( {r}_{\alpha } \) and \( {r}_{\beta } \) are equal but the angular coordinates \( {\theta }_{\alpha } \) and \( {\theta }_{\beta } \) differ by a rotation. By the orientability of \( E \) , it makes sense to speak of the "counterclockwise direction" in each fiber. This allows us to define unambiguously \( {\varphi }_{\alpha \beta } \) (up to a constant multiple of \( {2\pi } \) ) as the angle of rotation in the counterclockwise direction from the \( \alpha \) -coordinate system to the \( \beta \) -coordinate system:

(6.34)

\[
{\theta }_{\beta } = {\theta }_{\alpha } + {\pi }^{ * }{\varphi }_{\alpha \beta },{\varphi }_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  \mathbb{R}.
\]

![bo_d7b6f8alb0pc73dd9avg_81_423_1580_781_499_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_81_423_1580_781_499_0.jpg)

Figure 6.9

Although rotating from \( \alpha \) to \( \beta \) and then from \( \beta \) to \( \gamma \) is the same as rotating from \( \alpha \) to \( \gamma \) , it is not true that \( {\varphi }_{\alpha \beta } + {\varphi }_{\beta \gamma } - {\varphi }_{\alpha \gamma } = 0 \) ; indeed all that one can say is

\[
{\varphi }_{\alpha \beta } + {\varphi }_{\beta \gamma } - {\varphi }_{\alpha \gamma } \in  {2\pi }\mathbb{Z}.
\]

ASIDE. To each triple intersection we can associate an integer

(6.35)

\[
{\varepsilon }_{\alpha \beta \gamma } = \frac{1}{2\pi }\left( {{\varphi }_{\alpha \beta } - {\varphi }_{\alpha \gamma } + {\varphi }_{\beta \gamma }}\right) .
\]

The collection of integers \( \left\{  {\varepsilon }_{\alpha \beta \gamma }\right\} \) measures the extent to which \( \left\{  {\varphi }_{\alpha \beta }\right\} \) fails to be a cocyle. We will give another interpretation of \( \left\{  {\varepsilon }_{\alpha \beta \gamma }\right\} \) in Section 11.

Unlike the functions \( \left\{  {\varphi }_{\alpha \beta }\right\} \) , the 1-forms \( \left\{  {d{\varphi }_{\alpha \beta }}\right\} \) satisfy the cocycle condition.

Exercise 6.36. There exist 1-forms \( {\xi }_{\alpha } \) on \( {U}_{\alpha } \) such that

\[
\frac{1}{2\pi }d{\varphi }_{\alpha \beta } = {\xi }_{\beta } - {\xi }_{\alpha }.
\]

[Hint: Take \( {\xi }_{\alpha } = \left( {1/{2\pi }}\right) \mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d{\varphi }_{\gamma \alpha } \) , where \( \left\{  {\rho }_{\gamma }\right\} \) is a partition of unity subordinate to \( \left. \left\{  {U}_{\gamma }\right\}  \right\rbrack \) .]

It follows from Exercise 6.36 that \( d{\xi }_{\alpha } = d{\xi }_{\beta } \) on \( {U}_{\alpha } \cap  {U}_{\beta } \) . Hence the \( d{\xi }_{\alpha } \) piece together to give a global 2-form \( e \) on \( M \) . This global form \( e \) is clearly closed. It is not necessarily exact since the \( {\xi }_{\alpha } \) do not usually piece together to give a global 1-form. The cohomology class of \( e \) in \( {H}^{2}\left( M\right) \) is called the Euler class of the oriented vector bundle \( E \) . We sometimes write \( e\left( E\right) \) instead of \( e \) .

Claim. The cohomology class of \( e \) is independent of the choice of \( \xi \) in our construction.

Proof of CLAIM. If \( \left\{  {\overline{\xi }}_{\alpha }\right\} \) is a different choice of 1-forms such that

\[
\frac{1}{2\pi }d{\varphi }_{\alpha \beta } = {\overline{\xi }}_{\beta } - {\overline{\xi }}_{\alpha } = {\xi }_{\beta } - {\xi }_{\alpha },
\]

then

\[
{\overline{\xi }}_{\beta } - {\xi }_{\beta } = {\overline{\xi }}_{\alpha } - {\xi }_{\alpha } = \xi
\]

is a global form. So \( d{\overline{\xi }}_{\alpha } \) and \( d{\xi }_{\alpha } \) differ by an exact global form.

By (6.34) and (6.36), on \( {\left. {E}^{0}\right| }_{{U}_{x} \cap  {U}_{\beta }} \) ,

(6.36.1)

\[
\frac{d{\theta }_{\alpha }}{2\pi } - {\pi }^{ * }{\xi }_{\alpha } = \frac{d{\theta }_{\beta }}{2\pi } - {\pi }^{ * }{\xi }_{\beta }.
\]

These forms then piece together to give a global 1-form \( \psi \) on \( {E}^{0} \) , the global angular form, whose restriction to each fiber is the angular form \( \left( {1/{2\pi }}\right) {d\theta } \) , i.e., if \( {l}_{p} : {\mathbb{R}}^{2} \rightarrow  E \) is the orthogonal inclusion of a fiber over \( p \) , then \( {l}_{p} * \psi  = \; \left( {1/{2\pi }}\right) {d\theta } \) . The global angular form is not closed:

\[
{d\psi } = d\left( {\frac{d{\theta }_{\alpha }}{2\pi } - {\pi }^{ * }{\xi }_{\alpha }}\right)  =  - {\pi }^{ * }d{\xi }_{\alpha } =  - {\pi }^{ * }d{\xi }_{\beta }.
\]

Therefore,

(6.37)

\[
{d\psi } =  - {\pi }^{ * }e.
\]

When \( E \) is a product, \( \psi \) could be taken to be the pullback of \( \left( {1/{2\pi }}\right) {d\theta } \) under the projection \( {E}^{0} = M \times  \left( {{\mathbb{R}}^{2} - 0}\right)  \rightarrow  {\mathbb{R}}^{2} - 0 \) . In this case \( \psi \) is closed and \( e \) is 0 . The Euler class is in this sense a measure of the twisting of the oriented vector bundle \( E \) .

The Euler class of an oriented rank 2 vector bundle may be given in terms of the transition functions, as follows. Let \( {g}_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  \mathrm{{SO}}\left( 2\right) \) be the transition functions of \( E \) . By identifying \( \mathrm{{SO}}\left( 2\right) \) with the unit circle in the complex plane via \( \left( \begin{matrix} \cos \theta &  - \sin \theta \\  \sin \theta & \cos \theta  \end{matrix}\right)  = {e}^{i\theta },{g}_{\alpha \beta } \) may be thought of as complex-valued functions. In this context the angle from the \( \beta \) -coordinate system to the \( \alpha \) -coordinate system is \( \left( {1/i}\right) \log {g}_{\alpha \beta } \) . Thus

\[
{\theta }_{\alpha } - {\theta }_{\beta } = {\pi }^{ * }\left( {1/i}\right) \log {g}_{\alpha \beta },
\]

and

\[
{\pi }^{ * }{\varphi }_{\alpha \beta } =  - {\pi }^{ * }\left( {1/i}\right) \log {g}_{\alpha \beta }.
\]

Since the projection \( \pi \) has maximal rank (i.e., \( {\pi }_{ * } \) is onto), \( {\pi }^{ * } \) is injective, so that

\[
{\varphi }_{\alpha \beta } =  - \left( {1/i}\right) \log {g}_{\alpha \beta }.
\]

Let \( \left\{  {\rho }_{\gamma }\right\} \) be a partition of unity subordinate to \( \left\{  {U}_{\gamma }\right\} \) . Then

\[
\frac{1}{2\pi }d{\varphi }_{\alpha \beta } = {\xi }_{\beta } - {\xi }_{\alpha }
\]

where

(6.37.1)

\[
{\xi }_{\alpha } = \frac{1}{2\pi }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d{\varphi }_{\gamma \alpha } =  - \frac{1}{2\pi i}\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }.
\]

Therefore,

(6.38)

\[
e\left( E\right)  =  - \frac{1}{2\pi i}\mathop{\sum }\limits_{\gamma }d\left( {{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right) \;\text{ on }{U}_{\alpha }.
\]

Proposition 6.39. The Euler class is functorial, i.e., iff : \( N \rightarrow  M \) is a \( {C}^{\infty } \) map and \( E \) is a rank 2 oriented vector bundle over \( M \) , then

\[
e\left( {{f}^{-1}E}\right)  = {f}^{ * }e\left( E\right) .
\]

Proof. Since the transition functions of \( {f}^{-1}E \) are \( {f}^{ * }{g}_{\alpha \beta } \) , the proposition is an immediate consequence of (6.38).

We claim that just as in the untwisted case (6.33), the Thom class is the cohomology class of

(6.40)

\[
\Phi  = d\left( {\rho \left( r\right)  \cdot  \psi }\right)  = {d\rho }\left( r\right)  \cdot  \psi  - \rho \left( r\right) {\pi }^{ * }e.
\]

In this formula although \( \rho \left( r\right)  \cdot  \psi \) is defined only outside the zero section of \( E \) , the form \( \Phi \) is a global form on \( E \) since \( {d\rho } \equiv  0 \) near the zero section. \( \Phi \) has the following properties:

(a) compact support in the vertical direction;

(b) closed: \( {d\Phi } =  - {d\rho }\left( r\right)  \cdot  {d\psi } - {d\rho }\left( r\right) {\pi }^{ * }e = 0 \) ;

(c) restriction to each fiber has total integral 1 :

\[
{\pi }_{ * }{\iota }_{p}^{ * }\Phi  = {\int }_{0}^{\infty }{\int }_{0}^{2\pi }{d\rho }\left( r\right)  \cdot  \frac{d\theta }{2\pi } = \rho \left( \infty \right)  - \rho \left( 0\right)  = 1,
\]

where \( {\iota }_{p} : {E}_{p} \rightarrow  E \) is the inclusion of the fiber \( {E}_{p} \) into \( E \) ;

(d) the cohomology class of \( \Phi \) is independent of the choice of \( \rho \left( r\right) \) . Suppose \( \overline{\rho }\left( r\right) \) is another function of \( r \) which is -1 near 0 and 0 near infinity, and which defines \( \overline{\Phi } \) . Then

\[
\Phi  - \overline{\Phi } = d\left( {\left( {\rho \left( r\right)  - \overline{\rho }\left( r\right) }\right)  \cdot  \psi }\right)
\]

where \( \left( {\rho \left( r\right)  - \overline{\rho }\left( r\right) }\right)  \cdot  \psi \) is a global form on \( E \) because \( \rho \left( r\right)  - \overline{\rho }\left( r\right) \) vanishes near the zero section.

Therefore \( \Phi \) indeed defines the Thom class. Furthermore, if \( s : M \rightarrow  E \) is the zero section of \( E \) , then

\[
{s}^{ * }\Phi  = d\left( {\rho \left( 0\right) }\right)  \cdot  {s}^{ * }\psi  - \rho \left( 0\right) {s}^{ * }{\pi }^{ * }e = e.
\]

This proves

Proposition 6.41. The pullback of the Thom class to \( M \) by the zero section is the Euler class.

Let \( \left\{  {U}_{\alpha }\right\} \) be a trivializing cover for \( E,\left\{  {\rho }_{\alpha }\right\} \) a partition of unity subordinate to \( \left\{  {U}_{\alpha }\right\} \) , and \( {g}_{\alpha \beta } \) the transition functions for \( E \) . Since

\[
\psi  = \frac{d{\theta }_{\alpha }}{2\pi } - {\pi }^{ * }{\xi }_{\alpha }
\]

\[
= \frac{d{\theta }_{\alpha }}{2\pi } + \frac{1}{2\pi i}{\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }.
\]

(cf. (6.36.1) and (6.37.1)), we have by (6.40),

(6.42)

\[
\Phi  = d\left( {\rho \left( r\right) \frac{d{\theta }_{\alpha }}{2\pi }}\right)  + \frac{1}{2\pi i}d\left( {\rho \left( r\right) {\pi }^{ * }\mathop{\sum }\limits_{\gamma }{\rho }_{\gamma }d\log {g}_{\gamma \alpha }}\right) .
\]

This is the explicit formula for the Thom class.

Exercise 6.43. Let \( \pi  : E \rightarrow  M \) be an oriented rank 2 bundle. As we saw in the proof of the Thom isomorphism, wedging with the Thom class is an isomorphism \( \land  \Phi  : {H}^{ * }\left( M\right)  \simeq  {H}_{cv}^{* + 2}\left( E\right) \) . Therefore every cohomology class on \( E \) is the wedge product of \( \Phi \) with the pullback of a cohomology class on \( M \) . Find the class \( u \) on \( M \) such that

\[
{\Phi }^{2} = \Phi  \land  {\pi }^{ * }u\text{ in }{H}_{cv}^{ * }\left( E\right) .
\]

Exercise 6.44. The complex projective space \( \mathbb{C}{P}^{n} \) is the space of all lines through the origin in \( {\mathbb{C}}^{n + 1} \) , topologized as the quotient of \( {\mathbb{C}}^{n + 1} \) by the equivalence relation

\[
z \sim  {\lambda z}\text{ for }z \in  {\mathbb{C}}^{n + 1},\lambda \text{ a nonzero complex number. }
\]

Let \( {z}_{0},\ldots ,{z}_{n} \) be the complex coordinates on \( {\mathbb{C}}^{n + 1} \) . These give a set of homogeneous coordinates \( \left\lbrack  {{z}_{0},\ldots ,{z}_{n}}\right\rbrack \) on \( \mathbb{C}{P}^{n} \) , determined up to multiplication by a nonzero complex number \( \lambda \) . Define \( {U}_{i} \) to be the open subset of \( \mathbb{C}{P}^{n} \) given by \( {z}_{i} \neq  0.\left\{  {{U}_{0},\ldots ,{U}_{n}}\right\} \) is called the standard open cover of \( \mathbb{C}{P}^{n} \) .

(a) Show that \( \mathbb{C}{P}^{n} \) is a manifold.

(b) Find the transition functions of the normal bundle \( {N}_{\mathbb{C}{P}^{1}/\mathbb{C}{P}^{2}} \) relative to the standard open cover of \( \mathbb{C}{P}^{1} \) .

EXAMPLE 6.44.1. (The Euler class of the normal bundle of \( \mathbb{C}{P}^{1} \) in \( \left. {\mathbb{C}{P}^{2}}\right) \) . Let \( N = {N}_{\mathbb{C}{P}^{1}/\mathbb{C}{P}^{2}} \) be the normal bundle of \( \mathbb{C}{P}^{1} \) in \( \mathbb{C}{P}^{2} \) . Since \( \mathbb{C}{P}^{1} \) is a compact oriented manifold of real dimension 2, its top-dimensional cohomology is \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right)  = \mathbb{R} \) . We will find the Euler class \( e\left( N\right) \) as a multiple of the generator in \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) .

By Exercise 6.44 the transition function of \( N \) relative to the standard open cover is \( {g}_{01} = {z}_{1}/{z}_{0} \) at the point \( \left\lbrack  {{z}_{0},{z}_{1}}\right\rbrack \) . Let \( z = {z}_{1}/{z}_{0} \) be the coordinate of \( {U}_{0} \) , which we identify with the complex plane \( \mathbb{C} \) . Let \( w = {z}_{0}/{z}_{1} = 1/z \) be the coordinate on \( {U}_{1} \simeq  \mathbb{C} \) . Then \( {g}_{01} = z = 1/w \) on \( {U}_{0} \cap  {U}_{1} \) . The Euler class of \( N \) is given by

\[
e\left( N\right)  =  - \frac{1}{2\pi i}d\left( {{\rho }_{0}d\log \frac{1}{w}}\right) \text{ on }{U}_{1}\;\left( {\text{ by }\left( {6.38}\right) }\right)
\]

\[
=  - \frac{1}{2\pi i}d\left( {{\rho }_{0}d\log z}\right) \text{ on }{U}_{0} \cap  {U}_{1},
\]

where \( {\rho }_{0} \) is 1 in a neighborhood of the origin, and 0 in a neighborhood of infinity in the complex \( z \) -plane \( {U}_{0} \simeq  \mathbb{C} \) .

Fix a circle \( C \) in the complex plane with so large a radius that Supp \( {\rho }_{0} \) is contained inside \( C \) . Let \( {A}_{r} \) be the annulus centered at the origin whose outer circle is \( C \) and whose inner circle \( {B}_{r} \) has radius \( r \) (Figure 6.10). Note that as the boundary of \( {A}_{r} \) , the circle \( C \) is oriented counterclockwise while \( B \) is oriented clockwise.

![bo_d7b6f8alb0pc73dd9avg_86_438_1007_798_775_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_86_438_1007_798_775_0.jpg)

Figure 6.10

Now

\[
{\int }_{\mathbb{C}{P}^{1}}e\left( N\right)  =  - \frac{1}{2\pi i}{\int }_{\mathbb{C}}d{\rho }_{0}d\log z
\]

and

\[
{\int }_{\mathbb{C}}d\left( {{\rho }_{0}{dz}/z}\right)  = \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{{A}_{r}}d\left( {{\rho }_{0}{dz}/z}\right)
\]

\[
= \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{C}{\rho }_{0}{dz}/z + {\int }_{{B}_{r}}{\rho }_{0}{dz}/z\;\text{ by Stokes’ theorem }
\]

\[
= \mathop{\lim }\limits_{{r \rightarrow  0}}{\int }_{{B}_{r}}{dz}/z
\]

\[
=  - {2\pi i}\text{ , }
\]

where the minus sign is due to the clockwise orientation on \( {B}_{r} \) . Therefore,

\[
{\int }_{\mathbb{C}{P}^{1}}e\left( N\right)  =  - \frac{1}{2\pi i}\left( {-{2\pi i}}\right)  = 1.
\]

Exercise 6.45. On the complex projective space \( \mathbb{C}{P}^{n} \) there is a tautological line bundle \( S \) , called the universal subbundle; it is the subbundle of the product bundle \( \mathbb{C}{P}^{n} \times  {\mathbb{C}}^{n + 1} \) given by

\[
S = \{ \left( {\ell , z}\right)  \mid  z \in  \ell \} .
\]

Above each point \( \ell \) in \( \mathbb{C}{P}^{n} \) , the fiber of \( S \) is the line represented by \( \ell \) . Find the transition functions of the universal subbundle \( S \) of \( \mathbb{C}{P}^{1} \) relative to the standard open cover and compute its Euler class.

Exercise 6.46. Let \( {S}^{n} \) be the unit sphere in \( {\mathbb{R}}^{n + 1} \) and \( i \) the antipodal map on \( {S}^{n} \) :

\[
i : \left( {{x}_{1},\ldots ,{x}_{n + 1}}\right)  \rightarrow  \left( {-{x}_{1},\ldots , - {x}_{n + 1}}\right) .
\]

The real projective space \( \mathbb{R}{P}^{n} \) is the quotient of \( {S}^{n} \) by the equivalence relation

\[
x \sim  i\left( x\right) ,\;\text{ for }\;x \in  {\mathbb{R}}^{n + 1}
\]

(a) An invariant form on \( {S}^{n} \) is a form \( \omega \) such that \( {i}^{ * }\omega  = \omega \) . The vector space of invariant forms on \( {S}^{n} \) , denoted \( {\Omega }^{ * }{\left( {S}^{n}\right) }^{I} \) , is a differential complex, and so the invariant cohomology \( {H}^{ * }{\left( {S}^{n}\right) }^{I} \) of \( {S}^{n} \) is defined. Show that \( {H}^{ * }\left( {\mathbb{R}{P}^{n}}\right)  \simeq  {H}^{ * }{\left( {S}^{n}\right) }^{I}. \)

(b) Show that the natural map \( {H}^{ * }{\left( {S}^{n}\right) }^{I} \rightarrow  {H}^{ * }\left( {S}^{n}\right) \) is injective. [Hint : If \( \omega \) is an invariant form and \( \omega  = {d\tau } \) for some form \( \tau \) on \( {S}^{n} \) , then \( \omega  = \; d\left( {\tau  + {i}^{ * }\tau }\right) /2 \) .]

(c) Give \( {S}^{n} \) its standard orientation (p. 70). Show that the antipodal map \( i : {S}^{n} \rightarrow  {S}^{n} \) is orientation-preserving for \( n \) odd and orientation-reversing for \( n \) even. Hence, if \( \left\lbrack  \sigma \right\rbrack \) is a generator of \( {H}^{n}\left( {S}^{n}\right) \) , then \( \left\lbrack  \sigma \right\rbrack \) is a nontrivial invariant cohomology class if and only if \( n \) is odd.

(d) Show that the de Rham cohomology of \( \mathbb{R}{P}^{n} \) is

\[
{H}^{q}\left( {\mathbb{R}{P}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ for }q = 0, \\  0 & \text{ for }0 < q < n, \\  \mathbb{R} & \text{ for }q = n\text{ odd, } \\  0 & \text{ for }q = n\text{ even. } \end{array}\right.
\]

Relative de Rham Theory

The Thom class of an oriented vector bundle may be viewed as a relative cohomology class, which we now define. Let \( f : S \rightarrow  M \) be a map between two manifolds. Define a complex \( {\Omega }^{ * }\left( f\right)  = { \oplus  }_{q \geq  0}{\Omega }^{q}\left( f\right) \) by

\[
{\Omega }^{q}\left( f\right)  = {\Omega }^{q}\left( M\right)  \oplus  {\Omega }^{q - 1}\left( S\right)
\]

\[
d\left( {\omega ,\theta }\right)  = \left( {{d\omega },{f}^{ * }\omega  - {d\theta }}\right) .
\]

It is easily verified that \( {d}^{2} = 0 \) . Note that a cohomology class in \( {\Omega }^{ * }\left( f\right) \) is represented by a closed form \( \omega \) on \( M \) which becomes exact when pulled back to \( S \) .

By definition we have the exact sequence

\[
0 \rightarrow  {\Omega }^{q - 1}\left( S\right) \overset{\alpha }{ \rightarrow  }{\Omega }^{q}\left( f\right) \overset{\beta }{ \rightarrow  }{\Omega }^{q}\left( M\right)  \rightarrow  0
\]

with the obvious maps \( \alpha \) and \( \beta  : \alpha \left( \theta \right)  = \left( {0,\theta }\right) \) and \( \beta \left( {\omega ,\theta }\right)  = \omega \) . Clearly \( \beta \) is a chain map but \( \alpha \) is not quite a chain map; in fact it anticommutes with \( d \) , \( {\alpha d} =  - {d\alpha } \) . In any case there is still a long exact sequence in cohomology

(6.47)

\[
\cdots  \rightarrow  {H}^{q - 1}\left( S\right) \overset{{\alpha }^{ * }}{ \rightarrow  }{H}^{q}\left( f\right) \overset{{\beta }^{ * }}{ \rightarrow  }{H}^{q}\left( M\right) \overset{{\delta }^{ * }}{ \rightarrow  }{H}^{q}\left( S\right)  \rightarrow  \cdots
\]

Claim 6.48. \( {\delta }^{ * } = {f}^{ * } \) .

Proof of CLAIM. Consider the diagram

\[
0 \rightarrow  {\Omega }^{q}\left( S\right)  \rightarrow  {\Omega }^{q + 1}\left( f\right)  \rightarrow  {\Omega }^{q + 1}\left( M\right)  \rightarrow  0
\]

\[
d \uparrow  \;d \uparrow  \;d \uparrow
\]

\[
0 \rightarrow  {\Omega }^{q - 1}\left( S\right)  \rightarrow  {\Omega }^{q}\left( f\right)  \rightarrow  {\Omega }^{q}\left( M\right)  \rightarrow  0
\]

\[
\left( {\omega ,\theta }\right) \;\omega
\]

___

Let \( \omega  \in  {\Omega }^{q}\left( M\right) \) be a closed form and \( \left( {\omega ,\theta }\right) \) any element of \( {\Omega }^{q}\left( f\right) \) which maps to \( \omega \) . Then \( d\left( {\omega ,\theta }\right)  = \left( {0,{f}^{ * }\omega  - {d\theta }}\right) \) . So \( {\delta }^{ * }\left\lbrack  \omega \right\rbrack   = \left\lbrack  {{f}^{ * }\omega  - {d\theta }}\right\rbrack   = \left\lbrack  {{f}^{ * }\omega }\right\rbrack \) .

## Combining (6.47) and (6.48) we have

Proposition 6.49. Let \( f : S \rightarrow  M \) be a differentiable map between two manifolds. Then there is an exact sequence

\[
\cdots  \rightarrow  {H}^{q}\left( f\right) \overset{{\beta }^{ * }}{ \rightarrow  }{H}^{q}\left( M\right) \overset{{f}^{ * }}{ \rightarrow  }{H}^{q}\left( S\right) \overset{{\alpha }^{ * }}{ \rightarrow  }{H}^{q + 1}\left( f\right)  \rightarrow  \cdots .
\]

Exercise 6.50. If \( f, g : S \rightarrow  M \) are homotopic maps, show that \( {H}^{ * }\left( f\right) \) and \( {H}^{ * }\left( g\right) \) are isomorphic algebras.

If \( S \) is a submanifold of \( M \) and \( i : S \rightarrow  M \) is the inclusion map, we define the relative de Rham cohomology \( {H}^{q}\left( {M, S}\right) \) to be \( {H}^{q}\left( i\right) \) .

We now turn to the Thom class. Recall that if \( \pi  : E \rightarrow  M \) is a rank 2 oriented vector bundle and \( {E}^{0} \) is the complement of the zero section, then there is a global angular form \( \psi \) on \( {E}^{0} \) such that \( {d\psi } =  - {\pi }^{ * }e \) , where \( e \) represents the Euler class of \( E \) (6.37). Furthermore, if \( s : M \rightarrow  E \) is the zero section, then \( e = {s}^{ * }\Phi \) (Proposition 6.41). Hence, \( {\left( s \circ  \pi \right) }^{ * }\Phi  =  - {d\psi } \) , where \( s \circ  \pi  : {E}^{0} \rightarrow  E \) . This shows that \( \left( {\Phi , - \psi }\right) \) is closed in the complex \( {\Omega }^{ * }\left( {s \circ  \pi }\right) \) and so represents a class in \( {H}^{2}\left( {s \circ  \pi }\right) \) . Since the map \( s \circ  \pi  : {E}^{0} \rightarrow  E \) is clearly homotopic to the inclusion \( i : {E}^{0} \rightarrow  E \) , by Exercise \( {6.50},{H}^{2}\left( {s \circ  \pi }\right)  = {H}^{2}\left( i\right) \) . Hence, \( \left( {\Phi , - \psi }\right) \) represents a class in the relative cohomology \( {H}^{2}\left( {E,{E}^{0}}\right) \) . The rank \( n \) case is entirely analogous and will be taken up in Section 12.
