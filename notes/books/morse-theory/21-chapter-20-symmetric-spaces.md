# Chapter 20 Symmetric Spaces

## Part IV. Applications to Lie Groups and Symmetric Spaces

Based on lecture notes by

M. Spivak and R. Wells

A symmetric space is a connected Riemannian manifold \( M \) such that, for each \( p \in  M \) there is an isometry \( {I}_{p} : M \rightarrow  M \) which leaves \( p \) fixed and reverses geodesics through \( p \) , i.e., if \( \gamma \) is a geodesic and \( \gamma \left( 0\right)  = p \) then \( {I}_{p}\left( {\gamma \left( t\right) }\right)  = \gamma \left( {-t}\right) \) .

Lemma 20.1. Let \( \gamma \) be a geodesic in \( M \) , and let \( p = \gamma \left( 0\right) \) and \( q = \gamma \left( c\right) \) . Then \( {I}_{q}{I}_{p}\left( {\gamma \left( t\right) }\right)  = \gamma \left( {t + {2c}}\right) \) (assuming \( \gamma \left( t\right) \) and \( \gamma \left( {t + {2c}}\right) \) are defined). Moreover, \( {I}_{q}{I}_{p} \) preserves parallel vector fields along \( \gamma \) .

Proof. Let \( {\gamma }^{\prime }\left( t\right)  = \gamma \left( {t + c}\right) \) . Then \( {\gamma }^{\prime }\left( t\right) \) is a geodesic and \( {\gamma }^{\prime }\left( 0\right)  = q \) . Therefore \( {I}_{q}{I}_{p}\left( {\gamma \left( t\right) }\right)  = {I}_{q}\left( {\gamma \left( {-t}\right) }\right)  = {I}_{q}\left( {{\gamma }^{\prime }\left( {-t - c}\right) }\right)  = {\gamma }^{\prime }\left( {t + c}\right)  = \gamma \left( {t + {2c}}\right) . \)

If the vector field \( V \) is parallel along \( \gamma \) then \( {I}_{{p}_{ * }}\left( V\right) \) is parallel (since \( {I}_{p} \) is an isometry) and \( {I}_{{p}_{ * }}\left( 0\right)  =  - V\left( 0\right) \) ; therefore \( {I}_{{p}_{ * }}\left( t\right)  =  - V\left( {-t}\right) \) . Therefore \( {I}_{{q}_{ * }}{I}_{{p}_{ * }}\left( {V\left( t\right) }\right)  = \; V\left( {t + {2c}}\right) \) .

Corollary 20.2. \( M \) is complete.

Since Lemma 20.1 shows that geodesics can be indefinitely extended.

Corollary 20.3. \( {I}_{P} \) is unique.

Since any point is joined to \( p \) by a geodesic.

Corollary 20.4. If \( U, V \) and \( W \) are parallel vector fields along \( \gamma \) then \( \mathcal{R}\left( {U, V}\right) W \) is also a parallel field along \( \gamma \) .

Proof. If \( X \) denotes a fourth parallel vector field along \( \gamma \) , note that the quantity \( \langle \mathcal{R}\left( {U, V}\right) W, X\rangle \) is constant along \( \gamma \) . In fact, given \( p = \gamma \left( 0\right) , q = \gamma \left( c\right) \) , consider the isometry \( T = {I}_{\gamma \left( {c/2}\right) }{I}_{p} \) which carries \( p \) to \( q \) . Then

\[
\left\langle  {\mathcal{R}\left( {{U}_{q},{V}_{q}}\right) {W}_{q},{X}_{q}}\right\rangle   = \left\langle  {\mathcal{R}\left( {{T}_{ * }{U}_{p},{T}_{ * }{V}_{p}}\right) {T}_{ * }{W}_{p},{T}_{ * }{X}_{p}}\right\rangle
\]

by Lemma 20.1. Since \( T \) is an isometry, this quantity is equal to \( \left\langle  {\mathcal{R}\left( {{U}_{p},{V}_{p}}\right) {W}_{p},{X}_{p}}\right\rangle \) . Thus \( \langle \mathcal{R}\left( {U, V}\right) W, X\rangle \) is constant for every parallel vector field \( X \) . It clearly follows that \( \mathcal{R}\left( {U, V}\right) W \) is parallel.

Manifolds with the property of Corollary 20.4 are called locally symmetric. (A classical theorem, due to Cartan states that a complete, simply connected, locally symmetric manifold is actually symmetric.)

In any locally symmetric manifold the Jacobi differential equations have simple explicit solutions. Let \( \gamma  : \mathbf{R} \rightarrow  M \) be a geodesic in a locally symmetric manifold. Let \( V = \frac{\mathrm{d}\gamma }{\mathrm{d}t}\left( 0\right) \) be the velocity vector at \( p = \gamma \left( 0\right) \) . Define a linear transformation

\[
{K}_{V} : T{M}_{p} \rightarrow  T{M}_{p}
\]

\( {\text{ by }}^{1}{K}_{V}\left( W\right)  = \mathcal{R}\left( {V, W}\right) V \) . Let \( {e}_{1},\ldots ,{e}_{n} \) denote the eigenvalues of \( {K}_{V} \) .

Theorem 20.5. The conjugate points to \( p \) along \( \gamma \) are the points \( \gamma \left( {{\pi k}/\sqrt{{e}_{i}}}\right) \) where \( k \) is any non-zero integer, and \( {e}_{i} \) is any positive eigenvalue of \( {K}_{V} \) . The multiplicity of \( \gamma \left( t\right) \) as a conjugate point is equal to the number of \( {e}_{i} \) such that \( t \) is a multiple of \( \pi /\sqrt{{e}_{i}} \) .

Proof. First observe that \( {K}_{V} \) is self-adjoint:

\[
\left\langle  {{K}_{V}\left( W\right) ,{W}^{\prime }}\right\rangle   = \left\langle  {W,{K}_{V}\left( {W}^{\prime }\right) }\right\rangle  .
\]

This follows immediately from the symmetry relation

\[
\left\langle  {\mathcal{R}\left( {V, W}\right) {V}^{\prime },{W}^{\prime }}\right\rangle   = \left\langle  {\mathcal{R}\left( {{V}^{\prime },{W}^{\prime }}\right) V, W}\right\rangle  .
\]

Therefore we may choose an orthonormal basis \( {U}_{1},\ldots ,{U}_{n} \) for \( {M}_{p} \) so that

\[
{K}_{V}\left( {U}_{i}\right)  = {e}_{i}{U}_{i}
\]

where \( {e}_{1},\ldots ,{e}_{n} \) are the eigenvalues. Extend the \( {U}_{i} \) to vector fields along \( \gamma \) by parallel translation. Then since \( M \) is locally symmetric, the condition

\[
\mathcal{R}\left( {V,{U}_{i}}\right) V = {e}_{i}{U}_{i}
\]

remains true everywhere along \( \gamma \) . Any vector field \( W \) along \( \gamma \) may be expressed uniquely as

\[
W\left( t\right)  = {w}_{1}\left( t\right) {U}_{1}\left( t\right)  + \cdots  + {w}_{n}\left( t\right) {U}_{n}\left( t\right) .
\]

Then the Jacobi equation \( \frac{{\mathrm{D}}^{2}W}{\mathrm{\;d}{t}^{2}} + {K}_{V}\left( W\right)  = 0 \) takes the form

\[
\sum \frac{{\mathrm{d}}^{2}{w}_{i}}{\mathrm{\;d}{t}^{2}}{U}_{i} + \sum {e}_{i}{w}_{i}{U}_{i} = 0.
\]

Since the \( {U}_{i} \) are everywhere linearly independent this is equivalent to the system of \( n \) equations

\[
\frac{{\mathrm{d}}^{2}{w}_{i}}{\mathrm{\;d}{t}^{2}} + {e}_{i}{w}_{i} = 0.
\]

We are interested in solutions that vanish at \( t = 0 \) . If \( {e}_{i} > 0 \) then

\[
{w}_{i}\left( t\right)  = {c}_{i}\sin \left( {\sqrt{{e}_{i}}t}\right) ,\;\text{ for some constant }{c}_{i}.
\]

Then the zeros of \( {w}_{i}\left( t\right) \) are at the multiples of \( t = \pi /\sqrt{{e}_{i}} \) .

If \( {e}_{i} = 0 \) then \( {w}_{i}\left( t\right)  = {c}_{i}t \) and if \( {e}_{i} < 0 \) then \( {w}_{i}\left( t\right)  = {c}_{i}\sinh \left( {\sqrt{\left| {e}_{i}\right| }t}\right) \) for some constant \( {c}_{i} \) . Thus if \( {e}_{i} < 0,{w}_{i}\left( t\right) \) vanishes only at \( t = 0 \) . This completes the proof of Theorem 20.5.

---

\( {}^{1}{K}_{V} \) should not be confused with the Ricci tensor of chapter 19.

---
