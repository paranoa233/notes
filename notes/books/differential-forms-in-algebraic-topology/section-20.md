## CHAPTER IV Characteristic Classes

After the excursion into homotopy theory in the previous chapter, we return now to the differentiable category. Thus in this chapter, in the absence of explicit qualifications, all spaces are smooth manifolds, all maps are smooth maps, and \( {H}^{ * }\left( X\right) \) denotes the de Rham cohomology.

In Section 6 we first encountered the Euler class of a \( {C}^{\infty } \) oriented rank 2 vector bundle. It is but one of the many characteristic classes, that is, cohomology classes intrinsically associated to a vector bundle. In its modern form the theory of characteristic classes originated with Hopf, Stiefel, Whitney, Chern, and Pontrjagin. It has since found many applications to topology, differential geometry, and algebraic geometry.

In its most rudimentary form the point of view towards the Chern classes really goes back to the old Italian algebraic geometers, but in Section 20 we recast it along the ideas of Grothendieck. We introduce in Section 21 the computational and proof technique known as the splitting principle. This is followed by the Pontrjagin classes, which may be considered the real analogue of the Chern classes. We also include an application to the embedding of manifolds.

In the final section the Chern classes are shown to be the only complex characteristic classes in the following sense: any natural transformation from the complex vector bundles to the cohomology ring is a polynomial in the Chern classes. An added dividend is a classification theorem for complex vector bundles. With its aid we fulfill an earlier promise (see the remark following Prop. 11.9) to show that the vanishing of the Euler class of an oriented sphere bundle does not imply the existence of a section.

For the Euler class of a rank 2 bundle we had in (6.38) an explicit formula in terms of the patching data on the base manifold \( M \) . Elegant as the Grothendieck approach to the Chern classes is, it is not directly linked to the geometry of \( M \) , for it gives no such patching formulas. In the concluding remarks to this chapter we describe without proof a recipe for constructing the Chern classes of a complex vector bundle \( \pi  : E \rightarrow  M \) out of the transition functions of \( E \) and a partition of unity on \( M \) relative to some trivializing good cover for \( E \) .

## §20 Chern Classes of a Complex Vector Bundle

In this section we will study the characteristic classes of a complex vector bundle. To begin with we define the first Chern class of a complex line bundle as the Euler class of its underlying real bundle. Applying the Leray-Hirsch theorem, we then compute the cohomology ring of the projectivization \( P\left( E\right) \) of a complex vector bundle \( E \) and define the Chern classes of \( E \) in terms of the ring structure of \( {H}^{ * }\left( {P\left( E\right) }\right) \) . We conclude with a list of the main properties of the Chern classes.

## The First Chern Class of a Complex Line Bundle

Recall that a complex vector bundle of rank \( n \) is a fiber bundle with fiber \( {\mathbb{C}}^{n} \) and structure group \( {GL}\left( {n,\mathbb{C}}\right) \) . A complex vector bundle of rank 1 is also called a complex line bundle. Just as the structure group of a real vector bundle can be reduced to the orthogonal group \( O\left( n\right) \) , so by the Hermitian analogue of (6.4), the structure group of a rank \( n \) complex vector bundle can be reduced to the unitary group \( U\left( n\right) \) . Every complex vector bundle \( E \) of rank \( n \) has an underlying real vector bundle \( {E}_{\mathbb{R}} \) of rank \( {2n} \) , obtained by discarding the complex structure on each fiber. By the isomorphism of \( U\left( 1\right) \) with \( {SO}\left( 2\right) \) , this sets up a one-to-one correspondence between the complex line bundles and the oriented rank 2 real bundles. We define the first Chern class of a complex line bundle \( L \) over a manifold \( M \) to be the Euler class of its underlying real bundle \( {L}_{\mathbb{R}} : {c}_{1}\left( L\right)  = e\left( {L}_{\mathbb{R}}\right)  \in  {H}^{2}\left( M\right) \) .

If \( L \) and \( L \) are complex line bundles with transition functions \( \left\{  {g}_{\alpha \beta }\right\} \) and \( \left\{  {g}_{\alpha \beta }^{\prime }\right\} \)

\[
{g}_{\alpha \beta },{g}_{\alpha \beta }^{\prime } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  {\mathbb{C}}^{ * },
\]

then their tensor product \( L \otimes  L \) is the complex line bundle with transition functions \( \left\{  {{g}_{\alpha \beta } \cdot  {g}_{\alpha \beta }^{\prime }}\right\} \) . By the formula (6.38) which gives the Euler class in terms of the transition functions, we have

(20.1)

\[
{c}_{1}\left( {L \otimes  L}\right)  = {c}_{1}\left( L\right)  + {c}_{1}\left( L\right) .
\]

Let \( {L}^{ * } \) be the dual of \( L \) . Since the line bundle \( L \otimes  {L}^{ * } = \operatorname{Hom}\left( {L, L}\right) \) has a nowhere vanishing section given by the identity map, \( L \otimes  {L}^{ * } \) is a trivial bundle. By (20.1), \( {c}_{1}\left( L\right)  + {c}_{1}\left( {L}^{ * }\right)  = {c}_{1}\left( {L \otimes  {L}^{ * }}\right)  = 0 \) . Therefore,

(20.2)

\[
{c}_{1}\left( {L}^{ * }\right)  =  - {c}_{1}\left( L\right) .
\]

EXAMPLE 20.3 (Tautological bundles on a projective space). Let \( V \) be a complex vector space of dimension \( n \) and \( P\left( V\right) \) its projectivization:

\[
P\left( V\right)  = \{ 1\text{ -dimensional subspaces of }V\} \text{ . }
\]

On \( P\left( V\right) \) there are several God-given vector bundles: the product bundle \( \widehat{V} = P\left( V\right)  \times  V \) , the universal subbundle \( S \) , which is the subbundle of \( \widehat{V} \) defined by

\[
S = \{ \left( {\ell , v}\right)  \in  P\left( V\right)  \times  V \mid  v \in  \ell \} ,
\]

and the universal quotient bundle \( Q \) , defined by the exact sequence

(20.4)

\[
0 \rightarrow  S \rightarrow  \widehat{V} \rightarrow  Q \rightarrow  0
\]

The fiber of \( S \) above each point \( \ell \) in \( P\left( V\right) \) consists of all the points in \( \ell \) , where \( \ell \) is viewed as a line in the vector space \( V \) . The sequence (20.4) is called the tautological exact sequence over \( P\left( V\right) \) , and \( {S}^{ * } \) the hyperplane bundle.

Consider the composition

\[
\sigma  : S \hookrightarrow  P\left( V\right)  \times  V \rightarrow  V
\]

of the inclusion followed by the projection. The inverse image of any point \( v \) is

\[
{\sigma }^{-1}\left( v\right)  = \{ \left( {\ell , v}\right)  \mid  v \in  \ell \} .
\]

If \( v \neq  0,{\sigma }^{-1}\left( v\right) \) consists of precisely one point \( \left( {\ell , v}\right) \) where \( \ell \) is the line through the origin and \( v \) ; if \( v = 0 \) , then \( {\sigma }^{-1}\left( 0\right) \) is isomorphic to \( P\left( V\right) \) . Thus \( S \) may be obtained from \( V \) by separating all the lines through the origin in \( V \) . This map \( \sigma  : S \rightarrow  V \) is called the blow-up or the quadratic transformation of of \( V \) at the origin. Over the real numbers the blow-up of a plane may be pictured as the portion of a helicoid in Figure 20.1 with its top and bottom edges identified. Indeed, we may view the \( \left( {x, y}\right) \) -plane as being traced out by a horizontal line rotating about the origin. In order to separate these lines at the origin, we let the generating line move with constant velocity along the \( z \) -axis while it is rotating horizontally. The resulting surface in \( {\mathbb{R}}^{3} \) is a helicoid.

We now compute the cohomology of \( P\left( V\right) \) . Endow \( V \) with a Hermitian metric and let \( E \) be the unit sphere bundle of the universal subbundle \( S \) :

\[
E = \{ \left( {\ell , v}\right)  \mid  v \in  \ell ,\parallel v\parallel  = 1\} .
\]

Note that \( {\sigma }^{-1}\left( 0\right) \) is the zero section of the universal subbundle \( S \) . Since \( S - {\sigma }^{-1}\left( 0\right) \) is diffeomorphic to \( V - \{ 0\} \) , we see that \( E \) is diffeomorphic to the sphere \( {S}^{{2n} - 1} \) in \( V \) and that the map \( \pi  : E \rightarrow  P\left( V\right) \) gives a fibering

\[
{S}^{1} \rightarrow  {S}^{{2n} - 1}
\]

![bo_d7b6f8alb0pc73dd9avg_279_419_295_784_725_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_279_419_295_784_725_0.jpg)

Figure 20.1

By a computation similar to (14.32), the cohomology ring \( {H}^{ * }\left( {P\left( V\right) }\right) \) is seen to be generated by the Euler class of the circle bundle \( E \) , i.e., the first Chern class of the universal subbundle \( S \) . It is customary to take \( x = {c}_{1}\left( {S}^{ * }\right)  = \; - {c}_{1}\left( S\right) \) to be the generator and write

(20.5)

\[
{H}^{ * }\left( {P\left( V\right) }\right)  = \mathbb{R}\left\lbrack  x\right\rbrack  /\left( {x}^{n}\right) ,\;\text{ where }n = {\dim }_{\mathbb{C}}V.
\]

We define the Poincaré series of a manifold \( M \) to be

\[
{P}_{t}\left( M\right)  = \mathop{\sum }\limits_{{i = 0}}^{\infty }\dim {H}^{i}\left( M\right) {t}^{i}
\]

By (20.5) the Poincaré series of the projective space \( P\left( V\right) \) is

\[
{P}_{t}\left( {P\left( V\right) }\right)  = 1 + {t}^{2} + \cdots  + {t}^{2\left( {n - 1}\right) } = \frac{1 - {t}^{2n}}{1 - {t}^{2}}.
\]

## The Projectivization of a Vector Bundle

Let \( \rho  : E \rightarrow  M \) be a complex vector bundle with transition functions \( {g}_{\alpha \beta } \) : \( {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  {GL}\left( {n,\mathbb{C}}\right) \) . We write \( {E}_{p} \) for the fiber over \( p \) and \( {PGL}\left( {n,\mathbb{C}}\right) \) for the projective general linear group \( {GL}\left( {n,\mathbb{C}}\right) /\{ \) scalar matrices \( \} \) . The projectivization of \( E,\pi  : P\left( E\right)  \rightarrow  M \) , is by definition the fiber bundle whose fiber at a point \( p \) in \( M \) is the projective space \( P\left( {E}_{p}\right) \) and whose transition functions \( {\bar{g}}_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  {PGL}\left( {n,\mathbb{C}}\right) \) are induced from \( {g}_{\alpha \beta } \) . Thus a point of \( P\left( E\right) \) is a line \( {\ell }_{p} \) in the fiber \( {E}_{p} \) .

As on the projectivization of a vector space, on \( P\left( E\right) \) there are several tautological bundles: the pullback \( {\pi }^{-1}E \) , the universal subbundle \( S \) , and the universal quotient bundle \( Q \) .

\[
0 \rightarrow  S \rightarrow  {\pi }^{-1}E \rightarrow  Q \rightarrow  0
\]

![bo_d7b6f8alb0pc73dd9avg_280_671_466_422_209_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_280_671_466_422_209_0.jpg)

The pullback bundle \( {\pi }^{-1}E \) is the vector bundle over \( P\left( E\right) \) whose fiber at \( {\ell }_{p} \) is \( {E}_{p} \) . When restricted to the fiber \( {\pi }^{-1}\left( p\right) \) it becomes the trivial bundle,

\[
{\left. {\pi }^{-1}E\right| }_{P{\left( E\right) }_{p}} = P{\left( E\right) }_{p} \times  {E}_{p},
\]

since \( \rho  : {E}_{p} \rightarrow  \{ p\} \) is a trivial bundle. The universal subbundle \( S \) over \( P\left( E\right) \) is defined by

\[
S = \left\{  {\left( {{\ell }_{p}, v}\right)  \in  {\pi }^{-1}E \mid  v \in  {\ell }_{p}}\right\}  .
\]

Its fiber at \( {\ell }_{p} \) consists of all the points in \( {\ell }_{p} \) . The universal quotient bundle \( Q \) is determined by the tautological exact sequence

\[
0 \rightarrow  S \rightarrow  {\pi }^{-1}E \rightarrow  Q \rightarrow  0.
\]

Set \( x = {c}_{1}\left( {S}^{ * }\right) \) . Then \( x \) is a cohomology class in \( {H}^{2}\left( {P\left( E\right) }\right) \) . Since the restriction of the universal subbundle \( S \) on \( P\left( E\right) \) to a fiber \( P\left( {E}_{p}\right) \) is the universal subbundle \( \widetilde{S} \) of the projective space \( P\left( {E}_{p}\right) \) , by the naturality property of the first Chern class (6.39), it follows that \( {c}_{1}\left( \widetilde{S}\right) \) is the restriction of \( - x \) to \( P\left( {E}_{p}\right) \) . Hence the cohomology classes \( 1, x,\ldots ,{x}^{n - 1} \) are global classes on \( P\left( E\right) \) whose restrictions to each fiber \( P\left( {E}_{p}\right) \) freely generate the cohomology of the fiber. By the Leray-Hirsch theorem (5.11) the cohomology \( {H}^{ * }\left( {P\left( E\right) }\right) \) is a free module over \( {H}^{ * }\left( M\right) \) with basis \( \left\{  {1, x,\ldots ,{x}^{n - 1}}\right\} \) . So \( {x}^{n} \) can be written uniquely as a linear combination of \( 1, x,\ldots ,{x}^{n - 1} \) with coefficients in \( {H}^{ * }\left( M\right) \) ; these coefficients are by definition the Chern classes of the complex vector bundle \( E \) :

(20.6)

\[
{x}^{n} + {c}_{1}\left( E\right) {x}^{n - 1} + \cdots  + {c}_{n}\left( E\right)  = 0,\;{c}_{i}\left( E\right)  \in  {H}^{2i}\left( M\right) .
\]

In this equation by \( {c}_{i}\left( E\right) \) we really mean \( {\pi }^{ * }{c}_{i}\left( E\right) \) . We call \( {c}_{i}\left( E\right) \) the ith Chern class of \( E \) and

\[
c\left( E\right)  = 1 + {c}_{1}\left( E\right)  + \cdots  + {c}_{n}\left( E\right)  \in  {H}^{ * }\left( M\right)
\]

its total Chern class. With this definition of the Chern classes, we see that the ring structure of the cohomology of \( P\left( E\right) \) is given by

(20.7)

\[
{H}^{ * }\left( {P\left( E\right) }\right)  = {H}^{ * }\left( M\right) \left\lbrack  x\right\rbrack  /\left( {{x}^{n} + {c}_{1}\left( E\right) {x}^{n - 1} + \cdots  + {c}_{n}\left( E\right) }\right) ,
\]

where \( x = {c}_{1}\left( {S}^{ * }\right) \) and \( n \) is the rank of \( E \) . Since additively

\[
{H}^{ * }\left( {P\left( E\right) }\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( {P}^{n - 1}\right) ,
\]

where \( {P}^{n - 1} \) is the complex projective space \( P\left( {\mathbb{C}}^{n}\right) \) , the Poincaré series of \( P\left( E\right) \) is

(20.8)

\[
{P}_{t}\left( {P\left( E\right) }\right)  = {P}_{t}\left( M\right) \frac{1 - {t}^{2n}}{1 - {t}^{2}}.
\]

We now have two definitions of the first Chern class of a line bundle \( L \) : as the Euler class of \( {L}_{\mathbb{R}} \) , and as a coefficient in (20.6). To check that these two definitions agree we will temporarily reserve the notation \( {c}_{1} \) (   )for the second definition. What must be shown is that \( e\left( {L}_{\mathbb{R}}\right)  = {c}_{1}\left( L\right) \) .(20.9)

![bo_d7b6f8alb0pc73dd9avg_281_607_700_418_283_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_281_607_700_418_283_0.jpg)

For a line bundle \( L, P\left( L\right)  = M,{\pi }^{-1}L = L \) and the universal subbundle \( S \) on \( P\left( L\right) \) is \( L \) itself. Therefore, \( x = e\left( {S}_{\mathbb{R}}^{ * }\right)  =  - e\left( {S}_{\mathbb{R}}\right)  =  - e\left( {L}_{\mathbb{R}}\right) \) . So the relation (20.6) is \( x + e\left( {L}_{\mathbb{R}}\right)  = 0 \) , which proves that \( {c}_{1}\left( L\right)  = e\left( {L}_{\mathbb{R}}\right) \) .

If \( E \) is the trivial bundle \( M \times  V \) over \( M \) , then \( P\left( E\right)  = M \times  P\left( V\right) \) , so \( {x}^{n} = 0 \) . Hence all the Chern classes of a trivial bundle are zero. In this sense the Chern classes measure the twisting of a complex vector bundle.

## Main Properties of the Chern Classes

In this section we collect together some basic properties of the Chern classes.

(20.10.1) (Naturality) If \( f \) is a map from \( Y \) to \( X \) and \( E \) is a complex vector bundle over \( X \) , then \( c\left( {{f}^{-1}E}\right)  = {f}^{ * }c\left( E\right) \) .

![bo_d7b6f8alb0pc73dd9avg_281_728_1636_221_185_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_281_728_1636_221_185_0.jpg)

Proof. Basically this property follows from the functoriality of all the constructions in the definition of the Chern class. To be precise, by (6.39) the first Chern class of a line bundle is functorial. Write \( {S}_{E} \) for the universal subbundle over \( {PE} \) . Now \( {f}^{-1}{PE} = P\left( {{f}^{-1}E}\right) \) and \( {f}^{-1}{S}_{E}^{ * } = {S}_{{f}^{-1}E}^{ * } \) , so if \( {x}_{E} = {c}_{1}\left( {S}_{E}^{ * }\right) \) , then

\[
{x}_{{f}^{-1}E} = {c}_{1}\left( {S}_{{f}^{-1}E}^{ * }\right)  = {c}_{1}\left( {{f}^{-1}{S}_{E}^{ * }}\right)  = {f}^{ * }{x}_{E}.
\]

Applying \( {f}^{ * } \) to

\[
{x}_{E}^{n} + {c}_{1}\left( E\right) {x}_{E}^{n - 1} + \cdots  + {c}_{n}\left( E\right)  = 0,
\]

we get

\[
{x}_{{f}^{-1}E}^{n} + {f}^{ * }{c}_{1}\left( E\right) {x}_{{f}^{-1}E}^{n - 1} + \cdots  + {f}^{ * }{c}_{n}\left( E\right)  = 0.
\]

Hence

\[
{c}_{i}\left( {{f}^{-1}E}\right)  = {f}^{ * }{c}_{i}\left( E\right) .
\]

It follows from the naturality of the Chern class that if \( E \) and \( F \) are isomorphic vector bundles over \( X \) , then \( c\left( E\right)  = c\left( F\right) \) .

(20.10.2) Let \( V \) be a complex vector space. If \( {S}^{ * } \) is the hyperplane bundle over \( P\left( V\right) \) , then \( {c}_{1}\left( {S}^{ * }\right) \) generates the algebra \( {H}^{ * }\left( {P\left( V\right) }\right) \) .

This was proved earlier (20.5).

(20.10.3) (Whitney Product Formula) \( c\left( {{E}^{\prime } \oplus  {E}^{\prime \prime }}\right)  = c\left( {E}^{\prime }\right) c\left( {E}^{\prime \prime }\right) \) .

The proof will be given in the next section.

In fact, these three properties uniquely characterize the Chern class (Hirzebruch [1, pp. 58-60]). For future reference we list below three more useful properties.

(20.10.4) If \( E \) has rank \( n \) as a complex vector bundle, then \( {c}_{i}\left( E\right)  = 0 \) for \( i > n \) .

This is really a definition.

(20.10.5) If \( E \) has a nonvanishing section, then the top Chern class \( {c}_{n}\left( E\right) \) is zero.

Proof. Such a section \( s \) induces a section \( \widetilde{s} \) of \( P\left( E\right) \) as follows. At a point \( p \) in \( X \) , the value of \( \widetilde{s} \) is the line in \( {E}_{p} \) through the origin and \( s\left( p\right) \) .

\[
P\left( E\right)
\]

\[
\widetilde{s} \uparrow  \pi
\]

\( X \)

Then \( {\widetilde{s}}^{-1}{S}_{E} \) is a line bundle over \( X \) whose fiber at \( p \) is the line in \( {E}_{p} \) spanned by \( s\left( p\right) \) . Since every line bundle with a nonvanishing section is isomorphic to the trivial bundle, we have the tautology

\[
{\widetilde{s}}^{-1}{S}_{E} \simeq  \text{ the trivial line bundle. }
\]

It follows from the naturality of the Chern class that

\[
{\widetilde{s}}^{ * }{c}_{1}\left( {S}_{E}\right)  = 0,
\]

which implies that

\[
{\widetilde{s}}^{ * }x = 0\text{ . }
\]

Applying \( {\widehat{s}}^{ * } \) to

\[
{x}^{n} + {c}_{1}{x}^{n - 1} + \cdots  + {c}_{n} = 0,
\]

we get

\[
{\widetilde{s}}^{ * }{c}_{n} = 0\text{ . }
\]

By our abuse of notation this really means \( {\widetilde{s}}^{ * }{\pi }^{ * }{c}_{n} = 0 \) . Therefore \( {c}_{n} = 0 \) .

(20.10.6) The top Chern class of a complex vector bundle \( E \) is the Euler class of its realization :

\[
{c}_{n}\left( E\right)  = e\left( {E}_{\mathbb{R}}\right) ,\;\text{ where }n = \operatorname{rank}E.
\]

This proposition will be proved in the next section after we have established the splitting principle.
