# 18.2 Homotopy Groups Modulo \( {\mathrm{{Ab}}}_{ < \infty } \)

In order to relate homology groups to homotopy groups, we use some results of [Ser53]. Let \( {\mathbf{{Ab}}}_{ < \infty } \) denote the class of all finite abelian groups. A homomorphism \( h : A \rightarrow  B \) between abelian groups is called a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism if both the kernel \( {h}^{-1}\left( 0\right) \) and the cokernel \( B/h\left( A\right) \) belong to \( {\mathbf{{Ab}}}_{ < \infty } \) .

Theorem 18.3. Let \( X \) be a finite complex which is \( \left( {k - 1}\right) \) -connected, \( k \geq  2 \) . Then the Hurewicz homomorphism

\[
{\pi }_{r}\left( X\right)  \rightarrow  {\mathrm{H}}_{r}\left( {X;\mathbb{Z}}\right)
\]

is a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism for \( r < {2k} - 1 \) .

Proof. This Theorem will be established by assembling several results of Serre. First note that the Theorem is true for the special case of a sphere \( {S}^{n}, n \geq  k \) , for the homotopy groups \( {\pi }_{r}\left( {S}^{n}\right) \) are finite for \( r < {2n} - 1, r \neq  n \) . (See for example [Spa81, pp. 515-516].)

Next note that it is true for any finite bouquet of spheres. In fact if the Theorem is true for two \( \left( {k - 1}\right) \) -connected complexes \( X \) and \( Y \) then, using the Künneth theorem, it is certainly true for the product \( X \times  Y \) . Hence, applying the relative Hurewicz theorem to the pair \( \left( {X \times  Y, X \vee  Y}\right) \) , we see that

\[
{\pi }_{r}\left( {X \vee  Y}\right)  \cong  {\pi }_{r}\left( {X \times  Y}\right)  \cong  {\pi }_{r}\left( X\right)  \oplus  {\pi }_{r}\left( Y\right) \;\text{ for }r < {2k} - 1,
\]

and it follows that the theorem is true for \( X \vee  Y \) also.

Finally, consider an arbitrary \( \left( {k - 1}\right) \) -connected finite complex \( X \) . Since the homotopy groups \( {\pi }_{r}\left( X\right) \) are finitely generated [Spa81, pp. 509], we can choose a finite basis for the torsion free part of \( {\pi }_{r}\left( X\right) \) for each \( r < {2k} \) . Represent each basis element by a base point preserving map \( {S}^{{r}_{i}} \rightarrow  X \) , and combine these maps to form a single map

\[
f : {S}^{{r}_{1}} \vee  \ldots  \vee  {S}^{{r}_{p}} \rightarrow  X
\]

Since the Theorem has already been established for this bouquet of spheres, we see easily that \( f \) induces a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism of homotopy groups in dimension less than \( {2k} - 1 \) , and a \( {\mathbf{{Ab}}}_{ < \infty } \) -surjection in dimension \( {2k} - 1 \) . Therefore, by the generalized Whitehead theorem [Spa81, pp. 512], it follows that \( f \) also induces a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism of homology groups in dimensions less than \( {2k} - 1 \) . Thus, since the Theorem is true for the bouquet of spheres, it must also be true for \( X \) .

Alternative Proof. The corresponding statement for cohomotopy groups and cohomology groups is proved in [Ser53], hence the present Theorem follows by Spanier-Whitehead duality [SW55].

Corollary 18.4. If Th is the Thom space of an oriented \( k \) -plane bundle over the finite complex \( B \) , then there is a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism

\[
{\pi }_{n + k}\left( T\right)  \rightarrow  {\mathrm{H}}_{n}\left( {B;\mathbb{Z}}\right)
\]

for all dimensions \( n < k - 1 \) .

Proof. This follows immediately from Lemma 18.2 and 18.3.

Now we must show how to apply this corollary to the computation of cobor-dism groups.
