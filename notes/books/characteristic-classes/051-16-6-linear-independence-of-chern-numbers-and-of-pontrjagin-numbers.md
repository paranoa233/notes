# 16.6 Linear Independence of Chern Numbers and of Pontrjagin Numbers

The following basic result shows that there are no linear relations between Chern numbers.

Theorem 16.7 (Thom). Let \( {K}^{1},\ldots ,{K}^{n} \) be complex manifolds with \( {s}_{k}\left( \mathrm{c}\right) \left\lbrack  {K}^{k}\right\rbrack   \neq  0 \) . Then the \( p\left( n\right)  \times  p\left( n\right) \) matrix

\[
\left\lbrack  {{\mathrm{c}}_{{i}_{1}}\ldots {\mathrm{c}}_{{i}_{r}}\left\lbrack  {{K}^{{j}_{1}} \times  \ldots  \times  {K}^{{j}_{s}}}\right\rbrack  }\right\rbrack  ,
\]

of Chern numbers, where \( {i}_{1},\ldots ,{i}_{r} \) and \( {j}_{1},\ldots ,{j}_{s} \) range over all partitions of \( n \) , is non-singular.

For example, by 16.6, we can take \( {K}^{r} = {\mathbb{P}}^{r}\left( \mathbb{C}\right) \) . Similarly:

Theorem 16.8 (Thom). If \( {M}^{4},\ldots ,{M}^{4n} \) are oriented manifolds with \( {s}_{k}\left( \mathrm{p}\right) \left\lbrack  {M}^{4k}\right\rbrack   \neq \) 0, then the \( \mathrm{p}\left( n\right)  \times  \mathrm{p}\left( n\right) \) matrix

\[
\left\lbrack  {{\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {{M}^{4{j}_{1}} \times  \ldots  \times  {M}^{4{j}_{s}}}\right\rbrack  }\right\rbrack
\]

of Pontrjagin numbers is non-singular.

Again we can take the complex projective space \( {\mathbb{P}}^{2k}\left( \mathbb{C}\right) \) , with \( \mathrm{p}\left( {\tau }_{{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right)  = \; {\left( 1 + {a}^{2}\right) }^{{2k} + 1} \) and hence

\[
{s}_{k}\left( \mathrm{p}\right) \left\lbrack  {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right\rbrack   = {2k} + 1
\]

as a suitable manifold \( {M}^{4k} \) .

Here is an example. For complex dimension 2 taking \( {K}^{n} = {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) we obtain the matrix

\[
\left\lbrack  \begin{array}{rr} {\mathrm{c}}_{1}{\mathrm{c}}_{1}\left\lbrack  {{K}^{1} \times  {K}^{1}}\right\rbrack   = 8 & {\mathrm{c}}_{1}{\mathrm{c}}_{1}\left\lbrack  {K}^{2}\right\rbrack   = 9 \\  {\mathrm{c}}_{2}\left\lbrack  {{K}^{1} \times  {K}^{1}}\right\rbrack   = 4 & {\mathrm{c}}_{2}\left\lbrack  {K}^{2}\right\rbrack   = 3 \end{array}\right\rbrack
\]

of Chern numbers, with determinant -12. Evidently the direct approach of simply computing the matrix will not help much in the general case.

proof of 16.7. In place of the Chern numbers themselves, we may use the linear combinations \( {s}_{I}\left( \mathrm{c}\right) \) . As an immediate generalization of 16.4 we have

\[
{s}_{I}\left\lbrack  {{K}^{{j}_{1}} \times  \ldots  \times  {K}^{{j}_{q}}}\right\rbrack   = \mathop{\sum }\limits_{{{I}_{1}\ldots {I}_{q} = I}}{s}_{{I}_{1}}\left\lbrack  {K}^{{j}_{1}}\right\rbrack  \ldots {s}_{{I}_{q}}\left\lbrack  {K}^{{j}_{q}}\right\rbrack  ,.
\]

to be summed over all partitions \( {I}_{1} \) of \( {j}_{1},{I}_{2} \) of \( {j}_{2},\ldots \) , and \( {I}_{q} \) of \( {j}_{q} \) with juxtaposition \( {I}_{1}\ldots {I}_{q} \) equal to \( I \) . Thus the characteristic number \( {s}_{I}\left\lbrack  {{K}^{{j}_{1}} \times  \ldots  \times  {K}^{{j}_{q}}}\right\rbrack \) is zero unless the partition \( I = {i}_{1},\ldots ,{i}_{r} \) is a refinement of \( {j}_{1},\ldots ,{j}_{q} \) , In particular it is zero unless \( r \geq  q \) . Thus if the partitions \( {i}_{1},\ldots ,{i}_{r} \) and \( {j}_{1},\ldots ,{j}_{q} \) are arranged in a suitably chosen order, then the matrix

\[
\left\lbrack  {{s}_{{i}_{1},\ldots ,{i}_{r}}\left\lbrack  {{K}^{{j}_{1}} \times  \ldots  \times  {K}^{{j}_{q}}}\right\rbrack  }\right\rbrack
\]

will be triangular, with zeros everywhere above the diagonal. Each diagonal entry \( {s}_{{i}_{1},\ldots ,{i}_{r}}\left\lbrack  {{K}^{{i}_{1}} \times  \ldots  \times  {K}^{i}}\right\rbrack \) is clearly equal to the product

\[
{s}_{{i}_{1}}\left\lbrack  {K}^{{i}_{1}}\right\rbrack  \ldots {s}_{{i}_{r}}\left\lbrack  {K}^{ii}\right\rbrack   \neq  0
\]

Hence the matrix is non-singular. The proof of 16.8 is completely analogous.

Here are some problems for the reader.

Problem 16-A. Substituting \( - {t}_{i} \) for \( x \) in the identity

\[
\left( {x + {t}_{1}}\right) \ldots \left( {x + {t}_{n}}\right)  = {x}^{n} + {\sigma }_{1}{x}^{n - 1} + \ldots  + {\sigma }_{n}
\]

and then summing over \( i \) , prove Newton’s formula

\[
{s}_{n} - {\sigma }_{1}{s}_{n - 1} + {\sigma }_{2}{s}_{n - 2} - \cdots  \mp  {\sigma }_{n - 1}{s}_{1} \pm  n{\sigma }_{n} = 0.
\]

This formula can be used inductively to compute the polynomial \( {s}_{n}\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \) . Alternatively, taking the logarithm of both sides of the identity

\[
\left( {1 + {t}_{1}}\right) \ldots \left( {1 + {t}_{n}}\right)  = 1 + \left( {{\sigma }_{1} + \ldots  + {\sigma }_{n}}\right) ,
\]

prove Girard's formula

\[
{\left( -1\right) }^{k}\frac{{s}_{k}}{k} = \mathop{\sum }\limits_{{{i}_{1} + 2{i}_{2} + \ldots  + k{i}_{k} = k}}{\left( -1\right) }^{{i}_{1} + \ldots  + {i}_{i}}\frac{\left( {{i}_{1} + \ldots  + {i}_{k} - 1}\right) !}{{i}_{1}!\ldots {i}_{k}!}{\sigma }_{1}^{{i}_{1}}\ldots {\sigma }_{k}^{{i}_{k}}.
\]

Problem 16-B. The Chern character \( \operatorname{ch}\left( \omega \right) \) of a complex \( n \) -plane bundle \( \omega \) is defined to be the formal sum

\[
n + \mathop{\sum }\limits_{{k = 1}}^{\infty }\frac{{s}_{k}\left( {\mathrm{c}\left( \omega \right) }\right) }{k!} \in  {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Q}}\right) .
\]

Show that this Chern character is characterized by additivity

\[
\operatorname{ch}\left( {\omega  \oplus  {\omega }^{\prime }}\right)  = \operatorname{ch}\left( \omega \right)  + \operatorname{ch}\left( {\omega }^{\prime }\right) ,
\]

together with the property that \( \operatorname{ch}\left( {\eta }^{1}\right) \) is equal to the formal power series \( \exp \left( {{c}_{1}\left( {\eta }^{1}\right) }\right) \) for any line bundle \( {\eta }^{1} \) . Show that the Chern character is also multiplicative:

\[
\operatorname{ch}\left( {\omega  \otimes  {\omega }^{\prime }}\right)  = \operatorname{ch}\left( \omega \right) \operatorname{ch}\left( {\omega }^{\prime }\right) .
\]

(As in Problem 7-C, it suffices to consider first the case of two line bundles.)

Problem 16-C. If \( 2{i}_{1},\ldots ,2{i}_{r} \) is a partition of \( {2k} \) into even integers, show that the \( 4\mathrm{k} \) -dimensional characteristic class \( {s}_{2{i}_{1},\ldots ,2{i}_{r}}\left( {\mathrm{c}\left( \omega \right) }\right) \) of a complex vector bundle is equal to the characteristic class \( {s}_{{i}_{1},\ldots ,{i}_{r}}\left( {\mathrm{p}\left( {\omega }_{\mathbb{R}}\right) }\right) \) of its underlying real vector bundle. As examples, show that the \( {4k} \) -dimensional class \( {s}_{2,\ldots ,2}\left( {\mathrm{c}\left( \omega \right) }\right) \) is equal to \( {\mathrm{p}}_{k}\left( {\omega }_{\mathbb{R}}\right) \) , and show that the characteristic number \( {s}_{2n}\left( \mathrm{c}\right) \left\lbrack  {K}^{2n}\right\rbrack \) of a complex \( {2n} \) -manifold is equal to \( {s}_{n}\left( \mathrm{p}\right) \left\lbrack  {K}^{2n}\right\rbrack \)

Problem 16-D. If the complex manifold \( {K}^{n} \) is complex analytically embedded in \( {K}^{n + 1} \) with dual cohomology class \( u \in  {\mathrm{H}}^{2}\left( {{K}^{n + 1},\mathbb{Z}}\right) \) , show that the total tangential Chern class \( \mathrm{c}\left( {K}^{n}\right) \) is equal to the restriction to \( {K}^{n} \) of \( \mathrm{c}\left( {K}^{n + 1}\right) /\left( {1 + u}\right) \) . For any cohomology class \( x \in  {\mathrm{H}}^{2n}\left( {{K}^{n + 1};\mathbb{Z}}\right) \) show that the Kronecker index \( \left\langle  {x \mid  {K}^{n},{\mu }_{2n}}\right\rangle \) is equal to \( \left\langle  {{xu},{\mu }_{{2n} + 2}}\right\rangle \) . (Compare page 127 as well as Problem 11-C.) Using these constructions, compute \( \mathrm{c}\left( {K}^{n}\right) \) for a non-singular algebraic hypersurface \( {K}^{n} \) of degree \( d \) in \( {\mathbb{P}}^{n + 1}\left( \mathbb{C}\right) \) , and prove that the characteristic number \( {s}_{n}\left\lbrack  {K}^{n}\right\rbrack \) is equal to \( d\left( {n + 2 - {d}^{n}}\right) \) . (An algebraic hypersurfacealgebraic hypersurface of degree \( d \) is the set of zeroes of a homogeneous polynomial of degree d.)

Problem 16-E. Similarly, if \( {H}_{m, n} \) is a non-singular hypersurface of degree \( \left( {1,1}\right) \) in the product \( {\mathbb{P}}^{m}\left( \mathbb{C}\right)  \times  {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) of complex projective spaces, with \( m, n \geq  2 \) , prove that the characteristic number \( {s}_{m + n - 1}\left\lbrack  {H}_{m, n}\right\rbrack \) is equal to \( - \left( {m + n}\right) !/m!n! \) . Using disjoint unions of hypersurfaces, prove that for each dimension \( n \) there exists a complex manifold \( {K}^{n} \) with \( {s}_{n}\left\lbrack  {K}^{n}\right\rbrack   = p \) if \( n + 1 \) is a power of the prime \( p \) , or with \( {s}_{n}\left\lbrack  {K}^{n}\right\rbrack   = 1 \) if \( n + 1 \) is not a prime power. (A theorem of Milnor and Novikov asserts that these manifolds \( {K}^{1},{K}^{2},{K}^{3},\ldots \) freely generate the ring consisting of all "cobordism classes" of manifolds with a complex structure on the stable tangent bundle \( \tau  \oplus  {\varepsilon }^{k} \) . Compare [Sto68].)

Problem 16-F. Develop a corresponding calculus of mod 2 characteristic numbers \( {s}_{I}\left( {{\mathrm{w}}_{1},\ldots ,{\mathrm{w}}_{n}}\right) \left\lbrack  {M}^{n}\right\rbrack \) , where \( I \) ranges over partitions of \( n \) . Using real algebraic hypersurfaces of degree \( \left( {1,1}\right) \) in a product of real projective spaces, prove that there exists a manifold \( {Y}^{n} \) with \( {s}_{n}\left( \mathrm{w}\right) \left\lbrack  {Y}^{n}\right\rbrack   \neq  0 \) whenever \( n + 1 \) is not a power of 2 . For \( n \) odd show that \( {Y}^{n} \) is orientable. As in Problem 4-E, let \( {\mathfrak{N}}_{n} \) be the \( \mathbb{Z}/2 \) vector space consisting of cobordism classes of unoriented \( n \) -manifolds. Show that the products \( {Y}^{{i}_{1}} \times  \ldots  \times  {Y}^{{i}_{r}} \) , where \( {i}_{1},\ldots ,{i}_{r} \) ranges over all partitions of \( n \) into integers not of the form \( {2}^{k} - 1 \) , are linearly independent in \( {\mathfrak{N}}_{n} \) . ( \( A \) theorem of Thom asserts that these products actually form a basis for \( {\pi }_{n} \) , so that the cobordism algebra \( {\mathfrak{N}}_{ * } \) is a polynomial algebra freely generated by the manifolds \( {Y}^{2},{Y}^{4},{Y}^{5},{Y}^{6},{Y}^{8},\ldots \)
