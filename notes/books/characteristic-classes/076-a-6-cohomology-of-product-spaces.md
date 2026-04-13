# A.6 Cohomology of Product Spaces

Let \( {\mathbb{R}}_{0}^{n} \) denote the complement of the origin in \( {\mathbb{R}}^{n} \) . For any space \( X \) , we will prove that

\[
{\mathrm{H}}^{m}X \cong  {\mathrm{H}}^{m + n}\left( {X \times  {\mathbb{R}}^{n}, X \times  {\mathbb{R}}_{0}^{n}}\right) .
\]

This isomorphism can best be described by introducing the cohomology cross product operation. Suppose that one is given cohomology classes

\[
a \in  {\mathrm{H}}^{m}\left( {X, A}\right) , b \in  {\mathrm{H}}^{n}\left( {Y, B}\right)
\]

where \( A \) is an open subset of \( X \) and \( B \) is an open subset of \( Y \) . (If \( B \) is vacuous then \( A \) need not be open, and conversely.) Using the projection maps

\[
{p}_{1} : \left( {X \times  Y, A \times  Y}\right)  \rightarrow  \left( {X, A}\right)
\]

\[
{p}_{2} : \left( {X \times  Y, X \times  B}\right)  \rightarrow  \left( {Y, B}\right)
\]

the cross product (or external product) \( a \times  b \) is defined to be cohomology class

\[
\left( {{p}_{1}^{ * }a}\right) \left( {{p}_{2}^{ * }b}\right)  \in  {\mathrm{H}}^{m + n}\left( {X \times  Y,\left( {A \times  Y}\right)  \cup  \left( {X \times  B}\right) }\right) .
\]

It will sometimes be convenient to use the abbreviation \( \left( {X, A}\right)  \times  \left( {Y, B}\right) \) for the pair \( \left( {X \times  Y,\left( {A \times  Y}\right)  \cup  \left( {X \times  B}\right) }\right) \) . As an example of this notation, note that the pair \( \left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n}}\right) \) can be described as the \( n \) -fold product \( \left( {\mathbb{R},{\mathbb{R}}_{0}}\right)  \times  \cdots \left( {\mathbb{R},{\mathbb{R}}_{0}}\right) \) .

We will choose a specific generator \( {e}^{n} \) for the free module \( {\mathrm{H}}^{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n}}\right) \) , as follows. Note that \( {\mathbb{R}}_{0} = \mathbb{R} - 0 \) can be expressed as a disjoint union \( {\mathbb{R}}_{ - } \sqcup  {\mathbb{R}}_{ + } \) . Let \( e \in  {\mathrm{H}}^{1}\left( {\mathbb{R},{\mathbb{R}}_{0}}\right) \) correspond to the identity \( 1 \in  {\mathrm{H}}^{0}{\mathbb{R}}_{ + } \) under the excision and coboundary isomorphisms

\[
{\mathrm{H}}^{0}{\mathbb{R}}_{ + }\overset{ \cong  }{ \leftarrow  }{\mathrm{H}}^{0}\left( {{\mathbb{R}}_{0},{\mathbb{R}}_{ - }}\right) \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{1}\left( {\mathbb{R},{\mathbb{R}}_{0}}\right) ,
\]

where \( \delta \) arises from the exact sequence of the triple \( \left( {\mathbb{R},{\mathbb{R}}_{0},{\mathbb{R}}_{ - }}\right) \) . Finally let \( {e}^{n} \in  {\mathrm{H}}^{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n}}\right) \) denote the \( n \) -fold cross product \( e \times  \cdots  \times  e \) .

Theorem A.5. For any pair \( \left( {X, A}\right) \) with \( A \) open in \( X \) , the correspondence \( a \mapsto  a \times  {e}^{n} \) defines an isomorphism

\[
{\mathrm{H}}^{m}\left( {X, A}\right)  \rightarrow  {\mathrm{H}}^{m + n}\left( {\left( {X, A}\right)  \times  \left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n}}\right) }\right)
\]

Proof. First note that it is sufficient to consider the case \( n = 1 \) . The general case will then follow by induction, using the associative law

\[
a \times  {e}^{n} = \left( {a \times  {e}^{n - 1}}\right)  \times  e.
\]

Case 1. Suppose that \( n = 1 \) and that \( A \) is vacuous. For fixed \( a \in  {\mathrm{H}}^{m}X \) , one has the diagram

![bo_d7du9galb0pc73deir9g_271_406_849_1029_131_0.jpg](images/bo_d7du9galb0pc73deir9g_271_406_849_1029_131_0.jpg)

\( {\mathrm{H}}^{m}X \cong  {\mathrm{H}}^{m}\left( {X \times  {\mathbb{R}}_{ + }}\right) \overset{{i}^{ * }}{ \leftarrow  }{\mathrm{H}}^{m}\left( {X \times  {\mathbb{R}}_{0}, X \times  {\mathbb{R}}_{ - }}\right) \overset{{\delta }^{\prime }}{ \rightarrow  }{\mathrm{H}}^{m + 1}\left( {X \times  \mathbb{R}, X \times  {\mathbb{R}}_{0}}\right) \)

which commutes up to sign. The homomorphism \( {i}^{ * } \) is an excision isomorphism, while \( {\delta }^{\prime } \) is taken from the cohomology exact sequence of the triple \( \left( {X \times  \mathbb{R}, X \times  {\mathbb{R}}_{0}, X \times  {\mathbb{R}}_{ - }}\right) \) . It is an isomorphism since both \( X \times  \mathbb{R} \) and \( X \times  {\mathbb{R}}_{ - } \) contain the set \( X \times \) (constant) as deformation retract.

Following the diagram around, we see that \( a \times  e \in  {\mathrm{H}}^{m + 1}\left( {X \times  \mathbb{R}, X \times  {\mathbb{R}}_{0}}\right) \) is the image of \( a \in  {\mathrm{H}}^{m}X \) under a sequence of isomorphisms. This proves Case 1.

Case 2. Suppose that \( n = 1 \) but that \( A \) is non-vacuous. Let \( z \in  {Z}^{1}\left( {\mathbb{R},{\mathbb{R}}_{0}}\right) \) be a cocycle which represents the cohomology class \( e \) . Consider the following commutative diagram

![bo_d7du9galb0pc73deir9g_271_304_1559_1252_151_0.jpg](images/bo_d7du9galb0pc73deir9g_271_304_1559_1252_151_0.jpg)

A straightforward argument shows that the horizontal sequences are exact. Furthermore all of these homomorphisms commute with the coboundary operation:

\[
\delta \left( {a \times  z}\right)  = \left( {\delta a}\right)  \times  z.
\]

Hence there is a corresponding commutative diagram of cohomology groups

![bo_d7du9galb0pc73deir9g_272_196_385_1231_153_0.jpg](images/bo_d7du9galb0pc73deir9g_272_196_385_1231_153_0.jpg)

(See for example [Spa81, p. 182].) By Case 1, the two right hand vertical arrows are isomorphisms. Hence, by the Five Lemma, the left hand vertical arrow is an isomorphism also.

Thus we have proved Theorem A. 5 for the special case \( n = 1 \) . As remarked at the beginning of the proof, this implies that the Theorem holds for all \( n \) .

Now consider two spaces \( X \) and \( Y \) . The cross product operation gives rise to a homomorphism

\[
\times   : {\bigoplus }_{i + j = n}{\mathrm{H}}^{i}X \otimes  {\mathrm{H}}^{j}Y \rightarrow  {\mathrm{H}}^{n}\left( {X \times  Y}\right) .
\]

We would like to prove that \( \times \) is an isomorphism, but this is not true in complete generality. It is false for example if \( X \) and \( Y \) are real projective planes (using integer coefficients), or if \( X \) and \( Y \) are infinite discrete speaces (using arbitrary coefficients).

Theorem A.6. Let \( X \) and \( Y \) be CW-complexes such that each \( {\mathrm{H}}^{i}X \) is a torsion free \( \Lambda \) -module \( {}^{6} \) and such that \( Y \) has only finitely many cells in each dimension. Then the direct sum \( \bigoplus {\mathrm{H}}^{i}X \otimes  {\mathrm{H}}^{j}Y \) maps isomorphically onto \( {\mathrm{H}}^{n}\left( {X \times  Y}\right) \) . \( i + j = n \)

A similar result can be proved for pairs \( \left( {X, A}\right) \) and \( \left( {Y, B}\right) \) . Results of this type are known as "Künneth Theorems", since the prototype was proved by H. Künneth in 1923. For a sharper version, see [Spa81, p. 247].

Proof. First suppose that \( Y \) is finite CW-complex. Then A. 6 will be proved by induction on the number of cells of \( Y \) . Certainly it is true if \( Y \) consists of a single point.

---

\( {}^{6}\mathrm{{Of}} \) course this hypothesis is automatically satisfied if \( \Lambda \) is a field. The assumption that \( X \) is a CW-complex is not actually necessary, but will serve to simplify the proof.

---

Let \( E \) be an open cell of highest dimension and let \( {Y}_{1} = Y - E \) . Assume inductively that

\[
{ \times  }^{\prime } = {\bigoplus }_{i + j = n}{\mathrm{H}}^{i}X \otimes  {\mathrm{H}}^{j}{Y}_{1} \rightarrow  {\mathrm{H}}^{n}\left( {X \times  {Y}_{1}}\right)
\]

is an isomorphism. Consider the following diagram, which commutes up to sign

![bo_d7du9galb0pc73deir9g_273_299_642_1178_179_0.jpg](images/bo_d7du9galb0pc73deir9g_273_299_642_1178_179_0.jpg)

Here the top line is obtained from the exact sequence of the pair \( \left( {Y, Y - 1}\right) \) by tensoring with \( {\mathrm{H}}^{i}X \) , and then forming the direct sum over all \( i, j \) with \( i + j = n \) . The remains an exact sequence since \( {\mathrm{H}}^{i}X \) is torsion free. (Compare [Mac75, p. 152], [CE56, p. 133].)

We have assumed that \( { \times  }^{\prime } \) is an isomorphism. Using Theorem A. 5 together with the isomorphisms

\[
{\mathrm{H}}^{j}\left( {Y,{Y}_{1}}\right)  \leftarrow  {\mathrm{H}}^{j}\left( {Y, Y - \text{ point }}\right)  \leftarrow  {\mathrm{H}}^{j}\left( {E, E - \text{ point }}\right)
\]

and

\[
{\mathrm{H}}^{n}\left( {X \times  Y, X \times  {Y}_{1}}\right)  \leftarrow  {\mathrm{H}}^{n}\left( {X \times  Y, X \times  \left( {Y - \text{ point }}\right) }\right)  \rightarrow  {\mathrm{H}}^{n}\left( {X \times  E, X \times  \left( {E - \text{ point }}\right) }\right)
\]

we see that \( { \times  }^{\prime \prime } \) is also an isomorphism. Therefore, by the Five Lemma, \( \times \) is an isomorphism. This completes the proof, providing that \( Y \) is finite. (We have not yet used the hypothesis that \( X \) is a CW-complex.)

If \( Y \) is infinite but each skeleton \( {Y}^{r} \) is finite, then the above argument applies to \( X \times  {Y}^{r} \) . But it follows easily from Corollary A. 3 that the inclusions

\[
{Y}^{r} \rightarrow  Y, X \times  {Y}^{r} \rightarrow  X \times  Y
\]

induce isomorphism of cohomology in dimension of less than \( r \) . Thus A. 6 is true for \( n < r \) . Since \( r \) can be arbitrarily large this completes the proof.
