# 2.2 Computations and Applications

Now that the basic properties of homology have been established, we can begin to move a little more freely. Our first topic, exploiting the calculation of \( {H}_{n}\left( {S}^{n}\right) \) , is Brouwer’s notion of degree for maps \( {S}^{n} \rightarrow  {S}^{n} \) . Historically, Brouwer’s introduction of this concept in the years 1910-12 preceded the rigorous development of homology, so his definition was rather different, using the technique of simplicial approximation which we explain in §2.C. The later definition in terms of homology is certainly more elegant, though perhaps with some loss of geometric intuition. More in the spirit of Brouwer's definition is a third approach using differential topology, presented very lucidly in [Milnor 1965].

## Degree

For a map \( f : {S}^{n} \rightarrow  {S}^{n} \) with \( n > 0 \) , the induced map \( {f}_{ * } : {H}_{n}\left( {S}^{n}\right)  \rightarrow  {H}_{n}\left( {S}^{n}\right) \) is a homomorphism from an infinite cyclic group to itself and so must be of the form \( {f}_{ * }\left( \alpha \right)  = {d\alpha } \) for some integer \( d \) depending only on \( f \) . This integer is called the degree of \( f \) , with the notation \( \deg f \) . Here are some basic properties of degree:

(a) \( \deg \mathbb{1} = 1 \) , since \( {\mathbb{1}}_{ * } = \mathbb{1} \) .

(b) \( \deg f = 0 \) if \( f \) is not surjective. For if we choose a point \( {x}_{0} \in  {S}^{n} - f\left( {S}^{n}\right) \) then \( f \) can be factored as a composition \( {S}^{n} \rightarrow  {S}^{n} - \left\{  {x}_{0}\right\}   \hookrightarrow  {S}^{n} \) and \( {H}_{n}\left( {{S}^{n} - \left\{  {x}_{0}\right\}  }\right)  = 0 \) since \( {S}^{n} - \left\{  {x}_{0}\right\} \) is contractible. Hence \( {f}_{ * } = 0 \) .

(c) If \( f \simeq  g \) then \( \deg f = \deg g \) since \( {f}_{ * } = {g}_{ * } \) . The converse statement, that \( f \simeq  g \) if \( \deg f = \deg g \) , is a fundamental theorem of Hopf from around 1925 which we prove in Corollary 4.25.

(d) \( \deg {fg} = \deg f\deg g \) , since \( {\left( fg\right) }_{ * } = {f}_{ * }{g}_{ * } \) . As a consequence, \( \deg f =  \pm  1 \) if \( f \) is a homotopy equivalence since \( {fg} \simeq  \mathbb{1} \) implies \( \deg f\deg g = \deg \mathbb{1} = 1 \) .

(e) \( \deg f =  - 1 \) if \( f \) is a reflection of \( {S}^{n} \) , fixing the points in a subsphere \( {S}^{n - 1} \) and interchanging the two complementary hemispheres. For we can give \( {S}^{n} \) a \( \Delta \) -complex structure with these two hemispheres as its two \( n \) -simplices \( {\Delta }_{1}^{n} \) and \( {\Delta }_{2}^{n} \) , and the \( n \) -chain \( {\Delta }_{1}^{n} - {\Delta }_{2}^{n} \) represents a generator of \( {H}_{n}\left( {S}^{n}\right) \) as we saw in Example 2.23, so the reflection interchanging \( {\Delta }_{1}^{n} \) and \( {\Delta }_{2}^{n} \) sends this generator to its negative.

(f) The antipodal map \( - \mathbb{1} : {S}^{n} \rightarrow  {S}^{n}, x \mapsto   - x \) , has degree \( {\left( -1\right) }^{n + 1} \) since it is the composition of \( n + 1 \) reflections, each changing the sign of one coordinate in \( {\mathbb{R}}^{n + 1} \) .

(g) If \( f : {S}^{n} \rightarrow  {S}^{n} \) has no fixed points then \( \deg f = {\left( -1\right) }^{n + 1} \) . For if \( f\left( x\right)  \neq  x \) then the line segment from \( f\left( x\right) \) to \( - x \) , defined by \( t \mapsto  \left( {1 - t}\right) f\left( x\right)  - {tx} \) for \( 0 \leq  t \leq  1 \) , does not pass through the origin. Hence if \( f \) has no fixed points, the formula \( {f}_{t}\left( x\right)  = \left\lbrack  {\left( {1 - t}\right) f\left( x\right)  - {tx}}\right\rbrack  /\left| {\left( {1 - t}\right) f\left( x\right)  - {tx}}\right| \) defines a homotopy from \( f \) to the antipodal map. Note that the antipodal map has no fixed points, so the fact that maps without fixed points are homotopic to the antipodal map is a sort of converse statement.

Here is an interesting application of degree:

|| Theorem 2.28. \( {S}^{n} \) has a continuous field of nonzero tangent vectors iff \( n \) is odd.

Proof: Suppose \( x \mapsto  v\left( x\right) \) is a tangent vector field on \( {S}^{n} \) , assigning to a vector \( x \in  {S}^{n} \) the vector \( v\left( x\right) \) tangent to \( {S}^{n} \) at \( x \) . Regarding \( v\left( x\right) \) as a vector at the origin instead of at \( x \) , tangency just means that \( x \) and \( v\left( x\right) \) are orthogonal in \( {\mathbb{R}}^{n + 1} \) . If \( v\left( x\right)  \neq  0 \) for all \( x \) , we may normalize so that \( \left| {v\left( x\right) }\right|  = 1 \) for all \( x \) by replacing \( v\left( x\right) \) by \( v\left( x\right) /\left| {v\left( x\right) }\right| \) . Assuming this has been done, the vectors \( \left( {\cos t}\right) x + \left( {\sin t}\right) v\left( x\right) \) lie in the unit circle in the plane spanned by \( x \) and \( v\left( x\right) \) . Letting \( t \) go from 0 to \( \pi \) , we obtain a homotopy \( {f}_{t}\left( x\right)  = \left( {\cos t}\right) x + \left( {\sin t}\right) v\left( x\right) \) from the identity map of \( {S}^{n} \) to the antipodal map \( - \mathbb{1} \) . This implies that \( \deg \left( {-\mathbb{1}}\right)  = \deg \mathbb{1} \) , hence \( {\left( -1\right) }^{n + 1} = 1 \) and \( n \) must be odd.

Conversely, if \( n \) is odd, say \( n = {2k} - 1 \) , we can define \( v\left( {{x}_{1},{x}_{2},\cdots ,{x}_{{2k} - 1},{x}_{2k}}\right)  = \; \left( {-{x}_{2},{x}_{1},\cdots , - {x}_{2k},{x}_{{2k} - 1}}\right) \) . Then \( v\left( x\right) \) is orthogonal to \( x \) , so \( v \) is a tangent vector field on \( {S}^{n} \) , and \( \left| {v\left( x\right) }\right|  = 1 \) for all \( x \in  {S}^{n} \) .

For the much more difficult problem of finding the maximum number of tangent vector fields on \( {S}^{n} \) that are linearly independent at each point, see [VBKT] or [Husemoller 1966].

Another nice application of degree, giving a partial answer to a question raised in Example 1.43, is the following result:

Proposition 2.29. \( {\mathbb{Z}}_{2} \) is the only nontrivial group that can act freely on \( {S}^{n} \) if \( n \) is even.

Recall that an action of a group \( G \) on a space \( X \) is a homomorphism from \( G \) to the group Homeo \( \left( X\right) \) of homeomorphisms \( X \rightarrow  X \) , and the action is free if the homeomorphism corresponding to each nontrivial element of \( G \) has no fixed points. In the case of \( {S}^{n} \) , the antipodal map \( x \mapsto   - x \) generates a free action of \( {\mathbb{Z}}_{2} \) .

Proof: Since homeomorphisms have degree \( \pm  1 \) , an action of a group \( G \) on \( {S}^{n} \) determines a degree function \( d : G \rightarrow  \{  \pm  1\} \) . This is a homomorphism since \( \deg {fg} = \; \deg f\deg g \) . If the action is free, \( d \) sends each nontrivial element of \( G \) to \( {\left( -1\right) }^{n + 1} \) by property (g) above. Thus when \( n \) is even, \( d \) has trivial kernel, so \( G \subset  {\mathbb{Z}}_{2} \) .

Next we describe a technique for computing degrees which can be applied to most maps that arise in practice. Suppose \( f : {S}^{n} \rightarrow  {S}^{n}, n > 0 \) , has the property that for some point \( y \in  {S}^{n} \) , the preimage \( {f}^{-1}\left( y\right) \) consists of only finitely many points, say \( {x}_{1},\cdots ,{x}_{m} \) . Let \( {U}_{1},\cdots ,{U}_{m} \) be disjoint neighborhoods of these points, mapped by \( f \) into a neighborhood \( V \) of \( y \) . Then \( f\left( {{U}_{i} - {x}_{i}}\right)  \subset  V - y \) for each \( i \) , and we have a diagram

![bo_d7dtv0s91nqc73eq8nv0_144_353_259_1038_322_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_144_353_259_1038_322_0.jpg)

where all the maps are the obvious ones, and in particular \( {k}_{i} \) and \( {p}_{i} \) are induced by inclusions, so the triangles and squares commute. The two isomorphisms in the upper half of the diagram come from excision, while the lower two isomorphisms come from exact sequences of pairs. Via these four isomorphisms, the top two groups in the diagram can be identified with \( {H}_{n}\left( {S}^{n}\right)  \approx  \mathbb{Z} \) , and the top homomorphism \( {f}_{ * } \) becomes multiplication by an integer called the local degree of \( f \) at \( {x}_{i} \) , written \( \deg f \mid  {x}_{i} \) .

For example, if \( f \) is a homeomorphism, then \( y \) can be any point and there is only one corresponding \( {x}_{i} \) , so all the maps in the diagram are isomorphisms and \( \deg f \mid  {x}_{i} = \deg f =  \pm  1 \) . More generally, if \( f \) maps each \( {U}_{i} \) homeomorphically onto \( V \) , then \( \deg f \mid  {x}_{i} =  \pm  1 \) for each \( i \) . This situation occurs quite often in applications, and it is usually not hard to determine the correct signs.

Here is the formula that reduces degree calculations to computing local degrees:

\( \mid \) Proposition 2.30. \( \deg f = \mathop{\sum }\limits_{i}\deg f \mid  {x}_{i} \) .

Proof: By excision, the central term \( {H}_{n}\left( {{S}^{n},{S}^{n} - {f}^{-1}\left( y\right) }\right) \) in the preceding diagram is the direct sum of the groups \( {H}_{n}\left( {{U}_{i},{U}_{i} - {x}_{i}}\right)  \approx  \mathbb{Z} \) , with \( {k}_{i} \) the inclusion of the \( {i}^{\text{ th }} \) summand. The map \( {p}_{i} \) is projection onto the \( {i}^{th} \) summand since the upper triangle commutes and \( {p}_{i}{k}_{j} = 0 \) for \( j \neq  i \) , as \( {p}_{i}{k}_{j} \) factors through \( {H}_{n}\left( {{U}_{j},{U}_{j}}\right)  = 0 \) . Identifying the outer groups in the diagram with \( \mathbb{Z} \) as before, commutativity of the lower triangle says that \( {p}_{i}j\left( 1\right)  = 1 \) , hence \( j\left( 1\right)  = \left( {1,\cdots ,1}\right)  = \mathop{\sum }\limits_{i}{k}_{i}\left( 1\right) \) . Commutativity of the upper square says that the middle \( {f}_{ * } \) takes \( {k}_{i}\left( 1\right) \) to \( \deg f \mid  {x}_{i} \) , hence the sum \( \mathop{\sum }\limits_{i}{k}_{i}\left( 1\right)  = j\left( 1\right) \) is taken to \( \mathop{\sum }\limits_{i}\deg f \mid  {x}_{i} \) . Commutativity of the lower square then gives the formula \( \deg f = \mathop{\sum }\limits_{i}\deg f \mid  {x}_{i} \) .

Example 2.31. We can use this result to construct a map \( {S}^{n} \rightarrow  {S}^{n} \) of any given degree, for each \( n \geq  1 \) . Let \( q : {S}^{n} \rightarrow  \mathop{\bigvee }\limits_{k}{S}^{n} \) be the quotient map obtained by collapsing the complement of \( k \) disjoint open balls \( {B}_{i} \) in \( {S}^{n} \) to a point, and let \( p : \mathop{\bigvee }\limits_{k}{S}^{n} \rightarrow  {S}^{n} \) identify all the summands to a single sphere. Consider the composition \( f = {pq} \) . For almost all \( y \in  {S}^{n} \) we have \( {f}^{-1}\left( y\right) \) consisting of one point \( {x}_{i} \) in each \( {B}_{i} \) . The local degree of \( f \) at \( {x}_{i} \) is \( \pm  1 \) since \( f \) is a homeomorphism near \( {x}_{i} \) . By precomposing \( p \) with reflections of the summands of \( \mathop{\bigvee }\limits_{k}{S}^{n} \) if necessary, we can make each local degree either +1 or -1, whichever we wish. Thus we can produce a map \( {S}^{n} \rightarrow  {S}^{n} \) of degree \( \pm  k \) .

Example 2.32. In the case of \( {S}^{1} \) , the map \( f\left( z\right)  = {z}^{k} \) , where we view \( {S}^{1} \) as the unit circle in \( \mathbb{C} \) , has degree \( k \) . This is evident in the case \( k = 0 \) since \( f \) is then constant. The case \( k < 0 \) reduces to the case \( k > 0 \) by composing with \( z \mapsto  {z}^{-1} \) , which is a reflection, of degree -1 . To compute the degree when \( k > 0 \) , observe first that for any \( y \in  {S}^{1},{f}^{-1}\left( y\right) \) consists of \( k \) points \( {x}_{1},\cdots ,{x}_{k} \) near each of which \( f \) is a local homeomorphism, stretching a circular arc by a factor of \( k \) . This local stretching can be eliminated by a deformation of \( f \) near \( {x}_{i} \) that does not change local degree, so the local degree at \( {x}_{i} \) is the same as for a rotation of \( {S}^{1} \) . A rotation is a homeomorphism so its local degree at any point equals its global degree, which is +1 since a rotation is homotopic to the identity. Hence \( \deg f \mid  {x}_{i} = 1 \) and \( \deg f = k \) .

Another way of obtaining a map \( {S}^{n} \rightarrow  {S}^{n} \) of degree \( k \) is to take a repeated suspension of the map \( z \mapsto  {z}^{k} \) in Example 2.32, since suspension preserves degree:

Proposition 2.33. \( \deg {Sf} = \deg f \) , where \( {Sf} : {S}^{n + 1} \rightarrow  {S}^{n + 1} \) is the suspension of the map \( f : {S}^{n} \rightarrow  {S}^{n} \) .

Proof: Let \( C{S}^{n} \) denote the cone \( \left( {{S}^{n} \times  I}\right) /\left( {{S}^{n} \times  1}\right) \) with base \( {S}^{n} = {S}^{n} \times  0 \subset  C{S}^{n} \) , so \( C{S}^{n}/{S}^{n} \) is the suspension of \( {S}^{n} \) . The map \( f \) induces \( {Cf} : \left( {C{S}^{n},{S}^{n}}\right)  \rightarrow  \left( {C{S}^{n},{S}^{n}}\right) \) with quotient \( {Sf} \) . The naturality of the boundary maps in the long exact sequence of the pair \( \left( {C{S}^{n},{S}^{n}}\right) \) then gives commutativity of the diagram at the right. Hence if \( {f}_{ * } \) is multiplication by \( d \) , so is \( S{f}_{ * } \) .

\( {\widetilde{H}}_{n + 1}\left( {S}^{n + 1}\right) \underset{ \approx  }{\overset{\partial }{ \rightarrow  }}{\widetilde{H}}_{n}\left( {S}^{n}\right) \)

\( \int S{f}_{ * } \)

\[
{\widetilde{H}}_{n + 1}\left( {S}^{n + 1}\right) \underset{ \approx  }{ \approx  }{\widetilde{H}}_{n}\left( {S}^{n}\right)
\]

Note that for \( f : {S}^{n} \rightarrow  {S}^{n} \) , the suspension \( {Sf} \) maps only one point to each of the two ’poles’ of \( {S}^{n + 1} \) . This implies that the local degree of \( {Sf} \) at each pole must equal the global degree of \( {Sf} \) . Thus the local degree of a map \( {S}^{n} \rightarrow  {S}^{n} \) can be any integer if \( n \geq  2 \) , just as the degree itself can be any integer when \( n \geq  1 \) .

## Cellular Homology

Cellular homology is a very efficient tool for computing the homology groups of CW complexes, based on degree calculations. Before giving the definition of cellular homology, we first establish a few preliminary facts:

Lemma 2.34. If \( X \) is a CW complex, then:

(a) \( {H}_{k}\left( {{X}^{n},{X}^{n - 1}}\right) \) is zero for \( k \neq  n \) and is free abelian for \( k = n \) , with a basis in one-to-one correspondence with the \( n \) -cells of \( X \) .

(b) \( {H}_{k}\left( {X}^{n}\right)  = 0 \) for \( k > n \) . In particular, if \( X \) is finite-dimensional then \( {H}_{k}\left( X\right)  = 0 \) for \( k > \dim X \) .

(c) The map \( {H}_{k}\left( {X}^{n}\right)  \rightarrow  {H}_{k}\left( X\right) \) induced by the inclusion \( {X}^{n} \hookrightarrow  X \) is an isomorphism for \( k < n \) and surjective for \( k = n \) .

Proof: Statement (a) follows immediately from the observation that \( \left( {{X}^{n},{X}^{n - 1}}\right) \) is a good pair and \( {X}^{n}/{X}^{n - 1} \) is a wedge sum of \( n \) -spheres, one for each \( n \) -cell of \( X \) . Here we are using Proposition 2.22 and Corollary 2.25. Next consider the following part of the long exact sequence of the pair \( \left( {{X}^{n},{X}^{n - 1}}\right) \) :

\[
{H}_{k + 1}\left( {{X}^{n},{X}^{n - 1}}\right)  \rightarrow  {H}_{k}\left( {X}^{n - 1}\right)  \rightarrow  {H}_{k}\left( {X}^{n}\right)  \rightarrow  {H}_{k}\left( {{X}^{n},{X}^{n - 1}}\right)
\]

If \( k \neq  n \) the last term is zero by part (a) so the middle map is surjective, while if \( k \neq  n - 1 \) then the first term is zero so the middle map is injective. Now look at the inclusion-induced homomorphisms

\[
{H}_{k}\left( {X}^{0}\right)  \rightarrow  {H}_{k}\left( {X}^{1}\right)  \rightarrow  \cdots  \rightarrow  {H}_{k}\left( {X}^{k - 1}\right)  \rightarrow  {H}_{k}\left( {X}^{k}\right)  \rightarrow  {H}_{k}\left( {X}^{k + 1}\right)  \rightarrow  \cdots
\]

By what we have just shown these are all isomorphisms except that the map to \( {H}_{k}\left( {X}^{k}\right) \) may not be surjective and the map from \( {H}_{k}\left( {X}^{k}\right) \) may not be injective. The first part of the sequence then gives statement (b) since \( {H}_{k}\left( {X}^{0}\right)  = 0 \) when \( k > 0 \) . Also, the last part of the sequence gives (c) when \( X \) is finite-dimensional.

The proof of (c) when \( X \) is infinite-dimensional requires more work, and this can be done in two different ways. The more direct approach is to descend to the chain level and use the fact that a singular chain in \( X \) has compact image, hence meets only finitely many cells of \( X \) by Proposition A. 1 in the Appendix. Thus each chain lies in a finite skeleton \( {X}^{m} \) . So a \( k \) -cycle in \( X \) is a cycle in some \( {X}^{m} \) , and then by the finite-dimensional case of (c), the cycle is homologous to a cycle in \( {X}^{n} \) if \( n \geq  k \) , so \( {H}_{k}\left( {X}^{n}\right)  \rightarrow  {H}_{k}\left( X\right) \) is surjective. Similarly for injectivity, if a \( k \) -cycle in \( {X}^{n} \) bounds a chain in \( X \) , this chain lies in some \( {X}^{m} \) with \( m \geq  n \) , so by the finite-dimensional case the cycle bounds a chain in \( {X}^{n} \) if \( n > k \) .

The other approach is more general. From the long exact sequence of the pair \( \left( {X,{X}^{n}}\right) \) it suffices to show \( {H}_{k}\left( {X,{X}^{n}}\right)  = 0 \) for \( k \leq  n \) . Since \( {H}_{k}\left( {X,{X}^{n}}\right)  \approx  {\widetilde{H}}_{k}\left( {X/{X}^{n}}\right) \) , this reduces the problem to showing:

(*) \( {\widetilde{H}}_{k}\left( X\right)  = 0 \) for \( k \leq  n \) if the \( n \) -skeleton of \( X \) is a point.

When \( X \) is finite-dimensional, \( \left( *\right) \) is immediate from the finite-dimensional case of (c) which we have already shown. It will suffice therefore to reduce the infinite-dimensional case to the finite-dimensional case. This reduction will be achieved by stretching \( X \) out to a complex that is at least locally finite-dimensional, using a special case of the 'mapping telescope' construction described in greater generality in §3.F.

Consider \( X \times  \lbrack 0,\infty ) \) with its product cell structure, where we give \( \lbrack 0,\infty ) \) the cell structure with the integer points as 0-cells. Let \( T = \mathop{\bigcup }\limits_{i}{X}^{i} \times  \lbrack i,\infty ) \) , a subcomplex of \( X \times  \lbrack 0,\infty ) \) . The figure shows a schematic picture of \( T \) with \( \lbrack 0,\infty ) \) in the horizontal direction and the subcomplexes \( {X}^{i} \times  \left\lbrack  {i, i + 1}\right\rbrack \) as rectangles whose size increases with \( i \) since \( {X}^{i} \subset  {X}^{i + 1} \) . The line labeled \( R \) can be ignored for now. We claim that \( T \simeq  X \) , hence \( {H}_{k}\left( X\right)  \approx  {H}_{k}\left( T\right) \) for all \( k \) . Since \( X \) is a deformation retract of \( X \times  \lbrack 0,\infty ) \) , it suffices to show that \( X \times  \lbrack 0,\infty ) \) also deformation retracts onto \( T \) . Let \( {Y}_{i} = T \cup  \left( {X\times \lbrack i,\infty }\right) ) \) . Then \( {Y}_{i} \) deformation retracts onto \( {Y}_{i + 1} \) since \( X \times  \left\lbrack  {i, i + 1}\right\rbrack \) deformation retracts onto \( {X}^{i} \times  \left\lbrack  {i, i + 1}\right\rbrack   \cup  X \times  \{ i + 1\} \) by Proposition 0.16 . If we perform the deformation retraction of \( {Y}_{i} \) onto \( {Y}_{i + 1} \) during the \( t \) -interval \( \left\lbrack  {1 - 1/{2}^{i},1 - 1/{2}^{i + 1}}\right\rbrack \) , then this gives a deformation retraction \( {f}_{t} \) of \( X \times  \lbrack 0,\infty ) \) onto \( T \) , with points in \( {X}^{i} \times  \lbrack 0,\infty ) \) stationary under \( {f}_{t} \) for \( t \geq  1 - 1/{2}^{i + 1} \) . Continuity follows from the fact that CW complexes have the weak topology with respect to their skeleta, so a map is continuous if its restriction to each skeleton is continuous.

![bo_d7dtv0s91nqc73eq8nv0_146_1156_1765_424_135_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_146_1156_1765_424_135_0.jpg)

Recalling that \( {X}^{0} \) is a point, let \( R \subset  T \) be the ray \( {X}^{0} \times  \lbrack 0,\infty ) \) and let \( Z \subset  T \) be the union of this ray with all the subcomplexes \( {X}^{i} \times  \{ i\} \) . Then \( Z/R \) is homeomorphic to \( \mathop{\bigvee }\limits_{i}{X}^{i} \) , a wedge sum of finite-dimensional complexes with \( n \) -skeleton a point, so the finite-dimensional case of \( \left( *\right) \) together with Corollary 2.25 describing the homology of wedge sums implies that \( {\widetilde{H}}_{k}\left( {Z/R}\right)  = 0 \) for \( k \leq  n \) . The same is therefore true for \( Z \) , from the long exact sequence of the pair \( \left( {Z, R}\right) \) , since \( R \) is contractible. Similarly, \( T/Z \) is a wedge sum of finite-dimensional complexes with \( \left( {n + 1}\right) \) -skeleton a point, since if we first collapse each subcomplex \( {X}^{i} \times  \{ i\} \) of \( T \) to a point, we obtain the infinite sequence of suspensions \( S{X}^{i} \) ’skewered’ along the ray \( R \) , and then if we collapse \( R \) to a point we obtain \( \mathop{\bigvee }\limits_{i}\sum {X}^{i} \) where \( \sum {X}^{i} \) is the reduced suspension of \( {X}^{i} \) , obtained from \( S{X}^{i} \) by collapsing the line segment \( {X}^{0} \times  \left\lbrack  {i, i + 1}\right\rbrack \) to a point, so \( \sum {X}^{i} \) has \( \left( {n + 1}\right) \) -skeleton a point. Thus \( {\widetilde{H}}_{k}\left( {T/Z}\right)  = 0 \) for \( k \leq  n + 1 \) . The long exact sequence of the pair \( \left( {T, Z}\right) \) then implies that \( {\widetilde{H}}_{k}\left( T\right)  = 0 \) for \( k \leq  n \) , and we have proved \( \left( *\right) \) .

Let \( X \) be a CW complex. Using Lemma 2.34, portions of the long exact sequences for the pairs \( \left( {{X}^{n + 1},{X}^{n}}\right) ,\left( {{X}^{n},{X}^{n - 1}}\right) \) , and \( \left( {{X}^{n - 1},{X}^{n - 2}}\right) \) fit into a diagram

![bo_d7dtv0s91nqc73eq8nv0_147_217_1240_1368_532_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_147_217_1240_1368_532_0.jpg)

where \( {d}_{n + 1} \) and \( {d}_{n} \) are defined as the compositions \( {j}_{n}{\partial }_{n + 1} \) and \( {j}_{n - 1}{\partial }_{n} \) , which are just ’relativizations’ of the boundary maps \( {\partial }_{n + 1} \) and \( {\partial }_{n} \) . The composition \( {d}_{n}{d}_{n + 1} \) includes two successive maps in one of the exact sequences, hence is zero. Thus the horizontal row in the diagram is a chain complex, called the cellular chain complex of \( X \) since \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) is free with basis in one-to-one correspondence with the \( n \) -cells of \( X \) , so one can think of elements of \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) as linear combinations of \( n \) -cells of \( X \) . The homology groups of this cellular chain complex are called the cellular homology groups of \( X \) . Temporarily we denote them \( {H}_{n}^{CW}\left( X\right) \) .

Theorem 2.35. \( {H}_{n}^{CW}\left( X\right)  \approx  {H}_{n}\left( X\right) \) .

Proof: From the diagram above, \( {H}_{n}\left( X\right) \) can be identified with \( {H}_{n}\left( {X}^{n}\right) /\operatorname{Im}{\partial }_{n + 1} \) . Since \( {j}_{n} \) is injective, it maps \( \operatorname{Im}{\partial }_{n + 1} \) isomorphically onto \( \operatorname{Im}\left( {{j}_{n}{\partial }_{n + 1}}\right)  = \operatorname{Im}{d}_{n + 1} \) and \( {H}_{n}\left( {X}^{n}\right) \) isomorphically onto \( \operatorname{Im}{j}_{n} = \operatorname{Ker}{\partial }_{n} \) . Since \( {j}_{n - 1} \) is injective, \( \operatorname{Ker}{\partial }_{n} = \) Ker \( {d}_{n} \) . Thus \( {j}_{n} \) induces an isomorphism of the quotient \( {H}_{n}\left( {X}^{n}\right) /\operatorname{Im}{\partial }_{n + 1} \) onto \( \operatorname{Ker}{d}_{n}/\operatorname{Im}{d}_{n + 1} \) .

Here are a few immediate applications:

(i) \( {H}_{n}\left( X\right)  = 0 \) if \( X \) is a CW complex with no \( n \) -cells.

(ii) More generally, if \( X \) is a CW complex with \( kn \) -cells, then \( {H}_{n}\left( X\right) \) is generated by at most \( k \) elements. For since \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) is free abelian on \( k \) generators, the subgroup \( \operatorname{Ker}{d}_{n} \) must be generated by at most \( k \) elements, hence also the quotient Ker \( {d}_{n}/\operatorname{Im}{d}_{n + 1} \) .

(iii) If \( X \) is a CW complex having no two of its cells in adjacent dimensions, then \( {H}_{n}\left( X\right) \) is free abelian with basis in one-to-one correspondence with the \( n \) -cells of \( X \) . This is because the cellular boundary maps \( {d}_{n} \) are automatically zero in this case.

This last observation applies for example to \( {\mathbb{{CP}}}^{n} \) , which has a CW structure with one cell of each even dimension \( {2k} \leq  {2n} \) as we saw in Example 0.6. Thus

\[
{H}_{i}\left( {\mathbb{{CP}}}^{n}\right)  \approx  \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }i = 0,2,4,\cdots ,{2n} \\  0 & \text{ otherwise } \end{array}\right.
\]

Another simple example is \( {S}^{n} \times  {S}^{n} \) with \( n > 1 \) , using the product CW structure consisting of a 0-cell, two \( n \) -cells, and a \( {2n} \) -cell.

It is possible to prove the statements (i)-(iii) for finite-dimensional CW complexes by induction on the dimension, without using cellular homology but only the basic results from the previous section. However, the viewpoint of cellular homology makes (i)-(iii) quite transparent.

Next we describe how the cellular boundary maps \( {d}_{n} \) can be computed. When \( n = 1 \) this is easy since the boundary map \( {d}_{1} : {H}_{1}\left( {{X}^{1},{X}^{0}}\right)  \rightarrow  {H}_{0}\left( {X}^{0}\right) \) is the same as the simplicial boundary map \( {\Delta }_{1}\left( X\right)  \rightarrow  {\Delta }_{0}\left( X\right) \) . In case \( X \) is connected and has only one 0 -cell, then \( {d}_{1} \) must be 0, otherwise \( {H}_{0}\left( X\right) \) would not be \( \mathbb{Z} \) . When \( n > 1 \) we will show that \( {d}_{n} \) can be computed in terms of degrees:

Cellular Boundary Formula. \( {d}_{n}\left( {e}_{\alpha }^{n}\right)  = \mathop{\sum }\limits_{\beta }{d}_{\alpha \beta }{e}_{\beta }^{n - 1} \) where \( {d}_{\alpha \beta } \) is the degree of the map \( {S}_{\alpha }^{n - 1} \rightarrow  {X}^{n - 1} \rightarrow  {S}_{\beta }^{n - 1} \) that is the composition of the attaching map of \( {e}_{\alpha }^{n} \) with the quotient map collapsing \( {X}^{n - 1} - {e}_{\beta }^{n - 1} \) to a point.

Here we are identifying the cells \( {e}_{\alpha }^{n} \) and \( {e}_{\beta }^{n - 1} \) with generators of the corresponding summands of the cellular chain groups. The summation in the formula contains only finitely many terms since the attaching map of \( {e}_{\alpha }^{n} \) has compact image, so this image meets only finitely many cells \( {e}_{\beta }^{n - 1} \) .

To derive the cellular boundary formula, consider the commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_149_319_138_1159_352_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_149_319_138_1159_352_0.jpg)

where:

- \( {\Phi }_{\alpha } \) is the characteristic map of the cell \( {e}_{\alpha }^{n} \) and \( {\varphi }_{\alpha } \) is its attaching map.

- \( q : {X}^{n - 1} \rightarrow  {X}^{n - 1}/{X}^{n - 2} \) is the quotient map.

- \( {q}_{\beta } : {X}^{n - 1}/{X}^{n - 2} \rightarrow  {S}_{\beta }^{n - 1} \) collapses the complement of the cell \( {e}_{\beta }^{n - 1} \) to a point, the resulting quotient sphere being identified with \( {S}_{\beta }^{n - 1} = {D}_{\beta }^{n - 1}/\partial {D}_{\beta }^{n - 1} \) via the characteristic map \( {\Phi }_{\beta } \) .

- \( {\Delta }_{\alpha \beta } : \partial {D}_{\alpha }^{n} \rightarrow  {S}_{\beta }^{n - 1} \) is the composition \( {q}_{\beta }q{\varphi }_{\alpha } \) , in other words, the attaching map of \( {e}_{\alpha }^{n} \) followed by the quotient map \( {X}^{n - 1} \rightarrow  {S}_{\beta }^{n - 1} \) collapsing the complement of \( {e}_{\beta }^{n - 1} \) in \( {X}^{n - 1} \) to a point.

The map \( {\Phi }_{\alpha  * } \) takes a chosen generator \( \left\lbrack  {D}_{\alpha }^{n}\right\rbrack   \in  {H}_{n}\left( {{D}_{\alpha }^{n},\partial {D}_{\alpha }^{n}}\right) \) to a generator of the \( \mathbb{Z} \) summand of \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) corresponding to \( {e}_{\alpha }^{n} \) . Letting \( {e}_{\alpha }^{n} \) denote this generator, commutativity of the left half of the diagram then gives \( {d}_{n}\left( {e}_{\alpha }^{n}\right)  = {j}_{n - 1}{\varphi }_{\alpha  * }\partial \left\lbrack  {D}_{\alpha }^{n}\right\rbrack \) . In terms of the basis for \( {H}_{n - 1}\left( {{X}^{n - 1},{X}^{n - 2}}\right) \) corresponding to the cells \( {e}_{\beta }^{n - 1} \) , the map \( {q}_{\beta  * } \) is the projection of \( {\widetilde{H}}_{n - 1}\left( {{X}^{n - 1}/{X}^{n - 2}}\right) \) onto its \( \mathbb{Z} \) summand corresponding to \( {e}_{\beta }^{n - 1} \) . Commutativity of the diagram then yields the formula for \( {d}_{n} \) given above.

Example 2.36. Let \( {M}_{g} \) be the closed orientable surface of genus \( g \) with its usual CW structure consisting of one 0-cell, \( {2g} \) 1-cells, and one 2-cell attached by the product of commutators \( \left\lbrack  {{a}_{1},{b}_{1}}\right\rbrack  \cdots \left\lbrack  {{a}_{g},{b}_{g}}\right\rbrack \) . The associated cellular chain complex is

\[
0 \rightarrow  \mathbb{Z}\xrightarrow[]{{d}_{2}}{\mathbb{Z}}^{2g}\xrightarrow[]{{d}_{1}}\mathbb{Z} \rightarrow  0
\]

As observed above, \( {d}_{1} \) must be 0 since there is only one 0-cell. Also, \( {d}_{2} \) is 0 because each \( {a}_{i} \) or \( {b}_{i} \) appears with its inverse in \( \left\lbrack  {{a}_{1},{b}_{1}}\right\rbrack  \cdots \left\lbrack  {{a}_{g},{b}_{g}}\right\rbrack \) , so the maps \( {\Delta }_{\alpha \beta } \) are homotopic to constant maps. Since \( {d}_{1} \) and \( {d}_{2} \) are both zero, the homology groups of \( {M}_{g} \) are the same as the cellular chain groups, namely, \( \mathbb{Z} \) in dimensions 0 and 2, and \( {\mathbb{Z}}^{2g} \) in dimension 1 .

Example 2.37. The closed nonorientable surface \( {N}_{g} \) of genus \( g \) has a cell structure with one 0-cell, \( g \) 1-cells, and one 2-cell attached by the word \( {a}_{1}^{2}{a}_{2}^{2}\cdots {a}_{g}^{2} \) . Again \( {d}_{1} = 0 \) , and \( {d}_{2} : \mathbb{Z} \rightarrow  {\mathbb{Z}}^{g} \) is specified by the equation \( {d}_{2}\left( 1\right)  = \left( {2,\cdots ,2}\right) \) since each \( {a}_{i} \) appears in the attaching word of the 2-cell with total exponent 2, which means that each \( {\Delta }_{\alpha \beta } \) is homotopic to the map \( z \mapsto  {z}^{2} \) , of degree 2. Since \( {d}_{2}\left( 1\right)  = \left( {2,\cdots ,2}\right) \) , we have \( {d}_{2} \) injective and hence \( {H}_{2}\left( {N}_{g}\right)  = 0 \) . If we change the basis for \( {\mathbb{Z}}^{g} \) by replacing the last standard basis element \( \left( {0,\cdots ,0,1}\right) \) by \( \left( {1,\cdots ,1}\right) \) , we see that \( {H}_{1}\left( {N}_{g}\right)  \approx \; {\mathbb{Z}}^{g - 1} \oplus  {\mathbb{Z}}_{2} \) .

These two examples illustrate the general fact that the orientability of a closed connected manifold \( M \) of dimension \( n \) is detected by \( {H}_{n}\left( M\right) \) , which is \( \mathbb{Z} \) if \( M \) is orientable and 0 otherwise. This is shown in Theorem 3.26.

Example 2.38: An Acyclic Space. Let \( X \) be obtained from \( {S}^{1} \vee  {S}^{1} \) by attaching two 2-cells by the words \( {a}^{5}{b}^{-3} \) and \( {b}^{3}{\left( ab\right) }^{-2} \) . Then \( {d}_{2} : {\mathbb{Z}}^{2} \rightarrow  {\mathbb{Z}}^{2} \) has matrix \( \left( \begin{array}{rr} 5 &  - 2 \\   - 3 & 1 \end{array}\right) \) , with the two columns coming from abelianizing \( {a}^{5}{b}^{-3} \) and \( {b}^{3}{\left( ab\right) }^{-2} \) to \( {5a} - {3b} \) and \( - {2a} + b \) , in additive notation. The matrix has determinant -1, so \( {d}_{2} \) is an isomorphism and \( {\widetilde{H}}_{i}\left( X\right)  = 0 \) for all \( i \) . Such a space \( X \) is called acyclic.

We can see that this acyclic space is not contractible by considering \( {\pi }_{1}\left( X\right) \) , which has the presentation \( \left\langle  {a, b \mid  {a}^{5}{b}^{-3},{b}^{3}{\left( ab\right) }^{-2}}\right\rangle \) . There is a nontrivial homomorphism from this group to the group \( G \) of rotational symmetries of a regular dodecahedron, sending \( a \) to the rotation \( {\rho }_{a} \) through angle \( {2\pi }/5 \) about the axis through the center of a pentagonal face, and \( b \) to the rotation \( {\rho }_{b} \) through angle \( {2\pi }/3 \) about the axis through a vertex of this face. The composition \( {\rho }_{a}{\rho }_{b} \) is a rotation through angle \( \pi \) about the axis through the midpoint of an edge abutting this vertex. Thus the relations \( {a}^{5} = {b}^{3} = {\left( ab\right) }^{2} \) defining \( {\pi }_{1}\left( X\right) \) become \( {\rho }_{a}^{5} = {\rho }_{b}^{3} = {\left( {\rho }_{a}{\rho }_{b}\right) }^{2} = 1 \) in \( G \) , which means there is a well-defined homomorphism \( \rho  : {\pi }_{1}\left( X\right)  \rightarrow  G \) sending \( a \) to \( {\rho }_{a} \) and \( b \) to \( {\rho }_{b} \) . It is not hard to see that \( G \) is generated by \( {\rho }_{a} \) and \( {\rho }_{b} \) , so \( \rho \) is surjective. With more work one can compute that the kernel of \( \rho \) is \( {\mathbb{Z}}_{2} \) , generated by the element \( {a}^{5} = {b}^{3} = {\left( ab\right) }^{2} \) , and this \( {\mathbb{Z}}_{2} \) is in fact the center of \( {\pi }_{1}\left( X\right) \) . In particular, \( {\pi }_{1}\left( X\right) \) has order 120 since \( G \) has order 60 .

After these 2-dimensional examples, let us now move up to three dimensions, where we have the additional task of computing the cellular boundary map \( {d}_{3} \) .

Example 2.39. A 3-dimensional torus \( {T}^{3} = {S}^{1} \times  {S}^{1} \times  {S}^{1} \) can be constructed from a cube by identifying each pair of opposite square faces as in the first of the two figures. The second figure shows a slightly different pattern of identifications of opposite faces, with the front and back faces now identified via a rotation of the cube around a horizontal left-right axis. The space produced by these identifications is the product \( K \times  {S}^{1} \) of a Klein bottle and a circle. For both \( {T}^{3} \) and \( K \times  {S}^{1} \) we have a CW structure with one 3-cell, three 2-cells, three 1-cells, and one 0 -cell. The cellular chain complexes thus have the form

\[
0 \rightarrow  \mathbb{Z}\overset{{d}_{3}}{ \rightarrow  }{\mathbb{Z}}^{3}\overset{{d}_{2}}{ \rightarrow  }{\mathbb{Z}}^{3}\overset{0}{ \rightarrow  }\mathbb{Z} \rightarrow  0
\]

![bo_d7dtv0s91nqc73eq8nv0_150_853_1432_736_302_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_150_853_1432_736_302_0.jpg)

In the case of the 3-torus \( {T}^{3} \) the cellular boundary map \( {d}_{2} \) is zero by the same calculation as for the 2-dimensional torus. We claim that \( {d}_{3} \) is zero as well. This amounts to saying that the three maps \( {\Delta }_{\alpha \beta } : {S}^{2} \rightarrow  {S}^{2} \) corresponding to the three 2-cells have degree zero. Each \( {\Delta }_{\alpha \beta } \) maps the interiors of two opposite faces of the cube homeomorphically onto the complement of a point in the target \( {S}^{2} \) and sends the remaining four faces to this point. Computing local degrees at the center points of the two opposite faces, we see that the local degree is +1 at one of these points and -1 at the other, since the restrictions of \( {\Delta }_{\alpha \beta } \) to these two faces differ by a reflection of the boundary of the cube across the plane midway between them, and a reflection has degree -1 . Since the cellular boundary maps are all zero, we deduce that \( {H}_{i}\left( {T}^{3}\right) \) is \( \mathbb{Z} \) for \( i = 0,3,{\mathbb{Z}}^{3} \) for \( i = 1,2 \) , and 0 for \( i > 3 \) .

For \( K \times  {S}^{1} \) , when we compute local degrees for the front and back faces we find that the degrees now have the same rather than opposite signs since the map \( {\Delta }_{\alpha \beta } \) on these two faces differs not by a reflection but by a rotation of the boundary of the cube. The local degrees for the other faces are the same as before. Using the letters \( A, B, C \) to denote the 2-cells given by the faces orthogonal to the edges \( a, b, c \) , respectively, we have the boundary formulas \( {d}_{3}{e}^{3} = {2C},{d}_{2}A = {2b},{d}_{2}B = 0 \) , and \( {d}_{2}C = 0 \) . It follows that \( {H}_{3}\left( {K \times  {S}^{1}}\right)  = 0,{H}_{2}\left( {K \times  {S}^{1}}\right)  = \mathbb{Z} \oplus  {\mathbb{Z}}_{2} \) , and \( {H}_{1}\left( {K \times  {S}^{1}}\right)  = \mathbb{Z} \oplus  \mathbb{Z} \oplus  {\mathbb{Z}}_{2} \) .

Many more examples of a similar nature, quotients of a cube or other polyhedron with faces identified in some pattern, could be worked out in similar fashion. But let us instead turn to some higher-dimensional examples.

Example 2.40: Moore Spaces. Given an abelian group \( G \) and an integer \( n \geq  1 \) , we will construct a CW complex \( X \) such that \( {H}_{n}\left( X\right)  \approx  G \) and \( {\widetilde{H}}_{i}\left( X\right)  = 0 \) for \( i \neq  n \) . Such a space is called a Moore space, commonly written \( M\left( {G, n}\right) \) to indicate the dependence on \( G \) and \( n \) . It is probably best for the definition of a Moore space to include the condition that \( M\left( {G, n}\right) \) be simply-connected if \( n > 1 \) . The spaces we construct will have this property.

As an easy special case, when \( G = {\mathbb{Z}}_{m} \) we can take \( X \) to be \( {S}^{n} \) with a cell \( {e}^{n + 1} \) attached by a map \( {S}^{n} \rightarrow  {S}^{n} \) of degree \( m \) . More generally, any finitely generated \( G \) can be realized by taking wedge sums of examples of this type for finite cyclic summands of \( G \) , together with copies of \( {S}^{n} \) for infinite cyclic summands of \( G \) .

In the general nonfinitely generated case let \( F \rightarrow  G \) be a homomorphism of a free abelian group \( F \) onto \( G \) , sending a basis for \( F \) onto some set of generators of \( G \) . The kernel \( K \) of this homomorphism is a subgroup of a free abelian group, hence is itself free abelian. Choose bases \( \left\{  {x}_{\alpha }\right\} \) for \( F \) and \( \left\{  {y}_{\beta }\right\} \) for \( K \) , and write \( {y}_{\beta } = \mathop{\sum }\limits_{\alpha }{d}_{\beta \alpha }{x}_{\alpha } \) . Let \( {X}^{n} = \mathop{\bigvee }\limits_{\alpha }{S}_{\alpha }^{n} \) , so \( {H}_{n}\left( {X}^{n}\right)  \approx  F \) via Corollary 2.25. We will construct \( X \) from \( {X}^{n} \) by attaching cells \( {e}_{\beta }^{n + 1} \) via maps \( {f}_{\beta } : {S}^{n} \rightarrow  {X}^{n} \) such that the composition of \( {f}_{\beta } \) with the projection onto the summand \( {S}_{\alpha }^{n} \) has degree \( {d}_{\beta \alpha } \) . Then the cellular boundary map \( {d}_{n + 1} \) will be the inclusion \( K \hookrightarrow  F \) , hence \( X \) will have the desired homology groups.

The construction of \( {f}_{\beta } \) generalizes the construction in Example 2.31 of a map \( {S}^{n} \rightarrow  {S}^{n} \) of given degree. Namely, we can let \( {f}_{\beta } \) map the complement of \( \mathop{\sum }\limits_{\alpha }\left| {d}_{\beta \alpha }\right| \) disjoint balls in \( {S}^{n} \) to the 0-cell of \( {X}^{n} \) while sending \( \left| {d}_{\beta \alpha }\right| \) of the balls onto the summand \( {S}_{\alpha }^{n} \) by maps of degree +1 if \( {d}_{\beta \alpha } > 0 \) , or degree -1 if \( {d}_{\beta \alpha } < 0 \) .

Example 2.41. By taking a wedge sum of the Moore spaces constructed in the preceding example for varying \( n \) we obtain a connected CW complex with any prescribed sequence of homology groups in dimensions \( 1,2,3,\cdots \) .

Example 2.42: Real Projective Space \( {\mathbb{{RP}}}^{n} \) . As we saw in Example 0.4, \( {\mathbb{{RP}}}^{n} \) has a CW structure with one cell \( {e}^{k} \) in each dimension \( k \leq  n \) , and the attaching map for \( {e}^{k} \) is the 2-sheeted covering projection \( \varphi  : {S}^{k - 1} \rightarrow  {\mathbb{{RP}}}^{k - 1} \) . To compute the boundary map \( {d}_{k} \) we compute the degree of the composition \( {S}^{k - 1}\overset{\varphi }{ \rightarrow  }{\mathbb{{RP}}}^{k - 1}\overset{q}{ \rightarrow  }{\mathbb{{RP}}}^{k - 1}/{\mathbb{{RP}}}^{k - 2} = {S}^{k - 1} \) , with \( q \) the quotient map. The map \( {q\varphi } \) restricts to a homeomorphism from each component of \( {S}^{k - 1} - {S}^{k - 2} \) onto \( {\mathbb{{RP}}}^{k - 1} - {\mathbb{{RP}}}^{k - 2} \) , and these two homeomorphisms are obtained from each other by precomposing with the antipodal map of \( {S}^{k - 1} \) , which has degree \( {\left( -1\right) }^{k} \) . Hence \( \deg {q\varphi } = \deg \mathbb{1} + \deg \left( {-\mathbb{1}}\right)  = 1 + {\left( -1\right) }^{k} \) , and so \( {d}_{k} \) is either 0 or multiplication by 2 according to whether \( k \) is odd or even. Thus the cellular chain complex for \( {\mathbb{{RP}}}^{n} \) is

\[
0 \rightarrow  \mathbb{Z}\overset{2}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\cdots \overset{2}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{2}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z} \rightarrow  0\;\text{ if }n\text{ is even }
\]

\[
0 \rightarrow  \mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{2}{ \rightarrow  }\cdots \overset{2}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{2}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z} \rightarrow  0\;\text{ if }n\text{ is odd }
\]

From this it follows that

\[
{H}_{k}\left( {\mathbb{{RP}}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }k = 0\text{ and for }k = \\  {\mathbb{Z}}_{2} & \text{ for }k\text{ odd, }0 < k < n \\  0 & \text{ otherwise } \end{array}\right.
\]

Example 2.43: Lens Spaces. This example is somewhat more complicated. Given an integer \( m > 1 \) and integers \( {\ell }_{1},\cdots ,{\ell }_{n} \) relatively prime to \( m \) , define the lens space \( L = \; {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) to be the orbit space \( {S}^{{2n} - 1}/{\mathbb{Z}}_{m} \) of the unit sphere \( {S}^{{2n} - 1} \subset  {\mathbb{C}}^{n} \) with the action of \( {\mathbb{Z}}_{m} \) generated by the rotation \( \rho \left( {{z}_{1},\cdots ,{z}_{n}}\right)  = \left( {{e}^{{2\pi i}{\ell }_{1}/m}{z}_{1},\cdots ,{e}^{{2\pi i}{\ell }_{n}/m}{z}_{n}}\right) \) , rotating the \( {j}^{\text{ th }}\mathbb{C} \) factor of \( {\mathbb{C}}^{n} \) by the angle \( {2\pi }{\ell }_{j}/m \) . In particular, when \( m = 2,\rho \) is the antipodal map, so \( L = {\mathbb{{RP}}}^{{2n} - 1} \) in this case. In the general case, the projection \( {S}^{{2n} - 1} \rightarrow  L \) is a covering space since the action of \( {\mathbb{Z}}_{m} \) on \( {S}^{{2n} - 1} \) is free: Only the identity element fixes any point of \( {S}^{{2n} - 1} \) since each point of \( {S}^{{2n} - 1} \) has some coordinate \( {z}_{j} \) nonzero and then \( {e}^{{2\pi ik}{\ell }_{j}/m}{z}_{j} \neq  {z}_{j} \) for \( 0 < k < m \) , as a result of the assumption that \( {\ell }_{j} \) is relatively prime to \( m \) .

We shall construct a CW structure on \( L \) with one cell \( {e}^{k} \) for each \( k \leq  {2n} - 1 \) and show that the resulting cellular chain complex is

\[
0 \rightarrow  \mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{m}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\cdots \overset{0}{ \rightarrow  }\mathbb{Z}\overset{m}{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z} \rightarrow  0
\]

with boundary maps alternately 0 and multiplication by \( m \) . Hence

\[
{H}_{k}\left( {{L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }k = 0,{2n} - 1 \\  {\mathbb{Z}}_{m} & \text{ for }k\text{ odd, }0 < k < {2n} - 1 \\  0 & \text{ otherwise } \end{array}\right.
\]

To obtain the CW structure, first subdivide the unit circle \( C \) in the \( {n}^{th}\mathbb{C} \) factor of \( {\mathbb{C}}^{n} \) by taking the points \( {e}^{{2\pi ij}/m} \in  C \) as vertices, \( j = 1,\cdots , m \) . Joining the \( {j}^{th} \) vertex of \( C \) to the unit sphere \( {S}^{{2n} - 3} \subset  {\mathbb{C}}^{n - 1} \) by arcs of great circles in \( {S}^{{2n} - 1} \) yields a \( \left( {{2n} - 2}\right) \) -dimensional ball \( {B}_{j}^{{2n} - 2} \) bounded by \( {S}^{{2n} - 3} \) . Specifically, \( {B}_{j}^{{2n} - 2} \) consists of the points \( \cos \theta \left( {0,\cdots ,0,{e}^{{2\pi ij}/m}}\right)  + \sin \theta \left( {{z}_{1},\cdots ,{z}_{n - 1},0}\right) \) for \( 0 \leq  \theta  \leq  \pi /2 \) . Similarly, joining the \( {j}^{th} \) edge of \( C \) to \( {S}^{{2n} - 3} \) gives a ball \( {B}_{j}^{{2n} - 1} \) bounded by \( {B}_{j}^{{2n} - 2} \) and \( {B}_{j + 1}^{{2n} - 2} \) , subscripts being taken mod \( m \) . The rotation \( \rho \) carries \( {S}^{{2n} - 3} \) to itself and rotates \( C \) by the angle \( {2\pi }{\ell }_{n}/m \) , hence \( \rho \) permutes the \( {B}_{j}^{{2n} - 2} \) ’s and the \( {B}_{j}^{{2n} - 1} \) ’s. A suitable power of \( \rho \) , namely \( {\rho }^{r} \) where \( r{\ell }_{n} \equiv  1{\;\operatorname{mod}\;m} \) , takes each \( {B}_{j}^{{2n} - 2} \) and \( {B}_{j}^{{2n} - 1} \) to the next one. Since \( {\rho }^{r} \) has order \( m \) , it is also a generator of the rotation group \( {\mathbb{Z}}_{m} \) , and hence we may obtain \( L \) as the quotient of one \( {B}_{j}^{{2n} - 1} \) by identifying its two faces \( {B}_{j}^{{2n} - 2} \) and \( {B}_{j + 1}^{{2n} - 2} \) together via \( {\rho }^{r} \) .

In particular, when \( n = 2,{B}_{j}^{{2n} - 1} \) is a lens-shaped 3-ball and \( L \) is obtained from this ball by identifying its two curved disk faces via \( {\rho }^{r} \) , which may be described as the composition of the reflection across the plane containing the rim of the lens, taking one face of the lens to the other, followed by a rotation of this face through the angle \( {2\pi }\ell /m \) where \( \ell  = r{\ell }_{1} \) . The figure illustrates the case \( \left( {m,\ell }\right)  = \left( {7,2}\right) \) , with the two dots indicating a typical pair of identified points in the upper and lower faces of the lens. Since the lens space \( L \) is determined by the rotation angle \( {2\pi }\ell /m \) , it is conveniently written \( {L}_{\ell /m} \) . Clearly only the mod \( m \) value of \( \ell \) matters. It is a classical theorem of Reidemeister from the 1930s that \( {L}_{\ell /m} \) is homeomorphic to \( {L}_{{\ell }^{\prime }/{m}^{\prime }} \) iff \( {m}^{\prime } = m \) and \( {\ell }^{\prime } \equiv   \pm  {\ell }^{\pm 1}{\;\operatorname{mod}\;m} \) . For example, when \( m = 7 \) there are only two distinct lens spaces \( {L}_{1/7} \) and \( {L}_{2/7} \) . The ’if’ part of this theorem is easy: Reflecting the lens through a mirror shows that \( {L}_{\ell /m} \approx  {L}_{-\ell /m} \) , and by interchanging the roles of the two \( \mathbb{C} \) factors of \( {\mathbb{C}}^{2} \) one obtains \( {L}_{\ell /m} \approx  {L}_{{\ell }^{-1}/m} \) . In the converse direction, \( {L}_{\ell /m} \approx  {L}_{{\ell }^{\prime }/{m}^{\prime }} \) clearly implies \( m = {m}^{\prime } \) since \( {\pi }_{1}\left( {L}_{\ell /m}\right)  \approx  {\mathbb{Z}}_{m} \) . The rest of the theorem takes considerably more work, involving either special 3-dimensional techniques or more algebraic methods that generalize to classify the higher-dimensional lens spaces as well. The latter approach is explained in [Cohen 1973].

![bo_d7dtv0s91nqc73eq8nv0_153_1133_786_456_361_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_153_1133_786_456_361_0.jpg)

Returning to the construction of a CW structure on \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) , observe that the \( \left( {{2n} - 3}\right) \) -dimensional lens space \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n - 1}}\right) \) sits in \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) as the quotient of \( {S}^{{2n} - 3} \) , and \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) is obtained from this subspace by attaching two cells, of dimensions \( {2n} - 2 \) and \( {2n} - 1 \) , coming from the interiors of \( {B}_{j}^{{2n} - 1} \) and its two identified faces \( {B}_{j}^{{2n} - 2} \) and \( {B}_{j + 1}^{{2n} - 2} \) . Inductively this gives a CW structure on \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) with one cell \( {e}^{k} \) in each dimension \( k \leq  {2n} - 1 \) .

The boundary maps in the associated cellular chain complex are computed as follows. The first one, \( {d}_{{2n} - 1} \) , is zero since the identification of the two faces of \( {B}_{j}^{{2n} - 1} \) is via a reflection (degree -1) across \( {B}_{j}^{{2n} - 1} \) fixing \( {S}^{{2n} - 3} \) , followed by a rotation (degree +1), so \( {d}_{{2n} - 1}\left( {e}^{{2n} - 1}\right)  = {e}^{{2n} - 2} - {e}^{{2n} - 2} = 0 \) . The next boundary map \( {d}_{{2n} - 2} \) takes \( {e}^{{2n} - 2} \) to \( m{e}^{{2n} - 3} \) since the attaching map for \( {e}^{{2n} - 2} \) is the quotient map \( {S}^{{2n} - 3} \rightarrow  {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n - 1}}\right) \) and the balls \( {B}_{j}^{{2n} - 3} \) in \( {S}^{{2n} - 3} \) which project down onto \( {e}^{{2n} - 3} \) are permuted cyclically by the rotation \( \rho \) of degree +1 . Inductively, the subsequent boundary maps \( {d}_{k} \) then alternate between 0 and multiplication by \( m \) .

Also of interest are the infinite-dimensional lens spaces \( {L}_{m}\left( {{\ell }_{1},{\ell }_{2},\cdots }\right)  = {S}^{\infty }/{\mathbb{Z}}_{m} \) defined in the same way as in the finite-dimensional case, starting from a sequence of integers \( {\ell }_{1},{\ell }_{2},\cdots \) relatively prime to \( m \) . The space \( {L}_{m}\left( {{\ell }_{1},{\ell }_{2},\cdots }\right) \) is the union of the increasing sequence of finite-dimensional lens spaces \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) for \( n = 1,2,\cdots \) , each of which is a subcomplex of the next in the cell structure we have just constructed, so \( {L}_{m}\left( {{\ell }_{1},{\ell }_{2},\cdots }\right) \) is also a CW complex. Its cellular chain complex consists of a \( \mathbb{Z} \) in each dimension with boundary maps alternately 0 and \( m \) , so its reduced homology consists of a \( {\mathbb{Z}}_{m} \) in each odd dimension.

In the terminology of §1.B, the infinite-dimensional lens space \( {L}_{m}\left( {{\ell }_{1},{\ell }_{2},\cdots }\right) \) is an Eilenberg-MacLane space \( K\left( {{\mathbb{Z}}_{m},1}\right) \) since its universal cover \( {S}^{\infty } \) is contractible, as we showed there. By Theorem 1B.8 the homotopy type of \( {L}_{m}\left( {{\ell }_{1},{\ell }_{2},\cdots }\right) \) depends only on \( m \) , and not on the \( {\ell }_{i} \) ’s. This is not true in the finite-dimensional case, when two lens spaces \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) and \( {L}_{m}\left( {{\ell }_{1}^{\prime },\cdots ,{\ell }_{n}^{\prime }}\right) \) have the same homotopy type iff \( {\ell }_{1}\cdots {\ell }_{n} \equiv   \pm  {k}^{n}{\ell }_{1}^{\prime }\cdots {\ell }_{n}^{\prime }{\;\operatorname{mod}\;m} \) for some integer \( k \) . A proof of this is outlined in Exercise 2 in §3.E and Exercise 29 in §4.2. For example, the 3-dimensional lens spaces \( {L}_{1/5} \) and \( {L}_{2/5} \) are not homotopy equivalent, though they have the same fundamental group and the same homology groups. On the other hand, \( {L}_{1/7} \) and \( {L}_{2/7} \) are homotopy equivalent but not homeomorphic.

## Euler Characteristic

For a finite CW complex \( X \) , the Euler characteristic \( \chi \left( X\right) \) is defined to be the alternating sum \( \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}{c}_{n} \) where \( {c}_{n} \) is the number of \( n \) -cells of \( X \) , generalizing the familiar formula vertices - edges + faces for 2-dimensional complexes. The following result shows that \( \chi \left( X\right) \) can be defined purely in terms of homology, and hence depends only on the homotopy type of \( X \) . In particular, \( \chi \left( X\right) \) is independent of the choice of CW structure on \( X \) .

Theorem 2.44. \( \chi \left( X\right)  = \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\operatorname{rank}{H}_{n}\left( X\right) \) .

Here the rank of a finitely generated abelian group is the number of \( \mathbb{Z} \) summands when the group is expressed as a direct sum of cyclic groups. We shall need the following fact, whose proof we leave as an exercise: If \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) is a short exact sequence of finitely generated abelian groups, then \( \operatorname{rank}B = \operatorname{rank}A + \operatorname{rank}C \) .

Proof of 2.44: This is purely algebraic. Let

\[
0 \rightarrow  {C}_{k}\overset{{d}_{k}}{ \rightarrow  }{C}_{k - 1} \rightarrow  \cdots  \rightarrow  {C}_{1}\overset{{d}_{1}}{ \rightarrow  }{C}_{0} \rightarrow  0
\]

be a chain complex of finitely generated abelian groups, with cycles \( {Z}_{n} = \operatorname{Ker}{d}_{n} \) , boundaries \( {B}_{n} = \operatorname{Im}{d}_{n + 1} \) , and homology \( {H}_{n} = {Z}_{n}/{B}_{n} \) . Thus we have short exact sequences \( 0 \rightarrow  {Z}_{n} \rightarrow  {C}_{n} \rightarrow  {B}_{n - 1} \rightarrow  0 \) and \( 0 \rightarrow  {B}_{n} \rightarrow  {Z}_{n} \rightarrow  {H}_{n} \rightarrow  0 \) , hence

\[
\operatorname{rank}{C}_{n} = \operatorname{rank}{Z}_{n} + \operatorname{rank}{B}_{n - 1}
\]

\[
\operatorname{rank}{Z}_{n} = \operatorname{rank}{B}_{n} + \operatorname{rank}{H}_{n}
\]

Now substitute the second equation into the first, multiply the resulting equation by \( {\left( -1\right) }^{n} \) , and sum over \( n \) to get \( \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\operatorname{rank}{C}_{n} = \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\operatorname{rank}{H}_{n} \) . Applying this with \( {C}_{n} = {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) then gives the theorem.

For example, the surfaces \( {M}_{g} \) and \( {N}_{g} \) have Euler characteristics \( \chi \left( {M}_{g}\right)  = 2 - {2g} \) and \( \chi \left( {N}_{g}\right)  = 2 - g \) . Thus all the orientable surfaces \( {M}_{g} \) are distinguished from each other by their Euler characteristics, as are the nonorientable surfaces \( {N}_{g} \) , and there are only the relations \( \chi \left( {M}_{g}\right)  = \chi \left( {N}_{2g}\right) \) .

## Split Exact Sequences

Suppose one has a retraction \( r : X \rightarrow  A \) , so \( {ri} = \mathbb{1} \) where \( i : A \rightarrow  X \) is the inclusion. The induced map \( {i}_{ * } : {H}_{n}\left( A\right)  \rightarrow  {H}_{n}\left( X\right) \) is then injective since \( {r}_{ * }{i}_{ * } = \mathbb{1} \) . From this it follows that the boundary maps in the long exact sequence for \( \left( {X, A}\right) \) are zero, so the long exact sequence breaks up into short exact sequences

\[
0 \rightarrow  {H}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( X\right) \overset{{j}_{ * }}{ \rightarrow  }{H}_{n}\left( {X, A}\right)  \rightarrow  0
\]

The relation \( {r}_{ * }{i}_{ * } = \mathbb{1} \) actually gives more information than this, by the following piece of elementary algebra:

Splitting Lemma. For a short exact sequence \( 0 \rightarrow  A\overset{i}{ \rightarrow  }B\overset{j}{ \rightarrow  }C \rightarrow  0 \) of abelian groups the following statements are equivalent:

(a) There is a homomorphism \( p : B \rightarrow  A \) such that \( {pi} = \mathbb{1} : A \rightarrow  A \) .

(b) There is a homomorphism \( s : C \rightarrow  B \) such that \( {js} = \mathbb{1} : C \rightarrow  C \) .

(c) There is an isomorphism \( B \approx  A \oplus  C \) making a commutative diagram as at the right, where the maps in the lower row are the obvious ones, \( a \mapsto  \left( {a,0}\right) \) and \( \left( {a, c}\right)  \mapsto  c \) .

![bo_d7dtv0s91nqc73eq8nv0_155_1079_1663_513_157_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_155_1079_1663_513_157_0.jpg)

If these conditions are satisfied, the exact sequence is said to split. Note that (c) is symmetric: There is no essential difference between the roles of \( A \) and \( C \) .

Sketch of Proof: For the implication (a) \( \Rightarrow \) (c) one checks that the map \( B \rightarrow  A \oplus  C \) , \( b \mapsto  \left( {p\left( b\right) , j\left( b\right) }\right) \) , is an isomorphism with the desired properties. For (b) \( \Rightarrow \) (c) one uses instead the map \( A \oplus  C \rightarrow  B,\left( {a, c}\right)  \mapsto  i\left( a\right)  + s\left( c\right) \) . The opposite implications (c) \( \Rightarrow \) (a) and (c) \( \Rightarrow \) (b) are fairly obvious. If one wants to show (b) \( \Rightarrow \) (a) directly, one can define \( p\left( b\right)  = {i}^{-1}\left( {b - {sj}\left( b\right) }\right) \) . Further details are left to the reader.

Except for the implications (b) \( \Rightarrow \) (a) and (b) \( \Rightarrow \) (c), the proof works equally well for nonabelian groups. In the nonabelian case, (b) is definitely weaker than (a) and (c), and short exact sequences satisfying (b) only determine \( B \) as a semidirect product of \( A \) and \( C \) . The difficulty is that \( s\left( C\right) \) might not be a normal subgroup of \( B \) . In the nonabelian case one defines 'splitting' to mean that (b) is satisfied.

In both the abelian and nonabelian contexts, if \( C \) is free then every exact sequence \( 0 \rightarrow  A\overset{i}{ \rightarrow  }B\overset{j}{ \rightarrow  }C \rightarrow  0 \) splits, since one can define \( s : C \rightarrow  B \) by choosing a basis \( \left\{  {c}_{\alpha }\right\} \) for \( C \) and letting \( s\left( {c}_{\alpha }\right) \) be any element \( {b}_{\alpha } \in  B \) such that \( j\left( {b}_{\alpha }\right)  = {c}_{\alpha } \) . The converse is also true: If every short exact sequence ending in \( C \) splits, then \( C \) is free. This is because for every \( C \) there is a short exact sequence \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) with \( B \) free - choose generators for \( C \) and let \( B \) have a basis in one-to-one correspondence with these generators, then let \( B \rightarrow  C \) send each basis element to the corresponding generator - so if this sequence \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) splits, \( C \) is isomorphic to a subgroup of a free group, hence is free.

From the Splitting Lemma and the remarks preceding it we deduce that a retraction \( r : X \rightarrow  A \) gives a splitting \( {H}_{n}\left( X\right)  \approx  {H}_{n}\left( A\right)  \oplus  {H}_{n}\left( {X, A}\right) \) . This can be used to show the nonexistence of such a retraction in some cases, for example in the situation of the Brouwer fixed point theorem, where a retraction \( {D}^{n} \rightarrow  {S}^{n - 1} \) would give an impossible splitting \( {H}_{n - 1}\left( {D}^{n}\right)  \approx  {H}_{n - 1}\left( {S}^{n - 1}\right)  \oplus  {H}_{n - 1}\left( {{D}^{n},{S}^{n - 1}}\right) \) . For a somewhat more subtle example, consider the mapping cylinder \( {M}_{f} \) of a degree \( m \) map \( f : {S}^{n} \rightarrow  {S}^{n} \) with \( m > 1 \) . If \( {M}_{f} \) retracted onto the \( {S}^{n} \subset  {M}_{f} \) corresponding to the domain of \( f \) , we would have a split short exact sequence

\[
0 \rightarrow  {H}_{n}\left( {S}^{n}\right)  \rightarrow  {H}_{n}\left( {M}_{f}\right)  \rightarrow  {H}_{n}\left( {{M}_{f},{S}^{n}}\right)  \rightarrow  0
\]

\[
0 \rightarrow  \mathbb{Z}\xrightarrow[]{\parallel \;}\mathbb{Z}\xrightarrow[]{\parallel \;}\mathbb{Z}\xrightarrow[]{\parallel \;}{\mathbb{Z}}_{m}\xrightarrow[]{\parallel \;}
\]

But this sequence does not split since \( \mathbb{Z} \) is not isomorphic to \( \mathbb{Z} \oplus  {\mathbb{Z}}_{m} \) if \( m > 1 \) , so the retraction cannot exist. In the simplest case of the degree 2 map \( {S}^{1} \rightarrow  {S}^{1}, z \mapsto  {z}^{2} \) , this says that the Möbius band does not retract onto its boundary circle.

## Homology of Groups

In §1.B we constructed for each group \( G \) a CW complex \( K\left( {G,1}\right) \) having a contractible universal cover, and we showed that the homotopy type of such a space \( K\left( {G,1}\right) \) is uniquely determined by \( G \) . The homology groups \( {H}_{n}\left( {K\left( {G,1}\right) }\right) \) therefore depend only on \( G \) , and are usually denoted simply \( {H}_{n}\left( G\right) \) . The calculations for lens spaces in Example 2.43 show that \( {H}_{n}\left( {\mathbb{Z}}_{m}\right) \) is \( {\mathbb{Z}}_{m} \) for odd \( n \) and 0 for even \( n > 0 \) . Since \( {S}^{1} \) is a \( K\left( {\mathbb{Z},1}\right) \) and the torus is a \( K\left( {\mathbb{Z} \times  \mathbb{Z},1}\right) \) , we also know the homology of these two groups. More generally, the homology of finitely generated abelian groups can be computed from these examples using the Künneth formula in §3.B and the fact that a product \( K\left( {G,1}\right)  \times  K\left( {H,1}\right) \) is a \( K\left( {G \times  H,1}\right) \) .

Here is an application of the calculation of \( {H}_{n}\left( {\mathbb{Z}}_{m}\right) \) :

Proposition 2.45. If a finite-dimensional CW complex \( X \) is a \( K\left( {G,1}\right) \) , then the group \( G = {\pi }_{1}\left( X\right) \) must be torsionfree.

This applies to quite a few manifolds, for example closed surfaces other than \( {S}^{2} \) and \( {\mathbb{{RP}}}^{2} \) , and also many 3-dimensional manifolds such as complements of knots in \( {S}^{3} \) .

Proof: If \( G \) had torsion, it would have a finite cyclic subgroup \( {\mathbb{Z}}_{m} \) for some \( m > 1 \) , and the covering space of \( X \) corresponding to this subgroup of \( G = {\pi }_{1}\left( X\right) \) would be a \( K\left( {{\mathbb{Z}}_{m},1}\right) \) . Since \( X \) is a finite-dimensional CW complex, the same would be true of its covering space \( K\left( {{\mathbb{Z}}_{m},1}\right) \) , and hence the homology of the \( K\left( {{\mathbb{Z}}_{m},1}\right) \) would be nonzero in only finitely many dimensions. But this contradicts the fact that \( {H}_{n}\left( {\mathbb{Z}}_{m}\right) \) is nonzero for infinitely many values of \( n \) .

Reflecting the richness of group theory, the homology of groups has been studied quite extensively. A good starting place for those wishing to learn more is the textbook [Brown 1982]. At a more advanced level the books [Adem & Milgram 1994] and [Benson 1992] treat the subject from a mostly topological viewpoint.

## Mayer-Vietoris Sequences

In addition to the long exact sequence of homology groups for a pair \( \left( {X, A}\right) \) , there is another sort of long exact sequence, known as a Mayer-Vietoris sequence, which is equally powerful but is sometimes more convenient to use. For a pair of subspaces \( A, B \subset  X \) such that \( X \) is the union of the interiors of \( A \) and \( B \) , this exact sequence has the form

\[
\cdots  \rightarrow  {H}_{n}\left( {A \cap  B}\right) \overset{\Phi }{ \rightarrow  }{H}_{n}\left( A\right)  \oplus  {H}_{n}\left( B\right) \overset{\Psi }{ \rightarrow  }{H}_{n}\left( X\right) \overset{\partial }{ \rightarrow  }{H}_{n - 1}\left( {A \cap  B}\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {H}_{0}\left( X\right)  \rightarrow  0
\]

In addition to its usefulness for calculations, the Mayer-Vietoris sequence is also applied frequently in induction arguments, where one might know that a certain statement is true for \( A, B \) , and \( A \cap  B \) by induction and then deduce that it is true for \( A \cup  B \) by the exact sequence.

The Mayer-Vietoris sequence is easy to derive from the machinery of §2.1. Let \( {C}_{n}\left( {A + B}\right) \) be the subgroup of \( {C}_{n}\left( X\right) \) consisting of chains that are sums of chains in \( A \) and chains in \( B \) . The usual boundary map \( \partial  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n - 1}\left( X\right) \) takes \( {C}_{n}\left( {A + B}\right) \) to \( {C}_{n - 1}\left( {A + B}\right) \) , so the \( {C}_{n}\left( {A + B}\right) \) ’s form a chain complex. According to Proposition 2.21, the inclusions \( {C}_{n}\left( {A + B}\right)  \hookrightarrow  {C}_{n}\left( X\right) \) induce isomorphisms on homology groups. The Mayer-Vietoris sequence is then the long exact sequence of homology groups associated to the short exact sequence of chain complexes formed by the short exact sequences

\[
0 \rightarrow  {C}_{n}\left( {A \cap  B}\right) \overset{\varphi }{ \rightarrow  }{C}_{n}\left( A\right)  \oplus  {C}_{n}\left( B\right) \overset{\psi }{ \rightarrow  }{C}_{n}\left( {A + B}\right)  \rightarrow  0
\]

where \( \varphi \left( x\right)  = \left( {x, - x}\right) \) and \( \psi \left( {x, y}\right)  = x + y \) . The exactness of this short exact sequence can be checked as follows. First, Ker \( \varphi  = 0 \) since a chain in \( A \cap  B \) that is zero as a chain in \( A \) (or in \( B \) ) must be the zero chain. Next, \( \operatorname{Im}\varphi  \subset  \operatorname{Ker}\psi \) since \( {\psi \varphi } = 0 \) . Also, \( \operatorname{Ker}\psi  \subset  \operatorname{Im}\varphi \) since for a pair \( \left( {x, y}\right)  \in  {C}_{n}\left( A\right)  \oplus  {C}_{n}\left( B\right) \) the condition \( x + y = 0 \) implies \( x =  - y \) , so \( x \) is a chain in both \( A \) and \( B \) , that is, \( x \in  {C}_{n}\left( {A \cap  B}\right) \) , and \( \left( {x, y}\right)  = \left( {x, - x}\right)  \in  \operatorname{Im}\varphi \) . Finally, exactness at \( {C}_{n}\left( {A + B}\right) \) is immediate from the definition of \( {C}_{n}\left( {A + B}\right) \) .

The boundary map \( \partial  : {H}_{n}\left( X\right)  \rightarrow  {H}_{n - 1}\left( {A \cap  B}\right) \) can easily be made explicit. A class \( \alpha  \in  {H}_{n}\left( X\right) \) is represented by a cycle \( z \) , and by barycentric subdivision or some other method we can choose \( z \) to be a sum \( x + y \) of chains in \( A \) and \( B \) , respectively. It need not be true that \( x \) and \( y \) are cycles individually, but \( \partial x =  - \partial y \) since \( \partial \left( {x + y}\right)  = 0 \) , and the element \( \partial \alpha  \in  {H}_{n - 1}\left( {A \cap  B}\right) \) is represented by the cycle \( \partial x =  - \partial y \) , as is clear from the definition of the boundary map in the long exact sequence of homology groups associated to a short exact sequence of chain complexes.

There is also a formally identical Mayer-Vietoris sequence for reduced homology groups, obtained by augmenting the previous short exact sequence of chain complexes in the obvious way:

![bo_d7dtv0s91nqc73eq8nv0_158_374_1044_1050_171_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_158_374_1044_1050_171_0.jpg)

Mayer-Vietoris sequences can be viewed as analogs of the van Kampen theorem since if \( A \cap  B \) is path-connected, the \( {H}_{1} \) terms of the reduced Mayer-Vietoris sequence yield an isomorphism \( {H}_{1}\left( X\right)  \approx  \left( {{H}_{1}\left( A\right)  \oplus  {H}_{1}\left( B\right) }\right) /\operatorname{Im}\Phi \) . This is exactly the abelianized statement of the van Kampen theorem, and \( {H}_{1} \) is the abelianization of \( {\pi }_{1} \) for path-connected spaces, as we show in §2.A.

There are also Mayer-Vietoris sequences for decompositions \( X = A \cup  B \) such that \( A \) and \( B \) are deformation retracts of neighborhoods \( U \) and \( V \) with \( U \cap  V \) deformation retracting onto \( A \cap  B \) . Under these assumptions the five-lemma implies that the maps \( {C}_{n}\left( {A + B}\right)  \rightarrow  {C}_{n}\left( {U + V}\right) \) induce isomorphisms on homology, and hence so do the maps \( {C}_{n}\left( {A + B}\right)  \rightarrow  {C}_{n}\left( X\right) \) , which was all that we needed to obtain a Mayer-Vietoris sequence. For example, if \( X \) is a CW complex and \( A \) and \( B \) are subcomplexes, then we can choose for \( U \) and \( V \) neighborhoods of the form \( {N}_{\varepsilon }\left( A\right) \) and \( {N}_{\varepsilon }\left( B\right) \) constructed in the Appendix, which have the property that \( {N}_{\varepsilon }\left( A\right)  \cap  {N}_{\varepsilon }\left( B\right)  = {N}_{\varepsilon }\left( {A \cap  B}\right) \) .

Example 2.46. Take \( X = {S}^{n} \) with \( A \) and \( B \) the northern and southern hemispheres, so that \( A \cap  B = {S}^{n - 1} \) . Then in the reduced Mayer-Vietoris sequence the terms \( {\widetilde{H}}_{i}\left( A\right)  \oplus  {\widetilde{H}}_{i}\left( B\right) \) are zero, so we obtain isomorphisms \( {\widetilde{H}}_{i}\left( {S}^{n}\right)  \approx  {\widetilde{H}}_{i - 1}\left( {S}^{n - 1}\right) \) . This gives another way of calculating the homology groups of \( {S}^{n} \) by induction.

Example 2.47. We can decompose the Klein bottle \( K \) as the union of two Möbius bands \( A \) and \( B \) glued together by a homeomorphism between their boundary circles.

Then \( A, B \) , and \( A \cap  B \) are homotopy equivalent to circles, so the interesting part of the reduced Mayer-Vietoris sequence for the decomposition \( K = A \cup  B \) is the segment

\[
0 \rightarrow  {H}_{2}\left( K\right)  \rightarrow  {H}_{1}\left( {A \cap  B}\right) \overset{\Phi }{ \rightarrow  }{H}_{1}\left( A\right)  \oplus  {H}_{1}\left( B\right)  \rightarrow  {H}_{1}\left( K\right)  \rightarrow  0
\]

The map \( \Phi \) is \( \mathbb{Z} \rightarrow  \mathbb{Z} \oplus  \mathbb{Z},1 \mapsto  \left( {2, - 2}\right) \) , since the boundary circle of a Möbius band wraps twice around the core circle. Since \( \Phi \) is injective we obtain \( {H}_{2}\left( K\right)  = 0 \) . Furthermore, we have \( {H}_{1}\left( K\right)  \approx  \mathbb{Z} \oplus  {\mathbb{Z}}_{2} \) since we can choose \( \left( {1,0}\right) \) and \( \left( {1, - 1}\right) \) as a basis for \( \mathbb{Z} \oplus  \mathbb{Z} \) . All the higher homology groups of \( K \) are zero from the earlier part of the Mayer-Vietoris sequence.

Example 2.48. Let us describe an exact sequence which is somewhat similar to the Mayer-Vietoris sequence and which in some cases generalizes it. If we are given two maps \( f, g : X \rightarrow  Y \) then we can form a quotient space \( Z \) of the disjoint union of \( X \times  I \) and \( Y \) via the identifications \( \left( {x,0}\right)  \sim  f\left( x\right) \) and \( \left( {x,1}\right)  \sim  g\left( x\right) \) , thus attaching one end of \( X \times  I \) to \( Y \) by \( f \) and the other end by \( g \) . For example, if \( f \) and \( g \) are each the identity map \( X \rightarrow  X \) then \( Z = X \times  {S}^{1} \) . If only one of \( f \) and \( g \) , say \( f \) , is the identity map, then \( Z \) is homeomorphic to what is called the mapping torus of \( g \) , the quotient space of \( X \times  I \) under the identifications \( \left( {x,0}\right)  \sim  \left( {g\left( x\right) ,1}\right) \) . The Klein bottle is an example, with \( g \) a reflection \( {S}^{1} \rightarrow  {S}^{1} \) .

The exact sequence we want has the form

(*)

\[
\text{ ) }\cdots  \rightarrow  {H}_{n}\left( X\right) \xrightarrow[]{{f}_{ * } - {g}_{ * }}{H}_{n}\left( Y\right) \xrightarrow[]{{i}_{ * }}{H}_{n}\left( Z\right)  \rightarrow  {H}_{n - 1}\left( X\right) \xrightarrow[]{{f}_{ * } - {g}_{ * }}{H}_{n - 1}\left( Y\right)  \rightarrow  \cdots
\]

where \( i \) is the evident inclusion \( Y \hookrightarrow  Z \) . To derive this exact sequence, consider the map \( q : \left( {X \times  I, X \times  \partial I}\right)  \rightarrow  \left( {Z, Y}\right) \) that is the restriction to \( X \times  I \) of the quotient map \( X \times  I \coprod  Y \rightarrow  Z \) . The map \( q \) induces a map of long exact sequences:

\[
\begin{array}{l} \cdots  \rightarrow  {H}_{n + 1}\left( {Z, Y}\right) \overset{\partial }{ \rightarrow  }{H}_{n}\left( Y\right) \overset{\partial }{ \rightarrow  }{H}_{n}\left( {X \times  \partial I}\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( {X \times  I}\right) \overset{\partial }{ \rightarrow  }\cdots \\  \end{array}
\]

In the upper row the middle term is the direct sum of two copies of \( {H}_{n}\left( X\right) \) , and the map \( {i}_{ * } \) is surjective since \( X \times  I \) deformation retracts onto \( X \times  \{ 0\} \) and \( X \times  \{ 1\} \) . Sur-jectivity of the maps \( {i}_{ * } \) in the upper row implies that the next maps are 0, which in turn implies that the maps \( \partial \) are injective. Thus the map \( \partial \) in the upper row gives an isomorphism of \( {H}_{n + 1}\left( {X \times  I, X \times  \partial I}\right) \) onto the kernel of \( {i}_{ * } \) , which consists of the pairs \( \left( {\alpha , - \alpha }\right) \) for \( \alpha  \in  {H}_{n}\left( X\right) \) . This kernel is a copy of \( {H}_{n}\left( X\right) \) , and the middle vertical map \( {q}_{ * } \) takes \( \left( {\alpha , - \alpha }\right) \) to \( {f}_{ * }\left( \alpha \right)  - {g}_{ * }\left( \alpha \right) \) . The left-hand \( {q}_{ * } \) is an isomorphism since these are good pairs and \( q \) induces a homeomorphism of quotient spaces \( \left( {X \times  I}\right) /\left( {X \times  \partial I}\right)  \rightarrow  Z/Y \) . Hence if we replace \( {H}_{n + 1}\left( {Z, Y}\right) \) in the lower exact sequence by the isomorphic group \( {H}_{n}\left( X\right)  \approx  \operatorname{Ker}{i}_{ * } \) we obtain the long exact sequence we want.

In the case of the mapping torus of a reflection \( g : {S}^{1} \rightarrow  {S}^{1} \) , with \( Z \) a Klein bottle, the interesting portion of the exact sequence \( \left( *\right) \) is

\[
0 \rightarrow  {H}_{2}\left( Z\right)  \rightarrow  {H}_{1}\left( {S}^{1}\right) \xrightarrow[]{\mathbb{1} - {g}_{ * }}{H}_{1}\left( {S}^{1}\right)  \rightarrow  {H}_{1}\left( Z\right)  \rightarrow  {H}_{0}\left( {S}^{1}\right) \xrightarrow[]{\mathbb{1} - {g}_{ * }}{H}_{0}\left( {S}^{1}\right)
\]

\[
\text{ \_\_\_ }
\]

Thus \( {H}_{2}\left( Z\right)  = 0 \) and we have a short exact sequence \( 0 \rightarrow  {\mathbb{Z}}_{2} \rightarrow  {H}_{1}\left( Z\right)  \rightarrow  \mathbb{Z} \rightarrow  0 \) . This splits since \( \mathbb{Z} \) is free, so \( {H}_{1}\left( Z\right)  \approx  {\mathbb{Z}}_{2} \oplus  \mathbb{Z} \) . Other examples are given in the Exercises.

If \( Y \) is the disjoint union of spaces \( {Y}_{1} \) and \( {Y}_{2} \) , with \( f : X \rightarrow  {Y}_{1} \) and \( g : X \rightarrow  {Y}_{2} \) , then \( Z \) consists of the mapping cylinders of these two maps with their domain ends identified. For example, suppose we have a CW complex decomposed as the union of two subcomplexes \( A \) and \( B \) and we take \( f \) and \( g \) to be the inclusions \( A \cap  B \hookrightarrow  A \) and \( A \cap  B \hookrightarrow  B \) . Then the double mapping cylinder \( Z \) is homotopy equivalent to \( A \cup  B \) since we can view \( Z \) as \( \left( {A \cap  B}\right)  \times  I \) with \( A \) and \( B \) attached at the two ends, and then slide the attaching of \( A \) down to the \( B \) end to produce \( A \cup  B \) with \( \left( {A \cap  B}\right)  \times  I \) attached at one of its ends. By Proposition 0.18 the sliding operation preserves homotopy type, so we obtain a homotopy equivalence \( Z \simeq  A \cup  B \) . The exact sequence (*) in this case is the Mayer-Vietoris sequence.

A relative form of the Mayer-Vietoris sequence is sometimes useful. If one has a pair of spaces \( \left( {X, Y}\right)  = \left( {A \cup  B, C \cup  D}\right) \) with \( C \subset  A \) and \( D \subset  B \) , such that \( X \) is the union of the interiors of \( A \) and \( B \) , and \( Y \) is the union of the interiors of \( C \) and \( D \) , then there is a relative Mayer-Vietoris sequence

\[
\cdots  \rightarrow  {H}_{n}\left( {A \cap  B, C \cap  D}\right) \overset{\Phi }{ \rightarrow  }{H}_{n}\left( {A, C}\right)  \oplus  {H}_{n}\left( {B, D}\right) \overset{\Psi }{ \rightarrow  }{H}_{n}\left( {X, Y}\right) \overset{\partial }{ \rightarrow  }\cdots
\]

To derive this, consider the commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_160_249_1322_1310_421_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_160_249_1322_1310_421_0.jpg)

where \( {C}_{n}\left( {A + B, C + D}\right) \) is the quotient of the subgroup \( {C}_{n}\left( {A + B}\right)  \subset  {C}_{n}\left( X\right) \) by its subgroup \( {C}_{n}\left( {C + D}\right)  \subset  {C}_{n}\left( Y\right) \) . Thus the three columns of the diagram are exact. We have seen that the first two rows are exact, and we claim that the third row is exact also, with the maps \( \varphi \) and \( \psi \) induced from the \( \varphi \) and \( \psi \) in the second row. Since \( {\psi \varphi } = 0 \) in the second row, this holds also in the third row, so the third row is at least a chain complex. Viewing the three rows as chain complexes, the diagram then represents a short exact sequence of chain complexes. The associated long exact sequence of homology groups has two out of every three terms zero since the first two rows of the diagram are exact. Hence the remaining homology groups are zero and the third row is exact.

The third column maps to \( 0 \rightarrow  {C}_{n}\left( Y\right)  \rightarrow  {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( {X, Y}\right)  \rightarrow  0 \) , inducing maps of homology groups that are isomorphisms for the \( X \) and \( Y \) terms as we have seen above. So by the five-lemma the maps \( {C}_{n}\left( {A + B, C + D}\right)  \rightarrow  {C}_{n}\left( {X, Y}\right) \) also induce isomorphisms on homology. The relative Mayer-Vietoris sequence is then the long exact sequence of homology groups associated to the short exact sequence of chain complexes given by the third row of the diagram.

## Homology with Coefficients

There is an easy generalization of the homology theory we have considered so far that behaves in a very similar fashion and sometimes offers technical advantages. The generalization consists of using chains of the form \( \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} \) where each \( {\sigma }_{i} \) is a singular \( n \) -simplex in \( X \) as before, but now the coefficients \( {n}_{i} \) are taken to lie in a fixed abelian group \( G \) rather than \( \mathbb{Z} \) . Such \( n \) -chains form an abelian group \( {C}_{n}\left( {X;G}\right) \) , and there is the expected relative version \( {C}_{n}\left( {X, A;G}\right)  = {C}_{n}\left( {X;G}\right) /{C}_{n}\left( {A;G}\right) \) . The old formula for the boundary maps \( \partial \) can still be used for arbitrary \( G \) , namely \( \partial \left( {\mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i}}\right)  = \mathop{\sum }\limits_{{i, j}}{\left( -1\right) }^{j}{n}_{i}{\sigma }_{i} \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{n}}\right\rbrack \) . Just as before, a calculation shows that \( {\partial }^{2} = 0 \) , so the groups \( {C}_{n}\left( {X;G}\right) \) and \( {C}_{n}\left( {X, A;G}\right) \) form chain complexes. The resulting homology groups \( {H}_{n}\left( {X;G}\right) \) and \( {H}_{n}\left( {X, A;G}\right) \) are called homology groups with coefficients in G. Reduced groups \( {\widetilde{H}}_{n}\left( {X;G}\right) \) are defined via the augmented chain complex \( \cdots  \rightarrow  {C}_{0}\left( {X;G}\right) \overset{\varepsilon }{ \rightarrow  }G \rightarrow  0 \) with \( \varepsilon \) again defined by summing coefficients.

The case \( G = {\mathbb{Z}}_{2} \) is particularly simple since one is just considering sums of singular simplices with coefficients 0 or 1 , so by discarding terms with coefficient 0 one can think of chains as just finite 'unions' of singular simplices. The boundary formulas also simplify since one no longer has to worry about signs. Since signs are an algebraic representation of orientation considerations, one can also ignore orientations. This means that homology with \( {\mathbb{Z}}_{2} \) coefficients is often the most natural tool in the absence of orientability.

All the theory we developed in \( \text{ § }{2.1} \) for \( \mathbb{Z} \) coefficients carries over directly to general coefficient groups \( G \) with no change in the proofs. The same is true for Mayer-Vietoris sequences. Differences between \( {H}_{n}\left( {X;G}\right) \) and \( {H}_{n}\left( X\right) \) begin to appear only when one starts making calculations. When \( X \) is a point, the method used to compute \( {H}_{n}\left( X\right) \) shows that \( {H}_{n}\left( {X;G}\right) \) is \( G \) for \( n = 0 \) and 0 for \( n > 0 \) . From this it follows just as for \( G = \mathbb{Z} \) that \( {\widetilde{H}}_{n}\left( {{S}^{k};G}\right) \) is \( G \) for \( n = k \) and 0 otherwise.

Cellular homology also generalizes to homology with coefficients, with the cellular chain group \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) replaced by \( {H}_{n}\left( {{X}^{n},{X}^{n - 1};G}\right) \) , which is a direct sum of \( G \) ’s, one for each \( n \) -cell. The proof that the cellular homology groups \( {H}_{n}^{CW}\left( X\right) \) agree with singular homology \( {H}_{n}\left( X\right) \) extends immediately to give \( {H}_{n}^{CW}\left( {X;G}\right)  \approx  {H}_{n}\left( {X;G}\right) \) . The cellular boundary maps are given by the same formula as for \( \mathbb{Z} \) coefficients, \( {d}_{n}\left( {\mathop{\sum }\limits_{\alpha }{n}_{\alpha }{e}_{\alpha }^{n}}\right)  = \mathop{\sum }\limits_{{\alpha ,\beta }}{d}_{\alpha \beta }{n}_{\alpha }{e}_{\beta }^{n - 1} \) . The old proof applies, but the following result is needed to know that the coefficients \( {d}_{\alpha \beta } \) are the same as before:

Lemma 2.49. If \( f : {S}^{k} \rightarrow  {S}^{k} \) has degree \( m \) , then \( {f}_{ * } : {H}_{k}\left( {{S}^{k};G}\right)  \rightarrow  {H}_{k}\left( {{S}^{k};G}\right) \) is multiplication by \( m \) .

Proof: As a preliminary observation, note that a homomorphism \( \varphi  : {G}_{1} \rightarrow  {G}_{2} \) induces maps \( {\varphi }_{\sharp } : {C}_{n}\left( {X, A;{G}_{1}}\right)  \rightarrow  {C}_{n}\left( {X, A;{G}_{2}}\right) \) commuting with boundary maps, so there are induced homomorphisms \( {\varphi }_{ * } : {H}_{n}\left( {X, A;{G}_{1}}\right)  \rightarrow  {H}_{n}\left( {X, A;{G}_{2}}\right) \) . These have various naturality properties. For example, they give a commutative diagram mapping the long exact sequence of homology for the pair \( \left( {X, A}\right) \) with \( {G}_{1} \) coefficients to the corresponding sequence with \( {G}_{2} \) coefficients. Also, the maps \( {\varphi }_{ * } \) commute with homomorphisms \( {f}_{ * } \) induced by maps \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) .

Now let \( f : {S}^{k} \rightarrow  {S}^{k} \) have degree \( m \) and let \( \varphi  : \mathbb{Z} \rightarrow  G \) take 1 to a given element \( g \in  G \) . Then we have a commutative diagram as at the right, where commutativity of the outer two squares comes from the inductive calculation of these homology groups, reducing to the case \( k = 0 \) when the commutativity is obvious.

\[
\mathbb{Z} \approx  {\widetilde{H}}_{k}\left( {{S}^{k};\mathbb{Z}}\right) \overset{{f}_{ * }}{ \rightarrow  }{\widetilde{H}}_{k}\left( {{S}^{k};\mathbb{Z}}\right)  \approx  \mathbb{Z}
\]

\[
\left| {\varphi \;}\right| {\varphi }_{ * }\;\left| {{\varphi }_{ * }\;}\right| {\varphi }_{ * }\;|\varphi
\]

\[
G \approx  {\widetilde{H}}_{k}\left( {{S}^{k};G}\right) \overset{{f}_{ * }}{ \rightarrow  }{\widetilde{H}}_{k}\left( {{S}^{k};G}\right)  \approx  G
\]

Since the diagram commutes, the assumption that the map across the top takes 1 to \( m \) implies that the map across the bottom takes \( g \) to \( {mg} \) .

Example 2.50. It is instructive to see what happens to the homology of \( {\mathbb{{RP}}}^{n} \) when the coefficient group \( G \) is chosen to be a field \( F \) . The cellular chain complex is

\[
\cdots \overset{0}{ \rightarrow  }F\overset{2}{ \rightarrow  }F\overset{0}{ \rightarrow  }F\overset{2}{ \rightarrow  }F\overset{0}{ \rightarrow  }F \rightarrow  0
\]

Hence if \( F \) has characteristic 2, for example if \( F = {\mathbb{Z}}_{2} \) , then \( {H}_{k}\left( {{\mathbb{{RP}}}^{n};F}\right)  \approx  F \) for \( 0 \leq  k \leq  n \) , a more uniform answer than with \( \mathbb{Z} \) coefficients. On the other hand, if \( F \) has characteristic different from 2 then the boundary maps \( F\overset{2}{ \rightarrow  }F \) are isomorphisms, hence \( {H}_{k}\left( {{\mathbb{{RP}}}^{n};F}\right) \) is \( F \) for \( k = 0 \) and for \( k = n \) odd, and is zero otherwise.

In §3.A we will see that there is a general algebraic formula expressing homology with arbitrary coefficients in terms of homology with \( \mathbb{Z} \) coefficients. Some easy special cases that give much of the flavor of the general result are included in the Exercises.

In spite of the fact that homology with \( \mathbb{Z} \) coefficients determines homology with other coefficient groups, there are many situations where homology with a suitably chosen coefficient group can provide more information than homology with \( \mathbb{Z} \) coefficients. A good example of this is the proof of the Borsuk-Ulam theorem using \( {\mathbb{Z}}_{2} \) coefficients in §2.B.

As another illustration, we will now give an example of a map \( f : X \rightarrow  Y \) with the property that the induced maps \( {f}_{ * } \) are trivial for homology with \( \mathbb{Z} \) coefficients but not for homology with \( {\mathbb{Z}}_{m} \) coefficients for suitably chosen \( m \) . Thus homology with \( {\mathbb{Z}}_{m} \) coefficients tells us that \( f \) is not homotopic to a constant map, which we would not know using only \( \mathbb{Z} \) coefficients.

Example 2.51. Let \( X \) be a Moore space \( M\left( {{\mathbb{Z}}_{m}, n}\right) \) obtained from \( {S}^{n} \) by attaching a cell \( {e}^{n + 1} \) by a map of degree \( m \) . The quotient map \( f : X \rightarrow  X/{S}^{n} = {S}^{n + 1} \) induces trivial homomorphisms on reduced homology with \( \mathbb{Z} \) coefficients since the nonzero reduced homology groups of \( X \) and \( {S}^{n + 1} \) occur in different dimensions. But with \( {\mathbb{Z}}_{m} \) coefficients the story is different, as we can see by considering the long exact sequence of the pair \( \left( {X,{S}^{n}}\right) \) , which contains the segment

\[
0 = {\widetilde{H}}_{n + 1}\left( {{S}^{n};{\mathbb{Z}}_{m}}\right)  \rightarrow  {\widetilde{H}}_{n + 1}\left( {X;{\mathbb{Z}}_{m}}\right) \overset{{f}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n + 1}\left( {X/{S}^{n};{\mathbb{Z}}_{m}}\right)
\]

Exactness says that \( {f}_{ * } \) is injective, hence nonzero since \( {\widetilde{H}}_{n + 1}\left( {X;{\mathbb{Z}}_{m}}\right) \) is \( {\mathbb{Z}}_{m} \) , the cellular boundary map \( {H}_{n + 1}\left( {{X}^{n + 1},{X}^{n};{\mathbb{Z}}_{m}}\right)  \rightarrow  {H}_{n}\left( {{X}^{n},{X}^{n - 1};{\mathbb{Z}}_{m}}\right) \) being \( {\mathbb{Z}}_{m}\overset{m}{ \rightarrow  }{\mathbb{Z}}_{m} \) .

## Exercises

1. Prove the Brouwer fixed point theorem for maps \( f : {D}^{n} \rightarrow  {D}^{n} \) by applying degree theory to the map \( {S}^{n} \rightarrow  {S}^{n} \) that sends both the northern and southern hemispheres of \( {S}^{n} \) to the southern hemisphere via \( f \) . [This was Brouwer’s original proof.]

2. Given a map \( f : {S}^{2n} \rightarrow  {S}^{2n} \) , show that there is some point \( x \in  {S}^{2n} \) with either \( f\left( x\right)  = x \) or \( f\left( x\right)  =  - x \) . Deduce that every map \( {\mathbb{{RP}}}^{2n} \rightarrow  {\mathbb{{RP}}}^{2n} \) has a fixed point. Construct maps \( {\mathbb{{RP}}}^{{2n} - 1} \rightarrow  {\mathbb{{RP}}}^{{2n} - 1} \) without fixed points from linear transformations \( {\mathbb{R}}^{2n} \rightarrow  {\mathbb{R}}^{2n} \) without eigenvectors.

3. Let \( f : {S}^{n} \rightarrow  {S}^{n} \) be a map of degree zero. Show that there exist points \( x, y \in  {S}^{n} \) with \( f\left( x\right)  = x \) and \( f\left( y\right)  =  - y \) . Use this to show that if \( F \) is a continuous vector field defined on the unit ball \( {D}^{n} \) in \( {\mathbb{R}}^{n} \) such that \( F\left( x\right)  \neq  0 \) for all \( x \) , then there exists a point on \( \partial {D}^{n} \) where \( F \) points radially outward and another point on \( \partial {D}^{n} \) where \( F \) points radially inward.

4. Construct a surjective map \( {S}^{n} \rightarrow  {S}^{n} \) of degree zero, for each \( n \geq  1 \) .

5. Show that any two reflections of \( {S}^{n} \) across different \( n \) -dimensional hyperplanes are homotopic, in fact homotopic through reflections. [The linear algebra formula for a reflection in terms of inner products may be helpful.]

6. Show that every map \( {S}^{n} \rightarrow  {S}^{n} \) can be homotoped to have a fixed point if \( n > 0 \) .

7. For an invertible linear transformation \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) show that the induced map on \( {H}_{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n}-\{ 0\} }\right)  \approx  {\widetilde{H}}_{n - 1}\left( {{\mathbb{R}}^{n}-\{ 0\} }\right)  \approx  \mathbb{Z} \) is1or \( - \mathbb{1} \) according to whether the determinant of \( f \) is positive or negative. [Use Gaussian elimination to show that the matrix of \( f \) can be joined by a path of invertible matrices to a diagonal matrix with ±1's on the diagonal.]

8. A polynomial \( f\left( z\right) \) with complex coefficients, viewed as a map \( \mathbb{C} \rightarrow  \mathbb{C} \) , can always be extended to a continuous map of one-point compactifications \( \widehat{f} : {S}^{2} \rightarrow  {S}^{2} \) . Show that the degree of \( \widehat{f} \) equals the degree of \( f \) as a polynomial. Show also that the local degree of \( \widehat{f} \) at a root of \( f \) is the multiplicity of the root.

9. Compute the homology groups of the following 2-complexes:

(a) The quotient of \( {S}^{2} \) obtained by identifying north and south poles to a point.

(b) \( {S}^{1} \times  \left( {{S}^{1} \vee  {S}^{1}}\right) \) .

(c) The space obtained from \( {D}^{2} \) by first deleting the interiors of two disjoint subdisks in the interior of \( {D}^{2} \) and then identifying all three resulting boundary circles together via homeomorphisms preserving clockwise orientations of these circles.

(d) The quotient space of \( {S}^{1} \times  {S}^{1} \) obtained by identifying points in the circle \( {S}^{1} \times  \left\{  {x}_{0}\right\} \) that differ by \( {2\pi }/m \) rotation and identifying points in the circle \( \left\{  {x}_{0}\right\}   \times  {S}^{1} \) that differ by \( {2\pi }/n \) rotation.

10. Let \( X \) be the quotient space of \( {S}^{2} \) under the identifications \( x \sim   - x \) for \( x \) in the equator \( {S}^{1} \) . Compute the homology groups \( {H}_{i}\left( X\right) \) . Do the same for \( {S}^{3} \) with antipodal points of the equatorial \( {S}^{2} \subset  {S}^{3} \) identified.

11. In an exercise for \( \text{ § }{1.2} \) we described a 3-dimensional CW complex obtained from the cube \( {I}^{3} \) by identifying opposite faces via a one-quarter twist. Compute the homology groups of this complex.

12. Show that the quotient map \( {S}^{1} \times  {S}^{1} \rightarrow  {S}^{2} \) collapsing the subspace \( {S}^{1} \vee  {S}^{1} \) to a point is not nullhomotopic by showing that it induces an isomorphism on \( {H}_{2} \) . On the other hand, show via covering spaces that any map \( {S}^{2} \rightarrow  {S}^{1} \times  {S}^{1} \) is nullhomotopic.

13. Let \( X \) be the 2-complex obtained from \( {S}^{1} \) with its usual cell structure by attaching two 2-cells by maps of degrees 2 and 3, respectively.

(a) Compute the homology groups of all the subcomplexes \( A \subset  X \) and the corresponding quotient complexes \( X/A \) .

(b) Show that \( X \simeq  {S}^{2} \) and that the only subcomplex \( A \subset  X \) for which the quotient map \( X \rightarrow  X/A \) is a homotopy equivalence is the trivial subcomplex, the 0-cell.

14. A map \( f : {S}^{n} \rightarrow  {S}^{n} \) satisfying \( f\left( x\right)  = f\left( {-x}\right) \) for all \( x \) is called an even map. Show that an even map \( {S}^{n} \rightarrow  {S}^{n} \) must have even degree, and that the degree must in fact be zero when \( n \) is even. When \( n \) is odd, show there exist even maps of any given even degree. [Hints: If \( f \) is even, it factors as a composition \( {S}^{n} \rightarrow  {\mathbb{{RP}}}^{n} \rightarrow  {S}^{n} \) . Using the calculation of \( {H}_{n}\left( {\mathbb{{RP}}}^{n}\right) \) in the text, show that the induced map \( {H}_{n}\left( {S}^{n}\right)  \rightarrow  {H}_{n}\left( {\mathbb{{RP}}}^{n}\right) \) sends a generator to twice a generator when \( n \) is odd. It may be helpful to show that the quotient map \( {\mathbb{{RP}}}^{n} \rightarrow  {\mathbb{{RP}}}^{n}/{\mathbb{{RP}}}^{n - 1} \) induces an isomorphism on \( {H}_{n} \) when \( n \) is odd.]

15. Show that if \( X \) is a CW complex then \( {H}_{n}\left( {X}^{n}\right) \) is free by identifying it with the kernel of the cellular boundary map \( {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right)  \rightarrow  {H}_{n - 1}\left( {{X}^{n - 1},{X}^{n - 2}}\right) \) .

16. Let \( {\Delta }^{n} = \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) have its natural \( \Delta \) -complex structure with \( k \) -simplices \( \left\lbrack  {{v}_{{i}_{0}},\cdots ,{v}_{{i}_{k}}}\right\rbrack \) for \( {i}_{0} < \cdots  < {i}_{k} \) . Compute the ranks of the simplicial (or cellular) chain groups \( {\Delta }_{i}\left( {\Delta }^{n}\right) \) and the subgroups of cycles and boundaries. [Hint: Pascal’s triangle.] Apply this to show that the \( k \) -skeleton of \( {\Delta }^{n} \) has homology groups \( {\widetilde{H}}_{i}\left( {\left( {\Delta }^{n}\right) }^{k}\right) \) equal to 0 for \( i < k \) , and free of rank \( \left( \begin{matrix} n \\  k + 1 \end{matrix}\right) \) for \( i = k \) .

17. Show the isomorphism between cellular and singular homology is natural in the following sense: A map \( f : X \rightarrow  Y \) that is cellular - satisfying \( f\left( {X}^{n}\right)  \subset  {Y}^{n} \) for all \( n \) - induces a chain map \( {f}_{ * } \) between the cellular chain complexes of \( X \) and \( Y \) , and the map \( {f}_{ * } : {H}_{n}^{CW}\left( X\right)  \rightarrow  {H}_{n}^{CW}\left( Y\right) \) induced by this chain map corresponds to \( {f}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) under the isomorphism \( {H}_{n}^{CW} \approx  {H}_{n} \) .

18. For a CW pair \( \left( {X, A}\right) \) show there is a relative cellular chain complex formed by the groups \( {H}_{i}\left( {{X}^{i},{X}^{i - 1} \cup  {A}^{i}}\right) \) , having homology groups isomorphic to \( {H}_{n}\left( {X, A}\right) \) .

19. Compute \( {H}_{i}\left( {{\mathbb{{RP}}}^{n}/{\mathbb{{RP}}}^{m}}\right) \) for \( m < n \) by cellular homology, using the standard CW structure on \( {\mathbb{{RP}}}^{n} \) with \( {\mathbb{{RP}}}^{m} \) as its \( m \) -skeleton.

20. For finite CW complexes \( X \) and \( Y \) , show that \( \chi \left( {X \times  Y}\right)  = \chi \left( X\right) \chi \left( Y\right) \) .

21. If a finite CW complex \( X \) is the union of subcomplexes \( A \) and \( B \) , show that \( \chi \left( X\right)  = \chi \left( A\right)  + \chi \left( B\right)  - \chi \left( {A \cap  B}\right) . \)

22. For \( X \) a finite CW complex and \( p : \widetilde{X} \rightarrow  X \) an \( n \) -sheeted covering space, show that \( \chi \left( \widetilde{X}\right)  = {n\chi }\left( X\right) . \)

23. Show that if the closed orientable surface \( {M}_{g} \) of genus \( g \) is a covering space of \( {M}_{h} \) , then \( g = n\left( {h - 1}\right)  + 1 \) for some \( n \) , namely, \( n \) is the number of sheets in the covering. [Conversely, if \( g = n\left( {h - 1}\right)  + 1 \) then there is an \( n \) -sheeted covering \( {M}_{g} \rightarrow  {M}_{h} \) , as we saw in Example 1.41.]

24. Suppose we build \( {S}^{2} \) from a finite collection of polygons by identifying edges in pairs. Show that in the resulting CW structure on \( {S}^{2} \) the 1-skeleton cannot be either of the two graphs shown, with five and six vertices. [This is one step in a proof that neither of these graphs embeds in \( {\mathbb{R}}^{2} \) .]

![bo_d7dtv0s91nqc73eq8nv0_165_1123_1205_466_197_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_165_1123_1205_466_197_0.jpg)

25. Show that for each \( n \in  \mathbb{Z} \) there is a unique function \( \varphi \) assigning an integer to each finite CW complex, such that (a) \( \varphi \left( X\right)  = \varphi \left( Y\right) \) if \( X \) and \( Y \) are homeomorphic, (b) \( \varphi \left( X\right)  = \varphi \left( A\right)  + \varphi \left( {X/A}\right) \) if \( A \) is a subcomplex of \( X \) , and (c) \( \varphi \left( {S}^{0}\right)  = n \) . For such a function \( \varphi \) , show that \( \varphi \left( X\right)  = \varphi \left( Y\right) \) if \( X \simeq  Y \) .

26. For a pair \( \left( {X, A}\right) \) , let \( X \cup  {CA} \) be \( X \) with a cone on \( A \) attached.

(a) Show that \( X \) is a retract of \( X \cup  {CA} \) iff \( A \) is contractible in \( X \) : There is a homotopy \( {f}_{t} : A \rightarrow  X \) with \( {f}_{0} \) the inclusion \( A \hookrightarrow  X \) and \( {f}_{1} \) a constant map.

(b) Show that if \( A \) is contractible in \( X \) then \( {H}_{n}\left( {X, A}\right)  \approx  {\widetilde{H}}_{n}\left( X\right)  \oplus  {\widetilde{H}}_{n - 1}\left( A\right) \) , using the fact that \( \left( {X \cup  {CA}}\right) /X \) is the suspension \( {SA} \) of \( A \) .

27. The short exact sequences \( 0 \rightarrow  {C}_{n}\left( A\right)  \rightarrow  {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( {X, A}\right)  \rightarrow  0 \) always split, but why does this not always yield splittings \( {H}_{n}\left( X\right)  \approx  {H}_{n}\left( A\right)  \oplus  {H}_{n}\left( {X, A}\right) \) ?

28. (a) Use the Mayer-Vietoris sequence to compute the homology groups of the space obtained from a torus \( {S}^{1} \times  {S}^{1} \) by attaching a Möbius band via a homeomorphism from the boundary circle of the Möbius band to the circle \( {S}^{1} \times  \left\{  {x}_{0}\right\} \) in the torus.

(b) Do the same for the space obtained by attaching a Möbius band to \( {\mathbb{{RP}}}^{2} \) via a homeomorphism of its boundary circle to the standard \( {\mathbb{{RP}}}^{1} \subset  {\mathbb{{RP}}}^{2} \) .

29. The surface \( {M}_{g} \) of genus \( g \) , embedded in \( {\mathbb{R}}^{3} \) in the standard way, bounds a compact region \( R \) . Two copies of \( R \) , glued together by the identity map between their boundary surfaces \( {M}_{g} \) , form a closed 3-manifold \( X \) . Compute the homology groups of \( X \) via the Mayer-Vietoris sequence for this decomposition of \( X \) into two copies of \( R \) . Also compute the relative groups \( {H}_{i}\left( {R,{M}_{g}}\right) \) .

30. For the mapping torus \( {T}_{f} \) of a map \( f : X \rightarrow  X \) , we constructed in Example 2.48 a long exact sequence \( \cdots  \rightarrow  {H}_{n}\left( X\right) \xrightarrow[]{\mathbb{1} - {f}_{ * }}{H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( {T}_{f}\right)  \rightarrow  {H}_{n - 1}\left( X\right)  \rightarrow  \cdots \) . Use this to compute the homology of the mapping tori of the following maps:

(a) A reflection \( {S}^{2} \rightarrow  {S}^{2} \) .

(b) A map \( {S}^{2} \rightarrow  {S}^{2} \) of degree 2 .

(c) The map \( {S}^{1} \times  {S}^{1} \rightarrow  {S}^{1} \times  {S}^{1} \) that is the identity on one factor and a reflection on the other.

(d) The map \( {S}^{1} \times  {S}^{1} \rightarrow  {S}^{1} \times  {S}^{1} \) that is a reflection on each factor.

(e) The map \( {S}^{1} \times  {S}^{1} \rightarrow  {S}^{1} \times  {S}^{1} \) that interchanges the two factors and then reflects one of the factors.

31. Use the Mayer-Vietoris sequence to show there are isomorphisms \( {\widetilde{H}}_{n}\left( {X \vee  Y}\right)  \approx \; {\widetilde{H}}_{n}\left( X\right)  \oplus  {\widetilde{H}}_{n}\left( Y\right) \) if the basepoints of \( X \) and \( Y \) that are identified in \( X \vee  Y \) are deformation retracts of neighborhoods \( U \subset  X \) and \( V \subset  Y \) .

32. For \( {SX} \) the suspension of \( X \) , show by a Mayer-Vietoris sequence that there are isomorphisms \( {\widetilde{H}}_{n}\left( {SX}\right)  \approx  {\widetilde{H}}_{n - 1}\left( X\right) \) for all \( n \) .

33. Suppose the space \( X \) is the union of open sets \( {A}_{1},\cdots ,{A}_{n} \) such that each intersection \( {A}_{{i}_{1}} \cap  \cdots  \cap  {A}_{{i}_{k}} \) is either empty or has trivial reduced homology groups. Show that \( {\widetilde{H}}_{i}\left( X\right)  = 0 \) for \( i \geq  n - 1 \) , and give an example showing this inequality is best possible, for each \( n \) .

34. [Deleted - see the errata for comments.]

35. Use the Mayer-Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex \( X \) for which \( {H}_{1}\left( X\right) \) contains torsion, cannot be embedded as a subspace of \( {\mathbb{R}}^{3} \) in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to \( X \) . [This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]

36. Show that \( {H}_{i}\left( {X \times  {S}^{n}}\right)  \approx  {H}_{i}\left( X\right)  \oplus  {H}_{i - n}\left( X\right) \) for all \( i \) and \( n \) , where \( {H}_{i} = 0 \) for \( i < 0 \) by definition. Namely, show \( {H}_{i}\left( {X \times  {S}^{n}}\right)  \approx  {H}_{i}\left( X\right)  \oplus  {H}_{i}\left( {X \times  {S}^{n}, X \times  \left\{  {x}_{0}\right\}  }\right) \) and \( {H}_{i}\left( {X \times  {S}^{n}, X \times  \left\{  {x}_{0}\right\}  }\right)  \approx  {H}_{i - 1}\left( {X \times  {S}^{n - 1}, X \times  \left\{  {x}_{0}\right\}  }\right) \) . [For the latter isomorphism the relative Mayer-Vietoris sequence yields an easy proof.]

37. Give an elementary derivation for the Mayer-Vietoris sequence in simplicial homology for a \( \Delta \) -complex \( X \) decomposed as the union of subcomplexes \( A \) and \( B \) . 38. Show that a commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_167_330_200_1144_143_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_167_330_200_1144_143_0.jpg)

with the two sequences across the top and bottom exact, gives rise to an exact sequence \( \cdots  \rightarrow  {E}_{n + 1} \rightarrow  {B}_{n} \rightarrow  {C}_{n} \oplus  {D}_{n} \rightarrow  {E}_{n} \rightarrow  {B}_{n - 1} \rightarrow  \cdots \) where the maps are obtained from those in the previous diagram in the obvious way, except that \( {B}_{n} \rightarrow  {C}_{n} \oplus  {D}_{n} \) has a minus sign in one coordinate.

39. Use the preceding exercise to derive relative Mayer-Vietoris sequences for CW pairs \( \left( {X, Y}\right)  = \left( {A \cup  B, C \cup  D}\right) \) with \( A = B \) or \( C = D \) .

40. From the long exact sequence of homology groups associated to the short exact sequence of chain complexes \( 0 \rightarrow  {C}_{i}\left( X\right) \overset{n}{ \rightarrow  }{C}_{i}\left( X\right)  \rightarrow  {C}_{i}\left( {X;{\mathbb{Z}}_{n}}\right)  \rightarrow  0 \) deduce immediately that there are short exact sequences

\[
0 \rightarrow  {H}_{i}\left( X\right) /n{H}_{i}\left( X\right)  \rightarrow  {H}_{i}\left( {X;{\mathbb{Z}}_{n}}\right)  \rightarrow  n\text{ -Torsion }\left( {{H}_{i - 1}\left( X\right) }\right)  \rightarrow  0
\]

where \( n \) -Torsion \( \left( G\right) \) is the kernel of the map \( G\overset{n}{ \rightarrow  }G, g \mapsto  {ng} \) . Use this to show that \( {\widetilde{H}}_{i}\left( {X;{\mathbb{Z}}_{p}}\right)  = 0 \) for all \( i \) and all primes \( p \) iff \( {\widetilde{H}}_{i}\left( X\right) \) is a vector space over \( \mathbb{Q} \) for all \( i \) . 41. For \( X \) a finite CW complex and \( F \) a field, show that the Euler characteristic \( \chi \left( X\right) \) can also be computed by the formula \( \chi \left( X\right)  = \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\dim {H}_{n}\left( {X;F}\right) \) , the alternating sum of the dimensions of the vector spaces \( {H}_{n}\left( {X;F}\right) \) .

42. Let \( X \) be a finite connected graph having no vertex that is the endpoint of just one edge, and suppose that \( {H}_{1}\left( {X;\mathbb{Z}}\right) \) is free abelian of rank \( n > 1 \) , so the group of automorphisms of \( {H}_{1}\left( {X;\mathbb{Z}}\right) \) is \( G{L}_{n}\left( \mathbb{Z}\right) \) , the group of invertible \( n \times  n \) matrices with integer entries whose inverse matrix also has integer entries. Show that if \( G \) is a finite group of homeomorphisms of \( X \) , then the homomorphism \( G \rightarrow  G{L}_{n}\left( \mathbb{Z}\right) \) assigning to \( g : X \rightarrow  X \) the induced homomorphism \( {g}_{ * } : {H}_{1}\left( {X;\mathbb{Z}}\right)  \rightarrow  {H}_{1}\left( {X;\mathbb{Z}}\right) \) is injective. Show the same result holds if the coefficient group \( \mathbb{Z} \) is replaced by \( {\mathbb{Z}}_{m} \) with \( m > 2 \) . What goes wrong when \( m = 2 \) ?

43. (a) Show that a chain complex of free abelian groups \( {C}_{n} \) splits as a direct sum of subcomplexes \( 0 \rightarrow  {L}_{n + 1} \rightarrow  {K}_{n} \rightarrow  0 \) with at most two nonzero terms. [Show the short exact sequence \( 0 \rightarrow  \operatorname{Ker}\partial  \rightarrow  {C}_{n} \rightarrow  \operatorname{Im}\partial  \rightarrow  0 \) splits and take \( {K}_{n} = \operatorname{Ker}\partial \) .]

(b) In case the groups \( {C}_{n} \) are finitely generated, show there is a further splitting into summands \( 0 \rightarrow  \mathbb{Z} \rightarrow  0 \) and \( 0 \rightarrow  \mathbb{Z}\overset{m}{ \rightarrow  }\mathbb{Z} \rightarrow  0 \) . [Reduce the matrix of the boundary map \( {L}_{n + 1} \rightarrow  {K}_{n} \) to echelon form by elementary row and column operations.]

(c) Deduce that if \( X \) is a CW complex with finitely many cells in each dimension, then \( {H}_{n}\left( {X;G}\right) \) is the direct sum of the following groups:

- a copy of \( G \) for each \( \mathbb{Z} \) summand of \( {H}_{n}\left( X\right) \)

- a copy of \( G/{mG} \) for each \( {\mathbb{Z}}_{m} \) summand of \( {H}_{n}\left( X\right) \)

- a copy of the kernel of \( G\overset{m}{ \rightarrow  }G \) for each \( {\mathbb{Z}}_{m} \) summand of \( {H}_{n - 1}\left( X\right) \)
