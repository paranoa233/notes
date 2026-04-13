# Chapter 21 Lie Groups as Symmetric Spaces

Based on lecture notes by

M. Spivak and R. Wells

In this section we consider a Lie group \( G \) with a Riemannian metric which is invariant both under left translations

\[
\begin{array}{l} {L}_{\tau } : G \rightarrow  G, \\  {L}_{\tau }\left( \sigma \right)  = {\tau \sigma } \end{array}
\]

and right translation, \( {R}_{\tau }\left( \sigma \right)  = {\sigma \tau } \) . If \( G \) is commutative such a metric certainly exists. If \( G \) is compact then such a metric can be constructed as follows: Let \( \langle \) , \( \rangle \) be any Riemannian metric on \( G \) , and Let \( \mu \) denote the Haar measure on \( G \) . Then \( \nu \) is right and left invariant. Define a new inner product \( \langle \langle ,\rangle \rangle \) on \( G \) by

\[
\langle \langle V, W\rangle \rangle  = {\int }_{G \times  G}\left\langle  {{L}_{\sigma  * }{R}_{\tau  * }\left( V\right) ,{L}_{\sigma  * }{R}_{\tau  * }\left( W\right) }\right\rangle  \mathrm{d}\mu \left( \sigma \right) \mathrm{d}\mu \left( \tau \right) .
\]

Then \( \langle \langle ,\rangle \rangle \) is left and right invariant.

Lemma 21.1. If \( G \) is a Lie group with a left and right invariant metric, then \( G \) is a symmetric space. The reflection \( {I}_{\tau } \) in any point \( \tau  \in  G \) is given by the formula \( {I}_{\tau }\left( \sigma \right)  = \tau {\sigma }^{-1}\tau . \)

Proof. By hypothesis \( {L}_{\tau } \) and \( {R}_{\tau } \) are isometries. Define a map \( {I}_{e} : G \rightarrow  G \) by

\[
{I}_{e}\left( \sigma \right)  = {\sigma }^{-1}.
\]

Then \( {I}_{e * } : T{G}_{e} \rightarrow  T{G}_{e} \) reverses the tangent space of \( e \) ; so is certainly an isometry on this tangent space. Now the identity

\[
{I}_{e}\left( \sigma \right)  = {R}_{{\sigma }^{-1}}{I}_{e}{L}_{{\sigma }^{-1}}
\]

shows that \( {I}_{e * } : T{G}_{\sigma } \rightarrow  T{G}_{{\sigma }^{-1}} \) is an isometry for any \( \sigma  \in  G \) . Since \( {I}_{e} \) reverses the tangent space at \( e \) , it reverses geodesics through \( e \) .

Finally, defining \( {I}_{\tau }\left( \sigma \right)  = \tau {\sigma }^{-1}\tau \) , the identity \( {I}_{\tau } = {R}_{\tau }{I}_{e}{R}_{\tau }^{-1} \) shows that each \( {I}_{\tau } \) is an isometry which reverses geodesics through \( \tau \) .

A 1-parameter subgroup of \( G \) is a \( {C}^{\infty } \) homomorphism of \( \mathbf{R} \) into \( G \) . It is well known that a 1-parameter subgroup of \( G \) is determined by its tangent vector at \( e \) . (Compare Chevalley, "Theory of Lie Groups," Princeton, 1946.)

Lemma 21.2. The geodesics \( \gamma \) in \( G \) with \( \gamma \left( 0\right)  = e \) are precisely the one-parameter subgroups of \( G \) .

Proof. Let \( \gamma  : \mathbf{R} \rightarrow  G \) be a geodesic with \( \gamma \left( 0\right)  = e \) . By Lemma 20.1 the map \( {I}_{\gamma \left( t\right) }{I}_{e} \) takes \( \gamma \left( u\right) \) into \( \gamma \left( {u + {2t}}\right) \) . Now \( {I}_{\gamma \left( t\right) }{I}_{e}\left( \sigma \right)  = \gamma \left( t\right) {\sigma \gamma }\left( t\right) \) so \( \gamma \left( t\right) \gamma \left( u\right) \gamma \left( t\right)  = \gamma \left( {u + {2t}}\right) \) . By induction it follows that \( \gamma \left( {nt}\right)  = \gamma {\left( t\right) }^{n} \) for any integer \( n \) . If \( {t}^{\prime }/t \) " is rational so that \( {t}^{\prime } = {n}^{\prime }t \) and \( {t}^{\prime \prime } = {n}^{\prime \prime }t \) for some \( t \) and some integers \( {n}^{\prime } \) and \( {n}^{\prime \prime } \) then \( \gamma \left( {{t}^{\prime } + {t}^{\prime \prime }}\right)  = \; \gamma {\left( t\right) }^{{n}^{\prime } + {n}^{\prime \prime }} = \gamma \left( {t}^{\prime }\right) \gamma \left( {t}^{\prime \prime }\right) \) . By continuity \( \gamma \) is a homomorphism.

Now let \( \gamma  : \mathbf{R} \rightarrow  G \) be a 1-parameter subgroup. Let \( {\gamma }^{\prime } \) be the geodesic through \( e \) such that the tangent vector of \( {\gamma }^{\prime } \) at \( e \) is the tangent vector of \( \gamma \) at \( e \) . We have just seen that \( {\gamma }^{\prime } \) is a 1-parameter subgroup. Hence \( {\gamma }^{\prime } = \gamma \) . This completes the proof.

A vector field \( X \) on a Lie group \( G \) is called left invariant if and only if \( {\left( {L}_{a}\right) }_{ * }\left( {X}_{b}\right)  = \; {X}_{a \cdot  b} \) for every \( a \) and \( b \) in \( G \) . If \( X \) and \( Y \) are left invariant then \( \left\lbrack  {X, Y}\right\rbrack \) is also. The Lie algebra \( \mathfrak{g} \) of \( G \) is the vector space of all left invariant vector fields, made into an algebra by the bracket [,].

\( \mathfrak{g} \) is actually a Lie algebra because the Jacobi identity

\[
\left\lbrack  {\left\lbrack  {X, Y}\right\rbrack  , Z}\right\rbrack   + \left\lbrack  {\left\lbrack  {Y, Z}\right\rbrack  , X}\right\rbrack   + \left\lbrack  {\left\lbrack  {Z, X}\right\rbrack  , Y}\right\rbrack   = 0
\]

holds for all (not necessarily left invariant) vector fields \( X, Y \) and \( Z \) .

Theorem 21.3. Let \( G \) be a Lie group with a left and right invariant Riemannian metric. If \( X, Y, Z \) and \( W \) are left invariant vector fields on \( G \) then:

(a) \( \langle \left\lbrack  {X, Y}\right\rbrack  , Z\rangle  = \langle X,\left\lbrack  {Y, Z}\right\rbrack  \rangle \)

(b) \( \mathcal{R}\left( {X, Y}\right) Z = \frac{1}{4}\left\lbrack  {\left\lbrack  {X, Y}\right\rbrack  , Z}\right\rbrack \)

(c) \( \langle \mathcal{R}\left( {X, Y}\right) Z, W\rangle  = \frac{1}{4}\langle \left\lbrack  {X, Y}\right\rbrack  ,\left\lbrack  {Z, W}\right\rbrack  \rangle \) .

Proof. As in chapter 8 we will use the notation \( X \vdash  Y \) for the covariant derivative of \( Y \) in the direction \( X \) . For any left invariant \( X \) the identity

\[
X \vdash  X = 0
\]

is satisfied, since the integral curves of \( X \) are left translates of 1-parameter subgroups, and therefore are geodesics. Therefore

\[
\left( {X + Y}\right)  \vdash  \left( {X + Y}\right)  = \left( {X \vdash  X}\right)  + \left( {X \vdash  Y}\right)  + \left( {Y \vdash  X}\right)  + \left( {Y \vdash  Y}\right)
\]

is zero; hence

\[
X \vdash  Y + Y \vdash  X = 0.
\]

On the other hand

\[
X \vdash  Y - Y \vdash  X = \left\lbrack  {X, Y}\right\rbrack
\]

by Definition 8.7. Adding these two equations we obtain:

(d) \( {2X} \vdash  Y = \left\lbrack  {X, Y}\right\rbrack \) .

Now recall the identity

\[
Y\langle X, Z\rangle  = \langle Y \vdash  X, Z\rangle  + \langle X, Y \vdash  Z\rangle .
\]

(See Corollary 8.6.) The left side of this equation is zero, since \( \langle X, Z\rangle \) is constant. Substituting formula 21 in this equation we obtain

\[
0 = \langle \left\lbrack  {Y, X}\right\rbrack  , Z\rangle  + \langle X,\left\lbrack  {Y, Z}\right\rbrack  \rangle .
\]

Finally, using the skew commutativity of \( \left\lbrack  {Y, X}\right\rbrack \) , we obtain the required formula \( {}^{1} \)

\[
\langle \left\lbrack  {X, Y}\right\rbrack  , Z\rangle  = \langle X,\left\lbrack  {Y, Z}\right\rbrack  \rangle \tag{a}
\]

By definition, \( \mathcal{R}\left( {X, Y}\right) Z \) is equal to

\[
- X \vdash  \left( {Y \vdash  Z}\right)  + Y \vdash  \left( {X \vdash  Z}\right)  + \left\lbrack  {X, Y}\right\rbrack   \vdash  Z.
\]

Substituting formula 21, this becomes

\[
- \frac{1}{4}\left\lbrack  {X,\left\lbrack  {Y, Z}\right\rbrack  }\right\rbrack   + \frac{1}{4}\left\lbrack  {Y,\left\lbrack  {X, Z}\right\rbrack  }\right\rbrack   + \frac{1}{2}\left\lbrack  {\left\lbrack  {X, Y}\right\rbrack  , Z}\right\rbrack
\]

Using the Jacobi identity, this yields the required formula

\[
\mathcal{R}\left( {X, Y}\right) Z = \frac{1}{4}\left\lbrack  {\left\lbrack  {X, Y}\right\rbrack  , Z}\right\rbrack \tag{b}
\]

The formula (c) follows from (a) and (b).

Corollary 21.4. The sectional curvature \( \langle \mathcal{R}\left( {X, Y}\right) X, Y\rangle  = \frac{1}{4}\langle \left\lbrack  {X, Y}\right\rbrack  ,\left\lbrack  {X, Y}\right\rbrack  \rangle \) is always \( \geq  0 \) . Equality holds if and only if \( \left\lbrack  {X, Y}\right\rbrack   = 0 \) .

Recall that the center \( c \) of a Lie algebra \( \mathfrak{g} \) is defined to be the set of \( X \in  \mathfrak{g} \) such that \( \left\lbrack  {X, Y}\right\rbrack   = 0 \) for all \( Y \in  \mathfrak{g} \) .

Corollary 21.5. If \( G \) has a left and right invariant metric, and if the Lie algebra \( \mathfrak{g} \) has trivial center, then \( G \) is compact, with finite fundamental group.

Proof. This follows from Myers’ theorem (Theorem 19.5). Let \( {X}_{1} \) be any unit vector in \( \mathrm{g} \) and extend to a orthonormal basis \( {X}_{1},\ldots ,{X}_{n} \) . The Ricci curvature

\[
K\left( {{X}_{1},{X}_{1}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\left\langle  {\mathcal{R}\left( {{X}_{1},{X}_{i}}\right) {X}_{1},{X}_{i}}\right\rangle
\]

must be strictly positive, since \( \left\lbrack  {{X}_{1},{X}_{i}}\right\rbrack   \neq  0 \) for some \( i \) . Furthermore \( K\left( {{X}_{1},{X}_{1}}\right) \) is bounded away from zero, since the unit sphere in \( \mathfrak{g} \) is compact. Therefore, by Corollary 19.7, the manifold \( G \) is compact.

This result can be sharpened slightly as follows.

Corollary 21.6. A simply connected Lie group \( G \) with left and right invariant metric splits as a Cartesian product \( {G}^{\prime } \times  {\mathbf{R}}^{k} \) where \( {G}^{\prime } \) is compact and \( {\mathbf{R}}^{k} \) denotes the additive Lie group of some Euclidean space. Furthermore, the Lie algebra of \( {G}^{\prime } \) has trivial center.

---

\( {}^{1} \) It follows that the tri-linear function \( X, Y, Z \mapsto  \langle \left\lbrack  {X, Y}\right\rbrack  , Z\rangle \) is skew-symmetric in all three variables. Thus one obtains a left invariant differential 3-form on \( G \) , representing an element of the de Rham cohomology group \( {\mathrm{H}}^{3}\left( G\right) \) . In this way Cartan was able to prove that \( {\mathrm{H}}^{3}\left( G\right)  \neq  0 \) if \( G \) is a non-abelian compact connected Lie group. (See E. Cartan,"La Topologie des Espaces Représentatives des Groupes de Lie," Paris, Hermann, 1936.)

---

Conversely it is clear that any such product \( {G}^{\prime } \times  {\mathbf{R}}^{k} \) possesses a left and right invariant metric.

Proof. Let \( c \) be the center of the Lie algebra \( \mathfrak{g} \) and let

\[
{\mathfrak{g}}^{\prime } = \{ X \in  \mathfrak{g} : \langle X, C\rangle  = 0\text{ for all }C \in  c\}
\]

be the orthogonal complement of \( c \) . Then \( {\mathfrak{g}}^{\prime } \) is a Lie sub-algebra. For if \( X, Y \in  {\mathfrak{g}}^{\prime } \) and \( C \in  c \) then

\[
\langle \left\lbrack  {X, Y}\right\rbrack  , C\rangle  = \langle X,\left\lbrack  {Y, C}\right\rbrack  \rangle  = 0;
\]

hence \( \left\lbrack  {X, Y}\right\rbrack   \in  {g}^{\prime } \) . It follows that \( \mathfrak{g} \) splits as a direct sum \( {\mathfrak{g}}^{\prime } \oplus  c \) of Lie algebras. Hence \( G \) splits as a Cartesian product \( {G}^{\prime } \times  {G}^{\prime \prime } \) ; where \( {G}^{\prime } \) is compact by Corollary 21.5 and \( {G}^{\prime \prime } \) is simply connected and abelian, hence isomorphic to some \( {\mathbf{R}}^{k} \) . (See Chevalley, "Theory of Lie Groups.") This completes the proof.

Theorem 21.7 (Bott). Let \( G \) be a compact, simply connected Lie group. Then the loop space \( \Omega \left( G\right) \) has the homotopy type of a \( {CW} \) -complex with no odd dimensional cells, and with only finitely many \( \lambda \) -cells for each even value of \( \lambda \) .

Thus the \( \lambda \) -th homology groups of \( \Omega \left( G\right) \) is zero for \( \lambda \) odd, and is free abelian of finite rank for \( \lambda \) even.

Remark. This CW-complex will always be infinite dimensional. As an example, if \( G \) is the group \( {\mathbb{S}}^{3} \) of unit quaternions, then we have seen that the homology group \( {\mathrm{H}}_{i}\Omega \left( {\mathbb{S}}^{3}\right) \) is infinite cyclic for all even values of \( i \) .

Remark. This theorem remains true even for a non-compact group. In fact any connected Lie group contains a compact subgroup as deformation retract. (See [Iwa49, Theorem 6])

Proof of Theorem 21.7. Choose two points \( p \) and \( q \) in \( G \) which are not conjugate along any geodesic. By Theorem 17.3, \( \Omega \left( {G;p, q}\right) \) has the homotopy type of a CW-complex with one cell of dimension \( \lambda \) for each geodesic from \( p \) to \( q \) of index \( \lambda \) . By Theorem 19.5 there are only finitely many \( \lambda \) -cells for each \( \lambda \) . Thus it only remains to prove that the index \( \lambda \) of a geodesic is always even.

Consider a geodesic \( \gamma \) starting at \( p \) with velocity vector

\[
V = \frac{\mathrm{d}\gamma }{\mathrm{d}t}\left( 0\right)  \in  T{G}_{p} \cong  \mathfrak{g}.
\]

According to Theorem 20.5 the conjugate points of \( p \) on \( \gamma \) are determined by the eigenvalues of the linear transformation

\[
{K}_{V} : T{G}_{p} \rightarrow  T{G}_{p}
\]

defined by

\[
{K}_{V}\left( W\right)  = \mathcal{R}\left( {V, W}\right) V = \frac{1}{4}\left\lbrack  {\left\lbrack  {V, W}\right\rbrack  , V}\right\rbrack  .
\]

Defining the adjoint homomorphism

\[
\text{ Ad }V : \mathfrak{g} \rightarrow  \mathfrak{g}
\]

by

\[
\text{ Ad }V\left( W\right)  = \left\lbrack  {V, W}\right\rbrack
\]

we have

\[
{K}_{V} =  - \frac{1}{4}\left( {\operatorname{Ad}V}\right)  \circ  \left( {\operatorname{Ad}V}\right) .
\]

The linear transformation Ad \( V \) is skew-symmetric; that is

\[
\left\langle  {\operatorname{Ad}V\left( W\right) ,{W}^{\prime }}\right\rangle   =  - \langle W,\operatorname{Ad}V\left( {W}^{\prime }\right) \rangle .
\]

This follows immediately from the identity 21.3-(a). Therefore we can choose an orthonormal basis for \( \mathfrak{g} \) so that the matrix of Ad \( V \) takes the form

\[
\left( \begin{matrix} 0 & {a}_{1} & & & \\   - {a}_{1} & 0 & & & \\   & 0 & {a}_{2} & & \\   & &  - {a}_{2} & 0 & \\   & & & &  \ddots   \end{matrix}\right)
\]

It follows that the composite linear transformation \( \left( {\operatorname{Ad}V}\right)  \circ  \left( {\operatorname{Ad}V}\right) \) has matrix

\[
\left( \begin{array}{lllll}  - {a}_{1}^{2} & & & & \\   &  - {a}_{1}^{2} & & & \\   & &  - {a}_{2}^{2} & & \\   & & &  - {a}_{2}^{2} & \\   & & & &  \ddots   \end{array}\right)
\]

Therefore the non-zero eigenvalues of \( {K}_{V} =  - \frac{1}{4}{\left( \operatorname{Ad}V\right) }^{2} \) are positive, and occur in pairs.

It follows from Theorem 20.5 that the conjugate points of \( p \) along \( \gamma \) also occur in pairs. In other words every conjugate point has even multiplicity. Together with the Index Theorem, this implies that the index \( \lambda \) of any geodesic from \( p \) to \( q \) is even. This completes the proof.
