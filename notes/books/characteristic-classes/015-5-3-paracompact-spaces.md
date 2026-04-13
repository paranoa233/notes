# 5.3 Paracompact Spaces

Before beginning the proofs of Theorems 5.6 and 5.7, let us review the definition and the basic theorems concerning paracompactness. For further information the reader is referred [Kel55] and [Dug66].

Definition. A topological space \( B \) is paracompact if \( B \) is a Hausdorff space and if, for every open covering \( \left\{  {U}_{\alpha }\right\} \) of \( B \) , there exists an open covering \( \left\{  {\mathrm{V}}_{\beta }\right\} \) which

1) is a refinement of \( \left\{  {U}_{\alpha }\right\} \) : that is each \( {\mathrm{V}}_{\beta } \) is contained in some \( {U}_{\alpha } \) , and

2) is locally finite: that is each point of \( B \) has a neighborhood which intersects only finitely many of the \( {\mathrm{V}}_{\beta } \) .

Nearly all familiar topological spaces are paracompact. For example (see the above references):

Theorem (A. H. Stone). Every metric space is paracompact.

Theorem (Morita). If a regular topological space is the countable union of compact subsets, then it is paracompact.

Corollary. The direct limit of a sequence \( {K}_{1} \subset  {K}_{2} \subset  {K}_{3} \subset  \cdots \) of compact spaces is paracompact. In particular the infinite Grassmann space \( {\mathrm{{Gr}}}_{n} \) is para-compact.

For it follows from [Whi61, §18.3] that such a direct limit is regular. (The reader should have no difficulty in supplying a proof.)

Theorem (Dieudonné). Every paracompact space is normal.

The proof of 5.6 will be based on the following.

Lemma 5.9. For any fiber bundle \( \xi \) over a paracompact space \( B \) , there exists a locally finite covering of \( B \) by countably many open sets \( {U}_{1},{U}_{2},{U}_{3},\ldots \) so that \( {\left. \xi \right| }_{{U}_{i}} \) is trivial for each \( i \) .

Proof. Choose a locally finite open covering \( \left\{  {\mathrm{V}}_{\alpha }\right\} \) so that each \( {\left. \xi \right| }_{{\mathrm{V}}_{\alpha }} \) is trivial; and choose an open covering \( \left\{  {W}_{\alpha }\right\} \) with \( {\bar{W}}_{\alpha } \subset  {\mathrm{V}}_{\alpha } \) for each \( \alpha \) . (Compare [Kel55, p. 171].) By Urysohn's lemma (Compare [Mun00, §33]) we have continuous functions \( {\lambda }_{\alpha } : B \rightarrow  \mathbb{R} \) which takes the value 1 on \( {\bar{W}}_{\alpha } \) and the value 0 outside of \( {\mathrm{V}}_{\alpha } \) . For each non-vacuous finite subset \( S \) of the index set \( \{ \alpha \} \) , let \( U\left( S\right)  \subset  B \) denote the set of all \( b \in  B \) for which

\[
\mathop{\operatorname{Min}}\limits_{{\alpha  \in  S}}{\lambda }_{\alpha }\left( b\right)  > \mathop{\operatorname{Max}}\limits_{{\alpha  \notin  S}}{\lambda }_{\alpha }\left( b\right) .
\]

Let \( {U}_{k} \) be the union of those sets \( U\left( S\right) \) for which \( S \) has precisely \( k \) elements.

Clearly each \( {U}_{k} \) is an open set, and

\[
B = {U}_{1} \cup  {U}_{2} \cup  {U}_{3} \cup  \cdots
\]

For each given \( b \in  B \) , if precisely \( k \) of the numbers \( {\lambda }_{\alpha }\left( B\right) \) are positive, then \( b \in  {U}_{k} \) . If \( \alpha \) is any element of the set \( S \) , note that

\[
U\left( S\right)  \subset  {\mathrm{V}}_{\alpha }\text{ . }
\]

Since the covering \( \left\{  {\mathrm{V}}_{\alpha }\right\} \) is locally finite, it follows that \( \left\{  {U}_{k}\right\} \) is locally finite. Furthermore, since each \( {\left. \xi \right| }_{{\mathrm{V}}_{\alpha }} \) is trivial, it follows that each \( {\left. \xi \right| }_{U\left( S\right) } \) is trivial. But the set \( {U}_{k} \) is equal to the disjoint union of its open subsets \( U\left( S\right) \) . Therefore \( {\left. \xi \right| }_{{U}_{k}} \) is also trivial.

The bundle map \( f : \xi  \rightarrow  {\gamma }^{n} \) can now be constructed just as in the proof of Lemma 5.3. Details will be left to the reader. This proves Theorem 5.6.

Proof of Theorem 5.7. Any bundle map \( f : \xi  \rightarrow  {\gamma }^{n} \) determines a map

\[
\widehat{f} : E\left( \xi \right)  \rightarrow  {\mathbb{R}}^{\infty }
\]

whose restriction to each fiber of \( \xi \) is linear and injective. Conversely, \( \widehat{f} \) determines \( f \) by the identity

\[
f\left( e\right)  = \left( {\widehat{f}\left( {\text{ fiber through }e}\right) ,\widehat{f}\left( e\right) }\right) .
\]

Let \( f, g : \xi  \rightarrow  {\gamma }^{n} \) be any two bundle maps.

Case 1. Suppose that the vector \( \widehat{f}\left( e\right)  \in  {\mathbb{R}}^{\infty } \) is never equal to a negative multiple of \( \widehat{g}\left( e\right) \) for \( e \neq  0, e \in  E\left( \xi \right) \) . Then the formula

\[
{\widehat{h}}_{t}\left( e\right)  = \left( {1 - t}\right) \widehat{f}\left( e\right)  + t\widehat{g}\left( e\right) ,\;0 \leq  t \leq  1,
\]

defines a homotopy between \( \widehat{f} \) and \( \widehat{g} \) . To prove that \( \widehat{h} \) is continuous as a function of both variables, it is only necessary to prove that the vector space operations in \( {\mathbb{R}}^{\infty } \) (i.e., addition and multiplication by scalars) are continuous. But this follows easily from Lemma 5.5. Evidently \( {\widehat{h}}_{t}\left( e\right)  \neq  0 \) if \( e \) is a non-zero vector of \( E\left( \xi \right) \) . Hence we can define \( h : E\left( \xi \right)  \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  E\left( \eta \right) \) by

\[
{h}_{t}\left( e\right)  = \left( {{\widehat{h}}_{t}\left( {\text{ fiber through }e}\right) ,{\widehat{h}}_{t}\left( e\right) }\right) .
\]

To prove that \( h \) is continuous, it is sufficient to prove that the corresponding function

\[
\bar{h} : B\left( \xi \right)  \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathrm{{Gr}}}_{n}
\]

on the base space is continuous. Let \( U \) be an open subset of \( B\left( \xi \right) \) with \( {\left. \xi \right| }_{U} \) trivial, and let \( {s}_{1},\ldots ,{s}_{n} \) be nowhere dependent cross-sections of \( {\left. \xi \right| }_{U} \) . Then \( {\left. \bar{h}\right| }_{U \times  \left\lbrack  {0,1}\right\rbrack  } \) can be considered as the composition of

1) a continuous function \( B, t \mapsto  \left( {{\widehat{h}}_{t}{s}_{1}\left( B\right) ,\ldots ,{\widehat{h}}_{t}{s}_{n}\left( B\right) }\right) \) from \( U \times  \left\lbrack  {0,1}\right\rbrack \) to the "infinite Stiefel manifold" \( {\mathrm{V}}_{n}\left( {\mathbb{R}}^{\infty }\right)  \subset  {\mathbb{R}}^{\infty } \times  \cdots  \times  {\mathbb{R}}^{\infty } \) , and

2) the canonical projection \( q : {\mathrm{V}}_{n}\left( {\mathbb{R}}^{\infty }\right)  \rightarrow  {\mathrm{{Gr}}}_{n} \) .

Using 5.5 it is seen that \( q \) is continuous. Therefore \( \bar{h} \) is continuous; hence the bundle-homotopy \( h \) between \( f \) and \( g \) is continuous.

General Case. Let \( f, g : \xi  \rightarrow  {\gamma }^{n} \) be arbitrary bundle maps. A bundle map

\[
{d}_{1} : {\gamma }^{n} \rightarrow  {\gamma }^{n}
\]

is induced by the linear transformation \( {\mathbb{R}}^{\infty } \rightarrow  {\mathbb{R}}^{\infty } \) which carries the \( i \) -th basis vector of \( {\mathbb{R}}^{\infty } \) to the \( \left( {{2i} - 1}\right) \) -th. Similarly \( {d}_{2} : {\gamma }^{n} \rightarrow  {\gamma }^{n} \) is induced by the linear transformation which carries the \( i \) -th basis vector to the \( {2i} \) -th. Now note that three bundle-homotopies

\[
f \sim  {d}_{1} \circ  f \sim  {d}_{2} \circ  g \sim  g
\]

are given by three applications of Case 1. Hence \( f \sim  g \) .
