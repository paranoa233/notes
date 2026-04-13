# 8.1 Verification of the Axioms

With this definition, the four axioms for Stiefel-Whitney classes can be checked as follows.

AXIOM 1. Using properties (1) and (3) of the squaring operations, it is clear that \( {\mathrm{w}}_{i}\left( \xi \right)  \in  {\mathrm{H}}^{i}\left( B\right) \) , with \( {\mathrm{w}}_{0}\left( \xi \right)  = 1 \) , and with \( {\mathrm{w}}_{i}\left( \xi \right)  = 0 \) for \( i \) greater than the fiber dimension \( n \) .

Axiom 2. Any bundle map \( f : \xi  \rightarrow  {\xi }^{\prime } \) clearly induces a map \( g : \left( {E,{E}_{0}}\right)  \rightarrow  \left( {{E}^{\prime },{E}_{0}^{\prime }}\right) \) . Furthermore if \( {u}^{\prime } \) denotes the fundamental cohomology class in \( {\mathrm{H}}^{n}\left( {{E}^{\prime },{E}_{0}^{\prime }}\right) \) , then \( {g}^{ * }\left( {u}^{\prime }\right) \) is equal to the class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) by the definition of \( u \) (Theorem 8.1). It now follows easily that the Thom isomorphisms \( \phi \) and \( {\phi }^{\prime } \) satisfy the naturality condition

\[
{g}^{ * } \circ  {\phi }^{\prime } = \phi  \circ  {\bar{f}}^{ * }.
\]

Hence, using property (2), it follows that

\[
{\bar{f}}^{ * }{\mathrm{\;w}}_{i}\left( {\xi }^{\prime }\right)  = {\mathrm{w}}_{i}\left( \xi \right) ,
\]

as required.

AXIOM 3. Let us first compute the Stiefel-Whitney classes of a Cartesian product \( {\xi }^{\prime \prime } = \xi  \times  {\xi }^{\prime } \) , with projection map \( \pi  \times  {\pi }^{\prime } : E \times  {E}^{\prime } \rightarrow  B \times  {B}^{\prime } \) . Consider the fundamental classes

\[
u \in  {\mathrm{H}}^{m}\left( {E,{E}_{0}}\right) ,\;{u}^{\prime } \in  {\mathrm{H}}^{n}\left( {{E}^{\prime },{E}_{0}^{\prime }}\right)
\]

of \( \xi \) and \( {\xi }^{\prime } \) . Since \( {E}_{0} \) is open in \( E \) and \( {E}_{0}^{\prime } \) is open in \( {E}^{\prime } \) , the cross product

\[
u \times  {u}^{\prime } \in  {\mathrm{H}}^{m + n}\left( {E \times  {E}^{\prime }, E \times  {E}_{0}^{\prime } \cup  {E}_{0} \times  {E}^{\prime }}\right)
\]

is defined. (Compare Appendix A.) Note that the open subset

\( \left( {E \times  {E}_{0}^{\prime }}\right)  \cup  \left( {{E}_{0} \times  {E}^{\prime }}\right) \) in the total space \( {E}^{\prime \prime } = E \times  {E}^{\prime } \) is precisely equal to the set \( {E}_{0}^{\prime \prime } \) of non-zero vectors in \( {E}^{\prime \prime } \) . In fact we claim that \( u \times  {u}^{\prime } \) is precisely

equal to the fundamental class \( {u}^{\prime \prime } \in  {\mathrm{H}}^{m + n}\left( {{E}^{\prime \prime },{E}_{0}^{\prime \prime }}\right) \) . In order to prove this, it suffices to show that the restriction

\[
u \times  {u}^{\prime } \mid  \left( {{F}^{\prime \prime },{F}_{0}^{\prime \prime }}\right)
\]

is the non-zero cohomology class in \( {\mathrm{H}}^{m + n}\left( {{F}^{\prime \prime },{F}_{0}^{\prime \prime }}\right) \) for every fiber \( {F}^{\prime \prime } = F \times  {F}^{\prime } \) of \( {\xi }^{\prime \prime } \) . But this restriction is evidently equal to the cross product of \( {\left. u\right| }_{\left( F,{F}_{0}\right) } \) and \( {\left. {u}^{\prime }\right| }_{\left( {F}^{\prime },{F}_{0}^{\prime }\right) } \) , and hence is non-zero by A. 6 in the Appendix.

It follows easily that the Thom isomorphisms for \( \xi ,{\xi }^{\prime } \) , and \( {\xi }^{\prime \prime } \) are related by the identity

\[
{\phi }^{\prime \prime }\left( {a \times  b}\right)  = \phi \left( a\right)  \times  {\phi }^{\prime }\left( b\right) .
\]

In fact if \( \bar{a} = {\pi }^{ * }\left( a\right)  \in  {\mathrm{H}}^{ * }\left( E\right) \) and \( \bar{b} = {\pi }^{\prime  * }\left( b\right)  \in  {\mathrm{H}}^{ * }\left( {E}^{\prime }\right) \) , then this follows from the equation

\[
\left( {\bar{a} \times  \bar{b}}\right)  \smile  \left( {u \times  {u}^{\prime }}\right)  = \left( {\bar{a} \smile  u}\right)  \times  \left( {\bar{b} \smile  {u}^{\prime }}\right) ,
\]

where there is no sign since we are working modulo 2.

The total Stiefel-Whitney class of \( {\xi }^{\prime \prime } \) can now be computed by the formula

\[
{\phi }^{\prime \prime }\left( {w\left( {\xi }^{\prime \prime }\right) }\right)  = \operatorname{Sq}\left( {u}^{\prime \prime }\right)  = \operatorname{Sq}\left( {u \times  {u}^{\prime }}\right)  = \operatorname{Sq}\left( u\right)  \times  \operatorname{Sq}\left( {u}^{\prime }\right) .
\]

Setting the right side equal to

\[
\phi \left( {w\left( \xi \right) }\right)  \times  {\phi }^{\prime }\left( {w\left( {\xi }^{\prime }\right) }\right)  = {\phi }^{\prime \prime }\left( {w\left( \xi \right)  \times  w\left( {\xi }^{\prime }\right) }\right) ,
\]

and then applying \( {\left( {\phi }^{\prime \prime }\right) }^{-1} \) to both sides, we have proved that

\[
w\left( {\xi  \times  {\xi }^{\prime }}\right)  = w\left( \xi \right)  \times  w\left( {\xi }^{\prime }\right) .
\]

Now suppose that \( \xi \) and \( {\xi }^{\prime } \) are bundles over a common base space \( B \) . Lifting both sides of this equation back to \( B \) by means of the diagonal embedding \( B \rightarrow  B \times  B \) , we obtain the required formula

\[
w\left( {\xi  \oplus  {\xi }^{\prime }}\right)  = w\left( \xi \right)  \smile  w\left( {\xi }^{\prime }\right) .
\]

Axiom 4. Let \( {\gamma }_{1}^{1} \) be as usual the twisted line bundle over the circle \( {\mathbb{P}}^{1} \) . Then the space of vectors of length \( \leq  1 \) in the total space \( E = E\left( {\gamma }_{1}^{1}\right) \) is evidently a Möbius band \( M \) , bounded by a circle \( M \) . Since \( M \) is a deformation retract of \( E \) , and \( M \) a deformation retract of \( {E}_{0} \) , we have

\[
{\mathrm{H}}^{ * }\left( {M,\overset{ \bullet  }{M}}\right)  \cong  {\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right) .
\]

On the other hand if we embed a 2-cell \( {\mathbb{D}}^{2} \) in the projective plane \( {\mathbb{P}}^{2} \) , then the closure of \( {\mathbb{P}}^{2} \smallsetminus  {\mathbb{D}}^{2} \) is homeomorphic to \( M \) . Using the Excision Theorem of cohomology theory, it follows that

\[
{\mathrm{H}}^{ * }\left( {M,\overset{ \bullet  }{M}}\right)  \cong  {\mathrm{H}}^{ * }\left( {{\mathbb{P}}^{2},{\mathbb{D}}^{2}}\right) .
\]

Hence there are natural isomorphisms

\[
{\mathrm{H}}^{i}\left( {E,{E}_{0}}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {M,\overset{ \bullet  }{M}}\right)  \leftarrow  {\mathrm{H}}^{i}\left( {{\mathbb{P}}^{2},{\mathbb{D}}^{2}}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {\mathbb{P}}^{2}\right)
\]

for every dimension \( i \neq  0 \) . The fundamental cohomology class \( u \in  {\mathrm{H}}^{1}\left( {E,{E}_{0}}\right) \) certainly cannot be zero. Hence it must correspond to the generator \( a \in  {\mathrm{H}}^{1}\left( {\mathbb{P}}^{2}\right) \) under the composite isomorphism. Hence \( {\mathrm{{Sq}}}^{1}\left( u\right)  = u \smile  u \) must correspond to \( {\mathrm{{Sq}}}^{1}\left( a\right)  = a \smile  a \) . But \( a \smile  a \neq  0 \) by 4.3, so it follows that

\[
{\mathrm{w}}_{1}\left( {\gamma }_{1}^{1}\right)  = {\phi }^{-1}{\mathrm{{Sq}}}^{1}\left( u\right)
\]

must also be non-zero. This concludes the verification of the four axioms.

## Problems

Problem 8-A. It follows from 7.1 that the cohomology class that the cohomology class \( {\mathrm{{Sq}}}^{k}{\mathrm{w}}_{m}\left( \xi \right) \) can be expressed as a polynomial in \( {\mathrm{w}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{w}}_{m + k}\left( \xi \right) \) . Prove Wu's explicit formula

\[
{\mathrm{{Sq}}}^{k}\left( {\mathrm{w}}_{m}\right)  = {\mathrm{w}}_{k}{\mathrm{w}}_{m} + \left( \begin{matrix} k - m \\  1 \end{matrix}\right) {\mathrm{w}}_{k - 1}{\mathrm{w}}_{m + 1} + \cdots  + \left( \begin{matrix} k - m \\  k \end{matrix}\right) {\mathrm{w}}_{0}{\mathrm{w}}_{m + k}
\]

where \( \left( \begin{array}{l} x \\  i \end{array}\right)  = x\left( {x - 1}\right) \ldots \left( {x - i + 1}\right) /i \) !, as follows. If the formula is true for \( \xi \) , show that it is true for \( \xi  \times  {\gamma }^{1} \) . Thus by induction it is true for \( {\gamma }^{1} \times  \cdots  \times  {\gamma }^{1} \) , and hence for all \( \xi \) .

Problem 8-B. If \( \mathrm{w}\left( \xi \right)  \neq  1 \) , show that the smallest \( n > 0 \) with \( {\mathrm{w}}_{n}\left( \xi \right)  \neq  0 \) is a power of 2 . (Use the fact that \( \left( \begin{array}{l} x \\  k \end{array}\right) \) is odd whenever \( x \) is an odd multiple of \( k = {2}^{r} \) .)
