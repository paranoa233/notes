## Chapter 11 Comparison Theory

The purpose of this chapter is to show how upper or lower bounds on curvature can be used to derive bounds on other geometric quantities such as lengths of tangent vectors, distances, and volumes. The intuition behind all the comparison theorems is that negative curvature forces geodesics to spread apart faster as you move away from a point, and positive curvature forces them to spread slower and eventually to begin converging.

One of the most useful comparison theorems is the Jacobi field comparison theorem (see Thm. 11.9 below), which gives bounds on the sizes of Jacobi fields based on curvature bounds. Its importance is based on four observations: first, in a normal neighborhood of a point \( p \) , every tangent vector can be represented as the value of a Jacobi field that vanishes at \( p \) (by Cor. 10.11); second, zeros of Jacobi fields correspond to conjugate points, beyond which geodesics cannot be minimizing; third, Jacobi fields represent the first-order behavior of families of geodesics; and fourth, each Jacobi field satisfies a differential equation that directly involves the curvature.

In the first section of the chapter, we set the stage for the comparison theorems by showing how the growth of Jacobi fields in a normal neighborhood is controlled by the Hessian of the radial distance function, which satisfies a first-order differential equation called a Riccati equation. We then state and prove a fundamental comparison theorem for Riccati equations.

Next we proceed to derive some of the most important geometric comparison theorems that follow from the Riccati comparison theorem. The first few comparison theorems are all based on upper or lower bounds on sectional curvatures. Then we explain how some comparison theorems can also be proved based on lower bounds for the Ricci curvature. In the next chapter, we will see how these comparison theorems can be used to prove significant local-to-global theorems in Riemannian geometry.

Since all of the results in this chapter are deeply intertwined with lengths and distances, we restrict attention throughout the chapter to the Riemannian case.

## Jacobi Fields, Hessians, and Riccati Equations

Our main aim in this chapter is to use curvature inequalities to derive consequences about how fast the metric grows or shrinks, based primarily on size estimates for Jacobi fields. But first, we need to make one last stop along the way.

The Jacobi equation is a second-order differential equation, but comparison theory for differential equations generally works much more smoothly for first-order equations. In order to get the sharpest results about Jacobi fields and other geometric quantities, we will derive a first-order equation, called a Riccati equation, that is closely related to the Jacobi equation.

Let \( \left( {M, g}\right) \) be an \( n \) -dimensional Riemannian manifold, let \( U \) be a normal neighborhood of a point \( p \in  M \) , and let \( r : U \rightarrow  \mathbb{R} \) be the radial distance function as defined by (6.4). The Gauss lemma shows that the gradient of \( r \) on \( U \smallsetminus  \{ p\} \) is the radial vector field \( {\partial }_{r} \) .

On \( U \smallsetminus  \{ p\} \) , we can form the symmetric covariant 2-tensor field \( {\nabla }^{2}r \) (the covariant Hessian of \( r \) ) and the \( \left( {1,1}\right) \) -tensor field \( {\mathcal{H}}_{r} = \nabla \left( {\partial }_{r}\right) \) . Because \( {\partial }_{r} = \operatorname{grad}r = \; {\left( \nabla r\right) }^{\sharp } \) and \( \nabla \) commutes with the musical isomorphisms (Prop. 5.17), we have

\[
{\mathcal{H}}_{r} = \nabla \left( {\partial }_{r}\right)  = \nabla \left( {\left( \nabla r\right) }^{\sharp }\right)  = {\left( {\nabla }^{2}r\right) }^{\sharp }.
\]

In other words, \( {\mathcal{H}}_{r} \) is obtained from \( {\nabla }^{2}r \) by raising one of its indices.

Using Proposition B.1, we can also interpret the \( \left( {1,1}\right) \) -tensor field \( {\mathcal{H}}_{r} \) as an element of \( \Gamma \left( {\operatorname{End}\left( {{TM}{ \mid  }_{U\smallsetminus \{ p\} }}\right) }\right) \) (that is, a field of endomorphisms of \( {TM} \) over \( U \smallsetminus  \{ p\} \) ), defined by

\[
{\mathcal{H}}_{r}\left( w\right)  = {\nabla }_{w}{\partial }_{r} \tag{11.1}
\]

for all \( w \in  {TM}{ \mid  }_{U\smallsetminus \{ p\} } \) . The endomorphism field \( {\mathcal{H}}_{r} \) is called the Hessian operator of \( r \) . It is related to the \( \left( {0,2}\right) \) -Hessian by

\[
\left\langle  {{\mathcal{H}}_{r}\left( v\right) , w}\right\rangle   = \left( {{\nabla }^{2}r}\right) \left( {v, w}\right) ,\;\text{ for all }q \in  U \smallsetminus  \{ p\} \text{ and }v, w \in  {T}_{q}M. \tag{11.2}
\]

The next lemma summarizes some of its basic algebraic properties.

Lemma 11.1. Let \( r,{\partial }_{r} \) , and \( {\mathcal{H}}_{r} \) be defined as above.

(a) \( {\mathcal{H}}_{r} \) is self-adjoint.

(b) \( {\mathcal{H}}_{r}\left( {\partial }_{r}\right)  \equiv  0 \) .

(c) The restriction of \( {\mathcal{H}}_{r} \) to vectors tangent to a level set of \( r \) is equal to the shape operator of the level set associated with the normal vector field \( N =  - {\partial }_{r} \) .

Proof. Since the covariant Hessian \( {\nabla }^{2}r \) is symmetric, equation (11.2) shows that the Hessian operator is self-adjoint. Part (b) follows immediately from the fact that \( {\mathcal{H}}_{r}\left( {\partial }_{r}\right)  = {\nabla }_{{\partial }_{r}}{\partial }_{r} = 0 \) because the integral curves of \( {\partial }_{r} \) are geodesics.

Next, note that \( {\partial }_{r} \) is a unit vector field normal to each level set of \( r \) by the Gauss lemma, so (c) follows from the Weingarten equation 8.11.

Problem 11-1 gives another geometric interpretation of \( {\nabla }^{2}r \) , as the radial derivative of the nonconstant components of the metric in polar normal coordinates.

The Hessian operator also has a close relationship with Jacobi fields.

Proposition 11.2. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( U \subseteq  M \) is a normal neighborhood of \( p \in  M \) , and \( r \) is the radial distance function on \( U \) . If \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) is a unit-speed radial geodesic segment starting at \( p \) , and \( J \in  {\mathcal{J}}^{ \bot  }\left( \gamma \right) \) is a normal Jacobi field along \( \gamma \) that vanishes at \( t = 0 \) , then the following equation holds for all \( t \in  (0, b\rbrack \) :

\[
{D}_{t}J\left( t\right)  = {\mathcal{H}}_{r}\left( {J\left( t\right) }\right) \tag{11.3}
\]

Proof. Let \( v = {\gamma }^{\prime }\left( 0\right) \) , so \( {\left| v\right| }_{g} = 1 \) and \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) . Proposition 10.10 shows that

\[
J\left( t\right)  = d{\left( {\exp }_{p}\right) }_{tv}\left( {tw}\right) ,
\]

where \( {D}_{t}J\left( 0\right)  = w = {\left. {w}^{i}{\partial }_{i}\right| }_{p} \) . Because we are assuming that \( J \) is normal, it follows from Proposition 10.7 that \( w \bot  v \) .

Because \( w \bot  v \) ensures that \( w \) is tangent to the unit sphere in \( {T}_{p}M \) at \( v \) , we can choose a smooth curve \( \sigma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  {T}_{p}M \) that satisfies \( {\left| \sigma \left( s\right) \right| }_{g} = 1 \) for all \( s \in  \left( {-\varepsilon ,\varepsilon }\right) \) , with initial conditions \( \sigma \left( 0\right)  = v \) and \( {\sigma }^{\prime }\left( 0\right)  = w \) . (As always, we are using the canonical identification between \( {T}_{v}\left( {{T}_{p}M}\right) \) and \( {T}_{p}M \) .) Define a smooth family of curves \( \Gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) by \( \Gamma \left( {s, t}\right)  = {\exp }_{p}\left( {{t\sigma }\left( s\right) }\right) \) . Then \( \Gamma \left( {0, t}\right)  = \; {\exp }_{p}\left( {tv}\right)  = \gamma \left( t\right) \) , so \( \Gamma \) is a variation of \( \gamma \) . The stipulation that \( {\left| \sigma \left( s\right) \right| }_{g} \equiv  1 \) ensures that each main curve \( {\Gamma }_{s}\left( t\right)  = \Gamma \left( {s, t}\right) \) is a unit-speed radial geodesic, so its velocity satisfies the following identity for all \( \left( {s, t}\right) \) :

\[
{\partial }_{t}\Gamma \left( {s, t}\right)  = {\left( {\Gamma }_{s}\right) }^{\prime }\left( t\right)  = {\left. {\partial }_{r}\right| }_{\Gamma \left( {s, t}\right) }. \tag{11.4}
\]

The chain rule yields

\[
{\partial }_{s}\Gamma \left( {0, t}\right)  = d{\left( {\exp }_{p}\right) }_{{t\sigma }\left( 0\right) }\left( {t{\sigma }^{\prime }\left( 0\right) }\right)  = d{\left( {\exp }_{p}\right) }_{tv}\left( {tw}\right)  = J\left( t\right) ,
\]

so \( J \) is the variation field of \( \Gamma \) . By the symmetry lemma,

\[
{D}_{t}J\left( t\right)  = {D}_{t}{\partial }_{s}\Gamma \left( {0, t}\right)  = {D}_{s}{\partial }_{t}\Gamma \left( {0, t}\right) . \tag{11.5}
\]

This last expression is the covariant derivative of \( {\partial }_{t}\Gamma \left( {s, t}\right) \) along the curve \( {\Gamma }^{\left( t\right) }\left( s\right)  = \; \Gamma \left( {s, t}\right) \) evaluated at \( s = 0 \) . Since the velocity of this curve at \( s = 0 \) is \( {\partial }_{s}\Gamma \left( {0, t}\right)  = \; J\left( t\right) \) and \( {\partial }_{t}\Gamma \left( {s, t}\right)  = {\partial }_{r} \) is an extendible vector field by (11.4), we obtain

\[
{D}_{s}{\partial }_{t}\Gamma \left( {0, t}\right)  = {\nabla }_{{\Gamma }^{\left( t\right) \prime }\left( 0\right) }\left( {\partial }_{r}\right)  = {\nabla }_{J\left( t\right) }\left( {\partial }_{r}\right)  = {\mathcal{H}}_{r}\left( {J\left( t\right) }\right) .
\]

Combining this with (11.5) yields the result.

In order to compare the Hessian operator of an arbitrary metric with those of the constant-curvature models, we need the following explicit formula for the constant-curvature case.

Proposition 11.3. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( U \subseteq  M \) is a normal neighborhood of \( p \in  M \) , and \( r \) is the radial distance function on \( U \) . Then \( g \) has constant sectional curvature \( c \) on \( U \) if and only if the following formula holds at all points of \( U \smallsetminus  \{ p\} \) :

\[
{\mathcal{H}}_{r} = \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }{\pi }_{r}, \tag{11.6}
\]

where \( {s}_{c} \) is defined by (10.8), and for each \( q \in  U \smallsetminus  \{ p\} ,{\pi }_{r} : {T}_{q}M \rightarrow  {T}_{q}M \) is the orthogonal projection onto the tangent space of the level set of r (equivalently, onto the orthogonal complement of \( {\left. {\partial }_{r}\right| }_{q} \) ).

Proof. First suppose \( g \) has constant sectional curvature \( c \) on \( U \) . Let \( q \in  U \smallsetminus  \{ p\} \) , and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) be the unit-speed radial geodesic from \( p \) to \( q \) , so \( b = r\left( q\right) \) . Let \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be a parallel orthonormal frame along \( \gamma \) , chosen so that \( {E}_{n}\left( t\right)  = \; {\gamma }^{\prime }\left( t\right)  = {\left. {\partial }_{r}\right| }_{\gamma \left( t\right) } \) . It follows from Proposition 10.12 that for \( i = 1,\ldots , n - 1 \) , the vector fields \( {J}_{i}\left( t\right)  = {s}_{c}\left( t\right) {E}_{i}\left( t\right) \) are normal Jacobi fields along \( \gamma \) that vanish at \( t = 0 \) . The assumption that \( U \) is a normal neighborhood of \( p \) means that \( U = {\exp }_{p}\left( V\right) \) for some star-shaped neighborhood \( V \) of \( 0 \in  {T}_{p}M \) , and every point of \( V \) is a regular point for \( {\exp }_{p} \) . Thus Proposition 10.20 shows that \( p \) has no conjugate points along \( \gamma \) , which implies that \( {s}_{c}\left( t\right)  \neq  0 \) for \( t \in  (0, b\rbrack \) . (For \( c \leq  0 \) , this is automatic, because \( {s}_{c} \) vanishes only at 0 ; but in the case \( c = 1/{R}^{2} > 0 \) , it means that \( b < {\pi R} \) .)

For \( 1 \leq  i \leq  n - 1 \) , we use Proposition 11.2 to compute

\[
{D}_{t}{J}_{i}\left( t\right)  = {\mathcal{H}}_{r}\left( {{J}_{i}\left( t\right) }\right)  = {s}_{c}\left( t\right) {\mathcal{H}}_{r}\left( {{E}_{i}\left( t\right) }\right) .
\]

On the other hand, because each \( {E}_{i} \) is parallel along \( \gamma \) ,

\[
{D}_{t}{J}_{i}\left( t\right)  = {s}_{c}^{\prime }\left( t\right) {E}_{i}\left( t\right) .
\]

Comparing these two equations at \( t = b \) and dividing by \( {s}_{c}\left( b\right) \) , we obtain

\[
{\mathcal{H}}_{r}\left( {{E}_{i}\left( b\right) }\right)  = \frac{{s}_{c}^{\prime }\left( b\right) }{{s}_{c}\left( b\right) }{E}_{i}\left( b\right)  = \frac{{s}_{c}^{\prime }\left( b\right) }{{s}_{c}\left( b\right) }{\pi }_{r}\left( {{E}_{i}\left( b\right) }\right) .
\]

On the other hand, Lemma 11.1(b) shows that

\[
{\mathcal{H}}_{r}\left( {{E}_{n}\left( b\right) }\right)  = {\mathcal{H}}_{r}\left( {\left. {\partial }_{r}\right| }_{q}\right)  = 0 = \frac{{s}_{c}^{\prime }\left( b\right) }{{s}_{c}\left( b\right) }{\pi }_{r}\left( {{E}_{n}\left( b\right) }\right) ,
\]

because \( {\pi }_{r}\left( {{E}_{n}\left( b\right) }\right)  = {\pi }_{r}\left( {\left. {\partial }_{r}\right| }_{q}\right)  = 0 \) . Since \( \left( {{E}_{i}\left( b\right) }\right) \) is a basis for \( {T}_{q}M \) , this proves (11.6).

Conversely, suppose \( {\mathcal{H}}_{r} \) is given by (11.6). Let \( \gamma \) be a radial geodesic starting at \( p \) , and let \( J \) be a normal Jacobi field along \( \gamma \) that vanishes at \( t = 0 \) . By Proposition 11.2, \( {D}_{t}J\left( t\right)  = {\mathcal{H}}_{r}J\left( t\right)  = {s}_{c}^{\prime }\left( t\right) J\left( t\right) /{s}_{c}\left( t\right) \) . A straightforward computation then shows that \( {s}_{c}{\left( t\right) }^{-1}J\left( t\right) \) is parallel along \( \gamma \) . Thus we can write every such Jacobi field in the form \( J\left( t\right)  = k{s}_{c}\left( t\right) E\left( t\right) \) for some constant \( k \) and some parallel unit normal vector field \( E \) along \( \gamma \) . Proceeding exactly as in the proof of Theorem 10.14, we conclude that \( g \) is given by formula (10.17) in these coordinates, and therefore has constant sectional curvature \( c \) .

![bo_d7dtff491nqc73eq8m7g_332_386_190_765_663_0.jpg](images/bo_d7dtff491nqc73eq8m7g_332_386_190_765_663_0.jpg)

Fig. 11.1: The graph of \( {s}_{c}^{\prime }/{s}_{c} \)

For convenience, we record the exact formulas for the quotient \( {s}_{c}^{\prime }/{s}_{c} \) that appeared in the previous proposition (see Fig. 11.1):

\[
\frac{{s}_{c}^{\prime }\left( t\right) }{{s}_{c}\left( t\right) } = \left\{  \begin{array}{ll} \frac{1}{t}, & \text{ if }c = 0; \\  \frac{1}{R}\cot \frac{t}{R}, & \text{ if }c = \frac{1}{{R}^{2}} > 0; \\  \frac{1}{R}\coth \frac{t}{R}, & \text{ if }c =  - \frac{1}{{R}^{2}} < 0. \end{array}\right.
\]

Now we are in a position to derive the first-order equation mentioned at the beginning of this section. (Problem 11-3 asks you to show, with a different argument, that the conclusion of the next theorem holds for the Hessian operator of every smooth local distance function, not just the radial distance function in a normal neighborhood.) This theorem concerns the covariant derivative of the endomorphism field \( {\mathcal{H}}_{r} \) along a curve \( \gamma \) . We can compute the action of \( {D}_{t}{\mathcal{H}}_{r} \) on every \( V \in  \mathfrak{X}\left( \gamma \right) \) by noting that \( {\mathcal{H}}_{r}\left( {V\left( t\right) }\right) \) is a contraction of \( {\mathcal{H}}_{r} \otimes  V\left( t\right) \) , so the product rule implies \( {D}_{t}\left( {{\mathcal{H}}_{r}\left( V\right) }\right)  = \left( {{D}_{t}{\mathcal{H}}_{r}}\right) V + {\mathcal{H}}_{r}\left( {{D}_{t}V}\right) . \)

Theorem 11.4 (The Riccati Equation). Let \( \left( {M, g}\right) \) be a Riemannian manifold; let \( U \) be a normal neighborhood of a point \( p \in  M \) ; let \( r : U \rightarrow  \mathbb{R} \) be the radial distance function; and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) be a unit-speed radial geodesic. The Hessian operator \( {\mathcal{H}}_{r} \) satisfies the following equation along \( {\left. \gamma \right| }_{(0, b\rbrack } \) , called a Riccati equation:

\[
{D}_{t}{\mathcal{H}}_{r} + {\mathcal{H}}_{r}^{2} + {R}_{{\gamma }^{\prime }} = 0 \tag{11.7}
\]

where \( {\mathcal{H}}_{r}^{2} \) and \( {R}_{{\gamma }^{\prime }} \) are the endomorphism fields along \( \gamma \) defined by \( {\mathcal{H}}_{r}^{2}\left( w\right)  = \; {\mathcal{H}}_{r}\left( {{\mathcal{H}}_{r}\left( w\right) }\right) \) and \( {R}_{{\gamma }^{\prime }}\left( w\right)  = R\left( {w,{\gamma }^{\prime }}\right) {\gamma }^{\prime } \) , with \( R \) the curvature endomorphism of \( g \) .

Proof. Let \( {t}_{0} \in  (0, b\rbrack \) and \( w \in  {T}_{\gamma \left( {t}_{0}\right) }M \) be arbitrary. We can decompose \( w \) as \( w = \; y + z \) , where \( y \) is a multiple of \( {\partial }_{r} \) and \( z \) is tangent to a level set of \( r \) . Since (11.7) is an equation between linear operators, we can prove the equation by evaluating it separately on \( y \) and \( z \) .

Because \( \gamma \) is a unit-speed radial geodesic, its velocity is equal to \( {\partial }_{r} \) , and thus \( {D}_{t}{\partial }_{r} = 0 \) along \( \gamma \) . It follows that \( \left( {{D}_{t}{\mathcal{H}}_{r}}\right) \left( {\partial }_{r}\right)  = {D}_{t}\left( {{\mathcal{H}}_{r}\left( {\partial }_{r}\right) }\right)  - {\mathcal{H}}_{r}\left( {{D}_{t}{\partial }_{r}}\right)  = 0 \) . Since all three terms on the left-hand side of (11.7) annihilate \( {\partial }_{r} \) , the equation holds when applied to any multiple of \( {\partial }_{r} \) .

Next we consider a vector \( z \in  {T}_{\gamma \left( {t}_{0}\right) }M \) that is tangent to a level set of \( r \) , and thus by the Gauss lemma orthogonal to \( {\gamma }^{\prime }\left( {t}_{0}\right) \) . By Corollary 10.11, \( z \) can be expressed as the value at \( t = {t}_{0} \) of a Jacobi field \( J \) along \( \gamma \) vanishing at \( t = 0 \) . Because \( J\left( 0\right) \) and \( J\left( {t}_{0}\right) \) are orthogonal to \( {\gamma }^{\prime } \) , it follows that \( J \) is a normal Jacobi field, so Proposition 11.2 shows that \( {D}_{t}J\left( t\right)  = {\mathcal{H}}_{r}\left( {J\left( t\right) }\right) \) for all \( t \in  \left\lbrack  {0, b}\right\rbrack \) . Differentiation yields

\[
{D}_{t}^{2}J = {D}_{t}\left( {{\mathcal{H}}_{r}\left( J\right) }\right)  = \left( {{D}_{t}{\mathcal{H}}_{r}}\right) J + {\mathcal{H}}_{r}\left( {{D}_{t}J}\right)  = \left( {{D}_{t}{\mathcal{H}}_{r}}\right) J + {\mathcal{H}}_{r}\left( {{\mathcal{H}}_{r}\left( J\right) }\right) .
\]

On the other hand, the Jacobi equation gives \( {D}_{t}^{2}J =  - {R}_{{\gamma }^{\prime }}\left( J\right) \) , so

\[
\left( {{D}_{t}{\mathcal{H}}_{r} + {\mathcal{H}}_{r}^{2} + {R}_{{\gamma }^{\prime }}}\right) \left( J\right)  \equiv  0.
\]

Evaluating this at \( t = {t}_{0} \) proves the result.

The Riccati equation is named after Jacopo Riccati, an eighteenth-century Italian mathematician who studied scalar differential equations of the form \( {v}^{\prime } + p{v}^{2} + \; {qv} + r = 0 \) , where \( p, q, r \) are known functions and \( v \) is an unknown function of one real variable. As is shown in some ODE texts, a linear second-order equation in one variable of the form \( a{u}^{\prime \prime } + b{u}^{\prime } + {cu} = 0 \) can be transformed to a Riccati equation wherever \( u \neq  0 \) by making the substitution \( v = {u}^{\prime }/u \) . The relation (11.3) generalizes this, and allows us to replace the analysis of the second-order linear Jacobi equation by an analysis of the first-order nonlinear Riccati equation.

The primary tool underlying all of our geometric comparison theorems is a fundamental comparison theorem for solutions to Riccati equations. It says, roughly, that a larger curvature term results in a smaller solution, and vice versa. When we apply this to (11.3), it will yield an analogous comparison for Jacobi fields.

In the statement and proof of this theorem, we will compare self-adjoint en-domorphisms by comparing the quadratic forms they determine. Given a finite-dimensional inner product space \( V \) and self-adjoint endomorphisms \( A, B : V \rightarrow  V \) , the notation \( A \leq  B \) means that \( \langle {Av}, v\rangle  \leq  \langle {Bv}, v\rangle \) for all \( v \in  V \) , or equivalently that \( B - A \) is positive semidefinite. In particular, \( B \geq  0 \) means that \( B \) is positive semidefinite. Note that the square of every self-adjoint endomorphism is positive semidefinite, because \( \left\langle  {{B}^{2}v, v}\right\rangle   = \langle {Bv},{Bv}\rangle  \geq  0 \) for all \( v \in  V \) .

Theorem 11.5 (Riccati Comparison Theorem). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic segment. Suppose \( \eta ,\widetilde{\eta } \) are self-adjoint endomorphism fields along \( {\left. \gamma \right| }_{(a, b\rbrack } \) that satisfy the following Riccati equations:

\[
{D}_{t}\eta  + {\eta }^{2} + \sigma  = 0,\;{D}_{t}\widetilde{\eta } + {\widetilde{\eta }}^{2} + \widetilde{\sigma } = 0, \tag{11.8}
\]

where \( \sigma \) and \( \widetilde{\sigma } \) are continuous self-adjoint endomorphism fields along \( \gamma \) satisfying

\[
\widetilde{\sigma }\left( t\right)  \geq  \sigma \left( t\right) \text{ for all }t \in  \left\lbrack  {a, b}\right\rbrack  . \tag{11.9}
\]

Suppose further that \( \mathop{\lim }\limits_{{t \searrow  a}}\left( {\widetilde{\eta }\left( t\right)  - \eta \left( t\right) }\right) \) exists and satisfies

\[
\mathop{\lim }\limits_{{t \searrow  a}}\left( {\widetilde{\eta }\left( t\right)  - \eta \left( t\right) }\right)  \leq  0.
\]

Then

\[
\widetilde{\eta }\left( t\right)  \leq  \eta \left( t\right) \;\text{ for all }t \in  (a, b\rbrack .
\]

To prove this theorem, we will express the endomorphism fields \( \eta ,\widetilde{\eta },\sigma \) , and \( \widetilde{\sigma } \) in terms of a parallel orthonormal frame along \( \gamma \) . In this frame, they become symmetric matrix-valued functions, and then the Riccati equations for \( \eta \) and \( \widetilde{\eta } \) become ordinary differential equations for these matrix-valued functions. The crux of the matter is the following comparison theorem for solutions to such matrix-valued equations.

Let \( \mathrm{M}\left( {n,\mathbb{R}}\right) \) be the space of all \( n \times  n \) real matrices, viewed as linear endomor-phisms of \( {\mathbb{R}}^{n} \) , and let \( \mathrm{S}\left( {n,\mathbb{R}}\right)  \subseteq  \mathrm{M}\left( {n,\mathbb{R}}\right) \) be the subspace of symmetric matrices, corresponding to self-adjoint endomorphisms of \( {\mathbb{R}}^{n} \) with respect to the standard inner product.

Theorem 11.6 (Matrix Riccati Comparison Theorem). Suppose \( H,\widetilde{H} : (a, b\rbrack  \rightarrow \; \mathrm{S}\left( {n,\mathbb{R}}\right) \) satisfy the following matrix Riccati equations:

\[
{H}^{\prime } + {H}^{2} + S = 0,\;{\widetilde{H}}^{\prime } + {\widetilde{H}}^{2} + \widetilde{S} = 0, \tag{11.10}
\]

where \( S,\widetilde{S} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathrm{S}\left( {n,\mathbb{R}}\right) \) are continuous and satisfy

\[
\widetilde{S}\left( t\right)  \geq  S\left( t\right) \text{ for all }t \in  \left\lbrack  {a, b}\right\rbrack  \text{ . } \tag{11.11}
\]

Suppose further that \( \mathop{\lim }\limits_{{t \searrow  a}}\left( {\widetilde{H}\left( t\right)  - H\left( t\right) }\right) \) exists and satisfies

\[
\mathop{\lim }\limits_{{t \searrow  a}}\left( {\widetilde{H}\left( t\right)  - H\left( t\right) }\right)  \leq  0. \tag{11.12}
\]

Then

\[
\widetilde{H}\left( t\right)  \leq  H\left( t\right) \;\text{ for all }t \in  (a, b\rbrack . \tag{11.13}
\]

Proof. Define functions \( A, B : (a, b\rbrack  \rightarrow  \mathrm{S}\left( {n,\mathbb{R}}\right) \) by

\[
A\left( t\right)  = \widetilde{H}\left( t\right)  - H\left( t\right) ,\;B\left( t\right)  =  - \frac{1}{2}\left( {\widetilde{H}\left( t\right)  + H\left( t\right) }\right) .
\]

The hypothesis implies that \( A \) extends to a continuous matrix-valued function (still denoted by \( A \) ) on \( \left\lbrack  {a, b}\right\rbrack \) satisfying \( A\left( a\right)  \leq  0 \) . We need to show that \( A\left( t\right)  \leq  0 \) for all \( t \in  (a, b\rbrack \) .

Simple computations show that the following equalities hold on \( (a, b\rbrack \) :

\[
{A}^{\prime } = {BA} + {AB} - \widetilde{S} + S
\]

\[
{B}^{\prime } = \frac{1}{2}\left( {{\widetilde{H}}^{2} + \widetilde{S} + {H}^{2} + S}\right) .
\]

Our hypotheses applied to these formulas imply

\[
{A}^{\prime } \leq  {BA} + {AB}, \tag{11.14}
\]

\[
{B}^{\prime } \geq  k\text{ Id, } \tag{11.15}
\]

where the last inequality holds for some (possibly negative) real number \( k \) because \( {H}^{2} \) and \( {\widetilde{H}}^{2} \) are positive semidefinite and \( S \) and \( \widetilde{S} \) are continuous on all of \( \left\lbrack  {a, b}\right\rbrack \) and thus bounded below. Therefore, for every \( t \in  (a, b\rbrack \) ,

\[
B\left( t\right)  = B\left( b\right)  - {\int }_{t}^{b}{B}^{\prime }\left( u\right) {du} \tag{11.16}
\]

\[
\leq  B\left( b\right)  - \left( {b - t}\right) k\operatorname{Id} \leq  B\left( b\right)  + \left| {b - a}\right| \left| k\right| \operatorname{Id}
\]

which shows that \( B\left( t\right) \) is bounded above on \( (a, b\rbrack \) . Let \( K \) be a constant large enough that \( B\left( t\right)  - K\operatorname{Id} \) is negative definite for all such \( t \) .

Define a continuous function \( f : \left\lbrack  {a, b}\right\rbrack   \times  {\mathbb{S}}^{n - 1} \rightarrow  \mathbb{R} \) by

\[
f\left( {t, x}\right)  = {e}^{-{2Kt}}\langle A\left( t\right) x, x\rangle .
\]

To prove the theorem, we need to show that \( f\left( {t, x}\right)  \leq  0 \) for all \( \left( {t, x}\right)  \in  \left\lbrack  {a, b}\right\rbrack   \times  {\mathbb{S}}^{n - 1} \) . Suppose this is not the case; then by compactness of \( \left\lbrack  {a, b}\right\rbrack   \times  {\mathbb{S}}^{n - 1}, f \) takes on a positive maximum at some \( \left( {{t}_{0},{x}_{0}}\right)  \in  \left\lbrack  {a, b}\right\rbrack   \times  {\mathbb{S}}^{n - 1} \) . Since \( f\left( {a, x}\right)  = 0 \) for all \( x \) , we must have \( a < {t}_{0} \leq  b \) . Because \( \left\langle  {A\left( {t}_{0}\right) x, x}\right\rangle   \leq  \left\langle  {A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle \) for all \( x \in  {\mathbb{S}}^{n - 1} \) , it follows from Lemma 8.14 that \( {x}_{0} \) is an eigenvector of \( A\left( {t}_{0}\right) \) with eigenvalue \( {\lambda }_{0} = \left\langle  {A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle   > 0. \)

Since \( f \) is differentiable at \( \left( {{t}_{0},{x}_{0}}\right) \) and \( f\left( {t,{x}_{0}}\right)  \leq  f\left( {{t}_{0},{x}_{0}}\right) \) for \( a < t < {t}_{0} \) , we have

\[
\frac{\partial f}{\partial t}\left( {{t}_{0},{x}_{0}}\right)  = \mathop{\lim }\limits_{{t \nearrow  {t}_{0}}}\frac{f\left( {t,{x}_{0}}\right)  - f\left( {{t}_{0},{x}_{0}}\right) }{t - {t}_{0}} \geq  0.
\]

(We have to take a one-sided limit here to accommodate the fact that \( {t}_{0} \) might equal b.) On the other hand, from (11.14) and the fact that \( A\left( {t}_{0}\right) \) and \( B\left( {t}_{0}\right) \) are self-adjoint, we have

\[
\frac{\partial f}{\partial t}\left( {{t}_{0},{x}_{0}}\right)  = {e}^{-{2K}{t}_{0}}\left( {\left\langle  {{A}^{\prime }\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle   - {2K}\left\langle  {A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle  }\right)
\]

\[
\leq  {e}^{-{2K}{t}_{0}}\left( {\left\langle  {B\left( {t}_{0}\right) A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle   + \left\langle  {A\left( {t}_{0}\right) B\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle   - {2K}\left\langle  {A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle  }\right)
\]

\[
= {e}^{-{2K}{t}_{0}}\left( {2\left\langle  {A\left( {t}_{0}\right) {x}_{0}, B\left( {t}_{0}\right) {x}_{0}}\right\rangle   - {2K}\left\langle  {A\left( {t}_{0}\right) {x}_{0},{x}_{0}}\right\rangle  }\right)
\]

\[
= {e}^{-{2K}{t}_{0}}\left( {2{\lambda }_{0}\left\langle  {{x}_{0},\left( {B\left( {t}_{0}\right)  - K\operatorname{Id}}\right) {x}_{0}}\right\rangle  }\right)  < 0.
\]

These two inequalities contradict each other, thus completing the proof.

Proof of Theorem 11.5. Suppose \( \eta ,\widetilde{\eta },\sigma \) , and \( \widetilde{\sigma } \) are self-adjoint endomorphism fields along \( \gamma \) satisfying the hypotheses of the theorem. Let \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be a parallel orthonormal frame along \( \gamma \) , and let \( H,\widetilde{H} : (a, b\rbrack  \rightarrow  \mathrm{S}\left( {n,\mathbb{R}}\right) \) and \( S,\widetilde{S} : \left\lbrack  {a, b}\right\rbrack   \rightarrow \; \mathrm{S}\left( {n,\mathbb{R}}\right) \) be the symmetric matrix-valued functions defined by

\[
\eta \left( t\right) \left( {{E}_{i}\left( t\right) }\right)  = {H}_{i}^{j}\left( t\right) {E}_{j}\left( t\right) ,\;\widetilde{\eta }\left( t\right) \left( {{E}_{i}\left( t\right) }\right)  = {\widetilde{H}}_{i}^{j}\left( t\right) {E}_{j}\left( t\right) ,
\]

\[
\sigma \left( t\right) \left( {{E}_{i}\left( t\right) }\right)  = {S}_{i}^{j}\left( t\right) {E}_{j}\left( t\right) ,\;\widetilde{\sigma }\left( t\right) \left( {{E}_{i}\left( t\right) }\right)  = {\widetilde{S}}_{i}^{j}\left( t\right) {E}_{j}\left( t\right) .
\]

Because \( {D}_{t}{E}_{j} \equiv  0 \) , the Riccati equations (11.8) reduce to the ordinary differential equations (11.10) for these matrix-valued functions. Theorem 11.6 shows that \( \widetilde{H}\left( t\right)  \leq  H\left( t\right) \) for all \( t \in  (a, b\rbrack \) , which in turn implies that \( \widetilde{\eta }\left( t\right)  \leq  \eta \left( t\right) \) .

## Comparisons Based on Sectional Curvature

Now we are ready to establish some comparison theorems for metric quantities based on comparing sizes of Hessian operators and Jacobi fields for an arbitrary metric with those of the constant-curvature models.

The most fundamental comparison theorem is the following result, which compares the Hessian of the radial distance function with its counterpart for a constant-curvature metric.

Theorem 11.7 (Hessian Comparison). Suppose \( \left( {M, g}\right) \) is a Riemannian n-manifold, \( p \in  M, U \) is a normal neighborhood of \( p \) , and \( r \) is the radial distance function on \( U \) .

(a) If all sectional curvatures of \( M \) are bounded above by a constant \( c \) , then the following inequality holds in \( {U}_{0} \smallsetminus  \{ p\} \) :

\[
{\mathcal{H}}_{r} \geq  \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }{\pi }_{r} \tag{11.17}
\]

where \( {s}_{c} \) and \( {\pi }_{r} \) are defined as in Proposition 11.3, and \( {U}_{0} = U \) if \( c \leq  0 \) , while \( {U}_{0} = \{ q \in  U : r\left( q\right)  < {\pi R}\} \) if \( c = 1/{R}^{2} > 0 \) .

(b) If all sectional curvatures of \( M \) are bounded below by a constant \( c \) , then the following inequality holds in all of \( U \smallsetminus  \{ p\} \) :

\[
{\mathcal{H}}_{r} \leq  \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }{\pi }_{r}. \tag{11.18}
\]

Proof. Let \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) be Riemannian normal coordinates on \( U \) centered at \( p \) , let \( r \) be the radial distance function on \( U \) , and let \( {s}_{c} \) be the function defined by (10.8). Let \( {U}_{0} \subseteq  U \) be the subset on which \( {s}_{c}\left( r\right)  > 0 \) ; when \( c \leq  0 \) , this is all of \( U \) , but when \( c = 1/{R}^{2} > 0 \) , it is the subset where \( r < {\pi R} \) . Let \( {\mathcal{H}}_{r}^{c} \) be the endomorphism field on \( {U}_{0} \smallsetminus  \{ p\} \) given by

\[
{\mathcal{H}}_{r}^{c} = \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }{\pi }_{r}.
\]

Let \( q \in  {U}_{0} \smallsetminus  \{ p\} \) be arbitrary, and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  {U}_{0} \) be the unit-speed radial geodesic from \( p \) to \( q \) . Note that at every point \( \gamma \left( t\right) \) for \( 0 < t \leq  b \) , the endomorphism field \( {\pi }_{r} \) can be expressed as \( {\pi }_{r}\left( w\right)  = w - \left\langle  {w,{\partial }_{r}}\right\rangle  {\partial }_{r} = w - \left\langle  {w,{\gamma }^{\prime }}\right\rangle  {\gamma }^{\prime } \) , and in this form it extends smoothly to an endomorphism field along all of \( \gamma \) . Moreover, since \( {D}_{t}{\gamma }^{\prime } = 0 \) along \( \gamma \) , it follows that \( {D}_{t}{\pi }_{r} = 0 \) along \( \gamma \) as well. Therefore, direct computation using the facts that \( {s}_{c}^{\prime \prime } =  - c{s}_{c} \) and \( {\pi }_{r}^{2} = {\pi }_{r} \) shows that \( {\mathcal{H}}_{r}^{c} \) satisfies the following Riccati equation along \( {\left. \gamma \right| }_{(0, b\rbrack } \) :

\[
{D}_{t}{\mathcal{H}}_{r}^{c} + {\left( {\mathcal{H}}_{r}^{c}\right) }^{2} + c{\pi }_{r} = 0.
\]

On the other hand, Theorem 11.4 shows that \( {\mathcal{H}}_{r} \) satisfies

\[
{D}_{t}{\mathcal{H}}_{r} + {\mathcal{H}}_{r}^{2} + {R}_{{\gamma }^{\prime }} = 0.
\]

The sectional curvature hypothesis implies that \( {R}_{{\gamma }^{\prime }} \leq  c{\pi }_{r} \) in case (a) and \( {R}_{{\gamma }^{\prime }} \geq  c{\pi }_{r} \) in case (b), using the facts that \( {R}_{{\gamma }^{\prime }}\left( {\gamma }^{\prime }\right)  = 0 = {\pi }_{r}\left( {\gamma }^{\prime }\right) \) , and \( \left\langle  {{R}_{{\gamma }^{\prime }}\left( w\right) , w}\right\rangle   = \sec \left( {{\gamma }^{\prime }, w}\right) \) if \( w \) is a unit vector orthogonal to \( {\gamma }^{\prime } \) .

In order to apply the Riccati comparison theorem to \( {\mathcal{H}}_{r} \) and \( {\mathcal{H}}_{r}^{c} \) , we need to show that \( {\mathcal{H}}_{r} - {\mathcal{H}}_{r}^{c} \) has a finite limit along \( \gamma \) as \( t \searrow  0 \) . A straightforward series expansion shows that no matter what \( c \) is,

\[
{s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right)  = 1/r + O\left( r\right) \tag{11.19}
\]

as \( r \searrow  0 \) . We will show that \( {\mathcal{H}}_{r} \) satisfies the analogous estimate:

\[
{\mathcal{H}}_{r} = \frac{1}{r}{\pi }_{r} + O\left( r\right) . \tag{11.20}
\]

The easiest way to verify (11.20) is to note that on \( U \smallsetminus  \{ p\} ,{\mathcal{H}}_{r} \) has the following coordinate expression in normal coordinates:

\[
{\mathcal{H}}_{r} = {g}^{ij}\left( {{\partial }_{j}{\partial }_{k}r - {\Gamma }_{jk}^{m}{\partial }_{m}r}\right) {\partial }_{i} \otimes  d{x}^{k}.
\]

Now \( {\partial }_{m}r = {x}^{m}/r \) , which is bounded on \( U \smallsetminus  \{ p\} \) , and \( {\partial }_{j}{\partial }_{k}r = O\left( {r}^{-1}\right) \) . Moreover, \( {g}^{ij} = {\delta }^{ij} + O\left( {r}^{2}\right) \) and \( {\Gamma }_{jk}^{m} = O\left( r\right) \) , so \( {\mathcal{H}}_{r} \) is equal to \( {\delta }^{ij}\left( {{\partial }_{j}{\partial }_{k}r}\right) {\partial }_{i} \otimes  d{x}^{k} \) plus terms that are \( O\left( r\right) \) in these coordinates. But this last expression is exactly the coordinate expression for \( {\mathcal{H}}_{r} \) in the case of the Euclidean metric in normal coordinates, which Proposition 11.3 shows is equal to \( \left( {1/r}\right) {\pi }_{r} \) . This proves (11.20), from which we conclude that \( {\mathcal{H}}_{r} - {\mathcal{H}}_{r}^{c} \) approaches zero along \( \gamma \) as \( t \searrow  0 \) .

If the sectional curvatures of \( g \) are bounded above by \( c \) , then the arguments above show that the hypotheses of the Riccati comparison theorem are satisfied along \( {\left. \gamma \right| }_{\left\lbrack  0, b\right\rbrack  } \) with \( \eta \left( t\right)  = {\left. {\left. {\mathcal{H}}_{r}\right| }_{\gamma \left( t\right) },\sigma \left( t\right)  = {R}_{{\gamma }^{\prime }}\right| }_{\gamma \left( t\right) },\widetilde{\eta }\left( t\right)  = {\left. {\left. {\mathcal{H}}_{r}^{c}\right| }_{\gamma \left( t\right) }\text{ , and }\widetilde{\sigma }\left( t\right)  = c{\pi }_{r}\right| }_{\gamma \left( t\right) } \) . It follows that \( {\mathcal{H}}_{r} \geq  {\mathcal{H}}_{r}^{c} \) at \( q = \gamma \left( b\right) \) , thus proving (a).

On the other hand, if the sectional curvatures are bounded below by \( c \) , the same argument with the roles of \( {\mathcal{H}}_{r} \) and \( {\mathcal{H}}_{r}^{c} \) reversed shows that \( {\mathcal{H}}_{r} \leq  {\mathcal{H}}_{r}^{c} \) on \( {U}_{0} \) . It remains only to show that \( {U}_{0} = U \) in this case. If \( c \leq  0 \) , this is automatic. If \( c = \; 1/{R}^{2} > 0 \) , then \( {s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right)  \rightarrow   - \infty \) as \( r \nearrow  {\pi R} \) ; since \( {\mathcal{H}}_{r} \) is defined and smooth in all of \( U \smallsetminus  \{ p\} \) and bounded above by \( {\mathcal{H}}_{r}^{c} \) , it must be the case that \( r < {\pi R} \) in \( U \) , which implies that \( {U}_{0} = U \) .

Corollary 11.8 (Principal Curvature Comparison). Suppose \( \left( {M, g}\right) \) is a Riemannian n-manifold, \( p \in  M, U \) is a normal neighborhood of \( p, r \) is the radial distance function on \( U \) , and \( {s}_{c} \) and \( {\pi }_{r} \) are defined as in Proposition 11.3.

(a) If all sectional curvatures of \( M \) are bounded above by a constant \( c \) , then the principal curvatures of the \( r \) -level sets in \( {U}_{0} \smallsetminus  \{ p\} \) (with respect to the inward unit normal) satisfy

\[
\kappa  \geq  \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) },
\]

where \( {U}_{0} = U \) if \( c \leq  0 \) , while \( {U}_{0} = \{ q \in  U : r\left( q\right)  < {\pi R}\} \) if \( c = 1/{R}^{2} > 0 \) .

(b) If all sectional curvatures of \( M \) are bounded below by a constant \( c \) , then the principal curvatures of the \( r \) -level sets in \( U \smallsetminus  \{ p\} \) (with respect to the inward unit normal) satisfy

\[
\kappa  \leq  \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }.
\]

Proof. This follows immediately from the fact that the shape operator of each \( r \) - level set is the restriction of \( {\mathcal{H}}_{r} \) by Lemma 11.1(c).

Because Jacobi fields describe the behavior of families of geodesics, the next theorem gives some substance to the intuitive notion that negative curvature tends to make nearby geodesics spread out, while positive curvature tends to make them converge. More precisely, an upper bound on curvature forces Jacobi fields to be at least as large as their constant-curvature counterparts, and a lower curvature bound constrains them to be no larger.

Theorem 11.9 (Jacobi Field Comparison). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic segment, and \( J \) is any normal Jacobi field along \( \gamma \) such that \( J\left( 0\right)  = 0 \) . For each \( c \in  \mathbb{R} \) , let \( {s}_{c} \) be the function defined by (10.8).

(a) If all sectional curvatures of \( M \) are bounded above by a constant \( c \) , then

\[
\left| {J\left( t\right) }\right|  \geq  {s}_{c}\left( t\right) \left| {{D}_{t}J\left( 0\right) }\right| \tag{11.21}
\]

for all \( t \in  \left\lbrack  {0,{b}_{1}}\right\rbrack \) , where \( {b}_{1} = b \) if \( c \leq  0 \) , and \( {b}_{1} = \min \left( {b,{\pi R}}\right) \) if \( c = 1/{R}^{2} > 0 \) . (b) If all sectional curvatures of \( M \) are bounded below by a constant \( c \) , then

\[
\left| {J\left( t\right) }\right|  \leq  {s}_{c}\left( t\right) \left| {{D}_{t}J\left( 0\right) }\right| \tag{11.22}
\]

for all \( t \in  \left\lbrack  {0,{b}_{2}}\right\rbrack \) , where \( {b}_{2} \) is chosen so that \( \gamma \left( {b}_{2}\right) \) is the first conjugate point to \( \gamma \left( 0\right) \) along \( \gamma \) if there is one, and otherwise \( {b}_{2} = b \) .

Proof. If \( {D}_{t}J\left( 0\right)  = 0 \) , then \( J \) vanishes identically, so we may as well assume that \( {D}_{t}J\left( 0\right)  \neq  0 \) . Let \( {b}_{0} \) be the largest time in \( (0, b\rbrack \) such that \( \gamma \) has no conjugate points in \( \left( {0,{b}_{0}}\right) \) and \( {s}_{c}\left( t\right)  > 0 \) for \( t \in  \left( {0,{b}_{0}}\right) \) . Let \( p = \gamma \left( 0\right) \) , and assume temporarily that \( \gamma \left( {\lbrack 0,{b}_{0})}\right) \) is contained in a normal neighborhood \( U \) of \( p \) . Define a function \( f : \left( {0,{b}_{0}}\right)  \rightarrow  \mathbb{R} \) by

\[
f\left( t\right)  = \log \left( {{s}_{c}{\left( t\right) }^{-1}\left| {J\left( t\right) }\right| }\right) .
\]

Differentiating with respect to \( t \) and using \( {D}_{t}J = {\mathcal{H}}_{r}\left( J\right) \) , we get

\[
{f}^{\prime } = \frac{d}{dt}\log \left| J\right|  - \frac{d}{dt}\log {s}_{c} = \frac{\left\langle  {D}_{t}J, J\right\rangle  }{{\left| J\right| }^{2}} - \frac{{s}_{c}^{\prime }}{{s}_{c}} = \frac{\left\langle  {\mathcal{H}}_{r}\left( J\right) , J\right\rangle  }{{\left| J\right| }^{2}} - \frac{{s}_{c}^{\prime }}{{s}_{c}}.
\]

Under hypothesis (a), it follows from the Hessian comparison theorem that \( {f}^{\prime }\left( t\right)  \geq \) 0 for all \( t \in  \left( {0,{b}_{0}}\right) \) , so \( f\left( t\right) \) is nondecreasing, and thus so is \( {s}_{c}{\left( t\right) }^{-1}\left| {J\left( t\right) }\right| \) . Similarly, under hypothesis (b), we get \( {f}^{\prime }\left( t\right)  \leq  0 \) , which implies that \( {s}_{c}{\left( t\right) }^{-1}\left| {J\left( t\right) }\right| \) is nonincreasing.

Next we consider the limit of \( {s}_{c}{\left( t\right) }^{-1}\left| {J\left( t\right) }\right| \) as \( t \searrow  0 \) . Two applications of l'Hôpital's rule yield

\[
\mathop{\lim }\limits_{{t \searrow  0}}\frac{{\left| J\right| }^{2}}{{s}_{c}^{2}} = \mathop{\lim }\limits_{{t \searrow  0}}\frac{2\left\langle  {{D}_{t}J, J}\right\rangle  }{2{s}_{c}^{\prime }{s}_{c}} = \mathop{\lim }\limits_{{t \searrow  0}}\frac{2\left\langle  {{D}_{t}^{2}J, J}\right\rangle   + 2{\left| {D}_{t}J\right| }^{2}}{2{s}_{c}^{\prime \prime }{s}_{c} + 2{s}_{c}^{\prime 2}}
\]

\[
= \mathop{\lim }\limits_{{t \searrow  0}}\frac{-2\left\langle  {R\left( {J,{\gamma }^{\prime }}\right) {\gamma }^{\prime }, J}\right\rangle   + 2{\left| {D}_{t}J\right| }^{2}}{2{s}_{c}^{\prime \prime }{s}_{c} + 2{s}_{c}^{\prime 2}},
\]

provided the last limit exists. Since \( J \rightarrow  0,{s}_{c} \rightarrow  0 \) , and \( {s}_{c}^{\prime } \rightarrow  1 \) as \( t \searrow  0 \) , this last limit does exist and is equal to \( {\left| {D}_{t}J\left( 0\right) \right| }^{2} \) . Combined with the derivative estimates above, this shows that the appropriate conclusion (11.21) or (11.22) holds on \( \left( {0,{b}_{0}}\right) \) , and thus by continuity on \( \left\lbrack  {0,{b}_{0}}\right\rbrack \) , when \( \gamma \left( \left\lbrack  {0,{b}_{0}}\right) \right) \) is contained in a normal neighborhood of \( p \) .

Now suppose \( \gamma \) is an arbitrary geodesic segment, not assumed to be contained in a normal neighborhood of \( p \) . Let \( v = {\gamma }^{\prime }\left( 0\right) \) , so that \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) for \( t \in  \left\lbrack  {0, b}\right\rbrack \) , and define \( {b}_{0} \) as above. The definition ensures that \( \gamma \left( t\right) \) is not conjugate to \( \gamma \left( 0\right) \) for \( t \in  \left( {0,{b}_{0}}\right) \) , and therefore \( {\exp }_{p} \) is a local diffeomorphism on some neighborhood of the set \( L = \left\{  {{tv} : 0 \leq  t < {b}_{0}}\right\} \) . Let \( W \subseteq  {T}_{p}M \) be a convex open set containing \( L \) on which \( {\exp }_{p} \) is a local diffeomorphism, and let \( \widetilde{g} = {\exp }_{p}^{ * }g \) , which is a Riemannian metric on \( W \) that satisfies the same curvature estimates as \( g \) (Fig. 11.2). By construction, \( W \) is a normal neighborhood of 0, and \( {\exp }_{p} \) is a local isometry from \( \left( {W,\widetilde{g}}\right) \) to \( \left( {M, g}\right) \) . The curve \( \widetilde{\gamma }\left( t\right)  = {tv} \) for \( t \in  \left\lbrack  {0,{b}_{0}}\right) \) is a radial geodesic in \( W \) , and Proposition 10.5 shows that the vector field \( \widetilde{J}\left( t\right)  = d{\left( {\exp }_{p}\right) }_{tv}^{-1}\left( {J\left( t\right) }\right) \) is a Jacobi field along \( \widetilde{\gamma } \) that vanishes at \( t = 0 \) . Therefore, for \( t \in  \left( {0,{b}_{0}}\right) \) , the preceding argument implies that \( {\left| \widetilde{J}\left( t\right) \right| }_{\widetilde{g}} \geq  {s}_{c}\left( t\right) {\left| {\widetilde{D}}_{t}\widetilde{J}\left( 0\right) \right| }_{\widetilde{g}} \) in case (a) and \( {\left| \widetilde{J}\left( t\right) \right| }_{\widetilde{g}} \leq  {s}_{c}\left( t\right) {\left| {\widetilde{D}}_{t}\widetilde{J}\left( 0\right) \right| }_{\widetilde{g}} \) in case (b). This implies that the conclusions of the theorem hold for \( J \) on the interval \( \left( {0,{b}_{0}}\right) \) and thus by continuity on \( \left\lbrack  {0,{b}_{0}}\right\rbrack \) .

To complete the proof, we need to show that \( {b}_{0} \geq  {b}_{1} \) in case (a) and \( {b}_{0} \geq  {b}_{2} \) in case (b). Assuming the hypothesis of (a), suppose for contradiction that \( {b}_{0} < {b}_{1} \) . The only way this can occur is if \( \gamma \left( {b}_{0}\right) \) is conjugate to \( \gamma \left( 0\right) \) along \( \gamma \) , while \( {s}_{c}\left( {b}_{0}\right)  > 0 \) . This means that there is a nontrivial normal Jacobi field \( J \in  \mathcal{J}\left( \gamma \right) \) satisfying \( J\left( 0\right)  = \; 0 = J\left( {b}_{0}\right) \) . But the argument above showed that every such Jacobi field satisfies \( \left| {J\left( t\right) }\right|  \geq  {s}_{c}\left( t\right) \left| {{D}_{t}J\left( 0\right) }\right| \) for \( t \in  \left\lbrack  {0,{b}_{0}}\right\rbrack \) and thus \( \left| {J\left( {b}_{0}\right) }\right|  \geq  {s}_{c}\left( {b}_{0}\right) \left| {{D}_{t}J\left( 0\right) }\right|  > 0 \) , which is a contradiction. Similarly, in case (b), suppose \( {b}_{0} < {b}_{2} \) . Then \( {s}_{c}\left( {b}_{0}\right)  = 0 \) , but \( \gamma \left( {b}_{0}\right) \) is not conjugate to \( \gamma \left( 0\right) \) along \( \gamma \) . If \( J \) is any nontrivial normal Jacobi field along \( \gamma \) that vanishes at \( t = 0 \) , the argument above shows that \( \left| {J\left( t\right) }\right|  \leq  {s}_{c}\left( t\right) \left| {{D}_{t}J\left( 0\right) }\right| \) for \( t \in  \left\lbrack  {0,{b}_{0}}\right\rbrack \) , so \( \left| {J\left( {b}_{0}\right) }\right|  \leq  {s}_{c}\left( {b}_{0}\right) \left| {{D}_{t}J\left( 0\right) }\right|  = 0 \) ; but this is impossible because \( \gamma \left( {b}_{0}\right) \) is not conjugate to \( \gamma \left( 0\right) \) .

![bo_d7dtff491nqc73eq8m7g_340_259_185_1012_665_0.jpg](images/bo_d7dtff491nqc73eq8m7g_340_259_185_1012_665_0.jpg)

Fig. 11.2: Pulling the metric back to \( {T}_{p}M \)

There is a generalization of the preceding theorem, called the Rauch comparison theorem, that allows for comparison of Jacobi fields in two different Riemannian manifolds when neither is assumed to have constant curvature. The statement and proof can be found in [CE08, Kli95].

Because all tangent vectors in a normal neighborhood are values of Jacobi fields along radial geodesics, the Jacobi field comparison theorem leads directly to the following comparison theorem for metrics.

Theorem 11.10 (Metric Comparison). Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( \left( {U,\left( {x}^{i}\right) }\right) \) be any normal coordinate chart for \( g \) centered at \( p \in  M \) . For each \( c \in  \mathbb{R} \) , let \( {g}_{c} \) denote the constant-curvature metric on \( U \smallsetminus  \{ p\} \) given in the same coordinates by formula (10.17).

(a) Suppose all sectional curvatures of \( g \) are bounded above by a constant \( c \) . If \( c \leq  0 \) , then for all \( q \in  U \smallsetminus  \{ p\} \) and all \( w \in  {T}_{q}M \) , we have \( g\left( {w, w}\right)  \geq  {g}_{c}\left( {w, w}\right) \) . If \( c = 1/{R}^{2} > 0 \) , then the same holds, provided that \( {d}_{g}\left( {p, q}\right)  < {\pi R} \) .

(b) If all sectional curvatures of \( g \) are bounded below by a constant \( c \) , then for all \( q \in  U \smallsetminus  \{ p\} \) and all \( w \in  {T}_{q}M \) , we have \( g\left( {w, w}\right)  \leq  {g}_{c}\left( {w, w}\right) \) .

Proof. Let \( q \in  U \smallsetminus  \{ p\} \) , satisfying the restriction \( {d}_{g}\left( {p, q}\right)  < {\pi R} \) if we are in case (a) and \( c = 1/{R}^{2} > 0 \) , but otherwise arbitrary; and let \( b = {d}_{g}\left( {p, q}\right) \) . Given \( w \in  {T}_{q}M \) , we can decompose \( w \) as a sum \( w = y + z \) , where \( y \) is a multiple of the radial vector field \( {\partial }_{r} \) and \( z \) is tangent to the level set \( r = b \) . Then \( {g}_{c}\left( {y, z}\right)  = 0 \) by direct computation, and the Gauss lemma shows that \( g\left( {y, z}\right)  = 0 \) , so

\[
g\left( {w, w}\right)  = g\left( {y, y}\right)  + g\left( {z, z}\right) ,
\]

\[
{g}_{c}\left( {w, w}\right)  = {g}_{c}\left( {y, y}\right)  + {g}_{c}\left( {z, z}\right) .
\]

Because \( {\partial }_{r} \) is a unit vector with respect to both \( g \) and \( {g}_{c} \) , it follows that \( g\left( {y, y}\right)  = \; {g}_{c}\left( {y, y}\right) \) . So it suffices to prove the comparison for \( z \) .

There is a radial geodesic \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) satisfying \( \gamma \left( 0\right)  = p \) and \( \gamma \left( b\right)  = q \) , and Corollary 10.11 shows that \( z = J\left( b\right) \) for some Jacobi field \( J \) along \( \gamma \) vanishing at \( t = 0 \) , which is normal because it is orthogonal to \( {\gamma }^{\prime } \) at \( t = 0 \) and \( t = b \) . Proposition 10.10 shows that \( J \) has the coordinate formula \( J\left( t\right)  = {\left. t{a}^{i}{\partial }_{i}\right| }_{\gamma \left( t\right) } \) for some constants \( \left( {{a}^{1},\ldots ,{a}^{n}}\right) \) . Since the coordinates \( \left( {x}^{i}\right) \) are normal coordinates for both \( g \) and \( {g}_{c} \) , it follows that \( \gamma \) is also a radial geodesic for \( {g}_{c} \) , and the same vector field \( J \) is also a normal Jacobi field for \( {g}_{c} \) along \( \gamma \) . Therefore, \( g\left( {z, z}\right)  = {\left| J\left( b\right) \right| }_{g}^{2} \) and \( {g}_{c}\left( {z, z}\right)  = \; {\left| J\left( b\right) \right| }_{{g}_{c}}^{2} \) . In case (a), our hypothesis guarantees that \( {s}_{c}\left( b\right)  > 0 \) , so

\[
g\left( {z, z}\right)  = {\left| J\left( b\right) \right| }_{g}^{2} \geq  {\left| {s}_{c}\left( b\right) \right| }^{2}{\left| {D}_{t}J\left( 0\right) \right| }_{g}^{2}\;\text{ (Jacobi field comparison theorem) }
\]

\[
= {\left| {s}_{c}\left( b\right) \right| }^{2}{\left| {D}_{t}J\left( 0\right) \right| }_{{g}_{c}}^{2}\;\text{ (since }g\text{ and }{g}_{c}\text{ agree at }p\text{ ) }
\]

\[
= {\left| J\left( b\right) \right| }_{{g}_{c}}^{2} = {g}_{c}\left( {z, z}\right) \;\text{ (by Prop. 10.12). }
\]

In case (b), the same argument with the inequalities reversed shows that \( g\left( {z, z}\right)  \leq \; {g}_{c}\left( {z, z}\right) \) .

The next three comparison theorems (Laplacian, conjugate point, and volume comparisons) can be proved equally easily under the assumption of either an upper bound or a lower bound for the sectional curvature, just like the preceding theorems. However, we state these only for the case of an upper bound, because we will prove stronger theorems later in the chapter based on lower bounds for the Ricci curvature (see Thms. 11.15, 11.16, and 11.19).

The first of the three is a comparison of the Laplacian of the radial distance function with its constant-curvature counterpart. Our primary interest in the Laplacian of the distance function stems from its role in volume and conjugate point comparisons (see Thms. 11.14, 11.16, and 11.19 below); but it also plays an important role in the study of various partial differential equations on Riemannian manifolds.

Theorem 11.11 (Laplacian Comparison I). Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) - manifold whose sectional curvatures are all bounded above by a constant c. Suppose \( p \in  M, U \) is a normal neighborhood of \( p, r \) is the radial distance function on \( U \) , and \( {s}_{c} \) is defined as in Proposition 11.3. Then on \( {U}_{0} \smallsetminus  \{ p\} \) , we have

\[
{\Delta r} \geq  \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) },
\]

where \( {U}_{0} = U \) if \( c \leq  0 \) , while \( {U}_{0} = \{ q \in  U : r\left( q\right)  < {\pi R}\} \) if \( c = 1/{R}^{2} > 0 \) .

Proof. By the result of Problem 5-14, \( {\Delta r} = {\operatorname{tr}}_{g}\left( {{\nabla }^{2}r}\right)  = \operatorname{tr}\left( {\mathcal{H}}_{r}\right) \) . The result then follows from the Hessian comparison theorem, using the fact that \( \operatorname{tr}\left( {\pi }_{r}\right)  = n - 1 \) , which can be verified easily by expressing \( {\pi }_{r} \) locally in an adapted orthonormal frame for the \( r \) -level sets.

The next theorem shows how an upper curvature bound prevents the formation of conjugate points. It will play a decisive role in the proof of the Cartan-Hadamard theorem in the next chapter.

Theorem 11.12 (Conjugate Point Comparison I). Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold whose sectional curvatures are all bounded above by a constant \( c \) . If \( c \leq  0 \) , then no point of \( M \) has conjugate points along any geodesic. If \( c = 1/{R}^{2} > 0 \) , then there is no conjugate point along any geodesic segment shorter than \( {\pi R} \) .

Proof. The case \( c \leq  0 \) is covered by Problem 10-7, so assume \( c = 1/{R}^{2} > 0 \) . Let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) be a unit-speed geodesic segment, and suppose \( J \) is a nontrivial normal Jacobi field along \( \gamma \) that vanishes at \( t = 0 \) . The Jacobi field comparison theorem implies that \( \left| {J\left( t\right) }\right|  \geq  \left( \text{ constant }\right) \sin \left( {t/R}\right)  > 0 \) as long as \( 0 < t < {\pi R} \) .

The last of our sectional curvature comparison theorems is a comparison of volume growth of geodesic balls. Before proving it, we need the following lemma, which shows how the Riemannian volume form is related to the Laplacian of the radial distance function.

Lemma 11.13. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( \left( {x}^{i}\right) \) are Riemannian normal coordinates on a normal neighborhood \( U \) of \( p \in  M \) . Let \( \det g \) denote the determinant of the matrix \( \left( {g}_{ij}\right) \) in these coordinates, let \( r \) be the radial distance function, and let \( {\partial }_{r} \) be the unit radial vector field. The following identity holds on \( U \smallsetminus  \{ p\} \) :

\[
{\Delta r} = {\partial }_{r}\log \left( {{r}^{n - 1}\sqrt{\det g}}\right) . \tag{11.23}
\]

Proof. Corollary 6.10 to the Gauss lemma shows that the vector fields grad \( r \) and \( {\partial }_{r} \) are equal on \( U \smallsetminus  \{ p\} \) . Comparing the components of these two vector fields in normal coordinates, we conclude (using the summation convention as usual) that

\[
{g}^{ij}{\partial }_{j}r = \frac{{x}^{i}}{r}.
\]

Based on the formula for \( {\Delta r} \) from Proposition 2.46, we compute

\[
{\Delta r} = \frac{1}{\sqrt{\det g}}{\partial }_{i}\left( {{g}^{ij}\sqrt{\det g}{\partial }_{j}r}\right)
\]

\[
= \frac{1}{\sqrt{\det g}}{\partial }_{i}\left( {\frac{{x}^{i}}{r}\sqrt{\det g}}\right)
\]

\[
= {\partial }_{i}\left( \frac{{x}^{i}}{r}\right)  + \frac{1}{\sqrt{\det g}}\frac{{x}^{i}}{r}{\partial }_{i}\sqrt{\det g}
\]

\[
= \frac{n - 1}{r} + \frac{1}{\sqrt{\det g}}{\partial }_{r}\sqrt{\det g}
\]

where the first term in the last line follows by direct computation using \( r = \; {\left( \mathop{\sum }\limits_{i}{\left( {x}^{i}\right) }^{2}\right) }^{1/2} \) . This is equivalent to (11.23).

The following result was proved by Paul Günther in 1960 [Gün60]. (Günther also proved an analogous result in the case of a lower sectional curvature bound, but that result has been superseded by the Bishop-Gromov theorem, Thm. 11.19 below.)

Theorem 11.14 (Günther’s Volume Comparison). Suppose \( \left( {M, g}\right) \) is a connected Riemannian n-manifold whose sectional curvatures are all bounded above by a constant \( c \) . Given \( p \in  M \) , let \( {\delta }_{0} = \operatorname{inj}\left( p\right) \) if \( c \leq  0 \) , and \( {\delta }_{0} = \min \left( {{\pi R},\operatorname{inj}\left( p\right) }\right) \) if \( c = 1/{R}^{2} > 0 \) . For every positive number \( \delta  \leq  {\delta }_{0} \) , let \( {V}_{g}\left( \delta \right) \) denote the volume of the geodesic ball \( {B}_{\delta }\left( p\right) \) in \( \left( {M, g}\right) \) , and let \( {V}_{c}\left( \delta \right) \) denote the volume of a geodesic ball of radius \( \delta \) in the \( n \) -dimensional Euclidean space, hyperbolic space, or sphere with constant sectional curvature \( c \) . Then for every \( 0 < \delta  \leq  {\delta }_{0} \) , we have

\[
{V}_{g}\left( \delta \right)  \geq  {V}_{c}\left( \delta \right) \tag{11.24}
\]

and the quotient \( {V}_{g}\left( \delta \right) /{V}_{c}\left( \delta \right) \) is a nondecreasing function of \( \delta \) that approaches 1 as \( \delta  \searrow  0 \) . If equality holds in (11.24) for some \( \delta  \in  \left( {0,{\delta }_{0}}\right\rbrack \) , then \( g \) has constant sectional curvature \( c \) on the entire geodesic ball \( {B}_{\delta }\left( p\right) \) .

Proof. The volume estimate (11.24) follows easily from the metric comparison theorem, which implies that the determinants of the metrics \( g \) and \( {g}_{c} \) in normal coordinates satisfy \( \sqrt{\det g} \geq  \sqrt{\det {g}_{c}} \) . If that were all we needed, we could stop here; but to prove the other statements, we need a more involved argument, which incidentally provides another proof of (11.24) that does not rely directly on the metric comparison theorem, and therefore can be adapted more easily to the case in which we have only an estimate of the Ricci curvature (see Thm. 11.19 below).

Let \( \left( {x}^{i}\right) \) be normal coordinates on \( {B}_{{\delta }_{0}}\left( p\right) \) (interpreted as all of \( M \) if \( {\delta }_{0} = \infty \) ). Using these coordinates, we might as well consider \( g \) to be a Riemannian metric on an open subset of \( {\mathbb{R}}^{n} \) and \( p \) to be the origin. Let \( \bar{g} \) denote the Euclidean metric in these coordinates, and let \( {g}_{c} \) denote the constant-curvature metric in the same coordinates, given on the complement of the origin by (10.17).

The Laplacian comparison theorem together with Lemma 11.13 shows that

\[
{\partial }_{r}\log \left( {{r}^{n - 1}\sqrt{\det g}}\right)  = {\Delta r} \geq  \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) } = {\partial }_{r}\log \left( {{s}_{c}{\left( r\right) }^{n - 1}}\right) . \tag{11.25}
\]

Thus \( \log \left( {{r}^{n - 1}\sqrt{\det g}/{s}_{c}{\left( r\right) }^{n - 1}}\right) \) is a nondecreasing function of \( r \) along each radial geodesic, and so is the ratio \( {r}^{n - 1}\sqrt{\det g}/{s}_{c}{\left( r\right) }^{n - 1} \) . To compute the limit as \( r \searrow  0 \) , note that \( {g}_{ij} = {\delta }_{ij} \) at the origin, so \( \sqrt{\det g} \) converges uniformly to 1 as \( r \searrow  0 \) . Also, for every \( c \) , we have \( {s}_{c}\left( r\right) /r \rightarrow  1 \) as \( r \searrow  0 \) , so \( {r}^{n - 1}\sqrt{\det g}/{s}_{c}{\left( r\right) }^{n - 1} \rightarrow  1 \) .

We can write \( d{V}_{g} = \sqrt{\det g}d{V}_{\bar{g}} \) . Corollary 10.17 in the case \( c = 0 \) shows that

\[
{V}_{g}\left( \delta \right)  = {\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{\delta }\left( \sqrt{\det g}\right)  \circ  \Phi \left( {\rho ,\omega }\right) {\rho }^{n - 1}{d\rho d}{V}_{g}^{ \circ  },
\]

where \( \Phi \left( {\rho ,\omega }\right)  = {\rho \omega } \) for \( \rho  \in  \left( {0,{\delta }_{0}}\right) \) and \( \omega  \in  {\mathbb{S}}^{n - 1} \) . The same corollary shows that

\[
{V}_{c}\left( \delta \right)  = {\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{\delta }{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho d}{V}_{\overset{ \circ  }{g}} = \left( {{\int }_{0}^{\delta }{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}\right) \left( {{\int }_{{\mathbb{S}}^{n - 1}}d{V}_{\overset{ \circ  }{g}}}\right) .
\]

Therefore,

\[
\frac{{V}_{g}\left( \delta \right) }{{V}_{c}\left( \delta \right) } = \frac{{\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{\delta }\left( \sqrt{\det g}\right)  \circ  \Phi \left( {\rho ,\omega }\right) {\rho }^{n - 1}{d\rho d}{V}_{g}}{\left( {{\int }_{0}^{\delta }{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}\right) \left( {{\int }_{{\mathbb{S}}^{n - 1}}d{V}_{g}}\right) }
\]

\[
= \frac{1}{\operatorname{Vol}\left( {\mathbb{S}}^{n - 1}\right) }{\int }_{{\mathbb{S}}^{n - 1}}\left( \frac{{\int }_{0}^{\delta }\lambda \left( {\rho ,\omega }\right) {s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}{{\int }_{0}^{\delta }{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}\right) d{V}_{g}, \tag{11.26}
\]

where we have written

\[
\lambda \left( {\rho ,\omega }\right)  = \frac{\left( \sqrt{\det g}\right)  \circ  \Phi \left( {\rho ,\omega }\right) {\rho }^{n - 1}}{{s}_{c}{\left( \rho \right) }^{n - 1}}.
\]

The argument above (together with the fact that \( r \circ  \Phi  = \rho \) ) shows that \( \lambda \left( {\rho ,\omega }\right) \) is a nondecreasing function of \( \rho \) for each \( \omega \) , which approaches 1 uniformly as \( \rho  \searrow  0 \) .

We need to show that the quotient in parentheses in the last line of (11.26) is also nondecreasing as \( \delta \) increases. Suppose \( 0 < {\delta }_{1} < {\delta }_{2} \) . Because \( \lambda \) is nondecreasing, we have

\[
{\int }_{0}^{{\delta }_{1}}\lambda \left( {\rho ,\omega }\right) {s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }{\int }_{{\delta }_{1}}^{{\delta }_{2}}{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }
\]

\[
\leq  \left( {{\int }_{0}^{{\delta }_{1}}{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}\right) \lambda \left( {{\delta }_{1},\omega }\right) \left( {{\int }_{{\delta }_{1}}^{{\delta }_{2}}{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }}\right)
\]

\[
\leq  {\int }_{0}^{{\delta }_{1}}{s}_{c}{\left( \rho \right) }^{n - 1}{d\rho }{\int }_{{\delta }_{1}}^{{\delta }_{2}}\lambda \left( {\rho ,\omega }\right) {s}_{c}{\left( \rho \right) }^{n - 1}{d\rho },
\]

and therefore (suppressing the dependence of the integrands on \( \rho \) and \( \omega \) for brevity),

\[
{\int }_{0}^{{\delta }_{1}}\lambda {s}_{c}^{n - 1}{d\rho }{\int }_{0}^{{\delta }_{2}}{s}_{c}^{n - 1}{d\rho }
\]

\[
= {\int }_{0}^{{\delta }_{1}}\lambda {s}_{c}^{n - 1}{d\rho }\left( {{\int }_{0}^{{\delta }_{1}}{s}_{c}^{n - 1}{d\rho } + {\int }_{{\delta }_{1}}^{{\delta }_{2}}{s}_{c}^{n - 1}{d\rho }}\right)
\]

\[
\leq  {\int }_{0}^{{\delta }_{1}}\lambda {s}_{c}^{n - 1}{d\rho }{\int }_{0}^{{\delta }_{1}}{s}_{c}^{n - 1}{d\rho } + {\int }_{0}^{{\delta }_{1}}{s}_{c}^{n - 1}{d\rho }{\int }_{{\delta }_{1}}^{{\delta }_{2}}\lambda {s}_{c}^{n - 1}{d\rho }
\]

\[
= {\int }_{0}^{{\delta }_{1}}{s}_{c}^{n - 1}{d\rho }{\int }_{0}^{{\delta }_{2}}\lambda {s}_{c}^{n - 1}{d\rho }.
\]

Evaluating (11.26) at \( {\delta }_{1} \) and \( {\delta }_{2} \) and inserting the inequality above shows that the ratio \( {\operatorname{Vol}}_{g}\left( \delta \right) /{\operatorname{Vol}}_{c}\left( \delta \right) \) is nondecreasing as a function of \( \delta \) , and it approaches 1 as \( \delta  \searrow  0 \) because \( \lambda \left( {\rho ,\omega }\right)  \rightarrow  1 \) as \( \rho  \searrow  0 \) . It follows that \( {V}_{g}\left( \delta \right)  \geq  {V}_{c}\left( \delta \right) \) for all \( \delta  \in  \left( {0,{\delta }_{0}}\right\rbrack \) .

It remains only to consider the case in which the volume ratio is equal to 1 for some \( \delta \) . If \( \lambda \left( {\rho ,\omega }\right) \) is not identically 1 on the set where \( 0 < \rho  < \delta \) , then it is strictly greater than 1 on a nonempty open subset, which implies that the volume ratio in (11.26) is strictly greater than 1; so \( {\operatorname{Vol}}_{g}\left( \delta \right)  = {\operatorname{Vol}}_{c}\left( \delta \right) \) implies \( \lambda \left( {\rho ,\omega }\right)  \equiv  1 \) on \( \left( {0,\delta }\right)  \times  {\mathbb{S}}^{n - 1} \) , and pulling back to \( U \) via \( {\Phi }^{-1} \) shows that \( {r}^{n - 1}\sqrt{\det g} \equiv  {s}_{c}{\left( r\right) }^{n - 1} \) on \( {B}_{\delta }\left( p\right) \) . By virtue of (11.25), we have \( {\Delta r} \equiv  \left( {n - 1}\right) {s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right) \) , or in other words, \( \operatorname{tr}\left( {\mathcal{H}}_{r}\right)  = \operatorname{tr}\left( {\left( {{s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right) }\right) {\pi }_{r}}\right) \) . It follows from the Hessian comparison theorem that the endomorphism field \( {\mathcal{H}}_{r} - \left( {{s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right) }\right) {\pi }_{r} \) is positive semidefinite, so its eigenvalues are all nonnegative. Since its trace is zero, the eigenvalues must all be zero. In other words, \( {\mathcal{H}}_{r} \equiv  \left( {{s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right) }\right) {\pi }_{r} \) on the geodesic ball \( {B}_{\delta }\left( p\right) \) . It then follows from Proposition 11.3 that \( g \) has constant sectional curvature \( c \) on that ball.

## Comparisons Based on Ricci Curvature

All of our comparison theorems so far have been based on assuming an upper or lower bound for the sectional curvature. It is natural to wonder whether anything can be said if we weaken the hypotheses and assume only bounds on other curvature quantities such as Ricci or scalar curvature.

It should be noted that except in very low dimensions, assuming a bound on Ricci or scalar curvature is a strictly weaker hypothesis than assuming one on sectional curvature. Recall Proposition 8.32, which says that on an \( n \) -dimensional Riemannian manifold, the Ricci curvature evaluated on a unit vector is a sum of \( n - 1 \) sectional curvatures, and the scalar curvature is a sum of \( n\left( {n - 1}\right) \) sectional curvatures. Thus if \( \left( {M, g}\right) \) has sectional curvatures bounded below by \( c \) , then its Ricci curvature satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) , and its scalar curvature satisfies \( S \geq  n\left( {n - 1}\right) c \) , with analogous inequalities if the sectional curvature is bounded above. However, the converse is not true: an upper or lower bound on the Ricci curvature implies nothing about individual sectional curvatures, except in dimensions 2 and 3, where the entire curvature tensor is determined by the Ricci curvature (see Cors. 7.26 and 7.27). For example, in every even dimension greater than or equal to 4, there are compact Riemannian manifolds called Calabi-Yau manifolds that have zero Ricci curvature but nonzero sectional curvatures (see, for example, [Bes87, Chap. 11]).

In this section we investigate the extent to which bounds on the Ricci curvature lead to useful comparison theorems. The strongest theorems of the preceding section, such as the Hessian, Jacobi field, and metric comparison theorems, do not generalize to the case in which we merely have bounds on Ricci curvature. However, it is a remarkable fact that Laplacian, conjugate point, and volume comparison theorems can still be proved assuming only a lower (but not upper) bound on the Ricci curvature. (The problem of drawing global conclusions from scalar curvature bounds is far more subtle, and we do not pursue it here. A good starting point for learning about that problem is [Bes87].)

The next theorem is the analogue of Theorem 11.11.

Theorem 11.15 (Laplacian Comparison II). Let \( \left( {M, g}\right) \) be a Riemannian \( n \) -manifold, and suppose there is a constant \( c \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) . Given any point \( p \in  M \) , let \( U \) be a normal neighborhood of \( p \) and let \( r \) be the radial distance function on \( U \) . Then the following inequality holds on \( {U}_{0} \smallsetminus  \{ p\} \) :

\[
{\Delta r} \leq  \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }, \tag{11.27}
\]

where \( {s}_{c} \) is defined by (10.8), and \( {U}_{0} = U \) if \( c \leq  0 \) , while \( {U}_{0} = \{ q \in  U : r\left( q\right)  < {\pi R}\} \) if \( c = 1/{R}^{2} > 0 \) .

Proof. Let \( q \in  {U}_{0} \smallsetminus  \{ p\} \) be arbitrary, and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  {U}_{0} \) be the unit-speed radial geodesic from \( p \) to \( q \) . We will show that (11.27) holds at \( \gamma \left( t\right) \) for \( 0 < t \leq  b \) .

Because covariant differentiation commutes with the trace operator (since it is just a particular kind of contraction), the Riccati equation (11.7) for \( {\mathcal{H}}_{r} \) implies the following scalar equation along \( \gamma \) for \( {\Delta r} = \operatorname{tr}\left( {\mathcal{H}}_{r}\right) \) :

\[
\frac{d}{dt}{\Delta r} + \operatorname{tr}\left( {\mathcal{H}}_{r}^{2}\right)  + \operatorname{tr}{R}_{{\gamma }^{\prime }} = 0. \tag{11.28}
\]

We need to analyze the last two terms on the left-hand side. We begin with the last term. In terms of any local orthonormal frame \( \left( {E}_{i}\right) \) , we have

\[
\operatorname{tr}{R}_{{\gamma }^{\prime }} = \mathop{\sum }\limits_{{i = 1}}^{n}\left\langle  {{R}_{{\gamma }^{\prime }}\left( {E}_{i}\right) ,{E}_{i}}\right\rangle   = \mathop{\sum }\limits_{{i = 1}}^{n}\left\langle  {R\left( {{E}_{i},{\gamma }^{\prime }}\right) {\gamma }^{\prime },{E}_{i}}\right\rangle   = \mathop{\sum }\limits_{{i = 1}}^{n}\operatorname{Rm}\left( {{E}_{i},{\gamma }^{\prime },{\gamma }^{\prime },{E}_{i}}\right)
\]

\[
= \operatorname{Rc}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) \text{ . }
\]

To analyze the \( {\mathcal{H}}_{r}^{2} \) term, let us set

\[
{\overset{ \circ  }{\mathcal{H}}}_{r} = {\mathcal{H}}_{r} - \frac{\Delta r}{n - 1}{\pi }_{r} \tag{11.29}
\]

We compute

\[
\operatorname{tr}\left( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2}\right)  = \operatorname{tr}\left( {\mathcal{H}}_{r}^{2}\right)  - \frac{\Delta r}{n - 1}\operatorname{tr}\left( {{\mathcal{H}}_{r} \circ  {\pi }_{r}}\right)  - \frac{\Delta r}{n - 1}\operatorname{tr}\left( {{\pi }_{r} \circ  {\mathcal{H}}_{r}}\right)  + \frac{{\left( \Delta r\right) }^{2}}{{\left( n - 1\right) }^{2}}\operatorname{tr}\left( {\pi }_{r}^{2}\right) .
\]

To simplify this, note that \( {\pi }_{r}^{2} = {\pi }_{r} \) because \( {\pi }_{r} \) is a projection, and thus \( \operatorname{tr}\left( {\pi }_{r}^{2}\right)  = \; \operatorname{tr}\left( {\pi }_{r}\right)  = n - 1 \) . Also, \( {\mathcal{H}}_{r}\left( {\partial }_{r}\right)  \equiv  0 \) implies that \( {\mathcal{H}}_{r} \circ  {\pi }_{r} = {\mathcal{H}}_{r} \) ; and since \( {\mathcal{H}}_{r} \) is selfadjoint, \( {\left\langle  {\mathcal{H}}_{r}v,{\partial }_{r}\right\rangle  }_{g} = {\left\langle  v,{\mathcal{H}}_{r}{\partial }_{r}\right\rangle  }_{g} = 0 \) for all \( v \) , so the image of \( {\mathcal{H}}_{r} \) is contained in the orthogonal complement of \( {\partial }_{r} \) , and it follows that \( {\pi }_{r} \circ  {\mathcal{H}}_{r} = {\mathcal{H}}_{r} \) as well. Thus the last three terms in the formula for \( \operatorname{tr}\left( {\mathcal{H}}_{r}^{2}\right) \) combine to yield

\[
\operatorname{tr}\left( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2}\right)  = \operatorname{tr}\left( {\mathcal{H}}_{r}^{2}\right)  - \frac{{\left( \Delta r\right) }^{2}}{n - 1}.
\]

Solving this for \( \operatorname{tr}\left( {\mathcal{H}}_{r}^{2}\right) \) , substituting into (11.28), and dividing by \( n - 1 \) , we obtain

\[
\frac{d}{dt}\left( \frac{\Delta r}{n - 1}\right)  + {\left( \frac{\Delta r}{n - 1}\right) }^{2} + \frac{\operatorname{tr}\left( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2}\right)  + {Rc}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) }{n - 1} = 0. \tag{11.30}
\]

Let \( H\left( t\right)  = {s}_{c}^{\prime }\left( t\right) /{s}_{c}\left( t\right) \) , so that

\[
{H}^{\prime }\left( t\right)  + H{\left( t\right) }^{2} + c \equiv  0.
\]

We wish to apply the \( 1 \times  1 \) case of the matrix Riccati comparison theorem (Thm. 11.6) with \( H\left( t\right) \) as above, \( S\left( t\right)  \equiv  c \) ,

\[
\widetilde{H}\left( t\right)  = \frac{{\left. \left( \Delta r\right) \right| }_{\gamma \left( t\right) }}{n - 1},\;\text{ and }\;\widetilde{S}\left( t\right)  = \frac{{\left. \operatorname{tr}\left( {\mathring{\mathcal{H}}}_{r}^{2}\right) \right| }_{\gamma \left( t\right) } + \operatorname{Rc}\left( {{\gamma }^{\prime }\left( t\right) ,{\gamma }^{\prime }\left( t\right) }\right) }{n - 1}.
\]

Note that \( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2} \) is positive semidefinite, which means that all of its eigenvalues are nonnegative, so its trace (which is the sum of the eigenvalues) is also nonnegative. (This is the step that does not work in the case of an upper bound on Ricci curvature.) Thus our hypothesis on the Ricci curvature guarantees that \( \widetilde{S}\left( t\right)  \geq  c \) for all \( t \in  (0, b\rbrack \) .

To apply Theorem 11.6, we need to verify that \( \widetilde{S} \) has a continuous extension to \( \left\lbrack  {0, b}\right\rbrack \) and that \( \widetilde{H}\left( t\right)  - H\left( t\right) \) has a nonnegative limit as \( t \searrow  0 \) . Recall that we showed in (11.19) and (11.20) that \( {s}_{c}^{\prime }\left( r\right) /{s}_{c}\left( r\right)  = 1/r + O\left( r\right) \) and \( {\mathcal{H}}_{r} = \; \left( {1/r}\right) {\pi }_{r} + O\left( r\right) \) as \( r \searrow  0 \) . This implies that \( {\Delta r} = \operatorname{tr}\left( {\mathcal{H}}_{r}\right)  = \left( {n - 1}\right) /r + O\left( r\right) \) , and therefore both \( {\left. {\breve{\mathcal{H}}}_{r}\right| }_{\gamma \left( t\right) } \) and \( \widetilde{H}\left( t\right)  - H\left( t\right) \) approach 0 and \( \widetilde{S}\left( t\right) \) approaches \( {Rc}\left( {{\gamma }^{\prime }\left( 0\right) ,{\gamma }^{\prime }\left( 0\right) }\right) /\left( {n - 1}\right)  \geq  c \) as \( t \searrow  0 \) . Therefore, we can apply Theorem 11.6 to conclude that \( \widetilde{H}\left( t\right)  \leq  H\left( t\right) \) for \( t \in  (0, b\rbrack \) . Since \( \gamma \left( b\right)  = q \) was arbitrary, this completes the proof.

The next theorem and its two corollaries will be crucial ingredients in the proofs of our theorems in the next chapter about manifolds with positive Ricci curvature (see Thms. 12.28 and 12.24).

Theorem 11.16 (Conjugate Point Comparison II). Let \( \left( {M, g}\right) \) be a Riemannian \( n \) - manifold, and suppose there is a positive constant \( c = 1/{R}^{2} \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) . Then every geodesic segment of length at least \( {\pi R} \) has a conjugate point.

Proof. Let \( U \) be a normal neighborhood of an arbitrary point \( p \in  M \) . The second Laplacian comparison theorem (Thm. 11.15) combined with Lemma 11.13 shows that

\[
{\partial }_{r}\log \left( {{r}^{n - 1}\sqrt{\det g}}\right)  = {\Delta r} \leq  \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) } = {\partial }_{r}\log \left( {{s}_{c}{\left( r\right) }^{n - 1}}\right)
\]

on the subset \( {U}_{0} \subseteq  U \) where \( r < {\pi R} \) . Since \( {r}^{n - 1}\sqrt{\det g}/{s}_{c}{\left( r\right) }^{n - 1} \rightarrow  1 \) as \( r \searrow  0 \) , this implies that \( {r}^{n - 1}\sqrt{\det g}/{s}_{c}{\left( r\right) }^{n - 1} \leq  1 \) everywhere in \( {U}_{0} \) , or equivalently,

\[
\sqrt{\det g} \leq  {s}_{c}{\left( r\right) }^{n - 1}/{r}^{n - 1}. \tag{11.31}
\]

Suppose \( U \) contains a point \( q \) where \( r \geq  {\pi R} \) , and let \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) be the unit-speed radial geodesic from \( p \) to \( q \) . Because \( {s}_{c}\left( {\pi R}\right)  = 0,\left( {11.31}\right) \) shows that \( \det g\left( {\gamma \left( t\right) }\right)  \rightarrow \) 0 as \( t \nearrow  {\pi R} \) , and therefore by continuity \( \det g = 0 \) at \( \gamma \left( b\right) \) , which contradicts the fact that \( \det g > 0 \) in every coordinate neighborhood. The upshot is that no normal neighborhood can include points where \( r \geq  {\pi R} \) .

Now suppose \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) is a unit-speed geodesic with \( b \geq  {\pi R} \) , and assume for the sake of contradiction that \( \gamma \) has no conjugate points. Let \( p = \gamma \left( 0\right) \) and \( v = {\gamma }^{\prime }\left( 0\right) \) , so \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) for \( t \in  \left\lbrack  {0, b}\right\rbrack \) . As in the proof of Theorem 11.9, because \( \gamma \) has no conjugate points, we can choose a star-shaped open subset \( W \subseteq  {T}_{p}M \) containing the set \( L = \left\{  {{tv} : 0 \leq  t < {b}_{0}}\right\}   \subseteq  {T}_{p}M \) on which \( {\exp }_{p} \) is a local diffeomorphism, and let \( \widetilde{g} \) be the pulled-back metric \( {\exp }_{p}^{ * }g \) on \( W \) , which satisfies the same curvature estimates as \( g \) . Then \( \widetilde{\gamma }\left( t\right)  = {tv} \) is a radial \( \widetilde{g} \) -geodesic in \( W \) of length greater than or equal to \( {\pi R} \) , which contradicts the argument in the preceding paragraph.

Corollary 11.17 (Injectivity Radius Comparison). Let \( \left( {M, g}\right) \) be a Riemannian n-manifold, and suppose there is a positive constant \( c = 1/{R}^{2} \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) . Then for every point \( p \in  M \) , we have \( \operatorname{inj}\left( p\right)  \leq  {\pi R} \) .

Proof. Every radial geodesic segment in a geodesic ball is minimizing, but the preceding theorem shows that no geodesic segment of length \( {\pi R} \) or greater is minimizing. Thus no geodesic ball has radius greater than \( {\pi R} \) .

Corollary 11.18 (Diameter Comparison). Let \( \left( {M, g}\right) \) be a complete, connected Riemannian n-manifold, and suppose there is a positive constant \( c = 1/{R}^{2} \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) . Then the diameter of \( M \) is less than or equal to \( {\pi R} \) .

Proof. This follows from the fact that any two points of \( M \) can be connected by a minimizing geodesic segment, and the conjugate point comparison theorem implies that no such segment can have length greater than \( {\pi R} \) .

Our final comparison theorem is a powerful volume estimate under the assumption of a lower bound on the Ricci curvature. We will use it in the proof of Theorem 12.28 in the next chapter, and it plays a central role in many of the more advanced results of Riemannian geometry.

A weaker version of this result was proved by Paul Günther in 1960 [Gün60] for balls within the injectivity radius under the assumption of a lower bound on sectional curvature; it was improved by Richard L. Bishop in 1963 (announced in [Bis63], with a proof in [BC64]) to require only a lower Ricci curvature bound; and then it was extended by Misha Gromov in 1981 [Gro07] to cover all metric balls in the complete case, not just those inside the injectivity radius.

Theorem 11.19 (Bishop-Gromov Volume Comparison). Let \( \left( {M, g}\right) \) be a connected Riemannian n-manifold, and suppose there is a constant \( c \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) c \) for all unit vectors \( v \) . Let \( p \in  M \) be given, and for every positive number \( \delta \) , let \( {V}_{g}\left( \delta \right) \) denote the volume of the metric ball of radius \( \delta \) about \( p \) in \( \left( {M, g}\right) \) , and let \( {V}_{c}\left( \delta \right) \) denote the volume of a metric ball of radius \( \delta \) in the \( n \) -dimensional Euclidean space, hyperbolic space, or sphere with constant sectional curvature \( c \) . Then for every \( 0 < \delta  \leq  \operatorname{inj}\left( p\right) \) , we have

\[
{V}_{g}\left( \delta \right)  \leq  {V}_{c}\left( \delta \right) \tag{11.32}
\]

and the quotient \( {V}_{g}\left( \delta \right) /{V}_{c}\left( \delta \right) \) is a nonincreasing function of \( \delta \) that approaches 1 as \( \delta  \searrow  0 \) . If \( \left( {M, g}\right) \) is complete, the same is true for all positive \( \delta \) , not just \( \delta  \leq  \operatorname{inj}\left( p\right) \) . In either case, if equality holds in (11.32) for some \( \delta \) , then \( g \) has constant sectional curvature on the entire metric ball of radius \( \delta \) about \( p \) .

Proof. First consider \( \delta  \leq  \operatorname{inj}\left( p\right) \) , in which case a metric ball of radius \( \delta \) in \( M \) is actually a geodesic ball. With the exception of the first and last paragraphs, the proof of Theorem 11.14 goes through with all of the inequalities reversed, and with the first Laplacian comparison theorem replaced by its counterpart Theorem 11.15, to show that \( {V}_{g}\left( \delta \right) /{V}_{c}\left( \delta \right) \) is a nonincreasing function of \( \delta \) that approaches 1 as \( \delta  \searrow  0 \) , and (11.32) follows.

In case \( M \) is complete, \( {\exp }_{p} \) is defined and smooth on all of \( {T}_{p}M \) . Theorem 10.34 shows that \( \operatorname{Cut}\left( p\right) \) has measure zero in \( M \) and \( {\exp }_{p} \) maps the open subset \( \operatorname{ID}\left( p\right)  \subseteq  {T}_{p}M \) diffeomorphically onto the complement of \( \operatorname{Cut}\left( p\right) \) in \( M \) . Therefore, for every \( \delta  > 0 \) , the metric ball of radius \( \delta \) is equal to \( {\exp }_{p}\left( {{B}_{\delta }\left( 0\right)  \cap  \operatorname{ID}\left( p\right) }\right) \) up to a set of measure zero, where \( {B}_{\delta }\left( 0\right) \) denotes the \( \delta \) -ball about 0 in \( {T}_{p}M \) . Using an orthonormal basis to identify \( \left( {{T}_{p}M,{g}_{p}}\right) \) with \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) , we can compute the volume of a metric \( \delta \) -ball as

\[
{V}_{g}\left( \delta \right)  = {\int }_{\mathrm{{ID}}\left( p\right)  \cap  {B}_{\delta }\left( 0\right) }{\exp }_{p}^{ * }d{V}_{g} = {\int }_{\mathrm{{ID}}\left( p\right)  \cap  {B}_{\delta }\left( 0\right) }\sqrt{\det g}d{V}_{\bar{g}},
\]

where \( \det g \) denotes the determinant of the matrix of \( g \) in the normal coordinates determined by the choice of basis.

Let \( \Phi  : {\mathbb{R}}^{ + } \times  {\mathbb{S}}^{n - 1} \rightarrow  {T}_{p}M \smallsetminus  \{ 0\}  \cong  {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) be the map \( \Phi \left( {\rho ,\omega }\right)  = {\rho \omega } \) as in Corollary 10.17, and define \( {\widetilde{s}}_{c} : {\mathbb{R}}^{ + } \rightarrow  \lbrack 0,\infty ) \) by \( {\widetilde{s}}_{c}\left( \rho \right)  = {s}_{c}\left( \rho \right) \) if \( c \leq  0 \) , while in the case \( c = 1/{R}^{2} > 0 \) ,

\[
{\widetilde{s}}_{c}\left( \rho \right)  = \left\{  \begin{array}{ll} {s}_{c}\left( \rho \right) , & \rho  < {\pi R}, \\  0, & \rho  \geq  {\pi R}. \end{array}\right.
\]

Corollary 11.18 shows that the cut time of every unit vector in \( {T}_{p}M \) is less than or equal to \( {\pi R} \) . Thus \( {\widetilde{s}}_{c}\left( \rho \right)  > 0 \) whenever \( \Phi \left( {\rho ,\omega }\right)  \in  \operatorname{ID}\left( p\right) \) , and we can define \( \widetilde{\lambda } : {\mathbb{R}}^{ + } \times \; {\mathbb{S}}^{n - 1} \rightarrow  \mathbb{R} \) by

\[
\widetilde{\lambda }\left( {\rho ,\omega }\right)  = \left\{  \begin{array}{ll} \frac{\left( \sqrt{\det g}\right)  \circ  \Phi \left( {\rho ,\omega }\right) {\rho }^{n - 1}}{{\widetilde{s}}_{c}{\left( \rho \right) }^{n - 1}}, & \Phi \left( {\rho ,\omega }\right)  \in  \mathrm{{ID}}\left( p\right) , \\  0, & \Phi \left( {\rho ,\omega }\right)  \notin  \mathrm{{ID}}\left( p\right) , \end{array}\right.
\]

and just as in the proof of Theorem 11.14, we can write

\[
{V}_{g}\left( \delta \right)  = {\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{\delta }\widetilde{\lambda }\left( {\rho ,\omega }\right) {\widetilde{s}}_{c}{\left( \rho \right) }^{n - 1}{d\rho d}{V}_{g},
\]

\[
{V}_{c}\left( \delta \right)  = {\int }_{{\mathbb{S}}^{n - 1}}{\int }_{0}^{\delta }{\widetilde{s}}_{c}{\left( \rho \right) }^{n - 1}{d\rho d}{V}_{g}^{ \circ  }.
\]

The arguments of Theorem 11.14 (with inequalities reversed) show that for each \( \omega  \in  {\mathbb{S}}^{n - 1} \) , the function \( \widetilde{\lambda }\left( {\rho ,\omega }\right) \) is nonincreasing in \( \rho \) for all positive \( \rho \) , and it follows just as in that proof that \( {V}_{g}\left( \delta \right) /{V}_{c}\left( \delta \right) \) (now interpreted as a ratio of volumes of metric balls) is nonincreasing for all \( \delta  > 0 \) and approaches 1 as \( \delta  \searrow  0 \) , and (11.32) follows.

Finally, suppose \( {V}_{g}\left( \delta \right)  = {V}_{c}\left( \delta \right) \) for some \( \delta  > 0 \) , and assume first that \( \delta  \leq  \operatorname{inj}\left( p\right) \) . An argument exactly analogous to the one at the end of the proof of Theorem 11.14 shows that \( \lambda \left( {\rho ,\omega }\right)  \equiv  1 \) everywhere on the set where \( 0 < \rho  < \delta \) . Combined with Lemma 11.13, this implies that

\[
{\Delta r} = \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) } \tag{11.33}
\]

everywhere on \( {B}_{\delta }\left( p\right)  \smallsetminus  \{ p\} \) . This means that along each unit-speed radial geodesic \( \gamma \) , the function \( u\left( t\right)  = {\left. \left( \Delta r\right) \right| }_{\gamma \left( t\right) }/\left( {n - 1}\right)  = {s}_{c}^{\prime }\left( t\right) /{s}_{c}\left( t\right) \) satisfies \( {u}^{\prime } + {u}^{2} + c \equiv  0 \) by direct computation. Comparing this to (11.30), we conclude that

\[
\frac{\operatorname{tr}\left( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2}\right)  + \operatorname{Rc}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) }{n - 1} \equiv  c
\]

on \( {B}_{\delta }\left( p\right)  \smallsetminus  \{ p\} \) . Since \( \operatorname{tr}\left( {\overset{ \circ  }{\mathcal{H}}}_{r}^{2}\right)  \geq  0 \) and \( {Rc}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right)  \geq  \left( {n - 1}\right) c \) everywhere, this is possible only if \( \operatorname{tr}\left( {\widehat{\mathcal{H}}}_{r}^{2}\right) \) vanishes identically there. Because \( {\widehat{\mathcal{H}}}_{r}^{2} \) is positive semidefinite and its trace is zero, it must vanish identically, which by definition of \( {\mathcal{H}}_{r} \) means

\[
{\mathcal{H}}_{r} = \frac{\Delta r}{n - 1}{\pi }_{r} = \frac{{s}_{c}^{\prime }\left( r\right) }{{s}_{c}\left( r\right) }{\pi }_{r}.
\]

Proposition 11.3 then shows that \( g \) has constant sectional curvature \( c \) on \( {B}_{\delta }\left( p\right) \) .

Now suppose \( \left( {M, g}\right) \) is complete. The argument of Theorem 11.14 then shows that \( \widetilde{\lambda }\left( {\rho ,\omega }\right)  \equiv  1 \) everywhere on the set where \( 0 < \rho  < \delta \) and \( {\widetilde{s}}_{c}\left( \rho \right)  > 0 \) . In view of the definition of \( \widetilde{\lambda } \) , this implies in particular that \( \operatorname{ID}\left( p\right)  \cap  {B}_{\delta }\left( 0\right) \) contains all of the points in \( {B}_{\delta }\left( 0\right) \) where \( {\widetilde{s}}_{c}\left( r\right)  > 0 \) . In case \( c \leq  0,{\widetilde{s}}_{c}\left( r\right)  = {s}_{c}\left( r\right)  > 0 \) everywhere, so \( \operatorname{ID}\left( p\right)  \cap  {B}_{\delta }\left( 0\right)  = {B}_{\delta }\left( 0\right) \) and therefore the metric ball of radius \( \delta \) around \( p \) is actually a geodesic ball, and the argument above applies.

In case \( c = 1/{R}^{2} > 0 \) , if \( \delta  \leq  {\pi R} \) , then \( {\widetilde{s}}_{c}\left( r\right)  = {s}_{c}\left( r\right)  > 0 \) on \( {B}_{\delta }\left( 0\right) \) , and once again we conclude that the metric \( \delta \) -ball is a geodesic ball. On the other hand, if \( \delta  > {\pi R} \) , then the diameter comparison theorem (Cor. 11.18) shows that the metric ball of radius \( \delta \) is actually the entire manifold. The fact that the volume ratio is nonincreasing implies that \( {V}_{g}\left( {\pi R}\right)  = {V}_{c}\left( {\pi R}\right) \) , and the argument above shows that \( g \) has constant sectional curvature \( c \) on the metric ball of radius \( {\pi R} \) . Since the closure of that ball is all of \( M \) , the result follows by continuity.

The next corollary is immediate.

Corollary 11.20. Suppose \( \left( {M, g}\right) \) is a compact Riemannian manifold and there is a positive constant \( c = 1/{R}^{2} \) such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq \; \left( {n - 1}\right) c \) for all unit vectors \( v \) . Then the volume of \( M \) is no greater than the volume of the \( n \) -sphere of radius \( R \) with its round metric, and if equality holds, then \( \left( {M, g}\right) \) has constant sectional curvature c.

(For explicit formulas for the volumes of \( n \) -spheres, see Problem 10-4.)

## Problems

11-1. Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( U \) be a normal neighborhood of \( p \in  M \) . Use Corollary 6.42 to show that in every choice of polar normal coordinates \( \left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}, r}\right) \) on a subset of \( U \smallsetminus  \{ p\} \) (see Example 6.45), the covariant Hessian of \( r \) is given by

\[
{\nabla }^{2}r = \frac{1}{2}\mathop{\sum }\limits_{{\alpha ,\beta  = 1}}^{{n - 1}}\left( {{\partial }_{r}{g}_{\alpha \beta }}\right) d{\theta }^{\alpha }d{\theta }^{\beta }.
\]

11-2. Prove the following extension to Proposition 11.2: Suppose \( P \) is an embedded submanifold of a Riemannian manifold \( \left( {M, g}\right) , U \) is a normal neighborhood of \( P \) in \( M \) , and \( r \) is the radial distance function for \( P \) in \( U \) (see Prop. 6.37). If \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) is a geodesic segment with \( \gamma \left( 0\right)  \in  P \) and \( {\gamma }^{\prime }\left( 0\right) \) normal to \( P \) , and \( J \) is a Jacobi field along \( \gamma \) that is transverse to \( P \) in the sense of Problem 10-14, then \( {D}_{t}J\left( t\right)  = {\mathcal{H}}_{r}\left( {J\left( t\right) }\right) \) for all \( t \in  \left\lbrack  {0, b}\right\rbrack \) .

11-3. Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( f \) be any smooth local distance function defined on an open subset \( U \subseteq  M \) . Let \( F = \operatorname{grad}f \) (so the integral curves of \( F \) are unit-speed geodesics), and let \( {\mathcal{H}}_{f} = \nabla F \) (the Hessian operator of \( f \) ). Show that \( {\mathcal{H}}_{f} \) satisfies the following Riccati equation along each integral curve \( \gamma \) of \( F \) :

\[
{D}_{t}{\mathcal{H}}_{f} + {\mathcal{H}}_{f}^{2} + {R}_{{\gamma }^{\prime }} = 0, \tag{11.34}
\]

where \( {R}_{{\gamma }^{\prime }}\left( w\right)  = R\left( {w,{\gamma }^{\prime }}\right) {\gamma }^{\prime } \) . [Hint: Let \( W \) be any smooth vector field on \( U \) , and evaluate \( {\nabla }_{F}{\nabla }_{W}F \) in two different ways.]

11-4. Let \( \left( {M, g}\right) \) be a compact Riemannian manifold. Prove that if \( R, L \) are positive numbers such that all sectional curvatures of \( M \) are less than or equal to \( 1/{R}^{2} \) and all closed geodesics have lengths greater than or equal to \( L \) , then

\[
\operatorname{inj}\left( M\right)  \geq  \min \left( {{\pi R},\frac{1}{2}L}\right) .
\]

[Hint: Assume not, and use the result of Problem 10-23(b).]

11-5. TRANSVERSE JACOBI FIELD COMPARISON THEOREM: Let \( P \) be an embedded hypersurface in a Riemannian manifold \( \left( {M, g}\right) \) . Suppose \( \gamma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow \; M \) is a unit-speed geodesic segment with \( \gamma \left( 0\right)  \in  P \) and \( {\gamma }^{\prime }\left( 0\right) \) normal to \( P \) , and \( J \) is a normal Jacobi field along \( \gamma \) that is transverse to \( P \) . Let \( \lambda  = h\left( {J\left( 0\right) , J\left( 0\right) }\right) \) , where \( h \) is the scalar second fundamental form of \( P \) with respect to the normal \( - {\gamma }^{\prime }\left( 0\right) \) . Let \( c \) be a real number, and let \( u : \mathbb{R} \rightarrow  \mathbb{R} \) be the unique solution to the initial value problem

\[
{u}^{\prime \prime }\left( t\right)  + {cu}\left( t\right)  = 0,
\]

\[
u\left( 0\right)  = 1, \tag{11.35}
\]

\[
{u}^{\prime }\left( 0\right)  = \lambda \text{ . }
\]

In the following statements, the principal curvatures of \( P \) are computed with respect to the normal \( - {\gamma }^{\prime }\left( 0\right) \) .

(a) If all sectional curvatures of \( M \) are bounded above by \( c \) , all principal curvatures of \( P \) at \( \gamma \left( 0\right) \) are bounded below by \( \lambda \) , and \( u\left( t\right)  \neq  0 \) for \( t \in \; \left( {0, b}\right) \) , then \( \left| {J\left( t\right) }\right|  \geq  u\left( t\right) \left| {J\left( 0\right) }\right| \) for all \( t \in  \left\lbrack  {0, b}\right\rbrack \) .

(b) If all sectional curvatures of \( M \) are bounded below by \( c \) , all principal curvatures of \( P \) at \( \gamma \left( 0\right) \) are bounded above by \( \lambda \) , and \( J\left( t\right)  \neq  0 \) for \( t \in \; \left( {0, b}\right) \) , then \( \left| {J\left( t\right) }\right|  \leq  u\left( t\right) \left| {J\left( 0\right) }\right| \) for all \( t \in  \left\lbrack  {0, b}\right\rbrack \) .

[Hint: Mimic the proof of Theorem 11.9, using the results of Problems 11-3 and 11-2.]

11-6. Suppose \( P \) is an embedded hypersurface in a Riemannian manifold \( \left( {M, g}\right) \) and \( N \) is a unit normal vector field along \( P \) . Suppose the principal curvatures of \( P \) with respect to \( - N \) are bounded below by a constant \( \lambda \) , and the sectional curvatures of \( M \) are bounded above by \( - {\lambda }^{2} \) . Prove that \( P \) has no focal points along any geodesic segment with initial velocity \( {N}_{p} \) for \( p \in  P \) .

11-7. Suppose \( P \) is an embedded hypersurface in a Riemannian manifold \( \left( {M, g}\right) \) and \( N \) is a unit normal vector field along \( P \) . Suppose the sectional curvatures of \( M \) are bounded below by a constant \( c \) , and the principal curvatures of \( P \) with respect to \( - N \) are bounded above by a constant \( \lambda \) . Let \( u \) be the solution to the initial value problem (11.35). Prove that if \( b \) is a positive real number such that \( u\left( b\right)  = 0 \) , then \( P \) has a focal point along every geodesic segment with initial velocity \( {N}_{p} \) for some \( p \in  P \) and with length greater than or equal to \( b \) .
