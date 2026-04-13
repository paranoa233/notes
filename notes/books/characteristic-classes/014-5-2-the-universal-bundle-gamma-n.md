# 5.2 The Universal Bundle gamma^n

A canonical bundle \( {\gamma }^{n} \) over \( {\mathrm{{Gr}}}_{n} \) is constructed, just as in the finite dimensional case, as follows. Let

\[
E\left( {\gamma }^{n}\right)  \subset  {\mathrm{{Gr}}}_{n} \times  {\mathbb{R}}^{\infty }
\]

be the set of all pairs

( \( n \) -plane in \( {\mathbb{R}}^{\infty } \) , vector in that \( n \) -plane),

topologized as a subset of the Cartesian product. Define \( \pi  : E\left( {\gamma }^{n}\right)  \rightarrow  {\mathrm{{Gr}}}_{n} \) by \( \pi \left( {X, x}\right)  = X \) , and define the vector space structures in the fibers as before.

Lemma 5.4. This vector bundle \( {\gamma }^{n} \) satisfies the local triviality condition.

---

\( {}^{3} \) It is customary in algebraic topology to call this the "weak topology," a weak topology being one with many open sets. This usage is unfortunate since analysts use the term weak topology with precisely the opposite meaning. On the other hand the terms "fine topology" or "large topology" or "Whitehead topology" are certainly acceptable.

---

The proof will be essentially the same as that of Lemma 5.2. However the following technical lemma will be needed. (Compare [Whi61, §18.5].)

Lemma 5.5. Let \( {A}_{1} \subset  {A}_{2} \subset  \cdots \) and \( {B}_{1} \subset  {B}_{2} \subset  \cdots \) be sequences of locally compact spaces with direct limits \( A \) and \( B \) respectively. Then the Cartesian product topology on \( A \times  B \) coincides with the direct limit topology which is associated with the sequence \( {A}_{1} \times  {B}_{1} \subset  {A}_{2} \times  {B}_{2} \subset  \cdots \) .

Proof. Let \( W \) be open in the direct limit topology, and let \( \left( {a, b}\right) \) be any point of \( W \) . Suppose that \( \left( {a, b}\right)  \in  {A}_{i} \times  {B}_{i} \) . Choose a compact neighborhood \( {K}_{i} \) of \( a \) in \( {A}_{i} \) and a compact neighborhood \( {L}_{i} \) of \( b \) in \( {B}_{i} \) so that \( {K}_{i} \times  {L}_{i} \subset  W \) . It is now possible (with some effort) to choose compact neighborhoods \( {K}_{i + 1} \) of \( {K}_{i} \) in \( {A}_{i + 1} \) and \( {L}_{i + 1} \) of \( {L}_{i} \) in \( {B}_{i + 1} \) so that \( {K}_{i + 1} \times  {L}_{i + 1} \subset  W \) . Continue by induction, constructing neighborhoods \( {K}_{i} \subset  {K}_{i + 1} \subset  {K}_{i + 2} \subset  \cdots \) with union \( U \) and \( {L}_{i} \subset  {L}_{i + 1} \subset  \cdots \) with union \( V \) . Then \( U \) and \( V \) are open sets, and

\[
\left( {a, b}\right)  \in  U \times  V \subset  W.
\]

Thus \( W \) is open in the product topology, which completes the proof of 5.5.

Proof of Lemma 5.4. Let \( {X}_{0} \subset  {\mathbb{R}}^{\infty } \) be a fixed \( n \) -plane, and let \( U \subset  {\mathrm{{Gr}}}_{n} \) be the set of all \( n \) -planes \( Y \) which project onto \( {X}_{0} \) under the orthogonal projection \( p : {\mathbb{R}}^{\infty } \rightarrow  {X}_{0} \) . This set \( U \) is open since, for each finite \( k \) , the intersection

\[
{U}_{k} = U \cap  {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right)
\]

is known to be an open set. Defining

\[
h : U \times  {X}_{0} \rightarrow  {\pi }^{-1}\left( U\right)
\]

as in Lemma 5.2, it follows from 5.2 that \( {\left. h\right| }_{{U}_{k} \times  {X}_{0}} \) is continuous for each \( k \) . Now Lemma 5.5 implies that \( h \) itself is continuous.

As before, the identity \( {h}^{-1}\left( {Y, y}\right)  = \left( {Y,{py}}\right) \) implies that \( {h}^{-1} \) is continuous. Thus \( h \) is a homeomorphism. This completes the proof that \( {\gamma }^{n} \) is locally trivial.

The following two theorems assert that this bundle \( {\gamma }^{n} \) over \( {\mathrm{{Gr}}}_{n} \) is a "universal" \( {\mathbb{R}}^{n} \) -bundle.

Theorem 5.6. Any \( {\mathbb{R}}^{n} \) -bundle \( \xi \) over a paracompact base space admits a bundle map \( \xi  \rightarrow  {\gamma }^{n} \) .

Two bundle maps, \( f, g : \xi  \rightarrow  {\gamma }^{n} \) are called bundle-homotopic if there exists a one-parameter family of bundle maps

\[
{h}_{t} : \xi  \rightarrow  {\gamma }^{n},\;0 \leq  t \leq  1
\]

with \( {h}_{0} = f,{h}_{1} = g \) , such that \( h \) is continuous as a function of both variables. In other words the associated function

\[
h : E\left( \xi \right)  \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  E\left( {\gamma }^{n}\right)
\]

must be continuous.

Theorem 5.7. Any two bundle maps from an \( {\mathbb{R}}^{n} \) -bundle to \( {\gamma }^{n} \) are bundle-homotopic.
