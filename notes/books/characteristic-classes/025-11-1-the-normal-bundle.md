# 11.1 The Normal Bundle

Let \( M = {M}^{n} \) be a smooth manifold which is smoothly (and topologically) embedded in a Riemannian manifold \( A = {A}^{n + k} \) . In order to study characteristic classes of the normal bundle of \( M \) in \( A \) we will need the following geometrical result.

Theorem 11.1 (Tubular neighborhood theorem). There exists an open neighborhood of \( M \) in \( A \) which is diffeomorphic to the total space of the normal bundle under a diffeomorphism which maps each point \( x \) of \( M \) to the zero normal vector at \( x \) .

Such a neighborhood is called an open tubular neighborhood of \( M \) in \( A \) .

To simplify the presentation, we will carry out full details of the proof only in the special case where \( M \) is compact. This special case will suffice for nearly all of our applications. The proof in the general case is given, for example, in [Lan62].

Let \( E \) denote the total space of the normal bundle \( {\nu }^{k} \) . To any real number \( \varepsilon  > 0 \) , we associate the open subset \( E\left( \varepsilon \right)  \subset  E \) consisting of all pairs \( \left( {x, v}\right)  \in  E \) with \( \left| v\right|  < \varepsilon \) . Here \( x \) denotes a point of \( M \) , and \( v \) a normal vector to \( M \) at \( x \) .

[Or more generally, to any smooth real valued function \( x \mapsto  \varepsilon \left( x\right)  > 0 \) , we can associate the open set \( E\left( \varepsilon \right) \) consisting of all \( \left( {x, v}\right)  \in  E \) with \( \left| v\right|  < \varepsilon \left( x\right) \) . This more general construction is essential in dealing with non-compact manifolds.]

We will make use of the exponential map

\[
\operatorname{Exp} : E\left( \varepsilon \right)  \rightarrow  A
\]

of Riemannian geometry, which assigns to each \( \left( {x, v}\right)  \in  E \) with \( \left| v\right| \) sufficiently small the endpoint \( \gamma \left( 1\right) \) of the parametrized geodesic arc

\[
\gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  A
\]

of length \( \left| v\right| \) having initial point \( \gamma \left( 0\right) \) equal to \( x \) and initial velocity vector \( \mathrm{d}\gamma /{\left. \mathrm{d}t\right| }_{t = 0} \) equal to \( v \) . As an example, if the ambient Riemmannian manifold \( A \) is Euclidean space, then \( \gamma \) is just a straight line segment, and the exponential map is given by the formula \( \operatorname{Exp}\left( {x, v}\right)  = x + v \) .

The usual existence, uniqueness, and smoothness theorems for differential equations imply that \( \operatorname{Exp}\left( {x, v}\right) \) is defined, and smooth as a function of \( \left( {x, v}\right) \) , throughout some neighborhood of the zero cross-section \( M \times  0 \subset \) E. (See for example [BC11].) It follows easily that Exp is defined and smooth on \( E\left( \varepsilon \right) \) for \( \varepsilon \) sufficiently small.

Furthermore, applying the Inverse Function Theorem at any point \( \left( {x,0}\right) \) on the zero cross-section \( M \times  0 \subset  E \) , we see that some open neighborhood of \( \left( {x,0}\right) \) in \( E\left( \varepsilon \right) \) is mapped diffeomorphically onto an open subset of \( A \) .

Assertion. If \( \varepsilon \) is sufficiently small, then the entire open set \( E\left( \varepsilon \right) \) is mapped diffeomorphically onto an open set \( {N}_{\varepsilon } \subset  A \) by the exponential map.

Proof, assuming that \( M \) is compact. Certainly the exponential map restricted to \( E\left( \varepsilon \right) \) is a local diffeomorphism, for small \( \varepsilon \) , so it suffices to prove that it is one-to-one. If this were false, then for each integer \( i > 0 \) , taking \( \varepsilon  = 1/i \) , there would exist two distinct points

\[
\left( {{x}_{i},{v}_{i}}\right)  \neq  \left( {{x}_{i}^{\prime },{v}_{i}^{\prime }}\right)
\]

in the neighborhood \( E\left( {1/i}\right) \) for which

\[
\operatorname{Exp}\left( {{x}_{i},{v}_{i}}\right)  = \operatorname{Exp}\left( {{x}_{i}^{\prime },{v}_{i}^{\prime }}\right) .
\]

Therefore, since \( M \) is compact, there would exist a convergent subsequence \( \left\{  {x}_{{i}_{j}}\right\} \) so that say

\[
\lim \left( {{x}_{{i}_{j}},{v}_{{i}_{j}}}\right)  = \left( {x,0}\right) ,
\]

and simultaneously

\[
\lim \left( {{x}_{{i}_{j}}^{\prime },{v}_{{i}_{j}}^{\prime }}\right)  = \left( {{x}^{\prime },0}\right) .
\]

Evidently the limit point \( x = \operatorname{Exp}\left( {x,0}\right)  = \lim \operatorname{Exp}\left( {{x}_{{i}_{j}},{v}_{{i}_{j}}}\right) \) would be equal to the limit point \( {x}^{\prime } \) . But then the equation \( \operatorname{Exp}\left( {{x}_{{i}_{j}},{v}_{{i}_{j}}}\right)  = \operatorname{Exp}{\left( {x}_{{i}_{j}}\right) }^{\prime },{v}_{{i}_{j}}^{\prime } \) for large \( j \) would contradict the statement that Exp is one-to-one throughout a neighborhood of \( \left( {x,0}\right) \) .

Thus \( E\left( \varepsilon \right) \) is diffeomorphic to its image \( {N}_{\varepsilon } \) for small \( \varepsilon \) . To complete the proof of 11.1, we need only note that \( E\left( \varepsilon \right) \) is also diffeomorphic to \( E \) , under the correspondence

\[
\left( {x, v}\right)  \mapsto  \left( {x,\frac{v}{\sqrt{1 - {\left| v\right| }^{2}/\varepsilon {\left( x\right) }^{2}}}}\right)
\]

Now let us make the additional hypothesis that the submanifold \( M \subset  A \) is closed as a subset of the topological space \( A \) . Of course this hypothesis is automatically satisfied if \( M \) is compact.

Corollary 11.2. If \( M \) is closed in \( A \) , then the cohomology ring \( {\mathrm{H}}^{ * }\left( {E,{E}_{0};\Lambda }\right) \) associated with the normal bundle of \( M \) in \( A \) is canonically isomorphic to the cohomology ring \( {\mathrm{H}}^{ * }\left( {A, A - M;\Lambda }\right) \) .

Here \( \Lambda \) can be any coefficient ring.

Proof. Since the tubular neighborhood \( {N}_{\varepsilon } \) and the complement \( A - M \) are open subsets with union \( A \) and intersection \( {N}_{\varepsilon } - M \) , there is an excision isomorphism

\[
{\mathrm{H}}^{ * }\left( {A, A - M}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {{N}_{\varepsilon },{N}_{\varepsilon } - M}\right) .
\]

(See for example [Spa81].) Therefore the embedding

\[
\operatorname{Exp} : \left( {E\left( \varepsilon \right) , E{\left( \varepsilon \right) }_{0}}\right)  \rightarrow  \left( {{N}_{\varepsilon },{N}_{\varepsilon } - M}\right)  \subset  \left( {A, A - M}\right)
\]

induces an isomorphism

\[
{\operatorname{Exp}}^{ * } : {\mathrm{H}}^{ * }\left( {A, A - M}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {E\left( \varepsilon \right) , E{\left( \varepsilon \right) }_{0}}\right) .
\]

Composing with the excision isomorphism

\[
{\mathrm{H}}^{ * }\left( {E\left( \varepsilon \right) , E{\left( \varepsilon \right) }_{0}}\right)  \cong  {\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right)
\]

we obtain an isomorphism which clearly does not depend on the particular choice of \( \varepsilon \) .

Remark. This isomorphism \( {\mathrm{H}}^{ * }\left( {A, A - M}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right) \) does not even depend on the particular choice of Riemannian metric for \( A \) . To make sense of this statement, one must first choose a definition of "normal bundle" based on the exact sequence

\[
{\left. 0 \rightarrow  {\tau }_{M} \rightarrow  {\tau }_{A}\right| }_{M} \rightarrow  {\nu }^{k} \rightarrow  0
\]

which is independent of the particular Riemannian metric on \( A \) . (Compare 3-B.) Since any two Riemannian metrics \( {\mu }_{0} \) and \( {\mu }_{1} \) can be joined by a smooth one-parameter family of Riemannian metrics \( \left( {1 - t}\right) {\mu }_{0} + t{\mu }_{1} \) , it then follows easily that the corresponding exponential maps are homotopic.

As an application of Corollary 11.2, the fundamental cohomology class \( u \in  {\mathrm{H}}^{k}\left( {E,{E}_{0};\mathbb{Z}/2}\right) \) corresponds to a canonical cohomology class which we denote by the symbol

\[
{u}^{\prime } \in  {\mathrm{H}}^{k}\left( {A, A - M;\mathbb{Z}/2}\right) .
\]

Similarly if the normal bundle \( {\nu }^{k} \) is orientable, then any specific orientation for \( {\nu }^{k} \) determines a corresponding class \( {u}^{\prime } \in  {\mathrm{H}}^{k}\left( {A, A - M;\mathbb{Z}}\right) \) with integer coefficients.

Theorem 11.3. If \( M \) is embedded as a closed subset of \( A \) , then the composition of the two restriction homomorphisms

\[
{\mathrm{H}}^{k}\left( {A, A - M}\right)  \rightarrow  {\mathrm{H}}^{k}\left( A\right)  \rightarrow  {\mathrm{H}}^{k}\left( M\right)
\]

with mod 2 coefficients, maps the fundamental class \( {u}^{\prime } \) to the top Stiefel-Whitney class \( {\mathrm{w}}_{k}\left( {\nu }^{k}\right) \) of the normal bundle. Similarly, if \( {\nu }^{k} \) is oriented, then the corresponding composition with integer coefficients maps the integral fundamental class \( {u}^{\prime } \) to the Euler class \( \mathrm{e}\left( {\nu }^{k}\right) \)

Proof. Let \( s : M \rightarrow  E \) denote the zero cross-section of \( {\nu }^{k} \) , inducing a canonical isomorphism \( {\mathrm{H}}^{ * }\left( E\right)  \rightarrow  {\mathrm{H}}^{ * }\left( M\right) \) . First note that the composition

\[
{\mathrm{H}}^{k}\left( {E,{E}_{0}}\right)  \rightarrow  {\mathrm{H}}^{k}\left( E\right) \overset{{s}^{ * }}{ \rightarrow  }{\mathrm{H}}^{k}\left( M\right)
\]

with \( {\;\operatorname{mod}\;2} \) coefficients maps the fundamental class \( u \) to the Stiefel-Whitney class \( {\mathrm{w}}_{k}\left( {\nu }^{k}\right) \) . (Compare Property 9.5.) In fact the image of \( {s}^{ * }\left( {\left. u\right| }_{E}\right) \) under the Thom isomorphism

\[
\phi  : {\mathrm{H}}^{k}\left( M\right)  \rightarrow  {\mathrm{H}}^{2k}\left( {E,{E}_{0}}\right)
\]

is equal to

\[
{\pi }^{ * }{s}^{ * }\left( {\left. u\right| }_{E}\right)  \smile  u = \left( {\left. u\right| }_{E}\right)  \smile  u = u \smile  u = {\operatorname{Sq}}^{k}\left( u\right) .
\]

Therefore \( s * \left( {\left. u\right| }_{E}\right) \) is equal to \( {\phi }^{-1}{\mathrm{{Sq}}}^{k}\left( u\right)  = {\mathrm{w}}_{k}\left( {\nu }^{k}\right) \) .

Now, replacing \( \left( {E,{E}_{0}}\right) \) by the diffeomorphic pair \( \left( {{N}_{\varepsilon },{N}_{\varepsilon } - M}\right) \) , it follows that the composition of the two restriction homomorphisms

\[
{\mathrm{H}}^{k}\left( {{N}_{\varepsilon },{N}_{\varepsilon } - M}\right)  \rightarrow  {\mathrm{H}}^{k}\left( {N}_{\varepsilon }\right)  \rightarrow  {\mathrm{H}}^{k}\left( M\right)
\]

maps the class corresponding to \( u \) to \( {\mathrm{w}}_{k}\left( {\nu }^{k}\right) \) . Making use of the commutative diagram

![bo_d7du9galb0pc73deir9g_126_540_1194_457_188_0.jpg](images/bo_d7du9galb0pc73deir9g_126_540_1194_457_188_0.jpg)

the conclusion follows. The proof in the oriented case is completely analogous.

Definition. The image of \( {u}^{\prime } \) in \( {\mathrm{H}}^{k}\left( A\right) \) is called the dual cohomology class to the submanifold \( M \) of codimension \( k \) . (Compare Problem 11-C.) If this dual class \( {\left. {u}^{\prime }\right| }_{A} \) is zero, it follows of course that the top Stiefel-Whitney class [or the Euler class] of \( {\nu }^{k} \) must also be zero. One special case is particularly noteworthy:

Corollary 11.4. If \( M = {M}^{n} \) is smoothly embedded as a closed subset of the Euclidean space \( {\mathbb{R}}^{n + k} \) , then \( {\mathrm{w}}_{k}\left( {\nu }^{k}\right)  = 0 \) . In the oriented case \( e\left( {\nu }^{k}\right)  = 0 \) .

For the dual class \( {\left. {u}^{\prime }\right| }_{{\mathbb{R}}^{n + k}} \) belongs to a cohomology group \( {\mathrm{H}}^{k}\left( {\mathbb{R}}^{n + k}\right) \) which is zero.

By the Whitney duality theorem 4.2, the class \( {\mathrm{w}}_{k}\left( {\nu }^{k}\right) \) can be expressed as a characteristic class \( {\overline{\mathrm{w}}}_{k}\left( {\tau }_{M}\right) \) of the tangent bundle of \( M \) . Thus we can restate 11.4 as follows: If \( {\overline{\mathrm{w}}}_{k}\left( {\tau }_{M}\right)  \neq  0 \) , then \( M \) cannot be smoothly embedded as a closed subset of \( {\mathbb{R}}^{n + k} \) .

As an example, if \( n \) is a power of 2, then the real projective space \( {\mathbb{P}}^{n} \) cannot be smoothly embedded in \( {\mathbb{R}}^{{2n} - 1} \) . (Compare 4.8. According to [Whi44], every smooth \( n \) -manifold whose topology has a countable basis can be smoothly embedded in \( {\mathbb{R}}^{2n} \) . Presumably it can be embedded as a closed subset of \( {\mathbb{R}}^{2n} \) , although Whitney does not prove this).

Remark 7. It is essential in 11.4 that \( M \) be a manifold without boundary, embedded as a closed subset of Euclidean space. For example the open Möbius band of Figure 2 can certainly be embedded in \( {\mathbb{R}}^{3} \) . But it cannot be embedded as a closed subset, since the associated Stiefel Whitney class \( {\overline{\mathrm{w}}}_{1}\left( \tau \right) \) is non-zero. Similarly it is essential that \( M \) be embedded (i.e., without self-intersections) rather than simply immersed in \( {\mathbb{R}}^{n + k} \) . For example a theorem of [Boy03] asserts that the real projective plane \( {\mathbb{P}}^{2} \) can be immersed in \( {\mathbb{R}}^{3} \) . (See [HC99].) But again the dual Steifel-Whitney class \( {\overline{\mathrm{w}}}_{1}\left( \tau \right) \) is non-zero.
