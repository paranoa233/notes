# 14.2 Construction of Chern Classes

We will now give an inductive definition of characteristic classes for a complex \( n \) -plane bundle \( \omega \) . It is first necessary to construct a canonical \( \left( {n - 1}\right) \) -plane bundle \( {\omega }_{0} \) over the deleted total space \( {E}_{0} \) . (As in the real case, \( {E}_{0} = {E}_{0}\left( \omega \right) \) denotes the set of all non-zero vectors in the total space \( E\left( \omega \right)  = E\left( {\omega }_{\mathbb{R}}\right) \) .) A point in \( {E}_{0} \) is specified by a fiber \( F \) of \( \omega \) together with a non-zero vector \( v \) in that fiber. First suppose that a Hermitian metric has been specified on \( \omega \) . Then the fiber of \( {\omega }_{0} \) over \( v \) is by definition, the orthogonal complement of \( v \) in the vector space \( F \) . This is a complex vector space of dimension \( n - 1 \) , and these vector spaces clearly can be considered as the fibers of a new vector bundle \( {\omega }_{0} \) over \( {E}_{0} \) .

Alternatively, without using a Hermitian metric, the fiber of \( {\omega }_{0} \) over \( v \) can be defined as the quotient vector space \( F/\mathbb{C}v \) where \( \mathbb{C}v \) is the 1-dimensional subspace spanned by the vector \( v \neq  0 \) . In the presence of a Hermitian metric, it is of course clear that this quotient space is canonically isomorphic to the orthogonal complement of \( v \) in \( F \) .

Recall (Theorem 12.2) that any real oriented \( {2n} \) -plane bundle possesses an exact Gysin sequence

\[
\ldots  \rightarrow  {\mathrm{H}}^{i - {2n}}\left( B\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }{\mathrm{H}}^{i}\left( B\right) \overset{{\pi }_{0}^{ * }}{ \rightarrow  }{\mathrm{H}}^{i}\left( {E}_{0}\right)  \rightarrow  {\mathrm{H}}^{i - {2n} + 1}\left( B\right)  \rightarrow  \ldots
\]

with integer coefficients. For \( i < {2n} - 1 \) the groups \( {\mathrm{H}}^{i - {2n}}\left( B\right) \) and \( {\mathrm{H}}^{i - {2n} + 1}\left( B\right) \) are zero, so it follows that \( {\pi }_{0}^{ * } : {\mathrm{H}}^{i}\left( B\right)  \rightarrow  {\mathrm{H}}^{i}\left( {E}_{0}\right) \) is an isomorphism.

Definition. The Chern classes \( {\mathrm{c}}_{i}\left( \omega \right)  \in  {\mathrm{H}}^{2i}\left( {B;\mathbb{Z}}\right) \) are defined as follows, by

induction on the complex dimension \( n \) of \( \omega \) . The top Chern class \( {\mathrm{c}}_{n}\left( \omega \right) \) is equal to the Euler class \( \mathrm{e}\left( {\omega }_{\mathbb{R}}\right) \) . For \( i < n \) we set

\[
{\mathrm{c}}_{i}\left( \omega \right)  = {\pi }_{0}^{* - 1}{\mathrm{c}}_{i}\left( {\omega }_{0}\right) .
\]

This expression makes sense since \( {\pi }_{0}^{ * } : {\mathrm{H}}^{2i}\left( B\right)  \rightarrow  {\mathrm{H}}^{2i}\left( {E}_{0}\right) \) is an isomorphism for \( i < n \) . Finally, for \( i > n \) the class \( {\mathrm{c}}_{i}\left( \omega \right) \) is defined to be zero.

The formal sum \( \mathrm{c}\left( \omega \right)  = 1 + {\mathrm{c}}_{1}\left( \omega \right)  + \cdots  + {\mathrm{c}}_{n}\left( \omega \right) \) in the ring \( {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}}\right) \) is called the total Chern class of \( \omega \) . Clearly \( \mathrm{c}\left( \omega \right) \) is a unit, so that the inverse

\[
\mathrm{c}{\left( \omega \right) }^{-1} = 1 - {\mathrm{c}}_{1}\left( \omega \right)  + \left( {{\mathrm{c}}_{1}{\left( \omega \right) }^{2} - {\mathrm{c}}_{2}\left( \omega \right) }\right)  + \ldots
\]

is well-defined.

Lemma 14.2 (Naturality). If \( f : B \rightarrow  {B}^{\prime } \) is covered by a bundle map from the complex \( n \) -plane bundle \( \omega \) over \( B \) to the complex \( n \) -plane bundle \( {\omega }^{\prime } \) over \( {B}^{\prime } \) , then \( \mathrm{c}\left( \omega \right)  = {f}^{ * }\mathrm{c}\left( {\omega }^{\prime }\right) \) .

Proof by induction on \( \mathrm{n} \) . The top Chern class is natural, \( {\mathrm{c}}_{n}\left( \omega \right)  = {f}^{ * }{\mathrm{c}}_{n}\left( {\omega }^{\prime }\right) \) , since Euler classes are natural (Property 9.2). To prove the corresponding statement for lower Chern classes, first note that the bundle map \( \omega  \rightarrow  {\omega }^{\prime } \) gives rise to a map

\[
{f}_{0} : {E}_{0}\left( \omega \right)  \rightarrow  {E}_{0}\left( {\omega }^{\prime }\right)
\]

which clearly is covered by a bundle map \( {\omega }_{0} \rightarrow  {\omega }_{0}^{\prime } \) of \( \left( {n - 1}\right) \) -plane bundles. Hence \( {\mathrm{c}}_{i}\left( {\omega }_{0}\right)  = {f}_{0}^{ * }{\mathrm{c}}_{i}\left( {\omega }_{0}^{\prime }\right) \) by the induction hypothesis. Using the commutative diagram

![bo_d7du9galb0pc73deir9g_163_674_1545_383_235_0.jpg](images/bo_d7du9galb0pc73deir9g_163_674_1545_383_235_0.jpg)

and the identities \( {\mathrm{c}}_{i}\left( {\omega }_{0}\right)  = {\pi }_{0}^{ * }{\mathrm{c}}_{i}\left( \omega \right) \) and \( {\mathrm{c}}_{i}\left( {\omega }_{0}^{\prime }\right)  = {\pi }_{0}^{\prime  * }{\mathrm{c}}_{i}\left( {\omega }^{\prime }\right) \) where \( {\pi }_{0}^{\prime } \) is an isomorphism for \( i < n \) , it follows that \( {\mathrm{c}}_{i}\left( \omega \right)  = {f}^{ * }{\mathrm{c}}_{i}\left( {\omega }^{\prime }\right) \) , as required.

Lemma 14.3. If \( {\varepsilon }^{k} \) is the trivial complex \( k \) -bundle over \( B = B\left( \omega \right) \) , then \( \mathrm{c}\left( {\omega  \oplus  {\varepsilon }^{k}}\right)  = \mathrm{c}\left( \omega \right) . \)

Proof. It is sufficient to consider the special case \( k = 1 \) , since the general case then follows by induction. Let \( \phi  = \omega  \oplus  {\varepsilon }^{1} \) . Since the \( \left( {n + 1}\right) \) -plane bundle \( \phi \) has a non-zero cross-section, it follows by property 9.7 that the top Chern class \( {\mathrm{c}}_{n + 1}\left( \phi \right)  = \mathrm{e}\left( {\phi }_{\mathbb{R}}\right) \) is zero, and hence equal to \( {\mathrm{c}}_{n + 1}\left( \omega \right) \) . Let \( s : B \rightarrow  {E}_{0}\left( {\omega  \oplus  {\varepsilon }^{1}}\right) \) be the obvious cross-section. Clearly \( s \) is covered by a bundle map \( \omega  \rightarrow  {\phi }_{0} \) , hence

\[
{s}^{ * }{\mathrm{c}}_{i}\left( {\phi }_{0}\right)  = {\mathrm{c}}_{i}\left( \omega \right)
\]

by 14.2. Substituting \( {\pi }_{0}^{ * }{\mathrm{c}}_{i}\left( \phi \right) \) for \( {\mathrm{c}}_{i}\left( {\phi }_{0}\right) \) , and using the formula \( {s}^{ * } \circ  {\pi }_{0}^{ * } = \mathrm{{id}} \) , it follows that \( {\mathrm{c}}_{i}\left( \phi \right)  = {\mathrm{c}}_{i}\left( \omega \right) \) , as required.
