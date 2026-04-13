# 14.4 The Product Theorem for Chern Classes

Consider two complex vector bundles \( \omega \) and \( \phi \) over a common paracompact base space \( B \) . We want to prove the formula

\[
\mathrm{c}\left( {\omega  \oplus  \phi }\right)  = \mathrm{c}\left( \omega \right) \mathrm{c}\left( \phi \right) \tag{14.7}
\]

which expresses the total Chern class of a Whitney sum \( \omega  \oplus  \phi \) in terms of the total Chern classes of \( \omega \) and \( \phi \) . As a first step in this direction, we prove the following.

Lemma 14.8. There exists one and only one polynomial

\[
{p}_{m, n} = {p}_{m, n}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m};{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right)
\]

with integer coefficients in \( m + n \) indeterminates so that the identity

\[
\mathrm{c}\left( {\omega  \oplus  \phi }\right)  = {p}_{m, n}\left( {{\mathrm{c}}_{1}\left( \omega \right) ,\ldots ,{\mathrm{c}}_{m}\left( \omega \right) ;{\mathrm{c}}_{1}\left( \phi \right) ,\ldots ,{\mathrm{c}}_{n}\left( \phi \right) }\right)
\]

is valid for every complex \( m \) -plane bundle \( \omega \) and every complex n-plane bundle \( \phi \) over a common paracompact base space \( B \) .

Proof. As a universal model for pairs of complex vector bundles over a common base space we take the two vector bundles \( {\gamma }_{1}^{m} \) and \( {\gamma }_{2}^{n} \) over \( {\mathrm{{Gr}}}_{m} \times  {\mathrm{{Gr}}}_{n} \) constructed as follows. Let \( {\gamma }_{1}^{m} = {\pi }_{1}^{ * }\left( {\gamma }^{m}\right) \) where \( {\pi }_{1} : {\mathrm{{Gr}}}_{m} \times  {\mathrm{{Gr}}}_{n} \rightarrow  {\mathrm{{Gr}}}_{m} \) is the projection map to the first factor. Similarly let \( {y}_{2}^{n} = {\pi }_{2}^{ * }\left( {\gamma }^{n}\right) \) where \( {\pi }_{2} \) is the projection map to the second factor. Thus the Whitney sum \( {\gamma }_{1}^{m} \oplus  {\gamma }_{2}^{n} \) can be identified with the cartesian product bundle \( {\gamma }^{m} \times  {\gamma }^{n} \) .

We will make use of the fact that the external cohomology cross product operation

\[
a, b \mapsto  a \times  b = {\pi }_{1}^{ * }a \smile  {\pi }_{2}^{ * }b
\]

induces an isomorphism

\[
{\mathrm{H}}^{ * }\left( {\mathrm{{Gr}}}_{m}\right)  \otimes  {\mathrm{H}}^{ * }\left( {\mathrm{{Gr}}}_{n}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {{\mathrm{{Gr}}}_{m} \times  {\mathrm{{Gr}}}_{n}}\right)
\]

of integral cohomology. In fact, for the case of finite CW-complexes \( K \) and \( L \) with \( {\mathrm{H}}^{ * }\left( L\right) \) free abelian, the Künneth isomorphism \( {\mathrm{H}}^{ * }\left( K\right)  \otimes  {\mathrm{H}}^{ * }\left( L\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{H}}^{ * }\left( {K \times  L}\right) \) is established in Appendix A. The corresponding assertion for our infinite CW-complexes’ \( {\mathrm{{Gr}}}_{m} \) and \( {\mathrm{{Gr}}}_{n} \) follows immediately, since each skeleton of \( {\mathrm{{Gr}}}_{m} \) or \( {\mathrm{{Gr}}}_{n} \) is finite.

Therefore \( {\mathrm{H}}^{ * }\left( {{\mathrm{{Gr}}}_{m} \times  {\mathrm{{Gr}}}_{n}}\right) \) is a polynomial ring over \( \mathbb{Z} \) on the algebraically independent generators

\[
{\pi }_{1}^{ * }{\mathrm{c}}_{i}\left( {\gamma }^{m}\right)  = {\mathrm{c}}_{i}\left( {\gamma }_{1}^{m}\right) ,\;1 \leq  i \leq  m
\]

and

\[
{\pi }_{2}^{ * }{\mathrm{c}}_{j}\left( {\gamma }^{n}\right)  = {\mathrm{c}}_{j}\left( {\gamma }_{2}^{n}\right) ,\;1 \leq  j \leq  n.
\]

Hence the total Chern class of \( {\gamma }_{1}^{m} \oplus  {\gamma }_{2}^{n} \) can be expressed uniquely as a polynomial

\[
\mathrm{c}\left( {{\gamma }_{1}^{m} \oplus  {\gamma }_{2}^{n}}\right)  = {p}_{m, n}\left( {{\mathrm{c}}_{1}\left( {\gamma }_{1}^{m}\right) ,\ldots ,{\mathrm{c}}_{m}\left( {\gamma }_{1}^{m}\right) ;{\mathrm{c}}_{1}\left( {\gamma }_{2}^{n}\right) ,\ldots ,{\mathrm{c}}_{n}\left( {\gamma }_{2}^{n}\right) }\right) .
\]

Now if \( \omega \) is a complex \( m \) -plane bundle over \( B \) and \( \phi \) is a complex n-plane bundle over \( B \) , we can choose maps \( f : B \rightarrow  {\mathrm{{Gr}}}_{m} \) and \( g : B \rightarrow  {\mathrm{{Gr}}}_{n} \) so that

\[
{f}^{ * }\left( {\gamma }^{m}\right)  \cong  \omega ,{g}^{ * }\left( {\gamma }^{n}\right)  \cong  \phi .
\]

Defining the map \( h : B \rightarrow  {\mathrm{{Gr}}}_{m} \times  {\mathrm{{Gr}}}_{n} \) by \( h\left( b\right)  = \left( {f\left( b\right) , g\left( b\right) }\right) \) , note that the following diagram is commutative.

![bo_d7du9galb0pc73deir9g_170_437_589_665_250_0.jpg](images/bo_d7du9galb0pc73deir9g_170_437_589_665_250_0.jpg)

It follows that

\[
{h}^{ * }\left( {\gamma }_{1}^{m}\right)  \cong  \omega ,{h}^{ * }\left( {\gamma }_{2}^{n}\right)  \cong  \phi
\]

and hence

\[
\mathrm{c}\left( {\omega  \oplus  \phi }\right)  = {h}^{ * }\mathrm{c}\left( {{\gamma }_{1}^{m} \oplus  {\gamma }_{2}^{n}}\right)
\]

\[
= {p}_{m, n}\left( {{\mathrm{c}}_{1}\left( \omega \right) ,\ldots ,{\mathrm{c}}_{m}\left( \omega \right) ;{\mathrm{c}}_{1}\left( \phi \right) ,\ldots ,{\mathrm{c}}_{n}\left( \phi \right) }\right)
\]

as required.

To actually compute these polynomials \( {p}_{m, n} \) we proceed by induction on \( m + n \) as follows. Suppose inductively that \( \mathrm{c}\left( {{\gamma }_{1}^{m - 1} \oplus  {\gamma }_{2}^{n}}\right) \) is equal to

\[
\left( {1 + {\mathrm{c}}_{1}\left( {\gamma }_{1}^{m - 1}\right)  + \ldots  + {\mathrm{c}}_{m - 1}\left( {\gamma }_{1}^{m - 1}\right) }\right) \left( {1 + {\mathrm{c}}_{1}\left( {\gamma }_{2}^{n}\right)  + \ldots  + {\mathrm{c}}_{n}\left( {\gamma }_{2}^{n}\right) }\right) .
\]

Consider the two vector bundles \( {\gamma }_{1}^{m - 1} \oplus  {\varepsilon }^{1} \) and \( {\gamma }_{2}^{n} \) over \( {\operatorname{Gr}}_{m - 1} \times  {\operatorname{Gr}}_{n} \) , where \( {\varepsilon }^{1} \) is a trivial line bundle. By 14.8 we have

\[
\mathrm{c}\left( {{\gamma }_{1}^{m - 1} \oplus  {\varepsilon }^{1} \oplus  {\gamma }_{2}^{n}}\right)  = {p}_{m, n}\left( {{\mathrm{c}}_{1}\left( {{\gamma }_{1}^{m - 1} \oplus  {\varepsilon }^{1}}\right) ,\ldots ,{\mathrm{c}}_{m}\left( {{\gamma }_{1}^{m - 1} \oplus  {\varepsilon }^{1}}\right) ;{\mathrm{c}}_{1}\left( {\gamma }_{2}^{n}\right) ,\ldots ,{\mathrm{c}}_{n}\left( {\gamma }_{2}^{n}\right) }\right)
\]

But according to 14.3 the \( {\varepsilon }^{1} \) summand can always be ignored, so we have the alternative formula

\[
\mathrm{c}\left( {{\gamma }_{1}^{m - 1} \oplus  {\gamma }_{2}^{n}}\right)  = \mathrm{c}\left( {{\gamma }_{1}^{m - 1} \oplus  {\varepsilon }^{1} \oplus  {\gamma }_{2}^{n}}\right)
\]

\[
= {p}_{m, n}\left( {{\mathrm{c}}_{1}\left( {\gamma }_{1}^{m - 1}\right) ,\ldots ,{\mathrm{c}}_{m - 1}\left( {\gamma }_{1}^{m - 1}\right) ,0;{\mathrm{c}}_{1}\left( {\gamma }_{2}^{n}\right) ,\ldots ,{\mathrm{c}}_{n}\left( {\gamma }_{2}^{n}\right) }\right) .
\]

Comparing the induction hypothesis, and substituting indeterminates \( {\mathrm{c}}_{i} \) and \( {\mathrm{c}}_{j}^{\prime } \) for the algebraically independent elements \( {\mathrm{c}}_{i}\left( {\gamma }_{1}^{m - 1}\right) \) and \( {\mathrm{c}}_{j}\left( {\gamma }_{2}^{n}\right) \) , this yields

\[
{p}_{m, n}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m - 1},0;{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right)  = \left( {1 + {\mathrm{c}}_{1} + \ldots  + {\mathrm{c}}_{m - 1}}\right) \left( {1 + {\mathrm{c}}_{1}^{\prime } + \ldots  + {\mathrm{c}}_{n}^{\prime }}\right)
\]

Introducing a new indeterminate \( {\mathrm{c}}_{m} \) , it follows that the congruence

\[
{p}_{m, n}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m};{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right)  \equiv  \left( {1 + {\mathrm{c}}_{1} + \ldots  + {\mathrm{c}}_{m}}\right) \left( {1 + {\mathrm{c}}_{1}^{\prime } + \ldots  + {\mathrm{c}}_{n}^{\prime }}\right) \;\left( {\;\operatorname{mod}\;{\mathrm{c}}_{m}}\right)
\]

is valid in the polynomial ring \( \mathbb{Z}\left\lbrack  {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m},{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right\rbrack \) . A similar inductive argument shows that these two polynomials are congruent modulo \( {\mathrm{c}}_{n}^{\prime } \) . Since \( \mathbb{Z}\left\lbrack  {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m},{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right\rbrack \) is a unique factorization domain, it follows that they are congruent modulo the product \( {\mathrm{c}}_{m}{\mathrm{c}}_{n}^{\prime } \) ; that is

\[
{p}_{m, n}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{m};{\mathrm{c}}_{1}^{\prime },\ldots ,{\mathrm{c}}_{n}^{\prime }}\right)  = \left( {1 + {\mathrm{c}}_{1} + \ldots  + {\mathrm{c}}_{m}}\right) \left( {1 + {\mathrm{c}}_{1}^{\prime } + \ldots  + {\mathrm{c}}_{n}^{\prime }}\right)  + u{\mathrm{c}}_{m}{\mathrm{c}}_{n}^{\prime }
\]

for some polynomial \( u \) . Here \( u \) must be zero dimensional, hence an integer, since otherwise the whitney sum \( {\gamma }_{1}^{m} \oplus  {\gamma }_{2}^{n} \) would have non-zero Chern classes in dimensions greater than \( 2\left( {m + n}\right) \) .

But the top Chern class \( {\mathrm{c}}_{m + n}\left( {\omega  \oplus  \phi }\right) \) can be identified with the Euler class

\[
\mathrm{e}\left( {\left( \omega  \oplus  \phi \right) }_{\mathbb{R}}\right)  = \mathrm{e}\left( {{\omega }_{\mathbb{R}} \oplus  {\phi }_{\mathbb{R}}}\right) ,
\]

and hence is equal to the product \( {\mathrm{c}}_{m}\left( \omega \right) {\mathrm{c}}_{n}\left( \phi \right) \) . (Compare 9.6 and the discussion following 14.1.) Therefore the coefficient \( u \) must be zero, and we have proved the product formula 14.7.
