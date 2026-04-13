# Appendix: Classifying 1-Manifolds

We WILL prove the following result, which has been assumed in the text. A brief discussion of the classification problem for higher dimensional manifolds will also be given.

Theorem. Any smooth, connected 1-dimensional manifold is diffeomorphic either to the circle \( {S}^{1} \) or to some interval of real numbers.

(An interval is a connected subset of \( R \) which is not a point. It may be finite or infinite; closed, open, or half-open.)

Since any interval is diffeomorphic* either to \( \left\lbrack  {0,1}\right\rbrack  ,(0,1\rbrack \) , or \( \left( {0,1}\right) \) , it follows that there are only four distinct connected 1-manifolds.

The proof will make use of the concept of "arc-length." Let \( I \) be an interval.

Definition. A map \( f : I \rightarrow  M \) is a parametrization by arc-length if \( f \) maps \( I \) diffeomorphically onto an open subset \( \dagger \) of \( M \) , and if the "velocity vector" \( d{f}_{s}\left( 1\right) {\varepsilon T}{M}_{f\left( s\right) } \) has unit length, for each \( {s\varepsilon I} \) .

Any given local parametrization \( {I}^{\prime } \rightarrow  M \) can be transformed into a parametrization by arc-length by a straightforward change of variables.

Lemma. Let \( f : I \rightarrow  M \) and \( g : J \rightarrow  M \) be parametrizations by arc-length. Then \( f\left( I\right)  \cap  g\left( J\right) \) has at most two components. If it has only one component, then \( f \) can be extended to a parametrization by arc-length of the union \( f\left( I\right)  \cup  g\left( J\right) \) . If it has two components, then \( M \) must be diffeomorphic to \( {S}^{1} \) .

---

* For example, use a diffeomorphism of the form

\[
f\left( t\right)  = a\tanh \left( t\right)  + b.
\]

\( \dagger \) Thus \( I \) can have boundary points only if \( M \) has boundary points.

---

Proof. Clearly \( {g}^{-1} \circ  f \) maps some relatively open subset of \( I \) diffeomor-phically onto a relatively open subset of \( J \) . Furthermore the derivative of \( {g}^{-1} \circ  f \) is equal to \( \pm  1 \) everywhere.

Consider the graph \( \Gamma  \subset  I \times  J \) , consisting of all \( \left( {s, t}\right) \) with \( f\left( s\right)  = g\left( t\right) \) . Then \( \Gamma \) is a closed subset of \( I \times  J \) made up of line segments of slope \( \pm  1 \) . Since \( \Gamma \) is closed and \( {g}^{-1} \circ  f \) is locally a diffeomorphism, these line segments cannot end in the interior of \( I \times  J \) , but must extend to the boundary. Since \( {g}^{-1} \circ  f \) is one-one and single valued, there can be at most one of these segments ending on each of the four edges of the rectangle \( I \times  J \) . Hence \( \Gamma \) has at most two components. (See Figure 19.) Furthermore, if there are two components, the two must have the same slope.

![bo_d7du9valb0pc73deirc0_66_187_905_952_371_0.jpg](images/bo_d7du9valb0pc73deirc0_66_187_905_952_371_0.jpg)

Figure 19. Three of the possibilities for \( \Gamma \)

If \( \Gamma \) is connected, then \( {g}^{-1} \circ  f \) extends to a linear map \( L : R \rightarrow  R \) . Now \( f \) and \( g \circ  L \) piece together to yield the required extension

\[
F : I \cup  {L}^{-1}\left( J\right)  \rightarrow  f\left( I\right)  \cup  g\left( J\right) .
\]

If \( \Gamma \) has two components, with slope say +1, they must be arranged as in the left-hand rectangle of Figure 19. Translating the interval \( J = \left( {\gamma ,\beta }\right) \) if necessary, we may assume that \( \gamma  = c \) and \( \delta  = d \) , so that

\[
a < b \leq  c < d \leq  \alpha  < \beta .
\]

Now setting \( \theta  = {2\pi t}/\left( {\alpha  - a}\right) \) , the required diffeomorphism

\[
h : {S}^{1} \rightarrow  M
\]

is defined by the formula

\[
h\left( {\cos \theta ,\sin \theta }\right)  = f\left( t\right) \;\text{ for }\;a < t < d,
\]

\[
= g\left( t\right) \text{ for }c < t < \beta \text{ . }
\]

The image \( h\left( {S}^{1}\right) \) , being compact and open in \( M \) , must be the entire manifold \( M \) . This proves the lemma.

Proof of CLASSIFICATION THEOREM. Any parametrization by arclength can be extended to one

\[
f : I \rightarrow  M
\]

which is maximal in the sense that \( f \) cannot be extended over any larger interval as a parametrization by arc-length: it is only necessary to extend \( f \) as far as possible to the left and then as far as possible to the right.

If \( M \) is not diffeomorphic to \( {S}^{1} \) , we will prove that \( f \) is onto, and hence is a diffeomorphism. For if the open set \( f\left( I\right) \) were not all of \( M \) , there would be a limit point \( x \) of \( f\left( I\right) \) in \( M - f\left( I\right) \) . Parametrizing a neighborhood of \( x \) by arc-length and applying the lemma, we would see that \( f \) can be extended over a larger interval. This contradicts the assumption that \( f \) is maximal and hence completes the proof.

REMARKS. For manifolds of higher dimension the classification problem becomes quite formidable. For 2-dimensional manifolds, a thorough exposition has been given by Kerékjártó [17]. The study of 3-dimensional manifolds is very much a topic of current research. (See Papakyriakopoulos [26].) For compact manifolds of dimension \( \geq  4 \) the classification problem is actually unsolvable.* But for high dimensional simply connected manifolds there has been much progress in recent years, as exemplified by the work of Smale [31] and Wall [37].

---

* See Markov [19]; and also a forthcoming paper by Boone, Haken, and Poénaru in Fundamenta Mathematicae.

---
