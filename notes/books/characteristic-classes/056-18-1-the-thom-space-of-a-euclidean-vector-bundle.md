# 18.1 The Thom Space of a Euclidean Vector Bundle

Let \( \xi \) be a \( k \) -plane bundle with a Euclidean metric, and let \( A \subset  E\left( \xi \right) \) be the subset of the total space consisting of all vectors \( v \) with \( \left| v\right|  \geq  1 \) . Then the identification space \( E\left( \xi \right) /A \) in which \( A \) is pinched to a point will be called the Thom space \( \operatorname{Th}\left( \xi \right) \) . Thus \( \operatorname{Th}\left( \xi \right) \) has a preferred base point, denoted by \( {t}_{0} \) , and the complement \( \operatorname{Th}\left( \xi \right)  - {t}_{0} \) consists of all vectors \( v \in  E\left( \xi \right) \) with \( \left| v\right|  < 1 \) .

Remark. If the base space of \( \xi \) is compact, then \( \operatorname{Th}\left( \xi \right) \) can be identified with the single point (Alexandroff) compactification of \( E\left( \xi \right) \) . In fact the correspondence \( v \mapsto  v/\sqrt{1 - {\left| v\right| }^{2}} \) maps \( E\left( \xi \right)  - A \) diffeomorphically onto \( E\left( \xi \right) \) , inducing the required homeomorphism \( \operatorname{Th}\left( \xi \right)  \rightarrow  E\left( \xi \right)  \cup  \{ \infty \} \) .

The following two lemmas describe the topology of \( \operatorname{Th}\left( \xi \right) \) .

Lemma 18.1. If the base space \( B \) is a CW-complex, then the Thom space \( \operatorname{Th}\left( \xi \right) \) is a \( \left( {k - 1}\right) \) -connected CW-complex, having (in addition to the base point \( {t}_{0} \) ) one \( \left( {n + k}\right) \) -cell corresponding to each \( n \) -cell of \( B \) .

In particular, if \( B \) is a finite complex, then \( \operatorname{Th}\left( \xi \right) \) is a finite complex.

Proof. For each open \( n \) -cell \( {e}_{\alpha } \) of \( B \) , the inverse image \( {\pi }^{-1}\left( {e}_{\alpha }\right)  \cap  \left( {E - A}\right) \) is an open cell of dimension \( n + k \) ; these open cells are mutually disjoint and cover the set \( E - A \cong  \operatorname{Th} - {t}_{0} \) . Note that there are no cells in dimension 1 through \( k - 1 \) .

Let \( {\mathbb{D}}^{n} \) be the closed unit ball in \( {\mathbb{R}}^{n} \) and let \( f : {\mathbb{D}}^{n} \rightarrow  B \) be a characteristic map (Definition 6.1) for the cell \( {e}_{\alpha } \) . Then the induced Euclidean vector bundle \( {f}^{ * }\left( \xi \right) \) is trivial by the covering homotopy theorem [Ste51,§11.6], so the vectors of length \( \leq  1 \) in \( E\left( {{f}^{ * }\left( \xi \right) }\right) \) form a topological product \( {\mathbb{D}}^{n} \times  {\mathbb{D}}^{k} \) . The composition

\[
{\mathbb{D}}^{n} \times  {\mathbb{D}}^{k} \subset  E\left( {{f}^{ * }\left( \xi \right) }\right)  \rightarrow  E\left( \xi \right)  \rightarrow  \operatorname{Th}\left( \xi \right)
\]

now forms the required characteristic map for the image of \( {\pi }^{-1}\left( {e}_{\alpha }\right) \) in the Thom space \( \operatorname{Th}\left( \xi \right) \) . Further details will be left to the reader.

We will need to compute (or at least to estimate) the homotopy groups of such a Thom space \( \operatorname{Th}\left( \xi \right) \) . As a first step, here is a description of the homology.

Lemma 18.2. If \( \xi \) is an oriented \( k \) -plane bundle over \( B \) , then each integral homology group \( {\mathrm{H}}_{k + i}\left( {\operatorname{Th}\left( \xi \right) ,{t}_{0}}\right) \) is canonically isomorphic to \( {\mathrm{H}}_{i}\left( B\right) \) .

Proof. Evidently the base space \( B \) is embedded as the zero cross-section of the space \( E - A \cong  \operatorname{Th} - {t}_{0} \) . Let \( {\mathrm{{Th}}}_{0} = {E}_{0}/A \) be the complement of the zero section in the Thom space Th. Then evidently \( {\mathrm{{Th}}}_{0} \) is contractible, so by the exact sequence of the triple \( \left( {\mathrm{{Th}},{\mathrm{{Th}}}_{0},{t}_{0}}\right) \) it follows that

\[
{\mathrm{H}}_{n}\left( {\mathrm{{Th}},{t}_{0}}\right)  \cong  {\mathrm{H}}_{n}\left( {\mathrm{{Th}},{\mathrm{{Th}}}_{0}}\right) .
\]

But an easy excision argument shows that

\[
{\mathrm{H}}_{n}\left( {\mathrm{{Th}},{t}_{0}}\right)  \cong  {\mathrm{H}}_{n}\left( {E,{E}_{0}}\right) .
\]

Together with the Thom isomorphism

\[
{\mathrm{H}}_{n}\left( {E,{E}_{0}}\right)  \cong  {\mathrm{H}}_{n - k}\left( B\right)
\]

of Corollary 10.7, this completes the proof.
