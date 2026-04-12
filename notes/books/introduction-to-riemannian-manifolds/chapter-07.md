## Chapter 7 Curvature

In this chapter, we begin our study of the local invariants of Riemannian metrics. Starting with the question whether all Riemannian metrics are locally isometric, we are led to a definition of the Riemannian curvature tensor as a measure of the failure of second covariant derivatives to commute. Then we prove the main result of this chapter: a Riemannian manifold has zero curvature if and only if it is flat, or locally isometric to Euclidean space. Next, we derive the basic symmetries of the curvature tensor, and introduce the Ricci, scalar, and Weyl curvature tensors. At the end of the chapter, we explore how the curvature can be used to detect conformal flatness. As you will see, the results of this chapter apply essentially unchanged to pseudo-Riemannian metrics.

## Local Invariants

For any geometric structure defined on smooth manifolds, it is of great interest to address the local equivalence question: Are all examples of the structure locally equivalent to each other (under an appropriate notion of local equivalence)?

There are some interesting and useful structures in differential geometry that have the property that all such structures on manifolds of the same dimension are locally equivalent to each other. For example:

- NONVANISHING VECTOR FIELDS: Every nonvanishing vector field can be written as \( X = \partial /\partial {x}^{1} \) in suitable local coordinates, so they are all locally equivalent.

- RIEMANNIAN METRICS ON A 1-MANIFOLD: Problem 2-1 shows that every Riemannian 1-manifold is locally isometric to \( \mathbb{R} \) with its Euclidean metric.

- SYMPLECTIC FORMS: A symplectic form on a smooth manifold \( M \) is a closed 2-form \( \omega \) that is nondegenerate at each \( p \in  M \) , meaning that \( {\omega }_{p}\left( {v, w}\right)  = 0 \) for all \( w \in  {T}_{p}M \) only if \( v = 0 \) . By the theorem of Darboux [LeeSM, Thm. 22.13], every symplectic form can be written in suitable coordinates as \( \mathop{\sum }\limits_{i}d{x}^{i} \land  d{y}^{i} \) . Thus all symplectic forms on \( {2n} \) -manifolds are locally equivalent.

![bo_d7dtff491nqc73eq8m7g_204_472_188_588_591_0.jpg](images/bo_d7dtff491nqc73eq8m7g_204_472_188_588_591_0.jpg)

Fig. 7.1: Result of parallel transport along the \( {x}^{1} \) -axis and the \( {x}^{2} \) -coordinate lines

On the other hand, Problem 5-5 showed that the round 2-sphere and the Euclidean plane are not locally isometric.

The most important technique for proving that two geometric structures are not locally equivalent is to find local invariants, which are quantities that must be preserved by local equivalences. In order to address the general problem of local equivalence of Riemannian or pseudo-Riemannian metrics, we will define a local invariant for all such metrics called curvature. Initially, its definition will have nothing to do with the curvature of curves described in Chapter 1, but later we will see that the two concepts are intimately related.

To motivate the definition of curvature, let us look back at the argument outlined in Problem 5-5 for showing that the sphere and the plane are not locally isometric. The key idea is that every tangent vector in the plane can be extended to a parallel vector field, so every Riemannian manifold that is locally isometric to \( {\mathbb{R}}^{2} \) must have the same property locally.

Given a Riemannian 2-manifold \( M \) , here is one way to attempt to construct a parallel extension of a vector \( z \in  {T}_{p}M \) : working in any smooth local coordinates \( \left( {{x}^{1},{x}^{2}}\right) \) centered at \( p \) , first parallel transport \( z \) along the \( {x}^{1} \) -axis, and then parallel transport the resulting vectors along the coordinate lines parallel to the \( {x}^{2} \) -axis (Fig. 7.1). The result is a vector field \( Z \) that, by construction, is parallel along every \( {x}^{2} \) - coordinate line and along the \( {x}^{1} \) -axis. The question is whether this vector field is parallel along \( {x}^{1} \) -coordinate lines other than the \( {x}^{1} \) -axis, or in other words, whether \( {\nabla }_{{\partial }_{1}}Z \equiv  0 \) . Observe that \( {\nabla }_{{\partial }_{1}}Z \) vanishes when \( {x}^{2} = 0 \) . If we could show that

\[
{\nabla }_{{\partial }_{2}}{\nabla }_{{\partial }_{1}}Z = 0, \tag{7.1}
\]

then it would follow that \( {\nabla }_{{\partial }_{1}}Z \equiv  0 \) , because the zero vector field is the unique parallel transport of zero along the \( {x}^{2} \) -curves. If we knew that

\[
{\nabla }_{{\partial }_{2}}{\nabla }_{{\partial }_{1}}Z = {\nabla }_{{\partial }_{1}}{\nabla }_{{\partial }_{2}}Z \tag{7.2}
\]

then (7.1) would follow immediately, because \( {\nabla }_{{\partial }_{2}}Z = 0 \) everywhere by construction. Indeed, on \( {\mathbb{R}}^{2} \) with the Euclidean metric, direct computation shows that

\[
{\overline{\nabla }}_{{\partial }_{2}}{\overline{\nabla }}_{{\partial }_{1}}Z = {\overline{\nabla }}_{{\partial }_{2}}\left( {\left( {{\partial }_{1}{Z}^{k}}\right) {\partial }_{k}}\right)
\]

\[
= \left( {{\partial }_{2}{\partial }_{1}{Z}^{k}}\right) {\partial }_{k},
\]

and \( {\overline{\nabla }}_{{\partial }_{1}}{\overline{\nabla }}_{{\partial }_{2}}Z \) is equal to the same thing, because ordinary second partial derivatives commute. However, (7.2) might not hold for an arbitrary Riemannian metric; indeed, it is precisely the noncommutativity of such second covariant derivatives that forces this construction to fail on the sphere. Lurking behind this noncommuta-tivity is the fact that the sphere is "curved."

To express this noncommutativity in a coordinate-independent way, let us look more closely at the quantity \( {\overline{\nabla }}_{X}{\overline{\nabla }}_{Y}Z - {\overline{\nabla }}_{Y}{\overline{\nabla }}_{X}Z \) when \( X, Y \) , and \( Z \) are smooth vector fields. On \( {\mathbb{R}}^{2} \) with the Euclidean connection, we just showed that this always vanishes if \( X = {\partial }_{1} \) and \( Y = {\partial }_{2} \) ; however, for arbitrary vector fields this may no longer be true. In fact, in \( {\mathbb{R}}^{n} \) with the Euclidean connection we have

\[
{\overline{\nabla }}_{X}{\overline{\nabla }}_{Y}Z = {\overline{\nabla }}_{X}\left( {Y\left( {Z}^{k}\right) {\partial }_{k}}\right)  = {XY}\left( {Z}^{k}\right) {\partial }_{k},
\]

and similarly \( {\overline{\nabla }}_{Y}{\overline{\nabla }}_{X}Z = {YX}\left( {Z}^{k}\right) {\partial }_{k} \) . The difference between these two expressions is \( \left( {{XY}\left( {Z}^{k}\right)  - {YX}\left( {Z}^{k}\right) }\right) {\partial }_{k} = {\overline{\nabla }}_{\left\lbrack  X, Y\right\rbrack  }Z \) . Therefore, the following relation holds for all vector fields \( X, Y, Z \) defined on an open subset of \( {\mathbb{R}}^{n} \) :

\[
{\overline{\nabla }}_{X}{\overline{\nabla }}_{Y}Z - {\overline{\nabla }}_{Y}{\overline{\nabla }}_{X}Z = {\overline{\nabla }}_{\left\lbrack  X, Y\right\rbrack  }Z.
\]

Recall that a Riemannian manifold is said to be flat if it is locally isometric to a Euclidean space, that is, if every point has a neighborhood that is isometric to an open set in \( {\mathbb{R}}^{n} \) with its Euclidean metric. Similarly, a pseudo-Riemannian manifold is flat if it is locally isometric to a pseudo-Euclidean space. The computation above leads to the following simple necessary condition for a Riemannian or pseudo-Riemannian manifold to be flat. We say that a connection \( \nabla \) on a smooth manifold \( M \) satisfies the flatness criterion if whenever \( X, Y, Z \) are smooth vector fields defined on an open subset of \( M \) , the following identity holds:

\[
{\nabla }_{X}{\nabla }_{Y}Z - {\nabla }_{Y}{\nabla }_{X}Z = {\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z. \tag{7.3}
\]

Example 7.1. The metric on the \( n \) -torus induced by the embedding in \( {\mathbb{R}}^{2n} \) given in Example 2.21 is flat, because each point has a coordinate neighborhood in which the metric is Euclidean. ‖

Proposition 7.2. If \( \left( {M, g}\right) \) is a flat Riemannian or pseudo-Riemannian manifold, then its Levi-Civita connection satisfies the flatness criterion.

Proof. We just showed that the Euclidean connection on \( {\mathbb{R}}^{n} \) satisfies (7.3). By naturality, the Levi-Civita connection on every manifold that is locally isometric to a Euclidean or pseudo-Euclidean space must also satisfy the same identity.

## The Curvature Tensor

Motivated by the computation in the preceding section, we make the following definition. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, and define a map \( R : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) by

\[
R\left( {X, Y}\right) Z = {\nabla }_{X}{\nabla }_{Y}Z - {\nabla }_{Y}{\nabla }_{X}Z - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z.
\]

Proposition 7.3. The map \( R \) defined above is multilinear over \( {C}^{\infty }\left( M\right) \) , and thus defines a \( \left( {1,3}\right) \) -tensor field on \( M \) .

Proof. The map \( R \) is obviously multilinear over \( \mathbb{R} \) . For \( f \in  {C}^{\infty }\left( M\right) \) ,

\[
R\left( {X,{fY}}\right) Z = {\nabla }_{X}{\nabla }_{fY}Z - {\nabla }_{fY}{\nabla }_{X}Z - {\nabla }_{\left\lbrack  X, fY\right\rbrack  }Z
\]

\[
= {\nabla }_{X}\left( {f{\nabla }_{Y}Z}\right)  - f{\nabla }_{Y}{\nabla }_{X}Z - {\nabla }_{f\left\lbrack  {X, Y}\right\rbrack   + \left( {Xf}\right) Y}Z
\]

\[
= \left( {Xf}\right) {\nabla }_{Y}Z + f{\nabla }_{X}{\nabla }_{Y}Z - f{\nabla }_{Y}{\nabla }_{X}Z
\]

\[
- f{\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z - \left( {Xf}\right) {\nabla }_{Y}Z
\]

\[
= {fR}\left( {X, Y}\right) Z\text{ . }
\]

The same proof shows that \( R \) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) , because \( R\left( {X, Y}\right) Z = \; - R\left( {Y, X}\right) Z \) from the definition. The remaining case to be checked is linearity over \( {C}^{\infty }\left( M\right) \) in \( Z \) ; this is left to Problem 7-1.

By the tensor characterization lemma (Lemma B.6), the fact that \( R \) is multilinear over \( {C}^{\infty }\left( M\right) \) implies that it is a \( \left( {1,3}\right) \) -tensor field.

Thanks to this proposition, for each pair of vector fields \( X, Y \in  \mathfrak{X}\left( M\right) \) , the map \( R\left( {X, Y}\right)  : \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) given by \( Z \mapsto  R\left( {X, Y}\right) Z \) is a smooth bundle endomorphism of \( {TM} \) , called the curvature endomorphism determined by \( X \) and \( Y \) . The tensor field \( R \) itself is called the (Riemann) curvature endomorphism or the (1, 3)-curvature tensor. (Some authors call it simply the curvature tensor, but we reserve that name instead for another closely related tensor field, defined below.)

As a \( \left( {1,3}\right) \) -tensor field, the curvature endomorphism can be written in terms of any local frame with one upper and three lower indices. We adopt the convention that the last index is the contravariant (upper) one. (This is contrary to our default assumption that covector arguments come first.) Thus, for example, the curvature endomorphism can be written in terms of local coordinates \( \left( {x}^{i}\right) \) as

\[
R = {R}_{ijk}{}^{l}d{x}^{i} \otimes  d{x}^{j} \otimes  d{x}^{k} \otimes  {\partial }_{l},
\]

where the coefficients \( {R}_{ijk}{}^{l} \) are defined by

\[
R\left( {{\partial }_{i},{\partial }_{j}}\right) {\partial }_{k} = {R}_{ijk}{}^{l}{\partial }_{l}.
\]

The next proposition shows how to compute the components of \( R \) in coordinates.

Proposition 7.4. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold. In terms of any smooth local coordinates, the components of the (1,3)-curvature tensor are given by

\[
{R}_{ijk}{}^{l} = {\partial }_{i}{\Gamma }_{jk}^{l} - {\partial }_{j}{\Gamma }_{ik}^{l} + {\Gamma }_{jk}^{m}{\Gamma }_{im}^{l} - {\Gamma }_{ik}^{m}{\Gamma }_{jm}^{l}. \tag{7.4}
\]

Proof. Problem 7-2.

Importantly for our purposes, the curvature endomorphism also measures the failure of second covariant derivatives along families of curves to commute. Given a smooth one-parameter family of curves \( \Gamma  : J \times  I \rightarrow  M \) , recall from Chapter 6 that the velocity fields \( {\partial }_{t}\Gamma \left( {s, t}\right)  = {\left( {\Gamma }_{s}\right) }^{\prime }\left( t\right) \) and \( {\partial }_{s}\Gamma \left( {s, t}\right)  = {\Gamma }^{\left( t\right) \prime }\left( s\right) \) are smooth vector fields along \( \Gamma \) .

Proposition 7.5. Suppose \( \left( {M, g}\right) \) is a smooth Riemannian or pseudo-Riemannian manifold and \( \Gamma  : J \times  I \rightarrow  M \) is a smooth one-parameter family of curves in \( M \) . Then for every smooth vector field \( V \) along \( \Gamma \) ,

\[
{D}_{s}{D}_{t}V - {D}_{t}{D}_{s}V = R\left( {{\partial }_{s}\Gamma ,{\partial }_{t}\Gamma }\right) V. \tag{7.5}
\]

Proof. This is a local question, so for each \( \left( {s, t}\right)  \in  J \times  I \) , we can choose smooth coordinates \( \left( {x}^{i}\right) \) defined on a neighborhood of \( \Gamma \left( {s, t}\right) \) and write

\[
\Gamma \left( {s, t}\right)  = \left( {{\gamma }^{1}\left( {s, t}\right) ,\ldots ,{\gamma }^{n}\left( {s, t}\right) }\right) ,\;V\left( {s, t}\right)  = {\left. {V}^{j}\left( s, t\right) {\partial }_{j}\right| }_{\Gamma \left( {s, t}\right) }.
\]

Formula (4.15) yields

\[
{D}_{t}V = \frac{\partial {V}^{i}}{\partial t}{\partial }_{i} + {V}^{i}{D}_{t}{\partial }_{i}.
\]

Therefore, applying (4.15) again, we get

\[
{D}_{s}{D}_{t}V = \frac{{\partial }^{2}{V}^{i}}{\partial s\partial t}{\partial }_{i} + \frac{\partial {V}^{i}}{\partial t}{D}_{s}{\partial }_{i} + \frac{\partial {V}^{i}}{\partial s}{D}_{t}{\partial }_{i} + {V}^{i}{D}_{s}{D}_{t}{\partial }_{i}.
\]

Interchanging \( s \) and \( t \) and subtracting, we see that all the terms except the last cancel:

\[
{D}_{s}{D}_{t}V - {D}_{t}{D}_{s}V = {V}^{i}\left( {{D}_{s}{D}_{t}{\partial }_{i} - {D}_{t}{D}_{s}{\partial }_{i}}\right) . \tag{7.6}
\]

Now we need to compute the commutator in parentheses. For brevity, let us write

\[
S = {\partial }_{s}\Gamma  = \frac{\partial {\gamma }^{k}}{\partial s}{\partial }_{k};\;T = {\partial }_{t}\Gamma  = \frac{\partial {\gamma }^{j}}{\partial t}{\partial }_{j}.
\]

Because \( {\partial }_{i} \) is extendible,

\[
{D}_{t}{\partial }_{i} = {\nabla }_{T}{\partial }_{i} = \frac{\partial {\gamma }^{j}}{\partial t}{\nabla }_{{\partial }_{j}}{\partial }_{i},
\]

and therefore, because \( {\nabla }_{{\partial }_{j}}{\partial }_{i} \) is also extendible,

\[
{D}_{s}{D}_{t}{\partial }_{i} = {D}_{s}\left( {\frac{\partial {\gamma }^{j}}{\partial t}{\nabla }_{{\partial }_{j}}{\partial }_{i}}\right)
\]

\[
= \frac{{\partial }^{2}{\gamma }^{j}}{\partial s\partial t}{\nabla }_{{\partial }_{j}}{\partial }_{i} + \frac{\partial {\gamma }^{j}}{\partial t}{\nabla }_{S}\left( {{\nabla }_{{\partial }_{j}}{\partial }_{i}}\right)
\]

\[
= \frac{{\partial }^{2}{\gamma }^{j}}{\partial s\partial t}{\nabla }_{{\partial }_{j}}{\partial }_{i} + \frac{\partial {\gamma }^{j}}{\partial t}\frac{\partial {\gamma }^{k}}{\partial s}{\nabla }_{{\partial }_{k}}{\nabla }_{{\partial }_{j}}{\partial }_{i}.
\]

Interchanging \( s \leftrightarrow  t \) and \( j \leftrightarrow  k \) and subtracting, we find that the first terms cancel, and we get

\[
{D}_{s}{D}_{t}{\partial }_{i} - {D}_{t}{D}_{s}{\partial }_{i} = \frac{\partial {\gamma }^{j}}{\partial t}\frac{\partial {\gamma }^{k}}{\partial s}\left( {{\nabla }_{{\partial }_{k}}{\nabla }_{{\partial }_{j}}{\partial }_{i} - {\nabla }_{{\partial }_{j}}{\nabla }_{{\partial }_{k}}{\partial }_{i}}\right)
\]

\[
= \frac{\partial {\gamma }^{j}}{\partial t}\frac{\partial {\gamma }^{k}}{\partial s}R\left( {{\partial }_{k},{\partial }_{j}}\right) {\partial }_{i} = R\left( {S, T}\right) {\partial }_{i}.
\]

Finally, inserting this into (7.6) yields the result.

For many purposes, the information contained in the curvature endomorphism is much more conveniently encoded in the form of a covariant 4-tensor. We define the (Riemann) curvature tensor to be the \( \left( {0,4}\right) \) -tensor field \( {Rm} = {R}^{b} \) (also denoted by Riem by some authors) obtained from the \( \left( {1,3}\right) \) -curvature tensor \( R \) by lowering its last index. Its action on vector fields is given by

\[
\operatorname{Rm}\left( {X, Y, Z, W}\right)  = \langle R\left( {X, Y}\right) Z, W{\rangle }_{g}. \tag{7.7}
\]

In terms of any smooth local coordinates it is written

\[
{Rm} = {R}_{ijkl}d{x}^{i} \otimes  d{x}^{j} \otimes  d{x}^{k} \otimes  d{x}^{l},
\]

where \( {R}_{ijkl} = {g}_{lm}{R}_{ijk}{}^{m} \) . Thus (7.4) yields

\[
{R}_{ijkl} = {g}_{lm}\left( {{\partial }_{i}{\Gamma }_{jk}^{m} - {\partial }_{j}{\Gamma }_{ik}^{m} + {\Gamma }_{jk}^{p}{\Gamma }_{ip}^{m} - {\Gamma }_{ik}^{p}{\Gamma }_{jp}^{m}}\right) . \tag{7.8}
\]

It is appropriate to note here that there is much variation in the literature with respect to index positions in the definitions of the curvature endomorphism and curvature tensor. While almost all authors define the \( \left( {1,3}\right) \) -curvature tensor as we have, there are a few (notably [dC92, GHL04]) whose definition is the negative of ours. There is much less agreement on the definition of the \( \left( {0,4}\right) \) -curvature tensor: whichever definition is chosen for the curvature endomorphism, you will see the curvature tensor defined as in (7.7) but with various permutations of \( \left( {X, Y, Z, W}\right) \) on the right-hand side. After applying the symmetries of the curvature tensor that we will prove later in this chapter, however, all of the definitions agree up to sign. There are various arguments to support one choice or another; we have made a choice that makes equation (7.7) easy to remember. You just have to be careful when you begin reading any book or article to determine the author's sign convention.

The next proposition gives one reason for our interest in the curvature tensor.

Proposition 7.6. The curvature tensor is a local isometry invariant: if \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian or pseudo-Riemannian manifolds and \( \varphi  : M \rightarrow  \widetilde{M} \) is a local isometry, then \( {\varphi }^{ * }\widetilde{Rm} = {Rm} \) .

Exercise 7.7. Prove Proposition 7.6.

## Flat Manifolds

To give a qualitative geometric interpretation to the curvature tensor, we will show that it is precisely the obstruction to being locally isometric to Euclidean (or pseudo-Euclidean) space. (In Chapter 8, after we have developed more machinery, we will be able to give a far more detailed quantitative interpretation.) The crux of the proof is the following lemma.

Lemma 7.8. Suppose \( M \) is a smooth manifold, and \( \nabla \) is any connection on \( M \) satisfying the flatness criterion. Given \( p \in  M \) and any vector \( v \in  {T}_{p}M \) , there exists a parallel vector field \( V \) on a neighborhood of \( p \) such that \( {V}_{p} = v \) .

Proof. Let \( p \in  M \) and \( v \in  {T}_{p}M \) be arbitrary, and let \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) be any smooth coordinates for \( M \) centered at \( p \) . By shrinking the coordinate neighborhood if necessary, we may assume that the image of the coordinate map is an open cube \( {C}_{\varepsilon } = \left\{  {x : \left| {x}^{i}\right|  < \varepsilon , i = 1,\ldots , n}\right\} \) . We use the coordinate map to identify the coordinate domain with \( {C}_{\varepsilon } \) .

Begin by parallel transporting \( v \) along the \( {x}^{1} \) -axis; then from each point on the \( {x}^{1} \) -axis, parallel transport along the coordinate line parallel to the \( {x}^{2} \) -axis; then successively parallel transport along coordinate lines parallel to the \( {x}^{3} \) through \( {x}^{n} \) - axes (Fig. 7.2). The result is a vector field \( V \) defined in \( {C}_{\varepsilon } \) . The fact that \( V \) is smooth follows from an inductive application of the theorem concerning smooth dependence of solutions to linear ODEs on initial conditions (Thm. 4.31); the details are left as an exercise.

Since \( {\nabla }_{X}V \) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) , to show that \( V \) is parallel, it suffices to show that \( {\nabla }_{{\partial }_{i}}V = 0 \) for each \( i = 1,\ldots , n \) . By construction, \( {\nabla }_{{\partial }_{1}}V = 0 \) on the \( {x}^{1} \) -axis, \( {\nabla }_{{\partial }_{2}}V = 0 \) on the \( \left( {{x}^{1},{x}^{2}}\right) \) -plane, and in general \( {\nabla }_{{\partial }_{k}}V = 0 \) on the slice \( {M}_{k} \subseteq  {C}_{\varepsilon } \) defined by \( {x}^{k + 1} = \cdots  = {x}^{n} = 0 \) . We will prove the following fact by induction on \( k \) :

\[
{\nabla }_{{\partial }_{1}}V = \cdots  = {\nabla }_{{\partial }_{k}}V = 0\;\text{ on }{M}_{k}. \tag{7.9}
\]

For \( k = 1 \) , this is true by construction, and for \( k = n \) , it means that \( V \) is parallel on the whole cube \( {C}_{\varepsilon } \) . So assume that (7.9) holds for some \( k \) . By construction, \( {\nabla }_{{\partial }_{k + 1}}V = 0 \) on all of \( {M}_{k + 1} \) , and for \( i \leq  k \) , the inductive hypothesis shows that \( {\nabla }_{{\partial }_{i}}V = 0 \) on the hyperplane \( {M}_{k} \subseteq  {M}_{k + 1} \) .

Since \( \left\lbrack  {{\partial }_{k + 1},{\partial }_{i}}\right\rbrack   = 0 \) , the flatness criterion gives

\[
{\nabla }_{{\partial }_{k + 1}}\left( {{\nabla }_{{\partial }_{i}}V}\right)  = {\nabla }_{{\partial }_{i}}\left( {{\nabla }_{{\partial }_{k + 1}}V}\right)  = 0\;\text{ on }{M}_{k + 1}.
\]

![bo_d7dtff491nqc73eq8m7g_210_278_193_972_553_0.jpg](images/bo_d7dtff491nqc73eq8m7g_210_278_193_972_553_0.jpg)

Fig. 7.2: Proof of Lemma 7.8

This shows that \( {\nabla }_{{\partial }_{i}}V \) is parallel along the \( {x}^{k + 1} \) -curves starting on \( {M}_{k} \) . Since \( {\nabla }_{{\partial }_{i}}V \) vanishes on \( {M}_{k} \) and the zero vector field is the unique parallel transport of zero, we conclude that \( {\nabla }_{{\partial }_{i}}V \) is zero on each \( {x}^{k + 1} \) -curve. Since every point of \( {M}_{k + 1} \) is on one of these curves, it follows that \( {\nabla }_{{\partial }_{i}}V = 0 \) on all of \( {M}_{k + 1} \) . This completes the inductive step to show that \( V \) is parallel.

- Exercise 7.9. Prove that the vector field \( V \) constructed in the preceding proof is smooth.

Theorem 7.10. A Riemannian or pseudo-Riemannian manifold is flat if and only if its curvature tensor vanishes identically.

Proof. One direction is immediate: Proposition 7.2 showed that the Levi-Civita connection of a flat metric satisfies the flatness criterion, so its curvature endomorphism is identically zero, which implies that the curvature tensor is also zero.

Now suppose \( \left( {M, g}\right) \) has vanishing curvature tensor. This means that the curvature endomorphism vanishes as well, so the Levi-Civita connection satisfies the flatness criterion. We begin by showing that \( g \) shares one important property with Euclidean and pseudo-Euclidean metrics: it admits a parallel orthonormal frame in a neighborhood of each point.

Let \( p \in  M \) , and choose an orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{p}M \) . In the pseudo-Riemannian case, we may assume that the basis is in standard order (with positive entries before negative ones in the matrix \( {g}_{ij} = {g}_{p}\left( {{b}_{i},{b}_{j}}\right) \) ). Lemma 7.8 shows that there exist parallel vector fields \( {E}_{1},\ldots ,{E}_{n} \) on a neighborhood \( U \) of \( p \) such that \( {\left. {E}_{i}\right| }_{p} = {b}_{i} \) for each \( i = 1,\ldots , n \) . Because parallel transport preserves inner products, the vector fields \( \left( {E}_{j}\right) \) are orthonormal (and hence linearly independent) in all of \( U \) .

Because the Levi-Civita connection is symmetric, we have

\[
\left\lbrack  {{E}_{i},{E}_{j}}\right\rbrack   = {\nabla }_{{E}_{i}}{E}_{j} - {\nabla }_{{E}_{j}}{E}_{i} = 0.
\]

![bo_d7dtff491nqc73eq8m7g_211_458_198_588_432_0.jpg](images/bo_d7dtff491nqc73eq8m7g_211_458_198_588_432_0.jpg)

Fig. 7.3: The curvature endomorphism and parallel transport around a closed loop

Thus the vector fields \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) form a commuting orthonormal frame on \( U \) . The canonical form theorem for commuting vector fields (Prop. A.48) shows that there are coordinates \( \left( {{y}^{1},\ldots ,{y}^{n}}\right) \) on a (possibly smaller) neighborhood of \( p \) such that \( {E}_{i} = \partial /\partial {y}^{i} \) for \( i = 1,\ldots , n \) . In any such coordinates, \( {g}_{ij} = g\left( {{\partial }_{i},{\partial }_{j}}\right)  = g\left( {{E}_{i},{E}_{j}}\right)  = \; \pm  {\delta }_{ij} \) , so the map \( y = \left( {{y}^{1},\ldots ,{y}^{n}}\right) \) is an isometry from a neighborhood of \( p \) to an open subset of the appropriate Euclidean or pseudo-Euclidean space.

Using similar ideas, we can give a more precise interpretation of the meaning of the curvature tensor: it is a measure of the extent to which parallel transport around a small rectangle fails to be the identity map.

Theorem 7.11. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold; let I be an open interval containing 0; let \( \Gamma  : I \times  I \rightarrow  M \) be a smooth one-parameter family of curves; and let \( p = \Gamma \left( {0,0}\right) , x = {\partial }_{s}\Gamma \left( {0,0}\right) \) , and \( y = {\partial }_{t}\Gamma \left( {0,0}\right) \) . For any \( {s}_{1},{s}_{2},{t}_{1},{t}_{2} \in  I \) , let \( {P}_{{s}_{1},{t}_{1}}^{{s}_{1},{t}_{2}} : {T}_{\Gamma \left( {{s}_{1},{t}_{1}}\right) }M \rightarrow  {T}_{\Gamma \left( {{s}_{1},{t}_{2}}\right) }M \) denote parallel transport along the curve \( t \mapsto  \Gamma \left( {{s}_{1}, t}\right) \) from time \( {t}_{1} \) to time \( {t}_{2} \) , and let \( {P}_{{s}_{1},{t}_{1}}^{{s}_{2},{t}_{1}} : {T}_{\Gamma \left( {{s}_{1},{t}_{1}}\right) }M \rightarrow \; {T}_{\Gamma \left( {{s}_{2},{t}_{1}}\right) }M \) denote parallel transport along the curve \( s \mapsto  \Gamma \left( {s,{t}_{1}}\right) \) from time \( {s}_{1} \) to time \( {s}_{2} \) . (See Fig. 7.3.) Then for every \( z \in  {T}_{p}M \) ,

\[
R\left( {x, y}\right) z = \mathop{\lim }\limits_{{\delta ,\varepsilon  \rightarrow  0}}\frac{{P}_{\delta ,0}^{0,0} \circ  {P}_{\delta ,\varepsilon }^{\delta ,0} \circ  {P}_{0,\varepsilon }^{\delta ,\varepsilon } \circ  {P}_{0,0}^{0,\varepsilon }\left( z\right)  - z}{\delta \varepsilon }. \tag{7.10}
\]

Proof. Define a vector field \( Z \) along \( \Gamma \) by first parallel transporting \( z \) along the curve \( t \mapsto  \Gamma \left( {0, t}\right) \) , and then for each \( t \) , parallel transporting \( Z\left( {0, t}\right) \) along the curve \( s \mapsto  \Gamma \left( {s, t}\right) \) . The resulting vector field along \( \Gamma \) is smooth by another application of Theorem 4.31; and by construction, it satisfies \( {D}_{t}Z\left( {0, t}\right)  = 0 \) for all \( t \in  I \) , and \( {D}_{s}Z\left( {s, t}\right)  = 0 \) for all \( \left( {s, t}\right)  \in  I \times  I \) . Proposition 7.5 shows that

\[
R\left( {x, y}\right) z = {D}_{s}{D}_{t}Z\left( {0,0}\right)  - {D}_{t}{D}_{s}Z\left( {0,0}\right)  = {D}_{s}{D}_{t}Z\left( {0,0}\right) .
\]

Thus we need only show that \( {D}_{s}{D}_{t}Z\left( {0,0}\right) \) is equal to the limit on the right-hand side of (7.10).

From Theorem 4.34, we have

\[
{D}_{t}Z\left( {s,0}\right)  = \mathop{\lim }\limits_{{\varepsilon  \rightarrow  0}}\frac{{P}_{s,\varepsilon }^{s,0}\left( {Z\left( {s,\varepsilon }\right) }\right)  - Z\left( {s,0}\right) }{\varepsilon }, \tag{7.11}
\]

\[
{D}_{s}{D}_{t}Z\left( {0,0}\right)  = \mathop{\lim }\limits_{{\delta  \rightarrow  0}}\frac{{P}_{\delta ,0}^{0,0}\left( {{D}_{t}Z\left( {\delta ,0}\right) }\right)  - {D}_{t}Z\left( {0,0}\right) }{\delta }. \tag{7.12}
\]

Evaluating (7.11) first at \( s = \delta \) and then at \( s = 0 \) , and inserting the resulting expressions into (7.12), we obtain

\[
{D}_{s}{D}_{t}Z\left( {0,0}\right)
\]

\[
= \mathop{\lim }\limits_{{\delta ,\varepsilon  \rightarrow  0}}\frac{{P}_{\delta ,0}^{0,0} \circ  {P}_{\delta ,\varepsilon }^{\delta ,0}\left( {Z\left( {\delta ,\varepsilon }\right) }\right)  - {P}_{\delta ,0}^{0,0}\left( {Z\left( {\delta ,0}\right) }\right)  - {P}_{0,\varepsilon }^{0,0}\left( {Z\left( {0,\varepsilon }\right) }\right)  + Z\left( {0,0}\right) }{\delta \varepsilon }. \tag{7.13}
\]

Here we have used the fact that parallel transport is linear, so the \( \varepsilon \) -limit can be pulled past \( {P}_{\delta ,0}^{0,0} \) .

Now, the fact that \( Z \) is parallel along \( t \mapsto  \Gamma \left( {0, t}\right) \) and along all of the curves \( s \mapsto  \Gamma \left( {s, t}\right) \) implies

\[
{P}_{\delta ,0}^{0,0}\left( {Z\left( {\delta ,0}\right) }\right)  = {P}_{0,\varepsilon }^{0,0}\left( {Z\left( {0,\varepsilon }\right) }\right)  = Z\left( {0,0}\right)  = z
\]

\[
Z\left( {\delta ,\varepsilon }\right)  = {P}_{0,\varepsilon }^{\delta ,\varepsilon }\left( {Z\left( {0,\varepsilon }\right) }\right)  = {P}_{0,\varepsilon }^{\delta ,\varepsilon } \circ  {P}_{0,0}^{0,\varepsilon }\left( z\right) .
\]

Inserting these relations into (7.13) yields (7.10).

## Symmetries of the Curvature Tensor

The curvature tensor on a Riemannian or pseudo-Riemannian manifold has a number of symmetries besides the obvious skew-symmetry in its first two arguments.

Proposition 7.12 (Symmetries of the Curvature Tensor). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold. The \( \left( {0,4}\right) \) -curvature tensor of \( g \) has the following symmetries for all vector fields \( W, X, Y, Z \) :

(a) \( \operatorname{Rm}\left( {W, X, Y, Z}\right)  =  - \operatorname{Rm}\left( {X, W, Y, Z}\right) \) .

(b) \( \operatorname{Rm}\left( {W, X, Y, Z}\right)  =  - \operatorname{Rm}\left( {W, X, Z, Y}\right) \) .

(c) \( \operatorname{Rm}\left( {W, X, Y, Z}\right)  = \operatorname{Rm}\left( {Y, Z, W, X}\right) \) .

(d) \( \operatorname{Rm}\left( {W, X, Y, Z}\right)  + \operatorname{Rm}\left( {X, Y, W, Z}\right)  + \operatorname{Rm}\left( {Y, W, X, Z}\right)  = 0 \) .

Before we begin the proof, a few remarks are in order. First, as the proof will show, (a) is a trivial consequence of the definition of the curvature endomorphism; (b) follows from the compatibility of the Levi-Civita connection with the metric; (d)

follows from the symmetry of the connection; and (c) follows from (a), (b), and (d). The identity in (d) is called the algebraic Bianchi identity (or more traditionally but less informatively, the first Bianchi identity). It is easy to show using (a)-(d) that a three-term sum obtained by cyclically permuting any three arguments of \( {Rm} \) is also zero. Finally, it is useful to record the form of these symmetries in terms of components with respect to any basis:

\( \left( {\mathrm{a}}^{\prime }\right) {R}_{ijkl} =  - {R}_{jikl} \) .

\( \left( {\mathrm{b}}^{\prime }\right) {R}_{ijkl} =  - {R}_{ijlk}. \)

\( \left( {\mathrm{c}}^{\prime }\right) {R}_{ijkl} = {R}_{klij}. \)

\( \left( {\mathrm{d}}^{\prime }\right) {R}_{ijkl} + {R}_{jkil} + {R}_{kijl} = 0. \)

Proof of Proposition 7.12. Identity (a) is immediate from the definition of the curvature tensor, because \( R\left( {W, X}\right) Y =  - R\left( {X, W}\right) Y \) . To prove (b), it suffices to show that \( {Rm}\left( {W, X, Y, Y}\right)  = 0 \) for all \( Y \) , for then (b) follows from the expansion of \( \operatorname{Rm}\left( {W, X, Y + Z, Y + Z}\right)  = 0 \) . Using compatibility with the metric, we have

\[
{WX}{\left| Y\right| }^{2} = W\left( {2\left\langle  {{\nabla }_{X}Y, Y}\right\rangle  }\right)  = 2\left\langle  {{\nabla }_{W}{\nabla }_{X}Y, Y}\right\rangle   + 2\left\langle  {{\nabla }_{X}Y,{\nabla }_{W}Y}\right\rangle
\]

\[
{XW}{\left| Y\right| }^{2} = X\left( {2\left\langle  {{\nabla }_{W}Y, Y}\right\rangle  }\right)  = 2\left\langle  {{\nabla }_{X}{\nabla }_{W}Y, Y}\right\rangle   + 2\left\langle  {{\nabla }_{W}Y,{\nabla }_{X}Y}\right\rangle
\]

\[
\left\lbrack  {W, X}\right\rbrack  {\left| Y\right| }^{2} = 2\left\langle  {{\nabla }_{\left\lbrack  W, X\right\rbrack  }Y, Y}\right\rangle  .
\]

When we subtract the second and third equations from the first, the left-hand side is zero. The terms \( 2\left\langle  {{\nabla }_{X}Y,{\nabla }_{W}Y}\right\rangle \) and \( 2\left\langle  {{\nabla }_{W}Y,{\nabla }_{X}Y}\right\rangle \) cancel on the right-hand side, giving

\[
0 = 2\left\langle  {{\nabla }_{W}{\nabla }_{X}Y, Y}\right\rangle   - 2\left\langle  {{\nabla }_{X}{\nabla }_{W}Y, Y}\right\rangle   - 2\left\langle  {{\nabla }_{\left\lbrack  W, X\right\rbrack  }Y, Y}\right\rangle
\]

\[
= 2\langle R\left( {W, X}\right) Y, Y\rangle
\]

\[
= {2Rm}\left( {W, X, Y, Y}\right) \text{ . }
\]

Next we prove (d). From the definition of \( {Rm} \) , this will follow immediately from

\[
R\left( {W, X}\right) Y + R\left( {X, Y}\right) W + R\left( {Y, W}\right) X = 0.
\]

Using the definition of \( R \) and the symmetry of the connection, the left-hand side expands to

\[
\left( {{\nabla }_{W}{\nabla }_{X}Y - {\nabla }_{X}{\nabla }_{W}Y - {\nabla }_{\left\lbrack  W, X\right\rbrack  }Y}\right)
\]

\[
+ \left( {{\nabla }_{X}{\nabla }_{Y}W - {\nabla }_{Y}{\nabla }_{X}W - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }W}\right)
\]

\[
+ \left( {{\nabla }_{Y}{\nabla }_{W}X - {\nabla }_{W}{\nabla }_{Y}X - {\nabla }_{\left\lbrack  Y, W\right\rbrack  }X}\right)
\]

\[
= {\nabla }_{W}\left( {{\nabla }_{X}Y - {\nabla }_{Y}X}\right)  + {\nabla }_{X}\left( {{\nabla }_{Y}W - {\nabla }_{W}Y}\right)  + {\nabla }_{Y}\left( {{\nabla }_{W}X - {\nabla }_{X}W}\right)
\]

\[
- {\nabla }_{\left\lbrack  W, X\right\rbrack  }Y - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }W - {\nabla }_{\left\lbrack  Y, W\right\rbrack  }X
\]

\[
= {\nabla }_{W}\left\lbrack  {X, Y}\right\rbrack   + {\nabla }_{X}\left\lbrack  {Y, W}\right\rbrack   + {\nabla }_{Y}\left\lbrack  {W, X}\right\rbrack
\]

\[
- {\nabla }_{\left\lbrack  W, X\right\rbrack  }Y - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }W - {\nabla }_{\left\lbrack  Y, W\right\rbrack  }X
\]

\[
= \left\lbrack  {W,\left\lbrack  {X, Y}\right\rbrack  }\right\rbrack   + \left\lbrack  {X,\left\lbrack  {Y, W}\right\rbrack  }\right\rbrack   + \left\lbrack  {Y,\left\lbrack  {W, X}\right\rbrack  }\right\rbrack  .
\]

This is zero by the Jacobi identity.

Finally, we show that identity (c) follows from the other three. Writing the algebraic Bianchi identity four times with indices cyclically permuted gives

\[
{Rm}\left( {W, X, Y, Z}\right)  + {Rm}\left( {X, Y, W, Z}\right)  + {Rm}\left( {Y, W, X, Z}\right)  = 0,
\]

\[
{Rm}\left( {X, Y, Z, W}\right)  + {Rm}\left( {Y, Z, X, W}\right)  + {Rm}\left( {Z, X, Y, W}\right)  = 0,
\]

\[
{Rm}\left( {Y, Z, W, X}\right)  + {Rm}\left( {Z, W, Y, X}\right)  + {Rm}\left( {W, Y, Z, X}\right)  = 0,
\]

\[
{Rm}\left( {Z, W, X, Y}\right)  + {Rm}\left( {W, X, Z, Y}\right)  + {Rm}\left( {X, Z, W, Y}\right)  = 0.
\]

Now add up all four equations. Applying (b) four times makes all the terms in the first two columns cancel. Then applying (a) and (b) in the last column yields \( {2Rm}\left( {Y, W, X, Z}\right)  - {2Rm}\left( {X, Z, Y, W}\right)  = 0 \) , which is equivalent to (c).

There is one more identity that is satisfied by the covariant derivatives of the curvature tensor on every Riemannian manifold. Classically, it was called the second Bianchi identity, but modern authors tend to use the more informative name differential Bianchi identity.

Proposition 7.13 (Differential Bianchi Identity). The total covariant derivative of the curvature tensor satisfies the following identity:

\[
\nabla \operatorname{Rm}\left( {X, Y, Z, V, W}\right)  + \nabla \operatorname{Rm}\left( {X, Y, V, W, Z}\right)  + \nabla \operatorname{Rm}\left( {X, Y, W, Z, V}\right)  = 0. \tag{7.14}
\]

In components, this is

\[
{R}_{{ijkl};m} + {R}_{{ijlm};k} + {R}_{{ijmk};l} = 0. \tag{7.15}
\]

Proof. First of all, by the symmetries of \( {Rm},\left( {7.14}\right) \) is equivalent to

\[
\nabla \operatorname{Rm}\left( {Z, V, X, Y, W}\right)  + \nabla \operatorname{Rm}\left( {V, W, X, Y, Z}\right)  + \nabla \operatorname{Rm}\left( {W, Z, X, Y, V}\right)  = 0. \tag{7.16}
\]

This can be proved by a long and tedious computation, but there is a standard shortcut for such calculations in Riemannian geometry that makes our task immeasurably easier. To prove that (7.16) holds at a particular point \( p \) , it suffices by multilinear-ity to prove the formula when \( X, Y, Z, V, W \) are basis vectors with respect to some frame. The shortcut consists in choosing a special frame for each point \( p \) to simplify the computations there.

Let \( p \) be an arbitrary point, let \( \left( {x}^{i}\right) \) be normal coordinates centered at \( p \) , and let \( X, Y, Z, V, W \) be arbitrary coordinate basis vector fields. These vectors satisfy two properties that simplify our computations enormously: (1) their commutators vanish identically, since \( \left\lbrack  {{\partial }_{i},{\partial }_{j}}\right\rbrack   \equiv  0 \) ; and (2) their covariant derivatives vanish at \( p \) , since \( {\Gamma }_{ij}^{k}\left( p\right)  = 0 \) (Prop. 5.24(d)).

Using these facts and the compatibility of the connection with the metric, the first term in (7.16) evaluated at \( p \) becomes

\[
\left( {{\nabla }_{W}{Rm}}\right) \left( {Z, V, X, Y}\right)  = {\nabla }_{W}\left( {{Rm}\left( {Z, V, X, Y}\right) }\right)
\]

\[
= {\nabla }_{W}\langle R\left( {Z, V}\right) X, Y\rangle
\]

\[
= {\nabla }_{W}\left\langle  {{\nabla }_{Z}{\nabla }_{V}X - {\nabla }_{V}{\nabla }_{Z}X - {\nabla }_{\left\lbrack  Z, V\right\rbrack  }X, Y}\right\rangle
\]

\[
= \left\langle  {{\nabla }_{W}{\nabla }_{Z}{\nabla }_{V}X - {\nabla }_{W}{\nabla }_{V}{\nabla }_{Z}X, Y}\right\rangle  .
\]

Write this equation three times, with the vector fields \( W, Z, V \) cyclically permuted. Summing all three gives

\[
\nabla \operatorname{Rm}\left( {Z, V, X, Y, W}\right)  + \nabla \operatorname{Rm}\left( {V, W, X, Y, Z}\right)  + \nabla \operatorname{Rm}\left( {W, Z, X, Y, V}\right)
\]

\[
= \left\langle  {{\nabla }_{W}{\nabla }_{Z}{\nabla }_{V}X - {\nabla }_{W}{\nabla }_{V}{\nabla }_{Z}X}\right.
\]

\[
+ {\nabla }_{Z}{\nabla }_{V}{\nabla }_{W}X - {\nabla }_{Z}{\nabla }_{W}{\nabla }_{V}X
\]

\[
+ {\nabla }_{V}{\nabla }_{W}{\nabla }_{Z}X - {\nabla }_{V}{\nabla }_{Z}{\nabla }_{W}X, Y\rangle
\]

\[
= \left\langle  {R\left( {W, Z}\right) \left( {{\nabla }_{V}X}\right)  + R\left( {Z, V}\right) \left( {{\nabla }_{W}X}\right)  + R\left( {V, W}\right) \left( {{\nabla }_{Z}X}\right) , Y}\right\rangle
\]

\[
= 0\text{ , }
\]

where the last line follows because \( {\nabla }_{V}X = {\nabla }_{W}X = {\nabla }_{Z}X = 0 \) at \( p \) .

## The Ricci Identities

The curvature endomorphism also appears as the obstruction to commutation of total covariant derivatives. Recall from Chapter 4 that if \( F \) is any smooth tensor field of type \( \left( {k, l}\right) \) , then its second covariant derivative \( {\nabla }^{2}F = \nabla \left( {\nabla F}\right) \) is a smooth \( \left( {k, l + 2}\right) \) -tensor field, and for vector fields \( X \) and \( Y \) , the notation \( {\nabla }_{X, Y}^{2}F \) denotes \( {\nabla }^{2}F\left( {\ldots , Y, X}\right) \) . Given vector fields \( X \) and \( Y \) , let \( R{\left( X, Y\right) }^{ * } : {T}^{ * }M \rightarrow  {T}^{ * }M \) denote the dual map to \( R\left( {X, Y}\right) \) , defined by

\[
\left( {R{\left( X, Y\right) }^{ * }\eta }\right) \left( Z\right)  = \eta \left( {R\left( {X, Y}\right) Z}\right) .
\]

Theorem 7.14 (Ricci Identities). On a Riemannian or pseudo-Riemannian manifold \( M \) , the second total covariant derivatives of vector and tensor fields satisfy the following identities. If \( Z \) is a smooth vector field,

\[
{\nabla }_{X, Y}^{2}Z - {\nabla }_{Y, X}^{2}Z = R\left( {X, Y}\right) Z. \tag{7.17}
\]

If \( \beta \) is a smooth 1-form,

\[
{\nabla }_{X, Y}^{2}\beta  - {\nabla }_{Y, X}^{2}\beta  =  - R{\left( X, Y\right) }^{ * }\beta . \tag{7.18}
\]

And if \( B \) is a smooth \( \left( {k, l}\right) \) -tensor field,

\[
\left( {{\nabla }_{X, Y}^{2}B - {\nabla }_{Y, X}^{2}B}\right) \left( {{\omega }^{1},\ldots ,{\omega }^{k},{V}_{1},\ldots ,{V}_{l}}\right)
\]

\[
= B\left( {R{\left( X, Y\right) }^{ * }{\omega }^{1},{\omega }^{2},\ldots ,{\omega }^{k},{V}_{1},\ldots ,{V}_{l}}\right)  + \cdots
\]

\[
+ B\left( {{\omega }^{1},\ldots ,{\omega }^{k - 1}, R{\left( X, Y\right) }^{ * }{\omega }^{k},{V}_{1},\ldots ,{V}_{l}}\right) \tag{7.19}
\]

\[
- B\left( {{\omega }^{1},\ldots ,{\omega }^{k}, R\left( {X, Y}\right) {V}_{1},{V}_{2},\ldots ,{V}_{l}}\right)  - \cdots
\]

\[
\left. {-B\left( {{\omega }^{1},\ldots ,{\omega }^{k},{V}_{1},\ldots ,{V}_{l - 1}, R\left( {X, Y}\right) {V}_{l}}\right) }\right) \text{ , }
\]

for all covector fields \( {\omega }^{i} \) and vector fields \( {V}_{j} \) . In terms of any local frame, the component versions of these formulas read

\[
{Z}^{i}{}_{;{pq}} - {Z}^{i}{}_{;{qp}} =  - {R}_{pqm}{}^{i}{Z}^{m}, \tag{7.20}
\]

\[
{\beta }_{j;{pq}} - {\beta }_{j;{qp}} = {R}_{pqj}{}^{m}{\beta }_{m}, \tag{7.21}
\]

\[
{B}_{{j}_{1}\ldots {j}_{l};{pq}}^{{i}_{1}\ldots {i}_{k}} - {B}_{{j}_{1}\ldots {j}_{l};{qp}}^{{i}_{1}\ldots {i}_{k}} =  - {R}_{pqm}{}^{{i}_{1}}{B}_{{j}_{1}\ldots {j}_{l}}^{m{i}_{2}\ldots {i}_{k}} - \cdots  - {R}_{pqm}{}^{{i}_{k}}{B}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k - 1}m}
\]

\[
+ {R}_{{pq}{j}_{1}}{}^{m}{B}_{m{j}_{2}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}} + \cdots  + {R}_{{pq}{j}_{l}}{}^{m}{B}_{{j}_{1}\ldots {j}_{l - 1}m}^{{i}_{1}\ldots {i}_{k}}. \tag{7.22}
\]

Proof. For any tensor field \( B \) and vector fields \( X, Y \) , Proposition 4.21 implies

\[
{\nabla }_{X, Y}^{2}B - {\nabla }_{Y, X}^{2}B = {\nabla }_{X}{\nabla }_{Y}B - {\nabla }_{\left( {\nabla }_{X}Y\right) }B - {\nabla }_{Y}{\nabla }_{X}B + {\nabla }_{\left( {\nabla }_{Y}X\right) }B \tag{7.23}
\]

\[
= {\nabla }_{X}{\nabla }_{Y}B - {\nabla }_{Y}{\nabla }_{X}B - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }B,
\]

where the last equality follows from the symmetry of the connection. In particular, this holds when \( B = Z \) is a vector field, so (7.17) follows directly from the definition of the curvature endomorphism.

Next we prove (7.18). Using (4.13) repeatedly, we compute

\[
\left( {{\nabla }_{X}{\nabla }_{Y}\beta }\right) \left( Z\right)  = X\left( {\left( {{\nabla }_{Y}\beta }\right) \left( Z\right) }\right)  - \left( {{\nabla }_{Y}\beta }\right) \left( {{\nabla }_{X}Z}\right)
\]

\[
= X\left( {Y\left( {\beta \left( Z\right) }\right)  - \beta \left( {{\nabla }_{Y}Z}\right) }\right)  - \left( {{\nabla }_{Y}\beta }\right) \left( {{\nabla }_{X}Z}\right)
\]

\[
= {XY}\left( {\beta \left( Z\right) }\right)  - \left( {{\nabla }_{X}\beta }\right) \left( {{\nabla }_{Y}Z}\right)  - \beta \left( {{\nabla }_{X}{\nabla }_{Y}Z}\right)  - \left( {{\nabla }_{Y}\beta }\right) \left( {{\nabla }_{X}Z}\right) .
\]

(7.24)

Reversing the roles of \( X \) and \( Y \) , we get

\[
\left( {{\nabla }_{Y}{\nabla }_{X}\beta }\right) \left( Z\right)  = {YX}\left( {\beta \left( Z\right) }\right)  - \left( {{\nabla }_{Y}\beta }\right) \left( {{\nabla }_{X}Z}\right)  - \beta \left( {{\nabla }_{Y}{\nabla }_{X}Z}\right)  - \left( {{\nabla }_{X}\beta }\right) \left( {{\nabla }_{Y}Z}\right) ,
\]

(7.25)

and applying (4.13) one more time yields

\[
\left( {{\nabla }_{\left\lbrack  X, Y\right\rbrack  }\beta }\right) \left( Z\right)  = \left\lbrack  {X, Y}\right\rbrack  \left( {\beta \left( Z\right) }\right)  - \beta \left( {{\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z}\right) . \tag{7.26}
\]

Now subtract (7.25) and (7.26) from (7.24): all but three of the terms cancel, yielding

\[
\left( {{\nabla }_{X}{\nabla }_{Y}\beta  - {\nabla }_{Y}{\nabla }_{X}\beta  - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }\beta }\right) \left( Z\right)  =  - \beta \left( {{\nabla }_{X}{\nabla }_{Y}Z - {\nabla }_{Y}{\nabla }_{X}Z - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z}\right)
\]

\[
=  - \beta \left( {R\left( {X, Y}\right) Z}\right) ,
\]

which is equivalent to (7.18).

Next consider the action of \( {\nabla }_{X, Y}^{2} - {\nabla }_{Y, X}^{2} \) on an arbitrary tensor product:

\[
\left( {{\nabla }_{X, Y}^{2} - {\nabla }_{Y, X}^{2}}\right) \left( {F \otimes  G}\right)
\]

\[
= \left( {{\nabla }_{X}{\nabla }_{Y} - {\nabla }_{Y}{\nabla }_{X} - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }}\right) \left( {F \otimes  G}\right)
\]

\[
= {\nabla }_{X}{\nabla }_{Y}F \otimes  G + {\nabla }_{Y}F \otimes  {\nabla }_{X}G + {\nabla }_{X}F \otimes  {\nabla }_{Y}G + F \otimes  {\nabla }_{X}{\nabla }_{Y}G
\]

\[
- {\nabla }_{Y}{\nabla }_{X}F \otimes  G - {\nabla }_{X}F \otimes  {\nabla }_{Y}G - {\nabla }_{Y}F \otimes  {\nabla }_{X}G - F \otimes  {\nabla }_{Y}{\nabla }_{X}G
\]

\[
- {\nabla }_{\left\lbrack  X, Y\right\rbrack  }F \otimes  G - F \otimes  {\nabla }_{\left\lbrack  X, Y\right\rbrack  }G
\]

\[
= \left( {{\nabla }_{X, Y}^{2}F - {\nabla }_{Y, X}^{2}F}\right)  \otimes  G + F \otimes  \left( {{\nabla }_{X, Y}^{2}G - {\nabla }_{Y, X}^{2}G}\right) .
\]

A simple induction using this relation together with (7.17) and (7.18) shows that for all smooth vector fields \( {W}_{1},\ldots ,{W}_{k} \) and 1-forms \( {\eta }^{1},\ldots ,{\eta }^{l} \) ,

\[
\left( {{\nabla }_{X, Y}^{2} - {\nabla }_{Y, X}^{2}}\right) \left( {{W}_{1} \otimes  \cdots  \otimes  {W}_{k} \otimes  {\eta }^{1} \otimes  \cdots  \otimes  {\eta }^{l}}\right)
\]

\[
= \left( {R\left( {X, Y}\right) {W}_{1}}\right)  \otimes  {W}_{2} \otimes  \cdots  \otimes  {W}_{k} \otimes  {\eta }^{1} \otimes  \cdots  \otimes  {\eta }^{l} + \cdots
\]

\[
+ {W}_{1} \otimes  \cdots  \otimes  {W}_{k - 1} \otimes  \left( {R\left( {X, Y}\right) {W}_{k}}\right)  \otimes  {\eta }^{1} \otimes  \cdots  \otimes  {\eta }^{l}
\]

\[
+ {W}_{1} \otimes  \cdots  \otimes  {W}_{k} \otimes  \left( {-R{\left( X, Y\right) }^{ * }{\eta }^{1}}\right)  \otimes  {\eta }^{2} \otimes  \cdots  \otimes  {\eta }^{l} + \cdots
\]

\[
+ {W}_{1} \otimes  \cdots  \otimes  {W}_{k} \otimes  {\eta }^{1} \otimes  \cdots  \otimes  {\eta }^{l - 1} \otimes  \left( {-R{\left( X, Y\right) }^{ * }{\eta }^{l}}\right) .
\]

Since every tensor field can be written as a sum of tensor products of vector fields and 1-forms, this implies (7.19).

Finally, the component formula (7.22) follows by applying (7.19) to

\[
\left( {{\nabla }_{{E}_{q},{E}_{p}}^{2}B - {\nabla }_{{E}_{p},{E}_{q}}^{2}B}\right) \left( {{\varepsilon }^{{i}_{1}},\ldots ,{\varepsilon }^{{i}_{k}},{E}_{{j}_{1}},\ldots ,{E}_{{j}_{l}}}\right) ,
\]

where \( \left( {E}_{j}\right) \) and \( \left( {\varepsilon }^{i}\right) \) represent a local frame and its dual coframe, respectively, and using

\[
R\left( {{E}_{q},{E}_{p}}\right) {E}_{j} = {R}_{qpj}{}^{m}{E}_{m} =  - {R}_{pqj}{}^{m}{E}_{m},
\]

\[
R{\left( {E}_{q},{E}_{p}\right) }^{ * }{\varepsilon }^{i} = {R}_{qpm}{}^{i}{\varepsilon }^{m} =  - {R}_{pqm}{}^{i}{\varepsilon }^{m}.
\]

The other two component formulas are special cases of (7.22).

## Ricci and Scalar Curvatures

Suppose \( \left( {M, g}\right) \) is an \( n \) -dimensional Riemannian or pseudo-Riemannian manifold. Because 4-tensors are so complicated, it is often useful to construct simpler tensors that summarize some of the information contained in the curvature tensor. The most important such tensor is the Ricci curvature or Ricci tensor, denoted by \( {Rc} \) (or often Ric in the literature), which is the covariant 2-tensor field defined as the trace of the curvature endomorphism on its first and last indices. Thus for vector fields \( X, Y \) ,

\[
\operatorname{Rc}\left( {X, Y}\right)  = \operatorname{tr}\left( {Z \mapsto  R\left( {Z, X}\right) Y}\right) .
\]

The components of \( {Rc} \) are usually denoted by \( {R}_{ij} \) , so that

\[
{R}_{ij} = {R}_{kij}{}^{k} = {g}^{km}{R}_{kijm}.
\]

The scalar curvature is the function \( S \) defined as the trace of the Ricci tensor:

\[
S = {\operatorname{tr}}_{g}{Rc} = {R}_{i}{}^{i} = {g}^{ij}{R}_{ij}.
\]

It is probably not clear at this point why the Ricci tensor or scalar curvature might be interesting, and we do not yet have the tools to give them geometric interpretations. But be assured that there is such an interpretation; see Proposition 8.32.

Lemma 7.15. The Ricci curvature is a symmetric 2-tensor field. It can be expressed in any of the following ways:

\[
{R}_{ij} = {R}_{kij}{}^{k} = {R}_{ik}{}^{k}{}_{j} =  - {R}_{ki}{}^{k}{}_{j} =  - {R}_{ikj}{}^{k}.
\]

Exercise 7.16. Prove Lemma 7.15, using the symmetries of the curvature tensor.

It is sometimes useful to decompose the Ricci tensor into a multiple of the metric and a complementary piece with zero trace. Define the traceless Ricci tensor of \( g \) as the following symmetric 2-tensor:

\[
\overset{ \circ  }{Rc} = {Rc} - \frac{1}{n}{Sg}.
\]

Proposition 7.17. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian n-manifold. Then \( {\operatorname{tr}}_{g}{Rc} \equiv  0 \) , and the Ricci tensor decomposes orthogonally as

\[
{Rc} = \overset{ \circ  }{Rc} + \frac{1}{n}{Sg}. \tag{7.27}
\]

Therefore, in the Riemannian case,

\[
{\left| Rc\right| }_{g}^{2} = {\left| \overset{ \circ  }{Rc}\right| }_{g}^{2} + \frac{1}{n}{S}^{2}. \tag{7.28}
\]

Remark. The statement about norms, and others like it that we will prove below, works only in the Riemannian case because of the additional absolute value signs required to compute norms in the pseudo-Riemannian case. The pseudo-Riemannian analogue would be \( \langle {Rc},{Rc}{\rangle }_{g} = {\left\langle  Rc, Rc\right\rangle  }_{g} + \frac{1}{n}{S}^{2} \) , but this is not as useful.

Proof. Note that in every local frame, we have

\[
{\operatorname{tr}}_{g}g = {g}_{ij}{g}^{ji} = {\delta }_{i}^{i} = n.
\]

It then follows directly from the definition of \( \overset{ \circ  }{Rc} \) that \( {\operatorname{tr}}_{g}\overset{ \circ  }{Rc} \equiv  0 \) and (7.27) holds. The fact that the decomposition is orthogonal follows easily from the fact that for every symmetric 2-tensor \( h \) , we have

\[
\langle h, g\rangle  = {g}^{ik}{g}^{jl}{h}_{ij}{g}_{kl} = {g}^{ij}{h}_{ij} = {\operatorname{tr}}_{g}h,
\]

and therefore \( \langle {Rc}, g\rangle  = {\operatorname{tr}}_{g}{Rc} = 0 \) . Finally,(7.28) follows from (7.27) and the fact that \( \langle g, g\rangle  = {\operatorname{tr}}_{g}g = n \) .

The next proposition, which follows directly from the differential Bianchi identity, expresses some important relationships among the covariant derivatives of the various curvature tensors. To express it concisely, it is useful to introduce another operator on tensor fields. If \( T \) is a smooth 2-tensor field on a Riemannian or pseudo-Riemannian manifold, we define the exterior covariant derivative of \( \mathbf{T} \) to be the 3-tensor field \( {DT} \) defined by

\[
\left( {DT}\right) \left( {X, Y, Z}\right)  =  - \left( {\nabla T}\right) \left( {X, Y, Z}\right)  + \left( {\nabla T}\right) \left( {X, Z, Y}\right) . \tag{7.29}
\]

In terms of components, this is

\[
{\left( DT\right) }_{ijk} =  - {T}_{{ij};k} + {T}_{{ik};j}.
\]

(This operator is a generalization of the ordinary exterior derivative of a 1-form, which can be expressed in terms of the total covariant derivative by \( \left( {d\eta }\right) \left( {Y, Z}\right)  = \; - \left( {\nabla \eta }\right) \left( {Y, Z}\right)  + \left( {\nabla \eta }\right) \left( {Z, Y}\right) \) by the result of Problem 5-13. The exterior covariant derivative can be generalized to other types of tensors as well, but this is the only case we need.)

Proposition 7.18 (Contracted Bianchi Identities). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold. The covariant derivatives of the Riemann, Ricci, and scalar curvatures of \( g \) satisfy the following identities:

\[
{\operatorname{tr}}_{g}\left( {\nabla {Rm}}\right)  =  - D\left( {Rc}\right) , \tag{7.30}
\]

\[
{\operatorname{tr}}_{g}\left( {\nabla {Rc}}\right)  = \frac{1}{2}{dS} \tag{7.31}
\]

where the trace in each case is on the first and last indices. In components, this is

\[
{R}_{ijkl}{;}^{i} = {R}_{{jk};l} - {R}_{{jl};k}, \tag{7.32}
\]

\[
{R}_{{il};}{}^{i} = \frac{1}{2}{S}_{;l}. \tag{7.33}
\]

Proof. Start with the component form (7.15) of the differential Bianchi identity, raise the index \( m \) , and then contract on the indices \( i, m \) to obtain (7.32). (Note that covariant differentiation commutes with contraction by Proposition 4.15 and with the musical isomorphisms by Proposition 5.17, so it does not matter whether the indices that are raised and contracted come before or after the semicolon.) Then do the same with the indices \( j, k \) and simplify to obtain (7.33). The coordinate-free formulas (7.30) and (7.31) follow by expanding everything out in components.

It is important to note that if the sign convention chosen for the curvature tensor is the opposite of ours, then the Ricci tensor must be defined as the trace of \( {Rm} \) on the first and third (or second and fourth) indices. (The trace on the first two or last two indices is always zero by antisymmetry.) The definition is chosen so that the Ricci and scalar curvatures have the same meaning for everyone, regardless of the conventions chosen for the full curvature tensor. So, for example, if a manifold is said to have positive scalar curvature, there is no ambiguity as to what is meant.

A Riemannian or pseudo-Riemannian metric is said to be an Einstein metric if its Ricci tensor is a constant multiple of the metric-that is,

\[
{Rc} = {\lambda g}\;\text{ for some constant }\lambda \text{ . } \tag{7.34}
\]

This equation is known as the Einstein equation. As the next proposition shows, for connected manifolds of dimension greater than 2, it is not necessary to assume that \( \lambda \) is constant; just assuming that the Ricci tensor is a function times the metric is sufficient.

Proposition 7.19 (Schur’s Lemma). Suppose \( \left( {M, g}\right) \) is a connected Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) whose Ricci tensor satisfies \( {Rc} = {fg} \) for some smooth real-valued function \( f \) . Then \( f \) is constant and \( g \) is an Einstein metric.

Proof. Taking traces of both sides of \( {Rc} = {fg} \) shows that \( f = \frac{1}{n}S \) , so the traceless Ricci tensor is identically zero. It follows that \( \nabla {Rc} \equiv  0 \) . Because the covariant derivative of the metric is zero, this implies the following equation in any coordinate chart:

\[
0 = {R}_{{ij};k} - \frac{1}{n}{S}_{;k}{g}_{ij}.
\]

Tracing this equation on \( i \) and \( k \) , and comparing with the contracted Bianchi identity (7.33), we conclude that

\[
0 = \frac{1}{2}{S}_{;j} - \frac{1}{n}{S}_{;j}.
\]

Because \( n \geq  3 \) , this implies \( {S}_{;j} = 0 \) . But \( {S}_{;j} \) is the component of \( \nabla S = {dS} \) , so connectedness of \( M \) implies that \( S \) is constant and thus so is \( f \) .

Corollary 7.20. If \( \left( {M, g}\right) \) is a connected Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) , then \( g \) is Einstein if and only if \( {Rc} = 0 \) .

Proof. Suppose first that \( g \) is an Einstein metric with \( {Rc} = {\lambda g} \) . Taking traces of both sides, we find that \( \lambda  = \frac{1}{n}S \) , and therefore \( {Rc} = {Rc} - {\lambda g} = 0 \) . Conversely, if \( {Rc} = 0 \) , Schur’s lemma implies that \( g \) is Einstein.

By an argument analogous to those of Chapter 6, Hilbert showed (see [Bes87, Thm. 4.21]) that Einstein metrics are critical points for the total scalar curvature functional \( S\left( g\right)  = {\int }_{M}{Sd}{V}_{g} \) on the space of all metrics on \( M \) with fixed volume. Thus Einstein metrics can be viewed as "optimal" metrics in a certain sense, and as such they form an appealing higher-dimensional analogue of locally homogeneous metrics on 2-manifolds, with which one might hope to prove some sort of generalization of the uniformization theorem (Thm. 3.22). Although the statement of such a theorem cannot be as elegant as that of its 2-dimensional ancestor because there are known examples of smooth, compact manifolds that admit no Einstein metrics [Bes87, Chap. 6], there is still a reasonable hope that "most" higher-dimensional manifolds (in some sense) admit Einstein metrics. This is an active field of current research; see [Bes87] for a sweeping survey of Einstein metrics.

The term "Einstein metric" originated, as you might guess, in physics: the central assertion of Einstein's general theory of relativity is that physical spacetime is modeled by a 4-manifold that carries a Lorentz metric whose Ricci curvature satisfies the following Einstein field equation:

\[
{Rc} - \frac{1}{2}{Sg} = T \tag{7.35}
\]

where \( T \) is a certain symmetric 2-tensor field (the stress-energy tensor) that describes the density, momentum, and stress of the matter and energy present at each point in spacetime. It is shown in physics books (e.g., [CB09, pp. 51-53]) that (7.35) is the variational equation for a certain functional, called the Einstein-Hilbert action, on the space of all Lorentz metrics on a given 4-manifold. Einstein's theory can then be interpreted as the assertion that a physically realistic spacetime must be a critical point for this functional.

In the special case \( T \equiv  0,\left( {7.35}\right) \) reduces to the vacuum Einstein field equation \( {Rc} = \frac{1}{2}{Sg} \) . Taking traces of both sides and recalling that \( {\operatorname{tr}}_{g}g = \dim M = \) 4, we obtain \( S = {2S} \) , which implies \( S = 0 \) . Therefore, the vacuum Einstein equation is equivalent to \( {Rc} = 0 \) , which means that \( g \) is a (pseudo-Riemannian) Einstein metric in the mathematical sense of the word. (At one point in the development of the theory, Einstein considered adding a term \( {\Lambda g} \) to the left-hand side of (7.35), where \( \Lambda \) is a constant that he called the cosmological constant. With this modification the vacuum Einstein field equation would be exactly the same as the mathematicians' Einstein equation (7.34). Einstein soon decided that the cosmological constant was a mistake on physical grounds; however, researchers in general relativity have recently begun to believe that a theory with a nonzero cosmological constant might in fact have physical relevance.)

Other than these special cases and the obvious formal similarity between (7.35) and (7.34), there is no direct connection between the physicists' version of the Einstein equation and the mathematicians' version. The mathematical interest in Riemannian Einstein metrics stems more from their potential applications to uniformization in higher dimensions than from their relation to physics.

Another approach to generalizing the uniformization theorem to higher dimensions is to search for metrics of constant scalar curvature. These are also critical points of the total scalar curvature functional, but only with respect to variations of the metric with fixed volume within a given conformal equivalence class. Thus it makes sense to ask whether, given a metric \( g \) on a manifold \( M \) , there exists a metric \( \widetilde{g} \) conformal to \( g \) that has constant scalar curvature. This is called the Yamabe problem, because it was first posed in 1960 by Hidehiko Yamabe, who claimed to have proved that the answer is always yes when \( M \) is compact. Yamabe’s proof was later found to be in error, and it was two dozen years before the proof was finally completed by Richard Schoen; see [LP87] for an expository account of Schoen's solution. When \( M \) is noncompact, the issues are much subtler, and much current research is focused on determining exactly which conformal classes contain metrics of constant scalar curvature.

## The Weyl Tensor

As noted above, the Ricci and scalar curvatures contain only part of the information encoded into the curvature tensor. In this section, we introduce a tensor field called the Weyl tensor, which encodes all the rest.

We begin by considering some linear-algebraic aspects of tensors that have the symmetries of the curvature tensor. Suppose \( V \) is an \( n \) -dimensional real vector space. Let \( \mathcal{R}\left( {V}^{ * }\right)  \subseteq  {T}^{4}\left( {V}^{ * }\right) \) denote the vector space of all covariant 4-tensors \( T \) on \( V \) that have the symmetries of the \( \left( {0,4}\right) \) Riemann curvature tensor:

(a) \( T\left( {w, x, y, z}\right)  =  - T\left( {x, w, y, z}\right) \) .

(b) \( T\left( {w, x, y, z}\right)  =  - T\left( {w, x, z, y}\right) \) .

(c) \( T\left( {w, x, y, z}\right)  = T\left( {y, z, w, x}\right) \) .

(d) \( T\left( {w, x, y, z}\right)  + T\left( {x, y, w, z}\right)  + T\left( {y, w, x, z}\right)  = 0 \) .

(As the proof of Prop. 7.12 showed, (c) follows from the other three symmetries, so it would suffice to assume only (a), (b), and (d); but it is more convenient to include all four symmetries in the definition.) An element of \( \mathcal{R}\left( {V}^{ * }\right) \) is called an algebraic curvature tensor on \( V \) .

Proposition 7.21. If the vector space \( V \) has dimension \( n \) , then

\[
\dim \mathcal{R}\left( {V}^{ * }\right)  = \frac{{n}^{2}\left( {{n}^{2} - 1}\right) }{12}. \tag{7.36}
\]

Proof. Let \( \mathcal{B}\left( {V}^{ * }\right) \) denote the linear subspace of \( {T}^{4}\left( {V}^{ * }\right) \) consisting of tensors satisfying properties (a)-(c), and let \( {\sum }^{2}\left( {{\Lambda }^{2}{\left( V\right) }^{ * }}\right) \) denote the space of symmetric bilinear forms on the vector space \( {\Lambda }^{2}\left( V\right) \) of alternating contravariant 2-tensors on \( V \) . Define a map \( \Phi  : {\sum }^{2}\left( {{\Lambda }^{2}{\left( V\right) }^{ * }}\right)  \rightarrow  \mathcal{B}\left( {V}^{ * }\right) \) as follows:

\[
\Phi \left( B\right) \left( {w, x, y, z}\right)  = B\left( {w \land  x, y \land  z}\right) .
\]

It is easy to check that \( \Phi \left( B\right) \) satisfies (a)-(c), so \( \Phi \left( B\right)  \in  \mathcal{B}\left( {V}^{ * }\right) \) , and that \( \Phi \) is a linear map. In fact, it is an isomorphism, which we prove by constructing an inverse for it. Choose a basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( V \) , so the collection \( \left\{  {{b}_{i} \land  {b}_{j} : i < j}\right\} \) is a basis for \( {\Lambda }^{2}\left( V\right) \) . Define a map \( \Psi  : \mathcal{B}\left( {V}^{ * }\right)  \rightarrow  {\sum }^{2}\left( {{\Lambda }^{2}{\left( V\right) }^{ * }}\right) \) by setting

\[
\Psi \left( T\right) \left( {{b}_{i} \land  {b}_{j},{b}_{k} \land  {b}_{l}}\right)  = T\left( {{b}_{i},{b}_{j},{b}_{k},{b}_{l}}\right)
\]

when \( i < j \) and \( k < l \) , and extending by bilinearity. A straightforward computation shows that \( \Psi \) is an inverse for \( \Phi \) .

The upshot of the preceding construction is that

\[
\dim \mathcal{B}\left( {V}^{ * }\right)  = \dim \left( {{\sum }^{2}\left( {{\Lambda }^{2}{\left( V\right) }^{ * }}\right) }\right)  = \frac{\left( \begin{array}{l} n \\  2 \end{array}\right) \left( {\left( \begin{array}{l} n \\  2 \end{array}\right)  + 1}\right) }{2} = \frac{n\left( {n - 1}\right) \left( {{n}^{2} - n + 2}\right) }{8},
\]

where we have used the facts that \( \dim {\Lambda }^{2}\left( V\right)  = \left( \begin{array}{l} n \\  2 \end{array}\right)  = n\left( {n - 1}\right) /2 \) and the dimension of the space of symmetric bilinear forms on a vector space of dimension \( m \) is \( m\left( {m + 1}\right) /2 \) .

Now consider the linear map \( \pi  : \mathcal{B}\left( {V}^{ * }\right)  \rightarrow  {T}^{4}\left( {V}^{ * }\right) \) defined by

\[
\pi \left( T\right) \left( {w, x, y, z}\right)  = \frac{1}{3}\left( {T\left( {w, x, y, z}\right)  + T\left( {x, y, w, z}\right)  + T\left( {y, w, x, z}\right) }\right) .
\]

By definition, \( \mathcal{R}\left( {V}^{ * }\right) \) is equal to the kernel of \( \pi \) . In fact, \( \pi \) is equal to the restriction to \( \mathcal{B}\left( {V}^{ * }\right) \) of the operator Alt: \( {T}^{4}\left( {V}^{ * }\right)  \rightarrow  {\Lambda }^{4}\left( {V}^{ * }\right) \) defined by (B.9): thanks to the symmetries (a)-(c), the 24 terms in the definition of Alt \( T \) can be arranged in three groups of eight in such a way that all the terms in each group reduce to one of the terms in the definition of \( \pi \) . Thus the image of \( \pi \) is contained in \( {\Lambda }^{4}\left( {V}^{ * }\right) \) . In fact, the image is all of \( {\Lambda }^{4}\left( {V}^{ * }\right) \) : every \( T \in  {\Lambda }^{4}\left( {V}^{ * }\right) \) satisfies (a)-(c) and thus lies in \( \mathcal{B}\left( {V}^{ * }\right) \) , and \( \pi \left( T\right)  = \) Alt \( T = T \) for each such tensor.

Therefore, using the rank-nullity theorem of linear algebra, we conclude that

\[
\dim \mathcal{R}\left( {V}^{ * }\right)  = \dim \mathcal{B}\left( {V}^{ * }\right)  - \dim {\Lambda }^{4}\left( {V}^{ * }\right)  = \frac{n\left( {n - 1}\right) \left( {{n}^{2} - n + 2}\right) }{8} - \left( \begin{array}{l} n \\  4 \end{array}\right) ,
\]

and simplification yields (7.36).

Let us now assume that our vector space \( V \) is endowed with a (not necessarily positive definite) scalar product \( g \in  {\sum }^{2}\left( {V}^{ * }\right) \) . Let \( {\operatorname{tr}}_{g} : \mathcal{R}\left( {V}^{ * }\right)  \rightarrow  {\sum }^{2}\left( {V}^{ * }\right) \) denote the trace operation (with respect to \( g \) ) on the first and last indices (so that, for example, \( {Rc} = {\operatorname{tr}}_{g}\left( {Rm}\right) ) \) . It is natural to wonder whether this operator is surjective and what its kernel is, as a way of asking how much of the information contained in the Riemann curvature tensor is captured by the Ricci tensor. One way to try to answer the question is to attempt to construct a right inverse for the trace operator-a linear map \( G : {\sum }^{2}\left( {V}^{ * }\right)  \rightarrow  \mathcal{R}\left( {V}^{ * }\right) \) such that \( {\operatorname{tr}}_{g}\left( {G\left( S\right) }\right)  = S \) for all \( S \in  {\sum }^{2}\left( {V}^{ * }\right) \) .

Such an operator must start with a symmetric 2-tensor and construct a 4-tensor, using only the given 2-tensor and the metric. It turns out that there is a natural way to construct an algebraic curvature tensor out of two symmetric 2-tensors, which we now describe. Given \( h, k \in  {\sum }^{2}\left( {V}^{ * }\right) \) , we define a covariant 4-tensor \( h\text{ ① }k \) , called the Kulkarni-Nomizu product of \( \mathbf{h} \) and \( \mathbf{k} \) , by the following formula:

\[
h \oslash  k\left( {w, x, y, z}\right)  = h\left( {w, z}\right) k\left( {x, y}\right)  + h\left( {x, y}\right) k\left( {w, z}\right)
\]

\[
- h\left( {w, y}\right) k\left( {x, z}\right)  - h\left( {x, z}\right) k\left( {w, y}\right) . \tag{7.37}
\]

In terms of any basis, the components of \( h \oslash  k \) are

\[
{\left( h \oslash  k\right) }_{ijlm} = {h}_{im}{k}_{jl} + {h}_{jl}{k}_{im} - {h}_{il}{k}_{jm} - {h}_{jm}{k}_{il}.
\]

(It should be noted that the Kulkarni-Nomizu product must be defined as the negative of this expression when the Riemann curvature tensor is defined as the negative of ours.)

Lemma 7.22 (Properties of the Kulkarni-Nomizu Product). Let \( V \) be an \( n \) - dimensional vector space endowed with a scalar product \( g \) , let \( h \) and \( k \) be symmetric 2-tensors on \( V \) , let \( T \) be an algebraic curvature tensor on \( V \) , and let \( {\operatorname{tr}}_{g} \) denote the trace on the first and last indices.

(a) \( h \oslash  k \) is an algebraic curvature tensor.

(b) \( h \oslash  k = k \oslash  h \) .

(c) \( {\operatorname{tr}}_{g}\left( {h \oslash  g}\right)  = \left( {n - 2}\right) h + \left( {{\operatorname{tr}}_{g}h}\right) g \) .

(d) \( {\operatorname{tr}}_{g}\left( {g \oslash  g}\right)  = 2\left( {n - 1}\right) g \) .

(e) \( \langle T, h \oslash  g{\rangle }_{g} = 4{\left\langle  {\operatorname{tr}}_{g}T, h\right\rangle  }_{g} \) .

(f) In case \( g \) is positive definite, \( {\left| g \oslash  h\right| }_{g}^{2} = 4\left( {n - 2}\right) {\left| h\right| }_{g}^{2} + 4{\left( {\operatorname{tr}}_{g}h\right) }^{2} \) .

Proof. It is evident from the definition that \( h \oslash  k \) has three of the four symmetries of an algebraic curvature tensor: it is antisymmetric in its first two arguments and also in its last two, and its value is unchanged when the first two and last two arguments are interchanged. Thus to prove (a), only the algebraic Bianchi identity needs to be checked. This is a straightforward computation: when \( h@k\left( {w, x, y, z}\right) \) is written three times with the arguments \( w, x, y \) cyclically permuted and the three expressions are added together, all the terms cancel due to the symmetry of \( h \) and \( k \) .

Part (b) is immediate from the definition. To prove (c), choose a basis and use the definition to compute

\[
{\left( {\operatorname{tr}}_{g}\left( h \oslash  g\right) \right) }_{jk} = {g}^{im}\left( {{h}_{im}{g}_{jl} + {h}_{jl}{g}_{im} - {h}_{il}{g}_{jm} - {h}_{jm}{g}_{il}}\right)
\]

\[
= {h}_{i}{}^{i}{g}_{jl} + n{h}_{jl} - {h}_{jl} - {h}_{jl},
\]

which is equivalent to (c). Then (d) follows from (c) and the fact that \( {\operatorname{tr}}_{g}g = n \) .

The proofs of (e) and (f) are left to Problem 7-9.

Here is the primary application of the Kulkarni-Nomizu product.

Proposition 7.23. Let \( \left( {V, g}\right) \) be an \( n \) -dimensional scalar product space with \( n \geq  3 \) , and define a linear map \( G : {\sum }^{2}\left( {V}^{ * }\right)  \rightarrow  \mathcal{R}\left( {V}^{ * }\right) \) by

\[
G\left( h\right)  = \frac{1}{n - 2}\left( {h - \frac{{\operatorname{tr}}_{g}h}{2\left( {n - 1}\right) }g}\right)  \oslash  g. \tag{7.38}
\]

Then \( G \) is a right inverse for \( {\operatorname{tr}}_{g} \) , and its image is the orthogonal complement of the kernel of \( {\operatorname{tr}}_{g} \) in \( \mathcal{R}\left( {V}^{ * }\right) \) .

Proof. The fact that \( G \) is a right inverse is a straightforward computation based on the definition and Lemma 7.22(c, d). This implies that \( G \) is injective and \( {\operatorname{tr}}_{g} \) is surjective, so the dimension of \( \operatorname{Im}G \) is equal to the codimension of \( \operatorname{Ker}\left( {\operatorname{tr}}_{g}\right) \) , which in turn is equal to the dimension of \( \operatorname{Ker}{\left( {\operatorname{tr}}_{g}\right) }^{ \bot  } \) . If \( T \in  \mathcal{R}\left( {V}^{ * }\right) \) is an algebraic curvature tensor such that \( {\operatorname{tr}}_{g}T = 0 \) , then Lemma 7.22(e) shows that \( \langle T, G\left( h\right) \rangle  = 0 \) , so it follows by dimensionality that \( \operatorname{Im}G = \operatorname{Ker}{\left( {\operatorname{tr}}_{g}\right) }^{ \bot  } \) .

Now suppose \( g \) is a Riemannian or pseudo-Riemannian metric. Define the Schouten tensor of \( g \) , denoted by \( P \) , to be the following symmetric 2-tensor field:

\[
P = \frac{1}{n - 2}\left( {{Rc} - \frac{S}{2\left( {n - 1}\right) }g}\right) ;
\]

and define the Weyl tensor of \( g \) to be the following algebraic curvature tensor field:

\[
W = {Rm} - P \oslash  g
\]

\[
= {Rm} - \frac{1}{n - 2}{Rc} \oslash  g + \frac{S}{2\left( {n - 1}\right) \left( {n - 2}\right) }g \oslash  g.
\]

Proposition 7.24. For every Riemannian or pseudo-Riemannian manifold \( \left( {M, g}\right) \) of dimension \( n \geq  3 \) , the trace of the Weyl tensor is zero, and \( {Rm} = W + P \oslash  g \) is the orthogonal decomposition of \( {Rm} \) corresponding to \( \mathcal{R}\left( {V}^{ * }\right)  = \operatorname{Ker}\left( {\operatorname{tr}}_{g}\right)  \oplus  \operatorname{Ker}{\left( {\operatorname{tr}}_{g}\right) }^{ \bot  } \) .

Proof. This follows immediately from Proposition 7.23 and the fact that \( P\text{ ① }g = \; G\left( {Rc}\right)  = G\left( {{\operatorname{tr}}_{g}{Rm}}\right) . \)

These results lead to some important simplifications in low dimensions.

Corollary 7.25 Let \( V \) be an \( n \) -dimensional real vector space.

(a) If \( n = 0 \) or \( n = 1 \) , then \( \mathcal{R}\left( {V}^{ * }\right)  = \{ 0\} \) .

(b) If \( n = 2 \) , then \( \mathcal{R}\left( {V}^{ * }\right) \) is 1-dimensional, spanned by \( g \oslash  g \) .

(c) If \( n = 3 \) , then \( \mathcal{R}\left( {V}^{ * }\right) \) is 6-dimensional, and \( G : {\sum }^{2}\left( {V}^{ * }\right)  \rightarrow  \mathcal{R}\left( {V}^{ * }\right) \) is an isomorphism.

Proof. The dimensional results follow immediately from Proposition 7.21. In the case \( n = 2 \) , Lemma 7.22(d) shows that \( {\operatorname{tr}}_{g}\left( {g \oslash  g}\right)  = {2g} \neq  0 \) , which implies that \( g \oslash  g \) is nonzero and therefore spans the 1-dimensional space \( \mathcal{R}\left( {V}^{ * }\right) \) .

Now consider \( n = 3 \) . Proposition 7.23 shows that \( {\operatorname{tr}}_{g} \circ  G \) is the identity, which means that \( G : {\sum }^{2}\left( {V}^{ * }\right)  \rightarrow  \mathcal{R}\left( {V}^{ * }\right) \) is injective. On the other hand, Proposition 7.21 shows that \( \dim \mathcal{R}\left( {V}^{ * }\right)  = 6 = \dim {\sum }^{2}\left( {V}^{ * }\right) \) , so \( G \) is also surjective.

The next corollary shows that the entire curvature tensor is determined by the Ricci tensor in dimension 3.

Corollary 7.26 (The Curvature Tensor in Dimension 3). On every Riemannian or pseudo-Riemannian manifold \( \left( {M, g}\right) \) of dimension 3, the Weyl tensor is zero, and the Riemann curvature tensor is determined by the Ricci tensor via the formula

\[
{Rm} = P \oslash  g = {Rc} \oslash  g - \frac{1}{4}{Sg} \oslash  g. \tag{7.39}
\]

Proof. Corollary 7.25 shows that \( G : {\sum }^{2}\left( {V}^{ * }\right)  \rightarrow  \mathcal{R}\left( {V}^{ * }\right) \) is an isomorphism in dimension 3. Since \( {\operatorname{tr}}_{g} \circ  G \) is the identity, it follows that \( {\operatorname{tr}}_{g} \) is also an isomorphism. Because \( {\operatorname{tr}}_{g}W \) is always zero by Proposition 7.24, it follows that \( W \) is always zero. Formula (7.39) then follows from the definition of the Weyl tensor.

In dimension 2, the definitions of the Weyl and Schouten tensors do not make sense; but we have the following analogous result instead.

Corollary 7.27 (The Curvature Tensor in Dimension 2). On every Riemannian or pseudo-Riemannian manifold \( \left( {M, g}\right) \) of dimension 2, the Riemann and Ricci tensors are determined by the scalar curvature as follows:

\[
{Rm} = \frac{1}{4}{Sg} \oslash  g,\;{Rc} = \frac{1}{2}{Sg}.
\]

Proof. In dimension 2, it follows from Corollary 7.25(b) that there is some scalar function \( f \) such that \( {Rm} = {fg} \oslash  g \) . Taking traces, we find from Lemma 7.22(d) that \( {Rc} = {\operatorname{tr}}_{g}\left( {Rm}\right)  = {2fg} \) , and then \( S = {\operatorname{tr}}_{g}\left( {Rc}\right)  = {2f}{\operatorname{tr}}_{g}\left( g\right)  = {4f} \) . The results follow by substituting \( f = \frac{1}{4}S \) back into these equations.

Although the traceless Ricci tensor is always zero on a 2-manifold, this does not imply that \( S \) is constant, since the proof of Schur’s lemma fails in dimension 2. Einstein metrics in dimension 2 are simply those with constant scalar curvature.

Returning now to dimensions greater than 2, we can use (7.27) to further decompose the Schouten tensor into a part determined by the traceless Ricci tensor and a purely scalar part. The next proposition is the analogue of Proposition 7.17 for the full curvature tensor.

Proposition 7.28 (The Ricci Decomposition of the Curvature Tensor). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) . Then the \( \left( {0,4}\right) \) -curvature tensor of \( g \) has the following orthogonal decomposition:

\[
{Rm} = W + \frac{1}{n - 2}\overset{ \circ  }{Rc} \oslash  g + \frac{1}{{2n}\left( {n - 1}\right) }{Sg} \oslash  g. \tag{7.40}
\]

Therefore, in the Riemannian case,

\[
{\left| Rm\right| }_{g}^{2} = {\left| W\right| }_{g}^{2} + \frac{1}{{\left( n - 2\right) }^{2}}{\left| \overset{ \circ  }{Rc} \otimes  g\right| }_{g}^{2} + \frac{1}{4{n}^{2}{\left( n - 1\right) }^{2}}{\left| Sg \otimes  g\right| }_{g}^{2} \tag{7.41}
\]

\[
= {\left| W\right| }_{g}^{2} + \frac{4}{n - 2}{\left| \overset{ \circ  }{Rc}\right| }_{g}^{2} + \frac{2}{n\left( {n - 1}\right) }{S}^{2}.
\]

Proof. The decomposition (7.40) follows immediately by substituting (7.27) into the definition of the Weyl tensor and simplifying. The decomposition is orthogonal thanks to Lemma 7.22(e), and (7.41) follows from Lemma 7.22(f).

## Curvatures of Conformally Related Metrics

Recall that two Riemannian or pseudo-Riemannian metrics on the same manifold are said to be conformal to each other if one is a positive function times the other. For example, we have seen that the round metrics and the hyperbolic metrics are all conformal to Euclidean metrics, at least locally.

If \( g \) and \( \widetilde{g} \) are conformal metrics on a smooth manifold \( M \) , there is no reason to expect that the curvature tensors of \( g \) and \( \widetilde{g} \) should be closely related to each other.

But it is a remarkable fact that the Weyl tensor has a very simple transformation law under conformal changes of metric. In this section, we derive that law.

First we need to determine how the Levi-Civita connection changes when a metric is changed conformally. Given conformal metrics \( g \) and \( \widetilde{g} \) , we can always write \( \widetilde{g} = {e}^{2f}g \) for some smooth real-valued function \( f \) .

Proposition 7.29 (Conformal Transformation of the Levi-Civita Connection). Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian n-manifold (with or without boundary), and let \( \widetilde{g} = {e}^{2f}g \) be any metric conformal to \( g \) . If \( \nabla \) and \( \widetilde{\nabla } \) denote the Levi-Civita connections of \( g \) and \( \widetilde{g} \) , respectively, then

\[
{\widetilde{\nabla }}_{X}Y = {\nabla }_{X}Y + \left( {Xf}\right) Y + \left( {Yf}\right) X - \langle X, Y{\rangle }_{g}\operatorname{grad}f, \tag{7.42}
\]

where the gradient on the right-hand side is that of \( g \) . In any local coordinates, the Christoffel symbols of the two connections are related by

\[
{\widetilde{\Gamma }}_{ij}^{k} = {\Gamma }_{ij}^{k} + {f}_{;i}{\delta }_{j}^{k} + {f}_{;j}{\delta }_{i}^{k} - {g}^{kl}{f}_{;l}{g}_{ij}, \tag{7.43}
\]

where \( {f}_{;i} = {\partial }_{i}f \) is the ith component of \( \nabla f = {df} = {f}_{;i}d{x}^{i} \) .

Proof. Formula (7.43) is a straightforward computation using formula (5.10) for the Christoffel symbols in coordinates, and then (7.42) follows by expanding everything in coordinates and using (7.43).

This result leads to transformation laws for the various curvature tensors.

Theorem 7.30 (Conformal Transformation of the Curvature). Let \( g \) be a Riemannian or pseudo-Riemannian metric on an n-manifold \( M \) with or without boundary, \( f \in  {C}^{\infty }\left( M\right) \) , and \( \widetilde{g} = {e}^{2f}g \) . In the Riemannian case, the curvature tensors of \( \widetilde{g} \) (represented with tildes) are related to those of \( g \) by the following formulas:

\[
\widetilde{Rm} = {e}^{2f}\left( {{Rm} - \left( {{\nabla }^{2}f}\right)  \otimes  g + \left( {{df} \otimes  {df}}\right)  \otimes  g - \frac{1}{2}{\left| df\right| }_{g}^{2}\left( {g \otimes  g}\right) }\right) , \tag{7.44}
\]

\[
\widetilde{Rc} = {Rc} - \left( {n - 2}\right) \left( {{\nabla }^{2}f}\right)  + \left( {n - 2}\right) \left( {{df} \otimes  {df}}\right)  - \left( {{\Delta f} + \left( {n - 2}\right) {\left| df\right| }_{g}^{2}}\right) g, \tag{7.45}
\]

\[
\widetilde{S} = {e}^{-{2f}}\left( {S - 2\left( {n - 1}\right) {\Delta f} - \left( {n - 1}\right) \left( {n - 2}\right) {\left| df\right| }_{g}^{2}}\right) , \tag{7.46}
\]

where the curvatures and covariant derivatives on the right are those of \( g \) , and \( {\Delta f} = \operatorname{div}\left( {\operatorname{grad}f}\right) \) is the Laplacian of \( f \) defined in Chapter 2. If in addition \( n \geq  3 \) , then

\[
\widetilde{P} = P - {\nabla }^{2}f + \left( {{df} \otimes  {df}}\right)  - \frac{1}{2}{\left| df\right| }_{g}^{2}g, \tag{7.47}
\]

\[
\widetilde{W} = {e}^{2f}W \tag{7.48}
\]

In the pseudo-Riemannian case, the same formulas hold with each occurrence of \( {\left| df\right| }_{g}^{2} \) replaced by \( \langle {df},{df}{\rangle }_{g}^{2} \) .

Proof. We begin with (7.44). The plan is to choose local coordinates and insert formula (7.43) for the Christoffel symbols into the coordinate formula (7.8) for the coefficients of the curvature tensor. As in the proof of the differential Bianchi identity, we can make the computations much more tractable by computing the components of these tensors at a point \( p \in  M \) in normal coordinates for \( g \) centered at \( p \) , so that the equations \( {g}_{ij} = {\delta }_{ij},{\partial }_{k}{g}_{ij} = 0 \) , and \( {\Gamma }_{ij}^{k} = 0 \) hold at \( p \) . This has the following consequences at \( p \) :

\[
{f}_{;{ij}} = {\partial }_{j}{\partial }_{i}f
\]

\[
{\widetilde{\Gamma }}_{ij}^{k} = {f}_{;i}{\delta }_{j}^{k} + {f}_{;j}{\delta }_{i}^{k} - {g}^{kl}{f}_{;l}{g}_{ij},
\]

\[
{\partial }_{m}{\widetilde{\Gamma }}_{ij}^{k} = {\partial }_{m}{\Gamma }_{ij}^{k} + {f}_{;{im}}{\delta }_{j}^{k} + {f}_{;{jm}}{\delta }_{i}^{k} - {g}^{kl}{f}_{;{lm}}{g}_{ij},
\]

\[
{R}_{ijk}{}^{l} = {\partial }_{i}{\Gamma }_{jk}^{l} - {\partial }_{j}{\Gamma }_{ik}^{l}
\]

Now start with

\[
{\widetilde{R}}_{ijkl} = {e}^{2f}{g}_{lm}\left( {{\partial }_{i}{\widetilde{\Gamma }}_{jk}^{m} - {\partial }_{j}{\widetilde{\Gamma }}_{ik}^{m} + {\widetilde{\Gamma }}_{jk}^{p}{\widetilde{\Gamma }}_{ip}^{m} - {\widetilde{\Gamma }}_{ik}^{p}{\widetilde{\Gamma }}_{jp}^{m}}\right) .
\]

Inserting the relations above and simplifying, we eventually obtain

\[
{\widetilde{R}}_{ijkl} = {e}^{2f}\left( {{R}_{ijkl} - \left( {{f}_{;{il}}{g}_{jk} + {f}_{;{jk}}{g}_{il} - {f}_{;{il}}{g}_{jk} - {f}_{;{jk}}{g}_{il}}\right) }\right.
\]

\[
+ \left( {{f}_{;i}{f}_{;l}{g}_{jk} + {f}_{;j}{f}_{;k}{g}_{il} - {f}_{;i}{f}_{;k}{g}_{jl} - {f}_{;j}{f}_{;l}{g}_{ik}}\right)
\]

\[
\left. {-{g}^{mp}{f}_{;m}{f}_{;p}\left( {{g}_{il}{g}_{jk} - {g}_{ik}{g}_{jl}}\right) }\right) ,
\]

which is the coordinate version of (7.44). (See Problem 5-14 for the formula for the Laplacian in terms of covariant derivatives.) The rest of the formulas follow easily from this, using the identities of Lemma 7.22 and the fact that \( {g}^{ij} = {e}^{-{2f}}{\widetilde{g}}^{ij} \) .

The next corollary begins to explain the geometric significance of the Weyl tensor. Recall that a Riemannian manifold is said to be locally conformally flat if every point has a neighborhood that is conformally equivalent to an open subset of Euclidean space. Similarly, a pseudo-Riemannian manifold is locally conformally flat if every point has a neighborhood conformally equivalent to an open set in a pseudo-Euclidean space.

Corollary 7.31. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) . If \( g \) is locally conformally flat, then its Weyl tensor vanishes identically.

Proof. Suppose \( \left( {M, g}\right) \) is locally conformally flat. Then for each \( p \in  M \) there exist a neighborhood \( U \) and an embedding \( \varphi  : U \rightarrow  {\mathbb{R}}^{n} \) such that \( \varphi \) pulls back a flat (Riemannian or pseudo-Riemannian) metric on \( {\mathbb{R}}^{n} \) to a metric of the form \( \widetilde{g} = \; {e}^{2f}g \) . This implies that \( \widetilde{g} \) has zero Weyl tensor, because its entire curvature tensor is zero. By virtue of (7.48), the Weyl tensor of \( g \) is also zero.

Thus a necessary condition for a smooth manifold of dimension at least 3 to be locally conformally flat is that its Weyl tensor vanish identically. As Theorem 7.37 below will show, in dimensions 4 and higher, this condition is also sufficient. But in 3 dimensions, Corollary 7.26 shows that the Weyl tensor vanishes identically on every manifold, so to understand that case, we must introduce one more tensor field. On a Riemannian or pseudo-Riemannian manifold, the Cotton tensor is defined as the negative of the exterior covariant derivative of the Schouten tensor: \( C =  - {DP} \) . This is the 3-tensor field whose expression in terms of any local frame is

\[
{C}_{ijk} = {P}_{{ij};k} - {P}_{{ik};j}. \tag{7.49}
\]

Proposition 7.32. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) , and let \( W \) and \( C \) denote its Weyl and Cotton tensors, respectively. Then

\[
{\operatorname{tr}}_{g}\left( {\nabla W}\right)  = \left( {n - 3}\right) C \tag{7.50}
\]

where the trace is on the first and last indices of the 5-tensor \( \nabla W \) .

Proof. Writing \( W = {Rm} - P \oslash  g \) and using the component form of the first contracted Bianchi identity (7.32), we obtain

\[
{W}_{ijkl}{;}^{i} = {R}_{{jk};l} - {R}_{{jl};k} - {P}_{il}{;}^{i}{g}_{jk} - {P}_{{jk};}{}^{i}{g}_{il} + {P}_{{ik};}{}^{i}{g}_{jl} + {P}_{{jl};}{}^{i}{g}_{ik}. \tag{7.51}
\]

Note that \( {P}_{{jk};}{}^{i}{g}_{il} = {P}_{{jk};l} \) and \( {P}_{{jl};}{}^{i}{g}_{ik} = {P}_{{jl};k} \) . To simplify the other two terms, we use the definition of the Schouten tensor and the second contracted Bianchi identity (7.33) to obtain that

\[
{P}_{{il};}{}^{i} = \frac{1}{n - 2}\left( {{R}_{{il};}{}^{i} - \frac{{S}^{;i}}{2\left( {n - 1}\right) }{g}_{il}}\right)  = \frac{1}{2\left( {n - 1}\right) }{S}_{;l}.
\]

The analogous formula holds for \( {P}_{ik}{;}^{i} \) . When we insert these expressions into (7.51) and simplify, we find that the terms involving derivatives of the Ricci and scalar curvatures combine to yield

\[
{W}_{{ijkl};}{}^{i} = \left( {n - 2}\right) \left( {{P}_{{jk};l} - {P}_{{jl};k}}\right)  - {P}_{{jk};l} + {P}_{{jl};k} = \left( {n - 3}\right) {C}_{jkl},
\]

which is the component version of (7.50).

Corollary 7.33. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold. If \( \dim M \geq  4 \) and the Weyl tensor vanishes identically, then so does the Cotton tensor:

The next proposition expresses another important feature of the Cotton tensor.

Proposition 7.34 (Conformal Invariance of the Cotton Tensor in Dimension 3). Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian 3-manifold, and \( \widetilde{g} = {e}^{2f}g \) for some \( f \in  {C}^{\infty }\left( M\right) \) . If \( C \) and \( \widetilde{C} \) denote the Cotton tensors of \( g \) and \( \widetilde{g} \) , respectively, then \( \widetilde{C} = C \) .

Proof. Problem 7-10.

Corollary 7.35. If \( \left( {M, g}\right) \) is a locally conformally flat 3-manifold, then the Cotton tensor of \( g \) vanishes identically.

- Exercise 7.36. Prove this corollary.

The real significance of the Weyl and Cotton tensors is explained by the following important theorem.

Theorem 7.37 (Weyl-Schouten). Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold of dimension \( n \geq  3 \) .

(a) If \( n \geq  4 \) , then \( \left( {M, g}\right) \) is locally conformally flat if and only if its Weyl tensor is identically zero.

(b) If \( n = 3 \) , then \( \left( {M, g}\right) \) is locally conformally flat if and only if its Cotton tensor is identically zero.

Proof. The necessity of each condition was proved in Corollaries 7.31 and 7.35. To prove sufficiency, suppose \( \left( {M, g}\right) \) satisfies the hypothesis appropriate to its dimension; then it follows from Corollaries 7.26 and 7.33 that the Weyl and Cotton tensors of \( g \) are both identically zero. Every metric \( \widetilde{g} = {e}^{2f}g \) conformal to \( g \) also has zero Weyl tensor, and therefore its curvature tensor is \( \widetilde{Rm} = \widetilde{P} \cap  \widetilde{g} \) . We will show that in a neighborhood of each point, the function \( f \) can be chosen to make \( \widetilde{P} \equiv  0 \) , which implies that \( \widetilde{Rm} \equiv  0 \) and therefore \( \widetilde{g} \) is flat.

From (7.47), it follows that \( \widetilde{P} \equiv  0 \) if and only if

\[
P - {\nabla }^{2}f + \left( {{df} \otimes  {df}}\right)  - \frac{1}{2}\langle {df},{df}{\rangle }_{g}^{2}g = 0. \tag{7.52}
\]

This equation can be written in the form \( \nabla \left( {df}\right)  = A\left( {df}\right) \) , where \( A \) is the map from 1-tensors to symmetric 2-tensors given by

\[
A\left( \xi \right)  = \left( {\xi  \otimes  \xi }\right)  - \frac{1}{2}\langle \xi ,\xi {\rangle }_{g}^{2}g + P,
\]

or in components,

\[
A{\left( \xi \right) }_{ij} = {\xi }_{i}{\xi }_{j} - \frac{1}{2}{\xi }_{m}{\xi }^{m}{g}_{ij} + {P}_{ij}. \tag{7.53}
\]

We will solve this equation by first looking for a smooth 1-form \( \xi \) that satisfies \( \nabla \xi  = A\left( \xi \right) \) . In any local coordinates, if we write \( \xi  = {\xi }_{j}d{x}^{j} \) , this becomes an overdetermined system of first-order partial differential equations for the \( n \) unknown functions \( {\xi }_{1},\ldots ,{\xi }_{n} \) . (A system of differential equations is said to be overdetermined if there are more equations than unknown functions.) If \( \xi \) is a solution to \( \nabla \xi  = A\left( \xi \right) \) on an open subset of \( M \) , then the Ricci identity (7.21) shows that \( A\left( \xi \right) \) satisfies

\[
A{\left( \xi \right) }_{{ij};k} - A{\left( \xi \right) }_{{ik};j} = {\xi }_{i;{jk}} - {\xi }_{i;{kj}} = {R}_{jki}{}^{l}{\xi }_{l}. \tag{7.54}
\]

Lemma 7.38 below shows that this condition is actually sufficient: more precisely, \( \nabla \xi  = A\left( \xi \right) \) has a smooth solution in a neighborhood of each point, provided that for every smooth covector field \( \xi \) , the covariant derivatives of \( A\left( \xi \right) \) satisfy \( A{\left( \xi \right) }_{{ij};k} - \; A{\left( \xi \right) }_{{ik};j} = {R}_{jki}{}^{l}{\xi }_{l} \) when \( A{\left( \xi \right) }_{ij} \) is substituted for \( {\xi }_{i;j} \) wherever it appears.

To see that this condition is satisfied, differentiate (7.53) to obtain

\[
{A}_{{ij};k} - {A}_{{ik};j}
\]

\[
= {\xi }_{i;k}{\xi }_{j} + {\xi }_{i}{\xi }_{j;k} - {\xi }_{m;k}{\xi }^{m}{g}_{ij} - {\xi }_{i;j}{\xi }_{k} - {\xi }_{i}{\xi }_{k;j} + {\xi }_{m;j}{\xi }^{m}{g}_{ik} + {C}_{ijk}.
\]

Now substitute the right-hand side of (7.53) (with appropriate index substitutions) for \( {\xi }_{i;j} \) wherever it appears, subtract \( {R}_{jki}{}^{l}{\xi }_{l} \) , and use the relation \( {Rm} = W + P \oslash  g \) . After extensive cancellations, we obtain

\[
A{\left( \xi \right) }_{{ij};k} - A{\left( \xi \right) }_{{ik};j} - {R}_{jki}{}^{l}{\xi }_{l} =  - {W}_{jki}{}^{l}{\xi }_{l} + {C}_{ijk}. \tag{7.55}
\]

Our hypotheses guarantee that the right-hand side is identically zero, so there is a solution \( \xi \) to \( \nabla \xi  = A\left( \xi \right) \) in a neighborhood of each point.

Because \( A{\left( \xi \right) }_{ij} \) is symmetric in \( i \) and \( j \) , it follows that the ordinary derivatives \( {\partial }_{j}{\xi }_{i} = {\xi }_{i;j} + {\Gamma }_{ij}^{k}{\xi }_{k} \) are also symmetric, and thus \( \xi \) is a closed 1-form. By the Poincaré lemma, in some (possibly smaller) neighborhood of each point, there is a smooth function \( f \) such that \( \xi  = {df} = \nabla f \) ; this \( f \) is the function we seek.

Here is the lemma that was used in the proof of the preceding theorem.

Lemma 7.38. Let \( \left( {M, g}\right) \) be a Riemannian or pseudo-Riemannian manifold, and consider the overdetermined system of equations

\[
\nabla \xi  = A\left( \xi \right) , \tag{7.56}
\]

where \( A : {T}^{ * }M \rightarrow  {T}^{2}{T}^{ * }M \) is a smooth map satisfying the following compatibility condition: for any smooth covector field \( \xi \) , the 3-tensor field \( \nabla \left( {A\left( \xi \right) }\right) \) satisfies the following identity when \( A\left( \xi \right) \) is substituted for \( \nabla \xi \) wherever it appears:

\[
A{\left( \xi \right) }_{{ij};k} - A{\left( \xi \right) }_{{ik};j} = {R}_{jki}{}^{l}{\xi }_{l}. \tag{7.57}
\]

Then for every \( p \in  M \) and every covector \( {\eta }_{0} \in  {T}_{p}^{ * }M \) , there is a smooth solution to (7.56) on a neighborhood of \( p \) satisfying \( {\xi }_{p} = {\eta }_{0} \) .

Proof. Let \( p \in  M \) be given. In smooth local coordinates \( \left( {x}^{i}\right) \) on a neighborhood of \( p,\left( {7.56}\right) \) is equivalent to the overdetermined system

\[
\frac{\partial {\xi }_{i}\left( x\right) }{\partial {x}^{j}} = {a}_{ij}\left( {x,\xi \left( x\right) }\right) ,
\]

where

\[
{a}_{ij}\left( {x,\xi }\right)  = {\Gamma }_{ij}^{k}\left( x\right) {\xi }_{k} + A{\left( \xi \right) }_{ij}.
\]

An application of the Frobenius theorem [LeeSM, Prop. 19.29] shows that there is a smooth solution to this overdetermined system in a neighborhood of \( p \) with \( {\xi }_{p} \) arbitrary, provided that

\[
\frac{\partial {a}_{ij}}{\partial {x}^{k}} + {a}_{kl}\frac{\partial {a}_{ij}}{\partial {\xi }_{l}} = \frac{\partial {a}_{ik}}{\partial {x}^{j}} + {a}_{jl}\frac{\partial {a}_{ik}}{\partial {\xi }_{l}}. \tag{7.58}
\]

By virtue of the chain rule, this identity means exactly that the first derivatives \( \partial \left( {{a}_{ij}\left( {x,\xi \left( x\right) }\right) }\right) /\partial {x}^{k} \) , after substituting \( {a}_{kl}\left( {x,\xi \left( x\right) }\right) \) in place of \( \partial {\xi }_{k}\left( x\right) /\partial {x}^{l} \) , are symmetric in the indices \( j, k \) . Because \( {\xi }_{k;l} = {\partial }_{l}{\xi }_{k} - {\Gamma }_{kl}^{m}{\xi }_{m} \) , this substitution is equivalent to substituting \( A{\left( \xi \right) }_{kl} \) for \( {\xi }_{k;l} \) wherever it occurs. After expanding the hypothesis (7.57) in terms of Christoffel symbols, we find after some manipulation that it reduces to (7.58).

Because all Riemannian 1-manifolds are flat, the only nontrivial case that is not addressed by the Weyl-Schouten theorem is that of dimension 2. Smooth coordinates that provide a conformal equivalence between an open subset of a Riemannian or pseudo-Riemannian 2-manifold and an open subset of \( {\mathbb{R}}^{2} \) are called isothermal coordinates, and it is a fact that such coordinates always exist locally. For the Riemannian case, there are various proofs available, all of which involve more machinery from partial differential equations and complex analysis than we have at our disposal; see [Che55] for a reasonably elementary proof. For the pseudo-Riemannian 2-manifold case, see Problem 7-15. Thus every Riemannian or pseudo-Riemannian 2-manifold is locally conformally flat.

## Problems

7-1. Complete the proof of Proposition 7.3 by showing that \( R\left( {X, Y}\right) \left( {fZ}\right)  = \; {fR}\left( {X, Y}\right) Z \) for all smooth vector fields \( X, Y, Z \) and smooth real-valued functions \( f \) .

7-2. Prove Proposition 7.4 (the formula for the curvature tensor in coordinates).

7-3. Show that the curvature tensor of a Riemannian locally symmetric space is parallel: \( \nabla {Rm} \equiv  0 \) . (Used on pp. 297, 351.)

7-4. Let \( M \) be a Riemannian or pseudo-Riemannian manifold, and let \( \left( {x}^{i}\right) \) be normal coordinates centered at \( p \in  M \) . Show that the following holds at \( p \) :

\[
{R}_{ijkl} = \frac{1}{2}\left( {{\partial }_{j}{\partial }_{l}{g}_{ik} + {\partial }_{i}{\partial }_{k}{g}_{jl} - {\partial }_{i}{\partial }_{l}{g}_{jk} - {\partial }_{j}{\partial }_{k}{g}_{il}}\right) .
\]

7-5. Let \( \nabla \) be the Levi-Civita connection on a Riemannian or pseudo-Riemannian manifold \( \left( {M, g}\right) \) , and let \( {\omega }_{i}{}^{j} \) be its connection 1-forms with respect to a local frame \( \left( {E}_{i}\right) \) (Problem 4-14). Define a matrix of 2-forms \( {\Omega }_{i}{}^{j} \) , called the curvature 2-forms, by

\[
{\Omega }_{i}{}^{j} = \frac{1}{2}{R}_{kli}{}^{j}{\varepsilon }^{k} \land  {\varepsilon }^{l},
\]

where \( \left( {\varepsilon }^{i}\right) \) is the coframe dual to \( \left( {E}_{i}\right) \) . Show that the curvature 2-forms satisfy Cartan's second structure equation:

\[
{\Omega }_{i}{}^{j} = d{\omega }_{i}{}^{j} - {\omega }_{i}{}^{k} \land  {\omega }_{k}{}^{j}.
\]

[Hint: Expand \( R\left( {{E}_{k},{E}_{l}}\right) {E}_{i} \) in terms of \( \nabla \) and \( {\omega }_{i}{}^{j} \) .]

7-6. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are Riemannian manifolds, and \( {M}_{1} \times  {M}_{2} \) is endowed with the product metric \( g = {g}_{1} \oplus  {g}_{2} \) as in (2.12). Show that the Riemann curvature, Ricci curvature, and scalar curvature of \( g \) are given by the following formulas:

\[
{Rm} = {\pi }_{1}^{ * }R{m}_{1} + {\pi }_{2}^{ * }R{m}_{2}
\]

\[
{Rc} = {\pi }_{1}^{ * }R{c}_{1} + {\pi }_{2}^{ * }R{c}_{2}
\]

\[
S = {\pi }_{1}^{ * }{S}_{1} + {\pi }_{1}^{ * }{S}_{2}
\]

where \( R{m}_{i}, R{c}_{i} \) , and \( {S}_{i} \) are the Riemann, Ricci, and scalar curvatures of \( \left( {{M}_{i},{g}_{i}}\right) \) , and \( {\pi }_{i} : {M}_{1} \times  {M}_{2} \rightarrow  {M}_{i} \) is the projection. (Used on pp. 257,261.)

7-7. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( u \in  {C}^{\infty }\left( M\right) \) . Use (5.29) and (7.21) to prove Bochner's formula:

\[
\Delta \left( {\frac{1}{2}{\left| \operatorname{grad}u\right| }^{2}}\right)  = {\left| {\nabla }^{2}u\right| }^{2} + \langle \operatorname{grad}\left( {\Delta u}\right) ,\operatorname{grad}u\rangle  + {Rc}\left( {\operatorname{grad}u,\operatorname{grad}u}\right) .
\]

7-8. LICHNEROWICZ’S THEOREM: Suppose \( \left( {M, g}\right) \) is a compact Riemannian \( n \) -manifold, and there is a positive constant \( \kappa \) such that the Ricci tensor of \( g \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \kappa {\left| v\right| }^{2} \) for all tangent vectors \( v \) . If \( \lambda \) is any positive eigenvalue of \( M \) , then \( \lambda  \geq  {n\kappa }/\left( {n - 1}\right) \) . [Hint: Use Probs. 2-23(c),5-15, and 7-7.]

7-9. Prove parts (e) and (f) of Lemma 7.22 (properties of the Kulkarni-Nomizu product).

7-10. Prove Proposition 7.34 (conformal invariance of the Cotton tensor in dimension 3).

7-11. Let \( \left( {M, g}\right) \) be a Riemannian manifold of dimension \( n > 2 \) . Define the conformal Laplacian \( L : {C}^{\infty }\left( M\right)  \rightarrow  {C}^{\infty }\left( M\right) \) by the formula

\[
{Lu} =  - \frac{4\left( {n - 1}\right) }{\left( n - 2\right) }{\Delta u} + {Su},
\]

where \( \Delta \) is the Laplace-Beltrami operator of \( g \) and \( S \) is its scalar curvature. Prove that if \( \widetilde{g} = {e}^{2f}g \) for some \( f \in  {C}^{\infty }\left( M\right) \) , and \( \widetilde{L} \) denotes the conformal Laplacian with respect to \( \widetilde{g} \) , then for every \( u \in  {C}^{\infty }\left( M\right) \) ,

\[
{e}^{\frac{n + 2}{2}f}\widetilde{L}u = L\left( {{e}^{\frac{n - 2}{2}f}u}\right) .
\]

Conclude that a metric \( \widetilde{g} \) conformal to \( g \) has constant scalar curvature \( \lambda \) if and only if it can be expressed in the form \( \widetilde{g} = {\varphi }^{4/\left( {n - 2}\right) }g \) , where \( \varphi \) is a smooth positive solution to the Yamabe equation:

\[
{L\varphi } = \lambda {\varphi }^{\frac{n + 2}{n - 2}}. \tag{7.59}
\]

7-12. Let \( M \) be a smooth manifold and let \( \nabla \) be any connection on \( {TM} \) . We can define the curvature endomorphism of \( \nabla \) by the same formula as in the Riemannian case: \( R\left( {X, Y}\right) Z = {\nabla }_{X}{\nabla }_{Y}Z - {\nabla }_{Y}{\nabla }_{X}Z - {\nabla }_{\left\lbrack  X, Y\right\rbrack  }Z \) . Then \( \nabla \) is said to be a flat connection if \( R\left( {X, Y}\right) Z \equiv  0 \) . Prove that the following are equivalent:

(a) \( \nabla \) is flat.

(b) For every point \( p \in  M \) , there exists a parallel local frame defined on a neighborhood of \( p \) .

(c) For all \( p, q \in  M \) , parallel transport along an admissible curve segment \( \gamma \) from \( p \) to \( q \) depends only on the path-homotopy class of \( \gamma \) .

(d) Parallel transport around any sufficiently small closed curve is the identity; that is, for every \( p \in  M \) , there exists a neighborhood \( U \) of \( p \) such that if \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  U \) is an admissible curve in \( U \) starting and ending at \( p \) , then \( {P}_{ab} : {T}_{p}M \rightarrow  {T}_{p}M \) is the identity map.

7-13. Let \( G \) be a Lie group with a bi-invariant metric \( g \) . Show that the following formula holds whenever \( X, Y, Z \) are left-invariant vector fields on \( G \) :

\[
R\left( {X, Y}\right) Z = \frac{1}{4}\left\lbrack  {Z,\left\lbrack  {X, Y}\right\rbrack  }\right\rbrack
\]

(See Problem 5-8.)

7-14. Suppose \( \pi  : \left( {\widetilde{M},\widetilde{g}}\right)  \rightarrow  \left( {M, g}\right) \) is a Riemannian submersion. Using the notation and results of Problem 5-6, prove O'Neill's formula:

\[
{Rm}\left( {W, X, Y, Z}\right)  \circ  \pi  = \widetilde{Rm}\left( {\widetilde{W},\widetilde{X},\widetilde{Y},\widetilde{Z}}\right)  - \frac{1}{2}\left\langle  {{\left\lbrack  \widetilde{W},\widetilde{X}\right\rbrack  }^{V},{\left\lbrack  \widetilde{Y},\widetilde{Z}\right\rbrack  }^{V}}\right\rangle
\]

\[
- \frac{1}{4}\left\langle  {{\left\lbrack  \widetilde{W},\widetilde{Y}\right\rbrack  }^{V},{\left\lbrack  \widetilde{X},\widetilde{Z}\right\rbrack  }^{V}}\right\rangle   + \frac{1}{4}\left\langle  {{\left\lbrack  \widetilde{W},\widetilde{Z}\right\rbrack  }^{V},{\left\lbrack  \widetilde{X},\widetilde{Y}\right\rbrack  }^{V}}\right\rangle  .
\]

(Used on p. 258.)

7-15. Suppose \( \left( {M, g}\right) \) is a 2-dimensional pseudo-Riemannian manifold of signature \( \left( {1,1}\right) \) , and \( p \in  M \) .

(a) Show that there is a smooth local frame \( \left( {{E}_{1},{E}_{2}}\right) \) in a neighborhood of \( p \) such that \( g\left( {{E}_{1},{E}_{1}}\right)  = g\left( {{E}_{2},{E}_{2}}\right)  = 0 \) .

(b) Show that there are smooth coordinates \( \left( {x, y}\right) \) in a neighborhood of \( p \) such that \( {\left( dx\right) }^{2} - {\left( dy\right) }^{2} = {fg} \) for some smooth, positive real-valued function \( f \) . [Hint: Use Prop. A.45 to show that there exist coordinates \( \left( {t, u}\right) \) in which \( {E}_{1} = \partial /\partial t \) , and coordinates \( \left( {v, w}\right) \) in which \( {E}_{2} = \partial /\partial v \) , and set \( x = u + w, y = u - w \) .]

(c) Show that \( \left( {M, g}\right) \) is locally conformally flat.
