# 20.1 The Differentiable Case

In order to motivate the combinatorial definition, we will first give a new interpretation for the classes \( {L}_{i}\left( {{p}_{1},\ldots ,{p}_{i}}\right) \) of a smooth \( n \) -manifold. The restriction \( {4i} < \left( {n - 1}\right) /2 \) will be needed at first.

Let \( {M}^{n} \) be a smooth, compact \( n \) -dimensional manifold, and let \( f : {M}^{n} \rightarrow  {S}^{n - {4i}} \) be a smooth (i.e., infinitely differentiable) map.

Lemma 20.1. There exists a dense open subset of \( {S}^{n - {4i}} \) consisting of points \( y \) such that the inverse image \( {f}^{-1}\left( y\right) \) is a smooth \( {4i} \) -dimensional manifold with trivial normal bundle in \( {M}^{n} \) .

Proof. By the theorem of Brown and Sard (Section 18), the set of regular values of \( f \) is everywhere dense in \( {S}^{n - {4i}} \) . This set is open since it is the complement of the continuous image of a compact subset of \( {M}^{n} \) . For every regular value \( y \) , the inverse image \( {f}^{-1}\left( y\right) \) is smooth, compact, and has normal bundle which is trivial, since it is induced from the normal bundle of \( y \) in \( {S}^{n - {4i}} \) .

Now suppose that \( {M}^{n} \) is an oriented manifold. Then the orientations of \( {M}^{n} \) and \( {S}^{n - {4i}} \) determines an orientation for \( {f}^{-1}\left( y\right) \) , using the Whitney sum decomposition \( {\tau }^{4i}\left( {{f}^{-1}\left( y\right) }\right)  \oplus  {\nu }^{n - {4i}} = {\left. {\tau }^{n}\right| }_{{f}^{-1}\left( y\right) } \) .

Let \( u \) and \( {\mu }_{n} \) denote the standard generators of \( {\mathrm{H}}^{k}\left( {{S}^{k};\mathbb{Z}}\right) \) and \( {\mathrm{H}}_{n}\left( {{M}_{n};\mathbb{Z}}\right) \) respectively, and let \( {\tau }^{n} \) denote the tangent bundle of \( {M}^{n} \) . The class \( {L}_{i}\left( {{p}_{1}\left( {\tau }^{n}\right) ,\ldots ,{p}_{i}\left( {\tau }^{n}\right) }\right)  \in  {\mathrm{H}}^{4i}\left( {{M}^{n};\mathbb{Q}}\right) \) will be briefly written as \( {L}_{i}\left( {\tau }^{n}\right) \) .

Lemma 20.2. For every smooth map \( f : {M}^{n} \rightarrow  {S}^{n - {4i}} \) and every regular value \( y \) , the Kronecker index

\[
\left\langle  {{L}_{i}\left( {\tau }^{n}\right)  \smile  {f}^{ * }\left( u\right) ,{\mu }_{n}}\right\rangle
\]

is equal to the signature \( \sigma \) of the manifold \( {M}^{4i} = {f}^{-1}\left( y\right) \) . In the case \( {4i} < \left( {n - 1}\right) /2 \) , the class \( {L}_{i}\left( {\tau }^{n}\right) \) is completely characterized by these identities.

Proof. Let \( {\tau }^{4i} \) be the tangent bundle of \( {M}^{4i} \) , and \( j : {M}^{4i} \rightarrow  {M}^{n} \) the inclusion map. Then \( j \) is covered by a bundle map \( {\tau }^{4i} \oplus  {\nu }^{n - {4i}} \rightarrow  {\tau }^{n} \) . Since the normal bundle \( {\nu }^{n - {4i}} \) is trivial, this means that \( {L}_{i}\left( {\tau }^{4i}\right) \) is equal to \( {j}^{ * }{L}_{i}\left( {\tau }^{n}\right) \) . Hence the signature

\[
\sigma \left( {M}^{4i}\right)  = \left\langle  {{L}_{i}\left( {\tau }^{4i}\right) ,{\mu }_{4i}}\right\rangle   = \left\langle  {{j}^{ * }{L}_{i}\left( {\tau }^{n}\right) ,{\mu }_{4i}}\right\rangle
\]

is equal to \( \left\langle  {{L}_{i}\left( {\tau }^{n}\right) ,{j}_{ * }\left( {\mu }_{4i}\right) }\right\rangle \) .

Now consider the cohomology class \( {f}^{ * }\left( u\right)  \in  {\mathrm{H}}^{n - {4i}}\left( {{M}^{n};\mathbb{Z}}\right) \) . Using the commutative diagram

![bo_d7du9galb0pc73deir9g_234_390_272_751_250_0.jpg](images/bo_d7du9galb0pc73deir9g_234_390_272_751_250_0.jpg)

we see easily that \( {f}^{ * }\left( u\right) \) can be identified with the "dual cohomology class" (p. 127) to the submanifold \( {M}^{4i} \subset  {M}^{n} \) .

We will make use of the Poincaré duality isomorphism \( a \mapsto  a \cap  {\mu }_{n} \) from \( {\mathrm{H}}^{n - {4i}}\left( {M}^{n}\right) \) to \( {\mathrm{H}}_{4i}\left( {M}^{n}\right) \) , defined by means of the cap product operation. (See Appendix A.10.) According to Problem 11-C, this isomorphism maps the dual cohomology class \( {f}^{ * }\left( u\right) \) to the homology class \( {j}_{ * }\left( {\mu }_{4i}\right) \) . Hence the signature \( \left\langle  {{L}_{i}\left( {\tau }^{n}\right) ,{j}_{ * }\left( {\mu }_{4i}\right) }\right\rangle \) is equal to

\[
\left\langle  {{L}_{i}\left( {\tau }^{n}\right) ,{f}^{ * }\left( u\right)  \cap  {\mu }_{n}}\right\rangle   = \left\langle  {{L}_{i}\left( {\tau }^{n}\right)  \smile  {f}^{ * }\left( u\right) ,{\mu }_{n}}\right\rangle  .
\]

This proves the first half of Lemma 20.2.

To prove the second half, we will make use of a theorem of [Ser53, p. 289] concerning the Borsuk-Spanier cohomology groups. If \( n < {2k} - 1 \) , then the set of all homotopy classes of maps \( f : {M}^{n} \rightarrow  {S}^{k} \) forms an abelian group, denoted by \( {\pi }^{k}\left( {M}^{n}\right) \) and called the \( k \) -th cohomotopy group of \( {M}^{n} \) . Serre shows that the correspondence \( f \mapsto  {f}^{ * }\left( u\right) \) induces a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism

\[
{\pi }^{k}\left( {M}^{n}\right)  \rightarrow  {\mathrm{H}}^{k}\left( {{M}^{n};\mathbb{Z}}\right) .
\]

(Compare §18.2. This result is the Spanier-Whitehead dual of Theorem 18.3.) In particular, the images \( {f}^{ * }\left( u\right) \) generate a subgroup of finite index in \( {\mathrm{H}}^{k}\left( {{M}^{n};\mathbb{Z}}\right) \) . Now substitute \( k = n - {4i} \) , so that the dimensional restriction \( n < {2k} - 1 \) takes the form \( {4i} < \left( {n - 1}\right) /2 \) . If this restriction is satisfied, then by Poincaré duality (Theorem 11.10), the rational cohomology group \( {L}_{i}\left( {\tau }^{n}\right) \) is completely determined by the set of all Kronecker indices \( \left\langle  {{L}_{i}\left( {\tau }^{n}\right)  \smile  {f}^{ * }\left( u\right) ,{\mu }_{n}}\right\rangle \) .

Remark. As a method for computing \( {L}_{i}\left( {\tau }^{n}\right) \) , Theorem 20.2 is probably hopeless. However the statement that \( \left\langle  {{L}_{i}\left( {\tau }^{n}\right)  \smile  {f}^{ * }\left( u\right) ,{\mu }_{n}}\right\rangle \) is an integer for every \( \left( f\right)  \in  {\pi }^{n - {4i}}\left( {M}^{n}\right) \) could conceivably prove useful in computing cohomotopy groups.

As an example, for the complex projective space \( {\mathbb{P}}^{m}\left( \mathbb{C}\right) \) , the class \( L\left( {\tau }^{2m}\right) \) is equal to

\[
{\left( \frac{a}{\tanh \left( a\right) }\right) }^{m + 1} = 1 + \frac{m + 1}{3}{a}^{2} + \frac{5{m}^{2} + {3m} - 2}{90}{a}^{4} + \ldots
\]

Thus if \( m \text{ ≢ } 2\left( {\;\operatorname{mod}\;3}\right) \) it follows that the image of the homomorphism

\[
{\pi }^{{2m} - 4}\left( {{\mathbb{P}}^{m}\left( \mathbb{C}\right) }\right)  \rightarrow  {\mathrm{H}}^{{2m} - 4}\left( {{\mathbb{P}}^{m}\left( \mathbb{C}\right) }\right)
\]

is divisible by 3, while if \( m \equiv  0\left( {\;\operatorname{mod}\;3}\right) \) the image of

\[
{\pi }^{{2m} - 8}\left( {{\mathbb{P}}^{m}\left( \mathbb{C}\right) }\right)  \rightarrow  {\mathrm{H}}^{{2m} - 8}\left( {{\mathbb{P}}^{m}\left( \mathbb{C}\right) }\right)
\]

is divisible by 9 , and so on.
