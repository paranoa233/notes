# 11.6 Wu's Formula for Stiefel-Whitney Classes

Let \( {\mathrm{w}}_{i} = {\mathrm{w}}_{i}\left( {\tau }_{M}\right) \) be the \( i \) -th Stiefel-Whitney class of the tangent bundle of a smooth manifold \( M \) , or equivalently the \( i \) -th Stiefel-Whitney class of the normal bundle of the diagonal in \( M \times  M \) . Applying Thom’s formula (p. 99)

\[
{\mathrm{{Sq}}}^{i}\left( u\right)  = \left( {{\pi }^{ * }{\mathrm{\;w}}_{i}}\right)  \smile  u
\]

together with the isomorphism

\[
{\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right)  \cong  {\mathrm{H}}^{ * }\left( {{N}_{\varepsilon },{N}_{\varepsilon } - \Delta \left( M\right) }\right)  \cong  {\mathrm{H}}^{ * }\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)
\]

of 11.2 , it follows easily that

\[
{\mathrm{{Sq}}}^{i}\left( {u}^{\prime }\right)  = \left( {{\mathrm{w}}_{i} \times  1}\right)  \smile  {u}^{\prime }.
\]

Therefore, restricting to \( {\mathrm{H}}^{ * }\left( {M \times  M}\right) \) , we obtain \( {\mathrm{{Sq}}}^{i}\left( {u}^{\prime \prime }\right)  = \left( {{\mathrm{w}}_{i} \times  1}\right)  \smile  {u}^{\prime \prime } \) .

We will again make use of the fact that the slant product homomorphism

\[
/\beta  : {\mathrm{H}}^{ * }\left( {X \times  Y}\right)  \rightarrow  {\mathrm{H}}^{ * }\left( X\right)
\]

is left \( {\mathrm{H}}^{ * }\left( X\right) \) -linear for any \( \beta  \in  {\mathrm{H}}_{ * }\left( Y\right) \) . In particular, the slant product

\[
\left( {\left( {{\mathrm{w}}_{i} \times  1}\right)  \smile  {u}^{\prime \prime }}\right) /\mu
\]

is equal to

\[
{\mathrm{w}}_{i} \smile  \left( {{u}^{\prime \prime }/\mu }\right)  = {\mathrm{w}}_{i}.
\]

(Compare the proof of 11.11.) Since this is equal to \( {\mathrm{{Sq}}}^{i}\left( {u}^{\prime \prime }\right) /\mu \) , we have the following.

Lemma 11.13. If \( M \) is compact and smooth, then the Stiefel-Whitney classes of \( {\tau }_{M} \) are given by the formula \( {\mathrm{w}}_{i} = {\mathrm{{Sq}}}^{i}\left( {u}^{\prime \prime }\right) /\mu \) .

As a corollary, if two manifolds \( {M}_{1} \) and \( {M}_{2} \) have the same homotopy type, then their Stiefel-Whitney classes must correspond under the resulting isomorphism \( {\mathrm{H}}^{ * }\left( {M}_{1}\right)  \cong  {\mathrm{H}}^{ * }\left( {M}_{2}\right) \) . This follows since the class \( {u}^{\prime \prime } \) is determined by 11.11.

In fact, following Wu Wen-Tsün, one can work out an explicit recipe for computing \( {\mathrm{w}}_{i} \) , given only the mod 2 cohomology ring \( {\mathrm{H}}^{ * }\left( M\right) \) and the action of the Steenrod squares on \( {\mathrm{H}}^{ * }\left( M\right) \) . Consider the additive homomorphism

\[
x \mapsto  \left\langle  {{\mathrm{{Sq}}}^{k}\left( x\right) ,\mu }\right\rangle
\]

from \( {\mathrm{H}}^{n - k}\left( M\right) \) to \( \mathbb{Z}/2 \) . Using the Duality Theorem 11.10, there clearly exists one and only one cohomology class

\[
{v}_{k} \in  {\mathrm{H}}^{k}\left( M\right)
\]

which satisfies the identity

\[
\left\langle  {{v}_{k} \smile  x,\mu }\right\rangle   = \left\langle  {{\mathrm{{Sq}}}^{k}\left( x\right) ,\mu }\right\rangle
\]

for every \( x \) . (In fact, if one considers \( M \) as the disjoint union of its connected components, then it is easy to check that \( {v}_{k} \) satisfies the sharper condition

\[
{v}_{k} \smile  x = {\mathrm{{Sq}}}^{k}\left( x\right)  \in  {\mathrm{H}}^{n}\left( M\right)
\]

for every \( x \in  {\mathrm{H}}^{n - k}\left( M\right) \) . Of course the class \( {v}_{k} \) is zero whenever \( k > n - k \) ). We define the total Wu class

\[
v \in  {\mathrm{H}}^{\Pi }\left( M\right)  = {\mathrm{H}}^{0}\left( M\right)  \oplus  {\mathrm{H}}^{1}\left( M\right)  \oplus  \ldots  \oplus  {\mathrm{H}}^{n}\left( M\right)
\]

to be the formal sum

\[
v = 1 + {v}_{1} + \ldots  + {v}_{n}.
\]

Clearly \( v \) satisfies and is characterized by the identity

\[
\langle v \smile  x,\mu \rangle  = \langle \mathrm{{Sq}}\left( x\right) ,\mu \rangle ,
\]

which holds for every cohomology class \( x \) . Here \( \mathrm{{Sq}} \) denotes the total squaring operation \( {\mathrm{{Sq}}}^{0} + {\mathrm{{Sq}}}^{1} + {\mathrm{{Sq}}}^{2} + \ldots \)

Theorem 11.14 (Wu). The total Stiefel-Whitney class w of \( {\tau }_{M} \) is equal to \( \mathrm{{Sq}}\left( v\right) \) . In other words

\[
{\mathrm{w}}_{k} = \mathop{\sum }\limits_{{i + j = k}}{\mathrm{{Sq}}}^{i}\left( {v}_{j}\right) .
\]

Proof. Choose a basis \( \left\{  {b}_{i}\right\} \) for the mod 2 cohomology \( {\mathrm{H}}^{ * }\left( M\right) \) and a dual basis \( \left\{  {b}_{i}^{\# }\right\} \) , as in 11.10. Then for any cohomology class \( x \) in \( {\mathrm{H}}^{\Pi }\left( M\right) \) the identity

\[
x = \sum {b}_{i}\left\langle  {x \smile  {b}_{i}^{\# },\mu }\right\rangle
\]

is easily verified. Applying this identity to the total Wu class \( v \) we obtain

\[
v = \sum {b}_{i}\left\langle  {v \smile  {b}_{i}^{\# },\mu }\right\rangle   = \sum {b}_{i}\left\langle  {\operatorname{Sq}\left( {b}_{i}^{\# }\right) ,\mu }\right\rangle  .
\]

Therefore \( \mathrm{{Sq}}\left( v\right) \) is equal to

\[
\sum \operatorname{Sq}\left( {b}_{i}\right) \left\langle  {\operatorname{Sq}\left( {b}_{i}^{\# }\right) ,\mu }\right\rangle   = \sum \left( {\operatorname{Sq}\left( {b}_{i}\right)  \times  \operatorname{Sq}\left( {b}_{i}^{\# }\right) }\right) /\mu  = \operatorname{Sq}\left( {u}^{\prime \prime }\right) /\mu
\]

by 11.11. Hence \( \operatorname{Sq}\left( v\right)  = \mathrm{w} \) as required.

Here is a concrete application to illustrate Wu’s theorem. Let \( M \) be a compact manifold whose mod 2 cohomology ring is generated by a single element \( a \in  {\mathrm{H}}^{k}\left( M\right) \) , which \( k \geq  1 \) . Thus the cohomology \( {\mathrm{H}}^{ * }\left( M\right) \) has basis \( \left\{  {1, a,{a}^{2},\ldots ,{a}^{m}}\right\} \) and the dimension of \( M \) must be equal to \( {km} \) , for some integer \( m \geq  1 \) .

Corollary 11.15. With \( M \) as above, the total Stiefel-Whitney class \( \mathrm{w}\left( {\tau }_{M}\right) \) is equal to

\[
{\left( 1 + a\right) }^{m + 1} = 1 + \left( \begin{matrix} m + 1 \\  1 \end{matrix}\right) a + \ldots  + \left( \begin{matrix} m + 1 \\  m \end{matrix}\right) {a}^{m}.
\]

As an example, the hypothesis of 11.15 is certainly satisfied for the sphere \( {S}^{k} \) , with \( m = 1 \) and \( \mathrm{w} = {\left( 1 + a\right) }^{2} = 1 \) . It is also satisfied for the real projective space \( {\mathbb{P}}^{m} = {\mathbb{P}}^{m}\left( \mathbb{R}\right) \) , with cohomology generator \( a \) in dimension \( k = 1 \) . (Compare 4.5.) We will see in \( \text{ § }{14} \) that it is satisfied for the complex projective space \( {\mathbb{P}}^{m}\left( \mathbb{C}\right) \) , a \( {2m} \) - dimensional manifold with cohomology generator in dimension \( k = 2 \) . Similarly, it is satisfied for the quaternion projective \( m \) -space, a \( {4m} \) -dimensional manifold with cohomology generator in dimension \( k = 4 \) . (See for example [Spa81].) Finally, it is satisfied for the Cayley plane, a 16-dimensional manifold with cohomology generator \( a \in  {\mathrm{H}}^{8}\left( M\right) \) , and with Stiefel-Whitney class \( \mathrm{w} = {\left( 1 + a\right) }^{3} + 1 + a + {a}^{2} \) . (See Borel [Bor50].)

These are essentially the only examples which exist. For according to Adams[Ada60], if a space \( X \) has mod 2 cohomology generated by \( a \in  {\mathrm{H}}^{k}\left( X\right) \) with \( k \geq  1 \) , and if \( {a}^{2} \neq  0 \) , then \( k \) must be either 1,2,4 or 8 . Furthermore, if \( {a}^{3} \neq  0 \) , then by [Ade52] \( k \) must be 1,2 or 4 . Thus the manifolds described above give the only possibly truncated polynomial rings on one generator over \( \mathbb{Z}/2 \) . (Compare the discussion of related problems on page 54.)

Proof of 11.15. The action of the Steenrod squares on \( {\mathrm{H}}^{ * }\left( M\right) \) is evidently given by

\[
\operatorname{Sq}\left( a\right)  = a + {a}^{2},
\]

and hence

\[
\operatorname{Sq}\left( {a}^{i}\right)  = {\left( a + {a}^{2}\right) }^{i} = {a}^{i}{\left( 1 + a\right) }^{i}.
\]

It follows that the Kronecker index \( \left\langle  {\operatorname{Sq}\left( {a}^{i}\right) ,\mu }\right\rangle \) is equal to the binomial coefficient \( \left( \begin{matrix} i \\  m - i \end{matrix}\right) \) . Applying the formula

\[
\left\langle  {\operatorname{Sq}\left( {a}^{i}\right) ,\mu }\right\rangle   = \left\langle  {v \smile  {a}^{i},\mu }\right\rangle  ,
\]

this implies that the coefficient of \( {a}^{m - i} \) in the total Wu class \( v \) must also be equal to \( \left( \begin{matrix} i \\  m - i \end{matrix}\right) \) . Hence

\[
v = \sum \left( \begin{matrix} i \\  m - i \end{matrix}\right) {a}^{m - i}
\]

Substituting \( j \) for \( m - i \) , it will be more convenient to write this as \( v = \sum \left( \begin{matrix} m - j \\  j \end{matrix}\right) {a}^{j} \) . Therefore

\[
\mathrm{w} = \mathrm{{Sq}}\left( v\right)  = \sum \left( \begin{matrix} m - j \\  j \end{matrix}\right) \mathrm{{Sq}}\left( {a}^{j}\right) .
\]

Since we know how to compute \( \mathrm{{Sq}}\left( {a}^{j}\right) \) , an explicit computation with binomial coefficients should now complete the argument. For example, if \( m = 5 \) , then

\[
v = \sum \left( \begin{matrix} 5 - j \\  j \end{matrix}\right) {a}^{j} = 1 + {a}^{2},
\]

hence

\[
\mathrm{w} = \operatorname{Sq}\left( {1 + {a}^{2}}\right)  = 1 + {a}^{2} + {a}^{4}.
\]

In general it is clear that the necessary computation, expressing w as a polynomial function of \( a \) , depends only on \( m \) , being completely independent of the dimension \( k \) of \( a \) . But this gives us a convenient shortcut. For when \( k = 1 \) we already know that this computation must lead to the formula \( \mathrm{w} = {\left( 1 + a\right) }^{m + 1} \) by Theorem 4.5. Evidently an identical computation, applied to a generator \( a \) of higher dimension, must lead to this same formula.

Problem 11-A. Prove Lemma 4.3 (that is, compute the mod 2 cohomology of \( {\mathbb{P}}^{n} \) ) by induction on \( n \) , using the Duality Theorem 11.10 and the cell structure of 6.5.

Problem 11-B. More Poincaré Duality. For \( M \) compact, using field coefficients, show that

\[
{u}^{\prime \prime }/ : {\mathrm{H}}_{n - k}\left( M\right)  \rightarrow  {\mathrm{H}}^{k}\left( M\right)
\]

is an isomorphism. Using the cap product operation of Appendix A, show that the inverse isomorphism is given by

\[
\cap  \mu  : {\mathrm{H}}^{k}\left( M\right)  \rightarrow  {\mathrm{H}}_{n - k}\left( M\right)
\]

multiplied by the sign \( {\left( -1\right) }^{kn} \) .

Problem 11-C. Let \( M = {M}^{n} \) and \( A = {A}^{p} \) be compact oriented manifolds with smooth embedding \( i : M \rightarrow  A \) . Let \( k = p - n \) . Show that the Poincaré duality isomorphism

\[
\cap  {\mu }_{A} : {\mathrm{H}}^{k}\left( A\right)  \rightarrow  {\mathrm{H}}_{n}\left( A\right)
\]

maps the cohomology class \( {\left. {u}^{\prime }\right| }_{A} \) "dual" to \( M \) to the homology class \( {\left( -1\right) }^{nk}{i}_{ * }\left( {\mu }_{M}\right) \) . (We assume that the normal bundle \( {\nu }^{k} \) is oriented so that \( {\tau }_{M} \oplus  {\nu }^{k} \) is orientation preserving isomorphic to \( {\left. {\tau }_{A}\right| }_{M} \) . The proof makes use of the commutative diagram

![bo_d7du9galb0pc73deir9g_141_298_987_1195_157_0.jpg](images/bo_d7du9galb0pc73deir9g_141_298_987_1195_157_0.jpg)

where \( N \) is a tubular neighborhood of \( M \) in \( A \) .)

Problem 11-D. Prove that all Stiefel-Whitney numbers of a 3-manifold are zero.

Problem 11-E. Prove the following version of Wu's formula. Let

\[
\overline{\mathrm{{Sq}}} : {\mathrm{H}}^{\Pi }\left( M\right)  \rightarrow  {\mathrm{H}}^{\Pi }\left( M\right)
\]

be the inverse of the ring automorphism Sq. Show that the dual Stiefel-Whitney classes \( {\overline{\mathrm{w}}}_{i}\left( {\tau }_{M}\right) \) are determined by the formula

\[
\langle \overline{\mathrm{{Sq}}}\left( x\right) ,\mu \rangle  = \langle \overline{\mathrm{w}} \smile  x,\mu \rangle ,
\]

which holds for every cohomology class \( x \) . Show that \( {\overline{\mathrm{w}}}_{n} = 0 \) . If \( n \) is not a power of 2, show that \( {\overline{\mathrm{w}}}_{n - 1} = 0 \) .

Problem 11-F. Definining Steenrod operations \( {\mathrm{{Sq}}}^{i} : {\mathrm{H}}_{k}\left( X\right)  \rightarrow  {\mathrm{H}}_{k - i}\left( X\right) \) on mod 2 homology by the identity

\[
\left\langle  {x,{\mathrm{{Sq}}}^{i}\left( \beta \right) }\right\rangle   = \left\langle  {\overline{\mathrm{{Sq}}}{}^{i}\left( x\right) ,\beta }\right\rangle  ,
\]

show that

\[
\mathrm{{Sq}}\left( {a \cap  \beta }\right)  = \mathrm{{Sq}}\left( a\right)  \cap  \mathrm{{Sq}}\left( \beta \right) ,
\]

and that

\[
\operatorname{Sq}\left( {{u}^{\prime \prime }/\beta }\right)  = \operatorname{Sq}\left( {u}^{\prime \prime }\right) /\operatorname{Sq}\left( \beta \right) .
\]

Prove the formulas \( \mathrm{{Sq}}\left( \mu \right)  = \overline{\mathrm{w}} \cap  \mu \) and \( \overline{\mathrm{{Sq}}}\left( \mu \right)  = v \cap  \mu \) .
