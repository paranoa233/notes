## §23 The Search for the Universal Bundle

Let \( f : M \rightarrow  N \) be a map between two manifolds and \( E \) a complex bundle over \( N \) . The pullback \( {f}^{-1}E \) is a bundle over \( M \) . If the Chern classes of \( E \) vanish, by the naturality property (20.10.1), so do those of \( {f}^{-1}E \) . Taking the Chern classes to be a measure of the twisting of a bundle, we may assert that pulling back "dilutes" a bundle, i.e., makes it less twisted. One extreme example is when \( f \) is constant; in this case \( {f}^{-1}E \) is trivial. Another example is the flag construction of Section 21; pulling \( E \) back to the split manifold \( F\left( E\right) \) splits \( E \) into a direct sum of line bundles. One may wonder if there exists a bundle which is so twisted that every bundle is a pullback of this universal bundle. Such a bundle indeed exists, at least for manifolds of finite type; it is the universal quotient bundle on the Grassmannian \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) for \( n \) sufficiently large. We will prove this result and conclude from it that every natural transformation from the complex vector bundles to the cohomology classes is expressible in terms of the Chern classes, all for manifolds of finite type. We also indicate how the theorems generalize to an arbitrary manifold.

## The Grassmannian

Let \( V \) be a complex vector space of dimension \( n \) . The complex Grassmannian \( {G}_{k}\left( V\right) \) is the set of all subspaces of complex codimension \( k \) in \( V \) . We sometimes call such a subspace an \( \left( {n - k}\right) \) -plane in \( V \) . Given a Hermitian metric on \( V \) , the unitary group \( U\left( n\right) \) is the group of all metric-preserving endomorphisms of \( V \) . Clearly \( U\left( n\right) \) acts transitively on the collection of all \( \left( {n - k}\right) \) -planes in \( V \) . Since a unitary matrix which sends an \( \left( {n - k}\right) \) -plane to itself must also fix the complementary orthogonal \( k \) -plane, the stabilizer of an \( \left( {n - k}\right) \) -plane in \( V \) is \( U\left( {n - k}\right)  \times  U\left( k\right) \) . Thus the Grassmannian can be represented as a homogeneous space

\[
{G}_{k}\left( V\right)  = \frac{U\left( n\right) }{U\left( k\right)  \times  U\left( {n - k}\right) }.
\]

As the coset space of a Lie group by a closed subgroup, \( {G}_{k}\left( V\right) \) is a differentiable manifold (Warner [1, p. 120]). Note that \( {G}_{n - 1}\left( V\right) \) is the projective space \( P\left( V\right) \) .

Just as in the case of the projective space, over the Grassmannian \( {G}_{k}\left( V\right) \) there are three tautological bundles: the universal subbundle \( S \) , whose fiber at each point \( \Lambda \) of \( {G}_{k}\left( V\right) \) is the \( \left( {n - k}\right) \) -plane \( \Lambda \) itself; the product bundle \( \widehat{V} = {G}_{k}\left( V\right)  \times  V \) ; and the universal quotient bundle \( Q \) defined by

\[
0 \rightarrow  S \rightarrow  \widehat{V} \rightarrow  Q \rightarrow  0
\]

This exact sequence is called the tautological sequence on \( {G}_{k}\left( V\right) \) . Over \( {G}_{k}\left( V\right) \) the universal subbundle \( S \) has rank \( n - k \) and the universal quotient bundle has rank \( k \) .

Similarly, if \( V \) is a real vector space, one can define the real Grassmannian \( {G}_{k}\left( V\right) \) of codimension \( k \) real subspaces of \( V \) , and the analogous real universal bundles. The real Grassmannian can also be represented as a homogeneous space

\[
{G}_{k}\left( {\mathbb{R}}^{n}\right)  = \frac{O\left( n\right) }{O\left( k\right)  \times  O\left( {n - k}\right) }.
\]

Proposition 23.1. The cohomology of the complex Grassmannian \( {G}_{k}\left( V\right) \) has Poincaré polynomial

\[
{P}_{t}\left( {{G}_{k}\left( V\right) }\right)  = \frac{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2k}}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2\left( {n - k}\right) }}\right) }.
\]

Proof. The flag manifold \( F\left( V\right) \) may be obtained from the Grassmannian \( {G}_{k}\left( V\right) \) by a series of flag constructions as follows. Let \( \widehat{Q} \) be the pullback of \( Q \) to the flag bundle \( F\left( S\right) \) .

![bo_d7b6f8alb0pc73dd9avg_303_644_447_329_243_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_303_644_447_329_243_0.jpg)

A point of \( F\left( S\right) \) is a pair \( \left( {\Lambda ,{L}_{1} \subset  \cdots  \subset  \Lambda }\right) \) consisting of an \( \left( {n - k}\right) \) -plane \( \Lambda \) in \( V \) together with a flag in \( \Lambda \) . Therefore a point in \( F\left( \widehat{Q}\right) \) consists of a point in \( F\left( S\right) ,\left( {\Lambda ,{L}_{1} \subset  \cdots  \subset  \Lambda }\right) \) , together with a flag in \( V/\Lambda \) , i.e., a point in \( F\left( \widehat{Q}\right) \) is given by \( \left( {\Lambda ,{L}_{1} \subset  \cdots  \subset  {L}_{n - k - 1} \subset  \Lambda  \subset  {L}_{n - k + 1} \subset  \cdots  \subset  V}\right) \) . So \( F\left( \widehat{Q}\right) \) is the flag manifold \( F\left( V\right) \) , and \( F\left( V\right) \) is obtained from the Grassmannian \( {G}_{k}\left( V\right) \) by two flag constructions. By (21.18), the Poincaré polynomials of \( F\left( V\right) \) and \( {G}_{k}\left( V\right) \) satisfy the relation

\[
{P}_{t}\left( {F\left( V\right) }\right)  = {P}_{t}\left( {{G}_{k}\left( V\right) }\right) \frac{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2\left( {n - k}\right) }}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2k}}\right) }{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2}}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2}}\right) }.
\]

From (21.17) it follows that

\[
{P}_{t}\left( {{G}_{k}\left( V\right) }\right)  = \frac{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2\left( {n - k}\right) }}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2k}}\right) }.
\]

As for the ring structure of the cohomology of the Grassmannian \( {G}_{k}\left( V\right) \) , we have the following.

Proposition 23.2. Let \( V \) be a complex vector space of dimension \( n \) .

(a) As a ring

\[
{H}^{ * }\left( {{G}_{k}\left( V\right) }\right)  = \frac{\mathbb{R}\left\lbrack  {{c}_{1}\left( S\right) ,\ldots ,{c}_{n - k}\left( S\right) ,{c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) }\right\rbrack  }{\left( c\left( S\right) c\left( Q\right)  = 1\right) }
\]

(b) The Chern classes \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) \) of the quotient bundle generate the cohomology ring \( {H}^{ * }\left( {{G}_{k}\left( V\right) }\right) \) .

(c) For a fixed \( k \) and a fixed \( i \) there are no polynomial relations of degree \( i \) among \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) \) if the dimension of \( V \) is large enough.

Proof. In the proof of Proposition 23.1, we saw that the flag manifold \( F\left( V\right) \) is obtained from the Grassmannian by two flag constructions By (21.18) the cohomology ring of the flag manifold is

\[
{H}^{ * }\left( {F\left( V\right) }\right)  = \frac{{H}^{ * }\left( {{G}_{k}\left( V\right) }\right) \left\lbrack  {{x}_{1},\ldots ,{x}_{n - k},{y}_{1},\ldots ,{y}_{k}}\right\rbrack  }{\left( \prod \left( 1 + {x}_{i}\right)  = c\left( S\right) ,\prod \left( 1 + {y}_{j}\right)  = c\left( Q\right) \right) }.
\]

![bo_d7b6f8alb0pc73dd9avg_303_589_1902_478_247_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_303_589_1902_478_247_0.jpg)

On the other hand, we’ve computed the cohomology of \( F\left( V\right) \) in (21.17) to be

(*)

\[
\text{ (*) }{H}^{ * }\left( {F\left( V\right) }\right)  = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{n - k},{y}_{1},\ldots ,{y}_{k}}\right\rbrack  /\left( {\prod \left( {1 + {x}_{i}}\right) \prod \left( {1 + {y}_{j}}\right)  = 1}\right) \text{ . }
\]

Thus in \( {H}^{ * }\left( {{G}_{k}\left( V\right) }\right) \) the Chern classes of \( S \) and \( Q \) can satisfy no relation other than \( c\left( S\right) c\left( Q\right)  = 1 \) , for any relation among them would appear as a relation among the \( {x}_{i} \) ’s and \( {y}_{j} \) ’s in (*). It follows that there is an injection of algebras

(23.2.1)

\[
\frac{\mathbb{R}\left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack  }{\left( c\left( S\right) c\left( Q\right)  = 1\right) } \hookrightarrow  {H}^{ * }\left( {{G}_{k}\left( V\right) }\right)
\]

From the digression following this proof, the Poincaré series of \( \mathbb{R}\left\lbrack  {{c}_{1}\left( S\right) ,\ldots ,{c}_{n - k}\left( S\right) ,{c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) }\right\rbrack  /\left( {c\left( S\right) c\left( Q\right)  = 1}\right) \) is

\[
{P}_{t}\left( \frac{\mathbb{R}\left\lbrack  {c\left( S\right) , c\left( Q\right) }\right\rbrack  }{\left( c\left( S\right) c\left( Q\right)  = 1\right) }\right)  = \frac{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2\left( {n - k}\right) }}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2k}}\right) }.
\]

But this is also the Poincaré series of \( {H}^{ * }\left( {{G}_{k}\left( V\right) }\right) \) . Thus the injection (23.2.1) is an isomorphism. This proves (a).

Writing \( c\left( S\right)  = 1/c\left( Q\right) \) , we see from the description of the ring structure in (a) that \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) \) generate the cohomology ring of \( {G}_{k}\left( V\right) \) .

The equation \( c\left( S\right)  = 1/c\left( Q\right) \) not only allows one to eliminate \( {c}_{1}\left( S\right) ,\ldots \) , \( {c}_{n - k}\left( S\right) \) in terms of \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) \) , but also gives polynomial relations of degrees \( 2\left( {n - k + 1}\right) ,\ldots ,{2n} \) among \( {c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) \) . Thus for a given degree \( i \) , if the dimension \( n \) of the vector space \( V \) is so large that \( 2\left( {n - k + 1}\right)  > i \) , then there are no polynomial relations of degree \( i \) among the Chern classes of \( Q \) .

## Digression on the Poincaré Series of a Graded Algebra

Let \( k \) be a field and \( A = {\bigoplus }_{i = 1}^{\infty }{A}_{i} \) a graded algebra over \( k \) . The Poincaré series of \( A \) is defined to be

\[
{P}_{t}\left( A\right)  = \mathop{\sum }\limits_{{i = 0}}^{\infty }\left( {{\dim }_{k}{A}_{i}}\right) {t}^{i}
\]

If \( A \) is a graded \( \mathbb{Z} \) -module, its Poincaré series is defined to be that of the \( \mathbb{Q} \) -algebra \( A{ \otimes  }_{\mathrm{Z}}\mathbb{Q} \) .

EXAMPLE. Let \( A \) be the polynomial ring \( \mathbb{R}\left\lbrack  x\right\rbrack \) , where \( x \) is an element of degree \( n \) . Then

\[
{P}_{t}\left( A\right)  = 1 + {t}^{n} + {t}^{2n} + \cdots  = \frac{1}{1 - {t}^{n}}.
\]

EXAMPLE. Let \( A \) and \( B \) be two graded algebras. Suppose a basis for \( A \) as a vector space is \( {\left\{  {x}_{i}\right\}  }_{i \in  I} \) and a basis for \( B \) is \( {\left\{  {y}_{j}\right\}  }_{j \in  J} \) . Then a vector space basis for \( A \otimes  B \) is \( {\left\{  {x}_{i} \otimes  {y}_{j}\right\}  }_{i \in  I, j \in  J} \) . Therefore

\[
{P}_{t}\left( {A \otimes  B}\right)  = {P}_{t}\left( A\right) {P}_{t}\left( B\right) .
\]

EXAMPLE. Let \( A = \mathbb{R}\left\lbrack  {x, y}\right\rbrack \) , with \( \deg x = m \) and \( \deg y = n \) . Then since \( \mathbb{R}\left\lbrack  {x, y}\right\rbrack   = \mathbb{R}\left\lbrack  x\right\rbrack   \otimes  \mathbb{R}\left\lbrack  y\right\rbrack  , \)

\[
{P}_{t}\left( A\right)  = {P}_{t}\left( {\mathbb{R}\left\lbrack  x\right\rbrack  }\right) {P}_{t}\left( {\mathbb{R}\left\lbrack  y\right\rbrack  }\right)  = \frac{1}{1 - {t}^{m}} \cdot  \frac{1}{1 - {t}^{n}}.
\]

We next investigate the effect of a relation on the Poincaré series of a graded algebra.

Proposition 23.3. Let \( A = {\bigoplus }_{i = 0}^{\infty }{A}_{i} \) be a graded algebra over a field \( k \) , and \( x \) a homogeneous element of degree \( n \) in \( A \) . If \( x \) is not a zero-divisor, then

\[
{P}_{t}\left( {A/{xA}}\right)  = {P}_{t}\left( A\right) \left( {1 - {t}^{n}}\right) .
\]

Proof. Because \( x \) is not a zero-divisor, multiplication by \( x \) is an injection. Hence for each integer \( i \) there is an exact sequence of vector spaces

\[
0 \rightarrow  {A}_{i}\overset{x}{ \rightarrow  }{A}_{i + n} \rightarrow  {\left( A/xA\right) }_{i + n} \rightarrow  0.
\]

By the additivity of the dimension,

\[
\dim {A}_{i + n} = \dim {A}_{i} + \dim {\left( A/xA\right) }_{i + n}.
\]

Summing over all \( i \) ,

\[
\mathop{\sum }\limits_{{i =  - n}}^{\infty }\left( {\dim {A}_{i + n}}\right) {t}^{i + n} = \mathop{\sum }\limits_{{i =  - n}}^{\infty }\left( {\dim {A}_{i}}\right) {t}^{i + n} + \mathop{\sum }\limits_{{i =  - n}}^{\infty }\dim {\left( A/xA\right) }_{i + n}{t}^{i + n},
\]

where we set \( {A}_{i} = \{ 0\} \) if \( i \) is negative. Hence

\[
{P}_{t}\left( A\right)  = {P}_{t}\left( A\right) {t}^{n} + {P}_{t}\left( {A/{xA}}\right) .
\]

EXAMPLE. If \( x, y \) , and \( z \) are elements of degree 1, then the Poincaré series of \( A = \mathbb{R}\left\lbrack  {x, y, z}\right\rbrack  /\left( {{x}^{3}y + {y}^{2}{z}^{2} + x{y}^{2}z}\right) \) is

\[
{P}_{t}\left( A\right)  = {P}_{t}\left( {\mathbb{R}\left\lbrack  {x, y, z}\right\rbrack  }\right) \left( {1 - {t}^{4}}\right)
\]

\[
= \left( {1 - {t}^{4}}\right) /{\left( 1 - t\right) }^{3}.
\]

To generalize Proposition 23.3, we will need the notion of a regular sequence.

Definition. Let \( A \) be a ring. A sequence of elements \( {a}_{1},\ldots ,{a}_{r} \) in \( A \) is a regular sequence if \( {a}_{1} \) is not a zero-divisor in \( A \) and for each \( i \geq  2 \) , the image of \( {a}_{i} \) in \( A/\left( {{a}_{1},\ldots ,{a}_{i - 1}}\right) \) is not a zero-divisor.

Proposition 23.4. Let \( A \) be a graded algebra over a field \( k \) and \( {a}_{1},\ldots ,{a}_{r} \) a regular sequence of homogeneous elements of degrees \( {n}_{1},\ldots ,{n}_{r} \) . Then

\[
{P}_{t}\left( {A/\left( {{a}_{i},\ldots ,{a}_{r}}\right) }\right)  = {P}_{t}\left( A\right) \left( {1 - {t}^{{n}_{1}}}\right) \cdots \left( {1 - {t}^{{n}_{r}}}\right) .
\]

Proof. This is an immediate consequence of Proposition 23.3 and induction on \( r \) .

Let \( I \) be the ideal in \( \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{j},{y}_{1},\ldots ,{y}_{k}}\right\rbrack \) generated by the homogeneous terms of \( \left( {1 + {x}_{1} + \cdots  + {x}_{j}}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{k}}\right)  - 1 \) , where \( \deg {x}_{i} = {2i} \) and \( \deg {y}_{i} = {2i} \) . We will now compute the Poincaré series of \( \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{j}}\right. \) , \( \left. {{y}_{1},\ldots ,{y}_{k}}\right\rbrack  /I \) .

Lemma 23.5. Let \( A \) be a graded algebra over a field \( k \) . If \( {a}_{1},\ldots ,{a}_{r} \) is a regular sequence of homogeneous elements of positive degrees in \( A \) , so is any permutation of \( {a}_{1},\ldots ,{a}_{r} \) .

Proof. Since any permutation is a product of transpositions of adjacent elements, it suffices to show that \( {a}_{1},\ldots ,{a}_{i - 1},{a}_{i + 1},{a}_{i},\ldots ,{a}_{r} \) is a regular sequence. For this it is enough to show that in the ring \( A/\left( {{a}_{1},\ldots ,{a}_{i - 1}}\right) \) , the images of \( {a}_{i + 1},{a}_{i} \) form a regular sequence. In this way the lemma is reduced to the case of two elements: if \( a, b \) is a regular sequence of elements of positive degrees in the graded algebra \( A \) , so is \( b, a \) .

If \( x \) is an element of \( A \) , we write \( \bar{x} \) for the image of \( x \) in whatever quotient ring of \( A \) being discussed. Assume that \( a, b \) is a regular sequence in A.

(1) Suppose \( {bx} = 0 \) in \( A \) . Then \( \bar{b}\bar{x} = 0 \) in \( A/\left( a\right) \) . Since \( \bar{b} \) is not a zero-divisor in \( A/\left( a\right) , x = a{x}_{1} \) for some \( {x}_{1} \) in \( A \) . Therefore, \( {ab}{x}_{1} = 0 \) in \( A \) . Since \( a \) is not a zero divisor, \( b{x}_{1} = 0 \) . Repeating the argument, we get \( {x}_{1} = a{x}_{2} \) , \( {x}_{2} = a{x}_{3} \) , and so on. Thus \( x = a{x}_{1} = {a}^{2}{x}_{2} = {a}^{3}{x}_{3} = \ldots \) , showing that \( x \) is divisible by all the powers of \( a \) . Since \( a \) has positive degree, this is possible only if \( x = 0 \) . Therefore \( b \) is not a zero-divisor in \( A \) .

(2) Next we show that \( \bar{a} \) is not a zero-divisor in \( A/\left( b\right) \) . Suppose \( \bar{a}\bar{x} = 0 \) in \( A/\left( b\right) \) . Then \( {ax} = {by} \) for some \( y \) in \( A \) . It follows that \( \bar{b}\bar{y} = 0 \) in \( A/\left( a\right) \) . Since \( b \) is not a zero-divisor in \( A/\left( a\right) , y = {az} \) for some \( z \) . Therefore, \( {ax} = {abz} \) . Since \( a \) is not a zero-divisor in \( A, x = {bz} \) ; hence, \( \bar{x} = 0 \) in \( A/\left( b\right) \) .

Lemma 23.6. If \( {a}_{1},\ldots ,{a}_{r}, b \) and \( {a}_{1},\ldots ,{a}_{r}, c \) are regular sequences in a ring \( A \) , then so is \( {a}_{1},\ldots ,{a}_{r},{bc} \) .

Proof. It suffices to check that \( {bc} \) is not a zero-divisor in \( A/\left( {{a}_{1},\ldots ,{a}_{r}}\right) \) . This is clear since by hypothesis neither \( b \) nor \( c \) is a zero-divisor in \( A/\left( {{a}_{1},\ldots ,{a}_{r}}\right) \) .

Proposition 23.7. The homogeneous terms of

\[
\left( {1 + {x}_{1} + \cdots  + {x}_{j}}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{k}}\right)  - 1
\]

form a regular sequence in \( A = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{j},{y}_{1},\ldots ,{y}_{k}}\right\rbrack \) .

Proof. The proof proceeds by induction on \( j \) and \( k \) . Suppose \( j = 1 \) and \( k = 1 \) . Then \( \mathbb{R}\left\lbrack  {{x}_{1},{y}_{1}}\right\rbrack  /\left( {{x}_{1} + {y}_{1}}\right)  = \mathbb{R}\left\lbrack  {x}_{1}\right\rbrack \) and the image of \( {x}_{1}{y}_{1} \) in \( \mathbb{R}\left\lbrack  {{x}_{1}\text{ , }}\right. \; {y}_{1}\rbrack /\left( {{x}_{1} + {y}_{1}}\right) \) is \( - {x}_{1}^{2} \) , which is not a zero divisor. So \( {x}_{1} + {y}_{1},{x}_{1}{y}_{1} \) is a regular sequence in \( \mathbb{R}\left\lbrack  {{x}_{1},{y}_{1}}\right\rbrack \) . For a general \( j \) and \( k \) , let \( {f}_{i} \) be the homogeneous term of degree \( i \) in \( \left( {1 + {x}_{1} + \cdots  + {x}_{j}}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{k}}\right)  - 1 \) . We first show that \( {f}_{1},\ldots ,{f}_{j + k - 1},{x}_{j} \) and \( {f}_{1},\ldots ,{f}_{j + k - 1},{y}_{k} \) are regular sequences. By Lemma 23.5, \( {f}_{1},\ldots ,{f}_{j + k - 1},{x}_{j} \) is a regular sequence if and only if \( {x}_{j},{f}_{1},\ldots \) , \( {f}_{j + k - 1} \) is. Let \( {\bar{f}}_{i} \) be the image of \( {f}_{i} \) in \( A/\left( {x}_{j}\right) \) . Since \( {x}_{j} \) is not a zero-divisor in \( A \) , it suffices to show that \( {\bar{f}}_{1},\ldots ,{\bar{f}}_{j + k - 1} \) is a regular sequence in \( A/\left( {x}_{j}\right) \) . This is true by the induction hypothesis, since

\[
A/\left( {x}_{j}\right)  = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{j - 1},{y}_{1},\ldots ,{y}_{k}}\right\rbrack
\]

and

\[
1 + {\bar{f}}_{1} + \cdots  + {\bar{f}}_{j + k - 1} = \left( {1 + {x}_{1} + \cdots  + {x}_{j - 1}}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{k}}\right) .
\]

Therefore, \( {f}_{1},\ldots ,{f}_{j + k - 1},{x}_{j} \) is a regular sequence in \( A \) . Similarly, \( {f}_{1},\ldots \) , \( {f}_{j + k - 1},{y}_{k} \) is also a regular sequence in \( A \) . By Lemma 23.6, so is \( {f}_{1},\ldots \) , \( {f}_{j + k - 1},{x}_{j}{y}_{k} \) .

By Propositions 23.4 and 23.7, if \( I \) is the ideal in

\[
A = \mathbb{R}\left\lbrack  {{x}_{1},\ldots ,{x}_{n - k},{y}_{1},\ldots ,{y}_{k}}\right\rbrack
\]

generated by the homogeneous terms of

\[
\left( {1 + {x}_{1} + \cdots  + {x}_{n - k}}\right) \left( {1 + {y}_{1} + \cdots  + {y}_{k}}\right)  - 1,
\]

where \( \deg {x}_{i} = {2i} \) and \( \deg {y}_{i} = {2i} \) , then the Poincaré series of \( A/I \) is

\[
{P}_{t}\left( {A/I}\right)  = \frac{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2n}}\right) }{\left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2\left( {n - k}\right) }}\right) \left( {1 - {t}^{2}}\right) \cdots \left( {1 - {t}^{2k}}\right) }
\]

## The Classification of Vector Bundles

Vector bundles over a manifold \( M \) may be classified up to isomorphism by the homotopy classes of maps from \( M \) into a Grassmannian. We will discuss this first for complex vector bundles, and then state the result for real vector bundles.

Lemma 23.8. Let \( E \) be a rank \( k \) complex vector bundle over a differentiable manifold \( M \) of finite type. There exist on \( M \) finitely many smooth sections of E which span the fiber at every point.

Proof. Let \( {\left\{  {U}_{i}\right\}  }_{i \in  I} \) be a finite good cover for \( M \) . Since \( {U}_{i} \) is contractible, \( {\left. E\right| }_{{U}_{i}} \) is trivial and so we can find \( k \) sections \( {s}_{i,1},\ldots ,{s}_{i, k} \) over \( {U}_{i} \) which form a basis of the fiber above any point in \( {U}_{i} \) . By the Shrinking Lemma (see (21.4) and (21.5)), there is an open cover \( {\left\{  {V}_{i}\right\}  }_{i \in  I} \) with \( {\bar{V}}_{i} \subset  {U}_{i} \) and smooth functions \( {f}_{i} \) such that \( {f}_{i} \) is identically 1 on \( {V}_{i} \) and identically 0 outside \( {U}_{i} \) . Then \( {\left\{  {f}_{i}{s}_{i,1},\ldots ,{f}_{i}{s}_{i, k}\right\}  }_{i \in  I} \) are global sections of \( E \) which span the fiber at every point.

Proposition 23.9. Let \( E \) be a rank \( k \) complex vector bundle over a differentiable manifold \( M \) of finite type. Suppose there are n global sections of \( E \) which span the fiber at every point. Then there is a map \( f \) from \( M \) to some Grassmannian \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) such that \( E \) is the pullback under \( f \) of the universal quotient bundle \( Q \) ; that is, \( E = {f}^{-1}Q \) .

Proof. Let \( {s}_{1},\ldots ,{s}_{n} \) be \( n \) spanning sections of \( E \) and let \( V \) be the complex vector space with basis \( {s}_{1},\ldots ,{s}_{n} \) . Since \( {s}_{1},\ldots ,{s}_{n} \) are spanning sections, for each point \( p \) in \( M \) the evaluation map

\[
{\mathrm{{ev}}}_{p} : V \rightarrow  {E}_{p} \rightarrow  0
\]

is surjective. Hence ker \( {\mathrm{{ev}}}_{p} \) is a codimension \( k \) subspace of \( V \) , and the fiber of the universal quotient bundle \( Q \) at the point ker.ev, of the Grassmannian \( {G}_{k}\left( V\right) \) is \( V/\ker {\mathrm{{ev}}}_{p} = {E}_{p} \) . If the map \( f : M \rightarrow  {G}_{k}\left( V\right) \) is defined by

\[
f : p \mapsto  \ker {\mathrm{{ev}}}_{p},
\]

then the quotient bundle \( Q \) pulls back to \( E \) . We can identify \( V \) with \( {\mathbb{C}}^{n} \) , and \( {G}_{k}\left( V\right) \) with \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) .

This map \( f : M \rightarrow  {G}_{k}\left( {\mathbb{C}}^{n}\right) \) is called a classifying map for the bundle \( E \) .

It can be shown that the homotopy class of the classifying map \( f : M \rightarrow \; {G}_{k}\left( {\mathbb{C}}^{n}\right) \) in the preceding proposition is uniquely determined by the vector bundle \( E \) . This is a consequence of the following lemma, which we do not prove.

Lemma 23.9.1. Given a manifold \( M \) of dimension \( m \) , if \( n \geq  k + \frac{m}{2} \) and \( f \) and \( g : M \rightarrow  {G}_{k}\left( {\mathbb{C}}^{n}\right) \) are two maps such that \( {f}^{-1}Q \simeq  {g}^{-1}Q \) , then \( f \) and \( g \) are homotopic.

A proof of this lemma based on obstruction theory may be found in Steenrod \( \left\lbrack  {1,\text{ § }{19}}\right\rbrack \) and Husemoller \( \left\lbrack  {1,\text{ § }{7.6}}\right\rbrack \) .

Writing \( {\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right) \) for the isomorphism classes of the rank \( k \) complex vector bundles over \( M \) and \( \left\lbrack  {X, Y}\right\rbrack \) for the set of all homotopy classes of maps from \( X \) to \( Y \) , we have the following.

(23.9.2) For \( n \) sufficiently large, there is a well-defined map

\[
\beta  : {\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right)  \rightarrow  \left\lbrack  {M,{G}_{k}\left( {\mathbb{C}}^{n}\right) }\right\rbrack
\]

given by the classifying map of a vector bundle.

Theorem 23.10. Let \( M \) be a manifold having a finite good cover and let \( k \) be a positive integer. For \( n \) sufficiently large, the classifying map of a vector bundle induces a one-to-one correspondence

\[
{\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right)  \simeq  \left\lbrack  {M,{G}_{k}\left( {\mathbb{C}}^{n}\right) }\right\rbrack
\]

between the isomorphism classes of rank \( k \) complex vector bundles over \( M \) and the homotopy classes of maps from \( M \) into the complex Grassmannian \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) .

Proof. By the homotopy property of vector bundles (Theorem 6.8), there is a map

\[
\alpha  : \left\lbrack  {M,{G}_{k}\left( {\mathbb{C}}^{n}\right) }\right\rbrack   \rightarrow  {\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right)
\]

given by the pullback of the universal quotient bundle over \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) :

\[
f \mapsto  {f}^{-1}Q\text{ . }
\]

By (23.9),(23.9.2), and (23.9.3), for \( n \) sufficiently large, the map

\[
\beta  : {\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right)  \rightarrow  \left\lbrack  {M,{G}_{k}\left( {\mathbb{C}}^{n}\right) }\right\rbrack  ,
\]

given by the homotopy class of the classifying map of a vector bundle, is inverse to \( \alpha \) .

As a corollary of the existence of the universal bundle (23.9), we now show that in a precise sense the Chern classes are the only cohomological invariants of a smooth complex vector bundle. We think of \( {\operatorname{Vect}}_{k}\left( {;\mathbb{C}}\right) \) and \( {H}^{ * }\left(  \right) \) as functors from the category of manifolds to the category of sets. A natural transformation \( T \) between these functors is given by a collection of maps \( {T}_{M} \) from \( {\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right) \) to \( {H}^{ * }\left( M\right) \) such that the naturality diagrams commute. The Chern classes \( {c}_{1},\ldots ,{c}_{k} \) are examples of such natural transformations.

Proposition 23.11. Every natural transformation from the isomorphism classes of complex vector bundles over a manifold of finite type to the de Rham cohomology can be given as a polynomial in the Chern classes.

Proof. Let \( T \) be a natural transformation from the functor \( {\operatorname{Vect}}_{k}\left( {;\mathbb{C}}\right) \) to the functor \( {H}^{ * }\left( \right) \) in the category of manifolds of finite type. By Proposition 23.9 and the naturality of \( T \) , if \( E \) is any rank \( k \) complex vector bundle over \( M \) and \( f : M \rightarrow  {G}_{k}\left( {\mathbb{C}}^{n}\right) \) a classifying map for \( E \) , then

\[
T\left( E\right)  = T\left( {{f}^{-1}Q}\right)  = {f}^{ * }T\left( Q\right) .
\]

Because the cohomology of the Grassmannian \( {G}_{k}\left( {\mathbb{C}}^{n}\right) \) is generated by the Chern classes of \( Q \) (Prop. 23.2(b)), \( T\left( Q\right) \) can be written as

\[
T\left( Q\right)  = {P}_{T}\left( {{c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) }\right)
\]

for some polynomial \( {P}_{T} \) depending on \( T \) . Therefore

\[
T\left( E\right)  = {f}^{ * }T\left( Q\right)  = {P}_{T}\left( {{f}^{ * }{c}_{1}\left( Q\right) ,\ldots ,{f}^{ * }{c}_{k}\left( Q\right) }\right)  = {P}_{T}\left( {{c}_{1}\left( E\right) ,\ldots ,{c}_{k}\left( E\right) }\right) .
\]

Recall that we write \( {\operatorname{Vect}}_{k}\left( M\right) \) for the isomorphism classes of rank \( k \) real vector bundles over \( M \) . Of course, there is an analogue of Theorem 23.10 for real vector bundles. A proof applicable to both real and complex bundles may be found in Steenrod [1,§19]. The result for real bundles is as follows.

Theorem 23.12. Let \( M \) be a manifold of dimension \( m \) . Then there is a one-to-one correspondence

\[
\left\lbrack  {M,{G}_{k}\left( {\mathbb{R}}^{k + m}\right) }\right\rbrack   \simeq  {\operatorname{Vect}}_{k}\left( M\right)
\]

which assigns to the homotopy class of a map \( f : M \rightarrow  {G}_{k}\left( {\mathbb{R}}^{k + m}\right) \) the isomorphism class of the pullback \( {f}^{-1}Q \) of the universal quotient bundle \( Q \) over \( {G}_{k}\left( {\mathbb{R}}^{k + m}\right) \) .

We now classify the vector bundles over spheres and relate them to the homotopy groups of the orthogonal and unitary groups.

Exercise 23.13. (a) Use Exercise 17.24 and the homotopy exact sequence of the fibration

\[
\begin{matrix} O\left( k\right)  \rightarrow  O\left( n\right) /O\left( {n - k}\right) \\   \downarrow  \\  {G}_{k}\left( {\mathbb{R}}^{n}\right)  \end{matrix}
\]

to show that

\[
{\pi }_{q}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right)  = {\pi }_{q - 1}\left( {O\left( k\right) }\right) \;\text{ if }n \geq  k + q + 2.
\]

(b) Similarly show that

\[
{\pi }_{q}\left( {{G}_{k}\left( {\mathbb{C}}^{n}\right) }\right)  = {\pi }_{q - 1}\left( {U\left( k\right) }\right) \;\text{ if }n \geq  \left( {{2k} + q + 1}\right) /2.
\]

Combining these formulas with Proposition 17.6.1 concerning the relation of free versus base-point preserving homotopies we find that for \( n \) sufficiently large,

\[
{\operatorname{Vect}}_{k}\left( {S}^{q}\right)  = \left\lbrack  {{S}^{q},{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right\rbrack
\]

\[
= {\pi }_{q}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right) /{\pi }_{1}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right)
\]

\[
= {\pi }_{q - 1}\left( {O\left( k\right) }\right) /{\pi }_{0}\left( {O\left( k\right) }\right) .
\]

Exactly the same computation works for the complex vector bundles over \( {S}^{q} \) . We summarize the results in the following.

Proposition 23.14. The isomorphism classes of the differentiable rank \( k \) real vector bundles over the sphere \( {\mathrm{S}}^{q} \) are given by

\[
{\operatorname{Vect}}_{k}\left( {S}^{q}\right)  \simeq  {\pi }_{q - 1}\left( {O\left( k\right) }\right) /{\mathbb{Z}}_{2}
\]

the isomorphism classes of the complex vector bundles are given by

\[
{\operatorname{Vect}}_{k}\left( {{S}^{q};\mathbb{C}}\right)  \simeq  {\pi }_{q - 1}\left( {U\left( k\right) }\right) .
\]

REMARK 23.14.1 If \( G \) is a Lie group and \( a \in  G \) , then conjugation by \( a \) defines an automorphism \( {h}_{a} \) of \( G \) :

\[
{h}_{a}\left( g\right)  = {ag}{a}^{-1}.
\]

Let \( m \) be any integer. The map \( {h}_{a} \) induces a map of homotopy groups:

\[
{\left( {h}_{a}\right) }_{ * } : {\pi }_{m}\left( G\right)  \rightarrow  {\pi }_{m}\left( G\right) .
\]

If two elements \( a \) and \( b \) in \( G \) can be joined by a path \( \gamma \left( t\right) \) in \( G \) , then \( {h}_{a} \) is homotopic to \( {h}_{b} \) via the homotopy \( {h}_{\gamma \left( t\right) } \) . Consequently \( {\left( {h}_{a}\right) }_{ * } = {\left( {h}_{b}\right) }_{ * } \) . In this way conjugation induces an action of \( {\pi }_{0}\left( G\right) \) on \( {\pi }_{m}\left( G\right) \) , called the adjoint action.

We know from (17.6) that for any space \( X \) with base point \( x \) , conjugation on the loop space \( {\Omega }_{x}X \) induces an action of \( {\pi }_{1}\left( X\right) \) on \( {\pi }_{q}\left( X\right) \) . With a little more classifying space theory, it can be shown that the action of \( {\pi }_{0}\left( {O\left( k\right) }\right) \) on \( {\pi }_{q - 1}\left( {O\left( k\right) }\right) \) corresponding to the action of \( {\pi }_{1}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right) \) on \( {\pi }_{q}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right) \) under the identification of \( {\pi }_{q - 1}\left( {O\left( k\right) }\right) \) with \( {\pi }_{q}\left( {{G}_{k}\left( {\mathbb{R}}^{n}\right) }\right) \) is precisely the adjoint action.

REMARK 23.14.2. It is in fact possible to explain the correspondence (23.14) directly. Let \( E \) be a rank \( k \) vector bundle over \( {S}^{q} \) with structure group \( O\left( k\right) \) , and let \( {U}_{0} \) and \( {U}_{1} \) be small open neighborhoods of the upper and lower hemispheres. Because \( {U}_{0} \) and \( {U}_{1} \) are contractible, \( E \) is trivial over them. Hence \( E \) is completely determined by the transition function

\[
{g}_{01} : {U}_{0} \cap  {U}_{1} \rightarrow  O\left( k\right) .
\]

\( {g}_{01} \) is called a clutching function for \( E \) . Then Proposition 23.14 may be interpreted as a correspondence between the isomorphism classes of vector bundles over a sphere and the free homotopy classes of the clutching functions.

Exercise 23.15. Compute \( {\operatorname{Vect}}_{k}\left( {S}^{1}\right) ,{\operatorname{Vect}}_{k}\left( {S}^{2}\right) \) , and \( {\operatorname{Vect}}_{k}\left( {S}^{3}\right) \) .

EXAMPLE 23.16 (An orientable sphere bundle with zero Euler class but no section). Because \( {S}^{4} \) is simply connected, every vector bundle over \( {S}^{4} \) is orientable (Proposition 11.5). For a line bundle orientability implies triviality. Therefore,

\[
{\operatorname{Vect}}_{1}\left( {S}^{4}\right)  = 0\text{ . }
\]

By (23.14),

\[
{\operatorname{Vect}}_{2}\left( {S}^{4}\right)  = {\pi }_{3}\left( {{SO}\left( 2\right) }\right) /{\mathbb{Z}}_{2} = {\pi }_{3}\left( {S}^{1}\right) /{\mathbb{Z}}_{2} = 0,
\]

\[
{\operatorname{Vect}}_{3}\left( {S}^{4}\right)  = {\pi }_{3}\left( {{SO}\left( 3\right) }\right) /{\mathbb{Z}}_{2} = {\pi }_{3}\left( {\mathbb{R}{P}^{3}}\right) /{\mathbb{Z}}_{2}
\]

\[
= {\pi }_{3}\left( {S}^{3}\right) /{\mathbb{Z}}_{2} = \mathbb{Z}/{\mathbb{Z}}_{2}.
\]

Consequently there is a nontrivial rank 3 vector bundle \( E \) over \( {S}^{4} \) . The Euler class of \( E \) vanishes trivially, since \( e\left( E\right) \) is in \( {H}^{3}\left( {S}^{4}\right)  = 0 \) . If \( E \) has a nonzero global section, it would split into a direct sum \( E = L \oplus  F \) of a line bundle and a rank 2 bundle. Since \( {\operatorname{Vect}}_{1}\left( {S}^{4}\right)  = {\operatorname{Vect}}_{2}\left( {S}^{4}\right)  = 0 \) , this would imply that \( E \) is trivial, a contradiction. Therefore the unit sphere bundle of \( E \) relative to some Riemannian metric is an orientable \( {S}^{2} \) -bundle over \( {S}^{4} \) with zero Euler class but no section. This example shows that the converse of Proposition 11.9 is not true.

REMARK 23.16.1 Actually \( {\operatorname{Vect}}_{3}\left( {S}^{4}\right)  \simeq  \mathbb{Z} \) , because the action of \( {\mathbb{Z}}_{2} \) on \( {\pi }_{3}\left( {{SO}\left( 3\right) }\right) \) is trivial. Indeed, by Remark 23.14.1 this action is induced by the action of \( - 1 \in  O\left( 3\right) \) under conjugation on \( {SO}\left( 3\right) \) . But conjugating by -1 clearly gives the identity map.

In general, by the same reasoning, if \( k \) is odd, then the action of \( {\pi }_{0}\left( {O\left( k\right) }\right) \) on \( {\pi }_{q}\left( {O\left( k\right) }\right) \) is trivial for all \( q \) .

## The Infinite Grassmannian

We will now say a few words about vector bundles over manifolds not having a finite good cover. For Theorem 23.10 to hold here the analogue of the finite Grassmannian is the infinite Grassmannian. Given a sequence of complex vector spaces

\[
\cdots  \subset  {V}_{r} \subset  {V}_{r + 1} \subset  {V}_{r + 2} \subset  \cdots \;{\dim }_{\mathbb{C}}{V}_{i} = i
\]

there is a naturally induced sequence of Grassmannians

\[
\cdots  \subset  {G}_{k}\left( {V}_{r}\right)  \subset  {G}_{k}\left( {V}_{r + 1}\right)  \subset  {G}_{k}\left( {V}_{r + 2}\right)  \subset  \cdots .
\]

The infinite Grassmannian \( {G}_{k}\left( {V}_{\infty }\right) \) is the telescope constructed from this sequence. Over each \( {G}_{k}\left( {V}_{r}\right) \) there are the universal quotient bundles \( {Q}_{r} \) and there are maps

\[
\cdots  \subset  {Q}_{r} \subset  {Q}_{r + 1} \subset  {Q}_{r + 2} \subset  \cdots .
\]

By the telescoping construction again there is a bundle \( Q \) of rank \( k \) over \( {G}_{k}\left( {V}_{\infty }\right) \) . A point of \( {G}_{k}\left( {V}_{\infty }\right) \) is a subspace \( \Lambda \) of codimension \( k \) in \( {V}_{\infty } \) and the fiber of \( Q \) over \( \Lambda \) is the \( k \) -dimensional quotient space \( {V}_{\infty }/\Lambda \) .

Unfortunately the infinite Grassmannian is infinite-dimensional and so is not a manifold in our sense of the word. Since to discuss infinite-dimensional manifolds would take us too far afield, we will merely indicate how our theorems may be extended. By the countable analogue of the Shrinking Lemma (Ex. 21.4), with the finite cover replaced by a countable locally finite cover, one can show just as in Lemma 23.8 that every vector bundle over an arbitrary manifold \( M \) has a collection of countably many spanning sections \( {s}_{1},{s}_{2},\ldots \) . If \( {V}_{\infty } \) is the infinite-dimensional vector space with basis \( {s}_{1},{s}_{2},\ldots \) , there is again a surjective evaluation map at each point \( p \) in \( M \) :

\[
{\mathrm{{ev}}}_{p} : {V}_{\infty } \rightarrow  {E}_{p} \rightarrow  0.
\]

The kernel of \( {\operatorname{ev}}_{p} \) is a codimension \( k \) subspace of \( {V}_{\infty } \) . So the function \( f\left( p\right)  = \ker {\mathrm{{ev}}}_{p} \) sends \( M \) into the infinite Grassmannian \( {G}_{k}\left( {V}_{\infty }\right) \) . This map \( f \) is a classifying map for the vector bundle \( E \) and there is again a one-to-one correspondence

\[
{\operatorname{Vect}}_{k}\left( {M;\mathbb{C}}\right)  \simeq  \left\lbrack  {M,{G}_{k}\left( {\mathbb{C}}^{\infty }\right) }\right\rbrack  .
\]

All this can be proved in the same way as for manifolds of finite type. From Proposition 23.2, it is reasonable to conjecture that the cohomology ring of the infinite Grassmannian \( {G}_{k}\left( {\mathbb{C}}^{\infty }\right) \) is the free polynomial algebra

\[
\mathbb{R}\left\lbrack  {{c}_{1}\left( Q\right) ,\ldots ,{c}_{k}\left( Q\right) }\right\rbrack  .
\]

This is indeed the case. (For a proof see Milnor and Stasheff [1, p. 161] or Husemoller [1, Ch. 18, Th. 3.2, p. 269].) Hence Proposition 23.11 extends to a general manifold.

Exercise 23.17. Let \( V \) be a vector space over \( \mathbb{R} \) and \( {V}^{ * } = \operatorname{Hom}\left( {V,\mathbb{R}}\right) \) its dual.

(a) Show that \( P\left( {V}^{ * }\right) \) may be interpreted as the set of all hyperplanes in \( V \) . (b) Let \( Y \subset  P\left( V\right)  \times  P\left( {V}^{ * }\right) \) be defined by

\[
Y = \left\{  {\left( {\left\lbrack  v\right\rbrack  ,\left\lbrack  H\right\rbrack  }\right)  \mid  H\left( v\right)  = 0, v \in  V, H \in  {V}^{ * }}\right\}  .
\]

In other words, \( Y \) is the incidence correspondence of pairs (line in \( V \) , hyperplane in \( V \) ) such that the line is contained in the hyperplane. Compute \( {H}^{ * }\left( Y\right) \) .

## Concluding Remarks

In the preceding sections the Chern classes of a vector bundle \( E \) over \( M \) were first defined by studying the relations in the cohomology ring \( {H}^{ * }\left( {PE}\right) \) of the projective bundle, where the ring was considered as an algebra over \( {H}^{ * }\left( M\right) \) . This somewhat ad hoc procedure turned out to yield all characteristic classes of \( E \) only after we learned that all bundles of a given rank were pullbacks of a universal bundle and that the cohomology ring of the universal base space (the classifying space) was generated by the Chern classes of the universal bundle.

From a purely topological point of view one could therefore dispense with the original definition, for by designating a set of generators of the cohomology ring of the classifying space as the universal Chern classes, one can define the Chern classes of any vector bundle simply as the pullbacks via the classifying map of the universal Chern classes. On the other hand, from the differential-geometric point of view the projective-bundle definition is more appealing, starting as it does, with \( {c}_{1}\left( {S}^{ * }\right) \) , a class that we understand rather thoroughly and that furnishes us with a canonical generator for \( {H}^{ * }\left( {PE}\right) \) over \( {H}^{ * }\left( M\right) \) . However, this \( {c}_{1} \) is taken on the space \( P\left( E\right) \) rather than on \( M \) and is therefore not directly linked to the geometry of \( M \) . The question arises whether one can write down a form representing \( {c}_{k}\left( E\right) \) in terms of the following data:

(1) a good cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) of \( M \) which trivializes \( E \) ;

(2) the transition functions

\[
{g}_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  {GL}\left( {n,\mathbb{C}}\right)
\]

for \( E \) relative to such a trivialization;

(3) a partition of unity subordinate to the open cover \( \mathfrak{U} \) .

The answer to this question is yes and the reader is referred to Bott [2] for a thoroughgoing discussion. Here we will describe only the final recipe, for to understand it properly, we would have to explore the concepts of connections and curvature, which are beyond the scope of this book.

Observe first that we are already in possession of the desired formula for the first Chern class of a complex line bundle \( L \) (see (6.38)). Indeed, if \( {g}_{\alpha \beta } \) is the transition function for \( L \) , the element

\[
{c}^{1,1} = \frac{i}{2\pi }d\log {g}_{\alpha \beta }
\]

in the Čech-de Rham complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) is both \( d \) - and \( \delta \) -closed. By the collating formula (9.5), once a partition of unity is selected, this cocycle yields a global form. The cohomology class of this global form is \( {c}_{1}\left( L\right) \) .

In the general case one can construct a cocycle \( \mathop{\sum }\limits_{{q = 0}}^{{k - 1}}{c}^{k - q, k + q} \) , with \( {c}^{k - q, k + q} \) in \( {C}^{k - q}\left( {\mathfrak{U},{\Omega }^{k + q}}\right) \) , that represents the \( k \) -th Chern class \( {c}_{k}\left( E\right) \) by the following unfortunately rather formidable "averaging" procedure.

Let \( I = \left( {{i}_{0},\ldots ,{i}_{q}}\right) \) correspond to a nonvacuous intersection, set

\[
{U}_{I} = {U}_{{i}_{0}} \cap  \cdots  \cap  {U}_{{i}_{q}}
\]

and let

\[
{g}_{0j} : {U}_{{i}_{0}} \cap  {U}_{{i}_{j}} \rightarrow  {GL}\left( {n,\mathbb{C}}\right)
\]

be the pertinent transition matrix function for \( E \) . Consider the expression

\[
{\theta }_{I} = \mathop{\sum }\limits_{{j = 0}}^{q}{t}_{j}{g}_{0j}^{-1}d{g}_{0j}
\]

as a matrix of 1-forms on \( {U}_{I} \times  {\mathbb{R}}^{q + 1} \) , the \( t \) ’s being linear coordinates in \( {\mathbb{R}}^{q + 1} \) . From \( \theta \) one can construct the matrix of 2-forms

\[
{K}_{I} = d{\theta }_{I} + \frac{1}{2}{\theta }_{I}^{2}
\]

on \( {U}_{I} \times  {\mathbb{R}}^{q + 1} \) and set

\[
{c}_{I}\left( E\right)  = \det \left( {1 + \frac{i}{2\pi }{K}_{I}}\right) .
\]

Our recipe is now completed by the following ansatz. Let

\[
{\Delta }_{q} = \left\{  {\left( {{t}_{1},\cdots ,{t}_{q + 1}}\right)  \mid  {t}_{j} \geq  0,\sum {t}_{j} = 1}\right\}
\]

be the standard \( q \) -simplex in \( {\mathbb{R}}^{q + 1} \) . The \( {2k} \) -form \( {c}_{I}^{k}\left( E\right) \) restricted to \( {U}_{I} \times  {\Delta }_{q} \) , and integrated over the "fiber \( {\Delta }_{q} \) " yields the desired form on \( {U}_{I} \) :

\[
{c}_{I}^{k - q, k + q}\left( E\right)  = {\int }_{{\Delta }_{q}}{c}_{I}^{k}\left( E\right) .
\]

In other words, \( {c}_{k}\left( E\right) \) is represented by the chain

\[
\mathop{\sum }\limits_{{q = 0}}^{{k - 1}}{c}^{k - q, k + q} \in  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) .
\]

Note that for dimensional reasons this chain has no component below the diagonal and also no component in the zero-th column. This fact has interesting applications in foliation theory (Bott [1]). In any case, the collating procedure (9.5) now completes the construction of the forms \( {c}_{k}\left( E\right) \) in terms of the specified data.
