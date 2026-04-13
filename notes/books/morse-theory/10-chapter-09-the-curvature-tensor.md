# Chapter 9 The Curvature Tensor

Based on lecture notes by

M. Spivak and R. Wells

The curvature tensor \( \mathcal{R} \) of an affine connection \( \vdash \) measures the extent to which the second covariant derivative \( {\partial }_{i} \vdash  \left( {{\partial }_{j} \vdash  Z}\right) \) is symmetric in \( i \) and \( j \) . Given vector fields \( X, Y, Z \) define a new vector field \( \mathcal{R}\left( {X, Y}\right) Z \) by the identity \( {}^{1} \)

\[
\mathcal{R}\left( {X, Y}\right) Z =  - X \vdash  \left( {Y \vdash  Z}\right)  + Y \vdash  \left( {X \vdash  Z}\right)  + \left\lbrack  {X, Y}\right\rbrack   \vdash  Z.
\]

Lemma 9.1. The value of \( \mathcal{R}\left( {X, Y}\right) Z \) at a point \( p \in  M \) depends only on the vectors \( {X}_{p},{Y}_{p},{Z}_{p} \) at this point \( p \) and not on their values at nearby points. Furthermore the correspondence

\[
{X}_{p},{Y}_{p},{Z}_{p} \mapsto  \mathcal{R}\left( {{X}_{p},{Y}_{p}}\right) {Z}_{p}
\]

from \( T{M}_{p} \times  T{M}_{p} \times  T{M}_{p} \) to \( T{M}_{p} \) is tri-linear.

Briefly, this lemma can be expressed by saying that \( \mathcal{R} \) is a "tensor."

Proof. Clearly \( \mathcal{R}\left( {X, Y}\right) Z \) is a tri-linear function of \( X, Y \) , and \( Z \) . If \( X \) is replaced by a multiple \( {fX} \) then the three terms \( - X \vdash  \left( {Y \vdash  Z}\right) , Y \vdash  \left( {X \vdash  Z}\right) ,\left\lbrack  {X, Y}\right\rbrack   \vdash  Z \) are replaced respectively by

(1) \( - {fX} \vdash  \left( {Y \vdash  Z}\right) \) ,

(2) \( \left( {Yf}\right) \left( {X \vdash  Z}\right)  + {fY} \vdash  \left( {X \vdash  Z}\right) \) ,

(3) \( - \left( {Yf}\right) \left( {X \vdash  Z}\right)  + f\left\lbrack  {X, Y}\right\rbrack   \vdash  Z \) .

Adding these three terms one obtains the identity

\[
\mathcal{R}\left( {{fX}, Y}\right) Z = f\mathcal{R}\left( {X, Y}\right) Z.
\]

Corresponding identities for \( Y \) and \( Z \) are easily obtained by similar computations.

---

\( {}^{1} \) Nomizu gives \( \mathcal{R} \) the opposite sign. Our sign convention has the advantage that (in the Riemannian case) the inner product \( \left\langle  {\mathcal{R}\left( {{\partial }_{h},{\partial }_{i}}\right) {\partial }_{j},{\partial }_{k}}\right\rangle \) coincides with the classical symbol \( {\mathcal{R}}_{hijk} \) .

---

Now suppose that \( X = \sum {x}^{i}{\partial }_{i}, Y = \sum {y}^{j}{\partial }_{j} \) , and \( Z = \sum {z}^{k}{\partial }_{k} \) . Then

\[
\mathcal{R}\left( {X, Y}\right) Z = \sum \mathcal{R}\left( {{x}^{i}{\partial }_{i},{y}^{j}{\partial }_{j}}\right) \left( {{z}^{k}{\partial }_{k}}\right)
\]

\[
= \sum {x}^{i}{y}^{j}{z}^{k}\mathcal{R}\left( {{\partial }_{i},{\partial }_{j}}\right) {\partial }_{k}.
\]

Evaluating this expression at \( p \) one obtains the formula

\[
{\left( \mathcal{R}\left( X, Y\right) Z\right) }_{p} = \sum {x}^{i}\left( p\right) {y}^{j}\left( p\right) {z}^{k}\left( p\right) {\left( \mathcal{R}\left( {\partial }_{i},{\partial }_{j}\right) {\partial }_{k}\right) }_{p}
\]

which depends only on the values of the functions \( {x}^{i},{y}^{j},{z}^{k} \) at \( p \) , and not on their values at nearby points. This completes the proof.

Now consider a parametrized surface

\[
s : {\mathbf{R}}^{2} \rightarrow  M
\]

Given any vector field \( V \) along \( s \) . one can apply the two covariant differentiation operators \( \frac{\mathrm{D}}{\mathrm{d}x} \) and \( \frac{\mathrm{D}}{\mathrm{d}y} \) to \( V \) . In general these operators will not commute with each other.

Lemma 9.2. \( \frac{\mathrm{D}}{\mathrm{d}y}\frac{\mathrm{D}}{\mathrm{d}x}V - \frac{\mathrm{D}}{\mathrm{d}x}\frac{\mathrm{D}}{\mathrm{d}y}V = \mathcal{R}\left( {\frac{\partial s}{\partial x},\frac{\partial s}{\partial y}}\right) V \) .

Proof. Express both sides in terms of a local coordinate system, and compute, making use of the identity

\[
{\partial }_{j} \vdash  \left( {{\partial }_{i} \vdash  {\partial }_{k}}\right)  - {\partial }_{i} \vdash  \left( {{\partial }_{j} \vdash  {\partial }_{k}}\right)  = \mathcal{R}\left( {{\partial }_{i},{\partial }_{j}}\right) {\partial }_{k}.
\]

Note. It is interesting to ask whether one can construct a vector field \( P \) along \( s \) which is parallel, in the sense that

\[
\frac{\mathrm{D}}{\mathrm{d}x}P = \frac{\mathrm{D}}{\mathrm{d}y}P = 0,
\]

and which has a given value \( {P}_{\left( 0,0\right) } \) at the origin. In general no such vector field exists. However, if the curvature tensor happens to be zero then \( P \) can be constructed as follows. Let \( {P}_{\left( x,0\right) } \) be a parallel vector field along the \( x \) -axis, satisfying the given initial condition. For each fixed \( {x}_{0} \) let \( {P}_{\left( {x}_{0}, y\right) } \) be a parallel vector field along the curve

\[
y \mapsto  s\left( {{x}_{0}, y}\right) ,
\]

having the right value for \( y = 0 \) . This defines \( P \) everywhere along \( s \) . Clearly \( \frac{\mathrm{D}}{\mathrm{d}y}P \) is identically zero; and \( \frac{\mathrm{D}}{\mathrm{d}x}P \) is zero along the \( x \) -axis. Now the identity

\[
\frac{\mathrm{D}}{\mathrm{d}y}\frac{\mathrm{D}}{\mathrm{d}x}P - \frac{\mathrm{D}}{\mathrm{d}x}\frac{\mathrm{D}}{\mathrm{d}y}P = \mathcal{R}\left( {\frac{\partial s}{\partial x},\frac{\partial s}{\partial y}}\right) P = 0
\]

implies that \( \frac{\mathrm{D}}{\mathrm{d}y}\frac{\mathrm{D}}{\mathrm{d}x}P = 0 \) . In other words, the vector field \( \frac{\mathrm{D}}{\mathrm{d}x}P \) is parallel along the curves

\[
y \mapsto  s\left( {{x}_{0}, y}\right) \text{ . }
\]

Since \( {\left( \frac{\mathrm{D}}{\mathrm{d}x}P\right) }_{\left( {x}_{0},0\right) } = 0 \) , this implies that \( \frac{\mathrm{D}}{\mathrm{d}x}P \) is identically zero; and completes the proof that \( P \) is parallel along \( s \) .

Henceforth we will assume that \( M \) is a Riemannian manifold, provided with the unique symmetric connection which is compatible with its metric. In conclusion we will prove that the tensor \( \mathcal{R} \) satisfies four symmetry relations.

Lemma 9.3. The curvature tensor of a Riemannian manifold satisfies:

(1) \( \mathcal{R}\left( {X, Y}\right) Z + \mathcal{R}\left( {Y, X}\right) Z = 0 \) ,

(2) \( \mathcal{R}\left( {X, Y}\right) Z + \mathcal{R}\left( {Y, Z}\right) X + \mathcal{R}\left( {Z, X}\right) Y = 0 \) ,

(3) \( \langle \mathcal{R}\left( {X, Y}\right) Z, W\rangle  + \langle \mathcal{R}\left( {X, Y}\right) W, Z\rangle  = 0 \) ,

(4) \( \langle \mathcal{R}\left( {X, Y}\right) Z, W\rangle  + \langle \mathcal{R}\left( {Z, W}\right) X, Y\rangle  = 0 \) .

Proof. The skew-symmetry relation (1) follows immediately from the definition of \( \mathcal{R} \) .

Since all three terms of (2) are tensors, it is sufficient to prove (2) when the bracket products \( \left\lbrack  {X, Y}\right\rbrack  ,\left\lbrack  {X, Z}\right\rbrack \) and \( \left\lbrack  {Y, Z}\right\rbrack \) are all zero. Under this hypothesis we must verify the identity

\[
- X \vdash  \left( {Y \vdash  Z}\right)  + Y \vdash  \left( {X \vdash  Z}\right)
\]

\[
- Y \vdash  \left( {Z \vdash  X}\right)  + Z \vdash  \left( {Y \vdash  X}\right)
\]

\[
- Z \vdash  \left( {X \vdash  Y}\right)  + X \vdash  \left( {X \vdash  Y}\right)  = 0.
\]

But the symmetry of the connection implies that

\[
Y \vdash  Z - Z \vdash  Y = \left\lbrack  {Y, Z}\right\rbrack   = 0.
\]

Thus the upper left term cancels the lower right term. Similarly the remaining terms cancel in pairs. This proves (2).

To prove (3) we must show that the expression \( \langle \mathcal{R}\left( {X, Y}\right) Z, W\rangle \) is skew-symmetric in \( Z \) and \( W \) . This is clearly equivalent to the assertion that

\[
\langle \mathcal{R}\left( {X, Y}\right) Z, Z\rangle  = 0
\]

for all \( X, Y, Z \) . Again we may assume that \( \left\lbrack  {X, Y}\right\rbrack   = 0 \) , so that \( \langle \mathcal{R}\left( {X, Y}\right) Z, Z\rangle \) is equal to

\[
\langle  - X \vdash  \left( {Y \vdash  Z}\right)  + Y \vdash  \left( {X \vdash  Z}\right) , Z\rangle .
\]

In other words we must prove that the expression

\[
\langle Y \vdash  \left( {X \vdash  Z}\right) , Z\rangle
\]

is symmetric in \( X \) and \( Y \) .

Since \( \left\lbrack  {X, Y}\right\rbrack   = 0 \) the expression \( {YX}\langle Z, Z\rangle \) is symmetric in \( X \) and \( Y \) . Since the connection is compatible with the metric, we have

\[
X\langle Z, Z\rangle  = 2\langle X \vdash  Z, Z\rangle
\]

hence

\[
{YX}\langle Z, Z\rangle  = 2\langle Y \vdash  \left( {X \vdash  Z}\right) , Z\rangle  +  = 2\langle X \vdash  Z, Y \vdash  Z\rangle .
\]

But the right hand term is clearly symmetric in \( X \) and \( Y \) . Therefore \( \langle Y \vdash  (X \vdash \; Z), Z\rangle \) is symmetric in \( X \) and \( Y \) ; which proves property (3).

Property (4) may be proved from (1), (2), and (3) as follows.

![bo_d7du90alb0pc73deir8g_56_250_391_1188_692_0.jpg](images/bo_d7du90alb0pc73deir8g_56_250_391_1188_692_0.jpg)

Formula (2) asserts that the sum of the quantities at the vertices of shaded triangle \( W \) is zero. Similarly (making use of (1) and (3)) the sum of the vertices of each of the other shaded triangles is zero. Adding these identities for the top two shaded triangles, and subtracting the identities for the bottom ones, this means that twice the top vertex minus twice the bottom vertex is zero. This proves (4), and completes the proof.
