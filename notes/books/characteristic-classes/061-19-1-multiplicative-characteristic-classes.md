# 19.1 Multiplicative Characteristic Classes

For the remainder of this section we will very briefly describe another application of multiplicative sequences. Let \( \Lambda \) be an integral domain containing \( 1/2 \) , and let \( \left\{  {K}_{n}\right\} \) be a multiplicative sequence with coefficients in \( \Lambda \) . Setting

\[
{k}_{n}\left( \xi \right)  = {K}_{n}\left( {{\mathrm{p}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{p}}_{n}\left( \xi \right) }\right)
\]

for any real vector bundle \( \xi \) , we clearly obtain a sequence of "characteristic classes"

\[
{k}_{n}\left( \xi \right)  \in  {\mathrm{H}}^{4n}\left( {B;\Lambda }\right)
\]

which are natural with respect to bundle maps, and satisfy the product formula

\[
{k}_{n}\left( {\xi  \oplus  \eta }\right)  = \mathop{\sum }\limits_{{i + j = n}}{k}_{i}\left( \xi \right) {k}_{j}\left( \eta \right) .
\]

Here it is understood that \( {k}_{0}\left( \xi \right)  = 1 \) . [Setting \( k\left( \xi \right)  = \sum {k}_{i}\left( \xi \right) \) , we can of course write this product formula briefly as \( k\left( {\xi  \oplus  \eta }\right)  = k\left( \xi \right) k\left( \eta \right) \) .]

Conversely, given a sequence of characteristic classes \( {k}_{n}\left( \xi \right) \) satisfying these properties, it is not difficult to show that \( {k}_{n}\left( \xi \right)  = {K}_{n}\left( {{\mathrm{p}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{p}}_{n}\left( \xi \right) }\right) \) for some uniquely defined multiplicative sequence \( \left\{  {K}_{n}\right\} \) . (Compare Theorem 15.9 and Problem 15-B.) It does not matter whether or not the bundles \( \xi \) are required to be oriented or orientable.

The precise multiplicative sequence corresponding to a sequence \( \left\{  {{k}_{n}\left( \xi \right) }\right\} \) of characteristic classes can be identified as follows. Let \( {\gamma }^{1} \) be the canonical complex line bundle over \( {\mathbb{P}}^{\infty }\left( \mathbb{C}\right) \) , and recall that

\[
{\mathrm{p}}_{1}\left( {\gamma }_{\mathbb{R}}^{1}\right)  = {a}^{2} \in  {\mathrm{H}}^{4}\left( {{\mathbb{P}}^{\infty }\left( \mathbb{C}\right) ;\mathbb{Z}}\right) .
\]

( Compare Theorem 14.4, Theorem 14.10 and Corollary 15.5.) Defining a formal power series \( f\left( t\right) \) by setting \( f\left( {a}^{2}\right) \) equal to \( k\left( {\gamma }_{\mathbb{R}}^{1}\right)  = \sum {k}_{n}\left( {\gamma }_{\mathbb{R}}^{1}\right) \) , it clearly follows that \( \left\{  {K}_{n}\right\} \) is the multiplicative sequence belonging to this power series \( f\left( t\right) \) .

To illustrate these ideas, let us consider the case \( \Lambda  = \mathbb{Z}/l \) where \( l \) is a fixed odd prime. Let

\[
{\mathcal{P}}^{k} : {\mathrm{H}}^{i}\left( {X;\mathbb{Z}/l}\right)  \rightarrow  {\mathrm{H}}^{i + {4rk}}\left( {X;\mathbb{Z}/l}\right)
\]

denote the Steenrod reduced \( l \) -th power operation, where \( r = \frac{1}{2}\left( {l - 1}\right) \) . (Compare [SE62].) Following [Wu48], and in analogy with Thom's definition of Stiefel-Whitney classes (§8), we define a new characteristic class

\[
{\mathrm{q}}_{n}\left( \xi \right)  \in  {\mathrm{H}}^{4rn}\left( {B;\mathbb{Z}/l}\right)
\]

by the identity \( {\mathrm{q}}_{n}\left( \xi \right)  = {\phi }^{-1}{\mathcal{P}}^{n}\phi \left( 1\right) \) for any oriented vector bundle \( \xi \) . Just as in \( \text{ § }8 \) , it is easy to check that the \( {\mathrm{q}}_{n} \) are natural, and satisfy a product formula. Hence

\[
{\mathrm{q}}_{n}\left( \xi \right)  = {K}_{rn}\left( {{\mathrm{p}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{p}}_{rn}\left( \xi \right) }\right)
\]

for some uniquely determined multiplicative sequence \( \left\{  {K}_{n}\right\} \) with \( {\;\operatorname{mod}\;l} \) coefficients.

To identify this multiplicative sequence, we need only consider the particular vector bundle \( \xi  = {\gamma }_{\mathbb{R}}^{1} \) over the infinite complex projective space \( {\mathbb{P}}^{\infty }\left( \mathbb{C}\right) \) . The space \( {E}_{0} \) of non-zero vectors in \( E = E\left( {\gamma }_{\mathbb{R}}^{1}\right) \) has the homology of a point. Hence there are natural ring isomorphisms

\[
{\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right)  \cong  {\mathrm{H}}^{ * }\left( {E,\text{ point }}\right)  \cong  {\mathrm{H}}^{ * }\left( {{\mathbb{P}}^{\infty }\left( \mathbb{C}\right) ,\text{ point }}\right) .
\]

The fundamental cohomology class \( u \in  {\mathrm{H}}^{2}\left( {E,{E}_{0}}\right) \) corresponds to the class

\[
\mathrm{e}\left( {\gamma }_{\mathbb{R}}^{1}\right)  = {\mathrm{c}}_{1}\left( {\gamma }^{1}\right)  =  - a \in  {\mathrm{H}}^{2}\left( {{\mathbb{P}}^{2}\left( \mathbb{C}\right) }\right) .
\]

(See Theorem 14.10.) Therefore the element \( {\mathcal{P}}^{1}\left( u\right)  = {u}^{l} \) (see [SE62, p. 76]) corresponds to \( {\left( -a\right) }^{l} \) , and it follows that

\[
{\mathrm{q}}_{1}\left( {\gamma }_{\mathbb{R}}^{1}\right)  = {\left( -a\right) }^{l - 1} = {a}^{2r}.
\]

Since the higher \( {\mathcal{P}}^{k}\left( u\right) \) are zero for dimensional reasons, this shows that the formal power series \( f\left( {a}^{2}\right)  = \sum {\mathrm{q}}_{k}\left( {\gamma }_{\mathbb{R}}^{1}\right) \) is equal to \( 1 + {a}^{2r} \) , which proves the following.

Theorem 19.7 (Wu). If \( l = {2r} + 1 \) is an odd prime, then the mod \( l \) characteristic class

\[
{\mathrm{q}}_{n}\left( \xi \right)  = {\phi }^{-1}{\mathcal{P}}^{n}\phi \left( 1\right)
\]

is equal to \( {K}_{rn}\left( {{\mathrm{p}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{p}}_{rn}\left( \xi \right) }\right) \) where \( \left\{  {K}_{i}\right\} \) is the multiplicative sequence belonging to the power series \( f\left( t\right)  = 1 + {t}^{r} \) .

As examples, for \( l = 3 \) it follows that \( {\mathrm{q}}_{n}\left( \xi \right) \) is equal to the Pontrjagin class \( {\mathrm{p}}_{n}\left( \xi \right) \) reduced modulo 3, and for \( l = 5 \) it follows that \( {\mathrm{q}}_{n}\left( \xi \right) \) is equal to \( {\mathrm{p}}_{n}^{2} - 2{\mathrm{p}}_{n - 1}{\mathrm{p}}_{n + 1} +  - \ldots  \pm  2{\mathrm{p}}_{2n} \) reduced modulo 5 .

Just as in the mod 2 case, it can be shown that \( {\mathrm{q}}_{i}\left( {\tau }^{n}\right) \) , for the tangent bundle \( {\tau }^{n} \) of a compact oriented manifold, is a homotopy type invariant. (Compare Theorem 11.14.) In fact

\[
{\mathrm{q}}_{i} = {v}_{i} + {\mathcal{P}}^{1}{v}_{i - 1} + {\mathcal{P}}^{2}{v}_{i - 2} + \ldots
\]

where the Wu class \( {v}_{i} \) is characterized by the identity

\[
\left\langle  {{\mathcal{P}}^{i}x,\mu }\right\rangle   = \left\langle  {x \smile  {v}_{i},\mu }\right\rangle
\]

for all \( x \in  {\mathrm{H}}^{n - {4ri}}\left( {{M}^{n};\mathbb{Z}/l}\right) \) . In particular, it follows that Pontrjagin classes modulo 3 are homotopy type invariants. Proofs will be left to the reader.

These characteristic classes \( {\mathrm{q}}_{i}\left( \xi \right) \) generalize to play an important rule in the theory of fibrations with a homotopy sphere as fiber. Compare [Mil68], [Sta68], [May06].

We conclude with three problems for the reader, all taken from [Hir53].

Problem 19-A. Let \( \left\{  {T}_{n}\right\} \) be the multiplicative sequence of polynomials belonging to the power series \( f\left( t\right)  = t/\left( {1 - {\mathrm{e}}^{-t}}\right) \) . Then the Todd genus \( T\left\lbrack  M\right\rbrack \) of a complex \( n \) -dimensional manifold is defined to be the characteristic number \( \left\langle  {{T}_{n}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{n}}\right) ,{\mu }_{2n}}\right\rangle \) . Prove that \( T\left\lbrack  {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right\rbrack   =  + 1 \) , and prove that \( \left\{  {T}_{n}\right\} \) is the only multiplicative sequence with this property.

Problem 19-B. If \( \left\{  {K}_{n}\right\} \) is the multiplicative sequence belonging to \( f\left( t\right)  = 1 + {\lambda }_{1}t + {\lambda }_{2}{t}^{2} + \ldots \) , let us indicate the dependence on the coefficients \( {\lambda }_{i} \) by setting \( {K}_{n}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = {k}_{n}\left( {{\lambda }_{1},\ldots ,{\lambda }_{n},{x}_{1},\ldots ,{x}_{n}}\right) \) where \( {k}_{n} \) is a polynomial with integer coefficients. By considering the case where \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) are the elementary symmetric functions in \( n \) indeterminates, prove the symmetry property \( {k}_{n}\left( {{x}_{1},\ldots ,{x}_{n},{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  = {k}_{n}\left( {{\lambda }_{1},\ldots ,{\lambda }_{n},{x}_{1},\ldots ,{x}_{n}}\right) \) . In particular, prove that the coefficient of \( {x}_{{i}_{1}}\ldots {x}_{{i}_{r}} \) in the polynomial \( {K}_{n}\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is equal to \( {s}_{{i}_{1},\ldots ,{i}_{r}}\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) . \)

Problem 19-C. Using Cauchy's identity

\[
f\left( t\right) \frac{\mathrm{d}\left( {t/f\left( t\right) }\right) }{\mathrm{d}t} = 1 - t\frac{\mathrm{d}\log f\left( t\right) }{\mathrm{d}t} = 1 + \sum {\left( -1\right) }^{j}{s}_{j}\left( {{\lambda }_{1},\ldots ,{\lambda }_{j}}\right) {t}^{j},
\]

prove that the coefficient of \( {\mathrm{p}}_{n} \) in the \( L \) -polynomial \( {L}_{n}\left( {{\mathrm{p}}_{1},\ldots ,{\mathrm{p}}_{n}}\right) \) is equal to \( {2}^{2k}\left( {{2}^{{2k} - 1} - 1}\right) {B}_{k}/\left( {2k}\right) ! \neq  0 \) . (Compare Appendix B.)
