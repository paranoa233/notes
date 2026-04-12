# 3.1 Cohomology Groups

## Chapter 3

## Cohomology

Cohomology is an algebraic variant of homology, the result of a simple dualization in the definition. Not surprisingly, the cohomology groups \( {H}^{i}\left( X\right) \) satisfy axioms much like the axioms for homology, except that induced homomorphisms go in the opposite direction as a result of the dualization. The basic distinction between homology and cohomology is thus that cohomology groups are contravariant functors while homology groups are covariant. In terms of intrinsic information, however, there is not a big difference between homology groups and cohomology groups. The homology groups of a space determine its cohomology groups, and the converse holds at least when the homology groups are finitely generated.

What is a little surprising is that contravariance leads to extra structure in cohomology. This first appears in a natural product, called cup product, which makes the cohomology groups of a space into a ring. This is an extremely useful piece of additional structure, and much of this chapter is devoted to studying cup products, which are considerably more subtle than the additive structure of cohomology.

How does contravariance lead to a product in cohomology that is not present in homology? Actually there is a natural product in homology, but it takes the somewhat different form of a map \( {H}_{i}\left( X\right)  \times  {H}_{j}\left( Y\right)  \rightarrow  {H}_{i + j}\left( {X \times  Y}\right) \) called the cross product. If both \( X \) and \( Y \) are CW complexes, this cross product in homology is induced from a map of cellular chains sending a pair \( \left( {{e}^{i},{e}^{j}}\right) \) consisting of a cell of \( X \) and a cell of \( Y \) to the product cell \( {e}^{i} \times  {e}^{j} \) in \( X \times  Y \) . The details of the construction are described in §3.B. Taking \( X = Y \) , we thus have the first half of a hypothetical product

\[
{H}_{i}\left( X\right)  \times  {H}_{j}\left( X\right)  \rightarrow  {H}_{i + j}\left( {X \times  X}\right)  \rightarrow  {H}_{i + j}\left( X\right)
\]

The difficulty is in defining the second map. The natural thing would be for this to be induced by a map \( X \times  X \rightarrow  X \) . The multiplication map in a topological group, or more generally an H-space, is such a map, and the resulting Pontryagin product can be quite useful when studying these spaces, as we show in \( \text{ § }3 \) .C. But for general \( X \) , the only natural maps \( X \times  X \rightarrow  X \) are the projections onto one of the factors, and since these projections collapse the other factor to a point, the resulting product in homology is rather trivial.

With cohomology, however, the situation is better. One still has a cross product \( {H}^{i}\left( X\right)  \times  {H}^{j}\left( Y\right)  \rightarrow  {H}^{i + j}\left( {X \times  Y}\right) \) constructed in much the same way as in homology, so one can again take \( X = Y \) and get the first half of a product

\[
{H}^{i}\left( X\right)  \times  {H}^{j}\left( X\right)  \rightarrow  {H}^{i + j}\left( {X \times  X}\right)  \rightarrow  {H}^{i + j}\left( X\right)
\]

But now by contravariance the second map would be induced by a map \( X \rightarrow  X \times  X \) , and there is an obvious candidate for this map, the diagonal map \( \Delta \left( x\right)  = \left( {x, x}\right) \) . This turns out to work very nicely, giving a well-behaved product in cohomology, the cup product.

Another sort of extra structure in cohomology whose existence is traceable to contravariance is provided by cohomology operations. These make the cohomology groups of a space into a module over a certain rather complicated ring. Cohomology operations lie at a depth somewhat greater than the cup product structure, so we defer their study to §4.L.

The extra layer of algebra in cohomology arising from the dualization in its definition may seem at first to be separating it further from topology, but there are many topological situations where cohomology arises quite naturally. One of these is Poincaré duality, the topic of the third section of this chapter. Another is obstruction theory, covered in §4.3. Characteristic classes in vector bundle theory (see [Milnor & Stasheff 1974] or [VBKT]) provide a further instance.

From the viewpoint of homotopy theory, cohomology is in some ways more basic than homology. As we shall see in §4.3, cohomology has a description in terms of homotopy classes of maps that is very similar to, and in a certain sense dual to, the definition of homotopy groups. There is an analog of this for homology, described in §4.F, but the construction is more complicated.

## The Idea of Cohomology

Let us look at a few low-dimensional examples to get an idea of how one might be led naturally to consider cohomology groups, and to see what properties of a space they might be measuring. For the sake of simplicity we consider simplicial cohomology of \( \Delta \) -complexes, rather than singular cohomology of more general spaces.

Taking the simplest case first, let \( X \) be a 1-dimensional \( \Delta \) -complex, or in other words an oriented graph. For a fixed abelian group \( G \) , the set of all functions from vertices of \( X \) to \( G \) also forms an abelian group, which we denote by \( {\Delta }^{0}\left( {X;G}\right) \) . Similarly the set of all functions assigning an element of \( G \) to each edge of \( X \) forms an abelian group \( {\Delta }^{1}\left( {X;G}\right) \) . We will be interested in the homomorphism \( \delta  : {\Delta }^{0}\left( {X;G}\right)  \rightarrow  {\Delta }^{1}\left( {X;G}\right) \) sending \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) to the function \( {\delta \varphi } \in  {\Delta }^{1}\left( {X;G}\right) \) whose value on an oriented edge \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) is the difference \( \varphi \left( {v}_{1}\right)  - \varphi \left( {v}_{0}\right) \) . For example, \( X \) might be the graph formed by a system of trails on a mountain, with vertices at the junctions between trails. The function \( \varphi \) could then assign to each junction its elevation above sea level, in which case \( {\delta \varphi } \) would measure the net change in elevation along the trail from one junction to the next. Or \( X \) might represent a simple electrical circuit with \( \varphi \) measuring voltages at the connection points, the vertices, and \( {\delta \varphi } \) measuring changes in voltage across the components of the circuit, represented by edges.

Regarding the map \( \delta  : {\Delta }^{0}\left( {X;G}\right)  \rightarrow  {\Delta }^{1}\left( {X;G}\right) \) as a chain complex with 0 ’s before and after these two terms, the homology groups of this chain complex are by definition the simplicial cohomology groups of \( X \) , namely \( {H}^{0}\left( {X;G}\right)  = \operatorname{Ker}\delta  \subset  {\Delta }^{0}\left( {X;G}\right) \) and \( {H}^{1}\left( {X;G}\right)  = {\Delta }^{1}\left( {X;G}\right) /\operatorname{Im}\delta \) . For simplicity we are using here the same notation as will be used for singular cohomology later in the chapter, in anticipation of the theorem that the two theories coincide for \( \Delta \) -complexes, as we show in \( \text{ § }{3.1} \) .

The group \( {H}^{0}\left( {X;G}\right) \) is easy to describe explicitly. A function \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) has \( {\delta \varphi } = 0 \) iff \( \varphi \) takes the same value at both ends of each edge of \( X \) . This is equivalent to saying that \( \varphi \) is constant on each component of \( X \) . So \( {H}^{0}\left( {X;G}\right) \) is the group of all functions from the set of components of \( X \) to \( G \) . This is a direct product of copies of \( G \) , one for each component of \( X \) .

The cohomology group \( {H}^{1}\left( {X;G}\right)  = {\Delta }^{1}\left( {X;G}\right) /\operatorname{Im}\delta \) will be trivial iff the equation \( {\delta \varphi } = \psi \) has a solution \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) for each \( \psi  \in  {\Delta }^{1}\left( {X;G}\right) \) . Solving this equation means deciding whether specifying the change in \( \varphi \) across each edge of \( X \) determines an actual function \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) . This is rather like the calculus problem of finding a function having a specified derivative, with the difference operator \( \delta \) playing the role of differentiation. As in calculus, if a solution of \( {\delta \varphi } = \psi \) exists, it will be unique up to adding an element of the kernel of \( \delta \) , that is, a function that is constant on each component of \( X \) .

The equation \( {\delta \varphi } = \psi \) is always solvable if \( X \) is a tree since if we choose arbitrarily a value for \( \varphi \) at a basepoint vertex \( {v}_{0} \) , then if the change in \( \varphi \) across each edge of \( X \) is specified, this uniquely determines the value of \( \varphi \) at every other vertex \( v \) by induction along the unique path from \( {v}_{0} \) to \( v \) in the tree. When \( X \) is not a tree, we first choose a maximal tree in each component of \( X \) . Then, since every vertex lies in one of these maximal trees, the values of \( \psi \) on the edges of the maximal trees determine \( \varphi \) uniquely up to a constant on each component of \( X \) . But in order for the equation \( {\delta \varphi } = \psi \) to hold, the value of \( \psi \) on each edge not in any of the maximal trees must equal the difference in the already-determined values of \( \varphi \) at the two ends of the edge. This condition need not be satisfied since \( \psi \) can have arbitrary values on these edges. Thus we see that the cohomology group \( {H}^{1}\left( {X;G}\right) \) is a direct product of copies of the group \( G \) , one copy for each edge of \( X \) not in one of the chosen maximal trees. This can be compared with the homology group \( {H}_{1}\left( {X;G}\right) \) which consists of a direct sum of copies of \( G \) , one for each edge of \( X \) not in one of the maximal trees. Note that the relation between \( {H}^{1}\left( {X;G}\right) \) and \( {H}_{1}\left( {X;G}\right) \) is the same as the relation between \( {H}^{0}\left( {X;G}\right) \) and \( {H}_{0}\left( {X;G}\right) \) , with \( {H}^{0}\left( {X;G}\right) \) being a direct product of copies of \( G \) and \( {H}_{0}\left( {X;G}\right) \) a direct sum, with one copy for each component of \( X \) in either case.

Now let us move up a dimension, taking \( X \) to be a 2-dimensional \( \Delta \) -complex. Define \( {\Delta }^{0}\left( {X;G}\right) \) and \( {\Delta }^{1}\left( {X;G}\right) \) as before, as functions from vertices and edges of \( X \) to the abelian group \( G \) , and define \( {\Delta }^{2}\left( {X;G}\right) \) to be the functions from 2-simplices of \( X \) to \( G \) . A homomorphism \( \delta  : {\Delta }^{1}\left( {X;G}\right)  \rightarrow  {\Delta }^{2}\left( {X;G}\right) \) is defined by \( {\delta \psi }\left( \left\lbrack  {{v}_{0},{v}_{1},{v}_{2}}\right\rbrack  \right)  = \; \psi \left( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack  \right)  + \psi \left( \left\lbrack  {{v}_{1},{v}_{2}}\right\rbrack  \right)  - \psi \left( \left\lbrack  {{v}_{0},{v}_{2}}\right\rbrack  \right) \) , a signed sum of the values of \( \psi \) on the three edges in the boundary of \( \left\lbrack  {{v}_{0},{v}_{1},{v}_{2}}\right\rbrack \) , just as \( {\delta \varphi }\left( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack  \right) \) for \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) was a signed sum of the values of \( \varphi \) on the boundary of \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) . The two homomorphisms \( {\Delta }^{0}\left( {X;G}\right) \overset{\delta }{ \rightarrow  }{\Delta }^{1}\left( {X;G}\right) \overset{\delta }{ \rightarrow  }{\Delta }^{2}\left( {X;G}\right) \) form a chain complex since for \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) we have \( {\delta \delta \varphi } = \left( {\varphi \left( {v}_{1}\right)  - \varphi \left( {v}_{0}\right) }\right)  + \left( {\varphi \left( {v}_{2}\right)  - \varphi \left( {v}_{1}\right) }\right)  - \left( {\varphi \left( {v}_{2}\right)  - \varphi \left( {v}_{0}\right) }\right)  = 0 \) . Extending this chain complex by 0 's on each end, the resulting homology groups are by definition the cohomology groups \( {H}^{i}\left( {X;G}\right) \) .

The formula for the map \( \delta  : {\Delta }^{1}\left( {X;G}\right)  \rightarrow  {\Delta }^{2}\left( {X;G}\right) \) can be looked at from several different viewpoints. Perhaps the simplest is the observation that \( {\delta \psi } = 0 \) iff \( \psi \) satisfies the additivity property \( \psi \left( \left\lbrack  {{v}_{0},{v}_{2}}\right\rbrack  \right)  = \psi \left( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack  \right)  + \psi \left( \left\lbrack  {{v}_{1},{v}_{2}}\right\rbrack  \right) \) , where we think of the edge \( \left\lbrack  {{v}_{0},{v}_{2}}\right\rbrack \) as the sum of the edges \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) and \( \left\lbrack  {{v}_{1},{v}_{2}}\right\rbrack \) . Thus \( {\delta \psi } \) measures the deviation of \( \psi \) from being additive.

From another point of view, \( {\delta \psi } \) can be regarded as an obstruction to finding \( \varphi  \in  {\Delta }^{0}\left( {X;G}\right) \) with \( \psi  = {\delta \varphi } \) , for if \( \psi  = {\delta \varphi } \) then \( {\delta \psi } = 0 \) since \( {\delta \delta \varphi } = 0 \) as we saw above. We can think of \( {\delta \psi } \) as a local obstruction to solving \( \psi  = {\delta \varphi } \) since it depends only on the values of \( \psi \) within individual 2-simplices of \( X \) . If this local obstruction vanishes, then \( \psi \) defines an element of \( {H}^{1}\left( {X;G}\right) \) which is zero iff \( \psi  = {\delta \varphi } \) has an actual solution. This class in \( {H}^{1}\left( {X;G}\right) \) is thus the global obstruction to solving \( \psi  = {\delta \varphi } \) . This situation is similar to the calculus problem of determining whether a given vector field is the gradient vector field of some function. The local obstruction here is the vanishing of the curl of the vector field, and the global obstruction is the vanishing of all line integrals around closed loops in the domain of the vector field.

The condition \( {\delta \psi } = 0 \) has an interpretation of a more geometric nature when \( X \) is a surface and the group \( G \) is \( \mathbb{Z} \) or \( {\mathbb{Z}}_{2} \) . Consider first the simpler case \( G = {\mathbb{Z}}_{2} \) . The condition \( {\delta \psi } = 0 \) means that the number of times that \( \psi \) takes the value 1 on the edges of each 2-simplex is even, either 0 or 2 . This means we can associate to \( \psi \) a collection \( {C}_{\psi } \) of disjoint curves in \( X \) crossing the 1-skeleton transversely, such that the number of intersections of \( {C}_{\psi } \) with each edge is equal to the value of \( \psi \) on that edge. If \( \psi  = {\delta \varphi } \) for some \( \varphi \) , then the curves of \( {C}_{\psi } \) divide \( X \) into two regions \( {X}_{0} \) and \( {X}_{1} \) where the subscript indicates the value of \( \varphi \) on all vertices in the region.

![bo_d7dtv0s91nqc73eq8nv0_196_1052_1921_535_353_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_196_1052_1921_535_353_0.jpg)

When \( G = \mathbb{Z} \) we can refine this construction by building \( {C}_{\psi } \) from a number of arcs in each 2-simplex, each arc having a transverse orientation, the orientation which agrees or disagrees with the orientation of each edge according to the sign of the value of \( \psi \) on the edge, as in the figure at the right. The resulting collection \( {C}_{\psi } \) of disjoint curves in \( X \) can be thought of as something like level curves for a function \( \varphi \) with \( {\delta \varphi } = \psi \) , if such a function exists. The value of \( \varphi \) changes by 1 each time a curve of \( {C}_{\psi } \) is crossed. For example, if \( X \) is a disk then we will show that \( {H}^{1}\left( {X;\mathbb{Z}}\right)  = 0 \) , so \( {\delta \psi } = 0 \) implies \( \psi  = {\delta \varphi } \) for some \( \varphi \) , hence every transverse curve system \( {C}_{\psi } \) forms the level curves of a function \( \varphi \) . On the other hand, if \( X \) is an annulus then this need no longer be true, as illustrated in the example shown in the figure at the left, where the equation \( \psi  = {\delta \varphi } \) obviously has no solution even though \( {\delta \psi } = 0 \) . By identifying the inner and outer boundary circles of this annulus we obtain a similar example on the torus. Even with \( G = {\mathbb{Z}}_{2} \) the equation \( \psi  = {\delta \varphi } \) has no solution since the curve \( {C}_{\psi } \) does not separate \( X \) into two regions \( {X}_{0} \) and \( {X}_{1} \) .

![bo_d7dtv0s91nqc73eq8nv0_197_894_264_686_602_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_197_894_264_686_602_0.jpg)

![bo_d7dtv0s91nqc73eq8nv0_197_207_943_353_353_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_197_207_943_353_353_0.jpg)

The key to relating cohomology groups to homology groups is the observation that a function from \( i \) -simplices of \( X \) to \( G \) is equivalent to a homomorphism from the simplicial chain group \( {\Delta }_{i}\left( X\right) \) to \( G \) . This is because \( {\Delta }_{i}\left( X\right) \) is free abelian with basis the \( i \) -simplices of \( X \) , and a homomorphism with domain a free abelian group is uniquely determined by its values on basis elements, which can be assigned arbitrarily. Thus we have an identification of \( {\Delta }^{i}\left( {X;G}\right) \) with the group \( \operatorname{Hom}\left( {{\Delta }_{i}\left( X\right) , G}\right) \) of homomorphisms \( {\Delta }_{i}\left( X\right)  \rightarrow  G \) , which is called the dual group of \( {\Delta }_{i}\left( X\right) \) . There is also a simple relationship of duality between the homomorphism \( \delta  : {\Delta }^{i}\left( {X;G}\right)  \rightarrow  {\Delta }^{i + 1}\left( {X;G}\right) \) and the boundary homomorphism \( \partial  : {\Delta }_{i + 1}\left( X\right)  \rightarrow  {\Delta }_{i}\left( X\right) \) . The general formula for \( \delta \) is

\[
{\delta \varphi }\left( \left\lbrack  {{v}_{0},\cdots ,{v}_{i + 1}}\right\rbrack  \right)  = \mathop{\sum }\limits_{j}{\left( -1\right) }^{j}\varphi \left( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{i + 1}}\right\rbrack  \right)
\]

and the latter sum is just \( \varphi \left( {\partial \left\lbrack  {{v}_{0},\cdots ,{v}_{i + 1}}\right\rbrack  }\right) \) . Thus we have \( {\delta \varphi } = \varphi \partial \) . In other words, \( \delta \) sends each \( \varphi  \in  \operatorname{Hom}\left( {{\Delta }_{i}\left( X\right) , G}\right) \) to the composition \( {\Delta }_{i + 1}\left( X\right) \overset{\partial }{ \rightarrow  }{\Delta }_{i}\left( X\right) \overset{\varphi }{ \rightarrow  }G \) , which in the language of linear algebra means that \( \delta \) is the dual map of \( \partial \) .

Thus we have the algebraic problem of understanding the relationship between the homology groups of a chain complex and the homology groups of the dual complex obtained by applying the functor \( C \mapsto  \operatorname{Hom}\left( {C, G}\right) \) . This is the first topic of the chapter.

Homology groups \( {H}_{n}\left( X\right) \) are the result of a two-stage process: First one forms a chain complex \( \cdots  \rightarrow  {C}_{n}\overset{\partial }{ \rightarrow  }{C}_{n - 1} \rightarrow  \cdots \) of singular, simplicial, or cellular chains, then one takes the homology groups of this chain complex, Ker \( \partial /\operatorname{Im}\partial \) . To obtain the cohomology groups \( {H}^{n}\left( {X;G}\right) \) we interpolate an intermediate step, replacing the chain groups \( {C}_{n} \) by the dual groups \( \operatorname{Hom}\left( {{C}_{n}, G}\right) \) and the boundary maps \( \partial \) by their dual maps \( \delta \) , before forming the cohomology groups Ker \( \delta /\operatorname{Im}\delta \) . The plan for this section is first to sort out the algebra of this dualization process and show that the cohomology groups are determined algebraically by the homology groups, though in a somewhat subtle way. Then after this algebraic excursion we will define the cohomology groups of spaces and show that these satisfy basic properties very much like those for homology. The payoff for all this formal work will begin to be apparent in subsequent sections.

## The Universal Coefficient Theorem

Let us begin with a simple example. Consider the chain complex

![bo_d7dtv0s91nqc73eq8nv0_198_508_1112_782_152_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_198_508_1112_782_152_0.jpg)

where \( \mathbb{Z}\overset{2}{ \rightarrow  }\mathbb{Z} \) is the map \( x \mapsto  {2x} \) . If we dualize by taking \( \operatorname{Hom}\left( {-, G}\right) \) with \( G = \mathbb{Z} \) , we obtain the cochain complex

![bo_d7dtv0s91nqc73eq8nv0_198_503_1380_787_151_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_198_503_1380_787_151_0.jpg)

In the original chain complex the homology groups are \( \mathbb{Z} \) ’s in dimensions 0 and 3, together with a \( {\mathbb{Z}}_{2} \) in dimension 1 . The homology groups of the dual cochain complex, which are called cohomology groups to emphasize the dualization, are again Z's in dimensions 0 and 3, but the \( {\mathbb{Z}}_{2} \) in the 1-dimensional homology of the original complex has shifted up a dimension to become a \( {\mathbb{Z}}_{2} \) in 2-dimensional cohomology.

More generally, consider any chain complex of finitely generated free abelian groups. Such a chain complex always splits as the direct sum of elementary complexes of the forms \( 0 \rightarrow  \mathbb{Z} \rightarrow  0 \) and \( 0 \rightarrow  \mathbb{Z}\overset{m}{ \rightarrow  }\mathbb{Z} \rightarrow  0 \) , according to Exercise 43 in §2.2. Applying Hom \( \left( {-,\mathbb{Z}}\right) \) to this direct sum of elementary complexes, we obtain the direct sum of the corresponding dual complexes \( 0 \leftarrow  \mathbb{Z} \leftarrow  0 \) and \( 0 \leftarrow  \mathbb{Z}\overset{m}{ \leftarrow  }\mathbb{Z} \leftarrow  0 \) . Thus the cohomology groups are the same as the homology groups except that torsion is shifted up one dimension. We will see later in this section that the same relation between homology and cohomology holds whenever the homology groups are finitely generated, even when the chain groups are not finitely generated. It would also be quite easy to see in this example what happens if \( \operatorname{Hom}\left( {-,\mathbb{Z}}\right) \) is replaced by \( \operatorname{Hom}\left( {-, G}\right) \) , since the dual elementary cochain complexes would then be \( 0 \leftarrow  G \leftarrow  0 \) and \( 0 \leftarrow  G\overset{m}{ \leftarrow  }G \leftarrow  0 \) .

Consider now a completely general chain complex \( C \) of free abelian groups

\[
\cdots  \rightarrow  {C}_{n + 1}\overset{\partial }{ \rightarrow  }{C}_{n}\overset{\partial }{ \rightarrow  }{C}_{n - 1} \rightarrow  \cdots
\]

To dualize this complex we replace each chain group \( {C}_{n} \) by its dual cochain group \( {C}_{n}^{ * } = \operatorname{Hom}\left( {{C}_{n}, G}\right) \) , the group of homomorphisms \( {C}_{n} \rightarrow  G \) , and we replace each boundary map \( \partial  : {C}_{n} \rightarrow  {C}_{n - 1} \) by its dual coboundary map \( \delta  = {\partial }^{ * } : {C}_{n - 1}^{ * } \rightarrow  {C}_{n}^{ * } \) . The reason why \( \delta \) goes in the opposite direction from \( \partial \) , increasing rather than decreasing dimension, is purely formal: For a homomorphism \( \alpha  : A \rightarrow  B \) , the dual homomorphism \( {\alpha }^{ * } : \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right) \) is defined by \( {\alpha }^{ * }\left( \varphi \right)  = {\varphi \alpha } \) , so \( {\alpha }^{ * } \) sends \( B\overset{\varphi }{ \rightarrow  }G \) to the composition \( A\overset{\alpha }{ \rightarrow  }B\overset{\varphi }{ \rightarrow  }G \) . Dual homomorphisms obviously satisfy \( {\left( \alpha \beta \right) }^{ * } = {\beta }^{ * }{\alpha }^{ * } \) , \( {\mathbb{1}}^{ * } = \mathbb{1} \) , and \( {0}^{ * } = 0 \) . In particular, since \( \partial \partial  = 0 \) it follows that \( {\delta \delta } = 0 \) , and the cohomology group \( {H}^{n}\left( {C;G}\right) \) can be defined as the ’homology group’ Ker \( \delta /\operatorname{Im}\delta \) at \( {C}_{n}^{ * } \) in the cochain complex

\[
\cdots  \leftarrow  {C}_{n + 1}^{ * } \leftarrow  {C}_{n}^{ * } \leftarrow  {C}_{n - 1}^{ * } \leftarrow  \cdots
\]

Our goal is to show that the cohomology groups \( {H}^{n}\left( {C;G}\right) \) are determined solely by \( G \) and the homology groups \( {H}_{n}\left( C\right)  = \operatorname{Ker}\partial /\operatorname{Im}\partial \) . A first guess might be that \( {H}^{n}\left( {C;G}\right) \) is isomorphic to \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) , but this is overly optimistic, as shown by the example above where \( {H}_{2} \) was zero while \( {H}^{2} \) was nonzero. Nevertheless, there is a natural map \( h : {H}^{n}\left( {C;G}\right)  \rightarrow  \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) , defined as follows. Denote the cycles and boundaries by \( {Z}_{n} = \operatorname{Ker}\partial  \subset  {C}_{n} \) and \( {B}_{n} = \operatorname{Im}\partial  \subset  {C}_{n} \) . A class in \( {H}^{n}\left( {C;G}\right) \) is represented by a homomorphism \( \varphi  : {C}_{n} \rightarrow  G \) such that \( {\delta \varphi } = 0 \) , that is, \( \varphi \partial  = 0 \) , or in other words, \( \varphi \) vanishes on \( {B}_{n} \) . The restriction \( {\varphi }_{0} = \varphi  \mid  {Z}_{n} \) then induces a quotient homomorphism \( {\overline{\varphi }}_{0} : {Z}_{n}/{B}_{n} \rightarrow  G \) , an element of \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) . If \( \varphi \) is in \( \operatorname{Im}\delta \) , say \( \varphi  = {\delta \psi } = \psi \partial \) , then \( \varphi \) is zero on \( {Z}_{n} \) , so \( {\varphi }_{0} = 0 \) and hence also \( {\overline{\varphi }}_{0} = 0 \) . Thus there is a well-defined quotient map \( h : {H}^{n}\left( {C;G}\right)  \rightarrow  \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) sending the cohomology class of \( \varphi \) to \( {\overline{\varphi }}_{0} \) . Obviously \( h \) is a homomorphism.

It is not hard to see that \( h \) is surjective. The short exact sequence

\[
0 \rightarrow  {Z}_{n} \rightarrow  {C}_{n}\overset{\partial }{ \rightarrow  }{B}_{n - 1} \rightarrow  0
\]

splits since \( {B}_{n - 1} \) is free, being a subgroup of the free abelian group \( {C}_{n - 1} \) . Thus there is a projection homomorphism \( p : {C}_{n} \rightarrow  {Z}_{n} \) that restricts to the identity on \( {Z}_{n} \) . Composing with \( p \) gives a way of extending homomorphisms \( {\varphi }_{0} : {Z}_{n} \rightarrow  G \) to homomorphisms \( \varphi  = {\varphi }_{0}p : {C}_{n} \rightarrow  G \) . In particular, this extends homomorphisms \( {Z}_{n} \rightarrow  G \) that vanish on \( {B}_{n} \) to homomorphisms \( {C}_{n} \rightarrow  G \) that still vanish on \( {B}_{n} \) , or in other words, it extends homomorphisms \( {H}_{n}\left( C\right)  \rightarrow  G \) to elements of \( \operatorname{Ker}\delta \) . Thus we have a homomorphism \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  \operatorname{Ker}\delta \) . Composing this with the quotient map \( \operatorname{Ker}\delta  \rightarrow  {H}^{n}\left( {C;G}\right) \) gives a homomorphism from \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) to \( {H}^{n}\left( {C;G}\right) \) . If we follow this map by \( h \) we get the identity map on \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) since the effect of composing with \( h \) is simply to undo the effect of extending homomorphisms via \( p \) . This shows that \( h \) is surjective. In fact it shows that we have a split short exact sequence

\[
0 \rightarrow  \operatorname{Ker}h \rightarrow  {H}^{n}\left( {C;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  0
\]

The remaining task is to analyze Ker \( h \) . A convenient way to start the process is to consider not just the chain complex \( C \) , but also its subcomplexes consisting of the cycles and the boundaries. Thus we consider the commutative diagram of short exact sequences(i)

![bo_d7dtv0s91nqc73eq8nv0_200_512_632_715_169_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_200_512_632_715_169_0.jpg)

where the vertical boundary maps on \( {Z}_{n + 1} \) and \( {B}_{n} \) are the restrictions of the boundary map in the complex \( C \) , hence are zero. Dualizing (i) gives a commutative diagram(ii)

![bo_d7dtv0s91nqc73eq8nv0_200_516_930_709_160_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_200_516_930_709_160_0.jpg)

The rows here are exact since, as we have already remarked, the rows of (i) split, and the dual of a split short exact sequence is a split short exact sequence because of the natural isomorphism \( \operatorname{Hom}\left( {A \oplus  B, G}\right)  \approx  \operatorname{Hom}\left( {A, G}\right)  \oplus  \operatorname{Hom}\left( {B, G}\right) \) .

We may view (ii), like (i), as part of a short exact sequence of chain complexes. Since the coboundary maps in the \( {Z}_{n}^{ * } \) and \( {B}_{n}^{ * } \) complexes are zero, the associated long exact sequence of homology groups has the form

(iii)

\[
\cdots  \leftarrow  {B}_{n}^{ * } \leftarrow  {Z}_{n}^{ * } \leftarrow  {H}^{n}\left( {C;G}\right)  \leftarrow  {B}_{n - 1}^{ * } \leftarrow  {Z}_{n - 1}^{ * } \leftarrow  \cdots
\]

The ’boundary maps’ \( {Z}_{n}^{ * } \rightarrow  {B}_{n}^{ * } \) in this long exact sequence are in fact the dual maps \( {i}_{n}^{ * } \) of the inclusions \( {i}_{n} : {B}_{n} \rightarrow  {Z}_{n} \) , as one sees by recalling how these boundary maps are defined: In (ii) one takes an element of \( {Z}_{n}^{ * } \) , pulls this back to \( {C}_{n}^{ * } \) , applies \( \delta \) to get an element of \( {C}_{n + 1}^{ * } \) , then pulls this back to \( {B}_{n}^{ * } \) . The first of these steps extends a homomorphism \( {\varphi }_{0} : {Z}_{n} \rightarrow  G \) to \( \varphi  : {C}_{n} \rightarrow  G \) , the second step composes this \( \varphi \) with \( \partial \) , and the third step undoes this composition and restricts \( \varphi \) to \( {B}_{n} \) . The net effect is just to restrict \( {\varphi }_{0} \) from \( {Z}_{n} \) to \( {B}_{n} \) .

A long exact sequence can always be broken up into short exact sequences, and doing this for the sequence (iii) yields short exact sequences

(iv)

\[
0 \leftarrow  \operatorname{Ker}{i}_{n}^{ * } \leftarrow  {H}^{n}\left( {C;G}\right)  \leftarrow  \text{ Coker }{i}_{n - 1}^{ * } \leftarrow  0
\]

The group \( \operatorname{Ker}{i}_{n}^{ * } \) can be identified naturally with \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) since elements of Ker \( {i}_{n}^{ * } \) are homomorphisms \( {Z}_{n} \rightarrow  G \) that vanish on the subgroup \( {B}_{n} \) , and such homomorphisms are the same as homomorphisms \( {Z}_{n}/{B}_{n} \rightarrow  G \) . Under this identification of

Ker \( {i}_{n}^{ * } \) with \( \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) , the map \( {H}^{n}\left( {C;G}\right)  \rightarrow  \operatorname{Ker}{i}_{n}^{ * } \) in (iv) becomes the map \( h \) considered earlier. Thus we can rewrite (iv) as a split short exact sequence

(v)

\[
0 \rightarrow  \text{ Coker }{i}_{n - 1}^{ * } \rightarrow  {H}^{n}\left( {C;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  0
\]

Our objective now is to show that the more mysterious term Coker \( {i}_{n - 1}^{ * } \) depends only on \( {H}_{n - 1}\left( C\right) \) and \( G \) , in a natural, functorial way. First let us observe that Coker \( {i}_{n - 1}^{ * } \) would be zero if it were always true that the dual of a short exact sequence was exact, since the dual of the short exact sequence

(vi)

\[
0 \rightarrow  {B}_{n - 1}\xrightarrow[]{{i}_{n - 1}}{Z}_{n - 1} \rightarrow  {H}_{n - 1}\left( C\right)  \rightarrow  0
\]

is the sequence

(vii)

\[
0 \leftarrow  {B}_{n - 1}^{ * }\overset{{i}_{n - 1}^{ * }}{ \leftarrow  }{Z}_{n - 1}^{ * } \leftarrow  {H}_{n - 1}{\left( C\right) }^{ * } \leftarrow  0
\]

and if this were exact at \( {B}_{n - 1}^{ * } \) , then \( {i}_{n - 1}^{ * } \) would be surjective, hence Coker \( {i}_{n - 1}^{ * } \) would be zero. This argument does apply if \( {H}_{n - 1}\left( C\right) \) happens to be free, since (vi) splits in this case, which implies that (vii) is also split exact. So in this case the map \( h \) in (v) is an isomorphism. However, in the general case it is easy to find short exact sequences whose duals are not exact. For example, if we dualize \( 0 \rightarrow  \mathbb{Z}\overset{n}{ \rightarrow  }\mathbb{Z} \rightarrow  {\mathbb{Z}}_{n} \rightarrow  0 \) by applying \( \operatorname{Hom}\left( {-,\mathbb{Z}}\right) \) we get \( 0 \leftarrow  \mathbb{Z}\overset{n}{ \leftarrow  }\mathbb{Z} \leftarrow  0 \leftarrow  0 \) which fails to be exact at the left-hand \( \mathbb{Z} \) , precisely the place we are interested in for Coker \( {i}_{n - 1}^{ * } \) .

We might mention in passing that the loss of exactness at the left end of a short exact sequence after dualization is in fact all that goes wrong, in view of the following:

Exercise. If \( A \rightarrow  B \rightarrow  C \rightarrow  0 \) is exact, then dualizing by applying \( \operatorname{Hom}\left( {-, G}\right) \) yields an exact sequence \( {A}^{ * } \leftarrow  {B}^{ * } \leftarrow  {C}^{ * } \leftarrow  0 \) .

However, we will not need this fact in what follows.

The exact sequence (vi) has the special feature that both \( {B}_{n - 1} \) and \( {Z}_{n - 1} \) are free, so (vi) can be regarded as a free resolution of \( {H}_{n - 1}\left( C\right) \) , where a free resolution of an abelian group \( H \) is an exact sequence

\[
\cdots  \rightarrow  {F}_{2}\overset{{f}_{2}}{ \rightarrow  }{F}_{1}\overset{{f}_{1}}{ \rightarrow  }{F}_{0}\overset{{f}_{0}}{ \rightarrow  }H \rightarrow  0
\]

with each \( {F}_{n} \) free. If we dualize this free resolution by applying \( \operatorname{Hom}\left( {-, G}\right) \) , we may lose exactness, but at least we get a chain complex - or perhaps we should say 'cochain complex', but algebraically there is no difference. This dual complex has the form

\[
\cdots  \leftarrow  {F}_{2}^{ * }\overset{{f}_{2}^{ * }}{ \leftarrow  }{F}_{1}^{ * }\overset{{f}_{1}^{ * }}{ \leftarrow  }{F}_{0}^{ * }\overset{{f}_{0}^{ * }}{ \leftarrow  }{H}^{ * } \leftarrow  0
\]

Let us use the temporary notation \( {H}^{n}\left( {F;G}\right) \) for the homology group Ker \( {f}_{n + 1}^{ * }/\operatorname{Im}{f}_{n}^{ * } \) of this dual complex. Note that the group Coker \( {i}_{n - 1}^{ * } \) that we are interested in is \( {H}^{1}\left( {F;G}\right) \) where \( F \) is the free resolution in (vi). Part (b) of the following lemma therefore shows that Coker \( {i}_{n - 1}^{ * } \) depends only on \( {H}_{n - 1}\left( C\right) \) and \( G \) .

Lemma 3.1. (a) Given free resolutions \( F \) and \( {F}^{\prime } \) of abelian groups \( H \) and \( {H}^{\prime } \) , then every homomorphism \( \alpha  : H \rightarrow  {H}^{\prime } \) can be extended to a chain map from \( F \) to \( {F}^{\prime } \) :

![bo_d7dtv0s91nqc73eq8nv0_202_529_252_742_177_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_202_529_252_742_177_0.jpg)

Furthermore, any two such chain maps extending \( \alpha \) are chain homotopic.

(b) For any two free resolutions \( F \) and \( {F}^{\prime } \) of \( H \) , there are canonical isomorphisms \( {H}^{n}\left( {F;G}\right)  \approx  {H}^{n}\left( {{F}^{\prime };G}\right) \) for all \( n. \)

Proof: The \( {\alpha }_{i} \) ’s will be constructed inductively. Since the \( {F}_{i} \) ’s are free, it suffices to define each \( {\alpha }_{i} \) on a basis for \( {F}_{i} \) . To define \( {\alpha }_{0} \) , observe that surjectivity of \( {f}_{0}^{\prime } \) implies that for each basis element \( x \) of \( {F}_{0} \) there exists \( {x}^{\prime } \in  {F}_{0}^{\prime } \) such that \( {f}_{0}^{\prime }\left( {x}^{\prime }\right)  = \alpha {f}_{0}\left( x\right) \) , so we define \( {\alpha }_{0}\left( x\right)  = {x}^{\prime } \) . We would like to define \( {\alpha }_{1} \) in the same way, sending a basis element \( x \in  {F}_{1} \) to an element \( {x}^{\prime } \in  {F}_{1}^{\prime } \) such that \( {f}_{1}^{\prime }\left( {x}^{\prime }\right)  = {\alpha }_{0}{f}_{1}\left( x\right) \) . Such an \( {x}^{\prime } \) will exist if \( {\alpha }_{0}{f}_{1}\left( x\right) \) lies in \( \operatorname{Im}{f}_{1}^{\prime } = \operatorname{Ker}{f}_{0}^{\prime } \) , which it does since \( {f}_{0}^{\prime }{\alpha }_{0}{f}_{1} = \alpha {f}_{0}{f}_{1} = 0 \) . The same procedure defines all the subsequent \( {\alpha }_{i} \) ’s.

If we have another chain map extending \( \alpha \) given by maps \( {\alpha }_{i}^{\prime } : {F}_{i} \rightarrow  {F}_{i}^{\prime } \) , then the differences \( {\beta }_{i} = {\alpha }_{i} - {\alpha }_{i}^{\prime } \) define a chain map extending the zero map \( \beta  : H \rightarrow  {H}^{\prime } \) . It will suffice to construct maps \( {\lambda }_{i} : {F}_{i} \rightarrow  {F}_{i + 1}^{\prime } \) defining a chain homotopy from \( {\beta }_{i} \) to 0, that is, with \( {\beta }_{i} = {f}_{i + 1}^{\prime }{\lambda }_{i} + {\lambda }_{i - 1}{f}_{i} \) . The \( {\lambda }_{i} \) ’s are constructed inductively by a procedure much like the construction of the \( {\alpha }_{i} \) ’s. When \( i = 0 \) we let \( {\lambda }_{-1} : H \rightarrow  {F}_{0}^{\prime } \) be zero, and then the desired relation becomes \( {\beta }_{0} = {f}_{1}^{\prime }{\lambda }_{0} \) . We can achieve this by letting \( {\lambda }_{0} \) send a basis element \( x \) to an element \( {x}^{\prime } \in  {F}_{1}^{\prime } \) such that \( {f}_{1}^{\prime }\left( {x}^{\prime }\right)  = {\beta }_{0}\left( x\right) \) . Such an \( {x}^{\prime } \) exists since \( \operatorname{Im}{f}_{1}^{\prime } = \operatorname{Ker}{f}_{0}^{\prime } \) and \( {f}_{0}^{\prime }{\beta }_{0}\left( x\right)  = \beta {f}_{0}\left( x\right)  = 0 \) . For the inductive step we wish to define \( {\lambda }_{i} \) to take a basis element \( x \in  {F}_{i} \) to an element \( {x}^{\prime } \in  {F}_{i + 1}^{\prime } \) such that \( {f}_{i + 1}^{\prime }\left( {x}^{\prime }\right)  = {\beta }_{i}\left( x\right)  - {\lambda }_{i - 1}{f}_{i}\left( x\right) \) . This will be possible if \( {\beta }_{i}\left( x\right)  - {\lambda }_{i - 1}{f}_{i}\left( x\right) \) lies in \( \operatorname{Im}{f}_{i + 1}^{\prime } = \operatorname{Ker}{f}_{i}^{\prime } \) , which will hold if \( {f}_{i}^{\prime }\left( {{\beta }_{i} - {\lambda }_{i - 1}{f}_{i}}\right)  = 0 \) . Using the relation \( {f}_{i}^{\prime }{\beta }_{i} = {\beta }_{i - 1}{f}_{i} \) and the relation \( {\beta }_{i - 1} = {f}_{i}^{\prime }{\lambda }_{i - 1} + {\lambda }_{i - 2}{f}_{i - 1} \) which holds by induction, we have

\[
{f}_{i}^{\prime }\left( {{\beta }_{i} - {\lambda }_{i - 1}{f}_{i}}\right)  = {f}_{i}^{\prime }{\beta }_{i} - {f}_{i}^{\prime }{\lambda }_{i - 1}{f}_{i}
\]

\[
= {\beta }_{i - 1}{f}_{i} - {f}_{i}^{\prime }{\lambda }_{i - 1}{f}_{i} = \left( {{\beta }_{i - 1} - {f}_{i}^{\prime }{\lambda }_{i - 1}}\right) {f}_{i} = {\lambda }_{i - 2}{f}_{i - 1}{f}_{i} = 0
\]

as desired. This finishes the proof of (a).

The maps \( {\alpha }_{n} \) constructed in (a) dualize to maps \( {\alpha }_{n}^{ * } : {F}_{n}^{\prime  * } \rightarrow  {F}_{n}^{ * } \) forming a chain map between the dual complexes \( {F}^{\prime  * } \) and \( {F}^{ * } \) . Therefore we have induced homomorphisms on cohomology \( {\alpha }^{ * } : {H}^{n}\left( {{F}^{\prime };G}\right)  \rightarrow  {H}^{n}\left( {F;G}\right) \) . These do not depend on the choice of \( {\alpha }_{n} \) ’s since any other choices \( {\alpha }_{n}^{\prime } \) are chain homotopic, say via chain homotopies \( {\lambda }_{n} \) , and then \( {\alpha }_{n}^{ * } \) and \( {\alpha }_{n}^{\prime  * } \) are chain homotopic via the dual maps \( {\lambda }_{n}^{ * } \) since the dual of the relation \( {\alpha }_{i} - {\alpha }_{i}^{\prime } = {f}_{i + 1}^{\prime }{\lambda }_{i} + {\lambda }_{i - 1}{f}_{i} \) is \( {\alpha }_{i}^{ * } - {\alpha }_{i}^{\prime  * } = {\lambda }_{i}^{ * }{f}_{i + 1}^{\prime  * } + {f}_{i}^{ * }{\lambda }_{i - 1}^{ * } \) .

The induced homomorphisms \( {\alpha }^{ * } : {H}^{n}\left( {{F}^{\prime };G}\right)  \rightarrow  {H}^{n}\left( {F;G}\right) \) satisfy \( {\left( \beta \alpha \right) }^{ * } = {\alpha }^{ * }{\beta }^{ * } \) for a composition \( H\overset{\alpha }{ \rightarrow  }{H}^{\prime }\overset{\beta }{ \rightarrow  }{H}^{\prime \prime } \) with a free resolution \( {F}^{\prime \prime } \) of \( {H}^{\prime \prime } \) also given, since one can choose the compositions \( {\beta }_{n}{\alpha }_{n} \) of extensions \( {\alpha }_{n} \) of \( \alpha \) and \( {\beta }_{n} \) of \( \beta \) as an extension of \( {\beta \alpha } \) . In particular, if we take \( \alpha \) to be an isomorphism and \( \beta \) to be its inverse, with \( {F}^{\prime \prime } = F \) , then \( {\alpha }^{ * }{\beta }^{ * } = {\left( \beta \alpha \right) }^{ * } = \mathbb{1} \) , the latter equality coming from the obvious extension of \( \mathbb{1} : H \rightarrow  H \) by the identity map of \( F \) . The same reasoning shows \( {\beta }^{ * }{\alpha }^{ * } = \mathbb{1} \) , so \( {\alpha }^{ * } \) is an isomorphism. Finally, if we specialize further, taking \( \alpha \) to be the identity but with two different free resolutions \( F \) and \( {F}^{\prime } \) , we get a canonical isomorphism \( {\mathbb{1}}^{ * } : {H}^{n}\left( {{F}^{\prime };G}\right)  \rightarrow  {H}^{n}\left( {F;G}\right) \) .

Every abelian group \( H \) has a free resolution of the form \( 0 \rightarrow  {F}_{1} \rightarrow  {F}_{0} \rightarrow  H \rightarrow  0 \) , with \( {F}_{i} = 0 \) for \( i > 1 \) , obtainable in the following way. Choose a set of generators for \( H \) and let \( {F}_{0} \) be a free abelian group with basis in one-to-one correspondence with these generators. Then we have a surjective homomorphism \( {f}_{0} : {F}_{0} \rightarrow  H \) sending the basis elements to the chosen generators. The kernel of \( {f}_{0} \) is free, being a subgroup of a free abelian group, so we can let \( {F}_{1} \) be this kernel with \( {f}_{1} : {F}_{1} \rightarrow  {F}_{0} \) the inclusion, and we can then take \( {F}_{i} = 0 \) for \( i > 1 \) . For this free resolution we obviously have \( {H}^{n}\left( {F;G}\right)  = 0 \) for \( n > 1 \) , so this must also be true for all free resolutions. Thus the only interesting group \( {H}^{n}\left( {F;G}\right) \) is \( {H}^{1}\left( {F;G}\right) \) . As we have seen, this group depends only on \( H \) and \( G \) , and the standard notation for it is \( \operatorname{Ext}\left( {H, G}\right) \) . This notation arises from the fact that \( \operatorname{Ext}\left( {H, G}\right) \) has an interpretation as the set of isomorphism classes of extensions of \( G \) by \( H \) , that is, short exact sequences \( 0 \rightarrow  G \rightarrow  J \rightarrow  H \rightarrow  0 \) , with a natural definition of isomorphism between such exact sequences. This is explained in books on homological algebra, for example [Brown 1982], [Hilton & Stammbach 1970], or [MacLane 1963]. However, this interpretation of \( \operatorname{Ext}\left( {H, G}\right) \) is rarely needed in algebraic topology.

Summarizing, we have established the following algebraic result:

Theorem 3.2. If a chain complex \( C \) of free abelian groups has homology groups \( {H}_{n}\left( C\right) \) , then the cohomology groups \( {H}^{n}\left( {C;G}\right) \) of the cochain complex \( \operatorname{Hom}\left( {{C}_{n}, G}\right) \) are determined by split exact sequences

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( C\right) , G}\right)  \rightarrow  {H}^{n}\left( {C;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  0
\]

This is known as the universal coefficient theorem for cohomology because it is formally analogous to the universal coefficient theorem for homology in §3.A which expresses homology with arbitrary coefficients in terms of homology with \( \mathbb{Z} \) coefficients.

Computing \( \operatorname{Ext}\left( {H, G}\right) \) for finitely generated \( H \) is not difficult using the following three properties:

- \( \operatorname{Ext}\left( {H \oplus  {H}^{\prime }, G}\right)  \approx  \operatorname{Ext}\left( {H, G}\right)  \oplus  \operatorname{Ext}\left( {{H}^{\prime }, G}\right) \) .

- \( \operatorname{Ext}\left( {H, G}\right)  = 0 \) if \( H \) is free.

- \( \operatorname{Ext}\left( {{\mathbb{Z}}_{n}, G}\right)  \approx  G/{nG} \) .

The first of these can be obtained by using the direct sum of free resolutions of \( H \) and \( {H}^{\prime } \) as a free resolution for \( H \oplus  {H}^{\prime } \) . If \( H \) is free, the free resolution \( 0 \rightarrow  H \rightarrow  H \rightarrow  0 \) yields the second property, while the third comes from dualizing the free resolution \( 0 \rightarrow  \mathbb{Z}\overset{n}{ \rightarrow  }\mathbb{Z} \rightarrow  {\mathbb{Z}}_{n} \rightarrow  0 \) to produce an exact sequence

\[
0 \leftarrow  \operatorname{Ext}\left( {{\mathbb{Z}}_{n}, G}\right)  \leftarrow  \operatorname{Hom}\left( {\mathbb{Z}, G}\right)  \leftarrow  \operatorname{Hom}\left( {\mathbb{Z}, G}\right)  \leftarrow  \operatorname{Hom}\left( {{\mathbb{Z}}_{n}, G}\right)  \leftarrow  0
\]

\[
G/{nG} \leftarrow  G \leftarrow  {nG}
\]

In particular, these three properties imply that \( \operatorname{Ext}\left( {H,\mathbb{Z}}\right) \) is isomorphic to the torsion subgroup of \( H \) if \( H \) is finitely generated. Since \( \operatorname{Hom}\left( {H,\mathbb{Z}}\right) \) is isomorphic to the free part of \( H \) if \( H \) is finitely generated, we have:

Corollary 3.3. If the homology groups \( {H}_{n} \) and \( {H}_{n - 1} \) of a chain complex \( C \) of free abelian groups are finitely generated, with torsion subgroups \( {T}_{n} \subset  {H}_{n} \) and \( {T}_{n - 1} \subset  {H}_{n - 1} \) , then \( {H}^{n}\left( {C;\mathbb{Z}}\right)  \approx  \left( {{H}_{n}/{T}_{n}}\right)  \oplus  {T}_{n - 1} \) .

It is useful in many situations to know that the short exact sequences in the universal coefficient theorem are natural, meaning that a chain map \( \alpha \) between chain complexes \( C \) and \( {C}^{\prime } \) of free abelian groups induces a commutative diagram

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( C\right) , G}\right)  \rightarrow  {H}^{n}\left( {C;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  0
\]

\[
\uparrow  {\left( {\alpha }_{ * }\right) }^{ * }\; \uparrow  {\alpha }^{ * }
\]

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( {C}^{\prime }\right) , G}\right)  \rightarrow  {H}^{n}\left( {{C}^{\prime };G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( {C}^{\prime }\right) , G}\right)  \rightarrow  0
\]

This is apparent if one just thinks about the construction; one obviously obtains a map between the short exact sequences (iv) containing Ker \( {i}_{n}^{ * } \) and Coker \( {i}_{n - 1}^{ * } \) , the identification Ker \( {i}_{n}^{ * } = \operatorname{Hom}\left( {{H}_{n}\left( C\right) , G}\right) \) is certainly natural, and the proof of Lemma 3.1 shows that \( \operatorname{Ext}\left( {H, G}\right) \) depends naturally on \( H \) .

However, the splitting in the universal coefficient theorem is not natural since it depends on the choice of the projections \( p : {C}_{n} \rightarrow  {Z}_{n} \) . An exercise at the end of the section gives a topological example showing that the splitting in fact cannot be natural.

The naturality property together with the five-lemma proves:

Corollary 3.4. If a chain map between chain complexes of free abelian groups induces an isomorphism on homology groups, then it induces an isomorphism on cohomology groups with any coefficient group \( G \) .

One could attempt to generalize the algebraic machinery of the universal coefficient theorem by replacing abelian groups by modules over a chosen ring \( R \) and Hom by \( {\operatorname{Hom}}_{R} \) , the \( R \) -module homomorphisms. The key fact about abelian groups that was needed was that subgroups of free abelian groups are free. Submodules of free \( R \) -modules are free if \( R \) is a principal ideal domain, so in this case the generalization is automatic. One obtains natural split short exact sequences

\[
0 \rightarrow  {\operatorname{Ext}}_{R}\left( {{H}_{n - 1}\left( C\right) , G}\right)  \rightarrow  {H}^{n}\left( {C;G}\right) \overset{h}{ \rightarrow  }{\operatorname{Hom}}_{R}\left( {{H}_{n}\left( C\right) , G}\right)  \rightarrow  0
\]

where \( C \) is a chain complex of free \( R \) -modules with boundary maps \( R \) -module homomorphisms, and the coefficient group \( G \) is also an \( R \) -module. If \( R \) is a field, for example, then \( R \) -modules are always free and so the \( {\operatorname{Ext}}_{R} \) term is always zero since we may choose free resolutions of the form \( 0 \rightarrow  {F}_{0} \rightarrow  H \rightarrow  0 \) .

It is interesting to note that the proof of Lemma 3.1 on the uniqueness of free resolutions is valid for modules over an arbitrary ring \( R \) . Moreover, every \( R \) -module \( H \) has a free resolution, which can be constructed in the following way. Choose a set of generators for \( H \) as an \( R \) -module, and let \( {F}_{0} \) be a free \( R \) -module with basis in one-toone correspondence with these generators. Thus we have a surjective homomorphism \( {f}_{0} : {F}_{0} \rightarrow  H \) sending the basis elements to the chosen generators. Now repeat the process with \( \operatorname{Ker}{f}_{0} \) in place of \( H \) , constructing a homomorphism \( {f}_{1} : {F}_{1} \rightarrow  {F}_{0} \) sending a basis for a free \( R \) -module \( {F}_{1} \) onto generators for \( \operatorname{Ker}{f}_{0} \) . And inductively, construct \( {f}_{n} : {F}_{n} \rightarrow  {F}_{n - 1} \) with image equal to \( \operatorname{Ker}{f}_{n - 1} \) by the same procedure.

By Lemma 3.1 the groups \( {H}^{n}\left( {F;G}\right) \) depend only on \( H \) and \( G \) , not on the free resolution \( F \) . The standard notation for \( {H}^{n}\left( {F;G}\right) \) is \( {\operatorname{Ext}}_{R}^{n}\left( {H, G}\right) \) . For sufficiently complicated rings \( R \) the groups \( {\operatorname{Ext}}_{R}^{n}\left( {H, G}\right) \) can be nonzero for \( n > 1 \) . In certain more advanced topics in algebraic topology these \( {\operatorname{Ext}}_{R}^{n} \) groups play an essential role.

A final remark about the definition of \( {\operatorname{Ext}}_{R}^{n}\left( {H, G}\right) \) : By the Exercise stated earlier, exactness of \( {F}_{1} \rightarrow  {F}_{0} \rightarrow  H \rightarrow  0 \) implies exactness of \( {F}_{1}^{ * } \leftarrow  {F}_{0}^{ * } \leftarrow  {H}^{ * } \leftarrow  0 \) . This means that \( {H}^{0}\left( {F;G}\right) \) as defined above is zero. Rather than having \( {\operatorname{Ext}}_{R}^{0}\left( {H, G}\right) \) be automatically zero, it is better to define \( {H}^{n}\left( {F;G}\right) \) as the \( {n}^{th} \) homology group of the complex \( \cdots  \leftarrow  {F}_{1}^{ * } \leftarrow  {F}_{0}^{ * } \leftarrow  0 \) with the term \( {H}^{ * } \) omitted. This can be viewed as defining the groups \( {H}^{n}\left( {F;G}\right) \) to be unreduced cohomology groups. With this slightly modified definition we have \( {\operatorname{Ext}}_{R}^{0}\left( {H, G}\right)  = {H}^{0}\left( {F;G}\right)  = {H}^{ * } = {\operatorname{Hom}}_{R}\left( {H, G}\right) \) by the exactness of \( {F}_{1}^{ * } \leftarrow  {F}_{0}^{ * } \leftarrow  {H}^{ * } \leftarrow  0 \) . The real reason why unreduced Ext groups are better than reduced groups is perhaps to be found in certain exact sequences involving Ext and Hom derived in §3.F, which would not work with the Hom terms replaced by zeros.

## Cohomology of Spaces

Now we return to topology. Given a space \( X \) and an abelian group \( G \) , we define the group \( {C}^{n}\left( {X;G}\right) \) of singular \( n \) -cochains with coefficients in \( G \) to be the dual group \( \operatorname{Hom}\left( {{C}_{n}\left( X\right) , G}\right) \) of the singular chain group \( {C}_{n}\left( X\right) \) . Thus an \( n \) -cochain \( \varphi  \in  {C}^{n}\left( {X;G}\right) \) assigns to each singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) a value \( \varphi \left( \sigma \right)  \in  G \) . Since the singular \( n \) -simplices form a basis for \( {C}_{n}\left( X\right) \) , these values can be chosen arbitrarily, hence \( n \) -cochains are exactly equivalent to functions from singular \( n \) -simplices to \( G \) .

The coboundary map \( \delta  : {C}^{n}\left( {X;G}\right)  \rightarrow  {C}^{n + 1}\left( {X;G}\right) \) is the dual \( {\partial }^{ * } \) , so for a cochain \( \varphi  \in  {C}^{n}\left( {X;G}\right) \) , its coboundary \( {\delta \varphi } \) is the composition \( {C}_{n + 1}\left( X\right) \overset{\partial }{ \rightarrow  }{C}_{n}\left( X\right) \overset{\varphi }{ \rightarrow  }G \) . This means that for a singular \( \left( {n + 1}\right) \) -simplex \( \sigma  : {\Delta }^{n + 1} \rightarrow  X \) we have

\[
{\delta \varphi }\left( \sigma \right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\varphi \left( {\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n + 1}}\right\rbrack  }\right)
\]

It is automatic that \( {\delta }^{2} = 0 \) since \( {\delta }^{2} \) is the dual of \( {\partial }^{2} = 0 \) . Therefore we can define the cohomology group \( {H}^{n}\left( {X;G}\right) \) with coefficients in \( G \) to be the quotient \( \operatorname{Ker}\delta /\operatorname{Im}\delta \) at \( {C}^{n}\left( {X;G}\right) \) in the cochain complex

\[
\cdots  \leftarrow  {C}^{n + 1}\left( {X;G}\right) \overset{\delta }{ \leftarrow  }{C}^{n}\left( {X;G}\right) \overset{\delta }{ \leftarrow  }{C}^{n - 1}\left( {X;G}\right)  \leftarrow  \cdots  \leftarrow  {C}^{0}\left( {X;G}\right)  \leftarrow  0
\]

Elements of Ker \( \delta \) are cocycles, and elements of Im \( \delta \) are coboundaries. For a cochain \( \varphi \) to be a cocycle means that \( {\delta \varphi } = \varphi \partial  = 0 \) , or in other words, \( \varphi \) vanishes on boundaries.

Since the chain groups \( {C}_{n}\left( X\right) \) are free, the algebraic universal coefficient theorem takes on the topological guise of split short exact sequences

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( X\right) , G}\right)  \rightarrow  {H}^{n}\left( {X;G}\right)  \rightarrow  \operatorname{Hom}\left( {{H}_{n}\left( X\right) , G}\right)  \rightarrow  0
\]

which describe how cohomology groups with arbitrary coefficients are determined purely algebraically by homology groups with \( \mathbb{Z} \) coefficients. For example, if the homology groups of \( X \) are finitely generated then Corollary 3.3 tells how to compute the cohomology groups \( {H}^{n}\left( {X;\mathbb{Z}}\right) \) from the homology groups.

When \( n = 0 \) there is no Ext term, and the universal coefficient theorem reduces to an isomorphism \( {H}^{0}\left( {X;G}\right)  \approx  \operatorname{Hom}\left( {{H}_{0}\left( X\right) , G}\right) \) . This can also be seen directly from the definitions. Since singular 0-simplices are just points of \( X \) , a cochain in \( {C}^{0}\left( {X;G}\right) \) is an arbitrary function \( \varphi  : X \rightarrow  G \) , not necessarily continuous. For this to be a cocycle means that for each singular 1-simplex \( \sigma  : \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack   \rightarrow  X \) we have \( {\delta \varphi }\left( \sigma \right)  = \varphi \left( {\partial \sigma }\right)  = \; \varphi \left( {\sigma \left( {v}_{1}\right) }\right)  - \varphi \left( {\sigma \left( {v}_{0}\right) }\right)  = 0 \) . This is equivalent to saying that \( \varphi \) is constant on path-components of \( X \) . Thus \( {H}^{0}\left( {X;G}\right) \) is all the functions from path-components of \( X \) to \( G \) . This is the same as \( \operatorname{Hom}\left( {{H}_{0}\left( X\right) , G}\right) \) .

Likewise in the case of \( {H}^{1}\left( {X;G}\right) \) the universal coefficient theorem gives an isomorphism \( {H}^{1}\left( {X;G}\right)  \approx  \operatorname{Hom}\left( {{H}_{1}\left( X\right) , G}\right) \) since \( \operatorname{Ext}\left( {{H}_{0}\left( X\right) , G}\right)  = 0 \) , the group \( {H}_{0}\left( X\right) \) being free. If \( X \) is path-connected, \( {H}_{1}\left( X\right) \) is the abelianization of \( {\pi }_{1}\left( X\right) \) and we can identify \( \operatorname{Hom}\left( {{H}_{1}\left( X\right) , G}\right) \) with \( \operatorname{Hom}\left( {{\pi }_{1}\left( X\right) , G}\right) \) since \( G \) is abelian.

The universal coefficient theorem has a simpler form if we take coefficients in a field \( F \) for both homology and cohomology. In \( \text{ § }{2.2} \) we defined the homology groups \( {H}_{n}\left( {X;F}\right) \) as the homology groups of the chain complex of free \( F \) -modules \( {C}_{n}\left( {X;F}\right) \) , where \( {C}_{n}\left( {X;F}\right) \) has basis the singular \( n \) -simplices in \( X \) . The dual complex \( {\operatorname{Hom}}_{F}\left( {{C}_{n}\left( {X;F}\right) , F}\right) \) of \( F \) -module homomorphisms is the same as \( \operatorname{Hom}\left( {{C}_{n}\left( X\right) , F}\right) \) since both can be identified with the functions from singular \( n \) -simplices to \( F \) . Hence the homology groups of the dual complex \( {\operatorname{Hom}}_{F}\left( {{C}_{n}\left( {X;F}\right) , F}\right) \) are the cohomology groups \( {H}^{n}\left( {X;F}\right) \) . In the generalization of the universal coefficient theorem to the case of modules over a principal ideal domain, the \( {\operatorname{Ext}}_{F} \) terms vanish since \( F \) is a field, so we obtain isomorphisms

\[
{H}^{n}\left( {X;F}\right)  \approx  {\operatorname{Hom}}_{F}\left( {{H}_{n}\left( {X;F}\right) , F}\right)
\]

Thus, with field coefficients, cohomology is the exact dual of homology. Note that when \( F = {\mathbb{Z}}_{p} \) or \( \mathbb{Q} \) we have \( {\operatorname{Hom}}_{F}\left( {H, G}\right)  = \operatorname{Hom}\left( {H, G}\right) \) , the group homomorphisms, for arbitrary \( F \) -modules \( G \) and \( H \) .

For the remainder of this section we will go through the main features of singular homology and check that they extend without much difficulty to cohomology.

Reduced Groups. Reduced cohomology groups \( {\widetilde{H}}^{n}\left( {X;G}\right) \) can be defined by dualizing the augmented chain complex \( \cdots  \rightarrow  {C}_{0}\left( X\right) \overset{\varepsilon }{ \rightarrow  }\mathbb{Z} \rightarrow  0 \) , then taking Ker/ Im. As with homology, this gives \( {\widetilde{H}}^{n}\left( {X;G}\right)  = {H}^{n}\left( {X;G}\right) \) for \( n > 0 \) , and the universal coefficient theorem identifies \( {\widetilde{H}}^{0}\left( {X;G}\right) \) with \( \operatorname{Hom}\left( {{\widetilde{H}}_{0}\left( X\right) , G}\right) \) . We can describe the difference between \( {\widetilde{H}}^{0}\left( {X;G}\right) \) and \( {H}^{0}\left( {X;G}\right) \) more explicitly by using the interpretation of \( {H}^{0}\left( {X;G}\right) \) as functions \( X \rightarrow  G \) that are constant on path-components. Recall that the augmentation map \( \varepsilon  : {C}_{0}\left( X\right)  \rightarrow  \mathbb{Z} \) sends each singular 0 - simplex \( \sigma \) to 1, so the dual map \( {\varepsilon }^{ * } \) sends a homomorphism \( \varphi  : \mathbb{Z} \rightarrow  G \) to the composition \( {C}_{0}\left( X\right) \overset{\varepsilon }{ \rightarrow  }\mathbb{Z}\overset{\varphi }{ \rightarrow  }G \) , which is the function \( \sigma  \mapsto  \varphi \left( 1\right) \) . This is a constant function \( X \rightarrow  G \) , and since \( \varphi \left( 1\right) \) can be any element of \( G \) , the image of \( {\varepsilon }^{ * } \) consists of precisely the constant functions. Thus \( {\widetilde{H}}^{0}\left( {X;G}\right) \) is all functions \( X \rightarrow  G \) that are constant on path-components modulo the functions that are constant on all of \( X \) .

Relative Groups and the Long Exact Sequence of a Pair. To define relative groups \( {H}^{n}\left( {X, A;G}\right) \) for a pair \( \left( {X, A}\right) \) we first dualize the short exact sequence

\[
0 \rightarrow  {C}_{n}\left( A\right) \overset{i}{ \rightarrow  }{C}_{n}\left( X\right) \overset{j}{ \rightarrow  }{C}_{n}\left( {X, A}\right)  \rightarrow  0
\]

by applying \( \operatorname{Hom}\left( {-, G}\right) \) to get

\[
0 \leftarrow  {C}^{n}\left( {A;G}\right) \overset{{i}^{ * }}{ \leftarrow  }{C}^{n}\left( {X;G}\right) \overset{{j}^{ * }}{ \leftarrow  }{C}^{n}\left( {X, A;G}\right)  \leftarrow  0
\]

where by definition \( {C}^{n}\left( {X, A;G}\right)  = \operatorname{Hom}\left( {{C}_{n}\left( {X, A}\right) , G}\right) \) . This sequence is exact by the following direct argument. The map \( {i}^{ * } \) restricts a cochain on \( X \) to a cochain on \( A \) . Thus for a function from singular \( n \) -simplices in \( X \) to \( G \) , the image of this function under \( {i}^{ * } \) is obtained by restricting the domain of the function to singular \( n \) -simplices in \( A \) . Every function from singular \( n \) -simplices in \( A \) to \( G \) can be extended to be defined on all singular \( n \) -simplices in \( X \) , for example by assigning the value 0 to all singular \( n \) -simplices not in \( A \) , so \( {i}^{ * } \) is surjective. The kernel of \( {i}^{ * } \) consists of cochains taking the value 0 on singular \( n \) -simplices in \( A \) . Such cochains are the same as homomorphisms \( {C}_{n}\left( {X, A}\right)  = {C}_{n}\left( X\right) /{C}_{n}\left( A\right)  \rightarrow  G \) , so the kernel of \( {i}^{ * } \) is exactly \( {C}^{n}\left( {X, A;G}\right)  = \operatorname{Hom}\left( {{C}_{n}\left( {X, A}\right) , G}\right) \) , giving the desired exactness. Notice that we can view \( {C}^{n}\left( {X, A;G}\right) \) as the functions from singular \( n \) -simplices in \( X \) to \( G \) that vanish on simplices in \( A \) , since the basis for \( {C}_{n}\left( X\right) \) consisting of singular \( n \) -simplices in \( X \) is the disjoint union of the simplices with image contained in \( A \) and the simplices with image not contained in \( A \) .

Relative coboundary maps \( \delta  : {C}^{n}\left( {X, A;G}\right)  \rightarrow  {C}^{n + 1}\left( {X, A;G}\right) \) are obtained as restrictions of the absolute \( \delta \) ’s, so relative cohomology groups \( {H}^{n}\left( {X, A;G}\right) \) are defined. The fact that the relative cochain group is a subgroup of the absolute cochains, namely the cochains vanishing on chains in \( A \) , means that relative cohomology is conceptually a little simpler than relative homology.

The maps \( {i}^{ * } \) and \( {j}^{ * } \) commute with \( \delta \) since \( i \) and \( j \) commute with \( \partial \) , so the preceding displayed short exact sequence of cochain groups is part of a short exact sequence of cochain complexes, giving rise to an associated long exact sequence of cohomology groups

\[
\cdots  \rightarrow  {H}^{n}\left( {X, A;G}\right) \overset{{j}^{ * }}{ \rightarrow  }{H}^{n}\left( {X;G}\right) \overset{{i}^{ * }}{ \rightarrow  }{H}^{n}\left( {A;G}\right) \overset{\delta }{ \rightarrow  }{H}^{n + 1}\left( {X, A;G}\right)  \rightarrow  \cdots
\]

By similar reasoning one obtains a long exact sequence of reduced cohomology groups for a pair \( \left( {X, A}\right) \) with \( A \) nonempty, where \( {\widetilde{H}}^{n}\left( {X, A;G}\right)  = {H}^{n}\left( {X, A;G}\right) \) for all \( n \) , as in homology. Taking \( A \) to be a point \( {x}_{0} \) , this exact sequence gives an identification of \( {\widetilde{H}}^{n}\left( {X;G}\right) \) with \( {H}^{n}\left( {X,{x}_{0};G}\right) \) .

More generally there is a long exact sequence for a triple \( \left( {X, A, B}\right) \) coming from the short exact sequences

\[
0 \leftarrow  {C}^{n}\left( {A, B;G}\right) \overset{{i}^{ * }}{ \leftarrow  }{C}^{n}\left( {X, B;G}\right) \overset{{j}^{ * }}{ \leftarrow  }{C}^{n}\left( {X, A;G}\right)  \leftarrow  0
\]

The long exact sequence of reduced cohomology can be regarded as the special case that \( B \) is a point.

As one would expect, there is a duality relationship between the connecting homomorphisms \( \delta  : {H}^{n}\left( {A;G}\right)  \rightarrow  {H}^{n + 1}\left( {X, A;G}\right) \) and \( \partial  : {H}_{n + 1}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( A\right) \) . This takes the form of the commutative diagram shown at the right. To verify commutativity, recall how the two connecting homomorphisms are defined, via the

![bo_d7dtv0s91nqc73eq8nv0_208_895_1271_626_120_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_208_895_1271_626_120_0.jpg)

\( \operatorname{Hom}\left( {{H}_{n}\left( A\right) , G}\right) \overset{{\partial }^{ * }}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n + 1}\left( {X, A}\right) , G}\right) \)

diagrams

![bo_d7dtv0s91nqc73eq8nv0_208_231_1491_1335_196_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_208_231_1491_1335_196_0.jpg)

The connecting homomorphisms are represented by the dashed arrows, which are well-defined only when the chain and cochain groups are replaced by homology and cohomology groups. To show that \( {h\delta } = {\partial }^{ * }h \) , start with an element \( \alpha  \in  {H}^{n}\left( {A;G}\right) \) represented by a cocycle \( \varphi  \in  {C}^{n}\left( {A;G}\right) \) . To compute \( \delta \left( \alpha \right) \) we first extend \( \varphi \) to a cochain \( \overline{\varphi } \in  {C}^{n}\left( {X;G}\right) \) , say by letting it take the value 0 on singular simplices not in \( A \) . Then we compose \( \overline{\varphi } \) with \( \partial  : {C}_{n + 1}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) \) to get a cochain \( \overline{\varphi }\partial  \in  {C}^{n + 1}\left( {X;G}\right) \) , which actually lies in \( {C}^{n + 1}\left( {X, A;G}\right) \) since the original \( \varphi \) was a cocycle in \( A \) . This cochain \( \overline{\varphi }\partial  \in  {C}^{n + 1}\left( {X, A;G}\right) \) represents \( \delta \left( \alpha \right) \) in \( {H}^{n + 1}\left( {X, A;G}\right) \) . Now we apply the map \( h \) , which simply restricts the domain of \( \overline{\varphi }\partial \) to relative cycles in \( {C}_{n + 1}\left( {X, A}\right) \) , that is, \( \left( {n + 1}\right) \) -chains in \( X \) whose boundary lies in \( A \) . On such chains we have \( \overline{\varphi }\partial  = \varphi \partial \) since the extension of \( \varphi \) to \( \overline{\varphi } \) is irrelevant. The net result of all this is that \( {h\delta }\left( \alpha \right) \) is represented by \( \varphi \partial \) . Let us compare this with \( {\partial }^{ * }h\left( \alpha \right) \) . Applying \( h \) to \( \varphi \) restricts its domain to cycles in \( A \) . Then applying \( {\partial }^{ * } \) composes with the map which sends a relative \( \left( {n + 1}\right) \) -cycle in \( X \) to its boundary in \( A \) . Thus \( {\partial }^{ * }h\left( \alpha \right) \) is represented by \( \varphi \partial \) just as \( {h\delta }\left( \alpha \right) \) was, and so the square commutes.

Induced Homomorphisms. Dual to the chain maps \( {f}_{\sharp } : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( Y\right) \) induced by \( f : X \rightarrow  Y \) are the cochain maps \( {f}^{\sharp } : {C}^{n}\left( {Y;G}\right)  \rightarrow  {C}^{n}\left( {X;G}\right) \) . The relation \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) dualizes to \( \delta {f}^{\sharp } = {f}^{\sharp }\delta \) , so \( {f}^{\sharp } \) induces homomorphisms \( {f}^{ * } : {H}^{n}\left( {Y;G}\right)  \rightarrow  {H}^{n}\left( {X;G}\right) \) . In the relative case a map \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) induces \( {f}^{ * } : {H}^{n}\left( {Y, B;G}\right)  \rightarrow  {H}^{n}\left( {X, A;G}\right) \) by the same reasoning, and in fact \( f \) induces a map between short exact sequences of cochain complexes, hence a map between long exact sequences of cohomology groups, with commuting squares. The properties \( {\left( fg\right) }^{\sharp } = {g}^{\sharp }{f}^{\sharp } \) and \( {\mathbb{1}}^{\sharp } = \mathbb{1} \) imply \( {\left( fg\right) }^{ * } = \; {g}^{ * }{f}^{ * } \) and \( {\mathbb{1}}^{ * } = \mathbb{1} \) , so \( X \mapsto  {H}^{n}\left( {X;G}\right) \) and \( \left( {X, A}\right)  \mapsto  {H}^{n}\left( {X, A;G}\right) \) are contravariant functors, the 'contra' indicating that induced maps go in the reverse direction.

The algebraic universal coefficient theorem applies also to relative cohomology since the relative chain groups \( {C}_{n}\left( {X, A}\right) \) are free, and there is a naturality statement: A map \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) induces a commutative diagram

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( {X, A}\right) , G}\right)  \rightarrow  {H}^{n}\left( {X, A;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( {X, A}\right) , G}\right)  \rightarrow  0
\]

\[
\uparrow  {\left( {f}_{ * }\right) }^{ * }\; \uparrow  {f}^{ * }
\]

\[
0 \rightarrow  \operatorname{Ext}\left( {{H}_{n - 1}\left( {Y, B}\right) , G}\right)  \rightarrow  {H}^{n}\left( {Y, B;G}\right) \overset{h}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{n}\left( {Y, B}\right) , G}\right)  \rightarrow  0
\]

This follows from the naturality of the algebraic universal coefficient sequences since the vertical maps are induced by the chain maps \( {f}_{\sharp } : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n}\left( {Y, B}\right) \) . When the subspaces \( A \) and \( B \) are empty we obtain the absolute forms of these results.

Homotopy Invariance. The statement is that if \( f \simeq  g : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) , then \( {f}^{ * } = \; {g}^{ * } : {H}^{n}\left( {Y, B}\right)  \rightarrow  {H}^{n}\left( {X, A}\right) \) . This is proved by direct dualization of the proof for homology. From the proof of Theorem 2.10 we have a chain homotopy \( P \) satisfying \( {g}_{\sharp } - {f}_{\sharp } = \partial P + P\partial \) . This relation dualizes to \( {g}^{\sharp } - {f}^{\sharp } = {P}^{ * }\delta  + \delta {P}^{ * } \) , so \( {P}^{ * } \) is a chain homotopy between the maps \( {f}^{\sharp },{g}^{\sharp } : {C}^{n}\left( {Y;G}\right)  \rightarrow  {C}^{n}\left( {X;G}\right) \) . This restricts also to a chain homotopy between \( {f}^{\sharp } \) and \( {g}^{\sharp } \) on relative cochains, the cochains vanishing on singular simplices in the subspaces \( B \) and \( A \) . Since \( {f}^{\sharp } \) and \( {g}^{\sharp } \) are chain homotopic, they induce the same homomorphism \( {f}^{ * } = {g}^{ * } \) on cohomology.

Excision. For cohomology this says that for subspaces \( Z \subset  A \subset  X \) with the closure of \( Z \) contained in the interior of \( A \) , the inclusion \( i : \left( {X - Z, A - Z}\right)  \hookrightarrow  \left( {X, A}\right) \) induces isomorphisms \( {i}^{ * } : {H}^{n}\left( {X, A;G}\right)  \rightarrow  {H}^{n}\left( {X - Z, A - Z;G}\right) \) for all \( n \) . This follows from the corresponding result for homology by the naturality of the universal coefficient theorem and the five-lemma. Alternatively, if one wishes to avoid appealing to the universal coefficient theorem, the proof of excision for homology dualizes easily to cohomology by the following argument. In the proof for homology there were chain maps \( \iota  : {C}_{n}\left( {A + B}\right)  \rightarrow  {C}_{n}\left( X\right) \) and \( \rho  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( {A + B}\right) \) such that \( {\rho \iota } = \mathbb{1} \) and \( \mathbb{1} - {\iota \rho } = \; \partial D + D\partial \) for a chain homotopy \( D \) . Dualizing by taking \( \operatorname{Hom}\left( {-, G}\right) \) , we have maps \( {\rho }^{ * } \) and \( {\iota }^{ * } \) between \( {C}^{n}\left( {A + B;G}\right) \) and \( {C}^{n}\left( {X;G}\right) \) , and these induce isomorphisms on cohomology since \( {\iota }^{ * }{\rho }^{ * } = \mathbb{1} \) and \( \mathbb{1} - {\rho }^{ * }{\iota }^{ * } = {D}^{ * }\delta  + \delta {D}^{ * } \) . By the five-lemma, the maps \( {C}^{n}\left( {X, A;G}\right)  \rightarrow  {C}^{n}\left( {A + B, A;G}\right) \) also induce isomorphisms on cohomology. There is an obvious identification of \( {C}^{n}\left( {A + B, A;G}\right) \) with \( {C}^{n}\left( {B, A \cap  B;G}\right) \) , so we get isomorphisms \( {H}^{n}\left( {X, A;G}\right) ) \approx  {H}^{n}\left( {B, A \cap  B;G}\right) \) induced by the inclusion \( \left( {B, A \cap  B}\right)  \hookrightarrow  \left( {X, A}\right) \) .

Axioms for Cohomology. These are exactly dual to the axioms for homology. Restricting attention to CW complexes again, a (reduced) cohomology theory is a sequence of contravariant functors \( {\widetilde{h}}^{n} \) from CW complexes to abelian groups, together with natural coboundary homomorphisms \( \delta  : {\widetilde{h}}^{n}\left( A\right)  \rightarrow  {\widetilde{h}}^{n + 1}\left( {X/A}\right) \) for CW pairs \( \left( {X, A}\right) \) , satisfying the following axioms:

(1) If \( f \simeq  g : X \rightarrow  Y \) , then \( {f}^{ * } = {g}^{ * } : {\widetilde{h}}^{n}\left( Y\right)  \rightarrow  {\widetilde{h}}^{n}\left( X\right) \) .

(2) For each CW pair \( \left( {X, A}\right) \) there is a long exact sequence

\[
\cdots \overset{\delta }{ \rightarrow  }{\widetilde{h}}^{n}\left( {X/A}\right) \overset{{q}^{ * }}{ \rightarrow  }{\widetilde{h}}^{n}\left( X\right) \overset{{i}^{ * }}{ \rightarrow  }{\widetilde{h}}^{n}\left( A\right) \overset{\delta }{ \rightarrow  }{\widetilde{h}}^{n + 1}\left( {X/A}\right) \overset{{q}^{ * }}{ \rightarrow  }\cdots
\]

where \( i \) is the inclusion and \( q \) is the quotient map.

(3) For a wedge sum \( X = \mathop{\bigvee }\limits_{\alpha }{X}_{\alpha } \) with inclusions \( {i}_{\alpha } : {X}_{\alpha } \hookrightarrow  X \) , the product map \( \mathop{\prod }\limits_{\alpha }{i}_{\alpha }^{ * } : {\widetilde{h}}^{n}\left( X\right)  \rightarrow  \mathop{\prod }\limits_{\alpha }{\widetilde{h}}^{n}\left( {X}_{\alpha }\right) \) is an isomorphism for each \( n \) .

We have already seen that the first axiom holds for singular cohomology. The second axiom follows from excision in the same way as for homology, via isomorphisms \( {\widetilde{H}}^{n}\left( {X/A;G}\right)  \approx  {H}^{n}\left( {X, A;G}\right) \) . Note that the third axiom involves direct product, rather than the direct sum appearing in the homology version. This is because of the natural isomorphism \( \operatorname{Hom}\left( {{\bigoplus }_{\alpha }{A}_{\alpha }, G}\right)  \approx  \mathop{\prod }\limits_{\alpha }\operatorname{Hom}\left( {{A}_{\alpha }, G}\right) \) , which implies that the cochain complex of a disjoint union \( \mathop{\coprod }\limits_{\alpha }{X}_{\alpha } \) is the direct product of the cochain complexes of the individual \( {X}_{\alpha } \) ’s, and this direct product splitting passes through to cohomology groups. The same argument applies in the relative case, so we get isomorphisms \( {H}^{n}\left( {\mathop{\coprod }\limits_{\alpha }{X}_{\alpha },\mathop{\coprod }\limits_{\alpha }{A}_{\alpha };G}\right)  \approx  \mathop{\prod }\limits_{\alpha }{H}^{n}\left( {{X}_{\alpha },{A}_{\alpha };G}\right) \) . The third axiom is obtained by taking the \( {A}_{\alpha } \) ’s to be basepoints \( {x}_{\alpha } \) and passing to the quotient \( \mathop{\coprod }\limits_{\alpha }{X}_{\alpha }/\mathop{\coprod }\limits_{\alpha }{x}_{\alpha } = \mathop{\bigvee }\limits_{\alpha }{X}_{\alpha } \) .

The relation between reduced and unreduced cohomology theories is the same as for homology, as described in \( \text{ § }{2.3} \) .

Simplicial Cohomology. If \( X \) is a \( \Delta \) -complex and \( A \subset  X \) is a subcomplex, then the simplicial chain groups \( {\Delta }_{n}\left( {X, A}\right) \) dualize to simplicial cochain groups \( {\Delta }^{n}\left( {X, A;G}\right)  = \; \operatorname{Hom}\left( {{\Delta }_{n}\left( {X, A}\right) , G}\right) \) , and the resulting cohomology groups are by definition the simplicial cohomology groups \( {H}_{\Delta }^{n}\left( {X, A;G}\right) \) . Since the inclusions \( {\Delta }_{n}\left( {X, A}\right)  \subset  {C}_{n}\left( {X, A}\right) \) induce isomorphisms \( {H}_{n}^{\Delta }\left( {X, A}\right)  \approx  {H}_{n}\left( {X, A}\right) \) , Corollary 3.4 implies that the dual maps \( {C}^{n}\left( {X, A;G}\right)  \rightarrow  {\Delta }^{n}\left( {X, A;G}\right) \) also induce isomorphisms \( {H}^{n}\left( {X, A;G}\right)  \approx  {H}_{\Delta }^{n}\left( {X, A;G}\right) \) .

Cellular Cohomology. For a CW complex \( X \) this is defined via the cellular cochain complex formed by the horizontal sequence in the following diagram, where coefficients in a given group \( G \) are understood, and the cellular coboundary maps \( {d}_{n} \) are the compositions \( {\delta }_{n}{j}_{n} \) , making the triangles commute. Note that \( {d}_{n}{d}_{n - 1} = 0 \) since

![bo_d7dtv0s91nqc73eq8nv0_211_213_204_1365_549_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_211_213_204_1365_549_0.jpg)

Theorem 3.5. \( {H}^{n}\left( {X;G}\right)  \approx  \operatorname{Ker}{d}_{n}/\operatorname{Im}{d}_{n - 1} \) . Furthermore, the cellular cochain complex \( \left\{  {{H}^{n}\left( {{X}^{n},{X}^{n - 1};G}\right) ,{d}_{n}}\right\} \) is isomorphic to the dual of the cellular chain complex, obtained by applying \( \operatorname{Hom}\left( {-, G}\right) \) .

Proof: The universal coefficient theorem implies that \( {H}^{k}\left( {{X}^{n},{X}^{n - 1};G}\right)  = 0 \) for \( k \neq  n \) . The long exact sequence of the pair \( \left( {{X}^{n},{X}^{n - 1}}\right) \) then gives isomorphisms \( {H}^{k}\left( {{X}^{n};G}\right)  \approx \; {H}^{k}\left( {{X}^{n - 1};G}\right) \) for \( k \neq  n, n - 1 \) . Hence by induction on \( n \) we obtain \( {H}^{k}\left( {{X}^{n};G}\right)  = 0 \) if \( k > n \) . Thus the diagonal sequences in the preceding diagram are exact. The universal coefficient theorem also gives \( {H}^{k}\left( {X,{X}^{n + 1};G}\right)  = 0 \) for \( k \leq  n + 1 \) , so \( {H}^{n}\left( {X;G}\right)  \approx \; {H}^{n}\left( {{X}^{n + 1};G}\right) \) . The diagram then yields isomorphisms

\[
{H}^{n}\left( {X;G}\right)  \approx  {H}^{n}\left( {{X}^{n + 1};G}\right)  \approx  \operatorname{Ker}{\delta }_{n} \approx  \operatorname{Ker}{d}_{n}/\operatorname{Im}{\delta }_{n - 1} \approx  \operatorname{Ker}{d}_{n}/\operatorname{Im}{d}_{n - 1}
\]

For the second statement in the theorem we have the diagram

\[
{H}^{k}\left( {{X}^{k},{X}^{k - 1};G}\right)  \rightarrow  {H}^{k}\left( {{X}^{k};G}\right)  \rightarrow  {H}^{k + 1}\left( {{X}^{k + 1},{X}^{k};G}\right)
\]

\[
\left| \begin{array}{llll} h & & & \\   & & & \\   & & &  \end{array}\right| h
\]

\[
\operatorname{Hom}\left( {{H}_{k}\left( {{X}^{k},{X}^{k - 1}}\right) , G}\right)  \rightarrow  \operatorname{Hom}\left( {{H}_{k}\left( {X}^{k}\right) , G}\right) \overset{{\partial }^{ * }}{ \rightarrow  }\operatorname{Hom}\left( {{H}_{k + 1}\left( {{X}^{k + 1},{X}^{k}}\right) , G}\right)
\]

The cellular coboundary map is the composition across the top, and we want to see that this is the same as the composition across the bottom. The first and third vertical maps are isomorphisms by the universal coefficient theorem, so it suffices to show the diagram commutes. The first square commutes by naturality of \( h \) , and commutativity of the second square was shown in the discussion of the long exact sequence of cohomology groups of a pair \( \left( {X, A}\right) \) .

Mayer-Vietoris Sequences. In the absolute case these take the form

\[
\cdots  \rightarrow  {H}^{n}\left( {X;G}\right) \overset{\Psi }{ \rightarrow  }{H}^{n}\left( {A;G}\right)  \oplus  {H}^{n}\left( {B;G}\right) \overset{\Phi }{ \rightarrow  }{H}^{n}\left( {A \cap  B;G}\right)  \rightarrow  {H}^{n + 1}\left( {X;G}\right)  \rightarrow  \cdots
\]

where \( X \) is the union of the interiors of \( A \) and \( B \) . This is the long exact sequence associated to the short exact sequence of cochain complexes

\[
0 \rightarrow  {C}^{n}\left( {A + B;G}\right) \overset{\psi }{ \rightarrow  }{C}^{n}\left( {A;G}\right)  \oplus  {C}^{n}\left( {B;G}\right) \overset{\varphi }{ \rightarrow  }{C}^{n}\left( {A \cap  B;G}\right)  \rightarrow  0
\]

Here \( {C}^{n}\left( {A + B;G}\right) \) is the dual of the subgroup \( {C}_{n}\left( {A + B}\right)  \subset  {C}_{n}\left( X\right) \) consisting of sums of singular \( n \) -simplices lying in \( A \) or in \( B \) . The inclusion \( {C}_{n}\left( {A + B}\right)  \subset  {C}_{n}\left( X\right) \) is a chain homotopy equivalence by Proposition 2.21, so the dual restriction map \( {C}^{n}\left( {X;G}\right)  \rightarrow  {C}^{n}\left( {A + B;G}\right) \) is also a chain homotopy equivalence, hence induces an isomorphism on cohomology as shown in the discussion of excision a couple pages back. The map \( \psi \) has coordinates the two restrictions to \( A \) and \( B \) , and \( \varphi \) takes the difference of the restrictions to \( A \cap  B \) , so it is obvious that \( \varphi \) is onto with kernel the image of \( \psi \) .

There is a relative Mayer-Vietoris sequence

\[
\cdots  \rightarrow  {H}^{n}\left( {X, Y;G}\right)  \rightarrow  {H}^{n}\left( {A, C;G}\right)  \oplus  {H}^{n}\left( {B, D;G}\right)  \rightarrow  {H}^{n}\left( {A \cap  B, C \cap  D;G}\right)  \rightarrow  \cdots
\]

for a pair \( \left( {X, Y}\right)  = \left( {A \cup  B, C \cup  D}\right) \) with \( C \subset  A \) and \( D \subset  B \) such that \( X \) is the union of the interiors of \( A \) and \( B \) while \( Y \) is the union of the interiors of \( C \) and \( D \) . To derive this, consider first the map of short exact sequences of cochain complexes

![bo_d7dtv0s91nqc73eq8nv0_212_334_919_1129_154_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_212_334_919_1129_154_0.jpg)

Here \( {C}^{n}\left( {A + B, C + D;G}\right) \) is defined as the kernel of \( {C}^{n}\left( {A + B;G}\right)  \rightarrow  {C}^{n}\left( {C + D;G}\right) \) , the restriction map, so the second sequence is exact. The vertical maps are restrictions. The second and third of these induce isomorphisms on cohomology, as we have seen, so by the five-lemma the first vertical map also induces isomorphisms on cohomology. The relative Mayer-Vietoris sequence is then the long exact sequence associated to the short exact sequence of cochain complexes

\[
0 \rightarrow  {C}^{n}\left( {A + B, C + D;G}\right) \overset{\psi }{ \rightarrow  }{C}^{n}\left( {A, C;G}\right)  \oplus  {C}^{n}\left( {B, D;G}\right) \overset{\varphi }{ \rightarrow  }{C}^{n}\left( {A \cap  B, C \cap  D;G}\right)  \rightarrow  0
\]

This is exact since it is the dual of the short exact sequence

\[
0 \rightarrow  {C}_{n}\left( {A \cap  B, C \cap  D}\right)  \rightarrow  {C}_{n}\left( {A, C}\right)  \oplus  {C}_{n}\left( {B, D}\right)  \rightarrow  {C}_{n}\left( {A + B, C + D}\right)  \rightarrow  0
\]

constructed in \( \text{ § }{2.2} \) , which splits since \( {C}_{n}\left( {A + B, C + D}\right) \) is free with basis the singular \( n \) -simplices in \( A \) or in \( B \) that do not lie in \( C \) or in \( D \) .

## Exercises

1. Show that \( \operatorname{Ext}\left( {H, G}\right) \) is a contravariant functor of \( H \) for fixed \( G \) , and a covariant functor of \( G \) for fixed \( H \) .

2. Show that the maps \( G\overset{n}{ \rightarrow  }G \) and \( H\overset{n}{ \rightarrow  }H \) multiplying each element by the integer \( n \) induce multiplication by \( n \) in \( \operatorname{Ext}\left( {H, G}\right) \) .

3. Regarding \( {\mathbb{Z}}_{2} \) as a module over the ring \( {\mathbb{Z}}_{4} \) , construct a resolution of \( {\mathbb{Z}}_{2} \) by free modules over \( {\mathbb{Z}}_{4} \) and use this to show that \( {\operatorname{Ext}}_{{\mathbb{Z}}_{4}}^{n}\left( {{\mathbb{Z}}_{2},{\mathbb{Z}}_{2}}\right) \) is nonzero for all \( n \) .

4. What happens if one defines homology groups \( {h}_{n}\left( {X;G}\right) \) as the homology groups of the chain complex \( \cdots  \rightarrow  \operatorname{Hom}\left( {G,{C}_{n}\left( X\right) }\right)  \rightarrow  \operatorname{Hom}\left( {G,{C}_{n - 1}\left( X\right) }\right)  \rightarrow  \cdots \) ? More specifically, what are the groups \( {h}_{n}\left( {X;G}\right) \) when \( G = \mathbb{Z},{\mathbb{Z}}_{m} \) , and \( \mathbb{Q} \) ?

5. Regarding a cochain \( \varphi  \in  {C}^{1}\left( {X;G}\right) \) as a function from paths in \( X \) to \( G \) , show that if \( \varphi \) is a cocycle, then

(a) \( \varphi \left( {f \cdot  g}\right)  = \varphi \left( f\right)  + \varphi \left( g\right) \) ,

(b) \( \varphi \) takes the value 0 on constant paths,

(c) \( \varphi \left( f\right)  = \varphi \left( g\right) \) if \( f \simeq  g \) ,

(d) \( \varphi \) is a coboundary iff \( \varphi \left( f\right) \) depends only on the endpoints of \( f \) , for all \( f \) .

[In particular,(a) and (c) give a map \( {H}^{1}\left( {X;G}\right)  \rightarrow  \operatorname{Hom}\left( {{\pi }_{1}\left( X\right) , G}\right) \) , which the universal coefficient theorem says is an isomorphism if \( X \) is path-connected.]

6. (a) Directly from the definitions, compute the simplicial cohomology groups of \( {S}^{1} \times  {S}^{1} \) with \( \mathbb{Z} \) and \( {\mathbb{Z}}_{2} \) coefficients, using the \( \Delta \) -complex structure given in \( \text{ § }{2.1} \) .

(b) Do the same for \( {\mathbb{{RP}}}^{2} \) and the Klein bottle.

7. Show that the functors \( {h}^{n}\left( X\right)  = \operatorname{Hom}\left( {{H}_{n}\left( X\right) ,\mathbb{Z}}\right) \) do not define a cohomology theory on the category of CW complexes.

8. Many basic homology arguments work just as well for cohomology even though maps go in the opposite direction. Verify this in the following cases:

(a) Compute \( {H}^{i}\left( {{S}^{n};G}\right) \) by induction on \( n \) in two ways: using the long exact sequence of a pair, and using the Mayer-Vietoris sequence.

(b) Show that if \( A \) is a closed subspace of \( X \) that is a deformation retract of some neighborhood, then the quotient map \( X \rightarrow  X/A \) induces isomorphisms \( {H}^{n}\left( {X, A;G}\right)  \approx \; {\widetilde{H}}^{n}\left( {X/A;G}\right) \) for all \( n \) .

(c) Show that if \( A \) is a retract of \( X \) then \( {H}^{n}\left( {X;G}\right)  \approx  {H}^{n}\left( {A;G}\right)  \oplus  {H}^{n}\left( {X, A;G}\right) \) .

9. Show that if \( f : {S}^{n} \rightarrow  {S}^{n} \) has degree \( d \) then \( {f}^{ * } : {H}^{n}\left( {{S}^{n};G}\right)  \rightarrow  {H}^{n}\left( {{S}^{n};G}\right) \) is multiplication by \( d \) .

10. For the lens space \( {L}_{m}\left( {{\ell }_{1},\cdots ,{\ell }_{n}}\right) \) defined in Example 2.43, compute the cohomology groups using the cellular cochain complex and taking coefficients in \( \mathbb{Z},\mathbb{Q},{\mathbb{Z}}_{m} \) , and \( {\mathbb{Z}}_{p} \) for \( p \) prime. Verify that the answers agree with those given by the universal coefficient theorem.

11. Let \( X \) be a Moore space \( M\left( {{\mathbb{Z}}_{m}, n}\right) \) obtained from \( {S}^{n} \) by attaching a cell \( {e}^{n + 1} \) by a map of degree \( m \) .

(a) Show that the quotient map \( X \rightarrow  X/{S}^{n} = {S}^{n + 1} \) induces the trivial map on \( {\widetilde{H}}_{i}\left( {-;\mathbb{Z}}\right) \) for all \( i \) , but not on \( {H}^{n + 1}\left( {-;\mathbb{Z}}\right) \) . Deduce that the splitting in the universal coefficient theorem for cohomology cannot be natural.

(b) Show that the inclusion \( {S}^{n} \hookrightarrow  X \) induces the trivial map on \( {\widetilde{H}}^{i}\left( {-;\mathbb{Z}}\right) \) for all \( i \) , but not on \( {H}_{n}\left( {-;\mathbb{Z}}\right) \) .

12. Show \( {H}^{k}\left( {X,{X}^{n};G}\right)  = 0 \) if \( X \) is a CW complex and \( k \leq  n \) , by using the cohomology version of the second proof of the corresponding result for homology in Lemma 2.34. 13. Let \( \langle X, Y\rangle \) denote the set of basepoint-preserving homotopy classes of basepoint-preserving maps \( X \rightarrow  Y \) . Using Proposition 1B.9, show that if \( X \) is a connected CW complex and \( G \) is an abelian group, then the map \( \langle X, K\left( {G,1}\right) \rangle  \rightarrow  {H}^{1}\left( {X;G}\right) \) sending a map \( f : X \rightarrow  K\left( {G,1}\right) \) to the induced homomorphism \( {f}_{ * } : {H}_{1}\left( X\right)  \rightarrow  {H}_{1}\left( {K\left( {G,1}\right) }\right)  \approx  G \) is a bijection, where we identify \( {H}^{1}\left( {X;G}\right) \) with \( \operatorname{Hom}\left( {{H}_{1}\left( X\right) , G}\right) \) via the universal coefficient theorem.
