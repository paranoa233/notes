# Chapter 23 The Bott Periodicity Theorem for the Unitary Group

Based on lecture notes by

M. Spivak and R. Wells

First a review of well known facts concerning the unitary group. Let \( {\mathbb{C}}^{n} \) be the space of \( n \) -tuples of complex numbers, with the usual Hermitian inner product. The unitary group \( \mathrm{U}\left( n\right) \) is defined to be the group of all linear transformations \( S : {\mathbb{C}}^{n} \rightarrow  {\mathbb{C}}^{n} \) which preserve this inner product. Equivalently, using the matrix representation, \( \mathrm{U}\left( n\right) \) is the group of all \( n \times  n \) complex matrices \( S \) such that \( S{S}^{ * } = \mathrm{I} \) ; where \( {S}^{ * } \) denotes the conjugate transpose of \( S \) .

For any \( n \times  n \) complex matrix \( A \) the exponential of \( A \) is defined by the convergent power series expansion

\[
\exp A = \mathrm{I} + A + \frac{1}{2!}{A}^{2} + \frac{1}{3!}{A}^{3} + \cdots .
\]

The following properties are easily verified:

(1) \( \exp \left( {A}^{ * }\right)  = {\left( \exp A\right) }^{ * };\exp \left( {{TA}{T}^{-1}}\right)  = T\left( {\exp A}\right) {T}^{-1} \) .

(2) If \( A \) and \( B \) commute then

\[
\exp \left( {A + B}\right)  = \left( {\exp A}\right) \left( {\exp B}\right) .\;\text{ In particular: }
\]

(3) \( \left( {\exp A}\right) \left( {\exp  - A}\right)  = \mathrm{I} \)

(4) The function exp maps a neighborhood of 0 in the space of \( n \times  n \) matrices diffeomorphically onto a neighborhood of I.

If \( A \) is skew-Hermitian (that is if \( A + {A}^{ * } = 0 \) ), then it follows from ((1)) and ((3)) that \( \exp A \) is unitary. Conversely if \( \exp A \) is unitary, and \( A \) belongs to a sufficiently small neighborhood of 0, then it follows from ((1)), ((3)), and ((4)) that \( A + {A}^{ * } = 0 \) . From these facts one easily proves that:

(5) \( \mathrm{U}\left( n\right) \) is a smooth submanifold of the space of \( n \times  n \) matrices;

(6) the tangent space \( T\mathrm{U}{\left( n\right) }_{\mathrm{I}} \) can be identified with the space of \( n \times  n \) skew-Hermitian matrices.

Therefore the Lie algebra \( \mathfrak{g} \) of \( \mathrm{U}\left( n\right) \) can also be identified with the space of skew-Hermitian matrices. For any tangent vector at I extends uniquely to a left invariant vector field on \( \mathrm{U}\left( n\right) \) . Computation shows that the bracket product of left invariant vector fields corresponds to the product \( \left\lbrack  {A, B}\right\rbrack   = {AB} - {BA} \) of matrices.

Since \( \mathrm{U}\left( n\right) \) is compact, it possesses a left and right invariant Riemannian metric.

Note that the function

\[
\exp  : T\mathrm{U}{\left( n\right) }_{\mathrm{I}} \rightarrow  \mathrm{U}\left( n\right)
\]

defined by exponentiation of matrices coincides with the function exp defined (as in chapter 10) by following geodesics on the resulting Riemannian manifold. In fact for each skew-Hermitian matrix \( A \) the correspondence

\[
t \mapsto  \exp \left( {tA}\right)
\]

defines a 1-parameter subgroup of \( \mathrm{U}\left( n\right) \) (by Assertion (2) above); and hence defines a geodesic.

A specific Riemannian metric on \( \mathrm{U}\left( n\right) \) can be defined as follows. Given matrices \( A, B \in  \mathfrak{g} \) let \( \langle A, B\rangle \) denote the real part of the complex number

\[
\operatorname{tr}\left( {A{B}^{ * }}\right)  = \mathop{\sum }\limits_{{i, j}}{A}_{ij}{\bar{B}}_{ij}.
\]

Clearly this inner product is positive definite on \( \mathfrak{g} \) .

This inner product on \( \mathfrak{g} \) determines a unique left invariant Riemannian metric on \( \mathrm{U}\left( n\right) \) . To verify that the resulting metric is also right invariant, we must check that it is invariant under the adjoint action of \( \mathrm{U}\left( n\right) \) on \( \mathfrak{g} \) .

DEFINITION OF THE ADJOINT ACTION. Each \( S \in  \mathrm{U}\left( n\right) \) determines an inner automorphism

\[
X \mapsto  {SX}{S}^{-1} = \left( {{L}_{S}{R}_{{S}^{-1}}}\right) X
\]

of the group \( \mathrm{U}\left( n\right) \) . The induced linear mapping

\[
{\left( {L}_{S}{R}_{{S}^{-1}}\right) }_{ * } : T\mathrm{\;U}{\left( n\right) }_{\mathrm{I}} \rightarrow  T\mathrm{\;U}{\left( n\right) }_{\mathrm{I}}
\]

is called \( \operatorname{Ad}\left( S\right) \) . Thus \( \operatorname{Ad}\left( S\right) \) is an automorphism of the Lie algebra of \( \mathrm{U}\left( n\right) \) . Using Assertion (1) above we obtain the explicit formula

\[
\operatorname{Ad}\left( S\right) A = {SA}{S}^{-1},
\]

for \( A \in  \mathfrak{g}, S \in  \mathrm{U}\left( n\right) \) .

The inner product \( \langle A, B\rangle \) is invariant under each such automorphism \( \operatorname{Ad}\left( S\right) \) . In fact if \( {A}_{1} = \operatorname{Ad}\left( S\right) A,{B}_{1} = \operatorname{Ad}\left( S\right) B \) then the identity

\[
{A}_{1}{B}_{1}^{ * } = {SA}{S}^{-1}{\left( SB{S}^{-1}\right) }^{ * } = {SA}{B}^{ * }{S}^{-1}
\]

implies that

\[
\operatorname{tr}\left( {{A}_{1}{B}_{1}^{ * }}\right)  = \operatorname{tr}\left( {{SA}{B}^{ * }{S}^{-1}}\right)  = \operatorname{tr}\left( {A{B}^{ * }}\right) ;
\]

and hence that

\[
\left\langle  {{A}_{1},{B}_{1}}\right\rangle   = \langle A, B\rangle
\]

It follows that the corresponding left invariant metric on \( \mathrm{U}\left( n\right) \) is also right invariant.

Given \( A \in  \mathfrak{g} \) we know by ordinary matrix theory that there exists \( T \in  \mathrm{U}\left( n\right) \) so that \( {TA}{T}^{-1} \) is in diagonal form

\[
{TA}{T}^{-1} = \left( \begin{array}{llll} i{a}_{1} & & & \\   & i{a}_{2} & & \\   & &  \ddots  & \\   & & & i{a}_{n} \end{array}\right)
\]

where the \( {a}_{i} \) ’s are real. Also, given any \( S \in  \mathrm{U}\left( n\right) \) , there is a \( T \in  \mathrm{U}\left( n\right) \) such that

\[
{TS}{T}^{-1} = \left( \begin{array}{lll} {e}^{i{a}_{1}} & & \\   &  \ddots  & \\   & & {e}^{i{a}_{n}} \end{array}\right)
\]

where again the \( {a}_{i} \) ’s are real. Thus we see directly that \( \exp  : \mathfrak{g} \rightarrow  \mathrm{U}\left( n\right) \) is onto.

One may treat the special unitary group \( \mathrm{{SU}}\left( n\right) \) in the same way. \( \mathrm{{SU}}\left( n\right) \) is defined as the subgroup of \( \mathrm{U}\left( n\right) \) consisting of matrices of determinant 1 . If exp is regarded as the ordinary exponential map of matrices, it is easy to show, using the diagonal form, that

\[
\det \left( {\exp A}\right)  = {e}^{\operatorname{tr}A}.
\]

Using this equation, one may show that \( {\mathfrak{g}}^{\prime } \) , the Lie algebra of \( \mathrm{{SU}}\left( n\right) \) is the set of all matrices \( A \) such that \( A + {A}^{ * } = 0 \) and \( \operatorname{tr}A = 0 \) .

In order to apply Morse theory to the topology of \( \mathrm{U}\left( n\right) \) and \( \mathrm{{SU}}\left( n\right) \) , we begin by considering the set of all geodesics in \( \mathrm{U}\left( n\right) \) from I to \( - \mathrm{I} \) . In other words, we look for all \( A \in  T\mathrm{U}{\left( n\right) }_{\mathrm{I}} = \mathfrak{g} \) such that \( \exp A =  - \mathrm{I} \) . Suppose \( A \) is such a matrix; if it is not already in diagonal form, let \( T \in  \mathrm{U}\left( n\right) \) be such that \( {TA}{T}^{-1} \) is in diagonal form. Then

\[
\exp {TA}{T}^{-1} = T\left( {\exp A}\right) {T}^{-1} = T\left( {-\mathrm{I}}\right) {T}^{-1} =  - \mathrm{I}
\]

so that we may as well assume that \( A \) is already in diagonal form

\[
A = \left( \begin{array}{lll} i{a}_{1} & & \\   &  \ddots  & \\   & & i{a}_{n} \end{array}\right)
\]

In this case,

\[
\exp A = \left( \begin{array}{lll} {e}^{i{a}_{1}} & & \\   &  \ddots  & \\   & & {e}^{i{a}_{n}} \end{array}\right)
\]

so that \( \exp A =  - \mathrm{I} \) if and only if \( A \) has the form

\[
\left( \begin{array}{lll} {k}_{1}^{i\pi } & & \\   &  \ddots  & \\   & & {k}_{n}^{i\pi } \end{array}\right)
\]

for some odd integers \( {k}_{1},\ldots ,{k}_{n} \) .

Since the length of the geodesic \( t \mapsto  \exp {tA} \) to from \( t = 0 \) to \( t = 1 \) is \( \left| A\right|  = \; \sqrt{\operatorname{tr}A{A}^{ * }} \) , the length of the geodesic determined by \( A \) is it \( \pi \sqrt{{k}_{1}^{2} + \cdots  + {k}_{n}^{2}} \) . Thus \( A \) determines a minimal geodesic if and only if each \( {k}_{i} \) equals \( \pm  1 \) , and in that case, the length is \( \pi \sqrt{n} \) . Now, regarding such an \( A \) as a linear map of \( {\mathbb{C}}^{n} \) to \( {\mathbb{C}}^{n} \) observe that \( A \) is completely determined by specifying Eigen \( \left( {i\pi }\right) \) , the vector space consisting of all \( v \in  {\mathbb{C}}^{n} \) such that \( {Av} = {i\pi v} \) ; and Eigen \( \left( {-{i\pi }}\right) \) , the space of all \( v \in  {\mathbb{C}}^{n} \) such that \( {Av} =  - {i\pi v} \) . Since \( {\mathbb{C}}^{n} \) splits as the orthogonal sum Eigen \( \left( {i\pi }\right)  \oplus  \operatorname{Eigen}\left( {-{i\pi }}\right) \) , the matrix \( A \) is then completely determined by Eigen \( \left( {i\pi }\right) \) , which is an arbitrary subspace of \( {\mathbb{C}}^{n} \) . Thus the space of all minimal geodesics in \( \mathrm{U}\left( n\right) \) from I to -I may be identified with the space of all sub-vector-spaces of \( {\mathbb{C}}^{n} \) .

Unfortunately, this space is rather inconvenient to use since it has components of varying dimensions. This difficulty may be removed by replacing \( \mathrm{U}\left( n\right) \) by \( \mathrm{{SU}}\left( n\right) \) and setting \( n = {2m} \) . In this case, all the above considerations remain valid. But the additional condition that \( {a}_{1} + \cdots  + {a}_{2m} = 0 \) with \( {a}_{i} =  \pm  \pi \) restricts Eigen \( \left( {i\pi }\right) \) to being an arbitrary \( m \) dimensional sub-vector-space of \( {\mathbb{C}}^{2m} \) . This proves the following:

Lemma 23.1. The space of minimal geodesics from I to -I in the special unitary group \( \mathrm{{SU}}\left( {2m}\right) \) is homeomorphic to the complex Grassmann manifold \( {G}_{m}\left( {\mathbb{C}}^{2m}\right) \) , consisting of all \( m \) dimensional vector subspaces of \( {\mathbb{C}}^{2m} \) .

We will prove the following result at the end of this section.

Lemma 23.2. Every non-minimal geodesic from I to \( - \mathrm{I} \) in \( \mathrm{{SU}}\left( {2m}\right) \) has index \( \geq  {2m} + 2 \) .

Combining these two lemmas with chapter 22 we obtain:

Theorem 23.3 (Bott). The inclusion map \( {G}_{m}\left( {\mathbb{C}}^{2m}\right)  \hookrightarrow  \Omega \left( {\mathrm{{SU}}\left( {2m}\right) ;\mathrm{I}, - \mathrm{I}}\right) \) induces isomorphisms of homotopy groups in dimensions \( \leq  {2m} \) . Hence

\[
{\pi }_{i}{G}_{m}\left( {\mathbb{C}}^{2m}\right)  \cong  {\pi }_{i + 1}\mathrm{{SU}}\left( {2m}\right)
\]

for \( i \leq  {2m} \) .

On the other hand using standard methods of homotopy theory one obtains somewhat different isomorphisms.

Lemma 23.4. The group \( {\pi }_{i}{G}_{m}\left( {\mathbb{C}}^{2m}\right) \) is isomorphic to \( {\pi }_{i - 1}\mathrm{U}\left( m\right) \) for \( i \leq  {2m} \) . Furthermore,

\[
{\pi }_{i - 1}\mathrm{\;U}\left( m\right)  \cong  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 1}\right)  \cong  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 2}\right)  \cong  \ldots
\]

for \( i \leq  {2m} \) ; and

\[
{\pi }_{j}\mathrm{U}\left( m\right)  \cong  {\pi }_{j}\mathrm{{SU}}\left( m\right)
\]

for \( j \neq  1 \) .

Proof. First note that for each \( m \) there exists a fibration

\[
\mathrm{U}\left( m\right)  \rightarrow  \mathrm{U}\left( {m + 1}\right)  \rightarrow  {\mathbb{S}}^{{2m} + 1}
\]

From the homotopy exact sequence

\[
\ldots  \rightarrow  {\pi }_{i}{\mathbb{S}}^{{2m} + 1} \rightarrow  {\pi }_{i - 1}\mathrm{\;U}\left( m\right)  \rightarrow  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 1}\right)  \rightarrow  {\pi }_{i - 1}{\mathbb{S}}^{{2m} + 1} \rightarrow  \ldots
\]

of this fibration we see that

\[
{\pi }_{i - 1}\mathrm{\;U}\left( m\right)  \cong  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 1}\right)
\]

(Compare [Ste51, p. 35 and p. 90].) It follows that the inclusion homomorphisms

\[
{\pi }_{i - 1}\mathrm{\;U}\left( m\right)  \rightarrow  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 1}\right)  \rightarrow  {\pi }_{i - 1}\mathrm{\;U}\left( {m + 2}\right)  \rightarrow  \ldots
\]

are all isomorphisms for \( i \leq  {2m} \) . These mutually isomorphic groups are called the \( \left( {i - 1}\right) \) -st stable homotopy group of the unitary group. They will be denoted briefly by \( {\pi }_{i - 1}\mathrm{U} \) .

The same exact sequence shows that, for \( i = {2m} + 1 \) , the homomorphism \( {\pi }_{2m}\mathrm{\;U}\left( m\right)  \cong  {\pi }_{2m}\mathrm{\;U}\left( {m + 1}\right)  \cong  {\pi }_{2m}\mathrm{\;U} \) is onto.

The complex Stiefel manifold is defined to be the coset space \( \mathrm{U}\left( {2m}\right) /\mathrm{U}\left( m\right) \) . From the exact sequence of the fibration

\[
\mathrm{U}\left( m\right)  \rightarrow  \mathrm{U}\left( {2m}\right)  \rightarrow  \mathrm{U}\left( {2m}\right) /\mathrm{U}\left( m\right)
\]

we see that \( {\pi }_{i}\left( {\mathrm{\;U}\left( {2m}\right) /\mathrm{U}\left( m\right) }\right)  = 0 \) for \( i \leq  {2m} \) .

The complex Grassmann manifold \( {G}_{m}\left( {\mathbb{C}}^{2m}\right) \) can be identified with the coset space \( \mathrm{U}\left( {2m}\right) /\mathrm{U}\left( m\right)  \times  \mathrm{U}\left( m\right) \) . (Compare Steenrod §7.) From the exact sequence of the fibration

\[
\mathrm{U}\left( m\right)  \rightarrow  \mathrm{U}\left( {2m}\right) /\mathrm{U}\left( m\right)  \rightarrow  {G}_{m}\left( {\mathbb{C}}^{2m}\right)
\]

we see now that

\[
{\pi }_{i}{G}_{m}\left( {\mathbb{C}}^{2m}\right) \overset{ \cong  }{ \rightarrow  }{\pi }_{i - 1}\mathrm{U}\left( m\right)
\]

for \( i \leq  {2m} \) .

Finally, from the exact sequence of the fibration \( \mathrm{{SU}}\left( m\right)  \rightarrow  \mathrm{U}\left( m\right)  \rightarrow  {\mathbb{S}}^{1} \) we see that \( {\pi }_{j}\mathrm{{SU}}\left( m\right)  \cong  {\pi }_{j}\mathrm{U}\left( m\right) \) for \( j \neq  1 \) . This completes the proof of Lemma 23.4.

Combining Lemma 23.4 with Theorem 23.3 we see that

\[
{\pi }_{i - 1}\mathrm{U} = {\pi }_{i - 1}\mathrm{U}\left( m\right)  \cong  {\pi }_{i}{G}_{m}\left( {\mathbb{C}}^{2m}\right)  \cong  {\pi }_{i + 1}\mathrm{{SU}}\left( {2m}\right)  \cong  {\pi }_{i + 1}\mathrm{U}
\]

for \( 1 \leq  i \leq  {2m} \) . Thus we obtain:

Periodicity Theorem. \( {\pi }_{i - 1}U \cong  {\pi }_{i + 1}U \) for \( i \geq  1 \) .

To evaluate these groups it is now sufficient to observe that \( U\left( 1\right) \) is a circle; so that

\[
{\pi }_{0}\mathrm{U} = {\pi }_{0}\mathrm{U}\left( 1\right)  = 0
\]

\[
{\pi }_{1}\mathrm{U} = {\pi }_{1}\mathrm{U}\left( 1\right)  \cong  \mathbb{Z}\;\text{ (infinite cyclic). }
\]

As a check, since \( \mathrm{{SU}}\left( 2\right) \) is a 3 -sphere, we have:

\[
{\pi }_{2}\mathrm{{SU}} = {\pi }_{2}\mathrm{{SU}}\left( 2\right)  = 0
\]

\[
{\pi }_{3}\mathrm{{SU}} = {\pi }_{3}\mathrm{{SU}}\left( 2\right)  \cong  \mathbb{Z}\;\text{ (infinite cyclic). }
\]

Thus we have proved the following result.

Theorem 23.5 (Bott). The stable homotopy groups \( {\pi }_{i} \cup \) of the unitary groups are periodic with period 2. In fact the groups

\[
{\pi }_{0}\mathrm{U} \cong  {\pi }_{2}\mathrm{U} \cong  {\pi }_{4}\mathrm{U} \cong  \ldots
\]

are zero, and the groups

\[
{\pi }_{1}\mathrm{U} \cong  {\pi }_{3}\mathrm{U} \cong  {\pi }_{5}\mathrm{U} \cong  \ldots
\]

are infinite cyclic.

The rest of chapter 23 will be concerned with the proof of Lemma 23.2. We must compute the index of any non-minimal geodesic from I to-I on \( \mathrm{{SU}}\left( n\right) \) , where \( n \) is even. Recall that the Lie algebra

\[
{\mathfrak{g}}^{\prime } = T{\left( \mathrm{{SU}}\left( n\right) \right) }_{i}d
\]

consists of all \( n \times  n \) skew-Hermitian matrices with trace zero. A given matrix \( A \in  {\mathfrak{g}}^{\prime } \) corresponds to a geodesic from I to -I if and only if the eigenvalues of \( A \) have the form \( {i\pi }{k}_{1},\ldots ,{i\pi }{k}_{n} \) where \( {k}_{1},\ldots ,{k}_{n} \) are odd integers with sum zero.

We must find the conjugate points to I along the geodesic

\[
t \mapsto  \exp \left( {tA}\right)
\]

According to Theorem 20.5 these will be determined by the positive eigenvalues of the linear transformation

\[
{K}_{A} : {\mathfrak{g}}^{\prime } \rightarrow  {\mathfrak{g}}^{\prime }
\]

where

\[
{K}_{A}\left( W\right)  = \mathcal{R}\left( {A, W}\right) A = \frac{1}{4}\left\lbrack  {\left\lbrack  {A, W}\right\rbrack  , A}\right\rbrack  .
\]

(Compare Theorem 21.7.)

We may assume that \( A \) is the diagonal matrix

\[
\left( \begin{array}{lll} {i\pi }{k}_{1} & & \\   &  \ddots  & \\   & & {i\pi }{k}_{n} \end{array}\right)
\]

with \( {k}_{1} \geq  {k}_{2} \geq  \ldots  \geq  {k}_{n} \) . If \( W = \left( {w}_{j\ell }\right) \) then a short computation shows that

\[
\left\lbrack  {A, W}\right\rbrack   = \left( {{i\pi }\left( {{k}_{j} - {k}_{\ell }}\right) {w}_{j\ell }}\right) ,
\]

hence

\[
\left\lbrack  {A,\left\lbrack  {A, W}\right\rbrack  }\right\rbrack   = \left( {-{\pi }^{2}\left( {{k}_{j} - {k}_{\ell }}\right) {w}_{j\ell }}\right) ,
\]

and

\[
{K}_{A}\left( W\right)  = \left( {\frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2}{w}_{j\ell }}\right) .
\]

Now we find a basis for \( {\mathfrak{g}}^{\prime } \) consisting of eigenvectors of \( {K}_{A} \) , as follows:

(1) For each \( j < \ell \) the matrix \( {E}_{j\ell } \) , with +1 in the \( \left( {j\ell }\right) \) -th place,-1 in the \( \left( {\ell j}\right) \) - th place and zeros elsewhere, is in \( {\mathfrak{g}}^{\prime } \) and is an eigenvector corresponding to the eigenvalue \( \frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2} \) .

(2) Similarly For each \( j < \ell \) the matrix \( {E}_{j\ell }^{\prime } \) , with \( + i \) in the \( \left( {j\ell }\right) \) -th place, \( + i \) in the \( \left( {\ell j}\right) \) -th place is an eigenvector, also with eigenvalue \( \frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2} \) .

(3) Each diagonal matrix in \( {\mathfrak{g}}^{\prime } \) is an eigenvector with eigenvalue 0 .

Thus the non-zero eigenvalues of \( {K}_{A} \) are the numbers \( \frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2} \) with \( {k}_{j} > {k}_{\ell } \) . Each such eigenvalue is to be counted twice.

Now consider the geodesic \( \gamma \left( t\right)  = \exp {tA} \) . Each eigenvalue \( e = \frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2} > 0 \) gives rise to a series of conjugate points along \( \gamma \) corresponding to the values

\[
t = \pi /\sqrt{e},{2\pi }/\sqrt{e},{3\pi }/\sqrt{e},\ldots
\]

(See Theorem 20.5.) Substituting in the formula for \( e \) , this gives

\[
t = \frac{2}{{k}_{j} - {k}_{\ell }},\frac{4}{{k}_{j} - {k}_{\ell }},\frac{6}{{k}_{j} - {k}_{\ell }},\ldots
\]

The number of such values of \( t \) in the open interval \( \left( {0,1}\right) \) is evidently equal to \( \frac{{k}_{j} - {k}_{\ell }}{2} - 1 \)

Now let us apply the Index Theorem. For each \( j,\ell \) with \( {k}_{j} > {k}_{\ell } \) we obtain two copies of the eigenvalue \( \frac{{\pi }^{2}}{4}{\left( {k}_{j} - {k}_{\ell }\right) }^{2} \) , and hence a contribution of

\[
2\left( {\frac{{k}_{j} - {k}_{\ell }}{2} - 1}\right)
\]

to the index. Adding over all \( j,\ell \) this gives the formula

\[
\lambda  = \mathop{\sum }\limits_{{{k}_{j} > {k}_{\ell }}}\left( {{k}_{j} - {k}_{\ell } - 2}\right)
\]

for the index of the geodesic \( \gamma \) .

As an example, if \( \gamma \) is a minimal geodesic, then all of the \( {k}_{j} \) are equal to \( \pm  1 \) . Hence \( \lambda  = 0 \) , as was to be expected.

Now consider a non-minimal geodesic. Let \( n = {2m} \) .

Case 1. At least \( m + 1 \) of the \( {k}_{i} \) ’s are (say) negative. In this case at least one of the positive ki must be \( \geq  3 \) , and we have

\[
\lambda  \geq  \mathop{\sum }\limits_{1}^{{m + 1}}\left( {3 - \left( {-1}\right)  - 2}\right)  = 2\left( {m + 1}\right) .
\]

Case 2. \( m \) of the \( {k}_{i} \) are positive and \( m \) are negative but not all are \( \pm  1 \) . Then one is \( \geq  3 \) and one is \( \leq   - 3 \) so that

\[
\lambda  \geq  \mathop{\sum }\limits_{1}^{{m - 1}}\left( {3 - \left( {-1}\right)  - 2}\right)  + \mathop{\sum }\limits_{1}^{{m - 1}}\left( {1 - \left( {-3}\right)  - 2}\right)  + \left( {3 - \left( {-3}\right)  - 2}\right)
\]

\[
= {4m} \geq  2\left( {m + 1}\right) \text{ . }
\]

Thus in either case we have \( \lambda  \geq  {2m} + 2 \) . This proves Lemma 23.2, and therefore completes the proof of the Theorem 23.3.
