## Chapter 10 Jacobi Fields

Our goal for the remainder of this book is to generalize to higher dimensions some of the geometric and topological consequences of the Gauss-Bonnet theorem. We need to develop a new approach: instead of using Stokes's theorem and differential forms to relate the curvature to global topology as in the proof of the Gauss-Bonnet theorem, we study the way that curvature affects the behavior of nearby geodesics. Roughly speaking, positive curvature causes nearby geodesics to converge, while negative curvature causes them to spread out (Fig. 10.1). In order to draw topological consequences from this fact, we need a quantitative way to measure the effect of curvature on a one-parameter family of geodesics.

We begin by deriving the Jacobi equation, which is an ordinary differential equation satisfied by the variation field of any one-parameter family of geodesics. A vector field satisfying this equation along a geodesic is called a Jacobi field. We then introduce conjugate points, which are pairs of points along a geodesic where some nontrivial Jacobi field vanishes. Intuitively, if \( p \) and \( q \) are conjugate along a geodesic, one expects to find a one-parameter family of geodesic segments that start at \( p \) and end (almost) at \( q \) .

After defining conjugate points, we prove a simple but essential fact: the points conjugate to \( p \) are exactly the points where \( {\exp }_{p} \) fails to be a local diffeomorphism. We then derive an expression for the second derivative of the length functional with respect to proper variations of a geodesic, called the second variation formula. Using this formula, we prove another essential fact about conjugate points: once a geodesic passes its first conjugate point, it is no longer minimizing. The converse of this statement, however, is untrue: a geodesic can cease to be minimizing before it reaches its first conjugate point. In the last section of the chapter, we study the set of points where geodesics starting at a given point \( p \) cease to minimize, called the cut locus of \( p \) .

In the next two chapters, we will derive geometric and topological consequences of these facts.

![bo_d7dtff491nqc73eq8m7g_294_262_190_1007_249_0.jpg](images/bo_d7dtff491nqc73eq8m7g_294_262_190_1007_249_0.jpg)

Fig. 10.1: Geodesics converge in positive curvature, and spread out in negative curvature

## The Jacobi Equation

Let \( \left( {M, g}\right) \) be an \( n \) -dimensional Riemannian or pseudo-Riemannian manifold. In order to study the effect of curvature on nearby geodesics, we focus on variations through geodesics. Suppose, therefore, that \( I, K \subseteq  \mathbb{R} \) are intervals, \( \gamma  : I \rightarrow  M \) is a geodesic, and \( \Gamma  : K \times  I \rightarrow  M \) is a variation of \( \gamma \) (as defined in Chapter 6). We say that \( \Gamma \) is a variation through geodesics if each of the main curves \( {\Gamma }_{s}\left( t\right)  = \Gamma \left( {s, t}\right) \) is also a geodesic. (In particular, this requires that \( \Gamma \) be smooth.) Our first goal is to derive an equation that must be satisfied by the variation field of a variation through geodesics.

Theorem 10.1 (The Jacobi Equation). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, let \( \gamma \) be a geodesic in \( M \) , and let \( J \) be a vector field along \( \gamma \) . If \( J \) is the variation field of a variation through geodesics, then \( J \) satisfies the following equation, called the Jacobi equation:

\[
{D}_{t}^{2}J + R\left( {J,{\gamma }^{\prime }}\right) {\gamma }^{\prime } = 0. \tag{10.1}
\]

Proof. Write \( T\left( {s, t}\right)  = {\partial }_{t}\Gamma \left( {s, t}\right) \) and \( S\left( {s, t}\right)  = {\partial }_{s}\Gamma \left( {s, t}\right) \) as in Chapter 6 . The geodesic equation tells us that

\[
{D}_{t}T \equiv  0
\]

for all \( \left( {s, t}\right) \) . We can take the covariant derivative of this equation with respect to \( s \) , yielding

\[
{D}_{s}{D}_{t}T \equiv  0
\]

Using Proposition 7.5 to commute the covariant derivatives along \( \Gamma \) , we compute

\[
0 = {D}_{s}{D}_{t}T
\]

\[
= {D}_{t}{D}_{s}T + R\left( {S, T}\right) T
\]

\[
= {D}_{t}{D}_{t}S + R\left( {S, T}\right) T,
\]

where the last step follows from the symmetry lemma. Evaluating at \( s = 0 \) , where \( S\left( {0, t}\right)  = J\left( t\right) \) and \( T\left( {0, t}\right)  = {\gamma }^{\prime }\left( t\right) \) , we get (10.1).

A smooth vector field along a geodesic that satisfies the Jacobi equation is called a Jacobi field. As the following proposition shows, the Jacobi equation can be written as a system of second-order linear ordinary differential equations, so it has a unique solution given initial values for \( J \) and \( {D}_{t}J \) at one point.

Proposition 10.2 (Existence and Uniqueness of Jacobi Fields). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold. Suppose \( I \subseteq  \mathbb{R} \) is an interval, \( \gamma  : I \rightarrow \; M \) is a geodesic, \( a \in  I \) , and \( p = \gamma \left( a\right) \) . For every pair of vectors \( v, w \in  {T}_{p}M \) , there is a unique Jacobi field \( J \) along \( \gamma \) satisfying the initial conditions

\[
J\left( a\right)  = v,\;{D}_{t}J\left( a\right)  = w.
\]

Proof. Choose a parallel orthonormal frame \( \left( {E}_{i}\right) \) along \( \gamma \) , and write \( v = {v}^{i}{E}_{i}\left( a\right) \) , \( w = {w}^{i}{E}_{i}\left( a\right) \) , and \( {\gamma }^{\prime }\left( t\right)  = {y}^{i}\left( t\right) {E}_{i}\left( t\right) \) in terms of this frame. Writing an unknown vector field \( J \in  \mathcal{X}\left( \gamma \right) \) as \( J\left( t\right)  = {J}^{i}\left( t\right) {E}_{i}\left( t\right) \) , we can express the Jacobi equation as

\[
{\ddot{J}}^{i}\left( t\right)  + {R}_{jkl}{}^{i}\left( {\gamma \left( t\right) }\right) {J}^{j}\left( t\right) {y}^{k}\left( t\right) {y}^{l}\left( t\right)  = 0.
\]

This is a system of \( n \) linear second-order ODEs for the \( n \) functions \( {J}^{i} : I \rightarrow  \mathbb{R} \) . Making the substitution \( {W}^{i} = {\dot{J}}^{i} \) converts it to the following equivalent first-order linear system for the \( {2n} \) unknown functions \( \left( {{J}^{i},{W}^{i}}\right) \) :

\[
{\dot{J}}^{i}\left( t\right)  = {W}^{i}\left( t\right)
\]

\[
{\dot{W}}^{i}\left( t\right)  =  - {R}_{jkl}{}^{i}\left( {\gamma \left( t\right) }\right) {J}^{j}\left( t\right) {y}^{k}\left( t\right) {y}^{l}\left( t\right) .
\]

Then Theorem 4.31 guarantees the existence and uniqueness of a smooth solution on the whole interval \( I \) with arbitrary initial conditions \( {J}^{i}\left( a\right)  = {v}^{i},{W}^{i}\left( a\right)  = {w}^{i} \) . Since \( {D}_{t}J\left( a\right)  = {\dot{J}}^{i}\left( a\right) {E}_{i}\left( a\right)  = {W}^{i}\left( a\right) {E}_{i}\left( a\right)  = w \) , it follows that \( J\left( t\right)  = {J}^{i}\left( t\right) {E}_{i}\left( t\right) \) is the desired Jacobi field.

Given a geodesic \( \gamma \) , let \( \mathcal{J}\left( \gamma \right)  \subseteq  \mathcal{X}\left( \gamma \right) \) denote the set of Jacobi fields along \( \gamma \) .

Corollary 10.3. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold of dimension \( n \) , and \( \gamma \) is any geodesic in \( M \) . Then \( \mathcal{J}\left( \gamma \right) \) is a \( {2n} \) -dimensional linear subspace of \( \mathfrak{X}\left( \gamma \right) \) .

Proof. Because the Jacobi equation is linear, \( \mathcal{J}\left( \gamma \right) \) is a linear subspace of \( \mathcal{X}\left( \gamma \right) \) . Let \( p = \gamma \left( a\right) \) be any point on \( \gamma \) , and consider the linear map from \( \mathcal{J}\left( \gamma \right) \) to \( {T}_{p}M \oplus  {T}_{p}M \) by sending \( J \) to \( \left( {J\left( a\right) ,{D}_{t}J\left( a\right) }\right) \) . The preceding proposition says precisely that this map is bijective.

The following proposition is a converse to Theorem 10.1; it shows that each Jacobi field along a geodesic segment tells us how some family of geodesics behaves, at least to first order along \( \gamma \) .

Proposition 10.4. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, and let \( \gamma  : I \rightarrow  M \) be a geodesic. If \( M \) is complete or \( I \) is a compact interval, then every Jacobi field along \( \gamma \) is the variation field of a variation of \( \gamma \) through geodesics.

Proof. Let \( J \) be a Jacobi field along \( \gamma \) . After applying a translation in \( t \) (which does not affect either the fact that \( \gamma \) is a geodesic or the fact that \( J \) is a Jacobi field), we can assume that the interval \( I \) contains 0, and write \( p = \gamma \left( 0\right) \) and \( v = {\gamma }^{\prime }\left( 0\right) \) . Note that this implies \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) for all \( t \in  I \) .

Choose a smooth curve \( \sigma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  M \) and a smooth vector field \( V \) along \( \sigma \) satisfying

\[
\sigma \left( 0\right)  = p,\;V\left( 0\right)  = v,
\]

\[
{\sigma }^{\prime }\left( 0\right)  = J\left( 0\right) ,\;{D}_{s}V\left( 0\right)  = {D}_{t}J\left( 0\right) ,
\]

where \( {D}_{s} \) and \( {D}_{t} \) denote covariant differentiation along \( \sigma \) and \( \gamma \) , respectively. (They are easily constructed in local coordinates around \( p \) .) We wish to define a variation of \( \gamma \) by setting

\[
\Gamma \left( {s, t}\right)  = {\exp }_{\sigma \left( s\right) }\left( {{tV}\left( s\right) }\right) . \tag{10.2}
\]

If \( M \) is geodesically complete, this is defined for all \( \left( {s, t}\right)  \in  \left( {-\varepsilon ,\varepsilon }\right)  \times  I \) . On the other hand, if \( I \) is compact, the fact that the domain of the exponential map is an open subset of \( {TM} \) that contains the compact set \( \{ \left( {p,{tv}}\right)  : t \in  I\} \) guarantees that there is some \( \delta  > 0 \) such that \( \Gamma \left( {s, t}\right) \) is defined for all \( \left( {s, t}\right)  \in  \left( {-\delta ,\delta }\right)  \times  I \) .

Note that

\[
\Gamma \left( {0, t}\right)  = {\exp }_{\sigma \left( 0\right) }\left( {{tV}\left( 0\right) }\right)  = {\exp }_{p}\left( {tv}\right)  = \gamma \left( t\right) , \tag{10.3}
\]

\[
\Gamma \left( {s,0}\right)  = {\exp }_{\sigma \left( s\right) }\left( 0\right)  = \sigma \left( s\right) . \tag{10.4}
\]

In particular,(10.3) shows that \( \Gamma \) is a variation of \( \gamma \) . The properties of the exponential map guarantee that \( \Gamma \) is a variation through geodesics, and therefore its variation field \( W\left( t\right)  = {\partial }_{s}\Gamma \left( {0, t}\right) \) is a Jacobi field along \( \gamma \) .

Now, (10.4) implies

\[
W\left( 0\right)  = {\left. \frac{\partial }{\partial s}\right| }_{s = 0}\Gamma \left( {s,0}\right)  = {\sigma }^{\prime }\left( 0\right)  = J\left( 0\right) .
\]

If we can show that \( {D}_{t}W\left( 0\right)  = {D}_{t}J\left( 0\right) \) as well, it then follows from the uniqueness of Jacobi fields that \( W \equiv  J \) , and the proposition is proved.

Formula (10.2) shows that each main curve \( {\Gamma }_{s}\left( t\right) \) is a geodesic whose initial velocity is \( V\left( s\right) \) , so

\[
{\partial }_{t}\Gamma \left( {s,0}\right)  = {\left. \frac{\partial }{\partial t}\right| }_{t = 0}{\Gamma }_{s}\left( t\right)  = V\left( s\right) .
\]

It follows from the symmetry lemma that \( {D}_{t}{\partial }_{s}\Gamma  = {D}_{s}{\partial }_{t}\Gamma \) , and our choice of \( V \) gives

\[
{D}_{t}W\left( 0\right)  = {D}_{t}{\partial }_{s}\Gamma \left( {0,0}\right)  = {D}_{s}{\partial }_{t}\Gamma \left( {0,0}\right)  = {D}_{s}V\left( 0\right)  = {D}_{t}J\left( 0\right) .
\]

It follows that \( W \equiv  J \) , as claimed.

![bo_d7dtff491nqc73eq8m7g_297_283_184_957_208_0.jpg](images/bo_d7dtff491nqc73eq8m7g_297_283_184_957_208_0.jpg)

Fig. 10.2: Tangential Jacobi fields

Proposition 10.5 (Local Isometry Invariance of Jacobi Fields). Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian or pseudo-Riemannian manifolds and \( \varphi  : M \rightarrow  \widetilde{M} \) is a local isometry. Let \( \gamma  : I \rightarrow  M \) and \( \widetilde{\gamma } : I \rightarrow  \widetilde{M} \) be geodesics related by \( \widetilde{\gamma } = \varphi  \circ  \gamma \) , and let \( J \in  \mathfrak{X}\left( \gamma \right) ,\widetilde{J} \in  \mathfrak{X}\left( \widetilde{\gamma }\right) \) be related by \( d{\varphi }_{\gamma \left( t\right) }\left( {J\left( t\right) }\right)  = \widetilde{J}\left( t\right) \) for all \( t \in  I \) . Then \( J \) is a Jacobi field if and only if \( \widetilde{J} \) is.

Exercise 10.6. Prove the preceding proposition.

## Basic Computations with Jacobi Fields

There are various situations in which Jacobi fields can be computed explicitly. We begin by describing the most important of these.

## Tangential and Normal Jacobi Fields

Along every geodesic \( \gamma  : I \rightarrow  M \) , there are always two Jacobi fields that we can write down immediately (see Fig. 10.2). Because \( {D}_{t}{\gamma }^{\prime } \equiv  0 \) and \( R\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) {\gamma }^{\prime } \equiv  0 \) by antisymmetry of \( R \) , the vector fields \( {J}_{0}\left( t\right)  = {\gamma }^{\prime }\left( t\right) \) and \( {J}_{1}\left( t\right)  = t{\gamma }^{\prime }\left( t\right) \) both satisfy the Jacobi equation by direct computation. If \( I \) is compact or \( M \) is complete, the vector field \( {J}_{0} \) is the variation field of the variation \( \Gamma \left( {s, t}\right)  = \gamma \left( {s + t}\right) \) , while \( {J}_{1} \) is the variation field of \( \Gamma \left( {s, t}\right)  = \gamma \left( {\left( {1 + s}\right) t}\right) \) . Therefore, these two Jacobi fields just reflect the possible reparametrizations of \( \gamma \) , and do not tell us anything about the behavior of geodesics other than \( \gamma \) itself.

To distinguish these trivial cases from more informative ones, we make the following definitions. Given a regular curve \( \gamma  : I \rightarrow  M \) , for each \( t \in  I \) we let \( {T}_{\gamma \left( t\right) }^{\top }M \subseteq  {T}_{\gamma \left( t\right) }M \) denote the one-dimensional subspace spanned by \( {\gamma }^{\prime }\left( t\right) \) , and \( {T}_{\gamma \left( t\right) }^{ \bot  }M \) its orthogonal complement. A tangential vector field along \( \gamma \) is a vector field \( V \in  \mathcal{X}\left( \gamma \right) \) such that \( V\left( t\right)  \in  {T}_{\gamma \left( t\right) }^{\top }M \) for all \( t \) , and a normal vector field along \( \mathbf{\gamma } \) is one such that \( V\left( t\right)  \in  {T}_{\gamma \left( t\right) }^{ \bot  }M \) for all \( t \) . Thus a normal Jacobi field along \( \mathbf{\gamma } \) is a Jacobi field \( J \) satisfying \( J\left( t\right)  \bot  {\gamma }^{\prime }\left( t\right) \) for all \( t \) . Let \( {\mathfrak{X}}^{ \bot  }\left( \gamma \right) \) and \( {\mathfrak{X}}^{\top }\left( \gamma \right) \) denote the spaces of smooth normal and tangential vector fields along \( \gamma \) , respectively. When \( \gamma \) is a geodesic, \( {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) and \( {\mathcal{J}}^{\top }\left( \gamma \right) \) denote the spaces of normal and tangential Jacobi fields along \( \gamma \) , respectively.

Proposition 10.7. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold. Suppose \( \gamma  : I \rightarrow  M \) is a geodesic and \( J \) is a Jacobi field along \( \gamma \) . Then the following are equivalent:

(a) \( J \) is a normal Jacobi field.

(b) \( J \) is orthogonal to \( {\gamma }^{\prime } \) at two distinct points.

(c) Both \( J \) and \( {D}_{t}J \) are orthogonal to \( {\gamma }^{\prime } \) at one point.

(d) Both \( J \) and \( {D}_{t}J \) are orthogonal to \( {\gamma }^{\prime } \) everywhere along \( \gamma \) .

Proof. Define a function \( f : I \rightarrow  \mathbb{R} \) by \( f\left( t\right)  = \left\langle  {J\left( t\right) ,{\gamma }^{\prime }\left( t\right) }\right\rangle \) , so that \( f\left( t\right)  = 0 \) if and only if \( J\left( t\right)  \bot  {\gamma }^{\prime }\left( t\right) \) . Using compatibility with the metric and the fact that \( {D}_{t}{\gamma }^{\prime } \equiv  0 \) , we compute

\[
{f}^{\prime \prime } = \left\langle  {{D}_{t}^{2}J,{\gamma }^{\prime }}\right\rangle
\]

\[
=  - \left\langle  {R\left( {J,{\gamma }^{\prime }}\right) {\gamma }^{\prime },{\gamma }^{\prime }}\right\rangle
\]

\[
=  - {Rm}\left( {J,{\gamma }^{\prime },{\gamma }^{\prime },{\gamma }^{\prime }}\right)  = 0
\]

by the symmetries of the curvature tensor. Thus, by elementary calculus, \( f \) is an affine function of \( t \) .

Note that \( {f}^{\prime }\left( t\right)  = \left\langle  {{D}_{t}J\left( t\right) ,{\gamma }^{\prime }\left( t\right) }\right\rangle \) , which vanishes at \( t \) if and only if \( {D}_{t}J\left( t\right)  \bot \; {\gamma }^{\prime }\left( t\right) \) . It follows that \( J\left( a\right) \) and \( {D}_{t}J\left( a\right) \) are orthogonal to \( {\gamma }^{\prime }\left( a\right) \) for some \( a \in  I \) if and only if \( f \) and its first derivative vanish at \( a \) , which happens if and only if \( f \equiv  0 \) . Similarly, \( J \) is orthogonal to \( {\gamma }^{\prime } \) at two points if and only if \( f \) vanishes at two points, which happens if and only if \( f \) is identically zero. If this is the case, then \( {f}^{\prime } \equiv  0 \) as well, which implies that both \( J \) and \( {D}_{t}J \) are orthogonal to \( {\gamma }^{\prime } \) for all \( t \) .

Corollary 10.8. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian n-manifold and \( \gamma  : I \rightarrow  M \) is any nonconstant geodesic. Then \( {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) is a \( \left( {{2n} - 2}\right) \) -dimensional subspace of \( {\mathcal{J}}_{1}\left( \gamma \right) \) , and \( {\mathcal{J}}^{\top }\left( \gamma \right) \) is a 2-dimensional subspace. Every Jacobi field can be uniquely decomposed as a sum of a tangential Jacobi field plus a normal Jacobi field.

Proof. As we noted in the proof of Corollary 10.3, for every \( a \in  I \) , the map from \( \mathcal{J}\left( \gamma \right) \) to \( {T}_{\gamma \left( a\right) }M \oplus  {T}_{\gamma \left( a\right) }M \) given by \( J \mapsto  \left( {J\left( a\right) ,{D}_{t}J\left( a\right) }\right) \) is an isomorphism, and Proposition 10.7 shows that \( {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) is exactly the preimage of the subspace consisting of all pairs \( \left( {v, w}\right)  \in  {T}_{\gamma \left( a\right) }M \oplus  {T}_{\gamma \left( a\right) }M \) such that \( \left\langle  {v,{\gamma }^{\prime }\left( a\right) }\right\rangle   = \left\langle  {w,{\gamma }^{\prime }\left( a\right) }\right\rangle   = 0 \) . Because this subspace has dimension \( {2n} - 2 \) , it follows that \( {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) has the same dimension.

On the other hand, \( {\mathcal{J}}^{\top }\left( \gamma \right) \) contains \( {J}_{0}\left( t\right)  = {\gamma }^{\prime }\left( t\right) \) and \( {J}_{1}\left( t\right)  = t{\gamma }^{\prime }\left( t\right) \) , which are linearly independent over \( \mathbb{R} \) because \( {\gamma }^{\prime }\left( t\right) \) never vanishes, so it is a subspace of dimension at least 2. Because \( {\mathcal{J}}^{ \bot  }\left( \gamma \right)  \cap  {\mathcal{J}}^{\top }\left( \gamma \right)  = \{ 0\} \) , the dimension of \( {\mathcal{J}}^{\top }\left( \gamma \right) \) must be exactly 2, and we have a direct sum decomposition \( \mathcal{J}\left( \gamma \right)  = {\mathcal{J}}^{ \bot  }\left( \gamma \right)  \oplus  {\mathcal{J}}^{\top }\left( \gamma \right) \) . This implies that every \( J \in  \mathcal{J}\left( \gamma \right) \) has a unique decomposition \( J = {J}^{ \bot  } + {J}^{\top } \) , with \( {J}^{ \bot  } \in  {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) and \( {J}^{\top } \in  {\mathcal{J}}^{\top }\left( \gamma \right) \) .

![bo_d7dtff491nqc73eq8m7g_299_354_184_830_621_0.jpg](images/bo_d7dtff491nqc73eq8m7g_299_354_184_830_621_0.jpg)

Fig. 10.3: The variation of Lemma 10.9

## Jacobi Fields Vanishing at a Point

For many purposes, we will be primarily interested in Jacobi fields that vanish at a particular point. For these, there are some useful explicit formulas.

Lemma 10.9. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, \( I \subseteq  \mathbb{R} \) an interval containing 0, and \( \gamma  : I \rightarrow  M \) a geodesic. Suppose \( J : I \rightarrow  M \) is a Jacobi field such that \( J\left( 0\right)  = 0 \) . If \( M \) is geodesically complete or \( I \) is compact, then \( J \) is the variation field of the following variation of \( \gamma \) through geodesics (Fig. 10.3):

\[
\Gamma \left( {s, t}\right)  = {\exp }_{p}\left( {t\left( {v + {sw}}\right) }\right) , \tag{10.5}
\]

where \( p = \gamma \left( 0\right) , v = {\gamma }^{\prime }\left( 0\right) \) , and \( w = {D}_{t}J\left( 0\right) \) .

Proof. The proof of Proposition 10.4 showed that \( J \) is the variation field of a variation \( \Gamma \) of the form (10.2), with \( \sigma \) any smooth curve satisfying \( \sigma \left( 0\right)  = p \) and \( {\sigma }^{\prime }\left( 0\right)  = 0 \) , and \( V \) a smooth vector field along \( \sigma \) with \( V\left( 0\right)  = v \) and \( {D}_{s}V\left( 0\right)  = w \) . In this case, we can take \( \sigma \left( s\right)  \equiv  p \) and \( V\left( s\right)  = v + {sw} \in  {T}_{p}M \) , yielding (10.5).

This result leads to some explicit formulas for all of the Jacobi fields vanishing at a point.

Proposition 10.10 (Jacobi Fields Vanishing at a Point). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian \( n \) -manifold and \( p \in  M \) . Suppose \( \gamma  : I \rightarrow  M \) is a geodesic such that \( 0 \in  I \) and \( \gamma \left( 0\right)  = p \) . For every \( w \in  {T}_{p}M \) , the Jacobi field \( J \) along \( \gamma \) such that \( J\left( 0\right)  = 0 \) and \( {D}_{t}J\left( 0\right)  = w \) is given by

\[
J\left( t\right)  = d{\left( {\exp }_{p}\right) }_{tv}\left( {tw}\right) , \tag{10.6}
\]

where \( v = {\gamma }^{\prime }\left( 0\right) \) , and we regard \( {tw} \) as an element of \( {T}_{tv}\left( {{T}_{p}M}\right) \) by means of the canonical identification \( {T}_{tv}\left( {{T}_{p}M}\right)  \cong  {T}_{p}M \) . If \( \left( {x}^{i}\right) \) are normal coordinates on a normal neighborhood of \( p \) containing the image of \( \gamma \) , then \( J \) is given by the formula

\[
J\left( t\right)  = {\left. t{w}^{i}{\partial }_{i}\right| }_{\gamma \left( t\right) }, \tag{10.7}
\]

![bo_d7dtff491nqc73eq8m7g_300_416_184_695_696_0.jpg](images/bo_d7dtff491nqc73eq8m7g_300_416_184_695_696_0.jpg)

Fig. 10.4: A Jacobi field in normal coordinates

where \( {\left. {w}^{i}{\partial }_{i}\right| }_{0} \) is the coordinate representation of \( w \) .

Proof. Under the given hypotheses, Lemma 10.9 showed that the restriction of \( J \) to any compact interval containing 0 is the variation field of a variation \( \Gamma \) through geodesics of the form (10.5). Using the chain rule to compute \( J\left( t\right)  = {\partial }_{s}\Gamma \left( {0, t}\right) \) , we arrive at (10.6). Because every \( t \) in the domain of \( \gamma \) is contained in some such compact interval, the formula holds for all such \( t \) .

In normal coordinates, the coordinate representation of the exponential map is the identity, so \( \Gamma \) can be written explicitly in coordinates as

\[
\Gamma \left( {s, t}\right)  = \left( {t\left( {{v}^{1} + s{w}^{1}}\right) ,\ldots , t\left( {{v}^{n} + s{w}^{n}}\right) }\right) .
\]

(See Fig. 10.4.) Differentiating \( \Gamma \left( {s, t}\right) \) with respect to \( s \) and setting \( s = 0 \) shows that its variation field \( J \) is given by (10.7).

Corollary 10.11. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold and \( U \) is a normal neighborhood of \( p \in  M \) . For each \( q \in  U \smallsetminus  \{ p\} \) , every vector in \( {T}_{q}M \) is the value of a Jacobi field \( J \) along a radial geodesic such that \( J \) vanishes at \( p \) .

![bo_d7dtff491nqc73eq8m7g_301_407_186_716_684_0.jpg](images/bo_d7dtff491nqc73eq8m7g_301_407_186_716_684_0.jpg)

Fig. 10.5: The graph of \( {s}_{c} \)

Proof. Let \( \left( {x}^{i}\right) \) be normal coordinates on \( U \) . Given \( q = \left( {{q}^{1},\ldots ,{q}^{n}}\right)  \in  U \smallsetminus  \{ p\} \) and \( w = {\left. {w}^{i}{\partial }_{i}\right| }_{q} \in  {T}_{q}M \) , the curve \( \gamma \left( t\right)  = \left( {t{q}^{1},\ldots , t{q}^{n}}\right) \) is a radial geodesic satisfying \( \gamma \left( 0\right)  = p \) and \( \gamma \left( 1\right)  = q \) . The previous proposition showed that \( J\left( t\right)  = {\left. t{w}^{i}{\partial }_{i}\right| }_{\gamma \left( t\right) } \) is a Jacobi field along \( \gamma \) . Because \( J\left( 0\right)  = 0 \) and \( J\left( 1\right)  = w \) , the result follows.

## Jacobi Fields in Constant-Curvature Spaces

For metrics with constant sectional curvature, we have a different kind of explicit formula for Jacobi fields-this one expresses a Jacobi field as a scalar multiple of a parallel vector field. To handle the various cases concisely, for each \( c \in  \mathbb{R} \) , let us define a function \( {s}_{c} : \mathbb{R} \rightarrow  \mathbb{R} \) (Fig. 10.5) by

\[
{s}_{c}\left( t\right)  = \left\{  \begin{array}{ll} t, & \text{ if }c = 0 \\  R\sin \frac{t}{R}, & \text{ if }c = \frac{1}{{R}^{2}} > 0 \\  R\sinh \frac{t}{R}, & \text{ if }c =  - \frac{1}{{R}^{2}} < 0 \end{array}\right. \tag{10.8}
\]

Proposition 10.12 (Jacobi Fields in Constant Curvature). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with constant sectional curvature \( c \) , and \( \gamma \) is a unit-speed geodesic in \( M \) . The normal Jacobi fields along \( \gamma \) vanishing at \( t = 0 \) are the vector fields of the form

\[
J\left( t\right)  = k{s}_{c}\left( t\right) E\left( t\right) , \tag{10.9}
\]

where \( E \) is any parallel unit normal vector field along \( \gamma , k \) is an arbitrary constant, and \( {s}_{c} \) is defined by (10.8). The initial derivative of such a Jacobi field is

\[
{D}_{t}J\left( 0\right)  = {kE}\left( 0\right) , \tag{10.10}
\]

and its norm is

\[
\left| {J\left( t\right) }\right|  = \left| {{s}_{c}\left( t\right) }\right| \left| {{D}_{t}J\left( 0\right) }\right| . \tag{10.11}
\]

Proof. Since \( g \) has constant curvature, its curvature endomorphism is given by the formula of Proposition 8.36:

\[
R\left( {v, w}\right) x = c\left( {\langle w, x\rangle v-\langle v, x\rangle w}\right) .
\]

Substituting this into the Jacobi equation, we find that a normal Jacobi field \( J \) satisfies

(10.12)

\[
0 = {D}_{t}^{2}J + c\left( {\left\langle  {{\gamma }^{\prime },{\gamma }^{\prime }}\right\rangle  J - \left\langle  {J,{\gamma }^{\prime }}\right\rangle  {\gamma }^{\prime }}\right)
\]

\[
= {D}_{t}^{2}J + {cJ},
\]

where we have used the facts that \( {\left| {\gamma }^{\prime }\right| }^{2} = 1 \) and \( \left\langle  {J,{\gamma }^{\prime }}\right\rangle   = 0 \) .

Since (10.12) says that the second covariant derivative of \( J \) is a multiple of \( J \) itself, it is reasonable to try to construct a solution by choosing an arbitrary parallel unit normal vector field \( E \) along \( \gamma \) and setting \( J\left( t\right)  = u\left( t\right) E\left( t\right) \) for some function \( u \) to be determined. Plugging this into (10.12), we find that \( J \) is a Jacobi field if and only if \( u \) is a solution to the differential equation

\[
{u}^{\prime \prime }\left( t\right)  + {cu}\left( t\right)  = 0.
\]

It is an easy matter to solve this ODE explicitly. In particular, the solutions satisfying \( u\left( 0\right)  = 0 \) are constant multiples of \( {s}_{c} \) . This construction yields all the normal Jacobi fields vanishing at 0, since there is an \( \left( {n - 1}\right) \) -dimensional space of them, and the space of parallel normal vector fields has the same dimension.

To prove the last two statements, suppose \( J \) is given by (10.9), and compute

\[
{D}_{t}J\left( 0\right)  = k{s}_{c}^{\prime }\left( 0\right) E\left( 0\right)  = {kE}\left( 0\right) ,
\]

since \( {s}_{c}^{\prime }\left( 0\right)  = 1 \) in every case. Because \( E \) is a unit vector field, \( \left| {{D}_{t}J\left( 0\right) }\right|  = \left| k\right| \) , and (10.11) follows.

Here is our first significant application of Jacobi fields. Because every tangent vector in a normal neighborhood is the value of a Jacobi field vanishing at the origin by Corollary 10.11, Proposition 10.12 yields explicit formulas for constant-curvature metrics in normal coordinates. To set the stage, we will rewrite the Euclidean metric on \( {\mathbb{R}}^{n} \) in a form that is somewhat more convenient for these computations.

Let \( \pi  : {\mathbb{R}}^{n} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{S}}^{n - 1} \) be the radial projection

\[
\pi \left( x\right)  = \frac{x}{\left| x\right| } \tag{10.13}
\]

and define a symmetric 2-tensor field on \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) by

\[
\widehat{g} = {\pi }^{ * }\overset{ \circ  }{g}, \tag{10.14}
\]

where \( \overset{ \circ  }{g} \) is the round metric of radius 1 on \( {\mathbb{S}}^{n - 1} \) .

Lemma 10.13. On \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) , the metric \( \widehat{g} \) defined by (10.14) and the Euclidean metric \( \bar{g} \) are related by

\[
\bar{g} = d{r}^{2} + {r}^{2}\widehat{g}, \tag{10.15}
\]

where \( r\left( x\right)  = \left| x\right| \) is the Euclidean distance from the origin.

Proof. Example 2.24 observed that the map \( \Phi  : {\mathbb{R}}^{ + }{ \times  }_{\rho }{\mathbb{S}}^{n - 1} \rightarrow  {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) given by

\[
\Phi \left( {\rho ,\omega }\right)  = {\rho \omega } \tag{10.16}
\]

is an isometry when \( {\mathbb{R}}^{ + }{ \times  }_{\rho }{\mathbb{S}}^{n - 1} \) has the warped product metric \( d{\rho }^{2} \oplus  {\rho }^{2}\overset{ \circ  }{g} \) and \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) has the Euclidean metric (see also Problem 2-4). Because \( {\Phi }^{-1}\left( x\right)  = \; \left( {r\left( x\right) ,\pi \left( x\right) }\right) \) , this means that \( \bar{g} = {\left( {\Phi }^{-1}\right) }^{ * }\left( {d{\rho }^{2} \oplus  {\rho }^{2}\overset{ \circ  }{g}}\right)  = d{r}^{2} + {r}^{2}\widehat{g} \) .

Theorem 10.14 (Constant-Curvature Metrics in Normal Coordinates). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with constant sectional curvature \( c \) . Given \( p \in  M \) , let \( \left( {x}^{i}\right) \) be normal coordinates on a normal neighborhood \( U \) of \( p \) ; let \( r \) be the radial distance function on \( U \) defined by (6.4); and let \( \widehat{g} \) be the symmetric 2-tensor defined in \( x \) -coordinates by (10.14). On \( U \smallsetminus  \{ p\} \) , the metric \( g \) can be written

\[
g = d{r}^{2} + {s}_{c}{\left( r\right) }^{2}\widehat{g}, \tag{10.17}
\]

where \( {s}_{c} \) is defined by (10.8).

Proof. Let \( \bar{g} \) denote the Euclidean metric in \( x \) -coordinates, and let \( {g}_{c} \) denote the metric defined by the formula on the right-hand side of (10.17). By the properties of normal coordinates, at points of \( U \smallsetminus  \{ p\} \) , all three metrics \( g,\bar{g} \) , and \( {g}_{c} \) make the radial vector field \( {\partial }_{r} \) a unit vector orthogonal to the level sets of \( r \) . Thus we need only show that \( g\left( {{w}_{1},{w}_{2}}\right)  = {g}_{c}\left( {{w}_{1},{w}_{2}}\right) \) when \( {w}_{1},{w}_{2} \) are tangent to a level set of \( r \) , and by polarization it suffices to show that \( g\left( {w, w}\right)  = {g}_{c}\left( {w, w}\right) \) for every such vector \( w \) . Note that if \( w \) is tangent to a level set \( r = b \) , then formulas (10.17) and (10.15) imply

\[
{g}_{c}\left( {w, w}\right)  = {s}_{c}{\left( b\right) }^{2}\widehat{g}\left( {w, w}\right)  = \frac{{s}_{c}{\left( b\right) }^{2}}{{b}^{2}}\bar{g}\left( {w, w}\right) .
\]

Let \( q \in  U \smallsetminus  \{ p\} \) and \( w \in  {T}_{q}M \) , and assume that \( w \) is tangent to the \( r \) -level set containing \( q \) . Let \( b = {d}_{g}\left( {p, q}\right) \) , and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) be the unit-speed radial geodesic from \( p \) to \( q \) , so the coordinate representation of \( \gamma \) is

\[
\gamma \left( t\right)  = \left( {\frac{t}{b}{q}^{1},\ldots ,\frac{t}{b}{q}^{n}}\right) ,
\]

where \( \left( {{q}^{1},\ldots ,{q}^{n}}\right) \) is the coordinate representation of \( q \) . Let \( J \in  \mathcal{X}\left( \gamma \right) \) be the vector field along \( \gamma \) given by

\[
J\left( t\right)  = {\left. \frac{t}{b}{w}^{i}{\partial }_{i}\right| }_{\gamma \left( t\right) }, \tag{10.18}
\]

![bo_d7dtff491nqc73eq8m7g_304_326_187_876_708_0.jpg](images/bo_d7dtff491nqc73eq8m7g_304_326_187_876_708_0.jpg)

Fig. 10.6: Local isometry constructed from normal coordinate charts

where \( {w}^{i}{\left. {\partial }_{i}\right| }_{q} \) is the coordinate representation for \( w \) . By Proposition 10.10, \( J \) is a Jacobi field satisfying \( {D}_{t}J\left( 0\right)  = \left( {1/b}\right) {w}^{i}{\left. {\partial }_{i}\right| }_{p} \) , and it follows from the definition that \( J\left( b\right)  = w \) . Because \( J \) is orthogonal to \( {\gamma }^{\prime } \) at \( p \) and \( q \) , it is normal by Proposition 10.7. Thus by Proposition 10.12,

\[
{\left| w\right| }_{g}^{2} = {\left| J\left( b\right) \right| }_{g}^{2} = {s}_{c}{\left( b\right) }^{2}{\left| {D}_{t}J\left( 0\right) \right| }_{g}^{2}
\]

\[
= {s}_{c}{\left( b\right) }^{2}\frac{1}{{b}^{2}}{\left| {w}^{i}{\partial }_{i}\right| }_{p}{\left. \right| }_{g}^{2} = {s}_{c}{\left( b\right) }^{2}\frac{1}{{b}^{2}}{\left| w\right| }_{\bar{g}}^{2} = {\left| w\right| }_{{g}_{c}}^{2}.
\]

Corollary 10.15 (Local Uniqueness of Constant-Curvature Metrics). Let \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) be Riemannian manifolds of the same dimension with constant sectional curvature \( c \) . For all points \( p \in  M,\widetilde{p} \in  \widetilde{M} \) , there exist neighborhoods \( U \) of \( p \) and \( \widetilde{U} \) of \( \widetilde{p} \) and an isometry \( \varphi  : U \rightarrow  \widetilde{U} \) .

Proof. Choose \( p \in  M \) and \( \widetilde{p} \in  \widetilde{M} \) , and let \( U \) and \( \widetilde{U} \) be geodesic balls of small radius \( \varepsilon \) around \( p \) and \( \widetilde{p} \) , respectively. Riemannian normal coordinates give maps \( \psi  : U \rightarrow  {B}_{\varepsilon }\left( 0\right)  \subseteq  {\mathbb{R}}^{n} \) and \( \widetilde{\psi } : \widetilde{U} \rightarrow  {B}_{\varepsilon }\left( 0\right)  \subseteq  {\mathbb{R}}^{n} \) , under which both metrics are given by formula (10.17) on the complement of the origin (Fig. 10.6). At the origin, \( {g}_{ij} = {\widetilde{g}}_{ij} = {\delta }_{ij} \) . Therefore \( {\widetilde{\psi }}^{-1} \circ  \psi \) is the required local isometry.

Corollary 10.16 (Constant-Curvature Metrics as Warped Products). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with constant sectional curvature \( c \) , and \( U \) is a geodesic ball of radius \( b \) centered at \( p \in  M \) . Then \( U \smallsetminus  \{ p\} \) is isometric to a warped product of the form \( \left( {0, b}\right) { \times  }_{{s}_{c}}{\mathbb{S}}^{n - 1} \) , where \( \left( {0, b}\right)  \subseteq  \mathbb{R} \) has the Euclidean metric, and \( {\mathbb{S}}^{n - 1} \) is the unit sphere with the round metric \( \overset{ \circ  }{g} \) .

Proof. By virtue of Theorem 10.14, we may consider \( g \) to be a metric on the ball of radius \( b \) in \( {\mathbb{R}}^{n} \) given by formula (10.17). Let \( \Phi  : \left( {0, b}\right)  \times  {\mathbb{S}}^{n - 1} \rightarrow  U \smallsetminus  \{ p\} \) and \( \pi  : {\mathbb{R}}^{n} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{S}}^{n - 1} \) be the maps defined by (10.16) and (10.13). Because \( \pi  \circ \; \Phi \) restricts to the identity on \( \{ \rho \}  \times  {\mathbb{S}}^{n - 1} \) for each fixed \( \rho \) , it follows that \( {\Phi }^{ * }\widehat{g} = \; {\Phi }^{ * }{\pi }^{ * }\overset{ \circ  }{g} = \overset{ \circ  }{g} \) , and thus

\[
{\Phi }^{ * }g = d{\rho }^{2} \oplus  {s}_{c}{\left( \rho \right) }^{2}\overset{ \circ  }{g}.
\]

The next corollary describes a formula for integration in polar coordinates with respect to a constant-curvature metric. It will be useful in our proofs of volume comparison theorems in the next chapter.

Corollary 10.17 (Polar Decomposition of Integrals). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with constant sectional curvature \( c \) , and \( U \) is an open or closed geodesic ball of radius \( b \) around a point \( p \in  M \) . If \( f : U \rightarrow  \mathbb{R} \) is any bounded integrable function, then the integral of \( f \) over \( U \) can be expressed as

\[
{\int }_{U}{fd}{V}_{g} = {\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{b}f \circ  \Phi \left( {\rho ,\omega }\right) {s}_{c}{\left( \rho \right) }^{n - 1}{d\rho d}{V}_{\overset{ \circ  }{g}},
\]

where \( d{V}_{g} \) is the Riemannian density of \( g \) , and \( \Phi  : \left( {0, b}\right)  \times  {\mathbb{S}}^{n - 1} \rightarrow  U \smallsetminus  \{ p\} \) is defined in normal coordinates by (10.16).

Proof. Because every geodesic ball is orientable, we might as well choose an orientation on \( U \) and interpret \( d{V}_{g} \) as a differential form. Since the boundary of a geodesic ball has measure zero, it does not matter whether \( U \) is open or closed. Similarly, integrating over \( U \smallsetminus  \{ p\} \) instead of \( U \) does not change the value of the integral. The claim therefore follows from Corollary 10.16 together with the result of Problem 2-15, which shows that the volume form of the warped product metric \( d{\rho }^{2} \oplus  {s}_{c}{\left( \rho \right) }^{2}\overset{ \circ  }{g} \) can be written \( {s}_{c}{\left( \rho \right) }^{n - 1}{d\rho } \land  d{V}_{g}^{ \circ  } \) .

## Locally Symmetric Spaces

Here is another application of the theory of Jacobi fields. Recall that a Riemannian manifold is a locally symmetric space if every \( p \in  M \) has a neighborhood that admits a point reflection at \( p \) . Problem 7-3 showed that every locally symmetric space has parallel curvature tensor. Now we can prove the converse. The key is the following lemma due to Élie Cartan. We will use the lemma again in Chapter 12 to prove a more global result (see Thm. 12.6).

Lemma 10.18. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with parallel curvature tensor, and for some points \( p,\widehat{p} \in  M \) we are given a linear map \( A : {T}_{p}M \rightarrow  {T}_{\widehat{p}}M \) satisfying \( {A}^{ * }\left( {g}_{\widehat{p}}\right)  = {g}_{p} \) and \( {A}^{ * }\left( {R{m}_{\widehat{p}}}\right)  = R{m}_{p} \) . Then there exist a neighborhood \( U \) of \( p \) and a local isometry \( \varphi  : U \rightarrow  M \) such that \( \varphi \left( p\right)  = \widehat{p} \) and \( d{\varphi }_{p} = A \) . If \( M \) is complete, then \( U \) can be taken to be any normal neighborhood of \( p \) .

Proof. The hypothesis means that \( \nabla {Rm} \equiv  0 \) , and because covariant differentiation commutes with raising and lowering indices, the curvature endomorphism is also parallel. If \( M \) is complete, let \( U \) be any normal neighborhood of \( p \) ; otherwise choose \( U = {B}_{\varepsilon }\left( p\right) \) , where \( \varepsilon  > 0 \) is chosen small enough that both \( {B}_{\varepsilon }\left( p\right) \) and \( {B}_{\varepsilon }\left( \widehat{p}\right) \) are geodesic balls. Our choice guarantees that \( \varphi  = {\exp }_{\widehat{p}} \circ  A \circ  {\exp }_{p}^{-1} \) is a smooth map from \( U \) into \( M \) , and it satisfies \( \varphi \left( p\right)  = \widehat{p} \) and \( d{\varphi }_{p} = A \) . We will show that \( {\left| d{\varphi }_{q}\left( x\right) \right| }_{g} = {\left| x\right| }_{g} \) for every tangent vector \( x \) at every point \( q \in  U \) . It then follows by polarization that \( {\left\langle  d{\varphi }_{q}\left( x\right) , d{\varphi }_{q}\left( y\right) \right\rangle  }_{g} = \langle x, y{\rangle }_{g} \) for all \( x, y \in  {T}_{q}M \) , and thus \( {\varphi }^{ * }g = g \) .

Because \( d{\varphi }_{p} = A \) is a linear isometry, we have \( {\left| d{\varphi }_{p}\left( x\right) \right| }_{g} = {\left| x\right| }_{g} \) for \( x \in  {T}_{p}M \) , so we need only consider points \( q \neq  p \) . Let \( q \in  U \smallsetminus  \{ p\} \) and \( x \in  {T}_{q}M \) be arbitrary. Let \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  U \) be the radial geodesic from \( p \) to \( q \) , given explicitly by \( \gamma \left( t\right)  = \; {\exp }_{p}\left( {tv}\right) \) for some \( v \in  {T}_{p}M \) . It follows from Corollary 10.11 that there is a Jacobi field \( J \) along \( \gamma \) such that \( J\left( 0\right)  = 0 \) and \( J\left( 1\right)  = x \) ; and Proposition 10.10 shows that it is of the form \( J\left( t\right)  = d{\left( {\exp }_{p}\right) }_{tv}\left( {tw}\right) \) for some \( w \in  {T}_{p}M \) . Let \( \widehat{v} = A\left( v\right) \) and \( \widehat{w} = A\left( w\right)  \in  {T}_{\widehat{p}}M \) , and define \( \widehat{\gamma }\left( t\right)  = {\exp }_{\widehat{p}}\left( {t\widehat{v}}\right) \) and \( \widehat{J}\left( t\right)  = d{\left( {\exp }_{\widehat{p}}\right) }_{t\widehat{v}}\left( {t\widehat{w}}\right) \) for \( t \in  \left\lbrack  {0,1}\right\rbrack \) . Then \( \widehat{\gamma } \) is a geodesic from \( \widehat{p} = \varphi \left( p\right) \) to \( \varphi \left( q\right) \) , and \( \widehat{J} \) is a Jacobi field along \( \widehat{\gamma } \) . It follows from the definition of \( \varphi \) and the chain rule (using the fact that \( d{A}_{v} = A \) because \( A \) is linear) that \( d{\varphi }_{q} \circ  d{\left( {\exp }_{p}\right) }_{v} = d{\left( {\exp }_{\widehat{p}}\right) }_{\widehat{v}} \circ  A \) , and thus

\[
\widehat{J}\left( 1\right)  = d{\left( {\exp }_{\widehat{p}}\right) }_{\widehat{v}}\left( \widehat{w}\right)  = d{\left( {\exp }_{\widehat{p}}\right) }_{\widehat{v}} \circ  A\left( w\right)
\]

\[
= d{\varphi }_{q} \circ  d{\left( {\exp }_{p}\right) }_{v}\left( w\right)  = d{\varphi }_{q}\left( {J\left( 1\right) }\right)  = d{\varphi }_{q}\left( x\right) ,
\]

so to prove the theorem it suffices to show that \( {\left| \widehat{J}\left( 1\right) \right| }_{g} = {\left| J\left( 1\right) \right| }_{g} \) .

Let \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be a parallel orthonormal frame along \( \gamma \) , and let \( \left( {{\widehat{E}}_{1},\ldots ,{\widehat{E}}_{n}}\right) \) be the parallel orthonormal frame along \( \widehat{\gamma } \) such that \( {\widehat{E}}_{i}\left( 0\right)  = A\left( {{E}_{i}\left( 0\right) }\right) \) . At points of \( \gamma \) , we can express the curvature endomorphism in terms of the frame \( \left( {E}_{i}\right) \) as

\[
R\left( {{E}_{i}\left( t\right) ,{E}_{j}\left( t\right) }\right) {E}_{k}\left( t\right)  = {R}_{ijk}{}^{l}\left( t\right) {E}_{l}\left( t\right) ,
\]

for some smooth functions \( {R}_{ijk}{}^{l} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R} \) . The parallel curvature hypothesis and the fact that each \( {E}_{i} \) is parallel imply

\[
0 = \left( {{D}_{t}R}\right) \left( {{E}_{i}\left( t\right) ,{E}_{j}\left( t\right) }\right) {E}_{k}\left( t\right)  = {D}_{t}\left( {R\left( {{E}_{i}\left( t\right) ,{E}_{j}\left( t\right) }\right) {E}_{k}\left( t\right) }\right)  = {\left( {R}_{ijk}{}^{l}\right) }^{\prime }\left( t\right) {E}_{l}\left( t\right) ,
\]

so in fact the coefficients \( {R}_{ijk}{}^{l}\left( t\right) \) are constant in \( t \) . The same argument shows that the curvature endomorphism has constant coefficients along \( \widehat{\gamma } \) in terms of the frame \( \left( {\widehat{E}}_{i}\right) \) . Because our hypotheses guarantee that the coefficients of the two curvature endomorphisms agree at \( t = 0 \) , they are in fact the same constants along both geodesics; we write those constants henceforth as \( {R}_{ijk}{}^{l} \) .

Also, we can write \( J\left( t\right)  = {J}^{i}\left( t\right) {E}_{i}\left( t\right) \) and \( \widehat{J}\left( t\right)  = {\widehat{J}}^{i}\left( t\right) {\widehat{E}}_{i}\left( t\right) \) for some smooth functions \( {J}^{i},{\widehat{J}}^{i} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R} \) . The Jacobi equations for \( J \) and \( \widehat{J} \) , written in terms of our parallel frames, read

\[
{\left( {J}^{l}\right) }^{\prime \prime }\left( t\right)  + {R}_{ijk}{}^{l}{J}^{i}\left( t\right) {v}^{j}{v}^{k} = 0,
\]

\[
{\left( {\widehat{J}}^{l}\right) }^{\prime \prime }\left( t\right)  + {R}_{ijk}{}^{l}{\widehat{J}}^{i}\left( t\right) {v}^{j}{v}^{k} = 0.
\]

Proposition 10.10 shows that \( {D}_{t}J\left( 0\right)  = w \) , which we can write as \( w = {w}^{l}{E}_{l}\left( 0\right) \) . It also follows that \( {\widehat{D}}_{t}\widehat{J}\left( 0\right)  = \widehat{w} = A\left( w\right)  = {w}^{l}{\widehat{E}}_{l}\left( 0\right) \) , so the functions \( {J}^{l} \) and \( {\widehat{J}}^{l} \) satisfy the same system of differential equations with the same initial conditions \( {J}^{l}\left( 0\right)  = {\widehat{J}}^{l}\left( 0\right)  = 0 \) and \( {\left( {J}^{l}\right) }^{\prime }\left( 0\right)  = {\left( {\widehat{J}}^{l}\right) }^{\prime }\left( 0\right)  = {w}^{l} \) . Uniqueness of ODE solutions implies \( {J}^{l}\left( t\right)  = {\widehat{J}}^{l}\left( t\right) \) for all \( t \) , and in particular \( {J}^{l}\left( 1\right)  = {\widehat{J}}^{l}\left( 1\right) \) . Because the frames \( \left( {E}_{i}\right) \) and \( \left( {\widehat{E}}_{i}\right) \) are orthonormal, we have

\[
{\left| J\left( 1\right) \right| }_{g}^{2} = \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {J}^{i}\left( 1\right) \right) }^{2} = \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {\widehat{J}}^{i}\left( 1\right) \right) }^{2} = {\left| \widehat{J}\left( 1\right) \right| }_{g}^{2},
\]

thus completing the proof.

Theorem 10.19 (Characterization of Locally Symmetric Spaces). A Riemannian manifold is a locally symmetric space if and only if its curvature tensor is parallel.

Proof. One direction is taken care of by Problem 7-3. To prove the converse, suppose \( \left( {M, g}\right) \) is a Riemannian manifold with \( \nabla {Rm} \equiv  0 \) . Let \( p \in  M \) be arbitrary, and let \( U \) be a geodesic ball centered at \( p \) . The linear map \( A =  - \operatorname{Id} : {T}_{p}M \rightarrow  {T}_{p}M \) satisfies \( {A}^{ * }{g}_{p} = {g}_{p} \) , and for all \( w, x, y, z \in  {T}_{p}M \) , we have

\[
\left( {{A}^{ * }R{m}_{p}}\right) \left( {w, x, y, z}\right)  = R{m}_{p}\left( {-w, - x, - y, - z}\right)  = R{m}_{p}\left( {w, x, y, z}\right) .
\]

It follows that \( A =  - \mathrm{{Id}} \) satisfies the hypotheses of Lemma 10.18 with \( p = \widehat{p} \) , and thus there is a local isometry \( \varphi  : U \rightarrow  M \) such that \( \varphi \left( p\right)  = p \) and \( d{\varphi }_{p} =  - \) Id. Since a local isometry takes geodesics to geodesics, \( \varphi \left( U\right) \) is also a geodesic ball centered at \( p \) of the same radius as \( U \) , so \( \varphi \) actually maps \( U \) to \( U \) . If we take the radius of \( U \) small enough, then \( \varphi \) is an isometry from \( U \) to itself.

## Conjugate Points

Our next application of Jacobi fields is to study the question of when the exponential map is a local diffeomorphism.

Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold and \( p \in  M \) . The restricted exponential map \( {\exp }_{p} \) is defined on an open subset \( {\mathcal{E}}_{p} \subseteq  {T}_{p}M \) , and because it is a smooth map between manifolds of the same dimension, the inverse function theorem guarantees that it is a local diffeomorphism in a neighborhood of each of its regular points (points \( v \in  {T}_{p}M \) where \( d{\left( {\exp }_{p}\right) }_{v} \) is surjective and thus invertible). To see where this fails, we need to identify the critical points of \( {\exp }_{p} \) (the points where its differential is singular). Proposition 5.19(d) guarantees that 0 is a regular point, but it may well happen that it has critical points elsewhere in \( {\mathcal{E}}_{p} \) .

![bo_d7dtff491nqc73eq8m7g_308_375_185_782_568_0.jpg](images/bo_d7dtff491nqc73eq8m7g_308_375_185_782_568_0.jpg)

Fig. 10.7: The exponential map of the sphere

![bo_d7dtff491nqc73eq8m7g_308_287_878_862_278_0.jpg](images/bo_d7dtff491nqc73eq8m7g_308_287_878_862_278_0.jpg)

Fig. 10.8: Conjugate points

An enlightening example is provided by the sphere \( {\mathbb{S}}^{n}\left( R\right) \) (Fig. 10.7). All geodesics starting at a given point \( p \) meet at the antipodal point, which is at a distance of \( {\pi R} \) along each geodesic. The exponential map is a diffeomorphism on the ball \( {B}_{\pi R}\left( 0\right)  \subseteq  {T}_{p}{\mathbb{S}}^{n}\left( R\right) \) , but every point on the boundary of that ball is a critical point. Moreover, Proposition 10.12 shows that each Jacobi field on \( {\mathbb{S}}^{n}\left( R\right) \) vanishing at \( p \) has its first zero precisely at distance \( {\pi R} \) .

On the other hand, formula (10.7) shows that if \( U \) is a normal neighborhood of \( p \) (the image of a star-shaped open set on which \( {\exp }_{p} \) is a diffeomorphism), then no Jacobi field that vanishes at \( p \) can vanish at any other point in \( U \) . We might thus be led to expect a relationship between zeros of Jacobi fields and critical points of the exponential map.

Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, \( \gamma  : I \rightarrow  M \) a geodesic, and \( p = \gamma \left( a\right) , q = \gamma \left( b\right) \) for some \( a, b \in  I \) . We say that \( p \) and \( q \) are conjugate along \( \gamma \) if there is a Jacobi field along \( \gamma \) vanishing at \( t = a \) and \( t = b \) but not identically zero (Fig. 10.8). The order (or multiplicity) of conjugacy is the dimension of the space of Jacobi fields vanishing at \( a \) and \( b \) . From the existence and uniqueness theorem for Jacobi fields, there is an \( n \) -dimensional space of Jacobi fields that vanish at \( a \) ; since tangential Jacobi fields vanish at most at one point, the order of conjugacy of two points along \( \gamma \) can be at most \( n - 1 \) . This bound is sharp: Proposition 10.12 shows that if \( \gamma \) is a geodesic joining antipodal points \( p \) and \( q \) on \( {\mathbb{S}}^{n}\left( R\right) \) , then there is a Jacobi field vanishing at \( p \) and \( q \) for each parallel normal vector field along \( \gamma \) ; thus in that case \( p \) and \( q \) are conjugate to order exactly \( n - 1 \) .

The most important fact about conjugate points is that they are the images of critical points of the exponential map, as the following proposition shows.

Proposition 10.20. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold, \( p \in  M \) , and \( v \in  {\mathcal{E}}_{p} \subseteq  {T}_{p}M \) . Let \( \gamma  = {\gamma }_{v} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be the geodesic segment \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) , and let \( q = \gamma \left( 1\right)  = {\exp }_{p}\left( v\right) \) . Then \( v \) is a critical point of \( {\exp }_{p} \) if and only if \( q \) is conjugate to \( p \) along \( \gamma \) .

Proof. Suppose first that \( v \) is a critical point of \( {\exp }_{p} \) . Then there is a nonzero vector \( w \in  {T}_{v}\left( {{T}_{p}M}\right) \) such that \( d{\left( {\exp }_{p}\right) }_{v}\left( w\right)  = 0 \) . Because \( {T}_{p}M \) is a vector space, we can identify \( {T}_{v}\left( {{T}_{p}M}\right) \) with \( {T}_{p}M \) as usual and regard \( w \) as a vector in \( {T}_{p}M \) . Let \( \Gamma \) be the variation of \( \gamma \) defined by (10.5), and let \( J\left( t\right)  = {\partial }_{s}\Gamma \left( {0, t}\right) \) be its variation field. We can compute \( J\left( 1\right) \) as follows:

\[
J\left( 1\right)  = {\partial }_{s}\Gamma \left( {0,1}\right)  = {\left. \frac{\partial }{\partial s}\right| }_{s = 0}{\exp }_{p}\left( {v + {sw}}\right)  = d{\left( {\exp }_{p}\right) }_{v}\left( w\right)  = 0.
\]

Thus \( J \) is a nontrivial Jacobi field vanishing at \( t = 0 \) and \( t = 1 \) , so \( q \) is conjugate to \( p \) along \( \gamma \) .

Conversely, if \( q \) is conjugate to \( p \) along \( \gamma \) , then there is some nontrivial Jacobi field \( J \) along \( \gamma \) such that \( J\left( 0\right)  = 0 \) and \( J\left( 1\right)  = 0 \) . Lemma 10.9 shows that \( J \) is the variation field of a variation of \( \gamma \) of the form (10.5) with \( w = {D}_{t}J\left( 0\right)  \in  {T}_{p}M \) , and the computation in the preceding paragraph shows that \( d{\left( {\exp }_{p}\right) }_{v}\left( w\right)  = J\left( 1\right)  = 0 \) . Thus \( v \) is a critical point for \( {\exp }_{p} \) .

As Proposition 10.2 shows, the "natural" way to specify a unique Jacobi field is by giving its initial value and initial derivative. However, in Corollary 10.11 and Proposition 10.20, we had to construct Jacobi fields along a geodesic satisfying \( J\left( 0\right)  = 0 \) and \( J\left( 1\right)  = w \) for some specific vector \( w \) . More generally, one can pose the two-point boundary problem for Jacobi fields: given \( v \in  {T}_{\gamma \left( a\right) }M \) and \( w \in  {T}_{\gamma \left( b\right) }M \) , find a Jacobi field \( J \) along \( \gamma \) such that \( J\left( a\right)  = v \) and \( J\left( b\right)  = w \) . Another interesting property of conjugate points is that they are the obstructions to solving the two-point boundary problem, as the next proposition shows.

Proposition 10.21 (The Two-Point Boundary Problem for Jacobi Fields). Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold, and \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a geodesic segment. The two-point boundary problem for Jacobi fields along \( \gamma \) is uniquely solvable for every pair of vectors \( v \in  {T}_{\gamma \left( a\right) }M \) and \( w \in  {T}_{\gamma \left( b\right) }M \) if and only if \( \gamma \left( a\right) \) and \( \gamma \left( b\right) \) are not conjugate along \( \gamma \) .

## The Second Variation Formula

Our next task is to study the question of which geodesic segments are minimizing. In the remainder of the chapter, because of the complications involved in studying lengths on pseudo-Riemannian manifolds, we restrict our attention to the Riemannian case.

In our proof that every minimizing curve is a geodesic, we imitated the first-derivative test of elementary calculus: if a geodesic \( \gamma \) is minimizing, then the first derivative of the length functional must vanish for every proper variation of \( \gamma \) . Now we imitate the second-derivative test: if \( \gamma \) is minimizing, the second derivative must be nonnegative. First, we must compute this second derivative. In keeping with classical terminology, we call it the second variation of the length functional.

Theorem 10.22 (Second Variation Formula). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold. Let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a unit-speed geodesic segment, \( \Gamma  : J \times  \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) a proper variation of \( \gamma \) , and \( V \) its variation field. The second variation of \( {L}_{g}\left( {\Gamma }_{s}\right) \) is given by the following formula:

\[
{\left. \frac{{d}^{2}}{d{s}^{2}}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  = {\int }_{a}^{b}\left( {{\left| {D}_{t}{V}^{ \bot  }\right| }^{2} - \operatorname{Rm}\left( {{V}^{ \bot  },{\gamma }^{\prime },{\gamma }^{\prime },{V}^{ \bot  }}\right) }\right) {dt}, \tag{10.19}
\]

where \( {V}^{ \bot  } \) is the normal component of \( V \) .

Proof. As usual, write \( T = {\partial }_{t}\Gamma \) and \( S = {\partial }_{s}\Gamma \) , and let \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) be an admissible partition for \( \Gamma \) . We begin, as we did when computing the first variation formula, by restricting to a rectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) where \( \Gamma \) is smooth. From (6.3) we have, for every \( s \) ,

\[
\frac{d}{ds}{L}_{g}\left( {\left. {\Gamma }_{s}\right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  }\right)  = {\int }_{{a}_{i - 1}}^{{a}_{i}}\frac{\langle {D}_{t}S, T\rangle }{\langle T, T{\rangle }^{1/2}}{dt}.
\]

Differentiating again with respect to \( s \) , and using the symmetry lemma and Proposition 7.5, we obtain

\[
\frac{{d}^{2}}{d{s}^{2}}{L}_{g}\left( {\left. {\Gamma }_{s}\right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  }\right)
\]

\[
= {\int }_{{a}_{i - 1}}^{{a}_{i}}\left( {\frac{\left\langle  {D}_{s}{D}_{t}S, T\right\rangle  }{\langle T, T{\rangle }^{1/2}} + \frac{\left\langle  {D}_{t}S,{D}_{s}T\right\rangle  }{\langle T, T{\rangle }^{1/2}} - \frac{1}{2}\frac{\left\langle  {{D}_{t}S, T}\right\rangle  2\left\langle  {{D}_{s}T, T}\right\rangle  }{\langle T, T{\rangle }^{3/2}}}\right) {dt}
\]

\[
= {\int }_{{a}_{i - 1}}^{{a}_{i}}\left( {\frac{\left\langle  {{D}_{t}{D}_{s}S + R\left( {S, T}\right) S, T}\right\rangle  }{\left| T\right| } + \frac{\left\langle  {D}_{t}S,{D}_{t}S\right\rangle  }{\left| T\right| } - \frac{{\left\langle  {D}_{t}S, T\right\rangle  }^{2}}{{\left| T\right| }^{3}}}\right) {dt}.
\]

Now restrict to \( s = 0 \) , where \( \left| T\right|  = 1 \) :

\[
{\left. \frac{{d}^{2}}{d{s}^{2}}\right| }_{s = 0}{L}_{g}\left( {\left. {\Gamma }_{s}\right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  }\right)  = {\int }_{{a}_{i - 1}}^{{a}_{i}}\left( {\left\langle  {{D}_{t}{D}_{s}S, T}\right\rangle   - {Rm}\left( {S, T, T, S}\right) }\right. \tag{10.20}
\]

\[
+ {\left. {\left| {D}_{t}S\right| }^{2} - {\left\langle  {D}_{t}S, T\right\rangle  }^{2})dt\right| }_{s = 0}\text{ . }
\]

Because \( {D}_{t}T = {D}_{t}{\gamma }^{\prime } = 0 \) when \( s = 0 \) , the first term in (10.20) can be integrated as follows:

\[
{\int }_{{a}_{i - 1}}^{{a}_{i}}\left\langle  {{D}_{t}{D}_{s}S, T}\right\rangle  {dt} = {\left. {\int }_{{a}_{i - 1}}^{{a}_{i}}\frac{d}{dt}\left\langle  {D}_{s}S, T\right\rangle  dt = \left\langle  {D}_{s}S, T\right\rangle  \right| }_{t = {a}_{i - 1}}^{t = {a}_{i}}. \tag{10.21}
\]

Notice that \( S\left( {s, t}\right)  = 0 \) for all \( s \) at the endpoints \( t = {a}_{0} = a \) and \( t = {a}_{k} = b \) because \( \Gamma \) is a proper variation, so \( {D}_{s}S = 0 \) there. Moreover, along the boundaries \( \left\{  {t = {a}_{i}}\right\} \) of the smooth regions, \( {D}_{s}S = {D}_{s}\left( {{\partial }_{s}\Gamma }\right) \) depends only on the values of \( \Gamma \) when \( t = {a}_{i} \) , and it is smooth up to the line \( \left\{  {t = {a}_{i}}\right\} \) from both sides; therefore \( {D}_{s}S \) is continuous for all \( \left( {s, t}\right) \) . Thus when we insert (10.21) into (10.20) and sum over \( i \) , the boundary contributions from the first term all cancel, and we get

\[
{\left. \frac{{d}^{2}}{d{s}^{2}}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  = {\left. {\int }_{a}^{b}\left( {\left| {D}_{t}S\right| }^{2}-\langle {D}_{t}S, T{\rangle }^{2} - \operatorname{Rm}\left( S, T, T, S\right) \right) dt\right| }_{s = 0} \tag{10.22}
\]

\[
= {\int }_{a}^{b}\left( {{\left| {D}_{t}V\right| }^{2} - {\left\langle  {D}_{t}V,{\gamma }^{\prime }\right\rangle  }^{2} - \operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) }\right) {dt}.
\]

Every vector field \( V \) along \( \gamma \) can be written uniquely as \( V = {V}^{\top } + {V}^{ \bot  } \) , where \( {V}^{\top } \) is tangential and \( {V}^{ \bot  } \) is normal. Explicitly,

\[
{V}^{\top } = \left\langle  {V,{\gamma }^{\prime }}\right\rangle  {\gamma }^{\prime };\;{V}^{ \bot  } = V - {V}^{\top }.
\]

Because \( {D}_{t}{\gamma }^{\prime } = 0 \) , it follows that

\[
{D}_{t}\left( {V}^{\top }\right)  = \left\langle  {{D}_{t}V,{\gamma }^{\prime }}\right\rangle  {\gamma }^{\prime } = {\left( {D}_{t}V\right) }^{\top };\;{D}_{t}\left( {V}^{ \bot  }\right)  = {\left( {D}_{t}V\right) }^{ \bot  }.
\]

Therefore,

\[
{\left| {D}_{t}V\right| }^{2} = {\left| {\left( {D}_{t}V\right) }^{\top }\right| }^{2} + {\left| {\left( {D}_{t}V\right) }^{ \bot  }\right| }^{2} = {\left\langle  {D}_{t}V,{\gamma }^{\prime }\right\rangle  }^{2} + {\left| {D}_{t}{V}^{ \bot  }\right| }^{2}.
\]

Also, the fact that \( \operatorname{Rm}\left( {{\gamma }^{\prime },{\gamma }^{\prime },\cdot , \cdot  }\right)  = \operatorname{Rm}\left( {\cdot ,\cdot ,{\gamma }^{\prime },{\gamma }^{\prime }}\right)  = 0 \) implies

\[
\operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right)  = \operatorname{Rm}\left( {{V}^{ \bot  },{\gamma }^{\prime },{\gamma }^{\prime },{V}^{ \bot  }}\right) .
\]

Substituting these relations into (10.22) gives (10.19).

It should come as no surprise that the second variation depends only on the normal component of \( V \) , because the tangential component of \( V \) contributes only to a reparametrization of \( \gamma \) , and length is independent of parametrization. For this reason, we will generally restrict our attention to variations of the following type: if \( \gamma \) is an admissible curve, a variation of \( \gamma \) is called a normal variation if its variation field is a normal vector field along \( \gamma \) .

Given a geodesic segment \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) , we define a symmetric bilinear form \( I \) , called the index form of \( \gamma \) , on the space of normal vector fields along \( \gamma \) by

\[
I\left( {V, W}\right)  = {\int }_{a}^{b}\left( {\left\langle  {{D}_{t}V,{D}_{t}W}\right\rangle   - \operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, W}\right) }\right) {dt}. \tag{10.23}
\]

You should think of \( I\left( {V, W}\right) \) as a sort of "Hessian" or second derivative of the length functional. Because every proper normal vector field along \( \gamma \) is the variation field of some proper normal variation, the preceding theorem can be rephrased in terms of the index form in the following way.

Corollary 10.23. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold. Let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a unit-speed geodesic, \( \Gamma \) a proper normal variation of \( \gamma \) , and \( V \) its variation field. The second variation of \( {L}_{g}\left( {\Gamma }_{s}\right) \) is \( I\left( {V, V}\right) \) . If \( \gamma \) is minimizing, then \( I\left( {V, V}\right)  \geq  0 \) for every proper normal vector field along \( \gamma \) .

The next proposition gives another expression for \( I \) , which makes the role of the Jacobi equation more evident.

Proposition 10.24. Let \( \left( {M, g}\right) \) be a Riemannian manifold and let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a geodesic segment. For every pair of piecewise smooth normal vector fields \( V, W \) along \( \gamma \) ,

\[
I\left( {V, W}\right)  =  - {\int }_{a}^{b}\left\langle  {{D}_{t}^{2}V + R\left( {V,{\gamma }^{\prime }}\right) {\gamma }^{\prime }, W}\right\rangle  {dt}
\]

\[
+ {\left. \left\langle  {D}_{t}V, W\right\rangle  \right| }_{t = a}^{t = b} - \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}\left\langle  {{\Delta }_{i}{D}_{t}V, W\left( {a}_{i}\right) }\right\rangle  , \tag{10.24}
\]

where \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) is an admissible partition for \( V \) and \( W \) , and \( {\Delta }_{i}{D}_{t}V \) is the jump in \( {D}_{t}V \) at \( t = {a}_{i} \) .

Proof. On every subinterval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) where \( V \) and \( W \) are smooth,

\[
\frac{d}{dt}\left\langle  {{D}_{t}V, W}\right\rangle   = \left\langle  {{D}_{t}^{2}V, W}\right\rangle   + \left\langle  {{D}_{t}V,{D}_{t}W}\right\rangle  .
\]

Thus, by the fundamental theorem of calculus,

\[
{\int }_{{a}_{i - 1}}^{{a}_{i}}\left\langle  {{D}_{t}V,{D}_{t}W}\right\rangle  {dt} =  - {\left. {\int }_{{a}_{i - 1}}^{{a}_{i}}\left\langle  {D}_{t}^{2}V, W\right\rangle  dt + \left\langle  {D}_{t}V, W\right\rangle  \right| }_{{a}_{i - 1}}^{{a}_{i}}.
\]

Summing over \( i \) , and noting that \( W \) is continuous at \( t = {a}_{i} \) for \( i = 1,\ldots , k - 1 \) , we get (10.24).

Corollary 10.25. If \( \gamma \) is a geodesic segment and \( V \) is a proper normal piecewise smooth vector field along \( \gamma \) , then \( I\left( {V, W}\right)  = 0 \) for every proper normal piecewise smooth vector field \( W \) along \( \gamma \) if and only if \( V \) is a Jacobi field.

## Geodesics Do Not Minimize Past Conjugate Points

We can use the second variation formula to prove another extremely important fact about conjugate points: no geodesic is minimizing past its first conjugate point. The geometric intuition is as follows. Suppose \( \gamma  : \left\lbrack  {a, c}\right\rbrack   \rightarrow  M \) is a minimizing geodesic segment, and \( \gamma \left( b\right) \) is conjugate to \( \gamma \left( a\right) \) along \( \gamma \) for some \( a < b < c \) . If \( J \) is a Jacobi field along \( \gamma \) that vanishes at \( t = a \) and \( t = b \) , then there is a variation of \( \gamma \) through geodesics, all of which start at \( \gamma \left( a\right) \) . Since \( J\left( b\right)  = 0 \) , we can expect them to end "almost" at \( \gamma \left( b\right) \) . If they really did all end at \( \gamma \left( b\right) \) , we could construct a broken geodesic by following some \( {\Gamma }_{s} \) from \( \gamma \left( a\right) \) to \( \gamma \left( b\right) \) and then following \( \gamma \) from \( \gamma \left( b\right) \) to \( \gamma \left( c\right) \) , which would have the same length and thus would also be a minimizing curve. But this is impossible: as the proof of Theorem 6.4 shows, a broken geodesic can always be shortened by rounding the corner.

The problem with this heuristic argument is that there is no guarantee that we can construct a variation through geodesics that actually end at \( \gamma \left( b\right) \) . The proof of the following theorem is based on an "infinitesimal" version of rounding the corner to obtain a shorter curve.

Given a geodesic segment \( \gamma  : \left\lbrack  {a, c}\right\rbrack   \rightarrow  M \) , we say that \( \gamma \) has a conjugate point if there is some \( b \in  (a, c\rbrack \) such that \( \gamma \left( b\right) \) is conjugate to \( \gamma \left( a\right) \) along \( \gamma \) , and \( \gamma \) has an interior conjugate point if there is such a \( b \in  \left( {a, c}\right) \) .

Theorem 10.26. Let \( \left( {M, g}\right) \) be a Riemannian manifold and \( p, q \in  M \) . If \( \gamma \) is a unit-speed geodesic segment from \( p \) to \( q \) that has an interior conjugate point, then there exists a proper normal vector field \( X \) along \( \gamma \) such that \( I\left( {X, X}\right)  < 0 \) . Therefore, \( \gamma \) is not minimizing.

Proof. Suppose \( \gamma  : \left\lbrack  {a, c}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic segment, and \( \gamma \left( b\right) \) is conjugate to \( \gamma \left( a\right) \) along \( \gamma \) for some \( a < b < c \) . This means that there is a nontrivial normal Jacobi field \( J \) along \( \gamma \) that vanishes at \( t = a \) and \( t = b \) . Define a vector field \( V \) along all of \( \gamma \) by

\[
V\left( t\right)  = \left\{  \begin{array}{ll} J\left( t\right) , & t \in  \left\lbrack  {a, b}\right\rbrack  \\  0, & t \in  \left\lbrack  {b, c}\right\rbrack   \end{array}\right.
\]

This is a proper, normal, piecewise smooth vector field along \( \gamma \) .

Let \( W \) be a smooth proper normal vector field along \( \gamma \) such that \( W\left( b\right) \) is equal to the jump \( \Delta {D}_{t}V \) at \( t = b \) (Fig. 10.9). Such a vector field is easily constructed with the help of an orthonormal frame along \( \gamma \) and a bump function. Note that \( \Delta {D}_{t}V = \; - {D}_{t}J\left( b\right) \) is not zero, because otherwise \( J \) would be a Jacobi field satisfying \( J\left( b\right)  = \; {D}_{t}J\left( b\right)  = 0 \) , and thus would be identically zero.

For small positive \( \varepsilon \) , let \( {X}_{\varepsilon } = V + {\varepsilon W} \) . Then

\[
I\left( {{X}_{\varepsilon },{X}_{\varepsilon }}\right)  = I\left( {V + {\varepsilon W}, V + {\varepsilon W}}\right)
\]

\[
= I\left( {V, V}\right)  + {2\varepsilon I}\left( {V, W}\right)  + {\varepsilon }^{2}I\left( {W, W}\right) .
\]

Since \( V \) satisfies the Jacobi equation on each subinterval \( \left\lbrack  {a, b}\right\rbrack \) and \( \left\lbrack  {b, c}\right\rbrack \) , and \( V\left( b\right)  = 0,\left( {10.24}\right) \) gives

\[
I\left( {V, V}\right)  =  - \left\langle  {\Delta {D}_{t}V, V\left( b\right) }\right\rangle   = 0.
\]

![bo_d7dtff491nqc73eq8m7g_314_351_188_825_387_0.jpg](images/bo_d7dtff491nqc73eq8m7g_314_351_188_825_387_0.jpg)

Fig. 10.9: Constructing a vector field \( X \) with \( I\left( {X, X}\right)  < 0 \)

Similarly,

\[
I\left( {V, W}\right)  =  - \left\langle  {\Delta {D}_{t}V, W\left( b\right) }\right\rangle   =  - {\left| W\left( b\right) \right| }^{2}.
\]

Thus

\[
I\left( {{X}_{\varepsilon },{X}_{\varepsilon }}\right)  =  - {2\varepsilon }{\left| W\left( b\right) \right| }^{2} + {\varepsilon }^{2}I\left( {W, W}\right) .
\]

If we choose \( \varepsilon \) small enough, this is strictly negative.

There is a partial converse to the preceding theorem, which says that a geodesic without conjugate points has the shortest length among all nearby curves in any proper variation. Before we prove it, we need the following technical lemma.

Lemma 10.27. Let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a geodesic segment, and suppose \( {J}_{1} \) and \( {J}_{2} \) are Jacobi fields along \( \gamma \) . Then \( \left\langle  {{D}_{t}{J}_{1}\left( t\right) ,{J}_{2}\left( t\right) }\right\rangle   - \left\langle  {{J}_{1}\left( t\right) ,{D}_{t}{J}_{2}\left( t\right) }\right\rangle \) is constant along \( \gamma \) .

Proof. Let \( f\left( t\right)  = \left\langle  {{D}_{t}{J}_{1}\left( t\right) ,{J}_{2}\left( t\right) }\right\rangle   - \left\langle  {{J}_{1}\left( t\right) ,{D}_{t}{J}_{2}\left( t\right) }\right\rangle \) . Using the Jacobi equation, we compute

\[
{f}^{\prime }\left( t\right)  = \left\langle  {{D}_{t}^{2}{J}_{1}\left( t\right) ,{J}_{2}\left( t\right) }\right\rangle   + \left\langle  {{D}_{t}{J}_{1}\left( t\right) ,{D}_{t}{J}_{2}\left( t\right) }\right\rangle
\]

\[
- \left\langle  {{D}_{t}{J}_{1}\left( t\right) ,{D}_{t}{J}_{2}\left( t\right) }\right\rangle   - \left\langle  {{J}_{1}\left( t\right) ,{D}_{t}^{2}{J}_{2}\left( t\right) }\right\rangle
\]

\[
=  - {Rm}\left( {{J}_{1}\left( t\right) ,{\gamma }^{\prime }\left( t\right) ,{\gamma }^{\prime }\left( t\right) ,{J}_{2}\left( t\right) }\right)  + {Rm}\left( {{J}_{2}\left( t\right) ,{\gamma }^{\prime }\left( t\right) ,{\gamma }^{\prime }\left( t\right) ,{J}_{1}\left( t\right) }\right)  = 0,
\]

where the last equality follows from the symmetries of the curvature tensor.

Theorem 10.28. Let \( \left( {M, g}\right) \) be a Riemannian manifold. Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic segment without interior conjugate points. If \( V \) is any proper normal piecewise smooth vector field along \( \gamma \) , then \( I\left( {V, V}\right)  \geq  0 \) , with equality if and only if \( V \) is a Jacobi field. In particular, if \( \gamma \left( b\right) \) is not conjugate to \( \gamma \left( a\right) \) along \( \gamma \) , then \( I\left( {V, V}\right)  > 0 \) .

Proof. To simplify the notation, we can assume (after replacing \( t \) by \( t - a \) ) that \( a = 0 \) . Let \( p = \gamma \left( 0\right) \) , and let \( \left( {{w}_{1},\ldots ,{w}_{n}}\right) \) be an orthonormal basis for \( {T}_{p}M \) , chosen so that \( {w}_{1} = {\gamma }^{\prime }\left( 0\right) \) . For each \( \alpha  = 2,\ldots , n \) , let \( {J}_{\alpha } \) be the unique normal Jacobi field along \( \gamma \) satisfying \( {J}_{\alpha }\left( 0\right)  = 0 \) and \( {D}_{t}{J}_{\alpha }\left( 0\right)  = {w}_{\alpha } \) .

Our assumption that \( \gamma \) has no interior conjugate points guarantees that no linear combination of the \( {J}_{\alpha }\left( t\right) \) ’s can vanish for any \( t \in  \left( {0, b}\right) \) , and thus \( \left( {{J}_{\alpha }\left( t\right) }\right) \) forms a basis for the orthogonal complement of \( {\gamma }^{\prime }\left( t\right) \) in \( {T}_{\gamma \left( t\right) }M \) for each such \( t \) . Thus, given \( V \) as in the statement of the theorem, for \( t \in  \left( {0, b}\right) \) we can write

\[
V\left( t\right)  = {v}^{\alpha }\left( t\right) {J}_{\alpha }\left( t\right) \tag{10.25}
\]

for some piecewise smooth functions \( {v}^{\alpha } : \left( {0, b}\right)  \rightarrow  M \) . (Here and in the remainder of this proof, the summation convention is in effect, with Greek indices running from 2 to \( n \) .)

In fact, each function \( {v}^{\alpha } \) has a piecewise smooth extension to \( \left\lbrack  {0, b}\right\rbrack \) . To see why, let \( \left( {x}^{i}\right) \) be the normal coordinates centered at \( p \) determined by the basis \( \left( {w}_{i}\right) \) . For sufficiently small \( t > 0 \) , we can express \( {J}_{\alpha }\left( t\right) \) and \( V\left( t\right) \) in normal coordinates as

\[
{J}_{\alpha }\left( t\right)  = {\left. t\frac{\partial }{\partial {x}_{\alpha }}\right| }_{\gamma \left( t\right) },\;\alpha  = 2,\ldots , n,
\]

\[
V\left( t\right)  = {v}^{\alpha }\left( t\right) {J}_{\alpha }\left( t\right)  = {\left. t{v}^{\alpha }\left( t\right) \frac{\partial }{\partial {x}_{\alpha }}\right| }_{\gamma \left( t\right) }.
\]

(The formula for \( {J}_{\alpha }\left( t\right) \) follows from Prop. 10.10.) Because \( V \) is smooth on \( \lbrack 0,\delta ) \) for some \( \delta  > 0 \) and \( V\left( 0\right)  = 0 \) , it follows from Taylor’s theorem that the components of \( V\left( t\right) /t \) extend smoothly to \( \lbrack 0,\delta ) \) , which shows that \( {v}^{\alpha } \) is smooth there. Because \( V\left( b\right)  = 0 \) , it follows similarly that \( {v}^{\alpha } \) extends smoothly to \( t = b \) as well. (If \( {J}_{\alpha }\left( b\right)  = \) 0, the argument is the same as for \( t = 0 \) , while if not, it is even easier.)

Let \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) be an admissible partition for \( V \) . On each subinterval \( \left( {{a}_{i - 1},{a}_{i}}\right) \) where \( V \) is smooth, define vector fields \( X \) and \( Y \) along \( \gamma \) by

\[
X = {v}^{\alpha }{D}_{t}{J}_{\alpha },\;Y = {\dot{v}}^{\alpha }{J}_{\alpha }.
\]

Then \( {D}_{t}V = X + Y \) on each such interval, and the fact that \( V \) is piecewise smooth implies that \( {D}_{t}V, X \) , and \( Y \) extend smoothly to \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) for each \( i \) , with one-sided derivatives at the endpoints.

To compute \( I\left( {V, V}\right) \) , we will use the following identity, which holds on each subinterval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) :

\[
{\left| {D}_{t}V\right| }^{2} - \operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right)  = \frac{d}{dt}\langle V, X\rangle  + {\left| Y\right| }^{2}. \tag{10.26}
\]

Granting this for now, we use the fundamental theorem of calculus to compute

\[
I\left( {V, V}\right)  = \mathop{\sum }\limits_{{i = 1}}^{k}{\int }_{{a}_{i - 1}}^{{a}_{i}}\left( {{\left| {D}_{t}V\right| }^{2} - \operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) }\right) {dt}
\]

\[
= {\left. \mathop{\sum }\limits_{{i = 1}}^{k}\langle V, X\rangle \right| }_{t = {a}_{i - 1}}^{t = {a}_{i}} + {\int }_{0}^{b}{\left| Y\right| }^{2}{dt}
\]

where the boundary terms are to be interpreted as limits from above and below. Because \( X \) and \( V \) are both continuous on \( \left\lbrack  {0, b}\right\rbrack \) , the boundary terms at \( t = {a}_{1},\ldots ,{a}_{k - 1} \) all cancel, and because \( V\left( 0\right)  = V\left( b\right)  = 0 \) , the boundary terms at \( t = 0 \) and \( t = b \) are both zero. It follows that \( I\left( {V, V}\right)  = {\int }_{0}^{b}{\left| Y\right| }^{2}{dt} \geq  0 \) . If \( I\left( {V, V}\right)  = 0 \) , then \( Y \) is identically zero on \( \left( {0, b}\right) \) . Since the \( {J}_{\alpha } \) ’s are linearly independent there, this implies that \( {\dot{v}}^{\alpha } \equiv  0 \) for each \( \alpha \) , so each \( {v}^{\alpha } \) is constant. Thus \( V \) is a linear combination of Jacobi fields with constant coefficients, so it is a Jacobi field.

It remains only to prove (10.26). Note that

\[
\frac{d}{dt}\langle V, X\rangle  = \left\langle  {{D}_{t}V, X}\right\rangle   + \left\langle  {V,{D}_{t}X}\right\rangle   = \langle X + Y, X\rangle  + \left\langle  {V,{D}_{t}X}\right\rangle  . \tag{10.27}
\]

The Jacobi equation gives

\[
{D}_{t}X = {\dot{v}}^{\alpha }{D}_{t}{J}_{\alpha } + {v}^{\alpha }{D}_{t}^{2}{J}_{\alpha } = {\dot{v}}^{\alpha }{D}_{t}{J}_{\alpha } - {v}^{\alpha }R\left( {{J}_{\alpha },{\gamma }^{\prime }}\right) {\gamma }^{\prime } = {\dot{v}}^{\alpha }{D}_{t}{J}_{\alpha } - R\left( {V,{\gamma }^{\prime }}\right) {\gamma }^{\prime }.
\]

Therefore,

\[
\left\langle  {{D}_{t}X, V}\right\rangle   = \left\langle  {{\dot{v}}^{\alpha }{D}_{t}{J}_{\alpha },{v}^{\beta }{J}_{\beta }}\right\rangle   - {Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) . \tag{10.28}
\]

Because \( \left\langle  {{D}_{t}{J}_{\alpha },{J}_{\beta }}\right\rangle   - \left\langle  {{J}_{\alpha },{D}_{t}{J}_{\beta }}\right\rangle   = 0 \) at \( t = 0 \) , it follows from Lemma 10.27 that \( \left\langle  {{D}_{t}{J}_{\alpha },{J}_{\beta }}\right\rangle   = \left\langle  {{J}_{\alpha },{D}_{t}{J}_{\beta }}\right\rangle \) all along \( \gamma \) . Thus we can simplify the first term in (10.28) as follows:

\[
\left\langle  {{\dot{v}}^{\alpha }{D}_{t}{J}_{\alpha },{v}^{\beta }{J}_{\beta }}\right\rangle   = {\dot{v}}^{\alpha }{v}^{\beta }\left\langle  {{D}_{t}{J}_{\alpha },{J}_{\beta }}\right\rangle   = {\dot{v}}^{\alpha }{v}^{\beta }\left\langle  {{J}_{\alpha },{D}_{t}{J}_{\beta }}\right\rangle
\]

\[
= \left\langle  {{\dot{v}}^{\alpha }{J}_{\alpha },{v}^{\beta }{D}_{t}{J}_{\beta }}\right\rangle   = \langle Y, X\rangle .
\]

Inserting this into (10.28), and then inserting the latter into (10.27) yields

\[
\frac{d}{dt}\langle V, X\rangle  = \langle X + Y, X\rangle  + \langle Y, X\rangle  - {Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right)
\]

\[
= {\left| X + Y\right| }^{2} - {\left| Y\right| }^{2} - \operatorname{Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) ,
\]

which is equivalent to (10.26).

The next corollary summarizes the results of Theorems 10.26 and 10.28.

Corollary 10.29. Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a unit-speed geodesic segment.

(a) If \( \gamma \) has an interior conjugate point, then it is not minimizing.

![bo_d7dtff491nqc73eq8m7g_317_636_203_274_382_0.jpg](images/bo_d7dtff491nqc73eq8m7g_317_636_203_274_382_0.jpg)

Fig. 10.10: Geodesics on the cylinder

(b) If \( \gamma \left( a\right) \) and \( \gamma \left( b\right) \) are conjugate but \( \gamma \) has no interior conjugate points, then for every proper normal variation \( \Gamma \) of \( \gamma \) , the curve \( {\Gamma }_{s} \) is strictly longer than \( \gamma \) for all sufficiently small nonzero \( s \) unless the variation field of \( \Gamma \) is a Jacobi field.

(c) If \( \gamma \) has no conjugate points, then for every proper normal variation \( \Gamma \) of \( \gamma \) , the curve \( {\Gamma }_{s} \) is strictly longer than \( \gamma \) for all sufficiently small nonzero \( s \) .

There is a far-reaching quantitative generalization of Theorems 10.26 and 10.28, called the Morse index theorem, which we do not treat here. The index of a geodesic segment is defined to be the maximum dimension of a linear space of proper normal vector fields along the segment on which \( I \) is negative definite. Roughly speaking, the index is the number of independent directions in which \( \gamma \) can be deformed to decrease its length. (Analogously, the index of a critical point of a function on \( {\mathbb{R}}^{n} \) is defined as the number of negative eigenvalues of its Hessian.) The Morse index theorem says that the index of every geodesic segment is finite, and is equal to the number of its interior conjugate points counted with multiplicity. (Proofs can be found in [Mil63, CE08, dC92].)

## Cut Points

Theorem 10.26 showed that once a geodesic passes its first conjugate point, it ceases to be minimizing. The converse, however, is not true: a geodesic can cease to be minimizing without reaching a conjugate point. For example, on the cylinder \( {\mathbb{S}}^{1} \times  \mathbb{R} \) with the product metric, there are no conjugate points along any geodesic; but no geodesic segment that wraps more than halfway around the cylinder is minimizing (Fig. 10.10).

Therefore it is useful to make the following definitions. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold, \( p \) is a point of \( M \) , and \( v \in  {T}_{p}M \) . Define the cut time of \( \left( {p, v}\right) \) by

\[
{t}_{\text{ cut }}\left( {p, v}\right)  = \sup \{ b > 0\text{ : the restriction of }{\gamma }_{v}\text{ to }\left\lbrack  {0, b}\right\rbrack  \text{ is minimizing }\} \text{ , }
\]

where \( {\gamma }_{v} \) is the maximal geodesic starting at \( p \) with initial velocity \( v \) . Because \( {\gamma }_{v} \) is minimizing as long as its image stays inside a geodesic ball (Prop. 6.11), \( {t}_{\text{ cut }}\left( {p, v}\right) \) is always positive; but it might be \( + \infty \) .

If \( {t}_{\text{ cut }}\left( {p, v}\right)  < \infty \) , the cut point of \( p \) along \( {\gamma }_{v} \) is the point \( {\gamma }_{v}\left( {{t}_{\text{ cut }}\left( {p, v}\right) }\right)  \in  M \) . The cut locus of \( p \) , denoted by \( \operatorname{Cut}\left( p\right) \) , is the set of all \( q \in  M \) such that \( q \) is the cut point of \( p \) along some geodesic. Because the question whether a geodesic is minimizing is independent of parametrization, the cut point of \( p \) along \( {\gamma }_{v} \) is the same as the cut point along \( {\gamma }_{\lambda v} \) for every positive constant \( \lambda \) , so we may as well restrict attention to unit vectors \( v \) . Theorem 10.26 says that the cut point (if it exists) occurs at or before the first conjugate point along every geodesic.

The determination of the cut locus of a point is typically very difficult; but the next example gives some special cases in which it is relatively simple.

Example 10.30 (Cut Loci).

(a) If \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) is a sphere with a round metric, the cut locus of every point \( p \in  {\mathbb{S}}^{n}\left( R\right) \) is the singleton set containing only the antipodal point \( - p \) .

(b) On a product space \( {\mathbb{S}}^{n}\left( R\right)  \times  {\mathbb{R}}^{m} \) with the product metric, the cut locus of every point \( \left( {p, x}\right) \) is the set \( \{  - p\}  \times  {\mathbb{R}}^{m} \) . The case \( n = m = 1 \) is illustrated in Figure 10.10.

- Exercise 10.31. Verify the claims in the preceding example.

Proposition 10.32 (Properties of Cut Times). Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold, \( p \in  M \) , and \( v \) is a unit vector in \( {T}_{p}M \) . Let \( c = \; {t}_{\text{ cut }}\left( {p, v}\right)  \in  (0,\infty \rbrack . \)

(a) If \( 0 < b < c \) , then \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0, b\right\rbrack  } \) has no conjugate points and is the unique unit-speed minimizing curve between its endpoints.

(b) If \( c < \infty \) , then \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0, c\right\rbrack  } \) is minimizing, and one or both of the following conditions are true:

- \( {\gamma }_{v}\left( c\right) \) is conjugate to \( p \) along \( {\gamma }_{v} \) .

- There are two or more unit-speed minimizing geodesics from \( p \) to \( {\gamma }_{v}\left( c\right) \) .

Proof. Suppose first that \( 0 < b < c \) . By definition of \( {t}_{\text{ cut }}\left( {p, v}\right) \) , there is a time \( {b}^{\prime } \) such that \( b < {b}^{\prime } < c \) and \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0,{b}^{\prime }\right\rbrack  } \) is minimizing. Then \( {\gamma }_{v}\left( t\right) \) cannot be conjugate to \( p \) along \( {\gamma }_{v} \) for any \( 0 < t \leq  b \) (Thm. 10.26), and \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0, b\right\rbrack  } \) is minimizing because a shorter admissible curve from \( p \) to \( {\gamma }_{v}\left( b\right) \) could be combined with \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  b,{b}^{\prime }\right\rbrack  } \) to produce a shorter admissible curve from \( p \) to \( {\gamma }_{v}\left( {b}^{\prime }\right) \) , contradicting the fact that \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0,{b}^{\prime }\right\rbrack  } \) is minimizing.

To see that \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0, b\right\rbrack  } \) is the unique unit-speed minimizing curve between its endpoints, suppose for the sake of contradiction that \( \sigma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) is another. Note that \( {\sigma }^{\prime }\left( b\right)  \neq  {\gamma }_{v}^{\prime }\left( b\right) \) , since otherwise \( \sigma \) and \( {\gamma }_{v} \) would agree on \( \left\lbrack  {0, b}\right\rbrack \) by uniqueness of geodesics. Define a new unit-speed admissible curve \( \widetilde{\gamma } : \left\lbrack  {0,{b}^{\prime }}\right\rbrack   \rightarrow  M \) that is equal to \( \sigma \left( t\right) \) for \( t \in  \left\lbrack  {0, b}\right\rbrack \) and equal to \( {\gamma }_{v}\left( t\right) \) for \( t \in  \left\lbrack  {b,{b}^{\prime }}\right\rbrack \) . Then \( \widetilde{\gamma } \) has length \( {b}^{\prime } \) , so it is also a minimizing curve from \( p \) to \( {\gamma }_{v}\left( {b}^{\prime }\right) \) ; but it is not smooth at \( t = b \) , contradicting the fact that minimizing curves are smooth geodesics. This completes the proof of (a).

Now suppose \( c < \infty \) . By definition of \( {t}_{\text{ cut }}\left( {p, v}\right) \) , there is a sequence of times \( {b}_{i} \nearrow  c \) such that the restriction of \( {\gamma }_{v} \) to \( \left\lbrack  {0,{b}_{i}}\right\rbrack \) is minimizing. By continuity of the distance function, therefore,

\[
{d}_{g}\left( {p,{\gamma }_{v}\left( c\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{d}_{g}\left( {p,{\gamma }_{v}\left( {b}_{i}\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{b}_{i} = c,
\]

which shows that \( {\gamma }_{v} \) is minimizing on \( \left\lbrack  {0, c}\right\rbrack \) . To prove that one of the options in (b) must hold, assume that \( {\gamma }_{v}\left( c\right) \) is not conjugate to \( p \) along \( {\gamma }_{v} \) . We will prove the existence of a second unit-speed minimizing geodesic from \( p \) to \( {\gamma }_{v}\left( c\right) \) .

Let \( \left( {b}_{i}\right) \) be a sequence of real numbers such that \( {b}_{i} \searrow  c \) . By definition of cut time, \( {\left. {\gamma }_{v}\right| }_{\left\lbrack  0,{b}_{i}\right\rbrack  } \) is not minimizing, so for each \( i \) there is a unit-speed minimizing geodesic \( {\sigma }_{i} : \left\lbrack  {0,{a}_{i}}\right\rbrack   \rightarrow  M \) such that \( {\sigma }_{i}\left( 0\right)  = p,{\sigma }_{i}\left( {a}_{i}\right)  = {\gamma }_{v}\left( {b}_{i}\right) \) , and \( {a}_{i} < {b}_{i} \) . Set \( {w}_{i} = {\sigma }_{i}^{\prime }\left( 0\right)  \in \; {T}_{p}M \) , so each \( {w}_{i} \) is a unit vector. By compactness of the unit sphere, after passing to a subsequence we may assume that \( {w}_{i} \) converges to some unit vector \( w \) . Since the \( {a}_{i} \) ’s are all positive and bounded above by \( {b}_{1} \) , by passing to a further subsequence, we may also assume that \( {a}_{i} \) converges to some number \( a \) . Then by continuity of the exponential map, \( {\sigma }_{i}\left( {a}_{i}\right)  = {\exp }_{p}\left( {{a}_{i}{w}_{i}}\right) \) converges to \( {\exp }_{p}\left( {aw}\right) \) . But we also know that \( {\sigma }_{i}\left( {a}_{i}\right)  = {\gamma }_{v}\left( {b}_{i}\right) \) , which converges to \( {\gamma }_{v}\left( c\right) \) , so \( {\exp }_{p}\left( {aw}\right)  = {\gamma }_{v}\left( c\right) \) . Moreover, by continuity of the distance function,

\[
c = {d}_{g}\left( {p,{\gamma }_{v}\left( c\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{d}_{g}\left( {p,{\sigma }_{i}\left( {a}_{i}\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{a}_{i} = a.
\]

Thus \( \sigma  : \left\lbrack  {0, c}\right\rbrack   \rightarrow  M \) given by \( \sigma \left( t\right)  = {\exp }_{p}\left( {tw}\right) \) is also a unit-speed minimizing geodesic from \( p \) to \( {\gamma }_{v}\left( c\right) \) . We need to show that it is not equal to \( {\gamma }_{v} \) .

The assumption that \( {\gamma }_{v}\left( c\right) \) is not conjugate to \( p \) along \( {\gamma }_{v} \) implies that \( {cv} \) is a regular point of \( {\exp }_{p} \) (Prop. 10.20), so \( {\exp }_{p} \) is injective in some neighborhood \( V \) of \( {cv} \) . Note that \( {\exp }_{p}\left( {{a}_{i}{w}_{i}}\right)  = {\exp }_{p}\left( {{b}_{i}v}\right) \) for each \( i \) , while \( {a}_{i}{w}_{i} \neq  {b}_{i}v \) , since \( {w}_{i} \) and \( v \) are unit vectors and \( {a}_{i} < {b}_{i} \) . Since \( {b}_{i}v \) converges to \( {cv} \) , we conclude that \( {b}_{i}v \in  V \) for sufficiently large \( i \) , and thus by injectivity \( {a}_{i}{w}_{i} \notin  V \) for these values of \( i \) . Therefore \( {cw} = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{a}_{i}{w}_{i} \neq  {cv} \) , which implies \( w \neq  v \) and thus \( \sigma  \neq  {\gamma }_{v} \) , as claimed.

Next we examine how the cut time varies as the initial point and initial velocity of the geodesic vary. Recall that the unit tangent bundle of a Riemannian manifold \( \left( {M, g}\right) \) is the subset \( {UTM} = \left\{  {\left( {p, v}\right)  \in  {TM} : {\left| v\right| }_{g} = 1}\right\}   \subseteq  {TM} \) . In the next theorem, we interpret continuity of a function into \( (0,\infty \rbrack \) using the usual definition of infinite limits as in ordinary calculus.

Theorem 10.33. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold. The function \( {t}_{\text{ cut }} : {UTM} \rightarrow  (0,\infty \rbrack \) is continuous.

Proof. Let \( \left( {p, v}\right)  \in  {UTM} \) be arbitrary, and let \( \left( {{p}_{i},{v}_{i}}\right) \) be any sequence in \( {UTM} \) converging to \( \left( {p, v}\right) \) . Put \( {c}_{i} = {t}_{\text{ cut }}\left( {{p}_{i},{v}_{i}}\right) \) , and

\[
b = \mathop{\liminf }\limits_{{i \rightarrow  \infty }}{c}_{i},\;c = \mathop{\limsup }\limits_{{i \rightarrow  \infty }}{c}_{i}.
\]

We will show that \( c \leq  {t}_{\text{ cut }}\left( {p, v}\right)  \leq  b \) , which implies \( {c}_{i} \rightarrow  {t}_{\text{ cut }}\left( {p, v}\right) \) .

To show that \( c \leq  {t}_{\text{ cut }}\left( {p, v}\right) \) , suppose first that \( c < \infty \) . By passing to a subsequence, we may assume that \( {c}_{i} \) is finite for each \( i \) and \( {c}_{i} \rightarrow  c \) . Proposition 10.32 shows that \( {\gamma }_{{v}_{i}} \) is minimizing on \( \left\lbrack  {0,{c}_{i}}\right\rbrack \) . By continuity of the exponential map, \( \exp \left( {{p}_{i},{c}_{i}{v}_{i}}\right)  \rightarrow  \exp \left( {p,{cv}}\right) \) as \( i \rightarrow  \infty \) , and therefore by continuity of the distance function we have

\[
{d}_{g}\left( {p,\exp \left( {p,{cv}}\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{d}_{g}\left( {{p}_{i},\exp \left( {{p}_{i},{c}_{i}{v}_{i}}\right) }\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{c}_{i} = c.
\]

This shows that \( {\gamma }_{v} \) is minimizing on \( \left\lbrack  {0, c}\right\rbrack \) , and therefore \( {t}_{\text{ cut }}\left( {p, v}\right)  \geq  c \) , as claimed.

Now suppose \( c = \infty \) . Again, by passing to a subsequence, we may assume \( {c}_{i} \rightarrow  \infty \) . It follows that for every positive number \( {c}_{0} \) , the geodesic \( {\gamma }_{{v}_{i}} \) is minimizing on \( \left\lbrack  {0,{c}_{0}}\right\rbrack \) for \( i \) sufficiently large, and it follows by continuity as above that \( {\gamma }_{v} \) is minimizing on \( \left\lbrack  {0,{c}_{0}}\right\rbrack \) . Since \( {c}_{0} \) was arbitrary, this means that \( {t}_{\text{ cut }}\left( {p, v}\right)  = \infty \) .

Next we show that \( {t}_{\text{ cut }}\left( {p, v}\right)  \leq  b \) . If \( b = \infty \) , there is nothing to prove, so assume \( b < \infty \) . Again by passing to a subsequence, we may assume that \( {c}_{i} \) is finite for each \( i \) and \( {c}_{i} \rightarrow  b \) . By virtue of Proposition 10.32, either there are infinitely many indices \( i \) for which \( {\gamma }_{{v}_{i}}\left( {c}_{i}\right) \) is conjugate to \( {p}_{i} \) along \( {\gamma }_{{v}_{i}} \) , or there are infinitely many \( i \) for which there exists a second minimizing unit-speed geodesic \( {\sigma }_{i} \) from \( {p}_{i} \) to \( {\gamma }_{{v}_{i}}\left( {c}_{i}\right) \) .

In the first case, because conjugate points are critical values of the restricted exponential map, which can be detected in coordinates by the vanishing of a determinant of a matrix of first derivatives, it follows by continuity that \( {\gamma }_{v}\left( b\right) \) is also a critical value, and thus \( {\gamma }_{v}\left( b\right) \) is conjugate to \( p \) along \( {\gamma }_{v} \) . Then Theorem 10.26 shows that \( {t}_{\text{ cut }}\left( {p, v}\right)  \leq  b \) .

In the second case, let \( {w}_{i} \) be the unit vector in \( {T}_{{p}_{i}}M \) such that \( {\sigma }_{i} = {\gamma }_{{w}_{i}} \) . Because the components of \( {w}_{i} \) with respect to a local orthonormal frame lie in \( {\mathbb{S}}^{n - 1} \) , by passing to a subsequence we may assume \( \left( {{p}_{i}.{w}_{i}}\right)  \rightarrow  \left( {p, w}\right) \) . If \( {\gamma }_{v}\left( b\right) \) is conjugate to \( p \) along \( {\gamma }_{v} \) , then \( {t}_{\text{ cut }}\left( {p, v}\right)  \leq  b \) as above, so we may assume that \( {\gamma }_{v}\left( b\right) \) is not a conjugate point. This means that \( {bv} \) is a regular point of the restricted exponential map \( {\exp }_{p} \) . Since the set of such regular points is an open subset of \( {TM} \) , there is some \( \varepsilon  > 0 \) such that \( {\exp }_{{p}_{i}} \) is injective on the \( \varepsilon \) -neighborhood of \( {c}_{i}{w}_{i} \) for all \( i \) sufficiently large. This implies that \( {\left| {c}_{i}{w}_{i} - {c}_{i}{v}_{i}\right| }_{g} \geq  \varepsilon \) for all such \( i \) , and therefore the limits \( {bw} \) and \( {bv} \) are distinct. Thus \( {\left. {\gamma }_{w}\right| }_{\left\lbrack  0, b\right\rbrack  } \) is another minimizing geodesic from \( p \) to \( {\gamma }_{v}\left( b\right) \) , which by Proposition 10.32 implies that \( {t}_{\text{ cut }}\left( {p, v}\right)  \leq  b \) .

Given \( p \in  M \) , we define two subsets of \( {T}_{p}M \) as follows: the tangent cut locus of \( \mathbf{p} \) is the set

\[
\operatorname{TCL}\left( p\right)  = \left\{  {v \in  {T}_{p}M : \left| v\right|  = {t}_{\text{ cut }}\left( {p, v/\left| v\right| }\right) }\right\}  ,
\]

and the injectivity domain of \( p \) is

\[
\operatorname{ID}\left( p\right)  = \left\{  {v \in  {T}_{p}M : \left| v\right|  < {t}_{\text{ cut }}\left( {p, v/\left| v\right| }\right) }\right\}  .
\]

It is immediate that \( \operatorname{TCL}\left( p\right)  = \partial \operatorname{ID}\left( p\right) \) , and \( \operatorname{Cut}\left( p\right)  = {\exp }_{p}\left( {\operatorname{TCL}\left( p\right) }\right) \) . Further properties of \( \operatorname{Cut}\left( p\right) \) and \( \operatorname{ID}\left( p\right) \) are described in the following theorem.

Theorem 10.34. Let \( \left( {M, g}\right) \) be a complete, connected Riemannian manifold and \( p \in  M \) .

(a) The cut locus of \( p \) is a closed subset of \( M \) of measure zero.

(b) The restriction of \( {\exp }_{p} \) to \( \overline{\operatorname{ID}\left( p\right) } \) is surjective.

(c) The restriction of \( {\exp }_{p} \) to \( \operatorname{ID}\left( p\right) \) is a diffeomorphism onto \( M \smallsetminus  \operatorname{Cut}\left( p\right) \) .

Proof. To prove that the cut locus is closed, suppose \( \left( {q}_{i}\right) \) is a sequence of points in \( \operatorname{Cut}\left( p\right) \) converging to some \( q \in  M \) . Write \( {q}_{i} = {\exp }_{p}\left( {{t}_{\text{ cut }}\left( {p,{v}_{i}}\right) {v}_{i}}\right) \) for unit vectors \( {v}_{i} \) . By compactness of the unit sphere, we may assume after passing to a subsequence that \( {v}_{i} \) converges to some unit vector \( v \) , and by Theorem 10.33, \( {t}_{\text{ cut }}\left( {p, v}\right)  = \mathop{\lim }\limits_{{i \rightarrow  \infty }}{t}_{\text{ cut }}\left( {p,{v}_{i}}\right) \) . Because convergent sequences in a metric space are bounded, the sequence \( \left( {{t}_{\text{ cut }}\left( {p,{v}_{i}}\right) }\right) \) is bounded, and therefore \( {t}_{\text{ cut }}\left( {p, v}\right)  < \infty \) . By continuity of the exponential map, therefore, \( q \) must be equal to \( {\exp }_{p}\left( {{t}_{\text{ cut }}\left( {p, v}\right) }\right) \) , which shows that \( q \in  \operatorname{Cut}\left( p\right) \) , and thus \( \operatorname{Cut}\left( p\right) \) is closed.

To see that \( \operatorname{Cut}\left( p\right) \) has measure zero, note first that in any polar coordinates \( \left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}, r}\right) \) on \( {T}_{p}M \) , the set \( \operatorname{TCL}\left( p\right) \) can be expressed locally as the graph of the continuous function \( r = {t}_{\text{ cut }}\left( {p,\left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}}\right) }\right) \) , using the fact that \( \left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}}\right) \) form smooth local coordinates for the unit sphere in \( {T}_{p}M \) . Since graphs of continuous functions have measure zero (see, for example, [LeeSM, Prop. 6.3]), it follows that \( \operatorname{TCL}\left( p\right) \) is a union of finitely many sets of measure zero and thus has measure zero in \( {T}_{p}M \) ; and because smooth maps take sets of measure zero to sets of measure zero (see [LeeSM, Prop. 6.4]), \( \operatorname{Cut}\left( p\right)  = {\exp }_{p}\left( {\operatorname{TCL}\left( p\right) }\right) \) has measure zero in \( M \) . This proves (a).

Part (b) follows from the fact that every point of \( M \) can be connected to \( p \) by a minimizing geodesic. To prove (c), note that it follows easily from the definitions that \( {\exp }_{p}\left( {\operatorname{ID}\left( p\right) }\right)  = M \smallsetminus  \operatorname{Cut}\left( p\right) \) . Also, the definition of \( \operatorname{ID}\left( p\right) \) guarantees that no point in \( {\exp }_{p}\left( {\operatorname{ID}\left( p\right) }\right) \) can be a cut point of \( p \) , and thus no such point can be a conjugate point either. The absence of cut points implies that \( {\exp }_{p} \) is injective on \( \operatorname{ID}\left( p\right) \) , and the absence of conjugate points implies that it is a local diffeomorphism there. Together these two facts imply that it is a diffeomorphism onto its image.

The preceding theorem leads to the following intriguing topological result about compact manifolds.

Corollary 10.35. Every compact, connected, smooth n-manifold is homeomorphic to a quotient space of \( {\overline{\mathbb{B}}}^{n} \) by an equivalence relation that identifies only points on the boundary.

Proof. Let \( M \) be a compact, connected, smooth \( n \) -manifold, let \( p \) be any point of \( M \) , and let \( g \) be any Riemannian metric on \( M \) . Because a compact metric space has finite diameter, every unit vector in \( {T}_{p}M \) has a finite cut time, no greater than the diameter of \( M \) . Let \( {\bar{B}}_{1}\left( 0\right)  \subseteq  {T}_{p}M \) denote the closed unit ball in \( {T}_{p}M \) , and define a map \( f : {\bar{B}}_{1}\left( 0\right)  \rightarrow  \overline{\operatorname{ID}\left( p\right) } \) by

\[
f\left( v\right)  = \left\{  \begin{array}{ll} {t}_{\text{ cut }}\left( {p,\frac{v}{{\left| v\right| }_{g}}}\right) v, & v \neq  0, \\  0 & v = 0. \end{array}\right.
\]

It follows from Theorem 10.33 that \( f \) is continuous, and it is easily seen to be bijective, so it is a homeomorphism by the closed map lemma (Lemma A.4). Since every orthonormal basis for \( {T}_{p}M \) yields a homeomorphism of \( {\bar{B}}_{1}\left( 0\right) \) with \( {\overline{\mathbb{B}}}^{n} \) , it follows that \( \overline{\operatorname{ID}\left( p\right) } \) is homeomorphic to \( {\overline{\mathbb{B}}}^{n} \) and the homeomorphism takes \( \operatorname{TCL}\left( p\right)  = \partial \operatorname{ID}\left( p\right) \) to \( {\mathbb{S}}^{n - 1} \) .

By Theorem 10.34, \( {\exp }_{p} \) restricts to a surjective map from \( \overline{\operatorname{ID}\left( p\right) } \) to \( M \) , and it is a quotient map by the closed map lemma. It follows that \( M \) is homeomorphic to the quotient of \( \overline{\operatorname{ID}\left( p\right) } \) by the equivalence relation \( v \sim  w \) if and only if \( {\exp }_{p}\left( v\right)  = \; {\exp }_{p}\left( w\right) \) . Since \( {\exp }_{p} \) is injective on \( \operatorname{ID}\left( p\right) \) and the images of \( \operatorname{ID}\left( p\right) \) and \( \partial \operatorname{ID}\left( p\right)  = \; \operatorname{TCL}\left( p\right) \) are disjoint, the equivalence relation identifies only points on the boundary of ID \( \left( p\right) \) .

Recall from Chapter 6 that the injectivity radius of \( M \) at \( p \) , denoted by \( \operatorname{inj}\left( p\right) \) , is the supremum of all positive numbers \( a \) such that \( {\exp }_{p} \) is a diffeomorphism from \( {B}_{a}\left( 0\right)  \subseteq  {T}_{p}M \) to its image. The injectivity radius is closely related to the cut locus, as the next proposition shows.

Proposition 10.36. Let \( \left( {M, g}\right) \) be a complete, connected Riemannian manifold. For each \( p \in  M \) , the injectivity radius at \( p \) is the distance from \( p \) to its cut locus if the cut locus is nonempty, and infinite otherwise.

Proof. Given \( p \in  M \) , let \( d \) denote the distance from \( p \) to its cut locus, with the convention that \( d = \infty \) if the cut locus is empty. Let \( a \in  (0,\infty \rbrack \) be arbitrary, and let \( {B}_{a} \subseteq  {T}_{p}M \) denote the set of vectors \( v \in  {T}_{p}M \) with \( {\left| v\right| }_{g} < a \) (so \( {B}_{a} = {T}_{p}M \) if \( a = \infty ) \) . We will show that the restriction of \( {\exp }_{p} \) to \( {B}_{a} \) is a diffeomorphism onto its image if and only if \( a \leq  d \) , from which the result follows.

First suppose \( a \leq  d \) . By definition of \( d \) , no point of the form \( {\exp }_{p}\left( v\right) \) with \( v \in  {B}_{a} \) can be a cut point of \( p \) , so \( {B}_{a} \subseteq  \operatorname{ID}\left( p\right) \) . It follows from Theorem 10.34(c) that \( {\exp }_{p} \) is a diffeomorphism from \( {B}_{a} \) onto its image.

On the other hand, if \( a > d \) , then \( p \) has a cut point \( q \) whose distance from \( p \) is less than \( a \) . It follows from the definition of cut points that the radial geodesic from \( p \) to \( q \) is not minimizing past \( q \) , so Proposition 6.11 shows that there is no geodesic ball of radius greater than \( {d}_{g}\left( {p, q}\right) \) . In particular, the restriction of \( {\exp }_{p} \) to \( {B}_{a} \) cannot be a diffeomorphism onto its image.

Proposition 10.37. Let \( \left( {M, g}\right) \) be a complete, connected Riemannian manifold. The function inj: \( M \rightarrow  (0,\infty \rbrack \) is continuous.

Proof. Let \( p \in  M \) be arbitrary. Proposition 10.32(b) shows that for each point \( q \in \; \operatorname{Cut}\left( p\right) \) , there is a minimizing unit-speed geodesic \( {\gamma }_{v} \) from \( p \) to \( q \) whose length is \( {t}_{\text{ cut }}\left( {p, v}\right) \) , and therefore the distance from \( p \) to \( \operatorname{Cut}\left( p\right) \) is the infimum of the cut times of unit-speed geodesics starting at \( p \) . By the previous proposition, therefore,

\[
\operatorname{inj}\left( p\right)  = \inf \left\{  {{t}_{\text{ cut }}\left( {p, v}\right)  : v \in  {T}_{p}M\text{ with }{\left| v\right| }_{g} = 1}\right\}  .
\]

Suppose \( \left( {p}_{i}\right) \) is a sequence in \( M \) converging to a point \( p \in  M \) . As in the proof of Theorem 10.33, we will prove that \( \operatorname{inj}\left( {p}_{i}\right)  \rightarrow  \operatorname{inj}\left( p\right) \) by showing that \( c \leq  \operatorname{inj}\left( p\right)  \leq  b \) , where

\[
b = \mathop{\liminf }\limits_{{i \rightarrow  \infty }}\operatorname{inj}\left( {p}_{i}\right) ,\;c = \mathop{\limsup }\limits_{{i \rightarrow  \infty }}\operatorname{inj}\left( {p}_{i}\right) .
\]

First we show that \( \operatorname{inj}\left( p\right)  \leq  b \) . By passing to a subsequence, we may assume \( \operatorname{inj}\left( {p}_{i}\right)  \rightarrow  b \) . By compactness of the unit sphere, for each \( i \) there is a unit vector \( {v}_{i} \in \; {T}_{{p}_{i}}M \) such that \( \operatorname{inj}\left( {p}_{i}\right)  = {t}_{\text{ cut }}\left( {{p}_{i},{v}_{i}}\right) \) , and after passing to a further subsequence, we may assume \( \left( {{p}_{i},{v}_{i}}\right)  \rightarrow  \left( {p, v}\right) \) for some \( v \in  {T}_{p}M \) . By continuity of \( {t}_{\text{ cut }} \) , we have \( {t}_{\text{ cut }}\left( {p, v}\right)  = \mathop{\lim }\limits_{i}{t}_{\text{ cut }}\left( {{p}_{i},{v}_{i}}\right)  = b \) , so \( \operatorname{inj}\left( p\right)  \leq  b \) .

Next we show that \( \operatorname{inj}\left( p\right)  \geq  c \) . Once again, by passing to a subsequence of the original sequence \( \left( {p}_{i}\right) \) , we may assume \( \operatorname{inj}\left( {p}_{i}\right)  \rightarrow  c \) . Suppose for the sake of contradiction that \( \operatorname{inj}\left( p\right)  < c \) , and choose \( {c}_{0} \) such that \( \operatorname{inj}\left( p\right)  < {c}_{0} < c \) . Let \( w \) be a unit vector in \( {T}_{p}M \) such that \( {t}_{\text{ cut }}\left( {p, w}\right)  = \operatorname{inj}\left( p\right) \) . We can choose some sequence of unit vectors \( {w}_{i} \in  {T}_{{p}_{i}}M \) such that \( \left( {{p}_{i},{w}_{i}}\right)  \rightarrow  \left( {p, w}\right) \) , so \( {t}_{\text{ cut }}\left( {{p}_{i},{w}_{i}}\right)  \rightarrow  {t}_{\text{ cut }}\left( {p, w}\right)  = \) inj \( \left( p\right) \) . For \( i \) sufficiently large, this implies \( {t}_{\text{ cut }}\left( {{p}_{i},{w}_{i}}\right)  < {c}_{0} < c \) , contradicting the facts that \( {t}_{\text{ cut }}\left( {{p}_{i},{w}_{i}}\right)  \geq  \operatorname{inj}\left( {p}_{i}\right) \) and \( \operatorname{inj}\left( {p}_{i}\right)  \rightarrow  c \) .

## Problems

10-1. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( p \in  M \) . Show that the second-order Taylor series of \( g \) in normal coordinates centered at \( p \) is

\[
{g}_{ij}\left( x\right)  = {\delta }_{ij} - \frac{1}{3}\mathop{\sum }\limits_{{k, l}}{R}_{iklj}\left( p\right) {x}^{k}{x}^{l} + O\left( {\left| x\right| }^{3}\right) .
\]

[Hint: Let \( \gamma \left( t\right)  = \left( {t{v}^{1},\ldots , t{v}^{n}}\right) \) be a radial geodesic starting at \( p \) , let \( J\left( t\right)  = \; {\left. t{w}^{i}{\partial }_{i}\right| }_{\gamma \left( t\right) } \) be a Jacobi field along \( \gamma \) , and compute the first four \( t \) -derivatives of \( {\left| J\left( t\right) \right| }^{2} \) at \( t = 0 \) in two ways.]

10-2. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( p \in  M \) . Let \( {S}_{\Pi } \subseteq  M \) be the 2-dimensional submanifold obtained by applying the exponential map to a plane \( \Pi  \subseteq  {T}_{p}M \) , as on page 250. For sufficiently small \( r \) , let \( A\left( r\right) \) be the area of the geodesic disk of radius \( r \) about \( p \) in \( {S}_{\Pi } \) with its induced metric. Using the results of Problems 10-1 and 8-21, find the Taylor series of \( A\left( r\right) \) to fourth order in \( r \) . Then use this result to express \( \sec \left( \Pi \right) \) in terms of a limit involving the difference \( \pi {r}^{2} - A\left( r\right) \) .

10-3. Extend the result of Proposition 10.12 by finding a basis for the space of all Jacobi fields along a geodesic in the constant-curvature case, not just the normal ones that vanish at 0 .

10-4. Prove that the volume of the round sphere \( {\mathbb{S}}^{n}\left( R\right) \) is given for \( n \geq  0 \) by \( \operatorname{Vol}\left( {{\mathbb{S}}^{n}\left( R\right) }\right)  = {\alpha }_{n}{R}^{n} \) , where

\[
{\alpha }_{n} = \left\{  \begin{array}{ll} \frac{{2}^{{2k} + 1}{\pi }^{k}k!}{\left( {2k}\right) !}, & n = {2k}, k \in  \mathbb{Z}, \\  \frac{2{\pi }^{k + 1}}{k!}, & n = {2k} + 1, k \in  \mathbb{Z}. \end{array}\right.
\]

(The volume of a compact 0-manifold is just the number of points.)

(a) First show that it suffices to prove the volume formula for \( R = 1 \) .

(b) Use Corollary 10.17 to prove the recurrence relation

\[
\operatorname{Vol}\left( {\mathbb{S}}^{n + 1}\right)  = {\sigma }_{n}\operatorname{Vol}\left( {\mathbb{S}}^{n}\right)
\]

where

\[
{\sigma }_{n} = {\int }_{0}^{\pi }{\left( \sin r\right) }^{n}{dr}
\]

(c) By differentiating the function \( {\left( \sin r\right) }^{n}\cos r \) , prove that

\[
{\sigma }_{n + 1} = \frac{n}{n + 1}{\sigma }_{n - 1},
\]

and use this to prove that

\[
{\sigma }_{n}{\sigma }_{n - 1} = \frac{2\pi }{n}.
\]

(d) Prove the result by induction on \( k \) .

(Used on p. 342.)

10-5. For \( r > 0 \) , let \( {B}_{r}\left( 0\right) \) denote the ball of radius \( r \) in Euclidean space \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) , \( n \geq  1 \) . Prove that \( \operatorname{Vol}\left( {{B}_{r}\left( 0\right) }\right)  = \frac{1}{n}{\alpha }_{n - 1}{r}^{n} \) , with \( {\alpha }_{n - 1} \) as in Problem 10-4.

10-6. Let \( p \) be a point in a Riemannian \( n \) -manifold \( \left( {M, g}\right) \) . Use the results of Problems 10-1 and 8-21 to show that as \( r \searrow  0 \) ,

\[
\operatorname{Vol}\left( {{B}_{r}\left( p\right) }\right)  = \frac{1}{n}{\alpha }_{n - 1}{r}^{n}\left( {1 - \frac{S\left( p\right) {r}^{2}}{6\left( {n + 2}\right) } + O\left( {r}^{3}\right) }\right) ,
\]

where \( S\left( p\right) \) is the scalar curvature of \( g \) at \( p \) and \( {\alpha }_{n - 1} \) is as in Problem 10-4.

10-7. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with nonpositive sectional curvature. Prove that no point of \( M \) has conjugate points along any geodesic. [Hint: Consider derivatives of \( {\left| J\left( t\right) \right| }^{2} \) when \( J \) is a Jacobi field.] (Used on p. 333.)

10-8. Prove Proposition 10.21 (solvability of the two-point boundary problem).

10-9. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( {M}_{1},{M}_{2} \subseteq  M \) are embedded submanifolds. Let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a unit-speed geodesic segment that meets \( {M}_{1} \) orthogonally at \( t = a \) and meets \( {M}_{2} \) orthogonally at \( t = b \) , and let \( \Gamma  : K \times  \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be a normal variation of \( \gamma \) such that \( \Gamma \left( {s, a}\right)  \in  {M}_{1} \) and \( \Gamma \left( {s, b}\right)  \in  {M}_{2} \) for all \( s \) . Prove the following generalization of the second variation formula:

\[
{\left. \frac{{d}^{2}}{d{s}^{2}}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  = {\int }_{a}^{b}\left( {{\left| {D}_{t}V\right| }^{2} - {Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) }\right) {dt}
\]

\[
+ \left\langle  {{\mathrm{{II}}}_{2}\left( {V\left( b\right) , V\left( b\right) }\right) ,{\gamma }^{\prime }\left( b\right) }\right\rangle   - \left\langle  {{\mathrm{{II}}}_{1}\left( {V\left( a\right) , V\left( a\right) }\right) ,{\gamma }^{\prime }\left( a\right) }\right\rangle  ,
\]

where \( V \) is the variation field of \( \Gamma \) , and \( {\Pi }_{i} \) is the second fundamental form of \( {M}_{i} \) for \( i = 1,2 \) . (Used on p. 365.)

10-10. Prove the following theorem of Theodore Frankel [Fra61], generalizing the well-known fact that any two great circles on \( {\mathbb{S}}^{2} \) must intersect: Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold with positive sectional curvature. If \( {M}_{1},{M}_{2} \subseteq  M \) are compact, totally geodesic subman-ifolds such that \( \dim {M}_{1} + \dim {M}_{2} \geq  \dim M \) , then \( {M}_{1} \cap  {M}_{2} \neq  \varnothing \) . [Hint: Assuming that the intersection is empty, show that there exist a shortest geodesic segment \( \gamma \) connecting \( {M}_{1} \) and \( {M}_{2} \) and a parallel vector field along \( \gamma \) that is tangent to \( {M}_{1} \) and \( {M}_{2} \) at the endpoints; then apply the second variation formula of Problem 10-9 to derive a contradiction.]

10-11. Prove Corollary 10.25 ( \( I\left( {V, W}\right)  = 0 \) for all \( W \) if and only if \( V \) is a Jacobi field). [Hint: Adapt the proof of Theorem 6.4.]

10-12. Let \( \left( {M, g}\right) \) be a Riemannian manifold. Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic segment with no interior conjugate points, \( J \) is a normal Jacobi field along \( \gamma \) , and \( V \) is any other piecewise smooth normal vector field along \( \gamma \) such that \( V\left( a\right)  = J\left( a\right) \) and \( V\left( b\right)  = J\left( b\right) \) .

(a) Show that \( I\left( {V, V}\right)  \geq  I\left( {J, J}\right) \) .

(b) Now assume in addition that \( \gamma \left( b\right) \) is not conjugate to \( \gamma \left( a\right) \) along \( \gamma \) . Show that \( I\left( {V, V}\right)  = I\left( {J, J}\right) \) if and only if \( V = J \) .

10-13. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( X \in  \mathfrak{X}\left( M\right) \) is a Killing vector field (see Problems 5-22 and 6-24). Show that if \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any geodesic segment, then \( X \) restricts to a Jacobi field along \( \gamma \) .

10-14. Suppose \( P \) is an embedded submanifold of a Riemannian manifold \( M \) , and \( \gamma  : I \rightarrow  M \) is a geodesic that meets \( P \) orthogonally at \( t = a \) for some \( a \in  I \) . A Jacobi field \( J \) along \( \gamma \) is said to be transverse to \( P \) if its restriction to each compact subinterval of \( I \) containing \( a \) is the variation field of a variation of \( \gamma \) through geodesics that all meet \( P \) orthogonally at \( t = a \) .

(a) Prove that the tangential Jacobi field \( J\left( t\right)  = \left( {t - a}\right) {\gamma }^{\prime }\left( t\right) \) along \( \gamma \) is transverse to \( P \) .

(b) Prove that a normal Jacobi field \( J \) along \( \gamma \) is transverse to \( P \) if and only if

\[
{D}_{t}J\left( a\right)  =  - {W}_{{\gamma }^{\prime }\left( a\right) }\left( {J\left( a\right) }\right) ,
\]

where \( {W}_{{\gamma }^{\prime }\left( a\right) } \) is the Weingarten map of \( P \) in the direction of \( {\gamma }^{\prime }\left( a\right) \) .

(c) When \( M \) has dimension \( n \) , prove that the set of transverse Jacobi fields along \( \gamma \) is an \( n \) -dimensional linear subspace of \( \mathcal{J}\left( \gamma \right) \) , and the set of transverse normal Jacobi fields is an \( \left( {n - 1}\right) \) -dimensional subspace of that.

(Used on p. 342.)

10-15. Let \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) be any semigeodesic coordinates on an open subset \( U \) in a Riemannian \( n \) -manifold \( \left( {M, g}\right) \) (see Prop. 6.41 and Examples 6.43-6.46), and let \( \gamma \left( t\right)  = \left( {{x}^{1},\ldots ,{x}^{n - 1}, t}\right) \) be an \( {x}^{n} \) -coordinate curve defined on some interval \( I \) . Prove that for all constants \( \left( {{a}^{1},\ldots ,{a}^{n - 1}}\right) \) , the following vector field along \( \gamma \) is a normal Jacobi field along \( \gamma \) that is transverse to each of the level sets of \( {x}^{n} \) (in the sense defined in Problem 10-14):

\[
J\left( t\right)  = {\left. \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{a}^{i}\frac{\partial }{\partial {x}^{i}}\right| }_{\gamma \left( t\right) }.
\]

10-16. Suppose \( P \) is an embedded \( k \) -dimensional submanifold of a Riemannian \( n \) - manifold \( \left( {M, g}\right) \) , and \( \left( {{x}^{1},\ldots ,{x}^{k},{v}^{1},\ldots ,{v}^{n - k}}\right) \) are Fermi coordinates for \( P \) on some open subset \( {U}_{0} \subseteq  M \) . For fixed \( \left( {{x}^{i},{v}^{j}}\right) \) , let \( \gamma  : I \rightarrow  M \) be the curve with coordinate representation \( \gamma \left( t\right)  = \left( {{x}^{1},\ldots ,{x}^{k}, t{v}^{1},\ldots , t{v}^{n - k}}\right) \) ; Proposition 5.26 shows that \( \gamma \) is a geodesic that meets \( P \) orthogonally at \( t = 0 \) . Prove that the Jacobi fields along \( \gamma \) that are transverse to \( P \) are exactly the vector fields of the form

\[
J\left( t\right)  = {\left. \mathop{\sum }\limits_{{i = 1}}^{k}{a}^{i}\frac{\partial }{\partial {x}^{i}}\right| }_{\gamma \left( t\right) } + {\left. \mathop{\sum }\limits_{{j = 1}}^{{n - k}}t{b}^{j}\frac{\partial }{\partial {v}^{j}}\right| }_{\gamma \left( t\right) },
\]

for arbitrary constants \( {a}^{1},\ldots ,{a}^{k},{b}^{1},\ldots ,{b}^{n - k} \) .

10-17. Suppose \( P \) is an embedded submanifold of a Riemannian manifold \( \left( {M, g}\right) \) , and \( U \) is a normal neighborhood of \( P \) in \( M \) . Prove that every tangent vector to \( U \smallsetminus  P \) is the value of a transverse Jacobi field: more precisely, for each \( q \in  U \smallsetminus  P \) and each \( w \in  {T}_{q}M \) , there is a \( g \) -geodesic segment \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) such that \( \gamma \left( 0\right)  \in  P,{\gamma }^{\prime }\left( 0\right)  \bot  {T}_{\gamma \left( 0\right) }P \) , and \( \gamma \left( b\right)  = q \) , and a Jacobi field \( J \) along \( \gamma \) that is transverse to \( P \) and satisfies \( J\left( b\right)  = w \) . [Hint: Use Problem 10-16.]

10-18. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are Riemannian manifolds, \( f : {M}_{1} \rightarrow  {\mathbb{R}}^{ + } \) is a smooth positive function, and \( {M}_{1} \times  {}_{f}{M}_{2} \) is the resulting warped product manifold. Let \( {q}_{0} \in  {M}_{2} \) be arbitrary, let \( \gamma  : I \rightarrow  {M}_{1} \) be a \( {g}_{1} \) -geodesic, and let \( \widetilde{\gamma } : I \rightarrow  {M}_{1}{ \times  }_{f}{M}_{2} \) be the curve \( \widetilde{\gamma }\left( t\right)  = \left( {\gamma \left( t\right) ,{q}_{0}}\right) \) . It follows from the result of Problem 5-7 that \( \widetilde{\gamma } \) is a geodesic meeting each submanifold \( \{ \gamma \left( t\right) \}  \times  {M}_{2} \) orthogonally. Given any fixed vector \( w \in  {T}_{{q}_{0}}{M}_{2} \) , define a vector field \( J \) along \( \widetilde{\gamma } \) by \( J\left( t\right)  = \left( {0, w}\right)  \in  {T}_{\gamma \left( t\right) }{M}_{1} \oplus  {T}_{{q}_{0}}{M}_{2} \) . Prove that \( J \) is a Jacobi field that is transverse to each submanifold \( \{ \gamma \left( t\right) \}  \times  {M}_{2} \) (in the sense defined in Problem 10-14).

10-19. Suppose \( P \) is an embedded submanifold in a Riemannian manifold \( \left( {M, g}\right) \) . A point \( q \in  M \) is said to be a focal point of \( \mathbf{P} \) if it is a critical value of the normal exponential map \( E : {\mathcal{E}}_{P} \rightarrow  M \) (see p. 133). Show that \( q \) is a focal point of \( P \) if and only if there exist a geodesic segment \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) that starts normal to \( P \) and ends at \( q \) and a nontrivial Jacobi field \( J \in  \mathcal{J}\left( \gamma \right) \) that is transverse to \( P \) in the sense defined in Problem 10-14 and satisfies \( J\left( b\right)  = 0 \) . (If this is the case, we say that \( q \) is a focal point of \( P \) along \( \gamma \) .)

10-20. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with nonpositive sectional curvature, and \( P \subseteq  M \) is a totally geodesic embedded submanifold. Prove that \( P \) has no focal points. [Hint: See Problem 10-7.] (Used on p. 370.)

10-21. Determine the cut locus of an arbitrary point in the \( n \) -torus \( {\mathbb{T}}^{n} \) with the flat metric of Examples 2.21 and 7.1.

10-22. Suppose \( \left( {M, g}\right) \) is a connected, compact Riemannian manifold, \( p \in  M \) , and \( C \subseteq  M \) is the cut locus of \( p \) . Prove that \( C \) is homotopy equivalent to \( M \smallsetminus  \{ p\} \) .

10-23. Let \( \left( {M, g}\right) \) be a complete Riemannian manifold, and suppose \( p, q \in  M \) are points such that \( {d}_{g}\left( {p, q}\right) \) is equal to the distance from \( p \) to its cut locus.

(a) Prove that either \( q \) is conjugate to \( p \) along some minimizing geodesic segment, or there are exactly two minimizing geodesic segments from \( p \) to \( q \) , say \( {\gamma }_{1},{\gamma }_{2} : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) , such that \( {\gamma }_{1}^{\prime }\left( b\right)  =  - {\gamma }_{2}^{\prime }\left( b\right) \) .

(b) Now suppose in addition that \( \operatorname{inj}\left( p\right)  = \operatorname{inj}\left( M\right) \) . Prove that if \( q \) is not conjugate to \( p \) along any minimizing geodesic, then there is a closed geodesic \( \gamma  : \left\lbrack  {0,{2b}}\right\rbrack   \rightarrow  M \) such that \( \gamma \left( 0\right)  = \gamma \left( {2b}\right)  = p \) and \( \gamma \left( b\right)  = q \) , where \( b = {d}_{g}\left( {p, q}\right) \) .

(Used on p. 343.)

10-24. Let \( \left( {M, g}\right) \) be a complete Riemannian manifold and \( p \in  M \) . Show that inj \( \left( p\right) \) is equal to the radius of the largest open ball in \( {T}_{p}M \) on which \( {\exp }_{p} \) is injective.

(Used on p. 166.)
