# §2 The Theorem of Sard and Brown

IN GENERAL, it is too much to hope that the set of critical values of a smooth map be finite. But this set will be "small," in the sense indicated by the next theorem, which was proved by A. Sard in 1942 following earlier work by A. P. Morse. (References [30], [24].)

Theorem. Let \( f : U \rightarrow  {R}^{n} \) be a smooth map, defined on an open set \( U \subset  {R}^{m} \) , and let

\[
C = \left\{  {{x\varepsilon U} \mid  \text{ rank }d{f}_{x} < n}\right\}  .
\]

Then the image \( f\left( C\right)  \subset  {R}^{n} \) has Lebesgue measure zero.*

Since a set of measure zero cannot contain any nonvacuous open set, it follows that the complement \( {R}^{n} - f\left( C\right) \) must be everywhere dense† in \( {R}^{n} \) .

The proof will be given in \( \text{ § }3 \) . It is essential for the proof that \( f \) should have many derivatives. (Compare Whitney [38].)

We will be mainly interested in the case \( m \geq  n \) . If \( m < n \) , then clearly \( C = U \) ; hence the theorem says simply that \( f\left( U\right) \) has measure zero.

More generally consider a smooth map \( f : M \rightarrow  N \) , from a manifold of dimension \( m \) to a manifold of dimension \( n \) . Let \( C \) be the set of all \( {x\varepsilon M} \) such that

\[
d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{f\left( x\right) }
\]

has rank less than \( n \) (i.e. is not onto). Then \( C \) will be called the set of critical points, \( f\left( C\right) \) the set of critical values, and the complement \( N - f\left( C\right) \) the set of regular values of \( f \) . (This agrees with our previous definitions in the case \( m = n \) .) Since \( M \) can be covered by a countable collection of neighborhoods each diffeomorphic to an open subset of \( {R}^{m} \) , we have:

---

* In other words, given any \( \epsilon  > 0 \) , it is possible to cover \( f\left( C\right) \) by a sequence of cubes in \( {R}^{n} \) having total \( n \) -dimensional volume less than \( \epsilon \) .

† Proved by Arthur B. Brown in 1935. This result was rediscovered by Dubovickii in 1953 and by Thom in 1954. (References [5], [8], [36].)

---

Corollary (A. B. Brown). The set of regular values of a smooth map \( f : M \rightarrow  N \) is everywhere dense in \( N \) .

In order to exploit this corollary we will need the following:

Lemma 1. If \( f : M \rightarrow  N \) is a smooth map between manifolds of dimension \( m \geq  n \) , and if \( {y\varepsilon N} \) is a regular value, then the set \( {f}^{-1}\left( y\right)  \subset  M \) is a smooth manifold of dimension \( m - n \) .

Proof. Let \( {x\varepsilon }{f}^{-1}\left( y\right) \) . Since \( y \) is a regular value, the derivative \( d{f}_{x} \) must map \( T{M}_{x} \) onto \( T{N}_{y} \) . The null space \( \mathfrak{N} \subset  T{M}_{x} \) of \( d{f}_{x} \) will therefore be an \( \left( {m - n}\right) \) -dimensional vector space.

If \( M \subset  {R}^{k} \) , choose a linear map \( L : {R}^{k} \rightarrow  {R}^{m - n} \) that is nonsingular on this subspace \( \mathfrak{N} \subset  T{M}_{x} \subset  {R}^{k} \) . Now define

\[
F : M \rightarrow  N \times  {R}^{m - n}
\]

by \( F\left( \xi \right)  = \left( {f\left( \xi \right) , L\left( \xi \right) }\right) \) . The derivative \( d{F}_{x} \) is clearly given by the formula

\[
d{F}_{x}\left( v\right)  = \left( {d{f}_{x}\left( v\right) , L\left( v\right) }\right) .
\]

Thus \( d{F}_{x} \) is nonsingular. Hence \( F \) maps some neighborhood \( U \) of \( x \) diffeomorphically onto a neighborhood \( V \) of \( \left( {y, L\left( x\right) }\right) \) . Note that \( {f}^{-1}\left( y\right) \) corresponds, under \( F \) , to the hyperplane \( y \times  {R}^{m - n} \) . In fact \( F \) maps \( {f}^{-1}\left( y\right)  \cap  U \) diffeomorphically onto \( \left( {y \times  {R}^{m - n}}\right)  \cap  V \) . This proves that \( {f}^{-1}\left( y\right) \) is a smooth manifold of dimension \( m - n \) .

As an example we can give an easy proof that the unit sphere \( {S}^{m - 1} \) is a smooth manifold. Consider the function \( f : {R}^{m} \rightarrow  R \) defined by

\[
f\left( x\right)  = {x}_{1}^{2} + {x}_{2}^{2} + \cdots  + {x}_{m}^{2}.
\]

Any \( y \neq  0 \) is a regular value, and the smooth manifold \( {f}^{-1}\left( 1\right) \) is the unit sphere.

If \( {M}^{\prime } \) is a manifold which is contained in \( M \) , it has already been noted that \( T{M}_{x}^{\prime } \) is a subspace of \( T{M}_{x} \) for \( {x\varepsilon }{M}^{\prime } \) . The orthogonal complement of \( T{M}_{x}^{\prime } \) in \( T{M}_{x} \) is then a vector space of dimension \( m - {m}^{\prime } \) called the space of normal vectors to \( {M}^{\prime } \) in \( M \) at \( x \) .

In particular let \( {M}^{\prime } = {f}^{-1}\left( y\right) \) for a regular value \( y \) of \( f : M \rightarrow  N \) .

Lemma 2. The null space of \( d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{y} \) is precisely equal to the tangent space \( T{M}_{x}^{\prime } \subset  T{M}_{x} \) of the submanifold \( {M}^{\prime } = {f}^{-1}\left( y\right) \) . Hence \( d{f}_{x} \) maps the orthogonal complement of \( T{M}_{x}^{\prime } \) isomorphically onto \( T{N}_{v} \) .

Proof. From the diagram

![bo_d7du9valb0pc73deirc0_22_501_511_311_238_0.jpg](images/bo_d7du9valb0pc73deirc0_22_501_511_311_238_0.jpg)

we see that \( d{f}_{x} \) maps the subspace \( T{M}_{x}^{\prime } \subset  T{M}_{x} \) to zero. Counting dimensions we see that \( d{f}_{x} \) maps the space of normal vectors to \( {M}^{\prime } \) isomorphically onto \( T{N}_{y} \) .

## MANIFOLDS WITH BOUNDARY

The lemmas above can be sharpened so as to apply to a map defined on a smooth "manifold with boundary." Consider first the closed half-space

\[
{H}^{m} = \left\{  {\left( {{x}_{1},\cdots ,{x}_{m}}\right) \varepsilon {R}^{m} \mid  {x}_{m} \geq  0}\right\}  .
\]

The boundary \( \partial {H}^{m} \) is defined to be the hyperplane \( {R}^{m - 1} \times  0 \subset  {R}^{m} \) .

DEFINITION. A subset \( X \subset  {R}^{k} \) is called a smooth m-manifold with boundary if each \( {x\varepsilon X} \) has a neighborhood \( U \cap  X \) diffeomorphic to an open subset \( V \cap  {H}^{m} \) of \( {H}^{m} \) . The boundary \( \partial X \) is the set of all points in \( X \) which correspond to points of \( \partial {H}^{m} \) under such a diffeomorphism.

It is not hard to show that \( \partial X \) is a well-defined smooth manifold of dimension \( m - 1 \) . The interior \( X - \partial X \) is a smooth manifold of dimension \( m \) .

The tangent space \( T{X}_{x} \) is defined just as in \( \text{ § }1 \) , so that \( T{X}_{x} \) is a full \( m \) -dimensional vector space, even if \( x \) is a boundary point.

Here is one method for generating examples. Let \( M \) be a manifold without boundary and let \( g : M \rightarrow  R \) have 0 as regular value.

Lemma 3. The set of \( x \) in \( M \) with \( g\left( x\right)  \geq  0 \) is a smooth manifold, with boundary equal to \( {g}^{-1}\left( 0\right) \) .

The proof is just like the proof of Lemma 1.

EXAMPLE. The unit disk \( {D}^{m} \) , consisting of all \( {x\varepsilon }{R}^{m} \) with

\[
1 - \sum {x}_{i}^{2} \geq  0
\]

is a smooth manifold, with boundary equal to \( {S}^{m - 1} \) .

Now consider a smooth map \( f : X \rightarrow  N \) from an \( m \) -manifold with boundary to an \( n \) -manifold, where \( m > n \) .

Lemma 4. If \( {y\varepsilon N} \) is a regular value, both for \( f \) and for the restriction \( f \mid  \partial X \) , then \( {f}^{-1}\left( y\right)  \subset  X \) is a smooth \( \left( {m - n}\right) \) -manifold with boundary. Furthermore the boundary \( \partial \left( {{f}^{-1}\left( y\right) }\right) \) is precisely equal to the intersection of \( {f}^{-1}\left( y\right) \) with \( \partial X \) .

Proof. Since we have to prove a local property, it suffices to consider the special case of a map \( f : {H}^{m} \rightarrow  {R}^{n} \) , with regular value \( y \) ε \( {R}^{n} \) . Let \( \bar{x} \) ε \( {f}^{-1}\left( y\right) \) . If \( \bar{x} \) is an interior point, then as before \( {f}^{-1}\left( y\right) \) is a smooth manifold in the neighborhood of \( \bar{x} \) .

Suppose that \( \bar{x} \) is a boundary point. Choose a smooth map \( g : U \rightarrow  {R}^{n} \) that is defined throughout a neighborhood of \( \bar{x} \) in \( {R}^{m} \) and coincides with \( f \) on \( U \cap  {H}^{m} \) . Replacing \( U \) by a smaller neighborhood if necessary, we may assume that \( g \) has no critical points. Hence \( {g}^{-1}\left( y\right) \) is a smooth manifold of dimension \( m - n \) .

Let \( \pi  : {g}^{-1}\left( y\right)  \rightarrow  R \) denote the coordinate projection,

\[
\pi \left( {{x}_{1},\cdots ,{x}_{m}}\right)  = {x}_{m}.
\]

We claim that \( \pi \) has 0 as a regular value. For the tangent space of \( {g}^{-1}\left( y\right) \) at a point \( {x\varepsilon }{\pi }^{-1}\left( 0\right) \) is equal to the null space of

\[
d{g}_{x} = d{f}_{x} : {R}^{m} \rightarrow  {R}^{n};
\]

but the hypothesis that \( f \mid  \partial {H}^{m} \) is regular at \( x \) guarantees that this null space cannot be completely contained in \( {R}^{m - 1} \times  0 \) .

Therefore the set \( {g}^{-1}\left( y\right)  \cap  {H}^{m} = {f}^{-1}\left( y\right)  \cap  U \) , consisting of all \( {x\varepsilon }{g}^{-1}\left( y\right) \) with \( \pi \left( x\right)  \geq  0 \) , is a smooth manifold, by Lemma 3; with boundary equal to \( {\pi }^{-1}\left( 0\right) \) . This completes the proof.

## THE BROUWER FIXED POINT THEOREM

We now apply this result to prove the key lemma leading to the classical Brouwer fixed point theorem. Let \( X \) be a compact manifold with boundary.

Lemma 5. There is no smooth map \( f : X \rightarrow  \partial X \) that leaves \( \partial X \) pointwise fixed.

Proof (following M. Hirsch). Suppose there were such a map \( f \) . Let \( {y\varepsilon }\partial X \) be a regular value for \( f \) . Since \( y \) is certainly a regular value for the identity map \( f \mid  \partial X \) also, it follows that \( {f}^{-1}\left( y\right) \) is a smooth 1- manifold, with boundary consisting of the single point

\[
{f}^{-1}\left( y\right)  \cap  \partial X = \{ y\} .
\]

But \( {f}^{-1}\left( y\right) \) is also compact, and the only compact 1-manifolds are finite disjoint unions of circles and segments,* so that \( \partial {f}^{-1}\left( y\right) \) must consist of an even number of points. This contradiction establishes the lemma.

In particular the unit disk

\[
{D}^{n} = \left\{  {{x\varepsilon }{R}^{n} \mid  {x}_{1}^{2} + \cdots  + {x}_{n}^{2} \leq  1}\right\}
\]

is a compact manifold bounded by the unit sphere \( {S}^{n - 1} \) . Hence as a special case we have proved that the identity map of \( {S}^{n - 1} \) cannot be extended to a smooth map \( {D}^{n} \rightarrow  {S}^{n - 1} \) .

Lemma 6. Any smooth map \( g : {D}^{n} \rightarrow  {D}^{n} \) has a fixed point (i.e. a point \( {x\varepsilon }{D}^{n} \) with \( g\left( x\right)  = x) \) .

Proof. Suppose \( g \) has no fixed point. For \( {x\varepsilon }{D}^{n} \) , let \( f\left( x\right) \varepsilon {S}^{n - 1} \) be the point nearer \( x \) on the line through \( x \) and \( g\left( x\right) \) . (See Figure 4.) Then \( f : {D}^{n} \rightarrow  {S}^{n - 1} \) is a smooth map with \( f\left( x\right)  = x \) for \( {x\varepsilon }{S}^{n - 1} \) , which is impossible by Lemma 5. (To see that \( f \) is smooth we make the following explicit computation: \( f\left( x\right)  = x + {tu} \) , where

\[
u = \frac{x - g\left( x\right) }{\left| \right| x - g\left( x\right) \left| \right| },\;t =  - x \cdot  u + \sqrt{1 - x \cdot  x + {\left( x \cdot  u\right) }^{2}},
\]

the expression under the square root sign being strictly positive. Here and subsequently \( \parallel x\parallel \) denotes the euclidean length \( \sqrt{{x}_{1}^{2} + \cdots  + {x}_{n}^{2}} \) .)

Brouwer Fixed Point Theorem. Any continuous function \( G : {D}^{n} \rightarrow  {D}^{n} \) has a fixed point.

Proof. We reduce this theorem to the lemma by approximating \( G \) by a smooth mapping. Given \( \epsilon  > 0 \) , according to the Weierstrass approximation theorem,† there is a polynomial function \( {P}_{1} : {R}^{n} \rightarrow  {R}^{n} \) with \( \begin{Vmatrix}{{P}_{1}\left( x\right)  - G\left( x\right) }\end{Vmatrix} < \epsilon \) for \( {x\varepsilon }{D}^{n} \) . However, \( {P}_{1} \) may send points of \( {D}^{n} \) into points outside of \( {D}^{n} \) . To correct this we set

\[
P\left( x\right)  = {P}_{1}\left( x\right) /\left( {1 + \epsilon }\right) .
\]

---

* A proof is given in the Appendix.

† See for example Dieudonné [7, p. 133].

---

![bo_d7du9valb0pc73deirc0_25_508_291_439_408_0.jpg](images/bo_d7du9valb0pc73deirc0_25_508_291_439_408_0.jpg)

Figure 4

Then clearly \( P \) maps \( {D}^{n} \) into \( {D}^{n} \) and \( \begin{Vmatrix}{P\left( x\right)  - G\left( x\right) }\end{Vmatrix} < {2\epsilon } \) for \( {x\varepsilon }{D}^{n} \) .

Suppose that \( G\left( x\right)  \neq  x \) for all \( {x\varepsilon }{D}^{n} \) . Then the continuous function \( \begin{Vmatrix}{G\left( x\right)  - x}\end{Vmatrix} \) must take on a minimum \( \mu  > 0 \) on \( {D}^{n} \) . Choosing \( P : {D}^{n} \rightarrow  {D}^{n} \) as above, with \( \parallel P\left( x\right)  - G\left( x\right) \parallel  < \mu \) for all \( x \) , we clearly have \( P\left( x\right)  \neq  x \) . Thus \( P \) is a smooth map from \( {D}^{n} \) to itself without a fixed point. This contradicts Lemma 6, and completes the proof.

The procedure employed here can frequently be applied in more general situations: to prove a proposition about continuous mappings, we first establish the result for smooth mappings and then try to use an approximation theorem to pass to the continuous case. (Compare §8, Problem 4.)
