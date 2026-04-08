## §21 The Splitting Principle and Flag Manifolds

In this section we prove the Whitney product formula and compute a few Chern classes. The proof and the computations are based on the splitting principle, which, roughly speaking, states that if a polynomial identity in the Chern classes holds for direct sums of line bundles, then it holds for general vector bundles. In the course of establishing the splitting principle we introduce the flag manifolds. We conclude by computing the cohomology ring of a flag manifold.

## The Splitting Principle

Let \( \tau  : E \rightarrow  M \) be a \( {C}^{\infty } \) complex vector bundle of rank \( n \) over a manifold \( M \) . Our goal is to construct a space \( F\left( E\right) \) and a map \( \sigma  : F\left( E\right)  \rightarrow  M \) such that:

(1) the pullback of \( E \) to \( F\left( E\right) \) splits into a direct sum of line bundles: \( {\sigma }^{-1}E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n} \)

(2) \( {\sigma }^{ * } \) embeds \( {H}^{ * }\left( M\right) \) in \( {H}^{ * }\left( {F\left( E\right) }\right) \) .

Such a space \( F\left( E\right) \) , which is in fact a manifold by construction, is called a split manifold of \( E \) .

If \( E \) has rank 1, there is nothing to prove.

If \( E \) has rank 2, we can take as a split manifold \( F\left( E\right) \) the projective bundle \( P\left( E\right) \) , for on \( P\left( E\right) \) there is the exact sequence

\[
0 \rightarrow  {S}_{E} \rightarrow  {\sigma }^{-1}E \rightarrow  {Q}_{E} \rightarrow  0
\]

by the exercise below, \( {\sigma }^{-1}E = {S}_{E} \oplus  {Q}_{E} \) , which is a direct sum of line bundles.

Exercise 21.1. Let \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) be a short exact sequence of \( {C}^{\infty } \) complex vector bundles. Then \( B \) is isomorphic to \( A \oplus  C \) as a \( {C}^{\infty } \) bundle.

Now suppose \( E \) has rank 3. Over \( P\left( E\right) \) the line bundle \( {S}_{E} \) splits off as before. The quotient bundle \( {Q}_{E} \) over \( P\left( E\right) \) has rank 2 and so can be split into a direct sum of line bundles when pulled back to \( P\left( {Q}_{E}\right) \) .

![bo_d7b6f8alb0pc73dd9avg_284_443_829_772_450_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_284_443_829_772_450_0.jpg)

Thus we may take \( P\left( {Q}_{E}\right) \) to be a split manifold \( F\left( E\right) \) . Let \( {x}_{1} = {\beta }^{ * }{c}_{1}\left( {S}_{E}^{ * }\right) \) and \( {x}_{2} = {c}_{1}\left( {S}_{{\mathcal{Q}}_{E}}^{ * }\right) \) . By the result on the cohomology of a projective bundle (20.7),

\[
{H}^{ * }\left( {F\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  {{x}_{1},{x}_{2}}\right\rbrack  /\left( {{x}_{1}^{3} + {c}_{1}\left( E\right) {x}_{1}^{2} + {c}_{2}\left( E\right) {x}_{1} + {c}_{3}\left( \mathrm{E}\right) ,}\right.
\]

\[
\left. {{x}_{2}^{2} + {c}_{1}\left( {Q}_{E}\right) {x}_{2} + {c}_{2}\left( {Q}_{E}\right) }\right) \text{ . }
\]

The pattern is now clear; we split off one subbundle at a time by pulling back to the projectivization of a quotient bundle.

![bo_d7b6f8alb0pc73dd9avg_284_286_1692_1100_404_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_284_286_1692_1100_404_0.jpg)

So for a bundle \( E \) of any rank \( n \) , a split manifold \( F\left( E\right) \) exists and is given explicitly by (21.2). Its cohomology \( {H}^{ * }\left( {F\left( E\right) }\right) \) is a free \( {H}^{ * }\left( M\right) \) -module having as a basis all monomials of the form

(21.3)

\[
{x}_{1}^{{a}_{1}}{x}_{2}^{{a}_{2}}\cdots {x}_{n - 1}^{{a}_{n - 1}},{a}_{1} \leq  n - 1,{a}_{2} \leq  n - 2,\ldots ,{a}_{n - 1} \leq  1,
\]

\[
{a}_{1},\ldots ,{a}_{n - 1}\text{ nonnegative, }
\]

where \( {x}_{i} = {c}_{1}\left( {S}_{i}^{ * }\right) \) in the notation of the diagram.

More generally, by iterating the construction above we see that given any number of vector bundles \( {E}_{1},\ldots ,{E}_{r} \) over \( M \) , there is a manifold \( N \) and a map \( \sigma  : N \rightarrow  M \) such that the pullbacks of \( {E}_{1},\ldots ,{E}_{r} \) to \( N \) are all direct sums of line bundles and that \( {H}^{ * }\left( M\right) \) injects into \( {H}^{ * }\left( N\right) \) under \( {\sigma }^{ * } \) . The manifold \( N \) is a split manifold for \( {E}_{1},\ldots ,{E}_{r} \) .

Because of the existence of the split manifolds we can formulate the following general principle.

The Splitting Principle. To prove a polynomial identity in the Chern classes of complex vector bundles, it suffices to prove it under the assumption that the vector bundles are direct sums of line bundles.

For example, suppose we want to prove a certain polynomial relation \( P\left( {c\left( E\right) , c\left( F\right) , c\left( {E \otimes  F}\right) }\right)  = 0 \) for vector bundles \( E \) and \( F \) over a manifold \( M \) . Let \( \sigma  : N \rightarrow  M \) be a split manifold for the pair \( E, F \) . By the naturality of the Chern classes

\[
{\sigma }^{ * }P\left( {c\left( E\right) , c\left( F\right) , c\left( {E \otimes  F}\right) }\right)  = P\left( {c\left( {{\sigma }^{-1}E}\right) , c\left( {{\sigma }^{-1}F}\right) , c\left( {\left( {{\sigma }^{-1}E}\right)  \otimes  \left( {{\sigma }^{-1}F}\right) }\right) }\right) ,
\]

where \( {\sigma }^{-1}E \) and \( {\sigma }^{-1}F \) are direct sums of line bundles. So if the identity holds for direct sums of line bundles, then

\[
{\sigma }^{ * }P\left( {c\left( E\right) , c\left( F\right) , c\left( {E \otimes  F}\right) }\right)  = 0.
\]

By the injectivity of \( {\sigma }^{ * } : {H}^{ * }\left( M\right)  \rightarrow  {H}^{ * }\left( N\right) \) ,

\[
P\left( {c\left( E\right) , c\left( F\right) , c\left( {E \otimes  F}\right) }\right)  = 0.
\]

In the next two subsections we give some illustrations of this principle.

Proof of the Whitney Product Formula and the Equality of the Top Chern Class and the Euler Class

We consider first the case of a direct sum of line bundles:

\[
E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n}.
\]

By abuse of notation we write \( {\pi }^{-1}E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n} \) for the pullback of \( E \) to the projectivization \( P\left( E\right) \) . Over \( P\left( E\right) \) , the universal subbundle \( S \) splits off from \( {\pi }^{-1}E \) .

![bo_d7b6f8alb0pc73dd9avg_286_604_401_408_316_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_286_604_401_408_316_0.jpg)

Let \( {s}_{i} \) be the projection of \( S \) onto \( {L}_{i} \) . Then \( {s}_{i} \) is a section of \( \operatorname{Hom}\left( {S,{L}_{i}}\right)  = \; {S}^{ * } \otimes  {L}_{i} \) . Since at every point \( y \) of \( P\left( E\right) \) , the fiber \( {S}_{y} \) is a 1-dimensional subspace of \( {\left( {\pi }^{-1}E\right) }_{y} \) , the projections \( {s}_{1},\ldots ,{s}_{n} \) cannot be simultaneously zero. It follows that the open sets

\[
{U}_{i} = \left\{  {y \in  P\left( E\right)  \mid  {s}_{i}\left( y\right)  \neq  0}\right\}
\]

form an open cover of \( P\left( E\right) \) . Over each \( {U}_{i} \) the bundle \( {\left. \left( {S}^{ * } \otimes  {L}_{i}\right) \right| }_{{U}_{i}} \) has a nowhere-vanishing section, namely \( {s}_{i} \) ; so \( {\left. \left( {S}^{ * } \otimes  {L}_{i}\right) \right| }_{{U}_{i}} \) is trivial. Let \( {\xi }_{i} \) be a closed global 2-form on \( P\left( E\right) \) representing \( {c}_{1}\left( {{S}^{ * } \otimes  {L}_{i}}\right) \) . Then \( {\xi }_{i \mid  {U}_{i}} = d{\omega }_{i} \) for some 1-form \( {\omega }_{i} \) on \( {U}_{i} \) . The crux of the proof is to find a global form on \( P\left( E\right) \) that represents \( {c}_{1}\left( {{S}^{ * } \otimes  {L}_{i}}\right) \) and that vanishes on \( {U}_{i} \) ; because \( {\omega }_{i} \) is not a global form on \( P\left( E\right) ,{\xi }_{i} - d{\omega }_{i} \) won’t do. However, by shrinking the open cover \( \left\{  {U}_{i}\right\} \) slightly we can extend \( {\xi }_{i} - d{\omega }_{i} \) to a global form. To be precise we will need the following lemmas.

Exercise 21.4 (The Shrinking Lemma). Let \( X \) be a normal topological space and \( {\left\{  {U}_{i}\right\}  }_{i \in  I} \) a finite open cover of \( X \) . Then there is an open cover \( {\left\{  {V}_{i}\right\}  }_{i \in  I} \) with

\[
{\bar{V}}_{i} \subset  {U}_{i}.
\]

Exercise 21.5. Let \( M \) be a manifold, \( U \) an open subset, and \( A \) a closed subset contained in \( U \) . Then there is a \( {C}^{\infty } \) function \( f \) which is identically 1 on \( A \) and is 0 outside \( U \) .

It follows from these two lemmas that on \( P\left( E\right) \) there exists an open cover \( \left\{  {V}_{i}\right\} \) and \( {C}^{\infty } \) functions \( {\rho }_{i} \) satisfying

(a) \( {\bar{V}}_{i} \subset  {U}_{i} \)

(b) \( {\rho }_{i} \) is 1 on \( {\bar{V}}_{i} \) and is 0 outside \( {U}_{i} \) .

Now \( {\rho }_{i}{\omega }_{i} \) is a global form which agrees with \( {\omega }_{i} \) on \( {V}_{i} \) so that

\[
{\xi }_{i} - d\left( {{\rho }_{i}{\omega }_{i}}\right)
\]

is a global form representing \( {c}_{1}\left( {{S}^{ * } \otimes  {L}_{i}}\right) \) and vanishing on \( {V}_{i} \) . In summary, there is an open cover \( \left\{  {V}_{i}\right\} \) of \( P\left( E\right) \) such that \( {c}_{1}\left( {{S}^{ * } \otimes  {L}_{i}}\right) \) may be represented by a global form which vanishes on \( {V}_{i} \) .

Since \( \left\{  {V}_{i}\right\} \) covers \( P\left( E\right) ,\mathop{\prod }\limits_{{i = 1}}^{n}{c}_{1}\left( {{S}^{ * } \otimes  {L}_{i}}\right)  = 0 \) . Writing \( x = {c}_{1}\left( {S}^{ * }\right) \) , this gives by (20.1)

\[
\mathop{\prod }\limits_{{i = 1}}^{n}\left( {x + {c}_{1}\left( {L}_{i}\right) }\right)  = {x}^{n} + {\sigma }_{1}{x}^{n - 1} + \cdots  + {\sigma }_{n} = 0
\]

where \( {\sigma }_{i} \) is the \( i \) th elementary symmetric polynomial of \( {c}_{1}\left( {L}_{1}\right) ,\ldots ,{c}_{1}\left( {L}_{n}\right) \) . But this equation is precisely the defining equation of \( c\left( E\right) \) . Thus

\[
{\sigma }_{i} = {c}_{i}\left( E\right)
\]

and

\[
c\left( E\right)  = \prod \left( {1 + {c}_{1}\left( {L}_{i}\right) }\right)  = \prod c\left( {L}_{i}\right) .
\]

So the Whitney product formula holds for a direct sum of line bundles. By the splitting principle it holds for any complex vector bundle. As an illustration of the splitting principle we will go through the argument in detail. Let \( E \) and \( {E}^{\prime } \) be two complex vector bundles of rank \( n \) and \( m \) respectively and let \( \pi  : F\left( E\right)  \rightarrow  M \) and \( {\pi }^{\prime } : F\left( {{\pi }^{-1}{E}^{\prime }}\right)  \rightarrow  F\left( E\right) \) be the splitting constructions. Both bundles split completely when pulled back to \( F\left( {{\pi }^{-1}{E}^{\prime }}\right) \) as indicated in the diagram below.

![bo_d7b6f8alb0pc73dd9avg_287_352_1192_927_301_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_287_352_1192_927_301_0.jpg)

Let \( \sigma  = {\pi }^{\prime } \circ  \pi \) . Then

\[
{\sigma }^{ * }c\left( {E \oplus  {E}^{\prime }}\right)  = c\left( {{\sigma }^{-1}\left( {E \oplus  {E}^{\prime }}\right) }\right)  = c\left( {{L}_{1} \oplus  \cdots  \oplus  {L}_{n} \oplus  {L}_{1}^{\prime } \oplus  \cdots  \oplus  {L}_{m}^{\prime }}\right)
\]

\[
= \prod c\left( {L}_{i}\right) c\left( {L}_{i}^{\prime }\right)
\]

\[
= {\sigma }^{ * }c\left( E\right) {\sigma }^{ * }\left( {E}^{\prime }\right)  = {\sigma }^{ * }c\left( E\right) c\left( {E}^{\prime }\right) .
\]

Since \( {\sigma }^{ * } \) is injective, \( c\left( {E \oplus  {E}^{\prime }}\right)  = c\left( E\right) c\left( {E}^{\prime }\right) \) . This concludes the proof of the Whitney product formula.

REMARK 21.6. By Exercise (21.1) and the Whitney product formula, whenever we have an exact sequence of \( {C}^{\infty } \) complex vector bundles

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0,
\]

then \( c\left( B\right)  = c\left( A\right) c\left( C\right) \) .

As an application of the existence of the split manifold and the Whitney product formula, we will prove now the relation (20.10.6) between the top Chern class and the Euler class. Let \( E \) be a rank \( n \) complex vector bundle and \( \sigma  : F\left( E\right)  \rightarrow  E \) its split manifold. Write \( {\sigma }^{-1}E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n} \) , where the \( {L}_{i} \) ’s are line bundles on the split manifold \( F\left( E\right) \) .

\[
{\sigma }^{ * }{c}_{n}\left( E\right)  = {c}_{n}\left( {{\sigma }^{-1}E}\right)
\]

by the naturality of \( {c}_{n} \)

\[
= {c}_{1}\left( {L}_{1}\right) \cdots {c}_{1}\left( {L}_{n}\right)
\]

by the Whitney product formula (20.10.3)

\[
= e\left( {\left( {L}_{1}\right) }_{\mathbb{R}}\right) \cdots e\left( {\left( {L}_{n}\right) }_{\mathbb{R}}\right)
\]

by the definition of the first Chern class of a complex line bundle

\[
= e\left( {{\left( {L}_{1}\right) }_{\mathbb{R}} \oplus  \cdots  \oplus  {\left( {L}_{n}\right) }_{\mathbb{R}}}\right)
\]

by the Whitney product formula for the Euler class (12.5)

\[
= e\left( {\left( {\sigma }^{-1}E\right) }_{\mathbb{R}}\right)
\]

\[
= {\sigma }^{ * }e\left( {E}_{\mathbb{R}}\right) \text{ . }
\]

By the injectivity of \( {\sigma }^{ * } \) on cohomology, \( {c}_{n}\left( E\right)  = e\left( {E}_{\mathbb{R}}\right) \) .

## Computation of Some Chern Classes

Given a rank \( n \) complex vector bundle \( E \) we may write formally

\[
c\left( E\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right)
\]

where the \( {x}_{i} \) ’s may be thought of as the first Chern class of the line bundles into which \( E \) splits when pulled back to the splitting manifold \( F\left( E\right) \) . Since the Chern classes \( {c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) \) are the elementary symmetric functions of \( {x}_{1},\ldots ,{x}_{n} \) , by the symmetric function theorem (van der Waerden [1, p. 99]) any symmetric polynomial in \( {x}_{1},\ldots ,{x}_{n} \) is a polynomial in \( {c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) \) ; a similar result holds for power series.

EXAMPLE 21.7 (Exterior powers, symmetric powers, and tensor products). Recall that if \( V \) is a vector space with basis \( \left\{  {{v}_{1},\ldots ,{v}_{n}}\right\} \) , then the exterior power \( {\Lambda }^{p}V \) is the vector space with basis \( {\left\{  {v}_{{i}_{1}} \land  \cdots  \land  {v}_{{i}_{p}}\right\}  }_{1 \leq  {i}_{1} < \cdots  < {i}_{p} \leq  n} \) . So if \( E \) is the direct sum of line bundles \( E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n} \) , then

\[
{\Lambda }^{p}E = \mathop{\bigoplus }\limits_{{1 \leq  {i}_{1} < \cdots  < {i}_{p} \leq  n}}\left( {{L}_{{i}_{1}} \otimes  \cdots  \otimes  {L}_{{i}_{p}}}\right) .
\]

Hence

\( c\left( {{\Lambda }^{p}E}\right)  = \prod \left( {1 + {c}_{1}\left( {{L}_{{i}_{1}} \otimes  \cdots  \otimes  {L}_{{i}_{p}}}\right) }\right) \; \) by the Whitney product formula

\[
= \prod \left( {1 + {x}_{{i}_{1}} + \cdots  + {x}_{{i}_{p}}}\right) \;\text{ by }\left( {20.1}\right) \text{ , with }{x}_{i} = {c}_{1}\left( {L}_{i}\right) ,
\]

where the product is over all multi-indices \( 1 \leq  {i}_{1} < \cdots  < {i}_{p} \leq  n \) . Since the right-hand side is symmetric in \( {x}_{1},\ldots ,{x}_{n} \) , it is expressible as a polynomial \( Q \) in \( {c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) \) , so

\[
c\left( {{\Lambda }^{p}E}\right)  = Q\left( {{c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) }\right) .
\]

By the splitting principle this formula holds for every rank \( n \) vector bundle, whether it is a direct sum or not. It should be pointed out that the polynomial \( Q \) depends only on \( n \) and \( p \) , not on \( E \) ; for example, the Chern class of \( {\Lambda }^{2}E \) , where rank \( E = 3 \) , is given by

\[
c\left( {{\Lambda }^{2}E}\right)  = Q\left( {{c}_{1},{c}_{2},{c}_{3}}\right)  = \left( {1 + {c}_{1} - {x}_{1}}\right) \left( {1 + {c}_{1} - {x}_{2}}\right) \left( {1 + {c}_{1} - {x}_{3}}\right)
\]

\[
= {\left( 1 + {c}_{1}\right) }^{3} - {c}_{1}{\left( 1 + {c}_{1}\right) }^{2} + {c}_{2}\left( {1 + {c}_{1}}\right)  - {c}_{3}.
\]

Similarly, if \( V \) and \( W \) are vector spaces with bases \( \left\{  {{v}_{1},\ldots ,{v}_{n}}\right\} \) and \( \left\{  {{w}_{1},\ldots }\right. \) , \( {w}_{m}\} \) respectively, then the \( p \) th symmetric power \( {S}^{p}V \) of \( V \) is the vector space with basis \( {\left\{  {v}_{{i}_{1}} \otimes  \cdots  \otimes  {v}_{{i}_{p}}\right\}  }_{1 \leq  {i}_{1} \leq  \cdots  \leq  {i}_{p} \leq  n} \) and the tensor product \( V \otimes  W \) is the vector space with basis \( {\left\{  {v}_{i} \otimes  {w}_{j}\right\}  }_{1 \leq  i \leq  n,1 \leq  j \leq  m} \) . By the same discussion as above, if \( E \) is a rank \( n \) vector bundle with \( c\left( E\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right) \) and \( F \) is a rank \( m \) vector bundle with \( c\left( F\right)  = \mathop{\prod }\limits_{{j = 1}}^{m}\left( {1 + {y}_{j}}\right) \) , then

and

(21.8)

\[
c\left( {{S}^{P}E}\right)  = \mathop{\prod }\limits_{{1 \leq  {i}_{1} \leq  \cdots  \leq  {i}_{p} \leq  n}}\left( {1 + {x}_{{i}_{1}} + \cdots  + {x}_{{i}_{p}}}\right)
\]

(21.9)

\[
c\left( {E \otimes  F}\right)  = \mathop{\prod }\limits_{\substack{{1 \leq  i \leq  n} \\  {1 \leq  j \leq  m} }}\left( {1 + {x}_{i} + {y}_{j}}\right) .
\]

In particular if \( L \) is a complex line bundle with first Chern class \( y \) , then

(21.10)

\[
c\left( {E \otimes  L}\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + y + {x}_{i}}\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{c}_{i}\left( E\right) {\left( 1 + y\right) }^{n - i},
\]

where by convention we set \( {c}_{0}\left( E\right)  = 1 \) .

EXAMPLE 21.11 (The \( L \) -class and the Todd class). In the notation of the preceding example the power series

\[
\mathop{\prod }\limits_{{i = 1}}^{n}\frac{\sqrt{{x}_{i}}}{\tanh \sqrt{{x}_{i}}}
\]

is symmetric in \( {x}_{1},\ldots ,{x}_{n} \) , hence is some power series \( L \) in \( {c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) \) . This power series \( L\left( E\right)  = L\left( {{c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) }\right) \) is called the \( L \) -class of \( E \) . By the splitting principle the \( L \) -class automatically satisfies the product formula

\[
L\left( {E \oplus  F}\right)  = L\left( E\right) L\left( F\right) .
\]

Similarly,

\[
\mathop{\prod }\limits_{{i = 1}}^{n}\frac{{x}_{i}}{1 - {e}^{-{x}_{i}}} = \operatorname{Td}\left( {{c}_{1}\left( E\right) ,\ldots ,{c}_{n}\left( E\right) }\right)  = \operatorname{Td}\left( E\right)
\]

defines the Todd class of \( E \) . By the splitting principle the Todd class also automatically satisfies the product formula. The \( L \) -class and the Todd class turn out to be of fundamental importance in the Hirzebruch signature formula (see Remark 22.9) and the Riemann-Roch theorem (see Hirzebruch [1]).

Example 21.12 (The dual bundle). Let \( L \) be a complex line bundle. By (20.2),

\[
{c}_{1}\left( {L}^{ * }\right)  =  - {c}_{1}\left( L\right)
\]

Next consider a direct sum of line bundles

\[
E = {L}_{1} \oplus  \cdots  \oplus  {L}_{n}.
\]

By the Whitney product formula

\[
c\left( E\right)  = c\left( {L}_{1}\right) \cdots c\left( {L}_{n}\right)  = \left( {1 + {c}_{1}\left( {L}_{1}\right) }\right) \cdots \left( {1 + {c}_{1}\left( {L}_{n}\right) }\right) .
\]

On the other hand

\[
{E}^{ * } = {L}_{1}^{ * } \oplus  \cdots  \oplus  {L}_{n}^{ * }
\]

and

\[
c\left( {E}^{ * }\right)  = \left( {1 - {c}_{1}\left( {L}_{1}\right) }\right) \cdots \left( {1 - {c}_{1}\left( {L}_{n}\right) }\right) .
\]

Therefore

\[
{c}_{q}\left( {E}^{ * }\right)  = {\left( -1\right) }^{q}{c}_{q}\left( E\right) .
\]

By the splitting principle this result holds for all complex vector bundles \( E \) .

EXAMPLE 21.13 (The Chern classes of the complex projective space). By analogy with the definition of a differentiable manifold, we say that a second countable, Hausdorff space \( M \) is a complex manifold of dimension \( n \) if every point has a neighborhood \( {U}_{\alpha } \) homeomorphic to some open ball in \( {\mathbb{C}}^{n},{\phi }_{\alpha } : {U}_{\alpha } \rightarrow  {\mathbb{C}}^{n} \) , such that the transition functions

\[
{g}_{\alpha \beta } = {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1} : {\phi }_{\beta }\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \rightarrow  {\mathbb{C}}^{n}
\]

are holomorphic. Smooth maps and smooth vector bundles have obvious analogues in the holomorphic category. If \( {u}_{1},\ldots ,{u}_{n} \) are the coordinate functions on \( {\mathbb{C}}^{n} \) , then \( {z}_{i} = {u}_{i} \circ  {\phi }_{\alpha }, i = 1,\ldots , n \) , are the coordinate functions on \( {U}_{\alpha } \) . At each point \( p \) in \( {U}_{\alpha } \) the vectors \( \partial /\partial {z}_{1},\ldots ,\partial /\partial {z}_{n} \) span over \( \mathbb{C} \) the holomorphic tangent bundle of \( M \) . It is a complex vector bundle of rank \( n \) . The Chern class of a complex manifold is defined to be the Chern class of its holomorphic tangent bundle.

The complex projective space \( \mathbb{C}{P}^{n} \) is an example of a complex manifold, since, as in Exercise 6.44, the transition functions \( {g}_{ji} \) relative to the standard open cover are given by multiplication by \( {z}_{i}/{z}_{j} \) , which are holomorphic functions from \( {\phi }_{i}\left( {{U}_{i} \cap  {U}_{j}}\right) \) to \( {\phi }_{j}\left( {{U}_{i} \cap  {U}_{j}}\right) \) . Recall that there is a tautological exact sequence on \( \mathbb{C}{P}^{n} \)

\[
0 \rightarrow  S \rightarrow  {\mathbb{C}}^{n + 1} \rightarrow  Q \rightarrow  0
\]

where \( {\mathbb{C}}^{n + 1} \) denotes the trivial bundle of rank \( n + 1 \) over \( \mathbb{C}{P}^{n} \) . A tangent vector to \( \mathbb{C}{P}^{n} \) at a line \( \ell \) in \( {\mathbb{C}}^{n + 1} \) may be regarded as an infinitesimal motion of the line \( \ell \) (Figure 21.1). Such a motion corresponds to a linear map from \( \ell \) to the quotient space \( {\mathbb{C}}^{n + 1}/\ell \) , which may be represented by the complementary subspace of \( \ell \) in \( {\mathbb{C}}^{n + 1} \) (relative to some metric). Thus, denoting the holomorphic tangent bundle by \( T \) , we have

\[
T \simeq  \operatorname{Hom}\left( {S, Q}\right)  = Q \otimes  {S}^{ * }.
\]

![bo_d7b6f8alb0pc73dd9avg_291_564_297_498_376_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_291_564_297_498_376_0.jpg)

Figure 21.1

We will compute the Chern class of \( T \) in two ways.

(1) Tensoring the tautological sequence with \( {S}^{ * } \) , we get

\[
0 \rightarrow  \mathbb{C} \rightarrow  {S}^{ * } \otimes  {\mathbb{C}}^{n + 1} \rightarrow  {S}^{ * } \otimes  Q \rightarrow  0.
\]

By the Whitney product formula

\[
c\left( T\right)  = c\left( {{S}^{ * } \otimes  Q}\right)  = c\left( {{S}^{ * } \otimes  {\mathbb{C}}^{n + 1}}\right)  = c\left( {{S}^{ * } \oplus  \cdots  \oplus  {S}^{ * }}\right)  = {\left( 1 + x\right) }^{n + 1},
\]

where \( x = {c}_{1}\left( {S}^{ * }\right) \) .

(2) From the tautological exact sequence and the Whitney product formula

\[
c\left( Q\right)  = \frac{1}{c\left( S\right) } = \frac{1}{1 - x} = 1 + x + \cdots  + {x}^{n},
\]

since \( {x}^{n + 1} = 0 \) in \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) . By (21.10)

\[
c\left( {\mathbb{C}{P}^{n}}\right)  = c\left( {Q \otimes  {S}^{ * }}\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{c}_{i}\left( Q\right) {\left( 1 + x\right) }^{n - i} = \mathop{\sum }\limits_{{i = 0}}^{n}{x}^{i}{\left( 1 + x\right) }^{n - i}
\]

\[
= {\left( 1 + x\right) }^{n}\mathop{\sum }\limits_{{i = 0}}^{n}{\left( \frac{x}{1 + x}\right) }^{i}
\]

\[
= {\left( 1 + x\right) }^{n}\left\lbrack  {\left( {1 - {\left( \frac{x}{1 + x}\right) }^{n + 1}}\right) /\left( {1 - \frac{x}{1 + x}}\right) }\right\rbrack
\]

\[
= {\left( 1 + x\right) }^{n + 1}\left\lbrack  {1 - {\left( \frac{x}{1 + x}\right) }^{n + 1}}\right\rbrack
\]

\[
= {\left( 1 + x\right) }^{n + 1} - {x}^{n + 1}
\]

\[
= {\left( 1 + x\right) }^{n + 1}\text{ . }
\]

Exercise 21.14. Chern classes of a hypersurface in a complex projective space. Let \( H \) be the hyperplane bundle over the projective space \( \mathbb{C}{P}^{n} \) (see (20.3)), and \( {H}^{\otimes k} \) the tensor product of \( k \) copies of \( H \) . The line bundle \( H \) is in fact more than a \( {C}^{\infty } \) complex line bundle; because its transition functions are holomorphic, it is a holomorphic line bundle. The total space of a holomorphic bundle over a complex manifold is again a complex manifold, so that the notion of a holomorphic section makes sense. The zero locus of a holomorphic section of \( {H}^{\otimes k} \) is called a hypersurface of degree \( k \) in \( \mathbb{C}{P}^{n} \) . If the section is transversal to the zero section, then the hypersurface is a smooth complex manifold. Compute the Chern classes of a smooth hypersurface of degree \( k \) in \( \mathbb{C}{P}^{n} \) . (Hint: apply Prop. 12.7 to get the normal bundle of the hypersurface.)

## Flag Manifolds

Given a complex vector space \( V \) of dimension \( n \) , a flag in \( V \) is a sequence of subspaces \( {A}_{1} \subset  {A}_{2} \subset  \cdots  \subset  {A}_{n} = V,{\dim }_{\mathbb{C}}{A}_{i} = i \) . Let \( {Fl}\left( V\right) \) be the collection of all flags in \( V \) . Clearly any flag can be carried into any other flag in \( V \) by an element of the general linear group \( {GL}\left( {n,\mathbb{C}}\right) \) , and the stabilizer at a flag is the group \( H \) of the upper triangular matrices. So as a set \( {Fl}\left( V\right) \) is isomorphic to the coset space \( {GL}\left( {n,\mathbb{C}}\right) /H \) . Since the quotient of a Lie group by a closed subgroup is a manifold (Warner [1, p. 120]), \( {Fl}\left( V\right) \) can be made into a manifold. It is called the flag manifold of \( V \) .

Given a vector bundle \( E \) , just as one can form its projectivization \( P\left( E\right) \) , so one can form its associated flag bundle \( {Fl}\left( E\right) \) . The bundle \( {Fl}\left( E\right) \) is obtained from \( E \) by replacing each fiber \( {E}_{p} \) by the flag manifold \( {Fl}\left( {E}_{p}\right) \) ; the local trivialization \( {\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{C}}^{n} \) induces a natural trivialization \( {\left. Fl\left( E\right) \right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {Fl}\left( {\mathbb{C}}^{n}\right) \) . Since \( {GL}\left( {n,\mathbb{C}}\right) \) acts on \( {Fl}\left( {\mathbb{C}}^{n}\right) \) , we may take the transition functions of \( {Fl}\left( E\right) \) to be those of \( E \) , but note that \( {Fl}\left( E\right) \) is not a vector bundle.

Proposition 21.15. The associated flag bundle \( {Fl}\left( E\right) \) of a vector bundle is the split manifold \( F\left( E\right) \) constructed earlier.

Proof. We first show this for \( E = V \) a vector space of dimension 3, viewed as a rank 3 vector bundle over a point.

![bo_d7b6f8alb0pc73dd9avg_292_325_1867_994_315_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_292_325_1867_994_315_0.jpg)

In what follows all lines and planes go through the origin. A point in \( P\left( V\right) \) is a line \( L \) in \( V \) . A point of \( P\left( {Q}_{V}\right) \) is a line \( L \) in \( V \) and a line \( L \) in \( V/L.L \) may be regarded as a 2-plane in \( V \) containing \( L \) . Thus \( {Fl}\left( V\right)  = \; P\left( {Q}_{V}\right)  = \left\{  {{A}_{1} \subset  {A}_{2} \subset  V,\dim {A}_{i} = i}\right\}   = F\left( V\right) . \)

Now let \( E \) be a vector bundle of rank \( n \) over \( M \) . The split manifold \( F\left( E\right) \) is obtained by a sequence of \( n - 1 \) projectivizations as in (21.2). A point of \( P\left( E\right) \) is a pair \( \left( {p,\ell }\right) \) , where \( p \) is in \( M \) and \( \ell \) is a line in \( {E}_{p} \) . By introducing a Hermitian metric on \( E \) , we may regard all the quotient bundles \( {Q}_{1},\ldots \) , \( {Q}_{n - 1} \) in (21.2) as subbundles of \( E \) . Then a point of \( P\left( {Q}_{1}\right) \) over \( \left( {p,{\ell }_{1}}\right) \) in \( P\left( E\right) \) is a triple \( \left( {p,{\ell }_{1},{\ell }_{2}}\right) \) where \( {\ell }_{2} \) is a line in the orthogonal complement of \( {\ell }_{1} \) in \( {E}_{p} \) . A point of \( P\left( {Q}_{2}\right) \) over \( \left( {p,{\ell }_{1},{\ell }_{2}}\right) \) in \( P\left( {Q}_{1}\right) \) is a 4-tuple \( \left( {p,{\ell }_{1},{\ell }_{2},{\ell }_{3}}\right) \) where \( {\ell }_{3} \) is a line in the orthogonal complement of \( {\ell }_{1} \) and \( {\ell }_{2} \) in \( {E}_{p} \) . Thus, more generally, a point in the split manifold \( F\left( E\right)  = P\left( {Q}_{n - 1}\right) \) may be identified with the flag

\[
\left( {p,{\ell }_{1} \subset  \left\{  {{\ell }_{1},{\ell }_{2}}\right\}   \subset  \left\{  {{\ell }_{1},{\ell }_{2},{\ell }_{3}}\right\}   \subset  \cdots  \subset  {E}_{p}}\right) .
\]

This proves the equality of the split manifold \( F\left( E\right) \) and the flag bundle \( {Fl}\left( E\right) \) .

From now on the notations \( F\left( E\right) \) and \( {Fl}\left( E\right) \) will be used interchangeably.

The formula (21.3) gives one description of the vector space structure of the cohomology of a flag bundle. To compute its ring structure we first recall from (20.7) that if \( E \) is a rank \( n \) complex vector bundle over \( M \) , then the cohomology ring of its projectivization is

\[
{H}^{ * }\left( {P\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  x\right\rbrack  /\left( {{x}^{n} + {c}_{1}\left( E\right) {x}^{n - 1} + \cdots  + {c}_{n}\left( E\right) }\right) \text{ , where }x = {c}_{1}\left( {S}^{ * }\right) \text{ . }
\]

Notation. If \( A \) is a graded ring, and \( a, b, c, f \in  A \) , then \( \left( {a, b, c}\right) \) denotes the ideal generated by \( a, b \) , and \( c \) , while \( \left( {f = 0}\right) \) denotes the ideal generated by the homogeneous components of \( f \) .

There is an alternate description of the ring structure which is sometimes very useful. We write \( {H}^{ * }\left( M\right) \left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack \) for \( {H}^{ * }\left( M\right) \left\lbrack  {{c}_{1}\left( S\right) ,{c}_{1}\left( Q\right) ,\ldots ,{c}_{n - 1}\left( Q\right) }\right\rbrack \) , where \( S \) and \( Q \) are the universal subbundle and quotient bundle on \( P\left( E\right) \) .

![bo_d7b6f8alb0pc73dd9avg_293_623_1610_413_270_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_293_623_1610_413_270_0.jpg)

Proposition 21.16. \( {H}^{ * }\left( {P\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack  /\left( {c\left( S\right) c\left( Q\right)  = {\pi }^{ * }c\left( E\right) }\right) \) .

Proof. The idea is to eliminate the generators \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{n - 1}\left( Q\right) \) by using the relation \( c\left( S\right) c\left( Q\right)  = {\pi }^{ * }c\left( E\right) \) . Let \( x = {c}_{1}\left( {S}^{ * }\right) ,{y}_{i} = {c}_{i}\left( Q\right) \) , and \( {c}_{i} = {\pi }^{ * }{c}_{i}\left( E\right) \) . Equating the terms of equal degrees in

\[
\left( {1 - x}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{n - 1}}\right)  = 1 + {c}_{1} + \cdots  + {c}_{n},
\]

we get

\[
{y}_{1} - x = {c}_{1}
\]

\[
{y}_{2} - x{y}_{1} = {c}_{2}
\]

\[
{y}_{3} - x{y}_{2} = {c}_{3}
\]

\[
{y}_{n - 1} - x{y}_{n - 2} = {c}_{n - 1}
\]

\[
- x{y}_{n - 1} = {c}_{n}.
\]

By the first \( n - 1 \) equations, \( {y}_{1},\ldots ,{y}_{n - 1} \) can be expressed in terms of \( x \) and elements of \( {H}^{ * }\left( M\right) \) , and so can be eliminated as generators of \( {H}^{ * }\left( M\right) \left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack  /\left( {c\left( S\right) c\left( Q\right)  = {\pi }^{ * }c\left( E\right) }\right) \) . The last equation \( - x{y}_{n - 1} = {c}_{n} \) translates into

(*)

\[
{x}^{n} + {c}_{1}{x}^{n - 1} + \cdots  + {c}_{n} = 0.
\]

Hence \( {H}^{ * }\left( M\right) \left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack  /\left( {c\left( S\right) c\left( Q\right)  = {\pi }^{ * }c\left( E\right) }\right) \) is isomorphic to the polynomial ring over \( {H}^{ * }\left( M\right) \) with the single generator \( x \) and the single relation (*).

By (21.2) and (21.15) the flag bundle \( {Fl}\left( E\right) \) is obtained from a sequence of \( n - 1 \) projectivizations. Applying Proposition 21.16 to (21.2), we have

\[
{H}^{ * }\left( {P\left( {Q}_{1}\right) }\right)
\]

\[
= {H}^{ * }\left( {P\left( E\right) }\right) \left\lbrack  {c\left( {S}_{2}\right) , c\left( {Q}_{2}\right) }\right\rbrack  /\left( {c\left( {S}_{2}\right) c\left( {Q}_{2}\right)  = c\left( {Q}_{1}\right) }\right)
\]

\[
= {H}^{ * }\left( M\right) \left\lbrack  {c\left( {S}_{1}\right) , c\left( {Q}_{1}\right) , c\left( {S}_{2}\right) , c\left( {Q}_{2}\right) }\right\rbrack  /\left( {c\left( {S}_{1}\right) c\left( {Q}_{1}\right)  = c\left( E\right) , c\left( {S}_{2}\right) c\left( {Q}_{2}\right)  = c\left( {Q}_{1}\right) }\right)
\]

\[
= {H}^{ * }\left( M\right) \left\lbrack  {c\left( {S}_{1}\right) , c\left( {S}_{2}\right) , c\left( {Q}_{2}\right) }\right\rbrack  /\left( {c\left( {S}_{1}\right) c\left( {S}_{2}\right) c\left( {Q}_{2}\right)  = c\left( E\right) }\right) .
\]

By induction

\[
{H}^{ * }\left( {P\left( {Q}_{n - 2}\right) }\right)
\]

\[
= {H}^{ * }\left( M\right) \left\lbrack  {c\left( {S}_{1}\right) ,\ldots , c\left( {S}_{n - 1}\right) , c\left( {Q}_{n - 1}\right) }\right\rbrack  /\left( {c\left( {S}_{1}\right) \cdots c\left( {S}_{n - 1}\right) c\left( {Q}_{n - 1}\right)  = c\left( E\right) }\right) .
\]

Writing \( {x}_{i} = {c}_{1}\left( {S}_{i}\right) , i = 1,\ldots , n - 1 \) , and \( {x}_{n} = {c}_{1}\left( {Q}_{n - 1}\right) \) , the cohomology ring of the flag bundle \( {Fl}\left( E\right) \) is

\[
{H}^{ * }\left( {\left( {{Fl}\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  {{x}_{1},\ldots ,{x}_{n}}\right\rbrack  /\left( {\mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right)  = c\left( E\right) }\right) .}\right.
\]

Specializing this theorem to a complex vector space \( V \) , considered as the trivial bundle over a point, we obtain the cohomology ring of the flag manifold

\[
{H}^{ * }\left( {\left( {{Fl}\left( V\right) }\right)  = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{n}}\right\rbrack  /\left( {\mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right)  = 1}\right) .}\right.
\]

As for the Poincaré polynomial of the flag manifold we note again that the flag manifold is obtained by a sequence of \( n - 1 \) projectivizations (21.2).

By (20.8) each time we projectivize a rank \( k \) vector bundle, the Poincaré polynomial is multiplied by \( \left( {1 - {t}^{2k}}\right) /\left( {1 - {t}^{2}}\right) \) . So the Poincaré polynomial of the flag manifold \( {Fl}\left( V\right) \) is

\[
{P}_{t}\left( {{Fl}\left( V\right) }\right)  = \frac{1 - {t}^{2n}}{1 - {t}^{2}} \cdot  \frac{1 - {t}^{{2n} - 2}}{1 - {t}^{2}} \cdot  \cdots  \cdot  \frac{1 - {t}^{2}}{1 - {t}^{2}}.
\]

This discussion may be summarized in the following proposition.

Proposition 21.17. Let \( V \) be a complex vector space of dimension \( n \) . The cohomology ring of the flag manifold \( {Fl}\left( V\right) \) is

\[
{H}^{ * }\left( {{Fl}\left( V\right) }\right)  = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{n}}\right\rbrack  /\left( {\mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right)  = 1}\right) .
\]

It has Poincaré polynomial

\[
{P}_{t}\left( {{Fl}\left( V\right) }\right)  = \frac{\left( {1 - {t}^{2}}\right) \left( {1 - {t}^{4}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2}}\right) }.
\]

REMARK 21.18. Similarly, if \( E \) is a rank \( n \) complex vector bundle over a manifold \( M \) , then the cohomology ring of the flag bundle \( {Fl}\left( E\right) \) is

\[
{H}^{ * }\left( {{Fl}\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  {{x}_{1},\ldots ,{x}_{n}}\right\rbrack  /\left( {\mathop{\prod }\limits_{{i = 1}}^{n}\left( {1 + {x}_{i}}\right)  = c\left( E\right) }\right) ,
\]

and the Poincaré series is

\[
{P}_{t}\left( {{Fl}\left( E\right) }\right)  = {P}_{t}\left( M\right) \frac{\left( {1 - {t}^{2}}\right) \left( {1 - {t}^{4}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2}}\right) }.
\]

REMARK 21.19. Since projectivization does not introduce any torsion element in integer cohomology, the integer cohomology ring of the flag manifold \( {Fl}\left( V\right) \) is torsion-free and is given by the same formula as (21.17) with \( \mathbb{Z} \) in place of \( \mathbb{R} \) . The integer cohomology ring of a flag bundle is given by the same formula as (21.18). In fact, with a little care, the entire discussion can be translated into the Čech theory.
