# 3 Constructing New Vector Bundles Out of Old

This section will describe a number of basic constructions involving vector bundles.

(a) Restricting a bundle to a subset of the base space.

Let \( \xi \) be a vector bundle with projection \( \pi  : E \rightarrow  B \) and let \( \bar{B} \) be a subset of \( B \) . Setting \( \bar{E} = {\pi }^{-1}\left( \bar{B}\right) \) , and letting

\[
\overline{\pi } : \bar{E} \rightarrow  \bar{B}
\]

be the restriction of \( \pi \) to \( \bar{E} \) , one obtains a new vector bundle which will be denoted by \( {\left. \xi \right| }_{\bar{B}} \) , and called the restriction of \( \xi \) to \( \bar{B} \) . Each fiber \( {F}_{b}\left( {\left. \xi \right| }_{\bar{B}}\right) \) is equal to the corresponding fiber \( {F}_{b}\left( \xi \right) \) , and is to be given the same vector space structure.

As an example if \( M \) is a smooth manifold and \( U \) is an open subset of \( M \) , then the tangent bundle \( {\tau }_{U} \) is equal to \( {\left. {\tau }_{M}\right| }_{U} \) .

More generally one has the following construction.

(b) Induced bundles.

Let \( \xi \) be as above and let \( {B}_{1} \) be an arbitrary topological space. Given any map \( f : {B}_{1} \rightarrow  B \) one can construct the induced bundle \( {f}^{ * }\xi \) over \( {B}_{1} \) . The total space \( {E}_{1} \) of \( {f}^{ * }\xi \) is the subset \( {E}_{1} \subset  {B}_{1} \times  E \) consisting of all pairs \( \left( {b, e}\right) \) with

\[
f\left( b\right)  = \pi \left( e\right) .
\]

The projection map \( {\pi }_{1} : {E}_{1} \rightarrow  {B}_{1} \) is defined by \( {\pi }_{1}\left( {b, e}\right)  = b \) . Thus one has a commutative diagram

![bo_d7du9galb0pc73deir9g_33_797_405_225_184_0.jpg](images/bo_d7du9galb0pc73deir9g_33_797_405_225_184_0.jpg)

where \( \widehat{f}\left( {b, e}\right)  = e \) . The vector space structure in \( {\pi }_{1}^{-1}\left( b\right) \) is defined by

\[
{t}_{1}\left( {b,{e}_{1}}\right)  + {t}_{2}\left( {b,{e}_{2}}\right)  = \left( {b,{t}_{1}{e}_{1} + {t}_{2}{e}_{2}}\right) .
\]

Thus \( \widehat{f} \) carries each vector space \( {F}_{b}\left( {{f}^{ * }\xi }\right) \) isomorphically onto the vector space \( {F}_{f\left( b\right) }\left( \xi \right) \) .

If \( \left( {U, h}\right) \) is a local coordinate system for \( \xi \) , set \( {U}_{1} = {f}^{-1}\left( U\right) \) and define

\[
{h}_{1} : {U}_{1} \times  {\mathbb{R}}^{n} \rightarrow  {\pi }_{1}^{-1}\left( {U}_{1}\right)
\]

by \( {h}_{1}\left( {b, x}\right)  = \left( {b, h\left( {f\left( b\right) , x}\right) }\right) \) . Then \( \left( {{U}_{1},{h}_{1}}\right) \) is clearly a local coordinate system for \( {f}^{ * }\xi \) . This proves that \( {f}^{ * }\xi \) is locally trivial. (If \( \xi \) happens to be trivial, it follows that \( {f}^{ * }\xi \) is trivial.)

Remark 1. If \( \xi \) is a smooth vector bundle and \( f \) a smooth map, then it can be shown that \( {E}_{1} \) is a smooth submanifold of \( {B}_{1} \times  E \) , and hence that \( {f}^{ * }\xi \) is also a smooth vector bundle.

The above commutative diagram suggests the following concept which a priori, is more general. Let \( \xi \) and \( \eta \) be vector bundles.

Definition. A bundle map from \( \eta \) to \( \xi \) is a continuous function

\[
g : E\left( \eta \right)  \rightarrow  E\left( \xi \right)
\]

which carries each vector space \( {F}_{b}\left( \eta \right) \) isomorphically onto one of the vector spaces \( {F}_{{b}^{\prime }}\left( \xi \right) \) .

Setting \( \bar{g}\left( b\right)  = {b}^{\prime } \) , it is clear that the resulting function

\[
\bar{g} : B\left( \eta \right)  \rightarrow  B\left( \xi \right)
\]

is continuous.

Lemma 3.1. If \( g : E\left( \eta \right)  \rightarrow  E\left( \xi \right) \) is a bundle map, and if \( \bar{g} : B\left( \eta \right)  \rightarrow  B\left( \xi \right) \) is the corresponding map of base spaces, then \( \eta \) is isomorphic to the induced bundle \( {\bar{g}}^{ * }\xi \) .

Proof. Define \( h : E\left( \eta \right)  \rightarrow  E\left( {{\bar{g}}^{ * }\xi }\right) \) by

\[
h\left( e\right)  = \left( {\pi \left( e\right) , g\left( e\right) }\right)
\]

where \( \pi \) denotes the projection map of \( \eta \) . Since \( h \) is continuous and maps each fiber \( {F}_{b}\left( \eta \right) \) isomorphically onto the corresponding fiber \( {F}_{b}\left( {{\bar{g}}^{ * }\xi }\right) \) , it follows from Lemma 2.3 that \( h \) is an isomorphism.

## (c) Cartesian products

Given two vector bundles \( {\xi }_{1},{\xi }_{2} \) Projection maps \( {\pi }_{i} : {E}_{i} \rightarrow  {B}_{i}, i = 1,2 \) , the Cartesian product \( {\xi }_{1} \times  {\xi }_{2} \) is defined to be the bundle with projection map

\[
{\pi }_{1} \times  {\pi }_{2} : {E}_{1} \times  {E}_{2} \rightarrow  {B}_{1} \times  {B}_{2}
\]

where each fiber

\[
{\left( {\pi }_{1} \times  {\pi }_{2}\right) }^{-1}\left( {{b}_{1},{b}_{2}}\right)  = {F}_{{b}_{1}}\left( {\xi }_{1}\right)  \times  {F}_{{b}_{2}}\left( {\xi }_{2}\right) ,
\]

is given the obvious vector space structure. Clearly \( {\xi }_{1} \times  {\xi }_{2} \) is locally trivial.

As an example, if \( M = {M}_{1} \times  {M}_{2} \) is a product of smooth manifolds, then the tangent bundle \( {\tau }_{M} \) is isomorphic to \( {\tau }_{{M}_{1}} \times  {\tau }_{{M}_{2}} \) . (Compare 1-A.)

## (d) Whitney sums

Next consider two bundles \( {\xi }_{1},{\xi }_{2} \) over the same base space \( B \) . Let

\[
\Delta  : B \rightarrow  B \times  B
\]

denote the diagonal embedding. The bundle \( {\Delta }^{ * }\left( {{\xi }_{1} \times  {\xi }_{2}}\right) \) over \( B \) is called the Whitney sum of \( {\xi }_{1} \) and \( {\xi }_{2} \) ; and will denoted by \( {\xi }_{1} \oplus  {\xi }_{2} \) . Note that each fiber \( {F}_{b}\left( {{\xi }_{1} \oplus  {\xi }_{2}}\right) \) is canonically isomorphic to the direct sum \( {F}_{b}\left( {\xi }_{1}\right)  \oplus  {F}_{b}\left( {\xi }_{2}\right) \) .

Definition. Consider two vector bundles \( \xi \) and \( \eta \) over the same base space \( B \) with \( E\left( \xi \right)  \subset  E\left( \eta \right) \) ; then \( \xi \) is a sub-bundle of \( \eta \) (written \( \xi  \subset  \eta \) ) if each fiber \( {F}_{b}\left( \xi \right) \) is a sub-vector-space of the corresponding fiber \( {F}_{b}\left( \eta \right) \) .

Lemma 3.2. Let \( {\xi }_{1} \) and \( {\xi }_{2} \) be sub-bundles of \( \eta \) such that each vector space \( {F}_{b}\left( \eta \right) \) is equal to the direct sum of the sub-spaces \( {F}_{b}\left( {\xi }_{1}\right) \) and \( {F}_{b}\left( {\xi }_{2}\right) \) . Then \( \eta \) is isomorphic to the Whitney sum \( {\xi }_{1} \oplus  {\xi }_{2} \) .

Proof. Define \( f : E\left( {{\xi }_{1} \oplus  {\xi }_{2}}\right)  \rightarrow  E\left( \eta \right) \) by \( f\left( {b,{e}_{1},{e}_{2}}\right)  = {e}_{1} + {e}_{2} \) . It follows from Lemma 2.3 that \( f \) is an isomorphism.

## (e) Orthogonal complements

This suggests the following question. Given a sub-bundle \( \xi  \subset  \eta \) does there exist a complementary sub-bundle so that \( \eta \) splits as a Whitney sum? If \( \eta \) is provided with a Euclidean metric then such a complementary summand can be constructed as follows. \( {}^{1} \)

Let \( {F}_{b}\left( {\xi }^{ \bot  }\right) \) denote the subspace of \( {F}_{b}\left( \eta \right) \) consisting of all vectors \( v \) such that \( v \cdot  w = 0 \) for all \( w \in  {F}_{b}\left( \xi \right) \) . Let \( E\left( {\xi }^{ \bot  }\right)  \subset  E\left( \eta \right) \) denote the union of the \( {F}_{b}\left( {\xi }^{ \bot  }\right) \) .

Definition. \( {\xi }^{ \bot  } \) will be called the orthogonal complement of \( \xi \) in \( \eta \) .

Theorem 3.3. \( E\left( {\xi }^{ \bot  }\right) \) is the total space of a sub-bundle \( {\xi }^{ \bot  } \subset  \eta \) . Furthermore \( \eta \) is isomorphic to the Whitney sum \( \xi  \oplus  {\xi }^{ \bot  } \) .

Proof. Clearly each vector space \( {F}_{b}\left( \eta \right) \) is the direct sum of the sub-spaces \( {F}_{b}\left( \xi \right) \) and \( {F}_{b}\left( {\xi }^{ \bot  }\right) \) . Thus the only problem is to prove that \( {\xi }^{ \bot  } \) satisfies the local triviality condition.

Given any point \( {b}_{0} \in  B \) , let \( U \) be a neighborhood of \( {b}_{0} \) which is sufficiently small that both \( {\left. \xi \right| }_{U} \) and \( {\left. \eta \right| }_{U} \) are trivial. Let \( {s}_{1},\ldots ,{s}_{m} \) be normal orthogonal cross-sections of \( {\left. \xi \right| }_{U} \) and let \( {s}_{1}^{\prime },\ldots ,{s}_{n}^{\prime } \) be normal orthogonal cross-sections of

---

\( {}^{1} \) If the base space \( B \) is paracompact, then \( \eta \) can always be given a Euclidean metric (2- C); hence a sub-bundle \( \xi  \subset  \eta \) is always a Whitney summand. If \( B \) is not required to be paracompact, then counterexamples can be given.

---

\( {\left. \eta \right| }_{U} \) ; where \( m \) and \( n \) are the respective fiber dimensions. (Compare lemma 2.4.) Thus the \( m \times  n \) matrix

\[
\left\lbrack  {{s}_{i}\left( {b}_{0}\right)  \cdot  {s}_{j}^{\prime }\left( {b}_{0}\right) }\right\rbrack
\]

has rank \( m \) . Renumbering the \( {s}_{j}^{\prime } \) if necessary, we may assume that the first \( m \) columns are linearly independent.

Let \( V \subset  U \) be the open set consisting of all points \( b \) for which the first \( m \) columns of the matrix \( \left\lbrack  {{s}_{i}\left( b\right)  \cdot  {s}_{j}^{\prime }\left( b\right) }\right\rbrack \) are linearly independent. Then the \( n \) cross-sections

\[
{s}_{1},{s}_{2},\ldots ,{s}_{m},{s}_{m + 1}^{\prime },\ldots ,{s}_{n}^{\prime }
\]

of \( {\left. \eta \right| }_{U} \) are not linearly dependent at any point of \( V \) . (For a linear relation would imply that some non-zero linear combination of \( {s}_{1}\left( b\right) ,\ldots ,{s}_{m}\left( b\right) \) was also a linear combination of \( {s}_{m + 1}^{\prime }\left( b\right) ,\ldots ,{s}_{n}^{\prime }\left( b\right) \) , hence orthogonal to \( {s}_{1}^{\prime }\left( b\right) ,\ldots ,{s}_{m}^{\prime }\left( b\right) \) .) Applying the Gram-Schmidt process to this sequence of cross-sections, we obtain normal orthogonal cross-sections \( {s}_{1},\ldots {s}_{m},{s}_{m + 1},\ldots ,{s}_{n} \) of \( {\left. \eta \right| }_{V} \) .

Now a local coordinate system

\[
h : V \times  {\mathbb{R}}^{n - m} \rightarrow  E\left( {\xi }^{ \bot  }\right) ,
\]

for \( {\xi }^{ \bot  } \) is given by the formula

\[
h\left( {b, x}\right)  = {x}_{1}{s}_{m + 1}\left( b\right)  + \cdots  + {x}_{n - m}{s}_{n}\left( b\right) .
\]

The identity

\[
{h}^{-1}\left( e\right)  = \left( {{\pi e},\left( {e \cdot  {s}_{m + 1}\left( {\pi e}\right) ,\ldots , e \cdot  {s}_{n}\left( {\pi e}\right) }\right) }\right) ,
\]

shows that \( h \) is a homeomorphism, and completes the proof of Theorem 3.3.

As an example, suppose that \( M \subset  N \subset  {\mathbb{R}}^{A} \) are smooth manifolds, and suppose that \( N \) is provided with a Riemannian metric. Then the tangent bundle \( {\tau }_{M} \) is a sub-bundle of the restriction \( {\left. {\tau }_{N}\right| }_{M} \) . In this case the orthogonal complement \( {\left. {\tau }_{M}^{ \bot  } \subset  {\tau }_{N}\right| }_{M} \) is called the normal bundle \( \nu \) of \( M \) in \( N \) . Thus we have:

Corollary 3.4. For any smooth submanifold \( M \) of a smooth Riemannian manifold \( N \) the normal bundle \( \nu \) is defined, and

\[
{\tau }_{M} \oplus  \nu  \cong  {\left. {\tau }_{N}\right| }_{M}
\]

More generally a smooth map \( f : M \rightarrow  N \) between smooth manifolds is called an immersion if the Jacobian

\[
\mathrm{d}{f}_{x} : {\mathbf{T}}_{x}M \rightarrow  {\mathbf{T}}_{f\left( x\right) }N
\]

maps the tangent space \( {\mathbf{T}}_{x}M \) injectively (i.e. with kernel zero) for each \( x \in  M \) . [It follows from the implicit function theorem that an immersion is locally an embedding of \( M \) in \( N \) , but in the large there may be self-intersections. A typical immersion of the circle in the plane is illustrated in 4.]

![bo_d7du9galb0pc73deir9g_37_513_935_703_378_0.jpg](images/bo_d7du9galb0pc73deir9g_37_513_935_703_378_0.jpg)

Figure 4

Suppose that \( N \) is a Riemannian manifold. Then for each \( x \in  M \) , the tangent space \( {\mathbf{T}}_{f\left( x\right) }N \) splits as the direct sum of the image \( \mathrm{d}{f}_{x}\left( {{\mathbf{T}}_{x}M}\right) \) and its orthogonal complement. Correspondingly the induced bundle \( {f}^{ * }{\tau }_{N} \) over \( M \) splits as the Whitney sum of a sub-bundle isomorphic to \( {\tau }_{M} \) and a complementary sub-bundle \( {\nu }_{f} \) . Thus:

Corollary 3.5. For any immersion \( f : M \rightarrow  N \) , with \( N \) Riemannian, there is a Whitney sum decomposition

\[
{f}^{ * }{\tau }_{N} \cong  {\tau }_{M} \oplus  {\nu }_{f}
\]

This bundle \( {\nu }_{f} \) will be called the normal bundle of the immersion \( f \) .

## (f) Continuous functors of vector spaces and vector bundles

The direct sum operation is perhaps the most important method for building new vector spaces out of old, but many other such constructions play an important role in differential geometry. For example, to any pair \( V, W \) of real vector spaces one can assign:

1) the vector space \( \operatorname{Hom}\left( {V, W}\right) \) of linear transformations from \( V \) to \( W \) ;

2) the tensor product \( {}^{2}V \otimes  W \) ;

3) the vector space of all symmetric bilinear transformations from \( V \times  V \) to \( W \)

and so on. To a single vector space \( V \) one can assign:

4) the dual vector space \( \operatorname{Hom}\left( {V,\mathbb{R}}\right) \) ;

5) the \( k \) -th exterior power \( {}^{3}{\Lambda }^{k}V \) ;

6) the vector space of all 4-linear transformations \( V \times  V \times  V \times  V \rightarrow  \mathbb{R} \) satisfying the symmetry relations:

\[
K\left( {{v}_{1},{v}_{2},{v}_{3},{v}_{4}}\right)  = K\left( {{v}_{3},{v}_{4},{v}_{1},{v}_{2}}\right)  =  - K\left( {{v}_{1},{v}_{2},{v}_{4},{v}_{3}}\right)
\]

and

\[
K\left( {{v}_{1},{v}_{2},{v}_{3},{v}_{4}}\right)  + K\left( {{v}_{1},{v}_{4},{v}_{2},{v}_{3}}\right)  + K\left( {{v}_{1},{v}_{3},{v}_{4},{v}_{2}}\right)  = 0.
\]

(This last example would be rather far-fetched, were it not important in the theory of Riemannian curvature.)

These examples suggest that we consider a general functor of several vector space variables.

---

\( {}^{2} \) See for example [Lan65, pp. 408].

\( {}^{3} \) See for example [Lan65, pp. 424].

---

Definition. Let \( {\mathbf{{Vect}}}_{\mathbb{R}} \) denote the category consisting of all finite dimensional real vector spaces and all isomorphisms between such vector spaces. By a (covariant) \( {}^{4} \) functor \( T : {\operatorname{Vect}}_{\mathbb{R}} \times  {\operatorname{Vect}}_{\mathbb{R}} \rightarrow  {\operatorname{Vect}}_{\mathbb{R}} \) is meant an operation which assigns

1. to each pair \( V, W \in  {\mathbf{{Vect}}}_{\mathbb{R}} \) of vector spaces a vector space \( T\left( {V, W}\right)  \in \; {\operatorname{Vect}}_{\mathbb{R}} \)

and

2. to each pair \( f : V \rightarrow  {V}^{\prime }, g : W \rightarrow  {W}^{\prime } \) of isomorphisms an isomorphism

\[
T\left( {f, g}\right)  : T\left( {V, W}\right)  \rightarrow  T\left( {{V}^{\prime },{W}^{\prime }}\right) ;
\]

so that

3. \( T\left( {{\mathrm{{id}}}_{V},{\mathrm{{id}}}_{W}}\right)  = {\mathrm{{id}}}_{T\left( {V, W}\right) } \) and

4. \( T\left( {{f}_{1} \circ  {f}_{2},{g}_{1} \circ  {g}_{2}}\right)  = T\left( {{f}_{1},{g}_{1}}\right)  \circ  T\left( {{f}_{2},{g}_{2}}\right) \) .

Such a functor will be called continuous if \( T\left( {f, g}\right) \) depends continuously on \( f \) and \( g \) . This makes sense, since the set of all isomorphisms from one finite dimensional vector space to another has a natural topology.

The concept of a continuous functor \( T : {\mathbf{{Vect}}}_{\mathbb{R}} \times  \cdots  \times  {\mathbf{{Vect}}}_{\mathbb{R}} \rightarrow  {\mathbf{{Vect}}}_{\mathbb{R}} \) in \( k \) variables is defined similarly. Note that examples1,2,3above are continuous functors of two variables, and that examples 4, 5, 6 are continuous functors of one variable.

Let \( T : {\mathbf{{Vect}}}_{\mathbb{R}} \times  \cdots  \times  {\mathbf{{Vect}}}_{\mathbb{R}} \rightarrow  {\mathbf{{Vect}}}_{\mathbb{R}} \) be such a continuous functor of \( k \) variables, and let \( {\xi }_{1},\ldots ,{\xi }_{k} \) be vector bundles over a common base space \( B \) . Then a new vector bundle over \( B \) is constructed as follows. For each \( b \in  B \) let

\[
{F}_{b} = T\left( {{F}_{b}\left( {\xi }_{1}\right) ,\ldots ,{F}_{b}\left( {\xi }_{k}\right) }\right) .
\]

Let \( E \) denote the disjoint union of the vector spaces \( {F}_{b} \) and define \( \pi  : E \rightarrow  B \) by \( \pi \left( {F}_{b}\right)  = b \) .

---

\( {}^{4} \) The distinction between covariant and contravariant functors is not important here, since we are working only with isomorphisms.

---

Theorem 3.6. There exists a canonical topology for \( E \) so that \( E \) is the total space of a vector bundle with projection \( \pi \) and with fibers \( {F}_{b} \) .

Definition. This bundle will be denoted by \( T\left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) .

For example starting with the tensor product functor, this construction defines the tensor product \( \xi  \otimes  \eta \) of two vector bundles. Starting with the direct sum functor one obtains the Whitney sum \( \xi  \oplus  \eta \) of two bundles. Starting with the duality functor

\[
V \mapsto  \operatorname{Hom}\left( {V,\mathbb{R}}\right) ,
\]

one obtains the functor

\[
\xi  \mapsto  \operatorname{Hom}\left( {\xi ,{\varepsilon }^{1}}\right) ,
\]

which assigns to each vector bundle its dual vector bundle.

The proof of Theorem 3.6 will be indicated only briefly. Let \( \left( {U,{h}_{1}}\right) ,\ldots ,\left( {U,{h}_{k}}\right) \) be local coordinate systems for \( \left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) respectively, all using the same open set \( U \) . For each \( b \in  U \) define

\[
{h}_{ib} : {\mathbb{R}}^{{n}_{i}} \rightarrow  {F}_{b}\left( {\xi }_{i}\right) ,
\]

by \( {h}_{ib}\left( x\right)  = {h}_{i}\left( {b, x}\right) \) . Then the isomorphism

\[
T\left( {{h}_{1b},\ldots ,{h}_{kb}}\right)  : T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right)  \rightarrow  {F}_{b}
\]

is defined. The correspondence

\[
\left( {b, x}\right)  \rightarrow  T\left( {{h}_{1b},\ldots ,{h}_{kb}}\right) \left( x\right)
\]

defines a one-to-one function

\[
h : U \times  T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right)  \rightarrow  {\pi }^{-1}\left( U\right) .
\]

Assertion. There is a unique topology on \( E \) so that each such \( h \) is a homeomorphism, and so that each \( {\pi }^{-1}\left( U\right) \) is an open subset of \( E \) .

Proof. The uniqueness is clear. To prove existence, it is only necessary to observe that if two such "coordinate systems" \( \left( {U, h}\right) \) and \( \left( {{U}^{\prime },{h}^{\prime }}\right) \) overlap, then the transformation

\[
\left( {U \cap  {U}^{\prime }}\right)  \times  T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right) \xrightarrow[]{{h}^{-1}{h}^{\prime }}\left( {U \cap  {U}^{\prime }}\right)  \times  T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right)
\]

is continuous. This follows from the continuity of \( T \) .

It is now clear that \( \pi  : E \rightarrow  B \) is continuous, and that the resulting vector bundle \( T\left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) satisfies the local triviality condition.

Remark 1. This construction can be translated into Steenrod's terminology as follows. Let \( {\mathrm{{GL}}}_{n} = {\mathrm{{GL}}}_{n}\left( \mathbb{R}\right) \) denote the group of automorphisms of the vector space \( {\mathbb{R}}^{n} \) . Then \( T \) determines a continuous homomorphism from the product group \( {\mathrm{{GL}}}_{{n}_{1}} \times  \cdots  \times  {\mathrm{{GL}}}_{{n}_{k}} \) , to the group \( {\mathrm{{GL}}}^{\prime } \) of automorphisms of the vector space \( T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right) \) . Hence given bundles \( \left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) over \( B \) with structural groups \( {\mathrm{{GL}}}_{{n}_{1}} \times  \cdots  \times  {\mathrm{{GL}}}_{{n}_{k}} \) respectively, there corresponds a bundle \( T\left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) with structural group \( {\mathrm{{GL}}}^{\prime } \) and with fiber \( T\left( {{\mathbb{R}}^{{n}_{1}},\ldots ,{\mathbb{R}}^{{n}_{k}}}\right) \) . For further discussion, see [Hir66, §3.6].

Remark 2. Given bundles \( \left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) over distinct base spaces, a similar construction gives rise to a vector bundle \( \widehat{T}\left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) over \( B\left( {\xi }_{1}\right)  \times  \cdots  \times  B\left( {\xi }_{k}\right) \) , with typical fiber \( T\left( {{F}_{{b}_{1}}\left( {\xi }_{1}\right)  \times  \cdots  \times  {F}_{{b}_{1}}\left( {\xi }_{k}\right) }\right) \) . This yields a functor \( \widehat{T} \) from the category of vector bundles and bundle maps into itself. As an example, starting from the direct sum functor \( \oplus \) on the category \( {\operatorname{Vect}}_{\mathbb{R}} \) one obtains the Cartesian product functor

\[
\xi ,\eta  \mapsto  \xi \widehat{ \oplus  }\eta  = \xi  \times  \eta
\]

for vector bundles.

Remark 3. If \( \left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) are smooth vector bundles, then \( T\left( {{\xi }_{1},\ldots ,{\xi }_{k}}\right) \) can also be given the structure of a smooth vector bundle. The proof is similar to that of Theorem 3.6. It is necessary to make use of the fact that the isomorphism \( T\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) is a smooth function of the isomorphisms \( T\left( {{f}_{1},\ldots ,{f}_{k}}\right) \) . This follows from [Che99, p. 128].

As an illustration, let \( M\overset{f}{ \rightarrow  }N \) be a smooth map. Then \( \operatorname{Hom}\left( {{\tau }_{M},{f}^{ * }{\tau }_{N}}\right) \) is a smooth vector bundle over \( M \) . Note that \( \mathrm{d}f \) gives rise to a smooth cross-section of this vector bundle.

As a second illustration, if \( M \subset  N \) with normal bundle \( \nu \) , where \( N \) is a smooth Riemannian manifold, then the second fundamental form can be defined as a smooth symmetric cross-section of the bundle \( \operatorname{Hom}\left( {{\tau }_{M} \otimes  {\tau }_{N},\nu }\right) \) . (Compare [BC11], as well as 5-B.)

Here are six problems for the reader.

Problem 3-A. A smooth map \( f : M \rightarrow  N \) between smooth manifolds is called a submersion if each Jacobian

\[
\mathrm{d}{f}_{x} : {\mathbf{T}}_{x}M \rightarrow  {\mathbf{T}}_{f\left( x\right) }N
\]

is surjective (i.e. is onto). Construct a vector bundle \( {\kappa }_{f} \) built up out of the kernels of the \( \mathrm{d}{f}_{x} \) . If \( M \) is Riemannian, show that

\[
{\tau }_{M} \cong  {\kappa }_{f} \oplus  {f}^{ * }{\tau }_{N}
\]

Problem 3-B. Given vector bundles \( \xi  \subset  \eta \) define the quotient bundle \( \eta /\xi \) and prove that it is locally trivial. If \( \eta \) has a Euclidean metric, show that

\[
{\xi }^{ \bot  } \cong  \eta /\xi
\]

Problem 3-C. More generally let \( \xi ,\eta \) be arbitrary vector bundles over \( B \) and let \( f \) be a cross-section of the bundle \( \operatorname{Hom}\left( {\xi ,\eta }\right) \) . If the rank of the linear function

\[
f\left( b\right)  : {F}_{b}\left( \xi \right)  \rightarrow  {F}_{b}\left( \eta \right)
\]

is locally constant as a function of \( b \) , define the kernel \( {\kappa }_{f} \subset  \xi \) and the cokernel \( {\nu }_{f} \) , and prove that they are locally trivial.

Problem 3-D. If a vector bundle \( \xi \) possesses a Euclidean metric, show that \( \xi \) is isomorphic to its dual bundle \( \operatorname{Hom}\left( {\xi ,{\varepsilon }^{1}}\right) \) .

Problem 3-E. Show that the set of isomorphism classes of 1-dimensional vector bundles over \( B \) forms an abelian group with respect to the tensor product operation. Show that a given \( {\mathbb{R}}^{1} \) -bundle \( \xi \) possesses a Euclidean metric if and only if \( \xi \) represents an element of order \( \leq  2 \) in this group.

Problem 3-F. (Compare [Swa62].) Let \( B \) be a Tychonoff space \( {}^{5} \) and let \( \mathbb{R}\left( B\right) \) denote the ring of continuous real valued functions on \( B \) . For any vector bundle \( \xi \) over \( B \) , let \( S\left( \xi \right) \) denote the \( \mathbb{R}\left( B\right) \) -module consisting of all cross-sections of \( \xi \) .

1. Show that \( S\left( {\xi  \oplus  \eta }\right)  \cong  S\left( \xi \right)  \oplus  S\left( \eta \right) \) . Show that \( \xi \) is trivial if and only if \( S\left( \xi \right) \) is free.

2. If \( \xi  \oplus  \eta \) is trivial, show that \( S\left( \xi \right) \) is a finitely generated projective module. \( {}^{6} \) Conversely if \( Q \) is a finitely generated projective module over \( \mathbb{R}\left( B\right) \) , show that \( Q \cong  S\left( \xi \right) \) for some \( \xi \) .

3. Show that \( \xi  \cong  \eta \) if and only if \( S\left( \xi \right)  \cong  S\left( \eta \right) \) .

---

\( {}^{5} \) A topological space is Tychonoff if it is Hausdorff, and if for every point \( x \) and disjoint closed subset \( A \) there exists a continuous real valued function separating \( x \) from \( A \) . (Compare [Kel55].)

\( {}^{6} \) A module is projective if it is a direct summand of a free module. See for example [LB99, p. 368].

---
