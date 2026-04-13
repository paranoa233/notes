# 4.4 Stiefel-Whitney Number

We will now describe a tool which allows us to compare certain Stiefel-Whitney classes of two different manifolds.

Let \( M \) be a closed, possibly disconnected, smooth \( n \) -dimensional manifold. Using mod 2 coefficients, there is a unique fundamental homology class

\[
{\mu }_{M} \in  {\mathrm{H}}_{n}\left( {M;\mathbb{Z}/2}\right) \text{ . }
\]

(See Appendix A.) Hence for any cohomology class \( v \in  {\mathrm{H}}^{n}\left( {M;\mathbb{Z}/2}\right) \) , the Kronecker index

\[
\left\langle  {v,{\mu }_{M}}\right\rangle   \in  \mathbb{Z}/2,
\]

is defined. We will sometimes use the abbreviated notation \( v\left\lbrack  M\right\rbrack \) for this Kronecker index.

Let \( {r}_{1},\ldots ,{r}_{n} \) be non-negative integers with \( {r}_{1} + 2{r}_{2} + \cdots  + n{r}_{n} = n \) . Then corresponding to any vector bundle \( \xi \) we can form the monomial

\[
{\mathrm{w}}_{1}{\left( \xi \right) }^{{r}_{1}}\cdots {\mathrm{w}}_{n}{\left( \xi \right) }^{{r}_{n}}
\]

in \( {\mathrm{H}}^{n}\left( {B\left( \xi \right) ;\mathbb{Z}/2}\right) \) . In particular we can carry out this construction if \( \xi \) is the tangent bundle of the manifold \( M \) .

Definition. The corresponding integer mod 2

\[
\left\langle  {{\mathrm{w}}_{1}{\left( {\tau }_{M}\right) }^{{r}_{1}}\cdots {\mathrm{w}}_{n}{\left( {\tau }_{M}\right) }^{{r}_{n}},{\mu }_{M}}\right\rangle  \text{ or briefly }{\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}\left\lbrack  M\right\rbrack  \text{ , }
\]

is called the Stiefel-Whitney number of \( M \) associated with the monomial \( {\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}. \)

In studying these numbers, we will be interested in the collection of all possible Stiefel-Whitney numbers for a given manifold. Thus two different manifolds \( M \) and \( {M}^{\prime } \) have the same Stiefel-Whitney numbers if

\[
{\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}\left\lbrack  M\right\rbrack   = {\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}\left\lbrack  {M}^{\prime }\right\rbrack
\]

for every monomial \( {\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}} \) of total dimension \( n \) . (Compare Definition 88 of a partition and 6-D.)

As an example, let us try to compute the Stiefel-Whitney numbers of the projective space \( {\mathbb{P}}^{n} \) . (which is about the only manifold we are able to handle at this point.) Let \( \tau \) denote the tangent bundle of \( {\mathbb{P}}^{n} \) . If \( n \) is even, then the cohomology class \( {\mathrm{w}}_{n}\left( \tau \right)  = \left( {n + 1}\right) {a}^{n} \) is non-zero, and it follows that the Stiefel-Whitney number \( {\mathrm{w}}_{n}\left\lbrack  {\mathbb{P}}^{n}\right\rbrack \) is non-zero. Similarly, since \( {\mathrm{w}}_{1}\left( \tau \right)  = \left( {n + 1}\right) a \neq  0 \) , it follows that \( {\mathrm{w}}_{1}^{n}\left\lbrack  {\mathbb{P}}^{n}\right\rbrack   \neq  0 \) . If \( n \) is actually a power of 2, then \( \mathrm{w}\left( \tau \right)  = 1 + a + {a}^{n} \) , and it follows that all other Stiefel-Whitney numbers of \( {\mathbb{P}}^{n} \) are zero. In any case, even if \( n \) is not a power of 2, the remaining Stiefel-Whitney numbers can certainly be computed effectively as products of binomial coefficients.

On the other hand if \( n \) is odd, say \( n = {2k} - 1 \) , then \( \mathrm{w}\left( \tau \right)  = {\left( 1 + a\right) }^{2k} = {\left( 1 + {a}^{2}\right) }^{k} \) , so it follows that \( {\mathrm{w}}_{j}\left( \tau \right)  = 0 \) whenever \( j \) is odd. Since every monomial of total dimension \( {2k} - 1 \) must contain a factor \( {\mathrm{w}}_{j} \) of odd dimension, it follows that all of the Stiefel-Whitney numbers of \( {\mathbb{P}}^{{2k} - 1} \) are zero. This gives some indication of how much detail and structure this invariant overlooks.

The importance of Stiefel-Whitney numbers is indicated by the following theorem and its converse.

Theorem 4.9 (Pontrjagin). If \( B \) is a smooth compact \( \left( {n + 1}\right) \) -dimensional manifold with boundary equal to \( M \) (compare \( \text{ § }{17} \) ), then the Stiefel-Whitney numbers of \( M \) are all zero.

Proof. Let us denote the fundamental homology class of the pair by

\[
{\mu }_{B} \in  {\mathrm{H}}_{n + 1}\left( {B, M}\right) ,
\]

the coefficient group \( \mathbb{Z}/2 \) being understood. Then the natural homomorphism

\[
\partial  : {\mathrm{H}}_{n + 1}\left( {B, M}\right)  \rightarrow  {\mathrm{H}}_{n}\left( M\right)
\]

maps \( {\mu }_{B} \) to \( {\mu }_{M} \) . (Compare Appendix A.) For any class \( v \in  {\mathrm{H}}^{n}\left( M\right) \) , note the identity

\[
\left\langle  {v,\partial {\mu }_{B}}\right\rangle   = \left\langle  {{\delta v},{\mu }_{B}}\right\rangle  ,
\]

where \( \delta \) denotes the natural homomorphism from \( {\mathrm{H}}^{n}\left( M\right) \) to \( {\mathrm{H}}^{n + 1}\left( {B, M}\right) \) . (There is no sign since we are working mod 2.) Consider the tangent bundle \( {\tau }_{B} \) restricted to \( M \) , as well as the sub-bundle \( {\tau }_{M} \) . Choosing a Euclidean metric on \( {\tau }_{B} \) , there is a unique outward normal vector field along \( M \) , spanning a trivial line bundle \( {\varepsilon }^{1} \) , and it follows that

\[
{\left. {\tau }_{B}\right| }_{M} \cong  {\tau }_{M} \oplus  {\varepsilon }^{1}.
\]

Hence the Stiefel-Whitney classes of \( {\tau }_{B} \) , restricted to \( M \) , are precisely equal to the Stiefel-Whitney classes \( {w}_{j} \) of \( {\tau }_{M} \) . Using the exact sequence

\[
{\mathrm{H}}^{n}\left( B\right) \overset{{i}^{ * }}{ \rightarrow  }{\mathrm{H}}^{n}\left( M\right) \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{n + 1}\left( {B, M}\right)
\]

where \( {i}^{ * } \) is the restriction homomorphism, it follows that

\[
\delta \left( {{\mathrm{w}}_{1}^{{r}_{1}}\ldots {\mathrm{w}}_{n}^{{r}_{n}}}\right)  = 0,
\]

and therefore

\[
\left\langle  {\left( {{\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}}\right) ,\partial {\mu }_{B}}\right\rangle   = \left\langle  {\delta \left( {{\mathrm{w}}_{1}^{{r}_{1}}\cdots {\mathrm{w}}_{n}^{{r}_{n}}}\right) ,{\mu }_{B}}\right\rangle  .
\]

Thus all Stiefel-Whitney numbers of \( M \) are zero.

The converse, due to Thom, is much harder to prove.

Theorem 4.10 (Thom). If all of the Stiefel-Whitney numbers of \( M \) are zero, then \( M \) can be realized as the boundary of some smooth compact manifold.

For proof, the reader is referred to [Sto68].

For example the union of two disjoint copies of \( M \) , which certainly has all Stiefel-Whitney numbers zero, is equal to the boundary of the cylinder \( M \times  \left\lbrack  {0,1}\right\rbrack \) . Similarly, the odd dimensional projective space \( {\mathbb{P}}^{{2k} - 1} \) has all Stiefel-Whitney numbers zero. The reader may enjoy trying to prove directly that \( {\mathbb{P}}^{{2k} - 1} \) is a boundary.

Now let us introduce the concept of "cobordism class".

Definition. Two smooth closed \( n \) -manifolds \( {M}_{1} \) and \( {M}_{2} \) belong to the same unoriented cobordism class iff their disjoint union \( {M}_{1} \sqcup  {M}_{2} \) is the boundary of a smooth compact \( \left( {n + 1}\right) \) -dimensional manifold.

![bo_d7du9galb0pc73deir9g_59_502_1455_728_275_0.jpg](images/bo_d7du9galb0pc73deir9g_59_502_1455_728_275_0.jpg)

Figure 6

Theorems 4.9, 4.10 have the following important consequence.

Corollary 4.11. Two smooth closed \( n \) -manifolds belong to the same cobordism class if and only if all of their corresponding Stiefel-Whitney numbers are equal.

Proof. The proof is immediate.

Here are five problems for the reader.

Problem 4-A. Show that the Stiefel-Whitney classes of a Cartesian product are given by

\[
{\mathrm{w}}_{k}\left( {\xi  \times  \eta }\right)  = \mathop{\sum }\limits_{{i = 0}}^{k}{\mathrm{w}}_{i}\left( \xi \right)  \times  {\mathrm{w}}_{k - i}\left( \eta \right) .
\]

Problem 4-B. Prove the following theorem of Stiefel. If \( n + 1 = {2}^{r}m \) with \( m \) odd, then there do not exist \( {2}^{r} \) vector fields on the projective space \( {\mathbb{P}}^{n} \) which are everywhere linearly independent. \( {}^{2} \)

Problem 4-C. A manifold \( M \) is said to admit a field of tangent \( k \) -planes if its tangent bundle admits a sub-bundle of dimension \( k \) . Show that \( {\mathbb{P}}^{n} \) admits a field of tangent 1-planes if and only if \( n \) is odd. Show that \( {\mathbb{P}}^{4} \) and \( {\mathbb{P}}^{6} \) do not admit fields of tangent 2-planes.

Problem 4-D. If the \( n \) -dimensional manifold \( M \) can be immersed in \( {\mathbb{R}}^{n + 1} \) show that each \( {\mathrm{w}}_{i}\left( M\right) \) is equal to the \( i \) -fold cup product \( {\mathrm{w}}_{1}{\left( M\right) }^{i} \) . If \( {\mathbb{P}}^{n} \) can be immersed in \( {\mathbb{R}}^{n + 1} \) show that \( n \) must be of the form \( {2}^{r} - 1 \) or \( {2}^{r} - 2 \) .

Problem 4-E. Show that the set \( {\mathfrak{N}}_{n} \) consisting of all unoriented cobordism classes of smooth closed \( n \) -manifolds can be made into an additive group. This cobordism group \( {\mathfrak{N}}_{n} \) is finite by corollary 4.11, and is clearly a module over \( \mathbb{Z}/2 \) . Using the manifolds \( {\mathbb{P}}^{2} \times  {\mathbb{P}}^{2} \) and \( {\mathbb{P}}^{4} \) , show that \( {\mathfrak{N}}_{4} \) contains at least four distinct elements.

---

\( {}^{2} \) Compare [Sti35]; [WS51]; [Ada62].

---
