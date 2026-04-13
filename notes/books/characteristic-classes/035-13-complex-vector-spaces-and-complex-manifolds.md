# 13 Complex Vector Spaces and Complex Manifolds

It is often useful to consider vector bundles in which each fiber is a vector space over the complex numbers. Let \( B \) be a topological space.

Definition. A complex vector bundle \( \omega \) of complex dimension \( n \) over \( B \) (or briefly a complex \( n \) -plane bundle) consists of a topological space \( E \) and projection map \( \pi  : E \rightarrow  B \) , together with the structure of a complex vector space in each fibre \( {\pi }^{-1}\left( b\right) \) , subject to the following:

Condition 13.1 (local triviality). Each point of \( B \) must possess a neighborhood \( U \) so that the inverse image \( {\pi }^{-1}\left( U\right) \) is homeomorphic to \( U \times  {\mathbb{C}}^{n} \) under a homeomorphism which maps each fiber \( {\pi }^{-1}\left( b\right) \) complex linearly onto \( b \times  {\mathbb{C}}^{n} \) .

Here \( {\mathbb{C}}^{n} \) stands for the coordinate space of \( n \) -tuples of complex numbers, and \( b \times  {\mathbb{C}}^{n} \) is made into a complex vector space by ignoring the \( b \) coordinate.

Just as in §3, we can form new complex vector bundles out of old ones by forming Whitney sums or tensor products (over the complex numbers \( \mathbb{C} \) ) or by forming induced vector bundles.

One method of constructing a complex \( n \) -plane bundle is to start with a real \( {2n} \) -plane bundle, attempting to give each fiber the additional structure of a complex vector space.

Definition. A complex structure on a real \( {2n} \) -plane bundle \( \xi \) is a continuous mapping

\[
\mathbf{J} : E\left( \xi \right)  \rightarrow  E\left( \xi \right)
\]

From the total space to itself which maps each fiber \( \mathbb{R} \) -linearly into itself, and which satisfies the identity \( \mathbf{J}\left( {\mathbf{J}\left( v\right) }\right)  =  - v \) for every vector \( v \) in \( E\left( \xi \right) \) .

Given such a complex structure, we can make each fiber \( {F}_{b}\left( \xi \right) \) into a complex vector space by setting

\[
\left( {x + {iy}}\right) v = {xv} + \mathbf{J}\left( {yv}\right)
\]

for every ocmplex number \( x + {iy} \) . The local triviality condition 13.1 is easily verified, so that \( \xi \) becomes a complex vector bundle.

Conversely of course, given any complex \( n \) -plane bundle \( \omega \) we can simply forget about the complex structure and think of each fibre as a real vector space of dimension \( {2n} \) . Thus we obtain the underlying real \( {2n} \) -plane bundle \( {\omega }_{\mathbb{R}} \) .Note that this real bundle \( {\omega }_{\mathbb{R}} \) and the original complex bundle \( \omega \) both have the same total space, base space and the same projection map.

Perhaps the most important example of a complex vector bundle is provided by the tangent bundle of a "complex manifold". We will look at a special case first.

Example 13.2. Let \( U \) be the open subset of coordinate space \( {\mathbb{C}}^{n} \) . Then the tangent bundle \( {\tau }_{U} \) , with total space \( \mathbf{T}U = U \times  {\mathbb{C}}^{n} \) , has a cannonical complex structure \( {\mathbf{J}}_{0} \) defined by

\[
{\mathbf{J}}_{0}\left( {u, v}\right)  = \left( {u,{iv}}\right)
\]

for every \( u \in  U \) and \( v \in  {\mathbb{C}}^{n} \) .

Now consider a smooth mapping \( f : U \rightarrow  {U}^{\prime } \) , where \( {U}^{\prime } \subset  {\mathbb{C}}^{p} \) is also an open subset of complex coordinate space. We can ask whether the \( \mathbb{R} \) -linear mapping \( \mathrm{d}{f}_{u} : {\mathbf{T}}_{u}U \rightarrow  {\mathbf{T}}_{f\left( u\right) }{U}^{\prime } \) is actually complex linear for all \( u \) , so that

\[
\mathrm{d}f \circ  {\mathbf{J}}_{0} = {\mathbf{J}}_{0} \circ  \mathrm{d}f
\]

If the derivative is complex linear, one says that f satisfies the Cauchy-Riemann equations, or that \( f \) is holomorphic or complex analytic. A standard theorem asserts that \( f \) can then be expressed locally as the sum of a convergent complex power series.(Compare [Hor73] and [GR09].)

Let \( M \) be a smooth manifold of dimension \( {2n} \) . A complex structure on the tangent bundle of \( M \) is sometimes called an "almost complex structure" on \( M \) .

Definition 13.3. A complex structure on the manifold \( M \) is a complex structure \( \mathbf{J} \) on the tangent bundle \( {\tau }_{M} \) which satisfies the following extremely stringent condition: Every point of \( M \) must possess an open neighborhood which is diffeomorphic to an open subset of \( {\mathbb{C}}^{n} \) under a diffeomorphism \( h \) whose derivative is everywhere complex linear: \( \mathrm{d}h \circ  \mathbf{J} = {\mathbf{J}}_{0} \circ  \mathrm{d}h \) .

The pair \( \left( {M,\mathbf{J}}\right) \) is then called a complex manifold of complex dimension \( n \) . In practice, by abuse of notation, we will usually use the single symbol \( M \) for a complex manifold.

Definition. A smooth mapping \( f : M \rightarrow  N \) between complex manifolds is holomorphic if \( \mathrm{d}f \) is complex linear, \( \mathrm{d}f \circ  \mathbf{J} = \mathbf{J} \circ  \mathrm{d}f \) .

Remark 8. A fundamental theorem of [NN57] asserts that a smooth almost complex structure \( \mathbf{J} \) is actually a complex structure if and only if it satisfies a certain system of quadratic first order partial differential equations. In terms of the bracket product of vector fields, these equations can be written as

\[
\left\lbrack  {\mathbf{J}v,\mathbf{J}w}\right\rbrack   = \mathbf{J}\left\lbrack  {v,\mathbf{J}w}\right\rbrack   + \mathbf{J}\left\lbrack  {\mathbf{J}v, w}\right\rbrack   + \left\lbrack  {v, w}\right\rbrack
\]

where \( v \) and \( w \) are arbitrary smooth vector fields on \( M \) .

The most classical (and often the most convenient) procedure for assigning a complex structure to a smooth manifold is the following. One gives a collection of diffeomorphisms \( {h}_{\alpha } : {U}_{\alpha } \rightarrow  {V}_{\alpha } \) where the \( {U}_{\alpha } \) are open subsets of \( {\mathbb{C}}^{n} \) and the \( {V}_{\alpha } \) are open sets covering the manifold. It is only necessary to verify that each composition

\[
{h}_{\beta }^{-1} \circ  {h}_{\alpha } : {h}_{\alpha }^{-1}\left( {{V}_{\alpha } \cap  {V}_{\beta }}\right)  \rightarrow  {h}_{\beta }^{-1}\left( {{V}_{\alpha } \cap  {B}_{\beta }}\right)
\]

is holomorphic.

In conclusion here are some exercises for the reader.

Problem 13-A. Show that a complex structure \( \mathbf{J} : E\left( \xi \right)  \rightarrow  E\left( \xi \right) \) on a real vector bundle automatically satisfies the complex local triviality condition 13.1.

Problem 13-B. If \( M \) is a complex manifold, show that \( \mathbf{T}M \) is a complex manifold. Similarly, if \( f : M \rightarrow  N \) is holomorphic, show that \( \mathrm{d}f : \mathbf{T}M \rightarrow  \mathbf{T}N \) is holomorphic.

Problem 13-C. If \( M \) is a compact complex manifold, show that every holomorphic map \( f : M \rightarrow  \mathbb{C} \) is constant.

Problem 13-D. Show that the projective space \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) , consisting of all complex lines through the origin in \( {\mathbb{C}}^{n + 1} \) , can be given the structure of a complex manifold. (Note that \( {\mathbb{P}}^{1}\left( \mathbb{C}\right) \) can be identified with the complex line \( \mathbb{C} \) thogether with a single point at infinity.) More generally show the space \( {\operatorname{Gr}}_{k}\left( {\mathbb{C}}^{n}\right) \) of complex \( k \) planes through the origin in \( {\mathbb{C}}^{n} \) is a complex manifold of complex dimension \( k\left( {n - k}\right) \) .

Problem 13-E. Let \( {\gamma }_{n}^{1} \) denote the canonical complex line bundle over \( {\mathbb{P}}^{n}\left( {\mathbb{C}}^{n}\right) \) . Thus the total space \( E\left( {\gamma }_{n}^{1}\right) \) consists of all pairs \( \left( {L, v}\right) \) where \( L \) is a complex line through the origin in \( \mathbb{C} \) and \( v \in  L \) . Show that \( {\gamma }_{n}^{1} \) does not possess any holomorphic cross-section, other than the zero cross-section. Show, however, that the dual bundle \( {\operatorname{Hom}}_{\mathbb{C}}\left( {{\gamma }_{n}^{1},\mathbb{C}}\right) \) posses atleast \( n + 1 \) holomorphic cross-sections which are linearly independent over \( \mathbb{C} \) .

Problem 13-F. If \( M \) is a complex \( n \) -manifold, then the real bundle \( {\operatorname{Hom}}_{\mathbb{R}}\left( {{\tau }_{M},\mathbb{R}}\right) \) of tangent covetors does not possess any natural complex structure. Show however, that its "complexification"

\[
{\operatorname{Hom}}_{\mathbb{R}}\left( {{\tau }_{M},\mathbb{R}}\right) { \otimes  }_{\mathbb{R}}\mathbb{C} \cong  {\operatorname{Hom}}_{\mathbb{R}}\left( {{\tau }_{M},\mathbb{C}}\right)
\]

is a complex \( {2n} \) -plane bundle which splits canonically as a Whitney sum

\[
{\operatorname{Hom}}_{\mathbb{C}}\left( {{\tau }_{M},\mathbb{C}}\right)  \oplus  {\overline{\operatorname{Hom}}}_{\mathbb{C}}\left( {{\tau }_{M},\mathbb{C}}\right)
\]

Here \( {\overline{\operatorname{Hom}}}_{\mathbb{C}}\left( {{\mathbf{T}}_{x}M,\mathbb{C}}\right) \) denote the complex vectort space of conjugate linear mappings, \( h\left( {\lambda v}\right)  = \overline{\lambda }h\left( v\right) \) . If \( U \subset  {\mathbb{C}}^{n} \) is an open set with coordinate functions \( {z}_{1},\ldots ,{z}_{n} : U \rightarrow  \mathbb{C} \) , show that the local differentials \( \mathrm{d}{z}_{1}\left( u\right) ,\ldots \mathrm{d}{z}_{n}\left( u\right) \) form a basis for \( {\operatorname{Hom}}_{\mathbb{C}}\left( {{\mathbf{T}}_{u}U,\mathbb{C}}\right) \) , and that \( \mathrm{d}{\bar{z}}_{1}\left( u\right) ,\ldots ,\mathrm{d}{\bar{z}}_{n}\left( u\right) \) form a basis for \( {\overline{\operatorname{Hom}}}_{\mathbb{C}}\left( {{\mathbf{T}}_{u}U,\mathbb{C}}\right) \) .

If \( f \) is a smooth (but not necessarily holomorphic) complex valued funci-ton on \( U \) , it follows that \( \mathrm{d}f \) can be written uniquely as a linear combination of \( \mathrm{d}{z}_{1}\left( u\right) ,\ldots \mathrm{d}{z}_{n}\left( u\right) ,\mathrm{d}{\bar{z}}_{1}\left( u\right) ,\ldots ,\mathrm{d}{\bar{z}}_{n}\left( u\right) \) , with coefficients which are also smooth complex valued functions on \( U \) . These coefficients are customarily denoted by

\[
\frac{\partial f}{\partial {z}_{1}},\ldots ,\frac{\partial f}{\partial {z}_{n}},\frac{\partial f}{\partial {\bar{z}}_{1}},\ldots ,\frac{\partial f}{\partial {\bar{z}}_{n}}
\]

respectively. Thus the total differential \( \mathrm{d}f \) can be expressed uniquely as a sum \( \partial f + \overline{\partial }f \) where

\[
\partial f = \sum \frac{\partial f}{\partial {z}_{j}}\mathrm{\;d}{z}_{j}\;\text{ and }\;\overline{\partial }f = \sum \frac{\partial f}{\partial {\bar{z}}_{j}}\mathrm{\;d}{\bar{z}}_{j}.
\]

The former is a section of \( {\operatorname{Hom}}_{\mathbb{C}}\left( {{\tau }_{M},\mathbb{C}}\right) \) and the latter is a section of \( {\overline{\operatorname{Hom}}}_{\mathbb{C}}\left( {{\tau }_{M},\mathbb{C}}\right) \) .

Setting \( {z}_{j} = {x}_{j} + i{y}_{j} \) , show that

\[
\frac{\partial f}{\partial {z}_{j}} = \frac{1}{2}\left( {\frac{\partial f}{\partial {x}_{j}} + \frac{\partial f}{\partial {y}_{j}}}\right) .
\]

Show the Cauchy-Riemann equations for \( f \) can be written as \( \frac{\partial f}{\partial {\bar{z}}_{j}} = 0 \) , or briefly \( \overline{\partial }f = 0. \)

Problem 13-G. Show that the complex vector space spanned by the differential operators \( \partial /\partial {z}_{1},\ldots ,\partial /\partial {z}_{n} \) at \( z \) is canonically isomorphic to the tangent space \( {\mathbf{T}}_{z}U \) .

CHAPTER 13: COMPLEX VECTOR SPACES AND COMPLEX MANIFOLDS
