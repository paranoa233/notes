# §5 Oriented Manifolds

IN ORDER to define the degree as an integer (rather than an integer modulo 2) we must introduce orientations.

DEFINITIONS. An orientation for a finite dimensional real vector space is an equivalence class of ordered bases as follows: the ordered basis \( \left( {{b}_{1},\cdots ,{b}_{n}}\right) \) determines the same orientation as the basis \( \left( {{b}_{1}^{\prime },\cdots ,{b}_{n}^{\prime }}\right) \) if \( {b}_{i}^{\prime } = \sum {a}_{ij}{b}_{j} \) with \( \det \left( {a}_{ij}\right)  > 0 \) . It determines the opposite orientation if \( \det \left( {a}_{ij}\right)  < 0 \) . Thus each positive dimensional vector space has precisely two orientations. The vector space \( {R}^{n} \) has a standard orientation corresponding to the basis \( \left( {1,0,\cdots ,0}\right) ,\left( {0,1,0,\cdots ,0}\right) ,\cdots ,\left( {0,\cdots ,0,1}\right) \) .

In the case of the zero dimensional vector space it is convenient to define an "orientation" as the symbol +1 or -1 .

An oriented smooth manifold consists of a manifold \( M \) together with a choice of orientation for each tangent space \( T{M}_{x} \) . If \( m \geq  1 \) , these are required to fit together as follows: For each point of \( M \) there should exist a neighborhood \( U \subset  M \) and a diffeomorphism \( h \) mapping \( U \) onto an open subset of \( {R}^{m} \) or \( {H}^{m} \) which is orientation preserving, in the sense that for each \( {x\varepsilon U} \) the isomorphism \( d{h}_{x} \) carries the specified orientation for \( T{M}_{x} \) into the standard orientation for \( {R}^{m} \) .

If \( M \) is connected and orientable, then it has precisely two orientations.

If \( M \) has a boundary, we can distinguish three kinds of vectors in the tangent space \( T{M}_{x} \) at a boundary point:

1) there are the vectors tangent to the boundary, forming an \( \left( {m - 1}\right) \) - dimensional subspace \( T{\left( \partial M\right) }_{x} \subset  T{M}_{x} \) ;

2) there are the "outward" vectors, forming an open half space bounded by \( T{\left( \partial M\right) }_{x} \) ;

3) there are the "inward" vectors forming a complementary half space.

Each orientation for \( M \) determines an orientation for \( \partial M \) as follows: For \( {x\varepsilon }\partial M \) choose a positively oriented basis \( \left( {{v}_{1},{v}_{2},\cdots ,{v}_{m}}\right) \) for \( T{M}_{x} \) in such a way that \( {v}_{2},\cdots ,{v}_{m} \) are tangent to the boundary (assuming that \( m \geq  2 \) ) and that \( {v}_{1} \) is an "outward" vector. Then \( \left( {{v}_{2},\cdots ,{v}_{m}}\right) \) determines the required orientation for \( \partial M \) at \( x \) .

If the dimension of \( M \) is 1, then each boundary point \( x \) is assigned the orientation -1 or +1 according as a positively oriented vector at \( x \) points inward or outward. (See Figure 8.)

![bo_d7du9valb0pc73deirc0_37_328_733_807_333_0.jpg](images/bo_d7du9valb0pc73deirc0_37_328_733_807_333_0.jpg)

Figure 8. How to orient a boundary

As an example the unit sphere \( {S}^{m - 1} \subset  {R}^{m} \) can be oriented as the boundary of the disk \( {D}^{m} \) .

## THE BROUWER DEGREE

Now let \( M \) and \( N \) be oriented \( n \) -dimensional manifolds without boundary and let

\[
f : M \rightarrow  N
\]

be a smooth map. If \( M \) is compact and \( N \) is connected, then the degree of \( f \) is defined as follows:

Let \( {x\varepsilon M} \) be a regular point of \( f \) , so that \( d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{f\left( x\right) } \) is a linear isomorphism between oriented vector spaces. Define the sign of \( d{f}_{x} \) to be +1 or -1 according as \( d{f}_{x} \) preserves or reverses orientation. For any regular value \( y \) : \( N \) define

\[
\deg \left( {f;y}\right)  = \mathop{\sum }\limits_{{{x\varepsilon }{f}^{-1}\left( y\right) }}\operatorname{sign}d{f}_{x}.
\]

As in \( \text{ § }1 \) , this integer \( \deg \left( {f;y}\right) \) is a locally constant function of \( y \) . It is defined on a dense open subset of \( N \) .

Theorem A. The integer \( \deg \left( {f;y}\right) \) does not depend on the choice of regular value \( y \) .

It will be called the degree of \( f \) (denoted \( \deg f \) ).

Theorem B. If \( f \) is smoothly homotopic to \( g \) , then \( \deg f = \deg g \) .

The proof will be essentially the same as that in \( \text{ § }4 \) . It is only necessary to keep careful control of orientations.

First consider the following situation: Suppose that \( M \) is the boundary of a compact oriented manifold \( X \) and that \( M \) is oriented as the boundary of \( X \) .

Lemma 1. If \( f : M \rightarrow  N \) extends to a smooth map \( F : X \rightarrow  N \) , then \( \deg \left( {f;y}\right)  = 0 \) for every regular value \( y \) .

Proof. First suppose that \( y \) is a regular value for \( F \) , as well as for \( f = F \mid  M \) . The compact 1-manifold \( {F}^{-1}\left( y\right) \) is a finite union of arcs and circles, with only the boundary points of the arcs lying on \( M = \partial X \) . Let \( A \subset  {F}^{-1}\left( y\right) \) be one of these arcs, with \( \partial A = \{ a\}  \cup  \{ b\} \) . We will show that

\[
\operatorname{sign}d{f}_{a} + \operatorname{sign}d{f}_{b} = 0,
\]

and hence (summing over all such arcs) that \( \deg \left( {f;y}\right)  = 0 \) .

![bo_d7du9valb0pc73deirc0_38_222_1333_875_282_0.jpg](images/bo_d7du9valb0pc73deirc0_38_222_1333_875_282_0.jpg)

Figure 9. How to orient \( {F}^{-1}\left( y\right) \)

The orientations for \( X \) and \( N \) determine an orientation for \( A \) as follows: Given \( {x\varepsilon A} \) , let \( \left( {{v}_{1},\cdots ,{v}_{n + 1}}\right) \) be a positively oriented basis for \( T{X}_{x} \) with \( {v}_{1} \) tangent to \( A \) . Then \( {v}_{1} \) determines the required orientation for \( T{A}_{x} \) if and only if \( d{F}_{x} \) carries \( \left( {{v}_{2},\cdots ,{v}_{n + 1}}\right) \) into a positively oriented basis for \( T{N}_{y} \) .

Let \( {v}_{1}\left( x\right) \) denote the positively oriented unit vector tangent to \( A \) at \( x \) . Clearly \( {v}_{1} \) is a smooth function, and \( {v}_{1}\left( x\right) \) points outward at one boundary point (say \( b \) ) and inward at the other boundary point \( a \) .

It follows immediately that

\[
\operatorname{sign}d{f}_{a} =  - 1,\;\operatorname{sign}d{f}_{b} =  + 1;
\]

with sum zero. Adding up over all such arcs \( A \) , we have proved that \( \deg \left( {f;y}\right)  = 0 \) .

More generally, suppose that \( {y}_{0} \) is a regular value for \( f \) , but not for \( F \) . The function \( \deg \left( {f;y}\right) \) is constant within some neighborhood \( U \) of \( {y}_{0} \) . Hence, as in \( \text{ § }4 \) , we can choose a regular value \( y \) for \( F \) within \( U \) and observe that

\[
\deg \left( {f;{y}_{0}}\right)  = \deg \left( {f;y}\right)  = 0.
\]

This proves Lemma 1.

Now consider a smooth homotopy \( F : \left\lbrack  {0,1}\right\rbrack   \times  M \rightarrow  N\; \) between two mappings \( \;f\left( x\right)  = F\left( {0, x}\right) ,\;g\left( x\right)  = F\left( {1, x}\right) . \)

Lemma 2. The degree \( \deg \left( {g;y}\right) \) is equal to \( \deg \left( {f;y}\right) \) for any common regular value \( y \) .

Proof. The manifold \( \left\lbrack  {0,1}\right\rbrack   \times  {M}^{n} \) can be oriented as a product, and will then have boundary consisting of \( 1 \times  {M}^{n} \) (with the correct orientation) and \( 0 \times  {M}^{n} \) (with the wrong orientation). Thus the degree of \( F \mid  \partial \left( {\left\lbrack  {0,1}\right\rbrack   \times  {M}^{n}}\right) \) at a regular value \( y \) is equal to the difference

\[
\deg \left( {g;y}\right)  - \deg \left( {f;y}\right) \text{ . }
\]

According to Lemma 1 this difference must be zero.

The remainder of the proof of Theorems A and B is completely analogous to the argument in \( \text{ § }4 \) . If \( y \) and \( z \) are both regular values for \( f : M \rightarrow  N \) , choose a diffeomorphism \( h : N \rightarrow  N \) that carries \( y \) to \( z \) and is isotopic to the identity. Then \( h \) will preserve orientation, and

\[
\deg \left( {f;y}\right)  = \deg \left( {h \circ  f;h\left( y\right) }\right)
\]

by inspection. But \( f \) is homotopic to \( h \circ  f \) ; hence

\[
\deg \left( {h \circ  f;z}\right)  = \deg \left( {f;z}\right)
\]

by Lemma 2. Therefore \( \deg \left( {f;y}\right)  = \deg \left( {f;z}\right) \) , which completes the proof.

Examples. The complex function \( z \rightarrow  {z}^{k}, z \neq  0 \) , maps the unit circle onto itself with degree \( k \) . (Here \( k \) may be positive, negative, or zero.) The degenerate mapping

\[
f : M \rightarrow  \text{ constant }{\varepsilon N}
\]

has degree zero. A diffeomorphism \( f : M \rightarrow  N \) has degree +1 or -1 according as \( f \) preserves or reverses orientation. Thus an orientation reversing diffeomorphism of a compact boundaryless manifold is not smoothly homotopic to the identity.

One example of an orientation reversing diffeomorphism is provided by the reflection \( {r}_{i} : {S}^{n} \rightarrow  {S}^{n} \) , where

\[
{r}_{\imath }\left( {{x}_{1},\cdots ,{x}_{n + 1}}\right)  = \left( {{x}_{1},\cdots , - {x}_{i},\cdots ,{x}_{n + 1}}\right) .
\]

The antipodal map of \( {S}^{n} \) has degree \( {\left( -1\right) }^{n + 1} \) , as we can see by noting that the antipodal map is the composition of \( n + 1 \) reflections:

\[
- x = {r}_{1} \circ  {r}_{2} \circ  \cdots  \circ  {r}_{n + 1}\left( x\right) .
\]

Thus if \( n \) is even, the antipodal map of \( {S}^{n} \) is not smoothly homotopic to the identity, a fact not detected by the degree modulo 2.

As an application, following Brouwer, we show that \( {S}^{n} \) admits a smooth field of nonzero tangent vectors if and only if \( n \) is odd. (Compare Figures 10 and 11.)

![bo_d7du9valb0pc73deirc0_40_557_1180_237_236_0.jpg](images/bo_d7du9valb0pc73deirc0_40_557_1180_237_236_0.jpg)

Figure 10 (above). A nonzero vector field on the 1-sphere

Figure 11 (below). Attempts for \( n = \mathcal{2} \)

![bo_d7du9valb0pc73deirc0_40_377_1606_580_253_0.jpg](images/bo_d7du9valb0pc73deirc0_40_377_1606_580_253_0.jpg)

DEFINITION. A smooth tangent vector field on \( M \subset  {R}^{k} \) is a smooth map \( v : M \rightarrow  {R}^{k} \) such that \( v\left( x\right) {\varepsilon T}{M}_{x} \) for each \( {x\varepsilon M} \) . In the case of the sphere \( {S}^{n} \subset  {R}^{n + 1} \) this is clearly equivalent to the condition

1)

\[
v\left( x\right)  \cdot  x = 0\text{ for all }{x\varepsilon }{S}^{n},
\]

using the euclidean inner product.

If \( v\left( x\right) \) is nonzero for all \( x \) , then we may as well suppose that

2)

\[
v\left( x\right)  \cdot  v\left( x\right)  = 1\text{ for all }{x\varepsilon }{S}^{n}.
\]

For in any case \( \bar{v}\left( x\right)  = v\left( x\right) /\parallel v\left( x\right) \parallel \) would be a vector field which does satisfy this condition. Thus we can think of \( v \) as a smooth function from \( {S}^{n} \) to itself.

Now define a smooth homotopy

\[
F : {S}^{n} \times  \left\lbrack  {0,\pi }\right\rbrack   \rightarrow  {S}^{n}
\]

by the formula \( F\left( {x,\theta }\right)  = x\cos \theta  + v\left( x\right) \sin \theta \) . Computation shows that

\[
F\left( {x,\theta }\right)  \cdot  F\left( {x,\theta }\right)  = 1
\]

and that

\[
F\left( {x,0}\right)  = x,\;F\left( {x,\pi }\right)  =  - x.
\]

Thus the antipodal map of \( {S}^{n} \) is homotopic to the identity. But for \( n \) even we have seen that this is impossible.

On the other hand, if \( n = {2k} - 1 \) , the explicit formula

\[
v\left( {{x}_{1},\cdots ,{x}_{2k}}\right)  = \left( {{x}_{2}, - {x}_{1},{x}_{4}, - {x}_{3},\cdots ,{x}_{2k}, - {x}_{{2k} - 1}}\right)
\]

defines a nonzero tangent vector field on \( {S}^{n} \) . This completes the proof.

It follows, incidentally, that the antipodal map of \( {S}^{n} \) is homotopic to the identity for \( n \) odd. A famous theorem due to Heinz Hopf asserts that two mappings from a connected \( n \) -manifold to the \( n \) -sphere are smoothly homotopic if and only if they have the same degree. In \( \text{ § }7 \) we will prove a more general result which implies Hopf's theorem.
