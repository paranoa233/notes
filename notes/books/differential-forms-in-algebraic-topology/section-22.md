## §22 Pontrjagin Classes

Although the Chern classes are invariants of a complex bundle, they can be used to define invariants of a real vector bundle, called the Pontrjagin classes. In this section we define the Pontrjagin classes, compute a few examples, and as an application obtain an embedding criterion for differentiable manifolds.

## Conjugate Bundles

Let \( V \) be a complex vector space. If \( z \in  \mathbb{C} \) and \( v \in  V \) , the formula

\[
z * v = \bar{z}v
\]

defines an action of \( \mathbb{C} \) on \( V \) . The underlying additive group of \( V \) with this action as scalar multiplication is called the conjugate vector space of \( V \) , denoted \( \bar{V} \) . The conjugate space \( \bar{V} \) may be thought of as \( V \) with the opposite complex structure; as a vector space, \( \bar{V} \) is anti-isomorphic to \( V \) . A linear map \( f : V \rightarrow  W \) of two complex vector spaces \( V \) and \( W \) is also a linear map of the conjugate vector spaces \( f : \bar{V} \rightarrow  \bar{W} \) ; we denote both by \( f \) as they are represented by the same matrix.

Given a complex vector bundle \( E \) with trivialization

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \supset  {U}_{\alpha } \times  {\mathbb{C}}^{n}
\]

we construct the conjugate vector bundle \( \bar{E} \) by replacing each fiber of \( E \) by its conjugate. The trivialization of \( \bar{E} \) is given by

\[
{\left. {\overline{\phi }}_{\alpha } : \bar{E}\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  {\mathbb{C}}^{n}
\]

which is the composition

\[
{\left. \bar{E}\right| }_{{U}_{\alpha }}\overset{{\phi }_{\alpha }}{ \simeq  }{U}_{\alpha } \times  {\overline{\mathbb{C}}}^{n}\xrightarrow[]{\text{ conjugation }}{U}_{\alpha } \times  {\mathbb{C}}^{n}.
\]

In terms of transition functions, if the cocycle \( \left\{  {g}_{\alpha \beta }\right\} \) defines \( E \) , then its conjugate \( \left\{  {\bar{g}}_{\alpha \beta }\right\} \) defines \( \bar{E} \) .

As in (6.4), by endowing a complex vector bundle on a manifold with a Hermitian metric, we can reduce its structure group to the unitary group. Since unitary matrices \( {g}_{\alpha \beta } \) satisfy \( {\widetilde{g}}_{\alpha \beta } = {\left( {g}_{\alpha \beta }^{t}\right) }^{-1} \) , we see that the conjugate bundle \( \bar{E} \) and the dual bundle \( {E}^{ * } \) have the same transition functions and hence are isomorphic. So by Example 21.12, if \( c\left( E\right)  = \prod \left( {1 + {x}_{i}}\right) \) , then \( c\left( \bar{E}\right)  = \prod \left( {1 - {x}_{i}}\right) . \)

## Realization and Complexification

By simply forgetting the complex structure, we can regard a linear map of complex vector spaces \( L : {\mathbb{C}}^{n} \rightarrow  {\mathbb{C}}^{n} \) with coordinates \( {z}_{1},\ldots ,{z}_{n} \) as a linear map of the underlying real vector spaces \( {L}_{\mathbb{R}} : {\mathbb{R}}^{2n} \rightarrow  {\mathbb{R}}^{2n} \) with coordinates \( {x}_{1},\ldots ,{x}_{2n} \) where \( {z}_{k} = {x}_{{2k} - 1} + i{x}_{2k} \) . Conversely, via the natural embedding of \( {\mathbb{R}}^{n} \) in \( {\mathbb{C}}^{n} \) , a linear map of real vector spaces \( L : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) gives rise to a map \( L \otimes  \mathbb{C} : {\mathbb{C}}^{n} \rightarrow  {\mathbb{C}}^{n} \) . The first operation is called realization and the second, complexification. The complexification of a real matrix is the matrix itself, but with the entries viewed as complex numbers. The realization of a complex matrix is described in Examples 22.2 and 22.3 below. In terms of matrices these two operations give a sequence of embeddings

\[
U\left( n\right)  \hookrightarrow  O\left( {2n}\right) \; \hookrightarrow  U\left( {2n}\right)
\]

\[
\cap
\]

(22.1)

\[
{GL}\left( {n,\mathbb{C}}\right)  \hookrightarrow  {GL}\left( {{2n},\mathbb{R}}\right)  \hookrightarrow  {GL}\left( {{2n},\mathbb{C}}\right)
\]

\[
A \mapsto  {A}_{\mathbb{R}} \mapsto  {A}_{\mathbb{R}} \otimes  \mathbb{C}
\]

EXAMPLE 22.2. Let \( L : \mathbb{C} \rightarrow  \mathbb{C} \) be given by multiplication by the complex number \( \lambda  = \alpha  + {i\beta } \) . Since

\[
\left( {\alpha  + {i\beta }}\right) \left( {{x}_{1} + i{x}_{2}}\right)  = \left( {\alpha {x}_{1} - \beta {x}_{2}}\right)  + i\left( {\beta {x}_{1} + \alpha {x}_{2}}\right) ,
\]

as a linear map from \( {\mathbb{R}}^{2} \) to \( {\mathbb{R}}^{2},{L}_{\mathbb{R}} \) is given by

\[
\left( \begin{array}{l} {x}_{1} \\  {x}_{2} \end{array}\right)  \mapsto  \left( \begin{array}{rr} \alpha &  - \beta \\  \beta & \alpha  \end{array}\right) \left( \begin{array}{l} {x}_{1} \\  {x}_{2} \end{array}\right) .
\]

Thus

\[
{\left( \alpha  + i\beta \right) }_{\mathbb{R}} = \left( \begin{array}{rr} \alpha &  - \beta \\  \beta & \alpha  \end{array}\right) .
\]

EXAMPLE 22.3 Let \( L : {\mathbb{C}}^{2} \rightarrow  {\mathbb{C}}^{2} \) be given by the complex matrix \( \left( \begin{array}{ll} {\lambda }_{1} & {\lambda }_{2} \\  {\lambda }_{3} & {\lambda }_{4} \end{array}\right) \) where \( {\lambda }_{k} = {\alpha }_{k} + i{\beta }_{k} \) . A little computation shows that \( {L}_{\mathbb{R}} : {\mathbb{R}}^{4} \rightarrow  {\mathbb{R}}^{4} \) is given by

\[
\left( \begin{array}{l} {x}_{1} \\  {x}_{2} \\  {x}_{3} \\  {x}_{4} \end{array}\right)  \mapsto  \left( \begin{array}{rrrr} {\alpha }_{1} &  - {\beta }_{1} & {\alpha }_{2} &  - {\beta }_{2} \\  {\beta }_{1} & {\alpha }_{1} & {\beta }_{2} & {\alpha }_{2} \\  {\alpha }_{3} &  - {\beta }_{3} & {\alpha }_{4} &  - {\beta }_{4} \\  {\beta }_{3} & {\alpha }_{3} & {\beta }_{4} & {\alpha }_{4} \end{array}\right) \left( \begin{array}{l} {x}_{1} \\  {x}_{2} \\  {x}_{3} \\  {x}_{4} \end{array}\right) .
\]

Thus

\[
{\left( \begin{array}{ll} {\lambda }_{1} & {\lambda }_{2} \\  {\lambda }_{3} & {\lambda }_{4} \end{array}\right) }_{\mathbb{R}} = \left( \begin{array}{ll} {\left( {\lambda }_{1}\right) }_{\mathbb{R}} & {\left( {\lambda }_{2}\right) }_{\mathbb{R}} \\  {\left( {\lambda }_{3}\right) }_{\mathbb{R}} & {\left( {\lambda }_{4}\right) }_{\mathbb{R}} \end{array}\right)
\]

It is clear from these two examples what the realization of an \( n \) by \( n \) complex matrix should be.

Lemma 22.4. Let \( A \) be an \( n \) by \( n \) complex matrix. There is a \( {2n} \) by \( {2n} \) matrix \( B \) , independent of \( A \) , such that \( {A}_{\mathbb{R}} \otimes  \mathbb{C} \) is similar to \( \left( \begin{matrix} A & 0 \\  0 & \bar{A} \end{matrix}\right) \) via \( B \) .

Proof. In the 1 by 1 case, this is a matter of diagonalizing

\[
{\left( \alpha  + i\beta \right) }_{\mathbb{R}} \otimes  \mathbb{C} = \left( \begin{array}{rr} \alpha &  - \beta \\  \beta & \alpha  \end{array}\right) .
\]

Corresponding to the eigenvalues \( \alpha  + {i\beta } \) and \( \alpha  - {i\beta } \) are the eigenvectors \( \left( { - }_{i}^{1}\right) \) and \( \left( {}_{i}^{1}\right) \) . Therefore, \( B = \left( \begin{array}{ll} 1 & 1 \\   - i & i \end{array}\right) \) .

Now consider the 2 by 2 case:

\[
A = \left( \begin{array}{ll} {\lambda }_{1} & {\lambda }_{2} \\  {\lambda }_{3} & {\lambda }_{4} \end{array}\right) ,\;{\lambda }_{k} = {\alpha }_{k} + i{\beta }_{k}
\]

\[
{A}_{\mathbb{R}} \otimes  \mathbb{C} = \left( \begin{array}{ll} {A}_{1} & {A}_{2} \\  {A}_{3} & {A}_{4} \end{array}\right) \text{ where }{A}_{k} = \left( \begin{array}{rr} {\alpha }_{k} &  - {\beta }_{k} \\  {\beta }_{k} & {\alpha }_{k} \end{array}\right) .
\]

Note that

\[
\left( \begin{array}{ll} {A}_{1} & {A}_{2} \\  {A}_{3} & {A}_{4} \end{array}\right) \left( \begin{matrix} 1 \\   - i \\  0 \\  0 \end{matrix}\right)  = \left( \begin{matrix} {\lambda }_{1} \\   - i{\lambda }_{1} \\  {\lambda }_{3} \\   - i{\lambda }_{3} \end{matrix}\right)  = \left( \begin{matrix} 1 & 0 &  * &  * \\   - i & 0 &  * &  * \\  0 & 1 &  * &  * \\  0 &  - i &  * &  *  \end{matrix}\right) \left( \begin{matrix} {\lambda }_{1} \\  {\lambda }_{3} \\  0 \\  0 \end{matrix}\right)
\]

\[
\left( \begin{array}{ll} {A}_{1} & {A}_{2} \\  {A}_{3} & {A}_{4} \end{array}\right) \left( \begin{matrix} 1 & 0 & 1 & 0 \\   - i & 0 & i & 0 \\  0 & 1 & 0 & 1 \\  0 &  - i & 0 & i \end{matrix}\right)  = \left( \begin{matrix} 1 & 0 & 1 & 0 \\   - i & 0 & i & 0 \\  0 & 1 & 0 & 1 \\  0 &  - i & 0 & i \end{matrix}\right) \left( \begin{array}{llll} {\lambda }_{1} & {\lambda }_{2} & & \\  {\lambda }_{3} & {\lambda }_{4} & & \\   & & {\overline{\lambda }}_{1} & {\overline{\lambda }}_{2} \\   & & {\overline{\lambda }}_{3} & {\overline{\lambda }}_{4} \end{array}\right) .
\]

So

\[
B = \left( \begin{array}{rrrr} 1 & 0 & 1 & 0 \\   - i & 0 & i & 0 \\  0 & 1 & 0 & 1 \\  0 &  - i & 0 & i \end{array}\right)
\]

For the \( n \) by \( n \) case, we can take \( B \) to be

\[
\left( \begin{matrix} 1 & & & & & & & & \\   - i & & & & & & & & \\   & 1 & & & & & & & \\   & & 1 & & & & & 1 & \\   & &  - i & & & & & i & \\   & & & 1 & & & & & 1 \\   & &  - i & & & & & i & \\   & & & &  - i & & & & i \end{matrix}\right)
\]

If \( E \) is a complex vector bundle of rank \( n \) with transition functions \( \left\{  {g}_{\alpha \beta }\right\} \) , then \( {E}_{\mathbb{R}} \otimes  \mathbb{C} \) is the complex vector bundle of rank \( {2n} \) with transition functions \( \left\{  {{\left( {g}_{\alpha \beta }\right) }_{\mathbb{R}} \otimes  \mathbb{C}}\right\} \) . By Lemma 22.4,

(22.5)

\[
{E}_{\mathbb{R}} \otimes  \mathbb{C} \simeq  E \oplus  \bar{E}
\]

This result may be seen alternatively as follows. On the complex vector space \( {E}_{\mathbb{R}} \otimes  \mathbb{C} \) , multiplication by \( i \) is a linear transformation \( J \) satisfying \( {J}^{2} =  - 1 \) . Therefore, the eigenvalues of \( J \) are \( \pm  i \) and \( {E}_{\mathbb{R}} \otimes  \mathbb{C} \) accordingly decomposes into a direct sum

\[
{E}_{\mathbb{R}} \otimes  \mathbb{C} = \left( {i\text{ -eigenspace }}\right)  \oplus  (\left( {-i}\right) \text{ -eigenspace). }
\]

On the \( i \) -eigenspace, \( J \) acts as multiplication by \( i \) , hence

\[
\text{ (i-eigenspace) } \supset  E\text{ . }
\]

Similarly,

\[
\left( {\left( {-i}\right) \text{ -eigenspace }}\right)  \supset  \bar{E}\text{ . }
\]

It follows by reasons of dimension that

\[
{E}_{\mathbb{R}} \otimes  \mathbb{C} = E \oplus  \bar{E}.
\]

The Pontrjagin Classes of a Real Vector Bundle

By their naturality property the Chern classes of a \( {C}^{\infty } \) complex vector bundle are \( {C}^{\infty } \) invariants of the bundle. For a real vector bundle \( E \) similar invariants may be obtained by considering the Chern classes of its complexification \( E{ \otimes  }_{\mathbb{R}}\mathbb{C} \) ; these are the Pontrjagin classes of \( E \) . More precisely, if \( E \) is a rank \( n \) real vector bundle over \( M \) , then its total Pontrjagin class is

\[
p\left( E\right)  = 1 + {p}_{1}\left( E\right)  + \cdots  + {p}_{n}\left( E\right)
\]

\[
= 1 + {c}_{1}\left( {E \otimes  \mathbb{C}}\right)  + \cdots  + {c}_{n}\left( {E \otimes  \mathbb{C}}\right)  \in  {H}^{ * }\left( M\right) .
\]

It follows from the corresponding properties of the total Chern class that the Pontrjagin class is functorial and satisfies the Whitney product formula

\[
p\left( {E \oplus  {E}^{\prime }}\right)  = p\left( E\right) p\left( {E}^{\prime }\right) .
\]

The Pontrjagin class of a manifold is defined to be that of its tangent bundle.

Remark 22.6. Let \( E \) be a real vector bundle. Because the transition functions of \( E \otimes  \mathbb{C} \) are the same as those of \( E \) , they are real-valued, and therefore \( E \otimes  \mathbb{C} \) is isomorphic to its conjugate \( \overline{E \otimes  \mathbb{C}} \) . It follows that \( {c}_{i}\left( {E \otimes  \mathbb{C}}\right)  = {c}_{i}\overline{\left( E \otimes  \mathbb{C}\right) } = {\left( -1\right) }^{i}{c}_{i}\left( {E \otimes  \mathbb{C}}\right) \) . For an odd \( i \) , then, \( 2{c}_{i}\left( {E \otimes  \mathbb{C}}\right)  = 0 \) . Thus the odd Pontrjagin classes, as we have defined them, are zero in the de Rham cohomology, and torsion of order 2 in the integral cohomology. The usual definition of the Pontrjagin classes in the literature (see, for instance, Milnor and Stasheff [1, p. 174]) ignores these odd Chern classes and defines \( {p}_{i}\left( E\right) \) to be

\[
{\left( -1\right) }^{i}{c}_{2i}\left( {E \otimes  \mathbb{C}}\right) \text{ . }
\]

EXAMPLE 22.7. (The Pontrjagin class of the sphere). Since the sphere \( {S}^{n} \) is orientable, its normal bundle \( N \) in \( {\mathbb{R}}^{n + 1} \) is trivial. From the exact sequence

\[
{\left. 0 \rightarrow  {T}_{{S}^{n}} \rightarrow  {T}_{{\mathbb{R}}^{n + 1}}\right| }_{{S}^{n}} \rightarrow  N \rightarrow  0,
\]

we see by the Whitney product formula that

\[
p\left( {S}^{n}\right) p\left( N\right)  = p\left( {\left. {T}_{{\mathbb{R}}^{n + 1}}\right| }_{{S}^{n}}\right) .
\]

Therefore,

\[
p\left( {S}^{n}\right)  = 1
\]

EXAMPLE 22.8 (The Pontrjagin class of a complex manifold). The Pontrjagin class of a complex manifold \( M \) is defined to be that of the underlying real manifold \( {M}_{\mathbb{R}} \) . Let \( T \) be the holomorphic tangent bundle to \( M \) . Then the tangent bundle to \( {M}_{\mathbb{R}} \) is the realization of \( T \) and

\[
p\left( M\right)  = p\left( {T}_{\mathbb{R}}\right)  = c\left( {{T}_{\mathbb{R}} \otimes  \mathbb{C}}\right)  = c\left( {T \oplus  \bar{T}}\right)  = c\left( T\right) c\left( \bar{T}\right) .
\]

So if the total Chern class of the complex manifold \( M \) is \( c\left( M\right)  = \prod \left( {1 + {x}_{i}}\right) \) , then the Pontrjagin class is \( p\left( M\right)  = \prod \left( {1 - {x}_{i}^{2}}\right) \) .

REMARK 22.8.1. If we had followed the usual sign convention for the Pontrjagin classes (see Remark 22.6), the Pontrjagin class of a complex manifold would be \( p\left( M\right)  = \prod \left( {1 + {x}_{i}^{2}}\right) \) , where the \( {x}_{i} \) ’s are defined as above. To have only positive terms in this formula is one of the reasons for the sign in \( {\left( -1\right) }^{i}{c}_{2i}\left( {E \otimes  \mathbb{C}}\right) \) in the usual definition of the Pontrjagin class.

REMARK 22.9. Let \( M \) be a compact oriented manifold of dimension \( {4n} \) . By Poincaré duality the wedge product \( \land   : {H}^{2n}\left( M\right)  \otimes  {H}^{2n}\left( M\right)  \rightarrow  \mathbb{R} \) is a nondegenerate symmetric bilinear form and hence has a signature; this is called the signature of \( M \) . Recall that the signature of a symmetric matrix is the number of positive eigenvalues minus the number of negative eigenvalues. Hirzebruch proved that the signature is expressible in terms of the Pontrjagin classes.

Hirzebruch signature formula :

\[
\text{ signature of }M = {\left( -1\right) }^{n}{\int }_{M}L\left( {{p}_{1}\left( M\right) ,\ldots ,{p}_{n}\left( M\right) }\right) \text{ , }
\]

where \( L \) is the polynomial defined in Example 21.11. For a proof of the signature formula, see Milnor and Stasheff [1, p. 224].

## Application to the Embedding of a Manifold in a Euclidean Space

Using the Pontrjagin class one can sometimes decide if a conjectured embedding is possible. We illustrate this with the following example. EXAMPLE 22.10. Decide if \( \mathbb{C}{P}^{4} \) can be differentiably embedded in \( {\mathbb{R}}^{9} \) .

By (22.8) and (21.13) the Pontrjagin class of \( \mathbb{C}{P}^{4} \) is

\[
p\left( {\mathbb{C}{P}^{4}}\right)  = c\left( {T}_{\mathbb{C}{P}^{4}}\right) c\left( {\bar{T}}_{\mathbb{C}{P}^{4}}\right)  = {\left( 1 + x\right) }^{5}{\left( 1 - x\right) }^{5} = {\left( 1 - {x}^{2}\right) }^{5}.
\]

If \( \mathbb{C}{P}^{4} \) can be differentiably embedded in \( {\mathbb{R}}^{9} \) , then there is an exact sequence

\[
{\left. {\left. 0 \rightarrow  {\left( {T}_{\mathbb{C}{P}^{4}}\right) }_{\mathbb{R}} \rightarrow  {T}_{{\mathbb{R}}^{9}}\right| }_{\mathbb{C}{P}^{4}} \rightarrow  N \rightarrow  0,\right| }_{\infty }
\]

where \( {\left( {T}_{\mathbb{C}{P}^{4}}\right) }_{\mathbb{R}} \) is the realization of the holomorphic tangent bundle \( {T}_{\mathbb{C}{P}^{4}} \) and \( N \) is the normal bundle of \( \mathbb{C}{P}^{4} \) in \( {\mathbb{R}}^{9} \) . By the Whitney product formula

(22.11)

\[
p\left( {\left. {T}_{{\mathbb{R}}^{9}}\right| }_{\mathbb{C}{P}^{4}}\right)  = p\left( {\left( {T}_{\mathbb{C}{P}^{4}}\right) }_{\mathbb{R}}\right) p\left( N\right) .
\]

Since the restriction \( {\left. {T}_{{\mathbb{R}}^{9}}\right| }_{{\mathbb{{CP}}}^{4}} \) is the pullback of \( {T}_{{\mathbb{R}}^{9}} \) to \( \mathbb{C}{P}^{4} \) under the embedding \( i : \mathbb{C}{P}^{4} \rightarrow  {\mathbb{R}}^{9} \) , by the functoriality of the Pontrjagin class

\[
p\left( {\left. {T}_{{\mathbb{R}}^{9}}\right| }_{\mathbb{C}{P}^{4}}\right)  = {i}^{ * }p\left( {T}_{{\mathbb{R}}^{9}}\right)  = 1.
\]

Therefore, by (22.11)

(22.12)

\[
p\left( N\right)  = \frac{1}{p\left( {\left( {T}_{\mathbb{C}{P}^{4}}\right) }_{\mathbb{R}}\right) } = \frac{1}{{\left( 1 - {x}^{2}\right) }^{5}} = 1 + 5{x}^{2} + {15}{x}^{4}.
\]

Since \( N \) is a real line bundle, the top component of \( p\left( N\right) \) should be in \( {H}^{2}\left( {\mathbb{C}{P}^{4}}\right) \) . This contradicts the fact that \( 5{x}^{2} \) and \( {15}{x}^{4} \) are nonzero classes in \( {H}^{4}\left( {\mathbb{C}{P}^{4}}\right) \) and \( {H}^{8}\left( {\mathbb{C}{P}^{4}}\right) \) . Thus \( \mathbb{C}{P}^{4} \) cannot be embedded in \( {\mathbb{R}}^{9} \) .

From (22.12), if \( \mathbb{C}{P}^{4} \) can be embedded in \( {\mathbb{R}}^{n} \) , then the normal bundle has rank at least 4, since the top-degree term of the Pontrjagin class of a rank \( k \) real bundle is in dimension \( {2k} \) . It follows that \( \mathbb{C}{P}^{4} \) cannot be embedded in a Euclidean space of dimension 11 or less.
