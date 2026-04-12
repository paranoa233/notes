# 3.2 Cup Product

In the introduction to this chapter we sketched a definition of cup product in terms of another product called cross product. However, to define the cross product from scratch takes some work, so we will proceed in the opposite order, first giving an elementary definition of cup product by an explicit formula with simplices, then afterwards defining cross product in terms of cup product. The other approach of defining cup product via cross product is explained at the end of §3.B.

To define the cup product we consider cohomology with coefficients in a ring \( R \) , the most common choices being \( \mathbb{Z},{\mathbb{Z}}_{n} \) , and \( \mathbb{Q} \) . For cochains \( \varphi  \in  {C}^{k}\left( {X;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {X;R}\right) \) , the cup product \( \varphi  \smile  \psi  \in  {C}^{k + \ell }\left( {X;R}\right) \) is the cochain whose value on a singular simplex \( \sigma  : {\Delta }^{k + \ell } \rightarrow  X \) is given by the formula

\[
\left( {\varphi  \smile  \psi }\right) \left( \sigma \right)  = \varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{k}}\right\rbrack  }\right) \psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{k + \ell }}\right\rbrack  }\right)
\]

where the right-hand side is the product in \( R \) . To see that this cup product of cochains induces a cup product of cohomology classes we need a formula relating it to the coboundary map:

\( \parallel \) Lemma 3.6. \( \delta \left( {\varphi  - \psi }\right)  = {\delta \varphi } - \psi  + {\left( -1\right) }^{k}\varphi  - {\delta \psi } \) for \( \varphi  \in  {C}^{k}\left( {X;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {X;R}\right) \) .

Proof: For \( \sigma  : {\Delta }^{k + \ell  + 1} \rightarrow  X \) we have

\[
\left( {{\delta \varphi } \smile  \psi }\right) \left( \sigma \right)  = \mathop{\sum }\limits_{{i = 0}}^{{k + 1}}{\left( -1\right) }^{i}\varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{k + 1}}\right\rbrack  }\right) \psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k + 1},\cdots ,{v}_{k + \ell  + 1}}\right\rbrack  }\right)
\]

\[
{\left( -1\right) }^{k}\left( {\varphi  - {\delta \psi }}\right) \left( \sigma \right)  = \mathop{\sum }\limits_{{i = k}}^{{k + \ell  + 1}}{\left( -1\right) }^{i}\varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{k}}\right\rbrack  }\right) \psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{k + \ell  + 1}}\right\rbrack  }\right)
\]

When we add these two expressions, the last term of the first sum cancels the first term of the second sum, and the remaining terms are exactly \( \delta \left( {\varphi  - \psi }\right) \left( \sigma \right)  = \left( {\varphi  - \psi }\right) \left( {\partial \sigma }\right) \) since \( \partial \sigma  = \mathop{\sum }\limits_{{i = 0}}^{{k + \ell  + 1}}{\left( -1\right) }^{i}\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{k + \ell  + 1}}\right\rbrack \) .

From the formula \( \delta \left( {\varphi  \smile  \psi }\right)  = {\delta \varphi } \smile  \psi  \pm  \varphi  \smile  {\delta \psi } \) it is apparent that the cup product of two cocycles is again a cocycle. Also, the cup product of a cocycle and a coboundary, in either order, is a coboundary since \( \varphi  \smile  {\delta \psi } =  \pm  \delta \left( {\varphi  \smile  \psi }\right) \) if \( {\delta \varphi } = 0 \) , and \( {\delta \varphi } - \psi  = \delta \left( {\varphi  - \psi }\right) \) if \( {\delta \psi } = 0 \) . It follows that there is an induced cup product

\[
{H}^{k}\left( {X;R}\right)  \times  {H}^{\ell }\left( {X;R}\right) \overset{ \smile  }{ \rightarrow  }{H}^{k + \ell }\left( {X;R}\right)
\]

This is associative and distributive since at the level of cochains the cup product obviously has these properties. If \( R \) has an identity element, then there is an identity element for cup product, the class \( 1 \in  {H}^{0}\left( {X;R}\right) \) defined by the 0-cocycle taking the value 1 on each singular 0-simplex.

A cup product for simplicial cohomology can be defined by the same formula as for singular cohomology, so the canonical isomorphism between simplicial and singular cohomology respects cup products. Here are three examples of direct calculations of cup products using simplicial cohomology.

Example 3.7. Let \( M \) be the closed orientable surface of genus \( g \geq  1 \) with the \( \Delta \) -complex structure shown in the figure for the case \( g = 2 \) . The cup product of interest is \( {H}^{1}\left( M\right)  \times  {H}^{1}\left( M\right)  \rightarrow  {H}^{2}\left( M\right) \) . Taking \( \mathbb{Z} \) coefficients, a basis for \( {H}_{1}\left( M\right) \) is formed by the edges \( {a}_{i} \) and \( {b}_{i} \) , as we showed in Example 2.36 when we computed the homology of \( M \) using cellular homology. We have \( {H}^{1}\left( M\right)  \approx  \operatorname{Hom}\left( {{H}_{1}\left( M\right) ,\mathbb{Z}}\right) \) by cellular cohomology or the universal coefficient theorem. A basis for \( {H}_{1}\left( M\right) \) determines a dual basis for \( \operatorname{Hom}\left( {{H}_{1}\left( M\right) ,\mathbb{Z}}\right) \) , so dual to \( {a}_{i} \) is the cohomology class \( {\alpha }_{i} \) assigning the value 1 to \( {a}_{i} \) and 0 to the other basis elements, and similarly we have cohomology classes \( {\beta }_{i} \) dual to \( {b}_{i} \) .

![bo_d7dtv0s91nqc73eq8nv0_215_1094_918_493_463_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_215_1094_918_493_463_0.jpg)

To represent \( {\alpha }_{i} \) by a simplicial cocycle \( {\varphi }_{i} \) we need to choose values for \( {\varphi }_{i} \) on the edges radiating out from the central vertex in such a way that \( \delta {\varphi }_{i} = 0 \) . This is the 'cocycle condition' discussed in the introduction to this chapter, where we saw that it has a geometric interpretation in terms of curves transverse to the edges of \( M \) . With this interpretation in mind, consider the arc labeled \( {\alpha }_{i} \) in the figure, which represents a loop in \( M \) meeting \( {a}_{i} \) in one point and disjoint from all the other basis elements \( {a}_{j} \) and \( {b}_{j} \) . We define \( {\varphi }_{i} \) to have the value 1 on edges meeting the arc \( {\alpha }_{i} \) and the value 0 on all other edges. Thus \( {\varphi }_{i} \) counts the number of intersections of each edge with the arc \( {\alpha }_{i} \) . In similar fashion we obtain a cocycle \( {\psi }_{i} \) counting intersections with the \( \operatorname{arc}{\beta }_{i} \) , and \( {\psi }_{i} \) represents the cohomology class \( {\beta }_{i} \) dual to \( {b}_{i} \) .

Now we can compute cup products by applying the definition. Keeping in mind that the ordering of the vertices of each 2-simplex is compatible with the indicated orientations of its edges, we see for example that \( {\varphi }_{1} \smile  {\psi }_{1} \) takes the value 0 on all 2-simplices except the one with outer edge \( {b}_{1} \) in the lower right part of the figure, where it takes the value 1 . Thus \( {\varphi }_{1} \sim  {\psi }_{1} \) takes the value 1 on the 2-chain \( c \) formed by the sum of all the 2-simplices with the signs indicated in the center of the figure. It is an easy calculation that \( \partial c = 0 \) . Since there are no 3-simplices, \( c \) is not a boundary, so it represents a nonzero element of \( {H}_{2}\left( M\right) \) . The fact that \( \left( {{\varphi }_{1} \smile  {\psi }_{1}}\right) \left( c\right) \) is a generator of \( \mathbb{Z} \) implies both that \( c \) represents a generator of \( {H}_{2}\left( M\right)  \approx  \mathbb{Z} \) and that \( {\varphi }_{1} \smile  {\psi }_{1} \) represents the dual generator \( \gamma \) of \( {H}^{2}\left( M\right)  \approx  \operatorname{Hom}\left( {{H}_{2}\left( M\right) ,\mathbb{Z}}\right)  \approx  \mathbb{Z} \) . Thus \( {\alpha }_{1} \smile  {\beta }_{1} = \gamma \) . In similar fashion one computes:

\[
{\alpha }_{i} \smile  {\beta }_{j} = \left\{  \begin{array}{ll} y, & i = j \\  0, & i \neq  j \end{array}\right\}   =  - \left( {{\beta }_{i} \smile  {\alpha }_{j}}\right) ,\;{\alpha }_{i} \smile  {\alpha }_{j} = 0,\;{\beta }_{i} \smile  {\beta }_{j} = 0
\]

These relations determine the cup product \( {H}^{1}\left( M\right)  \times  {H}^{1}\left( M\right)  \rightarrow  {H}^{2}\left( M\right) \) completely since cup product is distributive. Notice that cup product is not commutative in this example since \( {\alpha }_{i} \smile  {\beta }_{i} =  - \left( {{\beta }_{i} \smile  {\alpha }_{i}}\right) \) . We will show in Theorem 3.11 below that this is the worst that can happen: Cup product is commutative up to a sign depending only on dimension, assuming that the coefficient ring itself is commutative.

One can see in this example that nonzero cup products of distinct classes \( {\alpha }_{i} \) or \( {\beta }_{j} \) occur precisely when the corresponding loops \( {\alpha }_{i} \) or \( {\beta }_{j} \) intersect. This is also true for the cup product of \( {\alpha }_{i} \) or \( {\beta }_{i} \) with itself if we allow ourselves to take two copies of the corresponding loop and deform one of them to be disjoint from the other.

Example 3.8. The closed nonorientable surface \( N \) of genus \( g \) can be treated in similar fashion if we use \( {\mathbb{Z}}_{2} \) coefficients. Using the \( \Delta \) -complex structure shown, the edges \( {a}_{i} \) give a basis for \( {H}_{1}\left( {N;{\mathbb{Z}}_{2}}\right) \) , and the dual basis elements \( {\alpha }_{i} \in  {H}^{1}\left( {N;{\mathbb{Z}}_{2}}\right) \) can be represented by cocycles with values given by counting intersections with the arcs labeled \( {\alpha }_{i} \) in the figure. Then one computes that \( {\alpha }_{i} \sim  {\alpha }_{i} \) is the nonzero element of \( {H}^{2}\left( {N;{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2} \) and \( {\alpha }_{i} \sim  {\alpha }_{j} = 0 \) for \( i \neq  j \) . In particular, when \( g = 1 \) we have \( N = {\mathbb{{RP}}}^{2} \) , and the cup product of a generator of \( {H}^{1}\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right) \) with itself is a generator of \( {H}^{2}\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_216_1114_1212_472_457_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_216_1114_1212_472_457_0.jpg)

The remarks in the paragraph preceding this example apply here also, but with the following difference: When one tries to deform a second copy of the loop \( {\alpha }_{i} \) in the present example to be disjoint from the original copy, the best one can do is make it intersect the original in one point. This reflects the fact that \( {\alpha }_{i} \smile  {\alpha }_{i} \) is now nonzero.

Example 3.9. Let \( X \) be the 2-dimensional CW complex obtained by attaching a 2-cell to \( {S}^{1} \) by the degree \( m \) map \( {S}^{1} \rightarrow  {S}^{1}, z \mapsto  {z}^{m} \) . Using cellular cohomology, or cellular homology and the universal coefficient theorem, we see that \( {H}^{n}\left( {X;\mathbb{Z}}\right) \) consists of a \( \mathbb{Z} \) for \( n = 0 \) and a \( {\mathbb{Z}}_{m} \) for \( n = 2 \) , so the cup product structure with \( \mathbb{Z} \) coefficients is uninteresting. However, with \( {\mathbb{Z}}_{m} \) coefficients we have \( {H}^{i}\left( {X;{\mathbb{Z}}_{m}}\right)  \approx  {\mathbb{Z}}_{m} \) for \( i = 0,1,2 \) , so there is the possibility that the cup product of two 1-dimensional classes can be nontrivial.

To obtain a \( \Delta \) -complex structure on \( X \) , take a regular \( m \) -gon subdivided into \( m \) triangles \( {T}_{i} \) around a central vertex \( v \) , as shown in the figure for the case \( m = 4 \) , then identify all the outer edges by rotations of the \( m \) -gon. This gives \( X \) a \( \Delta \) -complex structure with 2 vertices, \( m + 1 \) edges, and \( m \) 2-simplices. A generator \( \alpha \) of \( {H}^{1}\left( {X;{\mathbb{Z}}_{m}}\right) \) is represented by a cocycle \( \varphi \) assigning the value 1 to the edge \( e \) , which generates \( {H}_{1}\left( X\right) \) . The condition that \( \varphi \) be a cocycle means that \( \varphi \left( {e}_{i}\right)  + \varphi \left( e\right)  = \varphi \left( {e}_{i + 1}\right) \) for all \( i \) , subscripts being taken mod \( m \) . So we may take \( \varphi \left( {e}_{i}\right)  = i \in  {\mathbb{Z}}_{m} \) . Hence \( \left( {\varphi  \smile  \varphi }\right) \left( {T}_{i}\right)  = \varphi \left( {e}_{i}\right) \varphi \left( e\right)  = i \) . The map \( h : {H}^{2}\left( {X;{\mathbb{Z}}_{m}}\right)  \rightarrow  \operatorname{Hom}\left( {{H}_{2}\left( {X;{\mathbb{Z}}_{m}}\right) ,{\mathbb{Z}}_{m}}\right) \) is an isomorphism since \( \mathop{\sum }\limits_{i}{T}_{i} \) is a generator of \( {H}_{2}\left( {X;{\mathbb{Z}}_{m}}\right) \) and there are 2-cocycles taking the value 1 on \( \mathop{\sum }\limits_{i}{T}_{i} \) , for example the cocycle taking the value 1 on one \( {T}_{i} \) and 0 on all the others. The cocycle \( \varphi  \smile  \varphi \) takes the value \( 0 + 1 + \cdots  + \left( {m - 1}\right) \) on \( \mathop{\sum }\limits_{i}{T}_{i} \) , hence represents \( 0 + 1 + \cdots  + \left( {m - 1}\right) \) times a generator \( \beta \) of \( {H}^{2}\left( {X;{\mathbb{Z}}_{m}}\right) \) . In \( {\mathbb{Z}}_{m} \) the sum \( 0 + 1 + \cdots  + \left( {m - 1}\right) \) is 0 if \( m \) is odd and \( k \) if \( m = {2k} \) since the terms 1 and \( m - 1 \) cancel,2 and \( m - 2 \) cancel, and so on. Thus, writing \( {\alpha }^{2} \) for \( \alpha  \smile  \alpha \) , we have \( {\alpha }^{2} = 0 \) if \( m \) is odd and \( {\alpha }^{2} = {k\beta } \) if \( m = {2k} \) .

![bo_d7dtv0s91nqc73eq8nv0_217_1181_262_409_400_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_217_1181_262_409_400_0.jpg)

In particular, if \( m = 2, X \) is \( {\mathbb{{RP}}}^{2} \) and \( {\alpha }^{2} = \beta \) in \( {H}^{2}\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right) \) , as we showed already in Example 3.8.

The cup product formula \( \left( {\varphi  \smile  \psi }\right) \left( \sigma \right)  = \varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{k}}\right\rbrack  }\right) \psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{k + \ell }}\right\rbrack  }\right) \) also gives relative cup products

\[
{H}^{k}\left( {X;R}\right)  \times  {H}^{\ell }\left( {X, A;R}\right) \overset{ \smile  }{ \rightarrow  }{H}^{k + \ell }\left( {X, A;R}\right)
\]

\[
{H}^{k}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {X;R}\right) \overset{ \smile  }{ \rightarrow  }{H}^{k + \ell }\left( {X, A;R}\right)
\]

\[
{H}^{k}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {X, A;R}\right) \overset{ \smile  }{ \rightarrow  }{H}^{k + \ell }\left( {X, A;R}\right)
\]

since if \( \varphi \) or \( \psi \) vanishes on chains in \( A \) then so does \( \varphi  \smile  \psi \) . There is a more general relative cup product

\[
{H}^{k}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {X, B;R}\right)  \rightarrow  {H}^{k + \ell }\left( {X, A \cup  B;R}\right)
\]

when \( A \) and \( B \) are open subsets of \( X \) or subcomplexes of the CW complex \( X \) . This is obtained in the following way. The absolute cup product restricts to a cup product \( {C}^{k}\left( {X, A;R}\right)  \times  {C}^{\ell }\left( {X, B;R}\right)  \rightarrow  {C}^{k + \ell }\left( {X, A + B;R}\right) \) where \( {C}^{n}\left( {X, A + B;R}\right) \) is the subgroup of \( {C}^{n}\left( {X;R}\right) \) consisting of cochains vanishing on sums of chains in \( A \) and chains in \( B \) . If \( A \) and \( B \) are open in \( X \) , the inclusions \( {C}^{n}\left( {X, A \cup  B;R}\right)  \hookrightarrow  {C}^{n}\left( {X, A + B;R}\right) \) induce isomorphisms on cohomology, via the five-lemma and the fact that the restriction maps \( {C}^{n}\left( {A \cup  B;R}\right)  \rightarrow  {C}^{n}\left( {A + B;R}\right) \) induce isomorphisms on cohomology as we saw in the discussion of excision in the previous section. Therefore the cup product \( {C}^{k}\left( {X, A;R}\right)  \times  {C}^{\ell }\left( {X, B;R}\right)  \rightarrow  {C}^{k + \ell }\left( {X, A + B;R}\right) \) induces the desired relative cup product \( {H}^{k}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {X, B;R}\right)  \rightarrow  {H}^{k + \ell }\left( {X, A \cup  B;R}\right) \) . This holds also if \( X \) is a CW complex with \( A \) and \( B \) subcomplexes since here again the maps \( {C}^{n}\left( {A \cup  B;R}\right)  \rightarrow  {C}^{n}\left( {A + B;R}\right) \) induce isomorphisms on cohomology, as we saw for homology in §2.2.

Proposition 3.10. For a map \( f : X \rightarrow  Y \) , the induced maps \( {f}^{ * } : {H}^{n}\left( {Y;R}\right)  \rightarrow  {H}^{n}\left( {X;R}\right) \) satisfy \( {f}^{ * }\left( {\alpha  \smile  \beta }\right)  = {f}^{ * }\left( \alpha \right)  \smile  {f}^{ * }\left( \beta \right) \) , and similarly in the relative case.

Proof: This comes from the cochain formula \( {f}^{\sharp }\left( \varphi \right)  \smile  {f}^{\sharp }\left( \psi \right)  = {f}^{\sharp }\left( {\varphi  \smile  \psi }\right) \) :

\[
\left( {{f}^{\sharp }\varphi  \smile  {f}^{\sharp }\psi }\right) \left( \sigma \right)  = {f}^{\sharp }\varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{k}}\right\rbrack  }\right) {f}^{\sharp }\psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{k + \ell }}\right\rbrack  }\right)
\]

\[
= \varphi \left( {{f\sigma } \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{k}}\right\rbrack  }\right) \psi \left( {{f\sigma } \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{k + \ell }}\right\rbrack  }\right)
\]

\[
= \left( {\varphi  - \psi }\right) \left( {f\sigma }\right)  = {f}^{\sharp }\left( {\varphi  - \psi }\right) \left( \sigma \right)
\]

The natural question of whether the cup product is commutative is answered by the following:

Theorem 3.11. The identity \( \alpha  \smile  \beta  = {\left( -1\right) }^{k\ell }\beta  \smile  \alpha \) holds for all \( \alpha  \in  {H}^{k}\left( {X, A;R}\right) \) and \( \beta  \in  {H}^{\ell }\left( {X, A;R}\right) \) , when \( R \) is commutative.

Taking \( \alpha  = \beta \) , this implies in particular that if \( \alpha \) is an element of \( {H}^{k}\left( {X, A;R}\right) \) with \( k \) odd, then \( 2\left( {\alpha  - \alpha }\right)  = 0 \) in \( {H}^{2k}\left( {X, A;R}\right) \) , or more concisely, \( 2{\alpha }^{2} = 0 \) . Hence if \( {H}^{2k}\left( {X, A;R}\right) \) has no elements of order two, then \( {\alpha }^{2} = 0 \) . For example, if \( X \) is the 2-complex obtained by attaching a disk to \( {S}^{1} \) by a map of degree \( m \) as in Example 3.9 above, then we can deduce that the square of a generator of \( {H}^{1}\left( {X;{\mathbb{Z}}_{m}}\right) \) is zero if \( m \) is odd, and is either zero or the unique element of \( {H}^{2}\left( {X;{\mathbb{Z}}_{m}}\right)  \approx  {\mathbb{Z}}_{m} \) of order two if \( m \) is even. As we showed, the square is in fact nonzero when \( m \) is even.

Proof: Consider first the case \( A = \varnothing \) . For cochains \( \varphi  \in  {C}^{k}\left( {X;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {X;R}\right) \) one can see from the definition that the cup products \( \varphi  \smile  \psi \) and \( \psi  \smile  \varphi \) differ only by a permutation of the vertices of \( {\Delta }^{k + \ell } \) . The idea of the proof is to study a particularly nice permutation of vertices, namely the one that totally reverses their order. This has the convenient feature of also reversing the ordering of vertices in any face.

For a singular \( n \) -simplex \( \sigma  : \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack   \rightarrow  X \) , let \( \overline{\sigma } \) be the singular \( n \) -simplex obtained by preceding \( \sigma \) by the linear homeomorphism of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) reversing the order of the vertices. Thus \( \overline{\sigma }\left( {v}_{i}\right)  = \sigma \left( {v}_{n - i}\right) \) . This reversal of vertices is the product of \( n + \left( {n - 1}\right)  + \cdots  + 1 = n\left( {n + 1}\right) /2 \) transpositions of adjacent vertices, each of which reverses orientation of the \( n \) -simplex since it is a reflection across an \( \left( {n - 1}\right) \) -dimensional hyperplane. So to take orientations into account we would expect that a sign \( {\varepsilon }_{n} = {\left( -1\right) }^{n\left( {n + 1}\right) /2} \) ought to be inserted. Hence we define a homomorphism \( \rho  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) \) by \( \rho \left( \sigma \right)  = {\varepsilon }_{n}\overline{\sigma } \) .

We will show that \( \rho \) is a chain map, chain homotopic to the identity, so it induces the identity on cohomology. From this the theorem quickly follows. Namely, the formulas

\[
\left( {{\rho }^{ * }\varphi  - {\rho }^{ * }\psi }\right) \left( \sigma \right)  = \varphi \left( {{\varepsilon }_{k}\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{0}}\right\rbrack  }\right) \psi \left( {{\varepsilon }_{\ell }\sigma  \mid  \left\lbrack  {{v}_{k + \ell },\cdots ,{v}_{k}}\right\rbrack  }\right)
\]

\[
{\rho }^{ * }\left( {\psi  \smile  \varphi }\right) \left( \sigma \right)  = {\varepsilon }_{k + \ell }\psi \left( {\sigma  \mid  \left\lbrack  {{v}_{k + \ell },\cdots ,{v}_{k}}\right\rbrack  }\right) \varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{k},\cdots ,{v}_{0}}\right\rbrack  }\right)
\]

show that \( {\varepsilon }_{k}{\varepsilon }_{\ell }\left( {{\rho }^{ * }\varphi  - {\rho }^{ * }\psi }\right)  = {\varepsilon }_{k + \ell }{\rho }^{ * }\left( {\psi  - \varphi }\right) \) , since we assume \( R \) is commutative. A trivial calculation gives \( {\varepsilon }_{k + \ell } = {\left( -1\right) }^{k\ell }{\varepsilon }_{k}{\varepsilon }_{\ell } \) , hence \( {\rho }^{ * }\varphi  \smile  {\rho }^{ * }\psi  = {\left( -1\right) }^{k\ell }{\rho }^{ * }\left( {\psi  \smile  \varphi }\right) \) . Since \( \rho \) is chain homotopic to the identity, the \( {\rho }^{ * } \) ’s disappear when we pass to cohomology classes, and so we obtain the desired formula \( \alpha  \smile  \beta  = {\left( -1\right) }^{k\ell }\beta  \smile  \alpha \) .

The chain map property \( \partial \rho  = \rho \partial \) can be verified by calculating, for a singular \( n \) -simplex \( \sigma \) ,

\[
\partial \rho \left( \sigma \right)  = {\varepsilon }_{n}\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma  \mid  \left\lbrack  {{v}_{n},\cdots ,{\widehat{v}}_{n - i},\cdots ,{v}_{0}}\right\rbrack
\]

\[
\rho \partial \left( \sigma \right)  = \rho \left( {\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma \left| \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack  \right) }\right.
\]

\[
= {\varepsilon }_{n - 1}\mathop{\sum }\limits_{i}{\left( -1\right) }^{n - i}\sigma  \mid  \left\lbrack  {{v}_{n},\cdots ,{\widehat{v}}_{n - i},\cdots ,{v}_{0}}\right\rbrack
\]

so the result follows from the easily checked identity \( {\varepsilon }_{n} = {\left( -1\right) }^{n}{\varepsilon }_{n - 1} \) .

To define a chain homotopy between \( \rho \) and the identity we are motivated by the construction of the prism operator \( P \) in the proof that homotopic maps induce the same homomorphism on homology, in Theorem 2.10. The main ingredient in the construction of \( P \) was a subdivision of \( {\Delta }^{n} \times  I \) into \( \left( {n + 1}\right) \) -simplices with vertices \( {v}_{i} \) in \( {\Delta }^{n} \times  \{ 0\} \) and \( {w}_{i} \) in \( {\Delta }^{n} \times  \{ 1\} \) , the vertex \( {w}_{i} \) lying directly above \( {v}_{i} \) . Using the same subdivision, and letting \( \pi  : {\Delta }^{n} \times  I \rightarrow  {\Delta }^{n} \) be the projection, we now define \( P : {C}_{n}\left( X\right)  \rightarrow  {C}_{n + 1}\left( X\right) \) by

\[
P\left( \sigma \right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\varepsilon }_{n - i}\left( {\sigma \pi }\right) \left| \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{n},\cdots ,{w}_{i}}\right\rbrack  \right|
\]

Thus the \( w \) -vertices are written in reverse order, and there is a compensating sign \( {\varepsilon }_{n - i} \) . One can view this formula as arising from the \( \Delta \) -complex structure on \( {\Delta }^{n} \times  I \) in which the vertices are ordered \( {v}_{0},\cdots ,{v}_{n},{w}_{n},\cdots ,{w}_{0} \) rather than the more natural ordering \( {v}_{0},\cdots ,{v}_{n},{w}_{0},\cdots ,{w}_{n} \) .

To show \( \partial P + P\partial  = \rho  - \mathbb{1} \) we first calculate \( \partial P \) , leaving out \( \sigma \) ’s and \( {\sigma \pi } \) ’s for notational simplicity:

\[
\partial P = \mathop{\sum }\limits_{{j \leq  i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}{\varepsilon }_{n - i}\left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{i},{w}_{n},\cdots ,{w}_{i}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{j \geq  i}}{\left( -1\right) }^{i}{\left( -1\right) }^{i + 1 + n - j}{\varepsilon }_{n - i}\left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{n},\cdots ,{\widehat{w}}_{j},\cdots ,{w}_{i}}\right\rbrack
\]

The \( j = i \) terms in these two sums give

\[
{\varepsilon }_{n}\left\lbrack  {{w}_{n},\cdots ,{w}_{0}}\right\rbrack   + \mathop{\sum }\limits_{{i > 0}}{\varepsilon }_{n - i}\left\lbrack  {{v}_{0},\cdots ,{v}_{i - 1},{w}_{n},\cdots ,{w}_{i}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{i < n}}{\left( -1\right) }^{n + i + 1}{\varepsilon }_{n - i}\left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{n},\cdots ,{w}_{i + 1}}\right\rbrack   - \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack
\]

In this expression the two summation terms cancel since replacing \( i \) by \( i - 1 \) in the second sum produces a new sign \( {\left( -1\right) }^{n + i}{\varepsilon }_{n - i + 1} =  - {\varepsilon }_{n - i} \) . The remaining two terms \( {\varepsilon }_{n}\left\lbrack  {{w}_{n},\cdots ,{w}_{0}}\right\rbrack \) and \( - \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) represent \( \rho \left( \sigma \right)  - \sigma \) . So in order to show that \( \partial P + P\partial  = \rho  - \mathbb{1} \) , it remains to check that in the formula for \( \partial P \) above, the terms with \( j \neq  i \) give \( - P\partial \) . Calculating \( P\partial \) from the definitions, we have

\[
P\partial  = \mathop{\sum }\limits_{{i < j}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}{\varepsilon }_{n - i - 1}\left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{n},\cdots ,{\widehat{w}}_{j},\cdots ,{w}_{i}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{i > j}}{\left( -1\right) }^{i - 1}{\left( -1\right) }^{j}{\varepsilon }_{n - i}\left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{i},{w}_{n},\cdots ,{w}_{i}}\right\rbrack
\]

Since \( {\varepsilon }_{n - i} = {\left( -1\right) }^{n - i}{\varepsilon }_{n - i - 1} \) , this finishes the verification that \( \partial P + P\partial  = \rho  - \mathbb{1} \) , and so the theorem is proved when \( A = \varnothing \) . The proof also applies when \( A \neq  \varnothing \) since the maps \( \rho \) and \( P \) take chains in \( A \) to chains in \( A \) , so the dual homomorphisms \( {\rho }^{ * } \) and \( {P}^{ * } \) act on relative cochains.

## The Cohomology Ring

Since cup product is associative and distributive, it is natural to try to make it the multiplication in a ring structure on the cohomology groups of a space \( X \) . This is easy to do if we simply define \( {H}^{ * }\left( {X;R}\right) \) to be the direct sum of the groups \( {H}^{n}\left( {X;R}\right) \) . Elements of \( {H}^{ * }\left( {X;R}\right) \) are finite sums \( \mathop{\sum }\limits_{i}{\alpha }_{i} \) with \( {\alpha }_{i} \in  {H}^{i}\left( {X;R}\right) \) , and the product of two such sums is defined to be \( \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right) \left( {\mathop{\sum }\limits_{j}{\beta }_{j}}\right)  = \mathop{\sum }\limits_{{i, j}}{\alpha }_{i}{\beta }_{j} \) . It is routine to check that this makes \( {H}^{ * }\left( {X;R}\right) \) into a ring, with identity if \( R \) has an identity. Similarly, \( {H}^{ * }\left( {X, A;R}\right) \) is a ring via the relative cup product. Taking scalar multiplication by elements of \( R \) into account, these rings can also be regarded as \( R \) -algebras.

For example, the calculations in Example 3.8 or 3.9 above show that \( {H}^{ * }\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right) \) consists of the polynomials \( {a}_{0} + {a}_{1}\alpha  + {a}_{2}{\alpha }^{2} \) with coefficients \( {a}_{i} \in  {\mathbb{Z}}_{2} \) , so \( {H}^{ * }\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right) \) is the quotient \( {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{3}\right) \) of the polynomial ring \( {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack \) by the ideal generated by \( {\alpha }^{3} \) .

This example illustrates how \( {H}^{ * }\left( {X;R}\right) \) often has a more compact description than the sequence of individual groups \( {H}^{n}\left( {X;R}\right) \) , so there is a certain economy in the change of scale that comes from regarding all the groups \( {H}^{n}\left( {X;R}\right) \) as part of a single object \( {H}^{ * }\left( {X;R}\right) \) .

Adding cohomology classes of different dimensions to form \( {H}^{ * }\left( {X;R}\right) \) is a convenient formal device, but it has little topological significance. One always regards the cohomology ring as a graded ring: a ring \( A \) with a decomposition as a sum \( {\bigoplus }_{k \geq  0}{A}_{k} \) of additive subgroups \( {A}_{k} \) such that the multiplication takes \( {A}_{k} \times  {A}_{\ell } \) to \( {A}_{k + \ell } \) . To indicate that an element \( a \in  A \) lies in \( {A}_{k} \) we write \( \left| a\right|  = k \) . This applies in particular to elements of \( {H}^{k}\left( {X;R}\right) \) . Some authors call \( \left| a\right| \) the ’degree’ of \( a \) , but we will use the term 'dimension' which is more geometric and avoids potential confusion with the degree of a polynomial.

A graded ring satisfying the commutativity property of Theorem 3.11, \( {ab} = \; {\left( -1\right) }^{\left| a\right| \left| b\right| }{ba} \) , is usually called simply commutative in the context of algebraic topology, in spite of the potential for misunderstanding. In the older literature one finds less ambiguous terms such as graded commutative, anticommutative, or skew commutative.

Example 3.12: Polynomial Rings. Among the simplest graded rings are polynomial rings \( R\left\lbrack  \alpha \right\rbrack \) and their truncated versions \( R\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n}\right) \) , consisting of polynomials of degree less than \( n \) . The example we have seen is \( {H}^{ * }\left( {{\mathbb{{RP}}}^{2};{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{3}\right) \) . More generally we will show in Theorem 3.19 that \( {H}^{ * }\left( {{\mathbb{{RP}}}^{n};{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) \) and \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack \) . In these cases \( \left| \alpha \right|  = 1 \) . We will also show that \( {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right)  \approx \; \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) \) and \( {H}^{ * }\left( {{\mathbb{{CP}}}^{\infty };\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack \) with \( \left| \alpha \right|  = 2 \) . The analogous results for quaternionic projective spaces are also valid, with \( \left| \alpha \right|  = 4 \) . The coefficient ring \( \mathbb{Z} \) in the complex and quaternionic cases could be replaced by any commutative ring \( R \) , but not for \( {\mathbb{{RP}}}^{n} \) and \( {\mathbb{{RP}}}^{\infty } \) since a polynomial ring \( R\left\lbrack  \alpha \right\rbrack \) is strictly commutative, so for this to be a commutative ring in the graded sense we must have either \( \left| \alpha \right| \) even or \( 2 = 0 \) in \( R \) .

Polynomial rings in several variables also have graded ring structures, and these graded rings can sometimes be realized as cohomology rings of spaces. For example, \( {\mathbb{Z}}_{2}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) is \( {H}^{ * }\left( {X;{\mathbb{Z}}_{2}}\right) \) for \( X \) the product of \( n \) copies of \( {\mathbb{{RP}}}^{\infty } \) , with \( \left| {\alpha }_{i}\right|  = 1 \) for each \( i \) , as we will see in Example 3.20.

Example 3.13: Exterior Algebras. Another nice example of a commutative graded ring is the exterior algebra \( {\Lambda }_{R}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) over a commutative ring \( R \) with identity. This is the free \( R \) -module with basis the finite products \( {\alpha }_{{i}_{1}}\cdots {\alpha }_{{i}_{k}},{i}_{1} < \cdots  < {i}_{k} \) , with associative, distributive multiplication defined by the rules \( {\alpha }_{i}{\alpha }_{j} =  - {\alpha }_{j}{\alpha }_{i} \) for \( i \neq  j \) and \( {\alpha }_{i}^{2} = 0 \) . The empty product of \( {\alpha }_{i} \) ’s is allowed, and provides an identity element 1 in \( {\Lambda }_{R}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) . The exterior algebra becomes a commutative graded ring by specifying odd dimensions for the generators \( {\alpha }_{i} \) .

The example we have seen is the torus \( {T}^{2} = {S}^{1} \times  {S}^{1} \) , where \( {H}^{ * }\left( {{T}^{2};\mathbb{Z}}\right)  \approx  {\Lambda }_{\mathbb{Z}}\left\lbrack  {\alpha ,\beta }\right\rbrack \) with \( \left| \alpha \right|  = \left| \beta \right|  = 1 \) by the calculations in Example 3.7. More generally, for the \( n \) -torus \( {T}^{n},{H}^{ * }\left( {{T}^{n};R}\right) \) is the exterior algebra \( {\Lambda }_{R}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) as we will see in Example 3.16. The same is true for any product of odd-dimensional spheres, where \( \left| {\alpha }_{i}\right| \) is the dimension of the \( {i}^{\text{ th }} \) sphere.

Induced homomorphisms are ring homomorphisms by Proposition 3.10. Here is an example illustrating this fact.

Example 3.14: Product Rings. The isomorphism \( {H}^{ * }\left( {\mathop{\coprod }\limits_{\alpha }{X}_{\alpha };R}\right) \overset{ \approx  }{ \rightarrow  }\mathop{\prod }\limits_{\alpha }{H}^{ * }\left( {{X}_{\alpha };R}\right) \) whose coordinates are induced by the inclusions \( {i}_{\alpha } : {X}_{\alpha } \hookrightarrow  \mathop{\coprod }\limits_{\alpha }{X}_{\alpha } \) is a ring isomorphism with respect to the usual coordinatewise multiplication in a product ring, because each coordinate function \( {i}_{\alpha }^{ * } \) is a ring homomorphism. Similarly for a wedge sum the isomorphism \( {\widetilde{H}}^{ * }\left( {\mathop{\bigvee }\limits_{\alpha }{X}_{\alpha };R}\right)  \approx  \mathop{\prod }\limits_{\alpha }{\widetilde{H}}^{ * }\left( {{X}_{\alpha };R}\right) \) is a ring isomorphism. Here we take reduced cohomology to be cohomology relative to a basepoint, and we use relative cup products. We should assume the basepoints \( {x}_{\alpha } \in  {X}_{\alpha } \) are deformation retracts of neighborhoods, to be sure that the claimed isomorphism does indeed hold.

This product ring structure for wedge sums can sometimes be used to rule out splittings of a space as a wedge sum up to homotopy equivalence. For example, consider \( {\mathbb{{CP}}}^{2} \) , which is \( {S}^{2} \) with a cell \( {e}^{4} \) attached by a certain map \( f : {S}^{3} \rightarrow  {S}^{2} \) . Using homology or just the additive structure of cohomology it is impossible to conclude that \( {\mathbb{{CP}}}^{2} \) is not homotopy equivalent to \( {S}^{2} \vee  {S}^{4} \) , and hence that \( f \) is not homotopic to a constant map. However, with cup products we can distinguish these two spaces since the square of each element of \( {H}^{2}\left( {{S}^{2} \vee  {S}^{4};\mathbb{Z}}\right) \) is zero in view of the ring isomorphism \( {\widetilde{H}}^{ * }\left( {{S}^{2} \vee  {S}^{4};\mathbb{Z}}\right)  \approx  {\widetilde{H}}^{ * }\left( {{S}^{2};\mathbb{Z}}\right)  \oplus  {\widetilde{H}}^{ * }\left( {{S}^{4};\mathbb{Z}}\right) \) , but the square of a generator of \( {H}^{2}\left( {{\mathbb{{CP}}}^{2};\mathbb{Z}}\right) \) is nonzero since \( {H}^{ * }\left( {{\mathbb{{CP}}}^{2};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{3}\right) \) .

More generally, cup products can be used to distinguish infinitely many different homotopy classes of maps \( {S}^{{4n} - 1} \rightarrow  {S}^{2n} \) for all \( n \geq  1 \) . This is systematized in the notion of the Hopf invariant, which is studied in §4.B.

Here is the evident general question raised by the preceding examples:

The Realization Problem. Which graded commutative \( R \) -algebras occur as cup product algebras \( {H}^{ * }\left( {X;R}\right) \) of spaces \( X \) ?

This is a difficult problem, with the degree of difficulty depending strongly on the coefficient ring \( R \) . The most accessible case is \( R = \mathbb{Q} \) , where essentially every graded commutative Q-algebra is realizable, as shown in [Quillen 1969]. Next in order of difficulty is \( R = {\mathbb{Z}}_{p} \) with \( p \) prime. This is much harder than the case of \( \mathbb{Q} \) , and only partial results, obtained with much labor, are known. Finally there is \( R = \mathbb{Z} \) , about which very little is known beyond what is implied by the \( {\mathbb{Z}}_{p} \) cases.

## A Künneth Formula

One might guess that there should be some connection between cup product and product spaces, and indeed this is the case, as we will show in this subsection.

To begin, we define the cross product, or external cup product as it is sometimes called. This is the map

\[
{H}^{ * }\left( {X;R}\right)  \times  {H}^{ * }\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{H}^{ * }\left( {X \times  Y;R}\right)
\]

given by \( a \times  b = {p}_{1}^{ * }\left( a\right)  \smile  {p}_{2}^{ * }\left( b\right) \) where \( {p}_{1} \) and \( {p}_{2} \) are the projections of \( X \times  Y \) onto \( X \) and \( Y \) . Since cup product is distributive, the cross product is bilinear, that is, linear in each variable separately. We might hope that the cross product map would be an isomorphism in many cases, thereby giving a nice description of the cohomology rings of these product spaces. However, a bilinear map is rarely a homomorphism, so it could hardly be an isomorphism. Fortunately there is a nice algebraic solution to this problem, and that is to replace the direct product \( {H}^{ * }\left( {X;R}\right)  \times  {H}^{ * }\left( {Y;R}\right) \) by the tensor product \( {H}^{ * }\left( {X;R}\right) { \otimes  }_{R}{H}^{ * }\left( {Y;R}\right) \) .

Let us review the definition and basic properties of tensor products. For abelian groups \( A \) and \( B \) the tensor product \( A \otimes  B \) is defined to be the abelian group with generators \( a \otimes  b \) for \( a \in  A, b \in  B \) , and relations \( \left( {a + {a}^{\prime }}\right)  \otimes  b = a \otimes  b + {a}^{\prime } \otimes  b \) and \( a \otimes  \left( {b + {b}^{\prime }}\right)  = a \otimes  b + a \otimes  {b}^{\prime } \) . So the zero element of \( A \otimes  B \) is \( 0 \otimes  0 = 0 \otimes  b = a \otimes  0 \) , and \( - \left( {a \otimes  b}\right)  =  - a \otimes  b = a \otimes  \left( {-b}\right) \) . Some readily verified elementary properties are:

(1) \( A \otimes  B \approx  B \otimes  A \) .

(2) \( \left( {{\bigoplus }_{i}{A}_{i}}\right)  \otimes  B \approx  {\bigoplus }_{i}\left( {{A}_{i} \otimes  B}\right) \) .

(3) \( \left( {A \otimes  B}\right)  \otimes  C \approx  A \otimes  \left( {B \otimes  C}\right) \) .

(4) \( \mathbb{Z} \otimes  A \approx  A \) .

(5) \( {\mathbb{Z}}_{n} \otimes  A \approx  A/{nA} \) .

(6) A pair of homomorphisms \( f : A \rightarrow  {A}^{\prime } \) and \( g : B \rightarrow  {B}^{\prime } \) induces a homomorphism \( f \otimes  g : A \otimes  B \rightarrow  {A}^{\prime } \otimes  {B}^{\prime } \) via \( \left( {f \otimes  g}\right) \left( {a \otimes  b}\right)  = f\left( a\right)  \otimes  g\left( b\right) \) .

(7) A bilinear map \( \varphi  : A \times  B \rightarrow  C \) induces a homomorphism \( A \otimes  B \rightarrow  C \) sending \( a \otimes  b \) to \( \varphi \left( {a, b}\right) \) .

In (1)-(5) the isomorphisms are the obvious ones, for example \( a \otimes  b \mapsto  b \otimes  a \) in (1) and \( n \otimes  a \mapsto  {na} \) in (4). Properties (1),(2),(4), and (5) allow the calculation of tensor products of finitely generated abelian groups.

The generalization to tensor products of modules over a commutative ring \( R \) is easy. One defines \( A{ \otimes  }_{R}B \) for \( R \) -modules \( A \) and \( B \) to be the quotient of \( A \otimes  B \) obtained by imposing the further relations \( {ra} \otimes  b = a \otimes  {rb} \) for \( r \in  R, a \in  A \) , and \( b \in  B \) . This relation guarantees that \( A{ \otimes  }_{R}B \) is again an \( R \) -module. In case \( R \) is not commutative, one assumes \( A \) is a right \( R \) -module and \( B \) is a left \( R \) -module, and the relation is written instead \( {ar} \otimes  b = a \otimes  {rb} \) , but now \( A{ \otimes  }_{R}B \) is only an abelian group, not an \( R \) -module. However, we will restrict attention to the case that \( R \) is commutative in what follows.

It is an easy algebra exercise to see that \( A{ \otimes  }_{R}B = A \otimes  B \) when \( R \) is \( {\mathbb{Z}}_{m} \) or \( \mathbb{Q} \) . But in general \( A{ \otimes  }_{R}B \) is not the same as \( A \otimes  B \) . For example, if \( R = \mathbb{Q}\left( \sqrt{2}\right) \) , which is a 2-dimensional vector space over \( \mathbb{Q} \) , then \( R{ \otimes  }_{R}R = R \) but \( R \otimes  R \) is a 4-dimensional vector space over \( \mathbb{Q} \) .

The statements (1)-(3), (6), and (7) remain valid for tensor products of \( R \) -modules. The generalization of (4) is the canonical isomorphism \( R{ \otimes  }_{R}A \approx  A, r \otimes  a \mapsto  {ra} \) .

Property (7) of tensor products guarantees that the cross product as defined above gives rise to a homomorphism of \( R \) -modules

\[
{H}^{ * }\left( {X;R}\right) { \otimes  }_{R}{H}^{ * }\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{H}^{ * }\left( {X \times  Y;R}\right) ,\;a \otimes  b \mapsto  a \times  b
\]

which we shall also call cross product. This map becomes a ring homomorphism if we define the multiplication in a tensor product of graded rings by \( \left( {a \otimes  b}\right) \left( {c \otimes  d}\right)  = \; {\left( -1\right) }^{\left| b\right| \left| c\right| }{ac} \otimes  {bd} \) where \( \left| x\right| \) denotes the dimension of \( x \) . Namely, if we denote the cross product map by \( \mu \) and we define \( \left( {a \otimes  b}\right) \left( {c \otimes  d}\right)  = {\left( -1\right) }^{\left| b\right| \left| c\right| }{ac} \otimes  {bd} \) , then

\[
\mu \left( {\left( {a \otimes  b}\right) \left( {c \otimes  d}\right) }\right)  = {\left( -1\right) }^{\left| b\right| \left| c\right| }\mu \left( {{ac} \otimes  {bd}}\right)
\]

\[
= {\left( -1\right) }^{\left| b\right| \left| c\right| }\left( {a \smile  c}\right)  \times  \left( {b \smile  d}\right)
\]

\[
= {\left( -1\right) }^{\left| b\right| \left| c\right| }{p}_{1}^{ * }\left( {a \smile  c}\right)  \smile  {p}_{2}^{ * }\left( {b \smile  d}\right)
\]

\[
= {\left( -1\right) }^{\left| b\right| \left| c\right| }{p}_{1}^{ * }\left( a\right)  \smile  {p}_{1}^{ * }\left( c\right)  \smile  {p}_{2}^{ * }\left( b\right)  \smile  {p}_{2}^{ * }\left( d\right)
\]

\[
= {p}_{1}^{ * }\left( a\right)  \smile  {p}_{2}^{ * }\left( b\right)  \smile  {p}_{1}^{ * }\left( c\right)  \smile  {p}_{2}^{ * }\left( d\right)
\]

\[
= \left( {a \times  b}\right) \left( {c \times  d}\right)  = \mu \left( {a \otimes  b}\right) \mu \left( {c \otimes  d}\right)
\]

Theorem 3.15. The cross product \( {H}^{ * }\left( {X;R}\right) { \otimes  }_{R}{H}^{ * }\left( {Y;R}\right)  \rightarrow  {H}^{ * }\left( {X \times  Y;R}\right) \) is an isomorphism of rings if \( X \) and \( Y \) are CW complexes and \( {H}^{k}\left( {Y;R}\right) \) is a finitely generated free R-module for all \( k \) .

Results of this type, computing homology or cohomology of a product space, are known as Künneth formulas. The hypothesis that \( X \) and \( Y \) are CW complexes will be shown to be unnecessary in §4.1 when we consider CW approximations to arbitrary spaces. On the other hand, the freeness hypothesis cannot always be dispensed with, as we shall see in §3.B when we obtain a completely general Künneth formula for the homology of a product space.

When the conclusion of the theorem holds, the ring structure in \( {H}^{ * }\left( {X \times  Y;R}\right) \) is determined by the ring structures in \( {H}^{ * }\left( {X;R}\right) \) and \( {H}^{ * }\left( {Y;R}\right) \) . Example 3E.6 shows that some hypotheses are necessary in order for this to be true.

Example 3.16. The exterior algebra \( {\Lambda }_{R}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) is the graded tensor product over \( R \) of the one-variable exterior algebras \( {\Lambda }_{R}\left\lbrack  {\alpha }_{i}\right\rbrack \) where the \( {\alpha }_{i} \) ’s have odd dimension. The Künneth formula then gives an isomorphism \( {H}^{ * }\left( {{S}^{{k}_{1}} \times  \cdots  \times  {S}^{{k}_{n}};\mathbb{Z}}\right)  \approx \; {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) if the dimensions \( {k}_{i} \) are all odd. With some \( {k}_{i} \) ’s even, one would have the tensor product of an exterior algebra for the odd-dimensional spheres and truncated polynomial rings \( \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{2}\right) \) for the even-dimensional spheres. Of course, \( {\Lambda }_{\mathbb{Z}}\left\lbrack  \alpha \right\rbrack \) and \( \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{2}\right) \) are isomorphic as rings, but when one takes tensor products in the graded sense it becomes important to distinguish them as graded rings, with \( \alpha \) odd-dimensional in \( {\Lambda }_{\mathbb{Z}}\left\lbrack  \alpha \right\rbrack \) and even-dimensional in \( \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{2}\right) \) . These remarks apply more generally with any coefficient ring \( R \) in place of \( \mathbb{Z} \) , though when \( R = {\mathbb{Z}}_{2} \) there is no need to distinguish between the odd-dimensional and even-dimensional cases since signs become irrelevant.

The idea of the proof of the theorem will be to consider, for a fixed CW complex \( Y \) , the functors

\[
{h}^{n}\left( {X, A}\right)  = {\bigoplus }_{i}\left( {{H}^{i}\left( {X, A;R}\right) { \otimes  }_{R}{H}^{n - i}\left( {Y;R}\right) }\right)
\]

\[
{k}^{n}\left( {X, A}\right)  = {H}^{n}\left( {X \times  Y, A \times  Y;R}\right)
\]

The cross product, or a relative version of it, defines a map \( \mu  : {h}^{n}\left( {X, A}\right)  \rightarrow  {k}^{n}\left( {X, A}\right) \) which we would like to show is an isomorphism when \( X \) is a CW complex and \( A = \varnothing \) . We will show:

(1) \( {h}^{ * } \) and \( {k}^{ * } \) are cohomology theories on the category of CW pairs.

(2) \( \mu \) is a natural transformation: It commutes with induced homomorphisms and with coboundary homomorphisms in long exact sequences of pairs.

It is obvious that \( \mu  : {h}^{n}\left( X\right)  \rightarrow  {k}^{n}\left( X\right) \) is an isomorphism when \( X \) is a point since it is just the scalar multiplication map \( R{ \otimes  }_{R}{H}^{n}\left( {Y;R}\right)  \rightarrow  {H}^{n}\left( {Y;R}\right) \) . The following general fact will then imply the theorem.

Proposition 3.17. If a natural transformation between unreduced cohomology theories on the category of CW pairs is an isomorphism when the CW pair is (point, \( \varnothing \) ), then it is an isomorphism for all CW pairs.

Proof: Let \( \mu  : {h}^{ * }\left( {X, A}\right)  \rightarrow  {k}^{ * }\left( {X, A}\right) \) be the natural transformation. By the five-lemma it will suffice to show that \( \mu \) is an isomorphism when \( A = \varnothing \) .

First we do the case of finite-dimensional \( X \) by induction on dimension. The induction starts with the case that \( X \) is 0-dimensional, where the result holds by hypothesis and by the axiom for disjoint unions. For the induction step, \( \mu \) gives a map between the two long exact sequences for the pair \( \left( {{X}^{n},{X}^{n - 1}}\right) \) , with commuting squares since \( \mu \) is a natural transformation. The five-lemma reduces the inductive step to showing that \( \mu \) is an isomorphism for \( \left( {X, A}\right)  = \left( {{X}^{n},{X}^{n - 1}}\right) \) . Let \( \Phi  : \mathop{\coprod }\limits_{\alpha }\left( {{D}_{\alpha }^{n},\partial {D}_{\alpha }^{n}}\right)  \rightarrow  \left( {{X}^{n},{X}^{n - 1}}\right) \) be a collection of characteristic maps for all the \( n \) -cells of \( X \) . By excision, \( {\Phi }^{ * } \) is an isomorphism for \( {h}^{ * } \) and \( {k}^{ * } \) , so by naturality it suffices to show that \( \mu \) is an isomorphism for \( \left( {X, A}\right)  = \mathop{\coprod }\limits_{\alpha }\left( {{D}_{\alpha }^{n},\partial {D}_{\alpha }^{n}}\right) \) . The axiom for disjoint unions gives a further reduction to the case of the pair \( \left( {{D}^{n},\partial {D}^{n}}\right) \) . Finally, this case follows by applying the five-lemma to the long exact sequences of this pair, since \( {D}^{n} \) is contractible and hence is covered by the 0 -dimensional case, and \( \partial {D}^{n} \) is \( \left( {n - 1}\right) \) -dimensional.

The case that \( X \) is infinite-dimensional reduces to the finite-dimensional case by a telescope argument as in the proof of Lemma 2.34. We leave this for the reader since the finite-dimensional case suffices for the special \( {h}^{ * } \) and \( {k}^{ * } \) we are considering, as the maps \( {h}^{i}\left( X\right)  \rightarrow  {h}^{i}\left( {X}^{n}\right) \) and \( {k}^{i}\left( X\right)  \rightarrow  {k}^{i}\left( {X}^{n}\right) \) induced by the inclusion \( {X}^{n} \hookrightarrow  X \) are isomorphisms when \( n \) is sufficiently large with respect to \( i \) .

Proof of 3.15: It remains to check that \( {h}^{ * } \) and \( {k}^{ * } \) are cohomology theories, and that \( \mu \) is a natural transformation. Since we are dealing with unreduced cohomology theories there are four axioms to verify.

(1) Homotopy invariance: \( f \simeq  g \) implies \( {f}^{ * } = {g}^{ * } \) . This is obvious for both \( {h}^{ * } \) and \( {k}^{ * } \) .

(2) Excision: \( {h}^{ * }\left( {X, A}\right)  \approx  {h}^{ * }\left( {B, A \cap  B}\right) \) for \( A \) and \( B \) subcomplexes of the CW complex \( X = A \cup  B \) . This is obvious, and so is the corresponding statement for \( {k}^{ * } \) since \( \left( {A \times  Y}\right)  \cup  \left( {B \times  Y}\right)  = \left( {A \cup  B}\right)  \times  Y \) and \( \left( {A \times  Y}\right)  \cap  \left( {B \times  Y}\right)  = \left( {A \cap  B}\right)  \times  Y. \)

(3) The long exact sequence of a pair. This is a triviality for \( {k}^{ * } \) , but a few words of explanation are needed for \( {h}^{ * } \) , where the desired exact sequence is obtained in two steps. For the first step, tensor the long exact sequence of ordinary cohomology groups for a pair \( \left( {X, A}\right) \) with the free \( R \) -module \( {H}^{n}\left( {Y;R}\right) \) , for a fixed \( n \) . This yields another exact sequence because \( {H}^{n}\left( {Y;R}\right) \) is a direct sum of copies of \( R \) , so the result of tensoring an exact sequence with this direct sum is simply to produce a direct sum of copies of the exact sequence, which is again an exact sequence. The second step is to let \( n \) vary, taking a direct sum of the previously constructed exact sequences for each \( n \) , with the \( {n}^{\text{ th }} \) exact sequence shifted up by \( n \) dimensions.

(4) Disjoint unions. Again this axiom obviously holds for \( {k}^{ * } \) , but some justification is required for \( {h}^{ * } \) . What is needed is the algebraic fact that there is a canonical isomorphism \( \left( {\mathop{\prod }\limits_{\alpha }{M}_{\alpha }}\right) { \otimes  }_{R}N \approx  \mathop{\prod }\limits_{\alpha }\left( {{M}_{\alpha }{ \otimes  }_{R}N}\right) \) for \( R \) -modules \( {M}_{\alpha } \) and a finitely generated free \( R \) -module \( N \) . Since \( N \) is a direct product of finitely many copies \( {R}_{\beta } \) of \( R,{M}_{\alpha }{ \otimes  }_{R}N \) is a direct product of corresponding copies \( {M}_{\alpha \beta } = {M}_{\alpha }{ \otimes  }_{R}{R}_{\beta } \) of \( {M}_{\alpha } \) and the desired relation becomes \( \mathop{\prod }\limits_{\beta }\mathop{\prod }\limits_{\alpha }{M}_{\alpha \beta } \approx  \mathop{\prod }\limits_{\alpha }\mathop{\prod }\limits_{\beta }{M}_{\alpha \beta } \) , which is obviously true.

Finally there is naturality of \( \mu \) to consider. Naturality with respect to maps between spaces is immediate from the naturality of cup products. Naturality with respect to coboundary maps in long exact sequences is commutativity of the following square:

\[
{H}^{k}\left( {A;R}\right)  \times  {H}^{\ell }\left( {Y;R}\right) \xrightarrow[]{\delta  \times  \mathbb{1}}{H}^{k + 1}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {Y;R}\right)
\]

\[
{H}^{k + \ell }\left( {A \times  Y;R}\right)  \rightarrow  {H}^{k + \ell  + 1}\left( {X \times  Y, A \times  Y;R}\right)
\]

To check this, start with an element of the upper left product, represented by cocycles \( \varphi  \in  {C}^{k}\left( {A;R}\right) \) and \( \psi  \in  {C}^{\ell }\left( {Y;R}\right) \) . Extend \( \varphi \) to a cochain \( \overline{\varphi } \in  {C}^{k}\left( {X;R}\right) \) . Then the pair \( \left( {\varphi ,\psi }\right) \) maps rightward to \( \left( {\delta \overline{\varphi },\psi }\right) \) and then downward to \( {p}_{1}^{\sharp }\left( {\delta \overline{\varphi }}\right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) \) . Going the other way around the square, \( \left( {\varphi ,\psi }\right) \) maps downward to \( {p}_{1}^{\sharp }\left( \varphi \right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) \) and then rightward to \( \delta \left( {{p}_{1}^{\sharp }\left( \overline{\varphi }\right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) }\right) \) since \( {p}_{1}^{\sharp }\left( \overline{\varphi }\right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) \) extends \( {p}_{1}^{\sharp }\left( \varphi \right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) \) over \( X \times  Y \) . Finally, \( \delta \left( {{p}_{1}^{\sharp }\left( \overline{\varphi }\right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) }\right)  = {p}_{1}^{\sharp }\left( {\delta \overline{\varphi }}\right)  \smile  {p}_{2}^{\sharp }\left( \psi \right) \) since \( {\delta \psi } = 0 \) .

It is sometimes important to have a relative version of the Künneth formula in Theorem 3.15. The relative cross product is

\[
{H}^{ * }\left( {X, A;R}\right) { \otimes  }_{R}{H}^{ * }\left( {Y, B;R}\right) \overset{ \times  }{ \rightarrow  }{H}^{ * }\left( {X \times  Y, A \times  Y \cup  X \times  B;R}\right)
\]

for CW pairs \( \left( {X, A}\right) \) and \( \left( {Y, B}\right) \) , defined just as in the absolute case by \( a \times  b = \; {p}_{1}^{ * }\left( a\right)  \smile  {p}_{2}^{ * }\left( b\right) \) where \( {p}_{1}^{ * }\left( a\right)  \in  {H}^{ * }\left( {X \times  Y, A \times  Y;R}\right) \) and \( {p}_{2}^{ * }\left( b\right)  \in  {H}^{ * }\left( {X \times  Y, X \times  B;R}\right) . \)

Theorem 3.18. For CW pairs \( \left( {X, A}\right) \) and \( \left( {Y, B}\right) \) the cross product homomorphism

Proof: The case \( B = \varnothing \) was covered in the course of the proof of the absolute case, so it suffices to deduce the case \( B \neq  \varnothing \) from the case \( B = \varnothing \) .

The following commutative diagram shows that collapsing \( B \) to a point reduces the proof to the case that \( B \) is a point:

\[
{H}^{ * }\left( {X, A}\right) { \otimes  }_{R}{H}^{ * }\left( {Y, B}\right)  \leftarrow   = {H}^{ * }\left( {X, A}\right) { \otimes  }_{R}{H}^{ * }\left( {Y/B, B/B}\right)
\]

\[
\downarrow   \times  \; \downarrow   \times
\]

\[
{H}^{ * }\left( {X \times  Y, A \times  Y \cup  X \times  B}\right)  \leftarrow  {H}^{ * }\left( {X \times  \left( {Y/B}\right) , A \times  \left( {Y/B}\right)  \cup  X \times  \left( {B/B}\right) }\right)
\]

The lower map is an isomorphism since the quotient spaces \( \left( {X \times  Y}\right) /\left( {A \times  Y \cup  X \times  B}\right) \) and \( \left( {X \times  \left( {Y/B}\right) }\right) /\left( {A \times  \left( {Y/B}\right)  \cup  X \times  \left( {B/B}\right) }\right) \) are the same.

In the case that \( B \) is a point \( {y}_{0} \in  Y \) , consider the commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_227_229_891_1335_232_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_227_229_891_1335_232_0.jpg)

\( {H}^{ * }\left( {X \times  Y, X \times  {\mathcal{Y}}_{0} \cup  A \times  Y}\right)  \rightarrow  {H}^{ * }\left( {X \times  Y, A \times  Y}\right)  \rightarrow  {H}^{ * }\left( {X \times  {\mathcal{Y}}_{0} \cup  A \times  Y, A \times  Y}\right) \)

Since \( {y}_{0} \) is a retract of \( Y \) , the upper row of this diagram is a split short exact sequence. The lower row is the long exact sequence of a triple, and it too is a split short exact sequence since \( \left( {X \times  {y}_{0}, A \times  {y}_{0}}\right) \) is a retract of \( \left( {X \times  Y, A \times  Y}\right) \) . The middle and right cross product maps are isomorphisms by the case \( B = \varnothing \) since \( {H}^{k}\left( {Y;R}\right) \) is a finitely generated free \( R \) -module if \( {H}^{k}\left( {Y,{y}_{0};R}\right) \) is. The five-lemma then implies that the left-hand cross product map is an isomorphism as well.

The relative cross product for pairs \( \left( {X,{x}_{0}}\right) \) and \( \left( {Y,{y}_{0}}\right) \) gives a reduced cross product

\[
{\widetilde{H}}^{ * }\left( {X;R}\right) { \otimes  }_{R}{\widetilde{H}}^{ * }\left( {Y;R}\right) \overset{ \times  }{ \rightarrow  }{\widetilde{H}}^{ * }\left( {X \land  Y;R}\right)
\]

where \( X \land  Y \) is the smash product \( X \times  Y/\left( {X \times  \left\{  {y}_{0}\right\}   \cup  \left\{  {x}_{0}\right\}   \times  Y}\right) \) . The preceding theorem implies that this reduced cross product is an isomorphism if \( {\widetilde{H}}^{ * }\left( {X;R}\right) \) or \( {\widetilde{H}}^{ * }\left( {Y;R}\right) \) is free and finitely generated in each dimension. For example, we have isomorphisms \( {\widetilde{H}}^{n}\left( {X;R}\right)  \approx  {\widetilde{H}}^{n + k}\left( {X \land  {S}^{k};R}\right) \) via cross product with a generator of \( {H}^{k}\left( {{S}^{k};R}\right)  \approx  R \) . The space \( X \land  {S}^{k} \) is the \( k \) -fold reduced suspension \( {\sum }^{k}X \) of \( X \) , so we see that the suspension isomorphisms \( {\widetilde{H}}^{n}\left( {X;R}\right)  \approx  {\widetilde{H}}^{n + k}\left( {{\sum }^{k}X;R}\right) \) derivable by elementary exact sequence arguments can also be obtained via cross product with a generator of \( {\widetilde{H}}^{ * }\left( {{S}^{k};R}\right) \) .

## Spaces with Polynomial Cohomology

Earlier in this section we mentioned that projective spaces provide examples of spaces whose cohomology rings are polynomial rings. Here is the precise statement:

Theorem 3.19. \( {H}^{ * }\left( {{\mathbb{{RP}}}^{n};{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) \) and \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack \) , where \( \left| \alpha \right|  = 1 \) . In the complex case, \( {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) \) and \( {H}^{ * }\left( {{\mathbb{{CP}}}^{\infty };\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack \) where \( \left| \alpha \right|  = 2 \) .

This turns out to be a quite important result, and it can be proved in a number of different ways. The proof we give here uses the geometry of projective spaces to reduce the result to a very special case of the Künneth formula. Another proof using Poincaré duality will be given in Example 3.40. A third proof is contained in Example 4D.5 as an application of the Gysin sequence.

Proof: Let us do the case of \( {\mathbb{{RP}}}^{n} \) first. To simplify notation we abbreviate \( {\mathbb{{RP}}}^{n} \) to \( {P}^{n} \) and we let the coefficient group \( {\mathbb{Z}}_{2} \) be implicit. Since the inclusion \( {P}^{n - 1} \hookrightarrow  {P}^{n} \) induces an isomorphism on \( {H}^{i} \) for \( i \leq  n - 1 \) , it suffices by induction on \( n \) to show that the cup product of a generator of \( {H}^{n - 1}\left( {P}^{n}\right) \) with a generator of \( {H}^{1}\left( {P}^{n}\right) \) is a generator of \( {H}^{n}\left( {P}^{n}\right) \) . It will be no more work to show more generally that the cup product of a generator of \( {H}^{i}\left( {P}^{n}\right) \) with a generator of \( {H}^{n - i}\left( {P}^{n}\right) \) is a generator of \( {H}^{n}\left( {P}^{n}\right) \) . As a further notational aid, we let \( j = n - i \) , so \( i + j = n \) .

The proof uses some of the geometric structure of \( {P}^{n} \) . Recall that \( {P}^{n} \) consists of nonzero vectors \( \left( {{x}_{0},\cdots ,{x}_{n}}\right)  \in  {\mathbb{R}}^{n + 1} \) modulo multiplication by nonzero scalars. Inside \( {P}^{n} \) is a copy of \( {P}^{i} \) represented by vectors whose last \( j \) coordinates \( {x}_{i + 1},\cdots ,{x}_{n} \) are zero. We also have a copy of \( {P}^{j} \) represented by points whose first \( i \) coordinates \( {x}_{0},\cdots ,{x}_{i - 1} \) are zero. The intersection \( {P}^{i} \cap  {P}^{j} \) is a single point \( p \) , represented by vectors whose only nonzero coordinate is \( {x}_{i} \) . Let \( U \) be the subspace of \( {P}^{n} \) represented by vectors with nonzero coordinate \( {x}_{i} \) . Each point in \( U \) may be represented by a unique vector with \( {x}_{i} = 1 \) and the other \( n \) coordinates arbitrary, so \( U \) is homeomorphic to \( {\mathbb{R}}^{n} \) , with \( p \) corresponding to 0 under this homeomorphism. We can write this \( {\mathbb{R}}^{n} \) as \( {\mathbb{R}}^{i} \times  {\mathbb{R}}^{j} \) , with \( {\mathbb{R}}^{i} \) as the coordinates \( {x}_{0},\cdots ,{x}_{i - 1} \) and \( {\mathbb{R}}^{j} \) as the coordinates \( {x}_{i + 1},\cdots ,{x}_{n} \) . In the figure \( {P}^{n} \) is represented as a disk with antipodal points of its boundary sphere identified to form a \( {P}^{n - 1} \subset  {P}^{n} \) with \( U = {P}^{n} - {P}^{n - 1} \) the interior of the disk.

![bo_d7dtv0s91nqc73eq8nv0_228_1143_1434_443_303_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_228_1143_1434_443_303_0.jpg)

Consider the diagram(i)which commutes by naturality of cup product. We will show that the four vertical maps are isomorphisms and that the lower cup product map takes generator cross generator to generator. Commutativity of the diagram will then imply that the upper cup product map also takes generator cross generator to generator.

![bo_d7dtv0s91nqc73eq8nv0_228_382_2016_1012_266_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_228_382_2016_1012_266_0.jpg)

The lower map in the right column is an isomorphism by excision. For the upper map in this column, the fact that \( {P}^{n} - \{ p\} \) deformation retracts to a \( {P}^{n - 1} \) gives an isomorphism \( {H}^{n}\left( {{P}^{n},{P}^{n}-\{ p\} }\right)  \approx  {H}^{n}\left( {{P}^{n},{P}^{n - 1}}\right) \) via the five-lemma applied to the long exact sequences for these pairs. And \( {H}^{n}\left( {{P}^{n},{P}^{n - 1}}\right)  \approx  {H}^{n}\left( {P}^{n}\right) \) by cellular cohomology.

To see that the vertical maps in the left column of (i) are isomorphisms we will use the following commutative diagram:

\[
{H}^{i}\left( {P}^{n}\right)  \leftarrow  {H}^{i}\left( {{P}^{n},{P}^{i - 1}}\right)  \leftarrow  {H}^{i}\left( {{P}^{n},{P}^{n} - {P}^{j}}\right)  \rightarrow  {H}^{i}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - {\mathbb{R}}^{j}}\right)
\]

(ii)

\[
{H}^{i}\left( {P}^{i}\right)  \leftarrow  {H}^{i}\left( {{P}^{i},{P}^{i - 1}}\right)  \leftarrow  {H}^{i}\left( {{P}^{i},{P}^{i}-\{ p\} }\right)  \rightarrow  {H}^{i}\left( {{\mathbb{R}}^{i},{\mathbb{R}}^{i}-\{ 0\} }\right)
\]

\( \begin{matrix}  \downarrow  \\  {H}^{i}\left( {D}^{i}\right)  \downarrow  \cdots {H}^{i}\left( {{D}^{i}{D}^{i - 1}}\right)  \downarrow  \cdots {H}^{i}\left( {{D}^{i}{D}^{i}, i = 1}\right) \cdots {H}^{i}\left( {{D}^{i}{D}^{i}, i = 1}\right)  \end{matrix} \)

If we can show all these maps are isomorphisms, then the same argument will apply with \( i \) and \( j \) interchanged, and the vertical maps in the left column of (i) will be isomorphisms.

The left-hand square in (ii) consists of isomorphisms by cellular cohomology. The right-hand vertical map is obviously an isomorphism. The lower right horizontal map is an isomorphism by excision, and the map to the left of this is an isomorphism since \( {P}^{i} - \{ p\} \) deformation retracts onto \( {P}^{i - 1} \) . The remaining maps will be isomorphisms if the middle map in the upper row is an isomorphism. And this map is in fact an isomorphism because \( {P}^{n} - {P}^{j} \) deformation retracts onto \( {P}^{i - 1} \) by the following argument. The subspace \( {P}^{n} - {P}^{j} \subset  {P}^{n} \) consists of points represented by vectors \( v = \left( {{x}_{0},\cdots ,{x}_{n}}\right) \) with at least one of the coordinates \( {x}_{0},\cdots ,{x}_{i - 1} \) nonzero. The formula \( {f}_{t}\left( v\right)  = \left( {{x}_{0},\cdots ,{x}_{i - 1}, t{x}_{i},\cdots , t{x}_{n}}\right) \) for \( t \) decreasing from 1 to 0 gives a well-defined deformation retraction of \( {P}^{n} - {P}^{j} \) onto \( {P}^{i - 1} \) since \( {f}_{t}\left( {\lambda v}\right)  = \lambda {f}_{t}\left( v\right) \) for scalars \( \lambda  \in  \mathbb{R} \) .

The cup product map in the bottom row of (i) is equivalent to the cross product \( {H}^{i}\left( {{I}^{i},\partial {I}^{i}}\right)  \times  {H}^{j}\left( {{I}^{j},\partial {I}^{j}}\right)  \rightarrow  {H}^{n}\left( {{I}^{n},\partial {I}^{n}}\right) \) , where the cross product of generators is a generator by the relative form of the Künneth formula in Theorem 3.18. Alternatively, if one wishes to use only the absolute Künneth formula, the cross product for cubes is equivalent to the cross product \( {H}^{i}\left( {S}^{i}\right)  \times  {H}^{j}\left( {S}^{j}\right)  \rightarrow  {H}^{n}\left( {{S}^{i} \times  {S}^{j}}\right) \) by means of the quotient maps \( {I}^{i} \rightarrow  {S}^{i} \) and \( {I}^{j} \rightarrow  {S}^{j} \) collapsing the boundaries of the cubes to points.

This finishes the proof for \( {\mathbb{{RP}}}^{n} \) . The case of \( {\mathbb{{RP}}}^{\infty } \) follows from this since the inclusion \( {\mathbb{{RP}}}^{n} \hookrightarrow  {\mathbb{{RP}}}^{\infty } \) induces isomorphisms on \( {H}^{i}\left( {-;{\mathbb{Z}}_{2}}\right) \) for \( i \leq  n \) by cellular cohomology.

Complex projective spaces are handled in precisely the same way, using \( \mathbb{Z} \) coefficients and replacing each \( {H}^{k} \) by \( {H}^{2k} \) and \( \mathbb{R} \) by \( \mathbb{C} \) .

There are also quaternionic projective spaces \( {\mathbb{{HP}}}^{n} \) and \( {\mathbb{{HP}}}^{\infty } \) , defined exactly as in the complex case, with CW structures of the form \( {e}^{0} \cup  {e}^{4} \cup  {e}^{8} \cup  \cdots \) . Associativity of quaternion multiplication is needed for the identification \( v \sim  {\lambda v} \) to be an equivalence relation, so the definition does not extend to octonionic projective spaces, though there is an octonionic projective plane \( {\mathbb{{OP}}}^{2} \) defined in Example 4.47. The cup product structure in quaternionic projective spaces is just like that in complex projective spaces, except that the generator is 4-dimensional:

\[
{H}^{ * }\left( {\mathbb{H}{\mathrm{P}}^{\infty };\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  \text{ and }{H}^{ * }\left( {\mathbb{H}{\mathrm{P}}^{n};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) ,\;\text{ with }\left| \alpha \right|  = 4
\]

The same proof as in the real and complex cases works here as well.

The cup product structure for \( {\mathbb{{RP}}}^{\infty } \) with \( \mathbb{Z} \) coefficients can easily be deduced from the cup product structure with \( {\mathbb{Z}}_{2} \) coefficients, as follows. In general, a ring homomorphism \( R \rightarrow  S \) induces a ring homomorphism \( {H}^{ * }\left( {X, A;R}\right)  \rightarrow  {H}^{ * }\left( {X, A;S}\right) \) . In the case of the projection \( \mathbb{Z} \rightarrow  {\mathbb{Z}}_{2} \) we get for \( {\mathbb{{RP}}}^{\infty } \) an induced chain map of cellular cochain complexes with \( \mathbb{Z} \) and \( {\mathbb{Z}}_{2} \) coefficients:

\[
\cdots  \leftarrow  \mathbb{Z}\overset{2}{ \leftarrow  }\mathbb{Z}\overset{0}{ \leftarrow  }\mathbb{Z}\overset{2}{ \leftarrow  }\mathbb{Z}\overset{0}{ \leftarrow  }0
\]

\[
\begin{matrix}  &  \downarrow  \\  \cdots &  \leftarrow   \end{matrix}{\mathbb{Z}}_{2}\xleftarrow[]{0}{\mathbb{Z}}_{2}\xleftarrow[]{0}{\mathbb{Z}}_{2}\xleftarrow[]{0}{\mathbb{Z}}_{2}\xleftarrow[]{0}{\mathbb{Z}}_{2}\xleftarrow[]{0}0
\]

From this we see that the ring homomorphism \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right) \) is injective in positive dimensions, with image the even-dimensional part of \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right) \) . Alternatively, this could be deduced from the universal coefficient theorem. Hence we have \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {2\alpha }\right) \) with \( \left| \alpha \right|  = 2. \)

The cup product structure in \( {H}^{ * }\left( {{\mathbb{{RP}}}^{n};\mathbb{Z}}\right) \) can be computed in a similar fashion, though the description is a little cumbersome:

\[
{H}^{ * }\left( {\mathbb{R}{\mathrm{P}}^{2k};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {{2\alpha },{\alpha }^{k + 1}}\right) ,\;\left| \alpha \right|  = 2
\]

\[
{H}^{ * }\left( {{\mathbb{{RP}}}^{{2k} + 1};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {\alpha ,\beta }\right\rbrack  /\left( {{2\alpha },{\alpha }^{k + 1},{\beta }^{2},{\alpha \beta }}\right) ,\;\left| \alpha \right|  = 2,\left| \beta \right|  = {2k} + 1
\]

Here \( \beta \) is a generator of \( {H}^{{2k} + 1}\left( {{\mathbb{{RP}}}^{{2k} + 1};\mathbb{Z}}\right)  \approx  \mathbb{Z} \) . From this calculation we see that the rings \( {H}^{ * }\left( {{\mathbb{{RP}}}^{{2k} + 1};\mathbb{Z}}\right) \) and \( {H}^{ * }\left( {{\mathbb{{RP}}}^{2k} \vee  {S}^{{2k} + 1};\mathbb{Z}}\right) \) are isomorphic, though with \( {\mathbb{Z}}_{2} \) coefficients this is no longer true, as the generator \( \alpha  \in  {H}^{1}\left( {{\mathbb{{RP}}}^{{2k} + 1};{\mathbb{Z}}_{2}}\right) \) has \( {\alpha }^{{2k} + 1} \neq  0 \) , while \( {\alpha }^{{2k} + 1} = 0 \) for the generator \( \alpha  \in  {H}^{1}\left( {{\mathbb{{RP}}}^{2k} \vee  {S}^{{2k} + 1};{\mathbb{Z}}_{2}}\right) \) .

Example 3.20. Combining the calculation \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack \) with the Künneth formula, we see that \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty } \times  {\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2}}\right) \) is isomorphic to \( {\mathbb{Z}}_{2}\left\lbrack  {\alpha }_{1}\right\rbrack   \otimes  {\mathbb{Z}}_{2}\left\lbrack  {\alpha }_{2}\right\rbrack \) , which is just the polynomial ring \( {\mathbb{Z}}_{2}\left\lbrack  {{\alpha }_{1},{\alpha }_{2}}\right\rbrack \) . More generally it follows by induction that for a product of \( n \) copies of \( {\mathbb{{RP}}}^{\infty } \) , the \( {\mathbb{Z}}_{2} \) -cohomology is a polynomial ring in \( n \) variables. Similar remarks apply to \( {\mathbb{{CP}}}^{\infty } \) and \( {\mathbb{{HP}}}^{\infty } \) with coefficients in \( \mathbb{Z} \) or any commutative ring.

The following theorem of Hopf is a nice algebraic application of the cup product structure in \( {H}^{ * }\left( {{\mathbb{{RP}}}^{n} \times  {\mathbb{{RP}}}^{n};{\mathbb{Z}}_{2}}\right) \) .

Theorem 3.21. If \( {\mathbb{R}}^{n} \) has the structure of a division algebra over the scalar field \( \mathbb{R} \) , then \( n \) must be a power of 2 .

Proof: For a division algebra structure on \( {\mathbb{R}}^{n} \) the multiplication maps \( x \mapsto  {ax} \) and \( x \mapsto  {xa} \) are linear isomorphisms for each nonzero \( a \) , so the multiplication map \( {\mathbb{R}}^{n} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) induces a map \( h : {\mathbb{{RP}}}^{n - 1} \times  {\mathbb{{RP}}}^{n - 1} \rightarrow  {\mathbb{{RP}}}^{n - 1} \) which is a homeomorphism when restricted to each subspace \( {\mathbb{{RP}}}^{n - 1} \times  \{ y\} \) and \( \{ x\}  \times  {\mathbb{{RP}}}^{n - 1} \) . The map \( h \) is continuous since it is a quotient of the multiplication map which is bilinear and hence continuous. The induced homomorphism \( {h}^{ * } \) on \( {\mathbb{Z}}_{2} \) -cohomology is a ring homomorphism \( {\mathbb{Z}}_{2}\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n}\right)  \rightarrow  {\mathbb{Z}}_{2}\left\lbrack  {{\alpha }_{1},{\alpha }_{2}}\right\rbrack  /\left( {{\alpha }_{1}^{n},{\alpha }_{2}^{n}}\right) \) determined by the element \( {h}^{ * }\left( \alpha \right)  = {k}_{1}{\alpha }_{1} + {k}_{2}{\alpha }_{2} \) . The inclusion \( {\mathbb{{RP}}}^{n - 1} \hookrightarrow  {\mathbb{{RP}}}^{n - 1} \times  {\mathbb{{RP}}}^{n - 1} \) onto the first factor sends \( {\alpha }_{1} \) to \( \alpha \) and \( {\alpha }_{2} \) to 0, as one sees by composing with the projections of \( {\mathbb{{RP}}}^{n - 1} \times  {\mathbb{{RP}}}^{n - 1} \) onto its two factors. The fact that \( h \) restricts to a homeomorphism on the first factor then implies that \( {k}_{1} \) is nonzero. Similarly \( {k}_{2} \) is nonzero, so since these coefficients lie in \( {\mathbb{Z}}_{2} \) we have \( {h}^{ * }\left( \alpha \right)  = {\alpha }_{1} + {\alpha }_{2} \) .

Since \( {\alpha }^{n} = 0 \) we must have \( {h}^{ * }\left( {\alpha }^{n}\right)  = 0 \) , so \( {\left( {\alpha }_{1} + {\alpha }_{2}\right) }^{n} = \mathop{\sum }\limits_{k}\left( \begin{array}{l} n \\  k \end{array}\right) {\alpha }_{1}^{k}{\alpha }_{2}^{n - k} = 0 \) . This is an equation in the ring \( {\mathbb{Z}}_{2}\left\lbrack  {{\alpha }_{1},{\alpha }_{2}}\right\rbrack  /\left( {{\alpha }_{1}^{n},{\alpha }_{2}^{n}}\right) \) , so the coefficient \( \left( \begin{array}{l} n \\  k \end{array}\right) \) must be zero in \( {\mathbb{Z}}_{2} \) for all \( k \) in the range \( 0 < k < n \) . It is a rather easy number theory fact that this happens only when \( n \) is a power of 2 . Namely, an obviously equivalent statement is that in the polynomial ring \( {\mathbb{Z}}_{2}\left\lbrack  x\right\rbrack \) , the equality \( {\left( 1 + x\right) }^{n} = 1 + {x}^{n} \) holds only when \( n \) is a power of 2 . To prove the latter statement, write \( n \) as a sum of powers of \( 2, n = {n}_{1} + \cdots  + {n}_{k} \) with \( {n}_{1} < \cdots  < {n}_{k} \) . Then \( {\left( 1 + x\right) }^{n} = {\left( 1 + x\right) }^{{n}_{1}}\cdots {\left( 1 + x\right) }^{{n}_{k}} = \left( {1 + {x}^{{n}_{1}}}\right) \cdots \left( {1 + {x}^{{n}_{k}}}\right) \) since squaring is an additive homomorphism with \( {\mathbb{Z}}_{2} \) coefficients. If one multiplies the product \( \left( {1 + {x}^{{n}_{1}}}\right) \cdots \left( {1 + {x}^{{n}_{k}}}\right) \) out, no terms combine or cancel since \( {n}_{i} \geq  2{n}_{i - 1} \) for each \( i \) , and so the resulting polynomial has \( {2}^{k} \) terms. Thus if this polynomial equals \( 1 + {x}^{n} \) we must have \( k = 1 \) , which means that \( n \) is a power of 2 .

The same argument can be applied with \( \mathbb{C} \) in place of \( \mathbb{R} \) , to show that if \( {\mathbb{C}}^{n} \) is a division algebra over \( \mathbb{C} \) then \( \left( \begin{array}{l} n \\  k \end{array}\right)  = 0 \) for all \( k \) in the range \( 0 < k < n \) , but now we can use \( \mathbb{Z} \) rather than \( {\mathbb{Z}}_{2} \) coefficients, so we deduce that \( n = 1 \) . Thus there are no higher-dimensional division algebras over \( \mathbb{C} \) . This is assuming we are talking about finite-dimensional division algebras. For infinite dimensions there is for example the field of rational functions \( \mathbb{C}\left( x\right) \) .

We saw in Theorem 3.19 that \( {\mathbb{{RP}}}^{\infty },{\mathbb{{CP}}}^{\infty } \) , and \( {\mathbb{{HP}}}^{\infty } \) have cohomology rings that are polynomial algebras. We will describe now a construction for enlarging \( {S}^{2n} \) to a space \( J\left( {S}^{2n}\right) \) whose cohomology ring \( {H}^{ * }\left( {J\left( {S}^{2n}\right) ;\mathbb{Z}}\right) \) is almost the polynomial ring \( \mathbb{Z}\left\lbrack  x\right\rbrack \) on a generator \( x \) of dimension \( {2n} \) . And if we change from \( \mathbb{Z} \) to \( \mathbb{Q} \) coefficients, then \( {H}^{ * }\left( {J\left( {S}^{2n}\right) ;\mathbb{Q}}\right) \) is exactly the polynomial ring \( \mathbb{Q}\left\lbrack  x\right\rbrack \) . This construction, known as the James reduced product, is also of interest because of its connections with loopspaces described in §4.J.

For a space \( X \) , let \( {X}^{k} \) be the product of \( k \) copies of \( X \) . From the disjoint union \( \mathop{\coprod }\limits_{{k \geq  1}}{X}^{k} \) , let us form a quotient space \( J\left( X\right) \) by identifying \( \left( {{x}_{1},\cdots ,{x}_{i},\cdots ,{x}_{k}}\right) \) with \( \left( {{x}_{1},\cdots ,{\widehat{x}}_{i},\cdots ,{x}_{k}}\right) \) if \( {x}_{i} = e \) , a chosen basepoint of \( X \) . Points of \( J\left( X\right) \) can thus be thought of as \( k \) -tuples \( \left( {{x}_{1},\cdots ,{x}_{k}}\right) , k \geq  0 \) , with no \( {x}_{i} = e \) . Inside \( J\left( X\right) \) is the subspace \( {J}_{m}\left( X\right) \) consisting of the points \( \left( {{x}_{1},\cdots ,{x}_{k}}\right) \) with \( k \leq  m \) . This can be viewed as a quotient space of \( {X}^{m} \) under the identifications \( \left( {{x}_{1},\cdots ,{x}_{i}, e,\cdots ,{x}_{m}}\right)  \sim \; \left( {{x}_{1},\cdots , e,{x}_{i},\cdots ,{x}_{m}}\right) \) . For example, \( {J}_{1}\left( X\right)  = X \) and \( {J}_{2}\left( X\right)  = X \times  X/\left( {x, e}\right)  \sim  \left( {e, x}\right) \) . If \( X \) is a CW complex with \( e \) a 0 -cell, the quotient map \( {X}^{m} \rightarrow  {J}_{m}\left( X\right) \) glues together the \( m \) subcomplexes of the product complex \( {X}^{m} \) where one coordinate is \( e \) . These glueings are by homeomorphisms taking cells onto cells, so \( {J}_{m}\left( X\right) \) inherits a CW structure from \( {X}^{m} \) . There are natural inclusions \( {J}_{m}\left( X\right)  \subset  {J}_{m + 1}\left( X\right) \) as subcomplexes, and \( J\left( X\right) \) is the union of these subcomplexes, hence is also a CW complex.

Proposition 3.22. For \( n > 0,{H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) consists of a \( \mathbb{Z} \) in each dimension a multiple of \( n \) . If \( n \) is even, the \( {i}^{th} \) power of a generator of \( {H}^{n}\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) is \( i \) ! times a generator of \( {H}^{in}\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) , for each \( i \geq  1 \) . When \( n \) is odd, \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) is isomorphic as a graded ring to \( {H}^{ * }\left( {{S}^{n};\mathbb{Z}}\right)  \otimes  {H}^{ * }\left( {J\left( {S}^{2n}\right) ;\mathbb{Z}}\right) \) .

It follows that for \( n \) even, \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) can be identified with the subring of the polynomial ring \( \mathbb{Q}\left\lbrack  x\right\rbrack \) additively generated by the monomials \( {x}^{i}/i \) !. This subring is called a divided polynomial algebra and is denoted \( {\Gamma }_{\mathbb{Z}}\left\lbrack  x\right\rbrack \) . Thus \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) is isomorphic to \( {\Gamma }_{\mathbb{Z}}\left\lbrack  x\right\rbrack \) when \( n \) is even and to \( {\Lambda }_{\mathbb{Z}}\left\lbrack  x\right\rbrack   \otimes  {\Gamma }_{\mathbb{Z}}\left\lbrack  y\right\rbrack \) when \( n \) is odd.

Proof: Giving \( {S}^{n} \) its usual CW structure, the resulting CW structure on \( J\left( {S}^{n}\right) \) consists of exactly one cell in each dimension a multiple of \( n \) . If \( n > 1 \) we deduce immediately from cellular cohomology that \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) consists exactly of \( \mathbb{Z} \) ’s in dimensions a multiple of \( n \) . For an alternative argument that works also when \( n = 1 \) , consider the quotient map \( q : {\left( {S}^{n}\right) }^{m} \rightarrow  {J}_{m}\left( {S}^{n}\right) \) . This carries each cell of \( {\left( {S}^{n}\right) }^{m} \) homeomorphi-cally onto a cell of \( {J}_{m}\left( {S}^{n}\right) \) . In particular \( q \) is a cellular map, taking \( k \) -skeleton to \( k \) -skeleton for each \( k \) , so \( q \) induces a chain map of cellular chain complexes. This chain map is surjective since each cell of \( {J}_{m}\left( {S}^{n}\right) \) is the homeomorphic image of a cell of \( {\left( {S}^{n}\right) }^{m} \) . Hence the cellular boundary maps for \( {J}_{m}\left( {S}^{n}\right) \) will be trivial if they are trivial for \( {\left( {S}^{n}\right) }^{m} \) , as indeed they are since \( {H}^{ * }\left( {{\left( {S}^{n}\right) }^{m};\mathbb{Z}}\right) \) is free with basis in one-to-one correspondence with the cells, by Theorem 3.15.

We can compute cup products in \( {H}^{ * }\left( {{J}_{m}\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) by computing their images under \( {q}^{ * } \) . Let \( {x}_{k} \) denote the generator of \( {H}^{kn}\left( {{J}_{m}\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) dual to the \( {kn} \) -cell, represented by the cellular cocycle assigning the value 1 to the \( {kn} \) -cell. Since \( q \) identifies all the \( n \) -cells of \( {\left( {S}^{n}\right) }^{m} \) to form the \( n \) -cell of \( {J}_{m}\left( {S}^{n}\right) \) , we see from cellular cohomology that \( {q}^{ * }\left( {x}_{1}\right) \) is the sum \( {\alpha }_{1} + \cdots  + {\alpha }_{m} \) of the generators of \( {H}^{n}\left( {{\left( {S}^{n}\right) }^{m};\mathbb{Z}}\right) \) dual to the \( n \) -cells of \( {\left( {S}^{n}\right) }^{m} \) . By the same reasoning we have \( {q}^{ * }\left( {x}_{k}\right)  = \mathop{\sum }\limits_{{{i}_{1} < \cdots  < {i}_{k}}}{\alpha }_{{i}_{1}}\cdots {\alpha }_{{i}_{k}} \) .

If \( n \) is even, the cup product structure in \( {H}^{ * }\left( {{\left( {S}^{n}\right) }^{m};\mathbb{Z}}\right) \) is strictly commutative and \( {H}^{ * }\left( {{\left( {S}^{n}\right) }^{m};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{m}}\right\rbrack  /\left( {{\alpha }_{1}^{2},\cdots ,{\alpha }_{m}^{2}}\right) \) . Then we have

\[
{q}^{ * }\left( {x}_{1}^{m}\right)  = {\left( {\alpha }_{1} + \cdots  + {\alpha }_{m}\right) }^{m} = m!{\alpha }_{1}\cdots {\alpha }_{m} = m!{q}^{ * }\left( {x}_{m}\right)
\]

Since \( {q}^{ * } \) is an isomorphism on \( {H}^{mn} \) this implies \( {x}_{1}^{m} = m!{x}_{m} \) in \( {H}^{mn}\left( {{J}_{m}\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) . The inclusion \( {J}_{m}\left( {S}^{n}\right)  \hookrightarrow  J\left( {S}^{n}\right) \) induces isomorphisms on \( {H}^{i} \) for \( i \leq  {mn} \) so we have \( {x}_{1}^{m} = m!{x}_{m} \) in \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) as well, where \( {x}_{1} \) and \( {x}_{m} \) are interpreted now as elements of \( {H}^{ * }\left( {J\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) .

When \( n \) is odd we have \( {x}_{1}^{2} = 0 \) by commutativity, and it will suffice to prove the following two formulas:

(a) \( {x}_{1}{x}_{2m} = {x}_{{2m} + 1} \) in \( {H}^{ * }\left( {{J}_{{2m} + 1}\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) .

(b) \( {x}_{2}{x}_{{2m} - 2} = m{x}_{2m} \) in \( {H}^{ * }\left( {{J}_{2m}\left( {S}^{n}\right) ;\mathbb{Z}}\right) \) .

For (a) we apply \( {q}^{ * } \) and compute in the exterior algebra \( {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{{2m} + 1}}\right\rbrack \) :

\[
{q}^{ * }\left( {{x}_{1}{x}_{2m}}\right)  = \left( {\mathop{\sum }\limits_{i}{\alpha }_{i}}\right) \left( {\mathop{\sum }\limits_{i}{\alpha }_{1}\cdots {\widehat{\alpha }}_{i}\cdots {\alpha }_{{2m} + 1}}\right)
\]

\[
= \mathop{\sum }\limits_{i}{\alpha }_{i}{\alpha }_{1}\cdots {\widehat{\alpha }}_{i}\cdots {\alpha }_{{2m} + 1} = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i - 1}{\alpha }_{1}\cdots {\alpha }_{{2m} + 1}
\]

The coefficients in this last summation are \( + 1, - 1,\cdots , + 1 \) , so their sum is +1 and (a) follows. For (b) we have

\[
{q}^{ * }\left( {{x}_{2}{x}_{{2m} - 2}}\right)  = \left( {\mathop{\sum }\limits_{{{i}_{1} < {i}_{2}}}{\alpha }_{{i}_{1}}{\alpha }_{{i}_{2}}}\right) \left( {\mathop{\sum }\limits_{{{i}_{1} < {i}_{2}}}{\alpha }_{1}\cdots {\widehat{\alpha }}_{{i}_{1}}\cdots {\widehat{\alpha }}_{{i}_{2}}\cdots {\alpha }_{2m}}\right)
\]

\[
= \mathop{\sum }\limits_{{{i}_{1} < {i}_{2}}}{\alpha }_{{i}_{1}}{\alpha }_{{i}_{2}}{\alpha }_{1}\cdots {\widehat{\alpha }}_{{i}_{1}}\cdots {\widehat{\alpha }}_{{i}_{2}}\cdots {\alpha }_{2m} = \mathop{\sum }\limits_{{{i}_{1} < {i}_{2}}}{\left( -1\right) }^{{i}_{1} - 1}{\left( -1\right) }^{{i}_{2} - 2}{\alpha }_{1}\cdots {\alpha }_{2m}
\]

The terms in the coefficient \( \mathop{\sum }\limits_{{{i}_{1} < {i}_{2}}}{\left( -1\right) }^{{i}_{1} - 1}{\left( -1\right) }^{{i}_{2} - 2} \) for a fixed \( {i}_{1} \) have \( {i}_{2} \) varying from \( {i}_{1} + 1 \) to \( {2m} \) . These terms are \( + 1, - 1,\cdots \) and there are \( {2m} - {i}_{1} \) of them, so their sum is 0 if \( {i}_{1} \) is even and 1 if \( {i}_{1} \) is odd. Now letting \( {i}_{1} \) vary, it takes on the odd values \( 1,3,\cdots ,{2m} - 1 \) , so the whole summation reduces to \( m \) 1’s and we have the desired relation \( {x}_{2}{x}_{{2m} - 2} = m{x}_{2m} \) .

In \( {\Gamma }_{\mathbb{Z}}\left\lbrack  x\right\rbrack   \subset  \mathbb{Q}\left\lbrack  x\right\rbrack \) , if we let \( {x}_{i} = {x}^{i}/i \) ! then the multiplicative structure is given by \( {x}_{i}{x}_{j} = \left( \begin{matrix} i + j \\  i \end{matrix}\right) {x}_{i + j} \) . More generally, for a commutative ring \( R \) we could define \( {\Gamma }_{R}\left\lbrack  x\right\rbrack \) to be the free \( R \) -module with basis \( {x}_{0} = 1,{x}_{1},{x}_{2},\cdots \) and multiplication defined by \( {x}_{i}{x}_{j} = \left( \begin{matrix} i + j \\  i \end{matrix}\right) {x}_{i + j} \) . The preceding proposition implies that \( {H}^{ * }\left( {J\left( {S}^{2n}\right) ;R}\right)  \approx  {\Gamma }_{R}\left\lbrack  x\right\rbrack \) . When \( R = \mathbb{Q} \) it is clear that \( {\Gamma }_{\mathbb{Q}}\left\lbrack  x\right\rbrack \) is just \( \mathbb{Q}\left\lbrack  x\right\rbrack \) . However, for \( R = {\mathbb{Z}}_{p} \) with \( p \) prime something quite different happens: There is an isomorphism

\[
{\Gamma }_{{\mathbb{Z}}_{p}}\left\lbrack  x\right\rbrack   \approx  {\mathbb{Z}}_{p}\left\lbrack  {{x}_{1},{x}_{p},{x}_{{p}^{2}},\cdots }\right\rbrack  /\left( {{x}_{1}^{p},{x}_{p}^{p},{x}_{{p}^{2}}^{p},\cdots }\right)  = {\bigotimes }_{i \geq  0}{\mathbb{Z}}_{p}\left\lbrack  {x}_{{p}^{i}}\right\rbrack  /\left( {x}_{{p}^{i}}^{p}\right)
\]

as we show in \( \text{ § }3.\mathrm{C} \) , where we will also see that divided polynomial algebras are in a certain sense dual to polynomial algebras.

The examples of projective spaces lead naturally to the following question: Given a coefficient ring \( R \) and an integer \( d > 0 \) , is there a space \( X \) having \( {H}^{ * }\left( {X;R}\right)  \approx  R\left\lbrack  \alpha \right\rbrack \) with \( \left| \alpha \right|  = d \) ? Historically, it took major advances in the theory to answer this simple-looking question. Here is a table giving all the possible values of \( d \) for some of the most obvious and important choices of \( R \) , namely \( \mathbb{Z},\mathbb{Q},{\mathbb{Z}}_{2} \) , and \( {\mathbb{Z}}_{p} \) with \( p \) an odd prime. As we have seen, projective

---

<table><tr><td>\( R \)</td><td>d</td></tr><tr><td>\( \mathbb{Z} \)</td><td>2,4</td></tr><tr><td>Q</td><td>any even number</td></tr><tr><td>\( {\mathbb{Z}}_{2} \)</td><td>1, 2, 4</td></tr><tr><td>\( {\mathbb{Z}}_{p} \)</td><td>any even divisor of \( 2\left( {p - 1}\right) \)</td></tr></table>

---

spaces give the examples for \( \mathbb{Z} \) and \( {\mathbb{Z}}_{2} \) . Examples for \( \mathbb{Q} \) are the spaces \( J\left( {S}^{d}\right) \) , and examples for \( {\mathbb{Z}}_{p} \) are constructed in \( \text{ § }3 \) .G. Showing that no other \( d \) ’s are possible takes considerably more work. The fact that \( d \) must be even when \( R \neq  {\mathbb{Z}}_{2} \) is a consequence of the commutativity property of cup product. In Theorem 4L.9 and Corollary 4L.10 we will settle the case \( R = \mathbb{Z} \) and show that \( d \) must be a power of 2 for \( R = {\mathbb{Z}}_{2} \) and a power of \( p \) times an even divisor of \( 2\left( {p - 1}\right) \) for \( R = {\mathbb{Z}}_{p}, p \) odd. Ruling out the remaining cases is best done using K-theory, as in [VBKT] or the classical reference [Adams &Atiyah 1966]. However there is one slightly anomalous case, \( R = {\mathbb{Z}}_{2}, d = 8 \) , which must be treated by special arguments; see [Toda 1963].

It is an interesting fact that for each even \( d \) there exists a CW complex \( {X}_{d} \) which is simultaneously an example for all the admissible choices of coefficients \( R \) in the table. Moreover, \( {X}_{d} \) can be chosen to have the simplest CW structure consistent with its cohomology, namely a single cell in each dimension a multiple of \( d \) . For example, we may take \( {X}_{2} = {\mathbb{{CP}}}^{\infty } \) and \( {X}_{4} = {\mathbb{{HP}}}^{\infty } \) . The next space \( {X}_{6} \) would have \( {H}^{ * }\left( {{X}_{6};{\mathbb{Z}}_{p}}\right)  \approx \; {\mathbb{Z}}_{p}\left\lbrack  \alpha \right\rbrack \) for \( p = 7,{13},{19},{31},\cdots \) , primes of the form \( {3s} + 1 \) , the condition \( 6 \mid  2\left( {p - 1}\right) \) being equivalent to \( p = {3s} + 1 \) . (By a famous theorem of Dirichlet there are infinitely many primes in any such arithmetic progression.) Note that, in terms of \( \mathbb{Z} \) coefficients, \( {X}_{d} \) must have the property that for a generator \( \alpha \) of \( {H}^{d}\left( {{X}_{d};\mathbb{Z}}\right) \) , each power \( {\alpha }^{i} \) is an integer \( {a}_{i} \) times a generator of \( {H}^{di}\left( {{X}_{d};\mathbb{Z}}\right) \) , with \( {a}_{i} \neq  0 \) if \( {H}^{ * }\left( {{X}_{d};\mathbb{Q}}\right)  \approx  \mathbb{Q}\left\lbrack  \alpha \right\rbrack \) and \( {a}_{i} \) relatively prime to \( p \) if \( {H}^{ * }\left( {{X}_{d};{\mathbb{Z}}_{p}}\right)  \approx  {\mathbb{Z}}_{p}\left\lbrack  \alpha \right\rbrack \) . A construction of \( {X}_{d} \) is given in [SSAT], or in the original source [Hoffman & Porter 1973].

One might also ask about realizing the truncated polynomial ring \( R\left\lbrack  \alpha \right\rbrack  /\left( {\alpha }^{n + 1}\right) \) , in view of the examples provided by \( {\mathbb{{RP}}}^{n},{\mathbb{{CP}}}^{n} \) , and \( {\mathbb{{HP}}}^{n} \) , leaving aside the trivial case \( n = 1 \) where spheres provide examples. The analysis for polynomial rings also settles which truncated polynomial rings are realizable; there are just a few more than for the full polynomial rings.

There is also the question of realizing polynomial rings \( R\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) with generators \( {\alpha }_{i} \) in specified dimensions \( {d}_{i} \) . Since \( R\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{m}}\right\rbrack  { \otimes  }_{R}R\left\lbrack  {{\beta }_{1},\cdots ,{\beta }_{n}}\right\rbrack \) is equal to \( R\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{m},{\beta }_{1},\cdots ,{\beta }_{n}}\right\rbrack \) , the product of two spaces with polynomial cohomology is again a space with polynomial cohomology, assuming the number of polynomial generators is finite in each dimension. For example, the \( n \) -fold product \( {\left( {\mathbb{{CP}}}^{\infty }\right) }^{n} \) has \( {H}^{ * }\left( {{\left( {\mathbb{{CP}}}^{\infty }\right) }^{n};\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) with each \( {\alpha }_{i} \) 2-dimensional. Similarly, products of the spaces \( J\left( {S}^{{d}_{i}}\right) \) realize all choices of even \( {d}_{i} \) ’s with \( \mathbb{Q} \) coefficients.

However, with \( \mathbb{Z} \) and \( {\mathbb{Z}}_{p} \) coefficients, products of one-variable examples do not exhaust all the possibilities. As we show in §4.D, there are three other basic examples with \( \mathbb{Z} \) coefficients:

1. Generalizing the space \( {\mathbb{{CP}}}^{\infty } \) of complex lines through the origin in \( {\mathbb{C}}^{\infty } \) , there is the Grassmann manifold \( {G}_{n}\left( {\mathbb{C}}^{\infty }\right) \) of \( n \) -dimensional vector subspaces of \( {\mathbb{C}}^{\infty } \) , and this has \( {H}^{ * }\left( {{G}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) with \( \left| {\alpha }_{i}\right|  = {2i} \) . This space is also known as \( {BU}\left( n\right) \) , the ’classifying space’ of the unitary group \( U\left( n\right) \) . It is central to the study of vector bundles and K-theory.

2. Replacing \( \mathbb{C} \) by \( \mathbb{H} \) , there is the quaternionic Grassmann manifold \( {G}_{n}\left( {\mathbb{H}}^{\infty }\right) \) , also known as \( {BSp}\left( n\right) \) , the classifying space for the symplectic group \( {Sp}\left( n\right) \) , with \( {H}^{ * }\left( {{G}_{n}\left( {\mathbb{H}}^{\infty }\right) ;\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) with \( \left| {\alpha }_{i}\right|  = {4i}. \)

3. There is a classifying space \( {BSU}\left( n\right) \) for the special unitary group \( {SU}\left( n\right) \) , whose cohomology is the same as for \( {BU}\left( n\right) \) but with the first generator \( {\alpha }_{1} \) omitted, so \( {H}^{ * }\left( {{BSU}\left( n\right) ;\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  {{\alpha }_{2},\cdots ,{\alpha }_{n}}\right\rbrack \) with \( \left| {\alpha }_{i}\right|  = {2i}. \)

These examples and their products account for all the realizable polynomial cup product rings with \( \mathbb{Z} \) coefficients, according to a theorem in [Andersen &Grodal 2008]. The situation for \( {\mathbb{Z}}_{p} \) coefficients is more complicated and will be discussed in §3.G.

Polynomial algebras are examples of free graded commutative algebras, where 'free' means loosely 'having no unnecessary relations'. In general, a free graded commutative algebra is a tensor product of single-generator free graded commutative algebras. The latter are either polynomial algebras \( R\left\lbrack  \alpha \right\rbrack \) on even-dimension generators \( \alpha \) or quotients \( R\left\lbrack  \alpha \right\rbrack  /\left( {2{\alpha }^{2}}\right) \) with \( \alpha \) odd-dimensional. Note that if \( R \) is a field then \( R\left\lbrack  \alpha \right\rbrack  /\left( {2{\alpha }^{2}}\right) \) is either the exterior algebra \( {\Lambda }_{R}\left\lbrack  \alpha \right\rbrack \) if the characteristic of \( R \) is not 2, or the polynomial algebra \( R\left\lbrack  \alpha \right\rbrack \) otherwise. Every graded commutative algebra is a quotient of a free one, clearly.

Example 3.23: Subcomplexes of the \( n \) -Torus. To give just a small hint of the endless variety of nonfree cup product algebras that can be realized, consider subcomplexes of the \( n \) -torus \( {T}^{n} \) , the product of \( n \) copies of \( {S}^{1} \) . Here we give \( {S}^{1} \) its standard minimal cell structure and \( {T}^{n} \) the resulting product cell structure. We know that \( {H}^{ * }\left( {{T}^{n};\mathbb{Z}}\right) \) is the exterior algebra \( {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) , with the monomial \( {\alpha }_{{i}_{1}}\cdots {\alpha }_{{i}_{k}} \) corresponding via cellular cohomology to the \( k \) -cell \( {e}_{{i}_{1}}^{1} \times  \cdots  \times  {e}_{{i}_{k}}^{1} \) . So if we pass to a subcomplex \( X \subset  {T}^{n} \) by omitting certain cells, then \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) is the quotient of \( {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) obtained by setting the monomials corresponding to the omitted cells equal to zero. Since we are dealing with rings, we are factoring out by an ideal in \( {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},\cdots ,{\alpha }_{n}}\right\rbrack \) , the ideal generated by the monomials corresponding to the 'minimal' omitted cells, those whose boundary is entirely contained in \( X \) . For example, if we take \( X \) to be the subcomplex of \( {T}^{3} \) obtained by deleting the cells \( {e}_{1}^{1} \times  {e}_{2}^{1} \times  {e}_{3}^{1} \) and \( {e}_{2}^{1} \times  {e}_{3}^{1} \) , then \( {H}^{ * }\left( {X;\mathbb{Z}}\right)  \approx  {\Lambda }_{\mathbb{Z}}\left\lbrack  {{\alpha }_{1},{\alpha }_{2},{\alpha }_{3}}\right\rbrack  /\left( {{\alpha }_{2}{\alpha }_{3}}\right) . \)

How many different subcomplexes of \( {T}^{n} \) are there? To each subcomplex \( X \subset  {T}^{n} \) we can associate a finite simplicial complex \( {C}_{X} \) by the following procedure. View \( {T}^{n} \) as the quotient of the \( n \) -cube \( {I}^{n} = {\left\lbrack  0,1\right\rbrack  }^{n} \subset  {\mathbb{R}}^{n} \) obtained by identifying opposite faces. If we intersect \( {I}^{n} \) with the hyperplane \( {x}_{1} + \cdots  + {x}_{n} = \varepsilon \) for small \( \varepsilon  > 0 \) , we get a simplex \( {\Delta }^{n - 1} \) . Then for \( q : {I}^{n} \rightarrow  {T}^{n} \) the quotient map, we take \( {C}_{X} \) to be \( {\Delta }^{n - 1} \cap  {q}^{-1}\left( X\right) \) . This is a subcomplex of \( {\Delta }^{n - 1} \) whose \( k \) -simplices correspond exactly to the \( \left( {k + 1}\right) \) -cells of \( X \) . In this way we get a one-to-one correspondence between subcomplexes \( X \subset  {T}^{n} \) and subcomplexes \( {C}_{X} \subset  {\Delta }^{n - 1} \) . Every simplicial complex with \( n \) vertices is a subcomplex of \( {\Delta }^{n - 1} \) , so we see that \( {T}^{n} \) has quite a large number of subcomplexes if \( n \) is not too small. The cohomology rings \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) are of a type that was completely classified in [Gubeladze 1998], Theorem 3.1, and from this classification it follows that the ring \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) (or even \( {H}^{ * }\left( {X;{\mathbb{Z}}_{2}}\right) \) ) determines the subcomplex \( X \) uniquely, up to permutation of the \( n \) circle factors of \( {T}^{n} \) .

More elaborate examples could be produced by looking at subcomplexes of the product of \( n \) copies of \( {\mathbb{{CP}}}^{\infty } \) . In this case the cohomology rings are isomorphic to polynomial rings modulo ideals generated by monomials, and it is again true that the cohomology ring determines the subcomplex up to permutation of factors. However, these cohomology rings are still a whole lot less complicated than the general case, where one takes free algebras modulo ideals generated by arbitrary polynomials having all their terms of the same dimension.

Let us conclude this section with an example of a cohomology ring that is not too far removed from a polynomial ring.

Example 3.24: Cohen-Macaulay Rings. Let \( X \) be the quotient space \( {\mathbb{{CP}}}^{\infty }/{\mathbb{{CP}}}^{n - 1} \) . The quotient map \( {\mathbb{{CP}}}^{\infty } \rightarrow  X \) induces an injection \( {H}^{ * }\left( {X;\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{{CP}}}^{\infty };\mathbb{Z}}\right) \) embedding \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) in \( \mathbb{Z}\left\lbrack  \alpha \right\rbrack \) as the subring generated by \( 1,{\alpha }^{n},{\alpha }^{n + 1},\cdots \) . If we view this subring as a module over \( \mathbb{Z}\left\lbrack  {\alpha }^{n}\right\rbrack \) , it is free with basis \( \left\{  {1,{\alpha }^{n + 1},{\alpha }^{n + 2},\cdots ,{\alpha }^{{2n} - 1}}\right\} \) . Thus \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) is an example of a Cohen-Macaulay ring: a ring containing a polynomial subring over which it is a finitely generated free module. While polynomial cup product rings are rather rare, Cohen-Macauley cup product rings occur much more frequently.

## Exercises

1. Assuming as known the cup product structure on the torus \( {S}^{1} \times  {S}^{1} \) , compute the cup product structure in \( {H}^{ * }\left( {M}_{g}\right) \) for \( {M}_{g} \) the closed orientable surface of genus \( g \) by using the quotient map from \( {M}_{g} \) to a wedge sum of \( g \) tori, shown below.

![bo_d7dtv0s91nqc73eq8nv0_236_354_2018_1100_241_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_236_354_2018_1100_241_0.jpg)

2. Using the cup product \( {H}^{k}\left( {X, A;R}\right)  \times  {H}^{\ell }\left( {X, B;R}\right)  \rightarrow  {H}^{k + \ell }\left( {X, A \cup  B;R}\right) \) , show that if \( X \) is the union of contractible open subsets \( A \) and \( B \) , then all cup products of positive-dimensional classes in \( {H}^{ * }\left( {X;R}\right) \) are zero. This applies in particular if \( X \) is a suspension. Generalize to the situation that \( X \) is the union of \( n \) contractible open subsets, to show that all \( n \) -fold cup products of positive-dimensional classes are zero.

3. (a) Using the cup product structure, show there is no map \( {\mathbb{{RP}}}^{n} \rightarrow  {\mathbb{{RP}}}^{m} \) inducing a nontrivial map \( {H}^{1}\left( {{\mathbb{{RP}}}^{m};{\mathbb{Z}}_{2}}\right)  \rightarrow  {H}^{1}\left( {{\mathbb{{RP}}}^{n};{\mathbb{Z}}_{2}}\right) \) if \( n > m \) . What is the corresponding result for maps \( {\mathbb{{CP}}}^{n} \rightarrow  {\mathbb{{CP}}}^{m} \) ?

(b) Prove the Borsuk-Ulam theorem by the following argument. Suppose on the contrary that \( f : {S}^{n} \rightarrow  {\mathbb{R}}^{n} \) satisfies \( f\left( x\right)  \neq  f\left( {-x}\right) \) for all \( x \) . Then define \( g : {S}^{n} \rightarrow  {S}^{n - 1} \) by \( g\left( x\right)  = \left( {f\left( x\right)  - f\left( {-x}\right) }\right) /\left| {f\left( x\right)  - f\left( {-x}\right) }\right| \) , so \( g\left( {-x}\right)  =  - g\left( x\right) \) and \( g \) induces a map \( {\mathbb{{RP}}}^{n} \rightarrow  {\mathbb{{RP}}}^{n - 1} \) . Show that part (a) applies to this map.

4. Apply the Lefschetz fixed point theorem to show that every map \( f : {\mathbb{{CP}}}^{n} \rightarrow  {\mathbb{{CP}}}^{n} \) has a fixed point if \( n \) is even, using the fact that \( {f}^{ * } : {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right) \) is a ring homomorphism. When \( n \) is odd show there is a fixed point unless \( {f}^{ * }\left( \alpha \right)  =  - \alpha \) , for \( \alpha \) a generator of \( {H}^{2}\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right) \) . [See Exercise 3 in §2.C for an example of a map without fixed points in this exceptional case.]

5. Show the ring \( {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };{\mathbb{Z}}_{2k}}\right) \) is isomorphic to \( {\mathbb{Z}}_{2k}\left\lbrack  {\alpha ,\beta }\right\rbrack  /\left( {{2\alpha },{2\beta },{\alpha }^{2} - {k\beta }}\right) \) where \( \left| \alpha \right|  = 1 \) and \( \left| \beta \right|  = 2 \) . [Use the coefficient map \( {\mathbb{Z}}_{2k} \rightarrow  {\mathbb{Z}}_{2} \) and the proof of Theorem 3.19.] 6. Use cup products to compute the map \( {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{{CP}}}^{n};\mathbb{Z}}\right) \) induced by the map \( {\mathbb{{CP}}}^{n} \rightarrow  {\mathbb{{CP}}}^{n} \) that is a quotient of the map \( {\mathbb{C}}^{n + 1} \rightarrow  {\mathbb{C}}^{n + 1} \) raising each coordinate to the \( {d}^{th} \) power, \( \left( {{z}_{0},\cdots ,{z}_{n}}\right)  \mapsto  \left( {{z}_{0}^{d},\cdots ,{z}_{n}^{d}}\right) \) , for a fixed integer \( d > 0 \) . [First do the case \( n = 1 \) .]

7. Use cup products to show that \( {\mathbb{{RP}}}^{3} \) is not homotopy equivalent to \( {\mathbb{{RP}}}^{2} \vee  {S}^{3} \) .

8. Let \( X \) be \( \mathbb{C}{\mathrm{P}}^{2} \) with a cell \( {e}^{3} \) attached by a map \( {S}^{2} \rightarrow  \mathbb{C}{\mathrm{P}}^{1} \subset  \mathbb{C}{\mathrm{P}}^{2} \) of degree \( p \) , and let \( Y = M\left( {{\mathbb{Z}}_{p},2}\right)  \vee  {S}^{4} \) . Thus \( X \) and \( Y \) have the same 3-skeleton but differ in the way their 4-cells are attached. Show that \( X \) and \( Y \) have isomorphic cohomology rings with \( \mathbb{Z} \) coefficients but not with \( {\mathbb{Z}}_{p} \) coefficients.

9. Show that if \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) is free for each \( n \) , then \( {H}^{ * }\left( {X;{\mathbb{Z}}_{p}}\right) \) and \( {H}^{ * }\left( {X;\mathbb{Z}}\right)  \otimes  {\mathbb{Z}}_{p} \) are isomorphic as rings, so in particular the ring structure with \( \mathbb{Z} \) coefficients determines the ring structure with \( {\mathbb{Z}}_{p} \) coefficients.

10. Show that the cross product map \( {H}^{ * }\left( {X;\mathbb{Z}}\right)  \otimes  {H}^{ * }\left( {Y;\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {X \times  Y;\mathbb{Z}}\right) \) is not an isomorphism if \( X \) and \( Y \) are infinite discrete sets. [This shows the necessity of the hypothesis of finite generation in Theorem 3.15.]

11. Using cup products, show that every map \( {S}^{k + \ell } \rightarrow  {S}^{k} \times  {S}^{\ell } \) induces the trivial homomorphism \( {H}_{k + \ell }\left( {S}^{k + \ell }\right)  \rightarrow  {H}_{k + \ell }\left( {{S}^{k} \times  {S}^{\ell }}\right) \) , assuming \( k > 0 \) and \( \ell  > 0 \) .

12. Show that the spaces \( \left( {{S}^{1} \times  {\mathbb{{CP}}}^{\infty }}\right) /\left( {{S}^{1} \times  \left\{  {x}_{0}\right\}  }\right) \) and \( {S}^{3} \times  {\mathbb{{CP}}}^{\infty } \) have isomorphic cohomology rings with \( \mathbb{Z} \) or any other coefficients. [An exercise for \( \text{ § }4.\mathrm{L} \) is to show these two spaces are not homotopy equivalent.]

13. Describe \( {H}^{ * }\left( {{\mathbb{{CP}}}^{\infty }/{\mathbb{{CP}}}^{1};\mathbb{Z}}\right) \) as a ring with finitely many multiplicative generators. How does this ring compare with \( {H}^{ * }\left( {{S}^{6} \times  {\mathbb{{HP}}}^{\infty };\mathbb{Z}}\right) \) ?

14. Let \( q : {\mathbb{{RP}}}^{\infty } \rightarrow  {\mathbb{{CP}}}^{\infty } \) be the natural quotient map obtained by regarding both spaces as quotients of \( {S}^{\infty } \) , modulo multiplication by real scalars in one case and complex scalars in the other. Show that the induced map \( {q}^{ * } : {H}^{ * }\left( {{\mathbb{{CP}}}^{\infty };\mathbb{Z}}\right)  \rightarrow  {H}^{ * }\left( {{\mathbb{{RP}}}^{\infty };\mathbb{Z}}\right) \) is surjective in even dimensions by showing first by a geometric argument that the restriction \( q : {\mathbb{{RP}}}^{2} \rightarrow  {\mathbb{{CP}}}^{1} \) induces a surjection on \( {H}^{2} \) and then appealing to cup product structures. Next, form a quotient space \( X \) of \( {\mathbb{{RP}}}^{\infty } \coprod  {\mathbb{{CP}}}^{n} \) by identifying each point \( x \in  {\mathbb{{RP}}}^{2n} \) with \( q\left( x\right)  \in  {\mathbb{{CP}}}^{n} \) . Show there are ring isomorphisms \( {H}^{ * }\left( {X;\mathbb{Z}}\right)  \approx  \mathbb{Z}\left\lbrack  \alpha \right\rbrack  /\left( {2{\alpha }^{n + 1}}\right) \) and \( {H}^{ * }\left( {X;{\mathbb{Z}}_{2}}\right)  \approx  {\mathbb{Z}}_{2}\left\lbrack  {\alpha ,\beta }\right\rbrack  /\left( {{\beta }^{2} - {\alpha }^{{2n} + 1}}\right) \) , where \( \left| \alpha \right|  = 2 \) and \( \left| \beta \right|  = {2n} + 1 \) . Make a similar construction and analysis for the quotient map \( q : {\mathbb{{CP}}}^{\infty } \rightarrow  {\mathbb{{HP}}}^{\infty } \) .

15. For a fixed coefficient field \( F \) , define the Poincaré series of a space \( X \) to be the formal power series \( p\left( t\right)  = \mathop{\sum }\limits_{i}{a}_{i}{t}^{i} \) where \( {a}_{i} \) is the dimension of \( {H}^{i}\left( {X;F}\right) \) as a vector space over \( F \) , assuming this dimension is finite for all \( i \) . Show that \( p\left( {X \times  Y}\right)  = \; p\left( X\right) p\left( Y\right) \) . Compute the Poincaré series for \( {S}^{n},{\mathbb{{RP}}}^{n},{\mathbb{{RP}}}^{\infty },{\mathbb{{CP}}}^{n},{\mathbb{{CP}}}^{\infty } \) , and the spaces in the preceding three exercises.

16. Show that if \( X \) and \( Y \) are finite CW complexes such that \( {H}^{ * }\left( {X;\mathbb{Z}}\right) \) and \( {H}^{ * }\left( {Y;\mathbb{Z}}\right) \) contain no elements of order a power of a given prime \( p \) , then the same is true for \( X \times  Y \) . [Apply Theorem 3.15 with coefficients in various fields.]

17. [This has now been incorporated into Proposition 3.22.]

18. For the closed orientable surface \( M \) of genus \( g \geq  1 \) , show that for each nonzero \( \alpha  \in  {H}^{1}\left( {M;\mathbb{Z}}\right) \) there exists \( \beta  \in  {H}^{1}\left( {M;\mathbb{Z}}\right) \) with \( {\alpha \beta } \neq  0 \) . Deduce that \( M \) is not homotopy equivalent to a wedge sum \( X \vee  Y \) of CW complexes with nontrivial reduced homology. Do the same for closed nonorientable surfaces using cohomology with \( {\mathbb{Z}}_{2} \) coefficients.
