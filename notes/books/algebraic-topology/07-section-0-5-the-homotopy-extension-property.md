# 0.5 The Homotopy Extension Property

In this final section of the chapter we will actually prove a few things, including the two criteria for homotopy equivalence described above. The proofs depend upon a technical property that arises in many other contexts as well. Consider the following problem. Suppose one is given a map \( {f}_{0} : X \rightarrow  Y \) , and on a subspace \( A \subset  X \) one is also given a homotopy \( {f}_{t} : A \rightarrow  Y \) of \( {f}_{0} \mid  A \) that one would like to extend to a homotopy \( {f}_{t} : X \rightarrow  Y \) of the given \( {f}_{0} \) . If the pair \( \left( {X, A}\right) \) is such that this extension problem can always be solved, one says that \( \left( {X, A}\right) \) has the homotopy extension property. Thus \( \left( {X, A}\right) \) has the homotopy extension property if every pair of maps \( X \times  \{ 0\}  \rightarrow  Y \) and \( A \times  I \rightarrow  Y \) that agree on \( A \times  \{ 0\} \) can be extended to a map \( X \times  I \rightarrow  Y \) .

A pair \( \left( {X, A}\right) \) has the homotopy extension property if and only if \( X \times  \{ 0\}  \cup  A \times  I \) is a retract of \( X \times  I \) .

For one implication, the homotopy extension property for \( \left( {X, A}\right) \) implies that the identity map \( X \times  \{ 0\}  \cup  A \times  I \rightarrow  X \times  \{ 0\}  \cup  A \times  I \) extends to a map \( X \times  I \rightarrow  X \times  \{ 0\}  \cup  A \times  I \) , so \( X \times  \{ 0\}  \cup  A \times  I \) is a retract of \( X \times  I \) . The converse is equally easy when \( A \) is closed in \( X \) . Then any two maps \( X \times  \{ 0\}  \rightarrow  Y \) and \( A \times  I \rightarrow  Y \) that agree on \( A \times  \{ 0\} \) combine to give a map \( X \times  \{ 0\}  \cup  A \times  I \rightarrow  Y \) which is continuous since it is continuous on the closed sets \( X \times  \{ 0\} \) and \( A \times  I \) . By composing this map \( X \times  \{ 0\}  \cup  A \times  I \rightarrow  Y \) with a retraction \( X \times  I \rightarrow  X \times  \{ 0\}  \cup  A \times  I \) we get an extension \( X \times  I \rightarrow  Y \) , so \( \left( {X, A}\right) \) has the homotopy extension property. The hypothesis that \( A \) is closed can be avoided by a more complicated argument given in the Appendix. If \( X \times  \{ 0\}  \cup  A \times  I \) is a retract of \( X \times  I \) and \( X \) is Hausdorff, then \( A \) must in fact be closed in \( X \) . For if \( r : X \times  I \rightarrow  X \times  I \) is a retraction onto \( X \times  \{ 0\}  \cup  A \times  I \) , then the image of \( r \) is the set of points \( z \in  X \times  I \) with \( r\left( z\right)  = z \) , a closed set if \( X \) is Hausdorff, so \( X \times  \{ 0\}  \cup  A \times  I \) is closed in \( X \times  I \) and hence \( A \) is closed in \( X \) .

A simple example of a pair \( \left( {X, A}\right) \) with \( A \) closed for which the homotopy extension property fails is the pair \( \left( {I, A}\right) \) where \( A = \left\{  {0,1,1/2,1/3,1/4,\cdots }\right\} \) . It is not hard to show that there is no continuous retraction \( I \times  I \rightarrow  I \times  \{ 0\}  \cup  A \times  I \) . The breakdown of homotopy extension here can be attributed to the bad structure of \( \left( {X, A}\right) \) near 0 . With nicer local structure the homotopy extension property does hold, as the next example shows.

Example 0.15. A pair \( \left( {X, A}\right) \) has the homotopy extension property if \( A \) has a mapping cylinder neighborhood in \( X \) , by which we mean a closed neighborhood \( N \) containing a subspace \( B \) , thought of as the boundary of \( N \) , with \( N - B \) an open neighborhood of \( A \) , such that there exists a map \( f : B \rightarrow  A \) and a homeomorphism \( h : {M}_{f} \rightarrow  N \) with \( h \mid  A \cup  B = \mathbb{1} \) . Mapping cylinder neighborhoods like this occur fairly often. For example, the thick letters discussed at the beginning of the chapter provide such neighborhoods of the thin letters, regarded as subspaces of the plane. To verify the homotopy extension property, notice first that \( I \times  I \) retracts onto \( I \times  \{ 0\}  \cup  \partial I \times  I \) , hence \( B \times  I \times  I \) retracts onto \( B \times  I \times  \{ 0\}  \cup  B \times  \partial I \times  I \) , and this retraction induces a retraction of \( {M}_{f} \times  I \) onto \( {M}_{f} \times  \{ 0\}  \cup  \left( {A \cup  B}\right)  \times  I \) . Thus \( \left( {{M}_{f}, A \cup  B}\right) \) has the homotopy extension property. Hence so does the homeomorphic pair \( \left( {N, A \cup  B}\right) \) . Now given a map \( X \rightarrow  Y \) and a homotopy of its restriction to \( A \) , we can take the constant homotopy on \( X - \left( {N - B}\right) \) and then extend over \( N \) by applying the homotopy extension property for \( \left( {N, A \cup  B}\right) \) to the given homotopy on \( A \) and the constant homotopy on \( B \) .

![bo_d7dtv0s91nqc73eq8nv0_23_1217_375_373_350_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_23_1217_375_373_350_0.jpg)

Proposition 0.16. If \( \left( {X, A}\right) \) is a \( {CW} \) pair, then \( X \times  \{ 0\}  \cup  A \times  I \) is a deformation retract of \( X \times  I \) , hence \( \left( {X, A}\right) \) has the homotopy extension property.

Proof: There is a retraction \( r : {D}^{n} \times  I \rightarrow  {D}^{n} \times  \{ 0\}  \cup  \partial {D}^{n} \times  I \) , for example the radial projection from the point \( \left( {0,2}\right)  \in  {D}^{n} \times  \mathbb{R} \) . Then setting \( {r}_{t} = {tr} + \left( {1 - t}\right) \mathbb{1} \) gives a deformation retraction of \( {D}^{n} \times  I \) onto \( {D}^{n} \times  \{ 0\}  \cup  \partial {D}^{n} \times  I \) . This deformation retraction gives rise to a deformation retraction of \( {X}^{n} \times  I \) onto \( {X}^{n} \times  \{ 0\}  \cup  \left( {{X}^{n - 1} \cup  {A}^{n}}\right)  \times  I \) since \( {X}^{n} \times  I \) is obtained from \( {X}^{n} \times  \{ 0\}  \cup  \left( {{X}^{n - 1} \cup  {A}^{n}}\right)  \times  I \) by attaching copies of \( {D}^{n} \times  I \) along \( {D}^{n} \times  \{ 0\}  \cup  \partial {D}^{n} \times  I \) . If we perform the deformation retraction of \( {X}^{n} \times  I \) onto \( {X}^{n} \times  \{ 0\}  \cup  \left( {{X}^{n - 1} \cup  {A}^{n}}\right)  \times  I \) during the \( t \) -interval \( \left\lbrack  {1/{2}^{n + 1},1/{2}^{n}}\right\rbrack \) , this infinite concatenation of homotopies is a deformation retraction of \( X \times  I \) onto \( X \times  \{ 0\}  \cup  A \times  I \) . There is no problem with continuity of this deformation retraction at \( t = 0 \) since it is continuous on \( {X}^{n} \times  I \) , being stationary there during the \( t \) -interval \( \left\lbrack  {0,1/{2}^{n + 1}}\right\rbrack \) , and CW complexes have the weak topology with respect to their skeleta so a map is continuous iff its restriction to each skeleton is continuous.

![bo_d7dtv0s91nqc73eq8nv0_23_1315_1325_274_295_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_23_1315_1325_274_295_0.jpg)

Now we can prove a generalization of the earlier assertion that collapsing a contractible subcomplex is a homotopy equivalence.

Proposition 0.17. If the pair \( \left( {X, A}\right) \) satisfies the homotopy extension property and \( A \) is contractible, then the quotient map \( q : X \rightarrow  X/A \) is a homotopy equivalence.

Proof: Let \( {f}_{t} : X \rightarrow  X \) be a homotopy extending a contraction of \( A \) , with \( {f}_{0} = \mathbb{1} \) . Since \( {f}_{t}\left( A\right)  \subset  A \) for all \( t \) , the composition \( q{f}_{t} : X \rightarrow  X/A \) sends \( A \) to a point and hence factors as a composition \( X\overset{q}{ \rightarrow  }X/A \rightarrow  X/A \) . Denoting the latter map by \( {\bar{f}}_{t} : X/A \rightarrow  X/A \) , we have \( q{f}_{t} = {\bar{f}}_{t}q \) in the first of the two diagrams at the right. When \( t = 1 \) we have \( {f}_{1}\left( A\right) \) equal to a point, the point to which \( A \) contracts, so \( {f}_{1} \) induces a map \( g : X/A \rightarrow  X \) with \( {gq} = {f}_{1} \) , as in the second diagram. It follows that \( {qg} = {\bar{f}}_{1} \) since \( {qg}\left( \bar{x}\right)  = {qgq}\left( x\right)  = q{f}_{1}\left( x\right)  = {\bar{f}}_{1}q\left( x\right)  = {\bar{f}}_{1}\left( \bar{x}\right) \) . The maps \( g \) and \( q \) are inverse homotopy equivalences since \( {gq} = {f}_{1} \simeq  {f}_{0} = \mathbb{1} \) via \( {f}_{t} \) and \( {qg} = {\bar{f}}_{1} \simeq  {\bar{f}}_{0} = \mathbb{1} \) via \( {\bar{f}}_{t} \) .

![bo_d7dtv0s91nqc73eq8nv0_24_985_310_605_246_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_24_985_310_605_246_0.jpg)

Another application of the homotopy extension property, giving a slightly more refined version of one of our earlier criteria for homotopy equivalence, is the following:

Proposition 0.18. If \( \left( {{X}_{1}, A}\right) \) is a CW pair and we have attaching maps \( f, g : A \rightarrow  {X}_{0} \) that are homotopic, then \( {X}_{0}{ \sqcup  }_{f}{X}_{1} \simeq  {X}_{0}{ \sqcup  }_{g}{X}_{1} \) rel \( {X}_{0} \) .

Here the definition of \( W \simeq  Z \) rel \( Y \) for pairs \( \left( {W, Y}\right) \) and \( \left( {Z, Y}\right) \) is that there are maps \( \varphi  : W \rightarrow  Z \) and \( \psi  : Z \rightarrow  W \) restricting to the identity on \( Y \) , such that \( {\psi \varphi } \simeq  \mathbb{1} \) and \( {\varphi \psi } \simeq  \mathbb{1} \) via homotopies that restrict to the identity on \( Y \) at all times.

Proof: If \( F : A \times  I \rightarrow  {X}_{0} \) is a homotopy from \( f \) to \( g \) , consider the space \( {X}_{0}{ \sqcup  }_{F}\left( {{X}_{1} \times  I}\right) \) . This contains both \( {X}_{0}{ \sqcup  }_{f}{X}_{1} \) and \( {X}_{0}{ \sqcup  }_{g}{X}_{1} \) as subspaces. A deformation retraction of \( {X}_{1} \times  I \) onto \( {X}_{1} \times  \{ 0\}  \cup  A \times  I \) as in Proposition 0.16 induces a deformation retraction of \( {X}_{0}{ \sqcup  }_{F}\left( {{X}_{1} \times  I}\right) \) onto \( {X}_{0}{ \sqcup  }_{f}{X}_{1} \) . Similarly \( {X}_{0}{ \sqcup  }_{F}\left( {{X}_{1} \times  I}\right) \) deformation retracts onto \( {X}_{0}{ \sqcup  }_{g}{X}_{1} \) . Both these deformation retractions restrict to the identity on \( {X}_{0} \) , so together they give a homotopy equivalence \( {X}_{0}{ \sqcup  }_{f}{X}_{1} \simeq  {X}_{0}{ \sqcup  }_{g}{X}_{1} \) rel \( {X}_{0} \) .

We finish this chapter with a technical result whose proof will involve several applications of the homotopy extension property:

Proposition 0.19. Suppose \( \left( {X, A}\right) \) and \( \left( {Y, A}\right) \) satisfy the homotopy extension property, and \( f : X \rightarrow  Y \) is a homotopy equivalence with \( f \mid  A = \mathbb{1} \) . Then \( f \) is a homotopy equivalence rel \( A \) .

Corollary 0.20. If \( \left( {X, A}\right) \) satisfies the homotopy extension property and the inclusion \( A \hookrightarrow  X \) is a homotopy equivalence, then \( A \) is a deformation retract of \( X \) .

Proof: Apply the proposition to the inclusion \( A \hookrightarrow  X \) .

Corollary 0.21. A map \( f : X \rightarrow  Y \) is a homotopy equivalence iff \( X \) is a deformation retract of the mapping cylinder \( {M}_{f} \) . Hence, two spaces \( X \) and \( Y \) are homotopy equivalent iff there is a third space containing both \( X \) and \( Y \) as deformation retracts.

Proof: In the diagram at the right the maps \( i \) and \( j \) are the inclusions and \( r \) is the canonical retraction, so \( f = {ri} \) and \( i \simeq  {jf} \) . Since \( j \) and \( r \) are homotopy equivalences, it follows that \( f \) is a homotopy equivalence iff \( i \) is a homotopy equivalence, since the composition of two homotopy equivalences is a homotopy equivalence and a map homotopic to a homotopy equivalence is a homotopy equivalence. Now apply the preceding corollary to the pair \( \left( {{M}_{f}, X}\right) \) , which satisfies the homotopy extension property by Example 0.15 using the neighborhood \( X \times  \left\lbrack  {0,1/2}\right\rbrack \) of \( X \) in \( {M}_{f} \) .

![bo_d7dtv0s91nqc73eq8nv0_25_1357_155_235_191_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_25_1357_155_235_191_0.jpg)

Proof of 0.19: Let \( g : Y \rightarrow  X \) be a homotopy inverse for \( f \) . There will be three steps to the proof:

(1) Construct a homotopy from \( g \) to a map \( {g}_{1} \) with \( {g}_{1} \mid  A = \mathbb{1} \) .

(2) Show \( {g}_{1}f \simeq  \mathbb{1} \) rel \( A \) .

(3) Show \( f{g}_{1} \simeq  \mathbb{1} \) rel \( A \) .

(1) Let \( {h}_{t} : X \rightarrow  X \) be a homotopy from \( {gf} = {h}_{0} \) to \( \mathbb{1} = {h}_{1} \) . Since \( f \mid  A = \mathbb{1} \) , we can view \( {h}_{t} \mid  A \) as a homotopy from \( g \mid  A \) to1. Then since we assume \( \left( {Y, A}\right) \) has the homotopy extension property, we can extend this homotopy to a homotopy \( {g}_{t} : Y \rightarrow  X \) from \( g = {g}_{0} \) to a map \( {g}_{1} \) with \( {g}_{1} \mid  A = \mathbb{1} \) .

(2) A homotopy from \( {g}_{1}f \) to1is given by the formulas

\[
{k}_{t} = \left\{  \begin{array}{ll} {g}_{1 - {2t}}f, & 0 \leq  t \leq  1/2 \\  {h}_{{2t} - 1}, & 1/2 \leq  t \leq  1 \end{array}\right.
\]

Note that the two definitions agree when \( t = 1/2 \) . Since \( f \mid  A = \mathbb{1} \) and \( {g}_{t} = {h}_{t} \) on \( A \) , the homotopy \( {k}_{t} \mid  A \) starts and ends with the identity, and its second half simply retraces its first half, that is, \( {k}_{t} = {k}_{1 - t} \) on \( A \) . We will define a ’homotopy of homotopies’ \( {k}_{tu} : A \rightarrow  X \) by means of the figure at the right showing the parameter domain \( I \times  I \) for the pairs \( \left( {t, u}\right) \) , with the \( t \) -axis horizontal and the \( u \) -axis vertical. On the bottom edge of the square we define \( {k}_{t0} = {k}_{t} \mid  A \) . Below the ’ \( V \) ’ we define \( {k}_{tu} \) to be independent of \( u \) , and above the ’ \( V \) ’ we define \( {k}_{tu} \) to be independent of \( t \) . This is unambiguous since \( {k}_{t} = {k}_{1 - t} \) on \( A \) . Since \( {k}_{0} = \mathbb{1} \) on \( A \) , we have \( {k}_{tu} = \mathbb{1} \) for \( \left( {t, u}\right) \) in the left, right, and top edges of the square. Next we extend \( {k}_{tu} \) over \( X \) , as follows. Since \( \left( {X, A}\right) \) has the homotopy extension property, so does \( \left( {X \times  I, A \times  I}\right) \) , as one can see from the equivalent retraction property. Viewing \( {k}_{tu} \) as a homotopy of \( {k}_{t} \mid  A \) , we can therefore extend \( {k}_{tu} : A \rightarrow  X \) to \( {k}_{tu} : X \rightarrow  X \) with \( {k}_{t0} = {k}_{t} \) . If we restrict this \( {k}_{tu} \) to the left, top, and right edges of the \( \left( {t, u}\right) \) -square, we get a homotopy \( {g}_{1}f \simeq  \mathbb{1} \) rel \( A \) .

![bo_d7dtv0s91nqc73eq8nv0_25_1283_1440_309_297_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_25_1283_1440_309_297_0.jpg)

(3) Since \( {g}_{1} \simeq  g \) , we have \( f{g}_{1} \simeq  {fg} \simeq  \mathbb{1} \) , so \( f{g}_{1} \simeq  \mathbb{1} \) and steps (1) and (2) can be repeated with the pair \( f, g \) replaced by \( {g}_{1}, f \) . The result is a map \( {f}_{1} : X \rightarrow  Y \) with \( {f}_{1} \mid  A = \mathbb{1} \) and \( {f}_{1}{g}_{1} \simeq  \mathbb{1} \) rel \( A \) . Hence \( {f}_{1} \simeq  {f}_{1}\left( {{g}_{1}f}\right)  = \left( {{f}_{1}{g}_{1}}\right) f \simeq  f \) rel \( A \) . From this we deduce that \( f{g}_{1} \simeq  {f}_{1}{g}_{1} \simeq  \mathbb{1} \) rel \( A \) .

## Exercises

1. Construct an explicit deformation retraction of the torus with one point deleted onto a graph consisting of two circles intersecting in a point, namely, longitude and meridian circles of the torus.

2. Construct an explicit deformation retraction of \( {\mathbb{R}}^{n} - \{ 0\} \) onto \( {S}^{n - 1} \) .

3. (a) Show that the composition of homotopy equivalences \( X \rightarrow  Y \) and \( Y \rightarrow  Z \) is a homotopy equivalence \( X \rightarrow  Z \) . Deduce that homotopy equivalence is an equivalence relation.

(b) Show that the relation of homotopy among maps \( X \rightarrow  Y \) is an equivalence relation.

(c) Show that a map homotopic to a homotopy equivalence is a homotopy equivalence.

4. A deformation retraction in the weak sense of a space \( X \) to a subspace \( A \) is a homotopy \( {f}_{t} : X \rightarrow  X \) such that \( {f}_{0} = \mathbb{1},{f}_{1}\left( X\right)  \subset  A \) , and \( {f}_{t}\left( A\right)  \subset  A \) for all \( t \) . Show that if \( X \) deformation retracts to \( A \) in this weak sense, then the inclusion \( A \hookrightarrow  X \) is a homotopy equivalence.

5. Show that if a space \( X \) deformation retracts to a point \( x \in  X \) , then for each neighborhood \( U \) of \( x \) in \( X \) there exists a neighborhood \( V \subset  U \) of \( x \) such that the inclusion map \( V \hookrightarrow  U \) is nullhomotopic.

6. (a) Let \( X \) be the subspace of \( {\mathbb{R}}^{2} \) consisting of the horizontal segment \( \left\lbrack  {0,1}\right\rbrack   \times  \{ 0\} \) together with all the vertical segments \( \{ r\}  \times  \left\lbrack  {0,1 - r}\right\rbrack \) for \( r \) a rational number in \( \left\lbrack  {0,1}\right\rbrack \) . Show that \( X \) deformation retracts to any point in the segment \( \left\lbrack  {0,1}\right\rbrack   \times  \{ 0\} \) , but not to any other point. [See the preceding problem.]

![bo_d7dtv0s91nqc73eq8nv0_26_1370_1100_213_228_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_26_1370_1100_213_228_0.jpg)

(b) Let \( Y \) be the subspace of \( {\mathbb{R}}^{2} \) that is the union of an infinite number of copies of \( X \) arranged as in the figure below. Show that \( Y \) is contractible but does not deformation retract onto any point.

![bo_d7dtv0s91nqc73eq8nv0_26_262_1527_1331_140_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_26_262_1527_1331_140_0.jpg)

(c) Let \( Z \) be the zigzag subspace of \( Y \) homeomorphic to \( \mathbb{R} \) indicated by the heavier line. Show there is a deformation retraction in the weak sense (see Exercise 4) of \( Y \) onto \( Z \) , but no true deformation retraction.

7. Fill in the details in the following construction from [Edwards 1999] of a compact space \( Y \subset  {\mathbb{R}}^{3} \) with the same properties as the space \( Y \) in Exercise 6, that is, \( Y \) is contractible but does not deformation retract to any point. To begin, let \( X \) be the union of an infinite sequence of cones on the Cantor set arranged end-to-end, as in the figure. Next, form the one-point compactification of \( X \times  \mathbb{R} \) . This embeds in \( {\mathbb{R}}^{3} \) as a closed disk with curved ’fins’ attached along circular arcs, and with the one-point compactification of \( X \) as a cross-sectional slice. The desired space \( Y \) is then obtained from this subspace of \( {\mathbb{R}}^{3} \) by wrapping one more cone on the Cantor set around the boundary of the disk.

![bo_d7dtv0s91nqc73eq8nv0_26_1139_1868_451_353_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_26_1139_1868_451_353_0.jpg)

8. For \( n > 2 \) , construct an \( n \) -room analog of the house with two rooms.

9. Show that a retract of a contractible space is contractible.

10. Show that a space \( X \) is contractible iff every map \( f : X \rightarrow  Y \) , for arbitrary \( Y \) , is nullhomotopic. Similarly, show \( X \) is contractible iff every map \( f : Y \rightarrow  X \) is nullhomo-topic.

11. Show that \( f : X \rightarrow  Y \) is a homotopy equivalence if there exist maps \( g, h : Y \rightarrow  X \) such that \( {fg} \simeq  \mathbb{1} \) and \( {hf} \simeq  \mathbb{1} \) . More generally, show that \( f \) is a homotopy equivalence if \( {fg} \) and \( {hf} \) are homotopy equivalences.

12. Show that a homotopy equivalence \( f : X \rightarrow  Y \) induces a bijection between the set of path-components of \( X \) and the set of path-components of \( Y \) , and that \( f \) restricts to a homotopy equivalence from each path-component of \( X \) to the corresponding path-component of \( Y \) . Prove also the corresponding statements with components instead of path-components. Deduce that if the components of a space \( X \) coincide with its path-components, then the same holds for any space \( Y \) homotopy equivalent to \( X \) .

13. Show that any two deformation retractions \( {r}_{t}^{0} \) and \( {r}_{t}^{1} \) of a space \( X \) onto a subspace \( A \) can be joined by a continuous family of deformation retractions \( {r}_{t}^{s} \) , \( 0 \leq  s \leq  1 \) , of \( X \) onto \( A \) , where continuity means that the map \( X \times  I \times  I \rightarrow  X \) sending \( \left( {x, s, t}\right) \) to \( {r}_{t}^{s}\left( x\right) \) is continuous.

14. Given positive integers \( v, e \) , and \( f \) satisfying \( v - e + f = 2 \) , construct a cell structure on \( {S}^{2} \) having \( v \) 0-cells, \( {e1} \) -cells, and \( {f2} \) -cells.

15. Enumerate all the subcomplexes of \( {S}^{\infty } \) , with the cell structure on \( {S}^{\infty } \) that has \( {S}^{n} \) as its \( n \) -skeleton.

16. Show that \( {S}^{\infty } \) is contractible.

17. (a) Show that the mapping cylinder of every map \( f : {S}^{1} \rightarrow  {S}^{1} \) is a CW complex.

(b) Construct a 2-dimensional CW complex that contains both an annulus \( {S}^{1} \times  I \) and a Möbius band as deformation retracts.

18. Show that \( {S}^{1} * {S}^{1} = {S}^{3} \) , and more generally \( {S}^{m} * {S}^{n} = {S}^{m + n + 1} \) .

19. Show that the space obtained from \( {S}^{2} \) by attaching \( n \) 2-cells along any collection of \( n \) circles in \( {S}^{2} \) is homotopy equivalent to the wedge sum of \( n + 1 \) 2-spheres.

20. Show that the subspace \( X \subset  {\mathbb{R}}^{3} \) formed by a Klein bottle intersecting itself in a circle, as shown in the figure, is homotopy equivalent to \( {S}^{1} \vee  {S}^{1} \vee  {S}^{2} \) .

![bo_d7dtv0s91nqc73eq8nv0_27_1299_1936_287_180_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_27_1299_1936_287_180_0.jpg)

21. If \( X \) is a connected Hausdorff space that is a union of a finite number of 2-spheres, any two of which intersect in at most one point, show that \( X \) is homotopy equivalent to a wedge sum of \( {S}^{1} \) ’s and \( {S}^{2} \) ’s.

22. Let \( X \) be a finite graph lying in a half-plane \( P \subset  {\mathbb{R}}^{3} \) and intersecting the edge of \( P \) in a subset of the vertices of \( X \) . Describe the homotopy type of the ’surface of revolution’ obtained by rotating \( X \) about the edge line of \( P \) .

23. Show that a CW complex is contractible if it is the union of two contractible subcomplexes whose intersection is also contractible.

24. Let \( X \) and \( Y \) be CW complexes with 0-cells \( {x}_{0} \) and \( {y}_{0} \) . Show that the quotient spaces \( X * Y/\left( {X * \left\{  {y}_{0}\right\}   \cup  \left\{  {x}_{0}\right\}   * Y}\right) \) and \( S\left( {X \land  Y}\right) /S\left( {\left\{  {x}_{0}\right\}   \land  \left\{  {y}_{0}\right\}  }\right) \) are homeomorphic, and deduce that \( X * Y \simeq  S\left( {X \land  Y}\right) \) .

25. If \( X \) is a CW complex with components \( {X}_{\alpha } \) , show that the suspension \( {SX} \) is homotopy equivalent to \( Y\mathop{\bigvee }\limits_{\alpha }S{X}_{\alpha } \) for some graph \( Y \) . In the case that \( X \) is a finite graph, show that \( {SX} \) is homotopy equivalent to a wedge sum of circles and 2-spheres.

26. Use Corollary 0.20 to show that if \( \left( {X, A}\right) \) has the homotopy extension property, then \( X \times  I \) deformation retracts to \( X \times  \{ 0\}  \cup  A \times  I \) . Deduce from this that Proposition 0.18 holds more generally for any pair \( \left( {{X}_{1}, A}\right) \) satisfying the homotopy extension property.

27. Given a pair \( \left( {X, A}\right) \) and a homotopy equivalence \( f : A \rightarrow  B \) , show that the natural map \( X \rightarrow  B{ \sqcup  }_{f}X \) is a homotopy equivalence if \( \left( {X, A}\right) \) satisfies the homotopy extension property. [Hint: Consider \( X \cup  {M}_{f} \) and use the preceding problem.] An interesting case is when \( f \) is a quotient map, hence the map \( X \rightarrow  B{ \sqcup  }_{f}X \) is the quotient map identifying each set \( {f}^{-1}\left( b\right) \) to a point. When \( B \) is a point this gives another proof of Proposition 0.17.

28. Show that if \( \left( {{X}_{1}, A}\right) \) satisfies the homotopy extension property, then so does every pair \( \left( {{X}_{0}{ \sqcup  }_{f}{X}_{1},{X}_{0}}\right) \) obtained by attaching \( {X}_{1} \) to a space \( {X}_{0} \) via a map \( f : A \rightarrow  {X}_{0} \) .

29. In case the CW complex \( X \) is obtained from a subcomplex \( A \) by attaching a single cell \( {e}^{n} \) , describe exactly what the extension of a homotopy \( {f}_{t} : A \rightarrow  Y \) to \( X \) given by the proof of Proposition 0.16 looks like. That is, for a point \( x \in  {e}^{n} \) , describe the path \( {f}_{t}\left( x\right) \) for the extended \( {f}_{t} \) .

Chapter 1
