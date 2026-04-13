# 16.4 Symmetric Functions

The following classical algebraic techniques will enable us to define and manipulate certain useful linear combinations of Chern numbers or Pontrjagin numbers.

Let \( {t}_{1},\ldots ,{t}_{n} \) be indeterminates. A polynomial function \( f\left( {{t}_{1},\ldots ,{t}_{n}}\right) \) , say with integer coefficients, is called a symmetric function if it is invariant under all permutations of \( {t}_{1},\ldots ,{t}_{n} \) . Thus the symmetric functions form a sub-ring

\[
\mathcal{S} \subset  \mathbb{Z}\left\lbrack  {{t}_{1},\ldots ,{t}_{n}}\right\rbrack
\]

A familiar and fundamental theorem asserts that \( \mathcal{S} \) itself is also a poly- nomial ring on \( n \) algebraically independent generators

\[
\mathcal{S} = \mathbb{Z}\left\lbrack  {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right\rbrack
\]

where \( {\sigma }_{k} = {\sigma }_{k}\left( {{t}_{1},\ldots ,{t}_{n}}\right) \) denotes the \( k \) -th elementary symmetric function, uniquely characterized by the fact that \( {\sigma }_{k} \) is a homogeneous polynomial of degree \( k \) in \( {t}_{1},\ldots ,{t}_{n} \) with

\[
1 + {\sigma }_{1} + {\sigma }_{2} + \ldots  + {\sigma }_{n} = \left( {1 + {t}_{1}}\right) \left( {1 + {t}_{2}}\right) \ldots \left( {1 + {t}_{n}}\right) .
\]

(Compare with the proof of Lemma 7.2.)

If we make \( \mathbb{Z}\left\lbrack  {{t}_{1},\ldots ,{t}_{n}}\right\rbrack \) into a graded ring by assigning each \( {t}_{i} \) the degree 1, then of course the symmetric functions form a graded subring \( {\mathcal{S}}^{ * } = \mathbb{Z}\left\lbrack  {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right\rbrack \) , where each \( {\sigma }_{k} \) has degree \( k \) . Thus a basis for the additive group \( {S}^{k} \) , consisting of homogeneous symmetric polynomials of degree \( k \) in \( {t}_{1},\ldots ,{t}_{n} \) , is given by the set of monomials

\[
{\sigma }_{{i}_{1}}\ldots {\sigma }_{{i}_{r}}
\]

where \( {i}_{1},\ldots ,{i}_{r} \) ranges over all partitions of \( k \) into integers \( \leq  n \) .

A different and quite useful basis can be constructed as follows. Define two monomials in \( {t}_{1},\ldots ,{t}_{n} \) to be equivalent if some permutation of \( {t}_{1},\ldots ,{t}_{n} \) transforms one into the other. Define \( \sum {t}_{1}^{{a}_{1}}\ldots {t}_{r}^{{a}_{r}} \) to be the summation of all monomials in \( {t}_{1},\ldots ,{t}_{n} \) which are equivalent to \( {t}_{1}^{{a}_{1}}\ldots {t}_{r}^{{a}_{r}} \) . As an example, using this notation we can write \( {\sigma }_{k} = \sum {t}_{1}{t}_{2}\ldots {t}_{k} \) .

Lemma 16.1. An additive basis for \( {\delta }^{k} \) , the group of homogeneous symmetric polynomials of degree \( k \) in \( {t}_{1},\ldots ,{t}_{n} \) , is given by the polynomials \( \sum {t}_{1}^{{a}_{1}}\ldots {t}_{r}^{{a}_{r}} \) . Here \( {a}_{1},\ldots ,{a}_{r} \) ranges over all partitions of \( k \) with length \( r \leq  n \) .

Proof. The proof is not difficult.

Now for any partition \( I = {i}_{1},\ldots ,{i}_{r} \) of \( k \) , define a polynomial \( {s}_{I} \) in \( k \) variables as follows. Choose \( n \geq  k \) so that the elementary symmetric functions \( {\sigma }_{1},\ldots ,{\sigma }_{k} \) of \( {t}_{1},\ldots ,{t}_{n} \) are algebraically independent, and let \( {s}_{I} = {s}_{{i}_{1},\ldots ,{i}_{r}} \) be the unique polynomial satisfying

\[
{s}_{I}\left( {{\sigma }_{1},\ldots ,{\sigma }_{k}}\right)  = \sum {t}_{1}^{{i}_{1}}\ldots {t}_{r}^{{i}_{r}}
\]

This polynomial does not depend on \( n \) , as one easily verifies by introducing additional variables \( {t}_{n + 1} = \ldots  = {t}_{{n}^{\prime }} = 0 \) . In fact, even if \( n < k \) the corresponding identity

\[
{s}_{I}\left( {{\sigma }_{1},\ldots ,{\sigma }_{n},0,\ldots ,0}\right)  = \sum {t}_{1}^{{i}_{1}}\ldots {t}_{r}^{{i}_{r}}
\]

remains valid, as one verifies by a similar argument.

If \( n \geq  k \) , then evidently the \( p\left( k\right) \) polynomials \( {s}_{I}\left( {{\sigma }_{1},\ldots ,{\sigma }_{k}}\right) \) are linearly independent, and form a basis for \( {\mathcal{S}}^{k} \) . The first twelve such polynomials are given by

\[
s\left( \right) \; = 1
\]

\[
{s}_{1}\left( {\sigma }_{1}\right) \; = {\sigma }_{1}
\]

\[
{s}_{3}\left( {{\sigma }_{1},{\sigma }_{2},{\sigma }_{3}}\right) \; = {\sigma }_{1}^{2}\; - 3{\sigma }_{1}{\sigma }_{2} + 3{\sigma }_{3}
\]

\[
{s}_{1,2}\left( {{\sigma }_{1},{\sigma }_{2},{\sigma }_{3}}\right) \; = \;{\sigma }_{1}{\sigma }_{2} - 3{\sigma }_{3}
\]

\[
{s}_{1,1,1}\left( {{\sigma }_{1},{\sigma }_{2},{\sigma }_{3}}\right)  =  + \; + {\sigma }_{3},
\]

\[
{s}_{2}\left( {{\sigma }_{1},{\sigma }_{2}}\right) \; = {\sigma }_{1}^{2}\; - 2{\sigma }_{2},
\]

\[
{s}_{1,1}\left( {{\sigma }_{1},{\sigma }_{2}}\right) \; = \; + {\sigma }_{2}
\]

<table><tr><td>\( {s}_{3} \)</td><td>\( = {\sigma }_{1}^{4} \)</td><td>\( - 4{\sigma }_{1}^{2}{\sigma }_{2} + 2{\sigma }_{2}^{2} \)</td><td>\( + 4{\sigma }_{1}{\sigma }_{3} - 4{\sigma }_{4}, \)</td></tr><tr><td>\( {s}_{1,3} \)</td><td>\( = \)</td><td>\( + {\sigma }_{1}^{2}{\sigma }_{2} - 2{\sigma }_{2}^{2} \)</td><td>\( - {\sigma }_{1}{\sigma }_{3} + 4{\sigma }_{4}, \)</td></tr><tr><td>\( {s}_{2,2} \)</td><td>\( = \)</td><td>\( + {\sigma }_{2}^{2} \)</td><td>\( - 2{\sigma }_{1}{\sigma }_{3} + 2{\sigma }_{4}, \)</td></tr><tr><td>\( {s}_{1,1,2} \)</td><td>\( = \)</td><td></td><td>\( + {\sigma }_{1}{\sigma }_{3} + 4{\sigma }_{4}, \)</td></tr><tr><td>\( {s}_{1,1,1,1} \)</td><td>\( = \)</td><td></td><td>\( + {\sigma }_{4} \) .</td></tr></table>

For further information see Problem 16-A, as well as [Wae70, Chapter 26, the exercises]and [Mac01] .

The application of these ideas to Chern classes or Pontrjagin classes is very similar to the application to Stiefel-Whitney classes in \( \text{ § }7 \) . Thus if a complex \( n \) -plane bundle \( \omega \) splits as a Whitney sum \( {\eta }_{1} \oplus  \ldots  \oplus  {\eta }_{n} \) of line bundles, then the formula

\[
1 + {\mathrm{c}}_{1}\left( \omega \right)  + \ldots  + {\mathrm{c}}_{n}\left( \omega \right)  = \left( {1 + {\mathrm{c}}_{1}\left( {\eta }_{1}\right) }\right) \ldots \left( {1 + {\mathrm{c}}_{1}\left( {\eta }_{n}\right) }\right)
\]

shows that the Chern class \( {\mathrm{c}}_{k}\left( \omega \right) \) can be identified with the k-th elementary symmetric function \( {\sigma }_{k}\left( {{\mathrm{c}}_{1}\left( {\eta }_{1}\right) ,\ldots ,{\mathrm{c}}_{1}\left( {\eta }_{n}\right) }\right) \) . The "universal" example of a Whitney sum of line bundles is provided by the \( n \) -fold cartesian product \( {\gamma }^{1} \times  \ldots  \times  {\gamma }^{1} \) over the product \( {\mathbb{P}}^{\infty }\left( \mathbb{C}\right)  \times  \ldots  \times  {\mathbb{P}}^{\infty }\left( \mathbb{C}\right) \) of complex projective spaces. Note that the cohomology ring of this product is a polynomial ring \( \mathbb{Z}\left\lbrack  {{a}_{1},\ldots ,{a}_{n}}\right\rbrack \) where each \( {a}_{i} \) has degree 2, and where

\[
\mathrm{c}\left( {{\gamma }^{1} \times  \ldots  \times  {\gamma }^{1}}\right)  = \left( {1 + {a}_{1}}\right) \ldots \left( {1 + {a}_{n}}\right)
\]

Since the elementary symmetric functions are algebraically independent, it follows that the cohomology \( {\mathrm{H}}^{ * }\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) of the classifying space maps isomorphically to the ring

\[
{\mathcal{S}}^{ * } \subset  \mathbb{Z}\left\lbrack  {{a}_{1},\ldots ,{a}_{n}}\right\rbrack
\]

of symmetric polynomials. (This is a theorem of [Bor53], Compare with the proof of Lemma 7.2) Thus our new basis for \( {\mathcal{S}}^{ * } \) gives rise to a new basis

\[
\left\{  {{s}_{I}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{k}}\right) }\right\}
\]

for the cohomology \( {\mathrm{H}}^{2k}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) .
