# Chapter 17 The Topology of the Full Path Space

Based on lecture notes by

M. Spivak and R. Wells

Let \( M \) be a Riemannian manifold with Riemann metric \( g \) , and let \( \rho \) be the induced topological metric. Let \( p \) and \( q \) be two (not necessarily distinct) points of \( M \) .

In homotopy theory one studies the space \( {\Omega }^{ * } \) of all continuous paths

\[
\omega  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

from \( p \) to \( q \) , in the compact open topology. This topology can also be described as that induced by the metric

\[
{\mathrm{d}}^{ * }\left( {\omega ,{\omega }^{\prime }}\right)  = \mathop{\max }\limits_{t}\rho \left( {\omega \left( t\right) ,{\omega }^{\prime }\left( t\right) }\right) .
\]

On the other hand we have been studying the space \( \Omega \) of piecewise \( {C}^{\infty } \) paths from \( p \) to \( q \) with the metric

\[
\mathrm{d}\left( {\omega ,{\omega }^{\prime }}\right)  = {\mathrm{d}}^{ * }\left( {\omega ,{\omega }^{\prime }}\right)  + {\left( {\int }_{0}^{1}{\left( \frac{\mathrm{d}s}{\mathrm{\;d}t} - \frac{\mathrm{d}{s}^{\prime }}{\mathrm{d}t}\right) }^{2}\mathrm{\;d}t\right) }^{\frac{1}{2}}.
\]

Since \( \mathrm{d} \geq  {\mathrm{d}}^{ * } \) the natural map

\[
i : \Omega  \rightarrow  {\Omega }^{ * }
\]

is continuous.

Theorem 17.1. This natural map \( i \) is a homotopy equivalence between \( \Omega \) and \( {\Omega }^{ * } \) .

(Added June 1968. The following proof is based on suggestions by W. B. Houston, Jr., who has pointed out that my original proof of Theorem 17.1 was incorrect. The original proof made use of an alleged homotopy inverse \( \Omega  \rightarrow  {\Omega }^{ * } \) which in fact was not even continuous.)

Proof. We will use the fact that every point of \( M \) has an open neighborhood \( N \) which is "geodesically convex" in the sense that any two points of \( N \) are joined by a unique minimal geodesic which lies completely within \( N \) and depends differentiably on the endpoints. (This result is due to J. H. C. Whitehead. See for example [BC01, p. 246]; [Hel62, p. 53]; or [Hic65, p. 134].)

Choose a covering of \( M \) by such geodesically convex open sets \( {N}_{\alpha } \) . Subdividing the interval \( \left\lbrack  {0,1}\right\rbrack \) into \( {2}^{k} \) equal subintervals \( \left\lbrack  {\left( {j - l}\right) /{2}^{k}, j/{2}^{k}}\right\rbrack \) , let \( {\Omega }_{k}^{ * } \) denote the set of all continuous paths \( \omega \) from \( p \) to \( q \) which satisfy the following condition: the image under \( \omega \) of each subinterval \( \left\lbrack  {\left( {j - l}\right) /{2}^{k}, j/{2}^{k}}\right\rbrack \) should be contained in one of the sets \( {N}_{\alpha } \) of the covering.

Clearly each \( {\Omega }_{k}^{ * } \) is an open subset of the space \( {\Omega }^{ * } \) of all paths from \( p \) to \( q \) , and clearly \( {\Omega }^{ * } \) is the union of the sequence

\[
{\Omega }_{1}^{ * } \subset  {\Omega }_{2}^{ * } \subset  {\Omega }_{3}^{ * } \subset  \cdots
\]

Similarly the corresponding sets

\[
{\Omega }_{k} = {i}^{-1}\left( {\Omega }_{k}^{ * }\right)
\]

are open subsets of \( \Omega \) with union equal to \( \Omega \) .

We will first show that the natural map

\[
\left( {\left. i\right| }_{{\Omega }_{k}}\right)  : {\Omega }_{k} \rightarrow  {\Omega }_{k}^{ * }
\]

is a homotopy equivalence. For each \( \omega  \in  {\Omega }_{k}^{ * } \) let \( h\left( \omega \right)  \in  {\Omega }_{k} \) be the broken geodesic which coincides with \( \omega \) for the parameter values \( t = j/{2}^{k}, j = \; 0,1,2,\ldots ,{2}^{k} \) , and which is a minimal geodesic within each intermediate interval \( \left\lbrack  {\left( {j - l}\right) /{2}^{k}, j/{2}^{k}}\right\rbrack \) . This construction defines a function

\[
h : {\Omega }_{k}^{ * } \rightarrow  {\Omega }_{k}
\]

and it is not difficult to verify that \( h \) is continuous.

Just as in the proof of Theorem 16.2 on page 77, it can be verified that the composition \( \left( {\left. i\right| }_{{\Omega }_{k}}\right)  \circ  h \) is homotopic to the identity map of \( {\Omega }_{k}^{ * } \) and that the composition \( h \circ  \left( {\left. i\right| }_{{\Omega }_{k}}\right) \) is homotopic to the identity map of \( {\Omega }_{k} \) . This proves that \( {\left. i\right| }_{{\Omega }_{k}} \) is a homotopy equivalence.

To conclude the proof of Theorem 17.1 we appeal to the Appendix. Using Example A. 2 on page 126 note that the space \( \Omega \) is the homotopy direct limit of the sequence of subsets \( {\Omega }_{k} \) . Similarly note that \( {\Omega }^{ * } \) is the homotopy direct limit of the sequence of subsets \( {\Omega }_{k}^{ * } \) . Therefore, Theorem A. 5 (page 127) shows that \( i : \Omega { \rightarrow  }^{ * } \) is a homotopy equivalence. This completes the proof.

It is known that the space \( {\Omega }^{ * } \) has the homotopy type of a CW-complex. (See Milnor, On spaces having the homotopy type of a CW-complex, Trans. Amer. Math. Soc., Vol. 90 (1959), pp. 272-280.) Therefore

Corollary 17.2. \( \Omega \) has the homotopy type of a CW-complex.

This statement can be sharpened as follows.

Theorem 17.3 (Fundamental theorem of Morse Theory). Let \( M \) be a complete Riemannian manifold, and let \( p, q \in  M \) be two points which are not conjugate along any geodesic. Then \( \Omega \left( {M;p, q}\right) \) (or \( {\Omega }^{ * }\left( {M;p, q}\right) \) ) has the homotopy type of a countable CW-complex which contains one cell of dimension \( \lambda \) for each geodesic from \( p \) to \( q \) of index \( \lambda \) .

Proof. The proof is analogous to that of Theorem 3.3. Choose a sequence \( {a}_{0} < \; {a}_{1} < {a}_{2} < \cdots \) of real numbers which are not critical values of the energy function \( E \) , so that each interval \( \left( {{a}_{i - 1},{a}_{i}}\right) \) contains precisely one critical value. Consider the sequence

\[
{\Omega }^{{a}_{0}} \subset  {\Omega }^{{a}_{1}} \subset  {\Omega }^{{a}_{2}} \subset  \ldots ;
\]

where we may assume that \( {\Omega }^{{a}_{0}} \) is vacuous. It follows from Theorem 16.2 together with Chapter 3 and Lemma 3.5 that each \( {\Omega }^{{a}_{i}} \) has the homotopy type of \( {\Omega }^{{a}_{i - 1}} \) with a finite number of cells attached: one \( \lambda \) -cell for each geodesic of index \( \lambda \) in \( {E}^{-1}\left( {{a}_{i - 1},{a}_{i}}\right) \) . Now, just as in the proof of Theorem 3.3, one constructs a sequence \( {K}_{0} \subset  {K}_{1} \subset  {K}_{2} \subset  \ldots \) of CW-complexes with cells of the required description, and a sequence

![bo_d7du90alb0pc73deir8g_91_596_541_392_159_0.jpg](images/bo_d7du90alb0pc73deir8g_91_596_541_392_159_0.jpg)

of homotopy equivalences. Letting \( f : \Omega  \rightarrow  K \) be the direct limit mapping, it is clear that \( f \) induces isomorphisms of homotopy groups in all dimensions. Since \( \Omega \) is known to have the homotopy type of a OW-complex (Corollary 17.2) it follows from Whitehead’s theorem that \( f \) is a homotopy equivalence. This completes the proof. (For a different proof, not using Corollary 17.2, see p. 149.)

Example 17.4(The path space of the sphere \( {\mathbb{S}}^{n} \) ). Suppose that \( p \) and \( q \) are two non-conjugate points on \( {\mathbb{S}}^{n} \) . That is, suppose that \( q \neq  p,{p}^{\prime } \) where \( {p}^{\prime } \) denotes the antipode of \( p \) . Then there are denumerably many geodesics \( {\gamma }_{0},{\gamma }_{1},{\gamma }_{2},\ldots \) from \( p \) to \( q \) , as follows. Let \( {\gamma }_{0} \) denote the short great circle arc from \( p \) to \( q \) ; let \( {\gamma }_{1} \) denote the long great circle are \( p{q}^{\prime }{p}^{\prime }q \) ; let \( {\gamma }_{2} \) denote the arc \( {pq}{p}^{\prime }{q}^{\prime }{pq} \) ; and so on. The subscript \( k \) denotes the number of times that \( p \) or \( {p}^{\prime } \) occurs in the interior of \( {\gamma }_{k} \) .

![bo_d7du90alb0pc73deir8g_91_504_1247_575_577_0.jpg](images/bo_d7du90alb0pc73deir8g_91_504_1247_575_577_0.jpg)

The index \( \lambda \left( {\gamma }_{k}\right)  = \mu {1}_{ + }\ldots  + {\mu }_{k} \) is equal to \( k\left( {n - 1}\right) \) , since each of the points \( p \) or \( {p}^{\prime } \) in the interior is conjugate to \( p \) with multiplicity \( n - 1 \) .

Therefore we have:

Corollary 17.5. The loop space \( \Omega \left( {\mathbb{S}}^{n}\right) \) has the homotopy type of a CW-complex with one cell each in the dimensions \( 0, n - 1,2\left( {n - 1}\right) ,3\left( {n - 1}\right) ,\ldots \) .

For \( n > 2 \) the homology of \( \Omega \left( {\mathbb{S}}^{n}\right) \) can be computed immediately from this information. Since \( \Omega \left( {\mathbb{S}}^{n}\right) \) has non-trivial homology in infinitely many dimensions, we can conclude:

Corollary 17.6. Let \( M \) have the homotopy type of \( \Omega \left( {\mathbb{S}}^{n}\right) \) , for \( n > 2 \) . Then any two non-conjugate points of \( M \) are joined by infinitely many geodesics.

This follows since the homotopy type of \( {\Omega }^{ * }\left( M\right) \) (and hence of \( \Omega \left( M\right) \) ) depends only on the homotopy type of \( M \) . There must be at least one geodesic in \( \Omega \left( M\right) \) with index 0, at least one with index \( n - 1,2\left( {n - 1}\right) ,3\left( {n - 1}\right) \) , and so on.

Remark. More generally if \( M \) is any complete manifold which is not contractible then any two non-conjugate points of \( M \) are joined by infinitely many geodesics. Compare [Ser51, p. 484].

As another application of Corollary 17.5, one can give a proof of the Freudenthal suspension theorem. (Compare Corollary 22.3.)
