## Chapter 6 Geodesics and Distance

In this chapter, we explore the relationships among geodesics, lengths, and distances on a Riemannian manifold. A primary goal is to show that all length-minimizing curves are geodesics, and that all geodesics are locally length-minimizing. Later, we prove the Hopf-Rinow theorem, which states that a connected Riemannian manifold is geodesically complete if and only if it is complete as a metric space. At the end of the chapter, we study distance functions (which express the distance to a point or other subset) and show that they can be used to construct coordinates, called semigeodesic coordinates, that put a metric in a particularly simple form.

Most of the results of this chapter do not apply to general pseudo-Riemannian metrics, at least not without substantial modification. For this reason, we restrict our focus here to the Riemannian case. (For a treatment of lengths of curves in the pseudo-Riemannian setting, see [O'N83].) Also, the theory of minimizing curves becomes considerably more complicated in the presence of a nonempty boundary; thus, unless otherwise stated, throughout this chapter we assume that \( \left( {M, g}\right) \) is a Riemannian manifold without boundary. And because we will be using the Riemannian distance function, we assume for most results that \( M \) is connected.

## Geodesics and Minimizing Curves

Let \( \left( {M, g}\right) \) be a Riemannian manifold. An admissible curve \( \gamma \) in \( M \) is said to be a minimizing curve if \( {L}_{g}\left( \gamma \right)  \leq  {L}_{g}\left( \widetilde{\gamma }\right) \) for every admissible curve \( \widetilde{\gamma } \) with the same endpoints. When \( M \) is connected, it follows from the definition of the Riemannian distance that \( \gamma \) is minimizing if and only if \( {L}_{g}\left( \gamma \right) \) is equal to the distance between its endpoints.

Our first goal in this section is to show that all minimizing curves are geodesics. To do so, we will think of the length function \( {L}_{g} \) as a functional on the set of all admissible curves in \( M \) with fixed starting and ending points. (Real-valued functions whose domains are themselves sets of functions are typically called functionals.) Our project is to search for minima of this functional.

From calculus, we might expect that a necessary condition for a curve \( \gamma \) to be minimizing would be that the "derivative" of \( {L}_{g} \) vanish at \( \gamma \) , in some sense. This brings us to the brink of the subject known as the calculus of variations: the use of calculus to identify and analyze extrema of functionals defined on spaces of functions or maps. In its fully developed state, the calculus of variations allows one to apply all the usual tools of multivariable calculus in the infinite-dimensional setting of function spaces-tools such as directional derivatives, gradients, critical points, local extrema, saddle points, and Hessians. For our purposes, however, we do not need to formalize the theory of calculus in the infinite-dimensional setting. It suffices to note that if \( \gamma \) is a minimizing curve, and \( \left\{  {{\Gamma }_{s} : s \in  \left( {-\varepsilon ,\varepsilon }\right) }\right\} \) is a one-parameter family of admissible curves with the same endpoints such that \( {L}_{g}\left( {\Gamma }_{s}\right) \) is a differentiable function of \( s \) and \( {\Gamma }_{0} = \gamma \) , then by elementary calculus, the \( s \) -derivative of \( {L}_{g}\left( {\Gamma }_{s}\right) \) must vanish at \( s = 0 \) because \( {L}_{g}\left( {\Gamma }_{s}\right) \) attains a minimum there.

## Families of Curves

To make this rigorous, we introduce some more definitions. Let \( \left( {M, g}\right) \) be a Riemannian manifold.

Given intervals \( I, J \subseteq  \mathbb{R} \) , a continuous map \( \Gamma  : J \times  I \rightarrow  M \) is called a one-parameter family of curves. Such a family defines two collections of curves in \( M \) : the main curves \( {\Gamma }_{s}\left( t\right)  = \Gamma \left( {s, t}\right) \) defined for \( t \in  I \) by holding \( s \) constant, and the transverse curves \( {\Gamma }^{\left( t\right) }\left( s\right)  = \Gamma \left( {s, t}\right) \) defined for \( s \in  J \) by holding \( t \) constant.

If such a family \( \Gamma \) is smooth (or at least continuously differentiable), we denote the velocity vectors of the main and transverse curves by

\[
{\partial }_{t}\Gamma \left( {s, t}\right)  = {\left( {\Gamma }_{s}\right) }^{\prime }\left( t\right)  \in  {T}_{\Gamma \left( {s, t}\right) }M;\;{\partial }_{s}\Gamma \left( {s, t}\right)  = {\Gamma }^{\left( t\right) \prime }\left( s\right)  \in  {T}_{\Gamma \left( {s, t}\right) }M.
\]

Each of these is an example of a vector field along \( \mathbf{\Gamma } \) , which is a continuous map \( V : J \times  I \rightarrow  {TM} \) such that \( V\left( {s, t}\right)  \in  {T}_{\Gamma \left( {s, t}\right) }M \) for each \( \left( {s, t}\right) \) .

The families of curves that will interest us most in this chapter are of the following type. A one-parameter family \( \Gamma \) is called an admissible family of curves if (i) its domain is of the form \( J \times  \left\lbrack  {a, b}\right\rbrack \) for some open interval \( J \) ; (ii) there is a partition \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) of \( \left\lbrack  {a, b}\right\rbrack \) such that \( \Gamma \) is smooth on each rectangle of the form \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) ; and (iii) \( {\Gamma }_{s}\left( t\right)  = \Gamma \left( {s, t}\right) \) is an admissible curve for each \( s \in  J \) (Fig. 6.1). Every such partition is called an admissible partition for the family.

If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a given admissible curve, a variation of \( \gamma \) is an admissible family of curves \( \Gamma  : J \times  \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) such that \( J \) is an open interval containing 0 and \( {\Gamma }_{0} = \gamma \) . It is called a proper variation if in addition, all of the main curves have the same starting and ending points: \( {\Gamma }_{s}\left( a\right)  = \gamma \left( a\right) \) and \( {\Gamma }_{s}\left( b\right)  = \gamma \left( b\right) \) for all \( s \in  J \) .

In the case of an admissible family, the transverse curves are smooth on \( J \) for each \( t \) , but the main curves are in general only piecewise regular. Thus the velocity vector fields \( {\partial }_{s}\Gamma \) and \( {\partial }_{t}\Gamma \) are smooth on each rectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) , but not generally on the whole domain.

![bo_d7dtff491nqc73eq8m7g_164_364_213_802_363_0.jpg](images/bo_d7dtff491nqc73eq8m7g_164_364_213_802_363_0.jpg)

Fig. 6.1: An admissible family

We can say a bit more about \( {\partial }_{s}\Gamma \) , though. If \( \Gamma \) is an admissible family, a piecewise smooth vector field along \( \mathbf{\Gamma } \) is a (continuous) vector field along \( \Gamma \) whose restriction to each rectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) is smooth for some admissible partition \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) for \( \Gamma \) . In fact, \( {\partial }_{s}\Gamma \) is always such a vector field. To see that it is continuous on the whole domain \( J \times  \left\lbrack  {a, b}\right\rbrack \) , note on the one hand that for each \( i = 1,\ldots , k - 1 \) , the values of \( {\partial }_{s}\Gamma \) along the set \( J \times  \left\{  {a}_{i}\right\} \) depend only on the values of \( \Gamma \) on that set, since the derivative is taken only with respect to the \( s \) variable; on the other hand, \( {\partial }_{s}\Gamma \) is continuous (in fact smooth) on each subrectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) and \( J \times  \left\lbrack  {{a}_{i},{a}_{i + 1}}\right\rbrack \) , so the right-hand and left-hand limits at \( t = {a}_{i} \) must be equal. Therefore \( {\partial }_{s}\Gamma \) is always a piecewise smooth vector field along \( \Gamma \) . (However, \( {\partial }_{t}\Gamma \) is typically not continuous at \( t = {a}_{i} \) .)

If \( \Gamma \) is a variation of \( \gamma \) , the variation field of \( \mathbf{\Gamma } \) is the piecewise smooth vector field \( V\left( t\right)  = {\partial }_{s}\Gamma \left( {0, t}\right) \) along \( \gamma \) . We say that a vector field \( V \) along \( \gamma \) is proper if \( V\left( a\right)  = 0 \) and \( V\left( b\right)  = 0 \) ; it follows easily from the definitions that the variation field of every proper variation is itself proper.

Lemma 6.1. If \( \gamma \) is an admissible curve and \( V \) is a piecewise smooth vector field along \( \gamma \) , then \( V \) is the variation field of some variation of \( \gamma \) . If \( V \) is proper, the variation can be taken to be proper as well.

Proof. Suppose \( \gamma \) and \( V \) satisfy the hypotheses, and set \( \Gamma \left( {s, t}\right)  = {\exp }_{\gamma \left( t\right) }\left( {{sV}\left( t\right) }\right) \) (Fig. 6.2). By compactness of \( \left\lbrack  {a, b}\right\rbrack \) , there is some positive \( \varepsilon \) such that \( \Gamma \) is defined on \( \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {a, b}\right\rbrack \) . By composition, \( \Gamma \) is smooth on \( \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) for each subinterval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) on which \( V \) is smooth, and it is continuous on its whole domain. By the properties of the exponential map, the variation field of \( \Gamma \) is \( V \) . Moreover, if \( V\left( a\right)  = 0 \) and \( V\left( b\right)  = 0 \) , the definition gives \( \Gamma \left( {s, a}\right)  \equiv  \gamma \left( a\right) \) and \( \Gamma \left( {s, b}\right)  \equiv  \gamma \left( b\right) \) , so \( \Gamma \) is proper.

If \( V \) is a piecewise smooth vector field along \( \Gamma \) , we can compute the covariant derivative of \( V \) either along the main curves (at points where \( V \) is smooth) or along the transverse curves; the resulting vector fields along \( \Gamma \) are denoted by \( {D}_{t}V \) and \( {D}_{s}V \) respectively.

A key ingredient in the proof that minimizing curves are geodesics is the symmetry of the Levi-Civita connection. It enters into our proofs in the form of the

![bo_d7dtff491nqc73eq8m7g_165_354_191_827_349_0.jpg](images/bo_d7dtff491nqc73eq8m7g_165_354_191_827_349_0.jpg)

Fig. 6.2: Every vector field along \( \gamma \) is a variation field

following lemma. (Although we state and use this lemma only for the Levi-Civita connection, the proof shows that it is actually true for every symmetric connection in TM.)

Lemma 6.2 (Symmetry Lemma). Let \( \Gamma  : J \times  \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be an admissible family of curves in a Riemannian manifold. On every rectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) where \( \Gamma \) is smooth,

\[
{D}_{s}{\partial }_{t}\Gamma  = {D}_{t}{\partial }_{s}\Gamma
\]

Proof. This is a local question, so we may compute in local coordinates \( \left( {x}^{i}\right) \) around a point \( \Gamma \left( {{s}_{0},{t}_{0}}\right) \) . Writing the components of \( \Gamma \) as \( \Gamma \left( {s, t}\right)  = \left( {{x}^{1}\left( {s, t}\right) ,\ldots ,{x}^{n}\left( {s, t}\right) }\right) \) , we have

\[
{\partial }_{t}\Gamma  = \frac{\partial {x}^{k}}{\partial t}{\partial }_{k};\;{\partial }_{s}\Gamma  = \frac{\partial {x}^{k}}{\partial s}{\partial }_{k}.
\]

Then, using the coordinate formula (4.15) for covariant derivatives along curves, we obtain

\[
{D}_{s}{\partial }_{t}\Gamma  = \left( {\frac{{\partial }^{2}{x}^{k}}{\partial s\partial t} + \frac{\partial {x}^{i}}{\partial t}\frac{\partial {x}^{j}}{\partial s}{\Gamma }_{ji}^{k}}\right) {\partial }_{k}
\]

\[
{D}_{t}{\partial }_{s}\Gamma  = \left( {\frac{{\partial }^{2}{x}^{k}}{\partial t\partial s} + \frac{\partial {x}^{i}}{\partial s}\frac{\partial {x}^{j}}{\partial t}{\Gamma }_{ji}^{k}}\right) {\partial }_{k}.
\]

Reversing the roles of \( i \) and \( j \) in the second line above and using the symmetry condition \( {\Gamma }_{ji}^{k} = {\Gamma }_{ij}^{k} \) , we conclude that these two expressions are equal.

## Minimizing Curves Are Geodesics

We can now compute an expression for the derivative of the length functional along a variation of a curve. Traditionally, the derivative of a functional on a space of maps is called its first variation.

Theorem 6.3 (First Variation Formula). Let \( \left( {M, g}\right) \) be a Riemannian manifold. Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a unit-speed admissible curve, \( \Gamma  : J \times  \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a variation of \( \gamma \) , and \( V \) is its variation field. Then \( {L}_{g}\left( {\Gamma }_{s}\right) \) is a smooth function of \( s \) , and

\[
{\left. \frac{d}{ds}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  =  - {\int }_{a}^{b}\left\langle  {V,{D}_{t}{\gamma }^{\prime }}\right\rangle  {dt} - \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}\left\langle  {V\left( {a}_{i}\right) ,{\Delta }_{i}{\gamma }^{\prime }}\right\rangle
\]

\[
+ \left\langle  {V\left( b\right) ,{\gamma }^{\prime }\left( b\right) }\right\rangle   - \left\langle  {V\left( a\right) ,{\gamma }^{\prime }\left( a\right) }\right\rangle  , \tag{6.1}
\]

![bo_d7dtff491nqc73eq8m7g_166_428_195_674_258_0.jpg](images/bo_d7dtff491nqc73eq8m7g_166_428_195_674_258_0.jpg)

Fig. 6.3: \( {\Delta }_{i}{\gamma }^{\prime } \) is the "jump" in \( {\gamma }^{\prime } \) at \( {a}_{i} \)

where \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) is an admissible partition for \( V \) , and for each \( i = 1,\ldots , k - 1 \) , \( {\Delta }_{i}{\gamma }^{\prime } = {\gamma }^{\prime }\left( {a}_{i}^{ + }\right)  - {\gamma }^{\prime }\left( {a}_{i}^{ - }\right) \) is the "jump" in the velocity vector field \( {\gamma }^{\prime } \) at \( {a}_{i} \) (Fig. 6.3). In particular, if \( \Gamma \) is a proper variation, then

\[
{\left. \frac{d}{ds}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  =  - {\int }_{a}^{b}\left\langle  {V,{D}_{t}{\gamma }^{\prime }}\right\rangle  {dt} - \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}\left\langle  {V\left( {a}_{i}\right) ,{\Delta }_{i}{\gamma }^{\prime }}\right\rangle  . \tag{6.2}
\]

Proof. On every rectangle \( J \times  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) where \( \Gamma \) is smooth, since the integrand in \( {L}_{g}\left( {\Gamma }_{s}\right) \) is smooth and the domain of integration is compact, we can differentiate under the integral sign as many times as we wish. Because \( {L}_{g}\left( {\Gamma }_{s}\right) \) is a finite sum of such integrals, it follows that it is a smooth function of \( s \) .

For brevity, let us introduce the notations

\[
T\left( {s, t}\right)  = {\partial }_{t}\Gamma \left( {s, t}\right) ,\;S\left( {s, t}\right)  = {\partial }_{s}\Gamma \left( {s, t}\right) .
\]

Differentiating on the interval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) yields

\[
\frac{d}{ds}{L}_{g}\left( {\left. {\Gamma }_{s}\right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  }\right)  = {\int }_{{a}_{i - 1}}^{{a}_{i}}\frac{\partial }{\partial s}\langle T, T{\rangle }^{1/2}{dt}
\]

\[
= {\int }_{{a}_{i - 1}}^{{a}_{i}}\frac{1}{2}\langle T, T{\rangle }^{-1/2}2\left\langle  {{D}_{s}T, T}\right\rangle  {dt} \tag{6.3}
\]

\[
= {\int }_{{a}_{i - 1}}^{{a}_{i}}\frac{1}{\left| T\right| }\left\langle  {{D}_{t}S, T}\right\rangle  {dt}
\]

where we have used the symmetry lemma in the last line. Setting \( s = 0 \) and noting that \( S\left( {0, t}\right)  = V\left( t\right) \) and \( T\left( {0, t}\right)  = {\gamma }^{\prime }\left( t\right) \) (which has length 1), we get

\[
{\left. \frac{d}{ds}\right| }_{s = 0}{L}_{g}\left( {\left. {\Gamma }_{s}\right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  }\right)  = {\int }_{{a}_{i - 1}}^{{a}_{i}}\left\langle  {{D}_{t}V,{\gamma }^{\prime }}\right\rangle  {dt}
\]

\[
= {\int }_{{a}_{i - 1}}^{{a}_{i}}\left( {\frac{d}{dt}\left\langle  {V,{\gamma }^{\prime }}\right\rangle   - \left\langle  {V,{D}_{t}{\gamma }^{\prime }}\right\rangle  }\right) {dt}
\]

\[
= \left\langle  {V\left( {a}_{i}\right) ,{\gamma }^{\prime }\left( {a}_{i}^{ - }\right) }\right\rangle   - \left\langle  {V\left( {a}_{i - 1}\right) ,{\gamma }^{\prime }\left( {a}_{i - 1}^{ + }\right) }\right\rangle
\]

\[
- {\int }_{{a}_{i - 1}}^{{a}_{i}}\left\langle  {V,{D}_{t}{\gamma }^{\prime }}\right\rangle  {dt}.
\]

(The second equality follows from (5.3), and the third from the fundamental theorem of calculus.) Finally, summing over \( i \) , we obtain (6.1).

Because every admissible curve has a unit-speed parametrization and length is independent of parametrization, the requirement in the above proposition that \( \gamma \) be of unit speed is not a real restriction, but rather just a computational convenience.

Theorem 6.4. In a Riemannian manifold, every minimizing curve is a geodesic when it is given a unit-speed parametrization.

Proof. Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is minimizing and of unit speed, and \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) is an admissible partition for \( \gamma \) . If \( \Gamma \) is any proper variation of \( \gamma \) , then \( {L}_{g}\left( {\Gamma }_{s}\right) \) is a smooth function of \( s \) that achieves its minimum at \( s = 0 \) , so it follows from elementary calculus that \( d\left( {{L}_{g}\left( {\Gamma }_{s}\right) }\right) /{ds} = 0 \) when \( s = 0 \) . Since every proper vector field along \( \gamma \) is the variation field of some proper variation, the right-hand side of (6.2) must vanish for every such \( V \) .

First we show that \( {D}_{t}{\gamma }^{\prime } = 0 \) on each subinterval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) , so \( \gamma \) is a "broken geodesic." Choose one such interval, and let \( \varphi  \in  {C}^{\infty }\left( \mathbb{R}\right) \) be a bump function such that \( \varphi  > 0 \) on \( \left( {{a}_{i - 1},{a}_{i}}\right) \) and \( \varphi  = 0 \) elsewhere. Then (6.2) with \( V = \varphi {D}_{t}{\gamma }^{\prime } \) becomes

\[
0 =  - {\int }_{{a}_{i - 1}}^{{a}_{i}}\varphi {\left| {D}_{t}{\gamma }^{\prime }\right| }^{2}{dt}
\]

Since the integrand is nonnegative and \( \varphi  > 0 \) on \( \left( {{a}_{i - 1},{a}_{i}}\right) \) , this shows that \( {D}_{t}{\gamma }^{\prime } = 0 \) on each such subinterval.

Next we need to show that \( {\Delta }_{i}{\gamma }^{\prime } = 0 \) for each \( i \) between 0 and \( k \) , which is to say that \( \gamma \) has no corners. For each such \( i \) , we can use a bump function in a coordinate chart to construct a piecewise smooth vector field \( V \) along \( \gamma \) such that \( V\left( {a}_{i}\right)  = {\Delta }_{i}{\gamma }^{\prime } \) and \( V\left( {a}_{j}\right)  = 0 \) for \( j \neq  i \) . Then (6.2) reduces to \( - {\left| {\Delta }_{i}{\gamma }^{\prime }\right| }^{2} = 0 \) , so \( {\Delta }_{i}{\gamma }^{\prime } = 0 \) for each \( i \) .

Finally, since the two one-sided velocity vectors of \( \gamma \) match up at each \( {a}_{i} \) , it follows from uniqueness of geodesics that \( {\left. \gamma \right| }_{\left\lbrack  {a}_{i},{a}_{i + 1}\right\rbrack  } \) is the continuation of the geodesic \( {\left. \gamma \right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  } \) , and therefore \( \gamma \) is smooth.

The preceding proof has an enlightening geometric interpretation. Under the assumption that \( {D}_{t}{\gamma }^{\prime } \neq  0 \) , the first variation with \( V = \varphi {D}_{t}{\gamma }^{\prime } \) is negative, which shows that deforming \( \gamma \) in the direction of its acceleration vector field decreases its length (Fig. 6.4). Similarly, the length of a broken geodesic \( \gamma \) is decreased by deforming it in the direction of a vector field \( V \) such that \( V\left( {a}_{i}\right)  = {\Delta }_{i}{\gamma }^{\prime } \) (Fig. 6.5). Geometrically, this corresponds to "rounding the corner."

![bo_d7dtff491nqc73eq8m7g_168_207_187_567_160_0.jpg](images/bo_d7dtff491nqc73eq8m7g_168_207_187_567_160_0.jpg)

Fig. 6.4: Deforming in the direction of the acceleration

![bo_d7dtff491nqc73eq8m7g_168_866_202_484_181_0.jpg](images/bo_d7dtff491nqc73eq8m7g_168_866_202_484_181_0.jpg)

Fig. 6.5: Rounding the corner

The first variation formula actually tells us a bit more than is claimed in Theorem 6.4. In proving that \( \gamma \) is a geodesic, we did not use the full strength of the assumption that the length of \( {\Gamma }_{s} \) takes a minimum when \( s = 0 \) ; we only used the fact that its derivative is zero. We say that an admissible curve \( \gamma \) is a critical point of \( {\mathbf{L}}_{\mathbf{g}} \) if for every proper variation \( {\Gamma }_{s} \) of \( \gamma \) , the derivative of \( {L}_{g}\left( {\Gamma }_{s}\right) \) with respect to \( s \) is zero at \( s = 0 \) . Therefore we can strengthen Theorem 6.4 in the following way.

Corollary 6.5. A unit-speed admissible curve \( \gamma \) is a critical point for \( {L}_{g} \) if and only if it is a geodesic.

Proof. If \( \gamma \) is a critical point, the proof of Theorem 6.4 goes through without modification to show that \( \gamma \) is a geodesic. Conversely, if \( \gamma \) is a geodesic, then the first term on the right-hand side of (6.2) vanishes by the geodesic equation, and the second term vanishes because \( {\gamma }^{\prime } \) has no jumps.

The geodesic equation \( {D}_{t}{\gamma }^{\prime } = 0 \) thus characterizes the critical points of the length functional. In general, the equation that characterizes critical points of a functional on a space of maps is called the variational equation or the Euler-Lagrange equation of the functional. Many interesting equations in differential geometry arise as variational equations. We touch briefly on three others in this book: the Einstein equation (7.34), the Yamabe equation (7.59), and the minimal hypersurface equation \( H \equiv  0 \) (Thm. 8.18).

## Geodesics Are Locally Minimizing

Next we turn to the converse of Theorem 6.4. It is easy to see that the literal converse is not true, because not every geodesic segment is minimizing. For example, every geodesic segment on \( {\mathbb{S}}^{n} \) that goes more than halfway around the sphere is not minimizing, because the other portion of the same great circle is a shorter curve segment between the same two points. For that reason, we concentrate initially on local minimization properties of geodesics.

As usual, let \( \left( {M, g}\right) \) be a Riemannian manifold. A regular (or piecewise regular) curve \( \gamma  : I \rightarrow  M \) is said to be locally minimizing if every \( {t}_{0} \in  I \) has a neighborhood \( {I}_{0} \subseteq  I \) such that whenever \( a, b \in  {I}_{0} \) with \( a < b \) , the restriction of \( \gamma \) to \( \left\lbrack  {a, b}\right\rbrack \) is minimizing.

![bo_d7dtff491nqc73eq8m7g_169_519_190_492_403_0.jpg](images/bo_d7dtff491nqc73eq8m7g_169_519_190_492_403_0.jpg)

Fig. 6.6: The radial vector field in a normal neighborhood

Lemma 6.6. Every minimizing admissible curve segment is locally minimizing.

- Exercise 6.7. Prove the preceding lemma.

Our goal in this section is to show that geodesics are locally minimizing. The proof will be based on a careful analysis of the geodesic equation in Riemannian normal coordinates.

If \( \varepsilon \) is a positive number such that \( {\exp }_{p} \) is a diffeomorphism from the ball \( {B}_{\varepsilon }\left( 0\right)  \subseteq  {T}_{p}M \) to its image (where the radius of the ball is measured with respect to the norm defined by \( {g}_{p} \) ), then the image set \( {\exp }_{p}\left( {{B}_{\varepsilon }\left( 0\right) }\right) \) is a normal neighborhood of \( p \) , called a geodesic ball in \( \mathbf{M} \) , or sometimes an open geodesic ball for clarity.

Also, if the closed ball \( {\bar{B}}_{\varepsilon }\left( 0\right) \) is contained in an open set \( V \subseteq  {T}_{p}M \) on which \( {\exp }_{p} \) is a diffeomorphism onto its image, then \( {\exp }_{p}\left( {{\bar{B}}_{\varepsilon }\left( 0\right) }\right) \) is called a closed geodesic ball, and \( {\exp }_{p}\left( {\partial {B}_{\varepsilon }\left( 0\right) }\right) \) is called a geodesic sphere. Given such a \( V \) , by compactness there exists \( {\varepsilon }^{\prime } > \varepsilon \) such that \( {B}_{{\varepsilon }^{\prime }}\left( 0\right)  \subseteq  V \) , so every closed geodesic ball is contained in an open geodesic ball of larger radius. In Riemannian normal coordinates centered at \( p \) , the open and closed geodesic balls and geodesic spheres centered at \( p \) are just the coordinate balls and spheres.

Suppose \( U \) is a normal neighborhood of \( p \in  M \) . Given any normal coordinates \( \left( {x}^{i}\right) \) on \( U \) centered at \( p \) , define the radial distance function \( r : U \rightarrow  \mathbb{R} \) by

\[
r\left( x\right)  = \sqrt{{\left( {x}^{1}\right) }^{2} + \cdots  + {\left( {x}^{n}\right) }^{2}}, \tag{6.4}
\]

and the radial vector field on \( U \smallsetminus  \{ p\} \) (see Fig. 6.6), denoted by \( {\partial }_{r} \) , by

\[
{\partial }_{r} = \frac{{x}^{i}}{r\left( x\right) }\frac{\partial }{\partial {x}^{i}}. \tag{6.5}
\]

In Euclidean space, \( r\left( x\right) \) is the distance to the origin, and \( {\partial }_{r} \) is the unit vector field pointing radially outward from the origin. (The notation is suggested by the fact that \( {\partial }_{r} \) is a coordinate derivative in polar or spherical coordinates.)

Lemma 6.8. In every normal neighborhood \( U \) of \( p \in  M \) , the radial distance function and the radial vector field are well defined, independently of the choice of normal coordinates. Both \( r \) and \( {\partial }_{r} \) are smooth on \( U \smallsetminus  \{ p\} \) , and \( {r}^{2} \) is smooth on all of \( U \) .

Proof. Proposition 5.23 shows that any two normal coordinate charts on \( U \) are related by \( {\widetilde{x}}^{i} = {A}^{i}{}_{j}{x}^{j} \) for some orthogonal matrix \( \left( {A}_{j}^{i}\right) \) , and a straightforward computation shows that both \( r \) and \( {\partial }_{r} \) are invariant under such coordinate changes. The smoothness statements follow directly from the coordinate formulas.

The crux of the proof that geodesics are locally minimizing is the following deceptively simple geometric lemma.

Theorem 6.9 (The Gauss Lemma). Let \( \left( {M, g}\right) \) be a Riemannian manifold, let \( U \) be a geodesic ball centered at \( p \in  M \) , and let \( {\partial }_{r} \) denote the radial vector field on \( U \smallsetminus  \{ p\} \) . Then \( {\partial }_{r} \) is a unit vector field orthogonal to the geodesic spheres in \( U \smallsetminus  \{ p\} \) .

Proof. We will work entirely in normal coordinates \( \left( {x}^{i}\right) \) on \( U \) centered at \( p \) , using the properties of normal coordinates described in Proposition 5.24.

Let \( q \in  U \smallsetminus  \{ p\} \) be arbitrary, with coordinate representation \( \left( {{q}^{1},\ldots ,{q}^{n}}\right) \) , and let \( b = r\left( q\right)  = \sqrt{{\left( {q}^{1}\right) }^{2} + \cdots  + {\left( {q}^{n}\right) }^{2}} \) , where \( r \) is the radial distance function defined by (6.4). It follows that \( {\left. {\partial }_{r}\right| }_{q} \) has the coordinate representation

\[
{\left. {\partial }_{r}\right| }_{q} = {\left. \frac{{q}^{i}}{b}\frac{\partial }{\partial {x}^{i}}\right| }_{q}.
\]

Let \( v = {v}^{i}{\left. {\partial }_{i}\right| }_{p} \in  {T}_{p}M \) be the tangent vector at \( p \) with components \( {v}^{i} = {q}^{i}/b \) . By Proposition 5.24(c), the radial geodesic with initial velocity \( v \) is given in these coordinates by

\[
{\gamma }_{v}\left( t\right)  = \left( {t{v}^{1},\ldots , t{v}^{n}}\right) .
\]

It satisfies \( {\gamma }_{v}\left( 0\right)  = p,{\gamma }_{v}\left( b\right)  = q \) , and \( {\gamma }_{v}^{\prime }\left( b\right)  = {\left. {v}^{i}{\partial }_{i}\right| }_{q} = {\left. {\partial }_{r}\right| }_{q} \) . Because \( {g}_{p} \) is equal to the Euclidean metric in these coordinates, we have

\[
{\left| {\gamma }_{v}^{\prime }\left( 0\right) \right| }_{g} = {\left| v\right| }_{g} = \sqrt{{\left( {v}^{1}\right) }^{2} + \cdots  + {\left( {v}^{n}\right) }^{2}} = \frac{1}{b}\sqrt{{\left( {q}^{1}\right) }^{2} + \cdots  + {\left( {q}^{n}\right) }^{2}} = 1,
\]

so \( v \) is a unit vector, and thus \( {\gamma }_{v} \) is a unit-speed geodesic. It follows that \( {\left. {\partial }_{r}\right| }_{q} = {\gamma }_{v}^{\prime }\left( b\right) \) is also a unit vector.

To prove that \( {\partial }_{r} \) is orthogonal to the geodesic spheres let \( q, b \) , and \( v \) be as above, and let \( {\sum }_{b} = {\exp }_{p}\left( {\partial {B}_{b}\left( 0\right) }\right) \) be the geodesic sphere containing \( q \) . In these coordinates, \( {\sum }_{b} \) is the set of points satisfying the equation \( {\left( {x}^{1}\right) }^{2} + \cdots  + {\left( {x}^{n}\right) }^{2} = {b}^{2} \) . Let \( w \in  {T}_{q}M \) be any vector tangent to \( {\sum }_{b} \) at \( q \) . We need to show that \( {\left\langle  {\left. w,{\partial }_{r}\right| }_{q}\right\rangle  }_{g} = 0 \) .

Choose a smooth curve \( \sigma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  {\sum }_{b} \) satisfying \( \sigma \left( 0\right)  = q \) and \( {\sigma }^{\prime }\left( 0\right)  = w \) , and write its coordinate representation in \( \left( {x}^{i}\right) \) -coordinates as \( \sigma \left( s\right)  = \left( {{\sigma }^{1}\left( s\right) ,\ldots ,{\sigma }^{n}\left( s\right) }\right) \) . The fact that \( \sigma \left( s\right) \) lies in \( {\sum }_{b} \) for all \( s \) means that

\[
{\left( {\sigma }^{1}\left( s\right) \right) }^{2} + \cdots  + {\left( {\sigma }^{n}\left( s\right) \right) }^{2} = {b}^{2}. \tag{6.6}
\]

Define a smooth map \( \Gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0, b}\right\rbrack   \rightarrow  U \) (Fig. 6.7) by

\[
\Gamma \left( {s, t}\right)  = \left( {\frac{t}{b}{\sigma }^{1}\left( s\right) ,\ldots ,\frac{t}{b}{\sigma }^{n}\left( s\right) }\right) .
\]

![bo_d7dtff491nqc73eq8m7g_171_271_211_963_449_0.jpg](images/bo_d7dtff491nqc73eq8m7g_171_271_211_963_449_0.jpg)

Fig. 6.7: Proof of the Gauss lemma

For each \( s \in  \left( {-\varepsilon ,\varepsilon }\right) ,{\Gamma }_{s} \) is a geodesic by Proposition 5.24(c). Its initial velocity is \( {\Gamma }_{s}^{\prime }\left( 0\right)  = \left( {1/b}\right) {\sigma }^{i}\left( s\right) {\partial }_{i} \mid  p \) , which is a unit vector by (6.6) and the fact that \( {g}_{p} \) is the Euclidean metric in coordinates; thus each \( {\Gamma }_{s} \) is a unit-speed geodesic.

As before, let \( S = {\partial }_{s}\Gamma \) and \( T = {\partial }_{t}\Gamma \) . It follows from the definitions that

\[
S\left( {0,0}\right)  = {\left. \frac{d}{ds}\right| }_{s = 0}{\Gamma }_{s}\left( 0\right)  = 0
\]

\[
T\left( {0,0}\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}{\gamma }_{v}\left( t\right)  = v
\]

\[
S\left( {0, b}\right)  = {\left. \frac{d}{ds}\right| }_{s = 0}\sigma \left( s\right)  = w
\]

\[
T\left( {0, b}\right)  = {\left. \frac{d}{dt}\right| }_{t = b}{\gamma }_{v}\left( t\right)  = {\left. {\gamma }_{v}^{\prime }\left( b\right)  = {\partial }_{r}\right| }_{q}.
\]

Therefore \( \langle S, T\rangle \) is zero when \( \left( {s, t}\right)  = \left( {0,0}\right) \) and equal to \( \left\langle  {w,{\left. {\partial }_{r}\right| }_{q}}\right\rangle \) when \( \left( {s, t}\right)  = \; \left( {0, b}\right) \) , so to prove the theorem it suffices to show that \( \langle S, T\rangle \) is independent of \( t \) .

We compute

\[
\frac{\partial }{\partial t}\langle S, T\rangle  = \left\langle  {{D}_{t}S, T}\right\rangle   + \left\langle  {S,{D}_{t}T}\right\rangle  \;\text{ (compatibility with the metric) }
\]

(6.7)

\[
= \left\langle  {{D}_{s}T, T}\right\rangle   + \left\langle  {S,{D}_{t}T}\right\rangle  \;\text{ (symmetry lemma) }
\]

\[
= \left\langle  {{D}_{s}T, T}\right\rangle   + 0\;\text{ (each }{\Gamma }_{s}\text{ is a geodesic) }
\]

\[
= \frac{1}{2}\frac{\partial }{\partial s}{\left| T\right| }^{2} = 0\;\left( {\left| T\right|  = \left| {\Gamma }_{s}^{\prime }\right|  \equiv  1\text{ for all }\left( {s, t}\right) }\right) .
\]

![bo_d7dtff491nqc73eq8m7g_172_525_206_479_395_0.jpg](images/bo_d7dtff491nqc73eq8m7g_172_525_206_479_395_0.jpg)

Fig. 6.8: Radial geodesics are minimizing

This proves the theorem.

We will use the Gauss lemma primarily in the form of the next corollary.

Corollary 6.10. Let \( U \) be a geodesic ball centered at \( p \in  M \) , and let \( r \) and \( {\partial }_{r} \) be the radial distance and radial vector field as defined by (6.4) and (6.5). Then \( \operatorname{grad}r = {\partial }_{r} \) on \( U \smallsetminus  \{ p\} \) .

Proof. By the result of Problem 2-10, it suffices to show that \( {\partial }_{r} \) is orthogonal to the level sets of \( r \) and \( {\partial }_{r}\left( r\right)  \equiv  {\left| {\partial }_{r}\right| }_{g}^{2} \) . The first claim follows directly from the Gauss lemma, and the second from the fact that \( {\partial }_{r}\left( r\right)  \equiv  1 \) by direct computation in normal coordinates, which in turn is equal to \( {\left| {\partial }_{r}\right| }_{g}^{2} \) by the Gauss lemma.

Here is the payoff: our first step toward proving that geodesics are locally minimizing. Note that this is not yet the full strength of the theorem we are aiming for, because it shows only that for each point on a geodesic, sufficiently small segments of the geodesic starting at that point are minimizing. We will remove this restriction after a little more work below.

Proposition 6.11. Let \( \left( {M, g}\right) \) be a Riemannian manifold. Suppose \( p \in  M \) and \( q \) is contained in a geodesic ball around \( p \) . Then (up to reparametrization) the radial geodesic from \( p \) to \( q \) is the unique minimizing curve in \( M \) from \( p \) to \( q \) .

Proof. Choose \( \varepsilon  > 0 \) such that \( {\exp }_{p}\left( {{B}_{\varepsilon }\left( 0\right) }\right) \) is a geodesic ball containing \( q \) . Let \( \gamma  : \left\lbrack  {0, c}\right\rbrack   \rightarrow  M \) be the radial geodesic from \( p \) to \( q \) parametrized by arc length, and write \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) for some unit vector \( v \in  {T}_{p}M \) . Then \( {L}_{g}\left( \gamma \right)  = c \) , since \( \gamma \) has unit speed.

To show that \( \gamma \) is minimizing, we need to show that every other admissible curve from \( p \) to \( q \) has length at least \( c \) . Let \( \sigma  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) be an arbitrary admissible curve from \( p \) to \( q \) , which we may assume to be parametrized by arc length as well. Let \( {a}_{0} \in  \left\lbrack  {0, b}\right\rbrack \) denote the last time that \( \sigma \left( t\right)  = p \) , and \( {b}_{0} \in  \left\lbrack  {0, b}\right\rbrack \) the first time after \( {a}_{0} \) that \( \sigma \left( t\right) \) meets the geodesic sphere \( {\sum }_{c} \) of radius \( c \) around \( p \) (Fig. 6.8). Then the composite function \( r \circ  \sigma \) is continuous on \( \left\lbrack  {{a}_{0},{b}_{0}}\right\rbrack \) and piecewise smooth in \( \left( {{a}_{0},{b}_{0}}\right) \) , so we can apply the fundamental theorem of calculus to conclude that

\[
r\left( {\sigma \left( {b}_{0}\right) }\right)  - r\left( {\sigma \left( {a}_{0}\right) }\right)  = {\int }_{{a}_{0}}^{{b}_{0}}\frac{d}{dt}r\left( {\sigma \left( t\right) }\right) {dt}
\]

\[
= {\int }_{{a}_{0}}^{{b}_{0}}{dr}\left( {{\sigma }^{\prime }\left( t\right) }\right) {dt}
\]

\[
= {\int }_{{a}_{0}}^{{b}_{0}}\left\langle  {{\left. \operatorname{grad}r\right| }_{\sigma \left( t\right) },{\sigma }^{\prime }\left( t\right) }\right\rangle  {dt} \tag{6.8}
\]

\[
\leq  {\int }_{{a}_{0}}^{{b}_{0}}{\left| \operatorname{grad}r\right| }_{\sigma \left( t\right) }\left| \right| {\sigma }^{\prime }\left( t\right)  \mid  {dt}
\]

\[
= {\int }_{{a}_{0}}^{{b}_{0}}\left| {{\sigma }^{\prime }\left( t\right) }\right| {dt}
\]

\[
= {L}_{g}\left( {\left. \sigma \right| }_{\left\lbrack  {a}_{0},{b}_{0}\right\rbrack  }\right)  \leq  {L}_{g}\left( \sigma \right) .
\]

Thus \( {L}_{g}\left( \sigma \right)  \geq  r\left( {\sigma \left( {b}_{0}\right) }\right)  - r\left( {\sigma \left( {a}_{0}\right) }\right)  = c \) , so \( \gamma \) is minimizing.

Now suppose \( {L}_{g}\left( \sigma \right)  = c \) . Then \( b = c \) , and both inequalities in (6.8) are equalities. Because we assume that \( \sigma \) is a unit-speed curve, the second of these equalities implies that \( {a}_{0} = 0 \) and \( {b}_{0} = b = c \) , since otherwise the segments of \( \sigma \) before \( t = {a}_{0} \) and after \( t = {b}_{0} \) would contribute positive lengths. The first equality then implies that the nonnegative expression \( \left| {\operatorname{grad}r{\left. \right| }_{\sigma \left( t\right) }}\right| \left| {{\sigma }^{\prime }\left( t\right) }\right|  - \left\langle  {\operatorname{grad}r{\left. \right| }_{\sigma \left( t\right) },{\sigma }^{\prime }\left( t\right) }\right\rangle \) is identically zero on \( \left\lbrack  {0, b}\right\rbrack \) , which is possible only if \( {\sigma }^{\prime }\left( t\right) \) is a positive multiple of grad \( {\left. r\right| }_{\sigma \left( t\right) } \) for each \( t \) . Since we assume that \( \sigma \) has unit speed, we must have \( {\sigma }^{\prime }\left( t\right)  = {\left. \operatorname{grad}r\right| }_{\sigma \left( t\right) } = {\left. {\partial }_{r}\right| }_{\sigma \left( t\right) } \) . Thus \( \sigma \) and \( \gamma \) are both integral curves of \( {\partial }_{r} \) passing through \( q \) at time \( t = c \) , so \( \sigma  = \gamma \) .

The next two corollaries show how radial distance functions, balls, and spheres in normal coordinates are related to their global metric counterparts.

Corollary 6.12. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold and \( p \in  M \) . Within every open or closed geodesic ball around \( p \) , the radial distance function \( r\left( x\right) \) defined by (6.4) is equal to the Riemannian distance from \( p \) to \( x \) in \( M \) .

Proof. Since every closed geodesic ball is contained in an open geodesic ball of larger radius, we need only consider the open case. If \( x \) is in the open geodesic ball \( {\exp }_{p}\left( {{B}_{c}\left( 0\right) }\right) \) , the radial geodesic \( \gamma \) from \( p \) to \( x \) is minimizing by Proposition 6.11. Since its velocity is equal to \( {\partial }_{r} \) , which is a unit vector in both the \( g \) -norm and the Euclidean norm in normal coordinates, the \( g \) -length of \( \gamma \) is equal to its Euclidean length, which is \( r\left( x\right) \) .

Corollary 6.13. In a connected Riemannian manifold, every open or closed geodesic ball is also an open or closed metric ball of the same radius, and every geodesic sphere is a metric sphere of the same radius.

Proof. Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( p \in  M \) be arbitrary. First, let \( V = {\exp }_{p}\left( {{\bar{B}}_{c}\left( 0\right) }\right)  \subseteq  M \) be a closed geodesic ball of radius \( c > 0 \) around \( p \) . Suppose \( q \) is an arbitrary point of \( M \) . If \( q \in  V \) , then Corollary 6.12 shows that \( q \) is also in the closed metric ball of radius \( c \) . Conversely, suppose \( q \notin  V \) . Let \( S \) be the geodesic sphere \( {\exp }_{p}\left( {\partial {B}_{c}\left( 0\right) }\right) \) . The complement of \( S \) is the disjoint union of the open sets \( {\exp }_{p}\left( {{B}_{c}\left( 0\right) }\right) \) and \( M \sim  {\exp }_{p}\left( {{\bar{B}}_{c}\left( 0\right) }\right) \) , and hence disconnected. Thus if \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any admissible curve from \( p \) to \( q \) , there must be a time \( {t}_{0} \in  \left( {a, b}\right) \) when \( \gamma \left( {t}_{0}\right)  \in  S \) , and then Corollary 6.12 shows that the length of \( {\left. \gamma \right| }_{\left\lbrack  a,{t}_{0}\right\rbrack  } \) must be at least \( c \) . Since \( {\left. \gamma \right| }_{\left\lbrack  {t}_{0}, b\right\rbrack  } \) must have positive length, it follows that \( {d}_{g}\left( {p, q}\right)  > c \) , so \( q \) is not in the closed metric ball of radius \( c \) around \( p \) .

Next, let \( W = {\exp }_{p}\left( {{B}_{c}\left( 0\right) }\right) \) be an open geodesic ball of radius \( c \) . Since \( W \) is the union of all closed geodesic balls around \( p \) of radius less than \( c \) , and the open metric ball of radius \( c \) is similarly the union of all closed metric metric balls of smaller radii, the result of the preceding paragraph shows that \( W \) is equal to the open metric ball of radius \( c \) .

Finally, if \( S = {\exp }_{p}\left( {\partial {B}_{c}\left( 0\right) }\right) \) is a geodesic sphere of radius \( c \) , the arguments above show that \( S \) is equal to the closed metric ball of radius \( c \) minus the open metric ball of radius \( c \) , which is exactly the metric sphere of radius \( c \) .

The last corollary suggests a simplified notation for geodesic balls and spheres in \( M \) . From now on, we will use the notations \( {B}_{c}\left( p\right)  = {\exp }_{p}\left( {{B}_{c}\left( 0\right) }\right) ,{\bar{B}}_{c}\left( p\right)  = \; {\exp }_{p}\left( {{\bar{B}}_{c}\left( 0\right) }\right) \) , and \( {S}_{c}\left( p\right)  = {\exp }_{p}\left( {\partial {B}_{c}\left( 0\right) }\right) \) for open and closed geodesic balls and geodesic spheres, which we now know are also open and closed metric balls and spheres. (To avoid confusion, we refrain from using this notation for other metric balls and spheres unless explicitly stated.)

## Uniformly Normal Neighborhoods

We continue to let \( \left( {M, g}\right) \) be a Riemannian manifold. In order to prove that geodesics in \( M \) are locally minimizing, we need the following refinement of the concept of normal neighborhoods. A subset \( W \subseteq  M \) is called uniformly normal if there exists some \( \delta  > 0 \) such that \( W \) is contained in a geodesic ball of radius \( \delta \) around each of its points (Fig. 6.9). If \( \delta \) is any such constant, we will also say that \( W \) is uniformly \( \delta \) -normal. Clearly every subset of a uniformly \( \delta \) -normal set is itself uniformly \( \delta \) -normal.

Lemma 6.14 (Uniformly Normal Neighborhood Lemma). Given \( p \in  M \) and any neighborhood \( U \) of \( p \) , there exists a uniformly normal neighborhood of \( p \) contained in \( U \) .

Proof. Choose a normal coordinate chart \( \left( {{U}_{0},\left( {x}^{i}\right) }\right) \) centered at \( p \) and contained in \( U \) , and let \( \left( {{x}^{i},{v}^{i}}\right) \) be the corresponding natural coordinates for \( {\pi }^{-1}\left( {U}_{0}\right)  \subseteq  {TM} \) . Because this is a local question, we might as well identify \( {U}_{0} \) with an open subset of \( {\mathbb{R}}^{n} \) , and identify \( {TM} \) with \( {U}_{0} \times  {\mathbb{R}}^{n} \) . The exponential map for the Riemannian manifold \( \left( {{U}_{0}, g}\right) \) is defined on an open subset \( \mathcal{E} \subseteq  {U}_{0} \times  {\mathbb{R}}^{n} \) . Consider the map \( E : \mathcal{E} \rightarrow  {U}_{0} \times  {U}_{0} \) defined by

\[
E\left( {x, v}\right)  = \left( {x,{\exp }_{x}v}\right) .
\]

![bo_d7dtff491nqc73eq8m7g_175_482_187_569_543_0.jpg](images/bo_d7dtff491nqc73eq8m7g_175_482_187_569_543_0.jpg)

Fig. 6.9: Uniformly normal neighborhood

The differential of \( E \) at \( \left( {p,0}\right) \) is represented by the matrix

\[
d{E}_{\left( p,0\right) } = \left( \begin{matrix} \frac{\partial {x}^{i}}{\partial {x}^{j}} & \frac{\partial {x}^{i}}{\partial {v}^{j}} \\  \frac{\partial {\exp }^{i}}{\partial {x}^{j}} & \frac{\partial {\exp }^{i}}{\partial {v}^{j}} \end{matrix}\right)  = \left( \begin{matrix} \operatorname{Id}0 \\   * \operatorname{Id} \end{matrix}\right) ,
\]

which is invertible. By the inverse function theorem, therefore, there are neighborhoods \( \mathcal{U} \subseteq  {U}_{0} \times  {\mathbb{R}}^{n} \) of \( \left( {p,0}\right) \) and \( \mathcal{V} \subseteq  {U}_{0} \times  {U}_{0} \) of \( \left( {p, p}\right) \) such that \( E \) restricts to a diffeomorphism from \( \mathcal{U} \) to \( \mathcal{V} \) . Shrinking both neighborhoods if necessary, we may assume that \( \mathcal{U} \) is a product set of the form \( W \times  {B}_{\varepsilon }\left( 0\right) \) , where \( W \) is a neighborhood of \( p \) and \( {B}_{\varepsilon }\left( 0\right) \) is a Euclidean ball in \( v \) -coordinates. It follows that for each \( x \in  W \) , \( {\exp }_{x} \) maps \( {B}_{\varepsilon }\left( 0\right) \) smoothly onto the open set \( {\mathcal{V}}_{x} = \{ y : \left( {x, y}\right)  \in  \mathcal{V}\} \) , and it is a diffeomorphism because its inverse is given explicitly by \( {\exp }_{x}^{-1}\left( y\right)  = {\pi }_{2} \circ  {E}^{-1}\left( {x, y}\right) \) , where \( {\pi }_{2} : {U}_{0} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) is the projection. Shrinking \( W \) still further if necessary, we may assume that the metric \( g \) satisfies an estimate of the form (2.21) for all \( x \in  W \) . This means that for each \( x \in  W \) , the coordinate ball \( {B}_{\varepsilon }\left( 0\right)  \subseteq  {T}_{x}M \) contains a \( {g}_{x} \) -ball of radius at least \( \varepsilon /c \) . Put \( \delta  = \varepsilon /c \) ; we have shown that for each \( x \in  W \) , there is a \( g \) -geodesic ball of radius \( \delta \) in \( M \) centered at \( x \) .

Now, shrinking \( W \) once more, we may assume that its diameter (with respect to the metric \( {d}_{g} \) ) is less than \( \delta \) . It follows that for each \( x \in  W \) , the entire set \( W \) is contained in the metric ball of radius \( \delta \) around \( x \) , and Corollary 6.13 shows that this metric ball is also a geodesic ball of radius \( \delta \) . Thus \( W \) is the required uniformly normal neighborhood of \( p \) .

We are now ready to prove the main result of this section.

![bo_d7dtff491nqc73eq8m7g_176_285_185_851_486_0.jpg](images/bo_d7dtff491nqc73eq8m7g_176_285_185_851_486_0.jpg)

Fig. 6.10: Geodesics are locally minimizing

Theorem 6.15. Every Riemannian geodesic is locally minimizing.

Proof. Let \( \left( {M, g}\right) \) be a Riemannian manifold. Suppose \( \gamma  : I \rightarrow  M \) is a geodesic, which we may assume to be defined on an open interval, and let \( {t}_{0} \in  I \) . Let \( W \) be a uniformly normal neighborhood of \( \gamma \left( {t}_{0}\right) \) , and let \( {I}_{0} \subseteq  I \) be the connected component of \( {\gamma }^{-1}\left( W\right) \) containing \( {t}_{0} \) . If \( a, b \in  {I}_{0} \) with \( a < b \) , then the definition of uniformly normal neighborhood implies that \( \gamma \left( b\right) \) is contained in a geodesic ball centered at \( \gamma \left( a\right) \) (Fig. 6.10). Therefore, by Proposition 6.11, the radial geodesic segment from \( \gamma \left( a\right) \) to \( \gamma \left( b\right) \) is the unique minimizing curve segment between these points. However, the restriction of \( \gamma \) to \( \left\lbrack  {a, b}\right\rbrack \) is also a geodesic segment from \( \gamma \left( a\right) \) to \( \gamma \left( b\right) \) lying in the same geodesic ball, and thus \( {\left. \gamma \right| }_{\left\lbrack  a, b\right\rbrack  } \) must coincide with this minimizing geodesic.

It is interesting to note that the Gauss lemma and the uniformly normal neighborhood lemma also yield another proof that minimizing curves are geodesics, without using the first variation formula. On the principle that knowing more than one proof of an important fact always deepens our understanding of it, we present this proof for good measure.

Another proof of Theorem 6.4. Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a minimizing admissible curve. Just as in the preceding proof, for every \( {t}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) we can find a connected neighborhood \( {I}_{0} \) of \( {t}_{0} \) such that \( \gamma \left( {I}_{0}\right) \) is contained in a uniformly normal neighborhood \( W \) . Then for every \( {a}_{0},{b}_{0} \in  {I}_{0} \) , the same argument as above shows that the unique minimizing curve segment from \( \gamma \left( {a}_{0}\right) \) to \( \gamma \left( {b}_{0}\right) \) is a radial geodesic. Since the restriction of \( \gamma \) to \( \left\lbrack  {{a}_{0},{b}_{0}}\right\rbrack \) is such a minimizing curve segment, it must coincide with this radial geodesic. Therefore \( \gamma \) solves the geodesic equation in a neighborhood of \( {t}_{0} \) . Since \( {t}_{0} \) was arbitrary, \( \gamma \) is a geodesic.

Given a Riemannian manifold \( \left( {M, g}\right) \) (without boundary), for each point \( p \in  M \) we define the injectivity radius of \( M \) at \( p \) , denoted by \( \operatorname{inj}\left( p\right) \) , to be the supremum of all \( a > 0 \) such that \( {\exp }_{p} \) is a diffeomorphism from \( {B}_{a}\left( 0\right)  \subseteq  {T}_{p}M \) onto its image.

If there is no upper bound to the radii of such balls (as is the case, for example, on \( \left. {\mathbb{R}}^{n}\right) \) , then we set \( \operatorname{inj}\left( p\right)  = \infty \) . Then we define the injectivity radius of \( M \) , denoted by \( \operatorname{inj}\left( M\right) \) , to be the infimum of \( \operatorname{inj}\left( p\right) \) as \( p \) ranges over points of \( M \) . It can be zero, positive, or infinite. (The terminology is explained by Problem 10-24.)

Lemma 6.16. If \( \left( {M, g}\right) \) is a compact Riemannian manifold, then \( \operatorname{inj}\left( M\right) \) is positive.

Proof. For each \( x \in  M \) , there is a positive number \( \delta \left( x\right) \) such that \( x \) is contained in a uniformly \( \delta \left( x\right) \) -normal neighborhood \( {W}_{x} \) , and \( \operatorname{inj}\left( {x}^{\prime }\right)  \geq  \delta \left( x\right) \) for each \( {x}^{\prime } \in  W \) . Since \( M \) is compact, it is covered by finitely many such neighborhoods \( {W}_{{x}_{1}},\ldots ,{W}_{{x}_{k}} \) . Therefore, \( \operatorname{inj}\left( M\right) \) is at least equal to the minimum of \( \delta \left( {x}_{1}\right) ,\ldots ,\delta \left( {x}_{k}\right) \) . It cannot be infinite, because a compact metric space is bounded, and a geodesic ball of radius \( c \) contains points whose distances from the center are arbitrarily close to \( c \) .

In addition to uniformly normal neighborhoods, there is another, more specialized, kind of normal neighborhood that is frequently useful. Let \( \left( {M, g}\right) \) be a Riemannian manifold. A subset \( U \subseteq  M \) is said to be geodesically convex if for each \( p, q \in  U \) , there is a unique minimizing geodesic segment from \( p \) to \( q \) in \( M \) , and the image of this geodesic segment lies entirely in \( U \) .

The next theorem says that every sufficiently small geodesic ball is geodesically convex.

Theorem 6.17. Let \( \left( {M, g}\right) \) be a Riemannian manifold. For each \( p \in  M \) , there exists \( {\varepsilon }_{0} > 0 \) such that every geodesic ball centered at \( p \) of radius less than or equal to \( {\varepsilon }_{0} \) is geodesically convex.

Proof. Problem 6-5.

## Completeness

Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold. Now that we can view \( M \) as a metric space, it is time to address one of the most important questions one can ask about a metric space: Is it complete? In general, the answer is no: for example, if \( M \) is an open ball in \( {\mathbb{R}}^{n} \) with its Euclidean metric, then every sequence in \( M \) that converges in \( {\mathbb{R}}^{n} \) to a point in \( \partial M \) is Cauchy, but not convergent in \( M \) .

In Chapter 5, we introduced another notion of completeness for Riemannian and pseudo-Riemannian manifolds: recall that such a manifold is said to be geodesically complete if every maximal geodesic is defined for all \( t \in  \mathbb{R} \) . For clarity, we will use the phrase metrically complete for a connected Riemannian manifold that is complete as a metric space with the Riemannian distance function, in the sense that every Cauchy sequence converges.

The Hopf-Rinow theorem, which we will state and prove below, shows that these two notions of completeness are equivalent for connected Riemannian manifolds. Before we prove it, let us establish a preliminary result, which will have other important consequences besides the Hopf-Rinow theorem itself.

![bo_d7dtff491nqc73eq8m7g_178_306_204_911_294_0.jpg](images/bo_d7dtff491nqc73eq8m7g_178_306_204_911_294_0.jpg)

Fig. 6.11: Proof that \( {\left. \gamma \right| }_{\left\lbrack  0,\varepsilon \right\rbrack  } \) aims at \( q \)

Lemma 6.18. Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold, and there is a point \( p \in  M \) such that \( {\exp }_{p} \) is defined on the whole tangent space \( {T}_{p}M \) .

(a) Given any other \( q \in  M \) , there is a minimizing geodesic segment from \( p \) to \( q \) .

(b) \( M \) is metrically complete.

Proof. Let \( q \in  M \) be arbitrary. If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a geodesic segment starting at \( p \) , let us say that \( \gamma \) aims at \( q \) if \( \gamma \) is minimizing and

\[
{d}_{g}\left( {p, q}\right)  = {d}_{g}\left( {p,\gamma \left( b\right) }\right)  + {d}_{g}\left( {\gamma \left( b\right) , q}\right) . \tag{6.9}
\]

(This would be the case, for example, if \( \gamma \) were an initial segment of a minimizing geodesic from \( p \) to \( q \) ; but we are not assuming that.) To prove (a), it suffices to show that there is a geodesic segment \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) that begins at \( p \) , aims at \( q \) , and has length equal to \( {d}_{g}\left( {p, q}\right) \) , for then the fact that \( \gamma \) is minimizing means that \( {d}_{g}\left( {p,\gamma \left( b\right) }\right)  = {L}_{g}\left( \gamma \right)  = {d}_{g}\left( {p, q}\right) \) , and (6.9) becomes

\[
{d}_{g}\left( {p, q}\right)  = {d}_{g}\left( {p, q}\right)  + {d}_{g}\left( {\gamma \left( b\right) , q}\right) ,
\]

which implies \( \gamma \left( b\right)  = q \) . Since \( \gamma \) is a segment from \( p \) to \( q \) of length \( {d}_{g}\left( {p, q}\right) \) , it is the desired minimizing geodesic segment.

Choose \( \varepsilon  > 0 \) such that there is a closed geodesic ball \( {\bar{B}}_{\varepsilon }\left( p\right) \) around \( p \) that does not contain \( q \) . Since the distance function on a metric space is continuous, there is a point \( x \) in the geodesic sphere \( {S}_{\varepsilon }\left( p\right) \) where \( {d}_{g}\left( {x, q}\right) \) attains its minimum on the compact set \( {S}_{\varepsilon }\left( p\right) \) . Let \( \gamma \) be the maximal unit-speed geodesic whose restriction to \( \left\lbrack  {0,\varepsilon }\right\rbrack \) is the radial geodesic segment from \( p \) to \( x \) (Fig. 6.11); by assumption, \( \gamma \) is defined for all \( t \in  \mathbb{R} \) .

We begin by showing that \( {\left. \gamma \right| }_{\left\lbrack  0,\varepsilon \right\rbrack  } \) aims at \( q \) . Since it is minimizing by Proposition 6.11 (noting that every closed geodesic ball is contained in a larger open one), we need only show that (6.9) holds with \( b = \varepsilon \) , or

\[
{d}_{g}\left( {p, q}\right)  = {d}_{g}\left( {p, x}\right)  + {d}_{g}\left( {x, q}\right) . \tag{6.10}
\]

To this end, let \( \sigma  : \left\lbrack  {{a}_{0},{b}_{0}}\right\rbrack   \rightarrow  M \) be any admissible curve from \( p \) to \( q \) . Let \( {t}_{0} \) be the first time \( \sigma \) hits \( {S}_{\varepsilon }\left( p\right) \) , and let \( {\sigma }_{1} \) and \( {\sigma }_{2} \) denote the restrictions of \( {\sigma }_{1} \) to \( \left\lbrack  {{a}_{0},{t}_{0}}\right\rbrack \) and \( \left\lbrack  {{t}_{0},{b}_{0}}\right\rbrack \) , respectively (Fig. 6.11). Since every point in \( {S}_{\varepsilon }\left( p\right) \) is at a distance \( \varepsilon \) from \( p \) , we have \( {L}_{g}\left( {\sigma }_{1}\right)  \geq  {d}_{g}\left( {p,\sigma \left( {t}_{0}\right) }\right)  = {d}_{g}\left( {p, x}\right) \) ; and by our choice of \( x \) we have \( {L}_{g}\left( {\sigma }_{2}\right)  \geq  {d}_{g}\left( {\sigma \left( {t}_{0}\right) , q}\right)  \geq  {d}_{g}\left( {x, q}\right) \) . Putting these two inequalities together yields

\[
{L}_{g}\left( \sigma \right)  = {L}_{g}\left( {\sigma }_{1}\right)  + {L}_{g}\left( {\sigma }_{2}\right)  \geq  {d}_{g}\left( {p, x}\right)  + {d}_{g}\left( {x, q}\right) .
\]

![bo_d7dtff491nqc73eq8m7g_179_295_185_943_308_0.jpg](images/bo_d7dtff491nqc73eq8m7g_179_295_185_943_308_0.jpg)

Fig. 6.12: Proof that \( A = T \)

Taking the infimum over all such \( \sigma \) , we find that \( {d}_{g}\left( {p, q}\right)  \geq  {d}_{g}\left( {p, x}\right)  + {d}_{g}\left( {x, q}\right) \) . The opposite inequality is just the triangle inequality, so (6.10) holds.

Now let \( T = {d}_{g}\left( {p, q}\right) \) and

\[
\mathcal{A} = \left\{  {b \in  \left\lbrack  {0, T}\right\rbrack   : {\left. \gamma \right| }_{\left\lbrack  0, b\right\rbrack  }\text{ aims at }q}\right\}  .
\]

We have just shown that \( \varepsilon  \in  \mathcal{A} \) . Let \( A = \sup \mathcal{A} \geq  \varepsilon \) . By continuity of the distance function, it is easy to see that \( \mathcal{A} \) is closed in \( \left\lbrack  {0, T}\right\rbrack \) , and therefore \( A \in  \mathcal{A} \) . If \( A = T \) , then \( {\left. \gamma \right| }_{\left\lbrack  0, T\right\rbrack  } \) is a geodesic of length \( T = {d}_{g}\left( {p, q}\right) \) that aims at \( q \) , and by the remark above we are done. So we assume \( A < T \) and derive a contradiction.

Let \( y = \gamma \left( A\right) \) , and choose \( \delta  > 0 \) such that there is a closed geodesic ball \( {\bar{B}}_{\delta }\left( y\right) \) around \( y \) , small enough that it does not contain \( q \) (Fig. 6.12). The fact that \( A \in  \mathcal{A} \) means that

\[
{d}_{g}\left( {y, q}\right)  = {d}_{g}\left( {p, q}\right)  - {d}_{g}\left( {p, y}\right)  = T - A.
\]

Let \( z \in  {S}_{\delta }\left( y\right) \) be a point where \( {d}_{g}\left( {z, q}\right) \) attains its minimum, and let \( \tau  : \left\lbrack  {0,\delta }\right\rbrack   \rightarrow  M \) be the unit-speed radial geodesic from \( y \) to \( z \) . By exactly the same argument as before, \( \tau \) aims at \( q \) , so

\[
{d}_{g}\left( {z, q}\right)  = {d}_{g}\left( {y, q}\right)  - {d}_{g}\left( {y, z}\right)  = \left( {T - A}\right)  - \delta . \tag{6.11}
\]

By the triangle inequality and (6.11),

\[
{d}_{g}\left( {p, z}\right)  \geq  {d}_{g}\left( {p, q}\right)  - {d}_{g}\left( {z, q}\right)
\]

\[
= T - \left( {T - A - \delta }\right)  = A + \delta .
\]

Therefore, the admissible curve consisting of \( {\left. \gamma \right| }_{\left\lbrack  0, A\right\rbrack  } \) (of length \( A \) ) followed by \( \tau \) (of length \( \delta \) ) is a minimizing curve from \( p \) to \( z \) . This means that it has no corners, so \( z \) must lie on \( \gamma \) , and in fact, \( z = \gamma \left( {A + \delta }\right) \) . But then (6.11) says that

\[
{d}_{g}\left( {p, q}\right)  = T = \left( {A + \delta }\right)  + {d}_{g}\left( {z, q}\right)  = {d}_{g}\left( {p, z}\right)  + {d}_{g}\left( {z, q}\right) ,
\]

![bo_d7dtff491nqc73eq8m7g_180_271_187_945_603_0.jpg](images/bo_d7dtff491nqc73eq8m7g_180_271_187_945_603_0.jpg)

Fig. 6.13: Cauchy sequences converge

so \( {\left. \gamma \right| }_{\left\lbrack  0, A + \delta \right\rbrack  } \) aims at \( q \) and \( A + \delta  \in  \mathcal{A} \) , which is a contradiction. This completes the proof of (a).

To prove (b), we need to show that every Cauchy sequence in \( M \) converges. Let \( \left( {q}_{i}\right) \) be a Cauchy sequence in \( M \) . For each \( i \) , let \( {\gamma }_{i}\left( t\right)  = {\exp }_{p}\left( {t{v}_{i}}\right) \) be a unit-speed minimizing geodesic from \( p \) to \( {q}_{i} \) , and let \( {d}_{i} = {d}_{g}\left( {p,{q}_{i}}\right) \) , so that \( {q}_{i} = {\exp }_{p}\left( {{d}_{i}{v}_{i}}\right) \) (Fig. 6.13). The sequence \( \left( {d}_{i}\right) \) is bounded in \( \mathbb{R} \) (because Cauchy sequences in a metric space are bounded), and the sequence \( \left( {v}_{i}\right) \) consists of unit vectors in \( {T}_{p}M \) , so the sequence of vectors \( \left( {{d}_{i}{v}_{i}}\right) \) in \( {T}_{p}M \) is bounded. Therefore a subsequence \( \left( {{d}_{{i}_{k}}{v}_{{i}_{k}}}\right) \) converges to some \( v \in  {T}_{p}M \) . By continuity of the exponential map, \( {q}_{{i}_{k}} = \; {\exp }_{p}\left( {{d}_{{i}_{k}}{v}_{{i}_{k}}}\right)  \rightarrow  {\exp }_{p}v \) , and since the original sequence \( \left( {q}_{i}\right) \) is Cauchy, it converges to the same limit.

The next theorem is the main result of this section.

Theorem 6.19 (Hopf-Rinow). A connected Riemannian manifold is metrically complete if and only if it is geodesically complete.

Proof. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold. Suppose first that \( M \) is geodesically complete. Then in particular, it satisfies the hypothesis of Lemma 6.18, so it is metrically complete.

Conversely, suppose \( M \) is metrically complete, and assume for the sake of contradiction that it is not geodesically complete. Then there is some unit-speed geodesic \( \gamma  : \lbrack 0, b) \rightarrow  M \) that has no extension to a geodesic on any interval \( \left\lbrack  {0,{b}^{\prime }}\right) \) for \( {b}^{\prime } > b \) . Let \( \left( {t}_{i}\right) \) be any increasing sequence in \( \lbrack 0, b) \) that approaches \( b \) , and set \( {q}_{i} = \gamma \left( {t}_{i}\right) \) . Since \( \gamma \) is parametrized by arc length, the length of \( {\left. \gamma \right| }_{\left\lbrack  {t}_{i},{t}_{j}\right\rbrack  } \) is exactly \( \left| {{t}_{j} - {t}_{i}}\right| \) , so \( {d}_{g}\left( {{q}_{i},{q}_{j}}\right)  \leq  \left| {{t}_{j} - {t}_{i}}\right| \) and \( \left( {q}_{i}\right) \) is a Cauchy sequence in \( M \) . By completeness, \( \left( {q}_{i}\right) \) converges to some point \( q \in  M \) .

![bo_d7dtff491nqc73eq8m7g_181_497_186_537_422_0.jpg](images/bo_d7dtff491nqc73eq8m7g_181_497_186_537_422_0.jpg)

Fig. 6.14: \( \gamma \) extends past \( q \)

Let \( W \) be a uniformly \( \delta \) -normal neighborhood of \( q \) for some \( \delta  > 0 \) . Choose \( j \) large enough that \( {t}_{j} > b - \delta \) and \( {q}_{j} \in  W \) (Fig. 6.14). The fact that \( {B}_{\delta }\left( {q}_{j}\right) \) is a geodesic ball means that every unit-speed geodesic starting at \( {q}_{j} \) exists at least for \( t \in  \lbrack 0,\delta ) \) . In particular, this is true of the geodesic \( \sigma \) with \( \sigma \left( 0\right)  = {q}_{j} \) and \( {\sigma }^{\prime }\left( 0\right)  = \; {\gamma }^{\prime }\left( {t}_{j}\right) \) . Define \( \widetilde{\gamma } : \left\lbrack  {0,{t}_{j} + \delta }\right)  \rightarrow  M \) by

\[
\widetilde{\gamma }\left( t\right)  = \left\{  \begin{array}{ll} \gamma \left( t\right) , & t \in  \lbrack 0, b), \\  \sigma \left( {t - {t}_{j}}\right) , & t \in  \left( {{t}_{j} - \delta ,{t}_{j} + \delta }\right) . \end{array}\right.
\]

Note that both expressions on the right-hand side are geodesics, and they have the same position and velocity when \( t = {t}_{j} \) . Therefore, by uniqueness of geodesics, the two definitions agree where they overlap. Since \( {t}_{j} + \delta  > b,\widetilde{\gamma } \) is an extension of \( \gamma \) past \( b \) , which is a contradiction.

A connected Riemannian manifold is simply said to be complete if it is either geodesically complete or metrically complete; the Hopf-Rinow theorem then implies that it is both. For disconnected manifolds, we interpret "complete" to mean geodesically complete, which is equivalent to the requirement that each component be a complete metric space. As mentioned in the previous chapter, complete manifolds are the natural setting for global questions in Riemannian geometry.

We conclude this section by stating three important corollaries, whose proofs are easy applications of Lemma 6.18 and the Hopf-Rinow theorem.

Corollary 6.20. If \( M \) is a connected Riemannian manifold and there exists a point \( p \in  M \) such that the restricted exponential map \( {\exp }_{p} \) is defined on all of \( {T}_{p}M \) , then \( M \) is complete.

Corollary 6.21. If \( M \) is a complete, connected Riemannian manifold, then any two points in \( M \) can be joined by a minimizing geodesic segment.

Corollary 6.22. If \( M \) is a compact Riemannian manifold, then every maximal geodesic in \( M \) is defined for all time.

![bo_d7dtff491nqc73eq8m7g_182_467_186_598_856_0.jpg](images/bo_d7dtff491nqc73eq8m7g_182_467_186_598_856_0.jpg)

Fig. 6.15: Lifting geodesics

The Hopf-Rinow theorem and Corollary 6.20 are key ingredients in the following theorem about Riemannian covering maps. This theorem will play a key role in the proofs of some of the local-to-global theorems in Chapter 12.

Theorem 6.23. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( \left( {M, g}\right) \) are connected Riemannian manifolds with \( \widetilde{M} \) complete, and \( \pi  : \widetilde{M} \rightarrow  M \) is a local isometry. Then \( M \) is complete and \( \pi \) is a Riemannian covering map.

Proof. A fundamental property of covering maps is the path-lifting property (Prop. A.54(b)): if \( \pi \) is a covering map, then every continuous path \( \gamma  : I \rightarrow  M \) lifts to a path \( \widetilde{\gamma } \) in \( \widetilde{M} \) such that \( \pi  \circ  \widetilde{\gamma } = \gamma \) . We begin by proving that \( \pi \) possesses the path-lifting property for geodesics (Fig. 6.15): if \( p \in  M \) is a point in the image of \( \pi ,\gamma  : I \rightarrow  M \) is any geodesic starting at \( p \) , and \( \widetilde{p} \) is any point in \( {\pi }^{-1}\left( p\right) \) , then \( \gamma \) has a unique lift starting at \( \widetilde{p} \) . The lifted curve is necessarily also a geodesic because \( \pi \) is a local isometry.

To prove the path-lifting property for geodesics, suppose \( p \in  \pi \left( M\right) \) and \( \widetilde{p} \in \; {\pi }^{-1}\left( p\right) \) , and let \( \gamma  : I \rightarrow  M \) be any geodesic with \( p = \gamma \left( 0\right) \) . Let \( v = {\gamma }^{\prime }\left( 0\right) \) and \( \widetilde{v} = {\left( d{\pi }_{\widetilde{p}}\right) }^{-1}\left( v\right)  \in  {T}_{\widetilde{p}}\widetilde{M} \) (which is well defined because \( d{\pi }_{\widetilde{p}} \) is an isomorphism), and let \( \widetilde{\gamma } \) be the geodesic in \( \widetilde{M} \) with initial point \( \widetilde{p} \) and initial velocity \( \widetilde{v} \) . Because \( \widetilde{M} \) is complete, \( \widetilde{\gamma } \) is defined on all of \( \mathbb{R} \) . Since \( \pi \) is a local isometry, it takes geodesics to geodesics; and since by construction \( \pi \left( {\widetilde{\gamma }\left( 0\right) }\right)  = \gamma \left( 0\right) \) and \( d{\pi }_{\widetilde{p}}\left( {{\widetilde{\gamma }}^{\prime }\left( 0\right) }\right)  = {\gamma }^{\prime }\left( 0\right) \) , we must have \( \pi  \circ  \widetilde{\gamma } = \gamma \) on \( I \) , so \( {\left. \widetilde{\gamma }\right| }_{I} \) is a lift of \( \gamma \) starting at \( \widetilde{p} \) .

![bo_d7dtff491nqc73eq8m7g_183_181_189_570_663_0.jpg](images/bo_d7dtff491nqc73eq8m7g_183_181_189_570_663_0.jpg)

Fig. 6.16: Proof that \( {\widetilde{U}}_{\alpha } \cap  {\widetilde{U}}_{\beta } = \varnothing \)

![bo_d7dtff491nqc73eq8m7g_183_814_301_398_552_0.jpg](images/bo_d7dtff491nqc73eq8m7g_183_814_301_398_552_0.jpg)

Fig. 6.17: Proof that \( {\pi }^{-1}\left( U\right)  \subseteq  \mathop{\bigcup }\limits_{\alpha }{\widetilde{U}}_{\alpha } \)

To show that \( M \) is complete, let \( p \) be any point in the image of \( \pi \) . If \( \gamma  : I \rightarrow  M \) is any geodesic starting at \( p \) , then \( \gamma \) has a lift \( \widetilde{\gamma } : I \rightarrow  \widetilde{M} \) . Because \( \widetilde{M} \) is complete, \( \pi  \circ  \widetilde{\gamma } \) is a geodesic defined for all \( t \) that coincides with \( \gamma \) on \( I \) , so \( \gamma \) extends to all of \( \mathbb{R} \) . Thus \( M \) is complete by Corollary 6.20.

Next we show that \( \pi \) is surjective. Choose some point \( \widetilde{p} \in  \widetilde{M} \) , write \( p = \pi \left( \widetilde{p}\right) \) , and let \( q \in  M \) be arbitrary. Because \( M \) is connected and complete, there is a minimizing unit-speed geodesic segment \( \gamma \) from \( p \) to \( q \) . Letting \( \widetilde{\gamma } \) be the lift of \( \gamma \) starting at \( \widetilde{p} \) and \( r = {d}_{g}\left( {p, q}\right) \) , we have \( \pi \left( {\widetilde{\gamma }\left( r\right) }\right)  = \gamma \left( r\right)  = q \) , so \( q \) is in the image of \( \pi \) .

To show that \( \pi \) is a smooth covering map, we need to show that every point of \( M \) has a neighborhood \( U \) that is evenly covered, which means that \( {\pi }^{-1}\left( U\right) \) is a disjoint union of connected open sets \( {\widetilde{U}}_{\alpha } \) such that \( {\left. \pi \right| }_{{\widetilde{U}}_{\alpha }} : {\widetilde{U}}_{\alpha } \rightarrow  U \) is a diffeomorphism. We will show, in fact, that every geodesic ball is evenly covered.

Let \( p \in  M \) , and let \( U = {B}_{\varepsilon }\left( p\right) \) be a geodesic ball centered at \( p \) . Write \( {\pi }^{-1}\left( p\right)  = \; {\left\{  {\widetilde{p}}_{\alpha }\right\}  }_{\alpha  \in  A} \) , and for each \( \alpha \) let \( {\widetilde{U}}_{\alpha } \) denote the metric ball of radius \( \varepsilon \) around \( {\widetilde{p}}_{\alpha } \) (we are not claiming that \( {\widetilde{U}}_{\alpha } \) is a geodesic ball). The first step is to show that the various sets \( {\widetilde{U}}_{\alpha } \) are disjoint. For every \( \alpha  \neq  \beta \) , there is a minimizing geodesic segment \( \widetilde{\gamma } \) from \( {\widetilde{p}}_{\alpha } \) to \( {\widetilde{p}}_{\beta } \) because \( \widetilde{M} \) is complete. The projected curve \( \gamma  = \pi  \circ  \widetilde{\gamma } \) is a geodesic segment that starts and ends at \( p \) (Fig. 6.16), whose length is the same as that of \( \widetilde{\gamma } \) . Such a geodesic must leave \( U \) and reenter it (since all geodesics passing through \( p \) and lying in \( U \) are radial line segments), and thus must have length at least \( {2\varepsilon } \) . This means that \( {d}_{\widetilde{g}}\left( {{\widetilde{p}}_{\alpha },{\widetilde{p}}_{\beta }}\right)  \geq  {2\varepsilon } \) , and thus by the triangle inequality, \( {\widetilde{U}}_{\alpha } \cap  {\widetilde{U}}_{\beta } = \varnothing \) .

The next step is to show that \( {\pi }^{-1}\left( U\right)  = \mathop{\bigcup }\limits_{\alpha }{\widetilde{U}}_{\alpha } \) . If \( \widetilde{q} \) is any point in \( {\widetilde{U}}_{\alpha } \) , then there is a geodesic \( \widetilde{\gamma } \) of length less than \( \varepsilon \) from \( {\widetilde{p}}_{\alpha } \) to \( \widetilde{q} \) , and then \( \pi  \circ  \widetilde{\gamma } \) is a geodesic of the same length from \( p \) to \( \pi \left( \widetilde{q}\right) \) , showing that \( \pi \left( \widetilde{q}\right)  \in  U \) . It follows that \( \mathop{\bigcup }\limits_{\alpha }{\widetilde{U}}_{\alpha } \subseteq \; {\pi }^{-1}\left( U\right) \) .

Conversely, suppose \( \widetilde{q} \in  {\pi }^{-1}\left( U\right) \) , and set \( q = \pi \left( \widetilde{q}\right) \) . This means that \( q \in  U \) , so there is a minimizing radial geodesic \( \gamma \) in \( U \) from \( q \) to \( p \) , and \( r = {d}_{g}\left( {q, p}\right)  < \varepsilon \) . Let \( \widetilde{\gamma } \) be the lift of \( \gamma \) starting at \( \widetilde{q} \) (Fig. 6.17). It follows that \( \pi \left( {\widetilde{\gamma }\left( r\right) }\right)  = \gamma \left( r\right)  = p \) . Therefore \( \widetilde{\gamma }\left( r\right)  = {\widetilde{p}}_{\alpha } \) for some \( \alpha \) , and \( {d}_{\widetilde{g}}\left( {\widetilde{q},{\widetilde{p}}_{\alpha }}\right)  \leq  {L}_{g}\left( \widetilde{\gamma }\right)  = r < \varepsilon \) , so \( \widetilde{q} \in  {\widetilde{U}}_{\alpha } \) .

It remains only to show that \( \pi  : {\widetilde{U}}_{\alpha } \rightarrow  U \) is a diffeomorphism for each \( \alpha \) . It is certainly a local diffeomorphism (because \( \pi \) is). It is bijective because its inverse can be constructed explicitly: it is the map sending each radial geodesic starting at \( p \) to its lift starting at \( {\widetilde{p}}_{\alpha } \) . This completes the proof.

Corollary 6.24. Suppose \( \widetilde{M} \) and \( M \) are connected Riemannian manifolds, and \( \pi  : \widetilde{M} \rightarrow  M \) is a Riemannian covering map. Then \( M \) is complete if and only if \( \widetilde{M} \) is complete.

Proof. A Riemannian covering map is, in particular, a local isometry. Thus if \( \widetilde{M} \) is complete, \( \pi \) satisfies the hypotheses of Theorem 6.23, which implies that \( M \) is also complete.

Conversely, suppose \( M \) is complete. Let \( \widetilde{p} \in  \widetilde{M} \) and \( \widetilde{v} \in  {T}_{p}\widetilde{M} \) be arbitrary, and let \( p = \pi \left( \widetilde{p}\right) \) and \( v = d{\pi }_{\widetilde{p}}\left( \widetilde{v}\right) \) . Completeness of \( M \) implies that the geodesic \( \gamma \) with \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) is defined for all \( t \in  \mathbb{R} \) , and then its lift \( \widetilde{\gamma } : \mathbb{R} \rightarrow  \widetilde{M} \) starting at \( \widetilde{p} \) is a geodesic in \( \widetilde{M} \) with initial velocity \( \widetilde{v} \) , also defined for all \( t \) .

Corollary 6.21 to the Hopf-Rinow theorem shows that any two points in a complete, connected Riemannian manifold can be joined by a minimizing geodesic segment. The next proposition gives a refinement of that statement.

Proposition 6.25. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold, and \( p, q \in  M \) . Every path-homotopy class of paths from \( p \) to \( q \) contains a geodesic segment \( \gamma \) that minimizes length among all admissible curves in the same path-homotopy class.

Proof. Let \( \pi  : \widetilde{M} \rightarrow  M \) be the universal covering manifold of \( M \) , endowed with the pullback metric \( \widetilde{g} = {\pi }^{ * }g \) . Given \( p, q \in  M \) and a path \( \sigma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) from \( p \) to \( q \) , choose a point \( \widetilde{p} \in  {\pi }^{-1}\left( p\right) \) , and let \( \widetilde{\sigma } : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \widetilde{M} \) be the lift of \( \sigma \) starting at \( \widetilde{p} \) , and set \( \widetilde{q} = \widetilde{\sigma }\left( 1\right) \) . By Corollary 6.21, there is a minimizing \( \widetilde{g} \) -geodesic segment \( \widetilde{\gamma } \) from \( \widetilde{p} \) to \( \widetilde{q} \) , and because \( \pi \) is a local isometry, \( \gamma  = \pi  \circ  \widetilde{\gamma } \) is a geodesic in \( M \) from \( p \) to \( q \) . If \( {\gamma }_{1} \) is any other admissible curve from \( p \) to \( q \) in the same path-homotopy class, then by the monodromy theorem (Prop. A.54(c)), its lift \( {\widetilde{\gamma }}_{1} \) starting at \( \widetilde{p} \) also ends at \( \widetilde{q} \) . Thus \( {\widetilde{\gamma }}_{1} \) is no longer than \( \widetilde{\gamma } \) , which implies \( {\gamma }_{1} \) is no longer than \( \gamma \) .

## Closed Geodesics

Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold. A closed geodesic in \( M \) is a nonconstant geodesic segment \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) such that \( \gamma \left( a\right)  = \gamma \left( b\right) \) and \( {\gamma }^{\prime }\left( a\right)  = \; {\gamma }^{\prime }\left( b\right) \) .

---

- Exercise 6.26. Show that a geodesic segment is closed if and only if it extends to a periodic geodesic defined on all of \( \mathbb{R} \) .

---

Round spheres have the remarkable property that all of their geodesics are closed when restricted to appropriate intervals. Of course, this is not typically the case, even for compact Riemannian manifolds; but it is natural to wonder whether closed geodesics exist in more general manifolds. Much work has been done in Riemannian geometry to determine how many closed geodesics exist in various situations. Here we can only touch on the simplest case; these results will be useful in some of the proofs of local-to-global theorems in Chapter 12.

A continuous path \( \sigma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) is called a loop if \( \sigma \left( 0\right)  = \sigma \left( 1\right) \) . Two loops \( {\sigma }_{0},{\sigma }_{1} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) are said to be freely homotopic if they are homotopic through closed paths (but not necessarily preserving the base point), that is, if there exists a homotopy \( H : \left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) satisfying

(6.12)

\[
H\left( {s,0}\right)  = {\sigma }_{0}\left( s\right) \text{ and }H\left( {s,1}\right)  = {\sigma }_{1}\left( s\right) \text{ for all }s \in  \left\lbrack  {0,1}\right\rbrack  ,
\]

\[
H\left( {0, t}\right)  = H\left( {1, t}\right) \text{ for all }t \in  \left\lbrack  {0,1}\right\rbrack  .
\]

This is an equivalence relation on the set of all loops in \( M \) , and an equivalence class is called a free homotopy class. The trivial free homotopy class is the equivalence class of any constant path.

Exercise 6.27. Given a connected manifold \( M \) and a point \( x \in  M \) , show that a loop based at \( x \) represents the trivial free homotopy class if and only if it represents the identity element of \( {\pi }_{1}\left( {M, x}\right) \) .

The next proposition shows that closed geodesics are easy to find on compact Riemannian manifolds that are not simply connected.

Proposition 6.28 (Existence of Closed Geodesics). Suppose \( \left( {M, g}\right) \) is a compact, connected Riemannian manifold. Every nontrivial free homotopy class in \( M \) is represented by a closed geodesic that has minimum length among all admissible loops in the given free homotopy class.

Proof. Problem 6-17.

The previous proposition guarantees the existence of at least one closed geodesic on every non-simply-connected compact Riemannian manifold. In fact, it was proved in 1951 by the Russian mathematicians Lazar Lyusternik and Abram Fet that closed geodesics exist on every compact Riemannian manifold, but the proof in the simply connected case is considerably harder. Proofs can be found in [Jos17] and [Kli95].

## Distance Functions

Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold and \( S \subseteq  M \) is any subset. For each point \( x \in  M \) , we define the distance from \( \mathbf{x} \) to \( \mathbf{S} \) to be

\[
{d}_{g}\left( {x, S}\right)  = \inf \left\{  {{d}_{g}\left( {x, p}\right)  : p \in  S}\right\}  .
\]

Lemma 6.29. Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold and \( S \subseteq  M \) is any subset.

(a) \( {d}_{g}\left( {x, S}\right)  \leq  {d}_{g}\left( {x, y}\right)  + {d}_{g}\left( {y, S}\right) \) for all \( x, y \in  M \) .

(b) \( x \mapsto  {d}_{g}\left( {x, S}\right) \) is a continuous function on \( M \) .

Exercise 6.30. Prove the preceding lemma.

The simplest example of a distance function occurs when the set \( S \) is just a singleton, \( S = \{ p\} \) . Inside a geodesic ball around \( p \) , Corollary 6.12 shows that \( {d}_{g}\left( {x, S}\right)  = r\left( x\right) \) , the radial distance function, and Corollary 6.10 shows that it has unit gradient where it it smooth (everywhere inside the geodesic ball except at \( p \) itself). The next theorem is a far-reaching generalization of that result.

Theorem 6.31. Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold, \( S \subseteq  M \) is arbitrary, and \( f : M \rightarrow  \lbrack 0,\infty ) \) is the distance to \( S \) , that is, \( f\left( x\right)  = {d}_{g}\left( {x, S}\right) \) for all \( x \in  M \) . If \( f \) is continuously differentiable on some open subset \( U \subseteq  M \smallsetminus  S \) , then \( \left| {\operatorname{grad}f}\right|  \equiv  1 \) on \( U \) .

Proof. Suppose \( U \subseteq  M \smallsetminus  S \) is an open subset on which \( f \) is continuously differentiable, and \( x \in  U \) . We will show first that \( \left| {\operatorname{grad}f{\left. \right| }_{x}}\right|  \leq  1 \) , and then that \( \left| {\operatorname{grad}f{\left. \right| }_{x}}\right|  \geq  1 \) .

To prove the first inequality, we may assume grad \( {\left. f\right| }_{x} \neq  0 \) , for otherwise the inequality is trivial. Let \( v \in  {T}_{x}M \) be any unit vector, and let \( \gamma \) be the unit-speed geodesic with \( \gamma \left( 0\right)  = x \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) . Then for every positive \( t \) sufficiently small that \( {\left. \gamma \right| }_{\left\lbrack  0, t\right\rbrack  } \) is minimizing, Lemma 6.29 gives \( {d}_{g}\left( {\gamma \left( t\right) , S}\right)  \leq  {d}_{g}\left( {\gamma \left( t\right) ,\gamma \left( 0\right) }\right)  + \; {d}_{g}\left( {\gamma \left( 0\right) , S}\right) \) , or equivalently \( f\left( {\gamma \left( t\right) }\right)  \leq  t + f\left( {\gamma \left( 0\right) }\right) \) . Therefore, since \( f \) is differentiable at \( x \) ,

\[
{\left. \frac{d}{dt}\right| }_{t = 0}f\left( {\gamma \left( t\right) }\right)  = \mathop{\lim }\limits_{{t \searrow  0}}\frac{f\left( {\gamma \left( t\right) }\right)  - f\left( {\gamma \left( 0\right) }\right) }{t} \leq  1.
\]

In particular, taking \( v = \left( {\left. \operatorname{grad}f\right| }_{x}\right) /\left| {\left. \operatorname{grad}f\right| }_{x}\right| \) (the unit vector in the direction of grad \( f{|}_{x} \) ), we obtain

\[
{\left. \frac{d}{dt}\right| }_{t = 0}f\left( {\gamma \left( t\right) }\right)  = d{f}_{x}\left( {{\gamma }^{\prime }\left( 0\right) }\right)  = \left\langle  {{\left. \operatorname{grad}f\right| }_{x}, v}\right\rangle   = {\left| \operatorname{grad}f\right| }_{x}.
\]

This proves that \( \left| {\operatorname{grad}f{\left. \right| }_{x}}\right|  \leq  1 \) .

To prove the reverse inequality, assume for the sake of contradiction that \( \left| {\operatorname{grad}f{\left. \right| }_{x}}\right|  < 1 \) . Since we are assuming that \( \operatorname{grad}f \) is continuous on \( U \) , there exist \( \delta ,\varepsilon  > 0 \) such that \( {\bar{B}}_{\varepsilon }\left( x\right) \) is a closed geodesic ball contained in \( U \) and \( \left| {\operatorname{grad}f}\right|  \leq  1 - \delta \) on \( {\bar{B}}_{\varepsilon }\left( x\right) \) . Let \( c \) be a positive constant less than \( {\varepsilon \delta } \) . By definition of \( {d}_{g}\left( {x, S}\right) \) , there is an admissible curve \( \alpha  : \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) (which we may assume to be parametrized by arc length) such that \( \alpha \left( 0\right)  = x,\alpha \left( b\right)  \in  S \) , and \( b = {L}_{g}\left( \alpha \right)  < {d}_{g}\left( {x, S}\right)  + c \) .

Since we are assuming \( {\bar{B}}_{\varepsilon }\left( x\right)  \subseteq  U \subseteq  M \smallsetminus  S \) , we have that \( b > \varepsilon \) , so \( {\left. \alpha \right| }_{\left\lbrack  \varepsilon , b\right\rbrack  } \) is an admissible curve from \( \alpha \left( \varepsilon \right) \) to \( S \) . On the one hand,

\[
{d}_{g}\left( {\alpha \left( \varepsilon \right) , S}\right)  \leq  {L}_{g}\left( {\left. \alpha \right| }_{\left\lbrack  \varepsilon , b\right\rbrack  }\right)  = b - \varepsilon  < {d}_{g}\left( {x, S}\right)  + c - \varepsilon . \tag{6.13}
\]

On the other hand, for \( 0 \leq  t \leq  \varepsilon \) , the fact that \( \alpha \left( t\right)  \in  {\bar{B}}_{\varepsilon }\left( x\right) \) implies

\[
\left| {\frac{d}{dt}f\left( {\alpha \left( t\right) }\right) }\right|  = \left| \left\langle  {\operatorname{grad}f\left| {{\alpha }_{\left( t\right) },{\alpha }^{\prime }\left( t\right) }\right| }\right\rangle  \right|  \leq  {\left| \operatorname{grad}f\right| }_{\alpha \left( t\right) }\left| {{\alpha }^{\prime }\left( t\right) }\right|  \leq  1 - \delta .
\]

Thus \( f\left( {\alpha \left( t\right) }\right)  \geq  f\left( x\right)  - \left( {1 - \delta }\right) t \) for all such \( t \) . In particular, for \( t = \varepsilon \) , this means that

\[
{d}_{g}\left( {\alpha \left( \varepsilon \right) , S}\right)  \geq  {d}_{g}\left( {x, S}\right)  - \left( {1 - \delta }\right) \varepsilon . \tag{6.14}
\]

Combining (6.13) and (6.14) yields \( c > {\varepsilon \delta } \) , contradicting our choice of \( c \) .

Motivated by the previous theorem, if \( \left( {M, g}\right) \) is a Riemannian manifold and \( U \subseteq \; M \) is an open subset, we define a local distance function on \( U \) to be a continuously differentiable function \( f : U \rightarrow  \mathbb{R} \) such that \( {\left. \left. \text{ grad }f\right| \right| }_{g} \equiv  1 \) in \( U \) . Theorem 6.34 and Corollary 6.35 below will justify this terminology. But first, we develop some important general properties of local distance functions.

Theorem 6.32. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( f \) is a smooth local distance function on an open subset \( U \subseteq  M \) . Then \( {\nabla }_{\text{ grad }f}\left( {\operatorname{grad}f}\right)  \equiv  0 \) , and each integral curve of grad \( f \) is a unit-speed geodesic.

Proof. Let \( F \in  \mathcal{X}\left( U\right) \) denote the unit vector field grad \( f \) . The definition of the gradient shows that for every vector field \( W \) , we have

\[
{Wf} = {df}\left( W\right)  = \langle F, W\rangle , \tag{6.15}
\]

and therefore

\[
{Ff} = \langle F, F\rangle  = {\left| \operatorname{grad}f\right| }^{2} = 1. \tag{6.16}
\]

For every smooth vector field \( W \) on \( U \) , we have

\[
\langle W,{\nabla }_{F}F\rangle  = F\langle W, F\rangle  - \left\langle  {{\nabla }_{F}W, F}\right\rangle  \;\left( {\text{ compatibility with }g}\right)
\]

\[
= {FWf} - \langle \left\lbrack  {F, W}\right\rbrack  , F\rangle  - \left\langle  {{\nabla }_{W}F, F}\right\rangle  \;\left( {\left( {6.15}\right) \text{ , symmetry of }\nabla }\right)
\]

\[
= {FWf} - \left\lbrack  {F, W}\right\rbrack  f - \frac{1}{2}W{\left| F\right| }^{2}\;\left( {\left( {6.15}\right) \text{ , compatibility with }g}\right)
\]

\[
= {WFf} - \frac{1}{2}W{\left| F\right| }^{2}\;\left( {\text{ definition of }\left\lbrack  {F, W}\right\rbrack  }\right)
\]

\[
= 0
\]

\[
\text{ (since }{Ff} \equiv  {\left| F\right| }^{2} \equiv  1\text{ ). }
\]

Since \( W \) is arbitrary, this proves that \( {\nabla }_{F}F \equiv  0 \) .

If \( \gamma  : I \rightarrow  U \) is an integral curve of \( F \) , then the fact that \( {\gamma }^{\prime } \) is extendible implies

\[
{D}_{t}{\gamma }^{\prime }\left( t\right)  = {\left. {\nabla }_{F}F\right| }_{\gamma \left( t\right) } = 0,
\]

so \( \gamma \) is a geodesic.

Lemma 6.33. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( K \subseteq  M \) , and \( f : K \rightarrow  \mathbb{R} \) is a continuous function whose restriction to some open set \( W \subseteq  K \) is a smooth local distance function. For every admissible curve \( \sigma  : \left\lbrack  {{a}_{0},{b}_{0}}\right\rbrack   \rightarrow  K \) such that \( \sigma \left( \left( {{a}_{0},{b}_{0}}\right) \right)  \subseteq  W \) , we have

\[
{L}_{g}\left( \sigma \right)  \geq  \left| {f\left( {\sigma \left( {b}_{0}\right) }\right)  - f\left( {\sigma \left( {a}_{0}\right) }\right) }\right| .
\]

![bo_d7dtff491nqc73eq8m7g_188_528_187_476_372_0.jpg](images/bo_d7dtff491nqc73eq8m7g_188_528_187_476_372_0.jpg)

Fig. 6.18: Proving that \( f\left( x\right)  = {d}_{g}\left( {x, S}\right) \) in a neighborhood of \( S \)

Proof. This is proved exactly as in (6.8), noting that the only properties of \( r \) we used in that computation were that it is continuous on the image of \( \sigma \) and continuously differentiable on \( \sigma \left( \left( {{a}_{0},{b}_{0}}\right) \right) \) , and its gradient has unit length there.

The next theorem and its corollary explain why the name "local distance function" is justified. Its proof is an adaptation of the proof of Proposition 6.11.

Theorem 6.34. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( U \subseteq  M \) is an open subset, \( S \subseteq  U \) , and \( f : U \rightarrow  \lbrack 0,\infty ) \) is a continuous function such that \( {f}^{-1}\left( 0\right)  = S \) and \( f \) is a smooth local distance function on \( U \smallsetminus  S \) . Then there is a neighborhood \( {U}_{0} \subseteq  U \) of \( S \) in which \( f\left( x\right) \) is equal to the distance in \( M \) from \( x \) to \( S \) .

Proof. For each \( p \in  S \) , there are positive numbers \( {\varepsilon }_{p},{\delta }_{p} \) such that \( {B}_{{\varepsilon }_{p}}\left( p\right) \) is a uniformly \( {\delta }_{p} \) -normal geodesic ball and \( {B}_{2{\varepsilon }_{p}}\left( p\right)  \subseteq  U \) . This means that \( {B}_{{\varepsilon }_{p}}\left( p\right) \) is contained in the open geodesic ball of radius \( {\delta }_{p} \) around each of its points. In particular, \( {B}_{{\varepsilon }_{p}}\left( p\right)  \subseteq  {B}_{{\delta }_{p}}\left( p\right) \) , which means that \( {\delta }_{p} \geq  {\varepsilon }_{p} \) , and thus every geodesic starting at a point of \( {B}_{{\varepsilon }_{p}}\left( p\right) \) is defined at least for \( t \in  \left( {-{\varepsilon }_{p},{\varepsilon }_{p}}\right) \) . Let \( {U}_{0} \) be the union of all of the geodesic balls \( {B}_{{\varepsilon }_{p}}\left( p\right) \) for \( p \in  S \) , which is a neighborhood of \( S \) contained in \( U \) (Fig. 6.18).

Let \( x \in  {U}_{0} \) be arbitrary, and let \( c = f\left( x\right) \) . We will show that \( {d}_{g}\left( {x, S}\right)  = c \) . If \( x \in  S \) , then \( {d}_{g}\left( {x, S}\right)  = 0 = c \) , so we may as well assume \( x \notin  S \) .

There is some \( p \in  S \) such that \( x \in  {B}_{{\varepsilon }_{p}}\left( p\right) \) , which means that \( {d}_{g}\left( {x, S}\right)  < {\varepsilon }_{p} \) and geodesics starting at \( x \) are defined at least on \( \left( {-{\varepsilon }_{p},{\varepsilon }_{p}}\right) \) . Also, if \( \alpha  : \left\lbrack  {0, b}\right\rbrack   \rightarrow \; {B}_{\varepsilon }\left( p\right) \) is the radial geodesic segment from \( p \) to \( x \) , it follows from Lemma 6.33 that \( {L}_{g}\left( \alpha \right)  \geq  \left| {f\left( x\right)  - f\left( p\right) }\right|  = c \) , and we conclude that \( c \leq  {L}_{g}\left( \alpha \right)  < {\varepsilon }_{p} \) as well.

Let \( \gamma  : \left( {-{\varepsilon }_{p},{\varepsilon }_{p}}\right)  \rightarrow  U \) be the unit-speed geodesic starting at \( x \) with initial velocity equal to - grad \( {\left. f\right| }_{x} \) . By Theorem 6.32 and uniqueness of geodesics, \( \gamma \) coincides with an integral curve of - grad \( f \) as long as \( \gamma \left( t\right)  \in  U \smallsetminus  S \) , which is to say as long as \( f\left( {\gamma \left( t\right) }\right)  \neq  0 \) . For all such \( t \) we have

\[
\frac{d}{dt}f\left( {\gamma \left( t\right) }\right)  = \left\langle  {{\left. \operatorname{grad}f\right| }_{\gamma \left( t\right) },{\gamma }^{\prime }\left( t\right) }\right\rangle   =  - {\left| \operatorname{grad}f\right| }_{\gamma \left( t\right) }{\left. \right| }^{2} =  - 1,
\]

so \( f\left( {\gamma \left( t\right) }\right)  = c - t \) as long as \( t < c \) , and by continuity, \( f\left( {\gamma \left( c\right) }\right)  = 0 \) . This means that \( \gamma \left( c\right)  \in  S \) , and \( {\left. \gamma \right| }_{\left\lbrack  0, c\right\rbrack  } \) is a curve segment of length \( c \) connecting \( x \) with \( S \) , so \( {d}_{g}\left( {x, S}\right)  \leq  c. \)

To prove the reverse inequality, suppose \( \alpha  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any admissible curve starting at \( x \) and ending at a point of \( S \) . Assume first that \( \alpha \left( t\right)  \in  U \) for all \( t \in  \left\lbrack  {a, b}\right\rbrack \) , and let \( {b}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) be the first time that \( \alpha \left( {b}_{0}\right)  \in  S \) . Then Lemma 6.33 shows that \( {L}_{g}\left( \alpha \right)  \geq  {L}_{g}\left( {\left. \alpha \right| }_{\left\lbrack  a,{b}_{0}\right\rbrack  }\right)  \geq  \left| {f\left( {\alpha \left( {b}_{0}\right) }\right)  - f\left( {\alpha \left( a\right) }\right) }\right|  = c \) . On the other hand, suppose \( \alpha \left( t\right)  \in  M \smallsetminus  U \) for some \( t \) . The triangle inequality implies \( {B}_{{\varepsilon }_{p}}\left( x\right)  \subseteq  {B}_{2{\varepsilon }_{p}}\left( p\right)  \subseteq \; U \) , so there is a first time \( {b}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) such that \( {d}_{g}\left( {x,\alpha \left( {b}_{0}\right) }\right)  \geq  {\varepsilon }_{p} \) . Then \( {L}_{g}\left( \alpha \right)  \geq \; {L}_{g}\left( {\left. \alpha \right| }_{\left\lbrack  a,{b}_{0}\right\rbrack  }\right)  \geq  {\varepsilon }_{p} > c \) . Taken together, these two inequalities show that \( {L}_{g}\left( \alpha \right)  \geq  c \) for every such \( \alpha \) , which implies \( {d}_{g}\left( {x, S}\right)  \geq  c \) .

See Problem 6-27 for a global version of the preceding theorem.

Corollary 6.35. Let \( \left( {M, g}\right) \) be a Riemannian manifold, and let \( f \) be a smooth local distance function on an open subset \( U \subseteq  M \) . If \( c \) is a real number such that \( S = \; {f}^{-1}\left( c\right) \) is nonempty, then there is a neighborhood \( {U}_{0} \) of \( S \) in \( U \) on which \( \left| {f\left( x\right)  - c}\right| \) is equal to the distance in \( M \) from \( x \) to \( S \) .

- Exercise 6.36. Prove the preceding corollary.

## Distance Functions for Embedded Submanifolds

The most important local distance functions are those associated with embedded submanifolds. As we will see in this section, such distance functions are always smooth near the manifold.

Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold (without boundary) and \( P \subseteq  M \) is an embedded \( k \) -dimensional submanifold. Let \( {NP} \) denote the normal bundle of \( P \) in \( M \) , and let \( U \subseteq  M \) be a normal neighborhood of \( P \) in \( M \) , which is the diffeomorphic image of a certain open subset \( V \subseteq  {NP} \) under the normal exponential map. (Such a neighborhood always exists by Thm. 5.25.) We begin by constructing generalizations of the radial distance function and radial vector field (see (6.4) and (6.5)). Recall the definition of Fermi coordinates from Chapter 5 (see Prop. 5.26).

Proposition 6.37. Let \( P \) be an embedded submanifold of a Riemannian manifold \( \left( {M, g}\right) \) and let \( U \) be any normal neighborhood of \( P \) in \( M \) . There exist a unique continuous function \( r : U \rightarrow  \lbrack 0,\infty ) \) and smooth vector field \( {\partial }_{r} \) on \( U \smallsetminus  P \) that have the following coordinate representations in terms of any Fermi coordinates \( \left( {{x}^{1},\ldots ,{x}^{k},{v}^{1},\ldots ,{v}^{n - k}}\right) \) for \( P \) on a subset \( {U}_{0} \subseteq  U \) :

\[
r\left( {{x}^{1},\ldots ,{x}^{k},{v}^{1},\ldots ,{v}^{n - k}}\right)  = \sqrt{{\left( {v}^{1}\right) }^{2} + \cdots  + {\left( {v}^{n - k}\right) }^{2}}, \tag{6.17}
\]

\[
{\partial }_{r} = \frac{{v}^{1}}{r\left( {x, v}\right) }\frac{\partial }{\partial {v}^{1}} + \cdots  + \frac{{v}^{n - k}}{r\left( {x, v}\right) }\frac{\partial }{\partial {v}^{n - k}}. \tag{6.18}
\]

The function \( r \) is smooth on \( U \smallsetminus  P \) , and \( {r}^{2} \) is smooth on all of \( U \) .

Proof. The uniqueness, continuity, and smoothness claims follow immediately from the coordinate expressions (6.17) and (6.18), so we need only prove that \( r \) and \( {\partial }_{r} \) can be globally defined so as to have the indicated coordinate expressions in any Fermi coordinates.

Let \( V \subseteq  {NS} \) be the subset that is mapped diffeomorphically onto \( U \) by the normal exponential map \( E \) . Define a function \( \rho  : V \rightarrow  \lbrack 0,\infty ) \) by \( \rho \left( {p, v}\right)  = {\left| v\right| }_{g} \) , and define \( r : U \rightarrow  \lbrack 0,\infty ) \) by \( r = \rho  \circ  {E}^{-1} \) . Any Fermi coordinates for \( P \) are defined by choosing local coordinates \( \left( {{x}^{1},\ldots ,{x}^{k}}\right) \) for \( P \) and a local orthonormal frame \( \left( {E}_{\alpha }\right) \) for \( {NP} \) , and assigning the coordinates \( \left( {{x}^{1}\left( p\right) ,\ldots ,{x}^{k}\left( p\right) ,{v}^{1},\ldots ,{v}^{n - k}}\right) \) to the point \( E\left( {p,{\left. {v}^{\alpha }{E}_{\alpha }\right| }_{p}}\right) \) . (Here we are using the summation convention with Greek indices running from 1 to \( n - k \) .) Because the frame is orthonormal, for each \( \left( {p, v}\right)  = \left( {\left. p,{v}^{\alpha }{E}_{\alpha }\right| }_{p}\right)  \in  V \) we have \( r{\left( E\left( p, v\right) \right) }^{2} = \rho {\left( p, v\right) }^{2} = {\left( {v}^{1}\right) }^{2} + \cdots  + {\left( {v}^{n - k}\right) }^{2} \) , which shows that \( r \) has the coordinate representation (6.17).

To define \( {\partial }_{r} \) , let \( q \) be an arbitrary point in \( U \smallsetminus  P \) . Then \( q = {\exp }_{p}\left( v\right) \) for a unique \( \left( {p, v}\right)  \in  V \) , and the curve \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  U \) given by \( \gamma \left( t\right)  = {\exp }_{p}\left( {tv}\right) \) is a geodesic from \( p \) to \( q \) . Define

\[
{\left. {\partial }_{r}\right| }_{q} = \frac{1}{r\left( q\right) }{\gamma }^{\prime }\left( 1\right) \tag{6.19}
\]

which is independent of the choice of coordinates. Proposition 5.26 shows that in any Fermi coordinates, if we write \( v = {v}^{\alpha }{E}_{\alpha }{\left. \right| }_{p} \) , then \( \gamma \) has the coordinate formula \( \gamma \left( t\right)  = \left( {{x}^{1},\ldots ,{x}^{k}, t{v}^{1},\ldots , t{v}^{n - k}}\right) \) , and therefore \( {\gamma }^{\prime }\left( t\right)  = {v}^{\alpha }\partial /{\left. \partial {v}^{\alpha }\right| }_{\gamma \left( t\right) } \) . It follows that \( {\partial }_{r} \) has the coordinate formula (6.18).

By analogy with the special case in which \( P \) is a point, we call \( r \) the radial distance function for \( \mathbf{P} \) and \( {\partial }_{r} \) the radial vector field for \( \mathbf{P} \) .

Theorem 6.38 (Gauss Lemma for Submanifolds). Let \( P \) be an embedded sub-manifold of a Riemannian manifold \( \left( {M, g}\right) \) , let \( U \) be a normal neighborhood of \( P \) in \( M \) , and let \( r \) and \( {\partial }_{r} \) be defined as in Proposition 6.37. On \( U \smallsetminus  P,{\partial }_{r} \) is a unit vector field orthogonal to the level sets of \( r \) .

Proof. The proof is a dressed-up version of the proof of the ordinary Gauss lemma. Let \( q \in  U \smallsetminus  P \) be arbitrary, and let \( \left( {{x}^{1},\ldots ,{x}^{k},{v}^{1},\ldots ,{v}^{n - k}}\right) \) be the coordinate representation of \( q \) in some choice of Fermi coordinates associated with a local orthonormal frame \( \left( {E}_{\alpha }\right) \) for \( {NP} \) . As in the proof of Proposition \( {6.37}, q = \gamma \left( 1\right) \) , where \( \gamma \) is the geodesic \( {\exp }_{p}\left( {tv}\right) \) for some \( p \in  P \) and \( v = {\left. {v}^{\alpha }{E}_{\alpha }\right| }_{p} \in  {N}_{p}M \) . Since the frame \( \left( {E}_{\alpha }\right) \) is orthonormal, we have

\[
{\left| {\gamma }^{\prime }\left( 0\right) \right| }_{g} = {\left| v\right| }_{g} = \sqrt{{\left( {v}^{1}\right) }^{2} + \cdots  + {\left( {v}^{n - k}\right) }^{2}} = r\left( q\right) .
\]

Since geodesics have constant speed, it follows that \( {\left| {\gamma }^{\prime }\left( 1\right) \right| }_{g} = r\left( q\right) \) as well, and then (6.19) shows that \( {\left. {\partial }_{r}\right| }_{q} \) is a unit vector.

Next we show that \( {\partial }_{r} \) is orthogonal to the level sets of \( r \) . Suppose \( q \in  U \smallsetminus  P \) , and write \( q = {\exp }_{{p}_{0}}\left( {v}_{0}\right) \) for some \( {p}_{0} \in  P \) and \( {v}_{0} \in  {N}_{p}P \) with \( {v}_{0} \neq  0 \) . Let \( b = r\left( q\right)  = \; {\left| {v}_{0}\right| }_{g} \) , so \( q \) lies in the level set \( {r}^{-1}\left( b\right) \) . The coordinate representation (6.17) shows that this is a regular level set, and hence an embedded submanifold of \( U \) .

Let \( w \in  {T}_{q}M \) be an arbitrary vector tangent to this level set, and let \( \sigma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow \; U \) be a smooth curve lying in the same level set, with \( \sigma \left( 0\right)  = q \) and \( {\sigma }^{\prime }\left( 0\right)  = w \) . We can write \( \sigma \left( s\right)  = {\exp }_{x\left( s\right) }\left( {v\left( s\right) }\right) \) , where \( x\left( s\right)  \in  P \) and \( v\left( s\right)  \in  {N}_{x\left( s\right) }P \) with \( {\left| v\left( s\right) \right| }_{g} = \; b \) . The initial condition \( \sigma \left( 0\right)  = q \) translates to \( x\left( 0\right)  = {p}_{0} \) and \( v\left( 0\right)  = {v}_{0} \) . Define a smooth one-parameter family of curves \( \Gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0, b}\right\rbrack   \rightarrow  M \) by

\[
\Gamma \left( {s, t}\right)  = {\exp }_{x\left( s\right) }\left( {\frac{t}{b}{v}^{1}\left( s\right) ,\ldots ,\frac{t}{b}{v}^{n}\left( s\right) }\right) .
\]

Since \( {\left| v\left( s\right) \right| }_{g}/b \equiv  1 \) , each \( {\Gamma }_{s} \) is a unit-speed geodesic.

Write \( T\left( {s, t}\right)  = {\partial }_{t}\Gamma \left( {s, t}\right) \) and \( S\left( {s, t}\right)  = {\partial }_{s}\Gamma \left( {s, t}\right) \) as in the proof of Theorem 6.9. We have the following endpoint conditions:

\[
S\left( {0,0}\right)  = {\left. \frac{d}{ds}\right| }_{s = 0}x\left( s\right)  = {x}^{\prime }\left( 0\right)
\]

\[
T\left( {0,0}\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}{\exp }_{{p}_{0}}\left( {\frac{t}{b}{v}_{0}}\right)  = \frac{1}{b}{v}_{0}
\]

\[
S\left( {0, b}\right)  = {\left. \frac{d}{ds}\right| }_{s = 0}\sigma \left( s\right)  = w
\]

\[
T\left( {0, b}\right)  = {\left. \frac{d}{dt}\right| }_{t = b}{\exp }_{{p}_{0}}\left( {\frac{t}{b}{v}_{0}}\right)  = {\left. {\partial }_{r}\right| }_{q}.
\]

Then the same computation as in (6.7) shows that \( \left( {\partial /\partial t}\right) \langle S, T{\rangle }_{g} \equiv  0 \) , and therefore \( {\left\langle  w,{\partial }_{r}{|}_{q}\right\rangle  }_{g} = \langle S\left( {0, b}\right) , T\left( {0, b}\right) {\rangle }_{g} = \langle S\left( {0,0}\right) , T\left( {0,0}\right) {\rangle }_{g} = \left( {1/b}\right) {\left\langle  {x}^{\prime }\left( 0\right) ,{v}_{0}\right\rangle  }_{g} \) , which is zero because \( {x}^{\prime }\left( 0\right) \) is tangent to \( P \) and \( {v}_{0} \) is normal to it. This proves that \( {\partial }_{r} \) is orthogonal to the level sets of \( r \) .

Corollary 6.39. Assume the hypotheses of Theorem 6.38.

(a) \( {\partial }_{r} \) is equal to the gradient of \( r \) on \( U \smallsetminus  P \) .

(b) \( r \) is a local distance function.

(c) Each unit-speed geodesic \( \gamma  : \lbrack a, b) \rightarrow  U \) with \( {\gamma }^{\prime }\left( a\right) \) normal to \( P \) coincides with an integral curve of \( {\partial }_{r} \) on \( \left( {a, b}\right) \) .

(d) \( P \) has a tubular neighborhood in which the distance in \( M \) to \( P \) is equal to \( r \) .

Proof. By direct computation in Fermi coordinates using formulas (6.17) and (6.18), \( {\partial }_{r}\left( r\right)  \equiv  1 \) , which is equal to \( {\left| {\partial }_{r}\right| }_{g}^{2} \) by the previous theorem. Thus \( {\partial }_{r} = \operatorname{grad}r \) on \( U \smallsetminus  P \) by Problem 2-10. Because grad \( r \) is a unit vector field, \( r \) is a local distance function. By Proposition 5.26, the geodesics in \( U \) that start normal to \( P \) are represented in any Fermi coordinates by \( t \mapsto  \left( {{x}^{1},\ldots ,{x}^{k}, t{v}^{1},\ldots , t{v}^{n - k}}\right) \) , and such a geodesic has unit speed if and only if \( {\left( {v}^{1}\right) }^{2} + \cdots  + {\left( {v}^{n - k}\right) }^{2} = 1 \) . Another direct computation shows that each such curve is an integral curve of \( {\partial }_{r} \) wherever \( r \neq  0 \) .

Finally, to prove (d), note that Theorem 6.34 shows that there is some neighborhood \( {\widetilde{U}}_{0} \) of \( P \) in \( M \) on which \( r\left( x\right)  = {d}_{g}\left( {x, P}\right) \) ; if we take \( {U}_{0} \) to be a tubular neighborhood of \( P \) in \( {\widetilde{U}}_{0} \) , then \( {U}_{0} \) satisfies the conclusion.

---

When \( P \) is compact, we can say more.

---

Theorem 6.40. Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold, \( P \subseteq  M \) is a compact submanifold, and \( {U}_{\varepsilon } \) is an \( \varepsilon \) -tubular neighborhood of \( P \) . Then \( {U}_{\varepsilon } \) is also an \( \varepsilon \) -neighborhood in the metric space sense, and inside \( {U}_{\varepsilon } \) , the distance in \( M \) to \( P \) is equal to the function \( r \) defined in Proposition 6.37.

Proof. First we show that \( r \) can be extended continuously to \( {\bar{U}}_{\varepsilon } \) by setting \( r\left( q\right)  = \varepsilon \) for \( q \in  \partial {U}_{\varepsilon } \) . Indeed, suppose \( q \in  \partial {U}_{\varepsilon } \) and \( {q}_{i} \) is any sequence of points in \( {U}_{\varepsilon } \) converging to \( q \) . Then \( \mathop{\limsup }\limits_{i}r\left( {q}_{i}\right)  \leq  \varepsilon \) because \( r\left( {q}_{i}\right)  < \varepsilon \) for each \( i \) . Let \( c = \mathop{\liminf }\limits_{i}r\left( {q}_{i}\right) \) ; we will prove the result by showing that \( c = \varepsilon \) . Suppose for the sake of contradiction that \( c < \varepsilon \) . By passing to a subsequence, we may assume that \( r\left( {q}_{i}\right)  \rightarrow  c \) . We can write \( {q}_{i} = {\exp }_{{p}_{i}}\left( {v}_{i}\right) \) for \( {p}_{i} \in  P \) and \( {v}_{i} \in  {N}_{{p}_{i}}P \) , and because \( P \) is compact and \( \mathop{\lim }\limits_{i}{\left| {v}_{i}\right| }_{g} = \mathop{\lim }\limits_{i}r\left( {q}_{i}\right)  = c \) , we can pass to a further subsequence and assume that \( \left( {{p}_{i},{v}_{i}}\right)  \rightarrow  \left( {p, v}\right)  \in  {NP} \) with \( {\left| v\right| }_{g} = c < \varepsilon \) . Then we have \( q = \mathop{\lim }\limits_{i}{q}_{i} = \; \mathop{\lim }\limits_{i}{\exp }_{{p}_{i}}\left( {v}_{i}\right)  = {\exp }_{p}v \) , which lies in the open set \( {U}_{\varepsilon } \) , contradicting our assumption that \( q \in  \partial {U}_{\varepsilon } \) . Henceforth, we regard \( r \) as a continuous function on \( {\bar{U}}_{\varepsilon } \) .

Now to prove the theorem, let \( {W}_{\varepsilon } \) denote the \( \varepsilon \) -neighborhood of \( P \) in the metric space sense. Suppose first that \( q \in  M \smallsetminus  {U}_{\varepsilon } \) , and suppose \( \alpha  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any admissible curve from a point of \( P \) to \( q \) . There is a first time \( {b}_{0} \in  \left\lbrack  {a, b}\right\rbrack \) that \( \alpha \left( {b}_{0}\right)  \in \; \partial {U}_{\varepsilon } \) , and then Lemma 6.33 shows that

\[
{L}_{g}\left( \alpha \right)  \geq  {L}_{g}\left( {\left. \alpha \right| }_{\left\lbrack  a,{b}_{0}\right\rbrack  }\right)  \geq  \left| {r\left( {\alpha \left( {b}_{0}\right) }\right)  - r\left( {\alpha \left( a\right) }\right) }\right|  = \varepsilon .
\]

Thus \( q \notin  {U}_{\varepsilon } \Rightarrow  q \notin  {W}_{\varepsilon } \) , or equivalently \( {W}_{\varepsilon } \subseteq  {U}_{\varepsilon } \) .

Conversely, suppose \( q \in  {U}_{\varepsilon } \) . Then \( q \) is connected to \( P \) by a geodesic segment of length \( r\left( q\right) \) , so \( {d}_{g}\left( {q, P}\right)  \leq  r\left( q\right) \) . To prove the reverse inequality, suppose \( \alpha  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any admissible curve starting at a point of \( P \) and ending at \( q \) . If \( \alpha \left( t\right) \) remains in \( U \) for all \( t \in  \left\lbrack  {a, b}\right\rbrack \) , then Lemma 6.33 shows that

\[
{L}_{g}\left( \alpha \right)  \geq  {L}_{g}\left( {\left. \alpha \right| }_{\left\lbrack  {a}_{0}, b\right\rbrack  }\right)  \geq  \left| {r\left( {\gamma \left( b\right) }\right)  - r\left( {\gamma \left( {a}_{0}\right) }\right) }\right|  = r\left( q\right) ,
\]

where \( {a}_{0} \) is the last time that \( \alpha \left( {a}_{0}\right)  \in  P \) . On the other hand, if \( \alpha \left( t\right) \) does not remain in \( U \) , then there is a first time \( {b}_{0} \) such that \( \alpha \left( {b}_{0}\right)  \in  \partial {U}_{\varepsilon } \) , and the argument in the preceding paragraph shows that \( {L}_{g}\left( \alpha \right)  \geq  \varepsilon  > r\left( q\right) \) . Thus \( {d}_{g}\left( {q, P}\right)  = r\left( q\right) \) for all \( q \in  {U}_{\varepsilon } \) . Since \( r\left( q\right)  < \varepsilon \) for all such \( q \) , it follows also that \( {U}_{\varepsilon } \subseteq  {W}_{\varepsilon } \) .

## Semigeodesic Coordinates

Local distance functions can be used to build coordinate charts near submanifolds in which the metric has a particularly simple form. We begin by describing the kind of coordinates we are looking for.

Let \( \left( {M, g}\right) \) be an \( n \) -dimensional Riemannian manifold. Smooth local coordinates \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) on an open subset \( U \subseteq  M \) are called semigeodesic coordinates if each \( {x}^{n} \) -coordinate curve \( t \mapsto  \left( {{x}^{1},\ldots ,{x}^{n - 1}, t}\right) \) is a unit-speed geodesic that meets each level set of \( {x}^{n} \) orthogonally.

Because of the distinguished role played by the last coordinate function, throughout the rest of this section we will use the summation convention with Latin indices running from 1 to \( n \) and Greek indices running from 1 to \( n - 1 \) .

We will see below that semigeodesic coordinates are easy to construct. But first, let us develop some alternative characterizations of them.

Proposition 6.41 (Characterizations of Semigeodesic Coordinates). Let \( \left( {M, g}\right) \) be a Riemannian n-manifold, and let \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) be smooth coordinates on an open subset of \( M \) . The following are equivalent:

(a) \( \left( {x}^{i}\right) \) are semigeodesic coordinates.

(b) \( {\left| {\partial }_{n}\right| }_{g} \equiv  1 \) and \( {\left\langle  {\partial }_{\alpha },{\partial }_{n}\right\rangle  }_{g} \equiv  0 \) for \( \alpha  = 1,\ldots , n - 1 \) .

(c) \( {\left| d{x}^{n}\right| }_{g} \equiv  1 \) and \( {\left\langle  d{x}^{\alpha }, d{x}^{n}\right\rangle  }_{g} \equiv  0 \) for \( \alpha  = 1,\ldots , n - 1 \) .

(d) \( {\left| \operatorname{grad}{x}^{n}\right| }_{g} \equiv  1 \) and \( {\left\langle  \operatorname{grad}{x}^{\alpha },\operatorname{grad}{x}^{n}\right\rangle  }_{g} \equiv  0 \) for \( \alpha  = 1,\ldots , n - 1 \) .

(e) \( {x}^{n} \) is a local distance function and \( {x}^{1},\ldots ,{x}^{n - 1} \) are constant along the integral curves of grad \( {x}^{n} \) .

(f) grad \( {x}^{n} \equiv  {\partial }_{n} \) .

Proof. We begin by showing that (b) \( \Leftrightarrow \) (c) \( \Leftrightarrow \) (d) \( \Leftrightarrow \) (e) and (c) \( \Leftrightarrow \) (f). Note that (b) is equivalent to the coordinate matrix of \( g \) having the block form \( \left( \begin{array}{ll}  * & 0 \\  0 & 1 \end{array}\right) \) , where the asterisk represents an arbitrary \( \left( {n - 1}\right)  \times  \left( {n - 1}\right) \) positive definite symmetric matrix, while (c) is equivalent to the inverse matrix having the same form. It follows from Cramer’s rule that the matrix of \( g \) has this form if and only if its inverse does, and thus (b) is equivalent to (c).

The equivalence of (c) and (d) follows from the definitions of the gradient and of the inner product on 1-forms: for all \( i, j = 1,\ldots , n \) ,

\[
{\left\langle  d{x}^{i}, d{x}^{j}\right\rangle  }_{g} = {\left\langle  {\left( d{x}^{i}\right) }^{\# },{\left( d{x}^{j}\right) }^{\# }\right\rangle  }_{g} = {\left\langle  \operatorname{grad}{x}^{i},\operatorname{grad}{x}^{j}\right\rangle  }_{g}.
\]

The equivalence of (d) and (e) also follows from the definition of the gradient: \( {\left\langle  \operatorname{grad}{x}^{\alpha },\operatorname{grad}{x}^{n}\right\rangle  }_{g} = d{x}^{\alpha }\left( {\operatorname{grad}{x}^{n}}\right)  = \left( {\operatorname{grad}{x}^{n}}\right) \left( {x}^{\alpha }\right) \) for each \( \alpha \) , which means that \( {x}^{\alpha } \) is constant along the grad \( {x}^{n} \) integral curves if and only if \( {\left\langle  \operatorname{grad}{x}^{\alpha },\operatorname{grad}{x}^{n}\right\rangle  }_{g} = \) 0. Finally, by examining the individual components of the coordinate formula grad \( {x}^{n} = {g}^{nj}{\partial }_{j} \) , we see that (c) is also equivalent to (f).

To complete the proof, we show that (a) \( \Leftrightarrow \) (b). Assume first that (a) holds. Because the \( {x}^{n} \) -coordinate curves have unit speed, it follows that \( {\left| {\partial }_{n}\right| }_{g} \equiv  1 \) . The tangent space to any \( {x}^{n} \) -level set is spanned at each point by \( {\partial }_{1},\ldots ,{\partial }_{n - 1} \) , and (a) guarantees that \( {\partial }_{n} \) is orthogonal to each of these, showing that (b) holds. Conversely, if we assume (b), the first part of the proof shows that (f) holds as well, so \( {\left. {\left. \left| \operatorname{grad}{x}^{n}\right| \right| }_{g} \equiv  {\left| {\partial }_{n}\right| }_{g} \equiv  1\text{ , showing that }{x}^{n}\text{ is a local distance function. Thus the }\right| }_{n} \; {x}^{n} \) -coordinate curves are also integral curves of grad \( {x}^{n} \) and hence are unit-speed geodesics by Theorem 6.32. The fact that \( \left\langle  {{\partial }_{\alpha },{\partial }_{n}}\right\rangle   = 0 \) for \( \alpha  = 2,\ldots , n \) implies that these geodesics are orthogonal to the level sets of \( {x}^{n} \) , thus proving (a).

Part (b) of this proposition leads to the following simplified coordinate representations for the metric and Christoffel symbols in semigeodesic coordinates. Recall that implied summations with Greek indices run from 1 to \( n - 1 \) .

Corollary 6.42. Let \( \left( {x}^{i}\right) \) be semigeodesic coordinates on an open subset of a Riemannian n-manifold \( \left( {M, g}\right) \) .

(a) The metric has the following coordinate expression:

\[
g = {\left( d{x}^{n}\right) }^{2} + {g}_{\alpha \beta }\left( {{x}^{1},\ldots ,{x}^{n}}\right) d{x}^{\alpha }d{x}^{\beta }.
\]

(b) The Christoffel symbols of \( g \) have the following coordinate expressions:

\[
{\Gamma }_{nn}^{n} = {\Gamma }_{nn}^{\alpha } = {\Gamma }_{\alpha n}^{n} = {\Gamma }_{n\alpha }^{n} = 0,
\]

(6.20)

\[
{\Gamma }_{\alpha \beta }^{n} =  - \frac{1}{2}{\partial }_{n}{g}_{\alpha \beta }
\]

\[
{\Gamma }_{n\alpha }^{\beta } = {\Gamma }_{\alpha n}^{\beta } = \frac{1}{2}{g}^{\beta \gamma }{\partial }_{n}{g}_{\alpha \gamma },
\]

\[
{\Gamma }_{\alpha \beta }^{\gamma } = {\widehat{\Gamma }}_{\alpha \beta }^{\gamma }
\]

where for each fixed value of \( {x}^{n} \) , the quantities \( {\widehat{\Gamma }}_{\alpha \beta }^{\gamma } \) are the Christoffel symbols in \( \left( {x}^{\alpha }\right) \) coordinates for the induced metric \( \widehat{g} \) on the level set \( {x}^{n} = \) constant.

Proof. Part (a) follows immediately from part (b) of Proposition 6.41, and (b) is proved by inserting \( {g}_{nn} = 1 \) and \( {g}_{\alpha n} = {g}_{n\alpha } = 0 \) into formula (5.8) for the Christoffel symbols.

Proposition 6.41(e) gives us an effective way to construct semigeodesic coordinates: if \( r \) is any smooth local distance function (for example, the distance from a point or a smooth submanifold), just set \( {x}^{n} = r \) , choose any local coordinates \( {x}^{1},\ldots ,{x}^{n - 1} \) for a level set of \( r \) , and then extend them to be constant along the integral curves of grad \( r \) . Here are some explicit examples.

Example 6.43 (Fermi Coordinates for a Hypersurface). Suppose \( P \) is an embedded hypersurface in a Riemannian manifold \( \left( {M, g}\right) \) , and let \( \left( {{x}^{1},\ldots ,{x}^{n - 1}, v}\right) \) be any Fermi coordinates for \( P \) on an open subset \( U \subseteq  M \) (see (5.25)). In this case, the function \( r \) defined by (6.17) is just \( r\left( {{x}^{1},\ldots ,{x}^{n - 1}, v}\right)  = {\left( {v}^{2}\right) }^{1/2} = \left| v\right| \) , so \( v \) is a local distance function on \( U \smallsetminus  P \) . It follows from Corollary 6.39 that there is a neighborhood \( {U}_{0} \) of \( P \) on which \( \left| v\right| \) is equal to the distance from \( P \) . Moreover, (6.18) reduces to \( {\partial }_{r} =  \pm  \partial /{\partial }_{v} \) , which is equal to grad \( \left| v\right| \) by Corollary 6.39, so it follows from Proposition 6.41(f) that Fermi coordinates for a hypersurface are automatically semigeodesic coordinates.

Example 6.44 (Boundary Normal Coordinates). Suppose \( \left( {M, g}\right) \) is a smooth Riemannian manifold with nonempty boundary. The results in this chapter do not apply directly to manifolds with boundary, but we can embed \( M \) in its double \( \widetilde{M} \) (Prop. A.31), extend the metric smoothly to \( \widetilde{M} \) , and construct Fermi coordinates \( \left( {{x}^{1},\ldots ,{x}^{n - 1}, v}\right) \) for \( \partial M \) in \( \widetilde{M} \) . By replacing \( v \) with \( - v \) if necessary, we can arrange that \( v > 0 \) in Int \( M \) , and then these Fermi coordinates restrict to smooth boundary coordinates for \( M \) that are also semigeodesic coordinates. Such coordinates are called boundary normal coordinates for \( M \) .

![bo_d7dtff491nqc73eq8m7g_195_294_187_942_566_0.jpg](images/bo_d7dtff491nqc73eq8m7g_195_294_187_942_566_0.jpg)

Fig. 6.19: Polar normal coordinates

Example 6.45 (Polar Normal Coordinates). Polar coordinates for \( {\mathbb{R}}^{n} \) are constructed by choosing a smooth local parametrization \( \widehat{\psi } : \widehat{U} \rightarrow  U \subseteq  {\mathbb{S}}^{n - 1} \) for an open subset \( U \) of \( {\mathbb{S}}^{n - 1} \) , and defining \( \widehat{\Psi } : \widehat{U} \times  {\mathbb{R}}^{ + } \rightarrow  {\mathbb{R}}^{n} \) by \( \widehat{\Psi }\left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}, r}\right)  = \; r\widehat{\psi }\left( {{\theta }^{1},\ldots ,{\theta }^{n - 1}}\right) \) . It is straightforward to show that the differential of \( \widehat{\psi } \) vanishes nowhere, so \( \widehat{\Theta } = {\widehat{\Psi }}^{-1} \) is a smooth coordinate map on the open subset \( \mathcal{U} = \widehat{\Psi }\left( {\widehat{U} \times  {\mathbb{R}}^{ + }}\right)  \subseteq  {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) . Familiar examples are ordinary polar coordinates in the plane and spherical coordinates in \( {\mathbb{R}}^{3} \) . Such coordinates have the property that the last coordinate function is \( r\left( x\right)  = \left| x\right| \) .

Now let \( \left( {M, g}\right) \) be a Riemannian \( n \) -manifold, \( p \) a point in \( M \) , and \( \varphi \) any normal coordinate chart defined on a normal neighborhood \( V \) of \( p \) . For every choice of polar coordinates \( \left( {\mathcal{U},\widehat{\Theta }}\right) \) for \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) , we obtain a smooth coordinate map \( \Theta  = \widehat{\Theta } \circ  \varphi \) on an open subset of \( V \smallsetminus  \{ p\} \) (see Fig. 6.19). Such coordinates are called polar normal coordinates. They have the property that the last coordinate function \( r \) is the radial distance function on \( V \) , and the other coordinates are constant along the integral curves of grad \( r \) , so they are semigeodesic coordinates.

Example 6.46 (Polar Fermi Coordinates). Now let \( P \) be an embedded subman-ifold of \( \left( {M, g}\right) \) , and let \( \varphi  = \left( {{x}^{1},\ldots ,{x}^{k},{v}^{1},\ldots ,{v}^{n - k}}\right) \) be Fermi coordinates on a neighborhood \( {U}_{0} \) of a point \( p \in  P \) . Then any polar coordinate map \( \widehat{\Theta } \) for \( {\mathbb{R}}^{n - k} \) can be applied to the variables \( \left( {{v}^{1},\ldots ,{v}^{n - k}}\right) \) to yield a coordinate chart \( \Theta  = \; \left( {{\operatorname{Id}}_{{\mathbb{R}}^{k}} \times  \widehat{\Theta }}\right)  \circ  \varphi \) on an open subset of \( {U}_{0} \smallsetminus  P \) , taking values in \( {\mathbb{R}}^{k} \times  {\mathbb{R}}^{n - k - 1} \times  {\mathbb{R}}^{ + } \) . If we write the coordinate functions as \( \left( {{x}^{1},\ldots ,{x}^{k},{\theta }^{1},\ldots ,{\theta }^{n - k}, r}\right) \) , it follows from Proposition 5.26 that each coordinate curve \( t \mapsto  \left( {{x}^{1},\ldots ,{x}^{k},{\theta }^{1},\ldots ,{\theta }^{n - k}, t}\right) \) is a unit-speed geodesic. Thus these are semigeodesic coordinates, called polar Fermi coordinates. The polar normal coordinates described above are just the special case \( P = \{ p\} . \) ‖

## Problems

6-1. Suppose \( M \) is a nonempty connected Riemannian 1-manifold. Show that if \( M \) is noncompact, then it is isometric to an open interval in \( \mathbb{R} \) with the Euclidean metric, while if it is compact, it is isometric to a circle \( {\mathbb{S}}^{1}\left( R\right)  = \left\{  {x \in  {\mathbb{R}}^{2}}\right. \) : \( \left| x\right|  = R\} \) with its induced metric for some \( R > 0 \) , using the following steps.

(a) Let \( \gamma  : I \rightarrow  M \) be any maximal unit-speed geodesic. Show that its image is open and closed, and therefore \( \gamma \) is surjective.

(b) Show that if \( \gamma \) is injective, then it is an isometry between \( I \) with its Euclidean metric and \( M \) .

(c) Now suppose \( \gamma \left( {t}_{1}\right)  = \gamma \left( {t}_{2}\right) \) for some \( {t}_{1} \neq  {t}_{2} \) . In case \( {\gamma }^{\prime }\left( {t}_{1}\right)  = {\gamma }^{\prime }\left( {t}_{2}\right) \) , show that \( \gamma \) is periodic, and descends to a global isometry from an appropriate circle to \( M \) .

(d) It remains only to rule out the case \( \gamma \left( {t}_{1}\right)  = \gamma \left( {t}_{2}\right) \) and \( {\gamma }^{\prime }\left( {t}_{1}\right)  =  - {\gamma }^{\prime }\left( {t}_{2}\right) \) . If this occurs, let \( {t}_{0} = \left( {{t}_{1} + {t}_{2}}\right) /2 \) , and define geodesics \( \alpha \) and \( \beta \) by

\[
\alpha \left( t\right)  = \gamma \left( {{t}_{0} + t}\right) ,\;\beta \left( t\right)  = \gamma \left( {{t}_{0} - t}\right) .
\]

Use uniqueness of geodesics to conclude that \( \alpha  \equiv  \beta \) on their common domain, and show that this contradicts the fact that \( \gamma \) is injective on some neighborhood of \( {t}_{0} \) .

6-2. Let \( n \) be a positive integer and \( R \) a positive real number.

(a) Prove that the Riemannian distance between any two points \( p, q \) in \( {\mathbb{S}}^{n}\left( R\right) \) with the round metric is given by

\[
{d}_{{\overset{ \circ  }{g}}_{R}}\left( {p, q}\right)  = R\arccos \frac{\langle p, q\rangle }{{R}^{2}},
\]

where \( \langle  \cdot  , \cdot  \rangle \) is the Euclidean inner product on \( {\mathbb{R}}^{n + 1} \) .

(b) Prove that the metric space \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{d}_{{g}_{R}}^{ \circ  }}\right) \) has diameter \( {\pi R} \) .

(Used on pp. 39, 359.)

6-3. Let \( n \) be a positive integer and \( R \) a positive real number. Prove that the Riemannian distance between any two points in the Poincaré ball model \( \left( {{\mathbb{B}}^{n}\left( R\right) ,{\breve{g}}_{R}}\right) \) of hyperbolic space of radius \( R \) is given by

\[
{d}_{{\check{g}}_{R}}\left( {p, q}\right)  = R\operatorname{arccosh}\left( {1 + \frac{2{R}^{2}{\left| p - q\right| }^{2}}{\left( {{R}^{2} - {\left| p\right| }^{2}}\right) \left( {{R}^{2} - {\left| q\right| }^{2}}\right) }}\right) ,
\]

where \( \left| \cdot \right| \) represents the Euclidean norm in \( {\mathbb{R}}^{n} \) . [Hint: First use the result of Problem 3-5 to show that it suffices to consider the case \( R = 1 \) . Then use a rotation to reduce to the case \( n = 2 \) , and use the group action of Problem 3-8 to show that it suffices to consider the case in which \( p \) is the origin.]

6-4. In Chapter 2, we started with a Riemannian metric and used it to define the Riemannian distance function. This problem shows how to go back the other way: the distance function determines the Riemannian metric. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold.

(a) Show that if \( \gamma  : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  M \) is any smooth curve, then

\[
{\left| {\gamma }^{\prime }\left( 0\right) \right| }_{g} = \mathop{\lim }\limits_{{t \searrow  0}}\frac{{d}_{g}\left( {\gamma \left( 0\right) ,\gamma \left( t\right) }\right) }{t}.
\]

(b) Show that if \( g \) and \( \widetilde{g} \) are two Riemannian metrics on \( M \) such that \( {d}_{g}\left( {p, q}\right)  = {d}_{\widetilde{g}}\left( {p, q}\right) \) for all \( p, q \in  M \) , then \( g = \widetilde{g} \) .

6-5. Prove Theorem 6.17 (sufficiently small geodesic balls are geodesically convex) as follows.

(a) Let \( \left( {M, g}\right) \) be a Riemannian manifold, let \( p \in  M \) be fixed, and let \( W \) be a uniformly normal neighborhood of \( p \) . For \( \varepsilon  > 0 \) small enough that \( {B}_{3\varepsilon }\left( p\right)  \subseteq  W \) , define a subset \( {W}_{\varepsilon } \subseteq  {TM} \times  \mathbb{R} \) by

\[
{W}_{\varepsilon } = \left\{  {\left( {q, v, t}\right)  \in  {TM} \times  \mathbb{R} : q \in  {B}_{\varepsilon }\left( p\right) , v \in  {T}_{q}M,\left| v\right|  = 1,\left| t\right|  < {2\varepsilon }}\right\}  .
\]

Define \( f : {W}_{\varepsilon } \rightarrow  \mathbb{R} \) by

\[
f\left( {q, v, t}\right)  = {d}_{g}{\left( p,{\exp }_{q}\left( tv\right) \right) }^{2}.
\]

Show that \( f \) is smooth. [Hint: Use normal coordinates centered at \( p \) .]

(b) Show that if \( \varepsilon \) is chosen small enough, then \( {\partial }^{2}f/\partial {t}^{2} > 0 \) on \( {W}_{\varepsilon } \) . [Hint: Compute \( f\left( {p, v, t}\right) \) explicitly and use continuity. Be careful to verify that \( \varepsilon \) can be chosen independently of \( v \) .]

(c) Suppose \( \varepsilon \) is chosen as in (b). Show that if \( {q}_{1},{q}_{2} \in  {B}_{\varepsilon }\left( p\right) \) and \( \gamma \) is a minimizing geodesic segment from \( {q}_{1} \) to \( {q}_{2} \) , then \( {d}_{g}\left( {p,\gamma \left( t\right) }\right) \) attains its maximum at one of the endpoints of \( \gamma \) .

(d) Show that \( {B}_{\varepsilon }\left( p\right) \) is geodesically convex.

6-6. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold. For each \( x \in  M \) , define the convexity radius of \( M \) at \( x \) , denoted by conv \( \left( x\right) \) , to be the supremum of all \( \varepsilon  > 0 \) such that there is a geodesically convex geodesic ball of radius \( \varepsilon \) centered at \( x \) . Show that \( \operatorname{conv}\left( x\right) \) is a continuous function of \( x \) .

6-7. We now have two kinds of "metrics" on a connected Riemannian manifold: the Riemannian metric and the distance function. Correspondingly, there are two definitions of "isometry" between connected Riemannian manifolds: a Riemannian isometry is a diffeomorphism that pulls one Riemannian metric back to the other, and a metric isometry is a homeomorphism that preserves distances. Proposition 2.51 shows that every Riemannian isometry is a metric isometry. This problem outlines a proof of the converse. Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are connected Riemannian manifolds, and \( \varphi  : M \rightarrow  \widetilde{M} \) is a metric isometry.

(a) Show that for every \( p \in  M \) and \( v, w \in  {T}_{p}M \) , we have

\[
\mathop{\lim }\limits_{{t \rightarrow  0}}\frac{{d}_{g}\left( {{\exp }_{p}{tv},{\exp }_{p}{tw}}\right) }{t} = {\left| v - w\right| }_{g}.
\]

[Hint: Use the Taylor series for \( g \) in Riemannian normal coordinates on a convex geodesic ball centered at \( p \) .]

(b) Show that \( \varphi \) takes geodesics to geodesics.

(c) For each \( p \in  M \) , show that there exist an open ball \( {B}_{\varepsilon }\left( 0\right)  \subseteq  {T}_{p}M \) and a continuous map \( \psi  : {B}_{\varepsilon }\left( 0\right)  \rightarrow  {T}_{\varphi \left( p\right) }\widetilde{M} \) satisfying \( \psi \left( 0\right)  = 0 \) and \( {\exp }_{\varphi \left( p\right) }\psi \left( v\right)  = \varphi \left( {{\exp }_{p}v}\right) \) for all \( v \in  {B}_{\varepsilon }\left( 0\right) . \)

(d) With \( \psi \) as above, show that \( {\left| \psi \left( v\right)  - \psi \left( w\right) \right| }_{\widetilde{g}} = {\left| v - w\right| }_{g} \) for all \( v, w \in \; {B}_{\varepsilon }\left( 0\right) \) , and conclude from Problem 2-2 that \( \psi \) is the restriction of a linear isometry.

(e) With \( p \) and \( \psi \) as above, show that \( \varphi \) is smooth on a neighborhood of \( p \) and \( d{\varphi }_{p} = \psi \) .

(f) Conclude that \( \varphi \) is a Riemannian isometry.

6-8. Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are connected Riemannian manifolds (not necessarily complete), and for each \( i \in  {\mathbb{Z}}^{ + },{\varphi }_{i} : M \rightarrow  \widetilde{M} \) is a Riemannian isometry such that \( {\varphi }_{i} \) converges pointwise to a map \( \varphi  : M \rightarrow  \widetilde{M} \) . Show that \( \varphi \) is a Riemannian isometry. [Hint: Once you have shown that \( \varphi \) is a local isometry, to show that \( \varphi \) is surjective, suppose \( y \) is a limit point of \( \varphi \left( M\right) \) . Choose \( x \in  M \) such that \( \varphi \left( x\right) \) lies in a uniformly normal neighborhood of \( y \) , and show that there exists a convergent sequence of points \( \left( {{x}_{i},{v}_{i}}\right)  \in  {TM} \) such that \( {\varphi }_{i}\left( {x}_{i}\right)  = \varphi \left( x\right) \) and \( {\varphi }_{i}\left( {{\exp }_{{x}_{i}}{v}_{i}}\right)  = y \) .]

6-9. Suppose \( \left( {M, g}\right) \) is a (not necessarily connected) Riemannian manifold. In Problem 2-30, you were asked to show that there is a distance function \( d : M \times  M \rightarrow  \mathbb{R} \) that induces the given topology and restricts to the Riemannian distance on each connected component of \( M \) . Show that if each component of \( M \) is geodesically complete, then \( d \) can be chosen so that \( \left( {M, d}\right) \) is a complete metric space. Show also that if \( M \) has infinitely many components, then \( d \) can be chosen so that \( \left( {M, d}\right) \) is not complete.

6-10. A curve \( \gamma  : \lbrack 0, b) \rightarrow  M \) (with \( 0 < b \leq  \infty \) ) is said to diverge to infinity if for every compact set \( K \subseteq  M \) , there is a time \( T \in  \lbrack 0, b) \) such that \( \gamma \left( t\right)  \notin  K \) for \( t > T \) . (For those who are familiar with one-point compactifications, this means that \( \gamma \left( t\right) \) converges to the "point at infinity" in the one-point compactification of \( M \) as \( t \nearrow  b \) .) Prove that a connected Riemannian manifold is complete if and only if every regular curve that diverges to infinity has infinite length. (The length of a curve whose domain is not compact is just the supremum of the lengths of its restrictions to compact subintervals.)

6-11. Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold, \( P \subseteq  M \) is a connected embedded submanifold, and \( \widehat{g} \) is the induced Riemannian metric on \( P \) .

(a) Show that \( {d}_{\widehat{g}}\left( {p, q}\right)  \geq  {d}_{g}\left( {p, q}\right) \) for \( p, q \in  P \) .

(b) Prove that if \( \left( {M, g}\right) \) is complete and \( P \) is closed in \( M \) , then \( \left( {P,\widehat{g}}\right) \) is complete.

(c) Give an example of a complete Riemannian manifold \( \left( {M, g}\right) \) and a connected embedded submanifold \( P \subseteq  M \) that is complete but not closed in \( M \) .

6-12. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold.

(a) Suppose there exists \( \delta  > 0 \) such that for each \( p \in  M \) , every maximal unit-speed geodesic starting at \( p \) is defined at least on an interval of the form \( \left( {-\delta ,\delta }\right) \) . Prove that \( M \) is complete.

(b) Prove that if \( M \) has positive or infinite injectivity radius, then it is complete.

(c) Prove that if \( M \) is homogeneous, then it is complete.

(d) Give an example of a complete, connected Riemannian manifold that has zero injectivity radius.

6-13. Let \( G \) be a connected compact Lie group. Show that the Lie group exponential map of \( G \) is surjective. [Hint: Use Problem 5-8.]

6-14. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold.

(a) Show that \( M \) is complete if and only if the compact subsets of \( M \) are exactly the closed and bounded ones.

(b) Show that \( M \) is compact if and only if it is complete and bounded.

6-15. Let \( S \) be the unit 2-sphere minus its north and south poles, and let \( M = \; \left( {0,\pi }\right)  \times  \mathbb{R} \) . Define \( q : M \rightarrow  S \) by \( q\left( {\varphi ,\theta }\right)  = \left( {\sin \varphi \cos \theta ,\sin \varphi \sin \theta ,\cos \varphi }\right) \) , and let \( g \) be the metric on \( M \) given by pulling back the round metric: \( g = \; {q}^{ * }\overset{ \circ  }{g} \) . (Think of \( M \) as an infinitely long onion skin wrapping infinitely many times around an onion.) Prove that the Riemannian manifold \( \left( {M, g}\right) \) has diameter \( \pi \) , but contains infinitely long properly embedded geodesics.

6-16. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold with positive or infinite injectivity radius.

(a) Let \( \rho  \in  (0,\infty \rbrack \) denote the injectivity radius of \( M \) , and define \( {T}^{\rho }M \) to be the subset of \( {TM} \) consisting of vectors of length less than \( \rho \) , and \( {D}^{\rho } \) to be the subset \( \left\{  {\left( {p, q}\right)  : {d}_{g}\left( {p, q}\right)  < \rho }\right\}   \subseteq  M \times  M \) . Define \( E : {T}^{\rho }M \rightarrow  {D}^{\rho } \) by \( E\left( {x, v}\right)  = \left( {x,{\exp }_{x}v}\right) \) . Prove that \( E \) is a diffeomorphism.

(b) Use part (a) to prove that if \( B \) is a topological space and \( F, G : B \rightarrow  M \) are continuous maps such that \( {d}_{g}\left( {F\left( x\right) , G\left( x\right) }\right)  < \operatorname{inj}\left( M\right) \) for all \( x \in  B \) , then \( F \) and \( G \) are homotopic.

6-17. Prove Proposition 6.28 (existence of a closed geodesic in a free homotopy class). [Hint: Use Prop. 6.25 to show that the given free homotopy class is represented by a geodesic loop, i.e., a geodesic whose starting and ending points are the same. Show that the lengths of such loops have a positive greatest lower bound; then choose a sequence of geodesic loops whose lengths approach that lower bound, and show that a subsequence converges uniformly to a geodesic loop whose length is equal to the lower bound. Use Problem 6-16 to show that the limiting curve is in the given free homotopy class, and apply the first variation formula to show that the limiting curve is in fact a closed geodesic.]

6-18. A connected Riemannian manifold \( \left( {M, g}\right) \) is said to be \( \mathbf{k} \) -point homogeneous if for any two ordered \( k \) -tuples \( \left( {{p}_{1},\ldots ,{p}_{k}}\right) \) and \( \left( {{q}_{1},\ldots ,{q}_{k}}\right) \) of points in \( M \) such that \( {d}_{g}\left( {{p}_{i},{p}_{j}}\right)  = {d}_{g}\left( {{q}_{i},{q}_{j}}\right) \) for all \( i, j \) , there is an isometry \( \varphi  : M \rightarrow  M \) such that \( \varphi \left( {p}_{i}\right)  = {q}_{i} \) for \( i = 1,\ldots , k \) . Show that \( \left( {M, g}\right) \) is 2-point homogeneous if and only if it is isotropic. [Hint: Assuming that \( M \) is isotropic, first show that it is homogeneous by considering the midpoint of a geodesic segment joining sufficiently nearby points \( p, q \in  M \) , and then use the result of Problem 6-12(c) to show that it is complete.] (Used on pp. 56, 261.)

6-19. Prove that every Riemannian symmetric space is homogeneous. [Hint: Proceed as in Problem 6-18.] (Used on p. 78.)

6-20. A connected Riemannian manifold is said to be extendible if it is isometric to a proper open subset of a larger connected Riemannian manifold.

(a) Show that every complete, connected Riemannian manifold is nonextendible.

(b) Show that the converse is false by giving an example of a nonextendible connected Riemannian manifold that is not complete.

6-21. Let \( \left( {M, g}\right) \) be a complete, connected, noncompact Riemannian manifold. Define a ray in \( M \) to be a geodesic \( \gamma \) whose domain is \( \lbrack 0,\infty ) \) , and such that the restriction of \( \gamma \) to \( \left\lbrack  {0, b}\right\rbrack \) is minimizing for every \( b > 0 \) . Prove that for each \( p \in  M \) there is a ray in \( M \) starting at \( p \) .

6-22. Let \( \left( {M, g}\right) \) be a connected Riemannian manifold with boundary. Prove that \( \left( {M,{d}_{g}}\right) \) is a complete metric space if and only if the following condition holds: for every geodesic \( \gamma  : \lbrack 0, b) \rightarrow  M \) that cannot be extended to a geodesic on any interval \( \left\lbrack  {0,{b}^{\prime }}\right) \) with \( {b}^{\prime } > b,\gamma \left( t\right) \) converges to a point of \( \partial M \) as \( t \nearrow  b \) .

6-23. In some treatments of Riemannian geometry, instead of minimizing the length functional, one considers the following energy functional for an admissible curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) :

\[
E\left( \gamma \right)  = \frac{1}{2}{\int }_{a}^{b}{\left| {\gamma }^{\prime }\left( t\right) \right| }^{2}{dt}
\]

(Note that \( E\left( \gamma \right) \) is not independent of parametrization.)

(a) Prove that an admissible curve is a critical point for \( E \) (with respect to proper variations) if and only if it is a geodesic (which means, in particular, that it has constant speed).

(b) Prove that if \( \gamma \) is an admissible curve that minimizes energy among admissible curves with the same endpoints, then it also minimizes length.

(c) Prove that if \( \gamma \) is an admissible curve that minimizes length among admissible curves with the same endpoints, then it minimizes energy if and only if it has constant speed.

[Remark: For our limited purposes, it is easier and more straightforward to use the length functional. But because the energy functional does not involve the square root function, and its critical points automatically have constant-speed parametrizations, it is sometimes more useful for proving the existence of geodesics with certain properties.]

6-24. Let \( \left( {M, g}\right) \) be a Riemannian manifold. Recall that a vector field \( X \in  \mathfrak{X}\left( M\right) \) is called a Killing vector field if \( {\mathcal{L}}_{X}g = 0 \) (see Problem 5-22).

(a) Prove that a Killing vector field that is normal to a geodesic at one point is normal everywhere along the geodesic.

(b) Prove that if a Killing vector field vanishes at a point \( p \) , then it is tangent to geodesic spheres centered at \( p \) .

(c) Prove that a Killing vector field on an odd-dimensional manifold cannot have an isolated zero.

(Used on p. 315.)

6-25. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold and \( f : M \rightarrow  \mathbb{R} \) is a smooth local distance function. Prove that \( f \) is a Riemannian submersion.

6-26. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold and \( S \subseteq  M \) is a closed subset.

(a) Show that for every \( p \in  M \smallsetminus  S \) , there is a geodesic segment from \( p \) to a point of \( S \) whose length is equal to \( {d}_{g}\left( {p, S}\right) \) .

(b) In case \( S \) is a properly embedded submanifold of \( M \) , show that every geodesic segment satisfying the conclusion of (a) intersects \( S \) orthogonally.

(c) Give a counterexample to (a) if \( S \) is not closed.

6-27. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold, \( S \subseteq  M \) is a closed subset, and \( f : M \rightarrow  \mathbb{R} \) is a continuous function such that \( {f}^{-1}\left( 0\right)  = \; S \) and \( f \) is smooth with unit gradient on \( M \smallsetminus  S \) . Prove that \( f\left( x\right)  = {d}_{g}\left( {x, S}\right) \) for all \( x \in  M \) .

6-28. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian \( n \) -manifold whose isometry group is a Lie group acting smoothly on \( M \) . (The Myers-Steenrod theorem shows that this is always the case when \( M \) is connected, but we have not proved this.) Prove that if \( G \) is a closed subgroup of \( \operatorname{Iso}\left( M\right) \) , then \( G \) acts properly on \( M \) , using the following outline. Suppose \( \left( {\varphi }_{m}\right) \) is a sequence in \( G \) and \( \left( {p}_{m}\right) \) is a sequence in \( M \) such that \( {p}_{m} \rightarrow  {p}_{0} \) and \( {\varphi }_{m}\left( {p}_{m}\right)  \rightarrow  {q}_{0} \) .

(a) Prove that \( {\varphi }_{m}\left( {p}_{0}\right)  \rightarrow  {q}_{0} \) .

(b) Let \( {B}_{r}\left( {p}_{0}\right) \) be a geodesic ball centered at \( {p}_{0} \) ; let \( 0 < \varepsilon  < r \) ; let \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) be an orthonormal basis for \( {T}_{{p}_{0}}M \) ; and let \( {p}_{i} = {\exp }_{{p}_{0}}\left( {\varepsilon {b}_{i}}\right) \) for \( i = 1,\ldots , n \) . Prove that there exist a linear isometry \( A : {T}_{{p}_{0}}M \rightarrow \; {T}_{{q}_{0}}M \) and a subsequence \( \left( {\varphi }_{{m}_{j}}\right) \) such that \( {\varphi }_{{m}_{j}}\left( {p}_{i}\right)  \rightarrow  {\exp }_{{q}_{0}}\left( {{\varepsilon A}{b}_{i}}\right) \) for \( i = 1,\ldots , n \) . [Hint: Use Prop. 5.20.]

(c) Prove that there is an isometry \( \varphi  \in  G \) such that \( {\varphi }_{{m}_{j}} \rightarrow  \varphi \) pointwise, meaning that \( {\varphi }_{{m}_{j}}\left( x\right)  \rightarrow  \varphi \left( x\right) \) for every \( x \in  M \) .

(d) Prove that \( {\varphi }_{{m}_{j}} \rightarrow  \varphi \) in the topology of \( G \) . [Hint: Define a map \( F : G \rightarrow \; {M}^{n + 1} \) by \( F\left( \psi \right)  = \left( {\psi \left( {p}_{0}\right) ,\psi \left( {p}_{1}\right) ,\ldots ,\psi \left( {p}_{n}\right) }\right) \) , where \( {p}_{1},\ldots ,{p}_{n} \) are the points introduced in part (b). Show that \( F \) is continuous, injective, and closed, and therefore is a homeomorphism onto its image.]

(Used on p. 349.)

6-29. Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold that admits a nonzero parallel vector field \( X \) . Show that for each \( p \in  M \) , there exist a neighborhood \( U \) of \( p \) , a Riemannian \( \left( {n - 1}\right) \) -manifold \( N \) , and an open interval \( I \subseteq  \mathbb{R} \) with its Euclidean metric such that \( U \) is isometric to the Riemannian product \( N \times  I \) . [Hint: It might be helpful to prove that the 1-form \( {X}^{\flat } \) is closed and to compute the Lie derivative \( {\mathcal{L}}_{X}g \) .]

6-30. Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold, \( p \in  M \) , and \( {B}_{\varepsilon }\left( p\right) \) is a geodesic ball centered at \( p \) . Prove that for every \( \delta \) such that \( 0 < \delta  < \varepsilon \) ,

\[
\operatorname{Vol}\left( {{\bar{B}}_{\delta }\left( p\right) }\right)  = {\int }_{0}^{\delta }\operatorname{Area}\left( {\partial {B}_{r}\left( p\right) }\right) {dr}
\]

where \( \operatorname{Area}\left( {\partial {B}_{r}\left( p\right) }\right) \) represents the \( \left( {n - 1}\right) \) -dimensional volume of \( \partial {B}_{r}\left( p\right) \) with its induced Riemannian metric.

6-31. Suppose \( \left( {M, g}\right) \) is a Riemannian \( n \) -manifold, \( P \subseteq  M \) is a compact embedded submanifold, and \( U \) is an \( \varepsilon \) -tubular neighborhood of \( P \) for some \( \varepsilon  > 0 \) . For \( 0 < \delta  < \varepsilon \) , define \( {U}_{\delta } \) and \( {P}_{\delta } \) by

\[
{U}_{\delta } = \left\{  {x \in  U : {d}_{g}\left( {x, P}\right)  \leq  \delta }\right\}
\]

\[
{P}_{\delta } = \left\{  {x \in  U : {d}_{g}\left( {x, P}\right)  = \delta }\right\}  .
\]

(a) Prove that \( {U}_{\delta } \) is a regular domain and \( {P}_{\delta } \) is a compact, embedded sub-manifold of \( M \) for each \( \delta  \in  \left( {0,\varepsilon }\right) \) .

(b) Generalize the result of Problem 6-30 by proving that

\[
\operatorname{Vol}\left( {U}_{\delta }\right)  = {\int }_{0}^{\delta }\operatorname{Area}\left( {P}_{r}\right) {dr}
\]

where \( \operatorname{Area}\left( {P}_{r}\right) \) denotes the \( \left( {n - 1}\right) \) -dimensional volume of \( {P}_{r} \) with the induced Riemannian metric.
