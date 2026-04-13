# Chapter 24 The Periodicity Theorem for the Orthogonal Group

Based on lecture notes by

M. Spivak and R. Wells

This section will carry out an analogous study of the iterated loop space of the orthogonal group. However the treatment is rather sketchy, and many details are left out. The point of view in this section was suggested by the paper Clifford modules by M. Atiyah, R. Bott, and A. Shapiro, which relates the periodicity theorem with the structure of certain Clifford algebras. (See [ABS64].)

Consider the vector space \( {\mathbf{R}}^{n} \) with the usual inner product. The orthogonal group \( \mathrm{O}\left( n\right) \) consists of all linear maps

\[
T : {\mathbf{R}}^{n} \rightarrow  {\mathbf{R}}^{n}
\]

which preserve this inner product. Alternatively \( \mathrm{O}\left( n\right) \) consists of all real \( n \times  n \) matrices \( T \) such that \( T{T}^{ * } = \mathrm{I} \) . This group \( \mathrm{O}\left( n\right) \) can be considered as a smooth subgroup of the unitary group \( \mathrm{U}\left( n\right) \) ; and therefore inherits a right and left invariant Riemannian metric.

Now suppose that \( n \) is even.

Definition 24.1. A complex structure \( \mathrm{J} \) on \( {\mathbf{R}}^{n} \) is a linear transformation \( \mathrm{J} : {\mathbf{R}}^{n} \rightarrow \; {\mathbf{R}}^{n} \) belonging to the orthogonal group, which satisfies the identity \( {\mathrm{J}}^{2} =  - \mathrm{I} \) . The space consisting of all such complex structures on \( {\mathbf{R}}^{n} \) will be denoted by \( {\Omega }_{1}\left( n\right) \) .

We will see presently (Lemma 24.6) that \( {\Omega }_{1}\left( n\right) \) is a smooth submanifold of the orthogonal group \( \mathrm{O}\left( n\right) \) .

Remark. Given some fixed \( {\mathrm{J}}_{1} \in  {\Omega }_{1}\left( n\right) \) let \( \mathrm{U}\left( {n/2}\right) \) be the subgroup of \( \mathrm{O}\left( n\right) \) consisting of all orthogonal transformations which commute with \( {\mathrm{J}}_{1} \) . Then \( {\Omega }_{1}\left( n\right) \) can be identified with the quotient space \( \mathrm{O}\left( n\right) /\mathrm{U}\left( {n/2}\right) \) .

Lemma 24.2. The space of minimal geodesics from I to \( - \mathrm{I} \) on \( \mathrm{O}\left( n\right) \) is homeomorphic to the space \( {\Omega }_{1}\left( n\right) \) of complex structures on \( {\mathbf{R}}^{n} \) .

Proof. The space \( \mathrm{O}\left( n\right) \) can be identified with the group of \( n \times  n \) orthogonal matrices. Its tangent space \( \mathfrak{g} = T\mathrm{O}{\left( n\right) }_{\mathrm{I}} \) can be identified with the space of \( n \times  n \) skew-symmetric matrices. Any geodesic \( \gamma \) with \( \gamma \left( 0\right)  = \mathrm{I} \) can be written uniquely as

\[
\gamma \left( t\right)  = \exp \left( {\pi tA}\right)
\]

for some \( A \in  \mathfrak{g} \) .

Let \( n = {2m} \) . Since \( A \) is skew-symmetric, there exists an element \( T \in  \mathrm{O}\left( n\right) \) so that

\[
{TA}{T}^{-1} = \left( \begin{matrix} 0 & {a}_{1} & & & & \\   - {a}_{1} & 0 & & & & \\   & & 0 & {a}_{2} & & \\   & &  - {a}_{2} & 0 & & \\   & & & &  \ddots  & \\   & & & & &  - {a}_{m} \end{matrix}\right)
\]

with \( {a}_{1},{a}_{2},\ldots ,{a}_{m} \geq  0 \) . A short computation shows that \( T\left( {\exp {\pi A}}\right) {T}^{-1} \) is equal to

\[
\left( \begin{matrix} \cos \pi {a}_{1} & \sin \pi {a}_{1} & 0 & 0 & \cdots \\   - \sin \pi {a}_{1} & \cos \pi {a}_{1} & 0 & 0 & \cdots \\  0 & 0 & \cos \pi {a}_{2} & \sin \pi {a}_{2} & \cdots \\  0 & 0 &  - \sin \pi {a}_{2} & \cos \pi {a}_{2} & \cdots \\  \cdots & \cdots & \cdots & \cdots &  \ddots   \end{matrix}\right)
\]

Thus \( \exp \left( {\pi A}\right) \) is equal to -I if and only if \( {a}_{1},{a}_{2},\ldots ,{a}_{m} \) , are odd integers.

The inner product \( \langle A, A\rangle \) is easily seen to be \( 2\left( {{a}_{1}^{2} + {a}_{2}^{2} + \cdots  + {a}_{m}^{2}}\right) \) . Therefore the geodesic \( \gamma \left( t\right)  = \exp \left( {\pi tA}\right) \) from I to -I is minimal if and only if \( {a}_{1} = {a}_{2} = \ldots  = \; {a}_{m} = 1 \) .

If \( \gamma \) is minimal then

\[
{A}^{2} = {T}^{-1}\left( \begin{matrix} 0 & 1 & & & \\   - 1 & 0 & & & \\   & 0 & 1 & & \\   & &  - 1 & 0 & \\   & & & &  \ddots   \end{matrix}\right) T =  - \mathrm{I},
\]

hence A is a complex structure.

Conversely, let J be any complex structure. Since J is orthogonal we have

\[
{\mathrm{{JJ}}}^{ * } = \mathrm{I}
\]

where \( {\mathrm{J}}^{ * } \) denotes the transpose of \( \mathrm{J} \) . Together with the identity \( \mathrm{{JJ}} =  - \mathrm{I} \) this implies that \( {\mathrm{J}}^{ * } =  - \mathrm{J} \) . Thus \( \mathrm{J} \) is skew-symmetric. Hence

\[
T\mathrm{\;J}{T}^{-1} = \left( \begin{matrix} 0 & {a}_{1} & & \\   - {a}_{1} & 0 & & \\   & &  \ddots  & \\   & & &  \end{matrix}\right)
\]

for some \( {a}_{1},{a}_{2},\ldots ,{a}_{m} \geq  0 \) and some \( T \) . Now the identity \( {\mathrm{J}}^{2} =  - \mathrm{I} \) implies that \( {a}_{1} = \cdots  = {a}_{m} = 1 \) ; and hence that \( \exp \pi \mathrm{J} =  - \mathrm{I} \) . This completes the proof.

Lemma 24.3. Any non-minimal geodesic from I to \( - \mathrm{I} \) in \( \mathrm{O}\left( {2m}\right) \) has index \( \geq \; {2m} - 2 \) .

The proof is similar to that of Lemma 23.2. Suppose that the geodesic has the form \( t \mapsto  \exp \left( {\pi tA}\right) \) with

\[
A = \left( \begin{matrix} 0 & {a}_{1} & & & \\   - {a}_{1} & 0 & & & \\   & & 0 & {a}_{2} & \\   & &  - {a}_{2} & 0 & \\   & & & &  \ddots   \end{matrix}\right)
\]

where \( {a}_{1} \geq  {a}_{2} \geq  \cdots  \geq  {a}_{m} > 0 \) are odd integers. Computation shows that the non-zero eigenvalues of the linear transformation \( {K}_{A} =  - \frac{1}{4}{\left( \operatorname{Ad}A\right) }^{2} \) are

(1) for each \( i < j \) the number \( {\left( {a}_{i} + {a}_{j}\right) }^{2}/4 \) , and

(2) for each \( i < j \) with \( {a}_{i} \neq  {a}_{j} \) the number \( {\left( ai - aj\right) }^{2}/4 \) .

Each of these eigenvalues is to be counted twice. This leads to the formula

\[
\lambda  = \mathop{\sum }\limits_{{i < j}}\left( {{a}_{i} + {a}_{j} - 2}\right)  + \mathop{\sum }\limits_{{{a}_{i} > {a}_{j}}}\left( {{a}_{i} - {a}_{j} - 2}\right) .
\]

For a minimal geodesic we have \( {a}_{1} = {a}_{2} = \cdots  = {a}_{m} = 1 \) ; so that \( \lambda  = 0 \) , as expected. For a non-minimal geodesic we have \( {a}_{1} \geq  3 \) ; so that

\[
\lambda  \geq  \mathop{\sum }\limits_{2}^{m}\left( {3 + 1 - 2}\right)  + 0 = {2m} - 2.
\]

This completes the proof.

Now let us apply Theorem 22.1. The two lemmas above, together with the statement that \( {\Omega }_{1}\left( n\right) \) is a manifold imply the following.

Theorem 24.4 (Bott). The inclusion map \( {\Omega }_{1}\left( n\right)  \hookrightarrow  \Omega \mathrm{O}\left( n\right) \) induces isomorphisms of homotopy groups in dimensions \( \leq  n - 4 \) . Hence

\[
{\pi }_{i}{\Omega }_{1}\left( n\right)  \cong  {\pi }_{i + 1}\mathrm{O}\left( n\right)
\]

for \( i \leq  n - 4 \) .

Now we will iterate this procedure, studying the space of geodesics from J to -J in \( {\Omega }_{1}\left( n\right) \) ; and so on. Assume that \( n \) is divisible by a high power of 2 .

Let \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) be fixed complex structures on \( {\mathbf{R}}^{n} \) which anti-commute \( {}^{1} \) , in the sense that

\[
{\mathrm{J}}_{r}{\mathrm{\;J}}_{s} + {\mathrm{J}}_{s}{\mathrm{\;J}}_{r} = 0
\]

for \( r \neq  s \) . Suppose that there exists at least one other complex structure \( \mathrm{J} \) which anti-commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) .

Definition 24.5. Let \( {\Omega }_{k}\left( n\right) \) denote the set of all complex structures \( \mathrm{J} \) on \( {\mathbf{R}}^{n} \) which anti-commute with the fixed structures \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) .

---

\( {}^{1} \) These structures make \( {\mathbf{R}}^{n} \) into a module over a suitable Clifford algebra. However, the Clifford algebras will be suppressed in the following presentation.

---

Thus we have

\[
{\Omega }_{k}\left( n\right)  \subseteq  {\Omega }_{k - 1}\left( n\right)  \subseteq  \ldots  \subseteq  {\Omega }_{1}\left( n\right)  \subseteq  \mathrm{O}\left( n\right)
\]

Clearly each \( {\Omega }_{k}\left( n\right) \) is a compact set. To complete the definition it is natural to define \( {\Omega }_{0}\left( n\right) \) to be \( \mathrm{O}\left( n\right) \)

Lemma 24.6. Each \( {\Omega }_{k}\left( n\right) \) is a smooth, totally geodesic \( {}^{2} \) submanifold of \( \mathrm{O}\left( n\right) \) . The space of minimal geodesics from \( {\mathrm{J}}_{\ell } \) to \( - {\mathrm{J}}_{\ell } \) in \( {\Omega }_{\ell }\left( n\right) \) is homeomorphic to \( {\Omega }_{\ell  + 1}\left( n\right) \) , for \( 0 \leq  \ell  < k \) .

It follows that each component of \( {\Omega }_{k}\left( n\right) \) is a symmetric space. For the isometric reflection of \( \mathrm{O}\left( n\right) \) in a point of \( {\Omega }_{k}\left( n\right) \) will automatically carry \( {\Omega }_{k}\left( n\right) \) to itself.

Proof of Lemma 24.6. Any point in \( \mathrm{O}\left( n\right) \) close to the identity can be expressed uniquely in the form \( \exp A \) , where \( A \) is a "small," skew-symmetric matrix. Hence any point in \( \mathrm{O}\left( n\right) \) close to the complex structure \( \mathrm{J} \) can be expressed uniquely as J \( \exp A \) ; where again \( A \) is small and skew.

Assertion 24.1. J \( \exp A \) is a complex structure if and only if \( A \) anti-commutes with \( \mathrm{J} \) .

Proof. If \( \mathrm{A} \) anti-commutes with \( \mathrm{J} \) , then \( {\mathrm{J}}^{-1}A\mathrm{\;J} =  - A \) hence

\[
\mathrm{I} = \exp \left( {{\mathrm{J}}^{-1}A\mathrm{\;J}}\right) \exp A = {\mathrm{J}}^{-1}\exp A\mathrm{\;J}\exp A.
\]

Therefore \( {\left( \mathrm{J}\exp A\right) }^{2} =  - \mathrm{I} \) . Conversely if \( {\left( \mathrm{J}\exp A\right) }^{2} =  - \mathrm{I} \) then the above computation shows that

\[
\exp \left( {{\mathrm{J}}^{-1}A\mathrm{\;J}}\right) \exp A = \mathrm{I}.
\]

Since \( A \) is small, this implies that

\[
{\mathrm{J}}^{-1}A\mathrm{\;J} =  - A
\]

so that \( A \) anti-commutes with J.

Assertion 24.2. J \( \exp A \) anti-commutes with the complex structures \( {J}_{1},\ldots ,{J}_{k - 1} \) if and only if \( A \) commutes with \( {J}_{1},\ldots ,{J}_{k - 1} \) .

The proof is similar and straightforward.

Note that Assertions 24.1 and 24.2 both put linear conditions on \( A \) . Thus a neighborhood of \( \mathrm{J} \) in \( {\Omega }_{k}\left( n\right) \) consists of all points \( \mathrm{J}\exp A \) where \( A \) ranges over all small matrices in a linear subspace of the Lie algebra \( \mathfrak{g} \) . This clearly implies that \( {\Omega }_{k}\left( n\right) \) is a totally geodesic submanifold of \( \mathrm{O}\left( n\right) \) .

Now choose a specific point \( {\mathrm{J}}_{k} \in  {\Omega }_{k}\left( n\right) \) , and assume that there exists a complex structure \( \mathrm{J} \) which anti-commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k} \) . Setting \( \mathrm{J} = {\mathrm{J}}_{k}A \) we see easily that \( A \) is also a complex structure which anti-commutes with \( {\mathrm{J}}_{k} \) . However, \( A \) commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) . Hence the formula

\[
t \mapsto  {\mathrm{J}}_{k}\exp \left( {\pi tA}\right)
\]

defines a geodesic from \( {\mathrm{J}}_{k} \) to \( - {\mathrm{J}}_{k} \) in \( {\Omega }_{k}\left( n\right) \) . Since this geodesic is minimal in \( \mathrm{O}\left( n\right) \) , it is certainly minimal in \( {\Omega }_{k}\left( n\right) \) .

---

\( {}^{2} \) submanifold of a Riemannian manifold is called totally geodesic if each geodesic in the submanifold is also a geodesic in larger manifold.

---

Conversely, let \( \gamma \) be any minimal geodesic from \( {\mathrm{J}}_{k} \) to \( - {\mathrm{J}}_{k} \) in \( {\Omega }_{k}\left( n\right) \) . Setting \( \gamma \left( t\right)  = {\mathrm{J}}_{k}\exp \left( {\pi tA}\right) \) , it follows from Lemma 24.2 that \( A \) is a complex structure, and from Assertions 24.1 and 24.2 that \( A \) commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) and anti-commutes with \( {\mathrm{J}}_{k} \) . It follows easily that \( {\mathrm{J}}_{k}A \) belongs to \( {\Omega }_{k + 1}\left( n\right) \) . This completes the proof of Lemma 24.6.

Remark. The point \( {\mathrm{J}}_{k}A \in  {\Omega }_{k + 1}\left( n\right) \) which corresponds to a given geodesic \( \gamma \) has a very simple interpretation: it is the midpoint \( \gamma \left( \frac{1}{2}\right) \) of the geodesic.

In order to pass to a stable situation, note that \( {\Omega }_{k}\left( n\right) \) can be imbedded in \( {\Omega }_{k + 1}\left( {n + {n}^{\prime }}\right) \) as follows. Choose fixed anti-commuting complex structures \( {\mathrm{J}}_{1}^{\prime },\ldots ,{\mathrm{J}}_{k}^{\prime } \) on \( {\mathbf{R}}^{{n}^{\prime }} \) . Then each \( \mathrm{J} \in  {\Omega }_{k}\left( n\right) \) determines a complex structure \( \mathrm{J} \oplus  {\mathrm{J}}_{k}^{\prime } \) on \( {\mathbf{R}}^{n} \oplus  {\mathbf{R}}^{{n}^{\prime }} \) which anti-commutes with \( {\mathrm{J}}_{\alpha } \oplus  {\mathrm{J}}_{\alpha }^{\prime } \) for \( \alpha  = 1,\ldots , k - 1 \) .

Definition 24.7. Let \( {\Omega }_{k} \) denote the direct limit as \( n \rightarrow  \infty \) of the spaces \( {\Omega }_{k}\left( n\right) \) , with the direct limit topology. (I.e., the fine topology.) The space \( \mathrm{O} = {\Omega }_{0} \) is called the infinite orthogonal group.

It is not difficult to see that the inclusions \( {\Omega }_{k + 1}\left( n\right)  \hookrightarrow  \Omega {\Omega }_{k}\left( n\right) \) give rise, in the limit, to inclusions \( {\Omega }_{k + 1} \hookrightarrow  \Omega {\Omega }_{k} \) .

Theorem 24.8. For each \( k \geq  0 \) this limit map \( {\Omega }_{k + 1} \rightarrow  \Omega {\Omega }_{k} \) is a homotopy equivalence. Thus we have isomorphisms

\[
{\pi }_{h}\mathrm{O} \cong  {\pi }_{h - 1}{\Omega }_{1} \cong  {\pi }_{h - 2}{\Omega }_{2} \cong  \ldots  \cong  {\pi }_{1}{\Omega }_{h - 1}.
\]

The proof will be given presently.

Next we will give individual descriptions of the manifolds \( {\Omega }_{k}\left( n\right) \) for \( k = 0,1,2,\ldots ,8 \) .

\( {\Omega }_{0}\left( n\right) \; \) is the orthogonal group.

\( {\Omega }_{1}\left( n\right) \; \) is the set of all complex structures on \( {\mathbf{R}}^{n} \) .

Given a fixed complex structure \( {\mathrm{J}}_{1} \) we may think of \( {\mathbf{R}}^{n} \) as being a vector space \( {\mathbb{C}}^{n/2} \) over the complex numbers.

\( {\Omega }_{2}\left( n\right) \) can be described as the set of "quaternionic structures" on the complex vector space \( {\mathbb{C}}^{n/2} \) . Given a fixed \( {\mathrm{J}}_{2} \in  {\Omega }_{2}\left( n\right) \) we may think of \( {\mathbb{C}}^{n/2} \) as being a vector space \( {\mathrm{H}}^{n/4} \) over the quaternions \( \mathrm{H} \) . Let \( \mathrm{{Sp}}\left( {n/4}\right) \) be the group of isometries of this vector space onto itself. Then \( {\Omega }_{2}\left( n\right) \) can be identified with the quotient space \( \mathrm{U}\left( {n/2}\right) /\mathrm{{Sp}}\left( {n/4}\right) \) .

Before going further it will be convenient to set \( n = {16r} \) .

Lemma 24.6-(3). The space \( {\Omega }_{3}\left( {16r}\right) \) can be identified with the quaternionic Grass-mann manifold consisting of all quaternionic subspaces of \( {\mathrm{H}}^{4r} \) .

Proof. Any complex structure \( {\mathrm{J}}_{3} \in  {\Omega }_{3}\left( {16r}\right) \) determines a splitting of \( {\mathrm{H}}^{4r} = {\mathbf{R}}^{16r} \) into two mutually orthogonal subspaces \( {V}_{1} \) and \( {V}_{2} \) as follows. Note that \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) is an orthogonal transformation with square \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3}{\mathrm{\;J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) equal to +I. Hence the eigenvalues of \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) are \( \pm  1 \) . Let \( {V}_{1} \subseteq  {\mathbf{R}}^{16r} \) be the subspace on which \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) equals \( + \mathrm{I} \) ; and let \( {V}_{2} \) be the orthogonal subspace on which it equals \( - \mathrm{I} \) . Then clearly \( {\mathbf{R}}^{16r} = {V}_{1} \oplus  {V}_{2} \) . Since \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) commutes with \( {\mathrm{J}}_{1} \) and \( {\mathrm{J}}_{2} \) it is clear that both \( {V}_{1} \) and \( {V}_{2} \) are closed under the action of \( {\mathrm{J}}_{1} \) and \( {\mathrm{J}}_{2} \) .

Conversely, given the splitting \( {\mathrm{H}}^{4r} = {V}_{1} \oplus  {V}_{2} \) into mutually orthogonal quaternionic subspaces, we can define \( {\mathrm{J}}_{3} \in  {\Omega }_{3}\left( {16r}\right) \) by the identities

\[
\left\{  \begin{array}{l} {\left. {\mathrm{J}}_{3}\right| }_{{V}_{1}} =  - {\left. {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}\right| }_{{V}_{1}} \\  {\left. {\mathrm{\;J}}_{3}\right| }_{{V}_{2}} = {\left. {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}\right| }_{{V}_{2}}. \end{array}\right.
\]

This proves Lemma 24.6-(3).

The space \( {\Omega }_{3}\left( {16r}\right) \) is awkward in that it contains components of varying dimension. It is convenient to restrict attention to the component of largest dimension: namely the space of \( {2r} \) -dimensional quaternionic subspaces of \( {\mathrm{H}}^{4r} \) . Henceforth, we will assume that \( {\mathrm{J}}_{3} \) has been chosen in this way, so that dimes \( {\dim }_{\mathrm{H}}{V}_{1} = {\dim }_{\mathrm{H}}{V}_{2} = \; {2r} \) .

Lemma 24.6-(4). The space \( {\Omega }_{4}\left( {16r}\right) \) can be identified with the set of all quaternionic isometries from \( {V}_{1} \) to \( {V}_{2} \) . Thus \( {\Omega }_{4}\left( {16r}\right) \) is diffeomorphic to the symplectic group \( \mathrm{{Sp}}\left( {2r}\right) \) .

Proof. Given \( {\mathrm{J}}_{4} \in  {\Omega }_{4}\left( {16r}\right) \) note that the product \( {\mathrm{J}}_{3}{\mathrm{\;J}}_{4} \) anti-commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) . Hence \( {\mathrm{J}}_{3}{\mathrm{\;J}}_{4} \) maps \( {V}_{1} \) to \( {V}_{2} \) (and \( {V}_{2} \) to \( {V}_{1} \) ). Since \( {\mathrm{J}}_{3}{\mathrm{\;J}}_{4} \) commutes with \( {\mathrm{J}}_{1} \) and \( {\mathrm{J}}_{2} \) we see that

\[
{\left. {\mathrm{J}}_{3}{\mathrm{\;J}}_{4}\right| }_{{V}_{1}} : {V}_{1} \rightarrow  {V}_{2}
\]

is a quaternionic isomorphism. Conversely, given any such isomorphism \( T : {V}_{1} \rightarrow  {V}_{2} \) it is easily seen that \( {\mathrm{J}}_{4} \) is uniquely determined by the identities:

\[
\left\{  \begin{array}{l} {\left. {\mathrm{J}}_{4}\right| }_{{V}_{1}} = {\mathrm{J}}_{3}^{-1}T \\  {\left. {\mathrm{\;J}}_{4}\right| }_{{V}_{2}} =  - {T}^{-1}{\mathrm{\;J}}_{3}. \end{array}\right.
\]

This proves Lemma 24.6-(4).

Lemma 24.6-(5). The space \( {\Omega }_{5}\left( {16r}\right) \) can be identified with the set of all vector spaces \( W \subseteq  {V}_{1} \) such that

(1) \( W \) is closed under \( {\mathrm{J}}_{1} \) (i.e., \( W \) is a complex vector space) and

(2) \( {V}_{1} \) splits as the orthogonal sum \( W \oplus  {\mathrm{J}}_{2}W \) .

Proof. Given \( {J}_{5} \in  {\Omega }_{5}\left( {16r}\right) \) note that the transformation \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) and has square +I. Thus \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) maps \( {V}_{1} \) into itself; and determines a splitting of \( {V}_{1} \) into two mutually orthogonal subspaces. Let \( W \subseteq  {V}_{1} \) be the subspace on which \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) coincides with +I. Since \( {\mathrm{J}}_{2} \) anti-commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) , it follows that \( {\mathrm{J}}_{2}W \subseteq  {V}_{1} \) is precisely the orthogonal subspace, on which \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) equals -I. Clearly \( {\mathrm{J}}_{1}W = W \) .

Conversely, given the subspace \( W \) , it is not difficult to show that \( {\mathrm{J}}_{5} \) is uniquely determined.

Remark. If \( \mathrm{U}\left( {2r}\right)  \subseteq  \operatorname{Sp}\left( {2r}\right) \) denotes the group of quaternionic automorphisms of \( {V}_{1} \) keeping \( W \) fixed, then the quotient space \( \mathrm{{Sp}}\left( {2r}\right) /\mathrm{U}\left( {2r}\right) \) can be identified with \( {\Omega }_{5}\left( {16r}\right) \) .

Lemma 24.6-(6). The space \( {\Omega }_{6}\left( {16r}\right) \) can be identified with the set of all real subspaces \( X \subseteq  W \) such that \( W \) splits as the orthogonal sum \( X \oplus  {\mathrm{J}}_{1}X \) .

Proof. Given \( {J}_{6} \in  {\Omega }_{6}\left( {16r}\right) \) note that the transformation \( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6} \) commutes both with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) and with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) . Hence \( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6} \) maps \( W \) into itself. Since \( {\left( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6}\right) }^{2} = \mathrm{I} \) , it follows that \( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6} \) determines a splitting of \( W \) into two mutually orthogonal subspaces. Let \( X \subseteq  W \) be the subspace on which \( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6} \) equals +I. Then \( {\mathrm{J}}_{1}X \) will be the orthogonal subspace on which it equals -I.

Conversely, given \( X \subseteq  W \) , it is not hard to see that \( {\mathrm{J}}_{6} \) is uniquely determined.

Remark. If \( \mathrm{O}\left( {2r}\right)  \subseteq  \mathrm{U}\left( {2r}\right) \) denotes the group of complex automorphisms of \( W \) keeping \( X \) fixed, then the quotient space \( \mathrm{U}\left( {2r}\right) /\mathrm{O}\left( {2r}\right) \) can be identified with a \( {\Omega }_{6}\left( {16r}\right) \) .

Lemma 24.6-(7). The space \( {\Omega }_{7}\left( {16r}\right) \) can be identified with the set of all real Grassmann manifold consisting of all real subspaces of \( X \cong  {\mathbf{R}}^{2r} \) .

Proof. Given \( {\mathrm{J}}_{7} \) , anti-commuting with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{6} \) note that \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{6}{\mathrm{\;J}}_{7} \) commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3} \) , with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) , and with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{6} \) ; and has square +I. Thus \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{6}{\mathrm{\;J}}_{7} \) determines a splitting of \( X \) into two mutually orthogonal subspaces: \( {X}_{1} \) (where \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{6}{\mathrm{\;J}}_{7} \) equals +I) and \( {X}_{2} \) (where \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{6}{\mathrm{\;J}}_{7} \) equals -I). Conversely, given \( {X}_{1} \subseteq  X \) it can be shown that \( {\mathrm{J}}_{7} \) is uniquely determined.

This space \( {\Omega }_{7}\left( {16r}\right) \) , like \( {\Omega }_{3}\left( {16r}\right) \) , has components of varying dimension. Again we will restrict attention to the component of largest dimension, by assuming that

\[
\dim {X}_{1} = \dim {X}_{2} = r.
\]

Thus we obtain:

Assertion 24.3. The largest component of \( {\Omega }_{7}\left( {16r}\right) \) is diffeomorphic to the Grass-mann manifold consisting of r-dimensional subspaces of \( {\mathbf{R}}^{2r} \) .

Lemma 24.6-(8). The space \( {\Omega }_{8}\left( {16r}\right) \) can be identified with the set of all real isometries from \( {X}_{1} \) to \( {X}_{2} \) .

Proof. If \( {J}_{8} \in  {\Omega }_{8}\left( {16r}\right) \) then the orthogonal transformation \( {\mathrm{J}}_{7}{\mathrm{\;J}}_{8} \) commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3},{\mathrm{\;J}}_{1}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5} \) , and \( {\mathrm{J}}_{2}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{6} \) ; but anti-commutes with \( {\mathrm{J}}_{1}{\mathrm{\;J}}_{6}{\mathrm{\;J}}_{7} \) . Hence \( {\mathrm{J}}_{7}{\mathrm{\;J}}_{8} \) maps \( {X}_{1} \) isomorphically onto \( {X}_{2} \) . Clearly this isomorphism determines \( {\mathrm{J}}_{8} \) uniquely.

Thus we see that \( {\Omega }_{8}\left( {16r}\right) \) is diffeomorphic to the orthogonal group \( {}^{3}\mathrm{O}\left( r\right) \) .

Let us consider this diffeomorphism \( {\Omega }_{8}\left( {16r}\right)  \rightarrow  \mathrm{O}\left( r\right) \) , and pass to the limit as \( r \rightarrow  \infty \) . It follows that \( {\Omega }_{8} \) is homeomorphic to the infinite orthogonal group 0 . Combining this fact with Theorem 24.8, we obtain the following.

---

\( {}^{3} \) For \( k > 8 \) it can be shown that \( {\Omega }_{k}\left( {16r}\right) \) is diffeomorphic to \( {\Omega }_{k - 8}\left( {16r}\right) \) . In fact any additional complex structures \( {\mathrm{J}}_{9},{\mathrm{\;J}}_{10},\ldots ,{\mathrm{J}}_{k} \) on \( {\mathbf{R}}^{16r} \) give rise to anti-commuting complex structures \( {\mathrm{J}}_{8}{\mathrm{\;J}}_{9},{\mathrm{\;J}}_{8}{\mathrm{\;J}}_{10},{\mathrm{\;J}}_{8}{\mathrm{\;J}}_{11},\ldots ,{\mathrm{J}}_{8}{\mathrm{\;J}}_{k} \) on \( {X}_{1} \) ; and hence to an element of \( {\Omega }_{k - 8}\left( r\right) \) . However, for our purposes it will be sufficient to stop with \( k = 8 \) .

---

Theorem 24.9 (Bott). The infinite orthogonal group O has the same homotopy type as its own 8-th loop space. Hence the homotopy group \( {\pi }_{i}\mathrm{O} \) is isomorphic to \( {\pi }_{i + 8}\mathrm{O} \) for \( i \geq  0 \) .

If \( \mathrm{{Sp}} = {\Omega }_{4} \) denotes the infinite symplectic group, then the above argument also shows that \( \mathrm{O} \) has the homotopy type of the 4-fold loop space \( {\Omega \Omega \Omega \Omega }\mathrm{{Sp}} \) , and that Sp has the homotopy type of the 4-fold loop space \( {\Omega \Omega \Omega \Omega }\mathrm{O} \) . The actual homotopy groups can be tabulated as follows.

<table><tr><td>modulo 8</td><td>\( {\pi }_{i}\mathrm{O} \)</td><td>\( {\pi }_{i} \) Sp</td></tr><tr><td>0</td><td>\( {\mathbb{Z}}_{2} \)</td><td>0</td></tr><tr><td>1</td><td>\( {\mathbb{Z}}_{2} \)</td><td>0</td></tr><tr><td>2</td><td>0</td><td>0</td></tr><tr><td>3</td><td>\( \mathbb{Z} \)</td><td>\( \mathbb{Z} \)</td></tr><tr><td>4</td><td>0</td><td>\( {\mathbb{Z}}_{2} \)</td></tr><tr><td>5</td><td>0</td><td>\( {\mathbb{Z}}_{2} \)</td></tr><tr><td>6</td><td>0</td><td>0</td></tr><tr><td>7</td><td>\( \mathbb{Z} \)</td><td>\( \mathbb{Z} \)</td></tr></table>

The verification that these groups are correct will be left to the reader. (Note that \( \mathrm{{Sp}}\left( 1\right) \) is a 3-sphere, and that \( \mathrm{{Sp}}\left( 3\right) \) is a projective 3-space.)

The remainder of this section will be concerned with the proof of Theorem 24.8. It is first necessary to prove an algebraic lemma.

Consider a Euclidean vector space \( V \) with anti-commuting complex structures \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k} \)

Definition 24.10. \( V \) is a minimal \( \left( {{\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k}}\right) \) -space if no proper, nontrivial subspace is closed under the action of \( {\mathrm{J}}_{1},\ldots , \) and \( {\mathrm{J}}_{k} \) . Two such minimal vector spaces are isomorphic if there is an isometry between them which commutes with the action of \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k} \) .

Lemma 24.11 (Bott and Shapiro). For \( k \text{ ≢ } 3\left( {\;\operatorname{mod}\;4}\right) \) , any two minimal \( \left( {{\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k}}\right) \) vector spaces are isomorphic.

The proof of Lemma 24.11 follows that of Lemma 24.6. For \( k = 0,1 \) , or 2 a minimal space is just a 1-dimensional vector space over the reals, the complex numbers or the quaternions. Clearly any two such are isomorphic.

For \( k = 3 \) a minimal space is still a 1-dimensional vector space over the quater-nions. However, there are two possibilities, according as \( {\mathrm{J}}_{3} \) is equal to \( + {\mathrm{J}}_{1}{\mathrm{\;J}}_{2} \) or \( - {\mathrm{J}}_{1}{\mathrm{\;J}}_{2} \) . This gives two non-isomorphic minimal spaces, both with dimension equal to 4. Call these \( H \) and \( {H}^{\prime } \) .

For \( k = 4 \) a minimal space must be isomorphic to \( H \oplus  {H}^{\prime } \) , with \( {\mathrm{J}}_{3}{\mathrm{\;J}}_{4} \) mapping \( H \) to \( {H}^{\prime } \) . The dimension is equal to 8 .

For \( k = 5,6 \) we obtain the same minimal vector space \( H \oplus  {H}^{\prime } \) . The complex structures \( {\mathrm{J}}_{5},{\mathrm{\;J}}_{6} \) merely determine preferred complex or real subspaces. For \( k = 7 \) we again obtain the same space, but there are two possibilities, according as \( {\mathrm{J}}_{7} \) is equal to \( + {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5}{\mathrm{\;J}}_{6} \) or to \( - {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}{\mathrm{\;J}}_{3}{\mathrm{\;J}}_{4}{\mathrm{\;J}}_{5}{\mathrm{\;J}}_{6} \) . Thus in this case there are two non-isomorphic minimal vector spaces; call these \( L \) and \( {L}^{\prime } \) .

For \( k = 8 \) a minimal vector space must be isomorphic to \( L \oplus  {L}^{\prime } \) , with \( {\mathrm{J}}_{7}{\mathrm{\;J}}_{8} \) mapping \( L \) onto \( {L}^{\prime } \) . The dimension is equal to 16 .

For \( k > 8 \) it can be shown that the situation repeats more or less periodically. However, the cases \( k < 8 \) will suffice for our purposes.

Let \( {m}_{k} \) denote the dimension of a minimal \( \left( {{\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k}}\right) \) -vector space. From the above discussion we see that:

\[
{m}_{0} = 1,{m}_{1} = 2,{m}_{2} = 3,{m}_{3} = 4,
\]

\[
{m}_{4} = {m}_{5} = {m}_{6} = {m}_{7} = 8,{m}_{8} = {16},
\]

For \( k > 8 \) it can be shown that \( {m}_{k} = {16}{m}_{k - 8} \) .

Remark. These numbers \( {m}_{k} \) are closely connected with the problem of constructing linearly independent vector fields on spheres. Suppose for example that \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k} \) are anti-commuting complex structures on a vector space \( V \) of dimension \( r{m}_{k} \) . Here \( r \) can be any positive integer. Then for each unit vector \( u \in  V \) the \( k \) vectors \( {\mathrm{J}}_{1}u,{\mathrm{\;J}}_{2}u,\ldots ,{\mathrm{J}}_{k}u \) are perpendicular to each other and to \( u \) . Thus we obtain \( k \) linearly independent vector fields on an \( \left( {r{m}_{k} - 1}\right) \) -sphere. For example we obtain 3 vector fields on a \( \left( {{4r} - 1}\right) \) -sphere; 7 vector fields on an \( \left( {{8r} - 1}\right) \) -sphere; 8 vector fields on a (16r-1)-sphere; and so on. These results are due to Hurwitz and Radon. (Compare [Eck43].) J. F. Adams has recently proved that these estimates are best possible.

Proof of Theorem 24.8 for \( k \text{ ≢ } 2\left( {\;\operatorname{mod}\;4}\right) \) . We must study non-minimal geodesics from \( \mathrm{J} \) to \( - \mathrm{J} \) in \( {\Omega }_{k}\left( n\right) \) . Recall that the tangent space of \( {\Omega }_{k}\left( n\right) \) at \( \mathrm{J} \) consists of all matrices \( \mathrm{J}A \) where

(1) \( A \) is skew

(2) \( A \) anti-commutes with \( \mathrm{J} \)

(3) \( A \) commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \)

Let \( T \) denote the vector space of all such matrices \( A \) . A given \( A \in  T \) corresponds to a geodesic \( t \mapsto  \mathrm{J}\exp \left( {\pi tA}\right) \) from \( \mathrm{J} \) to \( - \mathrm{J} \) if and only if its eigenvalues are all odd multiples of \( i \) .

Each such \( A \in  T \) determines a self-adjoint transformation \( {K}_{A} : T \rightarrow  T \) . Since a \( {\Omega }_{k}\left( n\right) \) is a totally geodesic submanifold of \( \mathrm{O}\left( n\right) \) , we can compute \( {K}_{A} \) by the formula

\[
{K}_{A}B = \frac{1}{4}\left\lbrack  {A,\left\lbrack  {A, B}\right\rbrack  }\right\rbrack   = \frac{\left( -{A}^{2}B + 2ABA - B{A}^{2}\right) }{4},
\]

just as before. We must construct some non-zero eigenvalues of \( {K}_{A} \) so as to obtain a lower bound for the index of the corresponding geodesic

\[
t \mapsto  \mathrm{J}\exp \left( {\pi tA}\right)
\]

Split the vector space \( {\mathbf{R}}^{n} \) as a direct sum \( {M}_{1} \oplus  {M}_{2} \oplus  \cdots  \oplus  {M}_{s} \) of mutually orthogonal subspaces which are closed and minimal under the action of \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) , J and \( A \) . Then the eigenvalues of \( A \) on \( {M}_{h} \) must be all equal, except for sign. \( {}^{4} \) For otherwise \( {M}_{h} \) would split as a sum of eigenspaces of \( A \) ; and hence would not be minimal. Let \( \pm  i{a}_{h} \) be the two eigenvalues of \( {\left. A\right| }_{{M}_{h}} \) ; where \( {a}_{1},\ldots ,{a}_{s} \) are odd, positive integers.

---

\( {}^{4} \) We are dealing with the complex eigenvalues of a real, skew-symmetric transformation. Hence these eigenvalues are pure imaginary; and occur in conjugate pairs.

---

Now note that \( {\mathrm{J}}^{\prime } = {a}_{h}^{-1}\mathrm{\;J}{\left. A\right| }_{{M}_{h}} \) ; is a complex structure on \( {M}_{h} \) which anti-commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) , and \( \mathrm{J} \) . Thus \( {M}_{h} \) is \( \left( {{\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1},\mathrm{J},{\mathrm{J}}^{\prime }}\right) \) -minimal. Hence the dimension of \( {M}_{h} \) is \( {m}_{k + 1} \) . Since \( k + 1 \text{ ≢ } 3\left( {\;\operatorname{mod}\;4}\right) \) we see that \( {M}_{1},{M}_{2},\ldots ,{M}_{s} \) are mutually isomorphic.

For each pair \( h, j \) with \( h \neq  j \) we can construct an eigenvector \( B : {\mathbf{R}}^{n} \rightarrow  {\mathbf{R}}^{n} \) of the linear transformation \( {K}_{A} : T \rightarrow  T \) as follows. Let \( {\left. B\right| }_{{M}_{\ell }} \) , be zero for \( \ell  \neq  h, j \) . Let \( {\left. B\right| }_{{M}_{h}} \) be an isometry from \( {M}_{h} \) to \( {M}_{j} \) which satisfies the conditions

\[
B{\mathrm{\;J}}_{\alpha } = {\mathrm{J}}_{\alpha }B\;\text{ for }\;\alpha  = 1,\ldots , k - 1;
\]

\[
B\mathrm{\;J} =  - \mathrm{J}B\;\text{ and }\;B{\mathrm{\;J}}^{\prime } =  + {\mathrm{J}}^{\prime }B.
\]

In other words \( {\left. B\right| }_{{M}_{h}} \) is an isomorphism from \( {M}_{h} \) to \( {\bar{M}}_{j} \) ; where the bar indicates that we have changed the sign of \( \mathrm{J} \) on \( {M}_{j} \) . Such an isomorphism exists by Lemma 24.11. Finally let \( {\left. B\right| }_{{M}_{j}} \) be the negative adjoint of \( {\left. B\right| }_{{M}_{h}} \) .

Proof that \( B \) belongs to the vector space \( T \) . Since

\[
\langle {Bv}, w\rangle  = \langle v, - {Bw}\rangle \;\text{ for }\;v \in  {M}_{h}, w \in  {M}_{j}
\]

it is clear that \( B \) is skew-symmetric. It is also clear that \( {\left. B\right| }_{{M}_{h}} \) commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) and anti-commutes with \( \mathrm{J} \) . It follows easily that the negative adjoint \( {\left. B\right| }_{{M}_{j}} \) also commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) and anti-commutes with \( \mathrm{J} \) . Thus \( B \in  T \) .

We claim that \( B \) is an eigenvector of \( {K}_{A} \) corresponding to the eigenvalue \( \left( {{a}_{h} + }\right. \; {\left. {a}_{j}\right) }^{2}/4 \) . For example if \( v \in  {M}_{h} \) then

\[
{\left( {K}_{A}B\right) }_{v} = \frac{1}{4}\left( {-{A}^{2}B + {2ABA} - B{A}^{2}}\right) v
\]

\[
= \frac{1}{4}\left( {-{a}_{j}^{2}{Bv} + 2{a}_{j}B{a}_{h}v - B{a}_{h}^{2}v}\right)
\]

\[
= \frac{1}{4}{\left( {a}_{j} + {a}_{h}\right) }^{2}{Bv}
\]

and a similar computation applies for \( v \in  {M}_{j} \) .

Now let us count. The number of minimal spaces \( {M}_{h} \subseteq  {\mathbf{R}}^{n} \) is given by \( s = \; n/{m}_{k + 1} \) . For at least one of these the integer \( {a}_{h} \) must be \( \geq  3 \) . For otherwise we would have a minimal geodesic. This proves the following (always for \( k \text{ ≢ } 2 \) (mod 4)):

Assertion 24.4. \( {K}_{A} \) has at least \( s - 1 \) eigenvalues which are \( \geq  {\left( 3 + 1\right) }^{2}/4 = 4 \) . The integer \( s = n/{m}_{k + 1} \) tends to infinity with \( n \) .

Now consider the geodesic \( t \mapsto  \mathrm{J}\exp \left( {\pi tA}\right) \) . Each eigenvalue \( {e}^{2} \) of \( {K}_{A} \) gives rise to conjugate points along this geodesic for \( t = {e}^{-1},2{e}^{-1},3{e}^{-1},\ldots \) by Theorem 20.5. Thus if \( {e}^{2} \geq  4 \) then one obtains at least one interior conjugate point. Applying the index theorem, this proves the following.

Assertion 24.5. The index of a non-minimal geodesic from \( \mathrm{J} \) to \( - \mathrm{J} \) in \( {\Omega }_{k}\left( n\right) \) is \( \geq  n/{m}_{k + 1} - 1 \) .

It follows that the inclusion map

\[
{\Omega }_{k + 1}\left( n\right)  \rightarrow  \Omega {\Omega }_{k}\left( n\right)
\]

induces isomorphisms of homotopy groups in dimensions \( \leq  n/{m}_{k + 1} - 3 \) . This number tends to infinity with \( n \) . Therefore, passing to the direct limit as \( n \rightarrow  \infty \) , it follows that the inclusion map \( \iota  : {\Omega }_{k + 1}\left( n\right)  \hookrightarrow  \Omega {\Omega }_{k}\left( n\right) \) induces isomorphisms of homotopy groups in all dimensions. But it can be shown that both \( {\Omega }_{k + 1} \) and a \( {\Omega }_{k} \) have the homotopy type of a CW-complex. Therefore, by Whitehead's theorem, it follows that \( i \) is a homotopy equivalence. This completes the proof of Theorem 24.8 providing that \( k \text{ ≢ } 2\left( {\;\operatorname{mod}\;4}\right) \) .

Proof of Theorem 24.8 for \( k \equiv  2\left( {\;\operatorname{mod}\;4}\right) \) . The difficulty in this case may be ascribed to the fact that \( {\Omega }_{k}\left( n\right) \) has an infinite cyclic fundamental group. Thus \( \Omega {\Omega }_{k}\left( n\right) \) has infinitely many components, while the approximating subspace \( {\Omega }_{k + 1}\left( n\right) \) has only finitely many.

To describe the fundamental group \( {\pi }_{1}{\Omega }_{k}\left( n\right) \) we construct a map

\[
f : {\Omega }_{k}\left( n\right)  \rightarrow  {\mathbb{S}}^{1} \subseteq  \mathbb{C}
\]

as follows. Let \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) be the fixed anti-commuting complex structure on \( {\mathbf{R}}^{n} \) . Make \( {\mathbf{R}}^{n} \) into an \( \left( {n/2}\right) \) -dimensional complex vector space by defining

\[
{iv} = {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}\ldots {\mathrm{J}}_{k - 1}v
\]

for \( v \in  {\mathbf{R}}^{n} \) ; where \( i = \sqrt{-1} \in  \mathbb{C} \) . The condition \( k \equiv  2\left( {\;\operatorname{mod}\;4}\right) \) guarantees that \( {i}^{2} =  - 1 \) , and that \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) commute with \( i \) .

Choose a base point \( \mathrm{J} \in  {\Omega }_{k}\left( n\right) \) . For any \( {\mathrm{J}}^{\prime } \in  {\Omega }_{k}\left( n\right) \) note that the composition \( {\mathrm{J}}^{-1}{\mathrm{\;J}}^{\prime } \) commutes with \( i \) . Thus \( {\mathrm{J}}^{-1}{\mathrm{\;J}}^{\prime } \) is a unitary complex linear transformation, and has a well defined complex determinant which will be denoted by \( f\left( {\mathrm{\;J}}^{\prime }\right) \) .

Now consider a geodesic

\[
t \mapsto  \mathrm{J}\exp \left( {\pi tA}\right)
\]

from \( \mathrm{J} \) to \( - \mathrm{J} \) in \( {\Omega }_{k}\left( n\right) \) . Since \( A \) commutes with \( i = {\mathrm{J}}_{1}{\mathrm{\;J}}_{2}\ldots {\mathrm{J}}_{k - 1} \) (compare Assertion 24.5 in the proof of Lemma 24.6) we may think of \( A \) also as a complex linear transformation. In fact \( A \) is skew-Hermitian; hence the trace of \( A \) is a pure imaginary number. Now

\[
f\left( {\mathrm{\;J}\exp \left( {\pi tA}\right) }\right)  = \det \left( {\exp \left( {\pi tA}\right) }\right)  = {\mathrm{e}}^{{\pi t}\operatorname{tr}A}.
\]

Thus \( f \) maps the given geodesic into a closed loop on \( {\mathbb{S}}^{1} \) which is completely determined by the trace of \( A \) . It follows that this trace is invariant under homotopy of the geodesic within the path space \( \Omega \left( {{\Omega }_{k}\left( n\right) ;\mathrm{J}, - \mathrm{J}}\right) \) .

The index \( \lambda \) of this geodesic can be estimated as follows. As before split \( {\mathbf{R}}^{n} \) into an orthogonal sum \( {M}_{1} \oplus  \cdots  \oplus  {M}_{r} \) where each \( {M}_{h} \) is closed under the action of \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1},\mathrm{\;J} \) , and \( A \) ; and is minimal. Thus for each \( h \) , the complex linear transformation \( {\left. A\right| }_{{M}_{h}} \) can have only one eigenvalue, say \( i{a}_{h} \) . For otherwise \( {M}_{h} \) would split into eigenspaces. Thus \( {\left. A\right| }_{{M}_{h}} \) coincides with \( {a}_{h}{\mathrm{\;J}}_{1}{\mathrm{\;J}}_{2}\ldots {\mathrm{J}}_{k - 1}{ \mid  }_{{M}_{h}} \) . Since \( {M}_{h} \) is minimal under the action of \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) , and \( \mathrm{J} \) ; its complex dimension is \( {m}_{k}/2 \) . Therefore the trace of \( A \) is equal to \( i\left( {{a}_{1} + \cdots  + {a}_{r}}\right) {m}_{k}/2 \) .

Now for each \( h \neq  j \) an eigenvector \( B \) of the linear transformation

\[
B \mapsto  {K}_{A}B = \frac{1}{4}\left( {-{A}^{2}B + {2ABA} - B{A}^{2}}\right)
\]

can be constructed much as before. Since \( {M}_{h} \) and \( {M}_{j} \) are \( \left( {{\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1},\mathrm{\;J}}\right) \) - minimal it follows from Lemma 24.11 that there exists an isometry

\[
{\left. B\right| }_{{M}_{h}} : {M}_{h} \rightarrow  {M}_{j}
\]

which commutes with \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{k - 1} \) and anti-commutes with \( \mathrm{J} \) . Let \( {\left. B\right| }_{{M}_{j}} \) be the negative adjoint of \( {\left. B\right| }_{{M}_{h}} \) ; and let \( {\left. B\right| }_{{M}_{\ell }} \) be zero for \( \ell  \neq  h, j \) . Then an easy computation shows that

\[
{K}_{A}B = \frac{{\left( {a}_{h} - {a}_{j}\right) }^{2}B}{4}.
\]

Thus for each \( {a}_{h} > {a}_{j} \) we obtain an eigenvalue \( {\left( {a}_{h} - {a}_{j}\right) }^{2}/4 \) for \( {K}_{A} \) . Since each such eigenvalue makes a contribution of \( \left( {{a}_{h} - {a}_{j}}\right) /2 - 1 \) towards the index \( \lambda \) , we obtain the inequality

\[
{2\lambda } \geq  \mathop{\sum }\limits_{{{a}_{h} > {a}_{j}}}\left( {{a}_{h} - {a}_{j} - 2}\right) .
\]

Now let us restrict attention to some fixed component of \( \Omega {\Omega }_{k}\left( n\right) \) . That is let us look only at matrices \( A \) such that \( \operatorname{tr}A = {ic}{m}_{k}/2 \) where \( c \) is some constant integer.

Thus the integers \( {a}_{1},\ldots ,{a}_{r} \) satisfy

(1) \( {a}_{1} \equiv  {a}_{2} \equiv  \ldots  \equiv  {a}_{r}\left( {\;\operatorname{mod}\;2}\right) \) ,(since \( \exp \left( {\pi A}\right)  =  - \mathrm{I} \) ),

(2) \( {a}_{1} + \cdots  + {a}_{r} = c \) , and

(3) \( \max \left| {a}_{h}\right|  \geq  3 \) (for a non-minimal geodesic).

Suppose for example that some \( {a}_{h} \) is equal to -3 . Let \( p \) be the sum of the positive \( {a}_{h} \) and \( - q \) the sum of the negative \( {a}_{h} \) . Thus

\[
p - q = c,\;p + q \geq  r,
\]

hence \( {2p} \geq  r + c \) . Now

hence \( {4\lambda } \geq  {2p} \geq  r + c \) ; where \( r = n/{m}_{k} \) tends to infinity with \( n \) . It follows that the component of \( \Omega {\Omega }_{k}\left( n\right) \) is approximated up to higher and higher dimensions by the corresponding component of \( {\Omega }_{k + 1}\left( n\right) \) , as \( n \rightarrow  \infty \) . Passing to the direct limit, we obtain a homotopy equivalence on each component. This completes the proof of Theorem 24.8.

Appendix
