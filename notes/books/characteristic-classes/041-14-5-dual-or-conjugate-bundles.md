# 14.5 Dual or Conjugate Bundles

If \( \omega \) is a complex vector bundle, the conjugate bundle \( \overline{\omega } \) is defined to be the complex vector bundle with the same underlying real vector bundle

\[
{\omega }_{\mathbb{R}} = {\overline{\omega }}_{\mathbb{R}},
\]

but with the "opposite" complex structure. Thus, the identity map \( f : E\left( \omega \right)  \rightarrow  E\left( \overline{\omega }\right) \) is conjugate linear,

\[
f\left( {\lambda e}\right)  = \overline{\lambda }f\left( e\right)
\]

for every complex number \( \lambda \) and every \( e \in  E\left( \omega \right) \) . Here \( \overline{\lambda } \) is the complex conjugate of \( \lambda \) . In particular, it follows that \( f\left( {ie}\right)  =  - {if}\left( e\right) \) .

As an example, consider the tangent bundle \( {\tau }^{1} \) of the complex manifold \( {\mathbb{P}}^{1}\left( \mathbb{C}\right) \) .(Ignoring the complex structure, this is jut the tangent bundle of the 2- sphere). This bundle \( {\tau }^{1} \) is not isomorphic to its conjugate tangent bundle \( {\overline{\tau }}^{1} \) . For any isomorphism \( {\tau }^{1} \rightarrow  {\overline{\tau }}^{1} \) would have to map each tangent plane of the 2- sphere onto itself so as to reverse the complex structure (rotation by \( i \) ). Clearly any such map is obtained by reflection in some uniquely defined line in the plane. But we have seen in 9.3 that the 2-sphere does not admit any continuous field of tangent lines.

The chern class of a conjugate bundle can be computed as follows.

Lemma 14.9. The Chern class \( {\mathrm{c}}_{k}\left( \overline{\omega }\right) \) is equal to \( {\left( -1\right) }^{k}{\mathrm{c}}_{k}\left( \omega \right) \) . Hence

\[
\mathrm{c}\left( \overline{\omega }\right)  = 1 - {\mathrm{c}}_{1}\left( \omega \right)  + {\mathrm{c}}_{2}\left( \omega \right)  - \cdots  \pm  {\mathrm{c}}_{n}\left( \omega \right)
\]

Proof. For any fiber \( F \) of \( \omega \) , choose a basis \( {v}_{1},\ldots ,{v}_{n} \) for \( F \) over \( \mathbb{C} \) . Then the basis \( {v}_{1}, i{v}_{1},\ldots ,{v}_{n}, i{v}_{n} \) for the underlying real vector space \( {F}_{\mathbb{R}} \) determines the preferred orientation for \( {F}_{\mathbb{R}} \) . Similarly the basis \( {v}_{1}, - i{v}_{1},\ldots ,{v}_{n}, - i{v}_{n} \) determines the preferred orientation for the conjugate vector space. Thus the two oriented real vector bundles \( {\omega }_{\mathbb{R}} \) and \( \left( {\overline{\omega }}_{\mathbb{R}}\right. \) have the same orientation if \( n \) is even, but the opposite orientation if \( n \) is odd. It follows immediately that the top Chern class

\[
{\mathrm{c}}_{n}\left( \omega \right)  = \mathrm{e}\left( {\omega }_{\mathbb{R}}\right)
\]

is equal to \( {\left( -1\right) }^{n}{\mathrm{c}}_{n}\left( \overline{\omega }\right) \) . To compute \( {\mathrm{c}}_{k}\left( \overline{\omega }\right) \) for \( k < n \) , we recall the definition \( {\mathrm{c}}_{k}\left( \omega \right)  = {\pi }_{0}^{* - 1}{\mathrm{c}}_{k}\left( {\omega }_{0}\right) \) where \( {\omega }_{0} \) is a canonical \( \left( {n - 1}\right) \) -plane bundle over the space \( {E}_{0} \subset  E\left( \omega \right) \) . It is easy to check that the conjugate bundle \( \overline{\left( {\omega }_{0}\right) } \) is canonically isomorphic to \( {\left( \overline{\omega }\right) }_{0} \) , so a straightforward induction shows that

\[
{\mathrm{c}}_{k}\left( \overline{\omega }\right)  = {\left( -1\right) }^{k}{\mathrm{c}}_{k}\left( \omega \right)
\]

for all \( \mathrm{k} \)

Closely related to the conjugate bundle \( \overline{\omega } \) is the dual bundle \( {\operatorname{Hom}}_{\mathbb{C}}\left( {\omega ,\mathbb{C}}\right) \) . By definition this is the complex vector bundle over the same base space whose typical fiber is equal to the dual \( {\operatorname{Hom}}_{\mathbb{C}}\left( {F,\mathbb{C}}\right) \) of the corresponding fiber \( F \) of \( \omega \) . (compare the analogous discussion for the real vector bundles on p. 39) To simplify the notation, we will usually omit the subscript \( \mathbb{C} \) .

If the complex vector bundle \( \omega \) possesses a Hermitian metric, not that its dual bundle \( \operatorname{Hom}\left( {\omega ,\mathbb{C}}\right) \) is canonically isomorphic to the conjugate bundle \( \overline{\omega } \) . For if we are given a Hermitian inner product

\[
\left\langle  {{v}_{1},{v}_{2}}\right\rangle   \in  \mathbb{C}
\]

on the typical fiber \( F \) , linear in the first variable and conjugate linear in the second, then the correspondence

\[
{v}_{2} \mapsto  \left\langle  {-,{v}_{2}}\right\rangle
\]

maps the conjugate vector space \( \bar{F} \) isomorphically to the dual vector space \( \operatorname{Hom}\left( {F,\mathbb{C}}\right) \) .
