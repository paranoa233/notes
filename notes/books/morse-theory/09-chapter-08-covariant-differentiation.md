# Chapter 8 Covariant Differentiation

## Part II. A Rapid Course in Riemannian Geometry

Based on lecture notes by

M. Spivak and R. Wells

The object of Part II will be to give a rapid outline of some basic concepts of Riemannian geometry which will be needed later. For more information the reader should consult [Nom56, Hel62, Ste64] or [Lau65].

Let \( M \) be a smooth manifold.

Definition 8.1. An affine connection at a point \( p \in  M \) is a function which assigns to each tangent vector \( {X}_{p} \in  T{M}_{p} \) and to each vector field \( Y \) a new tangent vector

\[
{X}_{p} \vdash  Y \in  T{M}_{p}
\]

called the covariant derivative \( {}^{1} \) of \( Y \) in the direction \( {X}_{p} \) . This is required to be bilinear as a function of \( {X}_{p} \) and \( Y \) . Furthermore, if

\[
f : M \rightarrow  \mathbf{R}
\]

is a real valued function, and if \( {fY} \) denotes the vector field

\[
{\left( fY\right) }_{q} = f\left( q\right) {Y}_{q}
\]

then \( \vdash \) is required to satisfy the identity

\[
{X}_{p} \vdash  \left( {fY}\right)  = \left( {{X}_{p}f}\right) {Y}_{p} + f\left( p\right) {X}_{p} \vdash  Y.
\]

(As usual, \( {X}_{p}f \) denotes the directional derivative of \( f \) in the direction \( {X}_{p} \) .)

A global affine connection (or briefly a connection) on \( M \) is a function which assigns to each \( p \in  M \) an affine connection \( { \vdash  }_{p} \) at \( p \) , satisfying the following smoothness condition.

(1) If \( X \) and \( Y \) are smooth vector fields on \( M \) then the vector field \( X \vdash  Y \) , defined by the identity

\[
{\left( X \vdash  Y\right) }_{p} = {X}_{p}{ \vdash  }_{p}Y
\]

must also be smooth.

---

\( {}^{1} \) Note that our \( X \vdash  Y \) coincides with Nomizu’s \( {\nabla }_{X}Y \) . The notation is intended to suggest that the differential operator \( X \) acts on the vector field \( Y \) .

---

Note that:

(2) \( X \vdash  Y \) is bilinear as a function of \( X \) and \( Y \) ,

(3) \( \left( {fX}\right)  \vdash  Y = f\left( {X \vdash  Y}\right) \) ,

(4) \( (X \vdash  \left( {fY}\right)  = \left( {Xf}\right) Y + f\left( {X \vdash  Y}\right) \) .

Conditions (1), (2), (3), (4) can be taken as the definition of a connection.

In terms of local coordinates \( {u}^{l},\ldots ,{u}^{n} \) defined on a coordinate neighborhood \( U \subset  M \) , the connection \( \vdash \) is determined by \( {n}^{3} \) smooth real valued functions \( {\Gamma }_{ij}^{k} \) on \( U \) , as follows. Let \( {\partial }_{k} \) denote the vector field \( \frac{\partial }{\partial {u}^{k}} \) on \( U \) . Then any vector field \( X \) on \( U \) can be expressed uniquely as

\[
X = \mathop{\sum }\limits_{{k = 1}}{x}^{k}{\partial }_{k}
\]

where the \( {x}^{k} \) are real valued functions on \( U \) . In particular the vector field \( {\partial }_{i} \vdash  {\partial }_{j} \) can be expressed as

\[
{\partial }_{i} \vdash  {\partial }_{j} = \mathop{\sum }\limits_{k}{\Gamma }_{ij}^{k}{\partial }_{k} \tag{8.1}
\]

These functions \( {\Gamma }_{ij}^{k} \) , determine the connection completely on \( U \) . In fact given vector fields \( X = {x}^{i}{\partial }_{i} \) and \( Y = {y}^{j}{\partial }_{j} \) one can expand \( X \vdash  Y \) by the rules (2),(3), (4); yielding the formula

\[
X \vdash  Y = \mathop{\sum }\limits_{k}\left( {\mathop{\sum }\limits_{i}{x}^{i}{y}_{, i}^{k}}\right) {\partial }_{k} \tag{8.2}
\]

where the symbol \( {y}_{, i}^{k} \) stands for the real valued function

\[
{y}_{, i}^{k} = {\partial }_{i}{y}^{k} + \mathop{\sum }\limits_{j}{\Gamma }_{ij}^{k}{y}^{j}.
\]

Conversely, given any smooth real valued functions \( {\Gamma }_{ij}^{k} \) on \( U \) , one can define \( X \vdash  Y \) by the formula (8.2). The result clearly satisfies the conditions (1),(2),(3), (4), (8.1).

Using the connection \( \vdash \) one can define the covariant derivative of a vector field along a curve in \( M \) . First some definitions.

A parametrized curve in \( M \) is a smooth function \( c \) from the real numbers to \( M \) . A vector field \( V \) along the curve \( c \) is a function which assigns to each \( t \in  \mathbf{R} \) a tangent vector

\[
{V}_{t} \in  T{M}_{c\left( t\right) }.
\]

This is required to be smooth in the following sense: For any smooth function \( f \) on \( M \) the correspondence

\[
t \mapsto  {V}_{t}f
\]

should define a smooth function on \( \mathbf{R} \) .

As an example the velocity vector field \( \mathrm{d}c/\mathrm{d}t \) if of the curve is the vector field along \( c \) which is defined by the rule

\[
\frac{\mathrm{d}c}{\mathrm{\;d}t} = {c}_{ * }\frac{\mathrm{d}}{\mathrm{d}t}
\]

Here \( \frac{\mathrm{d}}{\mathrm{d}t} \) denotes the standard vector field on the real numbers, and

\[
{c}_{ * } : T{\mathbf{R}}_{t} \rightarrow  T{M}_{c\left( t\right) }
\]

denotes the homomorphism of tangent spaces induced by the map \( c \) . (Compare Figure 8.1.)

![bo_d7du90alb0pc73deir8g_49_246_629_1110_407_0.jpg](images/bo_d7du90alb0pc73deir8g_49_246_629_1110_407_0.jpg)

Figure 8.1

Now suppose that \( M \) is provided with an affine connection. Then any vector field \( V \) along \( c \) determines a new vector field \( \frac{\mathrm{D}V}{\mathrm{\;d}t} \) along \( c \) called the covariant derivative of \( V \) . The operation

\[
V \mapsto  \frac{\mathrm{D}V}{\mathrm{\;d}t}
\]

is characterized by the following three axioms:

(a) \( \frac{\mathrm{D}\left( {V + W}\right) }{\mathrm{d}t} = \frac{\mathrm{D}V}{\mathrm{\;d}t} + \frac{\mathrm{D}W}{\mathrm{\;d}t} \) .

(b) If \( f \) is a smooth real valued function on \( \mathbf{R} \) then

\[
\frac{\mathrm{D}\left( {fV}\right) }{\mathrm{d}t} = \frac{\mathrm{d}f}{\mathrm{\;d}t}V + f\frac{\mathrm{D}W}{\mathrm{\;d}t}.
\]

(c) If \( V \) is induced by a vector field \( Y \) on \( M \) , that is if \( {V}_{t} = {Y}_{c\left( t\right) } \) for each \( t \) , then \( \frac{\mathrm{D}V}{\mathrm{\;d}t} \) is equal to \( \mathrm{d}c/\mathrm{d}t \vdash  Y \) (= the covariant derivative of \( Y \) in the direction of the velocity vector of \( c \) ).

Lemma 8.2. There is one and only one operation \( V \mapsto  \frac{\mathrm{D}V}{\mathrm{\;d}t} \) which satisfies these three conditions.

Proof. Choose a local coordinate system for \( M \) , and let \( {u}^{1}\left( t\right) ,\ldots ,{u}^{n}\left( t\right) \) denote the coordinates of the point \( c\left( t\right) \) . The vector field \( V \) can be expressed uniquely in the form

\[
V = \sum {v}^{j}{\partial }_{j}
\]

where \( {v}^{1},\ldots ,{v}^{n} \) are real valued functions on \( \mathbf{R} \) (or an appropriate open subset of

R), and \( {\partial }_{1},\ldots ,{\partial }_{n} \) are the standard vector fields on the coordinate neighborhood. It follows from (a), (b) and (c) that

\[
\frac{\mathrm{D}V}{\mathrm{\;d}t} = \mathop{\sum }\limits_{j}\left( {\frac{\mathrm{d}{v}^{j}}{\mathrm{\;d}t}{\partial }_{j} + {v}^{j}\frac{\mathrm{d}c}{\mathrm{\;d}t}}\right)
\]

\[
= \mathop{\sum }\limits_{k}\left( {\frac{\mathrm{d}{v}^{k}}{\mathrm{\;d}t} + \mathop{\sum }\limits_{{i, j}}\frac{\mathrm{d}{u}^{i}}{\mathrm{\;d}t}{\Gamma }_{ij}^{k}{v}^{j}}\right) {\partial }_{k}.
\]

Conversely, defining \( \frac{\mathrm{D}V}{\mathrm{\;d}t} \) by this formula, it is not difficult to verify that conditions (a), (b) and (c) are satisfied.

A vector field \( V \) along \( c \) is said to be a parallel vector field if the covariant derivative \( \frac{\mathrm{D}V}{\mathrm{\;d}t} \) is identically zero.

Lemma 8.3. Given a curve \( c \) and a tangent vector \( {V}_{0} \) at the point \( c\left( 0\right) \) , there is one and only one parallel vector field \( V \) along \( c \) which extends \( {V}_{0} \) .

Proof. The differential equations

\[
\frac{\mathrm{d}{v}^{k}}{\mathrm{\;d}t} + \mathop{\sum }\limits_{{i, j}}\frac{\mathrm{d}{u}^{i}}{\mathrm{\;d}t}{\Gamma }_{ij}^{k}{v}^{j} = 0
\]

have solutions \( {v}^{k}\left( t\right) \) which are uniquely determined by the initial values \( {v}^{k}\left( 0\right) \) . Since these equations are linear, the solutions can be defined for all relevant values of \( t \) . (Compare [Gra56, p. 152].)

The vector \( {V}_{t} \) is said to be obtained from \( {V}_{0} \) by parallel translation along \( c \) .

Now suppose that \( M \) is a Riemannian manifold. The inner product of two vectors \( {X}_{p},{Y}_{p} \) will be denoted by \( \left\langle  {{X}_{p},{Y}_{p}}\right\rangle \) .

Definition 8.4. A connection \( \vdash \) on \( M \) is compatible with the Riemannian metric if parallel translation preserves inner products. In other words, for any parametrized curve \( c \) and any pair \( P,{P}^{\prime } \) of parallel vector fields along \( c \) , the inner product \( \left\langle  {P,{P}^{\prime }}\right\rangle \) should be constant.

Lemma 8.5. Suppose that the connection is compatible with the metric. Let \( V, W \) be any two vector fields along \( c \) . Then

\[
\frac{\mathrm{d}}{\mathrm{d}t}\langle V, W\rangle  = \left\langle  {\frac{\mathrm{D}V}{\mathrm{\;d}t}, W}\right\rangle   + \left\langle  {V,\frac{\mathrm{D}W}{\mathrm{\;d}t}}\right\rangle  .
\]

Proof. Choose parallel vector fields \( {P}_{1},\ldots ,{P}_{n} \) along \( c \) which are orthonormal at one point of \( c \) and hence at every point of \( c \) . Then the given fields \( V \) and \( W \) can be expressed as \( \sum {v}^{i}{P}_{i} \) and \( \sum {w}^{j}{P}_{j} \) respectively (where \( {v}^{i} = \left\langle  {V,{P}_{i}}\right\rangle \) is a real valued function on \( \mathbf{R}) \) . It follows that \( \langle V, W\rangle  = \sum {v}^{i}{w}^{i} \) and that

\[
\frac{\mathrm{D}V}{\mathrm{\;d}t} = \sum \frac{\mathrm{d}{v}^{i}}{\mathrm{\;d}t}{P}_{i},\;\frac{\mathrm{D}W}{\mathrm{\;d}t} = \sum \frac{\mathrm{d}{w}^{j}}{\mathrm{\;d}t}{P}_{j}.
\]

Therefore

\[
\left\langle  {\frac{\mathrm{D}V}{\mathrm{\;d}t}, W}\right\rangle   + \left\langle  {V,\frac{\mathrm{D}W}{\mathrm{\;d}t}}\right\rangle   = \sum \left( {\frac{\mathrm{d}{v}^{i}}{\mathrm{\;d}t}{w}_{i} + {v}^{i}\frac{\mathrm{d}{w}^{i}}{\mathrm{\;d}t}}\right)  = \frac{\mathrm{d}}{\mathrm{d}t}\langle V, W\rangle ,
\]

which completes the proof.

Corollary 8.6. For any vector fields \( Y,{Y}^{\prime } \) on \( M \) and any vector \( {X}_{p} \in  T{M}_{p} \) :

\[
{X}_{p}\left\langle  {Y,{Y}^{\prime }}\right\rangle   = \left\langle  {{X}_{p} \vdash  Y,{Y}_{p}^{\prime }}\right\rangle   + \left\langle  {{Y}_{p},{X}_{p} \vdash  {Y}^{\prime }}\right\rangle  .
\]

Proof. Choose a curve \( c \) whose velocity vector at \( t = 0 \) is \( {X}_{p} \) ; and apply Lemma 8.5.

Definition 8.7. A connection \( \vdash \) is called symmetric if it satisfies the identity \( {}^{2} \)

\[
\left( {X \vdash  Y}\right)  - \left( {Y \vdash  X}\right)  = \left\lbrack  {X, Y}\right\rbrack
\]

(As usual, \( \left\lbrack  {X, Y}\right\rbrack \) denotes the poison bracket \( \left\lbrack  {X, Y}\right\rbrack  f = X\left( {Yf}\right)  - Y\left( {Xf}\right) \) of two vector fields.) Applying this identity to the case \( X = {\partial }_{i}, Y = {\partial }_{j} \) , since \( \left\lbrack  {{\partial }_{i},{\partial }_{j}}\right\rbrack   = 0 \) one obtains the relation

\[
{\Gamma }_{ij}^{k} - {\Gamma }_{ji}^{k} = 0.
\]

Conversely if \( {\Gamma }_{ij}^{k} = {\Gamma }_{ji}^{k} \) then using formula (8.2) it is not difficult to verify that the connection \( \vdash \) is symmetric throughout the coordinate neighborhood.

Lemma 8.8 (Fundamental lemma of Riemannian geometry). A Riemannian manifold possesses one and only one symmetric connection which is compatible with its metric.

\[
\text{ (Compare [Nom56, p. 76], [Lau65, p. 95].) }
\]

Proof of Uniqueness. Applying Corollary 8.6 to the vector fields \( {\partial }_{i},{\partial }_{j},{\partial }_{k} \) , and setting \( \left\langle  {{\partial }_{i},{\partial }_{k}}\right\rangle   = {g}_{jk} \) one obtains the identity

\[
{\partial }_{i}{g}_{jk} = \left\langle  {{\partial }_{i} \vdash  {\partial }_{j},{\partial }_{k}}\right\rangle   + \left\langle  {{\partial }_{j},{\partial }_{i} \vdash  {\partial }_{k}}\right\rangle
\]

Permuting \( i, j \) , and \( k \) this gives three linear equations relating the three quantities

\[
\left\langle  {{\partial }_{i} \vdash  {\partial }_{j},{\partial }_{k}}\right\rangle  ,\;\left\langle  {{\partial }_{j} \vdash  {\partial }_{k},{\partial }_{i}}\right\rangle  ,\;\text{ and }\left\langle  {{\partial }_{k} \vdash  {\partial }_{i},{\partial }_{j}}\right\rangle  .
\]

(There are only three such quantities since \( {\partial }_{i} \vdash  {\partial }_{j} = {\partial }_{j} \vdash  {\partial }_{i} \) .) These equations can be solved uniquely; yielding the first Christoffel identity

\[
\left\langle  {{\partial }_{i} \vdash  {\partial }_{j},{\partial }_{k}}\right\rangle   = \frac{1}{2}\left( {{\partial }_{i}{g}_{jk} + {\partial }_{j}{g}_{ik} - {\partial }_{k}{g}_{ij}}\right)
\]

---

\( {}^{2} \) The following reformulation may (or may not) seem more intuitive. Define The "covariant second derivative" of a real valued function \( f \) along two vectors \( {X}_{p},{Y}_{p} \) to be the expression

\[
{X}_{p}\left( {Yf}\right)  - \left( {{X}_{p} \vdash  Y}\right) f
\]

where \( Y \) denotes any vector field extending \( {Y}_{p} \) . It can be verified that this expression does not depend on the choice of \( Y \) . (Compare the proof of Lemma 9.1 below.) Then the connection is symmetric if this second derivative is symmetric as a function of \( {X}_{p} \) and \( {Y}_{p} \) .

---

The left hand side of this identity is equal to \( \mathop{\sum }\limits_{\ell }{\Gamma }_{ij}^{\ell }{g}_{\ell k} \) . Multiplying by the inverse \( \left( {g}^{k\ell }\right) \) of the matrix \( \left( {g}_{\ell k}\right) \) this yields the second Christoffel identity

\[
{\Gamma }_{ij}^{\ell } = \mathop{\sum }\limits_{k}\frac{1}{2}\left( {{\partial }_{i}{g}_{jk} + {\partial }_{j}{g}_{ik} - {\partial }_{k}{g}_{ij}}\right) {g}^{\ell k}.
\]

Thus the connection is uniquely determined by the metric.

Conversely, defining \( {\Gamma }_{ij}^{\ell } \) by this formula, one can verify that the resulting connection is symmetric and compatible with the metric. This completes the proof.

An alternative characterization of symmetry will be very useful later. Consider a "parametrized surface" in \( M \) : that is a smooth function

\[
s : {\mathbf{R}}^{2} \rightarrow  M
\]

By a vector field \( V \) along \( s \) is meant a function which assigns to each \( \left( {x, y}\right)  \in  {\mathbf{R}}^{2} \) a tangent vector

\[
{V}_{\left( x, y\right) } \in  T{M}_{s\left( {x, y}\right) }.
\]

As examples, the two standard vector fields \( \frac{\partial }{\partial x} \) and \( \frac{\partial }{\partial y} \) give rise to vector fields \( {s}_{ * }\frac{\partial }{\partial x} \) , and \( {s}_{ * }\frac{\partial }{\partial y} \) along \( s \) . These will be denoted briefly by \( \frac{\partial s}{\partial x} \) and \( \frac{\partial s}{\partial y} \) ; and called the "velocity vector fields" of \( s \) .

For any smooth vector field \( V \) along \( s \) the covariant derivatives \( \frac{\mathrm{D}V}{\mathrm{\;d}x} \) and \( \frac{\mathrm{D}V}{\mathrm{\;d}y} \) are new vector fields, constructed as follows. For each fixed \( {y}_{0} \) , restricting \( V \) to the curve

\[
x \mapsto  s\left( {x,{y}_{0}}\right)
\]

one obtains a vector field along this curve. Its covariant derivative with respect to \( x \) is defined to be \( {\left( \frac{\mathrm{D}V}{\mathrm{\;d}x}\right) }_{\left( x,{y}_{0}\right) } \) . This defines \( \frac{\mathrm{D}V}{\mathrm{\;d}x} \) along the entire parametrized surface \( s \) .

As examples, we can form the two covariant derivatives of the two vector fields \( \frac{\partial s}{\partial x} \) and \( \frac{\partial s}{\partial y} \) . The derivatives \( \frac{\mathrm{D}}{\mathrm{d}x}\frac{\partial s}{\partial x} \) and \( \frac{\mathrm{D}}{\mathrm{d}y}\frac{\partial s}{\partial y} \) are simply the acceleration vectors of suitable coordinate curves. However, the mixed derivatives \( \frac{\mathrm{D}}{\mathrm{d}x}\frac{\partial s}{\partial y} \) and \( \frac{\mathrm{D}}{\mathrm{d}y}\frac{\partial s}{\partial x} \) cannot be described so simply.

Lemma 8.9. If the connection is symmetric then \( \frac{\mathrm{D}}{\mathrm{d}x}\frac{\partial s}{\partial y} = \frac{\mathrm{D}}{\mathrm{d}y}\frac{\partial s}{\partial x} \) .

Proof. Express both sides in terms of a local coordinate system, and compute.
