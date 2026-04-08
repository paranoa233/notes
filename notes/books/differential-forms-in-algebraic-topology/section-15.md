## §15 Cohomology with Integer Coefficients

An element in a \( \mathbb{Z} \) -module is said to be torsion if some integral multiple of it is zero. Since the de Rham theory is a cohomology theory with real coefficients, it necessarily overlooks the torsion phenomena. For applications to homotopy theory, however, it is essential to investigate the torsion. The goal of this section is to replace the differential form functor \( {\Omega }^{ * } \) with the singular cochain functor \( {S}^{ * } \) , define the singular cohomology, and show that the preceding results on spectral sequences carry over to integer coefficients. The key as before is the Mayer-Vietoris sequence for countably many open sets. The natural setting for the singular theory is the category of topological spaces and continuous maps, rather than the more restrictive category of differentiable manifolds and \( {C}^{\infty } \) maps of de Rham theory. Unless otherwise indicated, from here till the end of Section 18 we will work in the continuous category. We begin with a review of the basic definitions of singular homology.

## Singular Homology

Via the map

\[
\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  \left( {{x}_{1},\ldots ,{x}_{n},0}\right)
\]

each Euclidean space \( {\mathbb{R}}^{n} \) is naturally included in \( {\mathbb{R}}^{n + 1} \) . Viewing each \( {\mathbb{R}}^{n} \) as a subspace of \( {\mathbb{R}}^{n + 1} \) in this way we consider the union

\[
{\mathbb{R}}^{\infty } = \mathop{\bigcup }\limits_{{n \geq  0}}{\mathbb{R}}^{n}
\]

Denote by \( {P}_{i} \) the \( i \) -th standard basis vector in \( {\mathbb{R}}^{\infty } \) ; it is the vector whose \( i \) -th component is 1 and whose other components are all 0 . Let \( {P}_{0} \) be the origin. We define the standard \( q \) -simplex \( {\Delta }_{q} \) to be the set

\[
{\Delta }_{q} = \left\{  {\mathop{\sum }\limits_{{j = 0}}^{q}{t}_{j}{P}_{j}\left| {\;\mathop{\sum }\limits_{{j = 0}}^{q}{t}_{j} = 1}\right. ,{t}_{j} \geq  0}\right\}  .
\]

If \( X \) is a topological space, a singular \( q \) -simplex in \( X \) is a continuous map \( s : {\Delta }_{q} \rightarrow  X \) and a singular \( q \) -chain in \( X \) is a finite linear combination with integer coefficients of singular \( q \) -simplices. Collectively these \( q \) -chains form an Abelian group \( {S}_{q}\left( X\right) \) . We define the \( i \) -th face map of the standard \( q \) - simplex to be the function

\[
{\partial }_{q}^{i} : {\Delta }_{q - 1} \rightarrow  {\Delta }_{q}
\]

given by (see Figure 15.1)

\[
{\partial }_{q}^{i}\left( {\mathop{\sum }\limits_{{j = 0}}^{{q - 1}}{t}_{j}{P}_{j}}\right)  = \mathop{\sum }\limits_{{j = 0}}^{{i - 1}}{t}_{j}{P}_{j} + \mathop{\sum }\limits_{{j = i + 1}}^{q}{t}_{j - 1}{P}_{j}.
\]

![bo_d7b6f8alb0pc73dd9avg_193_592_1681_454_449_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_193_592_1681_454_449_0.jpg)

Figure 15.1

The graded group of singular chains,

\[
{S}_{ * }\left( X\right)  = {\bigoplus }_{q \geq  0}{S}_{q}\left( X\right)
\]

can be made into a differential complex with boundary operator

\[
\partial  : {S}_{q}\left( X\right)  \rightarrow  {S}_{q - 1}\left( X\right)
\]

\[
\partial s = \mathop{\sum }\limits_{{i = 0}}^{q}{\left( -1\right) }^{i}s \circ  {\partial }_{q}^{i}.
\]

It is easily checked that \( {\partial }^{2} = 0 \) . The homology of this complex is the singular homology with integer coefficients of \( X \) , denoted \( {H}_{ * }\left( X\right) \) or \( {H}_{ * }\left( {X;\mathbb{Z}}\right) \) . By taking the linear combination of simplices to be with coefficients in an Abelian group \( G \) , we obtain similarly singular homology with coefficients in \( G,{H}_{ * }\left( {X;G}\right) \) .

The degree of a 0-chain \( \sum {n}_{i}{P}_{i} \) is by definition \( \sum {n}_{i} \) . Suppose \( X \) is path connected. If \( - P \) and \( Q \) are in a 0-chain on \( X \) , then any path from \( P \) to \( Q \) is a 1-simplex with boundary \( Q - P \) . Hence a 0-chain on a path-connected space is the boundary of a 1-chain if and only if it has degree 0 . This gives rise to a short exact sequence

\[
0 \rightarrow  \partial {S}_{1}\left( X\right)  \rightarrow  {S}_{0}\left( X\right) \overset{\text{ deg }}{ \rightarrow  }\mathbb{Z} \rightarrow  0
\]

from which it follows that if \( X \) is path connected, \( {H}_{0}\left( X\right)  = \mathbb{Z} \) . In general,

rank \( {H}_{0}\left( X\right)  = \) the number of path components of \( X \) .

## The Cone Construction

The goal of this section is to compute the singular homology of \( {\mathbb{R}}^{n} \) . If \( s \) in \( {S}_{q}\left( {\mathbb{R}}^{n}\right) \) is a \( q \) -simplex in \( {\mathbb{R}}^{n} \) , we define the cone over \( s \) to be the \( \left( {q + 1}\right) \) - simplex \( {Ks} \) in \( {S}_{q + 1}\left( {\mathbb{R}}^{n}\right) \) given by

\[
{Ks}\left( {\mathop{\sum }\limits_{{j = 0}}^{{q + 1}}{t}_{j}{P}_{j}}\right)  = \left( {1 - {t}_{q + 1}}\right) s\left( {\mathop{\sum }\limits_{{j = 0}}^{q}\frac{{t}_{j}}{1 - {t}_{q + 1}}{P}_{j}}\right) .
\]

This is the cone in \( {\mathbb{R}}^{n} \) with vertex the origin and base the simplex \( s \) . To make sense of the formula, we view the last coordinate \( {t}_{q + 1} \) as "time"; as time goes from 0 to 1, the cone \( {Ks} \) moves from \( s \) to the origin. For the singular simplex \( s \) pictured in Figure 15.2, the cone \( {Ks} \) is the "tetrahedron" and

\[
\partial {Ks} = 0\text{ th face - 1st face + 2nd face - }s
\]

\[
K\partial s = 0\text{ th face - 1st face + 2nd face. }
\]

![bo_d7b6f8alb0pc73dd9avg_195_472_297_677_581_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_195_472_297_677_581_0.jpg)

Figure 15.2

In general we have the following.

Proposition 15.1. Let \( K : {S}_{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow  {S}_{* + 1}\left( {\mathbb{R}}^{n}\right) \) be the cone construction. Then

\[
\partial K - K\partial  = {\left( -1\right) }^{q + 1}
\]

on \( {S}_{q}\left( {\mathbb{R}}^{n}\right) \) for \( q \geq  1 \) .

Proof. The geometrical idea is clear from Figure 15.2. The proof itself is a routine matter of unravelling the definitions. We leave it to the reader.

In other words, the cone construction \( K \) is a homotopy operator between the identity map and the zero map on \( {S}_{q}\left( {\mathbb{R}}^{n}\right) , q \geq  1 \) . Consequently,

\[
{H}_{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} 0 & q \geq  1 \\  \mathbb{Z} & q = 0. \end{array}\right.
\]

The Mayer-Vietoris Sequence for Singular Chains

Let \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  J} \) be an open cover of the topological space \( X \) . Just as for differential forms on a manifold, the sequence of inclusions

\[
X \leftarrow  \mathop{\coprod }\limits_{{\alpha }_{0}}{U}_{{\alpha }_{0}} \leftleftarrows  \mathop{\coprod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{U}_{{\alpha }_{0}{\alpha }_{1}} \leftleftarrows  \cdots
\]

induces a Mayer-Vietoris sequence. However, for technical reasons which will become apparent in the proof of Proposition 15.2 (to show the surjectivity at one end of the Mayer-Vietoris sequence), we must consider here the group \( {S}_{ * }^{\mathfrak{u}}\left( X\right) \) of \( \mathfrak{U} \) -small chains in \( X \) ; these are chains made up of simplices each of which lies in some open set of the cover \( \mathfrak{U} \) . The inclusion

\[
i : {S}_{ * }^{\mathfrak{u}}\left( X\right)  \rightarrow  {S}_{ * }\left( X\right)
\]

is clearly a chain map, i.e., it commutes with the boundary operator \( \partial \) . Indeed, it is a chain equivalence. The proof of this fact is tedious and we will omit it (Vick [1, Appendix I, p. 207]), but the idea behind it is quite intuitive: to get an inverse chain map, subdivide each chain in \( X \) until it becomes \( \mathfrak{U} \) -small. In any case the upshot is that to compute the singular homology of \( X \) it suffices to use \( \mathfrak{U} \) -small chains: \( H\left( {{S}_{ * }\left( X\right) }\right)  = H\left( {{S}_{ * }^{\mathfrak{U}}\left( X\right) }\right) \) .

Define the Čech boundary operator

\[
\delta  : {\bigoplus }_{{\alpha }_{0} < \cdots  < {\alpha }_{p}}{S}_{q}\left( {U}_{{\alpha }_{0}\cdots {\alpha }_{p}}\right)  \rightarrow  {\bigoplus }_{{\alpha }_{0} < \cdots  < {\alpha }_{p - 1}}{S}_{q}\left( {U}_{{\alpha }_{0}\cdots {\alpha }_{p - 1}}\right)
\]

by the "alternating sum formula"

\[
{\left( \delta c\right) }_{{\alpha }_{0}\cdots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{c}_{\alpha {\alpha }_{0}\cdots {\alpha }_{p - 1}}
\]

Here, as always, we adopt the convention that interchanging two indices in \( {c}_{{\alpha }_{0}\cdots {\alpha }_{n}} \) introduces a minus sign. The fact that \( {\delta }^{2} = 0 \) is proved as in Proposition 12.12. The boundary operator \( \delta \) on \( \oplus  {S}_{q}\left( {U}_{{\alpha }_{0}}\right)  \rightarrow  {S}_{q}\left( X\right) \) is simply the sum; we denote this by \( \varepsilon \) .

Proposition 15.2 (The Mayer-Vietoris Sequence for Singular Chains). The following sequence is exact

\[
0 \leftarrow  {S}_{q}^{\mathrm{u}}\left( X\right) \overset{\varepsilon }{ \leftarrow  }{\bigoplus }_{{\alpha }_{0}}{S}_{q}\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \leftarrow  }{\bigoplus }_{{\alpha }_{0} < {\alpha }_{1}}{S}_{q}\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \leftarrow  }\cdots .
\]

Although this sequence bears a formal resemblance to the generalized Mayer-Vietoris sequence for compact supports (Proposition 12.12), because we do not have partitions of unity at our disposal now, the second half of the proof of (12.12) does not apply.

Lemma 15.3. Let

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0
\]

be a short exact sequence of differential complexes. If two out of the three complexes have zero homology, so does the third.

Proof. Consider the long exact sequence in homology

\[
\cdots  \rightarrow  {H}_{q}\left( A\right)  \rightarrow  {H}_{q}\left( B\right)  \rightarrow  {H}_{q}\left( C\right)  \rightarrow  {H}_{q - 1}\left( A\right)  \rightarrow  \cdots .
\]

Proof of proposition 15.2. For two open sets the Mayer-Vietoris sequence is

\[
0 \leftarrow  {S}_{q}^{\mathrm{u}}\left( {{U}_{0} \cup  {U}_{1}}\right) \overset{\text{ sum }}{ \leftarrow  }{S}_{q}\left( {U}_{0}\right)  \oplus  {S}_{q}\left( {U}_{1}\right)  \leftarrow  {S}_{q}\left( {U}_{01}\right)  \leftarrow  0
\]

\[
\left( {{c}_{10},{c}_{01}}\right)  \leftrightarrow  {c}_{01}
\]

The exactness of this sequence follows directly from the definition. For three open sets the sequence is

\[
0 \leftarrow  {S}_{q}^{\mathrm{u}}\left( {{U}_{0} \cup  {U}_{1} \cup  {U}_{2}}\right)  \leftarrow  {S}_{q}\left( {U}_{0}\right)  \oplus  {S}_{q}\left( {U}_{1}\right)  \oplus  {S}_{q}\left( {U}_{2}\right)  \leftarrow   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
\]

\[
\left( {{c}_{10} + {c}_{20},{c}_{01} + {c}_{21},{c}_{02} + {c}_{12}}\right)  \leftarrow  \left( {{c}_{01},{c}_{02},{c}_{12}}\right)
\]

\[
\left( {{c}_{201},{c}_{102},{c}_{012}}\right)  \leftarrow  1\left( {c}_{012}\right)
\]

The Mayer-Vietoris sequence for two open sets injects into the one for three open sets, giving rise to the following commutative diagram with exact columns

![bo_d7b6f8alb0pc73dd9avg_197_280_798_1072_359_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_197_280_798_1072_359_0.jpg)

The \( \mathfrak{U} \) in \( {S}^{\mathfrak{U}}\left( {{U}_{0} \cup  {U}_{1}}\right) \) is the open cover \( \left\{  {{U}_{0},{U}_{1}}\right\} \) , while the \( \mathfrak{U} \) in \( {S}^{\mathfrak{U}}\left( {{U}_{0} \cup  }\right. \; {U}_{1} \cup  {U}_{2} \) ) is the open cover \( \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) . So the group

\[
{S}^{\mathfrak{u}}\left( {{U}_{0} \cup  {U}_{1} \cup  {U}_{2}}\right) /{S}^{\mathfrak{u}}\left( {{U}_{0} \cup  {U}_{1}}\right)
\]

is generated by the simplices in \( {U}_{2} \) which do not lie entirely in \( {U}_{0} \) or \( {U}_{1} \) (see Figure 15.3).

![bo_d7b6f8alb0pc73dd9avg_197_430_1570_772_516_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_197_430_1570_772_516_0.jpg)

Figure 15.3

We now prove the exactness of the rows of the commutative diagram. The bottom row is almost the Mayer-Vietoris sequence for the open cover \( \left\{  {{U}_{02},{U}_{12}}\right\} \) ; it is exact except possibly at \( S\left( {U}_{2}\right) \) . Clearly \( \beta  \circ  \delta  = 0 \) . Now if \( c \) is in \( S\left( {U}_{2}\right) \) and \( \beta \left( c\right)  = 0 \) , then \( c \) is a chain in \( {U}_{2} \) whose simplices lie either in \( {U}_{0} \) or in \( {U}_{1} \) , i.e., \( c \) is in the image of \( S\left( {U}_{02}\right)  \oplus  S\left( {U}_{12}\right) \) . Therefore the bottom row is exact. Note that each row of the commutative diagram is a differential complex and the commutative diagram may be regarded as a short exact sequence of differential complexes. Since the top and bottom complexes have zero homology, by Lemma 15.3 so does the middle one; in other words, the middle row is exact. This proves the exactness of the Mayer-Vietoris sequence for a cover consisting of three open sets. In general the Mayer-Vietoris sequence for \( r \) open sets injects into the one for \( r + 1 \) open sets. By the above technique and induction, one proves the Mayer-Vietoris sequence for any finite cover.

Now consider a countable cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) . By the definition of the direct sum, an element \( c \) of \( \oplus  S\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) has only finitely many nonzero components. These components can involve only finitely many open sets. Therefore if \( {\delta c} = 0 \) , by the Mayer-Vietoris sequence for a finite cover, we know that \( c = {\delta b} \) for some \( b \) in \( \oplus  S\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}\right) \) . This proves the exactness of the Mayer-Vietoris sequence for countably many open sets.

REMARK 15.4. If the coefficients are in an arbitrary Abelian group \( G \) , the same proof holds word for word.

Now suppose the open cover \( \mathfrak{U} \) consists of two open sets \( U \) and \( V \) . By Proposition 15.2, there is a short exact sequence of singular chains

(15.5)

\[
0 \rightarrow  {S}_{q}\left( {U \cap  V}\right)  \rightarrow  {S}_{q}\left( U\right)  \oplus  {S}_{q}\left( V\right)  \rightarrow  {S}_{q}^{\mathfrak{U}}\left( X\right)  \rightarrow  0.
\]

The associated long exact sequence in homology is the usual homology Mayer-Vietoris sequence.

Corollary 15.6 (The Homology Mayer-Vietoris Sequence for Two Open Sets). Let \( X = U \cup  V \) be the union of two open sets. Then there is a long exact sequence in homology

\[
\cdots  \rightarrow  {H}_{q}\left( {U \cap  V}\right) \overset{f}{ \rightarrow  }{H}_{q}\left( U\right)  \oplus  {H}_{q}\left( V\right) \overset{g}{ \rightarrow  }{H}_{q}\left( X\right)  \rightarrow  {H}_{q - 1}\left( {U \cap  V}\right)  \rightarrow  \cdots
\]

Here \( f \) is the map induced by the signed inclusion \( a \mapsto  \left( {-a, a}\right) \) and \( g \) is the sum \( \left( {a, b}\right)  \mapsto  a + b \) .

## Singular Cohomology

A singular \( q \) -cochain on a topological space \( X \) is a linear functional on the \( \mathbb{Z} \) -module \( {S}_{q}\left( X\right) \) of singular \( q \) -chains. Thus the group of singular \( q \) -cochains is \( {S}^{q}\left( X\right)  = \) Hom \( \left( {{S}_{q}\left( X\right) ,\mathbb{Z}}\right) \) . With the coboundary operator \( d \) defined by \( \left( {d\omega }\right) \left( c\right)  = \omega \left( {\partial c}\right) \) , the graded group of singular cochains \( {S}^{ * }\left( X\right)  = \bigoplus {S}^{q}\left( X\right) \) becomes a differential complex; the homology of this complex is the singular cohomology of \( X \) with integer coefficients. Replacing \( \mathbb{Z} \) with an Abelian group \( G \) we obtain the singular cohomology with coefficients in \( G \) , denoted \( {H}^{ * }\left( {X;G}\right) \) . For the rest of this chapter we will reserve \( {H}^{ * }\left( X\right) \) for the singular cohomology with integer coefficients and write \( {H}_{DR}^{ * }\left( X\right) \) for the de Rham cohomology.

A function \( \omega \) on \( X \) is a 0-cocycle if and only if \( \omega \left( {\partial c}\right)  = 0 \) for all paths \( c \) in \( X \) . It follows that such an \( \omega \) is constant on each path component of \( X \) . Therefore, \( {H}^{0}\left( X\right)  = \mathbb{Z} \times  \mathbb{Z} \times  \cdots  \times  \mathbb{Z} \) where there are as many copies of \( \mathbb{Z} \) as there are path components of \( X \) .

REMARK. The singular cohomology does not always agree with the Čech cohomology. For instance,

\[
\dim {H}_{\operatorname{sing}}^{0}\left( X\right)  = \# \text{ path components of }X\text{ , }
\]

but

\[
\dim {H}_{\text{ Čech }}^{0}\left( X\right)  = \# \text{ connected components of }X\text{ . }
\]

We now compute the singular cohomology of \( {\mathbb{R}}^{n} \) . Define the operator \( L : {S}^{q}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {S}^{q - 1}\left( {\mathbb{R}}^{n}\right) \) to be the adjoint of the cone construction \( K \) : if \( \sigma  \in \; {S}^{q}\left( {\mathbb{R}}^{n}\right) \) and \( c \in  {S}_{q - 1}\left( {\mathbb{R}}^{n}\right) \) ,

\[
\left( {L\sigma }\right) \left( c\right)  = \sigma \left( {Kc}\right) .
\]

Then for \( \sigma  \in  {S}^{q}\left( {\mathbb{R}}^{n}\right) \) and \( c \in  {S}_{q}\left( {\mathbb{R}}^{n}\right) \) ,

\[
\left( {\left( {{dL} - {Ld}}\right) \sigma }\right) c = \left( {d\left( {L\sigma }\right) }\right) c - \left( {L\left( {d\sigma }\right) }\right) \left( c\right)
\]

\[
= \left( {L\sigma }\right) \left( {\partial c}\right)  - \left( {d\sigma }\right) \left( {Kc}\right)
\]

\[
= \sigma \left( {K\partial c}\right)  - \sigma \left( {\partial {Kc}}\right)
\]

\[
= \sigma \left( {\left( {K\partial  - \partial K}\right) c}\right)
\]

\[
= \left( {{\left( -1\right) }^{q + 1}\sigma }\right) c\text{ by Proposition 15.1. }
\]

Hence

\[
1 = {\left( -1\right) }^{q + 1}\left( {{dL} - {Ld}}\right) \text{ on }{S}^{q}\left( {\mathbb{R}}^{n}\right) , q \geq  1,
\]

i.e., \( L \) is a homotopy operator between the identity map and the zero map on the \( q \) -cochains, \( q \geq  1 \) . It follows that

\[
{H}^{q}\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{Z}, & q = 0 \\  0, & q > 0. \end{array}\right.
\]

Applying the functor \( \operatorname{Hom}\left( {,\mathbb{Z}}\right) \) to the Mayer-Vietoris sequence for singular chains we obtain the Mayer-Vietoris sequence for singular cochains

(15.7)

\[
0 \rightarrow  {S}_{\mathfrak{U}}^{ * }\left( X\right) \overset{{\varepsilon }^{ * }}{ \rightarrow  }\prod {S}^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{{\delta }^{ * }}{ \rightarrow  }\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{S}^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{{\delta }^{ * }}{ \rightarrow  }\ldots
\]

Since the functor \( \operatorname{Hom}\left( {,\mathbb{Z}}\right) \) preserves the exactness of a sequence of free \( \mathbb{Z} \) -modules (see Exercise 14.17.3), the Mayer-Vietoris sequence for singular_ cochains is exact.

Exercise 15.7.1. Show that \( {\varepsilon }^{ * } \) is the restriction map and \( {\delta }^{ * } \) is the alternating difference

\[
{\left( {\delta }^{ * }\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\alpha }_{i}\ldots {\alpha }_{p + 1}}
\]

Once we have the Mayer-Vietoris sequence we can set up the double complex \( {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) . Just as in the de Rham theory the double complex \( {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) computes the singular cohomology of \( X \) . This is because by the exactness of the Mayer-Vietoris sequence, \( {H}_{{\delta }^{ * }} \) of this complex has a single nonzero column

![bo_d7b6f8alb0pc73dd9avg_200_556_972_497_504_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_200_556_972_497_504_0.jpg)

so that the spectral sequence degenerates at the \( {E}_{2} \) term and

\[
H\left\{  {{C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) }\right\}   = {H}_{d}{H}_{{\delta }^{ * }} = {H}^{ * }\left( X\right) .
\]

To complete the analogy we will need the existence of a good cover on the topological space \( X \) . This presents no problem if \( X \) admits a triangulation, i.e., a homeomorphism with the support of a simplicial complex, since the open stars of the vertices of the triangulation form a good cover. By taking barycentric subdivisions of the triangulation we can refine its star ad infinitum. Hence just as in the case of manifolds, the good covers on a triangularizable space \( X \) are cofinal in the set of all covers of \( X \) . We note in passing that this gives an alternative proof of the existence of a good cover on a manifold since it is known that every manifold admits a triangulation (due to Cairns and Whitney, see Whitney [2, pp. 124-135]).

If \( \mathfrak{U} \) is a good cover of a topological space \( X \) , then \( {H}_{d} \) of the double complex \( {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) is

![bo_d7b6f8alb0pc73dd9avg_201_477_424_654_264_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_201_477_424_654_264_0.jpg)

and \( {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathfrak{U},\mathbb{Z}}\right)  = H\left\{  {{C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) }\right\} \) . So there is an isomorphism between the singular cohomology and the Čech cohomology of a good cover with coefficients in the constant presheaf \( \mathbb{Z} \) :

\[
{H}^{ * }\left( X\right)  \simeq  {H}^{ * }\left( {\mathfrak{U},\mathbb{Z}}\right) .
\]

Suppose \( X \) triangularizable. Since the good covers are cofinal in the set of all covers of \( X \) ,

\[
{H}^{ * }\left( {X,\mathbb{Z}}\right)  = {H}^{ * }\left( {\mathfrak{U},\mathbb{Z}}\right)
\]

where \( {H}^{ * }\left( {X,\mathbb{Z}}\right) \) is the Čech cohomology of \( X \) with coefficients in the constant presheaf \( \mathbb{Z} \) . Therefore,

Theorem 15.8. The singular cohomology of a triangularizable space \( X \) is isomorphic to its Čech cohomology with coefficients in the constant presheaf \( \mathbb{Z} \) . If \( \mathfrak{U} \) is a good cover of \( X \) , then

\[
{H}^{ * }\left( X\right)  \simeq  {H}^{ * }\left( {X,\mathbb{Z}}\right)  \simeq  {H}^{ * }\left( {\mathfrak{U},\mathbb{Z}}\right) .
\]

Let \( \pi  : E \rightarrow  X \) be a fiber bundle with fiber \( F \) over a triangularizable topological space \( X \) . Just as in Theorem 14.18, from the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{S}^{ * }}\right) \) on \( E \) we obtain a spectral sequence converging to the singular cohomology \( {H}^{ * }\left( E\right) \) whose \( {E}_{2} \) term is

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( F\right) }\right) ,
\]

where \( {\mathcal{H}}^{q}\left( F\right) \) is the locally constant presheaf \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}U}\right) \) . If \( {\mathcal{H}}^{q}\left( F\right) \) happens to be the constant presheaf \( \mathbb{Z} \oplus  \cdots  \oplus  \mathbb{Z} \) on \( \mathfrak{U} \) , then

\[
\begin{aligned} {E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},\underline{\mathbb{Z}}}\right)  \oplus  \cdots  \oplus  {H}^{p}\left( {\mathfrak{U},\mathbb{Z}}\right) &  = {H}^{p}\left( X\right)  \oplus  \cdots  \oplus  {H}^{p}\left( X\right) \\   &  = {H}^{p}\left( X\right)  \otimes  {H}^{q}\left( F\right) . \end{aligned}
\]

The singular cohomology group \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) can be given a product structure as follows. If \( \left( {{A}_{0}\ldots {A}_{q}}\right) \) is a \( q \) -simplex in \( X \) , we say that \( \left( {{A}_{0}\ldots {A}_{r}}\right) \) is its front \( r \) -face and \( \left( {{A}_{q - r}\ldots {A}_{q}}\right) \) its back r-face. Let \( \omega \) be a \( p \) -cochain and \( \eta \) a \( q \) -cochain; by definition their cup product is given by

(15.9)

\[
\left( {\omega  \cup  \eta }\right) \left( {{A}_{0}\ldots {A}_{p + q}}\right)  = \omega \left( {{A}_{0}\ldots {A}_{p}}\right) \eta \left( {{A}_{p}\ldots {A}_{p + q}}\right) .
\]

Exercise 15.10. Show that the coboundary operator \( d \) is an antiderivation relative to the cup product:

\[
d\left( {\omega  \cup  \eta }\right)  = \left( {d\omega }\right)  \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {d\eta }.
\]

By arguments analogous to (15.2) and (15.7) there is also a Mayer-Vietoris sequence for singular cochains with coefficients in a commutative ring A. Using the cup product (15.9) in place of the wedge product, the spectral sequence of the Čech-singular complex \( {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) can be given a product structure just as in (14.24). The arguments in Section 14 carry over mutatis mutandis. Hence the results on spectral sequences remain true for singular cohomology with coefficients in \( A \) . Note however in (14.18) and (14.30) the \( {E}_{2} \) term of a fiber bundle \( \pi  : E \rightarrow  M \) with fiber \( F \) over a simply connected base space \( M \) is the tensor product \( {H}^{ * }\left( {M;A}\right)  \otimes  {H}^{ * }\left( {F;A}\right) \) only if the cohomology of \( F \) is a free \( A \) -module. In summary we have the following.

Theorem 15.11 (Leray's Theorem for Singular Cohomology with Coefficients in a Commutative Ring \( A \) ). Let \( \pi  : E \rightarrow  X \) be a fiber bundle with fiber \( F \) over a topological space \( X \) and \( \mathfrak{U} \) an open cover of \( X \) . Then there is a spectral sequence converging to \( {H}^{ * }\left( {E;A}\right) \) with \( {E}_{2} \) term

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( {F;A}\right) }\right) .
\]

Each \( {E}_{r} \) in the spectral sequence can be given a product structure relative to which the differential \( {d}_{r} \) is an antiderivation. If \( X \) is simply connected and has a good cover, then

\[
{E}_{2}^{p, q} = {H}^{p}\left( {X,{H}^{q}\left( {F;A}\right) }\right) .
\]

If in addition \( {H}^{ * }\left( {F;A}\right) \) is a finitely generated free \( A \) -module, then

\[
{E}_{2} = {H}^{ * }\left( {X;A}\right)  \otimes  {H}^{ * }\left( {F;A}\right)
\]

as algebras over \( A \) .

Exercise 15.12 (Künneth Formula for Singular Cohomology). If \( X \) is a space having a good cover, e.g., a triangularizable space, and \( Y \) is any topological space, prove using the spectral sequence of the fiber bundle \( \pi  : X \times  Y \rightarrow  X \) that

\[
{H}^{n}\left( {X \times  Y}\right)  = {\bigoplus }_{p + q = n}{H}^{p}\left( {X,{H}^{q}\left( Y\right) }\right)
\]

We examine briefly here how some of the theorems in de Rham theory carry over to the singular theory. Both the Mayer-Vietoris argument of Section 5 and the tic-tac-toe proof of Section 9 for the Leray-Hirsch theorem go through for integer coefficients, with the singular complex \( {C}^{ * }(\mathfrak{U} \) , \( {S}^{ * } \) ) in place of \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) . However, since there may be torsion in \( {H}^{ * }\left( F\right) \) , the Künneth formula in the form \( {H}^{ * }\left( {M \times  F}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) is not true with integer coefficients; the Mayer-Vietoris argument fails because tensoring with \( {H}^{ * }\left( F\right) \) need not preserve exactness, and the tic-tac-toe proof fails because \( {H}^{ * }\left( F\right)  \otimes  {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) may not be simply a finite number of copies of \( {C}^{ * }\left( {\mathfrak{U},{S}^{ * }}\right) \) . These difficulties do not arise in the case of the Leray-Hirsch theorem, since in its hypothesis the cohomology of the fiber \( {H}^{ * }\left( F\right) \) is assumed to be a free \( \mathbb{Z} \) -module.

REMARK 15.13. Given any Abelian group \( A \) , let \( F \) be the free Abelian group generated by a set of generators for \( A \) and let \( R \) be the kernel of the natural map \( p : F \rightarrow  A \) . Then

(15.13.1)

\[
0 \rightarrow  R\overset{i}{ \rightarrow  }F\overset{p}{ \rightarrow  }A \rightarrow  0
\]

is a short exact sequence of Abelian groups. As a subgroup of a free group, \( R \) is also free (Jacobson [1,§3.6]). An exact sequence such as (15.13.1), in which \( F \) and \( R \) are free, is called a free resolution of \( A \) . Let \( G \) be an Abelian group. By Exercise 14.17.4, the two sequences

(15.13.2)

\[
0 \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  \operatorname{Hom}\left( {F, G}\right) \overset{{i}^{ * }}{ \rightarrow  }\operatorname{Hom}\left( {R, G}\right)
\]

and

(15.13.3)

\[
R \otimes  G\xrightarrow[]{i \otimes  1}F \otimes  G \rightarrow  A \otimes  G \rightarrow  0
\]

are exact.

Definition.

\[
\operatorname{Ext}\left( {A, G}\right)  = \text{ coker }{i}^{ * } = \operatorname{Hom}\left( {R, G}\right) /\operatorname{im}{i}^{ * }.
\]

\[
\operatorname{Tor}\left( {A, G}\right)  = \ker i \otimes  1.
\]

Thus Ext and Tor measure the failure of the two exact sequences (15.13.2) and (15.13.3) to be short exact. It is not hard to show that the definition of Ext and Tor is independent of the choice of the free resolution. For the elementary properties of these two functors see, for instance, Switzer [1, Chap. 13].

Exercise 15.13.4. If \( m \) and \( n \) are positive integers, we denote their greatest common divisor by \( \left( {m, n}\right) \) . Verify the tables

<table><tr><td>Ext</td><td>\( \mathbb{Z} \)</td><td>\( {\mathbb{Z}}_{n} \)</td></tr><tr><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td></tr><tr><td>\( \mathbb{{Z}_{m}} \)</td><td>\( {\mathbb{Z}}_{m} \)</td><td>\( {\mathbb{Z}}_{\left( m, n\right) } \)</td></tr></table>

<table><tr><td>Tor</td><td>\( \mathbb{Z} \)</td><td>\( {Z}_{n} \)</td></tr><tr><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td></tr><tr><td>\( \mathbb{{Z}_{m}} \)</td><td>0</td><td>\( {\mathbb{Z}}_{\left( m, n\right) } \)</td></tr></table>

For example,

\[
\operatorname{Ext}\left( {{\mathbb{Z}}_{m},\mathbb{Z}}\right)  = {\mathbb{Z}}_{m}.
\]

In terms of these completely algebraic functors, one finds the following description of the dependence of the singular theory on its coefficient group. For a proof see Spanier [1, pp. 222 and 243].

Theorem 15.14 (Universal Coefficient Theorems). For any space \( X \) and Abelian group G,

(a) the homology of \( X \) with coefficients in \( G \) has a splitting:

\[
{H}_{q}\left( {X;G}\right)  \simeq  {H}_{q}\left( X\right)  \otimes  G \oplus  \operatorname{Tor}\left( {{H}_{q - 1}\left( X\right) , G}\right) ;
\]

(b) the cohomology of \( X \) with coefficients in \( G \) also has a splitting:

\[
{H}^{q}\left( {X;G}\right)  \simeq  \operatorname{Hom}\left( {{H}_{q}\left( X\right) , G}\right)  \oplus  \operatorname{Ext}\left( {{H}_{q - 1}\left( X\right) , G}\right) .
\]

Applying Part (b) with \( G = \mathbb{Z} \) yields the following formula for the integer cohomology in terms of the integer homology.

Corollary 15.14.1. For any space \( X \) for which \( {H}_{q}\left( X\right) \) and \( {H}_{q - 1}\left( X\right) \) are finitely generated \( \mathbb{Z} \) -modules,

\[
{H}^{q}\left( X\right)  \simeq  {F}_{q} \oplus  {T}_{q - 1}
\]

where \( {F}_{q} \) is the free part of \( {H}_{q}\left( X\right) \) and \( {T}_{q - 1} \) is the torsion part of \( {H}_{q - 1}\left( X\right) \) .

REMARK. The splittings given by the universal coefficient theorems cannot be arranged to be compatible with the induced homomorphisms of maps. They are therefore often said to be unnatural splittings.

Example 15.15 (The cohomology of the unit tangent bundle of a sphere). The unit tangent bundle \( S\left( {T}_{{S}^{2}}\right) \) to the 2-sphere in \( {\mathbb{R}}^{3} \) is a fiber bundle with fiber \( {S}^{1} \) :

![bo_d7b6f8alb0pc73dd9avg_204_737_1998_191_140_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_204_737_1998_191_140_0.jpg)

By (15.11) the \( {E}_{2} \) term of the spectral sequence is

\[
{E}_{2}^{p, q} = {H}^{p}\left( {S}^{2}\right)  \otimes  {H}^{q}\left( {S}^{1}\right)
\]

![bo_d7b6f8alb0pc73dd9avg_205_532_462_553_327_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_205_532_462_553_327_0.jpg)

For dimensional reasons \( {d}_{3} = {d}_{4} = \cdots  = 0 \) , so \( {E}_{3} = {E}_{\infty } \) . By Remark 14.20 the differential \( {d}_{2} \) in the diagram defines the Euler class of the circle bundle \( S\left( {T}_{{S}^{2}}\right) \) . Since the Euler class of \( S\left( {T}_{{S}^{2}}\right) \) is twice the generator of \( {H}^{2}\left( {S}^{2}\right) \) (Example 11.18), this \( {d}_{2} \) is multiplication by 2 . Thus

\[
{H}^{ * }S\left( {T}_{{S}^{2}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in dimensions }0\text{ and }3 \\  {\mathbb{Z}}_{2} & \text{ in dimension }2 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Exercise 15.15.1. Compute the cohomology of the unit tangent bundle \( S\left( {T}_{Sk}\right) \) .

A point in \( S\left( {T}_{{S}^{2}}\right) \) is specified by a unit vector in \( {\mathbb{R}}^{3} \) and another unit vector orthogonal to it. This can be completed to a unique orthonormal basis with positive determinant. Therefore \( S\left( {T}_{{S}^{2}}\right)  = {SO}\left( 3\right) \) and we have computed above the cohomology of \( {SO}\left( 3\right) \) .

REMARK 15.15.2. The special orthogonal group \( {SO}\left( 3\right) \) comes in a different guise as \( \mathbb{R}{P}^{3} \) , as follows. We can think of \( {SO}\left( 3\right) \) as the group of all rotations about the origin in \( {\mathbb{R}}^{3} \) . Each such rotation is determined by its axis and an angle \( - \pi  \leq  \theta  \leq  \pi \) . In this way \( {SO}\left( 3\right) \) is parametrized by the solid 3-ball \( {D}^{3} \) of radius \( \pi \) in \( {\mathbb{R}}^{3} \) : a point in this 3-ball determines a unique axis and a unique angle of rotation, the axis being the line through the point and the origin, and the angle being the distance of the point from the origin. Since rotating through the angle \( - \pi \) has the same effect as through \( \pi \) , any pair of antipodal points on the boundary of \( {D}^{3} \) parametrize the same rotation. So \( {SO}\left( 3\right) \) is homeomorphic to \( \mathbb{R}{P}^{3} \) .

Exercise 15.16 (The Cohomology of \( {SO}\left( 4\right) \) ). The special orthogonal group \( {SO}\left( n\right) \) acts transitively on the unit sphere \( {S}^{n - 1} \) in \( {\mathbb{R}}^{n} \) with stabilizer \( {SO}\left( {n - 1}\right) \) . Therefore \( {SO}\left( n\right) /{SO}\left( {n - 1}\right)  = {S}^{n - 1} \) . A group with a differentiable structure relative to which the group operations, namely multiplication and inverse, are smooth is called a Lie group. \( {GL}\left( {n,\mathbb{R}}\right) \) and \( {SO}\left( n\right) \) are examples of Lie groups (see Spivak [1, Ex. 33, p. 83]). It is a fact from the theory of Lie groups that if \( H \) is a closed subgroup of a Lie group \( G \) , i.e., \( H \) is a Lie subgroup and a closed subset of \( G \) , then \( \pi  : G \rightarrow  G/H \) is a fiber bundle with fiber \( H \) (Warner [1, Th. 3.58, p. 120]). Apply the spectral sequence of the fiber bundle

\[
{SO}\left( 3\right)  \rightarrow  {SO}\left( 4\right)
\]

\[
{S}^{3}
\]

↓

to compute the cohomology of \( {SO}\left( 4\right) \) .

Exercise 15.17 (The Cohomology of the Unitary Group). The unitary group \( U\left( n\right) \) acts transitively on the unit sphere \( {S}^{{2n} - 1} \) in \( {\mathbb{C}}^{n} \) with stabilizer \( U\left( {n - 1}\right) \) . Hence \( U\left( n\right) /U\left( {n - 1}\right)  = {S}^{{2n} - 1} \) . Apply the spectral sequence of the fiber bundle

\[
U\left( {n - 1}\right)  \rightarrow  U\left( n\right)
\]

\[
{S}^{{2n} - 1}
\]

to compute the cohomology of \( U\left( n\right) \) .

## The Homology Spectral Sequence

Although in this book we are primarily concerned with cohomology, for applications to homotopy theory it is frequently advantageous to use the homology spectral sequence of a fibering. Since the construction of such a spectral sequence is analogous to that for cohomology, the discussion will be brief.

Using the singular chain functor \( {S}_{ * } \) in place of the differential form functor \( {\Omega }^{ * } \) we get a double complex \( {C}_{ * }\left( {\mathfrak{U},{S}_{ * }}\right) \) with differential operators \( \partial \) and \( \delta \) . Define \( D \) to be \( \delta  + {\left( -1\right) }^{p}\partial \) .

![bo_d7b6f8alb0pc73dd9avg_206_516_1787_567_393_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_206_516_1787_567_393_0.jpg)

As in Section 14 this double complex gives rise to a spectral sequence \( \left\{  {E}^{r}\right\} \) which converges to the total homology \( {H}_{D}\left\{  {{C}_{ * }\left( {\mathfrak{U},{S}_{ * }}\right) }\right\} \) . Because of the directions of the arrows \( \partial \) and \( \delta \) , the differential \( {d}^{r} \) goes in the opposite direction as the differential of a cohomology spectral sequence; more precisely,

\[
{d}^{r} : {E}_{p, q}^{r} \rightarrow  {E}_{p - r, q + r - 1}^{r}
\]

By the exactness of the Mayer-Vietoris sequence (15.2) the spectral sequence is degenerate at the \( {E}^{2} \) term and

\[
{E}^{2} = {H}_{0}{H}_{\delta } = {H}_{ * }\left( X\right)
\]

Hence we have the following.

Proposition 15.18. For any cover \( \mathfrak{U} \) of \( X \) the double complex \( {C}_{ * }\left( {\mathfrak{U},{S}_{ * }}\right) \) computes the singular homology of \( X \) :

\[
{H}_{D}\left\{  {{C}_{ * }\left( {\mathfrak{U},{S}_{ * }}\right) }\right\}   = {H}_{ * }\left( X\right) .
\]

To avoid confusion with the cohomology spectral sequence, we write \( r \) as a superscript and \( p \) and \( q \) as subscripts in the homology spectral sequence: \( {E}_{p, q}^{r} \) .

Now suppose \( \mathfrak{U} \) is a good cover of \( X \) . Interchanging the roles of \( \partial \) and \( \delta \) gives another spectral sequence which also converges to \( {H}_{D}\left\{  {{C}_{ * }\left( {\mathfrak{U},{S}_{ * }}\right) }\right\} \) . This time

(15.19)

\[
{E}^{\infty } = {E}^{2} = {H}_{\delta }{H}_{\delta } = {H}_{ * }\left( {\mathfrak{U},\mathbb{Z}}\right)
\]

where \( \mathbb{Z} \) is the constant presheaf with group \( \mathbb{Z} \) . Comparing (15.18) with (15.19) gives the isomorphism of the singular homology to the Čech homology \( {H}_{ * }\left( {\mathfrak{U},\mathbb{Z}}\right) \) of a good cover. Along the line of Theorem 14.18, if \( \pi  : E \rightarrow  X \) is a fiber bundle with fiber \( F \) , and \( X \) is a simply connected space with a good cover, then there is a spectral sequence converging to the singular homology \( {H}_{ * }\left( E\right) \) with \( {E}_{p, q}^{2} = {H}_{p}\left( {X,{H}_{q}\left( F\right) }\right) \) . If in addition \( {H}_{q}\left( F\right) \) is a free \( \mathbb{Z} \) -module, the \( {E}^{2} \) term is isomorphic to the tensor product \( {H}_{p}\left( X\right)  \otimes  {H}_{q}\left( F\right) \) as \( \mathbb{Z} \) -modules. Unlike the cohomology spectral sequence, there is in general no product structure in homology.
