## §7 The Nonorientable Case

Since the integral of a differential form on \( {\mathbb{R}}^{n} \) is not invariant under the whole group of diffeomorphisms of \( {\mathbb{R}}^{n} \) , but only under the subgroup of orientation-preserving diffeomorphisms, a differential form cannot be integrated over a nonorientable manifold. However, by modifying a differential form we obtain something called a density, which can be integrated over any manifold, orientable or not. This will give us a version of Poincaré duality for nonorientable manifolds and of the Thom isomorphism for nonorientable vector bundles.

## The Twisted de Rham Complex

Let \( M \) be a manifold and \( E \) a vector space. The space of differential forms on \( M \) with values in \( E \) , denoted \( {\Omega }^{ * }\left( {M, E}\right) \) , is by definition the vector space spanned by \( \omega  \otimes  v \) , where \( \omega  \in  {\Omega }^{ * }\left( M\right) , v \in  E \) , and the tensor product is over \( \mathbb{R} \) . This space can be made naturally into a differential complex if we let the differential be

\[
d\left( {\omega  \otimes  v}\right)  = \left( {d\omega }\right)  \otimes  v
\]

So the cohomology \( {H}^{ * }\left( {M, E}\right) \) is defined. Indeed, if \( E \) is a vector space of dimension \( n \) , then \( {H}^{ * }\left( {M, E}\right) \) is isomorphic to \( n \) copies of \( {H}_{DR}^{ * }\left( M\right) \) .

Now let \( E \) be a vector bundle. We define the space of \( E \) -valued q-forms, \( {\Omega }^{q}\left( {M, E}\right) \) , to be the global sections of the vector bundle \( \left( {{\Lambda }^{q}{T}_{M}^{ * }}\right)  \otimes  E \) . Locally such a \( q \) -form can be written as \( \sum {\omega }_{i} \otimes  {e}_{i} \) , where \( {\omega }_{i} \) are \( q \) -forms and \( {e}_{i} \) are sections of \( E \) over some open set \( U \) in \( M \) , and the tensor product is over the \( {C}^{\infty } \) functions on \( U \) . For these vector-valued differential forms, no natural extension of the de Rham complex is possible, unless one is first given a way of differentiating the sections of \( E \) .

Suppose the vector bundle \( E \) has a trivialization \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) relative to which the transition functions are locally constant. Such a vector bundle is called a flat vector bundle and the trivialization a locally constant trivialization. For a flat vector bundle \( E \) a differential operator on \( {\Omega }^{ * }\left( {M, E}\right) \) may be defined as follows. Let \( {e}_{\alpha }^{1},\ldots ,{e}_{\alpha }^{n} \) be the sections of \( E \) over \( {U}_{\alpha } \) corresponding to the standard basis under the trivialization \( {\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \rightarrow \; {U}_{\alpha } \times  {\mathbb{R}}^{n} \) . We declare these to be the standard locally constant sections, i.e., \( d{e}_{\alpha }^{i} = 0 \) . Over \( {U}_{\alpha } \) an \( E \) -valued \( q \) -form \( s \) in \( {\Omega }^{q}\left( {M, E}\right) \) can be written as \( \sum {\omega }_{i} \otimes  {e}_{\alpha }^{i} \) , where the \( {\omega }_{i} \) are \( q \) -forms over \( {U}_{\alpha } \) . We define the exterior derivative \( {ds} \) over \( {U}_{\alpha } \) by linearity and the Leibnitz rule:

\[
d\left( {\sum {\omega }_{i} \otimes  {e}_{\alpha }^{i}}\right)  = \sum \left( {d{\omega }_{i}}\right)  \otimes  {e}_{\alpha }^{i}.
\]

It is easy to show that, because the transition functions of \( E \) relative to \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) are locally constant, this definition of exterior differentiation is independent of the open sets \( {U}_{\alpha } \) . More precisely, on the overlap \( {U}_{\alpha } \cap  {U}_{\beta } \) , if

\[
s = \sum {\omega }_{i} \otimes  {e}_{\alpha }^{i} = \sum {\tau }_{j} \otimes  {e}_{\beta }^{j}
\]

and \( {e}_{\alpha }^{i} = \sum {c}_{ij}{e}_{\beta }^{j} \) , where the \( {c}_{ij} \) are locally constant functions, then

\[
{\tau }_{j} = \sum {c}_{ij}{\omega }_{i}
\]

and

\[
d\left( {\sum {\tau }_{j} \otimes  {e}_{\beta }^{j}}\right)  = \sum \left( {d{\tau }_{j}}\right)  \otimes  {e}_{\beta }^{j}
\]

\[
= \sum \left( {{c}_{ij}d{\omega }_{i}}\right)  \otimes  {e}_{\beta }^{j}
\]

\[
= \sum \left( {d{\omega }_{i}}\right)  \otimes  {e}_{\alpha }^{i}
\]

\[
= d\left( {\sum {\omega }_{i} \otimes  {e}_{\alpha }^{i}}\right) .
\]

Hence \( {ds} \) is globally defined and is an element of \( {\Omega }^{q + 1}\left( {M, E}\right) \) . Because \( {d}^{2} \) is clearly zero, \( {\Omega }^{ * }\left( {M, E}\right) \) is a differential complex and the cohomology \( {H}^{ * }\left( {M, E}\right) \) makes sense. As defined, \( d \) very definitely depends on the trivialization \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) , for it is through the trivialization that the locally constant sections are given. Hence, \( d,{\Omega }^{ * }\left( {M, E}\right) \) , and \( {H}^{ * }\left( {M, E}\right) \) are more properly denoted as \( {d}_{\phi },{\Omega }_{\phi }^{ * }\left( {M, E}\right) \) , and \( {H}_{\phi }^{ * }\left( {M, E}\right) \) .

EXAMPLE 7.1 (Two trivializations of a vector bundle \( E \) which give rise to distinct cohomology groups \( {H}^{ * }\left( {M, E}\right) ) \) .

Let \( M \) be the circle \( {S}^{1} \) and \( E \) the trivial line bundle \( {S}^{1} \times  {\mathbb{R}}^{1} \) over the circle. If \( E \) is given the usual constant trivialization \( \phi \) :

\[
\phi \left( {x, r}\right)  = r\text{ for }x \in  {S}^{1}\;\text{ and }\;r \in  {\mathbb{R}}^{1},
\]

then the cohomology \( {H}_{\phi }^{0}\left( {{S}^{1}, E}\right)  = \mathbb{R} \) .

However, we can define another locally constant trivialization \( \psi \) for \( E \) as follows. Cover \( {S}^{1} \) with two open sets \( U \) and \( V \) as indicated in Figure 7.1.

![bo_d7b6f8alb0pc73dd9avg_91_302_673_1014_836_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_91_302_673_1014_836_0.jpg)

Figure 7.1

Let \( \rho \left( x\right) \) be the real-valued function on \( V \) whose graph is as in Figure 7.2. The trivialization \( \psi \) is given by

\[
\psi \left( {x, r}\right)  = \left\{  \begin{array}{ll} r & \text{ for }x \in  U, r \in  {\mathbb{R}}^{1}, \\  \rho \left( x\right) r & \text{ for }x \in  V, r \in  {\mathbb{R}}^{1}. \end{array}\right.
\]

The standard locally constant sections over \( U \) and \( V \) are \( {e}_{U}\left( x\right)  = \left( {x,1}\right) \) and \( {e}_{V}\left( x\right)  = \left( {x,1/\rho \left( x\right) }\right) \) respectively. Relative to the trivialization \( \psi \) , the cohomology \( {H}_{\psi }^{0}\left( {{S}^{1}, E}\right)  = 0 \) , since the locally constant sections over \( U \) and \( V \) do not piece together to form a global section (except for the zero section).

It is natural to ask: to what extent is the twisted cohomology \( {H}_{\phi }^{ * }\left( {M, E}\right) \) independent of the trivialization \( \phi \) for \( E \) ?

![bo_d7b6f8alb0pc73dd9avg_92_343_272_970_485_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_92_343_272_970_485_0.jpg)

Figure 7.2

Proposition 7.2. The twisted cohomology is invariant under the refinement of open covers. More precisely, let \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  I} \) be a locally constant trivialization for \( E \) . Suppose \( {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) is a refinement of \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) and the coordinates maps \( {\psi }_{\beta } \) on \( {V}_{\beta } \subset  {U}_{\alpha } \) are the restrictions of \( {\phi }_{\alpha } \) . Then the two twisted complexes \( {\Omega }_{\phi }^{ * }\left( {M, E}\right) \) and \( {\Omega }_{\psi }^{ * }\left( {M, E}\right) \) are identical and so are their cohomology:

\[
{H}_{\phi }^{ * }\left( {M, E}\right)  = {H}_{\psi }^{ * }\left( {M, E}\right) .
\]

Proof. Since the definition of the differential operator on a twisted complex is local, and \( \phi \) and \( \psi \) agree on the open cover \( \left\{  {V}_{\beta }\right\} \) , we have \( {d}_{\phi } = {d}_{\psi } \) . Therefore the two complexes \( {\Omega }_{\phi }^{ * }\left( {M, E}\right) \) and \( {\Omega }_{\psi }^{ * }\left( {M, E}\right) \) are identical.

Still assuming \( E \) to be a flat vector bundle, suppose \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( \left\{  \left( {{U}_{\alpha },{\psi }_{\alpha }}\right) \right\} \) are two locally constant trivializations which differ by a locally constant comparison 0-cochain, i.e., if \( {e}_{\alpha }^{i} \) and \( {f}_{\alpha }^{j} \) are the standard locally constant sections over \( {U}_{\alpha } \) relative to the trivializations \( \phi \) and \( \psi \) respectively, then

\[
{e}_{\alpha }^{i} = \mathop{\sum }\limits_{j}{a}_{\alpha }^{ij}{f}_{\alpha }^{j}
\]

for some locally constant function

\[
{a}_{\alpha } = \left( {a}_{\alpha }^{ij}\right)  : {U}_{\alpha } \rightarrow  \mathrm{{GL}}\left( {n,\mathbb{R}}\right) .
\]

In this case there is an obvious isomorphism

\[
F : {\Omega }_{\phi }^{q}\left( {M, E}\right)  \rightarrow  {\Omega }_{\psi }^{q}\left( {M, E}\right)
\]

given by

\[
{e}_{\alpha }^{i} \mapsto  \mathop{\sum }\limits_{j}{a}_{\alpha }^{ij}{f}_{\alpha }^{j}
\]

It is easily checked that the diagram commutes. Hence \( F \) induces an isomorphism in cohomology. Next, suppose we are given two locally constant trivializations \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( \left\{  \left( {{V}_{\beta },{\psi }_{\beta }}\right) \right\} \) for \( E \) , with possibly different open covers. By taking a common refinement, which does not affect the twisted cohomology (Proposition 7.2), we may assume that the two open covers are identical. The discussion above therefore proves the following.

\[
{\Omega }_{\psi }^{ * }\left( {M, E}\right) \xrightarrow[F]{{d}_{\phi }}{\Omega }_{\phi }^{* + 1}\left( {M, E}\right)
\]

\[
{\Omega }_{\psi }^{ * }\left( {M, E}\right) \xrightarrow[{d}_{\psi }]{}{\Omega }_{\psi }^{* + 1}\left( {M, E}\right)
\]

Proposition 7.3. (a) Let \( E \) be a flat vector bundle over \( M \) , and \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( \left\{  \left( {{V}_{\beta },{\psi }_{\beta }}\right) \right\} \) two locally constant trivializations for \( E \) . Suppose after a common refinement the two trivializations differ by a locally constant comparison 0- cochain. Then there are isomorphisms

\[
{\Omega }_{\phi }^{ * }\left( {M, E}\right)  \simeq  {\Omega }_{\psi }^{ * }\left( {M, E}\right)
\]

and

\[
{H}_{\phi }^{ * }\left( {M, E}\right)  \simeq  {H}_{\psi }^{ * }\left( {M, E}\right) .
\]

This proposition may also be stated in terms of the transition functions for \( E \) .

Proposition 7.3. (b) Let \( E \) be a flat vector bundle of rank \( n \) and \( \left\{  {g}_{\alpha \beta }\right\} \) and \( \left\{  {h}_{\alpha \beta }\right\} \) the transition functions for \( E \) relative to two locally constant trivializations \( \phi \) and \( \psi \) with the same open cover. If there exist locally constant functions

\[
{\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  \mathrm{{GL}}\left( {n,\mathbb{R}}\right)
\]

such that

\[
{g}_{\alpha \beta } = {\lambda }_{\alpha }{h}_{\alpha \beta }{\lambda }_{\beta }^{-1},
\]

then there are isomorphisms as in 7.3(a).

Proposition 7.4. If \( E \) is a trivial rank \( n \) vector bundle over a manifold \( M \) , with \( \phi \) a trivialization of \( E \) given by \( n \) global sections, then

\[
{H}_{\phi }^{ * }\left( {M, E}\right)  = {H}^{ * }\left( {M,{\mathbb{R}}^{n}}\right)  = {\bigoplus }_{i = 1}^{n}{H}^{ * }\left( M\right)
\]

Proof. Let \( {e}_{1},\ldots ,{e}_{n} \) be the \( n \) global sections corresponding to the standard basis of \( {\mathbb{R}}^{n} \) . Then every element in \( {\Omega }^{ * }\left( {M, E}\right) \) can be written uniquely as \( \sum {\omega }_{i} \otimes  {e}_{i} \) , where \( {\omega }_{i} \in  {\Omega }^{ * }\left( M\right) \) and the tensor product is over the \( {C}^{\infty } \) functions on \( M \) . The map

\[
\sum {\omega }_{i} \otimes  {e}_{i} \mapsto  \left( {{\omega }_{1},\ldots ,{\omega }_{n}}\right)
\]

gives an isomorphism of the complexes \( {\Omega }_{\phi }^{ * }\left( {M, E}\right) \) and \( {\Omega }^{ * }\left( {M,{\mathbb{R}}^{n}}\right) \) .

Now let \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) be a coordinate open cover for the manifold \( M \) , with transition functions \( {g}_{\alpha \beta } = {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1} \) . Define the sign function on \( {\mathbb{R}}^{1} \) to be

\[
\operatorname{sgn}\left( x\right)  = \begin{cases}  + 1 & \text{ for }x\text{ positive } \\  0 & \text{ for }x = 0 \\   - 1 & \text{ for }x\text{ negative. } \end{cases}
\]

The orientation bundle of \( M \) is the line bundle \( L \) on \( M \) given by transition functions \( \operatorname{sgn}J\left( {g}_{\alpha \beta }\right) \) , where \( J\left( {g}_{\alpha \beta }\right) \) is the Jacobian determinant of the matrix of partial derivatives of \( {g}_{\alpha \beta } \) . It follows directly from the definition that \( M \) is orientable if and only if its orientation bundle is trivial.

Relative to the atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) for \( M \) with transition functions \( {g}_{\alpha \beta } \) , the orientation bundle is by definition the quotient

\[
\left( {{U}_{\alpha } \times  {\mathbb{R}}^{1}}\right) /\left( {x, v}\right)  \sim  \left( {x,\operatorname{sgn}J\left( {{g}_{\alpha \beta }\left( x\right) }\right) v}\right) ,
\]

where \( \left( {x, v}\right)  \in  {U}_{\alpha } \times  {\mathbb{R}}^{1} \) and \( \left( {x,\operatorname{sgn}J\left( {{g}_{\alpha \beta }\left( x\right) }\right) v}\right)  \in  {U}_{\beta } \times  {\mathbb{R}}^{1} \) . By construction there is a natural trivialization \( {\phi }^{\prime } \) on \( L \) ,

\[
{\phi }_{\alpha }^{\prime } : {\left. L\right| }_{{U}_{\alpha }} \supset  {U}_{\alpha } \times  {\mathbb{R}}^{1},
\]

which we call the trivialization induced from the atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) on \( M \) . Because sgn \( J\left( {g}_{\alpha \beta }\right) \) are locally constant functions on \( M \) , the locally constant sections of \( L \) relative to this trivialization are the equivalence classes of \( \left\{  {\left( {x, v}\right)  \mid  x \in  {U}_{\alpha }}\right\} \) for \( v \) fixed in \( {\mathbb{R}}^{1} \) .

Proposition 7.5. If \( {\phi }^{\prime } \) and \( {\psi }^{\prime } \) are two trivializations for \( L \) induced from two atlases \( \phi \) and \( \psi \) on \( M \) , then the two twisted complexes \( {\Omega }_{\phi \prime }^{ * }\left( {M, L}\right) \) and \( {\Omega }_{\psi \prime }^{ * }(M \) , L) are isomorphic and so are their cohomology \( {H}_{\phi ,\iota }^{ * }\left( {M, L}\right) \) and \( {H}_{\psi ,\iota }^{ * }\left( {M, L}\right) \) .

Proof. By going to a common refinement we may assume that the two atlases \( \phi \) and \( \psi \) have the same open cover. Thus on each \( {U}_{\alpha } \) there are two sets of coordinate functions, \( {\phi }_{\alpha } \) and \( {\psi }_{\alpha } \) (Figure 7.3.).

![bo_d7b6f8alb0pc73dd9avg_94_425_1543_794_542_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_94_425_1543_794_542_0.jpg)

Figure 7.3

The transition functions \( {g}_{\alpha \beta } \) and \( {h}_{\alpha \beta } \) for the two atlases \( \phi \) and \( \psi \) respectively are related by

\[
{g}_{\alpha \beta } = {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1}
\]

\[
= {\phi }_{\alpha } \circ  {\psi }_{\alpha }^{-1} \circ  {\psi }_{\alpha } \circ  {\psi }_{\beta }^{-1} \circ  {\psi }_{\beta } \circ  {\phi }_{\beta }^{-1}
\]

\[
= {\mu }_{\alpha } \circ  {h}_{\alpha \beta } \circ  {\mu }_{\beta }^{-1},
\]

where \( {\mu }_{\alpha } \mathrel{\text{ := }} {\phi }_{\alpha } \circ  {\psi }_{\alpha }^{-1} : {\psi }_{\alpha }\left( {U}_{\alpha }\right)  \rightarrow  {\phi }_{\alpha }\left( {U}_{\alpha }\right) \) . It follows that

\[
\operatorname{sgn}J\left( {g}_{\alpha \beta }\right)  = \operatorname{sgn}J\left( {\mu }_{\alpha }\right)  \cdot  \operatorname{sgn}J\left( {h}_{\alpha \beta }\right)  \cdot  \operatorname{sgn}J{\left( {\mu }_{\beta }\right) }^{-1}.
\]

Define a 0-chain \( {\lambda }_{\alpha } : {U}_{\alpha } \rightarrow  \mathrm{{GL}}\left( {1,\mathbb{R}}\right) \) by \( {\lambda }_{\alpha }\left( x\right)  = \operatorname{sgn}J\left( {\mu }_{\alpha }\right) \left( {{\psi }_{\alpha }\left( x\right) }\right) \) for \( x \in  {U}_{\alpha } \) . Since \( {\lambda }_{\alpha }\left( x\right)  =  \pm  1 \) , by Proposition 7.3(b)

\[
{\Omega }_{\phi }^{ * }\left( {M, L}\right)  \simeq  {\Omega }_{\psi }^{ * }\left( {M, L}\right) .
\]

We define the twisted de Rham complex \( {\Omega }^{ * }\left( {M, L}\right) \) and the twisted de Rham cohomology \( {H}^{ * }\left( {M, L}\right) \) to be \( {\Omega }_{\phi }^{ * }\left( {M, L}\right) \) and \( {H}_{\phi }^{ * }\left( {M, L}\right) \) for any trivialization \( {\phi }^{\prime } \) on \( L \) which is induced from \( M \) . Similarly one also has the twisted de Rham cohomology with compact support, \( {H}_{c}^{ * }\left( {M, L}\right) \) .

REMARK. If a trivialization \( \psi \) on \( L \) is not induced from \( M \) , then \( {H}_{\psi }^{ * }\left( {M, L}\right) \) may not be equal to the twisted de Rham cohomology \( {H}^{ * }\left( {M, L}\right) \) .

The following statement is an immediate consequence of Proposition 7.4 and the triviality of \( L \) on an orientable manifold.

Proposition 7.6. On an orientable manifold \( M \) the twisted de Rham cohomology \( {H}^{ * }\left( {M, L}\right) \) is the same as the ordinary de Rham cohomology.

## Integration of Densities, Poincaré Duality, and the Thom Isomorphism

Let \( M \) be a manifold of dimension \( n \) with coordinate open cover \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and transition functions \( {g}_{\alpha \beta } \) . A density on \( M \) is an element of \( {\Omega }^{n}\left( {M, L}\right) \) , or equivalently, a section of the density bundle \( \left( {{\Lambda }^{n}{T}_{M}^{ * }}\right)  \otimes  L \) . One may think of a density as a top-dimensional differential form twisted by the orientation bundle. Since the transition function for the exterior power \( {\Lambda }^{n}{T}_{M}^{ * } \) is \( 1/J\left( {g}_{\alpha \beta }\right) \) , the transition function for the density bundle is

\[
\frac{1}{J\left( {g}_{\alpha \beta }\right) } \cdot  \operatorname{sgn}J\left( {g}_{\alpha \beta }\right)  = \frac{1}{\left| J\left( {g}_{\alpha \beta }\right) \right| }.
\]

Let \( {e}_{\alpha } \) be the section of \( {\left. L\right| }_{{U}_{\alpha }} \) corresponding to 1 under the trivialization of \( L \) induced from the atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) . If \( {\phi }_{\alpha } = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) are the coordinates on \( {U}_{\alpha } \) , we define the density \( \left| {d{x}_{1}\cdots d{x}_{n}}\right| \) in \( \Gamma \left( {{U}_{\alpha },\left( {{\Lambda }^{n}{T}_{M}^{ * }}\right)  \otimes  L}\right) ) \) to be

\[
\left| {d{x}_{1}\cdots d{x}_{n}}\right|  = {e}_{\alpha }d{x}_{1}\cdots d{x}_{n}.
\]

Locally we may then write a density as \( g\left( {{x}_{1},\ldots ,{x}_{n}}\right) \left| {d{x}_{1}\cdots d{x}_{n}}\right| \) for some smooth function \( g \) .

Let \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) be a diffeomorphism of \( {\mathbb{R}}^{n} \) with coordinates \( {x}_{1},\ldots ,{x}_{n} \) and \( {y}_{1},\ldots ,{y}_{n} \) respectively. If \( \omega  = g\left| {d{y}_{1}\ldots d{y}_{n}}\right| \) is a density on \( {\mathbb{R}}^{n} \) , the pullback of \( \omega \) by \( T \) is

\[
{T}^{ * }\omega  = \left( {g \circ  T}\right) \left| {d\left( {{y}_{1} \circ  T}\right) \ldots d\left( {{y}_{n} \circ  T}\right) }\right|
\]

\[
= \left( {g \circ  T}\right) \left| {J\left( T\right) }\right| \left| {d{x}_{1}\ldots d{x}_{n}}\right| .
\]

The density \( g\left| {d{y}_{1}\ldots d{y}_{n}}\right| \) is said to have compact support on \( {\mathbb{R}}^{n} \) if \( g \) has compact support, and the integral of such a density over \( {\mathbb{R}}^{n} \) is defined to be the corresponding Riemann integral. Then

\[
{\int }_{{\mathbb{R}}^{n}}{T}^{ * }\omega  = {\int }_{{\mathbb{R}}^{n}}\left( {g \circ  T}\right) \left| {J\left( T\right) }\right| \left| {d{x}_{1}\ldots d{x}_{n}}\right|
\]

\[
= {\int }_{{\mathbb{R}}^{n}}g\left| {d{y}_{1}\ldots d{y}_{n}}\right| \text{ by the change of variable formula }
\]

\[
= {\int }_{{\mathbb{R}}^{n}}\omega
\]

Thus the integration of a density is invariant under the group of all diffeomorphisms on \( {\mathbb{R}}^{n} \) . This means we can globalize the integration of a density to a manifold. If \( \left\{  {\rho }_{\alpha }\right\} \) is a partition of unity subordinate to the open cover \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( \omega  \in  {\Omega }_{c}^{n}\left( {M, L}\right) \) , define

\[
{\int }_{M}\omega  = \mathop{\sum }\limits_{\alpha }{\int }_{{\mathbb{R}}^{n}}{\left( {\phi }_{\alpha }^{-1}\right) }^{ * }\left( {{\rho }_{\alpha }\omega }\right) .
\]

It is easy to check that this definition is independent of the choices involved.

Just as for differential forms there is a Stokes' theorem for densities. We state below only the weak version that we need.

Theorem 7.7 (Stokes' Theorem for Densities). On any manifold \( M \) of dimension \( n \) , orientable or not, if \( \omega  \in  {\Omega }_{c}^{n - 1}\left( {M, L}\right) \) , then

\[
{\int }_{M}{d\omega } = 0
\]

The proof is essentially the same as (3.5).

It follows from this Stokes' theorem that the pairings

\[
{\Omega }^{q}\left( M\right)  \otimes  {\Omega }_{c}^{n - q}\left( {M, L}\right)  \rightarrow  \mathbb{R}
\]

and

\[
{\Omega }_{c}^{q}\left( M\right)  \otimes  {\Omega }^{n - q}\left( {M, L}\right)  \rightarrow  \mathbb{R}
\]

given by

\[
\omega  \land  \tau  \mapsto  {\int }_{M}\omega  \land  \tau
\]

descend to cohomology.

Theorem 7.8 (Poincaré Duality). On a manifold \( M \) of dimension \( n \) with a finite good cover, there are nondegenerate pairings

\[
{H}^{q}\left( M\right) {\bigotimes }_{\mathbb{R}}{H}_{c}^{n - q}\left( {M, L}\right)  \rightarrow  \mathbb{R}
\]

and

\[
{H}_{c}^{q}\left( M\right) {\bigotimes }_{\mathbb{R}}{H}^{n - q}\left( {M, L}\right)  \rightarrow  \mathbb{R}
\]

Proof. By tensoring the Mayer-Vietoris sequences (2.2) and (2.7) with \( \Gamma \left( {M, L}\right) \) we obtain the corresponding Mayer-Vietoris sequences for twisted cohomology. The Mayer-Vietoris argument for Poincaré duality on an orientable manifold then carries over word for word.

Corollary 7.8.1. Let \( M \) be a connected manifold of dimension \( n \) having a finite good cover. Then

\[
{H}^{n}\left( M\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ if }M\text{ is compact orientable } \\  0 & \text{ otherwise. } \end{array}\right.
\]

Proof. By Poincaré duality, \( {H}^{n}\left( M\right)  = {H}_{c}^{0}\left( {M, L}\right) \) . Let \( \left\{  {U}_{\alpha }\right\} \) be a coordinate open cover for \( M \) . An element of \( {H}_{c}^{0}\left( {M, L}\right) \) is given by a collection of constants \( {f}_{\alpha } \) on \( {U}_{\alpha } \) satisfying

\[
{f}_{\alpha } = \left( {\operatorname{sgn}J\left( {g}_{\alpha \beta }\right) }\right) {f}_{\beta }.
\]

If \( {f}_{\alpha } = 0 \) for some \( \alpha \) , then by the connectedness of \( M \) , we have \( {f}_{\alpha } = 0 \) for all \( \alpha \) . It follows that a nonzero element of \( {H}_{c}^{0}\left( {M, L}\right) \) is nowhere vanishing. Thus, \( {H}_{c}^{0}\left( {M, L}\right)  \neq  0 \) if and only if \( M \) is compact and \( L \) has a nowhere-vanishing section, i.e., \( M \) is compact orientable. In that case,

\[
{H}_{c}^{0}\left( {M, L}\right)  = {H}_{c}^{0}\left( M\right)  = \mathbb{R}.
\]

Exercise 7.9. Let \( M \) be a manifold of dimension \( n \) . Compute the cohomology groups \( {H}_{c}^{n}\left( M\right) ,{H}^{n}\left( {M, L}\right) \) , and \( {H}_{c}^{n}\left( {M, L}\right) \) for each of the following four cases: \( M \) compact orientable, noncompact orientable, compact nonorientable, noncompact nonorientable.

Finally, we state but do not prove the Thom isomorphism theorem in all orientational generality. Let \( E \) be a rank \( n \) vector bundle over a manifold \( M \) , and let \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and \( {g}_{\alpha \beta } \) be a trivialization and transition functions for E. Neither \( E \) nor \( M \) is assumed to be orientable. The orientation bundle of \( E \) , denoted \( o\left( E\right) \) , is the line bundle over \( M \) with transition functions sgn \( J\left( {g}_{\alpha \beta }\right) \) . With this terminology, the orientation bundle of \( M \) is simply the orientation bundle of its tangent bundle \( {T}_{M} \) . It is easy to see that when \( E \) is not orientable, integration along the fiber of a form in \( {\Omega }_{cv}^{ * }\left( E\right) \) does not yield a global form on \( M \) , but an element of the twisted complex \( {\Omega }^{ * }\left( {M, o\left( E\right) }\right) \) .

Theorem 7.10 (Nonorientable Thom Isomorphism). Under the hypothesis above, integration along the fiber gives an isomorphism

\[
{\pi }_{ * } : {H}_{cv}^{* + n}\left( E\right)  \simeq  {H}^{ * }\left( {M, o\left( E\right) }\right) .
\]

Exercise 7.11. Compute the twisted de Rham cohomology \( {H}^{ * }\left( {\mathbb{R}{P}^{n}, L}\right) \) .
