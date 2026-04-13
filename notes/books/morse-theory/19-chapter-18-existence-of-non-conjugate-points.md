# Chapter 18 Existence of Non-Conjugate Points

Based on lecture notes by

M. Spivak and R. Wells

Theorem 17.3 gives a good description of the space \( \Omega \left( {M;p, q}\right) \) providing that the points \( p \) and \( q \) are not conjugate to each other along any geodesic. This section will justify this result by showing that such non-conjugate points always exist.

Recall that a smooth map \( f : N \rightarrow  M \) between manifolds of the same dimension is critical at a point \( x \in  N \) if the induced map

\[
{f}_{ * } : T{N}_{x} \rightarrow  T{M}_{f\left( x\right) }
\]

of tangent spaces is not 1-1 . We will apply this definition to the exponential map

\[
\exp  = {\exp }_{p} : T{M}_{p} \rightarrow  M.
\]

(We will assume that \( M \) is complete, so that exp is everywhere defined; although this assumption could easily be eliminated.)

Theorem 18.1. The point \( \exp v \) is conjugate to \( p \) along the geodesic \( {\gamma }_{v} \) from \( p \) to \( \exp v \) if and only if the mapping \( \exp \) is critical at \( v \) .

Proof. Suppose that \( \exp \) is critical at \( v \in  T{M}_{p} \) . Then \( {\exp }_{ * }\left( X\right)  = 0 \) for some nonzero \( X \in  T{\left( T{M}_{p}\right) }_{v} \) , the tangent space at \( v \) to \( T{M}_{p} \) , considered as a manifold. Let \( u \mapsto  v\left( u\right) \) be a path in \( T{M}_{p} \) such that \( v\left( 0\right)  = v \) and \( \frac{\mathrm{d}v}{\mathrm{\;d}u}\left( 0\right)  = X \) . Then the map a defined by \( \alpha \left( {u, t}\right)  = \exp {tv}\left( u\right) \) is a variation through geodesics of the geodesic \( {\gamma }_{v} \) given by \( t \mapsto  \exp {tv} \) . Therefore the vector field \( W \) given by \( t \mapsto  {\left. \frac{\partial }{\partial u}\left( \exp tv\left( u\right) \right) \right| }_{u = 0} \) is a Jacobi field along \( {\gamma }_{v} \) . Obviously \( W\left( 0\right)  = 0 \) . We also have

\[
W\left( 1\right)  = {\left. \frac{\partial }{\partial u}\left( \exp tv\left( u\right) \right) \right| }_{u = 0} = {\exp }_{ * }\frac{\mathrm{d}v\left( u\right) }{\mathrm{d}u}\left( 0\right)  = {\exp }_{ * }X = 0.
\]

But this field is not identically zero since

\[
\frac{\mathrm{D}W}{\mathrm{\;d}t}\left( 0\right)  = {\left. \frac{\mathrm{D}}{\mathrm{d}u}\frac{\partial }{\partial t}\left( \exp tv\left( u\right) \right) \right| }_{\left( 0,0\right) } = {\left. \frac{\mathrm{D}}{\mathrm{d}u}v\left( u\right) \right| }_{u = 0} \neq  0.
\]

So there is a non-trivial Jacobi field along \( {\gamma }_{v} \) from \( p \) to \( \exp v \) , vanishing at these points; hence \( p \) and \( \exp v \) are conjugate along \( {\gamma }_{v} \) .

Now suppose that \( {\exp }_{ * } \) is non-singular at \( v \) . Choose \( n \) independent vectors \( {X}_{1},\ldots ,{X}_{n} \) in \( T{\left( T{M}_{p}\right) }_{v} \) . Then \( {\exp }_{ * }\left( {X}_{1}\right) ,\ldots ,{\exp }_{ * }\left( {X}_{n}\right) \) are linearly independent. In \( T{M}_{p} \) choose paths \( u \mapsto  {v}_{1}\left( u\right) ,\ldots , u \mapsto  {v}_{n}\left( u\right) \) with \( {v}_{i}\left( 0\right)  = v \) and \( \frac{\mathrm{d}{v}_{i}\left( u\right) }{\mathrm{d}u}\left( 0\right)  = {X}_{i} \) .

Then \( {a}_{1},\ldots ,{a}_{n} \) , constructed as above, provide \( n \) Jacobi fields \( {W}_{1},\ldots ,{W}_{n} \) along \( {\gamma }_{v} \) , vanishing at \( p \) . Since the \( {W}_{i}\left( 1\right)  = {\exp }_{ * }\left( {X}_{i}\right) \) are independent, no non-trivial linear combination of the \( {W}_{i} \) can vanish at \( \exp v \) . Since \( n \) is the dimension of the space of Jacobi fields along \( {\gamma }_{v} \) , which vanish at \( p \) , clearly no non-trivial Jacobi field along \( {\gamma }_{v} \) vanishes at both \( p \) and \( \exp v \) . This completes the proof.

Corollary 18.2. Let \( p \in  M \) . Then for almost all \( q \in  M, p \) is not conjugate to \( q \) along any geodesic.

Proof. This follows immediately from Theorem 18.1 together with Sard's theorem (Theorem 6.2).
