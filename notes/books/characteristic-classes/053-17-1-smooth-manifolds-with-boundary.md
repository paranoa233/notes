# 17.1 Smooth Manifolds-with-Boundary

Let us first give a precise definition of this concept, which has already been used briefly in \( \text{ § }4 \) and \( \text{ § }{16} \) . As a universal model for manifolds-with-boundary, we take the closed half-space \( {\mathbb{H}}^{n} \) , consisting of all points \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) in the Euclidean space \( {\mathbb{R}}^{n} \) with \( {x}_{1} \geq  0 \) . A subset \( X \subset  {\mathbb{R}}^{A} \) is called a smooth \( n - \) dimensional manifold-with-boundary if, for each point \( x \in  X \) , there exists a smooth mapping

\[
h : U \rightarrow  {\mathbb{R}}^{A}
\]

which maps some relatively open set \( U \subset  {\mathbb{H}}^{n} \) homeomorphically onto a neighborhood of \( x \) in \( X \) , and for which the matrix of first derivatives \( \left\lbrack  {\partial {h}_{\alpha }/\partial {u}_{j}}\right\rbrack \) has rank \( n \) everywhere. (Compare page 14.)

A point \( x \) of \( X \) is called an interior point if there exists a local parameterization \( h : U \rightarrow  {\mathbb{R}}^{A} \) of \( X \) about \( x \) such that \( U \) is an open subset of \( {\mathbb{R}}^{n} \) (rather than \( {\mathbb{H}}^{n} \) ). Evidently the set of interior points forms a smooth \( n \) -dimensional manifold which is open as a subset of \( X \) . The non-interior points form a smooth \( \left( {n - 1}\right) \) -dimensional manifold, called the boundary \( \partial X \) , which is closed as a subset of \( X \) .

The tangent bundle \( {\tau }^{n} \) of a smooth manifold-with-boundary \( X \) is a smooth \( n \) -plane bundle over \( X \) . The definition is completely analogous to that of \( \text{ § }1 \) . This \( n \) -plane bundle has some additional structure that can be described as follows. If \( x \) is a boundary point of \( X \) , then the fibre \( {\mathbf{T}}_{x}X \) contains an \( \left( {n - 1}\right) \) -dimensional subspace \( {\mathbf{T}}_{x}\left( {\partial X}\right) \) consisting of vectors which are tangent to the boundary. This hyperplane \( {\mathbf{T}}_{x}\left( {\partial X}\right) \) separates the tangent space \( {\mathbf{T}}_{x}X \) into two open subsets, consisting respectively of vectors which point "into" or "out of" \( X \) . By definition a vector \( v \in  {\mathbf{T}}_{x}X \) with \( v \notin  {\mathbf{T}}_{x}\left( {\partial X}\right) \) , points into \( X \) if \( v \) is the velocity vector \( {\left( \mathrm{d}p/\mathrm{d}t\right) }_{t = 0} \) of a smooth path

\[
p : \lbrack 0,\epsilon ) \rightarrow  X
\]

with \( p\left( 0\right)  = x \) . Similarly \( v \) points out of \( X \) if \( v \) is the velocity vector at \( t = 0 \) of a path \( p : ( - \epsilon ,0\rbrack  \rightarrow  X \) with \( p\left( 0\right)  = x \) .

Now suppose that the tangent bundle \( {\tau }^{n} \) of \( X \) is an oriented \( n \) -plane bundle. Then the tangent bundle \( {\tau }^{n - 1} \) of \( \partial X \) has an induced orientation as follows. Choose an oriented basis \( {v}_{1},\ldots ,{v}_{n} \) for \( {\mathbf{T}}_{x}X \) at any boundary point \( x \) so that \( {v}_{1} \) points out of \( X \) and \( {v}_{2},\ldots ,{v}_{n} \) are tangent to \( \partial X \) . Then the ordered basis \( {v}_{2},\ldots ,{v}_{n} \) determines the required orientation for \( {\mathbf{T}}_{x}\left( {\partial X}\right) \) .

[In the special case of a 1-dimensional manifold-with-boundary, this construction must be modified as follows. An "orientation" of a point \( x \) of the \( 0 - \) dimensional manifold \( \partial X \) is just a choice of sign +1 or -1 . In fact we assign \( x \) the orientation +1 or -1 according as the positive direction in \( {\mathbf{T}}_{x}X \) points out of or into \( X \) .]

We will need the following statement.

Theorem 17.1 (Collar Neighborhood Theorem). If \( X \) is a smooth paracompact manifold-with-boundary, then there exists an open neighborhood of \( \partial X \) in \( X \) which is diffeomorphic to the product \( \partial X \times  \lbrack 0,1) \) .

Proof. The proof is similar to that of Theorem 11.1. (Just as for 11.1, we will actually need this assertion only in the special case where \( \partial X \) is compact.) Details will be left to the reader.
