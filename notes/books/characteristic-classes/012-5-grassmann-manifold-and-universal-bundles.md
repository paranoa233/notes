# 5 Grassmann Manifold and Universal Bundles

In classical differential geometry one encounters the "spherical image" of a curve \( {M}^{1} \subset  {\mathbb{R}}^{k + 1} \) . This is the image of \( {M}^{1} \) under the mapping

\[
t : {M}^{1} \rightarrow  {S}^{k}
\]

which carries each point of \( {M}^{1} \) to its unit tangent vector. Similarly Gauss defined the spherical image of a hypersurface \( {M}^{k} \subset  {\mathbb{R}}^{k + 1} \) as the image of \( {M}^{k} \) under the mapping

\[
n : {M}^{k} \rightarrow  {S}^{k}
\]

which carries each point of \( M \) to its unit normal vector. (Compare figure 7,8.) In order to specify the sign of the tangent or normal vector it is necessary to assume that \( {M}^{1} \) or \( {M}^{k} \) has a preferred orientation. (Compare §9.) However without this orientation one can still define a corresponding map from the manifold to the real projective space \( {\mathbb{P}}^{k} \) .

More generally let \( M \) be a smooth manifold of dimension \( n \) in the coordinate space \( {\mathbb{R}}^{n + k} \) . Then to each point \( x \) of \( M \) one can assign the tangent space \( {\mathbf{T}}_{x}M \subset  {\mathbb{R}}^{n + k} \) . We will think of \( {\mathbf{T}}_{x}M \) as determining a point in a new topological space \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) .

Definition. The Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is the set of all \( n \) -dimensional planes through the origin of the coordinate space \( {\mathbb{R}}^{n + k} \) . This is to be topologized as a quotient space, as follows. An \( n \) -frame in \( {\mathbb{R}}^{n + k} \) is an \( n \) -tuple of linearly independent vectors of \( {\mathbb{R}}^{n + k} \) . The collection of all \( n \) -frames in \( {\mathbb{R}}^{n + k} \) forms an open subset of the n-fold Cartesian product \( {\mathbb{R}}^{n + k} \times  \cdots  \times  {\mathbb{R}}^{n + k} \) , called the Stiefel manifold \( {\mathrm{V}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) . (Compare [Ste51,§7.7].) There is a canonical function

\[
q : {\mathrm{V}}_{n}\left( {\mathbb{R}}^{n + k}\right)  \rightarrow  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right)
\]

![bo_d7du9galb0pc73deir9g_63_280_250_1182_533_0.jpg](images/bo_d7du9galb0pc73deir9g_63_280_250_1182_533_0.jpg)

Figure 7

which maps each \( n \) -frame to the \( n \) -plane which it spans. Now give \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) the quotient topology: a subset \( U \subset  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is open if and only if its inverse image \( {q}^{-1}\left( U\right)  \subset  {\mathrm{V}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is open.

Alternatively let \( {\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) \) denote the subset of \( {\mathrm{V}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) consisting of all orthonormal \( n \) -frames, Then \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) can also be considered as an identification space of \( {\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) \) . One sees from the following commutative diagram that both constructions yield the same topology for \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) .

![bo_d7du9galb0pc73deir9g_63_406_1567_920_185_0.jpg](images/bo_d7du9galb0pc73deir9g_63_406_1567_920_185_0.jpg)

Here \( {q}_{0} \) denotes the restriction of \( q \) to \( {\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) \) .

Lemma 5.1. The Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is a compact topological man-

![bo_d7du9galb0pc73deir9g_64_185_267_1179_485_0.jpg](images/bo_d7du9galb0pc73deir9g_64_185_267_1179_485_0.jpg)

Figure 8

ifold \( {}^{1} \) of dimension \( {nk} \) . The correspondence \( X \rightarrow  {X}^{ \bot  } \) , which assigns to each \( n \) - plane its orthogonal \( k \) -plane, defines a homeomorphism between \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) and \( {\operatorname{Gr}}_{k}\left( {\mathbb{R}}^{n + k}\right) \) .

Remark. For the special case \( k = 1 \) note that \( {\operatorname{Gr}}_{1}\left( {\mathbb{R}}^{n + 1}\right) \) is equal to the real projective space \( {\mathbb{P}}^{n} \) . It follows that the manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + 1}\right) \) of \( n \) -planes in \( \left( {n + 1}\right) \) - space is canonically homeomorphic to \( {\mathbb{P}}^{n} \) .

Proof of 5.1. In order to show that \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is a Hausdorff space it is sufficient to show that any two points can be separated by a continuous real valued function. For fixed \( w \in  {\mathbb{R}}^{n + k} \) , let \( {\rho }_{w}\left( X\right) \) denote the square of the Euclidean distance from \( w \) to \( X \) . If \( {x}_{1},\ldots ,{x}_{n} \) is an orthonormal basis for \( X \) , then the identity

\[
{\rho }_{w}\left( X\right)  = w \cdot  w - {\left( w \cdot  {x}_{1}\right) }^{2} - \cdots  - {\left( w \cdot  {x}_{n}\right) }^{2}
\]

shows that the composition

\[
{\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) \overset{{q}_{0}}{ \rightarrow  }{\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \overset{{\rho }_{w}}{ \rightarrow  }\mathbb{R}
\]

is continuous; hence that \( {\rho }_{w} \) is continuous. Now if \( X, Y \) are distinct \( n \) -planes, and \( w \) belongs to \( X \) but not \( Y \) , then \( {\rho }_{w}\left( X\right)  \neq  {\rho }_{w}\left( Y\right) \) . This proves that \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is a Hausdorff space.

---

\( {}^{1} \) A topological manifold of dimension \( d \) is a Hausdorff space in which every point has a neighborhood homeomorphic to \( {\mathbb{R}}^{d} \) .

---

The set \( {\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) \) of orthonormal \( n \) -frames is a closed, bounded subset of \( {\mathbb{R}}^{n + k} \times  \cdots  \times  {\mathbb{R}}^{n + k} \) , and therefore is compact. It follows that

\[
{\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right)  = {q}_{0}\left( {{\mathrm{\;V}}_{n}^{0}\left( {\mathbb{R}}^{n + k}\right) }\right)
\]

is also compact.

Proof. that every point \( {X}_{0} \) of \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) has a neighborhood \( U \) which is homeomorphic to \( {\mathbb{R}}^{nk} \) . It will be convenient to regard \( {\mathbb{R}}^{n + k} \) as the direct sum \( {X}_{0} \oplus  {X}_{0}{}^{ \bot  } \) . Let \( U \) be the open subset of \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) consisting of all \( n \) -planes \( Y \) such that the orthogonal projection

\[
p : {X}_{0} \oplus  {X}_{0}^{ \bot  } \rightarrow  {X}_{0}
\]

maps \( Y \) onto \( {X}_{0} \) (i, e., all \( Y \) such that \( Y \cap  {X}_{0}^{ \bot  } = 0 \) ). Then each \( Y \in  U \) can be considered as the graph of a linear transformation

\[
T\left( Y\right)  : {X}_{0} \rightarrow  {X}_{0}^{ \bot  }.
\]

This defines a one-to-one correspondence

\[
T : U \rightarrow  \operatorname{Hom}\left( {{X}_{0},{X}_{0}^{ \bot  }}\right)  \cong  {\mathbb{R}}^{nk}.
\]

We will see that \( T \) is a homeomorphism.

Let \( {x}_{1},\ldots ,{x}_{n} \) be a fixed orthonormal basis for \( {X}_{0} \) . Note that each \( n \) -plane \( Y \in  U \) has a unique basis \( {y}_{1},\ldots ,{y}_{n} \) such that

\[
p\left( {y}_{1}\right)  = {x}_{1},\ldots , p\left( {y}_{n}\right)  = {x}_{n}.
\]

It is easily verified that the \( n \) -frame \( \left( {{y}_{1},\ldots ,{y}_{n}}\right) \) depends continuously on \( Y \) .

Now note the identity

\[
{y}_{i} = {x}_{i} + T\left( Y\right) {x}_{i}.
\]

Since \( {y}_{i} \) depends continuously on \( Y \) , it follows that the image \( T\left( Y\right) {x}_{i} \in  {X}_{0}^{ \bot  } \) depends continuously on \( Y \) . Therefore the linear transformation \( T\left( Y\right) \) depends continuously on \( Y \) .

On the other hand this identity shows that the \( n \) -frame \( \left( {{y}_{1},\ldots ,{y}_{n}}\right) \) depends continuously on \( T\left( Y\right) \) , and hence that \( Y \) depends continuously on \( T\left( Y\right) \) . Thus the function \( {T}^{-1} \) is also continuous. This completes the proof that \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is a manifold.

Proof that \( {Y}^{ \bot  } \) depends continuously on \( Y \) . Let \( \left( {{\bar{x}}_{1},\ldots ,{\bar{x}}_{k}}\right) \) be a fixed basis for \( {X}_{0}{}^{ \bot  } \) . Define a function

\[
f : {q}^{-1}U \rightarrow  {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n + k}\right)
\]

as follows. For each \( \left( {{y}_{1},\ldots ,{y}_{n}}\right)  \in  {q}^{-1}U \) , apply the Gram-Schmidt process to the vectors \( \left( {{y}_{1},\ldots ,{y}_{n},{\bar{x}}_{1},\ldots ,{\bar{x}}_{k}}\right) \) ; thus obtaining an orthonormal \( \left( {n + k}\right) \) -frame \( \left( {{y}_{1}^{\prime },\ldots ,{y}_{n + k}^{\prime }}\right) \) with \( {y}_{n + 1}^{\prime },\ldots ,{y}_{n + k}^{\prime } \in  {Y}^{ \bot  } \) . Setting \( f\left( {{y}_{1},\ldots ,{y}_{n}}\right)  = \left( {{y}_{n + 1}^{\prime },\ldots ,{y}_{n + k}^{\prime }}\right) \) , it follows that the diagram

![bo_d7du9galb0pc73deir9g_66_587_1174_364_188_0.jpg](images/bo_d7du9galb0pc73deir9g_66_587_1174_364_188_0.jpg)

is commutative. Now \( f \) is continuous, so \( q \circ  f \) is continuous, therefore the correspondence \( Y \mapsto  {Y}^{ \bot  } \) must also be continuous. This completes the proof of 5.1.

A canonical vector bundle \( {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) over \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is constructed as follows. Let

\[
E = E\left( {{\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) }\right)
\]

be the set of all pairs \( {}^{2} \)

( \( n \) -plane in \( {\mathbb{R}}^{n + k} \) , vector in that \( n \) -plane).

This is to be topologized as a subset of \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right)  \times  {\mathbb{R}}^{n + k} \) . The projection map \( \pi  : E \rightarrow  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is defined by \( \pi \left( {X, x}\right)  = X \) , and the vector space structure in the fiber over \( X \) is defined by \( {t}_{1}\left( {X,{x}_{1}}\right)  + {t}_{2}\left( {X,{x}_{2}}\right)  = \left( {X,{t}_{1}{x}_{1} + {t}_{2}{x}_{2}}\right) \) . (Note that \( {\gamma }^{1}\left( {\mathbb{R}}^{n + 1}\right) \) is the same as the line bundle \( {\gamma }_{n}^{1} \) described in §2.)

Lemma 5.2. The vector bundle \( {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) constructed in this way satisfies the local triviality condition.

Proof. Let \( U \) be the neighborhood of \( {X}_{0} \) constructed as in Lemma 5.1. Define the coordinate homeomorphism

\[
h : U \times  {X}_{0} \rightarrow  {\pi }^{-1}\left( U\right)
\]

as follows. Let \( h\left( {Y, x}\right)  = \left( {Y, y}\right) \) where \( y \) denotes the unique vector in \( Y \) which is carried into \( x \) by the orthogonal projection

\[
p : {\mathbb{R}}^{n + k} \rightarrow  {X}_{0}
\]

The identities

\[
h\left( {Y, x}\right)  = \left( {Y, x + T\left( Y\right) x}\right)
\]

and

\[
{h}^{-1}\left( {Y, y}\right)  = \left( {Y,{py}}\right)
\]

show that \( h \) and \( {h}^{-1} \) are continuous. This completes the proof of 5.2.

Given a smooth \( n \) -manifold \( M \subset  {\mathbb{R}}^{n + k} \) the generalized Gauss map

\[
\bar{g} : M \rightarrow  {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right)
\]

can be defined as the function which carries each \( x \in  M \) to its tangent space \( {\mathbf{T}}_{x}M \in  {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) . This is covered by a bundle map

\[
g : E\left( {\tau }_{M}\right)  \rightarrow  E\left( {{\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) }\right) .
\]

---

\( {}^{2} \) Here, and elsewhere, the expression " \( n \) -plane" means linear subspace of dimension \( n \) . Thus we only consider \( n \) -planes through the origin.

---

where \( g\left( {x, v}\right)  = \left( {{\mathbf{T}}_{x}M, v}\right) \) . We will use the abbreviated notation

\[
g : {\tau }_{M} \rightarrow  {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) .
\]

It is clear that both \( g \) and \( \bar{g} \) are continuous.

Not only tangent bundles, but most other \( {\mathbb{R}}^{n} \) -bundles can be mapped into the bundle \( {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) providing that \( k \) is sufficiently large. For this reason \( {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) is called a universal bundle. (Compare Theorems 5.6 and 5.7, as well as [WS51, § 19].)

Lemma 5.3. For any \( n \) -plane bundle \( \xi \) over a compact base space \( B \) there exists a bundle map \( \xi  \rightarrow  {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) provided that \( k \) is sufficiently large.

In order to construct a bundle map \( f : \xi  \rightarrow  {\gamma }^{n}\left( {\mathbb{R}}^{m}\right) \) it is sufficient to construct a map

\[
\widehat{f} : E\left( \xi \right)  \rightarrow  {\mathbb{R}}^{m}
\]

which is linear and injective (i.e., has kernel zero) on each fiber of \( \xi \) . The required function \( f \) can then be defined by

\[
f\left( e\right)  = \left( {\widehat{f}\left( {\text{ fiber through }e}\right) ,\widehat{f}\left( e\right) }\right) .
\]

The continuity of \( f \) is not difficult to verify, making use of the fact that \( \xi \) is locally trivial.

Proof of 5.3. Choose open sets \( {U}_{1},\ldots ,{U}_{r} \) covering \( B \) so that each \( {\left. \xi \right| }_{{U}_{i}} \) is trivial. Since \( B \) is normal, there exist open sets \( {V}_{1},\ldots ,{V}_{r} \) covering \( B \) with \( {\bar{V}}_{i} \subset  {U}_{i} \) . (Compare [Kel55, p. 171].) Here \( {\bar{V}}_{i} \) denotes the closure of \( {V}_{i} \) . Similarly construct \( {W}_{1},\ldots ,{W}_{r} \) with \( {\bar{W}}_{i} \subset  {V}_{i} \) . By Urysohn’s lemma (Compare [Mun00,§33]) we have continuous functions

\[
{\lambda }_{i} : B \rightarrow  \mathbb{R}
\]

which takes the value 1 on \( {\bar{W}}_{i} \) and the value 0 outside of \( {V}_{i} \) .

Since \( {\left. \xi \right| }_{{U}_{i}} \) is trivial there exists a map

\[
{h}_{i} : {\pi }^{-1}\left( {U}_{i}\right)  \rightarrow  {\mathbb{R}}^{n}
\]

which maps each fiber of \( {\left. \xi \right| }_{{U}_{i}} \) linearly onto \( {\mathbb{R}}^{n} \) . Define \( {h}_{i}^{\prime } : E\left( \xi \right)  \rightarrow  {\mathbb{R}}^{n} \) by

\[
{h}_{i}^{\prime }\left( e\right)  = \left\{  \begin{array}{ll} 0 & \text{ for }\pi \left( e\right)  \notin  {V}_{i} \\  {\lambda }_{i}\left( {\pi \left( e\right) }\right) {h}_{i}\left( e\right) & \text{ for }\pi \left( e\right)  \in  {U}_{i} \end{array}\right.
\]

Evidently \( {h}_{i}^{\prime } \) is continuous, and is linear on each fiber. Now define

\[
\widehat{f} : E\left( \xi \right)  \rightarrow  {\mathbb{R}}^{n} \oplus  \cdots  \oplus  {\mathbb{R}}^{n} \cong  {\mathbb{R}}^{rn}
\]

by \( \widehat{f}\left( e\right)  = \left( {{h}_{1}^{\prime }\left( e\right) ,{h}_{2}^{\prime }\left( e\right) ,\ldots ,{h}_{r}^{\prime }\left( e\right) }\right) \) . Then \( \widehat{f} \) is also continuous and maps each fiber injectively. This completes the proof of 5.3.
