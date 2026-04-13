# 20.2 The Combinatorial Case

The following will be a convenient class of objects to work with. Let \( K \) be a locally finite simplicial complex.

Definition. \( K \) is an \( n \) -dimensional rational homology manifold if for each point \( x \) of \( K \) the local homology group

\[
{\mathrm{H}}_{i}\left( {K, K - x;\mathbb{Q}}\right)
\]

is zero for \( i \neq  n \) and isomorphic to \( \mathbb{Q} \) for \( i = n \) .

This is equivalent to the requirement that the star boundary of every simplex of \( K \) has the rational homology of an \( \left( {n - 1}\right) \) -sphere. If \( K \) is a compact rational homology \( n \) -manifold, then it is easy to check that each component of \( K \) is a "simple n-circuit." (See [ES52, p. 106].) In particular, each \( \left( {n - 1}\right) \) -simplex of \( K \) is incident to precisely two \( n \) -simplexes. Such a complex \( K \) is said to be oriented if it is possible to assign an orientation to each \( n \) -simplex so that the sum of all \( n \) -simplexes forms an \( n \) -dimensional cycle. By definition, this cycle represents the fundamental homology class \( \mu  \in  {\mathrm{H}}_{n}\left( {K;\mathbb{Z}}\right) \) .

Such oriented rational homology manifolds satisfy the Ponicaré duality theorem with rational coefficients. See for example [Bor+60].

Similarly one can define the concept of an \( n \) -dimensional homology manifold-with-boundary. In this case the boundary \( \partial K \) is a homology \( \left( {n - 1}\right) \) -manifold, and the orientation determines and is determined by a relative homology class \( \mu  \in  {\mathrm{H}}_{n}\left( {K,\partial K;\mathbb{Z}}\right) . \)

We recall some standard definitions. Let \( K \) be a simplicial complex. By a (rectilinear) subdivision of \( K \) is meant a simplicial complex \( {K}^{\prime } \) together with a homeomorphism \( s : {K}^{\prime } \rightarrow  K \) which is simplexwise linear, i.e., maps each simplex of \( {K}^{\prime } \) linearly into a simplex of \( K \) . A map \( f : K \rightarrow  L \) between simplicial complexes is called piecewise linear if there exists a subdivision \( s : {K}^{\prime } \rightarrow  K \) so that the composition \( f \circ  s \) is simplexwise linear.

A map \( K \rightarrow  L \) is said to be simplicial if it is simplexwise linear and maps each vertex of \( K \) to a vertex of \( L \) . If \( K \) is compact, then given any piecewise linear map \( f : K \rightarrow  L \) is said to be simplicial if it is simplexwise linear and maps exch vertex of \( K \) to a vertex of \( L \) . If \( K \) is compact, then given any piecewise linear map \( f : K \rightarrow  L \) it can be shown that there exist subdivisions \( s : {K}^{\prime } \rightarrow  K \) and \( t : {L}^{\prime } \rightarrow  L \) so that the composition \( {t}^{-1} \circ  f \circ  s : {K}^{\prime } \rightarrow  {L}^{\prime } \) is simplicial. See for example [RS12, p. 17].

Let \( {\sum }^{r} \) denote the boundary of the standard \( \left( {r + 1}\right) \) -simplex. Our key lemma will be the following.

Lemma 20.3. Let \( {K}^{n} \) be a compact rational homology \( n \) -manifold, and let \( f : {K}^{n} \rightarrow  {\sum }^{r} \) be a piecewise linear map, with \( n - r = {4i} \) . Then for almost all \( y \in  {\sum }^{r} \) the inverse image \( {f}^{-1}\left( y\right) \) is a compact rational homology \( {4i} \) -manifold. Given orientations for \( {K}^{n} \) and \( {\sum }^{r} \) , there is an induced orientation for \( {f}^{-1}\left( y\right) \) . Furthermore the signature \( \sigma \left( {{f}^{-1}\left( y\right) }\right) \) of this oriented homology manifold is independent of \( y \) for almost all \( y \) .

Here "almost all \( y \) " can be taken to mean "except for \( y \) belonging to some lower dimensional subcomplex."

It will be convenient to introduce the abbreviated notation of \( \sigma \left( f\right) \) for this common value \( \sigma \left( {{f}^{-1}\left( y\right) }\right) \) . [There is perhaps an analogy between this definition of \( \sigma \left( f\right) \) and such classical homotopy invariants as the "degree" and the "Hopf invariant" of a mapping.]

Lemma 20.4. The integer \( \sigma \left( f\right) \) depends only on the homotopy class of \( f \) . Furthermore, if \( {4i} < \left( {n - 1}\right) /2 \) so that the cohomotopy group \( {\pi }^{r}\left( {K}^{n}\right) \) is defined, then the correspondence \( \left( f\right)  \mapsto  \sigma \left( f\right) \) defines a homomorphism \( {\pi }^{r}\left( {K}^{n}\right) \) to \( \mathbb{Z} \) .

The proof of 20.3 and 20.4 will be based on the following.

Lemma 20.5. If \( f : K \rightarrow  L \) is a simplicial mapping, and if \( y \) belongs to the interior \( U \) of a simplex \( \Delta \) of \( L \) , then \( {f}^{-1}\left( U\right) \) is homeomorphic to \( U \times  {f}^{-1}\left( y\right) \) .

The corresponding assertion for the entire closed simplex would of course be false.

Proof. Let \( {A}_{0},\cdots ,{A}_{r} \) be the vertices of \( \Delta \) , and set \( y = {t}_{0}{A}_{0} + \cdots  + {t}_{r}{A}_{r} \) , where the \( {t}_{i} \) are positive real numbers with sum 1 . Evidently any point \( x \in  {f}^{-1}\left( U\right) \) can be expressed uniquely as a sum

\[
x = {s}_{0}{A}_{0}^{\prime } + \cdots  + {s}_{r}{A}_{r}^{\prime }
\]

where each \( {A}_{i}^{\prime } \) is a boundary point of the smallest simplex of \( K \) containing \( x \) and where \( f\left( {A}_{i}^{\prime }\right)  = {A}_{i} \) . Note that \( f\left( x\right)  = {s}_{0}{A}_{0} + \cdots  + {s}_{r}{A}_{r} \) . The required homeomorphism \( {f}^{-1}\left( U\right)  \rightarrow  U \times  {f}^{-1}\left( y\right) \) is now defined by the formula \( x \mapsto  \left( {f\left( x\right) ,{t}_{0}{A}_{0}^{\prime } + \cdots  + {t}_{r}{A}_{r}^{\prime }}\right) . \)

It follows incidentally that \( {f}^{-1}\left( y\right) \) is homeomorphic to \( {f}^{-1}\left( {y}^{\prime }\right) \) for all \( y \) and \( {y}^{\prime } \) in \( U \) .

Proof of 20.3. Subdivide \( {K}^{n} \) and \( {\sum }^{r} \) so that \( f \) is simplicial. This is possible since \( {K}^{n} \) is compact. Assume that \( y \) belongs to the interior \( U \) of a top dimensional simplex \( {\Delta }^{r} \) of the subdivided \( {\sum }^{r} \) . Then by \( {20.5}, U \times  {f}^{-1}\left( y\right) \) has the local rational homology groups of an \( n \) -manifold. Since \( U \) has the local homology groups \( {\mathrm{H}}_{ * }\left( {U, U \smallsetminus  X}\right) \) of an \( r \) -manifold, it follows easily that \( {f}^{-1}\left( y\right) \) has the local rational homology groups of a manifold of dimension \( n - r = {4i} \) .

This set \( {f}^{-1}\left( y\right) \) can be given the structure of a simplicial complex. In fact, taking further subdivisions, so that \( y \) is a vertex of the subdivided \( {\sum }^{r} \) , it follows that \( {f}^{-1}\left( y\right) \) is a subcomplex of the correspondingly subdvided \( {K}^{n} \) .

Given orientations for \( U \) and \( U \times  {f}^{-1}\left( y\right) \) , it is not difficult to construct an induced orientation for \( {f}^{-1}\left( y\right) \) , using for example the homology cross product operation. Hence the signature \( \sigma \left( {{f}^{-1}\left( y\right) }\right) \) is defined. We noted above that \( {f}^{-1}\left( {y}^{\prime }\right) \) is homeomorphic to \( {f}^{-1}\left( y\right) \) for all \( {y}^{\prime } \in  U \) . Hence the integer valued function \( \sigma \left( {{f}^{-1}\left( y\right) }\right) \) is certainly independent of \( y \) for \( y \in  U \) .

Suppose that \( f \) and \( g \) are homotopic piecewise linear maps from \( {K}^{n} \) to \( {\sum }^{r} \) . Choosing a piecewise linear homotopy

\[
h : {K}^{n} \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\sum }^{r}
\]

then subdividing so that \( h \) is simplicial and choosing \( y \in  U \) as above, a similar argument shows that \( {h}^{-1}\left( y\right) \) is a rational homology manifold-with-boundary, bounded by the disjoint union \( {g}^{-1}\left( y\right)  + \left( {-{f}^{-1}\left( y\right) }\right) \) . Since the signature of a boundary is zero, this proves that

\[
\sigma \left( {{f}^{-1}\left( y\right) }\right)  = \sigma \left( {{g}^{-1}\left( y\right) }\right)
\]

for almost all \( y \) .

Now suppose that we are given two different points \( {y}_{1} \) and \( {y}_{2} \) of \( {\sum }^{r} \) , each of which satisfies the condition that the function \( y \mapsto  \sigma \left( {{f}^{-1}\left( y\right) }\right) \) is constant throughout a neighborhood of \( {y}_{i} \) . Choosing a piecewise linear homeomorphism \( u : {\sum }^{r} \rightarrow  {\sum }^{r} \) , homotopic to the identity, with \( u\left( {y}_{1}\right)  = {y}_{2} \) , it follows that \( u \circ  f \) is homotopic to \( f \) , and hence that

\[
\sigma \left( {{f}^{-1}{u}^{-1}\left( z\right) }\right)  = \sigma \left( {{f}^{-1}\left( z\right) }\right)
\]

for almost all \( z \) . Choosing \( z \) close to \( {y}_{2} \) , so that \( {u}^{-1}\left( z\right) \) is close to \( {y}_{1} \) , this implies that

\[
\sigma \left( {{f}^{-1}\left( {y}_{1}\right) }\right)  = \sigma \left( {{f}^{-1}\left( {y}_{2}\right) }\right) ,
\]

as required.

Proof of 20.4. It follows immediately from the argument above that \( \sigma \left( f\right) \) depends only on the homotopy class of \( f \) . To show that this correspondence \( \left( f\right)  \mapsto  \sigma \left( f\right) \) is additive, first recall the construction of the group operation in \( {\pi }^{r}\left( {K}^{n}\right) \) . Given two maps \( f, g : {K}^{n} \rightarrow  {\sum }^{r} \) we can form the map \( \left( {f, g}\right)  : x \mapsto  \left( {f\left( x\right) , g\left( x\right) }\right) \) from \( {K}^{n} \) to \( {\sum }^{r} \times  {\sum }^{r} \) . If \( n < {2r} \) , this can be deformed into the subcomplex

\[
{\sum }^{r} \land  {\sum }^{r} = \left( {{\sum }^{r}\times \{ \text{ point }\} }\right)  \cup  \left( {\{ \text{ point }\}  \times  {\sum }^{r}}\right)  \subset  {\sum }^{r} \times  {\sum }^{r}\text{ , }
\]

and if \( n < {2r} - 1 \) , the resulting map \( {K}^{n} \rightarrow  {\sum }^{r} \land  {\sum }^{r} \) is unique up to homotopy. (The hypothesis that \( \left( {f, g}\right) \) maps \( {K}^{n} \) into \( {\sum }^{r} \land  {\sum }^{r} \) is equivalent to the hypotheasis that for every \( x \in  {K}^{n} \) , either \( f\left( x\right) \) or \( g\left( x\right) \) is the base point.) Now mapping \( {\sum }^{r} \land  {\sum }^{r} \) to \( {\sum }^{r} \) by the "folding map," which is the identity on each copy of \( {\sum }^{r} \) , we obtain a composite map \( h : {K}^{n} \rightarrow  {\sum }^{r} \) , representing the required sum \( \left( f\right)  + \left( g\right) \) .

If \( f \) and \( g \) are chosen within their homotopy classes so that for all \( x \) either \( f\left( x\right) \) or \( g\left( x\right) \) is the basepoint, note that \( h\left( x\right) \) is defined simply by

\[
h\left( x\right)  = f\left( x\right) \text{ if }f\left( x\right)  \neq  \text{ base point },
\]

\[
h\left( x\right)  = g\left( x\right) \text{ if }f\left( x\right)  = \text{ base point . }
\]

Hence \( {h}^{-1}\left( y\right) \) is the disjoint union of \( {f}^{-1}\left( y\right) \) and \( {g}^{-1}\left( y\right) \) , for \( y \neq \) base point, and it follows immediately that \( \sigma \left( h\right)  = \sigma \left( f\right)  + \sigma \left( g\right) \) .

We can now prove one of the main results of this section. We continue to assume that the finite simplicial complex \( {K}^{n} \) is an oriented rational homology manifold.

Theorem 20.6. For \( {4i} < \left( {n - 1}\right) /2 \) , there is one and only one cohomology class

\[
{\ell }_{i} \in  {\mathrm{H}}^{4i}\left( {{K}^{n};\mathbb{Q}}\right)
\]

which satisfies the identity

\[
\left\langle  {{\ell }_{i} \smile  {f}^{ * }\left( u\right) ,{\mu }_{n}}\right\rangle   = \sigma \left( f\right)
\]

for every map \( f : {K}^{n} \rightarrow  {\sum }^{n - {4i}} \) .

Clearly this class \( {\ell }_{i} = {\ell }_{i}\left( {K}^{n}\right) \) is invariant under piecewise linear homomorphism.

Proof. As already noted, the homomorphism

\[
{\pi }^{n - {4i}}\left( {K}^{n}\right)  \rightarrow  {\mathrm{H}}^{n - {4i}}\left( {{K}^{n};\mathbb{Z}}\right)
\]

defined by \( \left( f\right)  \mapsto  {f}^{ * }\left( u\right) \) is a \( {\mathbf{{Ab}}}_{ < \infty } \) -isomorphism. (Compare proof of Lemma 20.2) It follows easily that there is one and only one homomorphism

\[
{\sigma }^{\prime } : {\mathrm{H}}^{n - {4i}}\left( {{K}^{n};\mathbb{Z}}\right)  \rightarrow  \mathbb{Q}
\]

which makes the following diagram commutative.

![bo_d7du9galb0pc73deir9g_240_464_769_609_233_0.jpg](images/bo_d7du9galb0pc73deir9g_240_464_769_609_233_0.jpg)

Now, by Poincaré duality, we have

\[
{\sigma }^{\prime }\left( x\right)  = \left\langle  {{\ell }_{i} \smile  x,{\mu }_{n}}\right\rangle
\]

for some uniquely defined rational homology class \( {\ell }_{i} \) .

Let us compare the combinatorial and differentiable definitions. We will need some basic results of J. H. C. Whitehead. Let \( M = {M}^{n} \) be a smooth manifold. By a smooth triangulation of \( M \) is meant a homeomorphism \( t : K \rightarrow  M \) where \( K \) is a simplicial complex, such that the restriction of \( t \) to each closed simplex of \( K \) is smooth and of maximal rank everywhere.

Theorem (Theorem of Whitehead). Every smooth paracompact manifold possesses a smooth triangulation. In fact, if \( M \) is a smooth paracompact manifold-with-boundary, then every smooth triangulation \( {K}_{0} \rightarrow  \partial M \) can be extended to a smooth triangulation \( K \rightarrow  M \) , where \( K \) is a simplicial complex containing \( {K}_{0} \) as a subcomplex. Finally, if \( {t}_{1} : {K}_{1} \rightarrow  M \) and \( {t}_{2} : {K}_{2} \rightarrow  M \) are two different smooth triangulations of \( M \) , then the homeomorphism \( {t}_{2}^{-1} \circ  {t}_{1} : {K}_{1} \rightarrow  {K}_{2} \) is homotopic to a piecewise linear homeomoprhism from \( {K}_{1} \) to \( {K}_{2} \) .

Thus the smooth manifold \( M \) determines a simplicial complex \( K \) which is unique up to piecewise linear homeomorphism. For the proofs we refer to [Whi61], [Mun00].

Now consider the characteristic cohomology class \( {\ell }_{i}\left( K\right) \) . Using the isomorphism \( {t}^{ * } : {\mathrm{H}}^{4i}\left( M\right)  \rightarrow  {\mathrm{H}}^{4i}\left( K\right) \) we obtain a corresponding class

\[
{t}^{* - 1}{\ell }_{i}\left( K\right)  \in  {\mathrm{H}}^{4i}\left( M\right) ,
\]

still assuming that \( {4i} < \left( {n - 1}\right) /2 \) . This class does not depend on the choice of smooth triangulation. For if \( {t}_{1} : {K}_{1} \rightarrow  M \) is another smooth triangulation, then \( {t}_{1}^{-1} \circ  t \) is homotopic to a piecewise linear homeomorphism, hence

\[
{t}^{* - 1}{\ell }_{i}\left( K\right)  = {t}_{1}^{* - 1}{\ell }_{i}\left( {K}_{1}\right) .
\]

This well defined rational cohomology class will be denoted briefly by \( {\ell }_{i}\left( M\right) \) .

Theorem 20.7. The class \( {\ell }_{i}\left( {M}^{n}\right) \) , defined for a smooth manifold by a combinatorial procedure, is equal to the Hirzebruch class \( {L}_{i}\left( {{p}_{1},\cdots ,{p}_{i}}\right) \) of the tangent bundle of \( {M}^{n} \) .

Proof. Let \( f : {M}^{n} \rightarrow  {S}^{r} \) be a smooth map. We will construct a diagram

![bo_d7du9galb0pc73deir9g_241_754_1282_227_160_0.jpg](images/bo_d7du9galb0pc73deir9g_241_754_1282_227_160_0.jpg)

commutative up to homotopy, where \( g \) is piecewise linear and \( t, s \) are smooth triangulations, so that

\[
\sigma \left( {{f}^{-1}\left( y\right) }\right)  = \sigma \left( {{g}^{-1}\left( z\right) }\right)
\]

for \( y \) belonging to a non-vacuous open set in \( {S}^{r} \) and for \( z \) belonging to a nonvacuous open set in \( {L}^{r} \) . Together with 20.2 and 20.6, this will complete the proof.

Let \( {y}_{0} \in  {S}^{r} \) be a regular value of \( f \) . If \( B \) is a sufficiently small ball around \( {y}_{0} \) , then it is not difficult to show that the inverse image \( {f}^{-1}\left( B\right) \) is diffeomorphic to \( {f}^{-1}\left( {y}_{0}\right)  \times  B \) under a diffeomorphism which preserves the projection map to \( B \) .

Choose smooth triangulations

\[
{t}_{1} : {K}_{1} \rightarrow  {f}^{-1}\left( {y}_{0}\right)
\]

and

\[
{t}_{2} : {K}_{2} \rightarrow  B\text{ . }
\]

Then the smooth triangulation

\[
{t}_{1} \times  {t}_{2} : {K}_{1} \times  {K}_{1} \rightarrow  {f}^{-1}\left( {y}_{0}\right)  \times  B \subset  {M}^{n}
\]

restricts to a smooth triangulation

\[
{K}_{1} \times  \partial {K}_{2} \rightarrow  {f}^{-1}\left( {y}_{0}\right)  \times  \partial B
\]

of the boundary which, by Whitehead's theorem, extends to a smooth triangulation

\[
{K}_{3} \rightarrow  {M}^{n} - \operatorname{interior}\left( {{f}^{-1}\left( {y}_{0}\right)  \times  B}\right)
\]

of the complementary domain. Setting \( {K}^{n} = {K}_{1} \times  {K}_{2} \cup  {K}_{3} \) (and subdividing if necessary), we thus obtain a smooth triangulation \( t : {K}^{n} \rightarrow  {M}^{n} \) . Similarly \( {t}_{2} \) can be extended to a smooth triangulation \( s : {L}^{r} \rightarrow  {S}^{r} \) .

Now the projection map \( {K}_{1} \times  {K}_{2} \rightarrow  {K}_{2} \subset  {L}^{r} \) can be extended to a piecewise linear map \( g : {K}^{n} \rightarrow  {L}^{r} \) , in such a manner that the complement of \( {K}_{1} \times  {K}_{2} \) maps to the complement of \( {K}_{2} \) . It is then easy to check that the composition \( s \circ  g \) is homotopic to \( f \circ  t \) . Furthermore

\[
{f}^{-1}\left( y\right)  \cong  {g}^{-1}\left( z\right)
\]

for every \( y \in  B \) and every \( z \in  {K}_{2} \) , so that the signature \( \sigma \left( {{f}^{-1}\left( y\right) }\right) \) is certainly equal to \( \sigma \left( {{g}^{-1}\left( z\right) }\right) \) .

So far, the condition \( {4i} < \left( {n - 1}\right) /2 \) has been imposed. However, given \( {K}^{n} \) , one can always form the product space \( {K}^{n} \times  {\sum }^{m} \) with \( m \) large. The class \( {\ell }_{i}\left( {K}^{n}\right) \) can then be defined as the class induced from \( {\ell }_{i}\left( {{K}^{n} \times  {\sum }^{m}}\right) \) by the natural inclusion map. It is not hard to show that this new class is well defined, and has the expected properties. In particular the Kronecker index \( \left\langle  {{\ell }_{i}\left( {K}^{4i}\right) ,{\mu }_{4i}}\right\rangle \) is always equal to the signature \( \sigma \left( {K}^{4i}\right) \) .

Another extension which can easily be made is to homology manifolds-with-boundary. It is only necessary to substitute the relative cohomotopy groups \( {\pi }^{n - {4i}}\left( {{K}^{n},\partial {K}^{n}}\right) \) and the Lefschetz duality theorem in the above discussion.
