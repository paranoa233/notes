## Chapter 9 The Gauss-Bonnet Theorem

All the work we have done so far has been focused on purely local properties of Riemannian manifolds and their submanifolds. We are finally in a position to prove our first major local-to-global theorem in Riemannian geometry: the Gauss-Bonnet theorem. The grandfather of all such theorems in Riemannian geometry, it is a local-to-global theorem par excellence, because it asserts the equality of two very differently defined quantities on a compact Riemannian 2-manifold: the integral of the Gaussian curvature, which is determined by the local geometry, and \( {2\pi } \) times the Euler characteristic, which is a global topological invariant. Although in this form it applies only in two dimensions, it has provided a model and an inspiration for innumerable local-to-global results in higher-dimensional geometry, some of which we will prove in Chapter 12.

This chapter begins with some not-so-elementary notions from plane geometry, leading up to a proof of Hopf's rotation index theorem, which expresses the intuitive idea that the velocity vector of a simple closed plane curve, or more generally of a "curved polygon," makes a net rotation through an angle of exactly \( {2\pi } \) as one traverses the curve counterclockwise. Then we investigate curved polygons on Riemannian 2-manifolds, leading to a far-reaching generalization of the rotation index theorem called the Gauss-Bonnet formula, which relates the exterior angles, geodesic curvature of the boundary, and Gaussian curvature in the interior of a curved polygon. Finally, we use the Gauss-Bonnet formula to prove the global statement of the Gauss-Bonnet theorem.

## Some Plane Geometry

Look back for a moment at the three local-to-global theorems about plane geometry stated in Chapter 1: the angle-sum theorem, the circumference theorem, and the total curvature theorem. When looked at correctly, these three theorems all turn out to be manifestations of the same phenomenon: as one traverses a simple closed plane curve, the velocity vector makes a net rotation through an angle of exactly \( {2\pi } \) . Our task in the first part of this chapter is to make these notions precise.

![bo_d7dtff491nqc73eq8m7g_274_399_192_734_319_0.jpg](images/bo_d7dtff491nqc73eq8m7g_274_399_192_734_319_0.jpg)

Fig. 9.1: A closed curve with \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \)

Throughout this section, \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) is an admissible curve in the plane. We say that \( \gamma \) is a simple closed curve if \( \gamma \left( a\right)  = \gamma \left( b\right) \) but \( \gamma \) is injective on \( \lbrack a, b) \) . We do not assume that \( \gamma \) has unit speed; instead, we define the unit tangent vector field of \( \gamma \) as the vector field \( T \) along each smooth segment of \( \gamma \) given by

\[
T\left( t\right)  = \frac{{\gamma }^{\prime }\left( t\right) }{\left| {\gamma }^{\prime }\left( t\right) \right| }
\]

Since each tangent space to \( {\mathbb{R}}^{2} \) is naturally identified with \( {\mathbb{R}}^{2} \) itself, we can think of \( T \) as a map into \( {\mathbb{R}}^{2} \) , and since \( T \) has unit length, it takes its values in \( {\mathbb{S}}^{1} \) .

If \( \gamma \) is smooth (or at least continuously differentiable), we define a tangent angle function for \( \gamma \) to be a continuous function \( \theta  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) such that \( T\left( t\right)  = \; \left( {\cos \theta \left( t\right) ,\sin \theta \left( t\right) }\right) \) for all \( t \in  \left\lbrack  {a, b}\right\rbrack \) . It follows from the theory of covering spaces that such a function exists: the map \( q : \mathbb{R} \rightarrow  {\mathbb{S}}^{1} \) given by \( q\left( s\right)  = \left( {\cos s,\sin s}\right) \) is a smooth covering map, and the path-lifting property of covering maps (Prop. A.54(b)) ensures that there is a continuous function \( \theta  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) that satisfies \( q\left( {\theta \left( t\right) }\right)  = T\left( t\right) \) . By the unique lifting property (Prop. A.54(a)), a lift is uniquely determined once its value at any single point is determined, and thus any two lifts differ by a constant integral multiple of \( {2\pi } \) .

If \( \gamma \) is a continuously differentiable simple closed curve such that \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \) (Fig. 9.1), then \( \left( {\cos \theta \left( a\right) ,\sin \theta \left( a\right) }\right)  = \left( {\cos \theta \left( b\right) ,\sin \theta \left( b\right) }\right) \) , so \( \theta \left( b\right)  - \theta \left( a\right) \) must be an integral multiple of \( {2\pi } \) . For such a curve, we define the rotation index of \( \gamma \) to be the following integer:

\[
\rho \left( \gamma \right)  = \frac{1}{2\pi }\left( {\theta \left( b\right)  - \theta \left( a\right) }\right) ,
\]

where \( \theta \) is any tangent angle function for \( \gamma \) . For any other choice of tangent angle function, \( \theta \left( a\right) \) and \( \theta \left( b\right) \) would change by addition of the same constant, so the rotation index is independent of the choice of \( \theta \) .

We would also like to extend the definition of the rotation index to certain piecewise regular closed curves. For this purpose, we have to take into account the "jumps" in the tangent angle function at corners. To do so, suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) is an admissible simple closed curve, and let \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) be an admissible partition of \( \left\lbrack  {a, b}\right\rbrack \) . The points \( \gamma \left( {a}_{i}\right) \) are called the vertices of \( \gamma \) , and the curve segments \( {\left. \gamma \right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  } \) are called its edges or sides.

![bo_d7dtff491nqc73eq8m7g_275_263_188_420_350_0.jpg](images/bo_d7dtff491nqc73eq8m7g_275_263_188_420_350_0.jpg)

Fig. 9.2: An exterior angle

![bo_d7dtff491nqc73eq8m7g_275_839_203_418_335_0.jpg](images/bo_d7dtff491nqc73eq8m7g_275_839_203_418_335_0.jpg)

Fig. 9.3: A cusp vertex

At each vertex \( \gamma \left( {a}_{i}\right) \) , recall that \( \gamma \) has left-hand and right-hand velocity vectors denoted by \( {\gamma }^{\prime }\left( {a}_{i}^{ - }\right) \) and \( {\gamma }^{\prime }\left( {a}_{i}^{ + }\right) \) , respectively; let \( T\left( {a}_{i}^{ - }\right) \) and \( T\left( {a}_{i}^{ + }\right) \) denote the corresponding unit vectors. We classify each vertex into one of three categories:

- If \( T\left( {a}_{i}^{ - }\right)  \neq   \pm  T\left( {a}_{i}^{ + }\right) \) , then \( \gamma \left( {a}_{i}\right) \) is an ordinary vertex.

- If \( T\left( {a}_{i}^{ - }\right)  = T\left( {a}_{i}^{ + }\right) \) , then \( \gamma \left( {a}_{i}\right) \) is a flat vertex.

- If \( T\left( {a}_{i}^{ - }\right)  =  - T\left( {a}_{i}^{ + }\right) \) , then \( \gamma \left( {a}_{i}\right) \) is a cusp vertex.

At each ordinary vertex, define the exterior angle at \( \gamma \left( {a}_{i}\right) \) to be the oriented measure \( {\varepsilon }_{i} \) of the angle from \( T\left( {a}_{i}^{ - }\right) \) to \( T\left( {a}_{i}^{ + }\right) \) , chosen to be in the interval \( \left( {-\pi ,\pi }\right) \) , with a positive sign if \( \left( {T\left( {a}_{i}^{ - }\right) , T\left( {a}_{i}^{ + }\right) }\right) \) is an oriented basis for \( {\mathbb{R}}^{2} \) , and a negative sign otherwise (Fig. 9.2). At a flat vertex, the exterior angle is defined to be zero. At a cusp vertex, there is no simple way to choose unambiguously between \( \pi \) and \( - \pi \) (Fig. 9.3), so we leave the exterior angle undefined. The vertex \( \gamma \left( a\right)  = \gamma \left( b\right) \) is handled in the same way, with \( T\left( b\right) \) and \( T\left( a\right) \) playing the roles of \( T\left( {a}_{i}^{ - }\right) \) and \( T\left( {a}_{i}^{ + }\right) \) , respectively. If \( \gamma \left( {a}_{i}\right) \) is an ordinary or a flat vertex, the interior angle at \( \gamma \left( {a}_{i}\right) \) is defined to be \( {\theta }_{i} = \pi  - {\varepsilon }_{i} \) ; our conventions ensure that \( 0 < {\theta }_{i} < {2\pi } \) .

The curves we wish to consider are of the following type: a curved polygon in the plane is an admissible simple closed curve without cusp vertices, whose image is the boundary of a precompact open set \( \Omega  \subseteq  {\mathbb{R}}^{2} \) . The set \( \Omega \) is called the interior of \( \gamma \) (not to be confused with the topological interior of its image as a subset of \( {\mathbb{R}}^{2} \) , which is the empty set).

Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) is a curved polygon. If \( \gamma \) is parametrized so that at smooth points, \( {\gamma }^{\prime } \) is positively oriented with respect to the induced orientation on \( \partial \Omega \) in the sense of Stokes’s theorem, we say that \( \gamma \) is positively oriented (Fig. 9.4). Intuitively, this means that \( \gamma \) is parametrized in the counterclockwise direction, or that \( \Omega \) is always to the left of \( \gamma \) .

We define a tangent angle function for a curved polygon \( \gamma \) to be a piecewise continuous function \( \theta  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) that satisfies \( T\left( t\right)  = \left( {\cos \theta \left( t\right) ,\sin \theta \left( t\right) }\right) \) at each point \( t \) where \( \gamma \) is smooth, that is continuous from the right at each \( {a}_{i} \) with

\[
\theta \left( {a}_{i}\right)  = \mathop{\lim }\limits_{{t \nearrow  {a}_{i}}}\theta \left( t\right)  + {\varepsilon }_{i} \tag{9.1}
\]

![bo_d7dtff491nqc73eq8m7g_276_452_183_617_361_0.jpg](images/bo_d7dtff491nqc73eq8m7g_276_452_183_617_361_0.jpg)

Fig. 9.4: A positively oriented curved polygon

![bo_d7dtff491nqc73eq8m7g_276_223_794_494_331_0.jpg](images/bo_d7dtff491nqc73eq8m7g_276_223_794_494_331_0.jpg)

Fig. 9.5: Tangent angle at a vertex

![bo_d7dtff491nqc73eq8m7g_276_776_670_538_485_0.jpg](images/bo_d7dtff491nqc73eq8m7g_276_776_670_538_485_0.jpg)

Fig. 9.6: Tangent angle function

and that satisfies

\[
\theta \left( b\right)  = \mathop{\lim }\limits_{{t \nearrow  b}}\theta \left( t\right)  + {\varepsilon }_{k} \tag{9.2}
\]

where \( {\varepsilon }_{k} \) is the exterior angle at \( \gamma \left( b\right) \) . (See Figs. 9.5 and 9.6.) Such a function always exists: start by defining \( \theta \left( t\right) \) for \( t \in  \left\lbrack  {a,{a}_{1}}\right) \) to be any lift of \( T \) on that interval; then on \( \left\lbrack  {{a}_{1},{a}_{2}}\right) \) define \( \theta \left( t\right) \) to be the unique lift that satisfies (9.1), and continue by induction, ending with \( \theta \left( b\right) \) defined by (9.2). Once again, the difference between any two such functions is a constant integral multiple of \( {2\pi } \) . We define the rotation index of \( \gamma \) to be \( \rho \left( \gamma \right)  = \frac{1}{2\pi }\left( {\theta \left( b\right)  - \theta \left( a\right) }\right) \) just as in the smooth case. As before, \( \rho \left( \gamma \right) \) is an integer, because the definition ensures that \( \left( {\cos \theta \left( b\right) ,\sin \theta \left( b\right) }\right)  = \left( {\cos \theta \left( a\right) ,\sin \theta \left( a\right) }\right) \) .

The following theorem was first proved by Heinz Hopf in 1935. (For a readable version of Hopf's proof, see [Hop89, p. 42].) It is frequently referred to by the German name given to it by Hopf, the Umlaufsatz.

Theorem 9.1 (Rotation Index Theorem). The rotation index of a positively oriented curved polygon in the plane is +1 .

![bo_d7dtff491nqc73eq8m7g_277_487_190_554_369_0.jpg](images/bo_d7dtff491nqc73eq8m7g_277_487_190_554_369_0.jpg)

Fig. 9.7: The curve \( \gamma \) after changing the parameter interval and translating \( \gamma \left( a\right) \) to the origin

Proof. Let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) be such a curved polygon. Assume first that all the vertices of \( \gamma \) are flat. This means, in particular, that \( {\gamma }^{\prime } \) is continuous and \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \) . Since \( \gamma \left( a\right)  = \gamma \left( b\right) \) , we can extend \( \gamma \) to a continuous map from \( \mathbb{R} \) to \( {\mathbb{R}}^{2} \) by requiring it to be periodic of period \( b - a \) , and our hypothesis \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \) guarantees that the extended map still has continuous first derivatives. Define \( T\left( t\right)  = {\gamma }^{\prime }\left( t\right) /\left| {{\gamma }^{\prime }\left( t\right) }\right| \) as before.

Let \( \theta  : \mathbb{R} \rightarrow  \mathbb{R} \) be any lift of \( T : \mathbb{R} \rightarrow  {\mathbb{S}}^{1} \) . Then \( {\left. \theta \right| }_{\left\lbrack  a, b\right\rbrack  } \) is a tangent angle function for \( \gamma \) , and thus \( \theta \left( b\right)  = \theta \left( a\right)  + {2\pi \rho }\left( \gamma \right) \) . If we set \( \widetilde{\theta }\left( t\right)  = \theta \left( {t + b - a}\right)  - {2\pi \rho }\left( \gamma \right) \) , then

\[
\left( {\cos \widetilde{\theta }\left( t\right) ,\sin \widetilde{\theta }\left( t\right) }\right)  = \left( {\cos \theta \left( {t + b - a}\right) ,\sin \theta \left( {t + b - a}\right) }\right)  = T\left( {t + b - a}\right)  = T\left( t\right) ,
\]

so \( \widetilde{\theta } \) is also a lift of \( T \) . Because \( \widetilde{\theta }\left( a\right)  = \theta \left( a\right) \) , it follows that \( \widetilde{\theta } \equiv  \theta \) , or in other words the following equation holds for all \( t \in  \mathbb{R} \) :

\[
\theta \left( {t + b - a}\right)  = \theta \left( t\right)  + {2\pi \rho }\left( \gamma \right) . \tag{9.3}
\]

If \( {a}_{1} \) is an arbitrary point in \( \left\lbrack  {a, b}\right\rbrack \) and \( {b}_{1} = {a}_{1} + b - a \) , then \( {\left. \gamma \right| }_{\left\lbrack  {a}_{1},{b}_{1}\right\rbrack  } \) is also a positively oriented curved polygon with only flat vertices, and \( {\left. \theta \right| }_{\left\lbrack  {a}_{1},{b}_{1}\right\rbrack  } \) is a tangent angle function for it. Note that (9.3) implies

\[
\theta \left( {b}_{1}\right)  - \theta \left( {a}_{1}\right)  = \theta \left( {{a}_{1} + b - a}\right)  - \theta \left( {a}_{1}\right)  = \left( {\theta \left( {a}_{1}\right)  + {2\pi \rho }\left( \gamma \right) }\right)  - \theta \left( {a}_{1}\right)  = {2\pi \rho }\left( \gamma \right) ,
\]

so \( {\left. \gamma \right| }_{\left\lbrack  {a}_{1},{b}_{1}\right\rbrack  } \) has the same rotation index as \( {\left. \gamma \right| }_{\left\lbrack  a, b\right\rbrack  } \) . Thus we obtain the same result by restricting \( \gamma \) to any closed interval of length \( b - a \) .

Using this freedom, we can assume that the parameter interval \( \left\lbrack  {a, b}\right\rbrack \) has been chosen so that the \( y \) -coordinate of \( \gamma \) achieves its minimum at \( t = a \) . Moreover, by a translation in the \( {xy} \) -plane (which does not change \( {\gamma }^{\prime } \) or \( \theta \) ), we may as well assume that \( \gamma \left( a\right) \) is the origin. With these adjustments, the image of \( \gamma \) remains in the closed upper half-plane, and \( T\left( a\right)  = T\left( b\right)  = \left( {1,0}\right) \) (Fig. 9.7). By adding a constant integral multiple of \( {2\pi } \) to \( \theta \) if necessary, we can also assume that \( \theta \left( a\right)  = 0 \) .

Next, we define a continuous secant angle function, denoted by \( \varphi \left( {{t}_{1},{t}_{2}}\right) \) , representing the angle between the positive \( x \) -direction and the vector from \( \gamma \left( {t}_{1}\right) \) to \( \gamma \left( {t}_{2}\right) \) . To be precise, let \( \Delta  \subseteq  {\mathbb{R}}^{2} \) be the triangular region \( \Delta  = \left\{  {\left( {{t}_{1},{t}_{2}}\right)  : a \leq  {t}_{1} \leq  {t}_{2} \leq  b}\right\} \)

![bo_d7dtff491nqc73eq8m7g_278_220_195_500_493_0.jpg](images/bo_d7dtff491nqc73eq8m7g_278_220_195_500_493_0.jpg)

Fig. 9.8: The domain of \( \varphi \)

![bo_d7dtff491nqc73eq8m7g_278_769_338_549_349_0.jpg](images/bo_d7dtff491nqc73eq8m7g_278_769_338_549_349_0.jpg)

Fig. 9.9: The secant angle function

(Fig. 9.8), and define a map \( V : \Delta  \rightarrow  {\mathbb{S}}^{1} \) by

\[
V\left( {{t}_{1},{t}_{2}}\right)  = \left\{  \begin{array}{ll} \frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{\left| \gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) \right| }, & {t}_{1} < {t}_{2}\text{ and }\left( {{t}_{1},{t}_{2}}\right)  \neq  \left( {a, b}\right) ; \\  T\left( {t}_{1}\right) , & {t}_{1} = {t}_{2}; \\   - T\left( b\right) , & \left( {{t}_{1},{t}_{2}}\right)  = \left( {a, b}\right) . \end{array}\right.
\]

The function \( V \) is continuous at points where \( {t}_{1} < {t}_{2} \) and \( \left( {{t}_{1},{t}_{2}}\right)  \neq  \left( {a, b}\right) \) , because \( \gamma \) is continuous and injective there. To see that it is continuous elsewhere, note that for \( {t}_{1} < {t}_{2} \) , the fundamental theorem of calculus gives

\[
\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right)  = {\int }_{0}^{1}\frac{d}{ds}\gamma \left( {{t}_{1} + s\left( {{t}_{2} - {t}_{1}}\right) }\right) {ds} = {\int }_{0}^{1}{\gamma }^{\prime }\left( {{t}_{1} + s\left( {{t}_{2} - {t}_{1}}\right) }\right) \left( {{t}_{2} - {t}_{1}}\right) {ds},
\]

and thus

\[
\left| {\frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{{t}_{2} - {t}_{1}} - {\gamma }^{\prime }\left( t\right) }\right|  \leq  {\int }_{0}^{1}\left| {{\gamma }^{\prime }\left( {{t}_{1} + s\left( {{t}_{2} - {t}_{1}}\right) }\right)  - {\gamma }^{\prime }\left( t\right) }\right| {ds}.
\]

Because \( {\gamma }^{\prime } \) is uniformly continuous on the compact set \( \left\lbrack  {a, b}\right\rbrack \) , this last expression can be made as small as desired by taking \( \left( {{t}_{1},{t}_{2}}\right) \) close to \( \left( {t, t}\right) \) . It follows that

\[
\mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {t, t}\right) } \\  {{t}_{1} < {t}_{2}} }}\frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{{t}_{2} - {t}_{1}} = {\gamma }^{\prime }\left( t\right) ,
\]

and therefore

\[
\mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {t, t}\right) } \\  {{t}_{1} < {t}_{2}} }}V\left( {{t}_{1},{t}_{2}}\right)  = \mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {t, t}\right) } \\  {{t}_{1} < {t}_{2}} }}\frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{\left| \gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) \right| }
\]

\[
= \mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {t, t}\right) } \\  {{t}_{1} < {t}_{2}} }}\frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{{t}_{2} - {t}_{1}}/\left| \frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1}\right) }{{t}_{2} - {t}_{1}}\right|
\]

\[
= \frac{{\gamma }^{\prime }\left( t\right) }{\left| {\gamma }^{\prime }\left( t\right) \right| } = T\left( t\right)  = V\left( {t, t}\right) .
\]

Similarly, because \( T \) is continuous,

\[
\mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {t, t}\right) } \\  {{t}_{1} = {t}_{2}} }}V\left( {{t}_{1},{t}_{2}}\right)  = \mathop{\lim }\limits_{{{t}_{1} \rightarrow  t}}T\left( {t}_{1}\right)  = T\left( t\right)  = V\left( {t, t}\right) .
\]

It follows that \( V \) is continuous at \( \left( {t, t}\right) \) .

To prove that \( V \) is continuous at \( \left( {a, b}\right) \) , recall that we have extended \( \gamma \) to be periodic of period \( b - a \) . The argument above gives

\[
\mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {a, b}\right) } \\  {{t}_{1} < {t}_{2}} }}V\left( {{t}_{1},{t}_{2}}\right)  = \mathop{\lim }\limits_{\substack{{\left( {{t}_{1},{t}_{2}}\right)  \rightarrow  \left( {a, b}\right) } \\  {{t}_{1} < {t}_{2}} }}\frac{\gamma \left( {t}_{2}\right)  - \gamma \left( {{t}_{1} + b - a}\right) }{\left| \gamma \left( {t}_{2}\right)  - \gamma \left( {t}_{1} + b - a\right) \right| }
\]

\[
= \mathop{\lim }\limits_{\substack{{\left( {{s}_{1},{s}_{2}}\right)  \rightarrow  \left( {b, b}\right) } \\  {{s}_{1} > {s}_{2}} }}\frac{\gamma \left( {s}_{2}\right)  - \gamma \left( {s}_{1}\right) }{\left| \gamma \left( {s}_{2}\right)  - \gamma \left( {s}_{1}\right) \right| } =  - T\left( b\right)  = V\left( {a, b}\right) .
\]

Thus \( V \) is continuous.

Since \( \Delta \) is simply connected, Corollary A. 57 guarantees that \( V : \Delta  \rightarrow  {\mathbb{S}}^{1} \) has a continuous lift \( \varphi  : \Delta  \rightarrow  \mathbb{R} \) , which is unique if we require \( \varphi \left( {a, a}\right)  = 0 \) (Fig. 9.9). This is our secant angle function.

We can express the rotation index in terms of the secant angle function as follows:

\[
\rho \left( \gamma \right)  = \frac{1}{2\pi }\left( {\theta \left( b\right)  - \theta \left( a\right) }\right)  = \frac{1}{2\pi }\left( {\varphi \left( {b, b}\right)  - \varphi \left( {a, a}\right) }\right)  = \frac{1}{2\pi }\varphi \left( {b, b}\right) .
\]

Observe that along the side of \( \Delta \) where \( {t}_{1} = a \) and \( {t}_{2} \in  \left\lbrack  {a, b}\right\rbrack \) , the vector \( V\left( {a,{t}_{2}}\right) \) has its tail at the origin and its head in the upper half-plane. Since we stipulate that \( \varphi \left( {a, a}\right)  = 0 \) , we must have \( \varphi \left( {a,{t}_{2}}\right)  \in  \left\lbrack  {0,\pi }\right\rbrack \) on this segment. By continuity, therefore, \( \varphi \left( {a, b}\right)  = \pi \) (since \( \varphi \left( {a, b}\right) \) represents the tangent angle of \( - T\left( b\right)  = \left( {-1,0}\right) \) ). Similarly, on the side where \( {t}_{2} = b \) , the vector \( V\left( {{t}_{1}, b}\right) \) has its head at the origin and its tail in the upper half-plane, so \( \varphi \left( {{t}_{1}, b}\right)  \in  \left\lbrack  {\pi ,{2\pi }}\right\rbrack \) . Therefore, since \( \varphi \left( {b, b}\right) \) represents the tangent angle of \( T\left( b\right)  = \left( {1,0}\right) \) , we must have \( \varphi \left( {b, b}\right)  = {2\pi } \) and therefore \( \rho \left( \gamma \right)  = 1 \) . This completes the proof for the case in which \( {\gamma }^{\prime } \) is continuous.

Now suppose \( \gamma \) has one or more ordinary vertices. It suffices to show there is a curve with a continuous velocity vector field that has the same rotation index as \( \gamma \) . We will construct such a curve by "rounding the corners" of \( \gamma \) . It will simplify the proof somewhat if we choose the parameter interval \( \left\lbrack  {a, b}\right\rbrack \) so that \( \gamma \left( a\right)  = \gamma \left( b\right) \) is not one of the ordinary vertices.

![bo_d7dtff491nqc73eq8m7g_280_214_194_1012_527_0.jpg](images/bo_d7dtff491nqc73eq8m7g_280_214_194_1012_527_0.jpg)

Fig. 9.10: Isolating the change in the tangent angle at a vertex

![bo_d7dtff491nqc73eq8m7g_280_355_832_824_426_0.jpg](images/bo_d7dtff491nqc73eq8m7g_280_355_832_824_426_0.jpg)

Fig. 9.11: Rounding a corner

Let \( \gamma \left( {a}_{i}\right) \) be any ordinary vertex, let \( {\varepsilon }_{i} \) be its exterior angle, and let \( \alpha \) be a positive number less than \( \frac{1}{2}\left( {\pi  - \left| {\varepsilon }_{i}\right| }\right) \) . Recall that \( \theta \) is continuous from the right at \( {a}_{i} \) and \( \mathop{\lim }\limits_{{t \nearrow  {a}_{i}}}\theta \left( t\right)  = \theta \left( {a}_{i}\right)  - {\varepsilon }_{i} \) . Therefore, we can choose \( \delta \) small enough that \( \left| {\theta \left( t\right)  - \left( {\theta \left( {a}_{i}\right)  - {\varepsilon }_{i}}\right) }\right|  < \alpha \) when \( t \in  \left( {{a}_{i} - \delta ,{a}_{i}}\right) \) , and \( \left| {\theta \left( t\right)  - \theta \left( {a}_{i}\right) }\right|  < \alpha \) when \( t \in \; \left( {{a}_{i},{a}_{i} + \delta }\right) \) .

The image under \( \gamma \) of \( \left\lbrack  {a, b}\right\rbrack   \smallsetminus  \left( {{a}_{i} - \delta ,{a}_{i} + \delta }\right) \) is a compact set that does not contain \( \gamma \left( {a}_{i}\right) \) , so we can choose \( r \) small enough that \( \gamma \) does not enter \( {\bar{B}}_{r}\left( {\gamma \left( {a}_{i}\right) }\right) \) except when \( t \in  \left( {{a}_{i} - \delta ,{a}_{i} + \delta }\right) \) . Let \( {t}_{1} \in  \left( {{a}_{i} - \delta ,{a}_{i}}\right) \) denote a time when \( \gamma \) enters \( {\bar{B}}_{r}\left( {\gamma \left( {a}_{i}\right) }\right) \) , and \( {t}_{2} \in  \left( {{a}_{i},{a}_{i} + \delta }\right) \) a time when it leaves (Fig. 9.10). By our choice of \( \delta \) , the total change in \( \theta \left( t\right) \) is not more than \( \alpha \) when \( t \in  \left\lbrack  {{t}_{1},{a}_{i}}\right) \) , and again not more than \( \alpha \) when \( t \in  \left( {{a}_{i},{t}_{2}}\right\rbrack \) . Therefore, the total change \( {\Delta \theta } \) in \( \theta \left( t\right) \) during the time interval \( \left\lbrack  {{t}_{1},{t}_{2}}\right\rbrack \) is between \( {\varepsilon }_{i} - {2\alpha } \) and \( {\varepsilon }_{i} + {2\alpha } \) , which implies \( - \pi  < {\Delta \theta } < \pi \) .

Now we simply replace \( {\left. \gamma \right| }_{\left\lbrack  {t}_{1},{t}_{2}\right\rbrack  } \) with a smooth curve segment \( \sigma \) that has the same velocity as \( \gamma \) at \( \gamma \left( {t}_{1}\right) \) and \( \gamma \left( {t}_{2}\right) \) , and whose tangent angle increases or decreases monotonically from \( \theta \left( {t}_{1}\right) \) to \( \theta \left( {t}_{2}\right) \) ; an arc of a hyperbola will do (Fig. 9.11). Since the change in tangent angle of \( \sigma \) is between \( - \pi \) and \( \pi \) and represents the angle between \( T\left( {t}_{1}\right) \) and \( T\left( {t}_{2}\right) \) , it must be exactly \( {\Delta \theta } \) . Repeating this process for each vertex, we obtain a new curved polygon with a continuous velocity vector field whose rotation index is the same as that of \( \gamma \) , thus proving the theorem.

![bo_d7dtff491nqc73eq8m7g_281_255_188_889_288_0.jpg](images/bo_d7dtff491nqc73eq8m7g_281_255_188_889_288_0.jpg)

Fig. 9.12: A curved polygon on a surface

From the rotation index theorem, it is not hard to deduce the three local-to-global theorems mentioned at the beginning of the chapter as corollaries. (The angle-sum theorem is immediate; for the total curvature theorem, the trick is to show that \( {\theta }^{\prime }\left( t\right) \) is equal to the signed curvature of \( \gamma \) ; the circumference theorem follows from the total curvature theorem as mentioned in Chapter 1.) However, instead of proving them directly, we will prove a general formula, called the Gauss-Bonnet formula, from which these results and more follow easily. You will easily see how the statement and proof of Theorem 9.3 below can be simplified in case the metric is Euclidean.

## The Gauss-Bonnet Formula

We now direct our attention to the case of an oriented Riemannian 2-manifold \( \left( {M, g}\right) \) . In this setting, an admissible simple closed curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is called a curved polygon in \( \mathbf{M} \) if the image of \( \gamma \) is the boundary of a precompact open set \( \Omega  \subseteq  M \) , and there is an oriented smooth coordinate disk containing \( \overline{\Omega } \) under whose image \( \gamma \) is a curved polygon in the plane (Fig. 9.12). As in the planar case, we call \( \Omega \) the interior of \( \gamma \) . A curved polygon whose edges are all geodesic segments is called a geodesic polygon.

For a curved polygon \( \gamma \) in \( M \) , our previous definitions go through almost unchanged. We say that \( \gamma \) is positively oriented if it is parametrized in the direction of its Stokes orientation as the boundary of \( \Omega \) . On each smooth segment of \( \gamma \) , we define the unit tangent vector field \( T\left( t\right)  = {\gamma }^{\prime }\left( t\right) /{\left| {\gamma }^{\prime }\left( t\right) \right| }_{g} \) . If \( \gamma \left( {a}_{i}\right) \) is an ordinary or flat vertex, we define the exterior angle of \( \gamma \) at \( \gamma \left( {a}_{i}\right) \) as the oriented measure \( {\varepsilon }_{i} \) of the angle from \( T\left( {a}_{i}^{ - }\right) \) to \( T\left( {a}_{i}^{ + }\right) \) with respect to the \( g \) -inner product and the given orientation of \( M \) ; explicitly, this is

\[
{\varepsilon }_{i} = \frac{d{V}_{g}\left( {T\left( {a}_{i}^{ - }\right) , T\left( {a}_{i}^{ + }\right) }\right) }{\left| d{V}_{g}\left( T\left( {a}_{i}^{ - }\right) , T\left( {a}_{i}^{ + }\right) \right) \right| }\arccos {\left\langle  T\left( {a}_{i}^{ - }\right) , T\left( {a}_{i}^{ + }\right) \right\rangle  }_{g}. \tag{9.4}
\]

The corresponding interior angle of \( \gamma \) at \( \gamma \left( {a}_{i}\right) \) is \( {\theta }_{i} = \pi  - {\varepsilon }_{i} \) . Exterior and interior angles at \( \gamma \left( a\right)  = \gamma \left( b\right) \) are defined similarly.

We need a version of the rotation index theorem for curved polygons in \( M \) . Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a curved polygon and \( \Omega \) is its interior, and let \( \left( {U,\varphi }\right) \) be an oriented smooth chart such that \( U \) contains \( \overline{\Omega } \) . Using the coordinate map \( \varphi \) to transfer \( \gamma ,\Omega \) , and \( g \) to the plane, we may as well assume that \( g \) is a metric on some open subset \( \widehat{U} \subseteq  {\mathbb{R}}^{2} \) , and \( \gamma \) is a curved polygon in \( \widehat{U} \) . Let \( \left( {{E}_{1},{E}_{2}}\right) \) be the oriented orthonormal frame for \( g \) obtained by applying the Gram-Schmidt algorithm to \( \left( {{\partial }_{x},{\partial }_{y}}\right) \) , so that \( {E}_{1} \) is a positive scalar multiple of \( {\partial }_{x} \) everywhere in \( \widehat{U} \) .

We define a tangent angle function for \( \gamma \) to be a piecewise continuous function \( \theta  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) that satisfies

\[
T\left( t\right)  = {\left. \cos \theta \left( t\right) {E}_{1}\right| }_{\gamma \left( t\right) } + {\left. \sin \theta \left( t\right) {E}_{2}\right| }_{\gamma \left( t\right) }
\]

at each \( t \) where \( {\gamma }^{\prime } \) is continuous, and that is continuous from the right and satisfies (9.1) and (9.2) at vertices. The existence of such a function follows as in the planar case, using the fact that

\[
T\left( t\right)  = {\left. {u}_{1}\left( t\right) {E}_{1}\right| }_{\gamma \left( t\right) } + {\left. {u}_{2}\left( t\right) {E}_{2}\right| }_{\gamma \left( t\right) } \tag{9.5}
\]

for a pair of piecewise continuous functions \( {u}_{1},{u}_{2} : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) that can be regarded as the coordinate functions of a map \( \left( {{u}_{1},{u}_{2}}\right)  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{S}}^{1} \) because \( T \) has unit length.

The rotation index of \( \gamma \) is \( \rho \left( \gamma \right)  = \frac{1}{2\pi }\left( {\theta \left( b\right)  - \theta \left( a\right) }\right) \) . Because of the role played by the specific frame \( \left( {{E}_{1},{E}_{2}}\right) \) in the definition, it is not obvious that the rotation index has any coordinate-independent meaning; however, the following easy consequence of the rotation index theorem shows that it does not depend on the choice of coordinates.

Lemma 9.2. If \( M \) is an oriented Riemannian 2-manifold, the rotation index of every positively oriented curved polygon in \( M \) is +1 .

Proof. If we use the given oriented coordinate chart to regard \( \gamma \) as a curved polygon in the plane, we can compute its tangent angle function either with respect to \( g \) or with respect to the Euclidean metric \( \bar{g} \) . In either case, \( \rho \left( \gamma \right) \) is an integer because \( \theta \left( a\right) \) and \( \theta \left( b\right) \) both represent the angle between the same two vectors, calculated with respect to some inner product. Now for \( 0 \leq  s \leq  1 \) , let \( {g}_{s} = {sg} + \left( {1 - s}\right) \bar{g} \) . By the same reasoning, the rotation index \( {\rho }_{{g}_{s}}\left( \gamma \right) \) with respect to \( {g}_{s} \) is also an integer for each \( s \) , so the function \( f\left( s\right)  = {\rho }_{{g}_{s}}\left( \gamma \right) \) is integer-valued.

In fact, the function \( f \) is continuous in \( s \) , as can be deduced easily from the following observations: (1) Our preferred \( {g}_{s} \) -orthonormal frame \( \left( {{E}_{1}^{\left( s\right) },{E}_{2}^{\left( s\right) }}\right) \) depends continuously on \( s \) , as can be seen from the formulas (2.5)-(2.6) used to implement the Gram-Schmidt algorithm. (2) On every interval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) where \( \gamma \) is smooth, the functions \( {u}_{1} \) and \( {u}_{2} \) satisfying the \( {g}_{s} \) -analogue of (9.5) can be expressed as \( {u}_{j}\left( {t, s}\right)  = {\left\langle  {T}_{s}\left( t\right) ,{\left. {E}_{j}^{\left( s\right) }\right| }_{\gamma \left( t\right) }\right\rangle  }_{{g}_{s}} \) , where \( {T}_{s}\left( t\right)  = {\gamma }^{\prime }\left( t\right) /{\left| {\gamma }^{\prime }\left( t\right) \right| }_{{g}_{s}} \) . Thus \( {u}_{1} \) and \( {u}_{2} \) depend continuously on \( \left( {t, s}\right)  \in  \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack \) , so the function \( \left( {{u}_{1},{u}_{2}}\right)  : \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack   \times \; \left\lbrack  {0,1}\right\rbrack   \rightarrow  {\mathbb{S}}^{1} \) has a continuous lift \( \theta  : \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{R} \) , uniquely determined by its value at one point. (3) At each vertex, it follows from formula (9.4) that the exterior angle depends continuously on \( {g}_{s} \) .

![bo_d7dtff491nqc73eq8m7g_283_511_190_512_395_0.jpg](images/bo_d7dtff491nqc73eq8m7g_283_511_190_512_395_0.jpg)

Fig. 9.13: \( N\left( t\right) \) is the inward-pointing normal

Because \( f \) is continuous and integer-valued, it follows that \( {\rho }_{g}\left( \gamma \right)  = f\left( 1\right)  = \; f\left( 0\right)  = {\rho }_{\bar{g}}\left( \gamma \right)  = 1 \) , which was to be proved.

From this point onward, we assume for convenience that our curved polygon \( \gamma \) is given a unit-speed parametrization, so the unit tangent vector field \( T\left( t\right) \) is equal to \( {\gamma }^{\prime }\left( t\right) \) . There is a unique unit normal vector field \( N \) along the smooth portions of \( \gamma \) such that \( \left( {{\gamma }^{\prime }\left( t\right) , N\left( t\right) }\right) \) is an oriented orthonormal basis for \( {T}_{\gamma \left( t\right) }M \) for each \( t \) . If \( \gamma \) is positively oriented as the boundary of \( \Omega \) , this is equivalent to \( N \) being the inward-pointing normal to \( \partial \Omega \) (Fig. 9.13). We define the signed curvature of \( \gamma \) at smooth points of \( \gamma \) by

\[
{\kappa }_{N}\left( t\right)  = {\left\langle  {D}_{t}{\gamma }^{\prime }\left( t\right) , N\left( t\right) \right\rangle  }_{g}.
\]

By differentiating \( {\left| {\gamma }^{\prime }\left( t\right) \right| }_{g}^{2} \equiv  1 \) , we see that \( {D}_{t}{\gamma }^{\prime }\left( t\right) \) is orthogonal to \( {\gamma }^{\prime }\left( t\right) \) , and therefore we can write \( {D}_{t}{\gamma }^{\prime }\left( t\right)  = {\kappa }_{N}\left( t\right) N\left( t\right) \) , and the (unsigned) geodesic curvature of \( \gamma \) is \( \kappa \left( t\right)  = \left| {{\kappa }_{N}\left( t\right) }\right| \) . The sign of \( {\kappa }_{N}\left( t\right) \) is positive if \( \gamma \) is curving toward \( \Omega \) , and negative if it is curving away.

Theorem 9.3 (The Gauss-Bonnet Formula). Let \( \left( {M, g}\right) \) be an oriented Riemannian 2-manifold. Suppose \( \gamma \) is a positively oriented curved polygon in \( M \) , and \( \Omega \) is its interior. Then

\[
{\int }_{\Omega }{KdA} + {\int }_{\gamma }{\kappa }_{N}{ds} + \mathop{\sum }\limits_{{i = 1}}^{k}{\varepsilon }_{i} = {2\pi } \tag{9.6}
\]

where \( K \) is the Gaussian curvature of \( g,{dA} \) is its Riemannian volume form, \( {\varepsilon }_{1},\ldots ,{\varepsilon }_{k} \) are the exterior angles of \( \gamma \) , and the second integral is taken with respect to arc length (Problem 2-32).

Proof. Let \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) be an admissible partition of \( \left\lbrack  {a, b}\right\rbrack \) , and let \( \left( {x, y}\right) \) be oriented smooth coordinates on an open set \( U \) containing \( \overline{\Omega } \) . Let \( \theta  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) be a tangent angle function for \( \gamma \) . Using the rotation index theorem and the fundamental theorem of calculus, we can write

\[
{2\pi } = \theta \left( b\right)  - \theta \left( a\right)  = \mathop{\sum }\limits_{{i = 1}}^{k}{\varepsilon }_{i} + \mathop{\sum }\limits_{{i = 1}}^{k}{\int }_{{a}_{i - 1}}^{{a}_{i}}{\theta }^{\prime }\left( t\right) {dt}. \tag{9.7}
\]

To prove (9.6), we need to derive a relationship among \( {\theta }^{\prime },{\kappa }_{N} \) , and \( K \) .

Let \( \left( {{E}_{1},{E}_{2}}\right) \) be the oriented \( g \) -orthonormal frame obtained by applying the Gram-Schmidt algorithm to \( \left( {\partial /\partial x,\partial /\partial y}\right) \) as before. Then by definition of \( \theta \) and \( N \) , the following formulas hold at smooth points of \( \gamma \) :

\[
{\gamma }^{\prime }\left( t\right)  = {\left. \cos \theta \left( t\right) {E}_{1}\right| }_{\gamma \left( t\right) } + {\left. \sin \theta \left( t\right) {E}_{2}\right| }_{\gamma \left( t\right) }
\]

\[
N\left( t\right)  =  - {\left. \sin \theta \left( t\right) {E}_{1}\right| }_{\gamma \left( t\right) } + {\left. \cos \theta \left( t\right) {E}_{2}\right| }_{\gamma \left( t\right) }.
\]

Differentiating \( {\gamma }^{\prime } \) (and omitting the \( t \) dependence from the notation for simplicity), we get

(9.8)

\[
{D}_{t}{\gamma }^{\prime } =  - \left( {\sin \theta }\right) {\theta }^{\prime }{E}_{1} + \left( {\cos \theta }\right) {\nabla }_{{\gamma }^{\prime }}{E}_{1} + \left( {\cos \theta }\right) {\theta }^{\prime }{E}_{2} + \left( {\sin \theta }\right) {\nabla }_{{\gamma }^{\prime }}{E}_{2}
\]

\[
= {\theta }^{\prime }N + \left( {\cos \theta }\right) {\nabla }_{{\gamma }^{\prime }}{E}_{1} + \left( {\sin \theta }\right) {\nabla }_{{\gamma }^{\prime }}{E}_{2}.
\]

Next we analyze the covariant derivatives of \( {E}_{1} \) and \( {E}_{2} \) . Because \( \left( {{E}_{1},{E}_{2}}\right) \) is an orthonormal frame, for every vector \( v \) we have

\[
0 = {\nabla }_{v}{\left| {E}_{1}\right| }^{2} = 2\left\langle  {{\nabla }_{v}{E}_{1},{E}_{1}}\right\rangle  ,
\]

\[
0 = {\nabla }_{v}{\left| {E}_{2}\right| }^{2} = 2\left\langle  {{\nabla }_{v}{E}_{2},{E}_{2}}\right\rangle  ,
\]

\[
0 = {\nabla }_{v}\left\langle  {{E}_{1},{E}_{2}}\right\rangle   = \left\langle  {{\nabla }_{v}{E}_{1},{E}_{2}}\right\rangle   + \left\langle  {{E}_{1},{\nabla }_{v}{E}_{2}}\right\rangle  .
\]

The first two equations show that \( {\nabla }_{v}{E}_{1} \) is a multiple of \( {E}_{2} \) and \( {\nabla }_{v}{E}_{2} \) is a multiple of \( {E}_{1} \) . Define a 1-form \( \omega \) by

\[
\omega \left( v\right)  = \left\langle  {{E}_{1},{\nabla }_{v}{E}_{2}}\right\rangle   =  - \left\langle  {{\nabla }_{v}{E}_{1},{E}_{2}}\right\rangle  .
\]

It follows that the covariant derivatives of the basis vectors are given by

(9.9)

\[
{\nabla }_{v}{E}_{1} =  - \omega \left( v\right) {E}_{2}
\]

\[
{\nabla }_{v}{E}_{2} = \omega \left( v\right) {E}_{1}
\]

Thus the 1-form \( \omega \) completely determines the connection in \( U \) . (In fact, when the connection is expressed in terms of the local frame \( \left( {{E}_{1},{E}_{2}}\right) \) as in Problem 4-14, this computation shows that the connection 1-forms are just \( {\omega }_{2}{}^{1} =  - {\omega }_{1}{}^{2} = \omega ,{\omega }_{1}{}^{1} = \; {\omega }_{2}{}^{2} = 0 \) ; but it is simpler in this case just to derive the result directly as we have done.)

Using (9.8) and (9.9), we can compute

\[
{\kappa }_{N} = \left\langle  {{D}_{t}{\gamma }^{\prime }, N}\right\rangle
\]

\[
= \left\langle  {{\theta }^{\prime }N, N}\right\rangle   + \cos \theta \left\langle  {{\nabla }_{{\gamma }^{\prime }}{E}_{1}, N}\right\rangle   + \sin \theta \left\langle  {{\nabla }_{{\gamma }^{\prime }}{E}_{2}, N}\right\rangle
\]

\[
= {\theta }^{\prime } - \cos \theta \left\langle  {\omega \left( {\gamma }^{\prime }\right) {E}_{2}, N}\right\rangle   + \sin \theta \left\langle  {\omega \left( {\gamma }^{\prime }\right) {E}_{1}, N}\right\rangle
\]

\[
= {\theta }^{\prime } - {\cos }^{2}{\theta \omega }\left( {\gamma }^{\prime }\right)  - {\sin }^{2}{\theta \omega }\left( {\gamma }^{\prime }\right)
\]

\[
= {\theta }^{\prime } - \omega \left( {\gamma }^{\prime }\right) \text{ . }
\]

Therefore, (9.7) becomes

\[
{2\pi } = \mathop{\sum }\limits_{{i = 1}}^{k}{\varepsilon }_{i} + \mathop{\sum }\limits_{{i = 1}}^{k}{\int }_{{a}_{i - 1}}^{{a}_{i}}{\kappa }_{N}\left( t\right) {dt} + \mathop{\sum }\limits_{{i = 1}}^{k}{\int }_{{a}_{i - 1}}^{{a}_{i}}\omega \left( {{\gamma }^{\prime }\left( t\right) }\right) {dt}
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{k}{\varepsilon }_{i} + {\int }_{\gamma }{\kappa }_{N}{ds} + {\int }_{\gamma }\omega
\]

The theorem will therefore be proved if we can show that

\[
{\int }_{\gamma }\omega  = {\int }_{\Omega }{KdA} \tag{9.10}
\]

Because \( \Omega \) is a smooth manifold with corners (see [LeeSM, pp. 415-419]), we can apply Stokes's theorem and conclude that the left-hand side of (9.10) is equal to \( {\int }_{\Omega }{d\omega } \) . The last step of the proof is to show that \( {d\omega } = {KdA} \) . This follows from the general formula relating the curvature tensor and the connection 1-forms given in Problem 7-5; but in the case of two dimensions we can give an easy direct proof. Since \( \left( {{E}_{1},{E}_{2}}\right) \) is an oriented orthonormal frame, it follows from Proposition 2.41 that \( {dA}\left( {{E}_{1},{E}_{2}}\right)  = 1 \) . Using (9.9), we compute

\[
{KdA}\left( {{E}_{1},{E}_{2}}\right)  = K = {Rm}\left( {{E}_{1},{E}_{2},{E}_{2},{E}_{1}}\right)
\]

\[
= \left\langle  {{\nabla }_{{E}_{1}}{\nabla }_{{E}_{2}}{E}_{2} - {\nabla }_{{E}_{2}}{\nabla }_{{E}_{1}}{E}_{2} - {\nabla }_{\left\lbrack  {E}_{1},{E}_{2}\right\rbrack  }{E}_{2},{E}_{1}}\right\rangle
\]

\[
= \left\langle  {{\nabla }_{{E}_{1}}\left( {\omega \left( {E}_{2}\right) {E}_{1}}\right)  - {\nabla }_{{E}_{2}}\left( {\omega \left( {E}_{1}\right) {E}_{1}}\right)  - \omega \left( \left\lbrack  {{E}_{1},{E}_{2}}\right\rbrack  \right) {E}_{1},{E}_{1}}\right\rangle
\]

\[
= \left\langle  {{E}_{1}\left( {\omega \left( {E}_{2}\right) }\right) {E}_{1} + \omega \left( {E}_{2}\right) {\nabla }_{{E}_{1}}{E}_{1} - {E}_{2}\left( {\omega \left( {E}_{1}\right) }\right) {E}_{1}}\right.
\]

\[
\left. {-\omega \left( {E}_{1}\right) {\nabla }_{{E}_{2}}{E}_{1} - \omega \left( \left\lbrack  {{E}_{1},{E}_{2}}\right\rbrack  \right) {E}_{1},{E}_{1}}\right\rangle
\]

\[
= {E}_{1}\left( {\omega \left( {E}_{2}\right) }\right)  - {E}_{2}\left( {\omega \left( {E}_{1}\right) }\right)  - \omega \left( \left\lbrack  {{E}_{1},{E}_{2}}\right\rbrack  \right)
\]

\[
= {d\omega }\left( {{E}_{1},{E}_{2}}\right) \text{ . }
\]

This completes the proof.

The three local-to-global theorems of plane geometry stated in Chapter 1 follow from the Gauss-Bonnet formula as easy corollaries.

Corollary 9.4 (Angle-Sum Theorem). The sum of the interior angles of a Euclidean triangle is \( \pi \) .

Corollary 9.5 (Circumference Theorem). The circumference of a Euclidean circle of radius \( R \) is \( {2\pi R} \) .

![bo_d7dtff491nqc73eq8m7g_286_292_186_951_398_0.jpg](images/bo_d7dtff491nqc73eq8m7g_286_292_186_951_398_0.jpg)

Fig. 9.14: Valid and invalid intersections of triangles in a triangulation

Corollary 9.6 (Total Curvature Theorem). If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) is a smooth, unit-speed, simple closed curve such that \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \) , and \( N \) is the inward-pointing normal, then

\[
{\int }_{a}^{b}{\kappa }_{N}\left( t\right) {dt} = {2\pi }
\]

## The Gauss-Bonnet Theorem

It is now a relatively easy matter to "globalize" the Gauss-Bonnet formula to obtain the Gauss-Bonnet theorem. The link between the local and global results is provided by triangulations, so we begin by discussing this construction borrowed from algebraic topology.

Let \( M \) be a smooth, compact 2-manifold. A curved triangle in \( M \) is a curved polygon with exactly three edges and three vertices. A smooth triangulation of \( M \) is a finite collection of curved triangles with disjoint interiors such that the union of the triangles with their interiors is \( M \) , and the intersection of any pair of triangles (if not empty) is either a single vertex of each or a single edge of each (Fig. 9.14). Every smooth, compact surface possesses a smooth triangulation. In fact, it was proved by Tibor Radó [Rad25] in 1925 that every compact topological 2-manifold possesses a triangulation (without the assumption of smoothness of the edges, of course), in which every edge belongs to exactly two triangles. There is a proof for the smooth case that is not terribly hard, based on choosing geodesic triangles contained in convex geodesic balls (see Problem 9-5).

If \( M \) is a triangulated 2-manifold, the Euler characteristic of \( M \) (with respect to the given triangulation) is defined to be

\[
\chi \left( M\right)  = V - E + F,
\]

where \( V \) is the number of vertices in the triangulation, \( E \) is the number of edges, and \( F \) is the number of faces (the interiors of the triangles). It is an important result of algebraic topology that the Euler characteristic is in fact a topological invariant, and is independent of the choice of triangulation (see [LeeTM, Cor. 10.25]), but we do not need that result here.

Theorem 9.7 (The Gauss-Bonnet Theorem). If \( \left( {M, g}\right) \) is a smoothly triangulated compact Riemannian 2-manifold, then

\[
{\int }_{M}{KdA} = {2\pi \chi }\left( M\right)
\]

where \( K \) is the Gaussian curvature of \( g \) and \( {dA} \) is its Riemannian density.

Proof. We may as well assume that \( M \) is connected, because if not we can prove the theorem for each connected component and add up the results.

First consider the case in which \( M \) is orientable. In this case, we can choose an orientation for \( M \) , and then \( {\int }_{M}{KdA} \) gives the same result whether we interpret \( {dA} \) as the Riemannian density or as the Riemannian volume form, so we will use the latter interpretation for the proof. Let \( \left\{  {{\Omega }_{i} : i = 1,\ldots , F}\right\} \) denote the faces of the triangulation, and for each \( i \) , let \( \left\{  {{\gamma }_{ij} : j = 1,2,3}\right\} \) be the edges of \( {\Omega }_{i} \) and \( \left\{  {{\theta }_{ij} : j = }\right. \; 1,2,3\} \) its interior angles. Since each exterior angle is \( \pi \) minus the corresponding interior angle, applying the Gauss-Bonnet formula to each triangle and summing over \( i \) gives

\[
\mathop{\sum }\limits_{{i = 1}}^{F}{\int }_{{\Omega }_{i}}{KdA} + \mathop{\sum }\limits_{{i = 1}}^{F}\mathop{\sum }\limits_{{j = 1}}^{3}{\int }_{{\gamma }_{ij}}{\kappa }_{N}{ds} + \mathop{\sum }\limits_{{i = 1}}^{F}\mathop{\sum }\limits_{{j = 1}}^{3}\left( {\pi  - {\theta }_{ij}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{F}{2\pi }. \tag{9.11}
\]

Note that each edge integral appears exactly twice in the above sum, with opposite orientations, so the integrals of \( {\kappa }_{N} \) all cancel out. Thus (9.11) becomes

\[
{\int }_{M}{KdA} + {3\pi F} - \mathop{\sum }\limits_{{i = 1}}^{F}\mathop{\sum }\limits_{{j = 1}}^{3}{\theta }_{ij} = {2\pi F}. \tag{9.12}
\]

Note also that each interior angle \( {\theta }_{ij} \) appears exactly once. At each vertex, the angles that touch that vertex must have interior measures that add up to \( {2\pi } \) (Fig. 9.15); thus the angle sum can be rearranged to give exactly \( {2\pi V} \) . Equation (9.12) thus can be written

\[
{\int }_{M}{KdA} = {2\pi V} - {\pi F}. \tag{9.13}
\]

Finally, since each edge appears in exactly two triangles, and each triangle has exactly three edges, the total number of edges counted with multiplicity is \( {2E} = {3F} \) , where we count each edge once for each triangle in which it appears. This means that \( F = {2E} - {2F} \) , so (9.13) finally becomes

\[
{\int }_{M}{KdA} = {2\pi V} - {2\pi E} + {2\pi F} = {2\pi \chi }\left( M\right) .
\]

![bo_d7dtff491nqc73eq8m7g_288_508_185_519_454_0.jpg](images/bo_d7dtff491nqc73eq8m7g_288_508_185_519_454_0.jpg)

Fig. 9.15: Interior angles at a vertex add up to \( {2\pi } \)

Now suppose \( M \) is nonorientable. Then Proposition B. 18 shows that there is an ori-entable connected smooth manifold \( \widehat{M} \) that admits a 2-sheeted smooth covering \( \widehat{\pi } : \widehat{M} \rightarrow  M \) , and Exercise A. 62 shows that \( \widehat{M} \) is compact. If we endow \( \widehat{M} \) with the metric \( \widehat{g} = {\widehat{\pi }}^{ * }g \) , then the Riemannian density of \( \widehat{g} \) is given by \( \widehat{dA} = {\widehat{\pi }}^{ * }{dA} \) , and its Gaussian curvature is \( \widehat{K} = {\widehat{\pi }}^{ * }K \) , so \( {\widehat{\pi }}^{ * }\left( {KdA}\right)  = \widehat{K}\widehat{dA} \) . The result of Problem 2-14 shows that \( {\int }_{\widehat{M}}\widehat{K}\widehat{dA} = 2{\int }_{M}{KdA} \) .

To compare Euler characteristics, we will show that the given triangulation of \( M \) "lifts" to a smooth triangulation of \( \widehat{M} \) . To see this, let \( \gamma \) be any curved triangle in \( M \) and let \( \Omega \) be its interior. By definition, this means that there exists a smooth chart \( \left( {U,\varphi }\right) \) whose domain contains \( \overline{\Omega } \) and whose image is a disk \( D \subseteq  {\mathbb{R}}^{2} \) , and such that \( \varphi \left( \overline{\Omega }\right)  = {\overline{\Omega }}_{0} \) , where \( {\Omega }_{0} \) is the interior of a curved triangle \( {\gamma }_{0} \) in \( {\mathbb{R}}^{2} \) . Then \( {\varphi }^{-1} \) is an embedding of \( D \) into \( M \) , which restricts to a diffeomorphism \( F : {\overline{\Omega }}_{0} \rightarrow  \overline{\Omega } \) . Because \( D \) is simply connected, it follows from Corollary A. 57 that \( {\varphi }^{-1} \) (and therefore also \( F \) ) has a lift to \( \widehat{M} \) , which is smooth because \( \widehat{\pi } \) is a local diffeomorphism; and because the covering is two-sheeted, there are exactly two such lifts \( {F}_{1},{F}_{2} \) . Each lift is injective because \( \widehat{\pi } \circ  {F}_{i} = F \) , which is injective, and their images are disjoint because if two lifts agree at a point, they must be identical. From this it is straightforward to verify that the lifted curved triangles form a triangulation of \( \widehat{M} \) with twice as many vertices, edges, and faces as that of \( M \) , and thus \( \chi \left( \widehat{M}\right)  = {2\chi }\left( M\right) \) . Substituting these relations into the Gauss-Bonnet theorem for \( M \) and dividing through by 2, we obtain the analogous relation for \( M \) .

The significance of this theorem cannot be overstated. Together with the classification theorem for compact surfaces, it gives us very detailed information about the possible Gaussian curvatures for metrics on compact surfaces. The classification theorem [LeeTM, Thms. 6.15 and 10.22] says that every compact, connected, ori-entable 2-manifold \( M \) is homeomorphic to a sphere or a connected sum of \( n \) tori, and every nonorientable one is homeomorphic to a connected sum of \( n \) copies of the real projective plane \( {\mathbb{{RP}}}^{2} \) ; the number \( n \) is called the genus of \( \mathbf{M} \) . (The sphere is said to have genus zero.) By constructing simple triangulations, one can show that the Euler characteristic of an orientable surface of genus \( n \) is \( 2 - {2n} \) , and that of a nonorientable one is \( 2 - n \) . The following corollary follows immediately from the Gauss-Bonnet theorem.

Corollary 9.8 Let \( \left( {M, g}\right) \) be a compact Riemannian 2-manifold and let \( K \) be its Gaussian curvature.

(a) If \( M \) is homeomorphic to the sphere or the projective plane, then \( K > 0 \) somewhere.

(b) If \( M \) is homeomorphic to the torus or the Klein bottle, then either \( K \equiv  0 \) or \( K \) takes on both positive and negative values.

(c) If \( M \) is any other compact surface, then \( K < 0 \) somewhere.

This corollary has a remarkable converse, proved in the mid-1970s by Jerry Kaz-dan and Frank Warner: If \( K \) is any smooth function on a compact 2-manifold \( M \) satisfying the necessary sign condition of Corollary 9.8, then there exists a Riemannian metric on \( M \) for which \( K \) is the Gaussian curvature. The proof is a deep application of the theory of nonlinear partial differential equations. (See [Kaz85] for a nice expository account.)

In Corollary 9.8 we assumed we knew the topology of \( M \) and drew conclusions about the possible curvatures it could support. In the following corollary we reverse our point of view, and use assumptions about the curvature to draw conclusions about the topology of the manifold.

Corollary 9.9 Let \( \left( {M, g}\right) \) be a compact Riemannian 2-manifold and \( K \) its Gaussian curvature.

(a) If \( K > 0 \) everywhere on \( M \) , then the universal covering manifold of \( M \) is homeomorphic to \( {\mathbb{S}}^{2} \) , and \( {\pi }_{1}\left( M\right) \) is either trivial or isomorphic to the two-element group \( \mathbb{Z}/2 \) .

(b) If \( K \leq  0 \) everywhere on \( M \) , then the universal covering manifold of \( M \) is homeomorphic to \( {\mathbb{R}}^{2} \) , and \( {\pi }_{1}\left( M\right) \) is infinite.

Proof. Suppose first that \( M \) has positive Gaussian curvature. From the Gauss-Bonnet theorem, \( M \) has positive Euler characteristic. The classification theorem for compact surfaces shows that the only such surfaces are the sphere (with trivial fundamental group) and the projective plane (with fundamental group isomorphic to \( \mathbb{Z}/2 \) ), both of which are covered by the sphere.

On the other hand, suppose \( M \) has nonpositive Gaussian curvature. Then its Euler characteristic is nonpositive, so it is either an orientable surface of genus \( n \geq  1 \) or a nonorientable one of genus \( n \geq  2 \) . Thus the universal covering space of \( M \) is \( {\mathbb{R}}^{2} \) if \( M \) is the torus or the Klein bottle, and \( {\mathbb{B}}^{2} \) in all other cases (see [LeeTM, Thm. 12.29]), both of which are homeomorphic to \( {\mathbb{R}}^{2} \) . The fact that the universal covering space is noncompact implies that the universal covering map has infinitely many sheets by the result of Exercise A.62, and then Proposition A.61 shows that \( {\pi }_{1}\left( M\right) \) is infinite.

Much of the effort in contemporary Riemannian geometry is aimed at generalizing the Gauss-Bonnet theorem and its topological consequences to higher dimensions. As we will see in the next few chapters, most of the interesting results have required the development of different methods.

However, there is one rather direct generalization of the Gauss-Bonnet theorem that deserves mention. For a compact manifold \( M \) of any dimension, the Euler characteristic of \( M \) , denoted by \( \chi \left( M\right) \) , can be defined analogously to that of a surface and is a topological invariant (see [LeeTM, Thm. 13.36]). It turns out that it is always zero for an odd-dimensional compact manifold, but it is a nontrivial invariant in each even-dimensional case.

The Chern-Gauss-Bonnet theorem equates the Euler characteristic of an even-dimensional compact oriented Riemannian manifold to a certain curvature integral. Versions of this theorem were proved by Heinz Hopf in 1925 for an embedded Riemannian hypersurface in Euclidean space, and independently by Carl Allendoerfer and Werner Fenchel in 1940 for an embedded Riemannian submanifold of any Euclidean space (well before Nash's 1956 proof that every Riemannian manifold has such an embedding). Finally, an intrinsic proof for the general case was discovered by Shiing-Shen Chern in 1944 (see [Spi79, Vol. 5] for a complete discussion with references). The theorem asserts that for each \( {2n} \) -dimensional oriented inner product space \( V \) , there exists a basis-independent function

\[
\text{ Pf: }\mathcal{R}\left( {V}^{ * }\right)  \rightarrow  {\Lambda }^{2n}\left( {V}^{ * }\right) \text{ , }
\]

called the Pfaffian, with the property that for every oriented compact Riemannian \( {2n} \) -manifold \( M \) ,

\[
{\int }_{M}\operatorname{Pf}\left( {Rm}\right)  = {\left( 2\pi \right) }^{n}\chi \left( M\right)
\]

(Depending on how the Pfaffian is defined, you will see different choices of normalization constants on the right-hand side of this equation.) For example, in four dimensions, the theorem can be written in terms of familiar curvature quantities as follows:

\[
{\int }_{M}\left( {{\left| Rm\right| }^{2} - 4{\left| Rc\right| }^{2} + {S}^{2}}\right) d{V}_{g} = {32}{\pi }^{2}\chi \left( M\right) . \tag{9.14}
\]

In a certain sense, this might be considered a very satisfactory generalization of Gauss-Bonnet. The only problem with this result is that the relationship between the Pfaffian and sectional curvatures is obscure in higher dimensions, so it is very hard to interpret the theorem geometrically. For example, after he proved the version of the theorem for Euclidean hypersurfaces, Hopf conjectured in the 1930s that every compact even-dimensional manifold that admits a metric with strictly positive sectional curvature must have positive Euler characteristic; to date, the conjecture is known to be true in dimensions 2 and 4, but it is still open in higher dimensions (see [Pet16, p. 320]).

## Problems

9-1. Let \( \left( {M, g}\right) \) be an oriented Riemannian 2-manifold with nonpositive Gaussian curvature everywhere. Prove that there are no geodesic polygons with exactly 0, 1 , or 2 ordinary vertices. Give examples of all three if the curvature hypothesis is not satisfied.

9-2. Let \( \left( {M, g}\right) \) be a Riemannian 2-manifold. If \( \gamma \) is a geodesic polygon in \( M \) with \( n \) vertices, the angle excess of \( \gamma \) is defined as

\[
E\left( \gamma \right)  = \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\theta }_{i}}\right)  - \left( {n - 2}\right) \pi
\]

where \( {\theta }_{1},\ldots ,{\theta }_{n} \) are the interior angles of \( \gamma \) . Show that if \( M \) has constant Gaussian curvature \( K \) , then every geodesic polygon has angle excess equal to \( K \) times the area of the region bounded by the polygon.

9-3. Given \( h \in  \left( {-R, R}\right) \) , let \( {C}_{h} \) be the circle in \( {\mathbb{S}}^{2}\left( R\right)  \subseteq  {\mathbb{R}}^{3} \) where \( z = h \) (where we label the standard coordinates in \( {\mathbb{R}}^{3} \) as \( \left( {x, y, z}\right) \) ), and let \( \Omega \) be the subset of \( {\mathbb{S}}^{2}\left( R\right) \) where \( z > h \) . Compute the signed curvature of \( {C}_{h} \) and verify the Gauss-Bonnet formula in this case.

9-4. Let \( T \subseteq  {\mathbb{R}}^{3} \) be the torus of revolution obtained by revolving the circle \( {\left( r - 2\right) }^{2} + {z}^{2} = 1 \) around the \( z \) -axis (see p. 19). Compute the Gaussian curvature of \( T \) and verify the Gauss-Bonnet theorem in this case.

9-5. This problem outlines a proof that every compact smooth 2-manifold has a smooth triangulation.

(a) Show that it suffices to prove that there exist finitely many convex geodesic polygons whose interiors cover \( M \) , and each of which lies in a uniformly normal convex geodesic ball. (A curved polygon is called convex if the union of the polygon and its interior is a geodesically convex subset of \( M \) .)

(b) Using Theorem 6.17, show that there exist finitely many points \( {v}_{1},\ldots \) , \( {v}_{k} \) and a positive number \( \varepsilon \) such that the geodesic balls \( {B}_{3\varepsilon }\left( {v}_{i}\right) \) are geodesically convex and uniformly normal, and the balls \( {B}_{\varepsilon }\left( {v}_{i}\right) \) cover \( M \) .

(c) For each \( i \) , show that there is a convex geodesic polygon in \( {B}_{3\varepsilon }\left( {v}_{i}\right) \) whose interior contains \( {B}_{\varepsilon }\left( {v}_{i}\right) \) . [Hint: Let the vertices be sufficiently nearby points on the circle of radius \( {2\varepsilon } \) around \( {v}_{i} \) .]

(d) Prove the result.

(Used on p. 276.)

9-6. Let \( M \subseteq  {\mathbb{R}}^{3} \) be a compact, embedded,2-dimensional Riemannian subman-ifold. Show that \( M \) cannot have \( K \leq  0 \) everywhere. [Hint: Look at a point where the distance from the origin takes a maximum.]

9-7. Suppose \( M \) is either the 2-sphere of radius \( R \) or the hyperbolic plane of radius \( R \) for some \( R > 0 \) . Show that similar triangles in \( M \) are congruent. More precisely, if \( {\gamma }_{1} \) and \( {\gamma }_{2} \) are geodesic triangles in \( M \) such that corresponding side lengths are proportional and corresponding interior angles are equal, then there exists an isometry of \( M \) taking \( {\gamma }_{1} \) to \( {\gamma }_{2} \) .

9-8. Use the Gauss-Bonnet theorem to prove that every compact connected Lie group of dimension 2 is isomorphic to the direct product group \( {\mathbb{S}}^{1} \times  {\mathbb{S}}^{1} \) . [Hint: See Problem 8-17.]

9-9. (a) Show that there is an upper bound for the areas of geodesic triangles in the hyperbolic plane \( {\mathbb{H}}^{2}\left( R\right) \) , and compute the least upper bound.

(b) Two distinct maximal geodesics in the hyperbolic plane \( {\mathbb{H}}^{2} \) are said to be asymptotically parallel if they have unit-speed parametrizations \( {\gamma }_{1},{\gamma }_{2} \) : \( \mathbb{R} \rightarrow  {\mathbb{H}}^{2} \) such that \( {d}_{\check{g}}\left( {{\gamma }_{1}\left( t\right) ,{\gamma }_{2}\left( 2\right) }\right) \) remains bounded as \( t \rightarrow   + \infty \) or as \( t \rightarrow   - \infty \) . An ideal triangle in \( {\mathbb{H}}^{2} \) is a region whose boundary consists of three distinct maximal geodesics, any two of which are asymptotically parallel to each other. Show that all ideal triangles have the same finite area, and compute it. Be careful to justify any limits.

9-10. THE GAUSS-BONNET THEOREM FOR SURFACES WITH BOUNDARY: Suppose \( \left( {M, g}\right) \) is a compact Riemannian 2-manifold with boundary, endowed with a smooth triangulation such that the intersection of each curved triangle with \( \partial M \) , if not empty, is either a single vertex or a single edge. Then

\[
{\int }_{M}{KdA} + {\int }_{\partial M}{\kappa }_{N}{ds} = {2\pi \chi }\left( M\right) ,
\]

where \( {\kappa }_{N} \) is the signed geodesic curvature of \( \partial M \) with respect to the inward-pointing normal \( N \) .

9-11. Suppose \( g \) is a Riemannian metric on the cylinder \( {\mathbb{S}}^{1} \times  \left\lbrack  {0,1}\right\rbrack \) such that both boundary curves are totally geodesic. Prove that the Gaussian curvature of \( g \) either is identically zero or attains both positive and negative values. Give examples of both possibilities.

9-12. Prove the plane curve classification theorem (Theorem 1.5). [Hint: Show that every smooth unit-speed plane curve \( \gamma \left( t\right)  = \left( {x\left( t\right) , y\left( t\right) }\right) \) satisfies the second-order ODE \( {\gamma }^{\prime \prime }\left( t\right)  = {\kappa }_{N}\left( t\right) N\left( t\right) \) , where \( N \) is the unit normal vector field given by \( \left. {N\left( t\right)  = \left( {-{y}^{\prime }\left( t\right) ,{x}^{\prime }\left( t\right) }\right) \text{ . }}\right\rbrack \) (Used on p. 4.)

9-13. Use the four-dimensional Chern-Gauss-Bonnet formula (9.14) to prove that a compact 4-dimensional Einstein manifold must have positive Euler characteristic unless it is flat.
