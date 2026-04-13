# 14.6 The Tangent Bundle of Complex Projective Space

As an application, consider the tangent bundle \( {\tau }^{n} \) of the projective space \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \)

Theorem 14.10. The total Chern class \( \mathrm{c}\left( {\tau }^{n}\right) \) is equal to \( {\left( 1 + a\right) }^{n + 1} \) where a is a suitably chosen generator for the group \( {\mathrm{H}}^{2}\left( {{\mathbb{P}}^{n}\left( \mathbb{C}\right) ;\mathbb{Z}}\right) \) .

In fact we will see that \( a \) is the negative of the generator \( {\mathrm{c}}_{1}\left( {\gamma }^{1}\right) \) which was used in 14.4.

Proof. Let \( {\gamma }^{1} = {\gamma }^{1}\left( {\mathbb{C}}^{n + 1}\right) \) be the canonical line bundle over \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) , and let \( {\omega }^{n} \) be its orthogonal complement, using the standard Hermitian metric on \( {\mathbb{C}}^{n + 1} \) , so that the Whitney sum \( {\gamma }^{1} \oplus  {\omega }^{n} \) is a trivial complex \( \left( {n + 1}\right) \) -plane bundle over \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) . We will show that the complex vector bundle

\[
{\operatorname{Hom}}_{\mathbb{C}}\left( {{\gamma }^{1},{\omega }^{n}}\right)
\]

can be identified with the tangent bundle \( {\tau }^{n} \) of \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) . In fact if \( L \) is a complex line through the origin in \( {\mathbb{C}}^{n + 1} \) , and \( {L}^{ \bot  } \) is its orthogonal complement, then the vector space \( \operatorname{Hom}\left( {L,{L}^{ \bot  }}\right) \) can be identified, complex analytically, with the neighborhood of \( L \) in \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) consisting of all lines \( {L}^{\prime } \) which can be considered as graphs of linear maps from \( L \) to \( {L}^{ \bot  } \) . (Compare pp. 64,78 as well as Lemma 4.4.) It follows easily that the tangent space of \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) at \( L \) can be identified with \( \operatorname{Hom}\left( {L,{L}^{ \bot  }}\right) \) , and hence that \( {\tau }^{n} \cong  \operatorname{Hom}\left( {{\gamma }^{1},{\omega }^{n}}\right) \) .

Now adding the trivial bundle \( {\varepsilon }^{1} \cong  \operatorname{Hom}\left( {{\gamma }^{1},{\gamma }^{1}}\right) \) to both sides of the equation \( {\tau }^{n} \cong  \operatorname{Hom}\left( {{\gamma }^{1},{\omega }^{n}}\right) \) it follows that

\[
{\tau }^{n} \oplus  {\varepsilon }^{1} \cong  \operatorname{Hom}\left( {{\gamma }^{1},{\omega }^{n} \oplus  {\gamma }^{1}}\right)
\]

\[
\cong  \operatorname{Hom}\left( {{\gamma }^{1},{\varepsilon }^{1} \oplus  \ldots  \oplus  {\varepsilon }^{1}}\right) .
\]

Clearly this can be identified with the Whitney sum of \( n + 1 \) copies of the dual bundle \( \operatorname{Hom}\left( {{\gamma }^{1},{\varepsilon }^{1}}\right)  \cong  {\overline{\gamma }}^{1} \) . Thus the total Chern class \( \mathrm{c}\left( {\gamma }^{n}\right)  = \mathrm{c}\left( {{\tau }^{n} \oplus  {\varepsilon }^{1}}\right) \) is equal to

\[
\mathrm{c}{\left( {\overline{\gamma }}^{1}\right) }^{n + 1} = {\left( 1 - {\mathrm{c}}_{1}\left( {\gamma }^{1}\right) \right) }^{n + 1},
\]

using Lemma 14.9. Setting \( a =  - {\mathrm{c}}_{1}\left( {\gamma }^{1}\right) \) , the conclusion follows.

Remark. It follows that the top Chern class \( {\mathrm{c}}_{n}\left( {\tau }^{n}\right) \) is equal to \( \left( {n + 1}\right) {a}^{n} \) . Therefore the Euler number

\[
\mathrm{e}\left\lbrack  {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right\rbrack   = {\mathrm{c}}_{n}\left\lbrack  {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right\rbrack
\]

\[
= \left\langle  {{\mathrm{c}}_{n}\left( {\tau }^{n}\right) ,{\mu }_{2n}}\right\rangle
\]

is equal to \( n + 1 \) multiplied by the sign \( \left\langle  {{a}^{n},{\mu }_{2n}}\right\rangle   =  \pm  1 \) . Here \( {\mu }_{2n} \) denotes the fundamental homology class of \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) . Setting this Euler number equal to

\[
\sum {\left( -1\right) }^{i}\operatorname{rank}{\mathrm{H}}^{i}\left( {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right)  = n + 1
\]

by corollary 11.12, it follows that the sign \( \left\langle  {{a}^{n},{\mu }_{2n}}\right\rangle \) is actually +1 . Thus \( {a}^{n} \) is precisely the generator of \( {\mathrm{H}}^{2n}\left( {{\mathbb{P}}^{n}\left( \mathbb{C}\right) ;\mathbb{Z}}\right) \) which is compatible with the preferred orientation.

Here are some exercises for the reader.

Problem 14-A. Use Lemma 14.9 to give another proof that the tangent bundle of \( {\mathbb{P}}^{1}\left( \mathbb{C}\right) \) is not isomorphic to its conjugate bundle.

Problem 14-B. Using Property 9.5, prove inductively that the coefficient homomorphism \( {\mathrm{H}}^{i}\left( {B;\mathbb{Z}}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {B;\mathbb{Z}/2}\right) \) maps the total Chern class \( \mathrm{c}\left( \omega \right) \) to the total Stiefel-Whitney class \( \mathrm{w}\left( {\omega }_{\mathbb{R}}\right) \) . In particular show that the odd Stiefel-Whitney classes of \( {\omega }_{\mathbb{R}} \) are zero.

Problem 14-C. Let \( {\mathrm{V}}_{n - q}\left( {\mathbb{C}}^{n}\right) \) denote the complex Stiefel manifold consisting of all complex \( \left( {n - q}\right) \) -frames in \( {\mathbb{C}}^{n} \) , where \( 0 \leq  q < n \) . According to [Ste51,§25.7] this manifold is \( {2q} \) -connected, and

\[
{\pi }_{{2q} + 1}{\mathrm{\;V}}_{n - q}\left( {\mathbb{C}}^{n}\right)  \cong  \mathbb{Z}
\]

Given a complex \( n \) -plane bundle \( \omega \) over a CW-complex \( B \) with typical fiber \( F \) , construct an associated bundle \( {\mathrm{V}}_{n - q}\left( \omega \right) \) over \( B \) with typical fiber \( {\mathrm{V}}_{n - q}\left( F\right) \) . Show that the primary obstruction to the existence of a cross-section of \( {\mathrm{V}}_{n - q}\left( \omega \right) \) is a cohomology class in

\[
{\mathrm{H}}^{{2q} + 2}\left( {B;\left\{  {{\pi }_{{2q} + 1}{\mathrm{\;V}}_{n - q}\left( F\right) }\right\}  }\right)
\]

which can be identified with the Chern class \( {\mathrm{c}}_{q + 1}\left( \omega \right) \) .

Problem 14-D. In analogy with \( \text{ § }6 \) , construct a cell subdivision for the complex Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{C}}^{\infty }\right) \) with one cell of dimension \( {2k} \) corresponding to each partition of \( k \) into at most \( n \) integers. Show that the Chern class \( {\mathrm{c}}_{k}\left( {\gamma }^{n}\right) \) corresponds to the cocycle which assigns \( \pm  1 \) to the Schubert cell indexed by the partition \( 1,1,\ldots ,1 \) of \( k \) , and zero to all other cells. (Compare Problem 6-C.)

Problem 14-E. In analogy with the construction of Chern classes, show that it is possible to define the Stiefel-Whitney classes of a real \( n \) -plane bundle inductively by the formula \( {\mathrm{w}}_{i}\left( \xi \right)  = {\pi }_{0}^{* - 1}{\mathrm{w}}_{i}\left( {\xi }_{0}\right) \) for \( i < n \) . Here the top Stiefel-Whitney class \( {\mathrm{w}}_{n}\left( \xi \right) \) must be constructed by the procedure of \( \text{ § }9 \) (Property 9.5), as a mod 2 analogue of the Euler class. [In this approach there is some difficulty in showing that \( {\mathrm{w}}_{n - 1}\left( {\xi }_{0}\right) \) belongs to the image of \( {\pi }_{0}^{ * } \) . It suffices to show that \( {\mathrm{w}}_{n - 1}\left( {\xi }_{0}\right) \) restricts to zero in each fiber \( {F}_{0} \) , or equivalently that the tangent bundle \( \tau \) of the \( \left( {n - 1}\right) \) - sphere satisfies \( {\mathrm{w}}_{n - 1}\left( \tau \right)  = 0 \) . Compare pp. 50. It is at this point that mod 2 coefficients are essential, since \( \mathrm{e}\left( \tau \right)  \neq  0 \) in general.] Using this construction of Stiefel-Whitney classes, verify the axioms of \( \text{ § }4 \) without making any use of Steenrod squares.
