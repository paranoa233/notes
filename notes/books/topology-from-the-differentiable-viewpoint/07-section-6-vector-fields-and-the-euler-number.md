# §6 Vector Fields and the Euler Number

As a further application of the concept of degree, we study vector fields on other manifolds.

Consider first an open set \( U \subset  {R}^{m} \) and a smooth vector field

\[
v : U \rightarrow  {R}^{m}
\]

with an isolated zero at the point \( z{\varepsilon U} \) . The function

\[
\bar{v}\left( x\right)  = v\left( x\right) /\left| \right| v\left( x\right) \left| \right|
\]

maps a small sphere centered at \( z \) into the unit sphere.* The degree of this mapping is called the index \( \iota \) of \( v \) at the zero \( z \) .

Some examples, with indices -1, 0, 1, 2, are illustrated in Figure 12. (Intimately associated with \( v \) are the curves "tangent" to \( v \) which are obtained by solving the differential equations \( \mathrm{d}{x}_{i}/\mathrm{d}t = {v}_{i}\left( {{x}_{1},\cdots ,{x}_{n}}\right) \) . It is these curves which are actually sketched in Figure 12.)

A zero with arbitrary index can be obtained as follows: In the plane of complex numbers the polynomial \( {z}^{k} \) defines a smooth vector field with a zero of index \( k \) at the origin, and the function \( {\bar{z}}^{k} \) defines a vector field with a zero of index \( - \mathrm{k} \) .

We must prove that this concept of index is invariant under diffeomorphism of \( U \) . To explain what this means, let us consider the more general situation of a map \( f : M \rightarrow  N \) , with a vector field on each manifold.

Definition. The vector fields \( v \) on \( M \) and \( {v}^{\prime } \) on \( N \) correspond under \( f \) if the derivative \( d{f}_{x} \) carries \( v\left( x\right) \) into \( {v}^{\prime }\left( {f\left( x\right) }\right) \) for each \( {x\varepsilon M} \) .

---

* Each sphere is to be oriented as the boundary of the corresponding disk.

---

![bo_d7du9valb0pc73deirc0_43_126_253_1207_1259_0.jpg](images/bo_d7du9valb0pc73deirc0_43_126_253_1207_1259_0.jpg)

Figure 12. Examples of plane vector fields

If \( f \) is a diffeomorphism, then clearly \( {v}^{\prime } \) is uniquely determined by \( v \) . The notation

\[
{v}^{\prime } = {df} \circ  v \circ  {f}^{-1}
\]

will be used.

Lemma 1. Suppose that the vector field \( v \) on \( U \) corresponds to

\[
{v}^{\prime } = {df} \circ  v \circ  {f}^{-1}
\]

on \( {U}^{\prime } \) under a diffeomorphism \( f : U \rightarrow  {U}^{\prime } \) . Then the index of \( v \) at an isolated zero \( z \) is equal to the index of \( {v}^{\prime } \) at \( f\left( z\right) \) .

Assuming Lemma 1, we can define the concept of index for a vector field \( w \) on an arbitrary manifold \( M \) as follows: If \( g : U \rightarrow  M \) is a parametrization of a neighborhood of \( z \) in \( M \) , then the index \( \iota \) of \( w \) at \( z \) is defined to be equal to the index of the corresponding vector field \( d{g}^{-1} \circ  w \circ  g \) on \( U \) at the zero \( {g}^{-1}\left( z\right) \) . It clearly will follow from Lemma 1 that \( \iota \) is well defined.

The proof of Lemma 1 will be based on the proof of a quite different result:

Lemma 2. Any orientation preserving diffeomorphism \( f \) of \( {R}^{m} \) is smoothly isotopic to the identity.

(In contrast, for many values of \( m \) there exists an orientation preserving diffeomorphism of the sphere \( {S}^{m} \) which is not smoothly isotopic to the identity. See [20, p. 404].)

Proof. We may assume that \( f\left( 0\right)  = 0 \) . Since the derivative at 0 can be defined by

\[
d{f}_{0}\left( x\right)  = \mathop{\lim }\limits_{{t \rightarrow  0}}f\left( {tx}\right) /t
\]

it is natural to define an isotopy

\[
F : {R}^{m} \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {R}^{m}
\]

by the formula

\[
F\left( {x, t}\right)  = f\left( {tx}\right) /t\;\text{ for }\;0 < t \leq  1,
\]

\[
F\left( {x,0}\right)  = d{f}_{0}\left( x\right) .
\]

To prove that \( F \) is smooth, even as \( t \rightarrow  0 \) , we write \( f \) in the form*

\[
f\left( x\right)  = {x}_{1}{g}_{1}\left( x\right)  + \cdots  + {x}_{m}{g}_{m}\left( x\right) ,
\]

where \( {g}_{1},\cdots ,{g}_{m} \) are suitable smooth functions, and note that

\[
F\left( {x, t}\right)  = {x}_{1}{g}_{1}\left( {tx}\right)  + \cdots  + {x}_{m}{g}_{m}\left( {tx}\right)
\]

for all values of \( t \) .

Thus \( f \) is isotopic to the linear mapping \( d{f}_{0} \) , which is clearly isotopic to the identity. This proves Lemma 2.

Proof of Lemma 1. We may assume that \( z = f\left( z\right)  = 0 \) and that \( U \) is convex. If \( f \) preserves orientation, then, proceeding exactly as above, we construct a one-parameter family of embeddings

\[
{f}_{t} : U \rightarrow  {R}^{m}
\]

---

* See for example [22, p. 5].

---

with \( {f}_{0} = \) identity, \( {f}_{1} = f \) , and \( {f}_{t}\left( 0\right)  = 0 \) for all \( t \) . Let \( {v}_{t} \) denote the vector field \( d{f}_{t} \circ  v \circ  {f}_{t}^{-1} \) on \( {f}_{t}\left( U\right) \) , which corresponds to \( v \) on \( U \) . These vector fields are all defined and nonzero on a sufficiently small sphere centered at 0 . Hence the index of \( v = {v}_{0} \) at0must be equal to the index of \( {v}^{\prime } = {v}_{1} \) at 0 . This proves Lemma 1 for orientation preserving diffeomorphisms.

To consider diffeomorphisms which reverse orientation it is sufficient to consider the special case of a reflection \( \rho \) . Then

\[
{v}^{\prime } = \rho  \circ  v \circ  {\rho }^{-1}
\]

so the associated function \( {\bar{v}}^{\prime }\left( x\right)  = {v}^{\prime }\left( x\right) /\begin{Vmatrix}{{v}^{\prime }\left( x\right) }\end{Vmatrix} \) on the \( \epsilon \) -sphere satisfies

\[
{\bar{v}}^{\prime } = \rho  \circ  \bar{v} \circ  {\rho }^{-1}.
\]

Evidently the degree of \( {\bar{v}}^{\prime } \) equals the degree of \( \bar{v} \) , which completes the proof of Lemma 1.

We will study the following classical result: Let \( M \) be a compact manifold and \( w \) a smooth vector field on \( M \) with isolated zeros. If \( M \) has a boundary, then w is required to point outward at all boundary points.

Poincaré-Hopf Theorem. The sum \( \sum \iota \) of the indices at the zeros of such a vector field is equal to the Euler number*

\[
\chi \left( M\right)  = \mathop{\sum }\limits_{{i = 0}}^{m}{\left( -1\right) }^{i}\text{ rank }{H}_{i}\left( M\right) .
\]

In particular this index sum is a topological invariant of \( M \) : it does not depend on the particular choice of vector field.

(A 2-dimensional version of this theorem was proved by Poincaré in 1885. The full theorem was proved by Hopf [14] in 1926 after earlier partial results by Brouwer and Hadamard.)

We will prove part of this theorem, and sketch a proof of the rest. First consider the special case of a compact domain in \( {R}^{m} \) .

Let \( X \subset  {R}^{m} \) be a compact \( m \) -manifold with boundary. The Gauss mapping

\[
g : \partial X \rightarrow  {S}^{m - 1}
\]

assigns to each \( {x\varepsilon }\partial X \) the outward unit normal vector at \( x \) .

---

* Here \( {H}_{i}\left( M\right) \) denotes the \( i \) -th homology group of \( M \) . This will be our first and last reference to homology theory.

---

Lemma 3 (Hopf). If \( v : X \rightarrow  {R}^{m} \) is a smooth vector field with isolated zeros, and if \( v \) points out of \( X \) along the boundary, then the index sum \( \sum \iota \) is equal to the degree of the Gauss mapping from \( \partial X \) to \( {S}^{m - 1} \) . In particular, \( \sum \iota \) does not depend on the choice of \( v \) .

For example, if a vector field on the disk \( {D}^{m} \) points outward along the boundary, then \( \sum \iota  =  + 1 \) . (Compare Figure 13.)

![bo_d7du9valb0pc73deirc0_46_444_659_475_473_0.jpg](images/bo_d7du9valb0pc73deirc0_46_444_659_475_473_0.jpg)

Figure 13. An example with index sum +1

Proof. Removing an \( \epsilon \) -ball around each zero, we obtain a new manifold with boundary. The function \( \bar{v}\left( x\right)  = v\left( x\right) /\parallel v\left( x\right) \parallel \) maps this manifold into \( {S}^{m - 1} \) . Hence the sum of the degrees of \( \bar{v} \) restricted to the various boundary components is zero. But \( \bar{v} \mid  \partial X \) is homotopic to \( g \) , and the degrees on the other boundary components add up to \( - \sum \iota \) . (The minus sign occurs since each small sphere gets the wrong orientation.) Therefore

\[
\deg \left( g\right)  - \sum \iota  = 0
\]

as required.

REMARK. The degree of \( g \) is also known as the "curvatura integra" of \( \partial X \) , since it can be expressed as a constant times the integral over \( \partial X \) of the Gaussian curvature. This integer is of course equal to the Euler number of \( X \) . For \( m \) odd it is equal to half the Euler number of \( \partial X \) .

Before extending this result to other manifolds, some more preliminaries are needed.

It is natural to try to compute the index of a vector field \( v \) at a zero \( z \) in terms of the derivatives of \( v \) at \( z \) . Consider first a vector field \( v \) on an open set \( U \subset  {R}^{m} \) and think of \( v \) as a mapping \( U \rightarrow  {R}^{m} \) , so that \( d{v}_{z} : {R}^{m} \rightarrow  {R}^{m} \) is defined.

DEFINITION. The vector field \( v \) is nondegenerate at \( z \) if the linear transformation \( d{v}_{z} \) is nonsingular.

It follows that \( z \) is an isolated zero.

Lemma 4. The index of \( v \) at a nondegenerate zero \( z \) is either \( + 1 \) or -1 according as the determinant of \( d{v}_{z} \) is positive or negative.

Proof. Think of \( v \) as a diffeomorphism from some convex neighborhood \( {U}_{0} \) of \( z \) into \( {R}^{m} \) . We may assume that \( z = 0 \) . If \( v \) preserves orientation, we have seen that \( v \mid  {U}_{0} \) can be deformed smoothly into the identity without introducing any new zeros. (See Lemmas 1, 2.) Hence the index is certainly equal to +1 .

If \( v \) reverses orientation, then similarly \( v \) can be deformed into a reflection; hence \( \iota  =  - 1 \) .

More generally consider a zero \( z \) of a vector field \( w \) on a manifold \( M \subset  {R}^{k} \) . Think of \( w \) as a map from \( M \) to \( {R}^{k} \) so that the derivative \( d{w}_{z} : T{M}_{z} \rightarrow  {R}^{k} \) is defined.

Lemma 5. The derivative \( d{w}_{z} \) actually carries \( T{M}_{z} \) into the subspace \( T{M}_{z} \subset  {R}^{k} \) , and hence can be considered as a linear transformation from \( T{M}_{z} \) to itself. If this linear transformation has determinant \( D \neq  0 \) then \( z \) is an isolated zero of \( w \) with index equal to +1 or -1 according as \( D \) is positive or negative.

Proof. Let \( h : U \rightarrow  M \) be a parametrization of some neighborhood of \( z \) . Let \( {e}^{i} \) denote the \( i \) -th basis vector of \( {R}^{m} \) and let

\[
{t}^{i} = d{h}_{u}\left( {e}^{i}\right)  = \partial h/\partial {u}_{i}
\]

so that the vectors \( {t}^{1},\cdots ,{t}^{m} \) form a basis for the tangent space \( T{M}_{h\left( u\right) } \) . We must compute the image of \( {t}^{i} = {t}^{i}\left( u\right) \) under the linear transformation \( d{w}_{h\left( u\right) } \) . First note that

1)

\[
d{w}_{h\left( u\right) }\left( {t}^{i}\right)  = d{\left( w \circ  h\right) }_{u}\left( {e}^{i}\right)  = \partial w\left( {h\left( u\right) }\right) /\partial {u}_{i}.
\]

Let \( v = \sum {v}_{j}{e}^{j} \) be the vector field on \( U \) which corresponds to the vector field \( w \) on \( M \) . By definition \( v = d{h}^{-1} \circ  w \circ  h \) , so that

\[
w\left( {h\left( u\right) }\right)  = d{h}_{u}\left( v\right)  = \sum {v}_{i}{t}^{i}.
\]

Therefore

2)

\[
\partial w\left( {h\left( u\right) }\right) /\partial {u}_{i} = \mathop{\sum }\limits_{i}\left( {\partial {v}_{i}/\partial {u}_{i}}\right) {t}^{i} + \mathop{\sum }\limits_{i}{v}_{i}\left( {\partial {t}^{i}/\partial {u}_{i}}\right) .
\]

Combining 1) and 2), and then evaluating at the zero \( {h}^{-1}\left( z\right) \) of \( v \) , we obtain the formula

3)

\[
d{w}_{z}\left( {t}^{i}\right)  = \mathop{\sum }\limits_{i}\left( {\partial {v}_{j}/\partial {u}_{i}}\right) {t}^{i}.
\]

Thus \( d{w}_{z} \) maps \( T{M}_{z} \) into itself, and the determinant \( D \) of this linear transformation \( T{M}_{z} \rightarrow  T{M}_{z} \) is equal to the determinant of the matrix \( \left( {\partial {v}_{j}/\partial {u}_{i}}\right) \) . Together with Lemma 4 this completes the proof.

Now consider a compact, boundaryless manifold \( M \subset  {R}^{k} \) . Let \( {N}_{\epsilon } \) denote the closed \( \epsilon \) -neighborhood of \( M \) (i.e., the set of all \( {x\varepsilon }{R}^{k} \) with \( \parallel x - y\parallel  \leq  \epsilon \) for some \( {y\varepsilon M} \) ). For \( \epsilon \) sufficiently small one can show that \( {N}_{\epsilon } \) is a smooth manifold with boundary. (See §8, Problem 11.)

Theorem 1. For any vector field \( v \) on \( M \) with only nondegenerate zeros, the index sum \( \sum \iota \) is equal to the degree of the Gauss mapping*

\[
g : \partial {N}_{\epsilon } \rightarrow  {S}^{k - 1}
\]

In particular this sum does not depend on the choice of vector field.

Proof. For \( {x\varepsilon }{N}_{\epsilon }\operatorname{let}r\left( x\right) {\varepsilon M} \) denote the closest point of \( M \) . (Compare \( \text{ § }8 \) , Problem 12.) Note that the vector \( x - r\left( x\right) \) is perpendicular to the tangent space of \( M \) at \( r\left( x\right) \) , for otherwise \( r\left( x\right) \) would not be the closest point of \( M \) . If \( \epsilon \) is sufficiently small, then the function \( r\left( x\right) \) is smooth and well defined.

![bo_d7du9valb0pc73deirc0_48_384_1439_540_427_0.jpg](images/bo_d7du9valb0pc73deirc0_48_384_1439_540_427_0.jpg)

Figure 14. The \( \epsilon \) -neighborhood of \( M \)

---

* A different interpretation of this degree has been given by Allendoerfer and Fenchel: the degree of \( g \) can be expressed as the integral over \( M \) of a suitable curvature scalar, thus yielding an \( m \) -dimensional version of the classical Gauss-Bonnet theorem. (References [1], [9]. See also Chern [6].)

---

We will also consider the squared distance function

\[
\varphi \left( x\right)  = \parallel x - r\left( x\right) {\parallel }^{2}.
\]

An easy computation shows that the gradient of \( \varphi \) is given by

\[
\operatorname{grad}\varphi  = 2\left( {x - r\left( x\right) }\right) .
\]

Hence, for each point \( x \) of the level surface \( \partial {N}_{\epsilon } = {\varphi }^{-1}\left( {\epsilon }^{2}\right) \) , the outward unit normal vector is given by

\[
g\left( x\right)  = \operatorname{grad}\varphi /\left| \right| \operatorname{grad}\varphi \left| \right|  = \left( {x - r\left( x\right) }\right) /\epsilon .
\]

Extend \( v \) to a vector field \( w \) on the neighborhood \( {N}_{\epsilon } \) by setting

\[
w\left( x\right)  = \left( {x - r\left( x\right) }\right)  + v\left( {r\left( x\right) }\right) .
\]

Then \( w \) points outward along the boundary, since the inner product \( w\left( x\right)  \cdot  g\left( x\right) \) is equal to \( \epsilon  > 0 \) . Note that \( w \) can vanish only at the zeros of \( v \) in \( M \) ; this is clear since the two summands \( \left( {x - r\left( x\right) }\right) \) and \( v\left( {r\left( x\right) }\right) \) are mutually orthogonal. Computing the derivative of \( w \) at a zero \( {z\varepsilon M} \) , we see that

\[
d{w}_{z}\left( h\right)  = d{v}_{z}\left( h\right) \;\text{ for all }\;{h\varepsilon T}{M}_{z}
\]

\[
d{w}_{z}\left( h\right)  = h\;\text{ for }{h\varepsilon T}{M}_{z}^{ \bot  }.
\]

Thus the determinant of \( d{w}_{z} \) is equal to the determinant of \( d{v}_{z} \) . Hence the index of \( w \) at the zero \( z \) is equal to the index \( \iota \) of \( v \) at \( z \) .

Now according to Lemma 3 the index sum \( \sum \iota \) is equal to the degree of \( g \) . This proves Theorem 1.

EXAMPLES. On the sphere \( {S}^{m} \) there exists a vector field \( v \) which points "north" at every point.* At the south pole the vectors radiate outward; hence the index is +1 . At the north pole the vectors converge inward; hence the index is \( {\left( -1\right) }^{m} \) . Thus the invariant \( \sum \iota \) is equal to 0 or 2 according as \( m \) is odd or even. This gives a new proof that every vector field on an even sphere has a zero.

For any odd-dimensional, boundaryless manifold the invariant \( \sum \iota \) is zero. For if the vector field \( v \) is replaced by \( - v \) , then each index is multiplied by \( {\left( -1\right) }^{m} \) , and the equality

\[
\sum \iota  = {\left( -1\right) }^{m}\sum \iota
\]

for \( m \) odd, implies that \( \sum \iota  = 0 \) .

---

* For example, \( v \) can be defined by the formula \( v\left( x\right)  = p - \left( {p \cdot  x}\right) x \) , where \( p \) is the north pole. (See Figure 11.)

---

REMARK. If \( \sum \iota  = 0 \) on a connected manifold \( M \) , then a theorem of Hopf asserts that there exists a vector field on \( M \) with no zeros at all.

In order to obtain the full strength of the Poincaré-Hopf theorem, three further steps are needed.

STEP 1. Identification of the invariant \( \sum \iota \) with the Euler number \( \chi \left( M\right) \) . It is sufficient to construct just one example of a nondegenerate vector field on \( M \) with \( \sum \iota \) equal to \( \chi \left( M\right) \) . The most pleasant way of doing this is the following: According to Marston Morse, it is always possible to find a real valued function on \( M \) whose "gradient" is a nondegenerate vector field. Furthermore, Morse showed that the sum of indices associated with such a gradient field is equal to the Euler number of \( M \) . For details of this argument the reader is referred to Milnor [22, pp. 29, 36].

STEP 2. Proving the theorem for a vector field with degenerate zeros. Consider first a vector field \( v \) on an open set \( U \) with an isolated zero at \( z \) . If

\[
\lambda  : U \rightarrow  \left\lbrack  {0,1}\right\rbrack
\]

takes the value 1 on a small neighborhood \( {N}_{1} \) of \( z \) and the value 0 outside a slightly larger neighborhood \( N \) , and if \( y \) is a sufficiently small regular value of \( v \) , then the vector field

\[
{v}^{\prime }\left( x\right)  = v\left( x\right)  - \lambda \left( x\right) y
\]

is nondegenerate* within \( N \) . The sum of the indices at the zeros within \( N \) can be evaluated as the degree of the map

\[
\bar{v} : \partial N \rightarrow  {S}^{m - 1}
\]

and hence does not change during this alteration.

More generally consider vector fields on a compact manifold \( M \) . Applying this argument locally we see that any vector field with isolated zeros can be replaced by a nondegenerate vector field without altering the integer \( \sum \iota \) .

STEP 3. Manifolds with boundary. If \( M \subset  {R}^{k} \) has a boundary, then any vector field \( v \) which points outward along \( \partial M \) can again be extended over the neighborhood \( {N}_{\epsilon } \) so as to point outward along \( \partial {N}_{\epsilon } \) . However, there is some difficulty with smoothness around the boundary of \( M \) . Thus \( {N}_{\epsilon } \) is not a smooth (i.e. differentiable of class \( {C}^{\infty } \) ) manifold, but only a \( {C}^{1} \) -manifold. The extension \( w \) , if defined as before by \( w\left( x\right)  = v\left( {r\left( x\right) }\right)  + x - r\left( x\right) \) , will only be a continuous vector field near \( \partial M \) . The argument can nonetheless be carried out either by showing that our strong differentiability assumptions are not really necessary or by other methods.

---

* Clearly \( {v}^{\prime } \) is nondegenerate within \( {N}_{1} \) . But if \( y \) is sufficiently small, then \( {v}^{\prime } \) will have no zeros at all within \( N - {N}_{1} \) .

---
