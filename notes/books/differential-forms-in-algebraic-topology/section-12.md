## §12 Thom Isomorphism and Poincaré Duality Revisited

In this section we study the Thom isomorphism and Poincaré duality from the tic-tac-toe point of view. The results obtained here are more general than those of Sections 5 and 6 in two ways:

(a) \( M \) need not have a finite good cover,

and

(b) the orientability assumption on the vector bundle \( E \) has been dropped.

## The Thom Isomorphism

Let \( \pi  : E \rightarrow  M \) be a rank \( n \) vector bundle. \( E \) is not assumed to be orient-able. We are interested in the cohomology of \( E \) with compact support in the vertical direction, \( {H}_{cv}^{ * }\left( E\right)  = {H}^{ * }\left\{  {{\Omega }_{cv}^{ * }\left( E\right) }\right\} \) . Recall that

(a) \( {H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimension }n \\  0 & \text{ otherwise } \end{array}\right. \)

(b) (Poincaré lemma) \( {H}_{cv}^{ * }\left( {M \times  {\mathbb{R}}^{n}}\right)  = {H}^{* - n}\left( M\right) \) .

Let \( \mathfrak{U} \) be a good cover of the base manifold \( M \) . We augment the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }_{cv}^{ * }}\right) \) by adding a column consisting of the kernels of the first \( \delta \) :

![bo_d7b6f8alb0pc73dd9avg_140_514_813_609_193_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_140_514_813_609_193_0.jpg)

Using a partition of unity from the base, it can be shown that all the rows of this agumented double complex are exact. The proof is identical to that of the generalized Mayer-Vietoris sequence in (8.5) and will not be repeated here. From the exactness of the rows of the augmented complex, it follows as in (8.8) that the cohomology of the initial column is the total cohomology of the double complex, i.e.,

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }_{cv}^{ * }}\right) }\right\}  .
\]

On the other hand,

\[
{H}_{d}^{p, q}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }_{cv}^{ * }}\right) }\right\}   = {H}_{cv}^{q}\left( {\coprod {\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)
\]

\[
= \prod {H}_{cv}^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)
\]

\[
= {C}^{p}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{q}}\right) ,
\]

where \( {\mathcal{H}}_{cv}^{q} \) is the presheaf given by

\[
{\mathcal{H}}_{cv}^{q}\left( U\right)  = {H}_{cv}^{q}\left( {{\pi }^{-1}U}\right)
\]

By the Poincaré lemma for compactly supported cohomology, if \( U \) is contractible, then

\[
{\mathcal{H}}_{cv}^{q}\left( U\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ if }q = n \\  0 & \text{ otherwise. } \end{array}\right.
\]

Therefore \( {H}_{d} \) and also \( {H}_{\delta }^{p, q}{H}_{d} = {H}_{\delta }^{p}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{q}}\right) }\right\}   = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{q}}\right) \) have entries only in the \( n \) th row.

Proposition 12.1. Given any double complex \( K \) , if \( {H}_{\delta }{H}_{d}\left( K\right) \) has entries only in one row, then \( {H}_{\delta }{H}_{d} \) is isomorphic to \( {H}_{D} \) .

This proposition will be substantially generalized in Section 14, for it is simply an example of a degenerate spectral sequence. Its proof is a technical exercise which we defer to the end of this section. Combined with the preceding discussion, it gives

\[
{H}_{cv}^{ * }\left( E\right)  = {H}_{D}^{ * } = {\bigoplus }_{p + q =  * }{H}^{p}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{q}}\right)  = {H}^{* - n}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{n}}\right) .
\]

This is the Thom isomorphism for a not necessarily orientable vector bundle.

Theorem 12.2 (Thom Isomorphism). For \( \pi  : E \rightarrow  M \) any vector bundle of rank \( n \) over \( M \) and \( \mathfrak{U} \) a good cover of \( M \) ,

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{n}}\right) ,
\]

where \( {\mathcal{H}}_{cv}^{n} \) is the presheaf \( {\mathcal{H}}_{cv}^{n}\left( U\right)  = {H}_{cv}^{n}\left( {{\pi }^{-1}U}\right) \) .

We now deduce the orientable version of the Thom isomorphism from this. So suppose \( \pi  : E \rightarrow  M \) is an orientable vector bundle of rank \( n \) over \( M \) . This means there exist forms \( {\sigma }_{\alpha } \) on the sphere bundles \( {\left. S\left( E\right) \right| }_{{U}_{\alpha }} \) which restrict to a generator on each fiber and such that on overlaps \( {U}_{\alpha } \cap  {U}_{\beta } \) their cohomology classes agree: \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {\sigma }_{\beta }\right\rbrack \) . Now choose a Riemannian metric on \( E \) so that the "radius" \( r \) is well-defined on each fiber and any function of the radius \( r \) is a global function on \( E \) . Let \( \rho \left( r\right) \) be the function shown in Figure 12.1. Then \( \left( {d\rho }\right) {\sigma }_{\alpha } \) is a form on \( {\left. E\right| }_{{U}_{\alpha }} \) , where we regard \( {\sigma }_{\alpha } \) as a form on the complement of the zero section. Furthermore, \( \left\lbrack  {\left( {d\rho }\right) {\sigma }_{\alpha }}\right\rbrack   \in  {H}_{ev}^{n}\left( {E{ \mid  }_{{U}_{\alpha }}}\right) \) restricts to a generator of the compactly supported cohomology of the fiber and \( \left\lbrack  {\left( {d\rho }\right) {\sigma }_{\alpha }}\right\rbrack   = \left\lbrack  {\left( {d\rho }\right) {\sigma }_{\beta }}\right\rbrack \) on \( {U}_{\alpha } \cap  {U}_{\beta } \) . Since the fiber has no cohomology in dimensions less than \( n,{\sigma }^{0, n} = \left\{  {\left( {d\rho }\right) {\sigma }_{\alpha }}\right\} \) can be extended to a \( D \) -cocycle. This \( D \) -cocycle corresponds to a global closed form \( \Phi \) on \( E \) , the Thom class of \( E \) , which restricts to a generator on each fiber. Now \( {\mathcal{H}}_{cv}^{n}\left( U\right) \) is generated by \( {\left. \Phi \right| }_{U} \) and for \( V \subset  U \) the restriction map from \( {\mathcal{H}}_{cv}^{n}\left( U\right) \) to \( {\mathcal{H}}_{cv}^{n}\left( V\right) \) sends \( {\left. \Phi \right| }_{U} \) to \( {\left. \Phi \right| }_{V} \) . Hence, via the map which sends \( {\left. \Phi \right| }_{U} \) , for every open set \( U \) , to the generator 1 of the constant presheaf \( \mathbb{R} \) , the presheaf \( {\mathcal{H}}_{cv}^{n} \) is isomorphic to R. The Thom isomorphism theorem then assumes the form

(12.2.1)

\[
{H}_{cv}^{ * }\left( E\right)  \simeq  {H}^{* - n}\left( {\mathfrak{U},{\mathcal{H}}_{cv}^{n}}\right)  = {H}^{* - n}\left( {\mathfrak{U},\mathbb{R}}\right)  = {H}^{* - n}\left( M\right) ,
\]

![bo_d7b6f8alb0pc73dd9avg_141_498_1591_628_488_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_141_498_1591_628_488_0.jpg)

Figure 12.1

for an orientable rank \( n \) vector bundle \( E \) . This agrees with Proposition 6.17. It holds in particular when \( M \) is simply connected, since by (11.5), every vector bundle over a simply connected manifold is orientable.

From the explicit formula (11.11) for the global angular form on an oriented sphere bundle, we can derive a formula for the Thom class of an oriented vector bundle. Let \( f : {E}^{0} \rightarrow  S\left( E\right) \) be a deformation retraction of the complement of the zero section in \( E \) onto the unit sphere bundle. If \( {\psi }_{s} \) is the global angular form on \( S\left( E\right) \) , then \( \psi  = {f}^{ * }{\psi }_{s} \in  {H}^{n - 1}\left( {E}^{0}\right) \) is the global angular form on \( {E}^{0} \) . It has the property that

\[
{d\psi } =  - {\pi }^{ * }e,
\]

where \( e \) represents the Euler class of the bundle \( E \) .

Proposition 12.3. The cohomology class of

\[
\Phi  = d\left( {\rho \left( r\right)  \cdot  \psi }\right)  \in  {\Omega }_{cv}^{n}\left( E\right)
\]

is the Thom class of the oriented vector bundle E.

Proof. Note that

(12.3.1)

\[
\Phi  = {d\rho }\left( r\right)  \cdot  \psi  - \rho \left( r\right) {\pi }^{ * }e.
\]

For the same reasons as in the discussion following (6.40), \( \Phi \) is a closed global form on \( E \) with compact support in the vertical direction. Its restriction to the fiber at \( p \) is \( {d\rho }\left( r\right)  \cdot  {\iota }_{p}^{ * }\psi \) , where \( {\iota }_{p} : {E}_{p} \rightarrow  E \) is the inclusion and \( {\iota }_{p}^{ * }\psi \) gives a generator of \( {H}^{n - 1}\left( {{\mathbb{R}}^{n}-\{ 0\} }\right)  = {H}^{n - 1}\left( {S}^{n - 1}\right) \) . Since

\[
{\int }_{{\mathbb{R}}^{n}}{d\rho }\left( r\right)  \cdot  {l}_{p}^{ * }\psi  = {\int }_{{\mathbb{R}}^{1}}{d\rho }\left( r\right) {\int }_{{S}^{n - 1}}{l}_{p}^{ * }\psi  = 1,
\]

by (6.18), \( \Phi \) is the Thom class of \( E \) .

If \( s \) is the zero section of \( E \) , then \( {s}^{ * }{d\rho } = 0 \) and \( {s}^{ * }\rho  =  - 1 \) . By (12.3.1),

\[
{s}^{ * }\Phi  =  - \left( {{s}^{ * }\rho }\right) {s}^{ * }{\pi }^{ * }e = e.
\]

Thus,

Proposition 12.4. The pullback of the Thom class of an oriented rank \( n \) vector bundle via the zero section to the base manifold is the Euler class.

REMARK 12.4.1. From the formula for the Thom class (12.3), it is clear that by making the support of \( \rho \left( r\right) \) sufficiently close to 0, the Thom class \( \Phi \) can be made to have support arbitrarily close to the zero section of the vector bundle.

REMARK 12.4.2. In fact, in Proposition 12.4 any section will pull the Thom class back to the Euler class. Let \( s \) be a section of the oriented vector bundle \( E \) and \( {s}^{ * } : {H}_{cv}^{ * }\left( E\right)  \rightarrow  {H}^{ * }\left( M\right) \) the induced map in cohomology. Note that \( {s}^{ * } \) can be written as the composition of the natural maps \( i : {H}_{cv}^{ * }\left( E\right)  \rightarrow  {H}^{ * }\left( E\right) \) and \( {\bar{s}}^{ * } : {H}^{ * }\left( E\right)  \rightarrow  {H}^{ * }\left( M\right) \) . As a map from \( M \) into \( E \) , the section \( s \) is homotopic to the zero section \( {s}_{0} \) . By the homotopy axiom for de Rham cohomology (Cor. 4.1.2), \( {\bar{s}}^{ * } = {\bar{s}}_{0}^{ * } \) . Hence, \( {s}^{ * } = {s}_{0}^{ * } \) .

Using the description of the Euler class as the pullback of the Thom class, it is easy to prove the Whitney product formula.

Theorem 12.5 (Whitney Product Formula for the Euler Class). If \( E \) and \( F \) are two oriented vector bundles, then \( e\left( {E \oplus  F}\right)  = e\left( E\right) e\left( F\right) \) .

Proof. By Proposition 6.19, the Thom class of \( E \oplus  F \) is

\[
\Phi \left( {E \oplus  F}\right)  = {\pi }_{1} * \Phi \left( E\right)  \land  {\pi }_{2}^{ * }\Phi \left( F\right)
\]

where \( {\pi }_{1} \) and \( {\pi }_{2} \) are the projections of \( E \oplus  F \) onto \( E \) and \( F \) respectively. Let \( s \) be the zero section of \( E \oplus  F \) . Then \( {\pi }_{1} \circ  s \) and \( {\pi }_{2} \circ  s \) are the zero sections of \( E \) and \( F \) . By Proposition 12.4,

\[
e\left( {E \oplus  F}\right)  = {s}^{ * }\Phi \left( {E \oplus  F}\right)  = {s}^{ * }{\pi }_{1}^{ * }\left( E\right)  \land  {s}^{ * }{\pi }_{2}^{ * }\Phi \left( F\right)  = e\left( E\right) e\left( F\right) .
\]

Exercise 12.6. Let \( \pi  : E \rightarrow  M \) be an oriented vector bundle.

(a) Show that \( {\pi }^{ * }e = \Phi \) as cohomology classes in \( {H}^{ * }\left( E\right) \) , but not in \( {H}_{cv}^{ * }\left( E\right) \) .

(b) Prove that \( \Phi  \land  \Phi  = \Phi  \land  {\pi }^{ * }e \) in \( {H}_{cv}^{ * }\left( E\right) \) .

Euler Class and the Zero Locus of a Section

Let \( \pi  : E \rightarrow  M \) be a vector bundle and \( {S}_{0} \) the image of the zero section in \( E \) . A section \( s \) of \( E \) is transversal if its image \( S = s\left( M\right) \) intersects \( {S}_{0} \) transversally. The purpose of this section is to derive an interpretation of the Euler class of an oriented vector bundle as the Poincaré dual of the zero locus of a transversal section. This is an analogue of Theorem 11.17, but it differs from Theorem 11.17 in two ways: (1) there is no hypothesis on the rank of \( E \) ; (2) the section is now assumed to be transversal.

Proposition 12.7. Let \( \pi  : E \rightarrow  M \) be any vector bundle and \( Z \) the zero locus of a transversal section. Then \( \mathbf{Z} \) is a submanifold of \( M \) and its normal bundle in \( M \) is \( {N}_{Z/M} \simeq  {\left. E\right| }_{Z} \) .

![bo_d7b6f8alb0pc73dd9avg_144_589_302_474_469_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_144_589_302_474_469_0.jpg)

Figure 12.2

Proof. Write \( S = s\left( M\right) \) for the image of the section \( s \) (see Figure 12.2). Because \( S \) intersects \( {S}_{0} \) transversally, \( S \cap  {S}_{0} \) is a submanifold of \( S \) by the transversality theorem (Guillemin and Pollack [1, p. 28]). Under the diffeomorphism \( s : M \rightarrow  S, Z \) is mapped homeomorphically to \( S \cap  {S}_{0} \) . So \( Z \) can be made into a submanifold of \( M \) .

To compute the normal bundle of \( Z \) , we first note that because \( E \) is locally trivial, its tangent bundle on \( {S}_{0} \) has the following canonical decomposition

\[
{\left. {T}_{E}\right| }_{{s}_{0}} = {\left. E\right| }_{{s}_{0}} \oplus  {T}_{{s}_{0}}.
\]

By the transversality of \( S \cap  {S}_{0} \) ,

\[
{T}_{S} + {T}_{{S}_{0}} = {T}_{E} = E \oplus  {T}_{{S}_{0}}\text{ on }S \cap  {S}_{0}.
\]

Hence the projection \( {T}_{S} \rightarrow  E \) over \( S \cap  {S}_{0} \) is surjective with kernel \( {T}_{S} \cap  {T}_{{S}_{0}} \) . Again by the transversality of \( S \cap  {S}_{0},{T}_{S} \cap  {T}_{{S}_{0}} = {T}_{S \cap  {S}_{0}} \) . So we have an exact sequence over \( Z \simeq  S \cap  {S}_{0} \) :

\[
{\left. 0 \rightarrow  {T}_{Z} \rightarrow  {T}_{S}\right| }_{Z} \rightarrow  {\left. E\right| }_{Z} \rightarrow  0.
\]

Hence \( {N}_{Z/M} \simeq  {\left. E\right| }_{Z} \) .

In the proposition above, if \( E \) and \( M \) are both oriented, then the zero locus \( Z \) of a transversal section is naturally an oriented manifold, oriented in such a way that

\[
{\left. E\right| }_{Z} \oplus  {T}_{Z} = {\left. {T}_{M}\right| }_{Z}
\]

has the direct sum orientation.

Proposition 12.8. Let \( \pi  : E \rightarrow  M \) be an oriented vector bundle over an oriented manifold M. Then the Euler class \( e\left( E\right) \) is Poincaré dual to the zero locus of a transversal section.

![bo_d7b6f8alb0pc73dd9avg_145_284_295_1056_395_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_145_284_295_1056_395_0.jpg)

Figure 12.3

Proof. We will identify \( M \) with the image \( {S}_{0} \) of the zero section. If \( S \) is the image in \( E \) of the transversal section \( s : M \rightarrow  E \) , then the zero locus of \( s \) is \( Z = S \cap  {S}_{0}.Z \) is a closed oriented submanifold of \( M \) and by Proposition 12.7, its normal bundle in \( M \) is \( {N}_{Z/M} = {\left. E\right| }_{Z} \) . Since \( S \) is diffeomorphic to \( M \) , the normal bundle \( {N}_{Z/S} \) of \( Z \) in \( S \) is also \( {\left. E\right| }_{Z} \) . The normal bundles \( {N}_{Z/M} \) and \( {N}_{Z/S} \) will be identified with the tubular neighborhoods of \( Z \) in \( M \) and in \( S \) respectively, as in Figure 12.3.

Choose the Thom class \( \Phi \) of \( E \) to have support so close to the zero section (Remark 12.4.1) that \( \Phi \) restricted to the tubular neighborhood \( {N}_{Z/S} \) in \( S \) has compact support in the vertical direction. In Figure 12.3 the support of \( \Phi \) is in the shaded region. We will now show that \( {s}^{ * }\Phi \) is the Thom class of the tubular neighborhood \( {N}_{Z/M} \) in \( M \) .

Let \( {E}_{z},{S}_{z} \) , and \( {M}_{z} \) be the fibers of \( {\left. E\right| }_{Z} \simeq  {N}_{Z/S} \simeq  {N}_{Z/M} \) respectively above the point \( z \) in \( Z \) . Because \( \Phi \) has compact support in \( {S}_{z},{s}^{ * }\Phi \) has compact support in \( {M}_{z} \) . Furthermore,

\( {\int }_{{M}_{z}}{s}^{ * }\Phi  = {\int }_{{S}_{z}}\Phi \) by the invariance of the integral under the \( = {\int }_{{E}_{z}}\Phi \) because \( {E}_{z} \) is homotopic to \( {S}_{z} \) modulo the region \( = 1 \) by the definition of the Thom class.

So \( {s}^{ * }\Phi \) is the Thom class of \( {N}_{Z/M} \) . By Proposition 12.4, \( {s}^{ * }\Phi  = e\left( E\right) \) . Since by (6.24) the Thom class of \( {N}_{Z/M} \) is Poincaré dual to \( Z \) in \( M \) , the Euler class \( e\left( E\right) \) is Poincaré dual to \( Z \) in \( M \) .

## A Tic-Tac-Toe Lemma

In this section we will prove the technical lemma (Proposition 12.1) that if \( {H}_{\delta }{H}_{d} \) of a double complex \( K \) has entries in only one row, then \( {H}_{\delta }{H}_{d} \) is isomorphic to the total cohomology \( {H}_{D}\left( K\right) \) . With this tic-tac-toe lemma we will re-examine the Mayer-Vietoris principle of Section 8. Proof of proposition 12.1.

![bo_d7b6f8alb0pc73dd9avg_146_613_363_409_265_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_146_613_363_409_265_0.jpg)

We first define a map \( h : {H}_{\delta }{H}_{d} \rightarrow  {H}_{D} \) . Recall that \( D = {D}^{\prime } + {D}^{\prime \prime } = \delta  + \; {\left( -1\right) }^{p}d \) . An element \( \left\lbrack  \phi \right\rbrack \) in \( {H}_{\delta }^{p, q}{H}_{d} \) may be represented by a \( D \) -cochain \( \phi \) of degree \( \left( {p, q}\right) \) such that

\[
{D}^{\prime \prime }\phi  = 0
\]

\[
{\delta \phi } =  - {D}^{\prime \prime }{\phi }_{1}\text{ for some }{\phi }_{1}.
\]

This is summarized by the diagram

\( \begin{matrix} 0 \\  {D}^{\prime \prime } \uparrow   \end{matrix} \)

\[
\phi \overset{\delta }{ \rightarrow  }{\delta \phi } + {D}^{\prime \prime }{\phi }_{1} = 0
\]

\[
\uparrow  {D}^{\prime \prime }
\]

\[
{\phi }_{1}
\]

Since \( {H}_{\delta }^{p + 2, q - 1}{H}_{d} = 0,\delta {\phi }_{1} =  - {D}^{\prime \prime }{\phi }_{2} \) for some \( {\phi }_{2} \) . Continuing in this manner, we see that \( \phi \) can be extended downward to a \( D \) -cocycle \( \phi  + \; {\phi }_{1} + \cdots  + {\phi }_{n} \) . The map \( h \) is defined by sending \( \left\lbrack  \phi \right\rbrack \) to \( \left\lbrack  {\phi  + {\phi }_{1} + \cdots  + {\phi }_{n}}\right\rbrack \) .

Next we define the inverse map \( g : {H}_{D} \rightarrow  {H}_{\delta }{H}_{d} \) . Let \( \omega \) be a cocycle in \( {H}_{D} \) . As the image of \( \omega \) we cannot simply take the component of \( \omega \) in the nonzero row because \( d \) of it may not be zero. Suppose \( \omega  = a + b + c + \cdots \) as shown.

![bo_d7b6f8alb0pc73dd9avg_146_676_1582_323_399_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_146_676_1582_323_399_0.jpg)

We will move \( \omega \) in its \( D \) -cohomology class so that it has nothing above the nonzero row. Since \( {da} = 0 \) and \( {\delta a} =  - {D}^{\prime \prime }b, a \) represents a cocycle in \( {H}_{\delta }{H}_{d} \) . But \( {H}_{\delta }{H}_{d} = 0 \) at the position of \( a \) , so \( a \) is 0 in \( {H}_{\delta }{H}_{d} \) ; this implies that \( a = {D}^{\prime \prime }{a}_{1} \) for some \( {a}_{1} \) . Then \( \omega  - D{a}_{1} \) has no components in the first column. Thus we may assume \( \omega  = b + c + \cdots \) . Again \( b \) is 0 in \( {H}_{\delta }{H}_{d} \) , so that \( b = \delta {b}_{1} + {D}^{\prime \prime }{b}_{2} \) , where \( {D}^{\prime \prime }{b}_{1} = 0 \) . Then \( \omega  - D\left( {{b}_{1} + {b}_{2}}\right)  = \left( {c - \delta {b}_{2}}\right) \) + ... starts at the nonzero row.

\[
\text{ 0 }
\]

\[
\text{ ↑ }
\]

\[
{b}_{1} \rightarrow  b
\]

\[
\text{ ↑ }
\]

\[
{b}_{2} \rightarrow  c
\]

Thus given \( \left\lbrack  \omega \right\rbrack   \in  {H}_{D} \) , we may pick \( \omega \) to have no components above the nonzero row of \( {H}_{\delta }{H}_{d} \) , say \( \omega  = c + \cdots \) . Then \( {dc} = 0 \) and the map \( g : {H}_{D} \rightarrow \; {H}_{\delta }{H}_{d} \) is defined by sending \( \left\lbrack  \omega \right\rbrack \) to \( \left\lbrack  c\right\rbrack \) .

Provided they are well-defined, \( h \) and \( g \) are clearly inverse to each other.

Exercise 12.9. Show that \( h \) and \( g \) are well-defined.

Using Proposition 12.1 we can give more succinct proofs of the main results of Section 8. Let \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) be an open cover of the manifold \( M \) and \( {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)  = \Pi {\Omega }^{q}\left( {U}_{{\alpha }_{0}\cdots {\alpha }_{p}}\right) \) . By the exactness of the Mayer-Vietoris sequence, \( {H}_{\delta } \) of the Čech-de Rham complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) is

![bo_d7b6f8alb0pc73dd9avg_147_560_1283_540_382_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_147_560_1283_540_382_0.jpg)

so that \( {H}_{d}{H}_{\delta } \) is

![bo_d7b6f8alb0pc73dd9avg_147_561_1751_570_387_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_147_561_1751_570_387_0.jpg)

Since \( {H}_{d}{H}_{\delta } \) has only one nonzero column, we conclude from Proposition 12.1 that

\[
{H}_{D}^{ * }\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   \simeq  {H}_{DR}^{ * }\left( M\right)
\]

for any cover \( \mathfrak{U} \) . This is the generalized Mayer-Vietoris principle (Proposition 8.8).

Now if \( \mathfrak{U} \) is a good cover, \( {H}_{d} \) of the Čech-de Rham complex is

![bo_d7b6f8alb0pc73dd9avg_148_447_616_671_401_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_148_447_616_671_401_0.jpg)

and \( {H}_{\delta }{H}_{d} \) is

![bo_d7b6f8alb0pc73dd9avg_148_455_1077_667_404_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_148_455_1077_667_404_0.jpg)

Again because \( {H}_{\delta }{H}_{d} \) has only one nonzero row,

\[
{H}_{D}^{ * }\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   \simeq  {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) .
\]

This gives the isomorphism between de Rham cohomology and the Čech cohomology of a good cover with coefficients in the constant presheaf \( \mathbb{R} \) .

Exercise 12.10. Let \( \mathbb{C}{P}^{n} \) have homogeneous coordinates \( {z}_{0},\ldots ,{z}_{n} \) . Define \( {U}_{i} = \left\{  {{z}_{i} \neq  0}\right\} \) . Then \( \mathfrak{U} = \left\{  {{U}_{0},\ldots ,{U}_{n}}\right\} \) is an open cover of \( \mathbb{C}{P}^{n} \) , although not a good cover. Compute \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) from the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) . Find elements in \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) which represent the generators of \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) .

Exercise 12.11. Apply the Thom isomorphism (12.2) to compute the cohomology with compact support of the open Möbius strip (cf. Exercise 4.8).

## Poincaré Duality

In the same spirit as above, we now give a version of Poincaré duality, in terms of the Čech-de Rham complex, for a not necessarily orientable mani-

fold. Let \( M \) be a manifold of dimension \( n \) and \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) any open cover of \( M \) . Define the coboundary operator

\[
\delta  :  \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow   \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right)
\]

by the formula

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

where on the right-hand side we mean the extension by zero of \( {\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \) to a form on \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) . To ensure that each component of \( {\delta \omega } \) has compact support, the groups here are direct sums rather than direct products, so that \( \omega  \in  \bigoplus \Omega \left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) by definition has only a finite number of nonzero components.

Proposition 12.12 (Generalized Mayer-Vietoris Sequence for Compact Supports). Suppose the open cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) of the manifold \( M \) satisfies the local finite condition:

\[
\text{ each open set }{U}_{\alpha }\text{ intersects only finitely many }{U}_{\beta }\text{ ’s. }
\]

Then the sequence

\[
0 \leftarrow  {\Omega }_{\mathrm{c}}^{ * }\left( M\right) \overset{\text{ sum }}{ \leftarrow  } \oplus  {\Omega }_{\mathrm{c}}^{ * }\left( {U}_{{\alpha }_{0}}\right)  \leftarrow   \oplus  {\Omega }_{\mathrm{c}}^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right)
\]

\[
\leftarrow  \cdots  \leftarrow   \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \leftarrow  \cdots
\]

is exact.

Proof. We first show \( {\delta }^{2} = 0 \) . Let \( \omega \) be in \( \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) . Then

\[
{\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 2}} = \mathop{\sum }\limits_{\alpha }{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 2}} = \mathop{\sum }\limits_{\alpha }\mathop{\sum }\limits_{\beta }{\omega }_{{\beta \alpha }{\alpha }_{0}\ldots {\alpha }_{p - 2}}
\]

\[
= 0\text{ , since }{\omega }_{{\alpha \beta }\ldots } =  - {\omega }_{{\beta \alpha }\ldots }\text{ . }
\]

Now suppose \( {\delta \omega } = 0 \) . We will show that \( \omega \) is a \( \delta \) -coboundary. Let \( \left\{  {\rho }_{\alpha }\right\} \) be a partition of unity subordinate to the cover \( \mathfrak{U} \) . Define

\[
{\tau }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\rho }_{{\alpha }_{i}}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}}.
\]

Note that \( {\tau }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} \) has compact support. Moreover, there are only finitely many \( \left( {\beta ,{\alpha }_{0},\ldots ,{\alpha }_{p}}\right) \) for which \( {\rho }_{\beta }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \neq  0 \) , since \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \neq  0 \) for finitely many \( \left( {{\alpha }_{0},\ldots ,{\alpha }_{p}}\right) \) and by (*) each \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \subset  {U}_{{\alpha }_{0}} \) intersects only finitely many \( {U}_{\beta } \) . Therefore, \( \tau \) has finitely many nonzero components, and \( \tau  \in  \bigoplus {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}}\right) \) . Then

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \mathop{\sum }\limits_{\alpha }{\tau }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}}
\]

\[
= \mathop{\sum }\limits_{\alpha }\left( {{\rho }_{\alpha }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{\rho }_{{\alpha }_{i}}{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}}\right)
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{\rho }_{{\alpha }_{i}}{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}}
\]

Exercise 12.12.1. Show that the definition of \( \tau \) in the proof above provides a homotopy operator for the compact Mayer-Vietoris sequence (12.12). More precisely, if \( \omega \) is in \( \oplus  {\Omega }_{c}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) and

\[
{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\rho }_{{\alpha }_{i}}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}},
\]

then

\[
{\delta K} + {K\delta } = 1.
\]

Consider the double complex \( {C}^{p}\left( {\mathfrak{U},{\Omega }_{c}^{q}}\right) \) , where \( \mathfrak{U} \) satisfies the local finite condition (*):

![bo_d7b6f8alb0pc73dd9avg_150_398_853_856_314_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_150_398_853_856_314_0.jpg)

In this double complex the \( \delta \) -operator goes in the wrong direction, so we define a new complex

\[
{K}^{-p, q} = {C}^{p}\left( {\mathfrak{U},{\Omega }_{c}^{q}}\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_150_287_1386_1047_278_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_150_287_1386_1047_278_0.jpg)

By the exactness of the rows, \( {H}_{\delta }\left( K\right) \) is

![bo_d7b6f8alb0pc73dd9avg_150_394_1804_874_342_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_150_394_1804_874_342_0.jpg)

Since \( {H}_{d}{H}_{\delta } \) has only one nonzero column, it follows from Proposition 12.1 that

(12.13)

\[
{H}_{D}\left( K\right)  = {H}_{d}{H}_{\delta }\left( K\right)  = {H}_{c}\left( M\right) .
\]

On the other hand, if \( \mathfrak{U} \) is a good cover, then \( {H}_{d}\left( K\right) \) is

\[
{H}_{d}^{-p, q}\left( K\right)  = {C}^{p}\left( {\mathfrak{U},{\mathcal{H}}_{c}^{q}}\right)
\]

![bo_d7b6f8alb0pc73dd9avg_151_286_514_1083_250_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_151_286_514_1083_250_0.jpg)

where \( {\mathcal{H}}_{c}^{q} \) is the covariant functor which associates to every open set \( U \) the compact cohomology \( {H}_{c}^{q}\left( U\right) \) and to every inclusion \( i \) , the extension by zero, \( {i}_{ * } \) ; moreover,

\[
{H}_{d}^{-p, q}\left( K\right)  = 0\;\text{ for }q \neq  n.
\]

Again by Proposition 12.1,

(12.14)

\[
{H}_{D}^{ * }\left( K\right)  = {H}_{\delta }^{* - n, n}{H}_{d} = {H}_{n -  * }\left( {\mathfrak{U},{\mathcal{H}}_{c}^{n}}\right) .
\]

Here \( {H}_{n -  * }\left( {\mathfrak{U},{\mathcal{H}}_{c}^{n}}\right) \) is the \( \left( {n -  * }\right) \) -th Čech homology of the cover \( \mathfrak{U} \) with coefficients in the covariant functor \( {\mathcal{H}}_{c}^{n} \) (cf. Remark 10.3). Comparing (12.13) and (12.14) gives

Theorem 12.15 (Poincaré Duality). Let \( M \) be a manifold of dimension \( n \) and \( \mathfrak{U} \) any good cover of \( M \) satisfying the local finite condition (*) of Proposition 12.12. Here \( M \) is not assumed to be orientable. Then

\[
{H}_{c}^{ * }\left( M\right)  \simeq  {H}_{n -  * }\left( {\mathfrak{U},{\mathcal{H}}_{c}^{n}}\right)
\]

where \( {\mathcal{H}}_{c}^{n} \) is the covariant functor \( {\mathcal{H}}_{c}^{n}\left( U\right)  = {H}_{c}^{n}\left( U\right) \) .

Exercise 12.16. By applying Poincaré duality (12.15), compute the compact cohomology of the open Möbius strip (cf. Exercise 4.8).
