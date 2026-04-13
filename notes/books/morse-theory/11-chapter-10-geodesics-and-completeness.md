# Chapter 10 Geodesics and Completeness

Based on lecture notes by

M. Spivak and R. Wells

Let \( M \) be a connected Riemannian manifold.

Definition 10.1. A parametrized path

\[
\gamma  : I \rightarrow  M,
\]

where I denotes any interval of real numbers, is called a geodesic if the acceleration vector field \( \frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{d}\gamma }{\mathrm{d}t} \) is identically zero. Thus the velocity vector field \( \frac{\mathrm{d}\gamma }{\mathrm{d}t} \) must be parallel along \( \gamma \) . if \( \gamma \) is a geodesic, then the identity

\[
\frac{\mathrm{d}}{\mathrm{d}t}\left\langle  {\frac{\mathrm{d}\gamma }{\mathrm{d}t},\frac{\mathrm{d}\gamma }{\mathrm{d}t}}\right\rangle   = 2\left\langle  {\frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{d}\gamma }{\mathrm{d}t},\frac{\mathrm{d}\gamma }{\mathrm{d}t}}\right\rangle   = 0
\]

shown that the length \( \begin{Vmatrix}\frac{\mathrm{d}\gamma }{\mathrm{d}t}\end{Vmatrix} = {\left\langle  \frac{\mathrm{d}\gamma }{\mathrm{d}t},\frac{\mathrm{d}\gamma }{\mathrm{d}t}\right\rangle  }^{\frac{1}{2}} \) of the velocity vector is constant along \( \gamma \) . Introducing the arc-length function

\[
s\left( t\right)  = \int \parallel \frac{\mathrm{d}\gamma }{\mathrm{d}t}\parallel  + \text{ constant }
\]

This statement can be rephrased as follows: The parameter \( t \) along a geodesic is a linear function of the arc-length. The parameter \( t \) is actually equal to the arc-length if and only if \( \begin{Vmatrix}\frac{\mathrm{d}\gamma }{\mathrm{d}t}\end{Vmatrix} = 1 \) .

In terms of a local coordinate system with coordinates \( {u}^{1},\ldots ,{u}^{n} \) a curve \( t \mapsto \; \gamma \left( t\right)  \in  M \) determines \( n \) smooth functions \( {u}^{1}\left( t\right) ,\ldots ,{u}^{n}\left( t\right) \) . The equation \( \frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{d}\gamma }{\mathrm{d}t} \) for a geodesic then takes the form

\[
\frac{{\mathrm{d}}^{2}{u}^{k}}{\mathrm{\;d}{t}^{2}} + \mathop{\sum }\limits_{{i, j = 1}}^{n}{\Gamma }_{ij}^{k}\left( {{u}^{1},\ldots ,{u}^{n}}\right) \frac{\mathrm{d}{u}^{i}}{\mathrm{\;d}t}\frac{\mathrm{d}{u}^{j}}{\mathrm{\;d}t} = 0.
\]

The existence of geodesics depends, therefore, on the solutions of a certain system of second order differential equations.

More generally consider any system of equations of the form

\[
\frac{{\mathrm{d}}^{2}\overrightarrow{u}}{\mathrm{\;d}{t}^{2}} = \overrightarrow{F}\left( {\overrightarrow{u},\frac{\mathrm{d}\overrightarrow{u}}{\mathrm{\;d}t}}\right) .
\]

Here \( \overrightarrow{u} \) stands for \( \left( {{u}^{1},\ldots ,{u}^{n}}\right) \) and \( \overrightarrow{F} \) stands for an \( n \) -tuple of \( {C}^{\infty } \) functions, all defined throughout some neighborhood \( U \) of a point

\[
\left( {{\overrightarrow{u}}_{1},{\overrightarrow{v}}_{1}}\right)  \in  {\mathbf{R}}^{2n}\text{ . }
\]

Theorem 10.2 (Existence and Uniqueness Theorem). There exists a neighborhood \( W \) of the point \( \left( {{\overrightarrow{u}}_{1},{\overrightarrow{v}}_{1}}\right) \) and a number \( \varepsilon  > 0 \) so that, for each \( \left( {{\overrightarrow{u}}_{0},{\overrightarrow{v}}_{0}}\right)  \in  W \) the differential equation

\[
\frac{{\mathrm{d}}^{2}\overrightarrow{u}}{\mathrm{\;d}{t}^{2}} = \overrightarrow{F}\left( {\overrightarrow{u},\frac{\mathrm{d}\overrightarrow{u}}{\mathrm{\;d}t}}\right)
\]

has a unique solution \( t \rightarrow  u\left( t\right) \) which is defined for \( \left| t\right|  < \varepsilon \) , and satisfies the initial conditions

\[
\overrightarrow{u}\left( 0\right)  = {\overrightarrow{u}}_{0},\;\frac{\mathrm{d}\overrightarrow{u}}{\mathrm{\;d}t}\left( 0\right)  = {\overrightarrow{v}}_{0}.
\]

Furthermore, the solution depends smoothly on the initial conditions. In other words, the correspondence

\[
\left( {{\overrightarrow{u}}_{0},{\overrightarrow{v}}_{0}, t}\right)  \mapsto  \overrightarrow{u}\left( t\right)
\]

from \( W \times  \left( {-\varepsilon ,\varepsilon }\right) \) to \( {\mathbf{R}}^{n} \) is a \( {C}^{\infty } \) function of all \( {2n} + 1 \) variables.

Proof. Introducing the new variables \( {v}^{i} = \frac{\mathrm{d}{u}^{i}}{\mathrm{\;d}t} \) this system of \( n \) second order equations becomes a system of \( {2n} \) first order equations:

\[
\left\{  \begin{array}{l} \frac{\mathrm{d}\overrightarrow{u}}{\mathrm{\;d}t} = \overrightarrow{v}, \\  \frac{\mathrm{d}\overrightarrow{v}}{\mathrm{\;d}t} = \overrightarrow{F}\left( {\overrightarrow{u},\overrightarrow{v}}\right) . \end{array}\right.
\]

The assertion then follows from [Gra56, p. 166]. (Compare our §2.4.)

Applying this theorem to the differential equation for geodesics, one obtains the following.

Lemma 10.3. For every point \( {p}_{0} \) on a Riemannian manifold \( M \) there exists a neighborhood \( U \) of \( {p}_{0} \) and a number \( \varepsilon  > 0 \) so that: for each \( p \in  U \) and each tangent vector \( v \in  T{M}_{p} \) with length \( < \varepsilon \) there is a unique geodesic

\[
{\gamma }_{v} : \left( {-2,2}\right)  \rightarrow  M
\]

satisfying the conditions

\[
{\gamma }_{v}\left( 0\right)  = p,\;\frac{\mathrm{d}{\gamma }_{v}}{\mathrm{\;d}t}\left( 0\right)  = v.
\]

Proof. If we were willing to replace the interval \( \left( {-2,2}\right) \) by an arbitrarily small interval, then this statement would follow immediately from Theorem 10.2. To be more precise; there exists a neighborhood \( U \) of \( {p}_{0} \) and numbers \( {\varepsilon }_{1},{\varepsilon }_{2} > 0 \) so that: for each \( p \in  U \) and each \( v \in  T{M}_{p} \) with \( \parallel v\parallel  < {\varepsilon }_{1} \) there is a unique geodesic

\[
{\gamma }_{v} : \left( {-2{\varepsilon }_{2},2{\varepsilon }_{2}}\right)  \rightarrow  M
\]

satisfying the required initial conditions.

To obtain the sharper statement it is only necessary to observe that the differential equation for geodesics has the following homogeneity property. Let \( c \) be any constant. If the parametrized curve

\[
t \mapsto  \gamma \left( t\right)
\]

is a geodesic, then the parametrized curve

\[
t \mapsto  \gamma \left( {ct}\right)
\]

will also be a geodesic.

Now suppose that \( \varepsilon \) is smaller than \( {\varepsilon }_{1}{\varepsilon }_{2} \) . Then if \( \parallel v\parallel  < \varepsilon \) and \( \left| t\right|  < 2 \) note that

\[
\begin{Vmatrix}\frac{v}{{\varepsilon }_{2}}\end{Vmatrix} < {\varepsilon }_{1}\;\text{ and }\;\left| {{\varepsilon }_{2}t}\right|  < 2{\varepsilon }_{2}.
\]

Hence we can define \( {\gamma }_{v}\left( t\right) \) to be \( {\gamma }_{v/{\varepsilon }_{2}}\left( {{\varepsilon }_{2}t}\right) \) . This proves Lemma 10.3.

This following notation will be convenient. Let \( V \in  T{M}_{q} \) be a tangent vector, and suppose that there exists a geodesic

\[
\gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

satisfying the conditions

\[
\gamma \left( 0\right)  = q,\;\frac{\mathrm{d}\gamma }{\mathrm{d}t}\left( 0\right)  = v.
\]

Then the point \( \gamma \left( 1\right)  \in  M \) will be denoted by \( {\exp }_{q}\left( v\right) \) and called the exponential \( {}^{1} \) of the tangent vector \( v \) . The geodesic \( \gamma \) can thus be described by the formula

\[
\gamma \left( t\right)  = {\exp }_{q}\left( {tv}\right) .
\]

Lemma 10.3 says that \( {\exp }_{q}\left( v\right) \) is defined providing that \( \parallel v\parallel \) is small enough. In general, \( {\exp }_{q}\left( v\right) \) is not defined for large vectors \( v \) . However, if defined at all, \( {\exp }_{q}\left( v\right) \) is always uniquely defined.

Definition 10.4. The manifold \( M \) is geodesically complete if \( {\exp }_{q}\left( v\right) \) is defined for all \( q \in  M \) and all vectors \( v \in  T{M}_{q} \) . This is clearly equivalent to the following requirement:

---

\( {}^{1} \) The historical motivation for this terminology is the following. If \( M \) is the group of all \( n \times  n \) unitary matrices then the tangent space \( T{M}_{\mathrm{I}} \) at the identity can be identified with the space of \( n \times  n \) skew-Hermitian matrices. The function

\[
{\exp }_{\mathrm{I}} : T{M}_{\mathrm{I}} \rightarrow  M
\]

as defined above is then given by the exponential power series

\[
{\exp }_{\mathrm{I}}\left( A\right)  = \mathrm{I} + A + \frac{1}{2!}{A}^{2} + \frac{1}{3!}{A}^{3} + \ldots .
\]

---

For every geodesic segment \( {\gamma }_{0} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) it should be possible to extend \( {\gamma }_{0} \) to an infinite geodesic

\[
\gamma  : \mathbf{R} \rightarrow  M
\]

We will return to a study of completeness after proving some local results.

Let \( {TM} \) be the tangent manifold of \( M \) , consisting of all pairs \( \left( {p, v}\right) \) with \( p \in  M \) , \( v \in  T{M}_{p} \) . We give \( {TM} \) the following \( {C}^{\infty } \) structure: if \( \left( {{u}^{1},\ldots ,{u}^{n}}\right) \) is a coordinate system in an open set \( U \subset  M \) then every tangent vector at \( q \in  U \) can be expressed uniquely as \( {t}^{1}{\partial }_{1} + \cdots  + {t}^{n}{\partial }_{n} \) , where \( {\partial }_{i} = {\left. \frac{\partial }{\partial {u}^{i}}\right| }_{q} \) . Then the functions \( {u}^{1},\ldots ,{u}^{n} \) , \( {t}^{1},\ldots ,{t}^{n} \) a coordinate system on the open set \( {TU} \subset  {TM} \) .

Lemma 10.3 says that for each \( p \in  M \) the map

\[
\left( {q, v}\right)  \mapsto  {\exp }_{q}\left( v\right)
\]

is defined throughout a neighborhood \( V \) of the point \( \left( {p,0}\right)  \in  {TM} \) . Furthermore this map is differentiable throughout \( V \) .

Now consider the smooth function \( F : V \rightarrow  M \times  M \) defined by \( F\left( {q, v}\right)  = \; \left( {q,{\exp }_{q}\left( v\right) }\right) \) . We claim that the Jacobian of \( F \) at the point \( \left( {p,0}\right) \) is non-singular. In fact, denoting the induced coordinates on \( U \times  U \subset  M \times  M \) by \( \left( {{u}_{1}^{1},\ldots ,{u}_{1}^{n},{u}_{2}^{1},\ldots ,{u}_{2}^{n}}\right) \) , we have

\[
{F}_{ * }\left( \frac{\partial }{\partial {u}^{i}}\right)  = \frac{\partial }{\partial {u}_{1}^{i}} + \frac{\partial }{\partial {u}_{2}^{i}}
\]

\[
{F}_{ * }\left( \frac{\partial }{\partial {t}^{j}}\right)  = \;\frac{\partial }{\partial {u}_{2}^{j}}
\]

Thus the Jacobian matrix of \( F \) at \( \left( {p,0}\right) \) has the form \( \left( \begin{matrix} \mathrm{I} & \mathrm{I} \\  o & \mathrm{I} \end{matrix}\right) \) , and hence is nonsingular.

It follows from the implicit function theorem that \( F \) maps some neighborhood \( {V}^{\prime } \) of \( \left( {p,0}\right)  \in  {TM} \) diffeomorphically onto some neighborhood of \( \left( {p, p}\right)  \in  M \times   = \) definition \( M \) . We may assume that the first neighborhood \( {V}^{\prime } \) , consists of all pairs \( \left( {q, v}\right) \) such that \( q \) belongs to a given neighborhood \( {U}^{\prime } \) of \( p \) and such that \( \parallel v\parallel  < \varepsilon \) . Choose a smaller neighborhood \( W \) of \( p \) so that \( F\left( {V}^{\prime }\right)  \supset  W \times  W \) . Then we have proven the following.

Lemma 10.5. For each \( p \in  M \) there exists a neighborhood \( W \) and a number \( e > 0 \) so that:

(1) Any two points of \( W \) are joined by a unique geodesic in \( M \) of length \( < \varepsilon \) .

(2) This geodesic depends smoothly upon the two points. (i.e., if \( t \rightarrow  {\exp }_{{q}_{1}}\left( {tv}\right) \) , \( 0 \leq  t \leq  1 \) , is the geodesic joining \( {q}_{1} \) and \( {q}_{2} \) , then the pair \( \left( {{q}_{1}, v}\right)  \in  {TM} \) depends differentiably on \( \left( {{q}_{1},{q}_{2}}\right) \) .)

(3) For each \( q \in  W \) the map \( {\exp }_{q} \) maps the open \( \varepsilon \) -ball in \( T{M}_{q} \) diffeomorphically onto an open set \( {U}_{q} \supset  W \) .

Remark. With more care it would be possible to choose \( W \) so that the geodesic joining any two of its points lies completely within \( W \) . Compare [Whi32].

Now let us study the relationship between geodesics and arc-length.

Theorem 10.6. Let \( W \) and \( \varepsilon \) be as in Lemma 10.5. Let

\[
\gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

be the geodesic of length \( < \varepsilon \) joining two points of \( W \) , and let

\[
\omega  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

be any other piecewise smooth path joining the same two points. Then,

\[
{\int }_{0}^{1}\begin{Vmatrix}\frac{\mathrm{d}\gamma }{\mathrm{d}t}\end{Vmatrix}\mathrm{d}t \leq  {\int }_{0}^{1}\begin{Vmatrix}\frac{\mathrm{d}\omega }{\mathrm{d}t}\end{Vmatrix}\mathrm{d}t
\]

where equality can hold only if the point set \( \omega \left( \left\lbrack  {o,1}\right\rbrack  \right) \) coincides with \( \gamma \left( \left\lbrack  {0,1}\right\rbrack  \right) \) .

Thus \( \gamma \) is the shortest path joining its end points.

The proof will be based on two lemmas. Let \( q = y\left( 0\right) \) and let \( {U}_{q} \) be as in Lemma 10.5.

Lemma 10.7. In \( {U}_{q} \) , the geodesics through \( q \) are the orthogonal trajectories of hypersurfaces

\[
\left\{  {{\exp }_{q}\left( v\right)  : v \in  T{M}_{q},\;\parallel v\parallel  = \text{ constant }}\right\}  .
\]

Proof. Let \( t \mapsto  v\left( t\right) \) denote any curve in \( T{M}_{q} \) with \( \parallel v\left( t\right) \parallel  = 1 \) . We must show that the corresponding curves

\[
t \mapsto  {\exp }_{q}\left( {{r}_{0}v\left( t\right) }\right)
\]

in \( {U}_{q} \) , where \( 0 < {r}_{0} < \varepsilon \) , are orthogonal to the radial geodesics

\[
t \mapsto  {\exp }_{q}\left( {{rv}\left( {t}_{0}\right) }\right) .
\]

In terms of the parametrized surface \( f \) given by

\[
f\left( {r, t}\right)  = {\exp }_{q}\left( {{rv}\left( t\right) }\right) ,\;0 \leq  r < \varepsilon ,
\]

we must prove that

\[
\left\langle  {\frac{\partial f}{\partial r},\frac{\partial f}{\partial t}}\right\rangle   = 0
\]

for all \( \left( {r, t}\right) \) .

Now

\[
\frac{\partial }{\partial r}\left\langle  {\frac{\partial f}{\partial r},\frac{\partial f}{\partial t}}\right\rangle   = \left\langle  {\frac{\mathrm{D}}{\partial r}\frac{\partial f}{\partial r},\frac{\partial f}{\partial t}}\right\rangle   + \left\langle  {\frac{\partial f}{\partial r},\frac{\mathrm{D}}{\partial r}\frac{\partial f}{\partial t}}\right\rangle  .
\]

The first expression on the right is zero since the curves

\[
r \mapsto  f\left( {r, t}\right)
\]

are geodesics. The second expression is equal to

\[
\left\langle  {\frac{\partial f}{\partial r},\frac{\mathrm{D}}{\partial r}\frac{\partial f}{\partial t}}\right\rangle   = \frac{1}{2}\frac{\partial }{\partial t}\left\langle  {\frac{\partial f}{\partial r},\frac{\partial f}{\partial r}}\right\rangle   = 0,
\]

since \( \begin{Vmatrix}\frac{\partial f}{\partial r}\end{Vmatrix} = \parallel v\left( t\right) \parallel  = 1 \) . Therefore the quantity \( \left\langle  {\frac{\partial f}{\partial r},\frac{\partial f}{\partial t}}\right\rangle \) is independent of \( r \) . But for \( r = 0 \) we have

\[
f\left( {0, t}\right)  = {\exp }_{q}\left( o\right)  = q
\]

hence \( \frac{\partial f}{\partial t}\left( {0, t}\right)  = 0 \) . Therefore \( \left\langle  {\frac{\partial f}{\partial r},\frac{\partial f}{\partial t}}\right\rangle \) is identically zero, which completes the proof.

Now consider any piecewise smooth curve

\[
\omega  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {U}_{q} - \{ q\} .
\]

Each point \( \omega \left( t\right) \) can be expressed uniquely in the form \( {\exp }_{q}\left( {r\left( t\right) v\left( t\right) }\right) \) with \( 0 < \; r\left( t\right)  < \varepsilon \) , and \( \parallel v\left( t\right) \parallel  = 1, v\left( t\right)  \in  T{M}_{q} \) .

Lemma 10.8. The length \( {\int }_{a}^{b}\parallel \mathrm{\;d}\omega /\mathrm{d}t\parallel \mathrm{d}t \) is greater than or equal to \( \left| {r\left( b\right)  - r\left( a\right) }\right| \) , where equality holds only if the function \( r\left( t\right) \) is monotone, and the function \( v\left( t\right) \) is constant.

Thus the shortest path joining two concentric spherical shells around \( q \) is a radial geodesic.

Proof. Let \( f\left( {r, t}\right)  = {\exp }_{q}\left( {{rv}\left( t\right) }\right) \) , so that \( \omega \left( t\right)  = f\left( {r\left( t\right) , t}\right) \) . Then

\[
\frac{\mathrm{d}\omega }{\mathrm{d}t} = \frac{\partial f}{\partial r}{r}^{\prime }\left( t\right)  + \frac{\partial f}{\partial t}.
\]

Since the two vectors on the right are mutually orthogonal, and since \( \begin{Vmatrix}\frac{\partial f}{\partial t}\end{Vmatrix} = 1 \) , this gives

\[
\parallel \frac{\mathrm{d}\omega }{\mathrm{d}t}{\parallel }^{2} = {\left| {r}^{\prime }\left( t\right) \right| }^{2} + {\begin{Vmatrix}\frac{\partial f}{\partial t}\end{Vmatrix}}^{2} \geq  {\left| {r}^{\prime }\left( t\right) \right| }^{2}
\]

where equality holds only if \( \frac{\partial f}{\partial t} = 0 \) ; hence only if \( \frac{\partial v}{\partial t} = 0 \) . Thus

\[
{\int }_{a}^{b}\begin{Vmatrix}\frac{\mathrm{d}\omega }{\mathrm{d}t}\end{Vmatrix}\mathrm{d}t \geq  {\int }_{a}^{b}{\left| {r}^{\prime }\left( t\right) \right| }^{2}\mathrm{\;d}t \geq  \left| {r\left( b\right)  - r\left( a\right) }\right|
\]

where equality holds only if \( r\left( t\right) \) is monotone and \( v\left( t\right) \) is constant. This completes the proof.

The proof of Theorem 10.6 is now straightforward. Consider any piecewise smooth path \( \omega \) from \( q \) to a point

\[
{q}^{\prime } = {\exp }_{q}\left( {rv}\right)  \in  {U}_{q};
\]

where \( 0 < r < \varepsilon ,\parallel v\parallel  = 1 \) . Then for any \( \delta  > 0 \) the path \( \omega \) must contain a segment joining the spherical shell of radius \( \delta \) to the spherical shell of radius \( r \) , and lying between these two shells. The length of this segment will be \( \geq  r - \delta \) ; hence letting \( \delta \) tend to 0 the length of \( \omega \) will be \( \geq  r \) . If \( \omega \left( \left\lbrack  {0,1}\right\rbrack  \right) \) does not coincide with \( \gamma \left( \left\lbrack  {0,1}\right\rbrack  \right) \) , then we easily obtain a strict inequality. This completes the proof of Theorem 10.6.

An important consequence of Theorem 10.6 is the following.

Corollary 10.9. Suppose that a path \( \omega  : \left\lbrack  {0,\ell }\right\rbrack   \rightarrow  M \) , parametrized by arc-length, has length less than or equal to the length of any other path from \( \omega \left( 0\right) \) to \( \omega \left( \ell \right) \) . Then \( \omega \) is a geodesic.

Proof. Consider any segment of \( \omega \) lying within an open set \( W \) , as above, and having length \( < \varepsilon \) . This segment must be a geodesic by Theorem 10.6. Hence the entire path \( \omega \) is a geodesic.

Definition 10.10. A geodesic \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) will be called minimal if its length is less than or equal to the length of any other piecewise smooth path joining its endpoints.

Theorem 10.6 asserts that any sufficiently small segment of a geodesic is minimal. On the other hand a long geodesic may not be minimal. For example we will see shortly that a great circle arc on the unit sphere is a geodesic. If such an arc has length greater than \( \pi \) , it is certainly not minimal.

In general, minimal geodesics are not unique. For example two antipodal points on a unit sphere are joined by infinitely many minimal geodesics. However, the following assertion is true.

Define the distance \( \rho \left( {p, q}\right) \) between two points \( p, q \in  M \) to be the greatest lower bound for the arc-lengths of piecewise smooth paths joining these points. This clearly makes \( M \) into a metric space. It follows easily from Theorem 10.6 that this metric is compatible with the usual topology of \( M \) .

Corollary 10.11. Given a compact set \( K \subset  M \) there exists a number \( \delta  > 0 \) so that any two points of \( K \) with distance less than \( \delta \) are joined by a unique geodesic of length less than \( \delta \) . Furthermore this geodesic is minimal; and depends differentiably on its endpoints.

Proof. Cover \( K \) by open sets \( {W}_{\alpha } \) , as in Lemma 10.5, and let \( \delta \) be small enough so that any two points in \( K \) with distance less than \( \delta \) lie in a common \( {W}_{\alpha } \) . This completes the proof.

Recall that the manifold \( \mathrm{M} \) is geodesically complete if every geodesic segment can be extended indefinitely.

Theorem 10.12 (Hopf and Rinow \( {}^{2} \) ). If \( M \) is geodesically complete, then any two points can be joined by a minimal geodesic.

Proof. Given \( p, q \in  M \) with distance \( r > 0 \) , choose a neighborhood \( {U}_{p} \) as in Lemma 10.5. Let \( S \subset  {U}_{p} \) denote a spherical shell of radius \( \delta  < \varepsilon \) about \( p \) . Since \( S \) is compact, there exists a point

\[
{p}_{0} = {\exp }_{p}\left( {\delta v}\right) ,\;\parallel v\parallel  = 1,
\]

on \( S \) for which the distance to \( q \) is minimized. We will prove that

\[
{\exp }_{p}\left( {rv}\right)  = q
\]

This implies that the geodesic segment \( t \mapsto  \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) ,0 \leq  t \leq  r \) , is actually a minimal geodesic from \( p \) to \( q \) .

---

\( {}^{2} \) Compare [DR52, p. 341]; as well as [HR31].

---

The proof will amount to showing that a point which moves along the geodesic \( \gamma \) must get closer and closer to \( q \) . In fact for each \( t \in  \left\lbrack  {\delta , r}\right\rbrack \) we will prove that

\[
\rho \left( {\gamma \left( t\right) , q}\right)  = r - t.
\]

\( \left( {1}_{t}\right) \)

This identity, for \( t = r \) , will complete the proof.

First we will show that the equality \( \left( {1}_{t}\right) \) is true. Since every path from \( p \) to \( q \) must pass through \( S \) , we have

\[
\rho \left( {p, q}\right)  = \mathop{\min }\limits_{{s \in  S}}\left( {\rho \left( {p, s}\right)  + \rho \left( {s, q}\right) }\right)  = \delta  + \rho \left( {{p}_{0}, q}\right) .
\]

Therefore \( \rho \left( {{p}_{0}, q}\right)  = r - \delta \) . Since \( {p}_{0} = \gamma \left( \delta \right) \) , this proves \( \left( {1}_{t}\right) \) .

Let \( {t}_{0} \in  \left\lbrack  {\delta , r}\right\rbrack \) denote the supremum of those numbers \( t \) for which \( \left( {1}_{t}\right) \) is true. Then by continuity the equality \( \left( {1}_{{t}_{0}}\right) \) is true also. If \( {t}_{0} < r \) we will obtain a contradiction. Let \( {S}^{\prime } \) denote a small spherical shell of radius \( {\delta }^{\prime } \) about the point \( \gamma \left( {t}_{0}\right) \) ; and let \( {p}_{0}^{\prime } \in  {S}^{\prime } \) be a point of \( {S}^{\prime } \) with minimum distance from \( q \) . (Compare Figure 10.1.)

![bo_d7du90alb0pc73deir8g_64_366_890_911_434_0.jpg](images/bo_d7du90alb0pc73deir8g_64_366_890_911_434_0.jpg)

Figure 10.1

Then

\[
\rho \left( {\gamma \left( {t}_{0}\right) , q}\right)  = \mathop{\min }\limits_{{s \in  {S}^{\prime }}}\left( {\rho \left( {\gamma \left( {t}_{0}\right) , s}\right)  + \rho \left( {s, q}\right) }\right)  = {\delta }^{\prime } + \rho \left( {{p}_{0}^{\prime }, q}\right) ,
\]

hence

\[
\rho \left( {{p}_{0}^{\prime }, q}\right)  = \left( {r - {t}_{0}}\right)  - {\delta }^{\prime }. \tag{10.1}
\]

We claim that \( {p}_{0} \) is equal to \( \gamma \left( {{t}_{0} + {\delta }^{\prime }}\right) \) . In fact the triangle inequality states that

\[
\rho \left( {p,{p}_{0}^{\prime }}\right)  \geq  \rho \left( {p, q}\right)  - \rho \left( {{p}_{0}^{\prime }, q}\right)  = {t}_{0} + {\delta }^{\prime }
\]

(making use of (10.1)). But a path of length precisely \( {t}_{0} + {\delta }^{\prime } \) from \( p \) to \( {p}_{0}^{\prime } \) is obtained by following \( \gamma \) from \( p \) to \( \gamma \left( {t}_{0}\right) \) , and then following a minimal geodesic from \( \gamma \left( {t}_{0}\right) \) to \( {p}_{0}^{\prime } \) . Since this broken geodesic has minimal length, it follows from Corollary 10.9 that it is an (unbroken) geodesic, and hence coincides with \( \gamma \) .

Thus \( \gamma \left( {{t}_{0} + {\delta }^{\prime }}\right)  = {p}_{0}^{\prime } \) . Now the equality (10.1) becomes

\[
\rho \left( {\gamma \left( {{t}_{0} + {\delta }^{\prime }}\right) , q}\right)  = r - \left( {{t}_{0} + {\delta }^{\prime }}\right) .
\]

\( \left( {1}_{{t}_{0} + {\delta }^{\prime }}\right) \)

This contradicts the definition of \( {t}_{0} \) ; and completes the proof.

As a consequence one has the following.

Corollary 10.13. If \( M \) is geodesically complete then every bounded subset of \( M \) has compact closure. Consequently \( M \) is complete as a metric space (i.e., every Cauchy sequence converges).

Proof. If \( X \subset  M \) has diameter \( d \) then for any \( p \in  X \) the map \( {\exp }_{p} : T{M}_{p} \rightarrow  M \) maps the disk of radius \( d \) in \( T{M}_{p} \) onto a compact subset of \( M \) which (making use of Theorem 10.12) contains \( X \) . Hence the closure of \( X \) is compact.

Conversely, if \( M \) is complete as a metric space, then it is not difficult, using Lemma 10.5, to prove that \( M \) is geodesically complete. For details the reader is referred to Hopf and Rinow. Henceforth we will not distinguish between geodesic completeness and metric completeness, but will refer simply to a complete Riemannian manifold.

FAMILIAR EXAMPLES OF GEODESICS. In Euclidean \( n \) -space, \( {\mathbf{R}}^{n} \) , with the usual coordinate system \( {x}_{1},\ldots ,{x}_{n} \) and the usual Riemannian metric \( \mathrm{d}{x}_{1} \otimes  \mathrm{d}{x}_{1} + \cdots  + \; \mathrm{d}{x}_{n} \otimes  \mathrm{d}{x}_{n} \) we have \( {\Gamma }_{ij}^{k} = 0 \) and the equations for a geodesic \( \gamma \) , given by \( t \mapsto \; \left( {{x}_{1}\left( t\right) ,\ldots ,{x}_{n}\left( t\right) }\right) \) become

\[
\frac{{\mathrm{d}}^{2}{x}_{i}}{\mathrm{\;d}{t}^{2}} = 0
\]

whose solutions are the straight lines. This could also have been seen as follows: it is easy to show that the formula for arc length

\[
\int {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( \mathrm{\;d}{x}_{i}/\mathrm{d}t\right) }^{2}\right) }^{\frac{1}{2}}\mathrm{\;d}t
\]

coincides with the usual definition of arc length as the least upper bound of the lengths of inscribed polygons; from this definition it is clear that straight lines have minimal length, and are therefore geodesics.

The geodesics on \( {\mathbb{S}}^{n} \) are precisely the great circles, that is, the intersections of \( {\mathbb{S}}^{n} \) with the planes through the center of \( {\mathbb{S}}^{n} \) .

Proof. Reflection through a plane \( {E}^{2} \) is an isometry \( I : {\mathbb{S}}^{n} \rightarrow  {\mathbb{S}}^{n} \) whose fixed point set is \( C = {\mathbb{S}}^{n} \cap  {E}^{2} \) . Let \( x \) and \( y \) be two points of \( C \) with a unique geodesic \( {C}^{\prime } \) of minimal length between them. Then, since \( I \) is an isometry, the curve \( I\left( {C}^{\prime }\right) \) is a geodesic of the same length as \( {C}^{\prime } \) between \( I\left( x\right)  = x \) and \( I\left( y\right)  = y \) . Therefore \( {C}^{\prime } = I\left( {C}^{\prime }\right) \) . This implies that \( {C}^{\prime } \subset  C \) .

Finally, since there is a great circle through any point of \( {\mathbb{S}}^{n} \) in any given direction, these are all the geodesics.

Antipodal points on the sphere have a continium of geodesics of minimal length between them. All other pairs of points have a unique geodesic of minimal length between them, but an infinite family of non-minimal geodesics, depending on how many times the geodesic goes around the sphere and in which direction it starts.

By the same reasoning every meridian line on a surface of revolution is a geodesic.

The geodesics on a right circular cylinder \( Z \) are the generating lines, the circles cut by planes perpendicular to the generating lines, and the helices on \( Z \) .

![bo_d7du90alb0pc73deir8g_66_721_201_213_422_0.jpg](images/bo_d7du90alb0pc73deir8g_66_721_201_213_422_0.jpg)

Proof. If \( L \) is a generating line of \( Z \) then we can set up an isometry \( I : Z - L \rightarrow  {\mathbf{R}}^{2} \) by rolling \( Z \) onto \( {\mathbf{R}}^{2} \) :

![bo_d7du90alb0pc73deir8g_66_369_781_920_420_0.jpg](images/bo_d7du90alb0pc73deir8g_66_369_781_920_420_0.jpg)

The geodesics on \( Z \) are just the images under \( {I}^{-1} \) of the straight lines in \( {\mathbf{R}}^{2} \) Two points on \( Z \) have infinitely many geodesics between them.

## Part III The Calculus of Variations Applied to Geodesics
