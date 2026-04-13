# 14 Chern Classes

We will first prove the following statement.

Lemma 14.1. If \( \omega \) is a complex vector bundle, then the underlying real vector bundle \( {\omega }_{\mathbb{R}} \) has a canonical preferred orientation.

Applying this lemma to the special case of a tangent bundle, it follows that any complex manifold has a canonical preferred orientation. For we have seen on Lemma 11.6 that every orientation for the tangent bundle of a manifold gives rise to a unique orientation of the manifold.

Proof of 14.1. Let \( V \) be any finite dimensional complex vector space. Choosing a basis \( {a}_{1},\ldots ,{a}_{n} \) for \( V \) over \( \mathbb{C} \) , note that the vectors \( {a}_{1}, i{a}_{1},{a}_{2}, i{a}_{2},\ldots ,{a}_{n}, i{a}_{n} \) form a real basis for the underlying real vector space \( {V}_{\mathbb{R}} \) . This ordered basis determines the required orientation for \( {V}_{\mathbb{R}} \) . To show that this orientation does not depend on the choice of complex basis, we need only note that the linear group \( {\mathrm{{GL}}}_{n}\left( \mathbb{C}\right) \) is connected. Hence we can pass from any given complex basis to any other complex basis by a continuous deformation, which cannot alter the induced orientation.

Now if \( \omega \) is a complex vector bundle, then applying this construction to every fiber of \( \omega \) , we obtain the required orientation for \( {\omega }_{\mathbb{R}} \) .

As an application of 14.1, for any complex \( n \) -plane bundle \( \omega \) over the base space \( B \) , note that the Euler class

\[
\mathrm{e}\left( {\omega }_{\mathbb{R}}\right)  \in  {\mathrm{H}}^{2n}\left( {B;\mathbb{Z}}\right)
\]

is well-defined. If \( {\omega }^{\prime } \) is a complex \( m \) -plane bundle over the same base space \( B \) , note that

\[
\mathrm{e}\left( {\left( \omega  \oplus  {\omega }^{\prime }\right) }_{\mathbb{R}}\right)  = \mathrm{e}\left( {\omega }_{\mathbb{R}}\right) \mathrm{e}\left( {\omega }_{\mathbb{R}}^{\prime }\right) .
\]

For if \( {a}_{1},\ldots ,{a}_{n} \) is a basis for a fiber \( F \) for \( \omega \) , and \( {b}_{1},\ldots ,{b}_{m} \) is a basis for the corresponding fiber \( {F}^{\prime } \) of \( {\omega }^{\prime } \) , then the preferred orientation \( {a}_{1}, i{a}_{1},\ldots ,{a}_{n}, i{a}_{n} \) for \( {F}_{\mathbb{R}} \) followed by the preferred orientation \( {b}_{1}, i{b}_{1},\ldots ,{b}_{m}, i{b}_{m} \) for \( {F}_{\mathbb{R}}^{\prime } \) yields the preferred orientation \( {a}_{1}, i{a}_{1},\ldots , i{a}_{n},{b}_{1}, i{b}_{1},\ldots , i{b}_{m} \) for \( {\left( F \oplus  {F}^{\prime }\right) }_{\mathbb{R}} \) . Thus \( {\omega }_{\mathbb{R}} \oplus  {\omega }_{\mathbb{R}}^{\prime } \) is isomorphic as an oriented bundle to \( {\left( \omega  \oplus  {\omega }^{\prime }\right) }_{\mathbb{R}} \) , and the conclusion follows.
