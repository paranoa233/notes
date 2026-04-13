# Chapter 6 Manifolds in Euclidean Space

Based on lecture notes by

M. Spivak and R. Wells

Although we have so far considered, on a manifold, only functions which have no degenerate critical points, we have not yet even shown that such functions always exist. In this section we will construct many functions with no degenerate critical points, on any manifold embedded in \( {\mathbf{R}}^{n} \) . In fact, if for fixed \( p \in  {\mathbf{R}}^{n} \) define the function \( {L}_{p} : M \rightarrow  \mathbf{R} \) by \( {L}_{p}\left( q\right)  = \parallel p - q{\parallel }^{2} \) . It will turn out that for almost all \( p \) , the function \( {L}_{p} \) has only non-degenerate critical points.

Let \( M \subset  {\mathbf{R}}^{n} \) be a manifold of dimension \( k < n \) , differentiably embedded in \( {\mathbf{R}}^{n} \) . Let \( N \subset  M \times  {\mathbf{R}}^{n} \) be defined by

\[
N = \{ \left( {q, v}\right)  : q \in  M, v\text{ perpendicular to }M\text{ at }q\} .
\]

It is not difficult to show that \( N \) is an \( n \) -dimensional manifold differentiably embedded in \( {\mathbf{R}}^{2n} \) . ( \( N \) is the total space of the normal vector bundle of \( M \) .)

Let \( E : N \rightarrow  {\mathbf{R}}^{n} \) be \( E\left( {q, v}\right)  = q + v \) . ( \( E \) is the "endpoint" map.)

![bo_d7du90alb0pc73deir8g_38_614_1365_411_409_0.jpg](images/bo_d7du90alb0pc73deir8g_38_614_1365_411_409_0.jpg)

Definition 6.1. \( \mathrm{e} \in  {\mathbf{R}}^{n} \) is a focal point of \( \left( {M, q}\right) \) with multiplicity \( \mu \) if \( e = q + v \) where \( \left( {q, v}\right)  \in  N \) and the Jacobian of \( E \) at \( \left( {q, v}\right) \) has nullity \( \mu  > 0 \) . The point \( \mathrm{e} \) will be called a focal point of \( M \) if \( \mathrm{e} \) is a focal point of \( \left( {M, q}\right) \) for some \( q \in  M \) .

Intuitively, a focal point of \( M \) is a point in \( {\mathbf{R}}^{n} \) where nearby normals intersect. We will use the following theorem, which we will not prove.

Theorem 6.2 (Sard). If \( {M}_{1} \) and \( {M}_{2} \) are differentiable manifolds having a countable basis, of the same dimension, and \( f : {M}_{1} \rightarrow  {M}_{2} \) is of class \( {C}^{1} \) , then the image of the set of critical points has measure 0 in \( {M}^{2} \) .

A critical point of \( f \) is a point where the Jacobian of \( f \) is singular. For a proof see [DR84, p. 10].

Corollary 6.3. For almost all \( x \in  {\mathbf{R}}^{n} \) , the point \( x \) is not a focal point of \( M \) .

Proof. We have just seen that \( N \) is an \( n \) -manifold. The point \( x \) is a focal point iff \( x \) is in the image of the set of critical points of \( E : N \rightarrow  {\mathbf{R}}^{n} \) . Therefore the set of focal points has measure 0 .

For a better understanding of the concept of focal point, it is convenient to introduce the "second fundamental form" of a manifold in Euclidean space. We will not attempt to give an invariant definition; but will make use of a fixed local coordinate system.

Let \( {u}^{1},\ldots ,{u}^{k} \) be coordinates for a region of the manifold \( M \subset  {\mathbf{R}}^{n} \) . Then the inclusion map from \( M \) to \( {\mathbf{R}}^{n} \) determines \( n \) smooth functions

\[
{x}_{1}\left( {{u}^{1},\ldots ,{u}^{k}}\right) ,\ldots ,{x}_{n}\left( {{u}^{1},\ldots ,{u}^{k}}\right) .
\]

These functions will be written briefly as \( \overrightarrow{x}\left( {{u}^{1},\ldots ,{u}^{k}}\right) \) where \( \overrightarrow{x} = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) . To be consistent the point \( q \in  M \subset  {\mathbf{R}}^{n} \) will now be denoted by \( \overrightarrow{q} \) .

The first fundamental form associated with the coordinate system is defined to be the symmetric matrix of real valued functions

\[
\left( {g}_{ij}\right)  = \left( {\frac{\partial \overrightarrow{x}}{\partial {u}_{i}} \cdot  \frac{\partial \overrightarrow{x}}{\partial {u}_{j}}}\right) .
\]

The second fundamental form on the other hand, is a symmetric matrix \( \left( {\overrightarrow{\ell }}_{ij}\right) \) of vector valued functions.

It is defined as follows. The vector \( \frac{{\partial }^{2}\overrightarrow{x}}{\partial {u}^{i}\partial {u}^{j}} \) at a point of \( M \) can be expressed as the sum of a vector tangent to \( M \) and a vector normal to \( M \) . Define \( {\overrightarrow{\ell }}_{ij} \) to be the normal component of \( \frac{{\partial }^{2}\overrightarrow{x}}{\partial {u}^{i}\partial {u}^{j}} \) . Given any unit vector \( \overrightarrow{v} \) which is normal to \( M \) at \( q \) the matrix

\[
\left( {\overrightarrow{v} \cdot  \frac{{\partial }^{2}\overrightarrow{x}}{\partial {u}^{i}\partial {u}^{j}}}\right)  = \left( {\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right)
\]

can be called the second fundamental form of \( M \) at \( q \) in the direction \( \overrightarrow{v} \) .

It will simplify the discussion to assume that the coordinates have been chosen to that \( {g}_{ij} \) , evaluated at \( \overrightarrow{q} \) , is the identity matrix. Then the eigenvalues of the matrix \( \left( {\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right) \) are called the principal curvatures \( {K}_{1},\ldots ,{K}_{K} \) of \( M \) at \( \overrightarrow{q} \) in the normal direction \( \overrightarrow{v} \) . The reciprocals \( {K}_{1}^{-1},\ldots ,{K}_{K}^{-1} \) of these principal curvatures are called the principal radii of curvature. Of course it may happen that the matrix \( \left( {\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right) \) is singular. In this case one or more of the \( {K}_{i} \) will be zero; and hence the corresponding radii \( {K}_{i}^{-1} \) will not be defined.

Now consider the normal line \( \ell \) consisting of all \( \overrightarrow{q} + t\overrightarrow{v} \) , where \( \overrightarrow{v} \) is a fixed unit vector orthogonal to \( M \) at \( q \) .

Lemma 6.4. The focal points of \( \left( {M\overrightarrow{q}}\right) \) along \( \ell \) are precisely the points \( \overrightarrow{q} + {K}_{i}^{-1}\overrightarrow{v} \) , where \( 1 \leq  i \leq  k,{K}_{i} \neq  0 \) . Thus there are at most, \( k \) focal points of \( \left( {M,\overrightarrow{q}}\right) \) along \( \ell \) , each being counted with its proper multiplicity.

Proof. Choose \( n - k \) vector fields \( {\overrightarrow{w}}_{1}\left( {{u}^{1},\ldots ,{u}^{k}}\right) ,\ldots ,{\overrightarrow{w}}_{n - k}\left( {{u}^{1},\ldots ,{u}^{k}}\right) \) along the manifold so that \( {\overrightarrow{w}}_{1},\ldots ,{\overrightarrow{w}}_{n - k} \) are unit vectors which are orthogonal to each other and to M. We can introduce coordinates \( \left( {{u}^{1},\ldots ,{u}^{k},{t}^{1},\ldots ,{t}^{n - k}}\right) \) on the manifold \( N \subset  M \times  {\mathbf{R}}^{n} \) as follows. Let \( \left( {{u}^{1},\ldots ,{u}^{k},{t}^{1},\ldots ,{t}^{n - k}}\right) \) correspond to the point

\[
\left( {\overrightarrow{x}\left( {{u}^{1},\ldots ,{u}^{k}}\right) ,\mathop{\sum }\limits_{{\alpha  = 1}}^{{n - k}}{t}^{\alpha }{\overrightarrow{w}}_{\alpha }\left( {{u}^{1},\ldots ,{u}^{k}}\right) }\right)  \in  N.
\]

Then the function \( E : N \rightarrow  {\mathbf{R}}^{n} \) gives rise to the correspondence

\[
\left( {{u}^{1},\ldots ,{u}^{k},{t}^{1},\ldots ,{t}^{n - k}}\right) \overset{\overrightarrow{e}}{ \mapsto  }\overrightarrow{x}\left( {{u}^{1},\ldots ,{u}^{k}}\right)  + \mathop{\sum }\limits_{{\alpha  = 1}}^{{n - k}}{t}^{\alpha }{\overrightarrow{w}}_{\alpha }\left( {{u}^{1},\ldots ,{u}^{k}}\right) ,
\]

with partial derivatives

\[
\left\{  \begin{array}{l} \frac{\partial \overrightarrow{\mathrm{e}}}{\partial {u}^{i}} = \frac{\partial \overrightarrow{x}}{\partial {u}^{i}} + \mathop{\sum }\limits_{\alpha }{t}^{\alpha }\frac{\partial {\overrightarrow{w}}_{\alpha }}{\partial {u}^{i}} \\  \frac{\partial \overrightarrow{\mathrm{e}}}{\partial {t}^{\beta }} = {\overrightarrow{w}}_{\beta }. \end{array}\right.
\]

Taking the inner products of these n-vectors with the linearly independent vectors \( \partial \overrightarrow{x}/\partial {u}^{1},\ldots ,\partial \overrightarrow{x}/\partial {u}^{k},{\overrightarrow{w}}_{1},\ldots ,{\overrightarrow{x}}_{n - k} \) will obtain an \( n \times  n \) matrix whose rank equals the rank of the Jacobian of \( E \) at the corresponding point.

This \( n \times  n \) matrix clearly has the following form

\[
\left( \begin{matrix} \left( {\frac{\partial \overrightarrow{x}}{\partial {u}_{i}} \cdot  \frac{\partial \overrightarrow{x}}{\partial {u}_{j}}}\right) & \left( {\mathop{\sum }\limits_{\alpha }{t}^{\alpha }\frac{\partial {\overrightarrow{w}}_{\alpha }}{\partial {u}^{i}} \cdot  {\overrightarrow{w}}_{\beta }}\right) \\   \text{ ○ } & \text{ identity matrix } \end{matrix}\right)
\]

Thus the nullity is equal to the nullity of the upper left hand block. Using the identity

\[
0 = \frac{\partial }{\partial {u}^{i}}\left( {{\overrightarrow{w}}_{\alpha } \cdot  \frac{\partial \overrightarrow{x}}{\partial {u}_{j}}}\right)  = \frac{\partial {\overrightarrow{w}}_{\alpha }}{\partial {u}_{i}} \cdot  \frac{\partial \overrightarrow{x}}{\partial {u}_{j}} + {\overrightarrow{w}}_{\alpha } \cdot  \frac{{\partial }^{2}\overrightarrow{x}}{\partial {u}_{i}\partial {u}_{j}}
\]

we see that this upper left hand block is just the matrix

\[
\left( {{g}_{ij} - \mathop{\sum }\limits_{\alpha }{t}^{\alpha }{\overrightarrow{w}}_{\alpha } \cdot  {\overrightarrow{\ell }}_{ij}}\right)
\]

Thus:

Assertion 6.1. \( \overrightarrow{q} + t\overrightarrow{v} \) is a focal point of \( \left( {M, q}\right) \) with multiplicity \( \mu \) if and only if the matrix

\[
\left( {{g}_{ij} - t\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right)
\]

\( \left( \star \right) \)

is singular, with nullity \( \mu \) .

Now suppose that \( \left( {g}_{ij}\right) \) is the identity matrix. Then \( \left( \star \right) \) is singular if and only if \( 1/t \) is an eigenvalue of the matrix \( \left( {\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right) \) . Furthermore the multiplicity \( \mu \) is equal to the multiplicity of \( 1/t \) as eigenvalue. This completes the proof of Lemma 6.4.

Now for fixed \( p \in  {\mathbf{R}}^{n} \) let us study the function

\[
{L}_{\overrightarrow{p}} = f : M \rightarrow  \mathbf{R}
\]

where

\[
f\left( {\overrightarrow{x}\left( {{u}^{1},\ldots ,{u}^{k}}\right) }\right)  = \parallel \overrightarrow{x}\left( {{u}^{1},\ldots ,{u}^{k}}\right)  - \overrightarrow{p}{\parallel }^{2} = \overrightarrow{x} \cdot  \overrightarrow{x} - 2\overrightarrow{x} \cdot  \overrightarrow{p} + \overrightarrow{p} \cdot  \overrightarrow{x}.
\]

We have

\[
\frac{\partial f}{\partial {u}^{i}} = 2\frac{\partial \overrightarrow{x}}{\partial {u}^{i}} \cdot  \left( {\overrightarrow{x} - \overrightarrow{p}}\right) .
\]

Thus \( f \) has a critical point at \( \overrightarrow{q} \) if and only if \( \overrightarrow{q} - \overrightarrow{p} \) is normal to \( M \) at \( \overrightarrow{q} \) .

The second partial derivatives at a critical point are given by

\[
\frac{{\partial }^{2}f}{\partial {u}^{i}\partial {u}^{j}} = 2\frac{\partial \overrightarrow{x}}{\partial {u}^{i}} \cdot  \frac{\partial \overrightarrow{x}}{\partial {u}^{j}} + \frac{\partial \overrightarrow{x}}{\partial {u}^{i}}{u}^{j} \cdot  \left( {\overrightarrow{x} - \overrightarrow{p}}\right) .
\]

Setting \( \overrightarrow{p} = \overrightarrow{x} + t\overrightarrow{v} \) , as in the proof of Lemma 6.4, this becomes

\[
\frac{{\partial }^{2}f}{\partial {u}^{i}\partial {u}^{j}} = 2\left( {{g}_{ij} - t\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right) .
\]

Therefore:

Lemma 6.5. The point \( \overrightarrow{q} \in  M \) is a degenerate critical point of \( f = {L}_{\overrightarrow{p}} \) if and only if \( \overrightarrow{p} \) is a focal point of \( \left( {M,\overrightarrow{p}}\right) \) . The nullity of \( \overrightarrow{q} \) as critical point is equal to the multiplicity of \( \overrightarrow{p} \) as focal point.

Combining this result with Corollary 6.3 to Sard's theorem, we immediately obtain:

Theorem 6.6. For almost all \( p \in  {\mathbf{R}}^{n} \) (all but a set of measure 0 ) the function

\[
{L}_{p} : M \rightarrow  \mathbf{R}
\]

has no degenerate critical points.

This theorem has several interesting consequences.

Corollary 6.7. On any manifold \( M \) there exists a differentiable function, with no degenerate critical points, for which each \( {M}^{a} \) is compact.

Proof. This follows from Theorem 6.6 and the fact that an \( n \) -dimensional manifold \( M \) can be embedded differentiably as a closed subset of \( {\mathbf{R}}^{{2n} + 1} \) (see [Whi05, p. 113]).

Application 6.1. A differentiable manifold has the homotopy type of a CW-complex. This follows from the above corollary and Theorem 3.3.

Application 6.2. On a compact manifold \( M \) there is a vector field \( X \) such that the sum of the indices of the critical points of \( X \) equals \( \chi \left( M\right) \) , the Euler characteristic of \( M \) . This can be seen as follows: for any differentiable function \( f \) on \( M \) we have \( \chi \left( M\right)  = \sum {\left( -1\right) }^{\lambda }{C}_{\lambda } \) where \( {C}_{\lambda } \) is the number of critical points with index \( \lambda \) . But \( {\left( -1\right) }^{\lambda } \) is the index of the vector field \( \operatorname{grad}f \) at a point where \( f \) has index \( \lambda \) .

It follows that the sum of the indices of any vector field on \( M \) is equal to \( \chi \left( M\right) \) because this sum is a topological invariant (see [Ste51, §39.7]).

The preceding corollary can be sharpened as follows. Let \( k \geq  0 \) be an integer and let \( K \subset  M \) be a compact set.

Corollary 6.8. Any bounded smooth function \( f : M \rightarrow  \mathbf{R} \) can be uniformly approximated by a smooth function \( g \) which has no degenerate critical points. Furthermore \( g \) can be chosen so that the \( i \) -th derivatives of \( g \) on the compact set \( K \) uniformly approximate the corresponding derivatives of \( f \) , for \( i \leq  k \) .

(Compare [Mor31].)

Proof. Choose some imbedding \( h : M \rightarrow  {\mathbf{R}}^{n} \) of \( M \) as a bounded subset of some euclidean space so that the first coordinate \( {h}_{1} \) is precisely the given function \( f \) . Let \( c \) be a large number. Choose a point

\[
p = \left( {-c + {\varepsilon }_{1},{\varepsilon }_{2},\ldots ,{\varepsilon }_{n}}\right)
\]

close to \( \left( {-c,0,\ldots ,0}\right)  \in  {\mathbf{R}}^{n} \) so that the function \( {L}_{P} : M \rightarrow  \mathbf{R} \) is non-degenerate; and set

\[
g\left( x\right)  = \frac{{L}_{p}\left( x\right)  - {c}^{2}}{2c}.
\]

Clearly \( g \) is non-degenerate. A short computation shows that

\[
g\left( x\right)  = f\left( x\right)  + \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{h}_{i}{\left( x\right) }^{2}}{2c} - \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{\varepsilon }_{i}{h}_{i}\left( x\right) }{c} + \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{\varepsilon }_{i}^{2}}{2c} - {\varepsilon }_{1}.
\]

Clearly, if \( c \) is large and the \( {\varepsilon }_{i} \) are small, then \( g \) will approximate \( f \) as required.

The above theory can also be used to describe the index of the function

\[
{L}_{p} : M \rightarrow  \mathbf{R}
\]

at a critical point.

Lemma 6.9 (Index Theorem for \( {L}_{p} \) ). The index of \( {L}_{p} \) at a non-degenerate critical point \( q \in  M \) is equal to the number of focal points of \( \left( {M, q}\right) \) which lie on the segment from \( q \) to \( p \) ; each focal point being counted with its multiplicity.

An analogous statement in part III (the Morse Index Theorem) will be of fundamental importance.

Proof. The index of the matrix

\[
\left( \frac{{\partial }^{2}{L}_{p}}{\partial {u}^{i}\partial {u}^{j}}\right)  = 2\left( {{g}_{ij} - t\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right)
\]

is equal to the number of negative eigenvalues. Assuming that \( \left( {g}_{ij}\right) \) is the identity matrix, this is equal to the number of eigenvalues of \( \left( {\overrightarrow{v} \cdot  {\overrightarrow{\ell }}_{ij}}\right) \) which are \( \geq  \frac{1}{2} \) . Comparing this statement with Lemma 6.4, the conclusion follows.
