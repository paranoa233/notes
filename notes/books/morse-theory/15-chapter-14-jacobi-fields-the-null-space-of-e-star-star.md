# Chapter 14 Jacobi Fields: The Null Space of E**

Jacobi Fields: The Null Space of \( {E}_{* * } \)

Based on lecture notes by

M. Spivak and R. Wells

A vector field J along a geodesic \( \gamma \) is called a Jacobi field if it satisfies the Jacobi differential equation

\[
\frac{{\mathrm{D}}^{2}\mathrm{\;J}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( {V,\mathrm{\;J}}\right) V = 0
\]

where \( V = \frac{\mathrm{d}\gamma }{\mathrm{d}t} \) . This is a linear, second order differential equation. (It can be put in a more familiar form by choosing orthonormal parallel vector fields \( {P}_{1},\ldots ,{P}_{n} \) along \( \gamma \) . Then setting \( \mathrm{J}\left( t\right)  = \sum {f}^{i}\left( t\right) {P}_{i}\left( t\right) \) , the equation becomes

\[
\frac{{\mathrm{d}}^{2}{f}^{i}}{\mathrm{\;d}{t}^{2}} + \mathop{\sum }\limits_{{j = 1}}^{n}{a}_{j}^{i}\left( t\right) {f}^{j}\left( t\right)  = 0,\;i = 1,\ldots , n;
\]

where \( {a}_{j}^{i} = \left\langle  {\mathcal{R}\left( {V,{P}_{j}}\right) V,{P}_{i}}\right\rangle \) .) Thus the Jacobi equation has \( {2n} \) linearly independent solutions, each of which can be defined throughout \( \gamma \) . The solutions are all \( {C}^{\infty } \) -differentiable. A given Jacobi field J is completely determined by its initial conditions:

\[
\mathrm{J}\left( 0\right) ,\frac{\mathrm{D}\mathrm{J}}{\mathrm{d}t}\left( 0\right)  \in  T{M}_{\gamma \left( 0\right) }.
\]

Let \( p = \gamma \left( a\right) \) and \( q = \gamma \left( b\right) \) be two points on the geodesic \( \gamma \) , with \( a \neq  b \) .

Definition 14.1. \( p \) and \( q \) are conjugate \( {}^{1} \) along \( \gamma \) if there exists a non-zero Jacobi field \( \mathrm{J} \) along \( \gamma \) which vanishes for \( t = a \) and \( t = b \) . The multiplicity of \( p \) and \( q \) as conjugate points is equal to the dimension of the vector space consisting of all such Jacobi fields.

Now let \( \gamma \) be a geodesic in \( \Omega  = \Omega \left( {M;p, q}\right) \) . Recall that the null space of the Hessian

\[
{E}_{* * } : T{\Omega }_{\gamma } \times  T{\Omega }_{\gamma } \rightarrow  \mathbf{R}
\]

is the vector space consisting of those \( {W}_{1} \in  T{\Omega }_{\gamma } \) such that \( {E}_{* * }\left( {{W}_{1},{W}_{2}}\right)  = 0 \) for all \( {W}_{2} \) . The nullity \( \nu \) of \( {E}_{* * } \) is equal to the dimension of this null space. \( {E}_{* * } \) is degenerate if \( \nu  > 0 \) .

---

\( {}^{1} \) If \( \gamma \) has self-intersections then this definition becomes ambiguous. One should rather say that the parameter values a and \( b \) are conjugate with respect to \( \gamma \) .

---

Theorem 14.2. A vector field \( {W}_{1} \in  T{\Omega }_{\gamma } \) belongs to the null space of \( {E}_{* * } \) if and only if \( {W}_{1} \) is a Jacobi field. Hence \( {E}_{* * } \) is degenerate if and only if the end points \( p \) and \( q \) are conjugate along \( \gamma \) . The nullity of \( {E}_{* * } \) is equal to the multiplicity of \( p \) and \( q \) as conjugate points.

Proof. (Compare the proof of Corollary 12.3.) If J is a Jacobi field which vanishes at \( p \) and \( q \) , then \( \mathrm{J} \) certainly belongs to \( T{\Omega }_{\gamma } \) . The second variation formula (Theorem 13.1) states that

\[
- \frac{1}{2}{E}_{* * }\left( {\mathrm{\;J},{W}_{2}}\right)  = \mathop{\sum }\limits_{t}\left\langle  {{W}_{2}\left( t\right) ,0}\right\rangle   + {\int }_{0}^{1}\left\langle  {{W}_{2},0}\right\rangle  \mathrm{d}t = 0.
\]

Hence J belongs to the null space.

Conversely, suppose that \( {W}_{1} \) belongs to the null space of \( {E}_{* * } \) . Choose a subdivision \( 0 = {t}_{0} < {t}_{1} < \ldots  < {t}_{k} = 1 \) of \( \left\lbrack  {0,1}\right\rbrack \) so that \( {\left. {W}_{1}\right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is smooth for each \( i \) . Let \( f : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \left\lbrack  {0,1}\right\rbrack \) be a smooth function which vanishes for the parameter values \( {t}_{0},{t}_{1},\ldots ,{t}_{k} \) and is positive otherwise; and let

\[
{W}_{2}\left( t\right)  = f\left( t\right) {\left( \frac{{\mathrm{D}}^{2}{W}_{1}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( V,{W}_{1}\right) V\right) }_{t}.
\]

Then

\[
- \frac{1}{2}{E}_{* * }\left( {{W}_{1},{W}_{2}}\right)  = \sum 0 + {\int }_{0}^{1}f\left( t\right) {\begin{Vmatrix}\frac{{\mathrm{D}}^{2}{W}_{1}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( V,{W}_{1}\right) V\end{Vmatrix}}^{2}\mathrm{\;d}t.
\]

Since this is zero, it follows that \( {\left. {W}_{1}\right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is a Jacobi field for each \( i \) .

Now let \( {W}_{2}^{\prime } \in  T{\Omega }_{\gamma } \) be a field such that \( {W}_{2}^{\prime }\left( {t}_{i}\right)  = {\Delta }_{{t}_{i}}\frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t} \) for \( i = 1,2,\ldots , k - 1 \) . Then

\[
- \frac{1}{2}{E}_{* * }\left( {{W}_{1},{W}_{2}^{\prime }}\right)  = \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}{\begin{Vmatrix}{\Delta }_{{t}_{i}}\frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}\end{Vmatrix}}^{2} + {\int }_{0}^{1}0\mathrm{\;d}t = 0
\]

Hence \( \frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t} \) has no jumps. But a solution \( {W}_{1} \) of the Jacobi equation is completely determined by the vectors \( {W}_{1}\left( {t}_{i}\right) \) and \( \frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}\left( {t}_{i}\right) \) . Thus it follows that the \( k \) Jacobi fields \( {\left. {W}_{1}\right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  }, i = 1,\ldots , k \) , fit together to give a Jacobi field \( {W}_{1} \) which is \( {C}^{\infty } \) -differentiable throughout the entire unit interval. This completes the proof of Theorem 14.2.

It follows that the nullity \( \nu \) of \( {E}_{* * } \) is always finite. For there are only finitely many linearly independent Jacobi fields along \( \gamma \) .

Remark. Actually the nullity \( \nu \) satisfies \( 0 \leq  \nu  < n \) . Since the space of Jacobi fields which vanish for \( t = 0 \) has dimension precisely \( n \) , it is clear that \( \nu  < n \) . We will construct one example of a Jacobi field which vanishes for \( t = 0 \) , but not for \( t = 1 \) . This will imply that \( \nu  < n \) . In fact let \( {\mathrm{J}}_{t} = t{V}_{t} \) where \( V = \frac{\mathrm{d}\gamma }{\mathrm{d}t} \) denotes the velocity vector field. Then

\[
\frac{\mathrm{D}\mathrm{J}}{\mathrm{d}t} = 1 \cdot  V + t\frac{\mathrm{D}V}{\mathrm{\;d}t} = V
\]

(Since \( \frac{\mathrm{D}V}{\mathrm{\;d}t} = 0 \) ), hence \( \frac{{\mathrm{D}}^{2}\mathrm{\;J}}{\mathrm{\;d}{t}^{2}} = 0 \) . Furthermore \( \mathcal{R}\left( {V, J}\right) V = t\mathcal{R}\left( {V, V}\right) V = 0 \) since

\( \mathcal{R} \) is skew symmetric in the first two variables. Thus J satisfies the Jacobi equation. Since \( {\mathrm{J}}_{0} = 0,{\mathrm{\;J}}_{1} \neq  0 \) , this completes the proof.

Example 14.3. Suppose that \( M \) is "flat" in the sense that the curvature tensor is identically zero. Then the Jacobi equation becomes \( \frac{{\mathrm{D}}^{2}\mathrm{\;J}}{\mathrm{d}{t}^{2}} = 0 \) . Setting \( \mathrm{J}\left( t\right)  = \; \sum {f}^{i}\left( t\right) {P}_{i}\left( t\right) \) where \( {P}_{i} \) are parallel, this becomes \( \frac{{\mathrm{d}}^{2}{f}^{i}}{\mathrm{\;d}{t}^{2}} = 0 \) . Evidently a Jacobi field along \( \gamma \) can have at most one zero. Thus there are no conjugate points, and \( {E}_{* * } \) is non-degenerate.

Example 14.4. Suppose that \( p \) and \( q \) are antipodal points on the unit sphere \( {\mathbb{S}}^{n} \) , and let \( \gamma \) be a great circle arc from \( p \) to \( q \) . Then we will see that \( p \) and \( q \) are conjugate with multiplicity \( n - 1 \) . Thus in this example the nullity \( \nu \) of \( {E}_{* * } \) takes its largest possible value. The proof will depend on the following discussion.

Let \( \alpha \) be a 1-parameter variation of \( \gamma \) , not necessarily keeping the endpoints fixed, such that each \( \overline{\alpha }\left( u\right) \) is a geodesic. That is, let

\[
\alpha  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

be a \( {C}^{\infty } \) map such that \( \alpha \left( {0, t}\right)  = \gamma \left( t\right) \) , and such that each \( \overline{\alpha }\left( u\right) \) (given by \( \overline{\alpha }\left( u\right) \left( t\right)  = \; \alpha \left( {u, t}\right) ) \) is a geodesic.

Lemma 14.5. If \( \alpha \) is such a variation of \( \gamma \) through geodesics, then the variation vector field \( W\left( t\right)  = \frac{\partial \alpha }{\partial u}\left( {0, t}\right) \) is a Jacobi field along \( \gamma \) .

Proof. If \( \alpha \) is a variation of \( \gamma \) through geodesics, then \( \frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t} \) is identically zero. Hence

\[
0 = \frac{\mathrm{D}}{\mathrm{d}u}\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t} = \frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{D}}{\mathrm{d}u}\frac{\partial \alpha }{\partial t} + \mathcal{R}\left( {\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial u}}\right) \frac{\partial \alpha }{\partial t}
\]

\[
= \frac{{\mathrm{D}}^{2}}{\mathrm{\;d}{t}^{2}}\frac{\partial \alpha }{\partial u} + \mathcal{R}\left( {\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial u}}\right) \frac{\partial \alpha }{\partial t}.
\]

(Compare equation (13.2).) Therefore the variation vector field \( \frac{\partial \alpha }{\partial u} \) is a Jacobi field.

Thus one way of obtaining Jacobi fields is to move geodesics around.

![bo_d7du90alb0pc73deir8g_78_285_1708_1087_448_0.jpg](images/bo_d7du90alb0pc73deir8g_78_285_1708_1087_448_0.jpg)

Now let us return to the example of two antipodal points on a unit \( n \) -sphere. Rotating the sphere, keeping \( p \) and \( q \) fixed, the variation vector field along the geodesic \( \gamma \) will be a Jacobi field vanishing at \( p \) and \( q \) . Rotating in \( n - 1 \) different directions one obtains \( n - 1 \) linearly independent Jacobi fields. Thus \( p \) and \( q \) are conjugate along \( \gamma \) with multiplicity \( n - 1 \) .

![bo_d7du90alb0pc73deir8g_79_554_436_473_484_0.jpg](images/bo_d7du90alb0pc73deir8g_79_554_436_473_484_0.jpg)

Lemma 14.6. Every Jacobi field along a geodesic \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) may be obtained by a variation of \( \gamma \) through geodesics.

Proof. Choose a neighborhood \( U \) of \( \gamma \left( 0\right) \) so that any two points of \( U \) are joined by a unique minimal geodesic which depends differentiably on the endpoints. Suppose that \( \gamma \left( t\right)  \in  U \) for \( 0 \leq  t \leq  \delta \) . We will first construct a Jacobi field \( W \) along \( {\left. \gamma \right| }_{\left\lbrack  0,\delta \right\rbrack  } \) with arbitrarily prescribed values at \( t = 0 \) and \( t = \delta \) . Choose a curve \( a : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  U \) so that \( a\left( 0\right)  = \gamma \left( 0\right) \) and so that \( \frac{\mathrm{d}a}{\mathrm{\;d}u}\left( 0\right) \) is any prescribed vector in \( T{M}_{\gamma \left( 0\right) } \) . Similarly choose \( b : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  U \) with \( b\left( 0\right)  = \gamma \left( \delta \right) \) and \( \frac{\mathrm{d}b}{\mathrm{\;d}u}\left( 0\right) \) arbitrary. Now define the variation

\[
\alpha  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0,\delta }\right\rbrack   \rightarrow  M
\]

by letting \( \overline{\alpha }\left( u\right)  : \left\lbrack  {0,\delta }\right\rbrack   \rightarrow  M \) be the unique minimal geodesic from \( a\left( u\right) \) to \( b\left( u\right) \) . Then the formula \( t \mapsto  \frac{\partial \alpha }{\partial u}\left( {0, t}\right) \) defines a Jacobi field with the given end conditions.

Any Jacobi field along \( {\left. \gamma \right| }_{\left\lbrack  0,\delta \right\rbrack  } \) can be obtained in this way: If \( \mathfrak{J}\left( \gamma \right) \) denotes the vector space of all Jacobi fields \( W \) along \( \gamma \) , then the formula \( W \mapsto  \left( {W\left( 0\right) , W\left( \delta \right) }\right) \) defines a linear map

\[
\ell  : \mathfrak{J}\left( \gamma \right)  \rightarrow  T{M}_{\gamma \left( 0\right) } \times  T{M}_{\gamma \left( 0\right) }
\]

We have just shown that \( \ell \) is onto. Since both vector spaces have the same dimension \( {2n} \) it follows that \( \ell \) is an isomorphism. I.e., a Jacobi field is determined by its values at \( \gamma \left( 0\right) \) and \( \gamma \left( \delta \right) \) . (More generally a Jacobi field is determined by its values at any two non-conjugate points.) Therefore the above construction yields all possible Jacobi fields along \( {\left. \gamma \right| }_{\left\lbrack  0,\delta \right\rbrack  } \) .

The restriction of \( \overline{\alpha }\left( u\right) \) to the interval \( \left\lbrack  {0,\delta }\right\rbrack \) is not essential. If \( u \) is sufficiently small then, using the compactness of \( \left\lbrack  {0,1}\right\rbrack  ,\overline{\alpha }\left( u\right) \) can be extended to a geodesic defined over the entire unit interval \( \left\lbrack  {0,1}\right\rbrack \) . This yields a variation through geodesics:

\[
{\alpha }^{\prime } : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0,\delta }\right\rbrack   \rightarrow  M
\]

with any given Jacobi field as variation vector.

Remark. This argument shows that in any such neighborhood \( U \) the Jacobi fields along a geodesic segment in \( U \) are uniquely determined by their values at the endpoints of the geodesic.

Remark. The proof shows also, that there is a neighborhood \( \left( {-\delta ,\delta }\right) \) of 0 so that if \( t \in  \left( {-\delta ,\delta }\right) \) then \( \gamma \left( t\right) \) is not conjugate to \( \gamma \left( 0\right) \) along \( \gamma \) . We will see in Corollary 15.2 that the set of conjugate points to \( \gamma \left( 0\right) \) along the entire geodesic \( \gamma \) has no cluster points.
