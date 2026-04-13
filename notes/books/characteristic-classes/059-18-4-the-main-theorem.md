# 18.4 The Main Theorem

In place of the smooth oriented \( k \) -plane bundle of Theorem 18.6, let us substitute the universal oriented \( k \) -plane bundle \( {\widetilde{\gamma }}^{k} \) over \( {\widetilde{\operatorname{Gr}}}_{k}\left( {\mathbb{R}}^{\infty }\right) \) . The following result lies at the heart of Thom's theory.

Theorem (Thom). For \( k > n + 1 \) the homotopy group \( {\pi }_{n + k}\left( {\operatorname{Th}\left( {\widetilde{\gamma }}^{k}\right) ,{t}_{0}}\right) \) of the universal Thom space is canonically isomorphic to the oriented cobordism group \( {\Omega }_{n} \) . Similarly the homotopy group \( {\pi }_{n + k}\left( {\operatorname{Th}\left( {\gamma }^{k}\right) ,{t}_{0}}\right) \) associated with the unoriented universal bundle is canonically isomorphic to the unoriented cobordism group \( {\mathfrak{N}}_{n} \) .

Remark. Thom uses the notations \( \operatorname{MSO}\left( k\right) \) and \( \operatorname{MO}\left( k\right) \) for these two universal Thom spaces. These correspond to the standard notations \( \operatorname{BSO}\left( k\right) \) and \( \operatorname{BO}\left( k\right) \) for the associated universal base spaces.

To simplify our discussion, we will not prove all of Thom's theorem, but only the following partial statement. Let \( {\widetilde{\gamma }}_{p}^{k} = {\widetilde{\gamma }}^{k}\left( {\mathbb{R}}^{k + p}\right) \) be the bundle of oriented \( k \) -planes in \( \left( {k + p}\right) \) -space.

Lemma 18.7. If \( k \geq  n \) and \( p \geq  n \) , then the homomorphism

\[
{\pi }_{n + k}\left( {\operatorname{Th}\left( {\widetilde{\gamma }}_{p}^{k}\right) }\right)  \rightarrow  {\Omega }_{n}
\]

of Theorem 18.6 is surjective.

Proof. Let \( {M}^{n} \) be an arbitrary smooth, compact, oriented \( n \) -dimensional manifold. Then, by a theorem of [Whi44], \( {M}^{n} \) can be embedded in the Euclidean space \( {\mathbb{R}}^{n + k} \) . Proceeding as in Theorem 11.1, we can choose a neighborhood \( U \) of \( {M}^{n} \) in \( {\mathbb{R}}^{n + k} \) which is diffeomorphic to the total space \( E\left( {\nu }^{k}\right) \) of the normal bundle. Using the Gauss map, we have

\[
U \cong  E\left( {\nu }^{k}\right)  \rightarrow  E\left( {\widetilde{\gamma }}_{n}^{k}\right)  \subset  E\left( {\widetilde{\gamma }}_{p}^{k}\right) ,
\]

and composing with the canonical map \( E\left( {\widetilde{\gamma }}_{p}^{k}\right)  \rightarrow  \operatorname{Th}\left( {\widetilde{\gamma }}_{p}^{k}\right) \) , we obtain a map \( g : U \rightarrow  \operatorname{Th}\left( {\widetilde{\gamma }}_{p}^{k}\right) \) which is transverse to the zero cross-section \( B \) , and satisfies \( {g}^{-1}\left( B\right)  = {M}^{n}. \)

Now extend \( g \) to the one-point compactification \( {\mathbb{R}}^{n + k} \cup  \{ \infty \}  \cong  {S}^{n + k} \) by mapping \( {S}^{n + k} - U \) to the base point \( {t}_{0} \) . The resulting map \( \widehat{g} : {S}^{n + k} \rightarrow  \operatorname{Th}\left( {\widetilde{\gamma }}_{p}^{k}\right) \) clearly gives rise, under the construction of Theorem 18.6, to the cobordism class of \( {M}^{n} \) .

We are now ready to prove our main result.

Theorem 18.8 (Thom). The oriented cobordism group \( {\Omega }_{n} \) is finite for \( n \text{ ≢ } 0 \) (mod 4), and is a finitely generated group with rank equal to \( p\left( r\right) \) , the number of partitions of \( r \) , when \( n = {4r} \) .

Proof. By Lemma 18.7 the group \( {\Omega }_{n} \) is a homomorphic image of \( {\pi }_{n + k}\left( {\operatorname{Th}\left( {\widetilde{\gamma }}_{p}^{k}\right) }\right) \) for \( k \) and \( p \) large, and by Corollary 18.4 this latter group is \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphic to \( {\mathrm{H}}_{n}\left( {{\widetilde{\mathrm{{Gr}}}}_{k}\left( {\mathbb{R}}^{k + p}\right) ;\mathbb{Z}}\right) \) . But using Theorem 15.9, the group \( {\mathrm{H}}_{n}\left( {{\widetilde{\mathrm{{Gr}}}}_{k}\left( {\mathbb{R}}^{k + p}\right) ;\mathbb{Z}}\right) \) is finite for \( n \text{ ≢ } 0\left( {\;\operatorname{mod}\;4}\right) \) , and is finitely generated of rank \( p\left( r\right) \) for \( n = {4r} \) . Therefore \( {\Omega }_{n} \) is finite for \( n \text{ ≢ } 0\left( {\;\operatorname{mod}\;4}\right) \) , and \( {\Omega }_{4r} \) is finitely generated with

\[
\operatorname{rank}\left( {\Omega }_{4r}\right)  \leq  p\left( r\right) .
\]

Since \( \operatorname{rank}\left( {\Omega }_{4r}\right)  \geq  p\left( r\right) \) by Corollary 17.5, the conclusion follows.

If we kill torsion by tensoring the cobordism ring \( {\Omega }_{ * } \) with the rational numbers \( \mathbb{Q} \) , then evidently the products

\[
{\mathbb{P}}^{2{i}_{1}}\left( \mathbb{C}\right)  \times  \ldots  \times  {\mathbb{P}}^{2{i}_{r}}\left( \mathbb{C}\right) ,
\]

where \( {i}_{1},\ldots ,{i}_{r} \) ranges over all partitions of \( k \) , will be linearly independent, and hence will form a basis for the vector space \( {\Omega }_{4k} \otimes  \mathbb{Q} \) . (Compare Corollary 17.5.) This proves the following.

Corollary 18.9. The tensor product \( {\Omega }_{ * } \otimes  \mathbb{Q} \) is a polynomial algebra over \( \mathbb{Q} \) with independent generators \( {\mathbb{P}}^{2}\left( \mathbb{C}\right) ,{\mathbb{P}}^{4}\left( \mathbb{C}\right) ,{\mathbb{P}}^{6}\left( \mathbb{C}\right) ,\ldots \)

Another immediate consequence is the following.

Corollary 18.10. Let \( {M}^{n} \) be smooth, compact and oriented. Then some positive multiple \( {M}^{n} + \ldots  + {M}^{n} \) is an oriented boundary if and only if every Pontrjagin number \( {\mathrm{p}}_{I}\left\lbrack  {M}^{n}\right\rbrack \) is zero.

Proof. For otherwise there would be too many linearly independent elements in \( {\Omega }_{n} \) .

[Wal60] has proved the following much sharper statement. The manifold \( {M}^{n} \) itself is an oriented boundary if and only if all Pontrjagin numbers and all Stiefel-Whitney numbers of \( {M}^{n} \) are zero. Thus the cobordism group \( {\Omega }_{n} \) is always the direct sum of a number of copies of \( \mathbb{Z}/2 \) and (if \( n \equiv  0 \) mod 4) a number of copies of \( \mathbb{Z} \) .

We conclude with a problem for the reader.

Problem 18-A. As in the proof of Lemma 18.5, suppose that \( f \) has the origin as regular value throughout a compact set \( {K}^{\prime \prime } \subset  W \subset  {\mathbb{R}}^{m} \) . If \( g \) is uniformly close to \( f \) and the derivatives \( \partial {g}_{i}/\partial {x}_{j} \) are uniformly close to the \( \partial {f}_{i}/\partial {x}_{j} \) , show that \( g \) has the origin as regular value throughout \( {K}^{\prime \prime } \) .
