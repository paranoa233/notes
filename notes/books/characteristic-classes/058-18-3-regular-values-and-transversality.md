# 18.3 Regular Values and Transversality

Let \( M \) and \( N \) be smooth manifolds of dimensions \( m \) and \( n \) respectively, and let \( f : M \rightarrow  N \) be a smooth map. A point \( y \in  N \) is called a regular value of \( f \) , or equivalently the map \( f \) is said to be transverse to \( y \) , if for each point \( x \in  {f}^{-1}\left( y\right) \) the induced map

\[
{\left( \mathrm{d}f\right) }_{x} : {\mathbf{T}}_{x}M \rightarrow  {\mathbf{T}}_{y}N
\]

of tangent spaces is surjective. [More generally, we say that \( f \) has \( y \) as regular value throughout some subset \( X \subset  M \) if this condition is satisfied for every \( x \in  {f}^{-1}\left( y\right)  \cap  X \) .] If \( M \) is compact, note that the set of regular value is an open subset of \( N \) .

Of course if the dimension \( m \) is less than \( n \) , then the condition can only be satisfied vacuously: the point \( y \in  N \) is a regular value of \( f \) if and only if \( {f}^{-1}\left( y\right) \) is vacuous. However, if \( m \geq  n \) , then the set \( {f}^{-1}\left( y\right) \) may well be non-vacuous.

If \( y \) is a regular value, note that the inverse image \( {f}^{-1}\left( y\right) \) is a (possibly vacuous) smooth manifold of dimension \( m - n \) . This statement follows easily from the Implicit Function Theorem. See for example [Gra57, p. 138].

The following extremely useful theorem is due to Arthur B. Brown and (in a sharper version) to Arthur Sand.

Theorem (Brown). Let \( f : W \rightarrow  {\mathbb{R}}^{n} \) be a smooth (i.e., infinitely differentiable) mapping, where \( W \) is an open subset of \( {\mathbb{R}}^{m} \) . Then the set of regular values of \( f \) is everywhere dense in \( {\mathbb{R}}^{n} \) .

Proofs may be found, for example, in [New67], [Sar42],[Ste99] and [MW97].

It follows easily that for any smooth map \( f : M \rightarrow  N \) , assuming only that there is a countable basis for the topology of \( M \) , the set of regular values is a countable intersection of dense open sets, and hence is everywhere dense in \( N \) .

Now suppose that we are given a smooth submanifold \( Y \subset  N \) of dimension \( n - k \) . A smooth map \( f : M \rightarrow  N \) is said to be transverse to \( Y \) , if for every \( x \in  {f}^{-1}\left( Y\right) \) the composition

\[
{\mathbf{T}}_{x}M\xrightarrow[]{{\left( \mathrm{d}f\right) }_{x}}{\mathbf{T}}_{y}N \rightarrow  \left( {{\mathbf{T}}_{y}N}\right) /\left( {{\mathbf{T}}_{y}Y}\right)
\]

from the tangent space at \( x \) to the normal space at \( f\left( x\right)  = y \) is surjective. [More generally, if \( f \) is tranverse to \( Y \) throughout some subset of \( X \) of \( M \) if this condition is satisfied for every \( x \in  X \cap  {f}^{-1}\left( Y\right) \) .]

If \( f \) is transverse to \( Y \) , then using the Implicit Function Theorem one verifies that the inverse image \( {f}^{-1}\left( Y\right) \) is a (possibly vacuous) smooth manifold of dimension \( m - k \) .

If \( {\nu }^{k} \) is the normal bundle of \( Y \) in \( N \) , then it is not difficult to show that the bundle over \( {f}^{-1}\left( Y\right) \) induced from \( {\nu }^{k} \) by \( f \) can be identified with the normal bundle of \( {f}^{-1}\left( Y\right) \) in \( M \) . In particular, if \( {\nu }^{k} \) is an oriented vector bundle, and if \( M \) is an oriented manifold, then it follows that \( {f}^{-1}\left( Y\right) \) is an oriented manifold.

In order to actually construct such transversal mappings, we proceed in two steps, starting with the theorem of Brown and Sard. Consider again an open set \( W \subset  {\mathbb{R}}^{m} \) and consider a smooth map \( f : W \rightarrow  {\mathbb{R}}^{k} \) . Suppose that \( f \) has the origin as a regular value throughout some relatively closed subset \( X \subset  W \) . Let \( K \) be a compact subset of \( W \) .

Lemma 18.5. There exists a smooth map \( g : W \rightarrow  {\mathbb{R}}^{k} \) which coincides with \( f \) outside of a compact set, and which has the origin as a regular value throughout \( X \cup  K \) . In fact, given \( \varepsilon  > 0 \) , we can choose \( g \) uniformly close to \( f \) so that \( \left| {f\left( x\right)  - g\left( x\right) }\right|  < \varepsilon \) for all \( x. \)

Proof. Using a smooth partition of unity, construct a smooth map \( \lambda  : W \rightarrow \; \left\lbrack  {0,1}\right\rbrack \) which takes the value 1 on a neighborhood of \( K \) and vanishes outside of a larger compact set \( {K}^{\prime } \subset  W \) . If \( y \) is any regular value of \( f \) , with \( \left| y\right|  < \varepsilon \) , then the function \( g \) defined by

\[
g\left( x\right)  = f\left( x\right)  - \lambda \left( x\right) y
\]

will certainly:

(a) have 0 as a regular value throughout \( K \) ,

(b) coincide with \( f \) outside \( {K}^{\prime } \) , and

(c) satisfy \( \left| {g\left( x\right)  - f\left( x\right) }\right|  < \varepsilon \) .

In fact, by Brown’s theorem, \( y \) can be chosen arbitrarily close to the origin 0 . If \( y \) is chosen sufficiently close to 0, we claim that \( g \) also has 0 as regular value throughout the intersection \( {K}^{\prime } \cap  X \) . For by choosing \( \left| y\right| \) small, we not only guarantee that \( g \) will be uniformly close to \( f \) , but also that the partial derivatives \( \partial {g}_{i}/\partial {x}_{j} \) will be uniformly close to the derivatives \( \partial {f}_{i}/\partial {x}_{j} \) . Therefore, since \( f \) has 0 as regular value throughout the compact set \( {K}^{\prime } \cap  X \) , it will follow easily that \( g \) also has 0 as regular value throughout \( {K}^{\prime } \cap  X \) . (See Problem 18-A.) Together with (a) and (b) this implies that \( g \) has 0 as regular value throughout the union \( X \cup  K \) , as required.

Now let \( \xi \) be a smooth oriented \( k \) -plane bundle. The base space \( B \) of \( \xi \) is smoothly embedded as the zero cross-section in the total space \( E\left( \xi \right) \) , and hence in the Thom space \( \mathrm{{Th}} = \mathrm{{Th}}\left( \xi \right) \) .

Given any continuous map \( f \) from the sphere \( {S}^{m} \) to the Thom space \( \mathrm{{Th}} \) , we would like to first approximate \( f \) by a "smooth" map. This does not quite make sense, since Th is not a manifold. However Th \( - {t}_{0} \) , the complement of the base point, certainly does have the structure of a smooth manifold, and it is not difficult to approximate \( f \) by a homotopic map \( {f}_{0} \) which coincides with \( f \) on \( {f}^{-1}\left( {t}_{0}\right)  = {f}_{0}^{-1}\left( {t}_{0}\right) \) and is smooth throughout the complement \( {f}_{0}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right) \) . The necessary techniques are described, for example, in [Ste51, §6.7].

Theorem 18.6. Every continuous map \( f : {S}^{m} \rightarrow  \operatorname{Th}\left( \xi \right) \) is homotopic to a map \( g \) which is smooth throughout \( {g}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right) \) , and is transverse to the zero cross-section \( B \) . The oriented cobordism class of the resulting smooth \( \left( {m - k}\right)  - \) dimensional manifold \( {g}^{-1}\left( B\right) \) depends only on the homotopy class of \( g \) . Hence the correspondence

\[
g \mapsto  {g}^{-1}\left( B\right)
\]

gives rise to a homomorphism from the homotopy group \( {\pi }_{m}\left( {\mathrm{{Th}},{t}_{0}}\right) \) to the oriented cobordism group \( {\Omega }_{m - k} \) .

Proof. As noted above, we can first approximate \( f \) by a map \( {f}_{0} \) which is smooth throughout \( {f}_{0}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right) \) . Choose a covering of the compact set \( {f}_{0}^{-1}\left( B\right) \) by open subsets \( {W}_{1},\ldots ,{W}_{r} \) of \( {f}^{-1}\left( {\mathrm{{Th}} - {t}_{0}}\right) \) which are small enough so that each image

\[
{f}_{0}\left( {W}_{i}\right)  \subset  \operatorname{Th} - {t}_{0} \subset  E\left( \xi \right)
\]

is contained in some product coordinate patch

\[
{\pi }^{-1}\left( {U}_{i}\right)  \cong  {U}_{i} \times  {\mathbb{R}}^{k}
\]

for the vector bundle \( \xi \) . Here \( {U}_{i} \) denotes an open subset of \( B \) which is small enough so that the bundle \( {\left. \xi \right| }_{{U}_{i}} \) is trivial.

Choose compact sets \( {K}_{i} \subset  {W}_{i} \) so that \( {f}_{0}^{-1}\left( B\right) \) is contained in the interior of \( {K}_{1} \cup  \ldots  \cup  {K}_{r} \) . Then we will modify \( {f}_{0} \) within one open set \( {W}_{i} \) after another, constructing mapping \( {f}_{1},{f}_{2},\ldots ,{f}_{r} \) satisfying following three conditions.

(1) Each \( {f}_{i} \) is smooth throughout \( {f}_{i}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right)  = {f}_{0}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right) \) , and coinciding with \( {f}_{i - 1} \) outside of a compact subset of \( {W}_{i} \) .

(2) Each \( {f}_{i} \) is transverse to \( B \) throughout the set \( {K}_{1} \cup  {K}_{2} \cup  \ldots  \cup  {K}_{i} \) .

(3) The projection \( \pi \left( {{f}_{i}\left( x\right) }\right)  \in  B \) is equal to \( \pi \left( {{f}_{0}\left( x\right) }\right) \) for all \( x \in  {f}_{0}^{-1}\left( {\mathrm{{Th}} - {t}_{0}}\right) \) .

Furthermore we will choose each \( {f}_{i} \) "close" to \( {f}_{i - 1} \) in a sense to be made precise later. To begin the construction, we assume inductively that a map \( {f}_{i - 1} \) has been chosen so as to satisfy (1), (2) and (3). It follows from Condition (3) that \( {f}_{i - 1} \) must map the open set \( {W}_{i} \) into the product coordinate patch \( {\pi }^{-1}\left( U\right) \) . Using the product structure

\[
{\pi }^{-1}\left( {U}_{i}\right)  \cong  {U}_{i} \times  {\mathbb{R}}^{k}
\]

let \( {\rho }_{i} : {\pi }^{-1}\left( {U}_{i}\right)  \rightarrow  {\mathbb{R}}^{k} \) be the projection map to the second factor. We want to choose a new map \( x \mapsto  {f}_{i}\left( x\right) \) for \( x \in  {W}_{i} \) . The first coordinate \( \pi \left( {{f}_{i}\left( x\right) }\right) \) is already determined by (3), so we need only choose the second coordinate \( {\rho }_{i}\left( {{f}_{i}\left( x\right) }\right) \) .

Since \( {f}_{i - 1} \) satisfies Condition (2), it follows easily that the composition \( x \mapsto  {\rho }_{i}\left( {{f}_{i - 1}\left( x\right) }\right) \) has the origin of \( {\mathbb{R}}^{k} \) as a regular value throughout the relatively closed subset \( \left( {{K}_{1} \cup  \ldots  \cup  {K}_{i - 1}}\right)  \cap  {W}_{i} \) of \( {W}_{i} \) . Hence, by Lemma 18.5, we can approximate this composition by a map from \( {W}_{i} \) to \( {\mathbb{R}}^{k} \) which

(a) agrees with \( {\rho }_{i} \circ  {f}_{i - 1} \) outside of a compact subset of \( {W}_{i} \) , and

(b) has the origin as regular value throughout \( \left( {{K}_{1} \cup  \ldots  \cup  {K}_{i}}\right)  \cap  {W}_{i} \) .

Taking this approximating map to be \( {\rho }_{i} \circ  {f}_{i} \) , we have evidently, in view of Conditions (1) and (3), defined \( {f}_{i}\left( x\right) \) for all \( x \) . Furthermore, it is clear that this new map \( {f}_{i} \) will satisfy Condition (2).

Thus, proceeding by induction, we can construct maps \( {f}_{1},{f}_{2},\ldots ,{f}_{r} \) , all satisfying the Conditions (1),(2),(3). Let \( g = {f}_{r} \) . Clearly \( g \) is transverse to \( B \) throughout the compact set \( {K}_{1} \cup  \ldots  \cup  {K}_{r} \) . If we can guarantee that the entire inverse image \( {g}^{-1}\left( B\right) \) is contained in \( {K}_{1} \cup  \ldots  \cup  {K}_{\mathrm{r}} \) , then we will be sure that \( g \) is transverse to \( B \) everywhere, as required.

For each \( t \in  \operatorname{Th} - {t}_{0} \cong  E - A \) let \( 0 \leq  \left| t\right|  < 1 \) denote the Euclidean norm, so that \( \left| t\right|  = 0 \) if and only if \( t \in  B \) . It is convenient to set \( \left| {t}_{0}\right|  = 1 \) . Since \( {K}_{1} \cup  \ldots  \cup  {K}_{r} \) is a neighborhood of \( {f}_{0}^{-1}\left( B\right) \) in the compact space \( {S}^{m} \) , there exists a constant \( c > 0 \) so that

\[
\left| {{f}_{0}\left( x\right) }\right|  \geq  c
\]

for all \( x \notin  {K}_{1} \cup  \ldots  \cup  {K}_{r} \) . Suppose that each \( {f}_{i} \) is chosen so close to \( {f}_{i - 1} \) that

\[
\left| {{f}_{i}\left( x\right)  - {f}_{i - 1}\left( x\right) }\right|  < c/r
\]

for all \( x \) . Then evidently

\[
\left| {g\left( x\right)  - {f}_{0}\left( x\right) }\right|  < c.
\]

Therefore \( \left| {g\left( x\right) }\right|  \neq  0 \) for \( x \notin  {K}_{1} \cup  \ldots  \cup  {K}_{r} \) , and the entire inverse image \( {g}^{-1}\left( B\right) \) must be contained in \( {K}_{1} \cup  \ldots  \cup  {K}_{r} \) . Hence \( g \) is transverse to \( B \) everywhere, and the inverse image \( {g}^{-1}\left( B\right) \) is a smooth, compact, oriented \( \left( {m - k}\right) \) -dimensional manifold. This proves the first part of 18.6.

Next consider two homotopic maps \( g \) and \( {g}^{\prime } \) from \( {S}^{m} \) to Th, both being smooth on the inverse image of \( \mathrm{{Th}} - {t}_{0} \) and both being transverse to \( B \) . Then it is not difficult to construct a homotopy

\[
{h}_{0} : {S}^{m} \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  \text{ Th }
\]

which is smooth throughout \( {h}_{0}^{-1}\left( {\operatorname{Th} - {t}_{0}}\right) \) , and which satisfies

\[
{h}_{0}\left( {x, t}\right)  = g\left( x\right) \;\text{ for }t \in  \left\lbrack  {0,1}\right\rbrack  ,
\]

\[
{h}_{0}\left( {x, t}\right)  = {g}^{\prime }\left( x\right) \;\text{ for }t \in  \left\lbrack  {2,3}\right\rbrack  .
\]

Proceeding as above, we can then construct a new map \( h : {S}^{m} \times  \left\lbrack  {0,3}\right\rbrack   \rightarrow \) Th which coincides with \( {h}_{0} \) except on a compact subset of \( {S}^{m} \times  \left( {0,3}\right) \) , and which is transverse to \( B \) . The construction is inductive, making sure each stage that transversality throughout the set \( {S}^{m} \times  \left\lbrack  {0,1}\right\rbrack   \cup  {S}^{m} \times  \left\lbrack  {2,3}\right\rbrack \) is not lost. The inverse image \( {h}^{-1}\left( B\right) \) under this new homotopy will then provide the required oriented cobordism between \( {g}^{-1}\left( B\right) \) and \( {g}^{\prime  - 1}\left( B\right) \) . Thus the oriented cobordism class of \( {g}^{-1}\left( B\right) \) depends only on the homotopy class of \( B \) .

Since the composition operations in the homotopy group \( {\pi }_{m}\left( {\mathrm{{Th}},{t}_{0}}\right) \) clearly corresponds to the disjoint union operation for the manifolds \( {g}^{-1}\left( B\right) \) , it follows that this correspondence \( g \mapsto  {g}^{-1}\left( B\right) \) gives rise to a well defined homomorphism from \( {\pi }_{m}\left( {\mathrm{{Th}},{t}_{0}}\right) \) to the cobordism group \( {\Omega }_{m - k} \) .
