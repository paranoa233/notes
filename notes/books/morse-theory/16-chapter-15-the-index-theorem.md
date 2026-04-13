# Chapter 15 The Index Theorem

Based on lecture notes by

M. Spivak and R. Wells

The index \( \lambda \) of the Hessian

\[
{E}_{* * } : T{\Omega }_{\gamma } \times  T{\Omega }_{\gamma } \rightarrow  \mathbf{R}
\]

is defined to be the maximum dimension of a subspace of \( T{\Omega }_{\gamma } \) on which \( {E}_{* * } \) is negative definite. We will prove the following.

Theorem 15.1 (Morse). The index \( \lambda \) of \( {E}_{* * } \) is equal to the number of points \( \gamma \left( t\right) \) , with \( 0 < t < 1 \) , such that \( \gamma \left( t\right) \) is conjugate to \( \gamma \left( 0\right) \) along \( \gamma \) ; each such conjugate point being counted with its multiplicity. This index \( \lambda \) is always finite \( {}^{1} \) .

As an immediate consequence one has:

Corollary 15.2. A geodesic segment \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) can contain only finitely many points which are conjugate to \( \gamma \left( 0\right) \) along \( \gamma \) .

In order to prove Theorem 15.1 we will first make an estimate for \( \lambda \) by splitting the vector space \( T{\Omega }_{\gamma } \) into two mutually orthogonal subspaces, on one of which \( {E}_{* * } \) is positive definite.

Each point \( \gamma \left( t\right) \) is contained in an open set \( U \) such that any two points of \( U \) are joined by a unique minimal geodesic which depends differentiably on the endpoints. (See chapter 10.) Choose a subdivision \( 0 = {t}_{0} < {t}_{1} < \ldots  < {t}_{k} = 1 \) of the unit interval which is sufficiently fine so that each segment \( \gamma \left\lbrack  {{t}_{i - 1},{t}_{i}}\right\rbrack \) lies within such an open set \( U \) ; and so that each \( {\left. \gamma \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is minimal.

Let \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right)  \subset  T{\Omega }_{\gamma } \) be the vector space consisting of all vector fields \( W \) along \( \gamma \) such that

(a) \( {\left. W\right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is a Jacobi field along \( {\left. \gamma \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) for each \( i \) ;

(b) \( W \) vanishes at the endpoints \( t = 0, t = 1 \) .

Thus \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right) \) is a finite dimensional vector space consisting of broken Jacobi fields along \( \gamma \) .

Let \( {T}^{\prime } \subset  T{\Omega }_{\gamma } \) be the vector space consisting of all vector fields \( W \in  T{\Omega }_{\gamma } \) for which \( W\left( {t0}\right)  = 0, W\left( {t}_{1}\right)  = 0, W\left( {t}_{2}\right)  = 0,\ldots , W\left( {t}_{k}\right)  = 0 \) .

---

\( {}^{1} \) For generalization of this result see: [Amb61].

---

Lemma 15.3. The vector space \( T{\Omega }_{\gamma } \) splits as the direct sum \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right)  \oplus \; {T}^{\prime } \) . These two subspaces are mutually perpendicular with respect to the inner product \( {E}_{* * } \) . Furthermore, \( {E}_{* * } \) restricted to \( {T}^{\prime } \) is positive definite.

Proof. Given any vector field \( W \in  T{\Omega }_{\gamma } \) let \( {W}_{1} \) denote the unique "broken Jacobi field" in \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right) \) such that \( {W}_{1}\left( {t}_{i}\right)  = W\left( {t}_{i}\right) \) for \( i = 0,1,\ldots , k \) . It follows from Chapter 14 that \( {W}_{1} \) exists and is unique. Clearly \( W - {W}_{1} \) belongs to \( {T}^{\prime } \) . Thus the two subspaces, \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right) \) and \( {T}^{\prime } \) generate \( T{\Omega }_{\gamma } \) , and have only the zero vector field in common.

If \( {W}_{1} \) belongs to \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{l},{t}_{2},\ldots ,{t}_{k}}\right) \) and \( {W}_{2} \) belongs to \( {T}^{\prime } \) , then the second variation formula (Theorem 13.1) takes the form

\[
\frac{1}{2}{E}_{* * }\left( {{W}_{1},{W}_{2}}\right)  =  - \mathop{\sum }\limits_{t}\left\langle  {{W}_{2}\left( t\right) ,{\Delta }_{t}\frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}}\right\rangle   - {\int }_{0}^{1}\left\langle  {{W}_{2},0}\right\rangle  \mathrm{d}t = 0.
\]

Thus the two subspaces are mutually perpendicular with respect to \( {E}_{* * } \) .

For any \( W \in  T{\Omega }_{\gamma } \) the Hessian \( {E}_{* * }\left( {W, W}\right) \) can be interpreted as the second derivative \( {\mathrm{d}}^{2}E \circ  \overline{\alpha }/\mathrm{d}{u}^{2}\left( 0\right) \) ; where \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) is any variation of \( \gamma \) with variation vector field \( \mathrm{d}\overline{\alpha }/\mathrm{d}t\left( 0\right) \) equal to \( W \) . (Compare Chapter 13.) If \( W \) belongs to \( {T}^{\prime } \) then we may assume that \( \overline{\alpha } \) is chosen so as to leave the points \( \left( {t}_{0}\right) , y\left( {t}_{1}\right) ,\ldots , y\left( {t}_{k}\right) \) fixed. In other words we may assume that \( \overline{\alpha }\left( u\right) \left( {t}_{i}\right)  = \gamma \left( {t}_{i}\right) \) for \( i = 0,1,\ldots , k \) .

Proof that \( {E}_{* * }\left( {W, W}\right)  \geq  0 \) for \( W \in  {T}^{\prime } \) . Each \( \overline{\alpha }\left( u\right)  \in  \Omega \) is a piecewise smooth path from \( \gamma \left( 0\right) \) to \( \gamma \left( {t}_{1}\right) \) to \( \gamma \left( {t}_{2}\right) \) to ... to \( \gamma \left( 1\right) \) . But each \( {\left. \gamma \right| }_{\left\lbrack  {t}_{i - 1},{t}_{i}\right\rbrack  } \) is a minimal geodesic, and therefore has smaller energy than any other path between its endpoints. This proves that

\[
E\left( {\overline{\alpha }\left( u\right) }\right)  \geq  E\left( \gamma \right)  = E\left( {\overline{\alpha }\left( 0\right) }\right) .
\]

Therefore the second derivative, evaluated at \( u = 0 \) , must be \( \geq  0 \) .

Proof that \( {E}_{* * }\left( {W, W}\right)  > 0 \) for \( W \in  {T}^{\prime }, W \neq  0 \) . Suppose that \( {E}_{* * }\left( {W, W}\right) \) were equal to 0 . Then \( W \) would lie in the null space of \( {E}_{* * } \) . In fact for any \( {W}_{1} \in  T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) we have already seen that \( {E}_{* * }\left( {{W}_{1}, W}\right)  = 0 \) . For any \( {W}_{2} \in  {T}^{\prime } \) the inequality

\[
0 \geq  {E}_{* * }\left( {W + c{W}_{2}, W + c{W}_{2}}\right)  = {2c}{E}_{* * }\left( {{W}_{2}, W}\right)  + {c}^{2}{E}_{* * }\left( {{W}_{2},{W}_{2}}\right)
\]

for all values of \( c \) implies that \( {E}_{* * }\left( {{W}_{2}, W}\right)  = 0 \) . Thus \( W \) lies in the null space. But the null space of \( {E}_{* * } \) consists of Jacobi fields. Since \( {T}^{\prime } \) contains no Jacobi fields other than zero, this implies that \( W = 0 \) .

Thus the quadratic form \( {E}_{* * } \) is positive definite on \( {T}^{\prime } \) . This completes the proof of Lemma 15.3.

An immediate consequence is the following:

Lemma 15.4. The index (or the nullity) of \( {E}_{* * } \) is equal to the index (or nullity) of \( {E}_{* * } \) restricted to the space \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) of broken Jacobi fields. In particular (since \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) is a finite dimensional vector space) the index \( \lambda \) is always finite.

The proof is straightforward.

Let \( {\gamma }_{\tau } \) denote the restriction of \( \gamma \) to the interval \( \left\lbrack  {0,\tau }\right\rbrack \) . Thus \( {\gamma }_{\tau } : \left\lbrack  {0,\tau }\right\rbrack   \rightarrow  M \) is a geodesic from \( \gamma \left( 0\right) \) to \( \gamma \left( \tau \right) \) . Let \( \lambda \left( \tau \right) \) denote the index of the Hessian \( {\left( {E}_{0}^{\tau }\right) }_{* * } \) which is associated with this geodesic. Thus \( \lambda \left( 1\right) \) is the index which we are actually trying to compute. First note that:

Assertion 15.1. \( \lambda \left( \tau \right) \) is a monotone function of \( \tau \) .

For if \( \tau  < {\tau }^{\prime } \) then there exists a \( \lambda \left( \tau \right) \) dimensional space \( V \) of vector fields along \( {\gamma }_{\tau } \) which vanish at \( \gamma \left( 0\right) \) and \( \gamma \left( \tau \right) \) such that the Hessian \( {\left( {E}_{0}^{\tau }\right) }_{* * } \) is negative definite on this vector space. Each vector field in \( V \) extends to a vector field along \( {\gamma }_{{\tau }^{\prime }} \) which vanishes identically between \( \gamma \left( \tau \right) \) and \( \gamma \left( {\tau }^{\prime }\right) \) . Thus we obtain a \( \lambda \left( \tau \right) \) dimensional vector space of fields along \( {\gamma }_{{\tau }^{\prime }} \) , on which \( {\left( {E}_{0}^{{\tau }^{\prime }}\right) }_{* * } \) is negative definite. Hence \( \lambda \left( \tau \right)  \leq  \lambda \left( {\tau }^{\prime }\right) \) .

Assertion 15.2. \( \lambda \left( \tau \right)  = 0 \) for small values of \( \tau \) .

For if \( \tau \) is sufficiently small then \( {\gamma }_{\tau } \) is a minimal geodesic, hence \( \lambda \left( \tau \right)  = 0 \) by Lemma 13.3.

Now let us examine the discontinuities of the function \( \lambda \left( \tau \right) \) . First note that \( \lambda \left( \tau \right) \) is continuous from the left:

Assertion 15.3. For all sufficiently small \( \varepsilon  > 0 \) we have \( \lambda \left( {\tau  - \varepsilon }\right)  = \lambda \left( \tau \right) \) .

Proof. According to Lemma 15.3 the number \( \lambda \left( 1\right) \) can be interpreted as the index of a quadratic form on a finite dimensional vector space \( T{\Omega }_{\gamma }\left( {{t}_{0},{t}_{1},\ldots ,{t}_{k}}\right) \) . We may assume that the subdivision is chosen so that say \( {t}_{i} < \tau  < {t}_{i + 1} \) . Then the index \( \lambda \left( \tau \right) \) can be interpreted as the index of a corresponding quadratic form \( {H}_{\tau } \) on a corresponding vector space of broken Jacobi fields along \( {\gamma }_{\tau } \) . This vector space is to be constructed using the subdivision \( 0 < {t}_{1} < {t}_{2} < \ldots  < {t}_{i} < \tau \) of \( \left\lbrack  {0,\tau }\right\rbrack \) . Since a broken Jacobi field is uniquely determined by its values at the break points \( \gamma \left( {t}_{i}\right) \) , this vector space is isomorphic to the direct sum

\[
\sum  = T{M}_{\gamma \left( {t}_{1}\right) } \oplus  T{M}_{\gamma \left( {t}_{2}\right) } \oplus  \cdots  \oplus  T{M}_{\gamma \left( {t}_{i}\right) }.
\]

Note that this vector space \( \sum \) is independent of \( \tau \) . Evidently the quadratic form \( {H}_{\tau } \) on \( \sum \) varies continuously with \( \tau \) .

Now \( {H}_{\tau } \) is negative definite on a subspace \( V \subset  \sum \) of dimension \( \lambda \left( \tau \right) \) . For all \( {\tau }^{\prime } \) sufficiently close to \( \tau \) it follows that \( {H}_{{\tau }^{\prime }} \) , is negative definite on \( V \) . Therefore \( \lambda \left( {\tau }^{\prime }\right)  \geq  \left( \tau \right) \) But if \( {\tau }^{\prime } = T - \varepsilon  < \tau \) then we also have \( \lambda \left( {\tau  - \varepsilon }\right)  \leq  \lambda \left( \tau \right) \) by Assertion 15.1. Hence \( \lambda \left( {\tau  - \varepsilon }\right)  = \lambda \left( \tau \right) \) .

Assertion 15.4. Let \( \nu \) be the nullity of the Hessian \( {\left( {E}_{0}^{\tau }\right) }_{* * } \) . Then for all sufficiently small \( \varepsilon  > 0 \) we have

\[
\lambda \left( {\tau  + \varepsilon }\right)  = \lambda \left( \tau \right)  + \nu .
\]

Thus the function \( \lambda \left( t\right) \) jumps by \( \nu \) when the variable \( t \) passes a conjugate point of multiplicity \( \nu \) ; and is continuous otherwise. Clearly this assertion will complete the proof of the Index Theorem.

Proof that \( \lambda \left( {\tau  + \varepsilon }\right)  \leq  \lambda \left( \tau \right)  + \nu \) . Let \( {H}_{\tau } \) and \( \sum \) be as in the proof of Assertion 15.3. Since \( \dim \sum  = {ni} \) we see that \( {H}_{\tau } \) is positive definite on some subspace \( {V}^{\prime } \subset  \sum \) of dimension \( {ni} - \lambda \left( \tau \right)  - \nu \) . For all \( {\tau }^{\prime } \) sufficiently close to \( \tau \) , it follows that \( {H}_{\tau } \) , is positive definite on \( {V}^{\prime } \) . Hence

\[
\lambda \left( {\tau }^{\prime }\right)  \leq  \dim \sum  - \dim {V}^{\prime } = \lambda \left( \tau \right)  + \nu .
\]

Proof THAT \( \lambda \left( {\tau  + \varepsilon }\right)  \geq  \lambda \left( \tau \right)  + \nu \) . Let \( {W}_{1},\ldots ,{W}_{\lambda \left( \tau \right) } \) be \( \lambda \left( \tau \right) \) vector fields along \( {\gamma }_{\tau } \) , vanishing at the endpoints, such that the matrix

\[
\left( {{\left( {E}_{0}^{\tau }\right) }_{* * }\left( {{W}_{i},{W}_{j}}\right) }\right)
\]

is negative definite. Let \( {\mathrm{J}}_{1},\ldots ,{\mathrm{J}}_{\nu } \) be \( \nu \) linearly independent Jacobi fields along \( {\gamma }_{\tau } \) , also vanishing at the endpoints. Note that the \( \nu \) vectors

\[
\frac{\mathrm{D}{\mathrm{J}}_{h}}{\mathrm{\;d}t}\left( \tau \right)  \in  T{M}_{\gamma \left( \tau \right) }
\]

are linearly independent. Hence it is possible to choose \( \nu \) vector fields \( {X}_{1},\ldots ,{X}_{\nu } \) along \( {\gamma }_{\tau  + \varepsilon } \) , vanishing at the endpoints of \( {\gamma }_{\tau  + \varepsilon } \) , so that

\[
\left( \left\langle  {\frac{{\mathrm{{DJ}}}_{h}}{\mathrm{\;d}t}\left( \tau \right) ,{X}_{k}\left( \tau \right) }\right\rangle  \right)
\]

is equal to the \( \nu  \times  \nu \) identity matrix. Extend the vector fields \( {W}_{i} \) and \( {\mathrm{J}}_{h} \) over \( {\gamma }_{\tau  + \varepsilon } \) by setting these fields equal to 0 for \( \tau  \leq  t \leq  \tau  + \varepsilon \) .

Using the second variation formula we see easily that

\[
{\left( {E}_{0}^{\tau  + \varepsilon }\right) }_{* * }\left( {{\mathrm{\;J}}_{h},{W}_{i}}\right)  = 0
\]

\[
{\left( {E}_{0}^{\tau  + \varepsilon }\right) }_{* * }\left( {{\mathrm{\;J}}_{h},{X}_{k}}\right)  = 2{\delta }_{hk}\;\text{ (Kronecker delta). }
\]

Now let \( c \) be a small number, and consider the \( \lambda \left( \tau \right)  + \nu \) vector fields

\[
{W}_{1},\ldots ,{W}_{\lambda \left( \tau \right) },{c}^{-1}{\mathrm{\;J}}_{1} - c{X}_{1},\ldots ,{c}^{-1}{\mathrm{\;J}}_{\nu } - c{X}_{\nu }
\]

along \( {\gamma }_{\tau  + \varepsilon } \) . We claim that these vector fields span a vector space of dimension \( \lambda \left( \tau \right)  + \nu \) on which the quadratic form \( {\left( {E}_{0}^{\tau  + \varepsilon }\right) }_{* * } \) is negative definite. In fact the matrix of \( {\left( {E}_{0}^{\tau  + \varepsilon }\right) }_{* * } \) with respect to this basis is

\[
\left( \begin{matrix} \left( {{\left( {E}_{0}^{\tau }\right) }_{* * }\left( {{W}_{i},{W}_{j}}\right) }\right) & {cA} \\  c{A}^{t} &  - 4\mathrm{I} + {c}^{2}B \end{matrix}\right)
\]

where \( A \) and \( B \) are fixed matrices. If \( c \) is sufficiently small, this compound matrix is certainly negative definite. This proves Assertion 15.4.

The index Theorem 15.1 clearly follows from the Assertions 15.2, 15.3, and 15.4.
