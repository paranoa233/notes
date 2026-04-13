# 11.2 The Tangent Bundle

Let \( M \) be a Riemannian manifold. Then the product \( M \times  M \) also has the structure of a Riemannian manifold, the length of the tangent vector

\[
\left( {u, v}\right)  \in  {\mathbf{T}}_{x}M \times  {\mathbf{T}}_{y}M \cong  {\mathbf{T}}_{\left( x, y\right) }\left( {M \times  M}\right)
\]

being defined by

\[
{\left| \left( u, v\right) \right| }^{2} = {\left| u\right| }^{2} + {\left| v\right| }^{2},
\]

and the inner product of two such vectors being defined by

\[
\left( {u, v}\right)  \cdot  \left( {{u}^{\prime },{v}^{\prime }}\right)  = u \cdot  {u}^{\prime } + v \cdot  {v}^{\prime }.
\]

Note that the diagonal mapping

\[
x \mapsto  \Delta \left( x\right)  = \left( {x, x}\right)
\]

embeds \( M \) smoothly as a closed subset of \( M \times  M \) . (This diagonal embedding is almost an isometry: it multiplies all lengths by \( \sqrt{2} \) .)

Lemma 11.5. The normal bundle \( {\nu }^{n} \) associated with the diagonal embedding of \( M \) in \( M \times  M \) is canonically isomorphic to the tangent bundle of \( M \) .

Proof. Evidently a vector

\[
\left( {u, v}\right)  \in  {\mathbf{T}}_{x}M \times  {\mathbf{T}}_{y}M \cong  {\mathbf{T}}_{\left( x, x\right) }\left( {M \times  M}\right)
\]

is tangent to \( \Delta \left( M\right) \) if and only if \( u = v \) , and normal to \( \Delta \left( M\right) \) if and only if \( u + v = 0 \) . Thus each tangent vector \( v \in  {\mathbf{T}}_{x}M \) corresponds uniquely to a normal vector \( \left( {-v, v}\right)  \in  {\mathbf{T}}_{\left( x, x\right) }\left( {M \times  M}\right) \) . This correspondence

\[
\left( {x, v}\right)  \mapsto  \left( {\left( {x, x}\right) ,\left( {-v, v}\right) }\right)
\]

maps the tangent manifold \( \mathbf{T}M = E\left( {\tau }_{M}\right) \) diffeomorphically onto the total space \( E\left( {\nu }^{n}\right) \) .

We will be particularly interested in Riemannian manifolds \( M \) for which the tangent bundle \( {\tau }_{M} \) is oriented.

Lemma 11.6. Any orientation for the tangent bundle \( {\tau }_{M} \) gives rise to an orientation for the underlying topological manifold \( M \) , and conversely any orientation for \( M \) gives rise to an orientation for \( {\tau }_{M} \) .

Proof. As defined in Appendix A, an orientation for a topological manifold \( M \) is a function which assigns to each point \( x \) of \( M \) a preferred generator \( {\mu }_{x} \) for the infinite cyclic group \( {\mathrm{H}}_{n}\left( {M, M - x}\right) \) , using integer coefficients. These preferred generators are required to "vary continuously" with \( x \) , in the sense that \( {\mu }_{x} \) corresponds to \( {\mu }_{y} \) under the isomorphisms

\[
{\mathrm{H}}_{n}\left( {M, M - x}\right)  \leftarrow  {\mathrm{H}}_{n}\left( {M, M - N}\right)  \rightarrow  {\mathrm{H}}_{n}\left( {M, M - y}\right) ,
\]

where \( N \) denotes a nicely embedded \( n \) -cell neighborhood of \( x \) and \( y \) is any point of \( N \) .

Similarly, an orientation for the vector bundle \( {\tau }_{M} \) can be specified by assigning a preferred generator \( {\mu }_{x}^{\prime } \) to the infinite cyclic group \( {\mathrm{H}}_{n}\left( {{\mathbf{T}}_{x}M,{\mathbf{T}}_{x}M - 0}\right) \) for each \( x \) . These generators \( {\mu }_{x}^{\prime } \) must vary continuously with \( x \) , for example in the sense that \( {\mu }_{x}^{\prime } \) corresponds to \( {\mu }_{y}^{\prime } \) under the isomorphisms

\[
{\mathrm{H}}_{n}\left( {{\mathbf{T}}_{x}M,{\mathbf{T}}_{x}M - 0}\right)  \rightarrow  {\mathrm{H}}_{n}\left( {\mathbf{T}N,\mathbf{T}N - \left( {N \times  0}\right) }\right)  \leftarrow  {\mathrm{H}}_{n}\left( {{\mathbf{T}}_{y}M,{\mathbf{T}}_{y}M - 0}\right)
\]

where \( N \) denotes an \( n \) -cell neighborhood and \( y \in  N \) . (Compare §9.)

But the homology group \( {\mathrm{H}}_{n}\left( {M, M - x}\right) \) is canonically isomorphic to \( {\mathrm{H}}_{n}\left( {{\mathbf{T}}_{x}M,{\mathbf{T}}_{x}M - 0}\right) \) as one sees by applying Corollary 11.2 to the 0-dimensional manifold \( x \) , embedded in \( M \) as a closed subset with normal bundle \( {\mathbf{T}}_{x}M \) . The proof that \( {\mu }_{x} \) varies continuously with \( x \) if and only if the corresponding generators \( {\mu }_{x}^{\prime } \) vary continuously with \( x \) is not difficult. In fact, since the problem is purely local, it suffices to consider the special case where \( M \) is Euclidean space with the standard metric. Details will be left to the reader.

Let us study homology and cohomology of \( M \) with coefficients in some fixed commutative ring \( \Lambda \) . We will always assume either that \( M \) is oriented or that \( \Lambda  = \mathbb{Z}/2 \) . It follows from Corollary 11.2 that there is a fundamental cohomology class

\[
{u}^{\prime } \in  {\mathrm{H}}^{n}\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)
\]

with coefficients in \( \Lambda \) . By Lemma 11.13, the restriction of \( {u}^{\prime } \) to the diagonal submanifold \( \Delta \left( M\right)  \cong  M \) is equal to the Euler class

\[
\mathrm{e}\left( {\nu }^{n}\right)  = \mathrm{e}\left( {\tau }_{M}\right)
\]

with coefficient ring \( \Lambda \) , in the oriented case, or to the Stiefel-Whitney class \( {\mathrm{w}}_{n}\left( {\tau }_{M}\right) \) in the mod 2 case.

This cohomology class \( {u}^{\prime } \) can be characterized more explicitly as follows. Note that each cohomology group \( {\mathrm{H}}^{n}\left( {M, M - x}\right) \) has a preferred generator \( {u}_{x} \) , defined by the condition

\[
\left\langle  {{u}_{x},{\mu }_{x}}\right\rangle   = 1
\]

(In the mod 2 case, \( {u}_{x} \) is the unique non-zero element of \( {\mathrm{H}}^{n}\left( {M, M - x}\right) \) .) Define the canonical embedding

\[
{j}_{x} : \left( {M, M - x}\right)  \rightarrow  \left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)
\]

by setting \( {j}_{x}\left( y\right)  = \left( {x, y}\right) \) .

Lemma 11.7. The class \( {u}^{\prime } \in  {\mathrm{H}}^{n}\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right) \) is uniquely characterized by the property that its image \( {j}_{x}^{ * }\left( {u}^{\prime }\right) \) is equal to the preferred generator \( {u}_{x} \) for every \( x \in  M \) .

Proof. By its construction (Theorem 10.4 and Corollary 11.2), the cohomology class \( {u}^{\prime } \) can be uniquely characterized as follows. For any \( x \) and any small neighborhood \( N \) of zero in the tangent space \( {\mathbf{T}}_{x}M \) , consider the embedding

\[
\left( {N, N - 0}\right)  \rightarrow  \left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)
\]

defined by the exponential map

\[
v \mapsto  \left( {\operatorname{Exp}\left( {x, - v}\right) ,\operatorname{Exp}\left( {x, v}\right) }\right) .
\]

Then the induced cohomology homomorphism must map \( {u}^{\prime } \) to the preferred generator for the module \( {\mathrm{H}}^{n}\left( {N, N - 0}\right)  \cong  {\mathrm{H}}^{n}\left( {{\mathbf{T}}_{x}M,{\mathbf{T}}_{x}M - 0}\right) \)

Making use of the homotopy \( \left( {v, t}\right)  \mapsto  \left( {\operatorname{Exp}\left( {x, - {tv}}\right) ,\operatorname{Exp}\left( {x, v}\right) }\right) \) for \( 0 \leq  t \leq  1 \) , it follows that we can equally well use the embedding of \( \left( {N, N - 0}\right) \) in \( \left( {M \times  M, M \times  M - \Delta \left( M\right) }\right) \) defined by

\[
v \mapsto  \left( {x,\operatorname{Exp}\left( {x, v}\right) }\right) .
\]

Since this is the composition of \( {j}_{x} \) with the canonical embedding

\[
\operatorname{Exp} : \left( {N, N - 0}\right)  \rightarrow  \left( {M, M - x}\right)
\]

which was used to prove 11.6, the conclusion follows.
