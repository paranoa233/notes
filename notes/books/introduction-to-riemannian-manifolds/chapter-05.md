## Chapter 5 The Levi-Civita Connection

If we are to use geodesics and covariant derivatives as tools for studying Riemannian geometry, it is evident that we need a way to single out a particular connection on a Riemannian manifold that reflects the properties of the metric. In this chapter, guided by the example of the tangential connection on a submanifold of \( {\mathbb{R}}^{n} \) , we describe two properties that determine a unique connection on every Riemannian manifold. The first property, compatibility with the metric, is easy to motivate and understand. The second, symmetry, is a bit more mysterious; but it is motivated by the fact that it is invariantly defined, and is always satisfied by the tangential connection. It turns out that these two conditions are enough to determine a unique connection associated with any Riemannian or pseudo-Riemannian metric, called the Levi-Civita connection after the early twentieth-century Italian differential geometer Tullio Levi-Civita.

After defining the Levi-Civita connection, we investigate the exponential map, which conveniently encodes the collective behavior of geodesics and allows us to study how they change as the initial point and initial velocity vary. Having established the properties of this map, we introduce normal neighborhoods and normal coordinates, which are essential computational and theoretical tools for studying local geometric properties near a point. Then we introduce the analogous notion for studying properties near a submanifold: tubular neighborhoods and Fermi coordinates. Finally, we return to our three main model Riemannian manifolds and determine their geodesics.

Except where noted otherwise, the results and proofs of this chapter do not use positivity of the metric, so they apply equally well to Riemannian and pseudo-Riemannian manifolds.

## The Tangential Connection Revisited

We are eventually going to show that on each Riemannian manifold there is a natural connection that is particularly well suited to computations in Riemannian geometry. Since we get most of our intuition about Riemannian manifolds from studying submanifolds of \( {\mathbb{R}}^{n} \) with the induced metric, let us start by examining that case.

Let \( M \subseteq  {\mathbb{R}}^{n} \) be an embedded submanifold. As a guiding principle, consider the idea mentioned at the beginning of Chapter 4: a geodesic in \( M \) should be "as straight as possible." A reasonable way to make this rigorous is to require that the geodesic have no acceleration in directions tangent to the manifold, or in other words that its acceleration vector have zero orthogonal projection onto \( {TM} \) .

The tangential connection defined in Example 4.9 is perfectly suited to this task, because it computes covariant derivatives on \( M \) by taking ordinary derivatives in \( {\mathbb{R}}^{n} \) and projecting them orthogonally to \( {TM} \) .

It is easy to compute covariant derivatives along curves in \( M \) with respect to the tangential connection. Suppose \( \gamma  : I \rightarrow  M \) is a smooth curve. Then \( \gamma \) can be regarded as either a smooth curve in \( M \) or a smooth curve in \( {\mathbb{R}}^{n} \) , and a smooth vector field \( V \) along \( \gamma \) that takes its values in \( {TM} \) can be regarded as either a vector field along \( \gamma \) in \( M \) or a vector field along \( \gamma \) in \( {\mathbb{R}}^{n} \) . Let \( {\bar{D}}_{t}V \) denote the covariant derivative of \( V \) along \( \gamma \) (as a curve in \( {\mathbb{R}}^{n} \) ) with respect to the Euclidean connection \( \overline{\nabla } \) , and let \( {D}_{t}^{\top }V \) denote its covariant derivative along \( \gamma \) (as a curve in \( M \) ) with respect to the tangential connection \( {\nabla }^{\top } \) . The next proposition shows that the two covariant derivatives along \( \gamma \) have a simple relationship to each other.

Proposition 5.1. Let \( M \subseteq  {\mathbb{R}}^{n} \) be an embedded submanifold, \( \gamma  : I \rightarrow  M \) a smooth curve in \( M \) , and \( V \) a smooth vector field along \( \gamma \) that takes its values in \( {TM} \) . Then for each \( t \in  I \) ,

\[
{D}_{t}^{\top }V\left( t\right)  = {\pi }^{\top }\left( {{\bar{D}}_{t}V\left( t\right) }\right) .
\]

Proof. Let \( {t}_{0} \in  I \) be arbitrary. By Proposition 2.14, on some neighborhood \( U \) of \( \gamma \left( {t}_{0}\right) \) in \( {\mathbb{R}}^{n} \) there is an adapted orthonormal frame for \( {TM} \) , that is, a local orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) for \( T{\mathbb{R}}^{n} \) such that \( \left( {{E}_{1},\ldots ,{E}_{k}}\right) \) restricts to an orthonormal frame for \( {TM} \) at points of \( M \cap  U \) (where \( k = \dim M \) ). If \( \varepsilon  > 0 \) is small enough that \( \gamma \left( \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right) \right)  \subseteq  U \) , then for \( t \in  \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right) \) we can write

\[
V\left( t\right)  = {\left. {V}^{1}\left( t\right) {E}_{1}\right| }_{\gamma \left( t\right) } + \cdots  + {\left. {V}^{k}\left( t\right) {E}_{k}\right| }_{\gamma \left( t\right) },
\]

for some smooth functions \( {V}^{1},\ldots ,{V}^{k} : \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right)  \rightarrow  \mathbb{R} \) . Formula (4.15) yields

\[
{\pi }^{\top }\left( {{\bar{D}}_{t}V\left( t\right) }\right)  = {\pi }^{\top }\left( \left. {\mathop{\sum }\limits_{{i = 1}}^{k}\left( {{\dot{V}}^{i}\left( t\right) {\left. {E}_{i}\right| }_{\gamma \left( t\right) } + {\left. {V}^{i}\left( t\right) {\overline{\nabla }}_{{\gamma }^{\prime }\left( t\right) }{E}_{i}\right| }_{\gamma \left( t\right) }}\right) }\right) \right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{k}\left( {{\left. {\dot{V}}^{i}\left( t\right) {E}_{i}\right| }_{\gamma \left( t\right) } + {V}^{i}\left( t\right) {\pi }^{\top }\left( {\left. {\overline{\nabla }}_{{\gamma }^{\prime }\left( t\right) }{E}_{i}\right| }_{\gamma \left( t\right) }\right) }\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{k}\left( {{\left. {\dot{V}}^{i}\left( t\right) {E}_{i}\right| }_{\gamma \left( t\right) } + {\left. {V}^{i}\left( t\right) {\nabla }_{{\gamma }^{\prime }\left( t\right) }^{\top }{E}_{i}\right| }_{\gamma \left( t\right) }}\right)
\]

\[
= {D}_{t}^{\top }V\left( t\right) \text{ . }
\]

Corollary 5.2. Suppose \( M \subseteq  {\mathbb{R}}^{n} \) is an embedded submanifold. A smooth curve \( \gamma  : I \rightarrow  M \) is a geodesic with respect to the tangential connection on \( M \) if and only if its ordinary acceleration \( {\gamma }^{\prime \prime }\left( t\right) \) is orthogonal to \( {T}_{\gamma \left( t\right) }M \) for all \( t \in  I \) .

Proof. As noted in Example 4.8, the connection coefficients of the Euclidean connection on \( {\mathbb{R}}^{n} \) are all zero. Thus it follows from (4.15) that the Euclidean covariant derivative of \( {\gamma }^{\prime } \) along \( \gamma \) is just its ordinary acceleration: \( {\bar{D}}_{t}{\gamma }^{\prime }\left( t\right)  = {\gamma }^{\prime \prime }\left( t\right) \) . The corollary then follows from Proposition 5.1.

These considerations can be extended to pseudo-Riemannian manifolds as well. Let \( \left( {{\mathbb{R}}^{r, s},{\bar{q}}^{\left( r, s\right) }}\right) \) be the pseudo-Euclidean space of signature \( \left( {r, s}\right) \) . If \( M \subseteq  {\mathbb{R}}^{r, s} \) is an embedded Riemannian or pseudo-Riemannian submanifold, then for each \( p \in  M \) , the tangent space \( {T}_{p}{\mathbb{R}}^{r, s} \) decomposes as a direct sum \( {T}_{p}M \oplus  {N}_{p}M \) , where \( {N}_{p}M = {\left( {T}_{p}M\right) }^{ \bot  } \) is the orthogonal complement of \( {T}_{p}M \) with respect to \( {\bar{q}}^{\left( r, s\right) } \) . We let \( {\pi }^{\top } : {T}_{p}{\mathbb{R}}^{r, s} \rightarrow  {T}_{p}M \) be the \( {\bar{q}}^{\left( r, s\right) } \) -orthogonal projection, and define the tangential connection \( {\nabla }^{\top } \) on \( M \) by

\[
{\nabla }_{X}^{\top }Y = {\pi }^{\top }\left( {{\overline{\nabla }}_{\widetilde{X}}\widetilde{Y}}\right)
\]

where \( \widetilde{X} \) and \( \widetilde{Y} \) are smooth extensions of \( X \) and \( Y \) to a neighborhood of \( M \) , and \( \overline{\nabla } \) is the ordinary Euclidean connection on \( {\mathbb{R}}^{r, s} \) . This is a well-defined connection on \( M \) by the same argument as in the Euclidean case, and the next proposition is proved in exactly the same way as Corollary 5.2.

Proposition 5.3. Suppose \( M \) is an embedded Riemannian or pseudo-Riemannian submanifold of the pseudo-Euclidean space \( {\mathbb{R}}^{r, s} \) . A smooth curve \( \gamma  : I \rightarrow  M \) is a geodesic with respect to \( {\nabla }^{\top } \) if and only if \( {\gamma }^{\prime \prime }\left( t\right) \) is \( {\bar{q}}^{\left( r, s\right) } \) -orthogonal to \( {T}_{\gamma \left( t\right) }M \) for all \( t \in  I \) .

- Exercise 5.4. Prove the preceding proposition.

## Connections on Abstract Riemannian Manifolds

There is a celebrated (and hard) theorem of John Nash [Nas56] that says that every Riemannian metric on a smooth manifold can be realized as the induced metric of some embedding in a Euclidean space. That theorem was later generalized independently by Robert Greene [Gre70] and Chris J. S. Clarke [Cla70] to pseudo-Riemannian metrics. Thus, in a certain sense, we would lose no generality by studying only submanifolds of Euclidean and pseudo-Euclidean spaces with their induced metrics, for which the tangential connection would suffice. However, when we are trying to understand intrinsic properties of a Riemannian manifold, an embedding introduces a great deal of extraneous information, and in some cases actually makes it harder to discern which geometric properties depend only on the metric. Our task in this chapter is to distinguish some important properties of the tangential connection that make sense for connections on an abstract Riemannian or pseudo-Riemannian manifold, and to use them to single out a unique connection in the abstract case.

## Metric Connections

The Euclidean connection on \( {\mathbb{R}}^{n} \) has one very nice property with respect to the Euclidean metric: it satisfies the product rule

\[
{\overline{\nabla }}_{X}\langle Y, Z\rangle  = \left\langle  {{\overline{\nabla }}_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\overline{\nabla }}_{X}Z}\right\rangle  ,
\]

as you can verify easily by computing in terms of the standard basis. (In this formula, the left-hand side represents the covariant derivative of the real-valued function \( \langle Y, Z\rangle \) regarded as a \( \left( {0,0}\right) \) -tensor field, which is really just \( X\langle Y, Z\rangle \) by virtue of property (ii) of Prop. 4.15.) The Euclidean connection has the same property with respect to the pseudo-Euclidean metric on \( {\mathbb{R}}^{r, s} \) . It is almost immediate that the tangential connection on a Riemannian or pseudo-Riemannian submanifold satisfies the same product rule, if we now interpret all the vector fields as being tangent to \( M \) and interpret the inner products as being taken with respect to the induced metric on \( M \) (see Prop. 5.8 below).

This property makes sense on an abstract Riemannian or pseudo-Riemannian manifold. Let \( g \) be a Riemannian or pseudo-Riemannian metric on a smooth manifold \( M \) (with or without boundary). A connection \( \nabla \) on \( {TM} \) is said to be compatible with \( g \) , or to be a metric connection, if it satisfies the following product rule for all \( X, Y, Z \in  \mathfrak{X}\left( M\right) \) :

\[
{\nabla }_{X}\langle Y, Z\rangle  = \left\langle  {{\nabla }_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\nabla }_{X}Z}\right\rangle  . \tag{5.1}
\]

The next proposition gives several alternative characterizations of compatibility with a metric, any one of which could be used as the definition.

Proposition 5.5 (Characterizations of Metric Connections). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold (with or without boundary), and let \( \nabla \) be a connection on TM. The following conditions are equivalent:

(a) \( \nabla \) is compatible with \( g : {\nabla }_{X}\langle Y, Z\rangle  = \left\langle  {{\nabla }_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\nabla }_{X}Z}\right\rangle \) .

(b) \( g \) is parallel with respect to \( \nabla  : \nabla g \equiv  0 \) .

(c) In terms of any smooth local frame \( \left( {E}_{i}\right) \) , the connection coefficients of \( \nabla \) satisfy

\[
{\Gamma }_{ki}^{l}{g}_{lj} + {\Gamma }_{kj}^{l}{g}_{il} = {E}_{k}\left( {g}_{ij}\right) . \tag{5.2}
\]

(d) If \( V, W \) are smooth vector fields along any smooth curve \( \gamma \) , then

\[
\frac{d}{dt}\langle V, W\rangle  = \left\langle  {{D}_{t}V, W}\right\rangle   + \left\langle  {V,{D}_{t}W}\right\rangle  . \tag{5.3}
\]

(e) If \( V, W \) are parallel vector fields along a smooth curve \( \gamma \) in \( M \) , then \( \langle V, W\rangle \) is constant along \( \gamma \) .

![bo_d7dtff491nqc73eq8m7g_130_412_190_706_404_0.jpg](images/bo_d7dtff491nqc73eq8m7g_130_412_190_706_404_0.jpg)

Fig. 5.1: A parallel orthonormal frame

(f) Given any smooth curve \( \gamma \) in \( M \) , every parallel transport map along \( \gamma \) is a linear isometry.

(g) Given any smooth curve \( \gamma \) in \( M \) , every orthonormal basis at a point of \( \gamma \) can be extended to a parallel orthonormal frame along \( \gamma \) (Fig. 5.1).

Proof. First we prove (a) \( \Leftrightarrow \) (b). By (4.14) and (4.12), the total covariant derivative of the symmetric 2-tensor \( g \) is given by

\[
\left( {\nabla g}\right) \left( {Y, Z, X}\right)  = \left( {{\nabla }_{X}g}\right) \left( {Y, Z}\right)  = X\left( {g\left( {Y, Z}\right) }\right)  - g\left( {{\nabla }_{X}Y, Z}\right)  - g\left( {Y,{\nabla }_{X}Z}\right) .
\]

This is zero for all \( X, Y, Z \) if and only if (5.1) is satisfied for all \( X, Y, Z \) .

To prove (b) \( \Leftrightarrow \) (c), note that Proposition 4.18 shows that the components of \( \nabla g \) in terms of a smooth local frame \( \left( {E}_{i}\right) \) are

\[
{g}_{{ij};k} = {E}_{k}\left( {g}_{ij}\right)  - {\Gamma }_{ki}^{l}{g}_{lj} - {\Gamma }_{kj}^{l}{g}_{il}.
\]

These are all zero if and only if (5.2) is satisfied.

Next we prove (a) \( \Leftrightarrow \) (d). Assume (a), and let \( V, W \) be smooth vector fields along a smooth curve \( \gamma  : I \rightarrow  M \) . Given \( {t}_{0} \in  I \) , in a neighborhood of \( \gamma \left( {t}_{0}\right) \) we may choose coordinates \( \left( {x}^{i}\right) \) and write \( V = {V}^{i}{\partial }_{i} \) and \( W = {W}^{j}{\partial }_{j} \) for some smooth functions \( {V}^{i},{W}^{j} : I \rightarrow  \mathbb{R} \) . Applying (5.1) to the extendible vector fields \( {\partial }_{i},{\partial }_{j} \) , we obtain

\[
\frac{d}{dt}\langle V, W\rangle  = \frac{d}{dt}\left( {{V}^{i}{W}^{j}\left\langle  {{\partial }_{i},{\partial }_{j}}\right\rangle  }\right)
\]

\[
= \left( {{\dot{V}}^{i}{W}^{j} + {V}^{i}{\dot{W}}^{j}}\right) \left\langle  {{\partial }_{i},{\partial }_{j}}\right\rangle   + {V}^{i}{W}^{j}\left( {\left\langle  {{\nabla }_{{\gamma }^{\prime }\left( t\right) }{\partial }_{i},{\partial }_{j}}\right\rangle   + \left\langle  {{\partial }_{i},{\nabla }_{{\gamma }^{\prime }\left( t\right) }{\partial }_{j}}\right\rangle  }\right)
\]

\[
= \left\langle  {{D}_{t}V, W}\right\rangle   + \left\langle  {V,{D}_{t}W}\right\rangle  ,
\]

which proves (d). Conversely, if (d) holds, then in particular it holds for extendible vector fields along \( \gamma \) , and then (a) follows from part (iii) of Theorem 4.24.

Now we will prove (d) \( \Rightarrow \) (e) \( \Rightarrow \) (f) \( \Rightarrow \) (g) \( \Rightarrow \) (d). Assume first that (d) holds. If \( V \) and \( W \) are parallel along \( \gamma \) , then (5.3) shows that \( \langle V, W\rangle \) has zero derivative with respect to \( t \) , so it is constant along \( \gamma \) .

Now assume (e). Let \( {v}_{0},{w}_{0} \) be arbitrary vectors in \( {T}_{\gamma \left( {t}_{0}\right) }M \) , and let \( V, W \) be their parallel transports along \( \gamma \) , so that \( V\left( {t}_{0}\right)  = {v}_{0}, W\left( {t}_{0}\right)  = {w}_{0},{P}_{{t}_{0}{t}_{1}}^{\gamma }{v}_{0} = \; V\left( {t}_{1}\right) \) , and \( {P}_{{t}_{0}{t}_{1}}^{\gamma }{w}_{0} = W\left( {t}_{1}\right) \) . Because \( \langle V, W\rangle \) is constant along \( \gamma \) , it follows that \( \left\langle  {{P}_{{t}_{0}{t}_{1}}^{\gamma }{v}_{0},{P}_{{t}_{0}{t}_{1}}^{\gamma }{w}_{0}}\right\rangle   = \left\langle  {V\left( {t}_{1}\right) , W\left( {t}_{1}\right) }\right\rangle   = \left\langle  {V\left( {t}_{0}\right) , W\left( {t}_{0}\right) }\right\rangle   = \left\langle  {{v}_{0},{w}_{0}}\right\rangle \) , so \( {P}_{{t}_{0}{t}_{1}}^{\gamma } \) is a linear isometry.

Next, assuming (f), we suppose \( \gamma  : I \rightarrow  M \) is a smooth curve and \( \left( {b}_{i}\right) \) is an orthonormal basis for \( {T}_{\gamma \left( {t}_{0}\right) }M \) , for some \( {t}_{0} \in  I \) . We can extend each \( {b}_{i} \) by parallel transport to obtain a smooth parallel vector field \( {E}_{i} \) along \( \gamma \) , and the assumption that parallel transport is a linear isometry guarantees that the resulting \( n \) -tuple \( \left( {E}_{i}\right) \) is an orthonormal frame at all points of \( \gamma \) .

Finally, assume that (g) holds, and let \( \left( {E}_{i}\right) \) be a parallel orthonormal frame along \( \gamma \) . Given smooth vector fields \( V \) and \( W \) along \( \gamma \) , we can express them in terms of this frame as \( V = {V}^{i}{E}_{i} \) and \( W = {W}^{j}{E}_{j} \) . The fact that the frame is orthonormal means that the metric coefficients \( {g}_{ij} = \left\langle  {{E}_{i},{E}_{j}}\right\rangle \) are constants along \( \gamma \left( {\pm 1\text{ or 0 }}\right) \) , and the fact that it is parallel means that \( {D}_{t}V = {\dot{V}}^{i}{E}_{i} \) and \( {D}_{t}W = {\dot{W}}^{i}{E}_{i} \) . Thus both sides of (5.3) reduce to the following expression:

\[
{g}_{ij}\left( {{\dot{V}}^{i}{W}^{j} + {V}^{i}{\dot{W}}^{j}}\right) . \tag{5.4}
\]

This proves (d).

Corollary 5.6. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold with or without boundary, \( \nabla \) is a metric connection on \( M \) , and \( \gamma  : I \rightarrow  M \) is a smooth curve.

(a) \( \left| {{\gamma }^{\prime }\left( t\right) }\right| \) is constant if and only if \( {D}_{t}{\gamma }^{\prime }\left( t\right) \) is orthogonal to \( {\gamma }^{\prime }\left( t\right) \) for all \( t \in  I \) .

(b) If \( \gamma \) is a geodesic, then \( \left| {{\gamma }^{\prime }\left( t\right) }\right| \) is constant.

- Exercise 5.7. Prove the preceding corollary.

Proposition 5.8. If \( M \) is an embedded Riemannian or pseudo-Riemannian subman-ifold of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}^{r, s} \) , the tangential connection on \( M \) is compatible with the induced Riemannian or pseudo-Riemannian metric.

Proof. We will show that \( {\nabla }^{\top } \) satisfies (5.1). Suppose \( X, Y, Z \in  \mathcal{X}\left( M\right) \) , and let \( \widetilde{X},\widetilde{Y},\widetilde{Z} \) be smooth extensions of them to an open subset of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}^{r, s} \) . At points of \( M \) , we have

\[
{\nabla }_{X}^{\top }\langle Y, Z\rangle  = X\langle Y, Z\rangle  = \widetilde{X}\langle \widetilde{Y},\widetilde{Z}\rangle
\]

\[
= {\overline{\nabla }}_{\widetilde{X}}\langle \widetilde{Y},\widetilde{Z}\rangle
\]

\[
= \left\langle  {{\overline{\nabla }}_{\widetilde{X}}\widetilde{Y},\widetilde{Z}}\right\rangle   + \left\langle  {\widetilde{Y},{\overline{\nabla }}_{\widetilde{X}}\widetilde{Z}}\right\rangle
\]

\[
= \left\langle  {{\pi }^{\top }\left( {{\overline{\nabla }}_{\widetilde{X}}\widetilde{Y}}\right) ,\widetilde{Z}}\right\rangle   + \left\langle  {\widetilde{Y},{\pi }^{\top }\left( {{\overline{\nabla }}_{\widetilde{X}}\widetilde{Z}}\right) }\right\rangle
\]

\[
= \left\langle  {{\nabla }_{X}^{\top }Y, Z}\right\rangle   + \left\langle  {Y,{\nabla }_{X}^{\top }Z}\right\rangle  ,
\]

where the next-to-last equality follows from the fact that \( \widetilde{Z} \) and \( \widetilde{Y} \) are tangent to \( M \) .

## Symmetric Connections

It turns out that every abstract Riemannian or pseudo-Riemannian manifold admits many different metric connections (see Problem 5-1), so requiring compatibility with the metric is not sufficient to pin down a unique connection on such a manifold. To do so, we turn to another key property of the tangential connection. Recall the definition (4.3) of the Euclidean connection. The expression on the right-hand side of that definition is reminiscent of part of the coordinate expression for the Lie bracket:

\[
\left\lbrack  {X, Y}\right\rbrack   = X\left( {Y}^{i}\right) \frac{\partial }{\partial {x}^{i}} - Y\left( {X}^{i}\right) \frac{\partial }{\partial {x}^{i}}.
\]

In fact, the two terms in the Lie bracket formula are exactly the coordinate expressions for \( {\overline{\nabla }}_{X}Y \) and \( {\overline{\nabla }}_{Y}X \) . Therefore, the Euclidean connection satisfies the following identity for all smooth vector fields \( X, Y \) :

\[
{\overline{\nabla }}_{X}Y - {\overline{\nabla }}_{Y}X = \left\lbrack  {X, Y}\right\rbrack
\]

This expression has the virtue that it is coordinate-independent and makes sense for every connection on the tangent bundle. We say that a connection \( \nabla \) on the tangent bundle of a smooth manifold \( M \) is symmetric if

\[
{\nabla }_{X}Y - {\nabla }_{Y}X \equiv  \left\lbrack  {X, Y}\right\rbrack  \text{ for all }X, Y \in  \mathfrak{X}\left( M\right) \text{ . }
\]

The symmetry condition can also be expressed in terms of the torsion tensor of the connection, which was introduced in Problem 4-6; this is the smooth (1, 2)- tensor field \( \tau  : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) defined by

\[
\tau \left( {X, Y}\right)  = {\nabla }_{X}Y - {\nabla }_{Y}X - \left\lbrack  {X, Y}\right\rbrack  .
\]

Thus a connection \( \nabla \) is symmetric if and only if its torsion vanishes identically. It follows from the result of Problem 4-6 that a connection is symmetric if and only if its connection coefficients in every coordinate frame satisfy \( {\Gamma }_{ij}^{k} = {\Gamma }_{ji}^{k} \) ; this is the origin of the term "symmetric."

Proposition 5.9. If \( M \) is an embedded (pseudo-)Riemannian submanifold of a (pseudo-)Euclidean space, then the tangential connection on \( M \) is symmetric.

Proof. Let \( M \) be an embedded Riemannian or pseudo-Riemannian submanifold of \( {\mathbb{R}}^{n} \) , where \( {\mathbb{R}}^{n} \) is endowed either with the Euclidean metric or with a pseudo-Euclidean metric \( {\bar{q}}^{\left( r, s\right) }, r + s = n \) . Let \( X, Y \in  \mathfrak{X}\left( M\right) \) , and let \( \widetilde{X},\widetilde{Y} \) be smooth extensions of them to an open subset of the ambient space. If \( \iota  : M \hookrightarrow  {\mathbb{R}}^{n} \) represents the inclusion map, it follows that \( X \) and \( Y \) are \( \iota \) -related to \( \widetilde{X} \) and \( \widetilde{Y} \) , respectively, and thus by the naturality of the Lie bracket (Prop. A.39), \( \left\lbrack  {X, Y}\right\rbrack \) is \( \iota \) -related to \( \left\lbrack  {\widetilde{X},\widetilde{Y}}\right\rbrack \) . In particular, \( \left\lbrack  {\widetilde{X},\widetilde{Y}}\right\rbrack \) is tangent to \( M \) , and its restriction to \( M \) is equal to \( \left\lbrack  {X, Y}\right\rbrack \) . Therefore,

\[
{\nabla }_{X}^{\top }Y - {\nabla }_{Y}^{\top }X = {\pi }^{\top }\left( {{\left. {\overline{\nabla }}_{\widetilde{X}}\widetilde{Y}\right| }_{M} - {\left. {\overline{\nabla }}_{\widetilde{Y}}\widetilde{X}\right| }_{M}}\right)
\]

\[
= {\pi }^{\top }\left( {\left. \left\lbrack  \widetilde{X},\widetilde{Y}\right\rbrack  \right| }_{M}\right)
\]

\[
= {\left. \left\lbrack  \widetilde{X},\widetilde{Y}\right\rbrack  \right| }_{M}
\]

\[
= \left\lbrack  {X, Y}\right\rbrack  \text{ . }
\]

The last two propositions show that if we wish to single out a connection on each Riemannian or pseudo-Riemannian manifold in such a way that it matches the tangential connection when the manifold is presented as an embedded submanifold of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}^{r, s} \) with the induced metric, then we must require at least that the connection be compatible with the metric and symmetric. It is a pleasant fact that these two conditions are enough to determine a unique connection.

Theorem 5.10 (Fundamental Theorem of Riemannian Geometry). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold (with or without boundary). There exists a unique connection \( \nabla \) on \( {TM} \) that is compatible with \( g \) and symmetric. It is called the Levi-Civita connection of \( \mathbf{g} \) (or also, when \( g \) is positive definite, the Riemannian connection).

Proof. We prove uniqueness first, by deriving a formula for \( \nabla \) . Suppose, therefore, that \( \nabla \) is such a connection, and let \( X, Y, Z \in  \mathfrak{X}\left( M\right) \) . Writing the compatibility equation three times with \( X, Y, Z \) cyclically permuted, we obtain

\[
X\langle Y, Z\rangle  = \left\langle  {{\nabla }_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\nabla }_{X}Z}\right\rangle
\]

\[
Y\langle Z, X\rangle  = \left\langle  {{\nabla }_{Y}Z, X}\right\rangle   + \left\langle  {Z,{\nabla }_{Y}X}\right\rangle
\]

\[
Z\langle X, Y\rangle  = \left\langle  {{\nabla }_{Z}X, Y}\right\rangle   + \left\langle  {X,{\nabla }_{Z}Y}\right\rangle
\]

Using the symmetry condition on the last term in each line, this can be rewritten as

\[
X\langle Y, Z\rangle  = \left\langle  {{\nabla }_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\nabla }_{Z}X}\right\rangle   + \langle Y,\left\lbrack  {X, Z}\right\rbrack  \rangle
\]

\[
Y\langle Z, X\rangle  = \left\langle  {{\nabla }_{Y}Z, X}\right\rangle   + \left\langle  {Z,{\nabla }_{X}Y}\right\rangle   + \langle Z,\left\lbrack  {Y, X}\right\rbrack  \rangle
\]

\[
Z\langle X, Y\rangle  = \left\langle  {{\nabla }_{Z}X, Y}\right\rangle   + \left\langle  {X,{\nabla }_{Y}Z}\right\rangle   + \langle X,\left\lbrack  {Z, Y}\right\rbrack  \rangle .
\]

Adding the first two of these equations and subtracting the third, we obtain

\[
X\langle Y, Z\rangle  + Y\langle Z, X\rangle  - Z\langle X, Y\rangle  =
\]

\[
2\left\langle  {{\nabla }_{X}Y, Z}\right\rangle   + \langle Y,\left\lbrack  {X, Z}\right\rbrack  \rangle  + \langle Z,\left\lbrack  {Y, X}\right\rbrack  \rangle  - \langle X,\left\lbrack  {Z, Y}\right\rbrack  \rangle .
\]

Finally, solving for \( \left\langle  {{\nabla }_{X}Y, Z}\right\rangle \) , we get

\[
\left\langle  {{\nabla }_{X}Y, Z}\right\rangle   = \frac{1}{2}(X\langle Y, Z\rangle  + Y\langle Z, X\rangle  - Z\langle X, Y\rangle
\]

\[
\left. {-\langle Y,\left\lbrack  {X, Z}\right\rbrack  \rangle -\langle Z,\left\lbrack  {Y, X}\right\rbrack  \rangle +\langle X,\left\lbrack  {Z, Y}\right\rbrack  \rangle }\right) \text{ . } \tag{5.5}
\]

Now suppose \( {\nabla }^{1} \) and \( {\nabla }^{2} \) are two connections on \( {TM} \) that are symmetric and compatible with \( g \) . Since the right-hand side of (5.5) does not depend on the connection, it follows that \( \left\langle  {{\nabla }_{X}^{1}Y - {\nabla }_{X}^{2}Y, Z}\right\rangle   = 0 \) for all \( X, Y, Z \) . This can happen only if \( {\nabla }_{X}^{1}Y = {\nabla }_{X}^{2}Y \) for all \( X \) and \( Y \) , so \( {\nabla }^{1} = {\nabla }^{2} \) .

To prove existence, we use (5.5), or rather a coordinate version of it. It suffices to prove that such a connection exists in each coordinate chart, for then uniqueness ensures that the connections in different charts agree where they overlap.

Let \( \left( {U,\left( {x}^{i}\right) }\right) \) be any smooth local coordinate chart. Applying (5.5) to the coordinate vector fields, whose Lie brackets are zero, we obtain

\[
\left\langle  {{\nabla }_{{\partial }_{i}}{\partial }_{j},{\partial }_{l}}\right\rangle   = \frac{1}{2}\left( {{\partial }_{i}\left\langle  {{\partial }_{j},{\partial }_{l}}\right\rangle   + {\partial }_{j}\left\langle  {{\partial }_{l},{\partial }_{i}}\right\rangle   - {\partial }_{l}\left\langle  {{\partial }_{i},{\partial }_{j}}\right\rangle  }\right) . \tag{5.6}
\]

Recall the definitions of the metric coefficients and the connection coefficients:

\[
{g}_{ij} = \left\langle  {{\partial }_{i},{\partial }_{j}}\right\rangle  ,\;{\nabla }_{{\partial }_{i}}{\partial }_{j} = {\Gamma }_{ij}^{m}{\partial }_{m}.
\]

Inserting these into (5.6) yields

\[
{\Gamma }_{ij}^{m}{g}_{ml} = \frac{1}{2}\left( {{\partial }_{i}{g}_{jl} + {\partial }_{j}{g}_{il} - {\partial }_{l}{g}_{ij}}\right) . \tag{5.7}
\]

Finally, multiplying both sides by the inverse matrix \( {g}^{kl} \) and noting that \( {g}_{ml}{g}^{kl} = \; {\delta }_{m}^{k} \) , we get

\[
{\Gamma }_{ij}^{k} = \frac{1}{2}{g}^{kl}\left( {{\partial }_{i}{g}_{jl} + {\partial }_{j}{g}_{il} - {\partial }_{l}{g}_{ij}}\right) . \tag{5.8}
\]

This formula certainly defines a connection in each chart, and it is evident from the formula that \( {\Gamma }_{ij}^{k} = {\Gamma }_{ji}^{k} \) , so the connection is symmetric by Problem 4-6(b). Thus only compatibility with the metric needs to be checked. Using (5.7) twice, we get

\[
{\Gamma }_{ki}^{l}{g}_{lj} + {\Gamma }_{kj}^{l}{g}_{il} = \frac{1}{2}\left( {{\partial }_{k}{g}_{ij} + {\partial }_{i}{g}_{kj} - {\partial }_{j}{g}_{ki}}\right)  + \frac{1}{2}\left( {{\partial }_{k}{g}_{ji} + {\partial }_{j}{g}_{ki} - {\partial }_{i}{g}_{kj}}\right)
\]

\[
= {\partial }_{k}{g}_{ij}.
\]

By Proposition 5.5(c), this shows that \( \nabla \) is compatible with \( g \) .

A bonus of this proof is that it gives us explicit formulas that can be used for computing the Levi-Civita connection in various circumstances.

Corollary 5.11 (Formulas for the Levi-Civita Connection). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold (with or without boundary), and let \( \nabla \) be its Levi-Civita connection.

(a) IN TERMS OF VECTOR FIELDS: If \( X, Y, Z \) are smooth vector fields on \( M \) , then

\[
\left\langle  {{\nabla }_{X}Y, Z}\right\rangle   = \frac{1}{2}(X\langle Y, Z\rangle  + Y\langle Z, X\rangle  - Z\langle X, Y\rangle
\]

\[
\left. {-\langle Y,\left\lbrack  {X, Z}\right\rbrack  \rangle -\langle Z,\left\lbrack  {Y, X}\right\rbrack  \rangle +\langle X,\left\lbrack  {Z, Y}\right\rbrack  \rangle }\right) \text{ . } \tag{5.9}
\]

(This is known as Koszul's formula.)

(b) IN COORDINATES: In any smooth coordinate chart for \( M \) , the coefficients of the Levi-Civita connection are given by

\[
{\Gamma }_{ij}^{k} = \frac{1}{2}{g}^{kl}\left( {{\partial }_{i}{g}_{jl} + {\partial }_{j}{g}_{il} - {\partial }_{l}{g}_{ij}}\right) . \tag{5.10}
\]

(c) IN A LOCAL FRAME: Let \( \left( {E}_{i}\right) \) be a smooth local frame on an open subset \( U \subseteq  M \) , and let \( {c}_{ij}^{k} : U \rightarrow  \mathbb{R} \) be the \( {n}^{3} \) smooth functions defined by

\[
\left\lbrack  {{E}_{i},{E}_{j}}\right\rbrack   = {c}_{ij}^{k}{E}_{k}. \tag{5.11}
\]

Then the coefficients of the Levi-Civita connection in this frame are

\[
{\Gamma }_{ij}^{k} = \frac{1}{2}{g}^{kl}\left( {{E}_{i}{g}_{jl} + {E}_{j}{g}_{il} - {E}_{l}{g}_{ij} - {g}_{jm}{c}_{il}^{m} - {g}_{lm}{c}_{ji}^{m} + {g}_{im}{c}_{lj}^{m}}\right) . \tag{5.12}
\]

(d) IN A LOCAL ORTHONORMAL FRAME: If \( g \) is Riemannian, \( \left( {E}_{i}\right) \) is a smooth local orthonormal frame, and the functions \( {c}_{ij}^{k} \) are defined by (5.11), then

\[
{\Gamma }_{ij}^{k} = \frac{1}{2}\left( {{c}_{ij}^{k} - {c}_{ik}^{j} - {c}_{jk}^{i}}\right) . \tag{5.13}
\]

Proof. We derived (5.9) and (5.10) in the proof of Theorem 5.10. To prove (5.12), apply formula (5.9) with \( X = {E}_{i}, Y = {E}_{j} \) , and \( Z = {E}_{l} \) , to obtain

\[
{\Gamma }_{ij}^{q}{g}_{ql} = \left\langle  {{\nabla }_{{E}_{i}}{E}_{j},{E}_{l}}\right\rangle
\]

\[
= \frac{1}{2}\left( {{E}_{i}{g}_{jl} + {E}_{j}{g}_{il} - {E}_{l}{g}_{ij} - {g}_{jm}{c}_{il}^{m} - {g}_{lm}{c}_{ji}^{m} + {g}_{im}{c}_{lj}^{m}}\right) .
\]

Multiplying both sides by \( {g}^{kl} \) and simplifying yields (5.12). Finally, under the hypotheses of (d), we have \( {g}_{ij} = {\delta }_{ij} \) , so (5.12) reduces to (5.13) after rearranging and using the fact that \( {c}_{ij}^{k} \) is antisymmetric in \( i, j \) .

On every Riemannian or pseudo-Riemannian manifold, we will always use the Levi-Civita connection from now on without further comment. Geodesics with respect to this connection are called Riemannian (or pseudo-Riemannian) geodesics, or simply "geodesics" as long as there is no risk of confusion. The connection coefficients \( {\Gamma }_{ij}^{k} \) of the Levi-Civita connection in coordinates, given by (5.10), are called the Christoffel symbols of \( g \) .

The next proposition shows that these connections are familiar ones in the case of embedded submanifolds of Euclidean or pseudo-Euclidean spaces.

## Proposition 5.12.

(a) The Levi-Civita connection on a (pseudo-)Euclidean space is equal to the Euclidean connection.

(b) Suppose M is an embedded (pseudo-)Riemannian submanifold of a (pseudo-) Euclidean space. Then the Levi-Civita connection on \( M \) is equal to the tangential connection \( {\nabla }^{\top } \) .

Proof. We observed earlier in this chapter that the Euclidean connection is symmetric and compatible with both the Euclidean metric \( \bar{g} \) and the pseudo-Euclidean metrics \( {\bar{q}}^{\left( r, s\right) } \) , which implies (a). Part (b) then follows from Propositions 5.8 and 5.9.

An important consequence of the definition is that because Levi-Civita connections are defined in coordinate-independent terms, they behave well with respect to isometries. Recall the definition of the pullback of a connection (see Lemma 4.37).

Proposition 5.13 (Naturality of the Levi-Civita Connection). Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian or pseudo-Riemannian manifolds with or without boundary, and let \( \nabla \) denote the Levi-Civita connection of \( g \) and \( \widetilde{\nabla } \) that of \( \widetilde{g} \) . If \( \varphi  : M \rightarrow  \widetilde{M} \) is an isometry, then \( {\varphi }^{ * }\widetilde{\nabla } = \nabla \) .

Proof. By uniqueness of the Levi-Civita connection, it suffices to show that the pullback connection \( {\varphi }^{ * }\widetilde{\nabla } \) is symmetric and compatible with \( g \) . The fact that \( \varphi \) is an isometry means that for any \( X, Y \in  \mathfrak{X}\left( M\right) \) and \( p \in  M \) ,

\[
\left\langle  {{Y}_{p},{Z}_{p}}\right\rangle   = \left\langle  {d{\varphi }_{p}\left( {Y}_{p}\right) , d{\varphi }_{p}\left( {Z}_{p}\right) }\right\rangle   = \left\langle  {{\left( {\varphi }_{ * }Y\right) }_{\varphi \left( p\right) },{\left( {\varphi }_{ * }Z\right) }_{\varphi \left( p\right) }}\right\rangle  ,
\]

or in other words, \( \langle Y, Z\rangle  = \left\langle  {{\varphi }_{ * }Y,{\varphi }_{ * }Z}\right\rangle   \circ  \varphi \) . Therefore,

\[
X\langle Y, Z\rangle  = X\left( {\left\langle  {{\varphi }_{ * }Y,{\varphi }_{ * }Z}\right\rangle   \circ  \varphi }\right)
\]

\[
= \left( {\left( {{\varphi }_{ * }X}\right) \left\langle  {{\varphi }_{ * }Y,{\varphi }_{ * }Z}\right\rangle  }\right)  \circ  \varphi
\]

\[
= \left( {\left\langle  {{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right) ,{\varphi }_{ * }Z}\right\rangle   + \left\langle  {{\varphi }_{ * }Y,{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Z}\right) }\right\rangle  }\right)  \circ  \varphi
\]

\[
= \left\langle  {{\left( {\varphi }^{-1}\right) }_{ * }{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right) , Z}\right\rangle   + \left\langle  {Y,{\left( {\varphi }^{-1}\right) }_{ * }{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Z}\right) }\right\rangle
\]

\[
= \left\langle  {{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y, Z}\right\rangle   + \left\langle  {Y,{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Z}\right\rangle  ,
\]

which shows that the pullback connection is compatible with \( g \) . Symmetry is proved as follows:

\[
{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y - {\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{Y}X = {\left( {\varphi }^{-1}\right) }_{ * }\left( {{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right)  - {\widetilde{\nabla }}_{{\varphi }_{ * }Y}\left( {{\varphi }_{ * }X}\right) }\right)
\]

\[
= {\left( {\varphi }^{-1}\right) }_{ * }\left\lbrack  {{\varphi }_{ * }X,{\varphi }_{ * }Y}\right\rbrack
\]

\[
= \left\lbrack  {X, Y}\right\rbrack  \text{ . }
\]

Corollary 5.14 (Naturality of Geodesics). Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian or pseudo-Riemannian manifolds with or without boundary, and \( \varphi  : M \rightarrow \; \widetilde{M} \) is a local isometry. If \( \gamma \) is a geodesic in \( M \) , then \( \varphi  \circ  \gamma \) is a geodesic in \( \widetilde{M} \) .

Proof. This is an immediate consequence of Proposition 4.38, together with the fact that being a geodesic is a local property.

Like every connection on the tangent bundle, the Levi-Civita connection induces connections on all tensor bundles.

Proposition 5.15. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold. The connection induced on each tensor bundle by the Levi-Civita connection is compatible with the induced inner product on tensors, in the sense that \( X\langle F, G\rangle  = \left\langle  {{\nabla }_{X}F, G}\right\rangle   + \left\langle  {F,{\nabla }_{X}G}\right\rangle \) for every vector field \( X \) and every pair of smooth tensor fields \( F, G \in  \Gamma \left( {{T}^{\left( k, l\right) }{TM}}\right) \) .

Proof. Since every tensor field can be written as a sum of tensor products of vector and/or covector fields, it suffices to consider the case in which \( F = {\alpha }_{1} \otimes  \cdots  \otimes  {\alpha }_{k + l} \) and \( G = {\beta }_{1} \otimes  \cdots  \otimes  {\beta }_{k + l} \) , where \( {\alpha }_{i} \) and \( {\beta }_{i} \) are covariant or contravariant 1-tensor fields, as appropriate. In this case, the formula follows from (2.15) by a routine computation.

Proposition 5.16. Let \( \left( {M, g}\right) \) be an oriented Riemannian manifold. The Riemannian volume form of \( g \) is parallel with respect to the Levi-Civita connection.

Proof. Let \( p \in  M \) and \( v \in  {T}_{p}M \) be arbitrary, and let \( \gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  M \) be a smooth curve satisfying \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) . Let \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be a parallel oriented orthonormal frame along \( \gamma \) . Since \( d{V}_{g}\left( {{E}_{1},\ldots ,{E}_{n}}\right)  \equiv  1 \) and \( {D}_{t}{E}_{i} \equiv  0 \) along \( \gamma \) , formula (4.12) shows that \( {\nabla }_{v}\left( {d{V}_{g}}\right)  = {\left. {D}_{t}\left( d{V}_{g}\right) \right| }_{t = 0} = 0 \) .

Proposition 5.17. The musical isomorphisms commute with the total covariant derivative operator: if \( F \) is any smooth tensor field with a contravariant i th index position, and \( \diamond \) represents the operation of lowering the ith index, then

\[
\nabla \left( {F}^{b}\right)  = {\left( \nabla F\right) }^{b}. \tag{5.14}
\]

Similarly, if \( G \) has a covariant \( i \) th position and \( \sharp \) denotes raising the \( i \) th index, then

\[
\nabla \left( {G}^{\sharp }\right)  = {\left( \nabla G\right) }^{\sharp }. \tag{5.15}
\]

Proof. The discussion on page 27 shows that \( {F}^{\flat } = \operatorname{tr}\left( {F \otimes  g}\right) \) , where the trace is taken on the \( i \) th and last indices of \( F \otimes  g \) . Because \( g \) is parallel, for every vector field \( X \) we have \( {\nabla }_{X}\left( {F \otimes  g}\right)  = \left( {{\nabla }_{X}F}\right)  \otimes  g \) . Because \( {\nabla }_{X} \) commutes with traces, therefore,

\[
{\nabla }_{X}\left( {F}^{b}\right)  = {\nabla }_{X}\left( {\operatorname{tr}\left( {F \otimes  g}\right) }\right)  = \operatorname{tr}\left( {\left( {{\nabla }_{X}F}\right)  \otimes  g}\right)  = {\left( {\nabla }_{X}F\right) }^{b}.
\]

This shows that when \( X \) is inserted into the last index position on both sides of (5.14), the results are equal. Since \( X \) is arbitrary, this proves (5.14).

Because the sharp and flat operators are inverses of each other when applied to the same index position,(5.15) follows by substituting \( F = {G}^{\sharp } \) into (5.14) and applying \( \sharp \) to both sides.

## The Exponential Map

Throughout this section, we let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian \( n \) -manifold, endowed with its Levi-Civita connection. Corollary 4.28 showed that each initial point \( p \in  M \) and each initial velocity vector \( v \in  {T}_{p}M \) determine a unique maximal geodesic \( {\gamma }_{v} \) . To deepen our understanding of geodesics, we need to study their collective behavior, and in particular, to address the following question: How do geodesics change if we vary the initial point or the initial velocity? The dependence of geodesics on the initial data is encoded in a map from the tangent bundle into the manifold, called the exponential map, whose properties are fundamental to the further study of Riemannian geometry.

(It is worth noting that the existence of the exponential map and the basic properties expressed in Proposition 5.19 below hold for every connection in \( {TM} \) , not just for the Levi-Civita connection. For simplicity, we restrict attention here to the latter case, because that is all we need. We also restrict to manifolds without boundary, in order to avoid complications with geodesics running into a boundary.)

The next lemma shows that geodesics with proportional initial velocities are related in a simple way.

Lemma 5.18 (Rescaling Lemma). For every \( p \in  M, v \in  {T}_{p}M \) , and \( c, t \in  \mathbb{R} \) ,

\[
{\gamma }_{cv}\left( t\right)  = {\gamma }_{v}\left( {ct}\right) , \tag{5.16}
\]

whenever either side is defined.

Proof. If \( c = 0 \) , then both sides of (5.16) are equal to \( p \) for all \( t \in  \mathbb{R} \) , so we may assume that \( c \neq  0 \) . It suffices to show that \( {\gamma }_{cv}\left( t\right) \) exists and (5.16) holds whenever the right-hand side is defined. (The same argument with the substitutions \( v = {c}^{\prime }{v}^{\prime } \) , \( t = {c}^{\prime }{t}^{\prime } \) , and \( c = 1/{c}^{\prime } \) then implies that the conclusion holds when only the left-hand side is known to be defined.)

Suppose the maximal domain of \( {\gamma }_{v} \) is the open interval \( I \subseteq  \mathbb{R} \) . For simplicity, write \( \gamma  = {\gamma }_{v} \) , and define a new curve \( \widetilde{\gamma } : {c}^{-1}I \rightarrow  M \) by \( \widetilde{\gamma }\left( t\right)  = \gamma \left( {ct}\right) \) , where \( {c}^{-1}I = \; \left\{  {{c}^{-1}t : t \in  I}\right\} \) . We will show that \( \widetilde{\gamma } \) is a geodesic with initial point \( p \) and initial velocity \( {cv} \) ; it then follows by uniqueness and maximality that it must be equal to \( {\gamma }_{cv} \) .

It is immediate from the definition that \( \widetilde{\gamma }\left( 0\right)  = \gamma \left( 0\right)  = p \) . Choose any smooth local coordinates on \( M \) and write the coordinate representation of \( \gamma \) as \( \gamma \left( t\right)  = \; \left( {{\gamma }^{1}\left( t\right) ,\ldots ,{\gamma }^{n}\left( t\right) }\right) \) ; then the chain rule gives

\[
{\dot{\widetilde{\gamma }}}^{i}\left( t\right)  = \frac{d}{dt}{\gamma }^{i}\left( {ct}\right)
\]

\[
= c{\dot{\gamma }}^{i}\left( {ct}\right) \text{ . }
\]

In particular, it follows that \( {\widetilde{\gamma }}^{\prime }\left( 0\right)  = c{\gamma }^{\prime }\left( 0\right)  = {cv} \) .

Now let \( {D}_{t} \) and \( {\widetilde{D}}_{t} \) denote the covariant differentiation operators along \( \gamma \) and \( \widetilde{\gamma } \) , respectively. Using the chain rule again in coordinates yields

\[
{\widetilde{D}}_{t}{\widetilde{\gamma }}^{\prime }\left( t\right)  = \left( {\frac{d}{dt}{\dot{\widetilde{\gamma }}}^{k}\left( t\right)  + {\Gamma }_{ij}^{k}\left( {\widetilde{\gamma }\left( t\right) }\right) {\dot{\widetilde{\gamma }}}^{i}\left( t\right) {\dot{\widetilde{\gamma }}}^{j}\left( t\right) }\right) {\partial }_{k}
\]

\[
= \left( {{c}^{2}{\ddot{\gamma }}^{k}\left( {ct}\right)  + {c}^{2}{\Gamma }_{ij}^{k}\left( {\gamma \left( {ct}\right) }\right) {\dot{\gamma }}^{i}\left( {ct}\right) {\dot{\gamma }}^{j}\left( {ct}\right) }\right) {\partial }_{k}
\]

\[
= {c}^{2}{D}_{t}{\gamma }^{\prime }\left( {ct}\right)  = 0.
\]

Thus \( \widetilde{\gamma } \) is a geodesic, so \( \widetilde{\gamma } = {\gamma }_{cv} \) , as claimed.

The assignment \( v \mapsto  {\gamma }_{v} \) defines a map from \( {TM} \) to the set of geodesics in \( M \) . More importantly, by virtue of the rescaling lemma, it allows us to define a map from (a subset of) the tangent bundle to \( M \) itself, which sends each line through the origin in \( {T}_{p}M \) to a geodesic.

Define a subset \( \mathcal{E} \subseteq  {TM} \) , the domain of the exponential map, by

\[
\mathcal{E} = \left\{  {v \in  {TM} : {\gamma }_{v}\text{ is defined on an interval containing }\left\lbrack  {0,1}\right\rbrack  }\right\}  ,
\]

and then define the exponential map \( \exp  : \mathcal{E} \rightarrow  M \) by

\[
\exp \left( v\right)  = {\gamma }_{v}\left( 1\right) .
\]

For each \( p \in  M \) , the restricted exponential map at \( \mathbf{p} \) , denoted by \( {\exp }_{p} \) , is the restriction of exp to the set \( {\mathcal{E}}_{p} = \mathcal{E} \cap  {T}_{p}M \) .

The exponential map of a Riemannian manifold should not be confused with the exponential map of a Lie group. The two are closely related for bi-invariant metrics (see Problem 5-8), but in general they need not be. To avoid confusion, we always designate the exponential map of a Lie group \( G \) by \( {\exp }^{G} \) , and reserve the undecorated notation exp for the Riemannian exponential map.

The next proposition describes some essential features of the exponential map. Recall that a subset of a vector space \( V \) is said to be star-shaped with respect to a point \( x \in  S \) if for every \( y \in  S \) , the line segment from \( x \) to \( y \) is contained in \( S \) .

Proposition 5.19 (Properties of the Exponential Map). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, and let exp: \( \mathcal{E} \rightarrow  M \) be its exponential map.

(a) \( \mathcal{E} \) is an open subset of TM containing the image of the zero section, and each set \( {\mathcal{E}}_{p} \subseteq  {T}_{p}M \) is star-shaped with respect to 0 .

(b) For each \( v \in  {TM} \) , the geodesic \( {\gamma }_{v} \) is given by

\[
{\gamma }_{v}\left( t\right)  = \exp \left( {tv}\right) \tag{5.17}
\]

for all \( t \) such that either side is defined.

(c) The exponential map is smooth.

(d) For each point \( p \in  M \) , the differential \( d{\left( {\exp }_{p}\right) }_{0} : {T}_{0}\left( {{T}_{p}M}\right)  \cong  {T}_{p}M \rightarrow  {T}_{p}M \) is the identity map of \( {T}_{p}M \) , under the usual identification of \( {T}_{0}\left( {{T}_{p}M}\right) \) with \( {T}_{p}M \) .

Proof. Write \( n = \dim M \) . The rescaling lemma with \( t = 1 \) says precisely that \( \exp \left( {cv}\right)  = {\gamma }_{cv}\left( 1\right)  = {\gamma }_{v}\left( c\right) \) whenever either side is defined; this is (b). Moreover, if \( v \in  {\mathcal{E}}_{p} \) , then by definition \( {\gamma }_{v} \) is defined at least on \( \left\lbrack  {0,1}\right\rbrack \) . Thus for \( 0 \leq  t \leq  1 \) , the rescaling lemma says that

\[
{\exp }_{p}\left( {tv}\right)  = {\gamma }_{tv}\left( 1\right)  = {\gamma }_{v}\left( t\right)
\]

is defined. This shows that \( {\mathcal{E}}_{p} \) is star-shaped with respect to 0 .

Next we will show that \( \mathcal{E} \) is open and exp is smooth. To do so, we revisit the proof of the existence and uniqueness theorem for geodesics (Theorem 4.27) and reformulate it in a more invariant way. Let \( \left( {x}^{i}\right) \) be any smooth local coordinates on an open set \( U \subseteq  M \) , let \( \pi  : {TM} \rightarrow  M \) be the projection, and let \( \left( {{x}^{i},{v}^{i}}\right) \) denote the associated natural coordinates for \( {\pi }^{-1}\left( U\right)  \subseteq  {TM} \) (see p. 384). In terms of these coordinates, formula (4.18) defines a smooth vector field \( G \) on \( {\pi }^{-1}\left( U\right) \) . The integral curves of \( G \) are the curves \( \eta \left( t\right)  = \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) ,{v}^{1}\left( t\right) ,\ldots ,{v}^{n}\left( t\right) }\right) \) that satisfy the system of ODEs given by (4.17), which is equivalent to the geodesic equation under the substitution \( {v}^{k} = {\dot{x}}^{k} \) , as we observed in the proof of Theorem 4.27. Stated somewhat more invariantly, every integral curve of \( G \) on \( {\pi }^{-1}\left( U\right) \) projects to a geodesic under \( \pi  : {TM} \rightarrow  M \) (which in these coordinates is just \( \pi \left( {x, v}\right)  = x \) ); conversely, every geodesic \( \gamma \left( t\right)  = \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) }\right) \) in \( U \) lifts to an integral curve of \( G \) in \( {\pi }^{-1}\left( U\right) \) by setting \( {v}^{i}\left( t\right)  = {\dot{x}}^{i}\left( t\right) \) .

The importance of \( G \) stems from the fact that it actually defines a global vector field on the total space of \( {TM} \) , called the geodesic vector field. We could verify this by computing the transformation law for the components of \( G \) under a change of coordinates and showing that they take the same form in every coordinate chart; but fortunately there is a way to avoid that messy computation. The key observation, to be proved below, is that \( G \) acts on a function \( f \in  {C}^{\infty }\left( {TM}\right) \) by

\[
{Gf}\left( {p, v}\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}f\left( {{\gamma }_{v}\left( t\right) ,{\gamma }_{v}^{\prime }\left( t\right) }\right) . \tag{5.18}
\]

(Here and whenever convenient, we use the notations \( \left( {p, v}\right) \) and \( v \) interchangeably for an element \( v \in  {T}_{p}M \) , depending on whether we wish to emphasize the point at which \( v \) is tangent.) Since this formula is independent of coordinates, it shows that the various definitions of \( G \) given by (4.18) in different coordinate systems agree.

To prove that \( G \) satisfies (5.18), we write the components of the geodesic \( {\gamma }_{v}\left( t\right) \) as \( {x}^{i}\left( t\right) \) and those of its velocity as \( {v}^{i}\left( t\right)  = {\dot{x}}^{i}\left( t\right) \) . Using the chain rule and the geodesic equation in the form (4.17), we can write the right-hand side of (5.18) as

\[
{\left. \left( \frac{\partial f}{\partial {x}^{k}}\left( x\left( t\right) , v\left( t\right) \right) {\dot{x}}^{k}\left( t\right)  + \frac{\partial f}{\partial {v}^{k}}\left( x\left( t\right) , v\left( t\right) \right) {\dot{v}}^{k}\left( t\right) \right) \right| }_{t = 0}
\]

\[
= \frac{\partial f}{\partial {x}^{k}}\left( {p, v}\right) {v}^{k} - \frac{\partial f}{\partial {v}^{k}}\left( {p, v}\right) {v}^{i}{v}^{j}{\Gamma }_{ij}^{k}\left( p\right)
\]

\[
= {Gf}\left( {p, v}\right) \text{ . }
\]

The fundamental theorem on flows (Thm. A.42) shows that there exist an open set \( \mathcal{D} \subseteq  \mathbb{R} \times  {TM} \) containing \( \{ 0\}  \times  {TM} \) and a smooth map \( \theta  : \mathcal{D} \rightarrow  {TM} \) , such that each curve \( {\theta }^{\left( p, v\right) }\left( t\right)  = \theta \left( {t,\left( {p, v}\right) }\right) \) is the unique maximal integral curve of \( G \) starting at \( \left( {p, v}\right) \) , defined on an open interval containing 0 .

Now suppose \( \left( {p, v}\right)  \in  \mathcal{E} \) . This means that the geodesic \( {\gamma }_{v} \) is defined at least on the interval \( \left\lbrack  {0,1}\right\rbrack \) , and therefore so is the integral curve of \( G \) starting at \( \left( {p, v}\right)  \in  {TM} \) . Since \( \left( {1,\left( {p, v}\right) }\right)  \in  \mathcal{D} \) , there is a neighborhood of \( \left( {1,\left( {p, v}\right) }\right) \) in \( \mathbb{R} \times  {TM} \) on which the flow of \( G \) is defined (Fig. 5.2). In particular, this means that there is a neighborhood of \( \left( {p, v}\right) \) on which the flow exists for \( t \in  \left\lbrack  {0,1}\right\rbrack \) , and therefore on which the exponential map is defined. This shows that \( \mathcal{E} \) is open.

![bo_d7dtff491nqc73eq8m7g_141_416_208_670_593_0.jpg](images/bo_d7dtff491nqc73eq8m7g_141_416_208_670_593_0.jpg)

Fig. 5.2: \( \mathcal{E} \) is open

Since geodesics are projections of integral curves of \( G \) , it follows that the exponential map can be expressed as

\[
{\exp }_{p}\left( v\right)  = {\gamma }_{v}\left( 1\right)  = \pi  \circ  \theta \left( {1,\left( {p, v}\right) }\right)
\]

wherever it is defined, and therefore \( {\exp }_{p}\left( v\right) \) is a smooth function of \( \left( {p, v}\right) \) .

To compute \( d{\left( {\exp }_{p}\right) }_{0}\left( v\right) \) for an arbitrary vector \( v \in  {T}_{p}M \) , we just need to choose a curve \( \tau \) in \( {T}_{p}M \) starting at 0 whose initial velocity is \( v \) , and compute the initial velocity of \( {\exp }_{p} \circ  \tau \) . A convenient curve is \( \tau \left( t\right)  = {tv} \) , which yields

\[
d{\left( {\exp }_{p}\right) }_{0}\left( v\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}\left( {{\exp }_{p} \circ  \tau }\right) \left( t\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}{\exp }_{p}\left( {tv}\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}{\gamma }_{v}\left( t\right)  = v.
\]

Thus \( d{\left( {\exp }_{p}\right) }_{0} \) is the identity map.

Corollary 5.14 on the naturality of geodesics translates into the following important property of the exponential map.

Proposition 5.20 (Naturality of the Exponential Map). Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian or pseudo-Riemannian manifolds and \( \varphi  : M \rightarrow  \widetilde{M} \) is a local isometry. Then for every \( p \in  M \) , the following diagram commutes: where \( {\mathcal{E}}_{p} \subseteq  {T}_{p}M \) and \( {\widetilde{\mathcal{E}}}_{\varphi \left( p\right) } \subseteq  {T}_{\varphi \left( p\right) }\widetilde{M} \) are the domains of the restricted exponential maps \( {\exp }_{p} \) (with respect to \( g \) ) and \( {\exp }_{\varphi \left( p\right) } \) (with respect to \( \widetilde{g} \) ), respectively.

![bo_d7dtff491nqc73eq8m7g_141_556_1830_416_230_0.jpg](images/bo_d7dtff491nqc73eq8m7g_141_556_1830_416_230_0.jpg)

Exercise 5.21. Prove Proposition 5.20.

An important consequence of the naturality of the exponential map is the following proposition, which says that local isometries of connected manifolds are completely determined by their values and differentials at a single point.

Proposition 5.22. Let \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) be Riemannian or pseudo-Riemannian manifolds, with \( M \) connected. Suppose \( \varphi ,\psi  : M \rightarrow  \widetilde{M} \) are local isometries such that for some point \( p \in  M \) , we have \( \varphi \left( p\right)  = \psi \left( p\right) \) and \( d{\varphi }_{p} = d{\psi }_{p} \) . Then \( \varphi  \equiv  \psi \) .

Proof. Problem 5-10.

A Riemannian or pseudo-Riemannian manifold \( \left( {M, g}\right) \) is said to be geodesically complete if every maximal geodesic is defined for all \( t \in  \mathbb{R} \) , or equivalently if the domain of the exponential map is all of \( {TM} \) . It is easy to construct examples of manifolds that are not geodesically complete; for example, in every proper open subset of \( {\mathbb{R}}^{n} \) with its Euclidean metric or with a pseudo-Euclidean metric, there are geodesics that reach the boundary in finite time. Similarly, on \( {\mathbb{R}}^{n} \) with the metric \( {\left( {\sigma }^{-1}\right) }^{ * }\overset{ \circ  }{g} \) obtained from the sphere by stereographic projection, there are geodesics that escape to infinity in finite time. Geodesically complete manifolds are the natural setting for global questions in Riemannian or pseudo-Riemannian geometry; beginning with Chapter 6, most of our attention will be focused on them.

## Normal Neighborhoods and Normal Coordinates

We continue to let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold of dimension \( n \) (without boundary). Recall that for every \( p \in  M \) , the restricted exponential map \( {\exp }_{p} \) maps the open subset \( {\mathcal{E}}_{p} \subseteq  {T}_{p}M \) smoothly into \( M \) . Because \( d{\left( {\exp }_{p}\right) }_{0} \) is invertible, the inverse function theorem guarantees that there exist a neighborhood \( V \) of the origin in \( {T}_{p}M \) and a neighborhood \( U \) of \( p \) in \( M \) such that \( {\exp }_{p} : V \rightarrow  U \) is a diffeomorphism. A neighborhood \( U \) of \( p \in  M \) that is the diffeomorphic image under \( {\exp }_{p} \) of a star-shaped neighborhood of \( 0 \in  {T}_{p}M \) is called a normal neighborhood of \( p \) .

Every orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) determines a basis isomorphism \( B : {\mathbb{R}}^{n} \rightarrow \; {T}_{p}M \) by \( B\left( {{x}^{1},\ldots ,{x}^{n}}\right)  = {x}^{i}{b}_{i} \) . If \( U = {\exp }_{p}\left( V\right) \) is a normal neighborhood of \( p \) , we can combine this isomorphism with the exponential map to get a smooth coordinate map \( \varphi  = {B}^{-1} \circ  {\left( {\exp }_{p}{ \mid  }_{V}\right) }^{-1} : U \rightarrow  {\mathbb{R}}^{n} : \)

![bo_d7dtff491nqc73eq8m7g_142_549_1889_436_232_0.jpg](images/bo_d7dtff491nqc73eq8m7g_142_549_1889_436_232_0.jpg)

Such coordinates are called (Riemannian or pseudo-Riemannian) normal coordinates centered at p.

Proposition 5.23 (Uniqueness of Normal Coordinates). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian n-manifold, \( p \) a point of \( M \) , and \( U \) a normal neighborhood of \( p \) . For every normal coordinate chart on \( U \) centered at \( p \) , the coordinate basis is orthonormal at \( p \) ; and for every orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) , there is a unique normal coordinate chart \( \left( {x}^{i}\right) \) on \( U \) such that \( {\left. {\partial }_{i}\right| }_{p} = {b}_{i} \) for \( i = 1,\ldots , n \) . In the Riemannian case, any two normal coordinate charts \( \left( {x}^{i}\right) \) and \( \left( {\widetilde{x}}^{j}\right) \) are related by

\[
{\widetilde{x}}^{j} = {A}_{i}^{j}{x}^{i} \tag{5.19}
\]

for some (constant) matrix \( \left( {A}_{i}^{j}\right)  \in  \mathrm{O}\left( n\right) \) .

Proof. Let \( \varphi \) be a normal coordinate chart on \( U \) centered at \( p \) , with coordinate functions \( \left( {x}^{i}\right) \) . By definition, this means that \( \varphi  = {B}^{-1} \circ  {\exp }_{p}^{-1} \) , where \( B : {\mathbb{R}}^{n} \rightarrow  {T}_{p}M \) is the basis isomorphism determined by some orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) . Note that \( d{\varphi }_{p}^{-1} = d{\left( {\exp }_{p}\right) }_{0} \circ  d{B}_{0} = B \) because \( d{\left( {\exp }_{p}\right) }_{0} \) is the identity and \( B \) is linear. Thus \( {\left. {\partial }_{i}\right| }_{p} = d{\varphi }_{p}^{-1}\left( {\left. {\partial }_{i}\right| }_{0}\right)  = B\left( {\left. {\partial }_{i}\right| }_{0}\right)  = {b}_{i} \) , which shows that the coordinate basis is orthonormal at \( p \) . Conversely, every orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) yields a basis isomorphism \( B \) and thus a normal coordinate chart \( \varphi  = {B}^{-1} \circ  {\exp }_{p}^{-1} \) , which satisfies \( {\left. {\partial }_{i}\right| }_{p} = {b}_{i} \) by the computation above.

If \( \widetilde{\varphi } = {\widetilde{B}}^{-1} \circ  {\exp }_{p}^{-1} \) is another such chart, then

\[
\widetilde{\varphi } \circ  {\varphi }^{-1} = {\widetilde{B}}^{-1} \circ  {\exp }_{p}^{-1} \circ  {\exp }_{p} \circ  B = {\widetilde{B}}^{-1} \circ  B,
\]

which is a linear isometry of \( {\mathbb{R}}^{n} \) and therefore has the form (5.19) in terms of standard coordinates on \( {\mathbb{R}}^{n} \) . Since \( \left( {\widetilde{x}}^{j}\right) \) and \( \left( {x}^{i}\right) \) are the same coordinates if and only if \( \left( {A}_{i}^{j}\right) \) is the identity matrix, this shows that the normal coordinate chart associated with a given orthonormal basis is unique.

Proposition 5.24 (Properties of Normal Coordinates). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian n-manifold, and let \( \left( {U,\left( {x}^{i}\right) }\right) \) be any normal coordinate chart centered at \( p \in  M \) .

(a) The coordinates of \( p \) are \( \left( {0,\ldots ,0}\right) \) .

(b) The components of the metric at \( p \) are \( {g}_{ij} = {\delta }_{ij} \) if \( g \) is Riemannian, and \( {g}_{ij} = \; \pm  {\delta }_{ij} \) otherwise.

(c) For every \( v = {\left. {v}^{i}{\partial }_{i}\right| }_{p} \in  {T}_{p}M \) , the geodesic \( {\gamma }_{v} \) starting at \( p \) with initial velocity \( v \) is represented in normal coordinates by the line

\[
{\gamma }_{v}\left( t\right)  = \left( {t{v}^{1},\ldots , t{v}^{n}}\right) , \tag{5.20}
\]

as long as \( t \) is in some interval \( I \) containing 0 such that \( {\gamma }_{v}\left( I\right)  \subseteq  U \) .

(d) The Christoffel symbols in these coordinates vanish at \( p \) .

(e) All of the first partial derivatives of \( {g}_{ij} \) in these coordinates vanish at \( p \) .

Proof. Part (a) follows directly from the definition of normal coordinates, and parts (b) and (c) follow from Propositions 5.23 and 5.19(b), respectively.

To prove (d), let \( v = {\left. {v}^{i}{\partial }_{i}\right| }_{p} \in  {T}_{p}M \) be arbitrary. The geodesic equation (4.16) for \( {\gamma }_{v}\left( t\right)  = \left( {t{v}^{1},\ldots , t{v}^{n}}\right) \) simplifies to

\[
{\Gamma }_{ij}^{k}\left( {tv}\right) {v}^{i}{v}^{j} = 0.
\]

Evaluating this expression at \( t = 0 \) shows that \( {\Gamma }_{ij}^{k}\left( 0\right) {v}^{i}{v}^{j} = 0 \) for every index \( k \) and every vector \( v \) . In particular, with \( v = {\partial }_{a} \) for some fixed \( a \) , this shows that \( {\Gamma }_{aa}^{k} = 0 \) for each \( a \) and \( k \) (no summation). Substituting \( v = {\partial }_{a} + {\partial }_{b} \) and \( v = {\partial }_{b} - {\partial }_{a} \) for any fixed pair of indices \( a \) and \( b \) and subtracting, we conclude also that \( {\Gamma }_{ab}^{k} = 0 \) at \( p \) for all \( a, b, k \) . Finally,(e) follows from (d) together with (5.2) in the case \( {E}_{k} = {\partial }_{k} \) .

Because they are given by the simple formula (5.20), the geodesics starting at \( p \) and lying in a normal neighborhood of \( p \) are called radial geodesics. (But be warned that geodesics that do not pass through \( p \) do not in general have a simple form in normal coordinates.)

## Tubular Neighborhoods and Fermi Coordinates

The exponential map and normal coordinates give us a good understanding of the behavior of geodesics starting a point. In this section, we generalize those constructions to geodesics starting on any embedded submanifold. We restrict attention to the Riemannian case, because we will be using the Riemannian distance function.

Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( P \subseteq  M \) is an embedded submanifold, and \( \pi  : {NP} \rightarrow  P \) is the normal bundle of \( P \) in \( M \) . Let \( \mathcal{E} \subseteq  {TM} \) denote the domain of the exponential map of \( M \) , and let \( {\mathcal{E}}_{P} = \mathcal{E} \cap  {NP} \) . Let \( E : {\mathcal{E}}_{P} \rightarrow  M \) denote the restriction of exp (the exponential map of \( M \) ) to \( {\mathcal{E}}_{P} \) . We call \( E \) the normal exponential map of \( P \) in \( M \) .

A normal neighborhood of \( \mathbf{P} \) in \( \mathbf{M} \) is an open subset \( U \subseteq  M \) that is the diffeomorphic image under \( E \) of an open subset \( V \subseteq  {\mathcal{E}}_{P} \) whose intersection with each fiber \( {N}_{x}P \) is star-shaped with respect to 0 . We will be primarily interested in normal neighborhoods of the following type: a normal neighborhood of \( P \) in \( M \) is called a tubular neighborhood if it is the diffeomorphic image under \( E \) of a subset \( V \subseteq  {\mathcal{E}}_{P} \) of the form

\[
V = \left\{  {\left( {x, v}\right)  \in  {NP} : {\left| v\right| }_{g} < \delta \left( x\right) }\right\}  , \tag{5.21}
\]

for some positive continuous function \( \delta  : P \rightarrow  \mathbb{R} \) (Fig. 5.3). If \( U \) is the diffeomorphic image of such a set \( V \) for a constant function \( \delta \left( x\right)  \equiv  \varepsilon \) , then it is called a uniform tubular neighborhood of radius \( \varepsilon \) , or an \( \varepsilon \) -tubular neighborhood.

Theorem 5.25 (Tubular Neighborhood Theorem). Let \( \left( {M, g}\right) \) be a Riemannian manifold. Every embedded submanifold of \( M \) has a tubular neighborhood in \( M \) , and every compact submanifold has a uniform tubular neighborhood.

![bo_d7dtff491nqc73eq8m7g_145_208_191_527_373_0.jpg](images/bo_d7dtff491nqc73eq8m7g_145_208_191_527_373_0.jpg)

Fig. 5.3: A tubular neighborhood

![bo_d7dtff491nqc73eq8m7g_145_801_222_489_343_0.jpg](images/bo_d7dtff491nqc73eq8m7g_145_801_222_489_343_0.jpg)

Fig. 5.4: Injectivity of \( E \)

Proof. Let \( P \subseteq  M \) be an embedded submanifold, and let \( {P}_{0} \subseteq  {NP} \) be the subset \( \{ \left( {x,0}\right)  : x \in  P\} \) (the image of the zero section of \( {NP} \) ). We begin by showing that the normal exponential map \( E \) is a local diffeomorphism on a neighborhood of \( {P}_{0} \) . By the inverse function theorem, it suffices to show that the differential \( d{E}_{\left( x,0\right) } \) is bijective at each point \( \left( {x,0}\right)  \in  {P}_{0} \) . The restriction of \( E \) to \( {P}_{0} \) is just the diffeomorphism \( {P}_{0} \rightarrow  P \) followed by the embedding \( P \hookrightarrow  M \) , so \( d{E}_{\left( x,0\right) } \) maps the subspace \( {T}_{\left( x,0\right) }{P}_{0} \subseteq  {T}_{\left( x,0\right) }{NP} \) isomorphically onto \( {T}_{x}P \) . On the other hand, on the fiber \( {N}_{x}P, E \) agrees with the restricted exponential map \( {\exp }_{x} \) , which is a diffeomorphism near 0, so \( d{E}_{\left( x,0\right) } \) maps \( {T}_{\left( x,0\right) }\left( {{N}_{x}P}\right)  \subseteq  {T}_{\left( x,0\right) }{NP} \) isomorphically onto \( {N}_{x}P \) . Since \( {T}_{x}M = {T}_{x}P \oplus  {N}_{x}P \) , this shows that \( d{E}_{\left( x,0\right) } \) is surjective, and hence it is bijective for dimensional reasons. Thus \( E \) is a diffeomorphism on a neighborhood of \( \left( {x,0}\right) \) in \( {NP} \) , which we can take to be of the form

\[
{V}_{\delta }\left( x\right)  = \left\{  {\left( {{x}^{\prime },{v}^{\prime }}\right)  \in  {NP} : {d}_{g}\left( {x,{x}^{\prime }}\right)  < \delta ,{\left| {v}^{\prime }\right| }_{g} < \delta }\right\} \tag{5.22}
\]

for some \( \delta  > 0 \) . (Here we are using the fact that \( P \) is embedded in \( M \) , so it has the subspace topology.)

To complete the proof, we need to show that there is a set \( V \subseteq  {\mathcal{E}}_{P} \) of the form (5.21) on which \( E \) is a diffeomorphism onto its image. For each point \( x \in  P \) , define

\[
\Delta \left( x\right)  = \sup \{ \delta  \leq  1 : E\text{ is a diffeomorphism from }{V}_{\delta }\left( x\right) \text{ to its image }\} . \tag{5.23}
\]

The argument in the preceding paragraph implies that \( \Delta \left( x\right) \) is positive for each \( x \) . Note that \( E \) is injective on the entire set \( {V}_{\Delta \left( x\right) }\left( x\right) \) , because any two points \( \left( {{x}_{1},{v}_{1}}\right) ,\left( {{x}_{2},{v}_{2}}\right) \) in this set are in \( {V}_{\delta }\left( x\right) \) for some \( \delta  < \Delta \left( x\right) \) . Because it is an injective local diffeomorphism, \( E \) is actually a diffeomorphism from \( {V}_{\Delta \left( x\right) }\left( x\right) \) onto its image.

Next we show that the function \( \Delta  : P \rightarrow  \mathbb{R} \) is continuous. For any \( x,{x}^{\prime } \in  P \) , if \( {d}_{g}\left( {x,{x}^{\prime }}\right)  < \Delta \left( x\right) \) , then the triangle inequality shows that \( {V}_{\delta }\left( {x}^{\prime }\right) \) is contained in \( {V}_{\Delta \left( x\right) }\left( x\right) \) for \( \delta  = \Delta \left( x\right)  - {d}_{g}\left( {x,{x}^{\prime }}\right) \) , which implies that \( \Delta \left( {x}^{\prime }\right)  \geq  \Delta \left( x\right)  - {d}_{g}\left( {x,{x}^{\prime }}\right) \) , or

\[
\Delta \left( x\right)  - \Delta \left( {x}^{\prime }\right)  \leq  {d}_{g}\left( {x,{x}^{\prime }}\right) . \tag{5.24}
\]

If \( {d}_{g}\left( {x,{x}^{\prime }}\right)  \geq  \Delta \left( x\right) \) , then (5.24) holds for trivial reasons. Reversing the roles of \( x \) and \( {x}^{\prime } \) yields an analogous inequality, which shows that \( \left| {\Delta \left( x\right)  - \Delta \left( {x}^{\prime }\right) }\right|  \leq  {d}_{g}\left( {x,{x}^{\prime }}\right) \) , so \( \Delta \) is continuous.

Let \( V = \left\{  {\left( {x, v}\right)  \in  {NP} : {\left| v\right| }_{g} < \frac{1}{2}\Delta \left( x\right) }\right\} \) , which is an open subset of \( {NP} \) containing \( {P}_{0} \) . We show that \( E \) is injective on \( V \) . Suppose \( \left( {x, v}\right) \) and \( \left( {{x}^{\prime },{v}^{\prime }}\right) \) are points in \( V \) such that \( E\left( {x, v}\right)  = E\left( {{x}^{\prime },{v}^{\prime }}\right) \) (Fig. 5.4). Assume without loss of generality that \( \Delta \left( {x}^{\prime }\right)  \leq  \Delta \left( x\right) \) . Because \( {\exp }_{x}\left( v\right)  = {\exp }_{{x}^{\prime }}\left( {v}^{\prime }\right) \) , there is an admissible curve from \( x \) to \( {x}^{\prime } \) of length \( {\left| v\right| }_{g} + {\left| {v}^{\prime }\right| }_{g} \) , and thus

\[
{d}_{g}\left( {x,{x}^{\prime }}\right)  \leq  {\left| v\right| }_{g} + {\left| {v}^{\prime }\right| }_{g} < \frac{1}{2}\Delta \left( x\right)  + \frac{1}{2}\Delta \left( {x}^{\prime }\right)  \leq  \Delta \left( x\right) .
\]

Therefore, both \( \left( {x, v}\right) \) and \( \left( {{x}^{\prime },{v}^{\prime }}\right) \) are in \( {V}_{\Delta \left( x\right) }\left( x\right) \) . Since \( E \) is injective on this set, this implies \( \left( {x, v}\right)  = \left( {{x}^{\prime },{v}^{\prime }}\right) \) .

The set \( U = E\left( V\right) \) is open in \( M \) because \( {\left. E\right| }_{V} \) is a local diffeomorphism and thus an open map, and \( E : V \rightarrow  U \) is a diffeomorphism. Therefore, \( U \) is a tubular neighborhood of \( P \) .

Finally, if \( P \) is compact, then the continuous function \( \frac{1}{2}\Delta \) achieves a minimum value \( \varepsilon  > 0 \) on \( P \) , so \( U \) contains a uniform tubular neighborhood of radius \( \varepsilon \) .

## Fermi Coordinates

Now we will construct coordinates on a tubular neighborhood that are analogous to Riemannian normal coordinates around a point. Let \( P \) be an embedded \( p \) -dimensional submanifold of a Riemannian \( n \) -manifold \( \left( {M, g}\right) \) , and let \( U \subseteq  M \) be a normal neighborhood of \( P \) , with \( U = E\left( V\right) \) for some appropriate open subset \( V \subseteq  {NP} \) .

Let \( \left( {{W}_{0},\psi }\right) \) be a smooth coordinate chart for \( P \) , and let \( \left( {{E}_{1},\ldots ,{E}_{n - p}}\right) \) be a local orthonormal frame for the normal bundle \( {NP} \) ; by shrinking \( {W}_{0} \) if necessary, we can assume that the coordinates and the local frame are defined on the same open subset \( {W}_{0} \subseteq  P \) . Let \( {\widehat{W}}_{0} = \psi \left( {W}_{0}\right)  \subseteq  {\mathbb{R}}^{p} \) , and let \( {\left. NP\right| }_{{W}_{0}} \) be the portion of the normal bundle over \( {W}_{0} \) . The coordinate map \( \psi \) and frame \( \left( {E}_{j}\right) \) yield a diffeomorphism \( B : {\widehat{W}}_{0} \times  {\mathbb{R}}^{n - p} \rightarrow  {\left. NP\right| }_{{W}_{0}} \) defined by

\[
B\left( {{x}^{1},\ldots ,{x}^{p},{v}^{1},\ldots ,{v}^{n - p}}\right)  = \left( {q,{\left. {v}^{1}{E}_{1}\right| }_{q} + \cdots  + {\left. {v}^{n - p}{E}_{n - p}\right| }_{q}}\right) ,
\]

where \( q = {\psi }^{-1}\left( {{x}^{1},\ldots ,{x}^{p}}\right) \) . Let \( {V}_{0} = V \cap  {NP}{ \mid  }_{{W}_{0}} \subseteq  {NP} \) and \( {U}_{0} = E\left( {V}_{0}\right)  \subseteq  M \) , and define a smooth coordinate map \( \varphi  : {U}_{0} \rightarrow  {\mathbb{R}}^{n} \) by \( \varphi  = {B}^{-1} \circ  {\left( {\left. E\right| }_{{V}_{0}}\right) }^{-1} \) :

![bo_d7dtff491nqc73eq8m7g_146_473_1800_590_264_0.jpg](images/bo_d7dtff491nqc73eq8m7g_146_473_1800_590_264_0.jpg)

The coordinate map can also be written

\[
\varphi  : E\left( {q,{\left. {v}^{1}{E}_{1}\right| }_{q} + \cdots  + {\left. {v}^{n - p}{E}_{n - p}\right| }_{q}}\right)  \mapsto  \left( {{x}^{1}\left( q\right) ,\ldots ,{x}^{p}\left( q\right) ,{v}^{1},\ldots ,{v}^{n - p}}\right) . \tag{5.25}
\]

Coordinates of this form are called Fermi coordinates, after the Italian physicist Enrico Fermi (1901-1954), who first introduced them in the special case in which \( P \) is the image of a geodesic in \( M \) . The generalization to arbitrary submanifolds was first introduced by Alfred Gray [Gra82]. (See also [Gra04] for a detailed study of the geometry of tubular neighborhoods.)

Here is the analogue of Proposition 5.24 for Fermi coordinates.

Proposition 5.26 (Properties of Fermi Coordinates). Let \( P \) be an embedded p-dimensional submanifold of a Riemannian n-manifold \( \left( {M, g}\right) \) , let \( U \) be a normal neighborhood of \( P \) in \( M \) , and let \( \left( {{x}^{1},\ldots ,{x}^{p},{v}^{1},\ldots ,{v}^{n - p}}\right) \) be Fermi coordinates on an open subset \( {U}_{0} \subseteq  U \) . For convenience, we also write \( {x}^{p + j} = {v}^{j} \) for \( j = 1,\ldots , n - p. \)

(a) \( P \cap  {U}_{0} \) is the set of points where \( {x}^{p + 1} = \cdots  = {x}^{n} = 0 \) .

(b) At each point \( q \in  P \cap  {U}_{0} \) , the metric components satisfy the following:

\[
{g}_{ij} = {g}_{ji} = \left\{  \begin{array}{ll} 0, & 1 \leq  i \leq  p\text{ and }p + 1 \leq  j \leq  n, \\  {\delta }_{ij}, & p + 1 \leq  i, j \leq  n. \end{array}\right.
\]

(c) For every \( q \in  P \cap  {U}_{0} \) and \( v = {\left. {v}^{1}{E}_{1}\right| }_{q} + \cdots  + {\left. {v}^{n - p}{E}_{n - p}\right| }_{q} \in  {N}_{q}P \) , the geodesic \( {\gamma }_{v} \) starting at \( q \) with initial velocity \( v \) is the curve with coordinate expression \( {\gamma }_{v}\left( t\right)  = \left( {{x}^{1}\left( q\right) ,\ldots ,{x}^{p}\left( q\right) , t{v}^{1},\ldots , t{v}^{n - p}}\right) \) .

(d) At each \( q \in  P \cap  {U}_{0} \) , the Christoffel symbols in these coordinates satisfy \( {\Gamma }_{ij}^{k} = 0 \) , provided \( p + 1 \leq  i, j \leq  n \) .

(e) At each \( q \in  P \cap  {U}_{0} \) , the partial derivatives \( {\partial }_{i}{g}_{jk}\left( q\right) \) vanish for \( p + 1 \leq  i, j, k \leq \; n \) .

Proof. Problem 5-18.

## Geodesics of the Model Spaces

In this section we determine the geodesics of the three types of frame-homogeneous Riemannian manifolds defined in Chapter 3. We could, of course, compute the Christoffel symbols of these metrics in suitable coordinates, and try to find the geodesics by solving the appropriate differential equations; but for these spaces, much easier methods are available based on symmetry and other geometric considerations.

## Euclidean Space

On \( {\mathbb{R}}^{n} \) with the Euclidean metric, Proposition 5.12 shows that the Levi-Civita connection is the Euclidean connection. Therefore, as one would expect, constant-coefficient vector fields are parallel, and the Euclidean geodesics are straight lines with constant-speed parametrizations (Exercises 4.29 and 4.30). Every Euclidean space is geodesically complete.

## Spheres

Because the round metric on the sphere \( {\mathbb{S}}^{n}\left( R\right) \) is induced by the Euclidean metric on \( {\mathbb{R}}^{n + 1} \) , it is easy to determine the geodesics on a sphere using Corollary 5.2. Define a great circle on \( {\mathbb{S}}^{n}\left( R\right) \) to be any subset of the form \( {\mathbb{S}}^{n}\left( R\right)  \cap  \Pi \) , where \( \Pi  \subseteq  {\mathbb{R}}^{n + 1} \) is a 2-dimensional linear subspace.

Proposition 5.27. A nonconstant curve on \( {\mathbb{S}}^{n}\left( R\right) \) is a maximal geodesic if and only if it is a periodic constant-speed curve whose image is a great circle. Thus every sphere is geodesically complete.

Proof. Let \( p \in  {\mathbb{S}}^{n}\left( R\right) \) be arbitrary. Because \( f\left( x\right)  = {\left| x\right| }^{2} \) is a defining function for \( {\mathbb{S}}^{n}\left( R\right) \) , a vector \( v \in  {T}_{p}{\mathbb{R}}^{n + 1} \) is tangent to \( {\mathbb{S}}^{n}\left( R\right) \) if and only if \( d{f}_{p}\left( v\right)  = 2\langle v, p\rangle  = \) 0, where we think of \( p \) as a vector by means of the usual identification of \( {\mathbb{R}}^{n + 1} \) with \( {T}_{p}{\mathbb{R}}^{n + 1} \) . Thus \( {T}_{p}{\mathbb{S}}^{n}\left( R\right) \) is exactly the set of vectors orthogonal to \( p \) .

Suppose \( v \) is an arbitrary nonzero vector in \( {T}_{p}{\mathbb{S}}^{n}\left( R\right) \) . Let \( a = \left| v\right| /R \) and \( \widehat{v} = v/a \) (so \( \left| \widehat{v}\right|  = R \) ), and consider the smooth curve \( \gamma  : \mathbb{R} \rightarrow  {\mathbb{R}}^{n + 1} \) given by

\[
\gamma \left( t\right)  = \left( {\cos {at}}\right) p + \left( {\sin {at}}\right) \widehat{v}.
\]

By direct computation, \( {\left| \gamma \left( t\right) \right| }^{2} = {R}^{2} \) , so \( \gamma \left( t\right)  \in  {\mathbb{S}}^{n}\left( R\right) \) for all \( t \) . Moreover,

\[
{\gamma }^{\prime }\left( t\right)  =  - a\left( {\sin {at}}\right) p + a\left( {\cos {at}}\right) \widehat{v},
\]

\[
{\gamma }^{\prime \prime }\left( t\right)  =  - {a}^{2}\left( {\cos {at}}\right) p - {a}^{2}\left( {\sin {at}}\right) \widehat{v}.
\]

Because \( {\gamma }^{\prime \prime }\left( t\right) \) is proportional to \( \gamma \left( t\right) \) (thinking of both as vectors in \( {\mathbb{R}}^{n + 1} \) ), it follows that \( {\gamma }^{\prime \prime }\left( t\right) \) is \( \bar{g} \) -orthogonal to \( {T}_{\gamma \left( t\right) }{\mathbb{S}}^{n}\left( R\right) \) , so \( \gamma \) is a geodesic in \( {\mathbb{S}}^{n}\left( R\right) \) by Corollary 5.2. Since \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = a\widehat{v} = v \) , it follows that \( \gamma  = {\gamma }_{v} \) .

Each \( {\gamma }_{v} \) is periodic of period \( {2\pi }/a \) , and has constant speed by Corollary 5.6 (or by direct computation). The image of \( {\gamma }_{v} \) is the great circle formed by the intersection of \( {\mathbb{S}}^{n}\left( R\right) \) with the linear subspace spanned by \( \{ p,\widehat{v}\} \) , as you can check.

Conversely, suppose \( C \) is a great circle formed by intersecting \( {\mathbb{S}}^{n}\left( R\right) \) with a 2-dimensional subspace \( \Pi \) , and let \( \{ v, w\} \) be an orthonormal basis for \( \Pi \) . Then \( C \) is the image of the geodesic with initial point \( p = {Rw} \) and initial velocity \( v \) .

![bo_d7dtff491nqc73eq8m7g_149_433_183_661_709_0.jpg](images/bo_d7dtff491nqc73eq8m7g_149_433_183_661_709_0.jpg)

Fig. 5.5: A great hyperbola

![bo_d7dtff491nqc73eq8m7g_149_278_1004_956_418_0.jpg](images/bo_d7dtff491nqc73eq8m7g_149_278_1004_956_418_0.jpg)

## Hyperbolic Spaces

The geodesics of hyperbolic spaces can be determined by an analogous procedure using the hyperboloid model.

Proposition 5.28. A nonconstant curve in a hyperbolic space is a maximal geodesic if and only if it is a constant-speed embedding of \( \mathbb{R} \) whose image is one of the following:

(a) HYPERBOLOID MODEL: The intersection of \( {\mathbb{H}}^{n}\left( R\right) \) with a 2-dimensional linear subspace of \( {\mathbb{R}}^{n,1} \) , called a great hyperbola (Fig. 5.5).

(b) BELTRAMI-KLEIN MODEL: The interior of a line segment whose endpoints both lie on \( \partial {\mathbb{K}}^{n}\left( R\right) \) (Fig. 5.6).

![bo_d7dtff491nqc73eq8m7g_150_505_187_519_372_0.jpg](images/bo_d7dtff491nqc73eq8m7g_150_505_187_519_372_0.jpg)

Fig. 5.8: Geodesics of \( {\mathbb{U}}^{n}\left( R\right) \)

(c) BALL MODEL: The interior of a diameter of \( {\mathbb{B}}^{n}\left( R\right) \) , or the intersection of \( {\mathbb{B}}^{n}\left( R\right) \) with a Euclidean circle that intersects \( \partial {\mathbb{B}}^{n}\left( R\right) \) orthogonally (Fig. 5.7).

(d) HALF-SPACE MODEL: The intersection of \( {\mathbb{U}}^{n}\left( R\right) \) with one of the following: a line parallel to the \( y \) -axis or a Euclidean circle with center on \( \partial {\mathbb{U}}^{n}\left( R\right) \) (Fig. 5.8).

Every hyperbolic space is geodesically complete.

Proof. We begin with the hyperboloid model, for which the proof is formally quite similar to what we just did for the sphere. Since the Riemannian connection on \( {\mathbb{H}}^{n}\left( R\right) \) is equal to the tangential connection by Proposition 5.12, it follows from Corollary 5.2 that a smooth curve \( \gamma  : I \rightarrow  {\mathbb{H}}^{n}\left( R\right) \) is a geodesic if and only if its acceleration \( {\gamma }^{\prime \prime }\left( t\right) \) is everywhere \( \bar{q} \) -orthogonal to \( {T}_{\gamma \left( t\right) }{\mathbb{H}}^{n}\left( R\right) \) (where \( \bar{q} = {\bar{q}}^{\left( n,1\right) } \) is the Minkowski metric).

Let \( p \in  {\mathbb{H}}^{n}\left( R\right) \) be arbitrary. Note that \( f\left( x\right)  = \bar{q}\left( {x, x}\right) \) is a defining function for \( {\mathbb{H}}^{n}\left( R\right) \) , and (3.10) shows that the gradient of \( f \) at \( p \) is equal to \( {2p} \) (where we regard \( p \) as a vector in \( {T}_{p}{\mathbb{R}}^{n,1} \) as before). It follows that a vector \( v \in  {T}_{p}{\mathbb{R}}^{n,1} \) is tangent to \( {\mathbb{H}}^{n}\left( R\right) \) if and only if \( \bar{q}\left( {p, v}\right)  = 0 \) . Let \( v \in  {T}_{p}{\mathbb{H}}^{n}\left( R\right) \) be an arbitrary nonzero vector. Put \( a = {\left| v\right| }_{\bar{q}}/R = \bar{q}{\left( v, v\right) }^{1/2}/R \) and \( \widehat{v} = v/a \) , and define \( \gamma  : \mathbb{R} \rightarrow \; {\mathbb{R}}^{n,1} \) by

\[
\gamma \left( t\right)  = \left( {\cosh {at}}\right) p + \left( {\sinh {at}}\right) \widehat{v}.
\]

Direct computation shows that \( \gamma \) takes its values in \( {\mathbb{H}}^{n}\left( R\right) \) and that its acceleration vector is everywhere proportional to \( \gamma \left( t\right) \) . Thus \( {\gamma }^{\prime \prime }\left( t\right) \) is \( \bar{q} \) -orthogonal to \( {T}_{\gamma \left( t\right) }{\mathbb{H}}^{n}\left( R\right) \) , so \( \gamma \) is a geodesic in \( {\mathbb{H}}^{n}\left( R\right) \) and therefore has constant speed. Because it satisfies the initial conditions \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) , it is equal to \( {\gamma }_{v} \) . Note that \( {\gamma }_{v} \) is a smooth embedding of \( \mathbb{R} \) into \( {\mathbb{H}}^{n}\left( R\right) \) whose image is the great hyperbola formed by the intersection between \( {\mathbb{H}}^{n}\left( R\right) \) and the plane spanned by \( \{ p,\widehat{v}\} \) .

Conversely, suppose \( \Pi \) is any 2-dimensional linear subspace of \( {\mathbb{R}}^{n,1} \) that has nontrivial intersection with \( {\mathbb{H}}^{n}\left( R\right) \) . Choose \( p \in  \Pi  \cap  {\mathbb{H}}^{n}\left( R\right) \) , and let \( v \) be another nonzero vector in \( \Pi \) that is \( \bar{q} \) -orthogonal to \( p \) , which implies \( v \in  {T}_{p}{\mathbb{H}}^{n}\left( R\right) \) . Using the computation above, we see that the image of the geodesic \( {\gamma }_{v} \) is the great hyperbola formed by the intersection of \( \Pi \) with \( {\mathbb{H}}^{n}\left( R\right) \) .

Before considering the other three models, note that since maximal geodesics in \( {\mathbb{H}}^{n}\left( R\right) \) are constant-speed embeddings of \( \mathbb{R} \) , it follows from naturality that maximal geodesics in each of the other models are also constant-speed embeddings of \( \mathbb{R} \) . Thus each model is geodesically complete, and to determine the geodesics in the other models we need only determine their images.

Consider the Beltrami-Klein model. Recall the isometry \( c : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{K}}^{n}\left( R\right) \) given by \( c\left( {\xi ,\tau }\right)  = {R\xi }/\tau \) (see (3.11)). The image of a maximal geodesic in \( {\mathbb{H}}^{n}\left( R\right) \) is a great hyperbola, which is the set of points \( \left( {\xi ,\tau }\right)  \in  {\mathbb{H}}^{n}\left( R\right) \) that solve a system of \( n - 1 \) independent linear equations. Simple algebra shows that \( \left( {\xi ,\tau }\right) \) satisfies a linear equation \( {\alpha }_{i}{\xi }^{i} + {\beta \tau } = 0 \) if and only if \( w = c\left( {\xi ,\tau }\right)  = {R\xi }/\tau \) satisfies the affine equation \( {\alpha }_{i}{w}^{i} =  - {\beta R} \) . Thus \( c \) maps each great hyperbola onto the intersection of \( {\mathbb{K}}^{n}\left( R\right) \) with an affine subspace of \( {\mathbb{R}}^{n} \) , and since it is the image of a smooth curve, it must be the intersection of \( {\mathbb{K}}^{n}\left( R\right) \) with a straight line.

Next consider the Poincaré ball model. First consider the 2-dimensional case, and recall the inverse hyperbolic stereographic projection \( {\pi }^{-1} : {\mathbb{B}}^{2}\left( R\right)  \rightarrow  {\mathbb{H}}^{2}\left( R\right) \) constructed in Chapter 3:

\[
{\pi }^{-1}\left( u\right)  = \left( {\xi ,\tau }\right)  = \left( {\frac{2{R}^{2}u}{{R}^{2} - {\left| u\right| }^{2}}, R\frac{{R}^{2} + {\left| u\right| }^{2}}{{R}^{2} - {\left| u\right| }^{2}}}\right) .
\]

In this case, a great hyperbola is the set of points on \( {\mathbb{H}}^{2}\left( R\right) \) that satisfy a single linear equation \( {\alpha }_{i}{\xi }^{i} + {\beta \tau } = 0 \) . In the special case \( \beta  = 0 \) , this hyperbola is mapped by \( \pi \) to a straight line segment through the origin, as can easily be seen from the geometric definition of \( \pi \) . If \( \beta  \neq  0 \) , we can assume (after multiplying through by a constant if necessary) that \( \beta  =  - 1 \) , and write the linear equation as \( \tau  = {\alpha }_{i}{\xi }^{i} = \alpha  \cdot  \xi \) (where the dot represents the Euclidean dot product between elements of \( {\mathbb{R}}^{2} \) ). Under \( {\pi }^{-1} \) , this pulls back to the equation

\[
R\frac{{R}^{2} + {\left| u\right| }^{2}}{{R}^{2} - {\left| u\right| }^{2}} = \frac{2{R}^{2}\alpha  \cdot  u}{{R}^{2} - {\left| u\right| }^{2}}
\]

on the disk, which simplifies to

\[
{\left| u\right| }^{2} - {2R\alpha } \cdot  u + {R}^{2} = 0.
\]

Completing the square, we can write this as

\[
{\left| u - R\alpha \right| }^{2} = {R}^{2}\left( {{\left| \alpha \right| }^{2} - 1}\right) . \tag{5.26}
\]

If \( {\left| \alpha \right| }^{2} \leq  1 \) , this locus is either empty or a point on \( \partial {\mathbb{B}}^{2}\left( R\right) \) , so it contains no points in \( {\mathbb{B}}^{2}\left( R\right) \) . Since we are assuming that it is the image of a maximal geodesic, we must therefore have \( {\left| \alpha \right| }^{2} > 1 \) . In that case,(5.26) is the equation of a circle with center \( {R\alpha } \) and radius \( R\sqrt{{\left| \alpha \right| }^{2} - 1} \) . At a point \( {u}_{0} \) where the circle intersects \( \partial {\mathbb{B}}^{2}\left( R\right) \) , the three points \( 0,{u}_{0} \) , and \( {R\alpha } \) form a triangle with sides \( \left| {u}_{0}\right|  = R,\left| {R\alpha }\right| \) , and \( \left| {{u}_{0} - {R\alpha }}\right| \) (Fig. 5.9), which satisfy the Pythagorean identity by (5.26); therefore the circle meets \( \partial {\mathbb{B}}^{2}\left( R\right) \) in a right angle.

![bo_d7dtff491nqc73eq8m7g_152_434_210_657_373_0.jpg](images/bo_d7dtff491nqc73eq8m7g_152_434_210_657_373_0.jpg)

Fig. 5.9: Geodesics are arcs of circles orthogonal to the boundary of \( {\mathbb{H}}^{2}\left( R\right) \)

In the higher-dimensional case, a geodesic on \( {\mathbb{H}}^{n}\left( R\right) \) is determined by a 2-plane. If the 2-plane contains the point \( \left( {0,\ldots ,0, R}\right) \) , then the corresponding geodesic on \( {\mathbb{B}}^{n}\left( R\right) \) is a line through the origin as before. Otherwise, we can use an orthogonal transformation in the \( \left( {{\xi }^{1},\ldots ,{\xi }^{n}}\right) \) variables (which preserves \( {\breve{g}}_{R} \) ) to move this 2-plane so that it lies in the \( \left( {{\xi }^{1},{\xi }^{2},\tau }\right) \) subspace, and then we are in the same situation as in the 2-dimensional case.

Finally, consider the upper half-space model. The 2-dimensional case is easiest to analyze using complex notation. Recall the complex formula for the Cayley transform \( \kappa  : {\mathbb{U}}^{2}\left( R\right)  \rightarrow  {\mathbb{B}}^{2}\left( R\right) \) given in Chapter 3:

\[
\kappa \left( z\right)  = w = {iR}\frac{z - {iR}}{z + {iR}}.
\]

Substituting this into equation (5.26) and writing \( w = u + {iv} \) and \( \alpha  = a + {ib} \) in place of \( u = \left( {{u}^{1},{u}^{2}}\right) ,\alpha  = \left( {{\alpha }^{1},{\alpha }^{2}}\right) \) , we get

\[
{R}^{2}\frac{{\left| z - iR\right| }^{2}}{{\left| z + iR\right| }^{2}} - i{R}^{2}\overline{\alpha }\frac{z - {iR}}{z + {iR}} + i{R}^{2}\alpha \frac{\bar{z} + {iR}}{\bar{z} - {iR}} + {R}^{2}{\left| \alpha \right| }^{2} = {R}^{2}\left( {{\left| \alpha \right| }^{2} - 1}\right) .
\]

Multiplying through by \( \left( {z + {iR}}\right) \left( {\bar{z} - {iR}}\right) /2{R}^{2} \) and simplifying yields

\[
\left( {1 - b}\right) {\left| z\right| }^{2} - {2aRx} + \left( {b + 1}\right) {R}^{2} = 0.
\]

This is the equation of a circle with center on the \( x \) -axis, unless \( b = 1 \) , in which case the condition \( {\left| \alpha \right| }^{2} > 1 \) forces \( a \neq  0 \) , and then it is a straight line \( x = \) constant. The other class of geodesics on the ball, line segments through the origin, can be handled similarly.

In the higher-dimensional case, suppose first that \( \gamma  : \mathbb{R} \rightarrow  {\mathbb{U}}^{n}\left( R\right) \) is a maximal geodesic such that \( \gamma \left( 0\right) \) lies on the \( y \) -axis and \( {\gamma }^{\prime }\left( 0\right) \) is in the span of \( \left\{  {\partial /\partial {x}^{1},\partial /\partial y}\right\} \) . From the explicit formula (3.15) for \( \kappa \) , it follows that \( \kappa  \circ  \gamma \left( 0\right) \) lies on the \( v \) -axis in the ball, and \( {\left( \kappa  \circ  \gamma \right) }^{\prime }\left( 0\right) \) is in the span of \( \left\{  {\partial /\partial {u}^{1},\partial /\partial v}\right\} \) . The image of the geodesic \( \kappa  \circ  \gamma \) is either part of a line through the origin or an arc of a circle perpendicular to \( \partial {\mathbb{B}}^{n}\left( R\right) \) , both of which are contained in the \( \left( {{u}^{1}, v}\right) \) -plane. By the argument in the preceding paragraph, it then follows that the image of \( \gamma \) is contained in the \( \left( {{x}^{1}, y}\right) \) -plane and is either a vertical half-line or a semicircle centered on the \( y = 0 \) hyperplane. For the general case, note that translations and orthogonal transformations in the \( x \) -variables preserve vertical half-lines and circles centered on the \( y = 0 \) hyperplane in \( {\mathbb{U}}^{n}\left( R\right) \) , and they also preserve the metric \( {\breve{g}}_{R}^{3} \) . Given an arbitrary maximal geodesic \( \gamma  : \mathbb{R} \rightarrow  {\mathbb{U}}^{n}\left( R\right) \) , after applying an \( x \) -translation we may assume that \( \gamma \left( 0\right) \) lies on the \( y \) -axis, and after an orthogonal transformation in the \( x \) variables, we may assume that \( {\gamma }^{\prime }\left( 0\right) \) is in the span of \( \left\{  {\partial /\partial {x}^{1},\partial /\partial y}\right\} \) ; then the argument above shows that the image of \( \gamma \) is either a vertical half-line or a semicircle centered on the \( y = 0 \) hyperplane.

## Euclidean and Non-Euclidean Geometries

In two dimensions, our model spaces can be interpreted as models of classical Euclidean and non-Euclidean plane geometries.

## Euclidean Plane Geometry

Euclid's axioms for plane and spatial geometry, written around 300 BCE, became a model for axiomatic treatments of geometry, and indeed for all of mathematics. As standards of rigor evolved, mathematicians revised and added to Euclid's axioms in various ways. One axiom system that meets modern standards of rigor was created by David Hilbert [Hil71]. Here (in somewhat simplified form) are his axioms for plane geometry. (See [Hil71, Gan73, Gre93] for more complete treatments of Hilbert's axioms, and see [LeeAG] for a different axiomatic approach based on the real number system.)

Hilbert's Axioms For Euclidean Plane Geometry. The terms point, line, lies on, between, and congruent are primitive terms, and are thus left undefined. We make the following definitions:

- Given a line \( l \) and a point \( P \) , we say that \( l \) contains \( P \) if \( P \) lies on \( l \) .

- A set of points is said to be collinear if there is a line that contains them all.

- Given two distinct points \( A, B \) , the segment \( \overline{AB} \) is the set consisting of \( A, B \) , and all points \( C \) such that \( C \) is between \( A \) and \( B \) .

- The notation \( \overline{AB} \cong  \overline{{A}^{\prime }{B}^{\prime }} \) means that \( \overline{AB} \) is congruent to \( \overline{{A}^{\prime }{B}^{\prime }} \) .

- Given two distinct points \( A, B \) , the ray \( \overrightarrow{AB} \) is the set consisting of \( A, B \) , and all points \( C \) such that either \( C \) is between \( A \) and \( B \) or \( B \) is between \( A \) and \( C \) .

- An interior point of the ray \( \overrightarrow{AB} \) is a point that lies on \( \overrightarrow{AB} \) and is not equal to \( A \) .

- Given three noncollinear points \( A, O, B \) , the angle \( \angle {AOB} \) is the union of the rays \( \overrightarrow{OA} \) and \( \overrightarrow{OB} \) . - The notation \( \angle {ABC} \cong  \angle {A}^{\prime }{B}^{\prime }{C}^{\prime } \) means that \( \angle {ABC} \) is congruent to \( \angle {A}^{\prime }{B}^{\prime }{C}^{\prime } \) .

- Given a line \( l \) and two points \( A, B \) that do not lie on \( l \) , we say that \( A \) and \( B \) are on the same side of \( l \) if no point of \( \overline{AB} \) lies on \( l \) .

- Two lines are said to be parallel if there is no point that lies on both of them.

These terms are assumed to satisfy the following postulates, among others:

## Incidence Postulates:

(a) For any two distinct points \( A, B \) , there exists a unique line that contains both of them.

(b) There exist at least two points on each line, and there exist at least three noncollinear points.

## Order Postulates:

(a) If a point \( B \) lies between a point \( A \) and a point \( C \) , then \( A, B, C \) are three distinct points of a line, and \( B \) also lies between \( C \) and \( A \) .

(b) Given two distinct points \( A \) and \( C \) , there always exists at least one point \( B \) such that \( C \) lies between \( A \) and \( B \) .

(c) Given three distinct points on a line, no more than one of them lies between the other two.

(d) Let \( A, B, C \) be three noncollinear points, and let \( l \) be a line that does not contain any of them. If \( l \) contains a point of \( \overline{AB} \) , then it also contains a point of \( \overline{AC} \) or \( \overline{BC} \) .

## Congruence Postulates:

(a) If \( A, B \) are two points on a line \( l \) , and \( {A}^{\prime } \) is a point on a line \( {l}^{\prime } \) , then it is always possible to find a point \( {B}^{\prime } \) on a given ray of \( {l}^{\prime } \) starting at \( {A}^{\prime } \) such that \( \overline{AB} \cong  \overline{{A}^{\prime }{B}^{\prime }} \) .

(b) If segments \( \overline{{A}^{\prime }{B}^{\prime }} \) and \( \overline{{A}^{\prime \prime }{B}^{\prime \prime }} \) are congruent to the same segment \( \overline{AB} \) , then \( \overline{{A}^{\prime }{B}^{\prime }} \) and \( \overline{{A}^{\prime \prime }{B}^{\prime \prime }} \) are congruent to each other.

(c) On a line \( l \) , let \( \overline{AB} \) and \( \overline{BC} \) be two segments that, except for \( B \) , have no points in common. Furthermore, on the same or another line \( {l}^{\prime } \) , let \( \overline{{A}^{\prime }{B}^{\prime }} \) and \( \overline{{B}^{\prime }{C}^{\prime }} \) be two segments that, except for \( {B}^{\prime } \) , have no points in common. In that case, if \( \overline{AB} \cong  \overline{{A}^{\prime }{B}^{\prime }} \) and \( \overline{BC} \cong  \overline{{B}^{\prime }{C}^{\prime }} \) , then \( \overline{AC} \cong  \overline{{A}^{\prime }{C}^{\prime }} \) .

(d) Let \( \angle {rs} \) be an angle and \( {l}^{\prime } \) a line, and let a definite side of \( {l}^{\prime } \) be given. Let \( {\overrightarrow{r}}^{\prime } \) be a ray on \( {l}^{\prime } \) starting at a point \( {O}^{\prime } \) . Then there exists one and only one ray \( {\overrightarrow{s}}^{\prime } \) such that \( \angle {r}^{\prime }{s}^{\prime } \cong  \angle {rs} \) and at the same time all the interior points of \( {\overrightarrow{s}}^{\prime } \) lie on the given side of \( {l}^{\prime } \) .

(e) If for two triangles \( \bigtriangleup {ABC} \) and \( \bigtriangleup {A}^{\prime }{B}^{\prime }{C}^{\prime } \) the congruences \( \overline{AB} \cong  \overline{{A}^{\prime }{B}^{\prime }} \) , \( \overline{AC} \cong  \overline{{A}^{\prime }{C}^{\prime }} \) , and \( \angle {BAC} \cong  \angle {B}^{\prime }{A}^{\prime }{C}^{\prime } \) hold, then \( \angle {ABC} \cong  \angle {A}^{\prime }{B}^{\prime }{C}^{\prime } \) and \( \angle {ACB} \cong  \angle {A}^{\prime }{C}^{\prime }{B}^{\prime } \) as well.

- Euclidean Parallel Postulate: Given a line \( l \) and a point \( A \) that does not lie on \( l \) , there exists a unique line that contains \( A \) and is parallel to \( l \) .

Given an axiomatic system such as this one, an interpretation of the system is simply an assignment of a definition for each of the primitive terms. An interpretation is called a model of the axiomatic system provided that each of the axioms becomes a theorem when the primitive terms are given the assigned meanings.

We are all familiar with the Cartesian plane as an interpretation of Euclidean plane geometry. Formally, in this interpretation, we make the following definitions:

- A point is an element of \( {\mathbb{R}}^{2} \) .

- A line is the image of a maximal geodesic with respect to the Euclidean metric.

- Given a point \( A \) and a line \( l \) , we say that \( A \) lies on \( l \) if \( A \in  l \) .

- Given three distinct points \( A, B, C \) , we say that \( B \) is between \( A \) and \( C \) if \( B \) is on the geodesic segment joining \( A \) to \( C \) .

- Given two sets of points \( S \) and \( {S}^{\prime } \) , we say that \( S \) is congruent to \( {S}^{\prime } \) if there is a Euclidean isometry \( \varphi  : {\mathbb{R}}^{2} \rightarrow  {\mathbb{R}}^{2} \) such that \( \varphi \left( S\right)  = {S}^{\prime } \) .

With this interpretation, it will come as no surprise that Hilbert's postulates are all theorems; proving them is just a standard exercise in plane analytic geometry.

Exercise 5.29. Verify that all of Hilbert's axioms are theorems when the primitive terms are given the interpretations listed above.

More interesting is the application of Riemannian geometry to non-Euclidean geometry. Hilbert's axioms can be easily modified to yield axioms for plane hyperbolic geometry, simply by replacing the Euclidean parallel postulate by the following:

- Hyperbolic Parallel Postulate: Given a line \( l \) and a point \( A \) that does not lie on \( l \) , there exist at least two distinct lines that contain \( A \) and are parallel to \( l \) .

We obtain an interpretation of this new axiomatic system by giving definitions to the primitive terms just as we did above, but now with \( {\mathbb{R}}^{2} \) replaced by \( {\mathbb{H}}^{2} \) and \( \bar{g} \) replaced by any hyperbolic metric \( {\breve{g}}_{R} \) . (The axioms we have listed here do not distinguish among hyperbolic metrics of different radii.) In Problem 5-19, you will be asked to prove that some of Hilbert's axioms are theorems under this interpretation.

In addition to hyperbolic geometry, it is possible to construct another version of non-Euclidean geometry, in which the Euclidean parallel postulate is replaced by the following assertion:

## Elliptic Parallel Postulate: No two lines are parallel.

Unfortunately, we cannot simply replace the Euclidean parallel postulate with this one and leave the other axioms alone, because it already follows from Hilbert's other axioms that for every line \( l \) and every point \( A \notin  l \) there exists at least one line through \( A \) that is parallel to \( l \) (for a proof, see [Gre93], for example). Nonetheless, we already know of an interesting geometry that satisfies the elliptic parallel postulate-the sphere \( {\mathbb{S}}^{2} \) with the round metric \( \overset{ \circ  }{g} \) . To construct a consistent axiomatic system including the elliptic parallel postulate, some of the other axioms need to be modified.

If we take the sphere as a guide, with images of maximal geodesics as lines, then we can see already that the first incidence postulate needs to be abandoned, because if \( A, B \in  {\mathbb{S}}^{2} \) are antipodal points (meaning that \( B =  - A \) ), then there are infinitely many lines containing \( A \) and \( B \) . Any axiomatic system for which \( \left( {{\mathbb{S}}^{2},\overset{ \circ  }{g}}\right) \) is a model is called double elliptic geometry, because every pair of distinct lines intersects in exactly two points.

It is also possible to construct an elliptic geometry in which the incidence postulates hold, as in the following example.

Example 5.30. The real projective plane \( {\mathbb{{RP}}}^{2} \) has a frame-homogeneous Riemannian metric \( g \) that is locally isometric to a round metric on \( {\mathbb{S}}^{n} \) (see Example 2.34 and Problem 3-2). As Problem 5-20 shows, single elliptic geometry satisfies Hilbert's incidence postulates as well as the elliptic parallel postulate. This interpretation is called single elliptic geometry.

## Problems

5-1. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, and let \( \nabla \) be its Levi-Civita connection. Suppose \( \widetilde{\nabla } \) is another connection on \( {TM} \) , and \( D \) is the difference tensor between \( \nabla \) and \( \widetilde{\nabla } \) (Prop. 4.13). Let \( {D}^{\flat } \) denote the covariant 3-tensor field defined by \( {D}^{\flat }\left( {X, Y, Z}\right)  = \langle D\left( {X, Y}\right) , Z\rangle \) . Show that \( \widetilde{\nabla } \) is compatible with \( g \) if and only if \( {D}^{b} \) is antisymmetric in its last two arguments: \( {D}^{b}\left( {X, Y, Z}\right)  =  - {D}^{b}\left( {X, Z, Y}\right) \) for all \( X, Y, Z \in  \mathcal{K}\left( M\right) \) . Conclude that on every Riemannian or pseudo-Riemannian manifold of dimension at least 2, the space of metric connections is an infinite-dimensional affine space. (Used on p. 121.)

5-2. Let \( \nabla \) be a connection on the tangent bundle of a Riemannian manifold \( \left( {M, g}\right) \) . Show that \( \nabla \) is compatible with \( g \) if and only if the connection 1-forms \( {\omega }_{i}{}^{j} \) (Problem 4-14) with respect to each local frame \( \left( {E}_{i}\right) \) satisfy

\[
{g}_{jk}{\omega }_{i}^{k} + {g}_{ik}{\omega }_{j}^{k} = d{g}_{ij}.
\]

Show that this implies that with respect to every local orthonormal frame, the matrix \( \left( {{\omega }_{i}{}^{j}}\right) \) is skew-symmetric.

5-3. Define a connection on \( {\mathbb{R}}^{3} \) by setting (in standard coordinates)

\[
{\Gamma }_{12}^{3} = {\Gamma }_{23}^{1} = {\Gamma }_{31}^{2} = 1
\]

\[
{\Gamma }_{21}^{3} = {\Gamma }_{32}^{1} = {\Gamma }_{13}^{2} =  - 1
\]

with all other connection coefficients equal to zero. Show that this connection is compatible with the Euclidean metric and has the same geodesics as the Euclidean connection, but is not symmetric. (See Problem 4-9.)

5-4. Let \( C \) be an embedded smooth curve in the half-plane \( H = \{ \left( {r, z}\right)  : r > 0\} \) , and let \( {S}_{C} \subseteq  {\mathbb{R}}^{3} \) be the surface of revolution determined by \( C \) as in Example 2.20. Let \( \gamma \left( t\right)  = \left( {a\left( t\right) , b\left( t\right) }\right) \) be a unit-speed local parametrization of \( C \) , and let \( X \) be the parametrization of \( {S}_{C} \) given by (2.11).

(a) Compute the Christoffel symbols of the induced metric on \( {S}_{C} \) in \( \left( {t,\theta }\right) \) coordinates.

(b) Show that each meridian is the image of a geodesic on \( {S}_{C} \) .

(c) Determine necessary and sufficient conditions for a latitude circle to be the image of a geodesic.

5-5. Recall that a vector field \( Y \) defined on (an open subset of) a Riemannian manifold is said to be parallel if \( \nabla Y \equiv  0 \) .

(a) Let \( p \in  {\mathbb{R}}^{n} \) and \( v \in  {T}_{p}{\mathbb{R}}^{n} \) . Show that there is a unique parallel vector field \( Y \) on \( {\mathbb{R}}^{n} \) such that \( {Y}_{p} = v \) .

(b) Let \( X\left( {\varphi ,\theta }\right)  = \left( {\sin \varphi \cos \theta ,\sin \varphi \sin \theta ,\cos \varphi }\right) \) be the spherical coordinate parametrization of an open subset \( U \) of the unit sphere \( {\mathbb{S}}^{2} \) (see Example 2.20 and Problem 5-4), and let \( {X}_{\theta } = {X}_{ * }\left( {\partial }_{\theta }\right) ,{X}_{\varphi } = {X}_{ * }\left( {\partial }_{\varphi }\right) \) denote the coordinate vector fields associated with this parametrization. Compute \( {\nabla }_{{X}_{\theta }}\left( {X}_{\varphi }\right) \) and \( {\nabla }_{{X}_{\varphi }}\left( {X}_{\varphi }\right) \) , and conclude that \( {X}_{\varphi } \) is parallel along the equator and along each meridian \( \theta  = {\theta }_{0} \) .

(c) Let \( p = \left( {1,0,0}\right)  \in  {\mathbb{S}}^{2} \) . Show that there is no parallel vector field \( W \) on any neighborhood of \( p \) in \( {\mathbb{S}}^{2} \) such that \( {W}_{p} = {\left. {X}_{\varphi }\right| }_{p} \) .

(d) Use (a) and (c) to show that no neighborhood of \( p \) in \( \left( {{\mathbb{S}}^{2},\overset{ \circ  }{g}}\right) \) is isometric to an open subset of \( \left( {{\mathbb{R}}^{2},\bar{g}}\right) \) .

(Used on p. 194.)

5-6. Suppose \( \pi  : \left( {\widetilde{M},\widetilde{g}}\right)  \rightarrow  \left( {M, g}\right) \) is a Riemannian submersion. If \( Z \) is any vector field on \( M \) , we let \( \widetilde{Z} \) denote its horizontal lift to \( \widetilde{M} \) (see Prop. 2.25).

(a) Show that for every pair of vector fields \( X, Y \in  \mathfrak{X}\left( M\right) \) , we have

\[
\langle \widetilde{X},\widetilde{Y}\rangle  = \langle X, Y\rangle  \circ  \pi
\]

\[
{\left\lbrack  \widetilde{X},\widetilde{Y}\right\rbrack  }^{H} = \left\lbrack  {\bar{X},\bar{Y}}\right\rbrack
\]

\[
\left\lbrack  {\widetilde{X}, W}\right\rbrack  \text{ is vertical if }W \in  \mathfrak{X}\left( \widetilde{M}\right) \text{ is vertical. }
\]

(b) Let \( \widetilde{\nabla } \) and \( \nabla \) denote the Levi-Civita connections of \( \widetilde{g} \) and \( g \) , respectively. Show that for every pair of vector fields \( X, Y \in  \mathfrak{X}\left( M\right) \) , we have

\[
{\widetilde{\nabla }}_{\widetilde{X}}\widetilde{Y} = \widetilde{{\nabla }_{X}Y} + \frac{1}{2}{\left\lbrack  \widetilde{X},\widetilde{Y}\right\rbrack  }^{V}. \tag{5.27}
\]

[Hint: Let \( \widetilde{Z} \) be a horizontal lift and \( W \) a vertical vector field on \( \widetilde{M} \) , and compute \( \left\langle  {{\widetilde{\nabla }}_{\widetilde{X}}\widetilde{Y},\widetilde{Z}}\right\rangle \) and \( \left\langle  {{\widetilde{\nabla }}_{\widetilde{X}}\widetilde{Y}, W}\right\rangle \) using (5.9).]

(Used on p. 224.)

5-7. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are Riemannian manifolds.

(a) Prove that if \( {M}_{1} \times  {M}_{2} \) is endowed with the product metric, then a curve \( \gamma  : I \rightarrow  {M}_{1} \times  {M}_{2} \) of the form \( \gamma \left( t\right)  = \left( {{\gamma }_{1}\left( t\right) ,{\gamma }_{2}\left( t\right) }\right) \) is a geodesic if and only if \( {\gamma }_{i} \) is a geodesic in \( \left( {{M}_{i},{g}_{i}}\right) \) for \( i = 1,2 \) .

(b) Now suppose \( f : {M}_{1} \rightarrow  {\mathbb{R}}^{ + } \) is a strictly positive smooth function, and \( {M}_{1}{ \times  }_{f}{M}_{2} \) is the resulting warped product (see Example 2.24). Let \( {\gamma }_{1} : I \rightarrow  {M}_{1} \) be a smooth curve and \( {q}_{0} \) a point in \( {M}_{2} \) , and define \( \gamma  : I \rightarrow  {M}_{1}{ \times  }_{f}{M}_{2} \) by \( \gamma \left( t\right)  = \left( {{\gamma }_{1}\left( t\right) ,{q}_{0}}\right) \) . Prove that \( \gamma \) is a geodesic with respect to the warped product metric if and only if \( {\gamma }_{1} \) is a geodesic with respect to \( {g}_{1} \) .

(Used on p. 316.)

5-8. Let \( G \) be a Lie group and \( \mathfrak{g} \) its Lie algebra. Suppose \( g \) is a bi-invariant Riemannian metric on \( G \) , and \( \langle  \cdot  , \cdot  \rangle \) is the corresponding inner product on \( \mathfrak{g} \) (see Prop. 3.12). Let ad: \( \mathfrak{g} \rightarrow  \mathfrak{{gl}}\left( \mathfrak{g}\right) \) denote the adjoint representation of \( \mathfrak{g} \) (see Appendix C).

(a) Show that \( \operatorname{ad}\left( X\right) \) is a skew-adjoint endomorphism of \( \mathfrak{g} \) for every \( X \in  \mathfrak{g} \) :

\[
\langle \operatorname{ad}\left( X\right) Y, Z\rangle  =  - \langle Y,\operatorname{ad}\left( X\right) Z\rangle .
\]

[Hint: Take the derivative of \( \left\langle  {\operatorname{Ad}\left( {{\exp }^{G}{tX}}\right) Y,\operatorname{Ad}\left( {{\exp }^{G}{tX}}\right) Z}\right\rangle \) with respect to \( t \) at \( t = 0 \) , where \( {\exp }^{G} \) is the Lie group exponential map of \( G \) , and use the fact that \( {\mathrm{{Ad}}}_{ * } = \) ad.]

(b) Show that \( {\nabla }_{X}Y = \frac{1}{2}\left\lbrack  {X, Y}\right\rbrack \) whenever \( X \) and \( Y \) are left-invariant vector fields on \( G \) .

(c) Show that the geodesics of \( g \) starting at the identity are exactly the one-parameter subgroups. Conclude that under the canonical isomorphism of \( \mathfrak{g} \cong  {T}_{e}G \) described in Proposition C.3, the restricted Riemannian exponential map at the identity coincides with the Lie group exponential map \( {\exp }^{G} : \mathfrak{g} \rightarrow  G \) . (See Prop. C.7.)

(d) Let \( {\mathbb{R}}^{ + } \) be the set of positive real numbers, regarded as a Lie group under multiplication. Show that \( g = {t}^{-2}d{t}^{2} \) is a bi-invariant metric on \( {\mathbb{R}}^{ + } \) , and the restricted Riemannian exponential map at 1 is given by \( c\partial /\partial t \mapsto  {e}^{c}. \)

(Used on pp. 128, 224.)

5-9. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( \left( {U,\varphi }\right) \) is a smooth coordinate chart on a neighborhood of \( p \in  M \) such that \( \varphi \left( p\right)  = 0 \) and \( \varphi \left( U\right) \) is star-shaped with respect to 0 . Prove that this chart is a normal coordinate chart for \( g \) if and only if \( {g}_{ij}\left( p\right)  = {\delta }_{ij} \) and the following identity is satisfied on \( U \) :

\[
{x}^{i}{x}^{j}{\Gamma }_{ij}^{k}\left( x\right)  \equiv  0.
\]

5-10. Prove Proposition 5.22 (a local isometry is determined by its value and differential at one point).

5-11. Recall the groups \( \mathrm{E}\left( n\right) ,\mathrm{O}\left( {n + 1}\right) \) , and \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) defined in Chapter 3, which act isometrically on the model Riemannian manifolds \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) ,\left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) , and \( \left( {{\mathbb{H}}^{n}\left( R\right) ,{\breve{g}}_{R}}\right) \) , respectively.

(a) Show that

\[
\operatorname{Iso}\left( {{\mathbb{R}}^{n},\bar{g}}\right)  = \mathrm{E}\left( n\right) ,
\]

\[
\operatorname{Iso}\left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right)  = \mathrm{O}\left( {n + 1}\right) ,
\]

\[
\operatorname{Iso}\left( {{\mathbb{H}}^{n}\left( R\right) ,{\breve{g}}_{R}}\right)  = {\mathrm{O}}^{ + }\left( {n,1}\right) .
\]

(b) Show that in each case, for each point \( p \) in \( {\mathbb{R}}^{n},{\mathbb{S}}^{n}\left( R\right) \) , or \( {\mathbb{H}}^{n}\left( R\right) \) , the isotropy group at \( p \) is a subgroup isomorphic to \( \mathrm{O}\left( n\right) \) .

(c) Strengthen the result above by showing that if \( \left( {M, g}\right) \) is one of the Riemannian manifolds \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) ,\left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) , or \( \left( {{\mathbb{H}}^{n}\left( R\right) ,{\breve{g}}_{R}}\right) , U \) is a connected open subset of \( M \) , and \( \varphi  : U \rightarrow  M \) is a local isometry, then \( \varphi \) is the restriction to \( U \) of an element of \( \operatorname{Iso}\left( {M, g}\right) \) .

(Used on pp. 57, 58, 67, 348, 349.)

5-12. Suppose \( M \) is a connected \( n \) -dimensional Riemannian manifold, and \( G \) is a Lie group acting isometrically and effectively on \( M \) . Show that \( \dim G \leq \; n\left( {n + 1}\right) /2 \) . (Used on p. 261.)

5-13. Let \( \left( {M, g}\right) \) be a Riemannian manifold.

(a) Show that the following formula holds for every smooth 1-form \( \eta  \in \; {\Omega }^{1}\left( M\right) \) :

\[
{d\eta }\left( {X, Y}\right)  = \left( {{\nabla }_{X}\eta }\right) \left( Y\right)  - \left( {{\nabla }_{Y}\eta }\right) \left( X\right) .
\]

(b) Generalize this to an arbitrary \( k \) -form \( \eta  \in  {\Omega }^{k}\left( M\right) \) as follows:

\[
{d\eta } = {\left( -1\right) }^{k}\left( {k + 1}\right) \operatorname{Alt}\left( {\nabla \eta }\right) ,
\]

where Alt denotes the alternation operator defined in (B.9). [Hint: For each \( p \in  M \) , do the computation in normal coordinates centered at \( p \) , and note that both sides of the equation are well defined, independently of the choice of coordinates.]

(Used on p. 209.)

5-14. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, and let div and \( \Delta \) be the divergence and Laplace operators defined on pages 32-33.

(a) Show that for every vector field \( X \in  \mathfrak{X}\left( M\right) \) , div \( X \) can be written in terms of the total covariant derivative as \( \operatorname{div}X = \operatorname{tr}\left( {\nabla X}\right) \) , and that if \( X = {X}^{i}{E}_{i} \) in terms of some local frame, then \( \operatorname{div}X = {X}^{i}{}_{;i} \) . [Hint: Show that it suffices to prove the formulas at the origin in normal coordinates.]

(b) Show that the Laplace operator acting on a smooth function \( u \) can be expressed as

\[
{\Delta u} = {\operatorname{tr}}_{g}\left( {{\nabla }^{2}u}\right) \tag{5.28}
\]

and in terms of any local frame,

\[
{\Delta u} = {g}^{ij}{u}_{;{ij}} = {u}_{;i}{}^{i}. \tag{5.29}
\]

(Used on pp. 218, 256, 333.)

5-15. Suppose \( \left( {M, g}\right) \) is a compact Riemannian \( n \) -manifold (without boundary) and \( u \in  {C}^{\infty }\left( M\right) \) is an eigenfunction of \( M \) , meaning that \( - {\Delta u} = {\lambda u} \) for some constant \( \lambda \) (see Prob. 2-24). Prove that

\[
\lambda {\int }_{M}{\left| \operatorname{grad}u\right| }^{2}d{V}_{g} \leq  n{\int }_{M}{\left| {\nabla }^{2}u\right| }^{2}d{V}_{g}.
\]

[Hint: Consider the 2-tensor field \( {\nabla }^{2}u - \frac{1}{n}\left( {\Delta u}\right) g \) , and use one of Green’s identities (Prob. 2-23).] (Used on p. 223.)

5-16. By analogy with the formula div \( X = \operatorname{tr}\left( {\nabla X}\right) \) developed in Problem 5-14, we can define a divergence operator on tensor fields of any rank on a Riemannian manifold. If \( F \) is any smooth \( k \) -tensor field (covariant, contravariant, or mixed), we define the divergence of \( \mathbf{F} \) by

\[
\operatorname{div}F = {\operatorname{tr}}_{g}\left( {\nabla F}\right) ,
\]

where the trace is taken on the last two indices of the \( \left( {k + 1}\right) \) -tensor field \( \nabla F \) . (If \( F \) is purely contravariant, then \( {\operatorname{tr}}_{g} \) can be replaced with \( \operatorname{tr} \) , because the next-to-last index of \( \nabla F \) is already an upper index.) Extend the integration by parts formula of Problem 2-22 as follows: if \( F \) is a smooth covariant \( k \) -tensor field and \( G \) is a smooth covariant \( \left( {k + 1}\right) \) -tensor field on a compact smooth Riemannian manifold \( \left( {M, g}\right) \) with boundary, then

\[
{\int }_{M}\langle \nabla F, G\rangle d{V}_{g} = {\int }_{\partial M}\left\langle  {F \otimes  {N}^{\flat }, G}\right\rangle  d{V}_{\widehat{g}} - {\int }_{M}\langle F,\operatorname{div}G\rangle d{V}_{g},
\]

where \( \widehat{g} \) is the induced metric on \( \partial M \) . This is often written more suggestively as

\[
{\int }_{M}{F}_{{i}_{1}\ldots {i}_{k};j}{G}^{{i}_{1}\ldots {i}_{k}j}d{V}_{g}
\]

\[
= {\int }_{\partial M}{F}_{{i}_{1}\ldots {i}_{k}}{G}^{{i}_{1}\ldots {i}_{k}j}{N}_{j}d{V}_{\widehat{g}} - {\int }_{M}{F}_{{i}_{1}\ldots {i}_{k}}{G}^{{i}_{1}\ldots {i}_{k}j}{}_{;j}d{V}_{g}.
\]

5-17. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( P \subseteq  M \) is an embedded sub-manifold. Show that \( P \) has a tubular neighborhood that is diffeomorphic to the total space of the normal bundle \( {NP} \) , by a diffeomorphism that sends the zero section of \( {NP} \) to \( P \) . [Hint: First show that the function \( \delta \) in (5.21) can be chosen to be smooth.]

5-18. Prove Proposition 5.26 (properties of Fermi coordinates).

5-19. Use \( {\mathbb{H}}^{2} \) with the metric \( \breve{g} \) to construct an interpretation of Hilbert’s axioms with the hyperbolic parallel postulate substituted for the Euclidean one, and prove that the incidence postulates, congruence postulate (e), and the hyperbolic parallel postulate are theorems in this geometry. (Used on p. 144.)

5-20. Show that single elliptic geometry (Example 5.30) satisfies Hilbert's incidence postulates and the elliptic parallel postulate if points are defined as elements of \( {\mathbb{{RP}}}^{2} \) and lines are defined as images of maximal geodesics.

5-21. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold and \( p \in  M \) . Show that for every orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{p}M \) , there is a smooth orthonormal frame \( \left( {E}_{i}\right) \) on a neighborhood of \( p \) such that \( {\left. {E}_{i}\right| }_{p} = {b}_{i} \) and \( {\left( \nabla {E}_{i}\right) }_{p} = 0 \) for each \( i \) .

5-22. A smooth vector field \( X \) on a Riemannian manifold is called a Killing vector field if the Lie derivative of the metric with respect to \( X \) vanishes. By Proposition B.10, this is equivalent to the requirement that the metric be invariant under the flow of \( X \) . Prove that \( X \) is a Killing vector field if and only if the covariant 2-tensor field \( {\left( \nabla X\right) }^{\flat } \) is antisymmetric. [Hint: Use Prop. B.9.] (Used on pp. 190, 315.)

5-23. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold and \( p \in  M \) . An admissible loop based at \( \mathbf{p} \) is an admissible curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) such that \( \gamma \left( a\right)  = \; \gamma \left( b\right)  = p \) . For each such loop \( \gamma \) , let \( {P}^{\gamma } \) denote the parallel transport operator \( {P}_{ab}^{\gamma } : {T}_{p}M \rightarrow  {T}_{p}M \) along \( \gamma \) , and let \( \operatorname{Hol}\left( p\right)  \subseteq  \operatorname{GL}\left( {{T}_{p}M}\right) \) denote the set of all automorphisms of \( {T}_{p}M \) obtained in this way:

\[
\operatorname{Hol}\left( p\right)  = \left\{  {{P}^{\gamma } : \gamma \text{ is an admissible loop based at }p}\right\}  .
\]

(a) Show that \( \operatorname{Hol}\left( p\right) \) is a subgroup of \( \mathrm{O}\left( {{T}_{p}M}\right) \) (the set of all linear isometries of \( {T}_{p}M \) ), called the holonomy group at \( \mathbf{p} \) .

(b) Let \( {\mathrm{{Hol}}}^{0}\left( p\right)  \subseteq  \mathrm{{Hol}}\left( p\right) \) denote the subset obtained by restricting to loops \( \gamma \) that are path-homotopic to the constant loop. Show that \( {\mathrm{{Hol}}}^{0}\left( p\right) \) is a normal subgroup of \( \operatorname{Hol}\left( p\right) \) , called the restricted holonomy group at \( p \) .

(c) Given \( p, q \in  M \) , show that there is an isomorphism of \( \mathrm{{GL}}\left( {{T}_{p}M}\right) \) with \( \mathrm{{GL}}\left( {{T}_{q}M}\right) \) that takes \( \operatorname{Hol}\left( p\right) \) to \( \operatorname{Hol}\left( q\right) \) .

(d) Show that \( M \) is orientable if and only if \( \operatorname{Hol}\left( p\right)  \subseteq  \operatorname{SO}\left( {{T}_{p}M}\right) \) (the set of linear isometries with determinant +1 ) for some \( p \in  M \) .

(e) Show that \( g \) is flat if and only if \( {\operatorname{Hol}}^{0}\left( p\right) \) is the trivial group for some \( p \in  M \) .
