# 19 Multiplicative Sequences and the Signature Theorem

The material in this chapter is due to [Hir66].

Let \( \Lambda \) be a fixed commutative ring with unit (usually the ring of rational numbers). The symbol

\[
{A}^{ * } = \left( {{A}^{0},{A}^{1},{A}^{2},\cdots }\right)
\]

will stand for a graded \( \Lambda \) -algebra with unit which is commutative in the classical sense \( \left( {{xy} = {yx}\text{ regardless of the degrees of }x\text{ and }y}\right) \) . In the main application, \( {A}^{n} \) will be the cohomology group \( {\mathrm{H}}^{4n}\left( {B;\Lambda }\right) \) .

To each such \( {A}^{ * } \) we associate the commutative ring \( {A}^{\Pi } \) consisting of all formal sums \( {a}_{0} + {a}_{1} + {a}_{2} + \cdots \) with \( {a}_{i} \in  {A}^{i} \) . (Compare p. 46) We will be particularly interested in the group consisting of all elements of the form

\[
a = 1 + {a}_{1} + {a}_{2} + \cdots
\]

in \( {A}^{\Pi } \) . The product of two such units is evidently given by the formula

\[
\left( {1 + {a}_{1} + {a}_{2} + \cdots }\right) \left( {1 + {b}_{1} + {b}_{2} + \cdots }\right)  = 1 + \left( {{a}_{1} + {b}_{1}}\right)  + \left( {{a}_{2} + {a}_{1}{b}_{1} + {b}_{2}}\right)  + \cdots
\]

Now consider a sequence of polynomials

\[
{K}_{1}\left( {x}_{1}\right) ,{K}_{2}\left( {{x}_{1},{x}_{2}}\right) ,{K}_{3}\left( {{x}_{1},{x}_{2},{x}_{3}}\right) ,\cdots
\]

with coefficients in \( \Lambda \) such that, if the variable \( {x}_{i} \) is the assigned degree \( i \) , then

\[
\text{ each }{K}_{n}\left( {{x}_{1},\cdots ,{x}_{n}}\right) \text{ is homogeneous of degree }n\text{ . } \tag{19.1}
\]

Given \( {A}^{\Pi } \) as above, and an element \( a \in  {A}^{\Pi } \) with leading term 1, define a new element \( K\left( a\right)  \in  {A}^{\Pi } \) , also with leading term 1, by the formula

\[
K\left( a\right)  = 1 + {K}_{1}\left( {a}_{1}\right)  + {K}_{2}\left( {{a}_{1},{a}_{2}}\right)  + \cdots
\]

Definition. The \( {K}_{n} \) form a multiplicative sequence of polynomials if the identity

\[
K\left( {ab}\right)  = K\left( a\right) K\left( b\right) \tag{19.2}
\]

is satisfied for all such \( \Lambda \) -algebras \( {A}^{ * } \) and for all \( a, b \in  {A}^{\Pi } \) with leading term 1 .

Example 1. Given any constant \( \lambda  \in  \Lambda \) the polynomials

\[
{K}_{n}\left( {{x}_{1},\cdots ,{x}_{n}}\right)  = {\lambda }^{n}{x}_{n}
\]

form a multiplicative sequence, with

\[
K\left( {1 + {a}_{1} + {a}_{2} + \cdots }\right)  = 1 + \lambda {a}_{1} + {\lambda }^{2}{a}_{2} + \cdots .
\]

The cases \( \lambda  = 1 \) (so that \( K\left( a\right)  = a \) ) and \( \lambda  =  - 1 \) (compare Lemma 14.9) are of particular interest.

Example 2. The identity \( K\left( a\right)  = {a}^{-1} \) defines a multiplicative sequence with

\[
{K}_{1}\left( {x}_{1}\right) \; =  - {x}_{1}
\]

\[
{K}_{2}\left( {{x}_{1},{x}_{2}}\right) \; = \;{x}_{1}^{2} - {x}_{2}
\]

\[
{K}_{3}\left( {{x}_{1},{x}_{2},{x}_{3}}\right) \; =  - {x}_{1}^{3} + 2{x}_{1}{x}_{2} - {x}_{3}
\]

\[
{K}_{4}\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right)  = \;{x}_{1}^{4} - 3{x}_{1}^{2}{x}_{2} + 2{x}_{1}{x}_{3} - {x}_{2}^{2} - {x}_{4}
\]

and in general

\[
{K}_{n} = \mathop{\sum }\limits_{{{i}_{1} + 2{i}_{2} + \cdots  + n{i}_{n} = n}}\frac{\left( {{i}_{1} + \cdots  + {i}_{n}}\right) !}{{i}_{1}!\cdots {i}_{n}!}{\left( -{x}_{1}\right) }^{{i}_{1}}\cdots {\left( -{x}_{n}\right) }^{{i}_{n}}
\]

These polynomials can be used to describe the relations between the Pontrjagin classes (or the Chern classes, or the Stiefel-Whitney classes) of two vector bundles with trivial Whitney sum. Compare 4.1.

Example 3. The polynomials \( {K}_{{2n} + 1} = 0 \) and

\[
{K}_{2n}\left( {{x}_{1},\cdots ,{x}_{2n}}\right)  = {x}_{n}^{2} - 2{x}_{n - 1}{x}_{n + 1} + \cdots  \mp  2{x}_{1}{x}_{{2n} - 1} \pm  2{x}_{n}
\]

form a multiplicative sequence which can be used to describe the relationship between the Chern classes of a complex vector bundle \( \omega \) and the Pontrjagin classes of the underlying real bundle \( {\omega }_{\mathbb{R}} \) . Compare Corollary 15.5.

The following theorem gives a simple classification of all possible multiplicative sequences. Let \( {A}^{ * } \) be the graded polynomial ring \( \Lambda \left\lbrack  t\right\rbrack \) where \( t \) is an indeterminate of degree 1 . Then an element of \( {A}^{\Pi } \) with leading term 1 can be thought of as a formal power series

\[
f\left( t\right)  = 1 + {\lambda }_{1}t + {\lambda }_{2}{t}^{2} + {\lambda }_{3}{t}^{3} + \cdots
\]

with coefficients in \( \Lambda \) . In particular \( 1 + t \) is such an element.

Lemma 19.1 (Hirzebruch). Given a formal power series \( f\left( t\right)  = 1 + {\lambda }_{1}t + {\lambda }_{2}{t}^{2} + \cdots \) with coefficients in \( \Lambda \) , there is one and only one multiplicative sequence \( \left\{  {K}_{n}\right\} \) with coefficients in \( \Lambda \) satisfying the condition

\[
K\left( {1 + t}\right)  = f\left( t\right)
\]

or equivalently satisfying the condition that the coefficient of \( {x}_{1}^{n} \) in each polynomial \( {K}_{n}\left( {{x}_{1},\cdots ,{x}_{n}}\right) \) is equal to \( {\lambda }_{n} \) .

Definition. \( \left\{  {K}_{n}\right\} \) is called the multiplicative sequence belonging to the power series \( f\left( t\right) \) .

Example. The three multiplicative sequneces mentioned above belong to the power series \( 1 + {\lambda t},1 - t + {t}^{2} - {t}^{3} + \cdots \) , and \( 1 + {t}^{2} \) respectively.

Remark. If the multiplicative sequence \( \left\{  {K}_{n}\right\} \) belongs to the power series \( f\left( t\right) \) , then for any \( {A}^{ * } \) and any \( {a}_{1} \in  {A}^{1} \) the identity

\[
K\left( {1 + {a}_{1}}\right)  = f\left( {a}_{1}\right)
\]

is satisfied. Of course this identity would no longer be true if something of degree \( \neq  1 \) were substituted in place of \( {a}_{1} \) .

Proof of uniqueness. Choosing any positive integer \( n \) , let \( {A}^{ * } \) be the polynomial ring \( \Lambda \left\lbrack  {{t}_{1},\cdots ,{t}_{n}}\right\rbrack \) where the \( {t}_{i} \) are algebraically independent of degree 1, and let

\[
\sigma  = \left( {1 + {t}_{1}}\right) \cdots \left( {1 + {t}_{n}}\right)  \in  {A}^{\Pi }
\]

Then

\[
K\left( \sigma \right)  = K\left( {1 + {t}_{1}}\right) \cdots K\left( {1 + {t}_{n}}\right)  = f\left( {t}_{1}\right) \cdots f\left( {t}_{n}\right) .
\]

Taking the homogeneous part of degree \( n \) , it follows that \( {K}_{n}\left( {{\sigma }_{1},\cdots ,{\sigma }_{n}}\right) \) is completely determined by the power series \( f\left( t\right) \) . Since the elementary symmetric functions \( {\sigma }_{1},\cdots ,{\sigma }_{n} \) are algebraically independent, this proves the uniqueness of each \( {K}_{n} \) .

Proof of existence. For any partition \( I = {i}_{1},\cdots ,{i}_{r} \) of \( n \) , it will be convenient to use the abbreviation \( {\lambda }_{I} \) for the product \( {\lambda }_{{i}_{1}}\cdots {\lambda }_{{i}_{r}} \) . With this convention, let us define the polynomial \( {K}_{n} \) by the formula

\[
{K}_{n}\left( {{\sigma }_{1},{\sigma }_{2},\cdots ,{\sigma }_{n}}\right) \sum {\lambda }_{I}{s}_{I}\left( {{\sigma }_{1},\cdots ,{\sigma }_{n}}\right) ,
\]

to be summed over all partitions \( I \) of \( n \) . Here \( {s}_{I} \) stands for the polynomial of Lemma 16.1, with \( {s}_{I}\left( {{\sigma }_{1},\cdots ,{\sigma }_{n}}\right)  = \sum {t}_{1}^{{i}_{1}}\cdots {t}_{r}^{{i}_{r}} \) .

Just as in Lemma 16.2, we have the identity

\[
{s}_{I}\left( {ab}\right)  = \mathop{\sum }\limits_{{{HJ} = I}}{s}_{H}\left( a\right) {s}_{J}\left( b\right) ,
\]

to be summed over all partitions \( H \) and \( J \) with juxtaposition \( {HJ} \) equal to \( I \) . Therefore

\[
K\left( {ab}\right)  = \mathop{\sum }\limits_{I}{\lambda }_{I}{s}_{I}\left( {ab}\right)
\]

is equal to

\[
\mathop{\sum }\limits_{I}{\lambda }_{I}\mathop{\sum }\limits_{{{HJ} = I}}{s}_{H}\left( a\right) {s}_{J}\left( b\right)  = \mathop{\sum }\limits_{{H, J}}{\lambda }_{H}{s}_{H}\left( a\right) {\lambda }_{j}{s}_{J}\left( b\right)
\]

Evidently this equals \( K\left( a\right) K\left( b\right) \) as required.

Now consider some multiplicative sequence of polynomials \( \left\{  {{K}_{n}\left( {{x}_{1},\cdots ,{x}_{n}}\right) }\right\} \) with rational coefficients. Let \( {M}^{m} \) be a smooth, compact, oriented \( m \) -dimensional manifold.

Definition. The \( K \) -genus \( K\left\lbrack  {M}^{m}\right\rbrack \) is zero if the dimension \( m \) is not divisible by 4, and is equal to the rational number

\[
{K}_{n}\left\lbrack  {M}^{4n}\right\rbrack   = \left\langle  {{K}_{n}\left( {{\mathrm{p}}_{1},\cdots ,{\mathrm{p}}_{n}}\right) ,{\mu }_{4n}}\right\rangle
\]

if \( m = {4}^{n} \) , where \( {\mathrm{p}}_{i} \) denotes the \( i \) -th Pontrjagin class of the tangent bundle. Thus \( K\left\lbrack  {M}^{m}\right\rbrack \) is a certain rational linear combination of the Pontrjagin numbers of \( {M}^{m} \) .

Lemma 19.2. For any multiplicative sequence \( \left\{  {K}_{n}\right\} \) , with rational coefficients, the correspondence \( M \mapsto  K\left\lbrack  M\right\rbrack \) defines a ring homomorphism from the cobordism ring \( {\Omega }_{ * } \) to the rational numbers \( \mathbb{Q} \) .

Equivalently, this correspoondence gives rise to an algebra homomorphism from \( {\Omega }_{ * } \otimes  \mathbb{Q} \) to \( \mathbb{Q} \) .

Proof. It is clear that the correspondence is additive, and that the \( K \) -genus of a boundary is zero. For a product manifold \( M \times  {M}^{\prime } \) , with total Pontrjagin class congruent to \( \mathrm{p} \times  {\mathrm{p}}^{\prime } \) modulo elements of order 2, we have \( K\left( {\mathrm{p} \times  {\mathrm{p}}^{\prime }}\right)  = K\left( \mathrm{p}\right)  \times  K\left( {\mathrm{p}}^{\prime }\right) \) , hence

\[
\left\langle  {K\left( {\mathrm{p} \times  {\mathrm{p}}^{\prime }}\right) ,\mu  \times  {\mu }^{\prime }}\right\rangle   = {\left( -1\right) }^{m{m}^{\prime }}\langle K\left( \mathrm{p}\right) ,\mu \rangle \left\langle  {K\left( {\mathrm{p}}^{\prime }\right) ,{\mu }^{\prime }}\right\rangle  .
\]

Since the sign in this formula is certainly +1 when the dimensions \( m,{m}^{\prime } \) are divisible by 4 , this proves that

\[
K\left\lbrack  {M \times  {M}^{\prime }}\right\rbrack   = K\left\lbrack  M\right\rbrack  K\left\lbrack  {M}^{\prime }\right\rbrack
\]

as required.

We will use this construction to compute an important homotopy type invariant of \( M \) .

Definition. The signature \( \sigma \) of a compact, oriented manifold \( {M}^{m} \) is defined to be zero if the dimension is not a multiple of 4, and as follows for \( m = {4k} \) . Choose a basis \( {a}_{1},\cdots ,{a}_{r} \) for \( {\mathrm{H}}^{2k}\left( {{M}^{4k};\mathbb{Q}}\right) \) so that the symmetric matrix

\[
\left\lbrack  \left\langle  {{a}_{i} \smile  {a}_{j},\mu }\right\rangle  \right\rbrack
\]

is diagonal. Then \( \sigma \left( {M}^{4k}\right) \) is the number of positive diagonal entries minus the number of negative ones. (In other words \( \sigma \) is the signature of the rational quadratic form \( a \mapsto  \langle a \smile  a,\mu \rangle \) .)

Alternatively, this number \( \sigma \) is often called the "index" of \( M \) , particularly in older literature.

Lemma 19.3 (Thom). The signature function has the following three properties:

1. \( \sigma \left( {M + {M}^{\prime }}\right)  = \sigma \left( M\right)  + \sigma \left( {M}^{\prime }\right) \) ,

2. \( \sigma \left( {M \times  {M}^{\prime }}\right)  = \sigma \left( M\right) \sigma \left( {M}^{\prime }\right) \) ,

3. if \( M \) is an oriented boundary, then \( \sigma \left( M\right)  = 0 \) .

In fact, Assertion (1) is trivial, (2) can be proved using the Künneth isomorphism \( {\mathrm{H}}^{ * }\left( {M \times  {M}^{\prime };\mathbb{Q}}\right)  \cong  {\mathrm{H}}^{ * }\left( {M;\mathbb{Q}}\right)  \otimes  {\mathrm{H}}^{ * }\left( {{M}^{\prime };\mathbb{Q}}\right) \) , and (3) can be proved using the Poincaré duality theorem for manifolds with boundary. Details may be found in [Hir66, §8], or in [Sto68, pp. 220-222].

It follows immediately from properties (1) and (3) that the signature of a manifold can be expressed as a linear function of its Pontrjagin numbers. More precisely, according to Hirzebruch, one has the following.

Theorem 19.4 (Signature Theorem). Let \( \left\{  {{L}_{k}\left( {{\mathrm{p}}_{1},\cdots ,{\mathrm{p}}_{k}}\right) }\right\} \) be the multiplicative sequence of polynomials belonging to the power series

\[
\frac{\sqrt{t}}{\tanh \sqrt{t}} = 1 + \frac{1}{3}t - \frac{1}{45}{t}^{2} + \cdots  + \frac{{\left( -1\right) }^{k - 1}{2}^{2k}{B}_{k}{t}^{k}}{\left( {2k}\right) !}\cdots
\]

Then the signature \( \sigma \left( {M}^{4k}\right) \) of any smooth compact oriented manifold \( {M}^{4k} \) is equal to the \( L \) -genus \( L\left\lbrack  {M}^{4k}\right\rbrack \) .

Here \( {B}_{k} \) denotes the \( k \) -th Bernoulli number (compare Appendix B), with

\[
{B}_{1} = \frac{1}{6},\;{B}_{2} = \frac{1}{30},\;{B}_{3} = \frac{1}{42},\;\cdots .
\]

The first four \( L \) -polynomials are

\[
{L}_{1} = \frac{1}{3}{\mathrm{p}}_{1}
\]

\[
{L}_{2} = \frac{1}{45}\left( {7{\mathrm{p}}_{2} - {\mathrm{p}}_{1}^{2}}\right)
\]

\[
{L}_{3} = \frac{1}{945}\left( {{62}{\mathrm{p}}_{3} - {13}{\mathrm{p}}_{2}{\mathrm{p}}_{1} + 2{\mathrm{p}}_{1}^{3}}\right)
\]

\[
{L}_{4} = \frac{1}{14175}\left( {{381}{\mathrm{p}}_{4} - {71}{\mathrm{p}}_{3}{\mathrm{p}}_{1} - {19}{\mathrm{p}}_{2}^{2} + {22}{\mathrm{p}}_{2}{\mathrm{p}}_{1}^{2} - 3{\mathrm{p}}_{1}^{4}}\right) .
\]

Proof of the Signature Theorem. Since the correspondences \( M \mapsto  \sigma \left( M\right) \) and \( M \mapsto  L\left\lbrack  M\right\rbrack \) both give rise to algebra homomorphisms from \( {\Omega }_{ * } \otimes  \mathbb{Q} \) to \( \mathbb{Q} \) , it suffices to check this theorem on a set of generators for the algebra \( {\Omega }_{ * } \otimes  \mathbb{Q} \) . According to Corollary 18.9, the complex projective space \( {\mathbb{P}}^{2k}\left( \mathbb{C}\right) \) provide such a set of generators.

To compute the signature of \( {\mathbb{P}}^{2k}\left( \mathbb{C}\right) \) , we need only note that \( {\mathrm{H}}^{2k}\left( {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) ;\mathbb{Q}}\right) \) is generated by a single element \( {a}^{k} \) with

\[
\left\langle  {{a}^{k} \smile  {a}^{k},\mu }\right\rangle   = 1.
\]

(Compare Theorem 14.4 and 14.10.) Hence the signature \( \sigma \left( {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right) \) is +1 .

To compute \( {L}_{k}\left\lbrack  {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right\rbrack \) , we recall from example 15.6 that the tangential Pon-trjagin class \( \mathrm{p} \) of \( {\mathbb{P}}^{2k}\left( \mathbb{C}\right) \) is equal to \( {\left( 1 + {a}^{2}\right) }^{{2k} + 1} \) . Since the multiplicative sequence \( \left\{  {L}_{k}\right\} \) belongs to the power series \( f\left( t\right)  = \sqrt{t}/\tanh \sqrt{t} \) , it follows that

\[
L\left( {1 + {a}^{2} + 0 + \cdots }\right)  = \frac{\sqrt{{a}^{2}}}{\tanh \sqrt{{a}^{2}}},
\]

and hence that

\[
L\left( \mathrm{p}\right)  = {\left( \frac{a}{\tanh a}\right) }^{{2k} + 1}.
\]

Thus the \( L \) -genus \( \langle L\left( \mathrm{p}\right) ,\mu \rangle \) is equal to the coefficient of \( {a}^{2k} \) in this power series.

Replacing \( a \) by the complex variable \( z \) , the coefficient of \( {z}^{2k} \) in the Taylor expansion of \( {\left( z/\tanh z\right) }^{{2k} + 1} \) can be computed by dividing by \( {2\pi i}{z}^{{2k} + 1} \) and then integrating around the origin. In fact the substitution \( u = \tanh z \) , with

\[
\mathrm{d}z = \frac{\mathrm{d}u}{1 - {u}^{2}} = \left( {1 + {u}^{2} + {u}^{4} + \cdots }\right) \mathrm{d}u,
\]

shows that

\[
\frac{1}{2\pi i}\oint \frac{\mathrm{d}z}{{\left( \tanh z\right) }^{{2k} + 1}} = \frac{1}{2\pi i}\oint \frac{\left( 1 + {u}^{2} + {u}^{4} + \cdots \right) }{{u}^{{2k} + 1}}\mathrm{\;d}u
\]

is equal to +1 . Hence \( L\left\lbrack  {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right\rbrack \) is equal to +1 = \( \sigma \left( {{\mathbb{P}}^{2k}\left( \mathbb{C}\right) }\right) \) , and it follows that \( L\left\lbrack  M\right\rbrack   = \sigma \left( M\right) \) for all \( M. \)

A more direct proof of the signature theorem has been given by [AS68, §6], as an application of the "Atiyah-Singer Index Theorem" for elliptic differential operators.

Corollary 19.5. The \( L \) -genus of any manifold is an integer.

For the signature \( \sigma \) is always an integer.

It follows, for example, that the Pontrjagin number \( {\mathrm{p}}_{1}\left\lbrack  {M}^{4}\right\rbrack \) is divisble by 3, and the number \( 7{\mathrm{p}}_{2}\left\lbrack  {M}^{8}\right\rbrack   - {\mathrm{p}}_{1}^{2}\left\lbrack  {M}^{8}\right\rbrack \) is divisible by 45 .

Corollary 19.6. The \( L \) -genus \( L\left\lbrack  M\right\rbrack \) depends only on the oriented homotopy type of \( M \) .

For \( \sigma \left( M\right) \) is clearly invariant under any orientation preserving homotopy equivalence.

According to [Kah72], the \( L \) -genus and its rational multiples are the only rational linear combinations of Pontrjagin numbers which are oriented homotopy type invariants.
