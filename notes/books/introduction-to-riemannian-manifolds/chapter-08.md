## Chapter 8 Riemannian Submanifolds

This chapter has a dual purpose: first to apply the theory of curvature to Riemannian submanifolds, and then to use these concepts to derive a precise quantitative interpretation of the curvature tensor.

After introducing some basic definitions and terminology concerning Riemannian submanifolds, we define a vector-valued bilinear form called the second fundamental form, which measures the way a submanifold curves within the ambient manifold. We then prove the fundamental relationships between the intrinsic and extrinsic geometries of a submanifold, including the Gauss formula, which relates the Riemannian connection on the submanifold to that of the ambient manifold, and the Gauss equation, which relates their curvatures. We then show how the second fundamental form measures the extrinsic curvature of submanifold geodesics.

Using these tools, we focus on the special case of hypersurfaces, and use the second fundamental form to define some real-valued curvature quantities called the principal curvatures, mean curvature, and Gaussian curvature. Specializing even more to hypersurfaces in Euclidean space, we describe various concrete geometric interpretations of these quantities. Then we prove Gauss's Theorema Egregium, which shows that the Gaussian curvature of a surface in \( {\mathbb{R}}^{3} \) can be computed intrinsically from the curvature tensor of the induced metric.

In the last section, we introduce the promised quantitative geometric interpretation of the curvature tensor. It allows us to compute sectional curvatures, which are just the Gaussian curvatures of 2-dimensional submanifolds swept out by geodesics tangent to 2-planes in the tangent space. Finally, we compute the sectional curvatures of our frame-homogeneous model Riemannian manifolds—Euclidean spaces, spheres, and hyperbolic spaces.

## The Second Fundamental Form

Suppose \( \left( {M, g}\right) \) is a Riemannian submanifold of a Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . Recall that this means that \( M \) is a submanifold of \( \widetilde{M} \) endowed with the induced metric \( g = {\iota }_{M}^{ * }\widetilde{g} \) (where \( {\iota }_{M} : M \hookrightarrow  \widetilde{M} \) is the inclusion map). Our goal in this chapter is to study the relationship between the geometry of \( M \) and that of \( \widetilde{M} \) .

Although we focus our attention in this chapter on embedded submanifolds for simplicity, the results we present are all local, so they apply in much greater generality. In particular, if \( M \subseteq  \widetilde{M} \) is an immersed submanifold, then every point of \( M \) has a neighborhood in \( M \) that is embedded in \( \widetilde{M} \) , so the results of this chapter can be applied by restricting to such a neighborhood. Even more generally, if \( \left( {M, g}\right) \) is any Riemannian manifold and \( F : M \rightarrow  \widetilde{M} \) is an isometric immersion (meaning that \( {F}^{ * }\widetilde{g} = g \) ), then again every point \( p \in  M \) has a neighborhood \( U \subseteq  M \) such that \( {\left. F\right| }_{U} \) is an embedding, so the results apply to \( F\left( U\right)  \subseteq  M \) . We leave it to the reader to sort out the minor modifications in notation and terminology needed to handle these more general situations.

The results in the first section of this chapter apply virtually without modification to Riemannian submanifolds of pseudo-Riemannian manifolds (ones on which the induced metric is positive definite), so we state most of our theorems in that case. Recall that when the ambient metric \( \widetilde{g} \) is indefinite, this includes the assumption that the induced metric \( g = {\iota }_{M}^{ * }\widetilde{g} \) is positive definite. Some of the results can also be extended to pseudo-Riemannian submanifolds of mixed signature, but there are various pitfalls to watch out for in that case; so for simplicity we restrict to the case of Riemannian submanifolds. See [dC92] for a thorough treatment of pseudo-Riemannian submanifolds.

Also, most of these results can be adapted to manifolds and submanifolds with boundary, simply by embedding everything in slightly larger manifolds without boundary, but one might need to be careful about the statements of some of the results when the submanifold intersects the boundary. Since the interaction of sub-manifolds with boundaries is not our primary concern here, for simplicity we state all of these results in the case of empty boundary only.

Throughout this chapter, therefore, we assume that \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian or pseudo-Riemannian manifold of dimension \( m \) , and \( \left( {M, g}\right) \) is an embedded \( n \) - dimensional Riemannian submanifold of \( \widetilde{M} \) . We call \( \widetilde{M} \) the ambient manifold. We will denote covariant derivatives and curvatures associated with \( \left( {M, g}\right) \) in the usual way \( \left( {\nabla , R,{Rm}\text{ , etc. }}\right) \) , and write those associated with \( \left( {\widetilde{M},\widetilde{g}}\right) \) with tildes \( (\widetilde{\nabla },\widetilde{R},\widetilde{Rm} \) , etc.). We can unambiguously use the inner product notation \( \langle v, w\rangle \) to refer either to \( g \) or to \( \widetilde{g} \) , since \( g \) is just the restriction of \( \widetilde{g} \) to pairs of vectors in \( {TM} \) .

Our first main task is to compare the Levi-Civita connection of \( M \) with that of \( \widetilde{M} \) . The starting point for doing so is the orthogonal decomposition of sections of the ambient tangent bundle \( {\left. T\widetilde{M}\right| }_{M} \) into tangential and orthogonal components. Just as we did for submanifolds of \( {\mathbb{R}}^{n} \) in Chapter 4, we define orthogonal projection maps called tangential and normal projections:

\[
{\pi }^{\top } : {\left. T\widetilde{M}\right| }_{M} \rightarrow  {TM}
\]

\[
{\pi }^{ \bot  } : {\left. T\widetilde{M}\right| }_{M} \rightarrow  {NM}
\]

In terms of an adapted orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) for \( M \) in \( \widetilde{M} \) , these are just the usual projections onto \( \operatorname{span}\left( {{E}_{1},\ldots ,{E}_{n}}\right) \) and \( \operatorname{span}\left( {{E}_{n + 1},\ldots ,{E}_{m}}\right) \) respectively, so both projections are smooth bundle homomorphisms (i.e., they are linear on fibers and map smooth sections to smooth sections). If \( X \) is a section of \( {\left. T\widetilde{M}\right| }_{M} \) , we often use the shorthand notations \( {X}^{\top } = {\pi }^{\top }X \) and \( {X}^{ \bot  } = {\pi }^{ \bot  }X \) for its tangential and normal projections.

![bo_d7dtff491nqc73eq8m7g_237_260_186_1013_422_0.jpg](images/bo_d7dtff491nqc73eq8m7g_237_260_186_1013_422_0.jpg)

Fig. 8.1: The second fundamental form

If \( X, Y \) are vector fields in \( \mathfrak{X}\left( M\right) \) , we can extend them to vector fields on an open subset of \( \widetilde{M} \) (still denoted by \( X \) and \( Y \) ), apply the ambient covariant derivative operator \( \widetilde{\nabla } \) , and then decompose at points of \( M \) to get

\[
{\widetilde{\nabla }}_{X}Y = {\left( {\widetilde{\nabla }}_{X}Y\right) }^{\top } + {\left( {\widetilde{\nabla }}_{X}Y\right) }^{ \bot  }. \tag{8.1}
\]

We wish to interpret the two terms on the right-hand side of this decomposition.

Let us focus first on the normal component. We define the second fundamental form of \( M \) to be the map II: \( \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \Gamma \left( {NM}\right) \) (read "two") given by

\[
\mathrm{{II}}\left( {X, Y}\right)  = {\left( {\widetilde{\nabla }}_{X}Y\right) }^{ \bot  },
\]

where \( X \) and \( Y \) are extended arbitrarily to an open subset of \( \widetilde{M} \) (Fig. 8.1). Since \( {\pi }^{ \bot  } \) maps smooth sections to smooth sections, \( \Pi \left( {X, Y}\right) \) is a smooth section of \( {NM} \) .

The term first fundamental form, by the way, was originally used to refer to the induced metric \( g \) on \( M \) . Although that usage has mostly been replaced by more descriptive terminology, we seem unfortunately to be stuck with the name "second fundamental form." The word "form" in both cases refers to bilinear form, not differential form.

Proposition 8.1 (Properties of the Second Fundamental Form). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , and let \( X, Y \in  \mathfrak{X}\left( M\right) \) .

(a) II \( \left( {X, Y}\right) \) is independent of the extensions of \( X \) and \( Y \) to an open subset of \( \widetilde{M} \) .

(b) II \( \left( {X, Y}\right) \) is bilinear over \( {C}^{\infty }\left( M\right) \) in \( X \) and \( Y \) .

(c) II \( \left( {X, Y}\right) \) is symmetric in \( X \) and \( Y \) .

(d) The value of \( \mathrm{{II}}\left( {X, Y}\right) \) at a point \( p \in  M \) depends only on \( {X}_{p} \) and \( {Y}_{p} \) .

Proof. Choose particular extensions of \( X \) and \( Y \) to a neighborhood of \( M \) in \( \widetilde{M} \) , and for simplicity denote the extended vector fields also by \( X \) and \( Y \) . We begin by proving that \( \coprod  \left( {X, Y}\right) \) is symmetric in \( X \) and \( Y \) when defined in terms of these extensions. The symmetry of the connection \( \widetilde{\nabla } \) implies

\[
\mathrm{{II}}\left( {X, Y}\right)  - \mathrm{{II}}\left( {Y, X}\right)  = {\left( {\widetilde{\nabla }}_{X}Y - {\widetilde{\nabla }}_{Y}X\right) }^{ \bot  } = {\left\lbrack  X, Y\right\rbrack  }^{ \bot  }.
\]

Since \( X \) and \( Y \) are tangent to \( M \) at all points of \( M \) , so is their Lie bracket (Cor. A.40). Therefore \( {\left\lbrack  X, Y\right\rbrack  }^{ \bot  } = 0 \) , so II is symmetric.

Because \( {\left. {\widetilde{\nabla }}_{X}Y\right| }_{p} \) depends only on \( {X}_{p} \) , it follows that the value of \( \Pi \left( {X, Y}\right) \) at \( p \) depends only on \( {X}_{p} \) , and in particular is independent of the extension chosen for \( X \) . Because \( {\widetilde{\nabla }}_{X}Y \) is linear over \( {C}^{\infty }\left( \widetilde{M}\right) \) in \( X \) , and every \( f \in  {C}^{\infty }\left( M\right) \) can be extended to a smooth function on a neighborhood of \( M \) in \( \widetilde{M} \) , it follows that \( \coprod  \left( {X, Y}\right) \) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) . By symmetry, the same claims hold for \( Y \) .

As a consequence of the preceding proposition, for every \( p \in  M \) and all vectors \( v, w \in  {T}_{p}M \) , it makes sense to interpret \( \mathrm{{II}}\left( {v, w}\right) \) as the value of \( \mathrm{{II}}\left( {V, W}\right) \) at \( p \) , where \( V \) and \( W \) are any vector fields on \( M \) such that \( {V}_{p} = v \) and \( {W}_{p} = W \) , and we will do so from now on without further comment.

We have not yet identified the tangential term in the decomposition of \( {\widetilde{\nabla }}_{X}Y \) . Proposition 5.12(b) showed that in the special case of a submanifold of a Euclidean or pseudo-Euclidean space, it is none other than the covariant derivative with respect to the Levi-Civita connection of the induced metric on \( M \) . The following theorem shows that the same is true in the general case. Therefore, we can interpret the second fundamental form as a measure of the difference between the intrinsic Levi-Civita connection on \( M \) and the ambient Levi-Civita connection on \( \widetilde{M} \) .

Theorem 8.2 (The Gauss Formula). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . If \( X, Y \in \; \mathcal{K}\left( M\right) \) are extended arbitrarily to smooth vector fields on a neighborhood of \( M \) in \( \widetilde{M} \) , the following formula holds along \( M \) :

\[
{\widetilde{\nabla }}_{X}Y = {\nabla }_{X}Y + \mathrm{{II}}\left( {X, Y}\right) .
\]

Proof. Because of the decomposition (8.1) and the definition of the second fundamental form, it suffices to show that \( {\left( {\widetilde{\nabla }}_{X}Y\right) }^{\top } = {\nabla }_{X}Y \) at all points of \( M \) .

Define a map \( {\nabla }^{\top } : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) by

\[
{\nabla }_{X}^{\top }Y = {\left( {\widetilde{\nabla }}_{X}Y\right) }^{\top },
\]

where \( X \) and \( Y \) are extended arbitrarily to an open subset of \( \widetilde{M} \) . We examined a special case of this construction, in which \( \widetilde{g} \) is a Euclidean or pseudo-Euclidean metric, in Example 4.9. It follows exactly as in that example that \( {\nabla }^{\top } \) is a connection on \( M \) , and exactly as in the proofs of Propositions 5.8 and 5.9 that it is symmetric and compatible with \( g \) . The uniqueness of the Riemannian connection on \( M \) then shows that \( {\nabla }^{\top } = \nabla \) .

The Gauss formula can also be used to compare intrinsic and extrinsic covariant derivatives along curves. If \( \gamma  : I \rightarrow  M \) is a smooth curve and \( X \) is a vector field along \( \gamma \) that is everywhere tangent to \( M \) , then we can regard \( X \) as either a vector field along \( \gamma \) in \( \widetilde{M} \) or a vector field along \( \gamma \) in \( M \) . We let \( {\widetilde{D}}_{t}X \) and \( {D}_{t}X \) denote its covariant derivatives along \( \gamma \) as a curve in \( \widetilde{M} \) and as a curve in \( M \) , respectively. The next corollary shows how the two covariant derivatives are related.

Corollary 8.3 (The Gauss Formula Along a Curve). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , and \( \gamma  : I \rightarrow  M \) is a smooth curve. If \( X \) is a smooth vector field along \( \gamma \) that is everywhere tangent to \( M \) , then

\[
{\widetilde{D}}_{t}X = {D}_{t}X + \Pi \left( {{\gamma }^{\prime }, X}\right) . \tag{8.2}
\]

Proof. For each \( {t}_{0} \in  I \) , we can find an adapted orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) in a neighborhood of \( \gamma \left( {t}_{0}\right) \) . (Recall that our default assumption is that \( \dim \widetilde{M} = m \) and \( \dim M = n \) .) In terms of this frame, \( X \) can be written \( X\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{X}^{i}\left( t\right) {\left. {E}_{i}\right| }_{\gamma \left( t\right) } \) . Applying the product rule and the Gauss formula, and using the fact that each vector field \( {E}_{i} \) is extendible, we get

\[
{\widetilde{D}}_{t}X = \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\dot{X}}^{i}{E}_{i} + {X}^{i}{\widetilde{\nabla }}_{{\gamma }^{\prime }}{E}_{i}}\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{n}\left( {{\dot{X}}^{i}{E}_{i} + {X}^{i}{\nabla }_{{\gamma }^{\prime }}{E}_{i} + {X}^{i}\mathrm{{II}}\left( {{\gamma }^{\prime },{E}_{i}}\right) }\right)
\]

\[
= {D}_{t}X + \mathrm{{II}}\left( {{\gamma }^{\prime }, X}\right) .
\]

Although the second fundamental form is defined in terms of covariant derivatives of vector fields tangent to \( M \) , it can also be used to evaluate extrinsic covariant derivatives of normal vector fields, as the following proposition shows. To express it concisely, we introduce one more notation. For each normal vector field \( N \in  \Gamma \left( {NM}\right) \) , we obtain a scalar-valued symmetric bilinear form \( {\mathrm{{II}}}_{N} : \mathfrak{X}\left( M\right)  \times \; \mathfrak{X}\left( M\right)  \rightarrow  {C}^{\infty }\left( M\right) \) by

\[
{\mathrm{{II}}}_{N}\left( {X, Y}\right)  = \langle N,\mathrm{{II}}\left( {X, Y}\right) \rangle . \tag{8.3}
\]

Let \( {W}_{N} : \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) denote the self-adjoint linear map associated with this bilinear form, characterized by

\[
\left\langle  {{W}_{N}\left( X\right) , Y}\right\rangle   = {\mathrm{{II}}}_{N}\left( {X, Y}\right)  = \langle N,\mathrm{{II}}\left( {X, Y}\right) \rangle . \tag{8.4}
\]

The map \( {W}_{N} \) is called the Weingarten map in the direction of \( N \) . Because the second fundamental form is bilinear over \( {C}^{\infty }\left( M\right) \) , it follows that \( {W}_{N} \) is linear over \( {C}^{\infty }\left( M\right) \) and thus defines a smooth bundle homomorphism from \( {TM} \) to itself.

Proposition 8.4 (The Weingarten Equation). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . For every \( X \in  \mathfrak{X}\left( M\right) \) and \( N \in  \Gamma \left( {NM}\right) \) , the following equation holds:

\[
{\left( {\widetilde{\nabla }}_{X}N\right) }^{\top } =  - {W}_{N}\left( X\right) \tag{8.5}
\]

when \( N \) is extended arbitrarily to an open subset of \( \widetilde{M} \) .

Proof. Note that at points of \( M \) , the covariant derivative \( {\widetilde{\nabla }}_{X}N \) is independent of the choice of extensions of \( X \) and \( N \) by Proposition 4.26. Let \( Y \in  \mathfrak{X}\left( M\right) \) be arbitrary, extended to a vector field on an open subset of \( \widetilde{M} \) . Since \( \langle N, Y\rangle \) vanishes identically along \( M \) and \( X \) is tangent to \( M \) , the following holds at points of \( M \) :

\[
0 = X\langle N, Y\rangle
\]

\[
= \left\langle  {{\widetilde{\nabla }}_{X}N, Y}\right\rangle   + \left\langle  {N,{\widetilde{\nabla }}_{X}Y}\right\rangle
\]

\[
= \left\langle  {{\widetilde{\nabla }}_{X}N, Y}\right\rangle   + \left\langle  {N,{\nabla }_{X}Y + \mathrm{{II}}\left( {X, Y}\right) }\right\rangle
\]

\[
= \left\langle  {{\widetilde{\nabla }}_{X}N, Y}\right\rangle   + \langle N,\mathrm{{II}}\left( {X, Y}\right) \rangle
\]

\[
= \left\langle  {{\widetilde{\nabla }}_{X}N, Y}\right\rangle   + \left\langle  {{W}_{N}\left( X\right) , Y}\right\rangle  .
\]

Since \( Y \) was an arbitrary vector field tangent to \( M \) , this implies

\[
0 = {\left( {\widetilde{\nabla }}_{X}N + {W}_{N}\left( X\right) \right) }^{\top } = {\left( {\widetilde{\nabla }}_{X}N\right) }^{\top } + {W}_{N}\left( X\right) ,
\]

which is equivalent to (8.5).

In addition to describing the difference between the intrinsic and extrinsic connections, the second fundamental form plays an even more important role in describing the difference between the curvature tensors of \( \widetilde{M} \) and \( M \) . The explicit formula, also due to Gauss, is given in the following theorem.

Theorem 8.5 (The Gauss Equation). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . For all \( W, X, Y, Z \in  \mathfrak{X}\left( M\right) \) , the following equation holds:

\[
\widetilde{Rm}\left( {W, X, Y, Z}\right)  = {Rm}\left( {W, X, Y, Z}\right)  - \langle \mathrm{{II}}\left( {W, Z}\right) ,\mathrm{{II}}\left( {X, Y}\right) \rangle  + \langle \mathrm{{II}}\left( {W, Y}\right) ,\mathrm{{II}}\left( {X, Z}\right) \rangle .
\]

Proof. Let \( W, X, Y, Z \) be extended arbitrarily to an open subset of \( \widetilde{M} \) . At points of \( M \) , using the definition of the curvature and the Gauss formula, we get

\[
\widetilde{Rm}\left( {W, X, Y, Z}\right)  = \left\langle  {{\widetilde{\nabla }}_{W}{\widetilde{\nabla }}_{X}Y - {\widetilde{\nabla }}_{X}{\widetilde{\nabla }}_{W}Y - {\widetilde{\nabla }}_{\left\lbrack  W, X\right\rbrack  }Y, Z}\right\rangle
\]

\[
= \left\langle  {{\widetilde{\nabla }}_{W}\left( {{\nabla }_{X}Y + \mathrm{{II}}\left( {X, Y}\right) }\right)  - {\widetilde{\nabla }}_{X}\left( {{\nabla }_{W}Y + \mathrm{{II}}\left( {W, Y}\right) }\right) }\right.
\]

\[
\left. {-{\widetilde{\nabla }}_{\left\lbrack  W, X\right\rbrack  }Y, Z}\right\rangle
\]

Apply the Weingarten equation to each of the terms involving II (with \( \mathrm{{II}}\left( {X, Y}\right) \) or \( \mathrm{{II}}\left( {W, Y}\right) \) playing the role of \( N \) ) to get

\[
\widetilde{Rm}\left( {W, X, Y, Z}\right)  = \left\langle  {{\widetilde{\nabla }}_{W}{\nabla }_{X}Y, Z}\right\rangle   - \langle \mathrm{{II}}\left( {X, Y}\right) ,\mathrm{{II}}\left( {W, Z}\right) \rangle
\]

\[
- \left\langle  {{\widetilde{\nabla }}_{X}{\nabla }_{W}Y, Z}\right\rangle   + \langle \mathrm{{II}}\left( {W, Y}\right) ,\mathrm{{II}}\left( {X, Z}\right) \rangle  - \left\langle  {{\widetilde{\nabla }}_{\left\lbrack  W, X\right\rbrack  }Y, Z}\right\rangle  .
\]

Decomposing each term involving \( \widetilde{\nabla } \) into its tangential and normal components, we see that only the tangential component survives, because \( Z \) is tangent to \( M \) . The Gauss formula allows each such term to be rewritten in terms of \( \nabla \) , giving

\[
\widetilde{Rm}\left( {W, X, Y, Z}\right)  = \left\langle  {{\nabla }_{W}{\nabla }_{X}Y, Z}\right\rangle   - \left\langle  {{\nabla }_{X}{\nabla }_{W}Y, Z}\right\rangle   - \left\langle  {{\nabla }_{\left\lbrack  W, X\right\rbrack  }Y, Z}\right\rangle
\]

\[
- \langle \mathrm{{II}}\left( {X, Y}\right) ,\mathrm{{II}}\left( {W, Z}\right) \rangle  + \langle \mathrm{{II}}\left( {W, Y}\right) ,\mathrm{{II}}\left( {X, Z}\right) \rangle
\]

\[
= \langle R\left( {W, X}\right) Y, Z\rangle
\]

\[
- \langle \mathrm{{II}}\left( {X, Y}\right) ,\mathrm{{II}}\left( {W, Z}\right) \rangle  + \langle \mathrm{{II}}\left( {W, Y}\right) ,\mathrm{{II}}\left( {X, Z}\right) \rangle .
\]

There is one other fundamental submanifold equation, which relates the normal part of the ambient curvature endomorphism to derivatives of the second fundamental form. We will not have need for it, but we include it here for completeness. To state it, we need to introduce a connection on the normal bundle of a Riemannian submanifold.

If \( \left( {M, g}\right) \) is a Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , the normal connection \( {\nabla }^{ \bot  } : \mathfrak{X}\left( M\right)  \times  \Gamma \left( {NM}\right)  \rightarrow  \Gamma \left( {NM}\right) \) is defined by

\[
{\nabla }_{X}^{ \bot  }N = {\left( {\widetilde{\nabla }}_{X}N\right) }^{ \bot  }
\]

where \( N \) is extended to a smooth vector field on a neighborhood of \( M \) in \( \widetilde{M} \) .

Proposition 8.6. If \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , then \( {\nabla }^{ \bot  } \) is a well-defined connection in \( {NM} \) , which is compatible with \( \widetilde{g} \) in the sense that for any two sections \( {N}_{1},{N}_{2} \) of \( {NM} \) and every \( X \in  \mathfrak{X}\left( M\right) \) , we have

\[
X\left\langle  {{N}_{1},{N}_{2}}\right\rangle   = \left\langle  {{\nabla }_{X}^{ \bot  }{N}_{1},{N}_{2}}\right\rangle   + \left\langle  {{N}_{1},{\nabla }_{X}^{ \bot  }{N}_{2}}\right\rangle  .
\]

- Exercise 8.7. Prove the preceding proposition.

We need the normal connection primarily to make sense of tangential covariant derivatives of the second fundamental form. To do so, we make the following definitions. Let \( F \rightarrow  M \) denote the bundle whose fiber at each point \( p \in  M \) is the set of bilinear maps \( {T}_{p}M \times  {T}_{p}M \rightarrow  {N}_{p}M \) . It is easy to check that \( F \) is a smooth vector bundle over \( M \) , and that smooth sections of \( F \) correspond to smooth maps \( \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \Gamma \left( {NM}\right) \) that are bilinear over \( {C}^{\infty }\left( M\right) \) , such as the second fundamental form. Define a connection \( {\nabla }^{F} \) in \( F \) as follows: if \( B \) is any smooth section of \( F \) , let \( {\nabla }_{X}^{F}B \) be the smooth section of \( F \) defined by

\[
\left( {{\nabla }_{X}^{F}B}\right) \left( {Y, Z}\right)  = {\nabla }_{X}^{ \bot  }\left( {B\left( {Y, Z}\right) }\right)  - B\left( {{\nabla }_{X}Y, Z}\right)  - B\left( {Y,{\nabla }_{X}Z}\right) .
\]

- Exercise 8.8. Prove that \( {\nabla }^{F} \) is a connection in \( F \) .

Now we are ready to state the last of the fundamental equations for submanifolds. This equation was independently discovered (in the special case of surfaces in \( {\mathbb{R}}^{3} \) ) by Karl M. Peterson (1853), Gaspare Mainardi (1856), and Delfino Codazzi (1868- 1869), and is sometimes designated by various combinations of these three names.

For the sake of simplicity we use the traditional but historically inaccurate name Codazzi equation.

Theorem 8.9 (The Codazzi Equation). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . For all \( W, X, Y \in  \mathcal{X}\left( M\right) \) , the following equation holds:

\[
{\left( \widetilde{R}\left( W, X\right) Y\right) }^{ \bot  } = \left( {{\nabla }_{W}^{F}\mathrm{{II}}}\right) \left( {X, Y}\right)  - \left( {{\nabla }_{X}^{F}\mathrm{{II}}}\right) \left( {W, Y}\right) . \tag{8.6}
\]

Proof. It suffices to show that both sides of (8.6) give the same result when we take their inner products with an arbitrary smooth normal vector field \( N \) along \( M \) :

\[
\langle \widetilde{R}\left( {W, X}\right) Y, N\rangle  = \langle \left( {{\nabla }_{W}^{F}\mathrm{{II}}}\right) \left( {X, Y}\right) , N\rangle  - \langle \left( {{\nabla }_{X}^{F}\mathrm{{II}}}\right) \left( {W, Y}\right) , N\rangle . \tag{8.7}
\]

We begin as in the proof of the Gauss equation: after extending the vector fields to a neighborhood of \( M \) and applying the Gauss formula, we obtain

\[
\widetilde{Rm}\left( {W, X, Y, N}\right)  = \left\langle  {{\widetilde{\nabla }}_{W}\left( {{\nabla }_{X}Y + \mathrm{{II}}\left( {X, Y}\right) }\right)  - {\widetilde{\nabla }}_{X}\left( {{\nabla }_{W}Y + \mathrm{{II}}\left( {W, Y}\right) }\right) }\right.
\]

\[
\left. {-{\widetilde{\nabla }}_{\left\lbrack  W, X\right\rbrack  }Y, N}\right\rangle
\]

Now when we expand the covariant derivatives, we need only pay attention to the normal components. This yields

\[
\widetilde{Rm}\left( {W, X, Y, N}\right)
\]

\[
= \left\langle  {\mathrm{{II}}\left( {W,{\nabla }_{X}Y}\right)  + \left( {{\nabla }_{W}^{F}\mathrm{{II}}}\right) \left( {X, Y}\right)  + \mathrm{{II}}\left( {{\nabla }_{W}X, Y}\right)  + \mathrm{{II}}\left( {X,{\nabla }_{W}Y}\right) , N}\right\rangle
\]

\[
- \left\langle  {\mathrm{{II}}\left( {X,{\nabla }_{W}Y}\right)  + \left( {{\nabla }_{X}^{F}\mathrm{{II}}}\right) \left( {W, Y}\right)  + \mathrm{{II}}\left( {{\nabla }_{X}W, Y}\right)  + \mathrm{{II}}\left( {W,{\nabla }_{X}Y}\right) , N}\right\rangle
\]

\[
- \langle \mathrm{{II}}\left( {\left\lbrack  {W, X}\right\rbrack  , Y}\right) , N\rangle .
\]

The terms involving \( {\nabla }_{X}Y \) and \( {\nabla }_{W}Y \) cancel each other in pairs, and three other terms sum to zero because \( {\nabla }_{W}X - {\nabla }_{X}W - \left\lbrack  {W, X}\right\rbrack   = 0 \) . What remains is (8.7).

## Curvature of a Curve

By studying the curvatures of curves, we can give a more geometric interpretation of the second fundamental form. Suppose \( \left( {M, g}\right) \) is a Riemannian or pseudo-Riemannian manifold, and \( \gamma  : I \rightarrow  M \) is a smooth unit-speed curve in \( M \) . We define the (geodesic) curvature of \( \gamma \) as the length of the acceleration vector field, which is the function \( \kappa  : I \rightarrow  \mathbb{R} \) given by

\[
\kappa \left( t\right)  = \left| {{D}_{t}{\gamma }^{\prime }\left( t\right) }\right| .
\]

If \( \gamma \) is an arbitrary regular curve in a Riemannian manifold (not necessarily of unit speed), we first find a unit-speed reparametrization \( \widetilde{\gamma } = \gamma  \circ  \varphi \) , and then define the curvature of \( \gamma \) at \( t \) to be the curvature of \( \widetilde{\gamma } \) at \( {\varphi }^{-1}\left( t\right) \) . In a pseudo-Riemannian manifold, the same approach works, but we have to restrict the definition to curves \( \gamma \) such that \( \left| {{\gamma }^{\prime }\left( t\right) }\right| \) is everywhere nonzero. Problem 8-6 gives a formula that can be used in the Riemannian case to compute the geodesic curvature directly without explicitly finding a unit-speed reparametrization.

From the definition, it follows that a smooth unit-speed curve has vanishing geodesic curvature if and only if it is a geodesic, so the geodesic curvature of a curve can be regarded as a quantitative measure of how far it deviates from being a geodesic. If \( M = {\mathbb{R}}^{n} \) with the Euclidean metric, the geodesic curvature agrees with the notion of curvature introduced in advanced calculus courses.

Now suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian or pseudo-Riemannian manifold and \( \left( {M, g}\right) \) is a Riemannian submanifold. Every regular curve \( \gamma  : I \rightarrow  M \) has two distinct geodesic curvatures: its intrinsic curvature \( \kappa \) as a curve in \( M \) , and its extrinsic curvature \( \widetilde{\kappa } \) as a curve in \( \widetilde{M} \) . The second fundamental form can be used to compute the relationship between the two.

Proposition 8.10 (Geometric Interpretation of II). Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) , p \in  M \) , and \( v \in  {T}_{p}M \) .

(a) II \( \left( {v, v}\right) \) is the \( \widetilde{g} \) -acceleration at \( p \) of the \( g \) -geodesic \( {\gamma }_{v} \) .

(b) If \( v \) is a unit vector, then \( \left| {\mathrm{{II}}\left( {v, v}\right) }\right| \) is the \( \widetilde{g} \) -curvature of \( {\gamma }_{v} \) at \( p \) .

Proof. Suppose \( \gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  M \) is any regular curve with \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) . Applying the Gauss formula (Corollary 8.3) to the vector field \( {\gamma }^{\prime } \) along \( \gamma \) , we obtain

\[
{\widetilde{D}}_{t}{\gamma }^{\prime } = {D}_{t}{\gamma }^{\prime } + \operatorname{II}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) .
\]

If \( \gamma \) is a \( g \) -geodesic in \( M \) , this formula simplifies to

\[
{\widetilde{D}}_{t}{\gamma }^{\prime } = \mathrm{{II}}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) .
\]

Both conclusions of the proposition follow from this.

Note that the second fundamental form is completely determined by its values of the form \( \operatorname{II}\left( {v, v}\right) \) for unit vectors \( v \) , by the following lemma.

Lemma 8.11. Suppose \( V \) is an inner product space, \( W \) is a vector space, and \( B,{B}^{\prime } : V \times  V \rightarrow  W \) are symmetric and bilinear. If \( B\left( {v, v}\right)  = {B}^{\prime }\left( {v, v}\right) \) for every unit vector \( v \in  V \) , then \( B = {B}^{\prime } \) .

Proof. Every vector \( v \in  V \) can be written \( v = \lambda \widehat{v} \) for some unit vector \( \widehat{v} \) , so the bilinearity of \( B \) and \( {B}^{\prime } \) implies \( B\left( {v, v}\right)  = {B}^{\prime }\left( {v, v}\right) \) for every \( v \) , not just unit vectors. The result then follows from the following polarization identity, which is proved in exactly the same way as its counterpart (2.2) for inner products:

\[
B\left( {v, w}\right)  = \frac{1}{4}\left( {B\left( {v + w, v + w}\right)  - B\left( {v - w, v - w}\right) }\right) .
\]

Because the intrinsic and extrinsic accelerations of a curve are usually different, it is generally not the case that a \( \widetilde{g} \) -geodesic that starts tangent to \( M \) stays in \( M \) ; just think of a sphere in Euclidean space, for example. A Riemannian submanifold \( \left( {M, g}\right) \) of \( \left( {\widetilde{M},\widetilde{g}}\right) \) is said to be totally geodesic if every \( \widetilde{g} \) -geodesic that is tangent to \( M \) at some time \( {t}_{0} \) stays in \( M \) for all \( t \) in some interval \( \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right) \) .

Proposition 8.12. Suppose \( \left( {M, g}\right) \) is an embedded Riemannian submanifold of a Riemannian or pseudo-Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , The following are equivalent:

(a) \( M \) is totally geodesic in \( \widetilde{M} \) .

(b) Every \( g \) -geodesic in \( M \) is also a \( \widetilde{g} \) -geodesic in \( \widetilde{M} \) .

(c) The second fundamental form of \( M \) vanishes identically.

Proof. We will prove (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (a). First assume that \( M \) is totally geodesic. Let \( \gamma  : I \rightarrow  M \) be a \( g \) -geodesic. For each \( {t}_{0} \in  I \) , let \( \widetilde{\gamma } : \widetilde{I} \rightarrow  \widetilde{M} \) be the \( \widetilde{g} \) - geodesic with \( \widetilde{\gamma }\left( {t}_{0}\right)  = \gamma \left( {t}_{0}\right) \) and \( {\widetilde{\gamma }}^{\prime }\left( {t}_{0}\right)  = {\gamma }^{\prime }\left( {t}_{0}\right) \) . The hypothesis implies that there is some open interval \( {I}_{0} \) containing \( {t}_{0} \) such that \( \widetilde{\gamma }\left( t\right)  \in  M \) for \( t \in  {I}_{0} \) . On \( {I}_{0} \) , the Gauss formula (8.2) for \( {\widetilde{\gamma }}^{\prime } \) reads

\[
0 = {\widetilde{D}}_{t}{\widetilde{\gamma }}^{\prime } = {D}_{t}{\widetilde{\gamma }}^{\prime } + \operatorname{II}\left( {{\widetilde{\gamma }}^{\prime },{\widetilde{\gamma }}^{\prime }}\right) .
\]

Because the first term on the right is tangent to \( M \) and the second is normal, the two terms must vanish individually. In particular, \( {D}_{t}{\widetilde{\gamma }}^{\prime } \equiv  0 \) on \( {I}_{0} \) , which means that \( \widetilde{\gamma } \) is also a \( g \) -geodesic there. By uniqueness of geodesics, therefore, \( \gamma  = \widetilde{\gamma } \) on \( {I}_{0} \) , so it follows in turn that \( \gamma \) is a \( \widetilde{g} \) -geodesic there. Since the same is true in a neighborhood of every \( {t}_{0} \in  I \) , it follows that \( \gamma \) is a \( \widetilde{g} \) -geodesic on its whole domain.

Next assume that every \( g \) -geodesic is a \( \widetilde{g} \) -geodesic. Let \( p \in  M \) and \( v \in  {T}_{p}M \) be arbitrary, and let \( \gamma  = {\gamma }_{v} : I \rightarrow  M \) be the \( g \) -geodesic with \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) . The hypothesis implies that \( \gamma \) is also a \( \widetilde{g} \) -geodesic. Thus \( {\widetilde{D}}_{t}{\gamma }^{\prime } = {D}_{t}{\gamma }^{\prime } = 0 \) , so the Gauss formula yields II \( \left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right)  = 0 \) along \( \gamma \) . In particular, \( \coprod  \left( {v, v}\right)  = 0 \) . By Lemma 8.11, this implies that II is identically zero.

Finally, assume that II \( \equiv  0 \) , and let \( \widetilde{\gamma } : I \rightarrow  \widetilde{M} \) be a \( \widetilde{g} \) -geodesic such that \( \widetilde{\gamma }\left( {t}_{0}\right)  \in \; M \) and \( {\widetilde{\gamma }}^{\prime }\left( {t}_{0}\right)  \in  {TM} \) for some \( {t}_{0} \in  I \) . Let \( \gamma  : I \rightarrow  M \) be the \( g \) -geodesic with the same initial conditions: \( \gamma \left( {t}_{0}\right)  = \widetilde{\gamma }\left( {t}_{0}\right) \) and \( {\gamma }^{\prime }\left( {t}_{0}\right)  = {\widetilde{\gamma }}^{\prime }\left( {t}_{0}\right) \) . The Gauss formula together with the hypothesis II \( \equiv  0 \) implies that \( {\widetilde{D}}_{t}\gamma  = {D}_{t}\gamma  = 0 \) , so \( \gamma \) is also a \( \widetilde{g} \) -geodesic. By uniqueness of geodesics, therefore, \( \widetilde{\gamma } = \gamma \) on the intersection of their domains, which implies that \( \widetilde{\gamma }\left( t\right) \) lies in \( M \) for \( t \) in some open interval around \( {t}_{0} \) .

## Hypersurfaces

Now we specialize the preceding considerations to the case in which \( M \) is a hypersurface (i.e., a submanifold of codimension 1) in \( \widetilde{M} \) . Throughout this section, our default assumption is that \( \left( {M, g}\right) \) is an embedded \( n \) -dimensional Riemannian sub-manifold of an \( \left( {n + 1}\right) \) -dimensional Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . (The analogous formulas in the pseudo-Riemannian case are a little different; see Problem 8-19.)

In this situation, at each point of \( M \) there are exactly two unit normal vectors. In terms of any local adapted orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{n + 1}}\right) \) , the two choices are \( \pm  {E}_{n + 1} \) . In a small enough neighborhood of each point of \( M \) , therefore, we can always choose a smooth unit normal vector field along \( M \) .

If both \( M \) and \( \widetilde{M} \) are orientable, we can use an orientation to pick out a global smooth unit normal vector field along all of \( M \) . In general, though, this might or might not be possible. Since all of our computations in this chapter are local, we will always assume that we are working in a small enough neighborhood that a smooth unit normal field exists. We will address as we go along the question of how various quantities depend on the choice of normal vector field.

## The Scalar Second Fundamental Form and the Shape Operator

Having chosen a distinguished smooth unit normal vector field \( N \) on the hypersurface \( M \subseteq  \widetilde{M} \) , we can replace the vector-valued second fundamental form II by a simpler scalar-valued form. The scalar second fundamental form of \( M \) is the symmetric covariant 2-tensor field \( h \in  \Gamma \left( {{\sum }^{2}{T}^{ * }M}\right) \) defined by \( h = {\mathrm{{II}}}_{N} \) (see (8.3)); in other words,

\[
h\left( {X, Y}\right)  = \langle N,\operatorname{II}\left( {X, Y}\right) \rangle . \tag{8.8}
\]

Using the Gauss formula \( {\widetilde{\nabla }}_{X}Y = {\nabla }_{X}Y + \mathrm{{II}}\left( {X, Y}\right) \) and noting that \( {\nabla }_{X}Y \) is orthogonal to \( N \) , we can rewrite the definition as

\[
h\left( {X, Y}\right)  = \left\langle  {N,{\widetilde{\nabla }}_{X}Y}\right\rangle \tag{8.9}
\]

Also, since \( N \) is a unit vector spanning \( {NM} \) at each point, the definition of \( h \) is equivalent to

\[
\mathrm{{II}}\left( {X, Y}\right)  = h\left( {X, Y}\right) N. \tag{8.10}
\]

Note that replacing \( N \) by \( - N \) multiplies \( h \) by -1, so the sign of \( h \) depends on which unit normal is chosen; but \( h \) is otherwise independent of the choices.

The choice of unit normal field also determines a Weingarten map \( {W}_{N} : \mathfrak{X}\left( M\right)  \rightarrow \; \mathfrak{X}\left( M\right) \) by (8.4); in the case of a hypersurface, we use the notation \( s = {W}_{N} \) and call it the shape operator of \( M \) . Alternatively, we can think of \( s \) as the \( \left( {1,1}\right) \) -tensor field on \( M \) obtained from \( h \) by raising an index. It is characterized by

\[
\langle {sX}, Y\rangle  = h\left( {X, Y}\right) \;\text{ for all }X, Y \in  \mathfrak{X}\left( M\right) .
\]

Because \( h \) is symmetric, \( s \) is a self-adjoint endomorphism of \( {TM} \) , that is,

\[
\langle {sX}, Y\rangle  = \langle X,{sY}\rangle \;\text{ for all }X, Y \in  \mathfrak{X}\left( M\right) .
\]

As with \( h \) , the sign of \( s \) depends on the choice of \( N \) .

In terms of the tensor fields \( h \) and \( s \) , the formulas of the last section can be rewritten somewhat more simply. For this purpose, we will use two tensor operations defined in Chapter 7: the Kulkarni-Nomizu product of symmetric 2-tensors \( h, k \) is

\[
h \oslash  k\left( {w, x, y, z}\right)  = h\left( {w, z}\right) k\left( {x, y}\right)  + h\left( {x, y}\right) k\left( {w, z}\right)
\]

\[
- h\left( {w, y}\right) k\left( {x, z}\right)  - h\left( {x, z}\right) k\left( {w, y}\right) ,
\]

and the exterior covariant derivative of a smooth symmetric 2-tensor field \( T \) is

\[
\left( {DT}\right) \left( {x, y, z}\right)  =  - \left( {\nabla T}\right) \left( {x, y, z}\right)  + \left( {\nabla T}\right) \left( {x, z, y}\right) .
\]

Theorem 8.13 (Fundamental Equations for a Hypersurface). Suppose \( \left( {M, g}\right) \) is a Riemannian hypersurface in a Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , and \( N \) is a smooth unit normal vector field along \( M \) .

(a) THE GAUSS FORMULA FOR A HYPERSURFACE: If \( X, Y \in  \mathfrak{X}\left( M\right) \) are extended to an open subset of \( \widetilde{M} \) , then

\[
{\widetilde{\nabla }}_{X}Y = {\nabla }_{X}Y + h\left( {X, Y}\right) N.
\]

(b) THE GAUSS FORMULA FOR A CURVE IN A HYPERSURFACE: If \( \gamma  : I \rightarrow  M \) is a smooth curve and \( X : I \rightarrow  {TM} \) is a smooth vector field along \( \gamma \) , then

\[
{\widetilde{D}}_{t}X = {D}_{t}X + h\left( {{\gamma }^{\prime }, X}\right) N.
\]

(c) THE WEINGARTEN EQUATION FOR A HYPERSURFACE: For every \( X \in \; X\left( M\right) \) ,

\[
{\widetilde{\nabla }}_{X}N =  - {sX} \tag{8.11}
\]

(d) THE GAUSS EQUATION FOR A HYPERSURFACE: For all \( W, X, Y, Z \in  \mathfrak{X}\left( M\right) \) ,

\[
\widetilde{Rm}\left( {W, X, Y, Z}\right)  = {Rm}\left( {W, X, Y, Z}\right)  - \frac{1}{2}\left( {h \oslash  h}\right) \left( {W, X, Y, Z}\right) .
\]

(e) THE CODAZZI EQUATION FOR A HYPERSURFACE: For all \( W, X, Y \in  \mathcal{X}\left( M\right) \) ,

\[
\widetilde{\operatorname{Rm}}\left( {W, X, Y, N}\right)  = \left( {Dh}\right) \left( {Y, W, X}\right) . \tag{8.12}
\]

Proof. Parts (a), (b), and (d) follow immediately from substituting (8.10) into the general versions of the Gauss formula and Gauss equation. To prove (c), note first that the general version of the Weingarten equation can be written \( {\left( {\widetilde{\nabla }}_{X}N\right) }^{\top } =  - {sX} \) . Since \( \left\langle  {{\widetilde{\nabla }}_{X}N, N}\right\rangle   = \frac{1}{2}X\left( {\left| N\right| }^{2}\right)  = 0 \) , it follows that \( {\widetilde{\nabla }}_{X}N \) is tangent to \( M \) , so (c) follows.

To prove the hypersurface Codazzi equation, note that the fact that \( N \) is a unit vector field implies

\[
0 = X{\left| N\right| }_{\widetilde{g}}^{2} = 2{\left\langle  {\nabla }_{X}^{ \bot  }N, N\right\rangle  }_{\widetilde{g}}.
\]

Since \( N \) spans the normal bundle, this implies that \( N \) is parallel with respect to the normal connection. Moreover,

Hypersurfaces

\[
\left( {{\nabla }_{W}^{F}\mathrm{{II}}}\right) \left( {X, Y}\right)  = {\nabla }_{W}^{ \bot  }\left( {\mathrm{{II}}\left( {X, Y}\right) }\right)  - \mathrm{{II}}\left( {{\nabla }_{W}X, Y}\right)  - \mathrm{{II}}\left( {X,{\nabla }_{W}Y}\right)
\]

\[
= {\nabla }_{W}^{ \bot  }\left( {h\left( {X, Y}\right) N}\right)  - \mathrm{{II}}\left( {{\nabla }_{W}X, Y}\right)  - \mathrm{{II}}\left( {X,{\nabla }_{W}Y}\right)
\]

\[
= \left( {W\left( {h\left( {X, Y}\right) }\right)  - h\left( {{\nabla }_{W}X, Y}\right)  - h\left( {X,{\nabla }_{W}Y}\right) }\right) N
\]

\[
= {\nabla }_{W}\left( h\right) \left( {X, Y}\right) N\text{ . }
\]

Inserting this into the general form (8.6) of the Codazzi equation and using the fact that \( \nabla h \) is symmetric in its first two indices yields

\[
\widetilde{Rm}\left( {W, X, Y, N}\right)  = {\nabla }_{W}\left( h\right) \left( {X, Y}\right)  - {\nabla }_{X}\left( h\right) \left( {W, Y}\right)
\]

\[
= \left( {\nabla h}\right) \left( {X, Y, W}\right)  - \left( {\nabla h}\right) \left( {W, Y, X}\right)
\]

\[
= \left( {\nabla h}\right) \left( {Y, X, W}\right)  - \left( {\nabla h}\right) \left( {Y, W, X}\right) ,
\]

which is equivalent to (8.12).

## Principal Curvatures

At every point \( p \in  M \) , we have seen that the shape operator \( s \) is a self-adjoint linear endomorphism of the tangent space \( {T}_{p}M \) . To analyze such an operator, we recall some linear-algebraic facts about self-adjoint endomorphisms.

Lemma 8.14. Suppose \( V \) is a finite-dimensional inner product space and \( s : V \rightarrow  V \) is a self-adjoint linear endomorphism. Let \( C \) denote the set of unit vectors in \( V \) . There is a vector \( {v}_{0} \in  C \) where the function \( v \mapsto  \langle {sv}, v\rangle \) achieves its maximum among elements of \( C \) , and every such vector is an eigenvector of \( s \) with eigenvalue \( {\lambda }_{0} = \left\langle  {s{v}_{0},{v}_{0}}\right\rangle  . \)

- Exercise 8.15. Use the Lagrange multiplier rule (Prop. A.29) to prove this lemma.

Proposition 8.16 (Finite-Dimensional Spectral Theorem). Suppose \( V \) is a finite-dimensional inner product space and \( s : V \rightarrow  V \) is a self-adjoint linear endomorphism. Then \( V \) has an orthonormal basis of s-eigenvectors, and all of the eigenvalues are real.

Proof. The proof is by induction on \( n = \dim V \) . The \( n = 1 \) result is easy, so assume that the theorem holds for some \( n \geq  1 \) and suppose \( \dim V = n + 1 \) . Lemma 8.14 shows that \( s \) has a unit eigenvector \( {b}_{0} \) with a real eigenvalue \( {\lambda }_{0} \) . Let \( B \subseteq  V \) be the span of \( {b}_{0} \) . Since \( s\left( B\right)  \subseteq  B \) , self-adjointness of \( s \) implies \( s\left( {B}^{ \bot  }\right)  \subseteq  {B}^{ \bot  } \) . The inductive hypothesis applied to \( {\left. s\right| }_{{B}^{ \bot  }} \) implies that \( {B}^{ \bot  } \) has an orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) of \( s \) -eigenvectors with real eigenvalues, and then \( \left( {{b}_{0},{b}_{1},\ldots ,{b}_{n}}\right) \) is the desired basis of \( V \) .

Applying this proposition to the shape operator \( s : {T}_{p}M \rightarrow  {T}_{p}M \) , we see that \( s \) has real eigenvalues \( {\kappa }_{1},\ldots ,{\kappa }_{n} \) , and there is an orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{p}M \) consisting of \( s \) -eigenvectors, with \( s{b}_{i} = {\kappa }_{i}{b}_{i} \) for each \( i \) (no summation). In this basis, both \( h \) and \( s \) are represented by diagonal matrices, and \( h \) has the expression

\[
h\left( {v, w}\right)  = {\kappa }_{1}{v}^{1}{w}^{1} + \cdots  + {\kappa }_{n}{v}^{n}{w}^{n}.
\]

The eigenvalues of \( s \) at a point \( p \in  M \) are called the principal curvatures of \( M \) at \( p \) , and the corresponding eigenspaces are called the principal directions. The principal curvatures all change sign if we reverse the normal vector, but the principal directions and principal curvatures are otherwise independent of the choice of coordinates or bases.

There are two combinations of the principal curvatures that play particularly important roles for hypersurfaces. The Gaussian curvature is defined as \( K = \det \left( s\right) \) , and the mean curvature as \( H = \left( {1/n}\right) \operatorname{tr}\left( s\right)  = \left( {1/n}\right) {\operatorname{tr}}_{g}\left( h\right) \) . Since the determinant and trace of a linear endomorphism are basis-independent, these are well defined once a unit normal is chosen. In terms of the principal curvatures, they are

\[
K = {\kappa }_{1}{\kappa }_{2}\cdots {\kappa }_{n},\;H = \frac{1}{n}\left( {{\kappa }_{1} + \cdots  + {\kappa }_{n}}\right) ,
\]

as can be seen by expressing \( s \) in terms of an orthonormal basis of eigenvectors. If \( N \) is replaced by \( - N \) , then \( H \) changes sign, while \( K \) is multiplied by \( {\left( -1\right) }^{n} \) .

## Computations in Semigeodesic Coordinates

Semigeodesic coordinates (Prop. 6.41) provide an extremely convenient tool for computing the invariants of hypersurfaces.

Let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be an \( \left( {n + 1}\right) \) -dimensional Riemannian manifold, and let \( \left( {{x}^{1},\ldots ,{x}^{n}, v}\right) \) be semigeodesic coordinates on an open subset \( U \subseteq  \widetilde{M} \) . (For example, they might be Fermi coordinates for the hypersurface \( {M}_{0} = {v}^{-1}\left( 0\right) \) ; see Example 6.43.) For each real number \( a \) such that \( {v}^{-1}\left( a\right)  \neq  \varnothing \) , the level set \( {M}_{a} = {v}^{-1}\left( a\right) \) is a properly embedded hypersurface in \( U \) . Let \( {g}_{a} \) denote the induced metric on \( {M}_{a} \) . Corollary 6.42 shows that \( \widetilde{g} \) is given by

\[
\widetilde{g} = d{v}^{2} + \mathop{\sum }\limits_{{\alpha ,\beta  = 1}}^{n}{g}_{\alpha \beta }\left( {{x}^{1},\ldots ,{x}^{n}, v}\right) d{x}^{\alpha }d{x}^{\beta }. \tag{8.13}
\]

The restrictions of \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) give smooth coordinates for each hypersurface \( {M}_{a} \) , and in those coordinates the induced metric \( {g}_{a} \) is given by \( {g}_{a} = {g}_{\alpha \beta }d{x}^{\alpha }d{x}^{\beta }{ \mid  }_{v = a} \) . (Here we use the summation convention with Greek indices running from 1 to \( n \) .) The vector field \( {\partial }_{v} = {\partial }_{n + 1} \) restricts to a unit normal vector field along each hypersurface \( {M}_{a} \) .

As the next proposition shows, semigeodesic coordinates give us a simple formula for the second fundamental forms of all of the submanifolds \( {M}_{a} \) at once.

Proposition 8.17. With notation as above, the components in \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) -coordinates of the scalar second fundamental form, the shape operator, and the mean curvature of \( \left( {{M}_{a},{g}_{a}}\right) \) (denoted by \( {h}_{a},{s}_{a} \) , and \( {H}_{a} \) , respectively) with respect to the normal \( N = {\partial }_{v} \) are given by

\[
{\left( {h}_{a}\right) }_{\alpha \beta } =  - {\left. \frac{1}{2}{\partial }_{v}{g}_{\alpha \beta }\right| }_{v = a},
\]

\[
{\left( {s}_{a}\right) }_{\beta }^{\alpha } =  - {\left. \frac{1}{2}{g}^{\alpha \gamma }{\partial }_{v}{g}_{\gamma \beta }\right| }_{v = a},
\]

\[
{H}_{a} =  - {\left. \frac{1}{2n}{g}^{\alpha \beta }{\partial }_{v}{g}_{\alpha \beta }\right| }_{v = a}.
\]

Proof. The normal component of \( {\widetilde{\nabla }}_{{\partial }_{\alpha }}{\partial }_{\beta } \) is \( {\widetilde{\Gamma }}_{\alpha \beta }^{n + 1}{\partial }_{v} \) , which Corollary 6.42 shows is equal to \( - \frac{1}{2}{\partial }_{v}{g}_{\alpha \beta }{\partial }_{r} \) (noting that the roles of \( g \) and \( \widehat{g} \) in that corollary are being played here by \( \widetilde{g} \) and \( {g}_{a} \) , respectively). Equation (8.9) evaluated at points of \( {M}_{a} \) gives

\[
{\left( {h}_{a}\right) }_{\alpha \beta } = {\left\langle  {\widetilde{\nabla }}_{{\partial }_{\alpha }}{\partial }_{\beta }, N\right\rangle  }_{\widetilde{g}} = {\left\langle  -\frac{1}{2}{\partial }_{v}{g}_{\alpha \beta }{\partial }_{v},{\partial }_{v}\right\rangle  }_{\widetilde{g}} =  - \frac{1}{2}{\partial }_{v}{g}_{\alpha \beta }.
\]

The formulas for \( {s}_{a} \) and \( {H}_{a} \) follow by using \( \left( {g}^{\alpha \gamma }\right) \) (the inverse matrix of \( \left( {g}_{\alpha \gamma }\right) \) ) to raise an index and then taking the trace.

## Minimal Hypersurfaces

A natural question that has received a great deal of attention over the past century is this: Given a simple closed curve \( C \) in \( {\mathbb{R}}^{3} \) , is there an embedded or immersed surface \( M \) with \( \partial M = C \) that has least area among all surfaces with the same boundary? If so, what is it? Such surfaces are models of the soap films that are produced when a closed loop of wire is dipped in soapy water.

More generally, we can consider the analogous question for hypersurfaces in Riemannian manifolds. Suppose \( M \) is a compact codimension-1 submanifold with nonempty boundary in an \( \left( {n + 1}\right) \) -dimensional Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . By analogy with the case of surfaces in \( {\mathbb{R}}^{3} \) , it is traditional to use the term area to refer to the \( n \) -dimensional volume of \( M \) with its induced Riemannian metric, and to say that \( M \) is area-minimizing if it has the smallest area among all compact embedded hypersurfaces in \( \widetilde{M} \) with the same boundary. One key observation is the following theorem, which is an analogue for hypersurfaces of Theorem 6.4 about length-minimizing curves.

Theorem 8.18. Let \( M \) be a compact codimension-1 submanifold with nonempty boundary in an \( \left( {n + 1}\right) \) -dimensional Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) . If \( M \) is area-minimizing, then its mean curvature is identically zero.

Proof. Let \( g \) denote the induced metric on \( M \) . The fact that \( M \) minimizes area among hypersurfaces with the same boundary means, in particular, that it minimizes area among small perturbations of \( M \) in a neighborhood of a single point. We will exploit this idea to prove that \( M \) must have zero mean curvature everywhere.

Let \( p \in  \operatorname{Int}M \) be arbitrary, let \( \left( {{x}^{1},\ldots ,{x}^{n}, v}\right) \) be Fermi coordinates for \( M \) on an open set \( \widetilde{U} \subseteq  \widetilde{M} \) containing \( p \) (see Example 6.43), and let \( U = \widetilde{U} \cap  M \) . By taking

![bo_d7dtff491nqc73eq8m7g_250_440_185_654_289_0.jpg](images/bo_d7dtff491nqc73eq8m7g_250_440_185_654_289_0.jpg)

Fig. 8.2: The hypersurface \( {M}_{t} \)

\( \widetilde{U} \) sufficiently small, we can arrange that \( U \) is a regular coordinate ball in \( M \) (see p. 374) and \( \widetilde{U} \cap  \partial M = \varnothing \) . We use \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) as coordinates on \( M \) , and observe the summation convention with Greek indices running from 1 to \( n \) .

Let \( \varphi \) be an arbitrary smooth real-valued function on \( M \) with compact support in \( U \) . For sufficiently small \( t \) , define a set \( {M}_{t} \subseteq  \widetilde{M} \) by

\[
{M}_{t} = \left( {M \smallsetminus  U}\right)  \cup  \left\{  {z \in  \widetilde{U} : v\left( z\right)  = {t\varphi }\left( {{x}^{1}\left( z\right) ,\ldots ,{x}^{n}\left( z\right) }\right) }\right\}  .
\]

(See Fig. 8.2.) Then \( {M}_{t} \) is an embedded smooth hypersurface in \( \widetilde{M} \) , which agrees with \( M \) outside of \( U \) and which coincides with the graph of \( v = {t\varphi } \) in \( \widetilde{U} \) . Let \( {f}_{t} : U \rightarrow  \widetilde{U} \) be the graph parametrization of \( {M}_{t} \cap  \widetilde{U} \) , given in Fermi coordinates by

\[
{f}_{t}\left( {{x}^{1},\ldots ,{x}^{n}}\right)  = \left( {{x}^{1},\ldots ,{x}^{n},{t\varphi }\left( x\right) }\right) . \tag{8.14}
\]

Using this map, for each \( t \) we can define a diffeomorphism \( {F}_{t} : M \rightarrow  {M}_{t} \) by

\[
{F}_{t}\left( z\right)  = \left\{  \begin{array}{ll} z, & z \in  M \smallsetminus  \operatorname{supp}\varphi , \\  {f}_{t}\left( z\right) , & z \in  U. \end{array}\right.
\]

For each \( t \) , let \( {\widehat{g}}_{t} = {\iota }_{{M}_{t}}^{ * }\widetilde{g} \) denote the induced Riemannian metric on \( {M}_{t} \) , and let \( {g}_{t} = {F}_{t}^{ * }{\widehat{g}}_{t} = {F}_{t}^{ * }\widetilde{g} \) denote the pulled-back metric on \( M \) . When \( t = 0 \) , we have \( {M}_{0} = M \) , and both \( {g}_{0} \) and \( {\widehat{g}}_{0} \) are equal to the induced metric \( g \) on \( M \) . Since \( \widetilde{g} \) is given by (8.13) in Fermi coordinates, a simple computation shows that in \( U \) , \( {g}_{t} = {F}_{t}^{ * }\widetilde{g} \) has the coordinate expression \( {g}_{t} = {\left( {g}_{t}\right) }_{\alpha \beta }d{x}^{\alpha }d{x}^{\beta } \) , where

\[
{\left( {g}_{t}\right) }_{\alpha \beta } = {t}^{2}\frac{\partial \varphi }{\partial {x}^{\alpha }}\left( x\right) \frac{\partial \varphi }{\partial {x}^{\beta }}\left( x\right)  + {g}_{\alpha \beta }\left( {x,{t\varphi }\left( x\right) }\right) , \tag{8.15}
\]

while on \( M \smallsetminus  U,{g}_{t} \) is equal to \( g \) and thus is independent of \( t \) .

Since each \( {M}_{t} \) is a smooth hypersurface with the same boundary as \( M \) , our hypothesis guarantees that \( \operatorname{Area}\left( {{M}_{t},{\widehat{g}}_{t}}\right) \) achieves a minimum at \( t = 0 \) . Because \( {F}_{t} \) is an isometry from \( \left( {M,{g}_{t}}\right) \) to \( \left( {{M}_{t},{\widehat{g}}_{t}}\right) \) , we can express this area as follows:

\[
\operatorname{Area}\left( {{M}_{t},{\widehat{g}}_{t}}\right)  = \operatorname{Area}\left( {M,{g}_{t}}\right)  = \operatorname{Area}\left( {M \smallsetminus  U, g}\right)  + \operatorname{Area}\left( {U,{g}_{t}}\right) .
\]

The first term on the right is independent of \( t \) , and we can compute the second term explicitly in coordinates \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) on \( U \) :

\[
\operatorname{Area}\left( {U,{g}_{t}}\right)  = {\int }_{U}\sqrt{\det {g}_{t}}d{x}^{1}\cdots d{x}^{n},
\]

where \( \det {g}_{t} \) denotes the determinant of the matrix \( \left( {\left( {g}_{t}\right) }_{\alpha \beta }\right) \) defined by (8.15). The integrand above is a smooth function of \( t \) and \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) , so the area is a smooth function of \( t \) . We have

(8.16)

\[
{\left. \frac{d}{dt}\right| }_{t = 0}\operatorname{Area}\left( {{M}_{t},{\widehat{g}}_{t}}\right)  = {\left. {\int }_{U}\frac{\partial }{\partial t}\right| }_{t = 0}\sqrt{\det {g}_{t}}d{x}^{1}\cdots d{x}^{n}
\]

\[
= {\int }_{U}\frac{1}{2}{\left( \det g\right) }^{-1/2}{\left. \frac{\partial }{\partial t}\right| }_{t = 0}\left( {\det {g}_{t}}\right) d{x}^{1}\cdots d{x}^{n}.
\]

(The differentiation under the integral sign is justified because the integrand is smooth and has compact support in \( U \) .)

To compute the derivative of the determinant, note that the expansion by minors along, say, row \( \alpha \) shows that the partial derivative of det with respect to the matrix entry in position \( \left( {\alpha ,\beta }\right) \) is equal to the cofactor \( {\operatorname{cof}}^{\alpha \beta } \) , and thus by the chain rule,

\[
{\left. \frac{\partial }{\partial t}\right| }_{t = 0}\left( {\det {g}_{t}}\right)  = {\left. {\operatorname{cof}}^{\alpha \beta }\frac{\partial }{\partial t}\right| }_{t = 0}{\left( {g}_{t}\right) }_{\alpha \beta }. \tag{8.17}
\]

On the other hand, Cramer’s rule shows that the \( \left( {\alpha ,\beta }\right) \) component of the inverse matrix is given by \( {g}^{\alpha \beta } = {\left( \det g\right) }^{-1}{\operatorname{cof}}^{\alpha \beta } \) . Thus from (8.17) and (8.15) we obtain

\[
{\left. \frac{\partial }{\partial t}\right| }_{t = 0}\left( {\det {g}_{t}}\right)  = \left( {\det g}\right) {g}^{\alpha \beta }{\left. \frac{\partial }{\partial t}\right| }_{t = 0}{\left( {g}_{t}\right) }_{\alpha \beta } = \left( {\det g}\right) {g}^{\alpha \beta }\frac{\partial {g}_{\alpha \beta }}{\partial v}\varphi .
\]

Inserting this into (8.16) and using the result of Proposition 8.17, we conclude that

\[
{\left. \frac{d}{dt}\right| }_{t = 0}\operatorname{Area}\left( {{M}_{t},{\widehat{g}}_{t}}\right)  = {\int }_{U}\frac{1}{2}{\left( \det g\right) }^{1/2}{g}^{\alpha \beta }\frac{\partial {g}_{\alpha \beta }}{\partial v}{\varphi d}{x}^{1}\cdots d{x}^{n} \tag{8.18}
\]

\[
=  - n{\int }_{U}{H\varphi d}{V}_{g},
\]

where \( H \) is the mean curvature of \( \left( {M, g}\right) \) . Since \( \operatorname{Area}\left( {{M}_{t},{\widehat{g}}_{t}}\right) \) attains a minimum at \( t = 0 \) , we conclude that \( {\int }_{U}{H\varphi d}{V}_{g} = 0 \) for every such \( \varphi \) .

Now suppose for the sake of contradiction that \( H\left( p\right)  \neq  0 \) . If \( H\left( p\right)  > 0 \) , we can let \( \varphi \) be a smooth nonnegative bump function that is positive at \( p \) and supported in a small neighborhood of \( p \) on which \( H > 0 \) . The argument above shows that \( {\int }_{U}{H\varphi d}{V}_{g} = \) 0, which is impossible because the integrand is nonnegative on \( U \) and positive on an open set. A similar argument rules out \( H\left( p\right)  < 0 \) . Since \( p \) was an arbitrary point in Int \( M \) , we conclude that \( H \equiv  0 \) on Int \( M \) , and then by continuity on all of \( M \) .

Because of the result of Theorem 8.18, a hypersurface (immersed or embedded, with or without boundary) that has mean curvature identically equal to zero is called a minimal hypersurface (or a minimal surface when it has dimension 2). It is an unfortunate historical accident that the term "minimal hypersurface" is defined in this way, because in fact, a minimal hypersurface is just a critical point for the area, not necessarily area-minimizing. It can be shown that as in the case of geodesics, a small enough piece of every minimal hypersurface is area-minimizing.

As a complement to the above theorem about hypersurfaces that minimize area with fixed boundary, we have the following result about hypersurfaces that minimize area while enclosing a fixed volume.

Theorem 8.19. Suppose \( \left( {\widetilde{M}, g}\right) \) is a Riemannian \( \left( {n + 1}\right) \) -manifold, \( D \subseteq  \widetilde{M} \) is a compact regular domain, and \( M = \partial D \) . If \( M \) has the smallest surface area among boundaries of compact regular domains with the same volume as \( D \) , then \( M \) has constant mean curvature (computed with respect to the outward unit normal).

Proof. Let \( g \) denote the induced metric on \( M \) . Assume for the sake of contradiction that the mean curvature \( H \) of \( M \) is not constant, and let \( p, q \in  M \) be points such that \( H\left( p\right)  < H\left( q\right) \) .

Since \( M \) is compact, it has an \( \varepsilon \) -tubular neighborhood for some \( \varepsilon  > 0 \) by Theorem 5.25. As in the previous proof, let \( \left( {{x}^{1},\ldots ,{x}^{n}, v}\right) \) be Fermi coordinates for \( M \) on an open set \( \widetilde{U} \subseteq  \widetilde{M} \) containing \( p \) , and let \( U = \widetilde{U} \cap  M \) . We may assume that \( U \) is a regular coordinate ball in \( M \) and the image of the chart is a set of the form \( \widehat{U} \times  \left( {-\varepsilon ,\varepsilon }\right) \) for some open subset \( \widehat{U} \subseteq  {\mathbb{R}}^{n} \) . Similarly, let \( \left( {{y}^{1},\ldots ,{y}^{n}, w}\right) \) be Fermi coordinates for \( M \) on an open set \( \widetilde{W} \subseteq  \widetilde{M} \) containing \( q \) and satisfying the analogous conditions, and let \( W = \widetilde{W} \cap  M \) . By replacing \( v \) with its negative if necessary, we can arrange that \( D \cap  \widetilde{U} \) is the set where \( v \leq  0 \) , and similarly for \( w \) . Also, by shrinking both domains, we can assume that the mean curvature of \( M \) satisfies \( H \leq \; {H}_{1} \) on \( U \) and \( H \geq  {H}_{2} \) on \( W \) , where \( {H}_{1},{H}_{2} \) are constants such that \( H\left( p\right)  < {H}_{1} < \; {H}_{2} < H\left( q\right) \)

Let \( \varphi \) and \( \psi \) be smooth real-valued functions on \( M \) , with \( \varphi \) compactly supported in \( U \) and \( \psi \) compactly supported in \( W \) , and satisfying \( {\int }_{U}{\varphi d}{V}_{g} = {\int }_{W}{\psi d}{V}_{g} = 1 \) . For sufficiently small \( s, t \in  \mathbb{R} \) , define a subset \( {D}_{s, t} \subseteq  \widetilde{M} \) as follows:

\[
{D}_{s, t} = \left\{  {z \in  \widetilde{U} : v\left( z\right)  \leq  {s\varphi }\left( {{x}^{1}\left( z\right) ,\ldots ,{x}^{n}\left( z\right) }\right) }\right\}
\]

\[
\cup  \left\{  {z \in  \widetilde{W} : w\left( z\right)  \leq  {t\psi }\left( {{y}^{1}\left( z\right) ,\ldots ,{y}^{n}\left( z\right) }\right) }\right\}
\]

\[
\cup  \left( {D \smallsetminus  \left( {\widetilde{U} \cup  \widetilde{W}}\right) }\right)
\]

and let \( {M}_{s, t} = \partial {D}_{s, t} \) , so \( {D}_{0,0} = D \) and \( {M}_{0,0} = M \) (see Fig. 8.3). For sufficiently small \( s \) and \( t \) , the set \( {D}_{s, t} \) is a regular domain and \( {M}_{s, t} \) is a compact smooth hypersurface, and \( \operatorname{Vol}\left( {D}_{s, t}\right) \) and \( \operatorname{Area}\left( {M}_{s, t}\right) \) are both smooth functions of \( \left( {s, t}\right) \) . For convenience, write \( V\left( {s, t}\right)  = \operatorname{Vol}\left( {D}_{s, t}\right) \) and \( A\left( {s, t}\right)  = \operatorname{Area}\left( {M}_{s, t}\right) \) .

The same argument that led to (8.18) shows that

\[
\frac{\partial A}{\partial s}\left( {0,0}\right)  =  - n{\int }_{U}{H\varphi d}{V}_{g},\;\frac{\partial A}{\partial t}\left( {0,0}\right)  =  - n{\int }_{W}{H\psi d}{V}_{g}.
\]

![bo_d7dtff491nqc73eq8m7g_253_499_188_532_531_0.jpg](images/bo_d7dtff491nqc73eq8m7g_253_499_188_532_531_0.jpg)

Fig. 8.3: The domain \( {D}_{s, t} \)

To compute the partial derivatives of the volume, we just note that if we hold \( t = 0 \) fixed and let \( s \) vary, the only change in volume occurs in the part of \( {D}_{s, t} \) contained in \( \widetilde{U} \) , so the fundamental theorem of calculus gives

\[
\frac{\partial V}{\partial s}\left( {0,0}\right)  = {\left. \frac{d}{ds}\right| }_{s = 0}\operatorname{Vol}\left( {{D}_{s,0} \cap  \widetilde{U}}\right)
\]

\[
= {\left. \frac{d}{ds}\right| }_{s = 0}{\int }_{U}\left( {{\int }_{-\varepsilon }^{{s\varphi }\left( x\right) }\sqrt{\det \widetilde{g}\left( {x, v}\right) }{dv}}\right) d{x}^{1}\cdots d{x}^{n}
\]

\[
= {\int }_{U}\left( {{\left. \frac{d}{ds}\right| }_{s = 0}{\int }_{-\varepsilon }^{{s\varphi }\left( x\right) }\sqrt{\det \widetilde{g}\left( {x, v}\right) }{dv}}\right) d{x}^{1}\cdots d{x}^{n}
\]

\[
= {\int }_{U}\varphi \left( x\right) \sqrt{\det \widetilde{g}\left( {x,0}\right) }d{x}^{1}\cdots d{x}^{n} = {\int }_{U}{\varphi d}{V}_{g} = 1,
\]

where the differentiation under the integral sign in the third line is justified just like (8.16), and in the last line we used the fact that \( {g}_{\alpha \beta }\left( x\right)  = {\widetilde{g}}_{\alpha \beta }\left( {x,0}\right) \) in these coordinates. Similarly, \( \partial V/\partial t\left( {0,0}\right)  = 1 \) .

Because \( V\left( {0,0}\right)  = \operatorname{Vol}\left( D\right) \) and \( \partial V/\partial t\left( {0,0}\right)  \neq  0 \) , the implicit function theorem guarantees that there is a smooth function \( \lambda  : \left( {-\delta ,\delta }\right)  \rightarrow  \mathbb{R} \) for some \( \delta  > 0 \) such that \( V\left( {s,\lambda \left( s\right) }\right)  \equiv  \operatorname{Vol}\left( D\right) \) . The chain rule then implies

\[
0 = {\left. \frac{d}{ds}\right| }_{s = 0}V\left( {s,\lambda \left( s\right) }\right)  = \frac{\partial V}{\partial s}\left( {0,0}\right)  + {\lambda }^{\prime }\left( 0\right) \frac{\partial V}{\partial t}\left( {0,0}\right)  = 1 + {\lambda }^{\prime }\left( 0\right) .
\]

Thus \( {\lambda }^{\prime }\left( 0\right)  =  - 1 \) .

Our hypothesis that \( M \) minimizes area implies that

\[
0 = {\left. \frac{d}{ds}\right| }_{s = 0}A\left( {s,\lambda \left( s\right) }\right)  = \frac{\partial A}{\partial s}\left( {0,0}\right)  + {\lambda }^{\prime }\left( 0\right) \frac{\partial A}{\partial t}\left( {0,0}\right)
\]

\[
=  - n{\int }_{U}{H\varphi d}{V}_{g} + n{\int }_{W}{H\psi d}{V}_{g},
\]

and thus \( {\int }_{U}{H\varphi d}{V}_{g} = {\int }_{W}{H\psi d}{V}_{g} \) . But our choice of \( U \) and \( V \) together with the fact that \( {\int }_{U}{\varphi d}{V}_{g} = {\int }_{W}{\psi d}{V}_{g} = 1 \) guarantees that \( {\int }_{U}{H\varphi d}{V}_{g} \leq  {H}_{1} < {H}_{2} \leq \; {\int }_{W}{H\psi d}{V}_{g} \) , which is a contradiction.

We do not pursue minimal or constant-mean-curvature hypersurfaces any further in this book, but you can find a good introductory treatment in [CM11].

## Hypersurfaces in Euclidean Space

Now we specialize even further, to hypersurfaces in Euclidean space. In this section, we assume that \( M \subseteq  {\mathbb{R}}^{n + 1} \) is an embedded \( n \) -dimensional submanifold with the induced Riemannian metric. The Euclidean metric will be denoted as usual by \( \bar{g} \) , and covariant derivatives and curvatures associated with \( \bar{g} \) will be indicated by a bar. The induced metric on \( M \) will be denoted by \( g \) .

In this setting, because \( \overline{Rm} \equiv  0 \) , the Gauss and Codazzi equations take even simpler forms:

\[
\frac{1}{2}h \oslash  h = {Rm} \tag{8.19}
\]

\[
{Dh} = 0\text{ , } \tag{8.20}
\]

or in terms of a local frame for \( M \) ,

\[
{h}_{il}{h}_{jk} - {h}_{ik}{h}_{jl} = {R}_{ijkl}, \tag{8.21}
\]

\[
{h}_{{ij};k} - {h}_{{ik};j} = 0. \tag{8.22}
\]

In particular, this means that the Riemann curvature tensor of a hypersurface in \( {\mathbb{R}}^{n + 1} \) is completely determined by the second fundamental form. A symmetric 2-tensor field that satisfies \( {Dh} = 0 \) is called a Codazzi tensor, so (8.20) can be expressed succinctly by saying that \( h \) is a Codazzi tensor.

Exercise 8.20. Show that a smooth 2-tensor field \( h \) on a Riemannian manifold is a Codazzi tensor if and only if both \( h \) and \( \nabla h \) are symmetric.

The equations (8.19)-(8.20) can be viewed as compatibility conditions for the existence of an embedding or immersion into Euclidean space with prescribed first and second fundamental forms. If \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold and \( h \) is a given smooth symmetric 2-tensor field on \( M \) , then Theorem 8.13 shows that these two equations are necessary conditions for the existence of an isometric immersion \( M \rightarrow  {\mathbb{R}}^{n + 1} \) for which \( h \) is the scalar second fundamental form. (Note that an immersion is locally an embedding, so the theorem applies in a neighborhood of each point.) It is a remarkable fact that the Gauss and Codazzi equations are actually sufficient, at least locally. A sketch of a proof of this fact, called the fundamental theorem of hypersurface theory, can be found in [Pet16, pp. 108-109].

![bo_d7dtff491nqc73eq8m7g_255_367_204_801_379_0.jpg](images/bo_d7dtff491nqc73eq8m7g_255_367_204_801_379_0.jpg)

Fig. 8.4: Geometric interpretation of \( h\left( {v, v}\right) \)

In the setting of a hypersurface \( M \subseteq  {\mathbb{R}}^{n + 1} \) , we can give some very concrete geometric interpretations of the quantities we have defined so far. We begin with curves. For every unit vector \( v \in  {T}_{p}M \) , let \( \gamma  = {\gamma }_{v} : I \rightarrow  M \) be the \( g \) -geodesic in \( M \) with initial velocity \( v \) . Then the Gauss formula shows that the ordinary Euclidean acceleration of \( \gamma \) at 0 is \( {\gamma }^{\prime \prime }\left( 0\right)  = {\bar{D}}_{t}{\gamma }^{\prime }\left( 0\right)  = h\left( {v, v}\right) {N}_{p} \) (Fig. 8.4). Thus \( \left| {h\left( {v, v}\right) }\right| \) is the Euclidean curvature of \( \gamma \) at 0, and \( h\left( {v, v}\right)  = \left\langle  {{\gamma }^{\prime \prime }\left( 0\right) ,{N}_{p}}\right\rangle   > 0 \) if and only if \( {\gamma }^{\prime \prime }\left( 0\right) \) points in the same direction as \( {N}_{p} \) . In other words, \( h\left( {v, v}\right) \) is positive if \( \gamma \) is curving in the direction of \( {N}_{p} \) , and negative if it is curving away from \( {N}_{p} \) .

The next proposition shows that this Euclidean curvature can be interpreted in terms of the radius of the "best circular approximation," as mentioned in Chapter 1.

Proposition 8.21. Suppose \( \gamma  : I \rightarrow  {\mathbb{R}}^{m} \) is a unit-speed curve, \( {t}_{0} \in  I \) , and \( \kappa \left( {t}_{0}\right)  \neq  0 \) .

(a) There is a unique unit-speed parametrized circle \( c : \mathbb{R} \rightarrow  {\mathbb{R}}^{m} \) , called the osculating circle at \( \gamma \left( {t}_{0}\right) \) , with the property that \( c \) and \( \gamma \) have the same position, velocity, and acceleration at \( t = {t}_{0} \) .

(b) The Euclidean curvature of \( \gamma \) at \( {t}_{0} \) is \( \kappa \left( {t}_{0}\right)  = 1/R \) , where \( R \) is the radius of the osculating circle.

Proof. An easy geometric argument shows that every circle in \( {\mathbb{R}}^{m} \) with center \( q \) and radius \( R \) has a unit-speed parametrization of the form

\[
c\left( t\right)  = q + R\cos \left( \frac{t - {t}_{0}}{R}\right) v + R\sin \left( \frac{t - {t}_{0}}{R}\right) w,
\]

where \( \left( {v, w}\right) \) is a pair of orthonormal vectors in \( {\mathbb{R}}^{m} \) . By direct computation, such a parametrization satisfies

\[
c\left( {t}_{0}\right)  = q + {Rv},\;{c}^{\prime }\left( {t}_{0}\right)  = w,\;{c}^{\prime \prime }\left( {t}_{0}\right)  =  - \frac{1}{R}v.
\]

Thus if we put

\[
R = \frac{1}{\left| {\gamma }^{\prime \prime }\left( {t}_{0}\right) \right| } = \frac{1}{\kappa \left( {t}_{0}\right) },\;v =  - R{\gamma }^{\prime \prime }\left( {t}_{0}\right) ,\;w = {\gamma }^{\prime }\left( {t}_{0}\right) ,\;q = \gamma \left( {t}_{0}\right)  - {Rv},
\]

we obtain a circle satisfying the required conditions, and its radius is equal to \( 1/\kappa \left( {t}_{0}\right) \) by construction. Uniqueness is left as an exercise.

- Exercise 8.22. Complete the proof of the preceding proposition by proving uniqueness of the osculating circle.

## Computations in Euclidean Space

When we wish to compute the invariants of a Euclidean hypersurface \( M \subseteq  {\mathbb{R}}^{n + 1} \) , it is usually unnecessary to go to all the trouble of computing Christoffel symbols. Instead, it is usually more effective to use either a defining function or a parametrization to compute the scalar second fundamental form, and then use (8.21) to compute the curvature. Here we describe several contexts in which this computation is not too hard.

Usually the computations are simplest if the hypersurface is presented in terms of a local parametrization. Suppose \( M \subseteq  {\mathbb{R}}^{n + 1} \) is a smooth embedded hypersurface, and let \( X : U \rightarrow  {\mathbb{R}}^{n + 1} \) be a smooth local parametrization of \( M \) . The coordinates \( \left( {{u}^{1},\ldots ,{u}^{n}}\right) \) on \( U \subseteq  {\mathbb{R}}^{n} \) thus give local coordinates for \( M \) . The coordinate vector fields \( {\partial }_{i} = \partial /\partial {u}^{i} \) push forward to vector fields \( {dX}\left( {\partial }_{i}\right) \) on \( M \) , which we can view as sections of the restricted tangent bundle \( {\left. T{\mathbb{R}}^{n + 1}\right| }_{M} \) , or equivalently as \( {\mathbb{R}}^{n + 1} \) -valued functions. If we think of \( X\left( u\right)  = \left( {{X}^{1}\left( u\right) ,\ldots ,{X}^{n + 1}\left( u\right) }\right) \) as a vector-valued function of \( u \) , these vectors can be written as

\[
d{X}_{u}\left( {\partial }_{i}\right)  = {\partial }_{i}X\left( u\right)  = \left( {{\partial }_{i}{X}^{1}\left( u\right) ,\ldots ,{\partial }_{i}{X}^{n + 1}\left( u\right) }\right) .
\]

For simplicity, write \( {X}_{i} = {\partial }_{i}X \) .

Once these vector fields are computed, a unit normal field can be computed as follows: Choose any coordinate vector field \( \partial /\partial {x}^{{j}_{0}} \) that is not contained in span \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) (there will always be one, at least in a neighborhood of each point). Then apply the Gram-Schmidt algorithm to the local frame \( \left( {{X}_{1},\ldots ,{X}_{n},\partial /\partial {x}^{{j}_{0}}}\right) \) along \( M \) to obtain an adapted orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{n + 1}}\right) \) . The two choices of unit normal are \( N =  \pm  {E}_{n + 1} \) .

The next proposition gives a formula for the second fundamental form that is often easy to use for computation.

Proposition 8.23. Suppose \( M \subseteq  {\mathbb{R}}^{n + 1} \) is an embedded hypersurface, \( X : U \rightarrow  M \) is a smooth local parametrization of \( M,\left( {{X}_{1},\ldots ,{X}_{n}}\right) \) is the local frame for \( {TM} \) determined by \( X \) , and \( N \) is a unit normal field on \( M \) . Then the scalar second fundamental form is given by

\[
h\left( {{X}_{i},{X}_{j}}\right)  = \left\langle  {\frac{{\partial }^{2}X}{\partial {u}^{i}\partial {u}^{j}}, N}\right\rangle  . \tag{8.23}
\]

Proof. Let \( {u}_{0} = \left( {{u}_{0}^{1},\ldots ,{u}_{0}^{n}}\right) \) be an arbitrary point of \( U \) and let \( p = X\left( {u}_{0}\right)  \in  M \) . For each \( i \in  \{ 1,\ldots , n\} \) , the curve \( \gamma \left( t\right)  = X\left( {{u}_{0}^{1},\ldots ,{u}_{0}^{i} + t,\ldots ,{u}_{0}^{n}}\right) \) is a smooth curve in \( M \) whose initial velocity is \( {X}_{i} \) . Regarding the normal field \( N \) as a smooth map from \( M \) to \( {\mathbb{R}}^{n + 1} \) , we have

\[
\frac{\partial }{\partial {u}^{i}}N\left( {X\left( {u}_{0}\right) }\right)  = {\left( N \circ  \gamma \right) }^{\prime }\left( 0\right)  = {\overline{\nabla }}_{{X}_{i}}N\left( {X\left( {u}_{0}\right) }\right) .
\]

Because \( {X}_{j} = \partial X/\partial {u}^{j} \) is tangent to \( M \) and \( N \) is normal, the following expression is zero for all \( u \in  U \) :

\[
\left\langle  {\frac{\partial X}{\partial {u}^{j}}\left( u\right) , N\left( {X\left( u\right) }\right) }\right\rangle  \text{ . }
\]

Differentiating with respect to \( {u}^{i} \) and using the product rule for ordinary inner products in \( {\mathbb{R}}^{n + 1} \) yields

\[
0 = \left\langle  {\frac{{\partial }^{2}X}{\partial {u}^{i}\partial {u}^{j}}\left( u\right) , N\left( {X\left( u\right) }\right) }\right\rangle   + \left\langle  {\frac{\partial X}{\partial {u}^{j}}\left( u\right) ,{\overline{\nabla }}_{{X}_{i}\left( u\right) }N\left( {X\left( u\right) }\right) }\right\rangle  .
\]

By the Weingarten equation (8.11), the last term on the right becomes

\[
\left\langle  {{X}_{j}\left( u\right) , - s\left( {{X}_{i}\left( u\right) }\right) }\right\rangle   =  - h\left( {{X}_{j}\left( u\right) ,{X}_{i}\left( u\right) }\right) .
\]

Inserting this above yields (8.23).

Here is an application of this formula: it shows how the principal curvatures give a concise description of the local shape of an embedded hypersurface by approximating the surface with the graph of a quadratic function.

Proposition 8.24. Suppose \( M \subseteq  {\mathbb{R}}^{n + 1} \) is a Riemannian hypersurface. Let \( p \in  M \) , and let \( {\kappa }_{1},\ldots ,{\kappa }_{n} \) denote the principal curvatures of \( M \) at \( p \) with respect to some choice of unit normal. Then there is an isometry \( \varphi  : {\mathbb{R}}^{n + 1} \rightarrow  {\mathbb{R}}^{n + 1} \) that takes \( p \) to the origin and takes a neighborhood of \( p \) in \( M \) to a graph of the form \( {x}^{n + 1} = \; f\left( {{x}^{1},\ldots ,{x}^{n}}\right) \) , where

\[
f\left( x\right)  = \frac{1}{2}\left( {{\kappa }_{1}{\left( {x}^{1}\right) }^{2} + \cdots  + {\kappa }_{n}{\left( {x}^{n}\right) }^{2}}\right)  + O\left( {\left| x\right| }^{3}\right) . \tag{8.24}
\]

Proof. Replacing \( M \) by its image under a translation and a rotation (which are Euclidean isometries), we may assume that \( p \) is the origin and \( {T}_{p}M \) is equal to the span of \( \left( {{\partial }_{1},\ldots ,{\partial }_{n}}\right) \) . Then after reflecting in the \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) -hyperplane if necessary, we may assume that the chosen unit normal is \( \left( {0,\ldots ,0,1}\right) \) . By an orthogonal transformation in the first \( n \) variables, we can also arrange that the scalar second fundamental form at 0 is diagonal with respect to the basis \( \left( {{\partial }_{1},\ldots ,{\partial }_{n}}\right) \) , with diagonal entries \( \left( {{\kappa }_{1},\ldots ,{\kappa }_{n}}\right) \) .

It follows from the implicit function theorem that there is some neighborhood \( U \) of 0 such that \( M \cap  U \) is the graph of a smooth function of the form \( {x}^{n + 1} = \; f\left( {{x}^{1},\ldots ,{x}^{n}}\right) \) with \( f\left( 0\right)  = 0 \) . A smooth local parametrization of \( M \) is then given by

\( X\left( u\right)  = \left( {{u}^{1},\ldots ,{u}^{n}, f\left( u\right) }\right) \) , and the fact that \( {T}_{0}M \) is spanned by \( \left( {\partial /\partial {x}^{1},\ldots ,\partial /\partial {x}^{n}}\right) \) guarantees that \( {\partial }_{1}f\left( 0\right)  = \cdots  = {\partial }_{n}f\left( 0\right)  = 0 \) . Because \( {X}_{i} = \partial /\partial {x}^{i} \) at 0, Proposition 8.23 then yields

\[
h\left( {\frac{\partial }{\partial {x}^{i}},\frac{\partial }{\partial {x}^{j}}}\right)  = \left\langle  {\left( {0,\ldots ,0,\frac{{\partial }^{2}f}{\partial {x}^{i}\partial {x}^{j}}\left( 0\right) }\right) ,\left( {0,\ldots ,0,1}\right) }\right\rangle   = \frac{{\partial }^{2}f}{\partial {x}^{i}\partial {x}^{j}}\left( 0\right) .
\]

It follows from our normalization that the matrix of second derivatives of \( f \) at 0 is diagonal, and its diagonal entries are the principal curvatures of \( M \) at that point. Then (8.24) follows from Taylor's theorem.

Here is another approach. When it is practical to write down a smooth vector field \( N = {N}^{i}{\partial }_{i} \) on an open subset of \( {\mathbb{R}}^{n + 1} \) that restricts to a unit normal vector field along \( M \) , then the shape operator can be computed straightforwardly using the Weingarten equation and observing that the Euclidean covariant derivatives of \( N \) are just ordinary directional derivatives in Euclidean space. Thus for every vector \( X = {X}^{j}{\partial }_{j} \) tangent to \( M \) , we have

\[
{sX} =  - {\overline{\nabla }}_{X}N =  - \mathop{\sum }\limits_{{i, j = 1}}^{{n + 1}}{X}^{j}\left( {{\partial }_{j}{N}^{i}}\right) {\partial }_{i}. \tag{8.25}
\]

One common way to produce such a smooth vector field is to work with a local defining function for \( M \) : Recall that this is a smooth real-valued function defined on some open subset \( U \subseteq  {\mathbb{R}}^{n + 1} \) such that \( U \cap  M \) is a regular level set of \( F \) (see Prop. A.27). The definition ensures that grad \( F \) (the gradient of \( F \) with respect to \( \bar{g} \) ) is nonzero on some neighborhood of \( M \cap  U \) , so a convenient choice for a unit normal vector field along \( M \) is

\[
N = \frac{\operatorname{grad}F}{\left| \operatorname{grad}F\right| }.
\]

Here is an application.

Example 8.25 (Shape Operators of Spheres). The function \( F : {\mathbb{R}}^{n + 1} \rightarrow  \mathbb{R} \) defined by \( F\left( x\right)  = {\left| x\right| }^{2} \) is a smooth defining function for each sphere \( {\mathbb{S}}^{n}\left( R\right) \) . The gradient of this function is grad \( F = 2\mathop{\sum }\limits_{i}{x}^{i}{\partial }_{i} \) , which has length \( {2R} \) along \( {\mathbb{S}}^{n}\left( R\right) \) . The smooth vector field

\[
N = \frac{1}{R}\mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{x}^{i}{\partial }_{i}
\]

thus restricts to a unit normal along \( {\mathbb{S}}^{n}\left( R\right) \) . (It is the outward pointing normal.) The shape operator is now easy to compute:

\[
{sX} =  - \frac{1}{R}\mathop{\sum }\limits_{{i, j = 1}}^{{n + 1}}{X}^{j}\left( {{\partial }_{j}{x}^{i}}\right) {\partial }_{i} =  - \frac{1}{R}X.
\]

Therefore \( s = \left( {-1/R}\right) \mathrm{{Id}} \) . The principal curvatures, therefore, are all equal to \( - 1/R \) , and it follows that the mean curvature is \( H =  - 1/R \) and the Gaussian curvature is \( {\left( -1/R\right) }^{n} \) .

For surfaces in \( {\mathbb{R}}^{3} \) , either of the above methods can be used. When a parametrization \( X \) is given, the normal vector field is particularly easy to compute: because \( {X}_{1} \) and \( {X}_{2} \) span the tangent space to \( M \) at each point, their cross product is a nonzero normal vector, so one choice of unit normal is

\[
N = \frac{{X}_{1} \times  {X}_{2}}{\left| {X}_{1} \times  {X}_{2}\right| } \tag{8.26}
\]

Problems 8-1, 8-2, and 8-3 will give you practice in carrying out these computations for surfaces presented in various ways.

## The Gaussian Curvature of a Surface Is Intrinsic

Because the Gaussian and mean curvatures are defined in terms of a particular embedding of \( M \) into \( {\mathbb{R}}^{n + 1} \) , there is little reason to suspect that they have much to do with the intrinsic Riemannian geometry of \( \left( {M, g}\right) \) . The next exercise illustrates the fact that the mean curvature has no intrinsic meaning.

Exercise 8.26. Let \( {M}_{1} \subseteq  {\mathbb{R}}^{3} \) be the plane \( \{ z = 0\} \) , and let \( {M}_{2} \subseteq  {\mathbb{R}}^{3} \) be the cylinder \( \left\{  {{x}^{2} + {y}^{2} = 1}\right\} \) . Show that \( {M}_{1} \) and \( {M}_{2} \) are locally isometric, but the former has mean curvature zero, while the latter has mean curvature \( \pm  \frac{1}{2} \) , depending on which normal is chosen.

The amazing discovery made by Gauss was that the Gaussian curvature of a surface in \( {\mathbb{R}}^{3} \) is actually an intrinsic invariant of the Riemannian manifold \( \left( {M, g}\right) \) . He was so impressed with this discovery that he called it Theorema Egregium, Latin for "excellent theorem."

Theorem 8.27 (Gauss's Theorema Egregium). Suppose \( \left( {M, g}\right) \) is an embedded 2-dimensional Riemannian submanifold of \( {\mathbb{R}}^{3} \) . For every \( p \in  M \) , the Gaussian curvature of \( M \) at \( p \) is equal to one-half the scalar curvature of \( g \) at \( p \) , and thus the Gaussian curvature is a local isometry invariant of \( \left( {M, g}\right) \) .

Proof. Let \( p \in  M \) be arbitrary, and choose an orthonormal basis \( \left( {{b}_{1},{b}_{2}}\right) \) for \( {T}_{p}M \) . In this basis \( g \) is represented by the identity matrix, and the shape operator has the same matrix as the scalar second fundamental form. Thus \( K\left( p\right)  = \det \left( {s}_{j}^{i}\right)  = \; \det \left( {h}_{ij}\right) \) , and the Gauss equation (8.21) reads

\[
R{m}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right)  = {h}_{11}{h}_{22} - {h}_{12}{h}_{21} = \det \left( {h}_{ij}\right)  = K\left( p\right) .
\]

On the other hand, Corollary 7.27 shows that \( {Rm} = \frac{1}{4}{Sg} \oslash  g \) , and thus by the definition of the Kulkarni-Nomizu product we have

\[
R{m}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right)  = \frac{1}{4}S\left( p\right) \left( {2{g}_{11}{g}_{22} - 2{g}_{12}{g}_{21}}\right)  = \frac{1}{2}S\left( p\right) .
\]

![bo_d7dtff491nqc73eq8m7g_260_257_187_1018_374_0.jpg](images/bo_d7dtff491nqc73eq8m7g_260_257_187_1018_374_0.jpg)

Fig. 8.5: A plane section

Motivated by the Theorema Egregium, for an abstract Riemannian 2-manifold \( \left( {M, g}\right) \) , not necessarily embedded in \( {\mathbb{R}}^{3} \) , we define the Gaussian curvature to be \( K = \frac{1}{2}S \) , where \( S \) is the scalar curvature. If \( M \) is a Riemannian submanifold of \( {\mathbb{R}}^{3} \) , then the Theorema Egregium shows that this new definition agrees with the original definition of \( K \) as the determinant of the shape operator. The following result is a restatement of Corollary 7.27 using this new definition.

Corollary 8.28. If \( \left( {M, g}\right) \) is a Riemannian 2-manifold, the following relationships hold:

\[
{Rm} = \frac{1}{2}{Kg} \oslash  g,\;{Rc} = {Kg},\;S = {2K}.
\]

## Sectional Curvatures

Now, finally, we can give a quantitative geometric interpretation to the curvature tensor in dimensions higher than 2. Suppose \( M \) is a Riemannian \( n \) -manifold (with \( n \geq  2), p \) is a point of \( M \) , and \( V \subseteq  {T}_{p}M \) is a star-shaped neighborhood of zero on which \( {\exp }_{p} \) is a diffeomorphism onto an open set \( U \subseteq  M \) . Let \( \Pi \) be any 2 - dimensional linear subspace of \( {T}_{p}M \) . Since \( \Pi  \cap  V \) is an embedded 2-dimensional submanifold of \( V \) , it follows that \( {S}_{\Pi } = {\exp }_{p}\left( {\Pi  \cap  V}\right) \) is an embedded 2-dimensional submanifold of \( U \subseteq  M \) containing \( p \) (Fig. 8.5), called the plane section determined by \( \Pi \) . Note that \( {S}_{\Pi } \) is just the set swept out by geodesics whose initial velocities lie in \( \Pi \) , and \( {T}_{p}{S}_{\Pi } \) is exactly \( \Pi \) .

We define the sectional curvature of \( \Pi \) , denoted by \( \sec \left( \Pi \right) \) , to be the intrinsic Gaussian curvature at \( p \) of the surface \( {S}_{\Pi } \) with the metric induced from the embedding \( {S}_{\Pi } \subseteq  M \) . If \( \left( {v, w}\right) \) is any basis for \( \Pi \) , we also use the notation \( \sec \left( {v, w}\right) \) for \( \sec \left( \Pi \right) \) .

The next theorem shows how to compute the sectional curvatures in terms of the curvature of \( \left( {M, g}\right) \) . To make the formula more concise, we introduce the following notation. Given vectors \( v, w \) in an inner product space \( V \) , we set

\[
\left| {v \land  w}\right|  = \sqrt{{\left| v\right| }^{2}{\left| w\right| }^{2}-\langle v, w{\rangle }^{2}}. \tag{8.27}
\]

It follows from the Cauchy-Schwarz inequality that \( \left| {v \land  w}\right|  \geq  0 \) , with equality if and only if \( v \) and \( w \) are linearly dependent, and \( \left| {v \land  w}\right|  = 1 \) when \( v \) and \( w \) are orthonormal. (One can define an inner product on the space \( {\Lambda }^{2}\left( V\right) \) of contravariant alternating 2-tensors, analogous to the inner product on forms defined in Problem 2-16, and this is the associated norm; see Problem 8-33(a).)

Proposition 8.29 (Formula for the Sectional Curvature). Let \( \left( {M, g}\right) \) be a Riemannian manifold and \( p \in  M \) . If \( v, w \) are linearly independent vectors in \( {T}_{p}M \) , then the sectional curvature of the plane spanned by \( v \) and \( w \) is given by

\[
\sec \left( {v, w}\right)  = \frac{R{m}_{p}\left( {v, w, w, v}\right) }{{\left| v \land  w\right| }^{2}}. \tag{8.28}
\]

Proof. Let \( \Pi  \subseteq  {T}_{p}M \) be the subspace spanned by \( \left( {v, w}\right) \) . For this proof, we denote the induced metric on \( {S}_{\Pi } \) by \( \widehat{g} \) , and its associated curvature tensor by \( \widehat{Rm} \) . By definition, \( \sec \left( {v, w}\right) \) is equal to \( \widehat{K}\left( p\right) \) , the Gaussian curvature of \( \widehat{g} \) at \( p \) .

We show first that the second fundamental form of \( {S}_{\Pi } \) in \( M \) vanishes at \( p \) . To see why, let \( z \in  \Pi \) be arbitrary, and let \( \gamma  = {\gamma }_{z} \) be the \( g \) -geodesic with initial velocity \( z \) , whose image lies in \( {S}_{\Pi } \) for \( t \) sufficiently near 0 . By the Gauss formula for vector fields along curves,

\[
0 = {D}_{t}{\gamma }^{\prime } = {\widehat{D}}_{t}{\gamma }^{\prime } + \mathrm{{II}}\left( {{\gamma }^{\prime },{\gamma }^{\prime }}\right) .
\]

Since the two terms on the right-hand side are orthogonal, each must vanish identically. Evaluating at \( t = 0 \) gives \( \coprod  \left( {z, z}\right)  = 0 \) . Since \( z \) was an arbitrary element of \( \Pi  = {T}_{p}\left( {S}_{\Pi }\right) \) and \( \Pi \) is symmetric, polarization shows that \( \Pi  = 0 \) at \( p \) . (We cannot in general expect II to vanish at other points of \( {S}_{\Pi } \) -it is only at \( p \) that all \( g \) -geodesics starting tangent to \( {S}_{\Pi } \) remain in \( {S}_{\Pi } \) .) The Gauss equation then tells us that the curvature tensors of \( M \) and \( {S}_{\Pi } \) are related at \( p \) by

\[
R{m}_{p}\left( {u, v, w, x}\right)  = {\widehat{Rm}}_{p}\left( {u, v, w, x}\right)
\]

whenever \( u, v, w, x \in  \Pi \) .

Now choose an orthonormal basis \( \left( {{b}_{1},{b}_{2}}\right) \) for \( \Pi \) . Based on the observations above, we see that the sectional curvature of \( \Pi \) is

\[
\widehat{K}\left( p\right)  = \frac{1}{2}\widehat{S}\left( p\right)
\]

\[
= \frac{1}{2}\mathop{\sum }\limits_{{i, j = 1}}^{2}{\widehat{Rm}}_{p}\left( {{b}_{i},{b}_{j},{b}_{j},{b}_{i}}\right)
\]

\[
= \frac{1}{2}{\widehat{Rm}}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right)  + \frac{1}{2}{\widehat{Rm}}_{p}\left( {{b}_{2},{b}_{1},{b}_{1},{b}_{2}}\right)
\]

\[
= {\widehat{Rm}}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right)  = R{m}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right) .
\]

To see how to compute this in terms of an arbitrary basis, let \( \left( {v, w}\right) \) be any basis for \( \Pi \) . The Gram-Schmidt algorithm yields an orthonormal basis as follows:

\[
{b}_{1} = \frac{v}{\left| v\right| }
\]

\[
{b}_{2} = \frac{w - \left\langle  {w,{b}_{1}}\right\rangle  {b}_{1}}{\left| w - \left\langle  w,{b}_{1}\right\rangle  {b}_{1}\right| }.
\]

Then by the preceding computation,

\[
\widehat{K}\left( p\right)  = R{m}_{p}\left( {{b}_{1},{b}_{2},{b}_{2},{b}_{1}}\right)
\]

\[
= R{m}_{p}\left( {\frac{v}{\left| v\right| },\frac{w - \left\langle  {w,{b}_{1}}\right\rangle  {b}_{1}}{\left| w - \left\langle  w,{b}_{1}\right\rangle  {b}_{1}\right| },\frac{w - \left\langle  {w,{b}_{1}}\right\rangle  {b}_{1}}{\left| w - \left\langle  w,{b}_{1}\right\rangle  {b}_{1}\right| },\frac{v}{\left| v\right| }}\right) \tag{8.29}
\]

\[
= \frac{R{m}_{p}\left( {v, w, w, v}\right) }{{\left| v\right| }^{2}{\left| w - \left\langle  w,{b}_{1}\right\rangle  {b}_{1}\right| }^{2}},
\]

where we have used the fact that \( \operatorname{Rm}\left( {v,{b}_{1},\cdot , \cdot  }\right)  = \operatorname{Rm}\left( {\cdot ,\cdot ,{b}_{1}, v}\right)  = 0 \) because \( {b}_{1} \) is a multiple of \( v \) . To simplify the denominator of this last expression, we substitute \( {b}_{1} = v/\left| v\right| \) to obtain

\[
{\left| v\right| }^{2}{\left| w - \left\langle  w,{b}_{1}\right\rangle  {b}_{1}\right| }^{2} = {\left| v\right| }^{2}\left( {{\left| w\right| }^{2} - 2\frac{\langle w, v{\rangle }^{2}}{{\left| v\right| }^{2}} + \frac{\langle w, v{\rangle }^{2}}{{\left| v\right| }^{2}}}\right)
\]

\[
= {\left| v\right| }^{2}{\left| w\right| }^{2} - \langle v, w{\rangle }^{2} = {\left| v \land  w\right| }^{2}.
\]

Inserting this into (8.29) proves the theorem.

Exercise 8.30. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( \widetilde{g} = {\lambda g} \) for some positive constant \( \lambda \) . Use Theorem 7.30 to prove that for every \( p \in  M \) and plane \( \Pi  \subseteq  {T}_{p}M \) , the sectional curvatures of \( \Pi \) with respect to \( \widetilde{g} \) and \( g \) are related by \( \widetilde{\sec }\left( \Pi \right)  = {\lambda }^{-1}\sec \left( \Pi \right) \) .

Proposition 8.29 shows that one important piece of quantitative information provided by the curvature tensor is that it encodes the sectional curvatures of all plane sections. It turns out, in fact, that this is all of the information contained in the curvature tensor: as the following proposition shows, the sectional curvatures completely determine the curvature tensor.

Proposition 8.31. Suppose \( {R}_{1} \) and \( {R}_{2} \) are algebraic curvature tensors on a finite-dimensional inner product space \( V \) . If for every pair of linearly independent vectors \( v, w \in  V, \)

\[
\frac{{R}_{1}\left( {v, w, w, v}\right) }{{\left| v \land  w\right| }^{2}} = \frac{{R}_{2}\left( {v, w, w, v}\right) }{{\left| v \land  w\right| }^{2}},
\]

then \( {R}_{1} = {R}_{2} \) .

Proof. Let \( {R}_{1} \) and \( {R}_{2} \) be tensors satisfying the hypotheses, and set \( D = {R}_{1} - {R}_{2} \) . Then \( D \) is an algebraic curvature tensor, and \( D\left( {v, w, w, v}\right)  = 0 \) for all \( v, w \in  V \) . (This is true by hypothesis when \( v \) and \( w \) are linearly independent, and it is true by the symmetries of \( D \) when they are not.) We need to show that \( D = 0 \) .

For all vectors \( v, w, x \) , the symmetries of \( D \) give

\[
0 = D\left( {v + w, x, x, v + w}\right)
\]

\[
= D\left( {v, x, x, v}\right)  + D\left( {v, x, x, w}\right)  + D\left( {w, x, x, v}\right)  + D\left( {w, x, x, w}\right)
\]

\[
= {2D}\left( {v, x, x, w}\right) \text{ . }
\]

From this it follows that

\[
0 = D\left( {v, x + u, x + u, w}\right)
\]

\[
= D\left( {v, x, x, w}\right)  + D\left( {v, x, u, w}\right)  + D\left( {v, u, x, w}\right)  + D\left( {v, u, u, w}\right)
\]

\[
= D\left( {v, x, u, w}\right)  + D\left( {v, u, x, w}\right) .
\]

Therefore \( D \) is antisymmetric in every adjacent pair of arguments. Now the algebraic Bianchi identity yields

\[
0 = D\left( {v, w, x, u}\right)  + D\left( {w, x, v, u}\right)  + D\left( {x, v, w, u}\right)
\]

\[
= D\left( {v, w, x, u}\right)  - D\left( {w, v, x, u}\right)  - D\left( {v, x, w, u}\right)
\]

\[
= {3D}\left( {v, w, x, u}\right) \text{ . }
\]

We can also give a geometric interpretation of the Ricci and scalar curvatures on a Riemannian manifold. Since the Ricci tensor is symmetric and bilinear, Lemma 8.11 shows that it is completely determined by its values of the form \( {Rc}\left( {v, v}\right) \) for unit vectors \( v \) .

Proposition 8.32 (Geometric Interpretation of Ricci and Scalar Curvatures). Let \( \left( {M, g}\right) \) be a Riemannian n-manifold and \( p \in  M \) .

(a) For every unit vector \( v \in  {T}_{p}M, R{c}_{p}\left( {v, v}\right) \) is the sum of the sectional curvatures of the 2-planes spanned by \( \left( {v,{b}_{2}}\right) ,\ldots ,\left( {v,{b}_{n}}\right) \) , where \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) is any orthonormal basis for \( {T}_{p}M \) with \( {b}_{1} = v \) .

(b) The scalar curvature at \( p \) is the sum of all sectional curvatures of the 2-planes spanned by ordered pairs of distinct basis vectors in any orthonormal basis.

Proof. Given any unit vector \( v \in  {T}_{p}M \) , let \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) be as in the hypothesis. Then \( R{c}_{p}\left( {v, v}\right) \) is given by

\[
R{c}_{p}\left( {v, v}\right)  = {R}_{11}\left( p\right)  = {R}_{k11}{}^{k}\left( p\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}R{m}_{p}\left( {{b}_{k},{b}_{1},{b}_{1},{b}_{k}}\right)  = \mathop{\sum }\limits_{{k = 2}}^{n}\sec \left( {{b}_{1},{b}_{k}}\right) .
\]

For the scalar curvature, we let \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) be any orthonormal basis for \( {T}_{p}M \) , and compute

\[
S\left( p\right)  = {R}_{j}{}^{j}\left( p\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}R{c}_{p}\left( {{b}_{j},{b}_{j}}\right)  = \mathop{\sum }\limits_{{j, k = 1}}^{n}R{m}_{p}\left( {{b}_{k},{b}_{j},{b}_{j},{b}_{k}}\right)
\]

\[
= \mathop{\sum }\limits_{{j \neq  k}}\sec \left( {{b}_{j},{b}_{k}}\right) .
\]

One consequence of this proposition is that if \( \left( {M, g}\right) \) is a Riemannian manifold in which all sectional curvatures are positive, then the Ricci and scalar curvatures are both positive as well. The analogous statement holds if "positive" is replaced by "negative," "nonpositive," or "nonnegative."

If the opposite sign convention is chosen for the curvature tensor, then the righthand side of formula (8.28) has to be adjusted accordingly, with \( R{m}_{p}\left( {v, w, v, w}\right) \) taking the place of \( R{m}_{p}\left( {v, w, w, v}\right) \) . This is so that whatever sign convention is chosen for the curvature tensor, the notion of positive or negative sectional, Ricci, or scalar curvature has the same meaning for everyone.

## Sectional Curvatures of the Model Spaces

We can now compute the sectional curvatures of our three families of frame-homogeneous model spaces. A Riemannian metric or Riemannian manifold is said to have constant sectional curvature if the sectional curvatures are the same for all planes at all points.

Lemma 8.33. If a Riemannian manifold \( \left( {M, g}\right) \) is frame-homogeneous, then it has constant sectional curvature.

Proof. Frame homogeneity implies, in particular, that given two 2-planes at the same or different points, there is an isometry taking one to the other. The result follows from the isometry invariance of the curvature tensor.

Thus to compute the sectional curvature of one of our model spaces, it suffices to compute the sectional curvature for one plane at one point in each space.

Theorem 8.34 (Sectional Curvatures of the Model Spaces). The following Riemannian manifolds have the indicated constant sectional curvatures:

(a) \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) has constant sectional curvature 0 .

(b) \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) has constant sectional curvature \( 1/{R}^{2} \) .

(c) \( \left( {{\mathbb{H}}^{n}\left( R\right) ,{\breve{g}}_{R}}\right) \) has constant sectional curvature \( - 1/{R}^{2} \) .

Proof. First we consider the simplest case: Euclidean space. Since the curvature tensor of \( {\mathbb{R}}^{n} \) is identically zero, clearly all sectional curvatures are zero. This is also easy to see geometrically, since each plane section is actually a plane, which has zero Gaussian curvature.

Next consider the sphere \( {\mathbb{S}}^{n}\left( R\right) \) . We need only compute the sectional curvature of the plane \( \Pi \) spanned by \( \left( {{\partial }_{1},{\partial }_{2}}\right) \) at the point \( \left( {0,\ldots ,0,1}\right) \) . The geodesics with initial velocities in \( \Pi \) are great circles in the \( \left( {{x}^{1},{x}^{2},{x}^{n + 1}}\right) \) subspace. Therefore \( {S}_{\Pi } \) is isometric to the round 2-sphere of radius \( R \) embedded in \( {\mathbb{R}}^{3} \) . As Example 8.25 showed, \( {\mathbb{S}}^{2}\left( R\right) \) has Gaussian curvature \( 1/{R}^{2} \) . Therefore \( {\mathbb{S}}^{n}\left( R\right) \) has constant sectional curvature equal to \( 1/{R}^{2} \) .

Finally, the proof for hyperbolic spaces is left to Problem 8-28.

Note that for every real number \( c \) , exactly one of the model spaces listed above has constant sectional curvature \( c \) . These spaces will play vital roles in our comparison and local-to-global theorems in the last two chapters of the book.

Exercise 8.35. Show that the metric on real projective space \( {\mathbb{{RP}}}^{n} \) defined in Example 2.34 has constant positive sectional curvature.

Since the sectional curvatures determine the curvature tensor, one would expect to have an explicit formula for the full curvature tensor when the sectional curvature is constant. Such a formula is provided in the following proposition.

Proposition 8.36. A Riemannian metric \( g \) has constant sectional curvature \( c \) if and only if its curvature tensor satisfies

\[
{Rm} = \frac{1}{2}{cg} \oslash  g.
\]

In this case, the Ricci tensor and scalar curvature of \( g \) are given by the formulas

\[
{Rc} = \left( {n - 1}\right) {cg};\;S = n\left( {n - 1}\right) c,
\]

and the Riemann curvature endomorphism is

\[
R\left( {v, w}\right) x = c\left( {\langle w, x\rangle v-\langle v, x\rangle w}\right) .
\]

In terms of any basis,

\[
{R}_{ijkl} = c\left( {{g}_{il}{g}_{jk} - {g}_{ik}{g}_{jl}}\right) ;\;{R}_{ij} = \left( {n - 1}\right) c{g}_{ij}.
\]

Proof. Problem 8-29.

The basic concepts of Riemannian metrics and sectional curvatures in arbitrary dimensions were introduced by Bernhard Riemann in a famous 1854 lecture at Göttingen University [Spi97, Vol. II, Chap. 4]. These were just a few of the seminal accomplishments in his tragically short life.

## Problems

8-1. Suppose \( U \) is an open set in \( {\mathbb{R}}^{n} \) and \( f : U \rightarrow  \mathbb{R} \) is a smooth function. Let \( M = \{ \left( {x, f\left( x\right) }\right)  : x \in  U\}  \subseteq  {\mathbb{R}}^{n + 1} \) be the graph of \( f \) , endowed with the induced Riemannian metric and upward unit normal (see Example 2.19).

(a) Compute the components of the shape operator in graph coordinates, in terms of \( f \) and its partial derivatives.

(b) Let \( M \subseteq  {\mathbb{R}}^{n + 1} \) be the \( n \) -dimensional paraboloid defined as the graph of \( f\left( x\right)  = {\left| x\right| }^{2} \) . Compute the principal curvatures of \( M \) .

(Used on p. 361.)

8-2. Let \( \left( {M, g}\right) \) be an embedded Riemannian hypersurface in a Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , let \( F \) be a local defining function for \( M \) , and let \( N = \) grad \( F/\left| {\operatorname{grad}F}\right| \) .

(a) Show that the scalar second fundamental form of \( M \) with respect to the unit normal \( N \) is given by

\[
h\left( {X, Y}\right)  =  - \frac{{\widetilde{\nabla }}^{2}F\left( {X, Y}\right) }{\left| \operatorname{grad}F\right| }
\]

for all \( X, Y \in  \mathfrak{X}\left( M\right) \) .

(b) Show that the mean curvature of \( M \) is given by

\[
H =  - \frac{1}{n}{\operatorname{div}}_{\widetilde{g}}\left( \frac{\operatorname{grad}F}{\left| \operatorname{grad}F\right| }\right) ,
\]

where \( n = \dim M \) and \( {\operatorname{div}}_{\widetilde{g}} \) is the divergence operator of \( \widetilde{g} \) (see Problem 5-14). [Hint: First prove the following linear-algebra lemma: If \( V \) is a finite-dimensional inner product space, \( w \in  V \) is a unit vector, and \( A : V \rightarrow  V \) is a linear map that takes \( {w}^{ \bot  } \) to \( {w}^{ \bot  } \) , then \( \operatorname{tr}\left( {\left. A\right| }_{{w}^{ \bot  }}\right)  = \operatorname{tr}B \) , where \( B : V \rightarrow  V \) is defined by \( {Bx} = {Ax} - \langle x, w\rangle {Aw} \) .]

8-3. Let \( C \) be an embedded smooth curve in the half-plane \( H = \{ \left( {r, z}\right)  : r > 0\} \) , and let \( {S}_{C} \subseteq  {\mathbb{R}}^{3} \) be the surface of revolution determined by \( C \) as in Example 2.20. Let \( \gamma \left( t\right)  = \left( {a\left( t\right) , b\left( t\right) }\right) \) be a unit-speed local parametrization of \( C \) , and let \( X \) be the local parametrization of \( {S}_{C} \) given by (2.11).

(a) Compute the shape operator and principal curvatures of \( {S}_{C} \) in terms of \( a \) and \( b \) , and show that the principal directions at each point are tangent to the meridians and latitude circles.

(b) Show that the Gaussian curvature of \( {S}_{C} \) at a point \( X\left( {t,\theta }\right) \) is equal to \( - {a}^{\prime \prime }\left( t\right) /a\left( t\right) \) .

8-4. Show that there is a surface of revolution in \( {\mathbb{R}}^{3} \) that has constant Gaussian curvature equal to 1 but does not have constant principal curvatures. [Remark: We will see in Chapter 10 that this surface is locally isometric to \( {\mathbb{S}}^{2} \) (see Cor. 10.15), so this gives an example of two nonflat hypersurfaces in \( {\mathbb{R}}^{3} \) that are locally isometric but have different principal curvatures.]

8-5. Let \( S \subseteq  {\mathbb{R}}^{3} \) be the paraboloid given by \( z = {x}^{2} + {y}^{2} \) , with the induced metric. Prove that \( S \) is isotropic at only one point. (Used on p. 56.)

8-6. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, and \( \gamma  : I \rightarrow  M \) is a regular (but not necessarily unit-speed) curve in \( M \) . Show that the geodesic curvature of \( \gamma \) at \( t \in  I \) is

\[
\kappa \left( t\right)  = \frac{\left| {\gamma }^{\prime }\left( t\right)  \land  {D}_{t}{\gamma }^{\prime }\left( t\right) \right| }{{\left| {\gamma }^{\prime }\left( t\right) \right| }^{3}},
\]

where the norm in the numerator is the one defined by (8.27). Show also that in \( {\mathbb{R}}^{3} \) with the Euclidean metric, the formula can be written

\[
\kappa \left( t\right)  = \frac{\left| {\gamma }^{\prime }\left( t\right)  \times  {\gamma }^{\prime \prime }\left( t\right) \right| }{{\left| {\gamma }^{\prime }\left( t\right) \right| }^{3}}.
\]

8-7. For \( w > 0 \) , let \( {M}_{w} \subseteq  {\mathbb{R}}^{3} \) be the surface of revolution obtained by revolving the curve \( \gamma \left( t\right)  = \left( {w\cosh \left( {t/w}\right) , t}\right) \) around the \( z \) -axis, called a catenoid. Show that \( {M}_{w} \) is a minimal surface for each \( w \) .

8-8. For \( h > 0 \) , let \( {C}_{h} \subseteq  {\mathbb{R}}^{3} \) be the one-dimensional submanifold \( \left\{  {\left( {x, y, z}\right)  : {x}^{2} + }\right. \; \left. {{y}^{2} = 1, z =  \pm  h}\right\} \) ; it is the union of two unit circles lying in the \( z =  \pm  h \) planes. Let \( {h}_{0} = 1/\sinh c \) , where \( c \) is the unique positive solution to the equation \( c\tanh c = 1 \) . Prove that if \( h < {h}_{0} \) , then there are two distinct positive values \( {w}_{1} < {w}_{2} \) such that the portions of the catenoids \( {M}_{{w}_{1}} \) and \( {M}_{{w}_{2}} \) lying in the region \( \left| z\right|  \leq  h \) are minimal surfaces with boundary \( {C}_{h} \) (using the notation of Problem 8-7), while if \( h = {h}_{0} \) , there is exactly one such value, and if \( h > {h}_{0} \) , there are none. [Remark: This phenomenon can be observed experimentally. If you dip two parallel wire circles into soapy water, as long as they are close together they will form an area-minimizing soap film in the shape of a portion of a catenoid (the one with the larger "waist," \( {M}_{{w}_{2}} \) in the notation above). As you pull the circles apart, the "waist" of the catenoid gets smaller, until the ratio of the distance between the circles to their diameter reaches \( {h}_{0} \approx  {0.6627} \) , at which point the film will burst and the only soap film that can be formed is two disjoint flat disks.]

8-9. Let \( M \subseteq  {\mathbb{R}}^{n + 1} \) be a Riemannian hypersurface, and let \( N \) be a smooth unit normal vector field along \( M \) . At each point \( p \in  M,{N}_{p} \in  {T}_{p}{\mathbb{R}}^{n + 1} \) can be thought of as a unit vector in \( {\mathbb{R}}^{n + 1} \) and therefore as a point in \( {\mathbb{S}}^{n} \) . Thus each choice of unit normal vector field defines a smooth map \( v : M \rightarrow  {\mathbb{S}}^{n} \) , called the Gauss map of \( M \) . Show that \( {v}^{ * }d{V}_{g}^{ \circ  } = {\left( -1\right) }^{n}{Kd}{V}_{g} \) , where \( K \) is the Gaussian curvature of \( M \) .

8-10. Suppose \( g = {g}_{1} \oplus  {g}_{2} \) is a product metric on \( {M}_{1} \times  {M}_{2} \) as in (2.12). (See also Problem 7-6.)

(a) Show that for each point \( {p}_{i} \in  {M}_{i} \) , the submanifolds \( {M}_{1} \times  \left\{  {p}_{2}\right\} \) and \( \left\{  {p}_{1}\right\}   \times  {M}_{2} \) are totally geodesic.

(b) Show that \( \sec \left( \Pi \right)  = 0 \) for every 2-plane \( \Pi  \subseteq  {T}_{\left( {p}_{1},{p}_{2}\right) }\left( {{M}_{1} \times  {M}_{2}}\right) \) spanned by \( {v}_{1} \in  {T}_{{p}_{1}}{M}_{1} \) and \( {v}_{2} \in  {T}_{{p}_{2}}{M}_{2} \) .

(c) Show that if \( {M}_{1} \) and \( {M}_{2} \) both have nonnegative sectional curvature, then \( {M}_{1} \times  {M}_{2} \) does too; and if \( {M}_{1} \) and \( {M}_{2} \) both have nonpositive sectional curvature, then \( {M}_{1} \times  {M}_{2} \) does too.

(d) Now suppose \( \left( {{M}_{i},{g}_{i}}\right) \) has constant sectional curvature \( {c}_{i} \) for \( i = 1,2 \) ; let \( {n}_{i} = \dim {M}_{i} \) . Show that \( \left( {M, g}\right) \) is Einstein if and only if \( {c}_{1}\left( {{n}_{1} - 1}\right)  = \; {c}_{2}\left( {{n}_{2} - 1}\right) \) ; and \( \left( {M, g}\right) \) has constant sectional curvature if and only if \( {n}_{1} = {n}_{2} = 1 \) or \( {c}_{1} = {c}_{2} = 0 \) .

(Used on p. 366.)

8-11. Suppose \( M \subseteq  {\mathbb{R}}^{3} \) is a smooth surface, \( p \in  M \) , and \( {N}_{p} \) is a normal vector to \( M \) at \( p \) . Show that if \( \Pi  \subseteq  {\mathbb{R}}^{3} \) is any affine plane containing \( p \) and parallel to \( {N}_{p} \) , then there is a neighborhood \( U \) of \( p \) in \( {\mathbb{R}}^{3} \) such that \( M \cap  \Pi  \cap  U \) is a smooth embedded curve in \( \Pi \) , and the principal curvatures of \( M \) at \( p \) are equal to the minimum and maximum signed Euclidean curvatures of these curves as \( \Pi \) varies. [Remark: This justifies the informal recipe for computing principal curvatures given in Chapter 1.]

8-12. Suppose \( \pi  : \left( {\widetilde{M},\widetilde{g}}\right)  \rightarrow  \left( {M, g}\right) \) is a Riemannian submersion, and \( \left( {\widetilde{M},\widetilde{g}}\right) \) has all sectional curvatures bounded below by a constant \( c \) . Use O’Neill’s formula (Problem 7-14) to show that the sectional curvatures of \( \left( {M, g}\right) \) are bounded below by the same constant.

8-13. Let \( p : {\mathbb{S}}^{{2n} + 1} \rightarrow  {\mathbb{{CP}}}^{n} \) be the Riemannian submersion described in Example 2.30. In this problem, we identify \( {\mathbb{C}}^{n + 1} \) with \( {\mathbb{R}}^{{2n} + 2} \) by means of coordinates \( \left( {{x}^{1},{y}^{1},\ldots ,{x}^{n + 1},{y}^{n + 1}}\right) \) defined by \( {z}^{j} = {x}^{j} + i{y}^{j} \) .

(a) Show that the vector field

\[
S = {x}^{j}\frac{\partial }{\partial {y}^{j}} - {y}^{j}\frac{\partial }{\partial {x}^{j}}
\]

on \( {\mathbb{C}}^{n + 1} \) is tangent to \( {\mathbb{S}}^{{2n} + 1} \) and spans the vertical space \( {V}_{z} \) at each point \( z \in  {\mathbb{S}}^{{2n} + 1} \) . (The implicit summation here is from 1 to \( n + 1 \) .)

(b) Show that for all horizontal vector fields \( W, Z \) on \( {\mathbb{S}}^{{2n} + 1} \) ,

\[
{\left\lbrack  W, Z\right\rbrack  }^{V} =  - {d\omega }\left( {W, Z}\right) S = 2\langle W,{JZ}\rangle S,
\]

where \( \omega \) is the 1 -form on \( {\mathbb{C}}^{n + 1} \) given by

\[
\omega  = {S}^{b} = \mathop{\sum }\limits_{j}{x}^{j}d{y}^{j} - {y}^{j}d{x}^{j},
\]

and \( J : T{\mathbb{C}}^{n + 1} \rightarrow  T{\mathbb{C}}^{n + 1} \) is the real-linear orthogonal map given by

\[
J\left( {{a}^{j}\frac{\partial }{\partial {x}^{j}} + {b}^{j}\frac{\partial }{\partial {y}^{j}}}\right)  = {a}^{j}\frac{\partial }{\partial {y}^{j}} - {b}^{j}\frac{\partial }{\partial {x}^{j}}.
\]

(This is just multiplication by \( i = \sqrt{-1} \) in complex coordinates. Notice that \( J \circ  J =  - \mathrm{{Id}} \) .)

(c) Using O'Neill's formula (Problem 7-14), show that the curvature tensor of \( {\mathbb{{CP}}}^{n} \) satisfies

\[
{Rm}\left( {w, x, y, z}\right)  = \langle \widetilde{w},\widetilde{z}\rangle \langle \widetilde{x},\widetilde{y}\rangle  - \langle \widetilde{w},\widetilde{y}\rangle \langle \widetilde{x},\widetilde{z}\rangle
\]

\[
- 2\langle \widetilde{w}, J\widetilde{x}\rangle \langle \widetilde{y}, J\widetilde{z}\rangle  - \langle \widetilde{w}, J\widetilde{y}\rangle \langle \widetilde{x}, J\widetilde{z}\rangle
\]

\[
+ \langle \widetilde{w}, J\widetilde{z}\rangle \langle \widetilde{x}, J\widetilde{y}\rangle
\]

for every \( q \in  {\mathbb{{CP}}}^{n} \) and \( w, x, y, z \in  {T}_{q}{\mathbb{{CP}}}^{n} \) , where \( \widetilde{w},\widetilde{x},\widetilde{y},\widetilde{z} \) are horizontal lifts of \( w, x, y, z \) to an arbitrary point \( \widetilde{q} \in  {p}^{-1}\left( q\right)  \subseteq  {\mathbb{S}}^{{2n} + 1} \) .

(d) Using the notation of part (c), show that for orthonormal vectors \( w, x \in \; {T}_{q}{\mathbb{{CP}}}^{n} \) , the sectional curvature of the plane spanned by \( \{ w, x\} \) is

\[
\sec \left( {w, x}\right)  = 1 + 3\langle \widetilde{w}, J\widetilde{x}{\rangle }^{2}.
\]

(e) Show that for \( n \geq  2 \) , the sectional curvatures at each point of \( {\mathbb{{CP}}}^{n} \) take on all values between 1 and 4, inclusive, and conclude that \( {\mathbb{{CP}}}^{n} \) is not frame-homogeneous.

(f) Compute the Gaussian curvature of \( {\mathbb{{CP}}}^{1} \) .

(Used on pp. 56, 262, 367.)

8-14. Show that a Riemannian 3-manifold is Einstein if and only if it has constant sectional curvature.

8-15. Suppose \( \left( {M, g}\right) \) is a 3-dimensional Riemannian manifold that is homogeneous and isotropic. Show that \( g \) has constant sectional curvature. Show that the analogous result in dimension 4 is not true. [Hint: See Problem 8-13.]

8-16. For each \( a > 0 \) , let \( {g}_{a} \) be the Berger metric on \( \mathrm{{SU}}\left( 2\right) \) defined in Problem 3-10. Compute the sectional curvatures with respect to \( {g}_{a} \) of the planes spanned by \( \left( {X, Y}\right) ,\left( {Y, Z}\right) \) , and \( \left( {Z, X}\right) \) . Prove that if \( a \neq  1 \) , then \( \left( {\mathrm{{SU}}\left( 2\right) ,{g}_{a}}\right) \) is homogeneous but not isotropic anywhere. (Used on p. 56.)

8-17. Let \( G \) be a Lie group with a bi-invariant metric \( g \) (see Problem 7-13).

(a) Suppose \( X \) and \( Y \) are orthonormal elements of \( \operatorname{Lie}\left( G\right) \) . Show that \( \sec \left( {{X}_{p},{Y}_{p}}\right)  = \frac{1}{4}{\left| \left\lbrack  X, Y\right\rbrack  \right| }^{2} \) for each \( p \in  G \) , and conclude that the sectional curvatures of \( \left( {G, g}\right) \) are all nonnegative.

(b) Show that every Lie subgroup of \( G \) is totally geodesic in \( G \) .

(c) Now suppose \( G \) is connected. Show that \( G \) is flat if and only if it is abelian.

(Used on p. 282.)

8-18. Suppose \( \left( {M, g}\right) \) is a Riemannian hypersurface in a Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , and \( N \) is a unit normal vector field along \( M \) . We say that \( M \) is convex (with respect to \( N \) ) if its scalar second fundamental form satisfies \( h\left( {v, v}\right)  \leq  0 \) for all \( v \in  {TM} \) . Show that if \( M \) is convex and \( \widetilde{M} \) has sectional curvatures bounded below by a constant \( c \) , then all sectional curvatures of \( M \) are bounded below by \( c \) .

8-19. Suppose \( \left( {M, g}\right) \) is a Riemannian hypersurface in an \( \left( {n + 1}\right) \) -dimensional Lorentz manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) , and \( N \) is a smooth unit normal vector field along \( M \) . Define the scalar second fundamental form \( h \) and the shape operator \( s \) by requiring that \( \mathrm{{II}}\left( {X, Y}\right)  = h\left( {X, Y}\right) N \) and \( \langle {sX}, Y\rangle  = h\left( {X, Y}\right) \) for all \( X, Y \in \; \mathcal{X}\left( M\right) \) . Prove the following Lorentz analogues of the formulas of Theorem 8.13 (with notation as in that theorem):

(a) GAUSS FORMULA: \( {\widetilde{\nabla }}_{X}Y = {\nabla }_{X}Y + h\left( {X, Y}\right) N \) .

(b) GAUSS FORMULA FOR A CURVE: \( {\widetilde{D}}_{t}X = {D}_{t}X + h\left( {{\gamma }^{\prime }, X}\right) N \) .

(c) WEINGARTEN EQUATION: \( {\widetilde{\nabla }}_{X}N = {sX} \) .

(d) GAUSS EQUATION: \( \widetilde{Rm}\left( {W, X, Y, Z}\right)  = \left( {{Rm} + \frac{1}{2}h \odot  h}\right) \left( {W, X, Y, Z}\right) \) .

(e) CODAZZI EQUATION: \( \widetilde{Rm}\left( {W, X, Y, N}\right)  =  - \left( {Dh}\right) \left( {Y, W, X}\right) \) .

8-20. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is an \( \left( {n + 1}\right) \) -dimensional Lorentz manifold, and assume that \( \widetilde{g} \) satisfies the Einstein field equation with a cosmological constant: \( \widetilde{Rc} - \frac{1}{2}\widetilde{S}\widetilde{g} + \Lambda \widetilde{g} = T \) , where \( \Lambda \) is a constant and \( T \) is a smooth symmetric 2-tensor field (see p. 211). Let \( \left( {M, g}\right) \) be a Riemannian hypersurface in \( \widetilde{M} \) , and let \( h \) be its scalar second fundamental form as defined in Problem 8-19. Use the results of Problem 8-19 to show that \( g \) and \( h \) satisfy the following Einstein constraint equations on \( M \) :

\[
S - {2\Lambda } - {\left| h\right| }_{g}^{2} + {\left( {\operatorname{tr}}_{g}h\right) }^{2} = {2\rho },
\]

\[
\operatorname{div}h - d\left( {{\operatorname{tr}}_{g}h}\right)  = J
\]

where \( S \) is the scalar curvature of \( g \) , div \( h \) the divergence of \( h \) with respect to \( g \) as defined in Problem 5-16, \( \rho \) is the function \( \rho  = T\left( {N, N}\right) \) , and \( J \) is the 1-form \( J\left( X\right)  = T\left( {N, X}\right) \) . [Remark: When \( J \) and \( \rho \) are both zero, these equations, known as the vacuum Einstein constraint equations, are necessary conditions for \( g \) and \( h \) to be the metric and second fundamental form of a Riemannian hypersurface in an \( \left( {n + 1}\right) \) -dimensional Lorentz manifold satisfying the vacuum Einstein field equation with cosmological constant \( \Lambda \) . It was proved in 1950 by Yvonne Choquet-Bruhat that these conditions are also sufficient; for a proof, see [CB09, pp. 166-168].]

8-21. For every linear endomorphism \( A : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) , the associated quadratic form is the function \( Q : {\mathbb{R}}^{n} \rightarrow  \mathbb{R} \) defined by \( Q\left( x\right)  = \langle {Ax}, x\rangle \) . Prove that

\[
{\int }_{{\mathbb{S}}^{n - 1}}{Qd}{V}_{\overset{ \circ  }{g}} = \frac{1}{n}\left( {\operatorname{tr}A}\right) \operatorname{Vol}\left( {\mathbb{S}}^{n - 1}\right) .
\]

[Hint: Show that \( {\int }_{{\mathbb{S}}^{n - 1}}{x}^{i}{x}^{j}d{V}_{g}^{ \circ  } = 0 \) when \( i \neq  j \) by examining the effect of the isometry

\[
\left( {{x}^{1},\ldots ,{x}^{i},\ldots ,{x}^{j},\ldots ,{x}^{n}}\right)  \mapsto  \left( {{x}^{1},\ldots ,{x}^{j},\ldots , - {x}^{i},\ldots ,{x}^{n}}\right) ,
\]

and compute \( {\int }_{{\mathbb{S}}^{n - 1}}{\left( {x}^{i}\right) }^{2}d{V}_{g} \) using the fact that \( \mathop{\sum }\limits_{i}{\left( {x}^{i}\right) }^{2} = 1 \) on the sphere.] [Remark: It is a standard fact of linear algebra that the trace of \( A \) is independent of the choice of basis. This gives a geometric interpretation to the trace as \( n \) times the average value of the associated quadratic form \( Q \) .] (Used on p. 313.)

8-22. Let \( \left( {M, g}\right) \) be a Riemannian \( n \) -manifold and \( p \in  M \) . Proposition 8.32 gave a geometric interpretation of the Ricci curvature at \( p \) based on a choice of orthonormal basis. This problem describes an interpretation that does not refer to a basis. For each unit vector \( v \in  {T}_{p}M \) , prove that

\[
R{c}_{p}\left( {v, v}\right)  = \frac{n - 1}{\operatorname{Vol}\left( {\mathbb{S}}^{n - 2}\right) }{\int }_{w \in  {S}_{v}^{ \bot  }}\sec \left( {v, w}\right) d{V}_{\widehat{g}},
\]

where \( {S}_{v}^{ \bot  } \) denotes the set of unit vectors in \( {T}_{p}M \) that are orthogonal to \( v \) and \( \widehat{g} \) denotes the Riemannian metric on \( {S}_{v}^{ \bot  } \) induced from the flat metric \( {g}_{p} \) on \( {T}_{p}M \) . [Hint: Use Problem 8-21.]

8-23. Suppose \( \left( {M, g}\right) \) is a connected \( n \) -dimensional Riemannian manifold, and a Lie group \( G \) acts isometrically and effectively on \( M \) . Problem 5-12 showed that \( \dim G \leq  n\left( {n + 1}\right) /2 \) . Prove that if equality holds, then \( g \) has constant sectional curvature.

8-24. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold. Recall the definition of \( k \) -point homogeneous from Problem 6-18. Prove the following:

(a) If \( \left( {M, g}\right) \) is homogeneous, then it has constant scalar curvature.

(b) If \( \left( {M, g}\right) \) is 2-point homogeneous, then it is Einstein.

(c) If \( \left( {M, g}\right) \) is 3-point homogeneous, then it has constant sectional curvature.

8-25. For \( i = 1,2 \) , suppose \( \left( {{M}_{i},{g}_{i}}\right) \) is a Riemannian manifold of dimension \( {n}_{i} \geq \) 2 with constant sectional curvature \( {c}_{i} \) ; and let \( g = {g}_{1} \oplus  {g}_{2} \) be the product metric on \( M = {M}_{1} \times  {M}_{2} \) . Show that the Weyl tensor of \( g \) is given by

\[
W = \frac{{c}_{1} + {c}_{2}}{2\left( {n - 1}\right) \left( {n - 2}\right) }\left( {{n}_{2}\left( {{n}_{2} - 1}\right) {h}_{1} \oslash  {h}_{1}}\right.
\]

\[
\left. {-2\left( {{n}_{1} - 1}\right) \left( {{n}_{2} - 1}\right) {h}_{1} \oslash  {h}_{2} + {n}_{1}\left( {{n}_{1} - 1}\right) {h}_{2} \oslash  {h}_{2}}\right) \text{ , }
\]

where \( n = {n}_{1} + {n}_{2} \) and \( {h}_{i} = {\pi }_{i}^{ * }{g}_{i} \) for \( i = 1,2 \) . Conclude that \( \left( {M, g}\right) \) is locally conformally flat if and only if \( {c}_{2} =  - {c}_{1} \) . (See also Problem 7-6.) (Used on p. 67.)

8-26. Let \( \left( {M, g}\right) \) be a 4-dimensional Riemannian manifold. Given \( p \in  M \) and an orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) , prove that the Weyl tensor at \( p \) satisfies

\[
{W}_{1221} = \frac{1}{3}\left( {{k}_{12} + {k}_{34}}\right)  - \frac{1}{6}\left( {{k}_{13} + {k}_{14} + {k}_{23} + {k}_{24}}\right) ,
\]

where \( {k}_{ij} \) is the sectional curvature of the plane spanned by \( \left( {{b}_{i},{b}_{j}}\right) \) .

8-27. Prove that the Fubini-Study metric on \( {\mathbb{{CP}}}^{2} \) is not locally conformally flat. [Hint: Use Problems 8-13 and 8-26.]

8-28. Complete the proof of Theorem 8.34 by showing in two ways that the hyperbolic space of radius \( R \) has constant sectional curvature equal to \( - 1/{R}^{2} \) .

(a) In the hyperboloid model, compute the second fundamental form of \( {\mathbb{H}}^{n}\left( R\right)  \subseteq  {\mathbb{R}}^{n,1} \) at the point \( \left( {0,\ldots ,0, R}\right) \) , and use either the general form of the Gauss equation (Thm. 8.5) or the formulas of Problem 8-19.

(b) In the Poincaré ball model, use formula (7.44) for the conformal transformation of the curvature to compute the Riemann curvature tensor at the origin.

8-29. Prove Proposition 8.36 (curvature tensors on constant-curvature spaces).

8-30. Suppose \( M \subseteq  {\mathbb{R}}^{n + 1} \) is a hypersurface with the induced Riemannian metric. Show that the Ricci tensor of \( M \) satisfies

\[
\operatorname{Rc}\left( {v, w}\right)  = \left\langle  {{nHsv} - {s}^{2}v, w}\right\rangle  ,
\]

where \( H \) and \( s \) are the mean curvature and shape operator of \( M \) , respectively, and \( {s}^{2}v = s\left( {sv}\right) \) .

8-31. For \( 1 < k \leq  n \) , show that any \( k \) points in the hyperbolic space \( {\mathbb{H}}^{n}\left( R\right) \) lie in a totally geodesic \( \left( {k - 1}\right) \) -dimensional submanifold, which is isometric to \( {\mathbb{H}}^{k - 1}\left( R\right) \) .

8-32. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( G \) is a Lie group acting smoothly and isometrically on \( M \) . Let \( S \subseteq  M \) be the fixed point set of \( G \) , that is, the set of points \( p \in  M \) such that \( \varphi \left( p\right)  = p \) for all \( \varphi  \in  G \) . Show that each connected component of \( S \) is a smoothly embedded totally geodesic submanifold of \( M \) . (The reason for restricting to a single connected component is that different components may have different dimensions.)

8-33. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold. Let \( {\Lambda }^{2}\left( {TM}\right) \) denote the bundle of 2-vectors (alternating contravariant 2-tensors) on \( M \) .

(a) Show that there is a unique fiber metric on \( {\Lambda }^{2}\left( {TM}\right) \) whose associated norm satisfies

\[
{\left| w \land  x\right| }^{2} = {\left| w\right| }^{2}{\left| x\right| }^{2} - \langle w, x{\rangle }^{2}
\]

for all tangent vectors \( w, x \) at every point \( q \in  M \) .

(b) Show that there is a unique bundle endomorphism \( \mathcal{R} : {\Lambda }^{2}\left( {TM}\right)  \rightarrow \; {\Lambda }^{2}\left( {TM}\right) \) , called the curvature operator of \( g \) , that satisfies

\[
\langle \mathcal{R}\left( {w \land  x}\right) , y \land  z\rangle  =  - \operatorname{Rm}\left( {w, x, y, z}\right) \tag{8.30}
\]

for all tangent vectors \( w, x, y, z \) at a point of \( M \) , where the inner product on the left-hand side is the one described in part (a).

(c) A Riemannian metric is said to have positive curvature operator if \( \mathcal{R} \) is positive definite, and negative curvature operator if \( \mathcal{R} \) is negative definite. Show that positive curvature operator implies positive sectional curvature, and negative curvature operator implies negative sectional curvature. [Remark: This is the reason for the negative sign in (8.30). If the Riemann curvature tensor is defined as the negative of ours, the negative sign should be omitted.]

(d) Show that the converse need not be true, by using the results of Problem 8-13 to compute the following expression on \( {\mathbb{{CP}}}^{2} \) with the Fubini-Study metric:

\[
\langle \mathcal{R}\left( {w \land  x + y \land  z}\right) , w \land  x + y \land  z\rangle ,
\]

where \( w, x, y, z \) are orthonormal vectors at an arbitrary point of \( {\mathbb{{CP}}}^{2} \) , chosen so that their horizontal lifts satisfy \( \widetilde{y} = J\widetilde{w} \) and \( \widetilde{z} = J\widetilde{x} \) .
