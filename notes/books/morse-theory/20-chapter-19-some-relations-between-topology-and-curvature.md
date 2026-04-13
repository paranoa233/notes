# Chapter 19 Some Relations Between Topology and Curvature

Based on lecture notes by

M. Spivak and R. Wells

This section will describe the behavior of geodesics in a manifold with "negative curvature" or with "positive curvature."

Lemma 19.1. Suppose that \( \langle \mathcal{R}\left( {A, B}\right) A, B\rangle  < 0 \) for every pair of vectors \( A, B \) in the tangent space \( T{M}_{p} \) and for every \( p \in  M \) . Then no two points of \( M \) are conjugate along any geodesic.

Proof. Let \( \gamma \) be a geodesic with velocity vector field \( V \) ; and let \( J \) be a Jacobi field along \( \gamma \) . Then

\[
\frac{{\mathrm{D}}^{2}J}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( {V, J}\right) V = 0
\]

so that

\[
\left\langle  {\frac{{\mathrm{D}}^{2}J}{\mathrm{\;d}{t}^{2}}, J}\right\rangle   =  - \langle \mathcal{R}\left( {V, J}\right) V, J\rangle  \geq  0.
\]

Therefore

\[
\frac{\mathrm{d}}{\mathrm{d}t}\left\langle  {\frac{\mathrm{D}J}{\mathrm{\;d}t}, J}\right\rangle   = \left\langle  {\frac{{\mathrm{D}}^{2}J}{\mathrm{\;d}{t}^{2}}, J}\right\rangle   + {\begin{Vmatrix}\frac{\mathrm{D}J}{\mathrm{\;d}t}\end{Vmatrix}}^{2} \geq  0.
\]

Thus the function \( \left\langle  {\frac{\mathrm{D}J}{\mathrm{\;d}t}, J}\right\rangle \) is monotonically increasing, and strictly so if \( \frac{\mathrm{D}J}{\mathrm{\;d}t} \neq  0 \) .

If \( J \) vanishes both at 0 and at \( {t}_{0} > 0 \) , then the function \( \left\langle  {\frac{\mathrm{D}J}{\mathrm{\;d}t}, J}\right\rangle \) also vanishes at 0 and \( {t}_{0} \) , and hence must vanish identically throughout the interval \( \left\lbrack  {0,{t}_{0}}\right\rbrack \) . This implies that

\[
J\left( 0\right)  = \frac{\mathrm{D}J}{\mathrm{\;d}t}\left( 0\right)  = 0,
\]

so that \( J \) is identically zero. This completes the proof.

Remark. If \( A \) and \( B \) are orthogonal unit vectors at \( p \) then the quantity \( \langle \mathcal{R}\left( {A, B}\right) A, B\rangle \) is called the sectional curvature determined by \( A \) and \( B \) . It is equal to the Gaussian curvature of the surface

\[
\left( {{u}_{1},{u}_{2}}\right)  \mapsto  {\exp }_{p}\left( {{u}_{1}A + {u}_{2}B}\right)
\]

spanned by the geodesics through \( p \) with velocity vectors in the subspace spanned by \( A \) and \( B \) . (See for example [Lau65, p. 101].)

Note. Intuitively the curvature of a manifold can be described in terms of "optics" within the manifold as follows. Suppose that we think of the geodesics as being the paths of light rays. Consider an observer at \( p \) looking in the direction of the unit vector \( U \) towards a point \( q = \exp \left( {rU}\right) \) . A small line segment at \( q \) with length \( L \) , pointed in a direction corresponding to the unit vector \( W \in  T{M}_{p} \) , would appear to the observer as a line segment of length

\[
L\left( {1 + \frac{{r}^{2}}{6}\langle \mathcal{R}\left( {U, W}\right) U, W\rangle  + \left( {\text{ terms involving higher powers of }r}\right) }\right) .
\]

Thus if sectional curvatures are negative then any object appears shorter than it really is. A small sphere of radius \( \varepsilon \) at \( q \) would appear to be an ellipsoid with principal radii \( \varepsilon \left( {1 + \frac{{r}^{2}}{6}{K}_{1} + \cdots }\right) ,\ldots ,\varepsilon \left( {1 + \frac{{r}^{2}}{6}{K}_{n} + \cdots }\right) \) where \( {K}_{1},\ldots ,{K}_{n} \) denote the eigenvalues of the linear transformation \( W \mapsto  \mathcal{R}\left( {U, W}\right) U \) . Any small object of volume \( v \) would appear to have volume \( v\left( {1 + \frac{{r}^{2}}{6}\left( {{K}_{1} + {K}_{2} + \cdots  + {K}_{n}}\right)  + \left( \text{ higher terms }\right) }\right) \) where \( {K}_{1} + \cdots  + {K}_{n} \) is equal to the "Ricci curvature" \( K\left( {U, U}\right) \) , as defined later in this section.

Here are some familiar examples of complete manifolds with curvature \( \leq  0 \) :

(a) The Euclidean space with curvature 0 .

(b) The paraboloid \( z = {x}^{2} - {y}^{2} \) , with curvature \( < 0 \) .

(c) The hyperboloid of rotation \( {x}^{2} + {y}^{2} - {z}^{2} = 1 \) , with curvature \( < 0 \) .

(d) The helicoid \( x\cos z + y\sin z = 0 \) , with curvature \( < 0 \) .

Remark. In all of these examples the curvature takes values arbitrarily close to 0. Cf. [Efi63].

A famous example of a manifold with everywhere negative sectional curvature is the pseudo-sphere

\[
z =  - \sqrt{1 - {x}^{2} - {y}^{2}} + {\operatorname{sech}}^{-1}\sqrt{{x}^{2} + {y}^{2}},\;z > 0
\]

with the Riemann metric induced from \( {\mathbf{R}}^{3} \) . Here the Gaussian curvature has the constant value -1 .

No geodesic on this surface has conjugate points although two geodesics may intersect in more than one point. The pseudo-sphere gives a non-Euclidean geometry, in which the sum of the angles of any triangle is \( < \pi \) radians. This manifold is not complete. In fact a theorem of Hilbert states that no complete surface of constant negative curvature can be imbedded in \( {\mathbf{R}}^{3} \) . (See Blaschke,"Differential Geometric I," 3rd edn., §96; or [Efi63].)

However, there do exist Riemannian manifolds of constant negative curvature which are complete. (See for example [Lau65, §12.6.2].) Such a manifold can even be compact; for example, a surface of genus \( \geq  2 \) . (Compare [HCV52, p. 259].)

Theorem 19.2 (Cartan1). Suppose that \( M \) is a simply connected, complete Riemannian manifold, and that the sectional curvature \( \langle \mathcal{R}\left( {A, B}\right) A, B\rangle \) is everywhere \( \leq  0 \) . Then any two points of \( M \) are joined by a unique geodesic. Furthermore, \( M \) is diffeomorphic to the Euclidean space \( {\mathbf{R}}^{n} \) .

---

\( {}^{1} \) See E. Cartan,"Lecons sur la Géométrie des Espaces de Riemann," Paris,1926 and 1951.

---

![bo_d7du90alb0pc73deir8g_97_434_197_714_638_0.jpg](images/bo_d7du90alb0pc73deir8g_97_434_197_714_638_0.jpg)

Proof. Since there are no conjugate points, it follows from the index theorem that every geodesic from \( p \) to \( q \) has index \( \lambda  = 0 \) . Thus Theorem 17.3 asserts that the path space \( \Omega \left( {M;p, q}\right) \) has the homotopy type of a 0-dimensional CW-complex, with one vertex for each geodesic.

The hypothesis that \( M \) is simply connected implies that \( \Omega \left( {M;p, q}\right) \) is connected. Since a connected 0-dimensional CW-complex must consist of a single point, it follows that there is precisely one geodesic from \( p \) to \( q \) .

Therefore, the exponential map \( {\exp }_{p} : T{M}_{p} \rightarrow  M \) is one-one and onto. But it follows from Theorem 18.1 that \( {\exp }_{p} \) is non-critical everywhere; so that \( {\exp }_{p} \) is locally a diffeomorphism. Combining these two facts, we see that \( {\exp }_{p} \) is a global diffeomorphism. This completes the proof of Theorem 19.2.

More generally, suppose that \( M \) is not simply connected; but is complete and has sectional curvature \( \leq  0 \) . (For example \( M \) might be a flat torus \( {\mathbb{S}}^{1} \times  {\mathbb{S}}^{1} \) , or a compact surface of genus \( \geq  2 \) with constant negative curvature.) Then Theorem 19.2 applies to the, universal covering space \( \widetilde{M} \) of \( M \) . For it is clear that \( \widetilde{M} \) inherits a Riemannian metric from \( M \) which is geodesically complete, and has sectional curvature \( \leq  0 \) .

Given two points \( p, q \in  M \) , it follows that each homotopy class of paths from \( p \) to \( q \) contains precisely one geodesic.

The fact that \( M \) is contractible puts strong restrictions on the topology of \( M \) . For example:

Corollary 19.3. If \( M \) is complete with \( \langle \mathcal{R}\left( {A, B}\right) A, B\rangle  \leq  0 \) then the homotopy groups \( {\pi }_{i}\left( M\right) \) are zero for \( i > 1 \) ; and \( {\pi }_{i}\left( M\right) \) contains no element of finite order other than the identity.

Proof. Clearly \( {\pi }_{i}\left( M\right)  = {\pi }_{i}\left( \widetilde{M}\right)  = 0 \) for \( i > 1 \) . Since \( \widetilde{M} \) is contractible the cohomology group \( {\mathrm{H}}^{k}\left( M\right) \) can be identified with the cohomology group \( {\mathrm{H}}^{k}\left( {{\pi }_{1}\left( M\right) }\right) \) of the group \( {\pi }_{1}\left( M\right) \) . (See for example pp. 200-202 of S. T. Hu "Homotopy Theory," Academic Press,1959.) Now suppose that \( {\pi }_{1}\left( M\right) \) contains a non-trivial finite cyclic subgroup \( G \) . Then for a suitable covering space \( \widehat{M} \) of \( M \) we have \( {\pi }_{1}\left( \widehat{M}\right)  = G \) ; hence

\[
{\mathrm{H}}^{k}\left( G\right)  = {\mathrm{H}}^{k}\left( \widehat{M}\right)  = 0\;\text{ for }k > n.
\]

But the cohomology groups of a finite cyclic group are non-trivial in arbitrarily high dimensions. This gives a contradiction; and completes the proof.

Now we will consider manifolds with "positive curvature." Instead of considering the sectional curvature, one can obtain sharper results in this case by considering the Ricci tensor (sometimes called the "mean curvature tensor").

Definition 19.4. The Ricci tensor at a point \( p \) of a Riemannian manifold \( M \) is a bilinear pairing

\[
K : T{M}_{p} \times  T{M}_{p} \rightarrow  \mathbf{R}
\]

defined as follows. Let \( K\left( {{U}_{1},{U}_{2}}\right) \) be the trace of the linear transformation

\[
W \mapsto  \mathcal{R}\left( {{U}_{1}, W}\right) {U}_{2}
\]

from \( T{M}_{p} \) to \( T{M}_{p} \) . (In classical terminology the tensor \( K \) is obtained from \( \mathcal{R} \) by contraction.) It follows easily from Lemma 9.3 that \( K \) is symmetric: \( K\left( {{U}_{1},{U}_{2}}\right)  = \; K\left( {{U}_{2},{U}_{1}}\right) \) .

The Ricci tensor is related to sectional curvature as follows. Let \( {U}_{1},\ldots ,{U}_{n} \) be an orthonormal basis for the tangent space \( T{M}_{p} \) .

Assertion 19.1. \( K\left( {{U}_{n},{U}_{n}}\right) \) is equal to the sum of the sectional curvatures \( \left\langle  {\mathcal{R}\left( {{U}_{n},{U}_{i}}\right) {U}_{n},{U}_{i}}\right\rangle \) for \( i = 1,2,\ldots , n - 1 \) .

Proof. By definition \( K\left( {{U}_{n},{U}_{n}}\right) \) is equal to the trace of the matrix \( \left( \left\langle  {\mathcal{R}\left( {{U}_{n},{U}_{i}}\right) {U}_{n},{U}_{i}}\right\rangle  \right) \) . Since the \( n \) -th diagonal term of this matrix is zero, we obtain a sum of \( n - 1 \) sectional curvatures, as asserted.

Theorem 19.5 (Myers [Mye41]). Suppose that the Ricci curvature \( K \) satisfies

\[
K\left( {U, U}\right)  \geq  \frac{\left( n - 1\right) }{{r}^{2}}
\]

for every unit vector \( U \) at every point of \( M \) ; where \( r \) is a positive constant. Then every geodesic on \( M \) of length \( > {\pi r} \) contains conjugate points; and hence is not minimal.

Proof. Let \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be a geodesic of length \( L \) . Choose parallel vector fields \( {P}_{1},\ldots ,{P}_{n} \) along \( \gamma \) which are orthonormal at one point, and hence are orthonormal everywhere along \( \gamma \) . We may assume that \( {P}_{n} \) points along \( \gamma \) , so that

\[
V = \frac{\mathrm{d}\gamma }{\mathrm{d}t} = L{P}_{n},\;\text{ and }\;\frac{\mathrm{D}{P}_{i}}{\mathrm{\;d}t} = 0.
\]

Let \( {W}_{i}\left( t\right)  = \left( {\sin \left( {\pi t}\right) }\right) {P}_{i}\left( t\right) \) . Then

\[
\frac{1}{2}{E}_{* * }\left( {{W}_{i},{W}_{i}}\right)  =  - {\int }_{0}^{1}\left\langle  {{W}_{i},\frac{{\mathrm{D}}^{2}{W}_{i}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( {V,{W}_{i}}\right) V}\right\rangle  \mathrm{d}t
\]

\[
= {\int }_{0}^{1}{\left( \sin \left( \pi t\right) \right) }^{2}\left( {{\pi }^{2} - {L}^{2}\left\langle  {\mathcal{R}\left( {{P}_{n},{P}_{i}}\right) {P}_{n},{P}_{i}}\right\rangle  }\right) \mathrm{d}t.
\]

Summing for \( i = 1,\ldots , n - 1 \) we obtain

\[
\frac{1}{2}\mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{E}_{* * }\left( {{W}_{i},{W}_{i}}\right)  = {\int }_{0}^{1}{\left( \sin \left( \pi t\right) \right) }^{2}\left( {\left( {n - 1}\right) {\pi }^{2} - {L}^{2}K\left( {{P}_{n},{P}_{n}}\right) }\right) \mathrm{d}t.
\]

Now if \( K\left( {{P}_{n},{P}_{n}}\right)  \geq  \left( {n - 1}\right) /{r}^{2} \) and \( L > {\pi r} \) then this expression is \( < 0 \) . Hence \( {E}_{* * }\left( {{W}_{i},{W}_{i}}\right)  < 0 \) for some \( i \) . This implies that the index of \( \gamma \) is positive, and hence, by the Index Theorem, that \( \gamma \) contains conjugate points.

It follows also that \( \gamma \) is not a minimal geodesic. In fact if \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) is a variation with variation vector field \( {W}_{i} \) then

\[
\frac{\mathrm{d}E\left( {\overline{\alpha }\left( u\right) }\right) }{\mathrm{d}u} = 0,\;\frac{{\mathrm{d}}^{2}E(\overline{\alpha }\left( u\right) }{\mathrm{d}{u}^{2}} < 0,
\]

for \( u = 0 \) . Hence \( E\left( {\overline{\alpha }\left( u\right) }\right)  < E\left( \gamma \right) \) for small values of \( u \neq  0 \) . This completes the proof.

Example 19.6. If \( M \) is a sphere of radius \( r \) then every sectional curvature is equal to \( 1/{r}^{2} \) . Hence \( K\left( {U, U}\right) \) takes the constant value \( \left( {n - 1}\right) /{r}^{2} \) . It follows from Theorem 19.5 that every geodesic of length \( > {\pi r} \) contains conjugate points: a best possible result.

Corollary 19.7. If \( M \) is complete, and \( K\left( {U, U}\right)  \geq  \left( {n - 1}\right) /{r}^{2} > 0 \) for all unit vectors \( U \) , then \( M \) is compact, with diameter \( \leq  {\pi r} \) .

Proof. If \( p, q \in  M \) let \( \gamma \) be a minimal geodesic from \( p \) to \( q \) . Then the length of \( \gamma \) must be \( \leq  {\pi r} \) . Therefore, all points have distance \( \leq  {\pi r} \) . Since closed bounded sets in a complete manifold are compact, it follows that \( M \) itself is compact.

This corollary applies also to the universal covering space \( \widetilde{M} \) of \( M \) . Since \( \widetilde{M} \) is compact, it follows that the fundamental group \( {\pi }_{1}\left( M\right) \) is finite. This assertion can be sharpened as follows.

Theorem 19.8. If \( M \) is a compact manifold, and if the Ricci tensor \( K \) of \( M \) is everywhere positive definite, then the path space \( \Omega \left( {M;p, q}\right) \) has the homotopy type of a CW-complex having only finitely many cells in each dimension.

Proof. Since the space consisting of all unit vectors \( U \) on \( M \) is compact, it follows that the continuous function \( K\left( {U, U}\right)  > 0 \) takes on a minimum, which we can denote by \( \left( {n - 1}\right) /{r}^{2} > 0 \) . Then every geodesic \( \gamma  \in  \Omega \left( {M;p, q}\right) \) of length \( > {\pi r} \) has index \( \lambda  \geq  1 \) .

More generally consider a geodesic \( \gamma \) of length \( > {k\pi r} \) . Then a similar argument shows that \( \gamma \) has index \( \lambda  \geq  k \) . In fact for each \( i = 1,2,\ldots , k \) one can construct a vector field \( {X}_{i} \) along \( \gamma \) which vanishes outside of the interval \( \left( {\left( {i - 1}\right) /k, i/k}\right) \) , and such that \( {E}_{* * }\left( {{X}_{i},{X}_{i}}\right)  < 0 \) .

Clearly \( {E}_{* * }\left( {{X}_{i},{X}_{j}}\right)  = 0 \) for \( i \neq  j \) ; so that \( {X}_{1},\ldots ,{X}_{k} \) span a \( k \) -dimensional subspace of \( T{\Omega }_{\gamma } \) on which \( {E}_{* * } \) is negative definite.

Now suppose that the points \( p \) and \( q \) are not conjugate along any geodesic. Then according to Theorem 16.3 there are only finitely many geodesics from \( p \) to \( q \) of length \( \leq  {k\pi r} \) . Hence there are only finitely many geodesics with index \( < k \) . Together with Theorem 17.3, this completes the proof.

Remark. I do not know whether or not this theorem remains true if \( M \) is allowed to be complete, but non-compact. The present proof certainly breaks down since, on a manifold such as the paraboloid \( z = {x}^{2} + {y}^{2} \) , the curvature \( K\left( {U, U}\right) \) will not be bounded away from zero.

It would be interesting to know which manifolds can carry a metric so that all sectional curvatures are positive. An instructive example is provided by the product \( {\mathbb{S}}^{m} \times  {\mathbb{S}}^{k} \) of two spheres; with \( m, k \geq  2 \) . For this manifold the Ricci tensor is everywhere positive definite. However, the sectional curvatures in certain directions (corresponding to flat tori \( {\mathbb{S}}^{1} \times  {\mathbb{S}}^{1} \subset  {\mathbb{S}}^{m} \times  {\mathbb{S}}^{k} \) ) are zero. It is not known whether or not \( {\mathbb{S}}^{m} \times  {\mathbb{S}}^{k} \) can be remetrized so that all sectional curvatures are positive. The following partial result is known: If such a new metric exists, then it can not be invariant under the involution \( \left( {x, y}\right)  \mapsto  \left( {-x, - y}\right) \) of \( {\mathbb{S}}^{m} \times  {\mathbb{S}}^{k} \) . This follows from a theorem of Synge. (See [Syn36]).

For other theorems relating topology and curvature, the following sources are useful: [YB53, Che55, Ber58, Gol62].

## Part IV Applications to Lie Groups and Symmetric Spaces
